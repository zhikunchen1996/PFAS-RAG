from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

import common
import build_final_resolution_v1 as final_resolution


FINAL_LEDGERS = (
    common.PACKAGE
    / "reference_build/revisions/model_a_ledgers_resolution3.jsonl"
)
AUDIT_DIR = common.PACKAGE / "project_author_audit_v1"
REVIEW_FILES = [
    common.PACKAGE / "reference_build/reviews/model_b_reviews_v1.jsonl",
    common.PACKAGE
    / "reference_build/reviews/model_b_reviews_v1_rereview1.jsonl",
    common.PACKAGE
    / "reference_build/reviews/model_b_reviews_v1_rereview2.jsonl",
    common.PACKAGE
    / "reference_build/reviews/model_b_reviews_v1_rereview3.jsonl",
    common.PACKAGE
    / "reference_build/reviews/model_b_reviews_v1_verbatim_review.jsonl",
    common.PACKAGE
    / "reference_build/reviews/model_b_reviews_v1_content_review.jsonl",
]
FORBIDDEN_MODEL_VISIBLE_KEYS = {
    "gold_minimal_answer",
    "gold_full_answer",
    "supported_claim",
    "candidate_answer",
    "retrieved_context",
    "system_identity",
    "test40_result",
}


def walk_keys(value: Any) -> set[str]:
    keys: set[str] = set()
    if isinstance(value, dict):
        keys.update(value)
        for child in value.values():
            keys.update(walk_keys(child))
    elif isinstance(value, list):
        for child in value:
            keys.update(walk_keys(child))
    return keys


def assert_candidate_blind_flags(value: Any, path: Path) -> None:
    if isinstance(value, dict):
        if value.get("candidate_test40_inputs_used") is not None:
            if value["candidate_test40_inputs_used"] is not False:
                raise RuntimeError(f"{path}: candidate-test input flag is not false")
        for child in value.values():
            assert_candidate_blind_flags(child, path)
    elif isinstance(value, list):
        for child in value:
            assert_candidate_blind_flags(child, path)


def main() -> None:
    packets = {
        row["question_id"]: row for row in common.read_jsonl(common.REFERENCE_PACKETS)
    }
    ledgers = {
        row["question_id"]: row for row in common.read_jsonl(FINAL_LEDGERS)
    }
    if len(packets) != 40 or set(ledgers) != set(packets):
        raise RuntimeError("Expected exactly 40 matching Test40 packets and ledgers")
    forbidden = set()
    for packet in packets.values():
        forbidden.update(walk_keys(packet) & FORBIDDEN_MODEL_VISIBLE_KEYS)
    if forbidden:
        raise RuntimeError(f"Forbidden model-visible keys found: {sorted(forbidden)}")

    latest_reviews = {}
    for path in REVIEW_FILES:
        for review in common.read_jsonl(path):
            latest_reviews[review["question_id"]] = review
    if set(latest_reviews) != set(packets):
        raise RuntimeError("Latest review coverage differs from Test40 membership")
    if any(review["verdict"] != "clean" for review in latest_reviews.values()):
        raise RuntimeError("At least one latest independent review is not clean")

    new_span_count = 0
    for qid, row in ledgers.items():
        ledger = row["draft_ledger"]
        final_resolution.validate_with_documented_component_amendment(
            ledger, packets[qid], qid
        )
        evidence = {
            item["evidence_id"]: item
            for item in packets[qid]["approved_source_evidence"]
        }
        group_ids = [
            group["claim_group_id"]
            for group in ledger["claim_groups"] + ledger["constraint_groups"]
        ]
        if len(group_ids) != len(set(group_ids)):
            raise RuntimeError(f"{qid}: duplicate claim-group ID")
        for group in ledger["claim_groups"] + ledger["constraint_groups"]:
            for span in group.get("exact_spans", []):
                source = evidence[span["evidence_id"]]
                if span["exact_evidence_span"] not in source["full_chunk_text"]:
                    raise RuntimeError(
                        f"{qid} {group['claim_group_id']}: non-verbatim exact span"
                    )
                registered = [source["exact_evidence_span"]] + list(
                    source.get("unit_exact_spans", [])
                )
                if span["exact_evidence_span"] not in registered:
                    new_span_count += 1

    audit_manifest_path = AUDIT_DIR / "build_manifest.json"
    audit_manifest = json.loads(audit_manifest_path.read_text(encoding="utf-8"))
    expected_hashes = {
        "ledgers_sha256": FINAL_LEDGERS,
        "source_packets_sha256": common.REFERENCE_PACKETS,
        "reference_candidates_sha256": AUDIT_DIR / "reference_candidates.jsonl",
        "decision_register_sha256": AUDIT_DIR / "decision_register.csv",
        "new_full_chunk_span_register_sha256": (
            AUDIT_DIR / "new_full_chunk_span_register.csv"
        ),
        "audit_packet_sha256": AUDIT_DIR / "AUTHOR_AUDIT_PACKET.md",
        "readme_sha256": AUDIT_DIR / "README.md",
    }
    for field, path in expected_hashes.items():
        if audit_manifest[field] != common.sha256(path):
            raise RuntimeError(f"Audit manifest hash mismatch: {field}")
    if audit_manifest["new_full_chunk_span_count"] != new_span_count:
        raise RuntimeError("Audit new-span count differs from final ledgers")

    with (AUDIT_DIR / "decision_register.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        decisions = list(csv.DictReader(handle))
    if len(decisions) != 40:
        raise RuntimeError("Project-author decision register must contain 40 rows")
    if any(row["project_author_decision"] != "pending" for row in decisions):
        raise RuntimeError("Unexpected non-pending project-author decision")

    for path in common.PACKAGE.rglob("*.json"):
        value = json.loads(path.read_text(encoding="utf-8"))
        assert_candidate_blind_flags(value, path)
    for path in common.PACKAGE.rglob("*.jsonl"):
        for value in common.read_jsonl(path):
            assert_candidate_blind_flags(value, path)

    print(
        json.dumps(
            {
                "status": "PASS",
                "question_count": len(ledgers),
                "latest_clean_reviews": len(latest_reviews),
                "nonverbatim_exact_spans": 0,
                "new_full_chunk_spans_pending_author_audit": new_span_count,
                "project_author_decisions": "40 pending",
                "candidate_test40_inputs_used": False,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

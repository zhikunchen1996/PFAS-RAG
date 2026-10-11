from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import build_human_audit_v2 as audit
import common
import run_reference_group_verification_v2 as verification
import run_reference_revision_v2 as revision


def validate_human_gate(
    candidate: dict[str, Any],
    packet: dict[str, Any],
    original_draft: dict[str, Any],
    model_b_row: dict[str, Any],
) -> None:
    qid = packet["question_id"]
    review = model_b_row["review"]
    if not verification.review_is_clean(review):
        raise RuntimeError(f"{qid}: Model B final review is not clean")
    if candidate.get("model_b_review_sha256") != common.payload_sha256(review):
        raise RuntimeError(f"{qid}: Model B review hash mismatch")
    if candidate.get("question_text") != packet["question"]["question_text"]:
        raise RuntimeError(f"{qid}: question text changed")
    if candidate.get("task_boundaries") != packet["task_boundaries"]:
        raise RuntimeError(f"{qid}: task boundaries changed")
    expected_revision_hash = model_b_row["revision_sha256"]
    if candidate.get("model_b_reviewed_revision_sha256") != expected_revision_hash:
        raise RuntimeError(f"{qid}: reviewed revision hash field differs")
    if common.payload_sha256(candidate["approved_ledger"]) != expected_revision_hash:
        raise RuntimeError(
            f"{qid}: ledger changed after Model B verification; re-review required"
        )
    revision.validate_revision(
        candidate["approved_ledger"],
        packet,
        {
            "question_id": qid,
            "task_components": candidate["approved_ledger"]["task_components"],
        },
        original_draft,
    )
    checks = candidate.get("project_author_checks", {})
    required_checks = {
        "task_components_approved",
        "all_claim_groups_reviewed",
        "atomic_dispositions_reviewed",
        "prose_ledger_consistent",
        "all_model_b_issues_resolved",
    }
    if set(checks) != required_checks or not all(
        checks.get(key) is True for key in required_checks
    ):
        raise RuntimeError(f"{qid}: project-author checklist is incomplete")
    human = candidate.get("human_review", {})
    if human.get("decision") != "approve":
        raise RuntimeError(f"{qid}: project-author decision is not approve")
    if human.get("reviewer_role") != "project_author":
        raise RuntimeError(f"{qid}: reviewer role is not project_author")
    if not str(human.get("review_date", "")).strip():
        raise RuntimeError(f"{qid}: human review date is missing")
    if not str(human.get("resolution_notes", "")).strip():
        raise RuntimeError(f"{qid}: human resolution notes are missing")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidates")
    parser.add_argument("--packets")
    parser.add_argument("--audit-manifest")
    parser.add_argument("--output-dir")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    candidates_path = (
        Path(args.candidates).expanduser().resolve()
        if args.candidates
        else audit.CANDIDATES
    )
    packets_path = (
        Path(args.packets).expanduser().resolve()
        if args.packets
        else common.PACKETS
    )
    audit_manifest_path = (
        Path(args.audit_manifest).expanduser().resolve()
        if args.audit_manifest
        else candidates_path.parent / "build_manifest.json"
    )
    output_dir = (
        Path(args.output_dir).expanduser().resolve()
        if args.output_dir
        else common.PACKAGE / "frozen"
    )
    output = output_dir / "reference_claim_ledgers_v2.jsonl"
    manifest_path = output_dir / "freeze_manifest_v2.json"
    if (output.exists() or manifest_path.exists()) and not args.force:
        raise RuntimeError(
            "V2 frozen references already exist; use a new output directory "
            "or pass --force only for an explicitly authorized rebuild"
        )
    required = [
        candidates_path,
        packets_path,
        common.DRAFTS,
        audit_manifest_path,
        common.PACKAGE / "protocol.json",
    ]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise RuntimeError(f"Missing V2 freeze inputs: {missing}")

    packets = {
        row["question_id"]: row for row in common.read_jsonl(packets_path)
    }
    original_drafts = {
        row["question_id"]: row["draft"]
        for row in common.read_jsonl(common.DRAFTS)
    }
    audit_manifest = json.loads(
        audit_manifest_path.read_text(encoding="utf-8")
    )
    if (
        audit_manifest.get("reference_candidates_sha256")
        != common.sha256(candidates_path)
    ):
        raise RuntimeError("Human-audit candidate hash mismatch")
    decision_register_path = candidates_path.parent / "decision_register.csv"
    if audit_manifest.get("decision_register_sha256") and (
        audit_manifest["decision_register_sha256"]
        != common.sha256(decision_register_path)
    ):
        raise RuntimeError("Human-audit decision-register hash mismatch")
    reviews_path = common.ROOT / audit_manifest["model_b_reviews_file"]
    revisions_path = common.ROOT / audit_manifest["revisions_file"]
    if common.sha256(reviews_path) != audit_manifest["model_b_reviews_sha256"]:
        raise RuntimeError("Human-audit Model B review hash mismatch")
    if common.sha256(revisions_path) != audit_manifest["revisions_sha256"]:
        raise RuntimeError("Human-audit revision hash mismatch")
    reviews = {
        row["question_id"]: row
        for row in common.read_jsonl(reviews_path)
    }
    candidates = {
        row["question_id"]: row
        for row in common.read_jsonl(candidates_path)
    }
    if not (set(packets) == set(original_drafts) == set(reviews) == set(candidates)):
        raise RuntimeError("V2 freeze input question membership differs")

    frozen = []
    for qid in packets:
        candidate = candidates[qid]
        validate_human_gate(
            candidate,
            packets[qid],
            original_drafts[qid],
            reviews[qid],
        )
        frozen.append(
            {
                "question_id": qid,
                "question_text": candidate["question_text"],
                "task_boundaries": candidate["task_boundaries"],
                "gold_is_non_exhaustive": True,
                "ledger_is_normative": True,
                "reference_prose_is_non_normative": True,
                "ledger": candidate["approved_ledger"],
                "human_review": candidate["human_review"],
                "provenance": {
                    "packet_sha256": common.payload_sha256(packets[qid]),
                    "model_b_review_sha256": common.payload_sha256(
                        reviews[qid]["review"]
                    ),
                    "approved_ledger_sha256": common.payload_sha256(
                        candidate["approved_ledger"]
                    ),
                },
            }
        )

    common.write_jsonl(output, frozen)
    manifest = {
        "freeze_id": "l3_gold_reference_dev13_v2",
        "freeze_date_utc": datetime.now(timezone.utc).isoformat(),
        "question_count": len(frozen),
        "status": "frozen_dev13_reference_claim_ledgers",
        "normative_scoring_source": str(output.relative_to(common.ROOT)),
        "normative_scoring_source_sha256": common.sha256(output),
        "protocol_sha256": common.sha256(common.PACKAGE / "protocol.json"),
        "prompt_hashes": {
            path.name: common.sha256(path)
            for path in sorted((common.PACKAGE / "prompts").glob("*_v2.txt"))
        },
        "source_hashes": {
            str(common.QUESTIONS.relative_to(common.ROOT)): common.sha256(
                common.QUESTIONS
            ),
            str(common.GOLD.relative_to(common.ROOT)): common.sha256(common.GOLD),
            str(common.BOUNDARIES.relative_to(common.ROOT)): common.sha256(
                common.BOUNDARIES
            ),
            str(revision.TASK_COMPONENTS.relative_to(common.ROOT)): common.sha256(
                revision.TASK_COMPONENTS
            ),
        },
        "construction_hashes": {
            "reference_packets": common.sha256(packets_path),
            "model_a_revisions_v2": common.sha256(revision.OUTPUT),
            "model_a_final_revisions_v2": common.sha256(revisions_path),
            "model_b_group_reviews_v2": common.sha256(reviews_path),
            "human_reference_candidates_v2": common.sha256(candidates_path),
            "human_audit_manifest_v2": common.sha256(audit_manifest_path),
            "human_decision_register_v2": common.sha256(
                decision_register_path
            ),
        },
        "candidate_answers_seen_during_reference_construction": False,
        "test40_l3_evaluated": False,
        "binary_pass_threshold": None,
        "binary_pass_status": "not_calibrated",
    }
    approval_record = candidates_path.parent / "project_author_approval_record.json"
    if approval_record.exists():
        manifest["construction_hashes"][
            "project_author_approval_record"
        ] = common.sha256(approval_record)
    common.write_json(manifest_path, manifest)
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()

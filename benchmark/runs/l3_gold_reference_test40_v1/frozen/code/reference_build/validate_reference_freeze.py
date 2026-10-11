from __future__ import annotations

import csv
import json

import common
import build_final_resolution_v1 as final_resolution


FROZEN = common.PACKAGE / "frozen"


def read_csv(path):
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    manifest_path = FROZEN / "freeze_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    recorded_manifest_hash = (FROZEN / "freeze_manifest.sha256").read_text(
        encoding="utf-8"
    ).split()[0]
    if recorded_manifest_hash != common.sha256(manifest_path):
        raise RuntimeError("Freeze manifest self-hash differs")
    if manifest["status"] != "FROZEN":
        raise RuntimeError("Freeze status is not FROZEN")
    for relative, expected in manifest["files"].items():
        path = common.ROOT / relative
        if not path.is_file() or common.sha256(path) != expected:
            raise RuntimeError(f"Frozen artifact hash differs: {relative}")

    questions = read_csv(FROZEN / "inputs/questions_test40.csv")
    gold = common.read_jsonl(FROZEN / "inputs/gold_test40.jsonl")
    packets = {
        row["question_id"]: row
        for row in common.read_jsonl(FROZEN / "inputs/reference_packets_test40.jsonl")
    }
    ledgers = {
        row["question_id"]: row
        for row in common.read_jsonl(
            FROZEN / "reference_claim_ledgers_test40_v1.jsonl"
        )
    }
    qids = {row["question_id"] for row in questions}
    if len(questions) != 40 or len(gold) != 189 or set(packets) != qids or set(
        ledgers
    ) != qids:
        raise RuntimeError("Frozen Test40 membership/count differs")
    nonverbatim = 0
    for qid in qids:
        ledger = ledgers[qid]["draft_ledger"]
        final_resolution.validate_with_documented_component_amendment(
            ledger, packets[qid], qid
        )
        evidence = {
            row["evidence_id"]: row for row in packets[qid]["approved_source_evidence"]
        }
        for group in ledger["claim_groups"] + ledger["constraint_groups"]:
            for span in group.get("exact_spans", []):
                if (
                    span["exact_evidence_span"]
                    not in evidence[span["evidence_id"]]["full_chunk_text"]
                ):
                    nonverbatim += 1
    if nonverbatim:
        raise RuntimeError(f"Frozen ledger contains {nonverbatim} non-verbatim spans")

    reviews = common.read_jsonl(
        FROZEN / "reviews/latest_clean_claude_reviews.jsonl"
    )
    if len(reviews) != 40 or any(row["verdict"] != "clean" for row in reviews):
        raise RuntimeError("Frozen independent reviews are not 40/40 clean")
    decisions = read_csv(FROZEN / "author/decision_register.csv")
    spans = read_csv(FROZEN / "author/new_span_decision_register.csv")
    if len(decisions) != 40 or any(
        row["project_author_decision"] != "approve" for row in decisions
    ):
        raise RuntimeError("Frozen author decision register is incomplete")
    if len(spans) != 165 or any(row["audit_decision"] != "approve" for row in spans):
        raise RuntimeError("Frozen new-span approval register is incomplete")

    approval = json.loads(
        (FROZEN / "author/project_author_approval_record.json").read_text(
            encoding="utf-8"
        )
    )
    if approval["decision"] != "approve" or approval[
        "manual_per_question_review_claimed"
    ] or approval["manual_per_span_review_claimed"]:
        raise RuntimeError("Frozen project-author approval record is inconsistent")

    summary = read_csv(FROZEN / "l15_validation/summary/summary.csv")[0]
    if (
        summary["question_count"] != "40"
        or summary["applicable_question_count"] != "40"
        or summary["cited_claim_count"] != "172"
        or float(summary["claim_supported_by_any_citation_rate"]) != 1.0
        or float(summary["unsupported_claim_rate"]) != 0.0
        or float(summary["contradicted_claim_rate"]) != 0.0
        or summary["questions_with_no_unsupported_or_contradicted_cited_claims"]
        != "40"
        or summary["uncited_source_dependent_claim_count"] != "0"
    ):
        raise RuntimeError("Frozen L1.5 summary no longer passes")
    if manifest["candidate_test40_inputs_used"] is not False or manifest[
        "formal_test40_l3_scoring_run"
    ] is not False:
        raise RuntimeError("Frozen held-out boundary flags differ")

    print(
        json.dumps(
            {
                "status": "PASS",
                "release_id": manifest["release_id"],
                "files_verified": len(manifest["files"]),
                "questions": 40,
                "gold_records": 189,
                "latest_clean_reviews": 40,
                "l15_claims_passed": "172/172",
                "author_approval_mode": approval["approval_mode"],
                "candidate_test40_inputs_used": False,
                "formal_test40_l3_scoring_run": False,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

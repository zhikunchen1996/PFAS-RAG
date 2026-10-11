from __future__ import annotations

import json

import common
import run_reference_drafts as drafts
import run_reference_repairs_v1 as repairs


SOURCE = common.PACKAGE / "reference_build/revisions/model_a_ledgers_repair1.jsonl"
REVIEWS = common.PACKAGE / "reference_build/reviews/model_b_reviews_v1.jsonl"
OUTPUT = common.PACKAGE / "reference_build/revisions/model_a_ledgers_repair2.jsonl"


def main() -> None:
    packets = {
        row["question_id"]: row for row in common.read_jsonl(common.REFERENCE_PACKETS)
    }
    source = {row["question_id"]: row for row in common.read_jsonl(SOURCE)}
    review = {row["question_id"]: row for row in common.read_jsonl(REVIEWS)}
    repaired = {row["question_id"]: row for row in common.read_jsonl(repairs.OUTPUT)}
    expected_repairs = {
        qid for qid, row in review.items() if row["verdict"] == "repair_required"
    }
    if set(repaired) != expected_repairs:
        raise RuntimeError("Repair membership differs from Claude repair-required set")

    output_rows = []
    for packet in common.read_jsonl(common.REFERENCE_PACKETS):
        qid = packet["question_id"]
        if qid in repaired:
            row = repaired[qid]
            if row["source_ledger_sha256"] != common.payload_sha256(
                source[qid]["draft_ledger"]
            ):
                raise RuntimeError(f"{qid}: repair source ledger hash differs")
            if row["model_b_review_sha256"] != common.payload_sha256(review[qid]):
                raise RuntimeError(f"{qid}: repair review hash differs")
            ledger = row["repaired_ledger"]
            provenance = {
                "status": "repaired_after_model_b_v1",
                "source_ledger_sha256": row["source_ledger_sha256"],
                "model_b_review_sha256": row["model_b_review_sha256"],
                "repair_response_id": row["generation"]["response_id"],
                "structural_normalizations": row.get(
                    "structural_normalizations", []
                ),
            }
            generation = row["generation"]
        else:
            ledger = source[qid]["draft_ledger"]
            provenance = {
                "status": "unchanged_after_clean_model_b_v1_review",
                "source_ledger_sha256": common.payload_sha256(ledger),
                "model_b_review_sha256": common.payload_sha256(review[qid]),
            }
            generation = source[qid]["generation"]
        drafts.validate(ledger, packets[qid])
        output_rows.append(
            {
                "question_id": qid,
                "reference_packet_sha256": common.payload_sha256(packets[qid]),
                "draft_ledger": ledger,
                "revision_provenance": provenance,
                "generation": generation,
            }
        )

    common.write_jsonl(OUTPUT, output_rows)
    manifest = {
        "stage": "Test40 canonical ledger repair2 assembly",
        "question_count": len(output_rows),
        "unchanged_clean_count": len(output_rows) - len(repaired),
        "repaired_count": len(repaired),
        "source_sha256": common.sha256(SOURCE),
        "model_b_reviews_sha256": common.sha256(REVIEWS),
        "repairs_sha256": common.sha256(repairs.OUTPUT),
        "output_sha256": common.sha256(OUTPUT),
        "candidate_test40_inputs_used": False,
    }
    common.write_json(
        common.PACKAGE / "reference_build/revisions/repair2_manifest.json",
        manifest,
    )
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()

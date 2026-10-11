from __future__ import annotations

import json

import common
import run_reference_drafts as drafts
import run_reference_repairs_v1 as repairs


def main() -> None:
    packets = {
        row["question_id"]: row for row in common.read_jsonl(common.REFERENCE_PACKETS)
    }
    quarantine_dir = (
        common.PACKAGE / "reference_build/revisions/quarantine_repair1"
    )
    recovered = []
    for path in sorted(quarantine_dir.glob("*.json")):
        row = json.loads(path.read_text(encoding="utf-8"))
        qid = row["question_id"]
        result, changes = repairs.structural_normalize_repair(
            row["raw_result"], packets[qid]
        )
        drafts.validate(result, packets[qid])
        recovered.append(
            {
                "question_id": qid,
                "reference_packet_sha256": common.payload_sha256(packets[qid]),
                "source_ledger_sha256": row["source_ledger_sha256"],
                "model_b_review_sha256": row["review_sha256"],
                "repair_prompt_sha256": common.sha256(repairs.PROMPT),
                "structural_normalizations": changes,
                "repaired_ledger": result,
                "generation": row["generation"],
                "recovered_from_quarantine": str(path.relative_to(common.ROOT)),
            }
        )
    existing = {
        row["question_id"]: row
        for row in (
            common.read_jsonl(repairs.OUTPUT) if repairs.OUTPUT.exists() else []
        )
    }
    existing.update({row["question_id"]: row for row in recovered})
    order = [
        row["question_id"]
        for row in common.read_jsonl(common.REFERENCE_PACKETS)
        if row["question_id"] in existing
    ]
    common.write_jsonl(repairs.OUTPUT, [existing[qid] for qid in order])
    print(json.dumps({"recovered": len(recovered)}, indent=2))


if __name__ == "__main__":
    main()

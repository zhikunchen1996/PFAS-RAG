from __future__ import annotations

import json

import common


CANONICAL = (
    common.PACKAGE / "reference_build/revisions/model_a_ledgers_repair1.jsonl"
)
BATCH_DIR = common.PACKAGE / "reference_build/reviews/batches"
MAX_BATCH_CHARS = 180_000


def main() -> None:
    packets = {row["question_id"]: row for row in common.read_jsonl(common.REFERENCE_PACKETS)}
    ledgers = common.read_jsonl(CANONICAL)
    items = [
        {
            "question_id": row["question_id"],
            "reference_packet": packets[row["question_id"]],
            "draft_ledger": row["draft_ledger"],
            "draft_ledger_sha256": common.payload_sha256(row["draft_ledger"]),
        }
        for row in ledgers
    ]
    batches: list[list[dict]] = []
    current: list[dict] = []
    current_chars = 0
    for item in items:
        size = len(json.dumps(item, ensure_ascii=False))
        if current and current_chars + size > MAX_BATCH_CHARS:
            batches.append(current)
            current = []
            current_chars = 0
        current.append(item)
        current_chars += size
    if current:
        batches.append(current)

    BATCH_DIR.mkdir(parents=True, exist_ok=True)
    manifest_rows = []
    for index, batch in enumerate(batches, start=1):
        batch_id = f"test40-review-batch-{index:02d}"
        payload = {
            "batch_id": batch_id,
            "candidate_blind": True,
            "questions": batch,
        }
        path = BATCH_DIR / f"batch_{index:02d}.json"
        common.write_json(path, payload)
        manifest_rows.append(
            {
                "batch_id": batch_id,
                "path": str(path.relative_to(common.ROOT)),
                "question_ids": [row["question_id"] for row in batch],
                "character_count": len(json.dumps(payload, ensure_ascii=False)),
                "sha256": common.sha256(path),
            }
        )
    manifest = {
        "stage": "candidate-blind Claude evidence-verification batching",
        "batch_count": len(manifest_rows),
        "question_count": sum(len(row["question_ids"]) for row in manifest_rows),
        "max_batch_characters": MAX_BATCH_CHARS,
        "batches": manifest_rows,
        "canonical_drafts_sha256": common.sha256(CANONICAL),
        "reference_packets_sha256": common.sha256(common.REFERENCE_PACKETS),
        "candidate_test40_inputs_used": False,
    }
    common.write_json(BATCH_DIR / "batch_manifest.json", manifest)
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()

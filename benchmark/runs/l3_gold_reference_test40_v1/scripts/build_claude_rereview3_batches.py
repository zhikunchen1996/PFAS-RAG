from __future__ import annotations

import json

import common


CANONICAL = (
    common.PACKAGE
    / "reference_build/revisions/model_a_ledgers_resolution1.jsonl"
)
REVIEWS = (
    common.PACKAGE
    / "reference_build/reviews/model_b_reviews_v1_rereview2.jsonl"
)
RESOLUTIONS = (
    common.PACKAGE / "reference_build/revisions/final_resolution_v1.jsonl"
)
BATCH_DIR = common.PACKAGE / "reference_build/reviews/rereview3_batches"
MAX_BATCH_CHARS = 180_000


def main() -> None:
    packets = {
        row["question_id"]: row for row in common.read_jsonl(common.REFERENCE_PACKETS)
    }
    ledgers = {row["question_id"]: row for row in common.read_jsonl(CANONICAL)}
    reviews = common.read_jsonl(REVIEWS)
    resolutions = {
        row["question_id"]: row for row in common.read_jsonl(RESOLUTIONS)
    }
    items = []
    for review in reviews:
        if review["verdict"] != "repair_required":
            continue
        qid = review["question_id"]
        items.append(
            {
                "question_id": qid,
                "reference_packet": packets[qid],
                "previous_review": review,
                "deterministic_resolution": resolutions[qid],
                "draft_ledger": ledgers[qid]["draft_ledger"],
                "draft_ledger_sha256": common.payload_sha256(
                    ledgers[qid]["draft_ledger"]
                ),
            }
        )
    batches = []
    current = []
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
        batch_id = f"test40-rereview3-batch-{index:02d}"
        payload = {
            "batch_id": batch_id,
            "candidate_blind": True,
            "review_round": "deterministic_resolution1_rereview",
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
        "stage": "Claude rereview3 batching after deterministic resolution1",
        "batch_count": len(manifest_rows),
        "question_count": len(items),
        "max_batch_characters": MAX_BATCH_CHARS,
        "batches": manifest_rows,
        "canonical_resolution1_sha256": common.sha256(CANONICAL),
        "previous_rereviews_sha256": common.sha256(REVIEWS),
        "resolutions_sha256": common.sha256(RESOLUTIONS),
        "candidate_test40_inputs_used": False,
    }
    common.write_json(BATCH_DIR / "batch_manifest.json", manifest)
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()

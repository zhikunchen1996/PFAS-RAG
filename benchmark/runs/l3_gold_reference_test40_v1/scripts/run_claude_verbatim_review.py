from __future__ import annotations

import argparse
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

import common


BATCH_DIR = common.PACKAGE / "reference_build/reviews/verbatim_review_batches"
RESULT_DIR = common.PACKAGE / "reference_build/reviews/verbatim_review_results"
PROMPT = common.PACKAGE / "prompts/claude_evidence_verification_v3.txt"
SCHEMA = common.PACKAGE / "prompts/claude_review_schema.json"


def validate_review(result: dict[str, Any], batch: dict[str, Any]) -> None:
    if result.get("batch_id") != batch["batch_id"]:
        raise RuntimeError(f"{batch['batch_id']}: returned batch ID differs")
    reviews = result.get("reviews")
    if not isinstance(reviews, list):
        raise RuntimeError(f"{batch['batch_id']}: missing reviews")
    review_by_qid = {row["question_id"]: row for row in reviews}
    expected_qids = {row["question_id"] for row in batch["questions"]}
    if set(review_by_qid) != expected_qids or len(review_by_qid) != len(reviews):
        raise RuntimeError(f"{batch['batch_id']}: question membership differs")
    for item in batch["questions"]:
        qid = item["question_id"]
        expected_groups = {
            row["claim_group_id"]
            for row in item["draft_ledger"]["claim_groups"]
            + item["draft_ledger"]["constraint_groups"]
        }
        group_reviews = review_by_qid[qid]["group_reviews"]
        actual_groups = {row["claim_group_id"] for row in group_reviews}
        if actual_groups != expected_groups or len(actual_groups) != len(group_reviews):
            raise RuntimeError(f"{batch['batch_id']} {qid}: group membership differs")


def run_batch(row: dict[str, Any]) -> dict[str, Any]:
    batch_path = common.ROOT / row["path"]
    batch = json.loads(batch_path.read_text(encoding="utf-8"))
    output_path = RESULT_DIR / f"{batch_path.stem}_review.json"
    if output_path.exists():
        stored = json.loads(output_path.read_text(encoding="utf-8"))
        validate_review(stored["review"], batch)
        return stored

    expected_group_text = "; ".join(
        f"{item['question_id']}: "
        + ", ".join(
            group["claim_group_id"]
            for group in item["draft_ledger"]["claim_groups"]
            + item["draft_ledger"]["constraint_groups"]
        )
        for item in batch["questions"]
    )
    instruction = (
        f"Read {PROMPT.relative_to(common.ROOT)} and "
        f"{batch_path.relative_to(common.ROOT)}. Review exactly that batch under "
        "the prompt. Do not read other Test40 files. Return the required "
        f"structured object with batch_id {batch['batch_id']} and one review "
        "for every question and every claim/constraint group. Verify whether "
        "the previous required repairs were resolved. The exact group IDs that "
        f"must each appear once are: {expected_group_text}."
    )
    command = [
        "claude",
        "-p",
        "--model",
        "sonnet",
        "--effort",
        "low",
        "--permission-mode",
        "plan",
        "--tools",
        "Read",
        "--no-session-persistence",
        "--output-format",
        "json",
        "--json-schema",
        json.dumps(json.loads(SCHEMA.read_text(encoding="utf-8"))),
        instruction,
    ]
    completed = subprocess.run(
        command,
        cwd=common.ROOT,
        check=True,
        capture_output=True,
        text=True,
        timeout=900,
    )
    outer = json.loads(completed.stdout)
    if outer.get("is_error") is True:
        raise RuntimeError(f"{batch['batch_id']}: Claude returned is_error")
    review = json.loads(outer["result"])
    validate_review(review, batch)
    stored = {
        "batch_id": batch["batch_id"],
        "batch_sha256": common.sha256(batch_path),
        "prompt_sha256": common.sha256(PROMPT),
        "schema_sha256": common.sha256(SCHEMA),
        "review": review,
        "claude_run": {
            key: value
            for key, value in outer.items()
            if key not in {"result", "structured_output", "iterations"}
        },
        "candidate_test40_inputs_used": False,
    }
    common.write_json(output_path, stored)
    return stored


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--limit", type=int)
    args = parser.parse_args()

    manifest = json.loads(
        (BATCH_DIR / "batch_manifest.json").read_text(encoding="utf-8")
    )
    rows = manifest["batches"]
    if args.limit:
        rows = rows[: args.limit]
    RESULT_DIR.mkdir(parents=True, exist_ok=True)
    completed_rows = []
    failures = []
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(run_batch, row): row for row in rows}
        for future in as_completed(futures):
            row = futures[future]
            try:
                result = future.result()
            except Exception as exc:
                failures.append((row["batch_id"], str(exc)))
                print(f"[error] {row['batch_id']}: {exc}", flush=True)
                continue
            completed_rows.append(result)
            print(f"[{len(completed_rows)}/{len(rows)}] {row['batch_id']}", flush=True)
    if failures:
        raise RuntimeError(f"Claude review failures: {failures}")

    all_results = []
    for row in manifest["batches"]:
        path = RESULT_DIR / f"{Path(row['path']).stem}_review.json"
        if path.exists():
            all_results.append(json.loads(path.read_text(encoding="utf-8")))
    review_rows = [review for batch in all_results for review in batch["review"]["reviews"]]
    if len(all_results) == len(manifest["batches"]):
        if len(review_rows) != manifest["question_count"]:
            raise RuntimeError(
                "Completed Claude question-review count differs from batch manifest"
            )
        common.write_jsonl(
            common.PACKAGE
            / "reference_build/reviews/model_b_reviews_v1_verbatim_review.jsonl",
            review_rows,
        )
        summary = {
            "stage": "independent Claude Sonnet review after verbatim-span resolution",
            "batch_count": len(all_results),
            "question_count": len(review_rows),
            "verdict_counts": {
                verdict: sum(row["verdict"] == verdict for row in review_rows)
                for verdict in ["clean", "repair_required", "unresolvable"]
            },
            "model": "Claude Sonnet 5 via Claude Pro CLI",
            "effort": "low",
            "prompt_sha256": common.sha256(PROMPT),
            "schema_sha256": common.sha256(SCHEMA),
            "review_output_sha256": common.sha256(
                common.PACKAGE
                / "reference_build/reviews/model_b_reviews_v1_verbatim_review.jsonl"
            ),
            "candidate_test40_inputs_used": False,
        }
        common.write_json(
            common.PACKAGE
            / "reference_build/reviews/run_manifest_v1_verbatim_review.json",
            summary,
        )
        print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()

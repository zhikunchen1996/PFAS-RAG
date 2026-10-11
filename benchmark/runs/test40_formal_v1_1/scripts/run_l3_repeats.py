from __future__ import annotations

import argparse
import csv
from pathlib import Path
from statistics import mean, stdev
from typing import Any

import common
import l3_scoring


SYSTEMS = ("hybrid", "bge", "bge_llm")
REPEAT_COUNT = 3
REASONING_EFFORT = "low"
MAX_COMPLETION_TOKENS = 12000


def normalize_references() -> dict[str, dict[str, Any]]:
    questions = {
        row["question_id"]: row for row in common.read_csv(common.QUESTIONS)
    }
    references: dict[str, dict[str, Any]] = {}
    for source in common.read_jsonl(common.REFERENCE_LEDGER):
        qid = str(source["question_id"])
        ledger = source.get("draft_ledger")
        if not isinstance(ledger, dict) or ledger.get("question_id") != qid:
            raise RuntimeError(f"{qid}: invalid frozen Test40 ledger")
        question = questions.get(qid)
        if question is None:
            raise RuntimeError(f"{qid}: reference lacks frozen question")
        references[qid] = {
            "question_id": qid,
            "question_text": question["question_text"],
            "task_boundaries": {
                "must_include": question.get("must_include", ""),
                "must_not_claim": question.get("must_not_claim", ""),
            },
            "ledger": ledger,
        }
    expected = common.question_ids()
    if set(references) != set(expected):
        raise RuntimeError("Test40 reference membership differs")
    return {qid: references[qid] for qid in expected}


def answer_path(root: Path, system: str) -> Path:
    return root / system / "answers/tagged_rag_gpt51.jsonl"


def build_items(
    generation_root: Path,
    references: dict[str, dict[str, Any]],
) -> tuple[list[dict[str, Any]], dict[str, Path]]:
    qids = list(references)
    paths = {system: answer_path(generation_root, system) for system in SYSTEMS}
    items = []
    for system in SYSTEMS:
        rows = common.ordered_rows(
            common.read_jsonl(paths[system]),
            qids,
            source=f"L3 {system}",
        )
        source_hash = common.sha256(paths[system])
        for row in rows:
            qid = str(row["question_id"])
            reference = references[qid]
            raw_answer = str(row.get("answer") or "")
            if not raw_answer.strip():
                raise RuntimeError(f"{system}/{qid}: empty answer")
            normalized = l3_scoring.canonicalize_answer(raw_answer)
            candidate_id = common.payload_sha256(
                {"question_id": qid, "answer": normalized}
            )[:16]
            payload = {
                "question_id": qid,
                "question": reference["question_text"],
                "task_boundaries": reference["task_boundaries"],
                "task_components": reference["ledger"]["task_components"],
                "content_claim_groups": reference["ledger"]["claim_groups"],
                "constraint_only_groups": reference["ledger"][
                    "constraint_groups"
                ],
                "gold_is_non_exhaustive": True,
                "anonymous_candidate_answer": normalized,
            }
            items.append(
                {
                    "item_id": f"{system}::{qid}",
                    "question_id": qid,
                    "system": system,
                    "candidate_id": candidate_id,
                    "source_answer_file_sha256": source_hash,
                    "raw_answer_sha256": common.payload_sha256(raw_answer),
                    "canonical_answer_sha256": common.payload_sha256(
                        normalized
                    ),
                    "payload": payload,
                }
            )
    if len(items) != 120:
        raise RuntimeError("Expected 3 systems x 40 L3 payloads")
    return items, paths


def summarize_repeat(
    rows: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    per_question = []
    for row in rows:
        scores = row["scores"]
        per_question.append(
            {
                "system": row["system"],
                "question_id": row["question_id"],
                **scores,
            }
        )
    summaries = []
    for system in SYSTEMS:
        values = [row for row in per_question if row["system"] == system]
        supplementary = [
            float(row["supplementary_reference_claim_coverage"])
            for row in values
            if row["supplementary_reference_claim_coverage"] is not None
        ]
        summaries.append(
            {
                "system": system,
                "question_count": len(values),
                "mean_component_balanced_core_reference_claim_coverage": mean(
                    float(
                        row[
                            "component_balanced_core_reference_claim_coverage"
                        ]
                    )
                    for row in values
                ),
                "mean_strict_core_reference_claim_coverage": mean(
                    float(row["strict_core_reference_claim_coverage"])
                    for row in values
                ),
                "mean_supplementary_reference_claim_coverage": (
                    mean(supplementary) if supplementary else ""
                ),
                "material_boundary_violation_rate": mean(
                    float(bool(row["material_boundary_violation"]))
                    for row in values
                ),
                "reference_anchored_material_error_rate": mean(
                    float(bool(row["reference_anchored_material_error"]))
                    for row in values
                ),
                "potential_external_scientific_error_rate": mean(
                    float(bool(row["potential_external_scientific_error"]))
                    for row in values
                ),
            }
        )
    return per_question, summaries


def aggregate_if_complete(out: Path) -> None:
    repeat_summaries: list[dict[str, Any]] = []
    for repeat in range(1, REPEAT_COUNT + 1):
        path = out / f"repeat_{repeat}/system_summary.csv"
        if not path.exists():
            return
        with path.open(encoding="utf-8-sig", newline="") as handle:
            for row in csv.DictReader(handle):
                repeat_summaries.append({"repeat": repeat, **row})

    summary = []
    metric = "mean_component_balanced_core_reference_claim_coverage"
    for system in SYSTEMS:
        rows = [row for row in repeat_summaries if row["system"] == system]
        values = [float(row[metric]) for row in rows]
        if len(values) != REPEAT_COUNT:
            raise RuntimeError(f"{system}: incomplete repeat aggregation")
        summary.append(
            {
                "system": system,
                "repeat_count": REPEAT_COUNT,
                "mean_l3_core_coverage": mean(values),
                "sample_sd_across_repeat_system_means": stdev(values),
                "repeat_min": min(values),
                "repeat_max": max(values),
            }
        )
    common.write_csv(out / "aggregate/repeat_system_metrics.csv", repeat_summaries)
    common.write_csv(out / "aggregate/system_three_repeat_summary.csv", summary)
    common.write_json(
        out / "aggregate/aggregation_manifest.json",
        {
            "protocol_id": "test40_formal_v1_l3_three_repeat",
            "status": "complete",
            "repeat_count": REPEAT_COUNT,
            "primary_metric": (
                "component-balanced core reference-claim coverage"
            ),
            "aggregation": (
                "Equal mean of three complete repeat-specific system means"
            ),
            "uncertainty": (
                "Sample standard deviation across three repeat-specific "
                "system means; not a confidence interval"
            ),
            "bootstrap": False,
            "claim_order": "canonical",
        },
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--generation-root", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--repeat", type=int, choices=[1, 2, 3], required=True)
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    references = normalize_references()
    generation_root = Path(args.generation_root).expanduser().resolve()
    common.require_exact_path(
        generation_root,
        common.GENERATION_RESULTS,
        label="L3 generation input",
    )
    items, answer_files = build_items(generation_root, references)
    prompt = common.L3_PROMPT.read_text(encoding="utf-8")

    def request(item: dict[str, Any]) -> dict[str, Any]:
        return common.json_request(
            system_prompt=prompt,
            payload=item["payload"],
            reasoning_effort=REASONING_EFFORT,
            max_completion_tokens=MAX_COMPLETION_TOKENS,
            temperature=None,
        )

    out = Path(args.out).expanduser().resolve()
    common.require_exact_path(
        out,
        common.L3_RESULTS,
        label="L3 output",
    )
    repeat_dir = out / f"repeat_{args.repeat}"
    repeat_dir.mkdir(parents=True, exist_ok=True)
    common.write_jsonl(
        out / "canonical_envelopes.jsonl",
        [
            {
                "item_id": item["item_id"],
                "question_id": item["question_id"],
                "candidate_id": item["candidate_id"],
                "source_answer_file_sha256": item[
                    "source_answer_file_sha256"
                ],
                "model_payload": item["payload"],
                "execution_sha256": common.payload_sha256(request(item)),
            }
            for item in items
        ],
    )
    if args.dry_run:
        print("DRY RUN PASS: 120 Test40 L3 payloads built; no API calls.")
        return
    results_path = repeat_dir / "judge_results.jsonl"
    if results_path.exists() and not args.resume:
        raise RuntimeError(
            "L3 repeat results already exist; use --resume to avoid "
            "duplicate calls"
        )

    def worker(item: dict[str, Any]) -> dict[str, Any]:
        result, metadata, request_hash = common.call_json(
            system_prompt=prompt,
            payload=item["payload"],
            reasoning_effort=REASONING_EFFORT,
            max_completion_tokens=MAX_COMPLETION_TOKENS,
            temperature=None,
        )
        reference = references[item["question_id"]]
        l3_scoring.validate_result(result, reference)
        return {
            "item_id": item["item_id"],
            "question_id": item["question_id"],
            "system": item["system"],
            "candidate_id": item["candidate_id"],
            "source_answer_file_sha256": item[
                "source_answer_file_sha256"
            ],
            "execution_sha256": request_hash,
            "assessment": result,
            "scores": l3_scoring.score_result(result, reference),
            "metadata": metadata,
            "repeat_index": args.repeat,
        }

    rows = common.run_resumable(
        items=items,
        key=lambda row: str(row["item_id"]),
        expected_execution_hash=lambda item: common.payload_sha256(
            request(item)
        ),
        worker=worker,
        output=results_path,
        workers=args.workers,
        resume=args.resume,
        label=f"Test40 L3 repeat {args.repeat}",
    )
    per_question, system_summary = summarize_repeat(rows)
    common.write_csv(repeat_dir / "question_level_scores.csv", per_question)
    common.write_csv(repeat_dir / "system_summary.csv", system_summary)
    common.write_json(
        repeat_dir / "run_manifest.json",
        {
            "protocol_id": "test40_formal_v1_l3_three_repeat",
            "repeat_index": args.repeat,
            "status": "complete",
            "question_count": 40,
            "systems": list(SYSTEMS),
            "judgment_count": len(rows),
            "model": common.MODEL,
            "required_snapshot": common.EXPECTED_MODEL,
            "reasoning_effort": REASONING_EFFORT,
            "temperature": "provider_default_not_sent",
            "max_completion_tokens": MAX_COMPLETION_TOKENS,
            "claim_order": "canonical",
            "one_anonymous_answer_per_request": True,
            "questions_sha256": common.sha256(common.QUESTIONS),
            "reference_ledger_sha256": common.sha256(
                common.REFERENCE_LEDGER
            ),
            "prompt_sha256": common.sha256(common.L3_PROMPT),
            "answer_inputs": {
                system: {
                    "path": common.project_relative(path),
                    "sha256": common.sha256(path),
                }
                for system, path in answer_files.items()
            },
            "api_calls": len(rows),
            "total_tokens": sum(
                int(row["metadata"]["total_tokens"]) for row in rows
            ),
            "estimated_cost_usd": sum(
                float(row["metadata"]["estimated_cost_usd"]) for row in rows
            ),
            "latency_seconds_sum": sum(
                float(row["metadata"]["latency_seconds"]) for row in rows
            ),
            "resume_hash_validated": True,
        },
    )
    aggregate_if_complete(out)


if __name__ == "__main__":
    main()

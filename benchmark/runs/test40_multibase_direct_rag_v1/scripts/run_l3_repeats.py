from __future__ import annotations

import argparse
import csv
import json
import time
from pathlib import Path
from statistics import mean, stdev
from typing import Any

import common
import l3_scoring
import run_generation


SYSTEMS = run_generation.SYSTEMS
BASE_MODELS = ("gpt51", "gemini31_pro", "claude_sonnet5")
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
    ids = common.question_ids()
    if set(references) != set(ids):
        raise RuntimeError("Test40 reference membership differs")
    return {qid: references[qid] for qid in ids}


def build_items(
    references: dict[str, dict[str, Any]],
) -> tuple[list[dict[str, Any]], dict[str, Path]]:
    ids = list(references)
    paths = {
        system: run_generation.output_path(system) for system in SYSTEMS
    }
    items = []
    for system in SYSTEMS:
        rows = common.ordered_rows(
            common.read_jsonl(paths[system]),
            ids,
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
    if len(items) != 240:
        raise RuntimeError("Expected 6 systems x 40 Test40 L3 payloads")
    return items, paths


def judge_request(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "model": common.OPENAI_MODEL,
        "response_format": {"type": "json_object"},
        "reasoning_effort": REASONING_EFFORT,
        "max_completion_tokens": MAX_COMPLETION_TOKENS,
        "messages": [
            {
                "role": "system",
                "content": common.L3_PROMPT.read_text(encoding="utf-8"),
            },
            {
                "role": "user",
                "content": json.dumps(
                    item["payload"],
                    ensure_ascii=False,
                ),
            },
        ],
    }


def judge(
    item: dict[str, Any],
    references: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    request = judge_request(item)
    started = time.perf_counter()
    response = common.openai_client().chat.completions.create(**request)
    latency = time.perf_counter() - started
    metadata = common.openai_metadata(response, latency)
    raw = response.choices[0].message.content or "{}"
    result = json.loads(raw)
    if not isinstance(result, dict):
        raise RuntimeError("L3 judge response is not a JSON object")
    reference = references[item["question_id"]]
    l3_scoring.validate_result(result, reference)
    return {
        "item_id": item["item_id"],
        "question_id": item["question_id"],
        "system": item["system"],
        "candidate_id": item["candidate_id"],
        "source_answer_file_sha256": item["source_answer_file_sha256"],
        "execution_sha256": common.payload_sha256(request),
        "assessment": result,
        "scores": l3_scoring.score_result(result, reference),
        "metadata": metadata,
    }


def summarize_repeat(
    rows: list[dict[str, Any]],
) -> tuple[
    list[dict[str, Any]],
    list[dict[str, Any]],
    list[dict[str, Any]],
]:
    per_question = [
        {
            "system": row["system"],
            "question_id": row["question_id"],
            **row["scores"],
        }
        for row in rows
    ]
    summaries = []
    metric = "component_balanced_core_reference_claim_coverage"
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
                    float(row[metric]) for row in values
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
    by_key = {
        (row["system"], row["question_id"]): row for row in per_question
    }
    effects = []
    for base_model in BASE_MODELS:
        direct = f"{base_model}_direct"
        rag = f"{base_model}_rag"
        deltas = [
            float(by_key[(rag, qid)][metric])
            - float(by_key[(direct, qid)][metric])
            for qid in common.question_ids()
        ]
        effects.append(
            {
                "base_model": base_model,
                "question_count": len(deltas),
                "mean_rag_minus_direct": mean(deltas),
                "rag_better_count": sum(value > 0 for value in deltas),
                "tie_count": sum(value == 0 for value in deltas),
                "direct_better_count": sum(value < 0 for value in deltas),
            }
        )
    return per_question, summaries, effects


def aggregate_if_complete() -> None:
    repeat_summaries: list[dict[str, Any]] = []
    repeat_effects: list[dict[str, Any]] = []
    for repeat in range(1, REPEAT_COUNT + 1):
        summary_path = common.L3_RESULTS / f"repeat_{repeat}/system_summary.csv"
        effect_path = common.L3_RESULTS / f"repeat_{repeat}/within_model.csv"
        if not summary_path.exists() or not effect_path.exists():
            return
        with summary_path.open(encoding="utf-8-sig", newline="") as handle:
            repeat_summaries.extend(
                {"repeat": repeat, **row} for row in csv.DictReader(handle)
            )
        with effect_path.open(encoding="utf-8-sig", newline="") as handle:
            repeat_effects.extend(
                {"repeat": repeat, **row} for row in csv.DictReader(handle)
            )
    metric = "mean_component_balanced_core_reference_claim_coverage"
    system_summary = []
    for system in SYSTEMS:
        values = [
            float(row[metric])
            for row in repeat_summaries
            if row["system"] == system
        ]
        if len(values) != REPEAT_COUNT:
            raise RuntimeError(f"{system}: incomplete repeat aggregation")
        system_summary.append(
            {
                "system": system,
                "repeat_count": REPEAT_COUNT,
                "mean_l3_core_coverage": mean(values),
                "sample_sd_across_repeat_system_means": stdev(values),
                "repeat_min": min(values),
                "repeat_max": max(values),
            }
        )
    effect_summary = []
    for base_model in BASE_MODELS:
        values = [
            float(row["mean_rag_minus_direct"])
            for row in repeat_effects
            if row["base_model"] == base_model
        ]
        if len(values) != REPEAT_COUNT:
            raise RuntimeError(f"{base_model}: incomplete effect aggregation")
        effect_summary.append(
            {
                "base_model": base_model,
                "repeat_count": REPEAT_COUNT,
                "mean_rag_minus_direct": mean(values),
                "sample_sd_across_repeat_mean_differences": stdev(values),
                "repeat_min": min(values),
                "repeat_max": max(values),
            }
        )
    aggregate = common.L3_RESULTS / "aggregate"
    common.write_csv(
        aggregate / "repeat_system_metrics.csv",
        repeat_summaries,
    )
    common.write_csv(
        aggregate / "system_three_repeat_summary.csv",
        system_summary,
    )
    common.write_csv(
        aggregate / "repeat_within_model_effects.csv",
        repeat_effects,
    )
    common.write_csv(
        aggregate / "within_model_three_repeat_summary.csv",
        effect_summary,
    )
    common.write_json(
        aggregate / "aggregation_manifest.json",
        {
            "protocol_id": "test40_multibase_direct_rag_v1_l3",
            "status": "complete",
            "repeat_count": REPEAT_COUNT,
            "primary_metric": (
                "component-balanced core reference-claim coverage"
            ),
            "primary_contrasts": "within-model RAG minus Direct",
            "aggregation": (
                "Equal mean of three complete repeat-specific system means"
            ),
            "uncertainty": (
                "Sample standard deviation across repeat-specific means; "
                "not a confidence interval"
            ),
            "bootstrap": False,
            "claim_order": "canonical",
        },
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repeat", type=int, choices=[1, 2, 3], required=True)
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    references = normalize_references()
    items, answer_paths = build_items(references)
    common.L3_RESULTS.mkdir(parents=True, exist_ok=True)
    common.write_jsonl(
        common.L3_RESULTS / "canonical_envelopes.jsonl",
        [
            {
                "item_id": item["item_id"],
                "question_id": item["question_id"],
                "candidate_id": item["candidate_id"],
                "source_answer_file_sha256": item[
                    "source_answer_file_sha256"
                ],
                "model_payload": item["payload"],
                "execution_sha256": common.payload_sha256(
                    judge_request(item)
                ),
            }
            for item in items
        ],
    )
    if args.dry_run:
        print("DRY RUN PASS: 240 anonymous L3 payloads built; no API calls.")
        return
    repeat_dir = common.L3_RESULTS / f"repeat_{args.repeat}"
    output = repeat_dir / "judge_results.jsonl"
    if output.exists() and not args.resume:
        raise RuntimeError(
            "L3 output exists; use --resume to avoid duplicate calls"
        )
    rows = common.run_resumable(
        items=items,
        key=lambda row: str(row["item_id"]),
        expected_execution_hash=lambda item: common.payload_sha256(
            judge_request(item)
        ),
        worker=lambda item: {
            **judge(item, references),
            "repeat_index": args.repeat,
        },
        output=output,
        workers=args.workers,
        resume=args.resume,
        label=f"Test40 multibase L3 repeat {args.repeat}",
    )
    per_question, system_summary, effects = summarize_repeat(rows)
    common.write_csv(repeat_dir / "question_level_scores.csv", per_question)
    common.write_csv(repeat_dir / "system_summary.csv", system_summary)
    common.write_csv(repeat_dir / "within_model.csv", effects)
    common.write_json(
        repeat_dir / "run_manifest.json",
        {
            "protocol_id": "test40_multibase_direct_rag_v1_l3",
            "status": "complete",
            "repeat_index": args.repeat,
            "question_count": 40,
            "systems": list(SYSTEMS),
            "judgment_count": len(rows),
            "model": common.OPENAI_MODEL,
            "required_snapshot": common.OPENAI_SNAPSHOT,
            "reasoning_effort": REASONING_EFFORT,
            "temperature": "provider_default_not_sent",
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
                for system, path in answer_paths.items()
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
    aggregate_if_complete()


if __name__ == "__main__":
    main()

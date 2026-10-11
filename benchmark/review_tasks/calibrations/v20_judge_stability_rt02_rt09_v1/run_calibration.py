#!/usr/bin/env python3
"""Run a prospective repeatability check of the V20 review-quality judge."""

from __future__ import annotations

import argparse
import csv
import json
import shutil
import statistics
import sys
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[4]
PACKAGE_ROOT = (
    PROJECT_ROOT
    / "benchmark"
    / "review_tasks"
    / "professional_review_v3_pilot_candidate_v20"
)
SOURCE_RUN = (
    PROJECT_ROOT
    / "benchmark"
    / "review_tasks"
    / "runs"
    / "professional_review_v3_pilot_candidate_v15_rt02_rt09_full"
)
sys.path.insert(0, str(PACKAGE_ROOT / "scripts"))

from review_runtime import (  # noqa: E402
    ResumableOpenAI,
    collect_call_records,
    load_json,
    sha256_file,
    utc_now,
    write_json,
)
from run_review_experiment import (  # noqa: E402
    _review_judge,
    package_hashes,
    selected_inputs,
)
from score_review_judgments import score_judgment  # noqa: E402


TASK_IDS = ["RT02", "RT09"]
SYSTEMS = ["bge_llm_local_rag", "gpt51_web_search"]
REPEATS = 3
MEAN_ANSWER_SD_LIMIT = 0.050
MAX_ANSWER_SD_LIMIT = 0.075
MAX_REPEAT_DEVIATION_LIMIT = 0.100
SOURCE_RUN_MANIFEST_SHA256 = (
    "e38d674f5352ce973bd975b0ff09831b177e015b7837b7e208e532e9749642e4"
)


def repo_relative(path: Path) -> str:
    """Return a portable repository-relative provenance path."""
    return path.resolve().relative_to(PROJECT_ROOT).as_posix()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--allow-paid", action="store_true")
    parser.add_argument("--workers", type=int, default=4)
    return parser.parse_args()


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def prepare_answers(run_dir: Path) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    for task_id in TASK_IDS:
        for system in SYSTEMS:
            relative = Path("systems") / system / task_id / "professional_review.md"
            source = SOURCE_RUN / relative
            destination = run_dir / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            if source.exists() and destination.exists():
                if sha256_file(destination) != sha256_file(source):
                    raise RuntimeError(f"Copied answer changed: {destination}")
            elif source.exists():
                shutil.copy2(source, destination)
            elif not destination.exists():
                raise RuntimeError(
                    "Missing both the provenance source and frozen copied answer: "
                    f"{source} / {destination}"
                )
            records.append(
                {
                    "path": str(relative),
                    "source_path": repo_relative(source),
                    "sha256": sha256_file(destination),
                }
            )
    return records


def status_signature(result: dict[str, Any]) -> tuple[str, ...]:
    values = [
        *(
            f"component:{item['component_id']}:{item['status']}"
            for item in sorted(
                result["component_fulfillment"],
                key=lambda item: item["component_id"],
            )
        ),
        f"calibration:{result['claim_calibration']['status']}",
        f"external_error:{result['potential_external_scientific_error']}",
    ]
    for dimension in (
        "critical_synthesis",
        "professional_depth",
        "current_research_outlook",
    ):
        for operation, assessment in sorted(result[dimension].items()):
            values.append(f"{dimension}:{operation}:{assessment['status']}")
    for item in sorted(
        result["constraint_assessments"],
        key=lambda item: item["constraint_id"],
    ):
        values.append(f"constraint:{item['constraint_id']}:{item['status']}")
    return tuple(values)


def summarize(run_dir: Path) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    answer_rows: list[dict[str, Any]] = []
    for task_id in TASK_IDS:
        for system in SYSTEMS:
            scores = []
            signatures = []
            for repeat in range(1, REPEATS + 1):
                call = load_json(
                    run_dir
                    / "calls"
                    / system
                    / task_id
                    / "review_judge"
                    / f"repeat_{repeat}.json"
                )
                scored = score_judgment(call["result"])
                score = float(scored["atomic_component_capped_review_quality"])
                scores.append(score)
                signatures.append(status_signature(call["result"]))
                rows.append(
                    {
                        "task_id": task_id,
                        "system": system,
                        "repeat": repeat,
                        "score": score,
                        "component_fulfillment": scored[
                            "mean_component_fulfillment"
                        ],
                        "critical_synthesis": scored["critical_synthesis"],
                        "professional_depth": scored["professional_depth"],
                        "current_research_outlook": scored[
                            "current_research_outlook"
                        ],
                    }
                )
            mean = statistics.fmean(scores)
            sample_sd = statistics.stdev(scores)
            answer_rows.append(
                {
                    "task_id": task_id,
                    "system": system,
                    "mean_score": mean,
                    "sample_sd": sample_sd,
                    "score_range": max(scores) - min(scores),
                    "max_abs_deviation": max(abs(score - mean) for score in scores),
                    "exact_three_way_status_agreement": len(set(signatures)) == 1,
                }
            )

    mean_answer_sd = statistics.fmean(row["sample_sd"] for row in answer_rows)
    max_answer_sd = max(row["sample_sd"] for row in answer_rows)
    max_repeat_deviation = max(
        row["max_abs_deviation"] for row in answer_rows
    )
    stability_gate = {
        "mean_per_answer_sample_sd": mean_answer_sd,
        "mean_per_answer_sample_sd_limit": MEAN_ANSWER_SD_LIMIT,
        "max_per_answer_sample_sd": max_answer_sd,
        "max_per_answer_sample_sd_limit": MAX_ANSWER_SD_LIMIT,
        "max_repeat_deviation_from_answer_mean": max_repeat_deviation,
        "max_repeat_deviation_limit": MAX_REPEAT_DEVIATION_LIMIT,
    }
    passed = (
        mean_answer_sd <= MEAN_ANSWER_SD_LIMIT
        and max_answer_sd <= MAX_ANSWER_SD_LIMIT
        and max_repeat_deviation <= MAX_REPEAT_DEVIATION_LIMIT
    )
    calls = collect_call_records(run_dir)
    summary = {
        "status": "complete",
        "completed_at": utc_now(),
        "task_ids": TASK_IDS,
        "systems": SYSTEMS,
        "judge_repeats": REPEATS,
        "answer_count": len(answer_rows),
        "paid_call_count": len(calls),
        "total_tokens": sum(int(call.get("total_tokens", 0)) for call in calls),
        "estimated_cost_usd": sum(
            float(call.get("estimated_cost_usd", 0.0)) for call in calls
        ),
        "total_latency_seconds": sum(
            float(call.get("latency_seconds", 0.0)) for call in calls
        ),
        "exact_three_way_status_agreement_count": sum(
            bool(row["exact_three_way_status_agreement"])
            for row in answer_rows
        ),
        "stability_gate": stability_gate,
        "stability_gate_passed": passed,
        "single_canonical_judge_supported": passed,
        "answer_summaries": answer_rows,
    }
    write_csv(run_dir / "summary" / "repeat_scores.csv", rows)
    write_csv(run_dir / "summary" / "answer_stability.csv", answer_rows)
    write_json(run_dir / "summary" / "summary.json", summary)
    return summary


def main() -> None:
    args = parse_args()
    if args.workers < 1:
        raise ValueError("--workers must be at least 1")
    run_dir = args.run_dir.expanduser().resolve()
    run_dir.mkdir(parents=True, exist_ok=True)
    answer_records = prepare_answers(run_dir)
    tasks, ledgers, _ = selected_inputs(TASK_IDS)
    manifest = {
        "calibration_id": "v20_judge_stability_rt02_rt09_v1",
        "created_at": utc_now(),
        "interpretation": "prospective_judge_stability_check_on_untouched_tasks",
        "source_run": repo_relative(SOURCE_RUN),
        "source_run_manifest_sha256": SOURCE_RUN_MANIFEST_SHA256,
        "v20_package_root": repo_relative(PACKAGE_ROOT),
        "v20_package_hashes": package_hashes(),
        "task_ids": TASK_IDS,
        "systems": SYSTEMS,
        "judge_repeats": REPEATS,
        "model": "gpt-5.1-2025-11-13",
        "reasoning_effort": "low",
        "fixed_answers": answer_records,
        "prospective_stability_limits": {
            "mean_per_answer_sample_sd": MEAN_ANSWER_SD_LIMIT,
            "max_per_answer_sample_sd": MAX_ANSWER_SD_LIMIT,
            "max_repeat_deviation_from_answer_mean": MAX_REPEAT_DEVIATION_LIMIT,
        },
    }
    manifest_path = run_dir / "calibration_manifest.json"
    if manifest_path.exists():
        prior = load_json(manifest_path)
        comparable = dict(prior)
        comparable.pop("created_at", None)
        expected = dict(manifest)
        expected.pop("created_at", None)
        if comparable != expected:
            raise RuntimeError("Existing calibration manifest does not match")
    else:
        write_json(manifest_path, manifest)

    api = ResumableOpenAI(allow_paid=args.allow_paid)
    _review_judge(
        run_dir=run_dir,
        tasks=tasks,
        ledgers=ledgers,
        systems=SYSTEMS,
        api=api,
        workers=args.workers,
        repeats=REPEATS,
    )
    summary = summarize(run_dir)
    verdict = "PASS" if summary["stability_gate_passed"] else "FAIL"
    print(
        f"{verdict}: {summary['paid_call_count']} calls, "
        f"USD {summary['estimated_cost_usd']:.4f}, "
        f"mean answer SD "
        f"{summary['stability_gate']['mean_per_answer_sample_sd']:.4f}, "
        f"max answer SD "
        f"{summary['stability_gate']['max_per_answer_sample_sd']:.4f}"
    )


if __name__ == "__main__":
    main()

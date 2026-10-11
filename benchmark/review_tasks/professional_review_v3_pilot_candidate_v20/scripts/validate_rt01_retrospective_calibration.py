#!/usr/bin/env python3
"""Validate the completed V19 RT01 retrospective calibration run."""

from __future__ import annotations

import argparse
import math
from collections import Counter
from pathlib import Path

from review_runtime import collect_call_records, load_json, sha256_file
from run_review_experiment import package_hashes
from validate_review_run import expected_execution_hash, expected_summary_hashes


EXPECTED_SYSTEMS = [
    "bge_llm_local_rag",
    "gpt51_web_search",
    "gpt51_direct",
]
EXPECTED_STAGES = ["source_support", "review_judge", "summary"]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    run_dir = parse_args().run_dir.expanduser().resolve()
    reused = load_json(run_dir / "reused_artifacts_manifest.json")
    require(reused["status"] == "prepared", "Reused-artifact manifest is invalid")
    for source_record in reused["source_runs"].values():
        source_run = Path(source_record["path"])
        require(
            sha256_file(source_run / "run_manifest.json")
            == source_record["manifest_sha256"],
            f"Source run manifest changed: {source_run}",
        )
    for record in reused["files"]:
        source_run = Path(record["source_run"])
        source = source_run / record["path"]
        copied = run_dir / record["path"]
        require(sha256_file(source) == record["source_sha256"], f"Source changed: {source}")
        require(sha256_file(copied) == record["copied_sha256"], f"Copy changed: {copied}")

    manifest = load_json(run_dir / "run_manifest.json")
    require(manifest["package_hashes"] == package_hashes(), "Package hashes changed")
    require(manifest["execution_hash"] == expected_execution_hash(manifest), "Execution hash mismatch")
    require(manifest["task_ids"] == ["RT01"], "Unexpected calibration task")
    require(manifest["systems"] == EXPECTED_SYSTEMS, "Unexpected systems")
    require(manifest["stages"] == EXPECTED_STAGES, "Unexpected stages")
    require(manifest["judge_repeats"] == 3, "Unexpected repeat count")
    require(manifest["status"] == "partial", "Calibration run should be stage-partial")

    calls = collect_call_records(run_dir)
    stage_counts = Counter(call["stage"] for call in calls)
    require(
        stage_counts == {"review_source_support": 2, "review_quality_judge": 9},
        f"Unexpected paid-call stages: {dict(stage_counts)}",
    )
    summary = load_json(run_dir / "summary" / "summary.json")
    require(summary["status"] == "complete", "Calibration summary is incomplete")
    require(summary["task_ids"] == ["RT01"], "Summary task mismatch")
    require(summary["systems"] == EXPECTED_SYSTEMS, "Summary systems mismatch")
    require(summary["judge_repeats"] == 3, "Summary repeat mismatch")
    require(summary["total_paid_call_count"] == 11, "Summary call count mismatch")
    require(
        summary["summary_input_hashes"] == expected_summary_hashes(run_dir),
        "Summary input hashes changed",
    )
    cost = sum(float(call.get("estimated_cost_usd", 0.0) or 0.0) for call in calls)
    require(
        math.isclose(summary["total_estimated_cost_usd"], cost, rel_tol=0.0, abs_tol=1e-9),
        "Summary cost mismatch",
    )
    for system in EXPECTED_SYSTEMS:
        anonymized = run_dir / "systems" / system / "RT01" / "layer_b_candidate_review.md"
        audit = run_dir / "systems" / system / "RT01" / "layer_b_anonymization.json"
        require(anonymized.exists() and audit.exists(), f"Missing Layer B anonymization for {system}")
    print("PASS: V19 RT01 retrospective calibration is complete and hash-valid")


if __name__ == "__main__":
    main()

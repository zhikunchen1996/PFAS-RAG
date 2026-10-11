#!/usr/bin/env python3
"""Copy immutable V17 RT01 artifacts into a clean V19 calibration run."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from review_runtime import PACKAGE_ROOT, load_json, sha256_file, utc_now, write_json


V17_SOURCE_RUN = (
    PACKAGE_ROOT.parent
    / "runs"
    / "professional_review_v3_pilot_candidate_v17_rt01"
)
V19_SOURCE_RUN = (
    PACKAGE_ROOT.parent
    / "runs"
    / "professional_review_v3_pilot_candidate_v19_rt01_retrospective"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    return parser.parse_args()


def copied_files(run_dir: Path) -> list[Path]:
    return sorted(
        path
        for directory in (
            run_dir / "systems",
            run_dir / "retrieval",
            run_dir / "calls",
        )
        if directory.exists()
        for path in directory.rglob("*")
        if path.is_file()
    )


def main() -> None:
    args = parse_args()
    run_dir = args.run_dir.expanduser().resolve()
    if run_dir.exists() and any(run_dir.iterdir()):
        raise RuntimeError(f"Calibration run directory is not empty: {run_dir}")
    run_dir.mkdir(parents=True, exist_ok=True)
    for directory_name in ("systems", "retrieval"):
        source = V17_SOURCE_RUN / directory_name
        if source.exists():
            shutil.copytree(source, run_dir / directory_name)

    reused_support_calls = [
        Path("calls") / system / "RT01" / "review_source_support.json"
        for system in ("bge_llm_local_rag", "gpt51_web_search")
    ]
    for relative in reused_support_calls:
        source = V19_SOURCE_RUN / relative
        destination = run_dir / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)

    records = []
    for destination in copied_files(run_dir):
        relative = destination.relative_to(run_dir)
        source_run = (
            V19_SOURCE_RUN
            if relative in reused_support_calls
            else V17_SOURCE_RUN
        )
        source = source_run / relative
        source_hash = sha256_file(source)
        destination_hash = sha256_file(destination)
        if source_hash != destination_hash:
            raise RuntimeError(f"Hash mismatch while copying {relative}")
        records.append(
            {
                "path": str(relative),
                "source_run": str(source_run),
                "source_sha256": source_hash,
                "copied_sha256": destination_hash,
            }
        )

    expected_answers = {
        f"systems/{system}/RT01/professional_review.md"
        for system in (
            "bge_llm_local_rag",
            "gpt51_web_search",
            "gpt51_direct",
        )
    }
    found = {record["path"] for record in records}
    if not expected_answers <= found:
        raise RuntimeError(
            f"Missing fixed candidate answers: {sorted(expected_answers - found)}"
        )
    if list(run_dir.glob("calls/*/RT01/review_judge")):
        raise RuntimeError("Old Layer B judgments were copied unexpectedly")
    if (run_dir / "summary").exists():
        raise RuntimeError("Old summary was copied unexpectedly")

    v17_manifest = load_json(V17_SOURCE_RUN / "run_manifest.json")
    v19_manifest = load_json(V19_SOURCE_RUN / "run_manifest.json")
    write_json(
        run_dir / "reused_artifacts_manifest.json",
        {
            "status": "prepared",
            "prepared_at": utc_now(),
            "interpretation": "retrospective_calibration_not_prospective_validation",
            "source_runs": {
                "v17_candidate_artifacts": {
                    "path": str(V17_SOURCE_RUN),
                    "execution_hash": v17_manifest["execution_hash"],
                    "manifest_sha256": sha256_file(
                        V17_SOURCE_RUN / "run_manifest.json"
                    ),
                },
                "v19_source_support_calls": {
                    "path": str(V19_SOURCE_RUN),
                    "execution_hash": v19_manifest["execution_hash"],
                    "manifest_sha256": sha256_file(
                        V19_SOURCE_RUN / "run_manifest.json"
                    ),
                },
            },
            "copied_file_count": len(records),
            "files": records,
        },
    )
    print(
        "PASS: copied and hash-verified "
        f"{len(records)} fixed artifacts with no V19 Layer B judgment"
    )


if __name__ == "__main__":
    main()

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any

import common
import run_generation
import run_l3_repeats


MANIFEST = common.PACKAGE / "pre_run_manifest.json"
REPORT = common.PACKAGE / "preflight_report.json"


def run_validator(command: list[str]) -> None:
    result = subprocess.run(
        command,
        cwd=common.ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode:
        raise RuntimeError(
            f"Validator failed: {' '.join(command)}\n"
            f"{result.stdout}\n{result.stderr}"
        )


def package_files() -> list[Path]:
    excluded = {MANIFEST.resolve(), REPORT.resolve()}
    return [
        path
        for path in sorted(common.PACKAGE.rglob("*"))
        if path.is_file()
        and path.resolve() not in excluded
        and common.RESULTS not in path.parents
        and "__pycache__" not in path.parts
        and path.suffix != ".pyc"
    ]


def validate_no_paid_outputs() -> None:
    if not common.RESULTS.exists():
        return
    found = [
        path
        for path in common.RESULTS.rglob("*")
        if path.is_file()
    ]
    if found:
        raise RuntimeError(
            "Paid outputs already exist before pre-run freeze: "
            + ", ".join(common.project_relative(path) for path in found)
        )


def validate_provider_keys() -> dict[str, bool]:
    keys = {
        "OPENAI_API_KEY": bool(__import__("os").getenv("OPENAI_API_KEY")),
        "GOOGLE_API_KEY": bool(__import__("os").getenv("GOOGLE_API_KEY")),
        "ANTHROPIC_API_KEY": bool(
            __import__("os").getenv("ANTHROPIC_API_KEY")
        ),
    }
    if not all(keys.values()):
        raise RuntimeError(
            "Missing provider credentials: "
            + ", ".join(name for name, present in keys.items() if not present)
        )
    return keys


def validate_references() -> dict[str, int]:
    references = run_l3_repeats.normalize_references()
    return {
        "questions": len(references),
        "claim_groups": sum(
            len(row["ledger"]["claim_groups"])
            for row in references.values()
        ),
        "constraint_groups": sum(
            len(row["ledger"]["constraint_groups"])
            for row in references.values()
        ),
    }


def expected_manifest() -> dict[str, Any]:
    files = package_files()
    return {
        "freeze_id": "test40_multibase_direct_rag_v1_prerun_2026-07-30",
        "status": "pre_run_no_paid_calls",
        "protocol_id": "test40_multibase_direct_rag_v1",
        "question_count": 40,
        "systems": list(run_generation.SYSTEMS),
        "planned_paid_calls": 960,
        "central_cost_estimate_usd": 24.688746307692305,
        "recommended_budget_ceiling_usd": 30.0,
        "generation_models": {
            name: value["model"]
            for name, value in run_generation.CONFIGS.items()
        },
        "judge_model": common.OPENAI_MODEL,
        "required_judge_snapshot": common.OPENAI_SNAPSHOT,
        "package_files": {
            common.project_relative(path): common.sha256(path) for path in files
        },
        "frozen_inputs": {
            common.project_relative(path): common.sha256(path)
            for path in (
                common.QUESTIONS,
                common.RETRIEVAL,
                common.TAGS,
                common.REFERENCE_LEDGER,
                common.SHARED_PROMPT,
                common.DIRECT_PROMPT,
                common.RAG_PROMPT,
                common.L3_PROMPT,
            )
        },
        "test40_multibase_candidate_outputs_observed": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-manifest", action="store_true")
    parser.add_argument("--verify-manifest", action="store_true")
    args = parser.parse_args()
    if args.write_manifest == args.verify_manifest:
        raise RuntimeError(
            "Choose exactly one of --write-manifest or --verify-manifest"
        )
    python = str(common.ROOT / ".venv/bin/python")
    run_validator(
        [
            python,
            "-m",
            "unittest",
            "discover",
            "-s",
            str(common.PACKAGE / "tests"),
            "-v",
        ]
    )
    run_validator(
        [
            python,
            str(common.ROOT / "benchmark/frozen_v3/scripts/build_freeze_manifest.py"),
            "--verify",
        ]
    )
    run_validator(
        [
            python,
            str(
                common.ROOT
                / "benchmark/frozen_v3/judge/scripts/validate_frozen_judge.py"
            ),
        ]
    )
    validate_no_paid_outputs()
    keys = validate_provider_keys()
    items = run_generation.load_items()
    references = validate_references()
    expected = expected_manifest()
    if args.write_manifest:
        common.write_json(MANIFEST, expected)
    else:
        actual = json.loads(MANIFEST.read_text(encoding="utf-8"))
        if actual != expected:
            raise RuntimeError("Pre-run manifest differs from current package")
    report = {
        "status": "PASS",
        "paid_api_calls_made": 0,
        "question_count": len(items),
        "systems": len(run_generation.SYSTEMS),
        "generation_payload_count": len(items) * len(run_generation.SYSTEMS),
        "l3_planned_judgment_count": (
            len(items) * len(run_generation.SYSTEMS) * 3
        ),
        "reference_schema": references,
        "provider_credentials_present": keys,
        "automatic_sdk_retries": 0,
        "resume_requires_exact_request_hash": True,
        "central_cost_estimate_usd": 24.688746307692305,
        "recommended_budget_ceiling_usd": 30.0,
    }
    common.write_json(REPORT, report)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()

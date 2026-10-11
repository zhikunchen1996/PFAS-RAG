from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import common
import build_scoring_reference_v2
import run_l3_repeats
import run_retrieval
import chromadb


MANIFEST = common.PACKAGE / "pre_run_manifest.json"
REPORT = common.PACKAGE / "preflight_report.json"
FORBIDDEN_RUNTIME_REFERENCES = (
    "input/questions_dev13.csv",
    "reference_claim_ledgers_v2.jsonl",
    "stage4_multibase_dev13_v1/results/",
)


def run_validator(path: Path, *args: str) -> None:
    command = [str(common.ROOT / ".venv/bin/python"), str(path), *args]
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
        and "__pycache__" not in path.parts
        and path.suffix != ".pyc"
    ]


def frozen_inputs() -> list[Path]:
    files = [
        common.QUESTIONS,
        common.GOLD,
        common.REFERENCE_LEDGER,
        common.REFERENCE_FREEZE_MANIFEST,
        common.FROZEN_V3 / "freeze_manifest.json",
        common.FROZEN_JUDGE / "freeze_manifest.json",
        common.SELECTOR_PROMPT,
        common.TAGGER_PROMPT,
        common.ANSWER_PROMPT,
        common.L15_PROMPT,
        common.L3_PROMPT,
        common.FROZEN_V3 / "scripts/run_dev13_soft_tags_v3.py",
        common.FROZEN_V3 / "scripts/runtime_helpers.py",
        common.FROZEN_V3 / "scripts/retrieval_metrics.py",
        common.ROOT / "corpus/corpus434_repaired_v1/version_manifest.json",
        common.ROOT / "corpus/corpus434_repaired_v1/validation_report.json",
    ]
    files.extend(sorted((common.ROOT / "src/rag_app").glob("*.py")))
    return files


def validate_reference_schema() -> dict[str, Any]:
    references = run_l3_repeats.normalize_references()
    claim_groups = 0
    core_groups = 0
    constraints = 0
    for qid, reference in references.items():
        ledger = reference["ledger"]
        component_ids = {
            row["task_component_id"] for row in ledger["task_components"]
        }
        groups = ledger["claim_groups"]
        claim_groups += len(groups)
        constraints += len(ledger["constraint_groups"])
        for component_id in component_ids:
            core = [
                row
                for row in groups
                if row["task_component_id"] == component_id
                and row["importance"] == "core"
                and row["scoring_role"] == "required_content"
            ]
            if not core:
                raise RuntimeError(
                    f"{qid}/{component_id}: no required core claim group"
                )
            core_groups += len(core)
    return {
        "questions": len(references),
        "claim_groups": claim_groups,
        "required_core_groups": core_groups,
        "constraint_groups": constraints,
    }


def validate_no_paid_outputs() -> None:
    results = common.PACKAGE / "results"
    if not results.exists():
        return
    found = [path for path in results.rglob("*") if path.is_file()]
    if found:
        raise RuntimeError(
            "Test40 formal output files already exist before pre-run freeze: "
            + ", ".join(common.project_relative(path) for path in found)
        )


def validate_runtime_references() -> None:
    for path in sorted((common.PACKAGE / "scripts").glob("*.py")):
        if path.resolve() == Path(__file__).resolve():
            continue
        text = path.read_text(encoding="utf-8")
        for forbidden in FORBIDDEN_RUNTIME_REFERENCES:
            if forbidden in text:
                raise RuntimeError(
                    f"{path.name}: forbidden Dev runtime input {forbidden}"
                )


def collection_fingerprint() -> dict[str, Any]:
    from rag_app.config import get_settings

    settings = get_settings()
    collection = chromadb.PersistentClient(
        path=str(settings.chroma_dir)
    ).get_collection(name=settings.collection_name)
    data = collection.get(include=["documents", "metadatas"])
    ids = data.get("ids") or []
    documents = data.get("documents") or []
    metadatas = data.get("metadatas") or []
    if not (len(ids) == len(documents) == len(metadatas) == 29805):
        raise RuntimeError(
            "Active Chroma collection must contain exactly 29,805 chunks"
        )
    digest = hashlib.sha256()
    for chunk_id, document, metadata in sorted(
        zip(ids, documents, metadatas),
        key=lambda row: str(row[0]),
    ):
        digest.update(
            json.dumps(
                {
                    "id": str(chunk_id),
                    "document": str(document),
                    "metadata": metadata or {},
                },
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
        )
        digest.update(b"\n")
    return {
        "collection_name": settings.collection_name,
        "chunk_count": len(ids),
        "content_sha256": digest.hexdigest(),
    }


def build_manifest(collection: dict[str, Any]) -> dict[str, Any]:
    files = package_files()
    inputs = frozen_inputs()
    return {
        "freeze_id": "test40_formal_v1_pre_run_2026-07-29",
        "status": "pre_run_no_paid_calls",
        "protocol_id": "test40_formal_v1",
        "question_count": 40,
        "systems": ["hybrid", "bge", "bge_llm"],
        "planned_paid_calls": 760,
        "recommended_budget_ceiling_usd": 20.0,
        "required_model_snapshot": common.EXPECTED_MODEL,
        "active_collection": collection,
        "package_files": {
            common.project_relative(path): common.sha256(path) for path in files
        },
        "frozen_inputs": {
            common.project_relative(path): common.sha256(path)
            for path in inputs
        },
        "test40_candidate_outputs_observed": False,
    }


def verify_manifest(expected: dict[str, Any]) -> None:
    if not MANIFEST.exists():
        raise RuntimeError("Pre-run manifest does not exist")
    actual = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if actual != expected:
        raise RuntimeError("Pre-run manifest differs from current package")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-manifest", action="store_true")
    parser.add_argument("--verify-manifest", action="store_true")
    args = parser.parse_args()
    if args.write_manifest == args.verify_manifest:
        raise RuntimeError(
            "Choose exactly one of --write-manifest or --verify-manifest"
        )

    run_validator(
        common.FROZEN_V3 / "scripts/build_freeze_manifest.py",
        "--verify",
    )
    run_validator(
        common.FROZEN_JUDGE / "scripts/validate_frozen_judge.py",
    )
    run_validator(
        common.TEST40_REFERENCE / "scripts/validate_reference_freeze.py",
    )
    run_validator(
        common.PACKAGE / "scripts/build_scoring_reference_v2.py",
        "--verify",
    )
    settings = run_retrieval.validate_settings()
    schema = validate_reference_schema()
    validate_no_paid_outputs()
    validate_runtime_references()
    collection = collection_fingerprint()
    expected = build_manifest(collection)
    if args.write_manifest:
        common.write_json(MANIFEST, expected)
    elif args.verify_manifest:
        verify_manifest(expected)

    report = {
        "status": "PASS",
        "paid_api_calls_made": 0,
        "question_count": 40,
        "gold_record_count": len(common.read_jsonl(common.GOLD)),
        "reference_schema": schema,
        "retrieval_settings": settings,
        "active_collection": collection,
        "package_file_count": len(expected["package_files"]),
        "frozen_input_count": len(expected["frozen_inputs"]),
        "resume_requires_exact_request_hash": True,
        "automatic_sdk_retries": 0,
        "recommended_budget_ceiling_usd": 20.0,
    }
    common.write_json(REPORT, report)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()

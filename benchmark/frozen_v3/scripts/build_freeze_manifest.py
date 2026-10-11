from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import platform
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
V3 = ROOT / "benchmark/frozen_v3"
JUDGE = V3 / "judge"
MANIFEST = V3 / "freeze_manifest.json"

SELECTED_RESULT_ROOTS = (
    V3 / "results/dev13_verified_tags_v3_r2_confirmation_2026-07-26",
    V3 / "results/dev13_neutral_evidence_v3_2026-07-26",
    V3 / "results/dev13_retrieval_budget_gpt51_2026-07-26",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT))


def selected_v3_files() -> list[Path]:
    paths: list[Path] = []
    for path in V3.rglob("*"):
        if not path.is_file():
            continue
        if path == MANIFEST or "__pycache__" in path.parts:
            continue
        if path.is_relative_to(JUDGE):
            continue
        if "results" in path.relative_to(V3).parts and not any(
            path.is_relative_to(result_root)
            for result_root in SELECTED_RESULT_ROOTS
        ):
            continue
        paths.append(path)
    return sorted(paths)


def package_versions() -> dict[str, str]:
    versions: dict[str, str] = {}
    for package in (
        "chromadb",
        "openai",
        "python-dotenv",
        "sentence-transformers",
        "torch",
    ):
        try:
            versions[package] = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            versions[package] = "not-installed"
    return versions


def git_value(*args: str) -> str:
    return subprocess.check_output(
        ("git", *args),
        cwd=ROOT,
        text=True,
    ).strip()


def git_tracked(path: Path) -> bool:
    result = subprocess.run(
        ("git", "ls-files", "--error-unmatch", relative(path)),
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.returncode == 0


def build_manifest() -> dict:
    missing_roots = [
        relative(path) for path in SELECTED_RESULT_ROOTS if not path.is_dir()
    ]
    if missing_roots:
        raise RuntimeError(
            "Cannot freeze before selected result roots exist: "
            + ", ".join(missing_roots)
        )
    v3_files = selected_v3_files()
    tracked_files = [path for path in v3_files if git_tracked(path)]
    untracked_files = [
        relative(path) for path in v3_files if path not in tracked_files
    ]
    if untracked_files:
        raise RuntimeError(
            "Cannot freeze untracked selected files:\n"
            + "\n".join(untracked_files)
        )
    selected_rel = [relative(path) for path in v3_files]
    for args, label in (
        (("diff", "--quiet", "--", *selected_rel), "unstaged"),
        (("diff", "--cached", "--quiet", "--", *selected_rel), "staged"),
    ):
        result = subprocess.run(("git", *args), cwd=ROOT, check=False)
        if result.returncode != 0:
            raise RuntimeError(
                f"Cannot freeze with {label} selected-file changes"
            )
    return {
        "freeze_id": "pfas_rag_frozen_v3_revision3_2026-07-26",
        "status": (
            "frozen_dev13_neutral_evidence_validated_test40_not_run"
        ),
        "freeze_date": "2026-07-26",
        "repository_branch": git_value("branch", "--show-current"),
        "repository_content_commit": git_value("rev-parse", "HEAD"),
        "repository_content_commit_definition": (
            "Clean commit containing every selected file except this "
            "self-excluded manifest; the subsequent release commit adds the "
            "manifest."
        ),
        "v3_files_tracked_at_manifest_build": len(tracked_files),
        "v3_files_untracked_at_manifest_build": (
            len(v3_files) - len(tracked_files)
        ),
        "v3_fully_tracked_at_manifest_build": (
            len(tracked_files) == len(v3_files)
        ),
        "integrity_boundary": (
            "The SHA-256 entries in this manifest define the frozen package "
            "even when the surrounding worktree contains later or unrelated "
            "changes."
        ),
        "nested_packages_excluded": [
            "benchmark/frozen_v3/judge"
        ],
        "self_contained_runtime": True,
        "runtime_dependency_on_frozen_v2": False,
        "runtime_dependency_on_benchmark_reports": False,
        "runtime_dependency_on_shared_benchmark_src": False,
        "question_count": 53,
        "dev_question_count": 13,
        "test_question_count": 40,
        "gold_chunk_count": 249,
        "test40_status": "not_run_for_frozen_v3",
        "canonical_protocol": (
            "benchmark/frozen_v3/methods/frozen_v3_protocol.json"
        ),
        "canonical_result": (
            "benchmark/frozen_v3/results/"
            "dev13_neutral_evidence_v3_2026-07-26"
        ),
        "canonical_result_comparison": "tagged_vs_matched_direct",
        "internal_diagnostic_excluded_from_article": (
            "tagged_vs_matched_untagged"
        ),
        "tagger_free_text_advice_exposed_to_answer": False,
        "judge_model_payload_contains_local_metadata": False,
        "judge_model_payload_contains_task_labels": False,
        "judge_citation_markers_retained": False,
        "required_gold_applicable_dev_questions": 12,
        "negative_gold_applicable_dev_questions": 6,
        "selected_result_roots": [
            relative(path) for path in SELECTED_RESULT_ROOTS
        ],
        "models": {
            "selector_requested": "gpt-5.1",
            "tagger_requested": "gpt-5.1",
            "answer_requested": "gpt-5.1",
            "judge_requested": "gpt-5.1",
            "returned_snapshot": "gpt-5.1-2025-11-13",
            "temperature": 0,
            "cross_encoder": "BAAI/bge-reranker-base",
        },
        "python": platform.python_version(),
        "package_versions": package_versions(),
        "v3_file_count": len(v3_files),
        "v3_file_sha256": {
            relative(path): sha256(path) for path in v3_files
        },
        "external_dependency_count": 0,
        "external_dependency_sha256": {},
    }


def verify(manifest: dict) -> list[str]:
    errors: list[str] = []
    current_paths = {
        relative(path) for path in selected_v3_files()
    }
    recorded_paths = set(manifest["v3_file_sha256"])
    if manifest.get("v3_file_count") != len(recorded_paths):
        errors.append(
            "v3_file_count does not match the number of recorded hashes"
        )
    for rel in sorted(recorded_paths - current_paths):
        errors.append(f"manifest-only path: {rel}")
    for rel in sorted(current_paths - recorded_paths):
        errors.append(f"unmanifested selected path: {rel}")
    for field in ("v3_file_sha256", "external_dependency_sha256"):
        for rel, expected in manifest[field].items():
            path = ROOT / rel
            if not path.is_file():
                errors.append(f"missing: {rel}")
            elif sha256(path) != expected:
                errors.append(f"hash mismatch: {rel}")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--verify",
        action="store_true",
        help="Verify the existing manifest instead of rebuilding it.",
    )
    args = parser.parse_args()
    if args.verify:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        errors = verify(manifest)
        if errors:
            raise SystemExit("\n".join(errors))
        print(
            f"PASS: {manifest['freeze_id']} "
            f"({manifest['v3_file_count']} V3 files, self-contained runtime)"
        )
        return

    manifest = build_manifest()
    MANIFEST.write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {MANIFEST}")


if __name__ == "__main__":
    main()

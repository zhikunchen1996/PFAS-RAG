from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BENCHMARK = ROOT / "benchmark"
RUNS = BENCHMARK / "runs"
REVIEW_TASKS = BENCHMARK / "review_tasks"


REQUIRED_RUNS = {
    "l3_gold_reference_dev13_v2",
    "l3_gold_reference_dev13_v3_continuous",
    "l3_gold_reference_test40_v1",
    "l3_three_repeat_dev13_v2_gpt51judge",
    "stage4_gpt51_dev13_pilot_v1",
    "stage4_multibase_dev13_v1",
    "test40_formal_v1_1",
    "test40_multibase_direct_rag_v1",
    "test40_multibase_l15_v1",
}

REQUIRED_REVIEW_RUNS = {
    "professional_review_v3_formal_v1",
    "professional_review_human_expert_v1",
    "v20_judge_stability_rt02_rt09_v1",
}

REQUIRED_FILES = [
    BENCHMARK / "README.md",
    BENCHMARK / "ablations/README.md",
    BENCHMARK / "frozen_v3/input/questions_all53.csv",
    BENCHMARK / "frozen_v3/input/questions_dev13.csv",
    BENCHMARK / "frozen_v3/input/questions_test40.csv",
    BENCHMARK / "frozen_v3/gold/chunk_based_gold.jsonl",
    BENCHMARK / "frozen_v3/judge/scripts/run_l1_retrieval.py",
    BENCHMARK / "frozen_v3/judge/scripts/run_l15_claim_support.py",
    RUNS / "l3_gold_reference_dev13_v3_continuous/frozen/freeze_manifest_v3.json",
    RUNS / "l3_three_repeat_dev13_v2_gpt51judge/FREEZE_DECISION.md",
    RUNS
    / "l3_gold_reference_test40_v1/frozen/reference_claim_ledgers_test40_v1.jsonl",
    RUNS / "test40_formal_v1_1/results/completion_manifest.json",
    RUNS / "test40_formal_v1_1/results/RESULTS_SUMMARY.md",
    RUNS / "test40_multibase_direct_rag_v1/results/completion_manifest.json",
    RUNS / "test40_multibase_direct_rag_v1/results/RESULTS_SUMMARY.md",
    RUNS / "test40_multibase_l15_v1/completion_manifest.json",
    RUNS / "test40_multibase_l15_v1/RESULTS_SUMMARY.md",
    REVIEW_TASKS / "professional_review_v3_formal_v1/freeze_manifest.json",
    REVIEW_TASKS / "runs/professional_review_v3_formal_v1/summary/summary.json",
    REVIEW_TASKS / "runs/professional_review_human_expert_v1/summary.json",
    REVIEW_TASKS / "runs/professional_review_human_expert_v1/README.md",
    REVIEW_TASKS / "runs/professional_review_human_expert_v1/manifest.json",
    REVIEW_TASKS
    / "runs/professional_review_human_expert_v1/scripts/validate_package.py",
    BENCHMARK / "ablations/dev13_dense_bm25_only_v1/manifest.json",
    BENCHMARK / "ablations/test40_retrieval_answer_cost_v2/manifest.json",
    BENCHMARK
    / "ablations/test40_retrieval_metric_answer_correlation_v1/manifest.json",
]

FORBIDDEN_ACTIVE_PATHS = [
    RUNS / "dev13_common_tagger_ablation_v1",
    BENCHMARK / "ablations/test40_retrieval_answer_cost_v1",
    REVIEW_TASKS / "runs/professional_review_human_deepseek_v4_flash_v1",
    RUNS / "stage4_multibase_dev13_v1/l2_sparse_v1",
    RUNS / "stage4_multibase_dev13_v1/l2_sparse_v2",
    RUNS / "stage4_multibase_dev13_v1/judge_sensitivity_deepseek_v1",
]

def require_directories(parent: Path, names: set[str], label: str) -> None:
    missing = sorted(name for name in names if not (parent / name).is_dir())
    if missing:
        raise SystemExit(f"Missing {label}: {missing}")


def main() -> None:
    require_directories(RUNS, REQUIRED_RUNS, "formal run packages")
    require_directories(
        REVIEW_TASKS / "runs", REQUIRED_REVIEW_RUNS, "professional-review runs"
    )

    missing_files = [str(path.relative_to(ROOT)) for path in REQUIRED_FILES if not path.is_file()]
    if missing_files:
        raise SystemExit(f"Required active files are missing: {missing_files}")

    active_history = [
        str(path.relative_to(ROOT)) for path in FORBIDDEN_ACTIVE_PATHS if path.exists()
    ]
    if active_history:
        raise SystemExit(f"Historical development paths remain active: {active_history}")

    # Independent historical archives are not dependencies of the public package.

    print(
        "ACTIVE BENCHMARK LAYOUT PASS: "
        f"{len(REQUIRED_RUNS)} benchmark packages, "
        f"{len(REQUIRED_REVIEW_RUNS)} professional-review runs, and "
        f"{len(REQUIRED_FILES)} canonical files verified."
    )


if __name__ == "__main__":
    main()

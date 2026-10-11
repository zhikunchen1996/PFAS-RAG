#!/usr/bin/env python3
"""Compare three frozen retrieval metrics with final-answer quality."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

_CACHE = Path(tempfile.gettempdir()) / "rag-python-cache"
_CACHE.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(_CACHE / "matplotlib"))

import numpy as np
import pandas as pd
from scipy.stats import rankdata, spearmanr, t


ROOT = Path(__file__).resolve().parents[4]
PACKAGE = Path(__file__).resolve().parents[1]
RESULTS = PACKAGE / "results"
FIGURES = PACKAGE / "figures"
SOURCE_PACKAGE = ROOT / "benchmark/ablations/test40_retrieval_answer_cost_v2"
CASES = SOURCE_PACKAGE / "results/analysis_cases.csv"
SOURCE_MANIFEST = SOURCE_PACKAGE / "manifest.json"
SOURCE_SCRIPT = SOURCE_PACKAGE / "scripts/run_analysis.py"

METRICS = [
    "MRR_required_gold",
    "required_gold_recall@10",
    "gold_doc_recall@10",
]
METRIC_LABELS = {
    "MRR_required_gold": "MRR of first required gold",
    "required_gold_recall@10": "Required-gold recall@10",
    "gold_doc_recall@10": "Gold-document recall@10",
}
BOOTSTRAP_REPLICATES = 10_000
BOOTSTRAP_SEED = 20260812


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_applicable_cases() -> pd.DataFrame:
    spec = importlib.util.spec_from_file_location("retrieval_answer_cost_v2", SOURCE_SCRIPT)
    source_module = importlib.util.module_from_spec(spec)
    if spec.loader is None:
        raise RuntimeError("Unable to load the V2 source case builder")
    spec.loader.exec_module(source_module)
    frame = source_module.build_cases()
    required = {
        "question_id",
        "system",
        "required_gold_count",
        "l3_mean",
        *METRICS,
    }
    missing = required - set(frame.columns)
    if missing:
        raise RuntimeError(f"Source case table lacks columns: {sorted(missing)}")
    applicable = frame[frame.required_gold_count > 0].copy()
    if len(applicable) != 114 or applicable.question_id.nunique() != 38:
        raise RuntimeError("Expected 114 observations from 38 applicable questions")
    counts = applicable.groupby("question_id").system.nunique()
    if not (counts == 3).all():
        raise RuntimeError("Each applicable question must contain all three systems")
    return applicable.sort_values(["question_id", "system"]).reset_index(drop=True)


def safe_spearman(x: np.ndarray, y: np.ndarray) -> float:
    if np.unique(x).size < 2 or np.unique(y).size < 2:
        return np.nan
    return float(spearmanr(x, y).statistic)


def cluster_robust_spearman_test(
    frame: pd.DataFrame, metric: str
) -> dict[str, float | int | str]:
    """Test a rank association with question-clustered CR1 uncertainty."""

    x = rankdata(frame[metric].to_numpy(dtype=float), method="average")
    y = rankdata(frame.l3_mean.to_numpy(dtype=float), method="average")
    design = np.column_stack([np.ones(len(frame)), x])
    inverse_information = np.linalg.inv(design.T @ design)
    coefficients = inverse_information @ design.T @ y
    residuals = y - design @ coefficients

    clusters = frame.question_id.to_numpy()
    unique_clusters = np.unique(clusters)
    meat = np.zeros((2, 2), dtype=float)
    for cluster in unique_clusters:
        selected = clusters == cluster
        score = design[selected].T @ residuals[selected]
        meat += np.outer(score, score)

    observations = len(frame)
    parameters = design.shape[1]
    cluster_count = len(unique_clusters)
    finite_sample_scale = (cluster_count / (cluster_count - 1)) * (
        (observations - 1) / (observations - parameters)
    )
    covariance = (
        finite_sample_scale
        * inverse_information
        @ meat
        @ inverse_information
    )
    standard_error = float(np.sqrt(covariance[1, 1]))
    test_statistic = float(coefficients[1] / standard_error)
    degrees_of_freedom = cluster_count - 1
    p_value = float(2 * t.sf(abs(test_statistic), df=degrees_of_freedom))
    return {
        "question_cluster_robust_t": test_statistic,
        "question_cluster_degrees_of_freedom": degrees_of_freedom,
        "question_cluster_robust_two_sided_p_value": p_value,
        "p_value_method": (
            "OLS on average ranks with question-clustered CR1 standard errors"
        ),
    }


def benjamini_hochberg(p_values: np.ndarray) -> np.ndarray:
    """Return monotone Benjamini-Hochberg adjusted p values."""

    order = np.argsort(p_values)
    ranked = p_values[order]
    adjusted = ranked * len(ranked) / np.arange(1, len(ranked) + 1)
    adjusted = np.minimum.accumulate(adjusted[::-1])[::-1]
    output = np.empty_like(adjusted)
    output[order] = np.minimum(adjusted, 1.0)
    return output


def question_cluster_bootstrap(
    frame: pd.DataFrame,
    metrics: list[str],
    *,
    replicates: int = BOOTSTRAP_REPLICATES,
    seed: int = BOOTSTRAP_SEED,
) -> np.ndarray:
    """Resample questions and retain every system row for sampled questions."""

    question_ids = sorted(frame.question_id.unique())
    question_index = {question_id: index for index, question_id in enumerate(question_ids)}
    question_codes = frame.question_id.map(question_index).to_numpy(dtype=int)
    metric_values = frame[metrics].to_numpy(dtype=float)
    answer = frame.l3_mean.to_numpy(dtype=float)
    rng = np.random.default_rng(seed)
    values = np.full((replicates, len(metrics)), np.nan)

    for replicate in range(replicates):
        sampled = rng.integers(0, len(question_ids), size=len(question_ids))
        question_weights = np.bincount(sampled, minlength=len(question_ids))
        row_weights = question_weights[question_codes]
        expanded_answer = np.repeat(answer, row_weights)
        for index in range(len(metrics)):
            expanded_metric = np.repeat(metric_values[:, index], row_weights)
            values[replicate, index] = safe_spearman(
                expanded_metric, expanded_answer
            )
    return values


def correlation_outputs(applicable: pd.DataFrame) -> None:
    observed = np.array(
        [safe_spearman(applicable[metric].to_numpy(), applicable.l3_mean.to_numpy()) for metric in METRICS]
    )
    bootstrap = question_cluster_bootstrap(applicable, METRICS)

    rows = []
    for index, metric in enumerate(METRICS):
        valid = bootstrap[:, index][np.isfinite(bootstrap[:, index])]
        low, high = np.quantile(valid, [0.025, 0.975])
        naive = spearmanr(applicable[metric], applicable.l3_mean)
        row = {
            "retrieval_metric": metric,
            "display_label": METRIC_LABELS[metric],
            "answer_metric": "final_answer_quality",
            "spearman_rho": observed[index],
            "question_cluster_bootstrap_95_ci_lower": low,
            "question_cluster_bootstrap_95_ci_upper": high,
            "bootstrap_valid_replicates": len(valid),
            "bootstrap_requested_replicates": BOOTSTRAP_REPLICATES,
            "bootstrap_seed": BOOTSTRAP_SEED,
            "question_system_observations": len(applicable),
            "unique_questions": applicable.question_id.nunique(),
            "naive_unclustered_p_value_do_not_use_for_inference": float(naive.pvalue),
        }
        row.update(cluster_robust_spearman_test(applicable, metric))
        rows.append(row)
    correlation_frame = pd.DataFrame(rows)
    correlation_frame["benjamini_hochberg_q_value_across_three_metrics"] = (
        benjamini_hochberg(
            correlation_frame.question_cluster_robust_two_sided_p_value.to_numpy()
        )
    )
    correlation_frame.to_csv(
        RESULTS / "retrieval_metric_answer_correlations.csv", index=False
    )

    difference_rows = []
    for first, second in ((0, 1), (0, 2), (1, 2)):
        differences = bootstrap[:, first] - bootstrap[:, second]
        valid = differences[np.isfinite(differences)]
        low, high = np.quantile(valid, [0.025, 0.975])
        difference_rows.append(
            {
                "first_metric": METRICS[first],
                "second_metric": METRICS[second],
                "observed_rho_difference": observed[first] - observed[second],
                "question_cluster_bootstrap_95_ci_lower": low,
                "question_cluster_bootstrap_95_ci_upper": high,
                "bootstrap_valid_replicates": len(valid),
                "bootstrap_probability_first_greater_than_second": float(
                    np.mean(valid > 0)
                ),
            }
        )
    pd.DataFrame(difference_rows).to_csv(
        RESULTS / "retrieval_metric_correlation_differences.csv", index=False
    )


def full_retrieval_output(applicable: pd.DataFrame) -> None:
    subset = applicable[np.isclose(applicable["required_gold_recall@10"], 1.0)].copy()
    observed = safe_spearman(
        subset.MRR_required_gold.to_numpy(), subset.l3_mean.to_numpy()
    )
    bootstrap = question_cluster_bootstrap(subset, ["MRR_required_gold"])
    valid = bootstrap[:, 0][np.isfinite(bootstrap[:, 0])]
    low, high = np.quantile(valid, [0.025, 0.975])
    row = {
        "subset": "full_required_gold_retrieval",
        "condition": "required_gold_recall@10 = 1",
        "retrieval_metric": "MRR_required_gold",
        "answer_metric": "final_answer_quality",
        "question_system_observations": len(subset),
        "unique_questions": subset.question_id.nunique(),
        "spearman_rho": observed,
        "question_cluster_bootstrap_95_ci_lower": low,
        "question_cluster_bootstrap_95_ci_upper": high,
        "bootstrap_valid_replicates": len(valid),
        "interpretation": (
            "MRR does not explain the remaining answer variation after all predefined "
            "required-gold chunks are present; full gold does not imply identical contexts."
        ),
    }
    row.update(cluster_robust_spearman_test(subset, "MRR_required_gold"))
    pd.DataFrame([row]).to_csv(
        RESULTS / "full_retrieval_mrr_diagnostic.csv", index=False
    )


def matched_full_retrieval_output(applicable: pd.DataFrame) -> None:
    """Describe questions where every retriever recovered all required gold."""

    recall = applicable.pivot(
        index="question_id", columns="system", values="required_gold_recall@10"
    )
    matched_ids = recall.index[np.isclose(recall, 1.0).all(axis=1)]
    subset = applicable[applicable.question_id.isin(matched_ids)].copy()
    detail_columns = [
        "question_id",
        "system",
        "MRR_required_gold",
        "required_gold_recall@10",
        "gold_doc_recall@10",
        "l3_mean",
    ]
    subset[detail_columns].to_csv(
        RESULTS / "matched_full_retrieval_question_system_rows.csv", index=False
    )
    summary = (
        subset.groupby("system", as_index=False)
        .agg(
            questions=("question_id", "nunique"),
            mean_MRR_required_gold=("MRR_required_gold", "mean"),
            mean_final_answer_quality=("l3_mean", "mean"),
        )
        .sort_values("system")
    )
    summary.to_csv(
        RESULTS / "matched_full_retrieval_system_summary.csv", index=False
    )


def write_summary() -> None:
    correlations = pd.read_csv(RESULTS / "retrieval_metric_answer_correlations.csv")
    differences = pd.read_csv(RESULTS / "retrieval_metric_correlation_differences.csv")
    full = pd.read_csv(RESULTS / "full_retrieval_mrr_diagnostic.csv").iloc[0]
    lines = [
        "# Retrieval-Metric–Answer Correlation Results",
        "",
        "## Overall Associations",
        "",
    ]
    for row in correlations.itertuples():
        lines.append(
            f"- {row.display_label}: Spearman's ρ {row.spearman_rho:.3f} "
            f"(question-cluster-robust t({int(row.question_cluster_degrees_of_freedom)}) "
            f"= {row.question_cluster_robust_t:.3f}, two-sided P = "
            f"{row.question_cluster_robust_two_sided_p_value:.3f}; "
            f"question-cluster bootstrap 95% interval "
            f"{row.question_cluster_bootstrap_95_ci_lower:.3f} to "
            f"{row.question_cluster_bootstrap_95_ci_upper:.3f}; BH-FDR q = "
            f"{row.benjamini_hochberg_q_value_across_three_metrics:.3f})."
        )
    lines += ["", "## Coefficient Comparisons", ""]
    for row in differences.itertuples():
        lines.append(
            f"- {row.first_metric} minus {row.second_metric}: "
            f"{row.observed_rho_difference:.3f} (95% interval "
            f"{row.question_cluster_bootstrap_95_ci_lower:.3f} to "
            f"{row.question_cluster_bootstrap_95_ci_upper:.3f})."
        )
    lines += [
        "",
        "The MRR-minus-required-gold-recall interval includes zero. The data therefore "
        "do not support the hypothesis that MRR is more strongly related to answer "
        "quality than chunk-level required-gold recall.",
        "",
        "## Full-Retrieval Diagnostic",
        "",
        f"Among {int(full.question_system_observations)} observations from "
        f"{int(full.unique_questions)} questions with full required-gold retrieval, "
        f"MRR had Spearman's ρ {full.spearman_rho:.3f} (95% interval "
        f"{full.question_cluster_bootstrap_95_ci_lower:.3f} to "
        f"{full.question_cluster_bootstrap_95_ci_upper:.3f}; "
        f"question-cluster-robust t({int(full.question_cluster_degrees_of_freedom)}) "
        f"= {full.question_cluster_robust_t:.3f}, P = "
        f"{full.question_cluster_robust_two_sided_p_value:.3f}).",
        "",
        "Full required-gold retrieval does not make the complete contexts identical. "
        "Remaining answer differences can reflect non-gold context composition, ordering, "
        "evidence-role tags, valid evidence outside the non-exhaustive gold, and how the "
        "answer model selects and synthesizes evidence.",
        "",
    ]
    matched = pd.read_csv(RESULTS / "matched_full_retrieval_system_summary.csv")
    lines += [
        "## Strict Matched Full-Retrieval Diagnostic",
        "",
        "Only seven questions had full required-gold retrieval under all three "
        "systems. Their descriptive system means were:",
        "",
    ]
    for row in matched.itertuples():
        lines.append(
            f"- {row.system}: mean MRR {row.mean_MRR_required_gold:.3f}; "
            f"mean final-answer quality {row.mean_final_answer_quality:.3f}."
        )
    lines += [
        "",
        "This small matched subset likewise does not support an MRR-only explanation "
        "of final-answer differences.",
        "",
    ]
    (RESULTS / "RESULTS_SUMMARY.md").write_text("\n".join(lines))


def write_manifest() -> None:
    source_files = [
        CASES,
        SOURCE_MANIFEST,
        SOURCE_SCRIPT,
        SOURCE_PACKAGE / "results/retrieval_answer_coupling_retrieval_groups.csv",
        *(ROOT / f"benchmark/runs/test40_formal_v1_1/results/l3/repeat_{repeat}/question_level_scores.csv" for repeat in (1, 2, 3)),
    ]
    package_files = [PACKAGE / "README.md", PACKAGE / "protocol.json", PACKAGE / "MANUSCRIPT_INTEGRATION.md"]
    package_files += sorted((PACKAGE / "scripts").glob("*.py"))
    package_files += sorted((PACKAGE / "tests").glob("*.py"))
    generated_files = sorted(
        path
        for folder in (RESULTS, FIGURES)
        for path in folder.glob("*")
        if path.is_file()
    )
    manifest = {
        "analysis_id": "test40_retrieval_metric_answer_correlation_v1",
        "new_model_calls": False,
        "source_files": [
            {"path": str(path.relative_to(ROOT)), "sha256": sha256(path)}
            for path in source_files
        ],
        "package_files": [
            {"path": str(path.relative_to(PACKAGE)), "sha256": sha256(path)}
            for path in package_files
        ],
        "generated_files": [
            {"path": str(path.relative_to(PACKAGE)), "sha256": sha256(path)}
            for path in generated_files
        ],
    }
    (PACKAGE / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")


def main() -> None:
    for folder in (RESULTS, FIGURES):
        folder.mkdir(parents=True, exist_ok=True)
        for path in folder.iterdir():
            if path.is_file():
                path.unlink()
    applicable = load_applicable_cases()
    correlation_outputs(applicable)
    full_retrieval_output(applicable)
    matched_full_retrieval_output(applicable)
    write_summary()
    subprocess.run(
        [sys.executable, str(PACKAGE / "scripts/build_figures.py")], check=True
    )
    write_manifest()
    print(f"Wrote retrieval-metric analysis for {len(applicable)} observations")


if __name__ == "__main__":
    main()

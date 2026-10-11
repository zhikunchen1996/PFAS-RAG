#!/usr/bin/env python3
"""Validate the retrieval-metric correlation package and source hashes."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[4]
PACKAGE = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    manifest = json.loads((PACKAGE / "manifest.json").read_text())
    assert manifest["analysis_id"] == "test40_retrieval_metric_answer_correlation_v1"
    assert manifest["new_model_calls"] is False
    for section in ("source_files", "package_files", "generated_files"):
        for record in manifest[section]:
            base = ROOT if section == "source_files" else PACKAGE
            path = base / record["path"]
            assert path.is_file(), f"Missing {path}"
            assert sha256(path) == record["sha256"], f"Hash mismatch: {path}"

    correlations = pd.read_csv(RESULTS := PACKAGE / "results/retrieval_metric_answer_correlations.csv")
    assert len(correlations) == 3
    expected = {
        "MRR_required_gold": 0.20590571122702533,
        "required_gold_recall@10": 0.23025610250347656,
        "gold_doc_recall@10": 0.0926160790186478,
    }
    observed = correlations.set_index("retrieval_metric").spearman_rho.to_dict()
    for metric, value in expected.items():
        assert np.isclose(observed[metric], value)
    assert (correlations.bootstrap_valid_replicates == 10_000).all()
    assert (correlations.question_system_observations == 114).all()
    assert (correlations.unique_questions == 38).all()
    expected_p = {
        "MRR_required_gold": 0.11184044730899718,
        "required_gold_recall@10": 0.07452346806465107,
        "gold_doc_recall@10": 0.501580432723519,
    }
    observed_p = correlations.set_index(
        "retrieval_metric"
    ).question_cluster_robust_two_sided_p_value.to_dict()
    for metric, value in expected_p.items():
        assert np.isclose(observed_p[metric], value)
    assert (
        correlations.benjamini_hochberg_q_value_across_three_metrics
        >= correlations.question_cluster_robust_two_sided_p_value
    ).all()

    differences = pd.read_csv(PACKAGE / "results/retrieval_metric_correlation_differences.csv")
    target = differences[
        (differences.first_metric == "MRR_required_gold")
        & (differences.second_metric == "required_gold_recall@10")
    ].iloc[0]
    assert target.question_cluster_bootstrap_95_ci_lower < 0
    assert target.question_cluster_bootstrap_95_ci_upper > 0

    full = pd.read_csv(PACKAGE / "results/full_retrieval_mrr_diagnostic.csv").iloc[0]
    assert int(full.question_system_observations) == 32
    assert int(full.unique_questions) == 14
    assert np.isclose(float(full.spearman_rho), -0.053950445435759505)
    assert np.isclose(
        float(full.question_cluster_robust_two_sided_p_value),
        0.7834815363289285,
    )

    matched = pd.read_csv(PACKAGE / "results/matched_full_retrieval_system_summary.csv")
    assert len(matched) == 3
    assert (matched.questions == 7).all()
    assert np.isclose(
        matched.set_index("system").loc["bge_llm", "mean_MRR_required_gold"],
        1.0,
    )
    print(
        "PASS: hashes, correlations, clustered significance, dependent differences, "
        "and full-retrieval diagnostics are valid"
    )


if __name__ == "__main__":
    main()

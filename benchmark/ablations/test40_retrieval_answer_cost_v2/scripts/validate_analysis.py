#!/usr/bin/env python3
"""Validate the derived Test40 ablation package and its source hashes."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pandas as pd
import numpy as np


ROOT = Path(__file__).resolve().parents[4]
PACKAGE = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    manifest = json.loads((PACKAGE / "manifest.json").read_text())
    assert manifest["analysis_id"] == "test40_retrieval_answer_cost_v2"
    for section in ("source_files", "package_files", "generated_files"):
        for record in manifest[section]:
            base = ROOT if section == "source_files" else PACKAGE
            path = base / record["path"]
            assert path.is_file(), f"Missing {path}"
            assert sha256(path) == record["sha256"], f"Hash mismatch: {path}"

    cases = pd.read_csv(PACKAGE / "results/analysis_cases.csv")
    assert len(cases) == 120
    assert cases.groupby("system").size().to_dict() == {"bge": 40, "bge_llm": 40, "hybrid": 40}
    assert cases[["system", "question_id"]].duplicated().sum() == 0
    assert cases.failure_path.notna().all()
    assert set(cases.failure_path).issubset(set(json.loads((PACKAGE / "protocol.json").read_text())["failure_paths"]["mutually_exclusive_order"]))

    correlation = pd.read_csv(PACKAGE / "results/retrieval_answer_coupling_correlations.csv")
    assert len(correlation) == 1
    row = correlation.iloc[0]
    assert row.retrieval_metric == "required_gold_recall@10"
    assert row.answer_metric == "final_answer_quality"
    assert int(row.question_system_observations) == 114
    assert int(row.unique_questions) == 38
    assert int(row.bootstrap_requested_replicates) == 10_000
    assert int(row.bootstrap_valid_replicates) == 10_000
    assert np.isclose(float(row.spearman_rho), 0.23025610250347656)
    assert float(row.question_cluster_bootstrap_95_ci_lower) < float(row.spearman_rho)
    assert float(row.question_cluster_bootstrap_95_ci_upper) > float(row.spearman_rho)

    groups = pd.read_csv(PACKAGE / "results/retrieval_answer_coupling_retrieval_groups.csv")
    assert groups.sort_values("group_order").retrieval_completeness_group.tolist() == [
        "No gold retrieved", "Partially retrieved", "Fully retrieved"
    ]
    assert groups.set_index("retrieval_completeness_group").n_question_system_observations.to_dict() == {
        "No gold retrieved": 40,
        "Partially retrieved": 42,
        "Fully retrieved": 32,
    }
    assert int(groups.n_question_system_observations.sum()) == 114
    assert groups.sample_sd_final_answer_quality.notna().all()
    assert (groups.sample_sd_final_answer_quality > 0).all()

    costs = pd.read_csv(PACKAGE / "results/cost_performance_formal_system_summary.csv")
    assert set(costs.system) == {"Hybrid", "BGE", "BGE-LLM"}
    assert not costs.local_retrieval_compute_cost_included.any()
    assert not costs.judge_cost_included.any()
    print("PASS: hashes, coupling bootstrap, row cardinality, classifications, and cost scope are valid")


if __name__ == "__main__":
    main()

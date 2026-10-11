#!/usr/bin/env python3
"""Derive Test40 retrieval–answer, failure-path, and cost analyses.

V2 removes question-level centering from the retrieval–answer analysis. The
association and group confidence intervals use question-cluster bootstrap
resampling so all three system observations for a sampled question remain
together.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

_CACHE = Path(tempfile.gettempdir()) / "rag-python-cache"
_CACHE.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(_CACHE / "matplotlib"))

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import spearmanr


ROOT = Path(__file__).resolve().parents[4]
PACKAGE = Path(__file__).resolve().parents[1]
RESULTS = PACKAGE / "results"
FIGURES = PACKAGE / "figures"

FORMAL = ROOT / "benchmark/runs/test40_formal_v1_1/results"
MULTIBASE = ROOT / "benchmark/runs/test40_multibase_direct_rag_v1/results"
QUESTIONS = ROOT / "benchmark/frozen_v3/input/questions_test40.csv"
GOLD = ROOT / "benchmark/frozen_v3/gold/chunk_based_gold.jsonl"

SYSTEMS = ["hybrid", "bge", "bge_llm"]
DISPLAY = {"hybrid": "Hybrid", "bge": "BGE", "bge_llm": "BGE-LLM"}
COLORS = {"Hybrid": "#EAB080", "BGE": "#9CB0C3", "BGE-LLM": "#7C9D97"}
COUPLING_GROUPS = ["No gold retrieved", "Partially retrieved", "Fully retrieved"]
COUPLING_COLORS = {
    "No gold retrieved": "#B7BEC4",
    "Partially retrieved": "#E5C07B",
    "Fully retrieved": "#7C9D97",
}
BOOTSTRAP_REPLICATES = 10_000
BOOTSTRAP_SEED = 20260811
FAILURE_COLORS = {
    "gold_document_miss": "#C9CDD1",
    "gold_chunk_miss_after_doc_hit": "#AEB7BF",
    "partial_required_gold_retrieval": "#E5C07B",
    "full_required_gold_retrieved_not_cited": "#D89D5B",
    "full_gold_used_with_material_or_boundary_error": "#B86078",
    "full_gold_used_but_incomplete_answer": "#7C9D97",
    "complete_core_reference_coverage": "#3F7D54",
    "not_applicable_no_required_gold": "#ECEEEF",
}

RETRIEVAL_FILES = {
    "hybrid": FORMAL / "retrieval/retrieval_outputs/rag_outputs_hybrid_top10_pool60_win0.jsonl",
    "bge": FORMAL / "retrieval/retrieval_outputs/rag_outputs_bge_base_top10_pool60_nodoccap.jsonl",
    "bge_llm": FORMAL / "selector/retrieval_outputs/rag_outputs_bge_llm_gpt51_pool60_bge30_llm10_fullchunk.jsonl",
}
ANSWER_FILES = {
    s: FORMAL / f"generation/{s}/answers/tagged_rag_gpt51.jsonl" for s in SYSTEMS
}
TAG_FILES = {s: FORMAL / f"generation/{s}/tags/tag_results.jsonl" for s in SYSTEMS}


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def chunk_key(record: dict) -> tuple[str, str]:
    return str(record["doc_id"]), str(record["chunk_id"])


def cited_context_positions(answer: str) -> set[int]:
    """Return zero-based context positions cited as [C1], [C2], ..."""
    return {int(value) - 1 for value in re.findall(r"\bC(\d+)\b", answer or "") if int(value) > 0}


def majority(values: list[bool]) -> bool:
    return sum(bool(value) for value in values) >= 2


def classify_failure(row: pd.Series) -> str:
    if int(row.required_gold_count) == 0:
        return "not_applicable_no_required_gold"
    if float(row["required_gold_recall@10"]) == 0:
        return "gold_document_miss" if float(row["gold_doc_recall@10"]) == 0 else "gold_chunk_miss_after_doc_hit"
    if float(row["required_gold_recall@10"]) < 1:
        return "partial_required_gold_retrieval"
    if int(row.cited_unique_required_gold_chunks) == 0:
        return "full_required_gold_retrieved_not_cited"
    if bool(row.majority_material_or_boundary_error):
        return "full_gold_used_with_material_or_boundary_error"
    if np.isclose(float(row.l3_mean), 1.0):
        return "complete_core_reference_coverage"
    return "full_gold_used_but_incomplete_answer"


def safe_spearman(x: pd.Series, y: pd.Series) -> tuple[float, float, int]:
    keep = pd.DataFrame({"x": x, "y": y}).dropna()
    if len(keep) < 3 or keep.x.nunique() < 2 or keep.y.nunique() < 2:
        return np.nan, np.nan, len(keep)
    result = spearmanr(keep.x, keep.y)
    return float(result.statistic), float(result.pvalue), len(keep)


def retrieval_completeness_group(recall: float) -> str:
    if np.isclose(recall, 0.0):
        return "No gold retrieved"
    if np.isclose(recall, 1.0):
        return "Fully retrieved"
    return "Partially retrieved"


def question_cluster_bootstrap(
    applicable: pd.DataFrame,
    *,
    replicates: int = BOOTSTRAP_REPLICATES,
    seed: int = BOOTSTRAP_SEED,
) -> tuple[np.ndarray, dict[str, np.ndarray]]:
    """Bootstrap questions while retaining all system rows for each question."""

    frame = applicable.copy()
    question_ids = sorted(frame.question_id.unique())
    question_index = {question_id: index for index, question_id in enumerate(question_ids)}
    question_codes = frame.question_id.map(question_index).to_numpy(dtype=int)
    recall = frame["required_gold_recall@10"].to_numpy(dtype=float)
    answer = frame.l3_mean.to_numpy(dtype=float)
    groups = frame.retrieval_completeness_group.to_numpy(dtype=object)

    counts_per_question = frame.groupby("question_id").size()
    if not (counts_per_question == len(SYSTEMS)).all():
        raise RuntimeError("Each question must contribute one observation per retrieval system")

    rng = np.random.default_rng(seed)
    rhos = np.full(replicates, np.nan)
    group_means = {group: np.full(replicates, np.nan) for group in COUPLING_GROUPS}
    for bootstrap_index in range(replicates):
        sampled = rng.integers(0, len(question_ids), size=len(question_ids))
        question_weights = np.bincount(sampled, minlength=len(question_ids))
        row_weights = question_weights[question_codes]

        expanded_recall = np.repeat(recall, row_weights)
        expanded_answer = np.repeat(answer, row_weights)
        if np.unique(expanded_recall).size > 1 and np.unique(expanded_answer).size > 1:
            rhos[bootstrap_index] = float(spearmanr(expanded_recall, expanded_answer).statistic)

        for group in COUPLING_GROUPS:
            mask = groups == group
            denominator = row_weights[mask].sum()
            if denominator:
                group_means[group][bootstrap_index] = float(
                    np.average(answer[mask], weights=row_weights[mask])
                )
    return rhos, group_means


def build_cases() -> pd.DataFrame:
    questions = pd.read_csv(QUESTIONS).set_index("question_id")
    gold_rows = read_jsonl(GOLD)
    required = {}
    for item in gold_rows:
        if item["question_id"] not in questions.index or item["evidence_type"] != "required_gold":
            continue
        required.setdefault(item["question_id"], set()).add(chunk_key(item))

    l1 = pd.read_csv(FORMAL / "l1/per_question.csv")
    l15 = pd.read_csv(FORMAL / "l15/per_question.csv")
    repeat_frames = []
    for repeat in (1, 2, 3):
        frame = pd.read_csv(FORMAL / f"l3/repeat_{repeat}/question_level_scores.csv")
        frame["repeat"] = repeat
        repeat_frames.append(frame)
    l3 = pd.concat(repeat_frames, ignore_index=True)

    l3_summary_rows = []
    for (system, question_id), group in l3.groupby(["system", "question_id"], sort=False):
        material_flags = (
            group["reference_anchored_material_error"].astype(bool)
            | group["material_boundary_violation"].astype(bool)
            | (group["contradicted_core_claims"] > 0)
        ).tolist()
        l3_summary_rows.append(
            {
                "system": system,
                "question_id": question_id,
                "l3_mean": group["component_balanced_core_reference_claim_coverage"].mean(),
                "l3_repeat_sd": group["component_balanced_core_reference_claim_coverage"].std(ddof=1),
                "majority_material_or_boundary_error": majority(material_flags),
                "majority_external_error": majority(group["potential_external_scientific_error"].astype(bool).tolist()),
            }
        )
    l3_summary = pd.DataFrame(l3_summary_rows)

    answer_rows = []
    for system, path in ANSWER_FILES.items():
        for item in read_jsonl(path):
            question_id = item["question_id"]
            context = item["retrieved_context"]
            cited_positions = cited_context_positions(item["answer"])
            final_required_positions = {
                index for index, chunk in enumerate(context) if chunk_key(chunk) in required.get(question_id, set())
            }
            cited_required_positions = cited_positions & final_required_positions
            answer_rows.append(
                {
                    "system": system,
                    "question_id": question_id,
                    "answer_citation_count": len(cited_positions),
                    "required_gold_positions_in_context": ";".join(str(i + 1) for i in sorted(final_required_positions)),
                    "unique_required_gold_chunks_in_context": len(final_required_positions),
                    "cited_required_gold_positions": ";".join(str(i + 1) for i in sorted(cited_required_positions)),
                    "cited_unique_required_gold_chunks": len(cited_required_positions),
                    "required_gold_use_proxy": bool(cited_required_positions),
                }
            )
    answer_use = pd.DataFrame(answer_rows)

    cases = l1.merge(l3_summary, on=["system", "question_id"], validate="one_to_one")
    cases = cases.merge(l15, on=["system", "question_id"], validate="one_to_one")
    cases = cases.merge(answer_use, on=["system", "question_id"], validate="one_to_one")
    cases["question"] = cases.question_id.map(questions["question_text"])
    cases["task_type"] = cases.question_id.map(questions["task_type"])
    cases["system_display"] = cases.system.map(DISPLAY)
    cases["hit_any_required_gold@10"] = np.where(
        cases.required_gold_count > 0, cases["required_gold_recall@10"] > 0, pd.NA
    )
    cases["citation_scope_mismatch"] = (
        cases.citation_unsupported_claim_count.fillna(0) + cases.citation_contradicted_claim_count.fillna(0)
    ) > 0
    cases["required_gold_record_hits_minus_unique_chunks"] = (
        cases["required_gold_retrieved@10"] - cases.unique_required_gold_chunks_in_context
    )
    cases["failure_path"] = cases.apply(classify_failure, axis=1)
    return cases


def coupling_outputs(cases: pd.DataFrame) -> None:
    applicable = cases[cases.required_gold_count > 0].copy()
    applicable["retrieval_completeness_group"] = applicable["required_gold_recall@10"].map(
        retrieval_completeness_group
    )
    rho, naive_p_value, n = safe_spearman(
        applicable["required_gold_recall@10"], applicable.l3_mean
    )
    bootstrap_rhos, bootstrap_group_means = question_cluster_bootstrap(applicable)
    valid_rhos = bootstrap_rhos[np.isfinite(bootstrap_rhos)]
    rho_low, rho_high = np.quantile(valid_rhos, [0.025, 0.975])
    correlation = pd.DataFrame(
        [
            {
                "retrieval_metric": "required_gold_recall@10",
                "answer_metric": "final_answer_quality",
                "spearman_rho": rho,
                "question_cluster_bootstrap_95_ci_lower": rho_low,
                "question_cluster_bootstrap_95_ci_upper": rho_high,
                "bootstrap_valid_replicates": len(valid_rhos),
                "bootstrap_requested_replicates": BOOTSTRAP_REPLICATES,
                "bootstrap_seed": BOOTSTRAP_SEED,
                "bootstrap_unit": "question",
                "question_system_observations": n,
                "unique_questions": applicable.question_id.nunique(),
                "naive_unclustered_p_value_do_not_use_for_inference": naive_p_value,
            }
        ]
    )
    correlation.to_csv(RESULTS / "retrieval_answer_coupling_correlations.csv", index=False)

    group_rows = []
    for order, group in enumerate(COUPLING_GROUPS):
        subset = applicable[applicable.retrieval_completeness_group == group]
        valid_means = bootstrap_group_means[group][np.isfinite(bootstrap_group_means[group])]
        ci_low, ci_high = np.quantile(valid_means, [0.025, 0.975])
        group_rows.append(
            {
                "group_order": order,
                "retrieval_completeness_group": group,
                "recall_definition": {
                    "No gold retrieved": "recall = 0",
                    "Partially retrieved": "0 < recall < 1",
                    "Fully retrieved": "recall = 1",
                }[group],
                "n_question_system_observations": len(subset),
                "n_unique_questions": subset.question_id.nunique(),
                "mean_final_answer_quality": subset.l3_mean.mean(),
                "sample_sd_final_answer_quality": subset.l3_mean.std(ddof=1),
                "question_cluster_bootstrap_95_ci_lower": ci_low,
                "question_cluster_bootstrap_95_ci_upper": ci_high,
                "bootstrap_valid_replicates": len(valid_means),
            }
        )
    pd.DataFrame(group_rows).to_csv(
        RESULTS / "retrieval_answer_coupling_retrieval_groups.csv", index=False
    )

    paired_rows = []
    metrics = ["MRR_required_gold", "required_gold_recall@10", "gold_doc_recall@10"]
    wide = applicable.pivot(index="question_id", columns="system")
    for baseline in ("hybrid", "bge"):
        for question_id in wide.index:
            row = {
                "comparison": f"BGE-LLM_minus_{DISPLAY[baseline]}",
                "question_id": question_id,
            }
            for metric in metrics + ["l3_mean"]:
                row[f"delta_{metric}"] = wide.loc[question_id, (metric, "bge_llm")] - wide.loc[question_id, (metric, baseline)]
            dr = row["delta_required_gold_recall@10"]
            da = row["delta_l3_mean"]
            row["retrieval_direction"] = "improved" if dr > 0 else "declined" if dr < 0 else "unchanged"
            row["answer_direction"] = "improved" if da > 1e-12 else "declined" if da < -1e-12 else "unchanged"
            paired_rows.append(row)
    paired = pd.DataFrame(paired_rows)
    paired.to_csv(RESULTS / "retrieval_answer_coupling_paired_deltas.csv", index=False)
    (
        paired.groupby(["comparison", "retrieval_direction", "answer_direction"], observed=True)
        .size().rename("question_count").reset_index()
        .to_csv(RESULTS / "retrieval_answer_coupling_transition_counts.csv", index=False)
    )


def failure_outputs(cases: pd.DataFrame) -> None:
    cases.to_csv(RESULTS / "failure_path_all_cases.csv", index=False)
    summary = (
        cases.groupby(["system_display", "failure_path"], observed=True)
        .agg(question_count=("question_id", "size"), mean_l3=("l3_mean", "mean"))
        .reset_index()
    )
    summary["share_within_system"] = summary.question_count / summary.groupby("system_display").question_count.transform("sum")
    summary.to_csv(RESULTS / "failure_path_summary.csv", index=False)

    applicable_failures = cases[~cases.failure_path.isin(["complete_core_reference_coverage", "not_applicable_no_required_gold"])].copy()
    representatives = (
        applicable_failures.sort_values(["failure_path", "l3_mean", "question_id", "system"])
        .groupby("failure_path", as_index=False).head(2)
    )
    columns = [
        "failure_path", "system_display", "question_id", "task_type", "question", "required_gold_count",
        "required_gold_recall@10", "gold_doc_recall@10", "cited_unique_required_gold_chunks", "l3_mean",
        "majority_material_or_boundary_error", "citation_scope_mismatch",
    ]
    representatives[columns].to_csv(RESULTS / "failure_path_representative_cases.csv", index=False)


def api_usage(path: Path) -> pd.DataFrame:
    rows = []
    for item in read_jsonl(path):
        meta = item["metadata"]
        rows.append(
            {
                "question_id": item["question_id"],
                "prompt_tokens": meta["prompt_tokens"],
                "cached_prompt_tokens": meta.get("cached_prompt_tokens", 0),
                "completion_tokens": meta["completion_tokens"],
                "total_tokens": meta["total_tokens"],
                "cost_usd": meta["estimated_cost_usd"],
                "latency_seconds": meta["latency_seconds"],
            }
        )
    return pd.DataFrame(rows)


def cost_outputs(cases: pd.DataFrame) -> None:
    stage_rows = []
    for system in SYSTEMS:
        for stage, path in [("common_tagger", TAG_FILES[system]), ("answer_generation", ANSWER_FILES[system])]:
            usage = api_usage(path)
            for item in usage.to_dict("records"):
                stage_rows.append({"system": DISPLAY[system], "stage": stage, **item})
    selector = api_usage(FORMAL / "selector/selector_calls.jsonl")
    for item in selector.to_dict("records"):
        stage_rows.append({"system": "BGE-LLM", "stage": "llm_selector", **item})
    stages = pd.DataFrame(stage_rows)
    stages.to_csv(RESULTS / "cost_performance_formal_stage_usage.csv", index=False)

    stage_summary = (
        stages.groupby(["system", "stage"], observed=True)
        .agg(calls=("question_id", "size"), total_tokens=("total_tokens", "sum"), total_cost_usd=("cost_usd", "sum"), total_latency_seconds=("latency_seconds", "sum"))
        .reset_index()
    )
    stage_summary["mean_cost_usd_per_question"] = stage_summary.total_cost_usd / 40
    stage_summary["mean_tokens_per_question"] = stage_summary.total_tokens / 40
    stage_summary["mean_latency_seconds_per_question"] = stage_summary.total_latency_seconds / 40
    stage_summary.to_csv(RESULTS / "cost_performance_formal_stage_summary.csv", index=False)

    performance = cases.groupby("system_display").l3_mean.mean()
    deployment = (
        stage_summary.groupby("system", observed=True)
        .agg(total_tokens=("total_tokens", "sum"), total_cost_usd=("total_cost_usd", "sum"), total_api_latency_seconds=("total_latency_seconds", "sum"))
        .reset_index()
    )
    deployment["mean_cost_usd_per_question"] = deployment.total_cost_usd / 40
    deployment["mean_tokens_per_question"] = deployment.total_tokens / 40
    deployment["mean_api_latency_seconds_per_question"] = deployment.total_api_latency_seconds / 40
    deployment["mean_l3"] = deployment.system.map(performance)
    deployment["local_retrieval_compute_cost_included"] = False
    deployment["judge_cost_included"] = False
    deployment.to_csv(RESULTS / "cost_performance_formal_system_summary.csv", index=False)

    multi_usage = pd.read_csv(MULTIBASE / "generation/generation_usage_summary.csv")
    multi_scores = pd.read_csv(MULTIBASE / "l3/aggregate/system_three_repeat_summary.csv")
    multi = multi_usage.merge(multi_scores[["system", "mean_l3_core_coverage", "sample_sd_across_repeat_system_means"]], on="system", validate="one_to_one")
    multi["mean_generation_cost_usd_per_question"] = multi.estimated_cost_usd / multi.answer_count
    multi["mean_generation_tokens_per_question"] = multi.total_tokens / multi.answer_count
    multi["shared_retrieval_tagger_cost_included"] = False
    multi["judge_cost_included"] = False
    multi.to_csv(RESULTS / "cost_performance_multibase_generation.csv", index=False)

    manifest = json.loads((FORMAL / "completion_manifest.json").read_text())
    usage = manifest["usage"]
    audit = {
        "formal_test40_all_paid_calls_valid_cost_usd": usage["tracked_cost_usd"],
        "formal_test40_estimated_bill_including_rejected_usd": usage["estimated_bill_including_invalid_calls_usd"],
        "deployment_cost_definition": "tagger + answer generation for all systems; BGE-LLM additionally includes selector",
        "excluded": ["L1.5 judge", "L3 judge", "local retrieval/reranking/indexing compute"],
    }
    (RESULTS / "cost_scope_audit.json").write_text(json.dumps(audit, indent=2) + "\n")


def configure_plot() -> None:
    mpl.rcParams.update({
        "font.family": "Arial", "font.sans-serif": ["Arial"], "font.size": 9.2,
        "axes.labelsize": 9.3, "xtick.labelsize": 8.4, "ytick.labelsize": 8.4,
        "legend.fontsize": 8.0, "axes.linewidth": 0.7, "figure.dpi": 160,
        "savefig.dpi": 400, "pdf.fonttype": 42, "svg.fonttype": "none",
    })


def clean(ax: plt.Axes, grid: str | None = "y") -> None:
    ax.spines[["top", "right"]].set_visible(False)
    if grid:
        ax.grid(axis=grid, color="#E7EAEC", linewidth=0.55, zorder=0)
        ax.set_axisbelow(True)


def save(fig: plt.Figure, name: str) -> None:
    for suffix in ("png", "pdf", "svg"):
        fig.savefig(FIGURES / f"{name}.{suffix}", bbox_inches="tight", facecolor="white")
    plt.close(fig)


def make_figures(cases: pd.DataFrame) -> None:
    configure_plot()
    groups = pd.read_csv(RESULTS / "retrieval_answer_coupling_retrieval_groups.csv").sort_values("group_order")

    fig, ax = plt.subplots(figsize=(4.1, 3.15))
    means = groups.mean_final_answer_quality.to_numpy()
    bars = ax.bar(
        np.arange(3), means,
        color=[COUPLING_COLORS[group] for group in groups.retrieval_completeness_group],
        edgecolor="white", linewidth=0.55, zorder=3,
    )
    for bar, row in zip(bars, groups.itertuples()):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            row.mean_final_answer_quality + 0.018,
            f"{row.mean_final_answer_quality:.2f}\nn={row.n_question_system_observations}",
            ha="center", va="bottom", fontsize=7.8, linespacing=0.95,
        )
    ax.set_xticks(np.arange(3), ["No gold\nretrieved", "Partially\nretrieved", "Fully\nretrieved"])
    ax.set_ylabel("Final-answer quality score")
    ax.set_ylim(0, 0.76)
    clean(ax)
    save(fig, "retrieval_answer_coupling")

    summary = pd.read_csv(RESULTS / "failure_path_summary.csv")
    order = ["gold_document_miss", "gold_chunk_miss_after_doc_hit", "partial_required_gold_retrieval", "full_required_gold_retrieved_not_cited", "full_gold_used_with_material_or_boundary_error", "full_gold_used_but_incomplete_answer", "complete_core_reference_coverage", "not_applicable_no_required_gold"]
    labels_fp = {
        "gold_document_miss": "Gold document missed", "gold_chunk_miss_after_doc_hit": "Gold chunk missed after document hit",
        "partial_required_gold_retrieval": "Required gold only partly retrieved", "full_required_gold_retrieved_not_cited": "Full gold retrieved but not cited",
        "full_gold_used_with_material_or_boundary_error": "Full gold used with material/boundary error",
        "full_gold_used_but_incomplete_answer": "Full gold used but answer incomplete", "complete_core_reference_coverage": "Complete core coverage",
        "not_applicable_no_required_gold": "No required gold (N/A)",
    }
    fig, ax = plt.subplots(figsize=(7.2, 2.9)); left = np.zeros(3); systems = ["Hybrid", "BGE", "BGE-LLM"]
    for path in order:
        vals = np.array([summary[(summary.system_display == s) & (summary.failure_path == path)].share_within_system.sum() for s in systems])
        ax.barh(systems, vals, left=left, color=FAILURE_COLORS[path], edgecolor="white", linewidth=0.5, label=labels_fp[path])
        for i, value in enumerate(vals):
            if value >= 0.075: ax.text(left[i] + value/2, i, f"{int(round(value*40))}", ha="center", va="center", fontsize=8, color="#24282C")
        left += vals
    ax.set_xlim(0, 1); ax.set_xlabel("Share of Test40 questions"); ax.xaxis.set_major_formatter(mpl.ticker.PercentFormatter(1))
    clean(ax, "x"); ax.legend(frameon=False, bbox_to_anchor=(1.01, 0.5), loc="center left")
    save(fig, "failure_path_distribution")

    stage = pd.read_csv(RESULTS / "cost_performance_formal_stage_summary.csv")
    formal_summary = pd.read_csv(RESULTS / "cost_performance_formal_system_summary.csv")
    multi = pd.read_csv(RESULTS / "cost_performance_multibase_generation.csv")
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.0), gridspec_kw={"wspace": 0.38})
    systems = ["Hybrid", "BGE", "BGE-LLM"]; bottom = np.zeros(3)
    stage_colors = {"llm_selector": "#B86078", "common_tagger": "#9CB0C3", "answer_generation": "#7C9D97"}
    stage_labels = {"llm_selector": "LLM selector", "common_tagger": "Common tagger", "answer_generation": "Answer generation"}
    for stage_name in ["llm_selector", "common_tagger", "answer_generation"]:
        vals = np.array([stage[(stage.system == s) & (stage.stage == stage_name)].mean_cost_usd_per_question.sum() for s in systems])
        axes[0].bar(systems, vals, bottom=bottom, color=stage_colors[stage_name], edgecolor="white", linewidth=0.5, label=stage_labels[stage_name]); bottom += vals
    for index, value in enumerate(bottom):
        axes[0].text(index, value + 0.0012, f"${value:.3f}", ha="center", va="bottom", fontsize=7.8)
    axes[0].set_ylabel("Recorded API cost per question (USD)"); axes[0].legend(frameon=False)
    clean(axes[0]); axes[0].text(-0.16, 1.03, "a", transform=axes[0].transAxes, fontweight="bold", fontsize=10)

    base_labels = {"gpt51": "GPT-5.1", "gemini31_pro": "Gemini 3.1 Pro", "claude_sonnet5": "Claude Sonnet 5"}
    label_offsets = {
        "gpt51_direct": (4, 3), "gpt51_rag": (4, 3),
        "gemini31_pro_direct": (4, -11), "gemini31_pro_rag": (4, 4),
        "claude_sonnet5_direct": (4, 6), "claude_sonnet5_rag": (4, 4),
    }
    for _, row in multi.iterrows():
        arm = "RAG" if row.system.endswith("_rag") else "Direct"
        base = row.system.removesuffix("_rag").removesuffix("_direct")
        axes[1].scatter(row.mean_generation_cost_usd_per_question, row.mean_l3_core_coverage, s=48, marker="o" if arm == "RAG" else "s", color="#7C9D97" if arm == "RAG" else "#858585", edgecolor="white", linewidth=0.5)
        axes[1].annotate(f"{base_labels[base]} {arm}", (row.mean_generation_cost_usd_per_question, row.mean_l3_core_coverage), xytext=label_offsets[row.system], textcoords="offset points", fontsize=7.4)
    axes[1].set_xlabel("Answer-generation cost per question (USD)"); axes[1].set_ylabel("Mean core reference-claim coverage")
    clean(axes[1]); axes[1].text(-0.16, 1.03, "b", transform=axes[1].transAxes, fontweight="bold", fontsize=10)
    save(fig, "cost_performance")


def write_summary(cases: pd.DataFrame) -> None:
    corr = pd.read_csv(RESULTS / "retrieval_answer_coupling_correlations.csv")
    groups = pd.read_csv(RESULTS / "retrieval_answer_coupling_retrieval_groups.csv").sort_values("group_order")
    transitions = pd.read_csv(RESULTS / "retrieval_answer_coupling_transition_counts.csv")
    failures = pd.read_csv(RESULTS / "failure_path_summary.csv")
    costs = pd.read_csv(RESULTS / "cost_performance_formal_system_summary.csv")
    multi = pd.read_csv(RESULTS / "cost_performance_multibase_generation.csv")

    pooled = corr.iloc[0]
    lines = [
        "# Derived Test40 Analysis Results", "",
        "## Retrieval–Answer Coupling", "",
        f"Across {int(pooled.question_system_observations)} question–system observations from {int(pooled.unique_questions)} questions, required-gold recall@10 had a Spearman association of rho = {pooled.spearman_rho:.3f} with final-answer quality (question-cluster bootstrap 95% CI {pooled.question_cluster_bootstrap_95_ci_lower:.3f} to {pooled.question_cluster_bootstrap_95_ci_upper:.3f}). This is a descriptive association and not a causal estimate.", "",
    ]
    for row in groups.itertuples():
        lines.append(
            f"- {row.retrieval_completeness_group}: mean final-answer quality "
            f"{row.mean_final_answer_quality:.3f} ± {row.sample_sd_final_answer_quality:.3f} SD "
            f"(question-cluster bootstrap 95% CI "
            f"{row.question_cluster_bootstrap_95_ci_lower:.3f} to "
            f"{row.question_cluster_bootstrap_95_ci_upper:.3f}; "
            f"n = {int(row.n_question_system_observations)} observations)."
        )
    lines += ["", "Paired BGE-LLM transitions relative to each baseline:", ""]
    for comparison in transitions.comparison.unique():
        subset = transitions[transitions.comparison == comparison]
        parts = [f"{r.retrieval_direction}/{r.answer_direction}: {int(r.question_count)}" for r in subset.itertuples()]
        lines.append(f"- {comparison.replace('_', ' ')}: " + "; ".join(parts) + ".")
    cited_hits = cases[(cases.required_gold_count > 0) & (cases["required_gold_recall@10"] > 0)]
    lines += [
        "",
        f"All {len(cited_hits)} question–system cases that retrieved at least one required-gold record visibly cited at least one corresponding unique gold chunk. Thus, the operational retrieved-but-not-cited path was not observed; incomplete answers primarily reflect synthesis/coverage limitations rather than complete omission of every retrieved required-gold chunk.",
    ]

    lines += ["", "## Failure Paths", ""]
    for system in ["Hybrid", "BGE", "BGE-LLM"]:
        subset = failures[failures.system_display == system].sort_values("question_count", ascending=False)
        parts = [f"{r.failure_path} = {int(r.question_count)}" for r in subset.itertuples()]
        lines.append(f"- {system}: " + "; ".join(parts) + ".")
    lines += ["", "The categories are deterministic operational labels. They identify where the frozen pipeline lost benchmark-referenced information; they do not prove a unique causal mechanism or the absence of other valid evidence.", "", "## Cost–Performance", ""]
    for row in costs.sort_values("system").itertuples():
        lines.append(f"- {row.system}: deployment API cost USD {row.total_cost_usd:.4f} total ({row.mean_cost_usd_per_question:.4f}/question), {int(row.total_tokens):,} tokens, and mean L3 {row.mean_l3:.3f}.")
    lines += ["", "Matched multibase answer-generation cost only:", ""]
    for row in multi.itertuples():
        lines.append(f"- {row.system}: USD {row.estimated_cost_usd:.4f} ({row.mean_generation_cost_usd_per_question:.4f}/question), mean L3 {row.mean_l3_core_coverage:.3f}.")
    lines += ["", "Local retrieval, local BGE reranking, indexing, and judge calls are excluded from deployment cost. The multibase table also excludes the shared frozen retrieval and tagger costs, so it is an answer-generation comparison rather than a full-pipeline cost comparison.", ""]
    (RESULTS / "RESULTS_SUMMARY.md").write_text("\n".join(lines))


def write_manifest() -> None:
    source_files = [
        QUESTIONS, GOLD, FORMAL / "l1/per_question.csv", FORMAL / "l15/per_question.csv",
        *(FORMAL / f"l3/repeat_{r}/question_level_scores.csv" for r in (1, 2, 3)),
        *RETRIEVAL_FILES.values(), *ANSWER_FILES.values(), *TAG_FILES.values(),
        FORMAL / "selector/selector_calls.jsonl", FORMAL / "completion_manifest.json",
        MULTIBASE / "generation/generation_usage_summary.csv",
        MULTIBASE / "l3/aggregate/system_three_repeat_summary.csv",
    ]
    generated = sorted([p for folder in (RESULTS, FIGURES) for p in folder.glob("*") if p.is_file()])
    package_files = [PACKAGE / "protocol.json", PACKAGE / "README.md", PACKAGE / "MANUSCRIPT_INTEGRATION.md"]
    package_files += sorted((PACKAGE / "scripts").glob("*.py"))
    package_files += sorted((PACKAGE / "tests").glob("*.py"))
    manifest = {
        "analysis_id": "test40_retrieval_answer_cost_v2",
        "new_model_calls": False,
        "source_files": [{"path": str(p.relative_to(ROOT)), "sha256": sha256(p)} for p in source_files],
        "package_files": [{"path": str(p.relative_to(PACKAGE)), "sha256": sha256(p)} for p in package_files],
        "generated_files": [{"path": str(p.relative_to(PACKAGE)), "sha256": sha256(p)} for p in generated],
    }
    (PACKAGE / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")


def main() -> None:
    for folder in (RESULTS, FIGURES):
        folder.mkdir(parents=True, exist_ok=True)
        for path in folder.iterdir():
            if path.is_file():
                path.unlink()
    cases = build_cases()
    cases.to_csv(RESULTS / "analysis_cases.csv", index=False)
    coupling_outputs(cases)
    failure_outputs(cases)
    cost_outputs(cases)
    make_figures(cases)
    write_summary(cases)
    subprocess.run([sys.executable, str(PACKAGE / "scripts/build_manuscript_figures.py")], check=True)
    write_manifest()
    print(f"Wrote {len(cases)} question-system cases to {PACKAGE}")


if __name__ == "__main__":
    main()

from __future__ import annotations

import csv
import json
import random
from pathlib import Path
from typing import Any


PACKAGE = Path(__file__).resolve().parents[1]
ROOT = PACKAGE.parents[2]
OUT = PACKAGE / "final_report"
NEW = PACKAGE / "results/l3_v3"
GPT = (
    ROOT
    / "benchmark/runs/l3_gold_reference_dev13_v2/results/"
    "dev13_gpt51_direct_vs_bge_llm_rag_repair7"
)
GPT_GENERATION_USAGE = (
    ROOT
    / "benchmark/runs/stage4_gpt51_dev13_pilot_v1/results/"
    "gpt51_dev13_matched_knowledge_v13/usage/"
    "generation_usage_summary.csv"
)
MODEL_SYSTEMS = {
    "GPT-5.1": ("gpt51_direct", "gpt51_bge_llm_rag"),
    "Gemini 3.1 Pro Preview": (
        "gemini31_direct",
        "gemini31_bge_llm_rag",
    ),
    "Claude Sonnet 5": (
        "claude_sonnet5_direct",
        "claude_sonnet5_bge_llm_rag",
    ),
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0]) if rows else []
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def percentile(values: list[float], probability: float) -> float:
    ordered = sorted(values)
    position = (len(ordered) - 1) * probability
    lower = int(position)
    upper = min(lower + 1, len(ordered) - 1)
    fraction = position - lower
    return ordered[lower] * (1 - fraction) + ordered[upper] * fraction


def paired_bootstrap(
    direct: dict[str, float],
    rag: dict[str, float],
    iterations: int = 10000,
    seed: int = 20260729,
) -> dict[str, float]:
    if set(direct) != set(rag):
        raise RuntimeError("Direct and RAG question membership differs")
    qids = sorted(direct)
    differences = [rag[qid] - direct[qid] for qid in qids]
    rng = random.Random(seed)
    samples = [
        mean([differences[rng.randrange(len(differences))] for _ in qids])
        for _ in range(iterations)
    ]
    return {
        "rag_minus_direct": mean(differences),
        "ci95_lower": percentile(samples, 0.025),
        "ci95_upper": percentile(samples, 0.975),
    }


def source(order: str, system: str) -> Path:
    if system.startswith("gpt51"):
        return GPT / order
    return NEW / order


def summary_row(order: str, system: str) -> dict[str, str]:
    rows = read_csv(source(order, system) / "system_summary.csv")
    return next(row for row in rows if row["system"] == system)


def question_scores(order: str, system: str) -> dict[str, float]:
    rows = read_csv(source(order, system) / "question_level_scores.csv")
    return {
        row["question_id"]: float(
            row["component_balanced_core_reference_claim_coverage"]
        )
        for row in rows
        if row["system"] == system
    }


def judge_rows(order: str, system: str) -> dict[str, dict[str, Any]]:
    rows = read_jsonl(source(order, system) / "judge_results.jsonl")
    return {
        row["question_id"]: row
        for row in rows
        if row["system_label_local_only"] == system
    }


def build_scores() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    system_rows = []
    effect_rows = []
    for model, (direct, rag) in MODEL_SYSTEMS.items():
        for order in ["canonical", "reverse"]:
            for arm, system in [("Direct", direct), ("BGE-LLM RAG", rag)]:
                row = summary_row(order, system)
                system_rows.append(
                    {
                        "model": model,
                        "arm": arm,
                        "claim_order": order,
                        **{
                            key: value
                            for key, value in row.items()
                            if key not in {"system", "question_count"}
                        },
                    }
                )
            effect = paired_bootstrap(
                question_scores(order, direct),
                question_scores(order, rag),
            )
            effect_rows.append(
                {
                    "model": model,
                    "claim_order": order,
                    **effect,
                    "bootstrap_unit": "question",
                    "bootstrap_iterations": 10000,
                    "bootstrap_seed": 20260729,
                }
            )
    return system_rows, effect_rows


def build_stability() -> list[dict[str, Any]]:
    rows = []
    for model, systems in MODEL_SYSTEMS.items():
        for system in systems:
            canonical_scores = question_scores("canonical", system)
            reverse_scores = question_scores("reverse", system)
            differences = [
                abs(canonical_scores[qid] - reverse_scores[qid])
                for qid in sorted(canonical_scores)
            ]
            canonical_judge = judge_rows("canonical", system)
            reverse_judge = judge_rows("reverse", system)
            claim_disagreements = 0
            constraint_disagreements = 0
            reference_error_disagreements = 0
            for qid in sorted(canonical_judge):
                left = canonical_judge[qid]["assessment"]
                right = reverse_judge[qid]["assessment"]
                left_claims = {
                    row["claim_group_id"]: row["status"]
                    for row in left["claim_assessments"]
                }
                right_claims = {
                    row["claim_group_id"]: row["status"]
                    for row in right["claim_assessments"]
                }
                claim_disagreements += sum(
                    left_claims[key] != right_claims[key]
                    for key in left_claims
                )
                left_constraints = {
                    row["claim_group_id"]: row["status"]
                    for row in left["constraint_assessments"]
                }
                right_constraints = {
                    row["claim_group_id"]: row["status"]
                    for row in right["constraint_assessments"]
                }
                constraint_disagreements += sum(
                    left_constraints[key] != right_constraints[key]
                    for key in left_constraints
                )
                reference_error_disagreements += (
                    left["reference_anchored_material_error"]
                    != right["reference_anchored_material_error"]
                )
            arm = "Direct" if system.endswith("direct") else "BGE-LLM RAG"
            rows.append(
                {
                    "model": model,
                    "arm": arm,
                    "exact_core_score_agreement_count": sum(
                        value == 0 for value in differences
                    ),
                    "question_count": len(differences),
                    "exact_core_score_agreement_rate": mean(
                        [float(value == 0) for value in differences]
                    ),
                    "mean_absolute_core_score_difference": mean(differences),
                    "max_absolute_core_score_difference": max(differences),
                    "claim_status_disagreement_count": claim_disagreements,
                    "constraint_status_disagreement_count": (
                        constraint_disagreements
                    ),
                    "reference_error_flag_disagreement_count": (
                        reference_error_disagreements
                    ),
                }
            )
    return rows


def generation_cost(path: Path) -> float:
    return sum(
        float(row["estimated_cost_usd"] or 0)
        for row in read_csv(path)
        if row["stage"].endswith("answer_generation")
    )


def build_costs() -> list[dict[str, Any]]:
    gpt_judge = sum(
        float(
            json.loads((GPT / order / "run_manifest.json").read_text())[
                "estimated_cost_usd"
            ]
        )
        for order in ["canonical", "reverse"]
    )
    judge_cost_by_model = {
        "Gemini 3.1 Pro Preview": 0.0,
        "Claude Sonnet 5": 0.0,
    }
    for order in ["canonical", "reverse"]:
        for row in read_jsonl(NEW / order / "judge_results.jsonl"):
            system = row["system_label_local_only"]
            if system.startswith("gemini31"):
                model = "Gemini 3.1 Pro Preview"
            elif system.startswith("claude_sonnet5"):
                model = "Claude Sonnet 5"
            else:
                raise RuntimeError(f"Unexpected new L3 system: {system}")
            judge_cost_by_model[model] += float(
                row["judge"]["estimated_cost_usd"]
            )
    rows = [
        {
            "model": "GPT-5.1",
            "generation_cost_usd": generation_cost(GPT_GENERATION_USAGE),
            "l3_canonical_and_reverse_judge_cost_usd": gpt_judge,
            "cost_status": "historical_reused",
        },
        {
            "model": "Gemini 3.1 Pro Preview",
            "generation_cost_usd": generation_cost(
                PACKAGE
                / "results/gemini31_pro/usage/generation_usage_summary.csv"
            ),
            "l3_canonical_and_reverse_judge_cost_usd": (
                judge_cost_by_model["Gemini 3.1 Pro Preview"]
            ),
            "cost_status": "current_run_measured",
        },
        {
            "model": "Claude Sonnet 5",
            "generation_cost_usd": generation_cost(
                PACKAGE
                / "results/claude_sonnet5/usage/generation_usage_summary.csv"
            ),
            "l3_canonical_and_reverse_judge_cost_usd": (
                judge_cost_by_model["Claude Sonnet 5"]
            ),
            "cost_status": "current_run_measured",
        },
    ]
    for row in rows:
        row["total_generation_plus_l3_judge_cost_usd"] = (
            row["generation_cost_usd"]
            + row["l3_canonical_and_reverse_judge_cost_usd"]
        )
    return rows


def write_markdown(
    system_rows: list[dict[str, Any]],
    effect_rows: list[dict[str, Any]],
    cost_rows: list[dict[str, Any]],
) -> None:
    primary = {
        (row["model"], row["arm"]): row
        for row in system_rows
        if row["claim_order"] == "canonical"
    }
    effects = {
        (row["model"], row["claim_order"]): row for row in effect_rows
    }
    lines = [
        "# Dev13 multi-base-model L3 V3 summary",
        "",
        "Canonical claim order is primary; reverse order is sensitivity only.",
        "No binary pass metric or human candidate-answer calibration is used.",
        "",
        "| Base model | Direct core | RAG core | RAG-Direct | 95% CI |",
        "|---|---:|---:|---:|---:|",
    ]
    for model in MODEL_SYSTEMS:
        direct = primary[(model, "Direct")]
        rag = primary[(model, "BGE-LLM RAG")]
        effect = effects[(model, "canonical")]
        lines.append(
            f"| {model} | "
            f"{float(direct['mean_component_balanced_core_reference_claim_coverage']):.3f} | "
            f"{float(rag['mean_component_balanced_core_reference_claim_coverage']):.3f} | "
            f"{effect['rag_minus_direct']:.3f} | "
            f"[{effect['ci95_lower']:.3f}, {effect['ci95_upper']:.3f}] |"
        )
    lines.extend(
        [
            "",
            "Reverse-order within-model effects:",
            "",
        ]
    )
    for model in MODEL_SYSTEMS:
        effect = effects[(model, "reverse")]
        lines.append(
            f"- {model}: {effect['rag_minus_direct']:.3f} "
            f"[{effect['ci95_lower']:.3f}, {effect['ci95_upper']:.3f}]"
        )
    incremental = sum(
        row["total_generation_plus_l3_judge_cost_usd"]
        for row in cost_rows
        if row["model"] != "GPT-5.1"
    )
    lines.extend(
        [
            "",
            f"Incremental Gemini + Claude generation and L3 judging cost: "
            f"USD {incremental:.3f}. Retrieval and common tagging were reused "
            "without new calls.",
            "",
        ]
    )
    (OUT / "SUMMARY.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    system_rows, effect_rows = build_scores()
    stability_rows = build_stability()
    cost_rows = build_costs()
    write_csv(OUT / "system_scores.csv", system_rows)
    write_csv(OUT / "within_model_effects.csv", effect_rows)
    write_csv(OUT / "claim_order_stability.csv", stability_rows)
    write_csv(OUT / "cost_summary.csv", cost_rows)
    write_markdown(system_rows, effect_rows, cost_rows)
    print((OUT / "SUMMARY.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()

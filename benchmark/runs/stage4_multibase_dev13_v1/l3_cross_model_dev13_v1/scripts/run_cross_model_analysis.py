from __future__ import annotations

import csv
import hashlib
import itertools
import json
from pathlib import Path
from typing import Any

import numpy as np


PACKAGE = Path(__file__).resolve().parents[1]
ROOT = PACKAGE.parents[3]
OUT = PACKAGE / "results"
MULTIBASE = (
    ROOT
    / "benchmark/runs/stage4_multibase_dev13_v1/results/l3_v3"
)
GPT = (
    ROOT
    / "benchmark/runs/l3_gold_reference_dev13_v2/results/"
    "dev13_gpt51_direct_vs_bge_llm_rag_repair7"
)
METRIC = "component_balanced_core_reference_claim_coverage"
BOOTSTRAP_ATTEMPTS = 10_000
BOOTSTRAP_SEED = 20260729
SYSTEMS = (
    "gpt51_direct",
    "gpt51_bge_llm_rag",
    "gemini31_direct",
    "gemini31_bge_llm_rag",
    "claude_sonnet5_direct",
    "claude_sonnet5_bge_llm_rag",
)
DISPLAY = {
    "gpt51_direct": "GPT-5.1 Direct",
    "gpt51_bge_llm_rag": "GPT-5.1 RAG",
    "gemini31_direct": "Gemini 3.1 Pro Direct",
    "gemini31_bge_llm_rag": "Gemini 3.1 Pro RAG",
    "claude_sonnet5_direct": "Claude Sonnet 5 Direct",
    "claude_sonnet5_bge_llm_rag": "Claude Sonnet 5 RAG",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def source_path(order: str, source: str) -> Path:
    base = GPT if source == "gpt" else MULTIBASE
    return base / order / "question_level_scores.csv"


def load_scores(order: str) -> tuple[list[str], dict[str, np.ndarray]]:
    gpt_rows = read_csv(source_path(order, "gpt"))
    multibase_rows = read_csv(source_path(order, "multibase"))
    rename = {
        "direct": "gpt51_direct",
        "bge_llm_rag": "gpt51_bge_llm_rag",
        "gpt51_direct": "gpt51_direct",
        "gpt51_bge_llm_rag": "gpt51_bge_llm_rag",
    }
    if len(gpt_rows) != 26 or len(multibase_rows) != 52:
        raise RuntimeError(
            f"{order}: expected 26 GPT and 52 multi-base score rows"
        )
    rows = []
    for row in gpt_rows:
        current = dict(row)
        current["system"] = rename[current["system"]]
        rows.append(current)
    rows.extend(multibase_rows)
    by_system: dict[str, dict[str, float]] = {}
    for row in rows:
        system = row["system"]
        if system not in SYSTEMS:
            continue
        qid = row["question_id"]
        by_system.setdefault(system, {})
        if qid in by_system[system]:
            raise RuntimeError(f"{order}/{system}: duplicate {qid}")
        score = float(row[METRIC])
        if not np.isfinite(score):
            raise RuntimeError(f"{order}/{system}/{qid}: non-finite score")
        by_system[system][qid] = score
    if set(by_system) != set(SYSTEMS):
        raise RuntimeError(f"{order}: incomplete system membership")
    qids = sorted(next(iter(by_system.values())))
    if len(qids) != 13:
        raise RuntimeError(f"{order}: expected 13 questions")
    if any(sorted(values) != qids for values in by_system.values()):
        raise RuntimeError(f"{order}: question membership differs by system")
    return qids, {
        system: np.array([by_system[system][qid] for qid in qids])
        for system in SYSTEMS
    }


def exact_sign_flip_p(differences: np.ndarray) -> float:
    observed = abs(float(differences.mean()))
    signs = np.array(
        list(itertools.product((-1.0, 1.0), repeat=len(differences))),
        dtype=float,
    )
    permuted = np.abs((signs * differences).mean(axis=1))
    return float(np.mean(permuted >= observed - 1e-15))


def holm_adjust(rows: list[dict[str, Any]]) -> None:
    ordered = sorted(
        enumerate(rows),
        key=lambda item: float(item[1]["permutation_p_raw"]),
    )
    running = 0.0
    count = len(rows)
    for rank, (index, row) in enumerate(ordered):
        adjusted = min(
            1.0,
            (count - rank) * float(row["permutation_p_raw"]),
        )
        running = max(running, adjusted)
        rows[index]["permutation_p_holm"] = running


def pairwise(order: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    qids, scores = load_scores(order)
    rng = np.random.default_rng(BOOTSTRAP_SEED)
    indices = rng.integers(
        0,
        len(qids),
        size=(BOOTSTRAP_ATTEMPTS, len(qids)),
    )
    rows: list[dict[str, Any]] = []
    question_rows: list[dict[str, Any]] = []
    for system_a, system_b in itertools.combinations(SYSTEMS, 2):
        differences = scores[system_a] - scores[system_b]
        draws = differences[indices].mean(axis=1)
        mean = float(differences.mean())
        wins = int(np.sum(differences > 1e-15))
        losses = int(np.sum(differences < -1e-15))
        ties = len(differences) - wins - losses
        rows.append(
            {
                "claim_order": order,
                "system_A": system_a,
                "system_B": system_b,
                "display_A": DISPLAY[system_a],
                "display_B": DISPLAY[system_b],
                "mean_A": float(scores[system_a].mean()),
                "mean_B": float(scores[system_b].mean()),
                "mean_delta_A_minus_B": mean,
                "lower_95": float(np.quantile(draws, 0.025)),
                "upper_95": float(np.quantile(draws, 0.975)),
                "question_wins_A": wins,
                "question_ties": ties,
                "question_wins_B": losses,
                "permutation_p_raw": exact_sign_flip_p(differences),
                "permutation_p_holm": 0.0,
                "direction": (
                    "A>B" if mean > 0 else "A<B" if mean < 0 else "tie"
                ),
            }
        )
        for qid, value_a, value_b, difference in zip(
            qids,
            scores[system_a],
            scores[system_b],
            differences,
            strict=True,
        ):
            question_rows.append(
                {
                    "claim_order": order,
                    "question_id": qid,
                    "system_A": system_a,
                    "system_B": system_b,
                    "score_A": float(value_a),
                    "score_B": float(value_b),
                    "delta_A_minus_B": float(difference),
                }
            )
    holm_adjust(rows)
    return rows, question_rows


def system_summary(order: str) -> list[dict[str, Any]]:
    _, scores = load_scores(order)
    ordered = sorted(
        SYSTEMS,
        key=lambda system: -float(scores[system].mean()),
    )
    return [
        {
            "claim_order": order,
            "rank_by_mean": rank,
            "system": system,
            "display": DISPLAY[system],
            "mean_core_coverage": float(scores[system].mean()),
        }
        for rank, system in enumerate(ordered, start=1)
    ]


def matrix(
    canonical_rows: list[dict[str, Any]],
    field: str,
    path: Path,
) -> None:
    lookup: dict[tuple[str, str], float] = {}
    for row in canonical_rows:
        a, b = row["system_A"], row["system_B"]
        value = float(row[field])
        lookup[(a, b)] = value
        lookup[(b, a)] = -value if field == "mean_delta_A_minus_B" else value
    rows = []
    for system_a in SYSTEMS:
        row: dict[str, Any] = {"system": system_a}
        for system_b in SYSTEMS:
            row[system_b] = (
                0.0 if system_a == system_b else lookup[(system_a, system_b)]
            )
        rows.append(row)
    write_csv(path, rows)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    canonical, canonical_questions = pairwise("canonical")
    reverse, reverse_questions = pairwise("reverse")
    canonical_lookup = {
        (row["system_A"], row["system_B"]): row for row in canonical
    }
    reverse_lookup = {
        (row["system_A"], row["system_B"]): row for row in reverse
    }
    stability = []
    for key, primary in canonical_lookup.items():
        sensitivity = reverse_lookup[key]
        primary_delta = float(primary["mean_delta_A_minus_B"])
        sensitivity_delta = float(sensitivity["mean_delta_A_minus_B"])
        stability.append(
            {
                "system_A": key[0],
                "system_B": key[1],
                "canonical_delta": primary_delta,
                "canonical_lower_95": primary["lower_95"],
                "canonical_upper_95": primary["upper_95"],
                "reverse_delta": sensitivity_delta,
                "reverse_lower_95": sensitivity["lower_95"],
                "reverse_upper_95": sensitivity["upper_95"],
                "same_direction": (
                    (primary_delta > 0 and sensitivity_delta > 0)
                    or (primary_delta < 0 and sensitivity_delta < 0)
                    or (primary_delta == 0 and sensitivity_delta == 0)
                ),
                "canonical_holm_p": primary["permutation_p_holm"],
                "reverse_holm_p": sensitivity["permutation_p_holm"],
            }
        )
    summaries = system_summary("canonical") + system_summary("reverse")
    write_csv(OUT / "pairwise_comparisons.csv", canonical + reverse)
    write_csv(
        OUT / "question_level_pair_differences.csv",
        canonical_questions + reverse_questions,
    )
    write_csv(OUT / "system_summary.csv", summaries)
    write_csv(OUT / "claim_order_stability.csv", stability)
    matrix(
        canonical,
        "mean_delta_A_minus_B",
        OUT / "canonical_mean_delta_matrix.csv",
    )
    matrix(
        canonical,
        "permutation_p_holm",
        OUT / "canonical_holm_p_matrix.csv",
    )

    canonical_rank = [
        row for row in summaries if row["claim_order"] == "canonical"
    ]
    lines = [
        "# Dev13 L3 cross-model analysis",
        "",
        "All results reuse frozen L3 V3 question-level scores. No judge or API "
        "was called.",
        "",
        "## Canonical mean ranking",
        "",
        "| Rank | System | Mean core coverage |",
        "|---:|---|---:|",
    ]
    for row in canonical_rank:
        lines.append(
            f"| {row['rank_by_mean']} | {row['display']} | "
            f"{row['mean_core_coverage']:.3f} |"
        )
    significant = [
        row
        for row in canonical
        if float(row["permutation_p_holm"]) < 0.05
    ]
    stable_count = sum(bool(row["same_direction"]) for row in stability)
    lines.extend(
        [
            "",
            "## Statistical summary",
            "",
            f"- Canonical pairwise comparisons: {len(canonical)}",
            f"- Holm-significant canonical comparisons: {len(significant)}",
            f"- Same mean direction in canonical and reverse: "
            f"{stable_count}/{len(stability)}",
            "- Canonical is primary; reverse is sensitivity only.",
            "- Pair-level confidence intervals and adjusted p-values are in "
            "`pairwise_comparisons.csv`.",
            "",
            "This is a post-hoc Dev13 analysis. It does not alter the frozen "
            "judge, reference ledger, answer sets, or Test40 boundary.",
        ]
    )
    (OUT / "SUMMARY.md").write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )
    manifest = {
        "protocol_id": "pfas_rag_dev13_l3_cross_model_v1",
        "status": "completed_local_analysis",
        "new_judge_calls": 0,
        "new_api_calls": 0,
        "bootstrap_attempts": BOOTSTRAP_ATTEMPTS,
        "bootstrap_seed": BOOTSTRAP_SEED,
        "exact_permutations_per_pair": 2**13,
        "pair_count_per_order": 15,
        "canonical_holm_significant_pair_count": len(significant),
        "same_direction_pair_count": stable_count,
        "held_out_test40_used": False,
        "source_sha256": {
            str(source_path(order, source).relative_to(ROOT)): sha256(
                source_path(order, source)
            )
            for order in ("canonical", "reverse")
            for source in ("gpt", "multibase")
        },
    }
    (OUT / "analysis_manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()

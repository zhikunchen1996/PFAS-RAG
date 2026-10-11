from __future__ import annotations

import csv
import hashlib
import json
import statistics
from pathlib import Path
from typing import Any


PACKAGE = Path(__file__).resolve().parents[1]
ROOT = PACKAGE.parents[2]
OUT = PACKAGE / "results"
POST = PACKAGE / "post_run_manifest.json"
SYSTEMS = (
    "gpt51_direct",
    "gpt51_bge_llm_rag",
    "gemini31_direct",
    "gemini31_bge_llm_rag",
    "claude_sonnet5_direct",
    "claude_sonnet5_bge_llm_rag",
)
MAIN = "component_balanced_core_reference_claim_coverage"
STRICT = "strict_core_reference_claim_coverage"
SUPPLEMENTARY = "supplementary_reference_claim_coverage"
CLAIM_VALUES = {
    "full": 1.0,
    "partial": 0.5,
    "absent": 0.0,
    "contradicted": 0.0,
}


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def mean(values: list[float]) -> float:
    return sum(values) / len(values)


def sample_sd(values: list[float]) -> float:
    return statistics.stdev(values)


def load_repeats() -> dict[int, dict[str, dict[str, Any]]]:
    result = {}
    expected: set[str] | None = None
    for repeat in (1, 2, 3):
        rows = read_jsonl(OUT / f"repeat_{repeat}/judge_results.jsonl")
        lookup = {row["item_id"]: row for row in rows}
        if len(lookup) != 78:
            raise RuntimeError(f"Repeat {repeat}: expected 78 judgments")
        if expected is None:
            expected = set(lookup)
        elif set(lookup) != expected:
            raise RuntimeError("Repeat item membership differs")
        result[repeat] = lookup
    return result


def repeat_system_rows(
    repeats: dict[int, dict[str, dict[str, Any]]],
) -> list[dict[str, Any]]:
    rows = []
    for repeat, lookup in repeats.items():
        for system in SYSTEMS:
            selected = [
                row
                for row in lookup.values()
                if row["system_label_local_only"] == system
            ]
            supplementary = [
                float(row["scores"][SUPPLEMENTARY])
                for row in selected
                if row["scores"][SUPPLEMENTARY] is not None
            ]
            rows.append(
                {
                    "repeat": repeat,
                    "system": system,
                    "question_count": len(selected),
                    "primary_core_coverage_mean": mean(
                        [float(row["scores"][MAIN]) for row in selected]
                    ),
                    "strict_core_coverage_mean": mean(
                        [float(row["scores"][STRICT]) for row in selected]
                    ),
                    "supplementary_coverage_mean": mean(supplementary),
                    "supplementary_question_count": len(supplementary),
                    "boundary_violation_rate": mean(
                        [
                            float(
                                row["scores"][
                                    "material_boundary_violation"
                                ]
                            )
                            for row in selected
                        ]
                    ),
                    "core_contradiction_rate": mean(
                        [
                            float(
                                row["scores"]["contradicted_core_claims"] > 0
                            )
                            for row in selected
                        ]
                    ),
                    "reference_anchored_material_error_rate": mean(
                        [
                            float(
                                row["scores"][
                                    "reference_anchored_material_error"
                                ]
                            )
                            for row in selected
                        ]
                    ),
                    "potential_external_error_flag_rate": mean(
                        [
                            float(
                                row["scores"][
                                    "potential_external_scientific_error"
                                ]
                            )
                            for row in selected
                        ]
                    ),
                }
            )
    return rows


def aggregate_system_rows(
    rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    metrics = [
        "primary_core_coverage_mean",
        "strict_core_coverage_mean",
        "supplementary_coverage_mean",
        "boundary_violation_rate",
        "core_contradiction_rate",
        "reference_anchored_material_error_rate",
        "potential_external_error_flag_rate",
    ]
    result = []
    for system in SYSTEMS:
        selected = [row for row in rows if row["system"] == system]
        output: dict[str, Any] = {"system": system, "repeat_count": 3}
        for metric in metrics:
            values = [float(row[metric]) for row in selected]
            output[f"{metric}_three_repeat_mean"] = mean(values)
            output[f"{metric}_repeat_sd"] = sample_sd(values)
            output[f"{metric}_repeat_min"] = min(values)
            output[f"{metric}_repeat_max"] = max(values)
        result.append(output)
    return result


def matched_effects(
    rows: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    lookup = {
        (int(row["repeat"]), row["system"]): row for row in rows
    }
    repeat_rows = []
    pairs = [
        ("gpt51", "gpt51_direct", "gpt51_bge_llm_rag"),
        ("gemini31", "gemini31_direct", "gemini31_bge_llm_rag"),
        (
            "claude_sonnet5",
            "claude_sonnet5_direct",
            "claude_sonnet5_bge_llm_rag",
        ),
    ]
    for repeat in (1, 2, 3):
        for base, direct, rag in pairs:
            effect = (
                float(lookup[(repeat, rag)]["primary_core_coverage_mean"])
                - float(
                    lookup[(repeat, direct)]["primary_core_coverage_mean"]
                )
            )
            repeat_rows.append(
                {
                    "repeat": repeat,
                    "base_model": base,
                    "rag_minus_direct": effect,
                }
            )
    summary = []
    for base, _, _ in pairs:
        values = [
            float(row["rag_minus_direct"])
            for row in repeat_rows
            if row["base_model"] == base
        ]
        summary.append(
            {
                "base_model": base,
                "repeat_count": 3,
                "rag_minus_direct_three_repeat_mean": mean(values),
                "rag_minus_direct_repeat_sd": sample_sd(values),
                "rag_minus_direct_repeat_min": min(values),
                "rag_minus_direct_repeat_max": max(values),
            }
        )
    return repeat_rows, summary


def claim_repeatability(
    repeats: dict[int, dict[str, dict[str, Any]]],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    rows = []
    exact = 0
    total = 0
    for item_id in sorted(repeats[1]):
        assessments = []
        for repeat in (1, 2, 3):
            assessments.append(
                {
                    row["claim_group_id"]: row["status"]
                    for row in repeats[repeat][item_id]["assessment"][
                        "claim_assessments"
                    ]
                }
            )
        for claim_id in sorted(assessments[0]):
            statuses = [
                assessments[index][claim_id] for index in range(3)
            ]
            values = [CLAIM_VALUES[status] for status in statuses]
            agreement = len(set(statuses)) == 1
            exact += int(agreement)
            total += 1
            rows.append(
                {
                    "item_id": item_id,
                    "claim_group_id": claim_id,
                    "repeat_1_status": statuses[0],
                    "repeat_2_status": statuses[1],
                    "repeat_3_status": statuses[2],
                    "three_way_exact_agreement": agreement,
                    "claim_numeric_three_repeat_mean": mean(values),
                    "claim_numeric_repeat_sd": sample_sd(values),
                }
            )
    return rows, {
        "claim_three_way_exact_matches": exact,
        "claim_count": total,
        "claim_three_way_exact_agreement": exact / total,
    }


def main() -> None:
    repeats = load_repeats()
    repeat_rows = repeat_system_rows(repeats)
    system_summary = aggregate_system_rows(repeat_rows)
    effect_rows, effect_summary = matched_effects(repeat_rows)
    claim_rows, claim_summary = claim_repeatability(repeats)
    write_csv(OUT / "repeat_system_metrics.csv", repeat_rows)
    write_csv(OUT / "system_three_repeat_summary.csv", system_summary)
    write_csv(OUT / "matched_effect_by_repeat.csv", effect_rows)
    write_csv(OUT / "matched_effect_three_repeat_summary.csv", effect_summary)
    write_csv(OUT / "claim_repeatability.csv", claim_rows)

    repeat_manifests = [
        json.loads(
            (OUT / f"repeat_{repeat}/run_manifest.json").read_text(
                encoding="utf-8"
            )
        )
        for repeat in (1, 2, 3)
    ]
    summary = {
        "protocol_id": "l3_three_repeat_dev13_v2_gpt51judge",
        "status": "complete",
        "question_count": 13,
        "system_count": 6,
        "repeat_count": 3,
        "judgment_count": 234,
        "new_call_count": sum(
            int(row["new_call_count"]) for row in repeat_manifests
        ),
        "new_call_tokens": sum(
            int(row["new_call_tokens"]) for row in repeat_manifests
        ),
        "new_call_cost_usd": sum(
            float(row["new_call_cost_usd"]) for row in repeat_manifests
        ),
        "new_call_latency_seconds_sum": sum(
            float(row["new_call_latency_seconds_sum"])
            for row in repeat_manifests
        ),
        "bootstrap_enabled": False,
        "error_bar_definition": (
            "sample SD across three complete canonical judge repeats"
        ),
        "reverse_claim_order_new_calls": 0,
        "held_out_test40_used": False,
        **claim_summary,
    }
    (OUT / "aggregation_summary.json").write_text(
        json.dumps(summary, indent=2) + "\n",
        encoding="utf-8",
    )
    paths = sorted(
        path
        for path in PACKAGE.rglob("*")
        if path.is_file()
        and path != POST
        and "__pycache__" not in path.parts
    )
    post = {
        **summary,
        "artifacts": {relative(path): sha256(path) for path in paths},
    }
    POST.write_text(
        json.dumps(post, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()

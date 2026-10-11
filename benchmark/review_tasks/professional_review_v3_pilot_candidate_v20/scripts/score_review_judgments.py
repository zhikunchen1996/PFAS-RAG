#!/usr/bin/env python3
"""Score atomic professional-review judgments deterministically."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import fmean
from typing import Any


STATUS_VALUES = {
    "full": 1.0,
    "partial": 0.5,
    "absent": 0.0,
    "contradicted": 0.0,
}

CALIBRATION_CAPS = {
    "consistent": 1.0,
    "minor_inconsistency": 0.85,
    "material_inconsistency": 0.50,
    "not_assessable": 1.0,
}

DIMENSION_WEIGHTS = {
    "critical_synthesis": 0.40,
    "professional_depth": 0.35,
    "current_research_outlook": 0.25,
}

ATOMIC_OPERATIONS = {
    "critical_synthesis": (
        "comparative_integration",
        "conditional_explanation",
        "tension_limitation_resolution",
        "decision_conclusion",
    ),
    "professional_depth": (
        "mechanism_specificity",
        "context_boundary_specificity",
        "empirical_data_use",
        "endpoint_comparability_discipline",
        "practitioner_decision_support",
        "citation_evidence_integration",
    ),
    "current_research_outlook": (
        "current_development_specificity",
        "specific_gap",
        "consequence_of_gap",
        "testable_priority",
    ),
}


def _score_atomic_group(judgment: dict[str, Any], dimension: str) -> float:
    assessments = judgment[dimension]
    return fmean(
        STATUS_VALUES[assessments[operation]["status"]]
        for operation in ATOMIC_OPERATIONS[dimension]
    )


def score_judgment(judgment: dict[str, Any]) -> dict[str, Any]:
    task_id = judgment["task_id"]
    components = judgment["component_fulfillment"]
    if len(components) != 3:
        raise ValueError("component_fulfillment must contain exactly 3 items")
    component_ids = [component["component_id"] for component in components]
    expected_component_ids = {f"{task_id}-C{index}" for index in range(1, 4)}
    if set(component_ids) != expected_component_ids:
        raise ValueError(
            "component_fulfillment must contain each expected component exactly once"
        )

    constraints = judgment["constraint_assessments"]
    if len(constraints) != 2:
        raise ValueError("constraint_assessments must contain exactly 2 items")
    constraint_ids = [assessment["constraint_id"] for assessment in constraints]
    expected_constraint_ids = {f"{task_id}-B{index}" for index in range(1, 3)}
    if set(constraint_ids) != expected_constraint_ids:
        raise ValueError(
            "constraint_assessments must contain each expected constraint exactly once"
        )

    component_scores = {
        component["component_id"]: STATUS_VALUES[component["status"]]
        for component in components
    }
    component_fulfillment = fmean(component_scores.values())
    dimension_scores = {
        dimension: _score_atomic_group(judgment, dimension)
        for dimension in DIMENSION_WEIGHTS
    }
    uncapped_quality = sum(
        DIMENSION_WEIGHTS[dimension] * score
        for dimension, score in dimension_scores.items()
    )

    calibration_status = judgment["claim_calibration"]["status"]
    calibration_cap = CALIBRATION_CAPS[calibration_status]
    violations = sum(
        assessment["status"] == "material_violation"
        for assessment in constraints
    )
    boundary_cap = 0.50 if violations else 1.0

    # Coverage is a cap rather than another subjective weight. A review cannot
    # score above the fraction of the frozen task it actually fulfills.
    primary = min(
        uncapped_quality,
        component_fulfillment,
        calibration_cap,
        boundary_cap,
    )

    return {
        "task_id": task_id,
        "component_fulfillment_scores": component_scores,
        "mean_component_fulfillment": component_fulfillment,
        "critical_synthesis": dimension_scores["critical_synthesis"],
        "professional_depth": dimension_scores["professional_depth"],
        "current_research_outlook": dimension_scores[
            "current_research_outlook"
        ],
        "uncapped_weighted_review_quality": uncapped_quality,
        "atomic_component_capped_review_quality": primary,
        "active_score_cap": min(
            component_fulfillment,
            calibration_cap,
            boundary_cap,
        ),
        "claim_calibration_status": calibration_status,
        "material_boundary_violation_count": violations,
        "potential_external_scientific_error": judgment[
            "potential_external_scientific_error"
        ],
    }


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records = []
    for line_number, line in enumerate(path.read_text().splitlines(), start=1):
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_number}: invalid JSON") from exc
    return records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_jsonl", type=Path)
    parser.add_argument("output_jsonl", type=Path)
    args = parser.parse_args()

    scored = [score_judgment(record) for record in load_jsonl(args.input_jsonl)]
    args.output_jsonl.parent.mkdir(parents=True, exist_ok=True)
    args.output_jsonl.write_text(
        "".join(json.dumps(record, sort_keys=True) + "\n" for record in scored)
    )


if __name__ == "__main__":
    main()

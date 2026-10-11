"""Frozen L3 continuous scoring logic for the formal Test40 run.

This is the Test40-local copy of the Dev13-developed L3 V3 scoring contract.
It intentionally contains only answer canonicalization, response validation,
and deterministic score calculation. It does not load Dev13 inputs or results.
"""

from __future__ import annotations

import re
from statistics import mean
from typing import Any


CLAIM_VALUES = {
    "full": 1.0,
    "partial": 0.5,
    "absent": 0.0,
    "contradicted": 0.0,
}


def canonicalize_answer(text: str) -> str:
    text = re.sub(
        r"\[(?:C|G)\d+(?:\s*[-\u2013\u2014,;]\s*(?:C|G)?\d+)*\]",
        "",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"(?im)^\s*(?:according to|based on) (?:the )?"
        r"(?:provided|retrieved) (?:context|evidence)[,:]?\s*",
        "",
        text,
    )
    text = re.sub(
        r"(?i)\b(?:the\s+)?(?:provided|retrieved)\s+"
        r"(?:context|evidence)\b",
        lambda match: (
            "The available evidence"
            if match.group(0)[0].isupper()
            else "the available evidence"
        ),
        text,
    )
    text = re.split(
        r"(?im)^\s*(?:references|bibliography)\s*:?\s*$",
        text,
        maxsplit=1,
    )[0]
    text = re.sub(r"\s+([,.;:])", r"\1", text)
    return re.sub(r"[ \t]{2,}", " ", text).strip()


def validate_result(
    result: dict[str, Any],
    reference: dict[str, Any],
) -> None:
    qid = reference["question_id"]
    if result.get("question_id") != qid:
        raise RuntimeError(f"{qid}: judge returned a different question ID")
    content_ids = {
        row["claim_group_id"] for row in reference["ledger"]["claim_groups"]
    }
    content_rows = result.get("claim_assessments", [])
    if not isinstance(content_rows, list):
        raise RuntimeError(f"{qid}: claim assessments are not a list")
    actual_content_ids = [
        row.get("claim_group_id")
        for row in content_rows
        if isinstance(row, dict)
    ]
    if (
        len(actual_content_ids) != len(content_rows)
        or set(actual_content_ids) != content_ids
        or len(actual_content_ids) != len(content_ids)
    ):
        raise RuntimeError(f"{qid}: content claim membership differs")

    constraint_ids = {
        row["claim_group_id"]
        for row in reference["ledger"]["constraint_groups"]
    }
    constraint_rows = result.get("constraint_assessments", [])
    if not isinstance(constraint_rows, list):
        raise RuntimeError(f"{qid}: constraint assessments are not a list")
    actual_constraint_ids = [
        row.get("claim_group_id")
        for row in constraint_rows
        if isinstance(row, dict)
    ]
    if (
        len(actual_constraint_ids) != len(constraint_rows)
        or set(actual_constraint_ids) != constraint_ids
        or len(actual_constraint_ids) != len(constraint_ids)
    ):
        raise RuntimeError(f"{qid}: constraint membership differs")

    for row in content_rows:
        if row.get("status") not in CLAIM_VALUES:
            raise RuntimeError(f"{qid}: invalid claim status")
    for row in constraint_rows:
        if row.get("status") not in {"compliant", "material_violation"}:
            raise RuntimeError(f"{qid}: invalid constraint status")
    for field in [
        "reference_anchored_material_error",
        "potential_external_scientific_error",
    ]:
        if not isinstance(result.get(field), bool):
            raise RuntimeError(f"{qid}: {field} must be boolean")


def score_result(
    result: dict[str, Any],
    reference: dict[str, Any],
) -> dict[str, Any]:
    groups = reference["ledger"]["claim_groups"]
    assessments = {
        row["claim_group_id"]: row for row in result["claim_assessments"]
    }
    components = [
        row["task_component_id"]
        for row in reference["ledger"]["task_components"]
    ]
    component_scores: dict[str, float] = {}
    component_strict_scores: dict[str, float] = {}
    for component_id in components:
        core_ids = [
            row["claim_group_id"]
            for row in groups
            if row["task_component_id"] == component_id
            and row["importance"] == "core"
            and row["scoring_role"] == "required_content"
        ]
        if not core_ids:
            raise RuntimeError(
                f"{reference['question_id']} {component_id}: no core groups"
            )
        component_scores[component_id] = mean(
            CLAIM_VALUES[assessments[group_id]["status"]]
            for group_id in core_ids
        )
        component_strict_scores[component_id] = mean(
            float(assessments[group_id]["status"] == "full")
            for group_id in core_ids
        )

    supplementary_ids = [
        row["claim_group_id"]
        for row in groups
        if row["importance"] == "supplementary"
        or row["scoring_role"] == "optional_content"
    ]
    core_ids = [
        row["claim_group_id"]
        for row in groups
        if row["importance"] == "core"
        and row["scoring_role"] == "required_content"
    ]
    supplementary_coverage = (
        mean(
            CLAIM_VALUES[assessments[group_id]["status"]]
            for group_id in supplementary_ids
        )
        if supplementary_ids
        else None
    )
    return {
        "component_core_coverage": component_scores,
        "component_strict_core_coverage": component_strict_scores,
        "component_balanced_core_reference_claim_coverage": mean(
            component_scores.values()
        ),
        "strict_core_reference_claim_coverage": mean(
            component_strict_scores.values()
        ),
        "supplementary_reference_claim_coverage": supplementary_coverage,
        "contradicted_core_claims": sum(
            assessments[group_id]["status"] == "contradicted"
            for group_id in core_ids
        ),
        "material_boundary_violation": any(
            row["status"] == "material_violation"
            for row in result["constraint_assessments"]
        ),
        "reference_anchored_material_error": bool(
            result["reference_anchored_material_error"]
        ),
        "potential_external_scientific_error": bool(
            result["potential_external_scientific_error"]
        ),
    }

from __future__ import annotations

import argparse
import itertools
import json
import random
import re
from pathlib import Path
from typing import Any

import common


PROMPT = common.PACKAGE / "prompts/l3_gold_referenced_judge_v2.txt"
FROZEN_REFERENCES = (
    common.PACKAGE / "frozen/reference_claim_ledgers_v2.jsonl"
)
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


def answer_text(row: dict[str, Any]) -> str:
    for key in ["answer", "response", "output", "text"]:
        if isinstance(row.get(key), str) and row[key].strip():
            return row[key]
    raise RuntimeError(f"No answer text in row {row.get('question_id', '')}")


def ordered_groups(
    reference: dict[str, Any],
    claim_order: str,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    content = list(reference["ledger"]["claim_groups"])
    constraints = list(reference["ledger"]["constraint_groups"])
    if claim_order == "reverse":
        content.reverse()
        constraints.reverse()
    return content, constraints


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
    actual_content_ids = [row.get("claim_group_id") for row in content_rows]
    if (
        set(actual_content_ids) != content_ids
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
        row.get("claim_group_id") for row in constraint_rows
    ]
    if (
        set(actual_constraint_ids) != constraint_ids
        or len(actual_constraint_ids) != len(constraint_ids)
    ):
        raise RuntimeError(f"{qid}: constraint membership differs")
    for row in result["claim_assessments"]:
        if row.get("status") not in CLAIM_VALUES:
            raise RuntimeError(f"{qid}: invalid claim status")
    for row in result["constraint_assessments"]:
        if row.get("status") not in {"compliant", "material_violation"}:
            raise RuntimeError(f"{qid}: invalid constraint status")
    for field in [
        "reference_anchored_material_error",
        "potential_external_scientific_error",
    ]:
        if not isinstance(result.get(field), bool):
            raise RuntimeError(f"{qid}: {field} must be boolean")


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def percentile(values: list[float], probability: float) -> float:
    if not values:
        raise RuntimeError("Cannot calculate a percentile of no values")
    ordered = sorted(values)
    position = (len(ordered) - 1) * probability
    lower = int(position)
    upper = min(lower + 1, len(ordered) - 1)
    fraction = position - lower
    return ordered[lower] * (1 - fraction) + ordered[upper] * fraction


def paired_question_bootstrap(
    scores_a: dict[str, float],
    scores_b: dict[str, float],
    *,
    iterations: int,
    seed: int,
) -> dict[str, float]:
    if set(scores_a) != set(scores_b) or not scores_a:
        raise RuntimeError("Paired bootstrap requires matching nonempty questions")
    qids = sorted(scores_a)
    differences = [scores_b[qid] - scores_a[qid] for qid in qids]
    point = mean(differences)
    if iterations <= 0:
        return {
            "mean_difference_b_minus_a": point,
            "ci95_lower": point,
            "ci95_upper": point,
        }
    rng = random.Random(seed)
    bootstrapped = [
        mean([differences[rng.randrange(len(differences))] for _ in qids])
        for _ in range(iterations)
    ]
    return {
        "mean_difference_b_minus_a": point,
        "ci95_lower": percentile(bootstrapped, 0.025),
        "ci95_upper": percentile(bootstrapped, 0.975),
    }


def score_result(
    result: dict[str, Any],
    reference: dict[str, Any],
    threshold: float | None = None,
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
            [
                CLAIM_VALUES[assessments[group_id]["status"]]
                for group_id in core_ids
            ]
        )
        component_strict_scores[component_id] = mean(
            [
                float(assessments[group_id]["status"] == "full")
                for group_id in core_ids
            ]
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
    core_coverage = mean(list(component_scores.values()))
    strict_core_coverage = mean(list(component_strict_scores.values()))
    supplementary_coverage = (
        mean(
            [
                CLAIM_VALUES[assessments[group_id]["status"]]
                for group_id in supplementary_ids
            ]
        )
        if supplementary_ids
        else None
    )
    contradicted_core = sum(
        assessments[group_id]["status"] == "contradicted"
        for group_id in core_ids
    )
    boundary_violation = any(
        row["status"] == "material_violation"
        for row in result["constraint_assessments"]
    )
    reference_error = bool(result["reference_anchored_material_error"])
    potential_external_error = bool(
        result["potential_external_scientific_error"]
    )
    passed = None
    if threshold is not None:
        passed = (
            core_coverage >= threshold
            and min(component_scores.values()) >= 0.5
            and contradicted_core == 0
            and not boundary_violation
            and not reference_error
        )
    return {
        "component_core_coverage": component_scores,
        "component_strict_core_coverage": component_strict_scores,
        "component_balanced_core_reference_claim_coverage": core_coverage,
        "strict_core_reference_claim_coverage": strict_core_coverage,
        "supplementary_reference_claim_coverage": supplementary_coverage,
        "contradicted_core_claims": contradicted_core,
        "material_boundary_violation": boundary_violation,
        "reference_anchored_material_error": reference_error,
        "potential_external_scientific_error": potential_external_error,
        "calibrated_threshold": threshold,
        "l3_gold_referenced_adequacy_pass": passed,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--system",
        action="append",
        required=True,
        help="LABEL=path/to/answers.jsonl; may be repeated",
    )
    parser.add_argument("--out", required=True)
    parser.add_argument("--model", default="gpt-4.1-2025-04-14")
    parser.add_argument("--reasoning-effort", default="none")
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--max-completion-tokens", type=int, default=7000)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument(
        "--claim-order",
        choices=["canonical", "reverse"],
        default="canonical",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        help="Dev-calibrated threshold; omit before calibration",
    )
    parser.add_argument("--bootstrap-iterations", type=int, default=10000)
    parser.add_argument("--bootstrap-seed", type=int, default=20260729)
    args = parser.parse_args()

    if not FROZEN_REFERENCES.exists():
        raise RuntimeError("V2 L3 references are not project-author frozen")
    references = {
        row["question_id"]: row
        for row in common.read_jsonl(FROZEN_REFERENCES)
    }
    systems: dict[str, Path] = {}
    for value in args.system:
        label, separator, raw_path = value.partition("=")
        if not separator or not label or not raw_path:
            raise RuntimeError(f"Invalid --system value: {value}")
        systems[label] = Path(raw_path).expanduser().resolve()

    items = []
    for label, path in systems.items():
        rows = {row["question_id"]: row for row in common.read_jsonl(path)}
        if set(rows) != set(references):
            raise RuntimeError(f"{label}: answer membership differs from reference")
        source_hash = common.sha256(path)
        for qid, reference in references.items():
            raw = answer_text(rows[qid])
            normalized = canonicalize_answer(raw)
            content, constraints = ordered_groups(
                reference,
                args.claim_order,
            )
            candidate_id = common.payload_sha256(
                {"question_id": qid, "answer": normalized}
            )[:16]
            payload = {
                "question_id": qid,
                "question": reference["question_text"],
                "task_boundaries": reference["task_boundaries"],
                "task_components": reference["ledger"]["task_components"],
                "content_claim_groups": content,
                "constraint_only_groups": constraints,
                "gold_is_non_exhaustive": True,
                "anonymous_candidate_answer": normalized,
            }
            items.append(
                {
                    "item_id": f"{label}::{qid}",
                    "question_id": qid,
                    "system_label_local_only": label,
                    "candidate_id": candidate_id,
                    "raw_answer_sha256": common.payload_sha256(raw),
                    "canonical_answer_sha256": common.payload_sha256(normalized),
                    "source_answer_file_sha256": source_hash,
                    "model_payload": payload,
                }
            )

    out = Path(args.out).expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)
    common.write_jsonl(out / "local_envelopes.jsonl", items)
    common.write_jsonl(
        out / "model_payloads.jsonl",
        [row["model_payload"] for row in items],
    )
    prompt = PROMPT.read_text(encoding="utf-8")

    def worker(item: dict[str, Any]) -> dict[str, Any]:
        result, metadata = common.call_openai_json(
            system_prompt=prompt,
            payload=item["model_payload"],
            model=args.model,
            reasoning_effort=args.reasoning_effort,
            max_completion_tokens=args.max_completion_tokens,
            temperature=args.temperature,
        )
        reference = references[item["question_id"]]
        validate_result(result, reference)
        return {
            "item_id": item["item_id"],
            "question_id": item["question_id"],
            "system_label_local_only": item["system_label_local_only"],
            "candidate_id": item["candidate_id"],
            "assessment": result,
            "scores": score_result(result, reference, args.threshold),
            "judge": metadata,
        }

    rows = common.run_parallel(
        items=items,
        worker=worker,
        key=lambda row: str(row["item_id"]),
        output=out / "judge_results.jsonl",
        workers=args.workers,
        resume=args.resume,
    )
    summaries = []
    for label in systems:
        selected = [
            row for row in rows if row["system_label_local_only"] == label
        ]
        supplementary = [
            row["scores"]["supplementary_reference_claim_coverage"]
            for row in selected
            if row["scores"]["supplementary_reference_claim_coverage"]
            is not None
        ]
        summary = {
            "system": label,
            "question_count": len(selected),
            "mean_component_balanced_core_reference_claim_coverage": mean(
                [
                    row["scores"][
                        "component_balanced_core_reference_claim_coverage"
                    ]
                    for row in selected
                ]
            ),
            "mean_strict_core_reference_claim_coverage": mean(
                [
                    row["scores"]["strict_core_reference_claim_coverage"]
                    for row in selected
                ]
            ),
            "mean_supplementary_reference_claim_coverage": (
                mean(supplementary) if supplementary else ""
            ),
            "boundary_compliance_rate": mean(
                [
                    float(not row["scores"]["material_boundary_violation"])
                    for row in selected
                ]
            ),
            "core_contradiction_rate": mean(
                [
                    float(row["scores"]["contradicted_core_claims"] > 0)
                    for row in selected
                ]
            ),
            "reference_anchored_material_error_rate": mean(
                [
                    float(row["scores"]["reference_anchored_material_error"])
                    for row in selected
                ]
            ),
            "potential_external_error_flag_rate": mean(
                [
                    float(
                        row["scores"]["potential_external_scientific_error"]
                    )
                    for row in selected
                ]
            ),
        }
        if args.threshold is not None:
            summary["l3_gold_referenced_adequacy_pass_rate"] = mean(
                [
                    float(row["scores"]["l3_gold_referenced_adequacy_pass"])
                    for row in selected
                ]
            )
        summaries.append(summary)
    common.write_csv(out / "system_summary.csv", summaries)
    question_scores = [
        {
            "system": row["system_label_local_only"],
            "question_id": row["question_id"],
            "component_balanced_core_reference_claim_coverage": row["scores"][
                "component_balanced_core_reference_claim_coverage"
            ],
            "strict_core_reference_claim_coverage": row["scores"][
                "strict_core_reference_claim_coverage"
            ],
            "supplementary_reference_claim_coverage": row["scores"][
                "supplementary_reference_claim_coverage"
            ],
            "contradicted_core_claims": row["scores"][
                "contradicted_core_claims"
            ],
            "material_boundary_violation": row["scores"][
                "material_boundary_violation"
            ],
            "reference_anchored_material_error": row["scores"][
                "reference_anchored_material_error"
            ],
            "potential_external_scientific_error": row["scores"][
                "potential_external_scientific_error"
            ],
            "component_core_coverage_json": json.dumps(
                row["scores"]["component_core_coverage"],
                sort_keys=True,
            ),
            "component_strict_core_coverage_json": json.dumps(
                row["scores"]["component_strict_core_coverage"],
                sort_keys=True,
            ),
        }
        for row in rows
    ]
    common.write_csv(out / "question_level_scores.csv", question_scores)
    scores_by_system = {
        label: {
            row["question_id"]: row["scores"][
                "component_balanced_core_reference_claim_coverage"
            ]
            for row in rows
            if row["system_label_local_only"] == label
        }
        for label in systems
    }
    paired_comparisons = []
    for comparison_index, (system_a, system_b) in enumerate(
        itertools.combinations(systems, 2)
    ):
        paired_comparisons.append(
            {
                "system_a": system_a,
                "system_b": system_b,
                **paired_question_bootstrap(
                    scores_by_system[system_a],
                    scores_by_system[system_b],
                    iterations=args.bootstrap_iterations,
                    seed=args.bootstrap_seed + comparison_index,
                ),
                "bootstrap_unit": "question",
                "bootstrap_iterations": args.bootstrap_iterations,
                "bootstrap_seed": args.bootstrap_seed + comparison_index,
            }
        )
    common.write_csv(out / "paired_comparisons.csv", paired_comparisons)
    common.write_json(
        out / "run_manifest.json",
        {
            "protocol_id": "l3_gold_reference_dev13_v2",
            "reference_sha256": common.sha256(FROZEN_REFERENCES),
            "prompt_sha256": common.sha256(PROMPT),
            "request_model": args.model,
            "reasoning_effort": args.reasoning_effort,
            "temperature": args.temperature,
            "claim_order": args.claim_order,
            "threshold": args.threshold,
            "bootstrap_unit": "question",
            "bootstrap_iterations": args.bootstrap_iterations,
            "bootstrap_seed": args.bootstrap_seed,
            "citation_markers_removed": True,
            "bibliography_removed": True,
            "candidate_system_count": len(systems),
            "candidate_answer_count": len(rows),
            "total_tokens": sum(row["judge"]["total_tokens"] for row in rows),
            "estimated_cost_usd": sum(
                row["judge"]["estimated_cost_usd"] for row in rows
            ),
            "latency_seconds_sum": sum(
                row["judge"]["latency_seconds"] for row in rows
            ),
        },
    )
    print(json.dumps(summaries, indent=2))


if __name__ == "__main__":
    main()

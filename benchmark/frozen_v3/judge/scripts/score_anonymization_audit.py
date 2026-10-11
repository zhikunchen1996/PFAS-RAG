from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any

import judge_common as common


SYSTEMS = {"hybrid", "bge", "bge_llm"}
SLOTS = {"X", "Y", "Z"}


def fixed_point_tail(question_count: int, observed: int) -> float:
    distribution = {0: 1.0}
    single = {0: 2 / 6, 1: 3 / 6, 3: 1 / 6}
    for _ in range(question_count):
        updated: dict[int, float] = defaultdict(float)
        for total, probability in distribution.items():
            for value, increment in single.items():
                updated[total + value] += probability * increment
        distribution = dict(updated)
    return sum(
        probability
        for total, probability in distribution.items()
        if total >= observed
    )


def binomial_tail(n: int, observed: int, probability: float) -> float:
    return sum(
        math.comb(n, value)
        * probability**value
        * (1 - probability) ** (n - value)
        for value in range(observed, n + 1)
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", required=True)
    parser.add_argument("--predictions", required=True)
    parser.add_argument("--deterministic-scan", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    key_rows = common.read_jsonl(Path(args.key))
    key = {row["audit_id"]: row for row in key_rows}
    predictions_raw = json.loads(
        Path(args.predictions).read_text(encoding="utf-8")
    )
    predictions = {
        row["audit_id"]: row
        for row in predictions_raw["assignments"]
    }
    if set(predictions) != set(key):
        raise ValueError("Prediction audit IDs do not match the local key")

    per_question: list[dict[str, Any]] = []
    total_correct = 0
    complete_correct = 0
    for audit_id in sorted(key):
        truth = key[audit_id]["slot_to_system"]
        predicted = predictions[audit_id]["slot_to_system"]
        if set(predicted) != SLOTS or set(predicted.values()) != SYSTEMS:
            raise ValueError(f"{audit_id}: invalid one-to-one assignment")
        correct = sum(predicted[slot] == truth[slot] for slot in SLOTS)
        total_correct += correct
        complete_correct += correct == 3
        per_question.append(
            {
                "audit_id": audit_id,
                "question_id": key[audit_id]["question_id"],
                "correct_assignments": correct,
                "complete_mapping_correct": correct == 3,
                "confidence": predictions[audit_id].get("confidence", ""),
                "rationale": predictions[audit_id].get("rationale", ""),
            }
        )

    question_count = len(key)
    assignment_count = question_count * 3
    assignment_p = fixed_point_tail(question_count, total_correct)
    complete_p = binomial_tail(question_count, complete_correct, 1 / 6)
    deterministic = json.loads(
        Path(args.deterministic_scan).read_text(encoding="utf-8")
    )
    no_above_chance_evidence = assignment_p >= 0.05 and complete_p >= 0.05
    status = (
        "passed_no_evidence_of_above_chance_identity_inference"
        if deterministic["status"] == "passed"
        and no_above_chance_evidence
        else "failed_requires_review"
    )
    summary = {
        "status": status,
        "deterministic_scan_status": deterministic["status"],
        "question_count": question_count,
        "assignment_count": assignment_count,
        "correct_assignments": total_correct,
        "assignment_accuracy": total_correct / assignment_count,
        "assignment_chance_level": 1 / 3,
        "assignment_exact_null_tail_p": assignment_p,
        "complete_mappings_correct": complete_correct,
        "complete_mapping_accuracy": complete_correct / question_count,
        "complete_mapping_chance_level": 1 / 6,
        "complete_mapping_exact_binomial_tail_p": complete_p,
        "interpretation": (
            "Failure to reject chance is evidence of no detected identity "
            "leakage, not proof that identity is impossible to infer."
        ),
    }
    out = Path(args.out).expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)
    common.write_csv(out / "per_question.csv", per_question)
    common.write_json(out / "summary.json", summary)


if __name__ == "__main__":
    main()

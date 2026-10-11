from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
ROOT = PACKAGE.parents[2]
V2 = ROOT / "benchmark/runs/l3_gold_reference_dev13_v2"
RESULTS = V2 / "results/dev13_gpt51_direct_vs_bge_llm_rag_repair7"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def close(actual: float, expected: float, tolerance: float = 1e-12) -> bool:
    return abs(actual - expected) <= tolerance


def main() -> None:
    errors: list[str] = []
    protocol = json.loads(
        (PACKAGE / "protocol.json").read_text(encoding="utf-8")
    )
    binary = protocol.get("binary_evaluation", {})
    if protocol.get("protocol_id") != "l3_gold_reference_v3_continuous":
        errors.append("Unexpected protocol ID")
    if binary.get("enabled") is not False or binary.get("threshold") is not None:
        errors.append("Binary evaluation is enabled or has a threshold")
    if binary.get("human_candidate_adequacy_labels_collected") != 0:
        errors.append("Protocol claims candidate-answer human labels")
    if binary.get("human_candidate_adequacy_labels_used") is not False:
        errors.append("Protocol uses candidate-answer human labels")
    if protocol["development_boundary"]["test40_l3_evaluated_before_freeze"]:
        errors.append("Protocol claims a pre-freeze Test40 L3 run")

    copied_reference = PACKAGE / "frozen/reference_claim_ledgers_v2.jsonl"
    source_reference = V2 / "frozen/reference_claim_ledgers_v2.jsonl"
    copied_prompt = PACKAGE / "frozen/l3_gold_referenced_judge_v2.txt"
    source_prompt = V2 / "prompts/l3_gold_referenced_judge_v2.txt"
    expected_reference_hash = protocol["frozen_reference"]["sha256"]
    if sha256(copied_reference) != expected_reference_hash:
        errors.append("Copied reference hash differs from protocol")
    if sha256(copied_reference) != sha256(source_reference):
        errors.append("V3 reference differs from frozen V2 reference")
    if sha256(copied_prompt) != sha256(source_prompt):
        errors.append("V3 judge prompt differs from frozen V2 prompt")

    register = read_csv(
        V2 / "human_adequacy_calibration_repair7/adequacy_register.csv"
    )
    if len(register) != 26:
        errors.append(f"Expected 26 blinded candidates, found {len(register)}")
    if any(row.get("adequacy_decision") != "pending" for row in register):
        errors.append("At least one candidate adequacy decision is not pending")
    if any(
        row.get("material_scientific_error") != "pending" for row in register
    ):
        errors.append("At least one material-error decision is not pending")
    for field in ["confidence", "review_date", "notes"]:
        if any((row.get(field) or "").strip() for row in register):
            errors.append(f"At least one human calibration {field} is populated")

    runner_text = (
        PACKAGE / "scripts/run_l3_continuous_scoring_v3.py"
    ).read_text(encoding="utf-8")
    for forbidden in [
        '"--threshold"',
        "l3_gold_referenced_adequacy_pass",
        "calibrated_threshold",
    ]:
        if forbidden in runner_text:
            errors.append(f"Continuous runner contains forbidden token: {forbidden}")

    expected_scores = {
        "canonical": {
            "gpt51_direct": 0.4455128205128205,
            "gpt51_bge_llm_rag": 0.6442307692307693,
        },
        "reverse": {
            "gpt51_direct": 0.4807692307692308,
            "gpt51_bge_llm_rag": 0.6335470085470085,
        },
    }
    for order, systems in expected_scores.items():
        manifest = json.loads(
            (RESULTS / order / "run_manifest.json").read_text(encoding="utf-8")
        )
        if manifest.get("threshold") is not None:
            errors.append(f"{order}: inherited run used a binary threshold")
        if manifest.get("claim_order") != order:
            errors.append(f"{order}: inherited run claim order differs")
        if manifest.get("candidate_answer_count") != 26:
            errors.append(f"{order}: inherited run does not contain 26 answers")
        summaries = {
            row["system"]: row
            for row in read_csv(RESULTS / order / "system_summary.csv")
        }
        for system, expected in systems.items():
            actual = float(
                summaries[system][
                    "mean_component_balanced_core_reference_claim_coverage"
                ]
            )
            if not close(actual, expected):
                errors.append(f"{order}/{system}: core score changed")

    stability = json.loads(
        (RESULTS / "stability_summary_sealed.json").read_text(encoding="utf-8")
    )
    if stability.get("candidate_answer_count") != 26:
        errors.append("Stability analysis answer count differs")

    freeze = json.loads(
        (PACKAGE / "frozen/freeze_manifest_v3.json").read_text(encoding="utf-8")
    )
    if freeze.get("test40_l3_evaluated") is not False:
        errors.append("Freeze manifest does not preserve the Test40 boundary")
    for relative, expected_hash in freeze.get("artifacts", {}).items():
        path = ROOT / relative
        if not path.exists() or sha256(path) != expected_hash:
            errors.append(f"Frozen artifact mismatch: {relative}")

    report = {
        "protocol_id": "l3_gold_reference_v3_continuous",
        "status": "pass" if not errors else "fail",
        "errors": errors,
        "human_candidate_adequacy_labels_collected": 0,
        "binary_metrics_enabled": False,
        "test40_l3_evaluated": False,
    }
    print(json.dumps(report, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

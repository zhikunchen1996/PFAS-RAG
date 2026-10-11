from __future__ import annotations

import csv
import importlib.util
import json
import sys
import unittest
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
V2 = PACKAGE.parent / "l3_gold_reference_dev13_v2"
RUNNER_PATH = PACKAGE / "scripts/run_l3_continuous_scoring_v3.py"
sys.path.insert(0, str(PACKAGE / "scripts"))
SPEC = importlib.util.spec_from_file_location("l3_v3_runner", RUNNER_PATH)
assert SPEC and SPEC.loader
RUNNER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(RUNNER)


class ContinuousProtocolTests(unittest.TestCase):
    def test_binary_evaluation_is_disabled(self) -> None:
        protocol = json.loads(
            (PACKAGE / "protocol.json").read_text(encoding="utf-8")
        )
        binary = protocol["binary_evaluation"]
        self.assertFalse(binary["enabled"])
        self.assertIsNone(binary["threshold"])
        self.assertFalse(binary["human_candidate_adequacy_labels_used"])

    def test_all_blinded_labels_remain_pending(self) -> None:
        path = (
            V2
            / "human_adequacy_calibration_repair7"
            / "adequacy_register.csv"
        )
        with path.open(encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 26)
        self.assertEqual({row["adequacy_decision"] for row in rows}, {"pending"})
        self.assertEqual(
            {row["material_scientific_error"] for row in rows},
            {"pending"},
        )

    def test_continuous_score_has_no_pass_fields(self) -> None:
        reference = {
            "question_id": "Q",
            "ledger": {
                "task_components": [{"task_component_id": "Q-T01"}],
                "claim_groups": [
                    {
                        "claim_group_id": "Q-G01",
                        "task_component_id": "Q-T01",
                        "importance": "core",
                        "scoring_role": "required_content",
                    }
                ],
            },
        }
        result = {
            "claim_assessments": [
                {"claim_group_id": "Q-G01", "status": "partial"}
            ],
            "constraint_assessments": [],
            "reference_anchored_material_error": False,
            "potential_external_scientific_error": False,
        }
        score = RUNNER.score_result(result, reference)
        self.assertEqual(
            score["component_balanced_core_reference_claim_coverage"],
            0.5,
        )
        self.assertNotIn("l3_gold_referenced_adequacy_pass", score)
        self.assertNotIn("calibrated_threshold", score)

    def test_paired_bootstrap_is_question_clustered(self) -> None:
        result = RUNNER.paired_question_bootstrap(
            {"Q1": 0.0, "Q2": 0.5},
            {"Q1": 0.5, "Q2": 1.0},
            iterations=100,
            seed=20260729,
        )
        self.assertEqual(result["mean_difference_b_minus_a"], 0.5)


if __name__ == "__main__":
    unittest.main()

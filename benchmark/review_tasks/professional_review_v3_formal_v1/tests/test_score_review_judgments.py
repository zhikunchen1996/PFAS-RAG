from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import json
import unittest


SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "score_review_judgments.py"
)
SPEC = spec_from_file_location("score_review_judgments", SCRIPT)
MODULE = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class ScoreReviewJudgmentTests(unittest.TestCase):
    def test_atomic_operation_contract_matches_schema(self):
        expected_professional_depth = (
            "mechanism_specificity",
            "context_boundary_specificity",
            "empirical_data_use",
            "endpoint_comparability_discipline",
            "practitioner_decision_support",
            "citation_evidence_integration",
        )
        self.assertEqual(
            MODULE.ATOMIC_OPERATIONS["professional_depth"],
            expected_professional_depth,
        )
        schema_path = (
            Path(__file__).resolve().parents[1]
            / "schemas"
            / "review_judgment.schema.json"
        )
        schema = json.loads(schema_path.read_text())
        self.assertEqual(
            tuple(schema["$defs"]["professionalDepth"]["required"]),
            expected_professional_depth,
        )

    @staticmethod
    def assessment(status="full"):
        return {"status": status, "candidate_span": "x", "rationale": "r"}

    def judgment(
        self,
        component_statuses=("full", "full", "full"),
        operation_status="full",
        calibration="consistent",
        violation=False,
    ):
        a = self.assessment
        return {
            "task_id": "RT01",
            "component_fulfillment": [
                {
                    "component_id": f"RT01-C{index}",
                    "status": status,
                    "candidate_span": "x",
                    "rationale": "r",
                }
                for index, status in enumerate(component_statuses, start=1)
            ],
            "critical_synthesis": {
                operation: a(operation_status)
                for operation in MODULE.ATOMIC_OPERATIONS["critical_synthesis"]
            },
            "professional_depth": {
                operation: a(operation_status)
                for operation in MODULE.ATOMIC_OPERATIONS["professional_depth"]
            },
            "current_research_outlook": {
                operation: a(operation_status)
                for operation in MODULE.ATOMIC_OPERATIONS[
                    "current_research_outlook"
                ]
            },
            "claim_calibration": {
                "status": calibration,
                "candidate_span": "",
                "rationale": "r",
            },
            "constraint_assessments": [
                {
                    "constraint_id": "RT01-B1",
                    "status": (
                        "material_violation" if violation else "compliant"
                    ),
                    "candidate_span": "x",
                    "rationale": "r",
                },
                {
                    "constraint_id": "RT01-B2",
                    "status": "compliant",
                    "candidate_span": "",
                    "rationale": "r",
                },
            ],
            "potential_external_scientific_error": False,
            "potential_external_error_rationale": "",
        }

    def test_full_atomic_judgment_scores_one(self):
        scored = MODULE.score_judgment(self.judgment())
        self.assertEqual(scored["critical_synthesis"], 1.0)
        self.assertEqual(scored["professional_depth"], 1.0)
        self.assertEqual(scored["current_research_outlook"], 1.0)
        self.assertEqual(
            scored["atomic_component_capped_review_quality"], 1.0
        )

    def test_dimension_weighting_is_local_and_normalized(self):
        judgment = self.judgment(operation_status="absent")
        for operation in MODULE.ATOMIC_OPERATIONS["critical_synthesis"]:
            judgment["critical_synthesis"][operation] = self.assessment("full")
        for operation in MODULE.ATOMIC_OPERATIONS["professional_depth"]:
            judgment["professional_depth"][operation] = self.assessment("partial")
        scored = MODULE.score_judgment(judgment)
        self.assertAlmostEqual(scored["critical_synthesis"], 1.0)
        self.assertAlmostEqual(scored["professional_depth"], 0.5)
        self.assertAlmostEqual(scored["current_research_outlook"], 0.0)
        self.assertAlmostEqual(
            scored["uncapped_weighted_review_quality"], 0.575
        )

    def test_component_coverage_caps_quality(self):
        scored = MODULE.score_judgment(
            self.judgment(component_statuses=("full", "full", "partial"))
        )
        self.assertAlmostEqual(scored["mean_component_fulfillment"], 5 / 6)
        self.assertAlmostEqual(
            scored["atomic_component_capped_review_quality"], 5 / 6
        )

    def test_material_calibration_caps_task_score(self):
        scored = MODULE.score_judgment(
            self.judgment(calibration="material_inconsistency")
        )
        self.assertEqual(scored["active_score_cap"], 0.5)
        self.assertEqual(
            scored["atomic_component_capped_review_quality"], 0.5
        )

    def test_material_boundary_violation_caps_task_score(self):
        scored = MODULE.score_judgment(self.judgment(violation=True))
        self.assertEqual(scored["material_boundary_violation_count"], 1)
        self.assertEqual(
            scored["atomic_component_capped_review_quality"], 0.5
        )

    def test_rejects_missing_component(self):
        judgment = self.judgment()
        judgment["component_fulfillment"].pop()
        with self.assertRaisesRegex(ValueError, "exactly 3"):
            MODULE.score_judgment(judgment)

    def test_rejects_duplicate_constraint(self):
        judgment = self.judgment()
        judgment["constraint_assessments"][1]["constraint_id"] = "RT01-B1"
        with self.assertRaisesRegex(ValueError, "each expected constraint"):
            MODULE.score_judgment(judgment)


if __name__ == "__main__":
    unittest.main()

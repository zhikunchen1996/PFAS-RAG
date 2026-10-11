import importlib.util
import unittest
from pathlib import Path

import numpy as np


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/run_analysis.py"
SPEC = importlib.util.spec_from_file_location("ablation_analysis", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class AnalysisRulesTest(unittest.TestCase):
    def test_citation_positions_are_zero_based_and_unique(self):
        self.assertEqual(MODULE.cited_context_positions("A [C1] B [C3] C [C1]"), {0, 2})

    def test_majority_requires_two_of_three(self):
        self.assertTrue(MODULE.majority([True, False, True]))
        self.assertFalse(MODULE.majority([True, False, False]))

    def test_build_cases_has_expected_cardinality(self):
        cases = MODULE.build_cases()
        self.assertEqual(len(cases), 120)
        self.assertEqual(cases[["system", "question_id"]].duplicated().sum(), 0)
        self.assertEqual(cases.groupby("system").size().to_dict(), {"bge": 40, "bge_llm": 40, "hybrid": 40})

    def test_failure_paths_are_exhaustive(self):
        cases = MODULE.build_cases()
        self.assertFalse(cases.failure_path.isna().any())
        self.assertEqual(int((cases.required_gold_count == 0).sum()), int((cases.failure_path == "not_applicable_no_required_gold").sum()))

    def test_unique_chunk_hits_do_not_exceed_gold_record_hits(self):
        cases = MODULE.build_cases()
        self.assertTrue((cases.unique_required_gold_chunks_in_context <= cases["required_gold_retrieved@10"]).all())

    def test_retrieval_completeness_groups_cover_boundaries(self):
        self.assertEqual(MODULE.retrieval_completeness_group(0.0), "No gold retrieved")
        self.assertEqual(MODULE.retrieval_completeness_group(0.5), "Partially retrieved")
        self.assertEqual(MODULE.retrieval_completeness_group(1.0), "Fully retrieved")

    def test_question_cluster_bootstrap_is_reproducible(self):
        cases = MODULE.build_cases()
        applicable = cases[cases.required_gold_count > 0].copy()
        applicable["retrieval_completeness_group"] = applicable[
            "required_gold_recall@10"
        ].map(MODULE.retrieval_completeness_group)
        rho_a, groups_a = MODULE.question_cluster_bootstrap(
            applicable, replicates=20, seed=123
        )
        rho_b, groups_b = MODULE.question_cluster_bootstrap(
            applicable, replicates=20, seed=123
        )
        np.testing.assert_allclose(rho_a, rho_b)
        for group in MODULE.COUPLING_GROUPS:
            np.testing.assert_allclose(groups_a[group], groups_b[group])


if __name__ == "__main__":
    unittest.main()

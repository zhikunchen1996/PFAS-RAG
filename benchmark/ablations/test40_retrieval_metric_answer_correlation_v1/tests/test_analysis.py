import importlib.util
import unittest
from pathlib import Path

import numpy as np


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/run_analysis.py"
SPEC = importlib.util.spec_from_file_location("retrieval_metric_analysis", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class RetrievalMetricAnalysisTest(unittest.TestCase):
    def test_applicable_case_cardinality(self):
        cases = MODULE.load_applicable_cases()
        self.assertEqual(len(cases), 114)
        self.assertEqual(cases.question_id.nunique(), 38)
        self.assertTrue((cases.groupby("question_id").system.nunique() == 3).all())

    def test_cluster_bootstrap_is_reproducible(self):
        cases = MODULE.load_applicable_cases()
        first = MODULE.question_cluster_bootstrap(
            cases, MODULE.METRICS, replicates=25, seed=123
        )
        second = MODULE.question_cluster_bootstrap(
            cases, MODULE.METRICS, replicates=25, seed=123
        )
        np.testing.assert_allclose(first, second)

    def test_full_retrieval_subset(self):
        cases = MODULE.load_applicable_cases()
        subset = cases[np.isclose(cases["required_gold_recall@10"], 1.0)]
        self.assertEqual(len(subset), 32)
        self.assertEqual(subset.question_id.nunique(), 14)

    def test_required_gold_recall_correlation_exceeds_mrr_descriptively(self):
        cases = MODULE.load_applicable_cases()
        mrr = MODULE.safe_spearman(
            cases.MRR_required_gold.to_numpy(), cases.l3_mean.to_numpy()
        )
        recall = MODULE.safe_spearman(
            cases["required_gold_recall@10"].to_numpy(), cases.l3_mean.to_numpy()
        )
        self.assertGreater(recall, mrr)

    def test_cluster_robust_significance_is_reproducible(self):
        cases = MODULE.load_applicable_cases()
        expected = {
            "MRR_required_gold": 0.11184044730899718,
            "required_gold_recall@10": 0.07452346806465107,
            "gold_doc_recall@10": 0.501580432723519,
        }
        for metric, p_value in expected.items():
            result = MODULE.cluster_robust_spearman_test(cases, metric)
            self.assertAlmostEqual(
                result["question_cluster_robust_two_sided_p_value"], p_value
            )

    def test_strict_matched_full_retrieval_subset(self):
        cases = MODULE.load_applicable_cases()
        recall = cases.pivot(
            index="question_id", columns="system", values="required_gold_recall@10"
        )
        matched = recall.index[np.isclose(recall, 1.0).all(axis=1)]
        self.assertEqual(len(matched), 7)


if __name__ == "__main__":
    unittest.main()

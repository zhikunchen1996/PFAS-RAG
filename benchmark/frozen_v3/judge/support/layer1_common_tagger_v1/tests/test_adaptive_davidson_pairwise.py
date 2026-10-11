from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


EXPERIMENT = Path(__file__).resolve().parents[1]
JUDGE = EXPERIMENT.parents[1]
ROOT = JUDGE.parent.parents[1]
SCRIPT = (
    EXPERIMENT / "scripts/run_dev13_adaptive_davidson_pairwise.py"
)
spec = importlib.util.spec_from_file_location("adaptive_davidson", SCRIPT)
runner = importlib.util.module_from_spec(spec)
assert spec and spec.loader
sys.modules[spec.name] = runner
spec.loader.exec_module(runner)


class AdaptiveDavidsonTests(unittest.TestCase):
    def test_davidson_recovers_order_and_ties(self) -> None:
        outcomes = []
        for qid in ("Q1", "Q2", "Q3", "Q4"):
            outcomes.extend(
                [
                    {
                        "question_id": qid,
                        "system_i": "hybrid",
                        "system_j": "bge",
                        "outcome": "bge",
                    },
                    {
                        "question_id": qid,
                        "system_i": "hybrid",
                        "system_j": "bge_llm",
                        "outcome": "bge_llm",
                    },
                    {
                        "question_id": qid,
                        "system_i": "bge",
                        "system_j": "bge_llm",
                        "outcome": "tie" if qid == "Q1" else "bge_llm",
                    },
                ]
            )
        fit = runner.fit_davidson(outcomes)
        score = fit["normalized_ability"]
        self.assertGreater(score["bge_llm"], score["bge"])
        self.assertGreater(score["bge"], score["hybrid"])
        self.assertGreater(fit["tie_parameter_nu"], 0)

    def test_disagreement_triggers_second_mirror(self) -> None:
        rows = [
            {
                "question_id": "Q1",
                "left_system": "hybrid",
                "right_system": "bge",
                "mapped_outcome": "hybrid",
            },
            {
                "question_id": "Q1",
                "left_system": "hybrid",
                "right_system": "bge",
                "mapped_outcome": "bge",
            },
        ]
        self.assertEqual(
            runner.discordant_units(rows),
            {("Q1", "hybrid", "bge")},
        )

    def test_final_tie_uses_all_mirrored_votes(self) -> None:
        rows = [
            {
                "question_id": "Q1",
                "left_system": "hybrid",
                "right_system": "bge",
                "mapped_outcome": outcome,
            }
            for outcome in ("hybrid", "bge", "tie", "tie")
        ]
        result = runner.finalize_units(rows)[0]
        self.assertEqual(result["outcome"], "tie")
        self.assertEqual(result["judgment_count"], 4)


if __name__ == "__main__":
    unittest.main()

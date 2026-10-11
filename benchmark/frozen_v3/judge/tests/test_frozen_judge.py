from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


PACKAGE = Path(__file__).resolve().parents[1]
SCRIPTS = PACKAGE / "scripts"
sys.path.insert(0, str(SCRIPTS))

import build_anonymization_audit  # noqa: E402
import fit_davidson_v2  # noqa: E402
import judge_common as common  # noqa: E402
import run_l15_claim_support  # noqa: E402
import run_l2_pairwise_v2  # noqa: E402
import summarize_l15_claim_support  # noqa: E402


class FrozenJudgeTests(unittest.TestCase):
    def test_citation_stripping_preserves_content(self) -> None:
        observed = common.strip_citations("Claim [C1] and detail [c10].")
        self.assertEqual(observed, "Claim and detail .")

    def test_l2_builds_exact_mirrored_pair_without_hidden_inputs(self) -> None:
        payloads = run_l2_pairwise_v2.build_payloads(
            questions=[
                {
                    "question_id": "Q1",
                    "question_text": "What is supported?",
                    "must_include": "scope",
                    "must_not_claim": "universality",
                }
            ],
            gold_rows=[
                {
                    "question_id": "Q1",
                    "evidence_id": "Q1_MMG001",
                    "evidence_type": "required",
                    "exact_evidence_span": "Known evidence.",
                    "supported_claim": "Bounded claim.",
                    "does_not_support": "Universal claim.",
                }
            ],
            left_rows=[{"question_id": "Q1", "answer": "Left [C1]"}],
            right_rows=[{"question_id": "Q1", "answer": "Right [C2]"}],
            left_label="left",
            right_label="right",
        )
        self.assertEqual(len(payloads), 2)
        first, second = payloads
        self.assertEqual(first["orientation_index"], 0)
        self.assertEqual(second["orientation_index"], 1)
        self.assertEqual(first["assignment"]["A"], second["assignment"]["B"])
        self.assertEqual(first["assignment"]["B"], second["assignment"]["A"])
        allowed = {
            "question",
            "task_boundaries",
            "non_exhaustive_gold_evidence",
            "answer_A",
            "answer_B",
        }
        for payload in payloads:
            self.assertEqual(set(payload["model_payload"]), allowed)
            serialized = json.dumps(payload["model_payload"]).lower()
            self.assertNotIn("retrieved_context", serialized)
            self.assertNotIn("question_id", serialized)
            self.assertNotIn("q1_mmg001", serialized)
            self.assertNotIn("[c1]", serialized)

    def test_visible_gold_removes_ids_and_decoys(self) -> None:
        visible = common.visible_gold(
            [
                {
                    "evidence_id": "Q1_MMG001",
                    "evidence_type": "required_gold",
                    "exact_evidence_span": "Evidence.",
                    "supported_claim": "Claim.",
                    "does_not_support": "",
                },
                {
                    "evidence_id": "Q1_DECOY",
                    "evidence_type": "decoy",
                    "exact_evidence_span": "Decoy.",
                },
            ]
        )
        self.assertEqual(len(visible), 1)
        self.assertNotIn("evidence_id", visible[0])

    def test_l2_production_identity_leakage_gate(self) -> None:
        with self.assertRaisesRegex(ValueError, "identity-leakage scan"):
            run_l2_pairwise_v2.build_payloads(
                questions=[
                    {
                        "question_id": "Q1",
                        "question_text": "Question?",
                    }
                ],
                gold_rows=[
                    {
                        "question_id": "Q1",
                        "evidence_type": "required_gold",
                        "exact_evidence_span": "Evidence.",
                    }
                ],
                left_rows=[
                    {
                        "question_id": "Q1",
                        "answer": "The BGE-LLM system returned this.",
                    }
                ],
                right_rows=[{"question_id": "Q1", "answer": "Answer."}],
                left_label="left",
                right_label="right",
            )

    def test_l2_resume_rejects_duplicate_payload_ids(self) -> None:
        valid_result = {
            "criterion_preferences": {
                criterion: "tie" for criterion in common.CRITERIA
            },
            "criterion_rationales": {
                criterion: "No material difference."
                for criterion in common.CRITERIA
            },
        }
        payload = {
            "payload_id": "duplicate",
            "question_id": "Q1",
            "model_payload": {},
            "judge_result": valid_result,
        }
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "judge_results.jsonl"
            common.write_jsonl(output, [payload, payload])
            with self.assertRaisesRegex(RuntimeError, "duplicate payload_id"):
                run_l2_pairwise_v2.run_payloads(
                    [payload],
                    prompt="unused",
                    output=output,
                    workers=1,
                    resume=True,
                )

    def test_l2_schema_misspelling_is_rejected(self) -> None:
        malformed = {
            "criterion_preferences": {
                criterion: "tie" for criterion in common.CRITERIA
            },
            "criterion_rationalles": {
                criterion: "No material difference."
                for criterion in common.CRITERIA
            },
        }
        with self.assertRaisesRegex(ValueError, "Missing"):
            common.validate_judge_result(malformed)

    def test_l15_supplies_all_complete_chunks(self) -> None:
        answer = {
            "question_id": "Q1",
            "answer": "Claim [C2].",
            "retrieved_context": [
                {"rank": 1, "text": "First complete chunk."},
                {"rank": 2, "text": "Second complete chunk."},
            ],
        }
        context = run_l15_claim_support.complete_context(answer)
        self.assertEqual(
            context,
            [
                {"citation_id": "C1", "text": "First complete chunk."},
                {"citation_id": "C2", "text": "Second complete chunk."},
            ],
        )

    def test_question_membership_must_match_exactly(self) -> None:
        questions = [
            {"question_id": "Q1"},
            {"question_id": "Q2"},
        ]
        with self.assertRaisesRegex(ValueError, "missing=.*Q2"):
            common.ordered_for_questions(
                [{"question_id": "Q1"}],
                questions,
                source_name="test",
            )
        with self.assertRaisesRegex(ValueError, "extra=.*Q3"):
            common.ordered_for_questions(
                [
                    {"question_id": "Q1"},
                    {"question_id": "Q2"},
                    {"question_id": "Q3"},
                ],
                questions,
                source_name="test",
            )

    def test_l15_zero_cited_claims_is_nonapplicable_not_failure(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            results = root / "results.jsonl"
            common.write_jsonl(
                results,
                [
                    {
                        "question_id": "Q1",
                        "judge_result": {
                            "cited_claims": [],
                            "uncited_source_dependent_claims": [],
                        },
                    }
                ],
            )
            out = root / "out"
            with patch.object(
                sys,
                "argv",
                [
                    "summarize_l15_claim_support.py",
                    "--results",
                    str(results),
                    "--out",
                    str(out),
                ],
            ):
                summarize_l15_claim_support.main()
            summary = common.read_csv(out / "summary.csv")[0]
            self.assertEqual(summary["applicable_question_count"], "0")
            self.assertEqual(
                summary["claim_supported_by_any_citation_rate"],
                "",
            )

    def test_bootstrap_minimum_is_enforced(self) -> None:
        grouped = {
            criterion: [
                ("Q1", "a", "b", "a"),
                ("Q1", "a", "b", "tie"),
            ]
            for criterion in common.CRITERIA
        }
        with self.assertRaises(ValueError):
            fit_davidson_v2.bootstrap_joint(grouped, samples=9_999)

    def test_tie_parameter_is_fitted_from_each_criterion(self) -> None:
        tie_heavy = [
            ("Q1", "a", "b", "tie"),
            ("Q2", "a", "b", "tie"),
            ("Q3", "a", "b", "tie"),
            ("Q4", "a", "b", "tie"),
            ("Q5", "a", "b", "a"),
            ("Q6", "a", "b", "b"),
        ]
        win_heavy = [
            ("Q1", "a", "b", "a"),
            ("Q2", "a", "b", "b"),
            ("Q3", "a", "b", "a"),
            ("Q4", "a", "b", "b"),
            ("Q5", "a", "b", "a"),
            ("Q6", "a", "b", "tie"),
        ]
        first = fit_davidson_v2.fit(tie_heavy)
        second = fit_davidson_v2.fit(win_heavy)
        self.assertGreater(
            first["tie_parameter"],
            second["tie_parameter"],
        )

    def test_disconnected_davidson_graph_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "disconnected"):
            fit_davidson_v2.fit(
                [
                    ("Q1", "a", "b", "a"),
                    ("Q2", "c", "d", "c"),
                ]
            )

    def test_anonymization_patterns_do_not_flag_domain_hybrid(self) -> None:
        domain_text = "Hybrid membrane treatment may combine two processes."
        matches = {
            name
            for name, pattern in (
                build_anonymization_audit.PROHIBITED_PATTERNS.items()
            )
            if pattern.search(domain_text)
        }
        self.assertNotIn("explicit_hybrid_system_label", matches)
        self.assertTrue(
            build_anonymization_audit.PROHIBITED_PATTERNS[
                "explicit_hybrid_system_label"
            ].search("Hybrid retrieval system")
        )

    def test_frozen_audit_has_no_detected_identity_leakage(self) -> None:
        summary = json.loads(
            (
                PACKAGE
                / "audits/anonymization/scored/summary.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(
            summary["status"],
            "passed_no_evidence_of_above_chance_identity_inference",
        )
        self.assertGreaterEqual(
            summary["assignment_exact_null_tail_p"],
            0.05,
        )
        self.assertGreaterEqual(
            summary["complete_mapping_exact_binomial_tail_p"],
            0.05,
        )


if __name__ == "__main__":
    unittest.main()

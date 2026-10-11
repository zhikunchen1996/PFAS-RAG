from __future__ import annotations

import json
import inspect
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock


PROJECT_ROOT = Path(__file__).resolve().parents[3]
SCRIPTS = PROJECT_ROOT / "benchmark/frozen_v3/scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import run_dev13_budget_bge_llm_gpt51 as budget  # noqa: E402
import run_dev13_neutral_evidence_judge_v3 as judge  # noqa: E402
import run_dev13_soft_tags_v3 as generation  # noqa: E402
import runtime_helpers  # noqa: E402
import validate_self_contained_v3 as package_validator  # noqa: E402
import build_freeze_manifest as freeze_manifest  # noqa: E402


class TemplateTests(unittest.TestCase):
    def test_render_is_single_pass_and_strict(self) -> None:
        rendered = runtime_helpers.render(
            "Question: {question}",
            question="Keep {untrusted_placeholder} literal.",
        )
        self.assertEqual(
            rendered,
            "Question: Keep {untrusted_placeholder} literal.",
        )
        with self.assertRaisesRegex(KeyError, "Missing template values"):
            runtime_helpers.render("{question} {context}", question="Q")
        with self.assertRaisesRegex(KeyError, "Unused template values"):
            runtime_helpers.render("{question}", question="Q", context="C")


class ResumeTests(unittest.TestCase):
    def test_fresh_run_does_not_reuse_and_resume_is_validated(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "rows.jsonl"
            runtime_helpers.write_jsonl(
                output,
                [{"item_id": "A", "version": 1, "value": "stale"}],
            )
            calls: list[int] = []

            def key(row: dict) -> str:
                return row["item_id"]

            def worker(item: dict) -> dict:
                calls.append(item["version"])
                return {**item, "value": f"fresh-{item['version']}"}

            rows = runtime_helpers.run_parallel(
                items=[{"item_id": "A", "version": 1}],
                key=key,
                worker=worker,
                output_path=output,
                workers=1,
                label="fresh-test",
            )
            self.assertEqual(calls, [1])
            self.assertEqual(rows[0]["value"], "fresh-1")

            calls.clear()
            rows = runtime_helpers.run_parallel(
                items=[{"item_id": "A", "version": 1}],
                key=key,
                worker=worker,
                output_path=output,
                workers=1,
                label="resume-test",
                resume=True,
                reuse_validator=lambda item, row: (
                    item["version"] == row["version"]
                ),
            )
            self.assertEqual(calls, [])
            self.assertEqual(rows[0]["value"], "fresh-1")

            calls.clear()
            rows = runtime_helpers.run_parallel(
                items=[{"item_id": "A", "version": 2}],
                key=key,
                worker=worker,
                output_path=output,
                workers=1,
                label="resume-mismatch-test",
                resume=True,
                reuse_validator=lambda item, row: (
                    item["version"] == row["version"]
                ),
            )
            self.assertEqual(calls, [2])
            self.assertEqual(rows[0]["value"], "fresh-2")

    def test_judge_envelope_is_not_sent_to_model(self) -> None:
        sent: list[dict] = []
        response = SimpleNamespace(
            id="judge-response",
            model="judge-model",
            system_fingerprint="fingerprint",
            usage=SimpleNamespace(
                prompt_tokens=1,
                completion_tokens=1,
                total_tokens=2,
            ),
            choices=[
                SimpleNamespace(
                    message=SimpleNamespace(content='{"ok":true}')
                )
            ],
        )

        def create(**kwargs):
            sent.append(json.loads(kwargs["messages"][1]["content"]))
            return response

        fake_client = SimpleNamespace(
            chat=SimpleNamespace(
                completions=SimpleNamespace(create=create),
            )
        )
        item = {
            "payload_id": "tagged_vs_matched_direct::Q1::R1::O1",
            "question_id": "Q1",
            "model_payload": {
                "question": "Visible question?",
                "answer_A": "A",
                "answer_B": "B",
            },
        }
        with tempfile.TemporaryDirectory() as directory:
            with mock.patch.object(
                runtime_helpers,
                "client",
                lambda: fake_client,
            ):
                rows = runtime_helpers.call_json_judge(
                    [item],
                    "Judge prompt",
                    "judge-model",
                    Path(directory) / "judge.jsonl",
                    workers=1,
                    label="judge-envelope-test",
                )
        self.assertEqual(sent, [item["model_payload"]])
        self.assertEqual(rows[0]["payload_id"], item["payload_id"])


class TagInterfaceTests(unittest.TestCase):
    def test_tagger_request_and_validation_execute_together(self) -> None:
        response = SimpleNamespace(
            id="response-1",
            model="gpt-5.1-test",
            system_fingerprint="fingerprint",
            usage=SimpleNamespace(
                prompt_tokens=10,
                completion_tokens=5,
                total_tokens=15,
            ),
            choices=[
                SimpleNamespace(
                    message=SimpleNamespace(
                        content=(
                            '{"question_components":[{"component_id":"R1",'
                            '"description":"Visible information need."}],'
                            '"chunk_tags":[{"candidate_id":1,'
                            '"eligibility":"direct_evidence",'
                            '"detail_policy":"use_full_claim",'
                            '"supports_components":["R1"],'
                            '"evidence_polarity":"support",'
                            '"exact_support":"Supported sentence.",'
                            '"confidence":1.0}]}'
                        )
                    )
                )
            ],
        )
        fake_client = SimpleNamespace(
            chat=SimpleNamespace(
                completions=SimpleNamespace(
                    create=lambda **_: response,
                )
            )
        )
        questions = [{"question_id": "Q1", "question_text": "Question?"}]
        retrieval = [
            {
                "question_id": "Q1",
                "retrieved_context": [
                    {
                        "doc_id": "D1",
                        "chunk_id": "1",
                        "citation": "Source",
                        "section": "Results",
                        "text": "Supported sentence.",
                    }
                ],
            }
        ]
        with tempfile.TemporaryDirectory() as directory:
            with (
                mock.patch.object(generation, "OUT", Path(directory)),
                mock.patch.object(generation.base, "client", lambda: fake_client),
            ):
                rows = generation.run_tagger(
                    questions,
                    retrieval,
                    workers=1,
                    resume=False,
                )
        self.assertEqual(len(rows), 1)
        self.assertEqual(
            rows[0]["validated_chunk_tags"][0]["exact_support"],
            "Supported sentence.",
        )
        self.assertTrue(rows[0]["tag_execution_sha256"])

    def test_unverified_free_text_and_excerpt_do_not_reach_answer(self) -> None:
        candidates = [{"text": "Only source-grounded text is allowed."}]
        tags, errors = generation.validate_tags(
            {
                "chunk_tags": [
                    {
                        "candidate_id": 1,
                        "eligibility": "direct_evidence",
                        "detail_policy": "use_full_claim",
                        "supports_components": ["R1"],
                        "evidence_polarity": "support",
                        "exact_support": "Fabricated answer hint.",
                        "allowed_use": "Leak this conclusion.",
                        "avoid_use": "Hide this conflict.",
                        "omit_details": ["Hide this condition."],
                        "confidence": 1.0,
                    }
                ]
            },
            candidates,
            {"R1"},
        )
        self.assertTrue(
            any("removed non-verbatim exact_support" in error for error in errors)
        )
        context = generation.format_tagged_context(
            candidates,
            {"validated_chunk_tags": tags},
        )
        self.assertNotIn("Fabricated answer hint", context)
        self.assertNotIn("Leak this conclusion", context)
        self.assertNotIn("Hide this conflict", context)
        self.assertNotIn("Hide this condition", context)
        self.assertEqual(
            set(tags[0]),
            {
                "candidate_id",
                "confidence",
                "detail_policy",
                "eligibility",
                "evidence_polarity",
                "exact_support",
                "exact_support_validated",
                "supports_components",
            },
        )

    def test_invalid_confidence_is_logged(self) -> None:
        tags, errors = generation.validate_tags(
            {
                "chunk_tags": [
                    {
                        "candidate_id": 1,
                        "eligibility": "direct_evidence",
                        "detail_policy": "use_full_claim",
                        "supports_components": ["R1"],
                        "evidence_polarity": "support",
                        "exact_support": "Supported.",
                        "confidence": "not-a-number",
                    }
                ]
            },
            [{"text": "Supported."}],
            {"R1"},
        )
        self.assertEqual(tags[0]["confidence"], 0.0)
        self.assertTrue(
            any("invalid confidence" in error for error in errors)
        )


class JudgeContractTests(unittest.TestCase):
    def test_duplicate_answer_sections_are_rejected(self) -> None:
        answer = (
            "Answerability\nanswerable\n\n"
            "Answer\nFirst\n\n"
            "Answer\nSecond\n\n"
            "Uncertainty and limitations\nNone\n\n"
            "Practical takeaway\nUse care"
        )
        with self.assertRaisesRegex(RuntimeError, "Duplicate answer section"):
            judge.normalized_answer_without_citations(answer)

    def test_citations_and_local_metadata_are_absent_from_model_payload(self) -> None:
        questions = runtime_helpers.read_csv(judge.QUESTIONS)
        gold = runtime_helpers.group_gold(
            runtime_helpers.read_jsonl(judge.GOLD)
        )
        tagged = runtime_helpers.read_jsonl(judge.TAGGED)
        direct = runtime_helpers.read_jsonl(judge.DIRECT)
        common = judge.load_common_verification(
            [row["question_id"] for row in questions]
        )
        payloads, mappings, _ = judge.build_payloads(
            questions,
            gold,
            common,
            tagged,
            None,
            direct,
            repeat=1,
        )
        self.assertEqual(len(payloads), 26)
        self.assertEqual(len(mappings), 26)
        for envelope in payloads:
            serialized = json.dumps(
                envelope["model_payload"],
                ensure_ascii=False,
            )
            self.assertNotIn(envelope["payload_id"], serialized)
            self.assertNotIn(envelope["question_id"], serialized)
            self.assertNotIn("tagged_vs_", serialized)
            self.assertNotIn('"task_type"', serialized)
            self.assertNotIn('"answerability_type"', serialized)
            self.assertIsNone(judge.CITATION_PATTERN.search(serialized))

    def test_judge_result_schema_and_orientation_mapping(self) -> None:
        mapping = {
            "payload_id": "P1",
            "comparison": "tagged_vs_matched_direct",
            "question_id": "Q1",
            "repeat": 1,
            "orientation": 1,
            "left_system": "tagged",
            "right_system": "direct",
            "system_A": "direct",
            "system_B": "tagged",
        }
        result = {
            "criterion_preferences": {
                criterion: "B" for criterion in judge.CRITERIA
            },
            "criterion_rationales": {
                criterion: "Materially better."
                for criterion in judge.CRITERIA
            },
            "material_errors_A": ["one error"],
            "material_errors_B": [],
            "confidence": "high",
        }
        parsed = judge.parse_judge_result(mapping, result)
        for criterion in judge.CRITERIA:
            self.assertEqual(parsed[f"{criterion}_tagged_point"], 1.0)
        self.assertEqual(parsed["confidence"], "high")

        invalid = {**result, "confidence": "certain"}
        repaired = judge.parse_judge_result(mapping, invalid)
        self.assertEqual(repaired["confidence"], "unspecified")
        self.assertEqual(repaired["schema_repair_count"], 1)

        missing_scored_field = {
            **result,
            "criterion_preferences": {
                criterion: "B"
                for criterion in judge.CRITERIA
                if criterion != "scientific_correctness"
            },
        }
        with self.assertRaisesRegex(
            RuntimeError,
            "Missing scientific_correctness",
        ):
            judge.parse_judge_result(mapping, missing_scored_field)

    def test_pairwise_aggregation_uses_declared_weights(self) -> None:
        rows = []
        for orientation in (1, 2):
            row = {
                "comparison": "tagged_vs_matched_direct",
                "question_id": "Q1",
                "repeat": 1,
                "orientation": orientation,
                "left_system": "tagged",
                "right_system": "direct",
            }
            for criterion in judge.CRITERIA:
                row[f"{criterion}_tagged_point"] = 1.0
            rows.append(row)
        with tempfile.TemporaryDirectory() as directory:
            with mock.patch.object(judge, "OUT", Path(directory)):
                per_question, summary = judge.aggregate(rows, repeats=1)
        self.assertEqual(per_question[0]["winner"], "tagged")
        self.assertEqual(per_question[0]["weighted_tagged_score"], 1.0)
        self.assertEqual(summary[0]["tagged_wins"], 1)
        self.assertEqual(summary[0]["mirrored_criterion_agreement"], 1.0)


class RetrievalContractTests(unittest.TestCase):
    def test_selector_parser_requires_schema_and_strict_ids(self) -> None:
        self.assertEqual(
            budget.parse_selector_json('{"selected_ids":[1,"2"]}')[
                "selected_ids"
            ],
            [1, "2"],
        )
        with self.assertRaisesRegex(ValueError, "selected_ids"):
            budget.parse_selector_json('{"scores":{"1":9}}')
        self.assertEqual(budget.id_to_int("2"), 2)
        self.assertIsNone(budget.id_to_int("ID 2"))
        self.assertIsNone(budget.id_to_int(True))
        with self.assertRaises(SystemExit):
            budget.build_parser().parse_args(
                ["--selector-input", "rubric_augmented"]
            )

    def test_current_data_and_retrieval_metrics_reproduce(self) -> None:
        package_validator.validate_data_integrity()
        package_validator.validate_fixed_retrieval_input()
        package_validator.validate_budget_metrics()


class FreezeManifestTests(unittest.TestCase):
    def test_git_cleanliness_checks_invoke_git(self) -> None:
        source = inspect.getsource(freeze_manifest.build_manifest)
        self.assertIn('subprocess.run(("git", *args)', source)


if __name__ == "__main__":
    unittest.main()

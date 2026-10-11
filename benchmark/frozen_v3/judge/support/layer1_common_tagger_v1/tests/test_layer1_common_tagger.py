from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock


EXPERIMENT = Path(__file__).resolve().parents[1]
JUDGE = EXPERIMENT.parents[1]
ROOT = JUDGE.parent.parents[1]
SCRIPT = (
    EXPERIMENT / "scripts/run_dev13_common_tagger.py"
)
spec = importlib.util.spec_from_file_location("layer1_runner", SCRIPT)
runner = importlib.util.module_from_spec(spec)
assert spec and spec.loader
sys.modules[spec.name] = runner
spec.loader.exec_module(runner)


class Layer1ContractTests(unittest.TestCase):
    def test_frozen_v3_and_all_retrieval_inputs_validate(self) -> None:
        runner.verify_frozen_v3()
        questions = runner.base.read_csv(runner.QUESTIONS)
        for system, config in runner.SYSTEMS.items():
            rows = runner.validate_retrieval(
                system,
                config["retrieval"],
            )
            runner.validate_information_boundary(questions, rows)

    def test_tagger_payload_has_no_system_gold_or_scores(self) -> None:
        questions = runner.base.read_csv(runner.QUESTIONS)
        rows = runner.validate_retrieval(
            "hybrid",
            runner.SYSTEMS["hybrid"]["retrieval"],
        )
        payload = runner.tagger_model_payload(questions[0], rows[0])
        self.assertEqual(set(payload), {"question", "candidates"})
        self.assertEqual(
            set(payload["candidates"][0]),
            {"candidate_id", "source", "section", "text"},
        )

    def test_validate_only_does_not_create_output(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory) / "unused"
            with mock.patch.object(
                sys,
                "argv",
                [
                    str(SCRIPT),
                    "--out",
                    str(out),
                    "--validate-only",
                ],
            ):
                runner.main()
            self.assertFalse(out.exists())

    def test_system_metadata_is_added_after_model_payload(self) -> None:
        row = {
            "question_id": "Q1",
            "validated_chunk_tags": [],
        }
        annotated = runner.annotate_rows(
            [row],
            system="hybrid",
            config_name="hybrid_top10_pool60_win0",
            pipeline_id="layer1_common_soft_tagger_v1",
        )[0]
        self.assertEqual(annotated["retrieval_system"], "hybrid")
        self.assertNotIn("retrieval_system", row)

    def test_call_order_is_question_major_and_rotated(self) -> None:
        questions = runner.base.read_csv(runner.QUESTIONS)[:3]
        systems = ["hybrid", "bge", "bge_llm"]
        retrieval = {
            system: runner.validate_retrieval(
                system,
                runner.SYSTEMS[system]["retrieval"],
            )[:3]
            for system in systems
        }
        items = runner.ordered_items(questions, retrieval, systems)
        orders = [
            [
                item["system"]
                for item in items[index * 3:(index + 1) * 3]
            ]
            for index in range(3)
        ]
        self.assertEqual(
            orders,
            [
                ["hybrid", "bge", "bge_llm"],
                ["bge", "bge_llm", "hybrid"],
                ["bge_llm", "hybrid", "bge"],
            ],
        )

    def test_selector_cost_is_loaded_from_frozen_ledger(self) -> None:
        usage = runner.selector_usage("bge_llm")
        self.assertEqual(usage["prompt_tokens_total"], 158572)
        self.assertEqual(usage["completion_tokens_total"], 6750)
        self.assertEqual(usage["total_tokens"], 165322)
        self.assertAlmostEqual(usage["estimated_usd"], 0.265715)
        self.assertGreater(usage["latency_seconds_sum"], 0)

    def test_mocked_common_tagger_to_answer_pipeline(self) -> None:
        requests: list[dict] = []

        class Completions:
            def create(self, **request):
                requests.append(request)
                if "response_format" in request:
                    content = json.dumps(
                        {
                            "question_components": [
                                {
                                    "component_id": "R1",
                                    "description": "Visible question",
                                }
                            ],
                            "chunk_tags": [
                                {
                                    "candidate_id": index,
                                    "eligibility": "background",
                                    "detail_policy": "do_not_use",
                                    "supports_components": [],
                                    "evidence_polarity": "none",
                                    "exact_support": "",
                                    "confidence": 0.5,
                                }
                                for index in range(1, 11)
                            ],
                        }
                    )
                    prefix = "tag"
                else:
                    content = (
                        "1. Answerability\npartially_answerable.\n\n"
                        "2. Answer\nA bounded answer.\n\n"
                        "3. Uncertainty and limitations\nLimited context.\n\n"
                        "4. Practical takeaway\nMore evidence is needed."
                    )
                    prefix = "answer"
                return SimpleNamespace(
                    id=f"{prefix}-response",
                    model="gpt-5.1-test",
                    system_fingerprint="test",
                    usage=SimpleNamespace(
                        prompt_tokens=10,
                        completion_tokens=5,
                        total_tokens=15,
                    ),
                    choices=[
                        SimpleNamespace(
                            message=SimpleNamespace(content=content)
                        )
                    ],
                )

        fake_client = SimpleNamespace(
            chat=SimpleNamespace(completions=Completions())
        )
        questions = runner.base.read_csv(runner.QUESTIONS)[:1]
        systems = ["hybrid", "bge", "bge_llm"]
        retrieval = {
            system: runner.validate_retrieval(
                system,
                runner.SYSTEMS[system]["retrieval"],
            )[:1]
            for system in systems
        }
        items = runner.ordered_items(questions, retrieval, systems)
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory)
            with mock.patch.object(
                runner.base,
                "client",
                return_value=fake_client,
            ):
                tags, tagger_wall = runner.run_common_tagger(
                    items,
                    out,
                    workers=1,
                    resume=False,
                )
                answers, answer_wall = runner.run_common_answers(
                    items,
                    tags,
                    out,
                    workers=1,
                    resume=False,
                )
            summaries, costs = runner.write_system_outputs(
                out,
                systems,
                tags,
                answers,
            )
            runner.write_manifest(
                out,
                runner.verify_frozen_v3(),
                systems,
                summaries,
                resume=False,
                stage_wall_clock={
                    "common_soft_tagger": tagger_wall,
                    "common_answer_generation": answer_wall,
                    "current_run_total": tagger_wall + answer_wall,
                },
            )
            self.assertEqual(len(tags), 3)
            self.assertEqual(len(answers), 3)
            self.assertEqual(len(summaries), 3)
            self.assertEqual(len(costs), 14)
            self.assertGreaterEqual(tagger_wall, 0)
            self.assertGreaterEqual(answer_wall, 0)
            self.assertTrue(
                (out / "tokens/all_stage_costs.csv").is_file()
            )
            manifest = json.loads(
                (out / "experiment_manifest.json").read_text()
            )
            self.assertIn(
                "stage_wall_clock_seconds",
                manifest,
            )
            for row in tags:
                self.assertIn("tag_latency_seconds", row)
            for row in answers:
                self.assertIn("answer_latency_seconds", row)
        tag_requests = [
            request for request in requests
            if "response_format" in request
        ]
        self.assertEqual(len(tag_requests), 3)
        for request in tag_requests:
            payload = json.loads(request["messages"][1]["content"])
            self.assertEqual(set(payload), {"question", "candidates"})
            self.assertEqual(
                set(payload["candidates"][0]),
                {"candidate_id", "source", "section", "text"},
            )


if __name__ == "__main__":
    unittest.main()

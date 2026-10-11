from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
SCRIPTS = PACKAGE / "scripts"
ROOT = PACKAGE.parents[2]
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import common  # noqa: E402
import l3_scoring  # noqa: E402
import run_generation  # noqa: E402
import run_l3_repeats  # noqa: E402


class TestMultibaseProtocol(unittest.TestCase):
    def test_prompt_copies_match_frozen_dev_and_l3_sources(self) -> None:
        dev = ROOT / "benchmark/runs/stage4_multibase_dev13_v1/prompts"
        formal = ROOT / "benchmark/runs/test40_formal_v1_1/prompts"
        for name in (
            "shared_system_v1.txt",
            "direct_user_v1.txt",
            "rag_user_v1.txt",
        ):
            self.assertEqual(
                common.sha256(PACKAGE / "prompts" / name),
                common.sha256(dev / name),
            )
        self.assertEqual(
            common.sha256(common.L3_PROMPT),
            common.sha256(
                formal / "l3_gold_referenced_judge_v2.txt"
            ),
        )

    def test_frozen_inputs_match_their_sources(self) -> None:
        source = ROOT / "benchmark/runs/test40_formal_v1_1"
        pairs = {
            common.QUESTIONS: (
                ROOT / "benchmark/frozen_v3/input/questions_test40.csv"
            ),
            common.RETRIEVAL: (
                source
                / "results/selector/retrieval_outputs/"
                "rag_outputs_bge_llm_gpt51_pool60_bge30_llm10_fullchunk.jsonl"
            ),
            common.TAGS: (
                source
                / "results/generation/bge_llm/tags/tag_results.jsonl"
            ),
            common.REFERENCE_LEDGER: (
                source
                / "frozen/reference_claim_ledgers_test40_scoring_v2.jsonl"
            ),
        }
        for copied, original in pairs.items():
            self.assertEqual(common.sha256(copied), common.sha256(original))

    def test_inputs_cover_exactly_40_questions(self) -> None:
        items = run_generation.load_items()
        self.assertEqual(len(items), 40)
        self.assertEqual(
            [row["question_id"] for row in items],
            common.question_ids(),
        )

    def test_integer_zero_chunk_id_is_valid(self) -> None:
        common.validate_contexts(
            [
                {
                    "question_id": "Q",
                    "retrieved_context": [
                        {
                            "doc_id": "D1",
                            "chunk_id": 0,
                            "text": "Complete first chunk.",
                        },
                        *[
                            {
                                "doc_id": "D1",
                                "chunk_id": rank,
                                "text": f"Complete chunk {rank}.",
                            }
                            for rank in range(1, 10)
                        ],
                    ],
                }
            ]
        )

    def test_direct_payload_has_no_rag_information(self) -> None:
        item = run_generation.load_items()[0]
        for system in (
            "gpt51_direct",
            "gemini31_pro_direct",
            "claude_sonnet5_direct",
        ):
            serialized = json.dumps(
                run_generation.provider_request(item, system),
                ensure_ascii=False,
            )
            self.assertNotIn("Retrieved evidence:", serialized)
            self.assertNotIn(item["retrieval"]["retrieved_context"][0]["text"], serialized)
            self.assertIn("You have no retrieved literature", serialized)

    def test_rag_payload_contains_all_full_chunks_and_no_gold(self) -> None:
        item = run_generation.load_items()[0]
        request = run_generation.provider_request(item, "gpt51_rag")
        user_prompt = request["payload"]["messages"][1]["content"]
        for hit in item["retrieval"]["retrieved_context"]:
            self.assertIn(hit["text"], user_prompt)
        serialized = json.dumps(request, ensure_ascii=False)
        self.assertNotIn("must_include", serialized)
        self.assertNotIn("must_not_claim", serialized)
        self.assertNotIn("reference_claim_ledgers", serialized)

    def test_l3_reference_is_scoreable(self) -> None:
        references = run_l3_repeats.normalize_references()
        self.assertEqual(len(references), 40)
        for reference in references.values():
            components = {
                row["task_component_id"]
                for row in reference["ledger"]["task_components"]
            }
            for component in components:
                required = [
                    row
                    for row in reference["ledger"]["claim_groups"]
                    if row["task_component_id"] == component
                    and row["importance"] == "core"
                    and row["scoring_role"] == "required_content"
                ]
                self.assertTrue(required)

    def test_l3_canonicalization_is_citation_blind(self) -> None:
        value = l3_scoring.canonicalize_answer(
            "Supported claim [C1]. Another [C2-C3]."
        )
        self.assertNotIn("[C", value)
        self.assertIn("Supported claim", value)

    def test_l3_payload_is_one_answer_and_system_anonymous(self) -> None:
        reference = next(
            iter(run_l3_repeats.normalize_references().values())
        )
        payload = {
            "question_id": reference["question_id"],
            "question": reference["question_text"],
            "task_boundaries": reference["task_boundaries"],
            "task_components": reference["ledger"]["task_components"],
            "content_claim_groups": reference["ledger"]["claim_groups"],
            "constraint_only_groups": reference["ledger"][
                "constraint_groups"
            ],
            "gold_is_non_exhaustive": True,
            "anonymous_candidate_answer": "An answer.",
        }
        serialized = json.dumps(payload)
        self.assertNotIn('"system"', serialized)
        self.assertNotIn("retrieved_context", serialized)
        self.assertEqual(
            set(payload) & {"answer_a", "answer_b"},
            set(),
        )

    def test_resume_requires_exact_request_hash(self) -> None:
        items = [{"question_id": "Q", "value": "same"}]

        def expected(item: dict) -> str:
            return common.payload_sha256(item["value"])

        calls = []

        def worker(item: dict) -> dict:
            calls.append(item["question_id"])
            return {
                "question_id": item["question_id"],
                "execution_sha256": expected(item),
            }

        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "rows.jsonl"
            common.run_resumable(
                items=items,
                key=lambda row: row["question_id"],
                expected_execution_hash=expected,
                worker=worker,
                output=output,
                workers=1,
                resume=False,
                label="test",
            )
            common.run_resumable(
                items=items,
                key=lambda row: row["question_id"],
                expected_execution_hash=expected,
                worker=worker,
                output=output,
                workers=1,
                resume=True,
                label="test",
            )
            self.assertEqual(calls, ["Q"])
            with self.assertRaisesRegex(RuntimeError, "resume hash mismatch"):
                common.run_resumable(
                    items=[{"question_id": "Q", "value": "changed"}],
                    key=lambda row: row["question_id"],
                    expected_execution_hash=expected,
                    worker=worker,
                    output=output,
                    workers=1,
                    resume=True,
                    label="test",
                )

    def test_call_count_and_repeat_policy(self) -> None:
        protocol = json.loads(
            (PACKAGE / "protocol.json").read_text(encoding="utf-8")
        )
        self.assertEqual(protocol["planned_paid_calls"]["total"], 960)
        self.assertEqual(protocol["l3"]["repeat_count"], 3)
        self.assertFalse(protocol["l3"]["bootstrap"])
        self.assertEqual(
            protocol["execution_safety"]["automatic_sdk_retries"],
            0,
        )
        self.assertEqual(
            protocol["terminal_refusal_policy"]["status"],
            "execution_amendment_1",
        )
        self.assertFalse(
            protocol["terminal_refusal_policy"]["prompt_or_metric_change"]
        )


if __name__ == "__main__":
    unittest.main()

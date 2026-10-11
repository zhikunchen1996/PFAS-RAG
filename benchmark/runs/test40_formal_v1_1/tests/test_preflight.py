from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import common  # noqa: E402
import build_scoring_reference_v2  # noqa: E402
import run_generation  # noqa: E402
import run_l15  # noqa: E402
import run_l3_repeats  # noqa: E402
import run_retrieval  # noqa: E402
import run_selector  # noqa: E402
import preflight  # noqa: E402
import l3_scoring  # noqa: E402


class Test40PreflightTests(unittest.TestCase):
    def test_scoring_reference_successor_is_reproducible(self) -> None:
        build_scoring_reference_v2.verify()

    def test_frozen_reference_is_scoreable(self) -> None:
        references = run_l3_repeats.normalize_references()
        self.assertEqual(len(references), 40)
        for reference in references.values():
            ledger = reference["ledger"]
            components = {
                row["task_component_id"]
                for row in ledger["task_components"]
            }
            for component in components:
                required = [
                    row
                    for row in ledger["claim_groups"]
                    if row["task_component_id"] == component
                    and row["importance"] == "core"
                    and row["scoring_role"] == "required_content"
                ]
                self.assertTrue(required)

    def test_scoring_reference_patch_is_candidate_blind(self) -> None:
        manifest = json.loads(
            build_scoring_reference_v2.MANIFEST.read_text(encoding="utf-8")
        )
        self.assertFalse(manifest["candidate_test40_answers_used"])
        self.assertFalse(manifest["candidate_test40_contexts_used"])
        self.assertFalse(manifest["system_identities_used"])
        self.assertFalse(manifest["question_text_changed"])
        self.assertFalse(manifest["gold_evidence_changed"])
        self.assertEqual(len(manifest["operations"]), 10)

    def test_tagger_payload_excludes_hidden_fields(self) -> None:
        question = {"question_text": "What is supported?"}
        retrieval = {
            "retrieved_context": [
                {
                    "rank": 1,
                    "doc_id": "D1",
                    "chunk_id": "C1",
                    "citation": "Source",
                    "section": "results",
                    "text": "Evidence text.",
                    "score": 99,
                }
            ]
        }
        payload = run_generation.tagger_payload(question, retrieval)
        serialized = json.dumps(payload)
        self.assertNotIn("retrieval_system", serialized)
        self.assertNotIn("gold_evidence", serialized)
        self.assertNotIn("must_include", serialized)
        self.assertNotIn('"score"', serialized)
        self.assertNotIn('"rank"', serialized)

    def test_answer_prompt_does_not_expose_system_identity(self) -> None:
        item = {
            "system": "secret_system_label",
            "question": {"question_text": "What is supported?"},
            "retrieval": {
                "retrieved_context": [
                    {
                        "rank": rank,
                        "doc_id": f"D{rank}",
                        "chunk_id": f"C{rank}",
                        "citation": f"Source {rank}",
                        "section": "results",
                        "text": f"Full evidence {rank}.",
                    }
                    for rank in range(1, 11)
                ]
            },
        }
        tag_row = {
            "validated_chunk_tags": [
                {
                    "candidate_id": rank,
                    "eligibility": "direct_evidence",
                    "detail_policy": "use_full_claim",
                    "evidence_polarity": "support",
                    "exact_support": f"Full evidence {rank}.",
                    "confidence": 1.0,
                }
                for rank in range(1, 11)
            ]
        }
        prompt = run_generation.answer_user_prompt(
            item,
            tag_row,
            common.ANSWER_PROMPT.read_text(encoding="utf-8"),
        )
        self.assertNotIn("secret_system_label", prompt)
        self.assertIn("Full evidence 10.", prompt)

    def test_selector_payload_keeps_full_chunk(self) -> None:
        long_text = "PFAS evidence " * 1000
        payload = run_selector.selector_payload(
            {"question_text": "Question"},
            [
                {
                    "citation": "Source",
                    "section": "results",
                    "text": long_text,
                }
            ],
        )
        self.assertIn("PFAS evidence", payload["candidates"])
        self.assertGreater(len(payload["candidates"]), len(long_text) - 10)
        self.assertEqual(set(payload), {"question", "instruction", "candidates"})

    def test_l15_context_requires_complete_rank_mapping(self) -> None:
        answer = {
            "question_id": "Q",
            "answer": "Claim [C1].",
            "retrieved_context": [
                {"rank": rank, "text": f"chunk {rank}"}
                for rank in range(1, 11)
            ],
        }
        context = run_l15.complete_context(answer)
        self.assertEqual(len(context), 10)
        self.assertEqual(context[0]["citation_id"], "C1")

    def test_l15_result_rejects_unknown_citation(self) -> None:
        result = {
            "cited_claims": [
                {
                    "claim_id": "S1",
                    "claim": "Claim",
                    "citation_ids": ["C11"],
                    "support": "supported",
                }
            ],
            "uncited_source_dependent_claims": [],
        }
        with self.assertRaisesRegex(RuntimeError, "invalid cited claim schema"):
            run_l15.validate_result(
                result,
                "system::Q",
                {f"C{rank}" for rank in range(1, 11)},
            )

    def test_bge_passage_matches_frozen_dev_truncation(self) -> None:
        text = "x" * (run_retrieval.BGE_MAX_CHARS + 50)
        passage = run_retrieval.candidate_passage(
            {
                "title": "Title",
                "section": "results",
                "text": text,
            }
        )
        self.assertTrue(passage.endswith("x" * run_retrieval.BGE_MAX_CHARS))

    def test_context_normalization_preserves_zero_chunk_id(self) -> None:
        normalized = common.normalize_context_hit(
            {
                "source": "document.pdf",
                "chunk": 0,
                "section": "abstract",
                "text": "Complete first chunk.",
            },
            1,
        )
        self.assertEqual(normalized["chunk_id"], "0")
        common.validate_contexts(
            [{"question_id": "Q", "retrieved_context": [normalized]}],
            expected_count=1,
            source="test",
        )

    def test_retrieval_device_resolution_is_runtime_validated(self) -> None:
        self.assertEqual(run_retrieval.resolve_device("cpu"), "cpu")
        self.assertIn(
            run_retrieval.resolve_device("auto"),
            {"cpu", "mps", "cuda"},
        )

    def test_formal_output_paths_are_canonical(self) -> None:
        common.require_exact_path(
            common.RETRIEVAL_RESULTS,
            common.RETRIEVAL_RESULTS,
            label="test",
        )
        with self.assertRaisesRegex(RuntimeError, "canonical path"):
            common.require_exact_path(
                common.PACKAGE / "elsewhere",
                common.RETRIEVAL_RESULTS,
                label="test",
            )

    def test_resume_reuses_only_exact_request_hash(self) -> None:
        items = [{"item_id": "A", "request": "same"}]

        def expected(item: dict) -> str:
            return common.payload_sha256(item["request"])

        calls = []

        def worker(item: dict) -> dict:
            calls.append(item["item_id"])
            return {
                "item_id": item["item_id"],
                "execution_sha256": expected(item),
            }

        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "rows.jsonl"
            first = common.run_resumable(
                items=items,
                key=lambda row: row["item_id"],
                expected_execution_hash=expected,
                worker=worker,
                output=output,
                workers=1,
                resume=False,
                label="test",
            )
            second = common.run_resumable(
                items=items,
                key=lambda row: row["item_id"],
                expected_execution_hash=expected,
                worker=worker,
                output=output,
                workers=1,
                resume=True,
                label="test",
            )
            self.assertEqual(first, second)
            self.assertEqual(calls, ["A"])

            changed = [{"item_id": "A", "request": "changed"}]
            with self.assertRaisesRegex(RuntimeError, "resume hash mismatch"):
                common.run_resumable(
                    items=changed,
                    key=lambda row: row["item_id"],
                    expected_execution_hash=expected,
                    worker=worker,
                    output=output,
                    workers=1,
                    resume=True,
                    label="test",
                )

    def test_protocol_call_count_and_repeat_policy(self) -> None:
        protocol = json.loads(
            (SCRIPTS.parent / "protocol.json").read_text(encoding="utf-8")
        )
        self.assertEqual(protocol["planned_paid_calls"]["total"], 760)
        self.assertEqual(protocol["l3"]["repeat_count"], 3)
        self.assertFalse(protocol["l3"]["bootstrap"])
        self.assertEqual(
            protocol["execution_safety"]["automatic_sdk_retries"],
            0,
        )

    def test_runtime_reference_scan_does_not_flag_its_rules(self) -> None:
        preflight.validate_runtime_references()

    def test_l3_component_balanced_scoring(self) -> None:
        reference = {
            "question_id": "Q",
            "ledger": {
                "task_components": [
                    {"task_component_id": "T1"},
                    {"task_component_id": "T2"},
                ],
                "claim_groups": [
                    {
                        "claim_group_id": "G1",
                        "task_component_id": "T1",
                        "importance": "core",
                        "scoring_role": "required_content",
                    },
                    {
                        "claim_group_id": "G2",
                        "task_component_id": "T1",
                        "importance": "core",
                        "scoring_role": "required_content",
                    },
                    {
                        "claim_group_id": "G3",
                        "task_component_id": "T2",
                        "importance": "core",
                        "scoring_role": "required_content",
                    },
                ],
                "constraint_groups": [],
            },
        }
        result = {
            "claim_assessments": [
                {"claim_group_id": "G1", "status": "full"},
                {"claim_group_id": "G2", "status": "partial"},
                {"claim_group_id": "G3", "status": "absent"},
            ],
            "constraint_assessments": [],
            "reference_anchored_material_error": False,
            "potential_external_scientific_error": False,
        }
        score = l3_scoring.score_result(result, reference)
        self.assertEqual(
            score["component_balanced_core_reference_claim_coverage"],
            0.375,
        )

    def test_l3_payloads_are_single_answer_and_system_anonymous(self) -> None:
        references = run_l3_repeats.normalize_references()
        qids = list(references)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for system in run_l3_repeats.SYSTEMS:
                path = run_l3_repeats.answer_path(root, system)
                common.write_jsonl(
                    path,
                    [
                        {
                            "question_id": qid,
                            "answer": "Supported statement [C1].",
                        }
                        for qid in qids
                    ],
                )
            items, _ = run_l3_repeats.build_items(root, references)
        self.assertEqual(len(items), 120)
        for item in items:
            payload = item["payload"]
            self.assertNotIn("system", payload)
            self.assertNotIn("retrieved_context", payload)
            self.assertNotIn("[C1]", payload["anonymous_candidate_answer"])


if __name__ == "__main__":
    unittest.main()

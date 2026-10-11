from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
SCRIPTS = PACKAGE / "scripts"
sys.path.insert(0, str(SCRIPTS))

import common  # noqa: E402


def load_scoring_module():
    path = SCRIPTS / "run_l3_scoring.py"
    spec = importlib.util.spec_from_file_location("l3_scoring", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_scoring_v2_module():
    path = SCRIPTS / "run_l3_scoring_v2.py"
    spec = importlib.util.spec_from_file_location("l3_scoring_v2", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class L3PipelineTests(unittest.TestCase):
    def test_reference_packets_exclude_candidate_outputs(self) -> None:
        packets = common.read_jsonl(common.PACKETS)
        self.assertEqual(len(packets), 13)
        forbidden = {
            "direct_answer",
            "rag_answer",
            "candidate_answer",
            "retrieved_context",
            "prior_judge_outcome",
        }
        for packet in packets:
            self.assertTrue(forbidden.isdisjoint(packet))
            self.assertTrue(packet["gold_evidence"])

    def test_citation_marker_removal_preserves_content(self) -> None:
        scoring = load_scoring_module()
        text = (
            "PFOS removal was 80% [C1], but destruction was not shown "
            "[C2, C3]."
        )
        normalized = scoring.strip_citation_markers(text)
        self.assertNotIn("[C", normalized)
        self.assertIn("PFOS removal was 80%", normalized)
        self.assertIn("destruction was not shown", normalized)

    def test_transparent_pass_rule(self) -> None:
        scoring = load_scoring_module()
        reference = {
            "question_id": "Q1",
            "reference": {
                "claims": [
                    {"claim_id": "Q1-C01", "claim_type": "core"},
                    {"claim_id": "Q1-C02", "claim_type": "supporting"},
                ]
            },
        }
        result = {
            "claim_assessments": [
                {"claim_id": "Q1-C01", "status": "full"},
                {"claim_id": "Q1-C02", "status": "absent"},
            ],
            "task_boundary_violation": False,
            "major_scientific_error": False,
        }
        scores = scoring.score_result(result, reference)
        self.assertEqual(scores["core_gold_claim_coverage"], 1.0)
        self.assertEqual(scores["all_gold_claim_coverage"], 0.5)
        self.assertTrue(scores["l3_gold_referenced_adequacy_pass"])

    def test_core_contradiction_forces_failure(self) -> None:
        scoring = load_scoring_module()
        reference = {
            "question_id": "Q1",
            "reference": {
                "claims": [{"claim_id": "Q1-C01", "claim_type": "core"}]
            },
        }
        result = {
            "claim_assessments": [
                {"claim_id": "Q1-C01", "status": "contradicted"}
            ],
            "task_boundary_violation": False,
            "major_scientific_error": False,
        }
        scores = scoring.score_result(result, reference)
        self.assertEqual(scores["contradicted_core_claims"], 1)
        self.assertFalse(scores["l3_gold_referenced_adequacy_pass"])

    def test_missing_support_map_entry_uses_exact_span(self) -> None:
        import run_reference_revision_v2 as revision

        packet = {
            "question_id": "Q1",
            "gold_evidence": [
                {
                    "evidence_id": "E1",
                    "exact_evidence_span": "Audited exact evidence.",
                }
            ],
        }
        result = {
            "claim_groups": [
                {
                    "claim_group_id": "G1",
                    "evidence_ids": ["E1"],
                    "evidence_support_map": [],
                }
            ],
            "constraint_groups": [],
        }
        revision.enrich_exact_spans(result, packet)
        self.assertEqual(
            result["claim_groups"][0]["exact_spans"],
            [
                {
                    "evidence_id": "E1",
                    "exact_evidence_span": "Audited exact evidence.",
                    "supports": "Audited exact evidence.",
                }
            ],
        )

    def test_dict_support_map_is_normalized(self) -> None:
        import run_reference_revision_v2 as revision

        packet = {
            "question_id": "Q1",
            "gold_evidence": [
                {"evidence_id": "E1", "exact_evidence_span": "Exact span."}
            ],
        }
        result = {
            "claim_groups": [
                {
                    "claim_group_id": "G1",
                    "evidence_ids": ["E1"],
                    "evidence_support_map": {"E1": "Direct support."},
                }
            ],
            "constraint_groups": [],
        }
        revision.enrich_exact_spans(result, packet)
        self.assertEqual(
            result["claim_groups"][0]["exact_spans"][0]["supports"],
            "Direct support.",
        )

    def test_question_derived_constraint_can_have_no_evidence(self) -> None:
        import run_reference_revision_v2 as revision

        result = {
            "claim_groups": [],
            "constraint_groups": [
                {
                    "claim_group_id": "B1",
                    "scoring_role": "constraint_only",
                    "evidence_ids": [],
                    "evidence_support_map": [],
                }
            ],
        }
        revision.enrich_exact_spans(
            result,
            {"question_id": "Q1", "gold_evidence": []},
        )
        self.assertEqual(result["constraint_groups"][0]["exact_spans"], [])

    def test_duplicate_evidence_ids_are_rejected(self) -> None:
        import run_reference_revision_v2 as revision

        evidence = {
            "E1": {"evidence_id": "E1", "exact_evidence_span": "Exact."}
        }
        group = {
            "claim_group_id": "G1",
            "evidence_ids": ["E1", "E1"],
            "exact_spans": [
                {"evidence_id": "E1", "exact_evidence_span": "Exact."},
                {"evidence_id": "E1", "exact_evidence_span": "Exact."},
            ],
        }
        with self.assertRaises(RuntimeError):
            revision.validate_exact_spans(
                qid="Q1",
                group=group,
                evidence_by_id=evidence,
            )

    def test_parallel_runner_persists_success_before_raising(self) -> None:
        items = [{"id": "ok"}, {"id": "bad"}]

        def worker(item):
            if item["id"] == "bad":
                raise ValueError("expected failure")
            return item

        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "rows.jsonl"
            with self.assertRaises(RuntimeError):
                common.run_parallel(
                    items=items,
                    worker=worker,
                    key=lambda row: row["id"],
                    output=output,
                    workers=2,
                    resume=False,
                )
            self.assertEqual(common.read_jsonl(output), [{"id": "ok"}])

    def test_parallel_runner_writes_empty_output(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "rows.jsonl"
            rows = common.run_parallel(
                items=[],
                worker=lambda item: item,
                key=lambda row: row["id"],
                output=output,
                workers=1,
                resume=False,
            )
            self.assertEqual(rows, [])
            self.assertTrue(output.exists())
            self.assertEqual(output.read_text(encoding="utf-8"), "")

    def test_repair_removes_only_known_echoed_input_fields(self) -> None:
        import run_reference_repair_v2 as repair

        result = {
            "question_id": "Q1",
            "claim_groups": [],
            "reference_construction_packet": {"question_id": "Q1"},
            "current_model_b_group_review": {"overall_verdict": "revise"},
        }
        repair.remove_echoed_input_fields(result)
        self.assertEqual(
            result,
            {"question_id": "Q1", "claim_groups": []},
        )

    def test_repair_unwraps_only_one_complete_ledger(self) -> None:
        import run_reference_repair_v2 as repair
        import run_reference_revision_v2 as revision

        ledger = {key: [] for key in revision.REQUIRED_REVISION_KEYS}
        ledger["question_id"] = "Q1"
        wrapped = {"replacement_ledger": ledger, "note": "complete"}
        self.assertEqual(
            repair.extract_replacement_ledger(wrapped),
            ledger,
        )

    def test_repair_moves_only_constraint_only_groups(self) -> None:
        import run_reference_repair_v2 as repair

        constraint = {
            "claim_group_id": "B1",
            "scoring_role": "constraint_only",
        }
        content = {
            "claim_group_id": "G1",
            "scoring_role": "required_content",
        }
        result = {
            "claim_groups": [constraint, content],
            "constraint_groups": [],
        }
        repair.normalize_group_locations(result)
        self.assertEqual(result["claim_groups"], [content])
        self.assertEqual(result["constraint_groups"], [constraint])

    def test_repair_prefers_existing_constraint_on_duplicate_id(self) -> None:
        import run_reference_repair_v2 as repair

        misplaced = {
            "claim_group_id": "B1",
            "scoring_role": "constraint_only",
            "canonical_proposition": "misplaced",
        }
        existing = {
            "claim_group_id": "B1",
            "scoring_role": "constraint_only",
            "canonical_proposition": "existing",
        }
        result = {
            "claim_groups": [misplaced],
            "constraint_groups": [existing],
        }
        repair.normalize_group_locations(result)
        self.assertEqual(result["claim_groups"], [])
        self.assertEqual(result["constraint_groups"], [existing])

    def test_repair_normalizes_known_ontology_aliases(self) -> None:
        import run_reference_repair_v2 as repair

        result = {
            "claim_groups": [
                {
                    "importance": "optional_evidence",
                    "scoring_role": "supplementary_content",
                }
            ],
            "constraint_groups": [
                {"scoring_role": "constraint"}
            ],
        }
        repair.normalize_ontology_labels(result)
        self.assertEqual(
            result["claim_groups"][0],
            {
                "importance": "supplementary",
                "scoring_role": "optional_content",
            },
        )
        self.assertEqual(
            result["constraint_groups"][0]["scoring_role"],
            "constraint_only",
        )

    def test_verification_compaction_keeps_only_open_review_items(self) -> None:
        import run_reference_group_verification_v2 as verification

        review = {
            "question_id": "Q1",
            "overall_verdict": "revise",
            "component_reviews": [
                {"task_component_id": "T1", "verdict": "approve"},
                {"task_component_id": "T2", "verdict": "revise"},
            ],
            "claim_group_reviews": [
                {"claim_group_id": "G1", "verdict": "supported"},
                {"claim_group_id": "G2", "verdict": "partially_supported"},
            ],
            "constraint_group_reviews": [],
            "atomic_disposition_complete": True,
            "unresolved_prior_claim_ids": [],
            "duplicate_or_weighting_issues": ["duplicate"],
            "prose_ledger_issues": [],
            "omitted_major_gold_findings": [],
            "human_review_priorities": ["check G2"],
        }
        compact = verification.compact_prior_group_review(review)
        self.assertEqual(
            [row["task_component_id"] for row in compact[
                "component_reviews_requiring_revision"
            ]],
            ["T2"],
        )
        self.assertEqual(
            [row["claim_group_id"] for row in compact[
                "group_reviews_requiring_revision"
            ]],
            ["G2"],
        )

    def test_verification_reuses_only_clean_hash_matched_review(self) -> None:
        import run_reference_group_verification_v2 as verification

        revised = {
            "task_components": [{"task_component_id": "Q1-T01"}],
            "claim_groups": [
                {
                    "claim_group_id": "Q1-G01",
                    "task_component_id": "Q1-T01",
                }
            ],
            "constraint_groups": [],
        }
        packet = {
            "question_id": "Q1",
            "gold_evidence": [{"evidence_id": "E1"}],
        }
        review = {
            "question_id": "Q1",
            "overall_verdict": "approve",
            "component_reviews": [
                {"task_component_id": "Q1-T01", "verdict": "approve"}
            ],
            "claim_group_reviews": [
                {
                    "claim_group_id": "Q1-G01",
                    "verdict": "supported",
                    "verified_evidence_ids": ["E1"],
                }
            ],
            "constraint_group_reviews": [],
            "atomic_disposition_complete": True,
            "unresolved_prior_claim_ids": [],
            "duplicate_or_weighting_issues": [],
            "prose_ledger_issues": [],
            "omitted_major_gold_findings": [],
        }
        row = {
            "question_id": "Q1",
            "packet_sha256": common.payload_sha256(packet),
            "revision_sha256": common.payload_sha256(revised),
            "review": review,
        }
        reused = verification.reusable_clean_review(
            row,
            packet=packet,
            revised=revised,
            source_path=PACKAGE / "prior.jsonl",
            source_sha256="abc",
        )
        self.assertIsNotNone(reused)
        self.assertTrue(reused["reuse"]["reused"])
        row["packet_sha256"] = "wrong"
        self.assertIsNone(
            verification.reusable_clean_review(
                row,
                packet=packet,
                revised=revised,
                source_path=PACKAGE / "prior.jsonl",
                source_sha256="abc",
            )
        )
        row["packet_sha256"] = common.payload_sha256(packet)
        row["revision_sha256"] = "wrong"
        self.assertIsNone(
            verification.reusable_clean_review(
                row,
                packet=packet,
                revised=revised,
                source_path=PACKAGE / "prior.jsonl",
                source_sha256="abc",
            )
        )


class L3V2ScoringTests(unittest.TestCase):
    def reference(self):
        return {
            "question_id": "Q1",
            "ledger": {
                "task_components": [
                    {"task_component_id": "Q1-T01"},
                    {"task_component_id": "Q1-T02"},
                ],
                "claim_groups": [
                    {
                        "claim_group_id": "Q1-G01",
                        "task_component_id": "Q1-T01",
                        "importance": "core",
                        "scoring_role": "required_content",
                    },
                    {
                        "claim_group_id": "Q1-G02",
                        "task_component_id": "Q1-T02",
                        "importance": "core",
                        "scoring_role": "required_content",
                    },
                    {
                        "claim_group_id": "Q1-G03",
                        "task_component_id": "Q1-T02",
                        "importance": "supplementary",
                        "scoring_role": "optional_content",
                    },
                ],
                "constraint_groups": [{"claim_group_id": "Q1-B01"}],
            },
        }

    def result(self):
        return {
            "claim_assessments": [
                {"claim_group_id": "Q1-G01", "status": "full"},
                {"claim_group_id": "Q1-G02", "status": "partial"},
                {"claim_group_id": "Q1-G03", "status": "absent"},
            ],
            "constraint_assessments": [
                {"claim_group_id": "Q1-B01", "status": "compliant"}
            ],
            "reference_anchored_material_error": False,
            "potential_external_scientific_error": False,
        }

    def test_component_balanced_core_coverage(self) -> None:
        scoring = load_scoring_v2_module()
        scores = scoring.score_result(self.result(), self.reference())
        self.assertEqual(
            scores["component_balanced_core_reference_claim_coverage"],
            0.75,
        )
        self.assertEqual(
            scores["strict_core_reference_claim_coverage"],
            0.5,
        )
        self.assertEqual(
            scores["supplementary_reference_claim_coverage"],
            0.0,
        )
        self.assertIsNone(scores["l3_gold_referenced_adequacy_pass"])

    def test_optional_content_does_not_change_core_score(self) -> None:
        scoring = load_scoring_v2_module()
        result = self.result()
        first = scoring.score_result(result, self.reference())
        result["claim_assessments"][2]["status"] = "full"
        second = scoring.score_result(result, self.reference())
        self.assertEqual(
            first["component_balanced_core_reference_claim_coverage"],
            second["component_balanced_core_reference_claim_coverage"],
        )

    def test_threshold_requires_all_gates(self) -> None:
        scoring = load_scoring_v2_module()
        scores = scoring.score_result(
            self.result(),
            self.reference(),
            threshold=0.7,
        )
        self.assertTrue(scores["l3_gold_referenced_adequacy_pass"])
        contradicted = self.result()
        contradicted["claim_assessments"][0]["status"] = "contradicted"
        scores = scoring.score_result(
            contradicted,
            self.reference(),
            threshold=0.2,
        )
        self.assertFalse(scores["l3_gold_referenced_adequacy_pass"])

    def test_judge_validation_rejects_duplicate_group_ids(self) -> None:
        scoring = load_scoring_v2_module()
        result = self.result()
        result["claim_assessments"].append(
            {"claim_group_id": "Q1-G01", "status": "full"}
        )
        with self.assertRaises(RuntimeError):
            scoring.validate_result(result, self.reference())

    def test_judge_validation_rejects_string_boolean(self) -> None:
        scoring = load_scoring_v2_module()
        result = self.result()
        result["reference_anchored_material_error"] = "false"
        with self.assertRaises(RuntimeError):
            scoring.validate_result(result, self.reference())

    def test_paired_bootstrap_uses_question_level_differences(self) -> None:
        scoring = load_scoring_v2_module()
        result = scoring.paired_question_bootstrap(
            {"Q1": 0.2, "Q2": 0.4},
            {"Q1": 0.5, "Q2": 0.5},
            iterations=1000,
            seed=7,
        )
        self.assertAlmostEqual(result["mean_difference_b_minus_a"], 0.2)
        self.assertLessEqual(result["ci95_lower"], 0.2)
        self.assertGreaterEqual(result["ci95_upper"], 0.2)

    def test_canonicalization_removes_identity_cues(self) -> None:
        scoring = load_scoring_v2_module()
        text = (
            "Based on the retrieved context, PFOS was retained [C1–C3,C7].\n"
            "The retrieved evidence supports a limited conclusion.\n"
            "A [specific interfacial area] term remains substantive.\n"
            "References\n1. Example"
        )
        normalized = scoring.canonicalize_answer(text)
        self.assertEqual(
            normalized,
            "PFOS was retained.\n"
            "The available evidence supports a limited conclusion.\n"
            "A [specific interfacial area] term remains substantive.",
        )


if __name__ == "__main__":
    unittest.main()

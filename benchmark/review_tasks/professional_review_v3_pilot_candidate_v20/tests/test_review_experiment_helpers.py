from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import json
import sys
import tempfile
import unittest


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
SPEC = spec_from_file_location(
    "run_review_experiment",
    SCRIPTS / "run_review_experiment.py",
)
MODULE = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class ReviewExperimentHelperTests(unittest.TestCase):
    def test_record_citations_are_normalized_to_source_ids(self):
        text = (
            "Claim [S01-R03]. Combined [S01, S01-R02, S02]. "
            "Plain identifier S03-R01 outside brackets is unchanged."
        )
        normalized, changes = MODULE.normalize_record_citation_ids(text)
        self.assertEqual(
            normalized,
            "Claim [S01]. Combined [S01, S02]. "
            "Plain identifier S03-R01 outside brackets is unchanged.",
        )
        self.assertEqual(len(changes), 2)
        self.assertEqual(changes[0]["original"], "[S01-R03]")
        self.assertEqual(changes[0]["replacement"], "[S01]")

    def test_layer_b_anonymizes_local_and_web_citations(self):
        text = (
            "Local result [S01, S02-E03]. Web result [WEB01-R02].\n\n"
            "## References\nS01 Example\nWEB01 Example\n"
        )
        anonymized, audit = (
            MODULE.prepare_anonymous_citation_aware_layer_b_review(text)
        )
        self.assertEqual(
            anonymized,
            "Local result [R01, R02]. Web result [R03].\n\n"
            "## References\nR01 Example\nR03 Example\n",
        )
        self.assertEqual(audit["replacement_count"], 5)
        self.assertEqual(audit["unique_cited_source_count"], 3)
        self.assertNotRegex(anonymized, r"(?:S|WEB)[0-9]{2}")

    def test_layer_b_anonymization_preserves_non_source_brackets(self):
        text = "A range [0, 1] and chemical notation [M] remain [S01]."
        anonymized, _ = (
            MODULE.prepare_anonymous_citation_aware_layer_b_review(text)
        )
        self.assertEqual(
            anonymized,
            "A range [0, 1] and chemical notation [M] remain [R01].\n",
        )

    def test_layer_b_anonymization_normalizes_unbracketed_source_identifier(self):
        anonymized, _ = (
            MODULE.prepare_anonymous_citation_aware_layer_b_review(
                "A claim attributed to S01 outside brackets."
            )
        )
        self.assertEqual(
            anonymized,
            "A claim attributed to R01 outside brackets.\n",
        )

    def test_layer_b_anonymization_handles_mixed_source_bracket(self):
        anonymized, _ = (
            MODULE.prepare_anonymous_citation_aware_layer_b_review(
                "A mixed citation [S01, unclear] preserves its content."
            )
        )
        self.assertEqual(
            anonymized,
            "A mixed citation [R01, unclear] preserves its content.\n",
        )

    def test_synthesis_excerpts_remove_retrieval_metadata(self):
        sources = [
            {
                "source_id": "S01",
                "citation": "Example citation",
                "title": "Example title",
                "covered_component_ids": ["RT02-C1"],
                "bge_score": 0.9,
                "access_scope": "full text",
                "source_limitations": "None reported",
                "evidence_chunks": [
                    {
                        "locator_id": "S01-E01",
                        "section": "results",
                        "text": "Complete scientific evidence text.",
                        "query_scores": {"RT02-C1": 0.8},
                    }
                ],
            }
        ]
        compact = MODULE.compact_supporting_excerpts_for_synthesis(sources)
        rendered = json.dumps(compact)
        self.assertIn("Complete scientific evidence text.", rendered)
        self.assertIn("full text", rendered)
        self.assertNotIn("RT02-C1", rendered)
        self.assertNotIn("query_scores", rendered)
        self.assertNotIn("bge_score", rendered)
        self.assertNotIn("covered_component_ids", rendered)

    def test_synthesis_requirements_remove_internal_identifiers(self):
        task = {
            "components": [
                {
                    "component_id": "RT09-C1",
                    "requirement": "Compare measured endpoints.",
                }
            ]
        }
        ledger = {
            "task_id": "RT09",
            "task_boundaries": "Preserve endpoint distinctions.",
            "required_component_ids": ["RT09-C1"],
            "constraints": [
                {
                    "constraint_id": "RT09-B1",
                    "material_violation_rule": "Do not overclaim.",
                }
            ],
        }
        components = MODULE.synthesis_component_text(task)
        boundaries = MODULE.synthesis_boundary_text(ledger)
        self.assertIn("Compare measured endpoints.", components)
        self.assertIn("Do not overclaim.", boundaries)
        self.assertNotIn("RT09", components)
        self.assertNotIn("RT09", boundaries)
        self.assertNotIn("component_id", components)
        self.assertNotIn("constraint_id", boundaries)

    def test_synthesis_compaction_preserves_non_supported_reasons(self):
        source = [
            {
                "record": {"record_id": "R1", "source_id": "S01"},
                "verification": {
                    "record_id": "R1",
                    "record_usable": True,
                    "record_usable_rationale": "Long redundant rationale.",
                    "anchor_exclusion_violation": False,
                    "field_assessments": [
                        {
                            "field_path": "matrix",
                            "status": "supported",
                            "error_type": "none",
                            "reason": "Long redundant support explanation.",
                        },
                        {
                            "field_path": "quantitative_findings[0].value",
                            "status": "partially_supported",
                            "error_type": "missing_qualifier",
                            "reason": "Only the upper bound is supported.",
                        },
                    ],
                },
            }
        ]
        compact = MODULE.compact_verified_records_for_synthesis(source)
        assessments = compact[0]["verification"]["field_assessments"]
        self.assertNotIn("reason", assessments[0])
        self.assertEqual(
            assessments[1]["reason"],
            "Only the upper bound is supported.",
        )
        self.assertNotIn(
            "record_usable_rationale", compact[0]["verification"]
        )
        self.assertIn(
            "reason", source[0]["verification"]["field_assessments"][0]
        )

    def test_citation_source_ids_union_plain_and_locator_forms(self):
        review = "Claim [S01]. Detail [S02-E03, S03-E01]. Repeat [S01-E02]."
        self.assertEqual(
            MODULE.citation_source_ids(review),
            ["S01", "S02", "S03", "S01"],
        )

    def test_paid_task_authorization_rejects_out_of_scope_task(self):
        protocol = {
            "execution_safety": {
                "paid_calls_authorized": True,
                "authorized_task_ids": ["RT01"],
                "authorized_stages": ["source_support", "review_judge"],
                "formal_ten_task_run_authorized": False,
            }
        }
        MODULE.enforce_paid_task_authorization(
            protocol=protocol,
            task_ids=["RT01"],
            stages=["source_support", "review_judge"],
            allow_paid=True,
        )
        with self.assertRaisesRegex(RuntimeError, "authorization failed"):
            MODULE.enforce_paid_task_authorization(
                protocol=protocol,
                task_ids=["RT02"],
                stages=["source_support", "review_judge"],
                allow_paid=True,
            )

        with self.assertRaisesRegex(RuntimeError, "stage authorization"):
            MODULE.enforce_paid_task_authorization(
                protocol=protocol,
                task_ids=["RT01"],
                stages=["synthesis"],
                allow_paid=True,
            )

    def test_unpaid_or_formal_execution_bypasses_pilot_allowlist(self):
        protocol = {
            "execution_safety": {
                "paid_calls_authorized": True,
                "authorized_task_ids": ["RT01"],
                "authorized_stages": ["source_support", "review_judge"],
                "formal_ten_task_run_authorized": False,
            }
        }
        MODULE.enforce_paid_task_authorization(
            protocol=protocol,
            task_ids=["RT01"],
            stages=["retrieval"],
            allow_paid=False,
        )
        protocol["execution_safety"]["formal_ten_task_run_authorized"] = True
        MODULE.enforce_paid_task_authorization(
            protocol=protocol,
            task_ids=["RT01", "RT02"],
            stages=["retrieval", "synthesis"],
            allow_paid=True,
        )

    def test_paid_execution_rejected_when_package_is_disabled(self):
        protocol = {
            "execution_safety": {
                "paid_calls_authorized": False,
                "authorized_task_ids": [],
                "authorized_stages": [],
                "formal_ten_task_run_authorized": False,
            }
        }
        with self.assertRaisesRegex(RuntimeError, "disabled"):
            MODULE.enforce_paid_task_authorization(
                protocol=protocol,
                task_ids=["RT01"],
                stages=["source_support"],
                allow_paid=True,
            )

    def test_direct_layer_a_metrics_are_zero_or_not_applicable(self):
        extraction = MODULE.extraction_metrics(
            Path("unused"), "RT01", "gpt51_direct"
        )
        self.assertEqual(extraction["evidence_access_mode"], "none")
        self.assertEqual(extraction["verified_usable_record_count"], 0)
        self.assertEqual(extraction["verified_unique_source_count"], 0)
        self.assertEqual(extraction["weighted_extracted_field_support"], "")
        self.assertEqual(extraction["numeric_transcription_accuracy"], "")

        support = MODULE.source_support_metrics(
            Path("unused"), "RT01", "gpt51_direct"
        )
        self.assertEqual(
            support["source_support_status"],
            "not_applicable_no_retrieved_sources",
        )
        self.assertEqual(support["unique_cited_sources"], 0)
        self.assertEqual(support["weighted_source_support_rate"], "")

    def test_quantitative_value_shape_validation(self):
        valid = (
            ("99.7", "exact_numeric"),
            ("31,000", "exact_numeric"),
            (">=95", "inequality"),
            (">=40,000", "inequality"),
            ("~2.5", "approximate_numeric"),
            ("30-55", "range"),
            ("ND", "not_detected"),
        )
        for value, value_form in valid:
            self.assertTrue(
                MODULE.quantitative_value_is_valid(
                    {"value": value, "value_form": value_form}
                )
            )
        self.assertFalse(
            MODULE.quantitative_value_is_valid(
                {"value": "nmol/L", "value_form": "exact_numeric"}
            )
        )
        self.assertFalse(
            MODULE.quantitative_value_is_valid(
                {"value": "99.7%", "value_form": "exact_numeric"}
            )
        )
        self.assertFalse(
            MODULE.quantitative_value_is_valid(
                {"value": "12,34", "value_form": "exact_numeric"}
            )
        )

    def test_unambiguous_approximate_value_is_normalized(self):
        finding = {
            "name": "Approximate capacity",
            "value": "44000",
            "value_form": "approximate_numeric",
            "unit": "BV",
        }
        normalized, reason = MODULE.normalize_quantitative_finding(finding)
        self.assertEqual(normalized["value"], "~44000")
        self.assertEqual(reason, "added_declared_approximation_marker")
        self.assertTrue(MODULE.quantitative_value_is_valid(normalized))
        self.assertEqual(finding["value"], "44000")

    def test_ambiguous_inequality_is_not_repaired(self):
        normalized, reason = MODULE.normalize_quantitative_finding(
            {
                "value": "78494",
                "value_form": "inequality",
                "unit": "BV",
            }
        )
        self.assertIsNone(normalized)
        self.assertIsNone(reason)

    def test_metric_field_path_classification_is_exact(self):
        self.assertTrue(
            MODULE.is_numeric_value_or_unit_assessment(
                {"field_path": "quantitative_findings[2].value"}
            )
        )
        self.assertFalse(
            MODULE.is_numeric_value_or_unit_assessment(
                {"field_path": "quantitative_findings[2].value_form"}
            )
        )
        self.assertTrue(
            MODULE.is_numeric_value_or_unit_assessment(
                {"field_path": "operating_conditions[2].unit"}
            )
        )
        self.assertTrue(
            MODULE.is_quantitative_value_or_unit_assessment(
                {"field_path": "quantitative_findings[2].unit"}
            )
        )
        self.assertFalse(
            MODULE.is_quantitative_value_or_unit_assessment(
                {"field_path": "operating_conditions[2].unit"}
            )
        )
        self.assertTrue(
            MODULE.is_endpoint_type_assessment(
                {"field_path": "endpoints[3].endpoint_type"}
            )
        )
        self.assertFalse(
            MODULE.is_endpoint_type_assessment(
                {"field_path": "endpoints[3].interpretation"}
            )
        )
        self.assertTrue(
            MODULE.is_comparability_status_assessment(
                {"field_path": "comparability.status"}
            )
        )

    def test_required_metric_paths_cover_each_existing_item(self):
        record = {
            "quantitative_findings": [{}, {}],
            "operating_conditions": [{}],
            "endpoints": [{}, {}, {}],
            "comparability": {},
        }
        self.assertEqual(
            MODULE.required_metric_assessment_paths(record),
            {
                "quantitative_findings[0].value",
                "quantitative_findings[0].unit",
                "quantitative_findings[1].value",
                "quantitative_findings[1].unit",
                "operating_conditions[0].value",
                "operating_conditions[0].unit",
                "endpoints[0].endpoint_type",
                "endpoints[1].endpoint_type",
                "endpoints[2].endpoint_type",
                "comparability.status",
            },
        )

    def test_extraction_schema_is_constrained_per_source(self):
        base = {
            "properties": {
                "task_id": {"type": "string"},
                "source_system": {"type": "string"},
            },
            "$defs": {
                "evidenceRecord": {
                    "properties": {
                        "source_id": {"type": "string"},
                    }
                },
                "evidenceText": {
                    "properties": {
                        "evidence_locator_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                        }
                    }
                },
            },
        }
        constrained = MODULE.extraction_schema_for_source(
            base,
            task_id="RT02",
            system="bge_llm_local_rag",
            source_id="S03",
            locator_ids=["S03-E02", "S03-E01"],
        )
        self.assertEqual(
            constrained["properties"]["task_id"]["enum"],
            ["RT02"],
        )
        self.assertEqual(
            constrained["properties"]["source_system"]["enum"],
            ["bge_llm_local_rag"],
        )
        self.assertEqual(
            constrained["$defs"]["evidenceRecord"]["properties"][
                "source_id"
            ]["enum"],
            ["S03"],
        )
        self.assertEqual(
            constrained["$defs"]["evidenceText"]["properties"][
                "evidence_locator_ids"
            ]["items"]["enum"],
            ["S03-E01", "S03-E02"],
        )
        self.assertNotIn("enum", base["properties"]["task_id"])

    def test_mean_present_handles_empty_metric(self):
        self.assertEqual(MODULE.mean_present([{"value": ""}], "value"), "")
        self.assertEqual(
            MODULE.mean_present([{"value": 0.5}, {"value": 1.0}], "value"),
            0.75,
        )

    def test_required_path_defects_and_completion_merge(self):
        record = {
            "quantitative_findings": [{}],
            "operating_conditions": [{}],
            "endpoints": [{}],
            "comparability": {},
        }
        initial = {
            "task_id": "RT02",
            "record_id": "R1",
            "anchor_exclusion_violation": False,
            "field_assessments": [
                {"field_path": "quantitative_findings[0].value"},
                {"field_path": "quantitative_findings[0].unit"},
                {"field_path": "endpoints[0].endpoint_type"},
                {"field_path": "comparability.status"},
            ],
            "record_usable": True,
            "record_usable_rationale": "Initially usable.",
        }
        missing, duplicated = MODULE.required_assessment_path_defects(
            record,
            initial,
        )
        self.assertEqual(
            missing,
            [
                "operating_conditions[0].unit",
                "operating_conditions[0].value",
            ],
        )
        self.assertEqual(duplicated, [])
        completion = {
            "task_id": "RT02",
            "record_id": "R1",
            "anchor_exclusion_violation": False,
            "field_assessments": [
                {"field_path": "operating_conditions[0].unit"},
                {"field_path": "operating_conditions[0].value"},
            ],
            "record_usable": False,
            "record_usable_rationale": "A core condition is unsupported.",
        }
        merged = MODULE.merge_verification_completion(
            initial=initial,
            completion=completion,
            required_paths=missing,
        )
        self.assertFalse(merged["record_usable"])
        self.assertEqual(len(merged["field_assessments"]), 6)
        self.assertTrue(merged["verification_completion_applied"])

    def test_completion_rejects_unrequested_path(self):
        with self.assertRaisesRegex(RuntimeError, "unexpected field paths"):
            MODULE.merge_verification_completion(
                initial={
                    "anchor_exclusion_violation": False,
                    "field_assessments": [],
                    "record_usable": True,
                    "record_usable_rationale": "Initial.",
                },
                completion={
                    "anchor_exclusion_violation": False,
                    "field_assessments": [
                        {"field_path": "comparability.status"}
                    ],
                    "record_usable": True,
                    "record_usable_rationale": "Completion.",
                },
                required_paths=["operating_conditions[0].unit"],
            )

    def test_internal_review_notation_is_removed_and_audited(self):
        text = (
            "## Evidence hierarchy (RT09-C1)\n"
            "Do not overclaim (to comply with RT09-B2).\n"
            "## Minimum evidence (Component RT02-C3)\n"
            "## Translation limits (C2)\n"
            "Ordinary scientific text remains."
        )
        cleaned, removed = MODULE.sanitize_internal_review_notation(text)
        self.assertNotIn("RT09", cleaned)
        self.assertNotIn("(C2)", cleaned)
        self.assertIn("Ordinary scientific text remains.", cleaned)
        self.assertEqual(len(removed), 4)

    def test_bare_internal_label_is_not_silently_rewritten(self):
        with self.assertRaisesRegex(RuntimeError, "outside a removable"):
            MODULE.sanitize_internal_review_notation(
                "This sentence exposes RT09-C1 without parentheses."
            )

    def test_collects_nested_locator_ids(self):
        record = {
            "evidence_locator_ids": ["S01-E01"],
            "endpoints": [
                {"evidence_locator_ids": ["S01-E02"]},
            ],
            "quantitative_findings": [
                {"evidence_locator_ids": ["S01-E03"]},
            ],
        }
        self.assertEqual(
            MODULE.all_locator_ids(record),
            {"S01-E01", "S01-E02", "S01-E03"},
        )

    def test_consulted_source_url_matching(self):
        sources = [
            {
                "url": "https://example.org/paper?id=1",
                "title": "Paper",
                "type": "url",
            }
        ]
        self.assertTrue(
            MODULE.consulted_source_match(
                "https://example.org/paper",
                "",
                sources,
            )
        )
        self.assertFalse(
            MODULE.consulted_source_match(
                "https://different.example/paper",
                "",
                sources,
            )
        )

    def test_source_support_metrics_count_bracketed_sources(self):
        with tempfile.TemporaryDirectory() as directory:
            run_dir = Path(directory)
            task_dir = run_dir / "systems" / "bge_llm_local_rag" / "RT01"
            task_dir.mkdir(parents=True)
            (task_dir / "sources.json").write_text(
                json.dumps(
                    {
                        "sources": [
                            {
                                "source_id": "S01",
                                "publication_status": (
                                    "peer_reviewed_or_formally_published"
                                ),
                                "doi_or_stable_url": "https://doi.org/10.1/a",
                            },
                            {
                                "source_id": "S02",
                                "publication_status": (
                                    "corpus_record_status_unresolved"
                                ),
                                "doi_or_stable_url": "corpus://paper.pdf",
                            },
                            {
                                "source_id": "S03",
                                "publication_status": "peer_reviewed",
                                "doi_or_stable_url": "https://doi.org/10.1/c",
                            },
                        ]
                    }
                )
            )
            (task_dir / "professional_review.md").write_text(
                "Supported result [S01]. Another result [S02]."
            )
            call_dir = (
                run_dir
                / "calls"
                / "bge_llm_local_rag"
                / "RT01"
            )
            call_dir.mkdir(parents=True)
            (call_dir / "review_source_support.json").write_text(
                json.dumps(
                    {
                        "result": {
                            "claim_assessments": [
                                {
                                    "status": "supported",
                                    "cited_source_ids": ["S01"],
                                },
                                {
                                    "status": "partially_supported",
                                    "cited_source_ids": ["S02-E01"],
                                },
                            ],
                            "anchor_exclusion_violation": False,
                        }
                    }
                )
            )
            metrics = MODULE.source_support_metrics(
                run_dir,
                "RT01",
                "bge_llm_local_rag",
            )
            self.assertEqual(metrics["citation_marker_count"], 2)
            self.assertEqual(metrics["unique_cited_sources"], 2)
            self.assertEqual(metrics["claim_citation_coverage_rate"], 1.0)
            self.assertEqual(metrics["unverifiable_citation_rate"], 0.0)
            self.assertEqual(
                metrics[
                    "peer_reviewed_primary_source_fraction_among_cited_sources"
                ],
                0.5,
            )
            self.assertEqual(
                metrics["valid_identifier_fraction_among_cited_sources"],
                1.0,
            )

    def test_extraction_accuracy_uses_support_status(self):
        with tempfile.TemporaryDirectory() as directory:
            run_dir = Path(directory)
            task_dir = run_dir / "systems" / "bge_llm_local_rag" / "RT01"
            task_dir.mkdir(parents=True)
            (task_dir / "extracted_records.json").write_text(
                json.dumps(
                    {
                        "records": [{"record_id": "R1"}],
                        "deterministic_preverification_rejections": [],
                        "deterministic_field_rejections": [],
                        "deterministic_field_normalizations": [],
                    }
                )
            )
            (task_dir / "verified_records.json").write_text(
                json.dumps(
                    {
                        "verified_records": [
                            {"record": {"source_id": "S01"}}
                        ],
                        "all_verifications": [
                            {
                                "field_assessments": [
                                    {
                                        "field_path": (
                                            "quantitative_findings[0].value"
                                        ),
                                        "status": "supported",
                                        "error_type": "numeric_transcription",
                                    },
                                    {
                                        "field_path": (
                                            "quantitative_findings[0].unit"
                                        ),
                                        "status": "partially_supported",
                                        "error_type": "unit",
                                    },
                                    {
                                        "field_path": (
                                            "operating_conditions[0].value"
                                        ),
                                        "status": "supported",
                                        "error_type": "none",
                                    },
                                    {
                                        "field_path": (
                                            "endpoints[0].endpoint_type"
                                        ),
                                        "status": "supported",
                                        "error_type": (
                                            "endpoint_classification"
                                        ),
                                    },
                                    {
                                        "field_path": "comparability.status",
                                        "status": "supported",
                                        "error_type": "other",
                                    },
                                ],
                                "anchor_exclusion_violation": False,
                            }
                        ],
                    }
                )
            )
            metrics = MODULE.extraction_metrics(
                run_dir,
                "RT01",
                "bge_llm_local_rag",
            )
            self.assertEqual(metrics["numeric_transcription_accuracy"], 0.5)
            self.assertEqual(
                metrics["endpoint_classification_accuracy"],
                1.0,
            )
            self.assertEqual(metrics["comparability_field_accuracy"], 1.0)

    def test_source_support_metrics_recognize_legacy_locator_ids(self):
        with tempfile.TemporaryDirectory() as directory:
            run_dir = Path(directory)
            task_dir = (
                run_dir / "systems" / "gpt51_web_search" / "RT09"
            )
            task_dir.mkdir(parents=True)
            (task_dir / "sources.json").write_text(
                json.dumps(
                    {
                        "sources": [
                            {
                                "source_id": "WEB01",
                                "publication_status": "peer_reviewed",
                                "doi_or_stable_url": (
                                    "https://doi.org/10.1/example"
                                ),
                            }
                        ]
                    }
                )
            )
            (task_dir / "professional_review.md").write_text(
                "Legacy locator citation WEB01-E03."
            )
            call_dir = (
                run_dir
                / "calls"
                / "gpt51_web_search"
                / "RT09"
            )
            call_dir.mkdir(parents=True)
            (call_dir / "review_source_support.json").write_text(
                json.dumps(
                    {
                        "result": {
                            "claim_assessments": [],
                            "anchor_exclusion_violation": False,
                        }
                    }
                )
            )
            metrics = MODULE.source_support_metrics(
                run_dir,
                "RT09",
                "gpt51_web_search",
            )
            self.assertEqual(metrics["citation_marker_count"], 1)
            self.assertEqual(metrics["unique_cited_sources"], 1)


if __name__ == "__main__":
    unittest.main()

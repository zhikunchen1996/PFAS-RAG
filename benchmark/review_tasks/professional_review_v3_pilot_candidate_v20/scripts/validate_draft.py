#!/usr/bin/env python3
"""Validate the extraction-first professional-review draft without paid calls."""

from __future__ import annotations

import csv
import importlib.util
import json
from pathlib import Path
import re

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parents[2]


def load_json(path: Path):
    return json.loads(path.read_text())


def load_jsonl(path: Path):
    records = []
    for line_number, line in enumerate(path.read_text().splitlines(), start=1):
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise AssertionError(f"{path}:{line_number}: invalid JSON") from exc
    return records


def load_anchor_filter_module():
    path = ROOT / "scripts" / "filter_anchor_reviews.py"
    spec = importlib.util.spec_from_file_location("filter_anchor_reviews", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def validate_anchor_metadata(tasks: list[dict], anchors: list[dict]) -> None:
    assert [record["task_id"] for record in anchors] == [
        task["task_id"] for task in tasks
    ]

    manifest_path = (
        PROJECT_ROOT / "corpus" / "corpus434_repaired_v1" / "raw_manifest.csv"
    )
    with manifest_path.open(encoding="utf-8-sig", newline="") as stream:
        manifest = list(csv.DictReader(stream))
    manifest_by_source = {row["source"]: row for row in manifest}

    anchor_definitions = {}
    present_count = 0
    for task_record in anchors:
        assert (
            task_record["provenance_status"]
            == "literature_derived_shared_anchor_bottom_up_v3"
        )
        assert task_record["supplemental_anchors"] == []
        task_anchors = [
            task_record["primary_anchor"],
            *task_record["supplemental_anchors"],
        ]
        assert task_anchors
        for anchor in task_anchors:
            assert anchor["anchor_id"]
            assert anchor["title"]
            assert anchor["doi"].startswith("10.")
            assert anchor["url"].startswith("https://doi.org/")
            assert anchor["scope_role"]
            stable_definition = {
                key: anchor.get(key)
                for key in (
                    "title",
                    "year",
                    "doi",
                    "url",
                    "alternate_dois",
                    "alternate_urls",
                    "corpus_presence",
                )
            }
            previous = anchor_definitions.setdefault(
                anchor["anchor_id"], stable_definition
            )
            assert previous == stable_definition

            if anchor["corpus_presence"] == "present":
                present_count += 1
                source = anchor["corpus_source"]
                assert source in manifest_by_source
                assert manifest_by_source[source]["doi"].lower() == anchor["doi"].lower()
            else:
                assert anchor["corpus_presence"] == "absent"
                assert anchor["corpus_source"] is None

    assert present_count == 10
    assert len(anchor_definitions) == 5


def validate_design_provenance(
    tasks: list[dict],
    anchors: list[dict],
    provenance: list[dict],
) -> None:
    task_ids = [task["task_id"] for task in tasks]
    assert [record["task_id"] for record in provenance] == task_ids
    anchor_by_task = {
        record["task_id"]: record["primary_anchor"] for record in anchors
    }

    answer_bearing_number = re.compile(
        r"\b\d+(?:\.\d+)?\s*(?:%|mg|ug|ng|kwh|v|ma|mpa)\b",
        re.IGNORECASE,
    )
    for task, record in zip(tasks, provenance, strict=True):
        assert (
            record["origin_type"]
            == "literature_derived_shared_anchor_bottom_up"
        )
        anchor = anchor_by_task[task["task_id"]]
        assert record["anchor_id"] == anchor["anchor_id"]
        snapshot_path = ROOT / record["source_snapshot"]
        assert snapshot_path.exists()
        snapshot = load_json(snapshot_path)
        assert snapshot["source"] == anchor["corpus_source"]
        assert snapshot["doi"].lower() == anchor["doi"].lower()

        available_indices = {
            item["chunk_index"] for item in snapshot["selected_chunks"]
        }
        for key in (
            "scope_chunks",
            "comparison_chunks",
            "engineering_chunks",
            "gap_chunks",
        ):
            indices = record["design_basis"][key]
            assert indices
            assert set(indices) <= available_indices

        visible_text = " ".join(
            [
                task["title"],
                task["review_brief"],
                *(component["requirement"] for component in task["components"]),
            ]
        )
        assert anchor["title"].casefold() not in visible_text.casefold()
        assert not answer_bearing_number.search(visible_text)
        assert record["derivation_summary"]
        assert record["answer_leakage_control"]


def validate_coverage_pilot(task_ids: list[str]) -> None:
    pilot = ROOT / "coverage_pilot"
    summary_path = pilot / "coverage_summary.csv"
    detail_path = pilot / "coverage_details.jsonl"
    manifest_path = pilot / "run_manifest.json"
    assert summary_path.exists()
    assert detail_path.exists()
    assert manifest_path.exists()

    with summary_path.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    assert [row["task_id"] for row in rows] == task_ids
    for row in rows:
        assert int(row["anchor_chunks_in_corpus"]) > 0
        assert int(row["anchor_query_hits_after_filter"]) == 0
        assert int(row["query_coverage_top20"]) == int(row["query_count"]) == 4
        assert int(row["likely_primary_documents_top20"]) >= 10

    details = load_jsonl(detail_path)
    assert [record["task_id"] for record in details] == task_ids
    for record in details:
        assert record["anchor_chunks_in_corpus"] > 0
        assert record["anchor_query_hits_after_filter"] == 0
        assert len(record["queries_with_likely_primary_top20"]) == 4

    manifest = load_json(manifest_path)
    assert manifest["status"] == "coverage_only_no_paid_calls"
    assert manifest["candidate_reviews_or_scores_viewed"] is False


def validate_prompts() -> None:
    required_placeholders = {
        "local_evidence_extraction_user.txt": {
            "{{REVIEW_TASK}}",
            "{{DATA_EXTRACTION_OBJECTIVE}}",
            "{{SOURCE_SYSTEM}}",
            "{{SOURCE_ID}}",
            "{{ANCHOR_EXCLUSIONS}}",
            "{{SOURCE_DOCUMENTS_AND_CHUNKS}}",
        },
        "web_evidence_extraction_user.txt": {
            "{{REVIEW_TASK}}",
            "{{DATA_EXTRACTION_OBJECTIVE}}",
            "{{SOURCE_SYSTEM}}",
            "{{SOURCE_ID}}",
            "{{ANCHOR_EXCLUSIONS}}",
            "{{INSPECTED_WEB_SOURCES}}",
        },
        "review_synthesis_user.txt": {
            "{{REVIEW_BRIEF}}",
            "{{REQUIRED_COMPONENTS}}",
            "{{TASK_BOUNDARIES}}",
            "{{ANCHOR_EXCLUSIONS}}",
            "{{VERIFIED_EVIDENCE_TABLE}}",
            "{{VERIFIED_SUPPORTING_EXCERPTS}}",
        },
        "direct_review_synthesis_user.txt": {
            "{{REVIEW_BRIEF}}",
            "{{REQUIRED_COMPONENTS}}",
            "{{TASK_BOUNDARIES}}",
            "{{ANCHOR_EXCLUSIONS}}",
        },
        "document_selector_user.txt": {
            "{{REVIEW_TASK}}",
            "{{REQUIRED_COMPONENTS}}",
            "{{TASK_BOUNDARIES}}",
            "{{CANDIDATE_SCREEN_BUDGET}}",
            "{{MINIMUM_RETAINED_SOURCES}}",
            "{{DOCUMENT_CARDS}}",
        },
        "web_source_discovery_user.txt": {
            "{{REVIEW_TASK}}",
            "{{REQUIRED_COMPONENTS}}",
            "{{DATA_EXTRACTION_OBJECTIVE}}",
            "{{ANCHOR_EXCLUSIONS}}",
            "{{CANDIDATE_SOURCE_BUDGET}}",
            "{{MINIMUM_RETAINED_SOURCES}}",
        },
        "extraction_verification_user.txt": {
            "{{REVIEW_TASK}}",
            "{{DATA_EXTRACTION_OBJECTIVE}}",
            "{{ANCHOR_EXCLUSIONS}}",
            "{{EVIDENCE_RECORD}}",
            "{{CITED_SOURCE_EVIDENCE}}",
        },
        "extraction_verification_completion_user.txt": {
            "{{REVIEW_TASK}}",
            "{{DATA_EXTRACTION_OBJECTIVE}}",
            "{{ANCHOR_EXCLUSIONS}}",
            "{{EVIDENCE_RECORD}}",
            "{{CITED_SOURCE_EVIDENCE}}",
            "{{MISSING_REQUIRED_FIELD_PATHS}}",
        },
        "review_source_support_user.txt": {
            "{{REVIEW_TASK}}",
            "{{CANDIDATE_REVIEW}}",
            "{{VERIFIED_EVIDENCE_TABLE}}",
            "{{VERIFIED_SUPPORTING_EXCERPTS}}",
            "{{ANCHOR_EXCLUSIONS}}",
        },
        "common_review_judge_user.txt": {
            "{{REVIEW_TASK}}",
            "{{REQUIRED_COMPONENTS}}",
            "{{TASK_LEDGER}}",
            "{{CANDIDATE_REVIEW}}",
        },
    }
    for filename, placeholders in required_placeholders.items():
        text = (ROOT / "prompts" / filename).read_text()
        assert placeholders <= {token for token in placeholders if token in text}

    extraction_system = (
        ROOT / "prompts" / "shared_evidence_extraction_system.txt"
    ).read_text()
    extraction_system_flat = " ".join(extraction_system.split())
    assert "one record per primary-study experiment" in extraction_system
    assert (
        "must not be used as the source of a quantitative study record"
        in extraction_system_flat
    )
    assert "held out" in extraction_system

    synthesis_system = (
        ROOT / "prompts" / "shared_review_synthesis_system.txt"
    ).read_text()
    synthesis_system_flat = " ".join(synthesis_system.split())
    assert "verified structured study evidence table" in synthesis_system_flat
    assert "Do not introduce" in synthesis_system
    completion_system = (
        ROOT
        / "prompts"
        / "extraction_verification_completion_judge.txt"
    ).read_text()
    assert "exactly the field paths" in completion_system
    assert "cannot override a prior exclusion" in completion_system
    source_support_system = (
        ROOT / "prompts" / "review_source_support_judge.txt"
    ).read_text()
    assert "including claims with no citation" in source_support_system
    assert "unsupported for traceability" in source_support_system
    review_judge_system = (
        ROOT / "prompts" / "common_review_judge.txt"
    ).read_text()
    assert "Meaningful evidence breadth may earn credit" in review_judge_system
    assert "multiple sources materially support" in review_judge_system

    obsolete = {
        "local_rag_review_user.txt",
        "shared_review_system.txt",
        "web_search_review_user.txt",
    }
    assert not any((ROOT / "prompts" / filename).exists() for filename in obsolete)


def main() -> None:
    protocol = load_json(ROOT / "protocol.json")
    tasks = load_jsonl(ROOT / "input" / "review_tasks.jsonl")
    ledgers = load_jsonl(ROOT / "input" / "review_task_ledgers.jsonl")
    anchors = load_jsonl(ROOT / "input" / "anchor_reviews.jsonl")
    provenance = load_jsonl(
        ROOT / "provenance" / "task_design_provenance.jsonl"
    )

    assert (
        protocol["protocol_id"]
        == "professional_pfas_review_v3_pilot_candidate_v20"
    )
    assert protocol["status"] == "rt01_retrospective_calibration_candidate"
    assert protocol["execution_safety"]["paid_calls_authorized"] is True
    assert protocol["execution_safety"]["authorized_task_ids"] == ["RT01"]
    assert protocol["execution_safety"]["authorized_stages"] == [
        "source_support",
        "review_judge",
        "summary",
    ]
    assert protocol["systems"] == [
        "bge_llm_local_rag",
        "gpt51_web_search",
        "gpt51_direct",
    ]
    assert protocol["end_to_end_review_evaluation"][
        "layer_a_evidence_acquisition_and_extraction"
    ]["applicable_systems"] == [
        "bge_llm_local_rag",
        "gpt51_web_search",
    ]
    assert (
        protocol["execution_safety"]["formal_ten_task_run_authorized"]
        is False
    )
    assert len(tasks) == protocol["tasks"]["planned_count"] == 10
    assert len(ledgers) == len(tasks)
    assert protocol["task_design"]["unique_anchor_review_count"] == 5
    assert protocol["tasks"]["unique_primary_anchor_review_count"] == 5

    task_ids = [task["task_id"] for task in tasks]
    ledger_ids = [ledger["task_id"] for ledger in ledgers]
    assert len(set(task_ids)) == len(task_ids)
    assert task_ids == ledger_ids

    for task, ledger in zip(tasks, ledgers, strict=True):
        components = task["components"]
        assert len(components) == protocol["tasks"]["components_per_task"] == 3
        component_ids = [component["component_id"] for component in components]
        assert len(set(component_ids)) == len(component_ids)
        assert ledger["required_component_ids"] == component_ids
        assert len(ledger["constraints"]) == 2
        assert task["data_extraction_objective"]
        assert task["deliverables"] == protocol["tasks"]["required_deliverables"]

    validate_anchor_metadata(tasks, anchors)
    validate_design_provenance(tasks, anchors, provenance)
    validate_coverage_pilot(task_ids)
    validate_prompts()

    for schema_name in (
        "document_selection.schema.json",
        "evidence_table.schema.json",
        "extraction_verification.schema.json",
        "review_judgment.schema.json",
        "review_source_support.schema.json",
        "web_source_packet.schema.json",
    ):
        Draft202012Validator.check_schema(
            load_json(ROOT / "schemas" / schema_name)
        )

    weights = protocol["common_review_judge"]["dimensions"]
    assert abs(sum(weights.values()) - 1.0) < 1e-12
    assert protocol["common_review_judge"]["repeat_count"] == 3
    assert protocol["common_review_judge"]["bootstrap"] is False
    assert protocol["common_review_judge"]["binary_threshold"] is None
    assert protocol["common_review_judge"]["status_values"] == {
        "full": 1.0,
        "partial": 0.5,
        "absent": 0.0,
        "contradicted": 0.0,
    }
    assert protocol["common_review_judge"]["judgment_structure"] == (
        "three component-fulfillment assessments plus fourteen global "
        "atomic review operations"
    )
    assert sum(
        len(operations)
        for operations in protocol["common_review_judge"][
            "atomic_operations"
        ].values()
    ) == 14
    end_to_end = protocol["end_to_end_review_evaluation"]
    assert end_to_end["aggregation"] == (
        "two co-primary layers; no weighted composite"
    )
    assert "verified_usable_record_count" in (
        end_to_end["layer_a_evidence_acquisition_and_extraction"]
        ["primary_metrics"]
    )
    layer_a_primary = end_to_end[
        "layer_a_evidence_acquisition_and_extraction"
    ]["primary_metrics"]
    assert "verified_unique_source_count" in layer_a_primary
    assert "claim_citation_coverage_rate" in layer_a_primary
    assert "unique_cited_sources" in layer_a_primary
    assert end_to_end["layer_b_citation_aware_synthesis"][
        "citation_integration_scored"
    ] is True
    retrieval = protocol["retrieval_and_extraction"]
    assert retrieval["query_chunk_budget"] == 100
    assert retrieval["local_candidate_screen_budget"] == 20
    assert retrieval["minimum_retained_sources"] == 6
    assert retrieval["within_document_chunk_budget"] == 8
    assert retrieval["web_search_candidate_screen_budget"] == 20
    assert retrieval["fixed_final_source_count"] is None
    assert (
        protocol["generation"]["synthesis_input_projection"]
        == "all verified records plus compact field statuses and reasons only "
        "for non-supported fields; supporting excerpts remain complete"
    )
    assert protocol["generation"]["synthesis_internal_ids_visible"] is False
    assert (
        protocol["generation"]["synthesis_retrieval_metadata_visible"]
        is False
    )
    assert (
        protocol["separate_source_diagnostics"][
            "uses_common_compact_evidence_view"
        ]
        is True
    )
    assert protocol["generation"]["record_citation_normalization"] == (
        "inside bracket citations only, convert exact <source>-R## record "
        "IDs to their source ID, deduplicate, and log every replacement"
    )
    assert "carbon-fate evidence" in retrieval["endpoint_measurement_rule"]
    quantitative_schema = load_json(
        ROOT / "schemas" / "evidence_table.schema.json"
    )["$defs"]["quantitativeValue"]
    assert "value_form" in quantitative_schema["required"]
    assert set(
        quantitative_schema["properties"]["value_form"]["enum"]
    ) == {
        "exact_numeric",
        "approximate_numeric",
        "inequality",
        "range",
        "not_detected",
    }
    assert protocol["generation"]["reasoning_effort"] == "low"
    assert (
        protocol["generation"]["technical_output_token_ceilings"][
            "per_record_verification"
        ]
        == 12000
    )
    assert (
        protocol["generation"]["technical_output_token_ceilings"][
            "per_source_extraction"
        ]
        == 16000
    )
    assert (
        protocol["generation"]["technical_output_token_ceilings"][
            "review_quality_judge"
        ]
        == 20000
    )
    assert (
        protocol["generation"]["extraction_model_snapshot"]
        == "gpt-5.1-2025-11-13"
    )

    filter_module = load_anchor_filter_module()
    for task_id in task_ids:
        identifiers = filter_module.task_anchor_identifiers(anchors, task_id)
        assert identifiers["dois"]
        assert identifiers["titles"]

    print(
        "PASS: literature-derived extraction-first V3 pilot candidate V20 "
        "has 10 focused "
        "tasks derived from 5 shared full-text anchor reviews, full-text "
        "design provenance, task-scoped anchor exclusions, aligned ledgers, "
        "valid schemas, matched extraction/synthesis prompts, and a "
        "retrospectively redesigned atomic Layer B judge with paid calls "
        "restricted to RT01 source-support and review-judge calibration."
    )


if __name__ == "__main__":
    main()

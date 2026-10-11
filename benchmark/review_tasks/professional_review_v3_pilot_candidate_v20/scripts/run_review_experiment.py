#!/usr/bin/env python3
"""Run the resumable professional-review pilot or formal experiment."""

from __future__ import annotations

import argparse
import copy
import csv
import json
import re
import statistics
import sys
import time
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Callable, Iterable
from urllib.parse import urlsplit, urlunsplit

from filter_anchor_reviews import (
    exclusion_reason,
    normalize_doi,
    normalize_title,
    normalize_url,
    task_anchor_identifiers,
)
from review_retrieval import (
    CHUNKS_PER_DOCUMENT,
    DOCUMENT_BUDGET,
    LLM_SELECTOR_POOL,
    MIN_RETAINED_SOURCES,
    LocalReviewRetriever,
    selector_cards,
)
from review_runtime import (
    DEFAULT_REASONING_EFFORT,
    MODEL_ALIAS,
    MODEL_SNAPSHOT,
    PACKAGE_ROOT,
    ResumableOpenAI,
    canonical_json,
    collect_call_records,
    load_json,
    load_jsonl,
    render_template,
    sha256_file,
    sha256_text,
    utc_now,
    write_json,
)
from score_review_judgments import DIMENSION_WEIGHTS, score_judgment


ALL_SYSTEMS = (
    "bge_llm_local_rag",
    "gpt51_web_search",
    "gpt51_direct",
)
LOCAL_SYSTEMS = {"bge_llm_local_rag"}
DIRECT_SYSTEMS = {"gpt51_direct"}
EVIDENCE_SYSTEMS = set(ALL_SYSTEMS) - DIRECT_SYSTEMS
ALL_STAGES = (
    "retrieval",
    "extraction",
    "verification",
    "synthesis",
    "source_support",
    "review_judge",
    "summary",
)
MIN_WEB_SOURCES = MIN_RETAINED_SOURCES
WEB_CANDIDATE_BUDGET = DOCUMENT_BUDGET
JUDGE_REPEATS = 3
CITATION_PATTERN = re.compile(r"\[([A-Z]{1,5}[0-9]{2})\]")
SOURCE_OR_LOCATOR_PATTERN = re.compile(
    r"\b((?:S|WEB)[0-9]{2})(?:-E[0-9]{2})?\b"
)
BRACKET_PATTERN = re.compile(r"\[([^\[\]]+)\]")
RECORD_CITATION_PATTERN = re.compile(
    r"\b((?:S|WEB)[0-9]{2})-R[0-9]{2}\b"
)
VALID_SOURCE_OR_LOCATOR_TOKEN = re.compile(
    r"^(?:S|WEB)[0-9]{2}(?:-E[0-9]{2})?$"
)
LAYER_B_SOURCE_TOKEN_PATTERN = re.compile(
    r"\b(?P<source>(?:S|WEB)[0-9]{2})(?:-(?:E|R)[0-9]{2})?\b"
)
INTEGER_PATTERN = r"(?:\d{1,3}(?:,\d{3})+|\d+)"
NUMBER_PATTERN = (
    rf"[+-]?(?:{INTEGER_PATTERN}(?:\.\d*)?|\.\d+)"
    r"(?:[eE][+-]?\d+)?"
)
BARE_NUMBER_PATTERN = re.compile(rf"^{NUMBER_PATTERN}$")
QUANTITATIVE_VALUE_PATTERNS = {
    "exact_numeric": re.compile(rf"^{NUMBER_PATTERN}$"),
    "approximate_numeric": re.compile(rf"^~\s*{NUMBER_PATTERN}$"),
    "inequality": re.compile(rf"^(?:<=|>=|<|>)\s*{NUMBER_PATTERN}$"),
    "range": re.compile(
        rf"^{NUMBER_PATTERN}\s*(?:-|to)\s*{NUMBER_PATTERN}$"
    ),
}
NOT_DETECTED_VALUES = {
    "nd",
    "n/d",
    "not detected",
    "below detection limit",
    "below quantification limit",
}
INTERNAL_LABEL_TOKEN_PATTERN = re.compile(
    r"\bRT\d{2}[\-\u2010-\u2015]?[BC]\d+\b",
    flags=re.IGNORECASE,
)
INTERNAL_LABEL_PARENTHETICAL_PATTERN = re.compile(
    r"\s*\((?:"
    r"(?:to\s+comply\s+with\s+)?RT\d{2}[\-\u2010-\u2015]?[BC]\d+"
    r"|Component\s+RT\d{2}[\-\u2010-\u2015]?[BC]\d+"
    r"|[BC]\d+"
    r"|Component\s+\d+"
    r")\)",
    flags=re.IGNORECASE,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--task-ids", nargs="+")
    parser.add_argument(
        "--systems",
        nargs="+",
        choices=ALL_SYSTEMS,
        default=list(ALL_SYSTEMS),
    )
    parser.add_argument(
        "--stages",
        nargs="+",
        choices=ALL_STAGES,
        default=list(ALL_STAGES),
    )
    parser.add_argument("--allow-paid", action="store_true")
    parser.add_argument("--device", default="auto")
    parser.add_argument("--bge-batch-size", type=int, default=16)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--judge-repeats", type=int, default=JUDGE_REPEATS)
    return parser.parse_args()


def by_id(records: list[dict[str, Any]], key: str) -> dict[str, dict[str, Any]]:
    result = {str(record[key]): record for record in records}
    if len(result) != len(records):
        raise RuntimeError(f"Duplicate {key} values")
    return result


def selected_inputs(
    task_ids: list[str] | None,
) -> tuple[
    list[dict[str, Any]],
    dict[str, dict[str, Any]],
    list[dict[str, Any]],
]:
    tasks = load_jsonl(PACKAGE_ROOT / "input" / "review_tasks.jsonl")
    ledgers = by_id(
        load_jsonl(PACKAGE_ROOT / "input" / "review_task_ledgers.jsonl"),
        "task_id",
    )
    anchors = load_jsonl(PACKAGE_ROOT / "input" / "anchor_reviews.jsonl")
    anchor_map = by_id(anchors, "task_id")
    expected = [f"RT{index:02d}" for index in range(1, 11)]
    if [task["task_id"] for task in tasks] != expected:
        raise RuntimeError("Review tasks must be ordered RT01 through RT10")
    requested = task_ids or expected
    unknown = set(requested) - set(expected)
    if unknown:
        raise ValueError(f"Unknown task ids: {sorted(unknown)}")
    chosen = [task for task in tasks if task["task_id"] in set(requested)]
    if len(chosen) != len(set(requested)):
        raise RuntimeError("Requested task ids are duplicated")
    for task in chosen:
        task_id = str(task["task_id"])
        if task_id not in ledgers or task_id not in anchor_map:
            raise RuntimeError(f"{task_id}: missing ledger or anchor")
    return chosen, ledgers, anchors


def enforce_paid_task_authorization(
    *,
    protocol: dict[str, Any],
    task_ids: Iterable[str],
    stages: Iterable[str],
    allow_paid: bool,
) -> None:
    if not allow_paid:
        return
    safety = protocol["execution_safety"]
    if safety.get("paid_calls_authorized") is not True:
        raise RuntimeError("Paid calls are disabled for this package")
    if safety.get("formal_ten_task_run_authorized") is True:
        return
    authorized = {
        str(task_id) for task_id in safety.get("authorized_task_ids", [])
    }
    requested = {str(task_id) for task_id in task_ids}
    if not requested or not requested.issubset(authorized):
        raise RuntimeError(
            "Paid task authorization failed: requested "
            f"{sorted(requested)}, authorized {sorted(authorized)}"
        )
    authorized_stages = {
        str(stage) for stage in safety.get("authorized_stages", [])
    }
    requested_stages = {str(stage) for stage in stages}
    if not requested_stages or not requested_stages.issubset(
        authorized_stages
    ):
        raise RuntimeError(
            "Paid stage authorization failed: requested "
            f"{sorted(requested_stages)}, authorized "
            f"{sorted(authorized_stages)}"
        )


def task_text(task: dict[str, Any]) -> str:
    return canonical_json(
        {
            "task_id": task["task_id"],
            "title": task["title"],
            "review_brief": task["review_brief"],
        }
    )


def component_text(task: dict[str, Any]) -> str:
    return canonical_json(task["components"])


def synthesis_component_text(task: dict[str, Any]) -> str:
    return canonical_json(
        [
            {"requirement": component["requirement"]}
            for component in task["components"]
        ]
    )


def synthesis_boundary_text(ledger: dict[str, Any]) -> str:
    return canonical_json(
        {
            "task_boundaries": ledger["task_boundaries"],
            "constraints": [
                {
                    "material_violation_rule": constraint[
                        "material_violation_rule"
                    ]
                }
                for constraint in ledger["constraints"]
            ],
        }
    )


def anchor_text(
    task_id: str,
    anchors: list[dict[str, Any]],
) -> str:
    record = next(item for item in anchors if item["task_id"] == task_id)
    anchor = record["primary_anchor"]
    identifiers = task_anchor_identifiers(anchors, task_id)
    return canonical_json(
        {
            "anchor_id": anchor["anchor_id"],
            "title": anchor["title"],
            "doi": anchor["doi"],
            "url": anchor["url"],
            "corpus_source": anchor["corpus_source"],
            "all_blocked_dois": sorted(identifiers["dois"]),
            "all_blocked_urls": sorted(identifiers["urls"]),
            "all_blocked_titles": sorted(identifiers["titles"]),
        }
    )


def prompt(path: str) -> Path:
    return PACKAGE_ROOT / "prompts" / path


def schema(path: str) -> dict[str, Any]:
    return load_json(PACKAGE_ROOT / "schemas" / path)


def extraction_schema_for_source(
    base_schema: dict[str, Any],
    *,
    task_id: str,
    system: str,
    source_id: str,
    locator_ids: Iterable[str],
) -> dict[str, Any]:
    constrained = copy.deepcopy(base_schema)
    constrained["properties"]["task_id"]["enum"] = [task_id]
    constrained["properties"]["source_system"]["enum"] = [system]
    constrained["$defs"]["evidenceRecord"]["properties"]["source_id"][
        "enum"
    ] = [source_id]
    allowed = sorted(set(locator_ids))
    if not allowed:
        raise ValueError(f"{task_id}/{system}/{source_id}: no locator ids")

    def constrain(value: Any) -> None:
        if isinstance(value, dict):
            properties = value.get("properties")
            if (
                isinstance(properties, dict)
                and "evidence_locator_ids" in properties
            ):
                locator_schema = properties["evidence_locator_ids"]
                locator_schema["items"] = {
                    "type": "string",
                    "enum": allowed,
                }
            for child in value.values():
                constrain(child)
        elif isinstance(value, list):
            for child in value:
                constrain(child)

    constrain(constrained)
    return constrained


def safe_url_without_query(value: str) -> str:
    parsed = urlsplit(value)
    return urlunsplit(
        parsed._replace(query="", fragment="")
    ).casefold().rstrip("/")


def consulted_source_match(
    inspected_url: str,
    doi: str,
    consulted_sources: list[dict[str, str]],
) -> bool:
    target_url = normalize_url(inspected_url)
    target_base = safe_url_without_query(target_url)
    target_doi = normalize_doi(doi) or normalize_doi(inspected_url)
    for source in consulted_sources:
        source_url = str(source.get("url") or "")
        if normalize_url(source_url) == target_url:
            return True
        if safe_url_without_query(normalize_url(source_url)) == target_base:
            return True
        source_doi = normalize_doi(source_url)
        if target_doi and source_doi == target_doi:
            return True
    return False


def all_locator_ids(record: dict[str, Any]) -> set[str]:
    found: set[str] = set()

    def visit(value: Any, key: str = "") -> None:
        if key == "evidence_locator_ids" and isinstance(value, list):
            found.update(str(item) for item in value)
            return
        if isinstance(value, dict):
            for child_key, child in value.items():
                visit(child, child_key)
        elif isinstance(value, list):
            for child in value:
                visit(child, key)

    visit(record)
    return found


def quantitative_value_is_valid(finding: dict[str, Any]) -> bool:
    value = str(finding.get("value") or "").strip()
    value_form = str(finding.get("value_form") or "")
    if value_form == "not_detected":
        return value.casefold() in NOT_DETECTED_VALUES
    pattern = QUANTITATIVE_VALUE_PATTERNS.get(value_form)
    return bool(pattern and pattern.fullmatch(value))


def normalize_quantitative_finding(
    finding: dict[str, Any],
) -> tuple[dict[str, Any] | None, str | None]:
    if quantitative_value_is_valid(finding):
        return dict(finding), None
    value = str(finding.get("value") or "").strip()
    if (
        finding.get("value_form") == "approximate_numeric"
        and BARE_NUMBER_PATTERN.fullmatch(value)
    ):
        normalized = dict(finding)
        normalized["value"] = f"~{value}"
        return normalized, "added_declared_approximation_marker"
    return None, None


def sanitize_internal_review_notation(
    text: str,
) -> tuple[str, list[str]]:
    removed: list[str] = []

    def remove(match: re.Match[str]) -> str:
        removed.append(match.group(0).strip())
        return ""

    cleaned = INTERNAL_LABEL_PARENTHETICAL_PATTERN.sub(remove, text)
    if INTERNAL_LABEL_TOKEN_PATTERN.search(cleaned):
        raise RuntimeError(
            "Review contains an internal task/component/boundary label "
            "outside a removable parenthetical"
        )
    return cleaned, removed


def normalize_record_citation_ids(
    text: str,
) -> tuple[str, list[dict[str, str]]]:
    changes: list[dict[str, str]] = []

    def replace_bracket(match: re.Match[str]) -> str:
        original = match.group(0)
        content = match.group(1)
        if not RECORD_CITATION_PATTERN.search(content):
            return original
        normalized = RECORD_CITATION_PATTERN.sub(r"\1", content)
        tokens = [
            token.strip()
            for token in re.split(r"[,;]", normalized)
            if token.strip()
        ]
        if tokens and all(
            VALID_SOURCE_OR_LOCATOR_TOKEN.fullmatch(token)
            for token in tokens
        ):
            tokens = list(dict.fromkeys(tokens))
            replacement = f"[{', '.join(tokens)}]"
        else:
            replacement = f"[{normalized}]"
        changes.append(
            {"original": original, "replacement": replacement}
        )
        return replacement

    return BRACKET_PATTERN.sub(replace_bracket, text), changes


def prepare_anonymous_citation_aware_layer_b_review(
    text: str,
) -> tuple[str, dict[str, Any]]:
    """Neutralize system-specific source IDs while preserving citation use."""
    source_map: dict[str, str] = {}
    replacement_count = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal replacement_count
        source = match.group("source")
        if source not in source_map:
            source_map[source] = f"R{len(source_map) + 1:02d}"
        replacement_count += 1
        return source_map[source]

    normalized = LAYER_B_SOURCE_TOKEN_PATTERN.sub(replace, text)
    normalized = normalized.strip() + "\n"
    surviving_token = LAYER_B_SOURCE_TOKEN_PATTERN.search(normalized)
    if surviving_token:
        raise RuntimeError(
            "Layer B citation anonymization failed: source identifier "
            f"survived: {surviving_token.group(0)}"
        )
    return normalized, {
        "method": "deterministic_source_id_anonymization_v1",
        "source_id_mapping": source_map,
        "replacement_count": replacement_count,
        "unique_cited_source_count": len(source_map),
        "original_sha256": sha256_text(text),
        "anonymized_sha256": sha256_text(normalized),
    }


def is_numeric_value_or_unit_assessment(
    assessment: dict[str, Any],
) -> bool:
    return bool(
        re.search(
            r"^(?:quantitative_findings|operating_conditions)"
            r"\[\d+\]\.(?:value|unit)$",
            str(assessment.get("field_path") or ""),
        )
    )


def is_quantitative_value_or_unit_assessment(
    assessment: dict[str, Any],
) -> bool:
    return bool(
        re.fullmatch(
            r"quantitative_findings\[\d+\]\.(?:value|unit)",
            str(assessment.get("field_path") or ""),
        )
    )


def is_endpoint_type_assessment(assessment: dict[str, Any]) -> bool:
    return bool(
        re.fullmatch(
            r"endpoints\[\d+\]\.endpoint_type",
            str(assessment.get("field_path") or ""),
        )
    )


def is_comparability_status_assessment(
    assessment: dict[str, Any],
) -> bool:
    return str(assessment.get("field_path") or "") == "comparability.status"


def required_metric_assessment_paths(record: dict[str, Any]) -> set[str]:
    paths = {
        "comparability.status",
        *{
            f"endpoints[{index}].endpoint_type"
            for index, _ in enumerate(record["endpoints"])
        },
    }
    for collection in ("quantitative_findings", "operating_conditions"):
        for index, _ in enumerate(record[collection]):
            paths.add(f"{collection}[{index}].value")
            paths.add(f"{collection}[{index}].unit")
    return paths


def required_assessment_path_defects(
    record: dict[str, Any],
    verification: dict[str, Any],
) -> tuple[list[str], list[str]]:
    expected = required_metric_assessment_paths(record)
    counts = Counter(
        str(item.get("field_path") or "")
        for item in verification["field_assessments"]
    )
    missing = sorted(expected - set(counts))
    duplicated = sorted(path for path in expected if counts[path] > 1)
    return missing, duplicated


def merge_verification_completion(
    *,
    initial: dict[str, Any],
    completion: dict[str, Any],
    required_paths: Iterable[str],
) -> dict[str, Any]:
    required = sorted(set(required_paths))
    returned = [
        str(item.get("field_path") or "")
        for item in completion["field_assessments"]
    ]
    if sorted(returned) != required or len(returned) != len(set(returned)):
        raise RuntimeError(
            "Verification completion returned unexpected field paths: "
            f"required={required}, returned={returned}"
        )
    merged = copy.deepcopy(initial)
    merged["field_assessments"].extend(
        copy.deepcopy(completion["field_assessments"])
    )
    merged["anchor_exclusion_violation"] = bool(
        initial["anchor_exclusion_violation"]
        or completion["anchor_exclusion_violation"]
    )
    merged["record_usable"] = bool(
        initial["record_usable"] and completion["record_usable"]
    )
    merged["record_usable_rationale"] = (
        f"{initial['record_usable_rationale']} "
        "Required-path completion: "
        f"{completion['record_usable_rationale']}"
    )
    merged["verification_completion_applied"] = True
    merged["verification_completion_paths"] = required
    return merged


def mean_present(rows: Iterable[dict[str, Any]], key: str) -> float | str:
    values = [
        float(row[key])
        for row in rows
        if row.get(key) not in {"", None}
    ]
    return statistics.fmean(values) if values else ""


def citation_source_ids(review: str) -> list[str]:
    """Return every source ID from plain and locator-level citations."""
    return SOURCE_OR_LOCATOR_PATTERN.findall(review)


def _parallel(
    items: list[Any],
    worker: Callable[[Any], Any],
    *,
    workers: int,
    label: str,
) -> list[Any]:
    if not items:
        return []
    if workers <= 1:
        results = []
        for index, item in enumerate(items, start=1):
            print(f"[{label} {index}/{len(items)}]", flush=True)
            results.append(worker(item))
        return results
    results_by_index: dict[int, Any] = {}
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(worker, item): index
            for index, item in enumerate(items)
        }
        completed = 0
        for future in as_completed(futures):
            index = futures[future]
            results_by_index[index] = future.result()
            completed += 1
            print(f"[{label} {completed}/{len(items)}]", flush=True)
    return [results_by_index[index] for index in range(len(items))]


def _local_retrieval(
    *,
    run_dir: Path,
    tasks: list[dict[str, Any]],
    anchors: list[dict[str, Any]],
    systems: list[str],
    api: ResumableOpenAI,
    device: str,
    batch_size: int,
) -> None:
    if not LOCAL_SYSTEMS.intersection(systems):
        return
    retriever = LocalReviewRetriever(
        anchor_records=anchors,
        device=device,
        batch_size=batch_size,
    )
    for task_index, task in enumerate(tasks, start=1):
        task_id = str(task["task_id"])
        print(f"[local retrieval {task_index}/{len(tasks)}] {task_id}", flush=True)
        candidate_path = run_dir / "retrieval" / task_id / "candidates.json"
        if candidate_path.exists():
            candidate_packet = load_json(candidate_path)
        else:
            candidate_packet = retriever.retrieve_document_candidates(task)
            candidate_packet["runtime"][
                "shared_bge_model_load_seconds"
            ] = retriever.model_load_seconds
            write_json(candidate_path, candidate_packet)
        candidates = candidate_packet["candidate_documents"]

        if "bge_llm_local_rag" in systems:
            source_path = (
                run_dir
                / "systems"
                / "bge_llm_local_rag"
                / task_id
                / "sources.json"
            )
            if not source_path.exists():
                cards = selector_cards(candidates)
                candidate_ids = [str(card["source_id"]) for card in cards]
                selector_user = render_template(
                    prompt("document_selector_user.txt"),
                    {
                        "REVIEW_TASK": task_text(task),
                        "REQUIRED_COMPONENTS": component_text(task),
                        "TASK_BOUNDARIES": canonical_json(
                            next(
                                ledger
                                for ledger in load_jsonl(
                                    PACKAGE_ROOT
                                    / "input"
                                    / "review_task_ledgers.jsonl"
                                )
                                if ledger["task_id"] == task_id
                            )
                        ),
                        "CANDIDATE_SCREEN_BUDGET": str(
                            len(cards)
                        ),
                        "MINIMUM_RETAINED_SOURCES": str(
                            MIN_RETAINED_SOURCES
                        ),
                        "DOCUMENT_CARDS": json.dumps(
                            cards,
                            ensure_ascii=True,
                            indent=2,
                        ),
                    },
                )
                call = api.call_json(
                    stage="document_selection",
                    call_key=f"{task_id}:bge_llm_local_rag:document_selector",
                    system_prompt=prompt(
                        "document_selector_system.txt"
                    ).read_text(encoding="utf-8"),
                    user_prompt=selector_user,
                    schema_name="review_document_selection",
                    schema=schema("document_selection.schema.json"),
                    output_path=(
                        run_dir
                        / "calls"
                        / "bge_llm_local_rag"
                        / task_id
                        / "document_selection.json"
                    ),
                    max_output_tokens=6000,
                )
                selected_ids = call["result"]["selected_source_ids"]
                excluded_ids = [
                    str(item["source_id"])
                    for item in call["result"]["excluded_sources"]
                ]
                if len(selected_ids) != len(set(selected_ids)):
                    raise RuntimeError(
                        f"{task_id}: selector returned duplicate source ids"
                    )
                if not (
                    MIN_RETAINED_SOURCES
                    <= len(selected_ids)
                    <= LLM_SELECTOR_POOL
                ):
                    raise RuntimeError(
                        f"{task_id}: selector retained {len(selected_ids)} "
                        f"sources; expected {MIN_RETAINED_SOURCES} to "
                        f"{LLM_SELECTOR_POOL}"
                    )
                if len(excluded_ids) != len(set(excluded_ids)):
                    raise RuntimeError(
                        f"{task_id}: selector returned duplicate exclusions"
                    )
                if set(selected_ids).intersection(excluded_ids):
                    raise RuntimeError(
                        f"{task_id}: selector both retained and excluded a "
                        "source"
                    )
                if set(selected_ids).union(excluded_ids) != set(candidate_ids):
                    raise RuntimeError(
                        f"{task_id}: selector did not classify every source"
                    )
                candidate_order = {
                    source_id: index
                    for index, source_id in enumerate(candidate_ids)
                }
                if selected_ids != sorted(
                    selected_ids,
                    key=candidate_order.__getitem__,
                ):
                    raise RuntimeError(
                        f"{task_id}: selected sources are not in BGE rank order"
                    )
                id_to_document = {
                    f"D{index:02d}": document
                    for index, document in enumerate(
                        candidates[: len(cards)],
                        start=1,
                    )
                }
                if not set(selected_ids).issubset(id_to_document):
                    raise RuntimeError(
                        f"{task_id}: selector returned unknown source id"
                    )
                selected = [id_to_document[source_id] for source_id in selected_ids]
                coverage = call["result"]["component_coverage"]
                required_components = {
                    str(component["component_id"])
                    for component in task["components"]
                }
                returned_components = {
                    str(item["component_id"]) for item in coverage
                }
                if returned_components != required_components:
                    raise RuntimeError(
                        f"{task_id}: selector returned incomplete component "
                        "coverage"
                    )
                for item in coverage:
                    covered_ids = item["selected_source_ids"]
                    if not covered_ids or not set(covered_ids).issubset(
                        selected_ids
                    ):
                        raise RuntimeError(
                            f"{task_id}: invalid selector component coverage"
                        )
                packet = retriever.expand_selected_documents(
                    task=task,
                    selected_documents=selected,
                )
                packet["selection"] = {
                    "method": "gpt51_eligibility_screen_from_bge_top20",
                    "candidate_screen_budget": LLM_SELECTOR_POOL,
                    "minimum_retained_sources": MIN_RETAINED_SOURCES,
                    "retained_source_count": len(selected_ids),
                    "selected_candidate_source_ids": selected_ids,
                    "selector_request_hash": call["request_hash"],
                }
                write_json(source_path, packet)


def _web_retrieval(
    *,
    run_dir: Path,
    tasks: list[dict[str, Any]],
    anchors: list[dict[str, Any]],
    systems: list[str],
    api: ResumableOpenAI,
) -> None:
    if "gpt51_web_search" not in systems:
        return
    web_schema = schema("web_source_packet.schema.json")
    for task_index, task in enumerate(tasks, start=1):
        task_id = str(task["task_id"])
        print(f"[web retrieval {task_index}/{len(tasks)}] {task_id}", flush=True)
        source_path = (
            run_dir
            / "systems"
            / "gpt51_web_search"
            / task_id
            / "sources.json"
        )
        if source_path.exists():
            continue
        user = render_template(
            prompt("web_source_discovery_user.txt"),
            {
                "REVIEW_TASK": task_text(task),
                "REQUIRED_COMPONENTS": component_text(task),
                "DATA_EXTRACTION_OBJECTIVE": str(
                    task["data_extraction_objective"]
                ),
                "ANCHOR_EXCLUSIONS": anchor_text(task_id, anchors),
                "CANDIDATE_SOURCE_BUDGET": str(WEB_CANDIDATE_BUDGET),
                "MINIMUM_RETAINED_SOURCES": str(MIN_WEB_SOURCES),
            },
        )
        call = api.call_web_json(
            stage="web_source_discovery",
            call_key=f"{task_id}:gpt51_web_search:source_discovery",
            system_prompt=prompt(
                "web_source_discovery_system.txt"
            ).read_text(encoding="utf-8"),
            user_prompt=user,
            schema_name="pfas_web_source_packet",
            schema=web_schema,
            output_path=(
                run_dir
                / "calls"
                / "gpt51_web_search"
                / task_id
                / "web_source_discovery.json"
            ),
            max_output_tokens=32000,
        )
        if call["result"]["task_id"] != task_id:
            raise RuntimeError(f"{task_id}: Web Search returned wrong task id")
        identifiers = task_anchor_identifiers(anchors, task_id)
        kept = []
        dropped = []
        seen_keys: set[str] = set()
        for source in call["result"]["sources"]:
            reason = exclusion_reason(
                {
                    "doi": source["doi"],
                    "url": source["inspected_url"],
                    "title": source["title"],
                },
                identifiers,
            )
            if reason is not None:
                dropped.append(
                    {"source": source, "reason": f"anchor:{reason}"}
                )
                continue
            if not consulted_source_match(
                source["inspected_url"],
                source["doi"],
                call["consulted_sources"],
            ):
                dropped.append(
                    {
                        "source": source,
                        "reason": "inspected_url_not_in_api_source_list",
                    }
                )
                continue
            dedup_key = (
                normalize_doi(source["doi"])
                or normalize_url(source["inspected_url"])
                or normalize_title(source["title"])
            )
            if not dedup_key or dedup_key in seen_keys:
                dropped.append(
                    {"source": source, "reason": "duplicate_or_empty_identity"}
                )
                continue
            locator_ids = [
                passage["locator_id"]
                for passage in source["evidence_passages"]
            ]
            if len(locator_ids) != len(set(locator_ids)):
                dropped.append(
                    {"source": source, "reason": "duplicate_locator_id"}
                )
                continue
            kept.append(source)
            seen_keys.add(dedup_key)
        if len(kept) < MIN_WEB_SOURCES:
            raise RuntimeError(
                f"{task_id}: only {len(kept)} verified Web Search sources "
                f"after deterministic checks; need {MIN_WEB_SOURCES}"
            )
        prepared = []
        for source_index, source in enumerate(kept, start=1):
            source_id = f"WEB{source_index:02d}"
            prepared.append(
                {
                    "source_id": source_id,
                    "source": source["inspected_url"],
                    "title": source["title"],
                    "year": source["year"],
                    "doi": source["doi"],
                    "doi_or_stable_url": (
                        f"https://doi.org/{normalize_doi(source['doi'])}"
                        if normalize_doi(source["doi"])
                        else source["inspected_url"]
                    ),
                    "citation": source["citation"],
                    "publication_type": source["publication_type"],
                    "publication_status": source["publication_status"],
                    "access_scope": source["access_scope"],
                    "covered_component_ids": source[
                        "covered_component_ids"
                    ],
                    "source_limitations": source["source_limitations"],
                    "evidence_chunks": [
                        {
                            "locator_id": (
                                f"{source_id}-E{passage_index:02d}"
                            ),
                            "corpus_chunk": None,
                            "section": passage["page_or_section"],
                            "text": passage["passage"],
                            "passage_type": passage["passage_type"],
                        }
                        for passage_index, passage in enumerate(
                            source["evidence_passages"],
                            start=1,
                        )
                    ],
                    "capture_source_id": source["source_id"],
                }
            )
        write_json(
            source_path,
            {
                "task_id": task_id,
                "candidate_source_budget": WEB_CANDIDATE_BUDGET,
                "minimum_retained_sources": MIN_WEB_SOURCES,
                "retained_source_count": len(prepared),
                "sources": prepared,
                "selection": {
                    "method": "gpt51_responses_web_search",
                    "request_hash": call["request_hash"],
                    "consulted_source_count": len(call["consulted_sources"]),
                    "candidate_source_count": len(
                        call["result"]["sources"]
                    ),
                    "retained_source_count": len(prepared),
                    "dropped_sources": dropped,
                },
            },
        )


def _source_packet(run_dir: Path, system: str, task_id: str) -> dict[str, Any]:
    path = run_dir / "systems" / system / task_id / "sources.json"
    if not path.exists():
        raise RuntimeError(f"Missing source packet: {path}")
    return load_json(path)


def _extract(
    *,
    run_dir: Path,
    tasks: list[dict[str, Any]],
    anchors: list[dict[str, Any]],
    systems: list[str],
    api: ResumableOpenAI,
    workers: int,
) -> None:
    evidence_schema = schema("evidence_table.schema.json")
    extraction_system = prompt(
        "shared_evidence_extraction_system.txt"
    ).read_text(encoding="utf-8")
    jobs = []
    for task in tasks:
        task_id = str(task["task_id"])
        for system in systems:
            if system in DIRECT_SYSTEMS:
                continue
            packet = _source_packet(run_dir, system, task_id)
            for source in packet["sources"]:
                jobs.append((task, system, source))

    def worker(job: tuple[dict[str, Any], str, dict[str, Any]]) -> dict[str, Any]:
        task, system, source = job
        task_id = str(task["task_id"])
        is_web = system == "gpt51_web_search"
        user_template = (
            "web_evidence_extraction_user.txt"
            if is_web
            else "local_evidence_extraction_user.txt"
        )
        source_key = (
            "INSPECTED_WEB_SOURCES"
            if is_web
            else "SOURCE_DOCUMENTS_AND_CHUNKS"
        )
        user = render_template(
            prompt(user_template),
            {
                "REVIEW_TASK": task_text(task),
                "DATA_EXTRACTION_OBJECTIVE": str(
                    task["data_extraction_objective"]
                ),
                "SOURCE_SYSTEM": system,
                "SOURCE_ID": str(source["source_id"]),
                "ANCHOR_EXCLUSIONS": anchor_text(task_id, anchors),
                source_key: json.dumps(source, ensure_ascii=True, indent=2),
            },
        )
        call = api.call_json(
            stage="structured_extraction",
            call_key=(
                f"{task_id}:{system}:extraction:{source['source_id']}"
            ),
            system_prompt=extraction_system,
            user_prompt=user,
            schema_name="pfas_review_evidence_table",
            schema=extraction_schema_for_source(
                evidence_schema,
                task_id=task_id,
                system=system,
                source_id=str(source["source_id"]),
                locator_ids=(
                    str(chunk["locator_id"])
                    for chunk in source["evidence_chunks"]
                ),
            ),
            output_path=(
                run_dir
                / "calls"
                / system
                / task_id
                / "extraction"
                / f"{source['source_id']}.json"
            ),
            max_output_tokens=16000,
        )
        result = call["result"]
        if result["task_id"] != task_id:
            raise RuntimeError(f"{task_id}: extraction returned wrong task id")
        if result["source_system"] != system:
            raise RuntimeError(
                f"{task_id}: extraction returned wrong source system"
            )
        return {
            "task_id": task_id,
            "system": system,
            "source": source,
            "call": call,
        }

    _parallel(jobs, worker, workers=workers, label="extraction")

    for task in tasks:
        task_id = str(task["task_id"])
        for system in systems:
            if system in DIRECT_SYSTEMS:
                continue
            packet = _source_packet(run_dir, system, task_id)
            records = []
            rejected = []
            field_rejections = []
            field_normalizations = []
            for source in packet["sources"]:
                call = load_json(
                    run_dir
                    / "calls"
                    / system
                    / task_id
                    / "extraction"
                    / f"{source['source_id']}.json"
                )
                valid_locators = {
                    chunk["locator_id"] for chunk in source["evidence_chunks"]
                }
                for index, record in enumerate(
                    call["result"]["records"],
                    start=1,
                ):
                    reasons = []
                    if record["source_id"] != source["source_id"]:
                        reasons.append("wrong_source_id")
                    locators = all_locator_ids(record)
                    if not locators:
                        reasons.append("no_evidence_locators")
                    if not locators.issubset(valid_locators):
                        reasons.append("unknown_evidence_locator")
                    if reasons:
                        rejected.append(
                            {"record": record, "reasons": reasons}
                        )
                        continue
                    normalized = dict(record)
                    normalized["record_id"] = (
                        f"{task_id}-{system}-{source['source_id']}-R{index:02d}"
                    )
                    valid_findings = []
                    for finding_index, finding in enumerate(
                        record["quantitative_findings"]
                    ):
                        canonical, normalization_reason = (
                            normalize_quantitative_finding(finding)
                        )
                        if canonical is not None:
                            valid_findings.append(canonical)
                            if normalization_reason is not None:
                                field_normalizations.append(
                                    {
                                        "record_id": normalized["record_id"],
                                        "field_path": (
                                            "quantitative_findings"
                                            f"[{finding_index}]"
                                        ),
                                        "reason": normalization_reason,
                                        "before": finding,
                                        "after": canonical,
                                    }
                                )
                            continue
                        field_rejections.append(
                            {
                                "record_id": normalized["record_id"],
                                "field_path": (
                                    "quantitative_findings"
                                    f"[{finding_index}]"
                                ),
                                "reason": (
                                    "invalid_value_for_declared_value_form"
                                ),
                                "finding": finding,
                            }
                        )
                    normalized["quantitative_findings"] = valid_findings
                    records.append(normalized)
            write_json(
                run_dir
                / "systems"
                / system
                / task_id
                / "extracted_records.json",
                {
                    "task_id": task_id,
                    "source_system": system,
                    "records": records,
                    "deterministic_preverification_rejections": rejected,
                    "deterministic_field_rejections": field_rejections,
                    "deterministic_field_normalizations": (
                        field_normalizations
                    ),
                },
            )


def _verify(
    *,
    run_dir: Path,
    tasks: list[dict[str, Any]],
    anchors: list[dict[str, Any]],
    systems: list[str],
    api: ResumableOpenAI,
    workers: int,
) -> None:
    verification_schema = schema("extraction_verification.schema.json")
    verification_system = prompt(
        "extraction_verification_judge.txt"
    ).read_text(encoding="utf-8")
    jobs = []
    task_map = by_id(tasks, "task_id")
    for task in tasks:
        task_id = str(task["task_id"])
        for system in systems:
            if system in DIRECT_SYSTEMS:
                continue
            extracted = load_json(
                run_dir
                / "systems"
                / system
                / task_id
                / "extracted_records.json"
            )
            packet = _source_packet(run_dir, system, task_id)
            source_map = by_id(packet["sources"], "source_id")
            for record in extracted["records"]:
                jobs.append((task, system, record, source_map[record["source_id"]]))

    def worker(
        job: tuple[
            dict[str, Any],
            str,
            dict[str, Any],
            dict[str, Any],
        ]
    ) -> dict[str, Any]:
        task, system, record, source = job
        task_id = str(task["task_id"])
        user = render_template(
            prompt("extraction_verification_user.txt"),
            {
                "REVIEW_TASK": task_text(task),
                "DATA_EXTRACTION_OBJECTIVE": str(
                    task["data_extraction_objective"]
                ),
                "ANCHOR_EXCLUSIONS": anchor_text(task_id, anchors),
                "EVIDENCE_RECORD": json.dumps(
                    record,
                    ensure_ascii=True,
                    indent=2,
                ),
                "CITED_SOURCE_EVIDENCE": json.dumps(
                    source,
                    ensure_ascii=True,
                    indent=2,
                ),
            },
        )
        call = api.call_json(
            stage="source_verification",
            call_key=f"{task_id}:{system}:verify:{record['record_id']}",
            system_prompt=verification_system,
            user_prompt=user,
            schema_name="pfas_extraction_verification",
            schema=verification_schema,
            output_path=(
                run_dir
                / "calls"
                / system
                / task_id
                / "verification"
                / f"{record['record_id']}.json"
            ),
            max_output_tokens=12000,
        )
        result = call["result"]
        if result["task_id"] != task_id:
            raise RuntimeError(f"{record['record_id']}: wrong task id")
        if result["record_id"] != record["record_id"]:
            raise RuntimeError(f"{record['record_id']}: wrong record id")
        return result

    _parallel(jobs, worker, workers=workers, label="verification")

    completion_system = (
        verification_system
        + "\n\n"
        + prompt("extraction_verification_completion_judge.txt").read_text(
            encoding="utf-8"
        )
    )
    completion_jobs = []
    for task in tasks:
        task_id = str(task["task_id"])
        for system in systems:
            if system in DIRECT_SYSTEMS:
                continue
            extracted = load_json(
                run_dir
                / "systems"
                / system
                / task_id
                / "extracted_records.json"
            )
            packet = _source_packet(run_dir, system, task_id)
            source_map = by_id(packet["sources"], "source_id")
            for record in extracted["records"]:
                initial = load_json(
                    run_dir
                    / "calls"
                    / system
                    / task_id
                    / "verification"
                    / f"{record['record_id']}.json"
                )["result"]
                missing, duplicated = required_assessment_path_defects(
                    record,
                    initial,
                )
                if duplicated:
                    raise RuntimeError(
                        f"{record['record_id']}: duplicate required "
                        f"verification paths {duplicated}"
                    )
                if missing:
                    completion_jobs.append(
                        (
                            task,
                            system,
                            record,
                            source_map[record["source_id"]],
                            missing,
                        )
                    )

    def completion_worker(
        job: tuple[
            dict[str, Any],
            str,
            dict[str, Any],
            dict[str, Any],
            list[str],
        ]
    ) -> dict[str, Any]:
        task, system, record, source, missing = job
        task_id = str(task["task_id"])
        user = render_template(
            prompt("extraction_verification_completion_user.txt"),
            {
                "REVIEW_TASK": task_text(task),
                "DATA_EXTRACTION_OBJECTIVE": str(
                    task["data_extraction_objective"]
                ),
                "ANCHOR_EXCLUSIONS": anchor_text(task_id, anchors),
                "EVIDENCE_RECORD": json.dumps(
                    record,
                    ensure_ascii=True,
                    indent=2,
                ),
                "CITED_SOURCE_EVIDENCE": json.dumps(
                    source,
                    ensure_ascii=True,
                    indent=2,
                ),
                "MISSING_REQUIRED_FIELD_PATHS": json.dumps(
                    missing,
                    ensure_ascii=True,
                    indent=2,
                ),
            },
        )
        call = api.call_json(
            stage="source_verification_completion",
            call_key=(
                f"{task_id}:{system}:verify_completion:"
                f"{record['record_id']}:{sha256_text(canonical_json(missing))}"
            ),
            system_prompt=completion_system,
            user_prompt=user,
            schema_name="pfas_extraction_verification_completion",
            schema=verification_schema,
            output_path=(
                run_dir
                / "calls"
                / system
                / task_id
                / "verification_completion"
                / f"{record['record_id']}.json"
            ),
            max_output_tokens=6000,
        )
        result = call["result"]
        if result["task_id"] != task_id:
            raise RuntimeError(f"{record['record_id']}: wrong task id")
        if result["record_id"] != record["record_id"]:
            raise RuntimeError(f"{record['record_id']}: wrong record id")
        merge_verification_completion(
            initial={
                "field_assessments": [],
                "anchor_exclusion_violation": False,
                "record_usable": True,
                "record_usable_rationale": "",
            },
            completion=result,
            required_paths=missing,
        )
        return result

    _parallel(
        completion_jobs,
        completion_worker,
        workers=workers,
        label="verification completion",
    )

    for task_id, task in task_map.items():
        for system in systems:
            if system in DIRECT_SYSTEMS:
                continue
            extracted = load_json(
                run_dir
                / "systems"
                / system
                / task_id
                / "extracted_records.json"
            )
            verified_records = []
            all_verifications = []
            for record in extracted["records"]:
                call = load_json(
                    run_dir
                    / "calls"
                    / system
                    / task_id
                    / "verification"
                    / f"{record['record_id']}.json"
                )
                verification = call["result"]
                missing, duplicated = required_assessment_path_defects(
                    record,
                    verification,
                )
                if duplicated:
                    raise RuntimeError(
                        f"{record['record_id']}: duplicate required "
                        f"verification paths {duplicated}"
                    )
                completion_path = (
                    run_dir
                    / "calls"
                    / system
                    / task_id
                    / "verification_completion"
                    / f"{record['record_id']}.json"
                )
                if missing:
                    completion = load_json(completion_path)["result"]
                    verification = merge_verification_completion(
                        initial=verification,
                        completion=completion,
                        required_paths=missing,
                    )
                elif completion_path.exists():
                    raise RuntimeError(
                        f"{record['record_id']}: stale completion call exists"
                    )
                all_verifications.append(verification)
                if (
                    verification["record_usable"]
                    and not verification["anchor_exclusion_violation"]
                ):
                    verified_records.append(
                        {
                            "record": record,
                            "verification": verification,
                        }
                    )
            write_json(
                run_dir
                / "systems"
                / system
                / task_id
                / "verified_records.json",
                {
                    "task_id": task_id,
                    "source_system": system,
                    "verified_records": verified_records,
                    "all_verifications": all_verifications,
                },
            )


def _verified_support(
    run_dir: Path,
    system: str,
    task_id: str,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    verified = load_json(
        run_dir
        / "systems"
        / system
        / task_id
        / "verified_records.json"
    )
    packet = _source_packet(run_dir, system, task_id)
    used_source_ids = {
        item["record"]["source_id"] for item in verified["verified_records"]
    }
    excerpts = [
        source
        for source in packet["sources"]
        if source["source_id"] in used_source_ids
    ]
    return verified, excerpts


def compact_verified_records_for_synthesis(
    verified_records: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Remove redundant verifier prose while preserving eligibility signals."""
    compact_records = []
    for item in verified_records:
        verification = item["verification"]
        assessments = []
        for assessment in verification["field_assessments"]:
            compact = {
                "field_path": assessment["field_path"],
                "status": assessment["status"],
                "error_type": assessment["error_type"],
            }
            if assessment["status"] != "supported":
                compact["reason"] = assessment["reason"]
            assessments.append(compact)
        compact_records.append(
            {
                "record": item["record"],
                "verification": {
                    "record_id": verification["record_id"],
                    "record_usable": verification["record_usable"],
                    "anchor_exclusion_violation": verification[
                        "anchor_exclusion_violation"
                    ],
                    "field_assessments": assessments,
                },
            }
        )
    return compact_records


def compact_supporting_excerpts_for_synthesis(
    sources: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Expose source evidence without retrieval scores or benchmark IDs."""
    source_fields = (
        "source_id",
        "citation",
        "title",
        "year",
        "doi",
        "doi_or_stable_url",
        "publication_status",
        "publication_type",
        "access_scope",
        "source_limitations",
    )
    evidence_fields = (
        "locator_id",
        "corpus_chunk",
        "section",
        "passage_type",
        "text",
    )
    compact_sources = []
    for source in sources:
        compact_source = {
            field: source[field]
            for field in source_fields
            if field in source
        }
        compact_source["evidence_chunks"] = [
            {
                field: chunk[field]
                for field in evidence_fields
                if field in chunk
            }
            for chunk in source["evidence_chunks"]
        ]
        compact_sources.append(compact_source)
    return compact_sources


def _synthesize(
    *,
    run_dir: Path,
    tasks: list[dict[str, Any]],
    ledgers: dict[str, dict[str, Any]],
    anchors: list[dict[str, Any]],
    systems: list[str],
    api: ResumableOpenAI,
    workers: int,
) -> None:
    synthesis_system = prompt(
        "shared_review_synthesis_system.txt"
    ).read_text(encoding="utf-8")
    jobs = [(task, system) for task in tasks for system in systems]

    def worker(job: tuple[dict[str, Any], str]) -> dict[str, Any]:
        task, system = job
        task_id = str(task["task_id"])
        if system in DIRECT_SYSTEMS:
            system_prompt = prompt(
                "direct_review_synthesis_system.txt"
            ).read_text(encoding="utf-8")
            user = render_template(
                prompt("direct_review_synthesis_user.txt"),
                {
                    "REVIEW_BRIEF": str(task["review_brief"]),
                    "REQUIRED_COMPONENTS": synthesis_component_text(task),
                    "TASK_BOUNDARIES": synthesis_boundary_text(
                        ledgers[task_id]
                    ),
                    "ANCHOR_EXCLUSIONS": anchor_text(task_id, anchors),
                },
            )
        else:
            system_prompt = synthesis_system
            verified, excerpts = _verified_support(
                run_dir, system, task_id
            )
            synthesis_records = compact_verified_records_for_synthesis(
                verified["verified_records"]
            )
            synthesis_excerpts = compact_supporting_excerpts_for_synthesis(
                excerpts
            )
            user = render_template(
                prompt("review_synthesis_user.txt"),
                {
                    "REVIEW_BRIEF": str(task["review_brief"]),
                    "REQUIRED_COMPONENTS": synthesis_component_text(task),
                    "TASK_BOUNDARIES": synthesis_boundary_text(
                        ledgers[task_id]
                    ),
                    "ANCHOR_EXCLUSIONS": anchor_text(task_id, anchors),
                    "VERIFIED_EVIDENCE_TABLE": json.dumps(
                        synthesis_records,
                        ensure_ascii=True,
                        indent=2,
                    ),
                    "VERIFIED_SUPPORTING_EXCERPTS": json.dumps(
                        synthesis_excerpts,
                        ensure_ascii=True,
                        indent=2,
                    ),
                },
            )
        call = api.call_text(
            stage="review_synthesis",
            call_key=f"{task_id}:{system}:review_synthesis",
            system_prompt=system_prompt,
            user_prompt=user,
            output_path=(
                run_dir
                / "calls"
                / system
                / task_id
                / "review_synthesis.json"
            ),
            max_output_tokens=16000,
        )
        raw_review = call["result"].strip()
        clean_review, removed_labels = sanitize_internal_review_notation(
            raw_review
        )
        clean_review, normalized_record_citations = (
            normalize_record_citation_ids(clean_review)
        )
        final_review = clean_review.strip() + "\n"
        review_path = (
            run_dir
            / "systems"
            / system
            / task_id
            / "professional_review.md"
        )
        review_path.parent.mkdir(parents=True, exist_ok=True)
        review_path.write_text(final_review, encoding="utf-8")
        write_json(
            review_path.with_name("synthesis_postprocessing.json"),
            {
                "task_id": task_id,
                "system": system,
                "synthesis_request_hash": call["request_hash"],
                "raw_review_sha256": sha256_text(raw_review),
                "final_review_sha256": sha256_text(final_review),
                "removed_internal_notation_spans": removed_labels,
                "normalized_record_citations": normalized_record_citations,
            },
        )
        return call

    _parallel(jobs, worker, workers=workers, label="synthesis")


def _source_support(
    *,
    run_dir: Path,
    tasks: list[dict[str, Any]],
    anchors: list[dict[str, Any]],
    systems: list[str],
    api: ResumableOpenAI,
    workers: int,
) -> None:
    support_schema = schema("review_source_support.schema.json")
    support_system = prompt(
        "review_source_support_judge.txt"
    ).read_text(encoding="utf-8")
    jobs = [
        (task, system)
        for task in tasks
        for system in systems
        if system not in DIRECT_SYSTEMS
    ]

    def worker(job: tuple[dict[str, Any], str]) -> dict[str, Any]:
        task, system = job
        task_id = str(task["task_id"])
        verified, excerpts = _verified_support(run_dir, system, task_id)
        support_records = compact_verified_records_for_synthesis(
            verified["verified_records"]
        )
        support_excerpts = compact_supporting_excerpts_for_synthesis(
            excerpts
        )
        review = (
            run_dir
            / "systems"
            / system
            / task_id
            / "professional_review.md"
        ).read_text(encoding="utf-8")
        user = render_template(
            prompt("review_source_support_user.txt"),
            {
                "REVIEW_TASK": task_text(task),
                "CANDIDATE_REVIEW": review,
                "VERIFIED_EVIDENCE_TABLE": json.dumps(
                    support_records,
                    ensure_ascii=True,
                    indent=2,
                ),
                "VERIFIED_SUPPORTING_EXCERPTS": json.dumps(
                    support_excerpts,
                    ensure_ascii=True,
                    indent=2,
                ),
                "ANCHOR_EXCLUSIONS": anchor_text(task_id, anchors),
            },
        )
        call = api.call_json(
            stage="review_source_support",
            call_key=f"{task_id}:{system}:review_source_support",
            system_prompt=support_system,
            user_prompt=user,
            schema_name="pfas_review_source_support",
            schema=support_schema,
            output_path=(
                run_dir
                / "calls"
                / system
                / task_id
                / "review_source_support.json"
            ),
            max_output_tokens=14000,
        )
        if call["result"]["task_id"] != task_id:
            raise RuntimeError(f"{task_id}: source judge returned wrong task id")
        return call

    _parallel(jobs, worker, workers=workers, label="source support")


def _review_judge(
    *,
    run_dir: Path,
    tasks: list[dict[str, Any]],
    ledgers: dict[str, dict[str, Any]],
    systems: list[str],
    api: ResumableOpenAI,
    workers: int,
    repeats: int,
) -> None:
    judge_schema = schema("review_judgment.schema.json")
    judge_system = prompt("common_review_judge.txt").read_text(
        encoding="utf-8"
    )
    blinded_reviews: dict[tuple[str, str], str] = {}
    for task in tasks:
        task_id = str(task["task_id"])
        for system in systems:
            task_dir = run_dir / "systems" / system / task_id
            review = (task_dir / "professional_review.md").read_text(
                encoding="utf-8"
            )
            anonymized, anonymization_audit = (
                prepare_anonymous_citation_aware_layer_b_review(review)
            )
            blinded_reviews[(task_id, system)] = anonymized
            (task_dir / "layer_b_candidate_review.md").write_text(
                anonymized,
                encoding="utf-8",
            )
            write_json(
                task_dir / "layer_b_anonymization.json",
                anonymization_audit,
            )
    jobs = [
        (task, system, repeat)
        for repeat in range(1, repeats + 1)
        for task in tasks
        for system in systems
    ]

    def worker(job: tuple[dict[str, Any], str, int]) -> dict[str, Any]:
        task, system, repeat = job
        task_id = str(task["task_id"])
        review = blinded_reviews[(task_id, system)]
        user = render_template(
            prompt("common_review_judge_user.txt"),
            {
                "REVIEW_TASK": task_text(task),
                "REQUIRED_COMPONENTS": component_text(task),
                "TASK_LEDGER": canonical_json(ledgers[task_id]),
                "CANDIDATE_REVIEW": review,
            },
        )
        call = api.call_json(
            stage="review_quality_judge",
            call_key=f"{task_id}:{system}:review_judge:r{repeat}",
            system_prompt=judge_system,
            user_prompt=user,
            schema_name="pfas_professional_review_judgment",
            schema=judge_schema,
            output_path=(
                run_dir
                / "calls"
                / system
                / task_id
                / "review_judge"
                / f"repeat_{repeat}.json"
            ),
            max_output_tokens=20000,
        )
        if call["result"]["task_id"] != task_id:
            raise RuntimeError(f"{task_id}: review judge returned wrong task id")
        return call

    _parallel(jobs, worker, workers=workers, label="review judge")


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def extraction_metrics(
    run_dir: Path,
    task_id: str,
    system: str,
) -> dict[str, Any]:
    if system in DIRECT_SYSTEMS:
        return {
            "task_id": task_id,
            "system": system,
            "evidence_access_mode": "none",
            "layer_a_status": "not_applicable_no_retrieval",
            "extracted_record_count": 0,
            "verified_usable_record_count": 0,
            "verified_unique_source_count": 0,
            "preverification_rejection_count": 0,
            "deterministic_field_rejection_count": 0,
            "deterministic_field_normalization_count": 0,
            "field_assessment_count": 0,
            "supported_extracted_field_rate": "",
            "weighted_extracted_field_support": "",
            "numeric_transcription_accuracy": "",
            "endpoint_classification_accuracy": "",
            "comparability_field_accuracy": "",
            "anchor_exclusion_violation_count": 0,
        }
    extracted = load_json(
        run_dir
        / "systems"
        / system
        / task_id
        / "extracted_records.json"
    )
    verified = load_json(
        run_dir
        / "systems"
        / system
        / task_id
        / "verified_records.json"
    )
    assessments = [
        assessment
        for verification in verified["all_verifications"]
        for assessment in verification["field_assessments"]
    ]
    status_counts = Counter(item["status"] for item in assessments)
    total = len(assessments)
    numeric = [
        item
        for item in assessments
        if is_quantitative_value_or_unit_assessment(item)
    ]
    endpoints = [
        item for item in assessments if is_endpoint_type_assessment(item)
    ]
    comparability = [
        item
        for item in assessments
        if is_comparability_status_assessment(item)
    ]
    usable = verified["verified_records"]
    unique_sources = {
        item["record"]["source_id"] for item in usable
    }
    return {
        "task_id": task_id,
        "system": system,
        "evidence_access_mode": "retrieval_enabled",
        "layer_a_status": "evaluated",
        "extracted_record_count": len(extracted["records"]),
        "verified_usable_record_count": len(usable),
        "verified_unique_source_count": len(unique_sources),
        "preverification_rejection_count": len(
            extracted["deterministic_preverification_rejections"]
        ),
        "deterministic_field_rejection_count": len(
            extracted.get("deterministic_field_rejections", [])
        ),
        "deterministic_field_normalization_count": len(
            extracted.get("deterministic_field_normalizations", [])
        ),
        "field_assessment_count": total,
        "supported_extracted_field_rate": (
            status_counts["supported"] / total if total else 0.0
        ),
        "weighted_extracted_field_support": (
            (
                status_counts["supported"]
                + 0.5 * status_counts["partially_supported"]
            )
            / total
            if total
            else 0.0
        ),
        "numeric_transcription_accuracy": (
            sum(item["status"] == "supported" for item in numeric)
            / len(numeric)
            if numeric
            else ""
        ),
        "endpoint_classification_accuracy": (
            sum(item["status"] == "supported" for item in endpoints)
            / len(endpoints)
            if endpoints
            else ""
        ),
        "comparability_field_accuracy": (
            sum(item["status"] == "supported" for item in comparability)
            / len(comparability)
            if comparability
            else ""
        ),
        "anchor_exclusion_violation_count": sum(
            verification["anchor_exclusion_violation"]
            for verification in verified["all_verifications"]
        ),
    }


def source_support_metrics(
    run_dir: Path,
    task_id: str,
    system: str,
) -> dict[str, Any]:
    if system in DIRECT_SYSTEMS:
        return {
            "task_id": task_id,
            "system": system,
            "source_support_status": "not_applicable_no_retrieved_sources",
            "source_dependent_claim_count": "",
            "supported_source_dependent_claim_rate": "",
            "weighted_source_support_rate": "",
            "claim_citation_coverage_rate": "",
            "unsupported_or_contradicted_claim_count": "",
            "unique_cited_sources": 0,
            "retained_source_count": 0,
            "peer_reviewed_primary_source_fraction_among_cited_sources": "",
            "valid_identifier_fraction_among_cited_sources": "",
            "citation_marker_count": 0,
            "unverifiable_citation_rate": "",
            "anchor_exclusion_violation": 0,
        }
    call = load_json(
        run_dir
        / "calls"
        / system
        / task_id
        / "review_source_support.json"
    )
    result = call["result"]
    statuses = Counter(
        item["status"] for item in result["claim_assessments"]
    )
    total = len(result["claim_assessments"])
    review = (
        run_dir
        / "systems"
        / system
        / task_id
        / "professional_review.md"
    ).read_text(encoding="utf-8")
    cited_ids = citation_source_ids(review)
    packet_sources = _source_packet(run_dir, system, task_id)["sources"]
    source_by_id = {source["source_id"]: source for source in packet_sources}
    known = set(source_by_id)
    unknown = set(cited_ids) - known
    cited_known_ids = set(cited_ids) & known
    cited_known_sources = [
        source_by_id[source_id] for source_id in sorted(cited_known_ids)
    ]
    claims_with_known_citations = 0
    for assessment in result["claim_assessments"]:
        assessment_ids = citation_source_ids(
            " ".join(assessment.get("cited_source_ids", []))
        )
        if set(assessment_ids) & known:
            claims_with_known_citations += 1
    peer_reviewed = {
        "peer_reviewed",
        "peer_reviewed_or_formally_published",
    }
    return {
        "task_id": task_id,
        "system": system,
        "source_support_status": "evaluated",
        "source_dependent_claim_count": total,
        "supported_source_dependent_claim_rate": (
            statuses["supported"] / total if total else 1.0
        ),
        "weighted_source_support_rate": (
            (statuses["supported"] + 0.5 * statuses["partially_supported"])
            / total
            if total
            else 1.0
        ),
        "claim_citation_coverage_rate": (
            claims_with_known_citations / total if total else 1.0
        ),
        "unsupported_or_contradicted_claim_count": (
            statuses["unsupported"] + statuses["contradicted"]
        ),
        "unique_cited_sources": len(set(cited_ids) & known),
        "retained_source_count": len(packet_sources),
        "peer_reviewed_primary_source_fraction_among_cited_sources": (
            sum(
                source.get("publication_status") in peer_reviewed
                for source in cited_known_sources
            )
            / len(cited_known_sources)
            if cited_known_sources
            else 0.0
        ),
        "valid_identifier_fraction_among_cited_sources": (
            sum(
                bool(source.get("doi_or_stable_url"))
                for source in cited_known_sources
            )
            / len(cited_known_sources)
            if cited_known_sources
            else 0.0
        ),
        "citation_marker_count": len(cited_ids),
        "unverifiable_citation_rate": (
            len([item for item in cited_ids if item in unknown]) / len(cited_ids)
            if cited_ids
            else 0.0
        ),
        "anchor_exclusion_violation": result[
            "anchor_exclusion_violation"
        ],
    }


def _summary(
    *,
    run_dir: Path,
    tasks: list[dict[str, Any]],
    systems: list[str],
    repeats: int,
) -> None:
    extraction_rows = []
    source_rows = []
    quality_rows = []
    for task in tasks:
        task_id = str(task["task_id"])
        for system in systems:
            extraction_rows.append(
                extraction_metrics(run_dir, task_id, system)
            )
            source_rows.append(
                source_support_metrics(run_dir, task_id, system)
            )
            for repeat in range(1, repeats + 1):
                call = load_json(
                    run_dir
                    / "calls"
                    / system
                    / task_id
                    / "review_judge"
                    / f"repeat_{repeat}.json"
                )
                scored = score_judgment(call["result"])
                quality_rows.append(
                    {
                        "task_id": task_id,
                        "system": system,
                        "repeat": repeat,
                        **{
                            key: value
                            for key, value in scored.items()
                            if key != "task_id"
                            and key != "component_fulfillment_scores"
                        },
                    }
                )

    system_rows = []
    for system in systems:
        system_quality = [
            row for row in quality_rows if row["system"] == system
        ]
        repeat_means = []
        dimension_repeat_means: dict[str, list[float]] = defaultdict(list)
        for repeat in range(1, repeats + 1):
            rows = [
                row for row in system_quality if row["repeat"] == repeat
            ]
            repeat_means.append(
                statistics.fmean(
                    row["atomic_component_capped_review_quality"]
                    for row in rows
                )
            )
            for dimension in DIMENSION_WEIGHTS:
                key = dimension
                dimension_repeat_means[key].append(
                    statistics.fmean(float(row[key]) for row in rows)
                )
        extraction = [
            row for row in extraction_rows if row["system"] == system
        ]
        sources = [row for row in source_rows if row["system"] == system]
        system_rows.append(
            {
                "system": system,
                "task_count": len(tasks),
                "review_quality_mean": statistics.fmean(repeat_means),
                "review_quality_repeat_sample_sd": (
                    statistics.stdev(repeat_means)
                    if len(repeat_means) > 1
                    else 0.0
                ),
                "mean_material_boundary_violation_count": statistics.fmean(
                    row["material_boundary_violation_count"]
                    for row in system_quality
                ),
                "potential_external_scientific_error_rate": statistics.fmean(
                    float(row["potential_external_scientific_error"])
                    for row in system_quality
                ),
                "mean_component_fulfillment": statistics.fmean(
                    row["mean_component_fulfillment"]
                    for row in system_quality
                ),
                "mean_critical_synthesis": statistics.fmean(
                    dimension_repeat_means["critical_synthesis"]
                ),
                "mean_professional_depth": statistics.fmean(
                    dimension_repeat_means["professional_depth"]
                ),
                "mean_current_research_outlook": statistics.fmean(
                    dimension_repeat_means["current_research_outlook"]
                ),
                "mean_verified_usable_records": statistics.fmean(
                    row["verified_usable_record_count"] for row in extraction
                ),
                "mean_verified_unique_sources": statistics.fmean(
                    row["verified_unique_source_count"] for row in extraction
                ),
                "supported_extracted_field_rate": mean_present(
                    extraction,
                    "supported_extracted_field_rate",
                ),
                "weighted_extracted_field_support": mean_present(
                    extraction,
                    "weighted_extracted_field_support",
                ),
                "numeric_transcription_accuracy": mean_present(
                    extraction,
                    "numeric_transcription_accuracy",
                ),
                "endpoint_classification_accuracy": mean_present(
                    extraction,
                    "endpoint_classification_accuracy",
                ),
                "comparability_status_accuracy": mean_present(
                    extraction,
                    "comparability_field_accuracy",
                ),
                "mean_deterministic_field_rejections": statistics.fmean(
                    row["deterministic_field_rejection_count"]
                    for row in extraction
                ),
                "mean_deterministic_field_normalizations": statistics.fmean(
                    row["deterministic_field_normalization_count"]
                    for row in extraction
                ),
                "supported_source_dependent_claim_rate": mean_present(
                    sources,
                    "supported_source_dependent_claim_rate",
                ),
                "weighted_source_support_rate": mean_present(
                    sources,
                    "weighted_source_support_rate",
                ),
                "claim_citation_coverage_rate": mean_present(
                    sources,
                    "claim_citation_coverage_rate",
                ),
                "mean_unique_cited_sources": statistics.fmean(
                    row["unique_cited_sources"] for row in sources
                ),
                "peer_reviewed_primary_source_fraction_among_cited_sources": mean_present(
                    sources,
                    "peer_reviewed_primary_source_fraction_among_cited_sources",
                ),
                "valid_identifier_fraction_among_cited_sources": mean_present(
                    sources,
                    "valid_identifier_fraction_among_cited_sources",
                ),
                "anchor_exclusion_violations": sum(
                    row["anchor_exclusion_violation_count"]
                    for row in extraction
                )
                + sum(
                    row["anchor_exclusion_violation"] for row in sources
                ),
            }
        )

    calls = collect_call_records(run_dir)
    stage_costs: dict[tuple[str, str], dict[str, float]] = defaultdict(
        lambda: {
            "call_count": 0,
            "input_tokens": 0,
            "cached_input_tokens": 0,
            "output_tokens": 0,
            "total_tokens": 0,
            "web_search_calls": 0,
            "latency_seconds": 0.0,
            "estimated_cost_usd": 0.0,
        }
    )
    for call in calls:
        parts = Path(call["path"]).parts
        system = parts[1] if len(parts) > 1 else ""
        key = (system, str(call["stage"]))
        bucket = stage_costs[key]
        bucket["call_count"] += 1
        for field in (
            "input_tokens",
            "cached_input_tokens",
            "output_tokens",
            "total_tokens",
            "web_search_calls",
        ):
            bucket[field] += int(call.get(field, 0) or 0)
        for field in ("latency_seconds", "estimated_cost_usd"):
            bucket[field] += float(call.get(field, 0.0) or 0.0)
    cost_rows = [
        {"system": system, "stage": stage, **values}
        for (system, stage), values in sorted(stage_costs.items())
    ]

    summary_dir = run_dir / "summary"
    write_csv(summary_dir / "extraction_per_task.csv", extraction_rows)
    write_csv(summary_dir / "source_support_per_task.csv", source_rows)
    write_csv(summary_dir / "review_quality_per_task_repeat.csv", quality_rows)
    write_csv(summary_dir / "system_summary.csv", system_rows)
    write_csv(summary_dir / "cost_latency_by_stage.csv", cost_rows)
    write_json(
        summary_dir / "summary.json",
        {
            "status": "complete",
            "task_ids": [task["task_id"] for task in tasks],
            "systems": systems,
            "judge_repeats": repeats,
            "system_summary": system_rows,
            "total_paid_call_count": len(calls),
            "total_tracked_tokens": sum(
                int(call.get("total_tokens", 0) or 0) for call in calls
            ),
            "total_web_search_calls": sum(
                int(call.get("web_search_calls", 0) or 0) for call in calls
            ),
            "total_estimated_cost_usd": sum(
                float(call.get("estimated_cost_usd", 0.0) or 0.0)
                for call in calls
            ),
            "total_api_latency_seconds": sum(
                float(call.get("latency_seconds", 0.0) or 0.0)
                for call in calls
            ),
            "summary_input_hashes": {
                str(path.relative_to(run_dir)): sha256_file(path)
                for path in sorted(
                    [
                        *run_dir.glob(
                            "systems/*/*/professional_review.md"
                        ),
                        *run_dir.glob(
                            "systems/*/*/extracted_records.json"
                        ),
                        *run_dir.glob(
                            "systems/*/*/verified_records.json"
                        ),
                        *run_dir.glob(
                            "calls/*/*/review_source_support.json"
                        ),
                        *run_dir.glob(
                            "calls/*/*/review_judge/repeat_*.json"
                        ),
                    ]
                )
            },
        },
    )


def package_hashes() -> dict[str, str]:
    paths = [
        PACKAGE_ROOT / "input" / "review_tasks.jsonl",
        PACKAGE_ROOT / "input" / "review_task_ledgers.jsonl",
        PACKAGE_ROOT / "input" / "anchor_reviews.jsonl",
        PACKAGE_ROOT / "protocol.json",
        *sorted((PACKAGE_ROOT / "prompts").glob("*.txt")),
        *sorted((PACKAGE_ROOT / "schemas").glob("*.json")),
        *sorted((PACKAGE_ROOT / "scripts").glob("*.py")),
        *sorted((PACKAGE_ROOT / "tests").glob("test_*.py")),
        PACKAGE_ROOT / "config" / "pricing_2026-07-31.json",
    ]
    return {
        str(path.relative_to(PACKAGE_ROOT)): sha256_file(path) for path in paths
    }


def main() -> None:
    args = parse_args()
    if args.workers < 1:
        raise ValueError("--workers must be at least 1")
    if args.judge_repeats < 1:
        raise ValueError("--judge-repeats must be at least 1")
    run_dir = args.run_dir.expanduser().resolve()
    tasks, ledgers, anchors = selected_inputs(args.task_ids)
    enforce_paid_task_authorization(
        protocol=load_json(PACKAGE_ROOT / "protocol.json"),
        task_ids=[str(task["task_id"]) for task in tasks],
        stages=args.stages,
        allow_paid=args.allow_paid,
    )
    run_dir.mkdir(parents=True, exist_ok=True)
    systems = list(args.systems)
    stages = list(args.stages)
    api = ResumableOpenAI(allow_paid=args.allow_paid)
    manifest_path = run_dir / "run_manifest.json"
    config = {
        "protocol_id": "professional_pfas_review_v3_execution",
        "created_at": utc_now(),
        "package_root": str(PACKAGE_ROOT),
        "package_hashes": package_hashes(),
        "task_ids": [task["task_id"] for task in tasks],
        "systems": systems,
        "stages": stages,
        "model_alias": MODEL_ALIAS,
        "required_model_snapshot": MODEL_SNAPSHOT,
        "reasoning_effort": DEFAULT_REASONING_EFFORT,
        "local_candidate_screen_budget": DOCUMENT_BUDGET,
        "minimum_retained_sources": MIN_RETAINED_SOURCES,
        "web_candidate_screen_budget": WEB_CANDIDATE_BUDGET,
        "within_document_chunk_budget": CHUNKS_PER_DOCUMENT,
        "judge_repeats": args.judge_repeats,
        "workers": args.workers,
        "allow_paid": args.allow_paid,
        "status": "running",
    }
    execution_hash = sha256_text(canonical_json(config["package_hashes"]) + canonical_json({
        key: config[key]
        for key in (
            "task_ids",
            "systems",
            "model_alias",
            "required_model_snapshot",
            "reasoning_effort",
            "local_candidate_screen_budget",
            "minimum_retained_sources",
            "web_candidate_screen_budget",
            "within_document_chunk_budget",
            "judge_repeats",
        )
    }))
    config["execution_hash"] = execution_hash
    if manifest_path.exists():
        prior = load_json(manifest_path)
        if prior.get("execution_hash") != execution_hash:
            raise RuntimeError(
                "Existing run directory has a different execution hash"
            )
        config["created_at"] = prior["created_at"]
    write_json(manifest_path, config)
    started = time.perf_counter()

    try:
        if "retrieval" in stages:
            _local_retrieval(
                run_dir=run_dir,
                tasks=tasks,
                anchors=anchors,
                systems=systems,
                api=api,
                device=args.device,
                batch_size=args.bge_batch_size,
            )
            _web_retrieval(
                run_dir=run_dir,
                tasks=tasks,
                anchors=anchors,
                systems=systems,
                api=api,
            )
        if "extraction" in stages:
            _extract(
                run_dir=run_dir,
                tasks=tasks,
                anchors=anchors,
                systems=systems,
                api=api,
                workers=args.workers,
            )
        if "verification" in stages:
            _verify(
                run_dir=run_dir,
                tasks=tasks,
                anchors=anchors,
                systems=systems,
                api=api,
                workers=args.workers,
            )
        if "synthesis" in stages:
            _synthesize(
                run_dir=run_dir,
                tasks=tasks,
                ledgers=ledgers,
                anchors=anchors,
                systems=systems,
                api=api,
                workers=args.workers,
            )
        if "source_support" in stages:
            _source_support(
                run_dir=run_dir,
                tasks=tasks,
                anchors=anchors,
                systems=systems,
                api=api,
                workers=args.workers,
            )
        if "review_judge" in stages:
            _review_judge(
                run_dir=run_dir,
                tasks=tasks,
                ledgers=ledgers,
                systems=systems,
                api=api,
                workers=args.workers,
                repeats=args.judge_repeats,
            )
        if "summary" in stages:
            _summary(
                run_dir=run_dir,
                tasks=tasks,
                systems=systems,
                repeats=args.judge_repeats,
            )
    except Exception as exc:
        config["status"] = "failed"
        config["failed_at"] = utc_now()
        config["failure_type"] = type(exc).__name__
        config["failure_message"] = str(exc)
        config["wall_seconds_this_invocation"] = (
            time.perf_counter() - started
        )
        write_json(manifest_path, config)
        raise
    else:
        config["status"] = (
            "complete" if set(stages) == set(ALL_STAGES) else "partial"
        )
        config["completed_at"] = utc_now()
        config["wall_seconds_this_invocation"] = (
            time.perf_counter() - started
        )
        write_json(manifest_path, config)
    print(
        f"PASS: {config['status']} review experiment at {run_dir}",
        flush=True,
    )


if __name__ == "__main__":
    main()

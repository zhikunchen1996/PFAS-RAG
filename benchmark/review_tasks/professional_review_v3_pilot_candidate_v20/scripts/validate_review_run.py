#!/usr/bin/env python3
"""Validate a completed professional-review experiment run."""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

from filter_anchor_reviews import exclusion_reason, task_anchor_identifiers
from review_retrieval import (
    CHUNKS_PER_DOCUMENT,
    DOCUMENT_BUDGET,
    MIN_RETAINED_SOURCES,
)
from review_runtime import (
    MODEL_SNAPSHOT,
    PACKAGE_ROOT,
    canonical_json,
    collect_call_records,
    load_json,
    load_jsonl,
    sha256_file,
    sha256_text,
)
from run_review_experiment import (
    ALL_STAGES,
    ALL_SYSTEMS,
    DIRECT_SYSTEMS,
    all_locator_ids,
    is_comparability_status_assessment,
    is_endpoint_type_assessment,
    is_numeric_value_or_unit_assessment,
    package_hashes,
    normalize_record_citation_ids,
    normalize_quantitative_finding,
    quantitative_value_is_valid,
    required_metric_assessment_paths,
    sanitize_internal_review_notation,
)


CITATION_PATTERN = re.compile(
    r"\b((?:S|WEB)[0-9]{2})(?:-E[0-9]{2})?\b"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument(
        "--allow-partial",
        action="store_true",
        help="Validate available artifacts without requiring all stages.",
    )
    return parser.parse_args()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def expected_execution_hash(manifest: dict[str, Any]) -> str:
    fields = (
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
    return sha256_text(
        canonical_json(manifest["package_hashes"])
        + canonical_json({field: manifest[field] for field in fields})
    )


def validate_source_packet(
    *,
    packet: dict[str, Any],
    task_id: str,
    system: str,
    anchor_identifiers: dict[str, set[str]],
) -> None:
    sources = packet.get("sources")
    require(isinstance(sources, list), f"{task_id}/{system}: missing sources")
    require(
        MIN_RETAINED_SOURCES <= len(sources) <= DOCUMENT_BUDGET,
        f"{task_id}/{system}: expected {MIN_RETAINED_SOURCES} to "
        f"{DOCUMENT_BUDGET} sources, "
        f"found {len(sources)}",
    )
    prefix = "WEB" if system == "gpt51_web_search" else "S"
    expected_ids = [
        f"{prefix}{index:02d}" for index in range(1, len(sources) + 1)
    ]
    source_ids = [str(source.get("source_id") or "") for source in sources]
    require(
        source_ids == expected_ids,
        f"{task_id}/{system}: noncanonical source ids {source_ids}",
    )
    identities: set[str] = set()
    for source in sources:
        reason = exclusion_reason(source, anchor_identifiers)
        require(
            reason is None,
            f"{task_id}/{system}/{source['source_id']}: anchor hit {reason}",
        )
        identity = str(
            source.get("doi")
            or source.get("doi_or_stable_url")
            or source.get("title")
            or ""
        ).casefold()
        require(identity, f"{task_id}/{system}: empty source identity")
        require(
            identity not in identities,
            f"{task_id}/{system}: duplicate source identity {identity}",
        )
        identities.add(identity)
        chunks = source.get("evidence_chunks")
        require(
            isinstance(chunks, list) and bool(chunks),
            f"{task_id}/{system}/{source['source_id']}: no evidence chunks",
        )
        if system != "gpt51_web_search":
            require(
                len(chunks) == CHUNKS_PER_DOCUMENT,
                f"{task_id}/{system}/{source['source_id']}: expected "
                f"{CHUNKS_PER_DOCUMENT} chunks, found {len(chunks)}",
            )
        locators = [str(chunk.get("locator_id") or "") for chunk in chunks]
        require(
            len(locators) == len(set(locators)),
            f"{task_id}/{system}/{source['source_id']}: duplicate locators",
        )
        for chunk in chunks:
            require(
                bool(str(chunk.get("text") or "").strip()),
                f"{task_id}/{system}/{source['source_id']}: empty chunk",
            )
            if system != "gpt51_web_search":
                require(
                    isinstance(chunk.get("corpus_chunk"), int),
                    f"{task_id}/{system}/{source['source_id']}: "
                    "noninteger corpus chunk",
                )


def is_allowed_judge_repeat_duplicate(
    previous: dict[str, Any],
    current: dict[str, Any],
) -> bool:
    if (
        previous.get("stage") != "review_quality_judge"
        or current.get("stage") != "review_quality_judge"
    ):
        return False
    previous_key = str(previous.get("call_key") or "")
    current_key = str(current.get("call_key") or "")
    previous_match = re.fullmatch(r"(.+):r(\d+)", previous_key)
    current_match = re.fullmatch(r"(.+):r(\d+)", current_key)
    return bool(
        previous_match
        and current_match
        and previous_match.group(1) == current_match.group(1)
        and previous_match.group(2) != current_match.group(2)
    )


def validate_call_records(run_dir: Path) -> tuple[int, float]:
    calls = collect_call_records(run_dir)
    require(calls, "No paid-call records found")
    seen_hashes: dict[str, dict[str, Any]] = {}
    seen_response_ids: set[str] = set()
    for path in sorted((run_dir / "calls").rglob("*.json")):
        record = load_json(path)
        if not isinstance(record.get("request"), dict):
            continue
        request_hash = sha256_text(canonical_json(record["request"]))
        require(
            record.get("request_hash") == request_hash,
            f"{path}: request hash mismatch",
        )
        if record.get("result_kind") in {"json", "text", "web_json"}:
            previous = seen_hashes.get(request_hash)
            require(
                previous is None
                or is_allowed_judge_repeat_duplicate(previous, record),
                f"{path}: duplicate successful request hash",
            )
            seen_hashes.setdefault(request_hash, record)
        metadata = record.get("response_metadata")
        if isinstance(metadata, dict):
            response_id = str(metadata.get("response_id") or "")
            require(response_id, f"{path}: missing response id")
            require(
                response_id not in seen_response_ids,
                f"{path}: duplicate response id",
            )
            seen_response_ids.add(response_id)
            require(
                metadata.get("response_model") == MODEL_SNAPSHOT,
                f"{path}: unexpected model snapshot",
            )
            require(
                int(metadata.get("total_tokens", 0)) > 0,
                f"{path}: missing token usage",
            )
            require(
                float(metadata.get("latency_seconds", 0.0)) >= 0.0,
                f"{path}: invalid latency",
            )
            require(
                float(metadata.get("estimated_cost_usd", 0.0)) >= 0.0,
                f"{path}: invalid cost",
            )
    return (
        len(calls),
        sum(float(call.get("estimated_cost_usd", 0.0)) for call in calls),
    )


def validate_required_assessments(
    *,
    record: dict[str, Any],
    verification: dict[str, Any],
    label: str,
) -> None:
    expected = required_metric_assessment_paths(record)
    paths = [
        str(item.get("field_path") or "")
        for item in verification.get("field_assessments", [])
    ]
    counts = Counter(paths)
    missing = sorted(expected - set(paths))
    require(not missing, f"{label}: missing required assessments {missing}")
    duplicated = sorted(path for path in expected if counts[path] != 1)
    require(
        not duplicated,
        f"{label}: required assessments must occur once {duplicated}",
    )
    metric_like = {
        path
        for item, path in zip(
            verification.get("field_assessments", []),
            paths,
            strict=True,
        )
        if (
            is_numeric_value_or_unit_assessment(item)
            or is_endpoint_type_assessment(item)
            or is_comparability_status_assessment(item)
        )
    }
    unexpected = sorted(metric_like - expected)
    require(
        not unexpected,
        f"{label}: assessments reference nonexistent metric fields "
        f"{unexpected}",
    )


def validate_extraction_artifacts(
    *,
    packet: dict[str, Any],
    extracted: dict[str, Any],
    verified: dict[str, Any],
    task_id: str,
    system: str,
) -> None:
    label = f"{task_id}/{system}"
    source_map = {
        str(source["source_id"]): source for source in packet["sources"]
    }
    records = extracted.get("records")
    require(isinstance(records, list), f"{label}: missing extracted records")
    record_ids = [str(record.get("record_id") or "") for record in records]
    require(
        all(record_ids) and len(record_ids) == len(set(record_ids)),
        f"{label}: empty or duplicate record ids",
    )
    record_map = dict(zip(record_ids, records, strict=True))
    for record in records:
        record_id = str(record["record_id"])
        source_id = str(record.get("source_id") or "")
        require(
            source_id in source_map,
            f"{label}/{record_id}: unknown source id {source_id}",
        )
        valid_locators = {
            str(chunk["locator_id"])
            for chunk in source_map[source_id]["evidence_chunks"]
        }
        locators = all_locator_ids(record)
        require(
            bool(locators) and locators.issubset(valid_locators),
            f"{label}/{record_id}: empty or unknown evidence locators",
        )
        require(
            all(
                quantitative_value_is_valid(finding)
                for finding in record["quantitative_findings"]
            ),
            f"{label}/{record_id}: malformed retained quantitative value",
        )
    for rejection in extracted.get("deterministic_field_rejections", []):
        require(
            normalize_quantitative_finding(rejection["finding"])[0] is None,
            f"{label}: deterministic rejection contains a valid value",
        )
    for normalization in extracted.get(
        "deterministic_field_normalizations",
        [],
    ):
        before = normalization["before"]
        after = normalization["after"]
        expected_after, expected_reason = normalize_quantitative_finding(
            before
        )
        require(
            expected_after == after
            and expected_reason == normalization.get("reason")
            and before != after
            and quantitative_value_is_valid(after),
            f"{label}: invalid deterministic field normalization",
        )

    verifications = verified.get("all_verifications")
    require(
        isinstance(verifications, list)
        and len(verifications) == len(records),
        f"{label}: extraction/verification count mismatch",
    )
    verification_ids = [
        str(item.get("record_id") or "") for item in verifications
    ]
    require(
        len(verification_ids) == len(set(verification_ids))
        and set(verification_ids) == set(record_ids),
        f"{label}: verification record ids do not match extraction",
    )
    verification_map = dict(
        zip(verification_ids, verifications, strict=True)
    )
    for record_id, record in record_map.items():
        validate_required_assessments(
            record=record,
            verification=verification_map[record_id],
            label=f"{label}/{record_id}",
        )

    expected_usable = {
        record_id
        for record_id, verification in verification_map.items()
        if verification.get("record_usable")
        and not verification.get("anchor_exclusion_violation")
    }
    retained = verified.get("verified_records")
    require(
        isinstance(retained, list),
        f"{label}: missing verified-record list",
    )
    actual_usable: list[str] = []
    for item in retained:
        record_id = str(item.get("record", {}).get("record_id") or "")
        require(
            record_id in record_map,
            f"{label}: retained unknown record {record_id}",
        )
        require(
            item["record"] == record_map[record_id]
            and item["verification"] == verification_map[record_id],
            f"{label}/{record_id}: retained record/verification drift",
        )
        actual_usable.append(record_id)
    require(
        len(actual_usable) == len(set(actual_usable))
        and set(actual_usable) == expected_usable,
        f"{label}: retained usable records do not match verification",
    )


def expected_summary_hashes(run_dir: Path) -> dict[str, str]:
    paths = sorted(
        [
            *run_dir.glob("systems/*/*/professional_review.md"),
            *run_dir.glob("systems/*/*/extracted_records.json"),
            *run_dir.glob("systems/*/*/verified_records.json"),
            *run_dir.glob("calls/*/*/review_source_support.json"),
            *run_dir.glob("calls/*/*/review_judge/repeat_*.json"),
        ]
    )
    return {
        str(path.relative_to(run_dir)): sha256_file(path) for path in paths
    }


def validate_direct_no_evidence_artifacts(
    *,
    run_dir: Path,
    task_dir: Path,
    task_id: str,
    system: str,
) -> None:
    for forbidden_name in (
        "sources.json",
        "extracted_records.json",
        "verified_records.json",
    ):
        require(
            not (task_dir / forbidden_name).exists(),
            f"{task_id}/{system}: Direct must not contain {forbidden_name}",
        )
    require(
        not (
            run_dir
            / "calls"
            / system
            / task_id
            / "review_source_support.json"
        ).exists(),
        f"{task_id}/{system}: Direct must not have source judge",
    )


def validate_direct_review(review: str, *, task_id: str, system: str) -> None:
    citations = CITATION_PATTERN.findall(review)
    require(
        not citations,
        f"{task_id}/{system}: Direct used benchmark citations",
    )


def validate_complete_run(run_dir: Path, manifest: dict[str, Any]) -> None:
    tasks = {
        record["task_id"]: record
        for record in load_jsonl(PACKAGE_ROOT / "input" / "review_tasks.jsonl")
    }
    anchors = load_jsonl(PACKAGE_ROOT / "input" / "anchor_reviews.jsonl")
    repeats = int(manifest["judge_repeats"])
    for task_id in manifest["task_ids"]:
        require(task_id in tasks, f"Unknown task in run: {task_id}")
        identifiers = task_anchor_identifiers(anchors, task_id)
        for system in manifest["systems"]:
            require(system in ALL_SYSTEMS, f"Unknown system in run: {system}")
            task_dir = run_dir / "systems" / system / task_id
            is_direct = system in DIRECT_SYSTEMS
            if is_direct:
                validate_direct_no_evidence_artifacts(
                    run_dir=run_dir,
                    task_dir=task_dir,
                    task_id=task_id,
                    system=system,
                )
                packet = {"sources": []}
            else:
                packet = load_json(task_dir / "sources.json")
                validate_source_packet(
                    packet=packet,
                    task_id=task_id,
                    system=system,
                    anchor_identifiers=identifiers,
                )
                extracted = load_json(task_dir / "extracted_records.json")
                verified = load_json(task_dir / "verified_records.json")
                require(
                    extracted.get("task_id") == task_id,
                    f"{task_id}/{system}: extracted task mismatch",
                )
                require(
                    verified.get("task_id") == task_id,
                    f"{task_id}/{system}: verified task mismatch",
                )
                validate_extraction_artifacts(
                    packet=packet,
                    extracted=extracted,
                    verified=verified,
                    task_id=task_id,
                    system=system,
                )
            review_path = task_dir / "professional_review.md"
            review = review_path.read_text(encoding="utf-8")
            synthesis_call = load_json(
                run_dir
                / "calls"
                / system
                / task_id
                / "review_synthesis.json"
            )
            raw_review = synthesis_call["result"].strip()
            expected_review, expected_removed = (
                sanitize_internal_review_notation(raw_review)
            )
            expected_review, expected_normalized_citations = (
                normalize_record_citation_ids(expected_review)
            )
            expected_review = expected_review.strip() + "\n"
            require(
                review == expected_review,
                f"{task_id}/{system}: synthesis postprocessing drift",
            )
            postprocessing = load_json(
                task_dir / "synthesis_postprocessing.json"
            )
            require(
                postprocessing.get("synthesis_request_hash")
                == synthesis_call["request_hash"]
                and postprocessing.get("raw_review_sha256")
                == sha256_text(raw_review)
                and postprocessing.get("final_review_sha256")
                == sha256_text(review)
                and postprocessing.get("removed_internal_notation_spans")
                == expected_removed
                and postprocessing.get("normalized_record_citations")
                == expected_normalized_citations,
                f"{task_id}/{system}: invalid synthesis postprocessing audit",
            )
            require(
                len(review.split()) >= 100,
                f"{task_id}/{system}: review unexpectedly short",
            )
            known = {
                str(source["source_id"]) for source in packet["sources"]
            }
            citations = CITATION_PATTERN.findall(review)
            if is_direct:
                validate_direct_review(
                    review,
                    task_id=task_id,
                    system=system,
                )
            else:
                require(
                    citations,
                    f"{task_id}/{system}: no bracketed citations",
                )
                require(
                    set(citations).issubset(known),
                    f"{task_id}/{system}: unknown citations "
                    f"{sorted(set(citations) - known)}",
                )
                support = load_json(
                    run_dir
                    / "calls"
                    / system
                    / task_id
                    / "review_source_support.json"
                )
                require(
                    support["result"].get("task_id") == task_id,
                    f"{task_id}/{system}: source-support task mismatch",
                )
                require(
                    not support["result"].get(
                        "anchor_exclusion_violation"
                    ),
                    f"{task_id}/{system}: source judge found anchor violation",
                )
                require(
                    not support["result"].get("unknown_source_ids"),
                    f"{task_id}/{system}: source judge found unknown citations",
                )
            for repeat in range(1, repeats + 1):
                judgment = load_json(
                    run_dir
                    / "calls"
                    / system
                    / task_id
                    / "review_judge"
                    / f"repeat_{repeat}.json"
                )
                require(
                    judgment["result"].get("task_id") == task_id,
                    f"{task_id}/{system}/r{repeat}: judge task mismatch",
                )

    summary = load_json(run_dir / "summary" / "summary.json")
    require(summary.get("status") == "complete", "Summary is not complete")
    require(
        summary.get("summary_input_hashes") == expected_summary_hashes(run_dir),
        "Summary input hashes do not match current artifacts",
    )
    calls, total_cost = validate_call_records(run_dir)
    require(
        int(summary.get("total_paid_call_count", -1)) == calls,
        "Summary paid-call count mismatch",
    )
    require(
        math.isclose(
            float(summary.get("total_estimated_cost_usd", -1.0)),
            total_cost,
            rel_tol=0.0,
            abs_tol=1e-9,
        ),
        "Summary cost does not equal call-record cost",
    )
    require(
        all(
            int(row.get("anchor_exclusion_violations", 0)) == 0
            for row in summary.get("system_summary", [])
        ),
        "System summary contains an anchor-exclusion violation",
    )


def main() -> None:
    args = parse_args()
    run_dir = args.run_dir.expanduser().resolve()
    manifest = load_json(run_dir / "run_manifest.json")
    require(
        manifest.get("package_hashes") == package_hashes(),
        "Run package hashes do not match the current package",
    )
    require(
        manifest.get("execution_hash") == expected_execution_hash(manifest),
        "Execution hash mismatch",
    )
    require(
        manifest.get("required_model_snapshot") == MODEL_SNAPSHOT,
        "Run requires an unexpected model snapshot",
    )
    if args.allow_partial:
        require(
            manifest.get("status") in {"partial", "failed", "complete"},
            f"Unexpected partial-run status {manifest.get('status')!r}",
        )
        validate_call_records(run_dir)
        print(f"PASS: validated available call records in {run_dir}")
        return
    require(
        manifest.get("status") == "complete",
        f"Run status is {manifest.get('status')!r}, not complete",
    )
    require(
        set(manifest.get("stages", [])) == set(ALL_STAGES),
        "Run does not contain the full stage set",
    )
    validate_complete_run(run_dir, manifest)
    print(f"PASS: completed professional-review run validated at {run_dir}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc

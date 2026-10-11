#!/usr/bin/env python3
"""Deterministically remove task-specific anchor reviews from source records."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


DOI_PATTERN = re.compile(r"10\.\d{4,9}/[-._;()/:a-z0-9]+", re.IGNORECASE)


def normalize_doi(value: object) -> str:
    text = str(value or "").strip().lower()
    for prefix in (
        "https://doi.org/",
        "http://doi.org/",
        "https://dx.doi.org/",
        "http://dx.doi.org/",
        "doi:",
    ):
        if text.startswith(prefix):
            text = text[len(prefix) :]
            break
    match = DOI_PATTERN.search(text)
    if not match:
        return ""
    return match.group(0).rstrip(".,;)]}")


def normalize_url(value: object) -> str:
    text = str(value or "").strip()
    if not text:
        return ""
    doi = normalize_doi(text)
    if doi:
        return f"https://doi.org/{doi}"
    parsed = urlsplit(text)
    if not parsed.netloc:
        return text.casefold().rstrip("/")
    normalized = parsed._replace(
        scheme=parsed.scheme.lower() or "https",
        netloc=parsed.netloc.lower(),
        fragment="",
    )
    return urlunsplit(normalized).rstrip("/")


def normalize_title(value: object) -> str:
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").casefold()).strip()


def normalize_source(value: object) -> str:
    return Path(str(value or "")).name.casefold().strip()


def load_jsonl(path: Path) -> list[dict]:
    records = []
    for line_number, line in enumerate(path.read_text().splitlines(), start=1):
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_number}: invalid JSON") from exc
    return records


def task_anchor_identifiers(anchor_records: list[dict], task_id: str) -> dict:
    task_record = next(
        (record for record in anchor_records if record["task_id"] == task_id),
        None,
    )
    if task_record is None:
        raise KeyError(f"No anchor record found for task {task_id}")

    anchors = [task_record["primary_anchor"], *task_record["supplemental_anchors"]]
    return {
        "anchor_ids": {anchor["anchor_id"] for anchor in anchors},
        "dois": {
            normalized
            for anchor in anchors
            for value in [
                anchor.get("doi"),
                *(anchor.get("alternate_dois") or []),
            ]
            if (normalized := normalize_doi(value))
        },
        "urls": {
            normalized
            for anchor in anchors
            for value in [
                anchor.get("url"),
                *(anchor.get("alternate_urls") or []),
            ]
            if (normalized := normalize_url(value))
        },
        "titles": {
            normalized
            for anchor in anchors
            for value in [
                anchor.get("title"),
                *(anchor.get("alternate_titles") or []),
            ]
            if (normalized := normalize_title(value))
        },
        "sources": {
            normalized
            for anchor in anchors
            if (normalized := normalize_source(anchor.get("corpus_source")))
        },
    }


def record_identifiers(record: dict) -> dict[str, str]:
    metadata = record.get("metadata")
    if not isinstance(metadata, dict):
        metadata = {}

    def first_value(*keys: str) -> object:
        for key in keys:
            value = record.get(key)
            if value not in (None, ""):
                return value
            value = metadata.get(key)
            if value not in (None, ""):
                return value
        return ""

    doi_value = first_value("doi", "DOI", "doi_or_stable_url")
    url_value = first_value("url", "source_url", "doi_or_stable_url")
    return {
        "doi": normalize_doi(doi_value) or normalize_doi(url_value),
        "url": normalize_url(url_value),
        "title": normalize_title(first_value("title")),
        "source": normalize_source(first_value("source", "corpus_source")),
    }


def exclusion_reason(record: dict, identifiers: dict) -> str | None:
    candidate = record_identifiers(record)
    if candidate["doi"] and candidate["doi"] in identifiers["dois"]:
        return f"anchor_doi:{candidate['doi']}"
    if candidate["source"] and candidate["source"] in identifiers["sources"]:
        return f"anchor_source:{candidate['source']}"
    if candidate["url"] and candidate["url"] in identifiers["urls"]:
        return f"anchor_url:{candidate['url']}"
    if candidate["title"] and candidate["title"] in identifiers["titles"]:
        return f"anchor_title:{candidate['title']}"
    return None


def filter_records(records: list[dict], identifiers: dict) -> tuple[list[dict], list[dict]]:
    kept = []
    removed = []
    for record in records:
        reason = exclusion_reason(record, identifiers)
        if reason is None:
            kept.append(record)
            continue
        removed.append(
            {
                "reason": reason,
                "record_identifiers": record_identifiers(record),
                "record": record,
            }
        )
    return kept, removed


def write_jsonl(path: Path, records: list[dict]) -> None:
    path.write_text(
        "".join(json.dumps(record, ensure_ascii=True) + "\n" for record in records)
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--task-id", required=True)
    parser.add_argument("--anchors", type=Path, required=True)
    parser.add_argument("--input-jsonl", type=Path, required=True)
    parser.add_argument("--output-jsonl", type=Path, required=True)
    parser.add_argument("--audit-json", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    anchors = load_jsonl(args.anchors)
    records = load_jsonl(args.input_jsonl)
    identifiers = task_anchor_identifiers(anchors, args.task_id)
    kept, removed = filter_records(records, identifiers)

    args.output_jsonl.parent.mkdir(parents=True, exist_ok=True)
    args.audit_json.parent.mkdir(parents=True, exist_ok=True)
    write_jsonl(args.output_jsonl, kept)
    args.audit_json.write_text(
        json.dumps(
            {
                "task_id": args.task_id,
                "input_records": len(records),
                "kept_records": len(kept),
                "removed_records": len(removed),
                "anchor_ids": sorted(identifiers["anchor_ids"]),
                "removed": removed,
            },
            indent=2,
            ensure_ascii=True,
        )
        + "\n"
    )
    print(
        f"PASS: {args.task_id}: kept {len(kept)} and removed {len(removed)} "
        "task-scoped anchor records."
    )


if __name__ == "__main__":
    main()

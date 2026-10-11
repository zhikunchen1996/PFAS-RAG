from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
import hashlib
import itertools
import json
from pathlib import Path
import re
from typing import Any

import chromadb


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def normalized_text(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip().lower()


def compact_text(value: str) -> str:
    return re.sub(r"\s+", "", value or "").lower()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate the repaired PFAS corpus.")
    parser.add_argument("--manifest", default="corpus/corpus434_repaired_v1/raw_manifest.csv")
    parser.add_argument("--active-manifest", default="data/raw_manifest.csv")
    parser.add_argument("--corrections", default="corpus/corpus434_repaired_v1/corrections.json")
    parser.add_argument("--chroma-path", default="data/chroma")
    parser.add_argument("--gold", default="benchmark/frozen_v3/gold/chunk_based_gold.jsonl")
    parser.add_argument("--output", default="corpus/corpus434_repaired_v1/validation_report.json")
    args = parser.parse_args()

    manifest_path = PROJECT_ROOT / args.manifest
    active_manifest_path = PROJECT_ROOT / args.active_manifest
    corrections = json.loads((PROJECT_ROOT / args.corrections).read_text(encoding="utf-8"))
    with manifest_path.open(encoding="utf-8-sig", newline="") as handle:
        manifest_rows = list(csv.DictReader(handle))
    manifest_by_source = {row["source"]: row for row in manifest_rows}

    doi_sources: dict[str, list[str]] = defaultdict(list)
    for row in manifest_rows:
        doi_sources[row.get("doi", "").strip().lower()].append(row["source"])
    duplicate_dois = {
        doi: sources for doi, sources in doi_sources.items() if doi and len(sources) > 1
    }

    client = chromadb.PersistentClient(path=str(PROJECT_ROOT / args.chroma_path))
    source_collection = client.get_collection(corrections["source_collection"])
    collection = client.get_collection(corrections["target_collection"])
    data = collection.get(include=["documents", "metadatas", "embeddings"])
    source_data = source_collection.get(include=["metadatas"])

    chunks_by_source: dict[str, list[tuple[int, str]]] = defaultdict(list)
    chunk_lookup: dict[tuple[str, str], str] = {}
    chunk_hashes: dict[str, set[bytes]] = defaultdict(set)
    for document, metadata in zip(data["documents"], data["metadatas"]):
        source = str(metadata.get("source") or "")
        chunk = int(metadata.get("chunk") or 0)
        chunks_by_source[source].append((chunk, document))
        chunk_lookup[(source, str(chunk))] = document
        digest = hashlib.sha1(normalized_text(document).encode("utf-8")).digest()
        chunk_hashes[source].add(digest)

    inverted: dict[bytes, list[str]] = defaultdict(list)
    for source, hashes in chunk_hashes.items():
        for digest in hashes:
            inverted[digest].append(source)
    shared_chunks: Counter[tuple[str, str]] = Counter()
    for sources in inverted.values():
        for pair in itertools.combinations(sorted(sources), 2):
            shared_chunks[pair] += 1
    near_duplicates = []
    for (left, right), shared in shared_chunks.items():
        similarity = shared / len(chunk_hashes[left] | chunk_hashes[right])
        if shared >= 5 and similarity >= 0.15:
            near_duplicates.append(
                {
                    "left": left,
                    "right": right,
                    "shared_exact_chunks": shared,
                    "chunk_jaccard": similarity,
                }
            )

    front_doi_checked = 0
    front_doi_mismatches = []
    doi_pattern = re.compile(r"10\s*\.\s*\d{4,9}\s*/", re.IGNORECASE)
    for source, chunks in chunks_by_source.items():
        front_text = " ".join(text for _, text in sorted(chunks) if _ <= 4)
        doi = manifest_by_source[source].get("doi", "").strip().lower()
        if doi and doi_pattern.search(front_text):
            front_doi_checked += 1
            if compact_text(doi) not in compact_text(front_text):
                front_doi_mismatches.append(source)

    gold = [
        json.loads(line)
        for line in (PROJECT_ROOT / args.gold).read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    missing_gold_chunks = []
    missing_gold_spans = []
    for row in gold:
        key = (str(row["doc_id"]), str(row["chunk_id"]))
        text = chunk_lookup.get(key)
        if text is None:
            missing_gold_chunks.append({"question_id": row["question_id"], "key": key})
            continue
        span = str(row.get("exact_evidence_span") or "")
        if span and span not in text and normalized_text(span) not in normalized_text(text):
            missing_gold_spans.append({"question_id": row["question_id"], "key": key})

    removed_sources = {item["source"] for item in corrections["remove_sources"]}
    source_removed_ids = {
        item_id
        for item_id, metadata in zip(source_data["ids"], source_data["metadatas"])
        if str(metadata.get("source") or "") in removed_sources
    }
    source_ids = set(source_data["ids"])
    target_ids = set(data["ids"])
    actual_removed_ids = source_ids - target_ids
    unexpected_new_ids = target_ids - source_ids

    embedding_config = collection.configuration_json.get("embedding_function", {})
    vector_result = collection.query(
        query_embeddings=[data["embeddings"][0]],
        n_results=1,
        include=["distances"],
    )
    vector_top_distance = float(vector_result["distances"][0][0])

    report: dict[str, Any] = {
        "version": corrections["version"],
        "manifest_sha256": sha256(manifest_path),
        "active_manifest_sha256": sha256(active_manifest_path),
        "active_manifest_matches_versioned_manifest": sha256(manifest_path)
        == sha256(active_manifest_path),
        "manifest_records": len(manifest_rows),
        "collection_chunks": collection.count(),
        "collection_unique_sources": len(chunks_by_source),
        "duplicate_doi_groups": duplicate_dois,
        "near_duplicate_pairs": near_duplicates,
        "front_doi_records_checked": front_doi_checked,
        "front_doi_mismatches": front_doi_mismatches,
        "gold_records": len(gold),
        "gold_chunk_resolution_failures": missing_gold_chunks,
        "gold_span_resolution_failures": missing_gold_spans,
        "expected_removed_chunk_ids": len(source_removed_ids),
        "actual_removed_chunk_ids": len(actual_removed_ids),
        "removed_ids_match_expected": actual_removed_ids == source_removed_ids,
        "unexpected_new_ids": len(unexpected_new_ids),
        "embedding_function": embedding_config,
        "vector_query_top_distance": vector_top_distance,
    }
    failures = []
    if len(manifest_rows) != 434 or collection.count() != 29805 or len(chunks_by_source) != 434:
        failures.append("unexpected corpus counts")
    if duplicate_dois or near_duplicates:
        failures.append("duplicate records remain")
    if front_doi_mismatches:
        failures.append("front-matter DOI mismatch remains")
    if missing_gold_chunks or missing_gold_spans:
        failures.append("frozen249 gold does not fully resolve")
    if not report["active_manifest_matches_versioned_manifest"]:
        failures.append("active manifest differs from versioned repaired manifest")
    if actual_removed_ids != source_removed_ids or unexpected_new_ids:
        failures.append("retained Chroma IDs changed")
    if embedding_config.get("name") != "sentence_transformer" or vector_top_distance > 1e-6:
        failures.append("embedding configuration or vector query failed")
    report["validation_failures"] = failures
    report["validation_passed"] = not failures

    output_path = PROJECT_ROOT / args.output
    output_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(bool(failures))


if __name__ == "__main__":
    main()

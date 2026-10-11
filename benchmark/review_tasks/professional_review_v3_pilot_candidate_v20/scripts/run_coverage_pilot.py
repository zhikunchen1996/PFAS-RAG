#!/usr/bin/env python3
"""Run a no-API dense-retrieval coverage pilot after anchor exclusion."""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from src.rag_app.config import get_settings
from src.rag_app.ingest import get_collection


REVIEW_TITLE_MARKERS = (
    " review",
    "review ",
    "a review of",
    "critical review",
    "systematic review",
    "meta-analysis",
    "perspective",
    "state of the art",
)


def load_jsonl(path: Path) -> list[dict]:
    return [
        json.loads(line)
        for line in path.read_text().splitlines()
        if line.strip()
    ]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "coverage_pilot",
    )
    parser.add_argument("--chunks-per-query", type=int, default=100)
    parser.add_argument("--reported-docs", type=int, default=30)
    return parser.parse_args()


def is_likely_review(
    title: str,
    source: str,
    front_matter: str,
    known_review_sources: set[str],
) -> bool:
    if source in known_review_sources:
        return True
    folded = f" {title.casefold()} "
    if any(marker in folded for marker in REVIEW_TITLE_MARKERS):
        return True
    front = f" {' '.join(front_matter.split()).casefold()[:900]} "
    return any(
        marker in front
        for marker in (
            " review article ",
            " review a review ",
            " critical review ",
            " systematic review ",
            " current opinion ",
        )
    )


def task_queries(task: dict) -> list[tuple[str, str]]:
    return [
        ("umbrella", f"{task['title']}. {task['review_brief']}"),
        *[
            (component["component_id"], component["requirement"])
            for component in task["components"]
        ],
    ]


def main() -> None:
    args = parse_args()
    tasks = load_jsonl(ROOT / "input" / "review_tasks.jsonl")
    anchors = {
        record["task_id"]: record["primary_anchor"]
        for record in load_jsonl(ROOT / "input" / "anchor_reviews.jsonl")
    }
    known_review_sources = {
        anchor["corpus_source"] for anchor in anchors.values()
    }

    settings = get_settings()
    collection = get_collection(settings)
    corpus = collection.get(include=["documents", "metadatas"])
    front_matter_by_source: dict[str, tuple[int, str]] = {}
    chunk_count_by_source: dict[str, int] = {}
    for text, metadata in zip(corpus["documents"], corpus["metadatas"]):
        source = str(metadata.get("source") or "")
        chunk = int(metadata.get("chunk", 0))
        chunk_count_by_source[source] = chunk_count_by_source.get(source, 0) + 1
        previous = front_matter_by_source.get(source)
        if previous is None or chunk < previous[0]:
            front_matter_by_source[source] = (chunk, text)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    detail_path = args.output_dir / "coverage_details.jsonl"
    summary_path = args.output_dir / "coverage_summary.csv"

    started = time.perf_counter()
    detail_records = []
    summary_rows = []
    for task in tasks:
        task_id = task["task_id"]
        anchor = anchors[task_id]
        documents: dict[str, dict] = {}
        anchor_query_hits_after_filter = 0

        queries = task_queries(task)
        results = collection.query(
            query_texts=[query for _, query in queries],
            n_results=args.chunks_per_query,
            where={"source": {"$ne": anchor["corpus_source"]}},
            include=["documents", "metadatas", "distances"],
        )
        for query_index, (query_id, query_text) in enumerate(queries):
            for rank, (text, metadata, distance) in enumerate(
                zip(
                    results["documents"][query_index],
                    results["metadatas"][query_index],
                    results["distances"][query_index],
                ),
                start=1,
            ):
                source = str(metadata.get("source") or "")
                if source == anchor["corpus_source"]:
                    anchor_query_hits_after_filter += 1
                    continue
                if str(metadata.get("section") or "").casefold() == "references":
                    continue
                record = documents.setdefault(
                    source,
                    {
                        "source": source,
                        "title": str(metadata.get("title") or source),
                        "doi": str(metadata.get("doi") or ""),
                        "year": str(metadata.get("year") or ""),
                        "rrf_score": 0.0,
                        "best_distance": float(distance),
                        "query_ids": set(),
                        "top_chunks": [],
                    },
                )
                record["rrf_score"] += 1.0 / (60 + rank)
                record["best_distance"] = min(
                    record["best_distance"],
                    float(distance),
                )
                record["query_ids"].add(query_id)
                if len(record["top_chunks"]) < 3:
                    record["top_chunks"].append(
                        {
                            "query_id": query_id,
                            "rank": rank,
                            "chunk": metadata.get("chunk"),
                            "section": metadata.get("section"),
                            "preview": " ".join(text.split())[:500],
                        }
                    )

        ranked = sorted(
            documents.values(),
            key=lambda item: (
                -item["rrf_score"],
                item["best_distance"],
                item["source"],
            ),
        )
        for rank, record in enumerate(ranked, start=1):
            record["document_rank"] = rank
            record["query_ids"] = sorted(record["query_ids"])
            record["query_coverage"] = len(record["query_ids"])
            record["likely_review"] = is_likely_review(
                record["title"],
                record["source"],
                front_matter_by_source.get(record["source"], (0, ""))[1],
                known_review_sources,
            )

        reported = ranked[: args.reported_docs]
        top20 = ranked[:20]
        top20_primary = [
            record for record in top20 if not record["likely_review"]
        ]
        covered_queries = {
            query_id
            for record in top20_primary
            for query_id in record["query_ids"]
        }
        detail_records.append(
            {
                "task_id": task_id,
                "anchor_source": anchor["corpus_source"],
                "anchor_doi": anchor["doi"],
                "query_count": len(queries),
                "chunks_per_query": args.chunks_per_query,
                "anchor_chunks_in_corpus": chunk_count_by_source[
                    anchor["corpus_source"]
                ],
                "anchor_query_hits_after_filter": anchor_query_hits_after_filter,
                "unique_nonanchor_documents": len(ranked),
                "likely_primary_documents_top20": len(top20_primary),
                "queries_with_likely_primary_top20": sorted(covered_queries),
                "reported_documents": reported,
            }
        )
        summary_rows.append(
            {
                "task_id": task_id,
                "anchor_chunks_in_corpus": chunk_count_by_source[
                    anchor["corpus_source"]
                ],
                "anchor_query_hits_after_filter": anchor_query_hits_after_filter,
                "unique_nonanchor_documents": len(ranked),
                "likely_primary_documents_top10": sum(
                    not record["likely_review"] for record in ranked[:10]
                ),
                "likely_primary_documents_top20": len(top20_primary),
                "query_coverage_top20": len(covered_queries),
                "query_count": len(queries),
            }
        )

    detail_path.write_text(
        "".join(
            json.dumps(record, ensure_ascii=True) + "\n"
            for record in detail_records
        )
    )
    with summary_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(summary_rows[0]))
        writer.writeheader()
        writer.writerows(summary_rows)

    elapsed = time.perf_counter() - started
    (args.output_dir / "run_manifest.json").write_text(
        json.dumps(
            {
                "status": "coverage_only_no_paid_calls",
                "collection": settings.collection_name,
                "embedding_model": settings.embedding_model,
                "embedding_device": settings.embedding_device,
                "chunks_per_query": args.chunks_per_query,
                "reported_docs": args.reported_docs,
                "elapsed_seconds": elapsed,
                "candidate_reviews_or_scores_viewed": False,
            },
            indent=2,
        )
        + "\n"
    )
    print(
        f"PASS: wrote coverage-only results for {len(tasks)} tasks in "
        f"{elapsed:.1f} seconds."
    )


if __name__ == "__main__":
    main()

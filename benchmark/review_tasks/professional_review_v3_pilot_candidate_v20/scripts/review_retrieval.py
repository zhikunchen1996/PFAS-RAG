#!/usr/bin/env python3
"""Deterministic local retrieval for the professional-review experiment."""

from __future__ import annotations

import math
import os
import sys
import time
from dataclasses import replace
from pathlib import Path
from typing import Any

from sentence_transformers import CrossEncoder

from filter_anchor_reviews import exclusion_reason, task_anchor_identifiers
from review_runtime import PACKAGE_ROOT, PROJECT_ROOT


SRC = PROJECT_ROOT / "src"
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from src.rag_app.config import get_settings  # noqa: E402
from src.rag_app.ingest import get_collection  # noqa: E402
from src.rag_app.rag import is_reference_like  # noqa: E402


BGE_RERANKER_MODEL = "BAAI/bge-reranker-base"
EXPECTED_COLLECTION = (
    "rag_documents_bge_large_en_v1_5_sent256_overlap2_"
    "corpus434_repaired_v1"
)
EXPECTED_EMBEDDING_MODEL = "BAAI/bge-large-en-v1.5"
QUERY_CHUNK_BUDGET = 100
RRF_K = 60
DOCUMENT_RERANK_POOL = 30
LLM_SELECTOR_POOL = 20
DOCUMENT_BUDGET = 20
MIN_RETAINED_SOURCES = 6
CHUNKS_PER_DOCUMENT = 8
BGE_MAX_LENGTH = 512
DOCUMENT_CARD_MAX_CHARS = 4200
CHUNK_MAX_CHARS = 2600

REVIEW_TITLE_MARKERS = (
    " review",
    "review ",
    "a review of",
    "critical review",
    "systematic review",
    "meta-analysis",
    "perspective",
    "state of the art",
    "current opinion",
)


def resolve_device(requested: str) -> str:
    value = requested.strip().lower()
    if value not in {"", "auto"}:
        if value == "cuda":
            import torch

            if not torch.cuda.is_available():
                raise RuntimeError("CUDA was requested but is unavailable")
        if value == "mps":
            import torch

            if not (
                getattr(torch.backends, "mps", None) is not None
                and torch.backends.mps.is_available()
            ):
                raise RuntimeError("MPS was requested but is unavailable")
        return value

    try:
        import torch
    except Exception:
        return "cpu"
    if torch.cuda.is_available():
        return "cuda"
    if (
        getattr(torch.backends, "mps", None) is not None
        and torch.backends.mps.is_available()
    ):
        return "mps"
    return "cpu"


def task_queries(task: dict[str, Any]) -> list[tuple[str, str]]:
    return [
        ("umbrella", f"{task['title']}. {task['review_brief']}"),
        *[
            (str(component["component_id"]), str(component["requirement"]))
            for component in task["components"]
        ],
    ]


def combined_task_query(task: dict[str, Any]) -> str:
    return "\n".join(
        [
            str(task["title"]),
            str(task["review_brief"]),
            *[
                str(component["requirement"])
                for component in task["components"]
            ],
        ]
    )


def _compact(text: str, max_chars: int) -> str:
    collapsed = " ".join(str(text).split())
    if len(collapsed) <= max_chars:
        return collapsed
    return collapsed[:max_chars].rsplit(" ", 1)[0] + "..."


def _minmax(values: list[float]) -> list[float]:
    if not values:
        return []
    low, high = min(values), max(values)
    if math.isclose(low, high):
        return [0.5 for _ in values]
    return [(value - low) / (high - low) for value in values]


def _likely_review(
    *,
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
    front = f" {' '.join(front_matter.split()).casefold()[:1200]} "
    return any(
        marker in front
        for marker in (
            " review article ",
            " critical review ",
            " systematic review ",
            " current opinion ",
            " perspective ",
        )
    )


def _document_card(document: dict[str, Any]) -> str:
    lines = [
        f"Title: {document['title']}",
        f"Year: {document['year']}",
        f"DOI: {document['doi']}",
        f"Query coverage: {document['query_coverage']}/4",
    ]
    remaining = DOCUMENT_CARD_MAX_CHARS - sum(len(line) for line in lines)
    per_excerpt = max(500, remaining // max(1, len(document["top_chunks"])))
    for hit in document["top_chunks"]:
        lines.append(
            f"[{hit['query_id']}; rank {hit['rank']}; "
            f"section {hit['section']}; chunk {hit['chunk']}] "
            f"{_compact(hit['text'], per_excerpt)}"
        )
    return "\n".join(lines)[:DOCUMENT_CARD_MAX_CHARS]


def selector_cards(candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    cards = []
    for index, document in enumerate(candidates[:LLM_SELECTOR_POOL], start=1):
        cards.append(
            {
                "source_id": f"D{index:02d}",
                "bge_document_rank": index,
                "title": document["title"],
                "year": document["year"],
                "doi": document["doi"],
                "query_coverage": document["query_coverage"],
                "card": _document_card(document),
            }
        )
    return cards


class LocalReviewRetriever:
    def __init__(
        self,
        *,
        anchor_records: list[dict[str, Any]],
        device: str = "auto",
        batch_size: int = 16,
    ) -> None:
        os.environ.setdefault("HF_HUB_OFFLINE", "1")
        os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
        self.anchor_records = anchor_records
        self.known_review_sources = {
            str(record["primary_anchor"]["corpus_source"])
            for record in anchor_records
        }
        self.device = resolve_device(device)
        self.batch_size = batch_size
        settings = get_settings()
        if settings.collection_name != EXPECTED_COLLECTION:
            raise RuntimeError(
                f"Unexpected collection {settings.collection_name!r}; "
                f"expected {EXPECTED_COLLECTION!r}"
            )
        if settings.embedding_model != EXPECTED_EMBEDDING_MODEL:
            raise RuntimeError(
                f"Unexpected embedding model {settings.embedding_model!r}; "
                f"expected {EXPECTED_EMBEDDING_MODEL!r}"
            )
        self.settings = replace(settings, embedding_device=self.device)
        self.collection = get_collection(self.settings)
        if self.collection.count() != 29805:
            raise RuntimeError(
                f"Unexpected active corpus chunk count {self.collection.count()}"
            )
        started = time.perf_counter()
        self.cross_encoder = CrossEncoder(
            BGE_RERANKER_MODEL,
            device=self.device,
            max_length=BGE_MAX_LENGTH,
        )
        self.model_load_seconds = time.perf_counter() - started

    def retrieve_document_candidates(
        self,
        task: dict[str, Any],
    ) -> dict[str, Any]:
        task_id = str(task["task_id"])
        identifiers = task_anchor_identifiers(self.anchor_records, task_id)
        anchor = next(
            record["primary_anchor"]
            for record in self.anchor_records
            if record["task_id"] == task_id
        )
        queries = task_queries(task)
        started = time.perf_counter()
        results = self.collection.query(
            query_texts=[query for _, query in queries],
            n_results=QUERY_CHUNK_BUDGET,
            where={"source": {"$ne": anchor["corpus_source"]}},
            include=["documents", "metadatas", "distances"],
        )
        dense_seconds = time.perf_counter() - started

        documents: dict[str, dict[str, Any]] = {}
        for query_index, (query_id, _) in enumerate(queries):
            for rank, (text, metadata, distance) in enumerate(
                zip(
                    results["documents"][query_index],
                    results["metadatas"][query_index],
                    results["distances"][query_index],
                ),
                start=1,
            ):
                candidate = {**metadata, "text": text}
                reason = exclusion_reason(candidate, identifiers)
                if reason is not None:
                    continue
                if str(metadata.get("section") or "").casefold() == "references":
                    continue
                source = str(metadata.get("source") or "")
                record = documents.setdefault(
                    source,
                    {
                        "source": source,
                        "title": str(metadata.get("title") or source),
                        "doi": str(metadata.get("doi") or ""),
                        "url": (
                            f"https://doi.org/{metadata.get('doi')}"
                            if metadata.get("doi")
                            else ""
                        ),
                        "year": str(metadata.get("year") or ""),
                        "citation": str(
                            metadata.get("citation_acs")
                            or metadata.get("citation_apa")
                            or metadata.get("title")
                            or source
                        ),
                        "rrf_score": 0.0,
                        "best_distance": float(distance),
                        "query_ids": set(),
                        "top_chunks": [],
                    },
                )
                record["rrf_score"] += 1.0 / (RRF_K + rank)
                record["best_distance"] = min(
                    float(record["best_distance"]),
                    float(distance),
                )
                record["query_ids"].add(query_id)
                record["top_chunks"].append(
                    {
                        "query_id": query_id,
                        "rank": rank,
                        "chunk": metadata.get("chunk"),
                        "section": metadata.get("section"),
                        "text": text,
                    }
                )

        ranked_rrf = sorted(
            documents.values(),
            key=lambda item: (
                -float(item["rrf_score"]),
                float(item["best_distance"]),
                str(item["source"]),
            ),
        )
        primary_candidates = []
        for document in ranked_rrf:
            document["query_ids"] = sorted(document["query_ids"])
            document["query_coverage"] = len(document["query_ids"])
            document["top_chunks"] = sorted(
                document["top_chunks"],
                key=lambda hit: (
                    int(hit["rank"]),
                    str(hit["query_id"]),
                    int(hit["chunk"] or 0),
                ),
            )[:8]
            front = self.collection.get(
                where={"source": document["source"]},
                include=["documents", "metadatas"],
            )
            first_chunk = ""
            if front["documents"]:
                first_index = min(
                    range(len(front["documents"])),
                    key=lambda index: int(
                        front["metadatas"][index].get("chunk", 0)
                    ),
                )
                first_chunk = str(front["documents"][first_index])
            document["likely_review"] = _likely_review(
                title=str(document["title"]),
                source=str(document["source"]),
                front_matter=first_chunk,
                known_review_sources=self.known_review_sources,
            )
            if not document["likely_review"]:
                primary_candidates.append(document)
            if len(primary_candidates) >= DOCUMENT_RERANK_POOL:
                break

        if len(primary_candidates) < MIN_RETAINED_SOURCES:
            raise RuntimeError(
                f"{task_id}: only {len(primary_candidates)} likely-primary "
                "candidate documents after anchor and review filtering"
            )
        query = combined_task_query(task)
        cards = [_document_card(document) for document in primary_candidates]
        started = time.perf_counter()
        raw_scores = [
            float(score)
            for score in self.cross_encoder.predict(
                [(query, card) for card in cards],
                batch_size=self.batch_size,
                show_progress_bar=False,
            )
        ]
        rerank_seconds = time.perf_counter() - started
        normalized = _minmax(raw_scores)
        for index, (document, raw, norm) in enumerate(
            zip(primary_candidates, raw_scores, normalized),
            start=1,
        ):
            document["rrf_primary_rank"] = index
            document["bge_score"] = raw
            document["bge_score_normalized"] = norm
        ranked_bge = sorted(
            primary_candidates,
            key=lambda item: (
                -float(item["bge_score"]),
                int(item["rrf_primary_rank"]),
                str(item["source"]),
            ),
        )
        for rank, document in enumerate(ranked_bge, start=1):
            document["bge_document_rank"] = rank
        return {
            "task_id": task_id,
            "queries": [
                {"query_id": query_id, "query": query}
                for query_id, query in queries
            ],
            "anchor_identifiers": {
                key: sorted(value) for key, value in identifiers.items()
            },
            "candidate_documents": ranked_bge,
            "runtime": {
                "dense_retrieval_seconds": dense_seconds,
                "bge_document_rerank_seconds": rerank_seconds,
            },
            "config": {
                "query_chunk_budget": QUERY_CHUNK_BUDGET,
                "rrf_k": RRF_K,
                "document_rerank_pool": DOCUMENT_RERANK_POOL,
                "bge_reranker": BGE_RERANKER_MODEL,
                "bge_max_length": BGE_MAX_LENGTH,
                "device": self.device,
            },
        }

    def expand_selected_documents(
        self,
        *,
        task: dict[str, Any],
        selected_documents: list[dict[str, Any]],
    ) -> dict[str, Any]:
        task_id = str(task["task_id"])
        identifiers = task_anchor_identifiers(self.anchor_records, task_id)
        queries = task_queries(task)
        prepared_sources = []
        expansion_seconds = 0.0
        for source_index, document in enumerate(selected_documents, start=1):
            if exclusion_reason(document, identifiers) is not None:
                raise RuntimeError(
                    f"{task_id}: anchor survived document selection"
                )
            corpus = self.collection.get(
                where={"source": document["source"]},
                include=["documents", "metadatas"],
            )
            chunks = []
            for text, metadata in zip(
                corpus["documents"],
                corpus["metadatas"],
            ):
                hit = {**metadata, "text": text}
                if exclusion_reason(hit, identifiers) is not None:
                    raise RuntimeError(
                        f"{task_id}: anchor survived within-document expansion"
                    )
                if is_reference_like(hit):
                    continue
                chunks.append(hit)
            chunks.sort(key=lambda hit: int(hit.get("chunk", 0)))
            if not chunks:
                raise RuntimeError(
                    f"{task_id}: selected source has no evidence chunks: "
                    f"{document['source']}"
                )

            pairs = []
            pair_keys = []
            for query_id, query in queries:
                for chunk_index, chunk in enumerate(chunks):
                    passage = (
                        f"Title: {document['title']}\n"
                        f"Section: {chunk.get('section') or 'unknown'}\n"
                        f"Text: {_compact(chunk['text'], CHUNK_MAX_CHARS)}"
                    )
                    pairs.append((query, passage))
                    pair_keys.append((query_id, chunk_index))
            started = time.perf_counter()
            raw_scores = [
                float(score)
                for score in self.cross_encoder.predict(
                    pairs,
                    batch_size=self.batch_size,
                    show_progress_bar=False,
                )
            ]
            expansion_seconds += time.perf_counter() - started
            scores_by_chunk: dict[int, dict[str, float]] = {
                index: {} for index in range(len(chunks))
            }
            for (query_id, chunk_index), score in zip(pair_keys, raw_scores):
                scores_by_chunk[chunk_index][query_id] = score

            selected_indices: list[int] = []
            for query_id, _ in queries:
                best = max(
                    range(len(chunks)),
                    key=lambda index: (
                        scores_by_chunk[index][query_id],
                        -int(chunks[index].get("chunk", 0)),
                    ),
                )
                if best not in selected_indices:
                    selected_indices.append(best)
            remaining = sorted(
                (
                    index
                    for index in range(len(chunks))
                    if index not in selected_indices
                ),
                key=lambda index: (
                    -max(scores_by_chunk[index].values()),
                    int(chunks[index].get("chunk", 0)),
                ),
            )
            selected_indices.extend(
                remaining[: max(0, CHUNKS_PER_DOCUMENT - len(selected_indices))]
            )
            selected_indices = selected_indices[:CHUNKS_PER_DOCUMENT]

            source_id = f"S{source_index:02d}"
            evidence_chunks = []
            for locator_index, chunk_index in enumerate(
                selected_indices,
                start=1,
            ):
                chunk = chunks[chunk_index]
                evidence_chunks.append(
                    {
                        "locator_id": f"{source_id}-E{locator_index:02d}",
                        "corpus_chunk": int(chunk.get("chunk", 0)),
                        "section": str(chunk.get("section") or "unknown"),
                        "text": str(chunk["text"]),
                        "query_scores": scores_by_chunk[chunk_index],
                    }
                )
            prepared_sources.append(
                {
                    "source_id": source_id,
                    "source": document["source"],
                    "title": document["title"],
                    "year": document["year"],
                    "doi": document["doi"],
                    "doi_or_stable_url": (
                        document["url"]
                        or f"corpus://{document['source']}"
                    ),
                    "citation": document["citation"],
                    "publication_status": (
                        "peer_reviewed_or_formally_published"
                        if document["doi"]
                        else "corpus_record_status_unresolved"
                    ),
                    "bge_document_rank": document["bge_document_rank"],
                    "bge_score": document["bge_score"],
                    "evidence_chunks": evidence_chunks,
                }
            )
        return {
            "task_id": task_id,
            "candidate_document_budget": DOCUMENT_BUDGET,
            "retained_source_count": len(prepared_sources),
            "minimum_retained_sources": MIN_RETAINED_SOURCES,
            "chunks_per_document": CHUNKS_PER_DOCUMENT,
            "sources": prepared_sources,
            "runtime": {
                "within_document_bge_seconds": expansion_seconds,
            },
        }

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import copy
import csv
import json
import math
from pathlib import Path
import re
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "benchmark/frozen_v3/scripts"))

from src.rag_app.config import get_settings  # noqa: E402
from src.rag_app.ingest import get_collection  # noqa: E402
from src.rag_app.rag import (  # noqa: E402
    hit_key,
    is_reference_like,
    merge_hits,
    metadata_to_hit,
    tokenize,
    tokenize_list,
)
from retrieval_metrics import eval_context  # noqa: E402


QUESTIONS = ROOT / "benchmark/frozen_v3/input/questions_all53.csv"
DEV_QUESTIONS = ROOT / "benchmark/frozen_v3/input/questions_dev13.csv"
GOLD = ROOT / "benchmark/frozen_v3/gold/chunk_based_gold.jsonl"
POOL_K = 60
TOP_K = 10
BM25_K1 = 1.5
BM25_B = 0.75


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def legacy_reference_penalty(text: str) -> float:
    lower = text[:2000].lower()
    markers = lower.count(" doi:") + lower.count(" et al.") + lower.count(" references")
    if lower.lstrip().startswith(("references", "bibliography")):
        return 0.25
    if markers >= 8:
        return 0.15
    return 0.0


def rank_hits(
    question: str,
    hits: list[dict[str, Any]],
    *,
    penalty_mode: str,
) -> list[dict[str, Any]]:
    query_terms = tokenize(question)
    max_distance = max(float(hit.get("distance") or 0.0) for hit in hits) or 1.0
    max_bm25 = max(float(hit.get("bm25_score") or 0.0) for hit in hits) or 1.0
    ranked_hits = copy.deepcopy(hits)
    for index, hit in enumerate(ranked_hits):
        text = " ".join(
            str(value or "")
            for value in (hit.get("title"), hit.get("source"), hit.get("text"))
        )
        text_terms = tokenize(text)
        lexical_score = (
            len(query_terms & text_terms) / len(query_terms) if query_terms else 0.0
        )
        vector_score = 1.0 - (float(hit.get("distance") or 0.0) / max_distance)
        bm25_score = float(hit.get("bm25_score") or 0.0) / max_bm25
        legacy_penalty = legacy_reference_penalty(hit["text"])
        if penalty_mode == "legacy_penalty":
            penalty = legacy_penalty
        elif penalty_mode == "marker_penalty_off":
            penalty = 0.0 if legacy_penalty == 0.15 else legacy_penalty
        elif penalty_mode == "all_penalties_off":
            penalty = 0.0
        else:
            raise ValueError(f"Unknown penalty mode: {penalty_mode}")
        hit["retrieval_rank"] = index + 1
        hit["rerank_score"] = (
            0.65 * vector_score + 0.20 * bm25_score + 0.15 * lexical_score - penalty
        )
        hit["reference_like"] = is_reference_like(hit)

    ranked_hits.sort(key=lambda hit: hit["rerank_score"], reverse=True)
    evidence = [hit for hit in ranked_hits if not hit["reference_like"]]
    references = [hit for hit in ranked_hits if hit["reference_like"]]
    return (evidence + references)[:POOL_K]


def bm25_hits_for_question(
    question: str,
    documents: list[str],
    metadatas: list[dict[str, Any]],
    tokenized_docs: list[list[str]],
    doc_freq: Counter[str],
    avg_doc_len: float,
) -> list[dict[str, Any]]:
    query_counts = Counter(tokenize_list(question))
    scores: list[tuple[float, int]] = []
    total_docs = len(documents)
    for index, terms in enumerate(tokenized_docs):
        if not terms:
            continue
        term_counts = Counter(terms)
        doc_len = len(terms)
        score = 0.0
        for term, query_count in query_counts.items():
            tf = term_counts.get(term)
            if not tf:
                continue
            df = doc_freq[term]
            idf = math.log(1 + (total_docs - df + 0.5) / (df + 0.5))
            denominator = tf + BM25_K1 * (
                1 - BM25_B + BM25_B * doc_len / avg_doc_len
            )
            score += query_count * idf * (tf * (BM25_K1 + 1) / denominator)
        if score > 0:
            scores.append((score, index))

    hits: list[dict[str, Any]] = []
    for rank, (score, index) in enumerate(
        sorted(scores, key=lambda item: item[0], reverse=True)[:POOL_K], start=1
    ):
        hit = metadata_to_hit(documents[index], metadatas[index], distance=1.0)
        hit["bm25_rank"] = rank
        hit["bm25_score"] = score
        hit["retrieval_source"] = "bm25"
        hits.append(hit)
    return hits


def metric_context(hits: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            "rank": rank,
            "doc_id": hit.get("source", "unknown"),
            "chunk_id": hit.get("chunk"),
            "section": hit.get("section"),
            "title": hit.get("title"),
            "text": hit.get("text", ""),
        }
        for rank, hit in enumerate(hits[:TOP_K], start=1)
    ]


def summarize_metrics(rows: list[dict[str, Any]]) -> dict[str, float]:
    required = [row for row in rows if int(row["required_gold_count"]) > 0]
    negative = [row for row in rows if int(row["negative_gold_count"]) > 0]

    def mean(group: list[dict[str, Any]], field: str) -> float:
        return sum(float(row[field]) for row in group) / len(group)

    return {
        "MRR_required_gold": mean(required, "MRR_required_gold"),
        "required_gold_recall@10": mean(required, "required_gold_recall@10"),
        "gold_doc_recall@10": mean(required, "gold_doc_recall@10"),
        "negative_gold_recall@10": mean(negative, "negative_gold_recall@10"),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    out = args.out.expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)

    questions = read_csv(QUESTIONS)
    dev_ids = {str(row["question_id"]) for row in read_csv(DEV_QUESTIONS)}
    gold_by_qid: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in read_jsonl(GOLD):
        gold_by_qid[str(row["question_id"])].append(row)

    collection = get_collection(get_settings())
    corpus = collection.get(include=["documents", "metadatas"])
    documents = corpus.get("documents", []) or []
    metadatas = corpus.get("metadatas", []) or []
    tokenized_docs = [tokenize_list(document) for document in documents]
    doc_freq: Counter[str] = Counter()
    for terms in tokenized_docs:
        doc_freq.update(set(terms))
    avg_doc_len = sum(map(len, tokenized_docs)) / max(len(tokenized_docs), 1)

    comparison_rows: list[dict[str, Any]] = []
    modes = ("legacy_penalty", "marker_penalty_off", "all_penalties_off")
    metrics: dict[str, list[dict[str, Any]]] = {mode: [] for mode in modes}
    for index, question in enumerate(questions, start=1):
        qid = str(question["question_id"])
        question_text = str(question["question_text"])
        dense = collection.query(
            query_texts=[question_text],
            n_results=POOL_K,
            include=["documents", "metadatas", "distances"],
        )
        dense_hits: list[dict[str, Any]] = []
        for rank, (document, metadata, distance) in enumerate(
            zip(
                dense["documents"][0],
                dense["metadatas"][0],
                dense["distances"][0],
            ),
            start=1,
        ):
            hit = metadata_to_hit(document, metadata, float(distance))
            hit["dense_rank"] = rank
            hit["retrieval_source"] = "dense"
            dense_hits.append(hit)
        bm25_hits = bm25_hits_for_question(
            question_text,
            documents,
            metadatas,
            tokenized_docs,
            doc_freq,
            avg_doc_len,
        )
        merged = merge_hits(dense_hits, bm25_hits)
        ranked_by_mode = {
            mode: rank_hits(question_text, merged, penalty_mode=mode) for mode in modes
        }
        legacy = ranked_by_mode["legacy_penalty"]
        marker_off = ranked_by_mode["marker_penalty_off"]
        all_off = ranked_by_mode["all_penalties_off"]
        legacy_top10 = [hit_key(hit) for hit in legacy[:TOP_K]]
        marker_off_top10 = [hit_key(hit) for hit in marker_off[:TOP_K]]
        all_off_top10 = [hit_key(hit) for hit in all_off[:TOP_K]]
        legacy_top60 = [hit_key(hit) for hit in legacy]
        marker_off_top60 = [hit_key(hit) for hit in marker_off]
        all_off_top60 = [hit_key(hit) for hit in all_off]
        comparison_rows.append(
            {
                "question_id": qid,
                "split": "dev13" if qid in dev_ids else "test40",
                "marker_off_top10_order_identical": legacy_top10 == marker_off_top10,
                "marker_off_top10_set_identical": set(legacy_top10) == set(marker_off_top10),
                "marker_off_top60_order_identical": legacy_top60 == marker_off_top60,
                "marker_off_top60_set_identical": set(legacy_top60) == set(marker_off_top60),
                "all_off_top10_order_identical": legacy_top10 == all_off_top10,
                "all_off_top10_set_identical": set(legacy_top10) == set(all_off_top10),
                "all_off_top60_order_identical": legacy_top60 == all_off_top60,
                "all_off_top60_set_identical": set(legacy_top60) == set(all_off_top60),
                "legacy_penalized_candidates_in_top60": sum(
                    legacy_reference_penalty(hit["text"]) > 0 for hit in legacy
                ),
            }
        )
        for name, hits in ranked_by_mode.items():
            metrics[name].append(
                eval_context(
                    qid,
                    gold_by_qid[qid],
                    metric_context(hits),
                    name,
                    "hybrid",
                    TOP_K,
                    POOL_K,
                    0,
                )
            )
        print(f"[{index}/{len(questions)}] {qid}", flush=True)

    with (out / "per_question.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(comparison_rows[0]))
        writer.writeheader()
        writer.writerows(comparison_rows)

    def identity_counts(rows: list[dict[str, Any]], prefix: str) -> dict[str, int]:
        return {
            "question_count": len(rows),
            "top10_order_identical": sum(row[f"{prefix}_top10_order_identical"] for row in rows),
            "top10_set_identical": sum(row[f"{prefix}_top10_set_identical"] for row in rows),
            "top60_order_identical": sum(row[f"{prefix}_top60_order_identical"] for row in rows),
            "top60_set_identical": sum(row[f"{prefix}_top60_set_identical"] for row in rows),
        }

    metric_by_split: dict[str, dict[str, dict[str, float]]] = {}
    for split in ("all53", "dev13", "test40"):
        selected_ids = {
            row["question_id"]
            for row in comparison_rows
            if split == "all53" or row["split"] == split
        }
        metric_by_split[split] = {
            mode: summarize_metrics(
                [row for row in mode_rows if str(row["question_id"]) in selected_ids]
            )
            for mode, mode_rows in metrics.items()
        }

    summary = {
        "identity": {
            split: {
                "marker_penalty_off": identity_counts(
                    [row for row in comparison_rows if split == "all53" or row["split"] == split],
                    "marker_off",
                ),
                "all_penalties_off": identity_counts(
                    [row for row in comparison_rows if split == "all53" or row["split"] == split],
                    "all_off",
                ),
            }
            for split in ("all53", "dev13", "test40")
        },
        "metrics": metric_by_split,
        "interpretation": (
            "The 0.15 citation-marker penalty and the complete numerical penalty are "
            "reported separately because the legacy function also assigned 0.25 to "
            "chunks beginning with a references or bibliography heading."
        ),
    }
    (out / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()

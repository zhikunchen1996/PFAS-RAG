from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
import hashlib
import json
import math
from pathlib import Path
import sys
import time
from typing import Any

import chromadb
from chromadb.utils import embedding_functions


ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "benchmark/frozen_v3/scripts"))

from src.rag_app.rag import is_reference_like, metadata_to_hit, tokenize_list  # noqa: E402
from retrieval_metrics import eval_context  # noqa: E402


QUESTIONS = ROOT / "benchmark/frozen_v3/input/questions_dev13.csv"
GOLD = ROOT / "benchmark/frozen_v3/gold/chunk_based_gold.jsonl"
CHROMA = ROOT / "data/chroma"
COLLECTION = "rag_documents_bge_large_en_v1_5_sent256_overlap2_corpus434_repaired_v1"
EMBEDDING_MODEL = "BAAI/bge-large-en-v1.5"
POOL_K = 60
TOP_K = 10
BM25_K1 = 1.5
BM25_B = 0.75


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def context_item(hit: dict[str, Any], rank: int, score_field: str) -> dict[str, Any]:
    return {
        "rank": rank,
        "doc_id": hit.get("source", "unknown"),
        "chunk_id": hit.get("chunk"),
        "section": hit.get("section"),
        "title": hit.get("title"),
        "text": hit.get("text", ""),
        score_field: hit.get(score_field),
        "reference_like": bool(hit.get("reference_like")),
    }


def select_nonreference_first(hits: list[dict[str, Any]]) -> list[dict[str, Any]]:
    for hit in hits:
        hit["reference_like"] = is_reference_like(hit)
    evidence = [hit for hit in hits if not hit["reference_like"]]
    references = [hit for hit in hits if hit["reference_like"]]
    return (evidence + references)[:TOP_K]


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    required = [row for row in rows if int(row["required_gold_count"]) > 0]
    negative = [row for row in rows if int(row["negative_gold_count"]) > 0]

    def average(group: list[dict[str, Any]], field: str) -> float:
        return sum(float(row[field]) for row in group) / len(group)

    return {
        "config_name": rows[0]["config_name"],
        "retrieval_method": rows[0]["retrieval_method"],
        "question_count": len(rows),
        "required_gold_applicable_questions": len(required),
        "MRR_required_gold": average(required, "MRR_required_gold"),
        "required_gold_recall@10": average(required, "required_gold_recall@10"),
        "gold_doc_recall@10": average(required, "gold_doc_recall@10"),
        "negative_gold_applicable_questions": len(negative),
        "negative_gold_recall@10": average(negative, "negative_gold_recall@10"),
    }


def output_row(
    question_id: str,
    context: list[dict[str, Any]],
    config_name: str,
    method: str,
) -> dict[str, Any]:
    return {
        "question_id": question_id,
        "retrieved_context": context,
        "retrieval_config_name": config_name,
        "retrieval_method": method,
        "retrieval_k": POOL_K,
        "top_k": TOP_K,
        "context_window": 0,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--device", default="cpu")
    args = parser.parse_args()
    out = args.out.expanduser().resolve()
    if out.exists() and any(out.iterdir()):
        raise RuntimeError(f"Refusing to overwrite non-empty output: {out}")
    out.mkdir(parents=True, exist_ok=True)

    started = time.perf_counter()
    questions = read_csv(QUESTIONS)
    gold_by_qid: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in read_jsonl(GOLD):
        gold_by_qid[str(row["question_id"])].append(row)

    embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=EMBEDDING_MODEL,
        device=args.device,
    )
    collection = chromadb.PersistentClient(path=str(CHROMA)).get_collection(
        COLLECTION,
        embedding_function=embedding_fn,
    )
    corpus = collection.get(include=["documents", "metadatas"])
    documents = corpus.get("documents", []) or []
    metadatas = corpus.get("metadatas", []) or []
    tokenized_docs = [tokenize_list(document) for document in documents]
    doc_freq: Counter[str] = Counter()
    for terms in tokenized_docs:
        doc_freq.update(set(terms))
    avg_doc_len = sum(map(len, tokenized_docs)) / max(len(tokenized_docs), 1)

    dense_rows: list[dict[str, Any]] = []
    bm25_rows: list[dict[str, Any]] = []
    dense_seconds = 0.0
    bm25_seconds = 0.0
    for question in questions:
        qid = str(question["question_id"])
        text = str(question["question_text"])

        stage_started = time.perf_counter()
        dense_result = collection.query(
            query_texts=[text],
            n_results=POOL_K,
            include=["documents", "metadatas", "distances"],
        )
        dense_hits: list[dict[str, Any]] = []
        for dense_rank, (document, metadata, distance) in enumerate(
            zip(
                dense_result["documents"][0],
                dense_result["metadatas"][0],
                dense_result["distances"][0],
            ),
            start=1,
        ):
            hit = metadata_to_hit(document, metadata, float(distance))
            hit["dense_rank"] = dense_rank
            dense_hits.append(hit)
        dense_selected = select_nonreference_first(dense_hits)
        dense_seconds += time.perf_counter() - stage_started
        dense_rows.append(
            output_row(
                qid,
                [
                    context_item(hit, rank, "distance")
                    for rank, hit in enumerate(dense_selected, start=1)
                ],
                "bge_large_dense_only_top10_pool60_refilter",
                "bge_dense_only",
            )
        )

        stage_started = time.perf_counter()
        query_counts = Counter(tokenize_list(text))
        scores: list[tuple[float, int]] = []
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
                idf = math.log(
                    1 + (len(documents) - df + 0.5) / (df + 0.5)
                )
                denominator = tf + BM25_K1 * (
                    1 - BM25_B + BM25_B * doc_len / avg_doc_len
                )
                score += query_count * idf * (
                    tf * (BM25_K1 + 1) / denominator
                )
            if score > 0:
                scores.append((score, index))
        bm25_hits: list[dict[str, Any]] = []
        for bm25_rank, (score, index) in enumerate(
            sorted(scores, key=lambda item: item[0], reverse=True)[:POOL_K],
            start=1,
        ):
            hit = metadata_to_hit(
                documents[index], metadatas[index], distance=1.0
            )
            hit["bm25_rank"] = bm25_rank
            hit["bm25_score"] = score
            bm25_hits.append(hit)
        bm25_selected = select_nonreference_first(bm25_hits)
        bm25_seconds += time.perf_counter() - stage_started
        bm25_rows.append(
            {
                **output_row(
                    qid,
                    [
                        context_item(hit, rank, "bm25_score")
                        for rank, hit in enumerate(bm25_selected, start=1)
                    ],
                    "bm25_only_top10_pool60_refilter",
                    "bm25_only",
                ),
                "bm25_k": POOL_K,
            }
        )
        print(f"completed {qid}", flush=True)

    retrieval_dir = out / "results/retrieval"
    dense_path = retrieval_dir / "dense_only_top10.jsonl"
    bm25_path = retrieval_dir / "bm25_only_top10.jsonl"
    write_jsonl(dense_path, dense_rows)
    write_jsonl(bm25_path, bm25_rows)

    for name, outputs in (("dense_only", dense_rows), ("bm25_only", bm25_rows)):
        metric_rows = [
            eval_context(
                str(row["question_id"]),
                gold_by_qid[str(row["question_id"])],
                row["retrieved_context"],
                str(row["retrieval_config_name"]),
                str(row["retrieval_method"]),
                TOP_K,
                POOL_K,
                0,
            )
            for row in outputs
        ]
        write_csv(out / f"results/l1/{name}/per_question.csv", metric_rows)
        write_csv(out / f"results/l1/{name}/summary.csv", [summarize(metric_rows)])

    manifest = {
        "status": "post-freeze exploratory Dev13 component ablation",
        "question_count": len(questions),
        "corpus_chunks": len(documents),
        "pool_k": POOL_K,
        "top_k": TOP_K,
        "embedding_model": EMBEDDING_MODEL,
        "embedding_device": args.device,
        "bm25": {
            "k1": BM25_K1,
            "b": BM25_B,
            "tokenizer": "src.rag_app.rag.tokenize_list",
        },
        "reference_filter": (
            "src.rag_app.rag.is_reference_like; non-reference first "
            "within each component's top-60"
        ),
        "excluded": [
            "hybrid fusion",
            "lexical-overlap fusion score",
            "cross-encoder reranking",
            "LLM selection",
            "answer generation",
        ],
        "inputs": {
            "questions_sha256": sha256(QUESTIONS),
            "gold_sha256": sha256(GOLD),
        },
        "runtime": {
            "dense_seconds": dense_seconds,
            "bm25_seconds": bm25_seconds,
            "total_seconds": time.perf_counter() - started,
        },
        "api_calls": 0,
        "test40_used": False,
    }
    (out / "results/run_manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )


if __name__ == "__main__":
    main()

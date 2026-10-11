from __future__ import annotations

import argparse
import math
import sys
import time
from collections import defaultdict
from dataclasses import replace
from pathlib import Path
from statistics import mean
from typing import Any

from sentence_transformers import CrossEncoder

import common


SRC = common.ROOT / "src"
FROZEN_SCRIPTS = common.FROZEN_V3 / "scripts"
for path in (SRC, FROZEN_SCRIPTS):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from rag_app.config import get_settings  # noqa: E402
from rag_app.rag import retrieve  # noqa: E402
from retrieval_metrics import eval_context  # noqa: E402


BGE_MODEL = "BAAI/bge-reranker-base"
POOL_K = 60
TOP_K = 10
BGE_MAX_LENGTH = 512
BGE_MAX_CHARS = 1800
EXPECTED_COLLECTION = (
    "rag_documents_bge_large_en_v1_5_sent256_overlap2_"
    "corpus434_repaired_v1"
)
EXPECTED_EMBEDDING = "BAAI/bge-large-en-v1.5"


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


def minmax(values: list[float]) -> list[float]:
    if not values:
        return []
    low, high = min(values), max(values)
    if math.isclose(low, high):
        return [0.5 for _ in values]
    return [(value - low) / (high - low) for value in values]


def candidate_passage(hit: dict[str, Any]) -> str:
    title = str(
        hit.get("title") or hit.get("citation_acs") or hit.get("source") or ""
    )
    section = str(hit.get("section") or "unknown")
    text = str(hit.get("text") or "")
    if len(text) > BGE_MAX_CHARS:
        text = text[:BGE_MAX_CHARS]
    return f"Title: {title}\nSection: {section}\nText: {text}"


def score_bge(
    model: CrossEncoder,
    question: str,
    candidates: list[dict[str, Any]],
    *,
    batch_size: int,
) -> list[dict[str, Any]]:
    pairs = [(question, candidate_passage(hit)) for hit in candidates]
    raw = [
        float(value)
        for value in model.predict(
            pairs,
            batch_size=batch_size,
            show_progress_bar=False,
        )
    ]
    normalized = minmax(raw)
    rows = []
    for original_rank, (hit, raw_score, norm_score) in enumerate(
        zip(candidates, raw, normalized),
        start=1,
    ):
        row = dict(hit)
        row.update(
            {
                "original_rank": original_rank,
                "cross_encoder_score": raw_score,
                "cross_encoder_score_norm": norm_score,
                "selector_score": norm_score,
            }
        )
        rows.append(row)
    return sorted(
        rows,
        key=lambda row: (
            -float(row["selector_score"]),
            int(row["original_rank"]),
        ),
    )


def output_row(
    *,
    question_id: str,
    config_name: str,
    method: str,
    context: list[dict[str, Any]],
) -> dict[str, Any]:
    return {
        "question_id": question_id,
        "system_mode": "rag_end_to_end",
        "answer": "",
        "retrieved_context": context,
        "retrieval_config_name": config_name,
        "retrieval_method": method,
        "retrieval_k": POOL_K,
        "bm25_k": POOL_K,
        "top_k": TOP_K,
        "context_window": 0,
        "llm_rerank": False,
        "cross_encoder_model": BGE_MODEL if method == "bge_cross_encoder" else "",
        "doc_cap": "",
    }


def summarize(
    rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["config_name"])].append(row)
    summaries = []
    for config_name, group in grouped.items():
        required = [
            row for row in group if int(row["required_gold_count"]) > 0
        ]
        negative = [
            row for row in group if int(row["negative_gold_count"]) > 0
        ]
        summaries.append(
            {
                "config_name": config_name,
                "question_count": len(group),
                "required_gold_applicable_questions": len(required),
                "MRR_required_gold": mean(
                    float(row["MRR_required_gold"]) for row in required
                ),
                "required_gold_recall@10": mean(
                    float(row["required_gold_recall@10"])
                    for row in required
                ),
                "gold_doc_recall@10": mean(
                    float(row["gold_doc_recall@10"]) for row in required
                ),
                "negative_gold_applicable_questions": len(negative),
                "negative_gold_recall@10": (
                    mean(
                        float(row["negative_gold_recall@10"])
                        for row in negative
                    )
                    if negative
                    else ""
                ),
            }
        )
    return summaries


def validate_settings() -> dict[str, Any]:
    settings = get_settings()
    errors = []
    if settings.collection_name != EXPECTED_COLLECTION:
        errors.append(
            f"COLLECTION_NAME={settings.collection_name!r}; "
            f"expected {EXPECTED_COLLECTION!r}"
        )
    if settings.embedding_model != EXPECTED_EMBEDDING:
        errors.append(
            f"EMBEDDING_MODEL={settings.embedding_model!r}; "
            f"expected {EXPECTED_EMBEDDING!r}"
        )
    if not settings.reference_filter:
        errors.append("REFERENCE_FILTER must be true")
    if errors:
        raise RuntimeError("; ".join(errors))
    return {
        "collection_name": settings.collection_name,
        "embedding_model": settings.embedding_model,
        "configured_embedding_device": settings.embedding_device,
        "auto_resolved_runtime_device": resolve_device("auto"),
        "reference_filter": settings.reference_filter,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True)
    parser.add_argument("--device", default="auto")
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()

    settings_record = validate_settings()
    questions = common.read_csv(common.QUESTIONS)
    expected_ids = common.question_ids()
    if args.validate_only:
        print(
            "VALIDATION PASS: Test40 membership and frozen retrieval "
            "environment settings are valid."
        )
        return

    selected_questions = (
        questions[: args.limit] if args.limit is not None else questions
    )
    if args.limit is None and len(selected_questions) != 40:
        raise RuntimeError("Formal retrieval requires all 40 questions")
    out = Path(args.out).expanduser().resolve()
    if args.limit is None:
        common.require_exact_path(
            out,
            common.RETRIEVAL_RESULTS,
            label="Formal retrieval output",
        )
    if out.exists() and any(out.iterdir()):
        raise RuntimeError(f"Refusing to overwrite non-empty output: {out}")
    out.mkdir(parents=True, exist_ok=True)

    settings = get_settings()
    device = resolve_device(args.device)
    effective = replace(
        settings,
        embedding_device=device,
        retrieval_mode="hybrid",
        retrieval_k=POOL_K,
        bm25_k=POOL_K,
        top_k=POOL_K,
        llm_rerank=False,
    )
    settings_record["runtime_device"] = device
    load_started = time.perf_counter()
    bge = CrossEncoder(
        BGE_MODEL,
        device=device,
        max_length=BGE_MAX_LENGTH,
    )
    bge_load_seconds = time.perf_counter() - load_started

    hybrid_rows = []
    bge_rows = []
    bge_candidates = []
    retrieval_seconds = 0.0
    bge_seconds = 0.0
    for index, question in enumerate(selected_questions, start=1):
        qid = str(question["question_id"])
        text = str(question["question_text"])
        print(f"[retrieval {index}/{len(selected_questions)}] {qid}", flush=True)
        started = time.perf_counter()
        candidates = retrieve(effective, text, question_metadata=question)[
            :POOL_K
        ]
        retrieval_seconds += time.perf_counter() - started
        normalized_pool = [
            common.normalize_context_hit(hit, rank)
            for rank, hit in enumerate(candidates, start=1)
        ]
        if len(normalized_pool) != POOL_K:
            raise RuntimeError(f"{qid}: expected {POOL_K} hybrid candidates")

        hybrid_context = [
            common.normalize_context_hit(hit, rank)
            for rank, hit in enumerate(candidates[:TOP_K], start=1)
        ]
        hybrid_rows.append(
            output_row(
                question_id=qid,
                config_name="hybrid_top10_pool60_win0",
                method="hybrid",
                context=hybrid_context,
            )
        )

        started = time.perf_counter()
        ranked = score_bge(
            bge,
            text,
            candidates,
            batch_size=args.batch_size,
        )
        bge_seconds += time.perf_counter() - started
        for rank, hit in enumerate(ranked, start=1):
            bge_candidates.append(
                {
                    "config_name": "bge_base_top10_pool60_nodoccap",
                    "question_id": qid,
                    "rank": rank,
                    **common.normalize_context_hit(hit, rank),
                }
            )
        bge_context = [
            common.normalize_context_hit(hit, rank)
            for rank, hit in enumerate(ranked[:TOP_K], start=1)
        ]
        bge_rows.append(
            output_row(
                question_id=qid,
                config_name="bge_base_top10_pool60_nodoccap",
                method="bge_cross_encoder",
                context=bge_context,
            )
        )

    output_dir = out / "retrieval_outputs"
    common.write_jsonl(
        output_dir / "rag_outputs_hybrid_top10_pool60_win0.jsonl",
        hybrid_rows,
    )
    common.write_jsonl(
        output_dir / "rag_outputs_bge_base_top10_pool60_nodoccap.jsonl",
        bge_rows,
    )
    common.write_jsonl(out / "bge_candidate_scores.jsonl", bge_candidates)

    if args.limit is None:
        common.ordered_rows(hybrid_rows, expected_ids, source="Hybrid")
        common.ordered_rows(bge_rows, expected_ids, source="BGE")
        common.validate_contexts(
            hybrid_rows,
            expected_count=TOP_K,
            source="Hybrid",
        )
        common.validate_contexts(
            bge_rows,
            expected_count=TOP_K,
            source="BGE",
        )
        gold_by_qid: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for row in common.read_jsonl(common.GOLD):
            gold_by_qid[str(row["question_id"])].append(row)
        metric_rows = []
        for output in hybrid_rows + bge_rows:
            metric_rows.append(
                eval_context(
                    str(output["question_id"]),
                    gold_by_qid[str(output["question_id"])],
                    output["retrieved_context"],
                    str(output["retrieval_config_name"]),
                    str(output["retrieval_method"]),
                    TOP_K,
                    POOL_K,
                    0,
                )
            )
        common.write_csv(out / "l1_per_question.csv", metric_rows)
        common.write_csv(out / "l1_summary.csv", summarize(metric_rows))

    common.write_json(
        out / "run_manifest.json",
        {
            "protocol_id": "test40_formal_v1_retrieval",
            "status": "complete" if args.limit is None else "smoke_only",
            "question_count": len(selected_questions),
            "held_out_test40_used": True,
            "test_results_used_for_configuration": False,
            "questions_sha256": common.sha256(common.QUESTIONS),
            "gold_sha256": common.sha256(common.GOLD),
            "settings": settings_record,
            "hybrid": {"pool_k": POOL_K, "final_top_k": TOP_K},
            "bge": {
                "pool_k": POOL_K,
                "final_top_k": TOP_K,
                "model": BGE_MODEL,
                "device": device,
                "batch_size": args.batch_size,
                "max_length": BGE_MAX_LENGTH,
                "max_chars_per_candidate": BGE_MAX_CHARS,
                "document_cap": None,
            },
            "runtime": {
                "bge_model_load_seconds": bge_load_seconds,
                "hybrid_retrieval_seconds_sum": retrieval_seconds,
                "bge_rerank_seconds_sum": bge_seconds,
            },
            "api_calls": 0,
        },
    )


if __name__ == "__main__":
    main()

"""Self-contained retrieval metrics used by the Frozen V3 budget sweep.

The formulas are promoted unchanged from benchmark/src/run_recall_rate_test.py
so the migrated V2 rows and new GPT-5.1 rows remain directly comparable.
"""

from __future__ import annotations

from typing import Any


K_VALUES = (5, 10, 20)


def norm(value: Any) -> str:
    return "" if value is None else str(value)


def metric_top_context(
    context: list[dict[str, Any]],
    k: int,
) -> list[dict[str, Any]]:
    if any("center_rank" in item for item in context):
        top = []
        for item in context:
            try:
                center_rank = int(
                    item.get("center_rank")
                    or item.get("rank")
                    or 999999
                )
            except (TypeError, ValueError):
                center_rank = 999999
            if center_rank <= k:
                top.append(item)
        return top
    return context[:k]


def gold_is_hit(
    ref: dict[str, Any],
    context: list[dict[str, Any]],
    k: int,
) -> bool:
    doc_id = norm(ref.get("doc_id"))
    chunk_id = norm(ref.get("chunk_id"))
    top = metric_top_context(context, k)
    if doc_id and chunk_id:
        return any(
            norm(item.get("doc_id")) == doc_id
            and norm(item.get("chunk_id")) == chunk_id
            for item in top
        )
    if chunk_id:
        return any(
            norm(item.get("chunk_id")) == chunk_id for item in top
        )
    if doc_id:
        return any(norm(item.get("doc_id")) == doc_id for item in top)
    return False


def chunk_is_hit(
    ref: dict[str, Any],
    context: list[dict[str, Any]],
    k: int,
) -> bool:
    doc_id = norm(ref.get("doc_id"))
    chunk_id = norm(ref.get("chunk_id"))
    if not chunk_id:
        return False
    if doc_id:
        return any(
            norm(item.get("doc_id")) == doc_id
            and norm(item.get("chunk_id")) == chunk_id
            for item in metric_top_context(context, k)
        )
    return any(
        norm(item.get("chunk_id")) == chunk_id
        for item in metric_top_context(context, k)
    )


def recall(numerator: int, denominator: int) -> float:
    return numerator / denominator if denominator else 0.0


def mrr_required(
    required_refs: list[dict[str, Any]],
    context: list[dict[str, Any]],
) -> float:
    if not required_refs:
        return 0.0
    max_rank = 0
    for item in context:
        try:
            rank = int(
                item.get("center_rank") or item.get("rank") or 0
            )
        except (TypeError, ValueError):
            rank = 0
        max_rank = max(max_rank, rank)
    for rank in range(1, max_rank + 1):
        if any(
            gold_is_hit(ref, context, rank)
            for ref in required_refs
        ):
            return 1.0 / rank
    return 0.0


def eval_context(
    question_id: str,
    gold_refs: list[dict[str, Any]],
    context: list[dict[str, Any]],
    config_name: str,
    method: str,
    top_k: int,
    candidate_k: int,
    window: int,
) -> dict[str, Any]:
    required = [
        ref
        for ref in gold_refs
        if ref.get("evidence_type") == "required_gold"
    ]
    optional = [
        ref
        for ref in gold_refs
        if ref.get("evidence_type") == "optional_gold"
    ]
    negative = [
        ref
        for ref in gold_refs
        if ref.get("evidence_type") == "negative_gold"
    ]
    decoy = [
        ref for ref in gold_refs if ref.get("evidence_type") == "decoy"
    ]
    row: dict[str, Any] = {
        "config_name": config_name,
        "retrieval_method": method,
        "top_k": top_k,
        "candidate_k": candidate_k,
        "context_window": window,
        "question_id": question_id,
        "required_gold_count": len(required),
        "optional_gold_count": len(optional),
        "negative_gold_count": len(negative),
        "decoy_count": len(decoy),
        "retrieved_context_count": len(context),
        "MRR_required_gold": mrr_required(required, context),
    }
    for k in K_VALUES:
        top = metric_top_context(context, k)
        required_hits = sum(
            gold_is_hit(ref, context, k) for ref in required
        )
        required_docs = {
            norm(ref.get("doc_id"))
            for ref in required
            if ref.get("doc_id")
        }
        retrieved_docs = {
            norm(item.get("doc_id"))
            for item in top
            if item.get("doc_id")
        }
        chunk_hits = sum(
            chunk_is_hit(ref, context, k) for ref in required
        )
        negative_hits = sum(
            gold_is_hit(ref, context, k) for ref in negative
        )
        decoy_hits = sum(
            gold_is_hit(ref, context, k) for ref in decoy
        )
        row[f"required_gold_retrieved@{k}"] = required_hits
        row[f"required_gold_recall@{k}"] = recall(
            required_hits,
            len(required),
        )
        row[f"gold_doc_recall@{k}"] = recall(
            len(required_docs & retrieved_docs),
            len(required_docs),
        )
        row[f"gold_chunk_recall@{k}"] = recall(
            chunk_hits,
            len(required),
        )
        row[f"negative_gold_recall@{k}"] = recall(
            negative_hits,
            len(negative),
        )
        row[f"decoy_retrieval_rate@{k}"] = recall(
            decoy_hits,
            len(top),
        )

    full_k = len(context)
    required_hits = sum(
        gold_is_hit(ref, context, full_k) for ref in required
    )
    required_docs = {
        norm(ref.get("doc_id"))
        for ref in required
        if ref.get("doc_id")
    }
    retrieved_docs = {
        norm(item.get("doc_id"))
        for item in metric_top_context(context, full_k)
        if item.get("doc_id")
    }
    chunk_hits = sum(
        chunk_is_hit(ref, context, full_k) for ref in required
    )
    negative_hits = sum(
        gold_is_hit(ref, context, full_k) for ref in negative
    )
    decoy_hits = sum(
        gold_is_hit(ref, context, full_k) for ref in decoy
    )
    row["required_gold_retrieved@full_context"] = required_hits
    row["required_gold_recall@full_context"] = recall(
        required_hits,
        len(required),
    )
    row["gold_doc_recall@full_context"] = recall(
        len(required_docs & retrieved_docs),
        len(required_docs),
    )
    row["gold_chunk_recall@full_context"] = recall(
        chunk_hits,
        len(required),
    )
    row["negative_gold_recall@full_context"] = recall(
        negative_hits,
        len(negative),
    )
    row["decoy_retrieval_rate@full_context"] = recall(
        decoy_hits,
        full_k,
    )
    return row

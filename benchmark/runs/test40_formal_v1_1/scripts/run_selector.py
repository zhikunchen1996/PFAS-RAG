from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

import common


CONFIG = "bge_llm_gpt51_pool60_bge30_llm10_fullchunk"
SOURCE_CONFIG = "bge_base_top10_pool60_nodoccap"
POOL_K = 60
SHORTLIST_K = 30
TOP_K = 10


def compact_text(text: str) -> str:
    return re.sub(r"\s+", " ", str(text)).strip()


def selector_payload(
    question: dict[str, str],
    candidates: list[dict[str, Any]],
) -> dict[str, Any]:
    blocks = []
    for index, hit in enumerate(candidates, start=1):
        citation = (
            hit.get("citation")
            or hit.get("citation_acs")
            or hit.get("source")
            or hit.get("doc_id")
            or "unknown"
        )
        blocks.append(
            f"ID: {index}\n"
            f"Section: {hit.get('section') or 'unknown'}\n"
            f"Source: {citation}\n"
            f"Chunk: {compact_text(hit.get('text', ''))}"
        )
    return {
        "question": question["question_text"],
        "instruction": (
            f"Select up to {TOP_K} candidate IDs in descending usefulness. "
            "Do not invent IDs. Return JSON: "
            '{"selected_ids":[1,2], "scores":{"1":9}, '
            '"reasons":{"1":"short reason"}}'
        ),
        "candidates": "\n\n".join(blocks),
    }


def parse_id(value: Any) -> int | None:
    if isinstance(value, int) and not isinstance(value, bool):
        return value
    text = str(value).strip()
    return int(text) if re.fullmatch(r"\d+", text) else None


def select_context(
    result: dict[str, Any],
    candidates: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    selected_values = result.get("selected_ids")
    if not isinstance(selected_values, list):
        raise RuntimeError("Selector response lacks selected_ids list")
    scores = result.get("scores") if isinstance(result.get("scores"), dict) else {}
    reasons = (
        result.get("reasons") if isinstance(result.get("reasons"), dict) else {}
    )
    selected_ids = []
    for value in selected_values:
        candidate_id = parse_id(value)
        if (
            candidate_id is not None
            and 1 <= candidate_id <= len(candidates)
            and candidate_id not in selected_ids
        ):
            selected_ids.append(candidate_id)
        if len(selected_ids) == TOP_K:
            break

    for candidate_id in range(1, len(candidates) + 1):
        if len(selected_ids) == TOP_K:
            break
        if candidate_id not in selected_ids:
            selected_ids.append(candidate_id)

    context = []
    for rank, candidate_id in enumerate(selected_ids, start=1):
        hit = dict(candidates[candidate_id - 1])
        try:
            score = float(
                scores.get(str(candidate_id), scores.get(candidate_id, 0))
            )
        except (TypeError, ValueError):
            score = 0.0
        hit.update(
            {
                "llm_rerank_rank": rank,
                "llm_relevance_score": score,
                "llm_reason": str(
                    reasons.get(
                        str(candidate_id),
                        reasons.get(candidate_id, ""),
                    )
                ),
            }
        )
        context.append(common.normalize_context_hit(hit, rank))
    return context


def load_shortlists(
    candidate_path: Path,
    expected_ids: list[str],
) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in common.read_jsonl(candidate_path):
        if str(row.get("config_name")) != SOURCE_CONFIG:
            continue
        grouped[str(row.get("question_id"))].append(row)
    if set(grouped) != set(expected_ids):
        raise RuntimeError("BGE candidate question membership differs")
    for qid, rows in grouped.items():
        rows.sort(key=lambda row: int(row.get("rank") or 999999))
        if len(rows) != POOL_K:
            raise RuntimeError(f"{qid}: expected {POOL_K} BGE candidates")
        identities = [
            (
                str(row.get("doc_id") or ""),
                str(row.get("chunk_id") or ""),
            )
            for row in rows
        ]
        if any(not all(value) for value in identities):
            raise RuntimeError(f"{qid}: incomplete BGE candidate identity")
        if len(identities) != len(set(identities)):
            raise RuntimeError(f"{qid}: duplicate BGE candidate")
        grouped[qid] = rows[:SHORTLIST_K]
    return grouped


def output_row(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "question_id": row["question_id"],
        "system_mode": "rag_end_to_end",
        "answer": "",
        "retrieved_context": row["selected_context"],
        "retrieval_config_name": CONFIG,
        "retrieval_method": "bge_llm_cascade",
        "retrieval_k": POOL_K,
        "bm25_k": POOL_K,
        "bge_shortlist_k": SHORTLIST_K,
        "top_k": TOP_K,
        "context_window": 0,
        "llm_rerank": True,
        "llm_rerank_mode": "short_selector",
        "llm_rerank_model": common.MODEL,
        "selector_input": "visible_question_only",
        "selector_temperature": 0,
        "selector_prompt": common.project_relative(common.SELECTOR_PROMPT),
        "selector_response_id": row["metadata"]["response_id"],
        "selector_response_model": row["metadata"]["response_model"],
        "selector_prompt_tokens": row["metadata"]["prompt_tokens"],
        "selector_cached_prompt_tokens": row["metadata"]["cached_prompt_tokens"],
        "selector_completion_tokens": row["metadata"]["completion_tokens"],
        "selector_total_tokens": row["metadata"]["total_tokens"],
        "selector_estimated_cost_usd": row["metadata"]["estimated_cost_usd"],
        "selector_latency_seconds": row["metadata"]["latency_seconds"],
        "selector_execution_sha256": row["execution_sha256"],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--retrieval-root", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    retrieval_root = Path(args.retrieval_root).expanduser().resolve()
    common.require_exact_path(
        retrieval_root,
        common.RETRIEVAL_RESULTS,
        label="Selector retrieval input",
    )
    candidate_path = retrieval_root / "bge_candidate_scores.jsonl"
    expected_ids = common.question_ids()
    questions = {
        row["question_id"]: row for row in common.read_csv(common.QUESTIONS)
    }
    shortlists = load_shortlists(candidate_path, expected_ids)
    prompt = common.SELECTOR_PROMPT.read_text(encoding="utf-8")
    items = [
        {
            "item_id": qid,
            "question_id": qid,
            "payload": selector_payload(questions[qid], shortlists[qid]),
            "candidates": shortlists[qid],
        }
        for qid in expected_ids
    ]

    def execution_hash(item: dict[str, Any]) -> str:
        request = common.json_request(
            system_prompt=prompt,
            payload=item["payload"],
            reasoning_effort=None,
            max_completion_tokens=None,
            temperature=0,
        )
        return common.payload_sha256(request)

    out = Path(args.out).expanduser().resolve()
    common.require_exact_path(
        out,
        common.SELECTOR_RESULTS,
        label="Selector output",
    )
    out.mkdir(parents=True, exist_ok=True)
    common.write_jsonl(
        out / "model_payloads.jsonl",
        [
            {
                "question_id": item["question_id"],
                "model_payload": item["payload"],
                "execution_sha256": execution_hash(item),
            }
            for item in items
        ],
    )
    if args.dry_run:
        print("DRY RUN PASS: 40 selector payloads built; no API calls.")
        return
    calls_path = out / "selector_calls.jsonl"
    if calls_path.exists() and not args.resume:
        raise RuntimeError(
            "Selector results already exist; use --resume to avoid duplicate calls"
        )

    def worker(item: dict[str, Any]) -> dict[str, Any]:
        result, metadata, request_hash = common.call_json(
            system_prompt=prompt,
            payload=item["payload"],
            reasoning_effort=None,
            max_completion_tokens=None,
            temperature=0,
        )
        return {
            "item_id": item["item_id"],
            "question_id": item["question_id"],
            "execution_sha256": request_hash,
            "selected_context": select_context(result, item["candidates"]),
            "selector_result": result,
            "metadata": metadata,
        }

    rows = common.run_resumable(
        items=items,
        key=lambda row: str(row["item_id"]),
        expected_execution_hash=execution_hash,
        worker=worker,
        output=calls_path,
        workers=args.workers,
        resume=args.resume,
        label="Test40 BGE-LLM selector",
    )
    outputs = [output_row(row) for row in rows]
    common.validate_contexts(
        outputs,
        expected_count=TOP_K,
        source="BGE-LLM",
    )
    common.write_jsonl(
        out / "retrieval_outputs" / f"rag_outputs_{CONFIG}.jsonl",
        outputs,
    )
    common.write_json(
        out / "run_manifest.json",
        {
            "protocol_id": "test40_formal_v1_bge_llm_selector",
            "status": "complete",
            "question_count": 40,
            "model": common.MODEL,
            "required_snapshot": common.EXPECTED_MODEL,
            "temperature": 0,
            "reasoning_effort": "provider_default_not_sent",
            "selector_input": "visible_question_only",
            "full_candidate_chunks": True,
            "pool_k": POOL_K,
            "bge_shortlist_k": SHORTLIST_K,
            "final_top_k": TOP_K,
            "questions_sha256": common.sha256(common.QUESTIONS),
            "candidate_file_sha256": common.sha256(candidate_path),
            "prompt_sha256": common.sha256(common.SELECTOR_PROMPT),
            "api_calls": len(rows),
            "total_tokens": sum(
                int(row["metadata"]["total_tokens"]) for row in rows
            ),
            "estimated_cost_usd": sum(
                float(row["metadata"]["estimated_cost_usd"]) for row in rows
            ),
            "latency_seconds_sum": sum(
                float(row["metadata"]["latency_seconds"]) for row in rows
            ),
            "resume_hash_validated": True,
        },
    )


if __name__ == "__main__":
    main()

from __future__ import annotations

import csv
import hashlib
import json
import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Callable

from dotenv import load_dotenv
from openai import OpenAI


PACKAGE = Path(__file__).resolve().parents[1]
ROOT = PACKAGE.parents[2]
RESULTS = PACKAGE / "results"
RETRIEVAL_RESULTS = RESULTS / "retrieval"
SELECTOR_RESULTS = RESULTS / "selector"
L1_RESULTS = RESULTS / "l1"
GENERATION_RESULTS = RESULTS / "generation"
L15_RESULTS = RESULTS / "l15"
L3_RESULTS = RESULTS / "l3"
FROZEN_V3 = ROOT / "benchmark/frozen_v3"
FROZEN_JUDGE = FROZEN_V3 / "judge"
TEST40_REFERENCE = ROOT / "benchmark/runs/l3_gold_reference_test40_v1"

QUESTIONS = FROZEN_V3 / "input/questions_test40.csv"
GOLD = FROZEN_V3 / "gold/chunk_based_gold.jsonl"
REFERENCE_LEDGER = (
    PACKAGE / "frozen/reference_claim_ledgers_test40_scoring_v2.jsonl"
)
REFERENCE_FREEZE_MANIFEST = (
    PACKAGE / "frozen/scoring_reference_v2_manifest.json"
)

SELECTOR_PROMPT = (
    FROZEN_V3 / "prompts/retrieval/bge_llm_selector_v3.txt"
)
TAGGER_PROMPT = (
    FROZEN_V3 / "prompts/evaluation/soft_eligibility_tagger_v3.txt"
)
ANSWER_PROMPT = (
    FROZEN_V3 / "prompts/evaluation/rag_answer_prompt_soft_tags_v3.txt"
)
L15_PROMPT = FROZEN_JUDGE / "prompts/l15_claim_citation_support_v2.txt"
L3_PROMPT = (
    PACKAGE / "prompts/l3_gold_referenced_judge_v2.txt"
)

MODEL = "gpt-5.1"
EXPECTED_MODEL = "gpt-5.1-2025-11-13"
PRICE_INPUT = 1.25
PRICE_CACHED_INPUT = 0.125
PRICE_OUTPUT = 10.0
_thread_state = threading.local()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_number}: {exc}") from exc
    return rows


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        raise ValueError(f"Refusing to write empty CSV: {path}")
    fields: list[str] = []
    for row in rows:
        for field in row:
            if field not in fields:
                fields.append(field)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fields,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload_sha256(value: Any) -> str:
    encoded = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def project_relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve()))


def require_exact_path(value: Path, expected: Path, *, label: str) -> None:
    if value.resolve() != expected.resolve():
        raise RuntimeError(
            f"{label} must use canonical path {project_relative(expected)}"
        )


def question_ids() -> list[str]:
    rows = read_csv(QUESTIONS)
    ids = [str(row.get("question_id", "")).strip() for row in rows]
    if len(ids) != 40 or len(ids) != len(set(ids)) or any(not qid for qid in ids):
        raise RuntimeError("Frozen Test40 question membership is invalid")
    return ids


def ordered_rows(
    rows: list[dict[str, Any]],
    expected_ids: list[str],
    *,
    source: str,
) -> list[dict[str, Any]]:
    by_id: dict[str, dict[str, Any]] = {}
    for row in rows:
        qid = str(row.get("question_id", ""))
        if qid in by_id:
            raise RuntimeError(f"{source}: duplicate question_id {qid}")
        by_id[qid] = row
    missing = sorted(set(expected_ids) - set(by_id))
    extra = sorted(set(by_id) - set(expected_ids))
    if missing or extra:
        raise RuntimeError(
            f"{source}: question membership mismatch; "
            f"missing={missing}, extra={extra}"
        )
    return [by_id[qid] for qid in expected_ids]


def normalize_context_hit(
    hit: dict[str, Any],
    rank: int,
) -> dict[str, Any]:
    chunk_id = hit.get("chunk_id")
    if chunk_id is None or chunk_id == "":
        chunk_id = hit.get("chunk")
    return {
        "rank": rank,
        "doc_id": str(hit.get("doc_id") or hit.get("source") or ""),
        "chunk_id": "" if chunk_id is None else str(chunk_id),
        "section": str(hit.get("section") or ""),
        "text": str(hit.get("text") or ""),
        "score": hit.get("score", hit.get("rerank_score", "")),
        "retrieval_source": str(hit.get("retrieval_source") or ""),
        "dense_rank": hit.get("dense_rank"),
        "bm25_rank": hit.get("bm25_rank"),
        "bm25_score": hit.get("bm25_score", ""),
        "rerank_score": hit.get("rerank_score", ""),
        "citation": (
            hit.get("citation")
            or hit.get("citation_acs")
            or hit.get("citation_apa")
            or hit.get("title")
            or hit.get("source", "")
        ),
        "cross_encoder_score": hit.get("cross_encoder_score"),
        "cross_encoder_score_norm": hit.get("cross_encoder_score_norm"),
        "selector_score": hit.get("selector_score"),
        "original_rank": hit.get("original_rank"),
        "llm_rerank_rank": hit.get("llm_rerank_rank"),
        "llm_relevance_score": hit.get("llm_relevance_score"),
        "llm_reason": hit.get("llm_reason", ""),
    }


def validate_contexts(
    rows: list[dict[str, Any]],
    *,
    expected_count: int,
    source: str,
) -> None:
    for row in rows:
        qid = str(row.get("question_id", ""))
        context = row.get("retrieved_context")
        if not isinstance(context, list) or len(context) != expected_count:
            raise RuntimeError(
                f"{source}/{qid}: expected {expected_count} chunks"
            )
        identities = []
        for hit in context:
            identity = (
                str(hit.get("doc_id") or ""),
                str(hit.get("chunk_id") or ""),
            )
            if not all(identity) or not str(hit.get("text") or "").strip():
                raise RuntimeError(f"{source}/{qid}: incomplete chunk")
            identities.append(identity)
        if len(identities) != len(set(identities)):
            raise RuntimeError(f"{source}/{qid}: duplicate final chunk")


def estimate_cost(metadata: dict[str, Any]) -> float:
    prompt = int(metadata.get("prompt_tokens", 0) or 0)
    cached = int(metadata.get("cached_prompt_tokens", 0) or 0)
    completion = int(metadata.get("completion_tokens", 0) or 0)
    return (
        max(0, prompt - cached) * PRICE_INPUT
        + cached * PRICE_CACHED_INPUT
        + completion * PRICE_OUTPUT
    ) / 1_000_000


def client() -> OpenAI:
    value = getattr(_thread_state, "client", None)
    if value is None:
        if not os.getenv("OPENAI_API_KEY"):
            raise RuntimeError("OPENAI_API_KEY is missing")
        value = OpenAI(timeout=600, max_retries=0)
        _thread_state.client = value
    return value


def response_metadata(response: Any, latency: float) -> dict[str, Any]:
    if str(response.model) != EXPECTED_MODEL:
        raise RuntimeError(
            f"Unexpected model snapshot {response.model}; "
            f"expected {EXPECTED_MODEL}"
        )
    finish_reason = str(response.choices[0].finish_reason or "")
    if finish_reason != "stop":
        raise RuntimeError(f"Model call did not finish normally: {finish_reason}")
    usage = response.usage
    details = getattr(usage, "prompt_tokens_details", None)
    metadata = {
        "response_id": str(response.id),
        "response_model": str(response.model),
        "system_fingerprint": str(response.system_fingerprint or ""),
        "finish_reason": finish_reason,
        "prompt_tokens": int(usage.prompt_tokens or 0),
        "cached_prompt_tokens": int(
            getattr(details, "cached_tokens", 0) or 0
        ),
        "completion_tokens": int(usage.completion_tokens or 0),
        "total_tokens": int(usage.prompt_tokens or 0)
        + int(usage.completion_tokens or 0),
        "latency_seconds": latency,
    }
    metadata["estimated_cost_usd"] = estimate_cost(metadata)
    return metadata


def call_json(
    *,
    system_prompt: str,
    payload: dict[str, Any],
    reasoning_effort: str | None,
    max_completion_tokens: int | None,
    temperature: float | None,
) -> tuple[dict[str, Any], dict[str, Any], str]:
    request = json_request(
        system_prompt=system_prompt,
        payload=payload,
        reasoning_effort=reasoning_effort,
        max_completion_tokens=max_completion_tokens,
        temperature=temperature,
    )
    started = time.perf_counter()
    response = client().chat.completions.create(**request)
    latency = time.perf_counter() - started
    metadata = response_metadata(response, latency)
    raw = response.choices[0].message.content or "{}"
    result = json.loads(raw)
    if not isinstance(result, dict):
        raise RuntimeError("JSON response is not an object")
    return result, metadata, payload_sha256(request)


def json_request(
    *,
    system_prompt: str,
    payload: dict[str, Any],
    reasoning_effort: str | None,
    max_completion_tokens: int | None,
    temperature: float | None,
) -> dict[str, Any]:
    request: dict[str, Any] = {
        "model": MODEL,
        "response_format": {"type": "json_object"},
        "messages": [
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": json.dumps(payload, ensure_ascii=False),
            },
        ],
    }
    if max_completion_tokens is not None:
        request["max_completion_tokens"] = max_completion_tokens
    if reasoning_effort is not None:
        request["reasoning_effort"] = reasoning_effort
    if temperature is not None:
        request["temperature"] = temperature
    return request


def call_text(
    *,
    system_prompt: str,
    user_prompt: str,
    temperature: float,
) -> tuple[str, dict[str, Any], str]:
    request = text_request(
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        temperature=temperature,
    )
    started = time.perf_counter()
    response = client().chat.completions.create(**request)
    latency = time.perf_counter() - started
    metadata = response_metadata(response, latency)
    return (
        response.choices[0].message.content or "",
        metadata,
        payload_sha256(request),
    )


def text_request(
    *,
    system_prompt: str,
    user_prompt: str,
    temperature: float,
) -> dict[str, Any]:
    return {
        "model": MODEL,
        "temperature": temperature,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    }


def run_resumable(
    *,
    items: list[dict[str, Any]],
    key: Callable[[dict[str, Any]], str],
    expected_execution_hash: Callable[[dict[str, Any]], str],
    worker: Callable[[dict[str, Any]], dict[str, Any]],
    output: Path,
    workers: int,
    resume: bool,
    label: str,
) -> list[dict[str, Any]]:
    if workers < 1:
        raise ValueError("workers must be at least one")
    order = [key(item) for item in items]
    if len(order) != len(set(order)):
        raise RuntimeError(f"{label}: duplicate scheduled keys")

    existing: dict[str, dict[str, Any]] = {}
    if resume and output.exists():
        for row in read_jsonl(output):
            item_key = key(row)
            if item_key in existing:
                raise RuntimeError(f"{label}: duplicate stored key {item_key}")
            existing[item_key] = row
        scheduled = {key(item): item for item in items}
        extra = sorted(set(existing) - set(scheduled))
        if extra:
            raise RuntimeError(f"{label}: unexpected stored keys {extra}")
        for item_key, row in existing.items():
            expected = expected_execution_hash(scheduled[item_key])
            if row.get("execution_sha256") != expected:
                raise RuntimeError(
                    f"{label}: resume hash mismatch for {item_key}"
                )

    pending = [item for item in items if key(item) not in existing]
    failures: list[tuple[str, Exception]] = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(worker, item): item for item in pending}
        for future in as_completed(futures):
            item = futures[future]
            item_key = key(item)
            try:
                row = future.result()
            except Exception as exc:
                failures.append((item_key, exc))
                print(f"[{label} error] {item_key}: {exc}", flush=True)
                continue
            if key(row) != item_key:
                failures.append(
                    (item_key, RuntimeError("worker returned a different key"))
                )
                continue
            existing[item_key] = row
            write_jsonl(
                output,
                [existing[value] for value in order if value in existing],
            )
            print(
                f"[{label}] completed={len(existing)}/{len(items)} "
                f"{item_key}",
                flush=True,
            )

    if failures:
        details = "; ".join(f"{item}: {exc}" for item, exc in failures)
        raise RuntimeError(
            f"{label}: {len(failures)} call(s) failed; successful calls were "
            f"saved and may be resumed. {details}"
        )
    if set(existing) != set(order):
        raise RuntimeError(f"{label}: incomplete output")
    return [existing[value] for value in order]


load_dotenv(ROOT / ".env", override=False)

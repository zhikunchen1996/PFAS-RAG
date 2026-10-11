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
FROZEN = PACKAGE / "frozen"
PROMPTS = PACKAGE / "prompts"
RESULTS = PACKAGE / "results"
GENERATION_RESULTS = RESULTS / "generation"
L3_RESULTS = RESULTS / "l3"

QUESTIONS = FROZEN / "questions_test40.csv"
RETRIEVAL = FROZEN / "bge_llm_top10.jsonl"
TAGS = FROZEN / "bge_llm_common_tags.jsonl"
REFERENCE_LEDGER = (
    FROZEN / "reference_claim_ledgers_test40_scoring_v2.jsonl"
)
SHARED_PROMPT = PROMPTS / "shared_system_v1.txt"
DIRECT_PROMPT = PROMPTS / "direct_user_v1.txt"
RAG_PROMPT = PROMPTS / "rag_user_v1.txt"
L3_PROMPT = PROMPTS / "l3_gold_referenced_judge_v2.txt"

OPENAI_MODEL = "gpt-5.1"
OPENAI_SNAPSHOT = "gpt-5.1-2025-11-13"
OPENAI_INPUT_PRICE = 1.25
OPENAI_CACHED_INPUT_PRICE = 0.125
OPENAI_OUTPUT_PRICE = 10.0
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
    ids = [
        str(row.get("question_id", "")).strip()
        for row in read_csv(QUESTIONS)
    ]
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
            f"{source}: membership mismatch; missing={missing}, extra={extra}"
        )
    return [by_id[qid] for qid in expected_ids]


def validate_contexts(rows: list[dict[str, Any]]) -> None:
    for row in rows:
        qid = str(row.get("question_id", ""))
        context = row.get("retrieved_context")
        if not isinstance(context, list) or len(context) != 10:
            raise RuntimeError(f"{qid}: expected ten complete chunks")
        identities = []
        for hit in context:
            chunk_id = hit.get("chunk_id")
            if chunk_id is None or chunk_id == "":
                chunk_id = hit.get("chunk")
            identity = (
                str(hit.get("doc_id") or ""),
                "" if chunk_id is None else str(chunk_id),
            )
            if not all(identity) or not str(hit.get("text") or "").strip():
                raise RuntimeError(f"{qid}: incomplete chunk")
            identities.append(identity)
        if len(identities) != len(set(identities)):
            raise RuntimeError(f"{qid}: duplicate final chunk")


def openai_client() -> OpenAI:
    value = getattr(_thread_state, "openai_client", None)
    if value is None:
        if not os.getenv("OPENAI_API_KEY"):
            raise RuntimeError("OPENAI_API_KEY is missing")
        value = OpenAI(timeout=600, max_retries=0)
        _thread_state.openai_client = value
    return value


def openai_metadata(response: Any, latency: float) -> dict[str, Any]:
    if str(response.model) != OPENAI_SNAPSHOT:
        raise RuntimeError(
            f"Unexpected model snapshot {response.model}; "
            f"expected {OPENAI_SNAPSHOT}"
        )
    finish_reason = str(response.choices[0].finish_reason or "")
    if finish_reason != "stop":
        raise RuntimeError(f"Model call did not finish normally: {finish_reason}")
    usage = response.usage
    details = getattr(usage, "prompt_tokens_details", None)
    prompt = int(usage.prompt_tokens or 0)
    cached = int(getattr(details, "cached_tokens", 0) or 0)
    completion = int(usage.completion_tokens or 0)
    cost = (
        max(0, prompt - cached) * OPENAI_INPUT_PRICE
        + cached * OPENAI_CACHED_INPUT_PRICE
        + completion * OPENAI_OUTPUT_PRICE
    ) / 1_000_000
    return {
        "response_id": str(response.id),
        "response_model": str(response.model),
        "system_fingerprint": str(response.system_fingerprint or ""),
        "finish_reason": finish_reason,
        "prompt_tokens": prompt,
        "cached_prompt_tokens": cached,
        "completion_tokens": completion,
        "total_tokens": prompt + completion,
        "estimated_cost_usd": cost,
        "latency_seconds": latency,
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
        if set(existing) - set(scheduled):
            raise RuntimeError(f"{label}: stored output contains extra keys")
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
                f"[{label}] completed={len(existing)}/{len(items)} {item_key}",
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

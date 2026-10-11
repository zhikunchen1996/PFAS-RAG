from __future__ import annotations

import csv
import hashlib
import json
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Callable

from dotenv import load_dotenv
from openai import OpenAI


PACKAGE = Path(__file__).resolve().parents[1]
ROOT = PACKAGE.parents[2]
FROZEN_V3 = ROOT / "benchmark/frozen_v3"

QUESTIONS = FROZEN_V3 / "input/questions_test40.csv"
GOLD = FROZEN_V3 / "gold/chunk_based_gold.jsonl"
AUTHOR_REVIEW = FROZEN_V3 / "methods/author_review_record.json"
GOLD_AUTHOR_REGISTER = FROZEN_V3 / "methods/gold_author_review_register.csv"
CHROMA_PATH = ROOT / "data/chroma"
COLLECTION_NAME = (
    "rag_documents_bge_large_en_v1_5_sent256_overlap2_corpus434_repaired_v1"
)

SOURCE_PACKETS = PACKAGE / "reference_build/inputs/source_packets.jsonl"
TASK_COMPONENTS = (
    PACKAGE / "reference_build/task_components/task_components.jsonl"
)
REFERENCE_PACKETS = PACKAGE / "reference_build/inputs/reference_packets.jsonl"
DRAFTS = PACKAGE / "reference_build/drafts/model_a_ledgers.jsonl"

EXPECTED_RESPONSE_MODEL = "gpt-5.1-2025-11-13"

load_dotenv(ROOT / ".env", override=False)

OPENAI_PRICES_PER_MILLION = {
    "gpt-5.1": {"input": 1.25, "cached_input": 0.125, "output": 10.0},
    "gpt-5.1-2025-11-13": {
        "input": 1.25,
        "cached_input": 0.125,
        "output": 10.0,
    },
}


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


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


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


def openai_client() -> OpenAI:
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is missing")
    return OpenAI(timeout=300, max_retries=2)


def estimate_cost(metadata: dict[str, Any], model: str) -> float:
    prices = OPENAI_PRICES_PER_MILLION.get(model)
    if not prices:
        return 0.0
    prompt = int(metadata.get("prompt_tokens", 0) or 0)
    cached = int(metadata.get("cached_prompt_tokens", 0) or 0)
    output = int(metadata.get("completion_tokens", 0) or 0)
    return (
        max(0, prompt - cached) * prices["input"]
        + cached * prices["cached_input"]
        + output * prices["output"]
    ) / 1_000_000


def call_openai_json(
    *,
    system_prompt: str,
    payload: dict[str, Any],
    model: str = "gpt-5.1",
    reasoning_effort: str = "low",
    max_completion_tokens: int,
) -> tuple[dict[str, Any], dict[str, Any]]:
    request = {
        "model": model,
        "reasoning_effort": reasoning_effort,
        "max_completion_tokens": max_completion_tokens,
        "response_format": {"type": "json_object"},
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": json.dumps(payload, ensure_ascii=False)},
        ],
    }
    started = time.perf_counter()
    response = openai_client().chat.completions.create(**request)
    latency = time.perf_counter() - started
    finish_reason = str(response.choices[0].finish_reason or "")
    if finish_reason != "stop":
        raise RuntimeError(f"OpenAI call did not finish normally: {finish_reason}")
    result = json.loads(response.choices[0].message.content or "")
    usage = response.usage
    details = getattr(usage, "prompt_tokens_details", None)
    metadata = {
        "request_model": model,
        "response_model": str(response.model),
        "response_id": str(response.id),
        "reasoning_effort": reasoning_effort,
        "temperature": "provider_default_not_sent",
        "max_completion_tokens": max_completion_tokens,
        "finish_reason": finish_reason,
        "prompt_tokens": int(usage.prompt_tokens or 0),
        "cached_prompt_tokens": int(getattr(details, "cached_tokens", 0) or 0),
        "completion_tokens": int(usage.completion_tokens or 0),
        "total_tokens": int(usage.total_tokens or 0),
        "latency_seconds": latency,
        "request_sha256": payload_sha256(request),
    }
    if metadata["response_model"] != EXPECTED_RESPONSE_MODEL:
        raise RuntimeError(
            f"Unexpected response model: {metadata['response_model']}"
        )
    metadata["estimated_cost_usd"] = estimate_cost(metadata, model)
    return result, metadata


def run_parallel(
    *,
    items: list[dict[str, Any]],
    worker: Callable[[dict[str, Any]], dict[str, Any]],
    key: Callable[[dict[str, Any]], str],
    output: Path,
    workers: int,
    resume: bool,
) -> list[dict[str, Any]]:
    existing = {
        key(row): row
        for row in (read_jsonl(output) if resume and output.exists() else [])
    }
    pending = [row for row in items if key(row) not in existing]
    failures: list[tuple[str, Exception]] = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(worker, row): row for row in pending}
        for future in as_completed(futures):
            source = futures[future]
            try:
                row = future.result()
            except Exception as exc:
                failures.append((key(source), exc))
                print(f"[error] {key(source)}: {exc}", flush=True)
                continue
            existing[key(row)] = row
            ordered = [existing[key(item)] for item in items if key(item) in existing]
            write_jsonl(output, ordered)
            print(f"[{len(existing)}/{len(items)}] {key(row)}", flush=True)
    if failures:
        detail = "; ".join(f"{item}: {exc}" for item, exc in failures)
        raise RuntimeError(f"{len(failures)} item(s) failed: {detail}")
    return [existing[key(item)] for item in items]

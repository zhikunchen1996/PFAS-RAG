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
STAGE4 = ROOT / "benchmark/runs/stage4_gpt51_dev13_pilot_v1"

QUESTIONS = FROZEN_V3 / "input/questions_dev13.csv"
GOLD = FROZEN_V3 / "gold/chunk_based_gold.jsonl"
BOUNDARIES = STAGE4 / "judge_calibration/citation_blind_boundaries_dev13.csv"
AUTHOR_REVIEW = FROZEN_V3 / "methods/author_review_record.json"
GOLD_AUTHOR_REGISTER = (
    FROZEN_V3 / "methods/gold_author_review_register.csv"
)

PACKETS = PACKAGE / "reference_build/inputs/reference_packets.jsonl"
DRAFTS = PACKAGE / "reference_build/drafts/model_a_drafts.jsonl"
REVIEWS = PACKAGE / "reference_build/reviews/model_b_reviews.jsonl"
HUMAN_CANDIDATES = PACKAGE / "human_review/reference_candidates.jsonl"

load_dotenv(ROOT / ".env", override=False)

OPENAI_PRICES_PER_MILLION = {
    "gpt-5.1": {
        "input": 1.25,
        "cached_input": 0.125,
        "output": 10.0,
    },
    "gpt-5.1-2025-11-13": {
        "input": 1.25,
        "cached_input": 0.125,
        "output": 10.0,
    },
    "gpt-4.1-2025-04-14": {
        "input": 2.0,
        "cached_input": 0.5,
        "output": 8.0,
    },
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0]) if rows else []
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


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


def by_question(rows: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    result: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        result.setdefault(str(row["question_id"]), []).append(row)
    return result


def openai_client() -> OpenAI:
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is missing")
    return OpenAI(timeout=300, max_retries=2)


def response_metadata(response: Any, latency: float) -> dict[str, Any]:
    usage = response.usage
    details = getattr(usage, "prompt_tokens_details", None)
    cached = int(getattr(details, "cached_tokens", 0) or 0)
    prompt_tokens = int(usage.prompt_tokens or 0)
    completion_tokens = int(usage.completion_tokens or 0)
    return {
        "response_id": str(response.id),
        "response_model": str(response.model),
        "system_fingerprint": str(response.system_fingerprint or ""),
        "finish_reason": str(response.choices[0].finish_reason or ""),
        "prompt_tokens": prompt_tokens,
        "cached_prompt_tokens": cached,
        "completion_tokens": completion_tokens,
        "total_tokens": prompt_tokens + completion_tokens,
        "latency_seconds": latency,
    }


def estimate_openai_cost(metadata: dict[str, Any], model: str) -> float:
    if model not in OPENAI_PRICES_PER_MILLION:
        return 0.0
    prices = OPENAI_PRICES_PER_MILLION[model]
    prompt = int(metadata.get("prompt_tokens", 0) or 0)
    cached = int(metadata.get("cached_prompt_tokens", 0) or 0)
    output = int(metadata.get("completion_tokens", 0) or 0)
    noncached = max(0, prompt - cached)
    return (
        noncached * prices["input"]
        + cached * prices["cached_input"]
        + output * prices["output"]
    ) / 1_000_000


def call_openai_json(
    *,
    system_prompt: str,
    payload: dict[str, Any],
    model: str,
    reasoning_effort: str,
    max_completion_tokens: int,
    temperature: float | None = None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    request = {
        "model": model,
        "max_completion_tokens": max_completion_tokens,
        "response_format": {"type": "json_object"},
        "messages": [
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": json.dumps(payload, ensure_ascii=False),
            },
        ],
    }
    if reasoning_effort != "none":
        request["reasoning_effort"] = reasoning_effort
    if temperature is not None:
        request["temperature"] = temperature
    started = time.perf_counter()
    response = openai_client().chat.completions.create(**request)
    latency = time.perf_counter() - started
    finish_reason = str(response.choices[0].finish_reason or "")
    if finish_reason != "stop":
        raise RuntimeError(f"OpenAI call did not finish normally: {finish_reason}")
    text = response.choices[0].message.content or ""
    result = json.loads(text)
    metadata = {
        "request_model": model,
        "reasoning_effort": reasoning_effort,
        "temperature": (
            temperature if temperature is not None else "provider_default_not_sent"
        ),
        "max_completion_tokens": max_completion_tokens,
        "request_sha256": payload_sha256(request),
        **response_metadata(response, latency),
    }
    metadata["estimated_cost_usd"] = estimate_openai_cost(metadata, model)
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
    if not items and not output.exists():
        write_jsonl(output, [])
    failures: list[tuple[str, Exception]] = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(worker, row): row for row in pending}
        for future in as_completed(futures):
            source = futures[future]
            try:
                row = future.result()
            except Exception as exc:
                item_key = key(source)
                failures.append((item_key, exc))
                print(f"[error] {item_key}: {exc}", flush=True)
                continue
            existing[key(row)] = row
            ordered = [existing[key(item)] for item in items if key(item) in existing]
            write_jsonl(output, ordered)
            print(f"[{len(existing)}/{len(items)}] {key(row)}", flush=True)
    if failures:
        details = "; ".join(f"{item_key}: {exc}" for item_key, exc in failures)
        raise RuntimeError(
            f"{len(failures)} parallel item(s) failed; successful rows were saved: "
            f"{details}"
        )
    return [existing[key(row)] for row in items]


def compact_gold(row: dict[str, Any]) -> dict[str, Any]:
    fields = [
        "evidence_id",
        "evidence_type",
        "doc_id",
        "chunk_id",
        "exact_evidence_span",
        "supported_claim",
        "does_not_support",
        "PFAS_compound",
        "matrix",
        "method_or_material",
        "endpoint",
        "numerical_value",
        "unit",
        "protocol_detail",
        "limitation",
        "supports_universal_claim",
        "author_review_decision",
    ]
    return {field: row.get(field, "") for field in fields}

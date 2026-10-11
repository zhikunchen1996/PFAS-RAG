from __future__ import annotations

import csv
import hashlib
import json
import re
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from openai import OpenAI


JUDGE = Path(__file__).resolve().parents[1]
V3 = JUDGE.parent
ROOT = V3.parents[1]
load_dotenv(ROOT / ".env")

QUESTIONS_DEV = V3 / "input/questions_dev13.csv"
QUESTIONS_TEST = V3 / "input/questions_test40.csv"
QUESTIONS_ALL = V3 / "input/questions_all53.csv"
GOLD = V3 / "gold/chunk_based_gold.jsonl"

MODEL = "gpt-5.1"
EXPECTED_MODEL_SNAPSHOT = "gpt-5.1-2025-11-13"
REASONING_EFFORT = "medium"
CRITERIA = (
    "scientific_correctness",
    "question_fulfillment",
    "scope_and_calibration",
    "practical_usefulness",
)
PREFERENCES = {"A", "B", "tie"}
CITATION_RE = re.compile(r"\[C(\d+)\]", re.IGNORECASE)
IDENTITY_LEAK_PATTERNS = {
    "bge_label": re.compile(r"\bbge(?:-llm|_llm)?\b", re.IGNORECASE),
    "explicit_hybrid_system_label": re.compile(
        r"\bhybrid\s+(?:retrieval|retriever|rag|system|pipeline|configuration)\b",
        re.IGNORECASE,
    ),
    "selector_metadata": re.compile(
        r"\b(?:selector_score|retrieval_config|rerank_score|chunk_id)\b",
        re.IGNORECASE,
    ),
    "question_id": re.compile(r"\b(?:NQ\d+|WF10_[A-Z0-9]+)\b"),
}

# USD per one million tokens. These values are versioned protocol metadata,
# not fetched dynamically.
PRICE_INPUT = 1.25
PRICE_CACHED_INPUT = 0.125
PRICE_OUTPUT = 10.00


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def read_jsonl(path: Path) -> list[dict[str, Any]]:
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
    raw = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode()
    return hashlib.sha256(raw).hexdigest()


def strip_citations(answer: str) -> str:
    text = CITATION_RE.sub("", answer)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r" {2,}", " ", text)
    return text.strip()


def identity_leak_findings(answer: str) -> list[dict[str, Any]]:
    findings = []
    for name, pattern in IDENTITY_LEAK_PATTERNS.items():
        matches = pattern.findall(answer)
        if matches:
            findings.append(
                {
                    "pattern": name,
                    "match_count": len(matches),
                }
            )
    return findings


def by_question(rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    indexed: dict[str, dict[str, Any]] = {}
    for row in rows:
        qid = str(row["question_id"])
        if qid in indexed:
            raise ValueError(f"Duplicate question_id: {qid}")
        indexed[qid] = row
    return indexed


def ordered_for_questions(
    rows: list[dict[str, Any]],
    questions: list[dict[str, Any]],
    *,
    source_name: str,
) -> list[dict[str, Any]]:
    indexed = by_question(rows)
    expected = [str(row["question_id"]) for row in questions]
    if len(expected) != len(set(expected)):
        raise ValueError("Question file contains duplicate question_id values")
    missing = sorted(set(expected) - set(indexed))
    extra = sorted(set(indexed) - set(expected))
    if missing or extra:
        raise ValueError(
            f"{source_name}: question membership mismatch; "
            f"missing={missing}, extra={extra}"
        )
    return [indexed[qid] for qid in expected]


def grouped_gold(rows: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["question_id"])].append(row)
    return grouped


def visible_gold(rows: list[dict[str, Any]]) -> list[dict[str, str]]:
    """Return the non-exhaustive pre-answer gold without provenance metadata."""
    return [
        {
            "evidence_type": str(row.get("evidence_type", "")),
            "evidence_span": str(row.get("exact_evidence_span", "")),
            "supported_claim": str(row.get("supported_claim", "")),
            "known_limitation": str(row.get("does_not_support", "")),
        }
        for row in rows
        if str(row.get("evidence_type", "")) != "decoy"
    ]


def task_boundaries(question: dict[str, Any]) -> dict[str, str]:
    return {
        "must_include": str(question.get("must_include", "")),
        "must_not_claim": str(question.get("must_not_claim", "")),
    }


def deterministic_first_left(
    question_id: str,
    left_label: str,
    right_label: str,
) -> bool:
    digest = hashlib.sha256(
        f"frozen-judge-2026-07-28::{question_id}::{left_label}::"
        f"{right_label}".encode()
    ).digest()
    return digest[0] % 2 == 0


def mapped_preference(
    preference: str,
    assignment: dict[str, str],
) -> str:
    if preference == "tie":
        return "tie"
    if preference not in {"A", "B"}:
        raise ValueError(f"Invalid preference: {preference}")
    return assignment[preference]


def validate_judge_result(result: dict[str, Any]) -> None:
    preferences = result.get("criterion_preferences")
    rationales = result.get("criterion_rationales")
    if not isinstance(preferences, dict) or not isinstance(rationales, dict):
        raise ValueError("Missing criterion_preferences or criterion_rationales")
    for criterion in CRITERIA:
        if preferences.get(criterion) not in PREFERENCES:
            raise ValueError(f"Invalid preference for {criterion}")
        if not str(rationales.get(criterion, "")).strip():
            raise ValueError(f"Missing rationale for {criterion}")


def call_json_judge(
    *,
    prompt: str,
    payload: dict[str, Any],
    model: str = MODEL,
    reasoning_effort: str = REASONING_EFFORT,
    max_completion_tokens: int = 12000,
) -> dict[str, Any]:
    started = time.perf_counter()
    response = OpenAI(timeout=600, max_retries=2).chat.completions.create(
        model=model,
        reasoning_effort=reasoning_effort,
        response_format={"type": "json_object"},
        max_completion_tokens=max_completion_tokens,
        messages=[
            {
                "role": "system",
                "content": prompt,
            },
            {
                "role": "user",
                "content": json.dumps(payload, ensure_ascii=False),
            },
        ],
    )
    if str(response.model) != EXPECTED_MODEL_SNAPSHOT:
        raise RuntimeError(
            "Unexpected judge snapshot: "
            f"{response.model}; expected {EXPECTED_MODEL_SNAPSHOT}"
        )
    latency = time.perf_counter() - started
    raw = response.choices[0].message.content or "{}"
    finish_reason = str(response.choices[0].finish_reason or "")
    if finish_reason != "stop":
        raise RuntimeError(
            f"Judge response did not finish normally: {finish_reason}"
        )
    result = json.loads(raw)
    usage = response.usage
    prompt_tokens = int(usage.prompt_tokens or 0)
    completion_tokens = int(usage.completion_tokens or 0)
    cached_tokens = 0
    details = getattr(usage, "prompt_tokens_details", None)
    if details is not None:
        cached_tokens = int(getattr(details, "cached_tokens", 0) or 0)
    noncached_tokens = max(0, prompt_tokens - cached_tokens)
    cost = (
        noncached_tokens * PRICE_INPUT
        + cached_tokens * PRICE_CACHED_INPUT
        + completion_tokens * PRICE_OUTPUT
    ) / 1_000_000
    return {
        "judge_result": result,
        "response_id": str(response.id),
        "response_model": str(response.model),
        "finish_reason": finish_reason,
        "prompt_tokens": prompt_tokens,
        "cached_prompt_tokens": cached_tokens,
        "completion_tokens": completion_tokens,
        "total_tokens": prompt_tokens + completion_tokens,
        "estimated_cost_usd": cost,
        "latency_seconds": latency,
    }


def run_payloads_parallel(
    *,
    payloads: list[dict[str, Any]],
    prompt: str,
    output_path: Path,
    workers: int,
    reasoning_effort: str = REASONING_EFFORT,
    max_completion_tokens: int = 12000,
) -> list[dict[str, Any]]:
    if workers < 1:
        raise ValueError("workers must be at least 1")
    order = [row["payload_id"] for row in payloads]
    completed: dict[str, dict[str, Any]] = {}

    def call(payload: dict[str, Any]) -> dict[str, Any]:
        result = call_json_judge(
            prompt=prompt,
            payload=payload["model_payload"],
            reasoning_effort=reasoning_effort,
            max_completion_tokens=max_completion_tokens,
        )
        return {**payload, **result}

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(call, payload): payload for payload in payloads
        }
        for index, future in enumerate(as_completed(futures), start=1):
            row = future.result()
            completed[row["payload_id"]] = row
            write_jsonl(
                output_path,
                [completed[key] for key in order if key in completed],
            )
            print(
                f"[{index}/{len(payloads)}] {row['question_id']}",
                flush=True,
            )
    return [completed[key] for key in order]

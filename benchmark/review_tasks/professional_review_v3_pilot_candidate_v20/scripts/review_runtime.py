#!/usr/bin/env python3
"""Shared deterministic runtime helpers for the professional-review experiment."""

from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator
from openai import OpenAI
from dotenv import load_dotenv


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = PACKAGE_ROOT.parents[2]
MODEL_ALIAS = "gpt-5.1"
MODEL_SNAPSHOT = "gpt-5.1-2025-11-13"
DEFAULT_REASONING_EFFORT = "low"
PRICING_PATH = PACKAGE_ROOT / "config" / "pricing_2026-07-31.json"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def canonical_json(value: Any) -> str:
    return json.dumps(
        value,
        ensure_ascii=True,
        sort_keys=True,
        separators=(",", ":"),
    )


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_text(value: str) -> str:
    return sha256_bytes(value.encode("utf-8"))


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected one JSON object")
    return value


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for line_number, line in enumerate(
        path.read_text(encoding="utf-8").splitlines(),
        start=1,
    ):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_number}: invalid JSON") from exc
        if not isinstance(value, dict):
            raise ValueError(f"{path}:{line_number}: expected JSON object")
        records.append(value)
    return records


def write_json(path: Path, value: Any) -> None:
    atomic_write_text(path, json.dumps(value, indent=2, sort_keys=True) + "\n")


def write_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    atomic_write_text(
        path,
        "".join(canonical_json(record) + "\n" for record in records),
    )


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        dir=path.parent,
        prefix=f".{path.name}.",
        suffix=".tmp",
        delete=False,
    ) as handle:
        handle.write(text)
        temporary = Path(handle.name)
    temporary.replace(path)


PLACEHOLDER = re.compile(r"\{\{([A-Z0-9_]+)\}\}")


def render_template(path: Path, values: dict[str, Any]) -> str:
    text = path.read_text(encoding="utf-8")
    expected = set(PLACEHOLDER.findall(text))
    missing = expected - set(values)
    extra = set(values) - expected
    if missing:
        raise KeyError(f"{path}: missing template values {sorted(missing)}")
    if extra:
        raise KeyError(f"{path}: unused template values {sorted(extra)}")
    for name in sorted(expected):
        value = values[name]
        if not isinstance(value, str):
            value = json.dumps(value, ensure_ascii=True, indent=2)
        text = text.replace(f"{{{{{name}}}}}", value)
    unresolved = PLACEHOLDER.findall(text)
    if unresolved:
        raise RuntimeError(f"{path}: unresolved placeholders {unresolved}")
    return text


def validate_schema(instance: Any, schema: dict[str, Any], label: str) -> None:
    errors = sorted(
        Draft202012Validator(schema).iter_errors(instance),
        key=lambda error: list(error.absolute_path),
    )
    if errors:
        details = "; ".join(
            f"{'/'.join(str(item) for item in error.absolute_path) or '<root>'}: "
            f"{error.message}"
            for error in errors[:8]
        )
        raise ValueError(f"{label}: schema validation failed: {details}")


def schema_for_openai(schema: dict[str, Any]) -> dict[str, Any]:
    """Remove only the draft declaration unsupported by Structured Outputs."""

    def clean(value: Any) -> Any:
        if isinstance(value, dict):
            return {
                key: clean(item)
                for key, item in value.items()
                if key != "$schema"
            }
        if isinstance(value, list):
            return [clean(item) for item in value]
        return value

    return clean(schema)


def _pricing() -> dict[str, Any]:
    return load_json(PRICING_PATH)


def estimate_cost(
    *,
    model_snapshot: str,
    input_tokens: int,
    cached_input_tokens: int,
    output_tokens: int,
    web_search_calls: int = 0,
) -> float:
    pricing = _pricing()
    model = pricing["models"][model_snapshot]
    uncached = max(0, input_tokens - cached_input_tokens)
    model_cost = (
        uncached * float(model["input_per_million_tokens"])
        + cached_input_tokens
        * float(model["cached_input_per_million_tokens"])
        + output_tokens * float(model["output_per_million_tokens"])
    ) / 1_000_000
    search_cost = (
        web_search_calls
        * float(pricing["tools"]["web_search_per_1000_calls"])
        / 1000
    )
    return model_cost + search_cost


def _chat_usage(
    response: Any,
    latency_seconds: float,
    *,
    require_success: bool = True,
) -> dict[str, Any]:
    model = str(response.model)
    if require_success and model != MODEL_SNAPSHOT:
        raise RuntimeError(
            f"Unexpected model snapshot {model!r}; expected {MODEL_SNAPSHOT!r}"
        )
    finish_reason = str(response.choices[0].finish_reason or "")
    if require_success and finish_reason != "stop":
        raise RuntimeError(f"Model call did not finish normally: {finish_reason}")
    usage = response.usage
    details = getattr(usage, "prompt_tokens_details", None)
    input_tokens = int(usage.prompt_tokens or 0)
    cached_tokens = int(getattr(details, "cached_tokens", 0) or 0)
    output_tokens = int(usage.completion_tokens or 0)
    return {
        "response_id": str(response.id),
        "response_model": model,
        "system_fingerprint": str(response.system_fingerprint or ""),
        "finish_reason": finish_reason,
        "input_tokens": input_tokens,
        "cached_input_tokens": cached_tokens,
        "output_tokens": output_tokens,
        "total_tokens": input_tokens + output_tokens,
        "reasoning_tokens": int(
            getattr(
                getattr(usage, "completion_tokens_details", None),
                "reasoning_tokens",
                0,
            )
            or 0
        ),
        "web_search_calls": 0,
        "latency_seconds": latency_seconds,
        "estimated_cost_usd": estimate_cost(
            model_snapshot=(
                model if model == MODEL_SNAPSHOT else MODEL_SNAPSHOT
            ),
            input_tokens=input_tokens,
            cached_input_tokens=cached_tokens,
            output_tokens=output_tokens,
        ),
    }


def _response_usage(
    response: Any,
    latency_seconds: float,
    *,
    require_success: bool = True,
) -> dict[str, Any]:
    model = str(response.model)
    if require_success and model != MODEL_SNAPSHOT:
        raise RuntimeError(
            f"Unexpected model snapshot {model!r}; expected {MODEL_SNAPSHOT!r}"
        )
    status = str(getattr(response, "status", "") or "")
    if require_success and status != "completed":
        raise RuntimeError(f"Web Search call did not complete: {status}")
    usage = response.usage
    input_tokens = int(getattr(usage, "input_tokens", 0) or 0)
    input_details = getattr(usage, "input_tokens_details", None)
    cached_tokens = int(getattr(input_details, "cached_tokens", 0) or 0)
    output_tokens = int(getattr(usage, "output_tokens", 0) or 0)
    output_details = getattr(usage, "output_tokens_details", None)
    dump = response.model_dump()
    output_items = dump.get("output") or []
    search_items = [
        item for item in output_items if item.get("type") == "web_search_call"
    ]
    return {
        "response_id": str(response.id),
        "response_model": model,
        "finish_reason": status,
        "input_tokens": input_tokens,
        "cached_input_tokens": cached_tokens,
        "output_tokens": output_tokens,
        "total_tokens": input_tokens + output_tokens,
        "reasoning_tokens": int(
            getattr(output_details, "reasoning_tokens", 0) or 0
        ),
        "web_search_calls": len(search_items),
        "latency_seconds": latency_seconds,
        "estimated_cost_usd": estimate_cost(
            model_snapshot=(
                model if model == MODEL_SNAPSHOT else MODEL_SNAPSHOT
            ),
            input_tokens=input_tokens,
            cached_input_tokens=cached_tokens,
            output_tokens=output_tokens,
            web_search_calls=len(search_items),
        ),
    }


def _web_sources(response: Any) -> list[dict[str, str]]:
    sources: list[dict[str, str]] = []
    seen: set[str] = set()
    for item in response.model_dump().get("output") or []:
        if item.get("type") != "web_search_call":
            continue
        action = item.get("action") or {}
        for source in action.get("sources") or []:
            url = str(source.get("url") or "").strip()
            if not url or url in seen:
                continue
            sources.append(
                {
                    "url": url,
                    "title": str(source.get("title") or "").strip(),
                    "type": str(source.get("type") or "").strip(),
                }
            )
            seen.add(url)
    return sources


class ResumableOpenAI:
    """Persist each successful API call and resume only on exact request hash."""

    def __init__(self, *, allow_paid: bool) -> None:
        self.allow_paid = allow_paid
        self._client: OpenAI | None = None

    @property
    def client(self) -> OpenAI:
        if not self.allow_paid:
            raise RuntimeError(
                "Paid call blocked. Pass --allow-paid after validating the run."
            )
        load_dotenv(PROJECT_ROOT / ".env", override=False)
        if not os.getenv("OPENAI_API_KEY"):
            raise RuntimeError("OPENAI_API_KEY is not set")
        if self._client is None:
            self._client = OpenAI(timeout=600.0, max_retries=0)
        return self._client

    def _resume(
        self,
        *,
        output_path: Path,
        request_hash: str,
        expected_kind: str,
    ) -> dict[str, Any] | None:
        if not output_path.exists():
            return None
        record = load_json(output_path)
        if record.get("request_hash") != request_hash:
            raise RuntimeError(
                f"{output_path}: request hash mismatch; refusing unsafe resume"
            )
        if record.get("result_kind") != expected_kind:
            raise RuntimeError(f"{output_path}: result kind mismatch")
        return record

    def call_json(
        self,
        *,
        stage: str,
        call_key: str,
        system_prompt: str,
        user_prompt: str,
        schema_name: str,
        schema: dict[str, Any],
        output_path: Path,
        reasoning_effort: str = DEFAULT_REASONING_EFFORT,
        max_output_tokens: int = 8000,
    ) -> dict[str, Any]:
        response_format = {
            "type": "json_schema",
            "json_schema": {
                "name": schema_name,
                "strict": True,
                "schema": schema_for_openai(schema),
            },
        }
        request = {
            "model": MODEL_ALIAS,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "response_format": response_format,
            "reasoning_effort": reasoning_effort,
            "max_completion_tokens": max_output_tokens,
        }
        request_hash = sha256_text(canonical_json(request))
        resumed = self._resume(
            output_path=output_path,
            request_hash=request_hash,
            expected_kind="json",
        )
        if resumed is not None:
            validate_schema(resumed["result"], schema, str(output_path))
            return resumed

        started = time.perf_counter()
        response = self.client.chat.completions.create(**request)
        latency = time.perf_counter() - started
        raw = response.choices[0].message.content or ""
        failure_metadata = _chat_usage(
            response,
            latency,
            require_success=False,
        )
        try:
            metadata = _chat_usage(response, latency)
            result = json.loads(raw)
            validate_schema(result, schema, call_key)
        except Exception as exc:
            write_json(
                output_path.with_name(
                    f"{output_path.stem}.failed.{response.id}.json"
                ),
                {
                    "stage": stage,
                    "call_key": call_key,
                    "created_at": utc_now(),
                    "request_hash": request_hash,
                    "request": request,
                    "result_kind": "failed_json",
                    "result": raw,
                    "failure": f"{type(exc).__name__}: {exc}",
                    "response_metadata": failure_metadata,
                },
            )
            raise
        record = {
            "stage": stage,
            "call_key": call_key,
            "created_at": utc_now(),
            "request_hash": request_hash,
            "request": request,
            "result_kind": "json",
            "result": result,
            "raw_response_text": raw,
            "response_metadata": metadata,
        }
        write_json(output_path, record)
        return record

    def call_text(
        self,
        *,
        stage: str,
        call_key: str,
        system_prompt: str,
        user_prompt: str,
        output_path: Path,
        reasoning_effort: str = DEFAULT_REASONING_EFFORT,
        max_output_tokens: int = 6000,
    ) -> dict[str, Any]:
        request = {
            "model": MODEL_ALIAS,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "reasoning_effort": reasoning_effort,
            "max_completion_tokens": max_output_tokens,
        }
        request_hash = sha256_text(canonical_json(request))
        resumed = self._resume(
            output_path=output_path,
            request_hash=request_hash,
            expected_kind="text",
        )
        if resumed is not None:
            return resumed

        started = time.perf_counter()
        response = self.client.chat.completions.create(**request)
        latency = time.perf_counter() - started
        result = response.choices[0].message.content or ""
        try:
            metadata = _chat_usage(response, latency)
        except RuntimeError as exc:
            failure = {
                "stage": stage,
                "call_key": call_key,
                "created_at": utc_now(),
                "request_hash": request_hash,
                "request": request,
                "result_kind": "failed_text",
                "result": result,
                "failure": str(exc),
                "response_id": str(response.id),
                "response_model": str(response.model),
                "finish_reason": str(
                    response.choices[0].finish_reason or ""
                ),
                "usage": response.usage.model_dump(),
                "latency_seconds": latency,
            }
            write_json(
                output_path.with_name(
                    f"{output_path.stem}.failed.{response.id}.json"
                ),
                failure,
            )
            raise
        if not result.strip():
            failure = {
                "stage": stage,
                "call_key": call_key,
                "created_at": utc_now(),
                "request_hash": request_hash,
                "request": request,
                "result_kind": "failed_text",
                "result": result,
                "failure": "empty text response",
                "response_metadata": metadata,
            }
            write_json(
                output_path.with_name(
                    f"{output_path.stem}.failed.{response.id}.json"
                ),
                failure,
            )
            raise RuntimeError(f"{call_key}: empty text response")
        record = {
            "stage": stage,
            "call_key": call_key,
            "created_at": utc_now(),
            "request_hash": request_hash,
            "request": request,
            "result_kind": "text",
            "result": result,
            "response_metadata": metadata,
        }
        write_json(output_path, record)
        return record

    def call_web_json(
        self,
        *,
        stage: str,
        call_key: str,
        system_prompt: str,
        user_prompt: str,
        schema_name: str,
        schema: dict[str, Any],
        output_path: Path,
        reasoning_effort: str = DEFAULT_REASONING_EFFORT,
        max_output_tokens: int = 10000,
    ) -> dict[str, Any]:
        request = {
            "model": MODEL_ALIAS,
            "input": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "tools": [{"type": "web_search"}],
            "tool_choice": "required",
            "include": ["web_search_call.action.sources"],
            "reasoning": {"effort": reasoning_effort},
            "max_output_tokens": max_output_tokens,
            "text": {
                "format": {
                    "type": "json_schema",
                    "name": schema_name,
                    "strict": True,
                    "schema": schema_for_openai(schema),
                }
            },
            "store": False,
        }
        request_hash = sha256_text(canonical_json(request))
        resumed = self._resume(
            output_path=output_path,
            request_hash=request_hash,
            expected_kind="web_json",
        )
        if resumed is not None:
            validate_schema(resumed["result"], schema, str(output_path))
            return resumed

        started = time.perf_counter()
        response = self.client.responses.create(**request)
        latency = time.perf_counter() - started
        raw = response.output_text or ""
        failure_metadata = _response_usage(
            response,
            latency,
            require_success=False,
        )
        try:
            metadata = _response_usage(response, latency)
            result = json.loads(raw)
            validate_schema(result, schema, call_key)
        except Exception as exc:
            write_json(
                output_path.with_name(
                    f"{output_path.stem}.failed.{response.id}.json"
                ),
                {
                    "stage": stage,
                    "call_key": call_key,
                    "created_at": utc_now(),
                    "request_hash": request_hash,
                    "request": request,
                    "result_kind": "failed_web_json",
                    "result": raw,
                    "failure": f"{type(exc).__name__}: {exc}",
                    "consulted_sources": _web_sources(response),
                    "response_metadata": failure_metadata,
                },
            )
            raise
        record = {
            "stage": stage,
            "call_key": call_key,
            "created_at": utc_now(),
            "request_hash": request_hash,
            "request": request,
            "result_kind": "web_json",
            "result": result,
            "raw_response_text": raw,
            "consulted_sources": _web_sources(response),
            "response_metadata": metadata,
        }
        write_json(output_path, record)
        return record


def collect_call_records(run_dir: Path) -> list[dict[str, Any]]:
    records = []
    for path in sorted((run_dir / "calls").rglob("*.json")):
        record = load_json(path)
        metadata = record.get("response_metadata")
        if isinstance(metadata, dict):
            records.append(
                {
                    "path": str(path.relative_to(run_dir)),
                    "stage": record.get("stage", ""),
                    "call_key": record.get("call_key", ""),
                    **metadata,
                }
            )
    return records

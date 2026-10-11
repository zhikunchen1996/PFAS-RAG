"""Self-contained runtime helpers promoted from the Frozen V2 workflow.

Only functions used by Frozen V3 generation and judging are retained. This
module intentionally has no dependency on Frozen V2 or benchmark/src.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import threading
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Callable

from openai import OpenAI


PROJECT_ROOT = Path(__file__).resolve().parents[3]
SYSTEM_MESSAGE = "Follow the benchmark instructions exactly."
_thread_state = threading.local()
PLACEHOLDER_PATTERN = re.compile(r"\{([A-Za-z_][A-Za-z0-9_]*)\}")


def norm(value: Any) -> str:
    return "" if value is None else str(value)


def read_csv(path: str | Path) -> list[dict[str, str]]:
    with Path(path).open(encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def read_jsonl(path: str | Path) -> list[dict[str, Any]]:
    path = Path(path)
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
                raise ValueError(
                    f"Invalid JSONL at {path}:{line_number}: {exc}"
                ) from exc
    return rows


def project_relative(path: Path) -> str:
    return str(path.resolve().relative_to(PROJECT_ROOT))


def prepare_output_dir(
    value: str | Path,
    *,
    resume: bool,
) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = PROJECT_ROOT / path
    path = path.resolve()
    if path.exists() and any(path.iterdir()) and not resume:
        raise RuntimeError(
            f"Refusing to overwrite non-empty result directory: {path}"
        )
    path.mkdir(parents=True, exist_ok=True)
    return path


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload_sha256(value: Any) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fields: list[str] = []
    seen: set[str] = set()
    for row in rows:
        for key in row:
            if key not in seen:
                seen.add(key)
                fields.append(key)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fields,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def client() -> OpenAI:
    value = getattr(_thread_state, "client", None)
    if value is None:
        value = OpenAI(timeout=300, max_retries=2)
        _thread_state.client = value
    return value


def api_metadata(response: Any, prefix: str) -> dict[str, Any]:
    usage = response.usage
    return {
        f"{prefix}_response_id": norm(response.id),
        f"{prefix}_response_model": norm(response.model),
        f"{prefix}_system_fingerprint": norm(response.system_fingerprint),
        f"{prefix}_prompt_tokens": int(usage.prompt_tokens or 0),
        f"{prefix}_completion_tokens": int(usage.completion_tokens or 0),
        f"{prefix}_total_tokens": int(usage.total_tokens or 0),
    }


def run_parallel(
    *,
    items: list[dict[str, Any]],
    key: Callable[[dict[str, Any]], str],
    worker: Callable[[dict[str, Any]], dict[str, Any]],
    output_path: Path,
    workers: int,
    label: str,
    resume: bool = False,
    reuse_validator: Callable[
        [dict[str, Any], dict[str, Any]],
        bool,
    ]
    | None = None,
) -> list[dict[str, Any]]:
    if workers < 1:
        raise ValueError("workers must be at least 1")
    order = [key(item) for item in items]
    if len(order) != len(set(order)):
        raise ValueError(f"Duplicate item keys in {label}")

    existing: dict[str, dict[str, Any]] = {}
    if resume and output_path.exists():
        stored_rows = read_jsonl(output_path)
        stored_keys = [key(row) for row in stored_rows]
        if len(stored_keys) != len(set(stored_keys)):
            raise RuntimeError(f"Duplicate stored keys in {label}")
        stored = dict(zip(stored_keys, stored_rows))
        for item in items:
            item_key = key(item)
            row = stored.get(item_key)
            if row is None:
                continue
            if reuse_validator is not None and not reuse_validator(item, row):
                continue
            existing[item_key] = row
    todo = [item for item in items if key(item) not in existing]
    print(
        f"[{label}] existing={len(existing)} "
        f"todo={len(todo)} workers={workers}",
        flush=True,
    )
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(worker, item): item for item in todo}
        for completed, future in enumerate(
            as_completed(futures),
            start=1,
        ):
            row = future.result()
            existing[key(row)] = row
            write_jsonl(
                output_path,
                [
                    existing[item_key]
                    for item_key in order
                    if item_key in existing
                ],
            )
            print(
                f"[{label} {completed}/{len(todo)}] {key(row)}",
                flush=True,
            )
    if set(existing) != set(order):
        raise RuntimeError(f"Incomplete {label} output")
    return [existing[item_key] for item_key in order]


def render(template: str, **values: str) -> str:
    placeholders = set(PLACEHOLDER_PATTERN.findall(template))
    missing = placeholders - set(values)
    if missing:
        raise KeyError(
            "Missing template values: " + ", ".join(sorted(missing))
        )
    unused = set(values) - placeholders
    if unused:
        raise KeyError(
            "Unused template values: " + ", ".join(sorted(unused))
        )
    return PLACEHOLDER_PATTERN.sub(
        lambda match: str(values[match.group(1)]),
        template,
    )


def call_json_judge(
    payloads: list[dict[str, Any]],
    prompt: str,
    model: str,
    output_path: Path,
    workers: int,
    label: str,
    resume: bool = False,
) -> list[dict[str, Any]]:
    def model_payload(item: dict[str, Any]) -> dict[str, Any]:
        payload = item.get("model_payload")
        if payload is None:
            return item
        if not isinstance(payload, dict):
            raise RuntimeError("model_payload must be a JSON object")
        return payload

    def row_key(row: dict[str, Any]) -> str:
        return norm(row.get("payload_id"))

    def worker(item: dict[str, Any]) -> dict[str, Any]:
        payload = model_payload(item)
        execution_fingerprint = payload_sha256(
            {
                "model": model,
                "temperature": 0,
                "prompt": prompt,
                "payload": payload,
            }
        )
        response = client().chat.completions.create(
            model=model,
            response_format={"type": "json_object"},
            temperature=0,
            messages=[
                {"role": "system", "content": prompt},
                {
                    "role": "user",
                    "content": json.dumps(payload, ensure_ascii=False),
                },
            ],
        )
        raw = response.choices[0].message.content or "{}"
        try:
            result = json.loads(raw)
        except json.JSONDecodeError as exc:
            result = {"parse_error": str(exc), "raw_output": raw}
        result["payload_id"] = item["payload_id"]
        result["question_id"] = item["question_id"]
        result["system_mode"] = item.get(
            "system_mode",
            "rag_end_to_end",
        )
        return {
            "payload_id": item["payload_id"],
            "question_id": item["question_id"],
            "system_mode": item.get(
                "system_mode",
                "rag_end_to_end",
            ),
            "judge_execution_sha256": execution_fingerprint,
            "judge_result": result,
            **api_metadata(response, "judge"),
        }

    def reusable(
        item: dict[str, Any],
        row: dict[str, Any],
    ) -> bool:
        payload = model_payload(item)
        expected = payload_sha256(
            {
                "model": model,
                "temperature": 0,
                "prompt": prompt,
                "payload": payload,
            }
        )
        return row.get("judge_execution_sha256") == expected

    return run_parallel(
        items=payloads,
        key=row_key,
        worker=worker,
        output_path=output_path,
        workers=workers,
        label=label,
        resume=resume,
        reuse_validator=reusable,
    )


def group_gold(
    rows: list[dict[str, Any]],
) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[norm(row.get("question_id"))].append(row)
    return grouped


def compact_gold(row: dict[str, Any]) -> dict[str, Any]:
    fields = (
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
        "review_status",
    )
    return {field: row.get(field, "") for field in fields}


def token_row(
    stage: str,
    config_name: str,
    rows: list[dict[str, Any]],
    prefix: str,
    note: str = "",
) -> dict[str, Any]:
    prompt_key = f"{prefix}_prompt_tokens"
    completion_key = f"{prefix}_completion_tokens"
    total_key = f"{prefix}_total_tokens"
    count = len(rows)
    total = sum(int(row.get(total_key, 0) or 0) for row in rows)
    return {
        "stage": stage,
        "config_name": config_name,
        "model": next(
            (
                row.get(f"{prefix}_response_model", "")
                for row in rows
                if row.get(f"{prefix}_response_model")
            ),
            "",
        ),
        "call_count": count,
        "prompt_tokens_total": sum(
            int(row.get(prompt_key, 0) or 0) for row in rows
        ),
        "completion_tokens_total": sum(
            int(row.get(completion_key, 0) or 0) for row in rows
        ),
        "total_tokens": total,
        "tokens_per_call": total / count if count else 0.0,
        "note": note,
    }

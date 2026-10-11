from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Any

import requests

import common


FROZEN_SCRIPTS = common.ROOT / "benchmark/frozen_v3/scripts"
if str(FROZEN_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(FROZEN_SCRIPTS))

import run_dev13_soft_tags_v3 as tag_runtime  # noqa: E402
import runtime_helpers as frozen_runtime  # noqa: E402


MAX_COMPLETION_TOKENS = 5000
SYSTEMS = (
    "gpt51_direct",
    "gpt51_rag",
    "gemini31_pro_direct",
    "gemini31_pro_rag",
    "claude_sonnet5_direct",
    "claude_sonnet5_rag",
)
CONFIGS = {
    "gpt51": {
        "provider": "openai",
        "model": "gpt-5.1",
        "reasoning": "low",
        "temperature": "provider_default_not_sent",
        "input_price": 1.25,
        "cached_input_price": 0.125,
        "output_price": 10.0,
    },
    "gemini31_pro": {
        "provider": "gemini",
        "model": "gemini-3.1-pro-preview",
        "reasoning": "thinking_level_low",
        "temperature": "provider_default_not_sent",
        "input_price": 2.0,
        "cached_input_price": 2.0,
        "output_price": 12.0,
    },
    "claude_sonnet5": {
        "provider": "claude",
        "model": "claude-sonnet-5",
        "reasoning": "adaptive_thinking_effort_low",
        "temperature": "provider_default_not_sent",
        "input_price": 2.0,
        "cached_input_price": 2.0,
        "output_price": 10.0,
    },
}


def split_system(system: str) -> tuple[str, str]:
    arm = "direct" if system.endswith("_direct") else "rag"
    base_model = system[: -(len(arm) + 1)]
    if base_model not in CONFIGS:
        raise ValueError(f"Unknown system: {system}")
    return base_model, arm


def load_items() -> list[dict[str, Any]]:
    ids = common.question_ids()
    questions = {
        row["question_id"]: row for row in common.read_csv(common.QUESTIONS)
    }
    retrieval_rows = common.ordered_rows(
        common.read_jsonl(common.RETRIEVAL),
        ids,
        source="BGE-LLM retrieval",
    )
    common.validate_contexts(retrieval_rows)
    tag_rows = common.ordered_rows(
        common.read_jsonl(common.TAGS),
        ids,
        source="BGE-LLM common tags",
    )
    retrieval = {row["question_id"]: row for row in retrieval_rows}
    tags = {row["question_id"]: row for row in tag_rows}
    items = []
    for qid in ids:
        tag_ids = {
            int(row["candidate_id"])
            for row in tags[qid].get("validated_chunk_tags", [])
        }
        if tag_ids != set(range(1, 11)):
            raise RuntimeError(f"{qid}: common tags do not cover C1-C10")
        items.append(
            {
                "question_id": qid,
                "question": questions[qid],
                "retrieval": retrieval[qid],
                "tags": tags[qid],
            }
        )
    return items


def rendered_user(item: dict[str, Any], arm: str) -> str:
    question = item["question"]["question_text"]
    if arm == "direct":
        return frozen_runtime.render(
            common.DIRECT_PROMPT.read_text(encoding="utf-8"),
            question_text=question,
        )
    tagged_context = tag_runtime.format_tagged_context(
        item["retrieval"]["retrieved_context"],
        item["tags"],
    )
    return frozen_runtime.render(
        common.RAG_PROMPT.read_text(encoding="utf-8"),
        question_text=question,
        retrieved_context=tagged_context,
    )


def provider_request(item: dict[str, Any], system: str) -> dict[str, Any]:
    base_model, arm = split_system(system)
    config = CONFIGS[base_model]
    system_prompt = common.SHARED_PROMPT.read_text(encoding="utf-8")
    user_prompt = rendered_user(item, arm)
    if config["provider"] == "openai":
        payload = {
            "model": config["model"],
            "reasoning_effort": "low",
            "max_completion_tokens": MAX_COMPLETION_TOKENS,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        }
    elif config["provider"] == "gemini":
        payload = {
            "systemInstruction": {"parts": [{"text": system_prompt}]},
            "contents": [{"role": "user", "parts": [{"text": user_prompt}]}],
            "generationConfig": {
                "maxOutputTokens": MAX_COMPLETION_TOKENS,
                "thinkingConfig": {"thinkingLevel": "low"},
            },
        }
    else:
        payload = {
            "model": config["model"],
            "max_tokens": MAX_COMPLETION_TOKENS,
            "system": system_prompt,
            "messages": [{"role": "user", "content": user_prompt}],
            "thinking": {"type": "adaptive"},
            "output_config": {"effort": "low"},
        }
    return {
        "system": system,
        "provider": config["provider"],
        "request_model": config["model"],
        "payload": payload,
    }


def execution_hash(item: dict[str, Any], system: str) -> str:
    return common.payload_sha256(provider_request(item, system))


def post_json(
    url: str,
    headers: dict[str, str],
    payload: dict[str, Any],
) -> tuple[dict[str, Any], float]:
    started = time.perf_counter()
    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=600,
    )
    latency = time.perf_counter() - started
    if response.status_code >= 400:
        raise RuntimeError(
            f"Provider HTTP {response.status_code}: {response.text[:1000]}"
        )
    value = response.json()
    if not isinstance(value, dict):
        raise RuntimeError("Provider response is not a JSON object")
    return value, latency


def call_openai(
    request: dict[str, Any],
) -> tuple[str, dict[str, Any]]:
    started = time.perf_counter()
    response = common.openai_client().chat.completions.create(
        **request["payload"]
    )
    latency = time.perf_counter() - started
    answer = response.choices[0].message.content or ""
    if not answer.strip():
        raise RuntimeError("OpenAI returned an empty answer")
    return answer, common.openai_metadata(response, latency)


def call_gemini(
    request: dict[str, Any],
    config: dict[str, Any],
) -> tuple[str, dict[str, Any]]:
    key = os.getenv("GOOGLE_API_KEY")
    if not key:
        raise RuntimeError("GOOGLE_API_KEY is missing")
    model = config["model"]
    response, latency = post_json(
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model}:generateContent",
        {"x-goog-api-key": key, "Content-Type": "application/json"},
        request["payload"],
    )
    candidates = response.get("candidates") or []
    if not candidates:
        raise RuntimeError("Gemini returned no candidate")
    finish = str(candidates[0].get("finishReason") or "")
    if finish != "STOP":
        raise RuntimeError(f"Gemini finish reason is {finish}")
    parts = ((candidates[0].get("content") or {}).get("parts") or [])
    answer = "".join(
        str(part.get("text") or "")
        for part in parts
        if not part.get("thought")
    ).strip()
    if not answer:
        raise RuntimeError("Gemini returned no answer text")
    response_model = str(response.get("modelVersion") or "")
    if response_model and response_model != model:
        raise RuntimeError(
            f"Unexpected Gemini model {response_model}; expected {model}"
        )
    usage = response.get("usageMetadata") or {}
    prompt = int(usage.get("promptTokenCount") or 0)
    cached = int(usage.get("cachedContentTokenCount") or 0)
    answer_tokens = int(usage.get("candidatesTokenCount") or 0)
    thinking = int(usage.get("thoughtsTokenCount") or 0)
    output = answer_tokens + thinking
    cost = (
        max(0, prompt - cached) * config["input_price"]
        + cached * config["cached_input_price"]
        + output * config["output_price"]
    ) / 1_000_000
    return answer, {
        "response_id": str(response.get("responseId") or ""),
        "response_model": response_model or model,
        "finish_reason": finish,
        "prompt_tokens": prompt,
        "cached_prompt_tokens": cached,
        "answer_tokens": answer_tokens,
        "thinking_tokens": thinking,
        "completion_tokens": output,
        "total_tokens": int(
            usage.get("totalTokenCount") or prompt + output
        ),
        "estimated_cost_usd": cost,
        "latency_seconds": latency,
    }


def call_claude(
    request: dict[str, Any],
    config: dict[str, Any],
) -> tuple[str, dict[str, Any]]:
    key = os.getenv("ANTHROPIC_API_KEY")
    if not key:
        raise RuntimeError("ANTHROPIC_API_KEY is missing")
    response, latency = post_json(
        "https://api.anthropic.com/v1/messages",
        {
            "x-api-key": key,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json",
        },
        request["payload"],
    )
    finish = str(response.get("stop_reason") or "")
    if finish not in {"end_turn", "stop_sequence", "refusal"}:
        raise RuntimeError(f"Claude stop reason is {finish}")
    response_model = str(response.get("model") or "")
    if response_model != config["model"]:
        raise RuntimeError(
            f"Unexpected Claude model {response_model}; "
            f"expected {config['model']}"
        )
    answer = "".join(
        str(block.get("text") or "")
        for block in response.get("content") or []
        if block.get("type") == "text"
    ).strip()
    if not answer and finish == "refusal":
        answer = "[Provider refusal: no answer content returned.]"
    elif not answer:
        raise RuntimeError("Claude returned no answer text")
    usage = response.get("usage") or {}
    prompt = int(usage.get("input_tokens") or 0)
    cached = int(usage.get("cache_read_input_tokens") or 0)
    output = int(usage.get("output_tokens") or 0)
    details = usage.get("output_tokens_details") or {}
    thinking = int(details.get("thinking_tokens") or 0)
    cost = (
        max(0, prompt - cached) * config["input_price"]
        + cached * config["cached_input_price"]
        + output * config["output_price"]
    ) / 1_000_000
    return answer, {
        "response_id": str(response.get("id") or ""),
        "response_model": response_model,
        "finish_reason": finish,
        "provider_refusal": finish == "refusal",
        "prompt_tokens": prompt,
        "cached_prompt_tokens": cached,
        "answer_tokens": max(0, output - thinking),
        "thinking_tokens": thinking,
        "completion_tokens": output,
        "total_tokens": prompt + output,
        "estimated_cost_usd": cost,
        "latency_seconds": latency,
    }


def call_provider(
    item: dict[str, Any],
    system: str,
) -> tuple[str, dict[str, Any], str]:
    base_model, _ = split_system(system)
    config = CONFIGS[base_model]
    request = provider_request(item, system)
    if config["provider"] == "openai":
        answer, metadata = call_openai(request)
    elif config["provider"] == "gemini":
        answer, metadata = call_gemini(request, config)
    else:
        answer, metadata = call_claude(request, config)
    return answer, metadata, common.payload_sha256(request)


def output_path(system: str) -> Path:
    return common.GENERATION_RESULTS / system / "answers.jsonl"


def run_system(
    items: list[dict[str, Any]],
    system: str,
    *,
    workers: int,
    resume: bool,
) -> list[dict[str, Any]]:
    base_model, arm = split_system(system)
    config = CONFIGS[base_model]

    def worker(item: dict[str, Any]) -> dict[str, Any]:
        answer, metadata, request_hash = call_provider(item, system)
        row: dict[str, Any] = {
            "item_id": f"{system}::{item['question_id']}",
            "question_id": item["question_id"],
            "question_text": item["question"]["question_text"],
            "system": system,
            "base_model": base_model,
            "arm": arm,
            "provider": config["provider"],
            "request_model": config["model"],
            "reasoning_setting": config["reasoning"],
            "temperature": config["temperature"],
            "max_completion_tokens": MAX_COMPLETION_TOKENS,
            "answer": answer,
            "execution_sha256": request_hash,
            "shared_system_prompt_sha256": common.sha256(
                common.SHARED_PROMPT
            ),
            "arm_prompt_sha256": common.sha256(
                common.DIRECT_PROMPT if arm == "direct" else common.RAG_PROMPT
            ),
            **metadata,
        }
        if arm == "rag":
            row.update(
                {
                    "retrieval_config_name": item["retrieval"].get(
                        "retrieval_config_name", ""
                    ),
                    "retrieved_context": item["retrieval"]["retrieved_context"],
                    "soft_eligibility_tags": item["tags"][
                        "validated_chunk_tags"
                    ],
                    "tag_execution_sha256": item["tags"].get(
                        "execution_sha256", ""
                    ),
                }
            )
        return row

    output = output_path(system)
    if output.exists() and not resume:
        raise RuntimeError(
            f"{system}: paid output exists; use --resume to avoid duplicates"
        )
    rows = common.run_resumable(
        items=items,
        key=lambda row: str(row.get("question_id", "")),
        expected_execution_hash=lambda item: execution_hash(item, system),
        worker=worker,
        output=output,
        workers=workers,
        resume=resume,
        label=f"Test40 {system}",
    )
    common.write_json(
        output.parent / "run_manifest.json",
        {
            "protocol_id": "test40_multibase_direct_rag_v1",
            "status": "complete",
            "system": system,
            "base_model": base_model,
            "arm": arm,
            "question_count": len(rows),
            "request_model": config["model"],
            "response_models": sorted(
                {str(row["response_model"]) for row in rows}
            ),
            "reasoning_setting": config["reasoning"],
            "temperature": config["temperature"],
            "max_completion_tokens": MAX_COMPLETION_TOKENS,
            "questions_sha256": common.sha256(common.QUESTIONS),
            "retrieval_sha256": common.sha256(common.RETRIEVAL),
            "tags_sha256": common.sha256(common.TAGS),
            "shared_system_prompt_sha256": common.sha256(
                common.SHARED_PROMPT
            ),
            "arm_prompt_sha256": common.sha256(
                common.DIRECT_PROMPT if arm == "direct" else common.RAG_PROMPT
            ),
            "api_calls": len(rows),
            "total_tokens": sum(int(row["total_tokens"]) for row in rows),
            "estimated_cost_usd": sum(
                float(row["estimated_cost_usd"]) for row in rows
            ),
            "latency_seconds_sum": sum(
                float(row["latency_seconds"]) for row in rows
            ),
            "resume_hash_validated": True,
            "retrieval_or_tagger_calls": 0,
        },
    )
    return rows


def write_generation_summary() -> None:
    summaries = []
    for system in SYSTEMS:
        path = output_path(system)
        if not path.exists():
            continue
        rows = common.read_jsonl(path)
        summaries.append(
            {
                "system": system,
                "answer_count": len(rows),
                "prompt_tokens": sum(int(row["prompt_tokens"]) for row in rows),
                "completion_tokens": sum(
                    int(row["completion_tokens"]) for row in rows
                ),
                "total_tokens": sum(int(row["total_tokens"]) for row in rows),
                "estimated_cost_usd": sum(
                    float(row["estimated_cost_usd"]) for row in rows
                ),
                "latency_seconds_sum": sum(
                    float(row["latency_seconds"]) for row in rows
                ),
            }
        )
    if summaries:
        common.write_csv(
            common.GENERATION_RESULTS / "generation_usage_summary.csv",
            summaries,
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--system",
        choices=("all", *SYSTEMS),
        required=True,
    )
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    items = load_items()
    selected = SYSTEMS if args.system == "all" else (args.system,)
    if args.dry_run:
        payloads = [
            provider_request(item, system)
            for system in selected
            for item in items
        ]
        print(
            f"DRY RUN PASS: {len(payloads)} generation payloads built; "
            "no API calls."
        )
        return
    for system in selected:
        run_system(
            items,
            system,
            workers=args.workers,
            resume=args.resume,
        )
    write_generation_summary()


if __name__ == "__main__":
    main()

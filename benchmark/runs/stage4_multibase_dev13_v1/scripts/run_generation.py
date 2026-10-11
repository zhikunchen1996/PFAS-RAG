from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from pathlib import Path
from typing import Any

import requests
from dotenv import load_dotenv


PACKAGE = Path(__file__).resolve().parents[1]
ROOT = PACKAGE.parents[2]
V3 = ROOT / "benchmark/frozen_v3"
V3_SCRIPTS = V3 / "scripts"
if str(V3_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(V3_SCRIPTS))

import run_dev13_soft_tags_v3 as tags_runtime  # noqa: E402
import runtime_helpers as base  # noqa: E402


load_dotenv(ROOT / ".env", override=False)

PROTOCOL = PACKAGE / "protocol.json"
SHARED_PROMPT = PACKAGE / "prompts/shared_system_v1.txt"
DIRECT_PROMPT = PACKAGE / "prompts/direct_user_v1.txt"
RAG_PROMPT = PACKAGE / "prompts/rag_user_v1.txt"
QUESTIONS = V3 / "input/questions_dev13.csv"
RETRIEVAL = (
    V3
    / "results/dev13_retrieval_budget_gpt51_2026-07-26/"
    "bge_llm_gpt51/retrieval_outputs/"
    "rag_outputs_bge_llm_gpt51_pool60_bge30_llm10_fullchunk.jsonl"
)
TAGS = (
    V3
    / "judge/support/layer1_common_tagger_v1/results/"
    "dev13_common_tagger_gpt51_2026-07-26/bge_llm/tags/"
    "tag_results.jsonl"
)
MAX_COMPLETION_TOKENS = 5000
PROVIDERS = {
    "gemini31_pro": {
        "model": "gemini-3.1-pro-preview",
        "key_env": "GOOGLE_API_KEY",
        "input_price": 2.0,
        "output_price": 12.0,
        "reasoning": "thinking_level_low",
        "temperature": "provider_default_1_not_sent",
    },
    "claude_sonnet5": {
        "model": "claude-sonnet-5",
        "key_env": "ANTHROPIC_API_KEY",
        "input_price": 2.0,
        "output_price": 10.0,
        "reasoning": "adaptive_thinking_effort_low",
        "temperature": "provider_default_not_sent",
    },
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_inputs(limit: int | None) -> list[dict[str, Any]]:
    questions = base.read_csv(QUESTIONS)
    if limit is not None:
        questions = questions[:limit]
    retrieval = {
        row["question_id"]: row for row in base.read_jsonl(RETRIEVAL)
    }
    tags = {row["question_id"]: row for row in base.read_jsonl(TAGS)}
    items = []
    for question in questions:
        qid = question["question_id"]
        if qid not in retrieval or qid not in tags:
            raise RuntimeError(f"{qid}: missing frozen retrieval or tags")
        contexts = retrieval[qid].get("retrieved_context", [])
        if len(contexts) != 10:
            raise RuntimeError(f"{qid}: expected ten retrieved chunks")
        items.append(
            {
                "question": question,
                "retrieval": retrieval[qid],
                "tags": tags[qid],
            }
        )
    return items


def rendered_user(item: dict[str, Any], arm: str) -> str:
    question = item["question"]["question_text"]
    if arm == "direct":
        return base.render(
            DIRECT_PROMPT.read_text(encoding="utf-8"),
            question_text=question,
        )
    context = tags_runtime.format_tagged_context(
        item["retrieval"]["retrieved_context"],
        item["tags"],
    )
    return base.render(
        RAG_PROMPT.read_text(encoding="utf-8"),
        question_text=question,
        retrieved_context=context,
    )


def request_payload(
    item: dict[str, Any],
    arm: str,
    provider: str,
) -> dict[str, Any]:
    config = PROVIDERS[provider]
    system = SHARED_PROMPT.read_text(encoding="utf-8")
    user = rendered_user(item, arm)
    if provider == "gemini31_pro":
        return {
            "systemInstruction": {"parts": [{"text": system}]},
            "contents": [
                {"role": "user", "parts": [{"text": user}]}
            ],
            "generationConfig": {
                "maxOutputTokens": MAX_COMPLETION_TOKENS,
                "thinkingConfig": {"thinkingLevel": "low"},
            },
        }
    return {
        "model": config["model"],
        "max_tokens": MAX_COMPLETION_TOKENS,
        "system": system,
        "messages": [{"role": "user", "content": user}],
        "thinking": {"type": "adaptive"},
        "output_config": {"effort": "low"},
    }


def post_json(
    url: str,
    headers: dict[str, str],
    payload: dict[str, Any],
) -> dict[str, Any]:
    last_error: Exception | None = None
    for attempt in range(3):
        try:
            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=600,
            )
            if response.status_code >= 400:
                detail = response.text[:1000]
                raise RuntimeError(
                    f"Provider HTTP {response.status_code}: {detail}"
                )
            value = response.json()
            if not isinstance(value, dict):
                raise RuntimeError("Provider response is not a JSON object")
            return value
        except Exception as exc:
            last_error = exc
            if attempt == 2:
                break
            time.sleep(2**attempt)
    raise RuntimeError(f"Provider call failed: {last_error}")


def call_gemini(
    payload: dict[str, Any],
    config: dict[str, Any],
) -> tuple[str, dict[str, Any]]:
    key = os.getenv(config["key_env"])
    if not key:
        raise RuntimeError(f"Missing {config['key_env']}")
    model = config["model"]
    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model}:generateContent"
    )
    started = time.perf_counter()
    response = post_json(
        url,
        {"x-goog-api-key": key, "Content-Type": "application/json"},
        payload,
    )
    latency = time.perf_counter() - started
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
    usage = response.get("usageMetadata") or {}
    prompt_tokens = int(usage.get("promptTokenCount") or 0)
    answer_tokens = int(usage.get("candidatesTokenCount") or 0)
    thinking_tokens = int(usage.get("thoughtsTokenCount") or 0)
    output_tokens = answer_tokens + thinking_tokens
    return answer, {
        "response_id": str(response.get("responseId") or ""),
        "response_model": str(response.get("modelVersion") or model),
        "finish_reason": finish,
        "prompt_tokens": prompt_tokens,
        "cached_prompt_tokens": int(
            usage.get("cachedContentTokenCount") or 0
        ),
        "answer_tokens": answer_tokens,
        "thinking_tokens": thinking_tokens,
        "output_tokens_billed": output_tokens,
        "total_tokens": int(
            usage.get("totalTokenCount") or prompt_tokens + output_tokens
        ),
        "estimated_cost_usd": (
            prompt_tokens * config["input_price"]
            + output_tokens * config["output_price"]
        )
        / 1_000_000,
        "latency_seconds": latency,
    }


def call_claude(
    payload: dict[str, Any],
    config: dict[str, Any],
) -> tuple[str, dict[str, Any]]:
    key = os.getenv(config["key_env"])
    if not key:
        raise RuntimeError(f"Missing {config['key_env']}")
    started = time.perf_counter()
    response = post_json(
        "https://api.anthropic.com/v1/messages",
        {
            "x-api-key": key,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json",
        },
        payload,
    )
    latency = time.perf_counter() - started
    finish = str(response.get("stop_reason") or "")
    if finish not in {"end_turn", "stop_sequence"}:
        raise RuntimeError(f"Claude stop reason is {finish}")
    answer = "".join(
        str(block.get("text") or "")
        for block in response.get("content") or []
        if block.get("type") == "text"
    ).strip()
    if not answer:
        raise RuntimeError("Claude returned no answer text")
    usage = response.get("usage") or {}
    input_tokens = int(usage.get("input_tokens") or 0)
    output_tokens = int(usage.get("output_tokens") or 0)
    details = usage.get("output_tokens_details") or {}
    thinking_tokens = int(details.get("thinking_tokens") or 0)
    cache_read = int(usage.get("cache_read_input_tokens") or 0)
    return answer, {
        "response_id": str(response.get("id") or ""),
        "response_model": str(response.get("model") or config["model"]),
        "finish_reason": finish,
        "prompt_tokens": input_tokens,
        "cached_prompt_tokens": cache_read,
        "answer_tokens": max(0, output_tokens - thinking_tokens),
        "thinking_tokens": thinking_tokens,
        "output_tokens_billed": output_tokens,
        "total_tokens": input_tokens + output_tokens,
        "estimated_cost_usd": (
            input_tokens * config["input_price"]
            + output_tokens * config["output_price"]
        )
        / 1_000_000,
        "latency_seconds": latency,
    }


def run_arm(
    items: list[dict[str, Any]],
    arm: str,
    provider: str,
    output: Path,
    workers: int,
    resume: bool,
) -> tuple[list[dict[str, Any]], float]:
    config = PROVIDERS[provider]

    def key(row: dict[str, Any]) -> str:
        if "question_id" in row:
            return str(row["question_id"])
        return str(row["question"]["question_id"])

    def worker(item: dict[str, Any]) -> dict[str, Any]:
        payload = request_payload(item, arm, provider)
        if provider == "gemini31_pro":
            answer, metadata = call_gemini(payload, config)
        else:
            answer, metadata = call_claude(payload, config)
        row: dict[str, Any] = {
            "question_id": item["question"]["question_id"],
            "question_text": item["question"]["question_text"],
            "arm": arm,
            "provider": provider,
            "request_model": config["model"],
            "reasoning_setting": config["reasoning"],
            "temperature": config["temperature"],
            "max_completion_tokens": MAX_COMPLETION_TOKENS,
            "answer": answer,
            "shared_system_prompt_sha256": sha256(SHARED_PROMPT),
            "arm_prompt_sha256": sha256(
                DIRECT_PROMPT if arm == "direct" else RAG_PROMPT
            ),
            "request_sha256": base.payload_sha256(payload),
            **metadata,
        }
        if arm == "rag":
            row.update(
                {
                    "retrieval_config_name": item["retrieval"].get(
                        "retrieval_config_name", ""
                    ),
                    "retrieved_context": item["retrieval"][
                        "retrieved_context"
                    ],
                    "soft_eligibility_tags": item["tags"][
                        "validated_chunk_tags"
                    ],
                    "tag_response_model": item["tags"].get(
                        "tag_response_model", ""
                    ),
                    "tag_execution_sha256": item["tags"].get(
                        "tag_execution_sha256", ""
                    ),
                }
            )
        return row

    def reusable(item: dict[str, Any], row: dict[str, Any]) -> bool:
        expected = base.payload_sha256(
            request_payload(item, arm, provider)
        )
        return (
            row.get("request_sha256") == expected
            and row.get("request_model") == config["model"]
        )

    started = time.perf_counter()
    rows = base.run_parallel(
        items=items,
        key=key,
        worker=worker,
        output_path=output,
        workers=workers,
        label=f"{provider} {arm}",
        resume=resume,
        reuse_validator=reusable,
    )
    return rows, time.perf_counter() - started


def write_usage(
    out: Path,
    arms: dict[str, tuple[list[dict[str, Any]], float]],
) -> None:
    rows = []
    for arm, (answers, wall_clock) in arms.items():
        rows.append(
            {
                "stage": f"{arm}_answer_generation",
                "api_call_count": len(answers),
                "prompt_tokens": sum(row["prompt_tokens"] for row in answers),
                "cached_prompt_tokens": sum(
                    row["cached_prompt_tokens"] for row in answers
                ),
                "answer_tokens": sum(row["answer_tokens"] for row in answers),
                "thinking_tokens": sum(
                    row["thinking_tokens"] for row in answers
                ),
                "output_tokens_billed": sum(
                    row["output_tokens_billed"] for row in answers
                ),
                "total_tokens": sum(row["total_tokens"] for row in answers),
                "estimated_cost_usd": sum(
                    row["estimated_cost_usd"] for row in answers
                ),
                "api_latency_seconds_sum": sum(
                    row["latency_seconds"] for row in answers
                ),
                "wall_clock_seconds": wall_clock,
            }
        )
    base.write_csv(out / "usage/generation_usage_summary.csv", rows)


def write_manifest(
    out: Path,
    provider: str,
    items: list[dict[str, Any]],
    arms: dict[str, tuple[list[dict[str, Any]], float]],
) -> None:
    config = PROVIDERS[provider]
    response_models = sorted(
        {
            row["response_model"]
            for answers, _ in arms.values()
            for row in answers
        }
    )
    value = {
        "protocol_id": json.loads(PROTOCOL.read_text(encoding="utf-8"))[
            "protocol_id"
        ],
        "protocol_sha256": sha256(PROTOCOL),
        "questions_sha256": sha256(QUESTIONS),
        "retrieval_sha256": sha256(RETRIEVAL),
        "tags_sha256": sha256(TAGS),
        "shared_system_prompt_sha256": sha256(SHARED_PROMPT),
        "direct_prompt_sha256": sha256(DIRECT_PROMPT),
        "rag_prompt_sha256": sha256(RAG_PROMPT),
        "question_count": len(items),
        "arms": sorted(arms),
        "provider": provider,
        "request_model": config["model"],
        "response_models": response_models,
        "reasoning_setting": config["reasoning"],
        "temperature": config["temperature"],
        "max_completion_tokens": MAX_COMPLETION_TOKENS,
        "retrieval_or_tagger_api_calls_in_this_run": 0,
        "frozen_retrieval_reused": True,
        "frozen_common_tagger_reused": True,
        "held_out_test40_used": False,
    }
    (out / "run_manifest.json").write_text(
        json.dumps(value, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--provider", choices=sorted(PROVIDERS), required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--question-limit", type=int)
    parser.add_argument(
        "--arm",
        choices=("both", "direct", "rag"),
        default="both",
    )
    args = parser.parse_args()
    out = base.prepare_output_dir(args.out, resume=args.resume)
    items = load_inputs(args.question_limit)
    arms = {}
    if args.arm in {"both", "direct"}:
        arms["direct"] = run_arm(
            items,
            "direct",
            args.provider,
            out / "answers/direct.jsonl",
            args.workers,
            args.resume,
        )
    if args.arm in {"both", "rag"}:
        arms["rag"] = run_arm(
            items,
            "rag",
            args.provider,
            out / "answers/rag.jsonl",
            args.workers,
            args.resume,
        )
    write_usage(out, arms)
    write_manifest(out, args.provider, items, arms)


if __name__ == "__main__":
    main()

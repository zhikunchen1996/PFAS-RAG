from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
import time
from pathlib import Path
from typing import Any

from dotenv import load_dotenv


PILOT = Path(__file__).resolve().parents[1]
ROOT = PILOT.parents[2]
V3 = ROOT / "benchmark/frozen_v3"
V3_SCRIPTS = V3 / "scripts"
if str(V3_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(V3_SCRIPTS))

import run_dev13_soft_tags_v3 as tags_runtime  # noqa: E402
import runtime_helpers as base  # noqa: E402


load_dotenv(ROOT / ".env")

PROTOCOL = PILOT / "protocol.json"
SHARED_PROMPT = PILOT / "prompts/shared_system_v1.txt"
DIRECT_PROMPT = PILOT / "prompts/direct_user_v1.txt"
RAG_PROMPT = PILOT / "prompts/rag_user_v1.txt"
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
SELECTOR_LEDGER = (
    V3
    / "results/dev13_retrieval_budget_gpt51_2026-07-26/"
    "bge_llm_gpt51/token_cost_summary.csv"
)
TAGGER_LEDGER = (
    V3
    / "judge/support/layer1_common_tagger_v1/results/"
    "dev13_common_tagger_gpt51_2026-07-26/bge_llm/tokens/"
    "stage_costs.csv"
)

MODEL = "gpt-5.1"
EXPECTED_SNAPSHOT = "gpt-5.1-2025-11-13"
REASONING_EFFORT = "low"
MAX_COMPLETION_TOKENS = 5000
PRICE_INPUT = 1.25
PRICE_CACHED_INPUT = 0.125
PRICE_OUTPUT = 10.0


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def cached_tokens(response: Any) -> int:
    details = getattr(response.usage, "prompt_tokens_details", None)
    return int(getattr(details, "cached_tokens", 0) or 0)


def response_metadata(response: Any, latency: float) -> dict[str, Any]:
    usage = response.usage
    prompt_tokens = int(usage.prompt_tokens or 0)
    completion_tokens = int(usage.completion_tokens or 0)
    cached = cached_tokens(response)
    noncached = max(0, prompt_tokens - cached)
    cost = (
        noncached * PRICE_INPUT
        + cached * PRICE_CACHED_INPUT
        + completion_tokens * PRICE_OUTPUT
    ) / 1_000_000
    finish_reason = str(response.choices[0].finish_reason or "")
    if finish_reason != "stop":
        raise RuntimeError(f"Generation did not finish normally: {finish_reason}")
    if str(response.model) != EXPECTED_SNAPSHOT:
        raise RuntimeError(
            f"Unexpected returned model {response.model}; "
            f"expected {EXPECTED_SNAPSHOT}"
        )
    return {
        "request_model": MODEL,
        "response_id": str(response.id),
        "response_model": str(response.model),
        "system_fingerprint": str(response.system_fingerprint or ""),
        "finish_reason": finish_reason,
        "reasoning_effort": REASONING_EFFORT,
        "temperature": "provider_default_not_sent",
        "max_completion_tokens": MAX_COMPLETION_TOKENS,
        "prompt_tokens": prompt_tokens,
        "cached_prompt_tokens": cached,
        "completion_tokens": completion_tokens,
        "total_tokens": prompt_tokens + completion_tokens,
        "estimated_cost_usd": cost,
        "latency_seconds": latency,
    }


def load_inputs(limit: int | None) -> list[dict[str, Any]]:
    questions = base.read_csv(QUESTIONS)
    if limit is not None:
        questions = questions[:limit]
    retrieval_rows = base.read_jsonl(RETRIEVAL)
    tag_rows = base.read_jsonl(TAGS)
    retrieval = {row["question_id"]: row for row in retrieval_rows}
    tags = {row["question_id"]: row for row in tag_rows}
    expected = [row["question_id"] for row in questions]
    if any(qid not in retrieval or qid not in tags for qid in expected):
        raise RuntimeError("Missing retrieval or tags for a pilot question")
    items = []
    for question in questions:
        qid = question["question_id"]
        row = retrieval[qid]
        contexts = row.get("retrieved_context", [])
        if len(contexts) != 10:
            raise RuntimeError(f"{qid}: expected ten retrieved chunks")
        items.append(
            {
                "question": question,
                "retrieval": row,
                "tags": tags[qid],
            }
        )
    return items


def request_for(item: dict[str, Any], arm: str) -> dict[str, Any]:
    shared = SHARED_PROMPT.read_text(encoding="utf-8")
    question = item["question"]["question_text"]
    if arm == "direct":
        user = base.render(
            DIRECT_PROMPT.read_text(encoding="utf-8"),
            question_text=question,
        )
    elif arm == "rag":
        context = tags_runtime.format_tagged_context(
            item["retrieval"]["retrieved_context"],
            item["tags"],
        )
        user = base.render(
            RAG_PROMPT.read_text(encoding="utf-8"),
            question_text=question,
            retrieved_context=context,
        )
    else:
        raise ValueError(f"Unknown arm: {arm}")
    return {
        "model": MODEL,
        "reasoning_effort": REASONING_EFFORT,
        "max_completion_tokens": MAX_COMPLETION_TOKENS,
        "messages": [
            {"role": "system", "content": shared},
            {"role": "user", "content": user},
        ],
    }


def run_arm(
    items: list[dict[str, Any]],
    arm: str,
    output: Path,
    workers: int,
    resume: bool,
) -> tuple[list[dict[str, Any]], float]:
    def key(row: dict[str, Any]) -> str:
        if "question_id" in row:
            return str(row["question_id"])
        return str(row["question"]["question_id"])

    def worker(item: dict[str, Any]) -> dict[str, Any]:
        request = request_for(item, arm)
        started = time.perf_counter()
        response = base.client().chat.completions.create(**request)
        latency = time.perf_counter() - started
        answer = response.choices[0].message.content or ""
        if not answer.strip():
            raise RuntimeError(
                f"{item['question']['question_id']}: empty {arm} answer"
            )
        row: dict[str, Any] = {
            "question_id": item["question"]["question_id"],
            "question_text": item["question"]["question_text"],
            "arm": arm,
            "answer": answer,
            "shared_system_prompt_sha256": sha256(SHARED_PROMPT),
            "arm_prompt_sha256": sha256(
                DIRECT_PROMPT if arm == "direct" else RAG_PROMPT
            ),
            "request_sha256": base.payload_sha256(request),
            **response_metadata(response, latency),
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
        return row.get("request_sha256") == base.payload_sha256(
            request_for(item, arm)
        )

    started = time.perf_counter()
    rows = base.run_parallel(
        items=items,
        key=key,
        worker=worker,
        output_path=output,
        workers=workers,
        label=f"Stage4 GPT-5.1 {arm}",
        resume=resume,
        reuse_validator=reusable,
    )
    return rows, time.perf_counter() - started


def write_usage_summary(
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
                "completion_tokens": sum(
                    row["completion_tokens"] for row in answers
                ),
                "total_tokens": sum(row["total_tokens"] for row in answers),
                "estimated_cost_usd": sum(
                    row["estimated_cost_usd"] for row in answers
                ),
                "api_latency_seconds_sum": sum(
                    row["latency_seconds"] for row in answers
                ),
                "wall_clock_seconds": wall_clock,
                "cost_provenance": "current_provider_calls",
            }
        )
    for label, path in (
        ("frozen_bge_llm_selector", SELECTOR_LEDGER),
        ("frozen_common_tagger", TAGGER_LEDGER),
    ):
        rows.append(
            {
                "stage": label,
                "api_call_count": "",
                "prompt_tokens": "",
                "cached_prompt_tokens": "",
                "completion_tokens": "",
                "total_tokens": "",
                "estimated_cost_usd": "",
                "api_latency_seconds_sum": "",
                "wall_clock_seconds": "",
                "cost_provenance": (
                    f"reused_frozen_ledger:{path.relative_to(ROOT)}"
                ),
            }
        )
    base.write_csv(out / "usage/generation_usage_summary.csv", rows)


def write_run_manifest(
    out: Path,
    items: list[dict[str, Any]],
    arms: dict[str, tuple[list[dict[str, Any]], float]],
) -> None:
    manifest = {
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
        "request_model": MODEL,
        "required_returned_snapshot": EXPECTED_SNAPSHOT,
        "reasoning_effort": REASONING_EFFORT,
        "temperature": "provider_default_not_sent",
        "max_completion_tokens": MAX_COMPLETION_TOKENS,
        "retrieval_or_tagger_api_calls_in_this_run": 0,
        "frozen_retrieval_reused": True,
        "frozen_common_tagger_reused": True,
    }
    (out / "run_manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True)
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--question-limit", type=int)
    parser.add_argument(
        "--arm",
        choices=("both", "direct", "rag"),
        default="both",
        help="Run both arms for formal generation; single-arm is for smoke tests.",
    )
    args = parser.parse_args()

    out = base.prepare_output_dir(args.out, resume=args.resume)
    items = load_inputs(args.question_limit)
    arms = {}
    if args.arm in ("both", "direct"):
        arms["direct"] = run_arm(
            items,
            "direct",
            out / "answers/direct.jsonl",
            args.workers,
            args.resume,
        )
    if args.arm in ("both", "rag"):
        arms["rag"] = run_arm(
            items,
            "rag",
            out / "answers/rag.jsonl",
            args.workers,
            args.resume,
        )
    write_usage_summary(out, arms)
    write_run_manifest(out, items, arms)


if __name__ == "__main__":
    main()

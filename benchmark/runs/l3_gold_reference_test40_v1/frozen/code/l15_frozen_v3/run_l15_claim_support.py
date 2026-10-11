from __future__ import annotations

import argparse
import time
from pathlib import Path
from typing import Any

import judge_common as common


PROMPT = common.JUDGE / "prompts/l15_claim_citation_support_v2.txt"
REASONING_EFFORT = "low"
MAX_COMPLETION_TOKENS = 12_000


def complete_context(answer: dict[str, Any]) -> list[dict[str, str]]:
    contexts = answer.get("retrieved_context")
    if not isinstance(contexts, list) or not contexts:
        raise ValueError(f"{answer.get('question_id')}: missing context")
    by_rank = {int(row["rank"]): row for row in contexts}
    if len(by_rank) != len(contexts):
        raise ValueError(f"{answer.get('question_id')}: duplicate rank")
    cited = {
        int(value) for value in common.CITATION_RE.findall(answer["answer"])
    }
    if cited - set(by_rank):
        raise ValueError(
            f"{answer.get('question_id')}: citation lacks original chunk"
        )
    return [
        {
            "citation_id": f"C{rank}",
            "text": str(by_rank[rank].get("text", "")),
        }
        for rank in sorted(by_rank)
    ]


def build_payloads(
    questions: list[dict[str, Any]],
    answers: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    question_map = common.by_question(questions)
    ordered_answers = common.ordered_for_questions(
        answers,
        questions,
        source_name="L1.5 answers",
    )
    payloads = []
    for answer in ordered_answers:
        qid = str(answer["question_id"])
        model_payload = {
            "question": question_map[qid]["question_text"],
            "answer_with_citations": answer["answer"],
            "complete_original_final_context": complete_context(answer),
        }
        payloads.append(
            {
                "payload_id": common.payload_sha256(model_payload),
                "question_id": qid,
                "model_payload": model_payload,
            }
        )
    return payloads


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--answers", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--questions", default=str(common.QUESTIONS_TEST))
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    out = Path(args.out).expanduser().resolve()
    if out.exists() and any(out.iterdir()):
        raise RuntimeError(f"Refusing to overwrite non-empty directory: {out}")
    out.mkdir(parents=True, exist_ok=True)
    answers_path = Path(args.answers).expanduser().resolve()
    questions_path = Path(args.questions).expanduser().resolve()
    payloads = build_payloads(
        common.read_csv(questions_path),
        common.read_jsonl(answers_path),
    )
    common.write_jsonl(out / "local_envelopes.jsonl", payloads)
    common.write_jsonl(
        out / "model_payloads.jsonl",
        [row["model_payload"] for row in payloads],
    )
    if args.dry_run:
        return

    started = time.perf_counter()
    results = common.run_payloads_parallel(
        payloads=payloads,
        prompt=PROMPT.read_text(encoding="utf-8"),
        output_path=out / "judge_results.jsonl",
        workers=args.workers,
        reasoning_effort=REASONING_EFFORT,
        max_completion_tokens=MAX_COMPLETION_TOKENS,
    )
    common.write_json(
        out / "run_manifest.json",
        {
            "layer": "L1.5 Test-only claim-level citation sanity",
            "model": common.MODEL,
            "returned_snapshot_required": common.EXPECTED_MODEL_SNAPSHOT,
            "reasoning_effort": REASONING_EFFORT,
            "prompt_sha256": common.sha256(PROMPT),
            "answers_sha256": common.sha256(answers_path),
            "questions_sha256": common.sha256(questions_path),
            "question_count": len(payloads),
            "claim_level_not_attachment_level": True,
            "all_final_chunks_supplied": True,
            "temperature": "provider default; not sent",
            "total_tokens": sum(row["total_tokens"] for row in results),
            "estimated_cost_usd": sum(
                row["estimated_cost_usd"] for row in results
            ),
            "latency_seconds_sum": sum(
                row["latency_seconds"] for row in results
            ),
            "wall_clock_seconds": time.perf_counter() - started,
        },
    )


if __name__ == "__main__":
    main()

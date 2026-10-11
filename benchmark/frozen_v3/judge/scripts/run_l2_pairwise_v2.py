from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from typing import Any

import judge_common as common


PROMPT = common.JUDGE / "prompts/l2_citation_blind_pairwise_v2.txt"


def build_orientation(
    *,
    question: dict[str, Any],
    gold: list[dict[str, Any]],
    left_answer: str,
    right_answer: str,
    left_label: str,
    right_label: str,
    orientation_index: int,
) -> dict[str, Any]:
    qid = str(question["question_id"])
    first_left = common.deterministic_first_left(
        qid,
        left_label,
        right_label,
    )
    left_is_a = first_left if orientation_index == 0 else not first_left
    assignment = (
        {"A": left_label, "B": right_label}
        if left_is_a
        else {"A": right_label, "B": left_label}
    )
    answer_a = common.strip_citations(
        left_answer if left_is_a else right_answer
    )
    answer_b = common.strip_citations(
        right_answer if left_is_a else left_answer
    )
    for position, answer in (("A", answer_a), ("B", answer_b)):
        findings = common.identity_leak_findings(answer)
        if findings:
            raise ValueError(
                f"{qid}: anonymous Answer {position} failed the mandatory "
                f"identity-leakage scan: {findings}"
            )
    model_payload = {
        "question": question["question_text"],
        "task_boundaries": common.task_boundaries(question),
        "non_exhaustive_gold_evidence": common.visible_gold(gold),
        "answer_A": answer_a,
        "answer_B": answer_b,
    }
    local = {
        "question_id": qid,
        "orientation_index": orientation_index,
        "assignment": assignment,
        "model_payload": model_payload,
    }
    local["payload_id"] = common.payload_sha256(local)
    return local


def build_payloads(
    *,
    questions: list[dict[str, Any]],
    gold_rows: list[dict[str, Any]],
    left_rows: list[dict[str, Any]],
    right_rows: list[dict[str, Any]],
    left_label: str,
    right_label: str,
) -> list[dict[str, Any]]:
    if left_label == right_label:
        raise ValueError("L2 comparison labels must be distinct")
    gold = common.grouped_gold(gold_rows)
    ordered_left = common.ordered_for_questions(
        left_rows,
        questions,
        source_name=f"L2 answers for {left_label}",
    )
    ordered_right = common.ordered_for_questions(
        right_rows,
        questions,
        source_name=f"L2 answers for {right_label}",
    )
    left = common.by_question(ordered_left)
    right = common.by_question(ordered_right)
    payloads: list[dict[str, Any]] = []
    for question in questions:
        qid = str(question["question_id"])
        if qid not in left or qid not in right:
            raise ValueError(f"{qid}: missing answer in one comparison arm")
        if qid not in gold:
            raise ValueError(f"{qid}: no gold evidence")
        for orientation in (0, 1):
            payloads.append(
                build_orientation(
                    question=question,
                    gold=gold[qid],
                    left_answer=str(left[qid]["answer"]),
                    right_answer=str(right[qid]["answer"]),
                    left_label=left_label,
                    right_label=right_label,
                    orientation_index=orientation,
                )
            )
    return payloads


def run_payloads(
    payloads: list[dict[str, Any]],
    *,
    prompt: str,
    output: Path,
    workers: int,
    resume: bool,
) -> list[dict[str, Any]]:
    temporary = output.with_name(output.stem + "_new.jsonl")
    existing: dict[str, dict[str, Any]] = {}
    if resume:
        for recovery_path in (output, temporary):
            if not recovery_path.exists():
                continue
            for row in common.read_jsonl(recovery_path):
                common.validate_judge_result(row["judge_result"])
                if row["payload_id"] in existing:
                    raise RuntimeError(
                        "Resume inputs contain duplicate payload_id: "
                        f"{row['payload_id']}"
                    )
                existing[row["payload_id"]] = row
    expected = {row["payload_id"] for row in payloads}
    if set(existing) - expected:
        raise RuntimeError("Resume output contains unknown payloads")
    if existing:
        common.write_jsonl(
            output,
            [
                existing[row["payload_id"]]
                for row in payloads
                if row["payload_id"] in existing
            ],
        )
    pending = [row for row in payloads if row["payload_id"] not in existing]
    new_rows = (
        common.run_payloads_parallel(
            payloads=pending,
            prompt=prompt,
            output_path=temporary,
            workers=workers,
        )
        if pending
        else []
    )
    combined = {**existing, **{row["payload_id"]: row for row in new_rows}}
    rows = [combined[row["payload_id"]] for row in payloads]
    common.write_jsonl(output, rows)
    if temporary.exists():
        temporary.unlink()
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--left", required=True)
    parser.add_argument("--right", required=True)
    parser.add_argument("--left-label", required=True)
    parser.add_argument("--right-label", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--questions", default=str(common.QUESTIONS_DEV))
    parser.add_argument("--gold", default=str(common.GOLD))
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    out = Path(args.out).expanduser().resolve()
    if out.exists() and any(out.iterdir()) and not args.resume:
        raise RuntimeError(f"Refusing to overwrite non-empty directory: {out}")
    out.mkdir(parents=True, exist_ok=True)
    payloads = build_payloads(
        questions=common.read_csv(Path(args.questions)),
        gold_rows=common.read_jsonl(Path(args.gold)),
        left_rows=common.read_jsonl(Path(args.left)),
        right_rows=common.read_jsonl(Path(args.right)),
        left_label=args.left_label,
        right_label=args.right_label,
    )
    common.write_jsonl(out / "local_envelopes.jsonl", payloads)
    common.write_jsonl(
        out / "model_payloads.jsonl",
        [row["model_payload"] for row in payloads],
    )
    if args.dry_run:
        return

    started = time.perf_counter()
    results = run_payloads(
        payloads,
        prompt=PROMPT.read_text(encoding="utf-8"),
        output=out / "judge_results.jsonl",
        workers=args.workers,
        resume=args.resume,
    )
    common.write_json(
        out / "run_manifest.json",
        {
            "layer": "L2 V2",
            "model": common.MODEL,
            "returned_snapshot_required": common.EXPECTED_MODEL_SNAPSHOT,
            "reasoning_effort": common.REASONING_EFFORT,
            "temperature": "provider default; not sent",
            "prompt_sha256": common.sha256(PROMPT),
            "questions_sha256": common.sha256(Path(args.questions)),
            "gold_sha256": common.sha256(Path(args.gold)),
            "left_sha256": common.sha256(Path(args.left)),
            "right_sha256": common.sha256(Path(args.right)),
            "question_count": len(payloads) // 2,
            "orientations_per_pair_question": 2,
            "adaptive_repeats": False,
            "hard_consensus_resolution": False,
            "unstable_outcomes": False,
            "mandatory_identity_leakage_scan": True,
            "schema_repair": False,
            "normal_finish_reason_required": True,
            "call_count": len(results),
            "total_tokens": sum(row["total_tokens"] for row in results),
            "estimated_cost_usd": sum(
                row["estimated_cost_usd"] for row in results
            ),
            "latency_seconds_sum": sum(
                row["latency_seconds"] for row in results
            ),
            "wall_clock_seconds": time.perf_counter() - started,
            "resume_mode": args.resume,
        },
    )


if __name__ == "__main__":
    main()

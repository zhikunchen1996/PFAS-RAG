from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any


PILOT = Path(__file__).resolve().parents[1]
ROOT = PILOT.parents[2]
V3 = ROOT / "benchmark/frozen_v3"
QUESTIONS = V3 / "input/questions_dev13.csv"
EXPECTED_SNAPSHOT = "gpt-5.1-2025-11-13"
CITATION = re.compile(r"\[C\d+\]", re.IGNORECASE)
SHARED_PROMPT = PILOT / "prompts/shared_system_v1.txt"
DIRECT_PROMPT = PILOT / "prompts/direct_user_v1.txt"
RAG_PROMPT = PILOT / "prompts/rag_user_v1.txt"


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def question_ids() -> list[str]:
    import csv

    with QUESTIONS.open(encoding="utf-8-sig", newline="") as handle:
        return [row["question_id"] for row in csv.DictReader(handle)]


def validate_arm(
    rows: list[dict[str, Any]],
    arm: str,
    expected: list[str],
) -> list[str]:
    errors = []
    ids = [str(row.get("question_id", "")) for row in rows]
    if ids != expected:
        errors.append(f"{arm}: question membership or order mismatch")
    if len(ids) != len(set(ids)):
        errors.append(f"{arm}: duplicate question IDs")
    for row in rows:
        qid = row.get("question_id", "<missing>")
        if row.get("arm") != arm:
            errors.append(f"{arm}/{qid}: incorrect arm")
        if not str(row.get("answer", "")).strip():
            errors.append(f"{arm}/{qid}: empty answer")
        if row.get("response_model") != EXPECTED_SNAPSHOT:
            errors.append(f"{arm}/{qid}: returned snapshot mismatch")
        if row.get("finish_reason") != "stop":
            errors.append(f"{arm}/{qid}: abnormal finish")
        if row.get("reasoning_effort") != "low":
            errors.append(f"{arm}/{qid}: reasoning mismatch")
        if int(row.get("max_completion_tokens", 0)) != 5000:
            errors.append(f"{arm}/{qid}: output budget mismatch")
        if arm == "direct" and CITATION.search(str(row.get("answer", ""))):
            errors.append(f"{arm}/{qid}: citation marker present")
        if arm == "rag":
            if len(row.get("retrieved_context", [])) != 10:
                errors.append(f"{arm}/{qid}: expected ten complete chunks")
            if len(row.get("soft_eligibility_tags", [])) != 10:
                errors.append(f"{arm}/{qid}: expected ten tags")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", required=True)
    args = parser.parse_args()

    run = Path(args.run).expanduser().resolve()
    expected = question_ids()
    direct = read_jsonl(run / "answers/direct.jsonl")
    rag = read_jsonl(run / "answers/rag.jsonl")
    errors = [
        *validate_arm(direct, "direct", expected),
        *validate_arm(rag, "rag", expected),
    ]
    shared_hashes = {
        row.get("shared_system_prompt_sha256") for row in direct + rag
    }
    if len(shared_hashes) != 1:
        errors.append("Direct and RAG do not share one system prompt hash")
    expected_shared_hash = hashlib.sha256(SHARED_PROMPT.read_bytes()).hexdigest()
    if shared_hashes != {expected_shared_hash}:
        errors.append("Recorded shared prompt hash does not match frozen prompt")
    expected_arm_hashes = {
        "direct": hashlib.sha256(DIRECT_PROMPT.read_bytes()).hexdigest(),
        "rag": hashlib.sha256(RAG_PROMPT.read_bytes()).hexdigest(),
    }
    for arm, rows in (("direct", direct), ("rag", rag)):
        hashes = {row.get("arm_prompt_sha256") for row in rows}
        if hashes != {expected_arm_hashes[arm]}:
            errors.append(
                f"{arm}: recorded arm prompt hash does not match frozen prompt"
            )
    report = {
        "status": "pass" if not errors else "fail",
        "expected_question_count": len(expected),
        "direct_question_count": len(direct),
        "rag_question_count": len(rag),
        "same_question_order": (
            [row["question_id"] for row in direct]
            == [row["question_id"] for row in rag]
            == expected
        ),
        "shared_system_prompt_hash_count": len(shared_hashes),
        "length_policy": (
            "No word-count limit, exclusion, or retry rule; word counts are "
            "descriptive diagnostics only."
        ),
        "direct_citation_marker_count": sum(
            len(CITATION.findall(str(row["answer"]))) for row in direct
        ),
        "rag_citation_marker_count": sum(
            len(CITATION.findall(str(row["answer"]))) for row in rag
        ),
        "direct_word_counts": {
            row["question_id"]: len(str(row["answer"]).split())
            for row in direct
        },
        "rag_word_counts": {
            row["question_id"]: len(str(row["answer"]).split())
            for row in rag
        },
        "errors": errors,
    }
    (run / "validation_report.json").write_text(
        json.dumps(report, indent=2) + "\n",
        encoding="utf-8",
    )
    if errors:
        raise SystemExit("\n".join(errors))
    print(
        "PASS: matched GPT-5.1 pilot has 13 Direct and 13 RAG answers "
        "with frozen prompt hashes and matched execution settings. Answer "
        "length was not used for validation."
    )


if __name__ == "__main__":
    main()

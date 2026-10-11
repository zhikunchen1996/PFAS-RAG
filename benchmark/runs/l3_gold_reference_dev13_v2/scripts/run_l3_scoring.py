from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

import common


PROMPT = common.PACKAGE / "prompts/l3_gold_referenced_judge_v1.txt"
FROZEN_REFERENCES = common.PACKAGE / "frozen/reference_answers.jsonl"
CLAIM_VALUES = {
    "full": 1.0,
    "partial": 0.5,
    "absent": 0.0,
    "contradicted": 0.0,
}


def strip_citation_markers(text: str) -> str:
    text = re.sub(
        r"\[(?:C|G)\d+(?:\s*[-,;]\s*(?:C|G)?\d+)*\]",
        "",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(r"\s+([,.;:])", r"\1", text)
    return re.sub(r"[ \t]{2,}", " ", text).strip()


def answer_text(row: dict[str, Any]) -> str:
    for key in ["answer", "response", "output", "text"]:
        if isinstance(row.get(key), str) and row[key].strip():
            return row[key]
    raise RuntimeError(f"No answer text in row {row.get('question_id', '')}")


def validate_result(result: dict[str, Any], reference: dict[str, Any]) -> None:
    qid = reference["question_id"]
    if result.get("question_id") != qid:
        raise RuntimeError(f"{qid}: judge returned a different question ID")
    expected = {
        row["claim_id"] for row in reference["reference"]["claims"]
    }
    actual = {
        row.get("claim_id") for row in result.get("claim_assessments", [])
    }
    if actual != expected:
        raise RuntimeError(f"{qid}: claim-assessment membership differs")
    for row in result["claim_assessments"]:
        if row.get("status") not in CLAIM_VALUES:
            raise RuntimeError(f"{qid}: invalid claim status")


def score_result(
    result: dict[str, Any],
    reference: dict[str, Any],
) -> dict[str, Any]:
    claim_types = {
        row["claim_id"]: row["claim_type"]
        for row in reference["reference"]["claims"]
    }
    assessments = {
        row["claim_id"]: row for row in result["claim_assessments"]
    }
    all_values = [
        CLAIM_VALUES[assessments[claim_id]["status"]]
        for claim_id in claim_types
    ]
    core_ids = [
        claim_id
        for claim_id, claim_type in claim_types.items()
        if claim_type == "core"
    ]
    core_values = [
        CLAIM_VALUES[assessments[claim_id]["status"]] for claim_id in core_ids
    ]
    contradicted_core = sum(
        assessments[claim_id]["status"] == "contradicted"
        for claim_id in core_ids
    )
    all_coverage = sum(all_values) / len(all_values)
    core_coverage = sum(core_values) / len(core_values)
    boundary_violation = bool(result["task_boundary_violation"])
    major_error = bool(result["major_scientific_error"])
    passed = (
        core_coverage >= 0.5
        and all_coverage >= 0.5
        and contradicted_core == 0
        and not boundary_violation
        and not major_error
    )
    return {
        "core_gold_claim_coverage": core_coverage,
        "all_gold_claim_coverage": all_coverage,
        "contradicted_core_claims": contradicted_core,
        "task_boundary_violation": boundary_violation,
        "major_scientific_error": major_error,
        "l3_gold_referenced_adequacy_pass": passed,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--system",
        action="append",
        required=True,
        help="LABEL=path/to/answers.jsonl; may be repeated",
    )
    parser.add_argument("--out", required=True)
    parser.add_argument("--model", default="gpt-4.1-2025-04-14")
    parser.add_argument("--reasoning-effort", default="none")
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--max-completion-tokens", type=int, default=4000)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()

    if not FROZEN_REFERENCES.exists():
        raise RuntimeError("L3 references are not frozen")
    references = {
        row["question_id"]: row
        for row in common.read_jsonl(FROZEN_REFERENCES)
    }
    systems: dict[str, Path] = {}
    for value in args.system:
        label, separator, raw_path = value.partition("=")
        if not separator or not label or not raw_path:
            raise RuntimeError(f"Invalid --system value: {value}")
        systems[label] = Path(raw_path).expanduser().resolve()

    items = []
    for label, path in systems.items():
        rows = {row["question_id"]: row for row in common.read_jsonl(path)}
        if set(rows) != set(references):
            raise RuntimeError(f"{label}: answer membership differs from reference")
        for qid, reference in references.items():
            normalized = strip_citation_markers(answer_text(rows[qid]))
            candidate_id = common.payload_sha256(
                {"system": label, "question_id": qid, "answer": normalized}
            )[:16]
            model_payload = {
                "question_id": qid,
                "question": reference["question_text"],
                "task_boundaries": reference["task_boundaries"],
                "gold_is_non_exhaustive": True,
                "frozen_reference_answer": reference["reference"][
                    "reference_answer"
                ],
                "frozen_reference_claims": reference["reference"]["claims"],
                "anonymous_candidate_answer": normalized,
            }
            items.append(
                {
                    "item_id": f"{label}::{qid}",
                    "question_id": qid,
                    "system_label_local_only": label,
                    "candidate_id": candidate_id,
                    "model_payload": model_payload,
                    "source_answer_sha256": common.sha256(path),
                }
            )

    out = Path(args.out).expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)
    common.write_jsonl(out / "local_envelopes.jsonl", items)
    common.write_jsonl(
        out / "model_payloads.jsonl",
        [row["model_payload"] for row in items],
    )
    prompt = PROMPT.read_text(encoding="utf-8")

    def worker(item: dict[str, Any]) -> dict[str, Any]:
        result, metadata = common.call_openai_json(
            system_prompt=prompt,
            payload=item["model_payload"],
            model=args.model,
            reasoning_effort=args.reasoning_effort,
            max_completion_tokens=args.max_completion_tokens,
            temperature=args.temperature,
        )
        reference = references[item["question_id"]]
        validate_result(result, reference)
        return {
            "item_id": item["item_id"],
            "question_id": item["question_id"],
            "system_label_local_only": item["system_label_local_only"],
            "candidate_id": item["candidate_id"],
            "assessment": result,
            "scores": score_result(result, reference),
            "judge": metadata,
        }

    rows = common.run_parallel(
        items=items,
        worker=worker,
        key=lambda row: str(row["item_id"]),
        output=out / "judge_results.jsonl",
        workers=args.workers,
        resume=args.resume,
    )
    summaries = []
    for label in systems:
        selected = [
            row for row in rows if row["system_label_local_only"] == label
        ]
        summaries.append(
            {
                "system": label,
                "question_count": len(selected),
                "mean_core_gold_claim_coverage": sum(
                    row["scores"]["core_gold_claim_coverage"]
                    for row in selected
                )
                / len(selected),
                "mean_all_gold_claim_coverage": sum(
                    row["scores"]["all_gold_claim_coverage"]
                    for row in selected
                )
                / len(selected),
                "task_boundary_compliance_rate": sum(
                    not row["scores"]["task_boundary_violation"]
                    for row in selected
                )
                / len(selected),
                "major_error_rate": sum(
                    row["scores"]["major_scientific_error"]
                    for row in selected
                )
                / len(selected),
                "l3_gold_referenced_adequacy_pass_rate": sum(
                    row["scores"]["l3_gold_referenced_adequacy_pass"]
                    for row in selected
                )
                / len(selected),
            }
        )
    common.write_csv(out / "system_summary.csv", summaries)
    common.write_json(
        out / "run_manifest.json",
        {
            "protocol_id": "l3_gold_reference_dev13_v1",
            "reference_sha256": common.sha256(FROZEN_REFERENCES),
            "prompt_sha256": common.sha256(PROMPT),
            "request_model": args.model,
            "reasoning_effort": args.reasoning_effort,
            "temperature": args.temperature,
            "citation_markers_removed": True,
            "candidate_system_count": len(systems),
            "candidate_answer_count": len(rows),
            "total_tokens": sum(row["judge"]["total_tokens"] for row in rows),
            "estimated_cost_usd": sum(
                row["judge"]["estimated_cost_usd"] for row in rows
            ),
            "latency_seconds_sum": sum(
                row["judge"]["latency_seconds"] for row in rows
            ),
        },
    )
    print(json.dumps(summaries, indent=2))


if __name__ == "__main__":
    main()

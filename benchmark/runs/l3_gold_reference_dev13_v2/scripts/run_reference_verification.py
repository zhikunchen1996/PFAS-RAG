from __future__ import annotations

import argparse
import json
import os
import subprocess
import time
from pathlib import Path
from typing import Any

import common


PROMPT = common.PACKAGE / "prompts/reference_claim_verification_v1.txt"

SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "question_id": {"type": "string"},
        "overall_verdict": {
            "type": "string",
            "enum": ["approve", "revise", "reject"],
        },
        "claim_reviews": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "claim_id": {"type": "string"},
                    "verdict": {
                        "type": "string",
                        "enum": [
                            "supported",
                            "partially_supported",
                            "unsupported",
                            "contradicted",
                        ],
                    },
                    "verified_evidence_ids": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                    "incorrect_or_unused_evidence_ids": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                    "issue_categories": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                    "rationale": {"type": "string"},
                    "recommended_claim_text": {"type": "string"},
                },
                "required": [
                    "claim_id",
                    "verdict",
                    "verified_evidence_ids",
                    "incorrect_or_unused_evidence_ids",
                    "issue_categories",
                    "rationale",
                    "recommended_claim_text",
                ],
            },
        },
        "omitted_gold_findings": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "suggested_claim_type": {
                        "type": "string",
                        "enum": [
                            "core",
                            "supporting",
                            "limitation",
                            "negative_boundary",
                        ],
                    },
                    "suggested_claim_text": {"type": "string"},
                    "evidence_ids": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                    "rationale": {"type": "string"},
                },
                "required": [
                    "suggested_claim_type",
                    "suggested_claim_text",
                    "evidence_ids",
                    "rationale",
                ],
            },
        },
        "reference_answer_issues": {
            "type": "array",
            "items": {"type": "string"},
        },
        "boundary_assessment": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "must_include_addressed": {"type": "boolean"},
                "must_not_claim_respected": {"type": "boolean"},
                "rationale": {"type": "string"},
            },
            "required": [
                "must_include_addressed",
                "must_not_claim_respected",
                "rationale",
            ],
        },
        "human_review_priorities": {
            "type": "array",
            "items": {"type": "string"},
        },
    },
    "required": [
        "question_id",
        "overall_verdict",
        "claim_reviews",
        "omitted_gold_findings",
        "reference_answer_issues",
        "boundary_assessment",
        "human_review_priorities",
    ],
}


def parse_cli_output(text: str) -> tuple[dict[str, Any], dict[str, Any]]:
    envelope = json.loads(text)
    raw_result = envelope.get("structured_output", envelope.get("result"))
    if isinstance(raw_result, str):
        result = json.loads(raw_result)
    elif isinstance(raw_result, dict):
        result = raw_result
    else:
        raise RuntimeError("Claude CLI did not return structured JSON")
    metadata = {
        key: envelope.get(key)
        for key in [
            "session_id",
            "duration_ms",
            "duration_api_ms",
            "num_turns",
            "total_cost_usd",
            "usage",
            "modelUsage",
        ]
        if key in envelope
    }
    return result, metadata


def validate_review(
    result: dict[str, Any],
    packet: dict[str, Any],
    draft: dict[str, Any],
) -> None:
    if result.get("question_id") != packet["question_id"]:
        raise RuntimeError(f"{packet['question_id']}: reviewer ID mismatch")
    expected_claims = {
        claim["claim_id"] for claim in draft["draft"]["claims"]
    }
    reviewed_claims = {
        claim["claim_id"] for claim in result.get("claim_reviews", [])
    }
    if reviewed_claims != expected_claims:
        raise RuntimeError(
            f"{packet['question_id']}: reviewer claim membership differs"
        )
    valid_evidence = {
        row["evidence_id"] for row in packet["gold_evidence"]
    }
    for review in result["claim_reviews"]:
        referenced = set(review["verified_evidence_ids"]) | set(
            review["incorrect_or_unused_evidence_ids"]
        )
        if not referenced <= valid_evidence:
            raise RuntimeError(
                f"{packet['question_id']}: reviewer cited unknown evidence"
            )
    for finding in result["omitted_gold_findings"]:
        if not set(finding["evidence_ids"]) <= valid_evidence:
            raise RuntimeError(
                f"{packet['question_id']}: omitted finding cited unknown evidence"
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="claude-sonnet-5")
    parser.add_argument("--effort", default="medium")
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--timeout", type=int, default=900)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--limit", type=int)
    args = parser.parse_args()

    if not common.PACKETS.exists() or not common.DRAFTS.exists():
        raise RuntimeError("Build packets and Model A drafts first")
    packets = common.read_jsonl(common.PACKETS)
    drafts = {
        row["question_id"]: row for row in common.read_jsonl(common.DRAFTS)
    }
    packets = [row for row in packets if row["question_id"] in drafts]
    if args.limit is not None:
        packets = packets[: args.limit]
    prompt = PROMPT.read_text(encoding="utf-8")

    def worker(packet: dict[str, Any]) -> dict[str, Any]:
        qid = packet["question_id"]
        reviewer_payload = {
            "reference_construction_packet": packet,
            "model_a_draft": drafts[qid]["draft"],
        }
        full_prompt = (
            prompt
            + "\n\nINPUT JSON:\n"
            + json.dumps(reviewer_payload, ensure_ascii=False)
        )
        command = [
            "claude",
            "-p",
            "--model",
            args.model,
            "--effort",
            args.effort,
            "--output-format",
            "json",
            "--json-schema",
            json.dumps(SCHEMA, separators=(",", ":")),
            "--no-session-persistence",
            "--permission-mode",
            "dontAsk",
        ]
        started = time.perf_counter()
        cli_environment = dict(os.environ)
        cli_environment.pop("ANTHROPIC_API_KEY", None)
        completed = subprocess.run(
            command,
            input=full_prompt,
            text=True,
            capture_output=True,
            timeout=args.timeout,
            check=False,
            env=cli_environment,
        )
        latency = time.perf_counter() - started
        if completed.returncode != 0:
            raise RuntimeError(
                f"{qid}: Claude CLI failed ({completed.returncode}): "
                f"{completed.stderr[-1000:]}"
            )
        result, metadata = parse_cli_output(completed.stdout)
        validate_review(result, packet, drafts[qid])
        return {
            "question_id": qid,
            "packet_sha256": common.payload_sha256(packet),
            "model_a_draft_sha256": common.payload_sha256(
                drafts[qid]["draft"]
            ),
            "prompt_sha256": common.sha256(PROMPT),
            "review": result,
            "verification": {
                "provider": "Anthropic Claude CLI",
                "request_model": args.model,
                "effort": args.effort,
                "temperature": "provider_managed_not_sent",
                "latency_seconds": latency,
                **metadata,
            },
        }

    rows = common.run_parallel(
        items=packets,
        worker=worker,
        key=lambda row: str(row["question_id"]),
        output=common.REVIEWS,
        workers=args.workers,
        resume=args.resume,
    )
    common.write_json(
        common.PACKAGE / "reference_build/reviews/run_manifest.json",
        {
            "stage": "Model B independent claim verification",
            "question_count": len(rows),
            "provider": "Anthropic Claude CLI",
            "future_rerun_model": args.model,
            "actual_request_models": sorted(
                {
                    str(row["verification"]["request_model"])
                    for row in rows
                }
            ),
            "actual_returned_models": sorted(
                {
                    model
                    for row in rows
                    for model in (
                        row["verification"].get("modelUsage") or {}
                    )
                    if "sonnet" in model
                }
            ),
            "effort": args.effort,
            "temperature": "provider_managed_not_sent",
            "prompt_sha256": common.sha256(PROMPT),
            "packets_sha256": common.sha256(common.PACKETS),
            "model_a_drafts_sha256": common.sha256(common.DRAFTS),
            "output_sha256": common.sha256(common.REVIEWS),
            "latency_seconds_sum": sum(
                float(row["verification"]["latency_seconds"]) for row in rows
            ),
            "reported_cost_usd": sum(
                float(row["verification"].get("total_cost_usd") or 0)
                for row in rows
            ),
        },
    )
    print(json.dumps({"reviews": len(rows)}, indent=2))


if __name__ == "__main__":
    main()

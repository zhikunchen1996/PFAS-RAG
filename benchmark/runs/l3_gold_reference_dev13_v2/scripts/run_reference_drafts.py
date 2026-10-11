from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import common


PROMPT = common.PACKAGE / "prompts/reference_draft_v1.txt"


def validate_draft(result: dict[str, Any], packet: dict[str, Any]) -> None:
    required = {
        "question_id",
        "answerability",
        "answerability_rationale",
        "reference_answer",
        "claims",
        "unresolved_or_unsupported",
        "boundary_check",
    }
    if set(result) != required:
        raise RuntimeError(
            f"{packet['question_id']}: draft keys differ: {sorted(set(result) ^ required)}"
        )
    if result["question_id"] != packet["question_id"]:
        raise RuntimeError(f"{packet['question_id']}: returned question ID differs")
    claims = result["claims"]
    if not isinstance(claims, list) or not claims:
        raise RuntimeError(f"{packet['question_id']}: no reference claims")
    allowed_ids = {
        evidence["evidence_id"] for evidence in packet["gold_evidence"]
    }
    claim_ids: set[str] = set()
    for claim in claims:
        claim_id = str(claim.get("claim_id", ""))
        if not claim_id or claim_id in claim_ids:
            raise RuntimeError(f"{packet['question_id']}: invalid claim ID")
        claim_ids.add(claim_id)
        evidence_ids = claim.get("evidence_ids")
        if not evidence_ids or not set(evidence_ids) <= allowed_ids:
            raise RuntimeError(
                f"{packet['question_id']} {claim_id}: invalid evidence links"
            )
        if claim.get("claim_type") not in {
            "core",
            "supporting",
            "limitation",
            "negative_boundary",
        }:
            raise RuntimeError(
                f"{packet['question_id']} {claim_id}: invalid claim type"
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="gpt-5.1-2025-11-13")
    parser.add_argument("--reasoning-effort", default="medium")
    parser.add_argument("--max-completion-tokens", type=int, default=7000)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--limit", type=int)
    args = parser.parse_args()

    if not common.PACKETS.exists():
        raise RuntimeError("Run build_reference_packets.py first")
    packets = common.read_jsonl(common.PACKETS)
    if args.limit is not None:
        packets = packets[: args.limit]
    prompt = PROMPT.read_text(encoding="utf-8")

    def worker(packet: dict[str, Any]) -> dict[str, Any]:
        result, metadata = common.call_openai_json(
            system_prompt=prompt,
            payload=packet,
            model=args.model,
            reasoning_effort=args.reasoning_effort,
            max_completion_tokens=args.max_completion_tokens,
        )
        validate_draft(result, packet)
        return {
            "question_id": packet["question_id"],
            "packet_sha256": common.payload_sha256(packet),
            "prompt_sha256": common.sha256(PROMPT),
            "draft": result,
            "generation": metadata,
        }

    rows = common.run_parallel(
        items=packets,
        worker=worker,
        key=lambda row: str(row["question_id"]),
        output=common.DRAFTS,
        workers=args.workers,
        resume=args.resume,
    )
    for row in rows:
        row["generation"]["estimated_cost_usd"] = (
            common.estimate_openai_cost(
                row["generation"],
                str(row["generation"]["request_model"]),
            )
        )
    common.write_jsonl(common.DRAFTS, rows)
    common.write_json(
        common.PACKAGE / "reference_build/drafts/run_manifest.json",
        {
            "stage": "Model A structured reference drafting",
            "question_count": len(rows),
            "future_rerun_model": args.model,
            "actual_request_models": sorted(
                {
                    str(row["generation"]["request_model"])
                    for row in rows
                }
            ),
            "actual_response_models": sorted(
                {
                    str(row["generation"]["response_model"])
                    for row in rows
                }
            ),
            "reasoning_effort": args.reasoning_effort,
            "temperature": "provider_default_not_sent",
            "prompt_sha256": common.sha256(PROMPT),
            "packets_sha256": common.sha256(common.PACKETS),
            "output_sha256": common.sha256(common.DRAFTS),
            "total_tokens": sum(
                int(row["generation"]["total_tokens"]) for row in rows
            ),
            "latency_seconds_sum": sum(
                float(row["generation"]["latency_seconds"]) for row in rows
            ),
            "estimated_cost_usd": sum(
                float(row["generation"]["estimated_cost_usd"])
                for row in rows
            ),
            "pricing_usd_per_million_tokens": (
                common.OPENAI_PRICES_PER_MILLION.get(args.model, {})
            ),
        },
    )
    print(json.dumps({"drafts": len(rows)}, indent=2))


if __name__ == "__main__":
    main()

from __future__ import annotations

import argparse
import copy
import json
import os
import subprocess
import time
from pathlib import Path
from typing import Any

import common
import run_reference_revision_v2 as revision


PROMPT = common.PACKAGE / "prompts/reference_group_verification_v2.txt"
OUTPUT = (
    common.PACKAGE
    / "reference_build/reviews/model_b_group_reviews_v2.jsonl"
)

VERDICT = {
    "type": "string",
    "enum": [
        "supported",
        "partially_supported",
        "unsupported",
        "contradicted",
        "duplicate_or_fragment",
    ],
}
SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "question_id": {"type": "string"},
        "overall_verdict": {
            "type": "string",
            "enum": ["approve", "revise", "reject"],
        },
        "component_reviews": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "task_component_id": {"type": "string"},
                    "verdict": {
                        "type": "string",
                        "enum": ["approve", "revise"],
                    },
                    "rationale": {"type": "string"},
                },
                "required": [
                    "task_component_id",
                    "verdict",
                    "rationale",
                ],
            },
        },
        "claim_group_reviews": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "claim_group_id": {"type": "string"},
                    "verdict": VERDICT,
                    "verified_evidence_ids": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                    "issue_categories": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                    "rationale": {"type": "string"},
                    "recommended_change": {"type": "string"},
                },
                "required": [
                    "claim_group_id",
                    "verdict",
                    "verified_evidence_ids",
                    "issue_categories",
                    "rationale",
                    "recommended_change",
                ],
            },
        },
        "constraint_group_reviews": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "claim_group_id": {"type": "string"},
                    "verdict": VERDICT,
                    "verified_evidence_ids": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                    "issue_categories": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                    "rationale": {"type": "string"},
                    "recommended_change": {"type": "string"},
                },
                "required": [
                    "claim_group_id",
                    "verdict",
                    "verified_evidence_ids",
                    "issue_categories",
                    "rationale",
                    "recommended_change",
                ],
            },
        },
        "atomic_disposition_complete": {"type": "boolean"},
        "unresolved_prior_claim_ids": {
            "type": "array",
            "items": {"type": "string"},
        },
        "duplicate_or_weighting_issues": {
            "type": "array",
            "items": {"type": "string"},
        },
        "prose_ledger_issues": {
            "type": "array",
            "items": {"type": "string"},
        },
        "omitted_major_gold_findings": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "task_component_id": {"type": "string"},
                    "suggested_proposition": {"type": "string"},
                    "evidence_ids": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                    "rationale": {"type": "string"},
                },
                "required": [
                    "task_component_id",
                    "suggested_proposition",
                    "evidence_ids",
                    "rationale",
                ],
            },
        },
        "human_review_priorities": {
            "type": "array",
            "items": {"type": "string"},
        },
    },
    "required": [
        "question_id",
        "overall_verdict",
        "component_reviews",
        "claim_group_reviews",
        "constraint_group_reviews",
        "atomic_disposition_complete",
        "unresolved_prior_claim_ids",
        "duplicate_or_weighting_issues",
        "prose_ledger_issues",
        "omitted_major_gold_findings",
        "human_review_priorities",
    ],
}


def compact_previous_draft(draft: dict[str, Any]) -> dict[str, Any]:
    return {
        "question_id": draft["question_id"],
        "claims": draft["claims"],
    }


def compact_previous_review(review: dict[str, Any]) -> dict[str, Any]:
    return {
        "question_id": review["question_id"],
        "overall_verdict": review["overall_verdict"],
        "non_supported_claim_reviews": [
            row
            for row in review["claim_reviews"]
            if row.get("verdict") != "supported"
        ],
        "boundary_assessment": review["boundary_assessment"],
        "reference_answer_issues": review["reference_answer_issues"],
        "omitted_gold_findings": review["omitted_gold_findings"],
        "human_review_priorities": review["human_review_priorities"],
    }


def compact_prior_group_review(review: dict[str, Any]) -> dict[str, Any]:
    return {
        "question_id": review["question_id"],
        "overall_verdict": review["overall_verdict"],
        "component_reviews_requiring_revision": [
            row
            for row in review["component_reviews"]
            if row.get("verdict") != "approve"
        ],
        "group_reviews_requiring_revision": [
            row
            for row in (
                review["claim_group_reviews"]
                + review["constraint_group_reviews"]
            )
            if row.get("verdict") != "supported"
        ],
        "atomic_disposition_complete": review["atomic_disposition_complete"],
        "unresolved_prior_claim_ids": review["unresolved_prior_claim_ids"],
        "duplicate_or_weighting_issues": review[
            "duplicate_or_weighting_issues"
        ],
        "prose_ledger_issues": review["prose_ledger_issues"],
        "omitted_major_gold_findings": review["omitted_major_gold_findings"],
        "human_review_priorities": review["human_review_priorities"],
    }


def review_is_clean(review: dict[str, Any]) -> bool:
    return (
        review.get("overall_verdict") == "approve"
        and all(
            row.get("verdict") == "approve"
            for row in review.get("component_reviews", [])
        )
        and all(
            row.get("verdict") == "supported"
            for row in review.get("claim_group_reviews", [])
            + review.get("constraint_group_reviews", [])
        )
        and review.get("atomic_disposition_complete") is True
        and not review.get("unresolved_prior_claim_ids")
        and not review.get("duplicate_or_weighting_issues")
        and not review.get("prose_ledger_issues")
        and not review.get("omitted_major_gold_findings")
    )


def reusable_clean_review(
    row: dict[str, Any],
    *,
    packet: dict[str, Any],
    revised: dict[str, Any],
    source_path: Path,
    source_sha256: str,
) -> dict[str, Any] | None:
    if row.get("question_id") != packet["question_id"]:
        return None
    if row.get("packet_sha256") != common.payload_sha256(packet):
        return None
    if row.get("revision_sha256") != common.payload_sha256(revised):
        return None
    review = row.get("review")
    if not isinstance(review, dict) or not review_is_clean(review):
        return None
    validate_review(review, packet, revised)
    reused = copy.deepcopy(row)
    try:
        display_path = str(source_path.relative_to(common.ROOT))
    except ValueError:
        display_path = str(source_path)
    reused["reuse"] = {
        "reused": True,
        "source_file": display_path,
        "source_file_sha256": source_sha256,
        "reason": (
            "The revised claim-ledger payload is byte-stable under canonical "
            "JSON hashing and the prior Claude review is clean."
        ),
    }
    return reused


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
    revised: dict[str, Any],
) -> None:
    qid = packet["question_id"]
    if result.get("question_id") != qid:
        raise RuntimeError(f"{qid}: reviewer question ID differs")
    expected_components = {
        row["task_component_id"] for row in revised["task_components"]
    }
    actual_components = {
        row["task_component_id"] for row in result["component_reviews"]
    }
    if actual_components != expected_components:
        raise RuntimeError(f"{qid}: component review membership differs")
    expected_claims = {
        row["claim_group_id"] for row in revised["claim_groups"]
    }
    actual_claims = {
        row["claim_group_id"] for row in result["claim_group_reviews"]
    }
    if actual_claims != expected_claims:
        raise RuntimeError(f"{qid}: claim-group review membership differs")
    expected_constraints = {
        row["claim_group_id"] for row in revised["constraint_groups"]
    }
    actual_constraints = {
        row["claim_group_id"] for row in result["constraint_group_reviews"]
    }
    if actual_constraints != expected_constraints:
        raise RuntimeError(f"{qid}: constraint review membership differs")
    valid_evidence = {
        row["evidence_id"] for row in packet["gold_evidence"]
    }
    for row in (
        result["claim_group_reviews"] + result["constraint_group_reviews"]
    ):
        if not set(row["verified_evidence_ids"]) <= valid_evidence:
            raise RuntimeError(f"{qid}: reviewer cited unknown evidence")
    for row in result["omitted_major_gold_findings"]:
        if row["task_component_id"] not in expected_components:
            raise RuntimeError(f"{qid}: omitted finding has unknown component")
        if not set(row["evidence_ids"]) <= valid_evidence:
            raise RuntimeError(f"{qid}: omitted finding cites unknown evidence")


def normalize_review_membership(
    result: dict[str, Any],
    revised: dict[str, Any],
) -> None:
    changed = False
    expected_components = {
        row["task_component_id"] for row in revised["task_components"]
    }
    result["component_reviews"] = [
        row
        for row in result.get("component_reviews", [])
        if row.get("task_component_id") in expected_components
    ]
    reviewed_components = {
        row["task_component_id"] for row in result["component_reviews"]
    }
    for component_id in sorted(expected_components - reviewed_components):
        changed = True
        result["component_reviews"].append(
            {
                "task_component_id": component_id,
                "verdict": "revise",
                "rationale": (
                    "Reviewer omitted this frozen component; it requires "
                    "explicit re-review."
                ),
            }
        )

    def normalize_groups(
        key: str,
        expected: set[str],
    ) -> None:
        nonlocal changed
        result[key] = [
            row
            for row in result.get(key, [])
            if row.get("claim_group_id") in expected
        ]
        reviewed = {row["claim_group_id"] for row in result[key]}
        for group_id in sorted(expected - reviewed):
            changed = True
            result[key].append(
                {
                    "claim_group_id": group_id,
                    "verdict": "partially_supported",
                    "verified_evidence_ids": [],
                    "issue_categories": ["reviewer_omission"],
                    "rationale": (
                        "Reviewer omitted this frozen group; no support "
                        "judgment is inferred."
                    ),
                    "recommended_change": (
                        "Retain the group unchanged and require explicit "
                        "independent re-review."
                    ),
                }
            )

    normalize_groups(
        "claim_group_reviews",
        {row["claim_group_id"] for row in revised["claim_groups"]},
    )
    normalize_groups(
        "constraint_group_reviews",
        {row["claim_group_id"] for row in revised["constraint_groups"]},
    )
    if changed:
        result["overall_verdict"] = "revise"
        priorities = result.setdefault("human_review_priorities", [])
        priorities.append(
            "One or more frozen components or groups were omitted by Model B; "
            "they require explicit re-review before project-author audit."
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="claude-sonnet-5")
    parser.add_argument("--effort", default="medium")
    parser.add_argument(
        "--auth-mode",
        choices=["subscription", "environment"],
        default="subscription",
        help=(
            "Use Claude subscription OAuth/keychain or retain the "
            "ANTHROPIC_API_KEY already loaded from the environment."
        ),
    )
    parser.add_argument(
        "--max-budget-usd",
        type=float,
        default=0.75,
        help="Per-question Claude CLI API budget cap.",
    )
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--timeout", type=int, default=1200)
    parser.add_argument(
        "--payload-profile",
        choices=["full", "compact"],
        default="compact",
    )
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--revisions")
    parser.add_argument(
        "--packets",
        help="Optional versioned reference-packet JSONL; defaults to V1 packets.",
    )
    parser.add_argument(
        "--prior-group-reviews",
        help="Optional prior V2 group-review JSONL for explicit repair verification",
    )
    parser.add_argument(
        "--reuse-clean-from",
        help=(
            "Optional prior group-review JSONL. Clean reviews are reused only "
            "when their canonical revision hash matches the current revision."
        ),
    )
    parser.add_argument("--out")
    args = parser.parse_args()

    packets_path = (
        Path(args.packets).expanduser().resolve()
        if args.packets
        else common.PACKETS
    )
    revisions_path = (
        Path(args.revisions).expanduser().resolve()
        if args.revisions
        else revision.OUTPUT
    )
    output_path = (
        Path(args.out).expanduser().resolve() if args.out else OUTPUT
    )
    required = [
        packets_path,
        common.DRAFTS,
        common.REVIEWS,
        revisions_path,
        PROMPT,
    ]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise RuntimeError(f"Missing group-verification inputs: {missing}")

    packets = common.read_jsonl(packets_path)
    previous_drafts = {
        row["question_id"]: row["draft"]
        for row in common.read_jsonl(common.DRAFTS)
    }
    previous_reviews = {
        row["question_id"]: row["review"]
        for row in common.read_jsonl(common.REVIEWS)
    }
    task_components = {
        row["question_id"]: row
        for row in common.read_jsonl(revision.TASK_COMPONENTS)
    }
    revisions = {
        row["question_id"]: row["revision"]
        for row in common.read_jsonl(revisions_path)
    }
    packets_by_id = {
        row["question_id"]: row for row in packets
    }
    for qid, revised in revisions.items():
        if qid not in packets_by_id or qid not in task_components:
            raise RuntimeError(f"{qid}: missing verification preflight input")
        revision.validate_revision(
            revised,
            packets_by_id[qid],
            task_components[qid],
            previous_drafts[qid],
        )
    prior_group_reviews: dict[str, dict[str, Any]] = {}
    prior_group_reviews_path = None
    if args.prior_group_reviews:
        prior_group_reviews_path = (
            Path(args.prior_group_reviews).expanduser().resolve()
        )
        prior_group_reviews = {
            row["question_id"]: row["review"]
            for row in common.read_jsonl(prior_group_reviews_path)
        }
        if set(prior_group_reviews) != set(revisions):
            raise RuntimeError(
                "Prior V2 group-review membership differs from revisions"
            )
    packets = [row for row in packets if row["question_id"] in revisions]
    if args.limit is not None:
        packets = packets[: args.limit]
    prompt = PROMPT.read_text(encoding="utf-8")
    reused_question_ids: list[str] = []
    reuse_clean_from_path = None
    if args.reuse_clean_from:
        reuse_clean_from_path = (
            Path(args.reuse_clean_from).expanduser().resolve()
        )
        if not reuse_clean_from_path.exists():
            raise RuntimeError(
                f"Reusable review file is missing: {reuse_clean_from_path}"
            )
        source_sha256 = common.sha256(reuse_clean_from_path)
        reusable_source = {
            row["question_id"]: row
            for row in common.read_jsonl(reuse_clean_from_path)
        }
        existing_rows = {
            row["question_id"]: row
            for row in (
                common.read_jsonl(output_path)
                if args.resume and output_path.exists()
                else []
            )
        }
        for packet in packets:
            qid = packet["question_id"]
            source_row = reusable_source.get(qid)
            if source_row is None or qid in existing_rows:
                continue
            reused = reusable_clean_review(
                source_row,
                packet=packet,
                revised=revisions[qid],
                source_path=reuse_clean_from_path,
                source_sha256=source_sha256,
            )
            if reused is not None:
                existing_rows[qid] = reused
                reused_question_ids.append(qid)
        common.write_jsonl(
            output_path,
            [
                existing_rows[packet["question_id"]]
                for packet in packets
                if packet["question_id"] in existing_rows
            ],
        )

    def worker(packet: dict[str, Any]) -> dict[str, Any]:
        qid = packet["question_id"]
        if args.payload_profile == "full":
            payload = {
                "reference_construction_packet": packet,
                "frozen_task_components": task_components[qid],
                "previous_model_a_draft": previous_drafts[qid],
                "previous_model_b_review": previous_reviews[qid],
                "revised_claim_ledger": revisions[qid],
            }
        else:
            payload = {
                "reference_construction_packet": packet,
                "frozen_task_components": task_components[qid],
                "previous_model_a_atomic_claims": compact_previous_draft(
                    previous_drafts[qid]
                ),
                "previous_model_b_open_issues": compact_previous_review(
                    previous_reviews[qid]
                ),
                "revised_claim_ledger": revisions[qid],
            }
        if qid in prior_group_reviews:
            payload["prior_model_b_group_review_open_issues"] = (
                compact_prior_group_review(prior_group_reviews[qid])
            )
        full_prompt = (
            prompt
            + "\n\nINPUT JSON:\n"
            + json.dumps(payload, ensure_ascii=False)
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
            "--max-budget-usd",
            str(args.max_budget_usd),
        ]
        cli_environment = dict(os.environ)
        if args.auth_mode == "subscription":
            cli_environment.pop("ANTHROPIC_API_KEY", None)
        started = time.perf_counter()
        completed = None
        attempt_count = 0
        for attempt_count in range(1, 3):
            completed = subprocess.run(
                command,
                input=full_prompt,
                text=True,
                capture_output=True,
                timeout=args.timeout,
                check=False,
                env=cli_environment,
            )
            if completed.returncode == 0:
                break
        latency = time.perf_counter() - started
        if completed is None or completed.returncode != 0:
            stderr_tail = completed.stderr[-1000:] if completed else ""
            stdout_tail = completed.stdout[-2000:] if completed else ""
            raise RuntimeError(
                f"{qid}: Claude CLI failed after {attempt_count} attempts "
                f"({completed.returncode if completed else 'no result'}): "
                f"stderr={stderr_tail!r}; stdout={stdout_tail!r}"
            )
        result, metadata = parse_cli_output(completed.stdout)
        normalize_review_membership(result, revisions[qid])
        validate_review(result, packet, revisions[qid])
        return {
            "question_id": qid,
            "packet_sha256": common.payload_sha256(packet),
            "revision_sha256": common.payload_sha256(revisions[qid]),
            "prior_group_review_sha256": (
                common.payload_sha256(prior_group_reviews[qid])
                if qid in prior_group_reviews
                else None
            ),
            "model_payload_profile": args.payload_profile,
            "model_payload_sha256": common.payload_sha256(payload),
            "prompt_sha256": common.sha256(PROMPT),
            "review": result,
            "verification": {
                "provider": "Anthropic Claude CLI",
                "request_model": args.model,
                "effort": args.effort,
                "auth_mode": args.auth_mode,
                "max_budget_usd": args.max_budget_usd,
                "temperature": "provider_managed_not_sent",
                "latency_seconds": latency,
                "attempt_count": attempt_count,
                **metadata,
            },
        }

    rows = common.run_parallel(
        items=packets,
        worker=worker,
        key=lambda row: str(row["question_id"]),
        output=output_path,
        workers=args.workers,
        resume=args.resume or reuse_clean_from_path is not None,
    )
    newly_verified = [
        row for row in rows if not row.get("reuse", {}).get("reused")
    ]
    final_reused_question_ids = sorted(
        row["question_id"]
        for row in rows
        if row.get("reuse", {}).get("reused")
    )
    common.write_json(
        output_path.with_name(output_path.stem + "_manifest.json"),
        {
            "stage": "Model B group-level reference verification",
            "question_count": len(rows),
            "provider": "Anthropic Claude CLI",
            "model": args.model,
            "effort": args.effort,
            "auth_mode": args.auth_mode,
            "max_budget_usd_per_question": args.max_budget_usd,
            "temperature": "provider_managed_not_sent",
            "payload_profile": args.payload_profile,
            "prompt_sha256": common.sha256(PROMPT),
            "packets_file": (
                str(packets_path.relative_to(common.ROOT))
                if packets_path.is_relative_to(common.ROOT)
                else str(packets_path)
            ),
            "packets_sha256": common.sha256(packets_path),
            "revisions_sha256": common.sha256(revisions_path),
            "prior_group_reviews_sha256": (
                common.sha256(prior_group_reviews_path)
                if prior_group_reviews_path
                else None
            ),
            "reuse_clean_from_sha256": (
                common.sha256(reuse_clean_from_path)
                if reuse_clean_from_path
                else None
            ),
            "reused_question_ids": final_reused_question_ids,
            "reused_question_count": len(final_reused_question_ids),
            "new_cli_call_question_ids": sorted(
                row["question_id"] for row in newly_verified
            ),
            "new_cli_call_question_count": len(newly_verified),
            "output_sha256": common.sha256(output_path),
            "underlying_review_latency_seconds_sum": sum(
                float(row["verification"]["latency_seconds"]) for row in rows
            ),
            "new_cli_call_latency_seconds_sum": sum(
                float(row["verification"]["latency_seconds"])
                for row in newly_verified
            ),
            "underlying_review_reported_cost_usd": sum(
                float(row["verification"].get("total_cost_usd") or 0)
                for row in rows
            ),
            "new_cli_call_reported_cost_usd": sum(
                float(row["verification"].get("total_cost_usd") or 0)
                for row in newly_verified
            ),
        },
    )
    print(json.dumps({"group_reviews": len(rows)}, indent=2))


if __name__ == "__main__":
    main()

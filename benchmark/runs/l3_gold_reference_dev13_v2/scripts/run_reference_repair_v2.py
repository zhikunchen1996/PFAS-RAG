from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import common
import run_reference_group_verification_v2 as verification
import run_reference_revision_v2 as revision


PROMPT = common.PACKAGE / "prompts/reference_repair_v2.txt"
ECHOED_INPUT_KEYS = {
    "reference_construction_packet",
    "frozen_task_components",
    "previous_model_a_draft",
    "previous_model_b_review",
    "current_revised_claim_ledger",
    "current_model_b_group_review",
}


def remove_echoed_input_fields(result: dict[str, Any]) -> None:
    for key in ECHOED_INPUT_KEYS:
        result.pop(key, None)


def extract_replacement_ledger(result: dict[str, Any]) -> dict[str, Any]:
    if revision.REQUIRED_REVISION_KEYS <= set(result):
        return result
    candidates = [
        value
        for value in result.values()
        if isinstance(value, dict)
        and revision.REQUIRED_REVISION_KEYS <= set(value)
    ]
    if len(candidates) != 1:
        return result
    return dict(candidates[0])


def normalize_group_locations(result: dict[str, Any]) -> None:
    content = result.get("claim_groups", [])
    constraints = result.get("constraint_groups", [])
    if not isinstance(content, list) or not isinstance(constraints, list):
        return
    misplaced = [
        group
        for group in content
        if isinstance(group, dict)
        and group.get("scoring_role") == "constraint_only"
    ]
    if misplaced:
        existing_constraint_ids = {
            group.get("claim_group_id")
            for group in constraints
            if isinstance(group, dict)
        }
        additions = [
            group
            for group in misplaced
            if group.get("claim_group_id") not in existing_constraint_ids
        ]
        result["claim_groups"] = [
            group for group in content if group not in misplaced
        ]
        result["constraint_groups"] = constraints + additions


def normalize_ontology_labels(result: dict[str, Any]) -> None:
    importance_aliases = {
        "optional": "supplementary",
        "optional_gold": "supplementary",
        "supporting": "supplementary",
        "core_required": "core",
    }
    scoring_role_aliases = {
        "required": "required_content",
        "optional": "optional_content",
        "optional_gold": "optional_content",
        "supporting": "optional_content",
        "supplementary": "optional_content",
        "constraint": "constraint_only",
    }
    for group in result.get("claim_groups", []) + result.get(
        "constraint_groups", []
    ):
        importance = group.get("importance")
        if importance in importance_aliases:
            group["importance"] = importance_aliases[importance]
        elif isinstance(importance, str) and importance not in revision.IMPORTANCE:
            normalized = importance.lower()
            if any(
                token in normalized
                for token in ["optional", "supp", "support"]
            ):
                group["importance"] = "supplementary"
            elif any(token in normalized for token in ["core", "required"]):
                group["importance"] = "core"
        scoring_role = group.get("scoring_role")
        if scoring_role in scoring_role_aliases:
            group["scoring_role"] = scoring_role_aliases[scoring_role]
        elif (
            isinstance(scoring_role, str)
            and scoring_role not in revision.SCORING_ROLE
        ):
            normalized = scoring_role.lower()
            if any(
                token in normalized
                for token in ["optional", "supp", "support"]
            ):
                group["scoring_role"] = "optional_content"
            elif any(token in normalized for token in ["core", "required"]):
                group["scoring_role"] = "required_content"
            elif any(
                token in normalized for token in ["constraint", "boundary"]
            ):
                group["scoring_role"] = "constraint_only"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--revisions", required=True)
    parser.add_argument("--reviews", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument(
        "--packets",
        help="Optional versioned reference-packet JSONL; defaults to V1 packets.",
    )
    parser.add_argument("--model", default="gpt-5.1-2025-11-13")
    parser.add_argument("--reasoning-effort", default="low")
    parser.add_argument("--max-completion-tokens", type=int, default=24000)
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--allow-partial-reviews", action="store_true")
    args = parser.parse_args()

    packets_path = (
        Path(args.packets).expanduser().resolve()
        if args.packets
        else common.PACKETS
    )
    revisions_path = Path(args.revisions).expanduser().resolve()
    reviews_path = Path(args.reviews).expanduser().resolve()
    output = Path(args.out).expanduser().resolve()
    packets = {
        row["question_id"]: row for row in common.read_jsonl(packets_path)
    }
    components = {
        row["question_id"]: row
        for row in common.read_jsonl(revision.TASK_COMPONENTS)
    }
    previous_drafts = {
        row["question_id"]: row["draft"]
        for row in common.read_jsonl(common.DRAFTS)
    }
    previous_reviews = {
        row["question_id"]: row["review"]
        for row in common.read_jsonl(common.REVIEWS)
    }
    current = {
        row["question_id"]: row["revision"]
        for row in common.read_jsonl(revisions_path)
    }
    group_reviews = {
        row["question_id"]: row["review"]
        for row in common.read_jsonl(reviews_path)
    }
    qids = set(packets)
    if not (
        qids
        == set(components)
        == set(previous_drafts)
        == set(previous_reviews)
        == set(current)
    ):
        raise RuntimeError("Repair input question membership differs")
    if args.allow_partial_reviews:
        if not set(group_reviews) <= qids:
            raise RuntimeError("Partial review contains unknown question IDs")
    elif set(group_reviews) != qids:
        raise RuntimeError("Repair requires complete reviews without --allow-partial-reviews")
    reviewed_qids = set(group_reviews)

    prompt = PROMPT.read_text(encoding="utf-8")
    items = [
        {"question_id": qid}
        for qid in packets
        if qid in reviewed_qids
        if not verification.review_is_clean(group_reviews[qid])
    ]
    approved_rows = {
        qid: {
            "question_id": qid,
            "packet_sha256": common.payload_sha256(packets[qid]),
            "task_components_sha256": common.payload_sha256(components[qid]),
            "previous_revision_sha256": common.payload_sha256(current[qid]),
            "previous_group_review_sha256": common.payload_sha256(
                group_reviews[qid]
            ),
            "prompt_sha256": common.sha256(PROMPT),
            "revision": current[qid],
            "generation": {
                "repair_skipped": True,
                "reason": "Model B approved the input revision",
            },
        }
        for qid in packets
        if qid in reviewed_qids
        if verification.review_is_clean(group_reviews[qid])
    }
    if output.exists() and args.resume:
        approved_rows.update(
            {
                row["question_id"]: row
                for row in common.read_jsonl(output)
            }
        )
        items = [
            item
            for item in items
            if item["question_id"] not in approved_rows
        ]

    def worker(item: dict[str, Any]) -> dict[str, Any]:
        qid = item["question_id"]
        payload = {
            "reference_construction_packet": packets[qid],
            "frozen_task_components": components[qid],
            "previous_model_a_draft": previous_drafts[qid],
            "previous_model_b_review": previous_reviews[qid],
            "current_revised_claim_ledger": current[qid],
            "current_model_b_group_review": group_reviews[qid],
        }
        result, metadata = common.call_openai_json(
            system_prompt=prompt,
            payload=payload,
            model=args.model,
            reasoning_effort=args.reasoning_effort,
            max_completion_tokens=args.max_completion_tokens,
        )
        result = extract_replacement_ledger(result)
        remove_echoed_input_fields(result)
        normalize_ontology_labels(result)
        normalize_group_locations(result)
        revision.enrich_exact_spans(result, packets[qid])
        revision.normalize_disposition_targets(result)
        revision.validate_revision(
            result,
            packets[qid],
            components[qid],
            previous_drafts[qid],
        )
        return {
            "question_id": qid,
            "packet_sha256": common.payload_sha256(packets[qid]),
            "task_components_sha256": common.payload_sha256(components[qid]),
            "previous_revision_sha256": common.payload_sha256(current[qid]),
            "previous_group_review_sha256": common.payload_sha256(
                group_reviews[qid]
            ),
            "prompt_sha256": common.sha256(PROMPT),
            "revision": result,
            "generation": metadata,
        }

    if items:
        repaired = common.run_parallel(
            items=items,
            worker=worker,
            key=lambda row: str(row["question_id"]),
            output=output.with_name(output.stem + "_pending.jsonl"),
            workers=args.workers,
            resume=args.resume,
        )
        approved_rows.update({row["question_id"]: row for row in repaired})
    rows = [approved_rows[qid] for qid in packets if qid in approved_rows]
    common.write_jsonl(output, rows)
    pending_path = output.with_name(output.stem + "_pending.jsonl")
    if pending_path.exists():
        pending_path.unlink()
    generated = [
        row for row in rows if not row["generation"].get("repair_skipped")
    ]
    common.write_json(
        output.with_name(output.stem + "_manifest.json"),
        {
            "stage": "Model A targeted claim-ledger repair",
            "packets_file": (
                str(packets_path.relative_to(common.ROOT))
                if packets_path.is_relative_to(common.ROOT)
                else str(packets_path)
            ),
            "packets_sha256": common.sha256(packets_path),
            "question_count": len(rows),
            "repaired_question_count": len(generated),
            "model": args.model,
            "reasoning_effort": args.reasoning_effort,
            "temperature": "provider_default_not_sent",
            "prompt_sha256": common.sha256(PROMPT),
            "input_revisions_sha256": common.sha256(revisions_path),
            "input_reviews_sha256": common.sha256(reviews_path),
            "output_sha256": common.sha256(output),
            "total_tokens": sum(
                int(row["generation"]["total_tokens"]) for row in generated
            ),
            "latency_seconds_sum": sum(
                float(row["generation"]["latency_seconds"]) for row in generated
            ),
            "estimated_cost_usd": sum(
                float(row["generation"]["estimated_cost_usd"])
                for row in generated
            ),
        },
    )
    print(
        json.dumps(
            {
                "references": len(rows),
                "repaired": len(generated),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

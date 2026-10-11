from __future__ import annotations

import argparse
import copy
import json
from typing import Any

import common
import run_reference_drafts as drafts


PROMPT = common.PACKAGE / "prompts/reference_repair_v1.txt"
CANONICAL = (
    common.PACKAGE / "reference_build/revisions/model_a_ledgers_repair1.jsonl"
)
REVIEWS = common.PACKAGE / "reference_build/reviews/model_b_reviews_v1.jsonl"
OUTPUT = common.PACKAGE / "reference_build/revisions/model_a_repairs_v1.jsonl"


def structural_normalize_repair(
    raw: dict[str, Any], packet: dict[str, Any]
) -> tuple[dict[str, Any], list[str]]:
    result = copy.deepcopy(raw)
    changes: list[str] = []
    if set(result) == {"replacement_ledger"} and isinstance(
        result["replacement_ledger"], dict
    ):
        result = result["replacement_ledger"]
        changes.append("unwrapped replacement_ledger")
    if "constraint_groups" not in result:
        result["constraint_groups"] = []
        changes.append("restored empty constraint_groups field")
    misplaced_constraints = [
        group
        for group in result.get("claim_groups", [])
        if group.get("scoring_role") == "constraint_only"
    ]
    if misplaced_constraints:
        result["claim_groups"] = [
            group
            for group in result.get("claim_groups", [])
            if group.get("scoring_role") != "constraint_only"
        ]
        existing_ids = {
            group.get("claim_group_id") for group in result["constraint_groups"]
        }
        result["constraint_groups"].extend(
            group
            for group in misplaced_constraints
            if group.get("claim_group_id") not in existing_ids
        )
        changes.append("moved constraint_only groups to constraint_groups")
    for field in ["claim_groups", "constraint_groups"]:
        deduplicated = []
        seen: dict[str, dict[str, Any]] = {}
        for group in result.get(field, []):
            group_id = str(group.get("claim_group_id", ""))
            if group_id in seen:
                if group != seen[group_id]:
                    raise RuntimeError(
                        f"{packet['question_id']} {group_id}: conflicting duplicate groups"
                    )
                changes.append(f"{group_id}: removed identical duplicate group")
                continue
            seen[group_id] = group
            deduplicated.append(group)
        result[field] = deduplicated
    if result.get("task_components") != packet["task_components"]:
        result["task_components"] = copy.deepcopy(packet["task_components"])
        changes.append("restored frozen task_components exactly")
    evidence = {
        row["evidence_id"]: row for row in packet["approved_source_evidence"]
    }
    groups = list(result.get("claim_groups", [])) + list(
        result.get("constraint_groups", [])
    )
    empty_group_ids = {
        str(group.get("claim_group_id", ""))
        for group in groups
        if not group.get("evidence_ids")
    }
    if empty_group_ids:
        result["claim_groups"] = [
            group
            for group in result.get("claim_groups", [])
            if group.get("claim_group_id") not in empty_group_ids
        ]
        result["constraint_groups"] = [
            group
            for group in result.get("constraint_groups", [])
            if group.get("claim_group_id") not in empty_group_ids
        ]
        result["reference_answer_claim_map"] = [
            row
            for row in result.get("reference_answer_claim_map", [])
            if row.get("claim_group_id") not in empty_group_ids
        ]
        for group_id in sorted(empty_group_ids):
            changes.append(f"{group_id}: deleted group without evidence links")
        groups = list(result.get("claim_groups", [])) + list(
            result.get("constraint_groups", [])
        )
    for group in groups:
        group_id = str(group.get("claim_group_id", ""))
        if group.get("numeric_required") is False and group.get(
            "accepted_numeric_equivalents"
        ):
            group["accepted_numeric_equivalents"] = []
            changes.append(f"{group_id}: cleared nonnumeric equivalents")
        for span in group.get("exact_spans", []):
            evidence_id = str(span.get("evidence_id", ""))
            if evidence_id not in evidence:
                continue
            approved = [evidence[evidence_id]["exact_evidence_span"]] + list(
                evidence[evidence_id].get("unit_exact_spans", [])
            )
            if span.get("exact_evidence_span") not in approved:
                span["exact_evidence_span"] = approved[0]
                changes.append(
                    f"{group_id}: restored approved verbatim span for {evidence_id}"
                )
        if not group.get("exact_spans") and group.get("evidence_ids"):
            evidence_id = str(group["evidence_ids"][0])
            if evidence_id in evidence:
                group["exact_spans"] = [
                    {
                        "evidence_id": evidence_id,
                        "exact_evidence_span": evidence[evidence_id][
                            "exact_evidence_span"
                        ],
                        "supports": str(group.get("central_proposition", "")),
                    }
                ]
                changes.append(
                    f"{group_id}: restored linked approved evidence span"
                )
    final_group_ids = {
        str(group.get("claim_group_id", "")) for group in groups
    }
    source_targets: dict[str, set[str]] = {}
    constraint_ids = {
        str(group.get("claim_group_id", ""))
        for group in result.get("constraint_groups", [])
    }
    for group in groups:
        group_id = str(group.get("claim_group_id", ""))
        for atomic_id in group.get("source_atomic_claim_ids", []):
            source_targets.setdefault(str(atomic_id), set()).add(group_id)
    for row in result.get("atomic_claim_dispositions", []):
        atomic_id = str(row.get("atomic_claim_id", ""))
        targets = sorted(source_targets.get(atomic_id, set()) & final_group_ids)
        if row.get("target_claim_group_ids") != targets:
            row["target_claim_group_ids"] = targets
            changes.append(f"{atomic_id}: normalized target group IDs")
        if not targets:
            action = "deleted"
        elif all(target in constraint_ids for target in targets):
            action = "constraint_only"
        elif len(targets) > 1:
            action = "merged"
        else:
            action = "retained"
        if row.get("action") != action:
            row["action"] = action
            changes.append(f"{atomic_id}: normalized action to {action}")
    return result, changes


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--limit", type=int)
    args = parser.parse_args()

    packets = {
        row["question_id"]: row for row in common.read_jsonl(common.REFERENCE_PACKETS)
    }
    ledgers = {
        row["question_id"]: row for row in common.read_jsonl(CANONICAL)
    }
    reviews = {
        row["question_id"]: row for row in common.read_jsonl(REVIEWS)
    }
    qids = [
        row["question_id"]
        for row in common.read_jsonl(common.REFERENCE_PACKETS)
        if reviews[row["question_id"]]["verdict"] == "repair_required"
    ]
    items = [
        {
            "question_id": qid,
            "reference_packet": packets[qid],
            "current_ledger": ledgers[qid]["draft_ledger"],
            "model_b_review": reviews[qid],
        }
        for qid in qids
    ]
    if args.limit:
        items = items[: args.limit]
    prompt = PROMPT.read_text(encoding="utf-8")

    def worker(item: dict[str, Any]) -> dict[str, Any]:
        result, metadata = common.call_openai_json(
            system_prompt=prompt,
            payload=item,
            max_completion_tokens=20000,
        )
        result, structural_changes = structural_normalize_repair(
            result, item["reference_packet"]
        )
        try:
            drafts.validate(result, item["reference_packet"])
        except Exception:
            quarantine = (
                common.PACKAGE
                / "reference_build/revisions/quarantine_repair1"
                / f"{item['question_id']}__{metadata['response_id']}.json"
            )
            common.write_json(
                quarantine,
                {
                    "question_id": item["question_id"],
                    "source_ledger_sha256": common.payload_sha256(
                        item["current_ledger"]
                    ),
                    "review_sha256": common.payload_sha256(item["model_b_review"]),
                    "raw_result": result,
                    "generation": metadata,
                    "analytical_status": "quarantined_schema_invalid_repair",
                },
            )
            raise
        return {
            "question_id": item["question_id"],
            "reference_packet_sha256": common.payload_sha256(
                item["reference_packet"]
            ),
            "source_ledger_sha256": common.payload_sha256(item["current_ledger"]),
            "model_b_review_sha256": common.payload_sha256(item["model_b_review"]),
            "repair_prompt_sha256": common.sha256(PROMPT),
            "structural_normalizations": structural_changes,
            "repaired_ledger": result,
            "generation": metadata,
        }

    rows = common.run_parallel(
        items=items,
        worker=worker,
        key=lambda row: str(row["question_id"]),
        output=OUTPUT,
        workers=args.workers,
        resume=args.resume,
    )
    common.write_json(
        common.PACKAGE / "reference_build/revisions/repair_v1_run_manifest.json",
        {
            "stage": "issue-targeted GPT-5.1 repair after Claude verification",
            "repair_question_count": len(rows),
            "model": "gpt-5.1",
            "required_response_model": common.EXPECTED_RESPONSE_MODEL,
            "reasoning_effort": "low",
            "prompt_sha256": common.sha256(PROMPT),
            "source_ledgers_sha256": common.sha256(CANONICAL),
            "model_b_reviews_sha256": common.sha256(REVIEWS),
            "output_sha256": common.sha256(OUTPUT),
            "total_tokens": sum(row["generation"]["total_tokens"] for row in rows),
            "estimated_cost_usd": sum(
                row["generation"]["estimated_cost_usd"] for row in rows
            ),
            "latency_seconds_sum": sum(
                row["generation"]["latency_seconds"] for row in rows
            ),
            "candidate_test40_inputs_used": False,
        },
    )
    print(json.dumps({"repairs": len(rows)}, indent=2))


if __name__ == "__main__":
    main()

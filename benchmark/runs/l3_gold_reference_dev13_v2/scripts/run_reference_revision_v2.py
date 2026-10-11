from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import common


PROMPT = common.PACKAGE / "prompts/reference_revision_v2.txt"
TASK_COMPONENTS = (
    common.PACKAGE / "reference_build/inputs/task_components_dev13.jsonl"
)
INITIAL_TASK_COMPONENTS = (
    common.PACKAGE
    / "reference_build/inputs/task_components_dev13_pre_repair2.jsonl"
)
OUTPUT = (
    common.PACKAGE
    / "reference_build/revisions/model_a_revisions_v2.jsonl"
)

IMPORTANCE = {"core", "supplementary"}
FUNCTION = {
    "affirmative",
    "limitation",
    "negative_finding",
    "boundary_constraint",
}
SCORING_ROLE = {"required_content", "optional_content", "constraint_only"}
REQUIRED_REVISION_KEYS = {
    "question_id",
    "answerability",
    "answerability_rationale",
    "task_components",
    "claim_groups",
    "constraint_groups",
    "atomic_claim_dispositions",
    "reference_answer",
    "reference_answer_claim_map",
    "unresolved_or_unsupported",
    "boundary_check",
}


def validate_exact_spans(
    *,
    qid: str,
    group: dict[str, Any],
    evidence_by_id: dict[str, dict[str, Any]],
    allow_empty: bool = False,
) -> None:
    evidence_ids = set(group.get("evidence_ids", []))
    evidence_id_list = group.get("evidence_ids", [])
    if len(evidence_id_list) != len(evidence_ids):
        raise RuntimeError(
            f"{qid} {group.get('claim_group_id')}: duplicate evidence IDs"
        )
    if not evidence_ids and allow_empty:
        if group.get("exact_spans"):
            raise RuntimeError(
                f"{qid} {group.get('claim_group_id')}: spans exist without evidence"
            )
        return
    if not evidence_ids or not evidence_ids <= set(evidence_by_id):
        raise RuntimeError(f"{qid} {group.get('claim_group_id')}: invalid evidence IDs")
    spans = group.get("exact_spans")
    if not isinstance(spans, list) or not spans:
        raise RuntimeError(f"{qid} {group.get('claim_group_id')}: missing exact spans")
    span_ids = set()
    for span in spans:
        evidence_id = str(span.get("evidence_id", ""))
        if evidence_id not in evidence_by_id:
            raise RuntimeError(
                f"{qid} {group.get('claim_group_id')}: unknown span evidence"
            )
        if span.get("exact_evidence_span") != evidence_by_id[evidence_id].get(
            "exact_evidence_span"
        ):
            raise RuntimeError(
                f"{qid} {group.get('claim_group_id')}: evidence span is not exact"
            )
        span_ids.add(evidence_id)
    if len(spans) != len(span_ids):
        raise RuntimeError(
            f"{qid} {group.get('claim_group_id')}: duplicate exact spans"
        )
    if span_ids != evidence_ids:
        raise RuntimeError(
            f"{qid} {group.get('claim_group_id')}: span/evidence membership differs"
        )


def enrich_exact_spans(
    result: dict[str, Any],
    packet: dict[str, Any],
) -> None:
    evidence_by_id = {
        row["evidence_id"]: row for row in packet["gold_evidence"]
    }
    for group in result.get("claim_groups", []) + result.get(
        "constraint_groups", []
    ):
        support_map_raw = group.pop("evidence_support_map", [])
        if isinstance(support_map_raw, dict):
            support_map = [
                {"evidence_id": evidence_id, "supports": supports}
                for evidence_id, supports in support_map_raw.items()
            ]
        elif isinstance(support_map_raw, list):
            support_map = [row for row in support_map_raw if isinstance(row, dict)]
        else:
            support_map = []
        support_by_id = {
            str(row.get("evidence_id", "")): str(row.get("supports", "")).strip()
            for row in support_map
            if str(row.get("evidence_id", "")).strip()
        }
        evidence_ids = [str(value) for value in group.get("evidence_ids", [])]
        if (
            not evidence_ids
            and group.get("scoring_role") == "constraint_only"
        ):
            group["exact_spans"] = []
            continue
        if not evidence_ids or not set(evidence_ids) <= set(evidence_by_id):
            raise RuntimeError(
                f"{packet['question_id']} {group.get('claim_group_id')}: "
                "invalid evidence IDs"
            )
        group["exact_spans"] = [
            {
                "evidence_id": evidence_id,
                "exact_evidence_span": evidence_by_id[evidence_id][
                    "exact_evidence_span"
                ],
                # The evidence list is normative. If the model omits a matching
                # support-map entry, retain the exact audited span rather than
                # inventing or accepting a mismatched evidence summary.
                "supports": support_by_id.get(evidence_id)
                or evidence_by_id[evidence_id]["exact_evidence_span"],
            }
            for evidence_id in evidence_ids
        ]


def normalize_disposition_targets(result: dict[str, Any]) -> None:
    source_targets: dict[str, set[str]] = {}
    for group in result.get("claim_groups", []) + result.get(
        "constraint_groups", []
    ):
        group_id = str(group.get("claim_group_id", ""))
        for source_id in group.get("source_atomic_claim_ids", []):
            source_targets.setdefault(str(source_id), set()).add(group_id)
    for row in result.get("atomic_claim_dispositions", []):
        source_id = str(row.get("atomic_claim_id", ""))
        normalized = sorted(source_targets.get(source_id, set()))
        previous = sorted(str(value) for value in row.get("target_claim_group_ids", []))
        if previous != normalized:
            note = (
                f"Disposition targets normalized from {previous} to {normalized} "
                "using final source_atomic_claim_ids."
            )
            rationale = str(row.get("rationale", "")).strip()
            row["rationale"] = f"{rationale} {note}".strip()
            row["target_claim_group_ids"] = normalized
        if not normalized:
            row["action"] = "deleted"
        elif len(normalized) > 1:
            row["action"] = "revised"


def validate_revision(
    result: dict[str, Any],
    packet: dict[str, Any],
    components: dict[str, Any],
    previous_draft: dict[str, Any],
) -> None:
    qid = packet["question_id"]
    if set(result) != REQUIRED_REVISION_KEYS:
        raise RuntimeError(
            f"{qid}: revision keys differ: "
            f"{sorted(set(result) ^ REQUIRED_REVISION_KEYS)}"
        )
    if result["question_id"] != qid:
        raise RuntimeError(f"{qid}: returned question ID differs")
    if result["task_components"] != components["task_components"]:
        raise RuntimeError(f"{qid}: frozen task components changed")

    component_ids = {
        row["task_component_id"] for row in components["task_components"]
    }
    if len(component_ids) != len(components["task_components"]):
        raise RuntimeError(f"{qid}: duplicate task component ID")
    evidence_by_id = {
        row["evidence_id"]: row for row in packet["gold_evidence"]
    }
    previous_claim_ids = {
        row["claim_id"] for row in previous_draft["claims"]
    }

    group_ids: set[str] = set()
    core_components: set[str] = set()
    core_count_by_component = {
        component_id: 0 for component_id in component_ids
    }
    source_targets: dict[str, set[str]] = {
        claim_id: set() for claim_id in previous_claim_ids
    }
    for group in result["claim_groups"]:
        group_id = str(group.get("claim_group_id", ""))
        if not group_id or group_id in group_ids:
            raise RuntimeError(f"{qid}: invalid or duplicate claim group ID")
        group_ids.add(group_id)
        if group.get("task_component_id") not in component_ids:
            raise RuntimeError(f"{qid} {group_id}: invalid task component")
        if group.get("importance") not in IMPORTANCE:
            raise RuntimeError(f"{qid} {group_id}: invalid importance")
        if group.get("function") not in FUNCTION:
            raise RuntimeError(f"{qid} {group_id}: invalid function")
        if group.get("scoring_role") not in SCORING_ROLE - {"constraint_only"}:
            raise RuntimeError(f"{qid} {group_id}: invalid content scoring role")
        if (
            group["importance"] == "core"
            and group["scoring_role"] == "required_content"
        ):
            core_components.add(group["task_component_id"])
            core_count_by_component[group["task_component_id"]] += 1
        for field in [
            "canonical_proposition",
            "central_proposition",
            "full_rule",
            "partial_rule",
            "contradiction_rule",
        ]:
            if not str(group.get(field, "")).strip():
                raise RuntimeError(f"{qid} {group_id}: empty {field}")
        if not isinstance(group.get("material_qualifiers"), list):
            raise RuntimeError(f"{qid} {group_id}: invalid material qualifiers")
        source_ids = set(group.get("source_atomic_claim_ids", []))
        if not source_ids <= previous_claim_ids:
            raise RuntimeError(f"{qid} {group_id}: unknown prior atomic claim")
        for source_id in source_ids:
            source_targets[source_id].add(group_id)
        numeric_required = group.get("numeric_required")
        if not isinstance(numeric_required, bool):
            raise RuntimeError(f"{qid} {group_id}: invalid numeric_required")
        equivalents = group.get("accepted_numeric_equivalents")
        if not isinstance(equivalents, list):
            raise RuntimeError(f"{qid} {group_id}: invalid numeric equivalents")
        if not numeric_required and equivalents:
            raise RuntimeError(
                f"{qid} {group_id}: nonnumeric claim has numeric equivalents"
            )
        validate_exact_spans(
            qid=qid,
            group=group,
            evidence_by_id=evidence_by_id,
        )
    if core_components != component_ids:
        missing = sorted(component_ids - core_components)
        raise RuntimeError(f"{qid}: components lack core required groups: {missing}")
    excessive = {
        component_id: count
        for component_id, count in core_count_by_component.items()
        if count > 3
    }
    if excessive:
        raise RuntimeError(f"{qid}: too many core groups per component: {excessive}")

    constraint_ids: set[str] = set()
    for group in result["constraint_groups"]:
        group_id = str(group.get("claim_group_id", ""))
        if not group_id or group_id in group_ids or group_id in constraint_ids:
            raise RuntimeError(f"{qid}: invalid or duplicate constraint group ID")
        constraint_ids.add(group_id)
        if group.get("task_component_id") not in component_ids:
            raise RuntimeError(f"{qid} {group_id}: invalid task component")
        if group.get("function") != "boundary_constraint":
            raise RuntimeError(f"{qid} {group_id}: invalid constraint function")
        if group.get("scoring_role") != "constraint_only":
            raise RuntimeError(f"{qid} {group_id}: invalid constraint role")
        if not str(group.get("violation_rule", "")).strip():
            raise RuntimeError(f"{qid} {group_id}: empty violation rule")
        source_ids = set(group.get("source_atomic_claim_ids", []))
        if not source_ids <= previous_claim_ids:
            raise RuntimeError(f"{qid} {group_id}: unknown prior atomic claim")
        for source_id in source_ids:
            source_targets[source_id].add(group_id)
        validate_exact_spans(
            qid=qid,
            group=group,
            evidence_by_id=evidence_by_id,
            allow_empty=True,
        )

    all_target_ids = group_ids | constraint_ids
    dispositions = result["atomic_claim_dispositions"]
    disposition_ids = [row.get("atomic_claim_id") for row in dispositions]
    if set(disposition_ids) != previous_claim_ids or len(disposition_ids) != len(
        previous_claim_ids
    ):
        raise RuntimeError(f"{qid}: prior atomic-claim disposition is incomplete")
    for row in dispositions:
        action = row.get("action")
        targets = set(row.get("target_claim_group_ids", []))
        if action not in {"mapped", "revised", "merged", "deleted"}:
            raise RuntimeError(f"{qid}: invalid atomic disposition action")
        if not targets <= all_target_ids:
            raise RuntimeError(f"{qid}: disposition points to unknown group")
        if action == "deleted" and targets:
            raise RuntimeError(f"{qid}: deleted claim has target groups")
        if action != "deleted" and not targets:
            raise RuntimeError(f"{qid}: non-deleted claim lacks a target group")
        source_id = str(row["atomic_claim_id"])
        if targets != source_targets[source_id]:
            raise RuntimeError(
                f"{qid} {source_id}: disposition/source-group mapping differs"
            )

    mapped_ids = set()
    for row in result["reference_answer_claim_map"]:
        ids = set(row.get("claim_group_ids", []))
        if not ids or not ids <= all_target_ids:
            raise RuntimeError(f"{qid}: prose map points to unknown group")
        mapped_ids.update(ids)
    if not str(result.get("reference_answer", "")).strip():
        raise RuntimeError(f"{qid}: reference prose is empty")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="gpt-5.1-2025-11-13")
    parser.add_argument("--reasoning-effort", default="medium")
    parser.add_argument("--max-completion-tokens", type=int, default=20000)
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--limit", type=int)
    args = parser.parse_args()

    required = [
        common.PACKETS,
        common.DRAFTS,
        common.REVIEWS,
        TASK_COMPONENTS,
        PROMPT,
    ]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise RuntimeError(f"Missing revision inputs: {missing}")

    packets = common.read_jsonl(common.PACKETS)
    components = {
        row["question_id"]: row for row in common.read_jsonl(TASK_COMPONENTS)
    }
    drafts = {
        row["question_id"]: row["draft"]
        for row in common.read_jsonl(common.DRAFTS)
    }
    reviews = {
        row["question_id"]: row["review"]
        for row in common.read_jsonl(common.REVIEWS)
    }
    qids = {row["question_id"] for row in packets}
    if set(components) != qids or set(drafts) != qids or set(reviews) != qids:
        raise RuntimeError("Revision input question membership differs")
    if args.limit is not None:
        packets = packets[: args.limit]
    prompt = PROMPT.read_text(encoding="utf-8")

    def worker(packet: dict[str, Any]) -> dict[str, Any]:
        qid = packet["question_id"]
        payload = {
            "reference_construction_packet": packet,
            "frozen_task_components": components[qid],
            "previous_model_a_draft": drafts[qid],
            "previous_model_b_review": reviews[qid],
        }
        result, metadata = common.call_openai_json(
            system_prompt=prompt,
            payload=payload,
            model=args.model,
            reasoning_effort=args.reasoning_effort,
            max_completion_tokens=args.max_completion_tokens,
        )
        enrich_exact_spans(result, packet)
        normalize_disposition_targets(result)
        validate_revision(
            result,
            packet,
            components[qid],
            drafts[qid],
        )
        return {
            "question_id": qid,
            "packet_sha256": common.payload_sha256(packet),
            "task_components_sha256": common.payload_sha256(components[qid]),
            "previous_draft_sha256": common.payload_sha256(drafts[qid]),
            "previous_review_sha256": common.payload_sha256(reviews[qid]),
            "prompt_sha256": common.sha256(PROMPT),
            "revision": result,
            "generation": metadata,
        }

    rows = common.run_parallel(
        items=packets,
        worker=worker,
        key=lambda row: str(row["question_id"]),
        output=OUTPUT,
        workers=args.workers,
        resume=args.resume,
    )
    common.write_json(
        OUTPUT.parent / "run_manifest_v2.json",
        {
            "stage": "Model A orthogonal claim-ledger revision",
            "question_count": len(rows),
            "model": args.model,
            "reasoning_effort": args.reasoning_effort,
            "temperature": "provider_default_not_sent",
            "prompt_sha256": common.sha256(PROMPT),
            "task_components_sha256": common.sha256(TASK_COMPONENTS),
            "packets_sha256": common.sha256(common.PACKETS),
            "previous_drafts_sha256": common.sha256(common.DRAFTS),
            "previous_reviews_sha256": common.sha256(common.REVIEWS),
            "output_sha256": common.sha256(OUTPUT),
            "total_tokens": sum(
                int(row["generation"]["total_tokens"]) for row in rows
            ),
            "latency_seconds_sum": sum(
                float(row["generation"]["latency_seconds"]) for row in rows
            ),
            "estimated_cost_usd": sum(
                float(row["generation"]["estimated_cost_usd"]) for row in rows
            ),
        },
    )
    print(json.dumps({"revisions": len(rows)}, indent=2))


if __name__ == "__main__":
    main()

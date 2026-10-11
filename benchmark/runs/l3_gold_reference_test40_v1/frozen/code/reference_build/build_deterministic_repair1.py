from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any

import common
import run_reference_drafts as drafts


REVISIONS = (
    common.PACKAGE / "reference_build/revisions/deterministic_repair1.jsonl"
)
CANONICAL = (
    common.PACKAGE / "reference_build/revisions/model_a_ledgers_repair1.jsonl"
)


def structural_normalize(
    raw: dict[str, Any], packet: dict[str, Any]
) -> tuple[dict[str, Any], list[str]]:
    result = copy.deepcopy(raw)
    changes: list[str] = []
    qid = packet["question_id"]
    evidence = {
        row["evidence_id"]: row for row in packet["approved_source_evidence"]
    }

    if result.get("task_components") != packet["task_components"]:
        result["task_components"] = copy.deepcopy(packet["task_components"])
        changes.append("restored frozen task_components exactly")

    groups = list(result.get("claim_groups", [])) + list(
        result.get("constraint_groups", [])
    )
    for group in groups:
        group_id = str(group.get("claim_group_id", ""))
        group_evidence_ids = [str(value) for value in group.get("evidence_ids", [])]
        span_evidence_ids = [
            str(span.get("evidence_id", ""))
            for span in group.get("exact_spans", [])
            if str(span.get("evidence_id", "")) in evidence
        ]
        merged_evidence_ids = list(dict.fromkeys(group_evidence_ids + span_evidence_ids))
        if merged_evidence_ids != group_evidence_ids:
            group["evidence_ids"] = merged_evidence_ids
            changes.append(f"{group_id}: added valid span evidence IDs to group links")
        if group.get("numeric_required") is False and group.get(
            "accepted_numeric_equivalents"
        ):
            group["accepted_numeric_equivalents"] = []
            changes.append(f"{group_id}: cleared nonnumeric equivalents")
        for span in group.get("exact_spans", []):
            evidence_id = str(span.get("evidence_id", ""))
            if evidence_id not in evidence:
                continue
            exact = evidence[evidence_id]["exact_evidence_span"]
            if span.get("exact_evidence_span") != exact:
                span["exact_evidence_span"] = exact
                changes.append(
                    f"{group_id}: restored verbatim span for {evidence_id}"
                )

    targets: dict[str, set[str]] = {}
    constraint_ids = {
        str(group.get("claim_group_id", ""))
        for group in result.get("constraint_groups", [])
    }
    for group in groups:
        group_id = str(group.get("claim_group_id", ""))
        for atomic_id in group.get("source_atomic_claim_ids", []):
            targets.setdefault(str(atomic_id), set()).add(group_id)
    for row in result.get("atomic_claim_dispositions", []):
        atomic_id = str(row.get("atomic_claim_id", ""))
        normalized_targets = sorted(targets.get(atomic_id, set()))
        if row.get("target_claim_group_ids") != normalized_targets:
            row["target_claim_group_ids"] = normalized_targets
            changes.append(f"{atomic_id}: normalized target group IDs")
        if not normalized_targets:
            normalized_action = "deleted"
        elif all(target in constraint_ids for target in normalized_targets):
            normalized_action = "constraint_only"
        elif len(normalized_targets) > 1:
            normalized_action = "merged"
        else:
            normalized_action = "retained"
        if row.get("action") != normalized_action:
            row["action"] = normalized_action
            changes.append(f"{atomic_id}: normalized action to {normalized_action}")

    if not changes:
        raise RuntimeError(f"{qid}: deterministic repair made no changes")
    drafts.validate(result, packet)
    return result, changes


def main() -> None:
    packets = {
        row["question_id"]: row for row in common.read_jsonl(common.REFERENCE_PACKETS)
    }
    valid = {
        row["question_id"]: row for row in common.read_jsonl(common.DRAFTS)
    }
    quarantine_dir = common.PACKAGE / "reference_build/drafts/quarantine"
    quarantined: dict[str, tuple[Path, dict[str, Any]]] = {}
    for path in sorted(quarantine_dir.glob("*.json")):
        row = json.loads(path.read_text(encoding="utf-8"))
        qid = row["question_id"]
        if qid in quarantined:
            raise RuntimeError(f"{qid}: multiple quarantine drafts require review")
        quarantined[qid] = (path, row)

    expected_failed = set(packets) - set(valid)
    if set(quarantined) != expected_failed:
        raise RuntimeError(
            "Quarantine membership differs from missing draft membership: "
            f"missing={sorted(expected_failed - set(quarantined))}, "
            f"extra={sorted(set(quarantined) - expected_failed)}"
        )

    repairs = []
    for qid in sorted(quarantined):
        path, row = quarantined[qid]
        repaired, changes = structural_normalize(row["raw_result"], packets[qid])
        repairs.append(
            {
                "question_id": qid,
                "reference_packet_sha256": common.payload_sha256(packets[qid]),
                "source_quarantine_file": str(path.relative_to(common.ROOT)),
                "source_response_id": row["generation"]["response_id"],
                "source_prompt_sha256": row["prompt_sha256"],
                "repair_type": "deterministic_structural_only",
                "changes": changes,
                "draft_ledger": repaired,
                "generation": row["generation"],
            }
        )
    common.write_jsonl(REVISIONS, repairs)

    combined = dict(valid)
    combined.update({row["question_id"]: row for row in repairs})
    if set(combined) != set(packets):
        raise RuntimeError("Canonical repaired draft membership is incomplete")
    ordered = [combined[row["question_id"]] for row in common.read_jsonl(common.REFERENCE_PACKETS)]
    common.write_jsonl(CANONICAL, ordered)
    manifest = {
        "stage": "deterministic structural repair of quarantined Model A drafts",
        "valid_original_count": len(valid),
        "repaired_count": len(repairs),
        "canonical_count": len(ordered),
        "scientific_content_regenerated": False,
        "allowed_repairs": [
            "restore exact frozen task components",
            "restore complete verbatim approved evidence span",
            "add valid span evidence IDs to the same group evidence links",
            "clear numeric equivalents when numeric_required is false",
            "normalize atomic target IDs and structural action from group links",
        ],
        "source_drafts_sha256": common.sha256(common.DRAFTS),
        "repairs_sha256": common.sha256(REVISIONS),
        "canonical_sha256": common.sha256(CANONICAL),
        "candidate_test40_inputs_used": False,
    }
    common.write_json(
        common.PACKAGE / "reference_build/revisions/repair1_manifest.json",
        manifest,
    )
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()

from __future__ import annotations

import json
from pathlib import Path

import common
import run_reference_revision_v2 as revision


def main() -> None:
    errors: list[str] = []
    protocol = json.loads(
        (common.PACKAGE / "protocol.json").read_text(encoding="utf-8")
    )
    if protocol["protocol_id"] != "l3_gold_reference_dev13_v2":
        errors.append("Protocol ID is not the V2 L3 design")
    if protocol["scope"] != "Dev13 only":
        errors.append("Protocol scope is not Dev13 only")
    required = [
        common.QUESTIONS,
        common.GOLD,
        common.BOUNDARIES,
        common.AUTHOR_REVIEW,
        common.GOLD_AUTHOR_REGISTER,
        common.PACKAGE / "prompts/reference_draft_v1.txt",
        common.PACKAGE / "prompts/reference_claim_verification_v1.txt",
        common.PACKAGE / "prompts/l3_gold_referenced_judge_v1.txt",
        revision.TASK_COMPONENTS,
        common.PACKAGE / "prompts/reference_revision_v2.txt",
        common.PACKAGE / "prompts/reference_group_verification_v2.txt",
        common.PACKAGE / "prompts/reference_repair_v2.txt",
        common.PACKAGE / "prompts/l3_gold_referenced_judge_v2.txt",
    ]
    errors.extend(
        f"Missing required file: {path}" for path in required if not path.exists()
    )
    if common.PACKETS.exists():
        packets = common.read_jsonl(common.PACKETS)
        if len(packets) != 13:
            errors.append(f"Expected 13 packets, found {len(packets)}")
        forbidden_keys = {
            "direct_answer",
            "rag_answer",
            "candidate_answer",
            "retrieved_context",
            "prior_judge_outcome",
        }
        for packet in packets:
            serialized = json.dumps(packet).lower()
            for key in forbidden_keys:
                if f'"{key}"' in serialized:
                    errors.append(
                        f"{packet['question_id']}: forbidden input {key}"
                    )
    if revision.TASK_COMPONENTS.exists():
        components = common.read_jsonl(revision.TASK_COMPONENTS)
        if len(components) != 13:
            errors.append(f"Expected 13 task-component rows, found {len(components)}")
        component_qids = [row.get("question_id") for row in components]
        if len(set(component_qids)) != len(component_qids):
            errors.append("Duplicate question ID in task components")
        for row in components:
            ids = [
                component.get("task_component_id")
                for component in row.get("task_components", [])
            ]
            if not ids or len(ids) != len(set(ids)):
                errors.append(
                    f"{row.get('question_id')}: invalid task-component membership"
                )
    if revision.OUTPUT.exists():
        revisions = common.read_jsonl(revision.OUTPUT)
        if len(revisions) != 13:
            errors.append(f"Expected 13 V2 revisions, found {len(revisions)}")
        packet_by_qid = {
            row["question_id"]: row for row in common.read_jsonl(common.PACKETS)
        }
        component_by_qid = {
            row["question_id"]: row
            for row in common.read_jsonl(revision.INITIAL_TASK_COMPONENTS)
        }
        draft_by_qid = {
            row["question_id"]: row["draft"]
            for row in common.read_jsonl(common.DRAFTS)
        }
        for row in revisions:
            qid = row["question_id"]
            try:
                revision.validate_revision(
                    row["revision"],
                    packet_by_qid[qid],
                    component_by_qid[qid],
                    draft_by_qid[qid],
                )
            except Exception as exc:
                errors.append(f"{qid}: invalid V2 revision: {exc}")
    frozen = common.PACKAGE / "frozen/reference_answers.jsonl"
    manifest = common.PACKAGE / "frozen/freeze_manifest.json"
    if frozen.exists() != manifest.exists():
        errors.append("Frozen reference and freeze manifest must coexist")
    if frozen.exists():
        freeze = json.loads(manifest.read_text(encoding="utf-8"))
        if freeze["reference_answers_sha256"] != common.sha256(frozen):
            errors.append("Frozen reference hash mismatch")
        if freeze.get("test40_l3_evaluated") is not False:
            errors.append("Test40 L3 status is not false")
    frozen_v2 = common.PACKAGE / "frozen/reference_claim_ledgers_v2.jsonl"
    manifest_v2 = common.PACKAGE / "frozen/freeze_manifest_v2.json"
    if frozen_v2.exists() != manifest_v2.exists():
        errors.append("V2 frozen ledger and manifest must coexist")
    if frozen_v2.exists():
        freeze_v2 = json.loads(manifest_v2.read_text(encoding="utf-8"))
        if freeze_v2["normative_scoring_source_sha256"] != common.sha256(
            frozen_v2
        ):
            errors.append("V2 frozen ledger hash mismatch")
        if freeze_v2.get("binary_pass_status") != "not_calibrated":
            errors.append("V2 binary pass was calibrated before the Dev stage")
        if freeze_v2.get("test40_l3_evaluated") is not False:
            errors.append("V2 Test40 L3 status is not false")

    report = {
        "protocol_id": "l3_gold_reference_dev13_v2",
        "status": "pass" if not errors else "fail",
        "errors": errors,
        "reference_frozen": frozen_v2.exists(),
        "human_review_ready": (
            common.PACKAGE / "human_review_v2/reference_candidates.jsonl"
        ).exists(),
    }
    common.write_json(common.PACKAGE / "validation_report.json", report)
    print(json.dumps(report, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

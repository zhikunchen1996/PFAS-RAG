from __future__ import annotations

import argparse
import json
import re
from typing import Any

import common


PROMPT = common.PACKAGE / "prompts/reference_ledger_draft_v1.txt"
TOP_LEVEL_KEYS = {
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
ANSWERABILITY = {
    "supported",
    "partially_supported",
    "conflicting_or_heterogeneous",
    "insufficient",
}
IMPORTANCE = {"core", "supplementary"}
FUNCTION = {"affirmative", "limitation", "negative"}
CONTENT_ROLES = {"required_content", "supplementary_content"}
ACTIONS = {"retained", "merged", "constraint_only", "deleted"}


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("–", "-").replace("—", "-")).strip()


def validate_group(
    *,
    group: dict[str, Any],
    qid: str,
    component_ids: set[str],
    evidence: dict[str, dict[str, Any]],
    group_ids: set[str],
    constraint: bool,
) -> None:
    group_id = str(group.get("claim_group_id", ""))
    if not group_id or group_id in group_ids:
        raise RuntimeError(f"{qid}: duplicate or empty claim group ID")
    group_ids.add(group_id)
    if group.get("task_component_id") not in component_ids:
        raise RuntimeError(f"{qid} {group_id}: invalid task component")
    if group.get("importance") not in IMPORTANCE:
        raise RuntimeError(f"{qid} {group_id}: invalid importance")
    if group.get("function") not in FUNCTION:
        raise RuntimeError(f"{qid} {group_id}: invalid function")
    expected_roles = {"constraint_only"} if constraint else CONTENT_ROLES
    if group.get("scoring_role") not in expected_roles:
        raise RuntimeError(f"{qid} {group_id}: invalid scoring role")
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
    evidence_ids = [str(value) for value in group.get("evidence_ids", [])]
    if not evidence_ids or not set(evidence_ids) <= set(evidence):
        raise RuntimeError(f"{qid} {group_id}: invalid evidence IDs")
    if not isinstance(group.get("synthesis_required"), bool):
        raise RuntimeError(f"{qid} {group_id}: invalid synthesis_required")
    if not isinstance(group.get("numeric_required"), bool):
        raise RuntimeError(f"{qid} {group_id}: invalid numeric_required")
    equivalents = group.get("accepted_numeric_equivalents")
    if not isinstance(equivalents, list):
        raise RuntimeError(f"{qid} {group_id}: invalid numeric equivalents")
    if not group["numeric_required"] and equivalents:
        raise RuntimeError(f"{qid} {group_id}: numeric equivalents on nonnumeric group")
    source_ids = group.get("source_atomic_claim_ids")
    if not isinstance(source_ids, list) or not source_ids:
        raise RuntimeError(f"{qid} {group_id}: missing atomic claim links")
    spans = group.get("exact_spans")
    if not isinstance(spans, list) or not spans:
        raise RuntimeError(f"{qid} {group_id}: missing exact spans")
    for span in spans:
        evidence_id = str(span.get("evidence_id", ""))
        quote = str(span.get("exact_evidence_span", "")).strip()
        if evidence_id not in evidence or evidence_id not in evidence_ids:
            raise RuntimeError(f"{qid} {group_id}: invalid span evidence ID")
        if not quote or not str(span.get("supports", "")).strip():
            raise RuntimeError(f"{qid} {group_id}: empty span or support explanation")
        source = evidence[evidence_id]
        searchable = " ".join(
            [source["exact_evidence_span"], source["full_chunk_text"]]
            + list(source.get("unit_exact_spans", []))
        )
        if normalized(quote) not in normalized(searchable):
            raise RuntimeError(f"{qid} {group_id}: quoted span not found in source")


def validate(result: dict[str, Any], packet: dict[str, Any]) -> None:
    qid = packet["question_id"]
    if set(result) != TOP_LEVEL_KEYS:
        raise RuntimeError(f"{qid}: invalid top-level keys")
    if result["question_id"] != qid:
        raise RuntimeError(f"{qid}: question ID changed")
    if result["answerability"] not in ANSWERABILITY:
        raise RuntimeError(f"{qid}: invalid answerability")
    if not str(result["answerability_rationale"]).strip():
        raise RuntimeError(f"{qid}: empty answerability rationale")
    if result["task_components"] != packet["task_components"]:
        raise RuntimeError(f"{qid}: frozen task components changed")
    component_ids = {
        row["task_component_id"] for row in packet["task_components"]
    }
    evidence = {
        row["evidence_id"]: row for row in packet["approved_source_evidence"]
    }
    group_ids: set[str] = set()
    claims = result["claim_groups"]
    constraints = result["constraint_groups"]
    if not isinstance(claims, list) or not claims:
        raise RuntimeError(f"{qid}: no content claim groups")
    if not isinstance(constraints, list):
        raise RuntimeError(f"{qid}: invalid constraint groups")
    for group in claims:
        validate_group(
            group=group,
            qid=qid,
            component_ids=component_ids,
            evidence=evidence,
            group_ids=group_ids,
            constraint=False,
        )
    for group in constraints:
        validate_group(
            group=group,
            qid=qid,
            component_ids=component_ids,
            evidence=evidence,
            group_ids=group_ids,
            constraint=True,
        )

    dispositions = result["atomic_claim_dispositions"]
    if not isinstance(dispositions, list) or not dispositions:
        raise RuntimeError(f"{qid}: no atomic claim dispositions")
    atomic_ids: set[str] = set()
    for row in dispositions:
        atomic_id = str(row.get("atomic_claim_id", ""))
        if not atomic_id or atomic_id in atomic_ids:
            raise RuntimeError(f"{qid}: invalid atomic claim ID")
        atomic_ids.add(atomic_id)
        if not str(row.get("atomic_claim", "")).strip():
            raise RuntimeError(f"{qid} {atomic_id}: empty atomic claim")
        if row.get("action") not in ACTIONS:
            raise RuntimeError(f"{qid} {atomic_id}: invalid action")
        evidence_ids = set(str(value) for value in row.get("evidence_ids", []))
        if not evidence_ids or not evidence_ids <= set(evidence):
            raise RuntimeError(f"{qid} {atomic_id}: invalid evidence IDs")
        targets = set(str(value) for value in row.get("target_claim_group_ids", []))
        if not targets <= group_ids:
            raise RuntimeError(f"{qid} {atomic_id}: invalid target groups")
        if row["action"] != "deleted" and not targets:
            raise RuntimeError(f"{qid} {atomic_id}: retained claim has no target")

    for group in claims + constraints:
        if not set(group["source_atomic_claim_ids"]) <= atomic_ids:
            raise RuntimeError(f"{qid} {group['claim_group_id']}: unknown atomic claim")

    if not str(result["reference_answer"]).strip():
        raise RuntimeError(f"{qid}: empty reference answer")
    mappings = result["reference_answer_claim_map"]
    if not isinstance(mappings, list):
        raise RuntimeError(f"{qid}: invalid reference map")
    for row in mappings:
        if row.get("claim_group_id") not in group_ids:
            raise RuntimeError(f"{qid}: reference map has unknown group")
        if not str(row.get("reference_answer_excerpt", "")).strip():
            raise RuntimeError(f"{qid}: empty reference map excerpt")
    if not isinstance(result["unresolved_or_unsupported"], list):
        raise RuntimeError(f"{qid}: invalid unresolved list")
    boundary = result["boundary_check"]
    if set(boundary) != {
        "must_include_addressed",
        "must_not_claim_respected",
        "notes",
    }:
        raise RuntimeError(f"{qid}: invalid boundary check")
    if boundary["must_include_addressed"] is not True:
        raise RuntimeError(f"{qid}: must_include not addressed")
    if boundary["must_not_claim_respected"] is not True:
        raise RuntimeError(f"{qid}: must_not_claim not respected")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--limit", type=int)
    args = parser.parse_args()

    packets = common.read_jsonl(common.REFERENCE_PACKETS)
    items = packets[: args.limit] if args.limit else packets
    prompt = PROMPT.read_text(encoding="utf-8")

    def worker(packet: dict[str, Any]) -> dict[str, Any]:
        result, metadata = common.call_openai_json(
            system_prompt=prompt,
            payload=packet,
            max_completion_tokens=20000,
        )
        try:
            validate(result, packet)
        except Exception:
            quarantine = (
                common.PACKAGE
                / "reference_build/drafts/quarantine"
                / f"{packet['question_id']}__{metadata['response_id']}.json"
            )
            common.write_json(
                quarantine,
                {
                    "question_id": packet["question_id"],
                    "reference_packet_sha256": common.payload_sha256(packet),
                    "prompt_sha256": common.sha256(PROMPT),
                    "raw_result": result,
                    "generation": metadata,
                    "analytical_status": "quarantined_schema_invalid",
                },
            )
            raise
        return {
            "question_id": packet["question_id"],
            "reference_packet_sha256": common.payload_sha256(packet),
            "prompt_sha256": common.sha256(PROMPT),
            "draft_ledger": result,
            "generation": metadata,
        }

    rows = common.run_parallel(
        items=items,
        worker=worker,
        key=lambda row: str(row["question_id"]),
        output=common.DRAFTS,
        workers=args.workers,
        resume=args.resume,
    )
    common.write_json(
        common.PACKAGE / "reference_build/drafts/run_manifest.json",
        {
            "stage": "candidate-blind Test40 structured claim-ledger drafting",
            "question_count": len(rows),
            "model": "gpt-5.1",
            "required_response_model": common.EXPECTED_RESPONSE_MODEL,
            "reasoning_effort": "low",
            "prompt_sha256": common.sha256(PROMPT),
            "reference_packets_sha256": common.sha256(common.REFERENCE_PACKETS),
            "output_sha256": common.sha256(common.DRAFTS),
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
    print(json.dumps({"draft_ledgers": len(rows)}, indent=2))


if __name__ == "__main__":
    main()

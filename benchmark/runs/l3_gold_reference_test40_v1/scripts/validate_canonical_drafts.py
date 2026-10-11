from __future__ import annotations

import json

import common
import run_reference_drafts as drafts


CANONICAL = (
    common.PACKAGE / "reference_build/revisions/model_a_ledgers_repair1.jsonl"
)


def main() -> None:
    packets = common.read_jsonl(common.REFERENCE_PACKETS)
    ledgers = common.read_jsonl(CANONICAL)
    if len(packets) != 40 or len(ledgers) != 40:
        raise RuntimeError("Expected 40 reference packets and canonical ledgers")
    packet_by_qid = {row["question_id"]: row for row in packets}
    if len(packet_by_qid) != 40 or {row["question_id"] for row in ledgers} != set(
        packet_by_qid
    ):
        raise RuntimeError("Canonical ledger membership differs from Test40")
    response_ids: set[str] = set()
    group_count = 0
    for row in ledgers:
        qid = row["question_id"]
        if row["reference_packet_sha256"] != common.payload_sha256(
            packet_by_qid[qid]
        ):
            raise RuntimeError(f"{qid}: stale reference packet hash")
        drafts.validate(row["draft_ledger"], packet_by_qid[qid])
        response_id = row["generation"]["response_id"]
        if response_id in response_ids:
            raise RuntimeError(f"{qid}: duplicate response ID")
        response_ids.add(response_id)
        group_count += len(row["draft_ledger"]["claim_groups"])
        group_count += len(row["draft_ledger"]["constraint_groups"])
    result = {
        "status": "pass",
        "question_count": len(ledgers),
        "distinct_model_a_responses": len(response_ids),
        "claim_and_constraint_group_count": group_count,
        "canonical_sha256": common.sha256(CANONICAL),
        "candidate_test40_inputs_used": False,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

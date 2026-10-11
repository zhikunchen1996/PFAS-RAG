from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Any

import common


def validate_reference(
    candidate: dict[str, Any],
    packet: dict[str, Any],
    review: dict[str, Any],
) -> None:
    qid = packet["question_id"]
    human = candidate.get("human_review", {})
    if human.get("decision") != "approve":
        raise RuntimeError(f"{qid}: human decision is not approve")
    if not str(human.get("review_date", "")).strip():
        raise RuntimeError(f"{qid}: human review date is missing")
    if review["review"]["overall_verdict"] != "approve" and not str(
        human.get("resolution_notes", "")
    ).strip():
        raise RuntimeError(
            f"{qid}: Model B requested revision; resolution notes are required"
        )
    if candidate.get("question_text") != packet["question"]["question_text"]:
        raise RuntimeError(f"{qid}: question text changed during human review")
    if candidate.get("task_boundaries") != packet["task_boundaries"]:
        raise RuntimeError(f"{qid}: task boundaries changed during human review")
    expected_review_hash = common.payload_sha256(review["review"])
    if candidate.get("model_b_review_sha256") != expected_review_hash:
        raise RuntimeError(f"{qid}: Model B review hash mismatch")
    reference = candidate.get("approved_reference")
    if not isinstance(reference, dict) or not reference.get("reference_answer"):
        raise RuntimeError(f"{qid}: approved reference is missing")
    if reference.get("question_id") != qid:
        raise RuntimeError(f"{qid}: reference question ID differs")
    claims = reference.get("claims")
    if not isinstance(claims, list) or not claims:
        raise RuntimeError(f"{qid}: no approved claims")
    valid_evidence = {
        row["evidence_id"] for row in packet["gold_evidence"]
    }
    claim_ids: set[str] = set()
    core_count = 0
    for claim in claims:
        claim_id = str(claim.get("claim_id", ""))
        if not claim_id or claim_id in claim_ids:
            raise RuntimeError(f"{qid}: invalid or duplicate claim ID")
        if not str(claim.get("claim_text", "")).strip():
            raise RuntimeError(f"{qid} {claim_id}: empty claim text")
        claim_ids.add(claim_id)
        if claim.get("claim_type") == "core":
            core_count += 1
        evidence_ids = set(claim.get("evidence_ids", []))
        if not evidence_ids or not evidence_ids <= valid_evidence:
            raise RuntimeError(f"{qid} {claim_id}: invalid evidence links")
    if core_count == 0:
        raise RuntimeError(f"{qid}: at least one core claim is required")


def main() -> None:
    if not common.HUMAN_CANDIDATES.exists():
        raise RuntimeError("Run build_human_audit.py first")
    packets = {
        row["question_id"]: row for row in common.read_jsonl(common.PACKETS)
    }
    reviews = {
        row["question_id"]: row for row in common.read_jsonl(common.REVIEWS)
    }
    candidates = common.read_jsonl(common.HUMAN_CANDIDATES)
    expected = set(packets)
    if {row["question_id"] for row in candidates} != expected:
        raise RuntimeError("Human candidate membership differs from Dev13")
    pending = [
        row["question_id"]
        for row in candidates
        if row.get("human_review", {}).get("decision") != "approve"
    ]
    if pending:
        raise RuntimeError(
            "Cannot freeze references; project-author approval is missing for "
            f"{len(pending)} questions: {', '.join(pending)}"
        )

    frozen: list[dict[str, Any]] = []
    for candidate in candidates:
        qid = candidate["question_id"]
        validate_reference(candidate, packets[qid], reviews[qid])
        frozen.append(
            {
                "question_id": qid,
                "question_text": candidate["question_text"],
                "task_boundaries": candidate["task_boundaries"],
                "gold_is_non_exhaustive": True,
                "reference": candidate["approved_reference"],
                "human_review": candidate["human_review"],
                "provenance": {
                    "packet_sha256": common.payload_sha256(packets[qid]),
                    "model_b_review_sha256": common.payload_sha256(
                        reviews[qid]["review"]
                    ),
                    "approved_reference_sha256": common.payload_sha256(
                        candidate["approved_reference"]
                    ),
                },
            }
        )

    output = common.PACKAGE / "frozen/reference_answers.jsonl"
    common.write_jsonl(output, frozen)
    manifest = {
        "freeze_id": "l3_gold_reference_dev13_v1",
        "freeze_date_utc": datetime.now(timezone.utc).isoformat(),
        "question_count": len(frozen),
        "status": "frozen_dev13_reference",
        "reference_answers": str(output.relative_to(common.ROOT)),
        "reference_answers_sha256": common.sha256(output),
        "protocol_sha256": common.sha256(common.PACKAGE / "protocol.json"),
        "prompt_hashes": {
            path.name: common.sha256(path)
            for path in sorted((common.PACKAGE / "prompts").glob("*.txt"))
        },
        "source_hashes": {
            str(common.QUESTIONS.relative_to(common.ROOT)): common.sha256(
                common.QUESTIONS
            ),
            str(common.GOLD.relative_to(common.ROOT)): common.sha256(common.GOLD),
            str(common.BOUNDARIES.relative_to(common.ROOT)): common.sha256(
                common.BOUNDARIES
            ),
        },
        "construction_hashes": {
            "reference_packets": common.sha256(common.PACKETS),
            "model_a_drafts": common.sha256(common.DRAFTS),
            "model_b_reviews": common.sha256(common.REVIEWS),
            "human_reference_candidates": common.sha256(
                common.HUMAN_CANDIDATES
            ),
        },
        "test40_l3_evaluated": False,
    }
    common.write_json(common.PACKAGE / "frozen/freeze_manifest.json", manifest)
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()

from __future__ import annotations

import json
from collections import Counter

import common


def main() -> None:
    questions = common.read_csv(common.QUESTIONS)
    boundaries = {
        row["question_id"]: row for row in common.read_csv(common.BOUNDARIES)
    }
    gold = common.read_jsonl(common.GOLD)
    gold_by_qid = common.by_question(gold)
    author_record = json.loads(common.AUTHOR_REVIEW.read_text(encoding="utf-8"))
    author_register = {
        (row["question_id"], row["evidence_id"]): row
        for row in common.read_csv(common.GOLD_AUTHOR_REGISTER)
    }

    qids = [row["question_id"] for row in questions]
    if set(qids) != set(boundaries):
        raise RuntimeError("Question and task-boundary membership differ")
    missing = [qid for qid in qids if not gold_by_qid.get(qid)]
    if missing:
        raise RuntimeError(f"Questions without gold: {missing}")
    if author_record.get("decision") is None:
        raise RuntimeError("Missing project-author gold review record")

    packets = []
    for question in questions:
        qid = question["question_id"]
        rows = gold_by_qid[qid]
        evidence_ids = [str(row["evidence_id"]) for row in rows]
        if len(evidence_ids) != len(set(evidence_ids)):
            raise RuntimeError(f"{qid}: duplicate evidence IDs")
        compact_rows = []
        for row in rows:
            review_key = (qid, str(row["evidence_id"]))
            if review_key not in author_register:
                raise RuntimeError(f"{qid}: missing author decision for {review_key[1]}")
            compact = common.compact_gold(row)
            compact["author_review_decision"] = author_register[review_key][
                "author_review_decision"
            ]
            compact_rows.append(compact)
        packets.append(
            {
                "question_id": qid,
                "question": {
                    "question_text": question["question_text"],
                    "task_type": question["task_type"],
                    "answerability_type": question["answerability_type"],
                },
                "task_boundaries": {
                    "must_include": boundaries[qid]["must_include"],
                    "must_not_claim": boundaries[qid]["must_not_claim"],
                },
                "gold_is_non_exhaustive": True,
                "gold_evidence": compact_rows,
                "author_review_provenance": {
                    "record_id": author_record["record_id"],
                    "decision_type": author_record["decision_type"],
                    "decision": author_record["decision"],
                    "interpretation_limit": author_record["interpretation_limit"],
                },
            }
        )

    common.write_jsonl(common.PACKETS, packets)
    type_counts = Counter(
        evidence["evidence_type"]
        for packet in packets
        for evidence in packet["gold_evidence"]
    )
    manifest = {
        "protocol_id": "l3_gold_reference_dev13_v1",
        "question_count": len(packets),
        "gold_record_count": sum(len(row["gold_evidence"]) for row in packets),
        "gold_type_counts": dict(sorted(type_counts.items())),
        "source_hashes": {
            str(common.QUESTIONS.relative_to(common.ROOT)): common.sha256(
                common.QUESTIONS
            ),
            str(common.GOLD.relative_to(common.ROOT)): common.sha256(common.GOLD),
            str(common.BOUNDARIES.relative_to(common.ROOT)): common.sha256(
                common.BOUNDARIES
            ),
            str(common.AUTHOR_REVIEW.relative_to(common.ROOT)): common.sha256(
                common.AUTHOR_REVIEW
            ),
            str(
                common.GOLD_AUTHOR_REGISTER.relative_to(common.ROOT)
            ): common.sha256(common.GOLD_AUTHOR_REGISTER),
        },
        "packet_file": str(common.PACKETS.relative_to(common.ROOT)),
        "packet_sha256": common.sha256(common.PACKETS),
        "packet_payload_sha256": {
            row["question_id"]: common.payload_sha256(row) for row in packets
        },
        "forbidden_inputs_confirmed_absent": [
            "candidate Direct answers",
            "candidate RAG answers",
            "retrieved top-k contexts",
            "system labels",
            "prior judge outcomes",
        ],
    }
    common.write_json(
        common.PACKAGE / "reference_build/inputs/build_manifest.json",
        manifest,
    )
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()

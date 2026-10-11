from __future__ import annotations

import json
import re
from collections import Counter
from typing import Any

import chromadb

import common


QUESTION_ALLOWLIST = [
    "question_id",
    "question_text",
    "task_type",
    "answerability_type",
    "must_include",
    "must_not_claim",
    "expected_operation",
    "required_conditions",
    "required_units",
    "forbidden_overclaims",
    "workflow_scenario",
    "information_need",
]

FORBIDDEN_QUESTION_FIELDS = {
    "gold_minimal_answer",
    "gold_full_answer",
    "pass_rule",
    "fatal_error_rule",
    "notes",
}


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("–", "-").replace("—", "-")).strip()


def collection_chunks() -> dict[tuple[str, str], dict[str, Any]]:
    client = chromadb.PersistentClient(path=str(common.CHROMA_PATH))
    collection = client.get_collection(common.COLLECTION_NAME)
    data = collection.get(include=["documents", "metadatas"])
    chunks: dict[tuple[str, str], dict[str, Any]] = {}
    for document, metadata in zip(data["documents"], data["metadatas"]):
        key = (str(metadata.get("source", "")), str(metadata.get("chunk", "")))
        if key in chunks:
            raise RuntimeError(f"Duplicate corpus chunk key: {key}")
        chunks[key] = {
            "full_chunk_text": str(document),
            "corpus_metadata": {
                field: metadata.get(field, "")
                for field in [
                    "source",
                    "chunk",
                    "title",
                    "authors",
                    "year",
                    "journal",
                    "doi",
                    "section",
                ]
            },
        }
    return chunks


def main() -> None:
    questions = common.read_csv(common.QUESTIONS)
    test_qids = [row["question_id"] for row in questions]
    if len(test_qids) != 40 or len(set(test_qids)) != 40:
        raise RuntimeError("Expected exactly 40 unique Test40 questions")

    gold_rows = [
        row
        for row in common.read_jsonl(common.GOLD)
        if str(row["question_id"]) in set(test_qids)
    ]
    if len(gold_rows) != 189:
        raise RuntimeError(f"Expected 189 Test40 gold records, found {len(gold_rows)}")

    author_record = json.loads(common.AUTHOR_REVIEW.read_text(encoding="utf-8"))
    decisions = {
        (row["question_id"], row["evidence_id"]): row["author_review_decision"]
        for row in common.read_csv(common.GOLD_AUTHOR_REGISTER)
        if row["question_id"] in set(test_qids)
    }
    if len(decisions) != 189 or set(decisions.values()) != {
        "retained_after_project_author_review"
    }:
        raise RuntimeError("Test40 gold author decisions are incomplete")

    chunks = collection_chunks()
    gold_by_qid: dict[str, list[dict[str, Any]]] = {}
    span_checks = Counter()
    for row in gold_rows:
        qid = str(row["question_id"])
        evidence_id = str(row["evidence_id"])
        key = (str(row["doc_id"]), str(row["chunk_id"]))
        if key not in chunks:
            raise RuntimeError(f"{qid} {evidence_id}: missing corpus chunk {key}")
        full_chunk = chunks[key]["full_chunk_text"]
        exact_span = str(row.get("exact_evidence_span", "")).strip()
        unit_spans = [str(value).strip() for value in row.get("unit_exact_spans", [])]
        exact_in_chunk = normalized(exact_span) in normalized(full_chunk)
        units_in_chunk = [normalized(span) in normalized(full_chunk) for span in unit_spans]
        span_checks["exact_in_chunk" if exact_in_chunk else "exact_not_in_chunk"] += 1
        span_checks["all_units_in_chunk" if all(units_in_chunk) else "unit_not_in_chunk"] += 1
        gold_by_qid.setdefault(qid, []).append(
            {
                "evidence_id": evidence_id,
                "evidence_type": str(row["evidence_type"]),
                "doc_id": key[0],
                "chunk_id": key[1],
                "exact_evidence_span": exact_span,
                "unit_exact_spans": unit_spans,
                "full_chunk_text": full_chunk,
                "corpus_metadata": chunks[key]["corpus_metadata"],
                "author_review_decision": decisions[(qid, evidence_id)],
                "exact_span_found_in_full_chunk": exact_in_chunk,
                "unit_spans_found_in_full_chunk": units_in_chunk,
            }
        )

    missing = [qid for qid in test_qids if not gold_by_qid.get(qid)]
    if missing:
        raise RuntimeError(f"Questions without gold: {missing}")

    packets = []
    for row in questions:
        forbidden_present = FORBIDDEN_QUESTION_FIELDS & {
            field for field, value in row.items() if value
        }
        allowlisted = {field: row.get(field, "") for field in QUESTION_ALLOWLIST}
        packets.append(
            {
                "question_id": row["question_id"],
                "question": allowlisted,
                "gold_is_non_exhaustive": True,
                "approved_source_evidence": gold_by_qid[row["question_id"]],
                "author_review_provenance": {
                    "record_id": author_record.get("record_id", ""),
                    "decision": author_record.get("decision", ""),
                    "interpretation_limit": author_record.get(
                        "interpretation_limit", ""
                    ),
                },
                "excluded_nonempty_question_fields": sorted(forbidden_present),
            }
        )

    common.write_jsonl(common.SOURCE_PACKETS, packets)
    manifest = {
        "protocol_id": "l3_gold_reference_test40_v1",
        "stage": "candidate-blind allowlisted source packet construction",
        "question_count": len(packets),
        "gold_record_count": sum(
            len(row["approved_source_evidence"]) for row in packets
        ),
        "evidence_type_counts": dict(
            sorted(Counter(row["evidence_type"] for row in gold_rows).items())
        ),
        "span_checks": dict(sorted(span_checks.items())),
        "question_allowlist": QUESTION_ALLOWLIST,
        "forbidden_model_visible_fields": sorted(FORBIDDEN_QUESTION_FIELDS),
        "source_hashes": {
            str(common.QUESTIONS.relative_to(common.ROOT)): common.sha256(
                common.QUESTIONS
            ),
            str(common.GOLD.relative_to(common.ROOT)): common.sha256(common.GOLD),
            str(common.AUTHOR_REVIEW.relative_to(common.ROOT)): common.sha256(
                common.AUTHOR_REVIEW
            ),
            str(common.GOLD_AUTHOR_REGISTER.relative_to(common.ROOT)): common.sha256(
                common.GOLD_AUTHOR_REGISTER
            ),
        },
        "packet_sha256": common.sha256(common.SOURCE_PACKETS),
        "packet_payload_sha256": {
            row["question_id"]: common.payload_sha256(row) for row in packets
        },
        "candidate_test40_inputs_used": False,
    }
    common.write_json(
        common.PACKAGE / "reference_build/inputs/source_packet_manifest.json",
        manifest,
    )
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()

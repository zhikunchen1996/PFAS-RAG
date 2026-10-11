from __future__ import annotations

import json
import common


LEDGERS = (
    common.PACKAGE
    / "reference_build/revisions/model_a_ledgers_resolution3.jsonl"
)
OUTPUT_DIR = common.PACKAGE / "l15_reference_validation_v2"
ANSWERS = OUTPUT_DIR / "inputs/reference_answers_l15.jsonl"
def main() -> None:
    if OUTPUT_DIR.exists():
        raise RuntimeError(
            "L1.5 reference validation directory already exists; refusing overwrite"
        )
    packets = {
        row["question_id"]: row for row in common.read_jsonl(common.REFERENCE_PACKETS)
    }
    ledgers = {
        row["question_id"]: row for row in common.read_jsonl(LEDGERS)
    }
    questions = common.read_csv(common.QUESTIONS)
    question_ids = [row["question_id"] for row in questions]
    if len(question_ids) != 40 or set(question_ids) != set(packets) or set(
        question_ids
    ) != set(ledgers):
        raise RuntimeError("L1.5 input membership must match all 40 Test questions")

    answer_rows = []
    mapping_rows = []
    for qid in question_ids:
        packet = packets[qid]
        ledger = ledgers[qid]["draft_ledger"]
        chunk_rank_by_key = {}
        contexts = []
        evidence_to_rank = {}
        for evidence in packet["approved_source_evidence"]:
            key = (
                evidence["doc_id"],
                str(evidence["chunk_id"]),
                evidence["full_chunk_text"],
            )
            if key not in chunk_rank_by_key:
                rank = len(contexts) + 1
                chunk_rank_by_key[key] = rank
                contexts.append(
                    {
                        "rank": rank,
                        "doc_id": evidence["doc_id"],
                        "chunk_id": str(evidence["chunk_id"]),
                        "text": evidence["full_chunk_text"],
                    }
                )
            evidence_to_rank[evidence["evidence_id"]] = chunk_rank_by_key[key]
        # Constraint-only groups are L3 violation rules, not positive content
        # that a gold answer is expected to state. L1.5 validates only the
        # normative answer-content claim groups.
        groups = ledger["claim_groups"]
        answer_lines = ["Normative reference claims:"]
        group_citations = []
        cited = set()
        for group in groups:
            ranks = []
            for evidence_id in group["evidence_ids"]:
                rank = evidence_to_rank[evidence_id]
                if rank not in ranks:
                    ranks.append(rank)
                    cited.add(rank)
            if not ranks:
                raise RuntimeError(
                    f"{qid} {group['claim_group_id']}: no cited evidence"
                )
            marker = "[" + ", ".join(f"C{rank}" for rank in ranks) + "]"
            answer_lines.append(f"- {group['canonical_proposition']} {marker}")
            group_citations.append(
                {
                    "claim_group_id": group["claim_group_id"],
                    "citation_ids": [f"C{rank}" for rank in ranks],
                }
            )
        answer = "\n".join(answer_lines)
        if not cited:
            raise RuntimeError(f"{qid}: reference answer contains no [C#] citation")
        if cited - {row["rank"] for row in contexts}:
            raise RuntimeError(f"{qid}: citation lacks a supplied full chunk")
        answer_rows.append(
            {
                "question_id": qid,
                "answer": answer,
                "retrieved_context": contexts,
                "validation_role": "pre-freeze normative-ledger citation support",
                "candidate_system_answer": False,
            }
        )
        mapping_rows.append(
            {
                "question_id": qid,
                "reference_ledger_sha256": common.payload_sha256(ledger),
                "citation_mapping": [
                    {
                        "evidence_id": evidence_id,
                        "citation_id": f"C{rank}",
                    }
                    for evidence_id, rank in evidence_to_rank.items()
                ],
                "group_citation_mapping": group_citations,
                "unique_complete_chunk_count": len(contexts),
                "cited_chunk_count": len(cited),
            }
        )

    common.write_jsonl(ANSWERS, answer_rows)
    mapping_path = OUTPUT_DIR / "inputs/citation_mapping.jsonl"
    common.write_jsonl(mapping_path, mapping_rows)
    manifest = {
        "stage": "pre-freeze L1.5 validation input construction",
        "purpose": (
            "citation-support validation of ledger-rendered normative Test40 "
            "answer-content claims; constraint-only violation rules are retained "
            "in the ledger but are not rendered as gold-answer statements; "
            "not a candidate-system Test40 evaluation"
        ),
        "question_count": len(answer_rows),
        "model_calls_made": False,
        "candidate_test40_inputs_used": False,
        "candidate_system_answers_used": False,
        "rendered_group_scope": "claim_groups only; constraint_groups excluded",
        "questions_sha256": common.sha256(common.QUESTIONS),
        "source_packets_sha256": common.sha256(common.REFERENCE_PACKETS),
        "reference_ledgers_sha256": common.sha256(LEDGERS),
        "reference_answers_l15_sha256": common.sha256(ANSWERS),
        "citation_mapping_sha256": common.sha256(mapping_path),
        "frozen_l15_prompt_sha256": common.sha256(
            common.FROZEN_V3
            / "judge/prompts/l15_claim_citation_support_v2.txt"
        ),
        "freeze_gate": (
            "Frozen L1.5 lenient claim-level rule: supported and "
            "partially_supported both pass; only not_supported or contradicted "
            "cited claims block freeze. Uncited claims are diagnostic only."
        ),
    }
    common.write_json(OUTPUT_DIR / "input_manifest.json", manifest)
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()

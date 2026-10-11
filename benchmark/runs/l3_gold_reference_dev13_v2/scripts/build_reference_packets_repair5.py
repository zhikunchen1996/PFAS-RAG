from __future__ import annotations

import copy
import json
import re
from pathlib import Path
from typing import Any

import chromadb

import common


SOURCE = common.PACKETS
OUTPUT = (
    common.PACKAGE
    / "reference_build/inputs/reference_packets_repair5.jsonl"
)
MANIFEST = OUTPUT.with_name("reference_packets_repair5_manifest.json")
CHROMA_PATH = common.ROOT / "data/chroma"
COLLECTION_NAME = (
    "rag_documents_bge_large_en_v1_5_sent256_overlap2_"
    "corpus434_repaired_v1"
)


def normalized_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()

# These replacements retain the original audited gold record and evidence ID,
# but expose the complete original chunk so method, table-header, or condition
# qualifiers are supported by the model-visible evidence rather than metadata.
SPAN_EXPANSIONS: dict[tuple[str, str], list[int]] = {
    ("NQ10", "NQ10_MMG007"): [11],
    ("NQ10", "NQ10_MMG009"): [32],
    ("NQ12", "NQ12_MMG001"): [44],
    ("NQ12", "NQ12_MMG002"): [47],
    ("NQ15", "NQ15_MMG003"): [18],
    ("NQ15", "NQ15_MMG004"): [46],
    ("NQ23", "NQ23_MMG004"): [46],
    ("WF10_025", "WF10_025_MMG001"): [1],
    ("WF10_004b", "WF10_004b_MMG002"): [14],
}

# All transferred records already belong to the frozen249 project-author
# audited gold. They are copied only into the L3 reference-construction packet;
# the frozen retrieval gold and retrieval metrics are unchanged.
TRANSFERRED_GOLD = {
    "WF10_002": {
        "WF10_002_L3X001": "NQ26_MMG004",
        "WF10_002_L3X002": "NQ26_MMG002",
        "WF10_002_L3X003": "WF10_030_MMG002",
    }
}

NQ24_CONTEXT_SOURCE = (
    "2023 - Shaikh - PFOA remediation from aqueous media using CTAB "
    "impregnated activated carbon - A closed-loop sustainable study with "
    "comprehensive selectivity analysis.pdf"
)


def chunk_lookup() -> dict[tuple[str, int], tuple[str, dict[str, Any]]]:
    client = chromadb.PersistentClient(path=str(CHROMA_PATH))
    collection = client.get_collection(COLLECTION_NAME)
    data = collection.get(include=["documents", "metadatas"])
    result: dict[tuple[str, int], tuple[str, dict[str, Any]]] = {}
    for document, metadata in zip(
        data.get("documents", []) or [],
        data.get("metadatas", []) or [],
    ):
        source = str(metadata.get("source") or "")
        chunk = int(metadata.get("chunk") or 0)
        result[(source, chunk)] = (str(document), dict(metadata))
    return result


def expand_gold_spans(
    packets: list[dict[str, Any]],
    chunks: dict[tuple[str, int], tuple[str, dict[str, Any]]],
) -> list[dict[str, Any]]:
    expanded: list[dict[str, Any]] = []
    for packet in packets:
        qid = str(packet["question_id"])
        for evidence in packet["gold_evidence"]:
            key = (qid, str(evidence["evidence_id"]))
            chunk_ids = SPAN_EXPANSIONS.get(key)
            if not chunk_ids:
                continue
            source = str(evidence["doc_id"])
            selected = []
            for chunk_id in chunk_ids:
                chunk_key = (source, chunk_id)
                if chunk_key not in chunks:
                    raise RuntimeError(
                        f"Missing source chunk for {key}: {chunk_key}"
                    )
                selected.append(chunks[chunk_key][0])
            expanded_span = "\n\n".join(selected)
            original_span = str(evidence["exact_evidence_span"])
            if normalized_whitespace(original_span) not in normalized_whitespace(
                expanded_span
            ):
                raise RuntimeError(
                    f"Original exact span is absent from expanded context: {key}"
                )
            evidence["original_exact_evidence_span"] = original_span
            evidence["exact_evidence_span"] = expanded_span
            evidence["span_revision_kind"] = "complete_original_chunk"
            evidence["span_context_chunk_ids"] = chunk_ids
            evidence["span_context_collection"] = COLLECTION_NAME
            expanded.append(
                {
                    "question_id": qid,
                    "evidence_id": evidence["evidence_id"],
                    "doc_id": source,
                    "chunk_ids": chunk_ids,
                    "original_span_sha256": common.payload_sha256(
                        original_span
                    ),
                    "expanded_span_sha256": common.payload_sha256(
                        expanded_span
                    ),
                }
            )
    if len(expanded) != len(SPAN_EXPANSIONS):
        raise RuntimeError("Not every declared span expansion was applied")
    return expanded


def add_transferred_gold(
    packets: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    packet_by_qid = {row["question_id"]: row for row in packets}
    source_by_evidence_id: dict[str, tuple[str, dict[str, Any]]] = {}
    for packet in packets:
        for evidence in packet["gold_evidence"]:
            source_by_evidence_id[str(evidence["evidence_id"])] = (
                str(packet["question_id"]),
                evidence,
            )
    additions: list[dict[str, Any]] = []
    for target_qid, mapping in TRANSFERRED_GOLD.items():
        target = packet_by_qid[target_qid]
        existing = {
            str(row["evidence_id"]) for row in target["gold_evidence"]
        }
        for new_id, source_id in mapping.items():
            if new_id in existing:
                raise RuntimeError(f"Duplicate transferred evidence ID: {new_id}")
            if source_id not in source_by_evidence_id:
                raise RuntimeError(f"Missing transferred gold source: {source_id}")
            source_qid, source = source_by_evidence_id[source_id]
            copied = copy.deepcopy(source)
            copied["source_question_id"] = source_qid
            copied["source_evidence_id"] = source_id
            copied["original_evidence_type"] = copied["evidence_type"]
            copied["evidence_type"] = "l3_transferred_audited_gold"
            copied["evidence_id"] = new_id
            copied["l3_transfer_reason"] = (
                "Adds already project-author-audited evidence needed to cover "
                "a treatment system named by the visible WF10_002 question; "
                "the retrieval-gold assignment is unchanged."
            )
            target["gold_evidence"].append(copied)
            existing.add(new_id)
            additions.append(
                {
                    "target_question_id": target_qid,
                    "evidence_id": new_id,
                    "source_question_id": source_qid,
                    "source_evidence_id": source_id,
                    "source_payload_sha256": common.payload_sha256(source),
                }
            )
    return additions


def add_nq24_context(
    packets: list[dict[str, Any]],
    chunks: dict[tuple[str, int], tuple[str, dict[str, Any]]],
) -> dict[str, Any]:
    packet = next(row for row in packets if row["question_id"] == "NQ24")
    chunk_key = (NQ24_CONTEXT_SOURCE, 0)
    if chunk_key not in chunks:
        raise RuntimeError(f"Missing NQ24 context chunk: {chunk_key}")
    document, metadata = chunks[chunk_key]
    evidence_id = "NQ24_L3CTX001"
    if any(
        row["evidence_id"] == evidence_id
        for row in packet["gold_evidence"]
    ):
        raise RuntimeError(f"Duplicate NQ24 context ID: {evidence_id}")
    packet["gold_evidence"].append(
        {
            "evidence_id": evidence_id,
            "evidence_type": "l3_source_context_pending_author_confirmation",
            "doc_id": NQ24_CONTEXT_SOURCE,
            "chunk_id": "0",
            "exact_evidence_span": document,
            "supported_claim": (
                "The source study investigates PFOA adsorption from aqueous "
                "media using CTAB-impregnated activated carbon."
            ),
            "does_not_support": (
                "This context chunk identifies the study, compound, and "
                "sorbent but does not contain the 5.71 or 6.85 mg/g values."
            ),
            "PFAS_compound": "PFOA",
            "matrix": "aqueous media",
            "method_or_material": "CTAB-impregnated activated carbon",
            "endpoint": "study identity and scope",
            "numerical_value": "",
            "unit": "",
            "protocol_detail": "",
            "limitation": (
                "L3 context supplement from the same source document; the "
                "project author must confirm it during the repair5 audit."
            ),
            "supports_universal_claim": "no",
            "author_review_decision": "pending_project_author_confirmation",
            "span_revision_kind": "same_document_identity_context",
            "span_context_chunk_ids": [0],
            "span_context_collection": COLLECTION_NAME,
            "source_metadata": {
                "title": metadata.get("title", ""),
                "doi": metadata.get("doi", ""),
            },
        }
    )
    return {
        "question_id": "NQ24",
        "evidence_id": evidence_id,
        "doc_id": NQ24_CONTEXT_SOURCE,
        "chunk_id": 0,
        "span_sha256": common.payload_sha256(document),
        "author_confirmation_required": True,
    }


def main() -> None:
    packets = copy.deepcopy(common.read_jsonl(SOURCE))
    chunks = chunk_lookup()
    expanded = expand_gold_spans(packets, chunks)
    transferred = add_transferred_gold(packets)
    context = add_nq24_context(packets, chunks)
    common.write_jsonl(OUTPUT, packets)
    common.write_json(
        MANIFEST,
        {
            "stage": "L3 repair5 reference-packet repair",
            "source_packets_file": str(SOURCE.relative_to(common.ROOT)),
            "source_packets_sha256": common.sha256(SOURCE),
            "output_file": str(OUTPUT.relative_to(common.ROOT)),
            "output_sha256": common.sha256(OUTPUT),
            "question_count": len(packets),
            "evidence_record_count": sum(
                len(row["gold_evidence"]) for row in packets
            ),
            "collection": COLLECTION_NAME,
            "span_expansions": expanded,
            "transferred_audited_gold": transferred,
            "new_source_context": context,
            "retrieval_gold_modified": False,
            "candidate_answers_used": False,
            "nq12_table_verification": {
                "status": "verified",
                "date": "2026-07-29",
                "source": (
                    "Pellicer-Castell et al., Nanomaterials 2022, 12, 1441, "
                    "Table 2 (PMC9105103)"
                ),
                "finding": (
                    "The Sensitivity header contains LOD and LOQ subcolumns; "
                    "the reported ranges 3-8 and 9-25 ng/L are retained."
                ),
            },
        },
    )
    print(
        json.dumps(
            {
                "questions": len(packets),
                "span_expansions": len(expanded),
                "transferred_gold": len(transferred),
                "new_context_records": 1,
                "output": str(OUTPUT),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Development utility for extracting review-outline candidates from Chroma."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import chromadb


KEY_TERMS = re.compile(
    r"\b("
    r"challenge|limitation|future|perspective|outlook|conclusion|"
    r"mechanism|operating condition|matrix|scale(?:-?up)?|field|"
    r"energy|cost|by-?product|residual|regenerat|treatment train|"
    r"research need|knowledge gap"
    r")\b",
    re.IGNORECASE,
)
DESIGN_EVIDENCE_GROUPS = {
    "scope": (
        "this review",
        "we review",
        "systematically review",
        "focus on",
        "scope",
        "current approaches",
        "state of the art",
    ),
    "comparison_axes": (
        "mechanism",
        "operating condition",
        "water matrix",
        "pfas structure",
        "chain length",
        "removal efficiency",
        "degradation",
        "defluorination",
        "energy",
    ),
    "engineering_constraints": (
        "scale-up",
        "scaling up",
        "pilot",
        "field",
        "cost",
        "energy",
        "fouling",
        "residual",
        "byproduct",
        "regeneration",
    ),
    "gaps_and_outlook": (
        "future",
        "perspective",
        "outlook",
        "challenge",
        "limitation",
        "knowledge gap",
        "research need",
        "further study",
        "remains",
    ),
}
HEADING = re.compile(
    r"^\s*(?:\d+(?:\.\d+){0,3}\s+|"
    r"(?:conclusions?|challenges?|limitations?|perspectives?|outlook|"
    r"future directions?|mechanisms?)\b)",
    re.IGNORECASE,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--chroma-path", default="data/chroma")
    parser.add_argument(
        "--collection",
        default=(
            "rag_documents_bge_large_en_v1_5_"
            "sent256_overlap2_corpus434_repaired_v1"
        ),
    )
    parser.add_argument("--preview-chars", type=int, default=900)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    collection = chromadb.PersistentClient(path=args.chroma_path).get_collection(
        args.collection
    )
    result = collection.get(
        where={"source": args.source},
        include=["documents", "metadatas"],
    )
    records = sorted(
        zip(result["ids"], result["documents"], result["metadatas"]),
        key=lambda item: int(item[2].get("chunk", 0)),
    )
    if not records:
        raise RuntimeError(f"No chunks found for source: {args.source}")

    selected = []
    last_chunk = max(int(metadata.get("chunk", 0)) for _, _, metadata in records)
    for chunk_id, document, metadata in records:
        chunk_index = int(metadata.get("chunk", 0))
        section = str(metadata.get("section") or "unknown")
        normalized = " ".join(document.split())
        reasons = []
        if chunk_index <= 3:
            reasons.append("opening")
        if chunk_index >= last_chunk - 4:
            reasons.append("closing")
        if section in {"abstract", "conclusion"}:
            reasons.append(section)
        if HEADING.search(normalized):
            reasons.append("heading")
        if KEY_TERMS.search(normalized):
            reasons.append("scope_or_gap_term")
        if not reasons:
            continue
        selected.append(
            {
                "chunk_id": chunk_id,
                "chunk_index": chunk_index,
                "section": section,
                "selection_reasons": sorted(set(reasons)),
                "preview": normalized[: args.preview_chars],
            }
        )

    nonreference_records = [
        (chunk_id, document, metadata)
        for chunk_id, document, metadata in records
        if str(metadata.get("section") or "") != "references"
    ]
    design_evidence = {}
    for group_name, phrases in DESIGN_EVIDENCE_GROUPS.items():
        scored = []
        for chunk_id, document, metadata in nonreference_records:
            normalized = " ".join(document.split())
            folded = normalized.casefold()
            matched = [phrase for phrase in phrases if phrase in folded]
            if not matched:
                continue
            scored.append(
                (
                    len(matched),
                    int(metadata.get("chunk", 0)),
                    {
                        "chunk_id": chunk_id,
                        "chunk_index": int(metadata.get("chunk", 0)),
                        "section": str(metadata.get("section") or "unknown"),
                        "matched_phrases": matched,
                        "preview": normalized[: args.preview_chars],
                    },
                )
            )
        design_evidence[group_name] = [
            item[2]
            for item in sorted(
                scored,
                key=lambda item: (-item[0], item[1]),
            )[:4]
        ]

    selected_by_index = {item["chunk_index"]: item for item in selected}
    for group_name, group_records in design_evidence.items():
        for record in group_records:
            chunk_index = record["chunk_index"]
            reason = f"design_evidence:{group_name}"
            if chunk_index in selected_by_index:
                selected_by_index[chunk_index]["selection_reasons"] = sorted(
                    {
                        *selected_by_index[chunk_index]["selection_reasons"],
                        reason,
                    }
                )
                continue
            selected_by_index[chunk_index] = {
                "chunk_id": record["chunk_id"],
                "chunk_index": chunk_index,
                "section": record["section"],
                "selection_reasons": [reason],
                "preview": record["preview"],
            }
    selected = [
        selected_by_index[index] for index in sorted(selected_by_index)
    ]

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(
            {
                "source": args.source,
                "title": records[0][2].get("title", ""),
                "doi": records[0][2].get("doi", ""),
                "chunk_count": len(records),
                "selected_chunk_count": len(selected),
                "selected_chunks": selected,
                "design_evidence": design_evidence,
            },
            ensure_ascii=True,
            indent=2,
        )
        + "\n"
    )
    print(
        f"PASS: selected {len(selected)} of {len(records)} chunks for "
        f"{args.source}"
    )


if __name__ == "__main__":
    main()

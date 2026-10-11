#!/usr/bin/env python3
"""Build compact, hash-traceable snapshots for cited task-design chunks."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import chromadb


ROOT = Path(__file__).resolve().parents[1]


def load_jsonl(path: Path) -> list[dict]:
    return [
        json.loads(line)
        for line in path.read_text().splitlines()
        if line.strip()
    ]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--chroma-path", default="data/chroma")
    parser.add_argument(
        "--collection",
        default=(
            "rag_documents_bge_large_en_v1_5_"
            "sent256_overlap2_corpus434_repaired_v1"
        ),
    )
    parser.add_argument("--preview-chars", type=int, default=320)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    anchors = {
        record["task_id"]: record["primary_anchor"]
        for record in load_jsonl(ROOT / "input" / "anchor_reviews.jsonl")
    }
    provenance = load_jsonl(
        ROOT / "provenance" / "task_design_provenance.jsonl"
    )
    collection = chromadb.PersistentClient(
        path=args.chroma_path
    ).get_collection(args.collection)

    for record in provenance:
        task_id = record["task_id"]
        anchor = anchors[task_id]
        required_indices = sorted(
            {
                index
                for indices in record["design_basis"].values()
                for index in indices
            }
        )
        result = collection.get(
            where={"source": anchor["corpus_source"]},
            include=["documents", "metadatas"],
        )
        chunks = {
            int(metadata.get("chunk", 0)): (
                chunk_id,
                text,
                metadata,
            )
            for chunk_id, text, metadata in zip(
                result["ids"],
                result["documents"],
                result["metadatas"],
            )
        }
        missing = set(required_indices) - set(chunks)
        if missing:
            raise RuntimeError(f"{task_id}: missing chunk indices {sorted(missing)}")

        selected = []
        for index in required_indices:
            chunk_id, text, metadata = chunks[index]
            normalized = " ".join(text.split())
            selected.append(
                {
                    "chunk_id": chunk_id,
                    "chunk_index": index,
                    "section": str(metadata.get("section") or "unknown"),
                    "chunk_sha256": hashlib.sha256(
                        text.encode("utf-8")
                    ).hexdigest(),
                    "preview": normalized[: args.preview_chars],
                }
            )

        output_path = ROOT / record["source_snapshot"]
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(
            json.dumps(
                {
                    "task_id": task_id,
                    "source": anchor["corpus_source"],
                    "title": anchor["title"],
                    "doi": anchor["doi"],
                    "collection": args.collection,
                    "source_chunk_count": len(chunks),
                    "selected_chunk_count": len(selected),
                    "preview_chars": args.preview_chars,
                    "selected_chunks": selected,
                },
                ensure_ascii=True,
                indent=2,
            )
            + "\n"
        )
        print(
            f"PASS: {task_id}: wrote {len(selected)} compact design chunks."
        )


if __name__ == "__main__":
    main()

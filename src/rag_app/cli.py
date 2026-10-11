from __future__ import annotations

import argparse
import sys
import textwrap

from .config import get_settings
from .ingest import ingest_documents
from .rag import answer, retrieve


def cmd_ingest() -> None:
    settings = get_settings()
    count = ingest_documents(settings)
    if count == 0:
        print(f"No supported documents found in {settings.raw_data_dir}")
        return
    print(f"Indexed {count} chunks into {settings.chroma_dir}")


def cmd_retrieve(question: str) -> None:
    settings = get_settings()
    hits = retrieve(settings, question)
    if not hits:
        print("No results found. Run ingest first or add documents to data/raw.")
        return

    for index, hit in enumerate(hits, start=1):
        title = hit.get("title") or hit["source"]
        year = hit.get("year") or "n.d."
        first_author = hit.get("first_author") or "Unknown"
        section = hit.get("section") or "unknown"
        citation = hit.get("citation_acs") or f"{first_author} ({year}) {title}"
        source_mode = hit.get("retrieval_source") or "dense"
        print(
            f"\n[{index}] {citation} "
            f"section={section} chunk={hit['chunk']} distance={hit['distance']:.4f} "
            f"rerank={hit.get('rerank_score', 0):.4f} source={source_mode} "
            f"reference_like={hit.get('reference_like', False)} "
            f"dense_rank={hit.get('dense_rank')} bm25_rank={hit.get('bm25_rank')} "
            f"llm_rank={hit.get('llm_rerank_rank')} "
            f"llm_score={hit.get('llm_relevance_score')}"
        )
        if hit.get("llm_reason"):
            print(f"llm_reason={hit['llm_reason']}")
        if hit.get("llm_evidence_type"):
            print(f"llm_evidence_type={hit['llm_evidence_type']}")
        if hit.get("llm_covered_evidence"):
            print(f"llm_covered_evidence={'; '.join(hit['llm_covered_evidence'])}")
        if hit.get("llm_redundancy_risk"):
            print(f"llm_redundancy_risk={hit['llm_redundancy_risk']}")
        print(f"source={hit['source']}")
        print(textwrap.shorten(hit["text"].replace("\n", " "), width=700, placeholder="..."))


def cmd_ask(question: str) -> None:
    settings = get_settings()
    response, hits = answer(settings, question)
    print(response)
    print("\nSources:")
    for index, hit in enumerate(hits, start=1):
        title = hit.get("title") or hit["source"]
        year = hit.get("year") or "n.d."
        first_author = hit.get("first_author") or "Unknown"
        section = hit.get("section") or "unknown"
        citation = hit.get("citation_acs") or f"{first_author} ({year}) {title}"
        source_mode = hit.get("retrieval_source") or "dense"
        print(
            f"[{index}] {citation} "
            f"section={section} chunk={hit['chunk']} distance={hit['distance']:.4f} "
            f"rerank={hit.get('rerank_score', 0):.4f} source={source_mode} "
            f"reference_like={hit.get('reference_like', False)} "
            f"dense_rank={hit.get('dense_rank')} bm25_rank={hit.get('bm25_rank')} "
            f"llm_rank={hit.get('llm_rerank_rank')} "
            f"llm_score={hit.get('llm_relevance_score')}"
        )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Local RAG project")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("ingest", help="Load documents and build/update vector index")

    retrieve_parser = subparsers.add_parser("retrieve", help="Retrieve relevant chunks")
    retrieve_parser.add_argument("question", help="Question to search for")

    ask_parser = subparsers.add_parser("ask", help="Answer a question using retrieved context")
    ask_parser.add_argument("question", help="Question to answer")

    return parser


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = build_parser()
    args = parser.parse_args()

    if args.command == "ingest":
        cmd_ingest()
    elif args.command == "retrieve":
        cmd_retrieve(args.question)
    elif args.command == "ask":
        cmd_ask(args.question)
    else:
        parser.error(f"Unknown command: {args.command}")

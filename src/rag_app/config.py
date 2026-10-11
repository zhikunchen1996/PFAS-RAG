from dataclasses import dataclass
from pathlib import Path
import os
from typing import Optional

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def resolve_embedding_device(value: Optional[str]) -> str:
    requested = (value or "auto").strip().lower()
    if requested not in {"", "auto"}:
        return requested

    try:
        import torch
    except Exception:
        return "cpu"

    if getattr(torch.backends, "mps", None) is not None and torch.backends.mps.is_available():
        return "mps"
    if torch.cuda.is_available():
        return "cuda"
    return "cpu"


@dataclass(frozen=True)
class Settings:
    raw_data_dir: Path = PROJECT_ROOT / "data" / "raw"
    chroma_dir: Path = PROJECT_ROOT / "data" / "chroma"
    collection_name: str = "rag_documents_bge_large_en_v1_5_sent256_overlap2"
    embedding_model: str = "BAAI/bge-large-en-v1.5"
    embedding_device: str = "auto"
    openai_model: str = "gpt-4o-mini"
    chunk_size: int = 256
    chunk_overlap: int = 0
    chunk_overlap_sentences: int = 2
    retrieval_mode: str = "hybrid"
    retrieval_k: int = 30
    bm25_k: int = 30
    reference_filter: bool = True
    llm_rerank: bool = False
    llm_rerank_mode: str = "score"
    llm_rerank_k: int = 30
    top_k: int = 10
    include_source_context_in_judge: bool = True


def get_settings() -> Settings:
    load_dotenv(PROJECT_ROOT / ".env", override=False)
    return Settings(
        collection_name=os.getenv("COLLECTION_NAME", "rag_documents_bge_large_en_v1_5_sent256_overlap2"),
        embedding_model=os.getenv("EMBEDDING_MODEL", "BAAI/bge-large-en-v1.5"),
        embedding_device=resolve_embedding_device(os.getenv("EMBEDDING_DEVICE", "auto")),
        openai_model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        chunk_size=int(os.getenv("CHUNK_SIZE", "256")),
        chunk_overlap=int(os.getenv("CHUNK_OVERLAP", "0")),
        chunk_overlap_sentences=int(os.getenv("CHUNK_OVERLAP_SENTENCES", "2")),
        retrieval_mode=os.getenv("RETRIEVAL_MODE", "hybrid"),
        retrieval_k=int(os.getenv("RETRIEVAL_K", "30")),
        bm25_k=int(os.getenv("BM25_K", "30")),
        reference_filter=os.getenv("REFERENCE_FILTER", "true").lower() in {"1", "true", "yes", "y"},
        llm_rerank=os.getenv("LLM_RERANK", "false").lower() in {"1", "true", "yes", "y"},
        llm_rerank_mode=os.getenv("LLM_RERANK_MODE", "score").lower(),
        llm_rerank_k=int(os.getenv("LLM_RERANK_K", "30")),
        top_k=int(os.getenv("TOP_K", "10")),
        include_source_context_in_judge=os.getenv("INCLUDE_SOURCE_CONTEXT_IN_JUDGE", "true").lower()
        in {"1", "true", "yes", "y"},
    )

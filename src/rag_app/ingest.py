from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv
import hashlib
import re

import chromadb
from chromadb.utils import embedding_functions
from docx import Document
from pypdf import PdfReader
from tqdm import tqdm

from .config import Settings
from .text import chunk_text, normalize_text


SUPPORTED_EXTENSIONS = {".txt", ".md", ".pdf", ".docx"}
SECTION_PATTERNS = [
    ("abstract", re.compile(r"\babstract\b", re.IGNORECASE)),
    ("introduction", re.compile(r"\b(?:1\.?\s*)?introduction\b", re.IGNORECASE)),
    ("methods", re.compile(r"\b(?:materials\s+and\s+methods|methods|methodology|experimental|experiments)\b", re.IGNORECASE)),
    ("results", re.compile(r"\b(?:results|results\s+and\s+discussion)\b", re.IGNORECASE)),
    ("discussion", re.compile(r"\bdiscussion\b", re.IGNORECASE)),
    ("conclusion", re.compile(r"\b(?:conclusions?|summary)\b", re.IGNORECASE)),
    ("references", re.compile(r"\b(?:references|bibliography)\b", re.IGNORECASE)),
]


@dataclass(frozen=True)
class LoadedDocument:
    path: Path
    text: str


def load_text_file(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def load_pdf(path: Path) -> str:
    reader = PdfReader(str(path))
    pages = []
    for page in reader.pages:
        pages.append(page.extract_text() or "")
    return "\n\n".join(pages)


def load_docx(path: Path) -> str:
    document = Document(str(path))
    return "\n".join(paragraph.text for paragraph in document.paragraphs)


def load_document(path: Path) -> LoadedDocument:
    suffix = path.suffix.lower()
    if suffix in {".txt", ".md"}:
        text = load_text_file(path)
    elif suffix == ".pdf":
        text = load_pdf(path)
    elif suffix == ".docx":
        text = load_docx(path)
    else:
        raise ValueError(f"Unsupported file type: {path}")

    return LoadedDocument(path=path, text=normalize_text(text))


def find_documents(raw_data_dir: Path) -> list[Path]:
    if not raw_data_dir.exists():
        return []

    return sorted(
        path
        for path in raw_data_dir.rglob("*")
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS
    )


def make_source(path: Path, raw_data_dir: Path) -> str:
    return path.relative_to(raw_data_dir).as_posix()


def detect_section(chunk: str, previous_section: str = "unknown") -> str:
    head = chunk[:800]
    best_section = previous_section
    best_position: int | None = None
    for section, pattern in SECTION_PATTERNS:
        match = pattern.search(head)
        if match and (best_position is None or match.start() < best_position):
            best_section = section
            best_position = match.start()

    if best_section == "unknown":
        lower = chunk[:2000].lower()
        if lower.lstrip().startswith(("references", "bibliography")):
            return "references"
        if lower.count(" doi:") + lower.count(" et al.") >= 8:
            return "references"

    return best_section


def load_raw_manifest(raw_data_dir: Path) -> dict[str, dict[str, str | bool]]:
    manifest_path = raw_data_dir.parent / "raw_manifest.csv"
    if not manifest_path.exists():
        return {}

    records: dict[str, dict[str, str | bool]] = {}
    with manifest_path.open("r", encoding="utf-8-sig", newline="") as file:
        for row in csv.DictReader(file):
            source = (row.get("source") or "").strip()
            if not source:
                continue

            metadata: dict[str, str | bool] = {}
            for key in (
                "year",
                "first_author",
                "title",
                "doi",
                "journal",
                "volume",
                "issue",
                "pages",
                "publisher",
                "published_year",
                "published_date",
                "authors",
                "citation_apa",
                "citation_acs",
                "metadata_source",
            ):
                value = (row.get(key) or "").strip()
                if value:
                    metadata[key] = value

            needs_review = (row.get("needs_review") or "").strip().lower()
            if needs_review:
                metadata["needs_review"] = needs_review in {"1", "true", "yes", "y"}

            records[source] = metadata

    return records


def make_chunk_id(path: Path, index: int, text: str) -> str:
    digest = hashlib.sha1(f"{path}:{index}:{text}".encode("utf-8")).hexdigest()
    return digest


def get_collection(settings: Settings):
    client = chromadb.PersistentClient(path=str(settings.chroma_dir))
    embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=settings.embedding_model,
        device=settings.embedding_device,
    )
    return client.get_or_create_collection(
        name=settings.collection_name,
        embedding_function=embedding_fn,
        metadata={"hnsw:space": "cosine"},
    )


def ingest_documents(settings: Settings) -> int:
    settings.raw_data_dir.mkdir(parents=True, exist_ok=True)
    settings.chroma_dir.mkdir(parents=True, exist_ok=True)

    paths = find_documents(settings.raw_data_dir)
    if not paths:
        return 0

    collection = get_collection(settings)
    manifest = load_raw_manifest(settings.raw_data_dir)
    total_chunks = 0

    for path in tqdm(paths, desc="Indexing documents"):
        document = load_document(path)
        chunks = chunk_text(
            document.text,
            settings.chunk_size,
            settings.chunk_overlap,
            settings.chunk_overlap_sentences,
        )
        if not chunks:
            continue

        source = make_source(path, settings.raw_data_dir)
        source_metadata = manifest.get(source, {})
        ids = [make_chunk_id(path, index, text) for index, text in enumerate(chunks)]
        metadatas = []
        current_section = "unknown"
        for index, text in enumerate(chunks):
            current_section = detect_section(text, current_section)
            metadatas.append(
                {"source": source, "chunk": index, "section": current_section, **source_metadata}
            )

        collection.upsert(ids=ids, documents=chunks, metadatas=metadatas)
        total_chunks += len(chunks)

    return total_chunks

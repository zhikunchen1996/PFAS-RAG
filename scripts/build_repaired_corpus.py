from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
from pathlib import Path
import re
import shutil
from typing import Any
from urllib.parse import quote
from urllib.request import Request, urlopen

import chromadb
from chromadb.utils import embedding_functions


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MANIFEST_FIELDS = [
    "source",
    "year",
    "first_author",
    "title",
    "doi",
    "needs_review",
    "file_size_bytes",
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
    "metadata_score",
]
CHROMA_METADATA_FIELDS = [
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
]


def read_csv(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader), list(reader.fieldnames or [])


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def crossref_work(doi: str) -> dict[str, Any]:
    url = f"https://api.crossref.org/works/{quote(doi, safe='')}"
    request = Request(url, headers={"User-Agent": "pfas-rag-corpus-repair/1.0"})
    with urlopen(request, timeout=30) as response:
        payload = json.loads(response.read().decode("utf-8"))
    if payload.get("status") != "ok":
        raise RuntimeError(f"Crossref did not resolve DOI {doi}")
    return payload["message"]


def first(value: Any) -> str:
    if isinstance(value, list):
        return str(value[0]) if value else ""
    return str(value or "")


def clean_markup(value: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", value or "")).strip()


def publication_date(work: dict[str, Any]) -> tuple[str, str]:
    for key in ("published-print", "published-online", "published", "issued"):
        parts = work.get(key, {}).get("date-parts", [])
        if parts and parts[0]:
            values = [str(value) for value in parts[0]]
            return values[0], "-".join(values)
    return "", ""


def author_name(author: dict[str, Any], compact: bool = False) -> str:
    family = str(author.get("family") or "")
    given = str(author.get("given") or "")
    if not family:
        return given or str(author.get("name") or "")
    initials = [f"{part[0]}." for part in given.replace("-", " ").split() if part]
    separator = "" if compact else " "
    return f"{family}, {separator.join(initials)}" if initials else family


def author_list(authors: list[dict[str, Any]], compact: bool = False) -> str:
    names = [author_name(author, compact) for author in authors]
    names = [name for name in names if name]
    return "; ".join(names[:10]) + ("; et al." if len(names) > 10 else "")


def apply_crossref(row: dict[str, str], work: dict[str, Any], doi: str) -> dict[str, str]:
    corrected = dict(row)
    year, date = publication_date(work)
    authors = work.get("author") or []
    corrected.update(
        {
            "year": year or corrected.get("year", ""),
            "first_author": str(authors[0].get("family") or "") if authors else corrected.get("first_author", ""),
            "title": clean_markup(first(work.get("title"))) or corrected.get("title", ""),
            "doi": doi.lower(),
            "needs_review": "false",
            "journal": clean_markup(first(work.get("container-title"))),
            "volume": str(work.get("volume") or ""),
            "issue": str(work.get("issue") or ""),
            "pages": str(work.get("page") or ""),
            "publisher": html.unescape(str(work.get("publisher") or "")),
            "published_year": year,
            "published_date": date,
            "authors": author_list(authors),
            "metadata_source": "crossref_doi_verified_corpus434_repair",
            "metadata_score": "",
        }
    )
    apa_authors = corrected["authors"] or corrected["first_author"] or "Unknown"
    journal_bits = corrected["journal"]
    if corrected["volume"]:
        journal_bits += f", {corrected['volume']}"
        if corrected["issue"]:
            journal_bits += f"({corrected['issue']})"
    if corrected["pages"]:
        journal_bits += f", {corrected['pages']}"
    corrected["citation_apa"] = (
        f"{apa_authors} ({year or 'n.d.'}). {corrected['title']}. {journal_bits}. "
        f"https://doi.org/{corrected['doi']}"
    ).strip()
    acs_authors = author_list(authors, compact=True) or corrected["first_author"] or "Unknown"
    acs_journal = " ".join(
        value for value in (corrected["journal"], year, corrected["volume"], corrected["pages"]) if value
    )
    corrected["citation_acs"] = (
        f"{acs_authors}. {corrected['title']}. {acs_journal}. DOI: {corrected['doi']}."
    )
    return corrected


def duplicate_dois(rows: list[dict[str, str]]) -> dict[str, list[str]]:
    grouped: dict[str, list[str]] = {}
    for row in rows:
        doi = row.get("doi", "").strip().lower()
        if doi:
            grouped.setdefault(doi, []).append(row["source"])
    return {doi: sources for doi, sources in grouped.items() if len(sources) > 1}


def copy_collection(
    chroma_path: Path,
    source_name: str,
    target_name: str,
    manifest: dict[str, dict[str, str]],
    removed_sources: set[str],
    replace: bool,
) -> tuple[int, int]:
    client = chromadb.PersistentClient(path=str(chroma_path))
    existing = {collection.name for collection in client.list_collections()}
    if target_name in existing:
        if not replace:
            raise RuntimeError(f"Target collection already exists: {target_name}; use --replace")
        client.delete_collection(target_name)
    source = client.get_collection(source_name)
    source_embedding = source.configuration_json.get("embedding_function", {}).get("config", {})
    embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=source_embedding.get("model_name", "BAAI/bge-large-en-v1.5"),
        device=source_embedding.get("device", "cpu"),
        normalize_embeddings=bool(source_embedding.get("normalize_embeddings", False)),
    )
    target = client.create_collection(
        target_name,
        embedding_function=embedding_function,
        metadata={"hnsw:space": "cosine"},
    )
    data = source.get(include=["documents", "metadatas", "embeddings"])
    kept: list[tuple[str, str, dict[str, Any], Any]] = []
    removed_chunks = 0
    for item_id, document, metadata, embedding in zip(
        data["ids"], data["documents"], data["metadatas"], data["embeddings"]
    ):
        source_id = str(metadata.get("source") or "")
        if source_id in removed_sources:
            removed_chunks += 1
            continue
        row = manifest[source_id]
        updated = dict(metadata)
        for field in CHROMA_METADATA_FIELDS:
            value = row.get(field, "").strip()
            if value:
                updated[field] = value
            else:
                updated.pop(field, None)
        updated["needs_review"] = row.get("needs_review", "").lower() in {"1", "true", "yes", "y"}
        kept.append((item_id, document, updated, embedding))
    for start in range(0, len(kept), 500):
        batch = kept[start : start + 500]
        target.add(
            ids=[item[0] for item in batch],
            documents=[item[1] for item in batch],
            metadatas=[item[2] for item in batch],
            embeddings=[item[3] for item in batch],
        )
    return len(kept), removed_chunks


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a versioned PFAS corpus with repaired metadata.")
    parser.add_argument("--manifest", default="data/raw_manifest.csv")
    parser.add_argument("--corrections", default="corpus/corpus434_repaired_v1/corrections.json")
    parser.add_argument("--output-manifest", default="corpus/corpus434_repaired_v1/raw_manifest.csv")
    parser.add_argument("--chroma-path", default="data/chroma")
    parser.add_argument("--replace", action="store_true")
    parser.add_argument("--skip-collection", action="store_true")
    parser.add_argument(
        "--promote-manifest",
        action="store_true",
        help="Back up the source manifest beside the repaired version, then make the repaired manifest active.",
    )
    parser.add_argument("--promote-to", default="data/raw_manifest.csv")
    args = parser.parse_args()

    manifest_path = PROJECT_ROOT / args.manifest
    corrections_path = PROJECT_ROOT / args.corrections
    output_path = PROJECT_ROOT / args.output_manifest
    rules = json.loads(corrections_path.read_text(encoding="utf-8"))
    rows, fields = read_csv(manifest_path)
    fields = list(dict.fromkeys(fields + MANIFEST_FIELDS))
    by_source = {row["source"]: row for row in rows}
    removed_sources = {item["source"] for item in rules["remove_sources"]}

    correction_log = []
    for correction in rules["metadata_corrections"]:
        source = correction["source"]
        if source not in by_source:
            raise KeyError(f"Correction source missing from manifest: {source}")
        before = dict(by_source[source])
        work = crossref_work(correction["doi"])
        by_source[source] = apply_crossref(before, work, correction["doi"])
        correction_log.append(
            {
                "source": source,
                "before_doi": before.get("doi", ""),
                "after_doi": by_source[source]["doi"],
                "after_title": by_source[source]["title"],
                "reason": correction["reason"],
            }
        )

    repaired_rows = [by_source[row["source"]] for row in rows if row["source"] not in removed_sources]
    duplicates = duplicate_dois(repaired_rows)
    if duplicates:
        raise RuntimeError(f"Duplicate DOI groups remain after repair: {duplicates}")
    write_csv(output_path, repaired_rows, fields)

    kept_chunks = 0
    removed_chunks = 0
    if not args.skip_collection:
        kept_chunks, removed_chunks = copy_collection(
            PROJECT_ROOT / args.chroma_path,
            rules["source_collection"],
            rules["target_collection"],
            {row["source"]: row for row in repaired_rows},
            removed_sources,
            args.replace,
        )

    report = {
        "version": rules["version"],
        "source_manifest": args.manifest,
        "source_manifest_sha256": sha256(manifest_path),
        "output_manifest": args.output_manifest,
        "output_manifest_sha256": sha256(output_path),
        "source_records": len(rows),
        "repaired_records": len(repaired_rows),
        "removed_sources": sorted(removed_sources),
        "metadata_corrections": correction_log,
        "remaining_duplicate_doi_groups": duplicates,
        "source_collection": rules["source_collection"],
        "target_collection": rules["target_collection"],
        "kept_chunks": kept_chunks,
        "removed_chunks": removed_chunks,
    }
    report_path = output_path.parent / "repair_report.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.promote_manifest:
        backup_path = output_path.parent / "raw_manifest_original.csv"
        promote_path = PROJECT_ROOT / args.promote_to
        if not backup_path.exists() and promote_path.exists():
            shutil.copy2(promote_path, backup_path)
        shutil.copy2(output_path, promote_path)
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

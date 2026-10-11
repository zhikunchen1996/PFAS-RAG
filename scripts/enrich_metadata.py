from __future__ import annotations

import argparse
import csv
from datetime import datetime
import json
from pathlib import Path
import shutil
import time
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen


CROSSREF_API = "https://api.crossref.org/works"
DEFAULT_FIELDS = [
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


def request_json(url: str, user_agent: str, timeout: int = 30) -> dict:
    request = Request(url, headers={"User-Agent": user_agent})
    with urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def crossref_by_doi(doi: str, mailto: str, user_agent: str) -> dict | None:
    if not doi:
        return None
    url = f"{CROSSREF_API}/{quote(doi, safe='')}"
    if mailto:
        url = f"{url}?{urlencode({'mailto': mailto})}"
    data = request_json(url, user_agent)
    if data.get("status") != "ok":
        return None
    return data.get("message")


def crossref_by_title(title: str, year: str, mailto: str, user_agent: str) -> dict | None:
    params = {
        "query.title": title,
        "rows": "1",
    }
    if year and year != "0000":
        params["filter"] = f"from-pub-date:{year},until-pub-date:{year}"
    if mailto:
        params["mailto"] = mailto
    url = f"{CROSSREF_API}?{urlencode(params)}"
    data = request_json(url, user_agent)
    items = data.get("message", {}).get("items", [])
    return items[0] if items else None


def first(value: object) -> str:
    if isinstance(value, list) and value:
        return str(value[0])
    return str(value or "")


def published_parts(work: dict) -> tuple[str, str]:
    for key in ("published-print", "published-online", "published", "issued"):
        parts = work.get(key, {}).get("date-parts", [])
        if parts and parts[0]:
            date_parts = [str(part) for part in parts[0]]
            return date_parts[0], "-".join(date_parts)
    return "", ""


def format_author(author: dict) -> str:
    family = author.get("family") or ""
    given = author.get("given") or ""
    if family and given:
        initials = " ".join(f"{part[0]}." for part in given.replace("-", " ").split() if part)
        return f"{family}, {initials}"
    return family or given or author.get("name", "")


def format_author_acs(author: dict) -> str:
    family = author.get("family") or ""
    given = author.get("given") or ""
    if family and given:
        initials = "".join(f"{part[0]}." for part in given.replace("-", " ").split() if part)
        return f"{family}, {initials}"
    return family or given or author.get("name", "")


def format_author_list(authors: list[dict], style: str) -> str:
    formatter = format_author_acs if style == "acs" else format_author
    names = [formatter(author) for author in authors if formatter(author)]
    if not names:
        return ""
    if len(names) > 10:
        return "; ".join(names[:10]) + "; et al."
    return "; ".join(names)


def citation_apa(row: dict) -> str:
    authors = row.get("authors") or row.get("first_author") or "Unknown"
    year = row.get("published_year") or row.get("year") or "n.d."
    title = row.get("title") or ""
    journal = row.get("journal") or ""
    volume = row.get("volume") or ""
    issue = row.get("issue") or ""
    pages = row.get("pages") or ""
    doi = row.get("doi") or ""

    issue_text = f"({issue})" if issue else ""
    journal_bits = f"{journal}, {volume}{issue_text}" if journal and volume else journal
    if pages:
        journal_bits = f"{journal_bits}, {pages}" if journal_bits else pages
    doi_text = f" https://doi.org/{doi}" if doi else ""
    return f"{authors} ({year}). {title}. {journal_bits}.{doi_text}".strip()


def citation_acs(row: dict) -> str:
    authors = row.get("authors") or row.get("first_author") or "Unknown"
    title = row.get("title") or ""
    journal = row.get("journal") or ""
    year = row.get("published_year") or row.get("year") or ""
    volume = row.get("volume") or ""
    pages = row.get("pages") or ""
    doi = row.get("doi") or ""

    parts = [authors, title]
    journal_text = " ".join(part for part in (journal, year, volume, pages) if part)
    if journal_text:
        parts.append(journal_text)
    if doi:
        parts.append(f"DOI: {doi}")
    return ". ".join(part.strip(". ") for part in parts if part).strip() + "."


def enrich_row(row: dict, work: dict, source: str) -> dict:
    year, date = published_parts(work)
    authors = work.get("author") or []
    doi = (work.get("DOI") or row.get("doi") or "").lower()

    row["doi"] = doi
    row["journal"] = html_unescape(first(work.get("container-title")))
    row["volume"] = str(work.get("volume") or "")
    row["issue"] = str(work.get("issue") or "")
    row["pages"] = str(work.get("page") or "")
    row["publisher"] = html_unescape(str(work.get("publisher") or ""))
    row["published_year"] = year
    row["published_date"] = date
    row["authors"] = format_author_list(authors, "apa")
    row["citation_apa"] = citation_apa(row)
    row["citation_acs"] = citation_acs({**row, "authors": format_author_list(authors, "acs")})
    row["metadata_source"] = source
    row["metadata_score"] = str(work.get("score") or "")

    if year and (not row.get("year") or row.get("year") == "0000"):
        row["year"] = year
    if authors and (not row.get("first_author") or row.get("first_author") == "Unknown"):
        row["first_author"] = authors[0].get("family") or row.get("first_author", "")

    return row


def html_unescape(value: str) -> str:
    import html

    return html.unescape(value or "")


def main() -> None:
    parser = argparse.ArgumentParser(description="Enrich raw_manifest.csv with Crossref metadata.")
    parser.add_argument("--manifest", default="data/raw_manifest.csv")
    parser.add_argument("--mailto", default="", help="Email for Crossref polite pool.")
    parser.add_argument("--limit", type=int, default=0, help="Limit rows for testing; 0 means all rows.")
    parser.add_argument("--sleep", type=float, default=0.15, help="Delay between Crossref requests.")
    parser.add_argument("--missing-only", action="store_true", help="Only enrich rows missing journal/citation fields.")
    args = parser.parse_args()

    manifest_path = Path(args.manifest)
    backup_path = manifest_path.with_suffix(
        f".backup-{datetime.now().strftime('%Y%m%d-%H%M%S')}.csv"
    )
    shutil.copy2(manifest_path, backup_path)

    with manifest_path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        fieldnames = list(reader.fieldnames or [])

    for field in DEFAULT_FIELDS:
        if field not in fieldnames:
            fieldnames.append(field)

    user_agent = "rag-project-metadata-enricher/0.1"
    if args.mailto:
        user_agent = f"{user_agent} (mailto:{args.mailto})"

    enriched = 0
    failed = 0
    processed = 0
    for row in rows:
        if args.limit and processed >= args.limit:
            break
        if args.missing_only and row.get("citation_apa") and row.get("journal"):
            continue

        processed += 1
        work = None
        source = ""
        try:
            if row.get("doi"):
                work = crossref_by_doi(row["doi"], args.mailto, user_agent)
                source = "crossref_doi" if work else ""
            if not work and row.get("title"):
                work = crossref_by_title(row["title"], row.get("year", ""), args.mailto, user_agent)
                source = "crossref_title" if work else ""
            if work:
                enrich_row(row, work, source)
                enriched += 1
            else:
                failed += 1
        except Exception as exc:
            row["metadata_source"] = f"error: {type(exc).__name__}"
            failed += 1
        time.sleep(args.sleep)

    with manifest_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Backup: {backup_path}")
    print(f"Processed: {processed}")
    print(f"Enriched: {enriched}")
    print(f"Failed/no match: {failed}")


if __name__ == "__main__":
    main()

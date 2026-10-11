#!/usr/bin/env python3
"""Validate the public corpus inventory and optional local source files."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data/raw_manifest.csv"
RAW_DIR = ROOT / "data/raw"
EXPECTED_RECORDS = 434
SUPPORTED_EXTENSIONS = {".pdf", ".docx", ".txt", ".md"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--require-files", action="store_true")
    parser.add_argument("--manifest", type=Path, default=MANIFEST)
    parser.add_argument("--raw-dir", type=Path, default=RAW_DIR)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    manifest = args.manifest.expanduser().resolve()
    raw_dir = args.raw_dir.expanduser().resolve()
    with manifest.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    if len(rows) != EXPECTED_RECORDS:
        raise SystemExit(f"Expected {EXPECTED_RECORDS} manifest records, found {len(rows)}")

    sources = [str(row.get("source") or "").strip() for row in rows]
    if any(not source for source in sources):
        raise SystemExit("Manifest contains an empty source")
    if len(set(sources)) != len(sources):
        raise SystemExit("Manifest contains duplicate sources")

    for source, row in zip(sources, rows, strict=True):
        path = PurePosixPath(source)
        if path.is_absolute() or ".." in path.parts:
            raise SystemExit(f"Source is not repository-relative: {source}")
        if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            raise SystemExit(f"Unsupported source extension: {source}")
        try:
            if int(row.get("file_size_bytes") or 0) <= 0:
                raise ValueError
        except ValueError as exc:
            raise SystemExit(f"Invalid file_size_bytes for {source}") from exc

    if args.require_files:
        local = {
            path.relative_to(raw_dir).as_posix(): path
            for path in raw_dir.rglob("*")
            if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS
        }
        missing = sorted(set(sources) - set(local))
        extra = sorted(set(local) - set(sources))
        if missing or extra:
            raise SystemExit(
                f"Source inventory mismatch: missing={len(missing)}, extra={len(extra)}"
            )
        for row in rows:
            source = str(row["source"]).strip()
            expected_size = int(row["file_size_bytes"])
            actual_size = local[source].stat().st_size
            if actual_size != expected_size:
                raise SystemExit(
                    f"File-size mismatch for {source}: expected {expected_size}, "
                    f"found {actual_size}"
                )

    mode = "manifest and local files" if args.require_files else "public manifest"
    print(f"PASS: {mode} contain {len(rows)} unique corpus records")


if __name__ == "__main__":
    main()

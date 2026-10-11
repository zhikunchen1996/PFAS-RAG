#!/usr/bin/env python3
"""Build or verify the immutable professional-review package manifest."""

from __future__ import annotations

import argparse
from pathlib import Path

from review_runtime import PACKAGE_ROOT, load_json, sha256_file, utc_now, write_json


MANIFEST_NAME = "freeze_manifest.json"


def package_files() -> list[Path]:
    files = []
    for path in PACKAGE_ROOT.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(PACKAGE_ROOT)
        if path.name == MANIFEST_NAME:
            continue
        if "__pycache__" in relative.parts or path.suffix == ".pyc":
            continue
        if path.name == ".DS_Store":
            continue
        files.append(path)
    return sorted(files)


def current_hashes() -> dict[str, str]:
    return {
        str(path.relative_to(PACKAGE_ROOT)): sha256_file(path)
        for path in package_files()
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--verify", action="store_true")
    parser.add_argument(
        "--release-id",
        default="professional-review-v3",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    path = PACKAGE_ROOT / MANIFEST_NAME
    hashes = current_hashes()
    if args.write:
        write_json(
            path,
            {
                "release_id": args.release_id,
                "created_at": utc_now(),
                "package_root_name": PACKAGE_ROOT.name,
                "file_count": len(hashes),
                "files": hashes,
            },
        )
        print(f"WROTE: {path} ({len(hashes)} files)")
        return
    manifest = load_json(path)
    if manifest.get("files") != hashes:
        missing = sorted(set(manifest.get("files", {})) - set(hashes))
        added = sorted(set(hashes) - set(manifest.get("files", {})))
        changed = sorted(
            key
            for key in set(hashes) & set(manifest.get("files", {}))
            if hashes[key] != manifest["files"][key]
        )
        raise RuntimeError(
            "Freeze manifest mismatch: "
            f"missing={missing}, added={added}, changed={changed}"
        )
    print(f"PASS: freeze manifest verified ({len(hashes)} files)")


if __name__ == "__main__":
    main()

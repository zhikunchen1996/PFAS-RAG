#!/usr/bin/env python3
"""Validate the deidentified professional-review expert package."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    manifest = json.loads((PACKAGE / "manifest.json").read_text())
    for relative, expected in manifest["files"].items():
        path = PACKAGE / relative
        assert path.is_file(), f"Missing package file: {relative}"
        assert sha256(path) == expected, f"Hash mismatch: {relative}"

    summary = json.loads((PACKAGE / "summary.json").read_text())
    assert summary["status"] == "complete"
    assert summary["judgments"] == 30
    assert summary["tasks"] == 10
    assert summary["candidate_appearances_per_system"] == 20
    assert summary["material_error_flags"] == 0

    expected = {
        "PFAS RAG vs Direct": {"PFAS RAG": 10.0, "Tie": 0, "Direct": 0.0},
        "Web Search vs Direct": {"Web Search": 10.0, "Tie": 0, "Direct": 0.0},
        "PFAS RAG vs Web Search": {"PFAS RAG": 4.0, "Tie": 2, "Web Search": 4.0},
    }
    observed = {row["pair"]: row for row in summary["pairwise"]}
    for pair, counts in expected.items():
        for label, value in counts.items():
            assert observed[pair][label] == value, f"Unexpected {pair}/{label}"

    assert len(summary["dimension_means"]) == 3
    assert {row["system"] for row in summary["dimension_means"]} == {
        "PFAS RAG",
        "Web Search",
        "Direct",
    }
    print("PASS: expert package hashes, design counts, and aggregates are valid")


if __name__ == "__main__":
    main()

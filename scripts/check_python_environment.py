#!/usr/bin/env python3
"""Verify the shared repository Python and core analysis dependencies."""

from __future__ import annotations

from importlib import metadata
import os
import platform
import sys
import tempfile
from pathlib import Path


cache_root = Path(tempfile.gettempdir()) / "rag-python-cache"
cache_root.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(cache_root / "matplotlib"))
os.environ.setdefault("XDG_CACHE_HOME", str(cache_root))


REQUIRED_PYTHON = (3, 12, 13)
REQUIRED_PACKAGES = {
    "chromadb": "1.5.9",
    "openai": "2.48.0",
    "python-dotenv": "1.2.2",
    "requests": "2.34.2",
    "sentence-transformers": "5.5.1",
    "pypdf": "6.13.2",
    "python-docx": "1.2.0",
    "tqdm": "4.68.2",
    "tiktoken": "0.13.0",
    "matplotlib": "3.11.1",
    "pandas": "2.3.3",
    "seaborn": "0.13.2",
}


def main() -> None:
    if sys.version_info[:3] != REQUIRED_PYTHON:
        raise SystemExit(
            f"Expected Python {'.'.join(map(str, REQUIRED_PYTHON))}, "
            f"found {platform.python_version()} at {sys.executable}"
        )

    failures = []
    for package, expected in REQUIRED_PACKAGES.items():
        actual = metadata.version(package)
        if actual != expected:
            failures.append(f"{package}: expected {expected}, found {actual}")

    if failures:
        raise SystemExit("Environment mismatch:\n- " + "\n- ".join(failures))

    print(f"Python {platform.python_version()}: OK")
    print(f"Interpreter: {sys.executable}")
    for package, expected in REQUIRED_PACKAGES.items():
        print(f"{package} {expected}: OK")


if __name__ == "__main__":
    main()

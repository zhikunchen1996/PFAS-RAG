from __future__ import annotations

import hashlib
import json
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
MANIFEST = PACKAGE / "completion_manifest.json"


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    files = manifest.get("files")
    if not isinstance(files, dict) or not files:
        raise RuntimeError("Completion manifest contains no files")
    for relative, expected in files.items():
        path = PACKAGE / relative
        if not path.is_file():
            raise RuntimeError(f"Missing completion artifact: {relative}")
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected:
            raise RuntimeError(f"Hash mismatch: {relative}")
    print(f"COMPLETION MANIFEST PASS: {len(files)} files")


if __name__ == "__main__":
    main()

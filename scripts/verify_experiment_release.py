"""Verify the exact inventory and hashes of an experiments-only export."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / 'release_manifest.json').read_text())
    assert manifest['release_profile'] == 'experiments-only'
    expected = set(manifest['files']) | {'release_manifest.json'}
    observed = {
        path.relative_to(root).as_posix()
        for path in root.rglob('*')
        if path.is_file()
        and not {'.git', '.venv', '__pycache__'}.intersection(path.relative_to(root).parts)
        and path.relative_to(root).parts[0] != 'outputs'
        and not path.relative_to(root).as_posix().startswith(('data/raw/', 'data/chroma/'))
        and path.name != '.env'
        and path.name != '.DS_Store'
    }
    assert observed == expected, f'Inventory mismatch: missing={expected - observed}, extra={observed - expected}'
    for relative, record in manifest['files'].items():
        path = root / relative
        assert not path.is_symlink(), f'Symlink in release: {relative}'
        assert path.stat().st_size == record['size_bytes'], f'Size mismatch: {relative}'
        assert hashlib.sha256(path.read_bytes()).hexdigest() == record['sha256'], f'Hash mismatch: {relative}'
    source = json.loads((root / manifest['formal_source_manifest']).read_text())
    frozen = json.loads((root / source['formal_anchor']).read_text())
    for relative, expected in source['files'].items():
        assert frozen['frozen_inputs'][relative] == expected, f'Invalid formal anchor: {relative}'
        assert hashlib.sha256((root / relative).read_bytes()).hexdigest() == expected, f'Formal source mismatch: {relative}'
    print(f"PASS: {len(manifest['files'])} experiment-release files match the manifest")
    print(f"PASS: {len(source['files'])} source files match the formal experimental freeze")
    print(f"Release status: {manifest['release_status']}")


if __name__ == '__main__':
    main()

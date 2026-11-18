"""Check source-field omissions and the distributed projection inventory."""
from pathlib import Path
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'reproduction/public_sources_v01'
MARKER = re.compile(r'\[SOURCE_TEXT_OMITTED sha256=[0-9a-f]{64}\]')
SOURCE_KEYS = {
    'text', 'preview', 'passage', 'full_chunk_text', 'complete_original_chunk',
    'exact_evidence_span', 'original_exact_evidence_span', 'evidence_span',
    'exact_support', 'registered_exact_span', 'new_verbatim_span', 'unit_exact_spans',
}


def check(value, key='', location=''):
    if isinstance(value, dict):
        for name, item in value.items():
            if name == 'content' and value.get('role') in {'system', 'developer'}:
                continue
            check(item, name, f'{location}/{name}')
    elif isinstance(value, list):
        for i, item in enumerate(value):
            check(item, key, f'{location}/{i}')
    elif isinstance(value, str) and value.strip():
        if key in SOURCE_KEYS:
            assert MARKER.fullmatch(value), f'Unprojected source field: {location}'
        elif value.lstrip().startswith(('{', '[')):
            try:
                nested = json.loads(value)
            except ValueError:
                return
            check(nested, location=f'{location}/serialized-json')


def main():
    manifest = json.loads((PACKAGE / 'projection_manifest.json').read_text())
    release = json.loads((ROOT / 'release_manifest.json').read_text())
    text_ids = {json.loads(line)['sha256'] for line in (PACKAGE / 'source_text_index.jsonl').read_text().splitlines()}
    for item in manifest['changes']:
        path = ROOT / item['path']
        assert hashlib.sha256(path.read_bytes()).hexdigest() == item['public_sha256'], path
    checked = 0
    for relative in release['files']:
        path = ROOT / relative
        for match in MARKER.finditer(path.read_text()):
            assert match.group()[len('[SOURCE_TEXT_OMITTED sha256='):-1] in text_ids, relative
        if 'prompts' in path.parts:
            continue
        if path.suffix == '.json':
            check(json.loads(path.read_text()), location=relative)
            checked += 1
        elif path.suffix == '.jsonl':
            for line in path.read_text().splitlines():
                if line.strip():
                    check(json.loads(line), location=relative)
            checked += 1
        elif path.suffix == '.csv':
            with path.open(encoding='utf-8-sig', newline='') as handle:
                for row in csv.DictReader(handle):
                    check(row, location=relative)
            checked += 1
    with (PACKAGE / 'citation_error_audit.csv').open(newline='') as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 44 and len({r['error_id'] for r in rows}) == 23
    assert len({r['source_doi'] for r in rows}) == 32
    assert 'complete_original_chunk' not in rows[0]
    assert all(r['source_doi'] and r['source_location'] for r in rows)
    print(f'PASS: {checked} structured files checked; dedicated source fields contain omission markers')
    print('PASS: every omission marker resolves to the source-text hash index')
    print('PASS: 44 citation-audit rows, 23 claims and 32 source DOIs')
    print('Git history was not rewritten; this check covers the current release tree only.')


if __name__ == '__main__':
    main()

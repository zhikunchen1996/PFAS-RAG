from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import build_manifest as manifest_builder


PACKAGE = Path(__file__).resolve().parents[1]
V3 = PACKAGE.parent
ROOT = V3.parents[1]
MANIFEST = PACKAGE / "freeze_manifest.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    if not MANIFEST.exists():
        fail("freeze_manifest.json is missing")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    listed_package_files = set(manifest["package_files"])
    actual_package_files = {
        str(path.relative_to(ROOT))
        for path in manifest_builder.included_files()
    }
    if listed_package_files != actual_package_files:
        fail(
            "manifest package index mismatch; "
            f"missing_from_manifest="
            f"{sorted(actual_package_files - listed_package_files)}, "
            f"stale_manifest_entries="
            f"{sorted(listed_package_files - actual_package_files)}"
        )
    checked = 0
    for section in ("package_files", "external_canonical_inputs"):
        for relative, expected in manifest[section].items():
            path = ROOT / relative
            if not path.is_file():
                fail(f"missing frozen file: {relative}")
            observed = sha256(path)
            if observed != expected:
                fail(
                    f"hash mismatch: {relative}\n"
                    f"expected {expected}\nobserved {observed}"
                )
            checked += 1

    protocol = json.loads(
        (PACKAGE / "methods/protocol.json").read_text(encoding="utf-8")
    )
    if protocol["status"] != "frozen_for_test40_execution":
        fail("protocol is not marked frozen for Test40 execution")
    l2 = protocol["layers"]["L2"]
    if l2["judgments_per_pair_question"] != 2:
        fail("L2 must use exactly two mirrored judgments")
    if l2["uncertainty"]["attempted_replicates"] < 10_000:
        fail("L2 bootstrap must use at least 10,000 replicates")
    if "independently estimated" not in l2["aggregation"]["tie_parameter"]:
        fail("criterion-specific tie parameter is not explicit")
    if protocol["judge"]["pricing_snapshot_date"] != "2026-07-28":
        fail("judge pricing snapshot date is missing")

    audit = json.loads(
        (
            PACKAGE
            / "audits/anonymization/scored/summary.json"
        ).read_text(encoding="utf-8")
    )
    if not audit["status"].startswith("passed_"):
        fail("anonymization audit did not pass")
    print(
        f"Frozen judge validation passed: {checked} hashes checked; "
        "protocol and anonymity audit valid."
    )


if __name__ == "__main__":
    main()

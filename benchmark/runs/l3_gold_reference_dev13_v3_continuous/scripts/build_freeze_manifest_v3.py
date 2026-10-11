from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
ROOT = PACKAGE.parents[2]
MANIFEST = PACKAGE / "frozen/freeze_manifest_v3.json"
V2 = ROOT / "benchmark/runs/l3_gold_reference_dev13_v2"
RESULTS = V2 / "results/dev13_gpt51_direct_vs_bge_llm_rag_repair7"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def artifact_paths() -> list[Path]:
    paths = [
        PACKAGE / "README.md",
        PACKAGE / "protocol.json",
        PACKAGE / "frozen/l3_gold_referenced_judge_v2.txt",
        PACKAGE / "frozen/reference_claim_ledgers_v2.jsonl",
        PACKAGE / "scripts/common.py",
        PACKAGE / "scripts/run_l3_continuous_scoring_v3.py",
        PACKAGE / "scripts/validate_continuous_v3.py",
        PACKAGE / "tests/test_continuous_protocol.py",
        V2 / "frozen/freeze_manifest_v2.json",
        V2
        / "human_adequacy_calibration_repair7"
        / "CANCELLED_BEFORE_LABELING.md",
        V2 / "human_adequacy_calibration_repair7/adequacy_register.csv",
    ]
    paths.extend(
        path
        for path in sorted(RESULTS.rglob("*"))
        if path.is_file() and "__pycache__" not in path.parts
    )
    return paths


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def build() -> dict[str, object]:
    paths = artifact_paths()
    missing = [relative(path) for path in paths if not path.exists()]
    if missing:
        raise RuntimeError(f"Missing frozen artifacts: {missing}")
    return {
        "freeze_id": "l3_gold_reference_v3_continuous",
        "freeze_date": "2026-07-29",
        "status": "frozen_dev_continuous_only_before_test40",
        "reference_sha256": sha256(
            PACKAGE / "frozen/reference_claim_ledgers_v2.jsonl"
        ),
        "binary_metrics_enabled": False,
        "human_candidate_adequacy_labels_collected": 0,
        "human_candidate_adequacy_labels_used": False,
        "test40_l3_evaluated": False,
        "canonical_claim_order_is_primary": True,
        "reverse_claim_order_is_sensitivity": True,
        "artifacts": {relative(path): sha256(path) for path in paths},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    expected = build()
    if args.verify:
        if not MANIFEST.exists():
            raise RuntimeError(f"Missing freeze manifest: {MANIFEST}")
        actual = json.loads(MANIFEST.read_text(encoding="utf-8"))
        if actual != expected:
            raise RuntimeError("V3 continuous freeze manifest mismatch")
        print(
            json.dumps(
                {
                    "status": "pass",
                    "freeze_id": actual["freeze_id"],
                    "artifact_count": len(actual["artifacts"]),
                },
                indent=2,
            )
        )
        return
    MANIFEST.write_text(
        json.dumps(expected, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {MANIFEST}")


if __name__ == "__main__":
    main()

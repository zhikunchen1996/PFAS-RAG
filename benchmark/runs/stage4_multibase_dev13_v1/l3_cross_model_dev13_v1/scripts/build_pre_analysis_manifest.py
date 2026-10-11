from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
ROOT = PACKAGE.parents[3]
MANIFEST = PACKAGE / "pre_analysis_manifest.json"
SOURCES = [
    ROOT
    / "benchmark/runs/stage4_multibase_dev13_v1/results/l3_v3/"
    f"{order}/question_level_scores.csv"
    for order in ("canonical", "reverse")
] + [
    ROOT
    / "benchmark/runs/l3_gold_reference_dev13_v2/results/"
    "dev13_gpt51_direct_vs_bge_llm_rag_repair7/"
    f"{order}/question_level_scores.csv"
    for order in ("canonical", "reverse")
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def build() -> dict[str, object]:
    paths = [
        PACKAGE / "README.md",
        PACKAGE / "protocol.json",
        PACKAGE / "scripts/run_cross_model_analysis.py",
        PACKAGE / "scripts/build_pre_analysis_manifest.py",
        *SOURCES,
    ]
    return {
        "freeze_id": "pfas_rag_dev13_l3_cross_model_v1_pre_analysis",
        "freeze_date": "2026-07-29",
        "status": "method_and_sources_hashed_before_local_analysis",
        "new_judge_calls": 0,
        "new_api_calls": 0,
        "held_out_test40_used": False,
        "artifact_sha256": {
            relative(path): sha256(path) for path in sorted(paths)
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    expected = build()
    if args.verify:
        actual = json.loads(MANIFEST.read_text(encoding="utf-8"))
        if actual != expected:
            raise RuntimeError("L3 cross-model pre-analysis manifest mismatch")
        print(json.dumps({"status": "pass", "artifacts": len(actual["artifact_sha256"])}, indent=2))
        return
    MANIFEST.write_text(
        json.dumps(expected, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {MANIFEST}")


if __name__ == "__main__":
    main()

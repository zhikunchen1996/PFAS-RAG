from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
ROOT = PACKAGE.parents[2]
MANIFEST = PACKAGE / "pre_run_manifest.json"
L3 = ROOT / "benchmark/runs/l3_gold_reference_dev13_v3_continuous"
GPT = (
    ROOT
    / "benchmark/runs/l3_gold_reference_dev13_v2/results/"
    "dev13_gpt51_direct_vs_bge_llm_rag_repair7/canonical"
)
MULTIBASE = (
    ROOT / "benchmark/runs/stage4_multibase_dev13_v1/results/l3_v3/canonical"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def artifacts() -> list[Path]:
    return [
        PACKAGE / "README.md",
        PACKAGE / "protocol.json",
        PACKAGE / "scripts/build_pre_run_manifest.py",
        PACKAGE / "scripts/run_repeats.py",
        PACKAGE / "scripts/aggregate_repeats.py",
        PACKAGE / "scripts/validate_completed_run.py",
        L3 / "frozen/l3_gold_referenced_judge_v2.txt",
        L3 / "frozen/reference_claim_ledgers_v2.jsonl",
        GPT / "local_envelopes.jsonl",
        MULTIBASE / "local_envelopes.jsonl",
    ]


def build() -> dict[str, object]:
    paths = artifacts()
    missing = [relative(path) for path in paths if not path.exists()]
    if missing:
        raise RuntimeError(f"Missing pre-run artifacts: {missing}")
    return {
        "protocol_id": "l3_three_repeat_dev13_v2_gpt51judge",
        "date": "2026-07-29",
        "status": "protocol_scripts_and_inputs_hashed_before_gpt51_calls",
        "question_count": 13,
        "system_count": 6,
        "repeat_count": 3,
        "planned_new_calls": 234,
        "bootstrap_enabled": False,
        "reverse_claim_order_new_calls": 0,
        "held_out_test40_used": False,
        "artifacts": {
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
            raise RuntimeError("GPT-5.1 three-repeat pre-run manifest mismatch")
        print(
            json.dumps(
                {
                    "status": "pass",
                    "artifact_count": len(actual["artifacts"]),
                    "planned_new_calls": 234,
                },
                indent=2,
            )
        )
        return
    MANIFEST.write_text(
        json.dumps(expected, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {MANIFEST}")


if __name__ == "__main__":
    main()

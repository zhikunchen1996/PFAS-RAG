from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path


CALIBRATION = Path(__file__).resolve().parent
PILOT = CALIBRATION.parent
ROOT = PILOT.parents[2]
JUDGE_SCRIPTS = ROOT / "benchmark/frozen_v3/judge/scripts"
if str(JUDGE_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(JUDGE_SCRIPTS))

import judge_common as common  # noqa: E402
import run_l2_pairwise_v2 as v2  # noqa: E402


PROMPT = CALIBRATION / "l2_citation_blind_pairwise_v3.txt"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--left", required=True)
    parser.add_argument("--right", required=True)
    parser.add_argument("--left-label", required=True)
    parser.add_argument("--right-label", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--questions", default=str(common.QUESTIONS_DEV))
    parser.add_argument("--gold", default=str(common.GOLD))
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    out = Path(args.out).expanduser().resolve()
    if out.exists() and any(out.iterdir()) and not args.resume:
        raise RuntimeError(f"Refusing to overwrite non-empty directory: {out}")
    out.mkdir(parents=True, exist_ok=True)
    payloads = v2.build_payloads(
        questions=common.read_csv(Path(args.questions)),
        gold_rows=common.read_jsonl(Path(args.gold)),
        left_rows=common.read_jsonl(Path(args.left)),
        right_rows=common.read_jsonl(Path(args.right)),
        left_label=args.left_label,
        right_label=args.right_label,
    )
    common.write_jsonl(out / "local_envelopes.jsonl", payloads)
    common.write_jsonl(
        out / "model_payloads.jsonl",
        [row["model_payload"] for row in payloads],
    )
    if args.dry_run:
        return

    started = time.perf_counter()
    results = v2.run_payloads(
        payloads,
        prompt=PROMPT.read_text(encoding="utf-8"),
        output=out / "judge_results.jsonl",
        workers=args.workers,
        resume=args.resume,
    )
    common.write_json(
        out / "run_manifest.json",
        {
            "layer": "L2 V3 non-exhaustive-gold calibration",
            "model": common.MODEL,
            "returned_snapshot_required": common.EXPECTED_MODEL_SNAPSHOT,
            "reasoning_effort": common.REASONING_EFFORT,
            "temperature": "provider default; not sent",
            "prompt_sha256": common.sha256(PROMPT),
            "questions_sha256": common.sha256(Path(args.questions)),
            "gold_sha256": common.sha256(Path(args.gold)),
            "left_sha256": common.sha256(Path(args.left)),
            "right_sha256": common.sha256(Path(args.right)),
            "question_count": len(payloads) // 2,
            "orientations_per_pair_question": 2,
            "adaptive_repeats": False,
            "hard_consensus_resolution": False,
            "unstable_outcomes": False,
            "mandatory_identity_leakage_scan": True,
            "schema_repair": False,
            "normal_finish_reason_required": True,
            "call_count": len(results),
            "total_tokens": sum(row["total_tokens"] for row in results),
            "estimated_cost_usd": sum(
                row["estimated_cost_usd"] for row in results
            ),
            "latency_seconds_sum": sum(
                row["latency_seconds"] for row in results
            ),
            "wall_clock_seconds": time.perf_counter() - started,
            "resume_mode": args.resume,
        },
    )


if __name__ == "__main__":
    main()

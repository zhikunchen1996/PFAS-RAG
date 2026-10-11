from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


PILOT = Path(__file__).resolve().parents[1]
ROOT = PILOT.parents[2]
V3 = ROOT / "benchmark/frozen_v3"
MANIFEST = PILOT / "protocol_freeze_manifest.json"
FILES = (
    PILOT / "protocol.json",
    PILOT / "prompts/shared_system_v1.txt",
    PILOT / "prompts/direct_user_v1.txt",
    PILOT / "prompts/rag_user_v1.txt",
    PILOT / "scripts/build_protocol_manifest.py",
    PILOT / "scripts/run_generation.py",
    PILOT / "scripts/validate_pilot.py",
    PILOT / "scripts/summarize_pilot.py",
    PILOT / "judge_calibration/l2_citation_blind_pairwise_v3.txt",
    PILOT / "judge_calibration/run_l2_pairwise_v3.py",
    PILOT / "judge_calibration/citation_blind_boundaries_dev13.csv",
    PILOT / "judge_calibration/run_l2_pairwise_v4.py",
    V3 / "input/questions_dev13.csv",
    V3
    / "results/dev13_retrieval_budget_gpt51_2026-07-26/"
    "bge_llm_gpt51/retrieval_outputs/"
    "rag_outputs_bge_llm_gpt51_pool60_bge30_llm10_fullchunk.jsonl",
    V3
    / "judge/support/layer1_common_tagger_v1/results/"
    "dev13_common_tagger_gpt51_2026-07-26/bge_llm/tags/"
    "tag_results.jsonl",
    V3 / "judge/methods/protocol.json",
    V3 / "judge/prompts/l2_citation_blind_pairwise_v2.txt",
    V3 / "judge/scripts/run_l2_pairwise_v2.py",
    V3 / "judge/scripts/aggregate_l2_v2.py",
    PILOT
    / "results/gpt51_dev13_matched_knowledge_v13/answers/direct.jsonl",
    PILOT / "results/gpt51_dev13_matched_knowledge_v13/answers/rag.jsonl",
    PILOT / "results/gpt51_dev13_matched_knowledge_v13/run_manifest.json",
    PILOT
    / "results/gpt51_dev13_matched_knowledge_v13/validation_report.json",
    PILOT
    / "results/gpt51_dev13_matched_knowledge_v13/usage/"
    "generation_usage_summary.csv",
    PILOT
    / "results/gpt51_dev13_matched_knowledge_v13/l2_v4/"
    "gpt51_direct_vs_rag/model_payloads.jsonl",
    PILOT
    / "results/gpt51_dev13_matched_knowledge_v13/l2_v4/"
    "gpt51_direct_vs_rag/local_envelopes.jsonl",
    PILOT
    / "results/gpt51_dev13_matched_knowledge_v13/l2_v4/"
    "gpt51_direct_vs_rag/judge_results.jsonl",
    PILOT
    / "results/gpt51_dev13_matched_knowledge_v13/l2_v4/"
    "gpt51_direct_vs_rag/run_manifest.json",
    PILOT
    / "results/gpt51_dev13_matched_knowledge_v13/l2_v4/"
    "aggregate/criterion_abilities.csv",
    PILOT
    / "results/gpt51_dev13_matched_knowledge_v13/l2_v4/"
    "aggregate/equal_weight_composite_secondary.csv",
    PILOT
    / "results/gpt51_dev13_matched_knowledge_v13/l2_v4/"
    "aggregate/fit_manifest.json",
    PILOT
    / "results/gpt51_dev13_matched_knowledge_v13/l2_v4/"
    "aggregate/mirrored_agreement.csv",
    PILOT
    / "results/gpt51_dev13_matched_knowledge_v13/l2_v4/"
    "aggregate/position_bias.csv",
    PILOT
    / "results/gpt51_dev13_matched_knowledge_v13/l2_v4/"
    "aggregate/raw_vote_counts.csv",
    PILOT
    / "results/gpt51_dev13_matched_knowledge_v13/final_report/"
    "per_question_l2_votes.csv",
    PILOT
    / "results/gpt51_dev13_matched_knowledge_v13/final_report/"
    "cost_latency_summary.csv",
    PILOT
    / "results/gpt51_dev13_matched_knowledge_v13/final_report/"
    "pilot_summary.json",
    PILOT
    / "results/gpt51_dev13_matched_knowledge_v13/FINAL_PILOT_AUDIT.md",
    PILOT / "reviews/claude_sonnet_l2v4_review.md",
    PILOT / "reviews/claude_sonnet_final_freeze_review.md",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def build() -> dict:
    missing = [relative(path) for path in FILES if not path.is_file()]
    if missing:
        raise RuntimeError("Missing protocol dependency: " + ", ".join(missing))
    return {
        "protocol_id": "pfas_rag_stage4_gpt51_dev13_matched_pilot_v1_5",
        "freeze_date": "2026-07-28",
        "formal_generation_started": True,
        "formal_generation_completed": True,
        "l2_v4_completed": True,
        "independent_review_verdict": "FREEZE_APPROVED",
        "file_count": len(FILES),
        "sha256": {relative(path): sha256(path) for path in FILES},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if args.verify:
        stored = json.loads(MANIFEST.read_text(encoding="utf-8"))
        current = build()
        if stored["file_count"] != current["file_count"]:
            raise SystemExit("Protocol manifest file count mismatch")
        if stored["sha256"] != current["sha256"]:
            raise SystemExit("Protocol manifest hash mismatch")
        print(f"PASS: {stored['file_count']} Stage 4 protocol hashes verified.")
        return
    MANIFEST.write_text(
        json.dumps(build(), indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {MANIFEST}")


if __name__ == "__main__":
    main()

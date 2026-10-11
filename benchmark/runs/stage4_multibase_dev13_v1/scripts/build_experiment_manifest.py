from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
ROOT = PACKAGE.parents[2]
MANIFEST = PACKAGE / "experiment_manifest.json"
V3 = ROOT / "benchmark/frozen_v3"
GPT_STAGE4 = ROOT / "benchmark/runs/stage4_gpt51_dev13_pilot_v1"
GPT_L3 = (
    ROOT
    / "benchmark/runs/l3_gold_reference_dev13_v2/results/"
    "dev13_gpt51_direct_vs_bge_llm_rag_repair7"
)
L3_CROSS_MODEL = PACKAGE / "l3_cross_model_dev13_v1"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def artifacts() -> list[Path]:
    paths = [
        path
        for path in PACKAGE.rglob("*")
        if path.is_file()
        and path != MANIFEST
        and "__pycache__" not in path.parts
    ]
    paths.extend(
        [
            V3 / "input/questions_dev13.csv",
            V3
            / "results/dev13_retrieval_budget_gpt51_2026-07-26/"
            "bge_llm_gpt51/retrieval_outputs/"
            "rag_outputs_bge_llm_gpt51_pool60_bge30_llm10_fullchunk.jsonl",
            V3
            / "judge/support/layer1_common_tagger_v1/results/"
            "dev13_common_tagger_gpt51_2026-07-26/bge_llm/tags/"
            "tag_results.jsonl",
            ROOT
            / "benchmark/runs/l3_gold_reference_dev13_v3_continuous/"
            "protocol.json",
            ROOT
            / "benchmark/runs/l3_gold_reference_dev13_v3_continuous/"
            "frozen/reference_claim_ledgers_v2.jsonl",
            ROOT
            / "benchmark/runs/l3_gold_reference_dev13_v3_continuous/"
            "frozen/l3_gold_referenced_judge_v2.txt",
            GPT_STAGE4
            / "results/gpt51_dev13_matched_knowledge_v13/answers/direct.jsonl",
            GPT_STAGE4
            / "results/gpt51_dev13_matched_knowledge_v13/answers/rag.jsonl",
        ]
    )
    for order in ["canonical", "reverse"]:
        for name in [
            "judge_results.jsonl",
            "question_level_scores.csv",
            "run_manifest.json",
            "system_summary.csv",
        ]:
            paths.append(GPT_L3 / order / name)
    return sorted(set(paths))


def build() -> dict[str, object]:
    paths = artifacts()
    missing = [relative(path) for path in paths if not path.exists()]
    if missing:
        raise RuntimeError(f"Missing experiment artifacts: {missing}")
    costs = list(
        __import__("csv").DictReader(
            (PACKAGE / "final_report/cost_summary.csv").open()
        )
    )
    l3_cross_model = json.loads(
        (L3_CROSS_MODEL / "post_analysis_manifest.json").read_text(
            encoding="utf-8"
        )
    )
    generation_l3_cost = sum(
        float(row["total_generation_plus_l3_judge_cost_usd"])
        for row in costs
        if row["model"] != "GPT-5.1"
    )
    return {
        "experiment_id": "pfas_rag_stage4_multibase_dev13_v1",
        "completion_date": "2026-07-29",
        "status": "dev13_complete_before_test40",
        "base_models": [
            "gpt-5.1-2025-11-13",
            "gemini-3.1-pro-preview",
            "claude-sonnet-5",
        ],
        "answer_system_count": 6,
        "question_count": 13,
        "new_answer_count": 52,
        "new_l3_judge_call_count": 104,
        "incremental_generation_plus_l3_cost_usd": generation_l3_cost,
        "incremental_cost_usd": generation_l3_cost,
        "l3_cross_model_status": l3_cross_model["status"],
        "l3_cross_model_pair_count_per_claim_order": l3_cross_model[
            "pair_count_per_claim_order"
        ],
        "l3_cross_model_new_judge_calls": l3_cross_model[
            "new_judge_calls"
        ],
        "l3_cross_model_incremental_cost_usd": l3_cross_model[
            "incremental_cost_usd"
        ],
        "l3_cross_model_canonical_holm_significant_pair_count": (
            l3_cross_model["canonical_holm_significant_pair_count"]
        ),
        "l3_cross_model_same_direction_pair_count": l3_cross_model[
            "same_direction_pair_count"
        ],
        "l3_binary_metrics_enabled": False,
        "l2_included_in_active_package": False,
        "historical_l2_archive": (
            "benchmark/archive/2026-07-29_l1_l15_l3_cleanup/"
            "multibase_dev13_l2_history"
        ),
        "human_candidate_adequacy_labels_used": False,
        "held_out_test40_used": False,
        "artifacts": {relative(path): sha256(path) for path in paths},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    expected = build()
    if args.verify:
        if not MANIFEST.exists():
            raise RuntimeError(f"Missing manifest: {MANIFEST}")
        actual = json.loads(MANIFEST.read_text(encoding="utf-8"))
        if actual != expected:
            raise RuntimeError("Multi-base Dev13 manifest mismatch")
        print(
            json.dumps(
                {
                    "status": "pass",
                    "artifact_count": len(actual["artifacts"]),
                    "incremental_generation_plus_l3_cost_usd": actual[
                        "incremental_generation_plus_l3_cost_usd"
                    ],
                    "l2_included_in_active_package": actual[
                        "l2_included_in_active_package"
                    ],
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

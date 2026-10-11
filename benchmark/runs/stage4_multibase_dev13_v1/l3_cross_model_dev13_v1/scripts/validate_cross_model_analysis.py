from __future__ import annotations

import csv
import json
import sys
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
sys.dont_write_bytecode = True
sys.path.insert(0, str(PACKAGE / "scripts"))

from finalize_cross_model_analysis import build  # noqa: E402


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    actual = json.loads(
        (PACKAGE / "post_analysis_manifest.json").read_text(encoding="utf-8")
    )
    expected = build()
    if actual != expected:
        raise RuntimeError("L3 cross-model post-analysis manifest mismatch")

    results = PACKAGE / "results"
    pairwise = read_csv(results / "pairwise_comparisons.csv")
    question_pairs = read_csv(
        results / "question_level_pair_differences.csv"
    )
    summaries = read_csv(results / "system_summary.csv")
    stability = read_csv(results / "claim_order_stability.csv")

    if len(pairwise) != 30:
        raise RuntimeError("Expected 15 pairs for each of two claim orders")
    if len(question_pairs) != 390:
        raise RuntimeError("Expected 30 pair-order cells x 13 questions")
    if len(summaries) != 12:
        raise RuntimeError("Expected six systems x two claim orders")
    if len(stability) != 15:
        raise RuntimeError("Expected one claim-order check per system pair")
    if {row["claim_order"] for row in pairwise} != {
        "canonical",
        "reverse",
    }:
        raise RuntimeError("Claim-order coverage is incomplete")
    if len({row["question_id"] for row in question_pairs}) != 13:
        raise RuntimeError("Question-level output does not contain Dev13")
    if any(
        row["permutation_p_holm"] == ""
        or not 0.0 <= float(row["permutation_p_holm"]) <= 1.0
        for row in pairwise
    ):
        raise RuntimeError("Invalid Holm-adjusted probability")
    if actual["held_out_test40_used"] is not False:
        raise RuntimeError("Test40 boundary was not preserved")
    if actual["new_judge_calls"] != 0 or actual["new_api_calls"] != 0:
        raise RuntimeError("Unexpected judge or API calls recorded")

    print(
        json.dumps(
            {
                "status": "pass",
                "artifact_count": len(actual["artifacts"]),
                "pairwise_rows": len(pairwise),
                "question_pair_rows": len(question_pairs),
                "canonical_holm_significant_pairs": actual[
                    "canonical_holm_significant_pair_count"
                ],
                "same_direction_pairs": actual[
                    "same_direction_pair_count"
                ],
                "new_judge_calls": 0,
                "incremental_cost_usd": 0.0,
                "held_out_test40_used": False,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

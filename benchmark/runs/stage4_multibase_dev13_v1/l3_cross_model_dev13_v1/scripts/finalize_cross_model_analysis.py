from __future__ import annotations

import hashlib
import json
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
ROOT = PACKAGE.parents[3]
MANIFEST = PACKAGE / "post_analysis_manifest.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def build() -> dict[str, object]:
    analysis = json.loads(
        (PACKAGE / "results/analysis_manifest.json").read_text(
            encoding="utf-8"
        )
    )
    paths = sorted(
        path
        for path in PACKAGE.rglob("*")
        if path.is_file()
        and path != MANIFEST
        and "__pycache__" not in path.parts
    )
    return {
        "freeze_id": "pfas_rag_dev13_l3_cross_model_v1",
        "freeze_date": "2026-07-29",
        "status": "completed_hash_verified_local_analysis",
        "source_score_status": "reused_frozen_l3_v3_question_scores",
        "new_judge_calls": 0,
        "new_api_calls": 0,
        "incremental_cost_usd": 0.0,
        "question_count": 13,
        "system_count": 6,
        "pair_count_per_claim_order": 15,
        "canonical_holm_significant_pair_count": analysis[
            "canonical_holm_significant_pair_count"
        ],
        "same_direction_pair_count": analysis[
            "same_direction_pair_count"
        ],
        "held_out_test40_used": False,
        "artifacts": {relative(path): sha256(path) for path in paths},
    }


def main() -> None:
    MANIFEST.write_text(
        json.dumps(build(), indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {MANIFEST}")


if __name__ == "__main__":
    main()

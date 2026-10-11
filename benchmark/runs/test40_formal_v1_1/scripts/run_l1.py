from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path
from statistics import mean
from typing import Any

import common


FROZEN_SCRIPTS = common.FROZEN_V3 / "scripts"
if str(FROZEN_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(FROZEN_SCRIPTS))

from retrieval_metrics import eval_context  # noqa: E402


def paths(
    retrieval_root: Path,
    selector_root: Path,
) -> dict[str, Path]:
    return {
        "hybrid": (
            retrieval_root
            / "retrieval_outputs/rag_outputs_hybrid_top10_pool60_win0.jsonl"
        ),
        "bge": (
            retrieval_root
            / "retrieval_outputs/"
            "rag_outputs_bge_base_top10_pool60_nodoccap.jsonl"
        ),
        "bge_llm": (
            selector_root
            / "retrieval_outputs/"
            "rag_outputs_bge_llm_gpt51_pool60_bge30_llm10_fullchunk.jsonl"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--retrieval-root", required=True)
    parser.add_argument("--selector-root", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    expected_ids = common.question_ids()
    gold: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in common.read_jsonl(common.GOLD):
        gold[str(row["question_id"])].append(row)

    retrieval_root = Path(args.retrieval_root).expanduser().resolve()
    selector_root = Path(args.selector_root).expanduser().resolve()
    common.require_exact_path(
        retrieval_root,
        common.RETRIEVAL_RESULTS,
        label="L1 retrieval input",
    )
    common.require_exact_path(
        selector_root,
        common.SELECTOR_RESULTS,
        label="L1 selector input",
    )
    input_paths = paths(retrieval_root, selector_root)
    per_question = []
    for system, path in input_paths.items():
        rows = common.ordered_rows(
            common.read_jsonl(path),
            expected_ids,
            source=system,
        )
        common.validate_contexts(rows, expected_count=10, source=system)
        for row in rows:
            metric = eval_context(
                str(row["question_id"]),
                gold[str(row["question_id"])],
                row["retrieved_context"],
                str(row["retrieval_config_name"]),
                str(row["retrieval_method"]),
                10,
                60,
                0,
            )
            per_question.append({"system": system, **metric})

    summaries = []
    for system in input_paths:
        rows = [row for row in per_question if row["system"] == system]
        required = [
            row for row in rows if int(row["required_gold_count"]) > 0
        ]
        negative = [
            row for row in rows if int(row["negative_gold_count"]) > 0
        ]
        summaries.append(
            {
                "system": system,
                "config_name": rows[0]["config_name"],
                "question_count": len(rows),
                "required_gold_applicable_questions": len(required),
                "MRR_required_gold": mean(
                    float(row["MRR_required_gold"]) for row in required
                ),
                "required_gold_recall@10": mean(
                    float(row["required_gold_recall@10"])
                    for row in required
                ),
                "gold_doc_recall@10": mean(
                    float(row["gold_doc_recall@10"]) for row in required
                ),
                "negative_gold_applicable_questions": len(negative),
                "negative_gold_recall@10": (
                    mean(
                        float(row["negative_gold_recall@10"])
                        for row in negative
                    )
                    if negative
                    else ""
                ),
            }
        )

    out = Path(args.out).expanduser().resolve()
    common.require_exact_path(
        out,
        common.L1_RESULTS,
        label="L1 output",
    )
    if out.exists() and any(out.iterdir()):
        raise RuntimeError(f"Refusing to overwrite non-empty output: {out}")
    out.mkdir(parents=True, exist_ok=True)
    common.write_csv(out / "per_question.csv", per_question)
    common.write_csv(out / "summary.csv", summaries)
    common.write_json(
        out / "run_manifest.json",
        {
            "protocol_id": "test40_formal_v1_l1",
            "status": "complete",
            "question_count": 40,
            "systems": list(input_paths),
            "llm_judge_used": False,
            "metrics": [
                "MRR_required_gold",
                "required_gold_recall@10",
                "gold_doc_recall@10",
                "negative_gold_recall@10",
            ],
            "questions_sha256": common.sha256(common.QUESTIONS),
            "gold_sha256": common.sha256(common.GOLD),
            "retrieval_inputs": {
                system: {
                    "path": common.project_relative(path),
                    "sha256": common.sha256(path),
                }
                for system, path in input_paths.items()
            },
        },
    )


if __name__ == "__main__":
    main()

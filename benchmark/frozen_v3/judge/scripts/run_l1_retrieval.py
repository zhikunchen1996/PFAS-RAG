from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path
from statistics import mean
from typing import Any

import judge_common as common
from retrieval_metrics import eval_context


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--retrieval", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--gold", default=str(common.GOLD))
    parser.add_argument(
        "--questions",
        default=str(common.QUESTIONS_TEST),
    )
    args = parser.parse_args()

    questions_path = Path(args.questions).expanduser().resolve()
    questions = common.read_csv(questions_path)
    gold_by_qid: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in common.read_jsonl(Path(args.gold)):
        gold_by_qid[str(row["question_id"])].append(row)

    per_question: list[dict[str, Any]] = []
    retrieval_path = Path(args.retrieval).expanduser().resolve()
    retrieval_rows = common.ordered_for_questions(
        common.read_jsonl(retrieval_path),
        questions,
        source_name=str(retrieval_path),
    )
    for row in retrieval_rows:
        context = row["retrieved_context"]
        qid = str(row["question_id"])
        if not isinstance(context, list) or not context:
            raise ValueError(f"{qid}: missing retrieved_context")
        if qid not in gold_by_qid:
            raise ValueError(f"{qid}: no gold records")
        per_question.append(
            eval_context(
                question_id=qid,
                gold_refs=gold_by_qid.get(qid, []),
                context=context,
                config_name=str(row.get("retrieval_config_name", "")),
                method=str(row.get("retrieval_method", "")),
                top_k=int(row.get("top_k") or len(context)),
                candidate_k=int(row.get("retrieval_k") or len(context)),
                window=int(row.get("context_window") or 0),
            )
        )

    required = [
        row for row in per_question if int(row["required_gold_count"]) > 0
    ]
    negative = [
        row for row in per_question if int(row["negative_gold_count"]) > 0
    ]
    if not required:
        raise RuntimeError("No questions with required gold")
    config_names = {str(row["config_name"]) for row in per_question}
    retrieval_methods = {
        str(row["retrieval_method"]) for row in per_question
    }
    if len(config_names) != 1 or len(retrieval_methods) != 1:
        raise ValueError(
            "A frozen L1 input file must contain one retrieval configuration"
        )
    summary = [
        {
            "config_name": per_question[0]["config_name"],
            "retrieval_method": per_question[0]["retrieval_method"],
            "question_count": len(per_question),
            "required_gold_applicable_questions": len(required),
            "MRR_required_gold": mean(
                float(row["MRR_required_gold"]) for row in required
            ),
            "required_gold_recall@10": mean(
                float(row["required_gold_recall@10"]) for row in required
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
    ]

    out = Path(args.out).expanduser().resolve()
    if out.exists() and any(out.iterdir()):
        raise RuntimeError(f"Refusing to overwrite non-empty directory: {out}")
    out.mkdir(parents=True, exist_ok=True)
    common.write_csv(out / "per_question.csv", per_question)
    common.write_csv(out / "summary.csv", summary)
    common.write_json(
        out / "run_manifest.json",
        {
            "layer": "L1 deterministic retrieval",
            "retrieval_file": str(retrieval_path),
            "retrieval_sha256": common.sha256(retrieval_path),
            "gold_file": str(Path(args.gold).resolve()),
            "gold_sha256": common.sha256(Path(args.gold)),
            "questions_file": str(questions_path),
            "questions_sha256": common.sha256(questions_path),
            "question_count": len(per_question),
            "llm_judge_used": False,
        },
    )


if __name__ == "__main__":
    main()

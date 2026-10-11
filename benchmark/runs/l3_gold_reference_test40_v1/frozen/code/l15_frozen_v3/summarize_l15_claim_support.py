from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import judge_common as common


VALID = {
    "supported",
    "partially_supported",
    "not_supported",
    "contradicted",
}
PASS = {"supported", "partially_supported"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    rows = common.read_jsonl(Path(args.results))
    per_question: list[dict[str, Any]] = []
    for row in rows:
        result = row["judge_result"]
        cited = result.get("cited_claims", [])
        uncited = result.get("uncited_source_dependent_claims", [])
        if not isinstance(cited, list) or not isinstance(uncited, list):
            raise ValueError(f"{row['question_id']}: invalid claim lists")
        labels = [str(item.get("support", "")) for item in cited]
        uncited_labels = [
            str(item.get("support_in_supplied_context", ""))
            for item in uncited
        ]
        if any(label not in VALID for label in labels):
            raise ValueError(f"{row['question_id']}: invalid cited claims")
        if any(label not in VALID for label in uncited_labels):
            raise ValueError(f"{row['question_id']}: invalid uncited claims")
        applicable = bool(cited)
        per_question.append(
            {
                "question_id": row["question_id"],
                "citation_support_applicable": applicable,
                "cited_claim_count": len(cited),
                "citation_supported_claim_count": sum(
                    label in PASS for label in labels
                ),
                "citation_unsupported_claim_count": sum(
                    label == "not_supported" for label in labels
                ),
                "citation_contradicted_claim_count": sum(
                    label == "contradicted" for label in labels
                ),
                "claim_supported_by_any_citation_rate": (
                    sum(label in PASS for label in labels) / len(labels)
                    if labels
                    else ""
                ),
                "uncited_source_dependent_claim_count": len(uncited),
            }
        )

    cited_total = sum(row["cited_claim_count"] for row in per_question)
    supported_total = sum(
        row["citation_supported_claim_count"] for row in per_question
    )
    unsupported_total = sum(
        row["citation_unsupported_claim_count"] for row in per_question
    )
    contradicted_total = sum(
        row["citation_contradicted_claim_count"] for row in per_question
    )
    applicable_questions = sum(
        bool(row["citation_support_applicable"]) for row in per_question
    )
    summary = [
        {
            "question_count": len(per_question),
            "applicable_question_count": applicable_questions,
            "cited_claim_count": cited_total,
            "claim_supported_by_any_citation_rate": (
                supported_total / cited_total
                if cited_total
                else ""
            ),
            "unsupported_claim_rate": (
                unsupported_total / cited_total if cited_total else ""
            ),
            "contradicted_claim_rate": (
                contradicted_total / cited_total if cited_total else ""
            ),
            "questions_with_no_unsupported_or_contradicted_cited_claims": sum(
                row["citation_support_applicable"]
                and
                row["citation_unsupported_claim_count"] == 0
                and row["citation_contradicted_claim_count"] == 0
                for row in per_question
            ),
            "uncited_source_dependent_claim_count": sum(
                row["uncited_source_dependent_claim_count"]
                for row in per_question
            ),
        }
    ]
    out = Path(args.out).expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)
    common.write_csv(out / "per_question.csv", per_question)
    common.write_csv(out / "summary.csv", summary)


if __name__ == "__main__":
    main()

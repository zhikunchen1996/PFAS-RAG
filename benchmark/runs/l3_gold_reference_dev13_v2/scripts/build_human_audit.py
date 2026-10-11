from __future__ import annotations

import argparse
import json
from collections import Counter
from typing import Any

import common


def evidence_line(row: dict[str, Any]) -> str:
    scope = "; ".join(
        str(row.get(field, "")).strip()
        for field in [
            "PFAS_compound",
            "matrix",
            "method_or_material",
            "endpoint",
            "numerical_value",
            "unit",
        ]
        if str(row.get(field, "")).strip()
    )
    return (
        f"**{row['evidence_id']}** ({row['evidence_type']}; "
        f"`{row['doc_id']}`, chunk `{row['chunk_id']}`)"
        + (f"  \nScope: {scope}" if scope else "")
        + f"  \n> {row['exact_evidence_span']}"
        + (
            f"  \nSupported claim metadata: {row['supported_claim']}"
            if row.get("supported_claim")
            else ""
        )
        + (
            f"  \nDoes not support: {row['does_not_support']}"
            if row.get("does_not_support")
            else ""
        )
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing pending human-review candidate file.",
    )
    args = parser.parse_args()
    if common.HUMAN_CANDIDATES.exists() and not args.force:
        raise RuntimeError(
            "Human-review candidates already exist. Refusing to overwrite "
            "possible manual edits; pass --force only when replacement is "
            "intentional."
        )
    packets = common.read_jsonl(common.PACKETS)
    drafts = {
        row["question_id"]: row for row in common.read_jsonl(common.DRAFTS)
    }
    reviews = {
        row["question_id"]: row for row in common.read_jsonl(common.REVIEWS)
    }
    qids = [row["question_id"] for row in packets]
    if set(qids) != set(drafts) or set(qids) != set(reviews):
        raise RuntimeError("Human packet requires complete Model A and B outputs")

    candidates = []
    markdown = [
        "# L3 Dev13 reference-answer human audit",
        "",
        "Status: **all decisions pending**",
        "",
        "For each question, inspect the complete gold evidence, Model A draft,",
        "and Model B review. Edit `reference_candidates.jsonl` if needed, then",
        "set `human_review.decision` to `approve` or `reject`. An approval of a",
        "Model B `revise` or `reject` item requires non-empty resolution notes.",
        "",
    ]
    register = []
    verdict_counts: Counter[str] = Counter()
    for packet in packets:
        qid = packet["question_id"]
        draft = drafts[qid]["draft"]
        review = reviews[qid]["review"]
        verdict_counts[review["overall_verdict"]] += 1
        candidate: dict[str, Any] = {
            "question_id": qid,
            "question_text": packet["question"]["question_text"],
            "task_boundaries": packet["task_boundaries"],
            "approved_reference": draft,
            "model_b_verdict": review["overall_verdict"],
            "model_b_review_sha256": common.payload_sha256(review),
            "human_review": {
                "decision": "pending",
                "reviewer_role": "project_author",
                "review_date": "",
                "resolution_notes": "",
            },
        }
        candidates.append(candidate)
        register.append(
            {
                "question_id": qid,
                "model_b_verdict": review["overall_verdict"],
                "claim_count": len(draft["claims"]),
                "model_b_omission_count": len(review["omitted_gold_findings"]),
                "model_b_reference_issue_count": len(
                    review["reference_answer_issues"]
                ),
                "human_decision": "pending",
                "resolution_notes": "",
            }
        )

        markdown.extend(
            [
                f"## {qid}",
                "",
                f"**Question:** {packet['question']['question_text']}",
                "",
                f"**Must include:** {packet['task_boundaries']['must_include']}",
                "",
                f"**Must not claim:** {packet['task_boundaries']['must_not_claim']}",
                "",
                "### Complete Gold Evidence",
                "",
                "\n\n".join(evidence_line(row) for row in packet["gold_evidence"]),
                "",
                "### Model A Reference Draft",
                "",
                draft["reference_answer"],
                "",
                "Claims:",
                "",
            ]
        )
        for claim in draft["claims"]:
            markdown.append(
                f"- `{claim['claim_id']}` [{claim['claim_type']}]: "
                f"{claim['claim_text']} "
                f"(evidence: {', '.join(claim['evidence_ids'])})"
            )
        markdown.extend(
            [
                "",
                "### Model B Verification",
                "",
                f"Overall verdict: **{review['overall_verdict']}**",
                "",
            ]
        )
        for claim in review["claim_reviews"]:
            markdown.append(
                f"- `{claim['claim_id']}`: **{claim['verdict']}**. "
                f"{claim['rationale']}"
            )
            if claim["recommended_claim_text"]:
                markdown.append(
                    f"  Recommended text: {claim['recommended_claim_text']}"
                )
        if review["omitted_gold_findings"]:
            markdown.extend(["", "Omitted findings:"])
            for finding in review["omitted_gold_findings"]:
                markdown.append(
                    f"- [{finding['suggested_claim_type']}] "
                    f"{finding['suggested_claim_text']} "
                    f"(evidence: {', '.join(finding['evidence_ids'])})"
                )
        if review["reference_answer_issues"]:
            markdown.extend(["", "Reference-answer issues:"])
            markdown.extend(
                f"- {issue}" for issue in review["reference_answer_issues"]
            )
        markdown.extend(["", "---", ""])

    common.write_jsonl(common.HUMAN_CANDIDATES, candidates)
    common.write_csv(
        common.PACKAGE / "human_review/decision_register.csv",
        register,
    )
    audit_path = common.PACKAGE / "human_review/HUMAN_AUDIT_PACKET.md"
    audit_path.parent.mkdir(parents=True, exist_ok=True)
    audit_path.write_text("\n".join(markdown), encoding="utf-8")
    common.write_json(
        common.PACKAGE / "human_review/build_manifest.json",
        {
            "question_count": len(candidates),
            "human_decisions": {"pending": len(candidates)},
            "model_b_verdicts": dict(sorted(verdict_counts.items())),
            "reference_candidates_sha256": common.sha256(
                common.HUMAN_CANDIDATES
            ),
            "audit_packet_sha256": common.sha256(audit_path),
            "model_a_drafts_sha256": common.sha256(common.DRAFTS),
            "model_b_reviews_sha256": common.sha256(common.REVIEWS),
        },
    )
    print(
        json.dumps(
            {
                "questions": len(candidates),
                "model_b_verdicts": verdict_counts,
                "human_decisions": "all pending",
            },
            default=dict,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

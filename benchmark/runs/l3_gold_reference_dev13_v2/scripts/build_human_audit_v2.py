from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

import common
import run_reference_group_verification_v2 as verification
import run_reference_revision_v2 as revision


OUTPUT_DIR = common.PACKAGE / "human_review_v2"
CANDIDATES = OUTPUT_DIR / "reference_candidates.jsonl"


def evidence_line(row: dict[str, Any]) -> str:
    return (
        f"**{row['evidence_id']}** ({row['evidence_type']}; "
        f"`{row['doc_id']}`, chunk `{row['chunk_id']}`)\n"
        f"> {row['exact_evidence_span']}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--revisions")
    parser.add_argument("--reviews")
    parser.add_argument("--packets")
    parser.add_argument("--output-dir")
    args = parser.parse_args()
    packets_path = (
        Path(args.packets).expanduser().resolve()
        if args.packets
        else common.PACKETS
    )
    output_dir = (
        Path(args.output_dir).expanduser().resolve()
        if args.output_dir
        else OUTPUT_DIR
    )
    candidates_path = output_dir / "reference_candidates.jsonl"
    if candidates_path.exists() and not args.force:
        raise RuntimeError(
            "V2 human candidates already exist; refusing to overwrite "
            "possible project-author edits without --force"
        )

    packets = {
        row["question_id"]: row for row in common.read_jsonl(packets_path)
    }
    previous_drafts = {
        row["question_id"]: row["draft"]
        for row in common.read_jsonl(common.DRAFTS)
    }
    revisions_path = (
        Path(args.revisions).expanduser().resolve()
        if args.revisions
        else revision.OUTPUT
    )
    reviews_path = (
        Path(args.reviews).expanduser().resolve()
        if args.reviews
        else verification.OUTPUT
    )
    revisions = {
        row["question_id"]: row
        for row in common.read_jsonl(revisions_path)
    }
    reviews = {
        row["question_id"]: row
        for row in common.read_jsonl(reviews_path)
    }
    if set(packets) != set(revisions) or set(packets) != set(reviews):
        raise RuntimeError("V2 audit requires complete Dev13 revisions and reviews")

    candidates = []
    register = []
    verdict_counts: Counter[str] = Counter()
    markdown = [
        "# L3 Dev13 V2 project-author audit",
        "",
        "Status: **all project-author decisions pending**",
        "",
        "The claim ledger is normative for scoring. The prose answer is",
        "non-normative. Review every task component and every claim group,",
        "including groups not flagged by Model B.",
        "",
        "Record decisions in `reference_candidates.jsonl`. Approval requires",
        "all five `project_author_checks` to be true, `human_review.decision`",
        "to be `approve`, a review date, and resolution notes. Any edit to an",
        "approved ledger requires a new Model B verification before freeze.",
        "",
    ]
    for qid, packet in packets.items():
        revised = revisions[qid]["revision"]
        review = reviews[qid]["review"]
        verdict_counts[review["overall_verdict"]] += 1
        candidate: dict[str, Any] = {
            "question_id": qid,
            "question_text": packet["question"]["question_text"],
            "task_boundaries": packet["task_boundaries"],
            "approved_ledger": revised,
            "model_b_verdict": review["overall_verdict"],
            "model_b_clean": verification.review_is_clean(review),
            "model_b_review_sha256": common.payload_sha256(review),
            "model_b_reviewed_revision_sha256": reviews[qid][
                "revision_sha256"
            ],
            "project_author_checks": {
                "task_components_approved": False,
                "all_claim_groups_reviewed": False,
                "atomic_dispositions_reviewed": False,
                "prose_ledger_consistent": False,
                "all_model_b_issues_resolved": False,
            },
            "human_review": {
                "decision": "pending",
                "reviewer_role": "project_author",
                "review_date": "",
                "resolution_notes": "",
            },
        }
        candidates.append(candidate)
        non_supported = sum(
            row["verdict"] != "supported"
            for row in review["claim_group_reviews"]
            + review["constraint_group_reviews"]
        )
        issue_count = (
            len(review["duplicate_or_weighting_issues"])
            + len(review["prose_ledger_issues"])
            + len(review["omitted_major_gold_findings"])
            + len(review["unresolved_prior_claim_ids"])
        )
        register.append(
            {
                "question_id": qid,
                "model_b_verdict": review["overall_verdict"],
                "model_b_clean": verification.review_is_clean(review),
                "task_component_count": len(revised["task_components"]),
                "content_claim_group_count": len(revised["claim_groups"]),
                "constraint_group_count": len(revised["constraint_groups"]),
                "non_supported_group_count": non_supported,
                "open_issue_count": issue_count,
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
                "### Frozen task components",
                "",
            ]
        )
        for component in revised["task_components"]:
            markdown.append(
                f"- `{component['task_component_id']}`: "
                f"{component['component_text']}"
            )
        markdown.extend(["", "### Complete gold evidence", ""])
        markdown.append(
            "\n\n".join(evidence_line(row) for row in packet["gold_evidence"])
        )
        markdown.extend(["", "### Normative content claim groups", ""])
        for group in revised["claim_groups"]:
            markdown.extend(
                [
                    f"#### {group['claim_group_id']}",
                    "",
                    f"- Component: `{group['task_component_id']}`",
                    f"- Importance: `{group['importance']}`",
                    f"- Function: `{group['function']}`",
                    f"- Scoring role: `{group['scoring_role']}`",
                    f"- Proposition: {group['canonical_proposition']}",
                    f"- Material qualifiers: {json.dumps(group['material_qualifiers'], ensure_ascii=False)}",
                    f"- Evidence: {', '.join(group['evidence_ids'])}",
                    f"- Prior atomic claims: {', '.join(group['source_atomic_claim_ids'])}",
                    f"- Full: {group['full_rule']}",
                    f"- Partial: {group['partial_rule']}",
                    f"- Contradiction: {group['contradiction_rule']}",
                    "",
                ]
            )
        markdown.extend(["", "### Prior atomic-claim dispositions", ""])
        prior_claims = {
            row["claim_id"]: row
            for row in previous_drafts[qid]["claims"]
        }
        for disposition in revised["atomic_claim_dispositions"]:
            prior = prior_claims[disposition["atomic_claim_id"]]
            targets = ", ".join(disposition["target_claim_group_ids"]) or "(deleted)"
            markdown.extend(
                [
                    f"#### {disposition['atomic_claim_id']}",
                    "",
                    f"- Prior claim: {prior['claim_text']}",
                    f"- Action: `{disposition['action']}`",
                    f"- Final target(s): {targets}",
                    f"- Rationale: {disposition['rationale']}",
                    "",
                ]
            )
        if revised["constraint_groups"]:
            markdown.extend(["### Constraint-only groups", ""])
            for group in revised["constraint_groups"]:
                markdown.extend(
                    [
                        f"- `{group['claim_group_id']}`: "
                        f"{group['canonical_proposition']}",
                        f"  Violation rule: {group['violation_rule']}",
                    ]
                )
        markdown.extend(
            [
                "",
                "### Model B verification",
                "",
                f"Overall verdict: **{review['overall_verdict']}**",
                "",
            ]
        )
        for row in (
            review["claim_group_reviews"] + review["constraint_group_reviews"]
        ):
            markdown.append(
                f"- `{row['claim_group_id']}`: **{row['verdict']}**. "
                f"{row['rationale']}"
            )
            if row["recommended_change"]:
                markdown.append(f"  Recommended change: {row['recommended_change']}")
        for label, issues in [
            ("Duplicate/weighting issues", review["duplicate_or_weighting_issues"]),
            ("Prose/ledger issues", review["prose_ledger_issues"]),
            ("Human-review priorities", review["human_review_priorities"]),
        ]:
            if issues:
                markdown.extend(["", f"{label}:"])
                markdown.extend(f"- {issue}" for issue in issues)
        markdown.extend(
            [
                "",
                "### Non-normative reference prose",
                "",
                revised["reference_answer"],
                "",
                "### Prose-to-ledger map",
                "",
            ]
        )
        for mapping in revised["reference_answer_claim_map"]:
            markdown.append(
                f"- {mapping['sentence_or_clause']} -> "
                f"{', '.join(mapping['claim_group_ids'])}"
            )
        markdown.extend(
            [
                "",
                "---",
                "",
            ]
        )

    common.write_jsonl(candidates_path, candidates)
    decision_register_path = output_dir / "decision_register.csv"
    common.write_csv(decision_register_path, register)
    audit_path = output_dir / "HUMAN_AUDIT_PACKET.md"
    audit_path.write_text("\n".join(markdown), encoding="utf-8")
    common.write_json(
        output_dir / "build_manifest.json",
        {
            "question_count": len(candidates),
            "human_decisions": {"pending": len(candidates)},
            "model_b_verdicts": dict(sorted(verdict_counts.items())),
            "packets_file": (
                str(packets_path.relative_to(common.ROOT))
                if packets_path.is_relative_to(common.ROOT)
                else str(packets_path)
            ),
            "packets_sha256": common.sha256(packets_path),
            "task_components_sha256": common.sha256(revision.TASK_COMPONENTS),
            "previous_atomic_drafts_sha256": common.sha256(common.DRAFTS),
            "revisions_file": str(revisions_path.relative_to(common.ROOT)),
            "revisions_sha256": common.sha256(revisions_path),
            "model_b_reviews_file": str(reviews_path.relative_to(common.ROOT)),
            "model_b_reviews_sha256": common.sha256(reviews_path),
            "reference_candidates_sha256": common.sha256(candidates_path),
            "decision_register_sha256": common.sha256(
                decision_register_path
            ),
            "audit_packet_sha256": common.sha256(audit_path),
        },
    )
    print(
        json.dumps(
            {
                "questions": len(candidates),
                "model_b_verdicts": dict(verdict_counts),
                "human_decisions": "all pending",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

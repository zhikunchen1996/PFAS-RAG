from __future__ import annotations

import csv
import json
import shutil
from pathlib import Path
from typing import Any

import common


RELEASE_ID = "l3_test40_reference_v1_2026-07-29"
FINAL_LEDGERS = (
    common.PACKAGE
    / "reference_build/revisions/model_a_ledgers_resolution3.jsonl"
)
L15 = common.PACKAGE / "l15_reference_validation_v2"
AUDIT = common.PACKAGE / "project_author_audit_v1"
FROZEN = common.PACKAGE / "frozen"
DATE = "2026-07-29"

REVIEW_FILES = [
    common.PACKAGE / "reference_build/reviews/model_b_reviews_v1.jsonl",
    common.PACKAGE
    / "reference_build/reviews/model_b_reviews_v1_rereview1.jsonl",
    common.PACKAGE
    / "reference_build/reviews/model_b_reviews_v1_rereview2.jsonl",
    common.PACKAGE
    / "reference_build/reviews/model_b_reviews_v1_rereview3.jsonl",
    common.PACKAGE
    / "reference_build/reviews/model_b_reviews_v1_verbatim_review.jsonl",
    common.PACKAGE
    / "reference_build/reviews/model_b_reviews_v1_content_review.jsonl",
]


def copy_file(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    if FROZEN.exists():
        raise RuntimeError("Frozen Test40 reference directory already exists")
    summary = read_csv(L15 / "summary/summary.csv")[0]
    if (
        summary["question_count"] != "40"
        or summary["applicable_question_count"] != "40"
        or float(summary["claim_supported_by_any_citation_rate"]) != 1.0
        or float(summary["unsupported_claim_rate"]) != 0.0
        or float(summary["contradicted_claim_rate"]) != 0.0
        or summary["questions_with_no_unsupported_or_contradicted_cited_claims"]
        != "40"
        or summary["uncited_source_dependent_claim_count"] != "0"
    ):
        raise RuntimeError("Frozen L1.5 reference freeze gate did not pass")

    questions = common.read_csv(common.QUESTIONS)
    question_ids = [row["question_id"] for row in questions]
    if len(question_ids) != 40 or len(set(question_ids)) != 40:
        raise RuntimeError("Expected 40 unique Test40 questions")
    ledgers = common.read_jsonl(FINAL_LEDGERS)
    if {row["question_id"] for row in ledgers} != set(question_ids):
        raise RuntimeError("Final ledger membership differs from Test40")
    test_gold = [
        row
        for row in common.read_jsonl(common.GOLD)
        if row["question_id"] in set(question_ids)
    ]
    if len(test_gold) != 189:
        raise RuntimeError("Expected 189 Test40 gold records")

    FROZEN.mkdir(parents=True, exist_ok=False)
    copy_file(common.QUESTIONS, FROZEN / "inputs/questions_test40.csv")
    common.write_jsonl(FROZEN / "inputs/gold_test40.jsonl", test_gold)
    copy_file(
        common.SOURCE_PACKETS,
        FROZEN / "inputs/source_packets_test40.jsonl",
    )
    copy_file(
        common.TASK_COMPONENTS,
        FROZEN / "inputs/task_components_test40.jsonl",
    )
    copy_file(
        common.REFERENCE_PACKETS,
        FROZEN / "inputs/reference_packets_test40.jsonl",
    )
    copy_file(FINAL_LEDGERS, FROZEN / "reference_claim_ledgers_test40_v1.jsonl")

    latest_reviews = {}
    for path in REVIEW_FILES:
        for review in common.read_jsonl(path):
            latest_reviews[review["question_id"]] = review
    if set(latest_reviews) != set(question_ids) or any(
        row["verdict"] != "clean" for row in latest_reviews.values()
    ):
        raise RuntimeError("Latest independent review set is not 40/40 clean")
    common.write_jsonl(
        FROZEN / "reviews/latest_clean_claude_reviews.jsonl",
        [latest_reviews[qid] for qid in question_ids],
    )
    for path in REVIEW_FILES:
        copy_file(path, FROZEN / "reviews/history" / path.name)

    for path in sorted((common.PACKAGE / "prompts").glob("*")):
        if path.is_file():
            copy_file(path, FROZEN / "prompts/reference_construction" / path.name)
    frozen_l15_prompt = (
        common.FROZEN_V3 / "judge/prompts/l15_claim_citation_support_v2.txt"
    )
    copy_file(frozen_l15_prompt, FROZEN / "prompts/l15_claim_citation_support_v2.txt")
    for path in sorted((common.PACKAGE / "scripts").glob("*.py")):
        copy_file(path, FROZEN / "code/reference_build" / path.name)
    for name in [
        "judge_common.py",
        "run_l15_claim_support.py",
        "summarize_l15_claim_support.py",
    ]:
        copy_file(
            common.FROZEN_V3 / "judge/scripts" / name,
            FROZEN / "code/l15_frozen_v3" / name,
        )

    for relative in [
        "inputs/reference_answers_l15.jsonl",
        "inputs/citation_mapping.jsonl",
        "input_manifest.json",
        "run/judge_results.jsonl",
        "run/local_envelopes.jsonl",
        "run/model_payloads.jsonl",
        "run/run_manifest.json",
        "summary/per_question.csv",
        "summary/summary.csv",
    ]:
        copy_file(L15 / relative, FROZEN / "l15_validation" / relative)

    original_decisions = read_csv(AUDIT / "decision_register.csv")
    if len(original_decisions) != 40:
        raise RuntimeError("Expected 40 pending audit decisions")
    final_decisions = []
    for row in original_decisions:
        final_decisions.append(
            {
                **row,
                "project_author_decision": "approve",
                "review_date": DATE,
                "resolution_notes": (
                    "Batch-approved under the project author's explicit "
                    "conditional instruction after 40/40 Frozen L1.5 passage; "
                    "not represented as individual manual review."
                ),
                "approval_mode": "conditional_batch_approval",
            }
        )
    write_csv(FROZEN / "author/decision_register.csv", final_decisions)

    span_rows = read_csv(AUDIT / "new_full_chunk_span_register.csv")
    if len(span_rows) != 165:
        raise RuntimeError("Expected 165 new full-chunk span audit rows")
    final_spans = []
    for row in span_rows:
        final_spans.append(
            {
                **row,
                "audit_decision": "approve",
                "audit_notes": (
                    "Batch-approved after exact-substring validation, 40/40 "
                    "clean Claude review, and 172/172 Frozen L1.5 claim passage; "
                    "not represented as individual manual review."
                ),
                "review_date": DATE,
                "approval_mode": "conditional_batch_approval",
            }
        )
    write_csv(FROZEN / "author/new_span_decision_register.csv", final_spans)

    approval_record = {
        "release_id": RELEASE_ID,
        "decision": "approve",
        "date": DATE,
        "reviewer_role": "project_author",
        "approval_mode": "explicit conditional batch approval",
        "project_author_instruction": (
            "你先把这个gold answer用l1.5评估下吧。能完成 我们就可以froze了"
        ),
        "agreed_l15_rule": (
            "A cited statement passes when its central proposition is supported "
            "by the cited chunk. supported and partially_supported both pass; "
            "not_supported and contradicted fail."
        ),
        "condition_result": {
            "questions_passed": "40/40",
            "cited_claims_passed": "172/172",
            "unsupported_claims": 0,
            "contradicted_claims": 0,
            "uncited_source_dependent_claims": 0,
        },
        "supporting_checks": {
            "latest_independent_claude_reviews_clean": "40/40",
            "nonverbatim_exact_spans": 0,
            "candidate_test40_inputs_used": False,
        },
        "manual_per_question_review_claimed": False,
        "manual_per_span_review_claimed": False,
        "scope_note": (
            "The approval applies to the candidate-blind Test40 reference "
            "package and its 165 newly selected verbatim spans on the stated "
            "automated evidence-validation basis."
        ),
    }
    common.write_json(FROZEN / "author/project_author_approval_record.json", approval_record)

    freeze_record = f"""# Test40 L3 reference freeze record

Release: `{RELEASE_ID}`

Freeze date: {DATE}

## Decision

The candidate-blind Test40 L3 reference package is frozen. The project author
explicitly authorized freezing if the gold answer completed the previously
agreed lenient Frozen L1.5 check. The corrected L1.5 V2 scope rendered only
normative answer-content `claim_groups`; `constraint_groups` remain L3
violation rules and were not treated as statements a gold answer must make.

The condition passed:

- 40/40 questions applicable and passed;
- 172/172 cited claims were `supported` or `partially_supported`;
- 0 `not_supported` claims;
- 0 `contradicted` claims; and
- 0 uncited source-dependent claims.

Approval is recorded as a conditional batch approval. It is not represented as
individual manual review of every question or every newly selected span.

## Additional evidence checks

- latest independent Claude Sonnet verdict: 40/40 clean;
- all ledger exact spans are verbatim in approved full chunks;
- 165 newly selected verbatim spans across 23 questions are retained with an
  explicit batch-approval register; and
- no candidate Test40 answer, candidate retrieved context, system identity, or
  Test40 result was used in reference construction or this reference check.

## L1.5 V1 diagnostic

The retained V1 diagnostic incorrectly rendered `constraint_groups` as gold
answer statements. It produced 209/217 passing claims and eight unsupported
absence/generalization constraints across seven questions. V2 corrected this
input-scope error prospectively for the freeze check; no scientific ledger
claim was deleted or edited in response. The V1 outputs remain outside this
frozen directory as transparent development history.

## Boundary

This freeze authorizes subsequent formal Test40 scoring under the unchanged
GPT-5.1 three-repeat L3 policy. Any later annotation correction requires a new
version; this release must not be overwritten.
"""
    (FROZEN / "FREEZE_RECORD.md").write_text(freeze_record, encoding="utf-8")

    excluded = {"freeze_manifest.json", "freeze_manifest.sha256"}
    files = {}
    for path in sorted(FROZEN.rglob("*")):
        if not path.is_file() or path.name in excluded:
            continue
        files[str(path.relative_to(common.ROOT))] = common.sha256(path)
    manifest = {
        "release_id": RELEASE_ID,
        "status": "FROZEN",
        "freeze_date": DATE,
        "question_count": 40,
        "gold_record_count": 189,
        "reference_claim_ledger_count": 40,
        "latest_clean_claude_review_count": 40,
        "new_full_chunk_span_count": 165,
        "project_author_decision": "approve_conditional_batch",
        "l15": {
            "model": "gpt-5.1-2025-11-13",
            "reasoning_effort": "low",
            "question_pass": "40/40",
            "claim_pass": "172/172",
            "unsupported": 0,
            "contradicted": 0,
            "uncited_source_dependent": 0,
            "prompt_sha256": common.sha256(frozen_l15_prompt),
        },
        "candidate_test40_inputs_used": False,
        "formal_test40_l3_scoring_run": False,
        "files": files,
    }
    manifest_path = FROZEN / "freeze_manifest.json"
    common.write_json(manifest_path, manifest)
    (FROZEN / "freeze_manifest.sha256").write_text(
        common.sha256(manifest_path) + "  freeze_manifest.json\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "release_id": RELEASE_ID,
                "status": "FROZEN",
                "file_count": len(files),
                "manifest_sha256": common.sha256(manifest_path),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

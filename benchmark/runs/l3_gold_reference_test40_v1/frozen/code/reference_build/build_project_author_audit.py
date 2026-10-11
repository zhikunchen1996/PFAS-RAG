from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import common


LEDGERS = (
    common.PACKAGE
    / "reference_build/revisions/model_a_ledgers_resolution3.jsonl"
)
RESOLUTION_FILES = [
    common.PACKAGE / "reference_build/revisions/final_resolution_v1.jsonl",
    common.PACKAGE
    / "reference_build/revisions/verbatim_span_resolution_v1.jsonl",
    common.PACKAGE / "reference_build/revisions/content_resolution_v1.jsonl",
]
OUTPUT_DIR = common.PACKAGE / "project_author_audit_v1"

REVIEW_FILES = [
    (
        "initial_review",
        common.PACKAGE / "reference_build/reviews/model_b_reviews_v1.jsonl",
    ),
    (
        "rereview1",
        common.PACKAGE
        / "reference_build/reviews/model_b_reviews_v1_rereview1.jsonl",
    ),
    (
        "rereview2",
        common.PACKAGE
        / "reference_build/reviews/model_b_reviews_v1_rereview2.jsonl",
    ),
    (
        "rereview3",
        common.PACKAGE
        / "reference_build/reviews/model_b_reviews_v1_rereview3.jsonl",
    ),
    (
        "verbatim_review",
        common.PACKAGE
        / "reference_build/reviews/model_b_reviews_v1_verbatim_review.jsonl",
    ),
    (
        "content_review",
        common.PACKAGE
        / "reference_build/reviews/model_b_reviews_v1_content_review.jsonl",
    ),
]


def latest_reviews() -> tuple[dict[str, dict[str, Any]], dict[str, list[dict[str, Any]]]]:
    latest: dict[str, dict[str, Any]] = {}
    history: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for round_name, path in REVIEW_FILES:
        for review in common.read_jsonl(path):
            qid = review["question_id"]
            history[qid].append(
                {
                    "round": round_name,
                    "verdict": review["verdict"],
                    "review_sha256": common.payload_sha256(review),
                    "required_repairs": review.get("required_repairs", []),
                }
            )
            latest[qid] = review
    return latest, history


def find_new_spans(packet: dict[str, Any], ledger: dict[str, Any]) -> list[dict[str, Any]]:
    evidence = {
        row["evidence_id"]: row for row in packet["approved_source_evidence"]
    }
    flags = []
    groups = ledger["claim_groups"] + ledger["constraint_groups"]
    for group in groups:
        for span in group.get("exact_spans", []):
            evidence_id = span["evidence_id"]
            source = evidence[evidence_id]
            text = span["exact_evidence_span"]
            registered = [source["exact_evidence_span"]] + list(
                source.get("unit_exact_spans", [])
            )
            if text in registered:
                continue
            if text not in source["full_chunk_text"]:
                raise RuntimeError(
                    f"{packet['question_id']} {group['claim_group_id']}: "
                    "new exact span is not verbatim in approved full chunk"
                )
            flags.append(
                {
                    "question_id": packet["question_id"],
                    "claim_group_id": group["claim_group_id"],
                    "evidence_id": evidence_id,
                    "doc_id": source["doc_id"],
                    "chunk_id": source["chunk_id"],
                    "new_verbatim_span": text,
                    "registered_exact_span": source["exact_evidence_span"],
                    "audit_decision": "pending",
                    "audit_notes": "",
                }
            )
    return flags


def duplicate_source_groups(packet: dict[str, Any]) -> list[list[str]]:
    duplicate_map: dict[tuple[str, str, str, str], list[str]] = defaultdict(list)
    for evidence in packet["approved_source_evidence"]:
        key = (
            evidence["doc_id"],
            str(evidence["chunk_id"]),
            evidence["exact_evidence_span"],
            evidence["full_chunk_text"],
        )
        duplicate_map[key].append(evidence["evidence_id"])
    return [ids for ids in duplicate_map.values() if len(ids) > 1]


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    if (OUTPUT_DIR / "reference_candidates.jsonl").exists():
        raise RuntimeError(
            "Project-author audit candidates already exist; refusing to overwrite"
        )
    packets = {
        row["question_id"]: row for row in common.read_jsonl(common.REFERENCE_PACKETS)
    }
    ledgers = {row["question_id"]: row for row in common.read_jsonl(LEDGERS)}
    resolutions: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for resolution_path in RESOLUTION_FILES:
        for resolution in common.read_jsonl(resolution_path):
            resolutions[resolution["question_id"]].append(resolution)
    reviews, review_history = latest_reviews()
    expected = set(packets)
    if set(ledgers) != expected or set(reviews) != expected:
        raise RuntimeError("Audit requires complete 40-question ledgers and reviews")
    if any(row["verdict"] != "clean" for row in reviews.values()):
        raise RuntimeError("Audit cannot be built until every latest review is clean")

    candidates = []
    register = []
    new_spans = []
    markdown = [
        "# Test40 L3 project-author audit packet",
        "",
        "Status: **40 project-author decisions pending**",
        "",
        "This packet was constructed without candidate Test40 answers, candidate",
        "retrieved contexts, system identities, or Test40 outcomes. The claim",
        "ledger is normative for future L3 scoring; reference prose is explanatory",
        "and non-normative. Gold evidence is human-audited and non-exhaustive.",
        "",
        "Approve a question only after checking the visible task, every core and",
        "supplementary claim group, every constraint, scoring rules, exact evidence,",
        "and the complete approved source chunks. Newly selected verbatim spans are",
        "listed separately and require an explicit author decision.",
        "",
    ]
    for packet in common.read_jsonl(common.REFERENCE_PACKETS):
        qid = packet["question_id"]
        ledger = ledgers[qid]["draft_ledger"]
        latest_review = reviews[qid]
        flags = find_new_spans(packet, ledger)
        new_spans.extend(flags)
        duplicates = duplicate_source_groups(packet)
        candidate = {
            "question_id": qid,
            "question": packet["question"],
            "task_components": ledger["task_components"],
            "approved_ledger": ledger,
            "approved_source_evidence": packet["approved_source_evidence"],
            "gold_is_non_exhaustive": packet["gold_is_non_exhaustive"],
            "latest_model_b_review": latest_review,
            "model_b_review_history": review_history[qid],
            "deterministic_resolutions": resolutions.get(qid, []),
            "new_full_chunk_span_flags": flags,
            "duplicate_source_evidence_id_groups": duplicates,
            "project_author_checks": {
                "visible_question_and_task_components_approved": False,
                "all_claim_and_constraint_groups_reviewed": False,
                "scoring_rules_approved": False,
                "complete_source_chunks_reviewed": False,
                "new_verbatim_spans_reviewed": len(flags) == 0,
                "all_model_b_issues_resolved": False,
                "reference_prose_consistent": False,
            },
            "project_author_review": {
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
                "latest_model_b_verdict": latest_review["verdict"],
                "claim_group_count": len(ledger["claim_groups"]),
                "constraint_group_count": len(ledger["constraint_groups"]),
                "approved_evidence_count": len(packet["approved_source_evidence"]),
                "new_verbatim_span_count": len(flags),
                "duplicate_source_group_count": len(duplicates),
                "project_author_decision": "pending",
                "review_date": "",
                "resolution_notes": "",
            }
        )
        markdown.extend(
            [
                f"## {qid}",
                "",
                f"**Question:** {packet['question']['question_text']}",
                "",
                "### Task components",
                "",
            ]
        )
        for component in ledger["task_components"]:
            markdown.append(
                f"- `{component['task_component_id']}`: {component['component_text']}"
            )
        markdown.extend(["", "### Normative claim groups", ""])
        for group in ledger["claim_groups"] + ledger["constraint_groups"]:
            markdown.extend(
                [
                    f"#### {group['claim_group_id']}",
                    "",
                    f"- Component: `{group['task_component_id']}`",
                    f"- Importance: `{group['importance']}`",
                    f"- Scoring role: `{group['scoring_role']}`",
                    f"- Proposition: {group.get('canonical_proposition', '')}",
                    f"- Full: {group.get('full_rule', group.get('violation_rule', ''))}",
                    f"- Partial: {group.get('partial_rule', '')}",
                    f"- Contradiction: {group.get('contradiction_rule', '')}",
                    "- Linked exact evidence:",
                ]
            )
            for span in group.get("exact_spans", []):
                marker = " [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]" if any(
                    flag["claim_group_id"] == group["claim_group_id"]
                    and flag["evidence_id"] == span["evidence_id"]
                    and flag["new_verbatim_span"] == span["exact_evidence_span"]
                    for flag in flags
                ) else ""
                markdown.extend(
                    [
                        f"  - `{span['evidence_id']}`{marker}",
                        f"    > {span['exact_evidence_span']}",
                        f"    Supports: {span.get('supports', '')}",
                    ]
                )
            markdown.append("")
        markdown.extend(
            [
                "### Latest independent review",
                "",
                f"Verdict: **{latest_review['verdict']}**",
                "",
                "### Non-normative reference prose",
                "",
                ledger["reference_answer"],
                "",
                "### Unresolved or unsupported boundaries",
                "",
            ]
        )
        markdown.extend(
            f"- {row}" for row in ledger["unresolved_or_unsupported"]
        )
        markdown.extend(["", "### Complete approved source chunks", ""])
        for evidence in packet["approved_source_evidence"]:
            markdown.extend(
                [
                    f"#### {evidence['evidence_id']}",
                    "",
                    f"- Role: `{evidence['evidence_type']}`",
                    f"- Document: `{evidence['doc_id']}`",
                    f"- Chunk: `{evidence['chunk_id']}`",
                    f"- Registered exact span: {evidence['exact_evidence_span']}",
                    "",
                    "```text",
                    evidence["full_chunk_text"],
                    "```",
                    "",
                ]
            )
        if qid in resolutions:
            markdown.extend(
                [
                    "### Deterministic resolution",
                    "",
                    *[
                        f"- {change}"
                        for resolution in resolutions[qid]
                        for change in resolution["changes"]
                    ],
                    "",
                ]
            )
        markdown.extend(["---", ""])

    OUTPUT_DIR.mkdir(parents=True, exist_ok=False)
    candidates_path = OUTPUT_DIR / "reference_candidates.jsonl"
    register_path = OUTPUT_DIR / "decision_register.csv"
    spans_path = OUTPUT_DIR / "new_full_chunk_span_register.csv"
    packet_path = OUTPUT_DIR / "AUTHOR_AUDIT_PACKET.md"
    common.write_jsonl(candidates_path, candidates)
    write_csv(register_path, register)
    write_csv(spans_path, new_spans)
    packet_path.write_text("\n".join(markdown), encoding="utf-8")
    readme = OUTPUT_DIR / "README.md"
    readme.write_text(
        "# Test40 project-author audit\n\n"
        "All 40 candidate-blind ledgers have a latest clean Claude Sonnet review. "
        "Project-author decisions remain pending. Review `AUTHOR_AUDIT_PACKET.md`, "
        "record per-question decisions in `reference_candidates.jsonl`, and record "
        "any newly selected full-chunk span decisions in "
        "`new_full_chunk_span_register.csv`. Do not run formal Test40 L3 scoring "
        "until every question is approved and a final freeze/hash manifest is built.\n",
        encoding="utf-8",
    )
    manifest = {
        "stage": "Test40 L3 project-author audit packet",
        "question_count": len(candidates),
        "latest_model_b_verdicts": dict(
            Counter(row["latest_model_b_review"]["verdict"] for row in candidates)
        ),
        "project_author_decisions": {"pending": len(candidates)},
        "new_full_chunk_span_count": len(new_spans),
        "questions_with_new_full_chunk_spans": len(
            {row["question_id"] for row in new_spans}
        ),
        "candidate_test40_inputs_used": False,
        "ledgers_sha256": common.sha256(LEDGERS),
        "resolution_files": [
            {
                "path": str(path.relative_to(common.ROOT)),
                "sha256": common.sha256(path),
            }
            for path in RESOLUTION_FILES
        ],
        "source_packets_sha256": common.sha256(common.REFERENCE_PACKETS),
        "reference_candidates_sha256": common.sha256(candidates_path),
        "decision_register_sha256": common.sha256(register_path),
        "new_full_chunk_span_register_sha256": common.sha256(spans_path),
        "audit_packet_sha256": common.sha256(packet_path),
        "readme_sha256": common.sha256(readme),
    }
    common.write_json(OUTPUT_DIR / "build_manifest.json", manifest)
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()

from __future__ import annotations

import argparse
import csv
import json
import random
from pathlib import Path
from typing import Any

import common
import run_l3_scoring_v2 as scoring


DEFAULT_REFERENCES = (
    common.PACKAGE / "frozen/reference_claim_ledgers_v2.jsonl"
)


def markdown_safe(text: str) -> str:
    return text.replace("\x00", "")


def evidence_for(reference: dict[str, Any]) -> list[dict[str, str]]:
    evidence: dict[str, str] = {}
    groups = (
        reference["ledger"]["claim_groups"]
        + reference["ledger"]["constraint_groups"]
    )
    for group in groups:
        for span in group.get("exact_spans", []):
            evidence_id = str(span["evidence_id"])
            text = str(span["exact_evidence_span"]).strip()
            if evidence_id in evidence and evidence[evidence_id] != text:
                raise RuntimeError(
                    f"{reference['question_id']}: evidence span differs for "
                    f"{evidence_id}"
                )
            evidence[evidence_id] = text
    return [
        {"evidence_id": evidence_id, "exact_evidence_span": evidence[evidence_id]}
        for evidence_id in sorted(evidence)
    ]


def read_answers(path: Path) -> dict[str, dict[str, Any]]:
    rows = common.read_jsonl(path)
    result = {str(row["question_id"]): row for row in rows}
    if len(result) != len(rows):
        raise RuntimeError(f"Duplicate question ID in {path}")
    return result


def write_register(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--system",
        action="append",
        required=True,
        help="PRIVATE_LABEL=path/to/answers.jsonl; may be repeated",
    )
    parser.add_argument("--references", default=str(DEFAULT_REFERENCES))
    parser.add_argument("--out", required=True)
    parser.add_argument("--seed", type=int, default=20260729)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    references_path = Path(args.references).expanduser().resolve()
    output_dir = Path(args.out).expanduser().resolve()
    public_candidates_path = output_dir / "blinded_candidates.jsonl"
    register_path = output_dir / "adequacy_register.csv"
    packet_path = output_dir / "BLINDED_ADEQUACY_PACKET.md"
    public_manifest_path = output_dir / "build_manifest.json"
    private_dir = output_dir / "sealed_mapping"
    private_mapping_path = private_dir / "private_mapping.jsonl"
    private_manifest_path = private_dir / "private_manifest.json"
    if output_dir.exists() and any(output_dir.iterdir()) and not args.force:
        raise RuntimeError(
            "Blinded adequacy output already exists; refusing to overwrite"
        )
    output_dir.mkdir(parents=True, exist_ok=True)
    private_dir.mkdir(parents=True, exist_ok=True)

    references = {
        row["question_id"]: row for row in common.read_jsonl(references_path)
    }
    systems: list[tuple[str, Path, dict[str, dict[str, Any]]]] = []
    for value in args.system:
        label, separator, raw_path = value.partition("=")
        if not separator or not label or not raw_path:
            raise RuntimeError(f"Invalid --system value: {value}")
        path = Path(raw_path).expanduser().resolve()
        rows = read_answers(path)
        if set(rows) != set(references):
            raise RuntimeError(f"{label}: answer membership differs")
        systems.append((label, path, rows))

    private_rows: list[dict[str, Any]] = []
    public_rows: list[dict[str, Any]] = []
    for label, path, answers in systems:
        source_sha256 = common.sha256(path)
        for qid, reference in references.items():
            raw_answer = scoring.answer_text(answers[qid])
            canonical_answer = scoring.canonicalize_answer(raw_answer)
            private_rows.append(
                {
                    "question_id": qid,
                    "private_system_label": label,
                    "source_answer_file": str(path),
                    "source_answer_file_sha256": source_sha256,
                    "raw_answer_sha256": common.payload_sha256(raw_answer),
                    "canonical_answer_sha256": common.payload_sha256(
                        canonical_answer
                    ),
                    "public_payload": {
                        "question_id": qid,
                        "question_text": reference["question_text"],
                        "task_boundaries": reference["task_boundaries"],
                        "gold_is_non_exhaustive": True,
                        "reference_evidence": evidence_for(reference),
                        "anonymous_candidate_answer": canonical_answer,
                    },
                }
            )

    rng = random.Random(args.seed)
    rng.shuffle(private_rows)
    for index, row in enumerate(private_rows, start=1):
        blind_id = f"D13-A{index:03d}"
        row["blind_id"] = blind_id
        public = {"blind_id": blind_id, **row.pop("public_payload")}
        public_rows.append(public)

    common.write_jsonl(public_candidates_path, public_rows)
    common.write_jsonl(private_mapping_path, private_rows)
    register = [
        {
            "blind_id": row["blind_id"],
            "question_id": row["question_id"],
            "adequacy_decision": "pending",
            "material_scientific_error": "pending",
            "confidence": "",
            "reviewer_role": "project_author",
            "review_date": "",
            "notes": "",
        }
        for row in public_rows
    ]
    write_register(register_path, register)

    markdown = [
        "# Blinded Dev13 adequacy calibration",
        "",
        "Status: **26 labels pending**",
        "",
        "Do not open `sealed_mapping/` or any L3 scoring result before all",
        "labels are finalized. System identity, L3 score, claim-level judge",
        "status, and candidate pairing are intentionally withheld.",
        "",
        "Judge each answer independently. Use the question, task boundaries,",
        "and non-exhaustive reference evidence. Do not count claim groups or",
        "estimate an L3 score.",
        "",
        "Record `yes` only when the answer is scientifically correct,",
        "sufficiently addresses the central researcher task, respects scope",
        "and endpoint distinctions, and has no material error. Record `no`",
        "when a central requirement is missing, endpoints are materially",
        "conflated, the answer overclaims, or a material scientific error",
        "makes it unsuitable. Use `uncertain` only for cases requiring",
        "adjudication before threshold calibration.",
        "",
    ]
    for row in public_rows:
        markdown.extend(
            [
                f"## {row['blind_id']}",
                "",
                f"**Question ID:** `{row['question_id']}`",
                "",
                f"**Question:** {row['question_text']}",
                "",
                f"**Must include:** {row['task_boundaries']['must_include']}",
                "",
                (
                    "**Must not claim:** "
                    f"{row['task_boundaries']['must_not_claim']}"
                ),
                "",
                "### Reference evidence",
                "",
            ]
        )
        for evidence in row["reference_evidence"]:
            markdown.extend(
                [
                    f"**{evidence['evidence_id']}**",
                    "",
                    f"> {markdown_safe(evidence['exact_evidence_span'])}",
                    "",
                ]
            )
        markdown.extend(
            [
                "### Anonymous candidate answer",
                "",
                markdown_safe(row["anonymous_candidate_answer"]),
                "",
                "### Human label",
                "",
                "- Adequate (`yes` / `no` / `uncertain`):",
                "- Material scientific error (`yes` / `no` / `uncertain`):",
                "- Confidence (`high` / `medium` / `low`):",
                "- Notes:",
                "",
                "---",
                "",
            ]
        )
    packet_path.write_text("\n".join(markdown), encoding="utf-8")

    common.write_json(
        public_manifest_path,
        {
            "protocol_id": "l3_gold_reference_dev13_v2",
            "purpose": "blinded binary adequacy labels for Dev threshold calibration",
            "candidate_count": len(public_rows),
            "question_count": len(references),
            "private_system_count": len(systems),
            "shuffle_seed": args.seed,
            "reference_sha256": common.sha256(references_path),
            "blinded_candidates_sha256": common.sha256(public_candidates_path),
            "adequacy_register_sha256": common.sha256(register_path),
            "audit_packet_sha256": common.sha256(packet_path),
            "system_identity_in_public_payload": False,
            "l3_scores_in_public_payload": False,
            "claim_judge_status_in_public_payload": False,
        },
    )
    common.write_json(
        private_manifest_path,
        {
            "warning": "Do not inspect before blinded adequacy labels are frozen.",
            "mapping_sha256": common.sha256(private_mapping_path),
            "private_systems": [
                {
                    "label": label,
                    "answer_file": str(path),
                    "answer_file_sha256": common.sha256(path),
                }
                for label, path, _ in systems
            ],
        },
    )
    print(
        json.dumps(
            {
                "candidate_count": len(public_rows),
                "question_count": len(references),
                "labels": "all pending",
                "system_identity_public": False,
                "l3_scores_public": False,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

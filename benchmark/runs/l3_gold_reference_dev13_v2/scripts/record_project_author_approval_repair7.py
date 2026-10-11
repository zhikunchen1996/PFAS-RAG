from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import common


AUDIT_DIR = common.PACKAGE / "human_review_repair7"
CANDIDATES = AUDIT_DIR / "reference_candidates.jsonl"
REGISTER = AUDIT_DIR / "decision_register.csv"
AUDIT_PACKET = AUDIT_DIR / "HUMAN_AUDIT_PACKET.md"
BUILD_MANIFEST = AUDIT_DIR / "build_manifest.json"
APPROVAL_RECORD = AUDIT_DIR / "project_author_approval_record.json"
REVIEW_DATE = "2026-07-29"
RESOLUTION_NOTES = (
    "The project author reviewed the repair7 Dev13 audit packet and "
    "explicitly approved all 13 claim ledgers for hashing, reference freeze, "
    "and Dev L3 scoring in the Codex task on 2026-07-29."
)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    if APPROVAL_RECORD.exists():
        raise RuntimeError(
            "Repair7 project-author approval is already recorded; refusing "
            "to rewrite its timestamp or hashes."
        )
    candidates = common.read_jsonl(CANDIDATES)
    if len(candidates) != 13:
        raise RuntimeError("Repair7 approval requires exactly 13 candidates")
    question_ids = [row["question_id"] for row in candidates]
    if len(set(question_ids)) != 13:
        raise RuntimeError("Repair7 candidate question IDs are not unique")
    for row in candidates:
        if row.get("model_b_verdict") != "approve":
            raise RuntimeError(
                f"{row['question_id']}: Model B verdict is not approve"
            )
        if row.get("model_b_clean") is not True:
            raise RuntimeError(
                f"{row['question_id']}: Model B review is not clean"
            )
        checks = row["project_author_checks"]
        for key in checks:
            checks[key] = True
        row["human_review"] = {
            "decision": "approve",
            "reviewer_role": "project_author",
            "review_date": REVIEW_DATE,
            "resolution_notes": RESOLUTION_NOTES,
        }

    register = read_csv(REGISTER)
    if {row["question_id"] for row in register} != set(question_ids):
        raise RuntimeError("Decision-register membership differs")
    for row in register:
        row["human_decision"] = "approve"
        row["resolution_notes"] = RESOLUTION_NOTES

    approval_record: dict[str, Any] = {
        "approval_id": "repair7-project-author-approval-2026-07-29",
        "recorded_at_utc": datetime.now(timezone.utc).isoformat(),
        "review_date": REVIEW_DATE,
        "reviewer_role": "project_author",
        "authorization_source": (
            "Explicit user instruction in the shared Codex task: the project "
            "author stated that the repair7 packet had been reviewed, was no "
            "longer pending, could be hashed, and Step 3 should begin."
        ),
        "scope": "all 13 repair7 Dev claim ledgers",
        "question_ids": question_ids,
        "decision": "approve",
        "all_project_author_checks": True,
        "resolution_notes": RESOLUTION_NOTES,
        "candidate_answers_seen_for_this_approval": False,
        "l3_scores_seen_for_this_approval": False,
    }

    common.write_jsonl(CANDIDATES, candidates)
    common.write_csv(REGISTER, register)
    common.write_json(APPROVAL_RECORD, approval_record)

    audit_text = AUDIT_PACKET.read_text(encoding="utf-8")
    audit_text = audit_text.replace(
        "Status: **all project-author decisions pending**",
        "Status: **project-author approved 13/13; ready for reference freeze**",
        1,
    )
    approval_section = (
        "\n\n## Project-author approval record\n\n"
        f"- Review date: {REVIEW_DATE}\n"
        "- Decision: approve all 13 repair7 claim ledgers\n"
        "- Candidate answers seen for this approval: no\n"
        "- L3 scores seen for this approval: no\n"
        f"- Record: `{APPROVAL_RECORD.name}`\n"
    )
    if "## Project-author approval record" not in audit_text:
        audit_text += approval_section
    AUDIT_PACKET.write_text(audit_text, encoding="utf-8")

    manifest = json.loads(BUILD_MANIFEST.read_text(encoding="utf-8"))
    manifest["human_decisions"] = {"approve": 13}
    manifest["project_author_checks_true"] = 13 * 5
    manifest["project_author_approval_record_sha256"] = common.sha256(
        APPROVAL_RECORD
    )
    manifest["reference_candidates_sha256"] = common.sha256(CANDIDATES)
    manifest["decision_register_sha256"] = common.sha256(REGISTER)
    manifest["audit_packet_sha256"] = common.sha256(AUDIT_PACKET)
    common.write_json(BUILD_MANIFEST, manifest)

    print(
        json.dumps(
            {
                "question_count": len(candidates),
                "decision": "approve",
                "project_author_checks_true": 13 * 5,
                "candidate_answers_seen": False,
                "l3_scores_seen": False,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

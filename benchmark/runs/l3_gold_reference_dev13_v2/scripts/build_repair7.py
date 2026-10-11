from __future__ import annotations

import copy
import json
from typing import Any

import common
import run_reference_revision_v2 as revision


PACKETS = (
    common.PACKAGE
    / "reference_build/inputs/reference_packets_repair6.jsonl"
)
SOURCE_REVISIONS = (
    common.PACKAGE
    / "reference_build/revisions/model_a_revisions_v2_repair6.jsonl"
)
SOURCE_REVIEWS = (
    common.PACKAGE
    / "reference_build/reviews/model_b_group_reviews_v2_repair6.jsonl"
)
OUTPUT = (
    common.PACKAGE
    / "reference_build/revisions/model_a_revisions_v2_repair7.jsonl"
)
MANIFEST = OUTPUT.with_name("model_a_revisions_v2_repair7_manifest.json")


def content_group(
    ledger: dict[str, Any],
    group_id: str,
) -> dict[str, Any]:
    matches = [
        row
        for row in ledger["claim_groups"]
        if row["claim_group_id"] == group_id
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one content group: {group_id}")
    return matches[0]


def main() -> None:
    packets = {
        row["question_id"]: row for row in common.read_jsonl(PACKETS)
    }
    ledgers = {
        row["question_id"]: copy.deepcopy(row["revision"])
        for row in common.read_jsonl(SOURCE_REVISIONS)
    }
    tasks = {
        row["question_id"]: row
        for row in common.read_jsonl(revision.TASK_COMPONENTS)
    }
    drafts = {
        row["question_id"]: row["draft"]
        for row in common.read_jsonl(common.DRAFTS)
    }

    group = content_group(ledgers["WF10_002"], "WF10_002-G06")
    group["material_qualifiers"] = [
        (
            "overall destruction and fluorine mass balance are interpretive "
            "outcomes distinct from any single measured endpoint"
        ),
        (
            "the cited SCWO example reports low fluorine mass balance at "
            "425 and 450 C, but exact temperatures are illustrative and are "
            "not required for credit"
        ),
        (
            "undetected fluorinated gas or liquid products are a possible "
            "explanation rather than identified or quantified species"
        ),
    ]
    group["numeric_required"] = False
    group["accepted_numeric_equivalents"] = []
    group["full_rule"] = (
        "Award full if the answer keeps overall destruction and fluorine "
        "mass balance separate from individual endpoints and uses the SCWO "
        "low-fluorine-balance example with appropriate uncertainty about "
        "possible undetected fluorinated products. Exact temperatures are "
        "not required."
    )
    group["partial_rule"] = (
        "Award partial if the answer generally distinguishes destruction or "
        "mass balance from individual endpoints but omits either the SCWO "
        "example or the uncertainty that the fluorinated products were not "
        "identified and quantified."
    )

    for question_id, ledger in ledgers.items():
        revision.validate_revision(
            ledger,
            packets[question_id],
            tasks[question_id],
            drafts[question_id],
        )

    rows = [
        {"question_id": question_id, "revision": ledgers[question_id]}
        for question_id in sorted(ledgers)
    ]
    common.write_jsonl(OUTPUT, rows)
    common.write_json(
        MANIFEST,
        {
            "stage": "Model A deterministic repair7 claim-ledger revision",
            "source_revisions_file": str(
                SOURCE_REVISIONS.relative_to(common.ROOT)
            ),
            "source_revisions_sha256": common.sha256(SOURCE_REVISIONS),
            "source_reviews_file": str(SOURCE_REVIEWS.relative_to(common.ROOT)),
            "source_reviews_sha256": common.sha256(SOURCE_REVIEWS),
            "packets_file": str(PACKETS.relative_to(common.ROOT)),
            "packets_sha256": common.sha256(PACKETS),
            "output_file": str(OUTPUT.relative_to(common.ROOT)),
            "output_sha256": common.sha256(OUTPUT),
            "question_count": len(rows),
            "changed_question_ids": ["WF10_002"],
            "repair": {
                "claim_group_id": "WF10_002-G06",
                "reason": (
                    "Removed an accidental exact-temperature scoring "
                    "requirement from an endpoint-distinction task while "
                    "retaining the source-supported SCWO uncertainty example."
                ),
                "numeric_required": False,
            },
            "candidate_answers_used": False,
            "project_author_decisions_written": False,
        },
    )
    print(
        json.dumps(
            {
                "questions": len(rows),
                "changed_question_ids": ["WF10_002"],
                "output": str(OUTPUT),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

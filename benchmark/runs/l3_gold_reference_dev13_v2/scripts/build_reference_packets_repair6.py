from __future__ import annotations

import copy
import json
from typing import Any

import common


SOURCE = (
    common.PACKAGE
    / "reference_build/inputs/reference_packets_repair5.jsonl"
)
OUTPUT = (
    common.PACKAGE
    / "reference_build/inputs/reference_packets_repair6.jsonl"
)
MANIFEST = OUTPUT.with_name("reference_packets_repair6_manifest.json")


def evidence_record(
    packets: list[dict[str, Any]],
    question_id: str,
    evidence_id: str,
) -> dict[str, Any]:
    packet = next(
        row for row in packets if row["question_id"] == question_id
    )
    matches = [
        row
        for row in packet["gold_evidence"]
        if row["evidence_id"] == evidence_id
    ]
    if len(matches) != 1:
        raise RuntimeError(
            f"Expected one evidence record: {question_id}/{evidence_id}"
        )
    return matches[0]


def main() -> None:
    packets = copy.deepcopy(common.read_jsonl(SOURCE))
    target = evidence_record(packets, "WF10_002", "WF10_002_L3X002")
    old_supported_claim = target["supported_claim"]
    target["supported_claim"] = (
        "Filtration, adsorption, and membrane distillation are described as "
        "treatments that can only concentrate PFAS."
    )
    target["does_not_support"] = (
        "The span does not show that a subsequent degradation step was used "
        "in the same experiment and does not quantify concentration."
    )
    target["repair6_note"] = (
        "Tightened the transferred record to the proposition directly "
        "entailed by its exact evidence span."
    )

    common.write_jsonl(OUTPUT, packets)
    common.write_json(
        MANIFEST,
        {
            "stage": "L3 repair6 reference-packet repair",
            "source_packets_file": str(SOURCE.relative_to(common.ROOT)),
            "source_packets_sha256": common.sha256(SOURCE),
            "output_file": str(OUTPUT.relative_to(common.ROOT)),
            "output_sha256": common.sha256(OUTPUT),
            "question_count": len(packets),
            "evidence_record_count": sum(
                len(row["gold_evidence"]) for row in packets
            ),
            "changed_records": [
                {
                    "question_id": "WF10_002",
                    "evidence_id": "WF10_002_L3X002",
                    "old_supported_claim_sha256": common.payload_sha256(
                        old_supported_claim
                    ),
                    "new_supported_claim": target["supported_claim"],
                    "reason": (
                        "The inherited supported_claim extended beyond the "
                        "transferred exact span. Repair6 retains only the "
                        "directly entailed concentration statement."
                    ),
                }
            ],
            "retrieval_gold_modified": False,
            "candidate_answers_used": False,
            "project_author_decisions_written": False,
        },
    )
    print(
        json.dumps(
            {
                "questions": len(packets),
                "changed_records": 1,
                "output": str(OUTPUT),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

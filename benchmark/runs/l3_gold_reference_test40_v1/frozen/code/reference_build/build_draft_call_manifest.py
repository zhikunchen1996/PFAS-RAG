from __future__ import annotations

import json

import common


def main() -> None:
    valid = common.read_jsonl(common.DRAFTS)
    quarantine = []
    for path in sorted(
        (common.PACKAGE / "reference_build/drafts/quarantine").glob("*.json")
    ):
        quarantine.append(json.loads(path.read_text(encoding="utf-8")))
    rows = valid + quarantine
    response_ids = [row["generation"]["response_id"] for row in rows]
    if len(rows) != 40 or len(set(response_ids)) != 40:
        raise RuntimeError("Expected 40 distinct recorded Model A responses")
    if {row["generation"]["response_model"] for row in rows} != {
        common.EXPECTED_RESPONSE_MODEL
    }:
        raise RuntimeError("Unexpected Model A response snapshot")
    manifest = {
        "stage": "candidate-blind Test40 Model A call accounting",
        "recorded_completed_calls": len(rows),
        "originally_valid_count": len(valid),
        "quarantined_schema_invalid_count": len(quarantine),
        "distinct_response_id_count": len(set(response_ids)),
        "total_tokens": sum(row["generation"]["total_tokens"] for row in rows),
        "estimated_cost_usd": sum(
            row["generation"]["estimated_cost_usd"] for row in rows
        ),
        "latency_seconds_sum": sum(
            row["generation"]["latency_seconds"] for row in rows
        ),
        "unrecorded_failed_attempts": [
            "NQ01 finish_reason=length at 12000-token ceiling",
            "NQ01 pre-quarantine schema-invalid nonnumeric equivalence output",
        ],
        "cost_accounting_limit": (
            "Totals exclude the two unrecorded failed NQ01 smoke attempts."
        ),
        "candidate_test40_inputs_used": False,
    }
    common.write_json(
        common.PACKAGE / "reference_build/drafts/draft_call_manifest.json",
        manifest,
    )
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()

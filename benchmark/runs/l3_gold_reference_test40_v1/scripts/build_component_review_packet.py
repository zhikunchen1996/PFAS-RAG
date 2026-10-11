from __future__ import annotations

import common


def main() -> None:
    sources = {row["question_id"]: row for row in common.read_jsonl(common.SOURCE_PACKETS)}
    components = common.read_jsonl(common.TASK_COMPONENTS)
    rows = []
    for row in components:
        source = sources[row["question_id"]]
        rows.append(
            {
                "question_id": row["question_id"],
                "question": source["question"],
                "task_components": row["task_components"],
                "coverage_check": row["coverage_check"],
            }
        )
    output = (
        common.PACKAGE
        / "reference_build/task_components/component_review_packet.jsonl"
    )
    common.write_jsonl(output, rows)
    common.write_json(
        output.with_name("component_review_packet_manifest.json"),
        {
            "question_count": len(rows),
            "source_packets_sha256": common.sha256(common.SOURCE_PACKETS),
            "task_components_sha256": common.sha256(common.TASK_COMPONENTS),
            "review_packet_sha256": common.sha256(output),
            "candidate_test40_inputs_used": False,
        },
    )


if __name__ == "__main__":
    main()

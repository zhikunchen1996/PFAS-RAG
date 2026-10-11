from __future__ import annotations

import json

import common


def main() -> None:
    source_rows = common.read_jsonl(common.SOURCE_PACKETS)
    component_rows = {
        row["question_id"]: row for row in common.read_jsonl(common.TASK_COMPONENTS)
    }
    if len(source_rows) != 40 or set(component_rows) != {
        row["question_id"] for row in source_rows
    }:
        raise RuntimeError("Source packet and task-component membership differ")

    packets = []
    for source in source_rows:
        component = component_rows[source["question_id"]]
        if component["source_packet_sha256"] != common.payload_sha256(source):
            raise RuntimeError(f"{source['question_id']}: stale task components")
        packets.append(
            {
                "question_id": source["question_id"],
                "question": source["question"],
                "task_components": component["task_components"],
                "gold_is_non_exhaustive": True,
                "approved_source_evidence": source["approved_source_evidence"],
                "author_review_provenance": source["author_review_provenance"],
            }
        )

    common.write_jsonl(common.REFERENCE_PACKETS, packets)
    manifest = {
        "stage": "candidate-blind Test40 reference packet freeze input",
        "question_count": len(packets),
        "gold_record_count": sum(
            len(row["approved_source_evidence"]) for row in packets
        ),
        "source_packets_sha256": common.sha256(common.SOURCE_PACKETS),
        "task_components_sha256": common.sha256(common.TASK_COMPONENTS),
        "reference_packets_sha256": common.sha256(common.REFERENCE_PACKETS),
        "packet_payload_sha256": {
            row["question_id"]: common.payload_sha256(row) for row in packets
        },
        "candidate_test40_inputs_used": False,
    }
    common.write_json(
        common.PACKAGE / "reference_build/inputs/reference_packet_manifest.json",
        manifest,
    )
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()

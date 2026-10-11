from __future__ import annotations

import argparse
import json
from typing import Any

import common


PROMPT = common.PACKAGE / "prompts/task_components_v1.txt"


def validate(result: dict[str, Any], packet: dict[str, Any]) -> None:
    if set(result) != {"question_id", "task_components", "coverage_check"}:
        raise RuntimeError(f"{packet['question_id']}: invalid top-level keys")
    if result["question_id"] != packet["question_id"]:
        raise RuntimeError(f"{packet['question_id']}: question ID changed")
    components = result["task_components"]
    if not isinstance(components, list) or not 1 <= len(components) <= 4:
        raise RuntimeError(f"{packet['question_id']}: expected 1-4 components")
    expected_ids = [
        f"{packet['question_id']}-T{index:02d}"
        for index in range(1, len(components) + 1)
    ]
    actual_ids = [str(row.get("task_component_id", "")) for row in components]
    if actual_ids != expected_ids:
        raise RuntimeError(f"{packet['question_id']}: component IDs not sequential")
    if any(not str(row.get("component_text", "")).strip() for row in components):
        raise RuntimeError(f"{packet['question_id']}: empty component text")
    check = result["coverage_check"]
    for field in [
        "question_covered",
        "must_include_covered",
        "must_not_claim_respected",
    ]:
        if check.get(field) is not True:
            raise RuntimeError(f"{packet['question_id']}: failed {field}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--limit", type=int)
    args = parser.parse_args()

    packets = common.read_jsonl(common.SOURCE_PACKETS)
    items = packets[: args.limit] if args.limit else packets
    prompt = PROMPT.read_text(encoding="utf-8")

    def worker(packet: dict[str, Any]) -> dict[str, Any]:
        payload = {
            "question_id": packet["question_id"],
            "question": packet["question"],
        }
        result, metadata = common.call_openai_json(
            system_prompt=prompt,
            payload=payload,
            max_completion_tokens=3000,
        )
        validate(result, packet)
        return {
            "question_id": packet["question_id"],
            "source_packet_sha256": common.payload_sha256(packet),
            "task_components": result["task_components"],
            "coverage_check": result["coverage_check"],
            "generation": metadata,
        }

    rows = common.run_parallel(
        items=items,
        worker=worker,
        key=lambda row: str(row["question_id"]),
        output=common.TASK_COMPONENTS,
        workers=args.workers,
        resume=args.resume,
    )
    common.write_json(
        common.PACKAGE / "reference_build/task_components/run_manifest.json",
        {
            "stage": "candidate-blind Test40 task-component drafting",
            "question_count": len(rows),
            "model": "gpt-5.1",
            "required_response_model": common.EXPECTED_RESPONSE_MODEL,
            "reasoning_effort": "low",
            "prompt_sha256": common.sha256(PROMPT),
            "source_packets_sha256": common.sha256(common.SOURCE_PACKETS),
            "output_sha256": common.sha256(common.TASK_COMPONENTS),
            "total_tokens": sum(row["generation"]["total_tokens"] for row in rows),
            "estimated_cost_usd": sum(
                row["generation"]["estimated_cost_usd"] for row in rows
            ),
            "latency_seconds_sum": sum(
                row["generation"]["latency_seconds"] for row in rows
            ),
            "candidate_test40_inputs_used": False,
        },
    )
    print(json.dumps({"task_components": len(rows)}, indent=2))


if __name__ == "__main__":
    main()

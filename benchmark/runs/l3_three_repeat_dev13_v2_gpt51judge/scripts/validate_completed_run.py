from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
ROOT = PACKAGE.parents[2]
RESULTS = PACKAGE / "results"
PROMPT = (
    ROOT
    / "benchmark/runs/l3_gold_reference_dev13_v3_continuous/frozen/"
    "l3_gold_referenced_judge_v2.txt"
)
MODEL = "gpt-5.1"
EXPECTED_MODEL = "gpt-5.1-2025-11-13"
REASONING_EFFORT = "low"
MAX_COMPLETION_TOKENS = 12000
SYSTEMS = {
    "gpt51_direct",
    "gpt51_bge_llm_rag",
    "gemini31_direct",
    "gemini31_bge_llm_rag",
    "claude_sonnet5_direct",
    "claude_sonnet5_bge_llm_rag",
}


def read_jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload_sha256(value: object) -> str:
    encoded = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def expected_request_hash(prompt: str, payload: dict) -> str:
    request = {
        "model": MODEL,
        "max_completion_tokens": MAX_COMPLETION_TOKENS,
        "response_format": {"type": "json_object"},
        "messages": [
            {"role": "system", "content": prompt},
            {
                "role": "user",
                "content": json.dumps(payload, ensure_ascii=False),
            },
        ],
        "reasoning_effort": REASONING_EFFORT,
    }
    return payload_sha256(request)


def main() -> None:
    prompt = PROMPT.read_text(encoding="utf-8")
    envelopes = {
        row["item_id"]: row
        for row in read_jsonl(RESULTS / "canonical_envelopes.jsonl")
    }
    assert len(envelopes) == 78
    response_ids = {item_id: set() for item_id in envelopes}
    memberships = []
    for repeat in (1, 2, 3):
        result_path = RESULTS / f"repeat_{repeat}/judge_results.jsonl"
        rows = read_jsonl(result_path)
        assert len(rows) == 78
        assert len({row["item_id"] for row in rows}) == 78
        assert {row["system_label_local_only"] for row in rows} == SYSTEMS
        assert {int(row["repeat_index"]) for row in rows} == {repeat}
        for row in rows:
            envelope = envelopes[row["item_id"]]
            assert row["candidate_id"] == envelope["candidate_id"]
            assert row["source_payload_sha256"] == payload_sha256(
                envelope["model_payload"]
            )
            judge = row["judge"]
            assert judge["request_model"] == MODEL
            assert judge["response_model"] == EXPECTED_MODEL
            assert judge["reasoning_effort"] == REASONING_EFFORT
            assert judge["temperature"] == "provider_default_not_sent"
            assert int(judge["max_completion_tokens"]) == MAX_COMPLETION_TOKENS
            assert judge["finish_reason"] == "stop"
            assert judge["request_sha256"] == expected_request_hash(
                prompt, envelope["model_payload"]
            )
            response_ids[row["item_id"]].add(judge["response_id"])
        memberships.append({row["item_id"] for row in rows})
        manifest = json.loads(
            (RESULTS / f"repeat_{repeat}/run_manifest.json").read_text(
                encoding="utf-8"
            )
        )
        assert manifest["status"] == "complete"
        assert manifest["valid_judgment_count"] == 78
        assert manifest["required_response_model"] == EXPECTED_MODEL
        assert manifest["judge_results_sha256"] == sha256(result_path)
    assert memberships[0] == memberships[1] == memberships[2]
    assert all(len(ids) == 3 for ids in response_ids.values())
    summary = json.loads(
        (RESULTS / "aggregation_summary.json").read_text(encoding="utf-8")
    )
    assert summary["judgment_count"] == 234
    assert summary["new_call_count"] == 234
    assert summary["bootstrap_enabled"] is False
    assert summary["held_out_test40_used"] is False
    assert len(read_csv(RESULTS / "system_three_repeat_summary.csv")) == 6
    assert len(
        read_csv(RESULTS / "matched_effect_three_repeat_summary.csv")
    ) == 3
    post = json.loads(
        (PACKAGE / "post_run_manifest.json").read_text(encoding="utf-8")
    )
    for relative, digest in post["artifacts"].items():
        assert sha256(ROOT / relative) == digest
    print(
        json.dumps(
            {
                "status": "pass",
                "judge_model": EXPECTED_MODEL,
                "judgment_count": 234,
                "held_out_test40_used": False,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

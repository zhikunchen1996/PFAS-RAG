from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


PACKAGE = Path(__file__).resolve().parents[1]
ROOT = PACKAGE.parents[2]
L3 = ROOT / "benchmark/runs/l3_gold_reference_dev13_v3_continuous"
sys.path.insert(0, str(L3 / "scripts"))

import common  # noqa: E402
import run_l3_continuous_scoring_v3 as scoring  # noqa: E402


PROMPT = L3 / "frozen/l3_gold_referenced_judge_v2.txt"
REFERENCES = L3 / "frozen/reference_claim_ledgers_v2.jsonl"
GPT = (
    ROOT
    / "benchmark/runs/l3_gold_reference_dev13_v2/results/"
    "dev13_gpt51_direct_vs_bge_llm_rag_repair7/canonical"
)
MULTIBASE = (
    ROOT / "benchmark/runs/stage4_multibase_dev13_v1/results/l3_v3/canonical"
)
OUT = PACKAGE / "results"
MODEL = "gpt-5.1"
EXPECTED_MODEL = "gpt-5.1-2025-11-13"
REASONING_EFFORT = "low"
MAX_COMPLETION_TOKENS = 12000
SYSTEMS = (
    "gpt51_direct",
    "gpt51_bge_llm_rag",
    "gemini31_direct",
    "gemini31_bge_llm_rag",
    "claude_sonnet5_direct",
    "claude_sonnet5_bge_llm_rag",
)


def all_envelopes() -> list[dict[str, Any]]:
    rows = common.read_jsonl(GPT / "local_envelopes.jsonl")
    rows.extend(common.read_jsonl(MULTIBASE / "local_envelopes.jsonl"))
    lookup = {
        (row["system_label_local_only"], row["question_id"]): row
        for row in rows
    }
    qids = sorted(
        {row["question_id"] for row in common.read_jsonl(REFERENCES)}
    )
    expected = {(system, qid) for system in SYSTEMS for qid in qids}
    if set(lookup) != expected:
        raise RuntimeError("Canonical envelope membership is not 6 x Dev13")
    return [
        {
            "item_id": f"{system}::{qid}",
            "question_id": qid,
            "system_label_local_only": system,
            "candidate_id": lookup[(system, qid)]["candidate_id"],
            "model_payload": lookup[(system, qid)]["model_payload"],
            "source_payload_sha256": common.payload_sha256(
                lookup[(system, qid)]["model_payload"]
            ),
        }
        for system in SYSTEMS
        for qid in qids
    ]


def validate_rows(
    rows: list[dict[str, Any]],
    items: list[dict[str, Any]],
    repeat: int,
    *,
    complete: bool,
) -> None:
    item_lookup = {row["item_id"]: row for row in items}
    actual = {row["item_id"] for row in rows}
    if len(actual) != len(rows) or not actual.issubset(item_lookup):
        raise RuntimeError(f"Repeat {repeat}: invalid item membership")
    if complete and actual != set(item_lookup):
        raise RuntimeError(f"Repeat {repeat}: incomplete item coverage")
    for row in rows:
        item = item_lookup[row["item_id"]]
        if row["candidate_id"] != item["candidate_id"]:
            raise RuntimeError(
                f"Repeat {repeat}/{row['item_id']}: candidate differs"
            )
        if row["judge"]["response_model"] != EXPECTED_MODEL:
            raise RuntimeError(
                f"Repeat {repeat}/{row['item_id']}: unexpected snapshot "
                f"{row['judge']['response_model']}"
            )


def write_manifest(
    repeat: int,
    rows: list[dict[str, Any]],
    *,
    complete: bool,
) -> None:
    repeat_dir = OUT / f"repeat_{repeat}"
    manifest = {
        "protocol_id": "l3_three_repeat_dev13_v2_gpt51judge",
        "repeat_index": repeat,
        "status": "complete" if complete else "partial_smoke_or_resumable",
        "valid_judgment_count": len(rows),
        "new_call_count": len(rows),
        "new_call_tokens": sum(
            row["judge"]["total_tokens"] for row in rows
        ),
        "new_call_cost_usd": sum(
            row["judge"]["estimated_cost_usd"] for row in rows
        ),
        "new_call_latency_seconds_sum": sum(
            row["judge"]["latency_seconds"] for row in rows
        ),
        "request_model": MODEL,
        "required_response_model": EXPECTED_MODEL,
        "response_models": sorted(
            {row["judge"]["response_model"] for row in rows}
        ),
        "reasoning_effort": REASONING_EFFORT,
        "temperature": "provider default; not sent",
        "max_completion_tokens": MAX_COMPLETION_TOKENS,
        "claim_order": "canonical",
        "one_answer_per_request": True,
        "bootstrap_enabled": False,
        "held_out_test40_used": False,
        "judge_results_sha256": common.sha256(
            repeat_dir / "judge_results.jsonl"
        ),
    }
    common.write_json(repeat_dir / "run_manifest.json", manifest)
    print(json.dumps(manifest, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repeat", type=int, choices=[1, 2, 3], required=True)
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--limit", type=int)
    args = parser.parse_args()
    items = all_envelopes()
    references = {
        row["question_id"]: row for row in common.read_jsonl(REFERENCES)
    }
    prompt = PROMPT.read_text(encoding="utf-8")
    OUT.mkdir(parents=True, exist_ok=True)
    common.write_jsonl(OUT / "canonical_envelopes.jsonl", items)
    repeat_dir = OUT / f"repeat_{args.repeat}"
    repeat_dir.mkdir(parents=True, exist_ok=True)
    output = repeat_dir / "judge_results.jsonl"
    selected = items[: args.limit] if args.limit else items

    def worker(item: dict[str, Any]) -> dict[str, Any]:
        result, metadata = common.call_openai_json(
            system_prompt=prompt,
            payload=item["model_payload"],
            model=MODEL,
            reasoning_effort=REASONING_EFFORT,
            max_completion_tokens=MAX_COMPLETION_TOKENS,
            temperature=None,
        )
        if metadata["response_model"] != EXPECTED_MODEL:
            raise RuntimeError(
                f"Unexpected judge snapshot: {metadata['response_model']}"
            )
        reference = references[item["question_id"]]
        scoring.validate_result(result, reference)
        return {
            "item_id": item["item_id"],
            "question_id": item["question_id"],
            "system_label_local_only": item["system_label_local_only"],
            "candidate_id": item["candidate_id"],
            "source_payload_sha256": item["source_payload_sha256"],
            "assessment": result,
            "scores": scoring.score_result(result, reference),
            "judge": metadata,
            "repeat_index": args.repeat,
            "repeat_provenance": "new_gpt51_canonical_call",
        }

    common.run_parallel(
        items=selected,
        worker=worker,
        key=lambda row: str(row["item_id"]),
        output=output,
        workers=args.workers,
        resume=True,
    )
    all_rows = common.read_jsonl(output)
    complete = len(all_rows) == len(items)
    validate_rows(all_rows, items, args.repeat, complete=complete)
    write_manifest(args.repeat, all_rows, complete=complete)


if __name__ == "__main__":
    main()

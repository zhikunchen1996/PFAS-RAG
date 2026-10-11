from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


PILOT = Path(__file__).resolve().parents[1]
ROOT = PILOT.parents[2]
RUN = PILOT / "results/gpt51_dev13_matched_knowledge_v13"
PAIR = RUN / "l2_v4/gpt51_direct_vs_rag"
AGGREGATE = RUN / "l2_v4/aggregate"
REPORT = RUN / "final_report"
SELECTOR = (
    ROOT
    / "benchmark/frozen_v3/results/dev13_retrieval_budget_gpt51_2026-07-26/"
    "bge_llm_gpt51/token_cost_summary.csv"
)
STAGE_COSTS = (
    ROOT
    / "benchmark/frozen_v3/judge/support/layer1_common_tagger_v1/results/"
    "dev13_common_tagger_gpt51_2026-07-26/bge_llm/tokens/stage_costs.csv"
)
GENERATION = RUN / "usage/generation_usage_summary.csv"
CRITERIA = (
    "scientific_correctness",
    "question_fulfillment",
    "scope_and_calibration",
    "practical_usefulness",
)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fields: list[str] = []
    for row in rows:
        for field in row:
            if field not in fields:
                fields.append(field)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def mapped_votes() -> list[dict[str, Any]]:
    envelopes = {
        row["payload_id"]: row
        for row in read_jsonl(PAIR / "local_envelopes.jsonl")
    }
    grouped: dict[tuple[str, str], list[tuple[int, str]]] = defaultdict(list)
    for result in read_jsonl(PAIR / "judge_results.jsonl"):
        envelope = envelopes[result["payload_id"]]
        for criterion, raw in result["judge_result"][
            "criterion_preferences"
        ].items():
            mapped = (
                "tie" if raw == "tie" else envelope["assignment"][raw]
            )
            grouped[(envelope["question_id"], criterion)].append(
                (int(envelope["orientation_index"]), mapped)
            )
    rows = []
    for (qid, criterion), votes in sorted(grouped.items()):
        ordered = [vote for _, vote in sorted(votes)]
        counts = Counter(ordered)
        rows.append(
            {
                "question_id": qid,
                "criterion": criterion,
                "orientation_0_vote": ordered[0],
                "orientation_1_vote": ordered[1],
                "mirrored_agreement": ordered[0] == ordered[1],
                "direct_votes": counts["gpt51_direct"],
                "rag_votes": counts["gpt51_rag"],
                "tie_votes": counts["tie"],
            }
        )
    return rows


def cost_rows() -> list[dict[str, Any]]:
    stage = {row["stage"]: row for row in read_csv(STAGE_COSTS)}
    selector = next(
        row
        for row in read_csv(SELECTOR)
        if row["config_name"] == "bge_llm_gpt51_pool60_bge30_llm10_fullchunk"
    )
    generation = {
        row["stage"]: row
        for row in read_csv(GENERATION)
        if row["stage"].endswith("answer_generation")
    }
    judge = json.loads((PAIR / "run_manifest.json").read_text(encoding="utf-8"))
    selector_cost = (
        int(selector["prompt_tokens"]) * 1.25
        + int(selector["completion_tokens"]) * 10.0
    ) / 1_000_000
    rows = [
        {
            "component": "hybrid_candidate_retrieval",
            "arm": "rag",
            "api_calls": 0,
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0,
            "estimated_cost_usd": 0.0,
            "latency_seconds_sum": float(
                stage["hybrid_candidate_retrieval"]["latency_seconds_sum"]
            ),
            "provenance": "reused_frozen_execution",
        },
        {
            "component": "bge_cross_encoder_rerank",
            "arm": "rag",
            "api_calls": 0,
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0,
            "estimated_cost_usd": 0.0,
            "latency_seconds_sum": float(
                stage["bge_cross_encoder_rerank"]["latency_seconds_sum"]
            ),
            "provenance": "reused_frozen_execution",
        },
        {
            "component": "bge_llm_selector",
            "arm": "rag",
            "api_calls": int(selector["api_calls"]),
            "prompt_tokens": int(selector["prompt_tokens"]),
            "completion_tokens": int(selector["completion_tokens"]),
            "total_tokens": int(selector["total_tokens"]),
            "estimated_cost_usd": selector_cost,
            "latency_seconds_sum": float(
                stage["retrieval_specific_llm_selector"][
                    "latency_seconds_sum"
                ]
            ),
            "provenance": "reused_frozen_execution",
        },
        {
            "component": "common_soft_tagger",
            "arm": "rag",
            "api_calls": int(stage["common_soft_tagger"]["call_count"]),
            "prompt_tokens": int(
                stage["common_soft_tagger"]["prompt_tokens_total"]
            ),
            "completion_tokens": int(
                stage["common_soft_tagger"]["completion_tokens_total"]
            ),
            "total_tokens": int(stage["common_soft_tagger"]["total_tokens"]),
            "estimated_cost_usd": float(
                stage["common_soft_tagger"]["estimated_usd"]
            ),
            "latency_seconds_sum": float(
                stage["common_soft_tagger"]["latency_seconds_sum"]
            ),
            "provenance": "reused_frozen_execution",
        },
    ]
    for arm in ("direct", "rag"):
        source = generation[f"{arm}_answer_generation"]
        rows.append(
            {
                "component": f"{arm}_answer_generation",
                "arm": arm,
                "api_calls": int(source["api_call_count"]),
                "prompt_tokens": int(source["prompt_tokens"]),
                "completion_tokens": int(source["completion_tokens"]),
                "total_tokens": int(source["total_tokens"]),
                "estimated_cost_usd": float(source["estimated_cost_usd"]),
                "latency_seconds_sum": float(
                    source["api_latency_seconds_sum"]
                ),
                "wall_clock_seconds": float(source["wall_clock_seconds"]),
                "provenance": "current_v1_3_execution",
            }
        )
    judge_rows = read_jsonl(PAIR / "judge_results.jsonl")
    rows.append(
        {
            "component": "l2_v4_judge",
            "arm": "evaluation",
            "api_calls": judge["call_count"],
            "prompt_tokens": sum(row["prompt_tokens"] for row in judge_rows),
            "completion_tokens": sum(
                row["completion_tokens"] for row in judge_rows
            ),
            "total_tokens": judge["total_tokens"],
            "estimated_cost_usd": judge["estimated_cost_usd"],
            "latency_seconds_sum": judge["latency_seconds_sum"],
            "wall_clock_seconds": judge["wall_clock_seconds"],
            "provenance": "current_l2_v4_execution",
        }
    )
    direct_cost = next(
        row["estimated_cost_usd"]
        for row in rows
        if row["component"] == "direct_answer_generation"
    )
    rag_cost = sum(
        row["estimated_cost_usd"] for row in rows if row["arm"] == "rag"
    )
    judge_cost = judge["estimated_cost_usd"]
    rows.extend(
        [
            {
                "component": "direct_deployment_total",
                "arm": "summary",
                "estimated_cost_usd": direct_cost,
                "latency_seconds_sum": sum(
                    row["latency_seconds_sum"]
                    for row in rows
                    if row["arm"] == "direct"
                ),
                "provenance": "derived",
            },
            {
                "component": "rag_deployment_total",
                "arm": "summary",
                "estimated_cost_usd": rag_cost,
                "latency_seconds_sum": sum(
                    row["latency_seconds_sum"]
                    for row in rows
                    if row["arm"] == "rag"
                ),
                "provenance": "derived",
            },
            {
                "component": "current_v1_3_plus_v4_new_api_total",
                "arm": "summary",
                "estimated_cost_usd": direct_cost
                + next(
                    row["estimated_cost_usd"]
                    for row in rows
                    if row["component"] == "rag_answer_generation"
                )
                + judge_cost,
                "provenance": "derived; selector_and_tagger_reused",
            },
            {
                "component": "full_pipeline_equivalent_plus_judge",
                "arm": "summary",
                "estimated_cost_usd": direct_cost + rag_cost + judge_cost,
                "provenance": "derived",
            },
        ]
    )
    return rows


def main() -> None:
    REPORT.mkdir(parents=True, exist_ok=True)
    votes = mapped_votes()
    costs = cost_rows()
    write_csv(REPORT / "per_question_l2_votes.csv", votes)
    write_csv(REPORT / "cost_latency_summary.csv", costs)
    fit = json.loads(
        (AGGREGATE / "fit_manifest.json").read_text(encoding="utf-8")
    )
    summary = {
        "status": "complete_dev13_calibration",
        "canonical_generation": str(RUN.relative_to(ROOT)),
        "canonical_judge": "L2 V4 citation-blind evaluable-boundary calibration",
        "question_count": 13,
        "generation_answer_count": 26,
        "judge_call_count": 26,
        "raw_vote_counts": read_csv(AGGREGATE / "raw_vote_counts.csv"),
        "criterion_abilities": read_csv(
            AGGREGATE / "criterion_abilities.csv"
        ),
        "mirrored_agreement": read_csv(
            AGGREGATE / "mirrored_agreement.csv"
        ),
        "position_bias": read_csv(AGGREGATE / "position_bias.csv"),
        "bootstrap": fit["bootstrap"],
        "cost_summary": {
            row["component"]: row["estimated_cost_usd"]
            for row in costs
            if row["component"].endswith("total")
        },
    }
    (REPORT / "pilot_summary.json").write_text(
        json.dumps(summary, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

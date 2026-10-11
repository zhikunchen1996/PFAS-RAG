from __future__ import annotations

import csv
import hashlib
import json
import sys
from collections import defaultdict
from pathlib import Path
from statistics import mean
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
RUN = (
    ROOT
    / "benchmark/frozen_v3/results/dev13_retrieval_budget_gpt51_2026-07-26"
)
LOCAL = RUN / "local_hybrid_bge"
LLM = RUN / "bge_llm_gpt51"
PROMOTED_ARTIFACTS = (
    ROOT
    / "benchmark/frozen_v3/methods/promoted_reusable_artifacts.json"
)
GOLD = ROOT / "benchmark/frozen_v3/gold/chunk_based_gold.jsonl"
sys.path.insert(0, str(ROOT / "benchmark/frozen_v3/scripts"))

from retrieval_metrics import eval_context  # noqa: E402


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
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fields,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def rel(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT))


def number(row: dict[str, str], field: str) -> float:
    return float(row.get(field, "0") or 0)


def integer(row: dict[str, str], field: str) -> int:
    return int(float(row.get(field, "0") or 0))


def main() -> None:
    rows: list[dict[str, Any]] = []
    local_runtime = {
        row["config_name"]: row
        for row in read_csv(LOCAL / "runtime_metrics.csv")
    }
    for row in read_csv(LOCAL / "summary_retrieval_metrics.csv"):
        final_k = integer(row, "top_k")
        doc_field = (
            "mean_final_gold_doc_recall@20"
            if final_k == 20
            else "mean_final_gold_doc_recall@10"
        )
        runtime = local_runtime[row["config_name"]]
        rows.append(
            {
                "system": (
                    "Hybrid"
                    if row["system_family"] == "hybrid"
                    else "BGE"
                ),
                "config_name": row["config_name"],
                "final_top_k": final_k,
                "bge_shortlist_k": "",
                "initial_pool_k": integer(row, "candidate_k"),
                "required_gold_recall": number(
                    row,
                    "mean_final_required_gold_recall@full_context",
                ),
                "gold_document_recall": number(row, doc_field),
                "MRR_required_gold": number(
                    row,
                    "mean_final_MRR_required_gold",
                ),
                "hit_any_required_gold_questions": integer(
                    row,
                    "hit_any_final_full_context",
                ),
                "required_question_count": integer(
                    row,
                    "required_question_count",
                ),
                "api_calls": 0,
                "prompt_tokens": 0,
                "completion_tokens": 0,
                "total_tokens": 0,
                "estimated_selector_cost_usd": 0.0,
                "retrieval_seconds_total": number(
                    runtime,
                    "hybrid_candidate_retrieval_seconds_total",
                ),
                "bge_seconds_total": number(
                    runtime,
                    "bge_scoring_seconds_total",
                ),
                "selector_seconds_total": 0.0,
            }
        )

    tokens = {
        row["config_name"]: row
        for row in read_csv(LLM / "token_cost_summary.csv")
    }
    for row in read_csv(LLM / "summary_retrieval_metrics.csv"):
        final_k = integer(row, "final_top_k")
        doc_field = (
            "mean_final_gold_doc_recall@20"
            if final_k == 20
            else "mean_final_gold_doc_recall@10"
        )
        token_row = tokens[row["config_name"]]
        prompt_tokens = integer(token_row, "prompt_tokens")
        completion_tokens = integer(token_row, "completion_tokens")
        rows.append(
            {
                "system": "BGE-LLM",
                "config_name": row["config_name"],
                "final_top_k": final_k,
                "bge_shortlist_k": integer(row, "bge_shortlist_k"),
                "initial_pool_k": integer(row, "pool_k"),
                "required_gold_recall": number(
                    row,
                    "mean_final_required_gold_recall@full_context",
                ),
                "gold_document_recall": number(row, doc_field),
                "MRR_required_gold": number(
                    row,
                    "mean_final_MRR_required_gold",
                ),
                "hit_any_required_gold_questions": integer(
                    row,
                    "hit_any_final_full_context",
                ),
                "required_question_count": integer(
                    row,
                    "required_question_count",
                ),
                "api_calls": integer(token_row, "api_calls"),
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "total_tokens": integer(token_row, "total_tokens"),
                "estimated_selector_cost_usd": (
                    prompt_tokens * 1.25 / 1_000_000
                    + completion_tokens * 10.0 / 1_000_000
                ),
                "retrieval_seconds_total": "inherited matched local pool",
                "bge_seconds_total": "inherited matched local shortlist",
                "selector_seconds_total": number(
                    row,
                    "llm_seconds_total",
                ),
            }
        )

    order = {"Hybrid": 0, "BGE": 1, "BGE-LLM": 2}
    rows.sort(key=lambda row: (order[row["system"]], row["final_top_k"]))
    write_csv(RUN / "dev13_retrieval_budget_summary.csv", rows)

    system_by_config = {
        str(row["config_name"]): str(row["system"]) for row in rows
    }
    gold_by_qid: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in read_jsonl(GOLD):
        gold_by_qid[str(record["question_id"])].append(record)
    negative_rows: list[dict[str, Any]] = []
    output_paths = sorted(
        (LOCAL / "retrieval_outputs").glob("*.jsonl")
    ) + sorted((LLM / "retrieval_outputs").glob("*.jsonl"))
    for output_path in output_paths:
        for output in read_jsonl(output_path):
            qid = str(output["question_id"])
            config_name = str(output["retrieval_config_name"])
            context = output["retrieved_context"]
            metrics = eval_context(
                qid,
                gold_by_qid.get(qid, []),
                context,
                config_name,
                str(output.get("retrieval_method", "")),
                int(output.get("top_k") or len(context)),
                int(output.get("retrieval_k") or len(context)),
                int(output.get("context_window") or 0),
            )
            negative_rows.append(
                {
                    "system": system_by_config[config_name],
                    "config_name": config_name,
                    "question_id": qid,
                    "negative_gold_count": metrics["negative_gold_count"],
                    "negative_gold_recall@5": metrics[
                        "negative_gold_recall@5"
                    ],
                    "negative_gold_recall@10": metrics[
                        "negative_gold_recall@10"
                    ],
                    "negative_gold_recall@20": metrics[
                        "negative_gold_recall@20"
                    ],
                    "negative_gold_recall@full_context": metrics[
                        "negative_gold_recall@full_context"
                    ],
                }
            )
    write_csv(RUN / "negative_gold_retrieval_per_question.csv", negative_rows)
    negative_groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in negative_rows:
        if int(row["negative_gold_count"]) > 0:
            negative_groups[str(row["config_name"])].append(row)
    negative_summary: list[dict[str, Any]] = []
    for config_name, group in sorted(
        negative_groups.items(),
        key=lambda item: (
            order[system_by_config[item[0]]],
            next(
                int(row["final_top_k"])
                for row in rows
                if row["config_name"] == item[0]
            ),
        ),
    ):
        negative_summary.append(
            {
                "system": system_by_config[config_name],
                "config_name": config_name,
                "negative_gold_applicable_questions": len(group),
                "mean_negative_gold_recall@full_context": mean(
                    float(row["negative_gold_recall@full_context"])
                    for row in group
                ),
            }
        )
    write_csv(RUN / "negative_gold_retrieval_summary.csv", negative_summary)

    selector_calls = read_jsonl(LLM / "selector_calls.jsonl")
    prompt_texts = {
        row["system_prompt"] for row in selector_calls
    }
    if len(prompt_texts) != 1:
        raise RuntimeError("Selector calls do not share one system prompt")
    if len(selector_calls) != 39:
        raise RuntimeError(
            f"Expected 39 selector calls; found {len(selector_calls)}"
        )
    fallback_by_config: dict[str, int] = {}
    for output_path in sorted(
        (LLM / "retrieval_outputs").glob("*.jsonl")
    ):
        for row in read_jsonl(output_path):
            config_name = str(row["retrieval_config_name"])
            fallback_by_config[config_name] = (
                fallback_by_config.get(config_name, 0)
                + sum(
                    "fallback after selector" in str(
                        hit.get("llm_reason", "")
                    )
                    for hit in row["retrieved_context"]
                )
            )
    fallback_count = sum(fallback_by_config.values())

    copied_files = sorted(path for path in LOCAL.rglob("*") if path.is_file())
    copied_by_name = {
        str(path.relative_to(LOCAL)): sha256(path)
        for path in copied_files
    }
    promotion = json.loads(
        PROMOTED_ARTIFACTS.read_text(encoding="utf-8")
    )
    reusable = promotion["artifacts"]["hybrid_bge_budget_results"]
    if reusable["copied_file_sha256"] != copied_by_name:
        raise RuntimeError(
            "Promoted Hybrid/BGE package differs from its locked V3 hashes"
        )

    total_prompt = sum(int(row["prompt_tokens"]) for row in selector_calls)
    total_completion = sum(
        int(row["completion_tokens"]) for row in selector_calls
    )
    estimated_cost = (
        total_prompt * 1.25 / 1_000_000
        + total_completion * 10.0 / 1_000_000
    )
    manifest = {
        "run_id": "dev13_retrieval_budget_gpt51_2026-07-26",
        "status": "frozen_dev13_retrieval_budget",
        "questions": 13,
        "required_gold_applicable_questions": 12,
        "negative_gold_applicable_questions": len(
            {
                row["question_id"]
                for row in negative_rows
                if int(row["negative_gold_count"]) > 0
            }
        ),
        "negative_gold_metric": (
            "Reported separately as secondary limitation-evidence retrieval; "
            "not included in required-gold recall or MRR."
        ),
        "systems": {
            "Hybrid": ["5/30", "10/60", "20/120"],
            "BGE": ["5/30", "10/60", "20/120"],
            "BGE-LLM": ["5/15/30", "10/30/60", "20/60/120"],
        },
        "reusable_results_provenance": rel(PROMOTED_ARTIFACTS),
        "historical_source_path": reusable["historical_source_path"],
        "runtime_dependency_on_historical_source": False,
        "copied_package_byte_identical": True,
        "bge_model": "BAAI/bge-reranker-base",
        "selector_model_requested": "gpt-5.1",
        "selector_models_returned": sorted(
            {str(row["model_returned"]) for row in selector_calls}
        ),
        "selector_temperature": 0,
        "selector_full_chunks": True,
        "selector_input": "visible_question_only",
        "selector_fallback_policy": (
            "When fewer than final_top_k valid IDs are returned, append the "
            "highest remaining BGE-ranked chunks."
        ),
        "selector_fallback_selected_chunks": fallback_count,
        "selector_fallback_selected_chunks_by_config": fallback_by_config,
        "selector_prompt": (
            "benchmark/frozen_v3/prompts/retrieval/"
            "bge_llm_selector_v3.txt"
        ),
        "selector_api_calls": len(selector_calls),
        "selector_prompt_tokens": total_prompt,
        "selector_completion_tokens": total_completion,
        "selector_total_tokens": total_prompt + total_completion,
        "estimated_selector_cost_usd": estimated_cost,
        "price_basis_usd_per_million": {
            "input": 1.25,
            "output": 10.0,
        },
        "promoted_hybrid_bge_file_sha256": copied_by_name,
    }

    lines = [
        "# Dev13 Retrieval Budget Sweep with GPT-5.1",
        "",
        "Hybrid and BGE outputs are hash-locked, byte-identical reusable "
        "results promoted from Frozen V2. Runtime validation uses only the "
        "internal V3 copy. All BGE-LLM rows were rerun with GPT-5.1, "
        "temperature 0, the visible question, and complete candidate chunks.",
        "",
        "| System | Budget | Required-gold recall | Gold-document recall | MRR | Hit any | Selector tokens |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in rows:
        budget = (
            f"{row['final_top_k']}/{row['initial_pool_k']}"
            if row["system"] != "BGE-LLM"
            else (
                f"{row['final_top_k']}/{row['bge_shortlist_k']}/"
                f"{row['initial_pool_k']}"
            )
        )
        lines.append(
            f"| {row['system']} | {budget} | "
            f"{float(row['required_gold_recall']):.3f} | "
            f"{float(row['gold_document_recall']):.3f} | "
            f"{float(row['MRR_required_gold']):.3f} | "
            f"{row['hit_any_required_gold_questions']}/"
            f"{row['required_question_count']} | "
            f"{row['total_tokens']} |"
        )
    bge_llm_rows = [row for row in rows if row["system"] == "BGE-LLM"]
    lines.extend(
        [
            "",
            "Required-gold recall, gold-document recall, and MRR are macro-"
            "averaged over the 12 of 13 Dev questions with at least one "
            "required-gold record. Negative-gold retrieval is reported "
            "separately in `negative_gold_retrieval_summary.csv`.",
            "",
            "## Cost",
            "",
            f"Total selector calls: {len(selector_calls)}.",
            f"Total selector tokens: {total_prompt + total_completion:,}.",
            "Estimated selector cost: "
            f"USD {estimated_cost:.4f}.",
            "The deterministic BGE fallback filled "
            f"{fallback_count} final-context positions when the selector "
            "returned fewer than the requested number of valid IDs.",
            "",
            "Mean BGE-LLM required-gold recall across budgets: "
            f"{mean(row['required_gold_recall'] for row in bge_llm_rows):.3f}.",
        ]
    )
    (RUN / "README.md").write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )
    result_files = sorted(
        path
        for path in RUN.rglob("*")
        if path.is_file() and path.name != "budget_manifest.json"
    )
    manifest["result_file_sha256"] = {
        rel(path): sha256(path) for path in result_files
    }
    (RUN / "budget_manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote finalized budget package to {RUN}")


if __name__ == "__main__":
    main()

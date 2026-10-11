from __future__ import annotations

import argparse
import re
from pathlib import Path
from statistics import mean
from typing import Any

import common


SYSTEMS = ("hybrid", "bge", "bge_llm")
CITATION_RE = re.compile(r"\[C(\d+)\]", re.IGNORECASE)
VALID = {
    "supported",
    "partially_supported",
    "not_supported",
    "contradicted",
}
PASS = {"supported", "partially_supported"}


def answer_path(root: Path, system: str) -> Path:
    return root / system / "answers/tagged_rag_gpt51.jsonl"


def complete_context(answer: dict[str, Any]) -> list[dict[str, str]]:
    contexts = answer.get("retrieved_context")
    if not isinstance(contexts, list) or len(contexts) != 10:
        raise RuntimeError(f"{answer.get('question_id')}: expected 10 chunks")
    by_rank = {int(row["rank"]): row for row in contexts}
    if len(by_rank) != 10:
        raise RuntimeError(f"{answer.get('question_id')}: duplicate rank")
    cited = {int(value) for value in CITATION_RE.findall(answer["answer"])}
    if cited - set(by_rank):
        raise RuntimeError(
            f"{answer.get('question_id')}: citation lacks original chunk"
        )
    return [
        {
            "citation_id": f"C{rank}",
            "text": str(by_rank[rank].get("text", "")),
        }
        for rank in sorted(by_rank)
    ]


def validate_result(
    result: dict[str, Any],
    item_id: str,
    valid_citation_ids: set[str],
) -> None:
    cited = result.get("cited_claims")
    uncited = result.get("uncited_source_dependent_claims")
    if not isinstance(cited, list) or not isinstance(uncited, list):
        raise RuntimeError(f"{item_id}: invalid L1.5 claim lists")
    claim_ids = []
    for row in cited:
        if not isinstance(row, dict):
            raise RuntimeError(f"{item_id}: non-object cited claim")
        if row.get("support") not in VALID:
            raise RuntimeError(f"{item_id}: invalid cited support label")
        citation_ids = row.get("citation_ids")
        if (
            not str(row.get("claim_id") or "").strip()
            or not str(row.get("claim") or "").strip()
            or not isinstance(citation_ids, list)
            or not citation_ids
            or any(value not in valid_citation_ids for value in citation_ids)
        ):
            raise RuntimeError(f"{item_id}: invalid cited claim schema")
        claim_ids.append(str(row["claim_id"]))
    for row in uncited:
        if not isinstance(row, dict):
            raise RuntimeError(f"{item_id}: non-object uncited claim")
        if row.get("support_in_supplied_context") not in VALID:
            raise RuntimeError(f"{item_id}: invalid uncited support label")
        if (
            not str(row.get("claim_id") or "").strip()
            or not str(row.get("claim") or "").strip()
        ):
            raise RuntimeError(f"{item_id}: invalid uncited claim schema")
        claim_ids.append(str(row["claim_id"]))
    if len(claim_ids) != len(set(claim_ids)):
        raise RuntimeError(f"{item_id}: duplicate L1.5 claim IDs")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--generation-root", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = Path(args.generation_root).expanduser().resolve()
    common.require_exact_path(
        root,
        common.GENERATION_RESULTS,
        label="L1.5 generation input",
    )
    qids = common.question_ids()
    questions = {
        row["question_id"]: row for row in common.read_csv(common.QUESTIONS)
    }
    answer_files = {
        system: answer_path(root, system) for system in SYSTEMS
    }
    items = []
    for system in SYSTEMS:
        answers = common.ordered_rows(
            common.read_jsonl(answer_files[system]),
            qids,
            source=f"L1.5 {system}",
        )
        for answer in answers:
            qid = str(answer["question_id"])
            payload = {
                "question": questions[qid]["question_text"],
                "answer_with_citations": answer["answer"],
                "complete_original_final_context": complete_context(answer),
            }
            items.append(
                {
                    "item_id": f"{system}::{qid}",
                    "question_id": qid,
                    "system": system,
                    "payload": payload,
                }
            )
    if len(items) != 120:
        raise RuntimeError("Expected 3 systems x 40 L1.5 payloads")

    prompt = common.L15_PROMPT.read_text(encoding="utf-8")

    def request(item: dict[str, Any]) -> dict[str, Any]:
        return common.json_request(
            system_prompt=prompt,
            payload=item["payload"],
            reasoning_effort="low",
            max_completion_tokens=12000,
            temperature=None,
        )

    out = Path(args.out).expanduser().resolve()
    common.require_exact_path(
        out,
        common.L15_RESULTS,
        label="L1.5 output",
    )
    out.mkdir(parents=True, exist_ok=True)
    common.write_jsonl(
        out / "model_payloads.jsonl",
        [
            {
                "item_id": item["item_id"],
                "question_id": item["question_id"],
                "model_payload": item["payload"],
                "execution_sha256": common.payload_sha256(request(item)),
            }
            for item in items
        ],
    )
    if args.dry_run:
        print("DRY RUN PASS: 120 L1.5 payloads built; no API calls.")
        return
    results_path = out / "judge_results.jsonl"
    if results_path.exists() and not args.resume:
        raise RuntimeError(
            "L1.5 results already exist; use --resume to avoid duplicate calls"
        )

    def worker(item: dict[str, Any]) -> dict[str, Any]:
        result, metadata, request_hash = common.call_json(
            system_prompt=prompt,
            payload=item["payload"],
            reasoning_effort="low",
            max_completion_tokens=12000,
            temperature=None,
        )
        validate_result(
            result,
            item["item_id"],
            {f"C{rank}" for rank in range(1, 11)},
        )
        return {
            "item_id": item["item_id"],
            "question_id": item["question_id"],
            "system": item["system"],
            "execution_sha256": request_hash,
            "judge_result": result,
            "metadata": metadata,
        }

    rows = common.run_resumable(
        items=items,
        key=lambda row: str(row["item_id"]),
        expected_execution_hash=lambda item: common.payload_sha256(
            request(item)
        ),
        worker=worker,
        output=results_path,
        workers=args.workers,
        resume=args.resume,
        label="Test40 L1.5",
    )

    per_question = []
    for row in rows:
        result = row["judge_result"]
        cited = result["cited_claims"]
        uncited = result["uncited_source_dependent_claims"]
        labels = [str(value["support"]) for value in cited]
        per_question.append(
            {
                "system": row["system"],
                "question_id": row["question_id"],
                "citation_support_applicable": bool(cited),
                "cited_claim_count": len(cited),
                "citation_supported_claim_count": sum(
                    label in PASS for label in labels
                ),
                "citation_unsupported_claim_count": sum(
                    label == "not_supported" for label in labels
                ),
                "citation_contradicted_claim_count": sum(
                    label == "contradicted" for label in labels
                ),
                "claim_supported_by_any_citation_rate": (
                    sum(label in PASS for label in labels) / len(labels)
                    if labels
                    else ""
                ),
                "uncited_source_dependent_claim_count": len(uncited),
            }
        )

    summaries = []
    for system in SYSTEMS:
        values = [row for row in per_question if row["system"] == system]
        cited_total = sum(int(row["cited_claim_count"]) for row in values)
        supported_total = sum(
            int(row["citation_supported_claim_count"]) for row in values
        )
        question_rates = [
            float(row["claim_supported_by_any_citation_rate"])
            for row in values
            if row["claim_supported_by_any_citation_rate"] != ""
        ]
        summaries.append(
            {
                "system": system,
                "question_count": len(values),
                "applicable_question_count": sum(
                    bool(row["citation_support_applicable"]) for row in values
                ),
                "cited_claim_count": cited_total,
                "claim_supported_by_any_citation_rate": (
                    supported_total / cited_total if cited_total else ""
                ),
                "mean_question_level_support_rate": (
                    mean(question_rates) if question_rates else ""
                ),
                "unsupported_claim_count": sum(
                    int(row["citation_unsupported_claim_count"])
                    for row in values
                ),
                "contradicted_claim_count": sum(
                    int(row["citation_contradicted_claim_count"])
                    for row in values
                ),
                "uncited_source_dependent_claim_count": sum(
                    int(row["uncited_source_dependent_claim_count"])
                    for row in values
                ),
            }
        )
    common.write_csv(out / "per_question.csv", per_question)
    common.write_csv(out / "summary.csv", summaries)
    common.write_json(
        out / "run_manifest.json",
        {
            "protocol_id": "test40_formal_v1_l15",
            "status": "complete",
            "question_count": 40,
            "systems": list(SYSTEMS),
            "model": common.MODEL,
            "required_snapshot": common.EXPECTED_MODEL,
            "reasoning_effort": "low",
            "temperature": "provider_default_not_sent",
            "prompt_sha256": common.sha256(common.L15_PROMPT),
            "answer_inputs": {
                system: {
                    "path": common.project_relative(path),
                    "sha256": common.sha256(path),
                }
                for system, path in answer_files.items()
            },
            "api_calls": len(rows),
            "total_tokens": sum(
                int(row["metadata"]["total_tokens"]) for row in rows
            ),
            "estimated_cost_usd": sum(
                float(row["metadata"]["estimated_cost_usd"]) for row in rows
            ),
            "latency_seconds_sum": sum(
                float(row["metadata"]["latency_seconds"]) for row in rows
            ),
            "resume_hash_validated": True,
        },
    )


if __name__ == "__main__":
    main()

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from statistics import mean
from typing import Any, Callable


PACKAGE = Path(__file__).resolve().parents[1]
ROOT = PACKAGE.parents[2]
SOURCE_PACKAGE = ROOT / "benchmark/runs/test40_multibase_direct_rag_v1"
SOURCE_SCRIPTS = SOURCE_PACKAGE / "scripts"
sys.path.insert(0, str(SOURCE_SCRIPTS))
import common as source_common  # noqa: E402


QUESTIONS = SOURCE_PACKAGE / "frozen/questions_test40.csv"
PROMPT = ROOT / "benchmark/frozen_v3/judge/prompts/l15_claim_citation_support_v2.txt"
SOURCE_PROTOCOL = SOURCE_PACKAGE / "protocol.json"
RESULTS = PACKAGE / "results/l15"
PREFLIGHT_PAYLOADS = PACKAGE / "preflight/model_payloads.jsonl"
PREFLIGHT_REPORT = PACKAGE / "preflight_report.json"
PRE_RUN_MANIFEST = PACKAGE / "pre_run_manifest.json"

SYSTEMS = {
    "gpt51_rag": SOURCE_PACKAGE / "results/generation/gpt51_rag/answers.jsonl",
    "gemini31_pro_rag": SOURCE_PACKAGE
    / "results/generation/gemini31_pro_rag/answers.jsonl",
    "claude_sonnet5_rag": SOURCE_PACKAGE
    / "results/generation/claude_sonnet5_rag/answers.jsonl",
}

CITATION_RE = re.compile(r"\[C(\d+)\]", re.IGNORECASE)
VALID = {"supported", "partially_supported", "not_supported", "contradicted"}
PASS = {"supported", "partially_supported"}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload_sha256(value: Any) -> str:
    encoded = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError as exc:
                raise RuntimeError(f"{path}:{line_number}: {exc}") from exc
            if not isinstance(value, dict):
                raise RuntimeError(f"{path}:{line_number}: expected object")
            rows.append(value)
    return rows


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        raise RuntimeError(f"Refusing to write empty CSV: {path}")
    fields: list[str] = []
    for row in rows:
        for key in row:
            if key not in fields:
                fields.append(key)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def request_payload(system_prompt: str, payload: dict[str, Any]) -> dict[str, Any]:
    return {
        "model": source_common.OPENAI_MODEL,
        "response_format": {"type": "json_object"},
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": json.dumps(payload, ensure_ascii=False)},
        ],
        "max_completion_tokens": 12000,
        "reasoning_effort": "low",
    }


def complete_context(answer: dict[str, Any]) -> list[dict[str, str]]:
    qid = str(answer.get("question_id") or "")
    contexts = answer.get("retrieved_context")
    if not isinstance(contexts, list) or len(contexts) != 10:
        raise RuntimeError(f"{qid}: expected ten complete chunks")
    by_rank: dict[int, dict[str, Any]] = {}
    for row in contexts:
        rank = int(row.get("rank"))
        if rank in by_rank:
            raise RuntimeError(f"{qid}: duplicate context rank {rank}")
        if not str(row.get("text") or "").strip():
            raise RuntimeError(f"{qid}: empty context rank {rank}")
        by_rank[rank] = row
    if set(by_rank) != set(range(1, 11)):
        raise RuntimeError(f"{qid}: context ranks must be 1 through 10")
    citations = {int(value) for value in CITATION_RE.findall(str(answer["answer"]))}
    if citations - set(by_rank):
        raise RuntimeError(f"{qid}: answer cites a missing final chunk")
    return [
        {"citation_id": f"C{rank}", "text": str(by_rank[rank]["text"])}
        for rank in range(1, 11)
    ]


def ordered_answers(
    path: Path,
    expected_ids: list[str],
    system: str,
) -> list[dict[str, Any]]:
    rows = read_jsonl(path)
    by_id: dict[str, dict[str, Any]] = {}
    for row in rows:
        qid = str(row.get("question_id") or "")
        if qid in by_id:
            raise RuntimeError(f"{system}: duplicate question {qid}")
        by_id[qid] = row
    missing = sorted(set(expected_ids) - set(by_id))
    extra = sorted(set(by_id) - set(expected_ids))
    if missing or extra:
        raise RuntimeError(f"{system}: missing={missing}, extra={extra}")
    return [by_id[qid] for qid in expected_ids]


def load_items() -> tuple[list[dict[str, Any]], dict[str, str]]:
    questions = read_csv(QUESTIONS)
    qids = [str(row.get("question_id") or "").strip() for row in questions]
    if len(qids) != 40 or len(set(qids)) != 40 or any(not qid for qid in qids):
        raise RuntimeError("Frozen Test40 question membership is invalid")
    question_text = {str(row["question_id"]): row["question_text"] for row in questions}

    items: list[dict[str, Any]] = []
    context_hashes: dict[str, dict[str, str]] = {}
    for system, path in SYSTEMS.items():
        answers = ordered_answers(path, qids, system)
        for answer in answers:
            qid = str(answer["question_id"])
            context = complete_context(answer)
            context_hashes.setdefault(qid, {})[system] = payload_sha256(context)
            items.append(
                {
                    "item_id": f"{system}::{qid}",
                    "question_id": qid,
                    "system": system,
                    "payload": {
                        "question": question_text[qid],
                        "answer_with_citations": answer["answer"],
                        "complete_original_final_context": context,
                    },
                }
            )
    if len(items) != 120:
        raise RuntimeError("Expected three systems by 40 questions")
    for qid, values in context_hashes.items():
        if len(set(values.values())) != 1:
            raise RuntimeError(f"{qid}: RAG systems do not share identical context")
    return items, question_text


def validate_result(
    result: dict[str, Any],
    item_id: str,
    valid_citations: set[str],
) -> None:
    cited = result.get("cited_claims")
    uncited = result.get("uncited_source_dependent_claims")
    if not isinstance(cited, list) or not isinstance(uncited, list):
        raise RuntimeError(f"{item_id}: invalid claim lists")
    claim_ids: list[str] = []
    for row in cited:
        if not isinstance(row, dict) or row.get("support") not in VALID:
            raise RuntimeError(f"{item_id}: invalid cited claim")
        citation_ids = row.get("citation_ids")
        if (
            not str(row.get("claim_id") or "").strip()
            or not str(row.get("claim") or "").strip()
            or not isinstance(citation_ids, list)
            or not citation_ids
            or any(value not in valid_citations for value in citation_ids)
        ):
            raise RuntimeError(f"{item_id}: invalid cited claim schema")
        claim_ids.append(str(row["claim_id"]))
    for row in uncited:
        if (
            not isinstance(row, dict)
            or row.get("support_in_supplied_context") not in VALID
            or not str(row.get("claim_id") or "").strip()
            or not str(row.get("claim") or "").strip()
        ):
            raise RuntimeError(f"{item_id}: invalid uncited claim schema")
        claim_ids.append(str(row["claim_id"]))
    if len(claim_ids) != len(set(claim_ids)):
        raise RuntimeError(f"{item_id}: duplicate claim IDs")


def call_json(
    system_prompt: str,
    payload: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, Any], str]:
    request = request_payload(system_prompt, payload)
    started = time.perf_counter()
    response = source_common.openai_client().chat.completions.create(**request)
    latency = time.perf_counter() - started
    metadata = source_common.openai_metadata(response, latency)
    value = json.loads(response.choices[0].message.content or "{}")
    if not isinstance(value, dict):
        raise RuntimeError("Judge response is not a JSON object")
    return value, metadata, payload_sha256(request)


def run_resumable(
    items: list[dict[str, Any]],
    system_prompt: str,
    workers: int,
    resume: bool,
) -> list[dict[str, Any]]:
    output = RESULTS / "judge_results.jsonl"
    order = [str(item["item_id"]) for item in items]
    scheduled = {str(item["item_id"]): item for item in items}
    existing: dict[str, dict[str, Any]] = {}
    if resume and output.exists():
        for row in read_jsonl(output):
            key = str(row["item_id"])
            if key in existing or key not in scheduled:
                raise RuntimeError(f"Invalid stored result key: {key}")
            expected = payload_sha256(
                request_payload(system_prompt, scheduled[key]["payload"])
            )
            if row.get("execution_sha256") != expected:
                raise RuntimeError(f"Resume request hash mismatch for {key}")
            existing[key] = row
    elif output.exists():
        raise RuntimeError("Results exist; use --resume to avoid duplicate calls")

    pending = [item for item in items if str(item["item_id"]) not in existing]

    def worker(item: dict[str, Any]) -> dict[str, Any]:
        result, metadata, request_hash = call_json(system_prompt, item["payload"])
        validate_result(result, str(item["item_id"]), {f"C{i}" for i in range(1, 11)})
        return {
            "item_id": item["item_id"],
            "question_id": item["question_id"],
            "system": item["system"],
            "execution_sha256": request_hash,
            "judge_result": result,
            "metadata": metadata,
        }

    failures: list[tuple[str, Exception]] = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(worker, item): item for item in pending}
        for future in as_completed(futures):
            item = futures[future]
            key = str(item["item_id"])
            try:
                row = future.result()
            except Exception as exc:
                failures.append((key, exc))
                print(f"[L1.5 error] {key}: {exc}", flush=True)
                continue
            existing[key] = row
            write_jsonl(output, [existing[k] for k in order if k in existing])
            print(f"[L1.5] completed={len(existing)}/{len(items)} {key}", flush=True)
    if failures:
        details = "; ".join(f"{key}: {exc}" for key, exc in failures)
        raise RuntimeError(f"{len(failures)} calls failed; resume is safe. {details}")
    if set(existing) != set(order):
        raise RuntimeError("L1.5 output is incomplete")
    return [existing[key] for key in order]


def summarize(rows: list[dict[str, Any]]) -> None:
    per_question: list[dict[str, Any]] = []
    for row in rows:
        result = row["judge_result"]
        cited = result["cited_claims"]
        uncited = result["uncited_source_dependent_claims"]
        labels = [str(value["support"]) for value in cited]
        supported = sum(label in PASS for label in labels)
        per_question.append(
            {
                "system": row["system"],
                "question_id": row["question_id"],
                "citation_support_applicable": bool(cited),
                "cited_claim_count": len(cited),
                "citation_supported_claim_count": supported,
                "citation_unsupported_claim_count": sum(
                    label == "not_supported" for label in labels
                ),
                "citation_contradicted_claim_count": sum(
                    label == "contradicted" for label in labels
                ),
                "claim_supported_by_any_citation_rate": (
                    supported / len(labels) if labels else ""
                ),
                "uncited_source_dependent_claim_count": len(uncited),
            }
        )

    summaries: list[dict[str, Any]] = []
    for system in SYSTEMS:
        values = [row for row in per_question if row["system"] == system]
        cited_total = sum(int(row["cited_claim_count"]) for row in values)
        supported_total = sum(
            int(row["citation_supported_claim_count"]) for row in values
        )
        rates = [
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
                "mean_question_level_support_rate": mean(rates) if rates else "",
                "unsupported_claim_count": sum(
                    int(row["citation_unsupported_claim_count"]) for row in values
                ),
                "contradicted_claim_count": sum(
                    int(row["citation_contradicted_claim_count"]) for row in values
                ),
                "uncited_source_dependent_claim_count": sum(
                    int(row["uncited_source_dependent_claim_count"]) for row in values
                ),
            }
        )
    write_csv(RESULTS / "per_question.csv", per_question)
    write_csv(RESULTS / "summary.csv", summaries)
    write_json(
        RESULTS / "run_manifest.json",
        {
            "protocol_id": "test40_multibase_l15_v1",
            "status": "complete",
            "question_count": 40,
            "systems": list(SYSTEMS),
            "model": source_common.OPENAI_MODEL,
            "required_snapshot": source_common.OPENAI_SNAPSHOT,
            "reasoning_effort": "low",
            "temperature": "provider_default_not_sent",
            "prompt_sha256": sha256(PROMPT),
            "answer_inputs": {
                system: {"path": str(path.relative_to(ROOT)), "sha256": sha256(path)}
                for system, path in SYSTEMS.items()
            },
            "api_calls": len(rows),
            "total_tokens": sum(int(row["metadata"]["total_tokens"]) for row in rows),
            "estimated_cost_usd": sum(
                float(row["metadata"]["estimated_cost_usd"]) for row in rows
            ),
            "latency_seconds_sum": sum(
                float(row["metadata"]["latency_seconds"]) for row in rows
            ),
            "resume_hash_validated": True,
        },
    )


def preflight(items: list[dict[str, Any]], system_prompt: str) -> None:
    if RESULTS.exists() and any(RESULTS.rglob("*")):
        raise RuntimeError("Paid result directory is not empty before preflight")
    payload_rows = [
        {
            "item_id": item["item_id"],
            "question_id": item["question_id"],
            "system": item["system"],
            "model_payload": item["payload"],
            "execution_sha256": payload_sha256(
                request_payload(system_prompt, item["payload"])
            ),
        }
        for item in items
    ]
    write_jsonl(PREFLIGHT_PAYLOADS, payload_rows)
    manifest = {
        "freeze_id": "test40_multibase_l15_v1_prerun_2026-08-07",
        "status": "pre_run_no_paid_calls",
        "protocol_id": "test40_multibase_l15_v1",
        "question_count": 40,
        "systems": list(SYSTEMS),
        "planned_paid_calls": 120,
        "judge_model": source_common.OPENAI_MODEL,
        "required_snapshot": source_common.OPENAI_SNAPSHOT,
        "frozen_inputs": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in [QUESTIONS, PROMPT, SOURCE_PROTOCOL, *SYSTEMS.values()]
        },
        "payload_file": {
            "path": str(PREFLIGHT_PAYLOADS.relative_to(ROOT)),
            "sha256": sha256(PREFLIGHT_PAYLOADS),
        },
        "source_answers_regenerated": False,
        "source_test_results_used_to_change_prompt_or_metric": False,
    }
    write_json(PRE_RUN_MANIFEST, manifest)
    write_json(
        PREFLIGHT_REPORT,
        {
            "status": "PASS",
            "paid_api_calls_made": 0,
            "payload_count": len(items),
            "identical_context_within_question_across_models": True,
            "source_answers_regenerated": False,
            "prompt_sha256": sha256(PROMPT),
        },
    )
    print("DRY RUN PASS: 120 frozen L1.5 payloads built; no API calls.")


def validate_complete(items: list[dict[str, Any]], system_prompt: str) -> None:
    rows = read_jsonl(RESULTS / "judge_results.jsonl")
    expected = {str(item["item_id"]): item for item in items}
    actual = {str(row["item_id"]): row for row in rows}
    if len(rows) != 120 or set(actual) != set(expected):
        raise RuntimeError("Expected 120 unique completed judgments")
    for key, row in actual.items():
        request_hash = payload_sha256(
            request_payload(system_prompt, expected[key]["payload"])
        )
        if row.get("execution_sha256") != request_hash:
            raise RuntimeError(f"Execution hash mismatch for {key}")
        validate_result(row["judge_result"], key, {f"C{i}" for i in range(1, 11)})
        if row["metadata"].get("response_model") != source_common.OPENAI_SNAPSHOT:
            raise RuntimeError(f"Unexpected model snapshot for {key}")
    if not (RESULTS / "summary.csv").exists():
        raise RuntimeError("Missing summary.csv")
    print("VALIDATION PASS: 120 judgments and request hashes are complete.")


def main() -> None:
    parser = argparse.ArgumentParser()
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--dry-run", action="store_true")
    modes.add_argument("--run", action="store_true")
    modes.add_argument("--validate", action="store_true")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()

    if args.workers < 1:
        raise RuntimeError("workers must be at least one")
    items, _ = load_items()
    system_prompt = PROMPT.read_text(encoding="utf-8")
    if args.dry_run:
        preflight(items, system_prompt)
        return
    if args.validate:
        validate_complete(items, system_prompt)
        return
    if not PRE_RUN_MANIFEST.exists() or not PREFLIGHT_REPORT.exists():
        raise RuntimeError("Run --dry-run before paid execution")
    rows = run_resumable(items, system_prompt, args.workers, args.resume)
    summarize(rows)
    print("L1.5 COMPLETE")


if __name__ == "__main__":
    main()

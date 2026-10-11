from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import sys
import time
from collections import defaultdict
from pathlib import Path
from statistics import mean
from typing import Any

from dotenv import load_dotenv
from openai import OpenAI

PROJECT_ROOT = Path(__file__).resolve().parents[3]

from retrieval_metrics import eval_context
import runtime_helpers as runtime_base

for module_path, module_name in (
    (Path(eval_context.__code__.co_filename), "retrieval_metrics"),
    (Path(runtime_base.__file__), "runtime_helpers"),
):
    if module_path.resolve().parent != Path(__file__).resolve().parent:
        raise RuntimeError(
            f"Resolved {module_name} outside Frozen V3 scripts"
        )

group_gold = runtime_base.group_gold
read_csv = runtime_base.read_csv
read_jsonl = runtime_base.read_jsonl


def project_path(value: str | Path) -> Path:
    path = Path(value)
    return path if path.is_absolute() else PROJECT_ROOT / path


def project_relative(path: Path) -> str:
    return str(path.resolve().relative_to(PROJECT_ROOT))


DEFAULT_SPECS = [
    {
        "config_name": "bge_llm_gpt51_pool30_bge15_llm5_fullchunk",
        "candidate_scores": "benchmark/frozen_v3/results/dev13_retrieval_budget_gpt51_2026-07-26/local_hybrid_bge/bge_candidate_scores.jsonl",
        "source_config": "bge_base_top5_pool30_nodoccap",
        "pool_k": 30,
        "bge_shortlist_k": 15,
        "final_top_k": 5,
    },
    {
        "config_name": "bge_llm_gpt51_pool60_bge30_llm10_fullchunk",
        "candidate_scores": "benchmark/frozen_v3/results/dev13_retrieval_budget_gpt51_2026-07-26/local_hybrid_bge/bge_candidate_scores.jsonl",
        "source_config": "bge_base_top10_pool60_nodoccap",
        "pool_k": 60,
        "bge_shortlist_k": 30,
        "final_top_k": 10,
    },
    {
        "config_name": "bge_llm_gpt51_pool120_bge60_llm20_fullchunk",
        "candidate_scores": "benchmark/frozen_v3/results/dev13_retrieval_budget_gpt51_2026-07-26/local_hybrid_bge/bge_candidate_scores.jsonl",
        "source_config": "bge_base_top20_pool120_nodoccap",
        "pool_k": 120,
        "bge_shortlist_k": 60,
        "final_top_k": 20,
    },
]


def norm(value: Any) -> str:
    return "" if value is None else str(value)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_jsonl(path: str | Path, rows: list[dict[str, Any]]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_csv(path: str | Path, rows: list[dict[str, Any]]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fields: list[str] = []
    seen = set()
    for row in rows:
        for key in row:
            if key not in seen:
                fields.append(key)
                seen.add(key)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def compact_text(text: str, max_chars: int) -> str:
    text = re.sub(r"\s+", " ", norm(text)).strip()
    if max_chars <= 0 or len(text) <= max_chars:
        return text
    return text[:max_chars].rsplit(" ", 1)[0] + "..."


def parse_selector_json(content: str) -> dict[str, Any]:
    content = norm(content).strip()
    try:
        data = json.loads(content, strict=False)
    except json.JSONDecodeError as first_error:
        match = re.search(r"\{.*\}", content, re.DOTALL)
        if not match:
            raise ValueError("Selector returned invalid JSON") from first_error
        try:
            data = json.loads(match.group(0), strict=False)
        except json.JSONDecodeError as second_error:
            raise ValueError("Selector returned invalid JSON") from second_error
    if not isinstance(data, dict):
        raise ValueError("Selector response must be a JSON object")
    if not isinstance(data.get("selected_ids"), list):
        raise ValueError("Selector response must contain selected_ids list")
    return data


def id_to_int(value: Any) -> int | None:
    if isinstance(value, int) and not isinstance(value, bool):
        return value
    text = norm(value).strip()
    return int(text) if re.fullmatch(r"\d+", text) else None


def load_candidates(path: Path, source_config: str) -> dict[str, list[dict[str, Any]]]:
    by_qid: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in read_jsonl(path):
        if norm(row.get("config_name")) != source_config:
            continue
        qid = norm(row.get("question_id"))
        hit = dict(row)
        hit["source"] = norm(hit.get("source") or hit.get("doc_id"))
        hit["chunk"] = norm(hit.get("chunk") or hit.get("chunk_id"))
        hit["citation_acs"] = hit.get("citation") or hit.get("citation_acs") or hit.get("source")
        try:
            hit["rank"] = int(hit.get("rank") or 999999)
        except (TypeError, ValueError):
            hit["rank"] = 999999
        by_qid[qid].append(hit)
    for rows in by_qid.values():
        rows.sort(key=lambda item: int(item.get("rank") or 999999))
    return by_qid


def normalize_context_hit(hit: dict[str, Any], rank: int) -> dict[str, Any]:
    return {
        "rank": rank,
        "doc_id": norm(hit.get("doc_id") or hit.get("source")),
        "chunk_id": norm(hit.get("chunk_id") or hit.get("chunk")),
        "section": norm(hit.get("section")),
        "text": norm(hit.get("text")),
        "score": hit.get("score", hit.get("rerank_score", "")),
        "retrieval_source": norm(hit.get("retrieval_source")),
        "dense_rank": hit.get("dense_rank"),
        "bm25_rank": hit.get("bm25_rank"),
        "bm25_score": hit.get("bm25_score", ""),
        "rerank_score": hit.get("rerank_score", ""),
        "citation": hit.get("citation") or hit.get("citation_acs") or hit.get("source", ""),
        "cross_encoder_score": hit.get("cross_encoder_score"),
        "cross_encoder_score_norm": hit.get("cross_encoder_score_norm"),
        "selector_score": hit.get("selector_score"),
        "original_rank": hit.get("original_rank"),
        "llm_rerank_rank": hit.get("llm_rerank_rank"),
        "llm_relevance_score": hit.get("llm_relevance_score"),
        "llm_reason": hit.get("llm_reason", ""),
        "llm_evidence_type": hit.get("llm_evidence_type", ""),
        "llm_covered_evidence": hit.get("llm_covered_evidence", []),
    }


def prefix_metric_row(prefix: str, row: dict[str, Any]) -> dict[str, Any]:
    fields = {
        "required_gold_recall@5",
        "required_gold_recall@10",
        "required_gold_recall@20",
        "required_gold_recall@full_context",
        "gold_doc_recall@10",
        "gold_doc_recall@20",
        "gold_doc_recall@full_context",
        "MRR_required_gold",
        "required_gold_retrieved@10",
        "required_gold_retrieved@20",
        "required_gold_retrieved@full_context",
        "negative_gold_recall@5",
        "negative_gold_recall@10",
        "negative_gold_recall@20",
        "negative_gold_recall@full_context",
    }
    return {f"{prefix}_{key}": value for key, value in row.items() if key in fields}


def llm_select_hits(
    *,
    client: OpenAI,
    model: str,
    question_text: str,
    question: dict[str, Any],
    selector_input: str,
    candidates: list[dict[str, Any]],
    top_k: int,
    max_chars: int,
    system_prompt: str,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    blocks = []
    id_to_hit: dict[int, dict[str, Any]] = {}
    for index, hit in enumerate(candidates, start=1):
        id_to_hit[index] = hit
        citation = norm(hit.get("citation") or hit.get("citation_acs") or hit.get("source") or "unknown")
        section = norm(hit.get("section") or "unknown")
        blocks.append(
            f"ID: {index}\n"
            f"Section: {section}\n"
            f"Source: {citation}\n"
            f"Chunk: {compact_text(hit.get('text', ''), max_chars)}"
        )
    user_payload = {
        "question": question_text,
        "instruction": (
            f"Select up to {top_k} candidate IDs in descending usefulness. "
            "Do not invent IDs. Return JSON: "
            '{"selected_ids":[1,2], "scores":{"1":9}, "reasons":{"1":"short reason"}}'
        ),
        "candidates": "\n\n".join(blocks),
    }
    if selector_input != "visible_question_only":
        raise RuntimeError(
            "Frozen V3 permits only visible_question_only selector input"
        )
    response = client.chat.completions.create(
        model=model,
        response_format={"type": "json_object"},
        temperature=0,
        timeout=300,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": json.dumps(user_payload, ensure_ascii=False)},
        ],
    )
    raw_content = response.choices[0].message.content or "{}"
    data = parse_selector_json(raw_content)
    selected_ids: list[int] = []
    if isinstance(data.get("selected_ids"), list):
        for value in data["selected_ids"]:
            candidate_id = id_to_int(value)
            if candidate_id in id_to_hit and candidate_id not in selected_ids:
                selected_ids.append(candidate_id)
            if len(selected_ids) >= top_k:
                break
    scores = data.get("scores", {}) if isinstance(data.get("scores"), dict) else {}
    reasons = data.get("reasons", {}) if isinstance(data.get("reasons"), dict) else {}
    selected = []
    selected_identity = set()
    for rank, candidate_id in enumerate(selected_ids, start=1):
        hit = id_to_hit[candidate_id]
        try:
            score = float(scores.get(str(candidate_id), scores.get(candidate_id, 0)))
        except (TypeError, ValueError):
            score = 0.0
        hit["llm_relevance_score"] = score
        hit["llm_reason"] = norm(reasons.get(str(candidate_id), reasons.get(candidate_id, "")))
        hit["llm_rerank_rank"] = rank
        selected.append(hit)
        selected_identity.add(id(hit))
    for hit in candidates:
        if len(selected) >= top_k:
            break
        if id(hit) not in selected_identity:
            hit["llm_rerank_rank"] = len(selected) + 1
            hit["llm_relevance_score"] = hit.get("llm_relevance_score", 0)
            hit["llm_reason"] = "fallback after selector returned fewer than top_k IDs"
            selected.append(hit)
            selected_identity.add(id(hit))
    usage = getattr(response, "usage", None)
    call_record = {
        "model_requested": model,
        "model_returned": norm(getattr(response, "model", "")),
        "response_id": norm(getattr(response, "id", "")),
        "system_fingerprint": norm(getattr(response, "system_fingerprint", "")),
        "temperature": 0,
        "system_prompt": system_prompt,
        "user_payload": user_payload,
        "raw_response": raw_content,
        "parsed_response": data,
        "prompt_tokens": int(getattr(usage, "prompt_tokens", 0) or 0),
        "completion_tokens": int(getattr(usage, "completion_tokens", 0) or 0),
        "total_tokens": int(getattr(usage, "total_tokens", 0) or 0),
    }
    return selected, call_record


def summarize(rows: list[dict[str, Any]], runtime_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_runtime = {row["config_name"]: row for row in runtime_rows}
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[str(row["config_name"])].append(row)
    summaries = []
    required_metric_fields = [
        "final_required_gold_recall@10",
        "final_required_gold_recall@20",
        "final_required_gold_recall@full_context",
        "final_gold_doc_recall@10",
        "final_gold_doc_recall@20",
        "final_MRR_required_gold",
        "bge_shortlist_required_gold_recall@full_context",
        "bge_pool_required_gold_recall@full_context",
        "bge_pool_MRR_required_gold",
    ]
    negative_metric_fields = [
        "final_negative_gold_recall@5",
        "final_negative_gold_recall@10",
        "final_negative_gold_recall@20",
        "final_negative_gold_recall@full_context",
        "bge_shortlist_negative_gold_recall@full_context",
        "bge_pool_negative_gold_recall@full_context",
    ]
    for config_name, group in sorted(groups.items()):
        first = group[0]
        row: dict[str, Any] = {
            "config_name": config_name,
            "pool_k": first["pool_k"],
            "bge_shortlist_k": first["bge_shortlist_k"],
            "final_top_k": first["final_top_k"],
            "num_questions": len(group),
        }
        required = [item for item in group if int(item.get("required_gold_count", 0) or 0) > 0]
        negative = [item for item in group if int(item.get("negative_gold_count", 0) or 0) > 0]
        for field in required_metric_fields:
            row[f"mean_{field}"] = (
                mean(float(item.get(field, 0) or 0) for item in required) if required else 0.0
            )
        for field in negative_metric_fields:
            row[f"mean_{field}"] = (
                mean(float(item.get(field, 0) or 0) for item in negative)
                if negative
                else 0.0
            )
        row["required_question_count"] = len(required)
        row["negative_question_count"] = len(negative)
        row["hit_any_final_full_context"] = sum(
            1 for item in required if int(item.get("final_required_gold_retrieved@full_context", 0) or 0) > 0
        )
        row["full_hit_final_full_context"] = sum(
            1 for item in required if float(item.get("final_required_gold_recall@full_context", 0) or 0) >= 0.999999
        )
        row.update(by_runtime.get(config_name, {}))
        summaries.append(row)
    return summaries


def output_row(
    qid: str,
    config_name: str,
    spec: dict[str, Any],
    context: list[dict[str, Any]],
    model: str,
    selector_input: str,
    prompt_version: str,
) -> dict[str, Any]:
    return {
        "question_id": qid,
        "system_mode": "rag_end_to_end",
        "answer": "",
        "retrieved_context": context,
        "retrieval_config_name": config_name,
        "retrieval_method": "bge_llm_cascade",
        "retrieval_k": int(spec["pool_k"]),
        "bm25_k": int(spec["pool_k"]),
        "bge_shortlist_k": int(spec["bge_shortlist_k"]),
        "top_k": int(spec["final_top_k"]),
        "context_window": 0,
        "llm_rerank": True,
        "llm_rerank_mode": "short_selector",
        "llm_rerank_model": model,
        "selector_input": selector_input,
        "prompt_version": prompt_version,
    }


def load_specs(path: str) -> list[dict[str, Any]]:
    if not path:
        return DEFAULT_SPECS
    with Path(path).open(encoding="utf-8") as handle:
        data = json.load(handle)
    specs = data.get("specs", data)
    if not isinstance(specs, list):
        raise ValueError("Specs file must contain a list or {'specs': [...]}.")
    return specs


def run(args: argparse.Namespace) -> None:
    load_dotenv(PROJECT_ROOT / ".env", override=False)
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is required for BGE+LLM cascade retrieval-only sweep.")
    questions_path = project_path(args.questions)
    gold_path = project_path(args.gold)
    specs_path = project_path(args.specs)
    questions = read_csv(questions_path)
    question_qids = [
        norm(row.get("question_id")).strip() for row in questions
    ]
    if len(questions) != 13:
        raise RuntimeError(f"Expected 13 Dev questions; found {len(questions)}")
    if any(not qid for qid in question_qids):
        raise RuntimeError("Every question must have a non-empty question_id")
    if len(question_qids) != len(set(question_qids)):
        raise RuntimeError("Duplicate question_id in Dev questions")
    if any(not norm(row.get("question_text")).strip() for row in questions):
        raise RuntimeError("Every question must have non-empty question_text")
    gold_by_qid = group_gold(read_jsonl(gold_path))
    specs = load_specs(str(specs_path))
    config_names = [norm(spec.get("config_name")) for spec in specs]
    if len(specs) != 3 or len(config_names) != len(set(config_names)):
        raise RuntimeError("Expected three uniquely named budget specs")
    for spec in specs:
        pool_k = int(spec["pool_k"])
        shortlist_k = int(spec["bge_shortlist_k"])
        final_top_k = int(spec["final_top_k"])
        if not (0 < final_top_k <= shortlist_k <= pool_k):
            raise RuntimeError(
                f"Invalid budget ordering for {spec['config_name']}"
            )
    out_dir = project_path(args.out)
    if out_dir.exists() and any(out_dir.iterdir()):
        raise RuntimeError(
            f"Refusing to overwrite non-empty result directory: {out_dir}"
        )
    outputs_dir = out_dir / "retrieval_outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    outputs_dir.mkdir(parents=True, exist_ok=True)
    model = args.openai_model or "gpt-5.1"
    client = OpenAI(timeout=300.0, max_retries=1)
    selector_prompt_path = project_path(args.selector_prompt)
    selector_prompt = selector_prompt_path.read_text(encoding="utf-8")

    manifest = {
        "run_id": out_dir.name,
        "questions": project_relative(questions_path),
        "questions_sha256": sha256(questions_path),
        "gold": project_relative(gold_path),
        "gold_sha256": sha256(gold_path),
        "specs_path": project_relative(specs_path),
        "specs_sha256": sha256(specs_path),
        "policy": "Hybrid poolK -> BGE shortlistK -> LLM final topK",
        "llm_model": model,
        "temperature": 0,
        "selector_max_chars": int(args.selector_max_chars),
        "selector_input": args.selector_input,
        "selector_prompt": str(
            selector_prompt_path.relative_to(PROJECT_ROOT)
        ),
        "selector_prompt_sha256": sha256(selector_prompt_path),
        "specs": specs,
    }
    (out_dir / "experiment_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    all_metrics: list[dict[str, Any]] = []
    runtime_rows: list[dict[str, Any]] = []
    llm_candidate_rows: list[dict[str, Any]] = []
    selector_call_rows: list[dict[str, Any]] = []
    config_manifest: list[dict[str, Any]] = []

    for spec in specs:
        config_name = str(spec["config_name"])
        source_config = str(spec["source_config"])
        pool_k = int(spec["pool_k"])
        shortlist_k = int(spec["bge_shortlist_k"])
        final_top_k = int(spec["final_top_k"])
        print(f"[config] {config_name}", flush=True)
        candidate_path = project_path(str(spec["candidate_scores"]))
        by_qid = load_candidates(candidate_path, source_config)
        output_rows = []
        llm_seconds = 0.0
        config_start = time.perf_counter()
        for index, question in enumerate(questions, start=1):
            qid = norm(question.get("question_id"))
            qtext = norm(question.get("question_text"))
            bge_pool = by_qid.get(qid, [])[:pool_k]
            if len(bge_pool) < min(pool_k, shortlist_k):
                raise RuntimeError(f"Insufficient candidates for {config_name} {qid}: {len(bge_pool)}")
            identities = [
                (
                    norm(hit.get("doc_id") or hit.get("source")),
                    norm(hit.get("chunk_id") or hit.get("chunk")),
                )
                for hit in bge_pool
            ]
            if any(not doc_id or not chunk_id for doc_id, chunk_id in identities):
                raise RuntimeError(
                    f"Incomplete candidate identity for {config_name} {qid}"
                )
            if len(identities) != len(set(identities)):
                raise RuntimeError(
                    f"Duplicate candidate identity for {config_name} {qid}"
                )
            bge_shortlist = [dict(hit) for hit in bge_pool[:shortlist_k]]
            print(f"  [llm {index}/{len(questions)}] {qid} shortlist={shortlist_k}", flush=True)
            start = time.perf_counter()
            selected, call_record = llm_select_hits(
                client=client,
                model=model,
                question_text=qtext,
                question=question,
                selector_input=args.selector_input,
                candidates=bge_shortlist,
                top_k=final_top_k,
                max_chars=int(args.selector_max_chars),
                system_prompt=selector_prompt,
            )
            llm_seconds += time.perf_counter() - start
            selector_call_rows.append(
                {
                    "config_name": config_name,
                    "question_id": qid,
                    "pool_k": pool_k,
                    "bge_shortlist_k": shortlist_k,
                    "final_top_k": final_top_k,
                    **call_record,
                }
            )
            selected_keys = {
                (norm(hit.get("doc_id") or hit.get("source")), norm(hit.get("chunk_id") or hit.get("chunk"))): hit
                for hit in selected
            }
            for rank, hit in enumerate(bge_shortlist, start=1):
                key = (norm(hit.get("doc_id") or hit.get("source")), norm(hit.get("chunk_id") or hit.get("chunk")))
                selected_hit = selected_keys.get(key, {})
                llm_candidate_rows.append(
                    {
                        "config_name": config_name,
                        "question_id": qid,
                        "bge_shortlist_rank": rank,
                        "doc_id": key[0],
                        "chunk_id": key[1],
                        "cross_encoder_score_norm": hit.get("cross_encoder_score_norm"),
                        "llm_relevance_score": selected_hit.get("llm_relevance_score", ""),
                        "llm_rerank_rank": selected_hit.get("llm_rerank_rank", ""),
                        "selected_by_llm": key in selected_keys,
                    }
                )
            final_context = [normalize_context_hit(hit, rank) for rank, hit in enumerate(selected, start=1)]
            shortlist_context = [normalize_context_hit(hit, rank) for rank, hit in enumerate(bge_shortlist, start=1)]
            pool_context = [normalize_context_hit(hit, rank) for rank, hit in enumerate(bge_pool, start=1)]
            output_rows.append(
                output_row(
                    qid,
                    config_name,
                    spec,
                    final_context,
                    model,
                    args.selector_input,
                    project_relative(selector_prompt_path),
                )
            )
            final_metrics = eval_context(qid, gold_by_qid.get(qid, []), final_context, config_name, "bge_llm_cascade", final_top_k, pool_k, 0)
            shortlist_metrics = eval_context(qid, gold_by_qid.get(qid, []), shortlist_context, config_name, "bge_shortlist", shortlist_k, pool_k, 0)
            pool_metrics = eval_context(qid, gold_by_qid.get(qid, []), pool_context, config_name, "bge_pool", pool_k, pool_k, 0)
            all_metrics.append(
                {
                    "config_name": config_name,
                    "question_id": qid,
                    "pool_k": pool_k,
                    "bge_shortlist_k": shortlist_k,
                    "final_top_k": final_top_k,
                    "required_gold_count": final_metrics.get("required_gold_count", 0),
                    "negative_gold_count": final_metrics.get("negative_gold_count", 0),
                    **prefix_metric_row("final", final_metrics),
                    **prefix_metric_row("bge_shortlist", shortlist_metrics),
                    **prefix_metric_row("bge_pool", pool_metrics),
                }
            )
        write_jsonl(outputs_dir / f"rag_outputs_{config_name}.jsonl", output_rows)
        runtime_rows.append(
            {
                "config_name": config_name,
                "llm_seconds_total": llm_seconds,
                "llm_seconds_per_question": llm_seconds / max(1, len(questions)),
                "config_wall_seconds": time.perf_counter() - config_start,
            }
        )
        config_manifest.append(
            {
                "config_name": config_name,
                "source_config": source_config,
                "candidate_scores": spec["candidate_scores"],
                "pool_k": pool_k,
                "bge_shortlist_k": shortlist_k,
                "final_top_k": final_top_k,
                "selector_input": args.selector_input,
                "rag_outputs_path": project_relative(
                    outputs_dir / f"rag_outputs_{config_name}.jsonl"
                ),
            }
        )

    summary_rows = summarize(all_metrics, runtime_rows)
    write_csv(out_dir / "retrieval_config_manifest.csv", config_manifest)
    write_csv(out_dir / "per_question_retrieval_metrics.csv", all_metrics)
    write_csv(out_dir / "summary_retrieval_metrics.csv", summary_rows)
    write_jsonl(out_dir / "llm_candidate_scores.jsonl", llm_candidate_rows)
    write_jsonl(out_dir / "selector_calls.jsonl", selector_call_rows)
    token_rows = []
    for spec in specs:
        config_name = str(spec["config_name"])
        calls = [row for row in selector_call_rows if row["config_name"] == config_name]
        token_rows.append(
            {
                "config_name": config_name,
                "stage": "llm_selector",
                "api_calls": len(calls),
                "prompt_tokens": sum(int(row["prompt_tokens"]) for row in calls),
                "completion_tokens": sum(int(row["completion_tokens"]) for row in calls),
                "total_tokens": sum(int(row["total_tokens"]) for row in calls),
                "mean_total_tokens_per_question": (
                    sum(int(row["total_tokens"]) for row in calls) / len(calls) if calls else 0
                ),
            }
        )
    write_csv(out_dir / "token_cost_summary.csv", token_rows)
    lines = [
        "# Frozen V3 Dev13 BGE-LLM GPT-5.1 Retrieval Budget Sweep",
        "",
        "Policy: Hybrid poolK -> BGE shortlistK -> LLM final topK.",
        "The selector receives the visible question and full candidate chunks only.",
        "",
        "| config | final recall | shortlist recall | pool recall | final MRR | hit-any final | LLM sec/q |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in summary_rows:
        lines.append(
            f"| `{row['config_name']}` | "
            f"{float(row['mean_final_required_gold_recall@full_context']):.3f} | "
            f"{float(row['mean_bge_shortlist_required_gold_recall@full_context']):.3f} | "
            f"{float(row['mean_bge_pool_required_gold_recall@full_context']):.3f} | "
            f"{float(row['mean_final_MRR_required_gold']):.3f} | "
            f"{row['hit_any_final_full_context']}/{row['required_question_count']} | "
            f"{float(row.get('llm_seconds_per_question') or 0):.1f} |"
        )
    (out_dir / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote BGE+LLM cascade retrieval-only sweep to {out_dir}", flush=True)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run dev13 BGE+LLM cascade retrieval-only sweep.")
    parser.add_argument(
        "--questions",
        default="benchmark/frozen_v3/input/questions_dev13.csv",
    )
    parser.add_argument(
        "--gold",
        default="benchmark/frozen_v3/gold/chunk_based_gold.jsonl",
    )
    parser.add_argument(
        "--out",
        required=True,
        help="New output directory; existing non-empty directories are refused.",
    )
    parser.add_argument(
        "--specs",
        default=(
            "benchmark/frozen_v3/methods/"
            "dev13_retrieval_budget_gpt51_specs.json"
        ),
    )
    parser.add_argument(
        "--selector-max-chars",
        type=int,
        default=0,
        help="Maximum characters per candidate chunk; 0 keeps the full chunk.",
    )
    parser.add_argument(
        "--selector-input",
        choices=("visible_question_only",),
        default="visible_question_only",
        help="Only the visible question may be exposed to the LLM selector.",
    )
    parser.add_argument(
        "--selector-prompt",
        default=(
            "benchmark/frozen_v3/prompts/retrieval/"
            "bge_llm_selector_v3.txt"
        ),
    )
    parser.add_argument("--openai-model", default="gpt-5.1")
    return parser


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    run(build_parser().parse_args())


if __name__ == "__main__":
    main()

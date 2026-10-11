from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

from dotenv import load_dotenv


EXPERIMENT = Path(__file__).resolve().parents[1]
JUDGE = EXPERIMENT.parents[1]
V3 = JUDGE.parent
ROOT = V3.parents[1]
V3_SCRIPTS = V3 / "scripts"
if str(V3_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(V3_SCRIPTS))

import build_freeze_manifest as freeze  # noqa: E402
import run_dev13_soft_tags_v3 as generation  # noqa: E402
import runtime_helpers as base  # noqa: E402


PROTOCOL = EXPERIMENT / "protocol.json"
QUESTIONS = V3 / "input/questions_dev13.csv"
TAG_PROMPT = V3 / "prompts/evaluation/soft_eligibility_tagger_v3.txt"
ANSWER_PROMPT = V3 / "prompts/evaluation/rag_answer_prompt_soft_tags_v3.txt"
FREEZE_MANIFEST = V3 / "freeze_manifest.json"
RUNNER = Path(__file__).resolve()
MODEL = "gpt-5.1"

RETRIEVAL_ROOT = (
    V3 / "results/dev13_retrieval_budget_gpt51_2026-07-26"
)
SELECTOR_LEDGER = (
    RETRIEVAL_ROOT / "bge_llm_gpt51/token_cost_summary.csv"
)
RETRIEVAL_SUMMARY = (
    RETRIEVAL_ROOT / "dev13_retrieval_budget_summary.csv"
)
SYSTEMS = {
    "hybrid": {
        "config_name": "hybrid_top10_pool60_win0",
        "retrieval": (
            RETRIEVAL_ROOT
            / "local_hybrid_bge/retrieval_outputs/"
            "rag_outputs_hybrid_top10_pool60_win0.jsonl"
        ),
    },
    "bge": {
        "config_name": "bge_base_top10_pool60_nodoccap",
        "retrieval": (
            RETRIEVAL_ROOT
            / "local_hybrid_bge/retrieval_outputs/"
            "rag_outputs_bge_base_top10_pool60_nodoccap.jsonl"
        ),
    },
    "bge_llm": {
        "config_name": (
            "bge_llm_gpt51_pool60_bge30_llm10_fullchunk"
        ),
        "retrieval": (
            RETRIEVAL_ROOT
            / "bge_llm_gpt51/retrieval_outputs/"
            "rag_outputs_bge_llm_gpt51_pool60_bge30_llm10_fullchunk.jsonl"
        ),
    },
}


def verify_frozen_v3() -> dict:
    manifest = json.loads(FREEZE_MANIFEST.read_text(encoding="utf-8"))
    errors = freeze.verify(manifest)
    if errors:
        raise RuntimeError(
            "Frozen V3 manifest verification failed:\n"
            + "\n".join(errors)
        )
    if manifest.get("freeze_id") != (
        "pfas_rag_frozen_v3_revision3_2026-07-26"
    ):
        raise RuntimeError("Unexpected Frozen V3 freeze_id")
    return manifest


def validate_retrieval(system: str, path: Path) -> list[dict]:
    questions = base.read_csv(QUESTIONS)
    rows = base.read_jsonl(path)
    question_ids = [row["question_id"] for row in questions]
    by_qid = {row.get("question_id"): row for row in rows}
    if len(rows) != len(questions) or set(by_qid) != set(question_ids):
        raise RuntimeError(
            f"{system}: retrieval membership does not match Dev13"
        )
    for qid in question_ids:
        contexts = by_qid[qid].get("retrieved_context")
        if not isinstance(contexts, list) or len(contexts) != 10:
            raise RuntimeError(
                f"{system}/{qid}: expected exactly ten final chunks"
            )
        identities: list[tuple[str, str]] = []
        for hit in contexts:
            doc_id = str(hit.get("doc_id") or "").strip()
            chunk_id = str(hit.get("chunk_id") or "").strip()
            text = str(hit.get("text") or "").strip()
            if not doc_id or not chunk_id or not text:
                raise RuntimeError(
                    f"{system}/{qid}: incomplete chunk identity or text"
                )
            identities.append((doc_id, chunk_id))
        if len(identities) != len(set(identities)):
            raise RuntimeError(
                f"{system}/{qid}: duplicate chunk in final top10"
            )
    return [by_qid[qid] for qid in question_ids]


def tagger_model_payload(
    question: dict,
    retrieval: dict,
) -> dict:
    return {
        "question": question["question_text"],
        "candidates": [
            {
                "candidate_id": index,
                "source": hit.get("citation") or hit.get("doc_id", ""),
                "section": hit.get("section", ""),
                "text": hit.get("text", ""),
            }
            for index, hit in enumerate(
                retrieval["retrieved_context"],
                start=1,
            )
        ],
    }


def validate_information_boundary(
    questions: list[dict],
    retrieval_rows: list[dict],
) -> None:
    retrieval_by_qid = {
        row["question_id"]: row for row in retrieval_rows
    }
    forbidden_keys = {
        "system",
        "system_name",
        "retrieval_system",
        "retrieval_config_name",
        "gold",
        "gold_evidence",
        "must_include",
        "must_not_claim",
        "task_type",
        "answerability_type",
        "score",
        "rank",
    }
    for question in questions:
        payload = tagger_model_payload(
            question,
            retrieval_by_qid[question["question_id"]],
        )
        candidate_keys = set().union(
            *(set(row) for row in payload["candidates"])
        )
        visible_keys = set(payload) | candidate_keys
        leaked = forbidden_keys & visible_keys
        if leaked:
            raise RuntimeError(
                f"Tagger payload exposes forbidden keys: {sorted(leaked)}"
            )


def annotate_rows(
    rows: list[dict],
    *,
    system: str,
    config_name: str,
    pipeline_id: str,
) -> list[dict]:
    return [
        {
            **row,
            "retrieval_system": system,
            "source_retrieval_config_name": config_name,
            "common_tagger_pipeline_id": pipeline_id,
        }
        for row in rows
    ]


def ordered_items(
    questions: list[dict],
    retrieval_by_system: dict[str, list[dict]],
    systems: list[str],
) -> list[dict]:
    by_system_qid = {
        system: {
            row["question_id"]: row
            for row in retrieval_by_system[system]
        }
        for system in systems
    }
    items: list[dict] = []
    for question_index, question in enumerate(questions):
        offset = question_index % len(systems)
        rotated = systems[offset:] + systems[:offset]
        for system in rotated:
            items.append(
                {
                    "item_id": f"{system}::{question['question_id']}",
                    "system": system,
                    "config_name": SYSTEMS[system]["config_name"],
                    "question": question,
                    "retrieval": by_system_qid[system][
                        question["question_id"]
                    ],
                }
            )
    return items


def selector_usage(system: str) -> dict:
    if system != "bge_llm":
        return {
            "stage": "retrieval_specific_llm_selector",
            "config_name": system,
            "model": "",
            "call_count": 0,
            "prompt_tokens_total": 0,
            "completion_tokens_total": 0,
            "total_tokens": 0,
            "tokens_per_call": 0.0,
            "estimated_usd": 0.0,
            "latency_seconds_sum": 0.0,
            "latency_seconds_mean": 0.0,
            "latency_provenance": "not_applicable",
            "note": "No LLM selector in this retrieval system.",
        }
    rows = base.read_csv(SELECTOR_LEDGER)
    config = SYSTEMS[system]["config_name"]
    matches = [
        row
        for row in rows
        if row.get("config_name") == config
        and row.get("stage") == "llm_selector"
    ]
    if len(matches) != 1:
        raise RuntimeError(
            f"Expected one selector ledger row for {config}"
        )
    source = matches[0]
    prompt_tokens = int(source["prompt_tokens"])
    completion_tokens = int(source["completion_tokens"])
    total_tokens = int(source["total_tokens"])
    calls = int(source["api_calls"])
    summary_rows = base.read_csv(RETRIEVAL_SUMMARY)
    summary = [
        row for row in summary_rows
        if row.get("config_name") == config
    ]
    if len(summary) != 1:
        raise RuntimeError(
            f"Expected one retrieval summary row for {config}"
        )
    latency = float(summary[0]["selector_seconds_total"])
    return {
        "stage": "retrieval_specific_llm_selector",
        "config_name": system,
        "model": MODEL,
        "call_count": calls,
        "prompt_tokens_total": prompt_tokens,
        "completion_tokens_total": completion_tokens,
        "total_tokens": total_tokens,
        "tokens_per_call": total_tokens / calls,
        "estimated_usd": (
            prompt_tokens / 1_000_000 * 1.25
            + completion_tokens / 1_000_000 * 10.0
        ),
        "latency_seconds_sum": latency,
        "latency_seconds_mean": latency / calls,
        "latency_provenance": (
            "Inherited from the Frozen V3 selector execution."
        ),
        "note": (
            "Inherited frozen selector usage; no new selector call in this "
            "generation experiment."
        ),
    }


def local_retrieval_usage(system: str) -> list[dict]:
    rows = base.read_csv(RETRIEVAL_SUMMARY)
    hybrid = next(
        row for row in rows
        if row.get("config_name") == "hybrid_top10_pool60_win0"
    )
    bge = next(
        row for row in rows
        if row.get("config_name")
        == "bge_base_top10_pool60_nodoccap"
    )
    stages = [
        {
            "stage": "hybrid_candidate_retrieval",
            "config_name": system,
            "model": "",
            "call_count": 13,
            "prompt_tokens_total": 0,
            "completion_tokens_total": 0,
            "total_tokens": 0,
            "tokens_per_call": 0.0,
            "estimated_usd": 0.0,
            "latency_seconds_sum": float(
                hybrid["retrieval_seconds_total"]
            ),
            "latency_seconds_mean": (
                float(hybrid["retrieval_seconds_total"]) / 13
            ),
            "latency_provenance": (
                "Inherited from the matched Frozen V3 retrieval run."
            ),
            "note": "Dense and lexical candidate retrieval.",
        }
    ]
    if system in {"bge", "bge_llm"}:
        stages.append(
            {
                "stage": "bge_cross_encoder_rerank",
                "config_name": system,
                "model": "BAAI/bge-reranker-base",
                "call_count": 13,
                "prompt_tokens_total": 0,
                "completion_tokens_total": 0,
                "total_tokens": 0,
                "tokens_per_call": 0.0,
                "estimated_usd": 0.0,
                "latency_seconds_sum": float(
                    bge["bge_seconds_total"]
                ),
                "latency_seconds_mean": (
                    float(bge["bge_seconds_total"]) / 13
                ),
                "latency_provenance": (
                    "Inherited from the matched Frozen V3 BGE run."
                ),
                "note": "Local cross-encoder reranking.",
            }
        )
    return stages


def token_ledger(
    system: str,
    tag_rows: list[dict],
    answer_rows: list[dict],
) -> list[dict]:
    tag = base.token_row(
        "common_soft_tagger",
        system,
        tag_rows,
        "tag",
        "Common downstream layer; visible question plus final top10 only.",
    )
    answer = base.token_row(
        "common_answer_generation",
        system,
        answer_rows,
        "answer",
        "Common answer model and prompt with full chunks plus advisory tags.",
    )
    for row in (tag, answer):
        prompt_tokens = int(row["prompt_tokens_total"])
        completion_tokens = int(row["completion_tokens_total"])
        row["estimated_usd"] = (
            prompt_tokens / 1_000_000 * 1.25
            + completion_tokens / 1_000_000 * 10.0
        )
    tag_latencies = [
        float(row.get("tag_latency_seconds", 0.0))
        for row in tag_rows
    ]
    answer_latencies = [
        float(row.get("answer_latency_seconds", 0.0))
        for row in answer_rows
    ]
    for row, latencies in (
        (tag, tag_latencies),
        (answer, answer_latencies),
    ):
        row["latency_seconds_sum"] = sum(latencies)
        row["latency_seconds_mean"] = (
            sum(latencies) / len(latencies) if latencies else 0.0
        )
        row["latency_provenance"] = (
            "Measured around each API request in this run."
        )
    return [
        *local_retrieval_usage(system),
        selector_usage(system),
        tag,
        answer,
    ]


def run_common_tagger(
    items: list[dict],
    root_out: Path,
    workers: int,
    resume: bool,
) -> tuple[list[dict], float]:
    system_prompt = TAG_PROMPT.read_text(encoding="utf-8")
    output = root_out / "common_tagger/tag_results.jsonl"

    def request_for(item: dict) -> tuple[dict, dict]:
        payload = tagger_model_payload(
            item["question"],
            item["retrieval"],
        )
        request = {
            "model": MODEL,
            "response_format": {"type": "json_object"},
            "temperature": 0,
            "messages": [
                {"role": "system", "content": system_prompt},
                {
                    "role": "user",
                    "content": json.dumps(payload, ensure_ascii=False),
                },
            ],
        }
        return payload, request

    def worker(item: dict) -> dict:
        payload, request = request_for(item)
        started = time.perf_counter()
        response = base.client().chat.completions.create(**request)
        latency = time.perf_counter() - started
        result = generation.parse_json(
            response.choices[0].message.content or "{}"
        )
        components, component_errors = (
            generation.validate_question_components(result)
        )
        tags, tag_errors = generation.validate_tags(
            result,
            item["retrieval"]["retrieved_context"],
            {row["component_id"] for row in components},
        )
        structural_errors = [
            error
            for error in component_errors + tag_errors
            if "removed non-verbatim exact_support" not in error
        ]
        if structural_errors:
            raise RuntimeError(
                f"Tagger schema failure for {item['item_id']}: "
                f"{structural_errors}"
            )
        return {
            "item_id": item["item_id"],
            "question_id": item["question"]["question_id"],
            "question_text": item["question"]["question_text"],
            "question_components": components,
            "validated_chunk_tags": tags,
            "validation_errors": component_errors + tag_errors,
            "tag_model": MODEL,
            "tag_temperature": 0,
            "tag_prompt": base.project_relative(TAG_PROMPT),
            "tag_prompt_payload_sha256": base.payload_sha256(payload),
            "tag_execution_sha256": base.payload_sha256(request),
            "retrieval_system": item["system"],
            "source_retrieval_config_name": item["config_name"],
            "common_tagger_pipeline_id": (
                "layer1_common_soft_tagger_v1"
            ),
            "tag_latency_seconds": latency,
            **base.api_metadata(response, "tag"),
        }

    def reusable(item: dict, row: dict) -> bool:
        _, request = request_for(item)
        return row.get("tag_execution_sha256") == base.payload_sha256(
            request
        )

    started = time.perf_counter()
    rows = base.run_parallel(
        items=items,
        key=lambda row: str(row["item_id"]),
        worker=worker,
        output_path=output,
        workers=workers,
        label="Layer1 common soft tagger",
        resume=resume,
        reuse_validator=reusable,
    )
    return rows, time.perf_counter() - started


def run_common_answers(
    items: list[dict],
    tag_rows: list[dict],
    root_out: Path,
    workers: int,
    resume: bool,
) -> tuple[list[dict], float]:
    prompt = ANSWER_PROMPT.read_text(encoding="utf-8")
    tags_by_item = {row["item_id"]: row for row in tag_rows}
    output = root_out / "common_answers/answers.jsonl"

    def request_for(item: dict) -> dict:
        context = generation.format_tagged_context(
            item["retrieval"]["retrieved_context"],
            tags_by_item[item["item_id"]],
        )
        user_message = base.render(
            prompt,
            context_mode_instructions=generation.TAGGED_MODE,
            question_text=item["question"]["question_text"],
            retrieved_context=context,
        )
        return {
            "model": MODEL,
            "temperature": 0,
            "messages": [
                {"role": "system", "content": base.SYSTEM_MESSAGE},
                {"role": "user", "content": user_message},
            ],
        }

    def worker(item: dict) -> dict:
        request = request_for(item)
        started = time.perf_counter()
        response = base.client().chat.completions.create(**request)
        latency = time.perf_counter() - started
        return {
            **item["retrieval"],
            "item_id": item["item_id"],
            "question_id": item["question"]["question_id"],
            "system_mode": "rag_end_to_end",
            "retrieval_system": item["system"],
            "source_retrieval_config_name": item["config_name"],
            "retrieval_config_name": (
                f"{item['config_name']}_common_soft_tags_v1"
            ),
            "common_tagger_pipeline_id": (
                "layer1_common_soft_tagger_v1"
            ),
            "answer": response.choices[0].message.content or "",
            "answer_model": MODEL,
            "answer_temperature": 0,
            "answer_prompt": base.project_relative(ANSWER_PROMPT),
            "answer_prompt_payload_sha256": base.payload_sha256(
                request
            ),
            "answer_execution_sha256": base.payload_sha256(request),
            "soft_tags_supplied": True,
            "soft_eligibility_tags": tags_by_item[item["item_id"]][
                "validated_chunk_tags"
            ],
            "answer_latency_seconds": latency,
            **base.api_metadata(response, "answer"),
        }

    def reusable(item: dict, row: dict) -> bool:
        request = request_for(item)
        return row.get("answer_execution_sha256") == (
            base.payload_sha256(request)
        )

    started = time.perf_counter()
    rows = base.run_parallel(
        items=items,
        key=lambda row: str(row["item_id"]),
        worker=worker,
        output_path=output,
        workers=workers,
        label="Layer1 common answer generator",
        resume=resume,
        reuse_validator=reusable,
    )
    return rows, time.perf_counter() - started


def write_system_outputs(
    root_out: Path,
    systems: list[str],
    tag_rows: list[dict],
    answer_rows: list[dict],
) -> tuple[list[dict], list[dict]]:
    summaries: list[dict] = []
    all_cost_rows: list[dict] = []
    for system in systems:
        system_out = root_out / system
        system_tags = [
            row for row in tag_rows
            if row["retrieval_system"] == system
        ]
        system_answers = [
            row for row in answer_rows
            if row["retrieval_system"] == system
        ]
        base.write_jsonl(
            system_out / "tags/tag_results.jsonl",
            system_tags,
        )
        base.write_jsonl(
            system_out / "answers/tagged_rag_gpt51.jsonl",
            system_answers,
        )
        ledger = token_ledger(system, system_tags, system_answers)
        ledger_by_stage = {row["stage"]: row for row in ledger}
        base.write_csv(system_out / "tokens/stage_costs.csv", ledger)
        all_cost_rows.extend(ledger)
        summaries.append(
            {
                "system": system,
                "config_name": SYSTEMS[system]["config_name"],
                "retrieval_file": base.project_relative(
                    SYSTEMS[system]["retrieval"]
                ),
                "retrieval_sha256": base.sha256(
                    SYSTEMS[system]["retrieval"]
                ),
                "question_count": len(system_tags),
                "final_chunks_per_question": 10,
                "tag_rows": len(system_tags),
                "answer_rows": len(system_answers),
                "selector_cost_usd": ledger_by_stage[
                    "retrieval_specific_llm_selector"
                ]["estimated_usd"],
                "tagger_cost_usd": ledger_by_stage[
                    "common_soft_tagger"
                ]["estimated_usd"],
                "answer_cost_usd": ledger_by_stage[
                    "common_answer_generation"
                ]["estimated_usd"],
                "tagger_latency_seconds_sum": ledger_by_stage[
                    "common_soft_tagger"
                ]["latency_seconds_sum"],
                "tagger_latency_seconds_mean": ledger_by_stage[
                    "common_soft_tagger"
                ]["latency_seconds_mean"],
                "answer_latency_seconds_sum": ledger_by_stage[
                    "common_answer_generation"
                ]["latency_seconds_sum"],
                "answer_latency_seconds_mean": ledger_by_stage[
                    "common_answer_generation"
                ]["latency_seconds_mean"],
            }
        )
    base.write_csv(root_out / "tokens/all_stage_costs.csv", all_cost_rows)
    return summaries, all_cost_rows


def write_manifest(
    root_out: Path,
    freeze_manifest: dict,
    systems: list[str],
    summaries: list[dict],
    resume: bool,
    stage_wall_clock: dict[str, float],
) -> None:
    manifest = {
        "status": "completed_dev13_layer1_common_tagger_generation",
        "protocol": base.project_relative(PROTOCOL),
        "source_freeze_id": freeze_manifest["freeze_id"],
        "source_freeze_content_commit": freeze_manifest[
            "repository_content_commit"
        ],
        "scope": "Dev13 only; no Test40 execution",
        "systems": systems,
        "model": MODEL,
        "temperature": 0,
        "reasoning_effort": "provider_default_not_explicit",
        "resume_enabled": resume,
        "common_tagger": True,
        "common_answer_generator": True,
        "api_call_schedule": (
            "Question-major with deterministic rotation of system order; "
            "tagger stage completes before answer stage."
        ),
        "full_context_retained": True,
        "chunk_order_retained": True,
        "tagger_model_payload_contains_system_identity": False,
        "tagger_model_payload_contains_gold_or_hidden_rubric": False,
        "retrieval_metrics_computed_before_tagger": True,
        "runtime_measurement": {
            "per_call_latency": (
                "Measured around each current-run API request."
            ),
            "system_latency": (
                "Sum and mean of per-call latency, reported by system."
            ),
            "stage_wall_clock": (
                "Observed elapsed time for the interleaved parallel stage."
            ),
            "inherited_retrieval_latency": (
                "Read from the matched Frozen V3 runtime records."
            ),
        },
        "stage_wall_clock_seconds": stage_wall_clock,
        "input_files": {
            base.project_relative(path): base.sha256(path)
            for path in (
                QUESTIONS,
                TAG_PROMPT,
                ANSWER_PROMPT,
                PROTOCOL,
                FREEZE_MANIFEST,
                RUNNER,
                SELECTOR_LEDGER,
                RETRIEVAL_SUMMARY,
            )
        },
        "system_summaries": summaries,
    }
    (root_out / "experiment_manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )


def validate_resume_contract(
    root_out: Path,
    systems: list[str],
) -> None:
    manifest_path = root_out / "experiment_manifest.json"
    if not manifest_path.exists():
        return
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("systems") != systems:
        raise RuntimeError(
            "Resume system list/order does not match the existing "
            "experiment manifest"
        )
    recorded = manifest.get("input_files", {})
    for path in (
        QUESTIONS,
        TAG_PROMPT,
        ANSWER_PROMPT,
        PROTOCOL,
        FREEZE_MANIFEST,
        RUNNER,
        SELECTOR_LEDGER,
        RETRIEVAL_SUMMARY,
    ):
        rel = base.project_relative(path)
        if recorded.get(rel) != base.sha256(path):
            raise RuntimeError(
                f"Resume input hash mismatch for {rel}"
            )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True)
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument(
        "--systems",
        nargs="+",
        choices=sorted(SYSTEMS),
        default=["hybrid", "bge", "bge_llm"],
    )
    parser.add_argument("--resume", action="store_true")
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Validate frozen inputs and model-visible boundaries without API calls.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    if args.workers < 1:
        raise RuntimeError("--workers must be at least one")
    freeze_manifest = verify_frozen_v3()
    questions = base.read_csv(QUESTIONS)
    selected = list(dict.fromkeys(args.systems))
    for system in selected:
        rows = validate_retrieval(system, SYSTEMS[system]["retrieval"])
        validate_information_boundary(questions, rows)
    if args.validate_only:
        print(
            "VALIDATION PASS: Frozen V3 verified; "
            f"{len(selected)} systems x {len(questions)} questions x "
            "10 chunks; common tagger payload hides system/gold/scores."
        )
        return

    load_dotenv(ROOT / ".env", override=False)
    root_out = base.prepare_output_dir(args.out, resume=args.resume)
    if args.resume:
        validate_resume_contract(root_out, selected)
    retrieval_by_system = {
        system: validate_retrieval(
            system,
            SYSTEMS[system]["retrieval"],
        )
        for system in selected
    }
    items = ordered_items(
        questions,
        retrieval_by_system,
        selected,
    )
    tag_rows, tagger_wall = run_common_tagger(
        items,
        root_out,
        args.workers,
        args.resume,
    )
    answer_rows, answer_wall = run_common_answers(
        items,
        tag_rows,
        root_out,
        args.workers,
        args.resume,
    )
    summaries, _ = write_system_outputs(
        root_out,
        selected,
        tag_rows,
        answer_rows,
    )
    stage_wall_clock = {
        "common_soft_tagger": tagger_wall,
        "common_answer_generation": answer_wall,
        "current_run_total": tagger_wall + answer_wall,
    }
    base.write_csv(
        root_out / "runtime/stage_wall_clock.csv",
        [
            {
                "stage": stage,
                "wall_clock_seconds": seconds,
                "provenance": "Measured in this interleaved run.",
            }
            for stage, seconds in stage_wall_clock.items()
        ],
    )
    write_manifest(
        root_out,
        freeze_manifest,
        selected,
        summaries,
        args.resume,
        stage_wall_clock,
    )
    print(f"Wrote Layer 1 common-tagger outputs to {root_out}")


if __name__ == "__main__":
    main()

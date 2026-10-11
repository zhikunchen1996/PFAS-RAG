from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import common


FROZEN_SCRIPTS = common.FROZEN_V3 / "scripts"
if str(FROZEN_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(FROZEN_SCRIPTS))

import run_dev13_soft_tags_v3 as frozen_generation  # noqa: E402
import runtime_helpers as frozen_runtime  # noqa: E402


SYSTEMS = ("hybrid", "bge", "bge_llm")
CONFIGS = {
    "hybrid": "hybrid_top10_pool60_win0",
    "bge": "bge_base_top10_pool60_nodoccap",
    "bge_llm": "bge_llm_gpt51_pool60_bge30_llm10_fullchunk",
}
FORBIDDEN_TAGGER_KEYS = {
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


def retrieval_paths(
    retrieval_root: Path,
    selector_root: Path,
) -> dict[str, Path]:
    return {
        "hybrid": (
            retrieval_root
            / "retrieval_outputs/rag_outputs_hybrid_top10_pool60_win0.jsonl"
        ),
        "bge": (
            retrieval_root
            / "retrieval_outputs/"
            "rag_outputs_bge_base_top10_pool60_nodoccap.jsonl"
        ),
        "bge_llm": (
            selector_root
            / "retrieval_outputs/"
            "rag_outputs_bge_llm_gpt51_pool60_bge30_llm10_fullchunk.jsonl"
        ),
    }


def tagger_payload(
    question: dict[str, str],
    retrieval: dict[str, Any],
) -> dict[str, Any]:
    payload = {
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
    visible_keys = set(payload)
    for candidate in payload["candidates"]:
        visible_keys.update(candidate)
    leaked = FORBIDDEN_TAGGER_KEYS & visible_keys
    if leaked:
        raise RuntimeError(
            f"Tagger payload exposes forbidden keys: {sorted(leaked)}"
        )
    return payload


def ordered_items(
    questions: list[dict[str, str]],
    retrieval: dict[str, list[dict[str, Any]]],
) -> list[dict[str, Any]]:
    by_system = {
        system: {row["question_id"]: row for row in rows}
        for system, rows in retrieval.items()
    }
    items = []
    for question_index, question in enumerate(questions):
        offset = question_index % len(SYSTEMS)
        rotated = SYSTEMS[offset:] + SYSTEMS[:offset]
        for system in rotated:
            qid = question["question_id"]
            items.append(
                {
                    "item_id": f"{system}::{qid}",
                    "question_id": qid,
                    "system": system,
                    "question": question,
                    "retrieval": by_system[system][qid],
                }
            )
    return items


def answer_user_prompt(
    item: dict[str, Any],
    tag_row: dict[str, Any],
    template: str,
) -> str:
    context = frozen_generation.format_tagged_context(
        item["retrieval"]["retrieved_context"],
        tag_row,
    )
    return frozen_runtime.render(
        template,
        context_mode_instructions=frozen_generation.TAGGED_MODE,
        question_text=item["question"]["question_text"],
        retrieved_context=context,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--retrieval-root", required=True)
    parser.add_argument("--selector-root", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    expected_ids = common.question_ids()
    questions = common.read_csv(common.QUESTIONS)
    paths = retrieval_paths(
        Path(args.retrieval_root).expanduser().resolve(),
        Path(args.selector_root).expanduser().resolve(),
    )
    common.require_exact_path(
        Path(args.retrieval_root).expanduser().resolve(),
        common.RETRIEVAL_RESULTS,
        label="Generation retrieval input",
    )
    common.require_exact_path(
        Path(args.selector_root).expanduser().resolve(),
        common.SELECTOR_RESULTS,
        label="Generation selector input",
    )
    retrieval: dict[str, list[dict[str, Any]]] = {}
    for system, path in paths.items():
        rows = common.ordered_rows(
            common.read_jsonl(path),
            expected_ids,
            source=system,
        )
        common.validate_contexts(rows, expected_count=10, source=system)
        retrieval[system] = rows
    items = ordered_items(questions, retrieval)
    if len(items) != 120:
        raise RuntimeError("Expected 3 systems x 40 Test questions")

    tag_prompt = common.TAGGER_PROMPT.read_text(encoding="utf-8")
    answer_template = common.ANSWER_PROMPT.read_text(encoding="utf-8")
    out = Path(args.out).expanduser().resolve()
    common.require_exact_path(
        out,
        common.GENERATION_RESULTS,
        label="Generation output",
    )
    out.mkdir(parents=True, exist_ok=True)

    def tag_request(item: dict[str, Any]) -> dict[str, Any]:
        return common.json_request(
            system_prompt=tag_prompt,
            payload=tagger_payload(item["question"], item["retrieval"]),
            reasoning_effort=None,
            max_completion_tokens=None,
            temperature=0,
        )

    common.write_jsonl(
        out / "tagger/model_payloads.jsonl",
        [
            {
                "item_id": item["item_id"],
                "question_id": item["question_id"],
                "model_payload": tagger_payload(
                    item["question"],
                    item["retrieval"],
                ),
                "execution_sha256": common.payload_sha256(tag_request(item)),
            }
            for item in items
        ],
    )
    if args.dry_run:
        print(
            "DRY RUN PASS: 120 common-tagger payloads built with no "
            "system/gold/score fields; no API calls."
        )
        return
    tag_output = out / "tagger/tag_results.jsonl"
    answer_output = out / "answers/all_system_answers.jsonl"
    if (tag_output.exists() or answer_output.exists()) and not args.resume:
        raise RuntimeError(
            "Paid generation output already exists; use --resume to avoid "
            "duplicate calls"
        )

    def tag_worker(item: dict[str, Any]) -> dict[str, Any]:
        payload = tagger_payload(item["question"], item["retrieval"])
        result, metadata, request_hash = common.call_json(
            system_prompt=tag_prompt,
            payload=payload,
            reasoning_effort=None,
            max_completion_tokens=None,
            temperature=0,
        )
        components, component_errors = (
            frozen_generation.validate_question_components(result)
        )
        tags, tag_errors = frozen_generation.validate_tags(
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
            raise RuntimeError(f"Tagger schema failure: {structural_errors}")
        return {
            "item_id": item["item_id"],
            "question_id": item["question_id"],
            "execution_sha256": request_hash,
            "question_components": components,
            "validated_chunk_tags": tags,
            "validation_errors": component_errors + tag_errors,
            "metadata": metadata,
        }

    tags = common.run_resumable(
        items=items,
        key=lambda row: str(row["item_id"]),
        expected_execution_hash=lambda item: common.payload_sha256(
            tag_request(item)
        ),
        worker=tag_worker,
        output=tag_output,
        workers=args.workers,
        resume=args.resume,
        label="Test40 common tagger",
    )
    tags_by_item = {row["item_id"]: row for row in tags}

    def answer_request(item: dict[str, Any]) -> dict[str, Any]:
        return common.text_request(
            system_prompt=frozen_runtime.SYSTEM_MESSAGE,
            user_prompt=answer_user_prompt(
                item,
                tags_by_item[item["item_id"]],
                answer_template,
            ),
            temperature=0,
        )

    common.write_jsonl(
        out / "answers/model_payloads.jsonl",
        [
            {
                "item_id": item["item_id"],
                "question_id": item["question_id"],
                "user_prompt": answer_user_prompt(
                    item,
                    tags_by_item[item["item_id"]],
                    answer_template,
                ),
                "execution_sha256": common.payload_sha256(
                    answer_request(item)
                ),
            }
            for item in items
        ],
    )

    def answer_worker(item: dict[str, Any]) -> dict[str, Any]:
        answer, metadata, request_hash = common.call_text(
            system_prompt=frozen_runtime.SYSTEM_MESSAGE,
            user_prompt=answer_user_prompt(
                item,
                tags_by_item[item["item_id"]],
                answer_template,
            ),
            temperature=0,
        )
        if not answer.strip():
            raise RuntimeError("Answer is empty")
        return {
            **item["retrieval"],
            "item_id": item["item_id"],
            "question_id": item["question_id"],
            "retrieval_system": item["system"],
            "source_retrieval_config_name": CONFIGS[item["system"]],
            "common_tagger_pipeline_id": "layer1_common_soft_tagger_v1",
            "system_mode": "rag_end_to_end",
            "answer": answer,
            "answer_model": common.MODEL,
            "answer_temperature": 0,
            "answer_prompt": common.project_relative(common.ANSWER_PROMPT),
            "soft_tags_supplied": True,
            "soft_eligibility_tags": tags_by_item[item["item_id"]][
                "validated_chunk_tags"
            ],
            "execution_sha256": request_hash,
            "metadata": metadata,
        }

    answers = common.run_resumable(
        items=items,
        key=lambda row: str(row["item_id"]),
        expected_execution_hash=lambda item: common.payload_sha256(
            answer_request(item)
        ),
        worker=answer_worker,
        output=answer_output,
        workers=args.workers,
        resume=args.resume,
        label="Test40 common answer generation",
    )

    for system in SYSTEMS:
        system_tags = [
            {**row, "retrieval_system_local_only": system}
            for row in tags
            if row["item_id"].startswith(f"{system}::")
        ]
        system_answers = [
            row for row in answers if row["retrieval_system"] == system
        ]
        if len(system_tags) != 40 or len(system_answers) != 40:
            raise RuntimeError(f"{system}: incomplete tag or answer output")
        common.write_jsonl(
            out / system / "tags/tag_results.jsonl",
            system_tags,
        )
        common.write_jsonl(
            out / system / "answers/tagged_rag_gpt51.jsonl",
            system_answers,
        )

    all_metadata = [
        ("tagger", row["metadata"]) for row in tags
    ] + [("answer", row["metadata"]) for row in answers]
    common.write_json(
        out / "run_manifest.json",
        {
            "protocol_id": "test40_formal_v1_common_tagger_generation",
            "status": "complete",
            "question_count": 40,
            "systems": list(SYSTEMS),
            "model": common.MODEL,
            "required_snapshot": common.EXPECTED_MODEL,
            "temperature": 0,
            "tagger_reasoning_effort": "provider_default_not_sent",
            "full_context_retained": True,
            "chunk_order_retained": True,
            "tagger_model_payload_contains_system_identity": False,
            "tagger_model_payload_contains_gold_or_hidden_rubric": False,
            "retrieval_metrics_computed_before_tagger": True,
            "questions_sha256": common.sha256(common.QUESTIONS),
            "tagger_prompt_sha256": common.sha256(common.TAGGER_PROMPT),
            "answer_prompt_sha256": common.sha256(common.ANSWER_PROMPT),
            "retrieval_inputs": {
                system: {
                    "path": common.project_relative(path),
                    "sha256": common.sha256(path),
                }
                for system, path in paths.items()
            },
            "tagger_api_calls": len(tags),
            "answer_api_calls": len(answers),
            "stage_usage": {
                stage: {
                    "total_tokens": sum(
                        int(metadata["total_tokens"])
                        for row_stage, metadata in all_metadata
                        if row_stage == stage
                    ),
                    "estimated_cost_usd": sum(
                        float(metadata["estimated_cost_usd"])
                        for row_stage, metadata in all_metadata
                        if row_stage == stage
                    ),
                    "latency_seconds_sum": sum(
                        float(metadata["latency_seconds"])
                        for row_stage, metadata in all_metadata
                        if row_stage == stage
                    ),
                }
                for stage in ("tagger", "answer")
            },
            "resume_hash_validated": True,
        },
    )


if __name__ == "__main__":
    main()

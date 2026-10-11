from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path

from dotenv import load_dotenv


ROOT = Path(__file__).resolve().parents[3]
V3 = ROOT / "benchmark/frozen_v3"
OUT: Path | None = None

QUESTIONS = V3 / "input/questions_dev13.csv"
RETRIEVAL = V3 / (
    "results/dev13_retrieval_budget_gpt51_2026-07-26/"
    "bge_llm_gpt51/retrieval_outputs/"
    "rag_outputs_bge_llm_gpt51_pool60_bge30_llm10_fullchunk.jsonl"
)
SELECTOR_PROMPT = V3 / "prompts/retrieval/bge_llm_selector_v3.txt"
TAG_PROMPT = V3 / "prompts/evaluation/soft_eligibility_tagger_v3.txt"
ANSWER_PROMPT = V3 / "prompts/evaluation/rag_answer_prompt_soft_tags_v3.txt"
DIRECT_PROMPT = (
    V3 / "prompts/evaluation/direct_answer_prompt_matched_v3.txt"
)

MODEL = "gpt-5.1"
VALID_LABELS = {
    "direct_evidence",
    "background",
    "nearby_but_mismatched",
    "irrelevant",
}
VALID_DETAIL_POLICIES = {
    "use_full_claim",
    "category_only",
    "limitation_only",
    "qualitative_relationship",
    "quantitative_detail",
    "procedural_detail",
    "do_not_use",
}
VALID_POLARITIES = {
    "support",
    "limitation",
    "contradiction",
    "mixed",
    "none",
}

TAGGED_MODE = """Each passage includes advisory tags generated only from the
visible question. The tags are not evidence and are not ground truth. Verify
them against the full chunk and override a tag only when the chunk clearly
supports a different use.

Apply the detail policy as follows:
- use_full_claim: use the narrow supported claim and necessary qualifiers.
- category_only: use only the relevant entity, method, material, evidence type,
  outcome, metric, route, or category identity.
- limitation_only: use only the explicit limitation, uncertainty, negative
  result, contradiction, bottleneck, evidence gap, or research need.
- qualitative_relationship: use only the supported direction, pattern,
  association, contrast, or relationship without unnecessary quantitative or
  procedural detail.
- quantitative_detail: preserve only a reported value whose metric, unit,
  denominator, and contextual scope materially answer the question.
- procedural_detail: preserve only directly reported actions, materials,
  settings, durations, amounts, or condition-dependent variations that
  materially answer the question.
- do_not_use: do not use the chunk to support the answer.

Only categorical tags and a locally verified verbatim excerpt are supplied.
The categorical tags are advisory classifications, not factual claims. The
verified excerpt and full chunk are the only answer-facing source text."""

UNTAGGED_MODE = """No advisory tag layer is provided. Inspect every full chunk
directly and independently determine whether it is direct evidence,
background, nearby but mismatched evidence, or irrelevant. Use only details
that materially answer the visible question."""

import runtime_helpers as base

if Path(base.__file__).resolve().parent != Path(__file__).resolve().parent:
    raise RuntimeError("Resolved runtime_helpers outside Frozen V3 scripts")


def parse_json(content: str) -> dict:
    try:
        value = json.loads(content)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", content, flags=re.DOTALL)
        if not match:
            return {}
        try:
            value = json.loads(match.group(0))
        except json.JSONDecodeError:
            return {}
    return value if isinstance(value, dict) else {}


def normalized_text(value: str) -> str:
    value = unicodedata.normalize("NFKC", str(value))
    value = value.replace("\u00ad", "")
    return re.sub(r"\s+", " ", value).strip()


def validate_question_components(
    raw_result: dict,
) -> tuple[list[dict], list[str]]:
    raw_components = raw_result.get("question_components", [])
    if not isinstance(raw_components, list):
        raw_components = []
    components: list[dict] = []
    errors: list[str] = []
    used_ids: set[str] = set()
    for index, raw_component in enumerate(raw_components, start=1):
        if not isinstance(raw_component, dict):
            errors.append("discarded non-object question component")
            continue
        component_id = str(
            raw_component.get("component_id", f"R{index}")
        ).strip()
        description = str(raw_component.get("description", "")).strip()
        if not re.fullmatch(r"R[1-9][0-9]*", component_id):
            errors.append(
                f"replaced invalid component_id {component_id!r}"
            )
            component_id = f"R{index}"
        if component_id in used_ids:
            errors.append(
                f"discarded duplicate component_id {component_id}"
            )
            continue
        if not description:
            errors.append(
                f"discarded empty component description {component_id}"
            )
            continue
        components.append(
            {
                "component_id": component_id,
                "description": description,
            }
        )
        used_ids.add(component_id)
    if not components:
        errors.append("inserted fallback question component R1")
        components = [
            {
                "component_id": "R1",
                "description": "The visible research question as a whole.",
            }
        ]
    return components, errors


def validate_tags(
    raw_result: dict,
    candidates: list[dict],
    valid_component_ids: set[str],
) -> tuple[list[dict], list[str]]:
    raw_tags = raw_result.get("chunk_tags", [])
    if not isinstance(raw_tags, list):
        raw_tags = []

    by_id: dict[int, dict] = {}
    errors: list[str] = []
    for raw_tag in raw_tags:
        if not isinstance(raw_tag, dict):
            errors.append("discarded non-object tag")
            continue
        try:
            candidate_id = int(raw_tag.get("candidate_id"))
        except (TypeError, ValueError):
            errors.append("discarded tag with invalid candidate_id")
            continue
        if candidate_id < 1 or candidate_id > len(candidates):
            errors.append(f"discarded unknown candidate_id {candidate_id}")
            continue
        if candidate_id in by_id:
            errors.append(f"discarded duplicate candidate_id {candidate_id}")
            continue

        eligibility = str(
            raw_tag.get("eligibility", "")
        ).strip().lower()
        if eligibility not in VALID_LABELS:
            errors.append(
                f"candidate {candidate_id}: invalid eligibility "
                f"{eligibility!r}"
            )
            eligibility = "irrelevant"

        detail_policy = str(
            raw_tag.get("detail_policy", "do_not_use")
        ).strip().lower()
        if detail_policy not in VALID_DETAIL_POLICIES:
            errors.append(
                f"candidate {candidate_id}: invalid detail_policy "
                f"{detail_policy!r}"
            )
            detail_policy = "do_not_use"

        supports = raw_tag.get("supports_components", [])
        if not isinstance(supports, list):
            supports = [str(supports)]
        validated_supports = []
        for value in supports:
            component_id = str(value).strip()
            if component_id in valid_component_ids:
                validated_supports.append(component_id)
            elif component_id:
                errors.append(
                    f"candidate {candidate_id}: removed unknown component "
                    f"{component_id!r}"
                )
        excerpt = str(raw_tag.get("exact_support", "")).strip().strip(
            "\"'“”‘’"
        )
        if excerpt and normalized_text(excerpt) not in normalized_text(
            candidates[candidate_id - 1].get("text", "")
        ):
            errors.append(
                f"candidate {candidate_id}: removed non-verbatim exact_support"
            )
            excerpt = ""

        try:
            confidence = float(raw_tag.get("confidence", 0.0))
        except (TypeError, ValueError):
            errors.append(
                f"candidate {candidate_id}: invalid confidence "
                f"{raw_tag.get('confidence')!r}"
            )
            confidence = 0.0
        evidence_polarity = str(
            raw_tag.get("evidence_polarity", "none")
        ).strip().lower()
        if evidence_polarity not in VALID_POLARITIES:
            errors.append(
                f"candidate {candidate_id}: invalid evidence_polarity "
                f"{evidence_polarity!r}"
            )
            evidence_polarity = "none"

        by_id[candidate_id] = {
            "candidate_id": candidate_id,
            "eligibility": eligibility,
            "detail_policy": detail_policy,
            "supports_components": validated_supports,
            "evidence_polarity": evidence_polarity,
            "exact_support": normalized_text(excerpt) if excerpt else "",
            "exact_support_validated": bool(excerpt),
            "confidence": max(0.0, min(1.0, confidence)),
        }

    validated: list[dict] = []
    for candidate_id in range(1, len(candidates) + 1):
        if candidate_id not in by_id:
            errors.append(f"candidate {candidate_id}: missing tag")
            by_id[candidate_id] = {
                "candidate_id": candidate_id,
                "eligibility": "irrelevant",
                "detail_policy": "do_not_use",
                "supports_components": [],
                "evidence_polarity": "none",
                "exact_support": "",
                "exact_support_validated": False,
                "confidence": 0.0,
            }
        validated.append(by_id[candidate_id])
    return validated, errors


def load_inputs() -> tuple[list[dict], list[dict]]:
    questions = base.read_csv(QUESTIONS)
    retrieval_rows = base.read_jsonl(RETRIEVAL)
    if len(questions) != 13:
        raise RuntimeError(f"Expected 13 Dev questions; found {len(questions)}")
    question_qids = [str(row.get("question_id", "")).strip() for row in questions]
    if any(not qid for qid in question_qids):
        raise RuntimeError("Every Dev question must have a non-empty question_id")
    if len(question_qids) != len(set(question_qids)):
        raise RuntimeError("Duplicate question_id in Dev questions")
    if any(not str(row.get("question_text", "")).strip() for row in questions):
        raise RuntimeError("Every Dev question must have non-empty question_text")

    if len(retrieval_rows) != 13:
        raise RuntimeError(
            f"Expected exactly 13 retrieval rows; found {len(retrieval_rows)}"
        )
    retrieval_qids = [
        str(row.get("question_id", "")).strip() for row in retrieval_rows
    ]
    if len(retrieval_qids) != len(set(retrieval_qids)):
        raise RuntimeError("Duplicate question_id in fixed retrieval input")
    if set(retrieval_qids) != set(question_qids):
        missing = sorted(set(question_qids) - set(retrieval_qids))
        extra = sorted(set(retrieval_qids) - set(question_qids))
        raise RuntimeError(
            f"Fixed retrieval membership mismatch; missing={missing}, extra={extra}"
        )
    retrieval_by_qid = {
        row["question_id"]: row for row in retrieval_rows
    }
    for qid, row in retrieval_by_qid.items():
        context = row.get("retrieved_context", [])
        if not isinstance(context, list):
            raise RuntimeError(f"retrieved_context is not a list for {qid}")
        count = len(context)
        if count != 10:
            raise RuntimeError(
                f"Expected 10 chunks for {qid}; found {count}"
            )
        identities = []
        for index, hit in enumerate(context, start=1):
            if not isinstance(hit, dict):
                raise RuntimeError(f"Non-object context C{index} for {qid}")
            doc_id = str(hit.get("doc_id") or "").strip()
            chunk_id = str(hit.get("chunk_id") or "").strip()
            text = str(hit.get("text") or "").strip()
            if not doc_id or not chunk_id or not text:
                raise RuntimeError(
                    f"Incomplete context identity/text at {qid} C{index}"
                )
            identities.append((doc_id, chunk_id))
        if len(identities) != len(set(identities)):
            raise RuntimeError(f"Duplicate context chunk identity for {qid}")
    ordered_retrieval = [
        retrieval_by_qid[question["question_id"]] for question in questions
    ]
    return questions, ordered_retrieval


def run_tagger(
    questions: list[dict],
    retrieval_rows: list[dict],
    workers: int,
    resume: bool,
) -> list[dict]:
    retrieval_by_qid = {row["question_id"]: row for row in retrieval_rows}
    system_prompt = TAG_PROMPT.read_text(encoding="utf-8")
    output = OUT / "tags/tag_results.jsonl"

    def key(question: dict) -> str:
        return str(question["question_id"])

    def request_for(
        question: dict,
    ) -> tuple[dict, dict, list[dict]]:
        qid = question["question_id"]
        context = retrieval_by_qid[qid]["retrieved_context"]
        payload = {
            "question": question["question_text"],
            "candidates": [
                {
                    "candidate_id": index,
                    "source": hit.get("citation") or hit.get("doc_id", ""),
                    "section": hit.get("section", ""),
                    "text": hit.get("text", ""),
                }
                for index, hit in enumerate(context, start=1)
            ],
        }
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
        return payload, request, context

    def worker(question: dict) -> dict:
        qid = question["question_id"]
        payload, request, context = request_for(question)
        response = base.client().chat.completions.create(
            **request
        )
        raw = response.choices[0].message.content or "{}"
        result = parse_json(raw)
        components, component_errors = validate_question_components(result)
        tags, tag_errors = validate_tags(
            result,
            context,
            {row["component_id"] for row in components},
        )
        structural_errors = [
            error
            for error in component_errors + tag_errors
            if "removed non-verbatim exact_support" not in error
        ]
        if structural_errors:
            raise RuntimeError(
                f"Tagger schema failure for {qid}: {structural_errors}"
            )
        return {
            "question_id": qid,
            "question_text": question["question_text"],
            "question_components": components,
            "validated_chunk_tags": tags,
            "validation_errors": component_errors + tag_errors,
            "tag_model": MODEL,
            "tag_temperature": 0,
            "tag_prompt": base.project_relative(TAG_PROMPT),
            "tag_prompt_payload_sha256": base.payload_sha256(payload),
            "tag_execution_sha256": base.payload_sha256(request),
            **base.api_metadata(response, "tag"),
        }

    def reusable(question: dict, row: dict) -> bool:
        _, request, _ = request_for(question)
        return row.get("tag_execution_sha256") == base.payload_sha256(
            request
        )

    rows = base.run_parallel(
        items=questions,
        key=key,
        worker=worker,
        output_path=output,
        workers=workers,
        label="Dev13 V3 soft eligibility tagger",
        resume=resume,
        reuse_validator=reusable,
    )
    base.write_csv(
        OUT / "tokens/tagger.csv",
        [
            base.token_row(
                "soft_eligibility_tagger",
                "bge_llm_v3_soft_tags",
                rows,
                "tag",
                "Visible question and ten full chunks; no gold.",
            )
        ],
    )
    return rows


def format_plain_context(context: list[dict]) -> str:
    blocks = []
    for index, hit in enumerate(context, start=1):
        blocks.append(
            "\n".join(
                [
                    f"[C{index}]",
                    f"Source: {hit.get('citation') or hit.get('doc_id', '')}",
                    f"Section: {hit.get('section') or 'unknown'}",
                    "Full chunk:",
                    str(hit.get("text", "")),
                ]
            )
        )
    return "\n\n".join(blocks)


def format_tagged_context(context: list[dict], tag_row: dict) -> str:
    tags = tag_row["validated_chunk_tags"]
    if len(context) != len(tags):
        raise RuntimeError("Context and tag counts do not match")
    blocks = []
    for index, (hit, tag) in enumerate(zip(context, tags), start=1):
        if tag["candidate_id"] != index:
            raise RuntimeError("Tag order does not match context order")
        blocks.append(
            "\n".join(
                [
                    f"[C{index}]",
                    "Advisory categorical tags (not evidence):",
                    f"- evidence role: {tag['eligibility']}",
                    f"- detail policy: {tag['detail_policy']}",
                    f"- evidence polarity: {tag['evidence_polarity']}",
                    f"- confidence: {tag['confidence']:.2f}",
                    "- locally verified verbatim excerpt: "
                    + (tag["exact_support"] or "[none; inspect full chunk]"),
                    f"Source: {hit.get('citation') or hit.get('doc_id', '')}",
                    f"Section: {hit.get('section') or 'unknown'}",
                    "Full chunk:",
                    str(hit.get("text", "")),
                ]
            )
        )
    return "\n\n".join(blocks)


def generate_answers(
    questions: list[dict],
    retrieval_rows: list[dict],
    tag_rows: list[dict],
    workers: int,
    tagged: bool,
    resume: bool,
) -> list[dict]:
    retrieval_by_qid = {row["question_id"]: row for row in retrieval_rows}
    tags_by_qid = {row["question_id"]: row for row in tag_rows}
    prompt = ANSWER_PROMPT.read_text(encoding="utf-8")
    system_label = "tagged" if tagged else "matched_untagged"
    output = OUT / f"answers/{system_label}_rag_gpt51.jsonl"

    def key(question: dict) -> str:
        return str(question["question_id"])

    def request_for(
        question: dict,
    ) -> tuple[dict, list[dict], dict]:
        qid = question["question_id"]
        retrieval = retrieval_by_qid[qid]
        context = retrieval["retrieved_context"]
        if tagged:
            formatted_context = format_tagged_context(
                context,
                tags_by_qid[qid],
            )
            mode = TAGGED_MODE
        else:
            formatted_context = format_plain_context(context)
            mode = UNTAGGED_MODE
        user_message = base.render(
            prompt,
            context_mode_instructions=mode,
            question_text=question["question_text"],
            retrieved_context=formatted_context,
        )
        payload = {
            "model": MODEL,
            "temperature": 0,
            "messages": [
                {"role": "system", "content": base.SYSTEM_MESSAGE},
                {"role": "user", "content": user_message},
            ],
        }
        return retrieval, context, payload

    def worker(question: dict) -> dict:
        qid = question["question_id"]
        retrieval, _, payload = request_for(question)
        response = base.client().chat.completions.create(**payload)
        result = {
            **retrieval,
            "question_id": qid,
            "system_mode": "rag_end_to_end",
            "answer": response.choices[0].message.content or "",
            "answer_model": MODEL,
            "answer_temperature": 0,
            "answer_prompt": base.project_relative(ANSWER_PROMPT),
            "answer_prompt_payload_sha256": base.payload_sha256(payload),
            "answer_execution_sha256": base.payload_sha256(payload),
            "retrieval_config_name": (
                "bge_llm_gpt51_pool60_bge30_llm10_soft_tags_v3"
                if tagged
                else "bge_llm_gpt51_pool60_bge30_llm10_matched_untagged_v3"
            ),
            "soft_tags_supplied": tagged,
            **base.api_metadata(response, "answer"),
        }
        if tagged:
            result["soft_eligibility_tags"] = tags_by_qid[qid][
                "validated_chunk_tags"
            ]
        return result

    def reusable(question: dict, row: dict) -> bool:
        _, _, payload = request_for(question)
        return row.get("answer_execution_sha256") == base.payload_sha256(
            payload
        )

    rows = base.run_parallel(
        items=questions,
        key=key,
        worker=worker,
        output_path=output,
        workers=workers,
        label=f"Dev13 V3 {system_label} answer",
        resume=resume,
        reuse_validator=reusable,
    )
    return rows


def generate_direct_answers(
    questions: list[dict],
    workers: int,
    resume: bool,
) -> list[dict]:
    prompt = DIRECT_PROMPT.read_text(encoding="utf-8")
    output = OUT / "answers/matched_direct_gpt51.jsonl"

    def key(question: dict) -> str:
        return str(question["question_id"])

    def request_for(question: dict) -> dict:
        user_message = base.render(
            prompt,
            question_text=question["question_text"],
        )
        payload = {
            "model": MODEL,
            "temperature": 0,
            "messages": [
                {"role": "system", "content": base.SYSTEM_MESSAGE},
                {"role": "user", "content": user_message},
            ],
        }
        return payload

    def worker(question: dict) -> dict:
        payload = request_for(question)
        response = base.client().chat.completions.create(**payload)
        return {
            "question_id": question["question_id"],
            "system_mode": "direct_closed_book",
            "answer": response.choices[0].message.content or "",
            "answer_model": MODEL,
            "answer_temperature": 0,
            "answer_prompt": base.project_relative(DIRECT_PROMPT),
            "answer_prompt_payload_sha256": base.payload_sha256(payload),
            "answer_execution_sha256": base.payload_sha256(payload),
            "soft_tags_supplied": False,
            **base.api_metadata(response, "answer"),
        }

    def reusable(question: dict, row: dict) -> bool:
        payload = request_for(question)
        return row.get("answer_execution_sha256") == base.payload_sha256(
            payload
        )

    return base.run_parallel(
        items=questions,
        key=key,
        worker=worker,
        output_path=output,
        workers=workers,
        label="Dev13 V3 matched Direct answer",
        resume=resume,
        reuse_validator=reusable,
    )


def write_generation_manifest(
    tag_rows: list[dict],
    tagged_answers: list[dict],
    untagged_answers: list[dict] | None,
    direct_answers: list[dict] | None,
    resume: bool,
) -> None:
    if OUT is None:
        raise RuntimeError("Output directory has not been configured")
    tag_tokens = base.token_row(
        "soft_eligibility_tagger",
        "tagged",
        tag_rows,
        "tag",
        "V3 tagger cost.",
    )
    tagged_tokens = base.token_row(
        "answer_generation",
        "tagged",
        tagged_answers,
        "answer",
        "Full context plus advisory tags.",
    )
    token_rows = [tag_tokens, tagged_tokens]
    if untagged_answers is not None:
        token_rows.append(
            base.token_row(
                "answer_generation",
                "matched_untagged",
                untagged_answers,
                "answer",
                "Same full context and base answer prompt without tags.",
            )
        )
    if direct_answers is not None:
        token_rows.append(
            base.token_row(
                "answer_generation",
                "matched_direct",
                direct_answers,
                "answer",
                "No retrieval, reference-answer, corpus, or web access.",
            )
        )
    base.write_csv(OUT / "tokens/generation.csv", token_rows)

    label_counts: dict[str, dict[str, int]] = {}
    policy_counts: dict[str, dict[str, int]] = {}
    validation_errors: dict[str, int] = {}
    for row in tag_rows:
        labels = {value: 0 for value in sorted(VALID_LABELS)}
        policies = {
            value: 0 for value in sorted(VALID_DETAIL_POLICIES)
        }
        for tag in row["validated_chunk_tags"]:
            labels[tag["eligibility"]] += 1
            policies[tag["detail_policy"]] += 1
        qid = row["question_id"]
        label_counts[qid] = labels
        policy_counts[qid] = policies
        validation_errors[qid] = len(row["validation_errors"])

    prompt_tokens = sum(
        int(row["prompt_tokens_total"]) for row in token_rows
    )
    completion_tokens = sum(
        int(row["completion_tokens_total"]) for row in token_rows
    )
    manifest = {
        "status": "frozen_canonical_generation",
        "protocol": (
            "benchmark/frozen_v3/methods/"
            "dev13_verified_tags_v3_protocol.json"
        ),
        "question_count": len(tag_rows),
        "questions": [row["question_id"] for row in tag_rows],
        "model_requested": MODEL,
        "temperature": 0,
        "resume_enabled": resume,
        "gold_hidden_from_tagger_and_answer": True,
        "full_context_retained": True,
        "chunk_order_retained": True,
        "matched_answer_prompt": True,
        "intended_difference": (
            "Categorical advisory tags plus locally verified verbatim "
            "excerpts; no tagger-generated free-text advice."
        ),
        "verbatim_exact_support_validation": True,
        "answer_visible_tag_fields": [
            "eligibility",
            "detail_policy",
            "evidence_polarity",
            "confidence",
            "exact_support",
        ],
        "audit_only_tag_fields": [
            "question_components",
            "supports_components",
        ],
        "free_text_advisory_fields_exposed": False,
        "tag_models_returned": sorted(
            {
                row.get("tag_response_model", "")
                for row in tag_rows
                if row.get("tag_response_model")
            }
        ),
        "answer_models_returned": sorted(
            {
                row.get("answer_response_model", "")
                for row in (
                    tagged_answers
                    + (untagged_answers or [])
                    + (direct_answers or [])
                )
                if row.get("answer_response_model")
            }
        ),
        "input_files": {
            base.project_relative(path): base.sha256(path)
            for path in (
                QUESTIONS,
                RETRIEVAL,
                SELECTOR_PROMPT,
                TAG_PROMPT,
                ANSWER_PROMPT,
                DIRECT_PROMPT,
            )
        },
        "matched_untagged_generated": untagged_answers is not None,
        "matched_direct_generated": direct_answers is not None,
        "label_counts": label_counts,
        "detail_policy_counts": policy_counts,
        "validation_error_counts": validation_errors,
        "token_accounting": {
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "total_tokens": prompt_tokens + completion_tokens,
            "estimated_usd": (
                prompt_tokens / 1_000_000 * 1.25
                + completion_tokens / 1_000_000 * 10.0
            ),
            "price_basis_usd_per_million": {
                "input": 1.25,
                "output": 10.0,
            },
        },
    }
    (OUT / "generation_manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    global OUT
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument(
        "--out",
        required=True,
        help=(
            "New result directory. A non-empty directory is accepted only "
            "with --resume."
        ),
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help=(
            "Reuse only existing rows produced by this frozen execution "
            "contract. The canonical default is a fresh run."
        ),
    )
    parser.add_argument(
        "--include-untagged",
        action="store_true",
        help="Generate the historical matched untagged diagnostic.",
    )
    parser.add_argument(
        "--include-direct",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Generate the prompt-matched Direct control (default: true).",
    )
    args = parser.parse_args()

    load_dotenv(ROOT / ".env", override=False)
    OUT = base.prepare_output_dir(args.out, resume=args.resume)
    optional_outputs = {
        "matched untagged": (
            args.include_untagged,
            OUT / "answers/matched_untagged_rag_gpt51.jsonl",
        ),
        "matched Direct": (
            args.include_direct,
            OUT / "answers/matched_direct_gpt51.jsonl",
        ),
    }
    for label, (enabled, path) in optional_outputs.items():
        if not enabled and path.exists():
            raise RuntimeError(
                f"Refusing to leave stale {label} output at {path}; "
                "use the canonical options or a fresh result directory."
            )
    questions, retrieval_rows = load_inputs()
    tag_rows = run_tagger(
        questions,
        retrieval_rows,
        args.workers,
        args.resume,
    )
    tagged_answers = generate_answers(
        questions,
        retrieval_rows,
        tag_rows,
        args.workers,
        tagged=True,
        resume=args.resume,
    )
    untagged_answers = (
        generate_answers(
            questions,
            retrieval_rows,
            tag_rows,
            args.workers,
            tagged=False,
            resume=args.resume,
        )
        if args.include_untagged
        else None
    )
    direct_answers = (
        generate_direct_answers(
            questions,
            args.workers,
            args.resume,
        )
        if args.include_direct
        else None
    )
    write_generation_manifest(
        tag_rows,
        tagged_answers,
        untagged_answers,
        direct_answers,
        args.resume,
    )
    print(f"Wrote V3 Dev13 generation outputs to {OUT}", flush=True)


if __name__ == "__main__":
    main()

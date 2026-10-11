from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path
from statistics import mean

from dotenv import load_dotenv


ROOT = Path(__file__).resolve().parents[3]
V3 = ROOT / "benchmark/frozen_v3"
SOURCE_RUN = (
    V3 / "results/dev13_verified_tags_v3_r2_confirmation_2026-07-26"
)
OUT: Path | None = None

QUESTIONS = V3 / "input/questions_dev13.csv"
GOLD = V3 / "gold/chunk_based_gold.jsonl"
TAGGED = SOURCE_RUN / "answers/tagged_rag_gpt51.jsonl"
UNTAGGED = SOURCE_RUN / "answers/matched_untagged_rag_gpt51.jsonl"
DIRECT = SOURCE_RUN / "answers/matched_direct_gpt51.jsonl"
JUDGE_PROMPT = (
    V3
    / "prompts/evaluation/neutral_evidence_pairwise_content_v3.txt"
)
COMMON_RETRIEVAL_FILES = (
    V3
    / (
        "results/dev13_retrieval_budget_gpt51_2026-07-26/"
        "local_hybrid_bge/retrieval_outputs/"
        "rag_outputs_hybrid_top10_pool60_win0.jsonl"
    ),
    V3
    / (
        "results/dev13_retrieval_budget_gpt51_2026-07-26/"
        "local_hybrid_bge/retrieval_outputs/"
        "rag_outputs_bge_base_top10_pool60_nodoccap.jsonl"
    ),
    V3
    / (
        "results/dev13_retrieval_budget_gpt51_2026-07-26/"
        "bge_llm_gpt51/retrieval_outputs/"
        "rag_outputs_bge_llm_gpt51_pool60_bge30_llm10_fullchunk.jsonl"
    ),
)

MODEL = "gpt-5.1"
CRITERIA = (
    "scientific_correctness",
    "question_fulfillment",
    "uncertainty_and_limitations",
    "practical_usefulness",
)
WEIGHTS = {
    "scientific_correctness": 0.40,
    "question_fulfillment": 0.30,
    "uncertainty_and_limitations": 0.15,
    "practical_usefulness": 0.15,
}
CITATION_PATTERN = re.compile(r"\[C(\d+)\]", flags=re.IGNORECASE)
HEADING_PATTERN = re.compile(
    r"(?im)^\s*(?:#{1,6}\s*)?(?:\d+\.\s*)?\**"
    r"(Answerability|Answer|Uncertainty and limitations|"
    r"Practical takeaway)"
    r"\**\s*:?\s*$"
)

import runtime_helpers as base
import run_dev13_soft_tags_v3 as generation

for module in (base, generation):
    if Path(module.__file__).resolve().parent != Path(__file__).resolve().parent:
        raise RuntimeError(
            f"Resolved {module.__name__} outside Frozen V3 scripts"
        )


def extract_sections(answer: str) -> dict[str, str]:
    matches = list(HEADING_PATTERN.finditer(answer))
    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        start = match.end()
        end = (
            matches[index + 1].start()
            if index + 1 < len(matches)
            else len(answer)
        )
        heading = match.group(1).lower()
        if heading in sections:
            raise RuntimeError(f"Duplicate answer section: {heading}")
        sections[heading] = answer[start:end].strip()
    return sections


def normalized_answer_without_citations(answer: str) -> str:
    sections = extract_sections(answer)
    selected = (
        ("Answerability", sections.get("answerability", "")),
        ("Answer", sections.get("answer", "")),
        (
            "Uncertainty and limitations",
            sections.get("uncertainty and limitations", ""),
        ),
        ("Practical takeaway", sections.get("practical takeaway", "")),
    )
    missing = [heading for heading, value in selected if not value]
    if missing:
        raise RuntimeError(f"Missing answer sections: {missing}")
    text = "\n\n".join(
        f"{heading}\n{value}" for heading, value in selected
    )
    text = CITATION_PATTERN.sub("", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r" {2,}", " ", text)
    return text.strip()


def context_digest(context: list[dict]) -> str:
    payload = json.dumps(
        context,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def first_assignment(
    comparison: str,
    qid: str,
    left_system: str,
    right_system: str,
) -> tuple[str, str]:
    digest = hashlib.sha256(
        (
            f"soft-tags-v3::{comparison}::{qid}::"
            "source-verified-citation-neutral"
        ).encode()
    ).digest()
    return (
        (left_system, right_system)
        if digest[0] % 2 == 0
        else (right_system, left_system)
    )


def validate_inputs(
    questions: list[dict],
    tagged_rows: list[dict],
    untagged_rows: list[dict] | None,
    direct_rows: list[dict] | None,
) -> None:
    generation_manifest_path = SOURCE_RUN / "generation_manifest.json"
    if not generation_manifest_path.is_file():
        raise RuntimeError("Missing canonical generation manifest")
    generation_manifest = json.loads(
        generation_manifest_path.read_text(encoding="utf-8")
    )
    if generation_manifest.get("status") != "frozen_canonical_generation":
        raise RuntimeError("Source answers are not a canonical generation run")
    if bool(generation_manifest.get("matched_untagged_generated")) != (
        untagged_rows is not None
    ):
        raise RuntimeError(
            "Source-run manifest and requested untagged comparison differ"
        )
    if bool(generation_manifest.get("matched_direct_generated")) != (
        direct_rows is not None
    ):
        raise RuntimeError(
            "Source-run manifest and requested Direct comparison differ"
        )
    for relative_path, expected_hash in generation_manifest.get(
        "input_files",
        {},
    ).items():
        path = ROOT / relative_path
        if not path.is_file() or base.sha256(path) != expected_hash:
            raise RuntimeError(
                f"Generation input hash mismatch: {relative_path}"
            )

    expected_qids = [row["question_id"] for row in questions]
    for label, rows in (
        ("tagged", tagged_rows),
        ("untagged", untagged_rows or []),
        ("direct", direct_rows or []),
    ):
        if label == "direct" and direct_rows is None:
            continue
        if label == "untagged" and untagged_rows is None:
            continue
        qids = [row["question_id"] for row in rows]
        if qids != expected_qids:
            raise RuntimeError(
                f"{label} question order or membership differs from Dev13"
            )
        if any(not str(row.get("answer", "")).strip() for row in rows):
            raise RuntimeError(f"{label} contains an empty answer")

    question_by_qid = {
        row["question_id"]: row for row in questions
    }
    untagged_by_qid = {
        row["question_id"]: row for row in (untagged_rows or [])
    }
    for tagged in tagged_rows:
        qid = tagged["question_id"]
        tagged_context = tagged.get("retrieved_context", [])
        if len(tagged_context) != 10:
            raise RuntimeError(
                f"Expected ten verification chunks for {qid}"
            )
        if untagged_rows is not None:
            untagged_context = untagged_by_qid[qid].get(
                "retrieved_context",
                [],
            )
            if context_digest(tagged_context) != context_digest(
                untagged_context
            ):
                raise RuntimeError(
                    f"Tagged and untagged contexts differ for {qid}"
                )
        answer_rows = [("tagged", tagged.get("answer", ""))]
        if untagged_rows is not None:
            answer_rows.append(
                (
                    "untagged",
                    untagged_by_qid[qid].get("answer", ""),
                )
            )
        for answer_label, answer in answer_rows:
            invalid = sorted(
                {
                    int(value)
                    for value in CITATION_PATTERN.findall(answer)
                    if not 1 <= int(value) <= 10
                }
            )
            if invalid:
                raise RuntimeError(
                    f"{answer_label} {qid} has invalid citations {invalid}"
                )
        tagged_prompt = generation.ANSWER_PROMPT.read_text(encoding="utf-8")
        tagged_context_text = generation.format_tagged_context(
            tagged_context,
            {
                "validated_chunk_tags": tagged.get(
                    "soft_eligibility_tags",
                    [],
                )
            },
        )
        tagged_user_message = base.render(
            tagged_prompt,
            context_mode_instructions=generation.TAGGED_MODE,
            question_text=question_by_qid[qid]["question_text"],
            retrieved_context=tagged_context_text,
        )
        tagged_payload = {
            "model": generation.MODEL,
            "temperature": 0,
            "messages": [
                {"role": "system", "content": base.SYSTEM_MESSAGE},
                {"role": "user", "content": tagged_user_message},
            ],
        }
        tagged_fingerprint = base.payload_sha256(tagged_payload)
        if tagged.get("answer_execution_sha256") != tagged_fingerprint:
            raise RuntimeError(
                f"Tagged answer execution fingerprint mismatch for {qid}"
            )
        if tagged.get("answer_prompt_payload_sha256") != tagged_fingerprint:
            raise RuntimeError(
                f"Tagged answer payload fingerprint mismatch for {qid}"
            )
    if direct_rows is not None:
        direct_prompt = generation.DIRECT_PROMPT.read_text(encoding="utf-8")
        for direct in direct_rows:
            citations = CITATION_PATTERN.findall(direct.get("answer", ""))
            if citations:
                raise RuntimeError(
                    f"Direct {direct['question_id']} contains C citations"
                )
            qid = direct["question_id"]
            direct_user_message = base.render(
                direct_prompt,
                question_text=question_by_qid[qid]["question_text"],
            )
            direct_payload = {
                "model": generation.MODEL,
                "temperature": 0,
                "messages": [
                    {"role": "system", "content": base.SYSTEM_MESSAGE},
                    {"role": "user", "content": direct_user_message},
                ],
            }
            direct_fingerprint = base.payload_sha256(direct_payload)
            if direct.get("answer_execution_sha256") != direct_fingerprint:
                raise RuntimeError(
                    f"Direct answer execution fingerprint mismatch for {qid}"
                )
            if (
                direct.get("answer_prompt_payload_sha256")
                != direct_fingerprint
            ):
                raise RuntimeError(
                    f"Direct answer payload fingerprint mismatch for {qid}"
                )


def load_common_verification(
    expected_qids: list[str],
) -> dict[str, list[dict]]:
    by_qid: dict[str, dict[tuple[str, str], dict]] = {
        qid: {} for qid in expected_qids
    }
    expected = set(expected_qids)
    for path in COMMON_RETRIEVAL_FILES:
        rows = base.read_jsonl(path)
        row_qids = [str(row.get("question_id", "")) for row in rows]
        if len(rows) != len(expected_qids) or set(row_qids) != expected:
            raise RuntimeError(
                f"Common verification retrieval membership mismatch: {path}"
            )
        for row in rows:
            qid = str(row["question_id"])
            for hit in row.get("retrieved_context", []):
                doc_id = str(hit.get("doc_id") or hit.get("citation") or "")
                chunk_id = str(hit.get("chunk_id") or hit.get("chunk") or "")
                text = str(hit.get("text") or "")
                if not doc_id or not chunk_id or not text.strip():
                    raise RuntimeError(
                        f"Incomplete verification chunk identity for {qid}"
                    )
                key = (doc_id, chunk_id)
                candidate = {
                    "source": hit.get("citation") or doc_id,
                    "section": hit.get("section", ""),
                    "text": text,
                }
                existing = by_qid[qid].get(key)
                if existing is not None and existing["text"] != text:
                    raise RuntimeError(
                        f"Conflicting text for verification chunk {qid} {key}"
                    )
                by_qid[qid][key] = candidate

    common: dict[str, list[dict]] = {}
    for qid in expected_qids:
        ordered = [
            value
            for _, value in sorted(
                by_qid[qid].items(),
                key=lambda item: item[0],
            )
        ]
        common[qid] = [
            {"passage_id": f"V{index}", **value}
            for index, value in enumerate(ordered, start=1)
        ]
        if not common[qid]:
            raise RuntimeError(f"No common verification evidence for {qid}")
    return common


def neutral_reference_evidence(row: dict) -> dict:
    fields = (
        "evidence_type",
        "exact_evidence_span",
        "supported_claim",
        "does_not_support",
        "PFAS_compound",
        "matrix",
        "method_or_material",
        "endpoint",
        "numerical_value",
        "unit",
        "protocol_detail",
        "limitation",
        "supports_universal_claim",
    )
    return {field: row.get(field, "") for field in fields}


def build_payloads(
    questions: list[dict],
    gold_by_qid: dict[str, list[dict]],
    common_verification: dict[str, list[dict]],
    tagged_rows: list[dict],
    untagged_rows: list[dict] | None,
    direct_rows: list[dict] | None,
    repeat: int,
) -> tuple[list[dict], list[dict], list[dict]]:
    answers = {
        "tagged": {
            row["question_id"]: normalized_answer_without_citations(
                row["answer"]
            )
            for row in tagged_rows
        },
    }
    comparisons: list[tuple[str, str, str]] = []
    if untagged_rows is not None:
        answers["untagged"] = {
            row["question_id"]: normalized_answer_without_citations(
                row["answer"]
            )
            for row in untagged_rows
        }
        comparisons.append(
            (
                "tagged_vs_matched_untagged",
                "tagged",
                "untagged",
            )
        )
    if direct_rows is not None:
        answers["direct"] = {
            row["question_id"]: normalized_answer_without_citations(
                row["answer"]
            )
            for row in direct_rows
        }
        comparisons.append(
            (
                "tagged_vs_matched_direct",
                "tagged",
                "direct",
            )
        )

    payloads: list[dict] = []
    mappings: list[dict] = []
    normalized_rows: list[dict] = []
    for comparison, left_system, right_system in comparisons:
        for question in questions:
            qid = question["question_id"]
            normalized_rows.extend(
                {
                    "comparison": comparison,
                    "question_id": qid,
                    "system": system,
                    "normalized_answer": answers[system][qid],
                }
                for system in (left_system, right_system)
            )
            first = first_assignment(
                comparison,
                qid,
                left_system,
                right_system,
            )
            for orientation, (system_a, system_b) in enumerate(
                (first, tuple(reversed(first))),
                start=1,
            ):
                payload_id = (
                    f"{comparison}::{qid}::R{repeat}::O{orientation}"
                )
                model_payload = {
                    "question": question["question_text"],
                    "common_scientific_boundaries": (
                        "Preserve compounds, matrices, methods, "
                        "conditions, endpoints, metrics, units, "
                        "comparison bases, and scope."
                    ),
                    "reference_evidence": [
                        neutral_reference_evidence(row)
                        for row in gold_by_qid.get(qid, [])
                    ],
                    "verification_evidence": common_verification[qid],
                    "answer_A": answers[system_a][qid],
                    "answer_B": answers[system_b][qid],
                }
                serialized = json.dumps(
                    model_payload,
                    ensure_ascii=False,
                )
                forbidden = {
                    comparison,
                    qid,
                    "tagged_vs_",
                    "matched_direct",
                    "matched_untagged",
                    '"task_type"',
                    '"answerability_type"',
                    '"payload_id"',
                    '"question_id"',
                }
                leaked = sorted(
                    value for value in forbidden if value in serialized
                )
                if leaked:
                    raise RuntimeError(
                        f"Model-visible judge payload leaks local metadata: {leaked}"
                    )
                if CITATION_PATTERN.search(serialized):
                    raise RuntimeError(
                        f"Model-visible judge payload retains citations for {qid}"
                    )
                payloads.append(
                    {
                        "payload_id": payload_id,
                        "question_id": qid,
                        "model_payload": model_payload,
                    }
                )
                mappings.append(
                    {
                        "payload_id": payload_id,
                        "comparison": comparison,
                        "question_id": qid,
                        "repeat": repeat,
                        "orientation": orientation,
                        "left_system": left_system,
                        "right_system": right_system,
                        "system_A": system_a,
                        "system_B": system_b,
                    }
                )
    return payloads, mappings, normalized_rows


def parse_judge_result(
    mapping: dict,
    result: dict,
) -> dict:
    if "parse_error" in result:
        raise RuntimeError(
            f"Judge parse failure for {mapping['payload_id']}: "
            f"{result['parse_error']}"
        )
    preferences = result.get("criterion_preferences")
    rationales = result.get("criterion_rationales")
    if not isinstance(preferences, dict):
        raise RuntimeError(
            f"Missing criterion_preferences for {mapping['payload_id']}"
        )
    if not isinstance(rationales, dict):
        raise RuntimeError(
            f"Missing criterion_rationales for {mapping['payload_id']}"
        )
    schema_repairs: list[str] = []
    confidence = str(result.get("confidence", "")).strip().lower()
    if confidence not in {"low", "medium", "high"}:
        schema_repairs.append(f"confidence={confidence!r}->unspecified")
        confidence = "unspecified"
    material_errors: dict[str, list] = {}
    for field in ("material_errors_A", "material_errors_B"):
        value = result.get(field)
        if not isinstance(value, list):
            schema_repairs.append(f"{field}->[]")
            value = []
        material_errors[field] = value

    row = {
        **mapping,
        "confidence": confidence,
        "schema_repair_count": len(schema_repairs),
        "schema_repairs": "; ".join(schema_repairs),
        "material_errors_A": json.dumps(
            material_errors["material_errors_A"],
            ensure_ascii=False,
        ),
        "material_errors_B": json.dumps(
            material_errors["material_errors_B"],
            ensure_ascii=False,
        ),
    }
    for criterion in CRITERIA:
        if criterion not in preferences:
            raise RuntimeError(
                f"Missing {criterion} for {mapping['payload_id']}"
            )
        preference = str(preferences[criterion]).strip().lower()
        if preference == "tie":
            tagged_point = 0.5
        elif preference in {"a", "b"}:
            preferred_system = mapping[f"system_{preference.upper()}"]
            tagged_point = 1.0 if preferred_system == "tagged" else 0.0
        else:
            raise RuntimeError(
                f"Unexpected preference {preference!r} for "
                f"{mapping['payload_id']} {criterion}"
            )
        rationale = rationales.get(criterion)
        if not isinstance(rationale, str) or not rationale.strip():
            raise RuntimeError(
                f"Missing rationale for {criterion} in "
                f"{mapping['payload_id']}"
            )
        row[f"{criterion}_tagged_point"] = tagged_point
        row[f"{criterion}_rationale"] = rationale.strip()
    return row


def run_judges(
    questions: list[dict],
    tagged_rows: list[dict],
    untagged_rows: list[dict] | None,
    direct_rows: list[dict] | None,
    repeats: int,
    workers: int,
    resume: bool,
) -> tuple[list[dict], list[dict]]:
    if OUT is None:
        raise RuntimeError("Output directory has not been configured")
    gold_by_qid = base.group_gold(base.read_jsonl(GOLD))
    ordered_qids = [row["question_id"] for row in questions]
    question_qids = set(ordered_qids)
    if not question_qids.issubset(gold_by_qid):
        missing = sorted(question_qids - set(gold_by_qid))
        raise RuntimeError(
            f"Dev13 gold membership mismatch; missing={missing}"
        )
    gold_by_qid = {qid: gold_by_qid[qid] for qid in question_qids}
    if any(not rows for rows in gold_by_qid.values()):
        raise RuntimeError("Every Dev13 question must have at least one gold row")
    common_verification = load_common_verification(ordered_qids)
    all_parsed: list[dict] = []
    token_rows: list[dict] = []

    for repeat in range(1, repeats + 1):
        run_dir = OUT / f"judge/run{repeat}"
        payloads, mappings, normalized = build_payloads(
            questions,
            gold_by_qid,
            common_verification,
            tagged_rows,
            untagged_rows,
            direct_rows,
            repeat,
        )
        base.write_jsonl(
            run_dir / "normalized_answers.jsonl",
            normalized,
        )
        base.write_jsonl(
            run_dir / "model_payloads.jsonl",
            [row["model_payload"] for row in payloads],
        )
        base.write_jsonl(
            run_dir / "local_request_envelopes.jsonl",
            payloads,
        )
        base.write_jsonl(run_dir / "blind_mapping.jsonl", mappings)
        raw = base.call_json_judge(
            payloads,
            JUDGE_PROMPT.read_text(encoding="utf-8"),
            MODEL,
            run_dir / "judge_results.jsonl",
            workers,
            (
                "Dev13 V3 neutral-evidence blinded judge "
                f"repeat {repeat}"
            ),
            resume=resume,
        )
        raw_by_id = {row["payload_id"]: row for row in raw}
        parsed: list[dict] = []
        for mapping in mappings:
            result = raw_by_id[mapping["payload_id"]]["judge_result"]
            parsed.append(parse_judge_result(mapping, result))
        base.write_csv(run_dir / "orientation_level.csv", parsed)
        all_parsed.extend(parsed)
        token_rows.append(
            base.token_row(
                "neutral_evidence_pairwise_content_judge",
                f"repeat_{repeat}",
                raw,
                "judge",
                (
                    "Non-exhaustive reference evidence plus a deduplicated "
                    "Hybrid/BGE/BGE-LLM verification union; citations and "
                    "local identifiers removed."
                ),
            )
        )

    base.write_csv(OUT / "tokens/judge.csv", token_rows)
    return all_parsed, token_rows


def aggregate(
    parsed: list[dict],
    repeats: int,
) -> tuple[list[dict], list[dict]]:
    if OUT is None:
        raise RuntimeError("Output directory has not been configured")
    grouped: dict[tuple[str, str], list[dict]] = defaultdict(list)
    mirrored: dict[tuple[str, str, int], list[dict]] = defaultdict(list)
    for row in parsed:
        key = (row["comparison"], row["question_id"])
        grouped[key].append(row)
        mirrored[
            (
                row["comparison"],
                row["question_id"],
                int(row["repeat"]),
            )
        ].append(row)

    per_question: list[dict] = []
    for (comparison, qid), rows in sorted(grouped.items()):
        expected = repeats * 2
        if len(rows) != expected:
            raise RuntimeError(
                f"Expected {expected} judgments for {qid}; "
                f"found {len(rows)}"
            )
        criterion_scores = {
            criterion: mean(
                float(row[f"{criterion}_tagged_point"])
                for row in rows
            )
            for criterion in CRITERIA
        }
        weighted_score = sum(
            WEIGHTS[criterion] * criterion_scores[criterion]
            for criterion in CRITERIA
        )
        winner = (
            "tagged"
            if weighted_score > 0.5
            else rows[0]["right_system"]
            if weighted_score < 0.5
            else "tie"
        )
        per_question.append(
            {
                "comparison": comparison,
                "question_id": qid,
                "left_system": "tagged",
                "right_system": rows[0]["right_system"],
                **{
                    f"{criterion}_tagged_score": (
                        criterion_scores[criterion]
                    )
                    for criterion in CRITERIA
                },
                "weighted_tagged_score": weighted_score,
                "winner": winner,
                "tagged_advantage": weighted_score - 0.5,
            }
        )

    summaries: list[dict] = []
    for comparison in sorted(
        {row["comparison"] for row in per_question}
    ):
        rows = [
            row
            for row in per_question
            if row["comparison"] == comparison
        ]
        opponent = rows[0]["right_system"]
        agreements: list[bool] = []
        for (
            mirror_comparison,
            _,
            _,
        ), orientation_rows in mirrored.items():
            if mirror_comparison != comparison:
                continue
            if len(orientation_rows) != 2:
                raise RuntimeError(
                    "Expected two mirrored orientation rows"
                )
            for criterion in CRITERIA:
                agreements.append(
                    float(
                        orientation_rows[0][
                            f"{criterion}_tagged_point"
                        ]
                    )
                    == float(
                        orientation_rows[1][
                            f"{criterion}_tagged_point"
                        ]
                    )
                )
        summaries.append(
            {
                "comparison": comparison,
                "question_count": len(rows),
                "judge_repeats": repeats,
                "tagged_wins": sum(
                    row["winner"] == "tagged" for row in rows
                ),
                "opponent": opponent,
                "opponent_wins": sum(
                    row["winner"] == opponent for row in rows
                ),
                "ties": sum(row["winner"] == "tie" for row in rows),
                "mean_weighted_tagged_score": mean(
                    float(row["weighted_tagged_score"])
                    for row in rows
                ),
                "mean_tagged_advantage": mean(
                    float(row["tagged_advantage"]) for row in rows
                ),
                "mirrored_criterion_agreement": (
                    sum(agreements) / len(agreements)
                ),
                **{
                    f"mean_{criterion}_tagged_score": mean(
                        float(row[f"{criterion}_tagged_score"])
                        for row in rows
                    )
                    for criterion in CRITERIA
                },
            }
        )

    base.write_csv(OUT / "results/per_question.csv", per_question)
    base.write_csv(OUT / "results/summary.csv", summaries)
    return per_question, summaries


def write_manifest(
    summaries: list[dict],
    token_rows: list[dict],
    repeats: int,
    direct_included: bool,
    untagged_included: bool,
    resume: bool,
    schema_repair_count: int,
    schema_repaired_response_count: int,
) -> None:
    if OUT is None:
        raise RuntimeError("Output directory has not been configured")
    prompt_tokens = sum(
        int(row["prompt_tokens_total"]) for row in token_rows
    )
    completion_tokens = sum(
        int(row["completion_tokens_total"]) for row in token_rows
    )
    inputs = [
        QUESTIONS,
        GOLD,
        TAGGED,
        JUDGE_PROMPT,
        *COMMON_RETRIEVAL_FILES,
    ]
    if untagged_included:
        inputs.append(UNTAGGED)
    if direct_included:
        inputs.append(DIRECT)
    manifest = {
        "status": "completed_dev13_neutral_evidence_evaluation",
        "protocol": (
            "benchmark/frozen_v3/methods/"
            "dev13_neutral_evidence_judge_v3_protocol.json"
        ),
        "source_run": base.project_relative(SOURCE_RUN),
        "judge_model_requested": MODEL,
        "judge_models_returned": sorted(
            {
                row.get("model", "")
                for row in token_rows
                if row.get("model")
            }
        ),
        "temperature": 0,
        "judge_temperature_zero_resamples": repeats,
        "resume_enabled": resume,
        "mirrored_answer_order": True,
        "model_payload_contains_local_identifiers": False,
        "model_payload_contains_task_labels": False,
        "citations_retained": False,
        "verification_context_included": True,
        "verification_context_source": (
            "Deduplicated union of frozen Hybrid, BGE, and BGE-LLM top-10 "
            "contexts, sorted by document and chunk identity."
        ),
        "citation_quality_scored": False,
        "verification_context_use": (
            "Scientific correctness verification only; model-visible answers "
            "contain no citation markers."
        ),
        "gold_available_to_judge": True,
        "gold_interpretation": (
            "Non-exhaustive reference evidence; absence is not treated as "
            "evidence that a claim is false."
        ),
        "weights": WEIGHTS,
        "non_scoring_judge_schema_repairs": schema_repair_count,
        "responses_with_non_scoring_schema_repairs": (
            schema_repaired_response_count
        ),
        "schema_repair_policy": (
            "Missing or invalid auxiliary confidence/material-error fields "
            "are recorded and normalized; every scored criterion preference "
            "and rationale remains mandatory."
        ),
        "input_files": {
            base.project_relative(path): base.sha256(path)
            for path in inputs
        },
        "direct_comparison_included": direct_included,
        "untagged_comparison_included": untagged_included,
        "summaries": summaries,
        "judge_token_accounting": {
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
    (OUT / "evaluation_manifest.json").parent.mkdir(
        parents=True,
        exist_ok=True,
    )
    (OUT / "evaluation_manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    global OUT
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=9)
    parser.add_argument("--repeats", type=int, default=3)
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
            "Reuse only judgments whose model, prompt, and payload "
            "fingerprint match the current frozen execution."
        ),
    )
    parser.add_argument(
        "--include-untagged",
        action="store_true",
        help="Also compare against the historical untagged diagnostic.",
    )
    parser.add_argument(
        "--include-direct",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Compare against matched Direct (default: true).",
    )
    args = parser.parse_args()
    if args.repeats < 1:
        raise RuntimeError("--repeats must be at least 1")
    if not args.include_direct and not args.include_untagged:
        raise RuntimeError("At least one comparison must be enabled")
    OUT = base.prepare_output_dir(args.out, resume=args.resume)

    load_dotenv(ROOT / ".env", override=False)
    questions = base.read_csv(QUESTIONS)
    tagged_rows = base.read_jsonl(TAGGED)
    untagged_rows = (
        base.read_jsonl(UNTAGGED) if args.include_untagged else None
    )
    direct_rows = (
        base.read_jsonl(DIRECT) if args.include_direct else None
    )
    if len(questions) != 13:
        raise RuntimeError(f"Expected 13 questions; found {len(questions)}")
    validate_inputs(
        questions,
        tagged_rows,
        untagged_rows,
        direct_rows,
    )
    parsed, token_rows = run_judges(
        questions,
        tagged_rows,
        untagged_rows,
        direct_rows,
        args.repeats,
        args.workers,
        args.resume,
    )
    _, summaries = aggregate(parsed, args.repeats)
    write_manifest(
        summaries,
        token_rows,
        args.repeats,
        direct_included=direct_rows is not None,
        untagged_included=untagged_rows is not None,
        resume=args.resume,
        schema_repair_count=sum(
            int(row.get("schema_repair_count", 0)) for row in parsed
        ),
        schema_repaired_response_count=sum(
            int(row.get("schema_repair_count", 0)) > 0 for row in parsed
        ),
    )
    print(
        f"Wrote neutral-evidence Dev13 evaluation to {OUT}",
        flush=True,
    )


if __name__ == "__main__":
    main()

from __future__ import annotations

import csv
import importlib.util
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
V3 = ROOT / "benchmark/frozen_v3"
TAG_PROMPT = V3 / "prompts/evaluation/soft_eligibility_tagger_v3.txt"
ANSWER_PROMPT = (
    V3 / "prompts/evaluation/rag_answer_prompt_soft_tags_v3.txt"
)
DIRECT_PROMPT = (
    V3 / "prompts/evaluation/direct_answer_prompt_matched_v3.txt"
)
JUDGE_PROMPT = (
    V3
    / "prompts/evaluation/neutral_evidence_pairwise_content_v3.txt"
)
RUNNER = V3 / "scripts/run_dev13_soft_tags_v3.py"
DEV_QUESTIONS = V3 / "input/questions_dev13.csv"
sys.path.insert(0, str(V3 / "scripts"))

EXPECTED_POLICIES = {
    "use_full_claim",
    "category_only",
    "limitation_only",
    "qualitative_relationship",
    "quantitative_detail",
    "procedural_detail",
    "do_not_use",
}
EXPECTED_LABELS = {
    "direct_evidence",
    "background",
    "nearby_but_mismatched",
    "irrelevant",
}
REQUIRED_OPERATIONS = {
    "extraction",
    "comparison",
    "classification",
    "explanation",
    "synthesis",
    "claim assessment",
    "limitations",
    "recommendation",
}
REQUIRED_DIMENSIONS = {
    "subject",
    "method",
    "matrix",
    "study design",
    "outcome",
    "metric",
    "unit",
    "conditions",
    "system boundary",
    "generality",
}
SUPERSEDED_MARKERS = {
    "For numeric questions",
    "For protocol questions",
    "activated-carbon",
    "supercritical water oxidation",
    "250--500 words",
    "numeric_required",
    "protocol_required",
    "identity_only",
    "qualitative_only",
    "nearby_metric",
}
FORBIDDEN_FREE_TEXT_FIELDS = {
    "allowed_use",
    "avoid_use",
    "omit_details",
}


def load_runner():
    spec = importlib.util.spec_from_file_location("v3_runner", RUNNER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not import {RUNNER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    tag_prompt = TAG_PROMPT.read_text(encoding="utf-8")
    answer_prompt = ANSWER_PROMPT.read_text(encoding="utf-8")
    direct_prompt = DIRECT_PROMPT.read_text(encoding="utf-8")
    judge_prompt = JUDGE_PROMPT.read_text(encoding="utf-8")
    combined = tag_prompt + "\n" + answer_prompt + "\n" + direct_prompt
    lower = re.sub(r"\s+", " ", combined.lower())
    errors: list[str] = []

    with DEV_QUESTIONS.open(
        newline="",
        encoding="utf-8-sig",
    ) as handle:
        questions = list(csv.DictReader(handle))
    for row in questions:
        qid = row["question_id"].strip()
        text = row["question_text"].strip()
        if qid and re.search(rf"\b{re.escape(qid)}\b", combined):
            errors.append(f"prompt contains development question ID {qid}")
        if text and text in combined:
            errors.append(
                f"prompt contains exact development question text {qid}"
            )

    for operation in EXPECTED_POLICIES:
        if operation not in tag_prompt:
            errors.append(f"tag prompt missing policy {operation}")
    for operation in REQUIRED_OPERATIONS:
        if operation not in lower:
            errors.append(f"prompt missing research operation {operation}")
    for dimension in REQUIRED_DIMENSIONS:
        if dimension not in lower:
            errors.append(f"prompt missing compatibility dimension {dimension}")
    for marker in SUPERSEDED_MARKERS:
        if marker in combined:
            errors.append(f"prompt retains superseded marker {marker!r}")

    for prompt_name, prompt_text in (
        ("RAG", answer_prompt),
        ("Direct", direct_prompt),
    ):
        prompt_lower = re.sub(r"\s+", " ", prompt_text.lower())
        for operation in REQUIRED_OPERATIONS:
            if operation not in prompt_lower:
                errors.append(
                    f"{prompt_name} prompt missing operation {operation}"
                )
        for dimension in REQUIRED_DIMENSIONS:
            if dimension not in prompt_lower:
                errors.append(
                    f"{prompt_name} prompt missing dimension {dimension}"
                )
        for heading in (
            "1. Answerability",
            "2. Answer",
            "3. Uncertainty and limitations",
            "4. Practical takeaway",
        ):
            if heading not in prompt_text:
                errors.append(
                    f"{prompt_name} prompt missing output heading {heading}"
                )
    if "{question_text}" not in direct_prompt:
        errors.append("Direct prompt missing question placeholder")
    if "{retrieved_context}" in direct_prompt:
        errors.append("Direct prompt must not accept retrieved context")
    if "[C#]" in direct_prompt:
        errors.append("Direct prompt must not request source citations")
    if "without access to retrieved" not in direct_prompt.lower():
        errors.append("Direct information condition is not explicit")
    for forbidden in (
        "human-audited",
        "authoritative",
        "task_type",
        "answerability_type",
        "payload_id",
        "question_id",
    ):
        if forbidden in judge_prompt:
            errors.append(
                f"neutral judge prompt contains forbidden marker {forbidden!r}"
            )
    for required in (
        "non-exhaustive reference evidence",
        "deduplicated union",
        "citation markers removed",
    ):
        if required not in judge_prompt:
            errors.append(
                f"neutral judge prompt missing contract {required!r}"
            )

    runner = load_runner()
    if runner.VALID_LABELS != EXPECTED_LABELS:
        errors.append("runner evidence-role schema does not match tag prompt")
    if runner.VALID_DETAIL_POLICIES != EXPECTED_POLICIES:
        errors.append("runner policy schema does not match tag prompt")
    for field in FORBIDDEN_FREE_TEXT_FIELDS:
        if field in tag_prompt:
            errors.append(
                f"tag prompt still requests free-text field {field}"
            )

    components, component_errors = runner.validate_question_components(
        {
            "question_components": [
                {
                    "component_id": "R1",
                    "description": "Neutral information need.",
                }
            ]
        }
    )
    candidates = [
        {"text": f"Verbatim support {index}."}
        for index in range(1, len(EXPECTED_POLICIES) + 1)
    ]
    raw = {
        "chunk_tags": [
            {
                "candidate_id": index,
                "eligibility": "direct_evidence",
                "detail_policy": policy,
                "supports_components": ["R1"],
                "evidence_polarity": "support",
                "exact_support": f"Verbatim support {index}.",
                "confidence": 1.0,
            }
            for index, policy in enumerate(
                sorted(EXPECTED_POLICIES),
                start=1,
            )
        ]
    }
    tags, tag_errors = runner.validate_tags(
        raw,
        candidates,
        {row["component_id"] for row in components},
    )
    if component_errors or tag_errors:
        errors.append(
            "valid synthetic component/tag schema produced validation errors"
        )
    if {row["detail_policy"] for row in tags} != EXPECTED_POLICIES:
        errors.append("not every general detail policy survives validation")

    leak_texts = {
        "component": "LEAKED EXPECTED CONCLUSION",
        "allowed": "LEAKED ALLOWED USE",
        "avoid": "LEAKED AVOID USE",
        "omit": "LEAKED OMIT DETAIL",
    }
    leak_candidates = [{"text": "The source contains only this sentence."}]
    leak_tags, _ = runner.validate_tags(
        {
            "chunk_tags": [
                {
                    "candidate_id": 1,
                    "eligibility": "direct_evidence",
                    "detail_policy": "use_full_claim",
                    "supports_components": ["R1"],
                    "allowed_use": leak_texts["allowed"],
                    "avoid_use": leak_texts["avoid"],
                    "omit_details": [leak_texts["omit"]],
                    "evidence_polarity": "support",
                    "exact_support": "FABRICATED VERBATIM EXCERPT",
                    "confidence": 1.0,
                }
            ]
        },
        leak_candidates,
        {"R1"},
    )
    leak_context = runner.format_tagged_context(
        leak_candidates,
        {
            "question_components": [
                {
                    "component_id": "R1",
                    "description": leak_texts["component"],
                }
            ],
            "validated_chunk_tags": leak_tags,
        },
    )
    for label, leaked_text in leak_texts.items():
        if leaked_text in leak_context:
            errors.append(
                f"answer-facing context leaks {label} free text"
            )
    if "FABRICATED VERBATIM EXCERPT" in leak_context:
        errors.append("non-verbatim exact_support reached answer context")
    if any(
        field in leak_tags[0] for field in FORBIDDEN_FREE_TEXT_FIELDS
    ):
        errors.append("validated tag retains forbidden free-text fields")

    if errors:
        raise SystemExit("TASK-GENERAL PROMPT VALIDATION FAIL\n" + "\n".join(errors))
    print("TASK-GENERAL PROMPT VALIDATION PASS")
    print(f"Research operations checked: {len(REQUIRED_OPERATIONS)}")
    print(f"Compatibility dimensions checked: {len(REQUIRED_DIMENSIONS)}")
    print(f"Detail policies checked: {len(EXPECTED_POLICIES)}")
    print(f"Evidence roles checked: {len(EXPECTED_LABELS)}")
    print("RAG and Direct shared operation/dimension vocabulary checked.")
    print("Neutral judge wording and hidden-metadata contract checked.")
    print("Unverified soft-tag prose is absent from answer-facing context.")
    print("No development question ID or exact question text appears in prompts.")


if __name__ == "__main__":
    main()

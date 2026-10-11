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
SOURCE_RUN = V3 / "results/dev13_soft_tags_v3_confirmation_2026-07-26"
OUT: Path | None = None

QUESTIONS = V3 / "input/questions_dev13.csv"
GOLD = V3 / "gold/chunk_based_gold.jsonl"
TAGGED = SOURCE_RUN / "answers/tagged_rag_gpt51.jsonl"
UNTAGGED = SOURCE_RUN / "answers/matched_untagged_rag_gpt51.jsonl"
DIRECT = SOURCE_RUN / "answers/matched_direct_gpt51.jsonl"
JUDGE_PROMPT = (
    V3 / "prompts/evaluation/citation_blind_pairwise_content_v1.txt"
)

MODEL = "gpt-5.1"
JUDGE_REPEATS = (1, 2, 3)
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
HEADING_PATTERN = re.compile(
    r"(?im)^\s*(?:#{1,6}\s*)?(?:\d+\.\s*)?\**"
    r"(Answerability|Answer|Uncertainty and limitations|"
    r"Practical takeaway)"
    r"\**\s*:?\s*$"
)
CITATION_PATTERN = re.compile(
    r"\s*\[(?:C\d+)(?:\s*,\s*C\d+)*\]",
    flags=re.IGNORECASE,
)

import runtime_helpers as base


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
        sections[match.group(1).lower()] = answer[start:end].strip()
    return sections


def normalize_answer(answer: str) -> str:
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


def first_assignment(
    comparison: str,
    qid: str,
    left_system: str,
    right_system: str,
) -> tuple[str, str]:
    digest = hashlib.sha256(
        f"soft-tags-v3::{comparison}::{qid}::citation-blind".encode()
    ).digest()
    return (
        (left_system, right_system)
        if digest[0] % 2 == 0
        else (right_system, left_system)
    )


def build_payloads(
    questions: list[dict],
    gold_by_qid: dict[str, list[dict]],
    tagged_rows: list[dict],
    untagged_rows: list[dict],
    direct_rows: list[dict] | None,
    repeat: int,
) -> tuple[list[dict], list[dict], list[dict]]:
    answers = {
        "tagged": {
            row["question_id"]: normalize_answer(row["answer"])
            for row in tagged_rows
        },
        "untagged": {
            row["question_id"]: normalize_answer(row["answer"])
            for row in untagged_rows
        },
    }
    comparisons = [
        (
            "tagged_vs_matched_untagged",
            "tagged",
            "untagged",
        )
    ]
    if direct_rows is not None:
        answers["direct"] = {
            row["question_id"]: normalize_answer(row["answer"])
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
                payloads.append(
                    {
                        "payload_id": payload_id,
                        "question_id": qid,
                        "question": question["question_text"],
                        "task_boundaries": {
                            "task_type": question.get("task_type", ""),
                            "answerability_type": question.get(
                                "answerability_type",
                                "",
                            ),
                            "common_scientific_boundaries": (
                                "Do not invent study-specific details, "
                                "values, methods, conditions, protocols, "
                                "compounds, matrices, or units. Preserve "
                                "outcome and metric distinctions, answer all "
                                "material parts, and state uncertainty."
                            ),
                        },
                        "gold_evidence": [
                            base.compact_gold(row)
                            for row in gold_by_qid.get(qid, [])
                        ],
                        "answer_A": answers[system_a][qid],
                        "answer_B": answers[system_b][qid],
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


def run_judges(
    questions: list[dict],
    tagged_rows: list[dict],
    untagged_rows: list[dict],
    direct_rows: list[dict] | None,
    workers: int,
) -> tuple[list[dict], list[dict]]:
    gold_by_qid = base.group_gold(base.read_jsonl(GOLD))
    all_parsed: list[dict] = []
    token_rows: list[dict] = []

    for repeat in JUDGE_REPEATS:
        run_dir = OUT / f"judge/run{repeat}"
        payloads, mappings, normalized = build_payloads(
            questions,
            gold_by_qid,
            tagged_rows,
            untagged_rows,
            direct_rows,
            repeat,
        )
        base.write_jsonl(run_dir / "normalized_answers.jsonl", normalized)
        base.write_jsonl(run_dir / "blind_payloads.jsonl", payloads)
        base.write_jsonl(run_dir / "blind_mapping.jsonl", mappings)
        raw = base.call_json_judge(
            payloads,
            JUDGE_PROMPT.read_text(encoding="utf-8"),
            MODEL,
            run_dir / "judge_results.jsonl",
            workers,
            f"Dev13 V3 citation-blind judge repeat {repeat}",
        )
        raw_by_id = {row["payload_id"]: row for row in raw}
        parsed: list[dict] = []
        for mapping in mappings:
            result = raw_by_id[mapping["payload_id"]]["judge_result"]
            preferences = result.get("criterion_preferences", {})
            row = {
                **mapping,
                "confidence": result.get("confidence", ""),
            }
            for criterion in CRITERIA:
                preference = str(
                    preferences.get(criterion, "tie")
                ).lower()
                if preference == "tie":
                    tagged_point = 0.5
                elif preference in {"a", "b"}:
                    preferred_system = mapping[
                        f"system_{preference.upper()}"
                    ]
                    tagged_point = (
                        1.0 if preferred_system == "tagged" else 0.0
                    )
                else:
                    raise RuntimeError(
                        f"Unexpected preference {preference!r} for "
                        f"{mapping['payload_id']} {criterion}"
                    )
                row[f"{criterion}_tagged_point"] = tagged_point
                row[f"{criterion}_rationale"] = result.get(
                    "criterion_rationales",
                    {},
                ).get(criterion, "")
            parsed.append(row)
        base.write_csv(run_dir / "orientation_level.csv", parsed)
        all_parsed.extend(parsed)
        token_rows.append(
            base.token_row(
                "citation_blind_pairwise_judge",
                f"repeat_{repeat}",
                raw,
                "judge",
                (
                    "One primary comparison plus an optional Direct "
                    "comparison; two mirrored orientations per question."
                ),
            )
        )

    base.write_csv(OUT / "tokens/judge.csv", token_rows)
    return all_parsed, token_rows


def aggregate(
    parsed: list[dict],
) -> tuple[list[dict], list[dict], dict[str, float]]:
    grouped: dict[tuple[str, str], list[dict]] = defaultdict(list)
    mirrored: dict[tuple[str, str, int], list[dict]] = defaultdict(list)
    for row in parsed:
        comparison = row["comparison"]
        qid = row["question_id"]
        grouped[(comparison, qid)].append(row)
        mirrored[(comparison, qid, int(row["repeat"]))].append(row)

    per_question: list[dict] = []
    for (comparison, qid), rows in sorted(grouped.items()):
        if len(rows) != 6:
            raise RuntimeError(
                f"Expected six judgments for {qid}; found {len(rows)}"
            )
        criterion_scores = {
            criterion: mean(
                float(row[f"{criterion}_tagged_point"]) for row in rows
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
                    f"{criterion}_tagged_score": criterion_scores[criterion]
                    for criterion in CRITERIA
                },
                "weighted_tagged_score": weighted_score,
                "winner": winner,
                "tagged_advantage": weighted_score - 0.5,
            }
        )

    summaries: list[dict] = []
    mirror_agreements: dict[str, float] = {}
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
        mirror_agreement = (
            sum(agreements) / len(agreements) if agreements else 0.0
        )
        mirror_agreements[comparison] = mirror_agreement
        summaries.append(
            {
                "comparison": comparison,
                "question_count": len(rows),
                "tagged_wins": sum(
                    row["winner"] == "tagged" for row in rows
                ),
                "opponent": opponent,
                "opponent_wins": sum(
                    row["winner"] == opponent for row in rows
                ),
                "ties": sum(row["winner"] == "tie" for row in rows),
                "mean_weighted_tagged_score": mean(
                    float(row["weighted_tagged_score"]) for row in rows
                ),
                "mean_tagged_advantage": mean(
                    float(row["tagged_advantage"]) for row in rows
                ),
                "mirrored_criterion_agreement": mirror_agreement,
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
    return per_question, summaries, mirror_agreements


def write_evaluation_manifest(
    token_rows: list[dict],
    summaries: list[dict],
    direct_included: bool,
) -> None:
    prompt_tokens = sum(
        int(row["prompt_tokens_total"]) for row in token_rows
    )
    completion_tokens = sum(
        int(row["completion_tokens_total"]) for row in token_rows
    )
    manifest = {
        "status": "completed_dev_only",
        "protocol": (
            "benchmark/frozen_v3/methods/"
            "dev13_soft_tags_v3_protocol.json"
        ),
        "judge_model_requested": MODEL,
        "judge_models_returned": sorted(
            {row.get("model", "") for row in token_rows if row.get("model")}
        ),
        "temperature": 0,
        "judge_repeats": len(JUDGE_REPEATS),
        "mirrored_answer_order": True,
        "citation_blind": True,
        "gold_available_to_judge": True,
        "weights": WEIGHTS,
        "input_files": {
            base.project_relative(path): base.sha256(path)
            for path in (
                QUESTIONS,
                GOLD,
                TAGGED,
                UNTAGGED,
                *([DIRECT] if direct_included else []),
                JUDGE_PROMPT,
            )
        },
        "direct_comparison_included": direct_included,
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
    (OUT / "evaluation_manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    global OUT
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=9)
    parser.add_argument(
        "--out",
        required=True,
        help="New output directory; existing non-empty directories are refused.",
    )
    parser.add_argument(
        "--include-direct",
        action="store_true",
        help="Also judge tagged RAG against the matched Direct control.",
    )
    args = parser.parse_args()

    load_dotenv(ROOT / ".env", override=False)
    OUT = base.prepare_output_dir(args.out, resume=False)
    questions = base.read_csv(QUESTIONS)
    tagged_rows = base.read_jsonl(TAGGED)
    untagged_rows = base.read_jsonl(UNTAGGED)
    direct_rows = (
        base.read_jsonl(DIRECT) if args.include_direct else None
    )
    if len(questions) != 13:
        raise RuntimeError(f"Expected 13 questions; found {len(questions)}")
    if len(tagged_rows) != 13 or len(untagged_rows) != 13:
        raise RuntimeError(
            "Run run_dev13_soft_tags_v3.py before the judge."
        )
    if direct_rows is not None and len(direct_rows) != 13:
        raise RuntimeError(
            "Run run_dev13_soft_tags_v3.py --include-direct before "
            "requesting the Direct judge comparison."
        )
    parsed, token_rows = run_judges(
        questions,
        tagged_rows,
        untagged_rows,
        direct_rows,
        args.workers,
    )
    _, summaries, _ = aggregate(parsed)
    write_evaluation_manifest(
        token_rows,
        summaries,
        direct_included=direct_rows is not None,
    )
    print(f"Wrote V3 Dev13 evaluation outputs to {OUT}", flush=True)


if __name__ == "__main__":
    main()

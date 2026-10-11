from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
import sys
import time
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
from typing import Any

import numpy as np
from dotenv import load_dotenv
from scipy.optimize import minimize
from scipy.stats import binomtest


EXPERIMENT = Path(__file__).resolve().parents[1]
JUDGE = EXPERIMENT.parents[1]
V3 = JUDGE.parent
ROOT = V3.parents[1]
SOURCE = (
    EXPERIMENT
    / "results/dev13_common_tagger_gpt51_2026-07-26"
)
QUESTIONS = V3 / "input/questions_dev13.csv"
GOLD = V3 / "gold/chunk_based_gold.jsonl"
PROMPT = EXPERIMENT / "prompts/adaptive_pairwise_davidson_judge_v1.txt"
SYSTEMS = ("hybrid", "bge", "bge_llm")
MODEL = "gpt-5.1"
CITATION = re.compile(r"\[C\d+\]", re.IGNORECASE)

sys.path.insert(0, str(V3 / "scripts"))
import runtime_helpers as base  # noqa: E402


def read_answers() -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    for system in SYSTEMS:
        path = SOURCE / system / "answers/tagged_rag_gpt51.jsonl"
        rows = base.read_jsonl(path)
        if len(rows) != 13:
            raise RuntimeError(f"Expected 13 answers in {path}")
        result[system] = {
            str(row["question_id"]): CITATION.sub("", str(row["answer"]))
            for row in rows
        }
    return result


def load_verification(qids: list[str]) -> dict[str, list[dict[str, str]]]:
    merged: dict[str, dict[tuple[str, str], dict[str, str]]] = {
        qid: {} for qid in qids
    }
    for system in SYSTEMS:
        rows = base.read_jsonl(
            SOURCE / system / "answers/tagged_rag_gpt51.jsonl"
        )
        for row in rows:
            qid = str(row["question_id"])
            for chunk in row["retrieved_context"]:
                key = (str(chunk["doc_id"]), str(chunk["chunk_id"]))
                value = {
                    "source": str(chunk.get("citation") or chunk["doc_id"]),
                    "section": str(chunk.get("section", "")),
                    "text": str(chunk["text"]),
                }
                old = merged[qid].get(key)
                if old is not None and old["text"] != value["text"]:
                    raise RuntimeError(f"Conflicting chunk text: {qid} {key}")
                merged[qid][key] = value
    return {
        qid: [
            {"passage_id": f"V{i}", **value}
            for i, (_, value) in enumerate(
                sorted(chunks.items()), start=1
            )
        ]
        for qid, chunks in merged.items()
    }


def compact_gold(row: dict[str, Any]) -> dict[str, Any]:
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


def first_order(qid: str, left: str, right: str) -> tuple[str, str]:
    digest = hashlib.sha256(
        f"layer1-davidson-v1::{qid}::{left}::{right}".encode()
    ).digest()
    return (left, right) if digest[0] % 2 == 0 else (right, left)


def build_calls(
    questions: list[dict[str, str]],
    answers: dict[str, dict[str, str]],
    verification: dict[str, list[dict[str, str]]],
    gold: dict[str, list[dict[str, Any]]],
    *,
    round_number: int,
    selected: set[tuple[str, str, str]] | None = None,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    payloads: list[dict[str, Any]] = []
    mappings: list[dict[str, Any]] = []
    for question in questions:
        qid = str(question["question_id"])
        for left, right in combinations(SYSTEMS, 2):
            unit = (qid, left, right)
            if selected is not None and unit not in selected:
                continue
            initial = first_order(qid, left, right)
            if round_number == 2:
                initial = tuple(reversed(initial))
            for orientation, (system_a, system_b) in enumerate(
                (initial, tuple(reversed(initial))), start=1
            ):
                payload_id = (
                    f"{qid}::{left}_vs_{right}::R{round_number}::O{orientation}"
                )
                visible = {
                    "question": question["question_text"],
                    "reference_evidence": [
                        compact_gold(row) for row in gold[qid]
                    ],
                    "verification_evidence": verification[qid],
                    "answer_A": answers[system_a][qid],
                    "answer_B": answers[system_b][qid],
                }
                serialized = json.dumps(visible, ensure_ascii=False)
                # PFAS prose can legitimately contain words such as "hybrid".
                # Check local metadata keys rather than ambiguous text values.
                forbidden = ("question_id", "system_A", "system_B")
                if any(value in serialized for value in forbidden):
                    raise RuntimeError(
                        f"Local metadata leaked into payload {payload_id}"
                    )
                if CITATION.search(serialized):
                    raise RuntimeError(
                        f"Citation marker leaked into payload {payload_id}"
                    )
                payloads.append(
                    {
                        "payload_id": payload_id,
                        "question_id": qid,
                        "model_payload": visible,
                    }
                )
                mappings.append(
                    {
                        "payload_id": payload_id,
                        "question_id": qid,
                        "left_system": left,
                        "right_system": right,
                        "round": round_number,
                        "orientation": orientation,
                        "system_A": system_a,
                        "system_B": system_b,
                    }
                )
    return payloads, mappings


def call_judge(
    payloads: list[dict[str, Any]],
    output_path: Path,
    *,
    workers: int,
    resume: bool,
) -> tuple[list[dict[str, Any]], float]:
    prompt = PROMPT.read_text(encoding="utf-8")

    def worker(item: dict[str, Any]) -> dict[str, Any]:
        started = time.perf_counter()
        response = base.client().chat.completions.create(
            model=MODEL,
            response_format={"type": "json_object"},
            temperature=0,
            messages=[
                {"role": "system", "content": prompt},
                {
                    "role": "user",
                    "content": json.dumps(
                        item["model_payload"], ensure_ascii=False
                    ),
                },
            ],
        )
        latency = time.perf_counter() - started
        result = json.loads(response.choices[0].message.content or "{}")
        return {
            "payload_id": item["payload_id"],
            "question_id": item["question_id"],
            "judge_result": result,
            "judge_latency_seconds": latency,
            **base.api_metadata(response, "judge"),
        }

    started = time.perf_counter()
    rows = base.run_parallel(
        items=payloads,
        key=lambda row: str(row["payload_id"]),
        worker=worker,
        output_path=output_path,
        workers=workers,
        label=output_path.stem,
        resume=resume,
    )
    return rows, time.perf_counter() - started


def mapped_outcome(mapping: dict[str, Any], raw: dict[str, Any]) -> str:
    result = raw["judge_result"]
    for field in (
        "scientific_correctness",
        "question_fulfillment",
        "overall_preference",
    ):
        if str(result.get(field, "")).lower() not in {"a", "b", "tie"}:
            raise RuntimeError(f"Invalid {field}: {mapping['payload_id']}")
    preference = str(result["overall_preference"]).lower()
    if preference == "tie":
        return "tie"
    return str(mapping[f"system_{preference.upper()}"])


def orientation_rows(
    mappings: list[dict[str, Any]],
    raw_rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    raw = {row["payload_id"]: row for row in raw_rows}
    rows: list[dict[str, Any]] = []
    for mapping in mappings:
        source = raw[mapping["payload_id"]]
        result = source["judge_result"]
        rows.append(
            {
                **mapping,
                "mapped_outcome": mapped_outcome(mapping, source),
                "scientific_correctness": result["scientific_correctness"],
                "question_fulfillment": result["question_fulfillment"],
                "overall_preference": result["overall_preference"],
                "confidence": result.get("confidence", ""),
                "rationale": result.get("rationale", ""),
                "material_errors_A": json.dumps(
                    result.get("material_errors_A", []),
                    ensure_ascii=False,
                ),
                "material_errors_B": json.dumps(
                    result.get("material_errors_B", []),
                    ensure_ascii=False,
                ),
                "judge_latency_seconds": source["judge_latency_seconds"],
                "judge_prompt_tokens": source["judge_prompt_tokens"],
                "judge_completion_tokens": source[
                    "judge_completion_tokens"
                ],
                "judge_total_tokens": source["judge_total_tokens"],
            }
        )
    return rows


def discordant_units(
    rows: list[dict[str, Any]],
) -> set[tuple[str, str, str]]:
    grouped: dict[tuple[str, str, str], list[str]] = defaultdict(list)
    for row in rows:
        grouped[
            (
                row["question_id"],
                row["left_system"],
                row["right_system"],
            )
        ].append(row["mapped_outcome"])
    return {
        key
        for key, outcomes in grouped.items()
        if len(outcomes) != 2 or outcomes[0] != outcomes[1]
    }


def finalize_units(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[
            (
                row["question_id"],
                row["left_system"],
                row["right_system"],
            )
        ].append(row)
    final: list[dict[str, Any]] = []
    for (qid, left, right), judgments in sorted(grouped.items()):
        points = {left: 0.0, right: 0.0}
        for judgment in judgments:
            outcome = judgment["mapped_outcome"]
            if outcome == "tie":
                points[left] += 0.5
                points[right] += 0.5
            else:
                points[outcome] += 1.0
        winner = (
            left
            if points[left] > points[right]
            else right
            if points[right] > points[left]
            else "tie"
        )
        final.append(
            {
                "question_id": qid,
                "system_i": left,
                "system_j": right,
                "outcome": winner,
                "judgment_count": len(judgments),
                "system_i_points": points[left],
                "system_j_points": points[right],
                "initial_mirror_agreement": (
                    judgments[0]["mapped_outcome"]
                    == judgments[1]["mapped_outcome"]
                ),
            }
        )
    return final


def fit_davidson(
    outcomes: list[dict[str, Any]],
    systems: tuple[str, ...] = SYSTEMS,
) -> dict[str, Any]:
    index = {system: i for i, system in enumerate(systems)}

    def unpack(values: np.ndarray) -> tuple[np.ndarray, float]:
        theta = np.r_[values[: len(systems) - 1], 0.0]
        theta -= theta.mean()
        return theta, math.exp(float(values[-1]))

    def objective(values: np.ndarray) -> float:
        theta, nu = unpack(values)
        loss = 0.0
        for row in outcomes:
            i, j = index[row["system_i"]], index[row["system_j"]]
            pi, pj = math.exp(theta[i]), math.exp(theta[j])
            tie_mass = 2.0 * nu * math.sqrt(pi * pj)
            denominator = pi + pj + tie_mass
            if row["outcome"] == row["system_i"]:
                probability = pi / denominator
            elif row["outcome"] == row["system_j"]:
                probability = pj / denominator
            else:
                probability = tie_mass / denominator
            loss -= math.log(max(probability, 1e-12))
        loss += 1e-4 * float(np.dot(values, values))
        return loss

    fitted = minimize(
        objective,
        np.zeros(len(systems)),
        method="BFGS",
    )
    if not fitted.success and not np.isfinite(fitted.fun):
        raise RuntimeError(f"Davidson fit failed: {fitted.message}")
    theta, nu = unpack(fitted.x)
    strengths = np.exp(theta)
    normalized = 100.0 * strengths / strengths.sum()
    return {
        "theta": dict(zip(systems, theta.tolist())),
        "normalized_ability": dict(zip(systems, normalized.tolist())),
        "tie_parameter_nu": nu,
        "objective": float(fitted.fun),
        "optimizer_success": bool(fitted.success),
    }


def bootstrap(
    outcomes: list[dict[str, Any]],
    *,
    repetitions: int,
    seed: int,
) -> list[dict[str, Any]]:
    by_qid: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in outcomes:
        by_qid[row["question_id"]].append(row)
    qids = sorted(by_qid)
    rng = np.random.default_rng(seed)
    draws: list[dict[str, Any]] = []
    for repeat in range(1, repetitions + 1):
        sample = rng.choice(qids, size=len(qids), replace=True)
        sampled = [
            row for qid in sample for row in by_qid[str(qid)]
        ]
        fit = fit_davidson(sampled)
        draws.append(
            {
                "bootstrap_repeat": repeat,
                **{
                    f"{system}_normalized_ability": fit[
                        "normalized_ability"
                    ][system]
                    for system in SYSTEMS
                },
            }
        )
    return draws


def percentile(values: list[float], q: float) -> float:
    return float(np.percentile(np.asarray(values), q))


def summarize(
    outcomes: list[dict[str, Any]],
    fit: dict[str, Any],
    draws: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    ability: list[dict[str, Any]] = []
    for system in SYSTEMS:
        values = [
            float(row[f"{system}_normalized_ability"]) for row in draws
        ]
        ability.append(
            {
                "system": system,
                "normalized_ability_score": fit["normalized_ability"][system],
                "ci95_low": percentile(values, 2.5),
                "ci95_high": percentile(values, 97.5),
                "rank1_probability": sum(
                    float(row[f"{system}_normalized_ability"])
                    == max(
                        float(row[f"{candidate}_normalized_ability"])
                        for candidate in SYSTEMS
                    )
                    for row in draws
                )
                / len(draws),
                "davidson_theta": fit["theta"][system],
                "tie_parameter_nu": fit["tie_parameter_nu"],
            }
        )
    pairwise: list[dict[str, Any]] = []
    for left, right in combinations(SYSTEMS, 2):
        rows = [
            row
            for row in outcomes
            if row["system_i"] == left and row["system_j"] == right
        ]
        pairwise.append(
            {
                "system_i": left,
                "system_j": right,
                "questions": len(rows),
                "system_i_wins": sum(
                    row["outcome"] == left for row in rows
                ),
                "ties": sum(row["outcome"] == "tie" for row in rows),
                "system_j_wins": sum(
                    row["outcome"] == right for row in rows
                ),
            }
        )
    return ability, pairwise


def write_manifest(
    out: Path,
    orientation: list[dict[str, Any]],
    outcomes: list[dict[str, Any]],
    fit: dict[str, Any],
    *,
    wall_clock: float,
    bootstrap_repetitions: int,
    seed: int,
) -> None:
    prompt_tokens = sum(int(row["judge_prompt_tokens"]) for row in orientation)
    completion_tokens = sum(
        int(row["judge_completion_tokens"]) for row in orientation
    )
    position_counts = Counter(
        str(row["overall_preference"]).lower() for row in orientation
    )
    decisive_position_calls = position_counts["a"] + position_counts["b"]
    manifest = {
        "status": "completed_dev13_adaptive_davidson_pairwise_v1",
        "scope": "Dev13 only; no Test40 execution",
        "systems": list(SYSTEMS),
        "judge_model": MODEL,
        "temperature": 0,
        "initial_mirrored_calls_per_pair_question": 2,
        "discordant_mirrors_receive_second_mirrored_pair": True,
        "question_pair_units": len(outcomes),
        "judge_call_count": len(orientation),
        "initial_mirror_agreement_rate": sum(
            bool(row["initial_mirror_agreement"]) for row in outcomes
        )
        / len(outcomes),
        "units_requiring_second_mirrored_pair": sum(
            int(row["judgment_count"]) == 4 for row in outcomes
        ),
        "final_tie_count": sum(
            row["outcome"] == "tie" for row in outcomes
        ),
        "position_diagnostic": {
            "answer_A_selected": position_counts["a"],
            "answer_B_selected": position_counts["b"],
            "tie_selected": position_counts["tie"],
            "answer_A_share_among_decisive": (
                position_counts["a"] / decisive_position_calls
                if decisive_position_calls
                else None
            ),
            "two_sided_binomial_p_against_0_5": (
                binomtest(
                    position_counts["a"],
                    decisive_position_calls,
                    0.5,
                ).pvalue
                if decisive_position_calls
                else None
            ),
        },
        "davidson_fit": fit,
        "bootstrap": {
            "cluster": "question_id",
            "repetitions": bootstrap_repetitions,
            "seed": seed,
            "interval": "95% percentile",
        },
        "tokens": {
            "prompt": prompt_tokens,
            "completion": completion_tokens,
            "total": prompt_tokens + completion_tokens,
            "estimated_usd": (
                prompt_tokens * 1.25 + completion_tokens * 10.0
            )
            / 1_000_000,
        },
        "latency": {
            "judge_request_seconds_sum": sum(
                float(row["judge_latency_seconds"]) for row in orientation
            ),
            "judge_request_seconds_mean": sum(
                float(row["judge_latency_seconds"]) for row in orientation
            )
            / len(orientation),
            "judge_stage_wall_clock_seconds": wall_clock,
        },
        "inputs": {
            base.project_relative(path): base.sha256(path)
            for path in (
                QUESTIONS,
                GOLD,
                PROMPT,
                SOURCE / "experiment_manifest.json",
            )
        },
    }
    (out / "experiment_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True)
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--bootstrap", type=int, default=2000)
    parser.add_argument("--seed", type=int, default=20260726)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()
    requested_out = Path(args.out).expanduser()
    if not requested_out.is_absolute():
        requested_out = ROOT / requested_out
    prior_manifest_path = requested_out.resolve() / "experiment_manifest.json"
    prior_wall_clock: float | None = None
    if args.resume and prior_manifest_path.is_file():
        prior_manifest = json.loads(
            prior_manifest_path.read_text(encoding="utf-8")
        )
        prior_wall_clock = float(
            prior_manifest.get("latency", {}).get(
                "judge_stage_wall_clock_seconds", 0.0
            )
            or 0.0
        )
    out = base.prepare_output_dir(args.out, resume=args.resume)
    load_dotenv(ROOT / ".env")

    questions = base.read_csv(QUESTIONS)
    qids = [str(row["question_id"]) for row in questions]
    answers = read_answers()
    verification = load_verification(qids)
    gold = base.group_gold(base.read_jsonl(GOLD))
    if any(qid not in gold or not gold[qid] for qid in qids):
        raise RuntimeError("Every Dev13 question must have gold evidence")

    payloads1, mappings1 = build_calls(
        questions,
        answers,
        verification,
        gold,
        round_number=1,
    )
    base.write_jsonl(out / "judge/round1/payloads.jsonl", payloads1)
    base.write_jsonl(out / "judge/round1/blind_mapping.jsonl", mappings1)
    raw1, wall1 = call_judge(
        payloads1,
        out / "judge/round1/raw_results.jsonl",
        workers=args.workers,
        resume=args.resume,
    )
    rows1 = orientation_rows(mappings1, raw1)
    base.write_csv(out / "judge/round1/orientation_results.csv", rows1)

    selected = discordant_units(rows1)
    rows2: list[dict[str, Any]] = []
    wall2 = 0.0
    if selected:
        payloads2, mappings2 = build_calls(
            questions,
            answers,
            verification,
            gold,
            round_number=2,
            selected=selected,
        )
        base.write_jsonl(out / "judge/round2/payloads.jsonl", payloads2)
        base.write_jsonl(
            out / "judge/round2/blind_mapping.jsonl", mappings2
        )
        raw2, wall2 = call_judge(
            payloads2,
            out / "judge/round2/raw_results.jsonl",
            workers=args.workers,
            resume=args.resume,
        )
        rows2 = orientation_rows(mappings2, raw2)
        base.write_csv(
            out / "judge/round2/orientation_results.csv", rows2
        )

    orientation = rows1 + rows2
    outcomes = finalize_units(orientation)
    if len(outcomes) != 39:
        raise RuntimeError(f"Expected 39 pair-question outcomes: {len(outcomes)}")
    fit = fit_davidson(outcomes)
    draws = bootstrap(
        outcomes, repetitions=args.bootstrap, seed=args.seed
    )
    ability, pairwise = summarize(outcomes, fit, draws)
    base.write_csv(out / "results/orientation_level.csv", orientation)
    base.write_csv(out / "results/pair_question_outcomes.csv", outcomes)
    base.write_csv(out / "results/pairwise_wtl.csv", pairwise)
    base.write_csv(out / "results/davidson_ability.csv", ability)
    base.write_csv(out / "results/bootstrap_draws.csv", draws)
    write_manifest(
        out,
        orientation,
        outcomes,
        fit,
        wall_clock=(
            prior_wall_clock
            if prior_wall_clock is not None and prior_wall_clock > 0.01
            else wall1 + wall2
        ),
        bootstrap_repetitions=args.bootstrap,
        seed=args.seed,
    )
    print(json.dumps({"ability": ability, "pairwise": pairwise}, indent=2))


if __name__ == "__main__":
    main()

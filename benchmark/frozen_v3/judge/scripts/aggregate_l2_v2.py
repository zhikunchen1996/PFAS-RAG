from __future__ import annotations

import argparse
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import fit_davidson_v2
import judge_common as common


def parse_pair(value: str) -> tuple[str, str, Path]:
    parts = value.split(",", 2)
    if len(parts) != 3:
        raise ValueError("--pair must be LEFT,RIGHT,DIRECTORY")
    return parts[0], parts[1], Path(parts[2]).expanduser().resolve()


def exact_binomial_p(first: int, second: int) -> float:
    total = first + second
    if total == 0:
        return 1.0
    lower = min(first, second)
    return min(
        1.0,
        2
        * sum(
            math.comb(total, value) * 0.5**total
            for value in range(lower + 1)
        ),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--pair",
        action="append",
        required=True,
        help="LEFT,RIGHT,DIRECTORY; repeat for each connected system pair",
    )
    parser.add_argument("--out", required=True)
    parser.add_argument("--bootstrap", type=int, default=10_000)
    parser.add_argument("--seed", type=int, default=20260728)
    args = parser.parse_args()

    grouped: dict[str, list[fit_davidson_v2.Observation]] = defaultdict(list)
    raw_counts: list[dict[str, Any]] = []
    agreement_rows: list[dict[str, Any]] = []
    position_counts: dict[str, Counter[str]] = defaultdict(Counter)
    seen_pairs: set[frozenset[str]] = set()

    for pair_value in args.pair:
        left, right, directory = parse_pair(pair_value)
        if left == right:
            raise ValueError("A pair must contain two distinct systems")
        pair_key = frozenset((left, right))
        if pair_key in seen_pairs:
            raise ValueError(f"Duplicate system pair: {left}, {right}")
        seen_pairs.add(pair_key)
        envelopes = common.read_jsonl(directory / "local_envelopes.jsonl")
        results = common.read_jsonl(directory / "judge_results.jsonl")
        if len(envelopes) != len(results) or len(envelopes) % 2:
            raise RuntimeError(f"{directory}: incomplete mirrored results")
        result_by_id = {row["payload_id"]: row for row in results}
        if len(result_by_id) != len(results):
            raise RuntimeError(f"{directory}: duplicate result payload_id")
        envelope_ids = [row["payload_id"] for row in envelopes]
        if len(set(envelope_ids)) != len(envelope_ids):
            raise RuntimeError(f"{directory}: duplicate envelope payload_id")
        if set(envelope_ids) != set(result_by_id):
            raise RuntimeError(
                f"{directory}: envelope/result payload IDs do not match"
            )
        votes: dict[str, dict[str, list[str]]] = defaultdict(
            lambda: defaultdict(list)
        )
        for envelope in envelopes:
            result = result_by_id[envelope["payload_id"]]["judge_result"]
            common.validate_judge_result(result)
            for criterion in common.CRITERIA:
                raw_preference = result["criterion_preferences"][criterion]
                position_counts[criterion][raw_preference] += 1
                votes[str(envelope["question_id"])][criterion].append(
                    common.mapped_preference(
                        raw_preference,
                        envelope["assignment"],
                    )
                )

        for criterion in common.CRITERIA:
            flattened: list[str] = []
            agreements = 0
            for qid in sorted(votes):
                criterion_votes = votes[qid][criterion]
                if len(criterion_votes) != 2:
                    raise RuntimeError(
                        f"{left}/{right}/{qid}/{criterion}: expected 2 votes"
                    )
                agreements += len(set(criterion_votes)) == 1
                for outcome in criterion_votes:
                    grouped[criterion].append(
                        (qid, left, right, outcome)
                    )
                    flattened.append(outcome)
            counts = Counter(flattened)
            raw_counts.append(
                {
                    "left_system": left,
                    "right_system": right,
                    "criterion": criterion,
                    "left_votes": counts[left],
                    "right_votes": counts[right],
                    "tie_votes": counts["tie"],
                    "raw_vote_count": len(flattened),
                }
            )
            agreement_rows.append(
                {
                    "left_system": left,
                    "right_system": right,
                    "criterion": criterion,
                    "question_count": len(votes),
                    "mirrored_agreement_count": agreements,
                    "mirrored_agreement_rate": agreements / len(votes),
                }
            )

    point_estimates = {
        criterion: fit_davidson_v2.fit(rows)
        for criterion, rows in grouped.items()
    }
    bootstrap = fit_davidson_v2.bootstrap_joint(
        grouped,
        samples=args.bootstrap,
        seed=args.seed,
    )
    ability_rows: list[dict[str, Any]] = []
    for criterion, fitted in point_estimates.items():
        for system, ability in fitted["normalized_ability"].items():
            interval = bootstrap["criterion_intervals"][criterion][system]
            ability_rows.append(
                {
                    "criterion": criterion,
                    "system": system,
                    "normalized_ability": ability,
                    "lower_95": interval["lower_95"],
                    "upper_95": interval["upper_95"],
                    "criterion_specific_tie_parameter": fitted[
                        "tie_parameter"
                    ],
                    "raw_vote_count": fitted["observation_count"],
                }
            )

    systems = sorted(
        point_estimates[next(iter(point_estimates))]["normalized_ability"]
    )
    composite_rows = []
    for system in systems:
        value = sum(
            point_estimates[criterion]["normalized_ability"][system]
            for criterion in point_estimates
        ) / len(point_estimates)
        interval = bootstrap["equal_weight_composite_intervals"][system]
        composite_rows.append(
            {
                "system": system,
                "equal_weight_composite": value,
                "lower_95": interval["lower_95"],
                "upper_95": interval["upper_95"],
                "role": "descriptive secondary only",
            }
        )

    position_rows = []
    for criterion, counts in position_counts.items():
        non_ties = counts["A"] + counts["B"]
        position_rows.append(
            {
                "criterion": criterion,
                "A_count": counts["A"],
                "B_count": counts["B"],
                "tie_count": counts["tie"],
                "A_share_among_non_ties": counts["A"] / non_ties,
                "two_sided_exact_binomial_p": exact_binomial_p(
                    counts["A"],
                    counts["B"],
                ),
            }
        )

    out = Path(args.out).expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)
    common.write_csv(out / "criterion_abilities.csv", ability_rows)
    common.write_csv(out / "equal_weight_composite_secondary.csv", composite_rows)
    common.write_csv(out / "raw_vote_counts.csv", raw_counts)
    common.write_csv(out / "mirrored_agreement.csv", agreement_rows)
    common.write_csv(out / "position_bias.csv", position_rows)
    common.write_json(
        out / "fit_manifest.json",
        {
            "model": "separate criterion-specific Davidson fits",
            "tie_parameter": (
                "one independently estimated tie parameter per criterion"
            ),
            "adaptive_repeats": False,
            "hard_consensus_resolution": False,
            "unstable_exclusion": False,
            "bootstrap": bootstrap,
        },
    )


if __name__ == "__main__":
    main()

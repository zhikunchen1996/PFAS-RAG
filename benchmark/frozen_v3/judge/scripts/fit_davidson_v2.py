from __future__ import annotations

import math
from collections import defaultdict
from typing import Any

import numpy as np
from scipy.optimize import minimize


Observation = tuple[str, str, str, str]


def ensure_connected(rows: list[Observation]) -> None:
    graph: dict[str, set[str]] = defaultdict(set)
    for _, left, right, _ in rows:
        if left == right:
            raise ValueError("A Davidson observation cannot compare a system to itself")
        graph[left].add(right)
        graph[right].add(left)
    if len(graph) < 2:
        raise ValueError("Davidson fit requires at least two systems")
    pending = [next(iter(graph))]
    visited: set[str] = set()
    while pending:
        system = pending.pop()
        if system in visited:
            continue
        visited.add(system)
        pending.extend(graph[system] - visited)
    if visited != set(graph):
        raise ValueError("Davidson comparison graph is disconnected")


def fit(rows: list[Observation]) -> dict[str, Any]:
    ensure_connected(rows)
    systems = sorted({value for row in rows for value in row[1:3]})
    index = {system: i for i, system in enumerate(systems)}
    anchor = len(systems) - 1

    def unpack(params: np.ndarray) -> tuple[np.ndarray, float]:
        theta = np.zeros(len(systems))
        theta[:anchor] = params[:anchor]
        return theta, math.exp(float(params[-1]))

    def objective(params: np.ndarray) -> float:
        theta, tie_parameter = unpack(params)
        loss = 0.0
        for _, left, right, outcome in rows:
            left_ability = math.exp(float(theta[index[left]]))
            right_ability = math.exp(float(theta[index[right]]))
            tie_mass = tie_parameter * math.sqrt(
                left_ability * right_ability
            )
            denominator = left_ability + right_ability + tie_mass
            if outcome == left:
                probability = left_ability / denominator
            elif outcome == right:
                probability = right_ability / denominator
            elif outcome == "tie":
                probability = tie_mass / denominator
            else:
                raise ValueError(f"Unknown outcome: {outcome}")
            loss -= math.log(max(probability, 1e-12))
        loss += 1e-6 * float(np.square(params).sum())
        return loss

    fitted = minimize(
        objective,
        np.zeros(anchor + 1),
        method="BFGS",
    )
    if not fitted.success:
        raise RuntimeError(f"Davidson fit failed: {fitted.message}")
    theta, tie_parameter = unpack(fitted.x)
    shifted = theta - theta.max()
    ability = np.exp(shifted)
    normalized = ability / ability.sum()
    return {
        "systems": systems,
        "normalized_ability": {
            system: float(normalized[index[system]]) for system in systems
        },
        "tie_parameter": float(tie_parameter),
        "observation_count": len(rows),
    }


def bootstrap_joint(
    grouped: dict[str, list[Observation]],
    *,
    samples: int = 10_000,
    seed: int = 20260728,
) -> dict[str, Any]:
    if samples < 10_000:
        raise ValueError("Frozen protocol requires at least 10,000 resamples")
    criteria = sorted(grouped)
    qids_by_criterion = {
        criterion: {row[0] for row in rows}
        for criterion, rows in grouped.items()
    }
    qids = sorted(next(iter(qids_by_criterion.values())))
    if any(set(qids) != values for values in qids_by_criterion.values()):
        raise ValueError("All criteria must contain the same questions")

    rows_by_criterion_qid: dict[
        str,
        dict[str, list[Observation]],
    ] = {}
    for criterion, rows in grouped.items():
        by_qid: dict[str, list[Observation]] = defaultdict(list)
        for row in rows:
            by_qid[row[0]].append(row)
        rows_by_criterion_qid[criterion] = by_qid

    rng = np.random.default_rng(seed)
    criterion_draws: dict[str, dict[str, list[float]]] = defaultdict(
        lambda: defaultdict(list)
    )
    composite_draws: dict[str, list[float]] = defaultdict(list)
    successful = 0
    failures = 0

    for _ in range(samples):
        sampled = [str(value) for value in rng.choice(
            qids,
            size=len(qids),
            replace=True,
        )]
        replicate: dict[str, dict[str, Any]] = {}
        try:
            for criterion in criteria:
                rows = [
                    row
                    for qid in sampled
                    for row in rows_by_criterion_qid[criterion][qid]
                ]
                replicate[criterion] = fit(rows)
        except (RuntimeError, OverflowError, ValueError):
            failures += 1
            continue

        successful += 1
        systems = replicate[criteria[0]]["systems"]
        for criterion in criteria:
            for system, value in replicate[criterion][
                "normalized_ability"
            ].items():
                criterion_draws[criterion][system].append(value)
        for system in systems:
            composite_draws[system].append(
                sum(
                    replicate[criterion]["normalized_ability"][system]
                    for criterion in criteria
                )
                / len(criteria)
            )

    if successful == 0:
        raise RuntimeError("Every bootstrap replicate failed")

    def interval(values: list[float]) -> dict[str, float]:
        return {
            "lower_95": float(np.quantile(values, 0.025)),
            "upper_95": float(np.quantile(values, 0.975)),
        }

    return {
        "method": "question-level clustered percentile bootstrap",
        "seed": seed,
        "attempted_replicates": samples,
        "successful_replicates": successful,
        "failed_replicates": failures,
        "nonconvergence_rate": failures / samples,
        "criterion_intervals": {
            criterion: {
                system: interval(values)
                for system, values in systems.items()
            }
            for criterion, systems in criterion_draws.items()
        },
        "equal_weight_composite_intervals": {
            system: interval(values)
            for system, values in composite_draws.items()
        },
    }

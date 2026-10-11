"""Recompute the expert aggregates from anonymized numeric records."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
import json
from pathlib import Path
from statistics import mean

DIMENSIONS = (
    'task_fulfillment', 'scientific_accuracy', 'technology_evidence_coherence',
    'critical_synthesis', 'evidence_citation_integration', 'research_gaps_outlook',
)
SYSTEMS = ('PFAS RAG', 'Web Search', 'Direct')
PAIRS = (('PFAS RAG', 'Direct'), ('Web Search', 'Direct'), ('PFAS RAG', 'Web Search'))
ROOT = Path(__file__).resolve().parents[2]


def read_csv(path: Path) -> list[dict]:
    with path.open(newline='', encoding='utf-8') as handle:
        return list(csv.DictReader(handle))


def aggregate(folder: Path) -> dict:
    pairs = read_csv(folder / 'expert_pairwise_records.csv')
    scores = read_csv(folder / 'expert_dimension_records.csv')
    if len(pairs) != 30 or len(scores) != 60:
        raise ValueError('Expected 30 pair judgments and 60 candidate ratings')
    keys = {(row['rater_id'], row['task_id']) for row in pairs}
    if len(keys) != 30 or set(Counter(row['task_id'] for row in pairs).values()) != {3}:
        raise ValueError('Duplicate judgments or unbalanced task coverage')
    if set(Counter(row['rater_id'] for row in pairs).values()) != {10}:
        raise ValueError('Each rater must assess ten tasks')
    expected_scores = {}
    error_flags = 0
    for row in pairs:
        if row['system_1'] == row['system_2'] or not {row['system_1'], row['system_2']} <= set(SYSTEMS):
            raise ValueError('Invalid system pair')
        if row['preferred_system'] not in {row['system_1'], row['system_2'], 'Tie'}:
            raise ValueError('Preference is not a member of the pair')
        for index in (1, 2):
            flag = row[f'material_error_{index}']
            if flag not in {'Y', 'N'}:
                raise ValueError('Missing explicit material-error flag')
            error_flags += flag == 'Y'
            key = (row['rater_id'], row['task_id'], row[f'candidate_{index}'])
            expected_scores[key] = row[f'system_{index}']
    observed_scores = {}
    grouped = defaultdict(list)
    for row in scores:
        key = (row['rater_id'], row['task_id'], row['candidate_id'])
        if key in observed_scores or expected_scores.get(key) != row['system']:
            raise ValueError('Duplicate rating or pair/score mapping mismatch')
        observed_scores[key] = row['system']
        values = {key: int(row[key]) for key in DIMENSIONS}
        if not all(1 <= value <= 5 for value in values.values()):
            raise ValueError('Ratings must be integers from 1 to 5')
        grouped[row['system']].append(values)
    if observed_scores != expected_scores or {len(grouped[system]) for system in SYSTEMS} != {20}:
        raise ValueError('Incomplete ratings or unbalanced system appearances')
    pairwise = []
    for first, second in PAIRS:
        selected = [row for row in pairs if {row['system_1'], row['system_2']} == {first, second}]
        if len(selected) != 10 or len({row['task_id'] for row in selected}) != 10:
            raise ValueError('Each system pair must be judged once per task')
        counts = Counter(row['preferred_system'] for row in selected)
        pairwise.append({'pair': f'{first} vs {second}', first: counts[first], 'Tie': counts['Tie'], second: counts[second]})
    return {
        'status': 'complete', 'judgments': 30, 'tasks': 10,
        'candidate_appearances_per_system': 20, 'pairwise': pairwise,
        'dimension_means': [
            {'system': system, **{key: mean(row[key] for row in grouped[system]) for key in DIMENSIONS}}
            for system in SYSTEMS
        ],
        'material_error_flags': error_flags,
    }


def compare_summary(actual: dict, expected: dict) -> None:
    for key in ('status', 'judgments', 'tasks', 'candidate_appearances_per_system', 'material_error_flags'):
        if actual[key] != expected[key]:
            raise ValueError(f'Expert summary mismatch: {key}')
    for row in actual['pairwise']:
        target = next(item for item in expected['pairwise'] if item['pair'] == row['pair'])
        if any(value != target[key] for key, value in row.items()):
            raise ValueError(f'Expert preference mismatch: {row["pair"]}')
    for row in actual['dimension_means']:
        target = next(item for item in expected['dimension_means'] if item['system'] == row['system'])
        if any(abs(row[key] - target[key]) > 1e-12 for key in DIMENSIONS):
            raise ValueError(f'Expert dimension mismatch: {row["system"]}')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    actual = aggregate(Path(__file__).resolve().parent / 'expert_scores')
    target = ROOT / 'benchmark/review_tasks/runs/professional_review_human_expert_v1/summary.json'
    compare_summary(actual, json.loads(target.read_text()))
    if args.output:
        output = args.output.resolve()
        output.relative_to(ROOT / 'outputs')
        if output.exists():
            raise FileExistsError(output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(actual, indent=2) + '\n')
    print('PASS: anonymized expert records reproduce all frozen aggregates')


if __name__ == '__main__':
    main()

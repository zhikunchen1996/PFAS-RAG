"""Recompute formal retrieval metrics and three-repeat answer summaries."""

from __future__ import annotations

from collections import defaultdict
import csv
import json
from pathlib import Path
from statistics import mean, stdev
import sys

ROOT = Path(__file__).resolve().parents[2]
FORMAL = ROOT / 'benchmark/runs/test40_formal_v1_1'


def read_csv(path: Path) -> list[dict]:
    with path.open(newline='', encoding='utf-8') as handle:
        return list(csv.DictReader(handle))


def require_close(actual: float, expected: float, label: str) -> None:
    if abs(actual - expected) > 1e-12:
        raise ValueError(f'{label}: {actual} != {expected}')


def main() -> None:
    sys.path.insert(0, str(FORMAL / 'scripts'))
    import run_l1

    gold = defaultdict(list)
    for row in run_l1.common.read_jsonl(run_l1.common.GOLD):
        gold[str(row['question_id'])].append(row)
    stored = {row['system']: row for row in read_csv(FORMAL / 'results/l1/summary.csv')}
    retrieval_checks = 0
    for system, path in run_l1.paths(run_l1.common.RETRIEVAL_RESULTS, run_l1.common.SELECTOR_RESULTS).items():
        calculated = [
            run_l1.eval_context(
                str(row['question_id']), gold[str(row['question_id'])], row['retrieved_context'],
                str(row['retrieval_config_name']), str(row['retrieval_method']), 10, 60, 0,
            )
            for row in run_l1.common.read_jsonl(path)
        ]
        required = [row for row in calculated if int(row['required_gold_count']) > 0]
        if len(calculated) != 40 or len(required) != 38:
            raise ValueError('Incorrect Test40 or required-gold membership')
        for metric in ('MRR_required_gold', 'required_gold_recall@10', 'gold_doc_recall@10'):
            require_close(mean(float(row[metric]) for row in required), float(stored[system][metric]), f'{system}/{metric}')
            retrieval_checks += 1
    answer_checks = 0
    for package in ('test40_formal_v1_1', 'test40_multibase_direct_rag_v1'):
        base = ROOT / 'benchmark/runs' / package / 'results/l3'
        repeats = defaultdict(list)
        for index in (1, 2, 3):
            per_question = read_csv(base / f'repeat_{index}/question_level_scores.csv')
            summary = read_csv(base / f'repeat_{index}/system_summary.csv')
            for row in summary:
                values = [float(item['component_balanced_core_reference_claim_coverage']) for item in per_question if item['system'] == row['system']]
                if len(values) != 40:
                    raise ValueError('Each system repeat must contain all forty questions')
                value = mean(values)
                require_close(value, float(row['mean_component_balanced_core_reference_claim_coverage']), f'{package}/{row["system"]}/repeat{index}')
                repeats[row['system']].append(value)
        for row in read_csv(base / 'aggregate/system_three_repeat_summary.csv'):
            values = repeats[row['system']]
            require_close(mean(values), float(row['mean_l3_core_coverage']), f'{package}/{row["system"]}/mean')
            require_close(stdev(values), float(row['sample_sd_across_repeat_system_means']), f'{package}/{row["system"]}/sample SD')
            answer_checks += 1
    print(json.dumps({'status': 'passed', 'retrieval_metrics': retrieval_checks, 'answer_systems': answer_checks, 'new_model_calls': False}))


if __name__ == '__main__':
    main()

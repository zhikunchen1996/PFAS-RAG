"""Recompute supplementary statistics without figures or frozen-file writes."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
COST = ROOT / 'benchmark/ablations/test40_retrieval_answer_cost_v2'
CORRELATION = ROOT / 'benchmark/ablations/test40_retrieval_metric_answer_correlation_v1'


def load_module(name: str, script: Path):
    spec = importlib.util.spec_from_file_location(name, script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate_output(path: Path) -> Path:
    output = path.resolve()
    output.relative_to((ROOT / 'outputs').resolve())
    if output.exists():
        raise FileExistsError(f'Refusing to overwrite {output}')
    return output


def compare_tables(expected: Path, observed: Path) -> list[str]:
    names = sorted(path.name for path in expected.glob('*.csv'))
    if names != sorted(path.name for path in observed.glob('*.csv')):
        raise ValueError('Regenerated CSV inventory differs from the frozen analysis')
    for name in names:
        pd.testing.assert_frame_equal(
            pd.read_csv(expected / name), pd.read_csv(observed / name),
            check_dtype=False, rtol=1e-10, atol=1e-12,
        )
    return names


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    output = validate_output(args.output)
    cost = load_module('release_cost_analysis', COST / 'scripts/run_analysis.py')
    cost.RESULTS = output / 'retrieval_answer_cost'
    cost.RESULTS.mkdir(parents=True)
    cases = cost.build_cases()
    cases.to_csv(cost.RESULTS / 'analysis_cases.csv', index=False)
    cost.coupling_outputs(cases)
    cost.failure_outputs(cases)
    cost.cost_outputs(cases)
    cost.write_summary(cases)
    cost_tables = compare_tables(COST / 'results', cost.RESULTS)
    print(f'PASS: {len(cost_tables)} cost/coupling result tables reproduced', flush=True)

    correlation = load_module('release_correlation_analysis', CORRELATION / 'scripts/run_analysis.py')
    correlation.RESULTS = output / 'retrieval_metric_correlations'
    correlation.RESULTS.mkdir()
    applicable = correlation.load_applicable_cases()
    correlation.correlation_outputs(applicable)
    correlation.full_retrieval_output(applicable)
    correlation.matched_full_retrieval_output(applicable)
    correlation.write_summary()
    correlation_tables = compare_tables(CORRELATION / 'results', correlation.RESULTS)
    scripts = [COST / 'scripts/run_analysis.py', CORRELATION / 'scripts/run_analysis.py']
    report = {
        'new_model_calls': False, 'figures_generated': False,
        'frozen_files_modified': False, 'status': 'passed',
        'cost_tables': cost_tables, 'correlation_tables': correlation_tables,
        'source_scripts': {
            path.relative_to(ROOT).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in scripts
        },
    }
    (output / 'validation_summary.json').write_text(json.dumps(report, indent=2) + '\n')
    print(f'PASS: {len(correlation_tables)} correlation result tables reproduced; no figures or model calls')


if __name__ == '__main__':
    main()

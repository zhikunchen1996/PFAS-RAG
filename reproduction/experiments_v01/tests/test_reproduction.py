from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

RELEASE = Path(__file__).resolve().parents[1]
ROOT = RELEASE.parents[1]
sys.path.insert(0, str(RELEASE))
import aggregate_expert_scores as experts
import run_analysis


class ReproductionTests(unittest.TestCase):
    def test_formal_source_matches_all_anchors(self):
        manifest = json.loads((RELEASE / 'formal_source_manifest.json').read_text())
        source = RELEASE / 'formal_source' if (RELEASE / 'formal_source').exists() else ROOT
        self.assertEqual(len(manifest['files']), 7)
        for relative, expected in manifest['files'].items():
            self.assertEqual(hashlib.sha256((source / relative).read_bytes()).hexdigest(), expected)

    def test_all_expert_aggregates_match(self):
        actual = experts.aggregate(RELEASE / 'expert_scores')
        expected = json.loads((ROOT / 'benchmark/review_tasks/runs/professional_review_human_expert_v1/summary.json').read_text())
        experts.compare_summary(actual, expected)

    def test_error_flags_are_calculated_not_assumed_zero(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            for name in ('expert_pairwise_records.csv', 'expert_dimension_records.csv'):
                rows = experts.read_csv(RELEASE / 'expert_scores' / name)
                if name == 'expert_pairwise_records.csv':
                    rows[0]['material_error_1'] = 'Y'
                with (folder / name).open('w', newline='') as handle:
                    writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
                    writer.writeheader()
                    writer.writerows(rows)
            self.assertEqual(experts.aggregate(folder)['material_error_flags'], 1)

    def test_missing_expert_flag_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            for name in ('expert_pairwise_records.csv', 'expert_dimension_records.csv'):
                rows = experts.read_csv(RELEASE / 'expert_scores' / name)
                if name == 'expert_pairwise_records.csv':
                    rows[0]['material_error_1'] = ''
                with (folder / name).open('w', newline='') as handle:
                    writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
                    writer.writeheader()
                    writer.writerows(rows)
            with self.assertRaises(ValueError):
                experts.aggregate(folder)

    def test_output_cannot_target_frozen_packages(self):
        with self.assertRaises(ValueError):
            run_analysis.validate_output(ROOT / 'benchmark/new_results')

    def test_existing_outputs_are_not_overwritten(self):
        (ROOT / 'outputs').mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=ROOT / 'outputs') as tmp:
            with self.assertRaises(FileExistsError):
                run_analysis.validate_output(Path(tmp))


if __name__ == '__main__':
    unittest.main()

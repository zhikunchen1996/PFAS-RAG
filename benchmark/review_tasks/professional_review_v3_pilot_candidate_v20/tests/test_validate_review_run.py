from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import sys
import tempfile
import unittest


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
SPEC = spec_from_file_location(
    "validate_review_run",
    SCRIPTS / "validate_review_run.py",
)
MODULE = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class ValidateReviewRunTests(unittest.TestCase):
    def test_allows_same_request_hash_for_distinct_judge_repeats(self):
        first = {
            "stage": "review_quality_judge",
            "call_key": "RT02:system:review_judge:r1",
        }
        second = {
            "stage": "review_quality_judge",
            "call_key": "RT02:system:review_judge:r2",
        }
        self.assertTrue(
            MODULE.is_allowed_judge_repeat_duplicate(first, second)
        )

    def test_rejects_duplicate_nonjudge_or_same_repeat(self):
        first = {
            "stage": "review_quality_judge",
            "call_key": "RT02:system:review_judge:r1",
        }
        self.assertFalse(
            MODULE.is_allowed_judge_repeat_duplicate(first, dict(first))
        )
        self.assertFalse(
            MODULE.is_allowed_judge_repeat_duplicate(
                {"stage": "structured_extraction", "call_key": "one"},
                {"stage": "structured_extraction", "call_key": "two"},
            )
        )

    @staticmethod
    def _metric_record():
        return {
            "quantitative_findings": [
                {
                    "value": "99",
                    "value_form": "exact_numeric",
                    "unit": "%",
                }
            ],
            "operating_conditions": [{"value": "30", "unit": "min"}],
            "endpoints": [{"endpoint_type": "removal"}],
            "comparability": {"status": "descriptive_only"},
        }

    def test_required_assessment_paths_are_complete_and_unique(self):
        record = self._metric_record()
        paths = MODULE.required_metric_assessment_paths(record)
        verification = {
            "field_assessments": [
                {
                    "field_path": path,
                    "status": "supported",
                    "error_type": "none",
                    "reason": "Supported.",
                }
                for path in sorted(paths)
            ]
        }
        MODULE.validate_required_assessments(
            record=record,
            verification=verification,
            label="RT01/system/record",
        )

    def test_required_assessment_paths_reject_missing_item(self):
        record = self._metric_record()
        verification = {
            "field_assessments": [
                {
                    "field_path": "comparability.status",
                    "status": "supported",
                    "error_type": "none",
                    "reason": "Supported.",
                }
            ]
        }
        with self.assertRaisesRegex(RuntimeError, "missing required"):
            MODULE.validate_required_assessments(
                record=record,
                verification=verification,
                label="RT01/system/record",
            )

    def test_required_assessment_paths_reject_duplicate_item(self):
        record = self._metric_record()
        paths = sorted(MODULE.required_metric_assessment_paths(record))
        assessments = [
            {
                "field_path": path,
                "status": "supported",
                "error_type": "none",
                "reason": "Supported.",
            }
            for path in paths
        ]
        assessments.append(dict(assessments[0]))
        with self.assertRaisesRegex(RuntimeError, "must occur once"):
            MODULE.validate_required_assessments(
                record=record,
                verification={"field_assessments": assessments},
                label="RT01/system/record",
            )

    def test_accepts_zero_based_complete_local_chunks(self):
        packet = {
            "sources": [
                {
                    "source_id": f"S{source_index:02d}",
                    "source": f"paper-{source_index}.pdf",
                    "title": f"Primary study {source_index}",
                    "doi": f"10.1000/test.{source_index}",
                    "doi_or_stable_url": (
                        f"https://doi.org/10.1000/test.{source_index}"
                    ),
                    "evidence_chunks": [
                        {
                            "locator_id": (
                                f"S{source_index:02d}-E{chunk_index:02d}"
                            ),
                            "corpus_chunk": chunk_index - 1,
                            "text": f"Evidence {chunk_index}",
                        }
                        for chunk_index in range(
                            1,
                            MODULE.CHUNKS_PER_DOCUMENT + 1,
                        )
                    ],
                }
                for source_index in range(
                    1,
                    MODULE.MIN_RETAINED_SOURCES + 1,
                )
            ]
        }
        MODULE.validate_source_packet(
            packet=packet,
            task_id="RT01",
            system="bge_llm_local_rag",
            anchor_identifiers={
                "dois": set(),
                "urls": set(),
                "titles": set(),
                "sources": set(),
            },
        )

    def test_rejects_source_count_below_minimum(self):
        with self.assertRaisesRegex(RuntimeError, "expected 6 to 20 sources"):
            MODULE.validate_source_packet(
                packet={"sources": []},
                task_id="RT01",
                system="gpt51_web_search",
                anchor_identifiers={
                    "dois": set(),
                    "urls": set(),
                    "titles": set(),
                    "sources": set(),
                },
            )

    def test_direct_artifact_guard_accepts_clean_no_retrieval_layout(self):
        with tempfile.TemporaryDirectory() as directory:
            run_dir = Path(directory)
            task_dir = run_dir / "systems" / "gpt51_direct" / "RT01"
            task_dir.mkdir(parents=True)
            MODULE.validate_direct_no_evidence_artifacts(
                run_dir=run_dir,
                task_dir=task_dir,
                task_id="RT01",
                system="gpt51_direct",
            )
            MODULE.validate_direct_review(
                "A citation-free scientific review.",
                task_id="RT01",
                system="gpt51_direct",
            )

    def test_direct_artifact_guard_rejects_retrieval_and_source_judge(self):
        with tempfile.TemporaryDirectory() as directory:
            run_dir = Path(directory)
            task_dir = run_dir / "systems" / "gpt51_direct" / "RT01"
            task_dir.mkdir(parents=True)
            (task_dir / "sources.json").write_text("{}", encoding="utf-8")
            with self.assertRaisesRegex(RuntimeError, "must not contain"):
                MODULE.validate_direct_no_evidence_artifacts(
                    run_dir=run_dir,
                    task_dir=task_dir,
                    task_id="RT01",
                    system="gpt51_direct",
                )
            (task_dir / "sources.json").unlink()
            support = (
                run_dir
                / "calls"
                / "gpt51_direct"
                / "RT01"
                / "review_source_support.json"
            )
            support.parent.mkdir(parents=True)
            support.write_text("{}", encoding="utf-8")
            with self.assertRaisesRegex(RuntimeError, "must not have"):
                MODULE.validate_direct_no_evidence_artifacts(
                    run_dir=run_dir,
                    task_dir=task_dir,
                    task_id="RT01",
                    system="gpt51_direct",
                )

    def test_direct_review_rejects_benchmark_source_identifier(self):
        with self.assertRaisesRegex(RuntimeError, "benchmark citations"):
            MODULE.validate_direct_review(
                "Unsupported benchmark citation [S01].",
                task_id="RT01",
                system="gpt51_direct",
            )


if __name__ == "__main__":
    unittest.main()

import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "filter_anchor_reviews.py"
SPEC = importlib.util.spec_from_file_location("filter_anchor_reviews", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class AnchorFilterTests(unittest.TestCase):
    def setUp(self):
        anchors = MODULE.load_jsonl(ROOT / "input" / "anchor_reviews.jsonl")
        self.rt01 = MODULE.task_anchor_identifiers(anchors, "RT01")
        self.rt04 = MODULE.task_anchor_identifiers(anchors, "RT04")
        self.rt06 = MODULE.task_anchor_identifiers(anchors, "RT06")
        self.rt07 = MODULE.task_anchor_identifiers(anchors, "RT07")

    def test_normalizes_doi_urls(self):
        self.assertEqual(
            MODULE.normalize_doi("https://doi.org/10.1016/J.ENVPOL.2023.121138"),
            "10.1016/j.envpol.2023.121138",
        )

    def test_excludes_by_nested_metadata_doi(self):
        record = {
            "metadata": {
                "doi": "doi:10.1016/j.envpol.2023.121138",
                "source": "unrelated.pdf",
            }
        }
        self.assertTrue(MODULE.exclusion_reason(record, self.rt01).startswith("anchor_doi"))

    def test_excludes_by_exact_corpus_source(self):
        record = {
            "source": (
                "/tmp/2023 - Lei - A review of PFAS adsorption from aqueous "
                "solutions - Current approaches, engineering applications, "
                "challenges, and opportunities.pdf"
            )
        }
        self.assertTrue(
            MODULE.exclusion_reason(record, self.rt01).startswith("anchor_source")
        )

    def test_excludes_rt06_primary_anchor(self):
        record = {"doi": "10.1016/j.jhazmat.2023.133182"}
        self.assertTrue(MODULE.exclusion_reason(record, self.rt06).startswith("anchor_doi"))

    def test_excludes_alternate_repository_identifier(self):
        by_doi = {"doi": "https://doi.org/10.3929/ethz-b-000506220"}
        by_url = {
            "url": (
                "https://www.research-collection.ethz.ch/items/"
                "f9152dfa-5b8e-4ce2-8153-1cbb37911e55"
            )
        }
        self.assertTrue(
            MODULE.exclusion_reason(by_doi, self.rt04).startswith("anchor_doi")
        )
        self.assertTrue(
            MODULE.exclusion_reason(by_url, self.rt04).startswith("anchor_url")
        )

    def test_does_not_apply_other_task_anchor(self):
        record = {"doi": "10.1016/j.envint.2021.106876"}
        self.assertIsNone(MODULE.exclusion_reason(record, self.rt01))

    def test_tasks_sharing_review_apply_same_exclusion(self):
        record = {"doi": "https://doi.org/10.1016/j.jhazmat.2023.133182"}
        self.assertIsNotNone(MODULE.exclusion_reason(record, self.rt06))
        self.assertIsNotNone(MODULE.exclusion_reason(record, self.rt07))

    def test_filter_records_returns_audit_payload(self):
        records = [
            {"doi": "10.1016/j.envpol.2023.121138", "title": "anchor"},
            {"doi": "10.1000/example", "title": "primary study"},
        ]
        kept, removed = MODULE.filter_records(records, self.rt01)
        self.assertEqual(len(kept), 1)
        self.assertEqual(len(removed), 1)
        self.assertEqual(kept[0]["title"], "primary study")


if __name__ == "__main__":
    unittest.main()

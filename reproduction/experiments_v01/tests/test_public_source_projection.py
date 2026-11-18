import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location('source_projection', ROOT / 'scripts/verify_public_source_projection.py')
projection = importlib.util.module_from_spec(spec)
spec.loader.exec_module(projection)


class SourceProjectionTests(unittest.TestCase):
    def test_unprojected_passage_is_rejected(self):
        with self.assertRaises(AssertionError):
            projection.check({'retrieved_context': [{'text': 'A source passage.'}]})

    def test_hash_marker_is_accepted(self):
        projection.check({'text': '[SOURCE_TEXT_OMITTED sha256=' + 'a' * 64 + ']'})

    def test_short_or_invalid_marker_is_rejected(self):
        with self.assertRaises(AssertionError):
            projection.check({'exact_support': '[SOURCE_TEXT_OMITTED sha256=abc]'})

    def test_serialized_source_passage_is_checked(self):
        with self.assertRaises(AssertionError):
            projection.check({'raw_response_text': '{"evidence_span":"A source passage."}'})

    def test_empty_source_field_is_valid(self):
        projection.check({'exact_support': '', 'unit_exact_spans': []})

    def test_system_prompt_is_not_treated_as_source_data(self):
        projection.check({'role': 'system', 'content': '{"text":"schema example"}'})


if __name__ == '__main__':
    unittest.main()

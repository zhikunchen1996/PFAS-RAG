from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import json
import tempfile
import unittest


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
SPEC = spec_from_file_location(
    "review_runtime",
    SCRIPTS / "review_runtime.py",
)
MODULE = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class ReviewRuntimeTests(unittest.TestCase):
    def test_template_requires_exact_placeholders(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "template.txt"
            path.write_text("Question: {{QUESTION}}")
            self.assertEqual(
                MODULE.render_template(path, {"QUESTION": "Q"}),
                "Question: Q",
            )
            with self.assertRaises(KeyError):
                MODULE.render_template(path, {})
            with self.assertRaises(KeyError):
                MODULE.render_template(
                    path,
                    {"QUESTION": "Q", "EXTRA": "x"},
                )

    def test_cost_includes_uncached_cached_output_and_search(self):
        cost = MODULE.estimate_cost(
            model_snapshot="gpt-5.1-2025-11-13",
            input_tokens=1_000_000,
            cached_input_tokens=200_000,
            output_tokens=100_000,
            web_search_calls=2,
        )
        self.assertAlmostEqual(
            cost,
            800_000 / 1_000_000 * 1.25
            + 200_000 / 1_000_000 * 0.125
            + 100_000 / 1_000_000 * 10.0
            + 2 * 0.01,
        )

    def test_all_strict_object_properties_are_required(self):
        schema_dir = Path(__file__).resolve().parents[1] / "schemas"

        def visit(value):
            if isinstance(value, dict):
                if value.get("type") == "object" and "properties" in value:
                    self.assertFalse(value.get("additionalProperties", True))
                    self.assertEqual(
                        set(value["required"]),
                        set(value["properties"]),
                    )
                for child in value.values():
                    visit(child)
            elif isinstance(value, list):
                for child in value:
                    visit(child)

        for path in schema_dir.glob("*.schema.json"):
            visit(json.loads(path.read_text()))

    def test_quantitative_value_schema_requires_declared_form(self):
        schema_path = (
            Path(__file__).resolve().parents[1]
            / "schemas"
            / "evidence_table.schema.json"
        )
        quantitative = json.loads(schema_path.read_text())["$defs"][
            "quantitativeValue"
        ]
        base = {
            "name": "reported result",
            "unit": "%",
            "qualifiers": "",
            "evidence_locator_ids": ["S01-E01"],
        }
        for value, value_form in (
            ("99.7", "exact_numeric"),
            (">=95", "inequality"),
            ("~2.5", "approximate_numeric"),
            ("30-55", "range"),
            ("ND", "not_detected"),
        ):
            MODULE.validate_schema(
                {**base, "value": value, "value_form": value_form},
                quantitative,
                value,
            )
        with self.assertRaises(ValueError):
            MODULE.validate_schema(
                {**base, "value": "99.7"},
                quantitative,
                "missing value form",
            )


if __name__ == "__main__":
    unittest.main()

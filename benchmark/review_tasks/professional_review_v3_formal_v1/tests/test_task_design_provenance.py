import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load_jsonl(path):
    return [
        json.loads(line)
        for line in path.read_text().splitlines()
        if line.strip()
    ]


class TaskDesignProvenanceTests(unittest.TestCase):
    def setUp(self):
        self.tasks = load_jsonl(ROOT / "input" / "review_tasks.jsonl")
        self.anchors = load_jsonl(ROOT / "input" / "anchor_reviews.jsonl")
        self.provenance = load_jsonl(
            ROOT / "provenance" / "task_design_provenance.jsonl"
        )

    def test_every_task_maps_to_one_present_anchor(self):
        self.assertEqual(
            [task["task_id"] for task in self.tasks],
            [anchor["task_id"] for anchor in self.anchors],
        )
        for anchor_record in self.anchors:
            self.assertEqual(anchor_record["supplemental_anchors"], [])
            self.assertEqual(
                anchor_record["primary_anchor"]["corpus_presence"],
                "present",
            )
        self.assertEqual(
            len(
                {
                    record["primary_anchor"]["anchor_id"]
                    for record in self.anchors
                }
            ),
            5,
        )

    def test_design_chunks_exist_in_source_snapshot(self):
        for record in self.provenance:
            snapshot = json.loads(
                (ROOT / record["source_snapshot"]).read_text()
            )
            available = {
                chunk["chunk_index"]
                for chunk in snapshot["selected_chunks"]
            }
            referenced = {
                index
                for indices in record["design_basis"].values()
                for index in indices
            }
            self.assertTrue(referenced <= available)

    def test_visible_tasks_do_not_name_anchor_review(self):
        anchors = {
            record["task_id"]: record["primary_anchor"]
            for record in self.anchors
        }
        for task in self.tasks:
            visible = " ".join(
                [
                    task["title"],
                    task["review_brief"],
                    *(
                        component["requirement"]
                        for component in task["components"]
                    ),
                ]
            ).casefold()
            self.assertNotIn(
                anchors[task["task_id"]]["title"].casefold(),
                visible,
            )


if __name__ == "__main__":
    unittest.main()

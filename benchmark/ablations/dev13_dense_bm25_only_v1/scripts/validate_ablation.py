from __future__ import annotations

from collections import defaultdict
import csv
import hashlib
import json
import math
from pathlib import Path
import sys
from typing import Any


PACKAGE = Path(__file__).resolve().parents[1]
ROOT = PACKAGE.parents[2]
sys.path.insert(0, str(ROOT / "benchmark/frozen_v3/scripts"))

from retrieval_metrics import eval_context  # noqa: E402


QUESTIONS = ROOT / "benchmark/frozen_v3/input/questions_dev13.csv"
GOLD = ROOT / "benchmark/frozen_v3/gold/chunk_based_gold.jsonl"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def average(rows: list[dict[str, Any]], field: str) -> float:
    return sum(float(row[field]) for row in rows) / len(rows)


def validate_system(name: str, output_path: Path) -> None:
    question_ids = [row["question_id"] for row in read_csv(QUESTIONS)]
    outputs = read_jsonl(output_path)
    assert [str(row["question_id"]) for row in outputs] == question_ids
    for row in outputs:
        context = row["retrieved_context"]
        assert len(context) == 10
        keys = {(str(hit["doc_id"]), str(hit["chunk_id"])) for hit in context}
        assert len(keys) == 10
        assert not any(bool(hit.get("reference_like")) for hit in context)

    gold_by_qid: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in read_jsonl(GOLD):
        gold_by_qid[str(row["question_id"])].append(row)
    metrics = [
        eval_context(
            str(row["question_id"]),
            gold_by_qid[str(row["question_id"])],
            row["retrieved_context"],
            str(row["retrieval_config_name"]),
            str(row["retrieval_method"]),
            10,
            60,
            0,
        )
        for row in outputs
    ]
    required = [row for row in metrics if int(row["required_gold_count"]) > 0]
    negative = [row for row in metrics if int(row["negative_gold_count"]) > 0]
    stored = read_csv(PACKAGE / f"results/l1/{name}/summary.csv")[0]
    expected = {
        "MRR_required_gold": average(required, "MRR_required_gold"),
        "required_gold_recall@10": average(required, "required_gold_recall@10"),
        "gold_doc_recall@10": average(required, "gold_doc_recall@10"),
        "negative_gold_recall@10": average(negative, "negative_gold_recall@10"),
    }
    for field, value in expected.items():
        assert math.isclose(float(stored[field]), value, abs_tol=1e-12)


def main() -> None:
    manifest = json.loads((PACKAGE / "manifest.json").read_text())
    for relative, expected_hash in manifest["sha256"].items():
        path = ROOT / relative
        assert path.is_file(), relative
        assert sha256(path) == expected_hash, relative

    validate_system(
        "dense_only", PACKAGE / "results/retrieval/dense_only_top10.jsonl"
    )
    validate_system(
        "bm25_only", PACKAGE / "results/retrieval/bm25_only_top10.jsonl"
    )
    sensitivity = json.loads(
        (PACKAGE / "results/reference_penalty_sensitivity_all53_v1/summary.json").read_text()
    )
    for split in ("dev13", "test40"):
        legacy = sensitivity["metrics"][split]["legacy_penalty"]
        simplified = sensitivity["metrics"][split]["all_penalties_off"]
        for field in (
            "required_gold_recall@10",
            "gold_doc_recall@10",
            "negative_gold_recall@10",
        ):
            assert math.isclose(legacy[field], simplified[field], abs_tol=1e-12)
    assert sensitivity["identity"]["dev13"]["all_penalties_off"]["top10_set_identical"] == 12
    assert sensitivity["identity"]["test40"]["all_penalties_off"]["top10_set_identical"] == 36
    print(
        "VALIDATION PASS: Dev13 component ablation and all-53 penalty "
        "sensitivity are complete."
    )


if __name__ == "__main__":
    main()

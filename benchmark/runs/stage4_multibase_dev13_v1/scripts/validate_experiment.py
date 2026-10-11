from __future__ import annotations

import csv
import json
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
EXPECTED_PROMPTS = {
    "shared_system_prompt_sha256": (
        "6be207338004080e62cad1f8bc1799a289722cb0a19d5287b4b3925f6190f986"
    ),
    "direct_prompt_sha256": (
        "49ac7c12ddcf5681b449ea9960e842ca3cd89624022dad395de81e123a88808b"
    ),
    "rag_prompt_sha256": (
        "c01f300e1eaace48306af41068c97f7d84c7d80d24386f526927ac2e38c588f2"
    ),
}


def read_jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def main() -> None:
    errors: list[str] = []
    expected = {
        "gemini31_pro": "gemini-3.1-pro-preview",
        "claude_sonnet5": "claude-sonnet-5",
    }
    for provider, model in expected.items():
        root = PACKAGE / "results" / provider
        manifest = json.loads(
            (root / "run_manifest.json").read_text(encoding="utf-8")
        )
        if manifest.get("question_count") != 13:
            errors.append(f"{provider}: question count is not 13")
        if manifest.get("request_model") != model:
            errors.append(f"{provider}: request model differs")
        if manifest.get("response_models") != [model]:
            errors.append(f"{provider}: returned model differs")
        if manifest.get("held_out_test40_used") is not False:
            errors.append(f"{provider}: Test40 boundary differs")
        for key, value in EXPECTED_PROMPTS.items():
            if manifest.get(key) != value:
                errors.append(f"{provider}: {key} differs")
        for arm in ["direct", "rag"]:
            rows = read_jsonl(root / "answers" / f"{arm}.jsonl")
            qids = [row["question_id"] for row in rows]
            if len(rows) != 13 or len(set(qids)) != 13:
                errors.append(f"{provider}/{arm}: membership differs")
            if any(not str(row.get("answer") or "").strip() for row in rows):
                errors.append(f"{provider}/{arm}: empty answer")
            if any(
                row.get("finish_reason") not in {"STOP", "end_turn"}
                for row in rows
            ):
                errors.append(f"{provider}/{arm}: abnormal finish")
            if any(row.get("request_model") != model for row in rows):
                errors.append(f"{provider}/{arm}: mixed request models")
            if any(row.get("response_model") != model for row in rows):
                errors.append(f"{provider}/{arm}: mixed returned models")

    for order in ["canonical", "reverse"]:
        root = PACKAGE / "results/l3_v3" / order
        manifest = json.loads(
            (root / "run_manifest.json").read_text(encoding="utf-8")
        )
        if manifest.get("protocol_id") != "l3_gold_reference_v3_continuous":
            errors.append(f"{order}: wrong L3 protocol")
        if manifest.get("candidate_answer_count") != 52:
            errors.append(f"{order}: expected 52 L3 answers")
        if manifest.get("binary_metrics_enabled") is not False:
            errors.append(f"{order}: binary metrics enabled")
        if manifest.get("human_adequacy_labels_used") is not False:
            errors.append(f"{order}: human labels used")
        if manifest.get("claim_order") != order:
            errors.append(f"{order}: claim order differs")
        summaries = list(
            csv.DictReader((root / "system_summary.csv").open())
        )
        if len(summaries) != 4:
            errors.append(f"{order}: expected four system summaries")

    required_reports = [
        "SUMMARY.md",
        "system_scores.csv",
        "within_model_effects.csv",
        "claim_order_stability.csv",
        "cost_summary.csv",
    ]
    for name in required_reports:
        if not (PACKAGE / "final_report" / name).exists():
            errors.append(f"Missing report: {name}")
    report = {
        "protocol_id": "pfas_rag_stage4_multibase_dev13_v1",
        "status": "pass" if not errors else "fail",
        "errors": errors,
        "answer_count": 52,
        "l3_judge_call_count": 104,
        "held_out_test40_used": False,
    }
    (PACKAGE / "validation_report.json").write_text(
        json.dumps(report, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

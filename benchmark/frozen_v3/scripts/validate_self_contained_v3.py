from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import retrieval_metrics
import run_dev13_neutral_evidence_judge_v3 as neutral_judge
import run_dev13_soft_tags_v3
import runtime_helpers


ROOT = Path(__file__).resolve().parents[3]
V3 = ROOT / "benchmark/frozen_v3"
PROMOTED = V3 / "methods/promoted_reusable_artifacts.json"
GENERATION = (
    V3 / "results/dev13_verified_tags_v3_r2_confirmation_2026-07-26"
)
CANONICAL_RESULT = (
    V3 / "results/dev13_neutral_evidence_v3_2026-07-26"
)
CANONICAL_SCRIPTS = (
    "run_dev13_soft_tags_v3.py",
    "run_dev13_neutral_evidence_judge_v3.py",
    "run_dev13_budget_bge_llm_gpt51.py",
    "finalize_dev13_retrieval_budget_gpt51.py",
    "runtime_helpers.py",
    "retrieval_metrics.py",
)
FORBIDDEN_RUNTIME_REFERENCES = (
    "benchmark/frozen_v2",
    "benchmark/reports",
    "run_dev13_evidence_ledger_generation",
    "from build_contexts import",
    "from load_data import",
    "from run_recall_rate_test import",
    "from rag_app",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def tree_hashes(path: Path) -> dict[str, str]:
    return {
        str(file.relative_to(path)): sha256(file)
        for file in sorted(path.rglob("*"))
        if file.is_file()
    }


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def validate_runtime_references() -> None:
    errors = []
    for name in CANONICAL_SCRIPTS:
        path = V3 / "scripts" / name
        text = path.read_text(encoding="utf-8").lower()
        for forbidden in FORBIDDEN_RUNTIME_REFERENCES:
            if forbidden.lower() in text:
                errors.append(f"{name}: {forbidden}")
    if errors:
        raise RuntimeError(
            "Forbidden external runtime references:\n" + "\n".join(errors)
        )


def validate_method_paths() -> None:
    missing: list[str] = []

    def visit(value: object, source: Path) -> None:
        if isinstance(value, dict):
            for child in value.values():
                visit(child, source)
        elif isinstance(value, list):
            for child in value:
                visit(child, source)
        elif (
            isinstance(value, str)
            and value.startswith("benchmark/frozen_v3/")
            and not (ROOT / value).exists()
        ):
            missing.append(f"{source.name}: {value}")

    for path in sorted((V3 / "methods").glob("*.json")):
        visit(json.loads(path.read_text(encoding="utf-8")), path)
    if missing:
        raise RuntimeError(
            "Missing Frozen V3 method path references:\n"
            + "\n".join(missing)
        )


def validate_data_integrity() -> None:
    all_rows = read_csv(V3 / "input/questions_all53.csv")
    dev_rows = read_csv(V3 / "input/questions_dev13.csv")
    test_rows = read_csv(V3 / "input/questions_test40.csv")
    if (len(all_rows), len(dev_rows), len(test_rows)) != (53, 13, 40):
        raise RuntimeError("Expected 53/13/40 all/dev/test question counts")

    def indexed(rows: list[dict[str, str]], label: str) -> dict[str, dict]:
        qids = [row.get("question_id", "").strip() for row in rows]
        if any(not qid for qid in qids) or len(qids) != len(set(qids)):
            raise RuntimeError(f"Invalid or duplicate question IDs in {label}")
        if any(not row.get("question_text", "").strip() for row in rows):
            raise RuntimeError(f"Empty question text in {label}")
        return {row["question_id"]: row for row in rows}

    all_by_qid = indexed(all_rows, "all53")
    dev_by_qid = indexed(dev_rows, "dev13")
    test_by_qid = indexed(test_rows, "test40")
    if set(dev_by_qid).intersection(test_by_qid):
        raise RuntimeError("Dev13 and Test40 overlap")
    if set(dev_by_qid).union(test_by_qid) != set(all_by_qid):
        raise RuntimeError("Dev13 and Test40 do not partition all53")
    for qid, row in {**dev_by_qid, **test_by_qid}.items():
        if row["question_text"] != all_by_qid[qid]["question_text"]:
            raise RuntimeError(f"Question text mismatch across splits: {qid}")

    gold_rows = runtime_helpers.read_jsonl(
        V3 / "gold/chunk_based_gold.jsonl"
    )
    if len(gold_rows) != 249:
        raise RuntimeError(f"Expected 249 gold rows; found {len(gold_rows)}")
    evidence_ids = [str(row.get("evidence_id", "")) for row in gold_rows]
    if any(not value for value in evidence_ids):
        raise RuntimeError("Gold row missing evidence_id")
    if len(evidence_ids) != len(set(evidence_ids)):
        raise RuntimeError("Duplicate gold evidence_id")
    gold_by_qid = runtime_helpers.group_gold(gold_rows)
    if set(gold_by_qid) != set(all_by_qid):
        raise RuntimeError("Gold question membership does not match all53")
    if any(not rows for rows in gold_by_qid.values()):
        raise RuntimeError("Every question must have at least one gold row")

    count_rows = {
        row["question_id"]: row
        for row in read_csv(V3 / "gold/chunk_based_gold_per_question.csv")
    }
    if set(count_rows) != set(all_by_qid):
        raise RuntimeError("Per-question gold table membership mismatch")
    for qid, rows in gold_by_qid.items():
        evidence_counts = {
            "required_gold_count": sum(
                row.get("evidence_type") == "required_gold" for row in rows
            ),
            "optional_gold_count": sum(
                row.get("evidence_type") == "optional_gold" for row in rows
            ),
            "negative_gold_count": sum(
                row.get("evidence_type") == "negative_gold" for row in rows
            ),
        }
        if int(count_rows[qid]["gold_count"]) != len(rows):
            raise RuntimeError(f"Gold count mismatch for {qid}")
        for field, count in evidence_counts.items():
            if int(count_rows[qid][field]) != count:
                raise RuntimeError(f"{field} mismatch for {qid}")


def validate_author_review_record() -> None:
    record_path = V3 / "methods/author_review_record.json"
    record = json.loads(record_path.read_text(encoding="utf-8"))
    source_paths = {
        "questions": V3 / "input/questions_all53.csv",
        "gold": V3 / "gold/chunk_based_gold.jsonl",
    }
    register_paths = {
        "questions": V3 / "methods/question_author_review_register.csv",
        "gold": V3 / "methods/gold_author_review_register.csv",
    }
    for label, path in source_paths.items():
        expected = record["source_files"][label]
        if ROOT / expected["path"] != path or sha256(path) != expected["sha256"]:
            raise RuntimeError(f"Author-review source hash mismatch: {label}")
    for label, path in register_paths.items():
        expected = record["decision_registers"][label]
        if ROOT / expected["path"] != path or sha256(path) != expected["sha256"]:
            raise RuntimeError(f"Author-review register hash mismatch: {label}")

    question_rows = read_csv(register_paths["questions"])
    gold_rows = read_csv(register_paths["gold"])
    if len(question_rows) != 53 or len(gold_rows) != 249:
        raise RuntimeError("Author-review register count mismatch")
    if {
        row["author_review_decision"] for row in question_rows + gold_rows
    } != {"retained_after_project_author_review"}:
        raise RuntimeError("Author-review register contains unresolved decisions")
    if len({row["question_id"] for row in question_rows}) != 53:
        raise RuntimeError("Question author-review register membership mismatch")
    if len({row["evidence_id"] for row in gold_rows}) != 249:
        raise RuntimeError("Gold author-review register membership mismatch")


def validate_promoted_artifacts() -> None:
    manifest = json.loads(PROMOTED.read_text(encoding="utf-8"))
    if manifest["runtime_access_to_source_paths_required"]:
        raise RuntimeError("Promoted artifacts still require source access")
    for label, artifact in manifest["artifacts"].items():
        current = tree_hashes(ROOT / artifact["v3_path"])
        if current != artifact["copied_file_sha256"]:
            raise RuntimeError(f"Promoted artifact hash mismatch: {label}")


def validate_fixed_retrieval_input() -> None:
    questions, retrieval_rows = run_dev13_soft_tags_v3.load_inputs()
    if len(questions) != 13 or len(retrieval_rows) != 13:
        raise RuntimeError("Expected 13 Dev13 questions and retrieval rows")
    if any(
        len(row.get("retrieved_context", [])) != 10
        for row in retrieval_rows
    ):
        raise RuntimeError("Every fixed retrieval row must contain 10 chunks")
    budget_output = (
        V3 / "results/dev13_retrieval_budget_gpt51_2026-07-26/"
        "bge_llm_gpt51/retrieval_outputs/"
        "rag_outputs_bge_llm_gpt51_pool60_bge30_llm10_fullchunk.jsonl"
    )
    if run_dev13_soft_tags_v3.RETRIEVAL != budget_output:
        raise RuntimeError("Canonical generation does not use budget output")
    selector_prompt = run_dev13_soft_tags_v3.SELECTOR_PROMPT.read_text(
        encoding="utf-8"
    )
    selector_calls = runtime_helpers.read_jsonl(
        V3 / "results/dev13_retrieval_budget_gpt51_2026-07-26/"
        "bge_llm_gpt51/selector_calls.jsonl"
    )
    matched_calls = [
        row
        for row in selector_calls
        if row["config_name"]
        == "bge_llm_gpt51_pool60_bge30_llm10_fullchunk"
    ]
    if len(matched_calls) != 13:
        raise RuntimeError("Expected 13 canonical selector calls")
    if {row["system_prompt"] for row in matched_calls} != {selector_prompt}:
        raise RuntimeError("Canonical selector prompt does not match calls")
    experiment_manifest = json.loads(
        (
            V3
            / "results/dev13_retrieval_budget_gpt51_2026-07-26/"
            "bge_llm_gpt51/experiment_manifest.json"
        ).read_text(encoding="utf-8")
    )
    if experiment_manifest.get("selector_input") != "visible_question_only":
        raise RuntimeError("Canonical selector input is not question-only")
    forbidden_payload_fields = {
        "task_type",
        "answerability_type",
        "must_include",
        "must_not_claim",
    }
    for row in matched_calls:
        if forbidden_payload_fields.intersection(
            row.get("user_payload", {})
        ):
            raise RuntimeError(
                f"Selector payload exposes rubric fields for "
                f"{row['question_id']}"
            )


def validate_budget_metrics() -> None:
    run = (
        V3 / "results/dev13_retrieval_budget_gpt51_2026-07-26"
    )
    outputs = run / "bge_llm_gpt51/retrieval_outputs"
    stored = {
        (row["config_name"], row["question_id"]): row
        for row in read_csv(
            run / "bge_llm_gpt51/per_question_retrieval_metrics.csv"
        )
    }
    gold = runtime_helpers.group_gold(
        runtime_helpers.read_jsonl(V3 / "gold/chunk_based_gold.jsonl")
    )
    checked = 0
    for output_path in sorted(outputs.glob("*.jsonl")):
        for output in runtime_helpers.read_jsonl(output_path):
            config = output["retrieval_config_name"]
            qid = output["question_id"]
            context = output["retrieved_context"]
            final_k = int(output["top_k"])
            pool_k = int(output["retrieval_k"])
            recalculated = retrieval_metrics.eval_context(
                qid,
                gold.get(qid, []),
                context,
                config,
                "bge_llm_cascade",
                final_k,
                pool_k,
                0,
            )
            expected = stored[(config, qid)]
            metric_fields = (
                "required_gold_recall@5",
                "required_gold_recall@10",
                "required_gold_recall@20",
                "required_gold_recall@full_context",
                "gold_doc_recall@10",
                "gold_doc_recall@20",
                "gold_doc_recall@full_context",
                "MRR_required_gold",
                "required_gold_retrieved@10",
                "required_gold_retrieved@20",
                "required_gold_retrieved@full_context",
            )
            comparisons = {
                f"final_{field}": recalculated[field]
                for field in metric_fields
            }
            for field, actual in comparisons.items():
                if abs(float(expected[field]) - float(actual)) > 1e-12:
                    raise RuntimeError(
                        f"Metric mismatch {config} {qid} {field}"
                    )
            checked += 1
    if checked != 39:
        raise RuntimeError(f"Expected 39 budget rows; checked {checked}")

    local = run / "local_hybrid_bge"
    local_stored = {
        (row["config_name"], row["question_id"]): row
        for row in read_csv(local / "per_question_retrieval_metrics.csv")
    }
    local_checked = 0
    for output_path in sorted((local / "retrieval_outputs").glob("*.jsonl")):
        for output in runtime_helpers.read_jsonl(output_path):
            config = output["retrieval_config_name"]
            qid = output["question_id"]
            context = output["retrieved_context"]
            recalculated = retrieval_metrics.eval_context(
                qid,
                gold.get(qid, []),
                context,
                config,
                str(output.get("retrieval_method", "")),
                int(output["top_k"]),
                int(output["retrieval_k"]),
                int(output.get("context_window") or 0),
            )
            expected = local_stored[(config, qid)]
            for field in (
                "required_gold_recall@5",
                "required_gold_recall@10",
                "required_gold_recall@20",
                "required_gold_recall@full_context",
                "gold_doc_recall@10",
                "gold_doc_recall@20",
                "gold_doc_recall@full_context",
                "MRR_required_gold",
            ):
                stored_field = f"final_{field}"
                if abs(
                    float(expected[stored_field])
                    - float(recalculated[field])
                ) > 1e-12:
                    raise RuntimeError(
                        f"Promoted metric mismatch {config} {qid} {field}"
                    )
            local_checked += 1
    if local_checked != 78:
        raise RuntimeError(
            f"Expected 78 promoted Hybrid/BGE rows; checked {local_checked}"
        )

    negative_rows = read_csv(run / "negative_gold_retrieval_per_question.csv")
    if len(negative_rows) != 117:
        raise RuntimeError("Expected 117 negative-gold question-config rows")
    negative_applicable = {
        row["question_id"]
        for row in negative_rows
        if int(row["negative_gold_count"]) > 0
    }
    if len(negative_applicable) != 6:
        raise RuntimeError("Expected six negative-gold-applicable Dev questions")


def validate_verified_tag_interface() -> dict:
    generation_manifest = json.loads(
        (GENERATION / "generation_manifest.json").read_text(
            encoding="utf-8"
        )
    )
    if generation_manifest["free_text_advisory_fields_exposed"]:
        raise RuntimeError("Generation manifest exposes free-text advice")
    if generation_manifest["protocol"] != (
        "benchmark/frozen_v3/methods/"
        "dev13_verified_tags_v3_protocol.json"
    ):
        raise RuntimeError("Canonical generation points to the wrong protocol")
    if generation_manifest["matched_untagged_generated"]:
        raise RuntimeError("Canonical generation unexpectedly includes untagged")
    if not generation_manifest["matched_direct_generated"]:
        raise RuntimeError("Canonical generation is missing matched Direct")

    forbidden = {"allowed_use", "avoid_use", "omit_details"}
    expected_tag_keys = {
        "candidate_id",
        "confidence",
        "detail_policy",
        "eligibility",
        "evidence_polarity",
        "exact_support",
        "exact_support_validated",
        "supports_components",
    }
    tag_rows = runtime_helpers.read_jsonl(
        GENERATION / "tags/tag_results.jsonl"
    )
    answer_rows = runtime_helpers.read_jsonl(
        GENERATION / "answers/tagged_rag_gpt51.jsonl"
    )
    direct_rows = runtime_helpers.read_jsonl(
        GENERATION / "answers/matched_direct_gpt51.jsonl"
    )
    if not (len(tag_rows) == len(answer_rows) == len(direct_rows) == 13):
        raise RuntimeError("Canonical generation must contain 13 rows per system")
    expected_qids = [
        row["question_id"]
        for row in runtime_helpers.read_csv(V3 / "input/questions_dev13.csv")
    ]
    for label, rows in (
        ("tag", tag_rows),
        ("tagged answer", answer_rows),
        ("Direct answer", direct_rows),
    ):
        if [row["question_id"] for row in rows] != expected_qids:
            raise RuntimeError(f"{label} question order or membership mismatch")
    retrieval_by_qid = {
        row["question_id"]: row
        for row in runtime_helpers.read_jsonl(
            run_dev13_soft_tags_v3.RETRIEVAL
        )
    }
    tags_by_qid = {row["question_id"]: row for row in tag_rows}
    for answer in answer_rows:
        qid = answer["question_id"]
        expected_context = retrieval_by_qid[qid]["retrieved_context"]
        if runtime_helpers.payload_sha256(
            answer.get("retrieved_context", [])
        ) != runtime_helpers.payload_sha256(expected_context):
            raise RuntimeError(
                f"Tagged answer context differs from fixed retrieval for {qid}"
            )
        if answer.get("soft_eligibility_tags") != (
            tags_by_qid[qid]["validated_chunk_tags"]
        ):
            raise RuntimeError(
                f"Tagged answer tags differ from tagger output for {qid}"
            )
    questions = runtime_helpers.read_csv(
        V3 / "input/questions_dev13.csv"
    )
    neutral_judge.validate_inputs(
        questions,
        answer_rows,
        None,
        direct_rows,
    )
    tag_prompt = run_dev13_soft_tags_v3.TAG_PROMPT.read_text(
        encoding="utf-8"
    )
    for row in tag_rows:
        context = retrieval_by_qid[row["question_id"]]["retrieved_context"]
        if (
            len(row["validated_chunk_tags"]) != len(context)
            or len(context) != 10
        ):
            raise RuntimeError(
                f"Tag/context count mismatch for {row['question_id']}"
            )
        for tag, hit in zip(row["validated_chunk_tags"], context):
            if set(tag) != expected_tag_keys:
                raise RuntimeError(
                    f"Unexpected validated tag schema for {row['question_id']}"
                )
            if forbidden.intersection(tag):
                raise RuntimeError(
                    f"Free-text tag field retained for {row['question_id']}"
                )
            if bool(tag["exact_support"]) != bool(
                tag["exact_support_validated"]
            ):
                raise RuntimeError(
                    f"Excerpt validation flag mismatch for {row['question_id']}"
                )
            if tag["exact_support"] and (
                run_dev13_soft_tags_v3.normalized_text(
                    tag["exact_support"]
                )
                not in run_dev13_soft_tags_v3.normalized_text(
                    hit.get("text", "")
                )
            ):
                raise RuntimeError(
                    f"Non-verbatim excerpt retained for {row['question_id']}"
                )
        payload = {
            "question": row["question_text"],
            "candidates": [
                {
                    "candidate_id": index,
                    "source": hit.get("citation") or hit.get("doc_id", ""),
                    "section": hit.get("section", ""),
                    "text": hit.get("text", ""),
                }
                for index, hit in enumerate(context, start=1)
            ],
        }
        request = {
            "model": run_dev13_soft_tags_v3.MODEL,
            "response_format": {"type": "json_object"},
            "temperature": 0,
            "messages": [
                {"role": "system", "content": tag_prompt},
                {
                    "role": "user",
                    "content": json.dumps(payload, ensure_ascii=False),
                },
            ],
        }
        if row.get("tag_prompt_payload_sha256") != (
            runtime_helpers.payload_sha256(payload)
        ):
            raise RuntimeError(
                f"Tag input payload fingerprint mismatch for "
                f"{row['question_id']}"
            )
        if row.get("tag_execution_sha256") != (
            runtime_helpers.payload_sha256(request)
        ):
            raise RuntimeError(
                f"Tag execution fingerprint mismatch for {row['question_id']}"
            )

    judge_manifest = json.loads(
        (CANONICAL_RESULT / "evaluation_manifest.json").read_text(
            encoding="utf-8"
        )
    )
    if judge_manifest["untagged_comparison_included"]:
        raise RuntimeError("Canonical judge includes untagged comparison")
    summaries = judge_manifest["summaries"]
    if len(summaries) != 1:
        raise RuntimeError("Canonical judge must contain one comparison")
    summary = summaries[0]
    if summary["comparison"] != "tagged_vs_matched_direct":
        raise RuntimeError("Canonical comparison is not tagged versus Direct")
    if int(summary["question_count"]) != 13:
        raise RuntimeError("Canonical summary does not contain 13 questions")
    if int(summary["judge_repeats"]) != 3:
        raise RuntimeError("Canonical summary does not contain three repeats")

    per_question = read_csv(CANONICAL_RESULT / "results/per_question.csv")
    if len(per_question) != 13:
        raise RuntimeError("Canonical per-question result must contain 13 rows")
    calculated = {
        "tagged_wins": sum(row["winner"] == "tagged" for row in per_question),
        "opponent_wins": sum(row["winner"] == "direct" for row in per_question),
        "ties": sum(row["winner"] == "tie" for row in per_question),
    }
    for field, value in calculated.items():
        if int(summary[field]) != value:
            raise RuntimeError(f"Canonical summary mismatch for {field}")
    mean_score = sum(
        float(row["weighted_tagged_score"]) for row in per_question
    ) / len(per_question)
    if abs(float(summary["mean_weighted_tagged_score"]) - mean_score) > 1e-12:
        raise RuntimeError("Canonical mean weighted score mismatch")

    prompt = neutral_judge.JUDGE_PROMPT.read_text(encoding="utf-8")
    for repeat in range(1, 4):
        run_dir = CANONICAL_RESULT / f"judge/run{repeat}"
        model_payloads = runtime_helpers.read_jsonl(
            run_dir / "model_payloads.jsonl"
        )
        envelopes = runtime_helpers.read_jsonl(
            run_dir / "local_request_envelopes.jsonl"
        )
        mappings = runtime_helpers.read_jsonl(run_dir / "blind_mapping.jsonl")
        results = runtime_helpers.read_jsonl(run_dir / "judge_results.jsonl")
        if not (
            len(model_payloads)
            == len(envelopes)
            == len(mappings)
            == len(results)
            == 26
        ):
            raise RuntimeError(
                f"Expected 26 payload/mapping/result rows in repeat {repeat}"
            )
        if model_payloads != [row["model_payload"] for row in envelopes]:
            raise RuntimeError(
                f"Model payload and local envelope mismatch in repeat {repeat}"
            )
        payload_by_id = {row["payload_id"]: row for row in envelopes}
        result_by_id = {row["payload_id"]: row for row in results}
        if (
            len(payload_by_id) != 26
            or len(result_by_id) != 26
            or {row["payload_id"] for row in mappings}
            != set(payload_by_id)
            or set(result_by_id) != set(payload_by_id)
        ):
            raise RuntimeError(f"Judge payload IDs mismatch in repeat {repeat}")
        for mapping in mappings:
            payload = payload_by_id[mapping["payload_id"]]
            result_row = result_by_id[mapping["payload_id"]]
            serialized = json.dumps(
                payload["model_payload"],
                ensure_ascii=False,
            )
            for forbidden in (
                mapping["payload_id"],
                mapping["question_id"],
                "tagged_vs_",
                '"task_type"',
                '"answerability_type"',
            ):
                if forbidden in serialized:
                    raise RuntimeError(
                        f"Judge model payload leak: {forbidden}"
                    )
            if neutral_judge.CITATION_PATTERN.search(serialized):
                raise RuntimeError("Judge model payload retains a citation")
            expected_fingerprint = runtime_helpers.payload_sha256(
                {
                    "model": neutral_judge.MODEL,
                    "temperature": 0,
                    "prompt": prompt,
                    "payload": payload["model_payload"],
                }
            )
            if (
                result_row.get("judge_execution_sha256")
                != expected_fingerprint
            ):
                raise RuntimeError(
                    f"Judge execution fingerprint mismatch: "
                    f"{mapping['payload_id']}"
                )
            neutral_judge.parse_judge_result(
                mapping,
                result_row["judge_result"],
            )
    return summary


def main() -> None:
    validate_data_integrity()
    validate_author_review_record()
    validate_runtime_references()
    validate_method_paths()
    validate_promoted_artifacts()
    validate_fixed_retrieval_input()
    validate_budget_metrics()
    summary = validate_verified_tag_interface()
    print("SELF-CONTAINED V3 VALIDATION PASS")
    print("Canonical runtime imports only V3-local benchmark modules.")
    print("Method path references: all Frozen V3 targets exist.")
    print("Project-author review: 53 questions and 249 gold decisions verified.")
    print("Promoted artifacts: 2 hash-verified internal copies.")
    print("Fixed retrieval input: 13 questions x 10 chunks.")
    print(
        "Budget metrics: 39 BGE-LLM and 78 promoted Hybrid/BGE rows "
        "reproduced."
    )
    print("Negative-gold retrieval: 117 rows, six applicable questions.")
    print("Verified tag interface: no answer-facing free-text advice.")
    print(
        "Canonical Dev13 result: "
        f"{summary['tagged_wins']}/"
        f"{summary['opponent_wins']}/"
        f"{summary['ties']} (V3/Direct/tie), three mirrored "
        "temperature-zero re-samples."
    )


if __name__ == "__main__":
    main()

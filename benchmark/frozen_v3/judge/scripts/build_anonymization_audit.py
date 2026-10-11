from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

import judge_common as common


SLOTS = ("X", "Y", "Z")
PROHIBITED_PATTERNS = {
    "citation_marker": re.compile(r"\[C\d+\]", re.IGNORECASE),
    **common.IDENTITY_LEAK_PATTERNS,
}


def portable_path(path: Path) -> str:
    try:
        return str(path.relative_to(common.ROOT))
    except ValueError:
        return str(path)


def parse_system(value: str) -> tuple[str, Path]:
    label, separator, path = value.partition(",")
    if not separator or not label or not path:
        raise ValueError("--system must be LABEL,ANSWER_FILE")
    return label, Path(path).expanduser().resolve()


def assignment(qid: str, systems: list[str], seed: str) -> dict[str, str]:
    ranked = sorted(
        systems,
        key=lambda system: hashlib.sha256(
            f"{seed}::{qid}::{system}".encode()
        ).hexdigest(),
    )
    return dict(zip(SLOTS, ranked, strict=True))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--system", action="append", required=True)
    parser.add_argument("--questions", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--seed", default="anonymization-audit-2026-07-28")
    args = parser.parse_args()

    systems = dict(parse_system(value) for value in args.system)
    if sorted(systems) != ["bge", "bge_llm", "hybrid"]:
        raise ValueError("Audit requires exactly hybrid, bge, and bge_llm")
    answer_maps = {
        label: common.by_question(common.read_jsonl(path))
        for label, path in systems.items()
    }
    questions = common.read_csv(Path(args.questions))

    local_keys = []
    model_payloads = []
    deterministic_findings = []
    for index, question in enumerate(questions, start=1):
        qid = str(question["question_id"])
        audit_id = f"A{index:02d}"
        slot_to_system = assignment(qid, sorted(systems), args.seed)
        answers: dict[str, str] = {}
        for slot, system in slot_to_system.items():
            raw = str(answer_maps[system][qid]["answer"])
            stripped = common.strip_citations(raw)
            answers[slot] = stripped
            for name, pattern in PROHIBITED_PATTERNS.items():
                matches = pattern.findall(stripped)
                if matches:
                    deterministic_findings.append(
                        {
                            "audit_id": audit_id,
                            "slot": slot,
                            "pattern": name,
                            "match_count": len(matches),
                        }
                    )
        local_keys.append(
            {
                "audit_id": audit_id,
                "question_id": qid,
                "slot_to_system": slot_to_system,
            }
        )
        model_payloads.append(
            {
                "audit_id": audit_id,
                "question": question["question_text"],
                "anonymous_answers": answers,
            }
        )

    out = Path(args.out).expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)
    common.write_jsonl(out / "local_answer_key.jsonl", local_keys)
    common.write_jsonl(out / "model_payloads.jsonl", model_payloads)
    common.write_json(
        out / "deterministic_leakage_scan.json",
        {
            "status": (
                "passed" if not deterministic_findings else "failed"
            ),
            "question_count": len(questions),
            "answer_count": len(questions) * 3,
            "citation_stripped": True,
            "standalone_hybrid_excluded": (
                "The word 'hybrid' is valid PFAS-domain terminology and is "
                "only flagged when paired with an explicit system term."
            ),
            "findings": deterministic_findings,
        },
    )
    prompt = (
        common.JUDGE
        / "prompts/anonymization_identity_audit_v1.txt"
    ).read_text(encoding="utf-8")
    request = (
        prompt
        + "\n\nAudit items:\n"
        + json.dumps(model_payloads, ensure_ascii=False)
        + "\n"
    )
    (out / "sonnet_audit_request.txt").write_text(
        request,
        encoding="utf-8",
    )
    common.write_json(
        out / "build_manifest.json",
        {
            "questions_sha256": common.sha256(Path(args.questions)),
            "answer_files": {
                label: {
                    "path": portable_path(path),
                    "sha256": common.sha256(path),
                }
                for label, path in systems.items()
            },
            "seed": args.seed,
            "ground_truth_not_in_model_payload": True,
            "model_payload_sha256": common.sha256(
                out / "model_payloads.jsonl"
            ),
            "request_sha256": common.sha256(
                out / "sonnet_audit_request.txt"
            ),
        },
    )


if __name__ == "__main__":
    main()

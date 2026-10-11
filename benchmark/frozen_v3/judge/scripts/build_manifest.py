from __future__ import annotations

import hashlib
import json
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
V3 = PACKAGE.parent
ROOT = V3.parents[1]
MANIFEST = PACKAGE / "freeze_manifest.json"
EXTERNAL_INPUTS = (
    ROOT / "benchmark/frozen_v3/input/questions_all53.csv",
    ROOT / "benchmark/frozen_v3/input/questions_dev13.csv",
    ROOT / "benchmark/frozen_v3/input/questions_test40.csv",
    ROOT / "benchmark/frozen_v3/gold/chunk_based_gold.jsonl",
    ROOT / "benchmark/frozen_v3/prompts/evaluation/soft_eligibility_tagger_v3.txt",
    ROOT / "benchmark/frozen_v3/prompts/evaluation/rag_answer_prompt_soft_tags_v3.txt",
    ROOT / "benchmark/frozen_v3/prompts/retrieval/bge_llm_selector_v3.txt",
    ROOT
    / (
        "benchmark/frozen_v3/results/dev13_retrieval_budget_gpt51_2026-07-26/"
        "local_hybrid_bge/retrieval_outputs/"
        "rag_outputs_hybrid_top10_pool60_win0.jsonl"
    ),
    ROOT
    / (
        "benchmark/frozen_v3/results/dev13_retrieval_budget_gpt51_2026-07-26/"
        "local_hybrid_bge/retrieval_outputs/"
        "rag_outputs_bge_base_top10_pool60_nodoccap.jsonl"
    ),
    ROOT
    / (
        "benchmark/frozen_v3/results/dev13_retrieval_budget_gpt51_2026-07-26/"
        "bge_llm_gpt51/retrieval_outputs/"
        "rag_outputs_bge_llm_gpt51_pool60_bge30_llm10_fullchunk.jsonl"
    ),
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def included_files() -> list[Path]:
    return sorted(
        path
        for path in PACKAGE.rglob("*")
        if path.is_file()
        and path != MANIFEST
        and "__pycache__" not in path.parts
        and path.name != ".DS_Store"
    )


def main() -> None:
    value = {
        "protocol_id": "pfas_rag_frozen_judge_2026-07-28",
        "freeze_date": "2026-07-28",
        "package_root": str(PACKAGE.relative_to(ROOT)),
        "package_files": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in included_files()
        },
        "external_canonical_inputs": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in EXTERNAL_INPUTS
        },
    }
    MANIFEST.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()

from __future__ import annotations

from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
V3 = PACKAGE.parent
ROOT = V3.parents[1]
OUTPUT = PACKAGE / "reviews/final_claude_review_request.md"

INCLUDED = (
    PACKAGE / "README.md",
    PACKAGE / "methods/protocol.json",
    PACKAGE / "methods/FREEZE_RECORD.md",
    PACKAGE / "audits/local/LOCAL_AUDIT.md",
    PACKAGE / "audits/anonymization/deterministic_leakage_scan.json",
    PACKAGE / "audits/anonymization/scored/summary.json",
    PACKAGE / "calibration/dev13/l1_retrieval_summary.csv",
    PACKAGE
    / "calibration/dev13/l2v2_10000_bootstrap/criterion_abilities.csv",
    PACKAGE
    / "calibration/dev13/l2v2_10000_bootstrap/"
    "equal_weight_composite_secondary.csv",
    PACKAGE
    / "calibration/dev13/l2v2_10000_bootstrap/fit_manifest.json",
    PACKAGE
    / "calibration/dev13/l2v2_10000_bootstrap/mirrored_agreement.csv",
    PACKAGE
    / "calibration/dev13/l2v2_10000_bootstrap/position_bias.csv",
    PACKAGE
    / "calibration/dev13/l2v2_10000_bootstrap/raw_vote_counts.csv",
    PACKAGE / "freeze_manifest.json",
    PACKAGE / "environment/python-version.txt",
    PACKAGE / "environment/requirements-lock.txt",
    *sorted((PACKAGE / "prompts").glob("*.txt")),
    *sorted((PACKAGE / "scripts").glob("*.py")),
    *sorted((PACKAGE / "tests").glob("*.py")),
)

INSTRUCTIONS = """# Independent final-freeze review request

Act as an independent senior reviewer of a literature-grounded PFAS RAG
benchmark. Review the complete frozen judge materials below. Do not assume the
local audit is correct.

The intended design is:

- L1: deterministic retrieval evaluation for Hybrid, BGE, and BGE-LLM.
- L1.5: claim-level citation-support sanity check for RAG answers.
- L2 V2: citation-blind pairwise answer quality with four independent
  criteria, exactly two mirrored orders, raw A/B/tie votes, criterion-specific
  Davidson fits, and 10,000 question-clustered percentile bootstrap attempts.
- Test40 must remain held out from method development.

Review all of the following:

1. statistical validity, Davidson likelihood, tie handling, graph
   identifiability, clustered bootstrap, failed-fit handling, and uncertainty;
2. prompt alignment, information supplied to each judge, leakage, gold bias,
   specificity/verbosity bias, abstention, and citation blindness;
3. L1 and L1.5 denominators and edge cases;
4. schema validation, exact question membership, resume/overwrite behavior,
   error handling, token/cost/latency records, and returned-model enforcement;
5. manifest completeness, external dependencies, portability, held-out
   boundaries, and whether the stored Dev13 confirmation supports freezing;
6. the anonymization audit and whether its interpretation is appropriately
   limited.

Reconstruct in your own words exactly what information L1, L1.5, and L2
receive. Classify every finding as BLOCKING, MAJOR, MINOR, or
DOCUMENTATION_ONLY. Give file/function references. Distinguish required
pre-freeze fixes from optional future improvements.

End with exactly one verdict:

- FREEZE_APPROVED
- FREEZE_APPROVED_WITH_DOCUMENTATION_CHANGES
- FREEZE_NOT_APPROVED

Do not rewrite the system. Focus on correctness, reproducibility, and whether
this exact package may be frozen before the first Test40 run.
"""


def fence_for(path: Path) -> str:
    return "python" if path.suffix == ".py" else path.suffix.lstrip(".")


def main() -> None:
    sections = [INSTRUCTIONS]
    for path in INCLUDED:
        if not path.is_file():
            raise FileNotFoundError(path)
        sections.extend(
            [
                f"\n## File: {path.relative_to(ROOT)}\n",
                f"```{fence_for(path)}\n",
                path.read_text(encoding="utf-8"),
                "\n```\n",
            ]
        )
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("".join(sections), encoding="utf-8")


if __name__ == "__main__":
    main()

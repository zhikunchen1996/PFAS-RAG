# Benchmark Release

This directory contains the frozen question benchmark, formal executions, and
the separate professional-review experiment reported in the manuscript.

## Active inputs and methods

`frozen_v3/` is the immutable source for:

- 53 researcher-intent questions split into 13 development and 40 test items;
- 249 human-audited, non-exhaustive chunk-based gold records;
- Hybrid, BGE, and BGE-LLM retrieval configurations;
- the shared evidence-role tagger and answer-generation interfaces; and
- deterministic retrieval and citation-support evaluation code.

The active final-answer protocol is continuous reference-claim coverage. L2
pairwise files retained inside sealed packages are historical and are not part
of the reported main analysis.

## Formal runs

| Package | Role |
| --- | --- |
| `runs/l3_gold_reference_dev13_v3_continuous/` | Frozen continuous final-answer method |
| `runs/l3_three_repeat_dev13_v2_gpt51judge/` | Three-repeat GPT-5.1 aggregation policy |
| `runs/l3_gold_reference_test40_v1/` | Candidate-blind test reference ledgers |
| `runs/test40_formal_v1_1/` | Hybrid, BGE, and BGE-LLM formal test |
| `runs/test40_multibase_direct_rag_v1/` | Matched three-base-model Direct/PFAS RAG test |
| `runs/test40_multibase_l15_v1/` | Cross-model RAG citation-support analysis |

Development packages retained in `runs/` provide the frozen reference and
model-comparison provenance. They are not additional test sets.

## Professional review

The ten-task method and formal run are:

- `review_tasks/professional_review_v3_formal_v1/`
- `review_tasks/runs/professional_review_v3_formal_v1/`
- `review_tasks/runs/professional_review_human_expert_v1/`

The first package contains tasks, anchor-review exclusions, prompts, schemas,
and the method freeze. The second contains the PFAS RAG, Web Search, and Direct
formal outputs. The third contains the deidentified blinded expert assessment.

Some immutable package READMEs preserve the status recorded before paid
execution. In particular, `runs/test40_formal_v1_1/README.md` is part of its
pre-run manifest. Current completion status and results are recorded under each
package's `results/` directory and in `docs/study_release_2026-09-02.md`.

## Supplementary analyses

Only manuscript-facing derived analyses remain under `ablations/`:

- `dev13_dense_bm25_only_v1/`: lexical/dense component comparison.
- `test40_retrieval_answer_cost_v2/`: retrieval-answer and resource analysis.
- `test40_retrieval_metric_answer_correlation_v1/`: retrieval-answer
  association analysis.

These analyses do not modify the frozen test results.

## Publication boundary

Independent historical experiments are excluded from the publication package.
Older-named inputs still required by formal validators remain at their original
paths. Sealed package records are preserved without altering their hashes.

## Validation

From the repository root:

```bash
.venv/bin/python benchmark/validate_active_layout.py
.venv/bin/python benchmark/frozen_v3/scripts/build_freeze_manifest.py --verify
.venv/bin/python benchmark/frozen_v3/judge/scripts/validate_frozen_judge.py
.venv/bin/python benchmark/runs/l3_gold_reference_test40_v1/scripts/validate_reference_freeze.py
```

The complete command sequence is in `REPRODUCIBILITY.md`.

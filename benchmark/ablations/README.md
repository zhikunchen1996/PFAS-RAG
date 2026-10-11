# Supplementary Analyses

This directory contains the three active manuscript-facing analyses derived
from frozen Dev13 or Test40 outputs:

- `dev13_dense_bm25_only_v1/`: dense-only, BM25-only, and Hybrid retrieval
  component comparison on the development set;
- `test40_retrieval_answer_cost_v2/`: retrieval-answer coupling, failure-stage,
  token, and cost summaries; and
- `test40_retrieval_metric_answer_correlation_v1/`: association of MRR,
  required-gold recall, and gold-document recall with final-answer quality.

These packages make no model calls and do not change frozen questions, gold,
retrieval outputs, answers, judgments, or main metrics. Each package contains
its own source hashes, derived outputs, validation script, and tests.

Superseded supplementary analyses are under
`benchmark/archive/2026-09-02_supplementary_development/` and must not be
pooled with the active packages.

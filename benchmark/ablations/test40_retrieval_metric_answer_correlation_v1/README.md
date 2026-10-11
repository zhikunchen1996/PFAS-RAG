# Test40 Retrieval-Metric–Answer Correlation V1

This post hoc analysis compares how three frozen retrieval diagnostics relate
to frozen final-answer quality on the 38 Test40 questions with at least one
required-gold chunk:

- `MRR_required_gold`;
- `required_gold_recall@10`; and
- `gold_doc_recall@10`.

Each of the three retrieval systems contributes one observation per applicable
question, giving 114 question-system observations. Spearman correlations and
their pairwise differences use 10,000 bootstrap replicates sampled by question,
retaining all three system rows whenever a question is sampled. A separate
diagnostic asks whether MRR remains associated with answer quality among the 32
observations for which all required gold was retrieved.

Two-sided significance tests regress ranked answer quality on each ranked
retrieval metric with question-clustered CR1 standard errors and 37 cluster
degrees of freedom. Exact unadjusted `P` values are shown in Figure 3d;
Benjamini-Hochberg adjusted values across the three exploratory tests and 95%
question-cluster bootstrap intervals are retained in the result table and SI.

The package makes no API calls and does not alter any frozen question, gold
record, retrieval output, answer, judgment, model, prompt, or metric. It reads
the same frozen inputs through the V2 case-construction implementation so the
existing required-gold correlation is reproduced exactly, and records both the
source script and its generated joined table in this package manifest.

## Run

```bash
.venv/bin/python \
  benchmark/ablations/test40_retrieval_metric_answer_correlation_v1/scripts/run_analysis.py
.venv/bin/python \
  benchmark/ablations/test40_retrieval_metric_answer_correlation_v1/scripts/validate_analysis.py
.venv/bin/python -m unittest discover \
  -s benchmark/ablations/test40_retrieval_metric_answer_correlation_v1/tests -v
```

## Interpretation

The analysis tests, rather than assumes, that MRR is the most consequential
retrieval metric. Correlation magnitudes are descriptive associations. The
three retrieval metrics are themselves correlated, the gold is non-exhaustive,
and the repeated system observations within a question are not independent.
Pairwise bootstrap intervals must therefore accompany comparisons among the
three coefficients. None of the three associations reached `P < 0.05`; the
results are reported as descriptive positive trends rather than statistically
established effects.

“Full required-gold retrieval” means that every predefined required-gold chunk
was present in a system's final top-10 context. It does not mean that systems
received identical contexts: non-gold chunks, ordering, evidence-role tags,
and valid evidence outside the non-exhaustive gold can differ.

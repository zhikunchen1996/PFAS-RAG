# Test40 Retrieval–Answer and Cost Analysis V2

This package implements three secondary analyses requested for the manuscript:

1. retrieval–answer coupling;
2. deterministic failure-path classification; and
3. cost–performance analysis.

It makes no API calls and does not alter the frozen Test40 questions, gold,
retrieval outputs, answers, or judgments. The analyses are post hoc and should
be described as descriptive/explanatory rather than confirmatory ablations.

## Run

```bash
.venv/bin/python benchmark/ablations/test40_retrieval_answer_cost_v2/scripts/run_analysis.py
.venv/bin/python benchmark/ablations/test40_retrieval_answer_cost_v2/scripts/validate_analysis.py
.venv/bin/python -m unittest discover \
  -s benchmark/ablations/test40_retrieval_answer_cost_v2/tests -v
```

`run_analysis.py` also builds the recommended 2 x 2 main-text Figure 3 and the
2 x 2 SI diagnostic/resource figure. See `MANUSCRIPT_INTEGRATION.md` for the
proposed panel order, captions, and ready-to-insert Results text.

## Outputs

- `results/analysis_cases.csv`: one joined record per question and RAG system.
- `results/retrieval_answer_coupling_*.csv`: the raw Spearman association,
  question-cluster bootstrap confidence intervals, retrieval-completeness
  group summaries, and paired BGE-LLM contrasts.
- `results/failure_path_*.csv`: full deterministic classification, aggregate
  counts, and representative cases.
- `results/cost_performance_*.csv`: deployment-stage and cross-model generation
  costs alongside frozen L3 scores.
- `results/RESULTS_SUMMARY.md`: manuscript-facing numerical summary and limits.
- `figures/`: publication-style PNG, PDF, and SVG figures.
- `manifest.json`: hashes of the protocol, scripts, frozen source artifacts,
  and generated outputs.

## Interpretation Limits

Gold is human-audited but non-exhaustive. A gold miss therefore identifies a
benchmark-referenced retrieval failure, not proof that the context contains no
scientifically useful evidence. “Used” means that the answer visibly cites the
retrieved required-gold chunk. This is an auditable proxy and can underestimate
uncited evidence use. Cost excludes local compute and all evaluation judges.
The correlation uses the original continuous scores without question-level
centering. Its percentile interval resamples the 38 questions as clusters,
keeping all three system observations for each sampled question together. The
CSV retains a naive unclustered p-value only as an audit field; it must not be
used for inferential manuscript claims.

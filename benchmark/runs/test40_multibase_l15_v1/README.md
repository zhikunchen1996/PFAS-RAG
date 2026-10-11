# Test40 Multibase Citation-Support Analysis V1

Status: complete supplementary analysis for manuscript Results Section 3.3

This package applies the frozen L1.5 citation-support sanity check to the
existing GPT-5.1, Gemini 3.1 Pro Preview, and Claude Sonnet 5 RAG answers from:

```text
benchmark/runs/test40_multibase_direct_rag_v1
```

No answer is regenerated. Direct answers are not evaluated because they do
not receive retrieved chunks or use chunk citations. Each judgment receives
only the visible question, one existing RAG answer with its `[C#]` markers,
and the ten complete original chunks supplied to that answer.

The analysis uses the frozen prompt:

```text
benchmark/frozen_v3/judge/prompts/l15_claim_citation_support_v2.txt
```

The principal descriptive outputs are:

- supported cited-claim rate;
- mean question-level citation-support rate;
- unsupported and contradicted cited-claim counts; and
- uncited source-dependent claim count.

L1.5 is supplementary. It measures observable citation-grounding behavior,
not retrieval recall or overall answer completeness, and does not replace L3.

## Results

| RAG base model | Supported cited-claim rate | Mean question-level support | Unsupported | Contradicted |
|---|---:|---:|---:|---:|
| GPT-5.1 | 0.995 | 0.994 | 4 | 0 |
| Gemini 3.1 Pro Preview | 0.984 | 0.986 | 5 | 0 |
| Claude Sonnet 5 | 0.970 | 0.968 | 11 | 3 |

All 120 valid judgments passed request-hash and model-snapshot validation.
One schema-invalid GPT-5.1 judgment was rejected and replaced using the same
request hash. The 120 valid calls used 999,744 tracked tokens and cost USD
5.13047125. The estimated bill including the rejected response is approximately
USD 5.18.

See `RESULTS_SUMMARY.md` and `EXECUTION_ACCOUNTING.md` for the manuscript
interpretation and execution record.

## Commands

```bash
.venv/bin/python benchmark/runs/test40_multibase_l15_v1/scripts/run_l15.py \
  --dry-run

.venv/bin/python benchmark/runs/test40_multibase_l15_v1/scripts/run_l15.py \
  --run --workers 4

.venv/bin/python benchmark/runs/test40_multibase_l15_v1/scripts/run_l15.py \
  --run --workers 4 --resume

.venv/bin/python benchmark/runs/test40_multibase_l15_v1/scripts/run_l15.py \
  --validate
```

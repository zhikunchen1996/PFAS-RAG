# Test40 matched Direct versus RAG multibase experiment

This package applies the Dev13-frozen matched Direct/RAG protocol to Test40
for three high-capability proprietary base models:

- GPT-5.1
- Gemini 3.1 Pro Preview
- Claude Sonnet 5

Each model generates one Direct answer and one BGE-LLM RAG answer for every
question. Direct receives no retrieval, gold, citations, or web search. RAG
receives the same frozen BGE-LLM top10 and independently generated common
soft tags. The shared scientific instructions, answer structure, lack of a
word limit, and 5000-token output ceiling are matched within each base model.

All six systems are evaluated with the frozen citation-blind L3 judge. The
judge sees one anonymous canonicalized answer and the candidate-blind
reference claim ledger. GPT-5.1 at low reasoning is run three times. The
primary result is the equal mean of the three repeat-specific system means;
the accompanying uncertainty is the sample SD across those three means.

The primary scientific contrasts are the three within-model RAG-minus-Direct
effects. Cross-model absolute scores are secondary because provider models
are capability-matched, not parameter- or compute-matched.

This extension was specified and developed on Dev13. Test40 had already been
opened for the preceding three-retriever experiment, so this package does not
claim that its planning predates every observation of Test40. Its prompts,
models, L3 metric, repeat count, and aggregation are transferred unchanged
from the frozen Dev protocol.

Formal generation uses provider APIs to preserve the Dev13 request contract.
Claude subscription access is reserved for protocol and code review and is
not substituted for the Anthropic Messages API in the experimental arm.

## Validation

```bash
.venv/bin/python -m unittest discover \
  -s benchmark/runs/test40_multibase_direct_rag_v1/tests -v

.venv/bin/python \
  benchmark/runs/test40_multibase_direct_rag_v1/scripts/preflight.py \
  --write-manifest
```

## Execution

Run each of the six systems, then each L3 repeat:

```bash
.venv/bin/python \
  benchmark/runs/test40_multibase_direct_rag_v1/scripts/run_generation.py \
  --system all --workers 3

.venv/bin/python \
  benchmark/runs/test40_multibase_direct_rag_v1/scripts/run_l3_repeats.py \
  --repeat 1 --workers 3
```

Use `--resume` after any interrupted or partially failed stage. Repeat the L3
command for repeats 2 and 3.

## Completed Results

Formal execution is complete. The canonical result summary and aggregate
tables are:

```text
results/RESULTS_SUMMARY.md
results/l3/aggregate/system_three_repeat_summary.csv
results/l3/aggregate/within_model_three_repeat_summary.csv
```

Across the three base models, RAG-minus-Direct mean L3 effects were +0.229 for
GPT-5.1, +0.154 for Gemini 3.1 Pro Preview, and +0.226 for Claude Sonnet 5.

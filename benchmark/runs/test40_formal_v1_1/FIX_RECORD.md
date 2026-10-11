# Test40 Formal V1.1 Fix Record

Date: 2026-07-30

The V1 local retrieval run completed all 40 questions but failed its final
context validation before any paid API call. The failure was caused by context
normalization using boolean fallback for chunk identifiers. A valid integer
chunk index of `0` was therefore serialized as an empty string.

V1.1 replaces that fallback with an explicit null/empty check and adds a
regression test proving that chunk index zero is retained as `"0"` and passes
complete-context validation.

The fix changes identifier serialization only. It does not change retrieval
ranking, retrieved text, questions, gold evidence, L3 references, prompts,
models, budgets, metrics, or aggregation.

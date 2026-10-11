# V20 Change Record

Date: 2026-08-04

V20 is an execution-only successor to V19. V19 revealed that all three
BGE-LLM Layer B responses ended at the frozen 12,000-token output ceiling and
were correctly rejected, while the six Web Search and Direct responses
completed normally.

V20 changes only the Layer B technical output ceiling from 12,000 to 20,000
tokens. It does not change the task, fixed candidate answers, prompt, schema,
judge model, reasoning effort, status mapping, weights, caps, metric, repeat
count, or aggregation.

The two successful V19 Layer A source-support calls are reused only after
exact request-hash validation because their prompt, schema, model, and
14,000-token ceiling are unchanged. All nine Layer B judgments are rerun under
the common 20,000-token ceiling; no V19 Layer B score is reused.

The result remains retrospective calibration, not prospective validation.

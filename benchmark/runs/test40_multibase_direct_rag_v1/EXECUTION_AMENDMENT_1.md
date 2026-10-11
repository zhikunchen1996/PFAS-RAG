# Execution amendment 1: provider refusals

Date: 2026-07-30

The pre-run implementation treated Anthropic `stop_reason=refusal` as a
failed call. During Claude Sonnet 5 Direct generation, `WF10_012` returned
that terminal status twice under the same frozen request. Discarding the
responses and retrying until a substantive answer appeared would selectively
condition the formal output on provider compliance.

The execution rule is therefore amended prospectively for the remaining
generation:

- a provider-level refusal is a valid terminal model behavior;
- returned refusal text is preserved as the candidate answer;
- if the provider returns no text, the deterministic marker
  `[Provider refusal: no answer content returned.]` is stored;
- `provider_refusal=true` and the provider finish reason are recorded;
- L3 scores the refusal under the unchanged citation-blind frozen protocol;
- no question, prompt, model, context, tag, reference, metric, repeat count,
  or aggregation rule is changed.

This amendment was made before any L3 judgment in this experiment. The two
earlier unrecorded refusal calls are retained in the final execution-accounting
note as paid-call overhead and are not counted as candidate answers.

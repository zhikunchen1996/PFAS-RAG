# L3 V3 continuous-only protocol

Status: **frozen on Dev13 before any Test40 L3 run**

This package removes the planned candidate-answer human adequacy labeling and
binary threshold calibration from L3. It retains the already frozen,
project-author-approved Dev13 reference claim ledger, the L3 judge prompt, the
claim-status scale, and all continuous aggregation rules.

## Why the human calibration step was removed

The blinded packet contained 26 candidate answers, but all 26 labels remained
`pending`. No adequacy decision or material-error label was collected.
Calibrating a threshold against the L3 judge's own scores would be circular,
and substituting another model would not constitute human calibration.
Therefore V3 makes no binary adequacy claim.

Do not report L3 pass rate, accuracy, sensitivity, specificity, or an
``optimal'' cutoff. Report continuous reference-claim coverage with
question-level uncertainty instead.

The abandoned packet is retained for provenance at:

```text
../l3_gold_reference_dev13_v2/human_adequacy_calibration_repair7/
```

## Frozen scoring

Primary metric:

```text
mean_component_balanced_core_reference_claim_coverage
```

Core claim groups receive `full = 1`, `partial = 0.5`, and
`absent/contradicted = 0`. Groups are averaged within each task component,
components receive equal weight within a question, and questions receive
equal weight at system level.

The canonical claim order is the predeclared primary analysis. Reverse claim
order is a mandatory sensitivity analysis and may not replace selected
canonical results. System differences use a paired, question-clustered
10,000-iteration percentile bootstrap with seed `20260729`.

Secondary metrics are strict-core coverage, supplementary coverage, boundary
compliance, core contradiction rate, reference-anchored material-error rate,
and potential external-error flag rate. Error flags are diagnostics, not
binary pass gates.

## Dev13 result retained by V3

The continuous scores were generated before the decision to remove binary
calibration. They are inherited without an API rerun because V3 does not
change the reference, judge prompt, or continuous scoring algorithm.

| Claim order | System | Core coverage | Strict core | Supplementary |
|---|---|---:|---:|---:|
| Canonical (primary) | GPT-5.1 Direct | 0.446 | 0.128 | 0.189 |
| Canonical (primary) | GPT-5.1 BGE-LLM RAG | 0.644 | 0.419 | 0.411 |
| Reverse (sensitivity) | GPT-5.1 Direct | 0.481 | 0.154 | 0.461 |
| Reverse (sensitivity) | GPT-5.1 BGE-LLM RAG | 0.634 | 0.404 | 0.421 |

The primary paired difference (RAG minus Direct) is `0.199`, with a
question-clustered bootstrap 95% interval of `[0.106, 0.304]`. The reverse
order difference is `0.153`, with interval `[0.036, 0.295]`.

Claim-order sensitivity is material: exact question-level core-score
agreement was 9/26 (34.6%), mean absolute difference was 0.119, and the
maximum absolute difference was 0.417. The direction of the system-level
difference was unchanged. Both analyses must be disclosed.

## Freeze boundary

This is a Dev-developed scoring protocol, not a claim that the method was
specified before Dev results existed. The protocol change removes an
unexecuted calibration step; it does not tune the observed continuous scores.
No Test40 L3 result existed at freeze.

Running L3 on Test40 additionally requires candidate-blind construction and
freezing of Test40 claim ledgers. Once that is done, this scoring protocol,
including canonical primary order, reverse sensitivity analysis, metrics,
and bootstrap settings, must remain unchanged.

## Validation

```bash
.venv/bin/python \
  benchmark/runs/l3_gold_reference_dev13_v3_continuous/scripts/build_freeze_manifest_v3.py \
  --verify

.venv/bin/python \
  benchmark/runs/l3_gold_reference_dev13_v3_continuous/scripts/validate_continuous_v3.py
```

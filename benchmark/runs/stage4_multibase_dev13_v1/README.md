# Multi-base-model Dev13 experiment

This versioned experiment adds two matched high-capability proprietary base
models to the completed GPT-5.1 Dev13 Direct-versus-BGE-LLM RAG pilot:

- `gemini-3.1-pro-preview`
- `claude-sonnet-5`

Both providers receive byte-identical copies of the frozen GPT-5.1 scientific
and arm prompts. Direct and RAG use the same provider, model, reasoning
setting, output ceiling, and response structure. The only planned information
difference is the frozen retrieved evidence, soft tags, and citation
instructions supplied to the RAG arm.

Gemini uses low thinking and its recommended default temperature. Claude uses
adaptive thinking with low effort and no temperature override. These settings
match the existing GPT-5.1 low-effort operational policy while controlling
cost. The models are comparable as high-capability proprietary
general-purpose systems, but no claim of equal parameter count, training
compute, or release maturity is made.

Retrieval and common tagging are reused without API calls. Every generation
records actual provider model identity, token usage, estimated cost, and
latency. A one-question, two-arm smoke test is resumed into the complete
13-question run, so successful smoke-test calls are not repeated.

Evaluation uses the frozen L3 V3 continuous-only protocol. Canonical claim
order is primary and reverse claim order is a mandatory sensitivity analysis.
No binary pass rate or human candidate-answer calibration is used.

## Dev13 results

| Base model | Direct core | BGE-LLM RAG core | Difference | 95% CI |
|---|---:|---:|---:|---:|
| GPT-5.1 | 0.446 | 0.644 | 0.199 | [0.106, 0.304] |
| Gemini 3.1 Pro Preview | 0.433 | 0.459 | 0.027 | [-0.058, 0.113] |
| Claude Sonnet 5 | 0.295 | 0.593 | 0.298 | [0.151, 0.446] |

Reverse-order effects were `0.153`, `0.010`, and `0.284`, respectively.
Thus, the positive RAG effect was stable for GPT-5.1 and Claude Sonnet 5 but
not distinguishable from zero for Gemini 3.1 Pro Preview on Dev13.

The incremental Gemini and Claude generation plus canonical/reverse L3 judge
cost was approximately USD 3.54. Retrieval and common tagging were reused
without new calls. Detailed scores, order sensitivity, and costs are under
`final_report/`.

The superseded sparse L2 pilots and their independent-judge sensitivity audit
are archived at:

```text
benchmark/archive/2026-07-29_l1_l15_l3_cleanup/multibase_dev13_l2_history
```

They are not included in this formal generation-and-L3 manifest.

## L3 cross-model analysis

The six systems were also compared on the common frozen L3 V3
component-balanced core reference-claim coverage scale. This analysis reused
the existing question-level scores and made no new judge or API calls.

Canonical means ranged from 0.295 for Claude Sonnet 5 Direct to 0.644 for
GPT-5.1 RAG. Seven of 15 canonical paired comparisons remained significant
after Holm correction, and 13 of 15 effect directions were preserved under
reverse claim order. The matched RAG-minus-Direct effects were 0.199 for
GPT-5.1, 0.027 for Gemini 3.1 Pro, and 0.298 for Claude Sonnet 5.

The complete zero-cost statistical package is under
`l3_cross_model_dev13_v1/`.

The corresponding manuscript figure, source tables, caption, and
reproducible plotting script are under
`figures/l3_cross_model_dev13_v1/`.

## Generation

```bash
.venv/bin/python \
  benchmark/runs/stage4_multibase_dev13_v1/scripts/run_generation.py \
  --provider gemini31_pro \
  --out benchmark/runs/stage4_multibase_dev13_v1/results/gemini31_pro \
  --question-limit 1

.venv/bin/python \
  benchmark/runs/stage4_multibase_dev13_v1/scripts/run_generation.py \
  --provider gemini31_pro \
  --out benchmark/runs/stage4_multibase_dev13_v1/results/gemini31_pro \
  --resume
```

Use the same commands with `--provider claude_sonnet5`.

## Validation

```bash
.venv/bin/python \
  benchmark/runs/stage4_multibase_dev13_v1/scripts/validate_experiment.py

.venv/bin/python \
  benchmark/runs/stage4_multibase_dev13_v1/scripts/build_experiment_manifest.py \
  --verify

.venv/bin/python \
  benchmark/runs/stage4_multibase_dev13_v1/l3_cross_model_dev13_v1/\
scripts/validate_cross_model_analysis.py
```

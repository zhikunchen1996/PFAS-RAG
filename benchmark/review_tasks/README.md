# Professional Review Benchmark

This directory contains the frozen Section 3.4 professional-review experiment.
Only the paths listed below are active.

## Active method and results

```text
professional_review_v3_formal_v1/          frozen method, prompts, tasks, schemas
runs/professional_review_v3_formal_v1/     complete ten-task formal execution
runs/professional_review_human_expert_v1/  deidentified blinded expert assessment
```

The formal systems are PFAS RAG, GPT-5.1 Web Search, and GPT-5.1 Direct.
PFAS RAG uses the frozen BGE-LLM retriever. Canonical model-judge results are in
`runs/professional_review_v3_formal_v1/RESULTS_SUMMARY.md`.

## Frozen calibration support

```text
professional_review_v3_pilot_candidate_v20/       judge implementation provenance
calibrations/v20_judge_stability_rt02_rt09_v1/    stability runner and policy
runs/v20_judge_stability_rt02_rt09_v1/            immutable calibration answers and calls
```

V20 remains at its original path because the calibration manifest and combined
manuscript freeze hash it there. It is support provenance, not an alternative
active experiment.

## Publication contents

Independent development archives and audit conversations are not part of the
publication export. The calibration dependencies above are retained because
their recorded inputs are needed for method verification.

## Validation

```bash
.venv/bin/python -m unittest discover \
  -s benchmark/review_tasks/professional_review_v3_formal_v1/tests -v
.venv/bin/python \
  benchmark/review_tasks/professional_review_v3_formal_v1/scripts/build_freeze_manifest.py \
  --verify
.venv/bin/python \
  benchmark/review_tasks/professional_review_v3_formal_v1/scripts/validate_review_run.py \
  --run-dir benchmark/review_tasks/runs/professional_review_v3_formal_v1
```

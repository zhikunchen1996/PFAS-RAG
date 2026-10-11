# V20 Judge Stability Calibration: RT02 and RT09

This calibration tests the frozen V20 Layer B judge on tasks that were not
used to develop that judge. It reuses four immutable candidate reviews from
the completed V15 pilot:

- RT02 BGE-LLM local RAG;
- RT02 GPT-5.1 Web Search;
- RT09 BGE-LLM local RAG; and
- RT09 GPT-5.1 Web Search.

No retrieval, extraction, verification, synthesis, source-support judgment, or
candidate-answer modification is performed. Each fixed answer receives three
new anonymous V20 GPT-5.1 judgments at low reasoning effort.

## Prospective Stability Gate

The gate was fixed before paid execution:

- mean per-answer sample SD <= 0.050;
- maximum per-answer sample SD <= 0.075; and
- maximum absolute repeat deviation from its answer's three-repeat mean <=
  0.100.

Passing this gate supports one canonical GPT-5.1 judge call per answer in the
formal ten-task experiment. Formal-system uncertainty should then be displayed
as the SD across the ten task-level scores, not as judge-repeat SD. Exact
three-way atomic-label agreement is reported as a diagnostic but is not an
additional gate because the primary metric is continuous.

## Run

```bash
.venv/bin/python \
  benchmark/review_tasks/calibrations/v20_judge_stability_rt02_rt09_v1/run_calibration.py \
  --run-dir benchmark/review_tasks/runs/v20_judge_stability_rt02_rt09_v1 \
  --allow-paid
```

The runner hash-verifies source answers, records the V20 package hashes and
request metadata, resumes only exact matching requests, and writes a JSON and
CSV summary. The completed calibration run contains immutable copies of all
four fixed answers and records repository-relative provenance paths. It can
therefore be audited without recreating the historical V15 run directory; a
fresh copy operation additionally checks that directory when it is available.

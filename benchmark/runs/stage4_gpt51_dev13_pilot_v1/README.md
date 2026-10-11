# Stage 4 GPT-5.1 Dev13 Matched Pilot

This run implements the first gate in Stage 4 of
`docs/archive/2026-07-29_l1_l15_l3_cleanup/development_checklist_2026-07-28.md`.

The directory remains at its original path because its matched GPT-5.1
Direct/RAG answers and task boundaries are hash-locked dependencies of the
active L3 packages. Its L2 outputs are historical and are not part of the
planned main analysis.

It compares GPT-5.1 Direct and GPT-5.1 BGE-LLM RAG on the same 13 development
questions. Both arms share one system prompt, model snapshot requirement,
reasoning effort, output budget, scientific instructions, response structure,
and task-alignment rules. The only intended information difference is that the
RAG arm receives the frozen retrieved chunks, frozen common-tagger annotations,
and atomic-citation instructions.

Frozen dependencies:

```text
benchmark/frozen_v3
benchmark/frozen_v3/judge
```

The pilot does not change any frozen retrieval, tagging, L1, L1.5, or L2
definition.

## Run

Generate answers:

```bash
.venv/bin/python \
  benchmark/runs/stage4_gpt51_dev13_pilot_v1/scripts/run_generation.py \
  --out benchmark/runs/stage4_gpt51_dev13_pilot_v1/results/gpt51_dev13_matched_knowledge_v13 \
  --workers 3
```

Validate:

```bash
.venv/bin/python \
  benchmark/runs/stage4_gpt51_dev13_pilot_v1/scripts/validate_pilot.py \
  --run benchmark/runs/stage4_gpt51_dev13_pilot_v1/results/gpt51_dev13_matched_knowledge_v13
```

The canonical L2 V4 runner and aggregation commands are recorded in
`protocol.json`. Canonical pilot results are under:

```text
results/gpt51_dev13_matched_knowledge_v13
```

`FINAL_PILOT_AUDIT.md` is the concise interpretation record.
`final_report/` contains mapped per-question votes, complete cost/latency
accounting, and a machine-readable summary.

No answer-length limit is imposed. Word counts are retained only as descriptive
diagnostics and cannot trigger exclusion, retry, or selective regeneration.

The earlier complete generation attempt is retained under
`results/gpt51_dev13_attempt1_failed_length_gate`. It produced all 26 answers
using a superseded prompt that contained a numeric length instruction. No L2
judgment was run on it, and it is excluded from performance evaluation.

The V1.2 development run is retained under `results/gpt51_dev13_unrestricted`.
Its L2 results identified an arm-specific wording asymmetry in access to
general scientific knowledge. The run is diagnostic only and is not used as
the Stage 4 pilot result.

The `l2/` and `l2_v3/` subdirectories in the canonical generation run are
judge-calibration history. `l2_v4/` is the frozen result. Claude Sonnet returned
`FREEZE_APPROVED` after reviewing the final source artifacts.

# Dev13 L3 three-repeat GPT-5.1 evaluation

This separately versioned package evaluates all six existing Dev13 answer
systems with three new canonical-order L3 judgments per answer.

Each call uses the frozen L3 reference claim ledger and judge prompt, one
anonymous answer per request, `gpt-5.1` with required returned snapshot
`gpt-5.1-2025-11-13`, reasoning effort `low`, provider-default
temperature, and a 12,000-token completion ceiling.

All 234 judgments are new GPT-5.1 calls. The package does not reuse or pool
the historical GPT-4.1 results. A one-answer smoke test is retained as the
first completed item of repeat 1 and is not called again.

The final system score is the equal mean of the three repeat-specific system
means. Uncertainty is the sample standard deviation across three complete
repeat means (`n = 3`). No bootstrap interval, permutation test, or
reverse-order repeat is used. This is Dev13-only; Test40 is not used.

## Run

```bash
.venv/bin/python \
  benchmark/runs/l3_three_repeat_dev13_v2_gpt51judge/scripts/build_pre_run_manifest.py

# Smoke test: completes the first repeat-1 item and leaves it resumable.
.venv/bin/python \
  benchmark/runs/l3_three_repeat_dev13_v2_gpt51judge/scripts/run_repeats.py \
  --repeat 1 --limit 1

.venv/bin/python \
  benchmark/runs/l3_three_repeat_dev13_v2_gpt51judge/scripts/run_repeats.py \
  --repeat 1
.venv/bin/python \
  benchmark/runs/l3_three_repeat_dev13_v2_gpt51judge/scripts/run_repeats.py \
  --repeat 2
.venv/bin/python \
  benchmark/runs/l3_three_repeat_dev13_v2_gpt51judge/scripts/run_repeats.py \
  --repeat 3

.venv/bin/python \
  benchmark/runs/l3_three_repeat_dev13_v2_gpt51judge/scripts/aggregate_repeats.py
```

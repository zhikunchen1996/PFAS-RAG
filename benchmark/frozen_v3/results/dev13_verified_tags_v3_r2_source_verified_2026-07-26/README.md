# Frozen V3 Revision 2 Source-Verified Dev13 Evaluation

This is the canonical Frozen V3 Revision 2 comparison against the
prompt-matched GPT-5.1 Direct baseline.

## Protocol

- 13 Dev questions;
- three judge repeats;
- both answer orientations in every repeat;
- GPT-5.1 at temperature 0;
- human-audited gold plus the common C1-C10 verification context;
- citations retained only as scientific-correctness locators;
- citation presence, format, count, density, and coverage not scored.

Weights:

- scientific correctness: 0.40;
- question fulfillment: 0.30;
- uncertainty and limitations: 0.15;
- practical usefulness: 0.15.

## Result

| V3 wins | Direct wins | Ties | Mean V3 score | Mirror agreement |
| ---: | ---: | ---: | ---: | ---: |
| 13 | 0 | 0 | 0.9218 | 0.7885 |

## Commands

The initial command was:

```bash
.venv/bin/python \
  benchmark/frozen_v3/scripts/run_dev13_soft_tags_v3_source_verified_judge.py \
  --workers 9
```

The final aggregation used `--resume`. Reuse required an exact model,
temperature, prompt, and payload fingerprint; all 78 judge calls matched.

GPT-5.1 omitted the three non-scoring auxiliary fields in 21 of 78 responses,
for 63 logged field-level normalizations. Every scored criterion preference
and rationale was present. Auxiliary fields do not enter the score or winner.

## Cost

- Prompt tokens: 726,585
- Completion tokens: 57,291
- Total tokens: 783,876
- Estimated cost: USD 1.4811

Question-level scores are in `results/per_question.csv`; the canonical summary
and exact input hashes are in `evaluation_manifest.json`. Test40 was not run.


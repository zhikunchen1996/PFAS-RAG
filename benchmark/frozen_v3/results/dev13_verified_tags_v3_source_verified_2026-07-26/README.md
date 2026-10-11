# Dev13 Source-Verified V3 Confirmation

Date: 2026-07-26

Status: `frozen_canonical_dev13_confirmation`

This is the canonical comparison between the regenerated verified-tag
BGE-LLM RAG system and the prompt-matched GPT-5.1 Direct baseline. It contains
no matched-untagged comparison.

The GPT-5.1 judge ran three repeats with both answer orientations. It received
human-audited gold and the common C1-C10 verification chunks. Citation markers
were retained only as locators for scientific verification; citation
presence, count, format, placement, and coverage were not scored.

## Result

| RAG wins | Direct wins | Ties | Mean weighted RAG score | Mirror agreement |
|---:|---:|---:|---:|---:|
| 13 | 0 | 0 | 0.8994 | 0.7949 |

Mean RAG criterion scores were 0.9551 for scientific correctness, 0.9423 for
question fulfillment, 0.6538 for uncertainty and limitations, and 0.9103 for
practical usefulness.

The repaired result preserves the earlier 13/0/0 direction while reducing the
mean score from 0.9131 to 0.8994. The difference is consistent with removal of
an avoidable unverified prose channel. The lower mirror agreement is retained
as judge uncertainty rather than concealed.

The judge used 795,138 tokens at an estimated cost of USD 1.4940.

Run command:

```bash
.venv/bin/python \
  benchmark/frozen_v3/scripts/run_dev13_soft_tags_v3_source_verified_judge.py \
  --include-direct --repeats 3 --workers 9
```

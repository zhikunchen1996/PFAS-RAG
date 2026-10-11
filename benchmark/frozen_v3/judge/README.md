# PFAS RAG frozen judge

Freeze date: **2026-07-28**

Immutable version and Git tag: **`frozen-judge-2026-07-28-v1`**

This nested directory is the canonical, self-contained judge implementation
inside the unified Frozen V3 PFAS RAG package. It freezes:

- L1 deterministic retrieval metrics;
- L1.5 claim-level citation-support sanity checking; and
- L2 V2 citation-blind pairwise answer-quality evaluation.

Question and gold inputs remain canonical in `benchmark/frozen_v3`. The
common-tagger Dev13 source package used by calibration is retained under
`support/layer1_common_tagger_v1`; judge scripts and prompts do not import code
from earlier experimental judge folders.

The runtime is pinned in `environment/python-version.txt` and
`environment/requirements-lock.txt`. The freeze manifest also hashes the
canonical Dev13 retrieval and answer artifacts used for calibration.

## Roles of the three layers

| Layer | Question | Primary use |
|---|---|---|
| L1 | Did retrieval return the known evidence? | Compare retrieval systems |
| L1.5 | Are material cited claims supported by their supplied chunks? | Test40 RAG citation sanity |
| L2 | Which anonymous answer is better on each answer-quality criterion? | Compare final answers |

L1.5 is not an answer-completion score and is not used to select a retrieval
system. L2 does not score citation format, citation count, or retrieval.

## L2 V2 statistical specification

Every pair-question has exactly two judgments with mirrored A/B order. All raw
system wins and ties are retained. Four independent Davidson models are fit:
scientific correctness, question fulfillment, scope and calibration, and
practical usefulness. Each criterion has its own estimated tie parameter.

Confidence intervals use 10,000 question-clustered percentile bootstrap
attempts. Failed fits and their rate are reported. The equal-weight composite
is secondary and is recomputed within each bootstrap replicate.

## Frozen development calibration

`calibration/dev13/l2v2_10000_bootstrap` contains the final Dev13 statistical
confirmation. The older 2,000-bootstrap files are retained only to show the
pre-freeze development trail and are not canonical.

`calibration/dev13/l15_legacy_attachment_diagnostic.csv` is also historical:
it motivated the final claim-level L1.5 design but is not a result produced by
the frozen prompt.

## Independent audit

`audits/anonymization` contains a deterministic leakage scan and an independent
Claude Sonnet 5 Medium forced-identification audit. The model did not receive
the local mapping key. Identity prediction was not significantly above random
at either the slot or complete-mapping level.

## Reproduction

Run the local integrity checks:

```bash
.venv/bin/python -m unittest discover \
  -s benchmark/frozen_v3/judge/tests -v
.venv/bin/python \
  benchmark/frozen_v3/judge/scripts/validate_frozen_judge.py
```

Calculate L1 for one retrieval file:

```bash
.venv/bin/python \
  benchmark/frozen_v3/judge/scripts/run_l1_retrieval.py \
  --retrieval PATH_TO_RETRIEVAL_JSONL \
  --questions benchmark/frozen_v3/input/questions_test40.csv \
  --out PATH_TO_L1_OUTPUT
```

Prepare L1.5 without calling the API:

```bash
.venv/bin/python \
  benchmark/frozen_v3/judge/scripts/run_l15_claim_support.py \
  --answers PATH_TO_RAG_ANSWERS_JSONL \
  --questions benchmark/frozen_v3/input/questions_test40.csv \
  --out PATH_TO_L15_OUTPUT \
  --dry-run
```

Remove `--dry-run` to execute the frozen judge, then summarize:

```bash
.venv/bin/python \
  benchmark/frozen_v3/judge/scripts/summarize_l15_claim_support.py \
  --results PATH_TO_L15_OUTPUT/judge_results.jsonl \
  --out PATH_TO_L15_SUMMARY
```

Run one L2 system pair:

```bash
.venv/bin/python \
  benchmark/frozen_v3/judge/scripts/run_l2_pairwise_v2.py \
  --left PATH_TO_SYSTEM_1_ANSWERS.jsonl \
  --right PATH_TO_SYSTEM_2_ANSWERS.jsonl \
  --left-label system_1 \
  --right-label system_2 \
  --questions benchmark/frozen_v3/input/questions_test40.csv \
  --out PATH_TO_PAIR_OUTPUT
```

Aggregate a connected set of pair directories:

```bash
.venv/bin/python \
  benchmark/frozen_v3/judge/scripts/aggregate_l2_v2.py \
  --pair system_1,system_2,PATH_TO_PAIR_1 \
  --pair system_1,system_3,PATH_TO_PAIR_2 \
  --pair system_2,system_3,PATH_TO_PAIR_3 \
  --bootstrap 10000 \
  --seed 20260728 \
  --out PATH_TO_AGGREGATE_OUTPUT
```

All API runners record model snapshot, token use, estimated cost, summed API
latency, and wall-clock duration.

L2 rejects identity-bearing text before any model call, removes evidence IDs
and decoys from visible gold, requires the exact frozen JSON schema, and
accepts only responses with `finish_reason=stop`. Interrupted runs validate
and recover existing results without silently duplicating payload IDs.

The independent Claude CLI review, follow-up verification, and finding
resolution table are stored under `reviews/`. The final external verdict is
`FREEZE_APPROVED`.

## Freeze boundary

The new judge had not been run on Test40 at freeze time. After the first Test40
execution, changes prompted by Test40 outcomes require a new protocol version;
they must not overwrite this directory.

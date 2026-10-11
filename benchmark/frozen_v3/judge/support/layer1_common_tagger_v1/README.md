# Layer 1 Common-Tagger Retrieval Comparison

Status: `dev13_protocol_candidate`

This experiment compares Hybrid, BGE, and BGE-LLM retrieval while holding the
evidence-use and answer-generation layers fixed.

```text
Hybrid top10  -> common soft tagger -> common answer generator
BGE top10     -> common soft tagger -> common answer generator
BGE-LLM top10 -> common soft tagger -> common answer generator
```

The runner reads the hash-verified Frozen V3 Revision 3 package but does not
modify it. Retrieval metrics are computed on each final top-10 context before
tagging. The common tagger:

- sees only the visible question and the final ten complete chunks;
- receives no gold, hidden rubric, system identity, retrieval scores, or
  expected answer;
- does not select, remove, truncate, or reorder chunks;
- uses the same model, prompt, temperature, and reasoning settings for all
  systems.

API calls are submitted in question-major order with a deterministic rotation
of system order. This prevents one retrieval system from being permanently
confounded with an earlier or later API execution block.

Tagger and answer-generation costs are recorded for every arm as common
downstream costs. The BGE-LLM selector cost remains a retrieval-specific cost.

Latency is recorded at three levels: every tagger/answer API call, per-system
sum and mean, and actual wall-clock duration of each interleaved parallel
stage. Matched retrieval, BGE, and selector stage latency is inherited from
the Frozen V3 runtime records and labeled as inherited rather than remeasured.
Summed request latency and parallel wall-clock are reported separately.

## Evaluation boundary

Before the tagger:

- primary retrieval metric: `MRR_required_gold`;
- secondary retrieval metrics: `required_gold_recall@10` and
  `gold_document_recall@10`.

After the common tagger and answer generator:

- citation-blind complete round-robin pairwise content comparison among
  Hybrid, BGE, and BGE-LLM;
- primary attribution metric:
  `citation_supported_claim_rate`, defined over externally verifiable answer
  claims and their immediately cited chunks;
- secondary attribution metrics: citation completeness, citation entailment
  accuracy, and unsupported-claim rate.

Citation recall against benchmark gold is prohibited because the gold set is
non-exhaustive.

Validate without API calls:

```bash
.venv/bin/python \
  benchmark/frozen_v3/judge/support/layer1_common_tagger_v1/scripts/run_dev13_common_tagger.py \
  --out /tmp/layer1-common-tagger-validation \
  --validate-only
```

Run generation into a new output directory:

```bash
.venv/bin/python \
  benchmark/frozen_v3/judge/support/layer1_common_tagger_v1/scripts/run_dev13_common_tagger.py \
  --out benchmark/frozen_v3/judge/support/layer1_common_tagger_v1/results/<run-id> \
  --workers 3
```
# Layer 1: retrieval-system comparison with a common evidence-use layer

This development-only experiment compares Frozen V3 Hybrid, BGE, and BGE-LLM
retrieval at the selected 10/60 budget. Retrieval metrics are computed on each
system's final top 10 before any tagging. The same GPT-5.1 soft tagger and
answer-generation prompt are then applied to every system.

## Answer comparison

`scripts/run_dev13_adaptive_davidson_pairwise.py` performs a complete
three-system round robin for every Dev13 question. Citations are removed from
the model-visible answers, and all comparisons use the same non-exhaustive
gold evidence and deduplicated retrieval union for verification.

Each pair-question unit receives an initial mirrored A/B pair. If the two
orientations map to the same system-level outcome, judging stops. A discordant
unit receives one additional mirrored pair. The final win/tie/loss outcome is
the majority of system-level points across its two or four calls, with a tie
worth one-half point to each system.

The primary normalized ranking is a Davidson Bradley-Terry model with an
explicit tie parameter. Scores are exponentiated fitted abilities normalized
to sum to 100 across the three systems; they are relative abilities, not
percent-correct values. Uncertainty is estimated by resampling questions and
retaining all pairwise outcomes from each sampled question.

Primary output:

- `results/davidson_ability.csv`
- `results/pairwise_wtl.csv`
- `results/pair_question_outcomes.csv`
- `results/bootstrap_draws.csv`
- `experiment_manifest.json`

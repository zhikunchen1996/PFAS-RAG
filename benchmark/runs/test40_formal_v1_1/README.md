# Formal Test40 L1, L1.5, and L3 execution package V1.1

Status: preflight only. No paid Test40 candidate-system call has been made by
this package.

V1.1 is an execution-only successor to V1. It preserves integer chunk index
zero during context normalization. V1 converted that valid identifier to an
empty string and therefore stopped at the final local retrieval validation.
No retrieval parameter, prompt, model, question, gold record, reference
ledger, metric, or aggregation rule changed.

This package executes the frozen Test40 plan without modifying
`benchmark/frozen_v3` or the original frozen Test40 reference release. It
contains a separately versioned, candidate-blind scoring-compatible successor
to that reference. The successor maps ten already audited task-component
conclusions to required L3 content because the original ledger left those
components without a scoreable core claim. It changes no question, gold
chunk, task component, or reference answer. It compares
Hybrid, BGE, and BGE-LLM retrieval under the selected 10/60 budget, applies
one common soft tagger and one matched answer prompt to every system, runs
L1.5 once as a supplementary citation-support sanity check, and runs three
canonical GPT-5.1 L3 repeats.

## Required order

1. Run `scripts/preflight.py --write-manifest`.
2. Commit and freeze the pre-run package before any paid call.
3. Run `scripts/preflight.py --verify-manifest` immediately before execution.
4. Run local retrieval with `scripts/run_retrieval.py`.
5. Run `scripts/run_selector.py`, then `scripts/run_l1.py`.
6. Run `scripts/run_generation.py`.
7. Run `scripts/run_l15.py`.
8. Run `scripts/run_l3_repeats.py` separately for repeats 1, 2, and 3.

Every paid stage supports `--dry-run`. If a paid output file already exists,
the command refuses to proceed unless `--resume` is supplied. Resume reuses
only rows whose complete request hash matches.

All formal outputs are fixed under `results/`; arbitrary output paths are
rejected. A non-formal retrieval smoke test may use another directory only
when `--limit` is supplied.

## Cost

The planned 760 paid calls are estimated at USD 15.2--17.8. The recommended
account ceiling is USD 20. Hybrid/BGE retrieval and L1 are local and have no
API charge. See `cost_estimate.json`.

The candidate-blind independent review record is
`reviews/claude_subscription_review_2026-07-29.md`.

## Boundaries

- Retrieval metrics are computed before the common tagger.
- The selector and tagger receive no gold or L3 reference data.
- The tagger receives no system identity.
- L1.5 receives no gold and performs no post-hoc retrieval.
- L3 receives one anonymous canonicalized answer and the frozen Test40 claim
  ledger scoring successor.
- Test40 outcomes cannot be used to revise prompts, models, parameters,
  repeat counts, or aggregation.

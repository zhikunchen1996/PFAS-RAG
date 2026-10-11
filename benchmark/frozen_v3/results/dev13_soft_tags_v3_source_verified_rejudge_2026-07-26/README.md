# Dev13 Source-Verified Pairwise Confirmation

Date: 2026-07-26

Status: `frozen_canonical_dev13_confirmation`

## Purpose

This run tests whether the citation-blind judge was misclassifying valid,
retrieved details as fabricated because it could see neither `[C#]` markers
nor the corresponding chunks.

No answers were regenerated. The run reused the exact tagged, matched
untagged, and matched Direct GPT-5.1 answers from
`dev13_soft_tags_v3_confirmation_2026-07-26`.

## Evaluation change

The judge received:

- the same question and human-audited gold;
- the same common C1-C10 verification chunks;
- answers with `[C#]` markers retained.

Citation presence, absence, count, density, placement, formatting, and
coverage were explicitly excluded from evaluation. A marker could be used
only to locate evidence when checking scientific correctness. Citation
quality was not a criterion or score.

## Results

| Comparison | Tagged wins | Opponent wins | Ties | Mean tagged score | Mirror agreement |
|---|---:|---:|---:|---:|---:|
| tagged vs matched untagged | 9 | 3 | 1 | 0.5631 | 0.6410 |
| tagged vs matched Direct | 13 | 0 | 0 | 0.9131 | 0.8846 |

Matched citation-blind repeat-1 values:

| Comparison | Citation-blind mean | Source-verified mean | Citation-blind W/L/T | Source-verified W/L/T |
|---|---:|---:|---:|---:|
| tagged vs matched untagged | 0.5856 | 0.5952 | 5/1/7 | 9/2/2 |
| tagged vs matched Direct | 0.3596 | 0.8990 | 3/10/0 | 12/1/0 |

The first source-verified repeat remained close to the matched citation-blind
repeat for tagged versus untagged (`0.5952` versus `0.5856`). Across all three
source-verified repeats, the mean settled at `0.5631`. Scientific correctness
for tagged versus untagged was `0.5833`, rather than automatically approaching
1.0. This argues against a simple more-citations bias.

For tagged versus Direct, three-repeat scientific correctness was `0.9487`.
Rationale inspection showed that the judge recognized values, protocols, and
comparisons present in the verification chunks instead of calling them
fabricated merely because they were absent from gold.

## Interpretation

The source-verified result answers a different and more suitable question for
literature-grounded system utility: whether the answer is correct and useful
after its source-specific claims can be verified.

It does not assess citation quality. Direct was not penalized for lacking
citations; it lost most questions because it supplied general frameworks where
the question and known evidence supported concrete literature-specific
answers. WF10_021 was the only Direct win because its broader screening
checklist fulfilled that question more effectively.

This is a complete three-repeat result with both answer orientations. It is
evidence that the original citation-blind Direct result was confounded.

The canonical article comparison is the complete tagged V3 system versus
matched Direct: `13/0/0`, mean `0.9131`, and mirror agreement `0.8846`.
Tagged versus matched untagged is retained only as an internal mechanism
diagnostic. It is not an article comparator and does not determine whether the
complete V3 system can be frozen.

## Cost

- calls: 156;
- input tokens: 1,467,651;
- output tokens: 110,174;
- total tokens: 1,577,825;
- estimated cost: USD 2.9363.

Canonical outputs are `results/summary.csv`, `results/per_question.csv`, and
`evaluation_manifest.json`.

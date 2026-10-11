# Dev13 L3 cross-model analysis

All results reuse frozen L3 V3 question-level scores. No judge or API was called.

## Canonical mean ranking

| Rank | System | Mean core coverage |
|---:|---|---:|
| 1 | GPT-5.1 RAG | 0.644 |
| 2 | Claude Sonnet 5 RAG | 0.593 |
| 3 | Gemini 3.1 Pro RAG | 0.459 |
| 4 | GPT-5.1 Direct | 0.446 |
| 5 | Gemini 3.1 Pro Direct | 0.433 |
| 6 | Claude Sonnet 5 Direct | 0.295 |

## Statistical summary

- Canonical pairwise comparisons: 15
- Holm-significant canonical comparisons: 7
- Same mean direction in canonical and reverse: 13/15
- Canonical is primary; reverse is sensitivity only.
- Pair-level confidence intervals and adjusted p-values are in `pairwise_comparisons.csv`.

This is a post-hoc Dev13 analysis. It does not alter the frozen judge, reference ledger, answer sets, or Test40 boundary.

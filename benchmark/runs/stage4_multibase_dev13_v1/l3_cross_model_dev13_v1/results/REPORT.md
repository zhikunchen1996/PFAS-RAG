# Dev13 L3 cross-model report

This report compares the six existing answer systems on the same frozen L3 V3
component-balanced core reference-claim coverage scale. It uses stored
question-level scores only. No new judge or API call was made.

## Canonical system means

| Rank | System | Mean |
|---:|---|---:|
| 1 | GPT-5.1 RAG | 0.644 |
| 2 | Claude Sonnet 5 RAG | 0.593 |
| 3 | Gemini 3.1 Pro RAG | 0.459 |
| 4 | GPT-5.1 Direct | 0.446 |
| 5 | Gemini 3.1 Pro Direct | 0.433 |
| 6 | Claude Sonnet 5 Direct | 0.295 |

## Matched RAG effects

| Base model | RAG minus Direct | Paired 95% CI | Holm p |
|---|---:|---:|---:|
| GPT-5.1 | 0.199 | [0.103, 0.304] | 0.038 |
| Gemini 3.1 Pro | 0.027 | [-0.059, 0.115] | 1.000 |
| Claude Sonnet 5 | 0.298 | [0.151, 0.446] | 0.047 |

These intervals are the jointly generated cross-model intervals from the
pre-analysis-hashed NumPy PCG64 implementation. The earlier within-model
summary used Python `random.Random` with the same iteration count and numeric
seed. This changes a few Monte Carlo percentile endpoints slightly (for
example, the GPT-5.1 lower endpoint is 0.103 here and 0.106 in the earlier
summary) but does not change any point estimate or substantive conclusion.
One interval table should be used consistently in reporting.

The corresponding reverse-order effects are 0.153, 0.010, and 0.284. All
three matched effects preserve direction. After correcting all 15 comparisons
within each order, the GPT-5.1 matched effect is significant in canonical
order but not reverse order; the Claude effect is significant in both; the
Gemini effect is not significant in either.

## Cross-model inference

Seven of 15 canonical pair comparisons have Holm-adjusted exact sign-flip
probabilities below 0.05. Thirteen pairs preserve their mean direction under
reverse claim order.

The two direction changes are:

- GPT-5.1 Direct versus Gemini 3.1 Pro RAG.
- GPT-5.1 RAG versus Claude Sonnet 5 RAG.

Neither direction-changing comparison is significant in either order. This
supports treating the highest two RAG means as statistically unresolved on
Dev13 rather than claiming that one is superior.

This is a post-hoc Dev13 analysis with 13 questions. The intervals and exact
tests characterize uncertainty in this development set; they are not a
substitute for Test40 confirmation. Test40 remains unused.

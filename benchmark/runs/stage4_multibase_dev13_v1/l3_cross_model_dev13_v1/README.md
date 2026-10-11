# Dev13 L3 cross-model analysis

This post-hoc local analysis reuses the already frozen canonical and reverse
L3 V3 question-level scores for all six systems. It performs all 15 paired
cross-system comparisons without calling an LLM judge or any external API.

Canonical claim order is primary. Reverse claim order is a mandatory
sensitivity analysis. Each pair reports the mean score difference, 10,000
question-clustered paired-bootstrap confidence interval, exact paired
sign-flip permutation p-value, Holm-adjusted p-value, and per-question
win/tie/loss counts.

No Test40 data are used.

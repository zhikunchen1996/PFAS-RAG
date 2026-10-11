# Retrieval-Metric–Answer Correlation Results

## Overall Associations

- MRR of first required gold: Spearman's ρ 0.206 (question-cluster-robust t(37) = 1.629, two-sided P = 0.112; question-cluster bootstrap 95% interval -0.045 to 0.444; BH-FDR q = 0.168).
- Required-gold recall@10: Spearman's ρ 0.230 (question-cluster-robust t(37) = 1.835, two-sided P = 0.075; question-cluster bootstrap 95% interval -0.017 to 0.466; BH-FDR q = 0.168).
- Gold-document recall@10: Spearman's ρ 0.093 (question-cluster-robust t(37) = 0.679, two-sided P = 0.502; question-cluster bootstrap 95% interval -0.181 to 0.355; BH-FDR q = 0.502).

## Coefficient Comparisons

- MRR_required_gold minus required_gold_recall@10: -0.024 (95% interval -0.178 to 0.137).
- MRR_required_gold minus gold_doc_recall@10: 0.113 (95% interval -0.100 to 0.339).
- required_gold_recall@10 minus gold_doc_recall@10: 0.138 (95% interval -0.026 to 0.308).

The MRR-minus-required-gold-recall interval includes zero. The data therefore do not support the hypothesis that MRR is more strongly related to answer quality than chunk-level required-gold recall.

## Full-Retrieval Diagnostic

Among 32 observations from 14 questions with full required-gold retrieval, MRR had Spearman's ρ -0.054 (95% interval -0.514 to 0.386; question-cluster-robust t(13) = -0.281, P = 0.783).

Full required-gold retrieval does not make the complete contexts identical. Remaining answer differences can reflect non-gold context composition, ordering, evidence-role tags, valid evidence outside the non-exhaustive gold, and how the answer model selects and synthesizes evidence.

## Strict Matched Full-Retrieval Diagnostic

Only seven questions had full required-gold retrieval under all three systems. Their descriptive system means were:

- bge: mean MRR 0.695; mean final-answer quality 0.510.
- bge_llm: mean MRR 1.000; mean final-answer quality 0.536.
- hybrid: mean MRR 0.592; mean final-answer quality 0.641.

This small matched subset likewise does not support an MRR-only explanation of final-answer differences.

# Dev13 Dense-only and BM25-only Ablation

| System | MRR required gold | Required-gold recall@10 | Gold-document recall@10 | Negative-gold recall@10 |
|---|---:|---:|---:|---:|
| Dense-only | 0.116 | 0.144 | 0.551 | 0.000 |
| BM25-only | 0.113 | 0.128 | 0.403 | 0.167 |

For context, the canonical frozen Hybrid 10/60 Dev13 result was MRR 0.158,
required-gold recall@10 0.200, gold-document recall@10 0.454, and
negative-gold recall@10 0.000. That Hybrid row is cited from the frozen result
and was not rerun or copied into this ablation as a third experimental arm.

Dense-only retrieved a broader set of gold documents than either BM25-only or
the frozen Hybrid configuration, but it localized fewer exact required gold
chunks in the final top 10. Hybrid fusion improved both MRR and exact required
gold recall over either isolated component. BM25-only provided the only
negative-gold hits in this small Dev13 comparison, but the diagnostic applies
to only six questions and should not be overinterpreted.

The component comparison is a post-freeze Dev13 analysis. It used no LLM,
answer generation, judge, or Test40 data.

The accompanying all-53 sensitivity check found that retiring the legacy
numerical reference penalty left required-gold recall, gold-document recall,
and negative-gold recall unchanged on both splits. Hybrid MRR changed by
-0.00149 on Dev13 and -0.00099 on Test40. The simplified active implementation
therefore retains only the separate deterministic reference-list filter; the
formal result files remain unchanged for provenance.

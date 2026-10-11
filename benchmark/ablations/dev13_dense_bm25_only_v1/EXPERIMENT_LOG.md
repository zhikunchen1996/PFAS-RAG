# Experiment Log

## 2026-08-10 to 2026-08-11: Retrieval-component exploration

### Question

Does either isolated retrieval component explain the performance of the frozen
Hybrid candidate retriever?

### Retained experiment

- Split: frozen Dev13 only; Test40 was not used.
- Corpus: `corpus434_repaired_v1`, 434 records and 29,805 chunks.
- Budget: 60 candidates followed by the shared deterministic reference filter
  and a final top-10 context.
- Dense-only: `BAAI/bge-large-en-v1.5` vector-distance ranking.
- BM25-only: `k1=1.5`, `b=0.75`, and the project tokenizer.
- Evaluation: deterministic frozen L1 metrics against the 249-record audited
  gold file.
- API and judge calls: none.
- Originating combined local runtime: 14.07 seconds after model and collection
  availability.

### Result

| System | MRR | Required-gold recall@10 | Gold-document recall@10 | Negative-gold recall@10 |
|---|---:|---:|---:|---:|
| Dense-only | 0.116 | 0.144 | 0.551 | 0.000 |
| BM25-only | 0.113 | 0.128 | 0.403 | 0.167 |

The canonical frozen Hybrid 10/60 reference was 0.158, 0.200, 0.454, and
0.000, respectively. Dense-only found more gold documents but localized fewer
required chunks. Hybrid improved MRR and required-gold recall over both
isolated components.

### Reproduction check

On 2026-08-11, the packaged script was rerun from the local Chroma collection
with the cached embedding model on CPU. Both systems reproduced identical
ordered document/chunk top-10 contexts for all 13 questions. Metric summaries
matched to numerical precision; byte-level CSV differences were limited to
newline formatting and final floating-point representation.

### Retention decision

Only the dense-only and BM25-only experiments were promoted into this package.
Temporary Jina reranking, reference-filter V2, reference-penalty sensitivity,
candidate-conversion, and duplicate dense-pool artifacts from the side-chat
exploration were deleted after promotion and validation.

### Analysis boundary

This is a post-freeze development-set ablation intended to explain retrieval
components. It does not alter the frozen systems, formal Test40 results, or
manuscript-analysis freeze.

## 2026-08-11: Numerical reference-penalty retirement

The legacy Hybrid score subtracted 0.15 from citation-dense chunks and 0.25
from chunks beginning with a references or bibliography heading. A
deterministic all-53-question sensitivity run compared the legacy ranking,
disabling only the 0.15 marker penalty, and disabling both numerical
penalties. The latter two conditions produced the same results because the
separate reference-list filter already handled heading-like chunks.

Required-gold recall@10, gold-document recall@10, and negative-gold recall@10
were unchanged on Dev13 and Test40. MRR changed from 0.157738 to 0.156250 on
Dev13 and from 0.333584 to 0.332592 on Test40. Top-10 membership changed for
one Dev13 question and four Test40 questions, while the top-60 candidate set
changed for zero and two questions, respectively. The result supports removal
as a code-simplification step with no material change to the study conclusion,
but it does not support a claim of exact ranking identity.

The active application ranking was simplified to dense, BM25, and lexical
overlap only. The independent deterministic reference-list filter remains.
Formal result artifacts were not regenerated or overwritten.

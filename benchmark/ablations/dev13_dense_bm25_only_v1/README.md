# Dev13 Dense-only and BM25-only Component Ablation

## Purpose

This package isolates the two primary candidate-retrieval components used by
the local Hybrid system. It retains only the BGE dense-only and BM25-only
experiments from the retrieval exploration conducted after the main analysis
freeze.

The comparison asks whether semantic dense retrieval and exact lexical
retrieval contribute complementary evidence. It is a Dev13 diagnostic, not a
new system-selection run and not a held-out Test40 result.

## Configurations

- **Dense-only:** `BAAI/bge-large-en-v1.5` retrieves 60 chunks by vector
  distance. The deterministic reference filter orders narrative chunks before
  reference-like chunks, and the first 10 are evaluated.
- **BM25-only:** BM25 (`k1=1.5`, `b=0.75`) retrieves 60 chunks using the
  project's frozen tokenizer. The same reference filtering and top-10 budget
  are applied.

Neither arm uses Hybrid fusion, the additional lexical-overlap fusion score,
BGE cross-encoder reranking, LLM selection, answer generation, or an LLM
judge. No reference score penalty is part of either isolated component score;
the shared deterministic reference filter alone is applied after retrieval.

## Results

| System | MRR | Required-gold recall@10 | Gold-document recall@10 | Negative-gold recall@10 |
|---|---:|---:|---:|---:|
| Dense-only | 0.116 | 0.144 | 0.551 | 0.000 |
| BM25-only | 0.113 | 0.128 | 0.403 | 0.167 |
| Frozen Hybrid 10/60, contextual reference only | 0.158 | 0.200 | 0.454 | 0.000 |

The frozen Hybrid result is referenced from its canonical Dev13 output and is
not retained here as another ablation run. Dense-only showed the highest
document-level coverage but lower exact required-chunk recall. Hybrid fusion
improved MRR and exact required-gold recall over both isolated components,
supporting the use of complementary semantic and lexical retrieval.

## Reference-penalty retirement check

An additional deterministic sensitivity check compared the legacy Hybrid
ranking with the citation-marker penalty disabled and with all numerical
reference penalties disabled. Across both Dev13 and Test40, required-gold
recall@10, gold-document recall@10, and negative-gold recall@10 were unchanged.
MRR changed slightly from 0.158 to 0.156 on Dev13 and from 0.334 to 0.333 on
Test40. The final top-10 set changed for 1 of 13 Dev questions and 4 of 40 Test
questions, so the implementations are not byte-identical, but the retrieval
conclusion and rounded main recall metrics are unchanged.

The active application therefore omits the numerical penalty and retains the
separate deterministic reference-list filter. The completed formal outputs
remain immutable historical results. This post hoc code-simplification check
is retained internally and is not treated as a new formal Test40 experiment.

## Files

- `protocol.json`: prospective interpretation and exact configurations.
- `EXPERIMENT_LOG.md`: dated execution, reproduction, and retention record.
- `results/retrieval/`: the 13 question-level top-10 contexts for each arm.
- `results/l1/`: deterministic per-question and aggregate L1 metrics.
- `results/RESULTS_SUMMARY.md`: concise interpretation.
- `results/reference_penalty_sensitivity_all53_v1/`: deterministic comparison
  of the legacy numerical penalty and the simplified active ranking.
- `manifest.json`: SHA-256 provenance for all retained artifacts.
- `scripts/run_ablation.py`: complete local reproduction script.
- `scripts/validate_ablation.py`: hash, membership, context, and metric checks.

## Reproduction

Use the repository Python environment and local Chroma collection:

```bash
HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 .venv/bin/python \
  benchmark/ablations/dev13_dense_bm25_only_v1/scripts/run_ablation.py \
  --out /private/tmp/dev13_dense_bm25_only_v1_reproduction \
  --device cpu
```

Validate the retained package:

```bash
.venv/bin/python \
  benchmark/ablations/dev13_dense_bm25_only_v1/scripts/validate_ablation.py
```

The originating run processed 13 questions over 29,805 chunks with no API
calls. Its combined local runtime was 14.07 seconds after model availability
and collection setup. Runtime is hardware- and cache-dependent.

## Interpretation Limits

- Results are based on 13 development questions and are descriptive.
- The Dense-only/BM25-only component ablation did not use Test40. Test40 was
  included only in the later deterministic penalty-retirement sensitivity
  check and was not used to select or tune a retrieval system.
- This package cannot alter the frozen retrieval parameters or formal Test40
  conclusions.
- Negative-gold recall applies to six Dev13 questions and is only diagnostic.

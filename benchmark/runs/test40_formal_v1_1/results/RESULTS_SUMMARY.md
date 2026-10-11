# Formal Test40 Results

Status: complete
Execution date: 2026-07-30
Pre-run tag: `test40-formal-v1.1-prerun-2026-07-30`

## L1 Retrieval

| System | MRR required gold | Required gold recall@10 | Gold document recall@10 | Negative gold recall@10 |
|---|---:|---:|---:|---:|
| Hybrid | 0.334 | 0.403 | 0.621 | 0.233 |
| BGE | 0.353 | 0.408 | 0.619 | 0.300 |
| BGE-LLM | 0.551 | 0.516 | 0.698 | 0.433 |

## L1.5 Citation-Support Sanity

| System | Supported cited-claim rate | Mean question-level support | Unsupported claims | Contradicted claims |
|---|---:|---:|---:|---:|
| Hybrid | 0.992 | 0.990 | 4 | 0 |
| BGE | 0.981 | 0.982 | 10 | 0 |
| BGE-LLM | 0.985 | 0.988 | 7 | 2 |

L1.5 is supplementary and is not used as the primary answer-quality result.

## L3 Final-Answer Evaluation

The primary value is the equal mean of three complete repeat-specific system
means. The uncertainty value is the sample standard deviation across those
three means and is not a confidence interval.

| System | Mean component-balanced core reference-claim coverage | Sample SD |
|---|---:|---:|
| Hybrid | 0.503 | 0.015 |
| BGE | 0.498 | 0.006 |
| BGE-LLM | 0.573 | 0.021 |

BGE-LLM had the highest primary L3 score in every repeat. Its three-repeat
mean was 0.070 higher than Hybrid and 0.075 higher than BGE.

## Usage And Cost

- Valid paid calls: 760
- Tracked tokens: 6,241,725
- Tracked cost: USD 20.1561
- Schema-invalid responses rejected before scoring: 3
- Estimated bill including those three rejected responses: approximately
  USD 20.24

The rejected responses were `hybrid::NQ03a` and `bge::WF10_011` in L3 repeat
2, and `bge_llm::NQ25` in L3 repeat 3. Each was replaced only through
request-hash-validated resume; no other completed judgment was repeated.

No Test40 result was used to alter questions, gold evidence, retrieval
parameters, prompts, models, metrics, repeat count, or aggregation.

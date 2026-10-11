# Layer B V2 Development Record

Date: 2026-08-04

## Why V17 Was Not Sufficient

The V17 judge assigned broad critical-analysis, professional-depth, and
outlook grades separately to each required component. That design had three
problems visible in the RT01 and earlier RT09 pilots:

1. fluent general prose could satisfy a broad rubric without using
   condition-bound empirical observations;
2. every component was implicitly required to contain its own outlook, even
   when outlook is naturally a review-level operation; and
3. frozen boundary violations were reported but did not reduce the numeric
   score.

## Side-Chat Design Basis

The WaterRAG review-task discussion separated short visible task components
from a strict hidden evaluator. It distinguished completeness, depth,
evidence use, critical analysis, and technical rigor, while warning that
source quantity, citation support, and extraction correctness must be audited
separately. It also emphasized cross-study synthesis, condition-linked
quantitative evidence, endpoint discipline, practical implications, and
specific future needs rather than generic calls for more research.

Layer B V2 implements those ideas without folding Layer A into a composite.
Evidence is assessed in two different senses:

- Layer A verifies how much nonredundant evidence was acquired and whether
  extracted fields and final claims are source-supported.
- Layer B asks whether the anonymous review visibly uses empirical
  observations and appropriately placed citations to perform analysis. It
  receives neutralized `R##` markers but no source packet or entailment result.

## Scoring

The judge returns no number. The local scorer maps atomic statuses to 1, 0.5,
or 0, averages atoms within each global dimension, and applies the frozen
40/35/25 dimension weights. The final score is the minimum of the uncapped
quality score, mean task-component fulfillment, calibration cap, and boundary
cap. All intermediate values remain reportable.

V20 copies the independently audited V18 method without changing the judge
rubric and raises only the Layer B output ceiling after V19 truncation.
It authorizes only retrospective rejudging of the fixed V17 RT01 artifacts;
RT01 is not a prospective validation task.

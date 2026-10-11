# Formal V1 Freeze Decision

Date: 2026-08-04  
Decision: approved for the formal ten-task Results Section 3.4 experiment

## Frozen Scope

- Tasks: RT01-RT10
- Systems: BGE-LLM local RAG, GPT-5.1 Web Search, and matched GPT-5.1 Direct
- Model snapshot: `gpt-5.1-2025-11-13`
- Reasoning effort: low
- Source-screening ceiling: 20 candidates
- Minimum evidence gate: 6 retained primary sources
- Within-document budget: 8 chunks per selected local document
- Layer A: verified evidence acquisition, extraction, and source-support metrics
- Layer B: one canonical citation-aware anonymous judgment per answer
- Layer B primary metric: `atomic_component_capped_review_quality`
- Formal error bar: sample SD across ten task-level scores

## Pre-Freeze Evidence

1. The no-API coverage pilot found all four query dimensions for every task,
   at least ten likely-primary documents in each top-20 pool, and zero defining
   review hits after task-scoped exclusion.
2. Claude Sonnet rated the ten-task set `READY WITH MINOR REVISIONS` and
   requested no wording changes. Its three feasibility checks were satisfied
   by the recorded coverage pilot.
3. The prospective RT02/RT09 judge-stability calibration reused four fixed
   answers not used in V20 judge development. Twelve new GPT-5.1 judgments
   passed all prespecified limits: mean per-answer SD 0.0177, maximum
   per-answer SD 0.0180, and maximum repeat deviation 0.0208.
4. Direct cannot be verified as leave-one-review-out because model-weight
   exposure is unknowable. It is frozen as a no-retrieval baseline.

## Analysis Boundary

Formal results may be summarized and visualized but must not be used to alter
the task text, task ledgers, defining-review exclusions, retrieval budgets,
prompts, model, repeat policy, score mapping, or aggregation. Any correction
requires a versioned successor with an explicit change record.

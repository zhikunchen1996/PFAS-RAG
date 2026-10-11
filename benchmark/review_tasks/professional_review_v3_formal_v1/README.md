# PFAS Professional-Review Experiment: Formal V1

Status: frozen formal execution package  
Date: 2026-08-04  
Scope: manuscript Results Section 3.4

## Objective

Evaluate whether a local PFAS literature-grounded RAG system produces stronger
professional evidence reviews than GPT-5.1 Web Search and matched GPT-5.1
Direct. The ten researcher-facing tasks were derived bottom-up from five
full-text PFAS reviews. Each task's defining review and all of its chunks are
excluded before candidate retrieval.

## Systems

1. `bge_llm_local_rag`: local dense retrieval, BGE reranking, GPT-5.1 document
   selection, within-document expansion, structured extraction, verification,
   and synthesis.
2. `gpt51_web_search`: GPT-5.1 Web Search with matched source screening,
   extraction, verification, and synthesis.
3. `gpt51_direct`: matched GPT-5.1 scientific synthesis without retrieval,
   Web Search, evidence extraction, or invented study citations.

The visible task, scientific role, answer structure, lack of a word limit,
reasoning effort, model snapshot, and synthesis ceiling are matched. The
intended treatment difference is evidence access.

## Frozen Tasks and Exclusion

- Ten tasks: RT01-RT10
- Five defining full-text reviews
- Three required components per task
- Six-source minimum evidence gate for retrieval-enabled systems
- Twenty-source candidate-screening ceiling
- Defining-review exclusion by normalized DOI, stable URL, exact corpus source,
  and normalized exact title
- Coverage pilot: all four query dimensions covered for every task and zero
  post-filter anchor hits

The Direct condition does not receive the defining review in its prompt, but
review exposure in model pretraining cannot be removed or verified. It must be
reported as a no-retrieval baseline rather than a verified leave-one-review-out
condition.

## Evaluation

### Layer A: Evidence Acquisition and Extraction

Layer A applies to BGE-LLM and Web Search. Primary outcomes include verified
usable evidence-record yield, verified independent-source yield, weighted
field support, endpoint accuracy when applicable, final-review source support,
claim citation coverage, and unique cited sources. Direct has zero retrieved
records by design; denominator-based extraction metrics are not applicable.

### Layer B: Citation-Aware Review Synthesis

The candidate-blind task ledger defines three task components and two material
boundaries. One anonymous answer is judged per request. System-specific source
IDs are deterministically mapped to neutral `[R##]` markers while preserving
citation placement and repeated-source relationships.

The continuous primary metric is
`atomic_component_capped_review_quality`. It combines:

- critical synthesis: 40%;
- professional depth: 35%; and
- current research and outlook: 25%.

Component fulfillment and material inconsistency are explicit caps rather than
additional weights. No binary pass threshold is used.

## Judge Repeat Policy and Error Bars

The formal run uses one canonical GPT-5.1 judge call per answer. This decision
was fixed after a prospective V20 stability calibration on four fixed RT02 and
RT09 answers:

- mean per-answer sample SD: 0.0177;
- maximum per-answer sample SD: 0.0180; and
- maximum repeat deviation: 0.0208.

All prespecified stability limits passed. Formal system values are the mean of
the ten task-level scores. Error bars are the sample SD across those ten task
scores, not judge-repeat SD.

## Reproducibility and Cost

Every paid response is persisted immediately. Resume is allowed only when the
new request hash matches the stored request exactly. Token use, dated API cost,
and latency are recorded by stage. The pre-run budget estimate is USD 44-50;
the final report must use tracked usage.

## Validation

```bash
.venv/bin/python -m unittest discover \
  -s benchmark/review_tasks/professional_review_v3_formal_v1/tests -v

.venv/bin/python \
  benchmark/review_tasks/professional_review_v3_formal_v1/scripts/validate_draft.py

.venv/bin/python \
  benchmark/review_tasks/professional_review_v3_formal_v1/scripts/build_freeze_manifest.py \
  --verify
```

After execution:

```bash
.venv/bin/python \
  benchmark/review_tasks/professional_review_v3_formal_v1/scripts/validate_review_run.py \
  --run-dir benchmark/review_tasks/runs/professional_review_v3_formal_v1
```

## Formal Run

```bash
.venv/bin/python \
  benchmark/review_tasks/professional_review_v3_formal_v1/scripts/run_review_experiment.py \
  --run-dir benchmark/review_tasks/runs/professional_review_v3_formal_v1 \
  --task-ids RT01 RT02 RT03 RT04 RT05 RT06 RT07 RT08 RT09 RT10 \
  --systems bge_llm_local_rag gpt51_web_search gpt51_direct \
  --stages retrieval extraction verification synthesis source_support review_judge summary \
  --judge-repeats 1 \
  --workers 4 \
  --allow-paid
```

Formal results cannot be used to change the frozen tasks, prompts, retrieval
budgets, model, metrics, or aggregation. Any correction requires a versioned
successor.

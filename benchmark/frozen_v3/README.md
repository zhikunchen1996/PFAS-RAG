# PFAS RAG Frozen V3

Status: `revision3_dev13_neutral_judge_validated_test40_not_run`

Freeze date: 2026-07-26

Frozen V3 Revision 3 is the canonical question-aware PFAS RAG configuration
developed after Frozen V2. It retains 53 questions and 249 non-exhaustive
chunk-based gold records after a project-author retention confirmation.
The registers record that blanket retention decision; they do not provide
item-specific rationales or erase historical machine-review flags. This is
not independent double annotation. Frozen V2 remains the last package with
completed Test40 results; V3 Test40 has not run.

This is the repository's single active frozen package. The canonical L1,
L1.5, and L2 V2 evaluation implementation is nested under `judge/`, including
its prompts, calibration outputs, statistical aggregation, audits, tests, and
the Dev13 common-tagger source package required for provenance. The system
subset and judge subset retain separate SHA-256 manifests so each historical
freeze boundary can be validated independently.

## Canonical system

1. Hybrid retrieval produces an initial pool of 60 chunks.
2. `BAAI/bge-reranker-base` produces a 30-chunk shortlist.
3. GPT-5.1 selects the final 10 full chunks using the visible question only.
4. GPT-5.1 assigns question-dependent advisory evidence-role and detail-policy
   tags without access to gold.
5. GPT-5.1 generates the answer from all 10 full chunks at temperature 0.

The tags do not remove, truncate, or reorder chunks. The answer-visible tag
interface contains only categorical evidence role, categorical detail policy,
categorical evidence polarity, confidence, and a locally verified verbatim
excerpt. Question-component descriptions and component assignments are stored
for audit only. Tagger-generated free-text advice is never exposed to the
answer model.

## Self-contained runtime

Frozen V3 does not import code from Frozen V2, `benchmark/reports`,
`benchmark/src`, or `src/rag_app`.

- Generation and judging utilities are internalized in
  `scripts/runtime_helpers.py`.
- Retrieval metric formulas are internalized in
  `scripts/retrieval_metrics.py`.
- The exact GPT-5.1 `10/30/60` retrieval output used for answer generation is
  the middle configuration under
  `results/dev13_retrieval_budget_gpt51_2026-07-26/bge_llm_gpt51`.
- Python requirements and the Python-version record are copied under
  `environment`.
- Promoted data are locked by
  `methods/promoted_reusable_artifacts.json`.

Historical source paths remain only as provenance strings inside the promoted
artifact manifest and byte-identical archived metadata. No canonical V3
runtime or validation command reads those source paths.

## Canonical evaluation

The Dev13 confirmation compares the final Frozen V3 system with a
prompt-matched GPT-5.1 Direct baseline. The neutral-evidence judge:

- uses GPT-5.1 at temperature 0;
- uses three temperature-zero API re-samples with both answer orientations;
- receives non-exhaustive reference evidence and a deduplicated union of
  Hybrid, BGE, and BGE-LLM top-10 verification passages;
- receives no system name, question ID, task label, answerability label,
  repeat number, or orientation;
- receives both answers after `[C#]` markers are removed;
- does not score citation behavior or retrieval performance.

The common verification union contains 20.8 chunks per question on average.
Because it is assembled from the three evaluated retrieval systems, all ten
canonical BGE-LLM RAG chunks are necessarily present and about 3.9 chunks per
question are unique to that system. This is substantially less asymmetric
than the superseded RAG-owned-context judge, but it does not make Direct an
information-matched generation arm: Direct remains the intended no-retrieval
baseline.

The four criterion weights are:

- scientific correctness: 0.40;
- question fulfillment: 0.30;
- uncertainty and limitations: 0.15;
- practical usefulness: 0.15.

The final Dev13 result is 10 Frozen V3 wins, 3 Direct wins, and 0 ties. Mean
weighted Frozen V3 score is 0.7846 and mirrored criterion agreement is 0.7692.
The returned model snapshot is `gpt-5.1-2025-11-13`.

Canonical result:

`results/dev13_neutral_evidence_v3_2026-07-26`

The source generation run is:

`results/dev13_verified_tags_v3_r2_confirmation_2026-07-26`

## Retrieval-budget analysis

The V2 Hybrid and no-cap BGE Dev13 outputs were copied byte-for-byte with
their original provenance. The three BGE-LLM budgets were rerun using GPT-5.1
at temperature 0 and complete candidate chunks:

| System | Budget | Required-gold recall | Gold-document recall | MRR |
| --- | --- | ---: | ---: | ---: |
| Hybrid | 5/30 | 0.200 | 0.301 | 0.169 |
| Hybrid | 10/60 | 0.200 | 0.454 | 0.158 |
| Hybrid | 20/120 | 0.200 | 0.663 | 0.113 |
| BGE | 5/30 | 0.211 | 0.368 | 0.174 |
| BGE | 10/60 | 0.278 | 0.464 | 0.180 |
| BGE | 20/120 | 0.389 | 0.658 | 0.173 |
| BGE-LLM | 5/15/30 | 0.311 | 0.568 | 0.361 |
| BGE-LLM | 10/30/60 | 0.372 | 0.610 | 0.426 |
| BGE-LLM | 20/60/120 | 0.442 | 0.696 | 0.388 |

The middle BGE-LLM budget has the highest MRR, while the largest budget has
the highest evidence coverage. The 39 GPT-5.1 selector calls used 575,659
tokens at an estimated cost of USD 0.9129.

Required-gold recall, gold-document recall, and MRR are macro-averaged over the
12 of 13 Dev questions with at least one required-gold record. Six Dev
questions contain negative gold. Their retrieval is reported separately in
`negative_gold_retrieval_summary.csv`; at the selected 10/60 budget, mean
negative-gold recall is 0.000 for Hybrid, 0.222 for BGE, and 0.389 for BGE-LLM.

Budget result:

`results/dev13_retrieval_budget_gpt51_2026-07-26`

## Judge sensitivity and development diagnostics

For the same Revision 1 answers, the citation-blind judge favored Direct 8-5,
whereas the source-verified judge favored RAG 13-0. The latter exposed system
labels and evaluator-only task metadata and used only the RAG-selected context
for verification. These results are retained and must be reported as judge
sensitivity, not as competing headline results. Revision 3 removes those
leaks, uses a multi-retriever evidence union, and produces the canonical 10-3
result on the selector-aligned Revision 2 answers.

The old matched tagged-versus-untagged diagnostic is retained only as
historical exploration. It used Revision 1 answers and a superseded judge, so
it is not evidence for tag efficacy under the canonical Revision 3 protocol.

Revision 1 also used a compact selector prompt for answer generation while the
budget sweep used the expanded frozen selector prompt. Its top-ten contexts
differed from the budget sweep for every Dev13 question. Revision 2 therefore
regenerated all tags and answers from the budget sweep's exact `10/30/60`
retrieval output. Revision 1 is historical and excluded from the selected
result hash boundary. The historical 5:8 citation-blind result also has a
tagger-prompt hash mismatch and is not exactly prompt-reproducible from this
package.

In the canonical generation run, 39 of 130 tagger excerpts failed local
verbatim validation. Those excerpt strings were removed before answer
generation; the categorical tags remained advisory and were not independently
verified. This distinction is recorded explicitly rather than describing the
entire tag as verified.

The neutral judge required non-scoring schema normalization in 17 of 78
responses (21.8%), totaling 51 auxiliary-field repairs. All scored criterion
preferences and rationales were present. Mirrored criterion agreement was
0.7692, so the small Dev13 comparison retains meaningful judge uncertainty.

## Freeze boundary

- Dev13 was used for system development and confirmation.
- Test40 was not run for the Frozen V3 system before this freeze.
- Frozen V2 Test40 results do not become Frozen V3 results.
- The final integrity boundary is defined by `freeze_manifest.json`.
- All runtime code, selected retrieval input, prompts, environment records,
  and promoted results are internal and locked by SHA-256.
- The manifest records whether every selected V3 file was Git-tracked when it
  was built; local hashes do not substitute for committing the package.
- `freeze_manifest.json` covers the original Frozen V3 system subset and
  explicitly excludes the nested `judge/` package.
- `judge/freeze_manifest.json` independently covers the judge package and
  hashes its canonical inputs from the parent V3 system.

The earlier free-text fields `allowed_use`, `avoid_use`, and `omit_details`
were removed before the current freeze because they could remain visible when
an accompanying `exact_support` failed verbatim validation. The current
formatter also drops these legacy keys defensively. Invalid excerpts are
cleared locally, and only verified source text plus categorical tags can reach
the answer model.

## Canonical files

- `methods/frozen_v3_protocol.json`
- `methods/canonical_evaluation.json`
- `judge/methods/protocol.json`
- `judge/freeze_manifest.json`
- `methods/dev13_verified_tags_v3_protocol.json`
- `methods/dev13_neutral_evidence_judge_v3_protocol.json`
- `methods/author_review_record.json`
- `methods/freeze_audit_revision3_2026-07-26.md`
- `prompts/evaluation/soft_eligibility_tagger_v3.txt`
- `prompts/evaluation/rag_answer_prompt_soft_tags_v3.txt`
- `prompts/evaluation/direct_answer_prompt_matched_v3.txt`
- `prompts/evaluation/neutral_evidence_pairwise_content_v3.txt`
- `scripts/run_dev13_soft_tags_v3.py`
- `scripts/run_dev13_neutral_evidence_judge_v3.py`
- `scripts/run_dev13_budget_bge_llm_gpt51.py`
- `scripts/finalize_dev13_retrieval_budget_gpt51.py`
- `scripts/runtime_helpers.py`
- `scripts/retrieval_metrics.py`
- `scripts/validate_self_contained_v3.py`
- `scripts/validate_task_general_prompt.py`
- `freeze_manifest.json`

## Validation

Use the repository virtual environment:

```bash
.venv/bin/python benchmark/frozen_v3/scripts/validate_task_general_prompt.py
.venv/bin/python benchmark/frozen_v3/scripts/validate_self_contained_v3.py
.venv/bin/python -m unittest discover -s benchmark/frozen_v3/tests
.venv/bin/python -m unittest discover -s benchmark/tests
.venv/bin/python benchmark/frozen_v3/scripts/build_freeze_manifest.py --verify
```

Generation, historical judge, and neutral-evidence judge commands are recorded
in the corresponding result READMEs and session logs. Runtime scripts require
an explicit output directory and refuse to overwrite non-empty frozen results.

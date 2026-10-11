# Professional PFAS Review Experiment V3

Status: RT01 retrospective calibration V20; paid calls stage-restricted  
Updated: 2026-08-04

## Purpose

V3 is the literature-derived, extraction-first design for Results Section 3.4.
It tests whether a retrieval system can:

1. find independent primary studies after the review that defined a task is
   held out;
2. extract source-verifiable study data; and
3. synthesize those data into a focused professional review.

It does not alter the frozen experiments reported in Results Sections
3.1--3.3.

## Bottom-Up Task Design

Ten focused review questions were derived from five full-text reviews in the
active corpus. A review may define more than one task when it contains
independent researcher decisions. The task, rather than the source review, is
the unit of evaluation.

The visible tasks retain only:

- scientific scope;
- relevant comparison axes;
- engineering and implementation constraints; and
- research gaps that motivate the focused question.

Study-specific values, named best technologies, answer-bearing rankings, and
anchor-review conclusions were not transferred into a task. The source chunks
used during design are recorded in:

```text
provenance/task_design_provenance.jsonl
provenance/source_snapshots/RT01.json ... RT10.json
```

Snapshots contain identifiers, hashes, and bounded previews for method audit.
They are not candidate evidence and must never be passed to a candidate
system.

## Ten Focused Review Tasks

| Tasks | Focused decisions | Defining review |
|---|---|---|
| RT01--RT03 | Adsorbent selection, laboratory-to-field translation, and media end of service | Lei et al. (2023) |
| RT04--RT05 | Membrane selection and management of retained PFAS streams | Jin et al. (2021) |
| RT06--RT07 | Foam-fractionation operation and treatment-train placement | We et al. (2024) |
| RT08--RT09 | Destructive-technology selection and evidence for meaningful destruction | Blotevogel et al. (2023) |
| RT10 | Matrix-representative treatment-study design | Zeidabadi et al. (2023) |

The visible questions are in `input/review_tasks_human_audit.md`. Exact DOI,
title, source filename, task mapping, and scope role are in
`input/anchor_reviews.jsonl`.

## Anchor Exclusion

The five defining reviews are present in the active corpus. For every task,
its defining review is removed before candidate document ranking or
within-document expansion. Tasks sharing a review therefore share the same
exclusion, but use different briefs, components, and task boundaries.

The deterministic filter matches:

- normalized DOI;
- normalized stable URL;
- exact corpus source filename; and
- normalized exact title.

Web Search must apply the same DOI, URL, and title block list during source
capture and reject any final record that resolves to the task's defining
review.

A closed-book Direct model cannot receive a verifiable anchor exclusion
because a review cannot be removed from pretrained weights. It receives no
retrieved evidence, browsing tool, post-hoc retrieval, benchmark source IDs,
structured extraction, or source-support judge. This limitation is stated
explicitly rather than being described as a verified anchor exclusion.

## Extraction-First Workflow

```text
focused literature-derived review brief
  -> task-scoped anchor exclusion
  -> candidate document retrieval
  -> within-document evidence expansion
  -> structured primary-study extraction
  -> source-level field verification
  -> verified evidence table
  -> focused cross-study professional review
```

One extraction record represents one primary-study experiment, modeled
scenario, or field deployment. Every populated source-dependent field carries
one or more exact evidence locators. Review articles may assist discovery but
cannot supply a quantitative evidence record.

Each extraction request receives a source-specific strict schema. The schema
enumerates the permitted task ID, system ID, source ID, and evidence-locator
IDs from the already frozen source packet. This prevents a model-generated
locator from silently referring to nonexistent evidence. A deterministic
post-schema check accepts valid thousands separators, logs the unambiguous
normalization of a bare number already declared `approximate_numeric`, and
removes ambiguous malformed quantitative fields while retaining the rest of
an otherwise valid record.

After initial source verification, a deterministic audit checks mandatory
quantitative value/unit, operating-condition value/unit, endpoint-type, and
comparability-status paths. If a path was omitted, one narrow completion
request assesses exactly the missing paths. It cannot revise earlier
assessments, and final record eligibility is the logical AND of the initial
and completion decisions.

The raw synthesis response is retained. A deterministic postprocessor removes
only complete parenthetical task, component, or boundary labels that the
prompt already prohibits, such as `(RT09-C1)` or `(C2)`. It records the removed
spans plus raw and final hashes. A bare internal label causes failure rather
than broader text rewriting; scientific content is never edited by this step.

The postprocessor also canonicalizes record-level citation IDs only when they
occur inside citation brackets. For example, `[S01-R03]` becomes `[S01]` and
`[S01, S01-R02]` becomes `[S01]`. The record belongs unambiguously to that
source, so this changes citation granularity rather than scientific content.
Every replacement and both raw and final hashes are retained. Record-like text
outside citation brackets is never changed.

Before synthesis, every usable verified record is projected into a compact
ledger. The complete structured record and every field path, support status,
and error type are retained. Verifier explanations are omitted for fields
marked `supported` because they repeat the record and supporting excerpts;
reasons remain present for `partially_supported`, `unsupported`, and
`contradicted` fields. Complete supporting excerpts for every source
represented by a usable record are still supplied. This projection changes no
source, record, value, endpoint, eligibility decision, or citation locator.

The synthesis renderer removes internal task, component, constraint, and
boundary identifiers before the request is sent. It retains every natural-
language component requirement, task boundary, and material-violation rule.
Internal identifiers remain available to validation and judging code but are
not shown to the answer model, preventing benchmark notation from leaking into
the professional review.

Supporting excerpts are also projected through an explicit allowlist. Source
identity, access limitations, locator IDs, sections, passage type, and complete
evidence text remain visible. Retrieval ranks, BGE scores, per-query scores,
and covered-component IDs are excluded because they are retrieval provenance,
not scientific evidence, and can contain internal benchmark identifiers.

The source-support diagnostic receives the same compact verified-record and
supporting-excerpt views as synthesis. It still receives the complete candidate
review, every substantive field status, every non-supported reason, and all
complete evidence text. This avoids repeating verifier prose and retrieval
metadata without weakening claim-level source checking.

## Coverage Pilot

The redesigned tasks were rerun with local BGE dense retrieval after anchor
exclusion. All ten tasks:

- returned zero defining-review hits;
- covered the umbrella brief and all three components in the top 20; and
- retained 14--19 heuristic likely-primary documents in the top 20.

These are source-type screening diagnostics, not confirmed eligible-study
counts.

## Candidate Systems

V20 compares three information-access conditions:

- **BGE-LLM local RAG:** the local full-text corpus, BGE document reranking,
  GPT-5.1 document eligibility selection, common extraction, and verification;
- **GPT-5.1 Web Search:** external Web Search followed by the same structured
  extraction and verification stages; and
- **GPT-5.1 Direct:** the same visible scientific review task and output token
  ceiling, but no retrieval or evidence packet.

BGE-only is omitted because its retrieval contribution is already evaluated in
Results Section 3.2. Repeating it here would add cost without answering the
Section 3.4 information-access question.

## Comparability And Known Limits

BGE-LLM and Web Search share a 20-source candidate-screening ceiling before
common extraction, verification, and synthesis. There is no fixed final source
count. BGE-LLM classifies every one of the 20 local cards and retains all
primary, task-relevant documents with extractable evidence. Web Search inspects
up to 20 eligible primary sources and retains every source that survives URL,
identity, duplicate, source-type, and anchor checks. A six-source minimum is a
failure gate, not a final quota. Final retained and cited source counts are
reported as system outcomes. Direct has no source budget because retrieval is
disabled.

This design fixes retrieval effort rather than forcing equal evidence counts.
It therefore permits a system that finds more eligible studies to use them,
while keeping the screening ceiling reproducible. A failed frozen
source-capture response is not deleted and retried; a scientifically justified
change requires a new versioned request and run directory.

Extraction and source verification are independent requests but use the same
frozen GPT-5.1 snapshot. Web Search inspected URLs are checked against the
API-returned consulted-source list, but the exact fidelity of a passage marked
`verbatim` is model-reported rather than established by an independent page
refetch. Both limitations are retained for the manuscript and human audit.

The task is the unit of analysis. Equal task weighting therefore gives topic
families represented by several focused tasks more influence than a defining
review represented by one task; per-task results will accompany aggregate
results.

## Evaluation

The end-to-end task has two co-primary layers. They are reported separately;
there is no weighted overall score.

Layer A measures verified evidence acquisition and extraction. A usable record
counts only after common source eligibility, exclusion, deduplication,
field-level verification, and final-usability checks. This is verified useful
evidence yield under the matched screening protocol, not recall of an
exhaustive literature universe.

Layer A primary metrics:

- verified usable evidence-record yield;
- verified independent-source yield;
- weighted extracted-field support;
- endpoint-classification accuracy when relevant to the task; and
- weighted final-review claim source support;
- source-dependent claim citation coverage; and
- unique cited-source count.

Layer A diagnostics include:

- supported extracted-field rate;
- numeric transcription accuracy;
- endpoint classification accuracy;
- verified primary-study record and unique-study counts;
- comparability-status accuracy; and
- cited-source publication-status and stable-identifier fractions;
- raw citation-marker count, reported only as a diagnostic; and
- anchor-exclusion violations.

Layer A applies to BGE-LLM and Web Search. For Direct, retrieved record and
source counts are zero by design, while denominator-based extraction accuracy
and source-support rates are `N/A`; absence of an extraction process is not
misreported as inaccurate extraction.

Numeric transcription accuracy is calculated only from the required
`quantitative_findings` value and unit assessments. Operating-condition values
and units are still mandatory verification fields and contribute to overall
field support. For numeric, endpoint, and comparability accuracy, a field is
accurate when its verification status is `supported`; `error_type` is retained
only to explain non-supported fields.

Layer B V2 measures citation-aware synthesis in two explicit stages. First,
each of the three task components is judged `full`, `partial`, `absent`, or
`contradicted`. Second, fourteen global review operations are judged on the
same scale: four critical-synthesis operations, five professional-depth
operations plus citation-evidence integration, and four
current-research/outlook operations. The three global
dimensions retain the WaterRAG-inspired 40%, 35%, and 25% weights.

Numeric scores are calculated locally. Mean component fulfillment is a score
cap rather than a fourth subjective weight. A material internal-calibration
inconsistency or frozen-boundary violation also applies an explicit cap. This
prevents fluent generic prose, repeated descriptions, or a review that misses
a required component from reaching the ceiling.

Layer B does not see original source identities, verified-field status,
citation entailment results, system identity, or retrieval scores. It judges
whether major source-dependent claims are cited, citations are attached to
identifiable claims, and multiple nonredundant sources support distinct parts
of the analysis. Verification, metadata-based reference quality, source counts,
and evidence yield remain Layer A outcomes. Before the request is built, the
runner maps system-specific `[S##]` and `[WEB##]` identifiers to neutral
`[R##]` markers while preserving citation placement and repeated-source
relationships. It writes the anonymized text and a hash audit beside the
original review.

This division follows the WaterRAG review criteria rather than a
citation-blind comparison. WaterRAG's evidence criterion asks whether major
claims have robust support from multiple recent high-quality sources, and its
professional-depth criterion includes data support, literature citations, and
reference quality. V20 makes that logic auditable: Layer B scores visible
citation-aware synthesis, while Layer A verifies whether the cited sources and
their claimed support are real and appropriate.

For Direct, `empirical_data_use` and `citation_evidence_integration` are
structurally constrained by the closed-book prompt, which prohibits invented
study-specific evidence and citations. Its professional-depth score therefore
is not a pure prose-synthesis score; this is an intended limitation of the
no-retrieval baseline and must be stated wherever Layer B is reported.

The two layers support directional interpretation: improved Layer A with
similar Layer B means better verified evidence acquisition at comparable
synthesis quality; improvement in both supports a stronger end-to-end review
system. No arbitrary exchange rate is imposed between the layers.
The layers are not statistically independent: evidence acquired in Layer A is
the material used for empirical synthesis and citation integration in Layer B.
An `A up / B up` result versus Direct is therefore one directional signal of
evidence-grounded review capability, not two independent confirmations.

## Development Validation Gates

The matched 20-source screening ceiling, variable retained-source count,
six-source minimum gate, GPT-5.1 snapshot, low reasoning effort,
extraction/verification/synthesis prompts, three-repeat review judge, exact
request-hash resume policy, stage-level token/cost/latency accounting, and ten
visible tasks are fixed in `protocol.json`. The executable runner and completed
run validator are implemented.

This successor was created by applying the following development gates:

1. run all unit and structural validators;
2. verify variable source counts and complete candidate classification;
3. preserve V17 and its RT01 answers as immutable development provenance;
4. copy only the fixed RT01 candidate artifacts into a separate calibration
   run with a complete hash ledger; and
5. authorize only `source_support`, `review_judge`, and `summary` for RT01.

V20 does not regenerate candidate answers. Because V18 was designed after
inspecting V17 RT01, this rejudging is retrospective calibration, not
prospective validation. No RT01 result may be used to modify the V20 prompt,
metric, or aggregation and still retain this package identity.

Pilot findings may create a separately versioned successor. They may not
silently alter a hashed candidate, tune the ten visible questions to favor a
system, or change Results Sections 3.1--3.3.

Local validation:

```bash
.venv/bin/python -m unittest discover \
  -s benchmark/review_tasks/professional_review_v3_pilot_candidate_v20/tests -v

.venv/bin/python \
  benchmark/review_tasks/professional_review_v3_pilot_candidate_v20/scripts/validate_draft.py

.venv/bin/python \
  benchmark/review_tasks/professional_review_v3_pilot_candidate_v20/scripts/validate_review_run.py \
  --run-dir <completed-run-directory>
```

Compact provenance snapshots can be rebuilt without an embedding model or API:

```bash
.venv/bin/python \
  benchmark/review_tasks/professional_review_v3_pilot_candidate_v20/scripts/build_compact_design_snapshots.py
```

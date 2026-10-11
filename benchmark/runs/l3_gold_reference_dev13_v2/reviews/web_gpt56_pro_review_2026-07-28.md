# Web GPT-5.6 Pro review

## Review metadata

- Date: 2026-07-28
- Reviewer surface: ChatGPT web
- Model shown in the UI: GPT-5.6 Sol
- Reasoning mode shown in the UI: Pro
- Conversation: https://chatgpt.com/c/6a6973f7-68a8-83ea-97ba-816411fd59d8
- Scope: L3 methodology, reference construction, candidate scoring, human audit, and freeze readiness
- Input: a structured description of the project, the full operative protocol, prompt rules, Dev13 construction statistics, the proposed metric definitions, and the prior Claude review outcome
- Limitation: Chrome file upload was disabled because the extension did not have file-URL access. The web review therefore assessed the supplied protocol and prompt content, not the local implementation files line by line.

## Verdict

`REVISE_BEFORE_HUMAN_AUDIT`

The reviewer accepted the L2/L3 separation and the candidate-blind reference-construction design. It did not consider the approach invalid. The package was judged not ready for formal human approval or freeze because the reference ontology, scoring unit, pass calibration, and error adjudication were not yet sufficiently operationalized.

## Blocking findings

1. The current mutually exclusive `core/supporting/limitation/negative_boundary` taxonomy conflates importance with evidentiary function.
2. Raw atomic claims are not necessarily valid independent scoring units; duplicated or fragmented findings may receive excess weight.
3. The normative relationship between the reference prose and claim ledger is undefined.
4. `full/partial/absent/contradicted` needs explicit handling of qualifiers, mixed correct/incorrect statements, numeric equivalence, modality, and internal contradiction.
5. The current `core >= 0.5` and `all >= 0.5` pass rule is not defensible without Dev calibration; all-claim coverage should not be a pass gate.
6. Automated punishment of a "clear major scientific error" can conflict with the non-exhaustive-reference policy when the error requires external knowledge.
7. Matched Direct/RAG generation and answer anonymization need to be specified as executable contracts.
8. The Test40 reference-construction, audit, freeze, and scoring order needs to be explicit.

## Required protocol changes

### Orthogonal claim schema

Replace the current claim type with independent fields:

- `importance`: `core | supplementary`
- `function`: `affirmative | limitation | negative_finding | boundary_constraint`
- `scoring_role`: `required_content | optional_content | constraint_only`

A limitation or negative finding may be a core required claim. A constraint-only boundary should not enter the coverage denominator.

### Scored claim groups

Retain atomic claims for evidence auditing, but add:

- `task_component_id`
- `claim_group_id`
- `central_proposition`
- `material_qualifiers`

Merge duplicate evidence, summary/subclaim duplication, and fragments of the same finding. Compute coverage over unique claim groups, not raw atomic-claim rows.

### Normative scoring source

The frozen claim ledger should be the only normative scoring target. Human-readable reference prose should be removed from the judge input or explicitly declared non-normative.

### Claim-label rules

- `full`: central proposition and all material qualifiers are correct.
- `partial`: the central proposition is correct, no incompatible statement is present, but at least one prespecified material qualifier is omitted or weakened.
- `absent`: the central proposition is not expressed.
- `contradicted`: the answer states an incompatible proposition or material qualifier.

If correct and incorrect versions both appear and the incorrect version is not explicitly corrected, score `contradicted`.

Numeric claims require claim-specific accepted units, rounding, ranges, approximations, and partial/contradiction rules. No implicit global tolerance should be left to the judge.

### Error policy

Separate:

- `reference_anchored_material_error`: verifiable from the frozen ledger, task boundary, or the answer's internal contradiction.
- `potential_external_scientific_error`: machine flag only.

Only a reference-anchored error, or an external error confirmed by blinded human adjudication, may enter the pass gate.

### Matched generation and anonymization

Direct and RAG must match on model snapshot, instructions, question, task instruction, decoding, output budget, format, retry policy, and tool access. Retrieved context should be the only planned difference.

Before judging, apply a frozen transformation that removes system labels, citation markers, bibliographies, and explicit system-identity language without changing substantive prose. Preserve raw/anonymized mappings and hashes.

## Recommended metrics

The primary metric should be **mean component-balanced core reference-claim coverage**:

1. Average claim-group scores within each frozen task component.
2. Average component scores within each question.
3. Average question scores across the system.

This makes the primary result question-macro, component-balanced, and core-only.

Recommended supporting metrics:

- strict-core coverage, with only `full=1`
- supplementary coverage
- boundary compliance rate
- core contradiction rate
- human-confirmed major-error rate
- potential external-error flag rate, reported separately

All-claim coverage may remain descriptive, but should not be primary and should not enter pass/fail.

## Recommended pass rule

For system `s` and question `q`, pass only when:

1. question-level component-balanced core coverage is at least the Dev-calibrated threshold;
2. every task component has coverage of at least 0.5;
3. there is no contradicted core claim;
4. there is no material boundary violation; and
5. there is no human-confirmed major scientific error.

The threshold must be selected on Dev13 only. The suggested procedure is:

1. Freeze the Dev references first.
2. Obtain blinded human adequate/inadequate consensus labels for all planned Dev candidate-answer types.
3. Search thresholds from 0.50 to 0.95 in 0.05 increments using balanced accuracy.
4. Break ties by lower false-pass rate, then higher specificity, then higher threshold.
5. Check stability by leave-one-question-out analysis.
6. Freeze the threshold before inspecting Test40.

If the threshold is unstable or human-machine agreement is poor, retain continuous core coverage as primary and label binary pass as exploratory.

## Reliability recommendation

Repeated identical temperature-zero judge calls measure test-retest stability, not independent inter-rater validity.

Recommended procedure:

- primary run with a fixed claim order;
- reliability run with a preregistered reversed claim order;
- retain all disagreements;
- send disagreements affecting core score, contradiction, boundary, major error, or pass status to blinded human adjudication.

Report claim-level exact agreement, nominal Cohen's kappa, question-level mean absolute score difference, pass agreement, flag agreement, human-adjudication rate, and agreement with blinded human consensus.

## Statistical comparison

Claims are nested within questions. Direct/RAG effects must be calculated as paired question-level differences, with confidence intervals obtained by paired resampling over questions. Claims must not be treated as independent observations.

## Human-audit gate

Before reference freeze:

- define task components for every question;
- review every claim, not only the 22 claims flagged as non-fully-supported;
- resolve all 21 partial claims and the one unsupported claim;
- close all 20 reference issue notes with an action record;
- merge/deduplicate atomic claims into scored groups;
- confirm exact-span support and all compound, matrix, method, condition, unit, and endpoint qualifiers;
- record numeric equivalence rules where applicable;
- distinguish required content from constraint-only boundaries;
- verify that all reference prose maps to approved ledger claims;
- record every merge, split, deletion, and revision;
- obtain explicit human approval for all 13 questions;
- generate and verify a complete SHA-256 manifest.

## Freeze decision

The current package cannot be frozen.

The reviewer recommended this order:

1. revise the claim ontology and scoring unit;
2. perform full Dev13 human audit;
3. freeze and hash the Dev reference package;
4. calibrate candidate scoring and the binary threshold on blinded Dev answers;
5. freeze the judge, parser, metrics, anonymization, retry rules, and matched-generation contract;
6. construct and human-audit Test40 references without candidate exposure;
7. freeze Test40 references;
8. run the locked L3 analysis at the question level.

The reviewer summarized the status as: the L3 layering and leakage-control framework are sound, but reference ontology, score units, pass calibration, and error adjudication are not yet freeze-ready.

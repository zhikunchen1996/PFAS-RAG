# Topic-General V3 Prompt Design

Date: 2026-07-26

## Design objective

The V3 prompt must support unseen PFAS research topics and researcher
workflows, not reproduce a list of known development questions. Dev13 is an
evaluation set for the candidate, not a source of topic-specific prompt rules.
Test40 content is not inspected during prompt development.

## Research-operation layer

The system infers the requested operation from the visible question. It does
not receive or require a benchmark task label. Supported operations include:

- extraction or description;
- comparison or ranking;
- classification or distinction;
- explanation or interpretation;
- evidence synthesis;
- assessment of a proposed claim;
- identification of limitations, conflicts, or evidence gaps;
- a bounded evidence-based recommendation.

These operations may occur alone or in combination. They are not tied to a
particular PFAS compound, technology, matrix, analytical method, or study.

## Evidence-compatibility layer

For each material answer component, evidence is checked on the dimensions that
matter for the claim:

- subject, entity, compound, or population;
- intervention, process, material, instrument, or method;
- matrix, environment, sample type, or application context;
- study design, test mode, scale, and time basis;
- outcome, endpoint, metric definition, and evidence polarity;
- value, unit, denominator, uncertainty, and reporting basis;
- operating, analytical, or environmental conditions;
- comparison reference, system boundary, and level of generality.

A question need not involve every dimension. The tagger determines which
dimensions are material from the visible wording and uses those dimensions to
separate direct evidence from background and nearby but mismatched evidence.

## Detail-control layer

Detail policies describe how a chunk may be used without presupposing a topic:

- `use_full_claim`;
- `category_only`;
- `limitation_only`;
- `qualitative_relationship`;
- `quantitative_detail`;
- `procedural_detail`;
- `do_not_use`.

The policies are advisory. Full chunks remain visible, original ranking is
preserved, and proposed exact excerpts are checked locally for verbatim
presence.

## Anti-overfitting constraints

- No question ID or question-specific expected answer appears in the prompt.
- No named development-set study, value, condition, material, or technology is
  encoded as a special case.
- No fixed benchmark task label is supplied to the tagger or answer model.
- No fixed answer length is imposed.
- The same prompt operates on tagged and matched-untagged contexts.
- Test40 content remains unused during development.

## Evaluation boundary

This design is topic-general within literature-grounded PFAS research. It does
not claim universal performance outside that domain. Dev13 testing determines
whether the tag layer helps on development data; it cannot by itself prove
generalization. Any later assessment on unseen questions must use a prompt
frozen before those questions are examined.

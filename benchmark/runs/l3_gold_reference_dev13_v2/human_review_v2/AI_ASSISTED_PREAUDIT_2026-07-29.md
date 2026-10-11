# AI-Assisted Project-Author Pre-Audit

Date: 2026-07-29

## Status and provenance

This document is an independent, AI-assisted pre-audit of the 13 Dev
reference-ledger candidates. It is not a project-author decision, does not
constitute human sign-off, and must not be used to satisfy the frozen
`project_author` approval requirement.

The audit was candidate-blind. It used only:

- the visible question and frozen task boundaries;
- the task components;
- the human-audited chunk-based gold records and exact evidence spans;
- the repair4 reference ledgers; and
- the final Model B group reviews.

No candidate Direct or RAG answers were inspected. The project-author fields
in `reference_candidates.jsonl` and `decision_register.csv` were not changed.

## Audit rule

The governing rule in the V2 verification and repair prompts was applied
strictly:

> Every canonical proposition and every material qualifier must be entailed
> by the cited exact evidence span.

Titles, metadata, a gold record's broader `supported_claim`, or surrounding
chunk context cannot rescue wording absent from the exact span. A factual
inference may be retained only when it is explicitly identified as an
inference and is not silently treated as direct source attribution.

## Scope

- Questions: 13
- Task components: 29
- Claim groups: 80
- Core claim groups: 52
- Supplementary claim groups: 28
- Atomic-claim dispositions: 100
- Constraint groups: 15
- Final Model B verdicts marked clean: 13/13
- Project-author decisions at the start of this audit: 13 pending

## Recommendation summary

| Question | Recommendation | Severity | Main reason |
|---|---|---:|---|
| NQ10 | Revise | Moderate | Two method/workflow attributions exceed the literal spans; one required rule is unnecessarily specific. |
| NQ12 | Revise | Major | Flattened table headers require visual verification; method/matrix attribution and cross-study causal wording exceed the spans. |
| NQ15 | Revise | Major | The buffer boundary lacks direct evidence, and two optional quantitative/order claims are absent from their exact spans. |
| NQ23 | Revise | Moderate | One required synthesis is duplicative, one comparison rule is too absolute, and one process label relies on context outside the span. |
| NQ24 | Revise | Major | The values are supported, but the compound, sorbent, and study-design attributions are not all present in the exact span. |
| NQ26 | Revise | Major | The ledger overgeneralizes all membrane processes despite separately recognizing membrane-assisted degradation. |
| WF10_002 | Defer | Critical | The question requires membrane evidence, but the gold set contains only plasma and SCWO evidence; several endpoint conclusions are also inferential. |
| WF10_021 | Revise | Major | The question includes activated carbon, but all affirmative gold is biochar; the absence statement is optional rather than required. |
| WF10_025 | Revise | Moderate | Kinetic values are supported, but surface-water and powdered-activated-carbon qualifiers are outside the exact span. |
| WF10_030 | Approve | None | Core claims and limits are directly supported and condition-specific. |
| WF10_004a | Approve | None | Trend, mechanism, contradictory evidence, and cross-study restrictions are appropriately separated and scoped. |
| WF10_004b | Revise | Major | The G07 evidence span is truncated and does not support several required material and process qualifiers. |
| WF10_036 | Approve | None | The EBCT synthesis is supported across distinct metrics and is explicitly non-universal. |

Recommended disposition before project-author sign-off:

- Approve without ledger repair: 3/13
- Revise and re-review: 9/13
- Defer until evidence is added or the task is narrowed: 1/13

## Question-level findings

### NQ10 — revise

1. `NQ10-G04` treats the foam-concentrate workflow as having no dedicated
   preconcentration step. The span describes dilution, reagent mixing, and
   HPLC injection but does not explicitly state that no extraction or
   preconcentration occurred.
2. `NQ10-G08` identifies “our method” as SPME, whereas the exact span itself
   does not name SPME. That attribution comes from surrounding context.
3. The full rule for `NQ10-G04` requires a long reagent inventory that is not
   central to answering the researcher-facing question.

Minimum repair: hedge the no-preconcentration inference, widen or replace the
G08 span so that SPME is named, and simplify the required-content rule.

### NQ12 — revise

Table-derived evidence is acceptable in principle, including
`NQ12_MMG001` and `NQ12_MMG002`, but the values and headers must remain
unambiguous.

1. `NQ12_MMG001` is a flattened multi-column table. The LOD/LOQ assignment
   should be checked visually against the source PDF before sign-off.
2. The table spans support compound-specific values, but the matrix and full
   method labels in `NQ12-G01` and `NQ12-G02` are not written in the supplied
   spans.
3. `NQ12-G04` similarly imports method and water-matrix context not present in
   its literal span.
4. `NQ12-G03` says method choice “strongly affects” sensitivity. The observed
   ranges differ, but analyte coverage and protocols also differ, so the
   comparison is descriptive and confounded rather than a causal method-only
   result.

Minimum repair: visually verify the original tables, widen the spans to carry
the required method and matrix context, and rewrite G03 as a scoped
cross-study comparison. Do not infer a universal or monotonic chain-length
law from either table.

### NQ15 — revise

1. The task boundary requires buffer choice to be evaluated as a balance
   between pH control and interference risk, but none of the supplied exact
   spans provides buffer-specific evidence.
2. `NQ15-G06` requires the order `NaClO4 > NaCl > Na2SO4`; its exact span only
   says that three electrolytes were compared.
3. `NQ15-G07` requires four removal percentages; its exact span only says that
   electrolyte components can affect removal.

Minimum repair: add or widen exact spans for the study-specific ordering and
percentages. Either add direct buffer evidence or rewrite the task boundary
so that it does not require an unsupported buffer-specific conclusion.

### NQ23 — revise

1. `NQ23-G08`, `NQ23-G09`, and `NQ23-G10` are all required under the
   comparison component. G10 repeats the non-universal synthesis already
   represented by G08/G09 and G01.
2. `NQ23-G09` says comparison is “only meaningful” when all listed parameters
   are reported. The source says the consolidated contextual table supports
   transparent evaluation, which is less absolute.
3. The process attribution in `NQ23-G02` is partly supplied by title or
   metadata rather than the exact evidence span.

Minimum repair: merge or demote G10, soften G09 to a contextual-comparison
recommendation, and include the process context in the exact span.

### NQ24 — revise

The exact span directly supports 5.71 and 6.85 mg/g, the two model names, the
particle-size difference, the background-water explanation, and the
batch/column contrast. It does not itself name PFOA or
CTAB-impregnated activated carbon. Those are material qualifiers in
`NQ24-G01` through `NQ24-G03`.

Minimum repair: widen the exact evidence span to include the compound,
sorbent, and experiment identity. The three-component decomposition can be
retained.

### NQ26 — revise

`NQ26-G04` states that membrane-based processes “as a class” do not degrade
PFAS. The same ledger also recognizes membrane-assisted degradation. This
creates an internal scope contradiction.

Minimum repair: restrict G04 to simple membrane separation or concentration
routes and explicitly exclude coupled membrane-assisted degradation systems
from that limitation.

### WF10_002 — defer

1. The question explicitly compares membrane filtration, gliding arc plasma,
   and SCWO, but the supplied gold contains no membrane experiment.
2. `WF10_002-G03` rewards saying that membrane endpoints are absent. That is a
   useful evidence limitation but does not answer the requested three-system
   comparison.
3. `WF10_002-G04` and `WF10_002-G06` infer that any single endpoint is
   insufficient and introduce destruction/mass-balance interpretation beyond
   the literal GAP span, which only lists measured endpoints.

Required action: add direct membrane endpoint evidence and direct support for
the destruction/mass-balance interpretation. Otherwise narrow the question
to the two represented systems. This question should not be approved merely
by rewarding abstention about the missing third system.

### WF10_021 — revise

The visible question asks about activated carbon or biochar, whereas all
affirmative matrix and regeneration evidence is biochar-specific. The
activated-carbon evidence gap appears only in optional `WF10_021-G04`, so a
candidate can receive full required coverage without disclosing that half of
the requested scope is unsupported.

Minimum repair: make the evidence-scope limitation required, add
activated-carbon evidence, or narrow the visible question to biochar.

### WF10_025 — revise

The exact span supports the 60-, 120-, and 240-minute equilibration statements
and the long-chain/short-chain distinction. It does not state that the matrix
is surface water or that the adsorbent is powdered activated carbon, although
both are required material qualifiers in the current ledger.

Minimum repair: widen the exact span to include matrix and adsorbent identity.
The planning inference about longer contact time for short-chain PFAS may be
retained if it remains explicitly labeled as an inference.

### WF10_030 — recommend approve

The exact spans directly support TFA persistence at the reported temperature
and residence time and the interpretation of low fluorine mass balance at the
reported lower temperatures. The ledger preserves the distinction between
measured intermediates, monitoring recommendations, and unresolved
organofluorine. Earlier metadata-only process qualifiers and duplicate
required weighting were removed.

Residual nonblocking note: ensure the optional synthesis and the
single-finding optional groups cannot produce accidental duplicate credit.

### WF10_004a — recommend approve

The ledger supports the observed long-chain/short-chain adsorption tendency,
the hydrophobic mechanism, the source-supported long-chain orientation
finding, and the existence of contradictory or context-dependent evidence.
It does not reuse the unsupported short-chain mechanism from the broader gold
record. The cross-study matching guidance is identified as synthesis rather
than a direct quotation.

Residual nonblocking note: the underlying gold record
`WF10_004a_MMG005` contains a broader `supported_claim` than its exact span,
but the ledger correctly excludes that unsupported portion.

### WF10_004b — revise

`WF10_004b-G07` relies on a truncated span ending with “but that anode
characteristics, i.” The required proposition additionally names pulsed
electrolysis, aqueous LiOH, PFOS versus GenX, and treats anode characteristics
as the controlling explanation. The supplied span does not fully entail those
qualifiers or the completed causal clause.

Minimum repair: recover a complete source span containing the method,
conditions, compared PFAS, and completed finding, or narrow G07 to the literal
negative statement that headgroup identity did not govern adsorption under
the identified study conditions.

### WF10_036 — recommend approve

The cross-study synthesis is supported by distinct reported endpoints:
capacity, a mechanism-related ratio, breakthrough/mass-transfer-zone
behavior, and carbon-use rate. The ledger correctly concludes that increasing
EBCT within the reported study ranges did not consistently improve every
performance metric and does not turn that observation into a universal rule.

Residual nonblocking note: the same evidence appears in single-study,
synthesis, limitation, and boundary groups, but those groups serve distinct
functions. The scoring implementation should continue to prevent duplicate
required-content inflation.

## Cross-cutting findings

1. **Model B clean status was necessary but not sufficient.** Several reviews
   accepted metadata or `supported_claim` fields as support even though the
   governing prompt says exact spans control attribution.
2. **Table evidence is usable.** It should not be discarded merely because it
   was extracted from a table. Visual header verification and complete
   method/matrix provenance are required.
3. **Evidence absence cannot replace task completion.** A ledger may reward a
   calibrated limitation, but a question that asks for a three-system
   comparison still needs evidence for all three systems unless the task is
   narrowed.
4. **Required coverage should reflect the visible question.** If half of a
   named scope is unsupported, acknowledging that limitation cannot remain
   merely optional.
5. **Cross-study numerical differences should be descriptive.** They should
   not be attributed causally to one method variable when analyte scope,
   matrix, instrumentation, or protocol also differs.

## Required next step

Do not freeze the repair4 candidates unchanged. Apply the minimal repairs
above, recover or widen source spans where needed, and send every changed
ledger through a new Model B verification pass. The project author can then
review the revised packet and record the final approve/revise decisions.


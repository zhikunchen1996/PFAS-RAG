# Dev13 V3 Safety and Judge Audit

Date: 2026-07-26

## Finding 1: the tag layer is too permissive

The tagger marked 95 of 130 chunks as direct evidence. It marked all ten
chunks direct for NQ15, NQ23, WF10_004a, and WF10_004b, and nine of ten direct
for NQ10, NQ26, and WF10_021. This is not a strong eligibility filter.

The useful signal appears to come more from the detail-policy annotations than
from the evidence-role labels.

## Finding 2: failed excerpts do not invalidate advisory summaries

The local validator removed 65 non-verbatim `exact_support` strings. The
answer still received each chunk's `allowed_use`, `avoid_use`, and
`omit_details` text. These fields were written by the tagger and were not
independently validated against the chunk.

Representative safe behavior exists because the full chunk remains visible
and the answer prompt says tags are not evidence. Nevertheless, this interface
permits an unverified tagger summary to influence generation. A later
candidate should either:

1. expose only schema labels plus locally validated excerpts; or
2. downgrade a direct-evidence tag when no short verbatim excerpt validates.

Shorter exact excerpts should also be requested to reduce failures caused by
PDF spacing, punctuation, and overly long quotations.

## Finding 3: the citation-blind judge cannot verify non-gold specifics

The judge repeatedly described details absent from gold as fabricated even
when they were present in the retrieved chunk cited by the answer.

Examples:

- NQ15: local anode pH, NaClO4 amendment, and `>90%` PFOA removal appear in
  C1 and C6.
- NQ23: hydrodynamic-cavitation energy ranges, plasma EE/O ranges, EO values
  of 270 and 93 kWh/m3, normalized values of 240 and 160 kWh/m3, and the
  cross-technology ranges criticized by the judge all appear in C1-C10.
- WF10_030: approximately 510 degrees C, incomplete defluorination of 62.6%,
  gas-analysis limitations, and trifluoromethane formation appear in C1-C6.
- WF10_004b: the AER adsorption ranges and log Kex/headgroup patterns appear
  in C1-C2.

The citation-blind prompt correctly states that gold need not be exhaustive,
but it gives the judge no source context with which to distinguish valid
retrieved specificity from fabrication. This affects both RAG systems and is
especially important in the exploratory RAG-versus-Direct comparison.

## Finding 4: some answer-level overreach remains real

The source audit does not make every tagged answer safe. Several answers
synthesize many source-specific examples into broad patterns. For example,
WF10_004b moves from medium-specific headgroup observations toward a general
sulfonate-over-carboxylate pattern, while the evidence itself is
system-dependent. NQ23 is technically sourced but much longer and more
numerically dense than needed for the research question.

The next answer prompt should make the use of a valid detail conditional on
its decision value for the visible question, not merely on source support.

## Direct prompt assessment

The matched Direct prompt does not need more scientific content or access.
It is structurally comparable and correctly excludes retrieval privileges.
However, it produced substantially longer answers than either RAG system.
Before using it in a final RAG-versus-Direct experiment, apply the same
explicit response budget to both systems.

The current citation-blind Direct result must not be interpreted as proof that
Direct is scientifically superior. A final comparison needs two separate
views:

- citation-blind content utility under a common response budget;
- source-aware support/entailment for RAG claims, reported separately rather
  than applied to Direct.

## Module-ablation decision

The predeclared direction condition passed, but the module-ablation stability
condition did not. This means the run does not independently confirm the
soft-tag layer as an isolated improvement. It does not determine whether the
complete V3 system can be frozen under its final system-level comparison.
Test40 was not run.

## Follow-up source-verified diagnostic

A later three-repeat diagnostic retained answer citations and supplied the
common retrieved chunks to the judge for scientific-correctness verification.
Citation behavior itself remained unscored. The table below compares matched
repeat 1 to isolate the protocol change.

Compared with citation-blind repeat 1:

| Comparison | Citation-blind | Source-verified |
|---|---:|---:|
| tagged vs matched untagged mean | 0.5856 | 0.5952 |
| tagged vs matched untagged W/L/T | 5/1/7 | 9/2/2 |
| tagged vs Direct mean | 0.3596 | 0.8990 |
| tagged vs Direct W/L/T | 3/10/0 | 12/1/0 |

The small matched-repeat mean change for tagged versus untagged indicates that
merely retaining citations did not automatically favor the tagged system when
both answers shared the same source access. Across all three source-verified
repeats, tagged versus untagged was 9/3/1 with mean 0.5631 and mirror agreement
0.6410. Tagged versus Direct was 13/0/0 with mean 0.9131 and mirror agreement
0.8846.

The Direct reversal shows that the citation-blind judge had treated valid but
non-gold source-specific details as unverifiable. It also shows that the two
protocols answer different questions: the source-verified version measures
literature-grounded answer utility, whereas the citation-blind version rewards
content that can be validated from gold or general knowledge alone.

The tagged-versus-untagged row remains an internal diagnostic because its
mirror agreement did not reach 0.70. The tagged-versus-Direct row is the
canonical system-level confirmation under the final protocol.

# Dev13 Soft-Tag V3 Confirmation

Date: 2026-07-26

Status: `completed_internal_development_diagnostic`

## Scope

This run evaluates a topic-general soft-tag layer on all 13 development
questions. Test40 was not inspected or run.

All three generated systems used GPT-5.1 at temperature 0:

- tagged RAG: BGE-LLM `60 -> 30 -> 10`, full chunks, plus soft tags;
- matched untagged RAG: the same final chunks, order, and answer prompt without
  soft tags;
- matched Direct: no retrieval, corpus, gold, web, or citations.

The primary module ablation is tagged RAG versus matched untagged RAG. The
Direct comparison is exploratory and does not select the tag module.

## Primary result

| Comparison | Tagged wins | Opponent wins | Ties | Mean tagged score | Tagged advantage | Mirrored criterion agreement |
|---|---:|---:|---:|---:|---:|---:|
| tagged vs matched untagged | 9 | 3 | 1 | 0.5865 | +0.0865 | 0.5321 |
| tagged vs matched Direct | 5 | 8 | 0 | 0.3987 | -0.1013 | 0.6603 |

The tag ablation passed the predeclared directional condition but failed the
predeclared mirrored-agreement target of 0.70. It therefore does not establish
the soft-tag layer as an independently confirmed module improvement.

## Repeat-level stability

| Repeat | Comparison | Mean tagged score | W/L/T | Mirror agreement |
|---:|---|---:|---:|---:|
| 1 | tagged vs matched untagged | 0.5856 | 5/1/7 | 0.5769 |
| 2 | tagged vs matched untagged | 0.6019 | 8/1/4 | 0.5385 |
| 3 | tagged vs matched untagged | 0.5721 | 7/2/4 | 0.4808 |
| 1 | tagged vs matched Direct | 0.3596 | 3/10/0 | 0.7115 |
| 2 | tagged vs matched Direct | 0.4135 | 4/8/1 | 0.7308 |
| 3 | tagged vs matched Direct | 0.4231 | 5/7/1 | 0.5385 |

The directional tagged-versus-untagged advantage recurred in all three
repeats, but many question-level preferences were near ties and order
sensitivity remained material.

## Tagger diagnostics

- 130 final chunks were tagged.
- 95 were labeled `direct_evidence`.
- 20 were labeled `background`.
- 13 were labeled `nearby_but_mismatched`.
- 2 were labeled `irrelevant`.
- 65 proposed `exact_support` strings failed verbatim validation and were
  removed.
- The failures were all `non_verbatim_exact_support`; component IDs, labels,
  and polarity values passed schema validation.

The direct-evidence rate of 73.1% is too permissive for a layer intended to
improve evidence selectivity. In addition, unvalidated `allowed_use`,
`avoid_use`, and `omit_details` summaries remained visible after a failed
exact-support check. Those summaries are explicitly advisory, but their
presence creates an avoidable unverified text channel.

## Length diagnostic

Approximate answer word counts:

| System | Mean | Minimum | Maximum |
|---|---:|---:|---:|
| tagged RAG | 825.5 | 349 | 1,743 |
| matched untagged RAG | 816.5 | 352 | 1,610 |
| matched Direct | 982.2 | 595 | 1,835 |

The matched Direct prompt shared task logic and output structure, but its
answers were about 19% longer on average. Future RAG-versus-Direct comparisons
should use a common explicit response budget or evaluate length-normalized
utility.

## Cost

| Stage | Calls | Input tokens | Output tokens | Total tokens | Estimated USD |
|---|---:|---:|---:|---:|---:|
| Tagging and all answer generation | 52 | 239,358 | 96,631 | 335,989 | 1.2655 |
| Three-repeat mirrored judging | 156 | 757,437 | 121,429 | 878,866 | 2.1611 |
| Total | 208 | 996,795 | 218,060 | 1,214,855 | 3.4266 |

Costs use the recorded GPT-5.1 price basis of USD 1.25 per million input
tokens and USD 10.00 per million output tokens.

## Decision

Preserve this run as a judge-sensitivity and tag-ablation diagnostic. The
matched untagged comparison may be reported only with its low mirrored
agreement and does not independently establish tag efficacy. The Direct result
is one endpoint in the documented judge-sensitivity analysis; the Revision 3
neutral-evidence comparison is canonical.

The tagger prompt hash recorded in this historical generation manifest does
not match the current `soft_eligibility_tagger_v3.txt`, and the exact historical
prompt text was not retained. This run is therefore not prompt-reproducible and
must not be used as a canonical execution artifact.

The historical numerical outputs are in `results/summary.csv` and
`results/per_question.csv`. The source audit is in `AUDIT.md`.

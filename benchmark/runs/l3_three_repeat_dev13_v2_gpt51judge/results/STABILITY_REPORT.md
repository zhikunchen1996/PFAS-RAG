# Dev13 GPT-5.1 L3 Stability Report

## Scope

This Dev13-only package rejudged the existing six matched Direct and
BGE-LLM RAG answer systems. It used the frozen L3 V3 canonical claim ledger
and the frozen L3 judge prompt. Each answer received three new, independent,
one-answer GPT-5.1 judgments. No Test40 answer, retrieved context, system
outcome, or test metric was used.

## Integrity checks

- 234/234 expected judgments were valid: 13 questions x 6 systems x 3 repeats.
- Every valid response reported `gpt-5.1-2025-11-13` for a request to `gpt-5.1`.
- Every call used reasoning effort `low`, provider-default temperature, and
  canonical claim order.
- Each answer has three distinct response IDs.
- One Repeat 3 response had an invalid claim-status label and was not retained.
  The single unfinished item was reissued once; the final analytical data have
  exactly one valid new judgment for that item in that repeat.
- The completed analytical calls totaled 2,295,434 reported tokens and
  USD 6.82732775. These are the valid-call totals and exclude the unrecorded
  token usage of the one schema-invalid response.

## Primary metric stability

The primary metric is component-balanced core reference-claim coverage. The
reported system value is the equal mean of the three repeat-specific Dev13
means; the accompanying variability is the sample SD across those three
means, not a confidence interval.

| System | Mean primary score | Repeat SD |
| --- | ---: | ---: |
| GPT-5.1 Direct | 0.2603 | 0.0279 |
| GPT-5.1 BGE-LLM RAG | 0.4829 | 0.0213 |
| Gemini 3.1 Direct | 0.1688 | 0.0067 |
| Gemini 3.1 BGE-LLM RAG | 0.3159 | 0.0259 |
| Claude Sonnet 5 Direct | 0.2169 | 0.0182 |
| Claude Sonnet 5 BGE-LLM RAG | 0.4145 | 0.0195 |

The matched RAG-minus-Direct primary effect was positive in all three repeats
for every base model:

| Base model | Mean effect | Repeat SD | Repeat range |
| --- | ---: | ---: | ---: |
| GPT-5.1 | 0.2226 | 0.0486 | 0.1827 to 0.2767 |
| Gemini 3.1 | 0.1471 | 0.0239 | 0.1197 to 0.1635 |
| Claude Sonnet 5 | 0.1976 | 0.0343 | 0.1677 to 0.2350 |

Across all 474 evaluated claim instances, 394 had identical full/partial/
absent/contradicted status in all three calls (83.1%). This supports use of
the frozen three-repeat mean as the Dev13 L3 aggregation policy, while still
requiring repeat-level SD disclosure.

## Interpretation boundary

This is a judge-stability and Dev13 development analysis. It does not make a
held-out Test40 performance claim, and the Dev13 effect sizes must not be
treated as the final benchmark result. Test40 reference-ledger construction
may proceed only through the documented candidate-blind workflow and only if
the independent methods review finds no blocking defect.

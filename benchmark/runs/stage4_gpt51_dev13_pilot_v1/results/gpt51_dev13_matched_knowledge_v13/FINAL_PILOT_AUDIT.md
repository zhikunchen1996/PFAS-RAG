# GPT-5.1 Dev13 matched pilot audit

## Canonical scope

The canonical generation is V1.3 and the canonical answer-quality evaluation
is L2 V4. Both were developed and calibrated only on Dev13. Test40 was not
used.

Direct and RAG use the same GPT-5.1 snapshot, reasoning effort, output-token
budget, shared scientific instructions, general-knowledge permission, response
structure, and question order. Neither prompt contains a word-count limit. The
RAG arm alone receives the frozen BGE-LLM top-10 chunks, common soft tags, and
atomic-citation instructions.

## Structural checks

- Direct generation: 13/13, no empty or excluded answer
- RAG generation: 13/13, no empty or excluded answer
- Returned snapshot: `gpt-5.1-2025-11-13`
- Finish reason: `stop` for all 26 generation calls
- Frozen retrieval and tagger calls repeated during generation: 0
- L2 V4 payloads: 26, exactly two mirrored orientations per question
- Citation markers reaching L2: 0
- System-identity findings reaching L2: 0
- L2 judge calls: 26/26, no schema repair or silent exclusion

## Final L2 V4 result

| Criterion | Direct | RAG | Tie | Direct ability | RAG ability |
|---|---:|---:|---:|---:|---:|
| Scientific correctness | 4 | 6 | 16 | 0.400 | 0.600 |
| Question fulfillment | 8 | 8 | 10 | 0.500 | 0.500 |
| Scope and calibration | 6 | 1 | 19 | 0.857 | 0.143 |
| Practical usefulness | 12 | 8 | 6 | 0.600 | 0.400 |

The equal-weight composite is descriptive only: Direct 0.589 and RAG 0.411.
Its 95% intervals overlap. Criterion-specific intervals are also broad, so the
pilot does not support a general claim that either arm is superior.

## Manual disagreement and tie audit

All question-criterion mirrored outcomes are retained in
`final_report/per_question_l2_votes.csv`.

- RAG showed consistent evidence-use advantages for reported analytical
  performance (`NQ12`), energy evidence (`NQ23`), protocol extraction
  (`WF10_025`), and limitation evidence (`WF10_036`).
- Direct showed consistent breadth or decision-framework advantages for
  preconcentration (`NQ10`), buffer selection (`NQ15`), endpoint distinctions
  (`WF10_002`), and one cross-study comparison (`WF10_004a`).
- `WF10_004b` and `NQ24` contained true A/B reversals on at least one
  criterion. These votes remain in the Davidson fit; they were not resolved,
  excluded, or selectively repeated.
- Most scientific-correctness and scope judgments were ties. This reflects
  non-exhaustive gold and overlap in scientifically plausible content, not
  missing output.
- Practical usefulness had the lowest mirrored agreement (7/13). It should be
  interpreted with its uncertainty interval and raw votes, not as a hard
  per-question winner.
- No conflict was attributable to truncation, malformed abstention, citation
  stripping, system-identity leakage, missing context, or unequal question
  membership.

## Judge calibration audit

V2 incorrectly inferred that some RAG details were invented because they were
outside non-exhaustive gold. V3 strengthened the neutral-outside-gold rule but
left one source-verification-dependent task boundary. V4 supplies explicit
citation-blind boundaries that retain scientifically evaluable constraints and
remove only clauses requiring unseen source access.

In V4, references to outside-gold content were descriptive and neutral. No
criterion rationale penalized an answer solely because a detail was absent from
gold. Claude Sonnet independently reviewed the V4 design and returned
`APPROVE_RERUN`.

## Interpretation

The pilot validates the matched generation pipeline, anonymous mirrored judge,
Davidson aggregation, uncertainty reporting, and cost accounting. It also
shows why retrieval value should be reported by criterion: retrieved evidence
can improve correctness and evidence-specific fulfillment while a strong
closed-book model may remain broader or more practically organized.

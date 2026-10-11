# Frozen V3 Revision 2 Historical Freeze Audit

> Superseded for evaluation by Frozen V3 Revision 3. This record is retained
> as historical provenance. Its 13:0 result used system-identifying payload
> metadata and RAG-owned verification context and is not the canonical result.
> The canonical Revision 3 audit and 10:3 result are recorded in
> `freeze_audit_revision3_2026-07-26.md`.

Date: 2026-07-26

Decision: `FREEZE AFTER REVISION-2 HASH VERIFICATION`

## Scope

The audit covered every Frozen V3 script, prompt, method record, question and
gold file, selected retrieval result, Dev13 generation output, judge payload,
result path, model identifier, temperature, token record, and manifest rule.
Test40 was not executed or inspected through a V3 result.

## Blocking issue corrected

Revision 1 generated its canonical answers from a pre-freeze GPT-5.1 selector
run that used a compact selector prompt. The retrieval-budget sweep used the
expanded prompt stored at
`prompts/retrieval/bge_llm_selector_v3.txt`. Although both runs used
`10/30/60`, their final top-ten contexts differed for all 13 questions.
Consequently, Revision 1 answer results and the budget table did not represent
the same retrieval system.

Revision 2 uses the exact `10/30/60` retrieval output from the budget sweep:

`results/dev13_retrieval_budget_gpt51_2026-07-26/bge_llm_gpt51/retrieval_outputs/rag_outputs_bge_llm_gpt51_pool60_bge30_llm10_fullchunk.jsonl`

The validator now checks that all 13 selector calls contain the byte-identical
frozen selector prompt. Revision 1 outputs remain historical and are excluded
from the selected-result hash boundary.

## Runtime and path corrections

- Generation, judging, retrieval metrics, and runtime helpers are V3-local.
- No canonical runtime import reads Frozen V2, `benchmark/reports`,
  `benchmark/src`, or `src/rag_app`.
- Project-relative CLI inputs resolve against the repository root, including
  when the budget runner is launched from another working directory.
- Fresh execution is the default. `--resume` reuses a row only when the model,
  temperature, prompt, and input payload fingerprint match.
- Template insertion is single-pass; braces inside questions or chunks cannot
  trigger a second template substitution.
- Question IDs, split membership, context identities, gold counts, selector
  response schema, answer sections, and scored judge fields are validated
  strictly.

## Prompt and information-boundary checks

The selector, tagger, and answer model receive no gold, expected answer, or
hidden benchmark rubric. The tagger sees only the visible question and the
same ten full chunks later supplied to the answer model.

The answer-visible tag interface contains only:

- categorical evidence role;
- categorical detail policy;
- categorical evidence polarity;
- confidence;
- a locally validated source excerpt.

Question-component prose and component assignments are audit-only.
`allowed_use`, `avoid_use`, and `omit_details` are neither requested nor
retained. A non-verbatim `exact_support` string is cleared before formatting,
while the full chunk remains available. In the Revision 2 run, 91 of 130
excerpts passed local substring verification and 37 were cleared. No
unverified tagger prose reached an answer prompt.

The RAG and Direct prompts use the same task-operation framing, scientific
compatibility dimensions, response-length policy, and four-section output.
Direct receives no retrieved context and is instructed not to invent
study-specific details. RAG receives the fixed context and must use atomic
source markers. The judge does not reward or penalize citation presence,
format, count, density, or coverage; markers are retained only as optional
locators for scientific-correctness verification.

## Canonical Dev13 result

Revision 2 regenerated all tags, RAG answers, and prompt-matched Direct answers
with GPT-5.1 at temperature 0. The source-verified judge then ran three repeats
with both answer orientations.

- V3 wins: 13
- Direct wins: 0
- Ties: 0
- Mean weighted V3 score: 0.9217948718
- Mirrored criterion agreement: 0.7884615385

The conclusion is unchanged from Revision 1, but only Revision 2 is aligned
with the retrieval-budget selector prompt. Generation used 213,856 tokens
(estimated USD 0.7564). Judging used 783,876 tokens (estimated USD 1.4811).

GPT-5.1 omitted all three non-scoring auxiliary fields (`confidence`,
`material_errors_A`, and `material_errors_B`) in 21 of 78 judge responses.
The 63 field-level omissions are recorded and normalized. No scored criterion
preference or rationale was missing, and these auxiliary fields never enter
the weighting or winner calculation.

## Verification gates

Passing offline checks include:

- 53 unique questions partitioned into disjoint Dev13 and Test40 sets;
- 249 unique project-author-reviewed chunk-based gold records, at least one per
  question; this provenance wording was formalized in Revision 3;
- per-question gold counts reproduced from JSONL;
- 39 BGE-LLM question-configuration retrieval metrics reproduced;
- 13 fixed retrieval rows with ten unique, non-empty chunks each;
- generation and judge execution fingerprints reproduced;
- all three judge runs contain 26 aligned payload, mapping, and result rows;
- canonical summary recomputed from the 13 per-question rows;
- eight Frozen V3 unit tests and seven repository regression tests passed;
- task-general prompt and synthetic leakage checks passed.

## Remaining repository-state condition

The V3 directory was untracked at the time of this audit. The SHA-256 manifest
defines the local artifact boundary, but a repository commit cannot be claimed
as the V3 freeze until these files are added and committed. The manifest
records the tracked/untracked count explicitly.

## Freeze boundary

Frozen V3 Revision 2 is approved as a Dev13-confirmed system definition once
`freeze_manifest.json --verify` passes. Test40 remains unrun for V3. Any later
Test40 execution must use the frozen questions, gold, prompts, code, selected
retrieval configuration, model settings, and hashes without test-driven
changes.

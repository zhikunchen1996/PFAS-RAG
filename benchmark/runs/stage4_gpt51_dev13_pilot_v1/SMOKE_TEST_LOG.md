# Stage 4 smoke-test log

## Attempt 1

- Scope: first Dev13 question, Direct arm first.
- API behavior: the GPT-5.1 call returned before a local persistence error.
- Local failure: the parallel writer's key callback handled the nested input
  item but not the flat output row, producing `KeyError: question`.
- Scientific impact: none; no result entered the pilot.
- Frozen-method impact: none; prompts, model settings, retrieval, tags, and
  judge code were unchanged.
- Accounting limitation: the returned usage object was lost before it could be
  persisted, so this one smoke call is excluded from formal pilot accounting
  and disclosed as an unquantified pre-pilot operational call.
- Resolution: use one key function that accepts both input and output schemas,
  then repeat the smoke test in a fresh temporary directory.

## Attempt 2

- Scope: first Dev13 question, both Direct and RAG arms.
- API behavior: both calls returned `gpt-5.1-2025-11-13` with
  `finish_reason=stop`.
- Local behavior: persistence, usage accounting, and run-manifest generation
  succeeded.
- Prompt finding: Direct produced approximately 1,208 words and RAG produced
  approximately 846 words. Direct also expanded into an unnecessary catalog of
  matrices and methods.
- Risk: unequal or excessive verbosity could bias the citation-blind quality
  judge and raise cost without improving question fulfillment.
- Resolution: apply one shared, arm-neutral limit of 250-550 preferred words
  and 700 absolute maximum, with explicit instructions against exhaustive
  catalogs. Repeat one final smoke test before formal generation.

## Attempt 3

- Scope: first Dev13 question, both Direct and RAG arms after adding the shared
  length policy.
- API behavior: both calls returned the required snapshot and stopped
  normally.
- Result: RAG was approximately 617 words and passed; Direct remained
  approximately 1,010 words and failed the declared maximum.
- Resolution: repeat the identical hard 700-word instruction at the end of
  both arm-specific user messages, where instruction salience is higher. Add a
  smoke-only single-arm runner option and retest Direct only.

## Attempt 4

- Scope: first Dev13 question, Direct arm only.
- API behavior: returned `gpt-5.1-2025-11-13` with `finish_reason=stop`.
- Result: approximately 693 words, within the hard 700-word limit.
- Decision: freeze the current prompts and begin the formal 13-question pilot
  in a fresh result directory. Smoke outputs remain temporary and are not
  included in formal performance or cost estimates.

## Complete generation attempt 1

- Scope: 13 Direct and 13 RAG answers.
- Coverage and API validity: 26/26 answers, required snapshot, normal finish,
  unique IDs, and matched question order.
- Cost: USD 0.1539 for Direct and USD 0.2690 for RAG generation.
- Length-gate result: Direct NQ10/NQ12/NQ15 and RAG NQ26 exceeded 700 words.
- Decision: no L2 judgment was run. The complete run is retained as a failed
  prompt-development attempt. V1.1 applies the same stronger 550-word
  instruction to both arms and reruns all 26 answers, rather than selectively
  retrying only failures.

## V1.2 length-policy decision

- Timing: made before any L2 answer-quality judgment.
- Decision: remove all word-count limits from both matched generation prompts.
- Validation: answer length is recorded descriptively but cannot determine
  inclusion, exclusion, or retry.
- Data handling: the superseded 26-answer run remains immutable development
  history. Direct and RAG are rerun completely under V1.2; no selective retry
  is permitted.

## V1.2 matched-knowledge audit

- Scope: complete 13-question Direct-versus-RAG generation and frozen L2 V2
  judgment, performed only on Dev13.
- Structural validity: 26/26 answers and 26/26 mirrored judge calls passed.
- Diagnostic result: Direct received higher L2 ability on all four criteria.
- Root cause: the Direct arm prompt explicitly permitted reliable general
  scientific knowledge, while the RAG arm prompt emphasized supplied evidence
  without the same explicit permission. Judge rationales repeatedly favored
  Direct for broader domain coverage while describing RAG as narrower.
- Decision: classify V1.2 as a development diagnostic, not a performance
  result. Move the general-knowledge instruction into the shared system prompt,
  preserve the no-length-limit policy, and rerun both arms completely as V1.3.

## V1.3 non-exhaustive-gold judge audit

- Generation validity: V1.3 fully matched general-knowledge permission and
  retained the no-length-limit policy.
- Judge finding: L2 V2 rationales sometimes called a RAG detail invented or
  unsupported solely because it was absent from the explicitly non-exhaustive
  gold evidence.
- Impact: because the citation-blind judge does not receive retrieved chunks,
  it cannot infer fabrication from gold absence. Doing so systematically
  penalizes evidence-rich answers.
- Resolution: retain the V1.3 answers and all statistical settings. L2 V3
  strengthens the existing neutral-outside-gold rule and is recalibrated only
  on Dev13.

## L2 V3 evaluable-boundary audit

- Improvement: V3 reduced the previous extreme Direct advantage and treated
  most outside-gold detail as neutral.
- Residual failure: one `WF10_030` orientation still used a source-verification
  clause in the task boundaries to penalize details solely because they were
  absent from gold.
- Resolution: L2 V4 uses an explicit Dev13 citation-blind boundary table.
  It removes only constraints that require unseen source access to enforce,
  while retaining endpoint distinctions, condition dependence, scope control,
  and prohibitions on universal claims.

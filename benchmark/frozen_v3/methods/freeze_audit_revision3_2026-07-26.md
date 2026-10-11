# Frozen V3 Revision 3 Freeze Audit

Date: 2026-07-26

Decision: `FREEZE AFTER CLEAN-COMMIT MANIFEST VERIFICATION`

## Scope

Revision 3 retains the selector-aligned Revision 2 generation artifact and
repairs the evaluation, provenance, output-safety, and metric-accounting
issues identified by an independent Claude Opus audit. Frozen V3 remains a
Dev13-confirmed system definition. Test40 has not been run for V3.

## Evaluation correction

The prior source-verified judge exposed local comparison metadata and verified
both answers against only the canonical RAG arm's retrieved chunks. It
therefore favored the RAG arm by construction and produced a 13:0 result that
is now retained only as a judge-sensitivity analysis.

The Revision 3 judge:

- removes question IDs, system identities, hidden task labels, and citation
  markers from the model-visible payload;
- supplies both answer arms with the same deduplicated union of Hybrid, BGE,
  and BGE-LLM top-10 chunks;
- describes gold as non-exhaustive and does not treat absence from gold as
  evidence that a claim is false;
- scores scientific correctness, question fulfillment, uncertainty and
  limitations, and practical usefulness;
- does not score citation presence, formatting, count, or coverage;
- uses three temperature-zero resamples and mirrored answer order.

The canonical Dev13 result is:

- V3 wins: 10
- Direct wins: 3
- Ties: 0
- Mean weighted V3 score: 0.7846153846
- Mirrored criterion agreement: 0.7692307692

The historical citation-blind and RAG-owned-context results are preserved to
show judge sensitivity: 5:8 and 13:0, respectively.

The common union contains 20.8 chunks per question on average. All ten
canonical RAG chunks are included by construction, and about 3.9 chunks per
question are unique to that retriever. Direct therefore remains a
no-retrieval baseline rather than an information-matched generation arm.
Seventeen of 78 judge responses required normalization of non-scoring
auxiliary fields; all scored fields were complete. Mirrored criterion
agreement of 0.7692 is reported as an uncertainty diagnostic.

## Information-boundary corrections

The BGE-LLM selector accepts only the visible question and candidate chunks.
The former `rubric_augmented` input branch was removed. Soft-tag free-text
advice is not passed to the answer model. A tag's `exact_support` excerpt is
retained only when it is a normalized substring of the source chunk; invalid
excerpts are removed and logged. All ten complete chunks remain available to
the answer model.

## Gold provenance

The retained benchmark contains 53 questions and 249 chunk-based gold records
after a project-author blanket retention confirmation. No item-specific
rationale was recorded. Gold is explicitly non-exhaustive and was not
independently adjudicated by a second annotator. Historical machine-review
fields remain unchanged, including unresolved flags. Separate review
registers and their source hashes provide the current provenance record.

## Metric and runtime corrections

- Required-gold recall, gold-document recall, and MRR are macro-averaged over
  the 12 Dev13 questions with required gold.
- Negative-gold retrieval is reported separately for the six applicable Dev
  questions.
- Hybrid and BGE metric rows, as well as BGE-LLM rows, are recomputed by the
  self-contained validator.
- Canonical runners refuse non-empty output directories unless `--resume` is
  explicitly supplied.
- Resume reuse requires matching model, temperature, prompt, and model-visible
  payload fingerprints.
- Frozen V3 runtime imports are checked to remain inside the V3 package.

## Freeze condition

Every selected V3 file must be committed before the manifest is built. The
manifest is generated from that clean content commit, excludes itself from its
hash set, and is committed as a separate release step. A passing manifest
verification, local regression suite, prompt-boundary validator, and
self-contained package validator are required before the revision is called
frozen.

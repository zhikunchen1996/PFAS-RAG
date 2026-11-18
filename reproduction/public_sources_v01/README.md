# Public Source Data

This release provides source locators instead of redistributing literature
passages. It preserves the experimental design, scores and result tables.

- `citation_error_audit.csv`: 44 claim-citation records covering 23 unsupported
  or contradicted claims. The original-text column is replaced by source DOI,
  title, PDF page location and corpus chunk ID. Page numbers count from the
  first page of the source PDF, not from the journal's printed page numbers.
- `source_text_index.jsonl`: SHA-256 identifiers, original character counts
  and available source metadata for omitted text values.
- `projection_manifest.json`: original and public file hashes and the scope
  of the transformation.

Dedicated source-text fields contain `[SOURCE_TEXT_OMITTED sha256=...]` markers.
Embedded verbatim passages matching at least 18 consecutive word tokens from
the corpus or recorded evidence were also omitted from stored outputs and
audit notes. This matching threshold is a reproducible cleanup rule, not a
copyright-permission threshold. Bibliographic identifiers and benchmark
questions remain intact. Short phrases can still appear in generated prose.

The files at historical `frozen` paths are public projections where indicated
in the projection manifest. Original freeze hashes remain as provenance and
are not claims that the projected files are byte-identical to the originals.
Prompts, executable experimental code and numeric scoring fields are unchanged.
Use the release verifier for this tree, not complete-private-workspace checks.

Retrieval metrics, answer-score summaries, expert aggregates and supplementary
statistics can be recomputed using the documented commands. New source-dependent
generation, support judging or exact-span verification requires the original
evidence. Restore it from lawfully obtained sources in a separate working copy;
do not send omission markers to a model as if they were evidence.

This update changes only the current public tree. Earlier Git commits remain
accessible and may contain the former evidence text.

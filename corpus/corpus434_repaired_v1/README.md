# Corpus434 Repaired V1

This package records the 2026-07-14 repair of the PFAS literature corpus used by
the local RAG system. The historical collection remains available for exact
reproduction of archived Frozen249 outputs; the active Frozen V3 benchmark and
all subsequent corrected runs use the repaired collection.

## Version

- Source manifest: 435 records.
- Repaired manifest: 434 unique records.
- Source collection: `rag_documents_bge_large_en_v1_5_sent256_overlap2`.
- Repaired collection: `rag_documents_bge_large_en_v1_5_sent256_overlap2_corpus434_repaired_v1`.
- Source chunks: 29,895.
- Repaired chunks: 29,805.
- Removed duplicate chunks: 90.

The repaired collection reuses the original BGE embeddings for all retained
chunks. Retained Chroma IDs, chunk text, chunk numbers, and source identifiers
are unchanged.

## Repairs

One duplicate PDF was removed. The duplicate and retained copies shared DOI
`10.1039/d4ew00600c`; 69 of their 90 normalized chunks were exact matches.

Thirteen metadata records were corrected by comparing the manifest DOI with the
DOI printed in the indexed article front matter and resolving the corrected DOI
through Crossref. Eleven were incorrect article matches and two aligned a
German-edition DOI with the International Edition represented by the indexed
English article. Corrected fields include DOI, canonical title, journal,
publication year/date, authors, volume, issue, pages, publisher, and citations.

## Validation

- Remaining duplicate DOI groups: 0.
- Remaining near-duplicate document pairs: 0 under the audit rule of at least
  five exact normalized chunks and chunk-set Jaccard similarity of at least 0.15.
- Front-matter DOI comparisons completed: 432 records with detectable DOI, 0
  mismatches after repair.
- Frozen V3 gold chunk resolutions: 249/249.
- Frozen V3 exact evidence-span resolutions: 249/249.
- Retained Chroma IDs changed: 0.
- Text-query retrieval smoke test: passed.

The repair does not alter the frozen questions or pseudo-gold evidence. Because
removing a duplicate can change candidate rankings, archived retrieval and
answer scores have not been relabeled as repaired-corpus results. Dev13 and
test40 retrieval were rerun on 2026-07-14. The deterministic Hybrid and
historical capped-BGE top10 contexts retained mean old/new overlap of at least
9.9 chunks on test40, with only small retrieval-metric changes. The complete
comparison is stored in
`benchmark/archive/frozen249/results/corpus434_repaired_v1_retrieval_2026-07-14`.

## Files

- `corrections.json`: explicit removal and metadata-correction rules.
- `raw_manifest_original.csv`: pre-repair manifest.
- `raw_manifest.csv`: repaired manifest.
- `repair_report.json`: machine-readable counts, hashes, and before/after DOI log.
- `scripts/build_repaired_corpus.py`: reproducible builder for the repaired
  manifest and Chroma collection.

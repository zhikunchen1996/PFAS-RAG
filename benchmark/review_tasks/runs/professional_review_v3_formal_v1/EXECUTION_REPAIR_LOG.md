# Formal execution repair log

## 2026-08-04: RT03 document-selector overlap

- Stage: `document_selection`
- Call key: `RT03:bge_llm_local_rag:document_selector`
- Request hash: `e68e926230e0bbdbd08c0e609b97c10ca02786cf4639c19854c8399802e8a491`
- Problem: the structured response placed `D12`, `D13`, and `D14` in both
  `selected_source_ids` and `excluded_sources`, so the strict execution
  validator stopped before constructing the source packet.
- Deterministic repair: the three duplicate entries were removed from
  `result.excluded_sources`. The ordered selected set, component-coverage
  mapping, candidate ranking, prompts, and raw API response were unchanged.
- Rationale: `selected_source_ids` is the authoritative retained set and all
  three identifiers were explicit members of it; `D12` and `D13` were also
  used in the returned component-coverage mapping. The repaired selected and
  excluded sets are disjoint and together classify all 20 candidates.
- Repaired file SHA-256:
  `b2be8666e54d0ecf2334ba5a6fd7391c5d090a3e626b316a5aac518a580ad7b6`
- Cost effect: no API call was repeated.

This is an execution-data consistency repair, not a change to the frozen
retrieval method or source ranking. The original response remains verbatim in
the file's `raw_response_text` field.

## 2026-08-04: RT08 document-selector overlap

- Stage: `document_selection`
- Call key: `RT08:bge_llm_local_rag:document_selector`
- Request hash: `f78b6b3b35de3a021145ac6d77eefd9fe06eed671eef6f0edaa050bb81ca3822`
- Problem: `D11` appeared in both the ordered selected set and the excluded
  set. It also appeared in the returned coverage mappings for `RT08-C1` and
  `RT08-C2`.
- Deterministic repair: `D11` was removed only from
  `result.excluded_sources`. The selected set, component mappings, ranking,
  prompts, and raw response were unchanged.
- Source check: `D11` is the 2022 primary experimental Chemosphere study by
  Saleem et al. on radial-plasma PFAS degradation (DOI
  `10.1016/j.chemosphere.2022.135800`), not the defining review excluded for
  RT08. The exclusion reason returned by the model was therefore inconsistent
  with both the selected set and candidate metadata.
- Repaired file SHA-256:
  superseded below after completing the same response's missing-source repair.
- Cost effect: no API call was repeated.

The next validator check showed that the same response omitted `D20` from
both output sets. `D20` is a primary hydrothermal alkaline treatment study,
whereas RT08 is restricted to electrochemical oxidation, non-thermal plasma,
and sonolysis. The response's own selection rationale classified HALT as a
non-target technology. `D20` was therefore added to `excluded_sources` with
the existing `task_irrelevant` category. This classifies all 20 screened
candidates without changing the six selected sources. The final repaired file
SHA-256 is
`7b099bb7144327ed095c2b7877b887a585356113d2948e0efe7015f34ed9f017`.

## 2026-08-04: RT04 Web Search URL normalization

- Stage: `web_source_discovery`
- Problem: the result packet recorded the inspected Nature source as
  `https://www.nature.com/articles/s41545-022-00193-y.pdf`, while the API's
  consulted-source metadata recorded the canonical URL without `.pdf`.
  Exact URL matching therefore dropped a genuinely consulted sixth source and
  stopped the run at the six-source minimum.
- Deterministic repair: only `result.sources[].inspected_url` for DOI
  `10.1038/s41545-022-00193-y` was normalized to the exact canonical URL in
  `consulted_sources`. Title, DOI, evidence passages, source count, and raw
  response were unchanged.
- Cost effect: no Web Search call was repeated.

## 2026-08-04: RT07 Web synthesis citation-ID retry

- Problem: the first completed RT07 Web review used inconsistent `S##`
  aliases rather than the packet's exact `WEB##` source IDs. The independent
  run validator rejected the answer before results were frozen.
- Resolution: the first synthesis, source-support judgment, and review-quality
  judgment were moved intact to
  `superseded/RT07_web_citation_id_retry1/`. RT07 synthesis was regenerated
  from the unchanged verified records and unchanged frozen prompt, followed by
  replacement source-support and quality judgments. The final complete run
  passed `validate_review_run.py`.
- Superseded-call cost: USD 0.33884525. It is excluded from canonical system
  summaries but included in the estimated billed-execution total.
- Scientific effect: no retrieval, extraction, verification, task, or source
  packet was changed. Only the invalid synthesis chain was replaced.

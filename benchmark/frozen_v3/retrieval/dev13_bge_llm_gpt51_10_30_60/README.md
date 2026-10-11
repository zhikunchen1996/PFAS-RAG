# Corrected Dev13 BGE plus LLM Retrieval-Only Sweep 2026-07-22

Policy: Hybrid poolK -> BGE shortlistK -> LLM final topK.
The selector receives the visible question and full candidate chunks only.

| config | final recall | shortlist recall | pool recall | final MRR | hit-any final | LLM sec/q |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `bge_llm_gpt51_pool60_bge30_llm10_fullchunk` | 0.344 | 0.406 | 0.406 | 0.458 | 6/12 | 7.3 |

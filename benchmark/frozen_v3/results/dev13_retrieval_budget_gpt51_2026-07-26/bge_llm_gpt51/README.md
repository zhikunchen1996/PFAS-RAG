# Frozen V3 Dev13 BGE-LLM GPT-5.1 Retrieval Budget Sweep

Policy: Hybrid poolK -> BGE shortlistK -> LLM final topK.
The selector receives the visible question and full candidate chunks only.

| config | final recall | shortlist recall | pool recall | final MRR | hit-any final | LLM sec/q |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `bge_llm_gpt51_pool120_bge60_llm20_fullchunk` | 0.442 | 0.475 | 0.517 | 0.388 | 8/12 | 11.6 |
| `bge_llm_gpt51_pool30_bge15_llm5_fullchunk` | 0.311 | 0.339 | 0.356 | 0.361 | 6/12 | 3.8 |
| `bge_llm_gpt51_pool60_bge30_llm10_fullchunk` | 0.372 | 0.406 | 0.406 | 0.426 | 7/12 | 7.3 |

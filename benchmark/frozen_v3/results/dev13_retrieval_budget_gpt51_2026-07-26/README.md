# Dev13 Retrieval Budget Sweep with GPT-5.1

Hybrid and BGE outputs are hash-locked, byte-identical reusable results promoted from Frozen V2. Runtime validation uses only the internal V3 copy. All BGE-LLM rows were rerun with GPT-5.1, temperature 0, the visible question, and complete candidate chunks.

| System | Budget | Required-gold recall | Gold-document recall | MRR | Hit any | Selector tokens |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| Hybrid | 5/30 | 0.200 | 0.301 | 0.169 | 4/12 | 0 |
| Hybrid | 10/60 | 0.200 | 0.454 | 0.158 | 4/12 | 0 |
| Hybrid | 20/120 | 0.200 | 0.662 | 0.113 | 4/12 | 0 |
| BGE | 5/30 | 0.211 | 0.368 | 0.174 | 4/12 | 0 |
| BGE | 10/60 | 0.278 | 0.464 | 0.180 | 5/12 | 0 |
| BGE | 20/120 | 0.389 | 0.658 | 0.173 | 6/12 | 0 |
| BGE-LLM | 5/15/30 | 0.311 | 0.568 | 0.361 | 6/12 | 84305 |
| BGE-LLM | 10/30/60 | 0.372 | 0.610 | 0.426 | 7/12 | 165322 |
| BGE-LLM | 20/60/120 | 0.442 | 0.696 | 0.388 | 8/12 | 326032 |

Required-gold recall, gold-document recall, and MRR are macro-averaged over the 12 of 13 Dev questions with at least one required-gold record. Negative-gold retrieval is reported separately in `negative_gold_retrieval_summary.csv`.

## Cost

Total selector calls: 39.
Total selector tokens: 575,659.
Estimated selector cost: USD 0.9129.
The deterministic BGE fallback filled 7 final-context positions when the selector returned fewer than the requested number of valid IDs.

Mean BGE-LLM required-gold recall across budgets: 0.375.

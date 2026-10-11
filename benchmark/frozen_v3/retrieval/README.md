# Frozen V3 Historical Retrieval Artifact

`dev13_bge_llm_gpt51_10_30_60` is a byte-identical copy of the pre-freeze
GPT-5.1 selector run used by Frozen V3 Revision 1.

It is **not canonical for Revision 2**. Its compact selector prompt differs
from the expanded prompt used by the retrieval-budget sweep, and its final
top-ten contexts differ for all 13 Dev questions.

Revision 2 reads the exact middle-budget output at:

`../results/dev13_retrieval_budget_gpt51_2026-07-26/bge_llm_gpt51/retrieval_outputs/rag_outputs_bge_llm_gpt51_pool60_bge30_llm10_fullchunk.jsonl`

This directory remains only for historical provenance. Its integrity and
noncanonical status are recorded in:

`benchmark/frozen_v3/methods/promoted_reusable_artifacts.json`

# Dev13 Retrieval-Only Sweep 2026-06-08

This run does not generate answers or call LLM judges. It writes benchmark-ready RAG output JSONL files with empty `answer` fields.

Configs:

- `hybrid_top5_pool30_win0` -> `benchmark/frozen249/results/dev13_corrected_retrieval_sweep_2026-07-22/local_hybrid_bge/retrieval_outputs/rag_outputs_hybrid_top5_pool30_win0.jsonl`
- `bge_base_top5_pool30_nodoccap` -> `benchmark/frozen249/results/dev13_corrected_retrieval_sweep_2026-07-22/local_hybrid_bge/retrieval_outputs/rag_outputs_bge_base_top5_pool30_nodoccap.jsonl`
- `hybrid_top10_pool60_win0` -> `benchmark/frozen249/results/dev13_corrected_retrieval_sweep_2026-07-22/local_hybrid_bge/retrieval_outputs/rag_outputs_hybrid_top10_pool60_win0.jsonl`
- `bge_base_top10_pool60_nodoccap` -> `benchmark/frozen249/results/dev13_corrected_retrieval_sweep_2026-07-22/local_hybrid_bge/retrieval_outputs/rag_outputs_bge_base_top10_pool60_nodoccap.jsonl`
- `hybrid_top20_pool120_win0` -> `benchmark/frozen249/results/dev13_corrected_retrieval_sweep_2026-07-22/local_hybrid_bge/retrieval_outputs/rag_outputs_hybrid_top20_pool120_win0.jsonl`
- `bge_base_top20_pool120_nodoccap` -> `benchmark/frozen249/results/dev13_corrected_retrieval_sweep_2026-07-22/local_hybrid_bge/retrieval_outputs/rag_outputs_bge_base_top20_pool120_nodoccap.jsonl`

Key files:

- `summary_retrieval_metrics.csv`
- `per_question_retrieval_metrics.csv`
- `retrieval_outputs/rag_outputs_*.jsonl`
- `runtime_metrics.csv`
- `bge_candidate_scores.jsonl`

Metric convention:

- `final_*` metrics evaluate the actual context budget supplied to the answer model.
- `ranking_pool_*` metrics evaluate the full ranked candidate pool, useful for fixed-depth ranking comparisons such as `ranking_pool_required_gold_recall@10`.

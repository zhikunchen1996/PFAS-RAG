# Derived Test40 Analysis Results

## Retrieval–Answer Coupling

Across 114 question–system observations from 38 questions, required-gold recall@10 had a Spearman association of rho = 0.230 with final-answer quality (question-cluster bootstrap 95% CI -0.012 to 0.459). This is a descriptive association and not a causal estimate.

- No gold retrieved: mean final-answer quality 0.436 ± 0.267 SD (question-cluster bootstrap 95% CI 0.312 to 0.559; n = 40 observations).
- Partially retrieved: mean final-answer quality 0.555 ± 0.281 SD (question-cluster bootstrap 95% CI 0.434 to 0.678; n = 42 observations).
- Fully retrieved: mean final-answer quality 0.590 ± 0.261 SD (question-cluster bootstrap 95% CI 0.481 to 0.712; n = 32 observations).

Paired BGE-LLM transitions relative to each baseline:

- BGE-LLM minus BGE: declined/declined: 1; declined/improved: 2; improved/declined: 3; improved/improved: 6; unchanged/declined: 5; unchanged/improved: 14; unchanged/unchanged: 7.
- BGE-LLM minus Hybrid: declined/declined: 2; improved/declined: 1; improved/improved: 9; improved/unchanged: 1; unchanged/declined: 6; unchanged/improved: 15; unchanged/unchanged: 4.

All 74 question–system cases that retrieved at least one required-gold record visibly cited at least one corresponding unique gold chunk. Thus, the operational retrieved-but-not-cited path was not observed; incomplete answers primarily reflect synthesis/coverage limitations rather than complete omission of every retrieved required-gold chunk.

## Failure Paths

- Hybrid: partial_required_gold_retrieval = 13; full_gold_used_but_incomplete_answer = 8; gold_document_miss = 8; gold_chunk_miss_after_doc_hit = 7; full_gold_used_with_material_or_boundary_error = 2; not_applicable_no_required_gold = 2.
- BGE: partial_required_gold_retrieval = 13; gold_chunk_miss_after_doc_hit = 8; gold_document_miss = 7; full_gold_used_but_incomplete_answer = 6; full_gold_used_with_material_or_boundary_error = 3; not_applicable_no_required_gold = 2; complete_core_reference_coverage = 1.
- BGE-LLM: partial_required_gold_retrieval = 16; full_gold_used_but_incomplete_answer = 9; gold_chunk_miss_after_doc_hit = 5; gold_document_miss = 5; full_gold_used_with_material_or_boundary_error = 2; not_applicable_no_required_gold = 2; complete_core_reference_coverage = 1.

The categories are deterministic operational labels. They identify where the frozen pipeline lost benchmark-referenced information; they do not prove a unique causal mechanism or the absence of other valid evidence.

## Cost–Performance

- BGE: deployment API cost USD 1.5140 total (0.0379/question), 554,731 tokens, and mean L3 0.498.
- BGE-LLM: deployment API cost USD 2.4365 total (0.0609/question), 1,074,473 tokens, and mean L3 0.573.
- Hybrid: deployment API cost USD 1.4719 total (0.0368/question), 545,281 tokens, and mean L3 0.503.

Matched multibase answer-generation cost only:

- gpt51_direct: USD 0.7369 (0.0184/question), mean L3 0.362.
- gpt51_rag: USD 1.0184 (0.0255/question), mean L3 0.591.
- gemini31_pro_direct: USD 0.6169 (0.0154/question), mean L3 0.299.
- gemini31_pro_rag: USD 1.1969 (0.0299/question), mean L3 0.453.
- claude_sonnet5_direct: USD 0.4989 (0.0125/question), mean L3 0.307.
- claude_sonnet5_rag: USD 1.2456 (0.0311/question), mean L3 0.533.

Local retrieval, local BGE reranking, indexing, and judge calls are excluded from deployment cost. The multibase table also excludes the shared frozen retrieval and tagger costs, so it is an answer-generation comparison rather than a full-pipeline cost comparison.

# Test40 Multibase L1.5 Results

Status: complete

Execution date: 2026-08-07

## Scope

The frozen L1.5 citation-support judge was applied once to the 40 existing RAG
answers from each of three base models. All systems received the same frozen
BGE-LLM top-10 context for each question. No answer was regenerated, and no
Direct answer was evaluated because Direct had no retrieved context or chunk
citations.

L1.5 received no gold evidence, reference ledger, retrieval scores, system
identity, or outside evidence. It measures whether material claims are
supported by their cited supplied chunks. It is supplementary to the L3
final-answer analysis and does not measure answer completeness.

## Citation Support

| RAG base model | Applicable questions | Cited claims | Supported cited-claim rate | Mean question-level support | Unsupported | Contradicted | Uncited source-dependent claims |
|---|---:|---:|---:|---:|---:|---:|---:|
| GPT-5.1 | 40 | 829 | 0.995 | 0.994 | 4 | 0 | 163 |
| Gemini 3.1 Pro Preview | 40 | 321 | 0.984 | 0.986 | 5 | 0 | 88 |
| Claude Sonnet 5 | 40 | 465 | 0.970 | 0.968 | 11 | 3 | 111 |

Perfect question-level citation support was observed for 36/40 GPT-5.1
answers, 35/40 Gemini answers, and 30/40 Claude answers. Median question-level
support was 1.0 for all three systems.

The results indicate high citation grounding for all three base models under a
shared retrieval condition. GPT-5.1 had the highest support values, followed by
Gemini and Claude. The raw claim and uncited-claim counts should not be treated
as normalized model scores because the models differed substantially in answer
length, claim granularity, and citation density.

## Manuscript Use

This is a post-freeze supplementary analysis for Results Section 3.3. It can
support a descriptive comparison of how different base models use and cite the
same retrieved evidence. It must not replace L3, change the frozen system
ordering, or be described as a retrieval result.


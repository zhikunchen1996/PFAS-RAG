# Test40 Matched Direct versus RAG Results

Status: complete
Execution date: 2026-07-30
Pre-run tag: `test40-multibase-direct-rag-v1-prerun-2026-07-30`
Execution amendment tag:
`test40-multibase-direct-rag-v1-amendment1-2026-07-30`

## Matched Comparison

Within each base model, Direct and BGE-LLM RAG used the same scientific
instructions, task framing, four-section answer structure, lack of a word
limit, and 5000-token output ceiling. The only intended treatment difference
was the evidence condition: Direct received no retrieved evidence, whereas
RAG received the frozen top-10 chunks, common soft tags, and source-use
instructions.

L3 removed citation markers before judging. The judge received one anonymous
answer and the frozen candidate-blind reference claim ledger. It did not
receive the system, base-model identity, retrieved context, or competing
answer, and it did not reward citation count, format, or coverage.

## L3 Final-Answer Evaluation

The primary value is the equal mean of three complete canonical GPT-5.1 judge
repeat-specific system means. The uncertainty value is the sample standard
deviation across those three means and is not a confidence interval.

| Base model | Direct mean | Direct SD | RAG mean | RAG SD | RAG minus Direct | Delta SD |
|---|---:|---:|---:|---:|---:|---:|
| GPT-5.1 | 0.362 | 0.020 | 0.591 | 0.019 | +0.229 | 0.033 |
| Gemini 3.1 Pro Preview | 0.299 | 0.017 | 0.453 | 0.016 | +0.154 | 0.023 |
| Claude Sonnet 5 | 0.307 | 0.006 | 0.533 | 0.012 | +0.226 | 0.017 |

RAG exceeded its matched Direct arm for all three base models in every judge
repeat. The direction therefore agrees with the Dev13 development result,
although the Test40 effect magnitudes are the primary reported values for this
experiment.

## Repeat-Level Direction

| Base model | Repeat | RAG better | Tie | Direct better | Mean delta |
|---|---:|---:|---:|---:|---:|
| GPT-5.1 | 1 | 28 | 9 | 3 | +0.257 |
| GPT-5.1 | 2 | 26 | 10 | 4 | +0.193 |
| GPT-5.1 | 3 | 29 | 5 | 6 | +0.237 |
| Gemini 3.1 Pro Preview | 1 | 22 | 11 | 7 | +0.128 |
| Gemini 3.1 Pro Preview | 2 | 24 | 10 | 6 | +0.163 |
| Gemini 3.1 Pro Preview | 3 | 24 | 9 | 7 | +0.171 |
| Claude Sonnet 5 | 1 | 26 | 10 | 4 | +0.209 |
| Claude Sonnet 5 | 2 | 27 | 10 | 3 | +0.227 |
| Claude Sonnet 5 | 3 | 29 | 9 | 2 | +0.242 |

These counts describe the sign of the within-question L3 score difference.
They are descriptive and are not a separate pairwise-judge result.

## Usage and Cost

- Persisted formal candidates: 240
- Persisted formal L3 judgments: 720
- Tracked tokens: 7,313,062
- Tracked cost: USD 23.956625
- Generation latency sum: 5,989.841 seconds
- L3 latency sum: 17,405.662 seconds
- Four schema-invalid L3 responses were rejected before scoring and replaced
  only through request-hash-validated resume.
- Two pre-amendment Claude refusal responses were discarded before refusal
  persistence was added; their exact usage is unavailable.
- Thirty Gemini HTTP 503 attempts returned no completion or usage metadata.
- The estimated bill including the four invalid L3 responses and two early
  Claude refusals is approximately USD 24.06; this estimate is separate from
  the tracked-cost total.

Claude Direct returned one formal provider refusal for `WF10_012`. The refusal
was retained and scored as the candidate answer rather than retried until a
substantive answer appeared.

No Test40 result was used to alter the questions, references, retrieved
contexts, prompts, model choices, L3 metric, repeat count, or aggregation.

# Execution Accounting

## Valid execution

- Valid persisted judgments: 120
- Judge: GPT-5.1 (`gpt-5.1-2025-11-13`)
- Reasoning effort: low
- Repeats: one per answer
- Tracked tokens: 999,744
- Tracked cost: USD 5.13047125
- Summed API latency: 4,244.277 seconds

By answer source:

| RAG base model | Valid calls | Tokens | Cost (USD) | Summed latency (s) |
|---|---:|---:|---:|---:|
| GPT-5.1 | 40 | 406,028 | 2.18760500 | 1,916.612 |
| Gemini 3.1 Pro Preview | 40 | 271,831 | 1.27638875 | 1,056.756 |
| Claude Sonnet 5 | 40 | 321,885 | 1.66647750 | 1,270.909 |

## Rejected response

The first GPT-5.1 RAG judgment for `NQ09` returned JSON that failed the frozen
cited-claim schema. It was rejected before aggregation and was not persisted as
a valid result. The answer was judged again only through request-hash-validated
resume. The replacement used 8,693 tokens and cost USD 0.04590125; this value
is used only as a proxy for the unrecorded rejected-response cost. The estimated
bill including that response is therefore approximately USD 5.18.

The initial sandboxed execution attempt could not reach the API and made no
paid calls.


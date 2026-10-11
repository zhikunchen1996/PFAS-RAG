# Execution accounting

This ledger records provider attempts that did not produce a persisted formal
candidate row and therefore do not appear in the normal per-answer usage
summaries.

## Generation overhead before execution amendment 1

| Provider/system | Event | Attempts | Persisted candidates | Cost treatment |
|---|---|---:|---:|---|
| Gemini 3.1 Pro Direct | HTTP 503 high demand | 18 | 0 | No completion or usage metadata returned; recorded as unsuccessful service attempts and excluded from tracked token cost |
| Gemini 3.1 Pro RAG | HTTP 503 high demand | 12 | 0 | No completion or usage metadata returned; recorded as unsuccessful service attempts and excluded from tracked token cost |
| Claude Sonnet 5 Direct | `stop_reason=refusal` for `WF10_012` | 2 | 0 | Provider responses were discarded by the pre-amendment implementation; token usage and exact cost are unavailable and must be disclosed as untracked paid-call overhead |

The next `WF10_012` call uses execution amendment 1 and will persist a refusal
as the formal candidate output if the provider refuses again. Its usage will
then be included in the normal answer ledger.

All six generation arms subsequently reached 40/40 persisted formal
candidates. Tracked successful generation usage was 1,274,731 tokens and
USD 5.3136545. This excludes the 30 Gemini 503 attempts and the two
pre-amendment Claude refusals described above.

## L3 structured-output overhead

| Repeat | Candidate | Event | Persisted judgment on attempt | Cost treatment |
|---|---|---|---:|---|
| 1 | `gpt51_rag::WF10_005` | Schema-invalid judge response | 0 | Exact usage unavailable; excluded from tracked cost |
| 1 | `gemini31_pro_direct::NQ20` | Schema-invalid judge response | 0 | Exact usage unavailable; excluded from tracked cost |
| 3 | `gemini31_pro_direct::WF10_032` | Schema-invalid judge response | 0 | Exact usage unavailable; excluded from tracked cost |
| 3 | `claude_sonnet5_direct::NQ08` | Schema-invalid judge response | 0 | Exact usage unavailable; excluded from tracked cost |

Each item was completed through exact request-hash-validated resume. No
already valid judgment was regenerated. All three repeats subsequently reached
240/240 persisted judgments.

## Final tracked totals

- Persisted generation calls: 240
- Persisted L3 judge calls: 720
- Tracked tokens: 7,313,062
- Tracked cost: USD 23.956625
- Untracked attempts: 30 Gemini HTTP 503 responses, two pre-amendment Claude
  refusals, and four schema-invalid L3 responses
- Approximate total bill after estimating the six likely paid untracked
  responses: USD 24.06

Service errors and schema-invalid paid responses are not silently folded into
the tracked-cost total.

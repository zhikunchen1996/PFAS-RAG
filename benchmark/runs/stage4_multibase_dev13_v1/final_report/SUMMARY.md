# Dev13 multi-base-model L3 V3 summary

Canonical claim order is primary; reverse order is sensitivity only.
No binary pass metric or human candidate-answer calibration is used.

| Base model | Direct core | RAG core | RAG-Direct | 95% CI |
|---|---:|---:|---:|---:|
| GPT-5.1 | 0.446 | 0.644 | 0.199 | [0.106, 0.304] |
| Gemini 3.1 Pro Preview | 0.433 | 0.459 | 0.027 | [-0.058, 0.113] |
| Claude Sonnet 5 | 0.295 | 0.593 | 0.298 | [0.151, 0.446] |

Reverse-order within-model effects:

- GPT-5.1: 0.153 [0.036, 0.295]
- Gemini 3.1 Pro Preview: 0.010 [-0.061, 0.083]
- Claude Sonnet 5: 0.284 [0.134, 0.460]

Incremental Gemini + Claude generation and L3 judging cost: USD 3.543. Retrieval and common tagging were reused without new calls.

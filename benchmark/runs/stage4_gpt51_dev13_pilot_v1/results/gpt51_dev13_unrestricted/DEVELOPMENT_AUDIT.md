# V1.2 development audit

## Status

This run is structurally valid but is not the final Stage 4 pilot result. It
was evaluated only on Dev13 and is retained to document prompt development.

## Validation

- Direct answers: 13/13
- RAG answers: 13/13
- Mirrored L2 judge calls: 26/26
- Returned generation and judge snapshot: `gpt-5.1-2025-11-13`
- Position-bias exact tests: no detected imbalance
- Word-count exclusion or retry: none

## Diagnostic result

Raw votes favored Direct:

| Criterion | Direct | RAG | Tie |
|---|---:|---:|---:|
| Scientific correctness | 10 | 2 | 14 |
| Question fulfillment | 12 | 6 | 8 |
| Scope and calibration | 18 | 1 | 7 |
| Practical usefulness | 17 | 4 | 5 |

Mirrored agreement was 53.8% for scientific correctness and question
fulfillment, and 76.9% for scope and calibration and practical usefulness.

## Blocking issue

The two generation arms did not receive perfectly matched permission to use
base-model knowledge. The Direct user prompt explicitly said to use reliable
general scientific knowledge. The RAG user prompt discussed only retrieved
evidence and its use. Judge rationales repeatedly favored Direct for broad
domain coverage and described RAG as overly constrained by the retrieved
material. That difference can reflect prompt wording rather than retrieval
value.

## Resolution

V1.3 moves the reliable-general-knowledge instruction into the shared system
prompt. The arm prompts then differ only in information availability and the
handling of supplied evidence. Both arms are regenerated in full. Frozen L2
prompts, criteria, model, mirrored schedule, and aggregation remain unchanged.

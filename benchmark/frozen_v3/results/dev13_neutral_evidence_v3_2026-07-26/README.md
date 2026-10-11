# Dev13 Neutral-Evidence Pairwise Evaluation

This is the canonical Frozen V3 Revision 3 answer-quality evaluation.

## Comparison

- Frozen V3 BGE-LLM RAG answers versus prompt-matched GPT-5.1 Direct answers
- GPT-5.1 judge at temperature 0
- three temperature-zero API re-samples
- both A/B orientations for every question
- 78 judge calls in total

The model-visible payload contains no system name, question ID, task label,
answerability label, repeat number, orientation, or citation marker. Reference
gold is explicitly non-exhaustive. Verification evidence is the deduplicated
union of the frozen Hybrid, BGE, and BGE-LLM top-10 contexts, sorted by
document and chunk identity without system or ranking labels.

The union contains 20.8 chunks per question on average. It necessarily
contains all ten canonical RAG chunks, with about 3.9 chunks per question
unique to that retriever. Direct remains a no-retrieval generation baseline,
not an information-matched answer-generation arm.

## Result

| Outcome | Questions |
| --- | ---: |
| Frozen V3 wins | 10 |
| Direct wins | 3 |
| Ties | 0 |

Mean weighted Frozen V3 score: 0.7846.

Mirrored criterion agreement: 0.7692.

Seventeen of 78 responses (21.8%) required normalization of non-scoring
auxiliary schema fields, totaling 51 repairs. Every scored criterion
preference and rationale was present.

The three Direct wins were `NQ24`, `WF10_002`, and `WF10_021`.

## Cost

- prompt tokens: 1,017,873
- completion tokens: 55,628
- total tokens: 1,073,501
- estimated API cost under the recorded price basis: USD 1.8286

## Reproduction

Use a new output directory. The runner refuses to overwrite a non-empty
directory unless `--resume` is explicitly supplied.

```bash
.venv/bin/python \
  benchmark/frozen_v3/scripts/run_dev13_neutral_evidence_judge_v3.py \
  --out benchmark/frozen_v3/results/<new-run-directory> \
  --workers 9 \
  --repeats 3
```

The canonical run was fresh: `resume_enabled` is false.

Historical citation-blind and RAG-context source-verified results are retained
as judge-sensitivity analyses. They are not interchangeable with this result.

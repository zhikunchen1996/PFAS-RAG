# Frozen V3 Revision 2 Dev13 Generation

This is the canonical selector-aligned generation run for Frozen V3 Revision
2. It uses the exact `10/30/60` output from the GPT-5.1 retrieval-budget sweep,
not the superseded compact-prompt selector run.

## Command

```bash
.venv/bin/python benchmark/frozen_v3/scripts/run_dev13_soft_tags_v3.py \
  --workers 6
```

The run was fresh (`resume_enabled=false`) and generated:

- 13 soft-tag records;
- 13 tagged BGE-LLM RAG answers;
- 13 prompt-matched Direct answers;
- no matched-untagged diagnostic.

GPT-5.1 (`gpt-5.1-2025-11-13`) was used at temperature 0 for the tagger,
RAG answer, and Direct answer. Gold was not supplied to any of these stages.

## Tag Interface

All 130 retrieved chunks retained their full text and original order. The
answer model received only categorical role, detail policy, polarity,
confidence, and a locally verified source excerpt. Of 130 proposed excerpts,
91 passed normalized substring verification and 37 were cleared. The full
chunk remained available in every case. No structural tag error or
answer-facing free-text advisory field was retained.

## Cost

- Prompt tokens: 157,960
- Completion tokens: 55,896
- Total tokens: 213,856
- Estimated cost: USD 0.7564

Exact input hashes, returned model snapshots, per-question tag counts, and
token details are in `generation_manifest.json`.


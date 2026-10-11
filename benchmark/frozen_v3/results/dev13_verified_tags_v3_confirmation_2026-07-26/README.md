# Dev13 Verified-Tag V3 Generation

Date: 2026-07-26

Status: `frozen_canonical_generation`

This run regenerated all Dev13 tag, BGE-LLM RAG, and prompt-matched Direct
outputs after removal of the answer-facing free-text tag channel. Test40 was
not inspected or run.

The tagger and both answer systems used GPT-5.1 at temperature 0. BGE-LLM used
the frozen `60 -> 30 -> 10` retrieval output. The answer model received all ten
chunks in their original order.

## Verified tag interface

The answer-visible interface contains only:

- categorical evidence role;
- categorical detail policy;
- categorical evidence polarity;
- confidence;
- a locally validated verbatim excerpt, when validation succeeds;
- the complete source chunk.

Question-component descriptions and component assignments are audit-only.
`allowed_use`, `avoid_use`, and `omit_details` are absent from the prompt
schema, validated tag object, and formatted answer context. Legacy values with
those keys are discarded.

Of 130 chunk tags, 96 contained a locally verified excerpt and 34 contained no
excerpt. Thirty-two proposed excerpts failed verbatim validation and were
cleared; the other two were returned empty by the tagger.

## Cost

Tagging plus tagged RAG and matched Direct generation used 216,264 tokens at
an estimated cost of USD 0.7753. The exact accounting and input hashes are in
`generation_manifest.json`.

Run command:

```bash
.venv/bin/python benchmark/frozen_v3/scripts/run_dev13_soft_tags_v3.py \
  --include-direct --workers 6
```

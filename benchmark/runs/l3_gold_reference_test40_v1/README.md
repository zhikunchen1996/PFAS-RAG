# Test40 L3 candidate-blind reference construction

Status on 2026-07-29: **frozen as
`l3_test40_reference_v1_2026-07-29`; formal Test40 L3 scoring not started.**

This package constructs Test40 L3 reference claim ledgers without reading any
candidate Test40 answer, candidate retrieved context, system identity, or
Test40 evaluation result.

The workflow is:

1. build allowlisted source packets from frozen questions, project-author-
   retained gold records, and the exact repaired-corpus chunks;
2. draft task components with GPT-5.1;
3. freeze the task-component payloads before claim drafting;
4. draft structured reference claim ledgers with GPT-5.1;
5. independently verify every ledger against the source packets with Claude
   Sonnet through the project author's Pro subscription;
6. repair and re-review non-clean ledgers;
7. prepare a project-author audit packet; and
8. freeze and hash the approved ledgers before any Test40 candidate scoring.

## Frozen artifacts

```text
frozen/reference_claim_ledgers_test40_v1.jsonl
frozen/FREEZE_RECORD.md
frozen/freeze_manifest.json
frozen/freeze_manifest.sha256
frozen/author/project_author_approval_record.json
frozen/l15_validation/summary/summary.csv
```

Freeze checks:

- 40/40 questions have a locally valid ledger;
- 40/40 latest Claude Sonnet reviews are `clean`;
- every ledger exact span is verbatim in its approved full original chunk;
- the ledger-rendered L1.5 V2 gold answers passed for 40/40 questions and
  172/172 cited claims, with no unsupported, contradicted, or uncited
  source-dependent claims;
- 165 newly selected verbatim spans across 23 questions are retained under the
  project author's explicit conditional batch approval;
- the approval record does not claim individual manual review; and
- no candidate Test40 answer, candidate retrieved context, system identity, or
  Test40 result was used.

Validation command:

```bash
.venv/bin/python \
  benchmark/runs/l3_gold_reference_test40_v1/scripts/validate_reference_freeze.py
```

The freeze manifest contains 76 hash-verified artifacts. Its SHA-256 is:

```text
885135b75a44e9248a8d5e679c17b452e9065d2c7833420ccbce7084b1877414
```

The legacy `gold_minimal_answer` and `gold_full_answer` columns are explicitly
forbidden. Machine-written `supported_claim` and similar summary metadata are
also excluded from model-visible source packets; the models receive exact
evidence spans and full original chunk text instead.

The scope-invalid L1.5 V1 diagnostic and its builder are archived under:

```text
benchmark/archive/2026-07-29_l1_l15_l3_cleanup/test40_reference_diagnostics
```

They are not valid current evaluation inputs.

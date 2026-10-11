# L3 gold-referenced adequacy, Dev13 V2

Status: **historical frozen-reference package; Dev Step 3 scoring complete;
candidate-answer adequacy calibration cancelled before labeling**

The active scoring successor is
`benchmark/runs/l3_gold_reference_dev13_v3_continuous`. V2 remains the
provenance source for reference construction and the original Dev13 judge
calls. Its frozen reference and freeze manifest were not modified.

This package separates two answer-evaluation questions:

- **L2** compares retrieval systems on citation-blind common answer quality.
- **L3** measures completion of frozen, project-author-approved,
  literature-specific reference claims for matched Direct and RAG answers.

L3 does not replace retrieval metrics, citation support, or L2. Its gold is
non-exhaustive, so L3 is not a universal scientific truth or hallucination
metric.

## V2 changes

The original V1 draft used mutually exclusive
`core/supporting/limitation/negative_boundary` labels and averaged raw atomic
claims. GPT-5.6 Pro identified that design as vulnerable to duplicated weights
and an unsupported binary threshold.

V2 therefore:

1. freezes question-derived task components before candidate scoring;
2. separates `importance`, `function`, and `scoring_role`;
3. retains atomic claims for evidence auditing but scores deduplicated claim
   groups;
4. excludes constraint-only groups from coverage denominators;
5. treats the claim ledger as normative and prose as non-normative;
6. uses component-balanced, question-macro core coverage as the primary
   continuous metric;
7. does not produce binary pass/fail until a threshold is calibrated against
   blinded project-author adequacy labels on Dev13.

## Candidate-blind construction

Reference construction may use only:

- the frozen question;
- pre-answer task boundaries and task components;
- all project-author-audited gold chunks;
- candidate-blind prior reference drafts and independent reviews.

It may not use candidate Direct/RAG answers, retrieved top-k contexts, system
identity, candidate judge outcomes, or Test40 L3 outcomes.

Model A (`gpt-5.1-2025-11-13`) revises and groups the candidate-blind ledger.
Model B (`claude-sonnet-5` through the logged-in Claude CLI) verifies every
group against exact evidence spans. Every non-clean review enters a traceable
repair and re-review round.

The frozen repair7 checkpoint is:

```text
reference_build/inputs/reference_packets_repair6.jsonl
reference_build/revisions/model_a_revisions_v2_repair7.jsonl
reference_build/reviews/model_b_group_reviews_v2_repair7.jsonl
reference_build/reviews/REPAIR7_REVIEW_STATUS_2026-07-29.md
human_review_repair7/reference_candidates.jsonl
human_review_repair7/decision_register.csv
human_review_repair7/HUMAN_AUDIT_PACKET.md
human_review_repair7/build_manifest.json
frozen/reference_claim_ledgers_v2.jsonl
frozen/freeze_manifest_v2.json
```

Model B approved 11/13 repair5 ledgers and 12/13 repair6 ledgers. The only
repair6 blocker was a numeric-rule inconsistency in `WF10_002-G06`; repair7
removed the accidental exact-temperature requirement because this is an
endpoint-distinction task. Repair7 reused 12 byte-stable clean reviews and
independently re-reviewed the changed `WF10_002` ledger. Final Model B result:
13/13 approve and clean, with no blocking issue arrays.

The project author explicitly approved all 13 repair7 ledgers before viewing
candidate answers or L3 scores. All 65 project-author checks are complete.
The normative frozen reference SHA-256 is
`0ad2bbfae02c30433ab030c36ad2e95d1278d029f3378d7111e1df63e18c413a`.

The `human_review_v2` packet is the earlier repair4 audit checkpoint and must
not be treated as the current repair7 packet. The current packet is
`human_review_repair7`.

## Dev Step 3

GPT-5.1 matched Direct and BGE-LLM RAG answers were scored independently with
the frozen L3 judge in canonical and reverse claim order:

- 2 systems
- 13 questions per system
- 26 candidate answers
- 52 total judge calls across both orders
- canonical order is the predeclared primary result
- reverse order is a sensitivity analysis
- no binary threshold was used
- Test40 was not run

The later candidate-answer human adequacy-labeling plan was cancelled before
any labels were collected. The following files are retained only as
provenance and must not be completed for the active protocol:

```text
results/dev13_gpt51_direct_vs_bge_llm_rag_repair7/
human_adequacy_calibration_repair7/sealed_mapping/
```

The blinded public packet is:

```text
human_adequacy_calibration_repair7/BLINDED_ADEQUACY_PACKET.md
human_adequacy_calibration_repair7/adequacy_register.csv
human_adequacy_calibration_repair7/blinded_candidates.jsonl
```

Clean Model B reviews may be reused across repair rounds only when the
canonical revision payload hash is unchanged and the reused review passes
membership and evidence-ID validation against the current packet. The
verification manifest records reused questions separately from new CLI calls.

The final project-author gate requires all five checks for all 13 questions:

- task components approved;
- every claim group reviewed;
- every prior atomic-claim disposition reviewed;
- prose and ledger confirmed consistent;
- all Model B issues resolved.

Any ledger edit after Model B verification requires a new Model B review.

## Continuous scoring

For each frozen content claim group:

- `full = 1`
- `partial = 0.5`
- `absent = 0`
- `contradicted = 0`, with a separate contradiction flag

Core groups are first averaged within each task component. Components are then
averaged within each question, and questions are averaged for each system.
This is the primary **mean component-balanced core reference-claim coverage**.

Secondary outputs are strict-core coverage, supplementary coverage, boundary
compliance, core contradiction rate, reference-anchored material-error rate,
and potential external-error flag rate.

System differences are calculated from paired question-level scores. The
default uncertainty estimate is a 10,000-iteration paired bootstrap over
questions with seed `20260729`; claims are never treated as independent
replicates.

No binary pass is defined. V3 permanently removes threshold calibration from
this experiment and reports continuous coverage with question-level
uncertainty instead.

## Main files

```text
reference_build/inputs/task_components_dev13.jsonl
reference_build/inputs/reference_packets_repair6.jsonl
reference_build/revisions/model_a_revisions_v2_repair7.jsonl
reference_build/reviews/model_b_group_reviews_v2_repair7.jsonl
reference_build/reviews/REPAIR7_REVIEW_STATUS_2026-07-29.md
human_review_repair7/HUMAN_AUDIT_PACKET.md
human_review_repair7/decision_register.csv
human_review_repair7/build_manifest.json
frozen/reference_claim_ledgers_v2.jsonl
frozen/freeze_manifest_v2.json
human_adequacy_calibration_repair7/BLINDED_ADEQUACY_PACKET.md
human_adequacy_calibration_repair7/adequacy_register.csv
results/dev13_gpt51_direct_vs_bge_llm_rag_repair7/STEP3_SEALED_RUN_RECORD.md
prompts/reference_revision_v2.txt
prompts/reference_group_verification_v2.txt
prompts/reference_repair_v2.txt
prompts/l3_gold_referenced_judge_v2.txt
scripts/run_reference_revision_v2.py
scripts/run_reference_group_verification_v2.py
scripts/run_reference_repair_v2.py
scripts/build_human_audit_v2.py
scripts/freeze_references_v2.py
scripts/run_l3_scoring_v2.py
```

V1 artifacts remain available for provenance but are not valid frozen
references or valid V2 scores.

## Required execution order

```bash
uv run python scripts/run_reference_revision_v2.py
uv run python scripts/run_reference_group_verification_v2.py
uv run python scripts/run_reference_repair_v2.py \
  --revisions <round-input.jsonl> \
  --reviews <round-review.jsonl> \
  --out <round-output.jsonl>
uv run python scripts/run_reference_group_verification_v2.py \
  --revisions <round-output.jsonl> \
  --prior-group-reviews <round-input-review.jsonl> \
  --reuse-clean-from <round-input-review.jsonl> \
  --out <round-output-review.jsonl>
uv run python scripts/build_human_audit_v2.py \
  --revisions <final-revisions.jsonl> \
  --reviews <final-reviews.jsonl>
uv run python scripts/freeze_references_v2.py
```

`freeze_references_v2.py` must fail until every project-author check and
decision is complete. Candidate scoring must fail until the V2 reference
freeze exists.

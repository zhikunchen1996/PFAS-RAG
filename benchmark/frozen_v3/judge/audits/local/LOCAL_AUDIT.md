# Final local audit

Audit date: 2026-07-28

Scope: L1, L1.5, and L2 V2 judge implementation; canonical inputs; Dev13
calibration; prompts; statistical aggregation; reproducibility; and held-out
boundaries.

## Findings resolved before external review

| ID | Severity | Finding | Resolution |
|---|---|---|---|
| LA-01 | Major | L1 and L1.5 could accept missing or extra question rows. | All runners now require exact question membership and reject duplicates, omissions, and extras. |
| LA-02 | Major | L2 rejected missing answers but did not reject extra answers; resume could silently collapse duplicate payload IDs. | Exact answer membership and duplicate resume checks are enforced. |
| LA-03 | Major | L1.5 summarization treated a valid answer with no cited source-dependent claim as a schema failure. | Such questions are now retained as `citation_support_applicable=false` and excluded from the claim-rate denominator. |
| LA-04 | Major | A disconnected Davidson comparison graph could yield regularization-dependent abilities. | Disconnected graphs and self-comparisons are now rejected before fitting. |
| LA-05 | Minor | The anonymization audit manifest stored machine-specific absolute paths. | Paths inside the repository are now root-relative. |
| LA-06 | Minor | The judge runtime did not have a compact explicit dependency lock. | Python and direct judge dependencies are pinned under `environment/`. |
| LA-07 | Minor | The manifest validator checked listed hashes but did not detect unlisted package files. | Validator now compares the complete package index with the manifest before checking hashes. |

These changes affect input validation and failure behavior only. They do not
change a metric formula, prompt, stored raw judgment, or accepted Dev13 value.

## Canonical input audit

- Questions: 53 unique total, split into 13 unique Dev and 40 unique Test
  questions with no overlap or duplicates.
- Gold: 249 records across all 53 questions.
- Gold types: 127 required, 95 optional, and 27 negative.
- Canonical question and gold hashes are stored in the package manifest.
- Dev13 calibration retrieval and answer artifacts are also indexed by hash.
- No new L1.5 or L2 V2 Test40 result is stored in this package.

## L1 audit

The frozen L1 runner was executed independently on all three original Dev13
retrieval JSONL files. Every summary metric was identical to the stored
calibration table.

| System | MRR | Required recall@10 | Gold-document recall@10 | Negative recall@10 |
|---|---:|---:|---:|---:|
| Hybrid | 0.157738 | 0.200000 | 0.454167 | 0.000000 |
| BGE | 0.179861 | 0.277778 | 0.463889 | 0.222222 |
| BGE-LLM | 0.425926 | 0.372222 | 0.609722 | 0.388889 |

Nine independent question-system spot calculations were also performed by
directly matching `(doc_id, chunk_id)` against the first ten retrieved chunks.
Examples:

| System | Question | Required hits/count | Recall | Document recall | MRR |
|---|---|---:|---:|---:|---:|
| Hybrid | NQ23 | 1/5 | 0.200 | 0.200 | 0.142857 |
| BGE | NQ23 | 2/5 | 0.400 | 0.400 | 0.333333 |
| BGE-LLM | NQ23 | 2/5 | 0.400 | 0.400 | 0.500000 |
| Hybrid | WF10_002 | 1/1 | 1.000 | 1.000 | 1.000000 |
| BGE | WF10_002 | 0/1 | 0.000 | 0.000 | 0.000000 |
| BGE-LLM | WF10_002 | 1/1 | 1.000 | 1.000 | 1.000000 |

L1 contains no model call.

## L1.5 audit

Dry-run payload generation succeeded for Hybrid, BGE, and BGE-LLM:

- 13 payloads per system;
- exactly ten complete original final chunks per payload;
- only question, cited answer, and complete original context are supplied;
- no gold, post-hoc retrieval, system name, or hidden rubric is supplied.

The prompt assesses material source-dependent claims, joins redundant
citations for the same claim, does not reward citation count or formatting,
and treats `supported` plus `partially_supported` as the claim-level pass set.
Unsupported, contradicted, uncited, and non-applicable cases remain explicit.

## L2 V2 audit

Dry-run generation succeeded for all three Dev13 system pairs:

- 26 payloads per pair: two orientations for each of 13 questions;
- the two assignments are exact A/B mirrors;
- allowed model fields are question, task boundaries, non-exhaustive gold,
  Answer A, and Answer B;
- citations, retrieved context, question IDs, system names, and retrieval
  configurations are absent from model payloads.

Stored raw-call audit:

| Pair | Calls | Returned snapshot | Total tokens | Estimated cost (USD) | Summed latency (s) |
|---|---:|---|---:|---:|---:|
| Hybrid vs BGE | 26 | gpt-5.1-2025-11-13 | 191,843 | 1.188539 | 2,060.490 |
| Hybrid vs BGE-LLM | 26 | gpt-5.1-2025-11-13 | 193,846 | 1.131293 | 1,813.580 |
| BGE vs BGE-LLM | 26 | gpt-5.1-2025-11-13 | 191,457 | 1.105695 | 2,589.673 |

The 10,000-replicate aggregation was rerun from the stored raw votes after the
validation changes. All six output files were byte-identical to the frozen
calibration:

- criterion abilities;
- descriptive composite;
- fit manifest;
- mirrored agreement;
- position diagnostics; and
- raw vote counts.

The fit uses one independently estimated tie parameter per criterion and
rejects disconnected comparison graphs.

## Prompt audit

The prompts contain no PFAS technology-specific decision rule and apply across
numeric extraction, protocol extraction, endpoint distinction, limitation
evidence, cross-study comparison, mechanism, method inventory, and
insufficient-evidence questions.

L2 explicitly prohibits rewards for citations, retrieval access, formatting,
verbosity, length, or similarity to gold wording. Evidence outside the
non-exhaustive gold is neutral unless it is incoherent or violates a visible
task boundary. Numeric specificity is useful only when material to the
question. Calibrated abstention is accepted only when it identifies the actual
evidence limitation.

L1.5 explicitly prohibits outside repair, retrieval evaluation, citation-count
rewards, and a requirement that every redundant citation independently entail
the whole claim.

## Reproducibility and held-out boundary

- Runtime: Python 3.12.13.
- Direct judge dependencies are pinned.
- L1.5 uses GPT-5.1 low reasoning; L2 uses GPT-5.1 medium reasoning.
- Required returned snapshot: `gpt-5.1-2025-11-13`.
- Temperature is not sent because the reasoning interface does not accept it.
- Raw responses, token usage, estimated cost, latency, and manifests are
  retained.
- API inference is not claimed to be bitwise deterministic.
- The new L1.5 prompt and L2 V2 protocol have not been run on Test40.

## Independent review resolution

Claude CLI Sonnet initially found one blocking-pending-verification and two
major issues. Evidence IDs and decoys are now excluded from L2, the
deterministic identity scan is a mandatory pre-API gate, and silent schema
repair has been removed. Optional resume, finish-reason, evidence-semantics,
dependency, and numerical-regularization documentation improvements were also
completed. The targeted follow-up review returned `FREEZE_APPROVED`.

## Local verdict

`PASS`

No unresolved local or Claude blocking/major finding remains. Final
publication is tied to the annotated Git tag
`frozen-judge-2026-07-28-v1`.

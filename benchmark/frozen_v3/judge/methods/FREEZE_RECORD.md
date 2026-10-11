# Frozen judge record

Freeze date: 2026-07-28

Status: frozen for the first Test40 execution. The new L2 V2 judge and the
new claim-level L1.5 judge have not been applied to Test40 before this freeze.

Immutable version: `frozen-judge-2026-07-28-v1`

Git tag: `frozen-judge-2026-07-28-v1`. The tagged commit is resolved with
`git rev-parse frozen-judge-2026-07-28-v1^{commit}`; the annotated tag is the
immutable commit record and avoids a self-referential commit hash inside the
same commit.

## Frozen layers

### L1 retrieval

L1 is deterministic and uses no LLM judge. It reports
`MRR_required_gold`, `required_gold_recall@10`, and
`gold_doc_recall@10`. `negative_gold_recall@10` is retained as a separate
diagnostic.

### L1.5 citation support

L1.5 is a Test40 RAG-only sanity check. It receives the visible question, the
answer with citation markers, and all complete original final chunks. It does
not receive gold and performs no additional retrieval.

The primary unit is a material source-dependent claim. A claim passes when its
cited chunks, considered jointly, support the central proposition
(`supported` or `partially_supported`) and do not contradict it. Redundant
citations attached to one claim are not required to each entail the whole
claim. The development attachment-level diagnostic is retained only as
historical calibration and is not the frozen L1.5 metric.

### L2 answer quality V2

Each system pair is judged twice per question with exactly mirrored A/B order.
The judge receives citation-stripped anonymous answers, pre-answer task
boundaries, and human-audited non-exhaustive gold. It does not receive
retrieved context, system identity, question IDs, retrieval metadata, or
citation information.

All raw A, B, and tie votes are retained. There are no adaptive repeats, no
hard consensus rule, no `unstable` label, and no discarded disagreement.
Four Davidson models are fit separately, one for each criterion. Each fit
estimates its own tie parameter, nu. The four criterion abilities are primary;
their equal-weight mean is descriptive secondary output only.

Evidence IDs and decoy records are removed from the judge payload. A mandatory
deterministic scan rejects citation-stripped answers containing system labels,
retrieval metadata, or question IDs before any API call. Judge JSON must match
the frozen schema exactly; no misspelling repair is permitted. Only responses
with `finish_reason=stop` are accepted.

The Davidson optimizer uses a fixed `1e-6` L2 penalty on the free log-ability
and log-tie parameters for numerical stabilization. It is applied identically
to point estimates and every bootstrap replicate.

## Bootstrap amendment

The earlier 2,000-resample development summary was superseded before freeze.
The frozen implementation performs 10,000 question-level clustered percentile
bootstrap attempts. For every replicate:

1. Dev13 question IDs are sampled with replacement.
2. All pairwise and mirrored votes belonging to each sampled question are
   retained.
3. The same sampled question list is used across all four criteria.
4. Each criterion-specific Davidson model, including its own tie parameter,
   is refit.
5. The secondary equal-weight composite is recomputed within the replicate.

The 95% interval is the 2.5th to 97.5th percentile of successful fits. Failed
fits are not imputed. Their count and rate are reported.

The Dev13 confirmation produced 9,976 successful and 24 failed fits from
10,000 attempts, a non-convergence rate of 0.24%.

## Independent anonymity audit

A deterministic scan found no citation marker, BGE/BGE-LLM label, explicit
retrieval-system label, retrieval metadata, or question ID in 39 anonymous
answers. Standalone `hybrid` was not treated as a leak because it is ordinary
PFAS-domain terminology; explicit system phrases remain prohibited.

Claude Sonnet 5 Medium then attempted a forced one-to-one assignment of the
three anonymous answers for each of 13 Dev questions. It did not receive the
local answer key.

- Correct slots: 15/39 (38.5%); random baseline 33.3%; exact tail
  `p = 0.326`.
- Correct complete mappings: 3/13 (23.1%); random baseline 16.7%; exact
  binomial tail `p = 0.372`.
- Confidence: 12 low, 1 medium.

The audit therefore found no statistically detectable above-chance identity
inference. This is evidence against obvious identity leakage, not proof that
identity can never be inferred. Sonnet's rationales often used answer breadth
and specificity, so residual stylistic inference remains a stated limitation.

## Development result

The 10,000-bootstrap Dev13 result preserved the prior ordering:

| Criterion | Hybrid | BGE | BGE-LLM | Tie parameter |
|---|---:|---:|---:|---:|
| Scientific correctness | 0.296 | 0.313 | 0.391 | 2.346 |
| Question fulfillment | 0.105 | 0.227 | 0.669 | 1.784 |
| Scope and calibration | 0.435 | 0.262 | 0.303 | 0.799 |
| Practical usefulness | 0.194 | 0.240 | 0.565 | 0.648 |

The different tie-parameter estimates are expected because the four criteria
show different tie frequencies. They are not manually selected parameters.

## External review

An earlier focused Claude review of L2 V2 recommended “freeze with minor
changes.” Its three requested changes were:

1. specify at least 10,000 bootstrap replicates and disclose fit failures;
2. state and enforce a separate tie parameter for each criterion; and
3. perform a one-time anonymous system-identity audit.

All three requirements are implemented in this frozen directory.

A final full-package Claude CLI Sonnet review then identified three additional
pre-freeze issues: evidence IDs could expose question IDs, the deterministic
identity-leakage scan was not yet a production gate, and a misspelled schema
key was silently repaired. The implementation now removes evidence IDs and
decoys from the L2 payload, fails before API calls on identity leakage, and
requires the exact response schema. The targeted verification returned
`FREEZE_APPROVED`; the full resolution is stored in
`reviews/CLAUDE_RESOLUTION.md`.

The stored Dev13 raw judgments predate those payload-hardening changes. No
scientific evidence span, answer, task boundary, raw vote, metric formula, or
aggregation changed. Re-aggregation remained byte-identical. Final no-cost
dry runs verify the hardened payload that will be used for Test40.

## Final verification gate

- 14/14 unit tests passed.
- Every Python script and test compiled successfully.
- The Hybrid L1 smoke test reproduced the frozen Dev13 summary.
- Hybrid, BGE, and BGE-LLM each produced 13 valid L1.5 dry-run payloads.
- All three system pairs each produced 26 valid mirrored L2 dry-run payloads.
- The final L2 payload scan found no question ID, evidence ID, system label,
  retrieval metadata, or citation marker.
- Re-running the 10,000-bootstrap aggregation reproduced all six canonical
  output files byte-for-byte.
- Rebuilding and rescoring the anonymization audit reproduced both canonical
  scored files byte-for-byte.
- The final manifest validator passed before publication.

# Test40 L3 reference freeze record

Release: `l3_test40_reference_v1_2026-07-29`

Freeze date: 2026-07-29

## Decision

The candidate-blind Test40 L3 reference package is frozen. The project author
explicitly authorized freezing if the gold answer completed the previously
agreed lenient Frozen L1.5 check. The corrected L1.5 V2 scope rendered only
normative answer-content `claim_groups`; `constraint_groups` remain L3
violation rules and were not treated as statements a gold answer must make.

The condition passed:

- 40/40 questions applicable and passed;
- 172/172 cited claims were `supported` or `partially_supported`;
- 0 `not_supported` claims;
- 0 `contradicted` claims; and
- 0 uncited source-dependent claims.

Approval is recorded as a conditional batch approval. It is not represented as
individual manual review of every question or every newly selected span.

## Additional evidence checks

- latest independent Claude Sonnet verdict: 40/40 clean;
- all ledger exact spans are verbatim in approved full chunks;
- 165 newly selected verbatim spans across 23 questions are retained with an
  explicit batch-approval register; and
- no candidate Test40 answer, candidate retrieved context, system identity, or
  Test40 result was used in reference construction or this reference check.

## L1.5 V1 diagnostic

The retained V1 diagnostic incorrectly rendered `constraint_groups` as gold
answer statements. It produced 209/217 passing claims and eight unsupported
absence/generalization constraints across seven questions. V2 corrected this
input-scope error prospectively for the freeze check; no scientific ledger
claim was deleted or edited in response. The V1 outputs remain outside this
frozen directory as transparent development history.

## Boundary

This freeze authorizes subsequent formal Test40 scoring under the unchanged
GPT-5.1 three-repeat L3 policy. Any later annotation correction requires a new
version; this release must not be overwritten.

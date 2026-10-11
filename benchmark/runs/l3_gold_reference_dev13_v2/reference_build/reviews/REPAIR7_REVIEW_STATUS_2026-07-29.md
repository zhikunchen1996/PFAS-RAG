# Repair7 review status

Date: 2026-07-29

Status: **Claude clean for 13/13; project-author approved 13/13; frozen**

## Scope

Repair5 responded to the candidate-blind pre-audit by exposing complete
original chunks where qualifiers were missing, adding already
project-author-audited L3-only evidence for `WF10_002`, and adding a
same-document identity chunk for `NQ24`. It did not modify frozen retrieval
gold or retrieval metrics.

Repair6 resolved the two blocking duplicate-weighting findings from the
repair5 Claude review:

- `NQ26-G04` was removed. Simple concentration routes remain scored in G02,
  membrane-assisted degradation remains described in G03, and the
  separation-versus-destruction prohibition remains a non-scored constraint.
- `WF10_002-G04` was removed. Its GAP endpoint-listing content was merged
  into G01 instead of being scored twice.
- The stale `WF10_002` statement that membrane evidence was absent was
  corrected after the L3-only evidence transfer.
- The inherited `WF10_002_L3X002` `supported_claim` was narrowed to the
  proposition directly entailed by its exact span.

Repair7 resolved the sole remaining repair6 blocker:

- `WF10_002-G06` no longer requires exact reporting of 425 and 450 C for
  full credit. Those temperatures remain an illustrative source detail,
  while scoring tests the endpoint distinction and uncertainty about
  incomplete fluorine mass-balance closure.

## Independent review results

Repair5 (`claude-sonnet-5`, medium effort):

- 3 clean reviews reused from repair4
- 10 new calls
- 11/13 clean
- blocking questions: `NQ26`, `WF10_002`
- new-call latency sum: 806.68 s
- reported new-call cost: USD 3.5685545

Repair6 (`claude-sonnet-5`, medium effort):

- 11 clean reviews reused from repair5
- 2 new calls
- 12/13 clean
- blocking question: `WF10_002`
- new-call latency sum: 217.47 s
- reported new-call cost: USD 0.6844224

Repair7:

- 12 clean reviews were hash-reused from repair6.
- The one changed ledger, `WF10_002`, was independently re-reviewed through
  the Anthropic API after the account was funded.
- Final result: 13/13 approve and clean, with no unsupported group,
  duplicate/weighting issue, prose issue, omitted major gold finding, or
  unresolved prior claim.
- New-call latency: 106.94 s
- New-call reported cost: USD 0.435783
- Final review SHA-256:
  `2517aaa592e4b5ca7b00bdf8e3a9b2e20e006a35299938b21e7244a634bc6450`

Two pre-inference attempts were rejected before the successful call:
subscription access had reached a session limit and the API account initially
reported insufficient credit. Those failed attempts used zero model tokens
and are not counted as review calls.

## Author-review boundary

No `project_author` decision or checklist field has been written. In
particular, the project author still needs to confirm:

- the same-document `NQ24_L3CTX001` identity context;
- the three already audited but newly transferred L3-only records used by
  `WF10_002`;
- the documented elevation of `WF10_002_MMG002` from optional gold to support
  a core mineralization distinction; and
- the final wording and scoring rules for all 13 ledgers.

The earlier `human_review_v2` packet remains a repair4 historical checkpoint.
The current repair7 author-audit packet is:

```text
human_review_repair7/reference_candidates.jsonl
human_review_repair7/decision_register.csv
human_review_repair7/HUMAN_AUDIT_PACKET.md
human_review_repair7/build_manifest.json
```

The project author explicitly approved all 13 ledgers on 2026-07-29 before
candidate answers or L3 scores were viewed. All 65 author-check fields are
true. The normative frozen reference is
`frozen/reference_claim_ledgers_v2.jsonl` with SHA-256
`0ad2bbfae02c30433ab030c36ad2e95d1278d029f3378d7111e1df63e18c413a`.

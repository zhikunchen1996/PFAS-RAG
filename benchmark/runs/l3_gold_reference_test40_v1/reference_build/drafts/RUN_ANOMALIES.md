# Draft-run anomalies

## 2026-07-29 NQ01 smoke attempt

The first NQ01 GPT-5.1 low-reasoning smoke call used a 12,000-token completion
ceiling and returned `finish_reason=length`. The response was not parsed,
validated, retained, or used in any ledger. The ceiling was increased to
20,000 tokens, matching the completed Dev13 structured-ledger revision stage.
The prompt, evidence inputs, reasoning effort, and validation rules were not
changed. The failed call's unrecorded token cost is excluded from analytical
cost totals.

## 2026-07-29 NQ01 schema-invalid smoke attempt

The next NQ01 call completed but placed a nonempty numeric-equivalence value on
a group marked `numeric_required=false`. Strict validation rejected the draft,
and it was not retained or used. The prompt was clarified to require `[]` for
all nonnumeric groups. Subsequent schema-invalid responses are stored in a
quarantine directory with generation provenance before being rejected.

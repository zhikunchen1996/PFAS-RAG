# Dev13 L3 Step 3 sealed run record

Status: **canonical and reverse-order scoring complete; results sealed pending
blinded human adequacy labels**

The run contains two matched GPT-5.1 answer sets and 13 questions per set.
System-level scores and question-level judge outcomes must not be inspected by
anyone who will provide the Dev adequacy labels used for threshold
calibration.

## Frozen inputs

- Reference claims:
  `benchmark/runs/l3_gold_reference_dev13_v2/frozen/reference_claim_ledgers_v2.jsonl`
- Reference SHA-256:
  `0ad2bbfae02c30433ab030c36ad2e95d1278d029f3378d7111e1df63e18c413a`
- Judge prompt SHA-256:
  `bc33bf90694e94759dcd39e88bb454162e4f740616c55204b4b2bef7abfa8341`
- Judge model: `gpt-4.1-2025-04-14`
- Temperature: `0`
- Binary threshold: not calibrated
- Test40 L3 run: no

## Execution

- Canonical order: 26/26 completed
- Reverse order: 26/26 completed
- Total judge calls: 52
- Total tokens: 504,581
- Estimated total cost: USD 1.419376
- Sum of per-call latency: 1,337.79 s

## Order-sensitivity diagnostic

This pooled diagnostic does not disclose system performance:

- exact core-score agreement: 9/26 (34.6%)
- mean absolute core-score difference: 0.1191
- maximum absolute core-score difference: 0.4167
- claim-status disagreements: 49
- constraint-status disagreements: 0
- boundary-flag disagreements: 0
- reference-error-flag disagreements: 2

The canonical order remains the predeclared primary result. Reverse order is a
sensitivity analysis and cannot replace the primary result selectively.
Threshold calibration must wait for blinded human adequacy labels and must
report sensitivity to both judge orders.

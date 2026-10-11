# Professional Review Formal V1 Results

Date: 2026-08-04  
Status: complete and independently validated

## Design

- Tasks: RT01--RT10
- Systems: BGE-LLM local RAG, GPT-5.1 Web Search, and GPT-5.1 Direct
- Defining-review exclusion: applied before local and Web retrieval
- Generation pipeline: source discovery, structured extraction, record-level
  verification, professional-review synthesis, source-support review for the
  two retrieval-enabled systems, and one calibrated GPT-5.1 Layer B judgment
  per answer
- Primary Layer B metric: component-balanced weighted review quality

## Primary results

| System | Mean quality | SD across 10 tasks | Min--max | Mean delta vs Direct |
|---|---:|---:|---:|---:|
| BGE-LLM local RAG | 0.985 | 0.026 | 0.938--1.000 | +0.123 |
| GPT-5.1 Web Search | 0.957 | 0.051 | 0.833--1.000 | +0.096 |
| GPT-5.1 Direct | 0.861 | 0.036 | 0.802--0.913 | reference |

Task-level comparisons were 10 wins, 0 ties, and 0 losses for BGE-LLM versus
Direct; 9/0/1 for Web Search versus Direct; and 6/2/2 for BGE-LLM versus Web
Search. These counts are descriptive comparisons of independently scored
answers, not a separate pairwise-judge metric.

RT01 was used during method development. Excluding RT01 gave means (task SD)
of 0.986 (0.027) for BGE-LLM, 0.959 (0.053) for Web Search, and 0.866 (0.035)
for Direct. The ordering and interpretation therefore did not depend on RT01.

The protocol used one judge call per formal answer after the prospective
RT02/RT09 stability calibration passed. Consequently, the zero
`review_quality_repeat_sample_sd` values in the machine summary only reflect
the single-repeat design and must not be presented as uncertainty. The SDs in
the table above are sample SDs across the ten task-level scores.

The ten tasks are a small, deliberately focused benchmark and were derived
from five anchor reviews. Tasks sharing an anchor may therefore share topical
and evidence-pool structure and should not be treated as statistically
independent replicates. The reported task SD is descriptive across-task
dispersion, not a confidence interval, and the experiment was not powered for
formal significance testing.

## Evidence diagnostics

| Metric | BGE-LLM | Web Search | Direct |
|---|---:|---:|---:|
| Mean verified usable records | 30.6 | 16.3 | 0 by design |
| Mean verified unique sources | 13.8 | 10.3 | 0 by design |
| Weighted extracted-field support | 0.956 | 0.926 | N/A |
| Numeric transcription accuracy | 0.977 | 0.946 | N/A |
| Endpoint classification accuracy | 0.945 | 0.936 | N/A |
| Weighted final-claim source support | 0.941 | 0.884 | N/A |
| Claim citation coverage | 0.989 | 0.977 | N/A |
| Mean unique cited sources | 13.7 | 10.2 | 0 |
| Peer-reviewed primary fraction among cited sources | 1.000 | 0.814 | N/A |
| Anchor-review exclusion violations | 0 | 0 | 0 |

Direct has N/A rather than zero for denominator-based evidence-accuracy
metrics because it received no retrieval or post-hoc source acquisition.
Layer B scores were near the upper boundary for both retrieval-enabled systems,
so small differences between BGE-LLM and Web Search should be interpreted with
the evidence diagnostics rather than as a finely resolved quality ranking.

## Cost and execution

| System | Paid calls | Tracked tokens | Canonical cost (USD) | Cost/task (USD) |
|---|---:|---:|---:|---:|
| BGE-LLM local RAG | 519 | 8,790,269 | 29.556 | 2.956 |
| GPT-5.1 Web Search | 322 | 3,452,007 | 14.056 | 1.406 |
| GPT-5.1 Direct | 20 | 196,429 | 1.174 | 0.117 |
| Total | 861 | 12,438,705 | 44.786 | 4.479 |

The canonical total excludes one superseded RT07 Web synthesis/support/judge
chain whose answer used invalid source aliases. That preserved chain cost
USD 0.338845. Estimated billed formal-execution cost including it was therefore
USD 45.124646, within the prospective USD 44--50 estimate. Web Search made 133
tool calls. API latency is additive across concurrent calls and must not be
reported as wall-clock runtime.

## Execution repairs

Three traceable execution-data repairs were needed without altering a frozen
retrieval rank, selected-source set, prompt, task, metric, or judge rule:

1. RT03 and RT08 selector responses placed retained sources in both selected
   and excluded sets. The selected set was authoritative and the duplicate
   exclusions were removed. RT08 also omitted non-target HALT source D20 from
   the exclusion list; it was added consistently with the response rationale.
2. RT04 Web Search returned the `.pdf` variant of a Nature URL while API
   consulted-source metadata used the canonical article URL. The result URL
   was normalized to the exact consulted URL.
3. The first RT07 Web synthesis used inconsistent `S##` aliases. It was
   preserved under `superseded/`, regenerated from the unchanged verified
   records and prompt, and the replacement source-support and judge calls were
   run. The final run then passed the independent validator.

Full details and request hashes are in `EXECUTION_REPAIR_LOG.md`.

## Integrity

- Run validator: PASS
- Package freeze-manifest SHA-256:
  `468bcd00bfa85ea9d375e59f2d2b1beae4d40160a188e44ecad177d53b67035a`
- Canonical `summary.json` SHA-256:
  `30c125e396e93e8e4164d5b01dfe90a5a6435f049e5490f35370ed7f7e079943`
- Canonical `system_summary.csv` SHA-256:
  `675c48ad129f5fde4f3b4e7741ea3519eb1796e3e2119090cefa1e5b4ad00b70`
- Canonical task-score CSV SHA-256:
  `da54bd4593960db8d738e78aab0a1e127bef2d264df0cf5fd07c56357722ebba`

These Section 3.4 results must not be used to revise the frozen Sections
3.1--3.3 experiments or to tune the Section 3.4 tasks, prompts, metrics, or
systems after seeing the outcomes.

RT02 and RT09 answers from an earlier pilot were used prospectively to confirm
judge stability before formal scoring. The Layer B prompt, rubric, scoring
code, and one-call formal repeat policy were fixed after that calibration and
were not revised after formal outcomes were observed. Accordingly, RT02 and
RT09 are not independent judge-validation tasks, although their formal
candidate answers were newly generated under the frozen experiment.

The observed differences describe the complete frozen system configurations.
They do not isolate full-text access, retrieval method, evidence budget, or
verification as a single causal mechanism. In particular, Layer A measures
verified evidence yield and support within the acquired source packets; it is
not an estimate of recall over all relevant literature.

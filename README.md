# PFAS RAG

This repository contains the experimental implementation, benchmark
questions and gold records, prompts, corpus metadata, stored model outputs,
evaluation code, and reported result tables for the PFAS RAG study.

The current release replaces literature passages with source-text hashes and
retains source identifiers and DOI metadata. Stored answers and audit notes
are public projections where embedded source quotations have been omitted.
Scores, retrieval ranks and question membership are unchanged. See
[the source-data guide](reproduction/public_sources_v01/README.md).

The release tree excludes manuscript and supplementary-information documents, submission
files, figure-only scripts and images, original expert assessment packets,
private writing records, credentials, and local databases. Development history
is retained privately and is outside the submission snapshot's file inventory.
Statistical analysis modules are retained when they also contain plotting
functions, but the supplied reproduction entry point does not call those
functions. No code license has been added.

## Environment

Use Python 3.12.13. `requirements.txt` records the direct dependencies;
`requirements-lock.txt` records the macOS ARM64 environment snapshot.

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/check_python_environment.py
.venv/bin/python scripts/verify_experiment_release.py
.venv/bin/python scripts/verify_public_source_projection.py
.venv/bin/python reproduction/experiments_v01/validate_results.py
.venv/bin/python reproduction/experiments_v01/aggregate_expert_scores.py
.venv/bin/python -m unittest discover -s reproduction/experiments_v01/tests -v
```

The inventory check verifies included files, not scientific correctness.
Publisher PDFs and a generated vector database are not supplied. Rebuilding
the corpus requires lawfully obtained source documents. Model execution
requires local credentials and access to the recorded provider models.

## Experiment Map

| Location | Contents |
| --- | --- |
| `benchmark/frozen_v3/` | Frozen questions, gold, prompts, retrieval and citation-support methods |
| `benchmark/runs/test40_formal_v1_1/` | Hybrid/BGE/BGE-LLM stored test results and execution code |
| `benchmark/runs/test40_multibase_direct_rag_v1/` | Matched Direct/PFAS RAG comparison |
| `benchmark/runs/test40_multibase_l15_v1/` | Cross-model citation-support analysis |
| `benchmark/runs/l3_gold_reference_test40_v1/` | Candidate-blind reference ledgers |
| `benchmark/review_tasks/professional_review_v3_formal_v1/` | Professional-review tasks and method |
| `benchmark/review_tasks/runs/` | Stored professional-review results and expert aggregates |
| `benchmark/ablations/` | Statistical analyses and result tables |
| `corpus/corpus434_repaired_v1/` | Corpus metadata and repair records |
| `src/rag_app/` | Exact implementation recorded by the formal experiment |
| `reproduction/experiments_v01/` | Analysis-only entry point, anonymized expert scores, and independent checks |

Additional development packages preserve experimental dependencies and
reference-building provenance. They are not additional test sets. Scientific
evidence-audit records are distinct from private manuscript-writing records.

## Reproducing the Analyses

```bash
.venv/bin/python reproduction/experiments_v01/run_analysis.py \
  --output outputs/recomputed_statistics
```

This recomputes the supplementary statistics without generating figures or
overwriting the frozen results and compares the regenerated tables with the
reported results. See [the reproduction guide](reproduction/experiments_v01/README.md)
for the experiment/source mapping, expert-score schema, and re-execution steps.

The current tree is a public projection, not a new experiment freeze.
`release_manifest.json` verifies the distributed files; the source-projection
manifest records the original and projected hashes of changed files. Historical
freeze manifests describe the original experimental records, not the projected
copies at those paths. Original prompts, executable experiment code, result
tables and expert scores are retained. Use the scoped verification and analysis
commands above. Re-running source-dependent generation or judging requires
restoring the original evidence from lawfully obtained documents; omitted-text
markers must not be used as model inputs. Earlier Git commits were not rewritten.

# Experiment Reproduction

The release maps the seven original `rag_app` files recorded in
`benchmark/runs/test40_formal_v1_1/pre_run_manifest.json` to `src/rag_app/`.
`formal_source_manifest.json` records the source commit and original hashes.
This is the experimental implementation, not the newer local application.
Its standalone CLI defaults are not the complete formal PFAS RAG pipeline;
use the frozen benchmark configurations and execution stages.

## Stored Results

From the repository root:

```bash
.venv/bin/python scripts/verify_experiment_release.py
.venv/bin/python scripts/verify_public_source_projection.py
.venv/bin/python reproduction/experiments_v01/validate_results.py
.venv/bin/python reproduction/experiments_v01/aggregate_expert_scores.py
.venv/bin/python -m unittest discover -s reproduction/experiments_v01/tests -v
```

The expert tables contain 30 pairwise judgments and 60 candidate ratings from
three anonymous raters across ten tasks. Rater labels are arbitrary IDs, not
names. `expert_pairwise_records.csv` preserves preferences and explicit Y/N
material-error flags; `expert_dimension_records.csv` preserves the six numeric
ratings. Free-text comments and document metadata are excluded. The
aggregation script checks the study design and reproduces every reported
expert aggregate from these records.

## Supplementary Statistics

```bash
.venv/bin/python reproduction/experiments_v01/run_analysis.py \
  --output outputs/recomputed_statistics
```

This entry point calls the existing statistical functions, not the original
script entry points. It writes only to a new directory under `outputs/`,
generates no figures, makes no model calls, and compares all regenerated CSV
tables with their frozen counterparts. Existing output directories are refused.
The original combined analysis modules remain unchanged because they are
method provenance; their figure functions are not called. Do not run their
legacy `main` entry points against the frozen results.

## Model Re-execution

The stage order, prompts, schemas, model snapshots, and request manifests are
in each experiment package. The public inventory and stored numeric results can
be checked without API credentials. Source passages and embedded quotations
have been replaced by hashes in the public records; these are not complete
inputs for another model run. Restore original evidence in a separate working
copy before source-dependent generation or judging. Fresh execution requires
provider access and may vary with hosted model availability.

Rebuilding retrieval additionally requires the recorded Chroma collection and
lawfully obtained source documents. The release does not supply publisher
PDFs or a vector database. The original ingestion code uses historical
source-path-derived chunk IDs; do not substitute a rebuilt corpus with new IDs
for the frozen benchmark contexts. The retained document IDs, chunk IDs and
ranks support retrieval-metric recomputation without the passage text. The
source-projection manifest preserves original record hashes separately from
the hashes of the distributed files.

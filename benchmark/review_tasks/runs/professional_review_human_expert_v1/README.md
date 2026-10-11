# Blinded Expert Assessment

This package contains the completed, deidentified human assessment used as a
validation analysis for the ten professional-review tasks. Three experts each
evaluated all ten tasks. Within every task, the three system pairs were
distributed across experts so that each pair was judged once and each system
appeared 20 times across the 30 comparisons.

The experts received anonymous candidate IDs and evaluated six review-quality
dimensions on a 1-5 scale, a pairwise overall preference, and material
scientific-error flags. The system mapping was not visible in the scoring
packets. The retained inputs are the completed packets, not model-generated
judgments.

`summary.json` contains the deterministic aggregate used for Figure 5:

- PFAS RAG versus Direct: 10/10 PFAS RAG preferences;
- Web Search versus Direct: 10/10 Web Search preferences; and
- PFAS RAG versus Web Search: 4 PFAS RAG, 2 ties, and 4 Web Search.

The summary is rebuilt by
`scripts/manuscript/build_figure5_with_expert_assessment.py`. Validate package
integrity and the expected design counts with:

```bash
.venv/bin/python \
  benchmark/review_tasks/runs/professional_review_human_expert_v1/scripts/validate_package.py
```

The repository records deidentified scores only. Recruitment, compensation,
conflict-of-interest, and institutional ethics statements are manuscript-level
author disclosures and are not inferred from the score files.

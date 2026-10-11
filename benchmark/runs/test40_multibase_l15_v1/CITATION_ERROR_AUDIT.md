# Citation-Error Audit

This audit classifies the 23 cited claims that did not pass the frozen lenient
L1.5 rule. `partially_supported` claims are not included because the frozen
metric treats them as passing.

## Label distribution

| RAG base model | Supported | Partially supported | Not supported | Contradicted | Total cited claims |
|---|---:|---:|---:|---:|---:|
| GPT-5.1 | 664 | 161 | 4 | 0 | 829 |
| Gemini 3.1 Pro Preview | 253 | 63 | 5 | 0 | 321 |
| Claude Sonnet 5 | 341 | 110 | 11 | 3 | 465 |

The fully supported-only fractions were 0.801, 0.788, and 0.733,
respectively. These are transparent secondary diagnostics derived from the
frozen labels, not replacements for the prespecified lenient L1.5 metric.

## Failure categories

| Category | Count | Interpretation |
|---|---:|---|
| Corpus-level or absence-based generalization | 14 | The answer inferred that a practice was common, unique, underreported, insufficiently validated, or absent across studies, although the cited chunks described only individual studies or did not explicitly establish that literature-level conclusion. |
| Wrong or incomplete citation attachment | 4 | The cited chunk was related to the topic but did not support the stated compound, material, treatment, or methodological detail; in one case another available chunk was the appropriate source. |
| Unsupported magnitude or boundary | 2 | The source documented that a condition was studied but did not establish the claimed performance magnitude or stated cycle boundary. |
| Direct numerical, endpoint, or categorical contradiction | 3 | The answer conflicted with an explicit source value or category. |

## Direct contradictions

1. `claude_sonnet5_rag::NQ22` reported PFOS defluorination up to 80.4%, but
   the source reported defluorination up to 70.0%; 80.4% referred to PFOS
   degradation, not defluorination.
2. `claude_sonnet5_rag::WF10_010` stated that phosphate significantly
   inhibited PFOA degradation, whereas the cited source reported that
   phosphate had little effect.
3. `claude_sonnet5_rag::WF10_032` stated that all sources were limited to two
   to four cycles, while one cited source reported four to five cycles.

## Representative unsupported citations

- `gemini31_pro_rag::WF10_034` attached adsorption chunks to an
  electrochemical destruction and Cr(VI)-reduction recommendation; the
  electrochemical evidence was present in a different chunk.
- `claude_sonnet5_rag::WF10_017` cited a chunk about salt-organic-solvent
  regeneration and iodide counterions for a broader claim about a
  field-demonstrated electrochemical-oxidation/ion-exchange system.
- `gemini31_pro_rag::NQ16` converted a reported 1-30 minute kinetic study
  interval into a claim that substantial removal occurred within that interval.
- `claude_sonnet5_rag::NQ02` stated that only one study reported duplicate
  precision and only one described confirmation criteria. The cited chunks
  supported the individual study practices but could not establish uniqueness
  across the literature.
- `gpt51_rag::NQ22` inferred that many photocatalytic studies omitted TOC or
  fluoride endpoints from a chunk that only stated that degradation
  efficiencies were summarized.

## Interpretation

Most failures were overextension of evidentiary scope rather than random
citation-number errors. In particular, a finite retrieved packet cannot by
itself support universal statements such as "only one study," "many studies
omit," or "field validation is limited" unless the source explicitly makes
that literature-level synthesis. The three contradicted Claude claims are
more consequential because they involve endpoint, quantitative, or categorical
misreading of evidence.

For manuscript comparison, mean question-level support is the preferable main
L1.5 descriptor because each question has equal weight. The pooled supported
cited-claim rate is retained as a micro-average describing all claims produced,
but it is influenced by model-specific answer length and claim granularity.


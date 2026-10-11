# Claude task-component review request

Review `component_review_packet.jsonl` as a candidate-blind scientific task
decomposition audit.

For each of the 40 questions, check whether the task components:

1. collectively cover the visible question and `must_include` boundary;
2. respect `must_not_claim`;
3. are non-overlapping enough to avoid duplicate scoring weight;
4. contain only information needs, not inferred scientific answers;
5. introduce no compounds, matrices, methods, examples, study goals, values,
   or conclusions absent from the visible question and boundaries; and
6. remain usable for a general researcher-facing answer.

Do not inspect candidate Test40 answers, retrieved contexts, system labels, or
Test40 results. Return `CLEAN` only if all 40 are acceptable. Otherwise return
`ISSUES` followed by one concise line per affected question in the format:

`QUESTION_ID | severity | problem | exact replacement component set`

The replacement set must preserve sequential component IDs and use 1-4
components.

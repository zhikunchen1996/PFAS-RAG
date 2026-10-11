# Dev13 L3 GPT-5.1 Aggregation Policy Freeze

Freeze date: 2026-07-29

This package fixes the prospective GPT-5.1 L3 canonical scoring aggregation
policy developed on Dev13. The policy was reviewed independently by Claude
Sonnet and passed the package validator after all results were completed.

This is a package-level methodological freeze, not a Test40 performance
result. The Test40 set remains untouched by L3 candidate scoring. The package
must not be modified in place; any change to the prompt, ledger, model,
reasoning effort, aggregation, or validation logic requires a new versioned
successor.

Repository-level immutable release commit and annotated tag remain a separate
git action so unrelated worktree changes are not staged incidentally.

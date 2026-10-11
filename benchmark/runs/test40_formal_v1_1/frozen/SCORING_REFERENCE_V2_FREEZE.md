# Test40 scoring reference V2 freeze

Date: 2026-07-29

This is a candidate-blind scoring-compatible successor to the frozen Test40
reference release. The original release remains unchanged.

- Source ledger SHA-256: `7a805a79a72333d21fd381fc43498ffc9ebe2ea6c367f1afe0b1528cafc50b76`
- Scoring ledger SHA-256: `e0e88dc3b6b2e82a2b6dd4afde3d71fda779693af8ffd4c3a913b7c427ab27f5`
- Candidate Test40 answers used: no
- Candidate Test40 retrieved contexts used: no
- System identities used: no
- Questions, gold chunks, task components, and reference answers changed: no
- Existing supplementary groups promoted to required core: 2
- Existing audited content mapped to new required core groups: 8

The successor fixes a structural incompatibility between the Test40 reference
ledger and component-balanced L3 scoring: ten task components previously had
no `core` + `required_content` claim. Evidence-limitation groups are explicitly
limited to the frozen reference packet and must not be interpreted as claims
that no relevant evidence exists outside that packet.

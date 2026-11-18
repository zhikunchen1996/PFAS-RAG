# L3 Dev13 V2 project-author audit

Status: **project-author approved 13/13; ready for reference freeze**

The claim ledger is normative for scoring. The prose answer is
non-normative. Review every task component and every claim group,
including groups not flagged by Model B.

Record decisions in `reference_candidates.jsonl`. Approval requires
all five `project_author_checks` to be true, `human_review.decision`
to be `approve`, a review date, and resolution notes. Any edit to an
approved ledger requires a new Model B verification before freeze.

## NQ10

**Question:** How are PFAS samples preconcentrated before mass spectrometry, and how do protocols vary by matrix, analyte, or method?

**Must include:** Must connect SPE selection to matrix and analyte scope; must mention recovery or chemistry-dependent suitability when supported.

**Must not claim:** Must not claim one exact SPE cartridge and elution protocol is universally correct for all PFAS environmental samples.

### Frozen task components

- `NQ10-T01`: Describe the preconcentration or sample-preparation approaches used before mass spectrometry.
- `NQ10-T02`: Explain how method choice and performance vary with matrix, analyte scope, or analytical workflow.

### Complete gold evidence

**NQ10_MMG001** (required_gold; `2021 - Olomukoro - Ion exchange solid phase microextraction coupled to liquid chromatography - laminar flow tandem mass spectrometry for the determination of.pdf`, chunk `36`)
> [SOURCE_TEXT_OMITTED sha256=469013d9469e2f088c33eba45896cb806c245ec2eb3f3e7be1c475ef589ac4ad].

**NQ10_MMG002** (required_gold; `2021 - Olomukoro - Ion exchange solid phase microextraction coupled to liquid chromatography - laminar flow tandem mass spectrometry for the determination of.pdf`, chunk `34`)
> [SOURCE_TEXT_OMITTED sha256=c378a9b6ac19269490bb0291bfbb3dccb3131b3fd5063898f6b886c43b97d7c6]

**NQ10_MMG003** (required_gold; `2021 - Olomukoro - Ion exchange solid phase microextraction coupled to liquid chromatography - laminar flow tandem mass spectrometry for the determination of.pdf`, chunk `6`)
> [SOURCE_TEXT_OMITTED sha256=03fa6037597d41bc4c6c5a8cea348634f2cae2ecfc43471a313752c65ceedc98] ].

**NQ10_MMG004** (optional_gold; `2022 - Pellicer-Castell - Iron-Doped Bimodal Mesoporous Silica Nanomaterials as Sorbents for Solid-Phase Extraction of Perfluoroalkyl Substances in Environmental.pdf`, chunk `42`)
> [SOURCE_TEXT_OMITTED sha256=87c68bb46c27be15a4694fda8735b811754ab515a80f0e9570fcd2ac0933ea18].

**NQ10_MMG005** (optional_gold; `2022 - Pellicer-Castell - Iron-Doped Bimodal Mesoporous Silica Nanomaterials as Sorbents for Solid-Phase Extraction of Perfluoroalkyl Substances in Environmental.pdf`, chunk `43`)
> ([SOURCE_TEXT_OMITTED sha256=4b0660a78efdf23a909ff5eb1ca11842ea6a8a985d897643c04897a0ad32694d].

**NQ10_MMG006** (optional_gold; `2022 - Croll - Adaptation of selected models for describing competitive per- and polyfluoroalkyl substances breakthrough curves in groundwater treated by granular.pdf`, chunk `12`)
> [SOURCE_TEXT_OMITTED sha256=32c6b524ae782f897b8c7ddfc2092da8ed5aaa55192906ba9a33d637b5e79a99].

**NQ10_MMG007** (optional_gold; `2024 - Habib - Green Analytical Method for Perfluorocarboxylic Acids (PFCAs) in Water of Stir Bar Sorptive Extraction Coupled with Thermal Desorption-Gas.pdf`, chunk `11`)
> [SOURCE_TEXT_OMITTED sha256=917d5b0ac27ef7fa00857760f8dbb7504e7a61f4c76da6fccc304f6a4ad1261f]

**NQ10_MMG008** (optional_gold; `2023 - Hao - Hydrothermal Alkaline Treatment (HALT) of Foam Fractionation Concentrate Derived from PFAS-Contaminated Groundwater.pdf`, chunk `9`)
> [SOURCE_TEXT_OMITTED sha256=22dde9e759cfb91bc92ed1d4758c0cde151d84863914426a035f338b3d829c32].

**NQ10_MMG009** (optional_gold; `2021 - Olomukoro - Ion exchange solid phase microextraction coupled to liquid chromatography - laminar flow tandem mass spectrometry for the determination of.pdf`, chunk `32`)
> ([SOURCE_TEXT_OMITTED sha256=eb2b3a25a3ca555a7aeb56e38dec7ecde3bb82dc8d89ed8dede61b7eaff3f191] .

**NQ10_MMG010** (negative_gold; `2021 - Olomukoro - Ion exchange solid phase microextraction coupled to liquid chromatography - laminar flow tandem mass spectrometry for the determination of.pdf`, chunk `7`)
> [SOURCE_TEXT_OMITTED sha256=bf770acb02a6cde476a8c0a120becd99a5b99de54d2c809bc12dd35556192b5b].

### Normative content claim groups

#### NQ10-G01

- Component: `NQ10-T01`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: For parts-per-trillion level PFAS determinations, sample preconcentration has been accomplished using solid phase extraction (SPE) or liquid–liquid extraction (LLE) prior to analysis.
- Material qualifiers: ["applies to PFAS at parts-per-trillion levels", "refers generally to preconcentration before analysis, without specifying matrix"]
- Evidence: NQ10_MMG003
- Prior atomic claims: NQ10-C01
- Full: Award full if the answer states that for parts-per-trillion-level PFAS, preconcentration has been done using solid phase extraction or liquid–liquid extraction (both methods mentioned) in a general sense prior to analysis.
- Partial: Award partial if the answer correctly mentions at least one of SPE or LLE as used for preconcentrating parts-per-trillion-level PFAS, but omits the other method or the parts-per-trillion qualifier, without asserting an incompatible method as the sole approach.
- Contradiction: Mark contradicted if the answer explicitly denies that SPE or LLE have been used for parts-per-trillion-level PFAS preconcentration, or asserts that a completely different technique is the only method used for such determinations.

#### NQ10-G02

- Component: `NQ10-T01`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: A solid phase microextraction ([SOURCE_TEXT_OMITTED sha256=215fa32bd6b0d5a2e94405abaddfd952894bb801a8fc03de3770271411b1dc1e] as the sample-preparation step before analysis.
- Material qualifiers: ["SPME used as sample-preparation / extraction", "applies to aqueous matrices including river, lake, tap, and bottled water"]
- Evidence: NQ10_MMG001
- Prior atomic claims: NQ10-C05
- Full: Award full if the answer describes an SPME-based method developed for PFAS and explicitly notes its application to aqueous samples including river, lake, tap, and bottled water.
- Partial: Award partial if the answer mentions SPME for PFAS in aqueous matrices but omits some of the specific water types, or only lists some (e.g., mentions drinking water but not all four), without contradicting the aqueous scope.
- Contradiction: Mark contradicted if the answer claims that SPME was not developed for PFAS aqueous analysis or misrepresents it as being applied to non-aqueous matrices only.

#### NQ10-G03

- Component: `NQ10-T01`
- Importance: `supplementary`
- Function: `affirmative`
- Scoring role: `optional_content`
- Proposition: A method integrating stir bar sorptive extraction (SBSE) with thermal desorption–gas chromatography–mass spectrometry (TD–GC–MS) was developed and validated for analysis of perfluorocarboxylic acids (PFCAs) in water, with SBSE serving as the preconcentration step.
- Material qualifiers: ["PFCAs are a subgroup of PFAS", "SBSE is used as the extraction/preconcentration step", "matrix is water"]
- Evidence: NQ10_MMG007
- Prior atomic claims: NQ10-C10
- Full: Award full if the answer mentions a PFAS-related method using stir bar sorptive extraction coupled with thermal desorption–GC–MS for perfluorocarboxylic acids in water, identifying SBSE as the preconcentration or extraction step.
- Partial: Award partial if the answer mentions SBSE with TD–GC–MS for PFAS/PFCAs in water but omits that the method was developed and validated, or does not explicitly call SBSE the preconcentration step.
- Contradiction: Mark contradicted if the answer claims that SBSE with TD–GC–MS was not used for PFCAs in water or misassigns this method to a different matrix or non-PFCA analytes.

#### NQ10-G04

- Component: `NQ10-T01`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: Some PFAS analytical workflows use dilution-based preparation rather than a separately described extraction step: EPA Method 8327 uses dilute-and-shoot for drinking water, while the cited foam-concentrate excerpt describes dilution and reagent mixing before HPLC injection without explicitly describing SPE or LLE.
- Material qualifiers: ["EPA Method 8327 is a drinking-water dilute-and-shoot workflow covering 24 PFAS compounds.", "The foam-concentrate excerpt directly reports dilution, reagent mixing, and HPLC injection; absence of a separate extraction step is limited to what that excerpt describes."]
- Evidence: NQ10_MMG002, NQ10_MMG008
- Prior atomic claims: NQ10-C08, NQ10-C09, NQ10-C14
- Full: Award full if the answer identifies both the EPA Method 8327 dilute-and-shoot example and the foam-concentrate dilution/reagent-mixing example, while framing the latter only as having no separate extraction step described in the cited excerpt. A complete reagent inventory is not required.
- Partial: Award partial if the answer correctly describes one of the two dilution-based examples or describes both but omits the excerpt-limited hedge for the foam-concentrate workflow.
- Contradiction: Mark contradicted if the answer says EPA Method 8327 requires SPE/LLE or claims that the foam-concentrate excerpt explicitly proves no extraction occurred anywhere in the full workflow.

#### NQ10-G05

- Component: `NQ10-T01`
- Importance: `supplementary`
- Function: `affirmative`
- Scoring role: `optional_content`
- Proposition: In one PFAS extraction workflow, elution into a 0.5 mL methanolic extract produced an effective 500-fold concentration of target analytes relative to the initial sample.
- Material qualifiers: ["eluted extract volume is 0.5 mL", "effective concentration factor is about 500-fold", "the exact span does not independently identify the source water matrix, so no groundwater qualifier is required"]
- Evidence: NQ10_MMG006
- Prior atomic claims: NQ10-C02
- Full: Award full if the answer reports both the 0.5 mL methanolic extract and the approximately 500-fold concentration factor without adding an unsupported matrix attribution.
- Partial: Award partial if the answer reports only one of the two numerical details or describes a large enrichment without both.
- Contradiction: Mark contradicted if the answer gives incompatible values or denies that the workflow produced substantial enrichment.

#### NQ10-G06

- Component: `NQ10-T01`
- Importance: `supplementary`
- Function: `affirmative`
- Scoring role: `optional_content`
- Proposition: When PFAS in water were extracted using 150 mg SPE cartridges, recoveries clearly decreased as the sample volume was increased from 10 to 100 mL, indicating a sample-volume dependence of extraction efficiency.
- Material qualifiers: ["matrix is water", "sorbent mass is 150 mg in the SPE cartridges", "comparison is between 10 mL and 100 mL sample volumes"]
- Evidence: NQ10_MMG004
- Prior atomic claims: NQ10-C03
- Full: Award full if the answer notes that for a water SPE method using 150 mg cartridges, increasing sample volume from 10 to 100 mL decreased recoveries, using numerically equivalent expressions for cartridge mass and volumes.
- Partial: Award partial if the answer states that recovery decreased with increasing sample volume for a PFAS water SPE method but omits either the cartridge mass or the specific volume range, without contradicting them.
- Contradiction: Mark contradicted if the answer claims that recoveries increased or remained unchanged when sample volume was increased from 10 to 100 mL in this 150 mg cartridge SPE setup.

#### NQ10-G07

- Component: `NQ10-T02`
- Importance: `supplementary`
- Function: `affirmative`
- Scoring role: `optional_content`
- Proposition: In one SPE protocol, C8–C14 PFAS showed extraction recoveries above 61% for all analytes and close to 100% for PFOS and PFNA, illustrating analyte-dependent performance within the same method.
- Material qualifiers: ["applies to C8–C14 PFAS", "PFOS and PFNA recoveries are close to 100%", "this is a single SPE protocol; matrix is not specified in the span"]
- Evidence: NQ10_MMG005
- Prior atomic claims: NQ10-C04
- Full: Award full if the answer states that, in a particular SPE method, C8–C14 PFAS had recoveries above 61% and that PFOS and PFNA were close to 100%, using numerically equivalent expressions.
- Partial: Award partial if the answer conveys that recoveries for C8–C14 PFAS in one SPE method were generally high and that PFOS/PFNA were among the highest, but does not mention the >61% threshold explicitly.
- Contradiction: Mark contradicted if the answer claims that in this cited SPE protocol, recoveries for C8–C14 PFAS were mostly below 61% or that PFOS/PFNA had particularly low recoveries.

#### NQ10-G08

- Component: `NQ10-T02`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: Compared with very fast sample-processing methods such as dilute-and-shoot, the SPME method for PFAS provided higher preconcentration and reduced the occurrence of matrix effects.
- Material qualifiers: ["comparison is to very fast methods like dilute-and-shoot", "endpoints are level of preconcentration and occurrence of matrix effects"]
- Evidence: NQ10_MMG009
- Prior atomic claims: NQ10-C06
- Full: Award full if the answer notes that an SPME-based PFAS method provides higher preconcentration and reduces matrix effects relative to dilute-and-shoot–type workflows.
- Partial: Award partial if the answer mentions either improved preconcentration or reduced matrix effects of SPME relative to dilute-and-shoot, but not both, without claiming the opposite for either endpoint.
- Contradiction: Mark contradicted if the answer claims that dilute-and-shoot provides higher preconcentration or fewer matrix effects than the SPME method in this comparison.

#### NQ10-G09

- Component: `NQ10-T02`
- Importance: `core`
- Function: `limitation`
- Scoring role: `required_content`
- Proposition: Substantial matrix effects in some PFAS analytical methods can make the method unsuitable and not robust for complex samples.
- Material qualifiers: ["applies to complex samples", "method affected is not named in the span"]
- Evidence: NQ10_MMG010
- Prior atomic claims: NQ10-C07
- Full: Award full if the answer explains that substantial matrix effects can render a PFAS analytical method unsuitable or not robust when dealing with complex samples.
- Partial: Award partial if the answer mentions substantial matrix effects as a problem in complex samples but does not explicitly connect this to method unsuitability or lack of robustness.
- Contradiction: Mark contradicted if the answer claims that substantial matrix effects do not impair suitability or robustness for complex samples, or asserts that matrix effects are negligible in complex matrices for such methods.


### Prior atomic-claim dispositions

#### NQ10-C01

- Prior claim: For parts-per-trillion level PFAS determinations, sample preconcentration has been accomplished using either solid phase extraction (SPE) or liquid–liquid extraction (LLE).
- Action: `mapped`
- Final target(s): NQ10-G01
- Rationale: Directly corresponds to the general statement that ppt-level PFAS have been preconcentrated using SPE or LLE.

#### NQ10-C02

- Prior claim: In a groundwater application, target PFAS were preconcentrated using weak anion exchange solid phase extraction, and elution to 0.5 mL of methanolic extract resulted in an effective 500-fold concentration of the analytes relative to the initial sampling.
- Action: `revised`
- Final target(s): NQ10-G05
- Rationale: Retained the span-supported details (0.5 mL methanolic extract and 500-fold concentration) while removing the unsupported attribution to specific SPE chemistry.

#### NQ10-C03

- Prior claim: When PFAS in water were extracted using 150 mg SPE cartridges, recoveries clearly decreased as the sample volume was increased from 10 mL to 100 mL.
- Action: `mapped`
- Final target(s): NQ10-G06
- Rationale: Matches the evidence that recoveries decreased when sample volume increased from 10 to 100 mL for 150 mg SPE cartridges in water.

#### NQ10-C04

- Prior claim: In one SPE protocol, C8–C14 PFAS showed extraction recoveries above 61% for all analytes and close to 100% for PFOS and PFNA, with enrichment factors between 121 and 212.
- Action: `revised`
- Final target(s): NQ10-G07
- Rationale: Kept the recovery figures for C8–C14 PFAS and PFOS/PFNA that appear in the exact span and removed enrichment-factor numbers that are only present in metadata.

#### NQ10-C05

- Prior claim: A solid phase microextraction ([SOURCE_TEXT_OMITTED sha256=215fa32bd6b0d5a2e94405abaddfd952894bb801a8fc03de3770271411b1dc1e].
- Action: `mapped`
- Final target(s): NQ10-G02
- Rationale: Fully supported by the SPME conclusion span; used as the SPME aqueous-matrix example.

#### NQ10-C06

- Prior claim: Compared with very fast sample-processing methods such as dilute-and-shoot, the SPME method provided higher preconcentration of PFAS and limited the occurrence of matrix effects.
- Action: `mapped`
- Final target(s): NQ10-G08
- Rationale: Directly describes the comparative performance of SPME versus dilute-and-shoot and is mapped to the corresponding variability-by-workflow claim.

#### NQ10-C07

- Prior claim: In some PFAS analytical methods, substantial matrix effects occurred during analysis, making the method not suitable and not robust for complex samples.
- Action: `mapped`
- Final target(s): NQ10-G09
- Rationale: Directly captures the limitation that substantial matrix effects can render a method unsuitable for complex samples.

#### NQ10-C08

- Prior claim: EPA Method 8327 for drinking water uses a dilute-and-shoot approach with no separate preconcentration step for 24 PFAS compounds.
- Action: `merged`
- Final target(s): NQ10-G04
- Rationale: Combined with C09 and C14 into a single synthesized claim about workflows that omit a distinct preconcentration step, while preserving the EPA 8327 dilute-and-shoot example.

#### NQ10-C09

- Prior claim: In analysis of PFAS in foam fractionation concentrate, [SOURCE_TEXT_OMITTED sha256=5b1224194a9ac936fc0d600a4995c5e37b7066a0c6357677e715c9e54cd3b411] HPLC injection, without employing solid-phase or liquid–liquid extraction for preconcentration.
- Action: `merged`
- Final target(s): NQ10-G04
- Rationale: Merged with C08 and C14 into the broader claim about dilution-based workflows, using the foam concentrate example framed strictly by its exact span.

#### NQ10-C10

- Prior claim: A method integrating stir bar sorptive extraction (SBSE) with thermal desorption–gas chromatography–mass spectrometry (TD-GC-MS) was developed and validated for analysis of perfluorocarboxylic acids (PFCAs) in water.
- Action: `mapped`
- Final target(s): NQ10-G03
- Rationale: Directly mapped to the SBSE + TD–GC–MS method for PFCAs in water.

#### NQ10-C11

- Prior claim: Across the reported examples, preconcentration and sample preparation strategies vary by matrix, with weak anion exchange SPE used for groundwater, SPME applied to river, lake, tap, and bottled waters, SBSE used for water samples containing PFCAs, and dilute-and-shoot or dilution-only approaches applied to drinking water and foam concentrate matrices.
- Action: `deleted`
- Final target(s): (deleted)
- Rationale: The synthesis that method choice varies by matrix is now covered in a more granular way by G02, G03, G04, G05, G08, and G09; retaining this as a separate group would duplicate scoring weight for the same underlying facts.

#### NQ10-C12

- Prior claim: Preconcentration performance and method suitability are analyte- and matrix-dependent, as shown by SPE recoveries above 61% and near 100% for some C8–C14 PFAS in one protocol, contrasted with reports that substantial matrix effects can render other methods unsuitable for complex samples.
- Action: `deleted`
- Final target(s): (deleted)
- Rationale: The original claim overinterpreted two separate studies as a single joint demonstration of analyte- and matrix-dependence. Its factual components are already covered more conservatively in G07 (analyte-dependent recovery) and G09 (matrix effects in complex samples), so the overgeneralized synthesis was removed.

#### NQ10-C13

- Prior claim: Reported preconcentration factors for SPE-based PFAS methods span at least from enrichment factors of 121–212 in one study to an effective 500-fold concentration in another groundwater application, indicating that achievable enrichment depends on the specific SPE protocol and matrix.
- Action: `deleted`
- Final target(s): (deleted)
- Rationale: The revised version of this claim was purely a synthesis restating span-supported facts already scored in G05 and G07 (500-fold concentration and high recoveries), so it was removed to avoid duplicate weighting of the same evidence.

#### NQ10-C14

- Prior claim: Some PFAS analytical workflows do not include a dedicated preconcentration step, instead relying on direct injection after dilution or simple solvent modification, as illustrated by dilute-and-shoot drinking water analysis and diluted foam concentrate prepared with added solvents and bases.
- Action: `merged`
- Final target(s): NQ10-G04
- Rationale: C14 restates the two dilution-based workflows already represented by C08 and C09; all three are merged into one claim group about methods that omit a dedicated preconcentration step.

### Constraint-only groups

- `NQ10-B01`: It must not be claimed that one exact SPE cartridge type and elution protocol is universally correct or optimal for all PFAS environmental samples and matrices.
  Violation rule: Flag a boundary violation if the answer asserts or clearly implies that a single specific SPE cartridge and elution protocol is universally applicable, universally optimal, or correct for all PFAS environmental samples or all matrices, without limitation.

### Model B verification

Overall verdict: **approve**

- `NQ10-G01`: **supported**. Canonical proposition and qualifiers reproduce the exact span verbatim in substance; SPE/LLE for ppt-level PFAS is directly entailed.
  Recommended change: None.
- `NQ10-G02`: **supported**. Directly entailed by the SPME conclusion span; matrix list (river, lake, tap, bottled water) matches exactly.
  Recommended change: None.
- `NQ10-G03`: **supported**. SBSE+TD-GC-MS for PFCAs in water is directly entailed by the expanded span; importance/scoring_role of supplementary/optional_content is a reasonable, non-core proportional weighting.
  Recommended change: None.
- `NQ10-G04`: **supported**. Both dilution-based examples are entailed by their exact spans. The foam-concentrate qualifier now correctly hedges that absence of a described extraction step is limited to what the excerpt describes, resolving the prior universalization concern (instruction #14). The partial_rule allows independent credit for either sub-fact, mitigating the merge of two independently verifiable facts from different papers.
  Recommended change: None required; optionally split into two groups for finer-grained scoring, but current partial_rule design is acceptable.
- `NQ10-G05`: **supported**. Revised to remove the 'weak anion exchange SPE' attribution flagged by the gold record's own does_not_support field as outside the quoted span; the 0.5 mL / 500-fold figures are directly entailed. This resolves the prior partially_supported finding on C02.
  Recommended change: None.
- `NQ10-G06`: **supported**. Matches the exact span verbatim; numeric equivalents are reasonable and claim-specific.
  Recommended change: None.
- `NQ10-G07`: **supported**. Revised to drop the EF 121-212 figure absent from the exact span, retaining only the >61% and ~100% recovery figures that are directly present. Resolves the prior partially_supported finding on C04.
  Recommended change: None.
- `NQ10-G08`: **supported**. Directly entailed by the exact span comparing SPME to dilute-and-shoot for preconcentration and matrix effects.
  Recommended change: None.
- `NQ10-G09`: **supported**. Canonical proposition correctly avoids naming 'dilute-and-shoot' as the affected method, consistent with the gold record's does_not_support flag; kept as a limitation rather than converted to positive evidence (instruction #14).
  Recommended change: None.
- `NQ10-B01`: **supported**. Correctly typed as constraint_only with no evidence_ids and an executable violation_rule directly mirroring the must_not_claim task boundary; properly excluded from coverage scoring.
  Recommended change: None.

Human-review priorities:
- G04 merges atomic claims from two unrelated papers/matrices (EPA 8327 drinking water; foam-concentrate excerpt) into one scoring group. The partial_rule allows independent credit for either sub-fact, which is defensible, but a project author may prefer splitting into two independently scorable groups for finer-grained credit.
- NQ10_MMG009 is classified 'optional_gold' in the source gold packet but G08 elevates it to importance 'core' / scoring_role 'required_content' based on its direct relevance to the must_include boundary (recovery/chemistry-dependent suitability). This is a defensible task-boundary-driven judgment call but should be confirmed with the project author since it departs from the gold packet's own evidence_type weighting.
- G03 uses an expanded/context-revised span (span_revision_kind: complete_original_chunk) for NQ10_MMG007 rather than the original narrower exact_evidence_span; confirm this span-expansion practice is acceptable for verification purposes.
- This revised ledger and its dispositions are materially identical to the version already reviewed and approved in the supplied prior_model_b_group_review_open_issues; independent re-verification here reaches the same approve conclusion with no new blocking defects found.

### Non-normative reference prose

PFAS sample preparation before mass spectrometry varies with matrix, analyte scope, and analytical workflow rather than following one universal protocol. For parts-per-trillion determinations, reported preconcentration approaches include solid-phase extraction (SPE) and liquid-liquid extraction (LLE). Sorptive formats include an SPME method applied to river, lake, tap, and bottled water and an SBSE-TD-GC-MS method for PFCAs. Dilution-based alternatives include EPA Method 8327 dilute-and-shoot and a foam-concentrate excerpt that reports dilution and reagent mixing before HPLC injection but does not explicitly describe a separate SPE or LLE step. Study-specific examples include a 0.5 mL methanolic extract with about 500-fold enrichment, lower SPE recovery when sample volume increased from 10 to 100 mL with a 150 mg cartridge, and compound-dependent recoveries for C8-C14 PFAS. In the developed SPME protocol, preconcentration was higher and matrix effects were less frequent than for very rapid methods such as dilute-and-shoot. Other cited methods showed substantial matrix effects in complex samples, so recovery and robustness must be evaluated for the specific matrix and analyte set.

### Prose-to-ledger map

- PFAS sample preparation before mass spectrometry varies with matrix, analyte scope, and analytical workflow rather than following one universal protocol. -> NQ10-B01
- For parts-per-trillion determinations, reported preconcentration approaches include solid-phase extraction (SPE) and liquid-liquid extraction (LLE). -> NQ10-G01
- Sorptive formats include an SPME method applied to river, lake, tap, and bottled water and an SBSE-TD-GC-MS method for PFCAs. -> NQ10-G02, NQ10-G03
- Dilution-based alternatives include EPA Method 8327 dilute-and-shoot and a foam-concentrate excerpt that reports dilution and reagent mixing before HPLC injection but does not explicitly describe a separate SPE or LLE step. -> NQ10-G04
- Study-specific examples include a 0.5 mL methanolic extract with about 500-fold enrichment, lower SPE recovery when sample volume increased from 10 to 100 mL with a 150 mg cartridge, and compound-dependent recoveries for C8-C14 PFAS. -> NQ10-G05, NQ10-G06, NQ10-G07
- In the developed SPME protocol, preconcentration was higher and matrix effects were less frequent than for very rapid methods such as dilute-and-shoot. -> NQ10-G08
- Other cited methods showed substantial matrix effects in complex samples, so recovery and robustness must be evaluated for the specific matrix and analyte set. -> NQ10-G09, NQ10-B01

---

## NQ12

**Question:** What chain-length-related differences in PFAS analytical sensitivity or LOD/LOQ have been reported, and how do method or instrument settings affect them?

**Must include:** Must recognize compound-dependent analytical behavior; must connect calculation or interpretation to method/instrument conditions.

**Must not claim:** Must not claim one universal LOD/LOQ calculation or performance pattern applies identically to all PFAS chain lengths.

### Frozen task components

- `NQ12-T01`: Describe reported chain-length-related differences in analytical sensitivity or LOD/LOQ.
- `NQ12-T02`: Explain how method and instrument settings affect the calculation or interpretation of those differences.

### Complete gold evidence

**NQ12_MMG001** (required_gold; `2022 - Pellicer-Castell - Iron-Doped Bimodal Mesoporous Silica Nanomaterials as Sorbents for Solid-Phase Extraction of Perfluoroalkyl Substances in Environmental.pdf`, chunk `44`)
> [SOURCE_TEXT_OMITTED sha256=b1841c10e792b88e543d6fbb982eef015ae0c786fb4f653a5855b659f5abb8ba].

**NQ12_MMG002** (required_gold; `2024 - Habib - Green Analytical Method for Perfluorocarboxylic Acids (PFCAs) in Water of Stir Bar Sorptive Extraction Coupled with Thermal Desorption-Gas.pdf`, chunk `47`)
> [SOURCE_TEXT_OMITTED sha256=22bd7cf91ea75c0d8318432197b7d9a9c48427e0746a04775d8fa4dbc5656fb0]

**NQ12_MMG003** (required_gold; `2025 - Tomei - Optimization and Testing of an SPE-LC - q-TOF Analytical Method for the Detection of PFAS Degradation Products in Water Treatment Processes.pdf`, chunk `14`)
> [SOURCE_TEXT_OMITTED sha256=9716eb05d3a1ce2ed1b058dc637da46c77e1c235bf06817a94b48103bce56198];

### Normative content claim groups

#### NQ12-G01

- Component: `NQ12-T01`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: In a water SPE–UHPLC–MS/MS method applied to C8–C14 PFAS (PFOA, PFNA, PFOS, PFDA, PFUnDA, PFDS, PFDoDA, PFTrDA, PFTeDA), each compound has its own LOD and LOQ, with LODs spanning 3–8 ng/L and LOQs 9–25 ng/L rather than a single uniform detection limit across the series.
- Material qualifiers: ["matrix is water", "method is SPE–UHPLC–MS/MS", "compounds are C8–C14 PFAS: PFOA, PFNA, PFOS, PFDA, PFUnDA, PFDS, PFDoDA, PFTrDA, PFTeDA", "LOD values fall within 3–8 ng/L", "LOQ values fall within 9–25 ng/L"]
- Evidence: NQ12_MMG001
- Prior atomic claims: NQ12-C01, NQ12-C03
- Full: Award full credit if the answer states that in a water SPE–UHPLC–MS/MS method, individual C8–C14 PFAS (or the listed compounds) have distinct, compound-specific LOD and LOQ values, and correctly indicates that LODs are in the 3–8 ng/L range and LOQs in the 9–25 ng/L range, with water and SPE–UHPLC–MS/MS clearly identified.
- Partial: Award partial credit if the answer correctly notes that in a water SPE–UHPLC–MS/MS method C8–C14 PFAS (or the listed compounds) have different, compound-specific LOD/LOQ values, but omits or materially blurs the numeric ranges (for example, only gives a single example LOD/LOQ or vaguely says 'a few ng/L' without clear bounds), while still correctly indicating the matrix and method and not presenting incompatible numbers.
- Contradiction: Mark as contradicted if the answer claims or clearly implies that in the reported SPE–UHPLC–MS/MS water method all C8–C14 PFAS share a single common LOD/LOQ, or gives numeric ranges that are materially incompatible with the evidence (e.g., LODs in the tens or hundreds of ng/L for this method), or misattributes the method or matrix in a way that reverses the core meaning (e.g., assigning these values to a different method or non-water matrix).

#### NQ12-G02

- Component: `NQ12-T01`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: In the reported SBSE-TD-GC-MS performance table for PFCAs PFHpA, PFOA, PFNA, PFDA, PFUnA, PFDoA, and PFTeDA, sensitivity is compound-specific, with LODs of about 21-74 ng/L and LOQs of about 91-192 ng/L.
- Material qualifiers: ["method is SBSE-TD-GC-MS", "compounds are PFHpA, PFOA, PFNA, PFDA, PFUnA, PFDoA, and PFTeDA", "LOD values span approximately 21-74 ng/L", "LOQ values span approximately 91-192 ng/L", "the expanded exact span does not independently identify the sample matrix, so no matrix-specific claim is required"]
- Evidence: NQ12_MMG002
- Prior atomic claims: NQ12-C04
- Full: Award full if the answer identifies the SBSE-TD-GC-MS PFCA table and reports compound-specific LOD and LOQ ranges equivalent to about 21-74 and 91-192 ng/L, respectively.
- Partial: Award partial if the answer correctly reports only one range or states that sensitivity varies by compound without both ranges.
- Contradiction: Mark contradicted if the answer swaps LOD and LOQ, gives incompatible ranges, or claims one identical detection limit for all listed PFCAs.

#### NQ12-G03

- Component: `NQ12-T02`
- Importance: `supplementary`
- Function: `affirmative`
- Scoring role: `optional_content`
- Proposition: The two reported method tables show different absolute sensitivity ranges: SPE-UHPLC-MS/MS reports LODs of 3-8 ng/L and LOQs of 9-25 ng/L for its C8-C14 PFAS set, whereas SBSE-TD-GC-MS reports LODs of 21.17-73.96 ng/L and LOQs of 90.80-192.01 ng/L for a different C7-C14 PFCA set. This is a descriptive cross-study comparison and does not isolate method choice as the cause because analyte sets and protocols differ.
- Material qualifiers: ["SPE-UHPLC-MS/MS table: LOD 3-8 ng/L and LOQ 9-25 ng/L for its listed C8-C14 PFAS", "SBSE-TD-GC-MS table: LOD 21.17-73.96 ng/L and LOQ 90.80-192.01 ng/L for its listed C7-C14 PFCAs", "the studies use different analyte sets and protocols, so the comparison does not establish method-only causation"]
- Evidence: NQ12_MMG001, NQ12_MMG002
- Prior atomic claims: NQ12-C06
- Full: Award full if the answer correctly compares both LOD/LOQ ranges and explicitly notes that different analyte sets and protocols prevent attributing the difference solely to method choice.
- Partial: Award partial if the ranges are compared correctly but the cross-study confounding caveat is omitted, or if the caveat is given without both numerical ranges.
- Contradiction: Mark contradicted if the ranges are reversed or if the answer claims the comparison proves that method choice alone caused the difference.

#### NQ12-G04

- Component: `NQ12-T02`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: In a fragmentor-voltage test for carboxylic acids, setting the fragmentor to 60 V almost eliminated the signal of short-chain PFAS (C < 5), so that setting was discarded; the excerpt reports signal loss rather than numerical LOD or LOQ values.
- Material qualifiers: ["instrument variable is fragmentor voltage", "setting is 60 V", "affected analytes are short-chain PFAS with C < 5", "endpoint is near-loss of signal, not a reported LOD/LOQ"]
- Evidence: NQ12_MMG003
- Prior atomic claims: NQ12-C07, NQ12-S02, NQ12-L01
- Full: Award full if the answer states that 60 V almost eliminated C < 5 PFAS signal and was discarded, while not inventing a numeric LOD or LOQ.
- Partial: Award partial if the answer identifies fragmentor-voltage sensitivity for short-chain PFAS but omits either 60 V or the decision to discard the setting.
- Contradiction: Mark contradicted if the answer says 60 V improved short-chain signal or assigns a numerical LOD/LOQ not present in the span.

#### NQ12-G05

- Component: `NQ12-T01`
- Importance: `supplementary`
- Function: `affirmative`
- Scoring role: `optional_content`
- Proposition: For the SPE–UHPLC–MS/MS water method, reported LOD/LOQ pairs were: PFOA 4/12 ng/L, PFNA 7/22 ng/L, PFOS 3/9 ng/L, PFDA 8/24 ng/L, PFUnDA 7/21 ng/L, PFDS 3/11 ng/L, PFDoDA 6/18 ng/L, PFTrDA 8/25 ng/L, and PFTeDA 3/11 ng/L.
- Material qualifiers: ["matrix is water", "method is SPE–UHPLC–MS/MS", "LOD/LOQ values are given in ng/L", "each listed compound is associated with the correct LOD/LOQ pair"]
- Evidence: NQ12_MMG001
- Prior atomic claims: NQ12-C02
- Full: Award full credit for this optional group if the answer correctly lists the compound-specific LOD/LOQ pairs for the nine PFAS in the SPE–UHPLC–MS/MS water method with no material numeric errors.
- Partial: Award partial credit for this optional group if the answer correctly reports at least some of the compound-specific LOD/LOQ pairs for the SPE–UHPLC–MS/MS method without introducing incorrect values for the ones it mentions, even if not all nine are covered.
- Contradiction: Mark as contradicted for this optional group if the answer assigns materially incorrect LOD/LOQ pairs to one or more of these nine compounds under the SPE–UHPLC–MS/MS water method.

#### NQ12-G06

- Component: `NQ12-T01`
- Importance: `supplementary`
- Function: `affirmative`
- Scoring role: `optional_content`
- Proposition: In the SBSE-TD-GC-MS table, individual LOD/LOQ pairs were PFHpA 21.17/138.27 ng/L, PFOA 21.20/103.13 ng/L, PFNA 30.12/90.80 ng/L, PFDA 54.29/169.85 ng/L, PFUnA 34.39/132.90 ng/L, PFDoA 73.96/192.01 ng/L, and PFTeDA 35.02/107.10 ng/L.
- Material qualifiers: ["method is SBSE-TD-GC-MS", "LOD/LOQ values are in ng/L", "each listed PFCA is paired with its tabulated values", "no sample-matrix qualifier is required from this exact span"]
- Evidence: NQ12_MMG002
- Prior atomic claims: NQ12-C05
- Full: Award optional full credit if all listed compound-specific LOD/LOQ pairs are reported correctly for the SBSE-TD-GC-MS table.
- Partial: Award optional partial credit if at least two listed pairs are reported correctly without incompatible values.
- Contradiction: Mark contradicted if LOD and LOQ are swapped or a listed pair is materially misstated.

#### NQ12-G07

- Component: `NQ12-T01`
- Importance: `supplementary`
- Function: `affirmative`
- Scoring role: `optional_content`
- Proposition: In the SBSE-TD-GC-MS PFCA table, retention time and parent-ion m/z increase from PFHpA to PFTeDA, whereas LOD and LOQ values vary without a simple monotonic trend.
- Material qualifiers: ["applies to PFHpA through PFTeDA in the reported table", "method is SBSE-TD-GC-MS", "retention time and parent-ion m/z increase across the series", "LOD/LOQ values do not change monotonically", "no sample-matrix qualifier is required from this exact span"]
- Evidence: NQ12_MMG002
- Prior atomic claims: NQ12-S01
- Full: Award optional full credit if the answer reports both the monotonic retention-time/parent-ion trend and the non-monotonic LOD/LOQ pattern.
- Partial: Award optional partial credit if only one of those two patterns is reported correctly.
- Contradiction: Mark contradicted if the answer claims LOD/LOQ changes monotonically across all listed PFCAs.

#### NQ12-G08

- Component: `NQ12-T01`
- Importance: `supplementary`
- Function: `limitation`
- Scoring role: `optional_content`
- Proposition: The tabulated patterns are compound- and protocol-specific: within-table LOD/LOQ values are non-monotonic, and cross-study differences cannot be assigned solely to chain length or method because the analyte sets and protocols differ.
- Material qualifiers: ["applies only to the two reported tables", "cross-study comparison is confounded by analyte and protocol differences"]
- Evidence: NQ12_MMG001, NQ12_MMG002
- Prior atomic claims: 
- Full: Award full if the answer rejects a universal monotonic chain-length rule and identifies compound/protocol specificity.
- Partial: Award partial if the answer gives only one of the two limitations without making a universal claim.
- Contradiction: Mark contradicted if the answer asserts a universal monotonic LOD/LOQ relationship across PFAS and methods.

#### NQ12-G09

- Component: `NQ12-T01`
- Importance: `supplementary`
- Function: `limitation`
- Scoring role: `optional_content`
- Proposition: The quantitative findings are limited to the listed C8-C14 PFAS and C7-C14 PFCA sets under the two reported methods; only the SPE-UHPLC-MS/MS span explicitly identifies water samples, so the combined evidence must not be generalized to all matrices.
- Material qualifiers: ["compound and method scope must be retained", "water is explicit for the SPE-UHPLC-MS/MS table but is not required for the SBSE-TD-GC-MS exact span"]
- Evidence: NQ12_MMG001, NQ12_MMG002
- Prior atomic claims: NQ12-L02
- Full: Award full if the answer limits the ranges to the listed compound sets and methods and avoids generalizing them to all PFAS or matrices.
- Partial: Award partial if the answer gives a general scope caveat but does not distinguish the two compound sets.
- Contradiction: Mark contradicted if the answer treats the values as universal across PFAS classes, methods, or matrices.


### Prior atomic-claim dispositions

#### NQ12-C01

- Prior claim: In a developed SPE–UHPLC–MS/MS method for C8–C14 PFAS in water, each compound showed its own LOD and LOQ, with LODs between 3 and 8 ng/L and LOQs between 9 and 25 ng/L.
- Action: `revised`
- Final target(s): NQ12-G01
- Rationale: Mapped to G01, which retains the compound-specific LOD/LOQ ranges for the SPE–UHPLC–MS/MS water method but removes the unsupported attribution that LOD/LOQ values are 'referred to the final injection solution.'

#### NQ12-C02

- Prior claim: Under this SPE–UHPLC–MS/MS method in water, reported LOD/LOQ pairs were 4/12 ng/L for PFOA, 7/22 ng/L for PFNA, 3/9 ng/L for PFOS, 8/24 ng/L for PFDA, 7/21 ng/L for PFUnDA, 3/11 ng/L for PFDS, 6/18 ng/L for PFDoDA, 8/25 ng/L for PFTrDA, and 3/11 ng/L for PFTeDA.
- Action: `mapped`
- Final target(s): NQ12-G05
- Rationale: Directly corresponds to the detailed compound-specific LOD/LOQ pairs for the SPE–UHPLC–MS/MS water method, now grouped as an optional content claim.

#### NQ12-C03

- Prior claim: The SPE–UHPLC–MS/MS data show that, even within a relatively narrow C8–C14 range, detection limits differ by individual PFAS rather than following a single uniform LOD/LOQ value across all compounds.
- Action: `merged`
- Final target(s): NQ12-G01
- Rationale: Its interpretive point that detection limits differ by compound within C8–C14 under SPE–UHPLC–MS/MS is captured within G01’s central proposition about compound-specific LOD/LOQ values.

#### NQ12-C04

- Prior claim: For a stir bar sorptive extraction with thermal desorption GC–MS (SBSE–TD–GC–MS) method applied to water, PFCAs PFHpA, PFOA, PFNA, PFDA, PFUnA, PFDoA, and PFTeDA exhibited compound-specific LODs ranging from 21.17 to 73.96 ng/L and LOQs from 90.80 to 192.01 ng/L.
- Action: `mapped`
- Final target(s): NQ12-G02
- Rationale: Provides the numeric LOD/LOQ ranges and compound-specific nature of sensitivity under the SBSE–TD–GC–MS water method, which form the basis of G02.

#### NQ12-C05

- Prior claim: Under the SBSE–TD–GC–MS method in water, individual LOD/LOQ pairs were 21.17/138.27 ng/L for PFHpA, 21.20/103.13 ng/L for PFOA, 30.12/90.80 ng/L for PFNA, 54.29/169.85 ng/L for PFDA, 34.39/132.90 ng/L for PFUnA, 73.96/192.01 ng/L for PFDoA, and 35.02/107.10 ng/L for PFTeDA.
- Action: `mapped`
- Final target(s): NQ12-G06
- Rationale: Consists of the detailed compound-specific LOD/LOQ pairs for the SBSE–TD–GC–MS water method, now represented as optional content in G06.

#### NQ12-S01

- Prior claim: In the SBSE–TD–GC–MS study, retention time and parent ion m/z increased with longer-chain PFCAs, while the LOD and LOQ values varied among analytes rather than mirroring a simple monotonic trend with chain length.
- Action: `mapped`
- Final target(s): NQ12-G07
- Rationale: Describes retention time/mass increases and non-monotonic LOD/LOQ behavior with chain length in the SBSE–TD–GC–MS PFCA series, which is captured in G07 as an optional interpretive claim.

#### NQ12-C06

- Prior claim: Comparing the two water-analysis methods, the SPE–UHPLC–MS/MS procedure reported lower LODs (3–8 ng/L) and LOQs (9–25 ng/L) for C8–C14 PFAS than the SBSE–TD–GC–MS method, which reported higher LODs (21.17–73.96 ng/L) and LOQs (90.80–192.01 ng/L) for C7–C14 PFCAs, indicating that absolute detection limits depend on the analytical method as well as on the individual PFAS.
- Action: `mapped`
- Final target(s): NQ12-G03
- Rationale: Cross-method comparison of LOD/LOQ ranges between SPE–UHPLC–MS/MS and SBSE–TD–GC–MS in water is preserved in G03, emphasizing method-dependent sensitivity.

#### NQ12-C07

- Prior claim: In an SPE–LC–q‑TOF method targeting PFAS-related carboxylic acids in water, setting the fragmentor voltage to 60 V caused the signal of short-chain PFAS (C < 5) to be almost lost, leading this fragmentor setting to be discarded.
- Action: `merged`
- Final target(s): NQ12-G04
- Rationale: The description of near-complete short-chain PFAS signal loss at 60 V fragmentor voltage in SPE–LC–q‑TOF is a core part of G04’s central proposition.

#### NQ12-S02

- Prior claim: The near-complete loss of short-chain PFAS signal at 60 V in the LC–q‑TOF study demonstrates that fragmentor voltage, an instrument tuning parameter, can selectively and strongly reduce sensitivity for short-chain PFAS relative to other analytes.
- Action: `merged`
- Final target(s): NQ12-G04
- Rationale: Its interpretive point that fragmentor voltage can selectively and strongly reduce sensitivity for short-chain PFAS is incorporated as part of G04’s explanation of the instrument-setting effect.

#### NQ12-L01

- Prior claim: The LC–q‑TOF study reporting loss of short-chain PFAS signal at 60 V did not provide numerical LOD or LOQ values, limiting quantitative assessment of how fragmentor voltage changes detection limits.
- Action: `merged`
- Final target(s): NQ12-G04
- Rationale: The limitation that no numerical LOD/LOQ values were reported in the LC–q‑TOF study is included as a material qualifier in G04.

#### NQ12-L02

- Prior claim: All reported LOD/LOQ data come from water matrices and from specific PFAS subsets (C7–C14 PFCAs and C8–C14 PFAS), so the available evidence does not establish chain-length–sensitivity relationships for other PFAS classes or matrices.
- Action: `mapped`
- Final target(s): NQ12-G09
- Rationale: Becomes G09, which states the matrix and compound-set limitations of the quantitative LOD/LOQ data.

### Constraint-only groups

- `NQ12-B01`: Answers must not claim that a single universal LOD/LOQ calculation or performance pattern applies identically to all PFAS chain lengths and analytical methods.
  Violation rule: Flag a boundary violation if the answer asserts or clearly implies that there is one universal or method-independent relationship between PFAS chain length and LOD/LOQ (such as a fixed monotonic trend or single formula) that applies identically across all PFAS and analytical configurations.

### Model B verification

Overall verdict: **approve**

- `NQ12-G01`: **supported**. LOD 3-8 ng/L / LOQ 9-25 ng/L ranges verified against the table (PFOA 4/12, PFNA 7/22, PFOS 3/9, PFDA 8/24, PFUnDA 7/21, PFDS 3/11, PFDoDA 6/18, PFTrDA 8/25, PFTeDA 3/11). The round-1 defect flagged by prior Model B (misattributing the 'final injection solution' footnote, anchored only to the Linearity column, to LOD/LOQ) has been removed from the canonical proposition and material qualifiers. Full/partial/contradiction rules are executable and consistent.
  Recommended change: None.
- `NQ12-G02`: **supported**. LOD ~21-74 ng/L / LOQ ~91-192 ng/L verified against the seven-compound table. The group correctly withholds a matrix qualifier because the exact span itself does not contain the word 'water', avoiding overclaiming beyond the literal evidence text even though the gold record's matrix metadata says water.
  Recommended change: None.
- `NQ12-G03`: **supported**. Synthesis claim correctly reports both ranges and explicitly caveats that different analyte sets/protocols prevent isolating method as the sole cause, avoiding an unsupported causal claim.
  Recommended change: None.
- `NQ12-G04`: **supported**. Matches the exact span: 60 V fragmentor voltage almost eliminated C<5 PFAS signal, so it was discarded. Correctly kept as a qualitative/negative finding (no invented numeric LOD/LOQ), satisfying rule 14.
  Recommended change: None.
- `NQ12-G05`: **supported**. Itemized compound-pair detail correctly marked optional_content, avoiding double-weighting against the core G01 range claim.
  Recommended change: None.
- `NQ12-G06`: **supported**. Itemized compound-pair detail for SBSE-TD-GC-MS, correctly optional relative to core G02.
  Recommended change: None.
- `NQ12-G07`: **supported**. Retention time/parent-ion monotonic increase versus non-monotonic LOD/LOQ pattern is verifiable from the table and correctly scoped as optional.
  Recommended change: None.
- `NQ12-G08`: **supported**. Limitation group correctly rejects a universal monotonic chain-length rule without introducing unsupported content.
  Recommended change: None.
- `NQ12-G09`: **supported**. Correctly scopes the quantitative findings to the listed compound sets/methods and avoids universalizing to other matrices; correctly notes water is explicit only for the SPE-UHPLC-MS/MS span.
  Recommended change: None.
- `NQ12-B01`: **supported**. Boundary constraint mirrors the frozen must_not_claim boundary verbatim in substance, has an executable violation_rule, and is correctly excluded from coverage scoring (constraint_only).
  Recommended change: None.

Human-review priorities:
- Confirm the grading harness excludes optional_content groups (G03, G05, G06, G07, G08, G09) and the constraint_only group (B01) from the required-content coverage denominator, since several optional groups deliberately restate numeric detail already present in the core groups G01/G02/G04 (e.g., G05/G06 itemize pairs already ranged in G01/G02).
- The NQ12_MMG001 table header ('Sensitivity (ng L−1) ... LOD LOQ') is a flattened OCR extraction whose column-to-subheader mapping is not fully unambiguous on its face; the gold annotator's own does_not_support note flags this. The ledger's consistent LOD/LOQ assignment (e.g., PFOA 4/12) matches the annotator's interpretation, but project authors should do a final visual check against the original PDF table before sign-off.
- G02's decision to omit a matrix ('water') qualifier because the literal exact span lacks the word, despite the source document's title and gold metadata identifying it as a water method, is a defensible strict-evidence choice but is a judgment call project authors may want to revisit if downstream scoring expects the matrix to be stated.

### Non-normative reference prose

The SPE-UHPLC-MS/MS table for C8-C14 PFAS in water reports compound-specific LODs of 3-8 ng/L and LOQs of 9-25 ng/L. The SBSE-TD-GC-MS PFCA table reports LODs of 21.17-73.96 ng/L and LOQs of 90.80-192.01 ng/L, with retention time and parent-ion mass increasing across the listed homologues but LOD/LOQ values not following a simple monotonic pattern. These two tables have different sensitivity ranges, but the comparison is descriptive because their analyte sets and protocols differ and therefore does not isolate method choice as the cause. Separately, a 60 V fragmentor setting almost eliminated the signal of short-chain PFAS (C < 5) and was discarded, showing an instrument-setting effect without reporting a numerical LOD or LOQ. The findings remain limited to the listed compounds and methods and do not support a universal chain-length, method, or matrix rule.

### Prose-to-ledger map

- The SPE-UHPLC-MS/MS table for C8-C14 PFAS in water reports compound-specific LODs of 3-8 ng/L and LOQs of 9-25 ng/L. -> NQ12-G01, NQ12-G05
- The SBSE-TD-GC-MS PFCA table reports LODs of 21.17-73.96 ng/L and LOQs of 90.80-192.01 ng/L, with retention time and parent-ion mass increasing across the listed homologues but LOD/LOQ values not following a simple monotonic pattern. -> NQ12-G02, NQ12-G06, NQ12-G07
- These two tables have different sensitivity ranges, but the comparison is descriptive because their analyte sets and protocols differ and therefore does not isolate method choice as the cause. -> NQ12-G03, NQ12-G08
- Separately, a 60 V fragmentor setting almost eliminated the signal of short-chain PFAS (C < 5) and was discarded, showing an instrument-setting effect without reporting a numerical LOD or LOQ. -> NQ12-G04
- The findings remain limited to the listed compounds and methods and do not support a universal chain-length, method, or matrix rule. -> NQ12-G08, NQ12-G09, NQ12-B01

---

## NQ15

**Question:** How do electrolyte composition and pH-control choices affect interpretation of PFAS removal or degradation experiments?

**Must include:** Must treat buffer choice as a balance between pH control and interference risk; must connect to system or mechanism dependence.

**Must not claim:** Must not claim one exact buffer is universally correct for all PFAS removal experiments.

### Frozen task components

- `NQ15-T01`: Explain how electrolyte composition and pH-control choices can affect PFAS removal or degradation experiments.
- `NQ15-T02`: Explain how those choices limit interpretation across systems or mechanisms.

### Complete gold evidence

**NQ15_MMG001** (required_gold; `2023 - Unknown - Recent advances in electrochemical decontamination of perfluorinated compounds from water - a review.pdf`, chunk `17`)
> [SOURCE_TEXT_OMITTED sha256=11d5e985b964819de392f3c37bce7cd0f8ac12b30557a4c868dc94b78dec96d6].

**NQ15_MMG002** (optional_gold; `2023 - Unknown - Recent advances in electrochemical decontamination of perfluorinated compounds from water - a review.pdf`, chunk `16`)
> There is no reported consensus on the effects of pH to date.

**NQ15_MMG003** (optional_gold; `2023 - Unknown - Recent advances in electrochemical decontamination of perfluorinated compounds from water - a review.pdf`, chunk `18`)
> [SOURCE_TEXT_OMITTED sha256=80752d02bc0fc2569dfa73d25e7dd148800c07a030387526c7d5b732fef6d7cc]

**NQ15_MMG004** (optional_gold; `2023 - Unknown - Recent advances in electrochemical decontamination of perfluorinated compounds from water - a review.pdf`, chunk `46`)
> [SOURCE_TEXT_OMITTED sha256=d91fafa8a280a9f1c6bc97bcb4ce404f7081449f1df3c149f1a9a40bc3f58788]

**NQ15_MMG005** (optional_gold; `2023 - Alam - Experimental investigations of Per- and Poly-fluoroalkyl substances (PFAS) degradation by non-thermal plasma in aqueous solutions.pdf`, chunk `40`)
> [SOURCE_TEXT_OMITTED sha256=c5bb0683645357f76271c376a41e814c9de8e411db1089a8ee8b768043acb239].

### Normative content claim groups

#### NQ15-G01

- Component: `NQ15-T02`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: Across PFAS electro-oxidation studies, there is no reported consensus on the effects of pH.
- Material qualifiers: ["the statement is limited to the cited review", "the span does not itself explain why consensus is absent or quantify between-study disagreement"]
- Evidence: NQ15_MMG002
- Prior atomic claims: NQ15-C01
- Full: Award full if the answer states that the cited literature reports no consensus on pH effects without inventing a consensus trend.
- Partial: Award partial if the answer describes pH effects as uncertain or inconsistent but does not explicitly state the lack of consensus.
- Contradiction: Mark contradicted if the answer claims the cited review reports one settled pH-effect direction.

#### NQ15-G02

- Component: `NQ15-T01`
- Importance: `core`
- Function: `limitation`
- Scoring role: `required_content`
- Proposition: In electrochemical PFAS degradation experiments, relying only on the initial bulk pH to assess pH effects is likely to lead to a false interpretation of degradation behavior.
- Material qualifiers: ["Applies to PFAS degradation in electrochemical oxidation systems in water.", "The warning concerns using only the starting (initial) pH, without accounting for pH changes during the experiment."]
- Evidence: NQ15_MMG001
- Prior atomic claims: NQ15-C02
- Full: FULL if the answer states that in electrochemical PFAS degradation experiments, using only the initial or starting pH to interpret pH effects is likely to result in a false or misleading interpretation of degradation behavior.
- Partial: PARTIAL if the answer conveys that initial pH alone is insufficient or potentially misleading for interpreting pH effects but does not clearly state that such reliance is likely to lead to a false interpretation, or omits that the context is electrochemical degradation.
- Contradiction: CONTRADICTED if the answer claims that relying solely on the initial pH is adequate or sufficient for correctly interpreting pH effects on PFAS degradation in electrochemical systems, or otherwise portrays initial pH alone as reliably representative of pH effects.

#### NQ15-G03

- Component: `NQ15-T01`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: Across the cited electro-oxidation, electro-coagulation, and non-thermal-plasma examples, electrolyte composition or ion identity changes PFAS removal or degradation behavior, so the electrolyte is a mechanistically active experimental variable.
- Material qualifiers: ["evidence spans three different treatment configurations", "effects are study- and mechanism-specific", "no named pH buffer is directly tested in the supplied evidence"]
- Evidence: NQ15_MMG003, NQ15_MMG004, NQ15_MMG005
- Prior atomic claims: NQ15-C03
- Full: Award full if the answer states that electrolyte composition or ion identity can change PFAS treatment performance and treats the effect as system-specific rather than universal.
- Partial: Award partial if the answer notes an electrolyte effect but does not state that the direction or mechanism depends on the system.
- Contradiction: Mark contradicted if the answer treats electrolyte composition as inert or claims one observed ordering is universal.

#### NQ15-G05

- Component: `NQ15-T02`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: Electrolyte-dependent changes in PFAS removal or degradation observed in electro-oxidation, electro-coagulation, and non-thermal plasma systems indicate that electrolyte choices are system- and mechanism-dependent and cannot be assumed to transfer universally between different PFAS treatment technologies.
- Material qualifiers: ["Supported by examples from electro-oxidation of 6:2 fluorotelomer sulfonic acid, electro-coagulation of PFOS, and non-thermal plasma degradation of PFOS.", "Implication is that an electrolyte composition that performs well in one PFAS treatment system may not behave the same way in another system based on a different mechanism."]
- Evidence: NQ15_MMG003, NQ15_MMG004, NQ15_MMG005
- Prior atomic claims: NQ15-C07
- Full: FULL if the answer explicitly states that electrolyte effects on PFAS removal/degradation are system- or mechanism-dependent and that an electrolyte (or ion composition) that works or behaves in one PFAS treatment technology cannot be assumed to work or behave the same in others, with at least a brief reference to the fact that different mechanisms (e.g., electro-oxidation vs electro-coagulation vs plasma) show different electrolyte dependencies.
- Partial: PARTIAL if the answer notes that electrolyte effects vary between different PFAS treatment systems or mechanisms but does not clearly articulate the non-transferability (e.g., does not explicitly say they cannot be assumed universal), or if it implies system dependence through examples without an explicit general statement.
- Contradiction: CONTRADICTED if the answer claims or strongly implies that a given electrolyte choice or electrolyte effect can be assumed to apply universally or similarly across different PFAS treatment systems and mechanisms.

#### NQ15-G06

- Component: `NQ15-T01`
- Importance: `supplementary`
- Function: `affirmative`
- Scoring role: `optional_content`
- Proposition: In electro-oxidation of 6:2 fluorotelomer sulfonic acid (20 mg/L) on a Ti/SnO2-Sb2O5-Bi2O3 anode, degradation efficiency decreases when the supporting electrolyte is changed in the order NaClO4 > NaCl > Na2SO4.
- Material qualifiers: ["PFAS compound is 6:2 fluorotelomer sulfonic acid at 20 mg/L in water.", "Anode material is Ti/SnO2-Sb2O5-Bi2O3.", "The ordering NaClO4 > NaCl > Na2SO4 is specific to this study and does not generalize to all systems."]
- Evidence: NQ15_MMG003
- Prior atomic claims: NQ15-C04
- Full: FULL if the answer accurately describes that, in a specific electro-oxidation study of 6:2 FTSA on a Ti/SnO2-Sb2O5-Bi2O3 anode, degradation was better in NaClO4 than NaCl, and better in NaCl than Na2SO4, indicating electrolyte-dependent performance.
- Partial: PARTIAL if the answer mentions that electrolyte identity (NaClO4, NaCl, Na2SO4) affected 6:2 FTSA electro-oxidation performance but omits the full ordering, gets part of the order correct, or omits some study details (e.g., anode type or concentration) while still correctly conveying that different electrolytes changed degradation.
- Contradiction: CONTRADICTED if the answer states an ordering that contradicts the evidence (e.g., Na2SO4 > NaCl or NaCl > NaClO4) or claims that electrolyte identity had no effect in this system.

#### NQ15-G07

- Component: `NQ15-T01`
- Importance: `supplementary`
- Function: `affirmative`
- Scoring role: `optional_content`
- Proposition: In Fe-anode electro-coagulation of PFOS, removal efficiencies varied strongly with electrolyte anion, with reported removals of 99.6% in NaCl, 93.7% in Na2SO4, 63.5% in NaNO3, and 45.4% in NaH2PO4 under the study conditions.
- Material qualifiers: ["Reported removals were 99.6% (NaCl), 93.7% (Na2SO4), 63.5% (NaNO3), and 45.4% (NaH2PO4).", "Applies to PFOS removal in water using Fe-anode electro-coagulation, and is study-specific."]
- Evidence: NQ15_MMG004
- Prior atomic claims: NQ15-C05
- Full: FULL if the answer describes that, in Fe-anode electro-coagulation experiments, PFOS removal efficiencies differed greatly among NaCl, Na2SO4, NaNO3, and NaH2PO4 electrolytes and reports those efficiencies with correct qualitative ranking (NaCl > Na2SO4 > NaNO3 > NaH2PO4) and approximately correct percentages. Percentages are considered approximately correct if they clearly correspond to about 99.6%, 93.7%, 63.5%, and 45.4% either by (a) using the exact values or any of the accepted textual equivalents listed in accepted_numeric_equivalents, or (b) giving numeric values within ±1 percentage point of each of these values, even without hedge words like 'about' or 'approximately'.
- Partial: PARTIAL if the answer notes that PFOS removal by Fe-anode electro-coagulation depends strongly on electrolyte type and gives either some but not all of the percentages correctly, or correctly provides the ranking (NaCl > Na2SO4 > NaNO3 > NaH2PO4) without all the numbers, or provides approximately but not exactly correct numerical values (outside the ±1 percentage point tolerance) while still clearly conveying large differences.
- Contradiction: CONTRADICTED if the answer asserts that these electrolytes provide similar or indistinguishable PFOS removal in Fe-anode electro-coagulation, or gives a clearly reversed or incompatible ranking (e.g., NaH2PO4 > NaCl).

#### NQ15-G08

- Component: `NQ15-T01`
- Importance: `supplementary`
- Function: `affirmative`
- Scoring role: `optional_content`
- Proposition: In non-thermal plasma degradation of PFOS, when an electrolyte solution and a surface water matrix had similar conductivities (300 vs 320 µS/cm), differences in cation composition (monovalent vs monovalent plus divalent) were considered a possible cause of differing PFOS breakdown rates.
- Material qualifiers: ["Conductivities of the electrolyte solution and surface water were comparable (300 vs 320 µS/cm).", "Ion composition differed: monovalent cations in the electrolyte solution versus monovalent plus divalent cations in the surface water.", "The influence of ion composition was hypothesized as a possible cause, not definitively proven, and is study-specific."]
- Evidence: NQ15_MMG005
- Prior atomic claims: NQ15-C06
- Full: FULL if the answer indicates that in a non-thermal plasma PFOS degradation experiment with similar conductivities in an electrolyte solution and surface water, differences in ion composition (monovalent vs monovalent plus divalent cations) were hypothesized as a reason for different breakdown rates.
- Partial: PARTIAL if the answer captures that ion composition, rather than conductivity alone, was thought to influence PFOS breakdown in a non-thermal plasma system but omits specific conductivity values or the precise distinction between monovalent and divalent cations.
- Contradiction: CONTRADICTED if the answer claims that in this context only conductivity matters and that ion composition was not considered or was ruled out as a factor, or that ion composition was found to have no possible influence.

#### NQ15-G09

- Component: `NQ15-T02`
- Importance: `core`
- Function: `limitation`
- Scoring role: `required_content`
- Proposition: The supplied evidence does not directly compare named pH buffers, so it cannot establish a buffer-specific performance rule. Electrolyte results motivate testing whether ions used for pH control interfere with a treatment system, but that extension is an explicitly identified inference rather than a measured buffer result.
- Material qualifiers: ["the limitation concerns the supplied evidence set", "buffer-specific behavior is not directly measured", "using electrolyte evidence to motivate buffer-interference testing is an inference, not a reported result"]
- Evidence: NQ15_MMG001, NQ15_MMG002, NQ15_MMG003, NQ15_MMG004, NQ15_MMG005
- Prior atomic claims: NQ15-C08
- Full: Award full if the answer explicitly states that no named buffer is directly compared and therefore avoids a buffer-specific recommendation, while allowing a clearly labeled inference that pH-control ions should be tested for interference.
- Partial: Award partial if the answer avoids recommending a universal buffer but does not explicitly identify the buffer-evidence gap.
- Contradiction: Mark contradicted if the answer presents a specific buffer as experimentally proven optimal by these records.


### Prior atomic-claim dispositions

#### NQ15-C01

- Prior claim: There is no reported consensus on the effects of pH on PFAS electro‑oxidation degradation across studies, which complicates comparison and interpretation of pH trends.
- Action: `revised`
- Final target(s): NQ15-G01
- Rationale: Directly restates the lack of consensus on pH effects and its impact on interpretation; fully supported by NQ15_MMG002 and now mapped solely to the cross-system interpretation group G01. The interpretive-difficulty point is treated as permissible inference rather than a required element for scoring.

#### NQ15-C02

- Prior claim: For electrochemical PFAS degradation experiments, relying only on the initial bulk pH to assess the effects of pH is likely to lead to a false interpretation, and real‑time monitoring of pH near the anode surface is indicated as necessary to avoid misinterpretation.
- Action: `revised`
- Final target(s): NQ15-G02
- Rationale: The portion stating that relying only on initial pH can lead to false interpretation is supported and retained in G02. The stronger assertion that real-time pH monitoring near the anode is necessary is not in the quoted span and is therefore dropped rather than scored.

#### NQ15-C03

- Prior claim: Because the chemical components in an electrolyte can affect PFAS removal through different influencing mechanisms in electro‑coagulation, electrolytes or buffers used for pH control or conductivity in such experiments should be treated as mechanistically active variables that can change removal performance rather than as inert background salts.
- Action: `revised`
- Final target(s): NQ15-G03
- Rationale: The factual core—that electrolyte components affect PFAS removal mechanisms and should be treated as mechanistically active variables—is supported and captured in G03, using the explicit electrolyte-based evidence. The more speculative extrapolation to buffers is treated as an interpretive extension in the prose but not required for scoring.

#### NQ15-C04

- Prior claim: Electrolyte identity strongly influences PFAS degradation efficiency in electrochemical oxidation, as shown by degradation of 6:2 fluorotelomer sulfonic acid (20 mg/L) on a Ti/SnO2‑Sb2O5‑Bi2O3 anode, where performance declined with electrolytes in the order NaClO4 > NaCl > Na2SO4.
- Action: `revised`
- Final target(s): NQ15-G06
- Rationale: Directly supported by NQ15_MMG003; preserved as a study-specific example of electrolyte effects on electro-oxidation and mapped only to the optional example group G06.

#### NQ15-C05

- Prior claim: In Fe‑anode electro‑coagulation experiments, PFOS removal efficiencies depended strongly on electrolyte anion, with reported removals of 99.6% in NaCl, 93.7% in Na2SO4, 63.5% in NaNO3, and 45.4% in NaH2PO4.
- Action: `revised`
- Final target(s): NQ15-G07
- Rationale: Directly supported by NQ15_MMG004; preserved as a quantitative example of electrolyte-dependent PFOS removal in electro-coagulation and mapped only to the optional example group G07.

#### NQ15-C06

- Prior claim: In non‑thermal plasma PFOS degradation tests where an electrolyte solution and surface water had comparable conductivities (300 versus 320 µS/cm), differing ion compositions—monovalent cations in the electrolyte solution versus monovalent plus divalent cations in the surface water—were considered a possible cause of differing PFOS breakdown rates, highlighting that electrolyte composition can influence degradation independently of conductivity.
- Action: `revised`
- Final target(s): NQ15-G08
- Rationale: Directly supported by NQ15_MMG005; retained as a hypothesis-based example of ion composition effects in non-thermal plasma and mapped only to the optional example group G08.

#### NQ15-C07

- Prior claim: The divergent effects of electrolyte composition observed in electro‑oxidation of 6:2 fluorotelomer sulfonic acid, Fe‑anode electro‑coagulation of PFOS, and non‑thermal plasma degradation of PFOS indicate that electrolyte or buffer choices are system‑ and mechanism‑dependent and cannot be assumed to transfer universally between different PFAS treatment technologies.
- Action: `mapped`
- Final target(s): NQ15-G05
- Rationale: This synthesis that electrolyte effects are system- and mechanism-dependent is supported by combining the three study-specific examples and is captured as a core interpretive claim in G05.

#### NQ15-C08

- Prior claim: The available evidence on pH and electrolyte effects focuses on electrochemical and non‑thermal plasma treatments of PFAS and does not establish how specific named buffer formulations perform or interfere across all PFAS compounds and treatment methods.
- Action: `mapped`
- Final target(s): NQ15-G09
- Rationale: Captures the scope limitation of the evidence base and the lack of direct data on specific buffers; retained as an optional limitation claim in G09.

### Constraint-only groups

- `NQ15-B01`: It is not supported to claim that any single specific buffer or electrolyte formulation is universally optimal or correct for all PFAS removal or degradation experiments across different systems and mechanisms.
  Violation rule: VIOLATION if the answer claims or strongly implies that one specific buffer or electrolyte formulation is universally correct, optimal, or appropriate for all PFAS removal or degradation experiments, regardless of treatment mechanism or system.

### Model B verification

Overall verdict: **approve**

- `NQ15-G01`: **supported**. Canonical proposition is a direct restatement of the quoted span; qualifiers correctly note the span doesn't explain the cause of disagreement.
  Recommended change: None.
- `NQ15-G02`: **supported**. Correctly resolves the prior overreach: the unsupported 'real-time monitoring near the anode' assertion (flagged in NQ15_MMG001's does_not_support field) has been dropped from the canonical proposition and full_rule, leaving only the span-entailed 'initial pH reliance is likely to mislead' claim.
  Recommended change: None.
- `NQ15-G03`: **supported**. Resolves prior C03 overreach: the buffer-specific extrapolation is now confined to a disclosed, non-mandatory qualifier ('no named pH buffer is directly tested') rather than being folded into the scored canonical proposition, which is limited to electrolyte-as-mechanistically-active.
  Recommended change: None.
- `NQ15-G05`: **supported**. Synthesis proposition (system/mechanism non-transferability) is distinct in scoring intent from G03 (electrolyte is active) even though it draws on the same three spans; each targets a different required proposition rather than double-counting the same claim.
  Recommended change: None.
- `NQ15-G06`: **supported**. Ordering and compound/matrix/anode attribution match the span exactly; correctly scoped as study-specific optional content.
  Recommended change: None.
- `NQ15-G07`: **supported**. Four percentages and ranking match the span; numeric_required with a tolerance-based equivalence rule is appropriately claim-specific.
  Recommended change: None.
- `NQ15-G08`: **supported**. Hypothesis framing ('possible cause,' not confirmed) is preserved from the source and not converted into a proven positive finding.
  Recommended change: None.
- `NQ15-G09`: **supported**. Correctly frames the buffer-evidence gap as a required limitation statement distinct from B01's violation-only check; explicitly labels the buffer-interference extension as inference, addressing the prior boundary-satisfaction concern.
  Recommended change: None.
- `NQ15-B01`: **supported**. Executable violation rule directly operationalizes the must_not_claim boundary (no single buffer/electrolyte universally correct); correctly excluded from coverage denominator as constraint_only.
  Recommended change: None.

Human-review priorities:
- G01 (core, required_content) rests solely on evidence_type='optional_gold' NQ15_MMG002, and G03/G05 (also core required_content) rest solely on optional_gold NQ15_MMG003-005; this evidence_type/scoring_role divergence appears intentional given the question's 'answerable_examples_only' nature, but merits final author sign-off as a schema convention.
- G03 and G05 both draw on the identical three exact spans (MMG003-005) to support two separate core required_content propositions; this is a defensible split (electrolyte-is-active vs. non-transferability-across-systems) rather than literal duplication, but is worth a quick author confirmation that it isn't inadvertently double-rewarding one underlying insight.
- Confirm the buffer must_include boundary is acceptably satisfied through disclosed inference in G03's qualifiers and the reference answer's closing sentence, since no gold record contains the word 'buffer' and no claim group makes a buffer-specific empirical assertion a scoring requirement.

### Non-normative reference prose

The cited review reports no consensus on pH effects and warns that relying only on initial pH can mislead interpretation of PFAS degradation. In one electro-oxidation study, degradation of 6:2 fluorotelomer sulfonic acid decreased in the order NaClO4 > NaCl > Na2SO4. In Fe-anode electro-coagulation, PFOS removal was 99.6% in NaCl, 93.7% in Na2SO4, 63.5% in NaNO3, and 45.4% in NaH2PO4. A non-thermal-plasma comparison also attributed differing PFOS breakdown rates in solutions of similar conductivity to a possible difference in monovalent and divalent ions. Together, these examples show that electrolyte composition is mechanistically active and that its effect is specific to the treatment configuration rather than transferable as one universal ordering. No supplied span directly compares named pH buffers, so a buffer-specific recommendation is unsupported; at most, the electrolyte evidence motivates explicitly testing whether ions introduced for pH control interfere with the selected system.

### Prose-to-ledger map

- The cited review reports no consensus on pH effects and warns that relying only on initial pH can mislead interpretation of PFAS degradation. -> NQ15-G01, NQ15-G02
- In one electro-oxidation study, degradation of 6:2 fluorotelomer sulfonic acid decreased in the order NaClO4 > NaCl > Na2SO4. -> NQ15-G06
- In Fe-anode electro-coagulation, PFOS removal was 99.6% in NaCl, 93.7% in Na2SO4, 63.5% in NaNO3, and 45.4% in NaH2PO4. -> NQ15-G07
- A non-thermal-plasma comparison also attributed differing PFOS breakdown rates in solutions of similar conductivity to a possible difference in monovalent and divalent ions. -> NQ15-G08
- Together, these examples show that electrolyte composition is mechanistically active and that its effect is specific to the treatment configuration rather than transferable as one universal ordering. -> NQ15-G03, NQ15-G05
- No supplied span directly compares named pH buffers, so a buffer-specific recommendation is unsupported; at most, the electrolyte evidence motivates explicitly testing whether ions introduced for pH control interfere with the selected system. -> NQ15-G09, NQ15-B01

---

## NQ23

**Question:** What energy-consumption or energy-efficiency evidence is available for PFAS degradation methods, and can values be compared across studies?

**Must include:** Must identify the energy metric used, such as EEO, EEM, kWh/m3, kWh/g, electrical input, or energy per mass removed; must explain comparability limits.

**Must not claim:** Must not claim one universal energy-consumption number fairly represents all PFAS degradation methods.

### Frozen task components

- `NQ23-T01`: Identify the reported energy-consumption or energy-efficiency evidence and the metrics used for PFAS degradation methods.
- `NQ23-T02`: Explain whether and under what restrictions energy values can be compared across studies.

### Complete gold evidence

**NQ23_MMG001** (required_gold; `2022 - Palma - State of the art and perspectives about non-thermal plasma applications for the removal of PFAS in water.pdf`, chunk `46`)
> [SOURCE_TEXT_OMITTED sha256=e56b37a858688639c55242276d7e94a3b67a8e5e83de58060e449ff423098610].

**NQ23_MMG002** (required_gold; `2021 - Nau-Hix - Field Demonstration of a Pilot-Scale Plasma Reactor for the Rapid Removal of Poly- and Perfluoroalkyl Substances in Groundwater.pdf`, chunk `28`)
> [SOURCE_TEXT_OMITTED sha256=c1567affb204244f5b483d7ecc78c1a161a91dbca626c8031125f9ffa459041f]).

**NQ23_MMG003** (required_gold; `2023 - Smith - Electrochemical Oxidation for Treatment of PFAS in Contaminated Water and Fractionated Foam─A Pilot-Scale Study.pdf`, chunk `33`)
> [SOURCE_TEXT_OMITTED sha256=41efa304c07178706d8f631de2ab3bce3b57c4bf72a90d4f106b21b846b55795].

**NQ23_MMG004** (required_gold; `2026 - Kumar - Degradation and defluorination of perfluorooctane sulfonate (PFOS) forever chemical in water using hydrodynamic cavitation treatment.pdf`, chunk `46`)
> [SOURCE_TEXT_OMITTED sha256=a351815a657247aad58e59b4f7988c25bae468eb9326d9de5e337ac998805ff8]

**NQ23_MMG005** (required_gold; `2024 - Chen - Combining nonthermal N2 plasma with a denitrifying biofilm reactor for PFAS-contaminated wastewater remediation.pdf`, chunk `21`)
> [SOURCE_TEXT_OMITTED sha256=f5233e6140d201d28af2a506bd29ae511a8a352399d5d18fef771f04d1a2f071]).

**NQ23_MMG006** (negative_gold; `2025 - Capodaglio - Prospects of Novel Technologies for PFAS Destruction in Water and Wastewater.pdf`, chunk `11`)
> [SOURCE_TEXT_OMITTED sha256=9c74702320cc7d38dbb958d4adf8984609e199f46c5274f2124052f82ffa8fb0]).

**NQ23_MMG007** (optional_gold; `2026 - Chen - Ferrate-assisted nonthermal plasma for efficient PFOA degradation in landfill leachate - Mitigating bulk organic interference and enhancing.pdf`, chunk `35`)
> [SOURCE_TEXT_OMITTED sha256=f6f48434e63810e6135f5782129b27b521b58706a8869e90c95a098df83e030c].

### Normative content claim groups

#### NQ23-G01

- Component: `NQ23-T01`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: Across the cited PFAS degradation studies, multiple distinct energy metrics are used, including electrical energy per order (EEO or EE/O, in kWh per cubic meter or kWh per cubic meter per order of removal) and energy yield in mg removed per kWh, so numerical values reported under different metrics are not directly interchangeable.
- Material qualifiers: ["these metrics include electrical energy per order (EEO or EE/O, reported in kWh per cubic meter or kWh per cubic meter per order of removal)", "some studies report energy yield in mg removed per kWh instead of or in addition to EEO", "because the metrics differ in definition, numerical values reported under different metrics are not directly interchangeable"]
- Evidence: NQ23_MMG001, NQ23_MMG004, NQ23_MMG005
- Prior atomic claims: NQ23-C08
- Full: Full credit if the answer explicitly notes that more than one type of energy metric is used across PFAS degradation studies and correctly identifies at least two distinct types (e.g., EEO/EE/O in kWh per cubic meter or kWh per cubic meter per order, and mg per kWh energy yield), and further states that values from different metrics are not directly interchangeable because they are defined differently.
- Partial: Partial credit if the answer correctly states that multiple distinct metrics are used across studies OR correctly names at least two of the specific metrics but does not clearly state that these differing definitions limit direct numerical comparability; or if it only alludes vaguely to 'different normalization methods' without naming any concrete metrics.
- Contradiction: Mark as contradicted if the answer asserts or clearly implies that all studies use a single, common energy metric, or that numerical energy values from different metrics are directly interchangeable without qualification.

#### NQ23-G02

- Component: `NQ23-T01`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: In hydrodynamic cavitation treatment of PFOS-contaminated water, electrical energy per order (EEO) ranged from 7 to 598 kWh/m³ per order, and the energy yield ranged between 17 and 286 mg per kWh, indicating a wide spread in reported energy efficiency under different conditions.
- Material qualifiers: ["the process is hydrodynamic cavitation applied to PFOS in water", "EEO values range from 7 to 598 kWh/m³ per order", "energy yield values range from 17 to 286 mg per kWh", "the ranges reflect variation under different experimental conditions within the study"]
- Evidence: NQ23_MMG004
- Prior atomic claims: NQ23-C04
- Full: Full credit if the answer: (1) identifies hydrodynamic cavitation of PFOS in water; (2) correctly reports that EEO ranges approximately from 7 to 598 kWh per cubic meter per order; and (3) correctly reports that energy yield ranges approximately from 17 to 286 mg per kWh. Minor formatting differences in units or range delimiters are acceptable as long as the numeric ranges and units are semantically equivalent.
- Partial: Partial credit if hydrodynamic cavitation of PFOS is correctly identified and at least one of the two ranges (EEO or energy yield) is correctly given with the right order of magnitude and units, but the other range is omitted or misstated; or if both metrics are mentioned but the numeric ranges are incomplete (e.g., only the lower or upper bound is given correctly).
- Contradiction: Mark as contradicted if the answer attributes clearly incompatible numeric ranges to hydrodynamic cavitation of PFOS (e.g., claiming EEO is consistently below 1 kWh/m³/order or above 1000 kWh/m³/order, or that energy yield is outside the 10–300 mg/kWh scale) or if it asserts that this study reports only a single fixed value instead of a range.

#### NQ23-G03

- Component: `NQ23-T01`
- Importance: `supplementary`
- Function: `affirmative`
- Scoring role: `optional_content`
- Proposition: For PFAS degradation in wastewater using N₂ nonthermal plasma, reported EEO values were 370 kWh/m³ for PFOA and 260 kWh/m³ for PFDA, with corresponding degradation efficiencies of 45% for PFOA and 60% for PFDA.
- Material qualifiers: ["the process is N₂ nonthermal plasma applied to wastewater containing PFOA and PFDA", "EEO is 370 kWh/m³ for PFOA", "EEO is 260 kWh/m³ for PFDA", "the corresponding degradation efficiencies are 45% for PFOA and 60% for PFDA"]
- Evidence: NQ23_MMG005
- Prior atomic claims: NQ23-C05
- Full: Full credit if the answer attributes to N₂ nonthermal plasma in wastewater both EEO values (about 370 kWh/m³ for PFOA and about 260 kWh/m³ for PFDA) and the corresponding degradation efficiencies (about 45% and 60%, respectively), with correct compound-to-value pairing.
- Partial: Partial credit if the answer correctly identifies N₂ nonthermal plasma in wastewater and mentions at least one of the EEO values or at least one of the efficiencies with the right order of magnitude and compound pairing, but omits the others; or if it gives all four values but slightly misstates one percentage or EEO figure while the qualitative high-energy, partial-removal picture remains correct.
- Contradiction: Mark as contradicted if the answer swaps the EEO values or efficiencies between PFOA and PFDA, or asserts values that are clearly incompatible in magnitude (e.g., claiming EEO below 100 kWh/m³ for both compounds or efficiencies near 100%) for this specific study.

#### NQ23-G04

- Component: `NQ23-T01`
- Importance: `supplementary`
- Function: `affirmative`
- Scoring role: `optional_content`
- Proposition: A state-of-the-art review of non-thermal plasma (NTP) technologies for PFAS-contaminated water reports that, when energy consumption is evaluated as electrical energy per order (EEO), NTP processes fall in a central zone with median energy consumptions in the range of 1–100 kWh/m³, at approximately the same level as photo-Fenton and pure electrolytic advanced oxidation processes.
- Material qualifiers: ["the processes are non-thermal plasma (NTP) technologies applied to water treatment, including PFAS-contaminated water", "energy consumption is evaluated as electrical energy per order (EEO)", "median EEO values fall in the range of 1–100 kWh/m³", "this energy-consumption range is described as a central zone and is comparable to photo-Fenton and pure electrolytic AOPs"]
- Evidence: NQ23_MMG001
- Prior atomic claims: NQ23-C01
- Full: Full credit if the answer notes that a review places non-thermal plasma processes in a 'central zone' with median EEO values on the order of 1–100 kWh per cubic meter and that this is comparable to photo-Fenton and pure electrolytic advanced oxidation processes.
- Partial: Partial credit if the answer correctly gives the approximate 1–100 kWh/m³ EEO range for NTP but omits either the 'median' qualifier or the comparison to photo-Fenton and electrolytic AOPs; or if it mentions a central-zone EEO range qualitatively without exact bounds (e.g., 'tens of kWh/m³') but clearly ties it to NTP and EEO.
- Contradiction: Mark as contradicted if the answer claims that NTP EEO values are consistently outside the 1–100 kWh/m³ range (e.g., always below 1 or above 1000 kWh/m³) or asserts that NTP is far more energy-intensive or far more efficient than photo-Fenton and pure electrolytic AOPs contrary to being at the same level.

#### NQ23-G06

- Component: `NQ23-T01`
- Importance: `supplementary`
- Function: `affirmative`
- Scoring role: `optional_content`
- Proposition: In a field pilot-scale plasma reactor treating groundwater contaminated with PFOA and PFOS, EE/O is defined as the electrical energy consumed by the high-voltage power supplies, gas and liquid pumps, and rotating spark gap, divided by the treated volume and normalized to the change from initial to final concentrations (driven below the USEPA health advisory level).
- Material qualifiers: ["the process is a field pilot-scale plasma reactor treating groundwater containing PFOA and PFOS", "E is the energy consumed by high-voltage power supplies, gas and liquid pumps, and rotating spark gap", "V is the treatment volume for each experimental condition", "Ci and Cf are the initial and final concentrations of PFOA and PFOS, with Cf below the USEPA health advisory level", "EE/O is calculated from E, V, Ci, and Cf"]
- Evidence: NQ23_MMG002
- Prior atomic claims: NQ23-C02
- Full: Full credit if the answer describes that the pilot plasma groundwater study defines EE/O from the total electrical energy used by the reactor’s power supplies, gas and liquid pumps, and rotating spark gap, divided by the treated volume and related to the reduction from initial to final PFOA and PFOS concentrations down to below the USEPA health advisory level.
- Partial: Partial credit if the answer mentions that EE/O in this pilot plasma study is based on total electrical energy input and treated volume but omits mention of one of the components (e.g., pumps or spark gap) or omits the health-advisory-level endpoint, while still correctly conveying that EE/O is defined from E, V, Ci, and Cf.
- Contradiction: Mark as contradicted if the answer claims that EE/O in this study excludes major electrical components (e.g., says it counts only plasma power and not pumps) or that it is unrelated to concentration reduction (e.g., defined solely as energy per time).

#### NQ23-G07

- Component: `NQ23-T01`
- Importance: `supplementary`
- Function: `affirmative`
- Scoring role: `optional_content`
- Proposition: In a pilot-scale electrochemical oxidation study treating PFAS-contaminated water and fractionated foam, the authors state that energy consumption can be calculated according to a previously described method and an equation presented as eq S18, without providing specific energy values in the cited excerpt.
- Material qualifiers: ["the process is electrochemical oxidation applied to PFAS-contaminated water and fractionated foam", "energy consumption is said to be calculable as described previously and in eq S18", "no explicit kWh/m³ or related numeric values appear in the cited sentence"]
- Evidence: NQ23_MMG003
- Prior atomic claims: NQ23-C03
- Full: Full credit if the answer notes that the electrochemical oxidation pilot study references a specific method or equation (eq S18) for calculating energy consumption, but does not itself provide explicit numeric energy-consumption values in the quoted text.
- Partial: Partial credit if the answer correctly notes that the EO study discusses an energy-consumption calculation method but omits mention of the equation reference, while not incorrectly inventing numeric values.
- Contradiction: Mark as contradicted if the answer attributes specific numeric energy-consumption values (e.g., kWh/m³ numbers) to this EO excerpt as though they appear in the text, or states that no energy-consumption calculation is mentioned for EO.

#### NQ23-G08

- Component: `NQ23-T02`
- Importance: `core`
- Function: `limitation`
- Scoring role: `required_content`
- Proposition: A review of PFAS destruction technologies in water and wastewater observes that the reported energy-related ranges show high variability, reflecting uncertainty and nonuniform experimental conditions across studies, which limits straightforward cross-study comparison of energy-consumption or efficiency values.
- Material qualifiers: ["the observation comes from a review of various PFAS destruction technologies in water and wastewater", "the high variability reflects uncertainty and nonuniformity of experimental conditions among the studies summarized", "this variability and nonuniformity constrain straightforward cross-study comparison of energy-consumption or efficiency values"]
- Evidence: NQ23_MMG006
- Prior atomic claims: NQ23-C06
- Full: Full credit if the answer states that energy-related values across PFAS destruction studies vary widely and that this is attributed to uncertain and nonuniform experimental conditions, and explicitly links this variability to limitations on straightforward or direct cross-study comparisons.
- Partial: Partial credit if the answer correctly notes high variability or nonuniform experimental conditions but does not clearly connect this to limits on comparability, or if it states that comparisons are difficult without specifying that variability and nonuniform conditions are the reason.
- Contradiction: Mark as contradicted if the answer claims that energy-related values are generally consistent across studies or that experimental conditions are uniform enough to allow simple, unqualified comparison of energy values.

#### NQ23-G09

- Component: `NQ23-T02`
- Importance: `core`
- Function: `limitation`
- Scoring role: `required_content`
- Proposition: A consolidated comparison presented reported EE/O values together with water type, initial PFAS concentration, reactor scale, reaction time, and removal or defluorination efficiency to support transparent, context-aware evaluation across technologies.
- Material qualifiers: ["the source describes a consolidated comparison in Table S1", "listed context includes water type, concentration, scale, time, and removal or defluorination efficiency", "the source supports context-aware comparison but does not state that comparison is impossible without every field"]
- Evidence: NQ23_MMG007
- Prior atomic claims: NQ23-C07
- Full: Award full if the answer says the source paired EE/O with key experimental parameters to support transparent context-aware comparison, without making the absolute claim that every comparison lacking all fields is meaningless.
- Partial: Award partial if the answer generally recommends contextualizing EE/O but omits most of the listed parameters.
- Contradiction: Mark contradicted if the answer says EE/O values are directly comparable without experimental context or claims the source proved comparison is impossible unless every listed field is present.

#### NQ23-G10

- Component: `NQ23-T02`
- Importance: `supplementary`
- Function: `limitation`
- Scoring role: `optional_content`
- Proposition: Taken together, the different energy metrics, broad reported ranges, nonuniform conditions, and use of contextual comparison tables indicate that no single energy-consumption value represents all PFAS degradation methods.
- Material qualifiers: ["this conclusion is based on the wide spread of reported energy metrics, from single-digit to several-hundred kWh/m³ or kWh/m³/order, and the use of different metrics such as EEO and mg/kWh", "high variability and nonuniform experimental conditions across studies contribute to this limitation", "meaningful comparison requires considering experimental context, including parameters such as water type, initial concentration, reactor scale, reaction time, and performance endpoints"]
- Evidence: NQ23_MMG001, NQ23_MMG004, NQ23_MMG005, NQ23_MMG006, NQ23_MMG007
- Prior atomic claims: NQ23-C10
- Full: Award optional full credit if the answer synthesizes metric differences, variability, and contextual conditions into a non-universal conclusion.
- Partial: Award optional partial credit if the answer gives the non-universal conclusion with only one supporting reason.
- Contradiction: Mark contradicted if the answer proposes one universal energy-consumption value for all PFAS degradation methods.


### Prior atomic-claim dispositions

#### NQ23-C01

- Prior claim: Non-thermal plasma (NTP) processes for PFAS-contaminated water have median energy consumptions, expressed as electrical energy per order (EEO), in the range of 1–100 kWh/m³, placing them in a central zone of energy demand comparable to photo-Fenton and pure electrolytic advanced oxidation processes.
- Action: `mapped`
- Final target(s): NQ23-G04
- Rationale: The claim about NTP median EEO values and their comparability to photo-Fenton and electrolytic AOPs is fully supported by NQ23_MMG001 and is retained as an optional, study-specific energy-evidence group.

#### NQ23-C02

- Prior claim: In a field pilot-scale plasma reactor treating groundwater contaminated with PFOA and PFOS, the reported EE/O values ranged from 9.2 to 31 kWh/m³, with an average of 16 ± 5.8 kWh/m³ across four treatment conditions, based on the total energy consumed by the power supplies, pumps, and rotating spark gap normalized to treated volume and concentration reduction.
- Action: `revised`
- Final target(s): NQ23-G06
- Rationale: The original claim included specific EE/O numeric values and an average that are not present in the exact_evidence_span of NQ23_MMG002. It has been revised to focus only on the supported definition of EE/O (total energy components, volume, and concentration change), dropping the unsupported numeric range and average.

#### NQ23-C03

- Prior claim: A pilot-scale electrochemical oxidation study treating PFAS-contaminated water and fractionated foam reported total specific energy consumptions after 9 hours of treatment of approximately 270 kWh/m³ for experiments treating 50 L and 93 kWh/m³ for experiments treating 150 L, with energy use described as mostly dependent on treated volume rather than normalized per order of removal.
- Action: `revised`
- Final target(s): NQ23-G07
- Rationale: The original claim cited specific numeric kWh/m³ values and a 9 h treatment duration that are not in the supplied excerpt for NQ23_MMG003. The revised group retains only the supported methodological statement that EO energy consumption can be calculated using a referenced equation, without asserting numeric outcomes.

#### NQ23-C04

- Prior claim: In hydrodynamic cavitation treatment of PFOS-contaminated water, the reported electrical energy per order (EEO) ranged from 7 to 598 kWh/m³/order, while the energy yield ranged between 17 and 286 mg of PFOS treated per kWh, indicating a wide spread in energy efficiency under different conditions.
- Action: `mapped`
- Final target(s): NQ23-G02
- Rationale: The hydrodynamic cavitation EEO and energy-yield ranges and their interpretation as a wide efficiency spread are directly supported by NQ23_MMG004 and are preserved as a core numeric example.

#### NQ23-C05

- Prior claim: For PFAS degradation in wastewater using N₂ nonthermal plasma, EEO values of 370 kWh/m³ for PFOA and 260 kWh/m³ for PFDA were reported, with corresponding degradation efficiencies of 45% for PFOA and 60% for PFDA, illustrating relatively high energy consumption per treated volume for partial degradation.
- Action: `mapped`
- Final target(s): NQ23-G03
- Rationale: The N₂ nonthermal plasma EEO values and associated degradation efficiencies are exactly supported by NQ23_MMG005 and are retained as an optional detailed study example.

#### NQ23-C06

- Prior claim: A review of PFAS destruction technologies in water and wastewater notes that reported energy-related ranges across studies show high variability, reflecting uncertainty and nonuniform experimental conditions, which limits straightforward cross-study comparison of energy-consumption or efficiency values.
- Action: `revised`
- Final target(s): NQ23-G08
- Rationale: The content of C06 is supported by NQ23_MMG006 but functions as a limitation about variability and comparability rather than a primary numeric finding. It is reclassified and slightly reframed as a core limitation claim in G08 for the cross-study-comparison component.

#### NQ23-C07

- Prior claim: Another study emphasizes that a consolidated comparison of reported EE/O values for different PFAS treatment technologies is only meaningful when presented together with key experimental parameters such as water type, initial PFAS concentration, reactor scale, reaction time, and removal or defluorination efficiency, to enable transparent and context-aware evaluation across technologies.
- Action: `revised`
- Final target(s): NQ23-G09
- Rationale: The content is supported by NQ23_MMG007 but is better treated as a limitation/supporting condition for meaningful EE/O comparisons. It has been retained with essentially the same substance but reclassified and aligned to the comparability component.

#### NQ23-C08

- Prior claim: The PFAS energy-efficiency evidence base uses multiple distinct metrics, including electrical energy per order (EEO or EE/O, kWh/m³), simple specific energy consumption per volume (kWh/m³), and energy yield (mg/kWh), so numerical values drawn from different metrics cannot be directly equated without accounting for how each is defined.
- Action: `mapped`
- Final target(s): NQ23-G01
- Rationale: C08 synthesizes the use of multiple energy metrics across studies; this synthesis is maintained in G01, which is now a core required-content group for identifying metrics across methods.

#### NQ23-C09

- Prior claim: Reported energy-consumption or efficiency values for PFAS degradation span from single-digit kWh/m³/order in some hydrodynamic cavitation conditions to several hundred kWh/m³ in N₂ nonthermal plasma and high end hydrodynamic cavitation cases, underscoring the wide variability in energy demand across technologies and operating conditions.
- Action: `deleted`
- Final target(s): (deleted)
- Rationale: C09’s synthesis that reported values span from single-digit to several-hundred kWh/m³(/order) is now fully entailed by the separate numeric example groups for hydrodynamic cavitation (G02) and N₂ plasma (G03), so a standalone synthesis group based on the same evidence would be redundant.

#### NQ23-C10

- Prior claim: Because of the high variability in reported energy ranges and the nonuniform experimental conditions across PFAS treatment studies, along with the use of different energy metrics, no single universal energy-consumption value can fairly represent all PFAS degradation methods, and cross-study comparisons must be interpreted in the specific context of each experiment.
- Action: `revised`
- Final target(s): NQ23-G10, NQ23-B01
- Rationale: C10’s conclusion that no universal energy-consumption value can represent all PFAS methods, and that context is needed for comparisons, is retained in G10 as a core limitation synthesis and also informs the explicit boundary-constraint group B01. The weak linkage to NQ23_MMG003 has been dropped, relying instead on directly supportive variability and context evidence.

### Constraint-only groups

- `NQ23-B01`: The answer must not claim that one universal energy-consumption number fairly represents all PFAS degradation methods.
  Violation rule: Flag a boundary violation if the answer proposes or endorses a single universal or representative numerical energy-consumption or energy-efficiency value as fairly describing all PFAS degradation methods, without emphasizing method- and condition-specific variability.

### Model B verification

Overall verdict: **approve**

- `NQ23-G01`: **supported**. Spans for MMG001 (EEO kWh/m3), MMG004 (EEO kWh/m3/order and mg/kWh energy yield), and MMG005 (EEO kWh/m3) jointly entail that multiple distinct metrics are reported; the non-interchangeability inference is a reasonable, appropriately flagged synthesis rather than an unsupported leap.
  Recommended change: None.
- `NQ23-G02`: **supported**. EEO 7-598 kWh/m3/order and energy yield 17-286 mg/kWh are quoted verbatim in the span; numeric equivalence list is claim-specific and correctly scoped.
  Recommended change: None.
- `NQ23-G03`: **supported**. EEO 370/260 kWh/m3 and efficiencies 45%/60% with correct PFOA/PFDA pairing are directly quoted.
  Recommended change: None.
- `NQ23-G04`: **supported**. Median EEO 1-100 kWh/m3 range and comparison to photo-Fenton/electrolytic AOPs are directly quoted; correctly scoped as study-specific (supplementary), not universalized.
  Recommended change: None.
- `NQ23-G06`: **supported**. Correctly resolves the prior Model B flag on C02 by dropping the unsupported 9.2-31/16±5.8 numeric range and retaining only the EE/O definition (E, V, Ci, Cf) that is actually present in the span.
  Recommended change: None.
- `NQ23-G07`: **supported**. Correctly resolves the prior Model B flag on C03 by dropping the unsupported 270/93 kWh/m3 figures and retaining only the eq S18 methodological pointer present in the span.
  Recommended change: None.
- `NQ23-G08`: **supported**. Variability/nonuniformity statement is directly quoted; the added 'limits comparison' clause is grounded in the same evidence record's own does_not_support annotation, not an invented inference.
  Recommended change: None.
- `NQ23-G09`: **supported**. Table S1 consolidated-comparison statement is directly quoted; qualifier explicitly avoids overclaiming that all listed fields are mandatory for any valid comparison.
  Recommended change: None.
- `NQ23-G10`: **supported**. Correctly resolves prior flag on C10 by dropping the weak NQ23_MMG003 linkage; synthesis is appropriately marked optional_content and synthesis_required, avoiding overclaiming as core required content.
  Recommended change: None.
- `NQ23-B01`: **supported**. Boundary proposition directly mirrors the frozen must_not_claim text; violation_rule is executable and the group is correctly marked constraint_only, excluded from coverage denominator per criterion 10.
  Recommended change: None.

Human-review priorities:
- G02 (hydrodynamic cavitation) is core/required_content while G03 (N2 plasma) and G04 (NTP) are supplementary/optional_content despite all three being equally verbatim-supported numeric examples from required_gold evidence; defensible since G01/G10 already cover generic metric identification, but worth a project-author sanity check on emphasis.
- G09's sole evidence record (NQ23_MMG007) is optional_gold in the raw gold set yet the claim group is scored core/required_content; justified by centrality to the T02 comparability requirement, but flag for author confirmation.
- Whether NQ23_MMG002's and NQ23_MMG003's source PDFs contain the EE/O numeric range/average (9.2-31, avg 16±5.8 kWh/m3) and EO totals (270/93 kWh/m3) elsewhere (e.g., results tables) remains unresolved for full document review; the ledger no longer depends on these unverified numbers for scoring, so this is documented in unresolved_or_unsupported and does not block approval.
- G10 (optional_content) and B01 (constraint_only) both draw on the same 'no universal value' theme and partly overlapping evidence (NQ23_MMG006); confirm in the downstream scoring implementation that constraint_only groups are truly excluded from the coverage denominator so no unintended double credit occurs.

### Non-normative reference prose

PFAS degradation studies report non-interchangeable energy metrics, including electrical energy per order in kWh/m3 or kWh/m3/order and energy yield in mg/kWh. A hydrodynamic-cavitation PFOS study reported EEO values of 7-598 kWh/m3/order and energy yields of 17-286 mg/kWh, while other plasma examples reported different ranges and compound-specific values. Pilot examples also differ in how energy is defined or reported, including explicit equipment loads or a referenced calculation equation without values in the selected excerpt. A review attributes the broad ranges to uncertainty and nonuniform experimental conditions, which limits direct cross-study comparison. Another comparison paired EE/O with water type, initial PFAS concentration, reactor scale, reaction time, and removal or defluorination efficiency to support transparent context-aware interpretation. Consequently, no single energy-consumption number represents all PFAS degradation methods.

### Prose-to-ledger map

- PFAS degradation studies report non-interchangeable energy metrics, including electrical energy per order in kWh/m3 or kWh/m3/order and energy yield in mg/kWh. -> NQ23-G01
- A hydrodynamic-cavitation PFOS study reported EEO values of 7-598 kWh/m3/order and energy yields of 17-286 mg/kWh, while other plasma examples reported different ranges and compound-specific values. -> NQ23-G02, NQ23-G03, NQ23-G04
- Pilot examples also differ in how energy is defined or reported, including explicit equipment loads or a referenced calculation equation without values in the selected excerpt. -> NQ23-G06, NQ23-G07
- A review attributes the broad ranges to uncertainty and nonuniform experimental conditions, which limits direct cross-study comparison. -> NQ23-G08
- Another comparison paired EE/O with water type, initial PFAS concentration, reactor scale, reaction time, and removal or defluorination efficiency to support transparent context-aware interpretation. -> NQ23-G09
- Consequently, no single energy-consumption number represents all PFAS degradation methods. -> NQ23-G10, NQ23-B01

---

## NQ24

**Question:** How do reported activated-carbon PFAS adsorption capacities differ between batch and column studies?

**Must include:** Must distinguish carbon type, PFAS chain length or compound, test conditions, endpoint, capacity units, and capacity values when values are presented.

**Must not claim:** Must not claim activated carbon has one fixed PFAS adsorption capacity across compounds and matrices.

### Frozen task components

- `NQ24-T01`: Describe activated-carbon PFAS adsorption capacities reported from batch studies.
- `NQ24-T02`: Describe capacities or performance measures reported from column studies.
- `NQ24-T03`: Explain the conditions and unit differences that limit direct comparison between batch and column results.

### Complete gold evidence

**NQ24_MMG001** (required_gold; `2023 - Shaikh - PFOA remediation from aqueous media using CTAB impregnated activated carbon - A closed-loop sustainable study with comprehensive selectivity analysis.pdf`, chunk `60`)
> [SOURCE_TEXT_OMITTED sha256=8a2066fbeea08688bf57fa41b3f0688afb1b08ea133d3c4cf9e11bfd54f3a9c2]).

**NQ24_L3CTX001** (l3_source_context_pending_author_confirmation; `2023 - Shaikh - PFOA remediation from aqueous media using CTAB impregnated activated carbon - A closed-loop sustainable study with comprehensive selectivity analysis.pdf`, chunk `0`)
> [SOURCE_TEXT_OMITTED sha256=e37220601557ee34859fd7d4c8b496ffffe0928d782e63073f106ee6455051a9].

### Normative content claim groups

#### NQ24-G01

- Component: `NQ24-T01`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: In a batch equilibrium study of PFOA adsorption onto CTAB‑impregnated activated carbon in aqueous media, the Langmuir isotherm maximum adsorption capacity (Qe) was 6.85 mg/g, with adsorbent particle sizes of 125–250 μm.
- Material qualifiers: ["measured in batch equilibrium conditions using a Langmuir isotherm model", "PFAS compound was PFOA", "adsorbent was CTAB‑impregnated activated carbon", "adsorbent particle size in batch was 125–250 μm", "endpoint reported in mg/g"]
- Evidence: NQ24_L3CTX001, NQ24_MMG001
- Prior atomic claims: 
- Full: Award full credit if the answer states that, in batch equilibrium conditions for PFOA adsorption onto CTAB‑impregnated activated carbon, the Langmuir isotherm maximum adsorption capacity (Qe) was 6.85 mg/g, and makes clear that this value comes from a batch isotherm model applied to that specific PFAS–carbon system. Minor wording differences are acceptable, but the numerical value (6.85), the unit (mg/g), the batch/isotherm context, and identification of PFOA and activated carbon must all be present.
- Partial: Award partial credit if the answer correctly states that the batch Langmuir isotherm capacity for PFOA on activated carbon was higher than the column capacity and gives an approximately correct numeric value (around 6.85 mg/g) OR clearly identifies it as a batch Langmuir Qe for PFOA on CTAB‑impregnated activated carbon, but omits one material qualifier (e.g., does not mention Langmuir explicitly, or omits the mg/g unit) while not introducing any incompatible statement about the batch capacity.
- Contradiction: Mark as contradicted if the answer states an incorrect central proposition (e.g., gives a substantially different batch capacity value, assigns the 6.85 mg/g value to the column instead of batch, or denies that such a batch Langmuir Qe was reported) or otherwise claims that no batch capacity for this system was reported.

#### NQ24-G02

- Component: `NQ24-T02`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: In a fixed‑bed column study of PFOA adsorption onto CTAB‑impregnated activated carbon in aqueous media with a background water matrix, the maximum adsorption capacity estimated by the Thomas model was 5.71 mg/g, using larger adsorbent particles (125–500 μm).
- Material qualifiers: ["measured in a fixed‑bed column using the Thomas breakthrough model", "PFAS compound was PFOA", "adsorbent was CTAB‑impregnated activated carbon", "column run included a background water matrix", "adsorbent particle size in the column was 125–500 μm", "endpoint reported in mg/g"]
- Evidence: NQ24_L3CTX001, NQ24_MMG001
- Prior atomic claims: 
- Full: Award full credit if the answer states that, in a fixed‑bed column experiment for PFOA adsorption onto CTAB‑impregnated activated carbon, the Thomas‑model maximum adsorption capacity was 5.71 mg/g, clearly situating this value in the column/Thomas‑model context for that PFAS–carbon system. Minor wording differences are acceptable, but the numerical value (5.71), the unit (mg/g), the column/Thomas context, and identification of PFOA and activated carbon must all be present.
- Partial: Award partial credit if the answer correctly reports that the column Thomas‑model capacity for PFOA on this activated carbon was lower than the batch capacity and gives an approximately correct numeric value (around 5.71 mg/g) OR clearly identifies 5.71 mg/g as a column Thomas‑model capacity for PFOA on CTAB‑impregnated activated carbon, but omits one material qualifier (e.g., does not mention Thomas by name, or omits the mg/g unit) while not introducing any incompatible statement about the column capacity.
- Contradiction: Mark as contradicted if the answer states an incorrect central proposition (e.g., assigns 5.71 mg/g to the batch instead of the column, gives a substantially different column capacity value, or claims that no column capacity for this system was reported) or asserts that the column capacity exceeded the batch capacity for this specific study.

#### NQ24-G03

- Component: `NQ24-T03`
- Importance: `core`
- Function: `limitation`
- Scoring role: `required_content`
- Proposition: In this single PFOA–CTAB‑impregnated activated carbon study, the modeled column adsorption capacity (5.71 mg/g from the Thomas model) was marginally lower than the modeled batch capacity (6.85 mg/g from the Langmuir isotherm), and the authors mainly attributed this difference to the presence of a background water matrix during the column run and the larger adsorbent particle size used in the column; these study‑specific conditions limit generalization of the batch–column comparison.
- Material qualifiers: ["the batch capacity was 6.85 mg/g from a Langmuir isotherm model", "the column capacity was 5.71 mg/g from a Thomas breakthrough model", "the lower column capacity was mainly attributed to the background water matrix in the column run and larger column particle size", "this finding is limited to a single PFAS–carbon system and does not establish a general rule across activated carbons or PFAS"]
- Evidence: NQ24_L3CTX001, NQ24_MMG001
- Prior atomic claims: NQ24-C01, NQ24-C02
- Full: Award full credit if the answer explains that, in the reported PFOA–CTAB‑impregnated activated carbon study, the column capacity (from a Thomas model) was slightly or marginally lower than the batch capacity (from a Langmuir isotherm), and explicitly cites the study‑reported reasons: competition or effects from a background water matrix during the column run and the use of larger adsorbent particles in the column. The answer must also make clear that this is a single‑system comparison and does not constitute a general rule for all activated carbons or PFAS. Mentioning the exact numeric values or model names strengthens the explanation but is not strictly required for full credit so long as the direction of difference, the two main reasons, and the limited generality are all correct.
- Partial: Award partial credit if the answer correctly conveys that, in the specific study, the column capacity was lower than the batch capacity and attributes this at least to one of the two main reported reasons (background water matrix or larger particle size) OR correctly notes that the comparison is based on different models and conditions that limit generalization, but omits either one of the reasons or does not clearly flag the single‑study/single‑system limitation, while not introducing any incompatible generalization (e.g., not claiming that this pattern holds universally).
- Contradiction: Mark as contradicted if the answer states that, in this PFOA–CTAB‑impregnated activated carbon study, the column capacity was equal to or higher than the batch capacity, or asserts that the observed batch–column relationship and its causes constitute a general rule for activated carbons or PFAS broadly (e.g., claiming that column capacities are always lower than batch capacities for PFAS on activated carbon due to background matrices and particle size).


### Prior atomic-claim dispositions

#### NQ24-C01

- Prior claim: For PFOA adsorption onto CTAB‑impregnated activated carbon, the maximum adsorption capacity obtained from a fixed‑bed column using the Thomas model was 5.71 mg/g, which was marginally lower than the batch equilibrium Langmuir isotherm capacity Qe of 6.85 mg/g.
- Action: `mapped`
- Final target(s): NQ24-G03
- Rationale: The original atomic claim combined the batch Langmuir capacity, the column Thomas capacity, and the explicit statement that the column capacity was marginally lower than the batch capacity. In the final ledger, the comparative relationship between batch and column capacities is captured in claim group G03, so this atomic claim is mapped to G03 as the single best representation of its combined content.

#### NQ24-C02

- Prior claim: In this PFOA–CTAB‑impregnated activated carbon study, the lower column capacity relative to batch was mainly attributed to the presence of a background water matrix during the column run and the larger adsorbent particle size used in the column compared with the batch tests.
- Action: `mapped`
- Final target(s): NQ24-G03
- Rationale: This atomic claim explains the study‑reported reasons for the lower column capacity relative to batch (background water matrix effects and larger particle size in the column), which are fully encoded in claim group G03. It is therefore mapped to G03 as its single target group.

### Constraint-only groups

- `NQ24-B01`: The available evidence does not support claiming a single fixed PFAS adsorption capacity or a universal batch–column capacity relationship for activated carbon across different PFAS compounds, carbon types, and matrices.
  Violation rule: Flag a boundary violation if the answer claims or clearly implies that activated carbon has one fixed PFAS adsorption capacity across compounds and matrices, or that the specific batch–column capacity relationship observed in this PFOA–CTAB‑impregnated activated carbon study (including the numeric values or direction of difference) applies universally to all PFAS or all activated carbons.

### Model B verification

Overall verdict: **approve**

- `NQ24-G01`: **supported**. Batch Langmuir Qe (6.85 mg/g) and batch particle size (125–250 μm) are directly stated in the MMG001 span. NQ24_L3CTX001 is listed as an evidence_id but only supplies redundant compound/adsorbent identity already present in MMG001 context; it adds no unverifiable factual content required for scoring, and its 'pending_project_author_confirmation' status does not affect satisfiability of full_rule since MMG001 alone (retained_after_project_author_review) already entails the full proposition.
  Recommended change: None required for scoring correctness; optionally note in rationale that L3CTX001 is supplementary/non-load-bearing so a reviewer does not mistake it for adding an unconfirmed fact.
- `NQ24-G02`: **supported**. Column Thomas-model Qe (5.71 mg/g), background water matrix, and column particle size (125–500 μm) are directly entailed by the MMG001 span. Same non-load-bearing use of L3CTX001 as in G01.
  Recommended change: None required.
- `NQ24-G03`: **supported**. Direction of difference (column marginally lower than batch), both stated reasons (background water matrix, larger column particle size), and the single-study limitation are all directly entailed by the MMG001 span, matching the gold record's own 'does_not_support' caveat. Correctly absorbs atomic claims C01 and C02 without residual unmapped content.
  Recommended change: None required.
- `NQ24-B01`: **supported**. Correctly scoped as constraint_only/boundary_constraint, excluded from required-content coverage, with an executable violation_rule that flags universalization of the single-study batch–column relationship or claiming one fixed capacity across compounds/matrices — consistent with the must_not_claim boundary and the gold's supports_universal_claim: no flag.
  Recommended change: None required.

Human-review priorities:
- Carried forward: confirm no other frozen gold record for NQ24 exists elsewhere in the corpus with additional batch-vs-column comparisons (other carbon types/PFAS), since G01/G02/G03/B01 all rest on the single MMG001 exact_evidence_span and gold is explicitly non-exhaustive.
- Carried forward judgment call: confirm decomposing this single evidence pair into three core required_content claim groups (vs. a more consolidated structure) matches project scoring-weight conventions for single-data-point numeric_extraction questions.
- Carried forward judgment call: verify the 'partially_supported' answerability label matches project convention where the single instance is fully supported but generalization is not possible.
- Non-blocking wording nitpick carried forward: in G01/G02 material_qualifiers, 'endpoint reported in mg/g' conflates endpoint (capacity) with unit (mg/g); scoring rules are unaffected since full_rule requires both independently.
- New observation, non-blocking: NQ24_L3CTX001 is tagged 'author_review_decision: pending_project_author_confirmation' (unlike MMG001's 'retained_after_project_author_review'), and its inclusion as an evidence_id in G01/G02/G03/B01 is purely supplementary (redundant identity context) rather than load-bearing for any required qualifier or numeric value; project author may want to explicitly confirm or drop this pending citation for cleanliness, though it does not currently affect scoring correctness.

### Non-normative reference prose

The source study concerns PFOA adsorption from aqueous media using CTAB-impregnated activated carbon. Its batch Langmuir result was 6.85 mg/g with 125-250 um particles. Its fixed-bed Thomas-model result was 5.71 mg/g with 125-500 um particles and a background water matrix. The authors attributed the marginally lower column value mainly to the background matrix and larger particles, so the two modeled capacities are study-specific and do not define a universal batch-column relationship.

### Prose-to-ledger map

- The source study concerns PFOA adsorption from aqueous media using CTAB-impregnated activated carbon. -> NQ24-G01, NQ24-G02, NQ24-G03
- Its batch Langmuir result was 6.85 mg/g with 125-250 um particles. -> NQ24-G01
- Its fixed-bed Thomas-model result was 5.71 mg/g with 125-500 um particles and a background water matrix. -> NQ24-G02
- The authors attributed the marginally lower column value mainly to the background matrix and larger particles, so the two modeled capacities are study-specific and do not define a universal batch-column relationship. -> NQ24-G03, NQ24-B01

---

## NQ26

**Question:** What membrane-based PFAS treatment routes are described, and which routes separate or concentrate PFAS rather than destroy or transform them?

**Must include:** Must distinguish pressure-driven separation, NF/RO, modified membranes, electrical membranes, and any destructive membrane-coupled process.

**Must not claim:** Must not equate membrane separation or retention with PFAS destruction.

### Frozen task components

- `NQ26-T01`: Describe the membrane-based PFAS treatment routes represented in the evidence.
- `NQ26-T02`: Distinguish routes that separate or concentrate PFAS from routes that transform or destroy PFAS.

### Complete gold evidence

**NQ26_MMG001** (required_gold; `2022 - Liang - Field demonstration of coupling ion-exchange resin with electrochemical oxidation for enhanced treatment of per- and polyfluoroalkyl substances.pdf`, chunk `35`)
> [SOURCE_TEXT_OMITTED sha256=03339764a1bb7d62ce6bf604ab3e477cc1f3961390fa4d7ccaca7b6047668851] ].

**NQ26_MMG002** (required_gold; `2025 - Liu - Filtration and electrical membrane-based treatment methods for PFAS-contaminated water and preparation methods for the membranes employed.pdf`, chunk `21`)
> [SOURCE_TEXT_OMITTED sha256=83cad68bd45d2078d6111dab03fa6fe6edf58ebe23a550abae1a931d9038d69b].

**NQ26_MMG003** (required_gold; `2023 - Sivagami - Electrochemical-based approaches for the treatment of forever chemicals - Removal of perfluoroalkyl and polyfluoroalkyl substances (PFAS) from.pdf`, chunk `58`)
> Another severe limitation of membrane-based processes is that they do not degrade PFAS;

**NQ26_MMG004** (required_gold; `2024 - Pervez - Structure and mechanism of nanoengineered membranes toward per- and polyfluoroalkyl substances (PFAS) removal from water - A critical review.pdf`, chunk `4`)
> [SOURCE_TEXT_OMITTED sha256=1c93c6bbc04d9e9b8e5fb4c698395a40b38ca869ce2ce319f451e9e4e5d0a23b] ].

**NQ26_MMG005** (required_gold; `2025 - Liu - Filtration and electrical membrane-based treatment methods for PFAS-contaminated water and preparation methods for the membranes employed.pdf`, chunk `43`)
> [SOURCE_TEXT_OMITTED sha256=9f34e97314f422560b564640d3916e33d8a593d42ff92ca15f3ea9c5a242ec23].

**NQ26_MMG006** (optional_gold; `2025 - Liu - Filtration and electrical membrane-based treatment methods for PFAS-contaminated water and preparation methods for the membranes employed.pdf`, chunk `21`)
> [SOURCE_TEXT_OMITTED sha256=f0b14257912b476dc875c738a98322b9a4eb2b8a25724c454b691b321ced0646].

**NQ26_MMG007** (negative_gold; `2021 - Ryan - Electrochemical technologies for per- and polyfluoroalkyl substances mitigation in.pdf`, chunk `51`)
> [SOURCE_TEXT_OMITTED sha256=efac268ac1e59907dde01bf057d08de85e3cf7451a581ce00c8ee059a00566a0];

**NQ26_MMG008** (optional_gold; `2021 - Groele - An investigation of plasma-driven decomposition of per- and polyfluoroalkyl substances (PFAS) in raw contaminated groundwater.pdf`, chunk `7`)
> [SOURCE_TEXT_OMITTED sha256=7dbda52a0949419af622b6a207b79e15153cbde0e9b684ab90530f14e23c146b].

### Normative content claim groups

#### NQ26-G01

- Component: `NQ26-T01`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: High-pressure membrane filtration using nanoporous nanofiltration (NF) and reverse osmosis (RO) is described as a traditional separation route that effectively separates PFAS from water, achieving high rejection of both short- and long-chain PFAS and producing a concentrated PFAS waste stream.
- Material qualifiers: ["the membranes are nanoporous, high-pressure NF and RO", "they separate both short- and long-chain PFAS with typically high rejection performance", "the outcome is a concentrated PFAS waste stream (not destruction) that may require further treatment"]
- Evidence: NQ26_MMG001, NQ26_MMG004
- Prior atomic claims: NQ26-C01, NQ26-C05
- Full: Count as full if the answer describes NF and RO as high-pressure (or equivalently framed) membrane separation processes using nanoporous membranes that (i) effectively separate PFAS from water, including both short- and long-chain PFAS, and (ii) generate a concentrated PFAS waste stream rather than destroying PFAS. Mention of high rejection performance must be present but need not specify an exact percentage.
- Partial: Count as partial if NF and RO are correctly described as membrane-based separation processes that remove PFAS and generate a concentrated waste stream, but the answer omits either the short- vs long-chain breadth or the idea of high/strong rejection performance, or it fails to identify them as traditional/high-pressure or nanoporous. Do not award partial if NF/RO are described as primarily destructive rather than separative.
- Contradiction: Mark as contradicted if the answer asserts that NF or RO primarily destroy or chemically degrade PFAS (rather than separate and concentrate them), or denies that they function as separation processes for PFAS.

#### NQ26-G02

- Component: `NQ26-T01`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: Filtration, membrane distillation, and forward osmosis are described as membrane-based concentration or separation treatments for PFAS-contaminated water that only concentrate PFAS rather than degrade them.
- Material qualifiers: ["the treatments are applied to PFAS-contaminated water", "they are characterized as concentration (or separation) methods", "they are explicitly distinguished from degradation methods and are said to only concentrate PFAS, not degrade them"]
- Evidence: NQ26_MMG002, NQ26_MMG005
- Prior atomic claims: NQ26-C02, NQ26-C03
- Full: Count as full if the answer groups filtration, membrane distillation, and forward osmosis as membrane-related PFAS treatment routes that are concentration or separation methods which only concentrate PFAS and are not themselves degradative, and notes that they are distinguished from degradation treatments.
- Partial: Count as partial if at least two of the three routes (filtration, membrane distillation, forward osmosis) are correctly identified as concentration/separation methods that do not degrade PFAS, but one route is omitted or the explicit contrast with degradation methods is missing. Do not award partial if any of these methods are described as inherently destructive or degradative for PFAS.
- Contradiction: Mark as contradicted if the answer claims that filtration, membrane distillation, or forward osmosis inherently destroy, chemically transform, or degrade PFAS rather than mainly concentrating or separating them.

#### NQ26-G03

- Component: `NQ26-T01`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: A membrane-assisted degradation route is described in which PFAS are first adsorbed onto a membrane, which may contain catalysts, and then degraded under light or an applied electric field.
- Material qualifiers: ["the membrane can have catalysts added", "the degradation step is driven by light or an applied electric field", "this route differs from simple separation because it includes a degradation step after adsorption"]
- Evidence: NQ26_MMG006
- Prior atomic claims: NQ26-C04, NQ26-C06
- Full: Count as full if the answer clearly describes a membrane-assisted degradation route where PFAS are first adsorbed on a membrane and subsequently degraded, and mentions at least one of the driving conditions (light or electric field) or the possible presence of catalysts on the membrane.
- Partial: Count as partial if the answer mentions membrane-assisted degradation involving PFAS adsorption onto a membrane followed by degradation, but omits both catalysts and the specific driving conditions (light or electric field), or only vaguely implies an external stimulus without specifying light or electric field.
- Contradiction: Mark as contradicted if the answer denies the existence of any membrane-coupled route that both concentrates and then degrades PFAS, or describes the so-called membrane-assisted degradation route as purely separative without any degradation step.

#### NQ26-G05

- Component: `NQ26-T02`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: Membrane routes that concentrate PFAS are discussed as being paired with separate destruction or degradation technologies in two ways: (i) NF/RO have already been demonstrated in tandem with a destruction technology, and (ii) combining other concentration treatments such as filtration, membrane distillation, and forward osmosis with degradation treatments like electrodegradation or biodegradation is recommended as a future research direction.
- Material qualifiers: ["NF/RO are traditional separation technologies that produce a concentrated PFAS waste stream and have been demonstrated in tandem with a destruction technology", "filtration, membrane distillation, and forward osmosis are identified as concentration treatments", "combining these latter concentration treatments with degradation processes such as electrodegradation or biodegradation is framed as a recommendation for future research rather than established current practice", "in all cases, the membrane stage concentrates PFAS and a separate, non-membrane stage provides destruction or degradation"]
- Evidence: NQ26_MMG001, NQ26_MMG005
- Prior atomic claims: NQ26-C02, NQ26-C05
- Full: Count as full if the answer explains both that (a) NF/RO (or equivalently framed high-pressure NF/RO separation) have been demonstrated in tandem with a destruction technology, and (b) that combining other concentration treatments such as filtration, membrane distillation, or forward osmosis with degradation treatments like electrodegradation or biodegradation is presented as a recommended or proposed research direction, not as already-established practice. The answer must make clear that the membrane step concentrates PFAS while a separate step achieves destruction or degradation.
- Partial: Count as partial if the answer correctly states either that NF/RO have been demonstrated in tandem with a destruction technology, or that pairing concentration treatments (filtration, membrane distillation, forward osmosis) with degradation processes is recommended or proposed, but does not clearly cover both aspects or blurs the demonstrated-vs-recommended distinction. Do not award partial if the answer implies that filtration, membrane distillation, or forward osmosis are already routinely operated in combined systems with degradation technologies when the text clearly frames this as future research.
- Contradiction: Mark as contradicted if the answer claims that concentrating membrane routes alone are sufficient to destroy PFAS without any additional degradation or destruction technology, or explicitly denies that NF/RO have been demonstrated in tandem with destruction technologies, or mischaracterizes clearly future-oriented recommendations as current, widely established practice.

#### NQ26-G06

- Component: `NQ26-T02`
- Importance: `supplementary`
- Function: `negative_finding`
- Scoring role: `optional_content`
- Proposition: Low-pressure membrane processes such as microfiltration and ultrafiltration are reported to poorly remove PFAS and are therefore not effective PFAS separation or concentration routes compared with high-pressure membranes.
- Material qualifiers: ["they are low-pressure membrane processes", "their poor PFAS removal implies they are not effective for PFAS separation or concentration relative to high-pressure membranes"]
- Evidence: NQ26_MMG007
- Prior atomic claims: NQ26-C07
- Full: Count as full (for optional credit) if the answer states that low-pressure membranes like microfiltration and ultrafiltration have poor PFAS removal performance or are ineffective for PFAS separation or concentration.
- Partial: Count as partial (for optional credit) if the answer implies limited PFAS removal by low-pressure microfiltration or ultrafiltration without clearly stating that performance is poor or ineffective.
- Contradiction: Mark as contradicted if the answer claims that low-pressure microfiltration or ultrafiltration are highly effective PFAS separation or concentration routes.

#### NQ26-G07

- Component: `NQ26-T02`
- Importance: `supplementary`
- Function: `affirmative`
- Scoring role: `optional_content`
- Proposition: In some membrane processes treating PFAS-contaminated groundwater, the PFAS-containing concentrate is sent to an evaporation pool and the resulting residue is collected and incinerated as a downstream destructive step.
- Material qualifiers: ["the context is membrane processes applied to PFAS-contaminated groundwater", "the membrane stage produces a concentrate that is sent to an evaporation pool", "the dried residue from the evaporation step is collected and incinerated, which constitutes the destructive step and is downstream of membrane separation", "the specific type of membrane process is not identified beyond being a membrane process"]
- Evidence: NQ26_MMG008
- Prior atomic claims: NQ26-C05
- Full: Count as full (for optional credit) if the answer notes that for some membrane processes treating PFAS, the resulting concentrate is further treated by sending it to an evaporation pool and then incinerating the collected residue as a destruction step.
- Partial: Count as partial (for optional credit) if the answer mentions that membrane-generated PFAS concentrates may be incinerated after some form of volume reduction or evaporation, but does not explicitly mention both the evaporation pool and residue collection.
- Contradiction: Mark as contradicted if the answer states that membrane processes never involve downstream incineration or evaporation-based handling of PFAS concentrates.


### Prior atomic-claim dispositions

#### NQ26-C01

- Prior claim: High-pressure membrane filtration processes using nanoporous nanofiltration (NF) and reverse osmosis (RO) are described as traditional separation technologies that effectively separate short- and long-chain PFAS from water, with rejection efficiencies typically exceeding 90%, and they produce a concentrated PFAS waste stream rather than degrading the PFAS.
- Action: `revised`
- Final target(s): NQ26-B01, NQ26-G01
- Rationale: The NF/RO separation and concentrated-waste-stream content is scored once in G01. B01 separately prevents treating separation as destruction without adding coverage weight.

#### NQ26-C02

- Prior claim: Filtration, membrane distillation, and forward osmosis are classified as concentration (separation) treatments for PFAS-contaminated water that can only concentrate PFAS and therefore need to be combined with separate degradation processes such as electrodegradation or biodegradation for PFAS destruction.
- Action: `revised`
- Final target(s): NQ26-B01, NQ26-G02, NQ26-G05
- Rationale: G02 scores the concentration-only route classification, G05 scores demonstrated or proposed pairing with a separate degradation step, and B01 enforces non-conflation.

#### NQ26-C03

- Prior claim: Membrane-based processes as a class are reported to have a severe limitation in that they do not degrade PFAS and instead function mainly to separate or concentrate PFAS.
- Action: `merged`
- Final target(s): NQ26-B01, NQ26-G02
- Rationale: The original class-level statement overlapped with the route-specific concentration evidence. It is merged into G02 and the non-scored B01 boundary rather than retained as a second required-content group.

#### NQ26-C04

- Prior claim: A membrane-assisted degradation route is described in which [SOURCE_TEXT_OMITTED sha256=c6dccf2785b3b7ced7d6eaf4d253403bd464a74f2516d880fc8baced246561f6], distinguishing this approach from purely separative membrane treatments.
- Action: `mapped`
- Final target(s): NQ26-G03
- Rationale: C04 directly describes membrane-assisted degradation where PFAS are adsorbed on a membrane and then degraded under light or an electric field. This is fully represented as the destructive membrane-coupled route in G03 without modification.

#### NQ26-C05

- Prior claim: Membrane separation processes that concentrate PFAS, including NF and RO, are implemented in practice in tandem with separate destruction technologies, such as sending the PFAS-rich concentrate to an evaporation pool and then collecting and incinerating the residue.
- Action: `revised`
- Final target(s): NQ26-G01, NQ26-G05, NQ26-G07
- Rationale: C05 conflated two sources: NF/RO being operated tandem with destruction technologies (MMG001) and a separate description of generic membrane-process concentrate handling via evaporation and incineration (MMG008). It is split so that: NF/RO separation and concentration aspects align with G01; the tandem-with-destruction concept joins the broader combination narrative in G05, where NF/RO demonstration is distinguished from recommended combinations for other membrane routes; and the specific evaporation-pool and incineration handling of membrane concentrates is represented generically (not tied specifically to NF/RO) in G07.

#### NQ26-C06

- Prior claim: Adsorption onto membranes, when used without a subsequent degradation step, is treated as a concentration or separation operation for PFAS rather than a destructive treatment.
- Action: `revised`
- Final target(s): NQ26-B01, NQ26-G03
- Rationale: The membrane-adsorption first step is represented in G03; B01 prevents equating retention with destruction. No additional scored limitation group is needed.

#### NQ26-C07

- Prior claim: Low-pressure membranes such as microfiltration and ultrafiltration are reported to poorly remove PFAS and are therefore not effective PFAS separation or concentration routes compared with high-pressure membranes.
- Action: `mapped`
- Final target(s): NQ26-G06
- Rationale: C07, about poor PFAS removal by low-pressure microfiltration and ultrafiltration, is directly captured in optional negative-finding group G06 without changes.

### Constraint-only groups

- `NQ26-B01`: Membrane separation or retention of PFAS must not be described as equivalent to PFAS destruction; membrane-based processes generally separate or concentrate PFAS and do not themselves degrade PFAS unless explicitly coupled to a degradation step.
  Violation rule: Flag a boundary violation if the answer equates membrane separation, retention, or concentration (e.g., by NF/RO, filtration, membrane distillation, forward osmosis) with PFAS destruction or degradation, or claims that membrane-based processes inherently degrade PFAS without any separate degradation step.
- `NQ26-B02`: The evidence set does not provide specific details about dedicated electrical membrane separation technologies (such as electrodialysis) or about modified or nanoengineered membranes beyond high-pressure NF/RO-style membranes; answers must not introduce specific performance claims for such routes as if supported by this evidence.
  Violation rule: Flag a boundary violation if the answer attributes specific separation, concentration, or destruction performance or mechanisms to electrical membrane separation technologies (e.g., electrodialysis) or to particular modified/nanoengineered membranes beyond the high-pressure NF/RO context, as though these claims were supported by the provided evidence.

### Model B verification

Overall verdict: **approve**

- `NQ26-G01`: **supported**. MMG004 directly supports high-pressure nanoporous NF/RO separating short- and long-chain PFAS at >90% rejection; MMG001 directly supports the concentrated-waste-stream outcome and 'traditional separation technologies' framing. The two-source synthesis is legitimate (both describe the same NF/RO technologies from complementary angles) and full/partial/contradiction rules correctly require the separative (not destructive) framing.
  Recommended change: None.
- `NQ26-G02`: **supported**. MMG002 explicitly states filtration, adsorption, and membrane distillation 'can only concentrate PFAS'; MMG005 explicitly places filtration, membrane distillation, and forward osmosis in a 'concentration' category contrasted with a separate 'degradation' category. The canonical proposition extends the 'only concentrate, not degrade' language to forward osmosis by combining these two spans; MMG002 itself never names forward osmosis. This is a defensible categorical inference (MMG005's concentration-vs-degradation contrast implies non-degradation for all three members) rather than a fabrication, so it does not rise to a blocking defect, but graders should not treat 'only concentrate' as verbatim-attributed to forward osmosis.
  Recommended change: Optional: note in the group's rationale/full_rule that the 'does not degrade' attribution to forward osmosis is inferred from MMG005's categorical contrast rather than stated by MMG002 verbatim, so future auditors do not mistake it for a direct quote.
- `NQ26-G03`: **supported**. Single-span, direct support for the adsorb-then-degrade-under-light-or-electric-field description, including the optional catalyst detail. Correctly scored as core/required despite the evidence being labeled optional_gold, since the task boundary explicitly requires any destructive membrane-coupled process to be represented.
  Recommended change: None.
- `NQ26-G05`: **supported**. This group now correctly resolves the prior conflation issue: it cleanly separates the already-demonstrated NF/RO-tandem-with-destruction fact (MMG001) from the future-research recommendation to pair other concentration treatments with degradation (MMG005), and the full/partial rules explicitly penalize blurring 'demonstrated' with 'recommended.' The conjunctive merge of two related but independently answerable facts under one AND-rule is a defensible design choice given both facts serve the same task-component distinction, though it does award only partial credit for an answer that correctly states just one half.
  Recommended change: None required; optionally consider whether the two sub-facts merit independent scoring, but the current merge is not a defect.
- `NQ26-G06`: **supported**. Directly supported negative finding, correctly kept as a limitation statement (poor removal) rather than being converted into an affirmative separation-effectiveness claim, and correctly scored as optional/supplementary.
  Recommended change: None.
- `NQ26-G07`: **supported**. This group resolves the prior cross-source conflation flagged against C05: it no longer attributes the evaporation-pool/incineration pathway to NF/RO specifically, explicitly noting in material_qualifiers that 'the specific type of membrane process is not identified beyond being a membrane process,' consistent with the evidence record's own does_not_support caveat.
  Recommended change: None.
- `NQ26-B01`: **supported**. Violation rule executably flags any equation of membrane separation/retention/concentration with destruction. MMG003's general 'membrane-based processes... do not degrade PFAS' statement is appropriately housed here rather than as a separate scored required-content group, since it restates the general principle already captured route-specifically in G01/G02/G03 and correctly stays outside the coverage denominator per constraint-only exclusion.
  Recommended change: None required.
- `NQ26-B02`: **supported**. A no-evidence boundary constraint correctly encoding an absence (no dedicated electrical-membrane or modified/nanoengineered-membrane performance data in the gold set); violation_rule is executable and appropriately scoped to prevent fabricated attribution rather than requiring positive evidence.
  Recommended change: None required.

Human-review priorities:
- The prior C05 (NF/RO-vs-evaporation-pool conflation) issue is genuinely resolved: G07 now generically attributes the evaporation-pool/incineration pathway to unspecified 'membrane processes,' not NF/RO specifically.
- The prior C06 (adsorption-attribution overreach) issue is genuinely resolved: G02's canonical proposition no longer claims MMG002's 'adsorption' is membrane-based; the membrane-adsorption content is confined to G03, which is directly supported by MMG006.
- The prior duplicate-weighting issue between G02 and G04 is resolved by removing G04 entirely and merging its content (C03) into G02 and the non-scored B01 boundary, eliminating the double-credit risk the prior Model B review flagged.
- G02's attribution of 'only concentrate, not degrade' to forward osmosis is an inference from MMG005's concentration-vs-degradation category contrast rather than a verbatim statement in MMG002 (which lists filtration/adsorption/membrane distillation only) — acceptable synthesis, but worth a light annotation for future auditors.
- MMG003 (required_gold) is referenced only inside constraint group B01 and never appears in any required_content group's exact_spans; this is defensible since its content duplicates the route-specific limitations already scored in G01/G02, but a project author may want to confirm this required_gold item is not meant to carry independent coverage weight.
- G05's conjunctive (AND) merge of the 'NF/RO already demonstrated tandem with destruction' fact and the 'future research recommendation to combine other concentration treatments with degradation' fact is a reasonable single-group design for task component T02, but project authors could alternatively split these into two independently scorable groups if finer-grained partial credit is desired.

### Non-normative reference prose

High-pressure nanofiltration and reverse osmosis are separation routes that can reject both short- and long-chain PFAS and produce a concentrated waste stream. Simple filtration, membrane distillation, and forward-osmosis routes concentrate or separate PFAS but do not themselves degrade it. That limitation does not apply to the distinct membrane-assisted degradation category, in which PFAS are first accumulated on a membrane and then degraded under light or an electric field. Concentrated PFAS streams can therefore be paired with a separate destruction or degradation step. The evidence also notes poor removal by some low-pressure membranes and an example in which concentrate residue is incinerated downstream. Separation or retention must not be reported as destruction unless an explicit degradation step is present.

### Prose-to-ledger map

- High-pressure nanofiltration and reverse osmosis are separation routes that can reject both short- and long-chain PFAS and produce a concentrated waste stream. -> NQ26-G01
- Simple filtration, membrane distillation, and forward-osmosis routes concentrate or separate PFAS but do not themselves degrade it. -> NQ26-G02
- That limitation does not apply to the distinct membrane-assisted degradation category, in which PFAS are first accumulated on a membrane and then degraded under light or an electric field. -> NQ26-G03
- Concentrated PFAS streams can therefore be paired with a separate destruction or degradation step. -> NQ26-G05
- The evidence also notes poor removal by some low-pressure membranes and an example in which concentrate residue is incinerated downstream. -> NQ26-G06, NQ26-G07
- Separation or retention must not be reported as destruction unless an explicit degradation step is present. -> NQ26-B01, NQ26-B02

---

## WF10_002

**Question:** When comparing membrane filtration, gliding arc plasma, and supercritical water oxidation for PFAS treatment, which reported endpoints should be kept separate?

**Must include:** Keep removal, separation, adsorption, degradation, defluorination, mineralization, destruction, byproduct formation, and mass-balance evidence separate.

**Must not claim:** Do not convert a condition-specific finding into a universal PFAS treatment claim.

### Frozen task components

- `WF10_002-T01`: Identify the distinct treatment endpoints reported for membrane filtration, gliding arc plasma, and supercritical water oxidation.
- `WF10_002-T02`: Explain why removal, separation, degradation, defluorination, mineralization, destruction, byproduct formation, and mass balance cannot be treated as interchangeable endpoints.

### Complete gold evidence

**WF10_002_MMG001** (required_gold; `2020 - Lewis - rsc.li - es-water Rapid degradation of PFAS in aqueous solutions by reverse vortex flow gliding arc plasma †.pdf`, chunk `18`)
> [SOURCE_TEXT_OMITTED sha256=8c6eeb4d26f0fa59429686e5c8a0bd616b5f15acf6f58113be34d3afe8d09f4f].

**WF10_002_MMG002** (optional_gold; `2024 - Shaji - Investigating the Effects of Gliding Arc Plasma Discharge’s Thermal Characteristic and Reactive Chemistry on Aqueous PFOS Mineralization.pdf`, chunk `8`)
> [SOURCE_TEXT_OMITTED sha256=4c6dba3ed2683f36ee4a6d9a6397c54d1ed8961480b521229e442ce8d8e8509d]].

**WF10_002_L3X001** (l3_transferred_audited_gold; `2024 - Pervez - Structure and mechanism of nanoengineered membranes toward per- and polyfluoroalkyl substances (PFAS) removal from water - A critical review.pdf`, chunk `4`)
> [SOURCE_TEXT_OMITTED sha256=1c93c6bbc04d9e9b8e5fb4c698395a40b38ca869ce2ce319f451e9e4e5d0a23b] ].

**WF10_002_L3X002** (l3_transferred_audited_gold; `2025 - Liu - Filtration and electrical membrane-based treatment methods for PFAS-contaminated water and preparation methods for the membranes employed.pdf`, chunk `21`)
> [SOURCE_TEXT_OMITTED sha256=83cad68bd45d2078d6111dab03fa6fe6edf58ebe23a550abae1a931d9038d69b].

**WF10_002_L3X003** (l3_transferred_audited_gold; `2021 - Pinkard - Destruction of perfluorooctanesulfonate (PFOS) in a batch supercritical water oxidation reactor.pdf`, chunk `1`)
> [SOURCE_TEXT_OMITTED sha256=7454baf423fad18cf260e97c56d02d9ae340bdcf5a0d679f5d482d4bf97a8285].

### Normative content claim groups

#### WF10_002-G01

- Component: `WF10_002-T01`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: In the reported gliding arc plasma PFAS treatment system, disappearance of the target analyte(s), formation of degradation products, defluorination, and energy costs are measured as distinct endpoints.
- Material qualifiers: ["These endpoints are all measured for PFAS-contaminated water treated by an engineered gliding arc plasma system.", "These four quantities are each measured and calculated as separate metrics for the same GAP treatment system."]
- Evidence: WF10_002_MMG001
- Prior atomic claims: WF10_002-C01, WF10_002-C02, WF10_002-C03, WF10_002-S01
- Full: Full credit if the answer states that, for gliding arc plasma treatment of PFAS-contaminated water, disappearance/removal of the parent analyte(s), degradation-product formation, defluorination, and energy or energy cost are all measured as distinct, separate endpoints for the same system.
- Partial: Partial credit if the answer correctly identifies at least two of the four GAP endpoints as separate measurements (e.g., disappearance and defluorination, or disappearance and degradation products), even if it omits energy/operational endpoints or does not explicitly note that all four are distinct.
- Contradiction: Mark as contradicted if the answer states or clearly implies that only one of these quantities is measured for GAP, or misidentifies the listed GAP endpoints in a way that conflicts with the evidence (e.g., replacing energy cost with an endpoint not reported in the cited record).

#### WF10_002-G02

- Component: `WF10_002-T01`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: For supercritical water oxidation, PFAS mineralization is reported as a distinct endpoint, with increased mineralization at higher reaction temperatures and minimal short-chain PFAS byproduct formation.
- Material qualifiers: ["Supercritical water oxidation has shown excellent potential for PFAS mineralization.", "Formation of short-chain PFAS byproducts during this mineralization is described as minimal.", "Increased mineralization with a rise in reaction temperature has been observed in SCWO."]
- Evidence: WF10_002_MMG002
- Prior atomic claims: WF10_002-C04, WF10_002-S02
- Full: Full credit if the answer states that, for supercritical water oxidation, PFAS mineralization is an explicit endpoint and notes both that (a) short-chain PFAS formation is reported as minimal and (b) mineralization increases with higher reaction temperature.
- Partial: Partial credit if the answer correctly identifies mineralization as a distinct SCWO endpoint but omits either the minimal short-chain byproduct qualifier or the temperature–mineralization relationship, without introducing incompatible statements.
- Contradiction: Mark as contradicted if the answer denies that mineralization is an SCWO endpoint, or claims that SCWO produces substantial short-chain PFAS byproducts, or that mineralization decreases with increasing temperature, when describing the supplied evidence.

#### WF10_002-G03

- Component: `WF10_002-T01`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: High-pressure NF and RO report separation or rejection of short- and long-chain PFAS, while filtration, adsorption, and membrane distillation are described as concentration treatments rather than degradation endpoints.
- Material qualifiers: ["high-pressure membrane examples are NF and RO", "the membrane endpoint is separation or rejection of short- and long-chain PFAS", "filtration, adsorption, and membrane distillation are described as concentration treatments"]
- Evidence: WF10_002_L3X001, WF10_002_L3X002
- Prior atomic claims: WF10_002-L01
- Full: Award full if the answer identifies membrane separation or rejection as distinct from degradation and also keeps adsorption or concentration distinct from destruction.
- Partial: Award partial if the answer correctly distinguishes either membrane separation/rejection or adsorption/concentration from degradation but does not cover both.
- Contradiction: Mark contradicted if the answer treats membrane rejection, adsorption, or concentration as PFAS degradation or destruction.

#### WF10_002-G05

- Component: `WF10_002-T02`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: Across the three represented treatment contexts, membrane filtration reports separation/rejection or concentration, GAP reports disappearance, degradation products, and defluorination, and SCWO reports mineralization and short-chain byproduct formation; these are different endpoint categories and should be reported separately.
- Material qualifiers: ["membrane: separation/rejection and concentration", "GAP: disappearance, degradation products, and defluorination", "SCWO: mineralization and short-chain byproduct formation"]
- Evidence: WF10_002_MMG001, WF10_002_MMG002, WF10_002_L3X001, WF10_002_L3X002
- Prior atomic claims: WF10_002-C05
- Full: Award full if the answer distinguishes the endpoint categories for all three treatment contexts rather than using removal, degradation, defluorination, and mineralization interchangeably.
- Partial: Award partial if the answer correctly distinguishes endpoints for two of the three treatment contexts.
- Contradiction: Mark contradicted if the answer equates membrane rejection, GAP disappearance, or SCWO mineralization as one identical endpoint.

#### WF10_002-G06

- Component: `WF10_002-T02`
- Importance: `core`
- Function: `limitation`
- Scoring role: `required_content`
- Proposition: Overall destruction and fluorine mass balance are interpretive outcomes distinct from individual measurements. In SCWO, a low fluorine mass balance at 425 and 450 C was interpreted as possible undetected fluorinated species in gas or liquid products, showing why target disappearance alone does not close fluorine fate.
- Material qualifiers: ["overall destruction and fluorine mass balance are interpretive outcomes distinct from any single measured endpoint", "the cited SCWO example reports low fluorine mass balance at 425 and 450 C, but exact temperatures are illustrative and are not required for credit", "undetected fluorinated gas or liquid products are a possible explanation rather than identified or quantified species"]
- Evidence: WF10_002_MMG001, WF10_002_L3X003
- Prior atomic claims: WF10_002-C06, WF10_002-L02
- Full: Award full if the answer keeps overall destruction and fluorine mass balance separate from individual endpoints and uses the SCWO low-fluorine-balance example with appropriate uncertainty about possible undetected fluorinated products. Exact temperatures are not required.
- Partial: Award partial if the answer generally distinguishes destruction or mass balance from individual endpoints but omits either the SCWO example or the uncertainty that the fluorinated products were not identified and quantified.
- Contradiction: Mark contradicted if the answer treats target disappearance as complete fluorine mass-balance closure or claims the undetected species were identified and quantified.


### Prior atomic-claim dispositions

#### WF10_002-C01

- Prior claim: In the reported gliding arc plasma PFAS treatment system, disappearance of the target analyte(s), formation of degradation products, defluorination, and energy costs are measured as distinct endpoints rather than being collapsed into a single destruction metric.
- Action: `merged`
- Final target(s): WF10_002-G01
- Rationale: C01 describes the four GAP endpoints and their treatment as distinct rather than a single destruction metric; the distinct endpoint listing is fully captured in G01.

#### WF10_002-C02

- Prior claim: For the GAP system, disappearance of the parent PFAS (a removal-type endpoint) must be distinguished from formation of degradation products (a degradation/byproduct-formation endpoint), because the study states that multiple measurements must be co-aligned to demonstrate PFAS destruction versus mere alteration.
- Action: `merged`
- Final target(s): WF10_002-G01
- Rationale: The atomic claim describes the separateness of GAP chemical measurements already scored in G01. It is merged there rather than counted again under a second required-content group.

#### WF10_002-C03

- Prior claim: Defluorination in the GAP study is treated as an endpoint separate from both target-analyte disappearance and degradation-product formation, and all three chemical endpoints must be considered together to assess whether PFAS are destroyed.
- Action: `merged`
- Final target(s): WF10_002-G01
- Rationale: The atomic claim describes the separateness of GAP chemical measurements already scored in G01. It is merged there rather than counted again under a second required-content group.

#### WF10_002-C04

- Prior claim: In the SCWO context, mineralization of PFAS is reported as a distinct endpoint, with increased mineralization at higher reaction temperatures, and this mineralization endpoint is differentiated from short-chain PFAS byproduct formation, which is described as minimal.
- Action: `mapped`
- Final target(s): WF10_002-G02
- Rationale: C04 describes SCWO mineralization as a distinct endpoint with minimal short-chain PFAS formation and increased mineralization at higher temperature; this is directly represented by G02.

#### WF10_002-C05

- Prior claim: When comparing GAP and SCWO, mineralization endpoints reported for SCWO should not be conflated with the disappearance, degradation-product formation, or defluorination endpoints reported for GAP, because the two studies emphasize different specific measurements.
- Action: `mapped`
- Final target(s): WF10_002-G05
- Rationale: C05 states that SCWO mineralization endpoints should not be conflated with GAP disappearance, degradation products, or defluorination; this cross-technology non-conflation is the central focus of G05.

#### WF10_002-C06

- Prior claim: Any overall judgment of PFAS destruction or fate in the GAP system is not a single measured endpoint but an interpretation that integrates separate measurements of disappearance, degradation products, and defluorination, so this integrative destruction or mass-balance view must be kept conceptually distinct from the individual endpoints themselves.
- Action: `mapped`
- Final target(s): WF10_002-G06
- Rationale: C06 explains that destruction in GAP is an interpretive integration of disappearance, degradation products, and defluorination; G06 generalizes this to the broader distinction between destruction/mass balance and individual endpoints.

#### WF10_002-S01

- Prior claim: In the GAP study, energy cost is explicitly tracked as an operational endpoint that is separate from chemical endpoints such as target-analyte disappearance, degradation products, and defluorination.
- Action: `merged`
- Final target(s): WF10_002-G01
- Rationale: S01 highlights energy cost as an operational endpoint separate from chemical endpoints in GAP; this distinction is included as part of the endpoint list and its separateness in G01.

#### WF10_002-S02

- Prior claim: The SCWO discussion highlights minimal formation of short-chain PFAS during mineralization, indicating that mineralization and byproduct formation are treated as separate outcome categories in that context.
- Action: `mapped`
- Final target(s): WF10_002-G02
- Rationale: S02 emphasizes minimal short-chain PFAS formation relative to mineralization in SCWO; G02 encodes this within the SCWO endpoint description.

#### WF10_002-L01

- Prior claim: The supplied evidence does not describe separation or adsorption endpoints, nor any membrane-filtration experiments, so separation and adsorption must be recognized as distinct, but currently unquantified, endpoint categories when comparing membrane filtration with GAP and SCWO.
- Action: `revised`
- Final target(s): WF10_002-G03
- Rationale: The original draft marked membrane evidence as absent. Repair5 added already audited membrane evidence, so G03 now positively represents membrane separation/rejection and concentration endpoints.

#### WF10_002-L02

- Prior claim: Although the GAP study combines disappearance, degradation products, and defluorination conceptually to argue that PFAS are destroyed rather than merely altered, it does not present a complete quantitative mass balance, so mass-balance evidence remains methodologically distinct and is not fully characterized in the supplied records.
- Action: `mapped`
- Final target(s): WF10_002-G06
- Rationale: L02 explains that no complete quantitative mass balance is reported and that destruction is inferred from co-aligned endpoints; G06 captures this as part of the conceptual separation between destruction/mass balance and individual endpoints.

### Constraint-only groups

- `WF10_002-B01`: Do not generalize condition-specific findings from the cited GAP or SCWO contexts into universal claims about all PFAS treatments or all technologies.
  Violation rule: Flag a boundary violation if the answer takes results or endpoint behavior described for GAP or SCWO under specific conditions and states or clearly implies that the same endpoint relationships or performance necessarily apply to all PFAS treatment technologies or all operating conditions.

### Model B verification

Overall verdict: **approve**

- `WF10_002-G01`: **supported**. Canonical proposition and qualifiers (four distinct GAP endpoints measured for the engineered system) are directly entailed by the exact span. Merge of C01/C02/C03/S01 into this single group is appropriate since all describe the same underlying endpoint-separateness finding rather than independently answerable facts.
  Recommended change: None.
- `WF10_002-G02`: **supported**. Mineralization as a distinct SCWO endpoint, minimal short-chain byproduct formation, and temperature dependence are all entailed by the cited span. C04/S02 merge is non-duplicative content consolidation.
  Recommended change: None.
- `WF10_002-G03`: **supported**. L3X001 directly entails NF/RO separation with >90% rejection; L3X002's 'can only concentrate PFAS' framing (under a header introducing membrane-assisted degradation as an addition) reasonably entails that filtration/adsorption/membrane distillation are concentration-only rather than degradation endpoints. This newly added group correctly resolves the prior coverage gap where membrane-filtration evidence was absent (L01 revised).
  Recommended change: None.
- `WF10_002-G05`: **supported**. Each per-technology fact synthesized here is independently entailed by the same spans underlying G01/G02/G03; the synthesis (these are non-interchangeable endpoint categories) is correctly flagged synthesis_required: true and answers T02's explanatory demand rather than merely restating T01 inventory content.
  Recommended change: None.
- `WF10_002-G06`: **supported**. The conceptual distinction (destruction/mass balance as interpretive, not a single measured endpoint) and the SCWO low-fluorine-balance example with appropriate uncertainty about undetected species are both entailed by the cited spans. The previously identified numeric-rule inconsistency is resolved: full_rule now explicitly states exact temperatures are not required, matching numeric_required: false.
  Recommended change: None.
- `WF10_002-B01`: **supported**. Correctly excluded from coverage scoring (scoring_role: constraint_only) with an executable violation_rule that matches the must_not_claim boundary (no generalization of condition-specific GAP/SCWO findings to all PFAS treatments).
  Recommended change: None.

Human-review priorities:
- G01, G05, and G06 all cite WF10_002_MMG001 for distinct synthesis purposes (endpoint listing, cross-technology comparison, destruction/mass-balance framing); this is defensible given their different scoring functions, but a project author may want to confirm the same span isn't effectively over-weighting one underlying GAP finding across three required_content groups.
- MMG002 remains tagged optional_gold yet anchors core required_content group G02 and also supports G05; this elevation is documented in the ledger and reasonable, but a project author may want to formally confirm it rather than rely on ledger self-justification.
- The reference answer now consistently uses 'SCWO discussion' rather than implying a dedicated SCWO primary study, addressing the earlier concern that MMG002 is secondary literature cited within a plasma paper.
- The previously flagged G06 numeric_required/accepted_numeric_equivalents inconsistency has been resolved via explicit 'Exact temperatures are not required' language in the full_rule; no further action needed on that specific defect.
- Confirm no additional membrane-filtration gold evidence exists beyond the two transferred L3 records (L3X001, L3X002), since G03/G05 coverage now depends on this L3 transfer being complete.

### Non-normative reference prose

Membrane filtration reports separation or rejection: high-pressure NF and RO separate short- and long-chain PFAS, while filtration, adsorption, and membrane distillation are concentration endpoints rather than degradation endpoints. The GAP study separately reports parent-analyte disappearance, degradation-product formation, defluorination, and energy cost. The SCWO discussion reports mineralization, temperature dependence, and minimal short-chain byproduct formation as separate outcomes. Therefore membrane separation, adsorption or concentration, GAP degradation measurements, and SCWO mineralization should not be treated as interchangeable endpoints. Overall destruction and fluorine mass balance are additional interpretive outcomes: in one SCWO example, low fluorine balance at 425 and 450 C suggested undetected fluorinated gas or liquid products rather than proving complete fate closure. These distinctions are condition-specific and do not establish a universal endpoint pattern for every PFAS technology.

### Prose-to-ledger map

- Membrane filtration reports separation or rejection: high-pressure NF and RO separate short- and long-chain PFAS, while filtration, adsorption, and membrane distillation are concentration endpoints rather than degradation endpoints. -> WF10_002-G03
- The GAP study separately reports parent-analyte disappearance, degradation-product formation, defluorination, and energy cost. -> WF10_002-G01
- The SCWO discussion reports mineralization, temperature dependence, and minimal short-chain byproduct formation as separate outcomes. -> WF10_002-G02
- Therefore membrane separation, adsorption or concentration, GAP degradation measurements, and SCWO mineralization should not be treated as interchangeable endpoints. -> WF10_002-G05
- Overall destruction and fluorine mass balance are additional interpretive outcomes: in one SCWO example, low fluorine balance at 425 and 450 C suggested undetected fluorinated gas or liquid products rather than proving complete fate closure. -> WF10_002-G06
- These distinctions are condition-specific and do not establish a universal endpoint pattern for every PFAS technology. -> WF10_002-B01

---

## WF10_021

**Question:** When screening activated-carbon or biochar PFAS adsorption studies, what matrix and regeneration gaps should be checked?

**Must include:** Use limitation, uncertainty, caveat, and negative evidence to avoid overclaiming beyond the reported study scope.

**Must not claim:** Do not convert a condition-specific finding into a universal PFAS treatment claim.

### Frozen task components

- `WF10_021-T01`: Identify matrix-related gaps that should be checked when screening activated-carbon or biochar adsorption studies.
- `WF10_021-T02`: Identify regeneration or reuse gaps that should be checked before drawing broader conclusions.

### Complete gold evidence

**WF10_021_MMG001** (negative_gold; `2026 - Sadmani - A critical review of the application of biochar in removing perfluoroalkyl and polyfluoroalkyl substances (PFAS) from water matrices.pdf`, chunk `52`)
> [SOURCE_TEXT_OMITTED sha256=ba983058c894e8f13a17557676d7f69e4842abdad2c8fc0f706b17853b9d9445].

**WF10_021_MMG002** (negative_gold; `2024 - Liang - A critical review of biochar for the remediation of PFAS-contaminated soil and water.pdf`, chunk `48`)
> [SOURCE_TEXT_OMITTED sha256=2ef738b52bd23cfd7945e62f17b2178422684983ba7d690836ca9792573b7ab7].

**WF10_021_MMG003** (negative_gold; `2026 - Sadmani - A critical review of the application of biochar in removing perfluoroalkyl and polyfluoroalkyl substances (PFAS) from water matrices.pdf`, chunk `68`)
> [SOURCE_TEXT_OMITTED sha256=1ee9fa0dacb5bd30615e945797f1feedd8ba78cfa3d955b6a7c30a213d78d909].

### Normative content claim groups

#### WF10_021-G01

- Component: `WF10_021-T01`
- Importance: `core`
- Function: `limitation`
- Scoring role: `required_content`
- Proposition: For biochar used to remove PFAS from water matrices, organic matter in the water has highly variable effects on PFAS sorption, and further research is needed to optimize biochar performance under diverse water-matrix conditions.
- Material qualifiers: ["the sorbent is biochar", "the endpoint is PFAS sorption/adsorption performance", "the matrix is diverse water matrices with differing organic-matter type and concentration", "the variability in organic-matter effects means further research is needed to optimize biochar performance under different water-matrix conditions"]
- Evidence: WF10_021_MMG001
- Prior atomic claims: WF10_021-C01, WF10_021-C02
- Full: Full credit if the answer states that for biochar used for PFAS removal from water matrices, organic matter in the water has variable or inconsistent effects on PFAS sorption (e.g., minimal interference in some cases and strong reductions in others) AND explicitly links this variability to an unresolved matrix-related limitation, such as a need for further research or incomplete understanding of biochar performance across diverse water matrices. The answer must mention all of: biochar, PFAS sorption/adsorption, water matrices, organic matter (or an equivalent term like natural organic matter or OM), and that the impact of OM is variable and not yet fully resolved.
- Partial: Partial credit if the answer correctly notes that organic matter effects on PFAS sorption by biochar in water are variable or uncertain, but omits either the need for further research/optimization OR one of the key qualifiers (e.g., does not clearly specify that the limitation is about diverse water matrices). The answer must not attribute this limitation to a different sorbent (such as activated carbon) without also correctly stating it for biochar.
- Contradiction: Contradiction if the answer states or clearly implies that organic matter has a consistent, well-understood, or uniformly minimal effect on PFAS sorption by biochar in water matrices, or claims that biochar PFAS sorption performance under differing organic-matter conditions is already well-optimized or does not require further research.

#### WF10_021-G02

- Component: `WF10_021-T02`
- Importance: `core`
- Function: `limitation`
- Scoring role: `required_content`
- Proposition: Biochar regeneration for PFAS removal has not been attempted frequently enough in the literature to draw definitive conclusions about regeneration efficacy.
- Material qualifiers: ["the sorbent is biochar", "the context is PFAS remediation (soil or water)", "the limitation is at the field/literature level (insufficient regeneration attempts overall)"]
- Evidence: WF10_021_MMG002
- Prior atomic claims: WF10_021-C03
- Full: Full credit if the answer states that biochar regeneration for PFAS removal has been evaluated too rarely or infrequently in the literature to allow firm or definitive conclusions about how effective regeneration is. It must clearly tie this limitation to biochar (not just sorbents in general) and to PFAS remediation.
- Partial: Partial credit if the answer correctly conveys that there is limited or insufficient evidence on the efficacy of biochar regeneration for PFAS removal, but does not clearly specify that this is because regeneration has not been attempted frequently enough OR omits either the explicit connection to PFAS or to biochar.
- Contradiction: Contradiction if the answer claims that there is ample, frequent, or sufficient evidence to draw firm or definitive conclusions about the efficacy of biochar regeneration for PFAS removal, or otherwise asserts that regeneration efficacy is already well established.

#### WF10_021-G03

- Component: `WF10_021-T02`
- Importance: `core`
- Function: `limitation`
- Scoring role: `required_content`
- Proposition: Each regeneration cycle can alter biochar characteristics, including surface morphology, functionalities, and porosity, so these regeneration-induced changes require thorough investigation when assessing biochar reusability for PFAS removal.
- Material qualifiers: ["the sorbent is biochar", "the context is regeneration for PFAS removal", "the affected properties include surface morphology, surface functionalities, and porosity", "these regeneration-induced changes necessitate thorough investigation when evaluating sustainable regeneration and reusability"]
- Evidence: WF10_021_MMG003
- Prior atomic claims: WF10_021-C04
- Full: Full credit if the answer explains that regeneration cycles change biochar’s properties and identifies at least one of the specified properties (surface morphology, surface functionalities, or porosity) AND explicitly notes that these regeneration-induced changes need to be or should be thoroughly investigated in the context of biochar reusability for PFAS removal.
- Partial: Partial credit if the answer correctly notes that regeneration can change or degrade biochar properties relevant to PFAS removal, but omits mention of any specific property (morphology, functionalities, or porosity) OR omits the explicit need for thorough investigation of these changes.
- Contradiction: Contradiction if the answer asserts that regeneration does not materially change biochar’s physical or chemical properties relevant to PFAS removal, or that such changes do not need to be investigated when assessing reusability.

#### WF10_021-G04

- Component: `WF10_021-T01`
- Importance: `core`
- Function: `limitation`
- Scoring role: `required_content`
- Proposition: The supplied matrix-limitation evidence is biochar-specific; it does not establish analogous matrix effects for activated carbon.
- Material qualifiers: ["scope is the supplied evidence set", "affirmative matrix evidence concerns biochar", "no activated-carbon matrix result is inferred"]
- Evidence: WF10_021_MMG001
- Prior atomic claims: WF10_021-C05
- Full: Award full if the answer explicitly states that the matrix evidence is biochar-specific and does not establish the activated-carbon case.
- Partial: Award partial if the answer discusses biochar matrix limitations without explicitly identifying the activated-carbon evidence gap.
- Contradiction: Mark contradicted if the answer generalizes the biochar matrix finding to activated carbon as a demonstrated result.

#### WF10_021-G05

- Component: `WF10_021-T02`
- Importance: `core`
- Function: `limitation`
- Scoring role: `required_content`
- Proposition: The supplied regeneration and reuse limitations are biochar-specific; they do not establish analogous regeneration behavior for activated carbon.
- Material qualifiers: ["scope is the supplied evidence set", "affirmative regeneration evidence concerns biochar", "no activated-carbon regeneration result is inferred"]
- Evidence: WF10_021_MMG002, WF10_021_MMG003
- Prior atomic claims: WF10_021-C05
- Full: Award full if the answer explicitly states that the regeneration evidence is biochar-specific and does not establish the activated-carbon case.
- Partial: Award partial if the answer discusses biochar regeneration limitations without identifying the activated-carbon evidence gap.
- Contradiction: Mark contradicted if the answer generalizes the biochar regeneration finding to activated carbon as a demonstrated result.


### Prior atomic-claim dispositions

#### WF10_021-C01

- Prior claim: For biochar used to remove PFAS from water matrices, the impact of organic matter on PFAS sorption is highly variable across studies, with some reporting minimal interference at environmentally relevant OM concentrations and others reporting substantial reductions in PFAS sorption, indicating a key matrix-related uncertainty.
- Action: `merged`
- Final target(s): WF10_021-G01
- Rationale: C01’s description of highly variable organic-matter impacts on PFAS sorption by biochar is directly supported by the evidence and forms the central proposition of G01. It overlapped substantially with C02, so both were merged into a single, more atomic matrix-related limitation claim.

#### WF10_021-C02

- Prior claim: Because biochar PFAS sorption is sensitive to the type and concentration of organic matter in diverse water matrices, further research is needed to optimize biochar performance under different water-matrix conditions, and studies that do not probe these conditions have important matrix-scope gaps.
- Action: `revised`
- Final target(s): WF10_021-G01
- Rationale: The portion of C02 stating that further research is needed to optimize biochar performance under diverse water matrices is supported and retained in G01. The interpretive extension about individual studies having matrix-scope gaps was removed to stay closer to the literal evidence.

#### WF10_021-C03

- Prior claim: Biochar regeneration for PFAS removal has not been attempted frequently enough in the literature to draw definitive conclusions on regeneration efficacy, so studies that omit or minimally test regeneration have a major regeneration-data gap.
- Action: `revised`
- Final target(s): WF10_021-G02
- Rationale: C03 included a supported field-level limitation (insufficient frequency of biochar regeneration attempts) plus an unsupported per-study screening inference. G02 retains the supported limitation and removes the interpretive statement about individual studies.

#### WF10_021-C04

- Prior claim: Each regeneration cycle can alter biochar characteristics, including surface morphology, surface functionalities, and porosity, making it necessary to investigate these regeneration-induced changes when assessing biochar reusability for PFAS removal.
- Action: `mapped`
- Final target(s): WF10_021-G03
- Rationale: C04 is directly supported by the evidence and is carried over unchanged as the canonical proposition in G03.

#### WF10_021-C05

- Prior claim: The matrix and regeneration limitations identified in the supplied evidence are specifically documented for biochar used to remove PFAS from water matrices, and are not automatically generalizable to other sorbents such as activated carbon.
- Action: `revised`
- Final target(s): WF10_021-B01, WF10_021-G04, WF10_021-G05
- Rationale: C05 provides a scope clarification that the documented limitations apply to biochar and are not established for activated carbon. This is represented as an optional scope/limitation claim (G04) and as a boundary constraint (B01) to enforce the must_not_claim rule. No new scientific content beyond the evidence and the absence of activated-carbon data is introduced. Disposition targets normalized from ['WF10_021-B01', 'WF10_021-G04'] to ['WF10_021-B01', 'WF10_021-G04', 'WF10_021-G05'] using final source_atomic_claim_ids.

### Constraint-only groups

- `WF10_021-B01`: Do not generalize the biochar-specific matrix and regeneration limitations in the provided evidence into universal PFAS treatment claims or into specific claims about activated carbon.
  Violation rule: Flag a boundary violation if the answer (1) presents the biochar-specific limitations as if they apply universally to all PFAS treatment technologies, or (2) explicitly states that the provided evidence demonstrates specific matrix or regeneration gaps for activated carbon, or (3) claims broad PFAS treatment efficacy without acknowledging the biochar- and condition-specific nature of the findings.

### Model B verification

Overall verdict: **approve**

- `WF10_021-G01`: **supported**. Merges C01/C02 as recommended in the prior review, resolving the redundancy flag. Canonical proposition, qualifiers, and full/partial/contradiction rules are all directly entailed by the single exact span; the interpretive 'per-study screening gap' language previously flagged as inference-beyond-span has been removed.
  Recommended change: None.
- `WF10_021-G02`: **supported**. C03's unsupported per-study screening inference was stripped; the retained proposition ('has not been attempted frequently enough ... definitive conclusions on efficacy') is a near-verbatim restatement of the exact span. Rules correctly require the biochar+PFAS tie rather than a generic sorbent claim.
  Recommended change: None.
- `WF10_021-G03`: **supported**. Directly entailed by the exact span (morphology, functionalities, porosity, need for investigation). Carried over unchanged from C04, which was never flagged as problematic.
  Recommended change: None.
- `WF10_021-G04`: **supported**. A legitimate synthesis-required negative/absence claim: the evidence never mentions activated carbon, so stating that the matrix finding is biochar-specific and does not establish the activated-carbon case is a correct entailment of what is (and is not) in the record, appropriate for a negative_limitation_evidence task. Does not convert absence-of-evidence into a positive claim about activated carbon.
  Recommended change: None required; optionally note in prose that this group is evidentiary-absence based rather than a directly stated span (already implicit via synthesis_required: true).
- `WF10_021-G05`: **supported**. Same reasoning as G04 applied to the regeneration task component; correctly kept as a separate group tied to T02 rather than folded into G04, since it is independently answerable and evidenced by different spans.
  Recommended change: None.
- `WF10_021-B01`: **supported**. Correctly marked constraint_only/excluded from coverage, with an executable violation_rule covering universalization to all PFAS treatments and false claims of activated-carbon-specific evidence. Directly operationalizes the must_not_claim boundary. It does not create duplicate coverage weight alongside G04/G05 since it is excluded from the scoring denominator.
  Recommended change: Optional: the group is tagged task_component_id=T01 only, but its violation_rule and evidence span equally cover T02 (regeneration). Since constraint_only groups are excluded from per-component coverage this has no scoring effect, so it is non-blocking.

Human-review priorities:
- G04/B01 both draw on the same evidence and originate from the same source atomic claim (C05), split across a scored required_content group and an unscored constraint group; this is architecturally sound (no double coverage weight since B01 is excluded from the denominator) but is a design choice worth the project author's sign-off given the question explicitly names activated carbon as a subject, not just a boundary to avoid.
- B01 is tagged to task_component_id=T01 only despite its violation_rule and evidence spans covering both matrix (T01) and regeneration (T02) gaps; this has no scoring impact (constraint_only groups are excluded from per-component coverage regardless of tag) but could be cleaned up for organizational clarity in a future ledger pass.
- Confirm the project author is comfortable with G04/G05 being synthesis-required absence-of-evidence claims (the evidence never mentions activated carbon) rather than directly stated spans — this is a valid and appropriately labeled use of synthesis_required for a negative_limitation_evidence task type, but is a judgment call worth flagging before audit.

### Non-normative reference prose

For biochar, organic matter can have highly variable effects on PFAS sorption across water matrices, leaving a need for matrix-specific optimization. Biochar regeneration has been studied too infrequently for definitive efficacy conclusions, and repeated cycles can alter morphology, functionality, and porosity. The supplied matrix evidence is biochar-specific and does not establish analogous matrix behavior for activated carbon. Likewise, the supplied regeneration evidence is biochar-specific and does not establish activated-carbon regeneration behavior. These evidence gaps should be reported rather than filled by generalizing biochar findings to activated carbon.

### Prose-to-ledger map

- For biochar, organic matter can have highly variable effects on PFAS sorption across water matrices, leaving a need for matrix-specific optimization. -> WF10_021-G01
- Biochar regeneration has been studied too infrequently for definitive efficacy conclusions, and repeated cycles can alter morphology, functionality, and porosity. -> WF10_021-G02, WF10_021-G03
- The supplied matrix evidence is biochar-specific and does not establish analogous matrix behavior for activated carbon. -> WF10_021-G04
- Likewise, the supplied regeneration evidence is biochar-specific and does not establish activated-carbon regeneration behavior. -> WF10_021-G05
- These evidence gaps should be reported rather than filled by generalizing biochar findings to activated carbon. -> WF10_021-B01

---

## WF10_025

**Question:** How should contact time be planned when powder activated carbon is used for both short- and long-chain PFAS?

**Must include:** Identify the relevant protocol steps, reagents/materials, operating conditions, matrix, target compounds, and reported limitations.

**Must not claim:** Do not convert a condition-specific finding into a universal PFAS treatment claim.

### Frozen task components

- `WF10_025-T01`: Describe evidence relevant to contact-time planning for short-chain PFAS adsorption by powdered activated carbon.
- `WF10_025-T02`: Describe evidence relevant to contact-time planning for long-chain PFAS adsorption by powdered activated carbon.
- `WF10_025-T03`: Explain how compound, matrix, material, and operating conditions constrain a single contact-time recommendation.

### Complete gold evidence

**WF10_025_MMG001** (required_gold; `2020 - Son - The Adsorption Selectivity of Short and Long Per- and Polyfluoroalkyl Substances (PFASs) from Surface Water Using Powder-Activated Carbon.pdf`, chunk `1`)
> [SOURCE_TEXT_OMITTED sha256=3fec3692c896c9aca0d5d09826c568aade707b018fa886e6ca2e63659ae1b770]

### Normative content claim groups

#### WF10_025-G01

- Component: `WF10_025-T02`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: In surface water treated with powdered activated carbon, long-chain PFAS reach about 80% of adsorption equilibrium by 60 minutes and about 90% by 120 minutes.
- Material qualifiers: ["Matrix is surface water.", "Adsorbent is powdered activated carbon.", "Endpoint is adsorption toward equilibrium, not complete equilibrium.", "Approximately 80% of equilibrium is reached at 60 minutes.", "Approximately 90% of equilibrium is reached at 120 minutes."]
- Evidence: WF10_025_MMG001
- Prior atomic claims: WF10_025-C01
- Full: FULL if the answer states that in (or under conditions clearly limited to) surface water treated with powdered activated carbon, long-chain PFAS reach approximately 80% of adsorption equilibrium at about 60 minutes and approximately 90% of equilibrium at about 120 minutes, and makes clear that these percentages represent fractions of equilibrium rather than necessarily full equilibrium. Minor wording differences and synonymous time or percentage phrases matching accepted_numeric_equivalents are allowed.
- Partial: PARTIAL if the answer correctly indicates that long-chain PFAS in a surface water–PAC system approach adsorption equilibrium within about 1–2 hours with at least one of the two specific approximate fractions (either ~80% at ~60 minutes or ~90% at ~120 minutes) correct, but omits the other fraction or time, or does not clearly identify that the reported values are fractions of equilibrium while still not misrepresenting them as complete equilibrium.
- Contradiction: CONTRADICTED if the answer asserts a substantially different kinetic pattern for long-chain PFAS (e.g., that they require several hours to reach similar fractions, or that they reach near-complete equilibrium in far less than an hour under these conditions), gives clearly incorrect key percentages or times (e.g., swapping long- and short-chain times, or claiming 80–90% is reached only after 240 minutes), or explicitly denies that these values were observed in a surface water–PAC system.

#### WF10_025-G02

- Component: `WF10_025-T01`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: In the same surface water–powdered activated carbon system, short-chain PFAS require about 240 minutes of contact time to reach approximately 85% of adsorption equilibrium.
- Material qualifiers: ["Matrix is surface water.", "Adsorbent is powdered activated carbon.", "Endpoint is adsorption toward equilibrium, not complete equilibrium.", "Approximately 85% of equilibrium is reached at about 240 minutes."]
- Evidence: WF10_025_MMG001
- Prior atomic claims: WF10_025-C02
- Full: FULL if the answer states that in (or under conditions clearly limited to) the same surface water system using powdered activated carbon, short-chain PFAS require about 240 minutes (around 4 hours) of contact time to reach approximately 85% of adsorption equilibrium, and indicates that this is a fraction of equilibrium rather than necessarily full equilibrium. Synonymous expressions matching accepted_numeric_equivalents are allowed.
- Partial: PARTIAL if the answer correctly conveys that short-chain PFAS in a surface water–PAC system equilibrate more slowly than long-chain PFAS and require several hours of contact time, with at least one of the specific numerical details (either ~240 minutes or ~85% of equilibrium) correct, but omits or clearly approximates the other detail, or fails to explicitly note that this is a fraction of equilibrium without misrepresenting it as complete equilibrium.
- Contradiction: CONTRADICTED if the answer claims that short-chain PFAS in this system equilibrate as fast as or faster than long-chain PFAS (e.g., reaching similar fractions of equilibrium within 60–120 minutes), asserts clearly different key kinetics (e.g., that 85% equilibrium is reached much sooner than 240 minutes or only after far longer times under the same conditions), or explicitly denies the reported 240-minute, ~85% equilibrium finding.

#### WF10_025-G03

- Component: `WF10_025-T03`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: Because short-chain PFAS equilibrate more slowly than long-chain PFAS in this surface water–PAC system, planning a single PAC contact time for treating both groups under similar conditions should be based on the slower short-chain kinetics, implying a contact time on the order of the longer equilibration period (around 240 minutes) if the goal is to reach comparable fractions of adsorption equilibrium for both groups.
- Material qualifiers: ["Reasoning is specific to the studied surface water matrix and powdered activated carbon adsorption system.", "The recommendation is inferential, derived from the reported relative equilibration times (short-chain slower than long-chain), not a direct protocol instruction in the source.", "The implied contact time is on the order of the longer equilibration period (~240 minutes).", "The planning goal is to reach similar fractions of adsorption equilibrium for both PFAS groups, not necessarily full equilibrium."]
- Evidence: WF10_025_MMG001
- Prior atomic claims: WF10_025-C03
- Full: FULL if the answer explains that, in this surface water–PAC adsorption context, when selecting a single PAC contact time to treat both short- and long-chain PFAS to similar fractions of equilibrium, the design should be controlled by the slower-equilibrating short-chain PFAS (rather than the faster long-chain PFAS), and it reasonably situates the resulting contact time as being on the order of the longer observed equilibration period (around 240 minutes) while explicitly or implicitly limiting the inference to conditions comparable to the study. The answer must acknowledge that this is an inference or planning implication from the reported kinetics rather than a directly stated protocol in the source.
- Partial: PARTIAL if the answer correctly states that a single contact time for treating both short- and long-chain PFAS in this surface water–PAC system should be governed by the slower short-chain PFAS kinetics, but either omits any indication of the approximate time scale (e.g., does not reference that this implies several hours or ~240 minutes), or fails to clearly note that this is an inference based on the kinetics rather than a direct protocol statement, while still not presenting it as a universally applicable PFAS treatment rule.
- Contradiction: CONTRADICTED if the answer claims or implies that in this system a single contact time for treating both groups should be set by the faster long-chain PFAS kinetics (e.g., suggesting 60–120 minutes is adequate for both without qualification), or presents the derived 240-minute planning value as a universal PFAS treatment requirement beyond conditions comparable to the studied surface water–PAC system.

#### WF10_025-G04

- Component: `WF10_025-T03`
- Importance: `core`
- Function: `limitation`
- Scoring role: `required_content`
- Proposition: In this study’s surface water–PAC system, the reported percentages for short- and long-chain PFAS represent approximate fractions of equilibrium rather than full equilibrium, so the associated contact times should not be treated as guaranteed times to reach complete equilibrium or as universally applicable beyond similar surface water–PAC conditions.
- Material qualifiers: ["Matrix is the studied surface water; other water qualities are not characterized in the cited finding.", "Adsorbent is powdered activated carbon.", "Reported values (80%, 90%, 85%) are approximate fractions of equilibrium, not full equilibrium.", "Because the values are approximate fractions in a specific system, the reported contact times should not be treated as guaranteed times to reach complete equilibrium or as broadly generalizable beyond similar surface water–PAC conditions."]
- Evidence: WF10_025_MMG001
- Prior atomic claims: WF10_025-C04
- Full: FULL if the answer notes that in this surface water–PAC system the reported percentages for short- and long-chain PFAS are approximate fractions of equilibrium (not full equilibrium) and explains that, as a result, the associated contact times should not be treated as guaranteed times to reach complete equilibrium or as universally applicable outside conditions similar to the studied surface water–PAC system.
- Partial: PARTIAL if the answer correctly identifies at least one major limitation (for example, that the reported percentages are only approximate fractions of equilibrium, or that they are specific to this surface water–PAC system) and indicates that this constrains treating the reported times as complete-equilibrium or universally generalizable values, but omits one or more of the other listed material qualifiers.
- Contradiction: CONTRADICTED if the answer states or clearly implies that the reported percentages represent full equilibrium, or that the associated contact times are guaranteed times to reach complete equilibrium across a wide range of matrices and conditions, without limiting them to systems comparable to the studied surface water–PAC adsorption setup.


### Prior atomic-claim dispositions

#### WF10_025-C01

- Prior claim: In a surface water matrix treated with powder activated carbon, long-chain PFAS reached approximately 80% of adsorption equilibrium within 60 minutes and approximately 90% of equilibrium within 120 minutes.
- Action: `mapped`
- Final target(s): WF10_025-G01
- Rationale: Directly restates the long-chain PFAS equilibration percentages and times in the surface water–PAC system; fully captured as a required-content kinetics claim for long-chain PFAS.

#### WF10_025-C02

- Prior claim: In the same surface water–powder activated carbon system, short-chain PFAS required about 240 minutes of contact time to reach approximately 85% of adsorption equilibrium.
- Action: `mapped`
- Final target(s): WF10_025-G02
- Rationale: Directly restates the short-chain PFAS equilibration time and fraction in the same system; fully captured as a required-content kinetics claim for short-chain PFAS.

#### WF10_025-C03

- Prior claim: When planning PAC contact time for simultaneous treatment of both short- and long-chain PFAS in surface water under conditions comparable to this study, the contact time should be at least on the order of the longer equilibration time (around 240 minutes) if the goal is to achieve similar fractions of adsorption equilibrium for both PFAS groups.
- Action: `mapped`
- Final target(s): WF10_025-G03
- Rationale: Captures the inferential contact-time planning recommendation based on the comparative kinetics of short- versus long-chain PFAS; represented as a core synthesis group specific to the studied surface water–PAC context.

#### WF10_025-C04

- Prior claim: The reported percentages of approximately 80–90% equilibrium for long-chain PFAS at 60–120 minutes and approximately 85% equilibrium for short-chain PFAS at 240 minutes represent approximate fractions of adsorption equilibrium rather than full equilibrium, so longer contact times may be needed if near-complete equilibrium is desired.
- Action: `mapped`
- Final target(s): WF10_025-G04
- Rationale: Provides the limitation that the reported percentages are approximate fractions of equilibrium rather than full equilibrium and supports the broader limitation that these study-specific fractions and times should not be treated as universally generalizable complete-equilibrium values.

#### WF10_025-C05

- Prior claim: The contact times and equilibrium fractions reported for short- and long-chain PFAS adsorption on powder activated carbon are specific to a single surface water matrix and do not include PAC dose, individual compound rate constants, or data for matrices other than surface water, which limits direct transfer of these contact times to other systems.
- Action: `mapped`
- Final target(s): WF10_025-B01
- Rationale: Addresses that the findings from this surface water–PAC system should not be generalized into a universal PFAS treatment rule, which is encoded as an explicit boundary constraint in B01.

### Constraint-only groups

- `WF10_025-B01`: Do not generalize the study’s surface water–PAC contact times and equilibrium fractions into a universal PFAS treatment rule across all water types and operating conditions.
  Violation rule: A boundary violation occurs if the answer presents the reported contact times or equilibrium fractions as generally or universally required for PFAS removal across water types or treatment conditions, rather than limiting them to conditions comparable to the studied surface water–PAC adsorption system.

### Model B verification

Overall verdict: **approve**

- `WF10_025-G01`: **supported**. Canonical proposition and all material qualifiers (matrix, adsorbent, endpoint, both percentage/time pairs) are directly entailed by the exact span. Numeric equivalents (60 min/1 hour, 120 min/2 hours) are reasonable and claim-specific. Full/partial/contradiction rules are executable and internally consistent.
  Recommended change: None.
- `WF10_025-G02`: **supported**. Directly restates the short-chain equilibration finding with matching qualifiers; numeric equivalents (240 min/4 hours, 85%) are claim-specific and correctly attributed to the short-chain compound group only.
  Recommended change: None.
- `WF10_025-G03`: **supported**. This is the synthesized protocol-planning inference flagged by the prior Model B review as needing either reclassification or explicit inference-flagging. The revision resolves this by keeping the group core (justified since T03 explicitly asks for this synthesis) while requiring the full_rule to demand the answer 'acknowledge that this is an inference ... rather than a directly stated protocol in the source.' This directly addresses the earlier concern about overstating evidentiary directness without misrepresenting the finding as a literal quote.
  Recommended change: None required; retaining as a judgment call for project-author sign-off (already flagged in human_review_priorities).
- `WF10_025-G04`: **supported**. Limitation content (approximate, non-complete equilibrium fractions; study-specific to surface water) is entailed by the evidence span's own qualifying language ('Approximately... equilibria'). Dose/rate-constant/other-matrix gaps flagged in the prior atomic claim (C05/does_not_support) have correctly been moved out of scored full/partial rules and into the non-scored unresolved_or_unsupported list, resolving the earlier concern about relying on non-span metadata fields as scored support.
  Recommended change: None.
- `WF10_025-B01`: **supported**. Correctly framed as constraint_only and excluded from coverage; violation_rule is executable (checks for universalization beyond conditions comparable to the studied surface water–PAC system) and matches the must_not_claim task boundary.
  Recommended change: None.

Human-review priorities:
- G03's core/required_content classification remains a judgment call: it is a synthesized inference (synthesis_required=true) rather than a literal restatement, though the ledger now requires the answer to explicitly flag it as an inference — acceptable but worth final project-author confirmation given the sparse single-record gold set for this protocol_extraction task.
- G04 (required_content limitation) and B01 (constraint_only) address overlapping non-generalization content; this does not create double-counted required-content weight since B01 is excluded from the coverage denominator, but the project author may want to confirm this separation reads cleanly downstream.
- The gold set for this question consists of a single non-exhaustive record; all four core claim groups and the one constraint group derive from the same exact_evidence_span, which is appropriate given the available evidence but leaves no independent corroboration if that single record's phrasing is later corrected.

### Non-normative reference prose

In a surface water matrix treated with powdered activated carbon (PAC), long-chain PFAS reached approximately 80% of adsorption equilibrium within about 60 minutes and about 90% of equilibrium within about 120 minutes. In the same surface water–PAC system, short-chain PFAS required about 240 minutes of contact time to reach approximately 85% of adsorption equilibrium.

Because the short-chain PFAS equilibrated more slowly than the long-chain PFAS in this experiment, planning a single PAC contact time for treating both groups under similar surface water–PAC conditions should be governed by the slower short-chain kinetics if the goal is to achieve comparable fractions of adsorption equilibrium for both groups. In practice, this implies choosing a contact time on the order of the longer observed equilibration period (around 240 minutes), recognizing that this is an inference from the reported kinetics rather than a protocol statement explicitly given in the study.

These kinetics are specific to the reported surface water matrix and PAC adsorption system. The study reports approximate fractions of equilibrium (80–90% for long-chain PFAS at 60–120 minutes and about 85% for short-chain PFAS at 240 minutes), not full equilibrium, so the associated contact times should not be treated as guaranteed times to reach complete equilibrium or as universal PFAS treatment requirements outside systems comparable to this surface water–PAC context.

### Prose-to-ledger map

- In a surface water matrix treated with powdered activated carbon (PAC), long-chain PFAS reached approximately 80% of adsorption equilibrium within about 60 minutes and about 90% of equilibrium within about 120 minutes. -> WF10_025-G01
- In the same surface water–PAC system, short-chain PFAS required about 240 minutes of contact time to reach approximately 85% of adsorption equilibrium. -> WF10_025-G02
- Because the short-chain PFAS equilibrated more slowly than the long-chain PFAS in this experiment, planning a single PAC contact time for treating both groups under similar surface water–PAC conditions should be governed by the slower short-chain kinetics if the goal is to achieve comparable fractions of adsorption equilibrium for both groups. -> WF10_025-G03
- In practice, this implies choosing a contact time on the order of the longer observed equilibration period (around 240 minutes), recognizing that this is an inference from the reported kinetics rather than a protocol statement explicitly given in the study. -> WF10_025-G03
- These kinetics are specific to the reported surface water matrix and PAC adsorption system. -> WF10_025-G04
- The study reports approximate fractions of equilibrium (80–90% for long-chain PFAS at 60–120 minutes and about 85% for short-chain PFAS at 240 minutes), not full equilibrium, so the associated contact times should not be treated as guaranteed times to reach complete equilibrium or as universal PFAS treatment requirements outside systems comparable to this surface water–PAC context. -> WF10_025-G01, WF10_025-G02, WF10_025-G04, WF10_025-B01

---

## WF10_030

**Question:** Under what conditions might supercritical water oxidation leave uncertainty about fluorinated products?

**Must include:** Use limitation, uncertainty, caveat, and negative evidence to avoid overclaiming beyond the reported study scope.

**Must not claim:** Do not convert a condition-specific finding into a universal PFAS treatment claim.

### Frozen task components

- `WF10_030-T01`: Identify the conditions under which supercritical water oxidation evidence leaves uncertainty about fluorinated products.

### Complete gold evidence

**WF10_030_MMG001** (required_gold; `2023 - Li - PFOS destruction in a continuous supercritical water oxidation reactor.pdf`, chunk `1`)
> [SOURCE_TEXT_OMITTED sha256=df18556a56815be6fbd9c5b8cd543f66672e0bcd9522c2dad92ab274948882c8].

**WF10_030_MMG002** (required_gold; `2021 - Pinkard - Destruction of perfluorooctanesulfonate (PFOS) in a batch supercritical water oxidation reactor.pdf`, chunk `1`)
> [SOURCE_TEXT_OMITTED sha256=7454baf423fad18cf260e97c56d02d9ae340bdcf5a0d679f5d482d4bf97a8285].

**WF10_030_MMG003** (optional_gold; `2026 - Su - ReaxFF simulation of the degradation mechanism of perfluorononanoic acid (PFNA) by supercritical water oxidation.pdf`, chunk `6`)
> However, SCWO experimental studies on identifying PFAS degradation intermediates are still incomplete.

### Normative content claim groups

#### WF10_030-G01

- Component: `WF10_030-T01`
- Importance: `core`
- Function: `negative_finding`
- Scoring role: `required_content`
- Proposition: In a SCWO reactor treating PFAS-impacted matrices, trifluoroacetic acid (TFA) persisted in the effluent at about 600 °C and a residence time of roughly 32 seconds as the most recalcitrant intermediate, indicating that under these high-temperature, short-residence conditions a fluorinated intermediate remains and the fate of fluorine in the effluent is not fully resolved.
- Material qualifiers: ["SCWO reactor", "PFAS-impacted matrices", "temperature about 600 °C", "residence time about 32 seconds", "TFA is described as the most recalcitrant intermediate product in the effluent", "persistence of TFA under these conditions indicates a remaining fluorinated intermediate and unresolved fluorine fate in the effluent"]
- Evidence: WF10_030_MMG001
- Prior atomic claims: WF10_030-C01
- Full: Full credit if the answer states that in a SCWO reactor treating PFAS-impacted matrices, TFA persists in the effluent as a recalcitrant intermediate at roughly 600 °C and on the order of tens of seconds residence time (about 32 s), and explicitly links this persistence to residual uncertainty about fluorinated products or fluorine fate in the effluent. All listed qualifiers (reactor being a SCWO system, PFAS-impacted matrices, approximate temperature, short residence time, and recalcitrant nature of TFA) must be correct if mentioned; minor omissions are handled under partial credit.
- Partial: Partial credit if the answer correctly conveys that a fluorinated intermediate such as TFA persists under high-temperature SCWO of PFAS-impacted matrices and that this persistence leaves uncertainty about fluorinated products or fluorine fate, but omits at least one material qualifier (e.g., does not mention temperature or residence time) without introducing any incompatible statements.
- Contradiction: Mark as contradicted if the answer asserts that under SCWO of PFAS-impacted matrices at around 600 °C and short residence times (on the order of tens of seconds), no fluorinated intermediates such as TFA remain, that TFA is completely destroyed, or otherwise clearly denies persistence of fluorinated intermediates or related uncertainty under these conditions.

#### WF10_030-G03

- Component: `WF10_030-T01`
- Importance: `core`
- Function: `negative_finding`
- Scoring role: `required_content`
- Proposition: In SCWO experiments at 425 and 450 °C, a low fluorine mass balance was observed, which may indicate the existence of fluorinated species in the gaseous and/or liquid product phases that were not detected by the targeted analytical methods, leaving uncertainty about fluorinated products under those temperature and analytical conditions.
- Material qualifiers: ["SCWO experiments", "temperatures of about 425 and 450 °C", "low fluorine mass balance under these conditions", "interpretation that missing fluorine may be in fluorinated species in gaseous and/or liquid products that are not detected by targeted analyses", "uncertainty is tied to both the temperature regime and limitations of targeted analysis"]
- Evidence: WF10_030_MMG002
- Prior atomic claims: WF10_030-C03
- Full: Full credit if the answer reports that in SCWO experiments at approximately 425–450 °C a low fluorine mass balance was observed and that this is interpreted as possibly due to undetected fluorinated species in gas and/or liquid phases not captured by targeted analysis, leading to uncertainty about fluorinated products under these specific conditions.
- Partial: Partial credit if the answer correctly conveys that at some lower temperatures in SCWO the fluorine mass balance is incomplete and suggests undetected fluorinated species, creating uncertainty, but omits at least one material qualifier (e.g., exact temperatures or the mention of both gas and liquid phases) and does not introduce any incompatible claim.
- Contradiction: Mark as contradicted if the answer states that at around 425–450 °C in the reported SCWO experiments the fluorine mass balance is complete with no missing fluorine, or clearly denies the possibility of undetected fluorinated species under those conditions.

#### WF10_030-G04

- Component: `WF10_030-T01`
- Importance: `supplementary`
- Function: `negative_finding`
- Scoring role: `optional_content`
- Proposition: SCWO experimental studies on identifying PFAS degradation intermediates have been described as still incomplete, so for the systems studied there is general uncertainty about the full set of fluorinated intermediates and products.
- Material qualifiers: ["statement applies to SCWO experimental studies on PFAS degradation intermediates reported in the evidence", "intermediate identification is described as incomplete", "uncertainty is described for the studied systems, not as a universal property of all SCWO conditions"]
- Evidence: WF10_030_MMG003
- Prior atomic claims: WF10_030-C04
- Full: Full credit for this optional group if the answer explains that SCWO studies on PFAS degradation intermediates are described as still incomplete, and that this incompleteness leaves uncertainty about the full set of fluorinated intermediates and products for the systems studied, while keeping the claim scoped to those studies rather than all possible SCWO conditions.
- Partial: Partial credit for this optional group if the answer notes in general terms that SCWO studies on PFAS degradation intermediates are incomplete or that not all intermediates have been identified in the available experiments, without overgeneralizing to all SCWO applications.
- Contradiction: Mark as contradicted for this group if the answer asserts that SCWO experimental studies on PFAS degradation intermediates comprehensively identify all intermediates and fluorinated products, denying the reported incompleteness.

#### WF10_030-G05

- Component: `WF10_030-T01`
- Importance: `supplementary`
- Function: `affirmative`
- Scoring role: `optional_content`
- Proposition: Because TFA was observed as a persistent, recalcitrant intermediate in SCWO effluent, the study explicitly emphasized the need for TFA monitoring in SCWO treatment of PFAS-impacted matrices to track this fluorinated intermediate.
- Material qualifiers: ["need for TFA monitoring arises from observations in SCWO of PFAS-impacted matrices", "TFA is a persistent, recalcitrant fluorinated intermediate in the effluent", "monitoring is explicitly emphasized in the study text"]
- Evidence: WF10_030_MMG001
- Prior atomic claims: WF10_030-C01
- Full: Full credit if the answer explains that the SCWO study explicitly emphasized the need for TFA monitoring in SCWO treatment of PFAS-impacted matrices, and links this monitoring recommendation to the observation that TFA persists as a recalcitrant fluorinated intermediate in the effluent.
- Partial: Partial credit if the answer mentions that monitoring persistent intermediates such as TFA is needed or recommended to address uncertainty in fluorinated products during SCWO of PFAS, but does not clearly tie this to PFAS-impacted matrices, provided it does not misattribute the need.
- Contradiction: Mark as contradicted if the answer states that there is no need to monitor TFA or similar recalcitrant intermediates in SCWO of PFAS-impacted matrices despite their observed persistence, or claims that such monitoring is not recommended in the cited study.

#### WF10_030-G07

- Component: `WF10_030-T01`
- Importance: `supplementary`
- Function: `limitation`
- Scoring role: `optional_content`
- Proposition: Across the reported SCWO studies, observations such as persistent TFA at 600 °C in SCWO, low fluorine mass balance at 425–450 °C, and incomplete identification of PFAS degradation intermediates indicate that, under these specific experimental conditions, the evidence does not establish complete defluorination or fully resolve all fluorinated products and fluorine fate.
- Material qualifiers: ["limitation applies to the specific SCWO systems, PFAS compounds, and temperature regimes reported in the evidence", "based on persistent intermediates such as TFA, low fluorine mass balance, and incomplete identification of intermediates and products", "does not generalize to all PFAS or all possible SCWO operating conditions"]
- Evidence: WF10_030_MMG001, WF10_030_MMG002, WF10_030_MMG003
- Prior atomic claims: WF10_030-C05
- Full: Full credit for this optional group if the answer states that, under the particular SCWO experimental conditions described in the studies, the evidence does not establish complete defluorination or fully resolve the identity and fate of all fluorinated products, and ties this limitation to observations such as persistent TFA, incomplete fluorine mass balance, or incomplete identification of degradation intermediates, without generalizing to all possible SCWO conditions.
- Partial: Partial credit if the answer mentions that complete defluorination or full product identification is not demonstrated in the cited SCWO studies, but does not clearly connect this to specific observations (e.g., TFA persistence or low fluorine mass balance), as long as it does not claim universal SCWO failure.
- Contradiction: Mark as contradicted if the answer asserts that the cited SCWO studies demonstrate complete defluorination and fully identify and resolve all fluorinated products and fluorine fate under the reported conditions, or otherwise denies the stated limitations.


### Prior atomic-claim dispositions

#### WF10_030-C01

- Prior claim: In a continuous-flow SCWO reactor treating PFAS-impacted matrices containing PFOS, TFA was the most recalcitrant intermediate observed, persisting in the effluent at 600 °C with a residence time of about 32 s and necessitating explicit TFA monitoring, indicating that fluorinated intermediates can remain under these conditions and leave uncertainty about complete fluorine transformation.
- Action: `revised`
- Final target(s): WF10_030-G01, WF10_030-G05
- Rationale: The original atomic claim combined the observation of persistent TFA at 600 °C/~32 s with its implication for uncertainty and the explicit recommendation for TFA monitoring. These aspects are preserved in two linked groups: G01 captures the condition-specific uncertainty about fluorinated products arising from persistent TFA, and G05 captures the explicit need for TFA monitoring as stated in the study. Flow-mode details are not enforced because they are not present in the exact evidence span.

#### WF10_030-C02

- Prior claim: In the same continuous-flow SCWO system operated at 420–530 °C, volatile organofluorine compounds including 1H‑perfluoroalkane were detected in the gaseous products, and GC/MS spectra only suggested the presence of other volatile organofluorines without definitively identifying them, so at 420–530 °C the specific fluorinated gas-phase products remain uncertain.
- Action: `deleted`
- Final target(s): (deleted)
- Rationale: The original atomic claim relied on details about volatile organofluorines at 420–530 °C (including 1H-perfluoroalkane and GC/MS-suggested species) that are not present in any supplied exact_evidence_span. Because exact spans control factual attribution and no literal supporting text is available in the packet, this atomic claim cannot be cleanly grounded and is removed from the final ledger.

#### WF10_030-C03

- Prior claim: In batch SCWO experiments with PFOS at 425 and 450 °C, a low fluorine mass balance was observed, which may indicate the presence of fluorinated species in the gas and/or liquid product phases that were not detected by the targeted analytical methods, leaving uncertainty about fluorinated products under these temperature and analytical conditions.
- Action: `revised`
- Final target(s): WF10_030-G03
- Rationale: The original atomic claim focuses on low fluorine mass balance at 425–450 °C in PFAS SCWO and the inferred presence of undetected fluorinated species. G03 preserves this condition-specific uncertainty with wording directly supported by the exact evidence span, without enforcing reactor-type or specific compound details that appear only in metadata.

#### WF10_030-C04

- Prior claim: SCWO experimental studies aimed at identifying PFAS degradation intermediates have been described as incomplete, with undetected liquid-phase products and a lack of gas-phase volatile organofluorine analysis complicating assessment of the fluorine element balance, so whenever intermediate identification and gas-phase VOF analysis are incomplete, SCWO leaves uncertainty about which fluorinated products are present.
- Action: `revised`
- Final target(s): WF10_030-G04, WF10_030-B01
- Rationale: The original atomic claim generalized from incomplete SCWO studies to a broad conditional about SCWO always leaving uncertainty when analyses are incomplete. G04 narrows this to a statement, grounded in the exact span, that SCWO studies on PFAS degradation intermediates are still incomplete for the systems studied, implying remaining uncertainty. B01 encodes the boundary that these study-specific limitations must not be turned into universal SCWO failure claims.

#### WF10_030-C05

- Prior claim: The observations of persistent TFA, unidentified volatile organofluorines, and incomplete fluorine mass balances in these SCWO studies do not establish complete defluorination or mineralization and highlight that the identity and quantity of all fluorinated products remain unresolved under the reported conditions.
- Action: `revised`
- Final target(s): WF10_030-G07, WF10_030-B01
- Rationale: The original synthesis claim that current studies do not establish complete defluorination or fully resolve all fluorinated products is preserved as G07, scoped to the specific experimental conditions and supported by the combination of persistent TFA, low fluorine mass balance, and incomplete studies. B01 captures the associated boundary that these limitations should not be generalized to all SCWO treatment of PFAS.

### Constraint-only groups

- `WF10_030-B01`: Findings about uncertainty in fluorinated products from specific PFAS SCWO experiments (e.g., at particular temperatures with particular analytical suites) must not be generalized into a universal claim that SCWO cannot fully destroy PFAS or always leaves fluorinated products uncertain under all conditions.
  Violation rule: Flag a boundary violation if the answer extrapolates the reported, condition-specific uncertainties (persistent TFA, low fluorine mass balance, incomplete intermediate identification) into an unqualified statement that SCWO universally fails to achieve complete PFAS destruction or that fluorinated products are always uncertain for all PFAS and all SCWO operating conditions.

### Model B verification

Overall verdict: **approve**

- `WF10_030-G01`: **supported**. The prior Model B flag (unsupported 'continuous-flow' descriptor embedded as a required qualifier) has been resolved: G01's material_qualifiers, canonical_proposition, and full_rule no longer mention 'continuous-flow'; the group now reads 'a SCWO reactor treating PFAS-impacted matrices,' which is fully entailed by the exact_evidence_span (TFA as most recalcitrant intermediate, persistence at 600°C, ~32 s residence, PFAS-impacted matrices, implied monitoring need).
  Recommended change: None.
- `WF10_030-G03`: **supported**. The prior Model B flag (unsupported 'batch reactor' and 'PFOS' descriptors) has been resolved: G03's qualifiers, canonical_proposition, and full_rule now say only 'SCWO experiments' with no reactor-mode or compound-identity requirement, matching the exact_evidence_span verbatim (low fluorine mass balance at 425/450°C, possible undetected fluorinated species in gas/liquid, targeted-analysis limitation).
  Recommended change: None.
- `WF10_030-G04`: **supported**. Narrowed correctly to the literal span ('SCWO experimental studies on identifying PFAS degradation intermediates are still incomplete'); the PFNA attribution and the unsupported liquid/gas-phase VOF detail flagged previously have been dropped, and the group is appropriately scoped as optional/supplementary rather than a universalized conditional.
  Recommended change: None.
- `WF10_030-G05`: **supported**. Content (explicit TFA monitoring recommendation) is entailed by the same exact_evidence_span as G01. The prior Model B duplicate/weighting concern (G05 scored as a second core/required_content item off the same single sentence as G01) is resolved: G05 is now importance=supplementary, scoring_role=optional_content, so it no longer competes with G01 for required-content weight. The unsupported 'continuous-flow' qualifier is also gone.
  Recommended change: None.
- `WF10_030-G07`: **supported**. Synthesis group correctly marked synthesis_required=true, scoped to 'the specific experimental conditions ... does not generalize to all PFAS or all possible SCWO operating conditions,' and each component fact traces to a literal exact_evidence_span. Appropriately optional_content so it does not inflate required-content weight alongside G01/G03.
  Recommended change: None.
- `WF10_030-B01`: **supported**. Constraint-only group, correctly excluded from coverage scoring, with an executable violation_rule tied to the must_not_claim boundary (no unqualified universal SCWO-failure statement). No evidence_ids needed since it is a boundary constraint rather than a factual claim.
  Recommended change: None.

Human-review priorities:
- Confirm against the source PDF (2023 Li, chunk 1) whether the volatile-organofluorine/1H-perfluoroalkane detail at 420–530°C (present in MMG001's supported_claim/limitation metadata but absent from the supplied exact_evidence_span) actually appears elsewhere in that chunk; if confirmed, consider adding it back as a separate span-grounded optional claim group rather than leaving it fully dropped.
- G04 (single-fact: SCWO intermediate identification is incomplete) and G07 (synthesis spanning MMG001+MMG002+MMG003, including the same incompleteness fact) both score as optional_content and share partial factual overlap; this is low-risk since neither is required_content, but confirm the scoring pipeline does not let a single generic sentence answer both groups' full_rule simultaneously.
- The removal of atomic claim C02 (VOF/420–530°C detail) via outright deletion, rather than a hedged/annotated retention, is a stricter application of the exact-span discipline than the prior Model B review suggested (which recommended keeping a caveated version); confirm this stricter standard is the intended project convention going forward.

### Non-normative reference prose

Evidence from PFAS SCWO experiments shows that uncertainty about fluorinated products arises under specific operating and analytical conditions.

In a SCWO reactor treating PFAS-impacted matrices, trifluoroacetic acid (TFA) remained in the effluent at about 600 °C and a residence time of roughly 32 seconds as the most recalcitrant intermediate. Its persistence under these high-temperature, short-residence conditions indicates that a fluorinated intermediate can remain in the effluent and that the fate of fluorine is not fully resolved. In SCWO experiments at 425 and 450 °C, a low fluorine mass balance was observed, which the authors interpret as possibly indicating fluorinated species in the gaseous and/or liquid products that were not detected by the targeted analytical methods; under these temperatures and analytical conditions, the identity and distribution of fluorinated products therefore remain uncertain. More generally, SCWO experimental work on PFAS degradation intermediates has been described as incomplete, implying that not all fluorinated intermediates and products have been identified for the systems studied.

In particular, the SCWO study explicitly emphasizes the need for monitoring TFA during SCWO treatment of PFAS-impacted matrices, so that this persistent fluorinated intermediate can be tracked. More complete fluorine mass-balance information and more comprehensive identification of intermediates and products under the reported conditions would be required before the experiments could demonstrate complete defluorination or fully resolve the identity and fate of all fluorinated products.

### Prose-to-ledger map

- In a SCWO reactor treating PFAS-impacted matrices, trifluoroacetic acid (TFA) remained in the effluent at about 600 °C and a residence time of roughly 32 seconds as the most recalcitrant intermediate. -> WF10_030-G01
- Its persistence under these high-temperature, short-residence conditions indicates that a fluorinated intermediate can remain in the effluent and that the fate of fluorine is not fully resolved. -> WF10_030-G01
- In SCWO experiments at 425 and 450 °C, a low fluorine mass balance was observed, which the authors interpret as possibly indicating fluorinated species in the gaseous and/or liquid products that were not detected by the targeted analytical methods; under these temperatures and analytical conditions, the identity and distribution of fluorinated products therefore remain uncertain. -> WF10_030-G03
- More generally, SCWO experimental work on PFAS degradation intermediates has been described as incomplete, implying that not all fluorinated intermediates and products have been identified for the systems studied. -> WF10_030-G04
- In particular, the SCWO study explicitly emphasizes the need for monitoring TFA during SCWO treatment of PFAS-impacted matrices, so that this persistent fluorinated intermediate can be tracked. -> WF10_030-G05
- More complete fluorine mass-balance information and more comprehensive identification of intermediates and products under the reported conditions would be required before the experiments could demonstrate complete defluorination or fully resolve the identity and fate of all fluorinated products. -> WF10_030-G07

---

## WF10_004a

**Question:** How does PFAS chain length affect reported treatment performance or adsorption behavior?

**Must include:** Compare studies only on matched compounds, matrices, endpoints, and conditions; avoid ranking technologies when the evidence is not comparable.

**Must not claim:** Do not convert a condition-specific finding into a universal PFAS treatment claim.

### Frozen task components

- `WF10_004a-T01`: Describe how PFAS chain length affects reported treatment performance.
- `WF10_004a-T02`: Describe how PFAS chain length affects adsorption or equilibrium behavior.
- `WF10_004a-T03`: State the compound, matrix, endpoint, and condition restrictions needed for cross-study interpretation.

### Complete gold evidence

**WF10_004a_MMG001** (required_gold; `2023 - Smaili - Adsorption as a remediation technology for short-chain per- and polyfluoroalkyl substances (PFAS) from water - a critical review.pdf`, chunk `18`)
> [SOURCE_TEXT_OMITTED sha256=b74e79a570d1149a404456da98719dd9a8a13619b8d733a9d0fbc9f3c80523e1].

**WF10_004a_MMG002** (required_gold; `2025 - Kebede - Adsorptive Removal of PFAS from Aqueous Solutions Using GAC, PAC and Ball-Milled Colloidal Activated Carbon - Characterizing Efficiency, Kinetics,.pdf`, chunk `18`)
> [SOURCE_TEXT_OMITTED sha256=23c92cd59d9fae3215bf0958e36d6ae28c1de0341ff2924d16551f212b88e948].

**WF10_004a_MMG003** (optional_gold; `2023 - Smaili - Adsorption as a remediation technology for short-chain per- and polyfluoroalkyl substances (PFAS) from water - a critical review.pdf`, chunk `29`)
> [SOURCE_TEXT_OMITTED sha256=ee0fc9f7a3f6ef8dee3c8c277b23e9307230af5a77b74a00b9baaa1619d87e1d].

**WF10_004a_MMG004** (optional_gold; `2026 - Sadmani - A critical review of the application of biochar in removing perfluoroalkyl and polyfluoroalkyl substances (PFAS) from water matrices.pdf`, chunk `37`)
> [SOURCE_TEXT_OMITTED sha256=1044cd21c880dc0df68e663beb668672c8ff6a812913e5c7b851a5e7d07dd973]].

**WF10_004a_MMG005** (optional_gold; `2025 - Hamza - Understanding PFAS Adsorption - How Molecular Structure Affects Sustainable Water Treatment.pdf`, chunk `21`)
> [SOURCE_TEXT_OMITTED sha256=1dd3a790b53e312490f36e35b956affdcf0c5dbbebed7969dab1660eaf263d0b].

**WF10_004a_MMG006** (negative_gold; `2022 - Vu - Recent progress in adsorptive removal of per- and poly-fluoroalkyl substances (PFAS) from water-wastewater.pdf`, chunk `63`)
> [SOURCE_TEXT_OMITTED sha256=a4e24844122d64243186fa2139524777c322ada9cb8d51793ac13f84e0e116e1].

### Normative content claim groups

#### WF10_004a-G01

- Component: `WF10_004a-T01`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: In aqueous adsorption- or sorbent-based treatments, longer-chain PFAS generally show higher removal efficiencies than shorter-chain PFAS under comparable conditions, although removal efficiencies are also influenced by other factors and can show contradictory patterns across different waters, adsorbents, and experimental conditions.
- Material qualifiers: ["context is aqueous solutions (water and wastewater)", "context is adsorption- or sorbent-based treatments (e.g., across sorbents and carbonaceous adsorbents)", "comparisons are made under the same experimental conditions or across the same sorbents", "other factors (e.g., matrix composition, adsorbent properties) and contradictory results limit the predictive power of chain length alone"]
- Evidence: WF10_004a_MMG001, WF10_004a_MMG002, WF10_004a_MMG003, WF10_004a_MMG006
- Prior atomic claims: WF10_004a-C01, WF10_004a-C02, WF10_004a-C03
- Full: Assign full credit if the answer states that, in aqueous adsorption- or sorbent-based PFAS treatments, longer-chain PFAS have higher (or often better) removal efficiencies than shorter-chain PFAS when compared under the same conditions or across the same sorbents, and also notes that removal efficiencies are influenced by other factors and can show contradictory patterns across different waters, adsorbents, and experimental conditions, so chain length alone does not fully determine performance.
- Partial: Assign partial credit if the answer correctly states that longer-chain PFAS have higher or often better removal efficiencies than shorter-chain PFAS in aqueous adsorption/sorbent-based systems, but does not clearly specify that the comparison is under comparable conditions, or only vaguely mentions that other factors or variability exist without clearly indicating that contradictory results occur or that chain length alone is not determinative. The answer must not extend the trend to all treatment technologies or non-aqueous settings.
- Contradiction: Mark as contradicted if the answer asserts that, in aqueous adsorption- or sorbent-based treatments, short-chain PFAS generally have equal or higher removal efficiencies than longer-chain PFAS, or if it explicitly denies that chain length is associated with higher removal for longer-chain PFAS in these systems.

#### WF10_004a-G03

- Component: `WF10_004a-T02`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: In adsorption studies from water matrices, longer-chain PFAS are more hydrophobic and less water-soluble, which leads to higher adsorption capacities onto adsorbents than for shorter-chain PFAS.
- Material qualifiers: ["described in reviews of adsorption onto biochar and related adsorbents", "matrix is water", "applies to adsorption capacities in the reviewed adsorption literature, not to non-adsorptive processes"]
- Evidence: WF10_004a_MMG004
- Prior atomic claims: WF10_004a-C04
- Full: Assign full credit if the answer explains that, in adsorption from water matrices, longer-chain PFAS are more hydrophobic and less water-soluble, and that these properties lead to higher adsorption capacities compared with shorter-chain PFAS.
- Partial: Assign partial credit if the answer correctly states that longer-chain PFAS have higher adsorption capacities than shorter-chain PFAS in water adsorption systems but omits either the hydrophobicity/water-solubility explanation or the explicit restriction to water matrices or adsorption-based behavior.
- Contradiction: Mark as contradicted if the answer claims that, in adsorption from water matrices, shorter-chain PFAS generally have higher adsorption capacities than longer-chain PFAS, or if it explicitly denies that longer-chain PFAS are more hydrophobic and less water-soluble.

#### WF10_004a-G04

- Component: `WF10_004a-T02`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: Mechanistic discussions of PFAS adsorption indicate that chain length and molecular orientation significantly influence the adsorption process, with long-chain PFAS interacting via their hydrophobic tails through hydrophobic interactions.
- Material qualifiers: ["based on adsorption-focused review work, not a single specific adsorbent", "highlights that long-chain PFAS can interact via hydrophobic tails through hydrophobic interactions", "emphasizes the role of chain length and orientation in governing adsorption behavior"]
- Evidence: WF10_004a_MMG005
- Prior atomic claims: WF10_004a-C05
- Full: Assign full credit if the answer notes that PFAS chain length (and molecular orientation) significantly affects adsorption behavior, and explains that long-chain PFAS can interact via their hydrophobic tails through hydrophobic interactions.
- Partial: Assign partial credit if the answer correctly states that chain length and/or molecular orientation significantly influence PFAS adsorption, or that long-chain PFAS interact via hydrophobic tails and hydrophobic interactions, but does not clearly tie both ideas together.
- Contradiction: Mark as contradicted if the answer asserts that chain length does not significantly influence PFAS adsorption mechanisms, or denies that long-chain PFAS can interact via hydrophobic tails through hydrophobic interactions in adsorption contexts.

#### WF10_004a-G05

- Component: `WF10_004a-T03`
- Importance: `core`
- Function: `boundary_constraint`
- Scoring role: `required_content`
- Proposition: Based on the available adsorption literature, meaningful cross-study comparisons of chain-length effects on PFAS removal are best made when compounds, matrices, adsorbents, and experimental conditions are matched, because differing waters, adsorbents, and conditions can produce contradictory removal results even for the same chain lengths, and the available evidence is limited to adsorption-based PFAS removal from water and wastewater.
- Material qualifiers: ["key elements to match include PFAS compounds (long- vs short-chain analogues), water or wastewater matrix, adsorbent type, and experimental conditions", "in adsorptive removal from water and wastewater, contradictory results are often reported across different waters, adsorbents, and conditions", "within-study comparisons under fixed conditions (e.g., same adsorbents and matrix) provide clearer chain-length contrasts and underpin this interpretive guidance", "the cited evidence focuses on adsorption- or sorbent-based removal from water and wastewater, so it does not establish chain-length effects for non-adsorptive treatment technologies"]
- Evidence: WF10_004a_MMG002, WF10_004a_MMG006
- Prior atomic claims: WF10_004a-C06
- Full: Assign full credit if the answer explains that, based on the available adsorption evidence, careful cross-study interpretation of chain-length effects should compare studies with matched PFAS compounds, water/wastewater matrices, adsorbents, and experimental conditions, because differing waters, adsorbents, or conditions can lead to contradictory removal outcomes that complicate interpretation. The answer should also recognize that the underlying evidence pertains to adsorption-based removal from water and wastewater and does not establish chain-length effects for non-adsorptive treatment technologies.
- Partial: Assign partial credit if the answer either (a) emphasizes that cross-study comparisons should match some, but not all, of the key elements (e.g., compounds and adsorbents but not matrix or conditions), or (b) mentions that contradictory results across waters/adsorbents/conditions limit comparability but does not clearly translate this into a requirement to match specific comparison dimensions, or (c) confines the scope of the evidence to adsorption-based water/wastewater treatments without explicitly tying this to cross-study comparison requirements.
- Contradiction: Mark as contradicted if the answer suggests that cross-study comparisons of chain-length effects can be made without regard to differences in compounds, matrices, adsorbents, or experimental conditions, or if it implies that contradictory results across differing conditions are not a concern for interpreting chain-length effects, or if it treats adsorption-based findings as universally valid for all treatment types without qualification.


### Prior atomic-claim dispositions

#### WF10_004a-C01

- Prior claim: In the aqueous sorbent-based systems reviewed by Smaili et al., the removal efficiency of long-chain PFAS was higher than that of short-chain PFAS across all sorbents considered.
- Action: `mapped`
- Final target(s): WF10_004a-G01
- Rationale: C01 describes the general review-level trend that long-chain PFAS have higher removal efficiencies than short-chain PFAS across sorbents in aqueous systems, which is captured as part of the broader cross-study treatment-performance trend in G01.

#### WF10_004a-C02

- Prior claim: In batch adsorption experiments with aqueous solutions using granular activated carbon, powdered activated carbon, and ball-milled colloidal activated carbon, the long-chain PFAS PFOA and PFOS showed higher removal efficiencies (73% ± 24% and 89% ± 35%, respectively) than the short-chain PFAS PFBA and PFBS (30% ± 11% and 55% ± 18%), demonstrating greater adsorption of long-chain PFAS on these carbonaceous adsorbents under the tested conditions.
- Action: `mapped`
- Final target(s): WF10_004a-G01
- Rationale: C02 provides a specific batch-study example showing higher removal for long-chain PFAS under matched conditions, reinforcing the general treatment-performance pattern included in G01.

#### WF10_004a-C03

- Prior claim: Using a PEI-f-CMC sorbent in aqueous solutions, PFOS and PFOA achieved high removal efficiencies of 98.8% and 87.6%, respectively, while the overall removal efficiency of short-chain PFAS was described as much lower, highlighting the greater difficulty of removing short-chain PFAS relative to long-chain PFAS with this adsorbent.
- Action: `mapped`
- Final target(s): WF10_004a-G01
- Rationale: C03, once corrected to remove the unsupported sorbent identity, contributes the supported point that short-chain PFAS have much lower removal than long-chain PFAS in the reviewed aqueous sorbent-based systems, which is part of the overall trend summarized in G01.

#### WF10_004a-C04

- Prior claim: In reviews of PFAS adsorption onto biochar and related adsorbents from water matrices, longer-chain PFAS are described as more hydrophobic and less water-soluble, which leads to higher adsorption capacities compared to shorter-chain analogues.
- Action: `mapped`
- Final target(s): WF10_004a-G03
- Rationale: C04 directly matches G03’s proposition that longer-chain PFAS are more hydrophobic and less water-soluble, leading to higher adsorption capacities in water matrices.

#### WF10_004a-C05

- Prior claim: Mechanistic discussion of PFAS adsorption indicates that long-chain PFAS can interact via their hydrophobic tails through hydrophobic interactions, and that chain length and molecular orientation significantly influence the adsorption process, whereas shorter-chain PFAS, with fewer fluorine moieties, exhibit weaker hydrophobic interactions and rely more on electrostatic interactions in adsorption systems.
- Action: `mapped`
- Final target(s): WF10_004a-G04
- Rationale: C05, narrowed to the supported content about long-chain PFAS hydrophobic-tail interactions and the influence of chain length and orientation on adsorption, is fully captured in G04.

#### WF10_004a-C06

- Prior claim: A review of PFAS adsorptive removal from water and wastewater reports that removal efficiencies are often better for long-chained PFAS but also notes that many other factors influencing large-scale removal efficiencies, such as water and wastewater organic and inorganic content and adsorbent properties, remain poorly understood and that contradictory results are frequently reported across different waters, adsorbents, and experimental conditions.
- Action: `mapped`
- Final target(s): WF10_004a-G05
- Rationale: C06 reports that removal efficiencies are often better for long-chained PFAS but that many factors remain unknown and contradictory results occur across waters, adsorbents, and conditions; G05 uses this as the primary evidence for cross-study comparison restrictions and interpretive guidance.

#### WF10_004a-C07

- Prior claim: The available review evidence on chain-length effects emphasizes that, although long-chained PFAS often show higher removal efficiencies than short-chained PFAS, contradictory results across water and wastewater matrices, adsorbents, and experimental conditions mean that chain length alone does not fully determine treatment performance in adsorption-based systems.
- Action: `mapped`
- Final target(s): WF10_004a-B01
- Rationale: C07 synthesizes limitation findings about contradictory results and the insufficiency of chain length as a sole predictor; this is used in B01 to define a constraint against universalizing longer-chain superiority across all contexts.

### Constraint-only groups

- `WF10_004a-B01`: Do not claim that longer-chain PFAS always have superior treatment performance across all matrices, adsorbents, and treatment types, because contradictory results and other influencing factors are reported for adsorptive removal from water and wastewater.
  Violation rule: Flag a boundary violation if the answer asserts or clearly implies that longer-chain PFAS invariably or universally have superior treatment performance or removal efficiencies across all matrices, adsorbents, and treatment technologies, without acknowledging exceptions or contradictory results.
- `WF10_004a-B02`: Do not rank or directly compare different PFAS treatment technologies on the basis of chain length when the underlying evidence is not drawn from matched compounds, matrices, endpoints, and conditions.
  Violation rule: Flag a boundary violation if the answer uses chain-length effects observed in one set of conditions (e.g., adsorption in water) to rank or compare fundamentally different treatment technologies under non-comparable compounds, matrices, endpoints, or operational conditions.

### Model B verification

Overall verdict: **approve**

- `WF10_004a-G01`: **supported**. The PEI-f-CMC sorbent misattribution flagged in the prior first-pass review of C03 has been removed: neither the canonical_proposition, material_qualifiers, nor the reference-answer paragraph 3 name a sorbent for the MMG003 span, matching the gold record's own does_not_support annotation. The group correctly combines the affirmative long-chain>short-chain trend (MMG001, MMG002, MMG003) with the MMG006 limitation (other factors, contradictory results) inside a single canonical_proposition and full_rule, so the negative/limitation evidence is used as a qualifier rather than converted into unqualified positive support, and the trend is not universalized beyond adsorption/sorbent-based aqueous systems.
  Recommended change: None required.
- `WF10_004a-G03`: **supported**. Canonical proposition, qualifiers, and rules track the MMG004 span (hydrophobicity/solubility -> adsorption capacity) exactly, restricted to water matrices and adsorption literature.
  Recommended change: None required.
- `WF10_004a-G04`: **supported**. The prior-review flag on C05 (short-chain electrostatic-interaction content traceable only to the gold record's supported_claim field, not its exact_evidence_span) has been resolved by dropping that unsupported portion entirely rather than caveating it; the canonical_proposition, material_qualifiers, and full/partial/contradiction rules now track only what the MMG005 span states (long-chain hydrophobic-tail interaction, chain length/orientation influence).
  Recommended change: None required.
- `WF10_004a-G05`: **supported**. The prior Model B finding that G05 presented a 'matching requirement' as if directly entailed by MMG002 is addressed: the exact_spans block now explicitly labels the MMG002 support type as 'illustrative_example_for_matched_conditions' (versus 'direct' for MMG006), the material_qualifiers state that the matched-condition example 'underpin[s] this interpretive guidance' rather than asserting the requirement is stated in the source, and reference-answer paragraph 4 now uses hedged synthesis language ('the available findings imply... as illustrated by') instead of presenting it as a direct source finding. This is a defensible ledger-level synthesis for a cross_study_comparison task, not an unresolved inference-beyond-span defect.
  Recommended change: None required.
- `WF10_004a-B01`: **supported**. Violation rule is executable and correctly derived from MMG006's negative/limitation span without converting it into a positive universal claim; excluded from coverage scoring as constraint_only.
  Recommended change: None required.
- `WF10_004a-B02`: **supported**. Restates task_boundaries.must_not_claim with an executable violation_rule; the previously missing grounding pointer has been added ('grounding': 'task_boundaries.must_not_claim'), making its non-gold-evidence origin explicit and auditable as the prior Model B review requested.
  Recommended change: None required.

Human-review priorities:
- MMG006's single exact_evidence_span is still scored as core/required evidence in three constructs (G01, G05, B01) and MMG002 in two (G01, G05); each usage supports a genuinely distinct proposition (general performance trend+limitation vs. cross-study matching guidance vs. anti-universalization constraint), which the prior Model B review already judged defensible non-duplication — confirm this remains intended scoring behavior before audit rather than incidental credit inflation from a single reference-answer sentence.
- Each claim group carries both a 'canonical_proposition' and a 'central_proposition' field that largely restate each other; consider consolidating for ledger clarity, though this is not a scoring defect.
- Gold record WF10_004a_MMG005's 'supported_claim' field asserts short-chain electrostatic-interaction behavior that its own 'exact_evidence_span' does not contain; the ledger correctly restricted G04 to only the span-supported long-chain content, but the underlying gold record itself may still warrant a span-widening or supported_claim-trimming fix at the gold-curation stage (pre-existing issue, not introduced by this revision).

### Non-normative reference prose

Within the supplied evidence, PFAS chain length is evaluated in the context of adsorption- or sorbent-based treatments for water and wastewater. Across these aqueous adsorption systems, longer-chain PFAS are generally reported to have higher treatment performance, in the sense of higher removal efficiencies, than shorter-chain analogues when they are tested under comparable conditions.

A critical review of sorbent-based removal from water found that, across the sorbents examined, long-chain PFAS consistently exhibited higher removal efficiencies than short-chain PFAS. This trend is echoed in a batch study using granular activated carbon, powdered activated carbon, and ball-milled colloidal activated carbon in aqueous solutions, where the long-chain compounds PFOA and PFOS were removed at substantially higher percentages than the shorter-chain PFBA and PFBS under the same experimental conditions. Another review notes that, relative to long-chain PFOS and PFOA, the overall removal efficiency of short-chain PFAS from aqueous solutions was much lower, underscoring the greater difficulty of removing shorter-chain PFAS in these sorbent-based systems. At the same time, a broader review of adsorptive PFAS removal from water and wastewater emphasizes that, although removal efficiencies are often better for long-chained PFAS, many other influencing factors remain poorly understood and contradictory removal results are frequently reported across different waters, adsorbents, and experimental conditions. This indicates that chain length alone does not fully determine treatment performance in adsorption-based treatments.

Regarding adsorption and equilibrium behavior, reviews of PFAS adsorption onto biochar and related adsorbents from water matrices describe longer-chain PFAS as more hydrophobic and less water-soluble than their shorter-chain counterparts, which leads to higher adsorption capacities onto these adsorbents. Mechanistic discussion of PFAS adsorption further notes that long-chain PFAS can interact via their hydrophobic tails through hydrophobic interactions, and that the chain length and orientation of PFAS molecules significantly influence the adsorption process.

For cross-study interpretation of chain-length effects, the available findings imply that the clearest contrasts come from studies that compare long- and short-chain PFAS under matched conditions, such as within one batch experiment using the same adsorbents and aqueous matrix, as illustrated by the PFOA/PFOS versus PFBA/PFBS comparison. The review of adsorptive removal from water and wastewater reports that contradictory results are often obtained when waters, adsorbents, or experimental conditions differ, suggesting that cross-study comparisons should be made only when compounds, matrices, adsorbents, and key operating conditions are aligned. In addition, all of the cited work is focused on adsorption- or sorbent-based removal of PFAS from water and wastewater; these findings therefore do not establish how chain length affects performance of non-adsorptive treatment technologies.

### Prose-to-ledger map

- Within the supplied evidence, PFAS chain length is evaluated in the context of adsorption- or sorbent-based treatments for water and wastewater. -> WF10_004a-G01, WF10_004a-G03, WF10_004a-G04, WF10_004a-G05
- Across these aqueous adsorption systems, longer-chain PFAS are generally reported to have higher treatment performance, in the sense of higher removal efficiencies, than shorter-chain analogues when they are tested under comparable conditions. -> WF10_004a-G01
- A critical review of sorbent-based removal from water found that, across the sorbents examined, long-chain PFAS consistently exhibited higher removal efficiencies than short-chain PFAS. -> WF10_004a-G01
- This trend is echoed in a batch study using granular activated carbon, powdered activated carbon, and ball-milled colloidal activated carbon in aqueous solutions, where the long-chain compounds PFOA and PFOS were removed at substantially higher percentages than the shorter-chain PFBA and PFBS under the same experimental conditions. -> WF10_004a-G01, WF10_004a-G05
- Another review notes that, relative to long-chain PFOS and PFOA, the overall removal efficiency of short-chain PFAS from aqueous solutions was much lower, underscoring the greater difficulty of removing shorter-chain PFAS in these sorbent-based systems. -> WF10_004a-G01
- At the same time, a broader review of adsorptive PFAS removal from water and wastewater emphasizes that, although removal efficiencies are often better for long-chained PFAS, many other influencing factors remain poorly understood and contradictory removal results are frequently reported across different waters, adsorbents, and experimental conditions. -> WF10_004a-G01, WF10_004a-G05
- This indicates that chain length alone does not fully determine treatment performance in adsorption-based treatments. -> WF10_004a-G01
- Regarding adsorption and equilibrium behavior, reviews of PFAS adsorption onto biochar and related adsorbents from water matrices describe longer-chain PFAS as more hydrophobic and less water-soluble than their shorter-chain counterparts, which leads to higher adsorption capacities onto these adsorbents. -> WF10_004a-G03
- Mechanistic discussion of PFAS adsorption further notes that long-chain PFAS can interact via their hydrophobic tails through hydrophobic interactions, and that the chain length and orientation of PFAS molecules significantly influence the adsorption process. -> WF10_004a-G04
- For cross-study interpretation of chain-length effects, the available findings imply that the clearest contrasts come from studies that compare long- and short-chain PFAS under matched conditions, such as within one batch experiment using the same adsorbents and aqueous matrix, as illustrated by the PFOA/PFOS versus PFBA/PFBS comparison. -> WF10_004a-G05
- The review of adsorptive removal from water and wastewater reports that contradictory results are often obtained when waters, adsorbents, or experimental conditions differ, suggesting that cross-study comparisons should be made only when compounds, matrices, adsorbents, and key operating conditions are aligned. -> WF10_004a-G05
- In addition, all of the cited work is focused on adsorption- or sorbent-based removal of PFAS from water and wastewater; these findings therefore do not establish how chain length affects performance of non-adsorptive treatment technologies. -> WF10_004a-G05, WF10_004a-B01

---

## WF10_004b

**Question:** How can PFAS compound class or headgroup affect treatment performance or equilibrium behavior?

**Must include:** Compare studies only on matched compounds, matrices, endpoints, and conditions; avoid ranking technologies when the evidence is not comparable.

**Must not claim:** Do not convert a condition-specific finding into a universal PFAS treatment claim.

### Frozen task components

- `WF10_004b-T01`: Describe how PFAS compound class or headgroup affects reported treatment performance.
- `WF10_004b-T02`: Describe how PFAS compound class or headgroup affects adsorption or equilibrium behavior.
- `WF10_004b-T03`: State the compound, matrix, endpoint, and condition restrictions needed for cross-study interpretation.

### Complete gold evidence

**WF10_004b_MMG001** (required_gold; `2025 - Saha - Foam fractionation of PFAS from landfill leachate using a membrane electrochemical reactor.pdf`, chunk `1`)
> [SOURCE_TEXT_OMITTED sha256=9267fd3f47c2241ef937a6540c6b77c49ce38a341deeba7e69a88142941cd948].

**WF10_004b_MMG002** (negative_gold; `2025 - Meng - Complete Aqueous Defluorination of GenX Hexafluoropropylene Oxide Dimer Acid Anion by Pulsed.pdf`, chunk `14`)
> [SOURCE_TEXT_OMITTED sha256=143b48b3cbd21f4e2378eef11059312f080d408dc1e06d82b34a5a7eaa167f13]

**WF10_004b_MMG003** (required_gold; `2021 - Liu - Pilot-scale field demonstration of a hybrid nanofiltration and UV-sulfite treatment train for groundwater contaminated by per- and polyfluoroalkyl.pdf`, chunk `17`)
> [SOURCE_TEXT_OMITTED sha256=ec94b010a0258744fed2e60dcacc0b8cdd2334eec3c889e9c3dc00f10639704f].

**WF10_004b_MMG004** (required_gold; `2023 - Lauwers - Adsorption of PFAS by All-Silica Zeolite β - Insights into the Effect of the Water Matrix, Regeneration of the Material, and Continuous PFAS.pdf`, chunk `34`)
> [SOURCE_TEXT_OMITTED sha256=6f53559af02714793ca579e8ed55c11f0f4338764b7442de73c6271cc17faec6].

**WF10_004b_MMG005** (optional_gold; `2023 - Wang - Removing per- and polyfluoroalkyl substances (PFAS) in water by foam fractionation.pdf`, chunk `36`)
> [SOURCE_TEXT_OMITTED sha256=a415e691e3be498886bdc14a63ccc51ffbde0827bea3e72db77e1a7206c33f92].

**WF10_004b_MMG006** (optional_gold; `2026 - Sadmani - A critical review of the application of biochar in removing perfluoroalkyl and polyfluoroalkyl substances (PFAS) from water matrices.pdf`, chunk `31`)
> [SOURCE_TEXT_OMITTED sha256=8b5f8307d7e34dc948917d638b816b76dae73dcb840522830a7d790fb556f893].

**WF10_004b_MMG007** (optional_gold; `2025 - Uwayezu - Efficient removal of PFAS in groundwater and landfill leachate using iron-modified peat residues and electrochemical oxidation.pdf`, chunk `19`)
> [SOURCE_TEXT_OMITTED sha256=eba319cd7e8f6a4fb168d4b099931888c13270cdb5de151cf88b6daa0715aa22].

### Normative content claim groups

#### WF10_004b-G01

- Component: `WF10_004b-T01`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: In foam fractionation, perfluorosulfonic acids are removed more efficiently than perfluorocarboxylic acids under the reported conditions, indicating a headgroup-driven performance difference for matched PFAS types.
- Material qualifiers: ["comparison is between sulfonate and carboxylate PFAS", "finding is specific to the reported foam fractionation systems and matrices, not universal"]
- Evidence: WF10_004b_MMG001, WF10_004b_MMG005
- Prior atomic claims: WF10_004b-C01, WF10_004b-C02, WF10_004b-C03
- Full: Award full credit if the answer states that in foam fractionation systems, perfluorosulfonic acids (sulfonates) show higher or more efficient removal than perfluorocarboxylic acids (carboxylates), and makes clear that this is based on the reported foam fractionation studies rather than asserted as a universal rule.
- Partial: Award partial credit if the answer notes a headgroup-related difference in foam fractionation performance but (a) is vague about which class is removed more efficiently, or (b) omits that the finding is specific to the reported systems and could be interpreted as broadly universal, while still not explicitly claiming universality.
- Contradiction: Mark as contradicted if the answer explicitly claims that foam fractionation removes perfluorocarboxylic acids more efficiently than perfluorosulfonic acids under comparable conditions, or asserts that foam fractionation performance does not differ by headgroup at all, without qualification.

#### WF10_004b-G04

- Component: `WF10_004b-T01`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: In iron-based treatment systems (zero-valent iron, zero-valent iron plus biochar, and iron-modified peat columns), sulfonate PFAS are removed or retained more than carboxylate PFAS of comparable chain length under the reported conditions.
- Material qualifiers: ["includes batch tests with zero-valent iron (ZVI) and ZVI plus biochar in water", "includes column treatment with iron-modified peat residues for groundwater and landfill leachate", "comparisons are between sulfonate and carboxylate PFAS, with equal perfluorocarbon chain lengths in the column study", "finding is specific to these iron-based systems and conditions, not universal to all media"]
- Evidence: WF10_004b_MMG006, WF10_004b_MMG007
- Prior atomic claims: WF10_004b-C04, WF10_004b-C05, WF10_004b-C09
- Full: Award full credit if the answer states that in iron-based treatments (such as ZVI/ZVI+biochar or iron-modified peat columns), sulfonate PFAS show higher removal or retention than carboxylate PFAS under the reported conditions, and recognizes that this is specific to those systems.
- Partial: Award partial credit if the answer notes a sulfonate-versus-carboxylate difference in at least one iron-based system but omits that sulfonates perform better, or omits that these findings are specific to the studied iron-based media.
- Contradiction: Mark as contradicted if the answer asserts that in these iron-based studies carboxylate PFAS were removed or retained more than sulfonate PFAS, or that no headgroup-related difference was observed in such iron-based systems.

#### WF10_004b-G05

- Component: `WF10_004b-T01`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: In nanofiltration of groundwater at pH 7.3, FHxSA, which is likely neutral due to its sulfonamide headgroup, shows consistently lower rejection than the anionic sulfonate analogue PFHxS, attributed to the lack of electrostatic repulsion for the neutral species.
- Material qualifiers: ["matrix is groundwater at pH 7.3", "FHxSA is likely neutral at this pH because of its sulfonamide headgroup", "PFHxS is an anionic sulfonate analogue", "difference in rejection is attributed to absence of electrostatic repulsion for the neutral compound", "finding is specific to this pH and nanofiltration system"]
- Evidence: WF10_004b_MMG003
- Prior atomic claims: WF10_004b-C07
- Full: Award full credit if the answer explains that in a nanofiltration study of groundwater at pH ~7.3, a sulfonamide PFAS (FHxSA), likely neutral, had lower rejection than an anionic sulfonate analogue (PFHxS), and ties this to the absence of electrostatic repulsion for the neutral species.
- Partial: Award partial credit if the answer mentions a headgroup/charge-related difference in nanofiltration rejection between FHxSA and PFHxS but omits either the pH condition or the electrostatic repulsion explanation.
- Contradiction: Mark as contradicted if the answer claims that FHxSA had higher or similar rejection compared to PFHxS under these conditions, or misrepresents FHxSA as an anionic species at pH 7.3 in this context.

#### WF10_004b-G06

- Component: `WF10_004b-T02`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: For adsorption onto all-silica zeolite β in aqueous solution, sulfonic-acid PFAS exhibit lower adsorption capacity and affinity than carboxylic-acid PFAS, an effect attributed to the more polar sulfonic moiety and the unlikely formation of sulfonic acid dimers.
- Material qualifiers: ["adsorbent is all-silica zeolite β", "matrix is aqueous solution", "endpoint is adsorption capacity and affinity (equilibrium behavior)", "mechanistic explanation involves the more polar sulfonic moiety and unlikely formation of sulfonic acid dimers", "finding is specific to this adsorbent"]
- Evidence: WF10_004b_MMG004
- Prior atomic claims: WF10_004b-C06, WF10_004b-C09
- Full: Award full credit if the answer states that on all-silica zeolite β, sulfonic-acid PFAS have lower adsorption capacity/affinity than carboxylic-acid PFAS in aqueous solution, and notes that this is attributed to the polar sulfonic group and lack of dimer formation.
- Partial: Award partial credit if the answer correctly identifies that zeolite β favors adsorption of carboxylates over sulfonates, but omits the mechanistic explanation or the aqueous-solution qualifier.
- Contradiction: Mark as contradicted if the answer asserts that, on all-silica zeolite β, sulfonates adsorb more strongly than carboxylates or that there is no headgroup-related difference in adsorption capacity/affinity.

#### WF10_004b-G07

- Component: `WF10_004b-T02`
- Importance: `core`
- Function: `negative_finding`
- Scoring role: `required_content`
- Proposition: In the reported laser-made [Ni0.75Fe0.25]-(OH)2 hydrophilic carbon-fiber-paper anode study, PFAS headgroup identity did not govern adsorption; available adsorption sites and oxidant generation instead imposed a concentration limit on efficient defluorination under those study conditions.
- Material qualifiers: ["anode is laser-made [Ni0.75Fe0.25]-(OH)2 on hydrophilic carbon fiber paper", "the finding is condition-specific", "the expanded span discusses similar concentration dependence for GenX and PFOS but does not support a universal PFAS rule", "pulsed-electrolysis and LiOH details are not required by this claim group"]
- Evidence: WF10_004b_MMG002
- Prior atomic claims: WF10_004b-C08, WF10_004b-C09
- Full: Award full if the answer states that headgroup identity did not govern adsorption at the specified anode and identifies available sites or oxidant generation as the limiting anode characteristics, without adding unsupported process conditions.
- Partial: Award partial if the answer reports the negative headgroup finding but omits the anode-specific limiting characteristics.
- Contradiction: Mark contradicted if the answer says headgroup identity governed adsorption in this study or universalizes the finding.

#### WF10_004b-G08

- Component: `WF10_004b-T03`
- Importance: `core`
- Function: `limitation`
- Scoring role: `required_content`
- Proposition: Across the supplied studies, the influence of PFAS class or headgroup on treatment performance or adsorption is strongly process- and condition-specific, so cross-study interpretation must respect differences in technology, matrix, and matched PFAS analogues and cannot be generalized into a universal rule.
- Material qualifiers: ["different technologies show different headgroup trends: sulfonates perform better than carboxylates in foam fractionation and several iron-based systems, carboxylates adsorb more strongly than sulfonates on all-silica zeolite β, and one electrochemical adsorption system shows no governing headgroup effect", "comparisons in the cited studies are made for specific PFAS pairs or classes (e.g., sulfonate vs carboxylate of equal chain length, or sulfonamide vs sulfonate analogue) within the same matrix and treatment", "cross-study interpretation should therefore avoid ranking technologies without matched compounds, matrices, endpoints, and conditions"]
- Evidence: WF10_004b_MMG001, WF10_004b_MMG005, WF10_004b_MMG006, WF10_004b_MMG007, WF10_004b_MMG004, WF10_004b_MMG003, WF10_004b_MMG002
- Prior atomic claims: WF10_004b-C03, WF10_004b-C09, WF10_004b-C10
- Full: Award full credit if the answer explicitly states that the impact of PFAS class or headgroup on treatment performance/adsorption varies by technology, material, and conditions (i.e., is process-specific rather than universal), and uses this to caution that cross-study comparisons must involve matched compounds, matrices, endpoints, and conditions and should not be generalized into a single ranking of technologies.
- Partial: Award partial credit if the answer mentions that headgroup effects differ between some technologies or materials but does not clearly connect this to the need for matched compounds/matrices/conditions in cross-study interpretation, or if it cautions against overgeneralization without clearly acknowledging the presence of opposing or null trends across systems.
- Contradiction: Mark as contradicted if the answer claims or strongly implies that headgroup identity has a uniform effect on treatment or adsorption across technologies (e.g., sulfonates always outperform carboxylates in all systems) or uses heterogeneous evidence to rank technologies without regard to matched compounds, matrices, endpoints, and conditions.


### Prior atomic-claim dispositions

#### WF10_004b-C01

- Prior claim: In landfill leachate treated by membrane electrochemical reactor foam fractionation for seven hours, perfluorosulfonic acids were removed more efficiently than perfluorocarboxylic acids, with 98.3% PFSA removal versus 85.5% PFCA removal overall, and short-chain PFSAs (C≤6) showing 92.5–99.1% removal compared to 80.8–90% for short-chain PFCAs.
- Action: `mapped`
- Final target(s): WF10_004b-G01
- Rationale: C01 reports that in MER foam fractionation of landfill leachate, overall PFSA removal (98.3%) exceeded PFCA removal (85.5%) after seven hours. This directional foam-fractionation headgroup effect is fully represented in the foam-focused synthesis group G01; unverified short-chain (C≤6) percentage ranges are not used for scoring because they are not present in the exact_evidence_span.

#### WF10_004b-C02

- Prior claim: In laboratory-spiked water treated by foam fractionation, overall removal of PFHeA (a perfluorocarboxylic acid) was 55%, much less than the 96% overall removal of PFHeS (a perfluorosulfonic acid) of similar perfluorocarbon chain length.
- Action: `mapped`
- Final target(s): WF10_004b-G01
- Rationale: C02 describes that in a laboratory foam fractionation study, PFHeA had 55% overall removal while PFHeS reached 96%, showing a sulfonate-over-carboxylate advantage. This comparison is incorporated into the foam-fractionation synthesis in G01 without asserting unsupported chain-length equivalence.

#### WF10_004b-C03

- Prior claim: Across foam fractionation studies in landfill leachate and laboratory-spiked water, sulfonate PFAS were removed more effectively than carboxylate PFAS of comparable chain length, indicating that the sulfonate headgroup can enhance foam-based PFAS separation under those specific conditions.
- Action: `revised`
- Final target(s): WF10_004b-G01, WF10_004b-G08
- Rationale: C03 synthesizes sulfonate-favoring behavior across foam fractionation systems. Its core cross-system content—that sulfonate PFAS are removed more effectively than carboxylate PFAS in the reported foam fractionation studies and that this is process-specific—is captured in the broader heterogeneity and non-universality synthesis group G08. Disposition targets normalized from ['WF10_004b-G08'] to ['WF10_004b-G01', 'WF10_004b-G08'] using final source_atomic_claim_ids.

#### WF10_004b-C04

- Prior claim: Batch tests using zero-valent iron or zero-valent iron plus biochar in water showed that perfluorosulfonic acids were more efficiently removed, with up to 94% removal, whereas perfluorocarboxylic acids reached up to 60% removal under the same treatment types.
- Action: `mapped`
- Final target(s): WF10_004b-G04
- Rationale: C04 states that batch tests with ZVI or ZVI+biochar removed PFSAs more efficiently (up to 94%) than PFCAs (up to 60%). This iron-based sulfonate advantage is represented in G04.

#### WF10_004b-C05

- Prior claim: In column treatment with iron-modified peat residues for groundwater and landfill leachate, sulfonate PFAS showed higher retention than carboxylate PFAS of equal perfluorocarbon chain length, exemplified by 84% PFOS versus 72% PFNA removal and 64% PFHxS versus 44% PFHpA removal.
- Action: `mapped`
- Final target(s): WF10_004b-G04
- Rationale: C05 reports that iron-modified peat columns showed higher retention of sulfonate PFAS than carboxylate PFAS of equal chain length (e.g., PFOS vs PFNA, PFHxS vs PFHpA). This is incorporated in the iron-based synthesis group G04.

#### WF10_004b-C06

- Prior claim: For adsorption onto all-silica zeolite β in aqueous solution, the adsorption capacity and affinity were lower for perfluorosulfonic acids than for perfluorocarboxylic acids, which was attributed to the more polar sulfonic moiety and the unlikely formation of sulfonic acid dimers.
- Action: `mapped`
- Final target(s): WF10_004b-G06
- Rationale: C06 describes that on all-silica zeolite β, sulfonic acids have lower adsorption capacity and affinity than carboxylic acids, attributed to the more polar sulfonic moiety and lack of dimer formation. This is directly captured in G06.

#### WF10_004b-C07

- Prior claim: In nanofiltration of groundwater at pH 7.3, FHxSA, which is likely neutral due to its sulfonamide headgroup, exhibited consistently lower rejection than the anionic analogue PFHxS, with the lower rejection attributed to the lack of an electrostatic repulsion mechanism for the neutral sulfonamide species.
- Action: `mapped`
- Final target(s): WF10_004b-G05
- Rationale: C07 reports that in nanofiltration of groundwater at pH 7.3, neutral FHxSA had consistently lower rejection than anionic PFHxS, attributed to the absence of electrostatic repulsion. This nanofiltration headgroup/charge effect is represented in G05.

#### WF10_004b-C08

- Prior claim: During pulsed electrolysis in an aqueous LiOH electrolyte using laser-made [Ni0.75Fe0.25]-(OH)2–hydrophilic carbon fiber paper anodes, the chemical identity of the PFAS headgroup did not govern PFAS adsorption, indicating that anode characteristics, rather than headgroup type, controlled adsorption of PFOS and GenX under those conditions.
- Action: `mapped`
- Final target(s): WF10_004b-G07
- Rationale: C08 states that in pulsed electrolysis with laser-made [Ni0.75Fe0.25]-(OH)2 anodes in aqueous LiOH, PFAS adsorption was not governed by headgroup identity. This negative headgroup finding is preserved in G07.

#### WF10_004b-C09

- Prior claim: The supplied studies collectively show that PFAS class or headgroup can either increase or decrease treatment performance depending on the technology—enhancing removal for sulfonates in foam fractionation, zero-valent iron-based systems, and iron-modified peat columns, but reducing adsorption relative to carboxylates on all-silica zeolite β and not governing adsorption on a Ni–Fe hydroxide anode—demonstrating that headgroup effects are highly process-specific.
- Action: `revised`
- Final target(s): WF10_004b-G04, WF10_004b-G06, WF10_004b-G07, WF10_004b-G08
- Rationale: C09 is a high-level synthesis that headgroup effects differ across foam fractionation, iron-based systems, zeolite β adsorption, and the Ni–Fe anode, showing process-specific and sometimes opposing trends; this overarching process-specificity conclusion is captured in the synthesis group G08. Disposition targets normalized from ['WF10_004b-G08'] to ['WF10_004b-G04', 'WF10_004b-G06', 'WF10_004b-G07', 'WF10_004b-G08'] using final source_atomic_claim_ids.

#### WF10_004b-C10

- Prior claim: The observed influence of PFAS class or headgroup on treatment performance in the supplied studies is specific to the tested compounds, matrices, and materials, and does not establish a universal rule that headgroup identity will control removal or adsorption behavior for all PFAS and all treatment technologies.
- Action: `revised`
- Final target(s): WF10_004b-B01, WF10_004b-G08
- Rationale: C10 emphasizes that the observed headgroup influences are specific to tested compounds, matrices, and materials, and do not establish a universal rule that headgroup identity controls removal or adsorption. This non-universality and cross-study caution underpin the boundary constraint in B01. Disposition targets normalized from ['WF10_004b-B01'] to ['WF10_004b-B01', 'WF10_004b-G08'] using final source_atomic_claim_ids.

### Constraint-only groups

- `WF10_004b-B01`: The reference must not assert that PFAS headgroup identity universally controls treatment or adsorption performance across all PFAS and technologies.
  Violation rule: Flag a boundary violation if the answer claims or clearly implies that headgroup identity always or generally controls PFAS treatment or adsorption performance across all PFAS and technologies, or if it extrapolates system-specific findings into blanket treatment rules for PFAS.

### Model B verification

Overall verdict: **approve**

- `WF10_004b-G01`: **supported**. Canonical proposition (sulfonates removed more efficiently than carboxylates in foam fractionation) and its qualifiers are entailed by both quoted spans (98.3% vs 85.5%; 55% vs 96%). The prior C01/C02 partial-support concerns (unverifiable short-chain figures; unsupported chain-length-equivalence qualifier) are resolved: the group's canonical proposition and material_qualifiers omit both unsupported elements, and the C01/C03 disposition rationale explicitly notes the short-chain figures are excluded from scoring.
  Recommended change: None required; optionally add an explicit qualifier noting MMG005's span is self-flagged as truncated, for transparency to the project author.
- `WF10_004b-G04`: **supported**. Both spans directly entail the canonical proposition that iron-based systems (ZVI/ZVI+BC, iron-modified peat columns) show higher sulfonate removal/retention than carboxylates; the chain-length-matching qualifier is correctly scoped only to the column study where it is stated, not overextended to the batch study.
  Recommended change: None required.
- `WF10_004b-G05`: **supported**. Span directly entails neutral-headgroup/charge-based rejection difference and the electrostatic-repulsion mechanism; pH qualifier and compound attribution correctly match the source.
  Recommended change: None required.
- `WF10_004b-G06`: **supported**. Span directly entails the reversed (carboxylate-favoring) adsorption trend and mechanistic explanation for all-silica zeolite β; correctly flagged as adsorbent-specific.
  Recommended change: None required.
- `WF10_004b-G07`: **supported**. Negative finding is preserved as negative (headgroup did not govern adsorption) without conversion to a positive/universal claim, consistent with the record's does_not_support field; anode-specific limiting factors correctly attributed.
  Recommended change: None required.
- `WF10_004b-G08`: **supported**. Synthesis proposition (process-specific, non-universal, sometimes-opposing direction) is entailed by the combined spans and is a distinct claim from the individual system-level groups, not a redundant fragment. However, it reuses the same seven spans already scored under G01/G04/G05/G06/G07, which a scoring implementation must treat as synthesis-level credit rather than double-counting each span's denominator weight across two required_content groups.
  Recommended change: No ledger text change required; add an explicit scoring-implementation note (already present as a human_review_priority) that G08's evidence reuse is synthesis-level credit, not additional per-span denominator weight.
- `WF10_004b-B01`: **supported**. Violation rule is executable and correctly scoped to flag universalization of headgroup effects across all PFAS/technologies; properly excluded from coverage scoring (constraint_only).
  Recommended change: None required.

Human-review priorities:
- Confirm the scoring implementation treats G08's reuse of the seven system-specific evidence spans (shared with G01/G04/G05/G06/G07) as synthesis-level credit and does not double-count the same span's denominator weight across two required_content groups.
- G04 bundles two different papers/matrices (ZVI/ZVI+BC batch study and iron-modified peat column study) under one canonical proposition; defensible given the shared direction and correctly scoped chain-length qualifier, but remains a project-author judgment call rather than a required change.
- G01 similarly bundles two different papers/matrices (landfill leachate MER foam fractionation and lab-spiked-water foam fractionation); acceptable given shared direction and appropriately hedged qualifiers, but note MMG005's span is self-flagged as truncated/garbled, so residual source-quality uncertainty should be disclosed to the project author.
- The project-author review provenance is a blanket retention confirmation without item-specific rationale; acceptable as a basis for retaining the seven gold records given gold_is_non_exhaustive, but does not constitute independent double-annotation.

### Non-normative reference prose

Several foam-fractionation studies reported higher removal of sulfonate PFAS than carboxylate PFAS under their specific conditions. Iron-based batch and column systems likewise showed stronger removal or retention of sulfonates than matched carboxylates in the cited examples. In nanofiltration, neutral FHxSA showed lower rejection than anionic PFHxS because the neutral compound lacked an electrostatic-repulsion mechanism. All-silica zeolite beta showed the opposite class trend, with lower capacity and affinity for sulfonic-acid PFAS than for carboxylic-acid PFAS. At a laser-made [Ni0.75Fe0.25]-(OH)2 hydrophilic carbon-fiber-paper anode, headgroup identity did not govern adsorption; available sites and oxidant generation instead limited efficient defluorination at higher concentration. The direction of headgroup effects is therefore specific to the process, material, charge state, and conditions, and no universal headgroup rule is supported.

### Prose-to-ledger map

- Several foam-fractionation studies reported higher removal of sulfonate PFAS than carboxylate PFAS under their specific conditions. -> WF10_004b-G01
- Iron-based batch and column systems likewise showed stronger removal or retention of sulfonates than matched carboxylates in the cited examples. -> WF10_004b-G04
- In nanofiltration, neutral FHxSA showed lower rejection than anionic PFHxS because the neutral compound lacked an electrostatic-repulsion mechanism. -> WF10_004b-G05
- All-silica zeolite beta showed the opposite class trend, with lower capacity and affinity for sulfonic-acid PFAS than for carboxylic-acid PFAS. -> WF10_004b-G06
- At a laser-made [Ni0.75Fe0.25]-(OH)2 hydrophilic carbon-fiber-paper anode, headgroup identity did not govern adsorption; available sites and oxidant generation instead limited efficient defluorination at higher concentration. -> WF10_004b-G07
- The direction of headgroup effects is therefore specific to the process, material, charge state, and conditions, and no universal headgroup rule is supported. -> WF10_004b-G08, WF10_004b-B01

---

## WF10_036

**Question:** Does longer empty-bed contact time necessarily translate into better PFAS performance in granular activated carbon systems?

**Must include:** Use limitation, uncertainty, caveat, and negative evidence to avoid overclaiming beyond the reported study scope.

**Must not claim:** Do not convert a condition-specific finding into a universal PFAS treatment claim.

### Frozen task components

- `WF10_036-T01`: Describe the reported relationship between empty-bed contact time and PFAS performance in granular activated-carbon systems.
- `WF10_036-T02`: Explain why longer empty-bed contact time does not necessarily guarantee better performance across compounds and operating conditions.

### Complete gold evidence

**WF10_036_MMG001** (required_gold; `2019 - Park - Adsorption of perfluoroalkyl substances (PFAS) in groundwater by granular activated carbons - Roles of hydrophobicity of PFAS and carbon.pdf`, chunk `29`)
> 5 B), which means that the apparent adsorption capacity did not change as EBCT increased.

**WF10_036_MMG002** (required_gold; `2020 - Zeng - Removing per- and polyfluoroalkyl substances from groundwaters using activated carbon.pdf`, chunk `16`)
> [SOURCE_TEXT_OMITTED sha256=16759fcbe6cc6b6f11a3ab8a8c3e08bc7534bc1dac7cbfdfc4398184827547c0].

**WF10_036_MMG003** (optional_gold; `2020 - Zeng - Removing per- and polyfluoroalkyl substances from groundwaters using activated carbon.pdf`, chunk `15`)
> [SOURCE_TEXT_OMITTED sha256=841e03841b4a8125efc76df319357f9459b66328b79d9fbd905cdc31d4a869e2].

**WF10_036_MMG004** (optional_gold; `2022 - Kempisty - Granular activated carbon adsorption of perfluoroalkyl acids from ground and surface.pdf`, chunk `37`)
> [SOURCE_TEXT_OMITTED sha256=b332058668356c17d30e3fcf544edf5a269d1a3c4d8864cfe0f83751380be28f].

### Normative content claim groups

#### WF10_036-G01

- Component: `WF10_036-T01`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: Across the reported granular and activated carbon studies treating PFAS in groundwater and surface water, PFAS adsorption performance metrics were largely insensitive to changes in EBCT within the tested ranges, so these data do not support the assertion that longer EBCT necessarily leads to better PFAS performance.
- Material qualifiers: ["performance metrics considered included apparent adsorption capacity, ΣPFAS adsorption capacity and inferred mechanisms, breakthrough curve behavior, and carbon usage rate", "studies involved granular or activated carbon systems treating PFAS (including ΣPFAS and PFAAs) in groundwater or ground/surface waters", "the lack of systematic improvement is limited to the EBCT ranges and configurations tested in these studies", "therefore, the available data do not support a claim that longer EBCT necessarily leads to better PFAS performance in such systems"]
- Evidence: WF10_036_MMG001, WF10_036_MMG002, WF10_036_MMG003, WF10_036_MMG004
- Prior atomic claims: WF10_036-C05
- Full: Full credit if the answer states that in the reported PFAS granular/activated carbon studies, PFAS adsorption performance did not systematically improve with longer EBCT over the tested ranges, and explicitly links this to at least two distinct performance metrics (e.g., capacity, mechanisms, breakthrough behavior, carbon usage rate) and to the idea that these study data do not support a claim that longer EBCT necessarily leads to better PFAS performance, while constraining the conclusion to the kinds of systems and EBCT ranges studied.
- Partial: Partial credit if the answer correctly states that PFAS performance did not consistently or systematically improve with longer EBCT in the reported studies OR that the data do not show that longer EBCT necessarily leads to better performance, but omits key qualifiers about the metrics considered or the limited study conditions (e.g., matrices, PFAS classes, or EBCT ranges), or mentions only one performance metric without any broader synthesis, while not asserting that longer EBCT clearly improves performance.
- Contradiction: Mark as contradicted if the answer asserts that, according to the reported studies, PFAS performance generally or systematically improves with longer EBCT, or that the data show longer EBCT necessarily leads to better PFAS performance, without immediately and clearly correcting this claim.

#### WF10_036-G02

- Component: `WF10_036-T01`
- Importance: `supplementary`
- Function: `affirmative`
- Scoring role: `optional_content`
- Proposition: In a groundwater granular activated carbon system, the apparent adsorption capacity did not change as EBCT increased, indicating that longer EBCT did not enhance adsorption capacity under those conditions.
- Material qualifiers: ["matrix was groundwater", "adsorbent was granular activated carbon", "finding is limited to the EBCT range tested in that study", "the lack of change in capacity indicates no enhancement of adsorption capacity from longer EBCT under those study conditions"]
- Evidence: WF10_036_MMG001
- Prior atomic claims: WF10_036-C01
- Full: Full credit for this optional group if the answer notes that in at least one groundwater GAC study, the apparent adsorption capacity did not change as EBCT increased, and makes clear that this was in a groundwater granular activated carbon system over the tested EBCT range.
- Partial: Partial credit if the answer conveys that adsorption capacity did not increase with longer EBCT in a GAC system but omits either the groundwater matrix or the fact that the observation is limited to the study’s tested EBCT range, while still making clear it is a single-study finding.
- Contradiction: Mark as contradicted for this group if the answer explicitly claims that in the referenced groundwater GAC study, apparent adsorption capacity increased with longer EBCT, or otherwise states that the study showed improved capacity at longer EBCT, without correction.

#### WF10_036-G03

- Component: `WF10_036-T01`
- Importance: `supplementary`
- Function: `affirmative`
- Scoring role: `optional_content`
- Proposition: In groundwater activated carbon columns treating ΣPFAS, the ratio of ΣPFAS adsorption capacity between a Lead+Lag configuration and a Lead-only column was 1.07 ± 0.12, which the authors interpreted as adsorption mechanisms being independent of EBCT.
- Material qualifiers: ["PFAS endpoint was ΣPFAS adsorption capacity (qΣPFAS)", "matrix was groundwater", "comparison was between Lead+Lag and Lead-only column configurations", "reported ratio was approximately 1 (1.07 ± 0.12)", "the conclusion about EBCT independence is the study authors’ interpretation for that system"]
- Evidence: WF10_036_MMG002
- Prior atomic claims: WF10_036-C02
- Full: Full credit for this optional group if the answer states that in groundwater activated carbon columns treating ΣPFAS, the Lead+Lag versus Lead-only qΣPFAS ratio was close to 1 (about 1.07 ± 0.12) and that this was interpreted as indicating adsorption mechanisms were independent of EBCT for that system.
- Partial: Partial credit if the answer conveys that ΣPFAS adsorption capacities in Lead+Lag and Lead-only columns were essentially the same and interpreted as EBCT-independent mechanisms, but omits the specific ratio value or the ±0.12 uncertainty, while still identifying the groundwater ΣPFAS activated carbon context.
- Contradiction: Mark as contradicted for this group if the answer claims that the Lead+Lag configuration showed clearly higher ΣPFAS capacity than the Lead-only column (i.e., a ratio well above unity) or that the study indicated adsorption mechanisms depended strongly on EBCT, without correction.

#### WF10_036-G04

- Component: `WF10_036-T01`
- Importance: `supplementary`
- Function: `affirmative`
- Scoring role: `optional_content`
- Proposition: In rapid small-scale column tests with activated carbon treating groundwater, longer EBCTs did not show additional loss of performance from competing adsorbates, and similar breakthrough curve shapes indicated that shorter EBCTs of approximately 2–5 minutes already captured the mass transfer zone.
- Material qualifiers: ["tests were rapid small-scale column tests (RSSCTs) with activated carbon in a lead–lag configuration", "matrix was groundwater", "shorter EBCTs were approximately 2–5 minutes", "longer EBCTs did not show additional impact from competing adsorbates such as ionic species or dissolved organic carbon", "inference is based on similar breakthrough curve shapes across EBCTs in that study"]
- Evidence: WF10_036_MMG003
- Prior atomic claims: WF10_036-C03
- Full: Full credit for this optional group if the answer notes that in groundwater RSSCTs with activated carbon, shorter EBCTs of roughly 2–5 minutes already captured the mass transfer zone and that longer EBCTs did not show additional performance loss from competing adsorbates, as inferred from similar breakthrough curves.
- Partial: Partial credit if the answer mentions either that shorter EBCTs (around a few minutes) captured the mass transfer zone or that longer EBCTs did not show more impact from competing adsorbates, but not both, while correctly situating the finding in groundwater RSSCT activated carbon tests.
- Contradiction: Mark as contradicted for this group if the answer asserts that in these RSSCTs, only longer EBCTs (not shorter ~2–5 min EBCTs) captured the mass transfer zone, or that longer EBCTs suffered greater competition from co‑adsorbates, without correction.

#### WF10_036-G05

- Component: `WF10_036-T01`
- Importance: `supplementary`
- Function: `affirmative`
- Scoring role: `optional_content`
- Proposition: For perfluoroalkyl acids in GAC adsorbers treating ground and surface water, comparison of two EBCTs showed no consistent trend in carbon usage rate, such that neither shorter nor longer EBCTs consistently yielded lower carbon usage rates.
- Material qualifiers: ["PFAS considered were perfluoroalkyl acids (PFAAs)", "systems were GAC adsorbers treating ground and surface water", "comparison involved two specific EBCTs in the study", "performance metric was carbon usage rate (CUR) derived from breakthrough curves", "no consistent trend in CUR favoring either shorter or longer EBCT was observed under the tested conditions"]
- Evidence: WF10_036_MMG004
- Prior atomic claims: WF10_036-C04
- Full: Full credit for this optional group if the answer states that in GAC adsorbers treating PFAAs in ground and surface waters, comparison of two EBCTs showed no consistent trend where either shorter or longer EBCT yielded lower carbon usage rates.
- Partial: Partial credit if the answer notes that for PFAAs in GAC systems, carbon usage rate did not clearly favor either of the two compared EBCTs, but omits mention of the ground and surface water matrices or does not explicitly name carbon usage rate, while still capturing the lack of consistent EBCT advantage.
- Contradiction: Mark as contradicted for this group if the answer claims that the study showed a clear, consistent reduction in carbon usage rate at longer EBCT (or at shorter EBCT) across PFAAs, without correction.

#### WF10_036-G06

- Component: `WF10_036-T02`
- Importance: `core`
- Function: `limitation`
- Scoring role: `required_content`
- Proposition: The available evidence on EBCT effects for PFAS adsorption in granular and activated carbon systems is limited to specific PFAS mixtures or PFAAs, particular groundwater and surface water matrices, specific carbon configurations, and the EBCT values tested in each study, so these findings cannot be generalized to all PFAS, water qualities, granular/activated carbon materials, or EBCT conditions, and therefore longer EBCT cannot be claimed to universally guarantee better PFAS performance.
- Material qualifiers: ["available studies address only certain PFAS groupings (unspecified PFAS mixture, ΣPFAS, PFAAs)", "matrices examined are groundwater and ground/surface waters", "systems are specific granular or activated carbon column or RSSCT configurations", "EBCT effects are characterized only over the EBCT values actually tested in each study (including EBCTs of roughly a few minutes in RSSCTs and unspecified values in other tests per the evidence spans)", "because of these limitations in scope, the results cannot be generalized to all PFAS, water qualities, carbon materials, or EBCT conditions, and longer EBCT cannot be assumed to universally guarantee better performance"]
- Evidence: WF10_036_MMG001, WF10_036_MMG002, WF10_036_MMG003, WF10_036_MMG004
- Prior atomic claims: WF10_036-C06
- Full: Full credit if the answer explains that the EBCT–PFAS performance findings come from a limited set of studies involving particular PFAS types (e.g., ΣPFAS, PFAAs or unspecified PFAS mixtures), specific groundwater or ground/surface water matrices, specific granular/activated carbon systems and configurations, and only the EBCT values actually tested, and explicitly concludes that these limitations mean the results cannot be generalized to all PFAS, water qualities, carbon materials, or EBCT conditions and therefore longer EBCT cannot be assumed to universally guarantee better performance.
- Partial: Partial credit if the answer mentions that the EBCT–PFAS performance findings are study-specific or limited in terms of PFAS types, water quality, or system configuration, and therefore should not be over-generalized, but does not clearly enumerate more than one dimension of limitation (e.g., only mentions PFAS types but not matrices or systems), or does not explicitly connect these limitations to the idea that longer EBCT does not universally guarantee better performance, while not making universal claims.
- Contradiction: Mark as contradicted if the answer asserts that the reported studies establish a general or universal rule about EBCT and PFAS performance that applies across all PFAS, water qualities, carbon materials, and EBCT conditions, or otherwise denies that the findings are limited in scope, without immediate correction.


### Prior atomic-claim dispositions

#### WF10_036-C01

- Prior claim: In a groundwater granular activated carbon system, the apparent adsorption capacity for PFAS did not change as EBCT increased, indicating that longer EBCT did not enhance adsorption capacity under those conditions.
- Action: `mapped`
- Final target(s): WF10_036-G02
- Rationale: C01’s content about unchanged apparent adsorption capacity with increased EBCT is preserved in G02 as a study-specific finding and contributes to the broader synthesis in G01 via shared evidence, while being directly mapped to a single primary group here.

#### WF10_036-C02

- Prior claim: In groundwater activated carbon columns treating ΣPFAS, the ratio of ΣPFAS adsorption capacity (qΣPFAS) between a Lead + Lag configuration and a Lead-only column was 1.07 ± 0.12, which was interpreted as indicating that adsorption mechanisms were independent of EBCT.
- Action: `mapped`
- Final target(s): WF10_036-G03
- Rationale: C02’s finding on qΣPFAS ratios and EBCT-independent mechanisms is captured in G03 as a distinct, single-study result that also supports the cross-study synthesis in G01 through shared evidence, while mapping this atomic claim to one primary group.

#### WF10_036-C03

- Prior claim: In rapid small-scale column tests with activated carbon treating groundwater, longer EBCTs did not show additional loss of performance from competing adsorbates, and similar breakthrough curve shapes indicated that shorter EBCTs of approximately 2–5 minutes already captured the mass transfer zone, suggesting no clear performance gain from extending EBCT beyond that range.
- Action: `revised`
- Final target(s): WF10_036-G04
- Rationale: C03 was trimmed to remove the interpretive clause about 'no clear performance gain from extending EBCT beyond that range' and now matches the evidence span more closely in G04; this group is the sole direct mapping for this atomic claim.

#### WF10_036-C04

- Prior claim: For perfluoroalkyl acids in GAC adsorbers treating ground and surface water, comparison of two EBCTs showed that breakthrough curves did not display a consistent trend where either shorter or longer EBCTs resulted in lower carbon usage rates, indicating that increasing EBCT did not systematically improve carbon usage efficiency.
- Action: `mapped`
- Final target(s): WF10_036-G05
- Rationale: C04’s statement about no consistent CUR trend between two EBCTs for PFAAs is preserved in G05 as a single-study finding that also feeds the broader synthesis in G01 via shared evidence, while mapping this atomic claim to one primary group.

#### WF10_036-C05

- Prior claim: Across these GAC and activated carbon studies in groundwater and surface water, the reported PFAS performance metrics—apparent adsorption capacity, adsorption mechanisms, breakthrough curve shapes, and carbon usage rate—were largely insensitive to EBCT changes within the tested ranges, so the data do not support a general assertion that longer EBCT necessarily leads to better PFAS performance.
- Action: `revised`
- Final target(s): WF10_036-G01
- Rationale: C05’s synthesis that performance metrics were largely insensitive to EBCT and that the data do not support a general 'longer is better' assertion is encoded in the main synthesis group G01; constraint B01 draws on the same evidence but is not treated as a separate primary mapping target for this atomic claim.

#### WF10_036-C06

- Prior claim: The available evidence on EBCT effects for PFAS adsorption in GAC systems is limited to specific PFAS mixtures or PFAAs, particular groundwater and surface water matrices, specific GAC configurations, and EBCT ranges from a few minutes to on the order of tens of minutes, so these findings cannot be generalized to all PFAS, water qualities, GAC materials, or EBCT conditions.
- Action: `revised`
- Final target(s): WF10_036-G06
- Rationale: C06 was revised to remove the unsupported 'tens of minutes' EBCT range language and now frames limitations in terms of the EBCT values tested in each study. This limitation is captured in G06 as the single primary mapping target; constraint B01 is derived from the same reasoning but is not an additional mapping target.

### Constraint-only groups

- `WF10_036-B01`: The findings from these specific PFAS granular and activated carbon studies must not be generalized into a universal claim that longer EBCT always or necessarily improves PFAS treatment performance for all PFAS, water qualities, GAC types, and operating conditions.
  Violation rule: Flag a boundary violation if the answer generalizes the reported findings into a universal or near-universal statement that longer EBCT always, generally, or necessarily improves PFAS treatment performance across all PFAS, water qualities, GAC types, or operating conditions.

### Model B verification

Overall verdict: **approve**

- `WF10_036-G01`: **supported**. Cross-study synthesis proposition is entailed by the four spans, each independently showing EBCT-insensitivity of a distinct performance metric (capacity, mechanism ratio, breakthrough/mass-transfer-zone, CUR). Full/partial/contradiction rules are executable and require ≥2 metrics for full credit, correctly distinguishing synthesis from single-study fragments.
  Recommended change: None.
- `WF10_036-G02`: **supported**. Matches span exactly; matrix, adsorbent, and single-study scope qualifiers are all entailed. Correctly scoped as optional/supplementary since it duplicates content already required at the synthesis level (G01).
  Recommended change: None.
- `WF10_036-G03`: **supported**. Numeric qualifier (1.07 ± 0.12) and compound (ΣPFAS), matrix, and configuration are all directly entailed. numeric_required=true with populated accepted_numeric_equivalents resolves the previously flagged inconsistency in the group-level review.
  Recommended change: None.
- `WF10_036-G04`: **supported**. The previously flagged interpretive add-on ('no clear performance gain from extending EBCT beyond that range', from atomic claim C03) has been dropped; canonical_proposition now tracks the span verbatim in substance (competing-adsorbate independence + ~2-5 min MTZ capture).
  Recommended change: None.
- `WF10_036-G05`: **supported**. Proposition and qualifiers (PFAAs, ground/surface water, two-EBCT comparison, CUR endpoint, no consistent trend) are entailed by the span; the limitation flag on MMG004's numeric EBCT values (13/26 min) is correctly omitted from this group's claim content.
  Recommended change: None.
- `WF10_036-G06`: **supported**. The previously flagged unsupported 'tens of minutes' scope language (built on MMG004's unverifiable 13/26 min metadata) has been removed; material_qualifiers now frame EBCT scope only as 'the EBCT values actually tested in each study,' explicitly noting only the verifiable ~2-5 min RSSCT figure. This resolves the prior partially_supported verdict on C06.
  Recommended change: None.
- `WF10_036-B01`: **supported**. Correctly excluded from coverage scoring (constraint_only) and carries an executable violation_rule (flags universal/near-universal 'longer EBCT always improves performance' statements) consistent with the must_not_claim task boundary.
  Recommended change: None.

Human-review priorities:
- MMG003 and MMG004 are each cited in an optional single-study group (G04/G05) and also in the core synthesis (G01), core limitation (G06), and boundary constraint (B01) groups. Propositions are logically distinct (single-study fact vs. cross-study synthesis vs. non-generalization boundary), so this is defensible non-duplicative reuse, but project authors should confirm this is the intended scoring design rather than an artifact that lets one candidate sentence satisfy multiple 'independent' groups.
- No independently sourced frozen task_component document was supplied to verify T01/T02 wording was 'copied exactly' from an upstream source outside this packet; the packet's own frozen_task_components list matches the ledger verbatim, but exact-copy provenance against any external boundary document remains unconfirmed and should be checked by a human reviewer with access to that source.

### Non-normative reference prose

Across the available granular and activated carbon studies, longer empty-bed contact time (EBCT) did not necessarily translate into better PFAS performance.

In groundwater granular activated carbon columns, one study reported that the apparent adsorption capacity did not change as EBCT increased, indicating that extending EBCT did not enhance PFAS adsorption capacity under those conditions. Another groundwater study using activated carbon columns treating ΣPFAS found that the ratio of ΣPFAS adsorption capacity (qΣPFAS) between a lead–lag configuration and a single lead column was close to unity (1.07 ± 0.12), which the authors interpreted as adsorption mechanisms being independent of EBCT. In rapid small-scale column tests with activated carbon treating groundwater, longer EBCTs did not show additional loss of performance from competing adsorbates, and similar breakthrough curve shapes indicated that shorter EBCTs of approximately 2–5 minutes already captured the mass transfer zone. In granular activated carbon adsorbers treating ground and surface waters for perfluoroalkyl acids (PFAAs), comparison of two EBCTs showed that breakthrough curves did not display a consistent trend where either shorter or longer EBCTs resulted in lower carbon usage rates.

Taken together, these studies show that, under the tested EBCT ranges, water matrices, granular/activated carbon systems, and PFAS mixtures, key performance metrics such as apparent adsorption capacity, inferred adsorption mechanisms, breakthrough behavior, and carbon usage efficiency were largely insensitive to EBCT changes. As a result, the available data do not support a general assertion that longer EBCT necessarily leads to better PFAS performance in these systems.

However, the evidence base is limited to specific PFAS mixtures or PFAAs, particular groundwater and ground/surface water matrices, specific granular and activated carbon configurations, and the EBCT values actually tested in each study. These findings therefore cannot be generalized to all PFAS classes, water qualities, carbon materials, or EBCT conditions, and they do not establish a universal rule that would make longer EBCT a guaranteed route to better PFAS treatment performance.

### Prose-to-ledger map

- Across the available granular and activated carbon studies, longer empty-bed contact time (EBCT) did not necessarily translate into better PFAS performance. -> WF10_036-G01
- In groundwater granular activated carbon columns, one study reported that the apparent adsorption capacity did not change as EBCT increased, indicating that extending EBCT did not enhance PFAS adsorption capacity under those conditions. -> WF10_036-G02
- Another groundwater study using activated carbon columns treating ΣPFAS found that the ratio of ΣPFAS adsorption capacity (qΣPFAS) between a lead–lag configuration and a single lead column was close to unity (1.07 ± 0.12), which the authors interpreted as adsorption mechanisms being independent of EBCT. -> WF10_036-G03
- In rapid small-scale column tests with activated carbon treating groundwater, longer EBCTs did not show additional loss of performance from competing adsorbates, and similar breakthrough curve shapes indicated that shorter EBCTs of approximately 2–5 minutes already captured the mass transfer zone. -> WF10_036-G04
- In granular activated carbon adsorbers treating ground and surface waters for perfluoroalkyl acids (PFAAs), comparison of two EBCTs showed that breakthrough curves did not display a consistent trend where either shorter or longer EBCTs resulted in lower carbon usage rates. -> WF10_036-G05
- Taken together, these studies show that, under the tested EBCT ranges, water matrices, granular/activated carbon systems, and PFAS mixtures, key performance metrics such as apparent adsorption capacity, inferred adsorption mechanisms, breakthrough behavior, and carbon usage efficiency were largely insensitive to EBCT changes. -> WF10_036-G01
- As a result, the available data do not support a general assertion that longer EBCT necessarily leads to better PFAS performance in these systems. -> WF10_036-G01
- However, the evidence base is limited to specific PFAS mixtures or PFAAs, particular groundwater and ground/surface water matrices, specific granular and activated carbon configurations, and the EBCT values actually tested in each study. -> WF10_036-G06
- These findings therefore cannot be generalized to all PFAS classes, water qualities, carbon materials, or EBCT conditions, and they do not establish a universal rule that would make longer EBCT a guaranteed route to better PFAS treatment performance. -> WF10_036-G06, WF10_036-B01

---


## Project-author approval record

- Review date: 2026-07-29
- Decision: approve all 13 repair7 claim ledgers
- Candidate answers seen for this approval: no
- L3 scores seen for this approval: no
- Record: `project_author_approval_record.json`

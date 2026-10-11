# L3 Dev13 V2 project-author audit

Status: **all project-author decisions pending**

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
> Conclusion An eﬃcient and convenient SPME method was developed for PFAS in aqueous matrices and applied to river, lake, tap and bottled water samples.

**NQ10_MMG002** (required_gold; `2021 - Olomukoro - Ion exchange solid phase microextraction coupled to liquid chromatography - laminar flow tandem mass spectrometry for the determination of.pdf`, chunk `34`)
> 3 ng L − 1 ∗∗ 40 – 160 ng L − 1 ∗∗∗∗ [39] Drinking water (EPA method 8327) Dilute and Shoot N/A 24 PFAS compounds

**NQ10_MMG003** (required_gold; `2021 - Olomukoro - Ion exchange solid phase microextraction coupled to liquid chromatography - laminar flow tandem mass spectrometry for the determination of.pdf`, chunk `6`)
> So far, to detect parts-per-trillion level PFAS, pre-concentration has been accomplished by either solid phase extraction (SPE) or liquid-liquid extraction (LLE) [ 9 , 34 , 40 ].

**NQ10_MMG004** (optional_gold; `2022 - Pellicer-Castell - Iron-Doped Bimodal Mesoporous Silica Nanomaterials as Sorbents for Solid-Phase Extraction of Perfluoroalkyl Substances in Environmental.pdf`, chunk `42`)
> Obtained results showed that, with 150 mg cartridges, recoveries clearly decreased when the sample volume was increased from 10 to 100 mL.

**NQ10_MMG005** (optional_gold; `2022 - Pellicer-Castell - Iron-Doped Bimodal Mesoporous Silica Nanomaterials as Sorbents for Solid-Phase Extraction of Perfluoroalkyl Substances in Environmental.pdf`, chunk `43`)
> (C8–C14), with values above 61% for all of them and close to 100% in the case of PFOS or PFNA.

**NQ10_MMG006** (optional_gold; `2022 - Croll - Adaptation of selected models for describing competitive per- and polyfluoroalkyl substances breakthrough curves in groundwater treated by granular.pdf`, chunk `12`)
> Eluted methanolic sample extracts of 0.5 mL resulted in an effective 500-fold concentration of target analytes from the initial sampling.

**NQ10_MMG007** (optional_gold; `2024 - Habib - Green Analytical Method for Perfluorocarboxylic Acids (PFCAs) in Water of Stir Bar Sorptive Extraction Coupled with Thermal Desorption-Gas.pdf`, chunk `11`)
> This study aimed to develop and validate a simple, sensitive, and efficient method by integrating green chemistry-based stir bar sorptive extraction (SBSE) with thermal desorption–gas chromatography–mass spectrometry (TD-GC-MS) specifically for the anal- ysis of perfluorocarboxylic acids (PFCAs), a significant subgroup of PFAS.

**NQ10_MMG008** (optional_gold; `2023 - Hao - Hydrothermal Alkaline Treatment (HALT) of Foam Fractionation Concentrate Derived from PFAS-Contaminated Groundwater.pdf`, chunk `9`)
> 23 Briefly, the diluted samples were mixed with aqueous ammonium hydroxide solution, isopropyl alcohol, trifluoroethanol, water, internal standards, and methanol before being injected into a SCIEX ExionLC high- pressure liquid chromatography (HPLC) system.

**NQ10_MMG009** (optional_gold; `2021 - Olomukoro - Ion exchange solid phase microextraction coupled to liquid chromatography - laminar flow tandem mass spectrometry for the determination of.pdf`, chunk `32`)
> to methods that require very fast sample processing such as dilute and shoot, our method provides higher preconcentration and limits occurrence of matrix effects.

**NQ10_MMG010** (negative_gold; `2021 - Olomukoro - Ion exchange solid phase microextraction coupled to liquid chromatography - laminar flow tandem mass spectrometry for the determination of.pdf`, chunk `7`)
> Furthermore, substantial matrix effects can occur from the samples during analysis, mak- ing the method not suitable and robust for such complex samples.

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
- Proposition: A solid phase microextraction (SPME) method was developed for PFAS in aqueous matrices and applied to river, lake, tap, and bottled water samples as the sample-preparation step before analysis.
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
- Proposition: Some PFAS analytical workflows do not include a dedicated preconcentration step, instead using dilute-and-shoot for drinking water and dilution with solvent/base addition for foam-fractionation concentrates before chromatographic–mass spectrometric analysis.
- Material qualifiers: ["EPA Method 8327 for drinking water uses dilute-and-shoot with no separate preconcentration for 24 PFAS compounds", "foam fractionation concentrate samples are diluted and mixed with aqueous ammonium hydroxide, isopropyl alcohol, trifluoroethanol, water, internal standards, and methanol before HPLC injection"]
- Evidence: NQ10_MMG002, NQ10_MMG008
- Prior atomic claims: NQ10-C08, NQ10-C09, NQ10-C14
- Full: Award full if the answer clearly states that some PFAS methods omit a distinct preconcentration step and instead (a) use dilute-and-shoot for drinking water (EPA Method 8327) and (b) prepare foam-fractionation concentrate by dilution and mixing with aqueous ammonium hydroxide, isopropyl alcohol, trifluoroethanol, water, internal standards, and methanol before chromatographic analysis.
- Partial: Award partial if the answer correctly describes at least one of these dilution-based workflows (either EPA Method 8327 or the foam-concentrate preparation) without introducing a contradictory claim that these same methods use an explicit SPE/LLE preconcentration step, but omits the other example.
- Contradiction: Mark contradicted if the answer asserts that EPA Method 8327 uses an SPE or LLE preconcentration step, or that the described foam-concentrate workflow does not involve dilution and mixing with the listed reagents before chromatographic analysis.

#### NQ10-G05

- Component: `NQ10-T01`
- Importance: `supplementary`
- Function: `affirmative`
- Scoring role: `optional_content`
- Proposition: In one groundwater application, PFAS were preconcentrated so that eluted methanolic sample extracts of 0.5 mL resulted in an effective 500-fold concentration of the target analytes from the initial sampling volume.
- Material qualifiers: ["matrix is groundwater", "elution volume is 0.5 mL methanolic extract", "effective concentration factor is about 500-fold"]
- Evidence: NQ10_MMG006
- Prior atomic claims: NQ10-C02
- Full: Award full if the answer mentions a groundwater PFAS example in which a 0.5 mL methanolic extract corresponds to roughly a 500-fold concentration of analytes relative to the original sample volume, using numerically equivalent expressions (e.g., 0.5 mL, ~500-fold).
- Partial: Award partial if the answer captures that a groundwater workflow achieved a large (multi-hundred-fold) concentration in a small methanolic volume but omits either the 0.5 mL detail or the approximate 500-fold figure, without mis-stating them.
- Contradiction: Mark contradicted if the answer states that the described groundwater methanolic extract did not result in substantial (e.g., multi-hundred-fold) preconcentration, or provides clearly incompatible numbers for this specific example.

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

- Prior claim: A solid phase microextraction (SPME) method was developed for PFAS in aqueous matrices and applied to river, lake, tap, and bottled water samples.
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

- Prior claim: In analysis of PFAS in foam fractionation concentrate, diluted samples were mixed with aqueous ammonium hydroxide solution, isopropyl alcohol, trifluoroethanol, water, internal standards, and methanol before HPLC injection, without employing solid-phase or liquid–liquid extraction for preconcentration.
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

- `NQ10-G01`: **supported**. Canonical proposition and qualifiers (ppt-level PFAS, SPE or LLE, general preconcentration) are directly entailed verbatim by the NQ10_MMG003 span.
  Recommended change: None.
- `NQ10-G02`: **supported**. Canonical proposition matches the span almost verbatim (SPME method for PFAS in aqueous matrices; river, lake, tap, bottled water). No unsupported numeric values (e.g., LOQ) were introduced, correctly respecting the gold record's does_not_support note.
  Recommended change: None.
- `NQ10-G03`: **supported**. Directly entailed by the NQ10_MMG007 span; PFCAs-as-subgroup and water matrix qualifiers are supported.
  Recommended change: None.
- `NQ10-G04`: **supported**. The EPA 8327 dilute-and-shoot/no-preconcentration portion is directly entailed by the NQ10_MMG002 span. The foam-concentrate material_qualifiers were correctly revised to drop the explicit 'no SPE or LLE' phrasing flagged in the prior Model B review, but the canonical_proposition's framing that this workflow lacks 'a dedicated preconcentration step' still rests on an inference from the absence of an extraction step in the NQ10_MMG008 span (dilution + reagent mixing + HPLC injection) rather than an explicit negation. This inference is consistent with the gold record's own (unflagged) supported_claim field, unlike the MMG006 case where the curator explicitly flagged the out-of-span attribution, so the difference in treatment across G04/G05 is justifiable rather than an inconsistency.
  Recommended change: Optional: add a brief hedge to the canonical_proposition or material_qualifiers noting that the foam-concentrate example's lack of a distinct extraction step is inferred from the absence of a described SPE/LLE step in the retrieved span, for consistency with how G05 was hedged.
- `NQ10-G05`: **supported**. The unsupported 'weak anion exchange SPE' attribution flagged by both prior Model B reviews has been removed; the canonical_proposition and qualifiers now track only the span-supported 0.5 mL / 500-fold facts, resolving atomic claim C02's partial-support issue.
  Recommended change: None.
- `NQ10-G06`: **supported**. Directly entailed by the NQ10_MMG004 span; 150 mg cartridge, 10 to 100 mL, and recovery decrease are all present.
  Recommended change: None.
- `NQ10-G07`: **supported**. The unsupported enrichment-factor figures (121-212) flagged for atomic claim C04 have been removed; only the >61% and close-to-100% recovery figures present in the exact span remain.
  Recommended change: None.
- `NQ10-G08`: **supported**. Directly entailed by the NQ10_MMG009 span comparing SPME to dilute-and-shoot on preconcentration and matrix effects.
  Recommended change: None.
- `NQ10-G09`: **supported**. Correctly scoped as a limitation tied to 'complex samples' without naming or universalizing the affected method, matching the gold record's own scope and does_not_support caveat.
  Recommended change: None.
- `NQ10-B01`: **supported**. Correctly excluded from coverage scoring (constraint_only) and carries an executable violation_rule matching the frozen must_not_claim boundary; no evidence_ids needed since it is a negative boundary constraint rather than a positive factual claim.
  Recommended change: None.

Human-review priorities:
- G04's canonical_proposition frames the foam-fractionation-concentrate example as lacking 'a dedicated preconcentration step,' which is an inference from the absence of a described extraction step in the NQ10_MMG008 span rather than an explicit statement; this is defensible (the gold record's own supported_claim makes the same inference without a does_not_support flag) but an optional hedge would make it maximally consistent with how the analogous NQ10_MMG006 attribution was hedged in G05.
- G04 merges three atomic claims (C08 EPA 8327 drinking water, C09 foam concentrate, C14 synthesis) covering two independently verifiable facts from different papers/matrices into one scoring group; this is a defensible design choice given partial_rule allows credit for either sub-fact alone, but a project author may prefer splitting it into two independently scorable groups for finer-grained credit.
- Confirm the prior Model B concern about optional group G10 restating core/optional content from G02-G05 is fully resolved by its removal from this revision, with no remaining vestige of double-crediting risk for T02.

### Non-normative reference prose

In the supplied studies, PFAS sample preparation and preconcentration prior to chromatographic–mass spectrometric analysis are performed using several different approaches, depending on the analytical context. For parts-per-trillion level PFAS determinations in general, preconcentration has been accomplished using either solid phase extraction (SPE) or liquid–liquid extraction (LLE) before analysis. Sorptive microextraction formats are also used: a solid phase microextraction (SPME) method was developed for PFAS in aqueous matrices and applied to river, lake, tap, and bottled water samples, and for perfluorocarboxylic acids (PFCAs) in water a method integrating stir bar sorptive extraction (SBSE) with thermal desorption–gas chromatography–mass spectrometry (TD–GC–MS) was developed and validated, with SBSE serving as the extraction/preconcentration step.

Other workflows reflect strong enrichment or adjustments to SPE conditions. In one groundwater application, eluted methanolic sample extracts of 0.5 mL resulted in an effective 500-fold concentration of the target analytes from the initial sampling volume. In another SPE study using 150 mg cartridges for water samples, recoveries clearly decreased when the sample volume was increased from 10 to 100 mL, indicating that sample volume relative to sorbent mass directly affects extraction efficiency. In a separate SPE protocol, C8–C14 PFAS showed extraction recoveries above 61% for all analytes and close to 100% for PFOS and PFNA, illustrating analyte-dependent performance within a single method. Across such SPE examples, reported outcomes range from high recoveries in some C8–C14 compounds to multi-hundred-fold enrichment in a groundwater application, underscoring that achievable enrichment and recovery depend on the specific SPE protocol and matrix.

Some PFAS workflows do not employ a dedicated preconcentration step. EPA Method 8327 for drinking water uses a dilute-and-shoot approach, with no separate preconcentration step, for 24 PFAS compounds. Another study analyzing PFAS in foam-fractionation concentrate derived from contaminated groundwater prepared samples by dilution and mixing with aqueous ammonium hydroxide solution, isopropyl alcohol, trifluoroethanol, water, internal standards, and methanol before HPLC injection.

Method choice and performance vary with matrix, analyte scope, and workflow. Groundwater applications rely on an extraction and elution scheme that yields strong preconcentration prior to analysis, while SPME is applied to river, lake, tap, and bottled waters, and SBSE is used for PFCAs in water in a TD–GC–MS workflow. In contrast, drinking water under EPA Method 8327 and foam-fractionation concentrates can be handled by dilute-and-shoot or dilution with solvent/base addition alone. The SPME method provided higher preconcentration and reduced the occurrence of matrix effects compared with very fast sample-processing methods such as dilute-and-shoot. At the same time, substantial matrix effects were reported in some methods when applied to complex samples, making those methods not suitable and not robust for such matrices. Together, these examples show that PFAS preconcentration and sample-preparation strategies are tailored to the matrix and analyte group, and that recovery, enrichment, and susceptibility to matrix effects depend on the specific protocol rather than a single universally applicable SPE configuration.

### Prose-to-ledger map

- For parts-per-trillion level PFAS determinations in general, preconcentration has been accomplished using either solid phase extraction (SPE) or liquid–liquid extraction (LLE) before analysis. -> NQ10-G01
- Sorptive microextraction formats are also used: a solid phase microextraction (SPME) method was developed for PFAS in aqueous matrices and applied to river, lake, tap, and bottled water samples, -> NQ10-G02
- and for perfluorocarboxylic acids (PFCAs) in water a method integrating stir bar sorptive extraction (SBSE) with thermal desorption–gas chromatography–mass spectrometry (TD–GC–MS) was developed and validated, with SBSE serving as the extraction/preconcentration step. -> NQ10-G03
- In one groundwater application, eluted methanolic sample extracts of 0.5 mL resulted in an effective 500-fold concentration of the target analytes from the initial sampling volume. -> NQ10-G05
- In another SPE study using 150 mg cartridges for water samples, recoveries clearly decreased when the sample volume was increased from 10 to 100 mL, indicating that sample volume relative to sorbent mass directly affects extraction efficiency. -> NQ10-G06
- In a separate SPE protocol, C8–C14 PFAS showed extraction recoveries above 61% for all analytes and close to 100% for PFOS and PFNA, illustrating analyte-dependent performance within a single method. -> NQ10-G07
- Across such SPE examples, reported outcomes range from high recoveries in some C8–C14 compounds to multi-hundred-fold enrichment in a groundwater application, underscoring that achievable enrichment and recovery depend on the specific SPE protocol and matrix. -> NQ10-G05, NQ10-G07
- Some PFAS workflows do not employ a dedicated preconcentration step. -> NQ10-G04
- EPA Method 8327 for drinking water uses a dilute-and-shoot approach, with no separate preconcentration step, for 24 PFAS compounds. -> NQ10-G04
- Another study analyzing PFAS in foam-fractionation concentrate derived from contaminated groundwater prepared samples by dilution and mixing with aqueous ammonium hydroxide solution, isopropyl alcohol, trifluoroethanol, water, internal standards, and methanol before HPLC injection. -> NQ10-G04
- Method choice and performance vary with matrix, analyte scope, and workflow. -> NQ10-G01, NQ10-G02, NQ10-G03, NQ10-G04, NQ10-G05, NQ10-G06, NQ10-G07, NQ10-G08, NQ10-G09
- Groundwater applications rely on an extraction and elution scheme that yields strong preconcentration prior to analysis, while SPME is applied to river, lake, tap, and bottled waters, and SBSE is used for PFCAs in water in a TD–GC–MS workflow. -> NQ10-G02, NQ10-G03, NQ10-G05
- In contrast, drinking water under EPA Method 8327 and foam-fractionation concentrates can be handled by dilute-and-shoot or dilution with solvent/base addition alone. -> NQ10-G04
- The SPME method provided higher preconcentration and reduced the occurrence of matrix effects compared with very fast sample-processing methods such as dilute-and-shoot. -> NQ10-G08
- At the same time, substantial matrix effects were reported in some methods when applied to complex samples, making those methods not suitable and not robust for such matrices. -> NQ10-G09
- Together, these examples show that PFAS preconcentration and sample-preparation strategies are tailored to the matrix and analyte group, and that recovery, enrichment, and susceptibility to matrix effects depend on the specific protocol rather than a single universally applicable SPE configuration. -> NQ10-G01, NQ10-G02, NQ10-G03, NQ10-G04, NQ10-G05, NQ10-G06, NQ10-G07, NQ10-G08, NQ10-G09, NQ10-B01

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
> Compound Linearity a (µg L−1) Sensitivity (ng L−1) Extraction Efﬁciency (%) EF Repeatability RSD (%) LOD LOQ Intra-Day Inter-Day PFOA 2–50 4 12 66 ± 20 132 22 38 PFNA 4–50 7 22 110 ± 30 212 16 28 PFOS 2–50 3 9 110 ± 30 212 19 29 PFDA 5–50 8 24 77 ± 16 154 15 21 PFUnDA 4–50 7 21 73 ± 15 145 17 21 PFDS 2–50 3 11 67 ± 14 134 21 21 PFDoDA 4–50 6 18 75 ± 13 151 13 17 PFTrDA 5–50 8 25 68 ± 17 136 14 25 PFTeDA 2–50 3 11 61 ± 14 121 18 23 a Referred to the ﬁnal injection solution.

**NQ12_MMG002** (required_gold; `2024 - Habib - Green Analytical Method for Perfluorocarboxylic Acids (PFCAs) in Water of Stir Bar Sorptive Extraction Coupled with Thermal Desorption-Gas.pdf`, chunk `47`)
> Analyte Retention Time (min) Parent Ion (m/z) Coefficient of Determination (R2) % Recovery (±SD) LOD (ng/L) LOQ (ng/L) MDL (ng/L) PFHpA 5.884 405 0.9984 97 ( ±11) 21.17 138.27 293.96 PFOA 6.640 455 0.9948 94 ( ±11) 21.20 103.13 495.37 PFNA 7.614 505 0.9956 86 ( ±5) 30.12 90.80 980.37 PFDA 8.448 555 0.9893 91 ( ±10) 54.29 169.85 888.30 PFUnA 9.416 605 0.9892 88 ( ±10) 34.39 132.90 1227.97 PFDoA 10.002 655 0.9925 85 ( ±8) 73.96 192.01 1458.84 PFTeDA 11.422 755 0.9906 85 ( ±3) 35.02 107.10 925.13

**NQ12_MMG003** (required_gold; `2025 - Tomei - Optimization and Testing of an SPE-LC - q-TOF Analytical Method for the Detection of PFAS Degradation Products in Water Treatment Processes.pdf`, chunk `14`)
> As expected, in-source fragmentation of the carboxylic acids was instead influenced by the voltage of the fragmentor: with 60 V, the signal of short-chain PFAS (C < 5) was almost lost, so 60 V was discarded;

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
- Proposition: In a water SBSE–TD–GC–MS method applied to PFCAs PFHpA, PFOA, PFNA, PFDA, PFUnA, PFDoA, and PFTeDA, analytical sensitivity is compound-specific, with LODs spanning about 21–74 ng/L and LOQs about 91–192 ng/L instead of a single detection limit across the PFCA series.
- Material qualifiers: ["matrix is water", "method is SBSE–TD–GC–MS", "compounds are PFCAs PFHpA, PFOA, PFNA, PFDA, PFUnA, PFDoA, PFTeDA", "LOD values fall within approximately 21–74 ng/L", "LOQ values fall within approximately 91–192 ng/L"]
- Evidence: NQ12_MMG002
- Prior atomic claims: NQ12-C04
- Full: Award full credit if the answer states that in a water SBSE–TD–GC–MS method the listed PFCAs have different, compound-specific LOD and LOQ values, and correctly conveys that LODs are on the order of 21–74 ng/L and LOQs on the order of 91–192 ng/L, with the water matrix and SBSE–TD–GC–MS method clearly identified.
- Partial: Award partial credit if the answer correctly notes compound-specific LOD/LOQ for these PFCAs in a water SBSE–TD–GC–MS method, but omits, substantially simplifies, or only loosely approximates the numeric ranges (e.g., says 'tens of ng/L LODs and around a hundred ng/L LOQs') while staying directionally accurate and not presenting incompatible numbers.
- Contradiction: Mark as contradicted if the answer claims that in the cited SBSE–TD–GC–MS water method all these PFCAs share a single common LOD/LOQ, or assigns dramatically different ranges (e.g., single-digit ng/L LODs or values in the µg/L range) to this method, or misattributes the method or matrix such that the core finding is reversed.

#### NQ12-G03

- Component: `NQ12-T02`
- Importance: `supplementary`
- Function: `affirmative`
- Scoring role: `optional_content`
- Proposition: Comparing the reported water methods shows that analytical method choice strongly affects absolute sensitivity: the SPE–UHPLC–MS/MS procedure achieved lower LODs (3–8 ng/L) and LOQs (9–25 ng/L) for C8–C14 PFAS than the SBSE–TD–GC–MS method, which reported higher LODs (21.17–73.96 ng/L) and LOQs (90.80–192.01 ng/L) for C7–C14 PFCAs.
- Material qualifiers: ["comparison is between a water SPE–UHPLC–MS/MS method and a water SBSE–TD–GC–MS method", "SPE–UHPLC–MS/MS LODs are in the 3–8 ng/L range and LOQs in the 9–25 ng/L range", "SBSE–TD–GC–MS LODs are in the 21.17–73.96 ng/L range and LOQs in the 90.80–192.01 ng/L range", "finding is limited to the reported PFAS/PFCA subsets and methods and does not imply a universal cross-method rule"]
- Evidence: NQ12_MMG001, NQ12_MMG002
- Prior atomic claims: NQ12-C06
- Full: Award full credit if the answer explicitly compares the two reported water methods, states that SPE–UHPLC–MS/MS yields substantially lower LOD/LOQ values than SBSE–TD–GC–MS for the covered PFAS, and gives numerically consistent ranges for both methods (within the cited ranges), while explicitly or implicitly tying this difference to the analytical method choice.
- Partial: Award partial credit if the answer correctly states that the water SPE–UHPLC–MS/MS method is more sensitive (lower LOD/LOQ) than the SBSE–TD–GC–MS method for the reported PFAS sets, but either omits numeric ranges for one of the methods or only qualitatively contrasts them (e.g., 'much lower' vs 'tens of ng/L') without incorrect numbers and without implying universality beyond these methods.
- Contradiction: Mark as contradicted if the answer asserts the opposite pattern (e.g., that SBSE–TD–GC–MS has lower LOD/LOQ than SPE–UHPLC–MS/MS for these water analyses), or presents clearly incompatible numeric ranges (e.g., single-digit ng/L LODs assigned to SBSE–TD–GC–MS while much higher values to SPE–UHPLC–MS/MS), or generalizes the observed difference as a universal rule for all methods rather than these specific protocols.

#### NQ12-G04

- Component: `NQ12-T02`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: In an SPE–LC–q‑TOF water method targeting PFAS-related carboxylic acids, setting the fragmentor voltage to 60 V caused the signal of short-chain PFAS (C < 5) to be almost lost, so this setting was discarded, demonstrating that fragmentor voltage can strongly and selectively reduce sensitivity for short-chain PFAS without provided numerical LOD or LOQ values.
- Material qualifiers: ["matrix is water", "method is SPE–LC–q‑TOF", "effect is observed for short-chain PFAS (C < 5) carboxylic acids", "instrument parameter is fragmentor voltage set to 60 V", "the observation is qualitative signal loss; no numerical LOD/LOQ values are reported"]
- Evidence: NQ12_MMG003
- Prior atomic claims: NQ12-C07, NQ12-S02, NQ12-L01
- Full: Award full credit if the answer explains that in an SPE–LC–q‑TOF water method a fragmentor voltage of 60 V nearly eliminated the signal for short-chain (C < 5) PFAS, leading to discarding that setting, and makes clear that this is a qualitative sensitivity effect tied to fragmentor voltage, with no numerical LOD/LOQ values reported.
- Partial: Award partial credit if the answer correctly links fragmentor voltage in an LC–q‑TOF PFAS method to strong loss of short-chain PFAS signal but omits the specific value of 60 V, or mentions 60 V but does not explicitly state that the signal was almost lost or that the setting was discarded, provided it does not invent quantitative LOD/LOQ figures.
- Contradiction: Mark as contradicted if the answer claims that increasing fragmentor voltage to 60 V improved short-chain PFAS signal in the cited SPE–LC–q‑TOF method, or that fragmentor voltage had no substantial effect on short-chain PFAS sensitivity, or if it fabricates specific LOD/LOQ numbers for this voltage despite the evidence indicating only qualitative signal loss.

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
- Proposition: In the SBSE–TD–GC–MS water method, individual LOD/LOQ pairs were: PFHpA 21.17/138.27 ng/L, PFOA 21.20/103.13 ng/L, PFNA 30.12/90.80 ng/L, PFDA 54.29/169.85 ng/L, PFUnA 34.39/132.90 ng/L, PFDoA 73.96/192.01 ng/L, and PFTeDA 35.02/107.10 ng/L.
- Material qualifiers: ["matrix is water", "method is SBSE–TD–GC–MS", "LOD/LOQ values are given in ng/L", "each listed PFCA is associated with the correct LOD/LOQ pair"]
- Evidence: NQ12_MMG002
- Prior atomic claims: NQ12-C05
- Full: Award full credit for this optional group if the answer lists the compound-specific LOD/LOQ pairs for these seven PFCAs in the SBSE–TD–GC–MS water method without material numeric error.
- Partial: Award partial credit for this optional group if some but not all of the PFCA LOD/LOQ pairs are accurately reported, with no incorrect values for those that are mentioned.
- Contradiction: Mark as contradicted for this optional group if the answer assigns clearly incorrect LOD/LOQ values to one or more of these PFCAs under the SBSE–TD–GC–MS water method.

#### NQ12-G07

- Component: `NQ12-T01`
- Importance: `supplementary`
- Function: `affirmative`
- Scoring role: `optional_content`
- Proposition: In the SBSE–TD–GC–MS PFCA study, retention time and parent ion m/z increased with chain length from PFHpA to PFTeDA, whereas the LOD and LOQ values varied among analytes without following a simple monotonic trend with chain length.
- Material qualifiers: ["applies to PFHpA through PFTeDA in water", "method is SBSE–TD–GC–MS", "retention time and parent ion m/z increase with chain length", "LOD/LOQ values do not simply increase or decrease monotonically with chain length"]
- Evidence: NQ12_MMG002
- Prior atomic claims: NQ12-S01
- Full: Award full credit for this optional group if the answer notes that in the SBSE–TD–GC–MS PFCA series, retention time and m/z increase with chain length but LOD/LOQ values vary in a more complex, non-monotonic way.
- Partial: Award partial credit for this optional group if the answer correctly describes either the retention time/mass trend or the lack of a simple LOD/LOQ–chain-length trend but not both, without making an incompatible statement about the other.
- Contradiction: Mark as contradicted for this optional group if the answer claims that LOD and LOQ strictly increase or strictly decrease with chain length in this SBSE–TD–GC–MS PFCA study, or that retention time/mass do not change with chain length.

#### NQ12-G08

- Component: `NQ12-T01`
- Importance: `supplementary`
- Function: `limitation`
- Scoring role: `optional_content`
- Proposition: Across the reported water studies, LOD/LOQ values are specific to the individual PFAS and method, and the data do not support a single universal or monotonic relationship between PFAS chain length and detection limits across all analytical platforms.
- Material qualifiers: ["summary is limited to the reported water methods and PFAS subsets", "states explicitly that no single universal LOD/LOQ–chain-length pattern is established by these data"]
- Evidence: NQ12_MMG001, NQ12_MMG002
- Prior atomic claims: 
- Full: Award full credit for this optional group if the answer explicitly notes that the reported LOD/LOQ data are compound- and method-specific and do not establish one universal or simple monotonic dependence of detection limits on PFAS chain length across methods.
- Partial: Award partial credit for this optional group if the answer either (a) stresses compound- and method-specific LOD/LOQ behavior without explicitly mentioning the lack of a universal pattern, or (b) states that no universal monotonic pattern is evident from the data but does not clearly emphasize method dependence.
- Contradiction: Mark as contradicted for this optional group if the answer claims that the provided data establish a single universal or strictly monotonic relationship between PFAS chain length and LOD/LOQ that applies across methods.

#### NQ12-G09

- Component: `NQ12-T01`
- Importance: `supplementary`
- Function: `limitation`
- Scoring role: `optional_content`
- Proposition: All reported quantitative LOD/LOQ values come from water matrices and from specific PFAS subsets (C8–C14 PFAS in the SPE–UHPLC–MS/MS study and C7–C14 PFCAs in the SBSE–TD–GC–MS study), so these results do not establish chain-length–sensitivity relationships for other PFAS classes or matrices.
- Material qualifiers: ["matrix limitation to water", "compound-class limitation to the specific C7–C14/C8–C14 PFAS/PFCA sets", "explicit statement that other PFAS types and matrices are not covered"]
- Evidence: NQ12_MMG001, NQ12_MMG002
- Prior atomic claims: NQ12-L02
- Full: Award full credit for this optional group if the answer notes that the numerical LOD/LOQ data pertain only to water and to specific C7–C14/C8–C14 PFAS subsets and explicitly cautions against generalizing chain-length sensitivity behavior to other PFAS classes or matrices.
- Partial: Award partial credit for this optional group if the answer mentions either the matrix limitation (water only) or the compound-set limitation but not both, while still communicating that broader generalization is not supported.
- Contradiction: Mark as contradicted for this optional group if the answer explicitly claims that the reported water-based LOD/LOQ findings establish chain-length sensitivity patterns for PFAS in general across all matrices or all PFAS classes.


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

- `NQ12-G01`: **supported**. LOD 3-8 ng/L and LOQ 9-25 ng/L are correctly computed from the table (LOD column: 4,7,3,8,7,3,6,8,3; LOQ column: 12,22,9,24,21,11,18,25,11). The previously flagged 'referred to the final injection solution' misattribution (footnote 'a' is attached only to the Linearity column, not Sensitivity/LOD/LOQ) has been removed from the material_qualifiers and full_rule, resolving the prior Model B partial-support finding on source claim C01.
  Recommended change: None.
- `NQ12-G02`: **supported**. LOD ~21-74 ng/L and LOQ ~91-192 ng/L correctly reflect the table (LOD column 21.17-73.96; LOQ column 90.80-192.01), correctly attributed to SBSE-TD-GC-MS in water for the seven listed PFCAs.
  Recommended change: None.
- `NQ12-G03`: **supported**. Cross-method comparison correctly cites the same two ranges as G01/G02 and is properly scoped as method-specific, not universal. synthesis_required=true and optional_content scoring role are appropriate since this is a derived comparison rather than a directly stated fact. The full_rule numeric-tolerance language ('within the cited ranges') is now consistent with the reference_answer's 'several-fold' phrasing, resolving the previously flagged terminology mismatch.
  Recommended change: None.
- `NQ12-G04`: **supported**. Correctly reports that 60 V fragmentor voltage nearly eliminated short-chain (C<5) PFAS signal in SPE-LC-q-TOF, leading to discarding the setting, and correctly notes no numeric LOD/LOQ was given -- this negative/qualitative finding is not converted into a fabricated quantitative claim.
  Recommended change: None.
- `NQ12-G05`: **supported**. Compound-resolved LOD/LOQ pairs match the table exactly and are correctly demoted to optional_content since they are a strict elaboration of G01's range claim, avoiding double counting in required-content coverage.
  Recommended change: None.
- `NQ12-G06`: **supported**. Compound-resolved LOD/LOQ pairs match the table exactly and are correctly demoted to optional_content relative to G02.
  Recommended change: None.
- `NQ12-G07`: **supported**. Retention time (5.884→11.422 min) and parent ion m/z (405→755) increase monotonically with chain length across the table, while LOD/LOQ values do not (e.g., LOD dips from 54.29 to 34.39 then rises to 73.96 before falling to 35.02), confirming both halves of the proposition.
  Recommended change: None.
- `NQ12-G08`: **supported**. Correctly synthesized limitation statement grounded in the compound- and method-specific patterns shown by both tables; does not overstate beyond the two studies.
  Recommended change: None.
- `NQ12-G09`: **supported**. Correctly restricts the quantitative findings to water matrix and the specific C7-C14/C8-C14 subsets without universalizing to other PFAS classes or matrices.
  Recommended change: None.
- `NQ12-B01`: **supported**. Boundary constraint directly restates the frozen must_not_claim boundary and has an executable violation_rule; correctly excluded from coverage scoring as constraint_only.
  Recommended change: None.

Human-review priorities:
- Confirm the grading harness truly excludes optional_content groups (G03, G05, G06, G07, G08, G09) and the constraint_only group (B01) from the required-content coverage denominator, since several optional groups restate numeric detail already present in G01/G02/G04 by design.
- The reference_answer's 'several-fold' language and G03's full_rule tolerance wording are now aligned in this revision; no further action needed but worth a final confirmation at project-author sign-off.

### Non-normative reference prose

The available evidence shows that PFAS analytical sensitivity, expressed as LOD and LOQ, depends on both chain length (or individual compound identity) and the analytical method, and that instrument settings can further alter this behavior in a chain-length-selective way.

In a developed SPE–UHPLC–MS/MS method for water, C8–C14 PFAS (PFOA, PFNA, PFOS, PFDA, PFUnDA, PFDS, PFDoDA, PFTrDA, PFTeDA) each have their own LOD and LOQ values, rather than sharing a single detection limit across the series. Reported LODs span 3–8 ng/L and LOQs 9–25 ng/L, with specific pairs such as 4/12 ng/L for PFOA, 7/22 ng/L for PFNA, 3/9 ng/L for PFOS, 8/24 ng/L for PFDA, 7/21 ng/L for PFUnDA, 3/11 ng/L for PFDS, 6/18 ng/L for PFDoDA, 8/25 ng/L for PFTrDA, and 3/11 ng/L for PFTeDA. These data show that, even across a relatively narrow C8–C14 range under one method, detection limits are compound-specific.

A different water-analysis procedure using stir bar sorptive extraction with thermal desorption GC–MS (SBSE–TD–GC–MS) for PFCAs PFHpA through PFTeDA also reports compound-dependent detection limits. In this method, LODs range from 21.17 to 73.96 ng/L and LOQs from 90.80 to 192.01 ng/L, with individual pairs such as 21.17/138.27 ng/L for PFHpA, 21.20/103.13 ng/L for PFOA, 30.12/90.80 ng/L for PFNA, 54.29/169.85 ng/L for PFDA, 34.39/132.90 ng/L for PFUnA, 73.96/192.01 ng/L for PFDoA, and 35.02/107.10 ng/L for PFTeDA. Under these SBSE–TD–GC–MS conditions, retention time and parent ion m/z increase with PFCA chain length, whereas LOD and LOQ values vary among analytes without following a simple monotonic trend with chain length.

Comparing the two water methods indicates that absolute sensitivity is strongly method-dependent as well as compound-dependent. For the C8–C14 PFAS set, the SPE–UHPLC–MS/MS procedure achieves lower LODs (3–8 ng/L) and LOQs (9–25 ng/L), while the SBSE–TD–GC–MS method for a C7–C14 PFCA set reports higher LODs (21.17–73.96 ng/L) and LOQs (90.80–192.01 ng/L). Thus, changing from one sample-preparation and instrumental configuration to another can shift the practical detection limits for a given PFAS chain-length range by several-fold, and each method yields its own compound-specific pattern.

Instrument tuning parameters can further influence chain-length-related sensitivity. In an SPE–LC–q‑TOF method for PFAS-related carboxylic acids in water, in-source fragmentation was affected by fragmentor voltage: at 60 V, the signal of short-chain PFAS (C < 5) was almost lost, leading the investigators to discard this setting. Although no numerical LOD or LOQ values were reported for this test, the observation shows that fragmentor voltage can selectively and strongly reduce the detectable signal, and therefore the effective sensitivity, for short-chain PFAS in this method.

Overall, the reported studies demonstrate that PFAS LOD/LOQ behavior is both compound- and method-specific. Within a given method, detection limits differ across PFAS chain lengths and do not necessarily follow a simple monotonic trend with chain length. Between methods, the absolute LOD/LOQ levels can differ substantially for similar chain-length ranges. The data are limited to water matrices and specific C7–C14/C8–C14 PFAS subsets and do not establish a single universal relationship between PFAS chain length and LOD/LOQ across all PFAS classes or analytical platforms.

### Prose-to-ledger map

- The available evidence shows that PFAS analytical sensitivity, expressed as LOD and LOQ, depends on both chain length (or individual compound identity) and the analytical method, and that instrument settings can further alter this behavior in a chain-length-selective way. -> NQ12-G01, NQ12-G02, NQ12-G03, NQ12-G04, NQ12-G08
- In a developed SPE–UHPLC–MS/MS method for water, C8–C14 PFAS (PFOA, PFNA, PFOS, PFDA, PFUnDA, PFDS, PFDoDA, PFTrDA, PFTeDA) each have their own LOD and LOQ values, rather than sharing a single detection limit across the series. -> NQ12-G01
- Reported LODs span 3–8 ng/L and LOQs 9–25 ng/L, with specific pairs such as 4/12 ng/L for PFOA, 7/22 ng/L for PFNA, 3/9 ng/L for PFOS, 8/24 ng/L for PFDA, 7/21 ng/L for PFUnDA, 3/11 ng/L for PFDS, 6/18 ng/L for PFDoDA, 8/25 ng/L for PFTrDA, and 3/11 ng/L for PFTeDA. -> NQ12-G01, NQ12-G05
- These data show that, even across a relatively narrow C8–C14 range under one method, detection limits are compound-specific. -> NQ12-G01
- A different water-analysis procedure using stir bar sorptive extraction with thermal desorption GC–MS (SBSE–TD–GC–MS) for PFCAs PFHpA through PFTeDA also reports compound-dependent detection limits. -> NQ12-G02
- In this method, LODs range from 21.17 to 73.96 ng/L and LOQs from 90.80 to 192.01 ng/L, with individual pairs such as 21.17/138.27 ng/L for PFHpA, 21.20/103.13 ng/L for PFOA, 30.12/90.80 ng/L for PFNA, 54.29/169.85 ng/L for PFDA, 34.39/132.90 ng/L for PFUnA, 73.96/192.01 ng/L for PFDoA, and 35.02/107.10 ng/L for PFTeDA. -> NQ12-G02, NQ12-G06
- Under these SBSE–TD–GC–MS conditions, retention time and parent ion m/z increase with PFCA chain length, whereas LOD and LOQ values vary among analytes without following a simple monotonic trend with chain length. -> NQ12-G07
- Comparing the two water methods indicates that absolute sensitivity is strongly method-dependent as well as compound-dependent. -> NQ12-G03, NQ12-G08
- For the C8–C14 PFAS set, the SPE–UHPLC–MS/MS procedure achieves lower LODs (3–8 ng/L) and LOQs (9–25 ng/L), while the SBSE–TD–GC–MS method for a C7–C14 PFCA set reports higher LODs (21.17–73.96 ng/L) and LOQs (90.80–192.01 ng/L). -> NQ12-G03
- Thus, changing from one sample-preparation and instrumental configuration to another can shift the practical detection limits for a given PFAS chain-length range by several-fold, and each method yields its own compound-specific pattern. -> NQ12-G03, NQ12-G08
- Instrument tuning parameters can further influence chain-length-related sensitivity. -> NQ12-G04
- In an SPE–LC–q‑TOF method for PFAS-related carboxylic acids in water, in-source fragmentation was affected by fragmentor voltage: at 60 V, the signal of short-chain PFAS (C < 5) was almost lost, leading the investigators to discard this setting. -> NQ12-G04
- Although no numerical LOD or LOQ values were reported for this test, the observation shows that fragmentor voltage can selectively and strongly reduce the detectable signal, and therefore the effective sensitivity, for short-chain PFAS in this method. -> NQ12-G04
- Overall, the reported studies demonstrate that PFAS LOD/LOQ behavior is both compound- and method-specific. -> NQ12-G01, NQ12-G02, NQ12-G03, NQ12-G08
- Within a given method, detection limits differ across PFAS chain lengths and do not necessarily follow a simple monotonic trend with chain length. -> NQ12-G01, NQ12-G02, NQ12-G07, NQ12-G08
- Between methods, the absolute LOD/LOQ levels can differ substantially for similar chain-length ranges. -> NQ12-G03
- The data are limited to water matrices and specific C7–C14/C8–C14 PFAS subsets and do not establish a single universal relationship between PFAS chain length and LOD/LOQ across all PFAS classes or analytical platforms. -> NQ12-G08, NQ12-G09

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
> If only relying on the initial pH for its effects on the degradation of PFAS, it is likely to lead to a false interpretation.

**NQ15_MMG002** (optional_gold; `2023 - Unknown - Recent advances in electrochemical decontamination of perfluorinated compounds from water - a review.pdf`, chunk `16`)
> There is no reported consensus on the effects of pH to date.

**NQ15_MMG003** (optional_gold; `2023 - Unknown - Recent advances in electrochemical decontamination of perfluorinated compounds from water - a review.pdf`, chunk `18`)
> (2014) compared the effects of three electrolytes on the degradation of 6:2 fluorotelomer sulfonic acid (20 mg/L) on a Ti/SnO2-Sb2O5-Bi2O3 anode.

**NQ15_MMG004** (optional_gold; `2023 - Unknown - Recent advances in electrochemical decontamination of perfluorinated compounds from water - a review.pdf`, chunk `46`)
> Electrochemical decontamination of perfluorinated compounds 11 4.2.3 Electrolyte type The chemical components in an electrolyte can also affect the removal of PFAS through different influencing mechanisms in an electro-coagulation process.

**NQ15_MMG005** (optional_gold; `2023 - Alam - Experimental investigations of Per- and Poly-fluoroalkyl substances (PFAS) degradation by non-thermal plasma in aqueous solutions.pdf`, chunk `40`)
> As the conductivity of the electrolyte solution and the surface water were comparable (300 µ S/cm versus 320 µ S/cm), the composition of the cations and anions in the surface water was then considered a possible cause of the differing breakdown rates.

### Normative content claim groups

#### NQ15-G01

- Component: `NQ15-T02`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: Across PFAS electro-oxidation studies, there is no reported consensus on how pH affects degradation, and this absence of consensus can make it harder to interpret or compare pH trends across experiments.
- Material qualifiers: ["The lack of consensus is explicitly stated in the review evidence.", "It is a reasonable inference (not directly quoted) that this lack of consensus complicates comparison and interpretation of pH trends across studies or experiments.", "Scope is PFAS electro-oxidation degradation in aqueous systems, based on a literature review rather than a single dataset."]
- Evidence: NQ15_MMG002
- Prior atomic claims: NQ15-C01
- Full: FULL if the answer states that there is no clear or no reported consensus on how pH affects PFAS electro-oxidation degradation (or PFAS electrochemical degradation). Mentioning that this lack of consensus makes it harder to interpret or compare pH effects across studies is permissible but not required for FULL credit.
- Partial: PARTIAL if the answer correctly implies but does not explicitly state that consensus is lacking (e.g., describes pH effects as highly variable or inconsistent without using consensus language), or if it correctly states that there is no consensus but places this in a clearly broader or only loosely related PFAS context without mentioning electro-oxidation or electrochemical degradation.
- Contradiction: CONTRADICTED if the answer asserts that there is a clear, consistent, or well-established consensus on how pH affects PFAS electro-oxidation degradation, or otherwise claims that pH effects are settled and straightforward to interpret across studies.

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
- Proposition: Electrolyte chemical composition, including the identities of its ions, can strongly affect PFAS removal or degradation performance, so the electrolyte should be treated as a mechanistically active variable rather than an inert background salt.
- Material qualifiers: ["Effects are demonstrated in specific systems: electro-oxidation, electro-coagulation, and non-thermal plasma treatments.", "Because of these effects, electrolyte choice should be treated as a mechanistically active experimental variable, not an inert background chosen only for conductivity.", "The inference that ions introduced for pH control (e.g., via buffers) may also act as active electrolyte components is suggested by extension but not directly tested in the cited studies."]
- Evidence: NQ15_MMG003, NQ15_MMG004, NQ15_MMG005
- Prior atomic claims: NQ15-C03
- Full: FULL if the answer explains that the chemical composition or identity of the electrolyte (including which ions are present) can significantly change PFAS removal or degradation outcomes, and explicitly draws the conclusion that electrolyte choice is a mechanistically active parameter rather than an inert background chosen only for conductivity or pH control.
- Partial: PARTIAL if the answer correctly notes that electrolyte or ion composition can affect PFAS removal or degradation, but does not explicitly state that electrolyte should be treated as a mechanistically active variable (e.g., only lists study-specific effects without generalizing), or if it states that electrolytes are mechanistically active but only weakly supports this with examples.
- Contradiction: CONTRADICTED if the answer claims or strongly implies that electrolyte identity or ion composition is generally inert or unimportant for PFAS removal/degradation performance (e.g., that any electrolyte of similar conductivity can be used without affecting results).

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
- Importance: `supplementary`
- Function: `limitation`
- Scoring role: `optional_content`
- Proposition: The available evidence on pH and electrolyte effects for PFAS focuses on electrochemical and non-thermal plasma treatments of a limited set of PFAS (such as 6:2 fluorotelomer sulfonic acid and PFOS) and does not establish how specific named buffer formulations perform or interfere across all PFAS compounds and treatment methods.
- Material qualifiers: ["Existing studies primarily cover electro-oxidation, electro-coagulation, and non-thermal plasma processes.", "The PFAS compounds explicitly covered include PFOS and 6:2 fluorotelomer sulfonic acid, among general PFAS.", "No supplied evidence directly evaluates specific named buffer systems or their interference across the full range of PFAS and treatment methods."]
- Evidence: NQ15_MMG001, NQ15_MMG002, NQ15_MMG003, NQ15_MMG004, NQ15_MMG005
- Prior atomic claims: NQ15-C08
- Full: FULL if the answer states that the cited evidence on pH and electrolyte effects is limited to certain PFAS, matrices, and treatment types (e.g., electro-oxidation, electro-coagulation, non-thermal plasma) and explicitly notes that it does not establish how specific buffer formulations perform or interfere across all PFAS and treatment methods.
- Partial: PARTIAL if the answer acknowledges that the evidence base is limited in PFAS types or treatment methods but does not specifically mention the gap regarding named buffer formulations, or vice versa.
- Contradiction: CONTRADICTED if the answer asserts that the current evidence base comprehensively covers how specific buffers behave across essentially all PFAS compounds and treatment technologies.


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

- `NQ15-G01`: **supported**. Central proposition ('no reported consensus on pH effects') is directly entailed by the exact span. The interpretive-difficulty material qualifier is explicitly labeled in the qualifier text itself as a reasonable inference rather than a directly quoted fact, and the full_rule correctly makes it optional/permissible rather than mandatory for FULL credit, resolving the prior overreach concern.
  Recommended change: None required; retain human-review note on whether the interpretive-difficulty qualifier should ever be tightened to non-required commentary outside material_qualifiers.
- `NQ15-G02`: **supported**. Canonical proposition and material qualifiers map exactly onto the quoted span. The previously flagged 'real-time monitoring near the anode is necessary' overreach (C02) has been dropped rather than folded into this group's scoring rules, correctly respecting the record's own does_not_support field.
  Recommended change: None.
- `NQ15-G03`: **supported**. Core proposition that electrolyte composition can strongly affect PFAS removal/degradation and should be treated as mechanistically active is supported by synthesis of MMG004 (explicit) plus MMG003/MMG005 (case examples). The buffer-extension material qualifier is explicitly self-flagged as untested/inferential and is not required by full_rule, partial_rule, or contradiction_rule, so it does not convert an unsupported inference into a scored requirement.
  Recommended change: None required; consider moving the buffer-extension sentence out of material_qualifiers into a non-scored note field if a future revision wants stricter separation between entailed qualifiers and disclosed inferences.
- `NQ15-G05`: **supported**. System/mechanism non-transferability is a reasonable synthesis across three distinct treatment technologies showing divergent electrolyte-dependent outcomes; synthesis_required=true is correctly set, and the proposition is independently answerable from G03 (general mechanistic-activity claim) rather than a duplicate.
  Recommended change: None.
- `NQ15-G06`: **supported**. Study-specific ordering (NaClO4 > NaCl > Na2SO4) is supported by the cited span combined with the supported_claim field; correctly scoped as optional_content, avoiding inflation of required denominator.
  Recommended change: None.
- `NQ15-G07`: **supported**. Quantitative electro-coagulation removal percentages are directly supported by the underlying gold record's supported_claim field, and this revision now includes an explicit ±1 percentage point numeric tolerance in addition to hedge-word equivalents, resolving the prior suggestion to strengthen the numeric rule.
  Recommended change: None.
- `NQ15-G08`: **supported**. Hypothesis-only framing (300 vs 320 µS/cm, monovalent vs monovalent+divalent) is faithfully preserved from the evidence and correctly scoped as optional_content with hedged full/partial rules that do not overstate the hypothesis as proven.
  Recommended change: None.
- `NQ15-G09`: **supported**. Limitation claim about scope of evidence (no direct data on named buffers, limited PFAS/treatment coverage) is a fair characterization of the five gold records collectively and does not assert any buffer-specific finding as positive evidence.
  Recommended change: None.
- `NQ15-B01`: **supported**. Boundary constraint against claiming a universally correct buffer/electrolyte is correctly excluded from coverage (scoring_role constraint_only) and has an executable violation_rule; it directly operationalizes the must_not_claim task boundary.
  Recommended change: None.

Human-review priorities:
- Confirm the buffer must_include boundary is acceptably satisfied via non-normative prose synthesis and the disclosed-but-unscored material qualifiers in G03, since no gold record contains the word 'buffer' and no claim group makes a buffer-specific assertion a scoring requirement.
- Note that G01's required core content rests on an evidence_type='optional_gold' record (NQ15_MMG002) while G03 and G05 (also core required_content) rest entirely on optional_gold records (MMG003-005); confirm this evidence_type/scoring_role divergence is an intentional and accepted convention in this ledger schema, not an oversight.
- G01's material qualifier that lack of consensus 'complicates comparison and interpretation of pH trends' remains an inference beyond the literal quoted span; the full_rule already treats it as optional/permissible rather than mandatory, which is an acceptable resolution but worth a final author sign-off.
- G03's material qualifier disclosing the buffer-extension inference is explicitly self-flagged as 'not directly tested'; consider whether such explicitly non-entailed statements belong in material_qualifiers versus a separate non-scored annotation, for schema cleanliness going forward.

### Non-normative reference prose

In PFAS electro-oxidation studies, a review notes that there is no reported consensus on how pH affects degradation, which makes it difficult to compare or generalize pH trends across experiments [NQ15_MMG002]. The same review warns that if one relies only on the initial pH to assess pH effects on PFAS degradation, this is likely to lead to a false interpretation of the results [NQ15_MMG001]. Together, these points imply that pH-control strategies that only specify a starting pH, without tracking how pH evolves in the system, can limit how reliably pH-dependent behavior is interpreted or compared between studies.

The studies also show that electrolyte composition is not an inert background condition. In electro-oxidation of 6:2 fluorotelomer sulfonic acid (20 mg/L) on a Ti/SnO2-Sb2O5-Bi2O3 anode, changing the supporting electrolyte from NaClO4 to NaCl to Na2SO4 caused degradation performance to decrease in the order NaClO4 > NaCl > Na2SO4 [NQ15_MMG003]. In Fe-anode electro-coagulation of PFOS, removal efficiencies differed markedly among electrolytes—99.6% in NaCl, 93.7% in Na2SO4, 63.5% in NaNO3, and 45.4% in NaH2PO4—demonstrating that the chemical components of the electrolyte can affect PFAS removal through different mechanisms in this process [NQ15_MMG004]. In non-thermal plasma degradation of PFOS, an electrolyte solution and surface water with comparable conductivities (300 vs 320 µS/cm) nonetheless showed different breakdown rates, and the differing cation compositions (monovalent vs monovalent plus divalent) were considered a possible cause [NQ15_MMG005]. These examples indicate that the identities of the ions present, including those added for conductivity or pH control, can substantially change PFAS removal or degradation behavior, so electrolyte choice should be treated as a mechanistically active design variable.

Because pH effects lack consensus and initial pH alone can be misleading [NQ15_MMG001; NQ15_MMG002], and because electrolyte ions clearly participate in or modify removal and degradation mechanisms [NQ15_MMG003; NQ15_MMG004; NQ15_MMG005], electrolyte and pH-control choices together limit how easily results can be transferred between systems. Electrolyte-dependent trends observed for 6:2 fluorotelomer sulfonic acid electro-oxidation on a Ti/SnO2-Sb2O5-Bi2O3 anode [NQ15_MMG003], for PFOS removal in Fe-anode electro-coagulation [NQ15_MMG004], and for PFOS degradation in non-thermal plasma [NQ15_MMG005] differ from one another, implying that optimal electrolyte or ion compositions are system- and mechanism-specific rather than universal. Thus, in designing PFAS removal or degradation experiments, electrolyte formulations (including ions introduced to control pH) should be chosen with an explicit awareness that they can both help maintain the desired pH range and simultaneously alter reaction pathways or rates, and their impacts need to be characterized separately for each treatment configuration. The current evidence, however, is limited to a small set of PFAS and treatment types and does not establish how particular named buffer systems behave across all PFAS compounds or technologies [NQ15_MMG001; NQ15_MMG002; NQ15_MMG003; NQ15_MMG004; NQ15_MMG005].

### Prose-to-ledger map

- In PFAS electro-oxidation studies, a review notes that there is no reported consensus on how pH affects degradation, which makes it difficult to compare or generalize pH trends across experiments [NQ15_MMG002]. -> NQ15-G01
- The same review warns that if one relies only on the initial pH to assess pH effects on PFAS degradation, this is likely to lead to a false interpretation of the results [NQ15_MMG001]. -> NQ15-G02
- Together, these points imply that pH-control strategies that only specify a starting pH, without tracking how pH evolves in the system, can limit how reliably pH-dependent behavior is interpreted or compared between studies. -> NQ15-G01, NQ15-G02
- The studies also show that electrolyte composition is not an inert background condition. -> NQ15-G03
- In electro-oxidation of 6:2 fluorotelomer sulfonic acid (20 mg/L) on a Ti/SnO2-Sb2O5-Bi2O3 anode, changing the supporting electrolyte from NaClO4 to NaCl to Na2SO4 caused degradation performance to decrease in the order NaClO4 > NaCl > Na2SO4 [NQ15_MMG003]. -> NQ15-G03, NQ15-G06
- In Fe-anode electro-coagulation of PFOS, removal efficiencies differed markedly among electrolytes—99.6% in NaCl, 93.7% in Na2SO4, 63.5% in NaNO3, and 45.4% in NaH2PO4—demonstrating that the chemical components of the electrolyte can affect PFAS removal through different mechanisms in this process [NQ15_MMG004]. -> NQ15-G03, NQ15-G07
- In non-thermal plasma degradation of PFOS, an electrolyte solution and surface water with comparable conductivities (300 vs 320 µS/cm) nonetheless showed different breakdown rates, and the differing cation compositions (monovalent vs monovalent plus divalent) were considered a possible cause [NQ15_MMG005]. -> NQ15-G03, NQ15-G08
- These examples indicate that the identities of the ions present, including those added for conductivity or pH control, can substantially change PFAS removal or degradation behavior, so electrolyte choice should be treated as a mechanistically active design variable. -> NQ15-G03, NQ15-G05
- Because pH effects lack consensus and initial pH alone can be misleading [NQ15_MMG001; NQ15_MMG002], and because electrolyte ions clearly participate in or modify removal and degradation mechanisms [NQ15_MMG003; NQ15_MMG004; NQ15_MMG005], electrolyte and pH-control choices together limit how easily results can be transferred between systems. -> NQ15-G01, NQ15-G02, NQ15-G03, NQ15-G05
- Electrolyte-dependent trends observed for 6:2 fluorotelomer sulfonic acid electro-oxidation on a Ti/SnO2-Sb2O5-Bi2O3 anode [NQ15_MMG003], for PFOS removal in Fe-anode electro-coagulation [NQ15_MMG004], and for PFOS degradation in non-thermal plasma [NQ15_MMG005] differ from one another, implying that optimal electrolyte or ion compositions are system- and mechanism-specific rather than universal. -> NQ15-G05, NQ15-B01
- Thus, in designing PFAS removal or degradation experiments, electrolyte formulations (including ions introduced to control pH) should be chosen with an explicit awareness that they can both help maintain the desired pH range and simultaneously alter reaction pathways or rates, and their impacts need to be characterized separately for each treatment configuration. -> NQ15-G02, NQ15-G03, NQ15-G05
- The current evidence, however, is limited to a small set of PFAS and treatment types and does not establish how particular named buffer systems behave across all PFAS compounds or technologies [NQ15_MMG001; NQ15_MMG002; NQ15_MMG003; NQ15_MMG004; NQ15_MMG005]. -> NQ15-G09, NQ15-B01

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
> The comparison between the NTP technologies and the other AOPs from the viewpoint of energy consumption (evaluated in term of elec - trical energy per order values - E EO ), classifies the NTP processes in a central zone with median energy consumptions in the 1 – 100 kWh/m 3 range, at the same level of photo-Fenton and pure electrolytic AOPs.

**NQ23_MMG002** (required_gold; `2021 - Nau-Hix - Field Demonstration of a Pilot-Scale Plasma Reactor for the Rapid Removal of Poly- and Perfluoroalkyl Substances in Groundwater.pdf`, chunk `28`)
> where E (kWh) is the energy consumed by the high-voltage power supplies, gas and liquid pumps, and rotating spark gap, V (L) is the treatment volume for each experimental condition, and C i and Cf are the initial and ﬁnal concentrations (below the USEPA HAL), respectively, of PFOA and PFOS (ng/L).

**NQ23_MMG003** (required_gold; `2023 - Smith - Electrochemical Oxidation for Treatment of PFAS in Contaminated Water and Fractionated Foam─A Pilot-Scale Study.pdf`, chunk `33`)
> The energy consumption of EO can be calculated as described previously 15 and as presented in eq S18.

**NQ23_MMG004** (required_gold; `2026 - Kumar - Degradation and defluorination of perfluorooctane sulfonate (PFOS) forever chemical in water using hydrodynamic cavitation treatment.pdf`, chunk `46`)
> The EEO ranged from 7 to 598 kWh/m³/order, while the energy yield varied between 17 and 286 mg/kWh.

**NQ23_MMG005** (required_gold; `2024 - Chen - Combining nonthermal N2 plasma with a denitrifying biofilm reactor for PFAS-contaminated wastewater remediation.pdf`, chunk `21`)
> However, the primary challenge with N 2 plasma is its low PFAS degradation efficiency (45 % for PFOA and 60 % for PFDA) combined with high energy consumption (EEO values of 370 kWh/m 3 for PFOA and 260 kWh/m 3 for PFDA).

**NQ23_MMG006** (negative_gold; `2025 - Capodaglio - Prospects of Novel Technologies for PFAS Destruction in Water and Wastewater.pdf`, chunk `11`)
> It can be observed that the reported ranges show a high variability, reflecting the uncertainty and nonuniformity of experimental conditions in the respective studies (Table 1).

**NQ23_MMG007** (optional_gold; `2026 - Chen - Ferrate-assisted nonthermal plasma for efficient PFOA degradation in landfill leachate - Mitigating bulk organic interference and enhancing.pdf`, chunk `35`)
> Application potential A consolidated comparison of reported EE/O values, together with key experimental parameters such as water type, initial PFAS concen - tration, reactor scale, reaction time, and removal/defluorination effi - ciency, is provided in Table S1 to support a transparent and context- aware evaluation across technologies.

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
- Proposition: Another study indicates that a consolidated comparison of reported EE/O values for different PFAS treatment technologies is only meaningful when EE/O is presented together with key experimental parameters such as water type, initial PFAS concentration, reactor scale, reaction time, and removal or defluorination efficiency, enabling transparent and context-aware evaluation across technologies.
- Material qualifiers: ["the comparison concerns reported EE/O values across multiple PFAS treatment technologies", "EE/O values are provided together with parameters such as water type, initial PFAS concentration, reactor scale, reaction time, and removal or defluorination efficiency", "this combined reporting is intended to support transparent and context-aware cross-technology evaluation rather than unqualified ranking by EE/O alone"]
- Evidence: NQ23_MMG007
- Prior atomic claims: NQ23-C07
- Full: Full credit if the answer explains that comparing EE/O values across PFAS treatment technologies requires contextual information—specifically naming at least several of the parameters (e.g., water type, initial concentration, reactor scale, reaction time, removal/defluorination efficiency)—and states that including these parameters enables more transparent, context-aware evaluation.
- Partial: Partial credit if the answer asserts that EE/O comparisons require contextual parameters but names them only generically (e.g., 'operating conditions') without specifying any of the listed examples, or if it lists some parameters without clearly stating that they are necessary for meaningful cross-technology EE/O comparison.
- Contradiction: Mark as contradicted if the answer claims that EE/O values alone, without accompanying experimental context, are sufficient for a fair and transparent comparison across different PFAS technologies.

#### NQ23-G10

- Component: `NQ23-T02`
- Importance: `core`
- Function: `limitation`
- Scoring role: `required_content`
- Proposition: Given the wide ranges of reported energy metrics for PFAS degradation (including EEO values from a few to several hundred kWh/m³ or kWh/m³ per order and differing metrics such as mg/kWh), together with high variability and nonuniform experimental conditions across studies and the need for contextual parameters in EE/O comparisons, no single universal energy-consumption value can fairly represent all PFAS degradation methods, and cross-study comparisons must be interpreted in the specific context of each experiment.
- Material qualifiers: ["this conclusion is based on the wide spread of reported energy metrics, from single-digit to several-hundred kWh/m³ or kWh/m³/order, and the use of different metrics such as EEO and mg/kWh", "high variability and nonuniform experimental conditions across studies contribute to this limitation", "meaningful comparison requires considering experimental context, including parameters such as water type, initial concentration, reactor scale, reaction time, and performance endpoints"]
- Evidence: NQ23_MMG001, NQ23_MMG004, NQ23_MMG005, NQ23_MMG006, NQ23_MMG007
- Prior atomic claims: NQ23-C10
- Full: Full credit if the answer explicitly states that no single universal energy-consumption or efficiency value can fairly represent all PFAS degradation methods and that cross-study numerical comparisons must be interpreted in light of the specific experimental context (e.g., metrics used, ranges of values, and differing conditions), drawing on ideas of wide value ranges, metric diversity, and nonuniform conditions.
- Partial: Partial credit if the answer correctly states either that no universal energy-consumption value can represent all methods or that cross-study comparisons must be context-specific, but does not clearly connect this to both wide value ranges and differing metrics/conditions; or if it mentions wide variability and different metrics but does not explicitly draw the conclusion about the impossibility of a single representative value.
- Contradiction: Mark as contradicted if the answer asserts or clearly implies that a single typical or universal energy-consumption number can adequately represent all PFAS degradation methods, or that cross-study comparisons can be made without regard to experimental context.


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

- `NQ23-G01`: **supported**. Metric diversity (EEO/EE-O kWh/m3 or kWh/m3/order vs. mg/kWh energy yield) is entailed collectively by the cited spans; MMG004 alone shows two distinct metrics in one span, so the synthesis is not overreaching.
  Recommended change: None.
- `NQ23-G02`: **supported**. EEO 7–598 kWh/m3/order and energy yield 17–286 mg/kWh are verbatim in the exact span; numeric_required correctly set true with matching accepted equivalents.
  Recommended change: None.
- `NQ23-G03`: **supported**. PFOA/PFDA EEO and efficiency values are verbatim in the span with correct compound pairing.
  Recommended change: None (see human_review_priorities on core/optional weighting vs. G02).
- `NQ23-G04`: **supported**. 1–100 kWh/m3 median EEO range and comparison to photo-Fenton/electrolytic AOPs verbatim in span.
  Recommended change: None.
- `NQ23-G06`: **supported**. Correctly resolves the prior Model B flag: the unverifiable EE/O numeric range/average (9.2-31, avg 16±5.8) has been dropped; remaining proposition (E, V, Ci, Cf components and below-HAL endpoint) matches the exact span verbatim, and numeric_required is now false, consistent with the absence of numbers in the span.
  Recommended change: None.
- `NQ23-G07`: **supported**. Correctly resolves the prior Model B flag: unverifiable kWh/m3 totals (270/93) and 9h duration have been dropped; remaining proposition (eq S18 reference, no numeric values in excerpt) matches the exact span verbatim.
  Recommended change: None.
- `NQ23-G08`: **supported**. Variability/nonuniformity statement and its link to comparison limits are entailed by the span; negative_gold evidence is used appropriately as direct support for a limitation claim, not converted into an affirmative numeric finding.
  Recommended change: None.
- `NQ23-G09`: **supported**. Need for contextual parameters (water type, initial concentration, reactor scale, reaction time, removal/defluorination efficiency) alongside EE/O values is entailed by the span. Note: sole evidence is typed 'optional_gold' in the raw gold set despite required_content scoring_role — thematically justified since this content is central to task component T02, but flagged for human review.
  Recommended change: None required; optionally annotate that MMG007's 'optional_gold' evidence-type label reflects lack of concrete values rather than importance to the answer.
- `NQ23-G10`: **supported**. Correctly resolves prior Model B flag: NQ23_MMG003 (unsupported numeric anchor) has been dropped from evidence_ids; remaining five spans jointly and directly entail the wide-range/differing-metric/nonuniform-conditions synthesis.
  Recommended change: None.
- `NQ23-B01`: **supported**. Constraint text mirrors the must_not_claim boundary and is grounded in MMG006's variability statement; violation_rule is executable and correctly marked scoring_role constraint_only (excluded from coverage denominator).
  Recommended change: None.

Human-review priorities:
- G02 (hydrodynamic cavitation) is core/required_content while G03 (N2 plasma) and G04 (NTP) are supplementary/optional_content, despite all three being equally verbatim-supported numeric examples from required_gold evidence; defensible since G01/G10 already cover generic metric-identification and comparability requirements, but confirm this distribution matches intended emphasis.
- G09's sole evidence record (NQ23_MMG007) is labeled 'optional_gold' in the raw gold evidence set, yet the claim group is scored as core/required_content; this is justified by the content's centrality to explaining comparability restrictions (task component T02), but worth a project-author sanity check.
- G10 (required_content) and B01 (constraint_only) both draw on NQ23_MMG006 and the 'no universal value' theme; confirm in the downstream scoring implementation that constraint_only groups are truly excluded from the coverage denominator so no unintended double credit occurs.
- The open question of whether NQ23_MMG002's and NQ23_MMG003's source PDFs contain the EE/O numeric range/average (9.2-31, avg 16±5.8 kWh/m3) and EO totals (270/93 kWh/m3) elsewhere (e.g., results tables) remains unresolved for full document review, though the ledger no longer depends on these unverified numbers for scoring — documented in unresolved_or_unsupported and does not block approval.
- The prior duplicate group G05 (restating G02/G03 content) has been removed in this revision, resolving the earlier non-blocking redundancy flag.

### Non-normative reference prose

Energy-consumption and energy-efficiency evidence for PFAS degradation methods is reported using several different metrics, including electrical energy per order (EEO or EE/O, typically in kWh per cubic meter or kWh per cubic meter per order of removal) and energy yield in mg of contaminant removed per kWh, so numerical values reported under different metrics are not directly interchangeable.

A review of non-thermal plasma (NTP) processes for PFAS-contaminated water reports that, when energy consumption is evaluated as EEO, NTP technologies fall in a central zone with median energy consumptions in the range of about 1–100 kWh/m³, at roughly the same level as photo-Fenton and pure electrolytic advanced oxidation processes. In a hydrodynamic cavitation study targeting PFOS degradation and defluorination in water, the reported EEO values ranged from 7 to 598 kWh/m³ per order, and the energy yield ranged from 17 to 286 mg per kWh, demonstrating a very wide spread in energy efficiency under different conditions. For PFAS degradation in wastewater using N₂ nonthermal plasma, one study reports EEO values of 370 kWh/m³ for PFOA and 260 kWh/m³ for PFDA, with corresponding degradation efficiencies of 45% and 60%, respectively, indicating relatively high energy inputs for only partial degradation.

Other work provides methodological context for how energy metrics are defined and calculated. In a field pilot-scale plasma reactor treating groundwater contaminated with PFOA and PFOS, EE/O is defined from the electrical energy consumed by the high-voltage power supplies, gas and liquid pumps, and rotating spark gap, together with the treated volume and the reduction from initial to final concentrations driven below the USEPA health advisory level. A pilot-scale electrochemical oxidation study treating PFAS-contaminated water and fractionated foam notes that the energy consumption of EO can be calculated according to a previously described method and an equation referred to as eq S18, although specific energy values are not given in the cited excerpt.

Taken together, these examples show that reported PFAS treatment energy metrics span from single-digit kWh/m³ per order (on the order of 7 kWh/m³/order in some hydrodynamic cavitation conditions) up to several hundred kWh/m³ or kWh/m³ per order (for example, 260–370 kWh/m³ in N₂ plasma and up to 598 kWh/m³/order in hydrodynamic cavitation), and that studies use varying metrics such as EEO or mg/kWh energy yield. A broader review of PFAS destruction technologies notes that the reported energy-related ranges show high variability, reflecting uncertainty and nonuniform experimental conditions across studies, which limits straightforward cross-study comparison of energy-consumption or efficiency values. Consistent with this, another study emphasizes that a consolidated comparison of reported EE/O values across technologies is only meaningful when presented together with key experimental parameters such as water type, initial PFAS concentration, reactor scale, reaction time, and removal or defluorination efficiency, to enable transparent and context-aware evaluation. In light of the wide spread of reported values, the differing energy metrics, and the nonuniform experimental conditions, no single universal energy-consumption value can fairly represent all PFAS degradation methods, and any cross-study comparison of energy metrics must be interpreted in the specific experimental context.

### Prose-to-ledger map

- Energy-consumption and energy-efficiency evidence for PFAS degradation methods is reported using several different metrics, including electrical energy per order (EEO or EE/O, typically in kWh per cubic meter or kWh per cubic meter per order of removal) and energy yield in mg of contaminant removed per kWh, so numerical values reported under different metrics are not directly interchangeable. -> NQ23-G01
- A review of non-thermal plasma (NTP) processes for PFAS-contaminated water reports that, when energy consumption is evaluated as EEO, NTP technologies fall in a central zone with median energy consumptions in the range of about 1–100 kWh/m³, at roughly the same level as photo-Fenton and pure electrolytic advanced oxidation processes. -> NQ23-G04
- In a hydrodynamic cavitation study targeting PFOS degradation and defluorination in water, the reported EEO values ranged from 7 to 598 kWh/m³ per order, and the energy yield ranged from 17 to 286 mg per kWh, demonstrating a very wide spread in energy efficiency under different conditions. -> NQ23-G02
- For PFAS degradation in wastewater using N₂ nonthermal plasma, one study reports EEO values of 370 kWh/m³ for PFOA and 260 kWh/m³ for PFDA, with corresponding degradation efficiencies of 45% and 60%, respectively, indicating relatively high energy inputs for only partial degradation. -> NQ23-G03
- In a field pilot-scale plasma reactor treating groundwater contaminated with PFOA and PFOS, EE/O is defined from the electrical energy consumed by the high-voltage power supplies, gas and liquid pumps, and rotating spark gap, together with the treated volume and the reduction from initial to final concentrations driven below the USEPA health advisory level. -> NQ23-G06
- A pilot-scale electrochemical oxidation study treating PFAS-contaminated water and fractionated foam notes that the energy consumption of EO can be calculated according to a previously described method and an equation referred to as eq S18, although specific energy values are not given in the cited excerpt. -> NQ23-G07
- Taken together, these examples show that reported PFAS treatment energy metrics span from single-digit kWh/m³ per order (on the order of 7 kWh/m³/order in some hydrodynamic cavitation conditions) up to several hundred kWh/m³ or kWh/m³ per order (for example, 260–370 kWh/m³ in N₂ plasma and up to 598 kWh/m³/order in hydrodynamic cavitation), and that studies use varying metrics such as EEO or mg/kWh energy yield. -> NQ23-G01, NQ23-G02, NQ23-G03
- A broader review of PFAS destruction technologies notes that the reported energy-related ranges show high variability, reflecting uncertainty and nonuniform experimental conditions across studies, which limits straightforward cross-study comparison of energy-consumption or efficiency values. -> NQ23-G08
- Consistent with this, another study emphasizes that a consolidated comparison of reported EE/O values across technologies is only meaningful when presented together with key experimental parameters such as water type, initial PFAS concentration, reactor scale, reaction time, and removal or defluorination efficiency, to enable transparent and context-aware evaluation. -> NQ23-G09
- In light of the wide spread of reported values, the differing energy metrics, and the nonuniform experimental conditions, no single universal energy-consumption value can fairly represent all PFAS degradation methods, and any cross-study comparison of energy metrics must be interpreted in the specific experimental context. -> NQ23-G10, NQ23-B01

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
> max ob - tained through the Thomas model was 5.71 mg/g, which was marginally lower as compared to the Q e obtained through Langmuir isotherm model (6.85 mg/g) mainly due to two reasons (a) the presence of the back - ground water matrix during the column run and (b) the size of the adsorbent was bigger (125 – 500 μ m) than used in the batch equilibrium and kinetic study (125 – 250 μ m).

### Normative content claim groups

#### NQ24-G01

- Component: `NQ24-T01`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: In a batch equilibrium study of PFOA adsorption onto CTAB‑impregnated activated carbon in aqueous media, the Langmuir isotherm maximum adsorption capacity (Qe) was 6.85 mg/g, with adsorbent particle sizes of 125–250 μm.
- Material qualifiers: ["measured in batch equilibrium conditions using a Langmuir isotherm model", "PFAS compound was PFOA", "adsorbent was CTAB‑impregnated activated carbon", "adsorbent particle size in batch was 125–250 μm", "endpoint reported in mg/g"]
- Evidence: NQ24_MMG001
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
- Evidence: NQ24_MMG001
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
- Evidence: NQ24_MMG001
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

- `NQ24-G01`: **supported**. Canonical proposition (batch Langmuir Qe 6.85 mg/g for PFOA on CTAB-impregnated AC, 125–250 μm) and all material qualifiers are directly entailed by the single exact_evidence_span. Numeric requirement and accepted equivalents are correctly scoped to this claim only. Full/partial/contradiction rules are executable and mutually consistent, and correctly guard against the 6.85 value being misattributed to the column.
  Recommended change: None.
- `NQ24-G02`: **supported**. Canonical proposition (column Thomas capacity 5.71 mg/g, background water matrix, 125–500 μm particles) and qualifiers are entailed by the same span. Rules correctly guard against misattributing 5.71 to batch or reversing the direction of difference for this study.
  Recommended change: None.
- `NQ24-G03`: **supported**. Correctly captures the comparative/limitation content (direction of difference, both attributed reasons, single-system scope) without re-requiring the numeric values, appropriately marked numeric_required: false. Function 'limitation' and scoring_role 'required_content' are consistent with task component T03's requirement to explain limiting conditions. Contradiction rule properly blocks universalization language, which is also independently covered by constraint B01 without double-counting since B01 is constraint_only.
  Recommended change: None.
- `NQ24-B01`: **supported**. Constraint is correctly excluded from coverage (scoring_role: constraint_only) and has an executable violation rule matching the frozen must_not_claim boundary (no single fixed capacity, no universalization of this study's specific batch–column relationship).
  Recommended change: None.

Human-review priorities:
- Resolved: the NQ24-C01 atomic_claim_dispositions rationale no longer contains the prior contradictory 'mapped to G03' vs. three-target-group wording; it now cleanly states a single target group (G03), consistent with source_atomic_claim_ids across G01/G02/G03.
- Resolved: the reference_answer_claim_map now includes the previously-unmapped opening sentence ('the batch equilibrium isotherm gave a higher modeled capacity...'), mapped to NQ24-G03.
- Non-blocking wording nitpick: in G01/G02 material_qualifiers, 'endpoint reported in mg/g' conflates endpoint (maximum adsorption capacity) with unit (mg/g); scoring rules are unaffected since both the endpoint concept and unit are independently required in full_rule, but a project author may wish to tighten this phrasing for clarity.
- Carried forward, unresolved by design (single non-exhaustive evidence record): confirm no other frozen gold record for NQ24 exists elsewhere in the corpus with additional batch-vs-column comparisons (other carbon types/PFAS/compounds), since decomposition into G01/G02/G03 all rest on one exact_evidence_span.
- Judgment call carried forward: confirm decomposing a single evidence span into three core required_content claim groups (vs. a more consolidated 1- or 2-group structure) matches project scoring-weight conventions for numeric_extraction questions with a single data point.
- Judgment call carried forward: verify the 'partially_supported' answerability label matches project convention for single-data-point numeric_extraction questions where the single instance itself is fully supported but generalization is not possible.

### Non-normative reference prose

In the available study of PFOA adsorption onto CTAB‑impregnated activated carbon, the batch equilibrium isotherm gave a higher modeled capacity than the corresponding column test. The Langmuir isotherm fit to batch data yielded a maximum adsorption capacity of 6.85 mg/g, whereas a fixed‑bed column analyzed with the Thomas breakthrough model gave a maximum capacity of 5.71 mg/g. The authors described the column capacity as marginally lower than the batch capacity and mainly attributed this difference to the presence of a background water matrix during the column run and the use of larger adsorbent particles in the column (125–500 μm) compared with the batch tests (125–250 μm). This example shows that, for this specific PFOA–activated carbon system under the reported aqueous conditions, modeled batch and column capacities differed slightly, and that differences in models, particle size, and water matrix conditions limit direct generalization to other activated carbons, PFAS, or test setups.

### Prose-to-ledger map

- In the available study of PFOA adsorption onto CTAB‑impregnated activated carbon, the batch equilibrium isotherm gave a higher modeled capacity than the corresponding column test. -> NQ24-G03
- The Langmuir isotherm fit to batch data yielded a maximum adsorption capacity of 6.85 mg/g, -> NQ24-G01
- whereas a fixed‑bed column analyzed with the Thomas breakthrough model gave a maximum capacity of 5.71 mg/g. -> NQ24-G02
- The authors described the column capacity as marginally lower than the batch capacity and mainly attributed this difference to the presence of a background water matrix during the column run and the use of larger adsorbent particles in the column (125–500 μm) compared with the batch tests (125–250 μm). -> NQ24-G02, NQ24-G03
- This example shows that, for this specific PFOA–activated carbon system under the reported aqueous conditions, modeled batch and column capacities differed slightly, and that differences in models, particle size, and water matrix conditions limit direct generalization to other activated carbons, PFAS, or test setups. -> NQ24-G03, NQ24-B01

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
> Beside regenerable IX-R, other traditional separation technologies such as reverse osmosis and nanofiltration, which produce a concentrated PFAS waste stream, have also been demonstrated in tandem with a destruction technology for effective remediation of PFAS [ 23 , 25 ].

**NQ26_MMG002** (required_gold; `2025 - Liu - Filtration and electrical membrane-based treatment methods for PFAS-contaminated water and preparation methods for the membranes employed.pdf`, chunk `21`)
> Membrane‑assisted chemical degradation Generally, the abovementioned treatment methods (filtra- tion, adsorption, and membrane distillation) can only con- centrate PFAS.

**NQ26_MMG003** (required_gold; `2023 - Sivagami - Electrochemical-based approaches for the treatment of forever chemicals - Removal of perfluoroalkyl and polyfluoroalkyl substances (PFAS) from.pdf`, chunk `58`)
> Another severe limitation of membrane-based processes is that they do not degrade PFAS;

**NQ26_MMG004** (required_gold; `2024 - Pervez - Structure and mechanism of nanoengineered membranes toward per- and polyfluoroalkyl substances (PFAS) removal from water - A critical review.pdf`, chunk `4`)
> Among different approaches, high-pressure membrane filtration pro - cesses that utilize nanoporous membranes like nanofiltration (NF) and reverse osmosis (RO) have proven to be highly effective in separating both short- and long-chain PFAS compounds with rejection efficiencies typically exceeding 90 % [ 24 , 25 ].

**NQ26_MMG005** (required_gold; `2025 - Liu - Filtration and electrical membrane-based treatment methods for PFAS-contaminated water and preparation methods for the membranes employed.pdf`, chunk `43`)
> To treat PFAS-contaminated water more effectively, research should be conducted on combining degradation (e.g., electrodegradation, biodegradation, etc.) and con- centration (e.g., filtration, membrane distillation, forward osmosis, etc.) treatments.

**NQ26_MMG006** (optional_gold; `2025 - Liu - Filtration and electrical membrane-based treatment methods for PFAS-contaminated water and preparation methods for the membranes employed.pdf`, chunk `21`)
> Membrane-assisted degradation differs from simple deg- radation in that PFAS are first adsorbed onto a membrane (to which catalysts may be added) and then degraded under light or an electric field (Fig.

**NQ26_MMG007** (negative_gold; `2021 - Ryan - Electrochemical technologies for per- and polyfluoroalkyl substances mitigation in.pdf`, chunk `51`)
> Of note, low-pressure membranes such as microfiltration and ultrafiltration poorly remove PFAS and are not discussed in this review (Glover et al., 2018;

**NQ26_MMG008** (optional_gold; `2021 - Groele - An investigation of plasma-driven decomposition of per- and polyfluoroalkyl substances (PFAS) in raw contaminated groundwater.pdf`, chunk `7`)
> carbon is incinerated, whereas in the membrane processes, the con- centrate is sent to an evaporation pool where the residue can be then collected and incinerated.

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
- Prior atomic claims: NQ26-C02
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

#### NQ26-G04

- Component: `NQ26-T02`
- Importance: `core`
- Function: `limitation`
- Scoring role: `required_content`
- Proposition: Membrane-based processes as a class are reported to have the limitation that they do not degrade PFAS and instead function mainly to separate or concentrate PFAS.
- Material qualifiers: ["their primary function is to separate or concentrate PFAS", "this limitation is noted for membrane-based processes as a class, including methods such as filtration, membrane distillation, forward osmosis, and related membranes", "degradation requires an additional distinct step or technology beyond simple membrane separation/concentration"]
- Evidence: NQ26_MMG003, NQ26_MMG002, NQ26_MMG005
- Prior atomic claims: NQ26-C01, NQ26-C02, NQ26-C03, NQ26-C06
- Full: Count as full if the answer explicitly states that membrane-based processes in general (or membrane PFAS treatments as a class) do not degrade PFAS and instead primarily separate or concentrate them, and notes that degradation requires additional steps or technologies beyond the membrane separation stage.
- Partial: Count as partial if the answer states that membrane-based PFAS treatments mainly separate or concentrate PFAS and are limited in that they do not destroy or chemically transform PFAS, but omits the explicit framing that this is a class-wide limitation or does not clearly distinguish these from separate degradation steps.
- Contradiction: Mark as contradicted if the answer asserts that membrane-based processes generally destroy or chemically degrade PFAS without needing separate degradation steps, or equates membrane retention/separation directly with PFAS destruction.

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
- Final target(s): NQ26-B01, NQ26-G01, NQ26-G04
- Rationale: The original claim combined (i) NF/RO separation performance and production of a concentrated waste stream and (ii) an implication that NF/RO specifically do not degrade PFAS. The NF/RO separation and concentration aspects are retained in G01. The non-degradation aspect is generalized and merged into the class-wide limitation on membrane-based processes in G04 and used in boundary constraint B01. Disposition targets normalized from ['NQ26-G01', 'NQ26-G04'] to ['NQ26-B01', 'NQ26-G01', 'NQ26-G04'] using final source_atomic_claim_ids.

#### NQ26-C02

- Prior claim: Filtration, membrane distillation, and forward osmosis are classified as concentration (separation) treatments for PFAS-contaminated water that can only concentrate PFAS and therefore need to be combined with separate degradation processes such as electrodegradation or biodegradation for PFAS destruction.
- Action: `revised`
- Final target(s): NQ26-B01, NQ26-G02, NQ26-G04, NQ26-G05
- Rationale: The original claim both classified filtration, membrane distillation, and forward osmosis as concentration treatments and asserted that they must be combined with separate degradation processes. These two independently scorable propositions are split: G02 captures their role as concentration-only routes, and G05 captures their relationship to separate degradation technologies, making clear that for filtration/membrane distillation/forward osmosis this combination is framed as a research recommendation rather than established practice. Disposition targets normalized from ['NQ26-G02', 'NQ26-G05'] to ['NQ26-B01', 'NQ26-G02', 'NQ26-G04', 'NQ26-G05'] using final source_atomic_claim_ids.

#### NQ26-C03

- Prior claim: Membrane-based processes as a class are reported to have a severe limitation in that they do not degrade PFAS and instead function mainly to separate or concentrate PFAS.
- Action: `revised`
- Final target(s): NQ26-B01, NQ26-G04
- Rationale: C03 restated, at a class level, that membrane-based processes do not degrade PFAS and mainly separate or concentrate them, overlapping heavily with content already covered via evidence in C01 and C02. It is merged into the broader class-wide limitation captured in G04 and into boundary constraint B01 rather than kept as a separate core claim. Disposition targets normalized from ['NQ26-G04'] to ['NQ26-B01', 'NQ26-G04'] using final source_atomic_claim_ids.

#### NQ26-C04

- Prior claim: A membrane-assisted degradation route is described in which PFAS are first adsorbed onto a membrane, to which catalysts may be added, and then degraded under light or an electric field, distinguishing this approach from purely separative membrane treatments.
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
- Final target(s): NQ26-B01, NQ26-G03, NQ26-G04
- Rationale: C06 asserted that adsorption onto membranes is a concentration step unless followed by degradation. The membrane-adsorption-as-first-step content is already covered in the description of membrane-assisted degradation in G03, while the non-destructive nature of such concentrating stages feeds into the class-wide limitation in G04 and boundary constraint B01. No additional distinct atomic claim was needed. Disposition targets normalized from ['NQ26-G03', 'NQ26-G04'] to ['NQ26-B01', 'NQ26-G03', 'NQ26-G04'] using final source_atomic_claim_ids.

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

- `NQ26-G01`: **supported**. Canonical proposition and material qualifiers (nanoporous high-pressure NF/RO, short/long-chain separation with high rejection, concentrated waste stream) are each entailed by the exact spans of MMG001 and MMG004. Full/partial/contradiction rules are executable and consistent with the proposition.
  Recommended change: None.
- `NQ26-G02`: **supported**. Filtration and membrane distillation 'can only concentrate PFAS' is directly stated in MMG002; forward osmosis's concentration-only classification is reasonably synthesized from MMG005's explicit concentration-vs-degradation categorization. Rules are executable.
  Recommended change: None.
- `NQ26-G03`: **supported**. Proposition and qualifiers (adsorption onto membrane, optional catalysts, light/electric-field degradation) match the MMG006 span exactly. This resolves the prior Model B concern that C06 conflated MMG002's generic 'adsorption' with membrane adsorption — G03 now relies only on MMG006 for this content.
  Recommended change: None.
- `NQ26-G04`: **supported**. Class-wide non-degradation limitation is directly supported by MMG003's explicit statement and corroborated by MMG002/MMG005's concentration-only framing. This appropriately consolidates the prior C03 redundancy flag into a single class-level group rather than a separate near-duplicate core claim.
  Recommended change: None.
- `NQ26-G05`: **supported**. This group now explicitly separates the already-demonstrated NF/RO tandem-with-destruction practice (MMG001) from the forward-looking research recommendation to combine filtration/membrane distillation/forward osmosis with degradation (MMG005), matching the prior Model B group review's recommended_change verbatim. The full_rule requires both the demonstrated/recommended aspects and forbids treating the recommendation as established practice.
  Recommended change: None — prior aspirational-treated-as-descriptive issue is resolved.
- `NQ26-G06`: **supported**. Directly supported by the MMG007 span; correctly scoped as optional/supplementary negative-finding content.
  Recommended change: None.
- `NQ26-G07`: **supported**. The proposition now explicitly notes 'the specific type of membrane process is not identified beyond being a membrane process,' resolving the earlier C05 conflation flag that had implied this evaporation/incineration pathway was specific to NF/RO.
  Recommended change: None.
- `NQ26-B01`: **supported**. Violation rule is executable (flags equating separation/retention with destruction) and directly reflects the must_not_claim boundary. Its evidence and proposition substantially overlap with G04, but since B01 is scoring_role constraint_only it is excluded from coverage and does not create double-counted required content — this is an acceptable design pattern, not a defect, though pipeline enforcement of the exclusion should be spot-checked.
  Recommended change: None required for approval; confirm at the scoring-pipeline level that constraint_only groups are excluded from the coverage denominator.
- `NQ26-B02`: **supported**. Correctly scoped as an absence-of-evidence boundary constraint (no electrodialysis/modified-membrane performance claims should be attributed to this evidence set). Violation rule is executable despite having no supporting evidence_ids, which is appropriate for a negative-scope constraint.
  Recommended change: None.

Human-review priorities:
- Confirm the scoring pipeline actually excludes constraint_only groups (B01, B02) from the coverage denominator despite B01's near-total evidence/proposition overlap with G04, to avoid inadvertent double-counting during automated grading.
- Spot-check that graders do not conflate the NF/RO-specific high-pressure filtration content in G01 with the generic 'filtration' evidence reused across G02/G04/G05, since MMG002 and MMG005 are cited in three separate core/optional groups.
- The G05 aspirational-vs-demonstrated conflation flagged in the prior Model B group review has been fully resolved in this revision — no further action needed, noted here only for audit continuity.

### Non-normative reference prose

The evidence describes several membrane-based routes for treating PFAS-contaminated water and distinguishes between those that mainly separate or concentrate PFAS and those that involve PFAS destruction.

High-pressure membrane filtration using nanoporous nanofiltration (NF) and reverse osmosis (RO) is presented as a traditional separation approach. These NF/RO systems are reported to be highly effective at separating both short- and long-chain PFAS from water, with typical rejection efficiencies above 90%, and they generate a concentrated PFAS waste stream rather than destroying the compounds. Because they only separate and concentrate PFAS, NF/RO have been demonstrated in tandem with separate destruction technologies.

More generally, membrane-related treatments such as filtration, membrane distillation, and forward osmosis are classified as concentration or separation routes. Review evidence states that these approaches can only concentrate PFAS and explicitly distinguishes them from degradation methods such as electrodegradation and biodegradation. This reflects a broader limitation of membrane-based processes as a class: they do not themselves degrade PFAS and function mainly to separate or concentrate the contaminants, so effective destruction requires an additional degradation step beyond the membrane stage.

As an example of how concentrating membrane routes are linked to destruction, NF/RO and other concentrating membrane processes are operated in combination with downstream destruction technologies. Recommended combinations also include pairing concentration treatments (filtration, membrane distillation, forward osmosis) with degradation processes (e.g., electrodegradation or biodegradation); in this case, the literature frames such combinations for filtration, membrane distillation, and forward osmosis as a direction for future research rather than as an already established practice.

In some membrane-process applications to PFAS-contaminated groundwater, the PFAS-rich concentrate is sent to an evaporation pool, and the resulting residue is collected and incinerated, with the incineration step providing destruction while the membrane serves only to concentrate the PFAS.

By contrast with purely separative uses of membranes, a distinct membrane-assisted degradation route is described. In this approach, PFAS are first adsorbed onto a membrane, to which catalysts may be added, and are then degraded under light or an applied electric field. Here, the membrane still acts as a concentrating interface but also serves as a platform that enables chemical degradation; PFAS transformation occurs only in this subsequent, stimulus-driven step rather than during simple membrane separation.

Low-pressure membrane processes such as microfiltration and ultrafiltration are noted to remove PFAS poorly and are therefore not regarded as effective routes for PFAS separation or concentration compared with high-pressure NF/RO and related concentrating membrane configurations.

Overall, the membrane-based treatment routes represented in the evidence fall into two categories: (i) pressure-driven and related membrane processes (including high-pressure NF/RO, general filtration, membrane distillation, and forward osmosis) that separate or concentrate PFAS but do not themselves degrade them and therefore require combination with external destruction technologies; and (ii) membrane-coupled destructive routes such as membrane-assisted degradation under light or electric fields, in which PFAS are first accumulated on a membrane and then chemically degraded. The evidence set does not provide specific separation performance data for dedicated electrical membrane separation processes (such as electrodialysis) or for modified or nanoengineered membranes beyond the high-pressure NF/RO context.

### Prose-to-ledger map

- High-pressure membrane filtration using nanoporous nanofiltration (NF) and reverse osmosis (RO) is presented as a traditional separation approach. -> NQ26-G01
- These NF/RO systems are reported to be highly effective at separating both short- and long-chain PFAS from water, with typical rejection efficiencies above 90%, and they generate a concentrated PFAS waste stream rather than destroying the compounds. -> NQ26-G01, NQ26-G04
- Because they only separate and concentrate PFAS, NF/RO have been demonstrated in tandem with separate destruction technologies. -> NQ26-G01, NQ26-G04, NQ26-G05
- More generally, membrane-related treatments such as filtration, membrane distillation, and forward osmosis are classified as concentration or separation routes. -> NQ26-G02, NQ26-G04
- Review evidence states that these approaches can only concentrate PFAS and explicitly distinguishes them from degradation methods such as electrodegradation and biodegradation. -> NQ26-G02, NQ26-G05
- This reflects a broader limitation of membrane-based processes as a class: they do not themselves degrade PFAS and function mainly to separate or concentrate the contaminants, so effective destruction requires an additional degradation step beyond the membrane stage. -> NQ26-G04, NQ26-B01
- As an example of how concentrating membrane routes are linked to destruction, NF/RO and other concentrating membrane processes are operated in combination with downstream destruction technologies. -> NQ26-G01, NQ26-G05
- Recommended combinations also include pairing concentration treatments (filtration, membrane distillation, forward osmosis) with degradation processes (e.g., electrodegradation or biodegradation); in this case, the literature frames such combinations for filtration, membrane distillation, and forward osmosis as a direction for future research rather than as an already established practice. -> NQ26-G02, NQ26-G05
- In some membrane-process applications to PFAS-contaminated groundwater, the PFAS-rich concentrate is sent to an evaporation pool, and the resulting residue is collected and incinerated, with the incineration step providing destruction while the membrane serves only to concentrate the PFAS. -> NQ26-G07, NQ26-G04, NQ26-B01
- By contrast with purely separative uses of membranes, a distinct membrane-assisted degradation route is described. -> NQ26-G03, NQ26-G04
- In this approach, PFAS are first adsorbed onto a membrane, to which catalysts may be added, and are then degraded under light or an applied electric field. -> NQ26-G03
- Here, the membrane still acts as a concentrating interface but also serves as a platform that enables chemical degradation; PFAS transformation occurs only in this subsequent, stimulus-driven step rather than during simple membrane separation. -> NQ26-G03, NQ26-G04, NQ26-B01
- Low-pressure membrane processes such as microfiltration and ultrafiltration are noted to remove PFAS poorly and are therefore not regarded as effective routes for PFAS separation or concentration compared with high-pressure NF/RO and related concentrating membrane configurations. -> NQ26-G06
- Overall, the membrane-based treatment routes represented in the evidence fall into two categories: (i) pressure-driven and related membrane processes (including high-pressure NF/RO, general filtration, membrane distillation, and forward osmosis) that separate or concentrate PFAS but do not themselves degrade them and therefore require combination with external destruction technologies; and (ii) membrane-coupled destructive routes such as membrane-assisted degradation under light or electric fields, in which PFAS are first accumulated on a membrane and then chemically degraded. -> NQ26-G01, NQ26-G02, NQ26-G03, NQ26-G04, NQ26-G05, NQ26-B01
- The evidence set does not provide specific separation performance data for dedicated electrical membrane separation processes (such as electrodialysis) or for modified or nanoengineered membranes beyond the high-pressure NF/RO context. -> NQ26-B02

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
> Results and discussion To demonstrate that the engineered GAP system is an effec- tive treatment system for PFAS contaminated water the disap- pearance of the target analyte Ĳs), formation of degradation products, defluorination, and energy costs were measured and calculated.

**WF10_002_MMG002** (optional_gold; `2024 - Shaji - Investigating the Effects of Gliding Arc Plasma Discharge’s Thermal Characteristic and Reactive Chemistry on Aqueous PFOS Mineralization.pdf`, chunk `8`)
> Non-plasma-based PFAS treatment technolo- gies where high temperature make an important contribution to PFAS degradation, such as sonolysis [23,27] and supercritical water oxidation (SCWO) [6], have shown excellent potential in mineralizing PFAS with minimal short-chain PFAS formation, and increased mineralization with a rise in reaction temperatures has been observed in SCWO [ 6,28].

### Normative content claim groups

#### WF10_002-G01

- Component: `WF10_002-T01`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: In the reported gliding arc plasma PFAS treatment system, disappearance of the target analyte(s), formation of degradation products, defluorination, and energy costs are measured as distinct endpoints.
- Material qualifiers: ["These endpoints are all measured for PFAS-contaminated water treated by an engineered gliding arc plasma system.", "These four quantities are each measured and calculated as separate metrics for the same GAP treatment system."]
- Evidence: WF10_002_MMG001
- Prior atomic claims: WF10_002-C01, WF10_002-S01
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
- Function: `limitation`
- Scoring role: `required_content`
- Proposition: The supplied evidence does not report membrane-filtration experiments or separation/adsorption endpoints for PFAS, so membrane-specific separation and adsorption remain conceptually distinct but unquantified endpoint categories in this record set.
- Material qualifiers: ["No separation or adsorption endpoints are described in the cited records.", "Separation and adsorption should still be recognized as distinct endpoint categories for membrane filtration, but they cannot be empirically characterized from the supplied evidence."]
- Evidence: WF10_002_MMG001
- Prior atomic claims: WF10_002-L01
- Full: Full credit if the answer explicitly notes that the supplied evidence set does not include membrane-filtration PFAS studies or separation/adsorption endpoints, and therefore membrane separation/adsorption must be treated as conceptually distinct but are not empirically defined here.
- Partial: Partial credit if the answer correctly indicates that membrane-specific endpoints (e.g., separation or adsorption) are not described in the provided evidence, but does not explicitly frame them as conceptually distinct endpoint categories.
- Contradiction: Mark as contradicted if the answer claims that the supplied evidence includes specific membrane-filtration separation or adsorption data, or otherwise fabricates membrane-filtration endpoints as if they were reported in the cited records.

#### WF10_002-G04

- Component: `WF10_002-T02`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: For gliding arc plasma PFAS treatment, disappearance of the parent PFAS, formation of degradation products, and defluorination are distinct chemical endpoints that must be considered together; examining only one is insufficient to determine whether PFAS are destroyed rather than merely altered.
- Material qualifiers: ["These chemical endpoints are measured separately in the GAP system (e.g., parent PFAS and degradation products by analytical methods, defluorination as fluoride release).", "Examining a single measurement among these is insufficient; the endpoints must be co-aligned to assess whether PFAS have been destroyed or only altered, so they cannot be treated as interchangeable or collapsed into one in the GAP context."]
- Evidence: WF10_002_MMG001
- Prior atomic claims: WF10_002-C02, WF10_002-C03
- Full: Full credit if the answer explains that, in the GAP system, disappearance/removal of the parent PFAS, degradation-product formation, and defluorination are separate measured endpoints and that no single one of these is sufficient to conclude PFAS destruction; instead, they must be considered together, so removal, degradation, and defluorination cannot be treated as interchangeable.
- Partial: Partial credit if the answer correctly states that at least two of these GAP endpoints (e.g., disappearance and defluorination) are distinct and that one alone is insufficient to infer destruction, but omits explicit mention of all three or the destruction-versus-alteration interpretive qualifier.
- Contradiction: Mark as contradicted if the answer claims that disappearance alone (or any single one of disappearance, degradation-product formation, or defluorination) is sufficient to demonstrate PFAS destruction in GAP, or otherwise treats these endpoints as interchangeable rather than distinct.

#### WF10_002-G05

- Component: `WF10_002-T02`
- Importance: `core`
- Function: `affirmative`
- Scoring role: `required_content`
- Proposition: When comparing gliding arc plasma and supercritical water oxidation, mineralization endpoints reported for SCWO in the literature should not be conflated with the disappearance, degradation-product formation, or defluorination endpoints reported for the GAP system, because they are different specific measurements and outcome categories.
- Material qualifiers: ["The GAP study reports disappearance/removal of parent PFAS, degradation-product formation, and defluorination (plus energy cost).", "The SCWO literature cited in the supplied evidence focuses on PFAS mineralization with minimal short-chain PFAS formation and increasing mineralization with temperature.", "Therefore, mineralization, removal/disappearance, defluorination, and byproduct formation are distinct endpoint categories that must not be treated as interchangeable across these technologies."]
- Evidence: WF10_002_MMG001, WF10_002_MMG002
- Prior atomic claims: WF10_002-C05
- Full: Full credit if the answer states that mineralization in SCWO is a different endpoint from disappearance/removal, degradation-product formation, and defluorination measured for GAP, and explicitly notes that these endpoint types must not be treated as interchangeable when comparing technologies.
- Partial: Partial credit if the answer correctly notes that SCWO mineralization is a distinct endpoint from at least one of the GAP endpoints (e.g., disappearance or defluorination) but does not clearly generalize this to a broader non-conflation rule across all listed endpoint categories.
- Contradiction: Mark as contradicted if the answer states or implies that mineralization in SCWO is equivalent to, or can be directly substituted for, GAP disappearance/removal, degradation-product formation, or defluorination endpoints, without qualification.

#### WF10_002-G06

- Component: `WF10_002-T02`
- Importance: `core`
- Function: `limitation`
- Scoring role: `required_content`
- Proposition: In the supplied records, overall PFAS destruction or fate is not a single measured endpoint but an interpretation that integrates distinct measurements such as removal/disappearance, degradation-product formation, and defluorination, so destruction and mass balance must be kept conceptually separate from individual endpoints like removal, degradation, defluorination, mineralization, byproduct formation, and energy use.
- Material qualifiers: ["In the GAP study, disappearance of the target analyte(s), degradation-product formation, and defluorination are all measured separately, and examining a single measurement is noted as insufficient to distinguish destruction from mere alteration.", "By extension, destruction and mass-balance interpretations should not be treated as interchangeable with any one individual endpoint such as removal, separation, degradation, defluorination, mineralization, byproduct formation, or energy use."]
- Evidence: WF10_002_MMG001
- Prior atomic claims: WF10_002-C06, WF10_002-L02
- Full: Full credit if the answer explains that destruction or overall fate of PFAS is inferred by integrating multiple endpoints (rather than any single measurement) and explicitly states that destruction/mass balance is conceptually distinct from and not interchangeable with individual endpoints such as removal, separation, degradation, defluorination, mineralization, byproduct formation, or energy use.
- Partial: Partial credit if the answer correctly indicates that destruction requires consideration of multiple endpoints and is not captured by a single measurement, but does not clearly list or connect this to the broader set of endpoint types specified in the task boundary.
- Contradiction: Mark as contradicted if the answer claims that destruction or mass balance is directly and fully represented by just one endpoint (e.g., by disappearance/removal alone, mineralization alone, or defluorination alone) without acknowledging the need for multiple, distinct measurements.


### Prior atomic-claim dispositions

#### WF10_002-C01

- Prior claim: In the reported gliding arc plasma PFAS treatment system, disappearance of the target analyte(s), formation of degradation products, defluorination, and energy costs are measured as distinct endpoints rather than being collapsed into a single destruction metric.
- Action: `merged`
- Final target(s): WF10_002-G01
- Rationale: C01 describes the four GAP endpoints and their treatment as distinct rather than a single destruction metric; the distinct endpoint listing is fully captured in G01.

#### WF10_002-C02

- Prior claim: For the GAP system, disappearance of the parent PFAS (a removal-type endpoint) must be distinguished from formation of degradation products (a degradation/byproduct-formation endpoint), because the study states that multiple measurements must be co-aligned to demonstrate PFAS destruction versus mere alteration.
- Action: `mapped`
- Final target(s): WF10_002-G04
- Rationale: C02 emphasizes distinguishing disappearance from degradation products and the need to co-align multiple measurements; this non-interchangeability and co-consideration of GAP chemical endpoints is the focus of G04.

#### WF10_002-C03

- Prior claim: Defluorination in the GAP study is treated as an endpoint separate from both target-analyte disappearance and degradation-product formation, and all three chemical endpoints must be considered together to assess whether PFAS are destroyed.
- Action: `mapped`
- Final target(s): WF10_002-G04
- Rationale: C03 focuses on defluorination as separate from disappearance and degradation products and the need to consider all three; G04 encodes this distinction and the requirement to evaluate these GAP endpoints together.

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
- Action: `mapped`
- Final target(s): WF10_002-G03
- Rationale: L01 notes the absence of separation/adsorption and membrane-filtration endpoints in the supplied evidence and frames them as distinct but unquantified; G03 formalizes this limitation for T01.

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

- `WF10_002-G01`: **supported**. Canonical proposition and both material qualifiers (co-measurement on the same engineered system, four distinct metrics) are directly entailed by the MMG001 span. C01 and S01 are correctly merged here without loss of content.
  Recommended change: None.
- `WF10_002-G02`: **supported**. Mineralization-as-endpoint, minimal short-chain byproduct qualifier, and temperature dependence are all entailed by the MMG002 span. Canonical proposition avoids over-claiming this is a dedicated SCWO primary study, addressing the prior caution about secondary-citation framing.
  Recommended change: None.
- `WF10_002-G03`: **supported**. This is an absence/limitation claim; the cited MMG001 span does not itself entail 'no membrane data exists' but the underlying support is the demonstrated silence of the full supplied gold set on membrane filtration, which prior Model B review already evaluated and approved as correct handling of a true coverage gap rather than fabrication. No new defect introduced in this revision.
  Recommended change: None; retain as-is given the structural nature of negative-evidence claims.
- `WF10_002-G04`: **supported**. Non-interchangeability of disappearance/degradation-products/defluorination and the co-alignment requirement are entailed by the MMG001 span. Correctly consolidates C02 and C03 without duplicating G01's simple endpoint-listing content, since this group targets T02's 'why non-interchangeable' framing rather than T01's 'identify' framing.
  Recommended change: None.
- `WF10_002-G05`: **supported**. Cross-technology non-conflation claim is jointly entailed by both spans (GAP endpoints in MMG001, SCWO mineralization in MMG002). Independently answerable from G02/G04 since it targets the comparison itself rather than either technology's endpoints in isolation.
  Recommended change: None.
- `WF10_002-G06`: **supported**. Correctly relies only on MMG001, consistent with the prior review's correction that this group does not depend on MMG002. Destruction-as-interpretation-not-single-endpoint is a reasonable synthesis of the span's 'examining a single measurement insufficient' logic; not duplicative of G04 since it addresses the destruction/mass-balance abstraction rather than the GAP chemical endpoints themselves.
  Recommended change: None.
- `WF10_002-B01`: **supported**. Correctly scoped as constraint_only and excluded from coverage denominator. Violation rule is executable (checks for generalization of GAP/SCWO condition-specific results to all technologies/conditions) and consistent with the must_not_claim boundary.
  Recommended change: None.

Human-review priorities:
- The prior duplicate_or_weighting_issue about MMG002 (optional_gold) anchoring core groups G02 and (jointly) G05 is now addressed by an explicit documented rationale in answerability_rationale and boundary_check.notes stating the elevation is intentional because mineralization is named in the task boundary and only this record documents it; combined with the blanket project-author retention of both gold records, this is an adequate documented resolution, but a project author may still wish to formally confirm the elevation rather than rely on ledger self-justification.
- Confirm no membrane-filtration gold evidence exists elsewhere for this question, since G03 and constraint B01 both depend on this coverage gap being genuine rather than a retrieval omission (carried over from two prior reviews).
- The reference_answer prose sentence 'mineralization and short-chain byproduct formation are reported as separate outcome categories' is a mild interpretive gloss beyond the literal MMG002 span; reasonable synthesis for an endpoint-distinction task, not a blocking prose defect, but worth a light author read-through.
- reference_answer_claim_map maps several compound summary sentences to multiple claim groups (G04+G05+G06, G04+G06, G02+G05); the underlying groups are non-duplicative and independently scorable, but confirm the automated scorer does not double-count shared sentence text as separate coverage evidence for multiple groups.

### Non-normative reference prose

In the gliding arc plasma (GAP) study of PFAS-contaminated water, the authors explicitly measure four separate endpoints: disappearance of the target analyte(s), formation of degradation products, defluorination, and energy cost. These quantities are each measured and calculated as distinct metrics for the same engineered GAP system.

Within those GAP measurements, disappearance of the parent PFAS, formation of non-parent degradation products, and defluorination are treated as distinct chemical endpoints. The study indicates that examining any one of these metrics in isolation is insufficient to conclude that PFAS have been destroyed rather than merely altered, so these removal, degradation, and defluorination measurements must be considered together and not treated as interchangeable.

For supercritical water oxidation (SCWO), the cited discussion reports PFAS mineralization as a distinct endpoint. SCWO is described as having excellent potential for mineralizing PFAS with minimal formation of short-chain PFAS byproducts, and increased mineralization is observed as reaction temperature rises. In this context, mineralization and short-chain byproduct formation are reported as separate outcome categories, with short-chain PFAS formation characterized as minimal alongside mineralization.

The supplied records do not include any membrane-filtration experiments or explicit separation or adsorption endpoints. Thus, while separation and adsorption are conceptually important endpoint categories for membrane systems, they cannot be empirically described from the provided evidence and must be acknowledged as distinct but unquantified in this reference.

Taken together, the GAP and SCWO evidence show why removal/disappearance, degradation, defluorination, mineralization, byproduct formation, and overall destruction or mass balance cannot be treated as interchangeable endpoints. In GAP, disappearance of the parent PFAS, degradation-product formation, and defluorination are measured separately and must be co-aligned to infer whether PFAS have been destroyed or only altered; no single metric is sufficient on its own. For SCWO, mineralization is the primary reported endpoint, with minimal short-chain PFAS formation and a clear dependence on temperature. When comparing GAP and SCWO, mineralization endpoints reported for SCWO in the literature should not be conflated with GAP endpoints such as disappearance/removal, degradation-product formation, or defluorination, because they represent different specific measurements and outcome categories.

More broadly, any judgment about PFAS destruction or mass balance in these systems is not a directly measured, standalone endpoint but an interpretation derived from several distinct measurements. Destruction, therefore, must remain conceptually separate from individual endpoints such as removal, separation, degradation, defluorination, mineralization, byproduct formation, and operational metrics like energy use, even though it is informed by them.

### Prose-to-ledger map

- In the gliding arc plasma (GAP) study of PFAS-contaminated water, the authors explicitly measure four separate endpoints: disappearance of the target analyte(s), formation of degradation products, defluorination, and energy cost. -> WF10_002-G01
- These quantities are each measured and calculated as distinct metrics for the same engineered GAP system. -> WF10_002-G01
- Within those GAP measurements, disappearance of the parent PFAS, formation of non-parent degradation products, and defluorination are treated as distinct chemical endpoints. -> WF10_002-G04
- The study indicates that examining any one of these metrics in isolation is insufficient to conclude that PFAS have been destroyed rather than merely altered, so these removal, degradation, and defluorination measurements must be considered together and not treated as interchangeable. -> WF10_002-G04
- For supercritical water oxidation (SCWO), the cited discussion reports PFAS mineralization as a distinct endpoint. -> WF10_002-G02
- SCWO is described as having excellent potential for mineralizing PFAS with minimal formation of short-chain PFAS byproducts, and increased mineralization is observed as reaction temperature rises. -> WF10_002-G02
- In this context, mineralization and short-chain byproduct formation are reported as separate outcome categories, with short-chain PFAS formation characterized as minimal alongside mineralization. -> WF10_002-G02, WF10_002-G05
- The supplied records do not include any membrane-filtration experiments or explicit separation or adsorption endpoints. -> WF10_002-G03
- Thus, while separation and adsorption are conceptually important endpoint categories for membrane systems, they cannot be empirically described from the provided evidence and must be acknowledged as distinct but unquantified in this reference. -> WF10_002-G03
- Taken together, the GAP and SCWO evidence show why removal/disappearance, degradation, defluorination, mineralization, byproduct formation, and overall destruction or mass balance cannot be treated as interchangeable endpoints. -> WF10_002-G04, WF10_002-G05, WF10_002-G06
- In GAP, disappearance of the parent PFAS, degradation-product formation, and defluorination are measured separately and must be co-aligned to infer whether PFAS have been destroyed or only altered; no single metric is sufficient on its own. -> WF10_002-G04, WF10_002-G06
- For SCWO, mineralization is the primary reported endpoint, with minimal short-chain PFAS formation and a clear dependence on temperature. -> WF10_002-G02
- When comparing GAP and SCWO, mineralization endpoints reported for SCWO in the literature should not be conflated with GAP endpoints such as disappearance/removal, degradation-product formation, or defluorination, because they represent different specific measurements and outcome categories. -> WF10_002-G05
- More broadly, any judgment about PFAS destruction or mass balance in these systems is not a directly measured, standalone endpoint but an interpretation derived from several distinct measurements. -> WF10_002-G06
- Destruction, therefore, must remain conceptually separate from individual endpoints such as removal, separation, degradation, defluorination, mineralization, byproduct formation, and operational metrics like energy use, even though it is informed by them. -> WF10_002-G06

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
> How - ever, the extent of this impact varies depending on the type and concentration of OM, with some studies indicating min- imal interference at environmentally relevant OM concen - trations, while others report substantial reductions in PFAS sorption, highlighting the need for further research on opti - mizing biochar performance under diverse water matrices.

**WF10_021_MMG002** (negative_gold; `2024 - Liang - A critical review of biochar for the remediation of PFAS-contaminated soil and water.pdf`, chunk `48`)
> However, biochar regeneration faces sig- nificant challenges as this simply has not been attempted frequently enough in the past to draw definitive conclusions on efficacy.

**WF10_021_MMG003** (negative_gold; `2026 - Sadmani - A critical review of the application of biochar in removing perfluoroalkyl and polyfluoroalkyl substances (PFAS) from water matrices.pdf`, chunk `68`)
> Sustainable regeneration and reusability of biochar Bio- char regeneration is crucial for reducing costs, but each regeneration cycle alters its characteristics, such as surface morphology, functionalities, and porosity, necessitating thorough investigation.

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
- Importance: `supplementary`
- Function: `limitation`
- Scoring role: `optional_content`
- Proposition: In the provided evidence set, matrix and regeneration limitations are documented for biochar used to remove PFAS from water matrices, but analogous limitations for activated carbon are not established.
- Material qualifiers: ["scope is restricted to the supplied evidence records", "the documented limitations pertain to biochar used for PFAS removal from water matrices", "no activated-carbon–specific matrix or regeneration gaps are characterized in the provided evidence"]
- Evidence: WF10_021_MMG001, WF10_021_MMG002, WF10_021_MMG003
- Prior atomic claims: WF10_021-C05
- Full: Because this is optional content, full-credit logic for this group is not applied to the overall score. Within this group, it is satisfied if the answer explicitly notes that the described matrix and regeneration gaps are documented for biochar and that the provided evidence does not characterize comparable gaps for activated carbon.
- Partial: Not applicable, as this group is optional_content and is not required for full credit on any task component.
- Contradiction: Within this group, it would be contradicted if the answer claims that the provided evidence establishes specific matrix or regeneration gaps for activated carbon; however, such a statement is primarily governed by the boundary-constraint group WF10_021-B01.


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
- Final target(s): WF10_021-G04, WF10_021-B01
- Rationale: C05 provides a scope clarification that the documented limitations apply to biochar and are not established for activated carbon. This is represented as an optional scope/limitation claim (G04) and as a boundary constraint (B01) to enforce the must_not_claim rule. No new scientific content beyond the evidence and the absence of activated-carbon data is introduced.

### Constraint-only groups

- `WF10_021-B01`: Do not generalize the biochar-specific matrix and regeneration limitations in the provided evidence into universal PFAS treatment claims or into specific claims about activated carbon.
  Violation rule: Flag a boundary violation if the answer (1) presents the biochar-specific limitations as if they apply universally to all PFAS treatment technologies, or (2) explicitly states that the provided evidence demonstrates specific matrix or regeneration gaps for activated carbon, or (3) claims broad PFAS treatment efficacy without acknowledging the biochar- and condition-specific nature of the findings.

### Model B verification

Overall verdict: **approve**

- `WF10_021-G01`: **supported**. Canonical proposition and all material qualifiers (sorbent=biochar, endpoint=PFAS sorption, matrix=diverse water matrices with varying OM, need for further research) are directly entailed by the exact evidence span. The prior interpretive 'per-study screening gap' extension from C02 was correctly removed; C01/C02 redundancy was resolved via merge, addressing the prior Model B review's two flagged issues.
  Recommended change: None.
- `WF10_021-G02`: **supported**. Canonical proposition is a near-verbatim restatement of the exact evidence span, correctly scoped to biochar and PFAS remediation at the field/literature level. The prior flagged 'per-study screening rule' inference from C03 was removed in this revision.
  Recommended change: None.
- `WF10_021-G03`: **supported**. Canonical proposition, including the three named properties (surface morphology, functionalities, porosity) and the need for thorough investigation, is directly entailed by the exact evidence span. C04 required no changes and was mapped unchanged.
  Recommended change: None.
- `WF10_021-G04`: **supported**. Correctly marked optional_content/supplementary so it adds no required-content coverage weight alongside its B01 constraint counterpart (both trace to C05). The scope-limitation claim is a defensible synthesis from the absence of activated-carbon evidence in this record set, clearly labeled as evidence-set-relative rather than a definitive claim about activated carbon.
  Recommended change: None required; project author may wish to confirm comfort with the evidence-set-relative framing given the question names activated carbon explicitly (already logged as a human-review item, not a defect).
- `WF10_021-B01`: **supported**. Violation rule is executable and directly operationalizes the must_not_claim boundary: universalizing biochar findings to all PFAS treatment, or asserting the evidence characterizes activated-carbon-specific gaps. Correctly excluded from coverage scoring (constraint_only).
  Recommended change: None.

Human-review priorities:
- The prior Model B group review flagged T02's wording as containing an ungrounded 'secondary-waste' phrase; that phrase is not present in the task_components supplied in this packet (either frozen or in the revised ledger), so the concern appears already resolved or was based on a different snapshot — confirm the live ledger matches what is shown here before closing that item.
- Confirm the project author is comfortable with G04/B01 representing the activated-carbon scope-limitation as an evidence-set-relative absence rather than a definitive claim about activated carbon, given the question explicitly names activated carbon (carried over from prior review, still a judgment call rather than a defect).
- The ledger's top-level 'answerability: partially_supported' field describes evidentiary completeness relative to the full two-sorbent question, while the frozen question's 'answerability_type' is 'answerable' — these serve different purposes (evidence-completeness note vs. frozen task classification) and are not in conflict, but reviewers should be aware both fields exist with different semantics.

### Non-normative reference prose

From the supplied evidence, the documented matrix and regeneration gaps for PFAS adsorption studies concern biochar used for PFAS removal from water matrices.

On the matrix side, existing work on biochar shows that organic matter in the water can affect PFAS sorption in highly variable ways: some studies report minimal interference at environmentally relevant organic-matter concentrations, whereas others find substantial reductions in PFAS sorption. This variability indicates that biochar performance across diverse water matrices, and under different organic-matter types and concentrations, remains uncertain and requires further research to optimize.

On the regeneration and reusability side, the literature indicates that regeneration of biochar for PFAS remediation has not been attempted frequently enough to draw definitive conclusions about how effective regeneration is. In addition, each regeneration cycle can alter important biochar characteristics, including surface morphology, surface functionalities, and porosity, so these regeneration-induced changes need thorough investigation when assessing sustainable regeneration and long-term reusability for PFAS removal.

These documented limitations are specific to biochar in the provided records. The evidence does not characterize analogous matrix or regeneration gaps for activated carbon, and the biochar-specific findings should not be generalized into universal PFAS treatment claims.

### Prose-to-ledger map

- From the supplied evidence, the documented matrix and regeneration gaps for PFAS adsorption studies concern biochar used for PFAS removal from water matrices. -> WF10_021-G01, WF10_021-G02, WF10_021-G03, WF10_021-G04
- On the matrix side, existing work on biochar shows that organic matter in the water can affect PFAS sorption in highly variable ways: some studies report minimal interference at environmentally relevant organic-matter concentrations, whereas others find substantial reductions in PFAS sorption. -> WF10_021-G01
- This variability indicates that biochar performance across diverse water matrices, and under different organic-matter types and concentrations, remains uncertain and requires further research to optimize. -> WF10_021-G01
- On the regeneration and reusability side, the literature indicates that regeneration of biochar for PFAS remediation has not been attempted frequently enough to draw definitive conclusions about how effective regeneration is. -> WF10_021-G02
- In addition, each regeneration cycle can alter important biochar characteristics, including surface morphology, surface functionalities, and porosity, so these regeneration-induced changes need thorough investigation when assessing sustainable regeneration and long-term reusability for PFAS removal. -> WF10_021-G03
- These documented limitations are specific to biochar in the provided records. -> WF10_021-G04
- The evidence does not characterize analogous matrix or regeneration gaps for activated carbon, and the biochar-specific findings should not be generalized into universal PFAS treatment claims. -> WF10_021-G04, WF10_021-B01

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
> Approximately 80% and 90% equilibria were accomplished within 60 and 120 min for the long chain carbon PFAS, respectively, while for the short chain PFAS, 240 min was required to reach 85% equilibrium.

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

- `WF10_025-G01`: **supported**. Canonical proposition and all material qualifiers (matrix, adsorbent, ~80% at ~60 min, ~90% at ~120 min, fraction-not-full-equilibrium) are directly entailed by the exact_evidence_span. Numeric equivalents are claim-specific (60/120/80%/90% only, no cross-contamination with the short-chain 240/85% values). Full/partial/contradiction rules are executable and consistent with the proposition.
  Recommended change: None.
- `WF10_025-G02`: **supported**. Directly restates the short-chain PFAS kinetics from the same sentence; numeric equivalents (240 min/4 hours, 85%) are correctly scoped to this group only. Rules correctly flag a swap with long-chain kinetics as contradiction.
  Recommended change: None.
- `WF10_025-G03`: **supported**. This is the one synthesized/inferential group (synthesis_required=true), directly responsive to the protocol_extraction question ('how should contact time be planned'). The prior-round concern that this inference was labeled 'core' without acknowledging its inferential nature is now resolved: the full_rule explicitly requires the answer to acknowledge the recommendation is an inference from the reported kinetics rather than a directly stated protocol instruction, and material_qualifiers state this explicitly. Retaining 'core'/'required_content' is defensible given the question directly asks for planning guidance that only this group provides.
  Recommended change: None required; project-author may still confirm comfort with scoring an inferential synthesis as core required content (see human_review_priorities).
- `WF10_025-G04`: **supported**. Resolves the carried-over issue from the prior Model B group review. The previous version's full_rule/material_qualifiers required PAC-dose, rate-constant, and other-matrix content sourced only from the gold record's does_not_support metadata field rather than the exact_evidence_span. In this revision, that dose/rate-constant-specific language has been removed from G04's full_rule and material_qualifiers; the group now only requires (a) recognizing the reported percentages as approximate fractions of equilibrium rather than full equilibrium (entailed by the span's 'Approximately') and (b) not treating the resulting contact times as guaranteed complete-equilibrium or broadly generalizable values (a reasonable, non-overreaching extrapolation from a single-matrix study). The specific PAC-dose/rate-constant/other-matrix content has been relocated to the non-scored unresolved_or_unsupported list, eliminating the metadata-vs-exact-span conflation.
  Recommended change: None; carry-forward issue is resolved.
- `WF10_025-B01`: **supported**. Correctly excluded from the coverage denominator (scoring_role: constraint_only) with an executable violation_rule. The prior-round attribution concern (dose/treatment-configuration language sourced only from gold metadata) is resolved: the canonical_proposition and violation_rule no longer reference PAC dose or configuration specifics, and instead mirror the frozen task_boundaries.must_not_claim clause directly ('Do not convert a condition-specific finding into a universal PFAS treatment claim'), which is itself a valid, independent normative source for a boundary constraint rather than requiring literal entailment from the evidence span.
  Recommended change: None.

Human-review priorities:
- Both carry-forward attribution concerns from the prior Model B group review (G04 and B01 relying on gold metadata fields like does_not_support rather than the literal exact_evidence_span for dose/rate-constant/matrix content) have been resolved in this revision by removing that content from the scored full/partial rules and relocating it to the non-scored unresolved_or_unsupported list — no further action needed unless the project author wants those limitations reinstated as scored content.
- Confirm final sign-off that G03's core/required_content classification is acceptable given it is a synthesized/inferential recommendation (synthesis_required=true) rather than a directly stated finding; the ledger now explicitly requires the answer to flag this inference status in the full_rule, which is judged sufficient here but remains a judgment call for the project author given the sparse single-record gold set for a protocol_extraction task.
- G04 (required_content, limitation) and B01 (constraint_only) still address overlapping non-generalization content; this is acceptable since B01 is excluded from the coverage denominator and each scores independently, but the project author may wish to confirm no double-counted weight is perceived downstream.

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
> Trifluoroacetic acid (TFA) was found to be the most recalcitrant intermediate product in the effluent, persisting at T = 600 ◦ C and residence time of ~ 32 s, emphasizing the need for TFA monitoring in SCWO treatment of PFAS-impacted matrices.

**WF10_030_MMG002** (required_gold; `2021 - Pinkard - Destruction of perfluorooctanesulfonate (PFOS) in a batch supercritical water oxidation reactor.pdf`, chunk `1`)
> However, a low fluorine mass balance at temperatures of 425 and 450 ◦ C may indicate the ex - istence of fluorinated species in the gaseous and/or liquid product which are not detected by targeted analysis.

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
> The removal efficiency of long- chain PFAS is higher than that of short-chain PFAS across all sorbents (Fig.

**WF10_004a_MMG002** (required_gold; `2025 - Kebede - Adsorptive Removal of PFAS from Aqueous Solutions Using GAC, PAC and Ball-Milled Colloidal Activated Carbon - Characterizing Efficiency, Kinetics,.pdf`, chunk `18`)
> The removal efficiency of PFOA (73% ± 24%) and PFOS (89% ± 35%) is higher than that of PFBA (30% ± 11%) and PFBS (55% ± 18%) in all three adsorbents (Figure 3a), as long-chain PFAS are more adsorbed on carbonaceous-based adsorbents than short-chain PFAS.

**WF10_004a_MMG003** (optional_gold; `2023 - Smaili - Adsorption as a remediation technology for short-chain per- and polyfluoroalkyl substances (PFAS) from water - a critical review.pdf`, chunk `29`)
> Compared to the removal of long-chain PFAS, e.g., 98.8% for PFOS and 87.6% for PFOA, the overall removal efficiency of short-chain PFAS is much lower than that of long-chain PFAS, highlighting once again the challenges of the removal of these short-chain substances from aqueous solutions because of their low hydrophobicity.

**WF10_004a_MMG004** (optional_gold; `2026 - Sadmani - A critical review of the application of biochar in removing perfluoroalkyl and polyfluoroalkyl substances (PFAS) from water matrices.pdf`, chunk `37`)
> longer-chain PFAS are more hydrophobic and less water-soluble, leading to higher adsorption capacities onto adsorbents [ 67, 68, 82, 89, 90].

**WF10_004a_MMG005** (optional_gold; `2025 - Hamza - Understanding PFAS Adsorption - How Molecular Structure Affects Sustainable Water Treatment.pdf`, chunk `21`)
> Long-chain PFASs can interact via hydrophobic tails through hydrophobic interactions, and the chain length and orientation of PFAS molecules signif- icantly influence the adsorption process.

**WF10_004a_MMG006** (negative_gold; `2022 - Vu - Recent progress in adsorptive removal of per- and poly-fluoroalkyl substances (PFAS) from water-wastewater.pdf`, chunk `63`)
> length, carboxylic/sulfonic groups, branched/linear structure and adsorb- ents’ ages on PFAS removal, although there are some agreement to certain extent (e.g., removal efficiencies are often better for long-chained, carbox- ylic, and linear PFAS), many other factors that can influence the large-scale removal efficiencies remain largely unknown (e.g., effects of water/waste- water organic and inorganic content) and contradictory results are often reported for different water/wastewater, adsorbents, and experimental con- ditions, which warrants further investigation.

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
> from landfill leachate within seven hours of operation, with 98.3 % of perfluorosulfonic acids (PFSA) and 85.5 % of perfluorocarboxylic acids (PFCA) removed from the leachate.

**WF10_004b_MMG002** (negative_gold; `2025 - Meng - Complete Aqueous Defluorination of GenX Hexafluoropropylene Oxide Dimer Acid Anion by Pulsed.pdf`, chunk `14`)
> [41] This indicates that the chemical identity of the PFAS headgroup did not govern the PFAS adsorption at laser-made [Ni 0.75 Fe 0.25 ]-(OH) 2 –hydrophilic carbon fiber paper anodes, but that anode characteristics, i.

**WF10_004b_MMG003** (required_gold; `2021 - Liu - Pilot-scale field demonstration of a hybrid nanofiltration and UV-sulfite treatment train for groundwater contaminated by per- and polyfluoroalkyl.pdf`, chunk `17`)
> Because FHxSA is likely neutral at pH 7.3 ( Nguyen et al., 2020 ) due to the sulfonamide headgroup, rejection by NF was consistently lower than the anionic analogue, PFHxS, attributed to the lack of an electrostatic repulsion rejection mechanism for this compound ( Fig.

**WF10_004b_MMG004** (required_gold; `2023 - Lauwers - Adsorption of PFAS by All-Silica Zeolite β - Insights into the Effect of the Water Matrix, Regeneration of the Material, and Continuous PFAS.pdf`, chunk `34`)
> The adsorption capacity and affinity of the zeolite β are lower for the sulfonic acids than for the carboxylic acids, which is due to the more polar nature of the sulfonic moiety and the unlikely formation of sulfonic acid dimers.

**WF10_004b_MMG005** (optional_gold; `2023 - Wang - Removing per- and polyfluoroalkyl substances (PFAS) in water by foam fractionation.pdf`, chunk `36`)
> For example, the removal of PFHeA (55%, overall) was much less than that of PFHeS (96%, overall), and PFHxA was removed Y.

**WF10_004b_MMG006** (optional_gold; `2026 - Sadmani - A critical review of the application of biochar in removing perfluoroalkyl and polyfluoroalkyl substances (PFAS) from water matrices.pdf`, chunk `31`)
> Batch tests revealed that perfluorosulfonic acids (PFSAs) were more efficiently removed, with up to 94% removal, compared to perfluorocarboxylic acids (PFCAs), which showed up to 60% removal when using either ZVI or ZVI + BC.

**WF10_004b_MMG007** (optional_gold; `2025 - Uwayezu - Efficient removal of PFAS in groundwater and landfill leachate using iron-modified peat residues and electrochemical oxidation.pdf`, chunk `19`)
> Similar to the behavior observed in batch mode, the column treatment demon - strated higher retention of sulfonate PFAS than carboxylate ones with equal perfluorocarbon chain lengths (e.g., 84 % PFOS versus 72 % PFNA removal, or 64 % PFHxS versus 44 % PFHpA), likely due to the greater effect of the sulfonate functional group.

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
- Proposition: In pulsed electrolysis using laser-made [Ni0.75Fe0.25]-(OH)2–hydrophilic carbon fiber paper anodes in aqueous LiOH, the chemical identity of the PFAS headgroup (e.g., PFOS vs GenX) did not govern PFAS adsorption; adsorption was controlled by anode characteristics under those conditions.
- Material qualifiers: ["electrode is laser-made [Ni0.75Fe0.25]-(OH)2–hydrophilic carbon fiber paper", "electrolyte is aqueous LiOH", "endpoint is adsorption behavior during pulsed electrolysis", "comparison includes PFOS and GenX with different headgroups", "finding is specific to this anode material and conditions"]
- Evidence: WF10_004b_MMG002
- Prior atomic claims: WF10_004b-C08, WF10_004b-C09
- Full: Award full credit if the answer notes that for adsorption on the specified Ni–Fe hydroxide anode in aqueous LiOH during pulsed electrolysis, PFAS adsorption was not controlled by headgroup identity (e.g., PFOS vs GenX) but instead by anode properties, and treats this as system-specific.
- Partial: Award partial credit if the answer conveys that in at least one electrochemical adsorption system headgroup identity was not a controlling factor, but omits the specific anode/electrolyte context.
- Contradiction: Mark as contradicted if the answer claims that in this Ni–Fe hydroxide anode system headgroup identity strongly governed adsorption in a way inconsistent with the evidence (e.g., asserting clear sulfonate vs carboxylate dominance for adsorption on this anode).

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

- `WF10_004b-G01`: **supported**. Both prior Model B flags (unverifiable short-chain figures in C01; unsupported 'similar chain length' qualifier in C02) are resolved: the canonical proposition and material_qualifiers now assert only the overall sulfonate>carboxylate direction, which is directly entailed by both exact spans.
  Recommended change: None.
- `WF10_004b-G04`: **supported**. Canonical proposition and qualifiers are entailed by the two spans; the 'equal chain length' qualifier is correctly scoped only to the column study (MMG007) where it appears, not misattributed to the ZVI batch data (MMG006).
  Recommended change: None.
- `WF10_004b-G05`: **supported**. Proposition, pH condition, neutral/anionic charge attribution, and mechanism are all directly entailed by the exact span.
  Recommended change: None.
- `WF10_004b-G06`: **supported**. Proposition and mechanistic qualifiers (polar sulfonic moiety, lack of dimer formation) match the exact span verbatim in substance.
  Recommended change: None.
- `WF10_004b-G07`: **supported**. Negative finding is preserved as negative_finding function, not converted to a positive/general claim; span entails the core statement and the does_not_support field is respected.
  Recommended change: None.
- `WF10_004b-G08`: **supported**. This is a distinct synthesis-level proposition (process-specificity/non-universality across systems) rather than a restatement of any single system finding, so reuse of the seven spans already cited in G01/G04/G05/G06/G07 is legitimate cross-referencing rather than duplicate scoring of the same claim.
  Recommended change: None required; ensure scoring implementation treats this as a separate synthesis credit (see human_review_priorities).
- `WF10_004b-B01`: **supported**. Correctly marked scoring_role constraint_only and excluded from coverage denominator; violation_rule is executable (flags blanket universal-headgroup claims) and consistent with supports_universal_claim:no across all cited records.
  Recommended change: None.

Human-review priorities:
- Confirm the scoring implementation treats G08's reuse of the seven system-specific evidence spans (shared with G01/G04/G05/G06/G07) as a distinct synthesis-level credit and does not inflate the coverage denominator by counting the same span twice against two required_content groups.
- Optionally consider whether G04 (bundling the ZVI/ZVI+BC batch study and the iron-modified peat column study, two different papers/matrices) should be split into two independently answerable groups; the current merge is defensible given the shared sulfonate>carboxylate direction and explicit qualifiers scoping the chain-length claim to only the column study, but is a legitimate project-author judgment call rather than a defect.
- The project-author review provenance is a blanket retention confirmation with no item-specific rationale; this is an acceptable basis for treating the seven gold records as retained given gold_is_non_exhaustive, but does not itself constitute independent double-annotation, so residual uncertainty in MMG005's truncated span should be noted to the project author as background context (already excluded from any specific claim numeric requirement in the current ledger).

### Non-normative reference prose

Across the supplied studies, PFAS compound class and headgroup influence treatment performance and adsorption behavior, but the direction and strength of these effects are strongly process- and material-specific.

For treatment performance, several technologies show higher removal or retention of sulfonate PFAS than carboxylate PFAS under comparable conditions. In landfill leachate treated by membrane electrochemical reactor foam fractionation, overall removal of perfluorosulfonic acids was about 98% compared with about 86% for perfluorocarboxylic acids after seven hours of operation. In laboratory-spiked water treated by foam fractionation, PFHeA (a perfluorocarboxylic acid) had about 55% overall removal, whereas PFHeS (a perfluorosulfonic acid) reached about 96%, again indicating a sulfonate advantage in that foam system. Iron-based treatments show a similar pattern: batch tests with zero-valent iron or zero-valent iron plus biochar in water reported more efficient removal of perfluorosulfonic acids (up to 94%) than perfluorocarboxylic acids (up to 60%), and column treatment with iron-modified peat residues for groundwater and landfill leachate retained sulfonate PFAS more strongly than carboxylate PFAS of equal perfluorocarbon chain length, for example 84% PFOS versus 72% PFNA and 64% PFHxS versus 44% PFHpA.

Other processes show different or even opposite headgroup trends. In nanofiltration of groundwater at pH 7.3, FHxSA, which is likely neutral at this pH due to its sulfonamide headgroup, exhibited consistently lower rejection than the anionic sulfonate analogue PFHxS. The lower rejection of FHxSA was attributed to the absence of an electrostatic repulsion mechanism for the neutral sulfonamide species. For adsorption onto all-silica zeolite β in aqueous solution, the trend was reversed relative to the iron-based and foam systems: the adsorption capacity and affinity of the zeolite were lower for sulfonic-acid PFAS than for carboxylic-acid PFAS, an effect linked to the more polar sulfonic moiety and the unlikely formation of sulfonic acid dimers. In yet another case, pulsed electrolysis using laser-made [Ni0.75Fe0.25]-(OH)2–hydrophilic carbon fiber paper anodes in aqueous LiOH showed that the chemical identity of the PFAS headgroup (e.g., comparing PFOS and GenX) did not govern PFAS adsorption; instead, adsorption behavior was controlled by anode characteristics under those specific conditions.

Taken together, these findings demonstrate that PFAS class and headgroup can substantially alter removal, retention, or adsorption equilibria for matched PFAS within individual studies, but the direction and magnitude of headgroup effects depend on the specific treatment technology, material, solution chemistry, and charge state. Some systems favor sulfonates over carboxylates, one adsorbent favors carboxylates over sulfonates, and one electrochemical adsorption system shows no dominant headgroup effect. Cross-study interpretation therefore requires careful matching of compounds, matrices, endpoints, and operating conditions, and the available evidence does not support a universal rule that headgroup identity will control treatment or adsorption behavior for all PFAS and all technologies.

### Prose-to-ledger map

- Across the supplied studies, PFAS compound class and headgroup influence treatment performance and adsorption behavior, but the direction and strength of these effects are strongly process- and material-specific. -> WF10_004b-G08
- For treatment performance, several technologies show higher removal or retention of sulfonate PFAS than carboxylate PFAS under comparable conditions. -> WF10_004b-G01, WF10_004b-G04
- In landfill leachate treated by membrane electrochemical reactor foam fractionation, overall removal of perfluorosulfonic acids was about 98% compared with about 86% for perfluorocarboxylic acids after seven hours of operation. -> WF10_004b-G01
- In laboratory-spiked water treated by foam fractionation, PFHeA (a perfluorocarboxylic acid) had about 55% overall removal, whereas PFHeS (a perfluorosulfonic acid) reached about 96%, again indicating a sulfonate advantage in that foam system. -> WF10_004b-G01
- Iron-based treatments show a similar pattern: batch tests with zero-valent iron or zero-valent iron plus biochar in water reported more efficient removal of perfluorosulfonic acids (up to 94%) than perfluorocarboxylic acids (up to 60%), and column treatment with iron-modified peat residues for groundwater and landfill leachate retained sulfonate PFAS more strongly than carboxylate PFAS of equal perfluorocarbon chain length, for example 84% PFOS versus 72% PFNA and 64% PFHxS versus 44% PFHpA. -> WF10_004b-G04
- Other processes show different or even opposite headgroup trends. -> WF10_004b-G06, WF10_004b-G07, WF10_004b-G05, WF10_004b-G08
- In nanofiltration of groundwater at pH 7.3, FHxSA, which is likely neutral at this pH due to its sulfonamide headgroup, exhibited consistently lower rejection than the anionic sulfonate analogue PFHxS. -> WF10_004b-G05
- The lower rejection of FHxSA was attributed to the absence of an electrostatic repulsion mechanism for the neutral sulfonamide species. -> WF10_004b-G05
- For adsorption onto all-silica zeolite β in aqueous solution, the trend was reversed relative to the iron-based and foam systems: the adsorption capacity and affinity of the zeolite were lower for sulfonic-acid PFAS than for carboxylic-acid PFAS, an effect linked to the more polar sulfonic moiety and the unlikely formation of sulfonic acid dimers. -> WF10_004b-G06
- In yet another case, pulsed electrolysis using laser-made [Ni0.75Fe0.25]-(OH)2–hydrophilic carbon fiber paper anodes in aqueous LiOH showed that the chemical identity of the PFAS headgroup (e.g., comparing PFOS and GenX) did not govern PFAS adsorption; instead, adsorption behavior was controlled by anode characteristics under those specific conditions. -> WF10_004b-G07
- Taken together, these findings demonstrate that PFAS class and headgroup can substantially alter removal, retention, or adsorption equilibria for matched PFAS within individual studies, but the direction and magnitude of headgroup effects depend on the specific treatment technology, material, solution chemistry, and charge state. -> WF10_004b-G01, WF10_004b-G04, WF10_004b-G05, WF10_004b-G06, WF10_004b-G07, WF10_004b-G08
- Some systems favor sulfonates over carboxylates, one adsorbent favors carboxylates over sulfonates, and one electrochemical adsorption system shows no dominant headgroup effect. -> WF10_004b-G01, WF10_004b-G04, WF10_004b-G06, WF10_004b-G07
- Cross-study interpretation therefore requires careful matching of compounds, matrices, endpoints, and operating conditions, and the available evidence does not support a universal rule that headgroup identity will control treatment or adsorption behavior for all PFAS and all technologies. -> WF10_004b-G08, WF10_004b-B01

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
> Table S8 shows that the ratios for the Lead + Lag to Lead column for q ΣPFAS were only slightly different from unity (1.07 ± 0.12), implying that adsorption mechanisms are inde- pendent of EBCT.

**WF10_036_MMG003** (optional_gold; `2020 - Zeng - Removing per- and polyfluoroalkyl substances from groundwaters using activated carbon.pdf`, chunk `15`)
> This indicates that longer EBCTs do not suffer from competing adsorbates (e.g., ionic species, DOC), and the similar breakthrough curve shapes suggest shorter EBCTs (i.e., ~2 –5 min) capture the mass transfer zone.

**WF10_036_MMG004** (optional_gold; `2022 - Kempisty - Granular activated carbon adsorption of perfluoroalkyl acids from ground and surface.pdf`, chunk `37`)
> Although break- through curves for individual PFAAs did not perfectly overlap at the two EBCTs, consistent trends suggesting that either shorter or longer EBCTs resulted in lower CURs were not observed.

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

# L3 Dev13 reference-answer human audit

Status: **all decisions pending**

For each question, inspect the complete gold evidence, Model A draft,
and Model B review. Edit `reference_candidates.jsonl` if needed, then
set `human_review.decision` to `approve` or `reject`. An approval of a
Model B `revise` or `reject` item requires non-empty resolution notes.

## NQ10

**Question:** How are PFAS samples preconcentrated before mass spectrometry, and how do protocols vary by matrix, analyte, or method?

**Must include:** Must connect SPE selection to matrix and analyte scope; must mention recovery or chemistry-dependent suitability when supported.

**Must not claim:** Must not claim one exact SPE cartridge and elution protocol is universally correct for all PFAS environmental samples.

### Complete Gold Evidence

**NQ10_MMG001** (required_gold; `2021 - Olomukoro - [SOURCE_TEXT_OMITTED sha256=ee628acbd9c2af4edf45cbdbfe7ee9b8944cf2c7fbb577c31501368c694526d7].pdf`, chunk `36`)  
Scope: PFAS; aqueous (river, lake, tap, bottled water); SPME; separation; 1-2 (unit truncated); ng/L (truncated in span)  
> [SOURCE_TEXT_OMITTED sha256=469013d9469e2f088c33eba45896cb806c245ec2eb3f3e7be1c475ef589ac4ad].  
Supported claim metadata: An [SOURCE_TEXT_OMITTED sha256=419f1980cb89d7fddef2454a16ce7c1df433321e8765c197db8056fc5cb4afd3]; the selected span reports LOQs beginning with “1–2” but truncates the units/range.  
Does not support: Does not support the specific value '1-2.5 ng L−1' or '1.5 mL sample volume' as those numbers are not present in the selected spans.

**NQ10_MMG002** (required_gold; `2021 - Olomukoro - [SOURCE_TEXT_OMITTED sha256=ee628acbd9c2af4edf45cbdbfe7ee9b8944cf2c7fbb577c31501368c694526d7].pdf`, chunk `34`)  
Scope: 24 PFAS compounds; drinking water; dilute-and-shoot (EPA method 8327); other (no preconcentration); 10-50 ng/L; ng/L  
> [SOURCE_TEXT_OMITTED sha256=c378a9b6ac19269490bb0291bfbb3dccb3131b3fd5063898f6b886c43b97d7c6]  
Supported claim metadata: EPA Method 8327 uses dilute-and-shoot (no separate preconcentration step) for 24 PFAS compounds in drinking water.  
Does not support: Does not support 'LOQs of 10-50 ng/L'; the span shows '3 ng L−1' and '40–160 ng L−1' for adjacent rows, not a clean 10-50 ng/L range for EPA 8327.

**NQ10_MMG003** (required_gold; `2021 - Olomukoro - [SOURCE_TEXT_OMITTED sha256=ee628acbd9c2af4edf45cbdbfe7ee9b8944cf2c7fbb577c31501368c694526d7].pdf`, chunk `6`)  
Scope: PFAS; SPE, LLE; preconcentration  
> [SOURCE_TEXT_OMITTED sha256=03fa6037597d41bc4c6c5a8cea348634f2cae2ecfc43471a313752c65ceedc98] ].  
Supported claim metadata: PFAS preconcentration to detect ppt-level analytes has been accomplished by either solid phase extraction (SPE) or liquid-liquid extraction (LLE).

**NQ10_MMG004** (optional_gold; `2022 - Pellicer-Castell - Iron-Doped Bimodal Mesoporous Silica Nanomaterials as Sorbents for Solid-Phase Extraction of Perfluoroalkyl Substances in Environmental.pdf`, chunk `42`)  
Scope: PFASs; water; SPE (150 mg cartridge); recovery (preconcentration); 150 mg, 10-100 mL; mg, mL  
> [SOURCE_TEXT_OMITTED sha256=87c68bb46c27be15a4694fda8735b811754ab515a80f0e9570fcd2ac0933ea18].  
Supported claim metadata: With 150 mg cartridges, recoveries decreased when sample volume was increased from 10 to 100 mL.

**NQ10_MMG005** (optional_gold; `2022 - Pellicer-Castell - Iron-Doped Bimodal Mesoporous Silica Nanomaterials as Sorbents for Solid-Phase Extraction of Perfluoroalkyl Substances in Environmental.pdf`, chunk `43`)  
Scope: PFOS, PFNA (C8-C14); SPE; recovery (preconcentration); >61%, ~100%, EF 121-212; %  
> ([SOURCE_TEXT_OMITTED sha256=4b0660a78efdf23a909ff5eb1ca11842ea6a8a985d897643c04897a0ad32694d].  
Supported claim metadata: SPE/extraction recoveries for C8-C14 PFAS were above 61%, close to 100% for PFOS or PFNA, differed among PFAS analytes, and produced enrichment factors of 121-212.

**NQ10_MMG006** (optional_gold; `2022 - Croll - [SOURCE_TEXT_OMITTED sha256=2da68f19fe53ac7102bced27c910f07f3248ff01d66b21468a8d59223b057783].pdf`, chunk `12`)  
Scope: target PFAS; groundwater; weak anion exchange SPE with methanolic elution; preconcentration; 500-fold, 0.5 mL; fold, mL  
> [SOURCE_TEXT_OMITTED sha256=32c6b524ae782f897b8c7ddfc2092da8ed5aaa55192906ba9a33d637b5e79a99].  
Supported claim metadata: [SOURCE_TEXT_OMITTED sha256=32c6b524ae782f897b8c7ddfc2092da8ed5aaa55192906ba9a33d637b5e79a99].  
Does not support: The selected span alone does not state weak anion exchange SPE; the preceding sentence in the full chunk supplies that context.

**NQ10_MMG007** (optional_gold; `2024 - Habib - [SOURCE_TEXT_OMITTED sha256=8c88db8a3af919c38e76bc825405f2148aacae0b1d14cb9ebfa199b5f94fc272].pdf`, chunk `11`)  
Scope: PFCAs; water; SBSE + TD-GC-MS; preconcentration  
> [SOURCE_TEXT_OMITTED sha256=30d7b57ac11c9607efbcb46f1561d12d7de16c38c34ce20d4b88323ced603271].  
Supported claim metadata: The study developed and validated a method integrating stir bar sorptive extraction (SBSE) with thermal desorption-GC-MS for analysis of perfluorocarboxylic acids (PFCAs), a subgroup of PFAS.

**NQ10_MMG008** (optional_gold; `2023 - Hao - Hydrothermal Alkaline Treatment (HALT) of Foam Fractionation Concentrate Derived from PFAS-Contaminated Groundwater.pdf`, chunk `9`)  
Scope: PFASs; foam concentrate; dilute and direct injection; other (no preconcentration)  
> [SOURCE_TEXT_OMITTED sha256=22dde9e759cfb91bc92ed1d4758c0cde151d84863914426a035f338b3d829c32].  
Supported claim metadata: Diluted samples were mixed with ammonium hydroxide solution, isopropyl alcohol, trifluoroethanol, water, internal standards, and methanol before injection into an HPLC system; no solid-phase or liquid-liquid extraction was used in the sample preparation.

**NQ10_MMG009** (optional_gold; `2021 - Olomukoro - [SOURCE_TEXT_OMITTED sha256=ee628acbd9c2af4edf45cbdbfe7ee9b8944cf2c7fbb577c31501368c694526d7].pdf`, chunk `32`)  
Scope: SPME vs dilute-and-shoot; preconcentration  
> [SOURCE_TEXT_OMITTED sha256=20d98169239ded1034935506504d212e72fb369325e92d4d503c4861fdf864dd].  
Supported claim metadata: Compared with very fast sample-processing methods such as dilute-and-shoot, the authors’ method provides higher preconcentration and limits occurrence of matrix effects.

**NQ10_MMG010** (negative_gold; `2021 - Olomukoro - [SOURCE_TEXT_OMITTED sha256=ee628acbd9c2af4edf45cbdbfe7ee9b8944cf2c7fbb577c31501368c694526d7].pdf`, chunk `7`)  
Scope: complex samples; not named in span; QAQC/limitation  
> [SOURCE_TEXT_OMITTED sha256=bf770acb02a6cde476a8c0a120becd99a5b99de54d2c809bc12dd35556192b5b].  
Supported claim metadata: Substantial matrix effects can occur during analysis, making the method unsuitable and not robust for complex samples.  
Does not support: The selected span does not explicitly name 'dilute-and-shoot' as the method with matrix effects; the attribution to dilute-and-shoot must be confirmed from surrounding context.

### Model A Reference Draft

Across the supplied studies, PFAS preconcentration prior to chromatographic–mass spectrometric analysis is typically achieved by sorptive extraction (SPE, SPME, SBSE) or, more generally, by SPE or liquid–liquid extraction when parts‑per‑trillion levels must be measured, although not all workflows include a dedicated preconcentration step.

For ppt‑level determinations in general, sample preconcentration has been accomplished using solid‑phase extraction (SPE) or liquid–liquid extraction (LLE) before analysis.
One groundwater workflow uses weak anion exchange SPE with methanolic elution; collecting 0.5 mL of methanolic extract produced an effective 500‑fold concentration of the target PFAS relative to the initial sampling volume.
Another SPE study using 150 mg cartridges for water samples found that recoveries clearly decreased as the loaded volume increased from 10 mL to 100 mL, indicating that SPE conditions (sorbent amount vs. sample volume) directly control preconcentration efficiency.
In that study, C8–C14 PFAS achieved recoveries above 61% for all analytes and close to 100% for PFOS and PFNA, with enrichment factors between 121 and 212, showing that even within a single SPE protocol, enrichment and recovery are analyte‑dependent.

Alternative sorptive microextraction formats are also used and are strongly matrix‑linked.
A solid‑phase microextraction ([SOURCE_TEXT_OMITTED sha256=215fa32bd6b0d5a2e94405abaddfd952894bb801a8fc03de3770271411b1dc1e]; in the same work, the SPME approach provided higher preconcentration and reduced matrix effects compared with very fast sample‑processing approaches such as dilute‑and‑shoot.
Nevertheless, substantial matrix effects were noted in some methods, to the extent that the method was judged unsuitable and not robust for complex samples, underscoring that matrix composition can limit the applicability of simpler preparations.
For perfluorocarboxylic acids (PFCAs), a significant PFAS subgroup, a separate method integrated stir bar sorptive extraction (SBSE) with thermal desorption–gas chromatography–mass spectrometry (TD‑GC‑MS) for water samples; SBSE here serves as the preconcentration step tailored specifically to PFCAs and is compatible with solvent‑free thermal desorption into GC‑MS.

In contrast, some protocols for relatively clean or highly enriched aqueous matrices omit explicit preconcentration.
EPA Method 8327 for drinking water employs a dilute‑and‑shoot strategy, with no dedicated preconcentration step, for 24 PFAS compounds.
Another study analyzing PFAS in foam‑fractionation concentrate (derived from contaminated groundwater) prepared samples by dilution and mixing with aqueous ammonium hydroxide solution, isopropyl alcohol, trifluoroethanol, water, internal standards, and methanol before HPLC injection, again without any solid‑phase or liquid–liquid extraction.
These examples illustrate that when concentrations are higher or matrices are amenable, analysts may rely on dilution and modifier addition rather than a separate preconcentration stage.

Taken together, the evidence shows that PFAS preconcentration strategies are chosen based on matrix and analyte scope: SPE (including anion‑exchange formats) is used for groundwater and other waters when high enrichment is required; SPME is applied to a range of natural and drinking waters to increase preconcentration and mitigate matrix effects relative to dilute‑and‑shoot; SBSE is adopted for PFCAs in water in a GC‑MS context; and dilute‑and‑shoot or dilution‑only protocols are used for drinking water and foam concentrate where PFAS levels or matrix simplicity make preconcentration less critical.
Performance metrics such as recovery, enrichment factor, and susceptibility to matrix effects vary by method, sorbent loading, sample volume, analyte chain length, and matrix complexity, and the supplied studies do not suggest that any single SPE cartridge or elution protocol would be universally appropriate for all environmental PFAS samples.

Claims:

- `NQ10-C01` [core]: For parts-per-trillion level PFAS determinations, sample preconcentration has been accomplished using either solid phase extraction (SPE) or liquid–liquid extraction (LLE). (evidence: NQ10_MMG003)
- `NQ10-C02` [core]: In a groundwater application, target PFAS were preconcentrated using weak anion exchange solid phase extraction, and elution to 0.5 mL of methanolic extract resulted in an effective 500-fold concentration of the analytes relative to the initial sampling. (evidence: NQ10_MMG006)
- `NQ10-C03` [supporting]: When PFAS in water were extracted using 150 mg SPE cartridges, recoveries clearly decreased as the sample volume was increased from 10 mL to 100 mL. (evidence: NQ10_MMG004)
- `NQ10-C04` [supporting]: In one SPE protocol, C8–C14 PFAS showed extraction recoveries above 61% for all analytes and close to 100% for PFOS and PFNA, with enrichment factors between 121 and 212. (evidence: NQ10_MMG005)
- `NQ10-C05` [core]: A solid phase microextraction ([SOURCE_TEXT_OMITTED sha256=215fa32bd6b0d5a2e94405abaddfd952894bb801a8fc03de3770271411b1dc1e]. (evidence: NQ10_MMG001)
- `NQ10-C06` [core]: Compared with very fast sample-processing methods such as dilute-and-shoot, the SPME method provided higher preconcentration of PFAS and limited the occurrence of matrix effects. (evidence: NQ10_MMG009)
- `NQ10-C07` [limitation]: In some PFAS analytical methods, substantial matrix effects occurred during analysis, making the method not suitable and not robust for complex samples. (evidence: NQ10_MMG010)
- `NQ10-C08` [core]: EPA Method 8327 for drinking water uses a dilute-and-shoot approach with no separate preconcentration step for 24 PFAS compounds. (evidence: NQ10_MMG002)
- `NQ10-C09` [core]: In analysis of PFAS in foam fractionation concentrate, [SOURCE_TEXT_OMITTED sha256=5b1224194a9ac936fc0d600a4995c5e37b7066a0c6357677e715c9e54cd3b411] HPLC injection, without employing solid-phase or liquid–liquid extraction for preconcentration. (evidence: NQ10_MMG008)
- `NQ10-C10` [core]: A method integrating stir bar sorptive extraction (SBSE) with thermal desorption–gas chromatography–mass spectrometry (TD-GC-MS) was developed and validated for analysis of perfluorocarboxylic acids (PFCAs) in water. (evidence: NQ10_MMG007)
- `NQ10-C11` [core]: Across the reported examples, preconcentration and sample preparation strategies vary by matrix, with weak anion exchange SPE used for groundwater, SPME applied to river, lake, tap, and bottled waters, SBSE used for water samples containing PFCAs, and dilute-and-shoot or dilution-only approaches applied to drinking water and foam concentrate matrices. (evidence: NQ10_MMG006, NQ10_MMG001, NQ10_MMG007, NQ10_MMG002, NQ10_MMG008)
- `NQ10-C12` [supporting]: Preconcentration performance and method suitability are analyte- and matrix-dependent, as shown by SPE recoveries above 61% and near 100% for some C8–C14 PFAS in one protocol, contrasted with reports that substantial matrix effects can render other methods unsuitable for complex samples. (evidence: NQ10_MMG005, NQ10_MMG010)
- `NQ10-C13` [core]: Reported preconcentration factors for SPE-based PFAS methods span at least from enrichment factors of 121–212 in one study to an effective 500-fold concentration in another groundwater application, indicating that achievable enrichment depends on the specific SPE protocol and matrix. (evidence: NQ10_MMG005, NQ10_MMG006)
- `NQ10-C14` [core]: Some PFAS analytical workflows do not include a dedicated preconcentration step, instead relying on direct injection after dilution or simple solvent modification, as illustrated by dilute-and-shoot drinking water analysis and diluted foam concentrate prepared with added solvents and bases. (evidence: NQ10_MMG002, NQ10_MMG008)

### Model B Verification

Overall verdict: **revise**

- `NQ10-C01`: **supported**. Exact span states preconcentration for ppt-level PFAS has been accomplished by SPE or LLE, matching the claim precisely.
  Recommended text: No change needed.
- `NQ10-C02`: **partially_supported**. The quoted exact_evidence_span only states '0.5 mL... 500-fold concentration'; it does not itself mention 'weak anion exchange SPE'. The gold record's own does_not_support field explicitly warns that this attribution comes from a preceding sentence outside the selected span. Model A stated the SPE chemistry as settled fact without hedging that this detail is drawn from surrounding context rather than the quoted span itself.
  Recommended text: In a groundwater application (reported to use weak anion exchange SPE per surrounding context), elution to 0.5 mL of methanolic extract resulted in an effective 500-fold concentration of target PFAS relative to the initial sampling.
- `NQ10-C03`: **supported**. Matches span exactly: 150 mg cartridges, recovery decrease from 10 to 100 mL.
  Recommended text: No change needed.
- `NQ10-C04`: **partially_supported**. The exact_evidence_span text ('([SOURCE_TEXT_OMITTED sha256=4b0660a78efdf23a909ff5eb1ca11842ea6a8a985d897643c04897a0ad32694d]') does not itself contain the enrichment factor figures 121-212; that number appears only in the gold record's supported_claim/numerical_value metadata fields, not the quoted span. The recovery portion of the claim is fully supported; the EF figure is not verifiable from the span text alone.
  Recommended text: In one SPE protocol, C8–C14 PFAS showed extraction recoveries above 61% for all analytes and close to 100% for PFOS and PFNA (enrichment factors reported elsewhere in the source as 121–212, not directly quoted in the retrieved span).
- `NQ10-C05`: **supported**. Directly matches span; correctly avoids the truncated LOQ numbers flagged as unsupported in the gold record.
  Recommended text: No change needed.
- `NQ10-C06`: **supported**. Matches span closely.
  Recommended text: No change needed.
- `NQ10-C07`: **supported**. Claim correctly avoids naming 'dilute-and-shoot' as the method with matrix effects, consistent with the gold record's does_not_support caveat that the span doesn't name the method.
  Recommended text: No change needed.
- `NQ10-C08`: **supported**. Matches span and metadata; correctly omits the unsupported '10-50 ng/L' LOQ figure flagged in does_not_support.
  Recommended text: No change needed.
- `NQ10-C09`: **supported**. Matches span; correctly frames as dilution/modifier addition without SPE/LLE.
  Recommended text: No change needed.
- `NQ10-C10`: **supported**. Matches span closely.
  Recommended text: No change needed.
- `NQ10-C11`: **supported**. This is an accurate aggregation of five already-verified individual claims into a matrix-comparison summary; content is faithful to the underlying evidence. Labeling it 'core' rather than 'supporting' is defensible since it directly answers the 'how protocols vary by matrix' part of the question, though it is a synthesis rather than a standalone finding.
  Recommended text: No change needed; claim_type could reasonably be 'supporting' instead of 'core' since it restates prior claims.
- `NQ10-C12`: **partially_supported**. The claim juxtaposes two unrelated studies (an SPE recovery study and a separate, unnamed-method matrix-effects limitation) to assert a general principle that 'preconcentration performance and method suitability are analyte- and matrix-dependent.' Each individual fact is supported, but framing them as a direct 'contrast' illustrating a shared dependency is an inferential leap beyond what either span states, since the two evidence items describe different, non-comparable methods.
  Recommended text: Preconcentration recovery can be analyte-dependent, as shown by SPE recoveries above 61% and near 100% for some C8–C14 PFAS in one protocol; separately, other reports note that substantial matrix effects can render some methods unsuitable for complex samples.
- `NQ10-C13`: **partially_supported**. Combines the same EF 121-212 figure not present in the NQ10_MMG005 exact span (see C04) with the weak-anion-exchange-SPE attribution for NQ10_MMG006 that the gold record itself flags as coming from outside the quoted span (see C02). The 500-fold figure and >61%/~100% recovery figures are directly supported, but the compound claim inherits both upstream span-verification gaps.
  Recommended text: Reported preconcentration/enrichment outcomes for SPE-based PFAS methods range from recoveries above 61% (up to ~100% for some analytes) in one study to an effective 500-fold concentration in a separate groundwater application, indicating that achievable enrichment depends on the specific protocol and matrix.
- `NQ10-C14`: **supported**. Accurately restates the two dilute/no-preconcentration workflows already verified in C08 and C09.
  Recommended text: No change needed.

Reference-answer issues:
- The gold packet itself contains an internal inconsistency for NQ10_MMG005: the exact_evidence_span text ('...[SOURCE_TEXT_OMITTED sha256=c11af0fe044c1da524bbec09a628429d254564b64da7a2144dc88d718a5879ba].') does not contain the enrichment-factor figures ('EF 121-212') that appear in the record's own supported_claim and numerical_value fields. Any claim reproducing the EF number is only verifiable against the metadata, not the literal quoted span, which weakens strict span-level verifiability.
- For NQ10_MMG006, the gold record's own does_not_support field flags that 'weak anion exchange SPE' is not stated in the selected span and requires context from a preceding sentence not included in exact_evidence_span; this creates a recurring risk that downstream claims (C02, C13) assert method chemistry not directly checkable from the supplied span text.

---

## NQ12

**Question:** What chain-length-related differences in PFAS analytical sensitivity or LOD/LOQ have been reported, and how do method or instrument settings affect them?

**Must include:** Must recognize compound-dependent analytical behavior; must connect calculation or interpretation to method/instrument conditions.

**Must not claim:** Must not claim one universal LOD/LOQ calculation or performance pattern applies identically to all PFAS chain lengths.

### Complete Gold Evidence

**NQ12_MMG001** (required_gold; `2022 - Pellicer-Castell - Iron-Doped Bimodal Mesoporous Silica Nanomaterials as Sorbents for Solid-Phase Extraction of Perfluoroalkyl Substances in Environmental.pdf`, chunk `44`)  
Scope: PFOA, PFNA, PFOS, PFDA, PFUnDA, PFDS, PFDoDA, PFTrDA, PFTeDA; water samples; developed SPE-UHPLC-MS/MS method; LOD/LOQ; LOD 3–8 ng/L; LOQ 9–25 ng/L; ng/L  
> [SOURCE_TEXT_OMITTED sha256=c9e327c778f731b6532a3deae84b57288d4614b08318dbbc0bf15c323f604e0f].  
Supported claim metadata: For the developed SPE-UHPLC-MS/MS method for C8–C14 PFASs from water samples, reported sensitivity varied by compound: LOD/LOQ values were PFOA 4/12 ng/L, PFNA 7/22 ng/L, PFOS 3/9 ng/L, PFDA 8/24 ng/L, PFUnDA 7/21 ng/L, PFDS 3/11 ng/L, PFDoDA 6/18 ng/L, PFTrDA 8/25 ng/L, and PFTeDA 3/11 ng/L.  
Does not support: The claim must not omit PFOS and PFDS, which are present in the table; and the column interpretation (LOD vs LOQ) must be read carefully since the header groups Sensitivity (LOD/LOQ) ambiguously.

**NQ12_MMG002** (required_gold; `2024 - Habib - [SOURCE_TEXT_OMITTED sha256=8c88db8a3af919c38e76bc825405f2148aacae0b1d14cb9ebfa199b5f94fc272].pdf`, chunk `47`)  
Scope: PFHpA, PFOA, PFNA, PFDA, PFUnA, PFDoA, PFTeDA; water; SBSE-TD-GC-MS; LOD/LOQ/MDL; LOD 21.17–73.96 ng/L; LOQ 90.80–192.01 ng/L; ng/L  
> [SOURCE_TEXT_OMITTED sha256=97e055ca053f6ab1f7c513ff7983ab62cf13f9edee1c0e0ff8660edcf6087d78]  
Supported claim metadata: For PFCAs analyzed in water by SBSE-TD-GC-MS, sensitivity varied by compound/chain length: LODs were 21.17 ng/L for PFHpA, 21.20 ng/L for PFOA, 30.12 ng/L for PFNA, 54.29 ng/L for PFDA, 34.39 ng/L for PFUnA, 73.96 ng/L for PFDoA, and 35.02 ng/L for PFTeDA; corresponding LOQs were 138.27, 103.13, 90.80, 169.85, 132.90, 192.01, and 107.10 ng/L, respectively. The table also reports increasing retention time and parent ion m/z with longer-chain PFCAs under the SBSE-TD-GC-MS method.

**NQ12_MMG003** (required_gold; `2025 - Tomei - [SOURCE_TEXT_OMITTED sha256=05336b6fc60565e4f0b1b9e0a861c5ad2d549d57f0d2d037e9e61c44be655f30].pdf`, chunk `14`)  
Scope: short-chain PFAS (C < 5); water; SPE-LC-q-TOF; instrument signal (sensitivity); 60 V; [SOURCE_TEXT_OMITTED sha256=5c6ee0cdfb6c182af2b806b41ac9f8bbc0c78e2aad5539e2a707c9524d7d3f77];  
Supported claim metadata: At a fragmentor voltage of [SOURCE_TEXT_OMITTED sha256=ac882bcfdf44ca19b70881247bb03a0b60b487bd2212abd1083392bd73d11cc7]; this demonstrates that fragmentor voltage (an instrument setting) strongly affects sensitivity for short-chain PFAS.  
Does not support: Does not provide LOD/LOQ numerical values; addresses only the instrument-setting/sensitivity relationship.

### Model A Reference Draft

Available studies consistently show that PFAS detection limits are both compound-specific and method-dependent, and that instrument settings can differentially affect sensitivity by chain length.

For an SPE–UHPLC–MS/MS method applied to water, C8–C14 PFAS (PFOA, PFNA, PFOS, PFDA, PFUnDA, PFDS, PFDoDA, PFTrDA, PFTeDA) exhibited distinct LOD and LOQ values by compound rather than a single pattern across the series. Reported LODs ranged from 3 to 8 ng/L and LOQs from 9 to 25 ng/L. For example, PFOA had an LOD/LOQ of 4/12 ng/L, PFNA 7/22 ng/L, PFOS 3/9 ng/L, PFDA 8/24 ng/L, PFUnDA 7/21 ng/L, PFDS 3/11 ng/L, PFDoDA 6/18 ng/L, PFTrDA 8/25 ng/L, and PFTeDA 3/11 ng/L in water with this SPE–UHPLC–MS/MS procedure. These values show that even within a relatively narrow chain-length range, individual PFAS achieve different detection limits under the same method and conditions.

In a different water-analysis method using stir bar sorptive extraction with thermal desorption GC–MS (SBSE–TD–GC–MS), perfluorocarboxylic acids PFHpA through PFTeDA also showed compound-dependent sensitivity. LODs spanned 21.17–73.96 ng/L and LOQs 90.80–192.01 ng/L, with specific examples such as PFHpA at 21.17/138.27 ng/L (LOD/LOQ), PFOA at 21.20/103.13 ng/L, PFNA at 30.12/90.80 ng/L, PFDA at 54.29/169.85 ng/L, PFUnA at 34.39/132.90 ng/L, PFDoA at 73.96/192.01 ng/L, and PFTeDA at 35.02/107.10 ng/L. Under this SBSE–TD–GC–MS method, retention time and parent ion m/z increased with chain length, while the LOD/LOQ values varied non-uniformly among the analytes, again demonstrating that detection limits are specific to each PFCA–method combination.

Comparing these two methods in water illustrates that absolute sensitivity ranges are strongly method-dependent in addition to being compound-dependent: the SPE–UHPLC–MS/MS procedure achieved lower LODs (3–8 ng/L) and LOQs (9–25 ng/L) for C8–C14 PFAS, whereas the SBSE–TD–GC–MS method reported higher LODs (21.17–73.96 ng/L) and LOQs (90.80–192.01 ng/L) for a set of C7–C14 PFCAs. The data do not support a single universal trend of LOD/LOQ versus chain length across methods; instead, each analytical configuration yields its own pattern of compound-specific detection limits.

Instrument tuning can further alter chain-length-dependent sensitivity. In an SPE–LC–q‑TOF method targeting PFAS degradation products in water, in-source fragmentation of carboxylic acids was strongly affected by the fragmentor voltage: at 60 V, the signal for short-chain PFAS (C < 5) was almost completely lost, leading the authors to discard this setting. This qualitative observation shows that a mass spectrometer parameter (fragmentor voltage) can disproportionately suppress the detectable signal of short-chain PFAS relative to other analytes, thereby worsening their effective sensitivity and practical detection limits, even though exact LOD/LOQ values were not reported.

Overall, the evidence indicates that (1) PFAS LODs/LOQs differ by individual compound within a given method; (2) the absolute LOD/LOQ ranges depend strongly on the sample preparation and instrumental platform (e.g., SPE–UHPLC–MS/MS versus SBSE–TD–GC–MS); and (3) specific instrument settings, such as fragmentor voltage in LC–q‑TOF, can critically and selectively impact sensitivity for particular chain lengths (notably short-chain PFAS). The available data do not justify a single universal LOD/LOQ pattern across all PFAS chain lengths or all analytical methods.

Claims:

- `NQ12-C01` [core]: In a developed SPE–UHPLC–MS/MS method for C8–C14 PFAS in water, each compound showed its own LOD and LOQ, with LODs between 3 and 8 ng/L and LOQs between 9 and 25 ng/L. (evidence: NQ12_MMG001)
- `NQ12-C02` [core]: Under this SPE–UHPLC–MS/MS method in water, reported LOD/LOQ pairs were 4/12 ng/L for PFOA, 7/22 ng/L for PFNA, 3/9 ng/L for PFOS, 8/24 ng/L for PFDA, 7/21 ng/L for PFUnDA, 3/11 ng/L for PFDS, 6/18 ng/L for PFDoDA, 8/25 ng/L for PFTrDA, and 3/11 ng/L for PFTeDA. (evidence: NQ12_MMG001)
- `NQ12-C03` [core]: The SPE–UHPLC–MS/MS data show that, even within a relatively narrow C8–C14 range, detection limits differ by individual PFAS rather than following a single uniform LOD/LOQ value across all compounds. (evidence: NQ12_MMG001)
- `NQ12-C04` [core]: For a stir bar sorptive extraction with thermal desorption GC–MS (SBSE–TD–GC–MS) method applied to water, PFCAs PFHpA, PFOA, PFNA, PFDA, PFUnA, PFDoA, and PFTeDA exhibited compound-specific LODs ranging from 21.17 to 73.96 ng/L and LOQs from 90.80 to 192.01 ng/L. (evidence: NQ12_MMG002)
- `NQ12-C05` [core]: Under the SBSE–TD–GC–MS method in water, individual LOD/LOQ pairs were 21.17/138.27 ng/L for PFHpA, 21.20/103.13 ng/L for PFOA, 30.12/90.80 ng/L for PFNA, 54.29/169.85 ng/L for PFDA, 34.39/132.90 ng/L for PFUnA, 73.96/192.01 ng/L for PFDoA, and 35.02/107.10 ng/L for PFTeDA. (evidence: NQ12_MMG002)
- `NQ12-S01` [supporting]: In the SBSE–TD–GC–MS study, retention time and parent ion m/z increased with longer-chain PFCAs, while the LOD and LOQ values varied among analytes rather than mirroring a simple monotonic trend with chain length. (evidence: NQ12_MMG002)
- `NQ12-C06` [core]: Comparing the two water-analysis methods, the SPE–UHPLC–MS/MS procedure reported lower LODs (3–8 ng/L) and LOQs (9–25 ng/L) for C8–C14 PFAS than the SBSE–TD–GC–MS method, which reported higher LODs (21.17–73.96 ng/L) and LOQs (90.80–192.01 ng/L) for C7–C14 PFCAs, indicating that absolute detection limits depend on the analytical method as well as on the individual PFAS. (evidence: NQ12_MMG001, NQ12_MMG002)
- `NQ12-C07` [core]: In an SPE–LC–q‑TOF method targeting PFAS-related carboxylic acids in water, setting the fragmentor voltage to 60 V caused the signal of short-chain PFAS (C < 5) to be almost lost, leading this fragmentor setting to be discarded. (evidence: NQ12_MMG003)
- `NQ12-S02` [supporting]: The near-complete loss of short-chain PFAS signal at 60 V in the LC–q‑TOF study demonstrates that fragmentor voltage, an instrument tuning parameter, can selectively and strongly reduce sensitivity for short-chain PFAS relative to other analytes. (evidence: NQ12_MMG003)
- `NQ12-L01` [limitation]: The LC–q‑TOF study reporting loss of short-chain PFAS signal at 60 V did not provide numerical LOD or LOQ values, limiting quantitative assessment of how fragmentor voltage changes detection limits. (evidence: NQ12_MMG003)
- `NQ12-L02` [limitation]: All reported LOD/LOQ data come from water matrices and from specific PFAS subsets (C7–C14 PFCAs and C8–C14 PFAS), so the available evidence does not establish chain-length–sensitivity relationships for other PFAS classes or matrices. (evidence: NQ12_MMG001, NQ12_MMG002)

### Model B Verification

Overall verdict: **revise**

- `NQ12-C01`: **partially_supported**. The LOD (3-8 ng/L) and LOQ (9-25 ng/L) ranges are correctly computed from the table. However, the claim's conditions_and_scope states detection limits 'refer to the final injection solution,' but in the evidence span the footnote marker 'a' is attached only to the 'Linearity' column header ('Linearity a (µg L−1)'), not to the Sensitivity/LOD/LOQ columns. Attributing this footnote to the LOD/LOQ values rather than to linearity is a scope misattribution not directly supported by the exact span.
  Recommended text: In a developed SPE–UHPLC–MS/MS method for C8–C14 PFAS in water, each compound showed its own LOD and LOQ, with LODs between 3 and 8 ng/L and LOQs between 9 and 25 ng/L (the table's 'referred to the final injection solution' footnote is attached to the linearity column, not explicitly to LOD/LOQ).
- `NQ12-C02`: **supported**. All nine compound-specific LOD/LOQ pairs (PFOA 4/12, PFNA 7/22, PFOS 3/9, PFDA 8/24, PFUnDA 7/21, PFDS 3/11, PFDoDA 6/18, PFTrDA 8/25, PFTeDA 3/11 ng/L) match the tabulated values exactly when the row is parsed as Linearity, LOD, LOQ, Extraction Efficiency, EF, Intra-Day RSD, Inter-Day RSD, consistent with the 'LOD LOQ' sub-headers present in the evidence span. No compound is omitted, addressing the does_not_support caution about PFOS/PFDS.
  Recommended text: No change needed.
- `NQ12-C03`: **supported**. The interpretive claim that detection limits differ by compound within the narrow C8–C14 range is a reasonable, non-overreaching reading of the divergent LOD/LOQ values in the table and does not assert any cross-method or cross-class generalization.
  Recommended text: No change needed.
- `NQ12-C04`: **supported**. LOD range (21.17-73.96 ng/L) and LOQ range (90.80-192.01 ng/L) are correctly computed as the min/max of the seven listed PFCAs' values in the evidence span.
  Recommended text: No change needed.
- `NQ12-C05`: **supported**. All seven compound-specific LOD/LOQ pairs match the evidence span exactly (PFHpA 21.17/138.27, PFOA 21.20/103.13, PFNA 30.12/90.80, PFDA 54.29/169.85, PFUnA 34.39/132.90, PFDoA 73.96/192.01, PFTeDA 35.02/107.10 ng/L), correctly attributed to the SBSE-TD-GC-MS method in water.
  Recommended text: No change needed.
- `NQ12-S01`: **supported**. Retention time (5.884→11.422 min) and parent ion m/z (405→755) both increase monotonically with chain length across the seven analytes in the evidence span, and LOD/LOQ values do not follow a simple monotonic trend, as claimed. Correctly labeled supporting rather than core.
  Recommended text: No change needed.
- `NQ12-C06`: **supported**. The cross-method comparison correctly restates the ranges already verified in C01 and C04 and draws a modest, evidence-scoped inference (method affects absolute sensitivity) without claiming causality or universality beyond the two reported protocols.
  Recommended text: No change needed.
- `NQ12-C07`: **supported**. Directly restates the exact evidence span: at 60 V fragmentor voltage the short-chain (C<5) PFAS signal was almost lost and 60 V was discarded. Method and compound scope match the gold record.
  Recommended text: No change needed.
- `NQ12-S02`: **supported**. A reasonable, appropriately qualified inference from the qualitative signal-loss observation; does not fabricate quantitative LOD/LOQ figures and correctly labeled supporting/qualitative.
  Recommended text: No change needed.
- `NQ12-L01`: **supported**. Accurately reflects the gold record's own 'limitation' field noting the absence of quantitative LOD/LOQ values in this study.
  Recommended text: No change needed.
- `NQ12-L02`: **supported**. Correctly scopes the quantitative findings to water matrices and the specific PFAS/PFCA subsets covered, without overgeneralizing to other classes or matrices.
  Recommended text: No change needed.

Reference-answer issues:
- NQ12_MMG001's exact_evidence_span is a garbled/flattened table extraction; the annotator's own does_not_support note flags ambiguity in whether the two numbers following Linearity represent LOD/LOQ, yet the record's own supported_claim and numerical_value fields assert a definitive LOD/LOQ interpretation without resolving or acknowledging that ambiguity for downstream consumers.
- The footnote marker 'a' in NQ12_MMG001's span is attached to 'Linearity a (µg L−1)' but the record's protocol_detail describes it generically as 'linearity values are referred to the final injection solution' without clarifying it does not necessarily extend to the Sensitivity/LOD/LOQ columns, which invites the kind of scope slippage seen in Model A's C01.

---

## NQ15

**Question:** How do electrolyte composition and pH-control choices affect interpretation of PFAS removal or degradation experiments?

**Must include:** Must treat buffer choice as a balance between pH control and interference risk; must connect to system or mechanism dependence.

**Must not claim:** Must not claim one exact buffer is universally correct for all PFAS removal experiments.

### Complete Gold Evidence

**NQ15_MMG001** (required_gold; `2023 - Unknown - Recent advances in electrochemical decontamination of perfluorinated compounds from water - a review.pdf`, chunk `17`)  
Scope: PFAS (general); water (electrochemical system); electrochemical oxidation; degradation  
> [SOURCE_TEXT_OMITTED sha256=11d5e985b964819de392f3c37bce7cd0f8ac12b30557a4c868dc94b78dec96d6].  
Supported claim metadata: Relying only on initial pH for assessing pH effects on PFAS degradation is likely to lead to a false interpretation.  
Does not support: The selected span does not itself state that real-time monitoring of pH near the anode is necessary.

**NQ15_MMG002** (optional_gold; `2023 - Unknown - Recent advances in electrochemical decontamination of perfluorinated compounds from water - a review.pdf`, chunk `16`)  
Scope: PFAS (general); water (electrochemical system); electro-oxidation; degradation  
> There is no reported consensus on the effects of pH to date.  
Supported claim metadata: There is no reported consensus on the effects of pH on PFAS electro-oxidation degradation; some studies claim acidic conditions facilitate degradation, while others find no pH effect.

**NQ15_MMG003** (optional_gold; `2023 - Unknown - Recent advances in electrochemical decontamination of perfluorinated compounds from water - a review.pdf`, chunk `18`)  
Scope: 6:2 fluorotelomer sulfonic acid; water; Ti/SnO2-Sb2O5-Bi2O3 anode electro-oxidation; degradation; 20; mg/L  
> ([SOURCE_TEXT_OMITTED sha256=28678ae005411876404eca828cb1f12d32e93eaf29cc4600596cba4de9757f43].  
Supported claim metadata: Degradation of 6:2 fluorotelomer sulfonic acid (20 mg/L) on a Ti/SnO2-Sb2O5-Bi2O3 anode declined with electrolyte in the order NaClO4 > NaCl > Na2SO4.

**NQ15_MMG004** (optional_gold; `2023 - Unknown - Recent advances in electrochemical decontamination of perfluorinated compounds from water - a review.pdf`, chunk `46`)  
Scope: PFOS; water; electro-coagulation with Fe anode; removal; 99.6, 93.7, 63.5, 45.4; %  
> [SOURCE_TEXT_OMITTED sha256=caf41aae6595cdd672b5f543c41bd708924c93499cc9ea9fd7ccd1c303d610b1].  
Supported claim metadata: PFOS removal by a Fe anode in electro-coagulation varied with electrolyte type: NaCl (99.6%) > Na2SO4 (93.7%) > NaNO3 (63.5%) > NaH2PO4 (45.4%).

**NQ15_MMG005** (optional_gold; `2023 - Alam - Experimental investigations of Per- and Poly-fluoroalkyl substances (PFAS) degradation by non-thermal plasma in aqueous solutions.pdf`, chunk `40`)  
Scope: PFOS; surface water / electrolyte solution; non-thermal plasma; degradation; 300, 320; µS/cm  
> [SOURCE_TEXT_OMITTED sha256=c5bb0683645357f76271c376a41e814c9de8e411db1089a8ee8b768043acb239].  
Supported claim metadata: With matched conductivity (300 vs 320 µS/cm), differing ion composition (monovalent vs monovalent+divalent cations) was hypothesized to affect PFOS degradation rate in non-thermal plasma treatment.

### Model A Reference Draft

In electrochemical PFAS degradation studies, pH effects are not consistent across the literature, and a review notes that there is no reported consensus on how pH influences electro‑oxidation; some studies report enhanced degradation under acidic conditions while others find no effect, making it difficult to generalize pH trends across systems [NQ15_MMG002]. Under these conditions, the same review cautions that relying only on the initial pH to interpret the role of pH in PFAS degradation is likely to lead to a false interpretation, and it specifies that real‑time monitoring of pH near the anode surface is needed to avoid misattributing performance changes to bulk pH alone [NQ15_MMG001]. For protocol design, this means pH‑control strategies must consider local and temporal pH, rather than a single starting value, when assigning mechanistic roles to pH.

Electrolyte composition is also shown to be an active variable rather than an inert background. In electro‑oxidation of 6:2 fluorotelomer sulfonic acid (20 mg/L) on a Ti/SnO2‑Sb2O5‑Bi2O3 anode, degradation performance decreased when the supporting electrolyte was changed in the order NaClO4 > NaCl > Na2SO4, demonstrating a strong dependence of degradation efficiency on electrolyte identity in that specific system [NQ15_MMG003]. In an electro‑coagulation process using a Fe anode, PFOS removal efficiencies differed markedly among electrolytes—NaCl (99.6%), Na2SO4 (93.7%), NaNO3 (63.5%), and NaH2PO4 (45.4%)—showing that the chemical components of the electrolyte can affect PFAS removal through different influencing mechanisms in electro‑coagulation [NQ15_MMG004]. In non‑thermal plasma treatment, when an electrolyte solution and a surface water matrix had comparable conductivities (300 vs 320 µS/cm), differing cation compositions (monovalent in the laboratory electrolyte versus monovalent plus divalent in surface water) were considered a possible cause of differing PFOS breakdown rates, indicating that ion composition can influence degradation even when conductivity is controlled [NQ15_MMG005].

Taken together, these results imply that any electrolyte or buffer chosen for pH control or conductivity in PFAS experiments can itself alter removal or degradation pathways and rates, so such choices must be treated as mechanistic variables rather than neutral background conditions [NQ15_MMG003; NQ15_MMG004; NQ15_MMG005]. Because pH effects on PFAS electro‑oxidation lack consensus and can be misinterpreted if only initial pH is considered [NQ15_MMG001; NQ15_MMG002], buffer selection involves balancing sufficient capacity to maintain the targeted pH against the risk that the buffer’s ions (as part of the electrolyte) will participate in or modify electro‑oxidation, electro‑coagulation, or plasma‑driven reactions. The available evidence, spanning electro‑oxidation, electro‑coagulation, and non‑thermal plasma systems, therefore supports treating electrolyte and pH‑control choices as system‑ and mechanism‑dependent design parameters whose impacts must be explicitly characterized in each experimental configuration, rather than assuming that any single electrolyte or buffer formulation is optimal across all PFAS removal or degradation studies [NQ15_MMG002; NQ15_MMG003; NQ15_MMG004; NQ15_MMG005].

Claims:

- `NQ15-C01` [core]: There is no reported consensus on the effects of pH on PFAS electro‑oxidation degradation across studies, which complicates comparison and interpretation of pH trends. (evidence: NQ15_MMG002)
- `NQ15-C02` [core]: For electrochemical PFAS degradation experiments, relying only on the initial bulk pH to assess the effects of pH is likely to lead to a false interpretation, and real‑time monitoring of pH near the anode surface is indicated as necessary to avoid misinterpretation. (evidence: NQ15_MMG001)
- `NQ15-C03` [core]: Because the chemical components in an electrolyte can affect PFAS removal through different influencing mechanisms in electro‑coagulation, electrolytes or buffers used for pH control or conductivity in such experiments should be treated as mechanistically active variables that can change removal performance rather than as inert background salts. (evidence: NQ15_MMG004)
- `NQ15-C04` [core]: Electrolyte identity strongly influences PFAS degradation efficiency in electrochemical oxidation, as shown by degradation of 6:2 fluorotelomer sulfonic acid (20 mg/L) on a Ti/SnO2‑Sb2O5‑Bi2O3 anode, where performance declined with electrolytes in the order NaClO4 > NaCl > Na2SO4. (evidence: NQ15_MMG003)
- `NQ15-C05` [core]: In Fe‑anode electro‑coagulation experiments, PFOS removal efficiencies depended strongly on electrolyte anion, with reported removals of 99.6% in NaCl, 93.7% in Na2SO4, 63.5% in NaNO3, and 45.4% in NaH2PO4. (evidence: NQ15_MMG004)
- `NQ15-C06` [supporting]: In non‑thermal plasma PFOS degradation tests where an electrolyte solution and surface water had comparable conductivities (300 versus 320 µS/cm), differing ion compositions—monovalent cations in the electrolyte solution versus monovalent plus divalent cations in the surface water—were considered a possible cause of differing PFOS breakdown rates, highlighting that electrolyte composition can influence degradation independently of conductivity. (evidence: NQ15_MMG005)
- `NQ15-C07` [supporting]: The divergent effects of electrolyte composition observed in electro‑oxidation of 6:2 fluorotelomer sulfonic acid, Fe‑anode electro‑coagulation of PFOS, and non‑thermal plasma degradation of PFOS indicate that electrolyte or buffer choices are system‑ and mechanism‑dependent and cannot be assumed to transfer universally between different PFAS treatment technologies. (evidence: NQ15_MMG003, NQ15_MMG004, NQ15_MMG005)
- `NQ15-C08` [limitation]: The available evidence on pH and electrolyte effects focuses on electrochemical and non‑thermal plasma treatments of PFAS and does not establish how specific named buffer formulations perform or interfere across all PFAS compounds and treatment methods. (evidence: NQ15_MMG001, NQ15_MMG002, NQ15_MMG003, NQ15_MMG004, NQ15_MMG005)

### Model B Verification

Overall verdict: **revise**

- `NQ15-C01`: **supported**. The exact_evidence_span ('There is no reported consensus on the effects of pH to date.') directly supports the claim as written. The claim appropriately omits the more detailed acidic-vs-no-effect split that appears only in the record's supported_claim paraphrase (not the exact span), keeping the claim conservative.
  Recommended text: There is no reported consensus on the effects of pH on PFAS electro-oxidation degradation across studies, which complicates comparison and interpretation of pH trends.
- `NQ15-C02`: **partially_supported**. The exact_evidence_span for NQ15_MMG001 only supports 'relying only on the initial pH ... is likely to lead to a false interpretation.' The record's own does_not_support field explicitly states: 'The selected span does not itself state that real-time monitoring of pH near the anode surface is necessary' — this detail lives only in the protocol_detail metadata field, not the quoted evidence. Claim C02 (and the matching sentence in the prose reference answer) attributes the 'real-time monitoring near the anode is necessary' assertion directly to this same evidence citation as though it were part of the quoted span, which the record itself flags as unsupported. This is a clear span/attribution mismatch that should be corrected or hedged.
  Recommended text: For electrochemical PFAS degradation experiments, relying only on the initial bulk pH to assess the effects of pH is likely to lead to a false interpretation. (Separately, the source material indicates — outside the directly quoted span — that real-time monitoring of pH near the anode may be needed to avoid this misinterpretation; this specific recommendation is not itself contained in the quoted evidence span.)
- `NQ15-C03`: **partially_supported**. NQ15_MMG004 supports that electrolyte chemical composition affects PFOS removal via different mechanisms in electro-coagulation. The claim extends this to 'electrolytes or buffers used for pH control' — but no evidence record mentions buffers or pH control in connection with MMG004's electro-coagulation findings; that record is about electrolyte type/removal, not pH buffering. This is a plausible inference used to satisfy the question's buffer framing, but it is broader than its cited evidence and should be labeled as an inference/synthesis rather than presented with the same directness as C05 (which restates the same evidence's numbers without the buffer extrapolation). Given its inferential/normative character ('should be treated as...'), this claim reads more as a supporting/interpretive claim than a core factual claim.
  Recommended text: The electrolyte-dependence observed in Fe-anode electro-coagulation of PFOS (NQ15_MMG004) suggests, by extension, that any electrolyte component — including ions introduced via a pH-control buffer — could similarly act as a mechanistically active variable in electro-coagulation systems, though the cited evidence itself addresses electrolyte type generally rather than buffers specifically.
- `NQ15-C04`: **supported**. Compound (6:2 FTS, 20 mg/L), matrix, anode material, electrolyte ordering (NaClO4 > NaCl > Na2SO4), and endpoint (degradation) all match the gold record's supported_claim and evidence fields.
  Recommended text: No change needed.
- `NQ15-C05`: **supported**. Numbers, units, electrolytes, compound (PFOS), matrix, method (Fe-anode electro-coagulation), and endpoint (removal) all match the gold record exactly.
  Recommended text: No change needed.
- `NQ15-C06`: **supported**. Correctly hedges the finding as a hypothesis ('considered a possible cause'), matches conductivity values and units, matrix framing (surface water vs electrolyte solution), and PFOS/non-thermal plasma attribution.
  Recommended text: No change needed.
- `NQ15-C07`: **supported**. This is a reasonable literature-level synthesis across three study-specific, non-universal records (each explicitly marked supports_universal_claim: 'no'), correctly scoped to 'these specific systems' and appropriately typed as supporting rather than core.
  Recommended text: No change needed.
- `NQ15-C08`: **supported**. Accurately describes the scope limitation of the evidence base (no named buffer formulations tested, limited to electrochemical/plasma treatments); consistent with limitation fields across all five records.
  Recommended text: No change needed.

Reference-answer issues:
- The task boundary requires the answer to 'treat buffer choice as a balance between pH control and interference risk,' but none of the five supplied gold records discuss buffers specifically — they discuss electrolyte composition/type and pH monitoring. Satisfying this boundary necessarily required Model A to infer a buffer-electrolyte equivalence not stated in any evidence span; this is a structural tension in the reference construction packet rather than a pure drafting error.
- NQ15_MMG001's protocol_detail field ('Real-time monitoring of pH near the anode surface is necessary to avoid misinterpretation') is presented as evidence content, but the record's own does_not_support field disclaims that the exact_evidence_span supports this detail. Including protocol_detail as citable content while simultaneously flagging it as unsupported by the span creates an inconsistency that invites exactly the kind of overreach seen in claim C02.

---

## NQ23

**Question:** What energy-consumption or energy-efficiency evidence is available for PFAS degradation methods, and can values be compared across studies?

**Must include:** Must identify the energy metric used, such as EEO, EEM, kWh/m3, kWh/g, electrical input, or energy per mass removed; must explain comparability limits.

**Must not claim:** Must not claim one universal energy-consumption number fairly represents all PFAS degradation methods.

### Complete Gold Evidence

**NQ23_MMG001** (required_gold; `2022 - Palma - [SOURCE_TEXT_OMITTED sha256=17b063b9343d837a62510f6a0711cd14cd4978461c53f7c695aecada64be6d6c].pdf`, chunk `46`)  
Scope: water; non-thermal plasma (NTP); removal; 1–100; kWh/m³  
> [SOURCE_TEXT_OMITTED sha256=e56b37a858688639c55242276d7e94a3b67a8e5e83de58060e449ff423098610].  
Supported claim metadata: Non-thermal plasma (NTP) processes have median energy consumptions in the 1–100 kWh/m³ range (as EEO), comparable to photo-Fenton and pure electrolytic AOPs.

**NQ23_MMG002** (required_gold; `2021 - Nau-Hix - [SOURCE_TEXT_OMITTED sha256=08b96669b712339edc5576317fb67415b737ce45decd34fcb2e66b658c632d83].pdf`, chunk `28`)  
Scope: PFOA, PFOS; groundwater; pilot-scale plasma reactor; removal; 9.2–31; average 16 ± 5.8; kWh/m³  
> [SOURCE_TEXT_OMITTED sha256=c1567affb204244f5b483d7ecc78c1a161a91dbca626c8031125f9ffa459041f]).  
Supported claim metadata: For pilot-scale plasma treatment of groundwater, EE/O for PFOA and PFOS removal ranged from 9.2 to 31 kWh/m³, with an average of 16 ± 5.8 kWh/m³.

**NQ23_MMG003** (required_gold; `2023 - Smith - Electrochemical Oxidation for Treatment of PFAS in Contaminated Water and Fractionated Foam─A Pilot-Scale Study.pdf`, chunk `33`)  
Scope: PFAS; contaminated water, fractionated foam; electrochemical oxidation (EO); degradation; 270 (50 L); 93 (150 L); kWh/m³  
> [SOURCE_TEXT_OMITTED sha256=41efa304c07178706d8f631de2ab3bce3b57c4bf72a90d4f106b21b846b55795].  
Supported claim metadata: Electrochemical oxidation energy consumption after 9 h was approximately 270 kWh/m³ for 50 L experiments and 93 kWh/m³ for 150 L experiments.  
Does not support: These are total energy consumption per volume, not EE/O (per-order) values, so they are not directly comparable to EE/O-reported studies.

**NQ23_MMG004** (required_gold; `2026 - Kumar - Degradation and defluorination of perfluorooctane sulfonate (PFOS) forever chemical in water using hydrodynamic cavitation treatment.pdf`, chunk `46`)  
Scope: PFOS; water; hydrodynamic cavitation (HC); defluorination; 7–598 (EEO); 17–286 (energy yield); kWh/m³/order; mg/kWh  
> [SOURCE_TEXT_OMITTED sha256=57f01e52432c3b441ce198b24ca4bf69f895fb4dc08b7ba6499580569d7611de].  
Supported claim metadata: In the cited hydrodynamic cavitation PFOS study context, the selected span reports EEO values ranging from 7 to 598 kWh/m3/order and energy yield from 17 to 286 mg/kWh.

**NQ23_MMG005** (required_gold; `2024 - Chen - Combining nonthermal N2 plasma with a denitrifying biofilm reactor for PFAS-contaminated wastewater remediation.pdf`, chunk `21`)  
Scope: PFOA, PFDA; wastewater; N₂ nonthermal plasma; degradation; 370 (PFOA); 260 (PFDA); kWh/m³  
> [SOURCE_TEXT_OMITTED sha256=f5233e6140d201d28af2a506bd29ae511a8a352399d5d18fef771f04d1a2f071]).  
Supported claim metadata: N₂ plasma treatment had EEO values of 370 kWh/m³ for PFOA and 260 kWh/m³ for PFDA, with degradation efficiencies of 45% (PFOA) and 60% (PFDA).

**NQ23_MMG006** (negative_gold; `2025 - Capodaglio - Prospects of Novel Technologies for PFAS Destruction in Water and Wastewater.pdf`, chunk `11`)  
Scope: water, wastewater; various PFAS destruction technologies; destruction  
> [SOURCE_TEXT_OMITTED sha256=9c74702320cc7d38dbb958d4adf8984609e199f46c5274f2124052f82ffa8fb0]).  
Supported claim metadata: The reported ranges in the referenced table show high variability, reflecting uncertainty and nonuniformity of experimental conditions across the respective studies.  
Does not support: Direct, unqualified cross-study comparison of energy values without accounting for differing experimental conditions.

**NQ23_MMG007** (optional_gold; `2026 - Chen - Ferrate-assisted nonthermal plasma for efficient PFOA degradation in landfill leachate - Mitigating bulk organic interference and enhancing.pdf`, chunk `35`)  
Scope: various technologies; degradation  
> [SOURCE_TEXT_OMITTED sha256=f6f48434e63810e6135f5782129b27b521b58706a8869e90c95a098df83e030c].  
Supported claim metadata: A consolidated comparison of reported EE/O values together with experimental parameters (water type, initial concentration, reactor scale, reaction time, removal/defluorination efficiency) supports context-aware cross-technology evaluation.  
Does not support: Provides no actual energy values itself; only points to a supplementary comparison table.

### Model A Reference Draft

Across PFAS degradation technologies, energy consumption is reported using different metrics, most commonly electrical energy per order (EEO or EE/O, kWh/m³ per log removal) and simpler specific energy consumptions (kWh/m³) or energy yields (mg removed per kWh). These values vary widely across methods and studies, and explicit evidence notes that differing experimental conditions limit direct comparability.

For non-thermal plasma (NTP) processes treating PFAS-contaminated water, a state-of-the-art review reports that, when energy is evaluated as electrical energy per order (EEO), NTP technologies fall in a “central zone” with median energy consumptions in the range of 1–100 kWh/m³, at approximately the same level as photo-Fenton and pure electrolytic advanced oxidation processes (AOPs). This range is characterized as median energy consumption and covers a broad span across different NTP configurations in water treatment applications. [NQ23_MMG001]

A pilot-scale plasma reactor applied in the field for rapid removal of PFOA and PFOS from groundwater reports EE/O values between 9.2 and 31 kWh/m³, with an average of 16 ± 5.8 kWh/m³ across four treatment conditions. The EE/O was defined from the total electrical energy consumed by the high-voltage power supplies, gas and liquid pumps, and rotating spark gap, divided by the treated volume and normalized by the change from initial to final PFOA and PFOS concentrations (driven below the USEPA health advisory level). [NQ23_MMG002]

For electrochemical oxidation (EO) applied at pilot scale to PFAS-contaminated water and fractionated foam, energy consumption after 9 h of treatment was reported as approximately 270 kWh/m³ for experiments treating 50 L and 93 kWh/m³ for experiments treating 150 L. In this study, the metric is total electrical energy per treated volume (kWh/m³) rather than EE/O, and the authors note that the energy consumption was mostly dependent on the treated volume. These values therefore quantify absolute specific energy input but are not normalized per order of contaminant removal. [NQ23_MMG003]

In a hydrodynamic cavitation (HC) study targeting PFOS degradation and defluorination in water, the reported EEO values ranged from 7 to 598 kWh/m³/order, and the energy yield (a complementary efficiency metric) varied between 17 and 286 mg/kWh. The very wide EEO range reflects changing experimental conditions and underscores the sensitivity of energy efficiency to operating parameters. [NQ23_MMG004]

For PFAS degradation using N₂ nonthermal plasma in wastewater, one study describes a primary challenge as low degradation efficiency combined with high energy consumption. Specifically, the EEO values were 370 kWh/m³ for PFOA and 260 kWh/m³ for PFDA, with degradation efficiencies of 45% for PFOA and 60% for PFDA. These values indicate that, under the reported conditions, a relatively high electrical energy input per treated volume was required to achieve only partial degradation. [NQ23_MMG005]

A broader review of novel PFAS destruction technologies in water and wastewater observes that reported energy-related ranges across studies show high variability, reflecting both uncertainty and nonuniformity of experimental conditions. This variability and nonuniformity mean that simple cross-study comparisons of energy consumption or efficiency values are not straightforward, because different studies operate under different water matrices, PFAS compounds and concentrations, reactor configurations, and performance targets. [NQ23_MMG006]

Consistent with this, another study notes that a consolidated comparison of reported EE/O values is only meaningful when accompanied by key experimental parameters such as water type, initial PFAS concentration, reactor scale, reaction time, and removal or defluorination efficiency. By presenting EE/O together with these contextual parameters, that work aims to enable a transparent and context-aware evaluation of energy performance across different technologies rather than a single, unqualified ranking based solely on EE/O numbers. [NQ23_MMG007]

Taken together, the available evidence shows that PFAS degradation methods such as non-thermal plasma, pilot-scale plasma reactors, electrochemical oxidation, and hydrodynamic cavitation have reported energy consumptions spanning from single-digit to several hundred kWh/m³ (or kWh/m³/order), and that some studies also report energy yields in mg removed per kWh. However, the metrics used (EEO vs total kWh/m³ vs mg/kWh), along with substantial variability and nonuniform experimental conditions, limit the ability to directly and fairly compare numerical energy-efficiency values across studies or to represent all PFAS degradation methods with any single, universal energy-consumption figure.

Claims:

- `NQ23-C01` [core]: Non-thermal plasma (NTP) processes for PFAS-contaminated water have median energy consumptions, expressed as electrical energy per order (EEO), in the range of 1–100 kWh/m³, placing them in a central zone of energy demand comparable to photo-Fenton and pure electrolytic advanced oxidation processes. (evidence: NQ23_MMG001)
- `NQ23-C02` [core]: In a field pilot-scale plasma reactor treating groundwater contaminated with PFOA and PFOS, the reported EE/O values ranged from 9.2 to 31 kWh/m³, with an average of 16 ± 5.8 kWh/m³ across four treatment conditions, based on the total energy consumed by the power supplies, pumps, and rotating spark gap normalized to treated volume and concentration reduction. (evidence: NQ23_MMG002)
- `NQ23-C03` [core]: A pilot-scale electrochemical oxidation study treating PFAS-contaminated water and fractionated foam reported total specific energy consumptions after 9 hours of treatment of approximately 270 kWh/m³ for experiments treating 50 L and 93 kWh/m³ for experiments treating 150 L, with energy use described as mostly dependent on treated volume rather than normalized per order of removal. (evidence: NQ23_MMG003)
- `NQ23-C04` [core]: In hydrodynamic cavitation treatment of PFOS-contaminated water, the reported electrical energy per order (EEO) ranged from 7 to 598 kWh/m³/order, while the energy yield ranged between 17 and 286 mg of PFOS treated per kWh, indicating a wide spread in energy efficiency under different conditions. (evidence: NQ23_MMG004)
- `NQ23-C05` [core]: For PFAS degradation in wastewater using N₂ nonthermal plasma, EEO values of 370 kWh/m³ for PFOA and 260 kWh/m³ for PFDA were reported, with corresponding degradation efficiencies of 45% for PFOA and 60% for PFDA, illustrating relatively high energy consumption per treated volume for partial degradation. (evidence: NQ23_MMG005)
- `NQ23-C06` [core]: A review of PFAS destruction technologies in water and wastewater notes that reported energy-related ranges across studies show high variability, reflecting uncertainty and nonuniform experimental conditions, which limits straightforward cross-study comparison of energy-consumption or efficiency values. (evidence: NQ23_MMG006)
- `NQ23-C07` [core]: Another study emphasizes that a consolidated comparison of reported EE/O values for different PFAS treatment technologies is only meaningful when presented together with key experimental parameters such as water type, initial PFAS concentration, reactor scale, reaction time, and removal or defluorination efficiency, to enable transparent and context-aware evaluation across technologies. (evidence: NQ23_MMG007)
- `NQ23-C08` [supporting]: The PFAS energy-efficiency evidence base uses multiple distinct metrics, including electrical energy per order (EEO or EE/O, kWh/m³), simple specific energy consumption per volume (kWh/m³), and energy yield (mg/kWh), so numerical values drawn from different metrics cannot be directly equated without accounting for how each is defined. (evidence: NQ23_MMG001, NQ23_MMG002, NQ23_MMG003, NQ23_MMG004)
- `NQ23-C09` [supporting]: Reported energy-consumption or efficiency values for PFAS degradation span from single-digit kWh/m³/order in some hydrodynamic cavitation conditions to several hundred kWh/m³ in N₂ nonthermal plasma and high end hydrodynamic cavitation cases, underscoring the wide variability in energy demand across technologies and operating conditions. (evidence: NQ23_MMG004, NQ23_MMG005)
- `NQ23-C10` [limitation]: Because of the high variability in reported energy ranges and the nonuniform experimental conditions across PFAS treatment studies, along with the use of different energy metrics, no single universal energy-consumption value can fairly represent all PFAS degradation methods, and cross-study comparisons must be interpreted in the specific context of each experiment. (evidence: NQ23_MMG001, NQ23_MMG003, NQ23_MMG004, NQ23_MMG006, NQ23_MMG007)

### Model B Verification

Overall verdict: **revise**

- `NQ23-C01`: **supported**. The exact_evidence_span directly states NTP processes fall in a 'central zone' with median EEO 1-100 kWh/m3, at the same level as photo-Fenton and pure electrolytic AOPs. Claim text matches span content and scope (median, range, comparator processes) without overreach.
  Recommended text: No change needed.
- `NQ23-C02`: **partially_supported**. The claim's numeric values (9.2-31 kWh/m3, average 16 ± 5.8 kWh/m3, four treatment conditions) are not present anywhere in the supplied exact_evidence_span for NQ23_MMG002, which only defines the variables of the EE/O equation (E, V, Ci, Cf) without stating any result values. Those numbers appear solely in the record's 'supported_claim' metadata field, not in the quoted document text. The description of what energy inputs comprise E (power supplies, pumps, rotating spark gap) and the concentration endpoint (below USEPA HAL) are genuinely supported by the span; the specific numeric range and average are not verifiable from the span alone.
  Recommended text: A field pilot-scale plasma reactor treating PFOA/PFOS-contaminated groundwater defines EE/O as the electrical energy consumed by the high-voltage power supplies, gas and liquid pumps, and rotating spark gap, divided by treated volume and normalized to the reduction from initial to final concentration (driven below the USEPA HAL); reported EE/O magnitudes should be treated as unverified against the supplied excerpt pending confirmation from the source results section.
- `NQ23-C03`: **unsupported**. The exact_evidence_span for NQ23_MMG003 reads only 'The energy consumption of EO can be calculated as described previously and as presented in eq S18,' a methods-section pointer with no numeric content whatsoever. The claim's figures (270 kWh/m3 for 50 L, 93 kWh/m3 for 150 L, 9 h duration, volume-dependence) all originate from the record's 'supported_claim' and 'protocol_detail' metadata fields, not from the quoted span itself. As supplied, this evidence span cannot verify any of the numeric or qualitative content in the claim.
  Recommended text: An electrochemical oxidation (EO) pilot study references an energy-consumption calculation method (eq S18) for treated PFAS water/foam; specific kWh/m3 values are asserted in accompanying annotation but are not present in the supplied excerpt and should be confirmed against the source before being cited as extracted values.
- `NQ23-C04`: **supported**. The exact_evidence_span states verbatim '[SOURCE_TEXT_OMITTED sha256=453f76d8bfc8ae3258b5477d84a9abd1886cdba49c8fa02a57c40e84e6717981],' matching the claim's values, units, and endpoint (PFOS degradation/defluorination via hydrodynamic cavitation) exactly.
  Recommended text: No change needed.
- `NQ23-C05`: **supported**. The exact_evidence_span states EEO values of 370 kWh/m3 (PFOA) and 260 kWh/m3 (PFDA) with 45% and 60% degradation efficiencies respectively, matching the claim precisely, including correct compound-to-value attribution.
  Recommended text: No change needed.
- `NQ23-C06`: **supported**. The exact_evidence_span supports the claim's content about high variability and nonuniform experimental conditions limiting comparison. However, NQ23_MMG006 is tagged 'negative_gold' and its 'does_not_support' field explicitly warns against unqualified direct comparison, which makes this more naturally a limitation-type claim (paralleling C10) than a 'core' finding claim, since it does not itself report a degradation method's energy value.
  Recommended text: Consider reclassifying as claim_type 'limitation' rather than 'core'; text itself is accurate as written.
- `NQ23-C07`: **supported**. The exact_evidence_span supports that a consolidated EE/O comparison is provided alongside contextual parameters (water type, concentration, reactor scale, reaction time, efficiency) in a supplementary table. The claim text correctly avoids implying any numeric values are given here (matching the gold record's 'does_not_support' note). Given evidence_type is 'optional_gold' and the span carries no concrete data, 'supporting' would be a more proportionate claim_type than 'core.'
  Recommended text: Consider reclassifying as claim_type 'supporting'; text itself is accurate as written.
- `NQ23-C08`: **supported**. The general claim that multiple distinct metrics (EEO/EE-O in kWh/m3, plain kWh/m3, mg/kWh) are used and are not directly interchangeable is well supported by the metric labels in the cited records' fields. NQ23_MMG005 also reports EEO in kWh/m3 and could have reasonably been included in evidence_ids for completeness, though its omission does not make the claim inaccurate.
  Recommended text: No substantive change needed; optionally add NQ23_MMG005 to evidence_ids since it also reports an EEO-in-kWh/m3 metric.
- `NQ23-C09`: **supported**. HC EEO range (7-598 kWh/m3/order) and N2 plasma EEO values (260-370 kWh/m3) are both directly quoted in their respective exact_evidence_spans, and the claim's qualitative summary ('single-digit' to 'several hundred') is a fair paraphrase of those ranges without overreach.
  Recommended text: No change needed.
- `NQ23-C10`: **partially_supported**. The limitation claim correctly synthesizes the comparability problem using MMG001, MMG004, MMG006, and MMG007, whose spans genuinely support variability/nonuniformity and metric-inconsistency themes. Its inclusion of NQ23_MMG003 as supporting evidence is weaker, since that record's exact_evidence_span contains no numeric or volume-dependence content to anchor the 'absolute kWh/m3' contrast being drawn; the volume-dependence detail relied upon is only in metadata, not the quoted span.
  Recommended text: Drop NQ23_MMG003 from evidence_ids, or caveat that its volume-dependence detail is drawn from unverified metadata rather than the quoted span; otherwise the synthesis and must_not_claim compliance are sound.

Reference-answer issues:
- For NQ23_MMG002 and NQ23_MMG003, the gold packet's 'exact_evidence_span' field does not contain the numeric values asserted in the same record's 'supported_claim' field (EE/O range/average for MMG002; kWh/m3 totals for MMG003). This is a construction issue in the gold packet itself: a verifier or downstream model relying on 'supported_claim' as if it were quoted text will present unverifiable numbers as directly extracted evidence. This should be corrected by either sourcing an exact_evidence_span that actually contains the results-table figures, or by explicitly flagging these two records as requiring external table verification.

---

## NQ24

**Question:** How do reported activated-carbon PFAS adsorption capacities differ between batch and column studies?

**Must include:** Must distinguish carbon type, PFAS chain length or compound, test conditions, endpoint, capacity units, and capacity values when values are presented.

**Must not claim:** Must not claim activated carbon has one fixed PFAS adsorption capacity across compounds and matrices.

### Complete Gold Evidence

**NQ24_MMG001** (required_gold; `2023 - Shaikh - [SOURCE_TEXT_OMITTED sha256=2fdd9fc6551a585909adde8f813316c5decdcef71d2dce5450f882ef211a386b].pdf`, chunk `60`)  
Scope: PFOA; aqueous media (column run with background water matrix); CTAB-impregnated activated carbon; adsorption; 5.71 (column, Thomas); 6.85 (batch, Langmuir); mg/g  
> [SOURCE_TEXT_OMITTED sha256=8a2066fbeea08688bf57fa41b3f0688afb1b08ea133d3c4cf9e11bfd54f3a9c2]).  
Supported claim metadata: In this study, the maximum column adsorption capacity obtained through the Thomas model was 5.71 mg/g, marginally lower than the batch Langmuir isotherm Qe of 6.85 mg/g; the difference was attributed to the background water matrix during the column run and the larger adsorbent size used in the column study.  
Does not support: Does not provide a general rule for all activated carbons or other PFAS; single-study, single-compound comparison.

### Model A Reference Draft

In a study of PFOA adsorption onto CTAB‑impregnated activated carbon, the maximum adsorption capacity estimated from a fixed‑bed column (Thomas model) was 5.71 mg/g, which was marginally lower than the batch equilibrium capacity from the Langmuir isotherm (Qe = 6.85 mg/g). The authors attributed this lower column capacity primarily to (i) the presence of a background water matrix during the column run and (ii) the use of larger adsorbent particles in the column (125–500 μm) compared with the batch experiments (125–250 μm). This provides a specific example where, under the reported aqueous conditions, the modeled batch adsorption capacity for PFOA slightly exceeded the modeled column capacity for the same CTAB‑impregnated activated carbon.

Claims:

- `NQ24-C01` [core]: For PFOA adsorption onto CTAB‑impregnated activated carbon, the maximum adsorption capacity obtained from a fixed‑bed column using the Thomas model was 5.71 mg/g, which was marginally lower than the batch equilibrium Langmuir isotherm capacity Qe of 6.85 mg/g. (evidence: NQ24_MMG001)
- `NQ24-C02` [supporting]: In this PFOA–CTAB‑impregnated activated carbon study, the lower column capacity relative to batch was mainly attributed to the presence of a background water matrix during the column run and the larger adsorbent particle size used in the column compared with the batch tests. (evidence: NQ24_MMG001)

### Model B Verification

Overall verdict: **approve**

- `NQ24-C01`: **supported**. The evidence span states the Thomas-model column capacity was 5.71 mg/g, 'marginally lower' than the Langmuir isotherm Qe of 6.85 mg/g. The claim reproduces these exact values, units, models, and the compound (PFOA) and material (CTAB-impregnated activated carbon) correctly, and the conditions_and_scope field correctly captures the particle-size and matrix distinctions given in the evidence's protocol_detail field. Labeling this 'core' is reasonable since it is the only quantitative batch-vs-column comparison in the supplied gold set and directly answers the question for this single system.
  Recommended text: For PFOA adsorption onto CTAB-impregnated activated carbon, the maximum adsorption capacity obtained from a fixed-bed column using the Thomas model was 5.71 mg/g, which was marginally lower than the batch equilibrium Langmuir isotherm capacity Qe of 6.85 mg/g.
- `NQ24-C02`: **supported**. The evidence explicitly attributes the lower column capacity to '(a) the presence of the background water matrix during the column run and (b) the size of the adsorbent was bigger... than used in the batch...study.' The claim restates both reasons accurately without overgeneralizing beyond this single study, and correctly labels it 'supporting' rather than 'core' since it explains rather than reports the primary numeric finding.
  Recommended text: In this PFOA-CTAB-impregnated activated carbon study, the lower column capacity relative to batch was mainly attributed to the presence of a background water matrix during the column run and the larger adsorbent particle size used in the column compared with the batch tests.

---

## NQ26

**Question:** What membrane-based PFAS treatment routes are described, and which routes separate or concentrate PFAS rather than destroy or transform them?

**Must include:** Must distinguish pressure-driven separation, NF/RO, modified membranes, electrical membranes, and any destructive membrane-coupled process.

**Must not claim:** Must not equate membrane separation or retention with PFAS destruction.

### Complete Gold Evidence

**NQ26_MMG001** (required_gold; `2022 - Liang - [SOURCE_TEXT_OMITTED sha256=a239c312767f1bdb2975f7bea56396014ec3147356c1046b284baf9e9fa898e6].pdf`, chunk `35`)  
Scope: PFAS; water; reverse osmosis, nanofiltration; separation  
> [SOURCE_TEXT_OMITTED sha256=03339764a1bb7d62ce6bf604ab3e477cc1f3961390fa4d7ccaca7b6047668851] ].  
Supported claim metadata: Reverse osmosis and nanofiltration are described as traditional separation technologies that produce a concentrated PFAS waste stream and have been demonstrated in tandem with destruction technologies.

**NQ26_MMG002** (required_gold; `2025 - Liu - [SOURCE_TEXT_OMITTED sha256=fc3f889e749d4d397e10a1a334a5e99284e0565490997ebfaa4e09a9eec6fe32].pdf`, chunk `21`)  
Scope: PFAS; water; membrane filtration, membrane distillation, adsorption; separation  
> [SOURCE_TEXT_OMITTED sha256=83cad68bd45d2078d6111dab03fa6fe6edf58ebe23a550abae1a931d9038d69b].  
Supported claim metadata: The cited review states that filtration, adsorption, and membrane distillation can only concentrate PFAS, while degradation can subsequently be used to remove PFAS.

**NQ26_MMG003** (required_gold; `2023 - Sivagami - Electrochemical-based approaches for the treatment of forever chemicals - Removal of perfluoroalkyl and polyfluoroalkyl substances (PFAS) from.pdf`, chunk `58`)  
Scope: PFAS; water; membrane-based processes; separation  
> Another severe limitation of membrane-based processes is that they do not degrade PFAS;  
Supported claim metadata: Membrane-based processes do not degrade PFAS, which is described as a limitation.

**NQ26_MMG004** (required_gold; `2024 - Pervez - [SOURCE_TEXT_OMITTED sha256=22ad5d5418c6d7cd8200d696c2e21c61fd694f0587eb218eb87da22954f6100c].pdf`, chunk `4`)  
Scope: PFAS (short- and long-chain); water; nanofiltration, reverse osmosis; separation; >90; % rejection  
> [SOURCE_TEXT_OMITTED sha256=1c93c6bbc04d9e9b8e5fb4c698395a40b38ca869ce2ce319f451e9e4e5d0a23b] ].  
Supported claim metadata: High-pressure membrane filtration (NF and RO) effectively separates both short- and long-chain PFAS with rejection efficiencies typically exceeding 90%.

**NQ26_MMG005** (required_gold; `2025 - Liu - [SOURCE_TEXT_OMITTED sha256=fc3f889e749d4d397e10a1a334a5e99284e0565490997ebfaa4e09a9eec6fe32].pdf`, chunk `43`)  
Scope: PFAS; water; filtration, membrane distillation, forward osmosis; separation  
> [SOURCE_TEXT_OMITTED sha256=9f34e97314f422560b564640d3916e33d8a593d42ff92ca15f3ea9c5a242ec23].  
Supported claim metadata: Filtration, membrane distillation, and forward osmosis are classified as concentration treatments, distinct from degradation treatments such as electrodegradation and biodegradation.

**NQ26_MMG006** (optional_gold; `2025 - Liu - [SOURCE_TEXT_OMITTED sha256=fc3f889e749d4d397e10a1a334a5e99284e0565490997ebfaa4e09a9eec6fe32].pdf`, chunk `21`)  
Scope: PFAS; water; membrane-assisted chemical degradation; degradation  
> [SOURCE_TEXT_OMITTED sha256=f0b14257912b476dc875c738a98322b9a4eb2b8a25724c454b691b321ced0646].  
Supported claim metadata: Membrane-assisted degradation first adsorbs PFAS onto a membrane (optionally with catalysts) and then degrades them under light or an electric field, representing a destructive membrane route.

**NQ26_MMG007** (negative_gold; `2021 - Ryan - Electrochemical technologies for per- and polyfluoroalkyl substances mitigation in.pdf`, chunk `51`)  
Scope: PFAS; water; microfiltration, ultrafiltration; removal  
> [SOURCE_TEXT_OMITTED sha256=efac268ac1e59907dde01bf057d08de85e3cf7451a581ce00c8ee059a00566a0];  
Supported claim metadata: Low-pressure membranes such as microfiltration and ultrafiltration poorly remove PFAS.  
Does not support: Does not support that these membranes effectively separate or concentrate PFAS.

**NQ26_MMG008** (optional_gold; `2021 - Groele - An investigation of plasma-driven decomposition of per- and polyfluoroalkyl substances (PFAS) in raw contaminated groundwater.pdf`, chunk `7`)  
Scope: PFAS; groundwater; membrane processes; separation  
> [SOURCE_TEXT_OMITTED sha256=7dbda52a0949419af622b6a207b79e15153cbde0e9b684ab90530f14e23c146b].  
Supported claim metadata: In the described membrane processes, a concentrate is sent to an evaporation pool and the resulting residue can be collected and incinerated.  
Does not support: Does not by itself establish that membranes separate PFAS rather than transform them; the span concerns downstream residue handling, not separation efficacy.

### Model A Reference Draft

The literature describes several membrane-based treatment routes for PFAS-contaminated water and distinguishes between those that primarily separate/concentrate PFAS and those that are coupled to destructive processes.

High-pressure membrane filtration using nanoporous nanofiltration (NF) and reverse osmosis (RO) is identified as a traditional separation approach. These NF/RO systems are reported to be highly effective at separating both short- and long-chain PFAS, with typical rejection efficiencies exceeding 90%, and are explicitly described as producing a concentrated PFAS waste stream rather than degrading the compounds. Because they do not destroy PFAS, NF and RO are commonly operated in tandem with a separate destruction technology.

More generally, membrane-based processes such as filtration, adsorption onto membranes, membrane distillation, and forward osmosis are classified as concentration or separation treatments. The available review evidence states that these approaches can only concentrate PFAS and that this inability to degrade PFAS is a key limitation of membrane-based processes. To achieve actual PFAS removal by transformation, these concentrating membrane routes are proposed to be combined with separate degradation processes such as electrodegradation or biodegradation. Operationally, membrane concentrates may then be managed by downstream destructive steps such as sending the concentrate to an evaporation pool and subsequently incinerating the collected residue.

By contrast, a distinct membrane-coupled destructive route—membrane-assisted degradation—is described. In this approach, PFAS are first adsorbed onto a membrane, which can incorporate catalysts, and are then degraded under light or an applied electric field. This membrane-assisted degradation differs from simple membrane separation in that the membrane functions both as a concentrating interface and as a platform enabling chemical degradation, including under electrically driven conditions.

Low-pressure membrane processes such as microfiltration and ultrafiltration are noted to remove PFAS poorly and therefore are not considered effective routes for PFAS separation or concentration compared with the high-pressure or tailored membrane configurations above.

Taken together, the described membrane-based routes fall into two main classes: (i) pressure-driven and related membrane processes (NF/RO, general filtration, membrane distillation, forward osmosis, and adsorption-based membranes) that separate or concentrate PFAS without degrading them and thus require additional destruction technologies; and (ii) membrane-coupled destructive routes such as membrane-assisted degradation under light or electric fields, where PFAS are first concentrated on a membrane and then chemically degraded.

Claims:

- `NQ26-C01` [core]: High-pressure membrane filtration processes using nanoporous nanofiltration (NF) and reverse osmosis (RO) are described as traditional separation technologies that effectively separate short- and long-chain PFAS from water, with rejection efficiencies typically exceeding 90%, and they produce a concentrated PFAS waste stream rather than degrading the PFAS. (evidence: NQ26_MMG001, NQ26_MMG004, NQ26_MMG003)
- `NQ26-C02` [core]: Filtration, membrane distillation, and forward osmosis are classified as concentration (separation) treatments for PFAS-contaminated water that can only concentrate PFAS and therefore need to be combined with separate degradation processes such as electrodegradation or biodegradation for PFAS destruction. (evidence: NQ26_MMG002, NQ26_MMG005)
- `NQ26-C03` [core]: Membrane-based processes as a class are reported to have a severe limitation in that they do not degrade PFAS and instead function mainly to separate or concentrate PFAS. (evidence: NQ26_MMG003, NQ26_MMG002, NQ26_MMG005)
- `NQ26-C04` [core]: A membrane-assisted degradation route is described in which [SOURCE_TEXT_OMITTED sha256=c6dccf2785b3b7ced7d6eaf4d253403bd464a74f2516d880fc8baced246561f6], distinguishing this approach from purely separative membrane treatments. (evidence: NQ26_MMG006)
- `NQ26-C05` [core]: Membrane separation processes that concentrate PFAS, including NF and RO, are implemented in practice in tandem with separate destruction technologies, such as sending the PFAS-rich concentrate to an evaporation pool and then collecting and incinerating the residue. (evidence: NQ26_MMG001, NQ26_MMG008)
- `NQ26-C06` [core]: Adsorption onto membranes, when used without a subsequent degradation step, is treated as a concentration or separation operation for PFAS rather than a destructive treatment. (evidence: NQ26_MMG002, NQ26_MMG006)
- `NQ26-C07` [supporting]: Low-pressure membranes such as microfiltration and ultrafiltration are reported to poorly remove PFAS and are therefore not effective PFAS separation or concentration routes compared with high-pressure membranes. (evidence: NQ26_MMG007)

### Model B Verification

Overall verdict: **revise**

- `NQ26-C01`: **supported**. MMG001 and MMG004 directly support the NF/RO-specific claims (traditional separation tech, concentrated waste stream, >90% rejection of short/long-chain PFAS). MMG003, however, is a general statement about 'membrane-based processes' as a class, not specific to NF/RO; using it to support the NF/RO-specific 'rather than degrading' clause is a mild generality mismatch, though logically consistent since NF/RO fall under that class.
  Recommended text: High-pressure membrane filtration processes using nanoporous NF and RO are described as traditional separation technologies that effectively separate short- and long-chain PFAS from water, with rejection efficiencies typically exceeding 90%, and produce a concentrated PFAS waste stream; membrane-based processes as a class (which includes NF/RO) are separately noted not to degrade PFAS.
- `NQ26-C02`: **supported**. MMG002 supports filtration and membrane distillation as concentrate-only methods; MMG005 supports filtration, membrane distillation, and forward osmosis as concentration treatments distinct from degradation methods (electrodegradation, biodegradation). The combined claim text is fully backed by the two spans.
  Recommended text: Filtration, membrane distillation, and forward osmosis are classified as concentration (separation) treatments for PFAS-contaminated water that can only concentrate PFAS and therefore need to be combined with separate degradation processes such as electrodegradation or biodegradation for PFAS destruction.
- `NQ26-C03`: **supported**. Each cited span supports the general statement that membrane-based processes do not degrade PFAS and mainly separate/concentrate it. However, this claim substantially restates content already covered by C01 and C02, raising a question of whether it should be 'supporting' rather than a distinct 'core' claim; it does not introduce new evidence-backed content beyond a summary framing.
  Recommended text: Membrane-based processes as a class are reported to have a severe limitation in that they do not degrade PFAS and instead function mainly to separate or concentrate PFAS (supporting/summary claim rather than a new core finding).
- `NQ26-C04`: **supported**. Directly paraphrases the exact span: PFAS adsorbed onto membrane (catalysts optional), then degraded under light or electric field. Correctly labeled as a destructive route distinct from separative membrane treatments, consistent with the evidence's supported_claim.
  Recommended text: A membrane-assisted degradation route is described in which [SOURCE_TEXT_OMITTED sha256=c6dccf2785b3b7ced7d6eaf4d253403bd464a74f2516d880fc8baced246561f6], distinguishing this approach from purely separative membrane treatments.
- `NQ26-C05`: **partially_supported**. MMG001 supports NF/RO being deployed in tandem with a destruction technology, but does not mention an evaporation pool or incineration mechanism. MMG008 comes from an unrelated paper (Groele, plasma-driven decomposition) discussing generic 'membrane processes' concentrate handling (evaporation pool, incineration) in a context contrasting with GAC/carbon incineration disposal — it is not shown to specifically describe NF/RO. The evidence record's own 'does_not_support' field warns the span concerns downstream residue handling, not separation efficacy, and by extension should not be read as establishing that NF/RO specifically use this evaporation/incineration pathway. The claim's phrase 'including NF and RO, are implemented in practice... such as sending the PFAS-rich concentrate to an evaporation pool' improperly fuses two distinct sources' technology scopes into one attribution.
  Recommended text: Membrane separation processes that concentrate PFAS, including NF and RO, are described as being implemented in tandem with separate destruction technologies (MMG001). Separately, one review of membrane processes in general notes that resulting concentrate can be sent to an evaporation pool with the residue then collected and incinerated (MMG008), though this span does not specifically identify NF/RO as the membrane process referenced.
- `NQ26-C06`: **partially_supported**. MMG006 directly supports that adsorption onto a membrane, without the subsequent light/electric-field step, is a concentrating (non-destructive) stage. MMG002's 'adsorption,' however, is listed as one of several 'abovementioned treatment methods (filtration, adsorption, and membrane distillation)' in a review section — the evidence record does not establish that this adsorption is onto a membrane specifically, versus being a distinct standalone adsorption technology (e.g., GAC or ion exchange) grouped alongside membrane methods. Treating it as 'adsorption onto membranes' overextends the source.
  Recommended text: Adsorption onto membranes, when used without a subsequent degradation step (as in the initial stage of membrane-assisted degradation), is treated as a concentration or separation operation for PFAS rather than a destructive treatment; a separate review also lists adsorption generally (not specified as membrane-based) among concentrate-only PFAS treatment methods.
- `NQ26-C07`: **supported**. Directly matches the exact span: low-pressure MF/UF poorly remove PFAS. Correctly typed as 'supporting' rather than core, and does not overclaim that these membranes are excluded from the treatment landscape beyond what the negative-gold record states.
  Recommended text: Low-pressure membranes such as microfiltration and ultrafiltration are reported to poorly remove PFAS and are therefore not effective PFAS separation or concentration routes compared with high-pressure membranes.

Reference-answer issues:
- Claim C05 conflates two distinct source papers (MMG001 on NF/RO tandem-with-destruction, and MMG008 on generic membrane-process concentrate disposal from an unrelated plasma-decomposition paper) into a single attribution implying NF/RO specifically use an evaporation-pool/incineration pathway, which the evidence does not establish.
- Claim C06 attributes MMG002's general 'adsorption' treatment method specifically to membrane-based adsorption, though the source span does not confirm the adsorption discussed is membrane-based rather than a separate technology grouped in the same list.
- Claim C03 substantially duplicates the destruction-limitation content already established in C01 and C02, raising an atomicity/redundancy concern for a 'core' claim designation.

---

## WF10_002

**Question:** When comparing membrane filtration, gliding arc plasma, and supercritical water oxidation for PFAS treatment, which reported endpoints should be kept separate?

**Must include:** Keep removal, separation, adsorption, degradation, defluorination, mineralization, destruction, byproduct formation, and mass-balance evidence separate.

**Must not claim:** Do not convert a condition-specific finding into a universal PFAS treatment claim.

### Complete Gold Evidence

**WF10_002_MMG001** (required_gold; `2020 - Lewis - [SOURCE_TEXT_OMITTED sha256=554163c7d2b072061858872c0b12860ea2a00a7012240bcdfef986aa2791bcf7] †.pdf`, chunk `18`)  
Scope: PFOA; PFOS; PFNA; 8:2 FtS; water; gliding arc plasma (GAP); removal (target analyte disappearance); degradation (degradation product formation); defluorination; other (energy costs)  
> [SOURCE_TEXT_OMITTED sha256=8c6eeb4d26f0fa59429686e5c8a0bd616b5f15acf6f58113be34d3afe8d09f4f].  
Supported claim metadata: For gliding arc plasma treatment of PFAS-contaminated water, four distinct endpoints—disappearance of target analyte, formation of degradation products, defluorination, and energy costs—must be measured and co-aligned, since examining only one or two is insufficient to determine whether PFAS are truly destroyed.  
Does not support: Does not establish endpoints for membrane filtration or SCWO; does not provide numerical endpoint values.

**WF10_002_MMG002** (optional_gold; `2024 - Shaji - [SOURCE_TEXT_OMITTED sha256=ffe789f2dc149533ddda1da2c60b4ba55d4ca6d1efaa6d32ed2a8cada448c791].pdf`, chunk `8`)  
Scope: water; supercritical water oxidation (SCWO); [SOURCE_TEXT_OMITTED sha256=88b02391e2884f778014f012127be5b391b0134372b9a93ba99cd62268bd1729]].  
Supported claim metadata: The cited span reports that SCWO, along with sonolysis, has shown potential for PFAS mineralization with minimal short-chain PFAS formation, and that increased mineralization with rising reaction temperature has been observed in SCWO.  
Does not support: Does not provide numerical mineralization values; does not address membrane filtration; does not entail that SCWO mineralization is distinct from defluorination beyond the term 'mineralizing' used in the span.

### Model A Reference Draft

In the gliding arc plasma (GAP) study, the authors explicitly track four separate metrics: disappearance of the target PFAS analyte(s), formation of degradation products, defluorination, and energy cost, and they emphasize that these must be evaluated together rather than collapsed into a single measure of “destruction.” This means that, when comparing GAP to membrane filtration or supercritical water oxidation (SCWO), disappearance/removal of the parent PFAS (a removal/separation-type endpoint) must be kept distinct from degradation-product formation (a degradation/byproduct-formation endpoint), and both must be distinguished from defluorination (release of fluoride from C–F bonds) and from operational metrics such as energy consumption.

For SCWO, the reported focus is on PFAS mineralization, with increased mineralization at higher reaction temperatures and minimal short-chain PFAS formation. Here, mineralization is a distinct endpoint from the generation of shorter-chain PFAS byproducts, which is characterized qualitatively as minimal. Because the GAP study does not report mineralization and the SCWO discussion does not report defluorination or target-analyte disappearance, mineralization endpoints for SCWO should not be conflated with the disappearance/removal and defluorination endpoints used in the GAP system.

Taken together, the supplied evidence supports keeping the following endpoint categories analytically separate when comparing membrane filtration, GAP, and SCWO: (i) removal/separation-type endpoints such as disappearance of the parent PFAS from the treated stream; (ii) adsorption/separation-related endpoints (relevant conceptually for membrane processes but not quantified in the supplied records); (iii) degradation endpoints, reflected by formation of non-parent degradation products; (iv) defluorination endpoints, reflected by fluoride release; (v) mineralization endpoints, as reported for SCWO; (vi) byproduct-formation endpoints, such as short-chain PFAS formation; and (vii) any overall destruction or mass-balance interpretation, which in the GAP study is derived from co-aligning disappearance, degradation products, and defluorination rather than from a single direct measurement.

Claims:

- `WF10_002-C01` [core]: In the reported gliding arc plasma PFAS treatment system, disappearance of the target analyte(s), formation of degradation products, defluorination, and energy costs are measured as distinct endpoints rather than being collapsed into a single destruction metric. (evidence: WF10_002_MMG001)
- `WF10_002-C02` [core]: For the GAP system, disappearance of the parent PFAS (a removal-type endpoint) must be distinguished from formation of degradation products (a degradation/byproduct-formation endpoint), because the study states that multiple measurements must be co-aligned to demonstrate PFAS destruction versus mere alteration. (evidence: WF10_002_MMG001)
- `WF10_002-C03` [core]: Defluorination in the GAP study is treated as an endpoint separate from both target-analyte disappearance and degradation-product formation, and all three chemical endpoints must be considered together to assess whether PFAS are destroyed. (evidence: WF10_002_MMG001)
- `WF10_002-C04` [core]: In the SCWO context, mineralization of PFAS is reported as a distinct endpoint, with increased mineralization at higher reaction temperatures, and this mineralization endpoint is differentiated from short-chain PFAS byproduct formation, which is described as minimal. (evidence: WF10_002_MMG002)
- `WF10_002-C05` [core]: When comparing GAP and SCWO, mineralization endpoints reported for SCWO should not be conflated with the disappearance, degradation-product formation, or defluorination endpoints reported for GAP, because the two studies emphasize different specific measurements. (evidence: WF10_002_MMG001, WF10_002_MMG002)
- `WF10_002-C06` [core]: Any overall judgment of PFAS destruction or fate in the GAP system is not a single measured endpoint but an interpretation that integrates separate measurements of disappearance, degradation products, and defluorination, so this integrative destruction or mass-balance view must be kept conceptually distinct from the individual endpoints themselves. (evidence: WF10_002_MMG001)
- `WF10_002-S01` [supporting]: In the GAP study, energy cost is explicitly tracked as an operational endpoint that is separate from chemical endpoints such as target-analyte disappearance, degradation products, and defluorination. (evidence: WF10_002_MMG001)
- `WF10_002-S02` [supporting]: The SCWO discussion highlights minimal formation of short-chain PFAS during mineralization, indicating that mineralization and byproduct formation are treated as separate outcome categories in that context. (evidence: WF10_002_MMG002)
- `WF10_002-L01` [limitation]: The supplied evidence does not describe separation or adsorption endpoints, nor any membrane-filtration experiments, so separation and adsorption must be recognized as distinct, but currently unquantified, endpoint categories when comparing membrane filtration with GAP and SCWO. (evidence: WF10_002_MMG001, WF10_002_MMG002)
- `WF10_002-L02` [limitation]: Although the GAP study combines disappearance, degradation products, and defluorination conceptually to argue that PFAS are destroyed rather than merely altered, it does not present a complete quantitative mass balance, so mass-balance evidence remains methodologically distinct and is not fully characterized in the supplied records. (evidence: WF10_002_MMG001)

### Model B Verification

Overall verdict: **approve**

- `WF10_002-C01`: **supported**. The raw span lists the four measured quantities (disappearance, degradation products, defluorination, energy costs); the gold record's supported_claim field explicitly adds the 'must be co-aligned...insufficient' framing, which the claim paraphrases as 'rather than being collapsed into a single destruction metric.' This is a faithful paraphrase of gold-endorsed interpretation, not an unsupported addition.
  Recommended text: No change needed.
- `WF10_002-C02`: **supported**. Correctly distinguishes disappearance (removal-type) from degradation-product formation, grounded in the evidence's explicit listing and its co-alignment/insufficiency statement. Substantively overlaps with C01 and C06, which could be consolidated, but is not factually incorrect.
  Recommended text: No change needed; consider merging with C01/C06 to reduce redundancy.
- `WF10_002-C03`: **supported**. Defluorination is listed as a separate measured quantity in the span, and protocol_detail confirms it was measured via a fluoride-selective probe distinct from LC-MS/MS. Claim is accurate but again overlaps substantially with C01/C02.
  Recommended text: No change needed; consider merging with C01 to reduce redundancy.
- `WF10_002-C04`: **supported**. Matches the span: SCWO shows potential for mineralization with minimal short-chain PFAS formation, and mineralization increases with reaction temperature. Correctly treats mineralization and byproduct formation as distinct endpoint categories, consistent with the gold's endpoint field ('mineralization') and protocol_detail.
  Recommended text: No change needed.
- `WF10_002-C05`: **supported**. The cross-technology non-conflation claim is a reasonable synthesis of both records. However, the claim's phrasing 'the two studies emphasize different specific measurements' implicitly treats MMG002 as a dedicated SCWO study, when in fact the doc_id shows this SCWO information is a secondary citation embedded within a gliding-arc-plasma mineralization paper (Shaji 2024), not a primary SCWO study. This does not misstate the endpoint content but slightly obscures evidentiary provenance.
  Recommended text: When comparing GAP and SCWO, mineralization endpoints reported for SCWO in the literature should not be conflated with the disappearance, degradation-product formation, or defluorination endpoints reported for the GAP system, because these are different specific measurements reported in different sources.
- `WF10_002-C06`: **supported**. Accurately reflects the gold's limitation field ('Examining a single measurement is insufficient; data must be co-aligned to demonstrate destruction vs. alteration') and appropriately maps this onto the must_include boundary term 'destruction'/'mass-balance.' Overlaps conceptually with C01.
  Recommended text: No change needed; consider merging with C01.
- `WF10_002-S01`: **supported**. Energy cost is explicitly listed alongside the three chemical endpoints in the span; correctly classified as an operational (non-chemical) endpoint kept separate.
  Recommended text: No change needed.
- `WF10_002-S02`: **supported**. Matches span language ('minimal short-chain PFAS formation') and correctly treats byproduct formation as separate from the mineralization endpoint. Appropriately scoped to 'that context' rather than generalized.
  Recommended text: No change needed.
- `WF10_002-L01`: **supported**. Correctly identifies that neither record addresses membrane filtration, separation, or adsorption endpoints, and appropriately frames these as unquantified categories rather than fabricating data. This is the correct handling of a question that names a technology (membrane filtration) with zero supporting gold evidence.
  Recommended text: No change needed.
- `WF10_002-L02`: **supported**. Correctly notes that no explicit quantitative mass-balance (e.g., fluorine/carbon closure) is reported in MMG001, only qualitative co-alignment of disappearance/degradation-products/defluorination to argue destruction. Appropriately hedged as a limitation rather than asserting a mass balance was performed.
  Recommended text: No change needed.

Reference-answer issues:
- The gold evidence set contains no membrane-filtration record even though the question explicitly asks for a three-way comparison including membrane filtration; this is a coverage gap in the supplied gold set rather than a defect in Model A's draft, and Model A handled it correctly by downgrading answerability and flagging separation/adsorption endpoints as unquantified rather than inventing data.

---

## WF10_021

**Question:** When screening activated-carbon or biochar PFAS adsorption studies, what matrix and regeneration gaps should be checked?

**Must include:** Use limitation, uncertainty, caveat, and negative evidence to avoid overclaiming beyond the reported study scope.

**Must not claim:** Do not convert a condition-specific finding into a universal PFAS treatment claim.

### Complete Gold Evidence

**WF10_021_MMG001** (negative_gold; `2026 - Sadmani - [SOURCE_TEXT_OMITTED sha256=e2dd4fda49f066575cf9c26093f2c0f0108101becaa30a85e582d06a6552c102].pdf`, chunk `52`)  
Scope: diverse water matrices; biochar; adsorption  
> [SOURCE_TEXT_OMITTED sha256=ba983058c894e8f13a17557676d7f69e4842abdad2c8fc0f706b17853b9d9445].  
Supported claim metadata: Further research is needed to optimize biochar PFAS adsorption performance under diverse water matrices due to variable organic matter effects.

**WF10_021_MMG002** (negative_gold; `2024 - Liang - A critical review of biochar for the remediation of PFAS-contaminated soil and water.pdf`, chunk `48`)  
Scope: biochar; regeneration  
> [SOURCE_TEXT_OMITTED sha256=2ef738b52bd23cfd7945e62f17b2178422684983ba7d690836ca9792573b7ab7].  
Supported claim metadata: Biochar regeneration for PFAS has not been attempted frequently enough to draw definitive conclusions on efficacy.

**WF10_021_MMG003** (negative_gold; `2026 - Sadmani - [SOURCE_TEXT_OMITTED sha256=e2dd4fda49f066575cf9c26093f2c0f0108101becaa30a85e582d06a6552c102].pdf`, chunk `68`)  
Scope: biochar; regeneration  
> [SOURCE_TEXT_OMITTED sha256=1ee9fa0dacb5bd30615e945797f1feedd8ba78cfa3d955b6a7c30a213d78d909].  
Supported claim metadata: Thorough investigation is needed on how regeneration cycles alter biochar characteristics such as surface morphology, functionalities, and porosity.

### Model A Reference Draft

From the available evidence, the main matrix- and regeneration-related gaps that should be checked when screening PFAS adsorption studies are documented for biochar used in water matrices.

On the matrix side, reviewers should look for whether a study adequately evaluates the effects of different types and concentrations of organic matter (OM) in relevant water matrices. Existing work on biochar shows that OM can have highly variable impacts on PFAS sorption: some studies report minimal interference at environmentally relevant OM concentrations, while others find substantial reductions in PFAS sorption. This variability means that biochar performance across diverse water matrices is not yet well constrained, and further research is needed to optimize biochar use under differing OM conditions. When screening studies, it is therefore a limitation if the matrix scope is narrow (e.g., a single OM type or concentration) or if OM effects are not characterized, because such studies cannot reliably be generalized to other water matrices.

On the regeneration side, reviewers should check whether regeneration has been evaluated at all, how many regeneration cycles were tested, and whether changes in the sorbent’s properties were characterized. For biochar, current literature indicates that regeneration has not been attempted frequently enough to draw definitive conclusions about regeneration efficacy. Moreover, each regeneration cycle can alter biochar characteristics such as surface morphology, surface functionalities, and porosity, and these regeneration-induced changes require thorough investigation. Thus, a study that either omits regeneration testing or does not track how regeneration alters biochar properties has important gaps for assessing long-term PFAS removal performance and reusability.

These documented gaps—matrix-specific OM effects in diverse water matrices and limited, poorly characterized regeneration—are specific to biochar in the supplied evidence. Activated-carbon–specific matrix and regeneration gaps are not characterized in the provided records and would require additional sources to define.

Claims:

- `WF10_021-C01` [core]: For biochar used to remove PFAS from water matrices, the impact of organic matter on PFAS sorption is highly variable across studies, with some reporting minimal interference at environmentally relevant OM concentrations and others reporting substantial reductions in PFAS sorption, indicating a key matrix-related uncertainty. (evidence: WF10_021_MMG001)
- `WF10_021-C02` [core]: Because biochar PFAS sorption is sensitive to the type and concentration of organic matter in diverse water matrices, further research is needed to optimize biochar performance under different water-matrix conditions, and studies that do not probe these conditions have important matrix-scope gaps. (evidence: WF10_021_MMG001)
- `WF10_021-C03` [core]: Biochar regeneration for PFAS removal has not been attempted frequently enough in the literature to draw definitive conclusions on regeneration efficacy, so studies that omit or minimally test regeneration have a major regeneration-data gap. (evidence: WF10_021_MMG002)
- `WF10_021-C04` [core]: Each regeneration cycle can alter biochar characteristics, including surface morphology, surface functionalities, and porosity, making it necessary to investigate these regeneration-induced changes when assessing biochar reusability for PFAS removal. (evidence: WF10_021_MMG003)
- `WF10_021-C05` [supporting]: The matrix and regeneration limitations identified in the supplied evidence are specifically documented for biochar used to remove PFAS from water matrices, and are not automatically generalizable to other sorbents such as activated carbon. (evidence: WF10_021_MMG001, WF10_021_MMG002, WF10_021_MMG003)

### Model B Verification

Overall verdict: **approve**

- `WF10_021-C01`: **supported**. Matches the exact evidence span: OM type/concentration variably affects biochar PFAS sorption, with minimal interference in some studies and substantial reductions in others. Matrix (diverse water matrices), method (biochar), endpoint (sorption) are all correctly attributed. Claim is appropriately bounded to biochar.
  Recommended text: For biochar used to remove PFAS from water matrices, the impact of organic matter on PFAS sorption is highly variable across studies, with some reporting minimal interference at environmentally relevant OM concentrations and others reporting substantial reductions in PFAS sorption.
- `WF10_021-C02`: **partially_supported**. The 'further research needed to optimize performance under diverse water matrices' portion is directly supported. The added clause 'studies that do not probe these conditions have important matrix-scope gaps' is a reasonable screening-checklist inference consistent with the question's intent (identify gaps to check) but is not literally stated in the evidence span, so it is an interpretive extension rather than a direct restatement. The claim also substantially overlaps with C01, drawn from the same single evidence record without adding new evidentiary content, so the two could be merged for atomicity.
  Recommended text: Because biochar PFAS sorption is sensitive to organic-matter type and concentration in diverse water matrices, the evidence indicates a need for further research to optimize biochar performance under different water-matrix conditions (merge with C01 to avoid redundancy).
- `WF10_021-C03`: **partially_supported**. The core statement ('regeneration has not been attempted frequently enough to draw definitive conclusions on efficacy') is directly and correctly supported. The trailing clause 'so studies that omit or minimally test regeneration have a major regeneration-data gap' reframes a field-level limitation as a per-study screening criterion; this is a reasonable interpretive extension for a 'gaps to check' question but goes slightly beyond what the evidence literally states.
  Recommended text: Biochar regeneration for PFAS removal has not been attempted frequently enough in the literature to draw definitive conclusions on regeneration efficacy.
- `WF10_021-C04`: **supported**. Directly and precisely matches the evidence span on regeneration cycles altering surface morphology, functionalities, and porosity, and the stated need for thorough investigation. Correct method/endpoint attribution.
  Recommended text: Each regeneration cycle can alter biochar characteristics, including surface morphology, surface functionalities, and porosity, making it necessary to investigate these regeneration-induced changes when assessing biochar reusability for PFAS removal.
- `WF10_021-C05`: **supported**. Correctly scopes all three evidence records to biochar and explicitly declines to generalize to activated carbon, which is accurate since no supplied record addresses activated carbon. This directly enforces the must_not_claim boundary.
  Recommended text: The matrix and regeneration limitations identified in the supplied evidence are specifically documented for biochar used to remove PFAS from water matrices and are not established for other sorbents such as activated carbon by the provided records.

Reference-answer issues:
- The reference answer and claims C02/C03 occasionally convert a general field-level limitation (e.g., 'regeneration has not been attempted frequently enough') into a per-study screening rule ('studies that omit...have a gap'). This is a reasonable synthesis for a screening-guidance question but slightly exceeds the literal evidence wording and should be flagged for reviewer awareness, not rejection.
- C01 and C02 are drawn from the same single evidence record (WF10_021_MMG001) and substantially overlap in content; they could be merged into one atomic claim to reduce redundancy.

---

## WF10_025

**Question:** How should contact time be planned when powder activated carbon is used for both short- and long-chain PFAS?

**Must include:** Identify the relevant protocol steps, reagents/materials, operating conditions, matrix, target compounds, and reported limitations.

**Must not claim:** Do not convert a condition-specific finding into a universal PFAS treatment claim.

### Complete Gold Evidence

**WF10_025_MMG001** (required_gold; `2020 - Son - [SOURCE_TEXT_OMITTED sha256=b51b9a102b7e0232cb5cd6d73a3a29f01a16687f3790d5e68f0fba51b1362e44].pdf`, chunk `1`)  
Scope: short and long chain PFAS; surface water; powder activated carbon (PAC); adsorption; 80, 90, 85, 60, 120, 240; % (equilibrium), min  
> [SOURCE_TEXT_OMITTED sha256=a620a322b3818ef1084ca8848691920c6973fe06ba125ec2cc16357b68bc6622].  
Supported claim metadata: Long-chain PFAS reached approximately 80% and 90% of equilibrium within 60 and 120 min, respectively, whereas short-chain PFAS required 240 min to reach approximately 85% equilibrium.  
Does not support: Does not give specific PAC dose, individual compound rate constants, or guidance for matrices other than surface water.

### Model A Reference Draft

In a surface water matrix treated with powder activated carbon (PAC), long-chain PFAS approached approximately 80% of adsorption equilibrium within about 60 minutes and about 90% of equilibrium within about 120 minutes, whereas short-chain PFAS required about 240 minutes to reach approximately 85% of equilibrium. Under conditions comparable to this surface water–PAC system, contact time planning for simultaneous treatment of both short- and long-chain PFAS should be governed by the slower-equilibrating short-chain PFAS, meaning the PAC contact time should be on the order of the longer equilibration period (around 240 minutes) if the goal is to reach similar fractions of adsorption equilibrium for both PFAS groups. These percentages represent approximate fractions of equilibrium rather than full equilibrium, and the study does not report PAC dose, individual compound rate constants, or performance in matrices other than surface water, so the specific contact times may not directly transfer to other water qualities or PAC operating conditions.

Claims:

- `WF10_025-C01` [core]: In a surface water matrix treated with powder activated carbon, long-chain PFAS reached approximately 80% of adsorption equilibrium within 60 minutes and approximately 90% of equilibrium within 120 minutes. (evidence: WF10_025_MMG001)
- `WF10_025-C02` [core]: In the same surface water–powder activated carbon system, short-chain PFAS required about 240 minutes of contact time to reach approximately 85% of adsorption equilibrium. (evidence: WF10_025_MMG001)
- `WF10_025-C03` [core]: When planning PAC contact time for simultaneous treatment of both short- and long-chain PFAS in surface water under conditions comparable to this study, the contact time should be at least on the order of the longer equilibration time (around 240 minutes) if the goal is to achieve similar fractions of adsorption equilibrium for both PFAS groups. (evidence: WF10_025_MMG001)
- `WF10_025-C04` [supporting]: The reported percentages of approximately 80–90% equilibrium for long-chain PFAS at 60–120 minutes and approximately 85% equilibrium for short-chain PFAS at 240 minutes represent approximate fractions of adsorption equilibrium rather than full equilibrium, so longer contact times may be needed if near-complete equilibrium is desired. (evidence: WF10_025_MMG001)
- `WF10_025-C05` [limitation]: The contact times and equilibrium fractions reported for short- and long-chain PFAS adsorption on powder activated carbon are specific to a single surface water matrix and do not include PAC dose, individual compound rate constants, or data for matrices other than surface water, which limits direct transfer of these contact times to other systems. (evidence: WF10_025_MMG001)

### Model B Verification

Overall verdict: **approve**

- `WF10_025-C01`: **supported**. Matches the exact evidence span verbatim in substance: long-chain PFAS reached ~80% equilibrium at 60 min and ~90% at 120 min. Compound class, matrix, method, values and units are all correctly attributed.
  Recommended text: In a surface water matrix treated with powder activated carbon, long-chain PFAS reached approximately 80% of adsorption equilibrium within 60 minutes and approximately 90% of equilibrium within 120 minutes.
- `WF10_025-C02`: **supported**. Matches the evidence span: short-chain PFAS required 240 min to reach ~85% equilibrium. Correct compound class, matrix, value and unit attribution.
  Recommended text: In the same surface water–powder activated carbon system, short-chain PFAS required about 240 minutes of contact time to reach approximately 85% of adsorption equilibrium.
- `WF10_025-C03`: **partially_supported**. The evidence only reports separate equilibration kinetics for long- vs short-chain PFAS; it says nothing about a combined-treatment contact-time strategy. Model A's recommendation that overall contact time 'should be governed by the slower-equilibrating short-chain PFAS' at ~240 min is a reasonable, well-hedged synthesis directly responsive to the protocol_extraction question, but it is an inference layered on top of the evidence rather than a directly stated finding. It does not misstate any value and is properly scoped ('under conditions comparable to this study'), so it does not violate the must_not_claim boundary, but labeling it 'core' alongside C01/C02 slightly overstates its evidentiary directness — 'supporting' or an explicitly-flagged inference framing would be more accurate.
  Recommended text: Because short-chain PFAS equilibrate more slowly than long-chain PFAS in this surface water–PAC system, contact time planning aimed at achieving comparable equilibrium fractions for both groups would need to be inferred from the short-chain PFAS kinetics (i.e., on the order of 240 minutes); this is an extrapolation from the reported kinetics rather than a directly stated protocol recommendation in the source.
- `WF10_025-C04`: **supported**. Consistent with the gold record's 'limitation' field ('percentages are approximate equilibrium fractions, not full equilibrium'). The added inference that 'longer contact times may be needed if near-complete equilibrium is desired' is a modest, reasonable corollary of that stated limitation rather than a fabricated claim.
  Recommended text: The reported percentages (approximately 80–90% equilibrium for long-chain PFAS at 60–120 minutes and approximately 85% equilibrium for short-chain PFAS at 240 minutes) represent approximate, not full, equilibrium fractions, implying that longer contact times could be needed to approach full equilibrium.
- `WF10_025-C05`: **supported**. Directly mirrors the gold record's 'does_not_support' and 'supports_universal_claim: no' fields. Properly scoped as a limitation and does not overreach into other matrices or PAC doses.
  Recommended text: The contact times and equilibrium fractions reported for short- and long-chain PFAS adsorption on PAC are specific to a single surface water matrix and study; PAC dose, individual compound rate constants, and performance in other matrices are not reported, limiting transfer of these specific contact times to other systems.

Reference-answer issues:
- The single supplied gold record reports only overall equilibrium kinetics for two PFAS length classes; it contains no PAC dose, reagent list, reactor configuration, or explicit step-by-step protocol. Model A appropriately flags these gaps in 'unresolved_or_unsupported' rather than fabricating them, which is correct given non-exhaustive gold, but reviewers should note the reference answer's protocol recommendation (C03) is necessarily inferential given how sparse the underlying record is for a 'protocol_extraction' task.

---

## WF10_030

**Question:** Under what conditions might supercritical water oxidation leave uncertainty about fluorinated products?

**Must include:** Use limitation, uncertainty, caveat, and negative evidence to avoid overclaiming beyond the reported study scope.

**Must not claim:** Do not convert a condition-specific finding into a universal PFAS treatment claim.

### Complete Gold Evidence

**WF10_030_MMG001** (required_gold; `2023 - Li - PFOS destruction in a continuous supercritical water oxidation reactor.pdf`, chunk `1`)  
Scope: PFOS / TFA (intermediate); PFAS-impacted matrices; continuous-flow supercritical water oxidation reactor; transformation; 600; 32; 420-530; °C; s; °C  
> [SOURCE_TEXT_OMITTED sha256=df18556a56815be6fbd9c5b8cd543f66672e0bcd9522c2dad92ab274948882c8].  
Supported claim metadata: In a continuous-flow SCWO reactor, TFA persisted at T=600°C and residence time ~32 s; volatile organofluorine (1H-perfluoroalkane) was detected in gaseous products at T=420–530°C, and GS/MS spectra suggested other VOFs may be present, indicating uncertainty about fluorinated products at lower temperatures.  
Does not support: Does not establish complete defluorination or mineralization; the VOF identity at lower temperatures is only suggestive.

**WF10_030_MMG002** (required_gold; `2021 - Pinkard - Destruction of perfluorooctanesulfonate (PFOS) in a batch supercritical water oxidation reactor.pdf`, chunk `1`)  
Scope: PFOS; batch supercritical water oxidation reactor; defluorination; 425; 450; °C  
> [SOURCE_TEXT_OMITTED sha256=7454baf423fad18cf260e97c56d02d9ae340bdcf5a0d679f5d482d4bf97a8285].  
Supported claim metadata: At 425 and 450°C in a batch SCWO reactor, a low fluorine mass balance may indicate fluorinated species in the gaseous and/or liquid product not detected by targeted analysis.  
Does not support: Does not confirm the identity or quantity of the undetected fluorinated species; it is an inference from an incomplete mass balance.

**WF10_030_MMG003** (optional_gold; `2026 - Su - ReaxFF simulation of the degradation mechanism of perfluorononanoic acid (PFNA) by supercritical water oxidation.pdf`, chunk `6`)  
Scope: PFNA / PFAS; supercritical water oxidation; transformation  
> However, SCWO experimental studies on identifying PFAS degradation intermediates are still incomplete.  
Supported claim metadata: SCWO experimental studies on identifying PFAS degradation intermediates are incomplete; undetected liquid-phase products and the lack of gas-phase VOF analysis complicate fluorine element balance assessment.  
Does not support: Does not provide specific temperature conditions or quantitative data; it is a general statement of analytical limitations.

### Model A Reference Draft

Available SCWO studies indicate that uncertainty about fluorinated products arises under several specific experimental and analytical conditions.

In a continuous-flow SCWO reactor treating PFOS-impacted matrices, trifluoroacetic acid (TFA) remained in the effluent at 600 °C with a residence time of about 32 s, where it was described as the most recalcitrant intermediate and its persistence "emphasiz[ed] the need for TFA monitoring" during SCWO treatment of PFAS-impacted matrices. This indicates that even at 600 °C and ~32 s, fluorinated intermediates may not be fully transformed and require explicit tracking, leaving uncertainty about the fate of fluorine in the effluent under those conditions. At lower temperatures (420–530 °C) in the same continuous-flow system, volatile organofluorine species were detected in the gas phase, including 1H‑perfluoroalkane, and gas chromatography/mass spectrometry (GC/MS) spectra only suggested the presence of additional volatile organofluorines without identifying them. Under these 420–530 °C conditions, the exact composition of gas-phase fluorinated products therefore remains uncertain.

In a batch SCWO reactor treating PFOS, experiments at 425 and 450 °C showed a low fluorine mass balance, which the authors interpreted as potentially indicating fluorinated species in the gaseous and/or liquid products that were not captured by the targeted analytical methods. Thus, at 425–450 °C in batch PFOS SCWO, limited analyte coverage and an incomplete fluorine balance leave uncertainty about the identity and distribution of fluorinated products.

More generally, SCWO experimental work on PFAS degradation intermediates has been described as incomplete: studies to date have not fully identified all intermediates, and undetected liquid-phase products together with a lack of gas-phase volatile organofluorine analysis complicate assessment of the fluorine element balance. Under such experimental conditions—where intermediate identification is incomplete and gas- and/or liquid-phase fluorinated products are not comprehensively analyzed—there is systematic uncertainty about which fluorinated species persist or form during SCWO and how completely fluorine is accounted for.

Claims:

- `WF10_030-C01` [core]: In a continuous-flow SCWO reactor treating PFAS-impacted matrices containing PFOS, TFA was the most recalcitrant intermediate observed, persisting in the effluent at 600 °C with a residence time of about 32 s and necessitating explicit TFA monitoring, indicating that fluorinated intermediates can remain under these conditions and leave uncertainty about complete fluorine transformation. (evidence: WF10_030_MMG001)
- `WF10_030-C02` [core]: In the same continuous-flow SCWO system operated at 420–530 °C, volatile organofluorine compounds including 1H‑perfluoroalkane were detected in the gaseous products, and GC/MS spectra only suggested the presence of other volatile organofluorines without definitively identifying them, so at 420–530 °C the specific fluorinated gas-phase products remain uncertain. (evidence: WF10_030_MMG001)
- `WF10_030-C03` [core]: In batch SCWO experiments with PFOS at 425 and 450 °C, a low fluorine mass balance was observed, which may indicate the presence of fluorinated species in the gas and/or liquid product phases that were not detected by the targeted analytical methods, leaving uncertainty about fluorinated products under these temperature and analytical conditions. (evidence: WF10_030_MMG002)
- `WF10_030-C04` [core]: SCWO experimental studies aimed at identifying PFAS degradation intermediates have been described as incomplete, with undetected liquid-phase products and a lack of gas-phase volatile organofluorine analysis complicating assessment of the fluorine element balance, so whenever intermediate identification and gas-phase VOF analysis are incomplete, SCWO leaves uncertainty about which fluorinated products are present. (evidence: WF10_030_MMG003)
- `WF10_030-C05` [limitation]: The observations of persistent TFA, unidentified volatile organofluorines, and incomplete fluorine mass balances in these SCWO studies do not establish complete defluorination or mineralization and highlight that the identity and quantity of all fluorinated products remain unresolved under the reported conditions. (evidence: WF10_030_MMG001, WF10_030_MMG002, WF10_030_MMG003)

### Model B Verification

Overall verdict: **approve**

- `WF10_030-C01`: **supported**. The exact_evidence_span verbatim states TFA was the most recalcitrant intermediate, persisting at 600°C and ~32 s residence time, with an explicit call for TFA monitoring in SCWO treatment of PFAS-impacted matrices. The claim's attribution of the source compound as PFOS matches the record's PFAS_compound field ('PFOS / TFA (intermediate)'). The interpretive gloss ('leave uncertainty about complete fluorine transformation') is a reasonable, appropriately hedged inference and does not overclaim.
  Recommended text: No change needed.
- `WF10_030-C02`: **partially_supported**. The specific details in this claim (temperature range 420–530°C, detection of 1H-perfluoroalkane, GC/MS spectra 'suggesting' other VOFs) do not appear anywhere in the exact_evidence_span quoted for WF10_030_MMG001, which covers only the TFA/600°C/32s finding. These details instead come solely from the record's 'supported_claim', 'numerical_value', and 'limitation' metadata fields. Those fields are part of the same gold evidence record and plausibly summarize the same source chunk, so the claim is not fabricated, but it cannot be independently verified against the literal quoted text supplied. This should be flagged for a human reviewer to confirm against the underlying chunk/document before being treated as fully verified.
  Recommended text: Per the gold record's chunk-level summary (not the quoted span) for the same continuous-flow SCWO system, volatile organofluorine compounds including 1H-perfluoroalkane were reportedly detected in gaseous products at 420–530°C, with GC/MS spectra only suggesting other VOFs without definitive identification — pending confirmation against the underlying source text, this leaves the specific fluorinated gas-phase products at 420–530°C uncertain.
- `WF10_030-C03`: **supported**. Exact_evidence_span verbatim: 'a low fluorine mass balance at temperatures of 425 and 450°C may indicate the existence of fluorinated species in the gaseous and/or liquid product which are not detected by targeted analysis.' The claim mirrors this precisely, correctly attributes it to a batch reactor and PFOS, and retains the hedged 'may indicate' framing rather than asserting certainty.
  Recommended text: No change needed.
- `WF10_030-C04`: **partially_supported**. The exact_evidence_span for MMG003 is only: 'However, SCWO experimental studies on identifying PFAS degradation intermediates are still incomplete.' The additional specifics ('undetected liquid-phase products,' 'lack of gas-phase volatile organofluorine analysis complicating the fluorine element balance') come from the record's 'supported_claim' and 'limitation' fields, not the quoted span itself, so they are not independently verifiable from the text given. Separately, the closing clause ('so whenever intermediate identification and gas-phase VOF analysis are incomplete, SCWO leaves uncertainty...') restates a single general observation as an if-then rule, drifting toward a generalized principle rather than staying tied to the specific PFNA/PFAS SCWO studies referenced — a mild boundary risk given the must_not_claim constraint against universalizing condition-specific findings.
  Recommended text: SCWO experimental studies on identifying PFAS (including PFNA) degradation intermediates have been described in the reviewed literature as still incomplete, which — per the same record's summary — reflects undetected liquid-phase products and limited gas-phase volatile organofluorine analysis complicating fluorine element balance assessment in the studies reviewed.
- `WF10_030-C05`: **supported**. This limitation claim appropriately synthesizes the does_not_support fields ('does not establish complete defluorination or mineralization,' 'does not confirm the identity or quantity of the undetected fluorinated species') and correctly refrains from claiming complete mineralization or universal applicability. It is properly scoped to the specific reactors/compounds/temperatures discussed and correctly labeled as a limitation rather than a core finding.
  Recommended text: No change needed.

Reference-answer issues:
- The gold evidence records mix a literal 'exact_evidence_span' quote with additional structured fields (supported_claim, limitation, numerical_value, protocol_detail) that in two cases (MMG001's 420–530°C/1H-perfluoroalkane detail, MMG003's liquid-phase/gas-phase VOF detail) assert facts not present in the quoted span itself. This makes it impossible to fully verify those specific details from the literal text supplied, even though they are plausibly legitimate summaries of the same source chunk. A human reviewer with access to the source PDFs should confirm these details against the underlying chunk text.

---

## WF10_004a

**Question:** How does PFAS chain length affect reported treatment performance or adsorption behavior?

**Must include:** Compare studies only on matched compounds, matrices, endpoints, and conditions; avoid ranking technologies when the evidence is not comparable.

**Must not claim:** Do not convert a condition-specific finding into a universal PFAS treatment claim.

### Complete Gold Evidence

**WF10_004a_MMG001** (required_gold; `2023 - Smaili - [SOURCE_TEXT_OMITTED sha256=3884ec13a07d30b0a4d88c53062028410a1ce2623d8e96cce084ea7ba1e13b06].pdf`, chunk `18`)  
Scope: long-chain PFAS; short-chain PFAS; aqueous; different sorbents; removal  
> [SOURCE_TEXT_OMITTED sha256=b74e79a570d1149a404456da98719dd9a8a13619b8d733a9d0fbc9f3c80523e1].  
Supported claim metadata: In the reviewed sorbent comparison, removal efficiency of long-chain PFAS is higher than that of short-chain PFAS across the sorbents considered.

**WF10_004a_MMG002** (required_gold; `2025 - Kebede - [SOURCE_TEXT_OMITTED sha256=db9915a269e1f93613d318b5b43545d2669031cfe286904d5961450a3a9adecb],.pdf`, chunk `18`)  
Scope: PFOA; PFOS; PFBA; PFBS; aqueous; GAC; PAC; ball-milled colloidal activated carbon; removal; 73; 24; 89; 35; 30; 11; 55; 18; %  
> [SOURCE_TEXT_OMITTED sha256=23c92cd59d9fae3215bf0958e36d6ae28c1de0341ff2924d16551f212b88e948].  
Supported claim metadata: For GAC, PAC, and ball-milled colloidal activated carbon, long-chain PFAS (PFOA: 73% ± 24%, PFOS: 89% ± 35%) showed higher removal efficiency than short-chain PFAS (PFBA: 30% ± 11%, PFBS: 55% ± 18%).

**WF10_004a_MMG003** (optional_gold; `2023 - Smaili - [SOURCE_TEXT_OMITTED sha256=3884ec13a07d30b0a4d88c53062028410a1ce2623d8e96cce084ea7ba1e13b06].pdf`, chunk `29`)  
Scope: PFOS; PFOA; short-chain PFAS; aqueous; PEI-f-CMC; removal; 98.8; 87.6; %  
> [SOURCE_TEXT_OMITTED sha256=ee0fc9f7a3f6ef8dee3c8c277b23e9307230af5a77b74a00b9baaa1619d87e1d].  
Supported claim metadata: Overall removal efficiency of short-chain PFAS is much lower than that of long-chain PFAS (e.g., PFOS 98.8%, PFOA 87.6%), attributed to short-chain PFAS' low hydrophobicity.  
Does not support: Specific short-chain values (PFBA 2.1%, PFPeA 1.1%) and the sorbent identity PEI-f-CMC are not in the selected span.

**WF10_004a_MMG004** (optional_gold; `2026 - Sadmani - [SOURCE_TEXT_OMITTED sha256=e2dd4fda49f066575cf9c26093f2c0f0108101becaa30a85e582d06a6552c102].pdf`, chunk `37`)  
Scope: water; biochar/adsorbents (review); adsorption  
> [SOURCE_TEXT_OMITTED sha256=1044cd21c880dc0df68e663beb668672c8ff6a812913e5c7b851a5e7d07dd973]].  
Supported claim metadata: In the reviewed adsorption literature, longer-chain PFAS are described as more hydrophobic and less water-soluble, leading to higher adsorption capacities onto adsorbents.

**WF10_004a_MMG005** (optional_gold; `2025 - Hamza - Understanding PFAS Adsorption - How Molecular Structure Affects Sustainable Water Treatment.pdf`, chunk `21`)  
Scope: long-chain PFASs; short-chain PFASs; adsorption  
> [SOURCE_TEXT_OMITTED sha256=1dd3a790b53e312490f36e35b956affdcf0c5dbbebed7969dab1660eaf263d0b].  
Supported claim metadata: In the discussed adsorption context, long-chain PFAS can interact through hydrophobic tails and hydrophobic interactions, while short-chain PFAS have fewer fluorine moieties and show less hydrophobic interaction, with electrostatic interaction becoming dominant in that type of adsorption.

**WF10_004a_MMG006** (negative_gold; `2022 - Vu - Recent progress in adsorptive removal of per- and poly-fluoroalkyl substances (PFAS) from water-wastewater.pdf`, chunk `63`)  
Scope: water; wastewater; various adsorbents; removal  
> [SOURCE_TEXT_OMITTED sha256=a4e24844122d64243186fa2139524777c322ada9cb8d51793ac13f84e0e116e1].  
Supported claim metadata: While removal efficiencies are often better for long-chained, carboxylic, and linear PFAS, contradictory results are frequently reported across different waters, adsorbents, and experimental conditions, and many influencing factors remain unknown.  
Does not support: The universal claim that longer chain always yields higher removal without exceptions.

### Model A Reference Draft

Across the aqueous adsorption literature summarized in the provided records, PFAS chain length is consistently reported to influence treatment performance, with longer-chain PFAS typically being removed more effectively than shorter-chain analogues under comparable adsorption conditions.

A critical review of sorbent-based removal from water reports that, across the sorbents examined, long-chain PFAS showed higher removal efficiencies than short-chain PFAS, indicating a systematic trend toward better adsorption of longer-chain compounds in those studies.[WF10_004a_MMG001] A specific batch study using three carbonaceous adsorbents (granular activated carbon, powdered activated carbon, and ball-milled colloidal activated carbon) in aqueous solutions found that long-chain PFAS (PFOA and PFOS) had substantially higher removal than short-chain PFAS (PFBA and PFBS) for all three adsorbents: PFOA removal was 73% ± 24% and PFOS removal was 89% ± 35%, compared with 30% ± 11% for PFBA and 55% ± 18% for PFBS.[WF10_004a_MMG002] This study concluded that long-chain PFAS are more adsorbed on carbonaceous-based adsorbents than short-chain PFAS under those batch conditions.[WF10_004a_MMG002]

Another review highlights a similar pattern for a specific sorbent: using a PEI-f-CMC adsorbent in aqueous solutions, PFOS and PFOA achieved high removal efficiencies of 98.8% and 87.6%, respectively, whereas the overall removal of short-chain PFAS was described as much lower, underscoring the difficulty of removing short-chain species from water.[WF10_004a_MMG003] In a broader review of biochar and related adsorbents for PFAS removal from water matrices, longer-chain PFAS are described as more hydrophobic and less water-soluble, which is linked to higher adsorption capacities onto these adsorbents.[WF10_004a_MMG004]

Mechanistically, review work on PFAS adsorption notes that long-chain PFAS can interact via their hydrophobic tails through hydrophobic interactions and that PFAS chain length and molecular orientation significantly influence the adsorption process.[WF10_004a_MMG005] In this framework, longer-chain PFAS—with more CF2 units—exhibit stronger hydrophobic interactions with adsorbent surfaces, whereas shorter-chain PFAS, having fewer fluorine moieties, show weaker hydrophobic interactions and rely more heavily on electrostatic interactions in adsorption systems, which is associated with lower overall adsorption in many cases.[WF10_004a_MMG005, WF10_004a_MMG004, WF10_004a_MMG003]

At the same time, a review of adsorptive PFAS removal from water and wastewater emphasizes that, although removal efficiencies are often better for long-chained, carboxylic, and linear PFAS, many other factors (such as water and wastewater organic/inorganic content and adsorbent age) can strongly influence large-scale removal efficiencies, and contradictory results are frequently reported across different waters, adsorbents, and experimental conditions.[WF10_004a_MMG006] This indicates that while chain length commonly correlates with higher adsorption and removal in aqueous adsorption-based treatments, chain length alone does not fully determine performance, and outcomes can diverge under different matrices and operational conditions.

Overall, within aqueous adsorption and sorbent-based treatments, the available evidence supports that longer-chain PFAS generally show higher adsorption capacities and higher removal efficiencies than shorter-chain PFAS, driven in large part by increased hydrophobicity and reduced water solubility. However, this trend is not sufficient by itself to predict treatment performance across all water matrices, adsorbents, and operating conditions, and the provided records do not address how chain length affects non-adsorptive treatment processes.

Claims:

- `WF10_004a-C01` [core]: In the aqueous sorbent-based systems reviewed by Smaili et al., the removal efficiency of long-chain PFAS was higher than that of short-chain PFAS across all sorbents considered. (evidence: WF10_004a_MMG001)
- `WF10_004a-C02` [core]: In batch adsorption experiments with aqueous solutions using granular activated carbon, powdered activated carbon, and ball-milled colloidal activated carbon, the long-chain PFAS PFOA and PFOS showed higher removal efficiencies (73% ± 24% and 89% ± 35%, respectively) than the short-chain PFAS PFBA and PFBS (30% ± 11% and 55% ± 18%), demonstrating greater adsorption of long-chain PFAS on these carbonaceous adsorbents under the tested conditions. (evidence: WF10_004a_MMG002)
- `WF10_004a-C03` [core]: Using a PEI-f-CMC sorbent in aqueous solutions, PFOS and PFOA achieved high removal efficiencies of 98.8% and 87.6%, respectively, while the overall removal efficiency of short-chain PFAS was described as much lower, highlighting the greater difficulty of removing short-chain PFAS relative to long-chain PFAS with this adsorbent. (evidence: WF10_004a_MMG003)
- `WF10_004a-C04` [core]: In reviews of PFAS adsorption onto biochar and related adsorbents from water matrices, longer-chain PFAS are described as more hydrophobic and less water-soluble, which leads to higher adsorption capacities compared to shorter-chain analogues. (evidence: WF10_004a_MMG004)
- `WF10_004a-C05` [supporting]: Mechanistic discussion of PFAS adsorption indicates that long-chain PFAS can interact via their hydrophobic tails through hydrophobic interactions, and that chain length and molecular orientation significantly influence the adsorption process, whereas shorter-chain PFAS, with fewer fluorine moieties, exhibit weaker hydrophobic interactions and rely more on electrostatic interactions in adsorption systems. (evidence: WF10_004a_MMG005)
- `WF10_004a-C06` [supporting]: A review of PFAS adsorptive removal from water and wastewater reports that removal efficiencies are often better for long-chained PFAS but also notes that many other factors influencing large-scale removal efficiencies, such as water and wastewater organic and inorganic content and adsorbent properties, remain poorly understood and that contradictory results are frequently reported across different waters, adsorbents, and experimental conditions. (evidence: WF10_004a_MMG006)
- `WF10_004a-C07` [limitation]: The available review evidence on chain-length effects emphasizes that, although long-chained PFAS often show higher removal efficiencies than short-chained PFAS, contradictory results across water and wastewater matrices, adsorbents, and experimental conditions mean that chain length alone does not fully determine treatment performance in adsorption-based systems. (evidence: WF10_004a_MMG006, WF10_004a_MMG001)

### Model B Verification

Overall verdict: **revise**

- `WF10_004a-C01`: **supported**. Evidence span states removal efficiency of long-chain PFAS is higher than short-chain across all sorbents in the Smaili review; claim faithfully restates this, correctly scoped as a review-level trend and attributed to Smaili et al.
  Recommended text: No change needed.
- `WF10_004a-C02`: **supported**. Compound, matrix, adsorbents, values, and units all match the exact evidence span exactly (PFOA 73%±24%, PFOS 89%±35% vs PFBA 30%±11%, PFBS 55%±18%, across GAC/PAC/ball-milled colloidal activated carbon). Attribution and scope are correct.
  Recommended text: No change needed.
- `WF10_004a-C03`: **partially_supported**. The gold record's own 'does_not_support' field explicitly states that the sorbent identity PEI-f-CMC is NOT contained in the selected exact_evidence_span ('[SOURCE_TEXT_OMITTED sha256=694b21f07f85b407c8c5308eb02c1dcddc6b8677a2a7afb71cfa1c74f09c96f3]...'). The span never names an adsorbent. Model A's claim (and the parallel prose in the reference_answer's third paragraph) asserts 'Using a PEI-f-CMC sorbent... PFOS and PFOA achieved high removal efficiencies of 98.8% and 87.6%', directly attributing these values to a sorbent that the gold packet flags as unsupported by this span. This is a method/material attribution error that should be removed.
  Recommended text: In the Smaili et al. critical review, the overall removal efficiency of short-chain PFAS from aqueous solutions was much lower than that of long-chain PFAS (e.g., PFOS 98.8%, PFOA 87.6%), a difference attributed to the lower hydrophobicity of short-chain PFAS; the specific sorbent used to obtain these values is not identified in the cited span.
- `WF10_004a-C04`: **supported**. Span directly supports the mechanistic claim that longer-chain PFAS are more hydrophobic/less water-soluble leading to higher adsorption capacities; claim correctly scopes this to the reviewed adsorption literature rather than universalizing.
  Recommended text: No change needed.
- `WF10_004a-C05`: **partially_supported**. The exact_evidence_span only supports the long-chain hydrophobic-tail/orientation sentence. The additional statement about short-chain PFAS having fewer fluorine moieties and relying on electrostatic interaction appears in the gold record's 'supported_claim' field but is not present in the quoted exact_evidence_span itself. Model A's claim mirrors the record's supported_claim verbatim, so this is a defensible use of the gold packet, but strictly the span alone does not substantiate the short-chain portion of the claim.
  Recommended text: Mechanistic discussion of PFAS adsorption indicates that long-chain PFAS can interact via their hydrophobic tails through hydrophobic interactions, and that chain length and molecular orientation significantly influence the adsorption process; per the underlying review's broader discussion, short-chain PFAS are described as relying more on electrostatic interaction, though this detail is not contained in the quoted span.
- `WF10_004a-C06`: **supported**. Faithfully reflects the negative_gold span, preserving the hedge that many factors remain unknown and contradictory results occur; does not convert the negative evidence into a positive universal finding.
  Recommended text: No change needed.
- `WF10_004a-C07`: **supported**. Combining MMG001's general trend statement with MMG006's explicit caveat about contradictory results is a reasonable synthesis and does not misattribute either record; it overlaps somewhat with C06 but is not incorrect. Correctly scoped as limited to adsorption-based systems.
  Recommended text: No change needed; consider merging with C06 to reduce redundancy.

Reference-answer issues:
- Paragraph 3 of the free-text reference_answer states 'using a PEI-f-CMC adsorbent in aqueous solutions, PFOS and PFOA achieved high removal efficiencies of 98.8% and 87.6%, respectively' — this repeats the C03 attribution error, naming a sorbent (PEI-f-CMC) that the gold record's own does_not_support field says is not established by the cited exact_evidence_span.
- The gold record WF10_004a_MMG005 has an exact_evidence_span that only covers the long-chain PFAS behavior, while its supported_claim field additionally asserts short-chain PFAS electrostatic-interaction behavior not present in the span; this is an internal inconsistency in the gold packet that should be tightened (either extend the span or trim the supported_claim) so downstream claims relying on supported_claim remain fully traceable to quoted text.

---

## WF10_004b

**Question:** How can PFAS compound class or headgroup affect treatment performance or equilibrium behavior?

**Must include:** Compare studies only on matched compounds, matrices, endpoints, and conditions; avoid ranking technologies when the evidence is not comparable.

**Must not claim:** Do not convert a condition-specific finding into a universal PFAS treatment claim.

### Complete Gold Evidence

**WF10_004b_MMG001** (required_gold; `2025 - Saha - Foam fractionation of PFAS from landfill leachate using a membrane electrochemical reactor.pdf`, chunk `1`)  
Scope: perfluorosulfonic acids (PFSAs), perfluorocarboxylic acids (PFCAs); landfill leachate; membrane electrochemical reactor (MER) foam fractionation; removal/separation; 98.3, 85.5, 92.5-99.1, 80.8-90; %  
> [SOURCE_TEXT_OMITTED sha256=9267fd3f47c2241ef937a6540c6b77c49ce38a341deeba7e69a88142941cd948].  
Supported claim metadata: In landfill leachate, PFSAs were removed more efficiently than PFCAs after seven hours of operation, with 98.3% PFSA removal versus 85.5% PFCA removal; short-chain PFSAs (C≤6, 92.5–99.1%) were removed more efficiently than short-chain PFCAs (C≤6, 80.8–90%), possibly due to stronger air-water interface affinity enhancing foam-based separation.

**WF10_004b_MMG002** (negative_gold; `2025 - Meng - Complete Aqueous Defluorination of GenX Hexafluoropropylene Oxide Dimer Acid Anion by Pulsed.pdf`, chunk `14`)  
Scope: GenX, PFOS; aqueous LiOH electrolyte; pulsed electrolysis on [Ni0.75Fe0.25]-(OH)2–hydrophilic carbon fiber paper anodes; adsorption  
> [[SOURCE_TEXT_OMITTED sha256=a6ff2602ad9393035900f90f368be80844cc1bc2f2fdc3ddfaea5d7d29d73d5a].  
Supported claim metadata: The chemical identity of the PFAS headgroup did not govern PFAS adsorption on laser-made [Ni0.75Fe0.25]-(OH)2–hydrophilic carbon fiber paper anodes.  
Does not support: Headgroup identity always affects PFAS adsorption.

**WF10_004b_MMG003** (required_gold; `2021 - Liu - [SOURCE_TEXT_OMITTED sha256=33e8319b0a45c042bb3ce8b369790255983cb1e48f0576b319c9ac9a8a727a44].pdf`, chunk `17`)  
Scope: FHxSA, PFHxS; groundwater (pH 7.3); nanofiltration (NF); separation  
> [SOURCE_TEXT_OMITTED sha256=ec94b010a0258744fed2e60dcacc0b8cdd2334eec3c889e9c3dc00f10639704f].  
Supported claim metadata: FHxSA is likely neutral at pH 7.3 due to its sulfonamide headgroup, and its NF rejection [SOURCE_TEXT_OMITTED sha256=758ba2be39ee3364095f450595244f9ce3784f0d556272a7be756c3aeb8f6bd9].

**WF10_004b_MMG004** (required_gold; `2023 - Lauwers - [SOURCE_TEXT_OMITTED sha256=4ebf7a9d3ced69a7d519610182586e2f99c564ad70850837cfad3b95589bbb18].pdf`, chunk `34`)  
Scope: perfluorosulfonic acids, perfluorocarboxylic acids; aqueous solution; all-silica zeolite β; adsorption  
> [SOURCE_TEXT_OMITTED sha256=6f53559af02714793ca579e8ed55c11f0f4338764b7442de73c6271cc17faec6].  
Supported claim metadata: All-silica zeolite β has lower adsorption capacity and affinity for sulfonic acids than for carboxylic acids, attributed to the more polar sulfonic moiety and lack of dimer formation.

**WF10_004b_MMG005** (optional_gold; `2023 - Wang - Removing per- and polyfluoroalkyl substances (PFAS) in water by foam fractionation.pdf`, chunk `36`)  
Scope: PFHeA, PFHeS; laboratory-spiked water; foam fractionation; removal/separation; 55, 96; %  
> [SOURCE_TEXT_OMITTED sha256=a415e691e3be498886bdc14a63ccc51ffbde0827bea3e72db77e1a7206c33f92].  
Supported claim metadata: In the cited removal example, PFHeA removal was 55% overall, much less than PFHeS removal at 96% overall.

**WF10_004b_MMG006** (optional_gold; `2026 - Sadmani - [SOURCE_TEXT_OMITTED sha256=e2dd4fda49f066575cf9c26093f2c0f0108101becaa30a85e582d06a6552c102].pdf`, chunk `31`)  
Scope: PFSAs, PFCAs; water; ZVI or ZVI+BC; removal; 94, 60; %  
> [SOURCE_TEXT_OMITTED sha256=8b5f8307d7e34dc948917d638b816b76dae73dcb840522830a7d790fb556f893].  
Supported claim metadata: With ZVI or ZVI+BC, PFSAs were removed up to 94% compared to PFCAs up to 60%.

**WF10_004b_MMG007** (optional_gold; `2025 - Uwayezu - Efficient removal of PFAS in groundwater and landfill leachate using iron-modified peat residues and electrochemical oxidation.pdf`, chunk `19`)  
Scope: PFOS, PFNA, PFHxS, PFHpA; groundwater/landfill leachate; column with iron-modified peat residues; removal/retention; 84, 72, 64, 44; %  
> [SOURCE_TEXT_OMITTED sha256=eba319cd7e8f6a4fb168d4b099931888c13270cdb5de151cf88b6daa0715aa22].  
Supported claim metadata: Column treatment retained sulfonate PFAS more than carboxylate PFAS with equal chain length, e.g., 84% PFOS vs 72% PFNA removal.

### Model A Reference Draft

Across the supplied studies, PFAS compound class and headgroup clearly influence treatment performance and equilibrium behavior, but the effect is strongly process- and material-specific rather than universal.

For foam-based separation, perfluorosulfonic acids (PFSAs) are removed more efficiently than perfluorocarboxylic acids (PFCAs) of comparable chain length. In landfill leachate treated by membrane electrochemical reactor foam fractionation, 98.3% of PFSAs were removed within seven hours compared with 85.5% for PFCAs, and short-chain PFSAs (C≤6) showed 92.5–99.1% removal versus 80.8–90% for short-chain PFCAs, an effect attributed by the authors to stronger PFSA affinity for the air–water interface that enhances foam separation under those conditions. In laboratory‑spiked water treated by foam fractionation, a similar trend was observed for specific analogues: overall removal of PFHeA (a PFCA) was 55%, much lower than 96% overall removal of PFHeS (a PFSA) of similar perfluorocarbon chain length.

For iron‑based treatment systems, sulfonate headgroups also corresponded to higher removal than carboxylates under the reported conditions. Batch tests using zero‑valent iron (ZVI) or ZVI plus biochar in water showed PFSAs were more efficiently removed, with up to 94% removal, compared to PFCAs, which reached up to 60% removal. In column experiments with iron‑modified peat residues treating groundwater and landfill leachate, sulfonate PFAS exhibited higher retention than carboxylate PFAS of equal perfluorocarbon chain length, for example 84% PFOS versus 72% PFNA removal and 64% PFHxS versus 44% PFHpA removal, which was attributed to the greater effect of the sulfonate functional group in that system.

In contrast, for adsorption onto an all‑silica zeolite β, the headgroup effect was reversed: the adsorption capacity and affinity of the zeolite were lower for sulfonic acids than for carboxylic acids in aqueous solution. This behavior was linked to the more polar nature of the sulfonic moiety and the unlikely formation of sulfonic acid dimers, indicating that, on this adsorbent, carboxylate headgroups favor stronger equilibrium adsorption than sulfonates.

For membrane separation, the headgroup’s impact on charge state can strongly affect nanofiltration rejection. In groundwater at pH 7.3, FHxSA, which is likely neutral due to its sulfonamide headgroup, showed consistently lower nanofiltration rejection than its anionic analogue PFHxS (a sulfonate). The lower rejection of FHxSA was attributed to the absence of an electrostatic repulsion mechanism for this neutral compound, in contrast to the charged sulfonate.

Finally, not all systems show a dominant headgroup effect. During pulsed electrolysis in an aqueous LiOH electrolyte using laser‑made [Ni0.75Fe0.25]‑(OH)2–hydrophilic carbon fiber paper anodes, the chemical identity of the PFAS headgroup (comparing GenX and PFOS) did not govern PFAS adsorption; instead, adsorption behavior was controlled by anode characteristics under those specific conditions.

Overall, the supplied evidence demonstrates that PFAS class and headgroup can substantially alter removal, retention, or adsorption equilibria for matched compounds, but the direction and magnitude of these effects depend on the specific treatment process, material, and solution chemistry, rather than following a single universal pattern.

Claims:

- `WF10_004b-C01` [core]: In landfill leachate treated by membrane electrochemical reactor foam fractionation for seven hours, perfluorosulfonic acids were removed more efficiently than perfluorocarboxylic acids, with 98.3% PFSA removal versus 85.5% PFCA removal overall, and short-chain PFSAs (C≤6) showing 92.5–99.1% removal compared to 80.8–90% for short-chain PFCAs. (evidence: WF10_004b_MMG001)
- `WF10_004b-C02` [supporting]: In laboratory-spiked water treated by foam fractionation, overall removal of PFHeA (a perfluorocarboxylic acid) was 55%, much less than the 96% overall removal of PFHeS (a perfluorosulfonic acid) of similar perfluorocarbon chain length. (evidence: WF10_004b_MMG005)
- `WF10_004b-C03` [core]: Across foam fractionation studies in landfill leachate and laboratory-spiked water, sulfonate PFAS were removed more effectively than carboxylate PFAS of comparable chain length, indicating that the sulfonate headgroup can enhance foam-based PFAS separation under those specific conditions. (evidence: WF10_004b_MMG001, WF10_004b_MMG005)
- `WF10_004b-C04` [core]: Batch tests using zero-valent iron or zero-valent iron plus biochar in water showed that perfluorosulfonic acids were more efficiently removed, with up to 94% removal, whereas perfluorocarboxylic acids reached up to 60% removal under the same treatment types. (evidence: WF10_004b_MMG006)
- `WF10_004b-C05` [core]: In column treatment with iron-modified peat residues for groundwater and landfill leachate, sulfonate PFAS showed higher retention than carboxylate PFAS of equal perfluorocarbon chain length, exemplified by 84% PFOS versus 72% PFNA removal and 64% PFHxS versus 44% PFHpA removal. (evidence: WF10_004b_MMG007)
- `WF10_004b-C06` [core]: For adsorption onto all-silica zeolite β in aqueous solution, the adsorption capacity and affinity were lower for perfluorosulfonic acids than for perfluorocarboxylic acids, which was attributed to the more polar sulfonic moiety and the unlikely formation of sulfonic acid dimers. (evidence: WF10_004b_MMG004)
- `WF10_004b-C07` [core]: In nanofiltration of groundwater at pH 7.3, FHxSA, which is likely neutral due to its sulfonamide headgroup, exhibited consistently lower rejection than the anionic analogue PFHxS, with the lower rejection attributed to the lack of an electrostatic repulsion mechanism for the neutral sulfonamide species. (evidence: WF10_004b_MMG003)
- `WF10_004b-C08` [limitation]: During pulsed electrolysis in an aqueous LiOH electrolyte using laser-made [Ni0.75Fe0.25]-(OH)2–hydrophilic carbon fiber paper anodes, the chemical identity of the PFAS headgroup did not govern PFAS adsorption, indicating that anode characteristics, rather than headgroup type, controlled adsorption of PFOS and GenX under those conditions. (evidence: WF10_004b_MMG002)
- `WF10_004b-C09` [supporting]: The supplied studies collectively show that PFAS class or headgroup can either increase or decrease treatment performance depending on the technology—enhancing removal for sulfonates in foam fractionation, zero-valent iron-based systems, and iron-modified peat columns, but reducing adsorption relative to carboxylates on all-silica zeolite β and not governing adsorption on a Ni–Fe hydroxide anode—demonstrating that headgroup effects are highly process-specific. (evidence: WF10_004b_MMG001, WF10_004b_MMG005, WF10_004b_MMG006, WF10_004b_MMG007, WF10_004b_MMG004, WF10_004b_MMG002)
- `WF10_004b-C10` [limitation]: The observed influence of PFAS class or headgroup on treatment performance in the supplied studies is specific to the tested compounds, matrices, and materials, and does not establish a universal rule that headgroup identity will control removal or adsorption behavior for all PFAS and all treatment technologies. (evidence: WF10_004b_MMG001, WF10_004b_MMG005, WF10_004b_MMG006, WF10_004b_MMG007, WF10_004b_MMG004, WF10_004b_MMG003, WF10_004b_MMG002)

### Model B Verification

Overall verdict: **revise**

- `WF10_004b-C01`: **partially_supported**. The overall 98.3% PFSA vs 85.5% PFCA removal figures are directly in the quoted exact_evidence_span. However, the short-chain (C≤6) figures of 92.5–99.1% and 80.8–90% appear only in the gold record's 'supported_claim' field, not in the quoted exact_evidence_span itself, so the specific numeric breakdown cannot be verified from the text actually supplied. This is a gap in the gold packet (span truncation) rather than a fabrication by Model A, but the claim as written asserts more precision than the supplied span text substantiates.
  Recommended text: In landfill leachate treated by membrane electrochemical reactor foam fractionation for seven hours, perfluorosulfonic acids were removed more efficiently than perfluorocarboxylic acids overall (98.3% PFSA vs. 85.5% PFCA removal); the source additionally reports a short-chain (C≤6) breakdown of 92.5–99.1% for PFSAs vs. 80.8–90% for PFCAs.
- `WF10_004b-C02`: **partially_supported**. The 55% PFHeA vs 96% PFHeS overall removal figures are directly supported by the quoted span. The added qualifier 'of similar perfluorocarbon chain length' is not stated in the evidence span and is an inference from compound naming; the same source sentence separately references a distinct compound 'PFHxA', and the span itself is flagged in the gold record as truncated/garbled, so chain-length equivalence between PFHeA and PFHeS cannot be confirmed from the supplied text.
  Recommended text: In laboratory-spiked water treated by foam fractionation, overall removal of PFHeA (a perfluorocarboxylic acid) was 55%, much less than the 96% overall removal of PFHeS (a perfluorosulfonic acid); chain-length equivalence between the two compounds is not confirmed by the (truncated) evidence span.
- `WF10_004b-C03`: **supported**. Reasonable synthesis of two matched foam-fractionation results, correctly scoped to 'those specific conditions' and not generalized beyond the two studies.
  Recommended text: No change needed.
- `WF10_004b-C04`: **supported**. Matches the evidence span and supported_claim closely; 'up to' qualifiers preserved.
  Recommended text: No change needed.
- `WF10_004b-C05`: **supported**. Numbers and compound pairs match the evidence span exactly, including the 'equal perfluorocarbon chain lengths' qualifier which is explicitly stated in the source.
  Recommended text: No change needed.
- `WF10_004b-C06`: **supported**. Direction (sulfonic < carboxylic adsorption on zeolite β) and mechanism (polar sulfonic moiety, lack of dimer formation) match the evidence span.
  Recommended text: No change needed.
- `WF10_004b-C07`: **supported**. Correctly attributes neutrality to sulfonamide headgroup at pH 7.3, lower NF rejection versus anionic PFHxS, and the electrostatic-repulsion mechanism, matching the span and correctly scoped as pH-dependent.
  Recommended text: No change needed.
- `WF10_004b-C08`: **supported**. Correctly treats this as a negative/limitation finding (headgroup identity did NOT govern adsorption) rather than converting it into a positive universal claim; scope to this anode/electrolyte system is preserved.
  Recommended text: No change needed.
- `WF10_004b-C09`: **supported**. Accurate high-level summary of directionally divergent findings across the six process-specific evidence records; no individual attribution errors introduced.
  Recommended text: No change needed.
- `WF10_004b-C10`: **supported**. Appropriately guards against the 'must_not_claim' boundary by explicitly stating non-universality; consistent with all evidence records' 'supports_universal_claim: no' flags.
  Recommended text: No change needed.

Reference-answer issues:
- WF10_004b_MMG001's exact_evidence_span only contains the overall 98.3%/85.5% PFSA/PFCA figures; the short-chain (C≤6) 92.5–99.1%/80.8–90% figures appear in the record's supported_claim field but are not present in the quoted span, so downstream claims citing those specific numbers cannot be independently verified from the supplied text alone.
- WF10_004b_MMG005's exact_evidence_span is self-flagged as truncated/garbled ('PFHxA was removed Y.'), and it is ambiguous whether PFHeA and PFHeS represent chain-length-matched analogues given a separate compound (PFHxA) is referenced in the same truncated sentence; this ambiguity was not fully resolved for the reference construction.

---

## WF10_036

**Question:** Does longer empty-bed contact time necessarily translate into better PFAS performance in granular activated carbon systems?

**Must include:** Use limitation, uncertainty, caveat, and negative evidence to avoid overclaiming beyond the reported study scope.

**Must not claim:** Do not convert a condition-specific finding into a universal PFAS treatment claim.

### Complete Gold Evidence

**WF10_036_MMG001** (required_gold; `2019 - Park - [SOURCE_TEXT_OMITTED sha256=31fdda8304c0d0a7a0d65ea0a5d6fd070a8aa91a8294dc26eaa9d4ae352d286d].pdf`, chunk `29`)  
Scope: groundwater; granular activated carbon; adsorption  
> 5 B), which means that the apparent adsorption capacity did not change as EBCT increased.  
Supported claim metadata: The apparent adsorption capacity did not change as EBCT increased.

**WF10_036_MMG002** (required_gold; `2020 - Zeng - Removing per- and polyfluoroalkyl substances from groundwaters using activated carbon.pdf`, chunk `16`)  
Scope: ΣPFAS; groundwater; activated carbon; adsorption; 1.07 ± 0.12; ratio (dimensionless)  
> [SOURCE_TEXT_OMITTED sha256=16759fcbe6cc6b6f11a3ab8a8c3e08bc7534bc1dac7cbfdfc4398184827547c0].  
Supported claim metadata: Lead+Lag to Lead column ratios for qΣPFAS were near unity (1.07 ± 0.12), implying adsorption mechanisms are independent of EBCT.

**WF10_036_MMG003** (optional_gold; `2020 - Zeng - Removing per- and polyfluoroalkyl substances from groundwaters using activated carbon.pdf`, chunk `15`)  
Scope: groundwater; activated carbon (RSSCTs); adsorption; 2-5 min; min  
> [SOURCE_TEXT_OMITTED sha256=841e03841b4a8125efc76df319357f9459b66328b79d9fbd905cdc31d4a869e2].  
Supported claim metadata: Longer EBCTs did not suffer from competing adsorbates, and similar breakthrough curve shapes suggest shorter EBCTs (~2–5 min) capture the mass transfer zone.

**WF10_036_MMG004** (optional_gold; `2022 - Kempisty - Granular activated carbon adsorption of perfluoroalkyl acids from ground and surface.pdf`, chunk `37`)  
Scope: PFAAs; ground and surface water; GAC adsorbers; adsorption  
> [SOURCE_TEXT_OMITTED sha256=b332058668356c17d30e3fcf544edf5a269d1a3c4d8864cfe0f83751380be28f].  
Supported claim metadata: No consistent trend was observed whereby either shorter or longer EBCTs resulted in lower carbon usage rates (CURs) for PFAAs.

### Model A Reference Draft

Across the available granular activated carbon studies, longer empty-bed contact time (EBCT) does not necessarily translate into better PFAS performance.

In groundwater GAC columns, one study reported that the apparent adsorption capacity remained unchanged as EBCT increased, indicating that extending EBCT did not enhance PFAS adsorption capacity under those conditions. Another groundwater study using activated carbon columns found that the ratio of ΣPFAS adsorption capacity (qΣPFAS) between a lead–lag configuration and a single lead column was close to unity (1.07 ± 0.12), which the authors interpreted as adsorption mechanisms being independent of EBCT. In the same experimental program, longer EBCTs did not show evidence of suffering from additional competition by co‑adsorbates, and the similarity of breakthrough curve shapes suggested that relatively short EBCTs (~2–5 min) already captured the mass transfer zone, implying no clear added benefit from further EBCT extension within that range.

In GAC adsorbers treating ground and surface waters for perfluoroalkyl acids (PFAAs), comparison of two EBCTs showed that breakthrough curves for individual PFAAs did not produce a consistent trend in carbon usage rate (CUR); neither shorter nor longer EBCTs consistently yielded lower CURs. This indicates that, for these systems, extending EBCT did not systematically improve GAC usage efficiency for PFAA adsorption.

Taken together, these studies show that, under the tested EBCT ranges, water matrices, GAC systems, and PFAS mixtures, longer EBCT did not reliably improve adsorption capacity, adsorption mechanisms, or carbon usage efficiency. Therefore, the claim that longer EBCT necessarily leads to better PFAS performance in GAC systems is not supported by these data. However, these findings are limited to specific PFAS types, groundwater and surface water matrices, particular GAC configurations, and the EBCT ranges studied; they do not establish a universal rule for all PFAS, GAC types, or operating conditions.

Claims:

- `WF10_036-C01` [core]: In a groundwater granular activated carbon system, the apparent adsorption capacity for PFAS did not change as EBCT increased, indicating that longer EBCT did not enhance adsorption capacity under those conditions. (evidence: WF10_036_MMG001)
- `WF10_036-C02` [core]: In groundwater activated carbon columns treating ΣPFAS, the ratio of ΣPFAS adsorption capacity (qΣPFAS) between a Lead + Lag configuration and a Lead-only column was 1.07 ± 0.12, which was interpreted as indicating that adsorption mechanisms were independent of EBCT. (evidence: WF10_036_MMG002)
- `WF10_036-C03` [core]: In rapid small-scale column tests with activated carbon treating groundwater, longer EBCTs did not show additional loss of performance from competing adsorbates, and similar breakthrough curve shapes indicated that shorter EBCTs of approximately 2–5 minutes already captured the mass transfer zone, suggesting no clear performance gain from extending EBCT beyond that range. (evidence: WF10_036_MMG003)
- `WF10_036-C04` [core]: For perfluoroalkyl acids in GAC adsorbers treating ground and surface water, comparison of two EBCTs showed that breakthrough curves did not display a consistent trend where either shorter or longer EBCTs resulted in lower carbon usage rates, indicating that increasing EBCT did not systematically improve carbon usage efficiency. (evidence: WF10_036_MMG004)
- `WF10_036-C05` [supporting]: Across these GAC and activated carbon studies in groundwater and surface water, the reported PFAS performance metrics—apparent adsorption capacity, adsorption mechanisms, breakthrough curve shapes, and carbon usage rate—were largely insensitive to EBCT changes within the tested ranges, so the data do not support a general assertion that longer EBCT necessarily leads to better PFAS performance. (evidence: WF10_036_MMG001, WF10_036_MMG002, WF10_036_MMG003, WF10_036_MMG004)
- `WF10_036-C06` [limitation]: The available evidence on EBCT effects for PFAS adsorption in GAC systems is limited to specific PFAS mixtures or PFAAs, particular groundwater and surface water matrices, specific GAC configurations, and EBCT ranges from a few minutes to on the order of tens of minutes, so these findings cannot be generalized to all PFAS, water qualities, GAC materials, or EBCT conditions. (evidence: WF10_036_MMG001, WF10_036_MMG002, WF10_036_MMG003, WF10_036_MMG004)

### Model B Verification

Overall verdict: **revise**

- `WF10_036-C01`: **supported**. Evidence span states apparent adsorption capacity did not change as EBCT increased, in a groundwater GAC study. The gold record's PFAS_compound field is blank, but the source document title (PFAS adsorption in GAC) supports generic 'PFAS' framing without introducing a specific unverified compound.
  Recommended text: In a groundwater granular activated carbon system, the apparent adsorption capacity did not change as EBCT increased, indicating that longer EBCT did not enhance adsorption capacity under those conditions.
- `WF10_036-C02`: **supported**. Numerical value (1.07 ± 0.12), compound (ΣPFAS), matrix (groundwater), method (activated carbon columns, Lead+Lag vs Lead), and interpretation (adsorption mechanisms independent of EBCT) all match the evidence span exactly, and the claim correctly frames this as the authors' interpretation.
  Recommended text: No change needed.
- `WF10_036-C03`: **supported**. Core content (no competing-adsorbate penalty at longer EBCT; ~2-5 min EBCTs capture the mass transfer zone) is faithfully restated. The closing clause 'suggesting no clear performance gain from extending EBCT beyond that range' is a reasonable but slightly interpretive extension beyond the literal span, though consistent with its logical implication.
  Recommended text: In rapid small-scale column tests with activated carbon treating groundwater, longer EBCTs did not show additional loss of performance from competing adsorbates, and similar breakthrough curve shapes indicated that shorter EBCTs of approximately 2-5 minutes already captured the mass transfer zone.
- `WF10_036-C04`: **supported**. Correctly restates that no consistent trend was observed linking shorter or longer EBCTs to lower CUR for PFAAs, and appropriately avoids citing the specific 13/26 min EBCT values that the gold record flags as unverifiable in the selected span.
  Recommended text: No change needed.
- `WF10_036-C05`: **supported**. Accurate synthesis claim; each cited endpoint (adsorption capacity, mechanisms, breakthrough shape, CUR) traces to its respective evidence record, and the claim stops short of asserting a universal rule.
  Recommended text: No change needed.
- `WF10_036-C06`: **partially_supported**. The phrase 'EBCT ranges from a few minutes to on the order of tens of minutes' is not directly supported by the evidence spans: only MMG003 gives a concrete range (~2-5 min), and the only 'tens of minutes' figures (13/26 min) come from MMG004's metadata, whose limitation field explicitly states those values are 'not verifiable in selected span.' Building a scope characterization on evidence the gold record itself flags as unverifiable is an overreach, even though the surrounding limitation framing (non-generalizability) is otherwise well supported.
  Recommended text: The available evidence on EBCT effects for PFAS adsorption in GAC systems is limited to specific PFAS mixtures or PFAAs, particular groundwater and surface water matrices, specific GAC configurations, and the EBCT values tested in each study, so these findings cannot be generalized to all PFAS, water qualities, GAC materials, or EBCT conditions.

Reference-answer issues:
- The narrative prose (paragraph 4) repeats the same 'tens of minutes'-adjacent framing issue as claim C06 by aggregating EBCT ranges without flagging that one contributing data point (MMG004's 13/26 min) is explicitly marked as unverifiable in its own evidence record.

---

# Test40 L3 project-author audit packet

Status: **40 project-author decisions pending**

This packet was constructed without candidate Test40 answers, candidate
retrieved contexts, system identities, or Test40 outcomes. The claim
ledger is normative for future L3 scoring; reference prose is explanatory
and non-normative. Gold evidence is human-audited and non-exhaustive.

Approve a question only after checking the visible task, every core and
supplementary claim group, every constraint, scoring rules, exact evidence,
and the complete approved source chunks. Newly selected verbatim spans are
listed separately and require an explicit author decision.

## NQ01

**Question:** What analytical methods are reported for PFAS quantification or detection, and how broadly can each method be applied across PFAS applications?

### Task components

- `NQ01-T01`: Identify and list the analytical methods that are reported for PFAS quantification or detection, and for each method describe its basic analytical approach (e.g., instrumental platform or assay type) as characterized in the sources, explicitly distinguishing targeted LC-MS/MS and LC-HRMS workflows from other methods.
- `NQ01-T02`: For each reported method, summarize how broadly it is applied across PFAS analytes, including whether it is used for specific PFAS compounds, classes, or broader PFAS mixtures, and describe any stated limitations or scope of analytes as supported by the cited sources.
- `NQ01-T03`: For each reported method, describe the types of matrices (e.g., environmental, biological, industrial, product-related) and study goals (e.g., routine monitoring, screening, source identification, method development, toxicological studies) for which the method is used or recommended in the sources, and assess method suitability in terms of analyte scope, matrix, and study goal, citing the specific sources that support each suitability statement and any claims about 'gold standard' status or lack thereof.

### Normative claim groups

#### NQ01-G01

- Component: `NQ01-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Targeted LC-MS and LC-MS/MS workflows are widely used for quantitative analysis of specific PFAS (including PFCAs) in water and other environmental samples, are treated as the gold standard for PFCA analysis in water, and are embedded in several US EPA regulatory methods, but they are constrained to predefined target analytes for which reference standards are available.
- Full: Award full credit if the answer: (1) identifies LC-MS and LC-MS/MS as targeted, quantitative methods used for specific PFAS (including explicit mention of PFCAs) in water or environmental matrices; (2) notes that LC-MS and GC-MS are commonly employed for targeted quantitative analysis of specific PFAS; (3) explicitly mentions that LC-MS/MS is described as the gold standard for PFCA analysis; (4) connects LC-MS/MS to US EPA regulatory methods (e.g., Methods 533, 537.1, 8327) with solid-phase extraction for PFAS; and (5) states that these targeted methods require predefined quantification targets and reference standards, thereby limiting detection to only a small fraction of PFAS. The description must clearly distinguish this targeted LC-MS/MS usage and its PFCA-focused 'gold standard' status from claims about universal superiority across all PFAS analyses.
- Partial: Award partial credit if the answer correctly identifies LC-MS or LC-MS/MS as targeted quantitative methods for specific PFAS or PFCAs in water and/or mentions their use in EPA methods or regulatory contexts, but omits either the gold-standard statement, the explicit PFCA focus, or the limitations around predefined targets and reference standards. Partial credit is also appropriate if LC-MS/MS is called a gold standard without restricting that statement to PFCA analysis in water.
- Contradiction: Mark as contradictory if the answer claims that LC-MS/MS (or LC-MS) is a universal gold standard for all PFAS analyses in all matrices, or if it states that targeted LC-MS/MS methods are not limited by predefined targets or reference standards, directly opposing the cited limitations. It is also contradictory to deny that these methods are commonly used for targeted quantitative analysis of specific PFAS compounds.
- Linked exact evidence:
  - `NQ01_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=4c35b22efee4fa653bc3d26dcb296d3e0c4bdd2165d0465486eebe178d706ff7] ].
    Supports: Shows that LC-MS is used as a targeted quantitative mass spectrometry method for specific PFAS compounds.
  - `NQ01_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=b8c69cb705182a18bb613db14fc47c6997e6cca600162d9490dc0a00a9369a97]].
    Supports: Indicates chromatographic methods, including LC variants, are frequently used to determine PFCAs in water matrices.
  - `NQ01_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=0fe4e77bdb36b04229830ec0cfcfdd68681bc2be64ad2bcb5fda25773722db4c]].
    Supports: Explicitly identifies LC-MS/MS as the gold standard for PFCA analysis (scope-limited to PFCAs).
  - `NQ01_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=1956e6fa70863e856d6b2cf66adba5caa7024d0d3be3e15c7f51b217651ed3a8]].
    Supports: Shows LC-MS/MS is used in specific US EPA methods for PFAS, with SPE sample preparation, indicating regulatory targeted application.
  - `NQ01_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=0235e71d5ecd73caa75ede6ed002233b6a7bee874253dc3e354c6f4420d505b5] ].
    Supports: Describes limitations of targeted methods (including LC-MS) in requiring predefined targets and reference standards, restricting PFAS coverage to a few dozen compounds.

#### NQ01-G02

- Component: `NQ01-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Gas chromatography-based methods, including GC-MS and stir bar sorptive extraction coupled with thermal desorption-GC-MS (SBSE-TD-GC-MS), are employed for determination and quantification of PFCAs in water matrices, particularly when relatively high PFCA concentrations are expected, and are presented as optimized, solvent-reducing alternatives to LC-MS/MS for such applications.
- Full: Award full credit if the answer: (1) identifies GC and/or GC-MS as methods used for determination of PFCAs in water matrices; (2) describes SBSE-TD-GC-MS as an analytical method for efficient analysis or quantification of PFCAs in water samples or aquatic environments; (3) notes that SBSE-TD-GC-MS is particularly appropriate when high concentrations (high ppt to low ppb) of PFCAs are expected; and (4) mentions its role as an optimized method that can eliminate the need for organic solvent usage required for desorption in LC-MS/MS methods. The answer should clearly link these GC-based methods to PFCA analysis in water and distinguish them from LC-based targeted workflows.
- Partial: Award partial credit if the answer correctly states that GC or GC-MS methods, including SBSE-TD-GC-MS, are used for PFCA analysis in water but omits either the concentration range, the explicit comparison to LC-MS/MS solvent usage, or the optimization and robustness claims. Partial credit is also appropriate if GC-MS is mentioned for PFAS/PFCAs generally without specifying water matrices.
- Contradiction: Mark as contradictory if the answer claims SBSE-TD-GC-MS is not used for PFCAs in water or denies its efficiency/optimization for such analysis, or if it states that GC-based methods are not used for determination of PFCAs in water matrices, in conflict with the evidence.
- Linked exact evidence:
  - `NQ01_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=4c35b22efee4fa653bc3d26dcb296d3e0c4bdd2165d0465486eebe178d706ff7] ].
    Supports: Shows GC-MS as a traditional analytical approach mentioned alongside LC-MS for PFAS characterization.
  - `NQ01_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=b8c69cb705182a18bb613db14fc47c6997e6cca600162d9490dc0a00a9369a97]].
    Supports: Indicates GC is frequently used to determine PFCAs in water matrices.
  - `NQ01_MMG008`
    > [SOURCE_TEXT_OMITTED sha256=c03a23622f08c5b49f627431372f85b37eefd9c5bb0fef5a7e1c76714633731b].
    Supports: States that SBSE-TD-GC-MS is efficient for analysis of PFCAs in water samples at high ppt to low ppb concentration ranges.
  - `NQ01_MMG008`
    > [SOURCE_TEXT_OMITTED sha256=c03a23622f08c5b49f627431372f85b37eefd9c5bb0fef5a7e1c76714633731b].
    Supports: Describes thermal desorption-GC-MS as an alternative that avoids organic solvents used for desorption in LC-MS/MS workflows.
  - `NQ01_MMG008`
    > [SOURCE_TEXT_OMITTED sha256=c03a23622f08c5b49f627431372f85b37eefd9c5bb0fef5a7e1c76714633731b].
    Supports: Characterizes SBSE-TD-GC-MS as an optimized, validated, simple, sensitive, and robust method for extraction and quantification of PFCAs in aquatic environments.

#### NQ01-G03

- Component: `NQ01-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: High-resolution and non-targeted analytical techniques such as HRMS, FT-ICR MS, and NMR are used to broaden PFAS characterization beyond targeted LC-MS, enabling suspect and non-targeted screening of many known and novel PFAS in complex media like impacted waters and aqueous film-forming foams (AFFF).
- Full: Award full credit if the answer: (1) lists HRMS, FT-ICR MS, and/or NMR as PFAS analytical methods distinct from targeted LC-MS/MS; (2) notes that these methods are used as non-targeted or suspect screening techniques leveraging accurate mass measurements; (3) explicitly connects them to broad PFAS identification in complex impacted waters or similar media; and (4) indicates that FT-ICR MS, in particular, has been used in a suspect and nontargeted workflow to identify large numbers of known and novel PFAS in AFFF. The answer should emphasize their expanded analyte scope compared to targeted LC-MS/MS.
- Partial: Award partial credit if the answer mentions HRMS, FT-ICR MS, or NMR for PFAS analysis but does not clearly describe their non-targeted or suspect screening role, or omits explicit mention of complex media or AFFF. Partial credit is also appropriate if only one of these techniques is discussed in the described non-targeted context.
- Contradiction: Mark as contradictory if the answer claims HRMS/FT-ICR MS/NMR are only used for targeted quantification of a small number of PFAS or denies that they support broader screening or identification of novel PFAS, directly opposing the evidence.
- Linked exact evidence:
  - `NQ01_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=4c35b22efee4fa653bc3d26dcb296d3e0c4bdd2165d0465486eebe178d706ff7] ].
    Supports: Lists NMR, HRMS, and FT-ICR MS as sophisticated analytical methodologies for PFAS characterization beyond traditional LC-MS or GC-MS.
  - `NQ01_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=0235e71d5ecd73caa75ede6ed002233b6a7bee874253dc3e354c6f4420d505b5] ].
    Supports: States that nontargeted methods including NMR, HRMS, and FT-ICR MS are used to identify a broad range of novel PFAS in complex impacted water, via accurate mass and database screening.
  - `NQ01_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=0235e71d5ecd73caa75ede6ed002233b6a7bee874253dc3e354c6f4420d505b5] ].
    Supports: Highlights FT-ICR MS as a preferred method for PFAS analysis in complex media, emphasizing analytical performance features that support broad screening.
  - `NQ01_MMG006`
    > [ [SOURCE_TEXT_OMITTED sha256=a38872a920e50a7b8eea877f6b878c42ec2ffdebe93882ef4fcb9b348a7ff2dc].
    Supports: Describes a suspect and nontargeted FT-ICR MS method applied to AFFF, identifying large numbers of known and novel PFAS, showing broad analyte coverage in a complex PFAS mixture matrix.

#### NQ01-G04

- Component: `NQ01-T01`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: An ion-exchange solid phase microextraction (SPME) method coupled to liquid chromatography/laminar flow tandem mass spectrometry was developed for PFAS determination in aqueous matrices, including various water types, achieving low limits of quantification and demonstrating suitability for quantitative analysis of PFAS with varying physicochemical properties.
- Full: Award full credit for this group if the answer: (1) identifies an SPME-based method coupled to LC-MS/MS (laminar flow tandem MS) as an analytical approach for PFAS; (2) states that it was developed for PFAS in aqueous matrices and applied to river, lake, tap, and bottled water samples; (3) notes that the HLB-WAX/PAN SPME phase was highly selective for PFAS; (4) reports low LOQs on the order of 1–2.5 ng L−1 for model analytes with small sample volumes, highlighting pre-concentration; and (5) mentions its suitability for quantitative analysis of PFAS with varying physicochemical properties and potential extension to more complex matrices.
- Partial: Award partial credit if the answer mentions an SPME-LC-MS/MS method for PFAS in aqueous or water matrices but omits one or more of: the specific water types, the selectivity of the HLB-WAX/PAN phase, the approximate LOQ range, or the broader applicability to PFAS with varying physicochemical properties and to more complex samples.
- Contradiction: Mark as contradictory if the answer asserts that this SPME-LC-MS/MS method was not applied to water samples or was not developed for PFAS, or if it denies its low LOQs or pre-concentration benefits, contrary to the evidence.
- Linked exact evidence:
  - `NQ01_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=469013d9469e2f088c33eba45896cb806c245ec2eb3f3e7be1c475ef589ac4ad].
    Supports: Indicates that an SPME method for PFAS was developed for aqueous matrices and applied to several water types (river, lake, tap, bottled).
  - `NQ01_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=469013d9469e2f088c33eba45896cb806c245ec2eb3f3e7be1c475ef589ac4ad].
    Supports: Shows the specific SPME phase (HLB-WAX/PAN) and its high selectivity for PFAS, as well as potential applicability to more complex samples.
  - `NQ01_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=469013d9469e2f088c33eba45896cb806c245ec2eb3f3e7be1c475ef589ac4ad].
    Supports: Provides LOQ range (1–2.5 ng L−1) and indicates strong pre-concentration performance for PFAS using SPME with small sample volume.
  - `NQ01_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=469013d9469e2f088c33eba45896cb806c245ec2eb3f3e7be1c475ef589ac4ad].
    Supports: States that the method enables highly sensitive quantitative analysis for PFAS with varying physicochemical properties, with LOQs below EPA health advisories.

#### NQ01-G05

- Component: `NQ01-T01`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: In addition to LC and GC approaches, less commonly used analytical methods for PFCA or PFAS determination include nuclear magnetic resonance, Fourier transform infrared spectroscopy, ion chromatography, several sensor-based methods, and the total oxidizable precursor assay, which reveals that many PFCAs in environmental samples are from unidentified compounds.
- Full: Award full credit if the answer: (1) lists at least some of the less commonly used methods—NMR, FTIR, ion chromatography, sensor-based methods—as being applied to PFCA/PFAS analysis; and (2) mentions that the total oxidizable precursor assay has been used to show that a significant fraction of total PFCAs in environmental samples consists of unidentified compounds. The answer should clearly distinguish these from mainline LC- or GC-based quantification.
- Partial: Award partial credit if the answer mentions at least one of the less common methods or the total oxidizable precursor assay in the context of PFCA/PFAS analysis but does not clearly connect them to their roles or to unidentified PFCA fractions.
- Contradiction: Mark as contradictory if the answer claims that no such alternative or less common methods (NMR, FTIR, ion chromatography, sensors, TOP assay) are used for PFCA/PFAS analysis, or denies the TOP assay’s indication of unidentified PFCAs, conflicting with the evidence.
- Linked exact evidence:
  - `NQ01_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=b8c69cb705182a18bb613db14fc47c6997e6cca600162d9490dc0a00a9369a97]].
    Supports: Identifies NMR, FTIR, ion chromatography, and sensor-based methods as less commonly used analytical methods for PFCA-related analysis.
  - `NQ01_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=b8c69cb705182a18bb613db14fc47c6997e6cca600162d9490dc0a00a9369a97]].
    Supports: Describes the total oxidizable precursor assay and its finding that a significant fraction of total PFCAs in environmental samples are from unidentified compounds.

#### NQ01-G06

- Component: `NQ01-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Direct-injection LC-MS has been used to determine the presence of common PFAS chemicals in different types of water, providing a targeted approach for monitoring a defined set of PFAS in multiple water matrices.
- Full: Award full credit if the answer notes that LC-MS operated with a direct injection approach has been used in at least one study (e.g., in Spain) to determine the presence of common PFAS chemicals in different types of water, thereby exemplifying a targeted LC-MS workflow applied across multiple water matrices. Any broader discussion of limitations on analyte scope for such methods may be credited under other groups but is not required for full credit in this group.
- Partial: Award partial credit if the answer correctly associates direct-injection LC-MS with PFAS determination in water but omits either the multi-matrix aspect (different types of water) or the fact that this is a targeted approach for common PFAS.
- Contradiction: Mark as contradictory if the answer asserts that LC-MS with direct injection has not been used to determine PFAS in water, or claims that such an approach cannot be applied to common PFAS in multiple water types, in conflict with the evidence.
- Linked exact evidence:
  - `NQ01_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=0235e71d5ecd73caa75ede6ed002233b6a7bee874253dc3e354c6f4420d505b5] ].
    Supports: Shows direct injection LC-MS being used to determine common PFAS chemicals in different water types.
  - `NQ01_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=0235e71d5ecd73caa75ede6ed002233b6a7bee874253dc3e354c6f4420d505b5] ].
    Supports: Provides general limitations for targeted regulatory methods; the associated analyte-scope limitation is primarily treated in another group and need not be separately scored here.

#### NQ01-G07

- Component: `NQ01-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: US EPA Method 1633 (or 1633 A) is a targeted LC-MS/MS-based method that quantifies on the order of 40 PFAS, illustrating the limited analyte scope of current regulatory targeted methods relative to the thousands of PFAS in commercial use and environmental media.
- Full: Award full credit if the answer notes that USEPA Method 1633 (or 1633 A) is a targeted PFAS method that quantifies about 40 PFAS, and explicitly interprets this as evidence that the analyte scope of such regulatory targeted methods is narrow compared with the thousands of PFAS in use and in environmental media.
- Partial: Award partial credit if the answer mentions Method 1633 as targeting a limited number of PFAS without giving an approximate number, or notes the approximately 40 PFAS but does not discuss the contrast with the thousands of PFAS present.
- Contradiction: Mark as contradictory if the answer claims that Method 1633 quantifies all or most PFAS in commercial use/environmental media, or denies that its analyte list is limited, opposing the evidence.
- Linked exact evidence:
  - `NQ01_MMG007`
    > [SOURCE_TEXT_OMITTED sha256=89cb84ea4c5e5592ce764d938a9a127127f1aa4183d5472a8929c4a75557ee71].
    Supports: Explicitly states that USEPA Method 1633 A quantifies about 40 PFAS while thousands exist, demonstrating limited analyte scope.

#### NQ01-X01

- Component: `NQ01-T03`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: No single analytical method is broadly applicable across all PFAS-related matrices; in particular, methods for PFAS analysis in wastewater sludges and biosolids lack a widely recognized standard and individual methods are not broadly applicable over diverse sludge/biosolid matrices.
- Full: Use this as a constraint: any answer should avoid implying that a single PFAS analytical method is broadly applicable across all matrices, especially sludge and biosolids. Full adherence requires acknowledging that for wastewater sludges and biosolids there is no widely recognized standard method and that individual methods do not work broadly across all such matrices.
- Partial: An answer may still receive content credit if it omits sludge/biosolid-specific caveats, but such omission should be noted as a limitation relative to this constraint.
- Contradiction: Flag as violating the constraint if the answer explicitly claims that PFAS analysis in sludge/biosolids has a widely recognized standard method or that a single method works broadly across all sludge/biosolid matrices, contradicting the evidence.
- Linked exact evidence:
  - `NQ01_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=7b505293f0345d09e8e48a5101e89b3ce4f15427f69038a0e495a50276daab11].
    Supports: Shows that PFAS analysis in sludge/biosolids lacks a widely recognized standard and that individual methods are not broadly applicable across different sludge/biosolid matrices.

#### NQ01-X02

- Component: `NQ01-T03`
- Importance: `supplementary`
- Scoring role: `constraint_only`
- Proposition: Targeted LC-based PFAS methods, although crucial for regulatory purposes, face challenges such as background contamination, so they should not be portrayed as universally sufficient or trouble-free for PFAS monitoring across all matrices.
- Full: Use this constraint to prevent overclaiming about the robustness of targeted LC-based methods: answers should not present LC-centered targeted methods as universally free from contamination issues or artifacts, given documented background contamination from PFAS-containing materials in the analytical system. Full adherence involves at least not contradicting these limitations and, where relevant, acknowledging the need to control such contamination sources.
- Partial: Answers that do not mention these contamination limitations are acceptable for content scoring but may be considered incomplete with respect to constraints.
- Contradiction: Flag as violating the constraint if an answer claims that LC-centered targeted methods have no contamination issues or that background PFAS from system components is not a concern, directly opposing the evidence.
- Linked exact evidence:
  - `NQ01_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=b8c69cb705182a18bb613db14fc47c6997e6cca600162d9490dc0a00a9369a97]].
    Supports: Describes background contamination issues affecting LC-centered PFAS methods, indicating methodological challenges.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

Across the supplied sources, several distinct analytical approaches are described for PFAS quantification or detection, with differing analyte scope, matrices, and study goals.

Targeted LC-based methods

Targeted LC-MS and LC-MS/MS workflows are consistently presented as core tools for quantitative PFAS determination. One review notes that “[SOURCE_TEXT_OMITTED sha256=29824bfe89daff422cfedc78a07b9fbd18e874aa4133380b34cb00ee4d6f53b3].” (NQ01_MMG001), emphasizing their role in targeted quantification. In PFCA-focused work, chromatographic methods including GC, HPLC, and UHPLC “are frequently used for the determination of PFCAs in water matrices” (NQ01_MMG002), and within this context “[SOURCE_TEXT_OMITTED sha256=c0e8ba62d2294f47251ff679beb9c7026b36d3cb35ff9c1c10c07bb8c48ca353])” (NQ01_MMG002). Thus, LC-MS/MS is explicitly framed as a gold standard for PFCA analysis, specifically in water matrices, rather than universally for all PFAS.

Regulatory targeted methods based on LC-MS/MS are also highlighted. Habib et al. state that “[SOURCE_TEXT_OMITTED sha256=b72bd66cf34f800b5e6d9caa07562df2c7b703fdef5eae1cf1e24cd9212049ac]” (NQ01_MMG002), indicating a coupling of SPE with LC-MS/MS for regulated PFAS determination in water. Another source notes that “[SOURCE_TEXT_OMITTED sha256=4ffe1d8b46bca16f4e633bcd845e432edd6cb13f454395a5b1a162e240ce3c88]” (NQ01_MMG004), illustrating application of targeted direct-injection LC-MS for common PFAS in multiple water types.

However, the same review stresses that these targeted methods, while crucial for regulatory purposes, “[SOURCE_TEXT_OMITTED sha256=01db980486e5eb3a4dcb667c34c4e8775599e21c7aebb0a968074ddeb6529642].” (NQ01_MMG004). Likewise, another regulatory method, “[SOURCE_TEXT_OMITTED sha256=89cb84ea4c5e5592ce764d938a9a127127f1aa4183d5472a8929c4a75557ee71].” (NQ01_MMG007). Together, these statements show that targeted LC-MS/MS and related LC-MS methods are suitable for routine monitoring and compliance of a defined PFAS list (e.g., several dozen PFAS including PFCAs) in water and wastewater-related matrices, but they cannot be assumed to capture the full diversity of PFAS.

The LC-centered methods also face practical challenges. Habib et al. note that “[SOURCE_TEXT_OMITTED sha256=5eb640b4df25166d263f26a6db6ac04505c73603522119d3971b221e9f735be3] … as they are sources of back-” (NQ01_MMG002). This underscores that, for PFAS monitoring in water, LC-based methods require careful control of materials to mitigate background contamination, particularly in low-level monitoring applications.

Gas chromatography-based methods

In addition to LC-based techniques, GC and GC-MS are also used. Sanzana et al. list “traditional approaches such as gas chromatography – mass spectrometry (GC – MS) and liquid chromatography-mass spectrometry (LC-MS)” among analytical methodologies for PFAS characterization (NQ01_MMG001). Habib et al. specify that “gas chromatography (GC)… are frequently used for the determination of PFCAs in water matrices” (NQ01_MMG002), showing that GC-based workflows can target PFCAs in water.

A more specialized GC-MS method combines stir bar sorptive extraction and thermal desorption: “[SOURCE_TEXT_OMITTED sha256=cc95b9c6fab854c7cdf5efadc2807d37187396c6662f5f9ebbbf2ce1d865aaae].” (NQ01_MMG008). The same study notes that “[SOURCE_TEXT_OMITTED sha256=fefb39c48ff9ddcf9888161a749d6475a5158c1cb2e91a8620e6dc981bd9c10e]” (NQ01_MMG008), positioning SBSE-TD-GC-MS as a solvent-saving alternative to LC-MS/MS for PFCA analyses in aquatic environments. The authors describe this as “an [SOURCE_TEXT_OMITTED sha256=d0c2574a72481ea43136c5934b36e932a65fb7cb5da65d62d69a8cab38ea6671].” (NQ01_MMG008). This indicates suitability for quantifying a defined set of PFCAs in water when concentrations are expected to be relatively high (high ppt–low ppb), including in method-development or higher-level monitoring scenarios, rather than ultra-trace screening.

Non-targeted and high-resolution methods (HRMS, FT‑ICR MS, NMR)

Beyond targeted LC and GC, the corpus describes more advanced platforms intended to broaden PFAS coverage. Sanzana et al. list “sophisticated methodologies like nuclear magnetic resonance (NMR) spectroscopy, high-resolution mass spectrometry (HRMS), and Fourier-transform ion cyclotron resonance mass spectrometry (FT-ICR MS)” (NQ01_MMG001) as PFAS characterization tools. In discussing limitations of targeted approaches, the same review argues that “[SOURCE_TEXT_OMITTED sha256=679cc2cd0b388a8422fc224f54721dc3ad294af2f3039bf90fb988e0fde3efcc] measurements, [SOURCE_TEXT_OMITTED sha256=c68dff01a9c0c4b47f7759eac809b51a82016fcadf46e5af74815a06ca77333b]” (NQ01_MMG004). They further note that “[SOURCE_TEXT_OMITTED sha256=73a0d93ec5af6acb6ac09381cfc9388df3be6eb5efbdd05fe7e0a8e1745566de].” (NQ01_MMG004).

A concrete example is provided for aqueous film-forming foam (AFFF), a complex PFAS mixture: “[SOURCE_TEXT_OMITTED sha256=5e33e1502e3d953f5ae11c4fc271a6c81345c0a0e05616b37799f30c23554a7a].” (NQ01_MMG006). This demonstrates that high-field FT‑ICR MS, operated in suspect and non-targeted modes, can detect and tentatively identify hundreds of PFAS in a highly complex industrial product matrix. These methods are therefore well suited to exploratory screening and source characterization in complex media (e.g., AFFF, impacted waters), where the aim is discovery and structural characterization of known and novel PFAS rather than routine quantification of a fixed list.

SPME-LC-MS/MS for aqueous PFAS

An additional LC-MS/MS workflow uses an ion-exchange solid phase microextraction format. Olomukoro et al. report that “[SOURCE_TEXT_OMITTED sha256=b5c0192bf9863de67e354a26716488397eb1784f6058a5ad312d1197bcd8629b].” (NQ01_MMG005). They describe that “[SOURCE_TEXT_OMITTED sha256=5fc2e7cd20b771f94289aa8548a66edf6722775ae0110e4e6f5cf1a63ba0bb2c] further studies of more complex samples in light of its biocompatibility.” (NQ01_MMG005). Regarding performance, “This developed protocol [SOURCE_TEXT_OMITTED sha256=52a5154b9f686965276f407be449066d31486bd6b8d0dc381320e6522fb03e57].” (NQ01_MMG005). The authors emphasize that “a highly sensitive quantitative analysis can be performed for PFAS of varying physicochemical properties, achieving LOQs below current EPA drinking water health advisories.” (NQ01_MMG005).

This method thus combines sample preparation (SPME with HLB-WAX/PAN) and LC/laminar flow tandem MS detection. It is applied to environmental and drinking water types (river, lake, tap, bottled water) and is explicitly positioned for sensitive quantitative analysis at low ng L−1 levels, suitable for monitoring PFAS near or below regulatory guidelines, and potentially extendable to more complex aqueous matrices.

Other less commonly used methods and TOP assay

Habib et al. also mention several other techniques: “Less commonly used methods include nuclear magnetic resonance, Fourier transform infrared spectroscopy, ion chromatography, and several sensor-based methods [42–45].” (NQ01_MMG002). While detailed matrices and analyte lists are not given in this excerpt, these platforms are presented as additional, non-routine options in the PFCA/PFAS analytical toolbox.

In terms of capturing precursors, “[SOURCE_TEXT_OMITTED sha256=d5807eb88954dc141aab727575bd80b40a84d5a481357e8f4c8130b12d67b219]” (NQ01_MMG002). The total oxidizable precursor assay is therefore used as a bulk measure of oxidizable PFCA precursors, indicating that standard targeted methods detect only part of the PFCA burden and that many PFCAs arise from previously unidentified precursors in environmental samples.

Matrix- and application-specific limitations

The suitability and generalizability of these methods are constrained by matrix and study goals. For sludge and biosolids, Ozelcaglayan et al. note that “[SOURCE_TEXT_OMITTED sha256=7da24b1c25d188587ae1ce913638aa9b0e833aeb28102a7536457ad7ca3006d8].” (NQ01_MMG003). This indicates that approaches optimized for water (e.g., EPA LC-MS/MS methods, SPME-LC-MS/MS, or SBSE-TD-GC-MS) cannot be assumed to perform universally across solid or highly heterogeneous matrices, and matrix-specific method development and cleanup are critical.

More broadly, the limitations of targeted LC-based regulatory methods (predefined analyte lists, restricted standards, background contamination) mean they are well suited to routine monitoring and regulatory compliance of known PFAS in relatively well-characterized matrices (e.g., drinking water, some wastewaters), but not to comprehensive PFAS discovery or full mass-balance closure. In contrast, non-targeted HRMS/FT-ICR MS and related techniques are better aligned with goals such as broad screening, source identification, and characterization of complex PFAS mixtures (e.g., AFFF, impacted waters). GC-based SBSE-TD-GC-MS provides an optimized option for PFCAs in water at higher concentrations, whereas SPME-LC-MS/MS targets low-level quantitative analysis of a range of PFAS in drinking and surface waters.

Overall, the cited studies collectively support a portfolio view: targeted LC-MS/MS (including EPA methods and direct-injection LC-MS) for specific PFAS/PFCAs in water with defined regulatory goals; GC-based methods including SBSE-TD-GC-MS for PFCAs in water, especially at higher concentrations; non-targeted HRMS/FT-ICR MS (and NMR) for broad PFAS screening in complex waters and AFFF; SPME-LC-MS/MS for sensitive PFAS quantification in aqueous matrices; and additional methods such as FTIR, ion chromatography, sensor-based approaches, and the total oxidizable precursor assay as complementary tools. None of the sources claim any single method as universally optimal across all PFAS analytes, matrices, and applications.

### Unresolved or unsupported boundaries

- Specific details of LC-HRMS targeted workflows (as distinct from generic HRMS or FT-ICR MS non-targeted applications) are not described in the supplied evidence.
- Applications of these methods in biological tissues, food, or other non-aqueous product matrices (beyond AFFF and sludge/biosolids) are not detailed in the provided texts.
- Use of these analytical methods for toxicological studies (e.g., PFAS measurements in in vitro or in vivo exposure experiments) is not discussed in the cited evidence.
- Comparative performance metrics across methods (e.g., relative sensitivity of LC-MS/MS vs. HRMS vs. GC-MS for the same PFAS set) are not provided in the supplied material.
- Any claim that LC-MS/MS is a gold standard for PFAS classes beyond PFCAs or for matrices beyond water is not supported by the cited passages.

### Complete approved source chunks

#### NQ01_MMG001

- Role: `required_gold`
- Document: `2025 - Sanzana - “A review of PFAS remediation - Separation and degradation technologies for water and wastewater treatment”.pdf`
- Chunk: `8`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=4c35b22efee4fa653bc3d26dcb296d3e0c4bdd2165d0465486eebe178d706ff7] ].

```text
[SOURCE_TEXT_OMITTED sha256=126971cad328d2e9e779a65ffb01c6eeeb60138cf94c69d493b5485ec9b042da]
```

#### NQ01_MMG002

- Role: `required_gold`
- Document: `2024 - Habib - Green Analytical Method for Perfluorocarboxylic Acids (PFCAs) in Water of Stir Bar Sorptive Extraction Coupled with Thermal Desorption-Gas.pdf`
- Chunk: `6`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=b8c69cb705182a18bb613db14fc47c6997e6cca600162d9490dc0a00a9369a97]].

```text
[SOURCE_TEXT_OMITTED sha256=4c0731bd7c660636f5575a2a78febdae8233bbb1dcb37430674db7c472dbf6df]-
```

#### NQ01_MMG003

- Role: `negative_gold`
- Document: `2023 - Ozelcaglayan - The analysis of per- and polyfluoroalkyl substances in wastewater sludges and biosolids - which adsorbents should be used.pdf`
- Chunk: `0`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=7b505293f0345d09e8e48a5101e89b3ce4f15427f69038a0e495a50276daab11].

```text
[SOURCE_TEXT_OMITTED sha256=f0498c585efbb83600dfcf921648d0d06598438c59e35513ebc33178fba26936]
```

#### NQ01_MMG004

- Role: `negative_gold`
- Document: `2025 - Sanzana - “A review of PFAS remediation - Separation and degradation technologies for water and wastewater treatment”.pdf`
- Chunk: `9`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=0235e71d5ecd73caa75ede6ed002233b6a7bee874253dc3e354c6f4420d505b5] ].

```text
[SOURCE_TEXT_OMITTED sha256=3902039f9fee863b18ef97461212ccb2f2b9358c447e52bfe1a5ae5bfbf37530]
```

#### NQ01_MMG005

- Role: `optional_gold`
- Document: `2021 - Olomukoro - Ion exchange solid phase microextraction coupled to liquid chromatography - laminar flow tandem mass spectrometry for the determination of.pdf`
- Chunk: `36`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=469013d9469e2f088c33eba45896cb806c245ec2eb3f3e7be1c475ef589ac4ad].

```text
[SOURCE_TEXT_OMITTED sha256=dc000fb4fa1215b5812a219eb8c5ade5002eb6143b7014b1c329b3cf38da69ac]
```

#### NQ01_MMG006

- Role: `optional_gold`
- Document: `2025 - Sanzana - “A review of PFAS remediation - Separation and degradation technologies for water and wastewater treatment”.pdf`
- Chunk: `10`
- Registered exact span: [ [SOURCE_TEXT_OMITTED sha256=a38872a920e50a7b8eea877f6b878c42ec2ffdebe93882ef4fcb9b348a7ff2dc].

```text
[SOURCE_TEXT_OMITTED sha256=5937029cbed86b6c29a762568f40751333cc9af5e6b1f464c2612af72165193f]
```

#### NQ01_MMG007

- Role: `negative_gold`
- Document: `2026 - Modiri - Practical Framework for Managing PFAS in Wastewater Treatment Plants Integrating.pdf`
- Chunk: `8`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=89cb84ea4c5e5592ce764d938a9a127127f1aa4183d5472a8929c4a75557ee71].

```text
[SOURCE_TEXT_OMITTED sha256=be202b18e8e5882a7de1729f1346866ba6dc74846df3766fab2512a58dd1bd8a] ).
```

#### NQ01_MMG008

- Role: `optional_gold`
- Document: `2024 - Habib - Green Analytical Method for Perfluorocarboxylic Acids (PFCAs) in Water of Stir Bar Sorptive Extraction Coupled with Thermal Desorption-Gas.pdf`
- Chunk: `59`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=c03a23622f08c5b49f627431372f85b37eefd9c5bb0fef5a7e1c76714633731b].

```text
[SOURCE_TEXT_OMITTED sha256=8cb84918c5e9e6713d90bbb4a93b629134b3a85419502ddf45305c5c69d98f9c]%.
```

---

## NQ02

**Question:** What QA/QC practices are reported for PFAS quantification, and which important QA/QC details are missing or inconsistently described?

### Task components

- `NQ02-T01`: Identify and list all QA/QC practices explicitly reported for PFAS quantification, capturing multiple distinct QA/QC elements where present (e.g., types of controls, checks, calibrations, or evaluations), and describe them strictly as reported without adding best-practice recommendations, acceptance criteria, or frequencies that are not stated.
- `NQ02-T02`: Identify which important QA/QC details for PFAS quantification are missing, incompletely specified, or inconsistently described (e.g., absent or vague information on procedures, criteria, or implementation details), describing only the gaps or inconsistencies without inferring or supplying missing information from general laboratory knowledge or external best practices.

### Normative claim groups

#### NQ02-G01

- Component: `NQ02-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: The study performed HRMS instrument quality control by injecting methanol before and after standard injections to assess contamination in the LC system.
- Full: Award full credit if the answer states that, for HRMS instrument quality control, the authors injected methanol before and after standard injections specifically to assess contamination in the LC system.
- Partial: Award partial credit if the answer mentions methanol injections as some form of instrument QC or blank check but omits that they were done both before and after standard injections or does not clearly link them to assessing contamination in the LC system.
- Contradiction: Flag a contradiction if the answer claims that no instrument QC using methanol was performed, or misstates that methanol was used only as a mobile phase or solvent without any QC role.
- Linked exact evidence:
  - `NQ02_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=2cb0561aad2e14eaf98b9c73898b1d3b717d18124326289da48533823a409932].
    Supports: Explicitly describes a QA/QC practice: methanol injections used as HRMS instrument quality control before and after standards to assess contamination in the LC system.

#### NQ02-G02

- Component: `NQ02-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: The study implemented internal mass calibration for each analysis by infusing a sodium acetate solution at the beginning of the analysis.
- Full: Award full credit if the answer notes that internal mass calibration was conducted for each analysis using an infused 2 mM sodium acetate solution in a 1:1 water:methanol mixture at the beginning of the analysis (0.1–0.5 min).
- Partial: Award partial credit if the answer states that internal mass calibration was performed with sodium acetate but omits one or more details such as concentration, solvent composition, or timing.
- Contradiction: Flag a contradiction if the answer claims that no internal mass calibration was performed or attributes calibration to a different compound or method than sodium acetate infusion as described.
- Linked exact evidence:
  - `NQ02_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=8e3ef463aa25b4baa90768f168e752423ec075b947d9e2672785e6d23d2ce5ef]).
    Supports: Describes internal mass calibration, including that it was done for each analysis, using 2 mM sodium acetate in 1:1 water:methanol, at 0.1–0.5 min at the beginning of the analysis.

#### NQ02-G03

- Component: `NQ02-T01`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: The study reports limits of quantification and recoveries for the PFAS analysis, referring to tables and prior work for details.
- Full: Award full credit if the answer notes that limits of quantification and recoveries were reported (with mention of Tables S1 and S3 or a reference to further details).
- Partial: Award partial credit if the answer mentions only that limits of quantification or recoveries were reported, but not both, or omits the mention of tables or referenced methods.
- Contradiction: Flag a contradiction if the answer asserts that limits of quantification and recoveries were not reported or were unavailable.
- Linked exact evidence:
  - `NQ02_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=309205f5cd7114aee6cb537aa48051f7ff5b4a86cfdd9c57f5e18b98d8723d9d].
    Supports: Indicates that limit of quantification and recoveries were determined and are available in Tables S1 and S3, with additional details in a referenced source.

#### NQ02-G04

- Component: `NQ02-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Procedural blanks were used, and PFBS, PFOA, and PFOS data were excluded due to high and inconsistent detection in these blanks, while other PFAS were below the limit of quantification in blanks.
- Full: Award full credit if the answer states that procedural blanks were assessed, that PFBS, PFOA, and PFOS (linear and branched) were excluded from further data analysis due to high and inconsistent detection in these blanks, and that other PFAS were below the limit of quantification in the blanks.
- Partial: Award partial credit if the answer mentions use of blanks and exclusion of some PFAS due to blank contamination but omits the specific compounds or the note that other PFAS were below the limit of quantification in blanks.
- Contradiction: Flag a contradiction if the answer claims that blanks were not used, or that PFBS, PFOA, and PFOS were retained despite high blank contamination, contrary to the described exclusion.
- Linked exact evidence:
  - `NQ02_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=d5a57374165c32ea8016608e74acb70077ec1a90e17199425a94762f405d0fbe] ).
    Supports: Shows that procedural blanks were evaluated, some PFAS (PFBS, PFOA, PFOS) showed high and inconsistent detection in blanks and were excluded from analysis, and that other PFAS were below the limit of quantification in blanks.

#### NQ02-G05

- Component: `NQ02-T01`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: The study assessed sorption of PFAS to HDPE plastic bottle walls over 24 h and 96 h and reported that no PFAS sorbed to the bottle walls.
- Full: Award full credit if the answer notes that the sorption of PFAS to HDPE plastic bottle walls was evaluated at 24 h and 96 h and that no PFAS sorption to the bottle walls was observed.
- Partial: Award partial credit if the answer mentions that potential sorption to container walls was assessed but omits the specific time points or the conclusion that no sorption occurred.
- Contradiction: Flag a contradiction if the answer states that no evaluation of PFAS sorption to bottle walls was done, or that sorption to HDPE walls was observed, which would conflict with the reported result of no PFAS sorbed.
- Linked exact evidence:
  - `NQ02_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=0ce5214815a55ea806b8b6e176d3ee46c579e0e867103c40edabe32d465c97ac].
    Supports: Describes an experimental check on PFAS sorption to HDPE bottle walls at 24 and 96 hours and reports that no PFAS sorbed, representing a QA/QC-like control on sample handling losses.

#### NQ02-G06

- Component: `NQ02-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: The description of methanol-based HRMS instrument quality control lacks details such as acceptance criteria, quantitative thresholds for contamination, and the number or frequency of methanol injections beyond occurring before and after standards.
- Full: Award full credit if the answer notes that, although methanol injections before and after standard injections were used as instrument QC, the description does not provide acceptance criteria, contamination thresholds, or other implementation details (e.g., how results from these injections were evaluated).
- Partial: Award partial credit if the answer mentions that some details of the methanol injection QC are missing or vague but does not clearly specify that acceptance criteria or thresholds are not described.
- Contradiction: Flag a contradiction if the answer invents explicit acceptance criteria or contamination thresholds for the methanol injections that are not present in the text, or claims that detailed criteria are provided.
- Linked exact evidence:
  - `NQ02_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=2cb0561aad2e14eaf98b9c73898b1d3b717d18124326289da48533823a409932].
    Supports: Shows what is reported (methanol injections before and after standards to assess contamination) and, by omission, that no acceptance criteria, thresholds, or detailed evaluation procedures are specified for this QC step.

#### NQ02-G07

- Component: `NQ02-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: The description of internal mass calibration specifies the reagent, solvent mixture, concentration, and timing, but does not report calibration performance criteria, acceptance limits, or how calibration adequacy was evaluated.
- Full: Award full credit if the answer explains that although the internal mass calibration procedure (sodium acetate solution, solvent, timing) is provided, there is no mention of performance or acceptance criteria for calibration quality.
- Partial: Award partial credit if the answer notes that calibration quality or criteria are not discussed but does not clearly tie this to the otherwise detailed calibration conditions.
- Contradiction: Flag a contradiction if the answer asserts that specific calibration performance criteria or numerical acceptance limits are provided, which are not present in the text.
- Linked exact evidence:
  - `NQ02_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=8e3ef463aa25b4baa90768f168e752423ec075b947d9e2672785e6d23d2ce5ef]).
    Supports: Details the calibration procedure but does not report any calibration performance metrics or acceptance criteria, highlighting a gap in QA/QC specification.

#### NQ02-G08

- Component: `NQ02-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Although limits of quantification and recoveries are said to be reported in supplementary tables and a reference, the excerpt does not specify how these were determined or any acceptance criteria related to them.
- Full: Award full credit if the answer points out that while LOQ and recoveries are said to be reported (with reference to tables and another work), this text does not describe how they were obtained or what criteria were applied.
- Partial: Award partial credit if the answer generically notes that details of LOQ or recovery determination are missing, without clearly distinguishing between being reported elsewhere and not described here.
- Contradiction: Flag a contradiction if the answer fabricates specific LOQ calculation methods, recovery procedures, or acceptance criteria as if they were described in this text.
- Linked exact evidence:
  - `NQ02_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=309205f5cd7114aee6cb537aa48051f7ff5b4a86cfdd9c57f5e18b98d8723d9d].
    Supports: Shows that LOQ and recoveries are reported in external tables/references but that the present excerpt does not provide methodological details or criteria for these QA/QC metrics.

#### NQ02-G09

- Component: `NQ02-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: The description of procedural blanks and resulting data exclusion does not provide information on blank frequency, number of blanks, or explicit criteria used to define 'high and inconsistent' detection.
- Full: Award full credit if the answer notes that, although procedural blanks were evaluated and led to exclusion of certain PFAS, the description lacks information on blank frequency, number, and quantitative or explicit criteria defining 'high and inconsistent' detection.
- Partial: Award partial credit if the answer mentions that criteria or frequency for blanks are missing but does not clearly describe all of these missing aspects.
- Contradiction: Flag a contradiction if the answer invents a specific number, frequency, or explicit numerical thresholds for procedural blanks that are not given in the text.
- Linked exact evidence:
  - `NQ02_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=d5a57374165c32ea8016608e74acb70077ec1a90e17199425a94762f405d0fbe] ).
    Supports: Indicates that procedural blanks were used and affected data interpretation, but does not state how many blanks were run, how frequently, or what numerical criteria defined 'high and inconsistent' detection, revealing missing QA/QC detail.

#### NQ02-G10

- Component: `NQ02-T02`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: The evaluation of sorption of PFAS to HDPE bottle walls provides only the time points and a qualitative outcome, without describing experimental design details such as number of replicates or quantitative detection limits relevant to this check.
- Full: Award full credit if the answer highlights that, while the study states that sorption to HDPE bottle walls was evaluated and not observed at 24 and 96 hours, it does not describe methodological details such as number of replicates, detection limits, or analytical approach for this check.
- Partial: Award partial credit if the answer generically notes that the sorption evaluation is qualitatively described without detailed methodology.
- Contradiction: Flag a contradiction if the answer specifies experimental design details (e.g., number of replicates or detection limits) as if they were stated in the text, when they are not.
- Linked exact evidence:
  - `NQ02_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=0ce5214815a55ea806b8b6e176d3ee46c579e0e867103c40edabe32d465c97ac].
    Supports: Provides only time points and a qualitative result for the sorption check, allowing identification of missing details such as replicates and detection limits.

#### NQ02-X01

- Component: `NQ02-T01`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: The text does not report other common QA/QC practices such as surrogate or internal standards, calibration curve characteristics, or replicate analyses, and these must not be inferred or added.
- Full: Treat as a constraint that only QA/QC elements explicitly mentioned in the text may be listed; do not infer additional QA/QC practices (such as surrogates, calibration curves, or replicates) that are not described.
- Partial: Mention that some QA/QC elements are not discussed, but avoid speculating about their presence or absence beyond the text.
- Contradiction: Flag a violation if the answer asserts specific QA/QC practices (e.g., surrogate standards, multi-point calibration, replicates) as if they were reported, when there is no mention of them in the excerpt.
- Linked exact evidence:
  - `NQ02_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=44ad0c6d86f8cf6355a3b19a038109e1cd26065741b7900d293ef10536ebcccf] ).
    Supports: Shows the full set of QA/QC-related elements actually mentioned and, by omission, that additional common QA/QC practices (e.g., surrogates, calibration curves, replicates) are not described here.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

Reported QA/QC practices for PFAS quantification in the provided study include several distinct elements:

1. HRMS instrument contamination check using methanol injections:
The authors state that, "[SOURCE_TEXT_OMITTED sha256=2cb0561aad2e14eaf98b9c73898b1d3b717d18124326289da48533823a409932]." This describes an instrument quality control step consisting of methanol injections immediately surrounding the standard injections, used specifically to evaluate potential contamination in the LC system.

2. Internal mass calibration for each analysis:
The study reports that, "[SOURCE_TEXT_OMITTED sha256=8e3ef463aa25b4baa90768f168e752423ec075b947d9e2672785e6d23d2ce5ef])." This indicates that every analysis included an internal mass calibration step, with the calibration solution composition (2 mM sodium acetate in 1:1 water:methanol) and the time window of infusion (0.1–0.5 min at the beginning of the run) explicitly defined.

3. Reporting of limits of quantification and recoveries:
The authors note that, "[SOURCE_TEXT_OMITTED sha256=19400778d23982c8d67fe3200d8a57311c0b253729aca0dcda5bf862431b114c]." Thus, limits of quantification and recoveries were determined and documented, with numerical values and methodological details provided in supplementary tables and a referenced publication, even though those details are not given in this excerpt.

4. Use of procedural blanks and data exclusion based on blank contamination:
The text states, "[SOURCE_TEXT_OMITTED sha256=7366568c3345aa47719e41c054ff3c555daf05643ac6609e3a8d4da762a20150])." This shows that procedural blanks were analyzed, that some PFAS (PFBS, PFOA, PFOS) showed high and inconsistent levels in the blanks, leading to their exclusion from subsequent data analysis, and that all other PFAS were below the limit of quantification in the blanks.

5. Evaluation of PFAS sorption to HDPE bottle walls:
The authors also report that, "[SOURCE_TEXT_OMITTED sha256=0ce5214815a55ea806b8b6e176d3ee46c579e0e867103c40edabe32d465c97ac]." This indicates an experimental check on potential PFAS loss to HDPE container walls at two time points, with the outcome that no sorption to bottle walls was detected.

Within this description, multiple important QA/QC details are missing or incompletely specified:

1. Details of methanol-based instrument QC implementation and criteria:
Although methanol injections before and after standard injections are clearly identified as HRMS instrument quality control to assess LC system contamination, the text does not provide any acceptance criteria or quantitative thresholds for judging contamination, nor does it describe how the results from these methanol injections were evaluated or used to qualify or reject runs. Only the existence, timing, and qualitative purpose of these injections are reported.

2. Calibration performance criteria for internal mass calibration:
The internal mass calibration procedure is described in terms of solution composition, concentration, and timing, but the excerpt does not report calibration performance indicators (e.g., mass accuracy metrics) or any acceptance limits for calibration quality. Thus, while the calibration step itself is documented, criteria for determining whether calibration was adequate are not specified here.

3. Lack of procedural detail and criteria for limits of quantification and recoveries in this excerpt:
The sentence, "[SOURCE_TEXT_OMITTED sha256=19400778d23982c8d67fe3200d8a57311c0b253729aca0dcda5bf862431b114c]," indicates that LOQ and recovery information exists elsewhere. However, this excerpt does not describe the procedures used to determine LOQ or recoveries, nor does it present any acceptance criteria or performance thresholds associated with these parameters. From the provided text alone, the methodological and evaluative details for these QA/QC metrics remain unspecified.

4. Incomplete specification of procedural blank implementation and decision rules:
While the authors explain that PFBS, PFOA, and PFOS were excluded due to "high and inconsistent" detection in procedural blanks and that other PFAS were below the limit of quantification in the blanks, the description does not state how many blanks were analyzed, how frequently blanks were run, or what quantitative levels defined "high and inconsistent" detection. Thus, important implementation details and explicit decision criteria for using blank results in data acceptance or exclusion are not reported in this excerpt.

5. Limited methodological detail for the HDPE sorption evaluation:
For the sorption check, the text provides only that sorption to HDPE plastic bottle walls was evaluated at 24 h and 96 h and that "no PFAS sorbed" was observed. It does not describe how sorption was measured, how many replicates or samples were included, or what detection limits applied to this assessment. Therefore, while the existence and qualitative outcome of this QA/QC-like evaluation are clear, its experimental design and sensitivity are not detailed here.

6. Absence of other QA/QC elements in the excerpt:
Beyond the practices explicitly mentioned—methanol QC injections, internal mass calibration, reporting of LOQ and recoveries, use of procedural blanks, and an HDPE sorption check—the excerpt does not describe other common QA/QC components such as the use of surrogate or internal standards for quantification, calibration curve characteristics, replicate sample analyses, or routine instrument performance checks. From the provided text alone, these elements are either not implemented or not reported; in any case, their procedures and criteria cannot be characterized without additional information.

### Unresolved or unsupported boundaries

- Whether surrogate or internal standards were used for PFAS quantification, and if so, how.
- Details of calibration curves (number of points, concentration range, regression characteristics) for PFAS quantification.
- The presence or absence of replicate analyses for samples, standards, or blanks.
- Any numerical acceptance criteria for instrument performance, calibration quality, recoveries, or blanks beyond what is referenced to external tables or literature.
- Frequencies or numbers of methanol QC injections and procedural blanks beyond being carried out before and after standard injections or being used generally.
- Specific procedures used to derive limits of quantification and recoveries, which are only referenced to supplementary tables and Ref. [14] and not described here.

### Complete approved source chunks

#### NQ02_MMG001

- Role: `required_gold`
- Document: `2024 - Sadia - Sorption of per- and poly-fluoroalkyl substances and their precursors on activated carbon under realistic drinking water conditions - Insights into.pdf`
- Chunk: `10`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=2cb0561aad2e14eaf98b9c73898b1d3b717d18124326289da48533823a409932].

```text
[SOURCE_TEXT_OMITTED sha256=593d6a828a99bfe5e71891c828e90acb4afb2994eb769b87156d50ecc891ecb9]
```

---

## NQ04

**Question:** How are detection and quantification limits reported for PFAS analytical methods, and why are these limits hard to compare across methods or matrices?

### Task components

- `NQ04-T01`: Describe how detection limits and quantification limits (LOD/LOQ) are reported for PFAS analytical methods, including explicit citation of the reported numerical values (with units) and the criteria or calculation approaches used to derive them (e.g., signal-to-noise, standard deviation of blanks, regulatory definitions), while making clear that these limits depend on the specific analytical method, sample matrix, and target analyte and cannot be used to rank methods solely by a single sensitivity number.
- `NQ04-T02`: Explain why LOD/LOQ values for PFAS are difficult to compare across different analytical methods or sample matrices, explicitly tying the explanation to differences in method, matrix, and analyte, as well as to differences in how LOD/LOQ are calculated and reported (including units and criteria), and avoiding any unqualified claims that the method with the lowest reported LOD/LOQ is universally best or that values are directly comparable across matrices or units.

### Normative claim groups

#### NQ04-G01

- Component: `NQ04-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: PFAS LOD/LOQ (or MDL) are reported using several different calculation criteria, including signal-to-noise thresholds, blank-based statistics, IUPAC recommendations, and EPA standard MDL procedures, yielding method- and analyte-specific values rather than a single universal sensitivity number.
- Full: Award full credit if the answer describes at least three distinct LOD/LOQ (or MDL) reporting approaches used for PFAS methods (e.g., signal-to-noise thresholds with specific S/N definitions for LOD and LOQ, statistical calculations based on blanks with explicit multipliers, IUPAC recommendation use with confidence level, EPA standard MDL procedures) and makes clear that the resulting limits are specific to the particular method and analytes, not a universal sensitivity figure.
- Partial: Award partial credit if the answer correctly describes one or two LOD/LOQ (or MDL) calculation approaches or mentions that PFAS limits are reported based on criteria like signal-to-noise or blank statistics but omits the diversity of criteria or does not clearly state that the limits are method- and analyte-specific.
- Contradiction: Mark as contradiction if the answer claims that PFAS LOD/LOQ are always calculated in a single standardized way (e.g., only by signal-to-noise) or if it attributes a specific calculation criterion (e.g., S/N thresholds, blank multipliers, confidence level, EPA MDL procedure) that is not supported by the cited evidence.
- Linked exact evidence:
  - `NQ04_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=98dd53327207a52724c6088058c16f7446c0bb01be5e5a595c2e652e2f0cf96b].
    Supports: Shows that in one PFAS LC/q‑TOF method, LOD and LOQ are reported based on signal-to-noise of deprotonated ions, illustrating an S/N-based definition of limits.
  - `NQ04_MMG001`
    > LOD and LOQ were defined as S/N equal to 3 and 10, respectively.
    Supports: Provides explicit S/N thresholds used to define LOD and LOQ in this PFAS method.
  - `NQ04_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=cfacd92d66dad52ca0f326efc92696b673e78615f2adb68edea7b761b4dbc2ae].
    Supports: Shows a PFAS method where LOD/LOQ are reported using a blank-based statistical approach (mean of Milli‑Q samples plus three or ten times the standard deviation).
  - `NQ04_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=9e913b7b091163c1651d7975a5f1d29d3d0077d4c0e8f56cd3669ced7e5ce37f]].
    Supports: Shows that another PFAS method estimates LOD and LOQ according to IUPAC recommendations at a 95% confidence level, indicating a standardized but distinct calculation approach.
  - `NQ04_MMG004`
    > Method detection limits (MDL) for all PFAS were calculated according to EPA standard methods ( U.S.
    Supports: Shows that PFAS method detection limits (MDL) can be reported based on EPA standard methods, adding another formalized procedure distinct from signal-to-noise or simple blank-based calculations.

#### NQ04-G02

- Component: `NQ04-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: PFAS LOD/LOQ (and MDL) values are difficult to compare across methods and matrices because they depend on the specific calculation approach, target analyte characteristics, and sample matrix effects, so reported limits from one study cannot be directly used to rank overall method sensitivity.
- Full: Award full credit if the answer explicitly explains that PFAS LOD/LOQ (and MDL) values are hard to compare across methods or matrices because (i) different studies use different calculation criteria or formal definitions (e.g., S/N-defined limits, mean blank plus 3/10 SD, IUPAC recommendations at a stated confidence level, EPA standard MDL procedures), and (ii) matrix effects such as signal suppression or enhancement in complex matrices influence detection, all while avoiding any unqualified claim that the method with the lowest reported limit is universally best or that values are directly comparable across matrices.
- Partial: Award partial credit if the answer mentions at least two of the following elements—differing calculation criteria or definitions, matrix effects, or analyte- and matrix-specific variability—but does not clearly connect them to the difficulty of comparing LOD/LOQ across methods and matrices.
- Contradiction: Mark as contradiction if the answer asserts that PFAS LOD/LOQ values from different methods or matrices are directly comparable without caveats, implies that the method with the lowest LOD/LOQ reported in one study is universally the most sensitive, or denies the role of matrix or method-definition differences despite the provided evidence.
- Linked exact evidence:
  - `NQ04_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=cfacd92d66dad52ca0f326efc92696b673e78615f2adb68edea7b761b4dbc2ae].
    Supports: Illustrates a specific blank-based LOD/LOQ calculation approach that differs from signal-to-noise or IUPAC methods, contributing to non-uniform definitions across studies.
  - `NQ04_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=98dd53327207a52724c6088058c16f7446c0bb01be5e5a595c2e652e2f0cf96b].
    Supports: Provides an example of LOD/LOQ definitions based on signal-to-noise thresholds, contrasting with other calculation approaches and underscoring definitional differences.
  - `NQ04_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=9e913b7b091163c1651d7975a5f1d29d3d0077d4c0e8f56cd3669ced7e5ce37f]].
    Supports: Indicates that some PFAS methods use IUPAC-based statistical criteria at a specified confidence level, distinct from simple S/N or blank-based thresholds.
  - `NQ04_MMG004`
    > Method detection limits (MDL) for all PFAS were calculated according to EPA standard methods ( U.S.
    Supports: Shows that some PFAS studies report MDL following EPA standard methods, which again differs from LOD/LOQ definitions used in other studies.
  - `NQ04_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=d4793bfd987f874aead1130f93e21bb0050dd3b6f3e69451042a873bb276103d].
    Supports: Explicitly states that matrix effects such as signal suppression or enhancement in complex matrices like wastewater affect detection of PFCAs, illustrating matrix dependence that complicates comparison of LOD/LOQ across matrices.

#### NQ04-X01

- Component: `NQ04-T02`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: Reported PFAS LOD/LOQ or MDL values and their definitions in these studies are specific to the methods, analytes, and matrices examined and should not be generalized as universally applicable or directly comparable rankings of method sensitivity.
- Full: Use this group to penalize answers that generalize the reported LOD/LOQ or MDL definitions and values as universally comparable or that claim a method with the lowest number is inherently best, despite evidence of method-specific calculation procedures and matrix effects.
- Partial: If an answer mostly respects context-dependence but slips into mild overgeneralization without explicit universal claims (e.g., implying broad comparability), treat this as a minor boundary issue rather than full contradiction.
- Contradiction: Mark as violating this constraint if the answer states or implies that LOD/LOQ or MDL values reported in these specific studies can be directly compared across all PFAS methods or matrices, or that the smallest reported value indicates the universally most sensitive method, ignoring method-definition and matrix dependence.
- Linked exact evidence:
  - `NQ04_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=cfacd92d66dad52ca0f326efc92696b673e78615f2adb68edea7b761b4dbc2ae].
    Supports: Demonstrates that limits are defined by a specific blank-based calculation procedure in this study, implying that a limit defined this way is not directly equivalent to limits defined by other criteria.
  - `NQ04_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=d4793bfd987f874aead1130f93e21bb0050dd3b6f3e69451042a873bb276103d].
    Supports: Shows that detection performance is matrix dependent and affected by matrix effects, indicating that LOD/LOQ determined in one matrix may not translate directly to another.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

Across PFAS analytical methods, detection and quantification limits are reported using several distinct calculation approaches, and the resulting limits are specific to the method, analyte, and matrix.

One LC/q‑TOF method for PFAS in an EPA‑533 PAR standard mix defined its limits based on instrument signal-to-noise. The authors state that “[SOURCE_TEXT_OMITTED sha256=bce725bbbce0662c50355f6e929ccb203d144039b3cf01e38231566b50e1bd18].” [NQ04_MMG001] This is a typical S/N-based reporting approach in which chosen S/N thresholds (3 for LOD, 10 for LOQ) are part of the method definition.

A different study measuring perfluoroalkyl acids in water used a blank-based statistical approach. It reports that “The limit of detection (LOD) and the limit of quantiﬁcation ([SOURCE_TEXT_OMITTED sha256=45b06a40639d523e4cc49ec73c436535a135a01c31c6a9cfb5e1f93be546c63f].” [NQ04_MMG002] In this method, the calculation procedure itself—using the mean of blank Milli‑Q samples plus three or ten times the standard deviation—is explicitly reported and defines how the LOD and LOQ are obtained for the analytes in that matrix.

Other PFAS methods formalize LOD/LOQ according to established guidelines. In an irrigation water application, “[SOURCE_TEXT_OMITTED sha256=237e372beb71c3dc08039cdac057b4128e368ba58d0c8836f85060a0bfffba76].” [NQ04_MMG003] Here the study specifies that IUPAC procedures at a 95% confidence level were used, which is a different criterion from a simple S/N threshold or a mean-plus-multiple‑SD rule.

In a groundwater treatment study, the authors report method detection limits according to U.S. regulatory guidance: “Method detection limits (MDL) for all PFAS were calculated according to EPA standard methods ( U.S.” [NQ04_MMG004] This introduces another related but distinct metric—MDL—determined via EPA standard procedures, again reinforcing that limit definitions vary by study.

These examples together show that PFAS LOD/LOQ (and MDL) are reported using different criteria: signal-to-noise thresholds with explicit S/N definitions for LOD and LOQ [NQ04_MMG001], blank-based statistics using the mean of multiple blank samples plus fixed multiples of the standard deviation [NQ04_MMG002], IUPAC-recommended calculations at a specified confidence level [NQ04_MMG003], and U.S. EPA standard MDL methods [NQ04_MMG004]. They also demonstrate that the resulting numerical values are specific to particular analytes, methods, and matrices and do not constitute a single universal sensitivity number.

Because of this diversity, PFAS LOD/LOQ values are difficult to compare across methods or matrices. First, the underlying definitions differ: one study defines LOD and LOQ as S/N = 3 and 10 [NQ04_MMG001], whereas another bases them on the mean of blank Milli‑Q samples plus three or ten times the standard deviation [NQ04_MMG002]; a third follows IUPAC recommendations at 95 % confidence [NQ04_MMG003]; and another reports MDLs obtained via EPA standard methods [NQ04_MMG004]. These criteria are not strictly interchangeable, so a numerical limit from one study does not necessarily correspond to the same detection probability or confidence level as a limit from another.

Second, matrix effects influence detection. Habib et al. emphasize that “[SOURCE_TEXT_OMITTED sha256=d4793bfd987f874aead1130f93e21bb0050dd3b6f3e69451042a873bb276103d].” [NQ04_MMG005] This indicates that a method’s effective detection capability can differ between relatively clean waters (e.g., Milli‑Q or lightly contaminated water) and complex matrices like wastewater, even if nominal LOD/LOQ values are calculated in a similar way.

Taken together, these studies show that reported LOD, LOQ, and MDL values for PFAS are conditioned by the specific analytical method (instrumentation and calculation criteria), the analytes under consideration, and the sample matrix (e.g., Milli‑Q water, irrigation water, groundwater, or wastewater with matrix effects). Therefore, even when individual studies report very low limits defined by a particular procedure, these numbers cannot be used in isolation to rank methods universally by sensitivity or to directly compare performance across different matrices or PFAS analyte sets without careful consideration of these contextual differences.

### Unresolved or unsupported boundaries

- The evidence set does not provide explicit regulatory or legal definitions of LOD/LOQ beyond referencing IUPAC recommendations and EPA MDL methods.
- No single study in the provided evidence explicitly compares LOD/LOQ values between different PFAS analytical methods or across different matrices in a quantitative way; cross-comparison reasoning is based on juxtaposing separate studies rather than direct comparison experiments.
- The approved exact/unit evidence spans do not report specific LOD/LOQ or MDL numeric values with units, so any detailed discussion of numeric magnitudes or ranges (e.g., LOQ ranges for different PFAAs) would require information beyond the supported spans.
- The evidence does not supply numeric MDL values from the EPA-based method, only stating that MDL was calculated according to EPA standard methods and tabulated elsewhere.

### Complete approved source chunks

#### NQ04_MMG001

- Role: `required_gold`
- Document: `2025 - Tomei - Optimization and Testing of an SPE-LC - q-TOF Analytical Method for the Detection of PFAS Degradation Products in Water Treatment Processes.pdf`
- Chunk: `15`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=98dd53327207a52724c6088058c16f7446c0bb01be5e5a595c2e652e2f0cf96b].

```text
[SOURCE_TEXT_OMITTED sha256=1a35e6c4d45e91e3d112c02dc22207e098c3b406910e91100cfd581c342f95ef]
```

#### NQ04_MMG002

- Role: `required_gold`
- Document: `2019 - Meng - Role of the air-water interface in removing perfluoroalkyl acids from drinking water by activated carbon treatment.pdf`
- Chunk: `12`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=cfacd92d66dad52ca0f326efc92696b673e78615f2adb68edea7b761b4dbc2ae].

```text
[SOURCE_TEXT_OMITTED sha256=c2723de89ffae9c380e6868db65de81e4735de2f5415fe155fec615b6f9373dc].
```

#### NQ04_MMG003

- Role: `required_gold`
- Document: `2022 - Pellicer-Castell - Iron-Doped Bimodal Mesoporous Silica Nanomaterials as Sorbents for Solid-Phase Extraction of Perfluoroalkyl Substances in Environmental.pdf`
- Chunk: `17`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=9e913b7b091163c1651d7975a5f1d29d3d0077d4c0e8f56cd3669ced7e5ce37f]].

```text
[SOURCE_TEXT_OMITTED sha256=d5f6d3ccfbdb164d6243d6707cafe7d35f68fe90224f899c1d8ae96a2d1f8ca0]-
```

#### NQ04_MMG004

- Role: `required_gold`
- Document: `2022 - Croll - Adaptation of selected models for describing competitive per- and polyfluoroalkyl substances breakthrough curves in groundwater treated by granular.pdf`
- Chunk: `13`
- Registered exact span: Method detection limits (MDL) for all PFAS were calculated according to EPA standard methods ( U.S.

```text
[SOURCE_TEXT_OMITTED sha256=07a52780f98e2c3f954e6d8a764df9d58b084e666f36087db45e60b0fe03d4ba]
```

#### NQ04_MMG005

- Role: `optional_gold`
- Document: `2024 - Habib - Green Analytical Method for Perfluorocarboxylic Acids (PFCAs) in Water of Stir Bar Sorptive Extraction Coupled with Thermal Desorption-Gas.pdf`
- Chunk: `57`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=d4793bfd987f874aead1130f93e21bb0050dd3b6f3e69451042a873bb276103d].

```text
[SOURCE_TEXT_OMITTED sha256=fc58a90abdbd4671ae8fd46ce1cd5727e8f2fc8b22f602c3c5ee4faa9356b2da].
```

---

## NQ08

**Question:** What types of blanks are used in PFAS analytical workflows, and how consistently is blank frequency reported across studies?

### Task components

- `NQ08-T01`: Identify and describe the types of blanks used in PFAS analytical workflows, explicitly distinguishing (when present) procedural blanks, method blanks, field blanks, solvent blanks, and instrument blanks, and explain how each blank type is used for contamination assessment.
- `NQ08-T02`: Summarize how frequently blanks are included and reported across PFAS analytical studies (for each blank type when possible), and assess how consistent or variable blank frequency reporting is, without claiming a single universal number of procedural blanks for all PFAS analytical batches.

### Normative claim groups

#### NQ08-G01

- Component: `NQ08-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In a full-scale municipal WWTP PFAS study, field blanks, transport blanks, and procedural blanks were included in each batch of samples to monitor potential contamination during sampling and analysis, and solvent blanks were analyzed to assess instrumental cleanliness.
- Full: Award full credit if the answer states that in at least one PFAS study, [SOURCE_TEXT_OMITTED sha256=c8f10c204d338f107af275d4170e247dec9168d0f098467c1f73b0ffef8beaad], and that solvent blanks were analyzed to ensure instrumental cleanliness, clearly linking each blank type to its role in contamination or cleanliness assessment.
- Partial: Award partial credit if the answer correctly mentions some but not all of the blank types (e.g., only field and procedural blanks) or does not clearly link each blank type to contamination or cleanliness assessment, while still correctly associating at least one blank type with its function as described in the evidence.
- Contradiction: Mark as contradictory if the answer claims that these blanks were not used for contamination monitoring or instrumental cleanliness in this workflow, or if it misrepresents their purpose (e.g., stating that field or transport blanks were used only for calibration rather than contamination assessment).
- Linked exact evidence:
  - `NQ08_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=580ea72d45f18c203f73f0bdc4415119906b45a68d81629d0c98d9ea1bb902ca].
    Supports: Shows that field blanks, transport blanks, and procedural blanks were used and links them to monitoring potential contamination during sampling and analysis, with a frequency of preparation for each batch.
  - `NQ08_MMG001`
    > Solvent blanks (methanol and acetonitrile) were also analyzed to ensure instrumental cleanliness.
    Supports: Shows that solvent blanks were included and that their role was to ensure instrumental cleanliness.

#### NQ08-G02

- Component: `NQ08-T01`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: In a PFAS sorption study, double blanks (without surrogate or standards) and blanks (with surrogate but without standards) were incorporated into the analytical sequence to ensure minimal contamination and adequate mass spectrometer performance, and blank signals were used as a background benchmark for accepting analytical signals.
- Full: Award full credit for this group if the answer explains that in a PFAS sorption study, double blanks (without surrogate or standards) and blanks (with surrogate but without standards) were included in the analytical sequence to ensure minimal contamination and adequate MS performance, and that analytical signals had to exceed blank or double blank background by a specified factor to be accepted.
- Partial: Award partial credit if the answer notes inclusion of double blanks and blanks for contamination or MS performance checks but omits details about their compositions (presence/absence of surrogate and standards) or the use of blank signals as a background threshold.
- Contradiction: Mark as contradictory if the answer claims that double blanks and blanks were not used for contamination or MS performance assessment, or that sample signals were accepted without reference to background signals from blanks or double blanks in this study.
- Linked exact evidence:
  - `NQ08_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=5286d91cd872a49b58c48eeb3e972ead5cad9d3fe5976d03d87528644d2bd234].
    Supports: Shows that double blanks and blanks of defined composition were included in the analytical sequence and that their purpose was to ensure minimal contamination and adequate MS performance.
  - `NQ08_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=df750dceb477ab5f80f7a8934f50b38c79ffdb624e868222bc2cb253354456e5].
    Supports: Shows that background signals from blanks and double blanks were used as a benchmark for deciding which analytical signals were acceptable, linking blank use directly to contamination/background assessment.

#### NQ08-G03

- Component: `NQ08-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In the WWTP PFAS study, field, transport, and procedural blanks were prepared for each batch of samples, indicating a batch-level inclusion frequency for these blanks, and solvent blanks were analyzed as part of the method.
- Full: Award full credit if the answer notes that in at least one PFAS WWTP study, field, transport, and procedural blanks are prepared for each batch of samples (indicating batch-level frequency) and that solvent blanks are also analyzed, recognizing this as reported blank inclusion frequency for that specific study.
- Partial: Award partial credit if the answer mentions that blanks are used in batches in this study but does not clearly tie the per-batch frequency to the specific types (field, transport, procedural) or omits the inclusion of solvent blanks.
- Contradiction: Mark as contradictory if the answer claims that this study did not specify blank inclusion frequency, or that blanks were not prepared per batch despite the evidence stating otherwise.
- Linked exact evidence:
  - `NQ08_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=580ea72d45f18c203f73f0bdc4415119906b45a68d81629d0c98d9ea1bb902ca].
    Supports: Indicates that in this PFAS study, these three blank types were prepared for each batch of samples, directly providing batch-level frequency information.

#### NQ08-G04

- Component: `NQ08-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In the PFAS sorption study, double blanks and blanks were included in the analytical sequence every 8–10 samples, and only signals exceeding 10 times the background in these blanks were accepted, providing a specific reported frequency and use pattern for blanks in that study.
- Full: Award full credit if the answer states that in a PFAS sorption study, double blanks and blanks were included every 8–10 samples in the analytical sequence and that only signals greater than 10 times the background observed in those blanks were accepted, showing both frequency and functional use.
- Partial: Award partial credit if the answer notes either the every-8–10-samples inclusion of blanks or the 10× background acceptance criterion, but not both, while still recognizing that blanks were used repeatedly within the sequence.
- Contradiction: Mark as contradictory if the answer asserts that blanks in this study were not included at a defined interval or that accepted signals were not compared to background signals from blanks or double blanks.
- Linked exact evidence:
  - `NQ08_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=5286d91cd872a49b58c48eeb3e972ead5cad9d3fe5976d03d87528644d2bd234].
    Supports: Provides the reported frequency of double blanks and blanks (every 8–10 samples) and links their inclusion to contamination control and MS performance in this study.
  - `NQ08_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=df750dceb477ab5f80f7a8934f50b38c79ffdb624e868222bc2cb253354456e5].
    Supports: Shows that signals were evaluated relative to background from blanks and double blanks, which were used to set a 10×-background threshold for accepting data.

#### NQ08-X01

- Component: `NQ08-T02`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: The available evidence only reports blank types and frequencies for individual PFAS studies and does not support claiming a single universal blank frequency, such as a universal number of procedural blanks per batch, across all PFAS analytical workflows.
- Full: Answers must not claim a single universal number or frequency of procedural blanks (or any blank type) for all PFAS analytical batches; they should instead treat the described frequencies as study-specific. Use the evidence that one study uses per-batch blanks and another uses every-8–10-samples blanks to illustrate that practices differ.
- Partial: If an answer correctly avoids asserting a universal procedural blank frequency but fails to note that the evidence is limited to a few specific studies, it still satisfies this constraint; this group is not scored for content but for preventing overgeneralization.
- Contradiction: If an answer states or implies that there is a single universal or standard number/frequency of procedural blanks (or other blank types) per PFAS analytical batch, or generalizes the specific reported frequencies as universally representative, it violates this constraint.
- Linked exact evidence:
  - `NQ08_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=580ea72d45f18c203f73f0bdc4415119906b45a68d81629d0c98d9ea1bb902ca].
    Supports: Shows that this specific study uses a per-batch approach to blank preparation, illustrating one study-specific practice rather than a universal rule.
  - `NQ08_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=5286d91cd872a49b58c48eeb3e972ead5cad9d3fe5976d03d87528644d2bd234].
    Supports: Shows that another study uses an every-8–10-samples approach to blank inclusion, differing from the per-batch approach and underscoring that frequencies vary between studies.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

Across the available PFAS analytical workflows, several distinct blank types and their roles in contamination assessment are described, but the information is limited to a small number of studies and does not support generalizing a single standard frequency of blank use.

For blank types and uses (T01):

• In a full-scale AO-MBR-RO municipal WWTP PFAS study, multiple blanks were implemented to monitor contamination associated with both sampling and analysis. Specifically, “[SOURCE_TEXT_OMITTED sha256=580ea72d45f18c203f73f0bdc4415119906b45a68d81629d0c98d9ea1bb902ca].” This links field blanks and transport blanks to assessing contamination introduced during sample collection and transport, and procedural blanks to contamination that could arise from the overall sample preparation procedure. In the same workflow, solvent blanks were used to address the analytical system itself: “Solvent blanks (methanol and acetonitrile) were also analyzed to ensure instrumental cleanliness.” Here, the solvent blanks serve to detect or rule out PFAS-related background originating from the solvents and instrument pathway, thereby assessing instrumental cleanliness.

• In a PFAS sorption study relevant to AFFF-impacted groundwater, the analytical sequence incorporated additional blank types that function as sequence-level quality controls for contamination and instrument behavior. The authors report: “[SOURCE_TEXT_OMITTED sha256=5286d91cd872a49b58c48eeb3e972ead5cad9d3fe5976d03d87528644d2bd234].” Double blanks (no surrogate, no standards) and blanks (with surrogate, no standards) therefore act as checks for contamination and mass spectrometer performance within the sequence. Their background signals directly inform data acceptance: “[SOURCE_TEXT_OMITTED sha256=df750dceb477ab5f80f7a8934f50b38c79ffdb624e868222bc2cb253354456e5].” This shows that these blanks are explicitly used to quantify background and to set a threshold for acceptable signal, linking them tightly to contamination and background assessment.

These excerpts collectively document use of field blanks, transport blanks, procedural blanks, solvent blanks, and analytical-sequence blanks (double blanks and blanks with surrogates) in PFAS workflows. They demonstrate how each is applied to assess different contamination pathways: sampling and transport, laboratory handling, solvent/instrument background, and ongoing sequence background and mass spectrometer performance.

For blank frequency and reporting consistency (T02):

• In the WWTP PFAS study, the reported frequency is at the batch level: “[SOURCE_TEXT_OMITTED sha256=580ea72d45f18c203f73f0bdc4415119906b45a68d81629d0c98d9ea1bb902ca].” This indicates that every analytical batch included these blanks, but the excerpt does not state a universal number of blanks per batch beyond this per-batch preparation statement. Solvent blanks were also analyzed, although their exact numerical frequency is not detailed beyond their inclusion for instrumental cleanliness.

• In the PFAS sorption study, blank inclusion is reported on an analytical-sequence basis: “[SOURCE_TEXT_OMITTED sha256=5286d91cd872a49b58c48eeb3e972ead5cad9d3fe5976d03d87528644d2bd234].” This specifies that double blanks and blanks recur every 8–10 samples. Furthermore, these blanks are operationally integrated into data quality criteria, as “[SOURCE_TEXT_OMITTED sha256=df750dceb477ab5f80f7a8934f50b38c79ffdb624e868222bc2cb253354456e5].”

Comparing these two studies shows that blank frequency and implementation are described in study-specific terms: one workflow uses per-batch field, transport, and procedural blanks plus solvent blanks, while another uses double blanks and blanks every 8–10 samples in the analytical sequence. The available evidence thus supports that PFAS analysts may employ multiple blank types for contamination assessment and instrument cleanliness, but it does not justify inferring a single, universal frequency (e.g., a standard number of procedural blanks per batch) or a uniform reporting practice across the broader PFAS literature. Any broader assessment of consistency or variability in blank frequency reporting would require additional studies beyond those cited here.

### Unresolved or unsupported boundaries

- Whether PFAS method blanks or instrument blanks are explicitly distinguished and named as such in other studies beyond those cited; the provided evidence does not use the terms 'method blank' or 'instrument blank'.
- Any comprehensive, cross-study summary of how frequently each blank type (field, transport, procedural, solvent, method, instrument, double blanks, etc.) is used across the broader PFAS literature.
- Any claim that there is a single, universally applied number of procedural blanks (or other blank types) per batch in PFAS analytical workflows.
- The overall consistency or variability of blank frequency reporting across all PFAS studies, beyond the two specific examples given.

### Complete approved source chunks

#### NQ08_MMG001

- Role: `required_gold`
- Document: `2025 - Ika - Occurrence, partitioning, and fate of per - and polyfluoroalkyl substances (PFAS) in a full-scale AO-MBR-RO municipal WWTP.pdf`
- Chunk: `14`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=580ea72d45f18c203f73f0bdc4415119906b45a68d81629d0c98d9ea1bb902ca].

```text
[SOURCE_TEXT_OMITTED sha256=3123aed0665e87554cc61fe99df09e13e72c9d1778f3006387a2381f776b5300]
```

#### NQ08_MMG002

- Role: `required_gold`
- Document: `2017 - Xiao - Sorption of Poly- and Perfluoroalkyl Substances (PFASs) Relevant to Aqueous Film-Forming Foam (AFFF)-Impacted Groundwater by Biochars and Activated.pdf`
- Chunk: `10`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=5286d91cd872a49b58c48eeb3e972ead5cad9d3fe5976d03d87528644d2bd234].

```text
[SOURCE_TEXT_OMITTED sha256=9d3e382b75d8aa5544b2ba45b7faca5d9548feffa1addbd7d60b851cd2e4bce5]
```

---

## NQ09

**Question:** Do PFAS analytical studies support replacing specific HPLC or solvent-line components with PEEK to reduce PTFE-related contamination?

### Task components

- `NQ09-T01`: Summarize what PFAS analytical studies report about general PTFE-related contamination risks in HPLC or solvent-line setups, without assuming that any specific components are always the source.
- `NQ09-T02`: Determine whether PFAS analytical studies provide evidence for replacing particular, explicitly named HPLC or solvent-line PTFE components with PEEK to reduce contamination, including how contamination sources were traced or verified (e.g., component-level testing, before/after comparisons), while avoiding claims that a single fixed set of component replacements universally resolves PFAS contamination in all LC systems or introducing components not named in the context.

### Normative claim groups

#### NQ09-G01

- Component: `NQ09-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: PFAS/PFC analytical methods report concern about background contamination from LC instrument parts or lines and therefore use stainless steel or PEEK components to minimize such contamination, without identifying specific components as the universal source.
- Full: Award full credit if the answer notes that PFAS/PFC analytical studies describe background contamination risks associated with LC instrument parts or lines and that they mitigate this by using stainless steel or PEEK components, while not asserting that any specific component is always the contaminant source. The answer should make clear that the concern is general background PFAS/PFC contamination from system hardware and that stainless steel/PEEK are used as cleaner alternatives.
- Partial: Award partial credit if the answer mentions that PFAS analytical methods use PEEK or stainless steel components to reduce contamination, but does not clearly link this to general background contamination risks from instrument parts/lines, or if it overemphasizes a specific source without stating that the evidence only indicates general hardware-related risk.
- Contradiction: Mark as contradictory if the answer claims that PFAS analytical studies do not report any contamination risks from instrument parts or lines, or denies that stainless steel or PEEK components are used as precautions against background contamination.
- Linked exact evidence:
  - `NQ09_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=b7094c83e67cd7a40b17d9b2e56c0b351d52774170e3be6b3bd360937d0a6447].
    Supports: Shows that in a PFAS analytical method, instrument parts were replaced with stainless steel or PEEK explicitly to prevent background contamination, indicating a general contamination risk from instrument hardware.
  - `NQ09_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=d3a6815b953973fb818a8fb294b269cee63591006cb9e3a1e8c543bc12c505e9].
    Supports: Shows that a PFAS-related analytical method took precautions to minimize PFC contamination by using stainless steel or PEEK lines, indicating concern about contamination originating from LC lines.

#### NQ09-G02

- Component: `NQ09-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: PFAS analytical studies report replacing unspecified instrument parts with stainless steel or PEEK, and using PEEK lines, as strategies to reduce background PFAS/PFC contamination, but they do not name specific PTFE components being replaced.
- Full: Award full credit if the answer states that PFAS analytical methods describe replacing general, unspecified instrument parts with stainless steel or PEEK, and using PEEK lines, to reduce background contamination, but also clearly notes that these studies do not explicitly identify which PTFE components were replaced or name particular PTFE parts in the LC or solvent-line system.
- Partial: Award partial credit if the answer mentions the use of PEEK or stainless steel parts/lines to reduce contamination but does not clearly state that the components are only described generically and that PTFE or specific parts are not explicitly named.
- Contradiction: Mark as contradictory if the answer claims that the cited studies provide explicit evidence of particular, named PTFE components (e.g., specific valves, frits, or solvent lines) being replaced with PEEK, when such component-level PTFE identification is not present in the evidence.
- Linked exact evidence:
  - `NQ09_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=b7094c83e67cd7a40b17d9b2e56c0b351d52774170e3be6b3bd360937d0a6447].
    Supports: Shows replacement of instrument parts with stainless steel or PEEK to prevent background contamination, but refers only to generic 'instrument parts' without specifying PTFE or naming exact components.
  - `NQ09_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=d3a6815b953973fb818a8fb294b269cee63591006cb9e3a1e8c543bc12c505e9].
    Supports: Shows that stainless steel or PEEK lines were used to minimize PFC contamination, but the lines are not identified as PTFE and no particular PTFE component is named.

#### NQ09-G03

- Component: `NQ09-T02`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: One PFAS analytical study verified that its contamination control measures, including replacement of instrument parts with stainless steel or PEEK, achieved negligible PFAS contamination by using a suite of blanks to confirm concentrations below the method LOQ.
- Full: Award full credit for this supplementary group if the answer notes that a PFAS analytical study not only replaced instrument parts with stainless steel or PEEK but also used multiple types of blanks and found PFAS concentrations below the LOQ in all blanks, thereby confirming negligible overall contamination after these measures, while acknowledging that this verification is at the system level and does not trace contamination back to individual components.
- Partial: Award partial credit if the answer mentions the use of blanks or verification of low contamination but does not connect it to the context of having replaced instrument parts with stainless steel or PEEK, or omits that contamination was below LOQ in all blanks.
- Contradiction: Mark as contradictory if the answer claims that no verification with blanks was performed, or that high PFAS contamination remained in blanks after replacing instrument parts with stainless steel or PEEK, contrary to the evidence.
- Linked exact evidence:
  - `NQ09_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=b7094c83e67cd7a40b17d9b2e56c0b351d52774170e3be6b3bd360937d0a6447].
    Supports: Provides context that replacement of instrument parts with stainless steel or PEEK was one of the contamination control measures implemented.
  - `NQ09_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=b1d3a0ea4525bb04a411abd6dc608b762f6a7340b8b6eac6641ab585a7d94c26].
    Supports: Shows that multiple types of blanks were used to monitor contamination and that PFAS concentrations were below LOQ in all blanks, confirming negligible contamination after the implemented measures.

#### NQ09-X01

- Component: `NQ09-T02`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: The available evidence does not identify specific PTFE components or demonstrate that replacing a fixed, named set of PTFE parts with PEEK universally resolves PFAS contamination, nor does it conduct component-level tracing of contamination sources.
- Full: To respect this constraint, the answer must refrain from claiming that the studies explicitly targeted named PTFE components for replacement with PEEK, must not suggest that a specific universal set of component replacements solves PFAS contamination in all LC systems, and must not imply that component-level source tracing was performed, since the evidence refers only to generic 'instrument parts' or 'lines' and demonstrates system-level, not component-resolved, verification.
- Partial: Minor overgeneralizations (e.g., implying PTFE involvement without saying it was explicitly identified) may be tolerated, but explicit statements that named PTFE components were replaced or that a universal component set solves contamination would violate the constraint.
- Contradiction: Mark as violating this constraint if the answer asserts that specific PTFE parts (not named in the evidence) were identified and replaced with PEEK, or that the evidence demonstrates a universally applicable fixed list of components whose replacement eliminates PFAS contamination, or that component-level tracing was performed, none of which is supported by the cited text.
- Linked exact evidence:
  - `NQ09_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=b7094c83e67cd7a40b17d9b2e56c0b351d52774170e3be6b3bd360937d0a6447].
    Supports: Shows that only generic 'instrument parts' are mentioned, with no specific PTFE components named, supporting the limitation that component-level identification is not provided.
  - `NQ09_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=d3a6815b953973fb818a8fb294b269cee63591006cb9e3a1e8c543bc12c505e9].
    Supports: Shows that precautions involved 'stainless steel or PEEK lines' and a pre-column, but does not specify PTFE or provide any universal list of components, reinforcing the constraint against overgeneralizing component-level solutions.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

PFAS and related PFC analytical methods do describe background contamination risks associated with LC hardware, but they do so at a general level rather than by pinpointing specific PTFE parts.

One wastewater PFAS study reports that "[SOURCE_TEXT_OMITTED sha256=243c378cea4acf5d577f02461c61ba9127060de0edf22cb46847811c5daac405]" [NQ09_MMG001]. This shows that the authors regarded instrument hardware as a potential source of background PFAS contamination and chose stainless steel or PEEK components as cleaner alternatives, without identifying any particular part as always being responsible. Another PFAS-related LC–MS method notes that "[SOURCE_TEXT_OMITTED sha256=d0a36d9820bb734b9b6766f742c6a1c39c6c0b5bc815c44088ddc42a42d83a88]" [NQ09_MMG002], again indicating concern about contamination from the LC lines themselves and the use of PEEK or stainless steel to mitigate it. Together, these methods support a general view that PFAS/PFC contamination can arise from LC instrument parts or lines and that switching to stainless steel or PEEK components is a common precaution, but they do not single out specific components as universal contamination sources.

Regarding explicit evidence for replacing particular PTFE components with PEEK, the available texts are more limited. The wastewater PFAS study describes replacing generic "instrument parts" with stainless steel or PEEK [NQ09_MMG001], and the advanced oxidation study mentions stainless steel or PEEK "lines" [NQ09_MMG002], but neither document states that the original parts or lines were PTFE, nor do they name specific elements such as particular valves, fittings, or solvent lines. Thus, they support the idea that replacing unspecified LC components with PEEK can be part of a contamination-control strategy, but they do not provide component-level, PTFE-specific replacement evidence.

System-level verification of contamination control is documented in the wastewater study. After implementing measures including replacement of instrument parts with stainless steel or PEEK, the authors prepared "field blanks, transport blanks, and procedural blanks" and also ran "solvent blanks" [NQ09_MMG001]. They report that "across all blank samples, PFAS concentrations were below the method's limit of quantification (LOQ), confirming negligible contamination" [NQ09_MMG001]. This demonstrates tracing and verification at the level of the whole analytical workflow: the combined precautions, including the material changes, produced negligible measurable PFAS contamination in blanks. However, this approach does not isolate which specific component(s) originally contributed contamination, nor does it establish that a single, fixed set of component replacements—much less any particular PTFE-to-PEEK swap—will resolve PFAS contamination in all LC systems.

Overall, the cited PFAS analytical studies support general concern about hardware-derived PFAS/PFC contamination and the use of stainless steel or PEEK parts and lines to reduce it, with system-level blank checks to verify low contamination. They do not, however, provide explicit, PTFE-identified, component-level replacement evidence or a universally applicable component-replacement recipe.

### Unresolved or unsupported boundaries

- Whether any specific HPLC or solvent-line components in these studies were definitively identified as PTFE and then replaced with PEEK.
- Any explicit list of named PTFE components (e.g., particular valves, frits, pump seals, or solvent lines) whose replacement with PEEK was shown to reduce PFAS contamination.
- Component-level tracing or testing (e.g., isolating individual LC parts and measuring their contribution to PFAS background) to verify that a particular component was the contamination source.
- Evidence that a single fixed set of component replacements universally resolves PFAS contamination in all LC systems.

### Complete approved source chunks

#### NQ09_MMG001

- Role: `optional_gold`
- Document: `2025 - Ika - Occurrence, partitioning, and fate of per - and polyfluoroalkyl substances (PFAS) in a full-scale AO-MBR-RO municipal WWTP.pdf`
- Chunk: `14`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=b7094c83e67cd7a40b17d9b2e56c0b351d52774170e3be6b3bd360937d0a6447].

```text
[SOURCE_TEXT_OMITTED sha256=3123aed0665e87554cc61fe99df09e13e72c9d1778f3006387a2381f776b5300]
```

#### NQ09_MMG002

- Role: `optional_gold`
- Document: `2015 - Anumol - Transformation of Polyfluorinated compounds in natural waters by advanced oxidation processes.pdf`
- Chunk: `13`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=d3a6815b953973fb818a8fb294b269cee63591006cb9e3a1e8c543bc12c505e9].

```text
[SOURCE_TEXT_OMITTED sha256=103a5e2257d1595071b615342ed650ee1282cee2bc06c0da85bc1ee56a945937]
```

---

## NQ11

**Question:** How are isotope-labelled internal standards used in PFAS analysis, and when do studies rely on non-exact labelled analogs?

### Task components

- `NQ11-T01`: Describe how isotope-labelled internal standards are used in PFAS analysis, including their function in quantification, correction for losses or matrix effects, and overall role in data quality.
- `NQ11-T02`: Explain how the choice of isotope-labelled standards (exact vs non-exact analogs) is connected to analyte coverage and the scope of the PFAS method (e.g., number and types of targeted PFAS).
- `NQ11-T03`: Identify situations or study designs in which non-exact isotope-labelled analogs are relied upon instead of exact labelled standards, and describe how they are applied in PFAS analysis under those conditions.

### Normative claim groups

#### NQ11-G01

- Component: `NQ11-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In PFAS analyses, isotope-labelled internal standards are added (often at the start of sample preparation) and used in isotope-dilution approaches to enable quantification and correct analytical bias in complex environmental samples, thereby supporting data quality.
- Full: Count this claim group as fully satisfied when the answer explains that isotope-labelled internal standards are used in PFAS analysis by adding them during sample preparation for isotope-dilution-based quantification and that they are used to correct analytical bias or matrix-related issues, thus supporting data quality; this must be explicitly tied to PFAS analytical workflows (e.g., SPE plus LC-MS/MS).
- Partial: Count this claim group as partially satisfied when the answer mentions isotope-labelled internal standards and quantification in PFAS analysis but does not clearly describe their timing of addition or their role in correcting analytical bias/matrix effects and data quality.
- Contradiction: Mark this claim group as contradicted if the answer asserts that isotope-labelled internal standards are not used for quantification or not needed for correcting analytical bias/matrix effects in PFAS analysis, or implies they are added only after all sample preparation steps without any role in isotope-dilution approaches.
- Linked exact evidence:
  - `NQ11_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=f31087c2a2354dfc0d672081f375a5bafba68eb066f062fab89b78f8333111d9].
    Supports: Shows that isotope-labelled internal standards are added at the start of PFAS sample preparation and are specifically used to enable isotope-dilution quantification.
  - `NQ11_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=584c48f2afd975d04e5e70d7929ba42da6ac38d8da3bb78f4d586dc463971cd7].
    Supports: Shows the use of isotope dilution with carbon-13 and/or oxygen-18 labeled analogs to correct analytical bias in chemically complex environmental PFAS samples.

#### NQ11-G02

- Component: `NQ11-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: When exact isotope-labelled analogs are unavailable for some PFAS, methods extend analyte coverage by assigning closely related or class-representative labeled internal standards selected based on functional group and fluorocarbon chain length, aligning standard choice with the scope of targeted and suspect PFAS.
- Full: Count this claim group as fully satisfied when the answer explains that PFAS analytical methods use exact isotope-labelled analogs when available, but to broaden analyte coverage and match the method’s scope they also assign non-exact or class-representative internal standards to other PFAS based on structural similarity, such as ionizable functional group and fluorocarbon chain length.
- Partial: Count this claim group as partially satisfied when the answer notes that non-exact or surrogate isotope-labelled standards are used for some PFAS but does not clearly connect this to method scope, analyte coverage, or the criteria (e.g., functional group, chain length) used to select these standards.
- Contradiction: Mark this claim group as contradicted if the answer claims that PFAS methods only use exact isotope-labelled analogs for every analyte, or denies that non-exact/structurally related internal standards are used to expand analyte coverage.
- Linked exact evidence:
  - `NQ11_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=584c48f2afd975d04e5e70d7929ba42da6ac38d8da3bb78f4d586dc463971cd7].
    Supports: Shows that when exact (identically labeled) analogs are not available for certain PFAS, quantification relies on closely related labeled analogs, linking standard choice to analyte coverage.
  - `NQ11_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=be2ea3003e6fccdd0b108fd9ddfc02cb8aa38a9c09d044f583aa5c5507c9ea5b].
    Supports: Shows that internal standards for suspect PFAS are selected from an existing target list based on ionizable functional group and fluorinated chain length, indicating a class/structure-based approach to extend coverage beyond analytes with exact labeled standards.

#### NQ11-G03

- Component: `NQ11-T03`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In PFAS studies that include suspect screening or PFAS classes lacking exact labeled analogs, non-exact isotope-labelled or class-representative internal standards from a target analyte list are used for semi-quantitative estimation or quantification, with assignments guided by PFAS functional group and chain length or by class (e.g., using quantifiable PFAAs for U-PFAAs and K-PFAAs).
- Full: Count this claim group as fully satisfied when the answer identifies that, in study designs such as suspect screening, semiquantitative analysis, or analysis of PFAS classes lacking exact labeled analogs, researchers rely on non-exact or class-representative isotope-labelled internal standards (or target analyte internal standards) and apply them by matching structural features such as ionizable functional group, fluorocarbon chain length, or PFAS class to estimate concentrations.
- Partial: Count this claim group as partially satisfied when the answer either (a) mentions use of non-exact isotope-labelled standards for suspect or non-target PFAS but does not describe how they are assigned/applied, or (b) describes class-based or chain-length-based internal standard assignment without clearly tying it to the absence of exact labeled analogs or to suspect/semiquantitative study designs.
- Contradiction: Mark this claim group as contradicted if the answer asserts that non-exact or class-representative isotope-labelled standards are not used in PFAS analysis, or claims that suspect and class-level PFAS analyses only rely on exact labeled analogs for every compound.
- Linked exact evidence:
  - `NQ11_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=be2ea3003e6fccdd0b108fd9ddfc02cb8aa38a9c09d044f583aa5c5507c9ea5b].
    Supports: Shows that in semiquantitative suspect analysis, non-exact internal standards from a target analyte list are used and selected based on functional group and chain length to estimate concentrations of suspect PFAS.
  - `NQ11_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=1ab84e3d45b277dd21f4979beb11b4c95edb13f7da464696f54c4a9882cfd87a]).
    Supports: Demonstrates a situation where quantifiable PFAAs are used as internal standards for unsaturated and keto PFAAs; assignments are based on chain length and are used to calculate suspect PFAS concentrations from target calibration curves, illustrating application of non-exact/class-based internal standards for suspect/class PFAS.

#### NQ11-X01

- Component: `NQ11-T02`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: The available evidence only describes internal standard choices and labeled-standard sets for specific PFAS methods and compound lists; it does not show that any single exact labeled-standard set is universally sufficient for all PFAS analytical methods.
- Full: Use this constraint to ensure the answer does not generalize from study-specific internal-standard strategies to a claim that one exact isotope-labelled standard set is universally sufficient for all PFAS methods; the answer should acknowledge or implicitly reflect that different studies target different PFAS and use different internal-standard selections.
- Partial: If the answer is silent on universality but otherwise neutral, treat this constraint as implicitly respected; only explicit overgeneralization should be flagged.
- Contradiction: This constraint is contradicted if the answer explicitly claims that a particular exact isotope-labelled standard set is sufficient for all PFAS analytical methods or implies universal adequacy without qualification.
- Linked exact evidence:
  - `NQ11_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=584c48f2afd975d04e5e70d7929ba42da6ac38d8da3bb78f4d586dc463971cd7].
    Supports: Shows that the described isotope-dilution and labeled-standard approach is defined for a specific set of 'PFAS compounds of interest', not all conceivable PFAS, indicating method-specific scope.
  - `NQ11_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=be2ea3003e6fccdd0b108fd9ddfc02cb8aa38a9c09d044f583aa5c5507c9ea5b].
    Supports: Indicates that the internal standards are drawn from a defined 'target analyte list', again emphasizing that the described approach pertains to a specific set of PFAS rather than a universal standard set.
  - `NQ11_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=1ab84e3d45b277dd21f4979beb11b4c95edb13f7da464696f54c4a9882cfd87a]).
    Supports: Shows that this internal-standard strategy is tailored to specific PFAS subclasses in this study, supporting the interpretation that internal-standard sets are method- and class-specific rather than universally applicable.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

In the PFAS methods illustrated, isotope‑labelled internal standards are incorporated directly into the sample‑preparation and LC‑MS/MS workflow to support isotope‑dilution quantification and control analytical bias.

For target PFAS analysis, isotope‑labelled internal standards are added early in the workflow so they experience the same extraction and concentration steps as the native analytes. In one protocol, “[SOURCE_TEXT_OMITTED sha256=969f426723a6c192af22ca436df3d611b19ce8ae02bb5ba75d2563911f4bee36]” [NQ11_MMG001]. In another study, LC‑MS/MS analysis of groundwater used “an isotope dilution technique … [SOURCE_TEXT_OMITTED sha256=acedc16f570567178dbdb1b04836e6316b8c9994bd5fd6f4d164b38d22f70656]” [NQ11_MMG002]. These examples show that isotope‑labelled standards are introduced before analysis and used in isotope‑dilution calculations to obtain quantitative results while correcting for matrix‑related analytical bias, thereby improving data quality.

The choice between exact and non‑exact isotope‑labelled standards is linked to which PFAS are targeted and how broad the method’s scope is. Where an identically labelled analog exists, it can be used directly. However, the groundwater study explicitly notes that “Compounds that do not have an identically labeled analog were quantitated using a closely related labeled analog” [NQ11_MMG002]. This indicates that, to maintain coverage when the target list includes PFAS lacking exact labelled standards, the method substitutes structurally similar labeled analogs. In broader AFFF studies that include both target and suspect PFAS, the internal standards for suspect compounds are chosen from an existing target list rather than being exact analogs. For semiquantitative suspect analysis, “[SOURCE_TEXT_OMITTED sha256=f8d7ba27b47308703860b0793d6540e44992e71c902a4755726c1cb232e70b61]” [NQ11_MMG003]. Similarly, another AFFF study assigned “quantifiable PFAAs … to be the internal standards of unsaturated perfluoroalkyl [SOURCE_TEXT_OMITTED sha256=0f2c58a368f74ebd56ec096be47be013c5e3fede1adf9c83764a9f6acfb4799a])” [NQ11_MMG004]. These approaches tie internal‑standard choice to PFAS class and chain length so that a finite set of labeled or quantifiable PFAAs can support measurement of a broader range of PFAS, aligning internal‑standard selection with the method’s analyte coverage.

Non‑exact isotope‑labelled or class‑representative analogs are therefore relied upon in several specific situations. In the ion‑exchange/electrochemical oxidation groundwater study, whenever a PFAS “do[es] not have an identically labeled analog” it “was quantitated using a closely related labeled analog” [NQ11_MMG002], showing that structurally related labeled standards are used to obtain quantitative results for PFAS beyond those with exact labels. In suspect‑screening workflows for AFFF, where many PFAS do not have individual calibrated standards, “semiquantitative analysis of suspect analytes” is performed by estimating concentrations “[SOURCE_TEXT_OMITTED sha256=e4867f596fd4bfe2278ffc2507b4250f6645174f57a04077f83ac388f1ecf66d]” [NQ11_MMG003]. Likewise, in class‑based analysis of novel PFAS such as U‑PFAAs and K‑PFAAs, “quantifiable PFAAs were assigned to be the internal standards” for those classes, with assignments matched by “fluorocarbon chain length,” and [SOURCE_TEXT_OMITTED sha256=5388996f07c084ee03ee38f02f407bed7f6363d0345152007ab6e1238d07ce7b]” [NQ11_MMG004]. These examples illustrate that, when expanding beyond a narrow set of targets or when exact labeled analogs are unavailable, studies rely on non‑exact, structurally or class‑matched internal standards for quantitative or semiquantitative PFAS analysis.

Across these studies, the internal‑standard and labeled‑standard sets are defined for specific PFAS compound lists (e.g., “PFAS compounds of interest” [NQ11_MMG002] or a particular “target analyte list” [NQ11_MMG003]) and specific PFAS classes such as U‑PFAAs and K‑PFAAs [NQ11_MMG004]. The evidence does not indicate that any one exact isotope‑labelled standard set would be sufficient for all PFAS analytical methods; rather, internal‑standard selection is tailored to the targeted PFAS and the scope of each method.

### Unresolved or unsupported boundaries

- Any general, method-independent rules for how many isotope-labelled internal standards are needed for a given number of PFAS analytes are not described in the evidence.
- The evidence does not specify detailed criteria for when a closely related labeled analog is considered sufficiently similar beyond mentioning functional group and fluorocarbon chain length.
- The evidence does not cover isotope-labelled standard strategies for all PFAS classes (e.g., fluorotelomer sulfonates, polymers) or all matrices beyond the specific groundwater and AFFF-related examples.

### Complete approved source chunks

#### NQ11_MMG001

- Role: `required_gold`
- Document: `2025 - El-Sawaf - Sustainable photocatalytic degradation of perfluoroctanoic acid (PFOA) and perfluorooctane sulfonate (PFOS) using chitosan-doped g-C₃N₄ for green.pdf`
- Chunk: `24`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=f31087c2a2354dfc0d672081f375a5bafba68eb066f062fab89b78f8333111d9].

```text
[SOURCE_TEXT_OMITTED sha256=47594a8b5d3656f9cf586970be9ebbb39eabc071553e59f7505b5cd221c55ffc]
```

#### NQ11_MMG002

- Role: `required_gold`
- Document: `2022 - Liang - Field demonstration of coupling ion-exchange resin with electrochemical oxidation for enhanced treatment of per- and polyfluoroalkyl substances.pdf`
- Chunk: `14`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=584c48f2afd975d04e5e70d7929ba42da6ac38d8da3bb78f4d586dc463971cd7].

```text
[SOURCE_TEXT_OMITTED sha256=e345a645fe55756b7716efdabf11df7217c3c6dfb0967add27eef7e0a6de77d0]
```

#### NQ11_MMG003

- Role: `optional_gold`
- Document: `2021 - Hao - Hydrothermal Alkaline Treatment for Destruction of Per- and Polyfluoroalkyl Substances in Aqueous Film-Forming Foam.pdf`
- Chunk: `12`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=be2ea3003e6fccdd0b108fd9ddfc02cb8aa38a9c09d044f583aa5c5507c9ea5b].

```text
[SOURCE_TEXT_OMITTED sha256=d40dce5244b169d8971317ee17dcf3423c0c5094c588faf87e0edde176a3e2d1]
```

#### NQ11_MMG004

- Role: `optional_gold`
- Document: `2021 - Fang - Removal of Per- and Polyfluoroalkyl Substances (PFASs) in Aqueous Film-Forming Foam (AFFF) Using Ion-Exchange and Nonionic Resins.pdf`
- Chunk: `12`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=1ab84e3d45b277dd21f4979beb11b4c95edb13f7da464696f54c4a9882cfd87a]).

```text
[SOURCE_TEXT_OMITTED sha256=20915698a9d9a5b7a9daf7a578306f78cf59323e344dc50335ff384f342271f3]
```

---

## NQ13

**Question:** What recovery performance is reported for extracting PFAS from complex water or wastewater matrices, and how do studies account for recovery in final concentrations?

### Task components

- `NQ13-T01`: Identify the reported recovery performance values for extracting PFAS from complex water and wastewater matrices, explicitly describing how recovery varies by matrix type and by individual analyte.
- `NQ13-T02`: Describe how the studies handle recovery when calculating and reporting final PFAS concentrations, including the logic by which recovery is incorporated or corrected for in a validated manner, and make clear that a single expected recovery percentage is not assumed valid for all PFAS in all complex water matrices.

### Normative claim groups

#### NQ13-G01

- Component: `NQ13-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In PFAS-spiked municipal wastewater effluent, reported recoveries for individual PFAS (PFOA, PFOS, PFBA) were high and near quantitative, with values around 91–100% depending on analyte and condition, indicating limited matrix influence compared to DDI water.
- Full: To receive full credit, an answer must report that in a PFAS-spiked municipal wastewater effluent matrix, recoveries for individual PFAS were high and near 100%, specifically around [SOURCE_TEXT_OMITTED sha256=9f0df0c0941fbaab3c67eea977ad003be9534a2f666c4cae47c3f5dc00a13961], and interpret this as indicating limited matrix influence relative to DDI water.
- Partial: Partial credit is given if the answer notes high or near-quantitative PFAS recoveries in municipal wastewater effluent and mentions at least one correct approximate recovery percentage or range, even if not all analytes or numeric values are provided.
- Contradiction: An answer is contradictory if it states that PFAS recoveries in municipal wastewater effluent were low (e.g., generally below ~50%) or that they were not quantified, or if it claims there was strong matrix interference leading to poor recovery in this matrix.
- Linked exact evidence:
  - `NQ13_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=57e6f44b20925eeb0a47d5c62bf1a555d96556fd0704de5e27b489c53f280eee].
    Supports: Provides specific numeric recoveries for PFOA, PFOS, and PFBA in municipal wastewater effluent and interprets them as indicating limited matrix influence compared to DDI water.

#### NQ13-G02

- Component: `NQ13-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In a stir bar sorptive extraction method for PFCAs, recovery performance varies strongly with wastewater matrix complexity: wastewater influent recoveries are low (about 21–44%), whereas wastewater effluent shows intermediate recoveries (about 43–74%), with recoveries also influenced by spike level and individual analyte.
- Full: To receive full credit, an answer must state that in the cited PFCA method, wastewater influent showed significantly lower recoveries, on the order of roughly 29–44% at 10 ng and about 21–31% at 20 ng, while wastewater effluent had intermediate recoveries of roughly 43–65% at 10 ng and 44–74% at 20 ng, and attribute this to matrix effects and matrix complexity.
- Partial: Partial credit is given if the answer correctly notes that wastewater influent recoveries are substantially lower than effluent recoveries and provides at least one approximate numeric range (e.g., “~20–40% in influent vs ~40–70% in effluent”), even if spike levels or full ranges are not detailed.
- Contradiction: An answer is contradictory if it claims that influent and effluent recoveries were similar in magnitude, that influent recoveries were high (e.g., mostly above 70%), or that matrix complexity did not impact recovery.
- Linked exact evidence:
  - `NQ13_MMG003` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=634bf74fa5a5dd74d8795250fd46b5bd9ba37ed1656dd00cf61af25580295176].
    Supports: Shows that wastewater influent recoveries are low (about 21–44%) and attributes this to substantial matrix effects and interfering substances.
  - `NQ13_MMG003` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=28b5b62dfb16642ff1e522408395099962b64e3eb328016ce65eba8efb4002df].
    Supports: Provides numeric intermediate recovery ranges for wastewater effluent (about 43–74%) and notes that this confirms the impact of matrix complexity on extraction efficiency.

#### NQ13-G03

- Component: `NQ13-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In a field demonstration of PFAS treatment in groundwater, LC-MS/MS quantification used isotope dilution with carbon-13 and/or oxygen-18 labeled analogs, allowing correction of analytical bias from chemically complex environmental samples, with unlabeled PFAS quantified using closely related labeled analogs.
- Full: To receive full credit, an answer must explain that in the referenced groundwater study, PFAS were analyzed by LC-MS/MS using isotope dilution with carbon-13 and/or oxygen-18 labeled analogs specifically to correct analytical bias in chemically complex environmental samples, and that PFAS without identical labeled analogs were quantified using closely related labeled analogs.
- Partial: Partial credit is given if the answer notes the use of isotope dilution with labeled standards to correct matrix-related analytical bias in complex water samples, even if specific isotopes or the handling of compounds without identical analogs are omitted.
- Contradiction: An answer is contradictory if it claims that PFAS were quantified without any correction for matrix effects or analytical bias, or that isotope dilution or labeled analogs were not used in complex environmental samples in this study.
- Linked exact evidence:
  - `NQ13_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=04362696ca20f0cf880ed6e6fdeeadb52813dd89ff3d40536dd81b37c67b822a].
    Supports: Shows that isotope dilution with carbon-13 and/or oxygen-18 labeled analogs was used explicitly to correct analytical bias in chemically complex environmental samples, and describes how PFAS lacking identical labeled analogs were quantified.

#### NQ13-G04

- Component: `NQ13-T02`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: For PFCA analysis in complex wastewater matrices, the standard addition method is identified as a viable approach to compensate for matrix-induced deviations and achieve more accurate quantification when recovery is affected by matrix effects.
- Full: To receive full credit for this supplementary claim, an answer should mention that in the PFCA wastewater study, standard addition was suggested as a method to address matrix effects, by adding known quantities of PFCAs directly to samples to compensate for matrix-induced deviations and thereby obtain more accurate analyte quantification.
- Partial: Partial credit is given if the answer references the use or suggestion of standard addition to handle matrix effects in complex wastewater samples, without fully describing its compensatory function.
- Contradiction: An answer is contradictory if it asserts that no methods such as standard addition are proposed or used to address matrix effects in these PFCA wastewater measurements.
- Linked exact evidence:
  - `NQ13_MMG003` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=4e2dabea6b36a4019d8a2af5f63c6950a458a5af3027ae58bc3b8d88fc151e7a].
    Supports: States that standard addition is a viable solution to matrix effects in complex wastewater samples, explains that adding known quantities directly compensates for matrix-induced deviations, and notes that this allows more accurate quantification.

#### NQ13-X01

- Component: `NQ13-T01`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: Recovery performance for PFAS extraction is not uniform across all complex water and wastewater matrices or all analytes; instead, it varies with matrix complexity and PFAS type, so a single universal expected recovery percentage cannot be assumed.
- Full: The answer must not claim or imply that a single expected recovery percentage is valid for all PFAS in all complex water matrices. It should recognize that recoveries differ between, for example, municipal wastewater effluent with high recoveries for PFOA, PFOS, and PFBA, and wastewater influent with much lower PFCA recoveries and effluent with intermediate recoveries, reflecting matrix- and analyte-specific behavior.
- Partial: Partial satisfaction of this constraint occurs if the answer avoids stating a universal recovery percentage, even if it does not explicitly contrast different matrices, as long as it does not imply uniformity of recovery across all PFAS and matrices.
- Contradiction: This constraint is violated if the answer claims or clearly implies that there is a single typical or expected recovery value (or narrow fixed range) that can be assumed for all PFAS in all complex water or wastewater matrices.
- Linked exact evidence:
  - `NQ13_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=57e6f44b20925eeb0a47d5c62bf1a555d96556fd0704de5e27b489c53f280eee].
    Supports: Shows high recoveries for specific PFAS in municipal wastewater effluent and suggests limited matrix influence in this case, providing a contrast point with other matrices.
  - `NQ13_MMG003` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=170b27dcc3db1e7d80db334c6e1d77ad13e4ff2184c9730877b0896b1456baa6].
    Supports: Demonstrates that in more complex matrices (wastewater influent), recoveries are much lower, and in effluent they are intermediate, showing matrix-dependent variability that contradicts any assumption of a single universal recovery percentage.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

Across the reported studies, PFAS recovery from complex water and wastewater matrices is quantitatively documented and clearly matrix- and analyte-dependent, and final concentration reporting employs validated approaches to correct for recovery and matrix effects.

For municipal wastewater effluent spiked with PFAS, Zheng et al. report high, near-quantitative recoveries for three individual PFAS. In PFAS-spiked municipal wastewater effluent, [SOURCE_TEXT_OMITTED sha256=11927333fe06dae0e7e333bf098479d9b3387c0f2f6d9e642aff3d1a427f3e0d], and this was interpreted as indicating limited influence of the municipal wastewater effluent matrix relative to DDI water (NQ13_MMG001: “[SOURCE_TEXT_OMITTED sha256=a352be09d7e6f8ea55e1001fb51e284dd4edd998a41ce7ba1443d0ed3ce34b18]… This result potentially indicated the limited influence of municipal wastewater effluent matrices compared to DDI water.”). These values show that, in this particular effluent and for these specific PFAS, recoveries are close to 100% but still differ somewhat by analyte.

In contrast, Habib et al. demonstrate that recovery is substantially lower and more affected by matrix in other wastewater matrices for PFCAs using a stir bar sorptive extraction method. For wastewater influent, recovery rates were significantly lower, with values from 29% (±12) to 44% (±11) at the 10 ng spike level and between 21% (±7) and 31% (±10) at the 20 ng level, indicating a substantial matrix effect due to interfering substances (NQ13_MMG003: “[SOURCE_TEXT_OMITTED sha256=e45109bf01907429f790e180649f9368e5a5b49cd176d00ab2daff58c9160e46] … between 21% (±7) and 31% (±10). This indicates a substantial matrix effect”). For wastewater effluent in the same study, recoveries were intermediate: 10 ng spikes yielded 43% (±6) to 65% (±14), and 20 ng spikes gave 44% (±11) to 74% (±8) (NQ13_MMG003: “[SOURCE_TEXT_OMITTED sha256=0857e7f6dac43030b31c58444be13f68a7410bf1b91be8a0eb511b7f43dbb048] results confirm that the extraction efficiency of PFCAs is strongly impacted by matrix complexity and that recovery varies both with matrix type (influent vs effluent) and analyte/spike level.

Taken together, these studies illustrate that PFAS and PFCA recovery cannot be represented by a single universal value across complex water matrices: some municipal wastewater effluents support recoveries near 100% for particular PFAS, whereas more complex matrices such as wastewater influent yield recoveries as low as roughly 20–40%, with effluents giving intermediate values. Recovery performance is therefore both matrix- and analyte-dependent.

Regarding how recovery and matrix effects are handled in final PFAS concentration calculations, different validated analytical strategies are employed. In a field demonstration of PFAS treatment in groundwater, Liang et al. corrected for analytical bias and matrix effects using isotope dilution. Water samples were extracted using SPE and analyzed by LC-MS/MS, and “[SOURCE_TEXT_OMITTED sha256=87f659fda4f3d691142b61dba6642d61157e82a45579dd80f63cef17d9e3c15b],” while “compounds that do not have an identically labeled analog were quantitated using a closely related labeled analog” (NQ13_MMG002). In this approach, the labeled internal standards co-extracted and co-eluted with each target PFAS provide compound-specific or closely related surrogates that account for recovery and matrix suppression or enhancement, so that the reported PFAS concentrations are corrected for analytical bias in the complex groundwater matrix.

In the PFCA wastewater work, Habib et al. explicitly link the observed low recovery and strong matrix effects in influent and intermediate recoveries in effluent to the need for matrix-aware quantification strategies. To address matrix effects in more complex wastewater samples, they propose using standard addition: “[SOURCE_TEXT_OMITTED sha256=a9bf77b3a00bb52c3954b80b3dd2c3dd54cfda63adcfe96b9bc2d385d82fe0b3]” (NQ13_MMG003). Here, calibration is performed in the sample itself, so the measured response inherently incorporates the matrix-induced recovery and signal modification, yielding final concentrations that are effectively corrected for those matrix-specific biases.

Across these examples, recovery is explicitly measured and reported for specific PFAS and PFCAs in defined complex matrices, and variability by matrix and analyte is clearly documented. Final concentration reporting makes use of validated correction logic—either via isotope dilution with appropriately chosen labeled analogs or via standard addition—to compensate for recovery losses and matrix-induced analytical bias. The data do not support assuming any single expected recovery percentage as valid for all PFAS across all complex water or wastewater matrices; instead, recovery and correction strategies are tailored to the particular matrix and target analytes.

### Unresolved or unsupported boundaries

- Recovery performance values for PFAS in complex water matrices other than the specific municipal wastewater effluent, wastewater influent, wastewater effluent, and groundwater systems described (e.g., industrial wastewaters, surface waters with complex organic loads, landfill leachate) are not provided in the available evidence.
- Detailed, compound-by-compound recovery data for PFAS beyond PFOA, PFOS, PFBA, and the unspecified set of PFCAs in the Habib et al. study are not reported in the evidence.
- Explicit numerical descriptions of how isotope dilution or standard addition quantitatively adjust raw concentrations (e.g., specific correction factors or equations) are not provided in the evidence; only the qualitative correction logic is described.

### Complete approved source chunks

#### NQ13_MMG001

- Role: `required_gold`
- Document: `2024 - Zheng - Using syringe filtration after lab-scale adsorption processes potentially overestimates.pdf`
- Chunk: `33`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=2720e77b873accc49d24a57f540808119d40cf3ea5f100402637c9ae8e0aeb24]).

```text
[SOURCE_TEXT_OMITTED sha256=3a4c92ad5f1d675a9222d635104dc3ac85a8da1f60a73cd2d293c70a59b77fe5]
```

#### NQ13_MMG002

- Role: `required_gold`
- Document: `2022 - Liang - Field demonstration of coupling ion-exchange resin with electrochemical oxidation for enhanced treatment of per- and polyfluoroalkyl substances.pdf`
- Chunk: `14`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=584c48f2afd975d04e5e70d7929ba42da6ac38d8da3bb78f4d586dc463971cd7].

```text
[SOURCE_TEXT_OMITTED sha256=e345a645fe55756b7716efdabf11df7217c3c6dfb0967add27eef7e0a6de77d0]
```

#### NQ13_MMG003

- Role: `optional_gold`
- Document: `2024 - Habib - Green Analytical Method for Perfluorocarboxylic Acids (PFCAs) in Water of Stir Bar Sorptive Extraction Coupled with Thermal Desorption-Gas.pdf`
- Chunk: `54`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=6f2c41506c5d08d1c3b305441ce64493aa24606f63557abc4f02617a165874df]).

```text
[SOURCE_TEXT_OMITTED sha256=9e5302da987e82c445d5d2a24c7038883b8bb52b8836229f5d4be41ef55839db].
```

---

## NQ16

**Question:** What kinetic sampling strategies are used in PFAS adsorption, removal, or degradation experiments, and what do they show about early uptake and endpoint timing?

### Task components

- `NQ16-T01`: Identify and describe the kinetic sampling strategies (i.e., timing and frequency of sample collection) used in PFAS adsorption, removal, or degradation experiments, with attention to how early-time sampling is implemented to capture rapid initial uptake or fast reaction phases, when such behavior is reported.
- `NQ16-T02`: Explain how later-time or endpoint sampling is scheduled in PFAS adsorption, removal, or degradation experiments to assess equilibrium, plateau behavior, or reaction completion, and describe how this timing is reported to depend on the reaction speed and the specific system behavior.
- `NQ16-T03`: Summarize what the reported kinetic sampling strategies reveal about the transition from early uptake to equilibrium or endpoint conditions in PFAS experiments, only where the underlying studies explicitly support such interpretations, and without implying that a single fixed set of time intervals is universally applicable.

### Normative claim groups

#### NQ16-G01

- Component: `NQ16-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: PFAS adsorption kinetic experiments use dense early-time sampling (from minutes to a few hours) to capture rapid initial uptake, with specific time grids such as 30–480 minutes for PAC systems and early-hour windows (≤6 h) for other adsorbents.
- Full: Give full credit if the answer notes that kinetic sampling strategies in the cited PFAS adsorption systems include multiple early-time sampling points designed to capture rapid initial uptake, explicitly mentioning at least one concrete time grid or time window (e.g., 30–480 min in Son et al., >80% PFOS uptake within the first 6 h in Militao et al., or PFOS complete removal within 2 h and GenX equilibrium at 6 h in Chaudhary et al.).
- Partial: Give partial credit if the answer correctly notes that these studies report rapid initial adsorption within an early time window but does not clearly describe the corresponding sampling intervals or conflates early-time behavior with general equilibrium behavior.
- Contradiction: Mark as contradictory if the answer claims that early-time sampling is sparse or unnecessary in these systems, or if it asserts that initial uptake is slow in any of the cited studies despite the evidence of fast early adsorption.
- Linked exact evidence:
  - `NQ16_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=27ad9c2c6d0d3128d362f052c0fd7044c5d1d83b203ed2a8f459a17110ca741c];
    Supports: Shows that in the early-time sampling window (30–60 min) most adsorption (around 70% removal by 30 min) is already captured, underscoring the need for early sampling to resolve fast uptake.
  - `NQ16_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=b191d2284cefcaf97f21b5452045758880bc7bb139b41adfc84932b8633ad124].
    Supports: Indicates that in the alginate-biochar system, the majority of PFOS adsorption (>80%) occurs within an early-time window of the first 6 h, motivating sampling in this period.
  - `NQ16_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=5243d776515d9ed980296e6c2780c1d3644dc08476e0bf29ec6e65627416eca8].
    Supports: Shows that in the carbonaceous adsorbent system, important kinetic behavior (complete PFOS removal, GenX equilibrium) occurs within the first 2–6 h, implying that kinetic sampling must cover this early-hours window.

#### NQ16-G02

- Component: `NQ16-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Later-time and endpoint sampling in PFAS adsorption kinetics are scheduled out to several hours or longer to capture constant efficiency, plateau, or equilibrium behavior, with the required duration varying widely among systems.
- Full: Give full credit if the answer explains that later-time or endpoint kinetic sampling is extended until constant efficiency, plateau, or equilibrium is observed, using specific examples such as Son et al.'s constant efficiency at ~240 min and 90% adsorption at 60–360 min, Militao et al.'s plateau within 16 h, and Chaudhary et al.'s equilibrium windows ranging from 2–6 h for their adsorbents to tens or hundreds of hours for some GAC systems.
- Partial: Give partial credit if the answer correctly notes that sampling continues until a plateau or equilibrium is reached and that the required time varies, but omits explicit timing examples or conflates plateau behavior with merely reduced rates without acknowledging constant efficiency or equilibrium.
- Contradiction: Mark as contradictory if the answer asserts that equilibrium is always reached at the same fixed time across systems, or if it claims that these studies did not extend sampling to capture equilibrium/plateau behavior.
- Linked exact evidence:
  - `NQ16_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=27ad9c2c6d0d3128d362f052c0fd7044c5d1d83b203ed2a8f459a17110ca741c];
    Supports: Shows that Son et al. sampled out to at least 240–360 min, observing constant efficiency at ~240 min and different times (60 vs 360 min) to reach 90% adsorption, which reflects later-time/endpoint behavior and its PFAS-specific variation.
  - `NQ16_MMG001`
    > The others required 360 min to reach 90% adsorption.
    Supports: Reinforces that some PFASs needed extended contact (360 min) to approach high removal, indicating later-time sampling to capture near-endpoint behavior.
  - `NQ16_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=b191d2284cefcaf97f21b5452045758880bc7bb139b41adfc84932b8633ad124].
    Supports: Indicates that Militao et al. followed the kinetics long enough (up to ~16 h) to observe slow kinetics and a plateau, defining an endpoint window for PFOS adsorption in that system.
  - `NQ16_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=5243d776515d9ed980296e6c2780c1d3644dc08476e0bf29ec6e65627416eca8].
    Supports: Provides explicit equilibrium/endpoint times ranging from 2–6 h in Chaudhary et al.'s system; the full chunk text also notes comparator studies with longer equilibrium times, demonstrating how later-time sampling is scheduled differently depending on adsorbent properties and system behavior.

#### NQ16-G03

- Component: `NQ16-T03`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: The reported kinetic sampling strategies reveal a transition from rapid initial uptake to slower, plateauing or equilibrium behavior in PFAS adsorption, with this transition occurring at different times depending on the adsorbent and PFAS, and thus not supporting a universal kinetic sampling schedule.
- Full: Give full credit if the answer explicitly connects early-time rapid uptake (e.g., 70% removal in 30 min; >80% PFOS uptake within 6 h; complete PFOS removal within 2 h) with later-time plateau or constant efficiency (e.g., constant efficiency at ~240 min; plateau within 16 h; equilibrium between 4 and 168 h depending on adsorbent), and emphasizes that these transitions and timings vary across systems, so no universal kinetic schedule is implied.
- Partial: Give partial credit if the answer mentions a qualitative transition from fast initial adsorption to slower or plateau behavior but either omits clear timing examples or fails to state that the transition timing depends on system-specific factors.
- Contradiction: Mark as contradictory if the answer claims there is no distinct early fast phase followed by slower plateau behavior in these studies, or if it suggests that the early-to-equilibrium transition always occurs at the same time for all PFAS adsorption experiments.
- Linked exact evidence:
  - `NQ16_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=27ad9c2c6d0d3128d362f052c0fd7044c5d1d83b203ed2a8f459a17110ca741c];
    Supports: Directly describes a transition from an initially fast adsorption phase (~70% in 30 min) to a later constant-efficiency regime at ~240 min in the PAC system.
  - `NQ16_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=b191d2284cefcaf97f21b5452045758880bc7bb139b41adfc84932b8633ad124].
    Supports: Shows a clear progression from a fast initial adsorption stage (>80% in 6 h) to slower kinetics and plateau by 16 h, and interprets the initial phase as a diffusion-controlled process.
  - `NQ16_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=5243d776515d9ed980296e6c2780c1d3644dc08476e0bf29ec6e65627416eca8].
    Supports: Illustrates that different PFASs and adsorbents show different transition times to equilibrium (2 vs 6 h), and the full chunk text further summarizes comparator studies with equilibrium times ranging from several hours to many tens of hours, reinforcing that transition behavior and timing are system-dependent rather than universal.

#### NQ16-X01

- Component: `NQ16-T03`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: PFAS kinetic studies in the supplied evidence indicate that equilibrium times and kinetic transitions depend strongly on adsorbent properties and system conditions, so one must not generalize a single fixed set of sampling intervals as universally applicable.
- Full: Treat as a constraint that any answer must acknowledge or at least not contradict: equilibrium times and kinetic behavior are strongly dependent on adsorbent properties and PFAS/system specifics, and reported equilibrium times range widely, so it is incorrect to state or imply that a single fixed set of sampling intervals is appropriate for all PFAS kinetic experiments.
- Partial: If the answer fails to mention variability but also does not claim a universal schedule, this constraint is not violated but also not explicitly addressed.
- Contradiction: If the answer claims or clearly implies that one fixed sampling schedule (e.g., specific time points) is universally suitable for all PFAS adsorption/removal/degradation kinetics, or denies that equilibrium time depends on adsorbent/system properties, mark this as violating the constraint.
- Linked exact evidence:
  - `NQ16_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=5243d776515d9ed980296e6c2780c1d3644dc08476e0bf29ec6e65627416eca8].
    Supports: Explicitly demonstrates that equilibrium timing differs between PFASs (2 vs 6 h in this system), and the full chunk text further notes much longer equilibrium times in comparator GAC/PAC studies, supporting the conclusion that equilibrium time is strongly dependent on adsorbent properties and that no single sampling schedule is universally applicable.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

Across the PFAS adsorption studies represented in the supplied evidence, kinetic sampling strategies are structured to resolve both rapid early uptake and later-time approach to plateau or equilibrium, with specific time grids tuned to the system behavior rather than following a single universal schedule.

For adsorption of nine PFASs on powder-activated carbon (PAC) from surface water, Son et al. report that sorption kinetics were measured as removal efficiency versus time at 30, 60, 120, 240, 360, and 480 minutes at 10 mg/L PAC. They note [SOURCE_TEXT_OMITTED sha256=4f1f833410d4dae88f3249ff2b5a3a84c5343bc8badc10f500a6bb3e39eb85d3] that for several PFASs “70–80% and 90% of the adsorption process was accomplished within 30 and 60 min, respectively.” This sampling grid, with multiple points in the first 1–2 hours, captures the rapid initial uptake phase. Later points out to 240–480 minutes are used to follow the system toward steady behavior: Son et al. state that “constant efficiency was observed at ~240 min” and that “the others required 360 min to reach 90% adsorption.” Thus, in this PAC system, kinetic sampling is dense enough at early times to quantify the fast initial removal and extended long enough to see the transition to a constant-efficiency regime and near-endpoint conditions, with different PFASs approaching 90% adsorption at different contact times.

In Militao et al.’s study of PFOS removal using alginate-encapsulated rice-straw biochar, the temporal pattern is resolved at the scale of hours. They report that “[SOURCE_TEXT_OMITTED sha256=43ea0e20aa5e7346b81bf3a51c1e5d6d8145bab3c679db05586ff8e8fd38d1a0].” The description of an “initial fast adsorption stage” followed by “slow kinetics that plateaued” indicates that sampling covered the initial hours to capture rapid uptake and was extended to at least ~16 hours to observe the plateau. These data show a clear transition: most adsorption occurs in the early 6-hour window, while additional contact time mainly reveals a slowing approach to a plateau, which defines the endpoint for this system.

Chaudhary et al. examine PFAS (including PFOS and GenX) adsorption on regenerable carbonaceous adsorbents under mixed PFAS/Cd(II) conditions and likewise report distinct early and later kinetic regimes on the timescale of hours. They state that “[SOURCE_TEXT_OMITTED sha256=dddd9a43f113842d89cfd3794b4843aa6d41075919bea02131bf1e37124c1357].” Their discussion emphasizes that “the time required to reach the PFAS adsorption equilibrium is strongly dependent on the adsorbent properties.” To illustrate this dependence, they summarize literature where PFOS and PFOA adsorption on granular activated carbon (GAC) required 168 h for equilibrium, while powdered activated carbon (PAC) in another study gave equilibrium within 4 h for PFOS and PFOA; additional reports cited include equilibrium times of 24 h for PFOS, ~120 h for PFOA, and ~15 h for PFOA and PFOS on PAC. Together, these examples show that endpoint sampling in PFAS adsorption experiments can range from a few hours to several days, depending on adsorbent type and PFAS identity, and that kinetic experiments are typically continued until equilibrium or a clear plateau is reached for the specific system.

Taken as a whole, the evidence shows that PFAS kinetic experiments commonly employ early-time sampling that is fine-grained enough (minutes to a few hours) to capture rapid initial uptake phases, followed by extended sampling (hours to days) to characterize the transition to constant efficiency or plateaued adsorption. The transition from fast uptake to slower, plateau-like behavior is explicitly documented in multiple systems: ~70% removal in 30 minutes with constant efficiency at ~240 minutes on PAC; >80% PFOS removal within 6 hours and plateau by 16 hours on alginate-biochar; complete PFOS removal within 2 hours and GenX equilibrium at 6 hours on certain carbonaceous adsorbents; and equilibrium times from 4 to 168 hours in other GAC and PAC systems. These observations also demonstrate that both early uptake dynamics and endpoint timing depend strongly on adsorbent properties and PFAS-specific interactions, so the reported strategies illustrate principles for scheduling kinetic sampling but do not support a single fixed set of time intervals as universally applicable across all PFAS adsorption, removal, or degradation experiments.

### Unresolved or unsupported boundaries

- The specific individual sampling time points (exact schedule and frequency) used in Militao et al.’s and Chaudhary et al.’s kinetic experiments beyond the reported early and endpoint windows are not detailed in the provided excerpts.
- Any kinetic sampling strategies for PFAS removal or degradation processes other than adsorption (e.g., advanced oxidation or biological degradation) are not described in the supplied evidence.
- The evidence does not specify how many replicate samples were taken at each time point or the exact analytical handling between sampling and analysis.
- No information is provided on kinetic sampling strategies for PFAS mixtures beyond the PFOS and GenX examples in the Chaudhary et al. mixed-contaminant system.

### Complete approved source chunks

#### NQ16_MMG001

- Role: `required_gold`
- Document: `2020 - Son - The Adsorption Selectivity of Short and Long Per- and Polyfluoroalkyl Substances (PFASs) from Surface Water Using Powder-Activated Carbon.pdf`
- Chunk: `30`
- Registered exact span: The others required 360 min to reach 90% adsorption.

```text
[SOURCE_TEXT_OMITTED sha256=d433230c616d8875b99fd7e0c5ebb14e603f426917ae95fb03b82da96d0caadd]),
```

#### NQ16_MMG002

- Role: `required_gold`
- Document: `2020 - Son - The Adsorption Selectivity of Short and Long Per- and Polyfluoroalkyl Substances (PFASs) from Surface Water Using Powder-Activated Carbon.pdf`
- Chunk: `29`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=27ad9c2c6d0d3128d362f052c0fd7044c5d1d83b203ed2a8f459a17110ca741c];

```text
[SOURCE_TEXT_OMITTED sha256=337b938883f906355d98b3d4d5ee8f9aa4dd9b36e1e29127813e408037345d7b].
```

#### NQ16_MMG003

- Role: `required_gold`
- Document: `2023 - Militao - PFAS removal from water by adsorption with alginate-encapsulated plant albumin and rice straw-derived biochar.pdf`
- Chunk: `35`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=b191d2284cefcaf97f21b5452045758880bc7bb139b41adfc84932b8633ad124].

```text
[SOURCE_TEXT_OMITTED sha256=e39fc3e05a7fecc369c30122eab63790d1acc8c9f4ac5c22cb81409e74993311]
```

#### NQ16_MMG004

- Role: `required_gold`
- Document: `2025 - Chaudhary - Simultaneous removal of PFAS and cadmium from different water matrices using regenerable carbonaceous adsorbents.pdf`
- Chunk: `17`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=5243d776515d9ed980296e6c2780c1d3644dc08476e0bf29ec6e65627416eca8].

```text
[SOURCE_TEXT_OMITTED sha256=4fc9b5090068fcc3a605e0781053d5b56324ba8a73faad0f6677e54980bfbf4c]
```

---

## NQ18

**Question:** What removal mechanisms are proposed for PFAS sorbents, and how well are those mechanisms supported by reported observations?

### Task components

- `NQ18-T01`: Identify and describe the specific PFAS removal mechanisms that have been proposed for different classes of PFAS sorbents (e.g., carbonaceous, mineral, polymeric, ion-exchange), explicitly linking each proposed mechanism to the sorbent characteristics, PFAS structures (e.g., chain length, functional headgroup, branching), and relevant experimental conditions (e.g., pH, ionic strength, co-solutes).
- `NQ18-T02`: Summarize the reported observational evidence (e.g., isotherms, kinetics, selectivity trends across PFAS, effects of changing conditions) that supports or challenges each proposed removal mechanism for the different sorbent–PFAS–condition combinations, and evaluate how directly and convincingly the observations substantiate the mechanisms.
- `NQ18-T03`: Integrate across sorbents, PFAS structures, and conditions to assess how multiple interactions may simultaneously contribute to PFAS removal for a given system, clarifying when and how different mechanisms appear to co-occur or shift in relative importance without asserting a single universal dominant interaction type.

### Normative claim groups

#### NQ18-G01

- Component: `NQ18-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Across PFAS sorbents, the major adsorption/sorption mechanisms proposed include electrostatic interactions, hydrophobic interactions, ligand and ion exchange, hydrogen bonding, pore-filling, cation bridging, complexation, and van der Waals interactions, with these mechanisms inferred largely from adsorption experiments.
- Full: Give full credit when an answer states that multiple PFAS adsorption/sorption mechanisms have been proposed, naming at least several of electrostatic interactions, hydrophobic interactions, ligand and/or ion exchange, hydrogen bonding, pore-filling, cation bridging, complexation, and van der Waals interactions, and noting that these mechanisms are largely inferred from adsorption experiments.
- Partial: Give partial credit if the answer lists at least two distinct mechanisms (e.g., hydrophobic and electrostatic, plus one other) but omits others or does not mention that they are inferred from adsorption experiments.
- Contradiction: Mark as contradictory if the answer claims that only a single mechanism type (e.g., only hydrophobic interactions) is proposed for PFAS sorbents overall, or denies that mechanisms such as electrostatic interactions or hydrophobic interactions have been proposed, despite the review evidence.
- Linked exact evidence:
  - `NQ18_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=dd5a448eb647b89369d8be4d57feaea408481ed5b80296389c788200e9e68724].
    Supports: Supports that proposed PFAS interaction mechanisms are largely inferred from adsorption experiment observations.
  - `NQ18_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=287f9f7a67df7c5c235284e922ffd71407646975348e463e811f33229ebe816f].
    Supports: Supports that major PFAS adsorption mechanisms include electrostatic interactions, hydrophobic interactions, ligand and ion exchange, and hydrogen bonding.
  - `NQ18_MMG003` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=ca841e672ff3d356c55411f4aef0ba7a034092c7e8fc6783fe49899e0f114bec]
    Supports: Supports that PFAS sorption mechanisms on sorbents are complicated and that the main mechanisms include hydrophobic interactions, electrostatic interactions, pore-filling, cation bridging, complexation, ion exchange, van der Waals interactions, and hydrogen bonding.
  - `NQ18_MMG006`
    > [SOURCE_TEXT_OMITTED sha256=0f425a075ea3d5232f2029d391a295631a2d0d5face98225b7b89af71975aa3f].
    Supports: Supports that van der Waals forces have been previously claimed as involved in PFAS adsorption mechanisms on various adsorbents.
  - `NQ18_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=414e1e72e29bae172c4df026b84d03f77ba6a7099b078d091339ed3891efd316].
    Supports: Supports that besides hydrophobic and electrostatic interactions, other proposed mechanisms including hydrogen bonding and ligand exchange have been reported to contribute to PFAS adsorption.

#### NQ18-G02

- Component: `NQ18-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Hydrophobic interactions between the fluorinated carbon chain of PFAS and hydrophobic regions of sorbents are proposed as a primary driving force for adsorption of long-chain PFAS, whereas short-chain PFAS are more hydrophilic and cannot rely heavily on hydrophobic interactions for removal.
- Full: Give full credit if the answer explains that hydrophobic interactions between PFAS fluorinated chains and hydrophobic sorbent regions are considered a major adsorption mechanism for long-chain PFAS, but that short-chain PFAS are more hydrophilic and therefore cannot depend predominantly on hydrophobic interactions.
- Partial: Give partial credit if the answer mentions hydrophobic interactions as important for PFAS adsorption without distinguishing long-chain versus short-chain behavior, or only notes that short-chain PFAS are more hydrophilic without clearly linking this to reduced hydrophobic mechanisms.
- Contradiction: Mark as contradictory if the answer states that hydrophobic interactions are the dominant or primary mechanism for short-chain PFAS removal, or denies that hydrophobic interactions are especially relevant for long-chain PFAS.
- Linked exact evidence:
  - `NQ18_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=cc4fd8c6d91f2c60054c04ff77dba0b4e85f3d3a9b85347ac6daad149c138aef].
    Supports: Supports that short-chain PFAS are hydrophilic and that mechanisms for their adsorption cannot heavily rely on hydrophobic interactions.
  - `NQ18_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=66cd910eb947e6d89a05509c1d1e1f54098ae0df378dd5e53090b56ae933b786]
    Supports: Supports that long-chain PFAS adsorption can be dominated by hydrophobic interactions between their long hydrophobic tails and hydrophobic sorbent regions.
  - `NQ18_MMG003` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=769aef367b5958f8a93c2e8ea0efe0c83b14050dc561592c9638c3ea5c53ab03]
    Supports: Supports that hydrophobic interactions between PFAS hydrophobic C–F chains and hydrophobic sorbent regions are the primary driving force for long-chain analogues with high hydrophobicity.
  - `NQ18_MMG004` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=e6c5f8df609cf6c8cf934b07523a497f931227b6816fc547edf40672f17e863d].
    Supports: Supports that a longer hydrophobic fluorocarbon chain (PFOA vs PFBA) increases hydrophobic partition on biochars, consistent with chain-length-dependent hydrophobic interactions.

#### NQ18-G03

- Component: `NQ18-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Electrostatic interactions between anionic PFAS headgroups (e.g., SO3− and COO−) and positively charged sorbent surfaces, including ion-exchange resins and cationic or Fe-modified surfaces, are widely proposed as key mechanisms, often involving ion exchange and being sensitive to pH and surface charge.
- Full: Give full credit if the answer notes that anionic PFAS headgroups (e.g., PFCA and PFSA SO3− and COO− groups) interact electrostatically with positively charged sorbent surfaces, including ion-exchange resins or Fe/cation-modified materials, often via ion exchange of PFAS anions with counter-ions, and that these interactions depend on pH and surface charge.
- Partial: Give partial credit if electrostatic attraction between anionic PFAS and positively charged sorbents is mentioned without explicitly naming ion exchange or pH dependence, or if ion exchange is discussed but without clear linkage to PFAS anionic headgroups and sorbent charge.
- Contradiction: Mark as contradictory if the answer claims that anionic PFAS adsorption on positively charged sorbents is not governed by electrostatic or ion-exchange interactions, or asserts that pH and surface charge have no influence on such adsorption.
- Linked exact evidence:
  - `NQ18_MMG003` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > Electrostatic interactions can form between head groups of anionic and cationic PFASs and charged sorbents
    Supports: Supports that electrostatic interactions form between PFAS headgroups and charged sorbents.
  - `NQ18_MMG003` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=02ebde406b8ee81cfee9a5614f70467820759a3c665a81c2ba400c5c76e9ac62]
    Supports: Supports that PFCA and PFSA molecules have hydrophilic heads including SO3²− and COO− groups, which can participate in electrostatic interactions.
  - `NQ18_MMG004` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=4dcdf7b76795a7fad269bbe4c595b1a25905e0b1d90b5e7927afb99204701292]
    Supports: Supports that increasing positive surface charge (via Fe doping increasing zeta potential) enhances electrostatic interaction with anionic PFAS, changing the relative contribution of hydrophobic partition vs electrostatic mechanisms.
  - `NQ18_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=da4fa8c22e4eac055c39945efcfdec415a4892c8f95fbff3b3e6bdeda21e8208].
    Supports: Supports that positively charged sites on sorbents can exchange ions with PFAS functional headgroups, indicating an ion-exchange mechanism coupled to hydrophobic interactions.
  - `NQ18_MMG005` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=5ce1e5f080cb057f3d9a121fb44b8431c37e0cff949a80fbbbe64efa0dc90320].
    Supports: Supports that electrostatic interactions and ion exchange are evidenced by chloride displacement and pH-dependent adsorption efficiency as sorbent surface charge becomes neutral, weakening attraction for anionic PFAS.
  - `NQ18_MMG005` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=7fdb6fbd04529d38d18272192838a5f911b5640063675561c7e7e497ea61d162].
    Supports: Supports that short-chain PFAS removal by ion exchange resins is primarily via electrostatic interactions, and that long-chain PFAS adsorption on positively charged resins is enhanced by micelle/hemimicelle formation on the sorbent surface.
  - `NQ18_MMG006` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=a866b9f6b79afc074f1e4a3725deaa5b1b71a1b76839e8bbe0656cfee05bd336].
    Supports: Supports that sorption onto carbonaceous surfaces can involve electrostatic attractions, and that sorption onto magnetite can occur through electrostatic attraction to positive surface sites and hydrogen bonding.

#### NQ18-G04

- Component: `NQ18-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Across published adsorption studies, hydrophobic, electrostatic, and combined hydrophobic–electrostatic mechanisms are frequently reported, with some studies also suggesting contributions from hydrogen bonding, fluorine–fluorine interactions, and ligand exchange; however, proposed mechanisms are largely qualitative and rely on indirect observations rather than direct molecular evidence.
- Full: Give full credit if the answer summarizes that in a large set of PFAS adsorption studies, many authors explicitly attribute removal to hydrophobic interactions, electrostatic interactions, or a combination of both, with a smaller number proposing other weaker mechanisms such as hydrogen bonding and ligand exchange, and notes that these inferences are mainly based on adsorption experiment observations (e.g., isotherms, kinetic trends) rather than direct molecular-scale evidence.
- Partial: Give partial credit if the answer mentions that many studies report hydrophobic and electrostatic mechanisms without providing the counts or acknowledging that mechanisms are inferred from observations rather than directly measured.
- Contradiction: Mark as contradictory if the answer states that almost no studies discuss mechanisms, or that only a single mechanism type (e.g., hydrophobic only) is reported across the literature, contradicting the review statistics.
- Linked exact evidence:
  - `NQ18_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=daf28ba5d8cf0b9b3b623692e7b87b60ebd8f790af368cd3c19087dd15350d4a].
    Supports: Supports that a substantial subset of 136 reviewed studies explicitly noted interaction types responsible for observed adsorption behavior.
  - `NQ18_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=0761c2aceadf7994ad84fa4b2a579e71e905df607527a9318e09833287657c22].
    Supports: Supports the distribution of reported mechanisms: hydrophobic, electrostatic, and combined hydrophobic–electrostatic interactions across the reviewed studies.
  - `NQ18_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=414e1e72e29bae172c4df026b84d03f77ba6a7099b078d091339ed3891efd316].
    Supports: Supports that a smaller number of studies reported additional mechanisms like hydrogen bonding, fluorine–fluorine interactions, and ligand exchange contributing to PFAS adsorption.
  - `NQ18_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=dd5a448eb647b89369d8be4d57feaea408481ed5b80296389c788200e9e68724].
    Supports: Supports that discussions of mechanisms are mostly based on adsorption experiment observations rather than direct molecular measurements.

#### NQ18-G05

- Component: `NQ18-T02`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: For Fe-doped graphitized biochars, quantitative partitioning analyses indicate that hydrophobic partition accounts for only a limited proportion of PFOA and PFBA sorption, and Fe-doping increases positive surface charge (zeta potential) to enhance electrostatic interactions and pore-filling contributions, thereby reducing the relative contribution of hydrophobic mechanisms.
- Full: Give full credit for this group if the answer describes that in Fe-doped graphitized biochar systems, hydrophobic partition contributes only a limited percentage to PFOA and PFBA sorption, and that Fe doping increases positive surface charge (zeta potential), strengthening electrostatic interactions and highlighting pore-filling and electrostatics as major mechanisms while reducing the relative role of hydrophobic partition.
- Partial: Give partial credit if the answer notes qualitatively that Fe doping makes electrostatic interactions more important than hydrophobic interactions in PFAS sorption on biochar, without specifying that hydrophobic partition is only a limited proportion.
- Contradiction: Mark as contradictory if the answer asserts that hydrophobic partition is the dominant or nearly exclusive mechanism for PFAS sorption on Fe-doped biochars, contrary to the reported limited contribution and strengthened electrostatics.
- Linked exact evidence:
  - `NQ18_MMG004` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=93db4e660f65c1661a7b0dec626c7171bb95c95518f67cb80f9f3b93f3f95587]
    Supports: Supports that hydrophobic partition accounted for only a limited proportion of PFOA and PFBA sorption on the studied biochars.
  - `NQ18_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=0dbc92fa032ee2c947b0308d8be6f757c554073d776a0e3ca07f7a83389865ec].
    Supports: Supports that electrostatic interaction and pore-filling are important sorption mechanisms in addition to hydrophobic partition.
  - `NQ18_MMG004` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=4dcdf7b76795a7fad269bbe4c595b1a25905e0b1d90b5e7927afb99204701292]
    Supports: Supports that Fe doping increases zeta potential, improving electrostatic interactions with anionic PFAS and reducing the relative contribution of hydrophobic partition in sorption.

#### NQ18-G06

- Component: `NQ18-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: For ion-exchange resins with hydrophobic functional groups and positively charged sites, observational evidence such as chloride displacement and pH-dependent adsorption efficiency supports a combined mechanism of hydrophobic interactions and electrostatic ion exchange, with short-chain PFAS primarily removed via electrostatic interactions and long-chain PFAS removal enhanced by micelle and hemimicelle formation on the positively charged surface.
- Full: Give full credit if the answer describes that for ion-exchange resins, hydrophobic functional groups contribute hydrophobic interactions while positively charged sites mediate ion exchange with PFAS headgroups, and that this is supported by evidence of chloride displacement and pH-dependent adsorption efficiencies, with short-chain PFAS relying mainly on electrostatic interactions and long-chain PFAS adsorption enhanced by micelle/hemimicelle formation on positively charged surfaces.
- Partial: Give partial credit if the answer correctly discusses either the electrostatic/ion-exchange nature of short-chain PFAS removal or the combined hydrophobic and ion-exchange behavior (including pH effects) without integrating all these aspects, such as micelle formation for long-chain PFAS.
- Contradiction: Mark as contradictory if the answer claims that ion-exchange resins remove PFAS purely via hydrophobic interactions without electrostatics, or asserts that pH and ion displacement observations do not support electrostatic ion-exchange mechanisms.
- Linked exact evidence:
  - `NQ18_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=da4fa8c22e4eac055c39945efcfdec415a4892c8f95fbff3b3e6bdeda21e8208].
    Supports: Supports that hydrophobic functional groups on the sorbent contribute hydrophobic interactions while positively charged sites perform ion exchange with PFAS headgroups.
  - `NQ18_MMG005` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=5ce1e5f080cb057f3d9a121fb44b8431c37e0cff949a80fbbbe64efa0dc90320].
    Supports: Supports that electrostatic interactions and ion exchange are evidenced by increased chloride in effluent and decreased adsorption efficiency with increasing pH as surface charge becomes neutral.
  - `NQ18_MMG005` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=7fdb6fbd04529d38d18272192838a5f911b5640063675561c7e7e497ea61d162].
    Supports: Supports that short-chain PFAS removal on ion-exchange resins is primarily via electrostatic interactions, and that long-chain PFAS adsorption is enhanced by micelle and hemimicelle formation on positively charged sorbent surfaces.
  - `NQ18_MMG005` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=9a5fe043ab46730b49fe4d903d2d55673d14bc0031928a5f910ef41cb8afdac7].
    Supports: Supports that for long-chain PFAS, adsorption capacity on resins depends strongly on the hydrophobicity of the sorbent functional group, implicating hydrophobic interactions.

#### NQ18-G07

- Component: `NQ18-T03`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Multiple interactions—including hydrophobic partition, electrostatic attraction/ion exchange, pore-filling, aggregation, and hydrogen bonding—can simultaneously contribute to PFAS removal on a given sorbent (e.g., carbonaceous or Fe-doped biochar, magnetite, ion-exchange resins), and experimental evidence shows that their relative importance can shift with PFAS chain length and solution conditions such as pH and surface modification.
- Full: Give full credit if the answer explains that multiple interactions (e.g., hydrophobic partition, electrostatic attraction/ion exchange, pore-filling, aggregation, hydrogen bonding) can simultaneously contribute to PFAS removal on specific sorbents like carbonaceous biochars, Fe-doped materials, magnetite, and ion-exchange resins, and notes that their relative importance shifts with factors such as PFAS chain length and conditions (e.g., Fe-induced changes in zeta potential, pH affecting surface charge), using concrete examples such as PFOA vs PFBA, short- vs long-chain PFAS, or the coexistence of hydrophobic, electrostatic, and micelle-based mechanisms on resins.
- Partial: Give partial credit if the answer states that multiple mechanisms co-occur for at least one sorbent–PFAS system but does not clearly illustrate how their relative contributions change with chain length or conditions.
- Contradiction: Mark as contradictory if the answer asserts that only a single mechanism operates for a given PFAS–sorbent system under all conditions, or claims that mechanisms do not vary with PFAS structure or environmental conditions, contradicting evidence of shifting contributions.
- Linked exact evidence:
  - `NQ18_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > 48 studied attributed the observed sorption to a combination of both hydrophobic and electrostatic interactions.
    Supports: Supports that many studies attribute PFAS sorption to a combination of hydrophobic and electrostatic interactions, indicating co-occurring mechanisms.
  - `NQ18_MMG003` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > The mechanisms underlying PFAS sorption on various sorbents are complicated.
    Supports: Supports that PFAS sorption mechanisms are complex, implying contributions from multiple interactions.
  - `NQ18_MMG003` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=59b1140ddb32d00aa86fd776adaa3fd3238ef340920e199658bc34a3f7f891f0]
    Supports: Supports that multiple different mechanisms (hydrophobic, electrostatic, pore-filling, cation bridging, complexation, ion exchange, van der Waals, hydrogen bonding) may all be involved, consistent with co-occurrence.
  - `NQ18_MMG004` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=cc22c7999d89564244e7050939d2afacf8db9442ee08dd42f4829cc8fb0183c8]
    Supports: Supports that hydrophobic partition is present but limited, implying that other mechanisms also contribute to sorption on biochars.
  - `NQ18_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=0dbc92fa032ee2c947b0308d8be6f757c554073d776a0e3ca07f7a83389865ec].
    Supports: Supports that, in addition to hydrophobic partition, electrostatic interaction and pore-filling are important sorption mechanisms on the same sorbents.
  - `NQ18_MMG004` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=aa5cb57f9f8160b8f05f3d21077414633d8a772b4cd80bc549dfbab3511b89a8]
    Supports: Supports that changing sorbent surface charge (via Fe doping) shifts the balance between electrostatic and hydrophobic mechanisms.
  - `NQ18_MMG004` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=e6c5f8df609cf6c8cf934b07523a497f931227b6816fc547edf40672f17e863d].
    Supports: Supports that PFAS chain length (PFOA vs PFBA) affects the relative contribution of hydrophobic partition, changing the balance of mechanisms.
  - `NQ18_MMG006` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > Sorption onto carbonaceous surfaces can occur through hydrophobic interactions, aggregation, and electrostatic attractions
    Supports: Supports that on carbonaceous surfaces multiple mechanisms—hydrophobic interactions, aggregation, and electrostatic attractions—can all contribute to sorption.
  - `NQ18_MMG006` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=b9191a94972eb74afc4563435978db3edb3711596e09ef2831eae570331c3c19].
    Supports: Supports that two mechanisms—electrostatic attraction and hydrogen bonding—can co-occur on magnetite surfaces.
  - `NQ18_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=da4fa8c22e4eac055c39945efcfdec415a4892c8f95fbff3b3e6bdeda21e8208].
    Supports: Supports that on one sorbent (resin) both hydrophobic interactions and ion exchange mechanisms operate simultaneously.
  - `NQ18_MMG005` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=7fdb6fbd04529d38d18272192838a5f911b5640063675561c7e7e497ea61d162].
    Supports: Supports that for a given class of sorbents (ion-exchange resins) mechanisms shift with PFAS chain length: short-chain dominated by electrostatics, long-chain additionally enhanced by micelle/hemimicelle formation.

#### NQ18-X01

- Component: `NQ18-T03`
- Importance: `supplementary`
- Scoring role: `constraint_only`
- Proposition: π–π bonding between PFAS and sorbent surfaces is not a plausible adsorption mechanism because PFAS C–F backbones lack π-electrons, and van der Waals forces are considered weak and unimportant for PFAS adsorption due to low fluorine polarizability and small PFAS molecular sizes.
- Full: Use this as a constraint to avoid giving credit to answers that present π–π bonding or strong van der Waals forces as major PFAS adsorption mechanisms. Answers may mention these only with appropriate caveats about their implausibility or weak contribution.
- Partial: Not applicable for scoring; used only to limit overclaims about π–π and van der Waals mechanisms.
- Contradiction: Flag as problematic if an answer asserts π–π bonding between PFAS backbones and sorbents or emphasizes van der Waals forces as important or dominant mechanisms for PFAS adsorption, contrary to this mechanistic evidence.
- Linked exact evidence:
  - `NQ18_MMG006`
    > [SOURCE_TEXT_OMITTED sha256=6afb6c1f3d3a257e5bc89274764db0dc5cffa37e7b2144b71f26366f3ca764a7].
    Supports: Supports that π–π bonding is formally impossible between PFAS backbones and sorbents due to absence of π-electrons.
  - `NQ18_MMG006` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=a9e7d7ca83e6e91ef81a44023548b85a8541300ba6a1f4dd1160c91bb1551011]
    Supports: Supports that van der Waals forces are considered weak and unimportant for PFAS adsorption due to low fluorine polarizabilities and small PFAS molecular sizes.
  - `NQ18_MMG006`
    > [SOURCE_TEXT_OMITTED sha256=0f425a075ea3d5232f2029d391a295631a2d0d5face98225b7b89af71975aa3f].
    Supports: Provides context that van der Waals forces had been previously claimed as mechanisms, which this source then critiques as weak and unimportant.

#### NQ18-X02

- Component: `NQ18-T01`
- Importance: `supplementary`
- Scoring role: `constraint_only`
- Proposition: Mechanistic understanding of PFAS sorption remains largely phenomenological, as current discussions are mostly based on adsorption experiment observations and computational studies typically use simplified systems, highlighting that proposed mechanisms may not capture all complexities of practical environments.
- Full: Use this constraint to avoid treating the described mechanisms as fully validated or exhaustive; answers should not overstate mechanistic certainty and should acknowledge that most mechanisms are inferred from adsorption data and simplified models, not complete mechanistic proofs.
- Partial: Not used for partial credit; it only constrains overconfident mechanistic claims.
- Contradiction: Flag as problematic if an answer implies that PFAS sorption mechanisms are fully established by comprehensive molecular-scale evidence across all conditions, ignoring the stated reliance on adsorption observations and simplified computational models.
- Linked exact evidence:
  - `NQ18_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=047bdb92c44785ea8ed81693d10d82469d7a82a84e8f628f827cf54b6853da8c].
    Supports: Supports that computational studies use simplified systems and require further improvement to capture practical environmental complexity.
  - `NQ18_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=dd5a448eb647b89369d8be4d57feaea408481ed5b80296389c788200e9e68724].
    Supports: Supports that mechanistic discussions are primarily based on adsorption experiment observations, not fully comprehensive molecular evidence.

#### NQ18-X03

- Component: `NQ18-T03`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: No single universal mechanism type can be assumed to dominate PFAS removal across all sorbent–PFAS–condition combinations; mechanisms vary with PFAS chain length and sorbent design, and short-chain PFAS in particular cannot rely heavily on hydrophobic interactions.
- Full: Use this constraint to ensure that answers acknowledge variability in dominant mechanisms across PFAS classes and sorbents and do not claim a single universal dominant interaction type; specifically, they should not suggest that hydrophobic interactions dominate for all PFAS, given the hydrophilic nature of short-chain PFAS and evidence of shifting mechanism contributions.
- Partial: Not used for partial credit; it only constrains overgeneralized mechanism claims.
- Contradiction: Flag as problematic if an answer claims that one mechanism such as hydrophobic interactions or electrostatics is universally dominant for PFAS removal across all PFAS structures and sorbents, contradicting evidence that short-chain PFAS cannot heavily rely on hydrophobic interactions and that mechanism contributions shift with chain length and surface properties.
- Linked exact evidence:
  - `NQ18_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=cc4fd8c6d91f2c60054c04ff77dba0b4e85f3d3a9b85347ac6daad149c138aef].
    Supports: Supports that hydrophobic interactions cannot be universally dominant because short-chain PFAS are hydrophilic and cannot heavily rely on them.
  - `NQ18_MMG004` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=e6c5f8df609cf6c8cf934b07523a497f931227b6816fc547edf40672f17e863d].
    Supports: Supports that mechanism contributions (here hydrophobic partition) vary with PFAS chain length (PFOA vs PFBA).
  - `NQ18_MMG004` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=aa5cb57f9f8160b8f05f3d21077414633d8a772b4cd80bc549dfbab3511b89a8]
    Supports: Supports that modifying sorbent design (Fe doping) changes relative contributions of hydrophobic vs electrostatic mechanisms, indicating no universal dominant type.
  - `NQ18_MMG005` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=7fdb6fbd04529d38d18272192838a5f911b5640063675561c7e7e497ea61d162].
    Supports: Supports that different mechanisms dominate for short- vs long-chain PFAS on the same sorbent class, arguing against a universal mechanism.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

Reviews of PFAS sorbents agree that PFAS removal from water proceeds through several interacting adsorption or sorption mechanisms rather than a single dominant process. Based largely on adsorption experiments, major proposed mechanisms include electrostatic interactions, hydrophobic interactions, ligand and ion exchange, hydrogen bonding, and additional contributions from pore-filling, cation bridging, complexation, and van der Waals interactions (where the latter are generally considered weak) [NQ18_MMG001; NQ18_MMG003; NQ18_MMG006]. These mechanisms are generally inferred phenomenologically from adsorption behaviors, and current computational studies still use simplified systems that do not fully represent practical sorbent environments [NQ18_MMG001].

Chain-length-dependent hydrophobic interactions are a central theme. For long-chain PFAS such as PFOA and PFOS, the hydrophobic C–F tail can interact strongly with hydrophobic regions of sorbents, and hydrophobic interactions are described as a primary driving force for adsorption of long-chain analogues with high hydrophobicity [NQ18_MMG002; NQ18_MMG003]. Quantitatively, a study on graphitized biochars found that PFOA exhibited a higher hydrophobic partition than PFBA on all biochars, attributed to PFOA’s longer hydrophobic fluorocarbon chain [NQ18_MMG004]. In contrast, a critical review emphasizes that adsorption mechanisms designed for short-chain PFAS “cannot heavily rely on hydrophobic interactions, given the hydrophilic nature of these compounds” [NQ18_MMG002], underscoring that hydrophobic uptake cannot be assumed universal across PFAS structures.

Electrostatic mechanisms are closely tied to PFAS functional headgroups and sorbent charge. Anionic PFAS such as PFCAs and PFSAs have hydrophilic heads (e.g., SO3²− and COO−) that can form electrostatic interactions with charged sorbents [NQ18_MMG003]. In a broad sorption-mechanism review, electrostatic interactions are explicitly identified as a main mechanism alongside hydrophobic interactions, pore-filling, cation bridging, complexation, ion exchange, van der Waals interactions, and hydrogen bonding [NQ18_MMG003]. Experimental work on Fe-doped graphitized biochars illustrates how sorbent modification shifts the mechanism balance: hydrophobic partition accounted for only 3.04–25.7% of PFOA sorption and 0.94–13.6% of PFBA sorption, leading the authors to conclude that other mechanisms, “for example electrostatic interaction and pore-filling, are important sorption mechanisms” [NQ18_MMG004]. Fe doping increased the zeta potential of biochars, thereby improving electrostatic interaction with anionic PFAS and reducing the relative contribution of hydrophobic partition [NQ18_MMG004]. This example directly links sorbent surface charge, PFAS anionic character, and the relative importance of electrostatic versus hydrophobic pathways.

Ion-exchange resins provide a clear case of combined hydrophobic and electrostatic removal mechanisms. A review describing PFAS-specific resins notes that their hydrophobic functional groups contribute hydrophobic interactions with PFAS, while “the positively charged sites exchange ions for the PFAS functional head group” [NQ18_MMG005]. Electrostatic interactions and ion exchange are supported observationally by increased chloride concentration in the effluent as PFAS are adsorbed, and by the effect of solution pH: adsorption efficiency decreases with increasing pH as the sorbent surface becomes neutral, weakening attraction for anionic PFAS [NQ18_MMG005]. The same review states that short-chain PFAS are “primarily removed by ion exchange resins via electrostatic interactions,” while for long-chain PFAS adsorption “is enhanced by the formation of micelles and hemimicelles on the positively charged surface of the sorbent” [NQ18_MMG005]. Additionally, for long-chain PFAS, the adsorption capacity of resins depends strongly on how hydrophobic the sorbent functional group is—the more hydrophobic the functional group, the higher the removal efficiency [NQ18_MMG005]. Together, these observations support a multi-mechanistic picture: electrostatic ion exchange dominating for short-chain PFAS, with added hydrophobic and micelle/hemimicelle-driven contributions for long-chain PFAS on the same resin platforms.

For carbonaceous and mineral sorbents, similar multi-mechanism behavior is evident. Mechanistic reviews summarize that PFAS sorption on various sorbents is “complicated” and can involve hydrophobic interactions, electrostatic interactions, pore-filling, cation bridging, complexation, ion exchange, van der Waals interactions, and hydrogen bonding [NQ18_MMG003]. A study of Douglas fir biochar and its Fe3O4 hybrids notes that sorption onto carbonaceous surfaces can occur through “hydrophobic interactions, aggregation, and electrostatic attractions,” while sorption onto the magnetite phase may occur through “electrostatic attraction to positive surface sites and hydrogen bonding” [NQ18_MMG006]. These examples show that even within a single composite material, different phases (carbon vs magnetite) may operate through different but concurrent mechanisms.

Evidence from a large survey of adsorption studies highlights how these mechanistic proposals are distributed across the literature. Out of 136 studies reviewed, 109 explicitly noted the type of interaction thought responsible for observed PFAS adsorption behavior [NQ18_MMG002]. Among these, 34 reported hydrophobic interactions as the dominant mechanism, 19 reported electrostatic interactions, 48 attributed sorption to a combination of hydrophobic and electrostatic interactions, and eight reported other interactions such as hydrogen bonding, fluorine–fluorine interactions, or ligand exchange contributing, even if weakly [NQ18_MMG002]. This distribution directly supports the view that hydrophobic and electrostatic interactions are most frequently invoked, often together, but that additional mechanisms such as hydrogen bonding and ligand/ion exchange are also considered relevant in some systems.

More detailed analysis on Fe-doped graphitized biochars further illustrates shifting mechanism contributions with PFAS structure and sorbent modification. Hydrophobic partition represented only a limited fraction of total sorption (3.04–25.7% for PFOA and 0.94–13.6% for PFBA), with PFOA showing higher hydrophobic partition than PFBA due to its longer fluorocarbon chain [NQ18_MMG004]. The authors interpret this as evidence that electrostatic interaction and pore-filling are important mechanisms in addition to hydrophobic partition [NQ18_MMG004]. Fe doping increased the biochars’ zeta potential, improving electrostatic interaction with anionic PFAS and correspondingly reducing the relative role of hydrophobic partition [NQ18_MMG004]. These observations support a mechanism model in which hydrophobic interactions, electrostatics, and pore-filling all operate, with their relative importance controlled by both PFAS chain length and sorbent surface chemistry.

Collectively, these sources also constrain which non-specific interactions should be considered plausible dominant mechanisms. While van der Waals forces have previously been claimed to be involved in PFAS adsorption, a mechanistic analysis argues that van der Waals forces appear “weak and unimportant in adsorption because of the low fluorine polarizabilities and small PFAS molecular sizes” and that [SOURCE_TEXT_OMITTED sha256=7f75352ceb9db63c53e3c7bc64617957c31367aab7e444cece848df61c789551]” [NQ18_MMG006]. Thus, despite their occasional mention, π–π interactions cannot be regarded as a valid PFAS–sorbent mechanism, and van der Waals forces are unlikely to be a primary driver compared with hydrophobic partition, electrostatic attraction, or chemically specific interactions.

Across sorbent classes, PFAS structures, and solution conditions, the available evidence supports a multi-mechanistic, context-dependent view of PFAS removal. Long-chain PFAS on hydrophobic and positively charged sorbents often experience strong hydrophobic interactions plus electrostatic attraction, sometimes accompanied by micelle or hemimicelle formation, while short-chain PFAS rely more heavily on electrostatic ion exchange and other non-hydrophobic pathways [NQ18_MMG002; NQ18_MMG005]. On carbonaceous and Fe-modified biochars, hydrophobic partition coexists with electrostatic interactions and pore-filling, with Fe-induced changes in zeta potential shifting the balance toward electrostatics [NQ18_MMG004; NQ18_MMG006]. On magnetite, electrostatic attraction and hydrogen bonding can both contribute [NQ18_MMG006]. At the same time, mechanistic assignments remain largely based on adsorption data and simplified modeling [NQ18_MMG001], so they should be interpreted as strongly suggested by, but not fully proven by, the current body of evidence. The literature therefore indicates that multiple interactions can and do contribute simultaneously to PFAS removal, and their relative importance varies with PFAS chain length, functional headgroup, sorbent composition and surface charge, and experimental conditions such as pH, without supporting any single universal dominant interaction type across all systems.


### Unresolved or unsupported boundaries

- Mechanistic roles of PFAS branching, specific headgroup chemistries beyond SO3²− and COO− (e.g., ether linkages), and other PFAS subclasses are not described in the provided evidence.
- Detailed kinetic model forms (e.g., pseudo-first-order vs pseudo-second-order) or isotherm model fits (e.g., Freundlich vs Langmuir) as mechanistic evidence are not presented in the supplied text.
- Direct spectroscopic or molecular modeling evidence identifying specific binding configurations (e.g., exact hydrogen-bond geometries or complexation motifs) is not included in the provided sources.
- Mechanisms for polymeric sorbents beyond ion-exchange resins and for other mineral sorbents besides magnetite are not covered in the current evidence set.

### Complete approved source chunks

#### NQ18_MMG001

- Role: `required_gold`
- Document: `2021 - Wang - Selectivity of Per- and Polyfluoroalkyl Substance Sensors and Sorbents in Water.pdf`
- Chunk: `53`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=dd5a448eb647b89369d8be4d57feaea408481ed5b80296389c788200e9e68724].

```text
[SOURCE_TEXT_OMITTED sha256=bc7b8dda423daf26b2651521cc826ae325706f7f73167efc1d03049b86e3f799].
```

#### NQ18_MMG002

- Role: `required_gold`
- Document: `2023 - Smaili - Adsorption as a remediation technology for short-chain per- and polyfluoroalkyl substances (PFAS) from water - a critical review.pdf`
- Chunk: `30`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=daf28ba5d8cf0b9b3b623692e7b87b60ebd8f790af368cd3c19087dd15350d4a].

```text
[SOURCE_TEXT_OMITTED sha256=e856c44be2c4741f59ca9e530a0e3429c94784c60f40d5ebbdadb5dd18f46eb0]
```

#### NQ18_MMG003

- Role: `optional_gold`
- Document: `2022 - Yu - Sorptive removal of per- and polyfluoroalkyl substances from aqueous solution - Enhanced sorption, challenges and perspectives.pdf`
- Chunk: `27`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=d7cc46f7f9f2f2613d72f8e5f115b72276aa760f68565dd5b67432d707a7849f].

```text
[SOURCE_TEXT_OMITTED sha256=8b4c9e29ee6645a6855112118c1157c6b4c1aa3c83604d77d481bbdac62f9415] −,
```

#### NQ18_MMG004

- Role: `optional_gold`
- Document: `2023 - Liu - Porous Fe-doped graphitized biochar - An innovative approach for co-removing per- - polyfluoroalkyl substances with different chain lengths from.pdf`
- Chunk: `28`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=28d52f8bd6cdbb0fee2e5bc47c4ccecaf4858aff6819548adcbe2a6b2471581a] ).

```text
[SOURCE_TEXT_OMITTED sha256=7de04b6bcb0356d9dbdbddb351b4544f6247abd21b5c0355cc176ea91f8616c6]
```

#### NQ18_MMG005

- Role: `optional_gold`
- Document: `2023 - Smaili - Adsorption as a remediation technology for short-chain per- and polyfluoroalkyl substances (PFAS) from water - a critical review.pdf`
- Chunk: `22`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=da4fa8c22e4eac055c39945efcfdec415a4892c8f95fbff3b3e6bdeda21e8208].

```text
[SOURCE_TEXT_OMITTED sha256=3430744dc7135717064a0e2551cc59d87ce7acb50c2e7b98bcf29fe4bdd7af27].
```

#### NQ18_MMG006

- Role: `negative_gold`
- Document: `2022 - Rodrigo - Batch and fixed bed sorption of low to moderate concentrations of aqueous per- and poly-fluoroalkyl substances (PFAS) on Douglas fir biochar and.pdf`
- Chunk: `37`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=0f425a075ea3d5232f2029d391a295631a2d0d5face98225b7b89af71975aa3f].

```text
[SOURCE_TEXT_OMITTED sha256=77f9cbfd9cbafee4e529773afc09d42b58c518da6e9c21c553bd37f135f21640]
```

---

## NQ20

**Question:** How do real wastewater or groundwater matrices affect PFAS removal or degradation compared with simpler synthetic or DI-water matrices?

### Task components

- `NQ20-T01`: Summarize how PFAS removal or degradation efficiencies differ when tested in real wastewater or groundwater matrices versus in simple synthetic solutions or DI water, including any quantitative or directional changes in performance.
- `NQ20-T02`: Describe the roles of matrix-related phenomena—such as contaminant competition, radical or oxidant scavenging, sorption to solids or organic matter, and other changes in reaction mechanisms or mechanism interpretation—in explaining why PFAS removal or degradation in real matrices differs from that observed in DI water or simple synthetic matrices.

### Normative claim groups

#### NQ20-G01

- Component: `NQ20-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Across several technologies, PFAS removal or degradation is generally lower in real or complex matrices (wastewater, leachate, river and storm water) than in DI water or simple synthetic matrices, with decreases ranging from roughly a few percent up to more than an order of magnitude in rate constants, although some systems show only minor (<10%) differences.
- Full: Award full credit if the answer states that, in multiple cited studies, PFAS removal or degradation is generally lower in real/complex matrices (wastewater, landfill leachate, river or stormwater) than in DI or simple synthetic matrices, and it provides at least some quantitative or directional comparisons (e.g., % decrease in removal, fold-reduction in rate constants). It should also acknowledge that in at least one advanced system the difference between synthetic and real matrices is small (≤ ~10%).
- Partial: Award partial credit if the answer notes that real matrices usually reduce PFAS treatment performance compared to DI/synthetic water but gives only one example, lacks quantitative context, or omits mention that some systems exhibit only minor differences.
- Contradiction: Flag as contradiction if the answer claims that real matrices consistently give equal or higher PFAS removal or degradation than DI/synthetic matrices, or implies that matrix composition does not affect performance, contrary to the reported decreases in real matrices.
- Linked exact evidence:
  - `NQ20_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=8497bb6d539a7c48790dc14bc4c2556501f026c1c710bd2847085cf566c58a1a].
    Supports: Shows that in a nonthermal plasma-ozonation system, real wastewater has slightly lower PFAS defluorination (~3% lower) and that differences between synthetic and real wastewater did not exceed 10%.
  - `NQ20_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=65a21bb75bd3bba656550becdeebe7eeb5b3ac81d148875e5b9f9845a24260fb])
    Supports: Shows that in photocatalytic degradation with Cs@g-C3N4, PFOA and PFOS removal and apparent rate constants are higher in deionized water (93%, 0.0222 min⁻¹; 88%, 0.0177 min⁻¹) than in filtered river water (72%, 0.0106 min⁻¹; 68%, 0.00950 min⁻¹).
  - `NQ20_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=30efc6ed153944f767944dfd4b482103eb1345bff7766b63772dec23c67aab64].
    Supports: Quantifies that plasma-alone treatment in real wastewater has 22% lower degradation and 19% lower defluorination of PFOA compared to synthetic wastewater.
  - `NQ20_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=7ab4e6460c1d374a1f9f78436ecfdd7cbbee77583bc17004458f25127b73c7a8].
    Supports: States that for standalone plasma or ferrate processes, degradation performance is always better in synthetic wastewater than in real wastewater.
  - `NQ20_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=c702e926adacb332abf03d73be2c689b22167f503963a3f808c32fdb0d077670].
    Supports: Shows that sorbent-based PFAS removal is lower in untreated field stormwater than in simple synthetic stormwater.
  - `NQ20_MMG006`
    > [SOURCE_TEXT_OMITTED sha256=88635c6c77f32ab485b3c8ffa7331698d4b25215005b23ea2084453e2619daac].
    Supports: Provides a quantitative comparison showing that in electrochemical treatment, the normalized kinetic constant for PFOA removal in real landfill leachate is 13-fold lower than in a synthetic mixed PFAS solution and 26-fold lower than in a single-compound synthetic solution.
  - `NQ20_MMG008`
    > [SOURCE_TEXT_OMITTED sha256=4f735e374f0465bc0dd19dba51b50476cee1d8322c8ba90e74debd518e98bfea]] .
    Supports: Reports that in BDD electrochemical systems, PFOA degradation rates in landfill leachate are reduced by roughly 33–50% compared to a phosphate buffer electrolyte, another simple synthetic matrix.

#### NQ20-G02

- Component: `NQ20-T01`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: Some advanced or combined treatment processes can substantially overcome matrix inhibition and achieve PFAS degradation or removal in real wastewater that is similar to that in synthetic matrices, despite the presence of complex constituents.
- Full: Award full credit if the answer notes that certain integrated processes can achieve similar PFAS degradation/removal in real and synthetic matrices and cites at least one example where differences are ≤ ~10% or the efficiencies are explicitly said to be comparable.
- Partial: Award partial credit if the answer vaguely mentions that some advanced treatments are less sensitive to matrix effects but does not provide a clear example or quantitative indication that real-matrix performance approaches synthetic performance.
- Contradiction: Flag as contradiction if the answer implies that no processes can overcome matrix inhibition or that real matrices always cause large performance losses, contradicting evidence of near-equal performance in some combined systems.
- Linked exact evidence:
  - `NQ20_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=8497bb6d539a7c48790dc14bc4c2556501f026c1c710bd2847085cf566c58a1a].
    Supports: Indicates that in the nonthermal plasma-ozonation cascade reactor, differences between synthetic and real wastewater were ≤10%, suggesting similar performance in both matrices.
  - `NQ20_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=c689148890a36860aee274eb3883eaf916200cd6bd0cf7ffee4be5e836faa038].
    Supports: Shows that the combined plasma–ferrate process produced similar degradation kinetics in real and synthetic wastewater, indicating that this integrated process can overcome typical real-matrix inhibition and achieve comparable performance.
  - `NQ20_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=30efc6ed153944f767944dfd4b482103eb1345bff7766b63772dec23c67aab64].
    Supports: Shows that adding ferrate to plasma treatment increases PFOA degradation efficiency in real wastewater to 91%, comparable to 92% in synthetic wastewater, thereby overcoming the inhibition observed with plasma alone.
  - `NQ20_MMG007`
    > [SOURCE_TEXT_OMITTED sha256=4174f9282a5379d8d2d71d5aa22a0a4a554c2f098529ff501a5d49d88f36911b] %).
    Supports: Indicates that in a plasma–ferrate process, ferrate addition restores high PFOA removal in real wastewater to a level comparable to that in synthetic wastewater (≈90%).

#### NQ20-G03

- Component: `NQ20-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Matrix-related phenomena such as scavenging of reactive species by coexisting organics and inorganics, competition from natural organic matter, salts, iron, and other ions, and inhibition of sorbent performance explain much of the reduced PFAS removal or degradation in real or complex matrices compared with DI or simple synthetic solutions.
- Full: Award full credit if the answer explains that coexisting organic and inorganic constituents, natural organic matter, salts, metals, and competing ions in real matrices can scavenge reactive species or otherwise inhibit PFAS degradation/removal, and explicitly links these mechanisms to the observed lower performance compared with DI/synthetic matrices in at least two different process types (e.g., plasma-based, electrochemical, sorption).
- Partial: Award partial credit if the answer mentions at least one matrix-related phenomenon (such as radical scavenging by organic matter or competition from co-contaminants) but does not connect it clearly to multiple process types or does not relate it explicitly to the observed performance differences.
- Contradiction: Flag as contradiction if the answer asserts that background organics, salts, or other matrix components have no meaningful effect on PFAS treatment mechanisms or interpretation, or that such effects are always negligible, contradicting the reported scavenging and inhibition.
- Linked exact evidence:
  - `NQ20_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=30efc6ed153944f767944dfd4b482103eb1345bff7766b63772dec23c67aab64].
    Supports: Directly attributes decreased plasma-based PFOA degradation and defluorination in real wastewater to coexisting organic and inorganic compounds that scavenge key reactive species (eaq– and H•), hindering performance.
  - `NQ20_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=7ab4e6460c1d374a1f9f78436ecfdd7cbbee77583bc17004458f25127b73c7a8].
    Supports: Explains that better performance in synthetic wastewater is likely because it lacks natural organic matter, competing anions, and metal ions that in real wastewater can scavenge reactive species or interfere with reaction pathways.
  - `NQ20_MMG007`
    > [SOURCE_TEXT_OMITTED sha256=4174f9282a5379d8d2d71d5aa22a0a4a554c2f098529ff501a5d49d88f36911b] %).
    Supports: Shows that organics and competing ions in real wastewater quench reductive species, lowering plasma-alone efficiency, and that ferrate mitigates this by oxidizing/coagulating organics, restoring high PFOA removal.
  - `NQ20_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=c702e926adacb332abf03d73be2c689b22167f503963a3f808c32fdb0d077670].
    Supports: Indicates that in stormwater, salts, iron, and organic matter inhibit performance of PFAS sorbents compared to simple synthetic stormwater, implicating competition or blockage mechanisms.
  - `NQ20_MMG006`
    > [SOURCE_TEXT_OMITTED sha256=88635c6c77f32ab485b3c8ffa7331698d4b25215005b23ea2084453e2619daac].
    Supports: Describes a detrimental effect of the leachate matrix on overall PFAS removal kinetics compared with mixed PFAS in simulated groundwater, consistent with matrix interference in electrochemical treatment.
  - `NQ20_MMG008`
    > [SOURCE_TEXT_OMITTED sha256=4f735e374f0465bc0dd19dba51b50476cee1d8322c8ba90e74debd518e98bfea]] .
    Supports: Shows that using landfill leachate as background matrix reduces PFOA degradation rates by one third to one-half compared to a phosphate buffer electrolyte, illustrating a matrix effect in electrochemical systems.
  - `NQ20_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=8497bb6d539a7c48790dc14bc4c2556501f026c1c710bd2847085cf566c58a1a].
    Supports: Notes that the complexity of real wastewater composition affects PFAS degradation and defluorination in the nonthermal plasma reactor, consistent with matrix-related effects.

#### NQ20-X01

- Component: `NQ20-T01`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: Performance in DI water or simple synthetic matrices cannot be assumed to directly predict performance in real wastewaters, landfill leachates, river water, or stormwater because matrix effects can range from minor to severe.
- Full: Treat as a constraint that the answer should not imply that DI or simple synthetic matrix performance directly predicts real-matrix performance; instead it should acknowledge that observed matrix effects range from ≤10% to >10-fold changes depending on system and matrix.
- Partial: If the answer discusses matrix effects but seems to generalize one specific magnitude of effect (e.g., always small or always large) to all systems, apply this constraint to reduce overgeneralization but do not treat it as a scored content error.
- Contradiction: Flag a must-not-claim violation if the answer explicitly states that DI/synthetic performance directly predicts real wastewater performance without caveats, contradicting multiple studies showing varied and sometimes severe matrix effects.
- Linked exact evidence:
  - `NQ20_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=8497bb6d539a7c48790dc14bc4c2556501f026c1c710bd2847085cf566c58a1a].
    Supports: Shows that in at least one system, real versus synthetic wastewater differences are small (<10%), indicating not all matrix effects are large.
  - `NQ20_MMG006`
    > [SOURCE_TEXT_OMITTED sha256=88635c6c77f32ab485b3c8ffa7331698d4b25215005b23ea2084453e2619daac].
    Supports: Shows that in another system, the real leachate matrix reduces kinetic constants by 13- to 26-fold compared with synthetic matrices, indicating large possible matrix effects.
  - `NQ20_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=65a21bb75bd3bba656550becdeebe7eeb5b3ac81d148875e5b9f9845a24260fb])
    Supports: Illustrates that deionized water performance is substantially higher than in river water for a photocatalytic system, so DI results cannot be assumed to represent natural waters.
  - `NQ20_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=c702e926adacb332abf03d73be2c689b22167f503963a3f808c32fdb0d077670].
    Supports: Indicates that even when a sorbent performs well in simple synthetic stormwater, actual stormwater can reduce performance, again warning against direct extrapolation.
  - `NQ20_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=30efc6ed153944f767944dfd4b482103eb1345bff7766b63772dec23c67aab64].
    Supports: Shows that replacing synthetic wastewater with real wastewater in a plasma system decreases degradation and defluorination efficiencies by about 20%, reinforcing that performance in simple matrices does not directly predict that in real matrices.
  - `NQ20_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=7ab4e6460c1d374a1f9f78436ecfdd7cbbee77583bc17004458f25127b73c7a8].
    Supports: Shows that for standalone plasma or ferrate processes, synthetic wastewater consistently outperforms real wastewater, underscoring that simple-matrix performance is not directly transferable to complex real matrices.
  - `NQ20_MMG008`
    > [SOURCE_TEXT_OMITTED sha256=4f735e374f0465bc0dd19dba51b50476cee1d8322c8ba90e74debd518e98bfea]] .
    Supports: Demonstrates that switching from a simple phosphate buffer to landfill leachate can reduce PFOA degradation rates by one third to one-half, further confirming that matrix changes can cause substantial, system-specific performance shifts.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

Studies comparing PFAS treatment in simple versus real matrices consistently show that matrix composition can substantially change observed removal or degradation efficiencies, and that the direction and magnitude of the effect are system‑specific.

For nonthermal plasma–ozonation, Chen et al. report that in real wastewater the PFAS defluorination percentage is only "about 3 % lower in real wastewater" than in synthetic wastewater and that "the difference in results obtained in both matrices did not exceed 10 % in this study" (NQ20_MMG001). This indicates that for this particular reactor, matrix effects are present but modest.

In contrast, other systems show much stronger matrix inhibition. In photocatalytic degradation of PFOA and PFOS with Cs@g‑C3N4, El‑Sawaf et al. report that in deionized water the PFOA removal and apparent rate constant are 93 ± 1.5% and 0.0222 min⁻¹, and PFOS values are 88 ± 1.7% and 0.0177 min⁻¹, whereas in filtered river water the corresponding values drop to 72 ± 2.6% and 0.0106 min⁻¹ for PFOA and 68 ± 3.1% and 0.00950 min⁻¹ for PFOS (NQ20_MMG002). Thus, both removal and kinetics are substantially worse in the real river matrix than in DI water.

Chen et al. also evaluated plasma‑based degradation of PFOA in synthetic versus real landfill leachate. Under plasma alone, they found that "[SOURCE_TEXT_OMITTED sha256=7bd036259a9fcdccdf3ae782a18df7b0b38e1f0d93b71d3db747293ab141a3db]" (NQ20_MMG003), and more generally that when comparing synthetic and real wastewater under standalone plasma or ferrate, "degradation performance was consistently better in synthetic wastewater" (NQ20_MMG004). Urtiaga et al. report an even more pronounced effect for electrochemical oxidation: the normalized kinetic constant for PFOA removal in real MBR‑treated landfill leachate is k′ₙ,PFOA = 0.238 h⁻¹ A⁻¹ L, which is "about 13 times lower" than in a synthetic mixed PFAS solution simulating groundwater and "26 times lower than for treating PFOA in a highly concentrated single compound solution" (NQ20_MMG006). They further cite Pierpaoli et al., who found that when landfill leachate is used as the background matrix, "the rates of PFOA degradation ... were reduced by one third to one-half" compared to a phosphate buffer electrolyte (NQ20_MMG008). These results show that real leachate matrices can slow electrochemical PFAS degradation by factors ranging from roughly 1.3 to more than 10 relative to simple synthetic electrolytes.

For sorbent‑based treatment, Parker et al. observed that [SOURCE_TEXT_OMITTED sha256=699cb3e9ff1622701cd10a35af7fb65fa7954de6e5f3d9d2f8a034e613cd0723]" (NQ20_MMG005). The stormwater was characterized by salts, relatively high iron (210 µg L⁻¹), and organic matter, which "suggests that OGSIR SW constituents inhibit the sorbents' performance" (NQ20_MMG005). Thus, even when a sorbent performs well in a simple synthetic stormwater, actual field stormwater composition can impair PFAS removal.

Some advanced or combined processes can partly or fully overcome these matrix effects. In the nonthermal plasma‑ozonation cascade reactor, the fact that the real versus synthetic wastewater differences "did not exceed 10 %" (NQ20_MMG001) shows relatively robust performance against matrix complexity. In the plasma–ferrate system, Chen et al. note that plasma alone in real wastewater suffers an efficiency drop of about 20%, but that adding ferrate "[SOURCE_TEXT_OMITTED sha256=9d1be133226807e1ed239868df69466a9e85189df96b4d8797d25faf5d7a4c73] comparable to that in synthetic wastewater (≈ 90 %)" (NQ20_MMG007). The same work reports that the combined plasma–ferrate process gave "similar degradation kinetics in real and synthetic wastewater, suggesting that the integrated process effectively overcame the inhibitory effects typically associated with real water matrices" (NQ20_MMG004), and that ferrate addition raised PFOA degradation efficiency in real wastewater to 91%, "comparable to that observed in synthetic wastewater (92 %)" (NQ20_MMG003).

Mechanistically, several matrix‑related phenomena are implicated. In the plasma systems, Chen et al. attribute the reduced PFOA degradation and defluorination in real wastewater primarily to "coexisting organic and inorganic compounds" that "act as scavengers of key plasma-generated reactive species, particularly eaq– [SOURCE_TEXT_OMITTED sha256=a6fb54a31e34b95bce02ca17a773877ca8f2a24780f0e1805b3d9997a37a2896]" (NQ20_MMG003). They further explain that performance is better in synthetic wastewater because it lacks "[SOURCE_TEXT_OMITTED sha256=9cb8cebdb9c7f5418a6c59a1c2ce870ff92e6f3f070da2f0b0ac0f9544624a12]" (NQ20_MMG004). The beneficial effect of ferrate is attributed to its ability to oxidize and coagulate organics, thereby "mitigating their quenching effect on reductive species" and restoring high removal (NQ20_MMG007).

In sorption systems, Parker et al. link decreased PFAS removal in untreated stormwater to the presence of "salts, iron ... and organic matter" (NQ20_MMG005), suggesting that these constituents compete with PFAS for sorbent sites, alter surface charge, or otherwise inhibit sorbent performance compared with the simpler sodium–chloride–carbonate composition of the synthetic stormwater.

Electrochemical studies do not detail specific scavenging reactions in the provided excerpts, but the observed 6‑ to 26‑fold decreases in normalized kinetic constants and the one‑third to one‑half rate reductions when landfill leachate replaces simulated groundwater or phosphate buffer electrolytes (NQ20_MMG006, NQ20_MMG008) are consistent with real matrices introducing additional electroactive species, competing ions, or natural organic matter that interfere with PFAS oxidation pathways.

Overall, the evidence shows that real wastewater, landfill leachate, river water, and stormwater matrices can substantially alter PFAS treatment performance relative to DI water or simple synthetic solutions. These changes arise largely from scavenging of key reactive species and competition or inhibition by salts, natural organic matter, metals, and other co‑contaminants. Because the magnitude of these effects ranges from minor (<10%) to more than an order-of-magnitude decrease in apparent kinetic constants, performance measured in DI or simple synthetic matrices cannot be assumed to directly predict outcomes in real wastewaters or environmental waters without explicitly considering matrix effects for the particular process and matrix in question.

### Unresolved or unsupported boundaries

- The question explicitly mentions groundwater, but the provided evidence does not include direct comparisons between real groundwater and DI water; only simulated groundwater or other synthetic solutions are described.
- Specific quantitative contributions of individual matrix components (e.g., the separate effects of iron versus organic matter on PFAS removal) are not resolved in the supplied excerpts.
- Changes in detailed reaction pathways or intermediate spectra in real versus DI matrices are not described beyond general statements about scavenging and interference with reaction pathways.

### Complete approved source chunks

#### NQ20_MMG001

- Role: `required_gold`
- Document: `2024 - Chen - Degradation of perfluoroalkyl and polyfluoroalkyl substances (PFAS) in water by use of a nonthermal plasma-ozonation cascade reactor - Role of.pdf`
- Chunk: `17`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=8497bb6d539a7c48790dc14bc4c2556501f026c1c710bd2847085cf566c58a1a].

```text
[SOURCE_TEXT_OMITTED sha256=c40654d7af04684e70a947a6d982341e544b33b472ab1a5dd40287b677e5696e]
```

#### NQ20_MMG002

- Role: `required_gold`
- Document: `2025 - El-Sawaf - Sustainable photocatalytic degradation of perfluoroctanoic acid (PFOA) and perfluorooctane sulfonate (PFOS) using chitosan-doped g-C₃N₄ for green.pdf`
- Chunk: `99`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=65a21bb75bd3bba656550becdeebe7eeb5b3ac81d148875e5b9f9845a24260fb])

```text
[SOURCE_TEXT_OMITTED sha256=266ee4a706b238b70c81a7ffe3079969478e83127a24ee7f896dd275f57e902c])
```

#### NQ20_MMG003

- Role: `required_gold`
- Document: `2026 - Chen - Ferrate-assisted nonthermal plasma for efficient PFOA degradation in landfill leachate - Mitigating bulk organic interference and enhancing.pdf`
- Chunk: `21`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=30efc6ed153944f767944dfd4b482103eb1345bff7766b63772dec23c67aab64].

```text
[SOURCE_TEXT_OMITTED sha256=69523b51c65675f8ff25012dd427cb7f1ead857c5c06a33cc4a2ae83c78afd3d] -
```

#### NQ20_MMG004

- Role: `required_gold`
- Document: `2026 - Chen - Ferrate-assisted nonthermal plasma for efficient PFOA degradation in landfill leachate - Mitigating bulk organic interference and enhancing.pdf`
- Chunk: `18`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=7ab4e6460c1d374a1f9f78436ecfdd7cbbee77583bc17004458f25127b73c7a8].

```text
[SOURCE_TEXT_OMITTED sha256=39cd5ef3164d953c77a372bfa91db4cc38118d520bd42533e05b174d8b7bd6aa]
```

#### NQ20_MMG005

- Role: `required_gold`
- Document: `2023 - Parker - rsc.li - es-water Evaluation of sorbents and matrix effects for treating heavy metals and per- and polyfluoroalkyl substances as co-contaminants in.pdf`
- Chunk: `19`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=c702e926adacb332abf03d73be2c689b22167f503963a3f808c32fdb0d077670].

```text
[SOURCE_TEXT_OMITTED sha256=69fdd5e324a4cce2ed020b455e6e08a76b94be965db90d0fbbd9f55ab1d54bee]
```

#### NQ20_MMG006

- Role: `required_gold`
- Document: `2022 - Urtiaga - Electrochemical treatment of municipal landfill leachates and implications for poly- and perfluoroalkyl substances (PFAS) removal.pdf`
- Chunk: `38`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=88635c6c77f32ab485b3c8ffa7331698d4b25215005b23ea2084453e2619daac].

```text
[SOURCE_TEXT_OMITTED sha256=80edcc68618dd09cd0b3daebec8c3597d6a6105b69630030db7a6dba14831b46]
```

#### NQ20_MMG007

- Role: `required_gold`
- Document: `2026 - Chen - Ferrate-assisted nonthermal plasma for efficient PFOA degradation in landfill leachate - Mitigating bulk organic interference and enhancing.pdf`
- Chunk: `38`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=4174f9282a5379d8d2d71d5aa22a0a4a554c2f098529ff501a5d49d88f36911b] %).

```text
[SOURCE_TEXT_OMITTED sha256=0f8c2ffecd6a900df0d5e97bdea088ebf035e6598ea2cb1badb5bcf5bfcb9834]
```

#### NQ20_MMG008

- Role: `optional_gold`
- Document: `2022 - Urtiaga - Electrochemical treatment of municipal landfill leachates and implications for poly- and perfluoroalkyl substances (PFAS) removal.pdf`
- Chunk: `39`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=4f735e374f0465bc0dd19dba51b50476cee1d8322c8ba90e74debd518e98bfea]] .

```text
[SOURCE_TEXT_OMITTED sha256=073a9e2cea2b3aa5e9d3583833ccb69f2e12a29db728a1cab8249c085c46cbcb].
```

---

## NQ22

**Question:** What endpoints are reported in photocatalytic PFAS treatment studies, and how clearly are removal, degradation, defluorination, and mineralization distinguished?

### Task components

- `NQ22-T01`: Summarize photocatalytic PFAS treatment as a research direction, explicitly describing the types of photocatalysts and irradiation conditions that are reported in studies (e.g., catalyst identity, light source/wavelength/intensity) without making maturity or full-mineralization claims beyond what is stated in the sources.
- `NQ22-T02`: Identify and describe the main endpoints reported in photocatalytic PFAS treatment studies, including but not limited to PFAS removal, PFAS degradation (e.g., transformation to intermediates), defluorination, and mineralization, as they are defined or operationalized in the literature.
- `NQ22-T03`: Evaluate how clearly photocatalytic PFAS treatment studies distinguish among the reported endpoints (removal vs degradation vs defluorination vs mineralization), including whether and how these are explicitly differentiated, conflated, or ambiguously reported in relation to specific catalysts and irradiation conditions.

### Normative claim groups

#### NQ22-G01

- Component: `NQ22-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Photocatalytic PFAS treatment studies investigate various photocatalysts under specified irradiation (visible or UV) conditions, including CS@g-C3N4, Ga/TNTs@AC, and a duo-functional tri-metallic-oxide hybrid photocatalyst, sometimes emphasizing adsorptive or duo-functional behavior and matrix-dependent performance.
- Full: Give full credit if the answer notes that photocatalytic PFAS treatment studies use specific photocatalysts such as CS@g-C3N4, Ga/TNTs@AC, and a duo-functional tri-metallic-oxide hybrid photocatalyst, and that these are operated under visible-light or UV irradiation and tested in various matrices (e.g., deionized water, natural matrices, river water, wastewater), without overclaiming technological maturity.
- Partial: Give partial credit if the answer mentions at least one named photocatalyst and an associated irradiation condition (e.g., visible light or UV), but omits others or does not mention matrix dependence.
- Contradiction: Mark as contradiction if the answer claims exclusively dark conditions or purely adsorptive non-photocatalytic operation for these systems, or asserts universal, unspecified irradiation without acknowledging visible or UV light, contrary to the evidence.
- Linked exact evidence:
  - `NQ22_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=950fafec59359ea34038a4b65bdbbb88b00e87228338166351ef0c9a26ba6369].
    Supports: Identifies CS@g-C₃N₄ as a photocatalyst operated under visible-light irradiation for PFAS treatment.
  - `NQ22_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=b61f09e0ca862c1f0fcfb973a3abe589e894819d05f43bdf93a8ccc7a72ca0fb].
    Supports: Shows CS@g-C₃N₄ photocatalyst being evaluated in complex media versus laboratory-grade (deionized) water, highlighting matrix dependence.
  - `NQ22_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=b61f09e0ca862c1f0fcfb973a3abe589e894819d05f43bdf93a8ccc7a72ca0fb].
    Supports: Indicates that the photocatalytic system is tested in deionized water and natural matrices, reflecting matrix-dependent behavior.
  - `NQ22_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=9fcf6d7ebb1e1cee538293e0341bc14541f4e79e842fcdd79c9c7faa756e0c75].
    Supports: Identifies Ga/TNTs@AC as an adsorptive photocatalyst for PFOS operated under 4 h of UV irradiation at pH 3.5, with Fe3+ as a variable.
  - `NQ22_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=9fcf6d7ebb1e1cee538293e0341bc14541f4e79e842fcdd79c9c7faa756e0c75].
    Supports: Shows that the Ga/TNTs@AC photocatalytic system is tuned by varying Fe3+ concentration, demonstrating process-condition variation under UV irradiation.
  - `NQ22_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=e92c7e8f3afb47a40dc134c35a5f672b8103ade3a4ac3b1a1fd15050399618fb] ).
    Supports: Indicates that photocatalytic removal with CS@g-C₃N₄ depends on matrix composition, catalyst dosing, and irradiation time, and contrasts deionized versus river water matrices.
  - `NQ22_MMG005`
    > • High removal efficiency of 99.8% and 99.4% for PFOS and PFOA, respectively.
    Supports: Identifies a duo-functional tri-metallic-oxide hybrid as a photocatalyst with both adsorption and photocatalytic functions for multiple PFASs.

#### NQ22-G02

- Component: `NQ22-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Photocatalytic PFAS studies report multiple distinct endpoints, including PFAS removal or disappearance (often via HPLC), mineralization via TOC reduction, defluorination via aqueous fluoride release, and sometimes overall removal efficiencies, with these endpoints operationalized and quantified separately.
- Full: Give full credit if the answer explains that photocatalytic PFAS studies measure (a) PFAS removal or disappearance (e.g., by HPLC), (b) TOC reduction as a mineralization endpoint, and (c) fluoride release as a defluorination endpoint, and notes that some studies also report overall removal efficiencies and adsorption capacities as part of photocatalytic performance.
- Partial: Give partial credit if at least two of the three main endpoint types (removal/degradation, TOC-based mineralization, fluoride-based defluorination) are described, even if one is missing or not clearly operationalized.
- Contradiction: Mark as contradiction if the answer claims that only a single endpoint (e.g., PFAS disappearance) is reported in these studies or denies the use of TOC or fluoride as separate endpoints, contrary to the described measurements.
- Linked exact evidence:
  - `NQ22_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=950fafec59359ea34038a4b65bdbbb88b00e87228338166351ef0c9a26ba6369].
    Supports: Shows separate reporting of HPLC-based degradation efficiencies (PFAS disappearance) and TOC removal (mineralization proxy) for PFOA and PFOS.
  - `NQ22_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=950fafec59359ea34038a4b65bdbbb88b00e87228338166351ef0c9a26ba6369].
    Supports: Explicitly interprets TOC decrease as indicating partial mineralization, defining TOC as a mineralization endpoint.
  - `NQ22_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=950fafec59359ea34038a4b65bdbbb88b00e87228338166351ef0c9a26ba6369].
    Supports: Demonstrates a fluorine mass balance including aqueous fluoride, residual PFAS, transformation products, and catalyst adsorption, treating fluoride as a defluorination endpoint and others as remaining organic fluorine.
  - `NQ22_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=b61f09e0ca862c1f0fcfb973a3abe589e894819d05f43bdf93a8ccc7a72ca0fb].
    Supports: Defines defluorination operationally as measurement of aqueous fluoride concentrations by ion chromatography.
  - `NQ22_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=b61f09e0ca862c1f0fcfb973a3abe589e894819d05f43bdf93a8ccc7a72ca0fb].
    Supports: Shows that measured fluoride release is interpreted as partial defluorination and is compared with TOC removal, linking defluorination and mineralization endpoints.
  - `NQ22_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=e92c7e8f3afb47a40dc134c35a5f672b8103ade3a4ac3b1a1fd15050399618fb] ).
    Supports: Connects measured F− (defluorination) with TOC data (mineralization) and PFAS disappearance, explicitly treating them as distinct yet related endpoints and noting short-chain fluorinated byproducts.
  - `NQ22_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=e92c7e8f3afb47a40dc134c35a5f672b8103ade3a4ac3b1a1fd15050399618fb] ).
    Supports: Reports ‘photocatalytic removal efficiencies’ as another endpoint, providing percent removal of PFOA and PFOS at trace levels and indicating matrix dependence.
  - `NQ22_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=9fcf6d7ebb1e1cee538293e0341bc14541f4e79e842fcdd79c9c7faa756e0c75].
    Supports: Indicates that PFOS photocatalysis on Ga/TNTs@AC tracks both degradation and mineralization profiles as separate but related endpoints.
  - `NQ22_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=9fcf6d7ebb1e1cee538293e0341bc14541f4e79e842fcdd79c9c7faa756e0c75].
    Supports: Shows that this study quantifies PFOS degradation and defluorination separately, each in percent terms, as distinct performance endpoints.
  - `NQ22_MMG005`
    > • High removal efficiency of 99.8% and 99.4% for PFOS and PFOA, respectively.
    Supports: Indicates that this photocatalyst study reports adsorption capacity, overall removal efficiency, and defluorination ratios as separate numerical endpoints.

#### NQ22-G03

- Component: `NQ22-T03`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Several photocatalytic PFAS studies explicitly distinguish among PFAS disappearance/removal, mineralization, and defluorination, highlighting gaps between these endpoints and recommending combined monitoring, though high removal or degradation is sometimes reported without full mineralization, showing that endpoints are related but not equivalent.
- Full: Give full credit if the answer notes that these photocatalytic studies explicitly distinguish removal/degradation from mineralization and defluorination, for example by (a) contrasting HPLC-based degradation with lower TOC removal and limited F− release, (b) separately reporting degradation and defluorination percentages, and/or (c) recommending both TOC and F− monitoring, while emphasizing that high removal does not necessarily mean complete mineralization or defluorination.
- Partial: Give partial credit if the answer indicates some recognition that endpoints differ (e.g., mentions a gap between removal and mineralization) but does not clearly explain how they are distinguished or does so for only one of the studies.
- Contradiction: Mark as contradiction if the answer asserts that removal, degradation, defluorination, and mineralization are used interchangeably or that high removal equates to complete mineralization in these studies, contrary to the explicit caveats in the evidence.
- Linked exact evidence:
  - `NQ22_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=950fafec59359ea34038a4b65bdbbb88b00e87228338166351ef0c9a26ba6369].
    Supports: Explicitly contrasts high HPLC-based degradation with much lower TOC removal, interpreting this gap as evidence of intermediates and incomplete mineralization, thereby distinguishing degradation from mineralization.
  - `NQ22_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=950fafec59359ea34038a4b65bdbbb88b00e87228338166351ef0c9a26ba6369].
    Supports: Shows that significant degradation does not imply complete defluorination; most fluorine remains in organic/adsorbed forms, distinguishing degradation from defluorination.
  - `NQ22_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=e92c7e8f3afb47a40dc134c35a5f672b8103ade3a4ac3b1a1fd15050399618fb] ).
    Supports: States that high PFAS disappearance coexists with limited mineralization and partial F− release, linking but distinguishing disappearance, TOC-based mineralization, and defluorination, and acknowledging fluorinated byproducts.
  - `NQ22_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=e92c7e8f3afb47a40dc134c35a5f672b8103ade3a4ac3b1a1fd15050399618fb] ).
    Supports: Recommends measuring defluorination (fluoride) alongside TOC to track mineralization, implying that neither endpoint alone fully captures treatment progress and emphasizing their distinct roles.
  - `NQ22_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=b61f09e0ca862c1f0fcfb973a3abe589e894819d05f43bdf93a8ccc7a72ca0fb].
    Supports: Shows that defluorination is explicitly defined and directly assessed, distinct from TOC or PFAS disappearance.
  - `NQ22_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=9fcf6d7ebb1e1cee538293e0341bc14541f4e79e842fcdd79c9c7faa756e0c75].
    Supports: Indicates that degradation and mineralization profiles are tracked separately for PFOS on Ga/TNTs@AC, distinguishing these endpoints under defined conditions.
  - `NQ22_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=9fcf6d7ebb1e1cee538293e0341bc14541f4e79e842fcdd79c9c7faa756e0c75].
    Supports: Reports distinct percentage values for PFOS degradation and defluorination under the same conditions, illustrating explicit separation of these endpoints.
  - `NQ22_MMG005`
    > • High removal efficiency of 99.8% and 99.4% for PFOS and PFOA, respectively.
    Supports: Lists adsorption capacity, removal efficiency, and defluorination ratios as separate metrics, implicitly distinguishing overall removal (which may include adsorption) from chemical defluorination.

#### NQ22-X01

- Component: `NQ22-T01`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: The available studies explicitly report that full mineralization and complete defluorination are limited, so answers must not claim universal full mineralization or technological maturity of photocatalytic PFAS treatment.
- Full: Treat as a hard boundary that answers must not claim that photocatalytic PFAS treatment universally achieves complete mineralization or defluorination, given explicit statements that mineralization is limited and most fluorine remains in organic or adsorbed forms.
- Partial: Not applicable; this group is used only to constrain overclaims.
- Contradiction: Mark as contradiction if the answer asserts that these photocatalytic systems achieve complete or near-complete mineralization or full defluorination of PFAS, or portrays the technology as universally mature, contrary to explicit limitations in the evidence.
- Linked exact evidence:
  - `NQ22_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=950fafec59359ea34038a4b65bdbbb88b00e87228338166351ef0c9a26ba6369].
    Supports: States that most fluorine remains in organic or adsorbed forms despite significant degradation, emphasizing that complete defluorination is challenging.
  - `NQ22_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=e92c7e8f3afb47a40dc134c35a5f672b8103ade3a4ac3b1a1fd15050399618fb] ).
    Supports: Indicates that recovered F− is only a fraction of what would be produced by complete mineralization, showing that full mineralization is not achieved.
  - `NQ22_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=e92c7e8f3afb47a40dc134c35a5f672b8103ade3a4ac3b1a1fd15050399618fb] ).
    Supports: Explicitly states that full mineralization is limited and that only partial fluoride release occurs with formation of fluorinated byproducts.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

Photocatalytic PFAS treatment is being actively investigated using a range of photocatalysts and irradiation conditions. One study employs CS@g-C₃N₄ under visible-light irradiation for 120 min to treat PFOA and PFOS, and evaluates performance in deionized water and more complex natural and river-water matrices. In this system, photocatalytic removal efficiencies at trace (10 µg·L⁻¹) levels reach up to 45% for PFOA and 40% for PFOS in deionized water but are substantially lower in higher-complexity river water, reflecting matrix effects on photocatalytic removal that depend on composition, concentration, catalyst dosing and irradiation time. Another work uses an adsorptive Ga/TNTs@AC photocatalyst to degrade PFOS under 4 h of UV irradiation at pH 3.5, studying the effect of Fe³⁺ as a cocatalyst. A separate study develops a duo-functional tri-metallic-oxide (f-TMO) hybrid photocatalyst, described as both adsorptive and photocatalytically active toward several PFASs including PFOA and PFOS.

Across these systems, several endpoint types are reported. For the CS@g-C₃N₄ visible-light system, HPLC-based PFAS disappearance is used as a degradation endpoint: after 120 min, PFOA and PFOS degradation efficiencies are 93% and 88%, respectively. Mineralization is evaluated via total organic carbon (TOC), where the same experiment shows TOC removal of only 27.1% for PFOA and 23% for PFOS; the TOC decrease is interpreted as indicating only partial mineralization. The authors further perform a fluorine mass balance, starting from a theoretical 2.568 mg of fluorine from PFOA and recovering only about 2.35% of this after 120 min, partitioned among aqueous fluoride, residual PFOA, transformation products, and fluorine adsorbed on the catalyst. This demonstrates that although PFOA degrades substantially, most fluorine remains in organic or adsorbed forms, underscoring that complete defluorination is difficult to achieve.

In the same CS@g-C₃N₄ study, defluorination is explicitly defined and measured as aqueous fluoride (F−) concentrations determined by ion chromatography for each test condition. Measurable fluoride release in deionized water is interpreted as partial defluorination, while diminished fluoride release in natural matrices coincides with reduced mineralization and lower TOC removal. The authors show that the recovered F− mass is only a fraction of the theoretical maximum F− that would result from complete mineralization of the initial PFAS load; combined with TOC data, this supports the conclusion that long-chain PFAS disappearance can be high under ideal conditions, yet full mineralization is limited and produces short-chain fluorinated byproducts plus only partial fluoride release. On this basis, they recommend including defluorination monitoring via fluoride analysis alongside TOC as a direct tracer of mineralization progress.

In the Ga/TNTs@AC system under UV irradiation, the study explicitly tracks PFOS photocatalytic degradation and mineralization profiles and separately quantifies defluorination. With Fe³⁺ as a cocatalyst, PFOS defluorination improves from 25.8% without Fe³⁺ to 36.4% and 44.7% at 25 and 40 µM Fe³⁺, respectively. At 60 µM Fe³⁺, PFOS degradation increases from 61.2% to 80.4% and defluorination from 25.8% to 70.0%, before declining at higher Fe³⁺ doses. These data show that degradation and defluorination are reported as separate percentage endpoints and that they respond differently to operating conditions, even though they are linked through the photocatalytic mechanism.

The duo-functional tri-metallic-oxide (f-TMO) hybrid photocatalyst study further illustrates endpoint separation by reporting high adsorption capacities for PFOS and PFOA, very high overall removal efficiencies of 99.8% and 99.4%, and distinct defluorination ratios of 74.8% for PFOA and 67.6% for PFOS. Here, overall removal encompasses both adsorption and photocatalytic processes, while defluorination ratios quantify the extent of C–F bond cleavage, reinforcing that removal and defluorination are not synonymous.

Taken together, these photocatalytic PFAS studies generally distinguish among several endpoints: (i) PFAS disappearance or removal, assessed via HPLC or mass-balance calculations; (ii) mineralization, inferred from TOC reduction; and (iii) defluorination, quantified by aqueous fluoride release and, in one case, through a detailed fluorine mass balance. The CS@g-C₃N₄ work explicitly contrasts high HPLC-based degradation with much lower TOC removal and very limited F− recovery, interpreting the gap as evidence for partially oxidized fluorinated intermediates, incomplete mineralization, and the challenge of complete defluorination. The Ga/TNTs@AC study reports degradation and defluorination percentages side by side and discusses changes in both with Fe³⁺ concentration, and the f-TMO study reports both overall removal and separate defluorination ratios alongside adsorption capacity. These examples show that, within the available evidence, authors generally treat removal/degradation, mineralization, and defluorination as related but distinct metrics rather than interchangeable terms, and they caution that high PFAS disappearance or removal does not imply full mineralization or complete defluorination.

### Unresolved or unsupported boundaries

- The specific wavelengths and light intensities used for visible-light and UV irradiation are not provided in the supplied evidence.
- The evidence does not describe detailed photocatalyst synthesis conditions or bandgap properties.
- There is no direct evidence about the overall technological maturity of photocatalytic PFAS treatment beyond the stated limitations on mineralization and defluorination.
- The full suite of intermediate transformation products and their toxicity are not characterized in the provided excerpts.
- No generalized conclusions about all photocatalytic PFAS systems beyond the specific CS@g-C₃N₄, Ga/TNTs@AC, and f-TMO examples can be supported from the supplied evidence alone.

### Complete approved source chunks

#### NQ22_MMG001

- Role: `required_gold`
- Document: `2025 - El-Sawaf - Sustainable photocatalytic degradation of perfluoroctanoic acid (PFOA) and perfluorooctane sulfonate (PFOS) using chitosan-doped g-C₃N₄ for green.pdf`
- Chunk: `83`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=950fafec59359ea34038a4b65bdbbb88b00e87228338166351ef0c9a26ba6369].

```text
[SOURCE_TEXT_OMITTED sha256=6a3a3baf45f52e66ce726a614b1faca07557d904cb6ec54cb7e16ba3a82fb21d]-
```

#### NQ22_MMG002

- Role: `required_gold`
- Document: `2025 - El-Sawaf - Sustainable photocatalytic degradation of perfluoroctanoic acid (PFOA) and perfluorooctane sulfonate (PFOS) using chitosan-doped g-C₃N₄ for green.pdf`
- Chunk: `97`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=e92c7e8f3afb47a40dc134c35a5f672b8103ade3a4ac3b1a1fd15050399618fb] ).

```text
[SOURCE_TEXT_OMITTED sha256=8e4bf956493cbc262f1a592888620fd3935e8089d73cb084ae048fb3a55f249a]
```

#### NQ22_MMG003

- Role: `optional_gold`
- Document: `2025 - El-Sawaf - Sustainable photocatalytic degradation of perfluoroctanoic acid (PFOA) and perfluorooctane sulfonate (PFOS) using chitosan-doped g-C₃N₄ for green.pdf`
- Chunk: `96`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=b61f09e0ca862c1f0fcfb973a3abe589e894819d05f43bdf93a8ccc7a72ca0fb].

```text
[SOURCE_TEXT_OMITTED sha256=61918a32ff881c8d9315f65d5711ecd74881c45367f8a3369f160c9674a6eba8]
```

#### NQ22_MMG004

- Role: `optional_gold`
- Document: `2026 - Zhu - Photocatalytic degradation of PFAS under field water matrix conditions using an adsorptive photocatalyst.pdf`
- Chunk: `35`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=9fcf6d7ebb1e1cee538293e0341bc14541f4e79e842fcdd79c9c7faa756e0c75].

```text
[SOURCE_TEXT_OMITTED sha256=9da35e329f91d091b29896e511a1968a4648f21aa7944a2d1fef0ea179d5e1f4] +
```

#### NQ22_MMG005

- Role: `optional_gold`
- Document: `2022 - Samuel - Photocatalytic degradation of perfluoroalkyl substances in water by using a duo-functional tri-metallic-oxide hybrid catalyst.pdf`
- Chunk: `0`
- Registered exact span: • High removal efficiency of 99.8% and 99.4% for PFOS and PFOA, respectively.

```text
[SOURCE_TEXT_OMITTED sha256=8bf7d9e0ba21bd20000aa7091e07a7c049472f8f71f959dd54fe6a8613f58a59]
```

---

## NQ27

**Question:** What options are discussed for managing spent PFAS-loaded adsorbents, and what residual-management concerns remain after adsorption?

### Task components

- `NQ27-T01`: Identify and describe the options discussed for managing spent PFAS-loaded adsorbents, such as regeneration, disposal, thermal treatment, or other post-use management strategies, explicitly recognizing that adsorption transfers or concentrates PFAS rather than destroying it.
- `NQ27-T02`: Explain the residual-management concerns that remain after adsorption, including issues such as remaining PFAS risk in spent adsorbents, potential for desorption or secondary contamination, and how different management options address or fail to address these concerns, without claiming that adsorption alone permanently eliminates PFAS risk or makes the spent adsorbent harmless.

### Normative claim groups

#### NQ27-G01

- Component: `NQ27-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Common management options for PFAS-loaded adsorbents include regeneration or replacement of the adsorbent, with specific regeneration strategies such as thermal, organic solvent-based, and chemical methods.
- Full: Award full credit if the answer states that spent PFAS-loaded adsorbents are commonly managed by replacement or regeneration and mentions at least one regeneration strategy (thermal, organic solvent-based, or chemical) as an end-of-life or reuse option, citing that these are current or common practices.
- Partial: Award partial credit if the answer mentions regeneration or replacement of PFAS-loaded adsorbents in general terms but does not detail specific regeneration strategies, or mentions just one type of regeneration without clearly linking it to spent PFAS adsorbents.
- Contradiction: Mark as contradictory if the answer claims that there are no regeneration options for PFAS-loaded adsorbents or that regeneration is not used at all for PFAS systems, contradicting the cited evidence.
- Linked exact evidence:
  - `NQ27_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=f9a80d5672aa7692f49173d7c0569bc1d3494d509aef14e60776a793777f3019]] .
    Supports: Supports that spent PFAS-loaded adsorbent must be replaced or regenerated as an operational management option.
  - `NQ27_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=98c1d7cbb3bcc1fd4f708a6ab811b40291f3c3f181cab9255005e8a6bb400ca9] ].
    Supports: Supports that regeneration and recycling are common end-of-life treatments for adsorption materials, alongside other options.
  - `NQ27_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=4c6700ec99720303b8cd2ed1b149a61a1b71a45cd761c9e902dde230b91ff084] ;
    Supports: Supports that failure to replace or regenerate GAC leads to exhaustion and potential PFAS leaching, underscoring the need for media replacement or regeneration.
  - `NQ27_MMG005` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=6da7c00665923344cf86d182ee31e2785e3f92694add3fe06687fb5b142ab5fe].
    Supports: Directly supports the importance of carbon replacement and/or regeneration as part of managing PFAS removal by GAC.
  - `NQ27_MMG009`
    > [[SOURCE_TEXT_OMITTED sha256=9305ff52b9932358d20167d56171dbb05984e5a41c8beb0946b35bb3dd1f6e70].
    Supports: Supports thermal regeneration/destruction, organic solvent-based regeneration, and chemical regeneration as regeneration strategies with reported PFAS desorption and recoveries.
  - `NQ27_MMG010`
    > [SOURCE_TEXT_OMITTED sha256=320e5baa4493eada4320f449e9d8c6378278280475e9a44b088fbeef8dad2868].
    Supports: Supports that thermal or chemical regeneration can restore the adsorptive capacity of coal fly ash (CFA) for reuse in PFAS adsorption.

#### NQ27-G02

- Component: `NQ27-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Landfilling and incineration, including high-temperature thermal destruction, are widely discussed disposal options for PFAS-loaded adsorbents, sometimes combined with stabilization or repurposing strategies.
- Full: Award full credit if the answer states that landfill disposal and incineration (including high-temperature thermal destruction) are key management options for PFAS-loaded adsorbents, and may additionally mention stabilization/solidification or repurposing (e.g., in construction materials) where supported.
- Partial: Award partial credit if only one of these disposal options (landfill or incineration) is mentioned without indicating that these are common or conventional options, or if stabilization/repurposing is mentioned without clearly linking it to PFAS-loaded adsorbents.
- Contradiction: Mark as contradictory if the answer asserts that landfilling and incineration are not used or not considered for PFAS-loaded adsorbents, or that high-temperature incineration is unnecessary for PFAS destruction, contradicting the evidence.
- Linked exact evidence:
  - `NQ27_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=6c0304fb3572efecc6732576502566d76a99e08bc372da424fa40510740ada33].
    Supports: Supports that common management options for saturated adsorbents include landfill disposal and incineration (along with desorption).
  - `NQ27_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=98c1d7cbb3bcc1fd4f708a6ab811b40291f3c3f181cab9255005e8a6bb400ca9] ].
    Supports: Supports that incineration with energy recovery and landfill disposal are common end-of-life treatments for adsorption materials.
  - `NQ27_MMG006`
    > incomplete recovery and generate secondary waste streams containing concentrated PFAS residues (Yadav et al.
    Supports: Supports that managing exhausted PFAS adsorbents can generate secondary waste streams with concentrated PFAS residues, highlighting environmental concerns around disposal options such as high-temperature incineration.
  - `NQ27_MMG007`
    > [SOURCE_TEXT_OMITTED sha256=2c986f843019c4f4e45fc1984eab4f387feb545eaf72a4249db8ccc47e0ff227].
    Supports: Supports that high-temperature incineration of spent adsorbent is a disposal option aimed at complete PFAS destruction and reducing dioxin generation.
  - `NQ27_MMG010`
    > [SOURCE_TEXT_OMITTED sha256=906d2a62dc3b61cd30110f10e7c03f6950812c1143e824f9e9d8f87e2d7a099b].
    Supports: Supports stabilization or solidification of spent CFA with subsequent disposal in controlled landfills as a management option.
  - `NQ27_MMG010`
    > [SOURCE_TEXT_OMITTED sha256=d6498a958d04f79e3998974ce8e96c2d41edd474c77f8999c0f6c41e05439629].
    Supports: Supports repurposing spent CFA in construction materials (cement or concrete) as another management option, subject to leachability standards.

#### NQ27-G03

- Component: `NQ27-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Regeneration of PFAS-loaded adsorbents often leaves residual PFAS on the adsorbent and generates secondary waste streams with concentrated PFAS, which can reduce adsorption capacity and create additional waste-treatment needs.
- Full: Award full credit if the answer explains that regeneration of PFAS-loaded adsorbents is often incomplete, leaving residual PFAS on the solid that decreases adsorption capacity, and that regeneration produces secondary waste streams (e.g., solvent waste, brine, PFAS-rich effluents) containing concentrated PFAS that then require additional management.
- Partial: Award partial credit if the answer notes either residual PFAS remaining on regenerated adsorbents or the generation of concentrated PFAS waste streams but not both aspects, or if it mentions capacity loss without explicitly connecting it to residual PFAS.
- Contradiction: Mark as contradictory if the answer claims that regeneration completely removes PFAS with no residual loading and produces no problematic secondary wastes, contradicting the evidence.
- Linked exact evidence:
  - `NQ27_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=39af40ce5a3e56e7a52f306fe5bea42cfa09480218ba1b7ec5d0efc064aa9e59]] .
    Supports: Reinforces that residual PFAS remains after regeneration and is linked to reduced adsorption capacity.
  - `NQ27_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=4c6700ec99720303b8cd2ed1b149a61a1b71a45cd761c9e902dde230b91ff084] ;
    Supports: Supports that if adsorbent is not replaced or suitably regenerated, PFAS can leach from exhausted GAC, indicating residual PFAS and potential breakthrough.
  - `NQ27_MMG006`
    > incomplete recovery and generate secondary waste streams containing concentrated PFAS residues (Yadav et al.
    Supports: Supports that regeneration can have incomplete PFAS recovery and generate secondary waste streams with concentrated PFAS residues.
  - `NQ27_MMG009`
    > [[SOURCE_TEXT_OMITTED sha256=9305ff52b9932358d20167d56171dbb05984e5a41c8beb0946b35bb3dd1f6e70].
    Supports: Supports that organic solvent-based regeneration produces PFAS-containing solvent waste requiring downstream treatment, and that chemical regeneration generates brine or surfactant-rich waste streams with incomplete desorption of strongly bound PFASs.

#### NQ27-G04

- Component: `NQ27-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Post-adsorption residual-management concerns include PFAS leaching from landfilled or exhausted adsorbents, risks of secondary contamination, and incomplete or uncertain destruction and by-product management in thermal treatment, leading to strict requirements for containment, stabilization, and flue-gas cleaning.
- Full: Award full credit if the answer notes that adsorbed PFAS remains a risk after adsorption, citing leaching or secondary contamination from exhausted or disposed adsorbents, concerns about completeness and by-products from incineration/thermal destruction, and mitigation strategies such as controlled landfills, stabilization/solidification, or advanced flue gas cleaning.
- Partial: Award partial credit if the answer mentions only one major concern (e.g., leaching from exhausted adsorbents or incomplete incineration) without describing other residual risks or mitigation strategies.
- Contradiction: Mark as contradictory if the answer asserts that once PFAS is adsorbed the spent adsorbent is harmless, poses no leaching or secondary contamination risk, or that standard incineration universally and safely destroys PFAS without by-products, contradicting the evidence.
- Linked exact evidence:
  - `NQ27_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=6c0304fb3572efecc6732576502566d76a99e08bc372da424fa40510740ada33].
    Supports: Supports that adsorption generates saturated adsorbents that require management via desorption, landfill disposal, or incineration, with notable environmental and economic implications.
  - `NQ27_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=4c6700ec99720303b8cd2ed1b149a61a1b71a45cd761c9e902dde230b91ff084] ;
    Supports: Supports that exhausted GAC can release PFAS, indicating leaching from spent adsorbent and ongoing risk.
  - `NQ27_MMG006`
    > incomplete recovery and generate secondary waste streams containing concentrated PFAS residues (Yadav et al.
    Supports: Supports that safe disposal of exhausted PFAS adsorbents is unresolved and that existing options can generate concentrated PFAS wastes.
  - `NQ27_MMG007`
    > [SOURCE_TEXT_OMITTED sha256=2c986f843019c4f4e45fc1984eab4f387feb545eaf72a4249db8ccc47e0ff227].
    Supports: Supports that incineration must be conducted at very high temperatures to ensure complete PFAS destruction and avoid formation of harmful by-products such as dioxins.
  - `NQ27_MMG008`
    > [SOURCE_TEXT_OMITTED sha256=9f6a983e21cb159345f3d8890a63074c51380fa241478a6a72039049381ee44f]].
    Supports: Supports that although thermal destruction can achieve high PFAS mineralisation in laboratory conditions, there are concerns about scalability, completeness of destruction, and the need to control HF and other fluorinated by-products with advanced flue gas cleaning.
  - `NQ27_MMG010`
    > [SOURCE_TEXT_OMITTED sha256=906d2a62dc3b61cd30110f10e7c03f6950812c1143e824f9e9d8f87e2d7a099b].
    Supports: Supports that spent CFA requires careful disposal or treatment to prevent PFAS leaching into the environment, and that stabilization/solidification in controlled landfills can reduce leaching risk.

#### NQ27-X01

- Component: `NQ27-T01`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: Adsorption of PFAS transfers or concentrates PFAS onto adsorbents and generates contaminant-bound solid wastes; it does not inherently destroy PFAS or eliminate risk, and these spent adsorbents cannot be directly disposed of without further management.
- Full: Use this constraint to ensure the answer does not imply that adsorption destroys PFAS or renders spent adsorbents harmless. The answer should reflect that adsorption results in contaminant-bound adsorbents that require further management and cannot simply be discarded without control.
- Partial: If the answer is otherwise correct but uses ambiguous wording that could be read as implying destruction (e.g., 'eliminates PFAS'), this constraint should trigger downgrading unless the context clearly indicates mere transfer or concentration.
- Contradiction: If the answer explicitly claims that adsorption alone permanently eliminates PFAS risk, destroys PFAS, or makes spent adsorbents harmless and safe for direct disposal, this constraint should be marked as violated.
- Linked exact evidence:
  - `NQ27_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=6c0304fb3572efecc6732576502566d76a99e08bc372da424fa40510740ada33].
    Supports: Supports that saturated adsorbents require management through options such as desorption, landfill disposal, or incineration, rather than simple discharge, and that these options have environmental implications.
  - `NQ27_MMG007`
    > [SOURCE_TEXT_OMITTED sha256=2c986f843019c4f4e45fc1984eab4f387feb545eaf72a4249db8ccc47e0ff227].
    Supports: Supports that achieving complete PFAS destruction requires demanding conditions, indicating that PFAS persists unless it is specifically destroyed under high-temperature treatment.
  - `NQ27_MMG006`
    > incomplete recovery and generate secondary waste streams containing concentrated PFAS residues (Yadav et al.
    Supports: Supports that attempts to manage PFAS-laden adsorbents can leave residual PFAS and create secondary waste streams with concentrated PFAS, so risk persists after adsorption.
  - `NQ27_MMG008`
    > [SOURCE_TEXT_OMITTED sha256=9f6a983e21cb159345f3d8890a63074c51380fa241478a6a72039049381ee44f]].
    Supports: Supports that removal from water via adsorption and subsequent thermal treatment still leaves challenges related to complete destruction and management of by-products.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

Across the cited literature, spent PFAS-loaded adsorbents are managed through several main routes. Operationally, adsorbents are either replaced or regenerated once their PFAS sorption capacity is reached, because "the treatment system will not remain effective unless the spent material is replaced or regenerated" [NQ27_MMG001]. Regeneration is described as a major end-of-life and reuse strategy: reviews note that "the most common end-of-life treatments for adsorption materials are regeneration and recycling of the adsorbent" alongside other options [NQ27_MMG003], and, for PFAS systems, carbon replacement and/or regeneration is highlighted as important "for ensuring the removal of PFAS by GAC" when GAC is exhausted [NQ27_MMG005]. Specific regeneration approaches include high-temperature thermal regeneration/destruction, organic solvent-based regeneration, and chemical regeneration. Thermal regeneration/destruction is characterised by "high PFAS desorption and potential destruction (

90% for long-chain PFASs)" and applicability "to carbonaceous and mineral adsorbents" [NQ27_MMG009]. Organic solvent-based regeneration can achieve "effective desorption (

90% for PFOA/PFOS)" under mild conditions [NQ27_MMG009], while chemical regeneration using salts, pH or ionic strength shifts, or surfactants has "reported recoveries of 60–90% for anion exchange resins and clays" [NQ27_MMG009]. For coal fly ash (CFA) used as a PFAS adsorbent, "thermal or chemical regeneration could restore CFA’s adsorptive capacity, enabling its reuse for PFAS adsorption" [NQ27_MMG010].

When regeneration is difficult or uneconomic, disposal options dominate. Conventional options for saturated adsorbents include "disposal in a landfill, and incineration" along with desorption [NQ27_MMG002], and a broader review similarly lists "incineration with energy recovery, and being sent to landfill" as common end-of-life treatments [NQ27_MMG003]. For PFAS-specific systems, high-temperature incineration and thermal destruction are repeatedly discussed: one study notes that "[SOURCE_TEXT_OMITTED sha256=1b2a8f5c1c2e3e68e1978aaedb86a2095377a37d49d6573deed3858ac06f32d0] (

1000 °C) ... to ensure the complete destruction of PFAS and avert unintentional dioxin generation" [NQ27_MMG007], while another review flags options that "generate secondary waste streams containing concentrated PFAS residues" [NQ27_MMG006], illustrating that disposal choices have substantial environmental implications. For some inorganic adsorbents such as CFA, additional strategies are considered: a "sustainable approach involves stabilizing or solidifying spent CFA, which can immobilize contaminants and reduce the risk of leaching when disposed of in controlled landfills" and "[SOURCE_TEXT_OMITTED sha256=01a8bf5dfc8ffe8abf9b999c78226097fb20ade6279c2ec93a8fb55f207ce490]" [NQ27_MMG010].

The evidence consistently indicates that adsorption does not destroy PFAS but concentrates it in contaminant-bound solids, creating new residual-management challenges. Nighojkar et al. describe how saturated adsorbents must be managed through desorption, landfill disposal, or incineration and that these options have "notable environmental and economic implications" [NQ27_MMG002]. Other reviews emphasise that even after removal from water, further steps such as incineration or other destruction processes are needed, and that these processes can still leave unresolved disposal and by-product issues [NQ27_MMG006, NQ27_MMG008]. Overall, removal of PFAS from water is only one part of the challenge; the PFAS concentrated on solids must still be handled safely.

Residual-management concerns after adsorption and regeneration are multifold. First, regeneration is frequently incomplete. Casella et al. report that PFAS adsorbents "[SOURCE_TEXT_OMITTED sha256=24d6ea8d8c21bdc918d07f8cca8ffe78744ab5199e17ed8ab834b698cc943266]" [NQ27_MMG004]. Operational experience with GAC in wastewater treatment plants shows that if adsorbent is not replaced or adequately regenerated, the media can become a PFAS source: some plant effluents have higher PFAS concentrations than influents because "the GAC has been exhausted and the level of PFAS may indicate chemical leaching" [NQ27_MMG005]. This means that regenerated or exhausted adsorbents continue to carry PFAS and may release it during subsequent use.

Second, regeneration generates additional, often highly contaminated, waste streams. Guo et al. state that some regeneration processes have "incomplete recovery and generate secondary waste streams containing concentrated PFAS residues" [NQ27_MMG006]. The regeneration method summaries further emphasise that organic solvent-based regeneration "produces PFAS-containing solvent waste requiring downstream treatment" and that chemical regeneration "generates brine or surfactant-rich waste streams" and may exhibit "incomplete desorption of strongly bound PFASs" [NQ27_MMG009]. These observations show that regeneration shifts PFAS from solid to liquid or solvent phases, concentrating it and requiring additional treatment technologies.

Third, there is evidence of PFAS release and secondary contamination from exhausted or disposed adsorbents. In wastewater treatment plants, Lei et al. note that some effluents have higher PFAS concentrations than influents because "the GAC has been exhausted and the level of PFAS may indicate chemical leaching" [NQ27_MMG005], illustrating that spent GAC can become a PFAS source rather than a sink. For CFA-based adsorbents, Patel et al. state that they require careful management to prevent leaching, noting that disposal or treatment is needed "to prevent leaching of PFAS or heavy metals into the environment" and proposing stabilization/solidification and controlled landfills to "reduce the risk of leaching" [NQ27_MMG010]. Overall, these findings show that without containment, stabilization, or other controls, PFAS can desorb or leach from spent adsorbents and contaminate surrounding media.

Fourth, safe destruction by thermal treatment is challenging and introduces its own by-product concerns. Bao et al. emphasise that incineration must be conducted "at very high temperatures (

1000 °C) ... to ensure the complete destruction of PFAS and avert unintentional dioxin generation" [NQ27_MMG007]. Andrunik and Smol report that "Thermal destruction, while capable of

95% [SOURCE_TEXT_OMITTED sha256=55d3ae1936306d177e49a73cc4611ee8089b6930810eacfa074bf560c9c1bad1]" [NQ27_MMG008]. The high-temperature regeneration/destruction summary notes risks of "emissions of CO2 and fluorinated gases unless controlled" and describes such approaches as "costly and environmentally intensive" [NQ27_MMG009]. Thus, even for incineration or thermal destruction, residual-management concerns extend beyond the solid phase to air emissions and the need for advanced flue-gas treatment.

Finally, the overall management of exhausted PFAS adsorbents is described as unresolved and constrained by environmental considerations. Guo et al. state that regeneration and disposal options can "generate secondary waste streams containing concentrated PFAS residues" and that "the safe disposal of exhausted adsorbents is unresolved, with options such as high-temperature incineration raising cost and environmental concerns" [NQ27_MMG006]. The suite of options discussed—regeneration, landfill disposal, incineration or thermal destruction, and, for some materials, stabilization/solidification or repurposing—are all accompanied by residual-management concerns such as incomplete PFAS removal, secondary PFAS-rich waste streams, leaching from exhausted or landfilled solids, and challenges associated with by-products and emissions from thermal treatment.

Taken together, the literature portrays adsorption as a transfer and concentration step rather than a final solution: it moves PFAS from water into solid adsorbents, which then require careful regeneration, stabilization, disposal, or destruction. None of the cited sources treat adsorption alone as permanently eliminating PFAS risk or rendering spent adsorbents harmless; instead, they emphasise the need for integrated, downstream management of the PFAS remaining in and released from these materials.

### Unresolved or unsupported boundaries

- The evidence does not comprehensively cover all possible emerging or novel management options for PFAS-loaded adsorbents beyond those listed (e.g., combined destruction–adsorption systems, electrochemical destruction of spent adsorbents).
- There is no detailed quantitative comparison in the provided evidence of life-cycle impacts or cost-benefit analyses between regeneration, landfilling, incineration, and stabilization/repurposing options.
- The evidence does not systematically address management strategies tailored to specific PFAS chemistries or to all types of advanced adsorbent materials (e.g., metal–organic frameworks) beyond general statements.

### Complete approved source chunks

#### NQ27_MMG001

- Role: `required_gold`
- Document: `2026 - Casella - Recent developments in membrane treatment technologies for PFAS removal from surface and groundwater.pdf`
- Chunk: `13`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=f9a80d5672aa7692f49173d7c0569bc1d3494d509aef14e60776a793777f3019]] .

```text
[SOURCE_TEXT_OMITTED sha256=da18c78aed2411a209724d7ca593e0975a48461de4bac6b9def76e09fdcc8a10]
```

#### NQ27_MMG002

- Role: `required_gold`
- Document: `2022 - Nighojkar - Sustainable conversion of saturated adsorbents (SAs) from wastewater into value-added products - future prospects and challenges with toxic per.pdf`
- Chunk: `5`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=79e3fead9afb7255e5a37dc4b67d061c566e2a63cc74c88dcccd1bab3dcd386a].

```text
[SOURCE_TEXT_OMITTED sha256=9c5149ea307bbe71064d46d1a1787d31597a856b2c8e7b9795dfe9ca83e77324]).
```

#### NQ27_MMG003

- Role: `required_gold`
- Document: `2025 - Coutinho - Enhanced removal of low-concentrations of PFOA from water and wastewater with a novel luffa sponge-derived adsorbent - one-step synthesis and.pdf`
- Chunk: `57`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=98c1d7cbb3bcc1fd4f708a6ab811b40291f3c3f181cab9255005e8a6bb400ca9] ].

```text
[SOURCE_TEXT_OMITTED sha256=658ece74a847d2bab159a31c07dda088041b11e548ae30017bce525917f28a39]
```

#### NQ27_MMG004

- Role: `required_gold`
- Document: `2026 - Casella - Recent developments in membrane treatment technologies for PFAS removal from surface and groundwater.pdf`
- Chunk: `13`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=39af40ce5a3e56e7a52f306fe5bea42cfa09480218ba1b7ec5d0efc064aa9e59]] .

```text
[SOURCE_TEXT_OMITTED sha256=da18c78aed2411a209724d7ca593e0975a48461de4bac6b9def76e09fdcc8a10]
```

#### NQ27_MMG005

- Role: `required_gold`
- Document: `2023 - Lei - A review of PFAS adsorption from aqueous solutions - Current approaches, engineering applications, challenges, and opportunities.pdf`
- Chunk: `48`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=4c6700ec99720303b8cd2ed1b149a61a1b71a45cd761c9e902dde230b91ff084] ;

```text
[SOURCE_TEXT_OMITTED sha256=495704ae3ce56c6fbbbc0432e335812514129f3b4e6739ff63c5d5eb55c6ec3b]
```

#### NQ27_MMG006

- Role: `required_gold`
- Document: `2025 - Guo - Adsorption-based removal of PFASs from water mechanisms, materials and future perspective.pdf`
- Chunk: `45`
- Registered exact span: incomplete recovery and generate secondary waste streams containing concentrated PFAS residues (Yadav et al.

```text
[SOURCE_TEXT_OMITTED sha256=4a03bcb167316ab472f78c3d868525e6a83ee23653da86d3a8f3d2245e203a1b].
```

#### NQ27_MMG007

- Role: `required_gold`
- Document: `2019 - Bao - Removal of F-53B as PFOS alternative in chrome plating wastewater by UV - Sulfite reduction.pdf`
- Chunk: `7`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=2c986f843019c4f4e45fc1984eab4f387feb545eaf72a4249db8ccc47e0ff227].

```text
[SOURCE_TEXT_OMITTED sha256=e6404343570b7ecb2d73b5031390961c8a764997efdb7939eae4580f52f95d17]
```

#### NQ27_MMG008

- Role: `required_gold`
- Document: `2025 - Andrunik - Life After Adsorption - Regeneration, Management, and Sustainability of PFAS Adsorbents in Water Treatment.pdf`
- Chunk: `52`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=9f6a983e21cb159345f3d8890a63074c51380fa241478a6a72039049381ee44f]].

```text
[SOURCE_TEXT_OMITTED sha256=ce3f5b10196f63d566f05cbc2ac7653efc73e225d57c6f8262f48cd75d98c95e]].
```

#### NQ27_MMG009

- Role: `optional_gold`
- Document: `2025 - Andrunik - Life After Adsorption - Regeneration, Management, and Sustainability of PFAS Adsorbents in Water Treatment.pdf`
- Chunk: `41`
- Registered exact span: [[SOURCE_TEXT_OMITTED sha256=9305ff52b9932358d20167d56171dbb05984e5a41c8beb0946b35bb3dd1f6e70].

```text
[[SOURCE_TEXT_OMITTED sha256=685ad4eeb6a715ab0ed95a2072f0593400814ed1e6f5370a45f516df21476b82])
```

#### NQ27_MMG010

- Role: `optional_gold`
- Document: `2024 - Patel - Adsorption capacity and mechanism of modified coal fly ash (CFA) for per- and polyfluoroalkyl substances (PFAS) in landfill leachate.pdf`
- Chunk: `46`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=906d2a62dc3b61cd30110f10e7c03f6950812c1143e824f9e9d8f87e2d7a099b].

```text
[SOURCE_TEXT_OMITTED sha256=9ad259cd5cb9bb7c9c18a7d39c5004ec4f235af7c7d4ba9e322ce1a8727cbd02].
```

### Deterministic resolution

- {'claim_group_id': 'NQ27-G02', 'evidence_id': 'NQ27_MMG002', 'action': 'restored_original_chunk_whitespace', 'old_span_sha256': '1efb0a7cbeb9168cb50201b7e5a3d68ca7a9f68c981d17dea169c5fab9472a79', 'new_span_sha256': '7f42f54ec20595b5a0b641515b2113dc7e36c6b387a9e3588eac0530519488ee'}
- {'claim_group_id': 'NQ27-G04', 'evidence_id': 'NQ27_MMG002', 'action': 'restored_original_chunk_whitespace', 'old_span_sha256': '1efb0a7cbeb9168cb50201b7e5a3d68ca7a9f68c981d17dea169c5fab9472a79', 'new_span_sha256': '7f42f54ec20595b5a0b641515b2113dc7e36c6b387a9e3588eac0530519488ee'}
- {'claim_group_id': 'NQ27-X01', 'evidence_id': 'NQ27_MMG002', 'action': 'restored_original_chunk_whitespace', 'old_span_sha256': '1efb0a7cbeb9168cb50201b7e5a3d68ca7a9f68c981d17dea169c5fab9472a79', 'new_span_sha256': '7f42f54ec20595b5a0b641515b2113dc7e36c6b387a9e3588eac0530519488ee'}

---

## NQ28

**Question:** How do advanced oxidation and advanced reduction pathways compare for PFAS treatment, and what factors limit direct comparison of their efficiency?

### Task components

- `NQ28-T01`: Describe and distinguish the mechanisms and pathways of advanced oxidation versus advanced reduction for PFAS treatment, including typical reactive species, main reaction steps, and characteristic intermediates for each approach.
- `NQ28-T02`: Compare the treatment outcomes of advanced oxidation and advanced reduction for PFAS in terms of defluorination, mineralization, and other relevant endpoints or limits (e.g., partial breakdown, transformation products), without claiming that either approach is universally more efficient for all PFAS compounds or endpoints.
- `NQ28-T03`: Explain the key factors that limit direct comparison of the efficiency of advanced oxidation and advanced reduction pathways for PFAS (such as differences in PFAS structures, operating conditions, metrics/endpoints used, and observed intermediates or pathways) and how these factors affect interpretation of comparative performance.

### Normative claim groups

#### NQ28-G01

- Component: `NQ28-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Advanced oxidation processes for PFAS typically rely on oxidizing radicals such as hydroxyl and sulfate radicals, whereas advanced reduction processes rely on reductive species such as hydrated electrons, leading to different reaction modes for PFAS degradation.
- Full: Award full credit if the answer notes that advanced oxidation for PFAS uses oxidizing radical species such as hydroxyl radicals and sulfate radicals, while advanced reduction uses reductive species, particularly hydrated electrons, and clearly distinguishes these as different underlying mechanisms for PFAS degradation.
- Partial: Award partial credit if the answer mentions that oxidation and reduction treatments use different radical or electron species for PFAS degradation but does not clearly identify or distinguish hydroxyl/sulfate radicals from hydrated electrons, or if it only states that oxidation and reduction are different without specifying the reactive species.
- Contradiction: Mark as contradiction if the answer claims that advanced oxidation and advanced reduction rely on the same main reactive species, or mislabels hydrated electrons as oxidation agents or hydroxyl/sulfate radicals as reduction agents in the PFAS context.
- Linked exact evidence:
  - `NQ28_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=32af73564b5183c710a8294d78b6d71f984491e37c64b2c88292d34436869cf3]] .
    Supports: Identifies advanced oxidation processes (AOPs) and advanced reduction processes (ARPs) as distinct treatment categories for PFAS in water.
  - `NQ28_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=99b0b4f191daedfa85080841366f2835f7c941b2b9568b9fd0ac0385eb96547f]] .
    Supports: Shows that hydrated electrons are distinguished from hydroxyl and sulfate radicals as different reactive species involved in PFAS treatment.

#### NQ28-G02

- Component: `NQ28-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Ultraviolet-advanced reduction processes generate hydrated electrons and other reductive species that nonselectively convert long- and short-chain PFAS to nonfluorinated products, and hydrated electron-based ARPs are considered among the most effective techniques for degrading PFAS.
- Full: Award full credit if the answer explains that ultraviolet-assisted advanced reduction processes generate hydrated electrons and related reductive species, that these species are described as particularly effective at eliminating PFAS (both long- and short-chain), and that these processes convert PFAS to nonfluorinated products.
- Partial: Award partial credit if the answer mentions that UV-ARPs or hydrated electrons are effective for PFAS destruction but omits that they convert PFAS to nonfluorinated products, or if it mentions nonselective conversion to nonfluorinated products without clearly tying this to hydrated electrons or UV-ARPs.
- Contradiction: Mark as contradiction if the answer asserts that UV-ARPs or hydrated electron-based ARPs are generally ineffective for PFAS degradation, or that they do not lead to nonfluorinated products, in opposition to the cited descriptions.
- Linked exact evidence:
  - `NQ28_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=ff72bdb61c65af62af4391d329f2bceff12d4814b173bc404b03880887d9c9bd].
    Supports: States that hydrated electron-based advanced reduction processes are considered among the most effective techniques for degrading PFAS.
  - `NQ28_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=99b0b4f191daedfa85080841366f2835f7c941b2b9568b9fd0ac0385eb96547f]] .
    Supports: Provides specific support that hydrated electrons are more effective for PFAS elimination than hydroxyl or sulfate radicals, reinforcing the effectiveness of ARPs.
  - `NQ28_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=f4379241d2cd5f57c3abe67a924379b395ce7b8626aaa5e91e8603b9a3617d3a]
    Supports: Indicates that UV-ARPs generate reductive species that nonselectively convert long- and short-chain PFAS to nonfluorinated products.
  - `NQ28_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=eb1b5dcbf79e01b52b38a2f94ddae5adefae9133e005ba5cd2ec1d0735670cbd].
    Supports: Adds that UV-ARPs can be low-energy and use hydrated electron sensitizers with UV lamps, providing additional characterization of UV-ARP mechanisms and operation.

#### NQ28-G03

- Component: `NQ28-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Advanced oxidation treatments for PFAS, including hydroxyl- and sulfate-radical-based AOPs and electrochemical oxidation, show variable performance: some AOPs can be slow or inefficient and may even result in PFAS levels above drinking water standards, while electrochemical oxidation generally outperforms several other AOPs but is constrained by energy use, electrode cost, and by-products.
- Full: Award full credit if the answer states that advanced oxidation processes for PFAS can be slow or inefficient and may even increase PFAS levels above drinking water standards, and also notes that electrochemical oxidation has generally performed better than several other oxidation-based methods (e.g., Fenton, photochemical oxidation, ozonation, activated persulfate) for PFAS removal but is limited by energy consumption, electrode cost, and by-products.
- Partial: Award partial credit if the answer mentions only that some AOPs can be ineffective or slow, or only that electrochemical oxidation often performs better than other AOPs without mentioning its limitations, or if it broadly notes variability in AOP performance without specifying electrochemical oxidation.
- Contradiction: Mark as contradiction if the answer claims that all oxidation treatments for PFAS are consistently fast and efficient, or that electrochemical oxidation does not have notable limitations related to energy, electrode cost, or by-product formation, contradicting the cited review.
- Linked exact evidence:
  - `NQ28_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=8539acda21d81e13f1fb9249b39b4413780006a84e0d44bbc47a350cfdd03b02]] .
    Supports: States that oxidation treatments are generally slow and inefficient for PFAS, framing limitations of AOPs.
  - `NQ28_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=f7f35a989a065030bdf38dc17cfd8ba4a2e1c7c018495ce50786639e38b2dc04]] .
    Supports: Indicates that AOPs can be ineffective to the point that PFAS levels rise above drinking water standards after treatment.
  - `NQ28_MMG003` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=2388badf1c754056c6cd717dc273b0f06432fcb66403936f06c29ca619160831].
    Supports: Shows that electrochemical oxidation outperformed several other oxidation-based processes for PFAS removal under the conditions reviewed.
  - `NQ28_MMG003` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=fdf11f6b55bc2501238469f6f8850e16d633181055ac060f901bccb3401d65cf].
    Supports: Describes successful elimination of various PFAS by electrochemical oxidation and notes limitations related to energy consumption, electrode cost, and harmful by-products.

#### NQ28-G04

- Component: `NQ28-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In a direct comparison for 35 PFAS, a hydrated electron-based UV/KI–SO3²⁻ advanced reduction process achieved similar or faster degradation rates than an electro-oxidation system, including 1.5 times faster PFOA degradation, but required much higher energy input and had a substantially higher electrical energy per order (EE/O).
- Full: Award full credit if the answer describes that in the cited comparison, the UV/KI–SO3²⁻ advanced reduction process degraded a suite of PFAS, including PFOA, at similar or faster rates than the electro-oxidation system (with PFOA being 1.5 times faster), but required much higher energy input (around an order of magnitude higher input energy density) and showed higher EE/O values than the electro-oxidation system.
- Partial: Award partial credit if the answer mentions either that the UV/KI–SO3²⁻ process had faster PFAS degradation or that it required more energy/EE/O than electro-oxidation, but does not clearly present both aspects (kinetic advantage and energy disadvantage).
- Contradiction: Mark as contradiction if the answer claims that the electro-oxidation system had faster PFAS degradation than the UV/KI–SO3²⁻ process in this study, or that the UV/KI–SO3²⁻ process used less energy or had lower EE/O than electro-oxidation, directly opposing the reported findings.
- Linked exact evidence:
  - `NQ28_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=32c1bfaee5913d6b7d3b7cae8bb9ed3191d91d8e7fba7a180cc674d604e71070].
    Supports: Establishes that a systematic comparison was carried out between an electro-oxidation system and a UV/KI–SO3²⁻ process.
  - `NQ28_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=074c8ab19a792e20d19e8e1bff5b49ec38f894c4f247d2ade28b326e4621bc99]).
    Supports: Shows that for 35 PFAS the UV/KI–SO3²⁻ process had similar or faster degradation than electro-oxidation, and that PFOA degradation was 1.5 times faster in the UV/KI–SO3²⁻ process.
  - `NQ28_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=633ba6df2eacf5471b00e0653395102622317012972975676b46735c44655259]).
    Supports: Indicates that the UV/KI–SO3²⁻ process required an input energy density over an order of magnitude higher than the electro-oxidation system (60 W/L vs ~4.2 W/L).
  - `NQ28_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=c6fb1e8156a2cc82b3d61a3931d132418a91dae5a50ff618e6a60556ee26c2ef].
    Supports: Reports the EE/O values for PFOA degradation: 5.2 kWh·m−3 for electro-oxidation and 48.5 kWh·m−3 for the UV/KI–SO3²⁻ process, indicating much higher energy per order for the reduction process.

#### NQ28-G05

- Component: `NQ28-T03`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: Electrical energy per order (EE/O) is used as a comparative metric for PFAS treatment processes, including advanced oxidation and advanced reduction driven by electrical means such as plasma, but EE/O values are sensitive to water matrix composition and are subject to uncertainty due to challenges in accurate power calculation.
- Full: Award full credit if the answer notes that EE/O is used to compare energy efficiency across PFAS treatment processes (including electrically driven advanced oxidation and reduction) and explains that EE/O is influenced by water matrix composition (e.g., co-contaminants and scavengers) and is subject to uncertainty because of difficulties in accurately calculating discharge power, especially in plasma systems.
- Partial: Award partial credit if the answer mentions EE/O as a comparison metric for PFAS treatment processes but does not clearly discuss its sensitivity to matrix composition or the associated uncertainties, or if it mentions either matrix effects or measurement uncertainties without explicitly tying them to EE/O.
- Contradiction: Mark as contradiction if the answer claims that EE/O is an exact, matrix-independent measure of process efficiency for PFAS treatments or that its calculation is straightforward and not subject to significant uncertainty in plasma or other electrically driven systems.
- Linked exact evidence:
  - `NQ28_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=03114fd65620257685059d0e42754f37c630d107b296aded1644ce5c042518a0].
    Supports: States that the parameter (EE/O) allows direct comparison between this work and other PFAS studies that use electrically driven advanced reduction or oxidation, including plasma methods.
  - `NQ28_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=eb4a92435dfedc8bac6cdb4e6e569b5553c47ad82afcd47a26da5c0ba7a9b320].
    Supports: Shows that EE/O values are higher in groundwater than in deionized water because of co-contaminants and scavengers of plasma-derived reactive species, indicating matrix effects on EE/O.
  - `NQ28_MMG006`
    > [SOURCE_TEXT_OMITTED sha256=5d10c9d388afe4a73bbf7fa47a11e33a8ae5185618d98e972e0ab8a9a4393f17].
    Supports: Identifies a challenge in calculating EE/O for plasma-based systems: difficulty interpreting waveforms due to reflected power and nonphysical voltage structures.
  - `NQ28_MMG006`
    > [SOURCE_TEXT_OMITTED sha256=0ff7dddc86f2b518b1785a0ae6f695defdeca66a66032d1dcee41a036b60d7ae].
    Supports: Explains that uncertainty in the power supply behavior leads to uncertainty in discharge power calculation and EE/O estimation.

#### NQ28-G06

- Component: `NQ28-T03`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Multiple reaction and system variables—including initial PFAS content, operational factors, water matrix composition, and differences in energy input and EE/O—complicate direct comparison of advanced oxidation and advanced reduction efficiency for PFAS.
- Full: Award full credit if the answer states that comparison of advanced oxidation and advanced reduction efficiencies for PFAS is limited by differences in initial PFAS concentrations and other operational factors, by water matrix composition and scavengers, and by differences and uncertainties in energy input and EE/O, and if it explains that these factors hinder straightforward or universal performance rankings.
- Partial: Award partial credit if the answer mentions at least one major limiting factor (e.g., variation in operating conditions, matrix composition, or energy/EE/O differences) that complicates comparison of AOPs and ARPs for PFAS, but does not integrate multiple factors or clearly connect them to the difficulty of direct comparison.
- Contradiction: Mark as contradiction if the answer asserts that advanced oxidation and advanced reduction efficiencies for PFAS can be directly and universally compared without regard to differences in conditions, matrices, or energy use, or that such variables do not materially affect comparative interpretation.
- Linked exact evidence:
  - `NQ28_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=c071116418c00f8355a91ca23f11dbb2eae265af5687438ff4a1c8b03671edac].
    Supports: Shows that PFAS abatement effectiveness varies with initial PFAS content and operational factors.
  - `NQ28_MMG003`
    > Because of these variables, comparing the competence of each method is difficult.
    Supports: Explicitly states that these variables make it difficult to compare the competence of different methods.
  - `NQ28_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=eb4a92435dfedc8bac6cdb4e6e569b5553c47ad82afcd47a26da5c0ba7a9b320].
    Supports: Indicates that co-contaminants and scavengers in groundwater increase EE/O compared to deionized water, highlighting matrix effects on energy efficiency metrics.
  - `NQ28_MMG006`
    > [SOURCE_TEXT_OMITTED sha256=0ff7dddc86f2b518b1785a0ae6f695defdeca66a66032d1dcee41a036b60d7ae].
    Supports: Shows that there is uncertainty in EE/O estimation due to power calculation issues, complicating comparative use of EE/O.
  - `NQ28_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=633ba6df2eacf5471b00e0653395102622317012972975676b46735c44655259]).
    Supports: Illustrates that compared processes (UV/KI–SO3²⁻ ARP vs electro-oxidation) can operate at very different energy inputs, which affects efficiency comparison.

#### NQ28-X01

- Component: `NQ28-T02`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: Because PFAS abatement effectiveness varies with reaction variables and conditions, the literature cautions that comparing the competence of different PFAS treatment methods is difficult, which constrains drawing universal efficiency rankings between advanced oxidation and advanced reduction.
- Full: Use this constraint to reject answers that claim advanced oxidation or advanced reduction is universally more efficient for all PFAS or under all conditions, because the cited review explicitly states that effectiveness varies with reaction variables and that comparing method competence is difficult.
- Partial: If an answer suggests general trends (e.g., that certain ARPs can outperform some AOPs in specific cases) while acknowledging dependence on conditions or PFAS types, do not treat this as violating the constraint.
- Contradiction: This constraint is contradicted if an answer explicitly asserts universal superiority of advanced oxidation or advanced reduction for PFAS treatment without qualification or acknowledgment of variable conditions.
- Linked exact evidence:
  - `NQ28_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=c071116418c00f8355a91ca23f11dbb2eae265af5687438ff4a1c8b03671edac].
    Supports: Provides the basis that PFAS abatement effectiveness varies with multiple reaction variables, undermining universal performance claims.
  - `NQ28_MMG003`
    > Because of these variables, comparing the competence of each method is difficult.
    Supports: Explicitly notes that comparing the competence of each method is difficult, cautioning against straightforward universal rankings.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

Across the available evidence, advanced oxidation processes (AOPs) and advanced reduction processes (ARPs) for PFAS treatment are treated as distinct classes of technologies that rely on different reactive species and reaction modes in aqueous systems.

For mechanisms and pathways, the literature explicitly notes that advanced oxidation and advanced reduction use different key species. AOPs are associated with oxidizing radicals such as the hydroxyl radical (•OH) and the sulfate radical (SO4•−), whereas ARPs are characterized by reductive species, especially hydrated electrons (eaq−). One review discussing PFAS treatments states that advanced oxidation processes and advanced reduction processes "have shown promise in degrading PFAS in the aqueous environment" and further contrasts "eaq− (hydrated electron)" with "hydroxyl radical (•OH)" and "sulfate radical (SO4•−)," noting that the hydrated electron is more effective in eliminating PFAS than these oxidizing radicals. Another review focused on advanced oxidation processes for PFAS describes hydroxyl- and sulphate-radical-based AOPs, providing context that these radical species underpin many oxidation pathways for PFAS.

On the reduction side, hydrated electron-based ARPs are repeatedly highlighted. In one electro-oxidation study, the authors remark that "[SOURCE_TEXT_OMITTED sha256=55ba44ed690ba0164e90da74f319312e6ca6f798f71d1cf267e84f98f6c64e0b]." A complementary review on ultraviolet-assisted ARPs explains that ultraviolet-advanced reduction processes (UV-ARPs) generate reductive species and that these species "nonselectively convert long- and short-chain PFAS to nonfluorinated" products. The same review notes that UV-ARPs can operate with hydrated electron sensitizers under UV lamps and are presented as low-energy, sustainable options relative to some other AOP/ARP technologies. Taken together, these reports indicate that PFAS oxidation pathways involve attack by oxidizing radicals, while reduction pathways prominently feature hydrated electrons and related reductive species, leading to transformation of PFAS, in the UV-ARP case, into nonfluorinated products. However, beyond this high-level description, the cited texts do not provide detailed stepwise mechanisms or a rich set of intermediates, so only limited mechanistic comparison is possible from the available evidence.

Regarding treatment outcomes and endpoints, the summaries of AOP performance emphasize heterogeneity and limitations. One review notes that "oxidation treatments are generally slow and inefficient" for PFAS, attributing this to the high stability of C–F bonds, and further states that advanced oxidation processes "[SOURCE_TEXT_OMITTED sha256=ae75682be719c3bacb154dc01f305911958aecea0595c8102132b95388d86c3b]." This indicates that for some systems, oxidation may primarily cause partial breakdown or transformation without sufficiently lowering PFAS concentrations, and in some cases apparent PFAS metrics may worsen post-treatment, highlighting limits in practical removal or transformation control under real conditions.

Within the AOP class, electrochemical oxidation is reported to perform relatively well compared with other oxidative approaches. A review of hydroxyl- and sulfate-radical-based processes concludes that, [SOURCE_TEXT_OMITTED sha256=9326e81cc7649fc6488a9c3a2fb422d83ae31f1a5dd772e5f9c9a1c464192289] activated persulphate for PFAS removal on the basis of initial PFAS concentration and reduction extent." Experimental-scale work has shown that PFCA, PFAS, and polyfluorinated compounds can be "successfully eliminated" by electrochemical oxidation, but the same review emphasizes that its wider industrial use is restricted by energy consumption, the expense of producing efficient electrodes, and harmful by-products. These observations indicate substantial PFAS removal and transformation under electrochemical oxidation, but also underscore trade-offs between removal performance and energy or by-product constraints.

In contrast, hydrated electron-based ARPs and UV-ARPs are portrayed as highly effective at degrading PFAS and transforming them into nonfluorinated products. The UV-ARP review notes that UV-assisted advanced reduction generates reductive species that nonselectively convert both long- and short-chain PFAS to nonfluorinated species, implying substantial transformation beyond simple chain shortening or partial oxidation. Although explicit defluorination percentages or full mineralization extents are not reported in the examined excerpts, the language of conversion to nonfluorinated products suggests significant progress toward destruction of the fluorinated backbone, at least under the studied conditions.

A particularly informative comparison comes from a study that directly evaluated an N-GS/CeO2@Ti4O7 membrane-based flow-through electro-oxidation system against a UV/KI–SO3²− process, the latter representing an advanced reduction system generating hydrated electrons. For a set of 35 PFAS, the authors report that the UV/KI–SO3²− process degraded all target PFAS rapidly, "with similar or even much faster degradation rates than the electro-oxidation system," and that for PFOA, the degradation kinetics in the UV/KI–SO3²− process were 1.5 times those in the electro-oxidation system. However, this kinetic advantage came at a substantial energy cost: the input energy density of the UV/KI–SO3²− process was 60 W/L, "over an order of magnitude higher" than the approximately 4.2 W/L used by the electro-oxidation system. The electrical energy per order (EE/O) for PFOA degradation further reflected this difference, with values of 5.2 kWh·m−3 for the electro-oxidation system versus 48.5 kWh·m−3 for the UV/KI–SO3²− process. Thus, in this specific experimental comparison, the advanced reduction pathway provided faster PFAS degradation but at considerably higher energy expenditure per unit contaminant removal.

More generally, energy-based metrics are used to compare PFAS treatment efficiency across processes, including both advanced oxidation and advanced reduction driven by electrical means. A plasma-based PFAS study employs electrical energy per order (EE/O) as a figure of merit and states that "[SOURCE_TEXT_OMITTED sha256=da37abdd1b4dd469782371b4a4ad935ef5fc54a932d29d3b4d0f7635573f4151]." Nonetheless, this same body of work underscores that EE/O is not a simple or universal metric. In groundwater samples treated with a nanosecond pulse plasma, EE/O values for PFOS removal ranged from 93 to 196 kWh/m3 and were higher than for deionized water spiked with PFOA, with the authors attributing the higher EE/O in groundwater to "the presence of multiple co-contaminants and other scavengers of plasma-derived reactive species." Furthermore, they note that for plasma-based systems, "one of the challenges with calculating EE/O" is that the waveforms can be difficult to interpret because of reflected power and nonphysical voltage peaks and oscillations, leading to "uncertainty in the discharge power calculation and thus the EE/O estimation." This illustrates that although EE/O is widely used to compare PFAS treatment efficiency across AOPs and ARPs, matrix effects and instrumental uncertainties limit the precision and generalizability of such comparisons.

Several factors explicitly limit direct comparison of advanced oxidation and advanced reduction efficiency for PFAS. A review of advanced oxidation processes states that the effectiveness of PFAS abatement "differ[s] across multiple reaction variables, including initial PFAS content and other operational factors" and concludes that "because of these variables, comparing the competence of each method is difficult." This variability applies not only within AOP subclasses (e.g., Fenton vs electrochemical oxidation) but also complicates cross-class comparisons to ARPs, because differences in initial PFAS concentrations, reactor configurations, and operational settings influence observed removal and transformation extents. The plasma study adds that water matrix composition strongly affects energy efficiency, with co-contaminants and scavengers in groundwater increasing EE/O compared to deionized water. In addition, the uncertainties in calculating discharge power and EE/O, especially for pulsed plasma systems, make quantitative comparisons less robust.

The direct comparison study between electro-oxidation and the UV/KI–SO3²− ARP further shows that different technologies may be operated at very different energy inputs. The UV/KI–SO3²− process used an input energy density more than an order of magnitude higher than the electro-oxidation system, and its EE/O for PFOA was roughly an order of magnitude higher as well. Such differences in operating conditions and energy intensity complicate any attempt to generalize efficiency rankings across AOP and ARP classes, because performance depends on how each system is configured and optimized.

Taken together, the evidence supports a high-level comparison: advanced oxidation relies primarily on oxidizing radical species such as hydroxyl and sulfate radicals and exhibits variable PFAS abatement performance, with some processes slow or ineffective and others, such as electrochemical oxidation, achieving substantial PFAS removal but with energy and by-product trade-offs. Advanced reduction, particularly hydrated electron-based and UV-assisted ARPs, uses reductive species like hydrated electrons, is portrayed as particularly effective at PFAS degradation, and in specific cases can degrade PFAS faster than electro-oxidation while requiring significantly higher energy input. However, the available excerpts do not provide detailed mechanistic pathways, intermediates, or quantitative defluorination and mineralization outcomes, and they emphasize that performance is highly dependent on reaction variables, matrices, and energy metrics. Consequently, while ARPs and AOPs can be contrasted in terms of their dominant reactive species and some comparative kinetic and energy data, the literature explicitly cautions that differing conditions and metrics make it difficult to draw universal conclusions about which pathway is more efficient for all PFAS or all endpoints.

### Unresolved or unsupported boundaries

- Detailed stepwise mechanisms for PFAS degradation under advanced oxidation (e.g., sequence of radical attacks, specific carbon–fluorine bond cleavage events) are not described in the provided evidence.
- Detailed stepwise mechanisms and characteristic intermediates (e.g., specific partially defluorinated PFAS, short-chain products, inorganic fluoride) for advanced reduction processes, including UV-ARPs, are not provided beyond the statement that PFAS are converted to nonfluorinated products.
- Quantitative defluorination extents and mineralization percentages for AOPs and ARPs, and their direct comparison, are not reported in the cited excerpts.
- Comparative data on a wide range of PFAS structures (e.g., sulfonates vs carboxylates, branched vs linear species, precursors) across multiple AOP and ARP technologies are not available in the provided text.
- Direct evidence on the formation and fate of specific PFAS transformation products other than the general category of 'nonfluorinated' products under ARPs is not present in the supplied evidence.

### Complete approved source chunks

#### NQ28_MMG001

- Role: `required_gold`
- Document: `2025 - Liang - Durable Ti4O7 Heterojunction Composite Membrane Encapsulating N-Doped Graphene Nanosheets for Efficient Electro-Oxidation of GenX and Other PFAS in.pdf`
- Chunk: `37`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=32c1bfaee5913d6b7d3b7cae8bb9ed3191d91d8e7fba7a180cc674d604e71070].

```text
[SOURCE_TEXT_OMITTED sha256=62a873a989de240e6b6835d301b4d8cb0b243e2eebd6740bb8cd2c749585a6a2].
```

#### NQ28_MMG002

- Role: `required_gold`
- Document: `2023 - Mukherjee - Can ultraviolet-assisted advanced reduction processes effectively destroy per- and polyfluoroalkyl substances in real water matrices.pdf`
- Chunk: `5`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=8539acda21d81e13f1fb9249b39b4413780006a84e0d44bbc47a350cfdd03b02]] .

```text
[SOURCE_TEXT_OMITTED sha256=6e2c08d9e6e53f29875050a253d8d4391c02641f09e160d6aac87637bc477150]
```

#### NQ28_MMG003

- Role: `required_gold`
- Document: `2024 - Hajalifard - Per- and polyfluoroalkyl substances degradation using hydroxyl- and sulphate- radical-based advanced.pdf`
- Chunk: `46`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=c071116418c00f8355a91ca23f11dbb2eae265af5687438ff4a1c8b03671edac].

```text
[SOURCE_TEXT_OMITTED sha256=05e755571985167233c2d5b7908fab2d4785851ac2b47bb6e0b11995a6135f61].
```

#### NQ28_MMG004

- Role: `optional_gold`
- Document: `2021 - Groele - An investigation of plasma-driven decomposition of per- and polyfluoroalkyl substances (PFAS) in raw contaminated groundwater.pdf`
- Chunk: `26`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=03114fd65620257685059d0e42754f37c630d107b296aded1644ce5c042518a0].

```text
[SOURCE_TEXT_OMITTED sha256=25179d664126f696071a360c0476374f528e8fc7bea16a13d47c33189d0f1823]
```

#### NQ28_MMG005

- Role: `optional_gold`
- Document: `2021 - Groele - An investigation of plasma-driven decomposition of per- and polyfluoroalkyl substances (PFAS) in raw contaminated groundwater.pdf`
- Chunk: `27`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=eb4a92435dfedc8bac6cdb4e6e569b5553c47ad82afcd47a26da5c0ba7a9b320].

```text
[SOURCE_TEXT_OMITTED sha256=97d41a9edb42fc7331d8b097cc8ac4645f630314252dbee0158647fa621fe103]
```

#### NQ28_MMG006

- Role: `optional_gold`
- Document: `2021 - Groele - An investigation of plasma-driven decomposition of per- and polyfluoroalkyl substances (PFAS) in raw contaminated groundwater.pdf`
- Chunk: `28`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=5d10c9d388afe4a73bbf7fa47a11e33a8ae5185618d98e972e0ab8a9a4393f17].

```text
[SOURCE_TEXT_OMITTED sha256=eaa02808a87b43943ef34a2c4a6d25db9064cbe777e4f6b8999f20d6994fb3a1]
```

### Deterministic resolution

- {'claim_group_id': 'NQ28-G01', 'evidence_id': 'NQ28_MMG002', 'action': 'restored_original_chunk_whitespace', 'old_span_sha256': '32ddd8842db8ec3cf64b946c9451bc0a2f12b0ea06f7e0c928318ba6a88949a7', 'new_span_sha256': '9efeb73435ea7e71b77f9a35d930cca87e33f5c3290f98968461ea92a9b37a3e'}
- {'claim_group_id': 'NQ28-G02', 'evidence_id': 'NQ28_MMG002', 'action': 'restored_original_chunk_whitespace', 'old_span_sha256': '32ddd8842db8ec3cf64b946c9451bc0a2f12b0ea06f7e0c928318ba6a88949a7', 'new_span_sha256': '9efeb73435ea7e71b77f9a35d930cca87e33f5c3290f98968461ea92a9b37a3e'}
- {'claim_group_id': 'NQ28-G02', 'evidence_id': 'NQ28_MMG002', 'action': 'restored_original_chunk_whitespace', 'old_span_sha256': '9134e74b6e2f96bfb9c07e5c45d166aeda22ee8d93ee3d2ee346fdcc8b6b1df8', 'new_span_sha256': '0fb5c90804bbda5c2c07f56e85eb1b30ea936d770c0ffdbb216d469709f57f22'}
- Replaced two misattributed NQ28_MMG001 quotes with its approved energy-density unit span.
- Removed unsupported NQ28_MMG003 linkage from atomic disposition NQ28-A02.

---

## WF10_003

**Question:** What regeneration, elution, and recovery-limit information is needed before calling a PFOA treatment material reusable?

### Task components

- `WF10_003-T01`: Describe the regeneration procedures applied to the PFOA treatment material, including the regeneration steps, regenerant solutions or reagents used, relevant operating conditions (e.g., contact times, sequence of steps), and the matrix and target compounds present during regeneration when reported.
- `WF10_003-T02`: Summarize the elution or desorption behavior of PFOA during regeneration, including what was measured or monitored after regeneration, how much PFOA was eluted or recovered when reported, and any information on the effectiveness or completeness of elution across regeneration cycles.
- `WF10_003-T03`: Summarize the post-regeneration performance of the PFOA treatment material, including any tests of PFOA removal or adsorption capacity after one or more regeneration cycles, the operating conditions and matrix under which these tests were run, and how performance compared to the initial use when reported.
- `WF10_003-T04`: Identify any stated limits or criteria related to reusability, such as the number of regeneration cycles tested, observed performance decline, operational or material constraints, or other reported limitations that qualify whether the material can be considered reusable under the studied conditions.

### Normative claim groups

#### WF10_003-G01

- Component: `WF10_003-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: For CTAB-impregnated activated carbon treating PFOA from aqueous media, regeneration was investigated using a range of organic (methanol, ethanol) and inorganic (NaCl, NaOH, NH4OH, NH4Cl, KCl) regenerants, and an optimized regenerant consisting of 50% ethanol with 1% NH4OH aqueous solution was used; the regeneration procedure included leaching PFOA from the adsorbent and then recovering PFOA and the regenerant from the spent regenerant solution by distillation with controlled heating and pH adjustment.
- Full: Count as fully supported if the answer describes, for at least one PFOA treatment material, the concrete regeneration procedure including: (a) that multiple organic and inorganic regenerants were evaluated; (b) that an optimized regenerant comprising 50% ethanol with 1% NH4OH aqueous solution was used; and (c) that regeneration involved leaching PFOA from the adsorbent followed by a distillation-based recovery of PFOA and regenerant with heating and pH adjustment, as specified in the evidence.
- Partial: Count as partially supported if the answer mentions the use of ethanol/NH4OH or other listed regenerants for regenerating a PFOA sorbent but omits either the optimization aspect (multiple regenerants screened) or the distillation/pH-adjustment conditions used to recover PFOA and regenerant.
- Contradiction: Mark as contradiction if the answer states that regeneration in the Shaikh study did not use organic or inorganic regenerants, or that regeneration did not involve ethanol, NH4OH, or any distillation or pH adjustment steps, or that no effort was made to recover the regenerant or PFOA from the spent regenerant solution.
- Linked exact evidence:
  - `WF10_003_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=c39a076184931139d08f83f3ce28b9955b6e3249288544b61f907bcd66267755]
    Supports: Lists the organic and inorganic regenerants investigated and indicates that both regenerant and PFOA were recovered from the spent regenerant solution.
  - `WF10_003_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=5df63474b372fe5e825e91dc2281144e883370e05348a9553f028222c983af3a].
    Supports: Specifies the optimized regenerant composition (50% ethanol with 1% NH4OH aqueous solution) and the distillation-based recovery procedure with heating and pH adjustment.

#### WF10_003-G02

- Component: `WF10_003-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: For the CTAB-impregnated activated carbon system, PFOA desorption during regeneration was quantified by defining percent regeneration as the mass of PFOA leached from the adsorbent divided by the mass of PFOA loaded, and the optimized regenerant (50% ethanol with 1% NH4OH aqueous solution) achieved around 80–90% PFOA recovery from the sorbent and about 89% PFOA recovery from an exhausted packed-bed column when around 200 bed volumes of regenerant were applied.
- Full: Count as fully supported if the answer states that desorption/elution of PFOA was quantified as percent regeneration (mass leached divided by mass loaded) for CTAB-impregnated activated carbon, and that using a regenerant of 50% ethanol with 1% NH4OH achieved roughly 80–90% PFOA recovery from the sorbent and about 89% recovery from an exhausted column with around 200 bed volumes of regenerant.
- Partial: Count as partially supported if the answer mentions that the optimized ethanol/NH4OH regenerant achieved high (around 80–90%) PFOA recovery, or that approximately 89% recovery was achieved from a column using around 200 bed volumes, but omits the definition of percent regeneration or does not clearly connect these values to elution behavior.
- Contradiction: Mark as contradiction if the answer claims that the ethanol/NH4OH regenerant in the Shaikh study yielded nearly 100% or complete PFOA elution, or that no quantitative PFOA recovery (e.g., 80–90% or 89%) was reported, or that PFOA could not be desorbed under these regeneration conditions.
- Linked exact evidence:
  - `WF10_003_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=8c03ad5c160384729d07c4d2a28e141511db37b61a57e13dd151e8055b046461]
    Supports: Defines how percent regeneration (i.e., PFOA desorption) was quantified.
  - `WF10_003_MMG003` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=f7dbcce763faa2bddf538d990c80328e550f837a871419a683f072e149186500].
    Supports: Indicates the optimized regenerant composition and that it achieved 80–90% PFOA recovery from the sorbent.
  - `WF10_003_MMG004`
    > Around 200-bed volumes of regenerant solution exhibited 89 % PFOA recovery from the exhausted column.
    Supports: Shows the elution behavior in a column configuration: around 200 bed volumes of the regenerant gave 89% PFOA recovery.

#### WF10_003-G03

- Component: `WF10_003-T03`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: For UiO-66 metal–organic frameworks tested with PFOA (and PFOS) at 1 mg/L over five regeneration cycles, regeneration experiments showed that on average UiO-66 maintained effective PFAS removal (about 80% for PFOA) and recovery (about 75% for PFOA), with removal rates staying within 5% of the mean and recovery values within 10% across cycles, indicating stable post-regeneration performance under the studied conditions.
- Full: Count as fully supported if the answer notes that for UiO-66 (and UiO-67) MOFs, regeneration experiments over five cycles at 1 mg/L PFOA/PFOS showed that UiO-66 could effectively remove and recover PFOA and PFOS, with average values around 80% removal and 75% recovery for PFOA and that removal stayed within 5% and recovery within 10% of the mean over the cycles.
- Partial: Count as partially supported if the answer mentions that UiO-66 underwent regeneration over multiple (five) cycles with PFOA/PFOS at 1 mg/L and that removal and recovery remained relatively stable, but omits specific approximate percentages or the stated variability bounds.
- Contradiction: Mark as contradiction if the answer claims that no multi-cycle regeneration or post-regeneration performance testing was done for UiO-66, or that performance degraded severely across cycles rather than staying within a narrow range around the mean.
- Linked exact evidence:
  - `WF10_003_MMG005` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=6258d9f1a5636e60c154818d438d58ad312161bcab84c0f4726b786d36e5d4bd]
    Supports: Shows that five-cycle regeneration experiments were performed on UiO-66 and UiO-67 with PFOA and PFOS at 1 mg/L.
  - `WF10_003_MMG005` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=6d9e21ed441de021cb1e57ac2c89b6424af9bae1c9fa897b2e0e9702ca7a9368]%.
    Supports: Provides the approximate average removal and recovery percentages for PFOA and PFOS on UiO-66 and indicates that both removal and recovery remained stable within 5–10% over five cycles.

#### WF10_003-G04

- Component: `WF10_003-T04`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: A review of PFAS adsorbent regeneration reports that solvent-based and alkaline regeneration of polymeric and carbonaceous adsorbents often achieve high desorption efficiencies for short-chain PFAS (>90%), but for long-chain species such as PFOA and PFOS, desorption efficiencies with methanol, ethanol, and methanol–salt or methanol–NaOH mixtures commonly drop to about 60–80% even over multiple cycles, indicating persistent residual PFOA/PFOS and incomplete elution under these conditions.
- Full: Count as fully supported if the answer explains that, according to the review, methanol, ethanol, and methanol–salt or methanol–NaOH mixtures can consistently achieve >90% desorption for short-chain PFAS but only about 60–80% desorption for PFOA and PFOS over multiple cycles on polymeric and carbonaceous adsorbents, illustrating that incomplete desorption of long-chain PFAS is a typical limitation for reusability.
- Partial: Count as partially supported if the answer notes that long-chain PFAS such as PFOA and PFOS show lower regeneration/desorption efficiencies than short-chain PFAS when using solvent or alkaline regenerants, but does not provide the specific 60–80% versus >90% ranges or does not clearly tie this to implications for reusability.
- Contradiction: Mark as contradiction if the answer claims that solvent and alkaline regenerants routinely achieve near-quantitative or >95–100% desorption of PFOA and PFOS comparable to short-chain PFAS on polymeric and carbonaceous adsorbents, or that there are no meaningful limitations on desorption efficiency for long-chain PFAS.
- Linked exact evidence:
  - `WF10_003_MMG006`
    > [SOURCE_TEXT_OMITTED sha256=609361f4faa891c2e72e6d44e7bde3210540894e1b932502bd3a42c3b9cb564a]].
    Supports: Shows that solvent-based regenerants give >90% desorption for short-chain PFAS but only 60–80% for PFOA and PFOS, indicating incomplete desorption for long-chain PFAS.

#### WF10_003-X01

- Component: `WF10_003-T01`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: The evidence does not provide full procedural details such as exact regeneration contact times, mixing speeds, or the full sequence of all regeneration and reuse cycles for every system; where these are not explicitly stated, they must not be inferred or invented.
- Full: Require this constraint to be respected if the answer avoids adding unreported numerical operating conditions or regeneration sequences (e.g., exact contact times or numbers of bed volumes beyond what is stated) and does not generalize any one study’s protocol to all PFAS treatment materials.
- Partial: If the answer mostly follows the evidence but extrapolates minor procedural details (e.g., implying continuous use beyond the reported five cycles or adding unreported timing), treat as partially respecting the constraint.
- Contradiction: If the answer invents regeneration protocol details or operating conditions not present in any evidence (such as specific temperatures, durations, or numbers of cycles) or presents study-specific findings as universal for all PFAS treatment materials, treat as violating this constraint.
- Linked exact evidence:
  - `WF10_003_MMG005` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=04d8f9ba42d3d9e39b33c3db32365e59250e1009ace166538ac8d70d2c648259])
    Supports: Shows that only five regeneration cycles are explicitly reported for this system; additional cycles are not described in the excerpt.
  - `WF10_003_MMG004`
    > Around 200-bed volumes of regenerant solution exhibited 89 % PFOA recovery from the exhausted column.
    Supports: Provides a specific operating detail (around 200 bed volumes) for one system, emphasizing that similar details for other systems are not given and should not be invented.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

Across the studies provided, several types of information were reported that are relevant to deciding whether a PFOA treatment material can be considered reusable. These include explicit regeneration procedures and regenerant compositions, quantitative measures of PFOA elution or recovery, multi‑cycle performance data, and known limitations on desorption efficiency for PFOA.

For CTAB‑impregnated activated carbon treating PFOA in aqueous media, Shaikh et al. explicitly developed a “[SOURCE_TEXT_OMITTED sha256=e894e09e0502e18328f2526383293f174e9431d1ee4c0e4a81284b097f3c799a].” The study reports that they performed “investigation of regeneration potential of sorbents using organic (methanol and ethanol) and inorganic (NaCl, NaOH, NH4OH, NH4Cl, and KCl) regenerant, (6) recovery of the regenerant and PFOA from the spent regenerant … solution,” indicating that multiple organic and inorganic regenerants were screened. The most effective formulation identified was “50 % ethanol and 1 % NH4OH aqueous solution,” which was then used as the optimized regenerant.

The regeneration procedure for this optimized system involved desorbing PFOA into the regenerant solution followed by recovery of both PFOA and the regenerant. The authors describe that “The PFOA was recovered from the spent regenerant solution (containing 50 % ethanol with 1 % NH4OH aqueous solution) through a distillation process … [SOURCE_TEXT_OMITTED sha256=c35e40114d60902bbbcea7f1343bcaff22439ecc0810ebbf21bc785b8d743b01] NH4+ ions to aqueous NH3 … pH of the spent regenerant was increased up to 11.” The distillation vapors were then condensed and collected, and “[SOURCE_TEXT_OMITTED sha256=6dff03f1d06389d1e6aa57900f3f5d5b198c40f59e875b2781cb6e0f4555bea0].” This provides a clear example of a closed-loop protocol where the regenerant composition, the temperature and pH adjustments, and the subsequent reuse of the regenerant are all documented.

Shaikh et al. also quantified PFOA desorption behavior during regeneration. They defined a metric for elution: “[SOURCE_TEXT_OMITTED sha256=8c03ad5c160384729d07c4d2a28e141511db37b61a57e13dd151e8055b046461].” Using this metric, they compared different regenerants and found that “the most desirable specification of 50 % ethanol and 1 % NH4OH [SOURCE_TEXT_OMITTED sha256=3421390fe5502f5646381e7e13a5d854a96131db1d254c73fe6a9968f26f6bf2].” In a continuous packed‑bed configuration with the same regenerant, they further observed that “Around 200-bed volumes of regenerant solution exhibited 89 % PFOA recovery from the exhausted column.” Together, these results show that regeneration performance was evaluated both in batch contact with PFOA‑loaded sorbent and in a column context, with explicit percent recovery values that fall short of complete desorption but indicate substantial elution of PFOA.

The same article positions this regeneration and recovery work as part of a closed-loop, reusable system: “[SOURCE_TEXT_OMITTED sha256=7fe159f476a109deb07fee84c2adf9f73d2652f3db2314b119b5ec35ebb80bc5].” Therefore, the information needed to claim reusability for this particular material includes: the regenerant formulation (50% ethanol, 1% NH4OH), the operational steps of the regeneration and distillation (heating to about 80 °C and increasing pH to 11 to volatilize ammonia), measured percent regeneration values (80–90% PFOA recovery from batch sorbent, ~89% from the column at ~200 bed volumes), and verification that the recovered regenerant was characterized and reserved for subsequent cycles. While the excerpt confirms reuse of the regenerant in subsequent cycles, the detailed cycle‑by‑cycle performance of the sorbent itself beyond these recovery percentages is not fully given in the provided text.

Hua et al. provide complementary information for metal–organic frameworks (MOFs), focusing on both adsorption and regeneration with PFOA and PFOS in water. They report that “Regeneration experiments ([SOURCE_TEXT_OMITTED sha256=4b000fc997a5e7bebcaca401b7fa5a77961c3b6722962e9cb9ad5a723d84b2ab].” Under these conditions, they found that “[SOURCE_TEXT_OMITTED sha256=386a843da5a77838eac6a28993810b69ff30fd1a1973ef3120e41cfbc611943f] … [SOURCE_TEXT_OMITTED sha256=cbb8974f2bed4c5c87b21a611ab4ecd3f4d67434284fc6eb79ef9d4b3629a10e]%.” Although the exact regenerant solution and procedural details are in the supporting information and not quoted here, the main text demonstrates that post‑regeneration performance was explicitly evaluated over five cycles.

For judging reusability of UiO‑66 under the tested conditions, the key pieces of information provided are: (1) the matrix and target compounds during regeneration tests (aqueous solutions with PFOA and PFOS at 1 mg/L); (2) the number of regeneration cycles (five); (3) average removal and recovery efficiencies for PFOA and PFOS (around 80% removal and 75% recovery for PFOA on UiO‑66); and (4) the stability of these values across cycles (within 5% variability for removal and within 10% for recovery). These data indicate that the MOF can be regenerated and reused multiple times with only modest changes in performance, which is essential information when labeling the material as reusable under the conditions studied.

At a broader level, the review by Andrunik and Smol summarizes typical regeneration outcomes and limitations for PFAS adsorbents, especially polymeric and carbonaceous materials. They note that “[SOURCE_TEXT_OMITTED sha256=dc84ccb3356ad70d9f8a68289fa96dc8bf03ca32086dccd61dcb7c0549f3547b].” This comparison shows that long‑chain PFAS such as PFOA and PFOS are more difficult to desorb than short‑chain PFAS, leading to persistent residual loading even when solvent or solvent–salt/base mixtures are used. The review also states that adding salts or bases “improved the desorption of long-chain PFASs … but rarely matched the near-quantitative recovery seen for short-chain species,” reinforcing that incomplete desorption for PFOA and PFOS is a common limitation.

From the perspective of defining reusability criteria, this review implies that for PFOA treatment materials regenerated with typical alcohol or alkaline solutions, it is necessary to report and consider: (i) the regenerant type and composition (e.g., methanol, ethanol, methanol–NaCl, methanol–NaOH, or alkaline solutions such as NaOH or ammonia); (ii) the desorption efficiency achieved for PFOA (here, on the order of 60–80% under many conditions, substantially lower than for short‑chain PFAS); and (iii) how these efficiencies hold up over multiple cycles. Because PFOA and PFOS are not fully desorbed under many standard regeneration regimes, residual PFAS on the sorbent can accumulate or limit effective capacity, and explicit reporting of desorption percentages and cycle‑to‑cycle retention is required before confidently calling such materials reusable.

Taken together, the evidence indicates that before labeling a PFOA treatment material as reusable, studies should provide: (1) a clear description of the regeneration procedure, including the regenerant composition (e.g., 50% ethanol with 1% NH4OH for CTAB‑impregnated activated carbon, or the regenerant used for MOFs), relevant operating conditions such as temperature and pH where available, and whether batch or column modes are used; (2) quantitative measures of PFOA desorption or recovery (e.g., percent regeneration defined as mass leached over mass loaded, with reported recovery ranges such as 80–90% in the CTAB system or 60–80% in general for PFOA/PFOS with many solvent regenerants); (3) multi‑cycle performance data showing how PFOA removal and recovery change across cycles (as in the UiO‑66 case, where removal and recovery remained within 5–10% of the mean over five cycles); and (4) an explicit discussion of limitations, including the fact that long‑chain PFAS like PFOA may not be completely eluted under common solvent or alkaline regeneration conditions, which constrains the practical reusability of the adsorbent and may necessitate process designs, such as the closed-loop regenerant recovery in the Shaikh study, to manage both sorbent and regenerant reuse.

### Unresolved or unsupported boundaries

- The specific regenerant solution and procedural details (e.g., solvent type, concentration, contact time) used to regenerate UiO-66 and UiO-67 in the Hua study are not included in the provided excerpt; only the existence of regeneration experiments and multi-cycle performance metrics are reported.
- The full number of regeneration cycles, detailed operating conditions, and cycle-by-cycle sorbent performance for the CTAB-impregnated activated carbon system beyond the reported recovery values (80–90% batch recovery and 89% column recovery at ~200 bed volumes) are not specified in the provided text.
- Any universal criteria or thresholds (e.g., a specific minimum number of cycles or exact percent recovery) that must be met before any PFOA treatment material can be called reusable are not defined in the evidence and cannot be inferred beyond the study-specific findings.

### Complete approved source chunks

#### WF10_003_MMG001

- Role: `required_gold`
- Document: `2023 - Shaikh - PFOA remediation from aqueous media using CTAB impregnated activated carbon - A closed-loop sustainable study with comprehensive selectivity analysis.pdf`
- Chunk: `10`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=9abece6f4e85d6a3ff0eb68bbc32d1d3d2fc8cff80101585f80db3f5dff0494d].

```text
[SOURCE_TEXT_OMITTED sha256=edf08b37645de170103053b21a0f87cd0d01f25466cdfcf5a196d13efcd655ef]
```

#### WF10_003_MMG002

- Role: `required_gold`
- Document: `2023 - Shaikh - PFOA remediation from aqueous media using CTAB impregnated activated carbon - A closed-loop sustainable study with comprehensive selectivity analysis.pdf`
- Chunk: `20`
- Registered exact span: ([SOURCE_TEXT_OMITTED sha256=de1bcff37d7ca366945bdce96a9c9478edbcf042fd10e6dd3a42ea3d98fc68d4].

```text
([SOURCE_TEXT_OMITTED sha256=0420261786131e4639ed66e70fb59a8b877aecfa77ea5e99f332a89834c395f0]
```

#### WF10_003_MMG003

- Role: `required_gold`
- Document: `2023 - Shaikh - PFOA remediation from aqueous media using CTAB impregnated activated carbon - A closed-loop sustainable study with comprehensive selectivity analysis.pdf`
- Chunk: `64`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=aeb1cce9b91e4cea4d28e92fff6fe57f8ee8a205883490562f3fce14ed28050e].

```text
[SOURCE_TEXT_OMITTED sha256=eb78c63f2db47bb4800d4709d715eaa781d8430847780c0e969a3c7d8a3e591d] %
```

#### WF10_003_MMG004

- Role: `optional_gold`
- Document: `2023 - Shaikh - PFOA remediation from aqueous media using CTAB impregnated activated carbon - A closed-loop sustainable study with comprehensive selectivity analysis.pdf`
- Chunk: `61`
- Registered exact span: Around 200-bed volumes of regenerant solution exhibited 89 % PFOA recovery from the exhausted column.

```text
[SOURCE_TEXT_OMITTED sha256=56f5ba8b686c7fc60942d7ac2d76692ccd20468a418212be3fd66afa3030c63e].
```

#### WF10_003_MMG005

- Role: `optional_gold`
- Document: `2025 - Hua - Dual-functional metal-organic frameworks for adsorptive removal and ultra-trace quantitation of 50 per- and polyfluoroalkyl substances in water.pdf`
- Chunk: `24`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=bc40a088835aa48278986f42a169baeef887a7e2f0c8c4096ded548980f8fe33] ).

```text
[SOURCE_TEXT_OMITTED sha256=75afede39af7389afcd73ef9ab3fa11bed7c3102bdae9b18bdfd64f929bce46b]%.
```

#### WF10_003_MMG006

- Role: `optional_gold`
- Document: `2025 - Andrunik - Life After Adsorption - Regeneration, Management, and Sustainability of PFAS Adsorbents in Water Treatment.pdf`
- Chunk: `43`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=609361f4faa891c2e72e6d44e7bde3210540894e1b932502bd3a42c3b9cb564a]].

```text
[SOURCE_TEXT_OMITTED sha256=236283c5d67a25bbb02fb7ae25968171a41a60c4f45c8eda22d75e88ff5f179b]].
```

---

## WF10_005

**Question:** When selecting ion-exchange media for broad PFAS removal, how can resin family and contact time affect performance?

### Task components

- `WF10_005-T01`: Extract and compare how different ion-exchange resin families perform for broad PFAS removal, using explicit evidence about the matrix (e.g., type of water or solution tested), the PFAS compounds or classes considered, and the performance endpoints used (e.g., removal extent, breakthrough behavior, or other reported outcomes), including any stated operating constraints and limitations on applicability.
- `WF10_005-T02`: Extract how contact time influences PFAS removal performance for the evaluated ion-exchange resin families, including any explicit evidence on how sufficient versus shorter contact times affect the observed endpoints, and describe any reported operating constraints or limitations related to contact time (such as diminishing returns, practical runtime limits, or matrix-dependent effects) without generalizing findings to universal PFAS treatment claims.

### Normative claim groups

#### WF10_005-G01

- Component: `WF10_005-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In drinking-water experiments with a broad suite of PFAS, polystyrene-divinylbenzene ion-exchange resins removed a larger fraction of PFAS to high levels than polymethacrylate and polyacrylic resins over a 24-hour contact time, indicating strong resin-family effects on broad PFAS removal performance.
- Full: Award full credit if the answer states that in drinking-water experiments with multiple PFAS, polystyrene-divinylbenzene (PS-DVB) ion-exchange resins achieved high removal (>90%) for many or most of the tested PFAS over a 24-hour contact time, while polymethacrylate and polyacrylic resins achieved >90% removal for less than half of the PFAS, explicitly attributing this difference to resin-family or polymer-matrix effects and clearly indicating that the matrix was drinking water and the endpoint was PFAS removal extent.
- Partial: Award partial credit if the answer notes that PS-DVB resins performed better than polymethacrylate and polyacrylic resins for PFAS removal in water, but omits the broad scope of PFAS tested, the 24-hour contact time, or the comparative nature of removal fractions, or if the matrix or endpoint is only implicitly described.
- Contradiction: Mark as contradicting if the answer claims that polymethacrylate or polyacrylic resins achieved equal or greater high-level removal than PS-DVB resins under the described conditions, or denies that resin-family (polymer matrix) affected broad PFAS removal performance in the drinking-water experiments.
- Linked exact evidence:
  - `WF10_005_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=52456c732e74df4a6ce80c0bd258506ea4b7fed16d8f8d8db178fa04cb5519cf].
    Supports: Direct comparison showing that PS-DVB resins achieved >90% removal for all 35 tested PFAS in 24 h, whereas polymethacrylate and polyacrylic resins achieved >90% removal for fewer than half of those PFAS, demonstrating resin-family performance differences and the endpoint of removal extent.
  - `WF10_005_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=52456c732e74df4a6ce80c0bd258506ea4b7fed16d8f8d8db178fa04cb5519cf].
    Supports: Reiterates that under the same experimental conditions, PS-DVB resins achieved >90% removal for all 35 PFAS, while polymethacrylate and polyacrylic resins achieved >90% removal for less than half, underscoring resin-family differences in performance.

#### WF10_005-G02

- Component: `WF10_005-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In drinking-water ion-exchange experiments, increasing contact time beyond about 2 hours reduced the influence of individual PFAS properties on removal and made the resin polymer matrix the dominant factor controlling PFAS removal performance.
- Full: Award full credit if the answer explains that in the drinking-water ion-exchange study, as contact time increased beyond roughly 2 hours, the influence of PFAS-specific properties (such as chain length, charge, and functional groups) on removal decreased and the resin polymer matrix (resin family) became the critical factor determining PFAS removal performance.
- Partial: Award partial credit if the answer notes that longer contact times make resin-family or polymer-matrix effects more important for PFAS removal, but does not explicitly mention the reduction in the impact of PFAS properties or the approximate 2-hour threshold, or if the matrix is not clearly identified as drinking water.
- Contradiction: Mark as contradicting if the answer asserts that at longer contact times PFAS properties remain the dominant factor over the resin polymer matrix in the described experiments, or that contact time did not change the relative importance of PFAS properties versus the resin matrix.
- Linked exact evidence:
  - `WF10_005_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=7920579b579871daecb8dbdb1a1f71ec17d4d95c5f5944f04d86588bbcaf4c21].
    Supports: Shows that although PFAS properties (chain length, charge, functional groups) initially affected adsorption, at contact times >2 h their impact on removal diminished and the resin polymer matrix became the critical factor controlling PFAS removal.
  - `WF10_005_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=7920579b579871daecb8dbdb1a1f71ec17d4d95c5f5944f04d86588bbcaf4c21].
    Supports: Provides the context that these contact-time-dependent effects were observed in experiments treating PFAS in drinking water.

#### WF10_005-G03

- Component: `WF10_005-T01`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: In PFAS-contaminated aqueous solutions, polystyrene divinylbenzene-based ion-exchange resins have been reported to achieve high removal rates for shorter-chain PFAS such as PFBA and PFBS, highlighting resin-family performance for specific PFAS subclasses.
- Full: Award full credit for this supplementary claim if the answer notes that polystyrene divinylbenzene (PS-DVB) based ion-exchange resins have been shown to achieve high removal rates for shorter-chain PFAS such as PFBA or PFBS in PFAS-contaminated water or aqueous solutions.
- Partial: Award partial credit if the answer mentions that PS-DVB resins remove short-chain PFAS effectively but does not name specific examples (PFBA, PFBS) or does not clearly indicate the aqueous/water matrix.
- Contradiction: Mark as contradicting if the answer claims that PS-DVB-based resins perform poorly for short-chain PFAS such as PFBA or PFBS under the conditions described, or explicitly denies that high removal rates were observed.
- Linked exact evidence:
  - `WF10_005_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=57c12f30e11ce182316f4968c18426673bd99a3299e5ba509a6e06791125d292]] .
    Supports: Indicates that PS-DVB-based ion-exchange resins achieved high removal rates for shorter-chain PFAS, specifically PFBA and PFBS, in the discussed aqueous systems.

#### WF10_005-G04

- Component: `WF10_005-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In PFAS-contaminated aqueous solutions treated with polystyrene divinylbenzene-based ion-exchange resins, very prolonged contact times greater than 48 hours have been reported to cause competitive adsorption between long- and short-chain PFAS, displacing short-chain PFAS from resin binding sites and reducing removal efficiency, representing a contact-time-related operating limitation.
- Full: Award full credit if the answer states that in PFAS-contaminated aqueous solutions, PS-DVB-based ion-exchange resins can exhibit competitive adsorption between long- and short-chain PFAS at prolonged contact times greater than 48 hours, where long-chain PFAS displace shorter-chain PFAS from binding sites, leading to reduced removal efficiency, and interprets this as a contact-time-related limitation or operating constraint.
- Partial: Award partial credit if the answer notes that very long contact times can reduce PFAS removal efficiency for PS-DVB resins due to competitive adsorption but does not specify the >48 h timescale or the displacement of short-chain PFAS, or does not clearly indicate that the matrix is an aqueous PFAS-contaminated solution.
- Contradiction: Mark as contradicting if the answer claims that increasing contact time beyond 48 hours always improves or does not affect removal efficiency for PS-DVB resins in PFAS-contaminated aqueous solutions, or denies the occurrence of competitive adsorption or displacement of short-chain PFAS under prolonged contact.
- Linked exact evidence:
  - `WF10_005_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=57c12f30e11ce182316f4968c18426673bd99a3299e5ba509a6e06791125d292]] .
    Supports: Shows that with PS-DVB-based ion-exchange resins, at prolonged contact times (>48 h), competitive adsorption between long- and short-chain PFAS occurs, displacing shorter-chain PFAS from binding sites and reducing removal efficiency.

#### WF10_005-X01

- Component: `WF10_005-T01`
- Importance: `supplementary`
- Scoring role: `constraint_only`
- Proposition: The reported resin-family performance and contact-time effects are specific to the studied ion-exchange resins, PFAS mixtures, and aqueous matrices (drinking water or PFAS-contaminated solutions) and should not be generalized as universal behavior for all PFAS or all ion-exchange systems.
- Full: Use this constraint to discount answers that generalize the observed resin-family and contact-time effects to all PFAS or all ion-exchange systems. Answers must acknowledge, at least implicitly, that the evidence comes from specific resin types, PFAS sets, and aqueous matrices rather than representing universal behavior.
- Partial: If an answer correctly describes the experimental findings but ambiguously suggests broader generality without clearly stating universality, treat it cautiously but do not automatically penalize unless a universal claim is explicit.
- Contradiction: Mark as violating this constraint if the answer explicitly states that the described resin-family differences and contact-time effects apply to all PFAS or all ion-exchange media regardless of matrix or conditions.
- Linked exact evidence:
  - `WF10_005_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=52456c732e74df4a6ce80c0bd258506ea4b7fed16d8f8d8db178fa04cb5519cf].
    Supports: Shows that the comparison is limited to five tested PS-DVB resins and specific polymethacrylate and polyacrylic resins for 35 PFAS compounds, indicating system-specific findings.
  - `WF10_005_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=7920579b579871daecb8dbdb1a1f71ec17d4d95c5f5944f04d86588bbcaf4c21].
    Supports: Indicates that one set of results is specific to drinking water as the matrix.
  - `WF10_005_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=57c12f30e11ce182316f4968c18426673bd99a3299e5ba509a6e06791125d292]] .
    Supports: Indicates that another set of findings concerns PS-DVB-based resins and specific shorter-chain PFAS, again reflecting system-specific behavior.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

In drinking-water ion-exchange experiments targeting a broad suite of PFAS, resin family had a strong effect on removal performance when sufficient contact time was provided. The study "[SOURCE_TEXT_OMITTED sha256=c8e71b4e131d473aba74b8410ec99f2b57070cf6ff6a89c0eac736e5c4bb88a2]" reported that all five tested polystyrene-divinylbenzene (PS-DVB) resins achieved more than 90% removal in 24 hours of 35 PFAS compounds, whereas polymethacrylate and polyacrylic resins achieved greater than 90% removal for less than half of these compounds, indicating higher broad-PFAS removal performance for PS-DVB resins under the tested conditions in drinking water.

Contact time influenced which factors controlled removal. Initially, PFAS properties such as chain length, charge, and functional groups affected adsorption to ion-exchange resins. However, in the same drinking-water experiments, when contact time increased beyond 2 hours, the impact of these PFAS properties on removal became less pronounced and the resin polymer matrix became the critical factor for PFAS removal. Thus, at longer contact times, differences among resin families (e.g., PS-DVB vs polymethacrylate or polyacrylic) played a dominant role in determining removal outcomes for the tested PFAS mixture.

Additional evidence from PFAS-contaminated aqueous solutions shows that PS-DVB-based resins can achieve high removal rates for shorter-chain PFAS such as PFBA and PFBS. However, very prolonged contact times can introduce operating limitations: with PS-DVB-based ion-exchange resins, prolonged contact times greater than 48 hours have been reported to cause competitive adsorption between long- and short-chain PFAS, which displaces shorter-chain PFAS from binding sites on the resin and reduces removal efficiency. This indicates that while longer contact times can be beneficial up to a point—allowing the polymer matrix to control broad PFAS removal—very long contact times may lead to diminished performance for some PFAS subclasses in certain aqueous matrices.

Overall, within the specific drinking-water and PFAS-contaminated aqueous systems studied, PS-DVB ion-exchange resins showed stronger broad PFAS removal than polymethacrylate and polyacrylic resins at 24-hour contact times, and increasing contact time beyond about 2 hours shifted control from PFAS-specific properties to the resin polymer matrix. At the same time, for PS-DVB resins in PFAS-contaminated aqueous solutions, contact times exceeding 48 hours were associated with competitive adsorption effects that reduced removal efficiency for shorter-chain PFAS. These findings are specific to the tested resins, PFAS mixtures, and aqueous matrices and should not be interpreted as universal behavior for all PFAS treatment scenarios.

### Unresolved or unsupported boundaries

- Any quantitative breakthrough behavior, capacity values, or kinetic rates for the different resin families or contact times are not provided in the supplied evidence.
- Details on specific polymethacrylate or polyacrylic resin products, functional groups, or formulations beyond their polymer family are not described in the supplied text.
- The exact composition of the 35 PFAS compounds (e.g., full list of names or structures) is not given in the provided excerpt.
- Matrix effects other than the general description of drinking water or PFAS-contaminated aqueous solutions (such as co-contaminants, ionic strength, or natural organic matter) are not characterized in the supplied evidence.
- Operational constraints such as flow regimes, bed configurations, or scale (bench, pilot, full scale) are not specified in the provided text.

### Complete approved source chunks

#### WF10_005_MMG001

- Role: `required_gold`
- Document: `2021 - Liu - Ion exchange removal and resin regeneration to treat per- and polyfluoroalkyl ether acids and other emerging PFAS in drinking water.pdf`
- Chunk: `1`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=7920579b579871daecb8dbdb1a1f71ec17d4d95c5f5944f04d86588bbcaf4c21].

```text
[SOURCE_TEXT_OMITTED sha256=a7e1dad3f08ff414065cbe930c721f91bc09377a1b6605719d06559fb555c1f8]
```

#### WF10_005_MMG002

- Role: `optional_gold`
- Document: `2023 - Alam - Experimental investigations of Per- and Poly-fluoroalkyl substances (PFAS) degradation by non-thermal plasma in aqueous solutions.pdf`
- Chunk: `25`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=57c12f30e11ce182316f4968c18426673bd99a3299e5ba509a6e06791125d292]] .

```text
[SOURCE_TEXT_OMITTED sha256=c863ecec1753ec98a60fd659fcb8d13ed32ded16745973fba9e2d1f44f893bfd] -
```

---

## WF10_006

**Question:** How can I tell whether a PFAS destruction study has actually addressed what the parent compound turned into?

### Task components

- `WF10_006-T01`: Identify what language, figures, or sections in a PFAS destruction study indicate that the authors explicitly investigated transformation products of the parent compound, including shorter-chain PFAS or other identifiable products, rather than only reporting disappearance of the parent.
- `WF10_006-T02`: Determine how to assess whether a PFAS destruction study evaluated fluorine mass balance (e.g., accounting for inorganic versus organic fluorine and unmeasured fractions) to understand what the parent compound turned into.
- `WF10_006-T03`: Describe how to recognize whether a study looked for or at least discussed the possibility of low–molecular-weight or volatile fluorinated species as transformation products, and how the chosen analytical methods constrain what species could have been detected.
- `WF10_006-T04`: Explain how a reviewer should use reported limitations, uncertainties, and caveats in a PFAS destruction paper—especially around uncharacterized products, incomplete fluorine recovery, and method detection limits—to avoid overclaiming complete destruction or universal PFAS treatment efficacy beyond the specific study conditions.

### Normative claim groups

#### WF10_006-G01

- Component: `WF10_006-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: A PFAS destruction study that explicitly investigates transformation products will often use language about monitoring transformation products and applying suspect or non-target screening, and may report identifiable breakdown products such as short-chain PFCAs and a fluorine mass balance for those products.
- Full: Mark as fully supported if the answer clearly states that reviewers should look for explicit wording about 'transformation products' and the use of suspect or non-target screening, and notes that detection of identifiable breakdown products (such as short-chain PFCAs) combined with a fluorine mass balance for those products indicates that the study has gone beyond simple parent PFAS disappearance.
- Partial: Mark as partially supported if the answer mentions that some studies identify transformation products or short-chain PFAS but does not tie this explicitly to the type of language or analytical framing (e.g., suspect/non-target screening, fluorine mass balance) that signals such investigation.
- Contradiction: Mark as contradictory if the answer implies that disappearance of the parent alone is sufficient to show product characterization, or denies the need for explicit monitoring of transformation products despite quoted evidence emphasizing that need.
- Linked exact evidence:
  - `WF10_006_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=928014e358ed17e740f8339c177d8b931b7f8c72bd0e9d7b7f6d62c0f34bb3fa].
    Supports: States explicitly that transformation products should be monitored during electrochemical oxidation and highlights suspect and non-target screening as the tools used, indicating the kind of language that shows a study is directly addressing transformation products.
  - `WF10_006_MMG008`
    > [SOURCE_TEXT_OMITTED sha256=c262f8982dc8b66138d1092f19b3e7873dec4ee95ea10f7a90504860684cd999].
    Supports: Shows a study explicitly reporting detection of short-chain PFCAs as breakdown products and using a fluorine mass balance to attribute a fraction of the parent fluorine to identified products, indicating detailed investigation of transformation products.

#### WF10_006-G02

- Component: `WF10_006-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Evaluation of fluorine mass balance in PFAS destruction studies is indicated when authors analyze fluoride and measures of adsorbable or organic fluorine, state that their purpose is to complete a fluorine mass balance, and compare increased fluoride to decreased PFAS or AOF, while noting when mineralized fluoride does not equal the decrease in organic fluorine.
- Full: Mark as fully supported if the answer points reviewers to explicit mentions of 'fluorine mass balance' and descriptions of analyzing fluoride together with AOF or organic fluorine, and explains that discussion of mismatches between fluoride increase and organic fluorine decrease signals that the authors assessed what fraction of fluorine was accounted for.
- Partial: Mark as partially supported if the answer mentions fluoride and AOF measurements but does not clearly connect them to an explicit fluorine mass balance objective or to interpreting incomplete closure.
- Contradiction: Mark as contradictory if the answer suggests that any measurement of fluoride alone suffices to establish fluorine mass balance, despite the evidence emphasizing combined fluoride/AOF analysis and explicit mass balance framing.
- Linked exact evidence:
  - `WF10_006_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=ceec181966ff3df3899a702bfa74f2cd9c162b525c9c91b8584656fb3835b4c0]].
    Supports: Shows explicit section heading 'Fluorine Mass Balance', indicates that both fluoride and AOF were analyzed, and states that their purpose was to complete a fluorine mass balance to verify mineralization and check for PFAS byproducts.
  - `WF10_006_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=ceec181966ff3df3899a702bfa74f2cd9c162b525c9c91b8584656fb3835b4c0]].
    Supports: Shows interpretation of mass balance by comparing increasing fluoride to decreasing PFAS/AOF and noting that mineralized fluoride did not equal the total decrease in adsorbable organic fluorine.
  - `WF10_006_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=cbd2b52cb22ac40ac26f1d4462e361f5084a1fcbb63a8d20d4318aa800185992].
    Supports: Links changes in AOF to C–F bond breaking and mineralization, and notes that unchanged or increasing AOF would indicate incomplete destruction or transformation into new PFAS, which is part of interpreting fluorine mass balance.

#### WF10_006-G03

- Component: `WF10_006-T03`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Signals that a study considered low–molecular-weight or volatile fluorinated species include discussion of poor or low fluorine mass balance as an indicator of unmeasured low–molecular-weight or gas-phase products, explicit statements that gaseous products were not analyzed because of analytical challenges, and recommendations to evaluate gas-phase intermediate compounds.
- Full: Mark as fully supported if the answer tells reviewers to look for explicit statements linking poor or low fluorine mass balance to potential low–molecular-weight or gas-phase fluorinated species, mentions that some studies report not analyzing gaseous products due to analytical difficulty, and notes that calls to evaluate gas-phase intermediate compounds indicate awareness of volatile products.
- Partial: Mark as partially supported if the answer mentions low fluorine mass balance or gas-phase compounds but does not clearly tie these to low–molecular-weight/volatile species or to analytical method constraints.
- Contradiction: Mark as contradictory if the answer suggests that low fluorine mass balance can be ignored or that gas-phase/volatile species are irrelevant, contrary to evidence that interprets poor closure as indicating unmeasured volatile/low-MW products and calls for their evaluation.
- Linked exact evidence:
  - `WF10_006_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=9a2a4ca07d83fb8ac32aaabd11ea9dd7e669afe94a2484cf93b3b4b2afab2807].
    Supports: Shows a study explicitly acknowledging that gaseous products were not analyzed because of analytical difficulty and interpreting poor fluorine mass balance as a strong indicator of lower molecular weight fluorinated species that could be off-gassed.
  - `WF10_006_MMG009`
    > [SOURCE_TEXT_OMITTED sha256=7454baf423fad18cf260e97c56d02d9ae340bdcf5a0d679f5d482d4bf97a8285].
    Supports: Links a low fluorine mass balance to the likely existence of fluorinated species in gaseous and/or liquid phases that are not detected by the targeted analytical method, highlighting unmeasured low–molecular-weight or volatile species.
  - `WF10_006_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=8bc6cc57c7ada99acf76bd5588c38bd5275d262afb358051dea7a6ab9b52e48e].
    Supports: Recommends evaluating gas-phase intermediate compounds to fully evaluate fluorine mass balance, indicating that the authors view possible gas-phase intermediates as relevant and currently under-characterized.

#### WF10_006-G04

- Component: `WF10_006-T04`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Reported limitations and caveats in PFAS destruction studies—such as incomplete fluorine mass balance, analytical methods that miss certain byproducts, lack of influent characterization, and unaccounted fractions of fluorine—should be used by reviewers to avoid overclaiming complete destruction or universal treatment effectiveness.
- Full: Mark as fully supported if the answer explicitly advises reviewers to use statements about incomplete fluorine mass balance, analytical detection limits or blind spots, unmeasured gas-phase or low–molecular-weight species, and calls for further byproduct studies as caveats that limit claims of complete destruction or universal PFAS treatment.
- Partial: Mark as partially supported if the answer mentions some limitations (e.g., incomplete mass balance) but does not clearly connect them to avoiding overclaiming complete destruction or broad applicability.
- Contradiction: Mark as contradictory if the answer encourages reviewers to claim complete PFAS destruction or universal applicability despite evidence of incomplete fluorine accounting, analytical limitations, and uncharacterized products.
- Linked exact evidence:
  - `WF10_006_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=ceec181966ff3df3899a702bfa74f2cd9c162b525c9c91b8584656fb3835b4c0]].
    Supports: Shows that even when fluoride increases and PFAS decrease, the mineralized fluoride did not match the loss of organic fluorine, indicating incomplete fluorine accounting that should temper claims of complete mineralization.
  - `WF10_006_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=cbd2b52cb22ac40ac26f1d4462e361f5084a1fcbb63a8d20d4318aa800185992].
    Supports: Identifies specific analytical limitations (AOF not capturing TFA, limited influent sampling) that contribute to incomplete mineralization assessment and limit confidence in the mass balance.
  - `WF10_006_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=928014e358ed17e740f8339c177d8b931b7f8c72bd0e9d7b7f6d62c0f34bb3fa].
    Supports: States that further studies are needed to identify transformation products for novel destructive technologies, which signals that current knowledge of products is incomplete and cautions against overclaiming safety or completeness.
  - `WF10_006_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=8bc6cc57c7ada99acf76bd5588c38bd5275d262afb358051dea7a6ab9b52e48e].
    Supports: Acknowledges that gas-phase intermediates were not yet evaluated and that doing so is necessary to fully evaluate fluorine mass balance, implying that current data do not capture all products.
  - `WF10_006_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=9a2a4ca07d83fb8ac32aaabd11ea9dd7e669afe94a2484cf93b3b4b2afab2807].
    Supports: Shows both an analytical gap (gaseous products not analyzed) and poor fluorine mass balance, indicating that unmeasured low-MW fluorinated species likely exist and limiting confidence in complete PFAS destruction under those conditions.
  - `WF10_006_MMG006`
    > [SOURCE_TEXT_OMITTED sha256=bcb49ab3dad2423d115db09887078da01f294e61e9567dddd88a4f59df4c5575].
    Supports: Explains that the analytical methods cannot detect PFAS whose head groups are altered or that are partially/fully defluorinated, and notes volatilization and adsorption preventing full mass balance closure, pointing to non-quantifiable byproducts that should preclude overconfident destruction claims.
  - `WF10_006_MMG007`
    > [SOURCE_TEXT_OMITTED sha256=5600bb3d1f3cbd0e91480021f9a56d6a4c33345f073921b42651a486f67f5fcf].
    Supports: Shows that targeted compounds accounted for only a fraction of generated fluoride, emphasizes limitations of targeted analysis alone, and explicitly calls for additional investigation of reaction byproducts to fully assess safety and effectiveness.
  - `WF10_006_MMG008`
    > [SOURCE_TEXT_OMITTED sha256=c262f8982dc8b66138d1092f19b3e7873dec4ee95ea10f7a90504860684cd999].
    Supports: Even in a study that identifies a substantial fraction of fluorine, a remaining fraction is attributed to sorption to reactor walls and tubing, underscoring that not all fluorine or products are measured and that conclusions must acknowledge this.
  - `WF10_006_MMG009`
    > [SOURCE_TEXT_OMITTED sha256=7454baf423fad18cf260e97c56d02d9ae340bdcf5a0d679f5d482d4bf97a8285].
    Supports: Shows that absence of intermediates in targeted liquid analysis does not mean they are absent overall, as low mass balance suggests undetected fluorinated species; this cautions against overclaiming based on targeted liquid data alone.
  - `WF10_006_MMG010`
    > [SOURCE_TEXT_OMITTED sha256=e0b452940327df6218b63cd5846ba1fab58d31213912ebf0b7baba76672bf4a0].
    Supports: Acknowledges that the chosen liquid phase analyses provide little information about the fate of key parts of the molecule, indicating that important aspects of product characterization remain unknown and limiting claims about complete mineralization.

#### WF10_006-G05

- Component: `WF10_006-T01`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: Analytical and interpretive statements about transformation products, such as acknowledging that declining AOF reflects C–F bond breaking and that stable or increasing AOF would indicate transformation into new PFAS, help reviewers distinguish between true mineralization and mere formation of other PFAS.
- Full: Mark as fully supported if the answer notes that language interpreting AOF behavior (e.g., decreasing vs. stable or rising) as distinguishing mineralization from transformation into new PFAS is a sign that authors conceptually addressed transformation products rather than only parent removal.
- Partial: Mark as partially supported if AOF is mentioned but without connecting the interpretation of AOF trends to transformation into new PFAS.
- Contradiction: Mark as contradictory if the answer implies that AOF trends are irrelevant to distinguishing mineralization from transformation, despite text that explicitly links them.
- Linked exact evidence:
  - `WF10_006_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=cbd2b52cb22ac40ac26f1d4462e361f5084a1fcbb63a8d20d4318aa800185992].
    Supports: Explains how AOF trends can differentiate between mineralization and incomplete destruction or transformation into new PFAS, providing conceptual language about transformation products.

#### WF10_006-X01

- Component: `WF10_006-T03`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: Targeted liquid-phase analyses and parent-focused methods have important blind spots: they may miss gaseous, low–molecular-weight, altered-head-group, or partially defluorinated species, and poor fluorine mass balance or incomplete product characterization should not be interpreted as proof of complete destruction.
- Full: Use this constraint to prevent answers from implying that targeted liquid-phase analyses or parent disappearance alone guarantee full knowledge of all products or complete destruction, when the evidence clearly states that gaseous, low–molecular-weight, altered-head-group, or partially defluorinated products may be undetected.
- Partial: Consider this constraint partially addressed if the answer hints at analytical limitations but still overstates the reliability of targeted liquid analyses or parent removal as indicators of complete destruction.
- Contradiction: Consider this constraint violated if the answer asserts that targeted LC-MS or fluoride measurements alone are sufficient to rule out problematic byproducts or to claim complete destruction, ignoring stated analytical blind spots.
- Linked exact evidence:
  - `WF10_006_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=9a2a4ca07d83fb8ac32aaabd11ea9dd7e669afe94a2484cf93b3b4b2afab2807].
    Supports: Shows that gaseous fluorinated products were not analyzed because of analytical difficulty, implying that such products could exist but remain undetected.
  - `WF10_006_MMG006`
    > [SOURCE_TEXT_OMITTED sha256=bcb49ab3dad2423d115db09887078da01f294e61e9567dddd88a4f59df4c5575].
    Supports: Indicates that the analytical methods used cannot detect PFAS once their head group is altered or they are defluorinated, leading to non-quantifiable byproducts that limit interpretability of parent disappearance.
  - `WF10_006_MMG007`
    > [SOURCE_TEXT_OMITTED sha256=5600bb3d1f3cbd0e91480021f9a56d6a4c33345f073921b42651a486f67f5fcf].
    Supports: Explicitly states that targeted analysis has limitations and may not capture all PFAS destruction or products.
  - `WF10_006_MMG009`
    > [SOURCE_TEXT_OMITTED sha256=7454baf423fad18cf260e97c56d02d9ae340bdcf5a0d679f5d482d4bf97a8285].
    Supports: Shows that absence of intermediates in targeted liquid LC-QTOF-MS does not rule out fluorinated species elsewhere, emphasizing detection limits of targeted analysis.
  - `WF10_006_MMG010`
    > [SOURCE_TEXT_OMITTED sha256=e0b452940327df6218b63cd5846ba1fab58d31213912ebf0b7baba76672bf4a0].
    Supports: Notes that liquid-phase analyses with fluoride ISE and LC-QTOF-MS provide little information on the fate of important parts of the molecule, reinforcing that these methods alone cannot fully characterize products.

#### WF10_006-X02

- Component: `WF10_006-T02`
- Importance: `supplementary`
- Scoring role: `constraint_only`
- Proposition: Even when fluorine mass balance is attempted, incomplete closure and unaccounted fluorine—such as organic fluorine loss not matching fluoride gain or fluoride associated with untargeted species—mean that the study has not fully determined what all fluorine-containing products are.
- Full: Use this constraint to ensure answers do not equate attempted fluorine mass balance with full product characterization when the cited studies explicitly report incomplete closure or unaccounted fluorine fractions.
- Partial: Consider this constraint partially addressed if the answer acknowledges some incomplete closure but still infers that the fate of all fluorine is essentially known.
- Contradiction: Flag as violating this constraint if the answer implies that mass balance in these studies is fully closed or that all fluorine is accounted for, contrary to explicit statements of mismatch or unaccounted fractions.
- Linked exact evidence:
  - `WF10_006_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=ceec181966ff3df3899a702bfa74f2cd9c162b525c9c91b8584656fb3835b4c0]].
    Supports: Documents a mismatch between organic fluorine loss and fluoride gain, indicating incomplete mass balance closure.
  - `WF10_006_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=cbd2b52cb22ac40ac26f1d4462e361f5084a1fcbb63a8d20d4318aa800185992].
    Supports: Explicitly mentions incomplete mineralization inferred from decoupled fluoride formation and AOF decrease.
  - `WF10_006_MMG007`
    > [SOURCE_TEXT_OMITTED sha256=5600bb3d1f3cbd0e91480021f9a56d6a4c33345f073921b42651a486f67f5fcf].
    Supports: States that only a portion of generated fluoride was associated with targeted compounds, leaving the rest unaccounted and underscoring incomplete closure.
  - `WF10_006_MMG008`
    > [SOURCE_TEXT_OMITTED sha256=c262f8982dc8b66138d1092f19b3e7873dec4ee95ea10f7a90504860684cd999].
    Supports: Shows that even in a detailed mass balance, some fluorine remains unassigned to specific dissolved products and is attributed to sorption, indicating not all products are quantified.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

For a reviewer, the key to telling whether a PFAS destruction study has really addressed what the parent compound turned into is to look for explicit language and data about transformation products and fluorine mass balance, and to pay close attention to the study’s own stated limitations.

1. Evidence that transformation products were explicitly investigated (T01)
A study that goes beyond simple parent disappearance will usually say so directly. One electrochemical oxidation paper states that its [SOURCE_TEXT_OMITTED sha256=6fd28d4189b829c606a90a1b93088a124d6cb91644a601a18324556a92e1f996]" (WF10_006_MMG003). Phrases like “monitor transformation products,” “transformation products were identified,” or mention of “suspect and non-target screening” indicate that the authors are explicitly looking for products rather than just tracking loss of the parent.

Some work also reports specific breakdown products and relates them to a mechanistic picture. In a plasma-based degradation study, the authors report that "[SOURCE_TEXT_OMITTED sha256=bc5422c47822cb018b81da62108608babf356ab2a339a256b7f0e319701f2fdc]" and that "[SOURCE_TEXT_OMITTED sha256=c262f8982dc8b66138d1092f19b3e7873dec4ee95ea10f7a90504860684cd999]" (WF10_006_MMG008). Detection of short-chain PFCAs linked to the parent, together with explicit fluorine accounting for those species, is a clear sign that the study has characterized at least part of the transformation pathway.

Other studies use bulk measures like adsorbable organic fluorine (AOF) to conceptually distinguish mineralization from transformation into new PFAS. In an ultrasonic treatment field demonstration, the authors state that "[SOURCE_TEXT_OMITTED sha256=cbd2b52cb22ac40ac26f1d4462e361f5084a1fcbb63a8d20d4318aa800185992]" (WF10_006_MMG002). This kind of interpretive language shows that the authors have explicitly considered the possibility of new PFAS formation, even if they have not individually identified every product.

In contrast, if a paper only reports disappearance of the parent with no discussion of transformation products, suspect/non-target screening, or bulk organic fluorine behavior, it is likely not fully addressing what the parent turned into.

2. How to recognize fluorine mass balance evaluation (T02)
A strong indicator that a study is trying to account for the fate of the parent compound is an explicit fluorine mass balance section or discussion. In an ultrasonic treatment study, the authors include a section titled “Fluorine Mass Balance” and explain that "Fluoride and AOF were analyzed" and that "[SOURCE_TEXT_OMITTED sha256=0985d4962ffd5f9c2bff9ed5e5eb4a057b66e6a0a68464f54cfe9c7a751831d3]" (WF10_006_MMG001). This type of framing—naming “fluorine mass balance” and stating a goal of verifying mineralization versus byproduct formation—clearly signals that the fate of fluorine is being evaluated.

The same study interprets the data quantitatively, noting that "[SOURCE_TEXT_OMITTED sha256=9be08b4a553ea6a9cfa20bd5049745facecfa33d96e1185b1eda30c70360ed59]" but that "[SOURCE_TEXT_OMITTED sha256=0d67b7ca4039bbef8357a1d27e1632bda5f692535d4f694a05728af79465f0ef]" (WF10_006_MMG001). For a reviewer, this kind of comparison (fluoride produced vs. organic fluorine lost) is a hallmark of fluorine mass balance analysis.

Other work approaches mass balance in a similarly explicit way. In the plasma-based degradation study, the authors state: "[SOURCE_TEXT_OMITTED sha256=c262f8982dc8b66138d1092f19b3e7873dec4ee95ea10f7a90504860684cd999]" (WF10_006_MMG008). They further explain that "The bulk of the remaining ﬂuorine was determined to be sorbed to reactor walls and tubing" (WF10_006_MMG008). This allocation of fluorine across identified species and other sinks (like sorption) is strong evidence that the study is consciously tracking the fluorine budget.

Conversely, some studies show that mass balance is attempted but clearly incomplete. A supercritical water oxidation (SCWO) demonstration reports [SOURCE_TEXT_OMITTED sha256=7d51508659461afc99d69d54e8582f2188606a2fedad7b433ea0974a9c7adbcc]" (WF10_006_MMG007). Here, the explicit mass balance comparison between fluoride generated and targeted PFAS accounted for reveals that the authors know not all fluorine ends up in measured species.

As a reviewer, you should look for:
- Section titles or text explicitly mentioning "fluorine mass balance".
- Concurrent measurement of fluoride and some measure of organic fluorine (such as AOF).
- Statements comparing the change in organic fluorine to the fluoride generated, including mismatches.
- Quantitative statements about what fraction of parent fluorine is accounted for in identified products and what remains unassigned.

When such language is absent and only fluoride or parent PFAS concentrations are reported, the study likely does not fully evaluate what the parent turned into.

3. Recognizing consideration of low–molecular-weight or volatile fluorinated species and method constraints (T03)
Low–molecular-weight and volatile fluorinated species are often missed unless a study explicitly looks for them or at least discusses their possible presence. One SCWO study describes a key limitation: "[SOURCE_TEXT_OMITTED sha256=f2054627a3ba3c16b75a9ad2094ff19b773763d6118f02123764d2002ace21f4]" and then notes that "[SOURCE_TEXT_OMITTED sha256=9a2a4ca07d83fb8ac32aaabd11ea9dd7e669afe94a2484cf93b3b4b2afab2807]" (WF10_006_MMG005). This combination—acknowledging the lack of gas-phase analysis and linking poor mass balance to possible low–molecular-weight, off-gassed species—shows that the authors recognize, but have not captured, volatile products.

Another supercritical water oxidation paper similarly cautions that targeted liquid analysis alone is not sufficient: "[SOURCE_TEXT_OMITTED sha256=0607ba1c3dfec6ff9845a139fc4ff2065222b8aca48e04b366e66677c9fa1205]" (WF10_006_MMG009). The key signal for reviewers is the explicit statement that low fluorine mass balance suggests undetected fluorinated species in gaseous and/or liquid phases, despite the absence of intermediates in the targeted chromatograms.

In the ultrasonic field study, the authors look ahead to this gap by recommending that "[SOURCE_TEXT_OMITTED sha256=2da81eed758da12319a84e3093324969c6303d228a54e17c4f6faa4176ad9c39]" (WF10_006_MMG004). This type of forward-looking statement indicates that the current work does not yet include gas-phase intermediate analysis, and hence does not fully capture all products.

Analytical method descriptions can further reveal what species could or could not have been detected. A gliding arc plasma study notes that "[SOURCE_TEXT_OMITTED sha256=bcb49ab3dad2423d115db09887078da01f294e61e9567dddd88a4f59df4c5575]" (WF10_006_MMG006). The same paper adds that "[SOURCE_TEXT_OMITTED sha256=cd3520b94002fdffada2e077a570363d92c0d6d2c3008350daa2b9a423b56237]" (WF10_006_MMG006). These statements tell a reviewer that altered or partially defluorinated species, as well as volatile or sorbed byproducts, fall outside the method’s detection capability.

Another plasma-based study explicitly discusses information gaps: it states that "[SOURCE_TEXT_OMITTED sha256=e0b452940327df6218b63cd5846ba1fab58d31213912ebf0b7baba76672bf4a0]" (WF10_006_MMG010). Here, the authors acknowledge that even though they measured fluoride and screened with LC-QTOF-MS, they do not know the fate of the carbon backbone or sulfonic acid group.

For reviewers, these kinds of statements are key. They show that:
- Gas-phase or low–molecular-weight species may exist but were not analyzed.
- Targeted liquid LC-MS and fluoride measurements can miss important classes of products (altered-head-group PFAS, partially defluorinated species, volatile fluorocarbons).
- Declining parent PFAS and increasing fluoride alone are not sufficient to rule out formation of other fluorinated species.

4. Using limitations, uncertainties, and caveats to avoid overclaiming (T04)
Most of the cited studies include explicit caveats that should temper claims of complete destruction or universal PFAS treatment. A careful reviewer can use these to avoid over-interpreting the results.

In the ultrasonic field study, despite an explicit fluorine mass balance effort, the authors report that "[SOURCE_TEXT_OMITTED sha256=0d67b7ca4039bbef8357a1d27e1632bda5f692535d4f694a05728af79465f0ef]" (WF10_006_MMG001). They further explain that TFA is not captured by AOF and that [SOURCE_TEXT_OMITTED sha256=7c7e57eb80359ce1897f444c71d2989b000dad1afa89e41f8b5a79435212327c]" and that "[SOURCE_TEXT_OMITTED sha256=b182e9788b2679cf2186dc7a7eddc3dc345445363555681ba73e5129d30a08fb]" (WF10_006_MMG002). These are clear statements that the mass balance is incomplete and influenced by method and sampling limitations, so a reviewer should not interpret the observed destruction as complete mineralization of all PFAS or all fluorine.

Several papers explicitly call for more work on transformation products and byproducts. The electrochemical oxidation study notes that its findings "highlight the need to monitor transformation prod - ucts during EO treatment" and that "Further studies are needed to identify trans - formation products arising in novel destructive treatment technologies" (WF10_006_MMG003). A SCWO review or demonstration adds that "[SOURCE_TEXT_OMITTED sha256=17da67db2e43f8ab6422f5bc15371f66707641ee1c96faf01a3933d92976430d]" (WF10_006_MMG007). The ultrasonic study recommends that "future research should consider evaluating gas- phase intermediate compounds" to "fully evaluate the fluorine mass balance" (WF10_006_MMG004).

Other limitations are explicitly tied to analytical methods. The gliding arc plasma study acknowledges that once PFAS head groups are altered or the molecules are partially/fully defluorinated, they "can no longer be detected by the methods used" and "could form non-quantifiable byproducts" (WF10_006_MMG006). It also notes probable "volatilization and adsorption of the byproducts" that prevent full fluorine mass balance closure (WF10_006_MMG006). Another plasma-based study emphasizes that its "[SOURCE_TEXT_OMITTED sha256=954d5012ff12fd5221957e95572c3be9f990f31a66a31193bd9a112386cdf52f]" (WF10_006_MMG010), directly limiting the conclusions that can be drawn about complete mineralization of the molecule.

Mass balance gaps are another recurring caveat. In the SCWO demonstration, "the targeted compounds accounted for only 27% of the generated fluoride," which "emphasiz[es] the limitations of targeted analysis alone" (WF10_006_MMG007). The plasma-based degradation study notes that even after identifying many products, only 77% and 58% of parent fluorine were identified for PFOA and PFOS, respectively, and that the bulk of the remainder was sorbed to reactor walls and tubing (WF10_006_MMG008). SCWO experiments at certain temperatures report that a "low fluorine mass balance" may indicate undetected fluorinated species in gaseous or liquid products (WF10_006_MMG009).

For a reviewer, these caveats should be used actively:
- When fluorine mass balance is incomplete or unaccounted fractions remain, treat any claims of “complete destruction” or “complete mineralization” with caution.
- When authors state that analytical methods miss altered-head-group, partially defluorinated, gas-phase, or low–molecular-weight products, recognize that transformation products may exist outside the reported analyte list.
- When papers call for further work on transformation products or byproducts, understand that current product characterization is partial, and that hazard or risk from unknown products has not been fully addressed.
- When targeted analysis is acknowledged as limited (e.g., only 27% of generated fluoride associated with targeted PFAS), avoid extrapolating to universal efficacy across PFAS classes or treatment conditions.

In summary, to judge whether a PFAS destruction study has addressed what the parent turned into, a reviewer should look for: explicit discussion of transformation products and their identification (including short-chain PFAS where applicable); a clearly described fluorine mass balance comparing fluoride to organic fluorine; consideration of low–molecular-weight and volatile products and recognition of what analytical methods can and cannot detect; and explicit limitations or future-research statements around uncharacterized products and incomplete mass balance. Where these are missing or where the authors themselves note significant gaps, the study should not be interpreted as demonstrating complete destruction or universal PFAS treatment efficacy beyond the specific conditions and analytes examined.

### Unresolved or unsupported boundaries

- The question asks about language, figures, or sections; the provided evidence contains text discussing fluorine mass balance and transformation products, but does not give detailed examples of specific figure labels, table formats, or section headings beyond the single 'Fluorine Mass Balance' heading, so guidance on figures and other section titles remains incomplete.
- The evidence does not systematically cover how shorter-chain PFAS are treated across multiple destruction technologies; only one plasma-based study explicitly mentions short-chain PFCAs as transformation products, so broader generalization about shorter-chain product monitoring is not supported.
- The corpus excerpts do not provide explicit method detection limits or quantitative thresholds for low–molecular-weight or volatile species, so any detailed guidance on detection limits cannot be derived here.
- No evidence excerpts describe specific numerical criteria for what constitutes an acceptable or 'closed' fluorine mass balance, so such criteria cannot be specified.

### Complete approved source chunks

#### WF10_006_MMG001

- Role: `required_gold`
- Document: `2026 - Juriasingani - Field Demonstration of a High-Frequency Ultrasonic Treatment Reactor for.pdf`
- Chunk: `23`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=ceec181966ff3df3899a702bfa74f2cd9c162b525c9c91b8584656fb3835b4c0]].

```text
[SOURCE_TEXT_OMITTED sha256=bd50cf918919db04447521bb18c33389530f1991f161518f53aa915281b0191a]
```

#### WF10_006_MMG002

- Role: `required_gold`
- Document: `2026 - Juriasingani - Field Demonstration of a High-Frequency Ultrasonic Treatment Reactor for.pdf`
- Chunk: `26`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=cbd2b52cb22ac40ac26f1d4462e361f5084a1fcbb63a8d20d4318aa800185992].

```text
[SOURCE_TEXT_OMITTED sha256=47b7d6f8fa5c0402d3b6d27822e49f3f2d45c9b0bc1510103d18bbc51c20eedf].
```

#### WF10_006_MMG003

- Role: `required_gold`
- Document: `2024 - Rehnstam - Suspect and non-target screening of per- and polyfluoroalkyl substances (PFAS) and other halogenated substances in electrochemically oxidized.pdf`
- Chunk: `44`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=928014e358ed17e740f8339c177d8b931b7f8c72bd0e9d7b7f6d62c0f34bb3fa].

```text
[SOURCE_TEXT_OMITTED sha256=2ca195a8353029b720cb2cc9dbf9805457c7986382d3027fb135e5340319feaf].
```

#### WF10_006_MMG004

- Role: `optional_gold`
- Document: `2026 - Juriasingani - Field Demonstration of a High-Frequency Ultrasonic Treatment Reactor for.pdf`
- Chunk: `36`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=8bc6cc57c7ada99acf76bd5588c38bd5275d262afb358051dea7a6ab9b52e48e].

```text
[SOURCE_TEXT_OMITTED sha256=d0ec67a9e43e5825dcbb6cf92ca615a85a7885c79af6949e73494e9ced2aab18]
```

#### WF10_006_MMG005

- Role: `required_gold`
- Document: `2021 - Pinkard - Destruction of perfluorooctanesulfonate (PFOS) in a batch supercritical water oxidation reactor.pdf`
- Chunk: `19`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=9a2a4ca07d83fb8ac32aaabd11ea9dd7e669afe94a2484cf93b3b4b2afab2807].

```text
[SOURCE_TEXT_OMITTED sha256=bc97eaf749115ec3dbfe1193c9dc7c5f0f8f8d6d0071781705234140ec879cc2]
```

#### WF10_006_MMG006

- Role: `negative_gold`
- Document: `2020 - Lewis - rsc.li - es-water Rapid degradation of PFAS in aqueous solutions by reverse vortex flow gliding arc plasma †.pdf`
- Chunk: `30`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=bcb49ab3dad2423d115db09887078da01f294e61e9567dddd88a4f59df4c5575].

```text
[SOURCE_TEXT_OMITTED sha256=cce8c8a1c9bc32819d29c2a452f220c434a1bc557898e0a5ca34e09c948a6330]
```

#### WF10_006_MMG007

- Role: `negative_gold`
- Document: `2021 - Krause1 - Supercritical Water Oxidation as an Innovative Technology for PFAS Destruction.pdf`
- Chunk: `1`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=5600bb3d1f3cbd0e91480021f9a56d6a4c33345f073921b42651a486f67f5fcf].

```text
[SOURCE_TEXT_OMITTED sha256=b0c20ad2468d1202c2c61683e2f86c55bab0b762343d087f56c24e8408ccc94d].
```

#### WF10_006_MMG008

- Role: `optional_gold`
- Document: `2019 - Singh - Breakdown Products from Perfluorinated Alkyl Substances (PFAS) Degradation in a Plasma-Based Water Treatment Process.pdf`
- Chunk: `1`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=c262f8982dc8b66138d1092f19b3e7873dec4ee95ea10f7a90504860684cd999].

```text
[SOURCE_TEXT_OMITTED sha256=c11c4d71eb97adf06107aed22cf5c7c2864394eeb59d06f89ff1136a9188eec9]
```

#### WF10_006_MMG009

- Role: `optional_gold`
- Document: `2021 - Pinkard - Destruction of perfluorooctanesulfonate (PFOS) in a batch supercritical water oxidation reactor.pdf`
- Chunk: `1`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=7454baf423fad18cf260e97c56d02d9ae340bdcf5a0d679f5d482d4bf97a8285].

```text
◦ [SOURCE_TEXT_OMITTED sha256=b502789e71a89148652df618666375b35188e5d24e958c93d6ca49e12fec4356]
```

#### WF10_006_MMG010

- Role: `optional_gold`
- Document: `2024 - Shaji - Investigating the Effects of Gliding Arc Plasma Discharge’s Thermal Characteristic and Reactive Chemistry on Aqueous PFOS Mineralization.pdf`
- Chunk: `49`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=e0b452940327df6218b63cd5846ba1fab58d31213912ebf0b7baba76672bf4a0].

```text
[SOURCE_TEXT_OMITTED sha256=afe0241c53912f9fc5f2396a59a150bec10f7b60bc1034bace48503347c2d4d3].
```

---

## WF10_007

**Question:** What can radical-scavenger experiments tell me about PFOA degradation chemistry?

### Task components

- `WF10_007-T01`: Describe what radical-scavenger experiments are in the context of PFOA degradation chemistry and what types of radical-related information they are intended to reveal (e.g., which reactive species are involved, relative importance of different radicals, or pathways they suggest) without adding any study-specific details.
- `WF10_007-T02`: Explain how to interpret outcomes of radical-scavenger experiments in PFOA treatment systems, including what patterns in degradation performance with and without scavengers can reasonably be taken as mechanistic evidence about radical involvement, and what cannot be concluded from such results.
- `WF10_007-T03`: Clarify how to separate observed treatment performance (e.g., extent or rate of PFOA removal under certain conditions) from mechanistic evidence provided by radical-scavenger experiments, so that radical-related findings are not overextended into broad claims about overall mineralization or universal PFAS treatment effectiveness.
- `WF10_007-T04`: Outline how a researcher can evaluate whether the reported radical-scavenger evidence in a study supports, is inconclusive for, or fails to support the specific mechanism that is being proposed for PFOA degradation, without introducing new experimental details or generalizing beyond the reported conditions.

### Normative claim groups

#### WF10_007-G01

- Component: `WF10_007-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In PFOA degradation studies, radical-scavenger (quenching) experiments are used by adding specific quenchers to identify which reactive species are involved in degradation and to infer their relative importance.
- Full: Award full credit when the answer explains that in PFOA degradation chemistry, researchers intentionally add radical scavengers/quenchers to degradation systems and then compare PFOA removal with and without these quenchers in order to identify which reactive species (e.g., specific radicals or charge carriers) are active and to gauge their relative contribution. The explanation must be grounded in the notion of quenching or scavenging as shown in the evidence and may reference that different quenchers target different species, but it must not introduce un-evidenced, study-specific experimental details.
- Partial: Award partial credit if the answer mentions radical scavengers or quenching in PFOA degradation but does not clearly state that the main purpose is to infer which species are involved and their importance, or if it does not clearly connect the addition of scavengers to comparing changes in PFOA removal.
- Contradiction: Mark as contradictory if the answer implies that radical-scavenger experiments are not about identifying active species or misrepresents them as primarily measuring unrelated properties (e.g., only toxicity or adsorption) without reference to quenching or scavenging reactive species.
- Linked exact evidence:
  - `WF10_007_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=cd69e0f46c068ee51c738903f2d80fa3df6dbcbb3522ae8590a1a9509b6ebd3c].
    Supports: Shows that authors explicitly conduct quenching experiments using different scavengers to identify which reactive oxygen species are involved in PFOA degradation and to infer which are major contributors based on changes in removal efficiency.
  - `WF10_007_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=cc050ac0ba7434858faffbe93e4628442d16bea202e8dbe75e010ab8d112ef08].
    Supports: Indicates that specific chemicals are added to quench targeted species (•OH and O2−) in order to assess their role in PFOA degradation.
  - `WF10_007_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=8a9a262f1fe4566f289402ed773ff0f07299b5effda6fc1626a1161ea1e5a801].
    Supports: Explicitly states that quenchers are used to determine the active species in PFAS photodegradation, demonstrating the general purpose of radical-scavenger experiments.
  - `WF10_007_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=50f683b7ed9c45449e870ccc97c3a2c3159278cb7080beb87fb1cd06b913244b].
    Supports: Shows that quenching specific species and monitoring the resulting changes in PFOA degradation efficiency is used to understand their role and relative contribution.
  - `WF10_007_MMG002`
    > ([SOURCE_TEXT_OMITTED sha256=3fb3297485931eaed619b25c88848bf953dc7d1614d886f890b6bef45d92d510].
    Supports: Illustrates that changes in PFOA degradation after quenching a given species are interpreted to infer its importance and distinguish between reductive and oxidative pathways.
  - `WF10_007_MMG006`
    > [SOURCE_TEXT_OMITTED sha256=556ee88fb0f209d94a4aa85ae4fd6a2ad5c9f1adb52b33d2b6169503265a2820].
    Supports: Shows that adding a radical scavenger and observing its effect (or lack thereof) on PFAS removal is used to draw mechanistic conclusions, here about the importance of direct electron transfer.

#### WF10_007-G02

- Component: `WF10_007-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: When radical scavengers significantly decrease PFOA degradation or removal, this is taken as evidence that the quenched species contributes to PFOA degradation, whereas negligible changes suggest that the species is not a major contributor under those conditions; however, such patterns do not by themselves establish full mineralization pathways.
- Full: Award full credit when the answer explains that in radical-scavenger experiments for PFOA, a marked reduction in PFOA degradation/removal upon adding a quencher is typically interpreted as evidence that the targeted radical or species contributes substantially to degradation, while little or no change suggests that species is not a dominant contributor under those conditions. The answer should also convey that these observations pertain to degradation or removal of the parent PFOA and do not on their own demonstrate complete mineralization or fully resolve pathways.
- Partial: Award partial credit if the answer notes that changes in performance with quenchers are used to infer radical involvement, but does not clearly differentiate between strong vs negligible effects, or omits the limitation that these data do not directly prove full mineralization pathways.
- Contradiction: Mark as contradictory if the answer claims that any change in performance with a scavenger automatically demonstrates full mineralization or fully proves a detailed reaction mechanism, or if it ignores cases where scavengers have negligible effect yet degradation proceeds by other steps.
- Linked exact evidence:
  - `WF10_007_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=8a9a262f1fe4566f289402ed773ff0f07299b5effda6fc1626a1161ea1e5a801].
    Supports: Shows that authors interpret decreases in PFOA removal upon addition of specific quenchers as indicating that the corresponding species are involved and that large decreases (e.g., with p-BQ or EDTA-2Na) imply more important roles.
  - `WF10_007_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=cd69e0f46c068ee51c738903f2d80fa3df6dbcbb3522ae8590a1a9509b6ebd3c].
    Supports: Provides a clear example where negligible change with one scavenger is interpreted as minimal involvement of that radical, whereas a notable decrease with another scavenger is interpreted as evidence that the corresponding species plays a major role.
  - `WF10_007_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=cc050ac0ba7434858faffbe93e4628442d16bea202e8dbe75e010ab8d112ef08].
    Supports: Shows that marked slowing of PFOA degradation is taken as evidence that the quenched species, here •OH, contributes, while a smaller impairment suggests only a minor contribution from O2−.
  - `WF10_007_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=50f683b7ed9c45449e870ccc97c3a2c3159278cb7080beb87fb1cd06b913244b].
    Supports: Demonstrates that different degrees of decrease in PFOA degradation efficiency upon quenching different species are used to infer their relative contributions, with a larger decrease indicating a dominant role.
  - `WF10_007_MMG002`
    > ([SOURCE_TEXT_OMITTED sha256=3fb3297485931eaed619b25c88848bf953dc7d1614d886f890b6bef45d92d510].
    Supports: Shows interpretation of negligible vs limited vs substantial changes in PFOA degradation upon quenching, where negligible change indicates the species’ direct contribution can be disregarded, and a large decline indicates a primary role.
  - `WF10_007_MMG006`
    > [SOURCE_TEXT_OMITTED sha256=556ee88fb0f209d94a4aa85ae4fd6a2ad5c9f1adb52b33d2b6169503265a2820].
    Supports: Provides an example where adding a radical scavenger does not affect PFAS removal rates, which is interpreted mechanistically as indicating that the rate-limiting step is not controlled by those scavenged radicals.

#### WF10_007-G03

- Component: `WF10_007-T03`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Radical-scavenger experiments provide mechanistic information about which species participate in PFOA degradation and how they interact with matrix components, but these results must be distinguished from overall treatment performance and cannot be generalized to universal mineralization or broad PFAS treatment claims.
- Full: Award full credit when the answer notes that radical-scavenger experiments inform which radicals or charge carriers participate in PFOA degradation, how strongly they contribute, and how they may interact with water matrix components, but also explicitly distinguishes these mechanistic insights from overall treatment performance and warns against extrapolating such findings into broad claims of full mineralization or universal PFAS treatment effectiveness.
- Partial: Award partial credit if the answer mentions that radical scavengers provide mechanistic insights but does not clearly distinguish these from performance metrics or does not explicitly caution against overgeneralizing results.
- Contradiction: Mark as contradictory if the answer treats mechanistic evidence from scavenger tests as sufficient proof of complete mineralization or as directly generalizable to all PFAS or treatment systems without limitation.
- Linked exact evidence:
  - `WF10_007_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=50f683b7ed9c45449e870ccc97c3a2c3159278cb7080beb87fb1cd06b913244b].
    Supports: Shows that scavenger-based mechanistic interpretation goes beyond overall degradation efficiency, identifying dominant and contributing species and their indirect roles via interactions with bulk organics, while also clarifying that ferrate does not directly oxidize PFOA C–F bonds.
  - `WF10_007_MMG002`
    > ([SOURCE_TEXT_OMITTED sha256=3fb3297485931eaed619b25c88848bf953dc7d1614d886f890b6bef45d92d510].
    Supports: Illustrates how changes in degradation with a scavenger are used to infer a dominant reductive defluorination mechanism under the studied conditions, not a universal conclusion about all systems.
  - `WF10_007_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=cc050ac0ba7434858faffbe93e4628442d16bea202e8dbe75e010ab8d112ef08].
    Supports: Indicates that even with scavenger-based evidence suggesting •OH involvement, the precise role in parent PFOA degradation and mineralization remains unclear, underscoring limits of mechanistic inference.
  - `WF10_007_MMG006`
    > [SOURCE_TEXT_OMITTED sha256=556ee88fb0f209d94a4aa85ae4fd6a2ad5c9f1adb52b33d2b6169503265a2820].
    Supports: Shows that lack of effect of a radical scavenger on removal rates supports a mechanism dominated by direct electron transfer while still acknowledging secondary radicals and matrix effects, distinguishing rate-limiting steps from overall performance.
  - `WF10_007_MMG007`
    > ([SOURCE_TEXT_OMITTED sha256=055a757a86e12ecb14b365691b2e9ee01905ffe6df65b8517c53ead274893b3c].
    Supports: Highlights that even when a scavenger changes PFOA degradation (here speeding it up), proposed radical-based explanations may lack direct mechanistic evidence and require further investigation, reinforcing the need to separate observed performance from firmly established mechanisms.
  - `WF10_007_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=8a9a262f1fe4566f289402ed773ff0f07299b5effda6fc1626a1161ea1e5a801].
    Supports: Explicitly states that quenchers are used to determine active species, showing that these experiments aim at mechanistic insight about active species rather than directly measuring overall long-term mineralization or universal performance.

#### WF10_007-G04

- Component: `WF10_007-T04`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: A researcher can evaluate whether radical-scavenger evidence supports or fails to support a proposed PFOA degradation mechanism by checking if changes in degradation upon scavenger addition are consistent with the claimed roles of specific species, considering indirect effects and matrix interactions, and recognizing when attributions lack direct supporting evidence.
- Full: Award full credit when the answer indicates that to judge whether radical-scavenger data support a proposed PFOA degradation mechanism, a researcher should (i) see whether quenching the claimed key species actually changes PFOA degradation in the expected direction and magnitude, (ii) consider alternative or indirect explanations such as matrix organics or secondary radicals, and (iii) recognize cases where mechanisms are hypothesized but direct evidence is acknowledged as lacking.
- Partial: Award partial credit if the answer mentions comparing scavenger effects with proposed mechanisms but does not discuss indirect effects or the need to identify when evidence is explicitly noted as incomplete.
- Contradiction: Mark as contradictory if the answer suggests accepting mechanistic claims from scavenger experiments without checking consistency with the data or ignores explicit statements that proposed mechanisms lack direct evidence.
- Linked exact evidence:
  - `WF10_007_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=50f683b7ed9c45449e870ccc97c3a2c3159278cb7080beb87fb1cd06b913244b].
    Supports: Shows how authors link specific decreases in degradation after quenching to a mechanistic interpretation involving dominant reductive species and indirect roles for •OH and Fe(IV)/Fe(V) through interactions with bulk organics, providing a model for evaluating whether data and proposed mechanism are consistent.
  - `WF10_007_MMG002`
    > ([SOURCE_TEXT_OMITTED sha256=3fb3297485931eaed619b25c88848bf953dc7d1614d886f890b6bef45d92d510].
    Supports: Illustrates using a strong effect of a specific scavenger to support a proposed reductive defluorination mechanism and to rule out alternative pathways as primary routes under those conditions.
  - `WF10_007_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=cc050ac0ba7434858faffbe93e4628442d16bea202e8dbe75e010ab8d112ef08].
    Supports: Shows that although scavenger data indicate •OH involvement, the authors explicitly note that the detailed contribution to parent degradation remains unclear, signaling that mechanism proposals should be treated as incomplete rather than fully proven.
  - `WF10_007_MMG006`
    > [SOURCE_TEXT_OMITTED sha256=556ee88fb0f209d94a4aa85ae4fd6a2ad5c9f1adb52b33d2b6169503265a2820].
    Supports: Provides an example where lack of effect of a radical scavenger is used to support a mechanism dominated by direct electron transfer at the rate-limiting step, while still positing secondary radicals later, illustrating how scavenger data are evaluated against a proposed mechanism.
  - `WF10_007_MMG007`
    > ([SOURCE_TEXT_OMITTED sha256=055a757a86e12ecb14b365691b2e9ee01905ffe6df65b8517c53ead274893b3c].
    Supports: Explicitly states that a proposed mechanism involving nitrate-derived radicals is not directly evidenced, emphasizing the need for a researcher to differentiate between observed effects of a scavenger and speculative mechanistic attributions.
  - `WF10_007_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=cd69e0f46c068ee51c738903f2d80fa3df6dbcbb3522ae8590a1a9509b6ebd3c].
    Supports: Shows how consistent changes (or lack thereof) in PFOA removal with targeted scavengers are used to argue for or against proposed roles of specific species such as •OH and O2−, providing a template for evaluating mechanistic claims.
  - `WF10_007_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=8a9a262f1fe4566f289402ed773ff0f07299b5effda6fc1626a1161ea1e5a801].
    Supports: Reinforces that the stated purpose of using quenchers is to determine active species, which a researcher can use as a criterion to check whether a study’s conclusions logically follow from the scavenger data presented.

#### WF10_007-X01

- Component: `WF10_007-T02`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: Radical-scavenger experiments in PFOA degradation do not automatically provide direct evidence for detailed radical pathways or complete PFOA defluorination, and some proposed radical-based mechanisms are explicitly noted as lacking direct evidence.
- Full: Use this constraint to prevent overclaiming: answers should not treat mechanisms inferred from scavenger-induced changes in PFOA degradation as fully proven when the source explicitly states that direct evidence is lacking. Specifically, when nitrate scavenging is said to speed up PFOA degradation and nitrate-derived radicals are proposed, the lack of direct evidence should be acknowledged, and no claim of fully established radical pathways or complete defluorination should be made on this basis alone.
- Partial: If an answer omits mention of such limitations but does not overstate the certainty of these mechanisms, this constraint is only partially engaged but not violated.
- Contradiction: If an answer presents the nitrate-radical mechanism or similar scavenger-based hypotheses as fully confirmed or as direct evidence of complete PFOA defluorination, it violates this constraint.
- Linked exact evidence:
  - `WF10_007_MMG007`
    > ([SOURCE_TEXT_OMITTED sha256=055a757a86e12ecb14b365691b2e9ee01905ffe6df65b8517c53ead274893b3c].
    Supports: Shows that authors themselves caution that the proposed nitrate and nitrogen dioxide radical mechanism for PFOA defluorination lacks direct evidence and requires further investigation, placing a limitation on how strongly these radical pathways can be claimed.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

Across PFOA and broader PFAS degradation studies, radical‑scavenger (quenching) experiments follow a common logic that can be used to interpret mechanistic claims.

In the context of PFOA degradation chemistry, radical‑scavenger experiments are typically set up by adding compounds that quench specific reactive species (such as hydroxyl radicals, superoxide, hydrated electrons, high‑valent iron species, or photogenerated holes) and then comparing PFOA removal with and without these quenchers. For example, one photocatalytic study states that “the quenching experiment was performed” to “further identify the ROS for PFOA degradation,” using different scavengers and monitoring changes in PFOA removal efficiency to infer which species are involved and which play a “major role” in degradation [WF10_007_MMG003]. Another work notes that [SOURCE_TEXT_OMITTED sha256=bccd061d71d03efc826ddbaa553e941b681c567909a59e28f555dbee357e4688]” of PFOA and PFOS [WF10_007_MMG005]. Similarly, in a plasma–ferrate system, the authors focus on eaq−, •OH, and Fe(IV)/Fe(V), quench each, and then examine how PFOA degradation efficiency changes [WF10_007_MMG001]. In a photocatalyst system, alcohols and superoxide dismutase are “added to quench •OH and O2−” and the effects on PFOA degradation are evaluated [WF10_007_MMG004]. Conversely, an electrochemical oxidation study notes that “the addition of a radical scavenger was shown not to affect PFAS removal rates,” which is interpreted in light of a mechanism dominated by direct electron transfer [WF10_007_MMG006]. Together, these examples show that radical‑scavenger experiments are intended to reveal which reactive species participate in PFOA degradation and how important each is under specific conditions.

Interpreting the outcomes of these experiments relies on the magnitude and direction of the change in PFOA removal when a given species is quenched. When addition of a scavenger causes little or no change in PFOA removal, authors tend to conclude that the targeted species is not a major contributor. In one photocatalytic system, using IPA as a scavenger resulted in an overall PFOA removal efficiency “almost the same as that of the control experiment,” which was interpreted to mean that •OH “was almost not involved in the removal of PFOA” [WF10_007_MMG003]. In the plasma–ferrate system, quenching Fe(IV)/Fe(V) changed PFOA degradation efficiency only slightly (from 91% to 92%), and the authors state that “their direct contribution can be disregarded” [WF10_007_MMG002]. In electrochemical oxidation on BDD electrodes, a radical scavenger “was shown not to affect PFAS removal rates,” which is used to support the idea that direct electron transfer, rather than hydroxyl radicals, controls the rate‑limiting step [WF10_007_MMG006].

By contrast, when quenching a species markedly slows PFOA degradation or substantially decreases its removal efficiency, this is taken as evidence that the species contributes significantly. For example, quenching •OH by IPA “markedly slowed PFOA degradation” in one photocatalytic Bi‑based system, and quenching O2− caused a “measurable impairment,” which the authors interpret as a possible minor contribution from O2− [WF10_007_MMG004]. In another photocatalytic study, adding p‑BQ, a superoxide scavenger, “decreased the removal efficiencies for PFOA and PFOS” substantially and is said to “imply that •O2− is an important free radical in PFAS degradation,” while EDTA‑2Na produced the greatest reduction in PFOA removal and is interpreted as showing that h+ “is of vital importance in PFOA degradation” [WF10_007_MMG005]. In the composite photocatalyst study, the removal efficiency decreased when BQ was used as scavenger, “implying that •O2− played a major role in the degradation of PFOA” [WF10_007_MMG003]. In the plasma–ferrate system, quenching eaq− led to a substantial drop in PFOA degradation efficiency, which “highlight[s] [SOURCE_TEXT_OMITTED sha256=7c6bfc3c364f4576a10c7350c1ff9a336b38361c3be6dddd0077c840209fb78b]” [WF10_007_MMG002]. Collectively, these patterns show how strong inhibition upon quenching is interpreted as evidence for major mechanistic involvement, while negligible inhibition suggests a limited role under the tested conditions.

However, radical‑scavenger experiments primarily give evidence about the involvement and relative contributions of species to degradation of the parent PFOA and about interactions with the water matrix; they do not automatically establish complete mineralization pathways or universal treatment behavior. In the plasma–ferrate case, the scavenger tests show that reductive species “played the dominant role in PFOA removal,” while •OH and Fe(IV)/Fe(V) “also contributed under complex matrix conditions” because bulk organics compete for eaq−, suppressing the reductive defluorination pathway [WF10_007_MMG001]. The authors interpret •OH and Fe(IV)/Fe(V) as pre‑oxidizing competing organics and “indirectly enhancing the availability of reductive species,” and they explicitly state that ferrate “does not act as a direct oxidant for the highly stable C–F bonds in PFOA” [WF10_007_MMG001]. This shows how scavenger evidence can reveal indirect roles and matrix effects without implying that ferrate itself directly cleaves PFOA’s C–F bonds. In another photocatalytic system, quenching‑based evidence indicates that •OH aids PFOA degradation, but the authors acknowledge that “the manner in which •OH contributes to parent compound degradation is not clear at this time,” even though it may aid mineralization and show synergism with photogenerated holes [WF10_007_MMG004]. These statements underscore that scavenger results characterize which species participate and how, rather than fully defining all intermediates, mineralization extents, or universally dominant pathways.

Similarly, the electrochemical oxidation example illustrates that the absence of a scavenger effect can be informative but does not, by itself, prove the absence of radical chemistry at all stages. There, the consensus that “an initial direct electron transfer to the BDD surface is rate‑limiting” is supported both by PFAA insusceptibility to direct hydroxyl radical oxidation and by the observation that a radical scavenger “was shown not to affect PFAS removal rates” [WF10_007_MMG006]. Yet the same passage notes that “secondary radicals are involved in the degradation after the rate‑limiting step” and that high concentrations of radical scavengers “may therefore still prevent effective PFAS degradation in complex matrices” [WF10_007_MMG006]. Thus, scavenger data help locate which step is rate‑limiting and where radicals likely act, but they do not, on their own, prove complete mineralization or exclude later radical processes.

These examples also show how to separate observed treatment performance from mechanistic inference. Changes in PFOA removal percentages (e.g., decreases when particular scavengers are added) are performance observations. Mechanistic conclusions—such as that reductive species dominate, that •O2− is an important free radical, or that h+ is of “vital importance” [WF10_007_MMG002; WF10_007_MMG003; WF10_007_MMG005]—are interpretations of those performance changes. Likewise, in the nitrate‑containing electron beam system, the presence of nitrate, described as “a strong scavenger of eaq−,” is reported to speed up “the degradation of PFOA and its intermediate,” and the authors attribute this to the generation of nitrate and nitrogen dioxide radicals that “may play a role in PFOA defluorination” [WF10_007_MMG007]. Yet they also state that “direct evidence of this mechanism was not presented,” calling for further investigation [WF10_007_MMG007]. This distinction clarifies that while performance data (faster degradation with nitrate present) are solid observations, the radical pathway explanation remains a hypothesis not fully supported by direct mechanistic evidence. A careful reader should therefore avoid turning such mechanistic suggestions into broad claims about complete PFOA defluorination or general PFAS treatment effectiveness.

From these studies, a general approach emerges for evaluating whether radical‑scavenger evidence supports, is inconclusive for, or fails to support a proposed PFOA degradation mechanism. First, compare the proposed key species or pathway with the scavenger data: if a species is claimed to be central, its quenching should, under the reported conditions, measurably affect PFOA degradation in a way consistent with the mechanism, as seen for eaq− in the plasma–ferrate system [WF10_007_MMG001; WF10_007_MMG002] or for h+ in the ChPCN system [WF10_007_MMG005]. If quenching produces only negligible changes, as with Fe(IV)/Fe(V) in one plasma system [WF10_007_MMG002] or IPA in a photocatalytic ZIF67–MIL‑100(Fe)–C3N4 material [WF10_007_MMG003], then claims that those species are primary drivers of PFOA degradation under those specific conditions are not strongly supported by the scavenger evidence. Second, consider indirect and matrix effects: in some systems, radicals contribute indirectly by modifying bulk organics that otherwise compete for key reductive species [WF10_007_MMG001], or secondary radicals may be involved in non‑rate‑limiting steps [WF10_007_MMG006]. Mechanistic claims should be compatible with such effects. Third, weigh the authors’ own caveats: when they explicitly state that the role of a radical is “not clear at this time” [WF10_007_MMG004] or that “direct evidence of this mechanism was not presented” [WF10_007_MMG007], the radical‑scavenger results should be regarded as suggestive, not definitive, and not extrapolated into broad conclusions about full mineralization or universal PFAS treatment.

In summary, radical‑scavenger experiments in PFOA degradation systems are powerful tools for probing which reactive species are involved and for ranking their relative contributions under specified conditions. Marked decreases in PFOA degradation upon quenching a species are commonly interpreted as evidence of its major role, whereas negligible changes suggest a minor or negligible direct contribution. These experiments also reveal indirect roles and matrix effects, such as radicals that pre‑oxidize competing organics or secondary radicals that act after the rate‑limiting step. At the same time, the literature explicitly notes that such scavenger‑based inferences may leave key aspects of the mechanism unresolved and, in some cases, lack direct evidence. For mechanistic assessment, a researcher should therefore treat scavenger data as condition‑specific mechanistic clues tied to observed PFOA removal, rather than as stand‑alone proof of complete mineralization or universally applicable PFAS treatment mechanisms.

### Unresolved or unsupported boundaries

- Any detailed description of radical‑scavenger protocols (such as exact concentrations, reaction times, or instrument settings) beyond what is explicitly quoted in the evidence.
- Quantitative generalizations about mineralization extents, defluorination percentages, or fluoride yields inferred from radical‑scavenger experiments, which are not provided in the supplied text.
- Universal statements that any particular radical or mechanism dominates PFOA degradation across all treatment technologies, water matrices, or PFAS chemistries.
- Mechanistic steps, intermediates, or rate constants not mentioned in the provided excerpts, including detailed reaction pathways for radicals other than those named.

### Complete approved source chunks

#### WF10_007_MMG001

- Role: `required_gold`
- Document: `2026 - Chen - Ferrate-assisted nonthermal plasma for efficient PFOA degradation in landfill leachate - Mitigating bulk organic interference and enhancing.pdf`
- Chunk: `33`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=50f683b7ed9c45449e870ccc97c3a2c3159278cb7080beb87fb1cd06b913244b].

```text
[SOURCE_TEXT_OMITTED sha256=04b768c0125f910099e039562dfad12bb18e809f87030a206cb557d2d8616fca]
```

#### WF10_007_MMG002

- Role: `optional_gold`
- Document: `2026 - Chen - Ferrate-assisted nonthermal plasma for efficient PFOA degradation in landfill leachate - Mitigating bulk organic interference and enhancing.pdf`
- Chunk: `31`
- Registered exact span: ([SOURCE_TEXT_OMITTED sha256=3fb3297485931eaed619b25c88848bf953dc7d1614d886f890b6bef45d92d510].

```text
([SOURCE_TEXT_OMITTED sha256=87d1b188969ed4342ab88661211dc3fc36a7641599349770594e1d853b5416ac]
```

#### WF10_007_MMG003

- Role: `optional_gold`
- Document: `2023 - Su - Boosting PFOA photocatalytic removal from water using highly adsorptive and sunlight-responsive ZIF67 - MIL-100(Fe) modified C3N4.pdf`
- Chunk: `41`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=cd69e0f46c068ee51c738903f2d80fa3df6dbcbb3522ae8590a1a9509b6ebd3c].

```text
[SOURCE_TEXT_OMITTED sha256=fef8112a5e8b3765e45cdbbaf31ed062886b7de9d8eb37cb566457f932679f39] +
```

#### WF10_007_MMG004

- Role: `optional_gold`
- Document: `2021 - Qanbarzadeh - Impacts of Reactor Configuration, Degradation Mechanisms, and Water Matrices on Perfluorocarboxylic Acid Treatment Efficiency by the UV.pdf`
- Chunk: `14`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=cc050ac0ba7434858faffbe93e4628442d16bea202e8dbe75e010ab8d112ef08].

```text
[SOURCE_TEXT_OMITTED sha256=d498e20d5032086d922cbd929d9610570e49a476c52bff4ee906f8990e8b927e].
```

#### WF10_007_MMG005

- Role: `optional_gold`
- Document: `2025 - Sun - Adsorption-photocatalysis synergistic removal of perfluoroalkyl - polyfluoroalkyl substances by reusable chitin - polyethylene imine - O-g-C3N4 sponges.pdf`
- Chunk: `30`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=8a9a262f1fe4566f289402ed773ff0f07299b5effda6fc1626a1161ea1e5a801].

```text
[SOURCE_TEXT_OMITTED sha256=c992134e829440b40541d8d8533a48020a2c5cc7cd8e1418ce85e73385a60bef] -
```

#### WF10_007_MMG006

- Role: `optional_gold`
- Document: `2023 - Smith - Electrochemical Oxidation for Treatment of PFAS in Contaminated Water and Fractionated Foam─A Pilot-Scale Study.pdf`
- Chunk: `6`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=556ee88fb0f209d94a4aa85ae4fd6a2ad5c9f1adb52b33d2b6169503265a2820].

```text
[SOURCE_TEXT_OMITTED sha256=79a8d6a3f3a7a451e9f99693cffda87db1c19fc1d2bc3294ee640f826ebc7111].
```

#### WF10_007_MMG007

- Role: `negative_gold`
- Document: `2023 - Zeidabadi - Effects of water matrix on per- and poly-fluoroalkyl substances (PFAS) treatment - Physical-separation and degradation processes - A review.pdf`
- Chunk: `87`
- Registered exact span: ([SOURCE_TEXT_OMITTED sha256=055a757a86e12ecb14b365691b2e9ee01905ffe6df65b8517c53ead274893b3c].

```text
[SOURCE_TEXT_OMITTED sha256=bb18f4f0b9e52aa3400d4c1f93c758e416f280a3c95e4ec1ee3876ca319f1ecb]-
```

---

## WF10_009

**Question:** What level of PFAS removal has been seen with pressure-driven membranes, and under what kind of operating conditions?

### Task components

- `WF10_009-T01`: Extract and summarize the reported ranges or representative values of PFAS removal (e.g., rejection percentages) achieved by pressure-driven nanofiltration (NF) and reverse osmosis (RO) membranes, making clear that these are condition-specific and not universal, and specifying PFAS compounds, matrices, and any stated operating conditions where provided.
- `WF10_009-T02`: Identify and report at least one specific example of PFAS removal using a reverse osmosis membrane operated at relatively high pressure, including the numeric removal level, the operating pressure, and any explicitly stated PFAS compounds, matrices, and other operating conditions, while clearly indicating that the result is condition-specific (e.g., bounded, approximate, or tied to particular conditions).

### Normative claim groups

#### WF10_009-G01

- Component: `WF10_009-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Commercial NF and RO membranes have achieved PFAS rejection efficiencies up to about 99% in water and wastewater under specific operating conditions.
- Full: Award full credit for recognizing that available commercial NF and RO membranes have demonstrated high PFAS rejection in water and wastewater, with efficiencies reaching up to about 99%, and for explicitly treating this as condition-specific rather than universal.
- Partial: Award partial credit if the answer notes high PFAS rejection by NF/RO membranes but omits the approximate 99% level, the water/wastewater matrix, or the condition-specific nature of the reported efficiencies.
- Contradiction: Mark as contradictory if the answer claims substantially different typical maximum rejection efficiencies (e.g., far below or above 99%) or presents these values as universally achievable under all conditions.
- Linked exact evidence:
  - `WF10_009_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=707191fba3077cab3d1683e56e382c32eccf751da9d69849ba92fc52cd231fdc].
    Supports: States that commercial NF and RO membranes treating water and wastewater achieved PFAS rejection efficiencies up to 99%.

#### WF10_009-G02

- Component: `WF10_009-T01`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: Pressure-driven NF and RO membranes have shown very high PFAA rejections (>98.3%) in CCMF sequences at 97% water recovery, and NF/RO studies report PFAS removals up to about 97–99% for specific compounds under defined conditions.
- Full: Award full credit for summarizing that specific NF/RO applications have reported very high PFAS rejection, including overall PFAA rejection >98.3% during CCMF sequences at 97% water recovery, PFOS removal increasing from about 91% to ~97.5% with pH adjustment and up to ~99.4% with increased Ca2+ using a PMIA NF membrane, and PFHxA rejection of about 99.4% by an NF membrane at 20 bar.
- Partial: Award partial credit if only one or two of these specific high-rejection examples are described, or if approximate percentages are mentioned without tying them to the stated operating conditions.
- Contradiction: Mark as contradictory if the answer misstates these high rejection values by a large margin or associates them with incorrect operating conditions (e.g., wrong pressure or pH trends).
- Linked exact evidence:
  - `WF10_009_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=707191fba3077cab3d1683e56e382c32eccf751da9d69849ba92fc52cd231fdc].
    Supports: Shows that PFAA rejection exceeded 98.3% when membranes were operated in CCMF sequences at 97% water recovery.
  - `WF10_009_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=248def89fcb24d3f586af586c6240f62c06ca45ed2a4dd1219c2b26d189f00cb] %.
    Supports: Reports PFOS elimination by a PMIA NF membrane increasing from 91.17% at pH 3.2 to 97.49% at pH 9.5.
  - `WF10_009_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=9f9eac7ecdae105927406ac4578789ad11226ff5d0e8316ab1caf9937631d9bf] %.
    Supports: Shows PFOS rejection increasing from 97.10% to 99.40% as Ca2+ concentration increased from 0.1 to 2 mM with the PMIA NF membrane.
  - `WF10_009_MMG003` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > The  NF  membrane  first  rejected 99.4  %  PFHxA  at  the  operating  pressure  of  20  bar.
    Supports: States that an NF membrane rejected 99.4% of PFHxA at an operating pressure of 20 bar.

#### WF10_009-G03

- Component: `WF10_009-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Specific NF membrane studies report PFAS rejection ranges around 89–99% for PFOA, PFOS, and PFHxA from synthetic solutions at low to moderate pressures.
- Full: Award full credit for correctly describing that, in synthetic solution tests, NF achieved about 99% PFOA rejection at 2 bar, about 97.6% PFOS rejection at 65 psi using an MXene-functionalized hollow fiber NF membrane, and 89–99% PFHxA rejection at 4.8 bar using N90/N270 flat-sheet NF membranes.
- Partial: Award partial credit if only some of these NF examples are mentioned, or if the correct rejection levels are reported without specifying the associated pressures or compounds.
- Contradiction: Mark as contradictory if the answer assigns these rejection percentages to the wrong PFAS, membrane types, or pressures, or significantly distorts the numeric ranges.
- Linked exact evidence:
  - `WF10_009_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=72d97a3686e5c81a6ffa1855bf5c638258df1a4ff53f517c71ac7c121c7b8722].
    Supports: Reports an NF lab study using a synthetic solution at 2 bar where PFOA rejection was 99%.
  - `WF10_009_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=72d97a3686e5c81a6ffa1855bf5c638258df1a4ff53f517c71ac7c121c7b8722].
    Supports: Reports a functionalized MXene PA hollow fiber NF membrane treating synthetic solution at 65 psi achieving 97.6% PFOS rejection.
  - `WF10_009_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=72d97a3686e5c81a6ffa1855bf5c638258df1a4ff53f517c71ac7c121c7b8722].
    Supports: Reports NF lab tests with N90 and N270 flat-sheet membranes treating synthetic solution at 4.8 bar, achieving PFHxA rejection in the 89–99% range.

#### WF10_009-G04

- Component: `WF10_009-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: A specific RO study using XLE, BW30, and SW30 membranes treating synthetic PFHxA solution at 6.9–55.2 bar achieved PFHxA rejection greater than 98%, demonstrating high-pressure RO performance under those conditions.
- Full: Award full credit for identifying that a lab-scale RO study using XLE, BW30, and SW30 polyamide flat-sheet membranes, with synthetic PFHxA solution, operated at pressures from 6.9 to 55.2 bar and fluxes around 15–90 LMH, achieved PFHxA rejection greater than 98%, and for emphasizing that this is specific to these conditions.
- Partial: Award partial credit if the answer notes PFHxA rejection >98% by RO at an elevated pressure but omits some operating details (e.g., pressure range, flux, or membrane names).
- Contradiction: Mark as contradictory if the answer substantially misstates the pressure range, the rejection level, or the compound (e.g., assigns the >98% rejection at 6.9–55.2 bar to a different PFAS or to NF instead of RO).
- Linked exact evidence:
  - `WF10_009_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=72d97a3686e5c81a6ffa1855bf5c638258df1a4ff53f517c71ac7c121c7b8722].
    Supports: Provides a lab RO example using XLE, BW30, and SW30 polyamide flat-sheet membranes treating synthetic PFHxA solution at 6.9–55.2 bar with ~15–90 LMH flux, achieving PFHxA rejection greater than 98%.

#### WF10_009-G05

- Component: `WF10_009-T02`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: Additional RO examples show PFOS or mixed PFOA/PFOS rejection around or above 99% at moderate pressures or in full-scale surface water treatment, complementing the high-pressure PFHxA example.
- Full: Award full credit for correctly stating that a lab-scale RO test with ESPA3, LFC3, BW30, and SG polyamide flat-sheet membranes treating synthetic solution at 1380 kPa and 33–42 LMH achieved 99% PFOS rejection, and that a full-scale RO treating surface water achieved >99% rejection of PFOA and PFOS, and for presenting these as condition-specific examples.
- Partial: Award partial credit if only one of these RO examples is mentioned or if some operating details (pressure, flux, matrix) are omitted.
- Contradiction: Mark as contradictory if the answer substantially misreports the rejection percentages or operating conditions (e.g., interpreting 1380 kPa as a drastically different pressure or assigning 99% rejection to a different PFAS).
- Linked exact evidence:
  - `WF10_009_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=72d97a3686e5c81a6ffa1855bf5c638258df1a4ff53f517c71ac7c121c7b8722].
    Supports: Describes a lab-scale RO study using ESPA3, LFC3, BW30, and SG polyamide flat-sheet membranes with synthetic solution at 1380 kPa and 33–42 LMH flux, achieving 99% PFOS rejection.
  - `WF10_009_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=72d97a3686e5c81a6ffa1855bf5c638258df1a4ff53f517c71ac7c121c7b8722].
    Supports: Reports a full-scale RO system treating surface water where PFOA and PFOS rejections were greater than 99%.

#### WF10_009-X01

- Component: `WF10_009-T01`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: Reported NF and RO PFAS rejection efficiencies are specific to the tested conditions and are not universal performance guarantees for all PFAS, membranes, or operating regimes.
- Full: Treat as a constraint that all cited NF/RO rejection values (e.g., >98.3%, up to 99%) are tied to specific experimental or operational conditions and should not be presented as universally applicable PFAS treatment performance.
- Partial: Still apply this constraint if an answer implicitly acknowledges condition-specificity (e.g., by using language like 'in this study'), even if it does not explicitly state the limitation.
- Contradiction: Flag as violating the constraint if an answer turns any of the condition-specific rejection values into universal claims about NF/RO performance across all PFAS, membranes, or operating conditions.
- Linked exact evidence:
  - `WF10_009_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=707191fba3077cab3d1683e56e382c32eccf751da9d69849ba92fc52cd231fdc].
    Supports: Indicates that the >98.3% PFAA rejection applies to the specific membranes and CCMF sequences at 97% water recovery used in that work, not universally.
  - `WF10_009_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=0a785b592a2d96e425f3c6a030d7b32008e2d1ecd377a616a048533a45cd9ac6] %.
    Supports: The phrase 'could reach up to 99%' implies a maximum under particular conditions, supporting the idea that 99% rejection is not universally guaranteed.
  - `WF10_009_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=248def89fcb24d3f586af586c6240f62c06ca45ed2a4dd1219c2b26d189f00cb] %.
    Supports: Shows that PFOS rejection by a given NF membrane depends on pH, underscoring condition-specific performance.
  - `WF10_009_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=72d97a3686e5c81a6ffa1855bf5c638258df1a4ff53f517c71ac7c121c7b8722].
    Supports: Lists rejection values together with specific matrices and operating pressures/fluxes, indicating that the reported high rejections are tied to these particular test conditions.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

Across the reported studies, pressure-driven nanofiltration (NF) and reverse osmosis (RO) membranes have achieved high, but clearly condition-specific, PFAS rejection in water and wastewater.

A review notes that available commercial NF and RO membranes treating water and wastewater "exhibited a good PFAS rejection in water and wastewater with efficiencies that could reach up to 99 %" (WF10_009_MMG001), indicating an approximate upper bound under favorable conditions rather than a universal value. In the same work, membranes operated in CCMF sequences with 97 % water recovery displayed overall PFAA rejection values of "> 98.3 %" for the assessed compounds (WF10_009_MMG001), showing very high removal for those specific PFAA and operating conditions.

Several NF studies provide more detailed, compound- and condition-specific benchmarks. A PMIA NF hollow-fiber membrane treating PFOS showed that raising pH from 3.2 to 9.5 increased PFOS elimination from 91.17 % to 97.49 %, and increasing Ca2+ from 0.1 mM to 2 mM further raised PFOS rejection from 97.10 % to 99.40 % (WF10_009_MMG002), illustrating that PFOS removal by this NF membrane can approach ~99 % under higher pH and ionic strength. Another study summarized in a table reports an NF lab test with a synthetic solution at 2 bar where PFOA rejection was 99 % (WF10_009_MMG004), and a functionalized MXene polyamide hollow-fiber NF membrane treating synthetic solution at 65 psi achieved 97.6 % PFOS rejection (WF10_009_MMG004). Commercial N90 and N270 flat-sheet NF membranes treating synthetic PFHxA solution at 4.8 bar achieved PFHxA rejection in the 89–99 % range (WF10_009_MMG004). In a coupled NF–electro-oxidation system, the NF step alone rejected 99.4 % PFHxA at an operating pressure of 20 bar (WF10_009_MMG003). Together, these NF results indicate that, under specific lab conditions with synthetic PFAS solutions at low to moderate pressures (2–20 bar or 65 psi), PFAS rejections on the order of roughly 90–99.4 % have been reported for PFOA, PFOS, and PFHxA.

RO studies likewise report very high, condition-dependent PFAS rejection. A lab-scale RO study using XLE, BW30, and SW30 polyamide flat-sheet membranes treating synthetic PFHxA solution operated at pressures from 6.9 to 55.2 bar with fluxes of approximately 15–90 LMH achieved PFHxA rejection greater than 98 % (WF10_009_MMG004). This provides a specific high-pressure RO example: under these lab conditions (synthetic PFHxA, 6.9–55.2 bar, ~15–90 LMH), PFHxA removal exceeded 98 %, demonstrating strong rejection but only for that particular configuration. Another lab RO study using ESPA3, LFC3, BW30, and SG polyamide flat-sheet membranes treating synthetic PFOS solution at 1380 kPa (with fluxes of 33–42 LMH) reported 99 % PFOS rejection (WF10_009_MMG004). At full scale, an RO system treating surface water achieved greater than 99 % rejection of PFOA and PFOS (WF10_009_MMG004). These RO results show that, in both lab and full-scale configurations, RO can reach around 99 % rejection for specific PFAS (PFHxA, PFOS, PFOA) under the documented pressures, fluxes, matrices, and membrane types.

Overall, the evidence indicates that pressure-driven NF and RO membranes have achieved PFAS rejections ranging from roughly the low 90% range up to about 99–99.4% for specific PFAS (including PFOA, PFOS, PFHxA, and PFAA mixtures) in synthetic solutions, water, and wastewater, at pressures from a few bar up to about 55.2 bar (or 1380 kPa) and with other operating variables such as pH, ionic strength, and recovery playing important roles. These values are explicitly tied to the particular compounds, membranes, matrices, and conditions reported and should not be generalized as universal performance for all PFAS or operating regimes.

### Unresolved or unsupported boundaries

- The question broadly refers to "pressure-driven membranes" but the supplied evidence only provides quantitative PFAS removal data for NF and RO; no data are given for other pressure-driven membrane types such as microfiltration or ultrafiltration.
- The evidence does not provide a systematic general rejection range across all PFAS species; only specific compounds (PFOA, PFOS, PFHxA, PFAA mixtures, GenX in one NF example) are quantified.
- No detailed operating conditions such as temperature, cross-flow velocity, or membrane age are reported in the evidence beyond pressure, flux, pH, ionic strength, recovery, and matrix descriptions.
- Mechanistic explanations (e.g., size exclusion vs. electrostatic effects) are only briefly mentioned for the PMIA NF membrane and are not quantified across studies, so a general mechanistic summary cannot be reliably drawn from the provided text.

### Complete approved source chunks

#### WF10_009_MMG001

- Role: `required_gold`
- Document: `2024 - Taher - Progress on remediation of per - and polyfluoroalkyl substances (PFAS) from water and wastewater using membrane technologies - A review.pdf`
- Chunk: `19`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=707191fba3077cab3d1683e56e382c32eccf751da9d69849ba92fc52cd231fdc].

```text
[SOURCE_TEXT_OMITTED sha256=7847a6cbc8c24230bdbb18384f4f339a348122895decb92abd94afc4e2fe1c58]
```

#### WF10_009_MMG002

- Role: `optional_gold`
- Document: `2024 - Taher - Progress on remediation of per - and polyfluoroalkyl substances (PFAS) from water and wastewater using membrane technologies - A review.pdf`
- Chunk: `20`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=248def89fcb24d3f586af586c6240f62c06ca45ed2a4dd1219c2b26d189f00cb] %.

```text
[SOURCE_TEXT_OMITTED sha256=b318c4b6a577bd48411b9b57d52e5a488809912323340da53d90d3dbd6af4b7c]
```

#### WF10_009_MMG003

- Role: `required_gold`
- Document: `2023 - Unknown - Recent advances in electrochemical decontamination of perfluorinated compounds from water - a review.pdf`
- Chunk: `51`
- Registered exact span: The NF membrane first rejected 99.4 % PFHxA at the operating pressure of 20 bar.

```text
[SOURCE_TEXT_OMITTED sha256=2ef856ca23acf6cb5eb9f5dbc4d9ac28b35f779601953e2667a95b001fbf2899]
```

#### WF10_009_MMG004

- Role: `required_gold`
- Document: `2024 - Taher - Progress on remediation of per - and polyfluoroalkyl substances (PFAS) from water and wastewater using membrane technologies - A review.pdf`
- Chunk: `17`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=72d97a3686e5c81a6ffa1855bf5c638258df1a4ff53f517c71ac7c121c7b8722].

```text
[SOURCE_TEXT_OMITTED sha256=0db2f7ac4b7fe41df2547799ea252b81cfe68c0fe9f429ffc6f8dab959fea4b2]
```

### Deterministic resolution

- {'claim_group_id': 'WF10_009-G02', 'evidence_id': 'WF10_009_MMG003', 'action': 'restored_original_chunk_whitespace', 'old_span_sha256': 'd46c590560334eb72f6e9896f35afa324657b075d0b44fb12ad2c8dbff9be727', 'new_span_sha256': 'a63fb8d567f9fe28c8e1ccb3cde2f9af3ace12a8c60f3c5615dc58d2b85a300b'}
- Replaced the duplicated pH quote with the verbatim Ca2+ sentence in G02.
- Replaced the duplicated CCMF quote with the verbatim up-to-99% sentence in X01.

---

## WF10_010

**Question:** What examples show background water chemistry or matrix components changing PFAS removal performance?

### Task components

- `WF10_010-T01`: Identify examples where dissolved organic matter (DOM) or other natural organic matrix components changed PFAS removal performance, and describe the reported limitations, uncertainties, or caveats that prevent generalizing these effects to all PFAS or all water types.
- `WF10_010-T02`: Identify examples where background cations or overall ionic composition of the water matrix changed PFAS removal performance, and explain the study-specific conditions and uncertainties so the effects are not overstated beyond the reported context.
- `WF10_010-T03`: Identify examples where ammonia or other competing species (such as co-contaminants or background solutes) changed PFAS removal performance, and summarize how the studies themselves frame these results as condition-specific, including any explicit limitations, caveats, or negative/weak effects reported.

### Normative claim groups

#### WF10_010-G01

- Component: `WF10_010-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: A realistic river-water matrix containing dissolved organic matter and other constituents decreased PFOA adsorption efficiency relative to simpler solutions, with the decrease attributed partly to humic substances and other solids, but the adsorbent still showed good performance under these realistic conditions.
- Full: Count as fully supported if the answer describes that, in the Shaikh et al. study, adding a realistic background river-water matrix (with organic matter, clay, and other typical species) reduced PFOA removal efficiency by roughly 10 percentage points compared to simpler water, attributes this decrease to humic acid, bentonite, and silicate species, and notes that the authors still consider PFOA removal performance good under realistic background conditions.
- Partial: Count as partially supported if the answer mentions that a realistic background water matrix decreased PFOA removal for the adsorbent or attributes the decrease to humic acid/bentonite/silicate species, but omits that the decrease was about 10 percentage points, or fails to note that the authors still consider performance good in realistic matrices.
- Contradiction: Flag as contradiction if the answer claims that the realistic background water matrix did not affect PFOA removal for these adsorbents, or that humic acid, bentonite, and silicate species had no role or improved PFOA removal in this specific study.
- Linked exact evidence:
  - `WF10_010_MMG003` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=3e73e41f078a5665ab129c1c68b32ea8c476451be0cc69d94cd910db7f09aba4] %.
    Supports: That a realistic background water matrix based on Ganga River composition (including organic matter and clay) decreased PFAS/PFOA removal efficiency from 98% to 88% compared to simpler conditions.
  - `WF10_010_MMG007` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=aff8f9c9284be94c509c404177f8866e111be609311f743967e1eae96b618286] .
    Supports: That the ~10% decrease in PFOA removal efficiency was attributed specifically to silicate species, humic acid, and bentonite interacting with the adsorbent.
  - `WF10_010_MMG007` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=07f5a7bdb1b4c662e2db500d6d4a44ddae18d1fb887455aa6b5d6aa063558afa].
    Supports: That despite the decrease, the authors concluded the adsorbents still exhibited good PFOA removal performance under realistic water-matrix conditions.

#### WF10_010-G02

- Component: `WF10_010-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Dissolved organic matter in groundwater and treated wastewater decreased PFAS removal in some membrane and adsorption systems, but the magnitude and even direction of the effect were PFAS- and material-specific and are not generalizable to all PFAS or all waters.
- Full: Count as fully supported if the answer notes that (1) Taher et al. report that changing the source water from spiked water to groundwater lowered NF removal of the same PFAAs, attributing this to components such as dissolved organic matters (and Ca2+), and (2) Ramos et al. report that for in-house biochars, PFAS removal performance decreased in treated municipal wastewater vs DI, explicitly linking this to ions and DOC reducing adsorption, while also noting that the decrease was almost non-existent for PFOS, illustrating PFAS- and matrix-specific behavior.
- Partial: Count as partially supported if the answer cites only one of these DOM-related examples (either the NF/groundwater case or the biochar/treated wastewater case) or mentions decreased performance due to DOM or DOC without describing PFAS- or matrix-specific exceptions such as the minor effect on PFOS.
- Contradiction: Flag as contradiction if the answer asserts that dissolved organic matter has no effect on PFAS removal in these reported NF or biochar systems, or claims that the reported effects apply universally to all PFAS and all water matrices without acknowledging the PFAS- and matrix-specific nature described in the evidence.
- Linked exact evidence:
  - `WF10_010_MMG009`
    > [SOURCE_TEXT_OMITTED sha256=ba574a1b6c97564b21e719e36b5690da9ffde3d635d98c33064de79c56dfb12e].
    Supports: That switching from spiked water to groundwater reduced NF removal of the same PFAAs, and that dissolved organic matters present in groundwater contributed to this reduced removal.
  - `WF10_010_MMG010` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=cfdd5d8f6520d118bad87c02e16d350ffa6f82370586ee018157b221e09a50ce].
    Supports: That for in-house biochars, PFAS removal performance decreased when switching from DI water to treated municipal wastewater.
  - `WF10_010_MMG010` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=cbd994e11276cb3a2935d403acee2bf3899a6ec087e0c94db922fe5d22e1c057]
    Supports: That the observed decrease in biochar removal performance is attributed to ions and DOC in treated wastewater decreasing PFAS adsorption capacity and performance.
  - `WF10_010_MMG010` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=62d2acd0c951bb82e3010fca4364abb8c4841cf2d759beaeda8afb56c3408d4d]
    Supports: That for PFOS specifically, the decrease in removal efficiency in treated wastewater versus DI water was almost non-existent, illustrating PFAS-specific behavior.

#### WF10_010-G03

- Component: `WF10_010-T01`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: Humic acid as a model natural organic matter slightly increased PFOS removal in one nanofiltration experiment, and the study cautioned that such findings should not be generalized because water quality and experimental parameters differ across studies.
- Full: Count as fully supported if the answer notes that Franke et al. observed a slight increase in PFOS removal efficiency for a humic-acid-containing solution relative to pure deionized water in NF270 experiments, and also mentions their caveat that comparisons with other studies should be made cautiously due to differing experimental parameters and water qualities.
- Partial: Count as partially supported if the answer mentions only that humic acid slightly increased PFOS removal efficiency, without referencing the authors' caution about generalizing across studies.
- Contradiction: Flag as contradiction if the answer states that humic acid decreased PFOS removal in this specific NF270 humic-acid experiment, or presents the observed increased removal as a general rule across all PFAS or water types.
- Linked exact evidence:
  - `WF10_010_MMG011`
    > [SOURCE_TEXT_OMITTED sha256=6d7ba27c1f7a129a6362d14a0419d48be81c2c7d74b747dbc567b8192906e765].
    Supports: That adding humic acid slightly increased PFOS removal efficiency compared to pure deionized water in this nanofiltration study.
  - `WF10_010_MMG011` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=4c68a8875ad52ad3459cde36231f892095110303298ff86b13289862bad12ae6].
    Supports: That the authors explicitly caution against overgeneralizing or directly comparing their humic-acid findings to other studies due to differing conditions and water qualities.

#### WF10_010-G04

- Component: `WF10_010-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Background ions and cations, including Ca2+ and salts in real waters, altered PFAS removal in nanofiltration, adsorption, and plasma systems, with effects ranging from decreased removal in some contexts to enhanced removal for specific PFAS, indicating highly condition-specific behavior.
- Full: Count as fully supported if the answer explains that (1) Taher et al. attribute reduced NF removal of PFAAs in groundwater vs spiked water partly to dissolved organic matters and Ca2+ affecting interactions with the membrane, (2) Ramos et al. report decreased PFAS adsorption by biochars in treated municipal wastewater compared to DI water and link this to ions and DOC in treated wastewater, and (3) Zhang et al. find that in a plasma system the impact of different real water matrices on PFOA, PFOS, and HFPO-TA removal is almost negligible, but removal efficiencies of PFHxA, PFHxS, and HFPO-DA are enhanced in these matrices, with the presence of salt cited as favoring interfacial adsorption and increased conductivity enhancing discharge and PFAS decomposition.
- Partial: Count as partially supported if the answer discusses only one or two of these ionic-composition examples (e.g., only NF/groundwater or only the plasma enhancement) or mentions that ions/salts affect PFAS removal without distinguishing between decreased and enhanced, PFAS-specific effects.
- Contradiction: Flag as contradiction if the answer claims that background ions or Ca2+ have no effect on PFAS removal in these studies, or presents ionic composition as always beneficial or always detrimental across all PFAS and technologies, contrary to the mixed effects reported.
- Linked exact evidence:
  - `WF10_010_MMG009`
    > [SOURCE_TEXT_OMITTED sha256=ba574a1b6c97564b21e719e36b5690da9ffde3d635d98c33064de79c56dfb12e].
    Supports: That in NF treatment, switching from spiked water to groundwater reduced PFAA rejection and that Ca2+ and other components in groundwater contributed to this effect.
  - `WF10_010_MMG010` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=cfdd5d8f6520d118bad87c02e16d350ffa6f82370586ee018157b221e09a50ce].
    Supports: That for in-house biochars, PFAS removal performance decreased in treated municipal wastewater compared to DI water, implying an effect of wastewater ions and chemistry.
  - `WF10_010_MMG010` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=cbd994e11276cb3a2935d403acee2bf3899a6ec087e0c94db922fe5d22e1c057]
    Supports: That ions prevalent in treated wastewater, together with DOC, can decrease PFAS adsorption capacity and performance of carbonaceous adsorbents.
  - `WF10_010_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=a8125f8d717683fcad00de3ab4959f2ef21a573012942fb3497ed30ce3e7450b]).
    Supports: That in a plasma system, the effect of different water matrices (tap, wastewater effluent, surface water) on PFOA, PFOS, and HFPO-TA removal was almost negligible, whereas removal of PFHxA, PFHxS, and HFPO-DA was enhanced in these matrices.
  - `WF10_010_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=b80c7a5b64dc93f384e9d320622fffec22d47ddf027f86ee3c3589faae304703]
    Supports: That salt in actual water matrices can favor PFAS interfacial adsorption by affecting electrostatic repulsion and hydrophobic-tail activity.
  - `WF10_010_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=7aaf9c5d89e63bc50f3956d59f6f77e0b29f33038efd34f1caab928967fd71d0]
    Supports: That higher conductivity from salts in the water matrix can strengthen electric discharge and further promote PFAS decomposition in the plasma system.

#### WF10_010-G05

- Component: `WF10_010-T02`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: Differences among leachate, deionized water, and groundwater led to modest differences in plasma-based PFAS degradation, but one study explicitly concluded that the water matrix did not have a major impact on removal of the two representative PFAS examined.
- Full: Count as fully supported if the answer notes that in Eeso et al.'s thin-water-film nonthermal plasma study, average PFOA and PFOS removal percentages differed among leachates, deionized water, and groundwater, but the authors explicitly concluded that the water matrix did not have a big impact on degradation of these two PFAS and attributed small variations potentially to different PFAS and precursor concentrations.
- Partial: Count as partially supported if the answer only mentions that removal percentages varied among leachate, deionized water, and groundwater, without stating that the authors considered the overall impact of matrix on PFOA and PFOS degradation to be small.
- Contradiction: Flag as contradiction if the answer claims that this study found large or dominant matrix effects on PFOA and PFOS degradation, or that the water matrix had no differences in removal percentages at all.
- Linked exact evidence:
  - `WF10_010_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=b187dbee2da2d6470da318c426a09e9f630b00fd890e81716cc50d8df8832b32].
    Supports: That average removal percentages for PFOA and PFOS varied among leachates, deionized water, and groundwaters in this plasma study.
  - `WF10_010_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=a9e641280b758333109664d6d96f9184631986b9376ba34a6f307e25600ea313].
    Supports: That the authors concluded the water matrix did not strongly impact degradation of PFOA and PFOS, and that small variations might be due to PFAS and precursor concentration differences.

#### WF10_010-G06

- Component: `WF10_010-T03`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Co-existing inorganic and organic species such as silicate, humic acid, bentonite, ions, and DOC acted as competing species that reduced PFAS adsorption in some studies, but the magnitude of competition and its mitigation were PFAS- and sorbent-specific.
- Full: Count as fully supported if the answer describes that (1) Shaikh et al. found a 10% decrease in PFOA removal efficiency for CTAB-impregnated activated carbon that they attribute to silicate species, humic acid, and bentonite—which are themselves adsorbed by the adsorbent—and (2) Ramos et al. report that ions and DOC in treated municipal wastewater reduce PFAS adsorption capacity and performance of biochars through pore-blockage effects, but the decrease is almost non-existent for PFOS and can be mitigated by selecting a suitable biochar (e.g., Rogue biochar), highlighting condition- and PFAS-specific competition effects.
- Partial: Count as partially supported if the answer mentions only one of these competition examples (e.g., only the silicate/humic/bentonite case or only the ions/DOC/pore blockage case) or describes decreased PFAS adsorption due to competing species without acknowledging PFAS-specific exceptions and the potential for mitigation through adsorbent selection.
- Contradiction: Flag as contradiction if the answer states that these co-existing species (silicate, humic acid, bentonite, ions, DOC) had no effect on PFAS adsorption in the cited studies, or that competition effects were uniformly large for all PFAS and could not be mitigated by changing adsorbent properties.
- Linked exact evidence:
  - `WF10_010_MMG007` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=aff8f9c9284be94c509c404177f8866e111be609311f743967e1eae96b618286] .
    Supports: That humic acid and bentonite interact with and are adsorbed by the activated carbon and that a 10% decrease in PFOA removal efficiency is attributed to silicate species, humic acid, and bentonite, indicating competition for adsorption sites.
  - `WF10_010_MMG010` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=cbd994e11276cb3a2935d403acee2bf3899a6ec087e0c94db922fe5d22e1c057]
    Supports: That ions in treated wastewater and DOC act as competing species that decrease PFAS adsorption capacity and performance of carbonaceous adsorbents via pore blockage.
  - `WF10_010_MMG010` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=62d2acd0c951bb82e3010fca4364abb8c4841cf2d759beaeda8afb56c3408d4d]
    Supports: That the competitive decrease in removal efficiency in treated wastewater was almost non-existent for PFOS, showing PFAS-specific competition effects.
  - `WF10_010_MMG010` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=04a2b3012bc8aeea1e6434463738962ba6fd30e5ecab839a0f2a3bb198233e5d].
    Supports: That choosing appropriate biochar properties (e.g., Rogue biochar) can mitigate competition between PFAS and between PFAS and background species in complex water chemistries.

#### WF10_010-X01

- Component: `WF10_010-T02`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: For some PFAS and systems, the impact of water matrices or ionic background on removal was reported as negligible or small, so these findings limit how strongly matrix effects can be generalized.
- Full: Use as a constraint if the answer acknowledges that some plasma-based studies report that the water matrix did not have a big impact on degradation of PFOA and PFOS, or that the impact of different water matrices on PFOA, PFOS, and HFPO-TA removal was almost negligible, thereby limiting claims that water-matrix or ionic composition always strongly changes PFAS removal.
- Partial: Use as a partial constraint if the answer mentions matrix effects but does not recognize that some reported effects are statistically negligible or characterized as small by the authors.
- Contradiction: Flag as contradiction if the answer claims that these plasma studies observed large or dominant water-matrix effects for PFOA, PFOS, or HFPO-TA.
- Linked exact evidence:
  - `WF10_010_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=a9e641280b758333109664d6d96f9184631986b9376ba34a6f307e25600ea313].
    Supports: That in this plasma study, the authors judged the impact of water matrix on PFOA and PFOS degradation to be small, limiting the strength of matrix-effect claims.
  - `WF10_010_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=dda1cd5124bd08bdb493d4ee646261a8a53942121c541cc2cfab0aabab2217fb]).
    Supports: That in another plasma study, the impact of different water matrices on removal of PFOA, PFOS, and HFPO-TA was statistically negligible, constraining overstatement of matrix effects for these compounds.

#### WF10_010-X02

- Component: `WF10_010-T01`
- Importance: `supplementary`
- Scoring role: `constraint_only`
- Proposition: One study explicitly warns that comparisons of PFAS removal efficiencies across studies and water qualities should be made with care, underscoring methodological and water-quality differences as key uncertainties.
- Full: Use as a constraint if the answer highlights that Franke et al. advise careful comparison of PFAS removal efficiencies across different studies and water qualities due to substantial differences in experimental parameters and water compositions, thereby limiting the generalizability of observed DOM effects.
- Partial: Use as a partial constraint if the answer notes some uncertainty or context-specificity but does not explicitly mention the caution about cross-study comparisons.
- Contradiction: Flag as contradiction if the answer claims that the humic-acid effects reported by Franke et al. can be directly generalized to all PFAS treatments or water qualities without limitations.
- Linked exact evidence:
  - `WF10_010_MMG011` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=4c68a8875ad52ad3459cde36231f892095110303298ff86b13289862bad12ae6].
    Supports: That the authors caution against straightforward comparison and generalization of their PFOS/humic-acid results to other studies and water qualities.

#### WF10_010-X03

- Component: `WF10_010-T03`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: The supplied evidence does not report ammonia effects on PFAS removal performance; ammonia-containing solutions appear only in the context of regeneration tests, not as competing species during removal.
- Full: Use as a constraint to prevent introducing unsupported claims about ammonia affecting PFAS removal performance, noting that the only mention of NH4Cl and NH4OH in the supplied evidence is in regeneration tests rather than removal experiments.
- Partial: Use as a partial constraint if the answer simply avoids making claims about ammonia effects without explicitly stating the lack of evidence.
- Contradiction: Flag as contradiction if the answer asserts ammonia changed PFAS removal performance in the reported studies, since the provided text only addresses ammonia in regeneration, not as a competing species during removal.
- Linked exact evidence:
  - `WF10_010_MMG007` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=6e04fb7b8262d94d0617bb8eb8b8f8f7248edc2b420e6543092de3e126ff0590] ).
    Supports: That NH4Cl and NH4OH were evaluated as regeneration solutions for PFOA-loaded adsorbents, not as competing species during PFAS removal from water.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

Across the supplied studies, several examples show that background water chemistry and matrix components can change PFAS removal performance, but the effects are clearly described as PFAS‑specific, technology‑specific, and often modest, with explicit limitations on generalization.

For dissolved organic matter (DOM) and natural organic matrices, Shaikh et al. prepared a realistic background water matrix by matching the aqueous concentrations of background anions, cations, organic matter, and clay to a Ganga River water matrix to study their combined effect on PFOA adsorption by CTAB‑impregnated activated carbon adsorbents. In this realistic matrix, the adsorbent’s PFAS removal efficiency decreased from 98% to 88%. The authors state that humic acid and bentonite interact with the activated carbon and that “[SOURCE_TEXT_OMITTED sha256=d7c97229201ff24e1cf093e4c2ca7e816b7ea7ae123fda6504b5fd36aedec3e5],” meaning these natural and mineral components act as competing species for adsorption sites. At the same time, they conclude [SOURCE_TEXT_OMITTED sha256=0c5cbece6317fc64648cbbf04452b3dc7894a6bfb1c28d2960aa3b23c08edb69] matrix species,” underscoring that while the realistic matrix reduces performance somewhat, PFOA removal remains high and the observed decrease should not be interpreted as a universal failure under natural-water conditions.

Other work links DOM in natural waters to reduced removal in membrane and adsorption systems but again underlines the context dependence. In a pilot‑scale nanofiltration (NF) study summarized by Taher et al., elimination of PFAAs using NF and RO membranes with spiked AFFF water was >98% and 99%, respectively. However, “[SOURCE_TEXT_OMITTED sha256=d35cbe608816fa11209da9fce0a0f96b19a0dfa96c25773ae2ff683a3968bc3c] Ca2+ that effect the interaction between functional groups of the PFAAs and membrane.” Here, natural groundwater constituents including dissolved organic matter and Ca2+ reduce NF rejection relative to a simpler spiked matrix, but the reported removal remains high, and the mechanism is described specifically for this NF system and set of PFAAs.

In an adsorption context, Ramos et al. evaluated biochars for PFAS removal from reclaimed water. They report that “for biochars generated in house, the removal performance decreased in treated municipal wastewater compared to DI water.” They interpret this as “[SOURCE_TEXT_OMITTED sha256=5f8fbadf0edc78dcdd3369ff5379f893fcf148e546b89cd8ad3da568f6e284bb] performance of carbonaceous adsorbents due to pore‑blockage effects.” This explicitly links dissolved organic carbon (DOC) and co‑occurring ions in a realistic wastewater effluent to lower PFAS adsorption capacity. However, the effect is not uniform across PFAS: “[SOURCE_TEXT_OMITTED sha256=0cb3c4759fee84cce789b37b002a0ef615e79f5f72c2b2e673702353514820c9] biochar surface and this compound.” Furthermore, they note that “[SOURCE_TEXT_OMITTED sha256=fa3f459af88034fc9baeb0b8034ab8a7bcc51e40fe4558bd24ed1d82f49d7cb7] competition effects existing in more complex water chemistries.” These observations indicate that while DOC and ions can reduce PFAS uptake via pore blockage, the magnitude of the effect depends on PFAS structure (e.g., PFOS vs others) and sorbent properties and should not be extrapolated indiscriminately.

There are also cases where natural organic matter slightly improves apparent removal under specific conditions. In a nanofiltration study of PFOS using an NF270 membrane, Franke et al. reported removal efficiencies “[SOURCE_TEXT_OMITTED sha256=d8a2f2779e266ffd01e28f35a93e713643eb8b8bce959873b4e3d2b1d357a523]” and noted that “[SOURCE_TEXT_OMITTED sha256=ec6572806fde14451f6f5e81c25c34037095d68e6390be5b0fc2346d57a235c9] solution.” However, they caution that “comparisons to other studies should be made with care as many experimental parameters as well as water quality are often substantially different between studies.” Thus, the small beneficial effect of humic acid on PFOS removal is explicitly framed as context‑specific to their NF270 system and feedwater, not as a general rule for DOM in all PFAS treatments.

Regarding background cations and overall ionic composition, several studies highlight that ions can either hinder or enhance PFAS removal, depending on the treatment process and PFAS examined. The nanofiltration example summarized by Taher et al. explicitly attributes the reduction in PFAA rejection in groundwater (down to 92%) to “other components in the groundwater, such as dissolved organic matters and Ca2+ that effect the interaction between functional groups of the PFAAs and membrane.” This identifies Ca2+ as a key cationic component in natural groundwater that alters the interaction between PFAAs and the NF membrane, reducing removal compared to simpler spiked water.

In the biochar work described above, Ramos et al. connect decreased removal in treated municipal wastewater not only to DOC but also to “the ions prevalent in treated wastewater,” which “can decrease the PFAS adsorption capacity and performance of carbonaceous adsorbents due to pore‑blockage effects.” Here, the ionic strength and specific ions in the effluent are treated as contributors to competition and pore blocking in carbonaceous materials, but again the authors stress that the performance drop is PFAS‑dependent and can be mitigated by choosing a biochar with suitable physicochemical properties.

By contrast, Zhang et al. examined plasma‑based PFAS treatment in three real water matrices (tap water, wastewater effluent, and surface water), all spiked with the same PFAS mixture. They found that “[SOURCE_TEXT_OMITTED sha256=59a83e6bcd687e7a2f54401cd3555671588b5622ca1f5b4304a892b8f6a09e89]),” meaning that variations in background ions and other constituents among these waters did not significantly change removal for those three PFAS. However, “[SOURCE_TEXT_OMITTED sha256=37f45ba985cf2c861496aa6766af484062e64e8e173cf222a091ef46bab0d9d2] authors attribute these enhancements to the ionic composition: “[SOURCE_TEXT_OMITTED sha256=80ea3dd079eb1d997c70955b7659a9ffcd7108dc1df106ece6f65f20bf48e91a],” and “[SOURCE_TEXT_OMITTED sha256=932c5a8989569b6b01579280349b4d41c1a8feca2925fcd8d34ab9eabd1e6519].” These mechanistic interpretations are specific to their plasma reactor and PFAS set and, together with the negligible matrix effect for PFOA, PFOS, and HFPO‑TA, show that salts and conductivity can enhance removal of some PFAS but not others under the same treatment.

Another plasma‑based study by Eeso et al. compared PFOA and PFOS degradation in three landfill leachates, deionized water, and several groundwaters. They report that [SOURCE_TEXT_OMITTED sha256=7f058b904a6f1b43265b8f5dc205928e43588279ca0910d62bead40297cf1d4f], and those of PFOS were 64, 84, and 72%, respectively. Despite these differences, they state that “the water matrix did not have a big impact on the degradation of the two representative PFAS” and that “the small variations might be caused by factors such as the different concentrations of PFAS and PFAS precursors in the water matrix.” This explicitly frames observed differences as relatively minor matrix effects for PFOA and PFOS in their system and cautions against overinterpreting matrix‑induced changes without considering concentration and precursor differences.

For competing species beyond bulk DOM and salts, the Shaikh et al. adsorption study provides a clear example. Their selectivity study showed that “both humic acid and bentonite interact with the AC” and that “[SOURCE_TEXT_OMITTED sha256=b67e29001941a1eb273040ca12379fbf23710672dc4c9e02b05601cfedbc7144].” They conclude that “[SOURCE_TEXT_OMITTED sha256=d7c97229201ff24e1cf093e4c2ca7e816b7ea7ae123fda6504b5fd36aedec3e5],” indicating that these co‑present inorganic and organic particulates compete with PFOA for adsorption capacity. However, they also emphasize that even with these competing species, the adsorbents still offer “good PFOA removal performance under realistic scenarios,” highlighting that competition reduces but does not eliminate removal.

Ramos et al. similarly identify ions and DOC as competing species that decrease PFAS adsorption capacity and performance of carbonaceous adsorbents via pore blockage in treated municipal wastewater. Yet they observe that “the decrease in RE was almost non‑existent in the case of PFOS,” and that using a biochar with high surface area and favorable elemental ratios ([SOURCE_TEXT_OMITTED sha256=7f6b88a84d0d0ab3161fa782fe62662a8385b641019931795cb4290cd5ef35bd] competition effects existing in more complex water chemistries.” These results underline that competition effects from background solutes are not uniform across PFAS and can be partly managed by sorbent design.

Ammonia is mentioned only in the context of regeneration and not as a competing species affecting removal performance. Shaikh et al. report that to desorb PFOA by weakening electrostatic interactions from PFOA‑loaded adsorbents, they tested NaCl, NaOH, NH4Cl, KCl, and NH4OH solutions (5% w/v), and that NH4Cl and NH4OH achieved certain regeneration capacities. This speaks to the role of ammonium salts and bases in desorption during regeneration, not to their impact on PFAS removal from water. The provided evidence does not describe ammonia as altering PFAS removal efficiencies in the primary treatment step, so any inference of ammonia‑induced removal changes would go beyond the available data.

Finally, some studies explicitly limit how far their findings on background chemistry can be generalized. In addition to Eeso et al.’s statement that the water matrix did not have a big impact on PFOA and PFOS degradation and Zhang et al.’s finding that matrix effects on PFOA, PFOS, and HFPO‑TA removal were almost negligible, Franke et al. state that “comparisons to other studies should be made with care as many experimental parameters as well as water quality are often substantially different between studies.” Collectively, these caveats show that while background DOM, cations, ions, and co‑contaminants can reduce or sometimes enhance PFAS removal under specific conditions, the magnitude and direction of these effects are strongly dependent on PFAS identity, treatment technology, and detailed water chemistry, and should not be assumed to apply universally.

### Unresolved or unsupported boundaries

- The effect of ammonia (NH3/NH4+) on PFAS removal performance during treatment is not described in the supplied evidence; ammonia is only mentioned as NH4Cl and NH4OH solutions used for regeneration of PFOA-loaded adsorbents, not as competing species affecting removal.
- No evidence is provided on how background ammonia in source waters changes PFAS removal for any specific treatment technology.
- The corpus excerpts do not describe detailed mechanisms or quantitative dependencies of DOM or cation effects beyond the qualitative attributions and percentage changes explicitly quoted; additional mechanistic or kinetic generalizations would require external information.

### Complete approved source chunks

#### WF10_010_MMG001

- Role: `negative_gold`
- Document: `2023 - Eeso - Degradation of per- and polyfluoroalkyl substances in landfill leachate by a thin-water-film nonthermal plasma reactor.pdf`
- Chunk: `19`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=e9eb75b04a383c8a4d6e9f269412bb31e8d90422be1543f37b627b6599a67884].

```text
[SOURCE_TEXT_OMITTED sha256=273773eeb895766ccd1c7a2e33ac61aa1f3cf72d23b6bfef9b267e6c5e10a7bc]
```

#### WF10_010_MMG002

- Role: `optional_gold`
- Document: `2024 - Zhang - Removal of per- and polyfluoroalkyl substances from water by plasma treatment - Insights into structural effects and underlying mechanisms.pdf`
- Chunk: `32`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=98fc8b729241440ce01df295a40f57d7c9f1c21081b4e0e38dab47bda11b9ad2]).

```text
[SOURCE_TEXT_OMITTED sha256=8f631ef3ee3799bfe8d3cfbd92dce5c8209531e0e62a3504bd9593449e07092f]
```

#### WF10_010_MMG003

- Role: `required_gold`
- Document: `2023 - Shaikh - PFOA remediation from aqueous media using CTAB impregnated activated carbon - A closed-loop sustainable study with comprehensive selectivity analysis.pdf`
- Chunk: `54`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=1aa6f9833eccddbb538588103767e3f9648256b2a538bc7c634a5c708c1b43dd] %.

```text
[SOURCE_TEXT_OMITTED sha256=05d334770dbb7a80022bfb954917b37ddccaad19f4efff23523eff3af3cb0fbc]
```

#### WF10_010_MMG007

- Role: `negative_gold`
- Document: `2023 - Shaikh - PFOA remediation from aqueous media using CTAB impregnated activated carbon - A closed-loop sustainable study with comprehensive selectivity analysis.pdf`
- Chunk: `55`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=846230eb9f9d4dba0fd0a2328eb600d9d4277d7b011d6a517d4f785e70215983] .

```text
[SOURCE_TEXT_OMITTED sha256=2bb50e6a8c0f8c6f8bc73067fda445aa1f9a71c7caaa9f3814e2c2359405d559]
```

#### WF10_010_MMG009

- Role: `required_gold`
- Document: `2024 - Taher - Progress on remediation of per - and polyfluoroalkyl substances (PFAS) from water and wastewater using membrane technologies - A review.pdf`
- Chunk: `14`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=ba574a1b6c97564b21e719e36b5690da9ffde3d635d98c33064de79c56dfb12e].

```text
[SOURCE_TEXT_OMITTED sha256=8c8ceb8faeed5ff7f0a43f4d301480fa51c18338ef1c9bc4c25efa27af93df01]
```

#### WF10_010_MMG010

- Role: `negative_gold`
- Document: `2025 - Ramos - Biochar selection for removal of perfluoroalkyl substances from reclaimed water for agricultural irrigation.pdf`
- Chunk: `39`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=c9405a41a4f5d635e0a38994a329ac9ab7359f1de8c09020a11b08aae48ba1e0].

```text
[SOURCE_TEXT_OMITTED sha256=65d4f2157d461dc7d923120e6e5dfb1a02734733697c744fd773090292f2ff5b]
```

#### WF10_010_MMG011

- Role: `optional_gold`
- Document: `2019 - Franke - Efficient removal of per- and polyfluoroalkyl substances (PFASs) in drinking water treatment - nanofiltration combined with active carbon or anion.pdf`
- Chunk: `14`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=6d7ba27c1f7a129a6362d14a0419d48be81c2c7d74b747dbc567b8192906e765].

```text
[SOURCE_TEXT_OMITTED sha256=c81f5bc71f1de1087af297d1dc5ceddb9bc929b2bbb33bc0afb40b84e3343ea5]
```

### Deterministic resolution

- {'claim_group_id': 'WF10_010-G02', 'evidence_id': 'WF10_010_MMG010', 'action': 'restored_original_chunk_whitespace', 'old_span_sha256': 'd98334322ed15d5387656b2ca96f13b03494c881de2a8663e81599a8ff6863c6', 'new_span_sha256': 'a986d75d348986b1d0bb34d2b48fb8fc77ba630d845171a2f2a4438bd8b45471'}
- {'claim_group_id': 'WF10_010-G04', 'evidence_id': 'WF10_010_MMG010', 'action': 'restored_original_chunk_whitespace', 'old_span_sha256': 'd98334322ed15d5387656b2ca96f13b03494c881de2a8663e81599a8ff6863c6', 'new_span_sha256': 'a986d75d348986b1d0bb34d2b48fb8fc77ba630d845171a2f2a4438bd8b45471'}

---

## WF10_011

**Question:** How can applied potential affect PFAS adsorption, removal, or transformation in electrochemical treatment systems?

### Task components

- `WF10_011-T01`: Extract how applied potential influences PFAS adsorption behavior in electrochemical treatment systems, focusing specifically on adsorption-related endpoints (e.g., adsorption rate, adsorption capacity, or electro-sorption) and clearly distinguishing these from removal, degradation, defluorination, mineralization, destruction, byproduct formation, and overall mass-balance outcomes.
- `WF10_011-T02`: Extract how applied potential affects regeneration of the adsorbing or electrode surface in electrochemical PFAS treatment (e.g., desorption or restoration of adsorption capacity), again keeping regeneration and adsorption endpoints clearly separated from degradation, defluorination, mineralization, destruction, byproduct formation, and mass-balance evidence.

### Normative claim groups

#### WF10_011-G01

- Component: `WF10_011-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In PFAS electro-adsorption systems, increasing the applied voltage generally increases the PFAS adsorption performance or adsorption capacity of the electrode.
- Full: Award full credit if the answer states that, in electro-adsorption of PFAS, increasing the applied voltage tends to increase adsorption performance or capacity of the electrode, explicitly as a voltage effect and framed as adsorption (not degradation or overall removal), consistent with the review statement.
- Partial: Award partial credit if the answer links applied voltage to improved PFAS capture or performance in electro-adsorption but is vague about whether this is specifically adsorption capacity or does not clearly distinguish adsorption from other endpoints.
- Contradiction: Mark contradiction if the answer claims that applied voltage has no effect or generally decreases PFAS adsorption performance in electro-adsorption systems, without restriction to exceptional cases.
- Linked exact evidence:
  - `WF10_011_MMG003` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=ac35e072800a5c5a24dad0c467da993ca2e934ec8f2fc39916616fca732c5bf5];
    Supports: Shows that, in electro-adsorption, increasing applied voltage generally increases PFAS adsorption performance and improves adsorption capacity of the electrode.

#### WF10_011-G02

- Component: `WF10_011-T01`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: Application of an anodic bias in electro-adsorption substantially increases the initial adsorption rate and adsorption capacity for PFOA compared to non-biased or non-electrified adsorbent suspensions, illustrating that specific applied potentials can dramatically enhance electro-adsorption performance.
- Full: Award full credit for this group if the answer notes that applying an electrochemical potential to an electrode (relative to a comparable non-biased or suspended sorbent) can greatly increase the initial adsorption rate and adsorption capacity for PFOA, indicating a strong enhancement of adsorption due to applied potential.
- Partial: Award partial credit if the answer mentions that a biased electrode shows higher adsorption rate or capacity than an un-biased material but does not clearly tie this difference to the applied potential condition.
- Contradiction: Mark contradiction if the answer asserts or implies that adding an applied potential to the electrode has little or no effect compared with suspended adsorbent in this context, or that it reduces adsorption rate and capacity relative to the suspended material.
- Linked exact evidence:
  - `WF10_011_MMG005` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=9578fb7f427c743c2a3bb1e7c34368ed58b7c1204931cf055097be49fef367da].
    Supports: Shows that when a potential is applied to an MWCNT electrode (0.6 V), the initial adsorption rate and adsorption capacity for PFOA are much higher than for suspended MWCNT powder, indicating strong enhancement of adsorption by applied potential.

#### WF10_011-G03

- Component: `WF10_011-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In the cited electro-adsorption study, applying a negative bias desorbed bound PFOA through charge repulsion and achieved more than 80% regeneration at -1.5 V.
- Full: Award full credit if the answer states that applying a negative bias caused charge-repulsion-driven desorption of bound PFOA and thereby regenerated the electrode in the reported system; the reported >80% regeneration at -1.5 V may be included.
- Partial: Award partial credit if the answer links negative or reversed bias to PFOA desorption or electrode regeneration but omits the charge-repulsion explanation or the condition-specific nature.
- Contradiction: Mark contradiction if the answer states that negative bias prevented PFOA desorption or regeneration in the cited system.
- Linked exact evidence:
  - `WF10_011_MMG003` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=8c0a329bd5b2931b954895c97666900e1e206abbbcbb85abb683777b435b8b98])).
    Supports: Reports charge-repulsion-driven desorption of bound PFOA under negative bias and >80% regeneration at -1.5 V.

#### WF10_011-X01

- Component: `WF10_011-T01`
- Importance: `supplementary`
- Scoring role: `constraint_only`
- Proposition: High applied potentials in electro-oxidation systems are discussed in the context of PFAS degradation via electron transfer to the anode, not adsorption or electro-sorption behavior.
- Full: Use this constraint to ensure that statements about high applied potential in electro-oxidation, where the main pathway is electron transfer and degradation, are not misrepresented as adsorption or electro-sorption effects.
- Partial: Partially apply this constraint if the answer loosely associates high potentials with performance improvements without clearly separating degradation from adsorption, but does not explicitly conflate them.
- Contradiction: Mark contradiction to this constraint if the answer explicitly treats the high-potential electro-oxidation evidence as demonstrating adsorption capacity or adsorption-rate behavior.
- Linked exact evidence:
  - `WF10_011_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=deda6642a0584bf66f59f5ecdd58b032b626a7117667dae4366ff94516879a46].
    Supports: Indicates that the role of high applied potential here is to induce electron transfer leading to PFAS degradation, not to control adsorption performance.

#### WF10_011-X02

- Component: `WF10_011-T01`
- Importance: `supplementary`
- Scoring role: `constraint_only`
- Proposition: Evidence on current density in electro-oxidation and EO-UV systems addresses PFAS degradation and removal efficiencies, not adsorption or electrode-sorption behavior.
- Full: Use this constraint to prevent misinterpretation of current-density effects on degradation in EO or EO-UV systems as adsorption behavior.
- Partial: Partially apply if the answer generically links current density to performance without specifying degradation versus adsorption endpoints.
- Contradiction: Mark contradiction if the answer explicitly cites this degradation-focused evidence as showing changes in adsorption rate or capacity.
- Linked exact evidence:
  - `WF10_011_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=856efcd21bf1846c42d4bf00a1c774835ab22b09800f2f445989e8a6bd89405d] ].
    Supports: Clarifies that the current density discussion is about electrochemical degradation, not adsorption.
  - `WF10_011_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=856efcd21bf1846c42d4bf00a1c774835ab22b09800f2f445989e8a6bd89405d] ].
    Supports: Specifies that the performance metric under varying current density is degradation efficiency via electron transfer, not adsorption performance.

#### WF10_011-X03

- Component: `WF10_011-T01`
- Importance: `supplementary`
- Scoring role: `constraint_only`
- Proposition: Applied voltage in electrocoagulation removes dissolved PFAS in flocs due to affinity with colloidal particles, representing a coagulation/aggregation mechanism rather than adsorption onto an electro-adsorption electrode.
- Full: Use this constraint to ensure that voltage effects causing PFAS removal via electrocoagulation flocs are not mischaracterized as adsorption rate or capacity changes on an electro-adsorption electrode.
- Partial: Partially apply if the answer mentions electrocoagulation removal under applied voltage but is ambiguous about whether this is adsorption versus flocculation.
- Contradiction: Mark contradiction if the answer explicitly describes this floc-based removal as increased adsorption capacity or electro-sorption on the electrode.
- Linked exact evidence:
  - `WF10_011_MMG006`
    > [SOURCE_TEXT_OMITTED sha256=249f86ab0d2da4b3c2676cbf25933198c218250572064adb3aba60758e5482be].
    Supports: Shows that applied voltage drives removal via formation of flocs in electrocoagulation, involving affinity to colloidal particles rather than adsorption to an electro-adsorption electrode.

#### WF10_011-X04

- Component: `WF10_011-T01`
- Importance: `supplementary`
- Scoring role: `constraint_only`
- Proposition: Higher applied voltage in electro-adsorption can improve PFAS removal, but voltage selection is also constrained by water hydrolysis and energy considerations; this statement is about overall removal optimization, not specifically adsorption rate or capacity.
- Full: Use this constraint to avoid overgeneralizing improved PFAS removal at higher voltages as purely adsorption-rate or capacity changes, and to note that operational voltage is limited by water hydrolysis and energy efficiency.
- Partial: Partially apply if the answer mentions that higher voltage improves PFAS capture but omits that voltages above the water hydrolysis potential are discouraged for energy reasons.
- Contradiction: Mark contradiction if the answer suggests that there is no upper constraint related to water hydrolysis or implies that removal efficiency keeps increasing without such limitation.
- Linked exact evidence:
  - `WF10_011_MMG004` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=222bc341a17f44b4f87373839897b07a3d82f7fae6835a365b43c70369e1dd22]).
    Supports: Indicates that higher applied voltage improves PFAS removal but also notes a recommended upper bound (below the water hydrolysis voltage) for energy efficiency, framing this as an operational removal consideration.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

In electro-adsorption-based PFAS treatment, the applied potential has a clear influence on adsorption behavior.

For adsorption behavior (Task T01), the review on electrochemical PFAS decontamination states that, under electro-adsorption conditions, ". . . the PFAS adsorption performance of an electrode increases with the increase of the applied voltage," and that this is associated with an improvement in the "adsorption capacity of the electrode" due to changes in the electrical double layer at the electrode–solution interface.[WF10_011_MMG003] This establishes that higher applied voltage generally enhances PFAS electro-adsorption performance and increases adsorption capacity, within the electro-adsorption operating window.

A specific example further illustrates the impact of applied potential on adsorption rate and capacity. For PFOA, the review reports that, compared with suspended MWCNT powder, an MWCNT electrode operated at an applied bias (0.6 V) shows a much higher initial adsorption rate and adsorption capacity.[WF10_011_MMG005] The paired values for the suspended powder and for the biased electrode demonstrate that imposing an electrochemical potential on the electrode can greatly enhance both the rate and capacity of PFOA adsorption compared with a non-electrified sorbent.

For regeneration behavior (Task T02), the same review reports that bound PFOA was effectively desorbed by charge repulsion when a negative bias was applied, with more than 80% regeneration at -1.5 V.[WF10_011_MMG003] This is a potential-controlled desorption and electrode-regeneration result, not evidence of PFAS degradation or mineralization.

Other parts of the supplied evidence discuss how high applied potentials in electro-oxidation drive electron-transfer-based degradation,[WF10_011_MMG001, WF10_011_MMG002] or how applied voltage in electrocoagulation leads to PFAS removal via floc formation with colloidal particles,[WF10_011_MMG006] and how higher voltage can improve overall PFAS removal but is limited by water hydrolysis and energy efficiency.[WF10_011_MMG004] These statements concern degradation, bulk removal, or coagulation and are separate from the adsorption-rate and adsorption-capacity effects of applied potential described for electro-adsorption systems.

### Unresolved or unsupported boundaries

- The supplied evidence does not provide a general quantitative relationship (e.g., functional form) between applied potential and adsorption rate or capacity beyond the specific examples given.
- The evidence does not detail how applied potential affects adsorption selectivity among different PFAS beyond example comparisons, nor does it generalize to all PFAS chemistries or all electrode materials.
- No explicit mass-balance closure or byproduct formation data related to adsorption steps under varying potential are provided in the supplied spans.

### Complete approved source chunks

#### WF10_011_MMG001

- Role: `required_gold`
- Document: `2023 - Unknown - Recent advances in electrochemical decontamination of perfluorinated compounds from water - a review.pdf`
- Chunk: `55`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=bfe3ece53ebc9499745531e564271f958213762763fb3eea8b2f2229351e5586].

```text
[SOURCE_TEXT_OMITTED sha256=3362b3fab37f5b1067c3e75a6de8b0e9645adb1c9ab8a8a6f64e879b90eda707].
```

#### WF10_011_MMG002

- Role: `optional_gold`
- Document: `2023 - Uwayezu - Combining electrochemistry and ultraviolet radiation for the degradation of per - and poly-fluoroalkyl substances in contaminated groundwater and.pdf`
- Chunk: `23`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=856efcd21bf1846c42d4bf00a1c774835ab22b09800f2f445989e8a6bd89405d] ].

```text
[SOURCE_TEXT_OMITTED sha256=ae2f5cd6abfb3b5df78acc2abca34fc2bcf291077ec927ae78fe6cee89449a16]
```

#### WF10_011_MMG003

- Role: `required_gold`
- Document: `2023 - Unknown - Recent advances in electrochemical decontamination of perfluorinated compounds from water - a review.pdf`
- Chunk: `33`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=9d5826ccd99915f8ff7982323dd157bc8ef1d7573421a3dc30b662ce037d7ff4];

```text
[SOURCE_TEXT_OMITTED sha256=640cea6e361aab8613f784f2a7cbf6e024c0560f0f21c67d5d4ec27423e8d1ae]
```

#### WF10_011_MMG004

- Role: `optional_gold`
- Document: `2023 - Unknown - Recent advances in electrochemical decontamination of perfluorinated compounds from water - a review.pdf`
- Chunk: `34`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=a61236dae2b44b9dfac7b4c15cb7d02b40e031c1c2a4deec6cf91ad3c7e82cc8]).

```text
([SOURCE_TEXT_OMITTED sha256=6a0f907532668d4b1f8308c70aaea1986ee701ed67bfc7a1d0c6d7dad37fa586]
```

#### WF10_011_MMG005

- Role: `optional_gold`
- Document: `2023 - Unknown - Recent advances in electrochemical decontamination of perfluorinated compounds from water - a review.pdf`
- Chunk: `31`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=6570455a88c39de5fe7e07f03b2a47c71c9c31059f99a1f9b71cb70a0894a09a].

```text
[SOURCE_TEXT_OMITTED sha256=606ca5b608658394b81675642d88468b6f7726766f04b896a06a64405fc2873f]).
```

#### WF10_011_MMG006

- Role: `optional_gold`
- Document: `2023 - Sivagami - Electrochemical-based approaches for the treatment of forever chemicals - Removal of perfluoroalkyl and polyfluoroalkyl substances (PFAS) from.pdf`
- Chunk: `62`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=249f86ab0d2da4b3c2676cbf25933198c218250572064adb3aba60758e5482be].

```text
[SOURCE_TEXT_OMITTED sha256=4711151d72f28d2817d271698b6e1c4a6cc5f59c253713e5b7ae72cfa0afc20b]
```

### Deterministic resolution

- {'claim_group_id': 'WF10_011-G01', 'evidence_id': 'WF10_011_MMG003', 'action': 'restored_original_chunk_whitespace', 'old_span_sha256': '146a770f326d32a89079354d3a1ea74b7068a6bcb81a9989bdf4568e940e2c37', 'new_span_sha256': '7488c693a31f4141a559094df922e8e70e9b87e2ae31894bae4f36655daa4802'}
- {'claim_group_id': 'WF10_011-G02', 'evidence_id': 'WF10_011_MMG005', 'action': 'restored_original_chunk_whitespace', 'old_span_sha256': 'acb8382955141fbe69379b225dcc92b75810828317f56d83c3bdc2c072c89b1c', 'new_span_sha256': 'b3f834124d4cb1d6d4b94f4f60c906bcd86b860694d3a6c0bf62eb13d6ecd85b'}
- {'claim_group_id': 'WF10_011-X01', 'evidence_id': 'WF10_011_MMG001', 'action': 'restored_original_chunk_whitespace', 'old_span_sha256': '287525ee51953c9eecbda6ca636dbfd81a23a2c5dea8442d9bad5bcce70b8800', 'new_span_sha256': 'b697b5f83b2c5e3c92501f06cdc6eff3e87288d8a2f511ba119c9096e3b1a8f5'}
- {'claim_group_id': 'WF10_011-X04', 'evidence_id': 'WF10_011_MMG004', 'action': 'restored_original_chunk_whitespace', 'old_span_sha256': 'e6adadde5afd0320f690be93f3a269639e4359f8a6a4e7084ea28244ab183a50', 'new_span_sha256': '6bbf68ea2efa05a6f13d34283a78d2ee14d814463deca8f8cd9c9a34ab32b3dc'}
- Added core regeneration group WF10_011-G03 from a verbatim approved full-chunk sentence and restored atomic disposition WF10_011-A03.
- Updated answerability, unresolved boundaries, prose, and claim map to cover Task T02 without conflating regeneration with destruction endpoints.

---

## WF10_012

**Question:** How do membrane modifications affect reported PFOA rejection, and what limits interpretation of those improvements?

### Task components

- `WF10_012-T01`: Extract how the base membrane was modified with PVA/MOF layers, including any described protocol steps and the reagents/materials used for the modification, without adding details that are not explicitly stated.
- `WF10_012-T02`: Extract the reported impact of adding PVA/MOF layers on PFOA rejection, including the operating conditions, water matrix (if stated), and the target compound(s) with emphasis on PFOA, without inventing numeric values or additional compounds.
- `WF10_012-T03`: Extract any reported limitations, caveats, or factors that constrain interpretation of the observed PFOA rejection improvements after membrane modification (e.g., condition-specificity, matrix effects, or measurement constraints), ensuring these are taken only from explicitly stated information and not generalized into universal PFAS treatment claims.

### Normative claim groups

#### WF10_012-G01

- Component: `WF10_012-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Incorporation of MXene–TiO2 composites into polyamide RO membranes increased PFOA rejection compared to the unmodified membrane under the reported test conditions.
- Full: Award full credit if the answer states that incorporation of MXene–TiO2 composites into the polyamide RO membrane increased PFOA rejection compared to the unmodified membrane, indicating enhanced PFOA rejection for all modified membranes and explicitly noting that maximum PFOA rejection was achieved for a modified membrane (M3) compared to M0.
- Partial: Award partial credit if the answer mentions that MXene–TiO2 modification improved PFOA rejection but does not clearly indicate that all modified membranes showed enhanced PFOA rejection relative to the unmodified membrane, or omits the comparison to M0.
- Contradiction: Flag a contradiction if the answer claims that MXene–TiO2 modification did not change or reduced PFOA rejection relative to the unmodified membrane, or suggests that PFOA rejection was not enhanced in the modified membranes.
- Linked exact evidence:
  - `WF10_012_MMG001`
    > All modified membranes exhibited significantly enhanced PFOA rejection ( Fig.
    Supports: Shows that all modified membranes had significantly enhanced PFOA rejection compared to the unmodified membrane M0, with the maximum rejection observed for a modified membrane (M3).
  - `WF10_012_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=c1ef2c44d781ef80c8eece382738313e2bcf6cc5e19cff735abdb469ad870b22].
    Supports: States that incorporation of MXene–TiO2 composites into the thin-film (polyamide) layers introduces additional surface negative charge and 2D nanochannel-like interfaces that further impede PFOA transport while facilitating water flux.
  - `WF10_012_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=ce46158b8ad7b6b5680ff66bb33360c0d6b776b251e42af969c01b9820916fce]%).
    Supports: Indicates that even at higher composite loading (M4), PFOA rejection remained high and only slightly lower than M3, reinforcing that modified membranes maintained strong PFOA rejection.

#### WF10_012-G02

- Component: `WF10_012-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Surface coatings and functionalizations such as polydopamine and polyethyleneimine have been reported to improve PFOA rejection in membrane processes under the tested conditions.
- Full: Award full credit if the answer states that polydopamine coating and PEI functionalization increased PFOA rejection, noting that PDA coating enhanced PFOA rejection and that PEI-functionalized GO membranes increased PFOA retention and water permeance.
- Partial: Award partial credit if the answer mentions only one of these modifications (either PDA or PEI) or states that surface functionalization improved PFOA rejection without specifying which modification.
- Contradiction: Flag a contradiction if the answer claims that PDA coating or PEI functionalization decreased PFOA rejection or had no effect on PFOA rejection.
- Linked exact evidence:
  - `WF10_012_MMG003`
    > For example, the PDA-coated membrane can enhance PFOA rejection by 20 %.
    Supports: Shows that applying a polydopamine coating improved removal of PFOA and that the PDA-coated membrane enhanced PFOA rejection by 20%.
  - `WF10_012_MMG004`
    > [[SOURCE_TEXT_OMITTED sha256=f7b7473d04d89e83a9b8de116cc8dbbcaac4754d3b3611d80e7803ca9a216b10].
    Supports: Shows that functionalizing a graphene oxide membrane surface with polyethyleneimine significantly increased PFOA retention and also increased water permeance.

#### WF10_012-G03

- Component: `WF10_012-T03`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Reported removal efficiencies for PFOA vary across different membrane distillation studies, indicating that PFOA rejection improvements are highly system- and condition-specific.
- Full: Award full credit if the answer notes that in membrane distillation, reported PFOA removal efficiencies vary across articles, implying that performance is not uniform and depends on study-specific factors.
- Partial: Award partial credit if the answer only states that PFOA removal in membrane distillation can be low or variable, without explicitly linking this to variation across different articles.
- Contradiction: Flag a contradiction if the answer claims that PFOA removal efficiencies in membrane distillation are consistent across studies or presents them as uniform.
- Linked exact evidence:
  - `WF10_012_MMG005`
    > In addition, even for the same substance, the reported removal efficiencies vary across different articles.
    Supports: Indicates that membrane distillation shows <60% removal for PFOA and that for the same substance, reported removal efficiencies vary between articles, highlighting variability and condition-specificity.

#### WF10_012-G04

- Component: `WF10_012-T03`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Fouling is a common limitation in membrane technologies and can reduce removal performance over time, constraining interpretation of initial PFOA rejection improvements.
- Full: Award full credit if the answer states that fouling commonly reduces removal performance over time in membrane technologies, and identifies this as a general limitation that affects interpretation of removal efficiencies.
- Partial: Award partial credit if the answer mentions fouling as a limitation but does not clearly connect it to reduced removal performance over time.
- Contradiction: Flag a contradiction if the answer claims that fouling does not affect removal performance over time or is not a relevant limitation for membrane-based contaminant removal.
- Linked exact evidence:
  - `WF10_012_MMG006`
    > [SOURCE_TEXT_OMITTED sha256=127e9dbc7e45202a80e5e3fc810a457adbd2b5e5a3311098199b4fa587403925].
    Supports: Directly states that reduction of removal performance over time due to fouling is a common limitation in membrane technologies.

#### WF10_012-G05

- Component: `WF10_012-T03`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: Natural organic matter such as humic acid can have complex and sometimes opposing effects on PFAS rejection, which complicates interpretation of rejection improvements observed in modified membranes.
- Full: Award full credit if the answer states that humic acid (as a form of natural organic matter) can either enhance or reduce PFAS rejection, and that this makes the influence of natural organic matter on PFAS rejection more complex than that of inorganic ions such as Ca2+.
- Partial: Award partial credit if the answer generally mentions that natural organic matter or humic acid affects PFAS rejection but does not clearly note that the effect can be both positive and negative.
- Contradiction: Flag a contradiction if the answer asserts that humic acid or natural organic matter has a simple, uniformly positive or negative effect on PFAS rejection, ignoring the explicitly described bidirectional influence.
- Linked exact evidence:
  - `WF10_012_MMG007`
    > [SOURCE_TEXT_OMITTED sha256=67ddcd6ac8d6fe66fc04d6079e061ca71168ba191d231d145dfd1b103ab3f668]] .
    Supports: States that the influence of humic acid on PFAS rejection is complex, with some studies showing higher rejection and others lower rejection in its presence, and compares this complexity to the simpler effect of Ca2+.
  - `WF10_012_MMG007`
    > [SOURCE_TEXT_OMITTED sha256=67ddcd6ac8d6fe66fc04d6079e061ca71168ba191d231d145dfd1b103ab3f668]] .
    Supports: Explains mechanistically that humic acid can increase PFAS rejection by forming large aggregates, but can also reduce rejection by competing for adsorption sites, reinforcing the bidirectional effect.

#### WF10_012-X01

- Component: `WF10_012-T02`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: Findings about PFOA rejection improvements from MXene–TiO2, PDA, PEI, or MD-related studies cannot be generalized to PVA/MOF-modified membranes or to universal PFAS treatment performance.
- Full: Answers must not treat the reported PFOA rejection improvements for MXene–TiO2-modified RO, PDA-coated membranes, PEI-functionalized GO membranes, or specific MD systems as universally representative of PVA/MOF-modified membranes or PFAS removal in general. They must recognize that these results are tied to the specific membrane materials, modifications, and conditions studied.
- Partial: If the answer is otherwise accurate but implicitly suggests broad generality (e.g., that membrane modification will always greatly improve PFOA or PFAS rejection) without explicitly naming PVA/MOF, treat this as a minor issue but do not award content credit based on such generalization.
- Contradiction: Flag a constraint violation if the answer explicitly claims that the reported MXene–TiO2, PDA, PEI, or MD results directly describe PVA/MOF layer performance or universally characterize PFAS removal across all membranes and conditions.
- Linked exact evidence:
  - `WF10_012_MMG001`
    > All modified membranes exhibited significantly enhanced PFOA rejection ( Fig.
    Supports: Shows that improved PFOA rejection is linked to a specific modification: incorporation of MXene–TiO2 composites into the thin-film layer.
  - `WF10_012_MMG003`
    > For example, the PDA-coated membrane can enhance PFOA rejection by 20 %.
    Supports: Shows that performance changes are tied to a specific PDA coating applied in a particular study.
  - `WF10_012_MMG004`
    > [[SOURCE_TEXT_OMITTED sha256=f7b7473d04d89e83a9b8de116cc8dbbcaac4754d3b3611d80e7803ca9a216b10].
    Supports: Shows that the reported improvement concerns a specific GO membrane functionalized with PEI.
  - `WF10_012_MMG005`
    > In addition, even for the same substance, the reported removal efficiencies vary across different articles.
    Supports: Indicates that removal efficiencies, even for the same compound, vary between studies, underscoring the lack of universal behavior.
  - `WF10_012_MMG007`
    > [SOURCE_TEXT_OMITTED sha256=67ddcd6ac8d6fe66fc04d6079e061ca71168ba191d231d145dfd1b103ab3f668]] .
    Supports: Shows that even matrix effects on PFAS rejection differ among studies, reinforcing that findings are not universally generalizable.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

Across the provided studies, several membrane modifications are reported to increase PFOA rejection, although none of the excerpts describe PVA/MOF layers specifically.

For reverse osmosis, incorporation of MXene–TiO2 composites into the thin‑film polyamide layer enhanced PFOA rejection relative to the unmodified membrane. The RO study notes that “All modified membranes exhibited significantly enhanced PFOA rejection … compared to M 0, with M 3 reaching a maximum rejection of 98.8 ± 0.3%,” and attributes this to the incorporation of MXene–TiO2 composites into the thin‑film layers, which “[SOURCE_TEXT_OMITTED sha256=1cbaf27037dad076116a8c93a310afd7f70ea202dbff69fe9e0f986d91895c4b].”

Other surface modifications also improved PFOA removal. A review reports that polydopamine coating was applied “to improve the removal of organic micropollutants including PFOA and PFOS,” with the example that “the PDA-coated membrane can enhance PFOA rejection by 20%.” Another study on graphene oxide membranes states that functionalizing “the GO membrane surface with polyethyleneimine (PEI)… significantly enhanced both PFOA retention … and water permeance.” These examples show that different chemical modifications of membrane surfaces (MXene–TiO2 incorporation, PDA coating, PEI functionalization) can all lead to increased PFOA rejection under their respective test conditions.

The evidence set, however, does not include protocols, reagents, or operating conditions for PVA/MOF layer modifications, so no PVA/MOF-specific preparation steps or performance data can be extracted from these excerpts. The described modification methods are limited to MXene–TiO2 incorporation into RO thin‑film layers, polydopamine surface coatings, and PEI functionalization of graphene oxide membranes.

Several limitations and context factors constrain how these PFOA rejection improvements should be interpreted. A review of membrane distillation reports that removal efficiencies are highly variable: “MD exhibits different retention efficiencies … [SOURCE_TEXT_OMITTED sha256=f871c04585c01260ea54ef04d138ee5b5d9c0bc73687fed4d8fc72b1e136c78d].” This indicates that PFOA removal performance is strongly system‑ and condition‑specific and cannot be assumed to be uniform across membranes or studies.

A broader review of membrane technologies identifies fouling as a common performance limitation, noting that “The reduction of removal performance over time by observed fouling issues is determined to be a common limitation in membrane technologies.” This means that even when a modification initially improves PFOA rejection, fouling can reduce effective removal over time, complicating direct comparison of short‑term rejection data.

Matrix effects, particularly from natural organic matter, add additional complexity. In the MXene–TiO2 RO study, the authors state that “the influence of HA on PFAS rejection appears to be more complex than that of inorganic ions like Ca2+ [SOURCE_TEXT_OMITTED sha256=de52090d7928123c7000bab3204f7946e1681cdd392abf6f27f832240b07cb7a],” and further explain that humic acid “[SOURCE_TEXT_OMITTED sha256=0e60a060965f6a32b21269c4f6a5494f5c50ad7bd05daf4b896fb0263557d403].” These observations highlight that the presence of humic substances or other natural organic matter can either increase or decrease PFAS rejection depending on conditions, making it difficult to generalize PFOA rejection improvements observed in clean or simplified matrices to more complex waters.

Taken together, the provided evidence supports that specific membrane modifications—such as MXene–TiO2 incorporation into RO thin‑film layers, polydopamine coatings, and PEI functionalization of GO—can enhance PFOA rejection under the conditions tested. Interpretation of these improvements is limited by study‑specific factors including the particular modification chemistry, the membrane process used, variability of reported efficiencies across studies, fouling‑induced performance decline over time, and complex matrix effects from natural organic matter. No conclusions can be drawn from these excerpts about PVA/MOF modification protocols or their impact on PFOA rejection.

### Unresolved or unsupported boundaries

- How the base membrane was modified with PVA/MOF layers, including specific protocol steps, reagents, and materials used for PVA/MOF modification.
- The quantitative or qualitative impact of adding PVA/MOF layers on PFOA rejection, including any PVA/MOF-specific operating conditions or water matrices.
- Any PVA/MOF-specific limitations, caveats, or matrix effects on PFOA rejection that are not explicitly described in the provided evidence.

### Complete approved source chunks

#### WF10_012_MMG001

- Role: `required_gold`
- Document: `2026 - Ghanbari - Harnessing phase engineered porous MXene-TiO2 in polyamide reverse osmosis membranes for enhanced short- and long chain PFAS removal from water.pdf`
- Chunk: `53`
- Registered exact span: All modified membranes exhibited significantly enhanced PFOA rejection ( Fig.

```text
[SOURCE_TEXT_OMITTED sha256=1d7be2fc3460fa9273bf22b40893f6984c36de80f4ed9888e029c82101ba2d6f]
```

#### WF10_012_MMG002

- Role: `required_gold`
- Document: `2026 - Ghanbari - Harnessing phase engineered porous MXene-TiO2 in polyamide reverse osmosis membranes for enhanced short- and long chain PFAS removal from water.pdf`
- Chunk: `54`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=ce46158b8ad7b6b5680ff66bb33360c0d6b776b251e42af969c01b9820916fce]%).

```text
[SOURCE_TEXT_OMITTED sha256=0ade209382545b6e5549d59505e9e8ad4e864a290e88a3bb3b5c768a16bc0f20].
```

#### WF10_012_MMG003

- Role: `optional_gold`
- Document: `2022 - Liu - Evaluating the efficiency of nanofiltration and reverse osmosis membrane processes for the removal of per- and polyfluoroalkyl substances from water.pdf`
- Chunk: `40`
- Registered exact span: For example, the PDA-coated membrane can enhance PFOA rejection by 20 %.

```text
[SOURCE_TEXT_OMITTED sha256=86bc82dc547c85136969e2a4b7c79559bb4741efbf053b9d44be9962f5aa76ae]
```

#### WF10_012_MMG004

- Role: `optional_gold`
- Document: `2025 - Pla - Removal of PFAS from complex matrix water by filtration with supported graphene oxide membranes.pdf`
- Chunk: `27`
- Registered exact span: [[SOURCE_TEXT_OMITTED sha256=f7b7473d04d89e83a9b8de116cc8dbbcaac4754d3b3611d80e7803ca9a216b10].

```text
[SOURCE_TEXT_OMITTED sha256=4f1da0f2f582bd117cd7786e5a44944cf594c7ef81bfb1c8a7b91bba4d4e9078]] .
```

#### WF10_012_MMG005

- Role: `optional_gold`
- Document: `2025 - Wu - Membrane distillation system for treatment of emerging contaminants in water - Enhancement of removal efficiency and mitigation of membrane fouling.pdf`
- Chunk: `5`
- Registered exact span: In addition, even for the same substance, the reported removal efficiencies vary across different articles.

```text
[SOURCE_TEXT_OMITTED sha256=18b2a5624b817441bf7c4c30975e2c0ae5402543fdfb7e18e1759c06793a68a1]
```

#### WF10_012_MMG006

- Role: `optional_gold`
- Document: `2026 - Gulver - Efficient removal of per-polyfluoroalkyl substances (PFAS) from water by using membrane distillation technology - a review.pdf`
- Chunk: `45`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=127e9dbc7e45202a80e5e3fc810a457adbd2b5e5a3311098199b4fa587403925].

```text
[SOURCE_TEXT_OMITTED sha256=659781828301e2adb8a603030986761425a6887e6bd4abe1f77a21957a305af7]
```

#### WF10_012_MMG007

- Role: `optional_gold`
- Document: `2026 - Ghanbari - Harnessing phase engineered porous MXene-TiO2 in polyamide reverse osmosis membranes for enhanced short- and long chain PFAS removal from water.pdf`
- Chunk: `62`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=67ddcd6ac8d6fe66fc04d6079e061ca71168ba191d231d145dfd1b103ab3f668]] .

```text
[SOURCE_TEXT_OMITTED sha256=a5073e1f92e57af3b992c710f3e42264b2561ccea33986744e85e6a1bc030ce2]
```

---

## WF10_013

**Question:** When evaluating electrochemical treatment of PFAS-contaminated landfill leachate, what transformation-product behavior should be checked in addition to parent-compound loss?

### Task components

- `WF10_013-T01`: Identify what precursor-related transformation signals (e.g., formation or depletion of PFAS precursors or intermediate products) should be checked in electrochemical treatment of PFAS-contaminated landfill leachate beyond simple parent-compound loss, noting any limitations or uncertainties in interpreting these signals.
- `WF10_013-T02`: Identify what product- and chain-shortening-related signals (e.g., appearance, accumulation, or persistence of transformation products and shorter-chain PFAS) should be checked in electrochemical treatment of PFAS-contaminated landfill leachate beyond simple parent-compound loss, including any caveats or negative evidence that constrain broader treatment claims.

### Normative claim groups

#### WF10_013-G01

- Component: `WF10_013-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In electrochemical treatment of landfill leachate, reviewers should explicitly consider the extent to which PFBA is degraded, rather than only reporting parent-compound loss.
- Full: Award full credit if the answer notes that, for electrochemical treatment of landfill leachate, the extent to which PFBA is degraded has to be explicitly considered when interpreting treatment performance, rather than focusing only on loss of initially targeted PFAS.
- Partial: Award partial credit if the answer mentions the need to consider degradation or persistence of PFBA (or an equivalent short-chain PFCA) in evaluating electrochemical treatment, but does not clearly frame this as an additional check beyond parent-compound loss or does not explicitly tie it to landfill leachate.
- Contradiction: Flag contradiction if the answer suggests that the extent of PFBA degradation does not need to be considered when evaluating electrochemical treatment of landfill leachate, or that persistence of PFBA is irrelevant to treatment performance.
- Linked exact evidence:
  - `WF10_013_MMG002`
    > Therefore, the extent to which PFBA should be degraded has to be considered for practical purposes.
    Supports: Directly states that the extent to which PFBA should be degraded has to be considered, supporting the need to explicitly evaluate PFBA degradation when assessing electrochemical treatment performance.

#### WF10_013-G02

- Component: `WF10_013-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In electrochemical oxidation of PFAS-contaminated landfill leachate and groundwater, reviewers should monitor the formation and behavior of transformation products, including PFAS, using suspect and non-targeted screening tools, rather than only tracking parent-compound loss.
- Full: Award full credit if the answer explains that, beyond loss of initially targeted PFAS, evaluation of electrochemical oxidation of landfill leachate and groundwater should include monitoring of PFAS transformation products during EO treatment and should make use of suspect and non-targeted screening tools.
- Partial: Award partial credit if the answer mentions that transformation products (including PFAS) should be monitored during EO treatment or that suspect/non-targeted screening tools are important, but does not clearly connect both points or does not explicitly contrast this with simple parent-compound loss.
- Contradiction: Flag contradiction if the answer suggests that transformation products do not form or do not need to be monitored during electrochemical oxidation of landfill leachate, or that suspect and non-targeted screening tools are unnecessary for evaluating these products.
- Linked exact evidence:
  - `WF10_013_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=928014e358ed17e740f8339c177d8b931b7f8c72bd0e9d7b7f6d62c0f34bb3fa].
    Supports: Directly states that there is a need to monitor transformation products during EO treatment and emphasizes the importance of suspect and non-targeted screening tools.
  - `WF10_013_MMG003`
    > However, formation of transformation products, including PFAS, is a well-known issue [17,18] .
    Supports: Indicates that formation of transformation products, including PFAS, is a well-known issue, reinforcing that these products exist and should be considered when evaluating EO treatment.
  - `WF10_013_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=0868d8143adc0a3a1540d6a49212783e5d99e5ecf2170f482f4ba60b6026c2f1]] .
    Supports: States that formation of transformation products is unwanted relative to the goal of complete PFAS mineralization, underscoring why their formation and fate should be evaluated during EO treatment.

#### WF10_013-X01

- Component: `WF10_013-T02`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: Formation of transformation products during EO, including PFAS, is a known and unwanted issue because complete PFAS mineralization is the ultimate goal, so answers should not imply that EO treatment simply achieves complete mineralization without generating transformation products.
- Full: Use this group only to constrain overclaiming: answers should recognize that EO treatment produces transformation products, including PFAS, and that this is an unwanted process because the ultimate goal is complete PFAS mineralization, avoiding implications that EO simply achieves full mineralization without byproducts.
- Partial: Not applicable; this group is for constraints only.
- Contradiction: Flag contradiction if the answer asserts or clearly implies that EO treatment achieves complete PFAS mineralization without generating transformation products, or that formation of transformation products is not an issue.
- Linked exact evidence:
  - `WF10_013_MMG003`
    > However, formation of transformation products, including PFAS, is a well-known issue [17,18] .
    Supports: Shows that formation of transformation products, including PFAS, is a known issue during degradation processes such as EO.
  - `WF10_013_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=0868d8143adc0a3a1540d6a49212783e5d99e5ecf2170f482f4ba60b6026c2f1]] .
    Supports: States that formation of transformation products is unwanted because the ultimate goal is complete PFAS mineralization, highlighting a limitation on how EO performance should be characterized.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

For electrochemical treatment of PFAS-contaminated landfill leachate, evaluation should go beyond reporting loss of initially targeted PFAS and explicitly consider both precursor/product behavior and transformation products.

On the precursor/product side, the literature notes that "the extent to which PFBA should be degraded has to be considered for practical purposes" during electrochemical treatment of landfill leachate. This means reviewers should not assume that the process is effective simply because targeted parents decline; they should also examine how much PFBA remains and explicitly consider the extent of PFBA degradation when interpreting treatment performance.

On the product side, formation of transformation products, including PFAS, is described as a well-known and unwanted issue in degradation processes, because the ultimate goal is complete PFAS mineralization. Studies of electrochemical oxidation of landfill leachate and groundwater highlight the need to monitor transformation products during EO treatment and emphasize the importance of suspect and non-targeted screening tools. Thus, when reviewing electrochemical landfill-leachate treatment, one should look for evidence that PFAS transformation products have been monitored with appropriate suspect or non-target approaches, and that persistence of species such as PFBA has been considered, rather than relying solely on parent-compound loss to judge treatment performance.

### Unresolved or unsupported boundaries

- The evidence does not specify detailed lists of individual PFAS precursors or intermediate products beyond PFBA, nor does it provide comprehensive coverage of all possible transformation products.
- No explicit quantitative criteria or thresholds for acceptable levels of PFBA or other transformation products after treatment are provided.
- Mechanistic details of specific electrochemical degradation pathways beyond the qualitative indication that transformation products form and that complete PFAS mineralization is the goal are not given in the provided spans.

### Complete approved source chunks

#### WF10_013_MMG001

- Role: `required_gold`
- Document: `2024 - Rehnstam - Suspect and non-target screening of per- and polyfluoroalkyl substances (PFAS) and other halogenated substances in electrochemically oxidized.pdf`
- Chunk: `44`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=928014e358ed17e740f8339c177d8b931b7f8c72bd0e9d7b7f6d62c0f34bb3fa].

```text
[SOURCE_TEXT_OMITTED sha256=2ca195a8353029b720cb2cc9dbf9805457c7986382d3027fb135e5340319feaf].
```

#### WF10_013_MMG002

- Role: `optional_gold`
- Document: `2022 - Maldonado - Electrochemical Transformations of Perfluoroalkyl Acid (PFAA) Precursors and PFAAs in Landfill Leachates.pdf`
- Chunk: `34`
- Registered exact span: Therefore, the extent to which PFBA should be degraded has to be considered for practical purposes.

```text
[SOURCE_TEXT_OMITTED sha256=55653b85ada2754da0608d034673b6ddf555cc67db554717ab03959df83b275e]
```

#### WF10_013_MMG003

- Role: `negative_gold`
- Document: `2024 - Rehnstam - Suspect and non-target screening of per- and polyfluoroalkyl substances (PFAS) and other halogenated substances in electrochemically oxidized.pdf`
- Chunk: `4`
- Registered exact span: However, formation of transformation products, including PFAS, is a well-known issue [17,18] .

```text
[SOURCE_TEXT_OMITTED sha256=8e991735c9cc0edaeacb032a92585d5ad1600de14c7cde178b8fdee9b0698641].
```

---

## WF10_014

**Question:** What do reported reusable functionalized hydrogel sorbents show about compound-specific PFAS removal, and what limits broader generalization?

### Task components

- `WF10_014-T01`: From the reported reusable functionalized hydrogel sorbent study or studies, extract how PFAS removal or sorption performance differs on a compound-specific basis (e.g., among long-chain, short-chain, and replacement PFAS), ensuring that any comparisons are made only where compounds, water matrices, performance endpoints, and experimental conditions are explicitly matched.
- `WF10_014-T02`: Describe what aspects of the reported hydrogel sorbent system and study design limit broader generalization of its PFAS removal performance, including why the evidence does not support extending findings beyond the specific hydrogel, compounds, matrices, endpoints, and conditions tested, and why it does not allow ranking this hydrogel against other PFAS treatment technologies when the evidence is not directly comparable.

### Normative claim groups

#### WF10_014-G01

- Component: `WF10_014-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: For the specific functionalized PEGDA hydrogel sorbents tested in aqueous solution, sorption performance differs among the five targeted PFAS, with aminated PEGDA having the highest sorption capacity for all five (especially PFBA and PFBS), bifunctionalized PEGDA showing higher capacities for PFOA and PFOS, and both aminated and bifunctionalized sorbents being able to remove GenX.
- Full: Award full credit if the answer states that, in this specific study of functionalized PEGDA hydrogels in aqueous solution, (1) the sorbents can sorb the five targeted PFAS to different degrees, (2) aminated PEGDA has the highest sorption capacity for all five PFAS and is particularly strong for PFBA and PFBS, (3) the bifunctionalized PEGDA has higher capacities for PFOA and PFOS, and (4) both aminated and bifunctionalized sorbents remove GenX, with all statements clearly tied to this particular hydrogel system and experimental conditions.
- Partial: Award partial credit if only some of the compound-specific differences are correctly described (e.g., noting that aminated PEGDA is particularly effective for PFBA and PFBS, or that bifunctionalized PEGDA is favored for PFOA and PFOS, or that the five PFAS are sorbed to different degrees) but the answer omits one or more of the other supported distinctions, or if it fails to clearly anchor these findings to the specific PEGDA hydrogels and aqueous-solution tests.
- Contradiction: Mark as contradictory if the answer reverses the reported patterns (e.g., claims bifunctionalized PEGDA is best for short-chain PFAS or that aminated PEGDA is not the highest capacity for the five PFAS), denies that compound-specific differences were observed, or generalizes these compound-specific trends beyond the tested PEGDA hydrogels or outside matched aqueous-solution conditions.
- Linked exact evidence:
  - `WF10_014_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=117b66a6b4cd56e2a985de154d940f2b33733acc918daad7b10efec8daf93c45].
    Supports: Shows that the functionalized PEGDA sorbents can sorb the five specific PFAS to different degrees from aqueous solution, establishing compound-specific sorption under matched conditions.
  - `WF10_014_MMG001`
    > Aminated PEGDA showed the highest sorption capacity for all ﬁve PFASs, particularly for PFBA and PFBS.
    Supports: Supports that aminated PEGDA has the highest sorption capacity for all five PFAS and is especially strong for PFBA and PFBS.
  - `WF10_014_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=2278940960ab09b3f1fc20f6a6d9de6a0ac1a1836b945ad82b6d5201af39dc85].
    Supports: Supports that bifunctionalized PEGDA is relatively favored for PFOA and PFOS compared with other sorbents in this study.
  - `WF10_014_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=db1184b0b27d67e01480d1bbb11317b373b381b351a33d95fafddf93a7b0966d].
    Supports: Supports that both aminated and bifunctionalized PEGDA sorb GenX, and that aminated PEGDA achieves a high GenX sorption capacity under the tested aqueous conditions.

#### WF10_014-G02

- Component: `WF10_014-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: The PEGDA hydrogel study evaluates only five model PFAS under laboratory aqueous-solution conditions, and the authors explicitly state that future studies are needed to assess effectiveness for waters contaminated with various PFAS types and concentrations and to study sorption kinetics under environmentally relevant conditions such as PFAS-contaminated groundwater or surface water, limiting generalization beyond the tested system and conditions.
- Full: Award full credit if the answer notes that this study focuses on five model PFAS and that the authors explicitly state that future studies are needed to (1) examine the effectiveness of these sorbents for treating water contaminated with various types and concentrations of PFASs and (2) evaluate sorption kinetics under environmentally relevant conditions such as PFAS-contaminated groundwater or surface water, and then correctly uses these points to explain that the evidence should not be generalized beyond the specific hydrogels, PFAS tested, and laboratory aqueous-solution conditions.
- Partial: Award partial credit if the answer mentions one but not both of the author-stated needs for future studies (e.g., only types/concentrations or only environmental waters) or more vaguely notes that further work is needed without clearly tying it to the limitations of PFAS types, concentrations, and matrices, while still correctly conveying that generalization is limited to the tested system.
- Contradiction: Mark as contradictory if the answer asserts that the study establishes broad effectiveness of the hydrogels across many PFAS types, concentrations, or real-world matrices without need for further validation, or if it claims that the findings can be directly generalized to environmental waters or other PFAS beyond those specifically tested.
- Linked exact evidence:
  - `WF10_014_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=ec4a8e6cd3146c8abb7cb4a39012ef920a6727aff010ca9b930ab9e5d9850965].
    Supports: Shows that only five targeted PFAS were evaluated and that the tests were in aqueous solution, constraining the scope of the evidence.
  - `WF10_014_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=3339577924e1043299bdea1823c7e52c26713eab95d3e3e575abac62da491cb9].
    Supports: Indicates that the current results are based on five model PFAS and that broader effectiveness across different PFAS types and concentrations has not yet been demonstrated.
  - `WF10_014_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=5d5118e67ea6197c38bba86545469eb410ddff60efbf8c824507e00497baf3d7].
    Supports: Shows that sorption behavior under environmentally relevant conditions (groundwater, surface water) has not been evaluated, limiting generalization to those matrices.

#### WF10_014-G03

- Component: `WF10_014-T02`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: Although the study compares the new hydrogel sorbents to specific commercial resins for certain PFAS, these comparisons are limited to a small set of PFAS and resins and do not support broad ranking of the hydrogel technology against other PFAS treatment technologies beyond the conditions and materials tested.
- Full: Award full credit if the answer notes that the study compares the hydrogel sorbents with specific commercial resins (Purolite A600E and A520E) for a subset of PFAS, points out that the resins perform better for PFOA and PFOS while the hydrogels perform much better for PFBA and PFBS, and then explains that such narrow, compound-specific comparisons do not allow a general ranking of the hydrogel technology against other PFAS treatment technologies beyond these particular materials and conditions.
- Partial: Award partial credit if the answer either (1) mentions that some comparison with commercial resins is made but does not correctly capture the compound-specific nature of the performance differences, or (2) correctly describes that the comparisons are limited to certain PFAS and resins but does not explicitly link this limitation to the inability to rank technologies more broadly.
- Contradiction: Mark as contradictory if the answer claims that the study establishes overall superiority or inferiority of the hydrogel technology relative to PFAS treatment technologies in general, or implies broad performance ranking beyond the specific resins and PFAS for which data are reported.
- Linked exact evidence:
  - `WF10_014_MMG003` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=03ea78343413319eaa1fd1772f819d8b0dbb5b409a830c2e1a0949dbabe7e84b].
    Supports: Shows that performance comparisons with other technologies are limited to specific commercial resins and four PFAS, with differing relative performance depending on the compound.
  - `WF10_014_MMG003` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=8d33bba823a95bab1fd1f16544ddc2b6d416accbc2d9769d379f7aa9a4f31393].
    Supports: Indicates that the hydrogel sorbents greatly outperform the named resins only for shorter-chain PFASs under the tested conditions, reinforcing the compound- and material-specific nature of the comparison rather than a general technology ranking.

#### WF10_014-X01

- Component: `WF10_014-T02`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: The study itself emphasizes that further research is required to evaluate these hydrogels for waters with various PFAS types and concentrations, meaning the current results cannot be generalized to all PFAS or contamination scenarios.
- Full: Treat as a boundary condition that any answer must respect: the text explicitly calls for future studies on various PFAS types and concentrations, so the current findings cannot be extended to untested PFAS or contamination scenarios.
- Partial: If an answer partially acknowledges a need for further research but still generalizes to untested PFAS types or concentrations, it does not fully respect this constraint.
- Contradiction: Flag as violating this constraint if the answer asserts that the hydrogels are broadly effective across all PFAS types or concentration ranges without further qualification.
- Linked exact evidence:
  - `WF10_014_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=cff0184bbec5117b477849e3d0532916b7c78de4372d001b979bb631a6a48942].
    Supports: Directly states that effectiveness across various PFAS types and concentrations remains untested and requires future study.

#### WF10_014-X02

- Component: `WF10_014-T02`
- Importance: `supplementary`
- Scoring role: `constraint_only`
- Proposition: Because the effects of pH and ions such as Na+ and Ca2+ on PFAS sorption by these hydrogels have not yet been investigated, the current results cannot be generalized across different geochemical conditions.
- Full: Treat as a boundary that any generalization of sorption performance to waters with different pH or ionic strengths should be avoided, since the authors explicitly state that these effects still need to be studied.
- Partial: If an answer hints that geochemistry might matter but nonetheless implies robustness across pH or ionic conditions, it only partially respects this constraint.
- Contradiction: Flag as violating this constraint if the answer claims that the hydrogels will perform similarly regardless of pH or presence of ions like Na+ and Ca2+.
- Linked exact evidence:
  - `WF10_014_MMG004` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=27e236bf783212122d8ad7d168f307f258861ce830a9943935cce392a1fd7353].
    Supports: Indicates that pH and ionic effects on PFAS sorption by the new sorbents have not yet been evaluated, constraining generalization across geochemical conditions.

#### WF10_014-X03

- Component: `WF10_014-T02`
- Importance: `supplementary`
- Scoring role: `constraint_only`
- Proposition: Although the study notes regeneration with methanol/NaCl and reuse, these aspects are not evaluated across diverse operational conditions, so they cannot be broadly generalized to all reuse scenarios.
- Full: Use as a constraint that any discussion of reusability must be tied to the specific regeneration method and conditions reported and should not be generalized to all operational settings or long-term cycles.
- Partial: If an answer correctly mentions regeneration but implies indefinite or general reusability without qualification, it partially violates this constraint.
- Contradiction: Flag as violating this constraint if the answer claims broad, condition-independent reusability or long-term stability not supported by the text.
- Linked exact evidence:
  - `WF10_014_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > The spent sorbents were reusable after readily regenerated with 70% methanol contained 1% NaCl.
    Supports: Shows that reusability was demonstrated only after regeneration with a specific methanol/NaCl solution, under unspecified broader operational variations.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

The reported study investigates reusable functionalized poly(ethylene glycol) diacrylate (PEGDA) hydrogel sorbents against a specific set of five PFAS in aqueous solution and shows clear compound-specific sorption behavior under those matched conditions.

For the five targeted PFAS—perfluorooctanoic acid (PFOA), perfluorooctanesulfonic acid (PFOS), perfluorobutanoic acid (PFBA), perfluorobutanesulfonic acid (PFBS), and GenX—the authors state that the newly synthesized sorbents "can sorb the ﬁve targeted PFASs ... to diﬀerent degrees from aqueous solution" (WF10_014_MMG001). Within this experimental system, aminated PEGDA is reported to have the strongest overall performance: "Aminated PEGDA showed the highest sorption capacity for all ﬁve PFASs, particularly for PFBA and PFBS" (WF10_014_MMG001). In contrast, the bifunctionalized PEGDA is relatively favored for the longer-chain acids, as "The bifunctionalized PEGDA showed higher capacities for PFOA and PFOS" (WF10_014_MMG001). For the replacement compound GenX, the study reports that "[SOURCE_TEXT_OMITTED sha256=cfb07ba731c7639bb2a7d2fbb0394c8a1028d73d6e42f2c3a8aa3f99231b3559]" (WF10_014_MMG001). Taken together, these findings show that, in these aqueous-solution tests on the PEGDA hydrogels, sorption is clearly compound-specific, with aminated PEGDA particularly strong for the short-chain PFBA and PFBS, bifunctionalized PEGDA favored for PFOA and PFOS, and both functionalizations effective for GenX.

The scope of these findings is, however, restricted in several ways that limit broader generalization. First, the study examines only "the ﬁve targeted PFASs" or "ﬁve model PFASs" in aqueous solution (WF10_014_MMG001; WF10_014_MMG002). The authors explicitly caution that "Future studies are needed to examine the eﬀectiveness of these sorbents for treating water contaminated with various types and concentrations of PFASs" (WF10_014_MMG002), indicating that performance for other PFAS structures or for different contamination levels has not been established. Second, the tests are not carried out in environmental matrices. The authors note that "[SOURCE_TEXT_OMITTED sha256=5d5118e67ea6197c38bba86545469eb410ddff60efbf8c824507e00497baf3d7]" (WF10_014_MMG003), so the present results should not be assumed to apply directly to groundwater, surface water, or other complex waters.

Geochemical variability further constrains extrapolation. The paper acknowledges that "presence of ions such as Na+ and Ca2+ have shown to interfere the absorption of PFASs" and therefore concludes that "future study is needed to investigate the eﬀects of pH and these ions on the sorption capability of PFAS by these newly developed sorbents" (WF10_014_MMG004). Because pH and major ions were not systematically evaluated for these hydrogels, their sorption performance cannot be confidently generalized to waters with differing pH or ionic composition beyond the conditions actually tested.

The study does provide a limited comparison with other treatment materials, specifically the commercial resins Purolite A600E and A520E. It reports that "[SOURCE_TEXT_OMITTED sha256=a1cf071eadf94eab55757b62ef941e43630b2e55ef2563e100810436884de10d]" (WF10_014_MMG003), and that "[SOURCE_TEXT_OMITTED sha256=712b050265f8952aaba000328569b0747a31e91d73fc2e0da7c8166be6a73939]" (WF10_014_MMG003). These comparisons show that, under the specific test conditions and for these particular PFAS, the hydrogel sorbents underperform the selected resins for PFOA and PFOS but substantially outperform them for PFBA and PFBS. However, because the comparison is limited to a small number of compounds and two specific resins under particular laboratory conditions, it does not support ranking the hydrogel technology against PFAS treatment technologies in general.

Finally, while the study notes that "The spent sorbents were reusable after readily regenerated with 70% methanol contained 1% NaCl" (WF10_014_MMG001), this regeneration and reuse are demonstrated only for that particular method and do not establish performance across many regeneration cycles or operational environments. Overall, the evidence allows only condition-specific conclusions: the functionalized PEGDA hydrogels show distinct compound-specific sorption for PFOA, PFOS, PFBA, PFBS, and GenX in aqueous-solution tests, with aminated and bifunctionalized formulations differing in their relative affinities, but the data cannot be generalized beyond the specific sorbents, PFAS, matrices, endpoints, and conditions evaluated, nor used to broadly rank this hydrogel system against other PFAS treatment technologies that were not directly and comparably tested.

### Unresolved or unsupported boundaries

- Any detailed description of experimental matrices beyond the fact that sorption was studied from aqueous solution; specific water chemistry, PFAS concentrations, and other test conditions are not provided in the supplied text.
- Quantitative kinetic data, such as rate constants or full breakthrough curves, for PFAS sorption on the hydrogels are not supported by the provided evidence, beyond the single GenX capacity value and general mention of short equilibrium times in other work.
- Information on long-term reusability across many regeneration cycles, or performance under field-scale or pilot-scale conditions, is not supported by the supplied excerpts.
- Comparative performance of these hydrogels versus other PFAS treatment technologies beyond the specifically mentioned Purolite A600E and A520E resins is not documented in the provided text.

### Complete approved source chunks

#### WF10_014_MMG001

- Role: `required_gold`
- Document: `2018 - Huang - Reusable Functionalized Hydrogel Sorbents for Removing Long- and Short-Chain Perfluoroalkyl Acids (PFAAs) and GenX from Aqueous Solution.pdf`
- Chunk: `1`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=117b66a6b4cd56e2a985de154d940f2b33733acc918daad7b10efec8daf93c45].

```text
[SOURCE_TEXT_OMITTED sha256=229ff0c9d7324cd2c1f7c87f72440b7920caf2293975ec42b68891e45b427700].
```

#### WF10_014_MMG002

- Role: `negative_gold`
- Document: `2018 - Huang - Reusable Functionalized Hydrogel Sorbents for Removing Long- and Short-Chain Perfluoroalkyl Acids (PFAAs) and GenX from Aqueous Solution.pdf`
- Chunk: `26`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=cff0184bbec5117b477849e3d0532916b7c78de4372d001b979bb631a6a48942].

```text
[SOURCE_TEXT_OMITTED sha256=5738dc03d5fa85b408e0c43db8279990f8a9d4bc72aff5494ab5144ef5406fa8]
```

#### WF10_014_MMG003

- Role: `negative_gold`
- Document: `2018 - Huang - Reusable Functionalized Hydrogel Sorbents for Removing Long- and Short-Chain Perfluoroalkyl Acids (PFAAs) and GenX from Aqueous Solution.pdf`
- Chunk: `25`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=5d5118e67ea6197c38bba86545469eb410ddff60efbf8c824507e00497baf3d7].

```text
[SOURCE_TEXT_OMITTED sha256=bb120f104ae075bcdf2eb91cc7ea620c5c2cce8aaf2b2ccac0b7ee037ab8eee4]-
```

#### WF10_014_MMG004

- Role: `negative_gold`
- Document: `2018 - Huang - Reusable Functionalized Hydrogel Sorbents for Removing Long- and Short-Chain Perfluoroalkyl Acids (PFAAs) and GenX from Aqueous Solution.pdf`
- Chunk: `27`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=b641f60d3d8669179e55f55e46aec166ee4063191896a19cd3e9bbe015493a40].

```text
[SOURCE_TEXT_OMITTED sha256=23ac322755cf22d376ac14da90ec03c29a0a63d4dc11e204dd9d5d967a09ae26]
```

---

## WF10_015

**Question:** What information do I need before comparing PFAS breakthrough curves from drinking-water adsorption columns?

### Task components

- `WF10_015-T01`: Extract the reported column protocol steps and operating procedures relevant to PFAS breakthrough curves (e.g., how the adsorption experiment is run from start to finish) so that procedural differences can be identified before comparing breakthrough behavior.
- `WF10_015-T02`: Extract the reported materials and setup used in the adsorption columns, including sorbent/column media, column configuration, and any other key hardware or reagents, along with the characteristics of the water matrix used (e.g., drinking water source or composition descriptors) so that physical and matrix differences are known before comparison.
- `WF10_015-T03`: Extract the reported operating conditions and model variables used to describe PFAS breakthrough, including flow-related conditions, loading or contact conditions, and how breakthrough is quantified or modeled, together with the specific target PFAS compounds considered and the stated meaning of each reported model variable.
- `WF10_015-T04`: Extract any reported study-specific limitations, assumptions, or caveats that the authors state regarding their PFAS breakthrough curves or model description, focusing on factors that could restrict or qualify comparisons across different adsorption column studies.

### Normative claim groups

#### WF10_015-G01

- Component: `WF10_015-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: To compare PFAS breakthrough curves from adsorption columns, researchers need information on column dimensions, the adsorbent material type, flow rates, and water quality, because differences in these parameters can make adsorption results from different studies not directly comparable.
- Full: Award full credit if the answer states that column dimensions, material/adsorbent type, flow rates, and water quality (or equivalent wording) are important variables that must be known or controlled when comparing adsorption or PFAS breakthrough curves across studies, and indicates that differences in these parameters reduce comparability.
- Partial: Award partial credit if the answer mentions at least two of the following as important for comparison: column dimensions, adsorbent/material type, flow rates, water quality, but does not clearly link them to comparability limitations, or omits one or more parameters.
- Contradiction: Mark as contradictory if the answer claims that column dimensions, material type, flow rates, and water quality do not meaningfully affect comparability of adsorption or PFAS breakthrough results, or that results are directly comparable without considering these parameters.
- Linked exact evidence:
  - `WF10_015_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=0bbb29e1f691355cff2fcd6ee130dcbd4b3fdc4e56c5f18296d5780fea030033].
    Supports: Identifies column dimension, material type, flow rates, and water quality as experimental parameters that differ between studies and affect comparability of adsorption results.

#### WF10_015-G02

- Component: `WF10_015-T03`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: When comparing PFAS breakthrough behavior, researchers often use bed volumes to breakthrough as a key comparison metric, but differences in bed volume size, operating conditions, and adsorbate concentrations must be known because they obscure direct comparison.
- Full: Award full credit if the answer notes that bed volumes (BVs) to breakthrough are widely used to characterize or compare PFAS breakthrough, and also mentions that comparability is affected by differences in BV size, operating conditions, and/or adsorbate concentration, which must be accounted for.
- Partial: Award partial credit if the answer mentions bed volumes as a comparison metric for breakthrough behavior but does not clearly mention why differences in BV size, operating conditions, or adsorbate concentration matter, or only mentions one of these complicating factors.
- Contradiction: Mark as contradictory if the answer asserts that bed volume–based breakthrough comparisons are straightforward or unaffected by differences in BV size, operating conditions, or adsorbate concentrations.
- Linked exact evidence:
  - `WF10_015_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=e23d0a56bff770b60c28dcdeb9d464f480576e485d835cab2f9141ffee8ff539]] .
    Supports: Shows that bed volumes to breakthrough are commonly used to evaluate breakthrough behavior.
  - `WF10_015_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=d5c638caece65bd2c9aad932a4ea6fe7c29729d084bfd9d9de56e18cc9fddc0e].
    Supports: States that differences in BV sizes, operating conditions, and adsorbate concentrations obscure comparisons based on bed volumes.

#### WF10_015-G04

- Component: `WF10_015-T04`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: Authors note that differences in experimental parameters and water quality make models describing micropollutant breakthrough based on water quality parameters scarce, indicating a limitation in using water-quality-based models for comparing PFAS breakthrough across studies.
- Full: Award full credit if the answer notes that models describing micropollutant or PFAS breakthrough as a function of water quality parameters are still scarce, and presents this as a limitation or caveat affecting cross-study comparison based on water quality.
- Partial: Award partial credit if the answer mentions scarcity of breakthrough models related to water quality without explicitly identifying it as a limitation for cross-study comparison.
- Contradiction: Mark as contradictory if the answer claims that models describing micropollutant or PFAS breakthrough based on water quality parameters are widely available or well established.
- Linked exact evidence:
  - `WF10_015_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=0bbb29e1f691355cff2fcd6ee130dcbd4b3fdc4e56c5f18296d5780fea030033].
    Supports: Explicitly identifies that models describing micropollutant breakthrough based on water quality parameters are scarce, implying a limitation.

#### WF10_015-X01

- Component: `WF10_015-T01`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: The available evidence does not provide detailed, step-by-step adsorption column operating procedures or specific protocol sequences for PFAS breakthrough experiments, so such procedural details should not be inferred or invented.
- Full: Ensure the answer does not specify or imply detailed column operating steps (e.g., exact start-up, equilibration, dosing sequence, or termination procedures) that are not explicitly present in the evidence.
- Partial: N/A for scoring; this is a constraint.
- Contradiction: Flag as violating constraints if the answer invents or describes specific procedural steps or time sequences for the adsorption column experiments that are not directly supported by the evidence.
- Linked exact evidence:
  - `WF10_015_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=0bbb29e1f691355cff2fcd6ee130dcbd4b3fdc4e56c5f18296d5780fea030033].
    Supports: Mentions only general experimental parameters and does not provide step-by-step protocol details, illustrating the absence of explicit procedural descriptions.
  - `WF10_015_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=e23d0a56bff770b60c28dcdeb9d464f480576e485d835cab2f9141ffee8ff539]] .
    Supports: Indicates an evaluation approach (bed volumes to breakthrough) but does not supply operational step sequences, reinforcing that the evidence lacks explicit protocol steps.

#### WF10_015-X02

- Component: `WF10_015-T02`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: The provided evidence does not specify detailed column hardware configurations, sorbent product names, or exact drinking water composition, so these must not be assumed or generalized.
- Full: Ensure the answer does not introduce specific column hardware designs, media brand names, or detailed drinking-water chemistry beyond the general mention of water quality and different water types.
- Partial: N/A for scoring; this is a constraint.
- Contradiction: Flag as violating constraints if the answer provides unreferenced specific details about column internals, sorbent brands, or full matrix composition.
- Linked exact evidence:
  - `WF10_015_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=0bbb29e1f691355cff2fcd6ee130dcbd4b3fdc4e56c5f18296d5780fea030033].
    Supports: Only broad categories of experimental parameters are listed; no specific hardware or composition details are provided.
  - `WF10_015_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=e23d0a56bff770b60c28dcdeb9d464f480576e485d835cab2f9141ffee8ff539]] .
    Supports: Refers generally to 'several source waters under different conditions' without detailing hardware or exact water compositions, underscoring the lack of specific matrix and setup details.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

The available evidence highlights several specific types of information that need to be known before comparing PFAS breakthrough curves from drinking-water adsorption columns, while also indicating important limitations.

First, basic experimental parameters strongly influence comparability across studies. Results for adsorption of organic micropollutants are noted to be “often not comparable because experimental parameters, such as column dimension, material type, ﬂow- rates, and water quality, diﬀer substantially” [WF10_015_MMG001]. Thus, before comparing breakthrough curves, a researcher should at minimum collect information on the column dimensions, the adsorbent or material type packed in the column, the flow rates used, and the water quality or type being treated. Differences in any of these parameters can lead to differences in observed breakthrough behavior even for the same PFAS.

Second, how breakthrough is quantified also matters. Many adsorption studies use bed volumes to breakthrough as a central comparison metric: “[SOURCE_TEXT_OMITTED sha256=1518456cd1d0bddefde0c87d3ce860496e4a6ba89bae12b429c3c11b146c4d0e]” [WF10_015_MMG002]. If breakthrough is reported in terms of bed volumes, then the bed volume definition and size, along with the operating conditions and influent concentration, become key variables. The same source cautions that “[SOURCE_TEXT_OMITTED sha256=2f8f9d536005bb42e175fcdd7458247e8d1c191d0fa27cb9c6700d799f16d1c3] availability of adsorption sites” [WF10_015_MMG002]. Therefore, to meaningfully compare bed‑volume‑based breakthrough curves, one needs explicit information on the bed volume size, the operating conditions under which the column was run, and the influent adsorbate (e.g., PFAS) concentrations.

Finally, the evidence identifies an important limitation relevant to cross‑study comparison: “models describing micropollutant breakthrough based on water quality parameters are still scarce” [WF10_015_MMG001]. This scarcity means that even if water quality is known, there may be limited modeling tools for directly predicting or normalizing PFAS breakthrough as a function of water quality, which restricts the ability to fully harmonize data across different source waters.

Within the provided text, no detailed stepwise column protocol, specific column hardware configuration, exact drinking‑water composition, or list of target PFAS compounds is given. Thus, only the general categories of needed information—column dimensions, material type, flow conditions, water quality, bed volume definitions, operating conditions, and influent concentrations—can be identified from this evidence as relevant variables and descriptors for comparing PFAS breakthrough curves.

### Unresolved or unsupported boundaries

- Detailed, stepwise column operating procedures for PFAS breakthrough experiments (e.g., start-up, equilibration, sampling schedule, and shutdown steps) are not described in the provided evidence.
- Specific column configurations (e.g., internal design details, packing arrangements) and sorbent product identities are not provided.
- Exact drinking-water source descriptions or composition (e.g., DOC, specific inorganic ions, full PFAS concentration profiles) are not given in the excerpts.
- The specific PFAS compounds targeted in the breakthrough studies, and their individual properties or behaviors, are not listed.
- Any numerical values, units, or quantitative performance metrics for PFAS breakthrough or adsorbent use rates are not present in the cited text.

### Complete approved source chunks

#### WF10_015_MMG001

- Role: `required_gold`
- Document: `2021 - Franke - The Price of Really Clean Water - Combining Nanofiltration with Granular Activated Carbon and Anion Exchange Resins for the Removal of Per- And.pdf`
- Chunk: `36`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=0bbb29e1f691355cff2fcd6ee130dcbd4b3fdc4e56c5f18296d5780fea030033].

```text
[SOURCE_TEXT_OMITTED sha256=f0df7b4d94fa63d2ede237b6648e9905323553513c2ce992738e6cb67e33e8b8]
```

#### WF10_015_MMG002

- Role: `optional_gold`
- Document: `2023 - Murray - PFAS adsorbent selection - The role of adsorbent use rate, water quality, and cost.pdf`
- Chunk: `6`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=e23d0a56bff770b60c28dcdeb9d464f480576e485d835cab2f9141ffee8ff539]] .

```text
[SOURCE_TEXT_OMITTED sha256=afbcbb41684092615c76309988c3a5f3d2ca9cd69ad145fd2d1eb1a0003a0c2a] -
```

---

## WF10_016

**Question:** When summarizing plasma treatment for PFAS, what performance, mass-balance, and energy-use details should be kept together?

### Task components

- `WF10_016-T01`: From the plasma treatment span, extract details that describe PFAS removal-like outcomes (e.g., changes in concentration between inlet and outlet) and keep these clearly distinguished from separation, adsorption, degradation, defluorination, mineralization, destruction, and byproduct formation descriptions.
- `WF10_016-T02`: From the same span, extract descriptions of PFAS transformation endpoints, including degradation, defluorination, mineralization, destruction, and byproduct formation, ensuring these are not conflated with simple removal, separation, or adsorption.
- `WF10_016-T03`: Extract any mass-balance-related evidence (e.g., accounting of PFAS and transformation products across phases or system components) and keep it distinct from performance endpoints like removal, defluorination, or mineralization.
- `WF10_016-T04`: Extract any energy-use details associated with the plasma treatment (e.g., how energy input or efficiency is characterized) and keep these clearly separate from removal, transformation endpoints, and mass-balance evidence.

### Normative claim groups

#### WF10_016-G01

- Component: `WF10_016-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In the plasma study, PFAS removal-like performance is characterized as degradation efficiency based on the change in PFAS concentration from an initial value (C0) to a concentration at reaction time (C1).
- Full: Award full credit if the answer explains that PFAS performance is expressed as a degradation efficiency calculated from an initial PFAS concentration (C0) and a PFAS concentration at a given reaction time (C1), clearly indicating this as a removal-like or concentration-change metric and not conflating it with defluorination or energy-use metrics.
- Partial: Award partial credit if the answer mentions that performance is based on differences between initial and final PFAS concentrations, but does not clearly identify this as a degradation efficiency metric or does not distinguish it from transformation or energy metrics.
- Contradiction: Mark as contradiction if the answer states that removal-like performance is based on defluorination efficiency alone or describes degradation efficiency as unrelated to PFAS concentration changes.
- Linked exact evidence:
  - `WF10_016_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=a5b78d2d933f78c16bacae081c8e843a57105a23ce9eea684b6bc1ef6f989583]).
    Supports: Shows that degradation efficiency is defined as a percent change from initial PFAS concentration (C0) to concentration at a given reaction time (C1), which is a removal-like performance measure based on concentration change.

#### WF10_016-G02

- Component: `WF10_016-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In the plasma study, PFAS transformation endpoints are characterized separately from removal-like metrics using defluorination efficiency and first-order reaction rate constants.
- Full: Award full credit if the answer states that transformation is evaluated using defluorination efficiency (based on fluoride concentrations over time relative to the fluoride content of PFOA) and/or first-order reaction rate constants, and notes that these are distinct from the degradation efficiency removal-like metric.
- Partial: Award partial credit if the answer only mentions defluorination efficiency or only mentions first-order rate constants as transformation endpoints, without clearly distinguishing them from removal-like metrics.
- Contradiction: Mark as contradiction if the answer conflates defluorination efficiency or first-order rate constants with simple removal or adsorption, or claims that no transformation endpoints are reported.
- Linked exact evidence:
  - `WF10_016_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=a5b78d2d933f78c16bacae081c8e843a57105a23ce9eea684b6bc1ef6f989583]).
    Supports: Indicates that, in addition to degradation efficiency, defluorination efficiency and first-order rate constants are explicitly calculated as distinct performance metrics.
  - `WF10_016_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=a5b78d2d933f78c16bacae081c8e843a57105a23ce9eea684b6bc1ef6f989583]).
    Supports: Shows that defluorination efficiency is defined based on the change in fluoride concentration over time relative to the fluoride content of PFOA, which is a transformation endpoint rather than a simple removal metric.

#### WF10_016-G04

- Component: `WF10_016-T04`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In the plasma study, energy use is characterized by electrical energy per order (EE/O), which is calculated from discharge power, treatment time, treated volume, and the logarithmic reduction in PFAS concentration.
- Full: Award full credit if the answer notes that energy input or efficiency is represented by an electrical energy per order (EE/O) metric and explains that it is calculated from discharge power, treatment time, treated volume, and the logarithm of the concentration ratio C0/C1, distinguishing this from degradation or defluorination efficiencies.
- Partial: Award partial credit if the answer mentions EE/O as an energy-use metric but does not clearly describe how it depends on power, time, volume, and concentration change, or does not explicitly distinguish it from removal or transformation endpoints.
- Contradiction: Mark as contradiction if the answer incorrectly describes EE/O as a defluorination or degradation efficiency metric, or claims that the plasma span does not report any energy-use characterization.
- Linked exact evidence:
  - `WF10_016_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=a5b78d2d933f78c16bacae081c8e843a57105a23ce9eea684b6bc1ef6f989583]).
    Supports: Shows that EE/O is explicitly used as a metric and is calculated from discharge power (P), treatment time (t), treated volume (V), and the logarithm of the concentration ratio C0/C1, which is an energy-use characterization distinct from degradation and defluorination efficiencies.

#### WF10_016-X01

- Component: `WF10_016-T03`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: The provided plasma-treatment span does not report mass-balance accounting of PFAS or transformation products across phases or system components.
- Full: Use this constraint to prevent overclaiming mass-balance information: the answer should not describe any accounting of PFAS or transformation products across phases, reactors, or system components, because the span only defines degradation efficiency, defluorination efficiency, EE/O, and rate constants.
- Partial: If an answer cautiously notes that mass-balance is not discussed or is unknown from this span, treat this constraint as partially respected.
- Contradiction: If an answer claims that this span provides quantitative mass-balance closure or distribution of PFAS/byproducts across phases or system components, mark this constraint as violated.
- Linked exact evidence:
  - `WF10_016_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=a5b78d2d933f78c16bacae081c8e843a57105a23ce9eea684b6bc1ef6f989583]).
    Supports: Lists the performance metrics reported (degradation efficiency, EE/O, defluorination efficiency, and rate constants) and implicitly indicates that no mass-balance metrics are included in this span.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

In this nonthermal plasma study, removal-like performance is expressed as a degradation efficiency that depends on the change in PFAS concentration between the start of treatment and a given reaction time. The authors define a degradation efficiency metric as a percentage based on the initial concentration of PFAS (C0) and its concentration at a given reaction time (C1), explicitly stating that “C0 denotes the initial concentration of PFAS … while C1 represents its concentration at a given reaction time.” This metric captures how much of the target PFAS has been degraded in terms of concentration decrease, and it should be kept conceptually separate from transformation-specific or energy-use descriptors.

Transformation endpoints are characterized with separate metrics. The span reports a defluorination efficiency, defined as a percentage based on the change in fluoride concentration over time relative to the theoretical fluoride content of PFOA, and it also lists first-order reaction rate constants k as determined from a kinetic expression involving C0 and C1. These reflect chemical transformation and bond-breaking (as inferred from fluoride release and kinetic behavior) rather than simple concentration-based degradation efficiency. When summarizing plasma performance, these transformation metrics should be clearly distinguished from removal-like concentration changes and from any separation or adsorption processes, which are not discussed in this span.

The same methods section also introduces an energy-use descriptor, electrical energy per order (EE/O). EE/O is calculated using the discharge power P, treatment time t, treated volume V, and the logarithm of the concentration ratio C0/C1. This provides an energy-efficiency context for the observed degradation and must be kept distinct from the degradation and defluorination efficiencies, which are performance endpoints rather than energy metrics.

Within this span, there is no explicit mass-balance accounting of PFAS or its transformation products across phases or system components. The reported quantities are limited to degradation efficiency, defluorination efficiency, EE/O, and first-order rate constants. Consequently, when summarizing gliding-arc or other nonthermal plasma performance on PFAS using this information, it is appropriate to treat: (i) degradation efficiency as a removal-like concentration-change measure; (ii) defluorination efficiency and first-order rate constants as transformation endpoints; and (iii) EE/O as an energy-use metric, while recognizing that mass-balance closure and byproduct distributions are not addressed in this particular span.

### Unresolved or unsupported boundaries

- Any explicit mass-balance accounting of PFAS or transformation products across phases or system components is not described in the provided span.
- Descriptions of mineralization, such as conversion of PFAS carbon to inorganic carbon species, are not present in the span.
- Descriptions of byproduct formation, including identification or quantification of specific transformation products, are not present.
- Evidence of separation or adsorption processes (e.g., PFAS transfer to another phase or sorbent) is not mentioned.
- Descriptions of destruction or complete mineralization endpoints beyond the reported degradation and defluorination efficiencies are not provided.
- Any study-specific numeric values for efficiencies, rate constants, EE/O, concentrations, or power, beyond the symbolic equations, are not given in the span.

### Complete approved source chunks

#### WF10_016_MMG001

- Role: `required_gold`
- Document: `2026 - Chen - Ferrate-assisted nonthermal plasma for efficient PFOA degradation in landfill leachate - Mitigating bulk organic interference and enhancing.pdf`
- Chunk: `13`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=a5b78d2d933f78c16bacae081c8e843a57105a23ce9eea684b6bc1ef6f989583]).

```text
[SOURCE_TEXT_OMITTED sha256=8aad6a007154db56166b8880fea207d66ac8be1a4645552014f34b2c4cdd548c]
```

---

## WF10_023

**Question:** What has been reported for PFOA or PFBA removal by reverse osmosis at elevated pressure, and what uncertainties limit generalizing that result?

### Task components

- `WF10_023-T01`: Extract what has been reported for PFOA or PFBA removal by reverse osmosis operated at elevated pressure, including any explicitly stated values, units, compounds, matrices, methods, and operating conditions, and note if the reported result is bounded, censored, approximate, or condition-specific.
- `WF10_023-T02`: Identify and describe the uncertainties, caveats, or limitations mentioned in the source that restrict how far this elevated-pressure RO removal result for PFOA or PFBA can be generalized beyond the specific reported conditions.

### Normative claim groups

#### WF10_023-G01

- Component: `WF10_023-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In a high-pressure reverse osmosis experiment, above 99.98% of PFOA or PFBA were removed by an RO membrane as transmembrane pressure increased from 13.79 to 55.16 bar, and this removal value is reported as a lower-bounded, condition-specific result for that membrane; separate text reports the operating conditions used for RO experiments examining PFOA/PFBA rejection under different operation pressures.
- Full: Award full credit if the answer states that in a reported high-pressure reverse osmosis experiment, above 99.98% of PFOA or PFBA were removed by the RO membrane and explicitly identifies the pressure range as 13.79 to 55.16 bar, noting that this is a condition-specific, lower-bounded removal result for that RO membrane. The answer may also report the separately stated operating conditions for RO experiments examining PFOA/PFBA rejection under different operation pressures (initial concentration 10,000 ppb, feed flow rate 30 mL /C1 min/C0 1, room temperature, 24 h filtration) as contextual information, but it should not imply that the evidence explicitly links those conditions to the >99.98% removal dataset.
- Partial: Award partial credit if the answer correctly reports that above 99.98% PFOA or PFBA removal was achieved by an RO membrane at elevated pressure and/or mentions the 13.79–55.16 bar range, but omits the lower-bounded nature of the value, does not clearly frame the result as condition-specific, or does not distinguish between the directly linked removal result and the separately reported experimental conditions for RO pressure-dependence experiments. Minor omissions of contextual conditions are acceptable for partial credit as long as the main numeric result and high-pressure RO context are correct.
- Contradiction: Mark as contradictory if the answer changes the reported percentage (e.g., claims 90% or 100% removal instead of above 99.98%), misstates the pressure range or units, attributes this result to a different technology (e.g., nanofiltration instead of RO), or generalizes the finding as a universal PFAS removal performance of RO rather than a specific high-pressure experiment.
- Linked exact evidence:
  - `WF10_023_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=f53f5c49622474f4574abb4f0c579269619a52b0674a6d413da3787b6d60420f].
    Supports: Reports that above 99.98% PFOA or PFBA were removed by the RO membrane, that removal efficiency increased slightly with transmembrane pressure, and that the pressure range was 13.79 to 55.16 bar in a high-pressure RO operation.
  - `WF10_023_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=a1707bb5bbf861051d0d9cb579af8cf60de7d99c282294dc0b2c6a984e25c9ca].
    Supports: States that at a 1000 ppb initial feed concentration, PFOA and PFBA permeate concentrations were below LC-QQQ detection limits, preventing assessment of the potency of PFAS rejection under different pressures.
  - `WF10_023_MMG003` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=f819387d1191ec5b25427264ad142327a41505e020765a60aac134603d2e5c87].
    Supports: Provides the experimental conditions (initial PFOA/PFBA concentration of 10,000 ppb, feed flow rate of 30 mL /C1 min/C0 1, room temperature, and 24 h filtration time) for RO membrane experiments examining PFOA/PFBA rejection under different operation pressures.

#### WF10_023-G02

- Component: `WF10_023-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Uncertainties and limitations in the study restrict how the high-pressure RO PFOA/PFBA removal result can be generalized, including that permeate concentrations were below LC-QQQ detection limits at 1000 ppb feed so potency of rejection under different pressures could not be assessed in that case, and that removal efficiency and mechanisms of PFAS in high-pressure RO processes remain largely unknown and were only partially addressed.
- Full: Award full credit if the answer notes that generalization of the elevated-pressure RO PFOA/PFBA removal result is limited because (1) PFOA and PFBA permeate concentrations were below LC-QQQ detection limits at an initial feeding concentration of 1000 ppb, which did not allow assessment of the potency of PFAS rejection under different pressures, and (2) the removal efficiency and mechanisms of many micropollutants such as PFAS in high-pressure RO processes are largely unknown and only partially addressed in the study. Both types of uncertainties must be described.
- Partial: Award partial credit if the answer correctly identifies at least one major limitation, such as the non-detect permeate concentrations preventing pressure-effect assessment, or the statement that PFAS removal efficiency and mechanisms in high-pressure RO are largely unknown, but omits the other or does not clearly tie these to limits on generalization.
- Contradiction: Mark as contradictory if the answer claims that the study fully characterizes PFAS removal efficiency and mechanisms in high-pressure RO, or suggests there were no analytical or interpretive limitations (e.g., denies the issue of permeate concentrations being below detection limits), thereby implying the results can be freely generalized.
- Linked exact evidence:
  - `WF10_023_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=a1707bb5bbf861051d0d9cb579af8cf60de7d99c282294dc0b2c6a984e25c9ca].
    Supports: States that at 1000 ppb initial feed, PFOA and PFBA permeate concentrations were below LC-QQQ detection limits, preventing assessment of the potency of PFAS rejection under different pressures, which is a key uncertainty limiting generalization.
  - `WF10_023_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=030418d41ac75c4a4b432c22a877f17df5746eea0f288a37a192f983aa17a56d].
    Supports: Indicates that, in general, removal efficiency and mechanisms of many micropollutants including PFAS in high-pressure RO processes are largely unknown and only partially addressed, highlighting a broader uncertainty that limits generalization of the specific high-pressure result.

#### WF10_023-X01

- Component: `WF10_023-T01`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: The reported high-pressure RO PFOA/PFBA removal result is specific to the studied RO membrane and experimental configuration, and should not be generalized to all RO systems, all PFAS, or all operating conditions; some data are censored (below detection limits) and the study notes that high-pressure RO PFAS removal mechanisms remain largely unknown.
- Full: Use this group to prevent overclaiming. Any answer that extrapolates the above 99.98% removal at 13.79–55.16 bar to all RO systems, all PFAS, or all high-pressure conditions without mentioning that the result is specific to the tested RO membrane, experimental configuration, and censored/unknown aspects of high-pressure RO PFAS removal should be considered overgeneralizing.
- Partial: If an answer largely respects study-specific boundaries but is slightly vague about scope, treat this as a minor issue. Only when the answer clearly implies universal performance or fully understood mechanisms should it be penalized based on this constraint.
- Contradiction: Treat it as a violation of this constraint if the answer states or clearly implies that high-pressure RO generally achieves above 99.98% removal for PFOA/PFBA (or PFAS broadly) across systems and conditions, or that high-pressure RO PFAS removal mechanisms are well understood, contradicting the cited limitations.
- Linked exact evidence:
  - `WF10_023_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=f53f5c49622474f4574abb4f0c579269619a52b0674a6d413da3787b6d60420f].
    Supports: Shows that the very high removal is reported for a specific RO membrane and experiment, implying it should not automatically be generalized.
  - `WF10_023_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=a1707bb5bbf861051d0d9cb579af8cf60de7d99c282294dc0b2c6a984e25c9ca].
    Supports: Highlights analytical censoring (below detection limits) that limits assessment of pressure effects, constraining generalization of performance estimates.
  - `WF10_023_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=030418d41ac75c4a4b432c22a877f17df5746eea0f288a37a192f983aa17a56d].
    Supports: States that mechanisms and removal efficiency in high-pressure RO are largely unknown, emphasizing that broad generalizations are not yet justified.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

In the cited study, a commercial reverse osmosis (RO) membrane operated at elevated transmembrane pressure achieved very high removal of perfluorooctanoic acid (PFOA) and perfluorobutanoic acid (PFBA). The authors report that "above 99.98% PFOA or PFBA were removed by the RO membrane" and that "[SOURCE_TEXT_OMITTED sha256=8b9891fd619016114d1cf0ca7dfd94290a892fd18d330cb1c68fc3ba03f76465]," indicating a high-pressure RO operation (WF10_023_MMG001). Separately, for RO experiments examining PFOA/PFBA rejection under different operation pressures, the experimental conditions were: initial PFOA/PFBA concentration of 10,000 ppb, feed flow rate of 30 mL /C1 min/C0 1, room temperature, and filtration time of 24 h (WF10_023_MMG003). The "above 99.98%" statement provides a lower-bounded, condition-specific removal result for this RO membrane under high-pressure operation, while the listed conditions describe how RO pressure-dependence experiments on PFOA/PFBA were conducted.

Several uncertainties limit how far this elevated-pressure RO result can be generalized. Analytically, when the initial feeding concentration was 1000 ppb, "both PFOA and PFBA concentration in permeate [were] below the LC-QQQ detection limits," which "does not allow us to assess the potency of PFAS rejection under different pressures" (WF10_023_MMG003). This censoring means pressure effects on rejection could not be quantified at that lower feed concentration. More broadly, the authors note that "the removal efficiency and mechanisms of many potential [SOURCE_TEXT_OMITTED sha256=97c0b48970a1fc8c85d2970c8dcf778a7509a7ee72550bf0d771a5ea9c11e204]" (WF10_023_MMG002). Together, these points indicate that while very high PFOA/PFBA removal was observed for a specific high-pressure RO experiment, the underlying mechanisms and broader performance of high-pressure RO for PFAS remain insufficiently characterized, and the result should not be generalized beyond the reported context.

### Unresolved or unsupported boundaries

- The specific water matrix composition (e.g., presence of co-solutes or natural organic matter) for the RO experiments is not described in the provided evidence.
- The exact membrane model, material, or manufacturer is not specified in the provided evidence.
- Quantitative permeate concentrations or rejection values as a function of each individual pressure step between 13.79 and 55.16 bar are not given; only the summary statement of above 99.98% removal and a qualitative increase with pressure is reported.
- Any detailed mechanistic explanation of PFAS removal in high-pressure RO (beyond the statement that mechanisms are largely unknown) is not provided in the evidence.

### Complete approved source chunks

#### WF10_023_MMG001

- Role: `required_gold`
- Document: `2024 - Ma - Evaluation of commercial nanofiltration and reverse osmosis membrane filtration to.pdf`
- Chunk: `34`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=f53f5c49622474f4574abb4f0c579269619a52b0674a6d413da3787b6d60420f].

```text
[SOURCE_TEXT_OMITTED sha256=9685c64c89d53be5de8bbc1c135d8d43bb091e04b11e8a3f335b0f0914264633]
```

#### WF10_023_MMG002

- Role: `required_gold`
- Document: `2024 - Ma - Evaluation of commercial nanofiltration and reverse osmosis membrane filtration to.pdf`
- Chunk: `34`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=030418d41ac75c4a4b432c22a877f17df5746eea0f288a37a192f983aa17a56d].

```text
[SOURCE_TEXT_OMITTED sha256=9685c64c89d53be5de8bbc1c135d8d43bb091e04b11e8a3f335b0f0914264633]
```

#### WF10_023_MMG003

- Role: `required_gold`
- Document: `2024 - Ma - Evaluation of commercial nanofiltration and reverse osmosis membrane filtration to.pdf`
- Chunk: `31`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=a1707bb5bbf861051d0d9cb579af8cf60de7d99c282294dc0b2c6a984e25c9ca].

```text
[SOURCE_TEXT_OMITTED sha256=162d2893078b11a4b33c7dafce9fe19a7c9663f57c9f8a5c4cd2269cc6128ee7].
```

---

## WF10_026

**Question:** What cautions apply when using early hydrogel sorbent results to infer broad PFAS removal performance?

### Task components

- `WF10_026-T01`: Assess whether broad claims about PFAS removal performance made from early hydrogel sorbent results are directly supported, partially supported, unsupported, or overgeneralized, with particular attention to compound-specific failures and partial removals that would limit any universal all-PFAS removal claim.
- `WF10_026-T02`: Specify what additional evidence would be required to legitimately support a stronger, broader PFAS removal claim (e.g., broader compound coverage, performance across differing conditions), without introducing new study-specific details, numeric values, mechanisms, materials, protocols, citations, or units, and without converting condition-specific findings into a universal PFAS treatment claim.

### Normative claim groups

#### WF10_026-G01

- Component: `WF10_026-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Early hydrogel sorbent results show PFAS-removal behavior that is strongly compound- and formulation-specific, so using these results to claim broad or universal all-PFAS removal is overgeneralized rather than fully supported.
- Full: Count as fully supported if the answer explicitly states that early hydrogel sorbent data do not justify broad all-PFAS removal claims because performance is compound-specific and formulation-specific, citing examples where sorption of some PFAS is limited (e.g., larger PFAS or short-chain PFAS) and explaining that this makes universal claims overgeneralized.
- Partial: Count as partially supported if the answer notes that performance varies among PFAS or formulations, but does not clearly connect this variation to the overgeneralization problem for all-PFAS claims.
- Contradiction: Mark as contradicted if the answer asserts or implies that early hydrogel results on a limited PFAS set are sufficient to support universal all-PFAS removal claims, or that performance is uniformly high across all PFAS without mentioning the documented limitations.
- Linked exact evidence:
  - `WF10_026_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=0bee0b85e0d9ed45d1cb7116b843103721edc1d3eaf963bdca833320a4f89880].
    Supports: Shows that changing crosslinking density in the hydrogel can limit removal of larger PFAS molecules and, as supported by the associated binding data in the study, can also limit sorption of PFOA and PFOS at high crosslinking density, highlighting formulation-dependent and size-dependent performance rather than uniform removal.
  - `WF10_026_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=09b81cff52c2852f735681a2ef1a4f86a49eb5385cc2cb99ab67e05104427e78].
    Supports: Shows a system where strong removal of PFOA and PFOS coexists with poor performance or unselectivity toward short-chain PFAS, illustrating compound-specific behavior and that success for some PFAS does not guarantee success for all.
  - `WF10_026_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=d2a82874c4a24d17e11d0325897d0792d5d1b4bbccb128b793bbec4a3befed61];
    Supports: Indicates that even for a single PFAS (PFOA), hydrogel performance is sensitive to synthesis parameters and that excess of particular components or over-crosslinking can limit other functionalities and hinder PFAS interactions, arguing against simple extrapolation of results from one optimized formulation to broad, robust PFAS removal.

#### WF10_026-G02

- Component: `WF10_026-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: To legitimately support a stronger, broader PFAS removal claim for hydrogel sorbents, additional evidence is needed that tests a wider range of PFAS and evaluates performance under environmentally relevant conditions and with background species and competing PFAS present.
- Full: Count as fully supported if the answer explicitly notes that broader PFAS removal claims would require evidence covering more PFAS types and realistic conditions, such as tests with competing short-chain PFAS, different crosslinking densities, environmentally relevant waters (groundwater or surface water), and the influence of background species.
- Partial: Count as partially supported if the answer mentions a need for some additional testing (e.g., more PFAS or environmental matrices) but omits key aspects like competing PFAS, crosslinking variations, or background species.
- Contradiction: Mark as contradicted if the answer suggests that no further evidence is needed, or fails to acknowledge that current work itself calls for additional studies under broader conditions.
- Linked exact evidence:
  - `WF10_026_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=5d5118e67ea6197c38bba86545469eb410ddff60efbf8c824507e00497baf3d7].
    Supports: Shows that the authors themselves state that further studies are needed to evaluate these sorbents under environmentally relevant conditions (e.g., groundwater or surface water), indicating that current evidence is not yet sufficient for strong broad claims.
  - `WF10_026_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=0bee0b85e0d9ed45d1cb7116b843103721edc1d3eaf963bdca833320a4f89880].
    Supports: Indicates that further work with additional crosslinking densities and binding studies including competing short-chain PFAS is planned, so current data do not yet provide comprehensive coverage of PFAS behavior or competition effects.
  - `WF10_026_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=63cddd91426ceb90506a00a2a26c8709d7e043c9ab6d01100501103acd08963e].
    Supports: Identifies a gap in existing PFAS remediation studies concerning how background species affect PFAS adsorption and implies that, because these background species can strongly influence adsorbent performance, systematic evaluation of their impact is needed before broad performance under realistic conditions can be claimed.

#### WF10_026-X01

- Component: `WF10_026-T01`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: Current PFAS remediation and hydrogel studies explicitly acknowledge gaps, including limited evaluation of background species and the need for future work under environmental conditions and with broader PFAS coverage, so their findings should not be interpreted as universally applicable.
- Full: Use this constraint to prevent answers from implying that existing hydrogel studies have already addressed all relevant matrices, PFAS types, and cofactors; answers should recognize that authors call out these gaps.
- Partial: Partially satisfied if the answer hints at remaining uncertainties but does not clearly root them in the authors’ stated gaps.
- Contradiction: Violated if the answer states or implies that the current studies already cover all relevant PFAS and environmental conditions, ignoring explicit calls for further work.
- Linked exact evidence:
  - `WF10_026_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=63cddd91426ceb90506a00a2a26c8709d7e043c9ab6d01100501103acd08963e].
    Supports: Concretely identifies a gap (impact of background species) in current PFAS remediation studies, cautioning against overgeneralization to real waters where such species are present.
  - `WF10_026_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=5d5118e67ea6197c38bba86545469eb410ddff60efbf8c824507e00497baf3d7].
    Supports: Shows that the authors do not consider their current data to fully represent environmental conditions, reinforcing that broad performance claims would be premature.
  - `WF10_026_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=0bee0b85e0d9ed45d1cb7116b843103721edc1d3eaf963bdca833320a4f89880].
    Supports: Indicates that key aspects (additional crosslinking densities and competitive binding with short-chain PFAS) remain to be tested, so current findings are incomplete.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

Early hydrogel sorbent results do not directly support broad or universal all‑PFAS removal claims; at most, they partially support more limited, compound‑ and condition‑specific claims.

For task component WF10_026-T01 (assessment of broad claims and compound-specific limitations):

The available evidence shows that PFAS removal by hydrogel‑based and related sorbents is strongly dependent on both the sorbent formulation and the specific PFAS involved. In a poly(acrylamide)‑based hydrogel system, the authors report that increasing crosslinking density was expected to reduce access for larger PFAS and that their binding data are consistent with limited sorption of even legacy PFAS at high crosslinking: “[SOURCE_TEXT_OMITTED sha256=e471c4b76df3e4aaf415b62215e172ae9d80995090da7760b0306294787ce6bb] “the systems with the highest crosslinking densities appear to limit some of the PFOA and PFOS sorption.” [WF10_026_MMG002] This indicates that performance is not uniformly high even for PFOA and PFOS, and that results from a particular crosslinking regime cannot be assumed to extend to all PFAS.

Similarly, work comparing hydrogel systems with powdered activated carbon (PAC) shows pronounced compound‑specific behavior. The authors state that “PAC outperformed all sorbents in removing PFOA and PFOS,” yet [SOURCE_TEXT_OMITTED sha256=1d1c91610d023b975c45f9545288727a3b6e402b29e062bae98f7fa92f93cf2d].” [WF10_026_MMG003] This demonstrates that strong performance for long‑chain legacy PFAS can coexist with poor or unselective performance for short‑chain PFAS, so strong removal of one PFAS subset cannot be interpreted as evidence of broad effectiveness across all PFAS.

In alginate‑based hydrogels functionalized with a cationic surfactant, the authors highlight that PFOA remediation “presents challenges in optimizing the quantities of its constituents … since any of these factors in excess can limit other functionalities,” and that “[SOURCE_TEXT_OMITTED sha256=6b137e45c23ed0b2c0be927f1bac34686e404cce118d41b5540996a9f115f057].” [WF10_026_MMG005] This shows that even for a single target PFAS, effective adsorption depends sensitively on tuned synthesis parameters; over‑crosslinking or excess surfactant can diminish PFAS interactions. Such sensitivity further undermines attempts to generalize early, optimized results to a blanket claim of robust removal for all PFAS.

Taken together, these observations mean that early hydrogel sorbent studies provide evidence for promising removal of specific PFAS under particular formulations and test conditions, but they also reveal clear compound‑specific limitations and performance trade‑offs. Using these early results to infer broad, all‑PFAS removal performance would therefore be overgeneralized and not directly supported by the cited work.

For task component WF10_026-T02 (additional evidence required for stronger, broader claims):

The same studies explicitly identify important gaps that would need to be addressed before making stronger, broader PFAS removal claims. One hydrogel study notes that “[SOURCE_TEXT_OMITTED sha256=d30d1e5a79473af3d4247f8bf1d0a589d92caec90c1adb983c16568137f932a1]” and points out that PFAS occur at trace concentrations while background species are present at much higher levels, so “the potential influence of these background species on adsorbent performance warrants careful consideration.” [WF10_026_MMG001] This implies that data in simple laboratory waters are not enough; broader claims would require systematic testing in the presence of typical background species at realistic relative concentrations.

Authors working on reusable hydrogel-based sorbents similarly emphasize that “[SOURCE_TEXT_OMITTED sha256=311316854dc7500815b0c21482bb563c2513fd38249a965bc028fa35ca0eb1a3].” [WF10_026_MMG004] This directly states that validation under environmentally relevant matrices (groundwater, surface water) and conditions is lacking. Without such studies, extending current findings to general environmental applications or to all PFAS would not be justified.

The poly(acrylamide) hydrogel composite study further notes that their mechanistic [SOURCE_TEXT_OMITTED sha256=d0234e30ba77e8f20605b92c2799f8af9a51a4bb566ee4914c2a7bdc894ba559].” [WF10_026_MMG002] This acknowledges that current data do not yet span the full range of crosslinking densities or competitive conditions needed to characterize selectivity across PFAS of different chain lengths.

Collectively, the cited authors themselves indicate what additional evidence is required for stronger and broader claims: (i) tests over a wider range of hydrogel formulations (e.g., crosslinking densities) to map how structure controls sorption across different PFAS; (ii) binding and competition studies that explicitly include short‑chain PFAS alongside legacy analytes; (iii) experiments that incorporate typical background species at realistic levels; and (iv) evaluations of sorption kinetics and performance in environmentally relevant waters such as PFAS‑contaminated groundwater and surface water. Until such evidence is available, early hydrogel sorbent results should be interpreted as promising but limited, and not as proof of universal all‑PFAS removal.

### Unresolved or unsupported boundaries

- Whether any specific hydrogel formulation achieves consistently high removal across a very large number of distinct PFAS beyond those mentioned (e.g., additional functional groups or chain lengths not cited in the evidence) is not addressed in the supplied texts.
- Long-term stability, fouling behavior, and performance over many regeneration cycles for hydrogel sorbents across diverse PFAS and complex matrices are not discussed in the provided evidence.
- Quantitative performance metrics (e.g., precise capacities, breakthrough behaviors, or kinetic rate constants) necessary to benchmark hydrogel sorbents against other technologies for a broad suite of PFAS are not provided in the excerpts.

### Complete approved source chunks

#### WF10_026_MMG001

- Role: `required_gold`
- Document: `2024 - Shaikh - Highly Efficient Cationic Surfactant Functionalized Alginate Hydrogel for Perfluorooctanoic Acid Adsorption - Optimization through Response Surface.pdf`
- Chunk: `7`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=63cddd91426ceb90506a00a2a26c8709d7e043c9ab6d01100501103acd08963e].

```text
[SOURCE_TEXT_OMITTED sha256=ee0b39476ed70e67944fa8da0c1be9901a63c836303a2ab218fd2595fac5c9c6]
```

#### WF10_026_MMG002

- Role: `required_gold`
- Document: `2023 - Klaus - Development of Poly(acrylamide)-Based Hydrogel Composites with Powdered Activated Carbon for Controlled Sorption of PFOA and PFOS in Aqueous Systems.pdf`
- Chunk: `42`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=0bee0b85e0d9ed45d1cb7116b843103721edc1d3eaf963bdca833320a4f89880].

```text
[SOURCE_TEXT_OMITTED sha256=dc64a5c7b00b9ffd0b838dc8fa3c58ad5a2c2b1f8404dc2cb5931c2353d47f23]
```

#### WF10_026_MMG003

- Role: `required_gold`
- Document: `2023 - Klaus - Development of Poly(acrylamide)-Based Hydrogel Composites with Powdered Activated Carbon for Controlled Sorption of PFOA and PFOS in Aqueous Systems.pdf`
- Chunk: `40`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=09b81cff52c2852f735681a2ef1a4f86a49eb5385cc2cb99ab67e05104427e78].

```text
[SOURCE_TEXT_OMITTED sha256=99fc50b1510c1742c94d03afccd86a02ec1a97060d9c13429826ca6626216aa4]-
```

#### WF10_026_MMG004

- Role: `required_gold`
- Document: `2018 - Huang - Reusable Functionalized Hydrogel Sorbents for Removing Long- and Short-Chain Perfluoroalkyl Acids (PFAAs) and GenX from Aqueous Solution.pdf`
- Chunk: `25`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=5d5118e67ea6197c38bba86545469eb410ddff60efbf8c824507e00497baf3d7].

```text
[SOURCE_TEXT_OMITTED sha256=bb120f104ae075bcdf2eb91cc7ea620c5c2cce8aaf2b2ccac0b7ee037ab8eee4]-
```

#### WF10_026_MMG005

- Role: `optional_gold`
- Document: `2024 - Shaikh - Highly Efficient Cationic Surfactant Functionalized Alginate Hydrogel for Perfluorooctanoic Acid Adsorption - Optimization through Response Surface.pdf`
- Chunk: `6`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=d2a82874c4a24d17e11d0325897d0792d5d1b4bbccb128b793bbec4a3befed61];

```text
[SOURCE_TEXT_OMITTED sha256=0c8d4c9eb2b0d96f19d1cf45e148e334cd0731da868c79fffad8f496d3c92fc4]
```

---

## WF10_027

**Question:** What mass-balance discrepancies and possible causes have been reported during regeneration-cycle evaluation of PFAS-removal membranes?

### Task components

- `WF10_027-T01`: Extract the regeneration-cycle evaluation protocol for the PFAS-removal membranes, including the sequence of regeneration steps, the use of ethanol (including reported concentration), other reagents or materials involved, operating conditions, and the water or environmental matrix and target PFAS compounds studied.
- `WF10_027-T02`: Extract how membrane performance was restored across regeneration cycles (e.g., described degree or extent of regeneration or recovery of removal performance), noting any reported limitations or caveats specific to the regeneration outcomes.
- `WF10_027-T03`: Extract any reported mass-balance discrepancies observed during regeneration-cycle evaluation of the PFAS-removal membranes (e.g., incomplete accounting of PFAS between feed, permeate, retentate, and regenerant streams) and the possible causes or explanations proposed in the source, along with any limitations or uncertainties the authors note about these discrepancies.

### Normative claim groups

#### WF10_027-G01

- Component: `WF10_027-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: During regeneration-cycle evaluation, a dual-functional mixed-matrix-composite nanofiltration membrane treating spiked tap water contaminated with PFOA was regenerated after filtration by an ethanol-based desorption step, concentrating PFOA in an ethanol eluent; the study matrix was spiked tap water and the target compound was PFOA.
- Full: Award full credit if the answer identifies that the membrane treated spiked tap water containing PFOA and that regeneration after filtration used an ethanol eluent in which PFOA was concentrated, indicating desorption from the membrane; it should also correctly name PFOA as the target compound and ethanol as the regenerant, without adding unsupported details such as ethanol concentration or unreported reagents.
- Partial: Award partial credit if the answer mentions ethanol-based regeneration and PFOA as the target in spiked tap water but omits either the membrane type or the concentration of PFOA in ethanol, or if it conflates but does not invent unsubstantiated details.
- Contradiction: Mark as contradictory if the answer states that regeneration did not use ethanol, that a different PFAS was the sole target instead of PFOA, or that the matrix was something other than spiked tap water, contrary to the evidence.
- Linked exact evidence:
  - `WF10_027_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > tion after spiked tap-water ﬁltration fully restored the membrane adsorption capacity.
    Supports: Identifies that the membrane was used for spiked tap-water filtration and that a post-filtration step (regeneration) was performed.
  - `WF10_027_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=b1f8d856126bf26c0eaa37a196b4990c93eaa4ba0adacc1903084cf3377d6c92]).
    Supports: Shows that regeneration involved desorption into an ethanol eluent with high PFOA concentration, confirming ethanol use and PFOA as the target compound.
  - `WF10_027_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=a99e9c250e44baa592e15752da75320e7a218493d8e4b69e3262d538277b3be5],
    Supports: Indicates that PFOA was concentrated in ethanol during regeneration, supporting ethanol as the regenerant and PFOA as the target PFAS.

#### WF10_027-G02

- Component: `WF10_027-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Across regeneration cycles, the membrane’s PFOA removal performance and adsorption capacity were restored to their initial levels after each regeneration step, while salt rejection was not significantly affected; however, pure water permeance decreased by about 30% and average water flux during filtration steps decreased by 12%, indicating some performance tradeoffs.
- Full: Award full credit if the answer states that regeneration restored PFOA removal rate and membrane adsorption capacity after each cycle, that salt rejection was not significantly affected, and that pure water permeance and average water flux decreased (with directionality and presence of a decrease correctly described), indicating a tradeoff in hydraulic performance.
- Partial: Award partial credit if the answer mentions restoration of PFOA removal and some indication of performance tradeoffs (e.g., decreased permeance or flux) but omits other aspects such as salt rejection or does not clearly relate these to regeneration.
- Contradiction: Mark as contradictory if the answer claims that PFOA removal was not restored, that adsorption capacity decreased after regeneration, or that permeance increased, directly opposing the evidence.
- Linked exact evidence:
  - `WF10_027_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > tion after spiked tap-water ﬁltration fully restored the membrane adsorption capacity.
    Supports: States that the regeneration step fully restored membrane adsorption capacity.
  - `WF10_027_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=99eec8f55035ab262eaf87c677891c629f3ccbf50e824dea433e00c1d13be222],
    Supports: Shows that PFOA removal rate was restored to the initial value after each regeneration step, indicating recovery of performance.
  - `WF10_027_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > The regeneration step did not signiﬁcantly affect the salt rejection.
    Supports: Indicates that salt rejection was not significantly affected by regeneration.
  - `WF10_027_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=07c689e3970047998332efa72db6d757d2ccf6c0aa24c7457752642bb8a0e63a]).
    Supports: Provides the reported decreases in pure water permeance and average water flux associated with regeneration cycles.
  - `WF10_027_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=8b63ab2e8c003a86bb981d87cd20c4e83b34cf023e0e4e0f136060256b086d16]
    Supports: Summarizes that regeneration desorbs practically all PFOA into ethanol and restores PFOA removal.

#### WF10_027-G03

- Component: `WF10_027-T03`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Mass-balance evaluation during regeneration cycles showed that PFOA was concentrated in the ethanol regenerant by a factor of 10–38 relative to the feed, but with a 29% PFOA surplus after the second cycle and a 19% deficit after the third cycle; the authors suggest these discrepancies may stem from adsorption or desorption on tubing or from analytical issues.
- Full: Award full credit if the answer reports that mass balance showed PFOA was concentrated in ethanol by a factor in the 10–38 range and that there was a PFOA surplus after the second cycle and a deficit after the third cycle, with the discrepancies potentially due to tubing adsorption/desorption or analytical issues.
- Partial: Award partial credit if the answer notes the presence of mass-balance discrepancies and suggests tubing or analytical issues as possible causes but omits the specific surplus/deficit character or the concentration factor, or if it mentions surplus/deficit without the proposed causes.
- Contradiction: Mark as contradictory if the answer claims there were no mass-balance discrepancies, or attributes the discrepancies to causes that contradict the evidence (e.g., stating they were definitively due to membrane degradation rather than tubing or analytical issues).
- Linked exact evidence:
  - `WF10_027_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=4c24f2f0fc0aeb0d27d7ecc7b90c005353e44a8e6db36a9fbe33ad4558b46550]).
    Supports: Provides the reported concentration factor range and the specific surplus and deficit percentages observed in the second and third regeneration cycles.
  - `WF10_027_MMG001`
    > These discrepancies may be related to adsorption/desorption from tubing or analytical issues.
    Supports: States the authors’ proposed possible causes for the observed mass-balance discrepancies.

#### WF10_027-G04

- Component: `WF10_027-T02`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: The authors note that much higher PFOA concentration factors in the ethanol regenerant should be possible by using a lower eluent-volume to membrane-surface-area ratio and lower PFOA feed concentration, but achieving this would require long-duration experiments and a larger membrane surface area than used in the study, representing a limitation of the current regeneration evaluation.
- Full: Award full credit if the answer explains that the authors expect higher PFOA concentration factors with lower eluent-volume to membrane-area ratio and lower PFOA feed concentration, but that realizing this would require longer experiments and larger membrane area than used, framing this as a limitation or caveat of the current regeneration evaluation.
- Partial: Award partial credit if the answer mentions either the expectation of higher concentration factors or the need for longer experiments / larger membrane area, but not both aspects together.
- Contradiction: Mark as contradictory if the answer claims that the current setup already achieves the maximum possible concentration factors or denies that longer experiments or larger membrane area would be needed for improvement.
- Linked exact evidence:
  - `WF10_027_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=0580788470bd0c6775c63963ecf2193187f31f12e6179dda3cfb19afc35b341a].
    Supports: Indicates that higher concentration factors are expected under different conditions and that achieving them would require longer experiments and a higher membrane surface area than in the present study, pointing to limitations of the current regeneration evaluation.

#### WF10_027-X01

- Component: `WF10_027-T01`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: The available evidence does not report the ethanol concentration, detailed sequence of regeneration steps (such as durations, flow rates, or pressures), or the use of any regenerants other than ethanol, nor does it indicate treatment of PFAS other than PFOA.
- Full: Answers must not introduce unreported ethanol concentrations, detailed operating conditions, other regenerants, or additional PFAS compounds beyond PFOA, because these are not specified in the evidence.
- Partial: If an answer partially speculates on unreported conditions while mostly adhering to the evidence, it should be treated cautiously and not given full credit for protocol detail.
- Contradiction: Treat as violating constraints if the answer confidently specifies ethanol concentration, flow conditions, additional reagents, or additional PFAS targets that are not present in the evidence.
- Linked exact evidence:
  - `WF10_027_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=b1f8d856126bf26c0eaa37a196b4990c93eaa4ba0adacc1903084cf3377d6c92]).
    Supports: Shows that ethanol is used as an eluent but does not specify its concentration or additional regenerants, constraining what can be claimed about protocol details.
  - `WF10_027_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=a99e9c250e44baa592e15752da75320e7a218493d8e4b69e3262d538277b3be5],
    Supports: Identifies PFOA as the target compound but does not mention any other PFAS, indicating that additional PFAS targets should not be inferred.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

In the reported regeneration-cycle evaluation, a dual-functional mixed-matrix-composite nanofiltration membrane was used to treat spiked tap water containing PFOA. After spiked tap-water filtration, a regeneration step was performed in which PFOA was desorbed from the membrane into an ethanol eluent. The high PFOA concentration measured in the ethanol eluent indicated successful desorption and showed that PFOA was being transferred from the membrane into the regenerant.

Regarding regeneration performance, the authors state that the regeneration step fully restored the membrane adsorption capacity. The PFOA removal rate returned to the high initial value after each regeneration step, indicating effective recovery of the PFAS-removal function across cycles. The regeneration step did not significantly affect salt rejection. However, there were hydraulic performance tradeoffs: pure water permeance decreased by about 30%, and the average water flux during the filtration steps was reduced by about 12%. The authors also note [SOURCE_TEXT_OMITTED sha256=a055a27bbf49c174aa2a4021e921f8de1e08ea2b3a120bd4c86a07e8b17d021d] significantly shorter times than the filtration time, thereby restoring PFOA removal.

The mass-balance evaluation focused on PFOA between the feed and the ethanol regenerant. The analysis showed that PFOA was concentrated in ethanol by a factor of 10–38 compared to the feed. Despite this concentration, discrepancies in the mass balance were observed between regeneration cycles: there was a 29% PFOA surplus after the second cycle and a 19% PFOA deficit after the third cycle. The authors attribute these discrepancies to possible adsorption or desorption from tubing or to analytical issues, indicating that not all of the imbalance could be confidently assigned to the membrane itself.

As a caveat, the authors explain that much higher concentration factors should be attainable in principle by using a lower eluent-volume to membrane-surface-area ratio and a lower PFOA feed concentration. Achieving these conditions would require long-duration experiments and a larger membrane surface area than was used in the present study, so the current regeneration evaluation is limited in this respect. The evidence does not specify the ethanol concentration, detailed operating conditions of the regeneration (such as pressures, flow rates, or times), additional reagents, or PFAS compounds other than PFOA.

### Unresolved or unsupported boundaries

- The ethanol concentration used during regeneration is not reported.
- The detailed stepwise regeneration protocol (e.g., sequence of flushing, contact times, pressures, and flow rates) is not provided.
- The presence or absence of additional regenerants or reagents besides ethanol is not specified.
- Operating conditions such as transmembrane pressure, temperature, or crossflow velocity during regeneration are not given.
- Treatment or evaluation of PFAS other than PFOA is not mentioned.
- Detailed accounting of permeate and retentate streams during mass-balance analysis (beyond the ethanol regenerant and feed) is not described.

### Complete approved source chunks

#### WF10_027_MMG001

- Role: `required_gold`
- Document: `2023 - Chaudhary - Efficient PFOA removal from drinking water by a dual-functional mixed-matrix-composite nanofiltration membrane.pdf`
- Chunk: `19`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=990d2ab911b160d863ba86eecb03ed98665ceab497a9a451a9a68d61f3ad81d4].

```text
[SOURCE_TEXT_OMITTED sha256=9295204fa2464aaa4d6bacaf6504614e9fd36724acf76203b402770cee537fea]
```

---

## WF10_028

**Question:** How does increasing membrane-modifier loading affect PFAS rejection, and what limitations are reported?

### Task components

- `WF10_028-T01`: Extract how increasing membrane-modifier loading is reported to affect PFAS rejection, including the available PFOA, total-PFAS, and PFOS examples; report the direction and extent of change, any plateau or loss of improvement, and any stated limitations or tradeoffs at higher loadings.
- `WF10_028-T02`: Evaluate whether the claim about PFAS/PFOA rejection improvement with increasing membrane-modifier loading and any plateau/limitations is directly supported, partially supported, unsupported, or overgeneralized by the described evidence, and state what additional evidence or data would be needed to justify any stronger or more general claim without converting a condition-specific finding into a universal PFAS treatment claim.

### Normative claim groups

#### WF10_028-G01

- Component: `WF10_028-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In a MOF-incorporated dual-layer membrane, increasing MOF loading in the hydrophilic layer increases PFOA rejection until it plateaus at about two-thirds rejection when 5% MOF is incorporated.
- Full: Award full credit if the answer states that in the cited MOF-incorporated dual-layer membrane system, increasing MOF loading in the hydrophilic layer increased PFOA rejection but that rejection plateaued at a reported plateau value when 5% MOF was incorporated. The description must clearly indicate both improvement with added MOF and the plateau at 5% loading.
- Partial: Award partial credit if the answer mentions that PFOA rejection increased with added MOF or that it plateaued at a certain loading, but does not clearly connect both trends (increase then plateau at 5% MOF) or omits the plateau nature.
- Contradiction: Mark as contradictory if the answer claims that PFOA rejection continued to increase beyond 5% MOF without plateau, or that adding MOF did not improve PFOA rejection at all in this system.
- Linked exact evidence:
  - `WF10_028_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=fef3d658a0d9d162c2836092a4040cdc736597d2cf6e37b8c6e2791f5a4c682e].
    Supports: Shows that PFOA rejection increases with more MOF in the hydrophilic layer but reaches a plateau at 65.6% when 5% MOF is incorporated.

#### WF10_028-G02

- Component: `WF10_028-T01`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: In the same MOF-modified membrane series, total PFAS rejection increased with modifier loading from the pristine membrane to an intermediate loading and then plateaued at higher loading.
- Full: Award full credit if the answer notes that total PFAS rejection increased from the pristine PTFE membrane to the MOF-modified PSA5 membrane and then plateaued (i.e., did not further increase) at the higher-loading PSA10 membrane.
- Partial: Award partial credit if the answer only mentions improvement of total PFAS rejection with MOF incorporation but omits that rejection plateaus at higher loading, or vice versa.
- Contradiction: Mark as contradictory if the answer states that total PFAS rejection decreases when going from pristine PTFE to PSA5, or that it keeps increasing beyond PSA5 without plateau under the described conditions.
- Linked exact evidence:
  - `WF10_028_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=b85e0cffd94639d6a5e6c22f3b9bfb600253940a392c94e1dc3159c90d7b257b].
    Supports: Shows total PFAS rejection increases from pristine PTFE to PSA5 and then plateaus at a similar level for PSA10.

#### WF10_028-G03

- Component: `WF10_028-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: For MXene-modified thin-film composite/nanocomposite membranes, increasing MXene loading beyond an optimal value leads to a slight decrease in PFOS rejection due to agglomeration and defect formation.
- Full: Award full credit if the answer explains that in MXene-modified membranes, increasing MXene concentration beyond an optimal loading (e.g., to 0.050%) causes a slight decrease in PFOS rejection, and that this reduction is linked to agglomeration of MXene nanosheets and the resulting defects in the PA layer.
- Partial: Award partial credit if the answer only notes a decrease in rejection at higher MXene loading or only mentions agglomeration-related defects without clearly linking them to a slight rejection decrease.
- Contradiction: Mark as contradictory if the answer claims PFOS rejection continues to increase monotonically with MXene loading up to the highest tested concentration, or that higher MXene loading has no impact on rejection or membrane integrity.
- Linked exact evidence:
  - `WF10_028_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=11c95bad72f161e9b28232986147316bdc2d89a9696e6738383f22efdde25454].
    Supports: Shows that at higher MXene concentration (0.050%), rejection slightly decreases (about 4%) and attributes this to agglomeration-induced defects in the PA layer.

#### WF10_028-G04

- Component: `WF10_028-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In MXene–TiO2 composite RO membranes, increasing composite loading from an optimal level to a higher level causes a slight decline in PFOA rejection, interpreted as arising from agglomeration and increased nano-defect probability, though PFOA selectivity remains high.
- Full: Award full credit if the answer notes that in the MXene–TiO2 RO membrane series, increasing composite loading from M3 to M4 caused a small drop in PFOA rejection and that this was attributed to agglomeration of excess composite loading and increased nano-defect probability, while maintaining relatively high selectivity for PFOA.
- Partial: Award partial credit if the answer only mentions a slight decline in PFOA rejection at higher loading or only mentions agglomeration/nano-defects without clearly connecting them to the observed slight decline in PFOA rejection.
- Contradiction: Mark as contradictory if the answer asserts that PFOA rejection increases when moving from M3 to M4, or that excess composite loading causes no change in PFOA rejection.
- Linked exact evidence:
  - `WF10_028_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=ce46158b8ad7b6b5680ff66bb33360c0d6b776b251e42af969c01b9820916fce]%).
    Supports: Provides the observation that PFOA rejection slightly declines when moving from M3 to M4, and that the drop is smaller than for Na2SO4.
  - `WF10_028_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=463b373875c7287b82e922e9e0cbdf78a9cb861b938408907adf79ca7344cea8].
    Supports: Interprets the effect of excess composite loading in M4 as causing some agglomeration and increased nano-defect probability, but with limited impact on PFOA selectivity versus smaller ions.

#### WF10_028-G05

- Component: `WF10_028-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: The evidence directly supports that PFAS/PFOA rejection increases with modifier loading up to an optimal range and then plateaus or slightly declines in the studied systems, but does not justify a universal assumption that further loading always improves PFAS rejection across membranes and PFAS types.
- Full: Award full credit if the answer (1) classifies the claim that PFOA/PFAS rejection always continues to improve with increasing modifier loading as overgeneralized or not fully supported, (2) explains that the cited studies show increased rejection only up to an optimal loading followed by plateau or slight decline, and (3) notes that broader generalization would require more data across membrane types, loadings, PFAS, and conditions.
- Partial: Award partial credit if the answer recognizes that the findings are condition-specific or that there is a plateau/decline, but does not clearly address overgeneralization or specify the additional evidence needed for stronger claims.
- Contradiction: Mark as contradictory if the answer asserts that the evidence proves a universal trend that more modifier loading always increases PFAS/PFOA rejection without plateau or limitation.
- Linked exact evidence:
  - `WF10_028_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=fef3d658a0d9d162c2836092a4040cdc736597d2cf6e37b8c6e2791f5a4c682e].
    Supports: Shows a plateau in PFOA rejection at 5% MOF, indicating that further loading beyond this point does not keep increasing rejection.
  - `WF10_028_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=b85e0cffd94639d6a5e6c22f3b9bfb600253940a392c94e1dc3159c90d7b257b].
    Supports: Shows total PFAS rejection improves then plateaus with increasing modifier loading (from pristine to PSA5 to PSA10).
  - `WF10_028_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=11c95bad72f161e9b28232986147316bdc2d89a9696e6738383f22efdde25454].
    Supports: Provides an example where increasing modifier loading beyond an optimal value causes a slight decrease in rejection, not continued improvement.
  - `WF10_028_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=ce46158b8ad7b6b5680ff66bb33360c0d6b776b251e42af969c01b9820916fce]%).
    Supports: Gives another example of a slight decline in PFOA rejection at higher composite loading, reinforcing that more modifier does not always yield better rejection.

#### WF10_028-X01

- Component: `WF10_028-T02`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: The reported effects of modifier loading on PFAS/PFOA rejection are specific to the studied membranes, PFAS species, and operating conditions and should not be treated as universally applicable to all PFAS treatment systems.
- Full: Use this constraint to prevent awarding credit to answers that extrapolate the observed trends (increase then plateau or slight decline) to all PFAS, all membranes, or all conditions. Answers should remain explicitly tied to the studied systems and not present the findings as universal.
- Partial: If an answer partially generalizes but still notes that results may be system-dependent, treat that as less severe but still constrained; emphasize the need for caution in generalization.
- Contradiction: This constraint is violated if an answer claims that any membrane with increased modifier loading will universally show similar PFAS rejection behavior without qualification.
- Linked exact evidence:
  - `WF10_028_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=b85e0cffd94639d6a5e6c22f3b9bfb600253940a392c94e1dc3159c90d7b257b].
    Supports: Refers to specific membranes (pristine PTFE, PSA5, PSA10) and total PFAS under defined conditions, implying system-specific behavior.
  - `WF10_028_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=11c95bad72f161e9b28232986147316bdc2d89a9696e6738383f22efdde25454].
    Supports: Indicates that the described effects are tied to a particular MXene–TFN membrane structure, not all membranes.
  - `WF10_028_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=ce46158b8ad7b6b5680ff66bb33360c0d6b776b251e42af969c01b9820916fce]%).
    Supports: Shows that the study focuses on specific fabricated membranes and particular PFAS, reinforcing that conclusions are system-specific.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

In the MOF-incorporated dual-layer membrane for landfill leachate, increasing MOF loading in the hydrophilic layer improves PFOA rejection but only up to a point. As reported, “[SOURCE_TEXT_OMITTED sha256=fef3d658a0d9d162c2836092a4040cdc736597d2cf6e37b8c6e2791f5a4c682e].” This indicates that beyond 5% MOF in the hydrophilic layer, additional MOF loading did not further increase PFOA rejection.

For total PFAS in the same membrane series, a similar trend is observed. The authors note [SOURCE_TEXT_OMITTED sha256=8bf0868a7720fc9797e1ff7476150e21540c4664d4e1f546796aed2fcb9766d0].” Thus, MOF modification substantially increases total PFAS rejection from the pristine membrane to the PSA5 configuration, but further loading in PSA10 does not meaningfully improve rejection, demonstrating a plateau in performance.

Other modifier systems similarly show that there is an optimal loading range and that excessive loading can introduce tradeoffs. In functionalized-MXene thin-film nanocomposite membranes, the study reports: “[SOURCE_TEXT_OMITTED sha256=11c95bad72f161e9b28232986147316bdc2d89a9696e6738383f22efdde25454].” Here, PFOS rejection is slightly reduced at higher MXene loading, and the limitation is tied to MXene agglomeration and defect formation in the selective layer.

In MXene–TiO2 composite reverse osmosis membranes, a similar limitation is seen for PFOA at higher composite loading. The authors state that the M4 [SOURCE_TEXT_OMITTED sha256=4150c044df53e2d6cae7444ead08caa463bc638bbc97a989378e5919d787a599],” and explain [SOURCE_TEXT_OMITTED sha256=0883c1218ae3ea0402d34e8b5768ad9fd623f1ed806eedd73331953351d3a8ef] drastically as it does for smaller salt ions.” This indicates that excessive composite loading introduces nano-defects and slightly lowers PFOA rejection, even though PFOA selectivity remains high relative to salts.

Taken together, these reports show that for the studied MOF and MXene-based membranes, increasing modifier loading initially enhances PFAS or PFOA rejection, but performance either plateaus (MOF dual-layer membranes for PFOA and total PFAS) or slightly declines (MXene-based membranes) once loading exceeds an optimal range, with limitations related to agglomeration and defect formation. Therefore, the idea that simply increasing MOF or other modifier loading will always continue to improve PFOA rejection is not supported by these data and would be an overgeneralization.

To justify a stronger or more general claim—such as that higher modifier loading consistently improves PFAS rejection across membrane types and PFAS species—additional evidence would be needed. This would include systematic studies spanning a broader range of modifier loadings for each membrane architecture, evaluation of multiple PFAS (short- and long-chain, different functional groups), testing under varied operating conditions and feed matrices, and comparative performance across different modifier chemistries and membrane platforms. Without such broader datasets, conclusions should remain limited to the specific systems and conditions documented in these studies.

### Unresolved or unsupported boundaries

- Any claim that increasing MOF or other modifier loading beyond the reported values will further improve PFOA or PFAS rejection in these systems is not supported by the provided evidence.
- Any claim that the observed increase-then-plateau or increase-then-decrease trends apply universally to all membrane types, modifier chemistries, PFAS species, or operating conditions is unsupported.
- Any mechanistic explanation beyond the explicitly mentioned agglomeration and defect formation (e.g., detailed transport mechanisms, specific structural metrics) would require additional data not provided here.
- Any specific optimal loading values, performance metrics, or behaviors for membranes, modifiers, or PFAS not mentioned in the evidence cannot be inferred from these studies.

### Complete approved source chunks

#### WF10_028_MMG001

- Role: `required_gold`
- Document: `2022 - Zhang - Study of MOF incorporated dual layer membrane with enhanced removal of ammonia and per- - poly-fluoroalkyl substances (PFAS) in landfill leachate.pdf`
- Chunk: `2`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=fef3d658a0d9d162c2836092a4040cdc736597d2cf6e37b8c6e2791f5a4c682e].

```text
[SOURCE_TEXT_OMITTED sha256=bc6b9717ec85b6d83a1e8e076f3eeb205c28c4bd33379201b1b32f56d514626b]
```

#### WF10_028_MMG002

- Role: `optional_gold`
- Document: `2022 - Zhang - Study of MOF incorporated dual layer membrane with enhanced removal of ammonia and per- - poly-fluoroalkyl substances (PFAS) in landfill leachate.pdf`
- Chunk: `29`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=b85e0cffd94639d6a5e6c22f3b9bfb600253940a392c94e1dc3159c90d7b257b].

```text
[SOURCE_TEXT_OMITTED sha256=fe0379b5cabe0a5fd7226bcead03bbcaed837925bc7ef98f21fec86e59f9b885]
```

#### WF10_028_MMG003

- Role: `required_gold`
- Document: `2022 - Le - Functionalized-MXene Thin-Film Nanocomposite Hollow Fiber Membranes for Enhanced PFAS Removal from Water.pdf`
- Chunk: `35`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=11c95bad72f161e9b28232986147316bdc2d89a9696e6738383f22efdde25454].

```text
[SOURCE_TEXT_OMITTED sha256=8b0b68b1b0c572d60ed768854c0a09604dae816687fd910e5094637752b78bff].
```

#### WF10_028_MMG004

- Role: `required_gold`
- Document: `2026 - Ghanbari - Harnessing phase engineered porous MXene-TiO2 in polyamide reverse osmosis membranes for enhanced short- and long chain PFAS removal from water.pdf`
- Chunk: `54`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=ce46158b8ad7b6b5680ff66bb33360c0d6b776b251e42af969c01b9820916fce]%).

```text
[SOURCE_TEXT_OMITTED sha256=0ade209382545b6e5549d59505e9e8ad4e864a290e88a3bb3b5c768a16bc0f20].
```

### Deterministic resolution

- Broadened T01 to match the visible question and the already-supported PFOA, total-PFAS, and PFOS claim groups.

---

## WF10_029

**Question:** What membrane, feed-water, and PFAS-mixture factors limit transferring PFAS removal results across water types?

### Task components

- `WF10_029-T01`: Identify membrane-related factors (e.g., specific membrane properties or operating conditions described in the study) that limit transferring PFAS removal results to other NF/RO membranes or systems, emphasizing any stated limitations, uncertainties, or caveats.
- `WF10_029-T02`: Identify feed-water–related factors (e.g., water matrix characteristics or co-contaminants described in the study) that constrain extrapolating PFAS removal performance to different water types, including any explicit negative or cautionary statements about such transfer.
- `WF10_029-T03`: Identify PFAS-mixture–related factors (e.g., composition, diversity, or concentrations of PFAS in the tested mixture) that limit generalizing the reported removal results to other PFAS mixtures, highlighting any limitations, uncertainties, or caveats noted by the authors.

### Normative claim groups

#### WF10_029-G01

- Component: `WF10_029-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Membrane operating configuration and membrane–solution interactions (e.g., bench- vs pilot-scale operation, concentration polarization, and charge-shielding effects during NF) limit how PFAS rejection results can be transferred to other NF/RO systems.
- Full: Award full credit when the answer notes that PFAS rejection results from specific membrane configurations or scales (e.g., bench-scale RO/NF, dead-end vs crossflow) and membrane–solution phenomena (e.g., concentration polarization, charge-shielding from highly rejected divalent cations, fouling-enhanced concentration polarization) may not translate directly to other NF/RO systems or operating conditions, explicitly framing these as limitations or caveats on transferring performance expectations.
- Partial: Award partial credit if the answer mentions at least one membrane- or operating-condition limitation (such as bench-scale vs pilot-scale performance differences, or charge-shielding effects) but does not clearly connect it to restricted transferability across NF/RO systems.
- Contradiction: Mark as contradictory if the answer suggests that bench-scale NF/RO PFAS rejection results or conditions with strong concentration polarization and charge-shielding can be broadly generalized to all NF/RO systems without limitation.
- Linked exact evidence:
  - `WF10_029_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=59b84c14dbc10df40aaf99ffb65b91e3b2a974de43b42a08c97a6c87750cb42e] ].
    Supports: Bench-scale RO/NF systems may not represent pilot- and full-scale performance because of configuration- and operation-specific issues such as leaking, concentration polarization, and dead-end rather than crossflow operation, limiting transferability of PFAS rejection results.
  - `WF10_029_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=7ee3f133dc67085f2b62b34def92e5539ad0e27852d1bb26ff6d84861d32240c].
    Supports: Pilot-scale PFAS rejection data can be uncertain (unquantifiable permeate, imprecise rejection), introducing additional limitations when using these results to predict performance in other systems.
  - `WF10_029_MMG003` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=e8cb18eae42072b02b61dad4b60dbeeb4dbfa9381af29fd89f1f1391695d6f0b]] .
    Supports: Under NF conditions where divalent cations are highly rejected, charge-shielding decreases electrostatic repulsion between PFAS and the membrane, reducing NF performance; this membrane–solution interaction may not occur similarly in other systems and thus constrains direct transfer of performance expectations.
  - `WF10_029_MMG003` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=f10bc71ab1c5fa1ba0c510729bf8a9652ffd47d6000629f19d3e199016f108c7]] .
    Supports: Fouling-enhanced concentration polarization at the membrane surface reduces PFAS rejection, indicating that membrane performance under such fouling conditions may not reflect performance in systems or conditions with different fouling behavior.

#### WF10_029-G02

- Component: `WF10_029-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Differences in water quality and composition between surface water, groundwater, and model waters (e.g., NOM/DOM levels, ionic strength, hardness, and divalent cations) create matrix-specific PFAS rejection behaviors that limit extrapolation of NF/RO removal across water types.
- Full: Award full credit when the answer highlights that water matrix properties—such as NOM/DOM content, ionic strength, hardness, presence of divalent cations, and the use of deionized or tap water instead of realistic surface/groundwater—alter fouling, electrostatic interactions, and NF/RO rejection mechanisms, and thus restrict straightforward transfer of PFAS removal performance between different water types.
- Partial: Award partial credit if the answer mentions at least one relevant matrix factor (e.g., NOM, ionic strength, divalent cations, or use of deionized/tap water) affecting PFAS rejection but does not clearly frame it as limiting extrapolation across water types.
- Contradiction: Mark as contradictory if the answer claims PFAS removal by NF/RO is generally independent of water quality, NOM/DOM, ionic strength, hardness, or cation composition, or implies that results from deionized/tap water directly represent surface and groundwater behavior.
- Linked exact evidence:
  - `WF10_029_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=7b2fe6a7f9b4c77f6be6a0b6e739c8281a3d7501575c6e70157528562227c8c7].
    Supports: Water quality and composition themselves affect the efficiency and rejection mechanisms of pressure-driven membranes, indicating that PFAS rejection is matrix-dependent and limiting simple transfer across water types.
  - `WF10_029_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=77bb7aee679f5b7aaf08df9ce1e1abf0c5f42478051223f53698bbf6760bb4c6].
    Supports: Higher NOM in surface water can cause higher fouling and affect membrane processes differently, so PFAS removal measured in one NOM condition may not apply to waters with different NOM levels.
  - `WF10_029_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=0ddb4c161c723a188210bd65cb3cf84091a6819b7fce0e9dae71da29e8e211bd]] .
    Supports: In groundwater, higher ionic strength and hardness change mechanisms such as size-exclusion and may reduce electrostatic repulsion, making PFAS rejection behavior different from that in other matrices.
  - `WF10_029_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=0a8a8d08b7550e8e7a2e22de05c5aa846a28bcb41cff1e20f044cf869124bbcb]] .
    Supports: DOM at higher concentrations, as in surface water, can compete with PFAS for adsorption and electrostatic interactions with NF membranes, leading to greater PFAS transport through membranes; this illustrates matrix-specific behavior that limits extrapolation to waters with different DOM levels.
  - `WF10_029_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=c3636cb1833a5448c8fc7ccc1321b7aae131cbc341a7e0dff8d0f943b0aac4c3].
    Supports: Divalent cations typical of groundwater can reduce NF performance, so PFAS removal observed in waters without such cations may not predict performance in groundwater.
  - `WF10_029_MMG003` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=698594fbf3e1b7f09605f7f093e68d620b28cd03676493fd479d7aae9e442687].
    Supports: Interactions between DOM and cations (formation of DOM–Ca2+ complexes) can increase membrane fouling, adding matrix-specific effects on PFAS rejection.
  - `WF10_029_MMG003` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=f10bc71ab1c5fa1ba0c510729bf8a9652ffd47d6000629f19d3e199016f108c7]] .
    Supports: DOM-induced fouling-enhanced concentration polarization reduces PFAS rejection, showing that DOM-rich waters behave differently from cleaner matrices.
  - `WF10_029_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=026b065a390b00c528ed061b4f404b17f3abe2d91f49270bb877bd3b7d253c4c] ].
    Supports: Use of deionized or tap water spiked with PFAS simplifies the water matrix relative to historically impacted sites, limiting how those PFAS rejection results can be extrapolated to more complex surface or groundwater conditions.

#### WF10_029-G03

- Component: `WF10_029-T03`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Simplified PFAS mixtures used in many NF/RO studies (e.g., single PFAS solutes or AFFF-spiked water focusing on PFAAs) omit numerous PFAS precursors such as perfluoroalkane sulfonamides, limiting generalization of removal results to complex PFAS mixtures at impacted sites.
- Full: Award full credit when the answer notes that many NF/RO PFAS studies use simplified PFAS mixtures (e.g., single PFAS or AFFF-spiked deionized/tap water) and focus on PFAAs, thereby omitting many PFAS precursors such as perfluoroalkane sulfonamides that occur at historically impacted sites, and explicitly identifies this as a limitation on generalizing removal performance to other PFAS mixtures.
- Partial: Award partial credit if the answer generally mentions that focusing on a subset of PFAS (e.g., only PFAAs or single compounds) limits extrapolation to broader PFAS mixtures but does not specify precursors or FASAs.
- Contradiction: Mark as contradictory if the answer claims that removal performance measured for single PFAAs or simplified AFFF-spiked systems can be broadly applied to all PFAS mixtures, including those with diverse precursors, without limitation.
- Linked exact evidence:
  - `WF10_029_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=026b065a390b00c528ed061b4f404b17f3abe2d91f49270bb877bd3b7d253c4c] ].
    Supports: Many studies focus on PFAAs in deionized or tap water spiked with AFFF or single PFAS, explicitly omitting the multitude of PFAA precursors that occur at historically impacted sites, indicating limited generalizability to more complex PFAS mixtures.
  - `WF10_029_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=4d69ab6c57ce7f28148dca610ee0cee7c2aace74aa35031d7641afa1c781f16d] ].
    Supports: Perfluoroalkane sulfonamides (FASAs) are identified as PFAS precursors often present at high concentrations at AFFF-impacted sites and as potentially more toxic than PFAAs, underscoring that PFAA-focused studies may not adequately represent behavior or risk for mixtures containing FASAs.

#### WF10_029-X01

- Component: `WF10_029-T02`
- Importance: `supplementary`
- Scoring role: `constraint_only`
- Proposition: The effect of natural organic matter or dissolved organic matter on PFAS removal by NF/RO is not consistent across studies, so the direction of its impact should not be universally generalized when transferring performance between water types.
- Full: Treat as a constraint when an answer might overgeneralize the role of NOM/DOM; full constraint satisfaction requires acknowledging that literature findings on NOM/DOM effects on PFAS transport and removal are not in consensus, with some studies indicating increased PFAS transport and others indicating enhanced removal.
- Partial: Partial satisfaction occurs if the answer hints that NOM/DOM effects can vary but does not clearly note the existence of opposing findings in the literature.
- Contradiction: Mark as violated if the answer asserts a single, universally applicable direction of NOM/DOM influence (e.g., always decreasing or always increasing PFAS removal) without mentioning any variability or uncertainty.
- Linked exact evidence:
  - `WF10_029_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=cd80793c8560541bc638625d5f11fe516aa30530bf100c9b686b734a833e323d].
    Supports: DOM is reported in one case to compete with PFAS and increase their transport through NF membranes, but this is explicitly described as not a consensus because other findings, such as NOM binding PFAS via cation-bridging and enhancing removal, show the opposite effect; this variability constrains overgeneralization of NOM/DOM impacts.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

For transferring NF and RO PFAS removal expectations across water types, the cited studies highlight several membrane-, feed-water-, and PFAS-mixture–related limitations rather than universal behavior.

From a membrane and operating-condition perspective, many PFAS rejection data come from bench scale RO and NF systems that "[SOURCE_TEXT_OMITTED sha256=96c15ab3943712d6f36a56317af59911de19a7c332d3552094e4acfb89dc7b99] … due to leaking, concentra - tion polarization … and operating in dead-end filtration instead of crossflow" (WF10_029_MMG002). Even pilot systems can yield uncertain performance because they "typically report on waters with relatively low PFAS concentrations, resulting in unquantifiable permeate concentrations … and imprecise rejection values" (WF10_029_MMG002). In NF, the interaction of the membrane with rejected ions and foulants can further limit transferability: in feed waters where divalent cations such as Ca2+ and Mg2+ [SOURCE_TEXT_OMITTED sha256=dd3365b9b80b3620069d3b48b7f7c504da156b14f765fbd708f55fc87cc791ce] … and the membrane surface" (WF10_029_MMG003), and dissolved organic matter (DOM) "reduces the rejection of PFAS due to fouling-enhanced concentration polarization" (WF10_029_MMG003). These configuration- and condition-specific phenomena mean that PFAS rejection observed under one set of scale and fouling conditions should not be uncritically assumed for other NF/RO systems.

Regarding the feed-water matrix, the review notes that "[SOURCE_TEXT_OMITTED sha256=7b2fe6a7f9b4c77f6be6a0b6e739c8281a3d7501575c6e70157528562227c8c7]" (WF10_029_MMG001). Surface water and groundwater differ in ways that directly change PFAS rejection: "[SOURCE_TEXT_OMITTED sha256=77bb7aee679f5b7aaf08df9ce1e1abf0c5f42478051223f53698bbf6760bb4c6]" (WF10_029_MMG001), and organic matter at higher concentration "can act at competitors with PFAS on the adsorption and electrostatic interactions with NF membranes … leading to a greater transport of PFAS through the membranes" (WF10_029_MMG001). By contrast, for groundwater "the higher ionic strength and hardness … may impact mechanisms such as size-exclusion, but potentially reduce the contribution of electrostatic repulsion" (WF10_029_MMG001), and divalent cations "often predominant in groundwater" (WF10_029_MMG003) "can also reduce the NF performance" (WF10_029_MMG003). These cations contribute to fouling patterns, as they "can also lead to increased membrane fouling by DOM due to the formation of DOM-Ca2+ complexes" and DOM "reduces the rejection of PFAS due to fouling-enhanced concentration polarization" (WF10_029_MMG003). Together with the statement that many studies instead use "deionized or tap water spiked with AFFF or single PFAS solutes" (WF10_029_MMG002), these observations emphasize that PFAS removal results from simplified or specific matrices may not represent behavior in other water types with different NOM/DOM, ionic strength, hardness, or cation composition.

For PFAS mixtures, the Masters et al. study points out that many NF/RO investigations use simplified mixtures: "Many studies have used deionized or tap water spiked with AFFF or single PFAS solutes … [SOURCE_TEXT_OMITTED sha256=36ef924ab815886ce83567ea341782adb9f3132c6d2951ba0730c05e61688d76]" (WF10_029_MMG002). It further notes that, in particular, "perfluoroalkane sulfonamides (FASAs) are often present at high concentrations at AFFF impacted sites … and several studies have revealed that they may be more toxic than the more well studied PFAAs" (WF10_029_MMG002). This means that removal performance reported for single PFAAs or AFFF-spiked model waters cannot be assumed to describe behavior for the broader sets of precursors and transformation products found at impacted sites.

Finally, the influence of natural organic matter and DOM on PFAS removal is itself uncertain, which cautions against overgeneralization of matrix effects. While one part of the review notes that DOM in surface water "can act at competitors with PFAS … leading to a greater transport of PFAS through the membranes" (WF10_029_MMG001), it immediately states that "This observation, however, is not a consensus in the literature since other findings reported the opposite" and that natural organic matter "can bind with PFAS by cation-bridging, enhancing PFAS removal by the membrane" (WF10_029_MMG001). This non-consensus underscores that, even for a single matrix component, literature findings on direction and magnitude of its effect on PFAS rejection vary, further limiting straightforward transfer of performance expectations between water types and PFAS mixtures.


### Unresolved or unsupported boundaries

- The specific roles of individual NF/RO membrane materials, surface charges, or pore-size distributions beyond what is explicitly mentioned are not described in the provided evidence and therefore are not characterized as limitations.
- Quantitative relationships or thresholds (e.g., exact NOM concentrations, ionic strengths, or PFAS concentration ranges) that determine when matrix effects become significant are not provided.
- Detailed behavior of PFAS classes other than PFAAs and perfluoroalkane sulfonamides (FASAs), such as fluorotelomer-based compounds or other precursor families, is not covered in the supplied text.
- Any universal ranking of surface water versus groundwater treatability by NF/RO for PFAS, beyond the specific mechanisms and tendencies noted, is not supported.
- Operational variables such as pressure, recovery, flux, and temperature, and how they might additionally limit extrapolation of PFAS removal across systems, are not discussed in the given excerpts.

### Complete approved source chunks

#### WF10_029_MMG001

- Role: `required_gold`
- Document: `2026 - Casella - Recent developments in membrane treatment technologies for PFAS removal from surface and groundwater.pdf`
- Chunk: `26`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=7b2fe6a7f9b4c77f6be6a0b6e739c8281a3d7501575c6e70157528562227c8c7].

```text
[SOURCE_TEXT_OMITTED sha256=5b3e52a27dbb89895e5dcdea578d8d4268e5d24b82c57f37e3d32ad036a4f5d8].
```

#### WF10_029_MMG002

- Role: `required_gold`
- Document: `2025 - Masters - Investigation of PFAS rejection by closed-circuit reverse osmosis and nanofiltration and sorption to treatment materials during groundwater.pdf`
- Chunk: `6`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=026b065a390b00c528ed061b4f404b17f3abe2d91f49270bb877bd3b7d253c4c] ].

```text
( > [SOURCE_TEXT_OMITTED sha256=506bdfb1ce6987b10dcaf11e0fd104c01b7979ba569445a88eb6776d300269a6] ].
```

#### WF10_029_MMG003

- Role: `optional_gold`
- Document: `2026 - Casella - Recent developments in membrane treatment technologies for PFAS removal from surface and groundwater.pdf`
- Chunk: `27`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=c3636cb1833a5448c8fc7ccc1321b7aae131cbc341a7e0dff8d0f943b0aac4c3].

```text
[SOURCE_TEXT_OMITTED sha256=a4227ec69fa1c4aff0ad87757ec9316dfe94740a07b7246f4a2d26777a1be431].
```

---

## WF10_032

**Question:** What is reported about short-chain PFCA adsorption and desorption after repeated adsorbent regeneration?

### Task components

- `WF10_032-T01`: Describe the experimental setup used to evaluate short-chain PFCA adsorption and desorption over repeated adsorbent regeneration cycles, including the protocol steps for adsorption and regeneration, the regenerant composition, the adsorbent and other key materials, the operating conditions, the matrix in which adsorption/desorption were tested, and the specific short-chain PFCA target compounds.
- `WF10_032-T02`: Extract what is reported about changes in short-chain PFCA adsorption and desorption behavior after the second, third, and any additional regeneration cycles, including observed performance patterns (e.g., maintained, improved, or decreased adsorption/desorption), and any explicitly stated limitations or constraints of the regeneration approach or adsorbent performance across cycles.

### Normative claim groups

#### WF10_032-G01

- Component: `WF10_032-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In Shaikh et al., a combination of ammonium solution with methanol (50% methanol with 1% NH4OH) was selected as the optimized regenerant and used for subsequent adsorption–desorption cycles to regenerate a synthesized PFCA adsorbent.
- Full: Count as fully supported if the answer notes that Shaikh et al. used a regenerant composed of ammonium solution with methanol, specifically 50% methanol with 1% NH4OH, and that this optimized regenerant was then applied in subsequent adsorption–desorption cycles to regenerate their synthesized adsorbent.
- Partial: Count as partially supported if the answer mentions either that an alcohol–ammonium regenerant (methanol with ammonium solution) was optimized and used in multiple adsorption–desorption cycles, or if it specifies the 50% methanol with 1% NH4OH composition but does not clearly state that this was used for successive cycles.
- Contradiction: Mark as contradicted if the answer claims a different regenerant composition (e.g., different solvent or different ammonium concentration) for Shaikh et al.'s multi-cycle tests, or states that regeneration was done without using the 50% methanol with 1% NH4OH combination.
- Linked exact evidence:
  - `WF10_032_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=de8c4d16fbd3c5f297e51db7b7637d8057582a03a00a07f877f8a9b15ec1f0e0].
    Supports: Describes the optimized regenerant composition (50% methanol with 1% NH 4OH) and states that this regenerant was employed for subsequent adsorption–desorption cycles.

#### WF10_032-G02

- Component: `WF10_032-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In Shaikh et al., the adsorption efficiency of the short-chain PFCAs PFPrA and PFBA decreased in the second cycle relative to the first but then remained almost consistent in the third cycle when using the regenerated adsorbent.
- Full: Count as fully supported if the answer states that PFPrA and PFBA adsorption efficiencies dropped between the first and second cycles but then were approximately stable or consistent in the third cycle.
- Partial: Count as partially supported if the answer only notes a reduction in PFPrA and PFBA adsorption in the second cycle, or only notes that adsorption for these short-chain PFCAs was similar between the second and third cycles, without describing both aspects.
- Contradiction: Mark as contradicted if the answer claims that PFPrA and PFBA adsorption efficiencies did not decrease in the second cycle, or that they continued to decline in the third cycle rather than remaining almost consistent.
- Linked exact evidence:
  - `WF10_032_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=66cb25ddbf03ccaf3ccf6cfeaa3a757a3818893dba0e8f8c315f517d0451435b].
    Supports: Directly reports that PFPrA and PFBA adsorption efficiencies decreased in the second cycle relative to the first and that adsorption remained almost consistent in the third cycle.

#### WF10_032-G03

- Component: `WF10_032-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In Shaikh et al., desorption efficiencies for PFPrA and PFBA increased in the second regeneration cycle relative to the first when using the optimized regenerant.
- Full: Count as fully supported if the answer explains that desorption of PFPrA and PFBA increased in the second cycle compared to the first when the optimized regenerant was used.
- Partial: Count as partially supported if the answer notes that desorption improved in later cycles without specifying that the reported increase occurred specifically in the second cycle for PFPrA and PFBA.
- Contradiction: Mark as contradicted if the answer states that PFPrA and PFBA desorption decreased or stayed the same in the second cycle relative to the first, or suggests that regeneration efficiency did not improve in that cycle.
- Linked exact evidence:
  - `WF10_032_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=0be8c25ce955920a3eac878e4df2e2fc58188224ccb3145cd89efff0e0743534].
    Supports: Shows that desorption efficiencies for PFPrA and PFBA were higher in the second cycle than in the first.
  - `WF10_032_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=dc657fc43c3900f55f736b3e0c5936cc8d6f2de757281140b32aaa44dd593894].
    Supports: Explicitly states that there was an increase in regeneration efficiency in the second cycle compared to the first, corresponding to improved desorption.

#### WF10_032-G04

- Component: `WF10_032-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In Shaikh et al., adsorption and desorption efficiencies for PFOA and PFPeA remained consistent over three adsorption–desorption cycles, indicating stable performance across regenerations for these PFCAs under the reported conditions.
- Full: Count as fully supported if the answer notes that PFOA and PFPeA adsorption remained consistent over three cycles and that desorption for these compounds was also consistent up to three successive cycles.
- Partial: Count as partially supported if the answer mentions only adsorption or only desorption consistency for PFOA and PFPeA over three cycles, or if it states multi-cycle stability for these compounds without specifying three cycles.
- Contradiction: Mark as contradicted if the answer claims that PFOA or PFPeA adsorption or desorption significantly declined or increased across the three cycles in Shaikh et al.'s study.
- Linked exact evidence:
  - `WF10_032_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=c3085b64b32f7b6c5b93ea31a2b93f1852b9984402da10fb11249d201be728c6].
    Supports: States that PFOA and PFPeA adsorption remained consistent across three cycles and gives approximate efficiencies.
  - `WF10_032_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > Similarly, the desorption was also consistent up to three successive cycles.
    Supports: Shows that desorption efficiencies were consistent over three successive cycles, supporting the desorption-stability part of the claim.

#### WF10_032-G05

- Component: `WF10_032-T02`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: Across multiple studies summarized by Andrunik and Smol, solvent-based and alkaline regenerants such as methanol, ethanol, methanol–NaCl, methanol–NaOH, NaOH, and ammonia typically achieve high multi-cycle desorption and recovery of short-chain PFASs, with desorption efficiencies often exceeding 90% and retention exceeding 85% after 4–5 cycles on certain adsorbents.
- Full: Count as fully supported if the answer conveys that, in the broader literature summarized by Andrunik and Smol, methanol- or ethanol-based solvent systems (with or without salts or bases) and alkaline regenerants like NaOH or ammonia provide high desorption or recovery of short-chain PFASs across multiple regeneration cycles, with mentions of >90% desorption or >85% retention after 4–5 cycles on suitable adsorbents.
- Partial: Count as partially supported if the answer notes that solvent or alkaline regenerants achieve generally high multi-cycle desorption of short-chain PFASs but omits either the involvement of salts/bases, the multi-cycle aspect, or the rough magnitude (>90% or >85%).
- Contradiction: Mark as contradicted if the answer claims that these regenerants generally show poor multi-cycle desorption for short-chain PFASs, or that desorption efficiencies for short-chain PFASs are typically below those of long-chain PFASs under the same solvent/alkaline regeneration conditions in this summarized literature.
- Linked exact evidence:
  - `WF10_032_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=609361f4faa891c2e72e6d44e7bde3210540894e1b932502bd3a42c3b9cb564a]].
    Supports: Reports that methanol, ethanol, and methanol–NaCl or methanol–NaOH mixtures achieve >90% desorption of short-chain PFASs over multiple cycles.
  - `WF10_032_MMG004` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=eb7749721870c3806eb703d737cffd0fff63d76524219f5436d5b09527c54aee]].
    Supports: Shows that alkaline regenerants NaOH and ammonia give high recovery of short-chain PFASs with >85% retention after 4–5 cycles on certain adsorbents.

#### WF10_032-X01

- Component: `WF10_032-T02`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: In Shaikh et al., incomplete desorption of short-chain PFCAs left some adsorption sites preoccupied and reduced adsorption capacity in the second cycle, and in the broader literature summarized by Andrunik and Smol, long-chain PFASs such as PFOA and PFOS generally exhibit lower desorption efficiencies and persistent residuals under the same regenerant conditions that are highly effective for short-chain species.
- Full: Use as a constraint if the answer acknowledges that, in Shaikh et al., incomplete desorption preoccupied adsorption sites and reduced adsorption capacity in the second cycle, and/or notes that in the broader literature long-chain PFASs like PFOA and PFOS do not regenerate as completely as short-chain species under similar solvent or alkaline conditions. Answers should not generalize high regeneration performance to all PFASs without these caveats.
- Partial: Use as partially satisfied if the answer mentions either (but not both) the incomplete desorption effect on second-cycle adsorption in Shaikh et al. or the poorer regeneration of long-chain PFASs in the reviewed studies, as a limitation.
- Contradiction: Flag as contradicting this constraint if the answer claims that desorption in Shaikh et al. was complete across cycles with no impact on adsorption capacity, or that long-chain PFASs such as PFOA and PFOS regenerated as well or better than short-chain PFASs under solvent or alkaline conditions described by Andrunik and Smol.
- Linked exact evidence:
  - `WF10_032_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=609361f4faa891c2e72e6d44e7bde3210540894e1b932502bd3a42c3b9cb564a]].
    Supports: Indicates that PFOA and PFOS desorption efficiencies are lower (60–80%) than those of short-chain PFASs under the same regenerant conditions.
  - `WF10_032_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=07327d77c90bac287d8fd72405d123e020df29113f7241ff19966ac57485d6fd].
    Supports: States that incomplete desorption preoccupied adsorption sites and reduced adsorption capacity in the second cycle.
  - `WF10_032_MMG004` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=eb7749721870c3806eb703d737cffd0fff63d76524219f5436d5b09527c54aee]].
    Supports: Notes persistent residuals of PFOA/PFOS even after extended contact times, reinforcing that long-chain PFASs regenerate less completely than short-chain PFASs.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

In the study by Shaikh et al., a synthesized PFCA adsorbent with a mesoporous structure and some micropores was subjected to repeated adsorption–desorption cycles. For regeneration, they screened different regenerants and identified a combination of ammonium solution with methanol as optimal: “50% methanol with 1% NH4OH” showed the highest PFCA desorption among the tested regenerants, and “the optimized spec of the regenerant was employed for subsequent cycles of adsorption–desorption.” No further protocol steps, operating conditions, or matrix details are provided in the supplied text beyond the indication that these were repeated adsorption–desorption cycles on the same synthesized adsorbent.

Regarding cycle-to-cycle performance for short-chain PFCAs, Shaikh et al. report that “in the second cycle, the adsorption efficiency of PFPrA and PFBA decreased … but remained almost consistent for the third cycle.” Thus, the regenerated adsorbent showed a drop in PFPrA and PFBA adsorption efficiency in the second cycle relative to the first, followed by approximately stable adsorption performance in the third cycle. At the same time, “desorption increased in the second cycle … for PFPrA and … for PFBA,” and the authors note “an increase in regeneration efficiency as compared to the first cycle,” indicating that the optimized regenerant improved desorption performance in the second cycle for these short-chain PFCAs.

For other PFCAs in the same experiment, multi-cycle performance appeared more stable. The authors state that “PFOA and PFPeA adsorption remained consistent over the three cycles” and that “the desorption was also consistent up to three successive cycles.” Under the reported conditions, adsorption and desorption of PFOA and PFPeA therefore did not show the second-cycle decrease in adsorption seen for PFPrA and PFBA.

The text further notes a limitation in Shaikh et al.’s system: the pore size distribution includes “a fraction of pores smaller than 1 nm,” and these micropores “likely facilitated the diffusion and entrapment of short chain PFCAs,” so “a fraction of these adsorbed molecules may remain trapped … [SOURCE_TEXT_OMITTED sha256=4bba7b538c642be5a5274a45ea00e13ec7c353ff0a975078ca053c0afb0ee08f].” Thus, while desorption of PFPrA and PFBA improved in the second cycle, incomplete desorption overall contributed to reduced second-cycle adsorption capacity for some short-chain PFCAs.

Complementing this single-study evidence, the review by Andrunik and Smol summarizes broader multi-cycle regeneration behavior for short-chain PFASs. They report that “[SOURCE_TEXT_OMITTED sha256=5e0f9451ace50539620b0094dc6fbe474edac08d42b84052855386197893674c],” indicating that solvent-based regenerants with or without salts can repeatedly desorb short-chain PFASs at high efficiency on polymeric and carbonaceous adsorbents. They also state that “alkaline regenerants such as NaOH and ammonia [SOURCE_TEXT_OMITTED sha256=e8b60fa290af2fe2b6f0b79425f77f344cbaf63f8111254767363e3c308f69de]).” In contrast, under the same conditions “efficiencies for PFOA and PFOS dropped to 60–80%” and there were “persistent residuals of PFOA/PFOS even after extended contact times,” highlighting that the high multi-cycle desorption and retention observed for short-chain PFASs does not necessarily extend to long-chain PFASs.

Within the limits of the provided text, the key multi-cycle pattern for short-chain PFCAs is therefore that, when using an optimized methanol–ammonium regenerant, PFPrA and PFBA show improved desorption but reduced adsorption in the second cycle followed by stable adsorption in the third, while PFOA and PFPeA maintain relatively consistent adsorption and desorption over three cycles. The broader literature indicates that methanol/ethanol-based and alkaline regenerants can maintain high desorption and recovery of short-chain PFASs over multiple regeneration cycles, though detailed experimental conditions and matrices are not fully specified in the excerpts provided here.

### Unresolved or unsupported boundaries

- Specific adsorption–desorption protocol steps (e.g., contact times, solid–liquid ratios, sequence and duration of adsorption vs regeneration stages) for Shaikh et al. are not described in the provided text.
- Detailed operating conditions such as temperature, pH, flow regime (batch vs column), and agitation for the adsorption and regeneration cycles in Shaikh et al. are not available in the supplied excerpts.
- The precise water matrix for Shaikh et al.’s adsorption/desorption experiments (e.g., specific surface water source, synthetic vs real water, ionic strength, co-contaminants) cannot be confirmed from the provided chunks alone.
- The exact identity or formulation name of Shaikh et al.’s quaternary ammonium adsorbent beyond being a synthesized, mesoporous material with some micropores is not given in the excerpts.
- The number of regeneration cycles beyond three, and any performance patterns after the third cycle in Shaikh et al.’s study, are not reported in the provided text.
- For the multi-study review summarized by Andrunik and Smol, study-specific details such as individual adsorbent types, matrices, and exact regeneration protocols for each cited system are not available in the excerpt and cannot be reconstructed.
- The question’s request for explicit second- and third-cycle performance of all individual short-chain PFCA species beyond PFPrA, PFBA, PFPeA, and PFOA cannot be fully satisfied because only these compounds are discussed in the supplied Shaikh et al. text.

### Complete approved source chunks

#### WF10_032_MMG001

- Role: `required_gold`
- Document: `2025 - Shaikh - Efficient removal of short- and long-chain perfluoroalkyl carboxylate acids from surface water matrices using a quaternary ammonium adsorbent.pdf`
- Chunk: `32`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=66cb25ddbf03ccaf3ccf6cfeaa3a757a3818893dba0e8f8c315f517d0451435b].

```text
[SOURCE_TEXT_OMITTED sha256=3b2b8e809eaa7334939823bc11710f2372f8ff9f95cb310e5d571305cd591533]
```

#### WF10_032_MMG002

- Role: `required_gold`
- Document: `2025 - Shaikh - Efficient removal of short- and long-chain perfluoroalkyl carboxylate acids from surface water matrices using a quaternary ammonium adsorbent.pdf`
- Chunk: `33`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=0be8c25ce955920a3eac878e4df2e2fc58188224ccb3145cd89efff0e0743534].

```text
[SOURCE_TEXT_OMITTED sha256=35d9db0b2864c7009d36f7c43584419cce0ebc75819cd60e204a4ef504b82063]
```

#### WF10_032_MMG003

- Role: `optional_gold`
- Document: `2025 - Shaikh - Efficient removal of short- and long-chain perfluoroalkyl carboxylate acids from surface water matrices using a quaternary ammonium adsorbent.pdf`
- Chunk: `33`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=c3085b64b32f7b6c5b93ea31a2b93f1852b9984402da10fb11249d201be728c6].

```text
[SOURCE_TEXT_OMITTED sha256=35d9db0b2864c7009d36f7c43584419cce0ebc75819cd60e204a4ef504b82063]
```

#### WF10_032_MMG004

- Role: `optional_gold`
- Document: `2025 - Andrunik - Life After Adsorption - Regeneration, Management, and Sustainability of PFAS Adsorbents in Water Treatment.pdf`
- Chunk: `43`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=609361f4faa891c2e72e6d44e7bde3210540894e1b932502bd3a42c3b9cb564a]].

```text
[SOURCE_TEXT_OMITTED sha256=236283c5d67a25bbb02fb7ae25968171a41a60c4f45c8eda22d75e88ff5f179b]].
```

---

## WF10_034

**Question:** For PFAS-containing plating wastewater, when might electrochemical treatment, carbon treatment, or ion exchange be preferable?

### Task components

- `WF10_034-T01`: Identify studies on PFAS-containing plating wastewater that evaluate electrochemical treatment, carbon treatment, or ion exchange under matched conditions (same or clearly comparable PFAS compounds, wastewater matrix, endpoints, and operating conditions), and select only those subsets of data that are directly comparable across technologies.
- `WF10_034-T02`: From the matched-condition studies, extract how electrochemical treatment performance and capacity for PFAS in plating wastewater change with influent PFAS concentration, including any reported limits or trends in removal or loading, without adding study-specific details or numeric values.
- `WF10_034-T03`: From the same or otherwise matched-condition studies, extract how carbon treatment performance and capacity for PFAS in plating wastewater depend on influent PFAS concentration, including any reported limits or trends in removal or loading, without adding study-specific details or numeric values.
- `WF10_034-T04`: From the same or otherwise matched-condition studies, extract how ion exchange performance and capacity for PFAS in plating wastewater depend on influent PFAS concentration, and synthesize a comparison across electrochemical treatment, carbon treatment, and ion exchange that only contrasts them where compounds, matrices, endpoints, and conditions are matched, avoiding any universal ranking when evidence is not directly comparable.

### Normative claim groups

#### WF10_034-G01

- Component: `WF10_034-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: A single electroplating wastewater study evaluated electrochemical oxidation (E-destruct), ion exchange, and activated carbon on the same PFAS-containing electroplating waste streams, providing directly comparable data under matched conditions.
- Full: Award full credit if the answer identifies that the available evidence comes from a study on electroplating industry PFAS-containing waste streams in which conventional alternative PFAS removal systems (ion exchange resin and activated carbon) were tested on the same waste streams and directly compared with each other and with an electrochemical oxidation (E-destruct) process, thereby providing matched-condition data across the three technologies.
- Partial: Award partial credit if the answer notes that ion exchange, activated carbon, and electrochemical treatment were compared for PFAS removal in plating wastewater, but does not clearly indicate that this comparison was performed on the same electroplating waste streams or under matched conditions.
- Contradiction: Mark as contradicted if the answer claims there is no study directly comparing ion exchange, activated carbon, and electrochemical treatment on PFAS-containing plating wastewater, or if it explicitly states that the available studies use completely different matrices that cannot be compared.
- Linked exact evidence:
  - `WF10_034_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=d7053b200517b77d4e81585ac84fc9f85bd45c9360b3a6f3aced094634747587].
    Supports: Shows that conventional PFAS removal systems (including ion exchange and activated carbon) were tested on the same waste streams and compared with each other and with electrochemical oxidation.
  - `WF10_034_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=27613cfcd9b7f380406e751991d0581fd6a2bf2663ead82fd4f389e343f3304e].
    Supports: Reiterates that all three technologies were compared on the same electroplating waste streams, providing matched conditions.

#### WF10_034-G02

- Component: `WF10_034-T04`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In the electroplating wastewater study, ion exchange resin treatment to complex and remove PFAS was substantially more efficient than conventional activated carbon absorption under the same conditions.
- Full: Award full credit if the answer states that, in the electroplating PFAS-containing wastewater study, ion exchange resin treatment was found to be significantly more efficient than conventional activated carbon absorption for PFAS removal under the same waste-stream conditions.
- Partial: Award partial credit if the answer indicates that ion exchange performed better than activated carbon in the plating wastewater study but does not clearly identify that this was an efficiency comparison or that the conditions were matched.
- Contradiction: Mark as contradicted if the answer claims that activated carbon was more efficient than ion exchange under the matched electroplating wastewater conditions, or that there was no difference in performance between the two.
- Linked exact evidence:
  - `WF10_034_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=d7053b200517b77d4e81585ac84fc9f85bd45c9360b3a6f3aced094634747587].
    Supports: Directly supports that, on the same wastewater, ion exchange was reported to be much more efficient than activated carbon for PFAS removal.

#### WF10_034-G03

- Component: `WF10_034-T04`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In the electroplating wastewater study, the electrochemical oxidation (E-destruct) process was reported to have higher capacity, longer service life, and lower operating costs for elimination of PFAS from the electroplating waste streams than either ion exchange or activated carbon.
- Full: Award full credit if the answer notes that, for the same PFAS-containing electroplating waste streams, the electrochemical E-destruct process was reported to have higher capacity, longer service life, and lower operating costs than both ion exchange and activated carbon for elimination of PFAS.
- Partial: Award partial credit if the answer mentions that E-destruct had advantages over ion exchange and carbon (e.g., higher capacity) but omits either service life or operating-cost information, or does not clearly state that the comparison was made on the same electroplating waste streams.
- Contradiction: Mark as contradicted if the answer states that E-destruct had lower capacity or shorter service life than ion exchange or carbon under these conditions, or that its operating costs were higher than those of ion exchange or carbon.
- Linked exact evidence:
  - `WF10_034_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=27613cfcd9b7f380406e751991d0581fd6a2bf2663ead82fd4f389e343f3304e].
    Supports: Directly supports that E-destruct has higher capacity, longer service life, and lower operating costs than ion exchange or carbon for PFAS elimination from the electroplating waste streams.

#### WF10_034-G04

- Component: `WF10_034-T02`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: In the plating-industry study, the electrochemical decomposition process achieved high PFAS treatment efficiency within a specified PFAS concentration range in the PFAS-containing wastewater, indicating that its performance was characterized within that influent concentration band.
- Full: Award full credit if the answer explains that the electrochemical decomposition process in the plating-industry wastewater study achieved very high PFAS treatment efficiency within a specified influent PFAS concentration range, indicating effective performance over that band of concentrations without needing to restate numeric values.
- Partial: Award partial credit if the answer mentions that the electrochemical process was effective or showed high removal in the plating wastewater study, but does not clearly tie this to its operation within a defined influent concentration range.
- Contradiction: Mark as contradicted if the answer claims that the electrochemical process was only tested at a single PFAS concentration or that its efficiency did not depend on or was not characterized over any influent concentration range in the study.
- Linked exact evidence:
  - `WF10_034_MMG003` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=1e6e9960631e547805feb6aaa4ac59bc4957c7c0e9b0a1e240ffa124f773c55a]).
    Supports: Shows that, under production conditions, the electrochemical process achieved very high PFAS treatment efficiency over a defined influent PFAS concentration range in the plating-industry wastewater.

#### WF10_034-X01

- Component: `WF10_034-T02`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: The electrochemical PFAS treatment process in the plating-industry wastewater study became ineffective when the PFAS-containing wastewater was mixed with other wastewater streams or when pH values exceeded 5, and it was less efficient for short-chain PFAS than for C6–C8 PFAS.
- Full: Use this as a constraint to ensure answers note that the plating-wastewater electrochemical process lost effectiveness when the PFAS-containing wastewater was mixed with other streams, particularly nickel plating drag out, or when pH values were greater than 5, and that it was less efficient for a short-chain PFAS than for C6–C8 PFAS. This should prevent overgeneralizing electrochemical performance to conditions outside those tested.
- Partial: Consider the constraint partially addressed if the answer mentions at least one of the key limitations (e.g., loss of effectiveness when mixed with other waste streams or at higher pH, or reduced efficiency for short-chain PFAS) but not all of them.
- Contradiction: Flag a contradiction if the answer claims the electrochemical process remained effective regardless of mixing with other wastewater streams or pH conditions, or that its efficiency was the same for short-chain PFAS as for C6–C8 PFAS in this study.
- Linked exact evidence:
  - `WF10_034_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=f61cda0b0338e33168be1911b512c48aec63274597ee669919eaa3975f6fad87].
    Supports: Shows that the electrochemical treatment process became ineffective when the PFAS-containing wastewater was mixed with other wastewater streams, especially nickel plating drag out, or when pH exceeded 5.
  - `WF10_034_MMG003` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > For the short chain PFAS, (per ﬂuorobutylsulfonate) the process was less ef ﬁcient than C6 –C8 PFAS.
    Supports: Indicates that the electrochemical process was less efficient for a short-chain PFAS compared to C6–C8 PFAS, constraining generalizations about its performance across PFAS types.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

The available evidence comes from a single plating‑industry study in which PFAS‑containing electroplating waste streams were treated using ion exchange resin, conventional activated carbon absorption (C‑treat), and an electrochemical oxidation process (E‑destruct). In this work, all three technologies were tested on the same electroplating waste streams, so their reported performances are directly comparable for that matrix and set of PFAS.

Under these matched electroplating‑wastewater conditions, ion exchange resin treatment to complex and remove PFAS was reported to be markedly more efficient than conventional activated carbon absorption. This indicates that, for these PFAS‑containing electroplating waste streams, ion exchange would be preferable to activated carbon when the goal is higher removal efficiency under otherwise similar operating conditions. The study, however, does not describe how the efficiency or capacity of ion exchange or activated carbon change as influent PFAS concentrations vary, so concentration‑dependent performance trends for these two technologies cannot be extracted from the provided text.

The same study found that the E‑destruct electrochemical process, applied to the same PFAS‑containing electroplating waste streams, had higher capacity, longer service life, and lower operating costs for PFAS elimination than either ion exchange or activated carbon. In addition, the electrochemical decomposition method was successfully demonstrated under production conditions to achieve very high PFAS treatment efficiency over a defined influent PFAS concentration range in the plating wastewater. This supports using electrochemical treatment when high PFAS loadings or extended service life are important, provided that the wastewater composition and operating conditions match those in the study.

The electrochemical process showed important limitations that constrain when it is preferable. It became ineffective when the PFAS‑containing wastewater was mixed with other wastewater streams, particularly nickel plating drag‑out, or when the pH exceeded a moderately acidic value. It was also less efficient for a short‑chain PFAS than for C6–C8 PFAS. Under such off‑spec conditions, the advantages of electrochemical treatment documented in this study may not apply.

Taken together, for the specific PFAS‑containing electroplating waste streams examined, ion exchange was more efficient than activated carbon, and the electrochemical E‑destruct process offered higher capacity, longer service life, and lower operating costs than both ion exchange and carbon while maintaining high efficiency over the studied influent concentration range, as long as the wastewater remained as an unmixed plating stream with appropriately low pH. The study does not provide detailed concentration‑dependent performance or capacity relationships for ion exchange or activated carbon, nor does it support any universal ranking of these technologies beyond these particular electroplating wastewater conditions.

### Unresolved or unsupported boundaries

- Any detailed description of how ion exchange resin performance or capacity in plating wastewater varies with influent PFAS concentration (e.g., breakthrough behavior, loading limits, or plateau effects) is not supported by the provided evidence.
- Any detailed description of how activated carbon treatment performance or capacity in plating wastewater varies with influent PFAS concentration is not supported by the provided evidence.
- Any quantitative comparison of removal efficiency, capacity, or cost among electrochemical treatment, ion exchange, and activated carbon beyond the qualitative relationships stated in the evidence is not supported.
- Any universal ranking of electrochemical treatment, carbon treatment, and ion exchange for PFAS removal in plating or other wastewaters beyond the specific electroplating waste streams and conditions studied is not supported.
- Any specific operational parameters (electrode materials beyond what is named, current density, contact times, resin or carbon types, or reactor configurations) are not supported by the provided evidence and therefore are not described.

### Complete approved source chunks

#### WF10_034_MMG001

- Role: `required_gold`
- Document: `2006 - Fath - Electrochemical decomposition of fluorinated wetting agents in plating industry waste water.pdf`
- Chunk: `1`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=d7053b200517b77d4e81585ac84fc9f85bd45c9360b3a6f3aced094634747587].

```text
[SOURCE_TEXT_OMITTED sha256=44fd8efcd864f502f3e867872896281e7e763afbfd0f5b2cef70267f188c9613]
```

#### WF10_034_MMG002

- Role: `required_gold`
- Document: `2006 - Fath - Electrochemical decomposition of fluorinated wetting agents in plating industry waste water.pdf`
- Chunk: `1`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=27613cfcd9b7f380406e751991d0581fd6a2bf2663ead82fd4f389e343f3304e].

```text
[SOURCE_TEXT_OMITTED sha256=44fd8efcd864f502f3e867872896281e7e763afbfd0f5b2cef70267f188c9613]
```

#### WF10_034_MMG003

- Role: `negative_gold`
- Document: `2006 - Fath - Electrochemical decomposition of fluorinated wetting agents in plating industry waste water.pdf`
- Chunk: `0`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=f61cda0b0338e33168be1911b512c48aec63274597ee669919eaa3975f6fad87].

```text
[SOURCE_TEXT_OMITTED sha256=866b8f346884f8422edbb2a9f651231a6594cfb3fa978799246b1021dfb76a5d]
```

---

## WF10_035

**Question:** In mixed PFAS groundwater, does one compound appear to displace another on anion-exchange resin?

### Task components

- `WF10_035-T01`: Extract what the described study reports about how PFHxS and PFOA adsorption behavior changes in mixed PFAS (co-adsorption) groundwater on anion-exchange resin, including any observed differences in removal, breakthrough, or retention for each compound, without describing this as one compound displacing or replacing another.
- `WF10_035-T02`: Calibrate the interpretation by explicitly distinguishing: (a) what is directly supported by the reported findings about PFHxS and PFOA behavior under the specific mixed-solute conditions studied, from (b) any mechanisms (e.g., true displacement on the resin), causal explanations, or broader generalizations to PFAS treatment that are not established by the available evidence, and note any limits on generalization beyond the reported conditions.

### Normative claim groups

#### WF10_035-G01

- Component: `WF10_035-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In simulated AFFF-impacted groundwater containing six PFAS on the anion-exchange resin IRA910, the competitive adsorption (adsorbed amount) follows the order PFOS > PFHxS > PFOA > PFBS > PFHxA > PFBA, indicating that under these mixed-solute conditions PFHxS is retained more strongly than PFOA but both are effectively removed.
- Full: Award full credit if the answer states that, in the simulated AFFF-impacted groundwater with multiple PFAS on anion-exchange resin (IRA910), the competitive adsorption or adsorbed amounts follow the order PFOS > PFHxS > PFOA > PFBS > PFHxA > PFBA, and explains that PFHxS is retained more strongly (or has a higher adsorbed amount) than PFOA under these mixed conditions, without framing this as active displacement or replacement.
- Partial: Award partial credit if the answer (a) mentions competitive adsorption in mixed PFAS groundwater and identifies PFOS, PFHxS, and PFOA in the correct qualitative order (PFOS highest and PFOA lower than PFHxS) OR (b) notes that PFHxS adsorption/removal is higher/stronger than PFOA under the mixed conditions, but omits part of the full ordering or the specific mixed-groundwater context.
- Contradiction: Mark as contradictory if the answer reverses the order of PFHxS and PFOA (e.g., claims PFOA has higher adsorption than PFHxS under the mixed conditions), asserts that PFOA is preferentially retained over PFHxS in this study, or attributes this ordering to single-solute rather than competitive mixed-PFAS conditions.
- Linked exact evidence:
  - `WF10_035_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=497b1f708340dc6f8715424397c4d1ca0dd98d3134587384ecc9d3ffc3da8b72].
    Supports: States that in simulated AFFF-impacted groundwater with six PFAS on IRA910, the adsorbed amounts follow the order PFOS > PFHxS > PFOA > PFBS > PFHxA > PFBA, implying PFHxS has a higher adsorbed amount than PFOA.
  - `WF10_035_MMG002`
    >  Competitive sorption follows the order of PFOS > PFHxS > PFOA > PFBS > PFHxA > PFBA.
    Supports: Confirms that the competitive sorption order for the PFAS mixture on IRA910 is PFOS > PFHxS > PFOA > PFBS > PFHxA > PFBA.

#### WF10_035-G02

- Component: `WF10_035-T01`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: In the same mixed-PFAS system on IRA910, nonionic organic co-solutes (TEC and MB) hardly affected PFHxS removal, whereas ionic organic co-solutes (SDS and HA) significantly decreased the adsorbed amount of PFHxS, and common inorganic anions slightly decreased PFHxS removal with similar influence, with no parallel detail reported for PFOA.
- Full: Award full credit for this supplementary claim if the answer notes that in the mixed-PFAS groundwater system on IRA910, nonionic organic compounds (TEC and MB) hardly interfered with PFHxS removal, while ionic organic compounds (SDS and HA) significantly decreased the PFHxS adsorbed amount, and that inorganic anions (sulfate, bicarbonate, chloride, phosphate) slightly decreased PFHxS removal with similar influence, and also notes that comparable co-solute effects are not reported for PFOA in the provided evidence.
- Partial: Award partial credit if the answer mentions at least one of these observed co-solute effects on PFHxS (e.g., that nonionic organics had little effect, or ionic organics decreased PFHxS adsorption) but omits the others or does not explicitly differentiate from PFOA.
- Contradiction: Mark as contradictory if the answer claims that nonionic organics substantially reduced PFHxS removal, or that ionic organics had no effect, or that inorganic anions greatly increased PFHxS removal, contrary to the reported slight decreases and described patterns.
- Linked exact evidence:
  - `WF10_035_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=3843d634f95cfdf566b41bb9783fe22cc5d8df9ddf1956698a73fcbe0f728a0d].
    Supports: Reports that nonionic organics (TEC, MB) hardly interfered with PFHxS removal, whereas ionic organics (SDS, HA) significantly decreased the adsorbed amount of PFHxS.
  - `WF10_035_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=8e07defb4e83a6fb243906bdf1347d2a214ce6a9545c18aaa62152094ddfc4e7].
    Supports: States that sulfate, bicarbonate, chloride, and phosphate slightly decreased the removal efficiency of PFHxS with similar influence.

#### WF10_035-G03

- Component: `WF10_035-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: The reported findings for IRA910 in simulated AFFF-impacted groundwater support only a condition-specific conclusion that PFHxS shows higher competitive adsorption than PFOA in a particular six-PFAS mixture; they do not provide detailed breakthrough or retention curves for PFHxS versus PFOA, nor do they, by themselves, establish a general mechanism of compound displacement or broad treatment rules for all PFAS or all anion-exchange resins.
- Full: Award full credit if the answer explicitly distinguishes that: (a) the IRA910 study directly shows only that in a six-PFAS simulated AFFF groundwater mixture, PFHxS has a higher adsorbed amount than PFOA, with competitive sorption order PFOS > PFHxS > PFOA > PFBS > PFHxA > PFBA, and reports co-solute effects on PFHxS; and (b) the study does not provide detailed PFHxS vs PFOA breakthrough curves, does not prove a general resin displacement mechanism between these two compounds, and cannot be generalized to all PFAS, all groundwater matrices, or all anion-exchange resins. The answer may mention that other work observes displacement behavior for PFAS with lower resin affinity, but must emphasize that specific mechanisms and generalizations remain unresolved beyond the studied conditions.
- Partial: Award partial credit if the answer acknowledges at least that the observed ordering PFOS > PFHxS > PFOA is specific to the studied mixed-PFAS system and does not by itself justify broad generalization or mechanistic claims, even if it does not fully articulate all the limitations or does not mention the lack of detailed breakthrough data.
- Contradiction: Mark as contradictory if the answer implies or states that the evidence proves a universal displacement mechanism between PFHxS and PFOA on all anion-exchange resins, or that the reported order PFOS > PFHxS > PFOA universally governs PFAS behavior in all groundwater, or if it asserts detailed PFHxS vs PFOA breakthrough behavior that is not reported.
- Linked exact evidence:
  - `WF10_035_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=497b1f708340dc6f8715424397c4d1ca0dd98d3134587384ecc9d3ffc3da8b72].
    Supports: Shows that in the specific six-PFAS simulated AFFF-impacted groundwater system on IRA910, PFHxS has a higher adsorbed amount than PFOA, with competitive adsorption order PFOS > PFHxS > PFOA > PFBS > PFHxA > PFBA.
  - `WF10_035_MMG002`
    >  Competitive sorption follows the order of PFOS > PFHxS > PFOA > PFBS > PFHxA > PFBA.
    Supports: Reinforces that the reported competitive sorption order is specific to the studied system and does not itself imply a general rule for all PFAS or resins.
  - `WF10_035_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=3843d634f95cfdf566b41bb9783fe22cc5d8df9ddf1956698a73fcbe0f728a0d].
    Supports: Illustrates that the study reports co-solute effects specifically for PFHxS under the conditions tested, underscoring the condition-specific nature of the findings.
  - `WF10_035_MMG004`
    > displacement in breakthrough behavior of PFAS with lower resin affinity.
    Supports: Indicates that another study observes displacement in breakthrough for PFAS with lower resin affinity, but without specifying PFHxS or PFOA or providing generalizable mechanisms.

#### WF10_035-X01

- Component: `WF10_035-T02`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: The wording that PFHxS "replaced" PFAS with shorter C–F chains on IRA910 in bisolute systems, and that short-chain PFAS are exchanged by longer-chain PFAS, should not be overinterpreted as general proof of a universal displacement mechanism for PFHxS versus PFOA in mixed groundwater or on all anion-exchange resins.
- Full: Use this constraint to prevent answers from generalizing the study's description of PFHxS replacing shorter-chain PFAS in bisolute systems, or the statement that short-chain PFAS are exchanged by long-chain PFAS, into a universal claim that PFHxS displaces PFOA or all shorter-chain PFAS in all mixed groundwater or on all anion-exchange resins. Answers should not frame the observed competitive adsorption order as definitive evidence of a general displacement mechanism between specific compounds.
- Partial: If an answer hints at displacement but clearly restricts it to the studied bisolute systems or long-chain vs short-chain patterns without overstating generality, treat this as acceptable but still constrained.
- Contradiction: Flag as violating this constraint if the answer asserts that PFHxS universally displaces PFOA or other PFAS on any anion-exchange resin or in all groundwater, or treats the reported "replacement" language as conclusive mechanistic proof beyond the study's specific systems.
- Linked exact evidence:
  - `WF10_035_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=2e6cb024a7370176f09bf8505a7b56e47a431615a2f7f23bd363cb78c2ed6744].
    Supports: Shows that the authors describe PFHxS as replacing PFAS with shorter C–F chains in a bisolute system on IRA910, but this is specific to certain PFAS and conditions.
  - `WF10_035_MMG002`
    >  PFASs with short C-F chain are ex- changed by those with long C-F chain.
    Supports: Summarizes the general observation that short-chain PFAS are exchanged by longer-chain PFAS, which should not be overgeneralized into a universal displacement mechanism.

#### WF10_035-X02

- Component: `WF10_035-T02`
- Importance: `supplementary`
- Scoring role: `constraint_only`
- Proposition: The brief mention of "displacement in breakthrough behavior of PFAS with lower resin affinity" in a separate pilot study does not specify PFHxS or PFOA and should not be treated as direct evidence for how PFHxS and PFOA displace each other or behave on the specific resin and conditions of the IRA910 study.
- Full: Use this constraint to prevent answers from using the brief mention of displacement in breakthrough behavior of PFAS with lower resin affinity as if it were specific, mechanistic evidence about PFHxS and PFOA on IRA910 or in the Maimaiti et al. system. It may only be cited as illustrating that breakthrough displacement can occur for some lower-affinity PFAS in some systems, with no compound-specific details.
- Partial: If an answer notes that some PFAS with lower affinity may show displacement in breakthrough in other studies but clearly states that PFHxS and PFOA behavior is not specified there, treat it as acceptable but still bound by this constraint.
- Contradiction: Flag as violating this constraint if the answer claims that the pilot study directly demonstrates PFHxS displacing PFOA (or vice versa), or provides specific PFHxS vs PFOA breakthrough behavior that is not reported.
- Linked exact evidence:
  - `WF10_035_MMG004`
    > displacement in breakthrough behavior of PFAS with lower resin affinity.
    Supports: Shows that another study notes displacement in breakthrough for PFAS with lower resin affinity, but without naming PFHxS or PFOA or specifying conditions.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

In the study of competitive adsorption on the strong-base anion-exchange resin IRA910 in simulated AFFF-impacted groundwater, PFHxS and PFOA were evaluated as part of a six-compound PFAS mixture.

Under these mixed-PFAS conditions, the authors report that, when six PFAS were present in simulated AFFF-impacted groundwater, their adsorbed amounts on IRA910 decreased in the order PFOS > PFHxS > PFOA > PFBS > PFHxA > PFBA, and summarize that competitive sorption follows the same order.
This ordering indicates that, in this specific mixed-solute system, PFHxS exhibits a higher adsorbed amount and therefore stronger competitive adsorption on IRA910 than PFOA, even though both compounds are removed by the resin.

For PFHxS, the study further reports how co-solutes influence its behavior in this mixed system: nonionic organic compounds (TEC and MB) hardly interfered with PFHxS removal, whereas ionic organic compounds (SDS and HA) significantly decreased the adsorbed amount of PFHxS.
Common inorganic anions (sulfate, bicarbonate, chloride, and phosphate) slightly decreased the removal efficiency of PFHxS, with similar influence among these anions.
Comparable co-solute effects are not detailed for PFOA in the provided evidence, so direct contrasts between PFHxS and PFOA beyond their relative position in the adsorption-order sequence are not reported.

The same work also describes, in separate bisolute systems, that PFHxS co-existing with other PFAS replaced adsorbed PFAS with shorter C–F chains on IRA910, while PFAS with longer C–F chains such as PFOS were not replaced by PFHxS, and the study highlights generally that PFAS with short C–F chains are exchanged by those with long C–F chains.
This language reflects observations under particular bisolute and chain-length–contrast conditions and should not be interpreted as establishing a universal, mechanistically resolved displacement relationship between PFHxS and PFOA across all mixed-groundwater matrices or anion-exchange resins.

Beyond this, a separate pilot study on PFAS treatment with anion-exchange resins notes displacement in breakthrough behavior of PFAS with lower resin affinity, but does not specify which PFAS are involved.
Consequently, it provides only generic support that displacement phenomena can occur for some lower-affinity PFAS during column operation and does not supply compound-specific information about PFHxS or PFOA.

Taken together, the directly supported findings under the studied conditions are:
- In a six-PFAS simulated AFFF groundwater mixture on IRA910, PFHxS has a higher adsorbed amount than PFOA, with competitive sorption in the order PFOS > PFHxS > PFOA > PFBS > PFHxA > PFBA.
- PFHxS adsorption in this system is relatively insensitive to the tested nonionic organic co-solutes but is reduced by ionic organic co-solutes and slightly reduced by several common inorganic anions.

What remains unresolved or not established by the available evidence is:
- Detailed breakthrough curves or retention-time comparisons specifically contrasting PFHxS and PFOA under these mixed conditions.
- A mechanistic demonstration of how, or whether, PFHxS and PFOA displace each other on the resin in mixed-solute groundwater.
- Any broad generalization of the observed behavior and ordering to other resins, other groundwater compositions, or PFAS mixtures beyond those explicitly studied.

Accordingly, the evidence supports a calibrated, system-specific statement that PFHxS is competitively adsorbed more strongly than PFOA in the reported mixed-PFAS IRA910 system, without justifying broader claims about universal displacement or replacement between these two compounds.

### Unresolved or unsupported boundaries

- Any quantitative comparison of breakthrough times, breakthrough curves, or retention times for PFHxS versus PFOA in the IRA910 mixed-PFAS system.
- Direct evidence that PFHxS displaces or replaces PFOA on IRA910 in mixed-solute groundwater, as opposed to a relative difference in adsorbed amounts.
- Mechanistic details of how competitive adsorption among PFHxS, PFOA, and other PFAS occurs at the molecular scale on IRA910 under the mixed conditions.
- Generalization of the observed competitive adsorption order PFOS > PFHxS > PFOA > PFBS > PFHxA > PFBA to other anion-exchange resins, other PFAS mixtures, or other groundwater chemistries.
- Compound-specific interpretation of the phrase "displacement in breakthrough behavior of PFAS with lower resin affinity" for PFHxS or PFOA in the pilot study, which does not name these compounds.

### Complete approved source chunks

#### WF10_035_MMG001

- Role: `required_gold`
- Document: `2018 - Maimaiti - Competitive adsorption of perfluoroalkyl substances on anion exchange resins in simulated AFFF-impacted groundwater.pdf`
- Chunk: `38`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=2e6cb024a7370176f09bf8505a7b56e47a431615a2f7f23bd363cb78c2ed6744].

```text
[SOURCE_TEXT_OMITTED sha256=3b39c726b6ab56cca694f8f181d0ca8465317ec4a9ba44c8203ccb57bbbea024].
```

#### WF10_035_MMG002

- Role: `optional_gold`
- Document: `2018 - Maimaiti - Competitive adsorption of perfluoroalkyl substances on anion exchange resins in simulated AFFF-impacted groundwater.pdf`
- Chunk: `0`
- Registered exact span:  Competitive sorption follows the order of PFOS > PFHxS > PFOA > PFBS > PFHxA > PFBA.

```text
[SOURCE_TEXT_OMITTED sha256=ce1dc43172b64732ce6043d67ae7e72ecae7eab830905e2fc35b9b6802fd329e].
```

#### WF10_035_MMG003

- Role: `negative_gold`
- Document: `2018 - Maimaiti - Competitive adsorption of perfluoroalkyl substances on anion exchange resins in simulated AFFF-impacted groundwater.pdf`
- Chunk: `38`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=2e6cb024a7370176f09bf8505a7b56e47a431615a2f7f23bd363cb78c2ed6744].

```text
[SOURCE_TEXT_OMITTED sha256=3b39c726b6ab56cca694f8f181d0ca8465317ec4a9ba44c8203ccb57bbbea024].
```

#### WF10_035_MMG004

- Role: `optional_gold`
- Document: `2022 - Ellis - Pilot study comparison of regenerable and emerging single-use anion exchange resins for treatment of groundwater contaminated by per- and.pdf`
- Chunk: `48`
- Registered exact span: displacement in breakthrough behavior of PFAS with lower resin affinity.

```text
[SOURCE_TEXT_OMITTED sha256=e0aca7b8fbd57de6c54420333440bb28b2673c7a83d905b1130a124d5f56ffa7]
```

### Deterministic resolution

- Retained MMG001 and MMG003 in the immutable source packet because they preserve distinct human-audited required-gold and negative-gold provenance roles; the normative ledger uses the duplicated source content only once and does not double-weight it.

---

## WF10_039

**Question:** What compound-selectivity behavior has been reported for iron-containing PFAS sorption media, particularly for PFOS versus PFOA?

### Task components

- `WF10_039-T01`: Extract what has been reported about compound-selectivity behavior of iron-containing PFAS sorption media in terms of removal performance, specifically describing any observed differences between PFOS and PFOA (e.g., which compound is removed more effectively or preferentially), without generalizing beyond the reported conditions.
- `WF10_039-T02`: Extract the reported explanation for PFOS-versus-PFOA affinity or selectivity in iron-containing PFAS sorption media, and clearly indicate whether the cited evidence demonstrates a mechanistic basis or merely proposes a mechanism without direct supporting evidence, keeping this distinct from observed treatment performance.

### Normative claim groups

#### WF10_039-G01

- Component: `WF10_039-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In the studied iron-containing green sorption media, PFOS is removed more efficiently than PFOA under both batch and column conditions.
- Full: Award full credit if the answer states that, in the described iron-containing green sorption media systems (including IFGEM-7 and AGEM-2), PFOS shows higher or more efficient removal than PFOA in both batch and/or column experiments, explicitly identifying PFOS as preferentially or more effectively removed under those specific conditions.
- Partial: Award partial credit if the answer notes that PFOS removal exceeds PFOA removal but does not clearly tie this to the iron-containing green sorption media context, or if it mentions only one experimental mode (batch or column) without making clear that this represents observed compound-selective behavior.
- Contradiction: Mark as contradiction if the answer claims that PFOA is removed more efficiently than PFOS in these iron-containing green sorption media, or claims there is no difference in removal between PFOS and PFOA in the reported systems.
- Linked exact evidence:
  - `WF10_039_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=f7adc169f72d725236d9bf71a1e4ab9827b19ffcc5b0bcaec50936662d68d9e8].
    Supports: States explicitly that PFOS can be removed more efficiently than PFOA by the green sorption media, indicating PFOS-selective removal performance.
  - `WF10_039_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=644e572dc258af4f491d4965a032cc0bd1b755e4e74f95d36c057be9c62f519e].
    Supports: Provides quantitative ranges for batch tests showing PFOS removal efficiencies higher than those for PFOA for both IFGEM-7 and AGEM-2 media.
  - `WF10_039_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=6413d12f539357a4cb4ceffef525e38145bc52d0ffcecbac82425a780636e7bf].
    Supports: Shows that under dynamic adsorption in the column (initial 1 h), PFOS removal by IFGEM-7 is much higher than PFOA removal, indicating preferential PFOS removal.
  - `WF10_039_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=a961fd9b04c0e5e88f75a1351333e7d336279d4d06af827404ab8c600a0bb437].
    Supports: Summarizes across batch and column studies that PFOS removal is higher than PFOA removal.

#### WF10_039-G02

- Component: `WF10_039-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: The authors attribute the higher PFOS removal in iron-containing green sorption media to the higher affinity of PFOS sulfonate groups for iron or aluminum compared with the carboxylate groups of PFOA, but this is a proposed explanation rather than a directly demonstrated mechanism in these experiments.
- Full: Award full credit if the answer explains that the higher PFOS removal is attributed to a higher affinity of PFOS sulfonate groups for iron or aluminum relative to the carboxylate groups of PFOA, and explicitly notes that this is an attribution/proposed mechanism (based on observed removal and literature) rather than a directly proven mechanistic interaction in these experiments.
- Partial: Award partial credit if the answer mentions higher sulfonate affinity for iron/aluminum as an explanation for PFOS selectivity but does not clearly distinguish that this is a proposed mechanism instead of directly demonstrated mechanistic evidence.
- Contradiction: Mark as contradiction if the answer asserts that the study directly proves at the mechanistic level (e.g., via spectroscopic binding measurements) that PFOS sulfonate groups bind more strongly to iron/aluminum than PFOA carboxylate groups, or if it claims the authors did not discuss any affinity-based explanation at all.
- Linked exact evidence:
  - `WF10_039_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=a961fd9b04c0e5e88f75a1351333e7d336279d4d06af827404ab8c600a0bb437].
    Supports: Explicitly states that the higher PFOS removal can be attributed to higher affinity of PFOS sulfonate groups for iron or aluminum relative to PFOA carboxylate groups, and uses attribution language rather than describing direct mechanistic proof.
  - `WF10_039_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=496bd2ee50a0209c82810a53861738585a38f1ff6a54858c112911c9acd29f1f].
    Supports: Reiterates that the higher percentage removal of PFOS compared to PFOA can be attributed to higher affinity of PFOS sulfonate groups for iron or aluminum than PFOA carboxylate groups, again as an attribution.
  - `WF10_039_MMG006`
    > [SOURCE_TEXT_OMITTED sha256=b30f86e0d089c65b6c756b82cc02f6a371b75053d4ebf45675618c4cba8579c4] ).
    Supports: States in the results section that the higher removal of PFOS can be attributed to higher affinity of PFOS sulfonate groups toward irons or alumina compared to PFOA carboxylate groups, citing prior work; this is phrased as an attribution rather than direct mechanistic proof.

#### WF10_039-G03

- Component: `WF10_039-T02`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: Additional proposed contributors to PFOS and PFOA sorption in the green media include hydrophobic interactions with sand, electrostatic interactions with clay and iron, and adsorption promoted by hydrophilic films surrounding iron particles; these are presented as likely or attributed mechanisms rather than directly demonstrated mechanisms.
- Full: Award full credit for this supplementary group if the answer notes that the authors propose hydrophobic interactions with sand and electrostatic interactions with clay and iron (including roles of hydrophilic films on iron particles) as contributing to PFOS/PFOA adsorption in the green media, and clarifies that these are described as likely or attributed mechanisms rather than directly proven mechanistic interactions.
- Partial: Award partial credit if the answer mentions hydrophobic or electrostatic interactions or the role of iron-associated films but does not clearly indicate that these are proposed or likely mechanisms rather than directly demonstrated.
- Contradiction: Mark as contradiction if the answer claims that these interaction mechanisms (hydrophobic, electrostatic, hydrophilic films) were directly measured or definitively proven in this study, or if it states that no such mechanistic explanations were discussed.
- Linked exact evidence:
  - `WF10_039_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=dfd64a00a5d929d3a535c261ca96b949c94152d175cd44c0da1186ff1e2495d0].
    Supports: Describes that PFOS and PFOA removal may be governed by hydrophobic interactions with sand and that electrostatic interactions from clay and iron, together with hydrophilic films around iron particles, appear to promote adsorption, indicating proposed mechanisms rather than directly demonstrated ones.
  - `WF10_039_MMG003` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=6fb2396f83a80ec6bb64fa4cfd483d197896f4e1546e090882a47891983151b6]).
    Supports: States that high removals could be attributed to a combination of electrostatic and hydrophobic interactions with sand and clay particles, using attribution language that indicates hypothesized mechanisms.
  - `WF10_039_MMG006` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=323a6984cd229ae8ceebbe3d16984ce6d26327f706faa1502ee5fb6b4525e407].
    Supports: Indicates that the higher PFOS removal could be attributed to synergistic interactions with sand, clay, and ZVI, again framed as an attribution rather than a directly observed mechanistic interaction.

#### WF10_039-G04

- Component: `WF10_039-T01`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: In a granular activated carbon system amended with iron oxide solids, the presence of iron oxide increased PFOA sorption substantially while causing negligible change in PFOS sorption, illustrating a condition-specific difference in how iron-containing phases affect PFOS versus PFOA sorption.
- Full: Award full credit for this supplementary group if the answer notes that, in the cited GAC study, adding iron oxide solids increased PFOA sorption substantially while PFOS sorption showed negligible change, and uses this only as an example of condition-specific compound-selective behavior of iron-containing media rather than a universal rule.
- Partial: Award partial credit if the answer mentions that iron oxide affected PFOA sorption more than PFOS in a GAC system but omits either the direction of the effect or the system context.
- Contradiction: Mark as contradiction if the answer claims that iron oxide solids increased PFOS sorption more than PFOA, or that PFOS and PFOA were affected equally by iron oxide in this GAC system.
- Linked exact evidence:
  - `WF10_039_MMG007`
    > [SOURCE_TEXT_OMITTED sha256=11dac3a888aa679a2c9be6a221d680c8a8f2aec9b3976896288c9b1e22cec1a6].
    Supports: Shows that when iron oxide solids are present with the GACs F400 and CBC, PFOA sorption increases substantially while PFOS sorption changes negligibly, demonstrating differential impact of iron oxide on PFOS vs PFOA sorption in this system.

#### WF10_039-X01

- Component: `WF10_039-T01`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: Findings about PFOS and PFOA selectivity in iron-containing media are specific to the studied green sorption media and GAC systems and should not be generalized to all PFAS treatment scenarios; in the GAC study the influence of iron oxide was minor compared to GAC sorption capacity.
- Full: Answers must not claim that PFOS is always removed more effectively than PFOA in all iron-containing PFAS sorption media. They should respect that selectivity is reported for specific green media formulations and, in a separate GAC study, iron oxide effects are described as minor compared with GAC sorption capacity.
- Partial: If an answer hints at broader applicability but still mentions system context (e.g., specific media or GAC) without explicitly stating universal behavior, treat as partially respecting constraints.
- Contradiction: If an answer generalizes the observed PFOS>PFOA behavior or iron-oxide effects to all iron-containing media or all PFAS treatments without qualification, mark this constraint as violated.
- Linked exact evidence:
  - `WF10_039_MMG007` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=cb42686ea55679b4092dfc4131ed47bd33ebed6cd007e67674dcaf4f6499f5be].
    Supports: Indicates that in the GAC system, iron oxide solids increase PFOA sorption with negligible change in PFOS and that the influence of iron oxide is expected to be minor compared to the GAC sorption capacity, highlighting system-specific and limited impact.
  - `WF10_039_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=e3d19b854368c27e49559ac2d748808704910028364a991b702f0fff91fcad83].
    Supports: Shows the batch-test removal efficiency ranges for PFOS and PFOA and explicitly states that inclusion of aluminum in AGEM-2 did not incrementally contribute to additional PFOS/PFOA removal efficiency, underscoring that metal effects are formulation-specific.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

In the iron-containing green sorption media studied by Ordonez et al. (IFGEM-7 and AGEM-2, which contain sand, clay, and recycled iron and/or aluminum), PFOS consistently shows higher removal than PFOA under the reported conditions. The authors state that “PFOS can be removed more efﬁciently than PFOA from water by green sorption media,” and batch tests show PFOS removal efficiencies ranging from 27–46% and 23–42%, while PFOA removal efficiencies are much lower, 6–16% and 5–18% for IFGEM-7 and AGEM-2, respectively. In column experiments, the initial (within 1 h) removal by IFGEM-7 is reported as greater than 99% for PFOS and 28% for PFOA. The conclusion summarizes that, as evidenced by these batch and column studies, there is “higher removal of PFOS compared to PFOA,” indicating compound-selective behavior favoring PFOS in these media.

The primary affinity explanation offered for this selectivity is that PFOS’s sulfonate headgroup interacts more strongly with iron- or aluminum-bearing phases than PFOA’s carboxylate headgroup. Specifically, the authors state that the higher PFOS removal “can be attributed to the higher afﬁnity [SOURCE_TEXT_OMITTED sha256=750be950ccb540aec664ff7384e0cdec496879ed3def5833b43745eab834b9fa],” and reiterate that “the higher percentage removal of PFOS compared to that of PFOA can be attributed to higher afﬁnity [SOURCE_TEXT_OMITTED sha256=750be950ccb540aec664ff7384e0cdec496879ed3def5833b43745eab834b9fa].” A similar statement appears in the results section, noting that “the higher removal of PFOS can be attributed to higher afﬁnity of sulfonate [SOURCE_TEXT_OMITTED sha256=567236939a1569941559b6f2342fb1cde3e3dc20768831038f4ef93a7f30b364].” These passages frame the affinity explanation as an attribution based on observed removal patterns and prior literature, rather than as a mechanism that is directly demonstrated (for example, no independent binding measurements are reported in the provided text).

The study also proposes additional interaction mechanisms that may contribute to PFOS and PFOA sorption in these green media. With sand as the main ingredient, the authors state that PFOS and PFOA removal “may be primarily governed by hydrophobic interactions,” and that “[SOURCE_TEXT_OMITTED sha256=c06e4590f1394d60d68773c85e402895e9e46266acaa2aae0b0beb9d781de683].” Under dynamic adsorption, they further note that [SOURCE_TEXT_OMITTED sha256=6dbcd9f63231b940187e276b84d62767599f5dfc868dcb10b971f0643d10a9e9]” and that [SOURCE_TEXT_OMITTED sha256=91a0e119f20e1f95bf43562b2ee7a7932a86cf17b0e3ca47209452739bf5a479] surrounding the iron particles.” They also suggest that the higher PFOS removal “could be attributed to the synergistic interactions of PFOS with sand, clay, and ZVI.” The modal language (“may,” “could be attributed,” “likely facilitated”) indicates that these are proposed mechanisms to rationalize the performance, not mechanisms conclusively demonstrated by separate mechanistic assays.

A separate GAC study with iron oxide solids illustrates that iron-containing phases can influence PFOS and PFOA differently in other systems. For granular activated carbons F400 and CBC, the presence of iron oxide solids increased the extent of PFOA sorption by 4.5 mg/g (46%) and 3.8 mg/g (45%), respectively, while PFOS exhibited negligible change (<1 mg/L [10%]) in the presence of iron oxide. The authors add that, although PFAS can sorb onto iron oxide–rich materials, “the influence of iron oxide is expected to be minor compared to the GAC sorption capacity.” This shows that iron oxide can differentially affect PFOA versus PFOS sorption in a GAC system, but that its impact is described as minor relative to the underlying carbon sorption.

Taken together, the supplied evidence supports that, for the specific iron-containing green sorption media tested, PFOS is removed more effectively than PFOA, and this behavior is attributed to higher affinity of PFOS sulfonate groups toward iron or aluminum plus hydrophobic and electrostatic interactions with the media components. These explanations are presented as attributions and likely mechanisms grounded in observed performance and prior literature, rather than as mechanisms directly proven by independent mechanistic measurements. In a different system (GAC with iron oxide solids), iron oxide has a larger relative effect on PFOA than PFOS, underscoring that PFOS-versus-PFOA selectivity in iron-containing media is system- and condition-specific.

### Unresolved or unsupported boundaries

- Whether the higher affinity of PFOS sulfonate groups for iron or aluminum compared to PFOA carboxylate groups was directly quantified in these studies (e.g., via sorption isotherms on isolated iron phases or spectroscopic binding measurements) is not addressed in the provided text.
- Any detailed time-course behavior differences between PFOS and PFOA beyond the initial and general trends described (e.g., full breakthrough curves, long-term kinetic patterns) are not available in the supplied evidence.
- The behavior of PFOS versus PFOA in other types of iron-containing PFAS treatment media (e.g., iron oxides without GAC, other iron-bearing minerals, or different green media formulations) is not supported by the provided excerpts and cannot be inferred.
- Specific quantitative contributions of hydrophobic versus electrostatic interactions, or of iron versus aluminum versus sand/clay, to overall PFOS and PFOA removal are not given in the supplied text.

### Complete approved source chunks

#### WF10_039_MMG001

- Role: `required_gold`
- Document: `2021 - Ordonez - Green sorption media for the removal of perfluorooctanesulfonic acid (PFOS) and perfluorooctanoic acid (PFOA) from water.pdf`
- Chunk: `39`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=a961fd9b04c0e5e88f75a1351333e7d336279d4d06af827404ab8c600a0bb437].

```text
[SOURCE_TEXT_OMITTED sha256=8bcb55b0b2e79f5a2c4e8a742d916474c0169e008d034b7946d4d669dbf0e3d4]
```

#### WF10_039_MMG002

- Role: `required_gold`
- Document: `2021 - Ordonez - Green sorption media for the removal of perfluorooctanesulfonic acid (PFOS) and perfluorooctanoic acid (PFOA) from water.pdf`
- Chunk: `38`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=644e572dc258af4f491d4965a032cc0bd1b755e4e74f95d36c057be9c62f519e].

```text
[SOURCE_TEXT_OMITTED sha256=aa8edaf315adad1759fd96cf2526b5cf36408b11f9b9617eaf1734b043371e3b]
```

#### WF10_039_MMG003

- Role: `required_gold`
- Document: `2021 - Ordonez - Green sorption media for the removal of perfluorooctanesulfonic acid (PFOS) and perfluorooctanoic acid (PFOA) from water.pdf`
- Chunk: `28`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=6413d12f539357a4cb4ceffef525e38145bc52d0ffcecbac82425a780636e7bf].

```text
[SOURCE_TEXT_OMITTED sha256=1f2281b3170f50082841753ddc427dbd69cf8143cf2ca78e92675bd1ab42dd1f]
```

#### WF10_039_MMG004

- Role: `optional_gold`
- Document: `2021 - Ordonez - Green sorption media for the removal of perfluorooctanesulfonic acid (PFOS) and perfluorooctanoic acid (PFOA) from water.pdf`
- Chunk: `0`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=f7adc169f72d725236d9bf71a1e4ab9827b19ffcc5b0bcaec50936662d68d9e8].

```text
[SOURCE_TEXT_OMITTED sha256=616fc7793543a6647065ee15ec5f375e3d5f1dfe755df28f767ec1d64bc249e2]-
```

#### WF10_039_MMG005

- Role: `optional_gold`
- Document: `2021 - Ordonez - Green sorption media for the removal of perfluorooctanesulfonic acid (PFOS) and perfluorooctanoic acid (PFOA) from water.pdf`
- Chunk: `30`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=496bd2ee50a0209c82810a53861738585a38f1ff6a54858c112911c9acd29f1f].

```text
[SOURCE_TEXT_OMITTED sha256=a1ab0a9e9a78f1bf87c1506b092005a33b374ad1564a8932fe0a01a536d12c13]-
```

#### WF10_039_MMG006

- Role: `optional_gold`
- Document: `2021 - Ordonez - Green sorption media for the removal of perfluorooctanesulfonic acid (PFOS) and perfluorooctanoic acid (PFOA) from water.pdf`
- Chunk: `25`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=b30f86e0d089c65b6c756b82cc02f6a371b75053d4ebf45675618c4cba8579c4] ).

```text
[SOURCE_TEXT_OMITTED sha256=95a3befad24f652f358ce61597bb049428f0f34589f3d3a83b9adc2401eb42c6].
```

#### WF10_039_MMG007

- Role: `optional_gold`
- Document: `2019 - Siriwardena - Influence of groundwater conditions and co-contaminants on sorption of.pdf`
- Chunk: `36`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=11dac3a888aa679a2c9be6a221d680c8a8f2aec9b3976896288c9b1e22cec1a6].

```text
[SOURCE_TEXT_OMITTED sha256=25b0ae06eba30f05b0fe646cabbb9b4628a07fb6bf5c86ac66d01c19beb0711c]
```

---

## NQ03a

**Question:** How are PFAS stock standards or calibration standards prepared in published analytical workflows?

### Task components

- `NQ03a-T01`: Describe how PFAS stock standards are prepared in published analytical workflows, including the practical preparation steps (e.g., dilution, solvents, use of commercial mixes vs. in-house preparation) and how the stated/nominal concentrations are established or calculated, without assuming that the nominal label alone guarantees validity.
- `NQ03a-T02`: Explain how concentration accuracy of PFAS stock standards is demonstrated or supported in published workflows, including any checks on traceability, purity, or verification of stock concentrations, and clearly distinguishing these from mere nominal concentration labels on standards.
- `NQ03a-T03`: Describe how PFAS calibration standards are prepared from the stock solutions in published workflows, including dilution schemes, matrices, and handling steps, and how procedures aim to maintain concentration accuracy during calibration standard preparation.
- `NQ03a-T04`: Summarize contamination control measures applied during PFAS stock and calibration standard preparation in published workflows (e.g., controls, blanks, materials and handling practices used to minimize PFAS contamination) and connect these measures explicitly to achieving or preserving accurate concentrations of the standards.

### Normative claim groups

#### NQ03a-G01

- Component: `NQ03a-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Published PFAS workflows commonly prepare stock standards by dissolving PFAS (often purchased as analytical standards or solids) in organic solvents such as methanol or acetonitrile at defined nominal concentrations (e.g., 10 ppm, 1000 mg/L or µg/mL), sometimes as individual stocks and sometimes as mixtures, which then serve as the basis for further dilutions.
- Full: Award full credit if the answer explains, with at least one concrete example, that PFAS stock standards in published methods are prepared by dissolving commercially obtained PFAS (solids or analytical standards) in organic solvents such as methanol or acetonitrile to specified nominal concentrations (e.g., 10 ppm, 1000 mg/L or µg/mL), and recognizes that these are described as nominal preparation steps rather than proven accurate concentrations.
- Partial: Award partial credit if the answer mentions preparation of PFAS stock standards in organic solvents at specified concentrations but omits either the commercial/solid origin of the PFAS, the range of example concentrations, or the fact that these are nominal labels not automatically guaranteeing validity.
- Contradiction: Flag a contradiction if the answer claims that PFAS stock standards in the cited workflows are not prepared using organic solvents at specified concentrations, or asserts that no information is provided about how stock standards are prepared, despite evidence describing such preparations.
- Linked exact evidence:
  - `NQ03a_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=6c71c4d1a0aa502c7ffa629e4bcc8833e919adbd96299c4c3920b0f83a5108e7].
    Supports: Analytical PFCA standards were purchased commercially and used to prepare stock solutions at a nominal concentration of 1000 µg/mL in acetonitrile.
  - `NQ03a_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=57707cce9d0dae3f5b823602c63c8f6201d47bcff0d377577dbf76ab8418cdc2].
    Supports: Target PFCAs obtained as solids were dissolved in methanol to prepare individual stock solutions at a nominal concentration of 1000 mg/L.
  - `NQ03a_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=1cafa09f4fb380e7d41dd07587b4020de6f108fc885ac8ef4f99771ae054104e].
    Supports: Individual PFAS stock solutions were prepared at a nominal 10 ppm concentration in methanol.
  - `NQ03a_MMG008`
    > [SOURCE_TEXT_OMITTED sha256=f498d83e91b942b829ac482ab02af32f4545218f521362408a20e4421ea15019].
    Supports: Concentrated stock solutions for PFOA, PFBS, and PFOS were prepared at specified nominal concentrations of 600 mg/L and 400 mg/L.
  - `NQ03a_MMG006`
    > [SOURCE_TEXT_OMITTED sha256=8a657658884e631a6899b0e4da531f03e8de4daebccd91a7bffc9b702c402bb3].
    Supports: A PFAS stock solution was initially prepared in methanol, consistent with the use of organic solvent for stock preparation.

#### NQ03a-G02

- Component: `NQ03a-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Some workflows go beyond nominal labels by analytically verifying PFAS solution concentrations (e.g., by GC–ECD external calibration showing agreement within ±5% of nominal), whereas other workflows only report nominal stock concentrations without explicit verification, so nominal labels alone are not treated as proof of concentration accuracy.
- Full: Award full credit if the answer notes that some workflows explicitly verify PFAS solution or stock concentrations using analytical measurement against calibration standards (e.g., GC–ECD external calibration showing agreement within a few percent of nominal), and contrasts this with other workflows that only report nominal stock concentrations (such as 1000 µg/mL or 1000 mg/L in organic solvent) without explicit verification, emphasizing that nominal labels alone are not evidence of accuracy.
- Partial: Award partial credit if the answer mentions verification of PFAS solution concentrations against calibration standards but does not clearly contrast this with workflows that only provide nominal concentrations, or if it only describes nominal stock concentrations and vaguely suggests they are assumed accurate without explicit evidence.
- Contradiction: Flag a contradiction if the answer claims that none of the cited workflows verify PFAS solution concentrations analytically, or asserts that nominal stock labels in these studies are explicitly shown to be accurate without any mention of verification steps such as external calibration.
- Linked exact evidence:
  - `NQ03a_MMG006` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=916cf7a53f9200a7ad597933f8a8108524bc10650da084efa1d0ad2ff00529c5].
    Supports: Describes analytical verification of prepared PFOA solution concentrations using GC–ECD with external calibration, with measured concentrations within ±5% of nominal values.
  - `NQ03a_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=6c71c4d1a0aa502c7ffa629e4bcc8833e919adbd96299c4c3920b0f83a5108e7].
    Supports: Provides an example where only the nominal concentration of the stock solution (1000 µg/mL) is stated, with no described verification of this concentration.
  - `NQ03a_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=57707cce9d0dae3f5b823602c63c8f6201d47bcff0d377577dbf76ab8418cdc2].
    Supports: Another example where the stock concentration (1000 mg/L) is given nominally, with no explicit mention of analytical verification in this excerpt.
  - `NQ03a_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=1cafa09f4fb380e7d41dd07587b4020de6f108fc885ac8ef4f99771ae054104e].
    Supports: Illustrates a nominal stock concentration (10 ppm) being reported without accompanying verification details in the text shown.

#### NQ03a-G03

- Component: `NQ03a-T03`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: PFAS calibration or working standards are prepared from stock solutions by dilution into specified matrices (e.g., methanol/water mixtures, ultrapure or Milli-Q water), often using serial dilutions or defined concentration series to span the calibration range, and these schemes aim to maintain concentration accuracy by controlled volumetric dilution and use of clean solvents.
- Full: Award full credit if the answer describes, with multiple examples, that PFAS calibration or working standards are prepared by diluting stock solutions into defined matrices (e.g., methanol/water mixtures, ultrapure or Milli-Q water), using serial or stepwise dilution schemes to generate several concentration levels, and notes that controlled dilution and clean matrices are used to maintain concentration accuracy during calibration standard preparation.
- Partial: Award partial credit if the answer describes dilution of stock PFAS solutions to prepare calibration or working standards but mentions only one example or omits details on the matrices or the multi-level calibration schemes.
- Contradiction: Flag a contradiction if the answer states that calibration standards are not prepared from stock solutions in these workflows, or that no dilution schemes or defined matrices are reported, contrary to the cited evidence.
- Linked exact evidence:
  - `NQ03a_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=12e361f5aabcb36d5c0633f6c6dca745727e214e5b1258218f11d6db09e270c2].
    Supports: Shows that working solutions are prepared by diluting methanol stock solutions with methanol/water (80:20) to achieve the desired concentrations.
  - `NQ03a_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=04e8bb3b1ce4f1b92d916f48e607d6a5e8f10a2f6bc29c599b42259559caba4e]
    Supports: Indicates that an SPME calibration curve was generated by spiking ultra-pure water at 5000 ng/L and diluting it to multiple final concentration levels.
  - `NQ03a_MMG007`
    > [SOURCE_TEXT_OMITTED sha256=f5e1f8fc96ebdfbd66536dfb200bf91fdfeede01e9a00026f9b402f8768d3b60].
    Supports: Indicates that calibration curves are constructed from seven-level dilutions of stock standards in a methanol/water (70:30) matrix, covering 1–250 ng/mL.
  - `NQ03a_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=f0c0a9dff2cde827ec15781ffa8124f268701b9afa840637df518dd8847817ec].
    Supports: Describes calibration curves for PFOA built using standards generated from high-grade PFOA solutions to specified high and low concentration ranges.
  - `NQ03a_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=a116f8956c36609e99f23134ae9afe9c964add38b87ddfd760e22bf88edaa007].
    Supports: Shows that the calibration standards covering 0.5–25 mg/L and 5–500 µg/L were prepared by serial dilution of 50 mg/L and 1 mg/L stock solutions.
  - `NQ03a_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=db406ffb1ef8d83e5b0a55db4ed01e0b57d42e9e9aacc9e935b97a0bf1269623].
    Supports: Shows that working standards of PFCA mixtures or individual PFCAs were prepared by diluting higher-concentration stock solutions to 10 or 1 mg/L.
  - `NQ03a_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=1cafa09f4fb380e7d41dd07587b4020de6f108fc885ac8ef4f99771ae054104e].
    Supports: Confirms that experimental working solutions are obtained by diluting PFAS stock standards to desired concentrations.
  - `NQ03a_MMG008`
    > [SOURCE_TEXT_OMITTED sha256=f498d83e91b942b829ac482ab02af32f4545218f521362408a20e4421ea15019].
    Supports: Indicates that concentrated PFAS stock solutions at specific mg/L levels were prepared as the starting point for subsequent dilutions used in the adsorption tests.
  - `NQ03a_MMG006`
    > [SOURCE_TEXT_OMITTED sha256=8a657658884e631a6899b0e4da531f03e8de4daebccd91a7bffc9b702c402bb3].
    Supports: Shows that working PFOA solutions were prepared by diluting a methanol stock solution into Milli-Q water, using a clean water matrix for subsequent solutions.

#### NQ03a-G04

- Component: `NQ03a-T04`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Contamination control and quality assurance for PFAS standards in the cited workflows include using high-purity or ultrapure water and clean solvent matrices for dilutions, employing method blanks and calibration linearity checks, and in some cases storing solutions in appropriate containers at low temperature, all of which help ensure that prepared standard concentrations are not biased by contamination or instability.
- Full: Award full credit if the answer explains that contamination control and QC for PFAS standards include selecting high-purity matrices (ultrapure or Milli-Q water and clean solvent mixtures) for dilutions, using method blanks and calibration linearity as part of method validation, and appropriate storage of standards, and explicitly links these practices to maintaining accurate and uncontaminated standard concentrations.
- Partial: Award partial credit if the answer mentions some contamination control or QC measures (e.g., use of ultrapure water or method blanks) but does not explicitly connect them to maintaining standard concentrations, or omits either matrix purity or QC/blank aspects.
- Contradiction: Flag a contradiction if the answer claims that no contamination control or QC measures related to PFAS standard preparation are described in these workflows, or if it asserts that low-purity water or undefined matrices are used despite the evidence of ultrapure/Milli-Q water and quality control steps.
- Linked exact evidence:
  - `NQ03a_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=12e361f5aabcb36d5c0633f6c6dca745727e214e5b1258218f11d6db09e270c2].
    Supports: Indicates that stock standard solutions are stored in methanol at low temperature and that working solutions are prepared in a controlled methanol/water (80:20) matrix, practices that help limit contamination and maintain consistent concentrations.
  - `NQ03a_MMG007`
    > [SOURCE_TEXT_OMITTED sha256=f5e1f8fc96ebdfbd66536dfb200bf91fdfeede01e9a00026f9b402f8768d3b60].
    Supports: Shows that calibration dilutions are prepared in a defined methanol/water (70:30) matrix at multiple concentration levels and that calibration curves are used to control the linear range of the instrumental response, supporting reliable standard-based quantification.
  - `NQ03a_MMG004` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > All solutions were stored at 4 ◦ C in polypropylene (PP) bottles.
    Supports: Shows that all solutions, including PFAS standards, were stored at 4 °C in polypropylene bottles, which can help preserve their concentrations over time.
  - `NQ03a_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=57707cce9d0dae3f5b823602c63c8f6201d47bcff0d377577dbf76ab8418cdc2].
    Supports: Shows that PFCA stock solutions in methanol are stored refrigerated at 4 °C, which helps reduce degradation or other changes that could affect concentrations.
  - `NQ03a_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=db406ffb1ef8d83e5b0a55db4ed01e0b57d42e9e9aacc9e935b97a0bf1269623].
    Supports: Indicates that working PFCA standards at 10 or 1 mg/L are also kept refrigerated at 4 °C, helping preserve their concentrations over time.
  - `NQ03a_MMG006`
    > [SOURCE_TEXT_OMITTED sha256=8a657658884e631a6899b0e4da531f03e8de4daebccd91a7bffc9b702c402bb3].
    Supports: Indicates use of Milli-Q water for all working solutions, which reduces the risk of PFAS contamination from the water matrix.
  - `NQ03a_MMG007` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=08b7eab87a038791a358abb0725b922a4a9c3463a0b73d156efc116a2f3b3d38].
    Supports: Shows that quality control and validation employed internal standards, recovery rates, method blanks, and calibration linearity, which help monitor potential contamination or drift associated with standards.
  - `NQ03a_MMG008`
    > [SOURCE_TEXT_OMITTED sha256=f498d83e91b942b829ac482ab02af32f4545218f521362408a20e4421ea15019].
    Supports: Shows that concentrated PFAS stock solutions were prepared at defined mg/L levels before use in adsorption tests, providing controlled starting solutions for subsequent dilutions.

#### NQ03a-X01

- Component: `NQ03a-T01`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: Reporting a nominal concentration for a PFAS stock solution (e.g., 10 ppm, 1000 µg/mL, 1000 mg/L) in these methods does not by itself constitute demonstrated accuracy or traceability of that stock; some studies provide only nominal values without showing additional verification.
- Full: Use this constraint to avoid overclaiming: the presence of a reported nominal stock concentration in the methods should not be described as if it inherently demonstrates concentration accuracy or traceability, particularly when no verification is mentioned in the excerpt.
- Partial: If the answer distinguishes nominal labels from verified concentrations, this constraint is satisfied; if it treats nominal concentrations as proven accurate without additional evidence, this constraint is violated.
- Contradiction: Flag an issue if the answer states that the nominal stock concentrations in these excerpts are explicitly validated when no such validation is described here.
- Linked exact evidence:
  - `NQ03a_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=6c71c4d1a0aa502c7ffa629e4bcc8833e919adbd96299c4c3920b0f83a5108e7].
    Supports: Shows only the nominal concentration of PFCA stock solutions in acetonitrile; no explicit verification is described in this sentence.
  - `NQ03a_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=57707cce9d0dae3f5b823602c63c8f6201d47bcff0d377577dbf76ab8418cdc2].
    Supports: Reports a nominal stock concentration (1000 mg/L in methanol) without describing any analytical verification in this excerpt.
  - `NQ03a_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=1cafa09f4fb380e7d41dd07587b4020de6f108fc885ac8ef4f99771ae054104e].
    Supports: States a nominal 10 ppm concentration in methanol without accompanying verification details in the provided text.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

Across the cited PFAS workflows, stock standards are generally prepared in-house from commercially obtained materials by dissolution in organic solvents at defined nominal concentrations. For example, Habib et al. report that analytical standards of perfluorocarboxylic acids were “purchased from Fisher Scientific … and standard stock solutions of 1000 µg/mL of PFCA were prepared in acetonitrile” (NQ03a_MMG001). Rahman et al. state that “[SOURCE_TEXT_OMITTED sha256=c4933d6767e826c8b998e6d8a3d9270f618285a612e2b1862712ea5f4e8ffc46]” (NQ03a_MMG005). Mel et al. describe that “individual PFAS stock solutions of 10 ppm were prepared in methanol” (NQ03a_MMG004), and Roque et al. prepared “concentrated stock solutions for all the PFAS … with a concentration [SOURCE_TEXT_OMITTED sha256=c8cdb8833b82cbc0c4cd4d1cc8e0f2f279443dcc813fb85b650471c313705e50]” (NQ03a_MMG008). Pavithra and Chakraborty indicate that “the stock solution was initially made with methanol” (NQ03a_MMG006). In all of these cases, the methods sections provide the target nominal stock concentrations and solvents, but the nominal values themselves do not automatically constitute proof of concentration accuracy unless additional verification steps are described.

One of the cited studies explicitly demonstrates concentration accuracy of the prepared PFAS solutions. Pavithra and Chakraborty state that “the concentrations of the prepared PFOA solutions were verified using Gas Chromatography–Electron Capture Detector (GC–ECD) … after derivatization [SOURCE_TEXT_OMITTED sha256=5986067789e33572b4094bc623d77940ed711e835b9aa906f5271f2fbb5c32b3]” (NQ03a_MMG006). This shows that the nominal concentrations of the prepared PFOA solutions were checked against an external calibration curve and found to agree within a defined tolerance. By contrast, several other workflows, such as Habib et al. (1000 µg/mL in acetonitrile; NQ03a_MMG001), Mel et al. (10 ppm in methanol; NQ03a_MMG004), and Rahman et al. (1000 mg/L in methanol; NQ03a_MMG005), provide nominal stock concentrations but, in the provided excerpts, do not describe independent analytical verification of those stock levels. These nominal labels therefore should not be interpreted as demonstrated accuracy or traceability in the absence of such checks.

Calibration and working standards are consistently prepared by controlled dilution of these stock solutions into specified matrices. Olomukoro et al. report that “[SOURCE_TEXT_OMITTED sha256=1d153754e013e8ab0adc079e1cbb5c6c0255e9489d955e7d4f3deac176728889] concentrations” and that, for SPME calibration, “ultra-pure water was spiked at 5000 ng L−1 with the targeted analytes and diluted to give final concentration levels of 0.5, 1, 2.5, 5, 10, 20, 50, 250, 500 …” (NQ03a_MMG002), illustrating stepwise dilution from an initial spike concentration in ultra-pure water to a multi-point calibration series. Urtiaga et al. describe that “dilutions from the stock standard solutions were prepared in methanol/[SOURCE_TEXT_OMITTED sha256=24e0888a34b1f0115d708cfe1ff142800c85b64b6fe3ba014af6c7e729dcd59f]” (NQ03a_MMG007), again indicating preparation of a defined concentration series from stock solutions in a mixed solvent matrix.

Other studies use serial dilution of stock standards to construct calibration or working ranges. Shaikh et al. prepared PFOA calibration curves where “[SOURCE_TEXT_OMITTED sha256=ef0e6bbfb0c9a4e2180a06f296908f38e16d455efb2b7225798e894f32ea551f] µg/L) concentration ranges using standards prepared by high grade PFOA solutions,” with “concentrations … [SOURCE_TEXT_OMITTED sha256=ee4db60313df3fbaf344fe7ae43998e7c38bbf1b61bcde1f1b051ad7986854e1]” (NQ03a_MMG003). Rahman et al. state that “[SOURCE_TEXT_OMITTED sha256=424895a43f5cef082d20926ff4905747510325c9067c71f1eeace94ac758b0d6]” (NQ03a_MMG005), and Mel et al. note that “[SOURCE_TEXT_OMITTED sha256=00ae2ba928ca3170864148d95f16664aca2556e703e0612ba914c30b97a9948d]” (NQ03a_MMG004). Roque et al. indicate that “all the solutions used for the adsorption tests have been prepared by dilution of these stock solutions with ultrapure water” (NQ03a_MMG008), while Pavithra and Chakraborty describe that “Milli-Q water was used to formulate all subsequent working solutions” from a methanol stock (NQ03a_MMG006). Together, these examples show that calibration and experimental standards are generated from stock solutions by serial or stepwise volumetric dilution into methanol/water mixtures or high-purity water matrices, which is intended to preserve the proportionality and accuracy of concentrations across the calibration range.

Several of the workflows incorporate measures that support contamination control and preservation of standard concentrations. Use of high-purity aqueous matrices is common: Olomukoro et al. obtained “ultra-pure water … from a Milli-Q system” (NQ03a_MMG002) and used it both for spiking during calibration and in methanol/water working solutions; Pavithra and Chakraborty note that “Milli-Q water was used to formulate all subsequent working solutions” (NQ03a_MMG006); and Roque et al. report that all adsorption-test solutions were prepared by diluting stocks with “ultrapure water” (NQ03a_MMG008). These practices help minimize exogenous PFAS background that could bias the apparent concentrations of calibration or working standards. Urtiaga et al. further describe method-level quality control: dilutions from stock standards in methanol/water (70:30) were used to build calibration curves “[SOURCE_TEXT_OMITTED sha256=a48b5d64d5bc96ce95555b761d7af8b12385885ca5afcf49b8826f7f65a523b5],” and they state that “quality control and validation of the method were made using internal standards and recovery rates, method blanks and calibration linearity” (NQ03a_MMG007). The use of method blanks and calibration linearity checks helps detect contamination or drift associated with standards and ensures that the calibration response remains reliable over the concentration range.

Handling and storage conditions are also described in some cases in ways that can help preserve accurate concentrations. Mel et al. state that “all solutions were stored at 4 °C in polypropylene (PP) bottles” (NQ03a_MMG004), and Rahman et al. indicate that PFCA stock and working standards were stored in methanol at 4 °C and that working standards were “also kept refrigerated at 4 °C” (NQ03a_MMG005). While these details pertain primarily to solution stability rather than formal verification of concentration, refrigerated storage in suitable containers is consistent with efforts to prevent concentration changes that might arise from degradation or adsorption. Overall, the provided methods show that preparation of PFAS stocks and calibration standards relies on well-defined solvent systems and dilution schemes, with at least one study explicitly verifying concentrations against external calibration and others using high-purity matrices, blanks, and calibration quality checks to support accurate and uncontaminated standard concentrations. At the same time, several methods report only nominal stock concentrations without explicit verification, so nominal labels in those cases should be interpreted as target preparation values rather than inherently validated concentrations.

### Unresolved or unsupported boundaries

- Detailed descriptions of how nominal stock concentrations were calculated from masses and volumes (e.g., weighing procedures, volumetric glassware calibration) are not provided in the supplied excerpts.
- Explicit evidence of traceability of PFAS standards to certified reference materials or primary standards is not described in the provided text.
- Comprehensive purity assessment of PFAS solids or analytical standards (e.g., certificate data, impurity profiling) is not detailed in the excerpts.
- Specific contamination control measures during the physical act of stock preparation (such as PFAS-free labware certification, avoidance of particular polymers, or cleanroom conditions) are not reported in the provided spans, beyond general references to ultrapure/Milli-Q water and blank-based QC.
- Any claim that nominal stock concentrations in Habib, Mel, or Rahman are analytically verified would require additional information beyond the provided excerpts.

### Complete approved source chunks

#### NQ03a_MMG001

- Role: `required_gold`
- Document: `2024 - Habib - Green Analytical Method for Perfluorocarboxylic Acids (PFCAs) in Water of Stir Bar Sorptive Extraction Coupled with Thermal Desorption-Gas.pdf`
- Chunk: `12`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=6c71c4d1a0aa502c7ffa629e4bcc8833e919adbd96299c4c3920b0f83a5108e7].

```text
[SOURCE_TEXT_OMITTED sha256=62e58a2f6b3cb833c03eb7e474418eb920fa9733d13876de19c8bad191bfb13d]
```

#### NQ03a_MMG002

- Role: `required_gold`
- Document: `2021 - Olomukoro - Ion exchange solid phase microextraction coupled to liquid chromatography - laminar flow tandem mass spectrometry for the determination of.pdf`
- Chunk: `10`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=12e361f5aabcb36d5c0633f6c6dca745727e214e5b1258218f11d6db09e270c2].

```text
[SOURCE_TEXT_OMITTED sha256=c8f96a7f5390a0e2813c31ee72bbc524cc759c91e4403bd648dcdcdc9bd39bfc]
```

#### NQ03a_MMG003

- Role: `required_gold`
- Document: `2023 - Shaikh - PFOA remediation from aqueous media using CTAB impregnated activated carbon - A closed-loop sustainable study with comprehensive selectivity analysis.pdf`
- Chunk: `24`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=f0c0a9dff2cde827ec15781ffa8124f268701b9afa840637df518dd8847817ec].

```text
[SOURCE_TEXT_OMITTED sha256=7975e11cf4441bca15e58bb773a018d72cb8d582c72832f90bd05e9a5fe67e95]
```

#### NQ03a_MMG004

- Role: `required_gold`
- Document: `2024 - Mel - Sorption of per- and polyfluoroalkyl substances by lignin in pulp and paper wastewater.pdf`
- Chunk: `8`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=1cafa09f4fb380e7d41dd07587b4020de6f108fc885ac8ef4f99771ae054104e].

```text
[SOURCE_TEXT_OMITTED sha256=483b63e17d5dbb69576a39dfa2c949f83ce5cf8789cdbbbc23b7549e47c595fc]
```

#### NQ03a_MMG005

- Role: `required_gold`
- Document: `2022 - Rahman - Ion-Exchange Treatment of Perfluorinated Carboxylic Acids in Water - Comparison of Polystyrenic and Polyacrylic Resin Structures and Impact of.pdf`
- Chunk: `6`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=57707cce9d0dae3f5b823602c63c8f6201d47bcff0d377577dbf76ab8418cdc2].

```text
[SOURCE_TEXT_OMITTED sha256=8bc0d6945503d84d934377314f350253e5ce7d992c7e9830064f3afe43d6febb]
```

#### NQ03a_MMG006

- Role: `optional_gold`
- Document: `2025 - Pavithra - Adsorption of Perfluorooctanoic Acid from Aqueous Media Using an Engineered Sugarcane Bagasse Biochar-Chitosan Composite.pdf`
- Chunk: `7`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=8a657658884e631a6899b0e4da531f03e8de4daebccd91a7bffc9b702c402bb3].

```text
[SOURCE_TEXT_OMITTED sha256=a66b85180d2b0684530d734bd397aa9766935503b3d7251de34a5940b365a865]
```

#### NQ03a_MMG007

- Role: `required_gold`
- Document: `2022 - Urtiaga - Electrochemical treatment of municipal landfill leachates and implications for poly- and perfluoroalkyl substances (PFAS) removal.pdf`
- Chunk: `16`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=f5e1f8fc96ebdfbd66536dfb200bf91fdfeede01e9a00026f9b402f8768d3b60].

```text
[SOURCE_TEXT_OMITTED sha256=7edb41855dc07521b948d1553a35bcc79e267cca8853ef299c3098e9fb4cac14].
```

#### NQ03a_MMG008

- Role: `required_gold`
- Document: `2025 - Roque - Highly efficient aerogel adsorbent for cleaning process water effluents with high concentration of PFAS.pdf`
- Chunk: `16`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=f498d83e91b942b829ac482ab02af32f4545218f521362408a20e4421ea15019].

```text
[SOURCE_TEXT_OMITTED sha256=70885b8eb708e70935a7d12eb680eecbc811b2c3f42f79e091444975e36cfbe4].
```

---

## NQ07a

**Question:** What sample-container materials and storage conditions are reported for PFAS water samples or extracts?

### Task components

- `NQ07a-T01`: Extract all reported sample-container materials used for collecting PFAS water samples (e.g., bottles, vials, liners), and describe the specific sampling or matrix context in which each material is used (such as type of water, field vs. lab use, expected PFAS levels), making clear that container choice is context-dependent and tied to analyte properties and study conditions.
- `NQ07a-T02`: Extract all reported storage conditions for PFAS water samples prior to extraction (e.g., temperature, duration, light protection, headspace or filling practices, use of preservatives), and link these conditions to both the container materials used and the relevant analyte or matrix properties (e.g., volatility, adsorption concerns, sample type).
- `NQ07a-T03`: Extract all reported sample-container materials used for storing PFAS extracts (post-extraction) and describe the analytical or processing context (e.g., solvent composition, concentration level, time until analysis), emphasizing how container choice depends on the extract composition and PFAS properties.
- `NQ07a-T04`: Extract all reported storage conditions for PFAS extracts (e.g., temperature, storage time, protection from light or evaporation) and connect these conditions to both the chosen container materials and the properties of the PFAS analytes and solvents, without asserting that any one container type is universally safe or mandatory for all PFAS scenarios.

### Normative claim groups

#### NQ07a-G01

- Component: `NQ07a-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: High-density polyethylene (HDPE) containers and tubing are used to collect PFAS-containing landfill leachate, condensate, groundwater, and treatment-column effluent, with authors explicitly noting HDPE’s suitability for minimizing PFAS adsorption in trace-organic sampling contexts.
- Full: Award full credit if the answer states that HDPE containers (including bottles and larger 1–5 L containers) and tubing are used to collect PFAS-containing aqueous samples such as landfill leachate/condensate, groundwater, and treatment effluent, and notes that at least one study explicitly selected HDPE because it minimizes adsorption of PFASs and is suitable for trace organic pollutant sampling.
- Partial: Award partial credit if HDPE is mentioned as a container material for PFAS water samples but without specifying the matrices (e.g., landfill leachate vs. groundwater vs. effluent) or without noting its stated role in minimizing PFAS adsorption or meeting trace-organic sampling requirements.
- Contradiction: Mark as contradicted if the answer claims that HDPE is avoided or considered unsuitable for PFAS water sampling in these contexts, or asserts that HDPE causes high PFAS adsorption in these studies, contrary to the provided evidence.
- Linked exact evidence:
  - `NQ07a_MMG004` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=4f4ad095a9fd763a11a52278e58e17a1d56726071c19486484dad04e628db817] —
    Supports: HDPE 1–5 L containers are used for collected landfill leachate, and HDPE is explicitly chosen because it minimizes adsorption of PFASs and meets trace-organic sampling requirements.
  - `NQ07a_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=61f81f0a9ae66c57c89c1ccb033ce92c862a038324079ba03192a071d5af1571]).
    Supports: HDPE bottles were used in condensate traps along the landfill gas pipeline.
  - `NQ07a_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=df35fad42e3efa6fdacf2610c9caf2fe43e366f7abdaeb95c482b88d1f907769]
    Supports: Groundwater was sampled through an inertial hand pump connected to HDPE tubing.
  - `NQ07a_MMG002` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=efbfdcba6ec1c3b08d4a7787e920989f7b04dfdb2ba95fef3edde4c081eb8d5f]).
    Supports: Clean HDPE sample bottles are used to collect column effluent water for PFAS analysis, with careful rinsing using sample water before filling.

#### NQ07a-G02

- Component: `NQ07a-T01`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: Pre-treated glass containers are used to collect PFAS-relevant groundwater samples at a drinking-water treatment pilot plant, with high-temperature heating and acid washing applied before sampling.
- Full: Award full credit for this group if the answer notes that glass containers (about 800 mL) were used for sampling groundwater at a pilot plant, and that these glass containers were pre-treated by heating to 550 °C for 5 h and then acid washed.
- Partial: Award partial credit if the answer mentions glass containers for PFAS-related water sampling but omits the specific pre-treatment (high-temperature heating and acid washing) or the pilot-plant groundwater context.
- Contradiction: Mark as contradicted if the answer claims that glass containers were not used in PFAS water sampling in this study or that they were used without any pre-cleaning, contrary to the evidence.
- Linked exact evidence:
  - `NQ07a_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=058b278bebd8f1bcc01b871ced67ed4577f919adb22a2b00b239552505c0ddd1].
    Supports: Glass containers of 800 mL volume, pre-heated to 550 °C and acid washed, were selected as sampling containers in a treatment pilot-plant context.

#### NQ07a-G03

- Component: `NQ07a-T01`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: Polypropylene bottles are used to collect influent and effluent water samples for PFAS analysis following EPA Method 537.1, with buffer added to the bottles prior to collection.
- Full: Award full credit for this group if the answer states that 250 mL polypropylene bottles were used to collect influent and effluent water samples for PFAS analysis, and notes that Trizma buffer solids were pre-added to the bottles following EPA Method 537.1 procedures.
- Partial: Award partial credit if the answer mentions polypropylene bottles for PFAS water sampling without specifying the volume, the influent/effluent context, or the addition of Trizma buffer solids.
- Contradiction: Mark as contradicted if the answer asserts that glass or HDPE bottles (but not polypropylene) were used in this specific advanced oxidation pilot study, or denies the use of polypropylene bottles for influent and effluent collection.
- Linked exact evidence:
  - `NQ07a_MMG006` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=4a655937bb8a96dff7e180d71825fe54012ee0213c40fad1a62ffbf4d4dc2beb].
    Supports: Shows that influent and effluent water samples were collected in 250 mL polypropylene bottles with Trizma buffer solids added before sample collection.

#### NQ07a-G04

- Component: `NQ07a-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: PFAS-containing aqueous samples in HDPE, glass, or polypropylene containers are consistently stored cold (approximately 4–8 °C), often under light-limited conditions and with prompt analysis (same day to within 72 h), to limit changes in PFAS concentrations and related matrix properties such as dissolved organic matter and microbial activity.
- Full: Award full credit if the answer describes that PFAS water samples, once collected in their respective containers (HDPE, glass, polypropylene), are stored refrigerated at around 4–8 °C, sometimes in light-proof conditions or under full cold chain, and that analysis or extraction is begun promptly (same day, next day, or within 72 h) to limit changes in PFAS concentrations, DOM morphology, or microbial activity.
- Partial: Award partial credit if the answer mentions cold storage (e.g., 4 °C) for PFAS water samples without linking it to specific container materials, matrix types, or the rationale of preserving PFAS and matrix properties, or if only one study’s conditions are mentioned without recognizing that cold storage is a common approach across different matrices.
- Contradiction: Mark as contradicted if the answer claims that PFAS water samples in these studies were stored at room temperature for extended periods prior to extraction, or that no refrigeration or timing considerations were used, contrary to the provided descriptions.
- Linked exact evidence:
  - `NQ07a_MMG001`
    > Samples were stored below 4 ◦ C until analysis.
    Supports: Indicates that landfill-related samples (including condensate and groundwater collected with HDPE materials) were kept below 4 °C until analysis.
  - `NQ07a_MMG003` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=26535e0e837b176f9aa19aeb305380f805475ad8dbdff2f19bfc77223c7f6c9b].
    Supports: Landfill leachate samples are temporarily stored at 4–8 °C and transported under full cold chain specifically to prevent fluctuations in sample properties.
  - `NQ07a_MMG003` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=353315c67d6ebc0dec6ea353da100fa5406b4149d867aea6a787c99dfd593c66].
    Supports: Leachate samples are stored at a constant 4 °C in a light-proof environment and analyzed within 72 h to inhibit microbial impacts on DOM morphology and PFAS concentrations.
  - `NQ07a_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=71008fe9008a385d05ac8e7aa3ca8aad8f7a5be2cf6e531a6a016353583546f4].
    Supports: Treatment-column effluent samples in HDPE bottles are tightly capped, double bagged, stored in a refrigerator, and shipped in coolers with double-bagged wet ice, indicating refrigerated storage and transport.
  - `NQ07a_MMG005` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > All samples were stored at 4 ◦ C and prepared the same day or the day after sampling.
    Supports: Groundwater samples in glass containers were stored at 4 °C and prepared for analysis the same day or the next day, indicating prompt, cold storage conditions.
  - `NQ07a_MMG006` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > The samples were sealed properly and kept at 4 °C until extraction.
    Supports: Influent and effluent samples in polypropylene bottles were sealed and kept at 4 °C until extraction, reinforcing the consistent use of refrigeration prior to PFAS extraction.

#### NQ07a-X01

- Component: `NQ07a-T01`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: Reported container choices for PFAS water sampling are specific to the study context, matrix, and analytical needs (e.g., landfill leachate vs. groundwater vs. treatment effluent), and the evidence does not support claiming that any single container material is universally required or universally safe for all PFAS scenarios.
- Full: For constraint satisfaction, the answer should not claim that one container type (e.g., HDPE, glass, or polypropylene) is universally safe or mandatory for all PFAS water sampling. It may instead note that different studies used different materials for different matrices and purposes, without overgeneralizing beyond the reported contexts.
- Partial: Partial satisfaction occurs if the answer avoids universal statements about container safety or requirements but does not explicitly highlight that container choice is context-dependent.
- Contradiction: Mark as violated if the answer explicitly claims that a single container material (e.g., HDPE only) is universally safe, preferred, or required for all PFAS sampling scenarios, ignoring the diversity of materials and contexts shown in the evidence.
- Linked exact evidence:
  - `NQ07a_MMG004` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > [SOURCE_TEXT_OMITTED sha256=25d33082f43452eef814b64e9e619ce1db1fd3da87bc6d6b10dbbb2da9cc8d85] —
    Supports: Shows that HDPE containers are chosen in a landfill leachate context for reasons related to PFAS adsorption and trace-organic sampling requirements.
  - `NQ07a_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=058b278bebd8f1bcc01b871ced67ed4577f919adb22a2b00b239552505c0ddd1].
    Supports: Shows that a different study, focused on groundwater treatment, uses glass containers rather than HDPE, indicating container selection varies by context.
  - `NQ07a_MMG006`
    > Inﬂuent and efﬂuent samples were collected directly in a 250 mL poly- propylene bottle.
    Supports: Shows that yet another study uses polypropylene bottles for influent and effluent sampling, further illustrating that no single container type is used across all PFAS sampling scenarios.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

Across the provided studies, several container materials and storage practices are reported for PFAS-containing water samples, and these choices are tied to the specific matrices and analytical needs rather than a single universal standard.

For sample-container materials used at the water-sample collection stage (T01):

• High-density polyethylene (HDPE)
  – Hui et al. sampled landfill leachate at key locations in several landfills and, immediately after collection, divided the samples "[SOURCE_TEXT_OMITTED sha256=3c13b9b4c89e0387168c67d7bec368f9b19cdcd58875e8b70b98a47039d0e021]" [NQ07a_MMG004]. Here, the matrix is landfill leachate containing PFASs and dissolved organic matter (DOM), and HDPE is explicitly chosen to limit PFAS adsorption and to satisfy trace-organic sampling requirements.
  – Chen et al. describe landfill gas and groundwater sampling: condensate traps along the gas pipeline were set up "using HDPE bottles" and "Groundwater was sampled from a monitoring well using a Waterra ® inertial hand pump connected to HDPE tubing" [NQ07a_MMG001]. These HDPE bottles and tubing are used in landfill condensate and groundwater contexts where PFASs are subsequently characterized.
  – In a column-treatment experiment on groundwater, Hayman et al. collected effluent samples to quantify PFAS breakthrough by attaching "clean HDPE sample bottles" directly to the end of each effluent tube; the bottles were "rinsed with a small amount of the sample water three times, then left in place to fill" [NQ07a_MMG002]. The same type of precleaned HDPE bottles was used to collect effluent water for ancillary water-quality measurements [NQ07a_MMG002]. These uses are in a controlled laboratory or pilot-testing context, with low-level PFASs in groundwater-like matrices.

• Glass
  – In a non-target evaluation of drinking water contaminants at a pilot-scale treatment plant, Tisler et al. report that "[SOURCE_TEXT_OMITTED sha256=058b278bebd8f1bcc01b871ced67ed4577f919adb22a2b00b239552505c0ddd1]" [NQ07a_MMG005]. The matrix is untreated and treated groundwater in a pilot plant. The glass containers are extensively pre-cleaned by high-temperature heating and acid washing, consistent with trace-level analysis of PFASs and other contaminants.

• Polypropylene
  – In a pilot study on hydroxyl-radical-based advanced oxidation processes, Venkatesan et al. followed the EPA Method 537.1 framework and state that "Influent and effluent samples were collected directly in a 250 mL polypropylene bottle" and that "[SOURCE_TEXT_OMITTED sha256=c7c3c07c3cb8441d8012a96680f063810da293caff6bfd14bd6b5e985e583e96]" [NQ07a_MMG006]. The context here is influent and effluent water from oxidation processes, with PFASs and their precursors measured; polypropylene bottles are used in conjunction with a buffering agent prescribed by the method.

These examples show that container choice varies by study: HDPE is used for landfill leachate, condensate traps, groundwater, and column effluent (with an explicit rationale of minimizing PFAS adsorption in leachate), glass is used for pilot-scale groundwater treatment sampling after high-temperature and acid cleaning, and polypropylene is used for influent and effluent sampling in an advanced oxidation pilot following EPA 537.1. The evidence therefore supports a context-dependent selection of container materials rather than a single universally mandated container for PFAS water sampling.

For storage conditions of PFAS water samples prior to extraction (T02):

• Landfill leachate and related landfill samples
  – Chen et al. report that samples associated with their landfill study (including groundwater and landfill-related waters collected with HDPE materials) "were stored below 4 ◦ C until analysis" [NQ07a_MMG001], indicating cold storage for PFAS stability.
  – In Hui et al., landfill leachate samples collected into HDPE containers at several landfills were first "temporarily stored in a designated low-temperature area (4 – 8 ◦ C) at the landfill entrance" and then retrieved "via full cold chain to prevent fluctuations in sample properties" [NQ07a_MMG003]. After transport, "they were immediately sent to the Refrigerated Sample Library … [SOURCE_TEXT_OMITTED sha256=75e29b965634f8b6e92b617867328697220105094531bd401e9d242374e6e428]" [NQ07a_MMG003]. Thus, for leachate rich in DOM and PFASs, the authors use HDPE containers plus refrigerated, light-protected storage and initiate analysis within 72 hours, explicitly linking these conditions to preserving DOM morphology and PFAS concentrations and minimizing microbial effects.

• Treatment-column effluent from groundwater (Hayman et al.)
  – Effluent samples collected in HDPE bottles were "[SOURCE_TEXT_OMITTED sha256=4b5ee69769bc8a27f8093fa0ee28dda402c9e80837760dbfdee6547621b74ace] … in coolers with double-bagged wet ice" [NQ07a_MMG002]. Here, PFAS-bearing column effluent is stored refrigerated and protected by double bagging and chilled shipment, again emphasizing low-temperature storage of the HDPE-bottled samples before analysis at an external laboratory.

• Groundwater at a treatment pilot plant (Tisler et al.)
  – For the glass containers used in [SOURCE_TEXT_OMITTED sha256=58aae73bf90d38dfb3eb7ff682c3175b9f69f1cab76bdc6db629a4bffa16338d]" [NQ07a_MMG005]. This indicates refrigerated storage at 4 °C and very short holding times between sampling and analytical preparation in a mixed-target (including PFAS) context.

• Advanced oxidation influent and effluent (Venkatesan et al.)
  – For the polypropylene bottles used in this advanced oxidation pilot, Venkatesan et al. state: "The samples were sealed properly and kept at 4 °C until extraction" [NQ07a_MMG006], indicating that PFAS-influenced influent and effluent waters are refrigerated prior to solid-phase extraction for PFAS analysis.

Taken together, these studies illustrate that PFAS-containing water samples in HDPE, glass, or polypropylene containers are routinely stored refrigerated at about 4–8 °C. In landfill leachate, additional measures such as light-proof storage and analysis within 72 hours are explicitly linked to maintaining DOM morphology and PFAS concentrations and limiting microbial activity. In other matrices (groundwater, column effluent, advanced oxidation influent/effluent), the focus is on maintaining samples at 4 °C and minimizing holding time (same day, next day, or until extraction) to preserve analytes prior to PFAS extraction and analysis.

No information in the provided evidence explicitly describes container materials or storage conditions for post-extraction PFAS extracts (T03 and T04), so extract-storage protocols (such as solvent composition, extract vial material, or long-term freezer conditions) cannot be specified from these records.

Within these limits, the available studies consistently support that container and storage choices for PFAS water samples are context-dependent—varying with matrix (landfill leachate vs. groundwater vs. treatment effluent), analytical method, and concerns such as PFAS adsorption, DOM preservation, and microbial activity—and do not establish any single container material as universally safe or mandatory for all PFAS sampling scenarios.

### Unresolved or unsupported boundaries

- No provided evidence explicitly reports the container materials used for storing PFAS extracts (post-extraction), such as vial material, caps, or liners.
- No provided evidence explicitly describes storage conditions for PFAS extracts (e.g., freezer temperature, storage duration post-extraction, protection from evaporation or light at the extract stage).
- The evidence does not specify headspace management (e.g., filling bottles completely vs. leaving headspace) for PFAS water samples.
- The evidence does not discuss long-term (multi-week or multi-month) storage stability of PFAS in collected water samples or extracts.
- The evidence does not provide a comparative evaluation of different container materials (e.g., HDPE vs. glass vs. polypropylene) under identical conditions; it only reports the chosen materials in each study context.

### Complete approved source chunks

#### NQ07a_MMG001

- Role: `required_gold`
- Document: `2025 - Chen - Per- and polyfluoroalkyl substances (PFAS) in landfill leachate, condensate, and groundwater - Characterization by landfill age and evaluation of.pdf`
- Chunk: `8`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=61f81f0a9ae66c57c89c1ccb033ce92c862a038324079ba03192a071d5af1571]).

```text
[SOURCE_TEXT_OMITTED sha256=87c811ef772e79768e36abe7048cc36a69f0ae716baa83b345e64cdf7d85c5e9]
```

#### NQ07a_MMG002

- Role: `required_gold`
- Document: `2023 - Hayman - Water quality impacts on sorbent efficacy for per- and polyfluoroalkyl substances.pdf`
- Chunk: `16`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=1fb14c06092c4f7758acc9bff2611ca0934063139c076434fd1aaed7ae971448]).

```text
[SOURCE_TEXT_OMITTED sha256=5f458330d5568423145d7d02aff979449e3dc164f55482ffecad3fd40be87e86].
```

#### NQ07a_MMG003

- Role: `optional_gold`
- Document: `2025 - Hui - Adsorption and fate of per- and polyfluoroalkyl substances from landfill leachate onto aquifer media under the influence of dissolved organic matter.pdf`
- Chunk: `9`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=91e06c69a207b5d37a939c96149108d1f08af7e24a58b5ce6514f1088fef0f70].

```text
[SOURCE_TEXT_OMITTED sha256=e634f1ccaf56db01a4115a36bdbc5df24cffdd7410f6fb792a12b980bbeb884a] -
```

#### NQ07a_MMG004

- Role: `optional_gold`
- Document: `2025 - Hui - Adsorption and fate of per- and polyfluoroalkyl substances from landfill leachate onto aquifer media under the influence of dissolved organic matter.pdf`
- Chunk: `8`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=97bf597e97a1cef7081c962b999af93d15265cd0e6a178940c1f45ab2b8b97eb] -

```text
[SOURCE_TEXT_OMITTED sha256=08d754be50cf9ae9a36525fadb861fd5dd0a198013ee06d644337f5388f8e764] -
```

#### NQ07a_MMG005

- Role: `optional_gold`
- Document: `2024 - Tisler - A non-target evaluation of drinking water contaminants in pilot scale activated carbon and anion exchange resin treatments.pdf`
- Chunk: `8`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=058b278bebd8f1bcc01b871ced67ed4577f919adb22a2b00b239552505c0ddd1].

```text
[SOURCE_TEXT_OMITTED sha256=ef44e95898321e8096c9de948f24129362b790e02ae8ec41730ff0f791dc3629]
```

#### NQ07a_MMG006

- Role: `optional_gold`
- Document: `2022 - Venkatesan - Hydroxyl-radical based advanced oxidation processes can increase perfluoroalkyl substances beyond drinking water standards - Results from a.pdf`
- Chunk: `14`
- Registered exact span: Inﬂuent and efﬂuent samples were collected directly in a 250 mL poly- propylene bottle.

```text
[SOURCE_TEXT_OMITTED sha256=1c909ce3d5bcc33f4e3e357f582afbd6eb52213e65e59537f58a37c224531d5b]
```

### Deterministic resolution

- {'claim_group_id': 'NQ07a-G01', 'evidence_id': 'NQ07a_MMG001', 'action': 'split_noncontiguous_span_into_two_verbatim_spans', 'old_span_sha256': 'f70c0a40cedb9ebcf49d02a1c11f4482f08a516462be1ca1ada3179e26fd44f5', 'new_span_sha256': '75c2ed592ac8bc4fcde8b69a6c5358e3b542c68f04eb3790247ccc70e98cfbad'}

---

## NQ07b

**Question:** Do published PFAS studies justify treating HDPE as universally safe or polypropylene as strictly required for sample storage?

### Task components

- `NQ07b-T01`: Summarize how published PFAS studies evaluate HDPE and polypropylene containers for sample storage, explicitly noting what the source evidence does and does not support about their performance.
- `NQ07b-T02`: Assess whether the existing PFAS literature justifies (or fails to justify) treating HDPE as universally safe for all PFAS sample storage scenarios.
- `NQ07b-T03`: Assess whether the existing PFAS literature justifies (or fails to justify) treating polypropylene as strictly required or mandatory for all PFAS sample storage scenarios.
- `NQ07b-T04`: Explain why container choice for PFAS sample storage is context-dependent, explicitly connecting conclusions to analyte properties, storage conditions, and specific source evidence rather than universal claims about container types.

### Normative claim groups

#### NQ07b-G01

- Component: `NQ07b-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In Sadia et al. (2024), sorption of the studied PFAS to HDPE bottle walls was evaluated over 24–96 hours and no sorption to the HDPE walls was observed under those specific experimental conditions.
- Full: Award full credit when the answer notes that in the cited Sadia et al. study, sorption of the studied PFAS to HDPE bottle walls was explicitly evaluated at 24 and 96 hours and that the authors report no PFAS sorbed to the HDPE bottle walls under those specific conditions.
- Partial: Award partial credit if the answer mentions that HDPE was evaluated and that no PFAS sorption was seen, but omits key qualifiers such as time frame (24–96 h), that this is a single study, or that it concerns the specific PFAS studied rather than all PFAS.
- Contradiction: Mark as contradictory if the answer claims that Sadia et al. observed sorption or loss of PFAS to HDPE bottle walls under the reported conditions, or states that the study demonstrated that HDPE always leads to PFAS sorption.
- Linked exact evidence:
  - `NQ07b_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=0ce5214815a55ea806b8b6e176d3ee46c579e0e867103c40edabe32d465c97ac].
    Supports: Direct evidence that HDPE bottle walls were tested for PFAS sorption at 24 and 96 hours and that no PFAS sorption was observed under the study’s conditions.
  - `NQ07b_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > Fig. 1. Chemical structure of the studied per-/poly-fluoroalkyl ether acids (PFEA) with different chain lengths.
    Supports: Indicates that the PFAS evaluated in the study were specific per-/poly-fluoroalkyl ether acids (PFEA), constraining the analyte scope of the HDPE sorption finding.

#### NQ07b-G02

- Component: `NQ07b-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: The available evidence from Sadia et al. (2024) does not justify treating HDPE as universally safe for all PFAS sample storage scenarios because it only assesses sorption of specific PFEA to HDPE bottle walls over 24–96 hours and does not address other PFAS classes, longer storage times, or different conditions.
- Full: Award full credit when the answer explicitly states that the Sadia et al. HDPE result (no sorption at 24–96 h for the studied PFEA) is limited in scope and does not support treating HDPE as universally safe for all PFAS storage scenarios, highlighting that only specific PFAS and conditions were tested.
- Partial: Award partial credit if the answer mentions that the evidence is limited or cannot be generalized to all PFAS or all scenarios but does not clearly connect this to the specific analytes and time frame tested in Sadia et al.
- Contradiction: Mark as contradictory if the answer asserts that the Sadia et al. findings prove HDPE is universally safe for all PFAS storage conditions or implies broad generality without noting the study’s limited scope.
- Linked exact evidence:
  - `NQ07b_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=0ce5214815a55ea806b8b6e176d3ee46c579e0e867103c40edabe32d465c97ac].
    Supports: Shows that HDPE performance was evaluated only over 24 and 96 hours, indicating a limited storage-time scope that cannot by itself establish universal safety across all PFAS storage scenarios.
  - `NQ07b_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > Fig. 1. Chemical structure of the studied per-/poly-fluoroalkyl ether acids (PFEA) with different chain lengths.
    Supports: Shows that only a specific group of PFAS (PFEA with different chain lengths) were studied, which limits the generalizability to other PFAS classes and thus constrains any universal claims about HDPE.

#### NQ07b-G03

- Component: `NQ07b-T03`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: The provided evidence set contains no data on polypropylene containers, so it does not justify treating polypropylene as strictly required or mandatory for PFAS sample storage.
- Full: Award full credit when the answer clearly notes that the supplied evidence discusses only HDPE (and not polypropylene), and therefore cannot justify any claim that polypropylene is strictly required or mandatory for PFAS sample storage.
- Partial: Award partial credit if the answer notes that there is no basis in the provided evidence to require polypropylene, but does not explicitly connect this to the absence of polypropylene evaluations.
- Contradiction: Mark as contradictory if the answer claims that the provided PFAS literature demonstrates polypropylene is required or superior for all PFAS storage scenarios, despite no polypropylene data being present in the supplied evidence.
- Linked exact evidence:
  - `NQ07b_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=0ce5214815a55ea806b8b6e176d3ee46c579e0e867103c40edabe32d465c97ac].
    Supports: Shows that the study focuses specifically on HDPE bottles; the absence of any mention of polypropylene implies no experimental basis here for claiming polypropylene is required or mandatory.

#### NQ07b-G04

- Component: `NQ07b-T04`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: The Sadia et al. (2024) findings illustrate that conclusions about container suitability for PFAS storage are context-dependent, tied to the specific PFAS studied (PFEA) and the 24–96 hour storage window, rather than supporting universal claims about HDPE or polypropylene.
- Full: Award full credit when the answer explains that the Sadia et al. result (no sorption of the studied PFEA to HDPE at 24–96 h) is tied to the specific analytes and time frame, and uses this to argue that container choice is context-dependent rather than governed by universal rules for HDPE or polypropylene.
- Partial: Award partial credit if the answer mentions that container choice is context-dependent and loosely links this to analyte properties or storage time, but does not clearly connect to the specific PFEA and 24–96 h conditions in Sadia et al.
- Contradiction: Mark as contradictory if the answer uses the Sadia et al. findings to claim that container choice is not context-dependent or that a single container material (HDPE or polypropylene) is universally appropriate for all PFAS and conditions.
- Linked exact evidence:
  - `NQ07b_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=0ce5214815a55ea806b8b6e176d3ee46c579e0e867103c40edabe32d465c97ac].
    Supports: Shows that the no-sorption conclusion for HDPE is specific to the evaluated time points (24 h and 96 h) and to the studied PFAS, indicating context dependence in interpreting container performance.
  - `NQ07b_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > Fig. 1. Chemical structure of the studied per-/poly-fluoroalkyl ether acids (PFEA) with different chain lengths.
    Supports: Indicates that the analytes are specific PFEA with different chain lengths, supporting the point that container performance was evaluated for particular PFAS structures, not all PFAS, reinforcing context dependence.

#### NQ07b-X01

- Component: `NQ07b-T02`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: The Sadia et al. (2024) result that no PFAS sorbed to HDPE bottle walls over 24–96 hours for the studied PFEA must not be generalized into a statement that HDPE is universally safe for all PFAS and all storage scenarios.
- Full: Require that answers do not claim universal HDPE safety based solely on the Sadia et al. findings; they must acknowledge the limited scope (specific PFEA, 24–96 h, single study) if generalization is discussed.
- Partial: If an answer hints at HDPE being generally acceptable but avoids explicit universal language, treat this as weakly constrained; only penalize if the universal safe claim is clear.
- Contradiction: Flag as violating the constraint if the answer explicitly states that HDPE is universally safe or always appropriate for all PFAS storage scenarios based on the provided evidence.
- Linked exact evidence:
  - `NQ07b_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=0ce5214815a55ea806b8b6e176d3ee46c579e0e867103c40edabe32d465c97ac].
    Supports: Shows that the evidence for HDPE comes from a single test over specific time points with particular PFAS, which constrains generalization and must not be turned into a universal safety claim.
  - `NQ07b_MMG001` [NEW FULL-CHUNK SPAN: AUTHOR AUDIT REQUIRED]
    > Fig. 1. Chemical structure of the studied per-/poly-fluoroalkyl ether acids (PFEA) with different chain lengths.
    Supports: Reinforces that only certain PFAS (PFEA) were evaluated, which limits the scope of any conclusions about HDPE safety and thus constrains universal claims.

#### NQ07b-X02

- Component: `NQ07b-T03`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: Because the supplied evidence does not evaluate polypropylene containers at all, no claim that polypropylene is strictly required or mandatory for PFAS sampling can be supported from this evidence set.
- Full: Require that answers do not claim polypropylene is strictly required or mandatory for PFAS storage based on the supplied evidence, since polypropylene is not evaluated in the provided study.
- Partial: If an answer speculates about polypropylene but does not state it is mandatory, treat it cautiously; only penalize if strict requirement is asserted.
- Contradiction: Flag as violating the constraint if the answer asserts that polypropylene is required or the only acceptable option for PFAS storage according to the provided literature.
- Linked exact evidence:
  - `NQ07b_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=0ce5214815a55ea806b8b6e176d3ee46c579e0e867103c40edabe32d465c97ac].
    Supports: Indicates that the focus is on HDPE bottles; the lack of any mention of polypropylene shows that the evidence does not support claims about polypropylene being mandatory.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

In the supplied PFAS literature, only one study (Sadia et al. 2024) explicitly evaluates container sorption, and it focuses on HDPE rather than polypropylene. In this work, the authors state that “[SOURCE_TEXT_OMITTED sha256=0ce5214815a55ea806b8b6e176d3ee46c579e0e867103c40edabe32d465c97ac],” and they identify the analytes as “the studied per-/poly-fluoroalkyl ether acids (PFEA) with different chain lengths.” This shows that, for those specific PFEA and for a relatively short storage window of 24–96 hours under the study’s conditions, HDPE bottle walls did not measurably sorb the target compounds.

However, this result is narrowly scoped. It covers only the PFEA structures examined by Sadia et al. and only two time points (24 and 96 hours). The study does not report tests on other PFAS classes, different storage durations, or a range of environmental conditions. As a result, while it supports the use of HDPE for these particular analytes and conditions, it does not justify treating HDPE as universally safe for all PFAS sample storage scenarios.

The provided evidence also contains no experiments involving polypropylene containers. Because polypropylene is not mentioned or evaluated, the evidence cannot be used to argue that polypropylene is strictly required or mandatory for PFAS storage, nor to compare its performance to HDPE.

Overall, the Sadia et al. study illustrates that container performance for PFAS storage is context-dependent: their conclusion of no sorption is tied to specific analyte properties (PFEA) and to the 24–96 hour storage period in HDPE bottles. Without data on other PFAS, longer or different storage conditions, or alternative materials such as polypropylene, the current evidence set does not support universal claims that HDPE is always safe or that polypropylene is mandatory across all PFAS sampling scenarios.

### Unresolved or unsupported boundaries

- Any quantitative comparison of HDPE versus polypropylene performance for PFAS storage is unsupported, because polypropylene data are absent from the supplied evidence.
- Any claim that HDPE is universally safe or always appropriate for all PFAS classes, matrices, or storage durations is not supported by the single HDPE study provided.
- Any assertion that polypropylene is strictly required, superior, or mandatory for PFAS sampling and storage cannot be grounded in the provided evidence, which does not evaluate polypropylene.
- Details about how other PFAS chemistries, matrices, temperatures, or very long storage times affect sorption in HDPE or polypropylene containers are not addressed in the supplied text.

### Complete approved source chunks

#### NQ07b_MMG001

- Role: `optional_gold`
- Document: `2024 - Sadia - Sorption of per- and poly-fluoroalkyl substances and their precursors on activated carbon under realistic drinking water conditions - Insights into.pdf`
- Chunk: `10`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=0ce5214815a55ea806b8b6e176d3ee46c579e0e867103c40edabe32d465c97ac].

```text
[SOURCE_TEXT_OMITTED sha256=593d6a828a99bfe5e71891c828e90acb4afb2994eb769b87156d50ecc891ecb9]
```

---

## NQ25

**Question:** What factors make PFAS adsorption performance difficult to compare between activated carbon and ion-exchange resins?

### Task components

- `NQ25-T01`: Identify and describe the study design and operating-condition factors that make it difficult to directly compare PFAS adsorption performance between activated carbon and ion-exchange resins, including differences in water/wastewater matrices, operating modes, and other experimental conditions, while only comparing like-for-like (comparable compounds, matrices, and operating modes). Mention any reported capacity values only when they are explicitly supported by the source.
- `NQ25-T02`: Identify and describe the PFAS- and adsorbent-specific factors, as well as data reporting and performance-metric choices, that complicate cross-study comparison of adsorption performance between activated carbon and ion-exchange resins for comparable PFAS and conditions. Ensure that any mention of relative capacity is source-supported and avoid any statement that either material is universally higher-capacity for all PFAS under all conditions.

### Normative claim groups

#### NQ25-G01

- Component: `NQ25-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Differences in water matrices and background species alter ion-exchange PFAS sorption behavior, making cross-study comparisons difficult unless matrices are comparable.
- Full: Award full credit if the answer explains that differences in water or wastewater matrix composition, especially the presence of background species such as multivalent cations, anions, and dissolved organic matter in natural waters, can significantly affect PFAS adsorption/removal by ion-exchange resins, and that therefore performance comparisons must be made only for comparable matrices. The explanation should reference that background species can compete with PFAS for ion-exchange sites and can block pores, compromising performance.
- Partial: Award partial credit if the answer mentions that water matrix or co-contaminants affect PFAS adsorption performance for ion-exchange resins, but does not clearly connect this to difficulties in comparing studies or does not emphasize that comparisons should be limited to similar matrices.
- Contradiction: Flag a contradiction if the answer implies that PFAS adsorption performance for ion-exchange resins is independent of water matrix or background species, or that results from one matrix can be universally applied to other matrices without qualification.
- Linked exact evidence:
  - `NQ25_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=308cce6e6248f3149f13c101938801f7601da70c695a5bac383c807876099e99].
    Supports: Shows that background species in natural water matrices can compete with PFAS for ion-exchange resin sites and cause pore blockage, significantly compromising performance and thereby making matrix-dependent comparisons necessary.

#### NQ25-G03

- Component: `NQ25-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Different underlying sorption mechanisms for granular activated carbon and ion-exchange resins mean PFAS properties influence each adsorbent type differently, complicating direct comparison of performance.
- Full: Award full credit if the answer clearly describes that GAC adsorbs PFAS mainly through hydrophobic interactions with pore surfaces plus secondary electrostatic interactions, while anion-exchange resins remove PFAS via a mixture of anion exchange and physical sorption that may be less dependent on PFAS polarity, and explains that these differing mechanisms make direct performance comparisons PFAS- and condition-specific.
- Partial: Award partial credit if the answer notes that sorption mechanisms differ between GAC and ion-exchange resins but does not clearly connect these differences to PFAS property dependence or to difficulties in performance comparison.
- Contradiction: Flag a contradiction if the answer asserts that GAC and ion-exchange resins operate via essentially the same sorption mechanisms for PFAS, or that PFAS properties affect both adsorbent classes in the same way.
- Linked exact evidence:
  - `NQ25_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=8f6c7e3a860a4e47474f79923198e82f21ddc862a29808be0f60fe07d2e7a263].
    Supports: Shows that PFAS adsorption on granular activated carbon is dominated by hydrophobic interactions with pore surfaces and influenced by secondary electrostatic interactions.
  - `NQ25_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=1d258d195ee82a92e6dca5f28135f028dc743f97d41292202c54f31b67d22133].
    Supports: Shows that PFAS sorption onto anion exchange resins involves both anion exchange and physical sorption (e.g., van der Waals), and may be less dependent on PFAS polarity than GAC sorption.

#### NQ25-G04

- Component: `NQ25-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: PFAS chain length and functional group strongly influence sorption affinity on activated carbon and ion-exchange resins, complicating like-for-like comparison across different PFAS classes.
- Full: Award full credit if the answer explains that, for comparable experimental conditions, PFAS sorption affinity varies significantly with chain length and functional group on activated carbon and ion-exchange resins, and notes that short-chain PFCA have significantly lower affinity than long-chain PFAS or short-chain PFSA across all adsorbents tested, emphasizing that comparisons must use the same PFAS species and cannot be generalized across PFAS classes.
- Partial: Award partial credit if the answer mentions that PFAS chain length or functional group affects sorption on one or both adsorbent types but does not clearly relate this to comparison difficulty or cross-material comparison.
- Contradiction: Flag a contradiction if the answer suggests that PFAS chain length or functional group have negligible effect on sorption affinity for either activated carbon or ion-exchange resins, or that relative performance is independent of PFAS speciation.
- Linked exact evidence:
  - `NQ25_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=cabbbf47dd245cc69fca2ad3f3557a30b937c8864575a9aa71c5833492d99d78]).
    Supports: Demonstrates that, across all tested adsorbents (activated carbon and ion-exchange), short-chain PFCA have significantly lower sorption affinity than long-chain PFAS or short-chain PFSA, emphasizing PFAS-class dependence.

#### NQ25-G05

- Component: `NQ25-T02`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: Different preparation routes among commercial granular activated carbons complicate class-wide generalization and cross-study comparison.
- Full: Award full credit if the answer notes that the cited commercial GAC products use different preparation routes and explains that this product-level variation complicates class-wide performance comparisons.
- Partial: Award partial credit if the answer mentions that different GAC products or preparation routes exist but does not connect that variation to the difficulty of cross-study comparison.
- Contradiction: Flag a contradiction if the answer states that all commercial GAC products have the same preparation route or can be assumed to be interchangeable in cross-study comparisons.
- Linked exact evidence:
  - `NQ25_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=5b7753c8241bc0d7000e7e6647be06c23c4e628d410afdc91eb23e02a6b652db].
    Supports: Shows that different GAC products (Filtrasorb 400 and Norit 1240 W) have different origins and preparation methods, implying that PFAS adsorption performance can vary within the GAC class.

#### NQ25-X01

- Component: `NQ25-T02`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: PFAS adsorption performance for activated carbon and ion-exchange resins is PFAS- and condition-specific, and the available evidence does not support universal claims that one class is always higher-capacity or superior under all conditions.
- Full: Ensure the answer does not claim that ion-exchange resins or activated carbon are universally higher-capacity or superior for all PFAS and conditions. The answer should instead emphasize PFAS- and matrix-specific performance, noting that short-chain PFCA have lower sorption affinity on all tested adsorbents and that ion-exchange performance can be severely compromised by background species.
- Partial: If the answer hints that one material is generally better but includes clear qualifications about PFAS type and conditions, treat this as partially respecting the constraint but still note the need for stronger conditional language.
- Contradiction: Flag a contradiction if the answer explicitly states or clearly implies that one adsorbent class (either activated carbon or ion-exchange resins) has universally higher capacity or superior performance for all PFAS and under all conditions.
- Linked exact evidence:
  - `NQ25_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=cabbbf47dd245cc69fca2ad3f3557a30b937c8864575a9aa71c5833492d99d78]).
    Supports: Shows that sorption affinity depends on PFAS class across all adsorbents, indicating performance is PFAS-specific rather than universally high for one material class.
  - `NQ25_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=308cce6e6248f3149f13c101938801f7601da70c695a5bac383c807876099e99].
    Supports: Shows that ion-exchange resin capacity and kinetics are sensitive to background species, emphasizing that performance depends on water matrix conditions rather than being universally superior.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

Several groups of factors make it difficult to directly compare PFAS adsorption performance between granular activated carbon (GAC) and ion‑exchange (IEX) resins, and they mean that meaningful comparisons must be restricted to like‑for‑like PFAS, matrices, and operating modes.

From a study‑design and matrix perspective, ion‑exchange performance is clearly matrix‑dependent. Shaikh and co‑workers note that commercially available ion‑exchange resins, although widely used for PFAS, can have their performance "[SOURCE_TEXT_OMITTED sha256=3423e6fa4a1229003e11343bc7c6453c801dfced89a07f3a2c549cff4ff8c909]," and that these background species can compete with trace‑level PFAS for active sites and contribute to pore blockage, diminishing resin capacity and kinetics.
This means that IEX performance data generated in one water matrix (with a particular mixture and level of competing ions and dissolved organic matter) are not directly transferable to other matrices, and cross‑study comparisons are only valid when the water or wastewater matrices are comparable.

PFAS‑ and adsorbent‑specific factors further complicate direct comparison between GAC and IEX. Mechanistically, Sanzana et al. report that PFAS adsorption on GAC "primarily involve[s] hydrophobic interactions with the pore surfaces of the carbon," with secondary electrostatic interactions that can attract or repel PFAS depending on the GAC surface charge. In contrast, Riegel et al. describe PFAS sorption on anion‑exchange resins as "a mixture of anion exchange and physical sorption, like van der Waals interaction … that might be less dependent on substance polarity." Because GAC emphasizes hydrophobic interactions and surface‑charge effects, whereas IEX combines anion exchange with less polarity‑dependent physical sorption, the same PFAS species can interact differently with each adsorbent under nominally similar conditions. As a result, relative performance rankings between GAC and IEX are PFAS‑ and condition‑specific rather than universally applicable.

Within and across studies, PFAS chain length and functional group also strongly influence adsorption affinity on both material classes. Riegel et al. report that, "[SOURCE_TEXT_OMITTED sha256=ff4215a82267144c465ecb8286d293cdd437a98806a5e18ef0fc7dfd22349519])." This cross‑adsorbent trend shows that short‑chain PFCA are consistently more weakly sorbed than long‑chain PFAS or short‑chain PFSA, regardless of whether GAC or IEX is used. Consequently, comparisons of GAC and IEX performance are only meaningful when the same PFAS (or closely related PFAS classes) are considered; results obtained for one PFAS class (e.g., long‑chain PFSA) cannot be simply generalized to another (e.g., short‑chain PFCA).

There is also substantial variability within adsorbent classes. Franke et al. describe two commercial GACs, noting [SOURCE_TEXT_OMITTED sha256=a910efb318b1bbaaea186f07aa43a6b7eed015c24786dceb11a86b9fecc0d9e3]," and that this preparation difference is a main distinction between the materials. These distinct preparation routes show that the broad GAC label can encompass different commercial materials. Cross-study comparisons that treat all GAC materials as interchangeable may therefore reflect product-specific preparation differences rather than class-wide behavior.

Taken together, the evidence indicates that PFAS adsorption performance for activated carbon and ion‑exchange resins is highly dependent on water matrix composition (especially competing background species), PFAS chain length and functional group, and the specific adsorbent formulation and sorption mechanism. Cross‑study comparison should therefore be limited to like‑for‑like scenarios—matching PFAS chemistries, water matrices, and adsorbent types—and the available evidence does not justify universal claims that either GAC or IEX resins are always higher‑capacity or superior for all PFAS and conditions.

### Unresolved or unsupported boundaries

- The influence of pH, temperature, and ionic strength on comparative PFAS adsorption performance between activated carbon and ion-exchange resins is not described in the available evidence.
- Specific quantitative adsorption capacities (e.g., mg PFAS per g adsorbent) for particular PFAS on GAC versus ion-exchange resins are not reported in the provided excerpts, so no capacity comparison in those units can be made.
- The role of non-PFAS organic micropollutants or natural organic matter in competing with PFAS specifically for GAC adsorption sites is not detailed beyond general pore blockage and competition effects described for ion-exchange resins.
- Regeneration protocols, number of use cycles, and how regeneration affects long-term comparative performance of GAC and ion-exchange resins for PFAS are not covered in the supplied text.
- Detailed hydraulic conditions in column tests (e.g., flow rates, empty bed contact times) and their direct impact on cross-material comparison are not provided in the evidence excerpts.

### Complete approved source chunks

#### NQ25_MMG001

- Role: `optional_gold`
- Document: `2025 - Sanzana - “A review of PFAS remediation - Separation and degradation technologies for water and wastewater treatment”.pdf`
- Chunk: `12`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=8f6c7e3a860a4e47474f79923198e82f21ddc862a29808be0f60fe07d2e7a263].

```text
[SOURCE_TEXT_OMITTED sha256=4c5807b68ed701cf57dcdfa1da0bb531fb553a4b52615d3e1a9a9b3d4d2af206] -
```

#### NQ25_MMG002

- Role: `required_gold`
- Document: `2023 - Riegel - Sorptive removal of short-chain perfluoroalkyl substances (PFAS) during drinking water treatment using activated carbon and anion exchanger.pdf`
- Chunk: `16`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=1d258d195ee82a92e6dca5f28135f028dc743f97d41292202c54f31b67d22133].

```text
[SOURCE_TEXT_OMITTED sha256=4b68a787061f88a26aa49957287f7335d97fe213836178e1b929bae8f7707bda].
```

#### NQ25_MMG003

- Role: `required_gold`
- Document: `2023 - Riegel - Sorptive removal of short-chain perfluoroalkyl substances (PFAS) during drinking water treatment using activated carbon and anion exchanger.pdf`
- Chunk: `1`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=cabbbf47dd245cc69fca2ad3f3557a30b937c8864575a9aa71c5833492d99d78]).

```text
[SOURCE_TEXT_OMITTED sha256=ac27956c41c43bb665af4ac9492bb0620a5c49c1a48df44f60f9da22649a8e78]
```

#### NQ25_MMG004

- Role: `optional_gold`
- Document: `2025 - Shaikh - Efficient removal of short- and long-chain perfluoroalkyl carboxylate acids from surface water matrices using a quaternary ammonium adsorbent.pdf`
- Chunk: `6`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=308cce6e6248f3149f13c101938801f7601da70c695a5bac383c807876099e99].

```text
[SOURCE_TEXT_OMITTED sha256=637632f40bb26f621878759f031fb5cb198127e0d44ca0c4dba1c2c6a47162b1].
```

#### NQ25_MMG005

- Role: `optional_gold`
- Document: `2021 - Franke - The Price of Really Clean Water - Combining Nanofiltration with Granular Activated Carbon and Anion Exchange Resins for the Removal of Per- And.pdf`
- Chunk: `11`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=5b7753c8241bc0d7000e7e6647be06c23c4e628d410afdc91eb23e02a6b652db].

```text
[SOURCE_TEXT_OMITTED sha256=0056c0f19b5b196ed358110795d45c4425d72f51134aeba9038c3ec0aa18bdb7]).
```

### Deterministic resolution

- Trimmed G05 and its prose to the directly supported preparation-route comparison; removed the stale unresolved item about deleted prose.

---

## WF10_017

**Question:** What regeneration approaches have been reported or proposed for PFAS ion-exchange resins, and what practical limitations are noted?

### Task components

- `WF10_017-T01`: From the described studies on PFAS ion-exchange resins, extract the specific regeneration approaches and protocol steps used or proposed, including: the regenerant solutions or other reagents/materials applied, any operating conditions (e.g., contact times, sequence of steps, temperature, pH adjustments, flow or loading changes) that were varied or optimized, the water or waste matrix in which regeneration was tested, the PFAS or PFAS groups targeted, and any reported changes that improved regeneration effectiveness.
- `WF10_017-T02`: From the same studies, extract the practical limitations or challenges reported for these PFAS ion-exchange resin regeneration approaches, including any noted constraints on performance, incomplete regeneration, resin degradation, operational complexity, byproduct or waste management issues, or other factors that limit practical application under the tested conditions.

### Normative claim groups

#### WF10_017-G01

- Component: `WF10_017-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: For PFAS-loaded PS-DVB ion-exchange resins in drinking-water treatment, regeneration with simple chloride brines (about 10% NH4Cl or NaCl, without organic solvent) was identified as an operationally reasonable approach, with chloride outperforming bicarbonate and acetate salts and NaOH being a weaker regenerant than NH4Cl or NaCl.
- Full: Award full credit if the answer notes that, for PFAS-loaded PS-DVB ion-exchange resins in drinking-water treatment, regeneration with relatively high-strength simple chloride brines (described as 10% chloride salt solutions, using NH4Cl or NaCl without organic solvent) was identified as a practical regenerant; that chloride salts performed better than bicarbonate and acetate salts; and that NaOH (higher pH) was a weaker regenerant than NH4Cl or NaCl. Mentioning that this work pertains to drinking-water treatment and PS-DVB resins is required for full credit.
- Partial: Award partial credit if the answer mentions use of chloride brines or simple salt solutions (NH4Cl or NaCl) as regenerants for PFAS-loaded PS-DVB resins or in drinking-water contexts, or notes relative performance trends among chloride, bicarbonate, acetate, and NaOH, but omits either the 10% strength/practicality aspect, the explicit comparison among anions, or the drinking-water/PS-DVB context.
- Contradiction: Mark as contradiction if the answer claims that bicarbonate or acetate salts were superior to chloride for regenerating these PFAS-loaded PS-DVB resins, that NaOH was a stronger regenerant than chloride salts in this study, or that low-strength salt solutions were identified as the most reasonable option instead of the described ~10% chloride brine.
- Linked exact evidence:
  - `WF10_017_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=16e8a95ac74c3d78fc776d34a3890ded0bae78810dcfc8e99390cc083d7f2607].
    Supports: Identifies 10% simple chloride salt solutions without organic solvent as the most reasonable regeneration option for PFAS-loaded PS-DVB resins in full-scale water treatment.
  - `WF10_017_MMG004`
    > [SOURCE_TEXT_OMITTED sha256=b60fd74ee35cff85bd46209af64938434839184c3ad89c6e5d125dc2a0888f40].
    Supports: Shows that chloride salts gave the best regeneration performance for the tested PS-DVB resins, compared to bicarbonate and acetate.
  - `WF10_017_MMG005`
    > [SOURCE_TEXT_OMITTED sha256=c63e528797741c3d1ba6817ae5a1eeda5bfe5398048614dae359f35b675ff2dc].
    Supports: Shows that NaOH was a weaker regenerant compared to NH4Cl or NaCl for PFAS recovery from the resins.
  - `WF10_017_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=8a94a9348c3b5f1c57845b0f400555c4495cbb751bf557e16191cdbf24d57af6].
    Supports: Confirms that the regeneration work was conducted in the context of drinking-water treatment and targeted PFAS including PFCA and PFECA.

#### WF10_017-G02

- Component: `WF10_017-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: For the tested PFAS and PS-DVB resins, regeneration with salt brines and related approaches showed significant limitations: gel-type resins achieved less than 50% recovery for almost all PFAS (with a PFAS-specific gel-type resin showing particularly low recovery), PFAS-specific resins were effectively non-regenerable by conventional methods, and overall regeneration in drinking-water treatment was limited except for short-chain PFCA and PFECA.
- Full: Award full credit if the answer notes that, under the studied regeneration conditions (including 10% chloride brines), PFAS recovery from gel-type resins was often below 50% (with a PFAS-specific gel-type resin showing especially low recovery), that PFAS-specific resins were characterized as non-regenerable by conventional approaches, and that regeneration in drinking-water treatment was considered limited for most PFAS except short-chain PFCA and PFECA.
- Partial: Award partial credit if the answer mentions at least one key limitation from these studies, such as low recovery (<50%) for many PFAS on gel-type or PFAS-specific resins, the difficulty regenerating PFAS-specific resins, or the conclusion that regeneration is limited for most PFAS except short-chain PFCA/PFECA, but does not clearly connect these findings to the specific resin types.
- Contradiction: Mark as contradiction if the answer claims that the tested PFAS-specific resins were readily regenerable by conventional salt-based methods, or that most PFAS showed high (e.g., near-complete) recovery under the described brine regeneration conditions.
- Linked exact evidence:
  - `WF10_017_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=3f1ac9da4514c52eb60b9ea2940116fee9ab73842a3c0358983d1a7b0181a04b].
    Supports: Shows that the two gel-type resins had less than 50% recovery for almost all PFAS, with the PFAS-specific gel-type resin having particularly low recovery.
  - `WF10_017_MMG002`
    > [SOURCE_TEXT_OMITTED sha256=8a94a9348c3b5f1c57845b0f400555c4495cbb751bf557e16191cdbf24d57af6].
    Supports: Explicitly states that regeneration for drinking-water treatment is limited for most PFAS except short-chain PFCA and PFECA, and that this limitation persists across salt type, concentration, pH, and small amounts of organic solvent.
  - `WF10_017_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=57830d81b65e8bc15fa00c600b587527cbca868f0dee85f1aefe70329c571fe6].
    Supports: States that PFAS-specific resins were non-regenerable using conventional regeneration approaches in this study.

#### WF10_017-G03

- Component: `WF10_017-T01`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: Because simple salt solutions did not effectively release PFAS and frequent organic-solvent regeneration was considered impractical, one proposed operational approach was to use simple salt solutions mainly to desorb co-adsorbed major anions and natural organic matter between cycles to restore PFAS uptake sites.
- Full: Award full credit for this group if the answer explains that, because simple salts do not effectively desorb PFAS and organic-solvent regeneration every cycle is impractical, the authors propose using simple salt solutions primarily to regenerate sites occupied by major anions and natural organic matter between cycles to restore PFAS uptake capacity.
- Partial: Award partial credit if the answer mentions either that simple salt regeneration is suggested mainly to desorb co-adsorbed species (not PFAS) or that frequent organic-solvent regeneration is considered impractical, but does not clearly state the proposed use of simple salts to clear co-adsorbed components.
- Contradiction: Mark as contradiction if the answer claims that simple salt solutions were found to effectively and completely release PFAS under these conditions, or that the authors recommended frequent organic-solvent regeneration of the resins every cycle as a practical strategy.
- Linked exact evidence:
  - `WF10_017_MMG009`
    > [SOURCE_TEXT_OMITTED sha256=eac2b1221bf6877dccce6c9e083b4838ca9a41ca366a6d24cfae81748dca948f] );
    Supports: Explicitly states that simple salts do not effectively release PFAS, that regenerating every cycle with organic solvents is not practical, and proposes using simple salts to desorb co-adsorbed major anions and natural organic matter to restore PFAS uptake sites.

#### WF10_017-G05

- Component: `WF10_017-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Riegel et al. demonstrated that mixtures of ethanol with NaOH or HCl could elute a wide range of PFAS from a loaded anion exchange resin using only 3 to 10 bed volumes of regeneration solution.
- Full: Award full credit if the answer states that mixtures of ethanol with NaOH or HCl were used to elute a wide range of PFAS from loaded anion exchange resins, and that satisfactory desorption was achieved with roughly 3–10 bed volumes of regenerant.
- Partial: Award partial credit if the answer mentions the use of ethanol plus NaOH or HCl to regenerate PFAS-loaded anion exchange resins, or mentions the 3–10 bed volumes, but does not capture both aspects together.
- Contradiction: Mark as contradiction if the answer asserts that ethanol plus NaOH or HCl regenerants were ineffective for PFAS desorption, or that many tens of bed volumes were required.
- Linked exact evidence:
  - `WF10_017_MMG006`
    > ([SOURCE_TEXT_OMITTED sha256=b9a11b1be6f76e9643c839f30d895bb52b1d53db6970e9f483cd2d912c7f9130].
    Supports: Provides the key protocol details: mixtures of ethanol and NaOH or HCl as regenerants, applied in 3–10 bed volumes, achieving satisfactory desorption of a wide range of PFAS.

#### WF10_017-G06

- Component: `WF10_017-T02`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Despite the effectiveness of solvent-containing regenerants like ethanol–NaOH/HCl mixtures, practical challenges such as preventing solvent leaching during resin reuse and the need for additional solvent/brine treatment, together with dangerous and expensive waste streams from aqueous or solvent-based regeneration, have led to many such resins being used mainly in single-use-and-dispose modes in water treatment.
- Full: Award full credit if the answer explains that, although solvent-containing regenerants can regenerate PFAS-loaded ion exchange resins, in practice there are major challenges including preventing solvent leaching during reuse and the need for additional solvent/brine treatment, that such resins tend to be used in single-use-and-dispose modes, and that aqueous or solvent-based regeneration produces dangerous and expensive waste streams often incompatible with upstream processes.
- Partial: Award partial credit if the answer mentions at least one key limitation of solvent-containing or aqueous regeneration—such as solvent leaching, waste treatment challenges, or dangerous/expensive waste streams—but not the broader implication that these limitations push systems toward single-use-and-dispose operation.
- Contradiction: Mark as contradiction if the answer claims that solvent-containing regeneration for PFAS-loaded resins poses minimal waste- or solvent-related challenges and is widely and straightforwardly applied in multi-cycle reuse without significant environmental or operational concerns.
- Linked exact evidence:
  - `WF10_017_MMG006`
    > [SOURCE_TEXT_OMITTED sha256=564a35bc5305d8674c6c15b9993d99c4b6d41bd329b90e68285d1a6c728ff82d]).
    Supports: Directly describes the limitations: solvent-leaching challenges, increased effort for solvent/brine treatment, and resulting single-use-and-dispose practice.
  - `WF10_017_MMG007`
    > [SOURCE_TEXT_OMITTED sha256=63d6743ed7d4cbdbd974ff47fe951f8a72efb1a907c3ec5721c3c70b48c80039].
    Supports: Adds that aqueous or solvent-based regeneration creates dangerous, expensive, and often process-incompatible waste streams, reinforcing the practical limitations.

#### WF10_017-G07

- Component: `WF10_017-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Cationic cetyltrimethylammonium bromide (CTAB) was used as a regenerant to efficiently desorb PFOS from saturated ion-exchange resins, and the regenerated resins retained their adsorption efficiency over at least five reuse cycles.
- Full: Award full credit if the answer states that cationic CTAB was used to efficiently desorb PFOS from saturated ion-exchange resins and that the regenerated resins retained their adsorption efficiency for at least five reuse cycles.
- Partial: Award partial credit if the answer mentions CTAB as a regenerant enabling PFOS desorption from ion-exchange resins or the reuse of regenerated resins, but omits either the efficiency of desorption or the reuse-cycle performance.
- Contradiction: Mark as contradiction if the answer claims that CTAB failed to desorb PFOS or that the regenerated resins rapidly lost adsorption efficiency within a small number of cycles under this approach.
- Linked exact evidence:
  - `WF10_017_MMG008`
    > [SOURCE_TEXT_OMITTED sha256=1528828309ed9c09d97dbf4c2722aa7884fe613496c410a45a74b2fc54a14324]] .
    Supports: Identifies CTAB as a cationic regenerant that efficiently desorbed PFOS from saturated ion-exchange resins and is described as a practical regeneration strategy.
  - `WF10_017_MMG008`
    > The regenerated IERs retained their adsorption efficiency over at least five reuse cycles.
    Supports: Shows that regenerated resins maintained adsorption efficiency over at least five reuse cycles.

#### WF10_017-G09

- Component: `WF10_017-T02`
- Importance: `supplementary`
- Scoring role: `supplementary_content`
- Proposition: At a broader technology level, there are knowledge gaps and practical challenges regarding regeneration of PFAS-targeting anion exchange resins, including optimal selection of resins to minimize fouling by natural organic matter and uncertainties and environmental burdens related to regeneration options and waste management.
- Full: Award full credit if the answer explicitly notes that, although anion exchange resins can be advantageous for short-chain PFAS removal, there are knowledge gaps regarding optimal resin selection to minimize negative impacts and natural organic matter fouling, as well as uncertainties and burdens related to regeneration options and associated waste streams.
- Partial: Award partial credit if the answer mentions either knowledge gaps in regeneration options or concerns about fouling and regeneration, but not both components.
- Contradiction: Mark as contradiction if the answer claims that regeneration of PFAS-targeting anion exchange resins is well understood with no major knowledge gaps or environmental/waste challenges identified in the cited literature.
- Linked exact evidence:
  - `WF10_017_MMG010`
    > [SOURCE_TEXT_OMITTED sha256=d3ac32a5c07222c868514a2e5f4869064bfcf33525d0550aadbaaea92a59c0e2] ;
    Supports: States that although anion exchange resins can perform well for short-chain PFAS, there are knowledge gaps in resin selection to reduce negative impacts and natural organic matter fouling, and in regeneration options.
  - `WF10_017_MMG007`
    > [SOURCE_TEXT_OMITTED sha256=63d6743ed7d4cbdbd974ff47fe951f8a72efb1a907c3ec5721c3c70b48c80039].
    Supports: Adds that waste streams from aqueous or solvent-based regeneration are dangerous, expensive, and often incompatible with upstream processes, which is part of the broader challenge and environmental burden.

#### WF10_017-X01

- Component: `WF10_017-T01`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: Findings on regeneration efficiency, regenerant choice, and resin regenerability are resin- and PFAS-specific, and should not be generalized as universally applicable to all PFAS ion-exchange systems, especially PFAS-specific resins that were found non-regenerable by conventional methods and for which simple salt solutions do not effectively release PFAS.
- Full: Use this group to constrain overgeneralization: answers should recognize that regeneration behaviors and optimal regenerants depend on resin type and PFAS, and they should not universalize results from regenerable resins to PFAS-specific resins, which were found non-regenerable by conventional methods and for which simple salt solutions do not effectively release PFAS.
- Partial: Not applicable; this group is for constraint only and does not earn content credit.
- Contradiction: Mark as contradiction under this constraint if an answer implies that PFAS-specific resins in these studies could be effectively regenerated by the same simple salt solutions and conventional approaches that were applied to other resins.
- Linked exact evidence:
  - `WF10_017_MMG003`
    > [SOURCE_TEXT_OMITTED sha256=57830d81b65e8bc15fa00c600b587527cbca868f0dee85f1aefe70329c571fe6].
    Supports: Shows that PFAS-specific resins were non-regenerable with conventional approaches in this particular study.
  - `WF10_017_MMG009`
    > [SOURCE_TEXT_OMITTED sha256=eac2b1221bf6877dccce6c9e083b4838ca9a41ca366a6d24cfae81748dca948f] );
    Supports: States that simple salt solutions do not effectively release PFAS from resins, underscoring limitations of this approach for PFAS desorption.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

Across the cited studies, several regeneration approaches for PFAS-loaded ion-exchange resins and their limitations are described.

For PS-DVB anion-exchange resins used in drinking-water treatment, Liu and Sun evaluated chloride-based brines as regenerants. They note that, [SOURCE_TEXT_OMITTED sha256=bcb95e23256a67edb71a2a5c6f43248b0b1b401880e91397f8c05ac4bc153c29].” In their tests on five PS-DVB resins (including macroporous and gel-type materials), regeneration with chloride brine at this strength was identified as an optimal salt condition. Comparison of different anions showed that “chloride salts worked the best for our five tested PS-DVB resins, followed by bicarbonate and … acetate salts,” and they conclude that bicarbonate, though more eco‑friendly and effective for nitrate-laden resins, “is not suitable for PFAS treatment by PS-DVB resins.” They also examined the influence of pH and base addition by partially replacing NH4Cl or NaCl with NaOH, and observed that “our results indicate that NaOH is a weaker regenerant than NH4Cl or NaCl to recover PFAS.”

Despite optimizing brine composition in this way, regeneration performance was limited for many resin–PFAS combinations. Using 10% brine, “[SOURCE_TEXT_OMITTED sha256=1da565b6f8dfc1cc4b16b18c6d238e5c7dfa61b13cf56f825ba097f59992e981]%).” The authors further conclude [SOURCE_TEXT_OMITTED sha256=900e4e7e6571387765439c3a4a261df802ca5f82dd8db9aa88c2e9e30804b1a4],” and they classify PFAS-specific resins as essentially non-regenerable by standard methods: “the PFAS-specific resins are non-regenerable in our study via the conventional regeneration approaches, consistent with the manufacturer’s recommendation of one-time use.”

Recognizing [SOURCE_TEXT_OMITTED sha256=cad4e4a002198a4b7daa9dbbf7f4dfa2f9e6974217a8c8b7e041bf05f823cabe],” Liu and Sun propose an operational compromise. They suggest that “[SOURCE_TEXT_OMITTED sha256=9b90080310ab7be7605e8fb8d7c03a2f702baa47f260bf33c5ef715dd8ee1250].” In this view, simple brines would mainly clear competing anions and natural organic matter between cycles, with organic-solvent regeneration, if used, applied more sparingly.

Other work summarized by Aumeier et al. highlights solvent-containing regenerants. Riegel et al. “[SOURCE_TEXT_OMITTED sha256=85796aa32793bfab9eccd81f836f7d4e6a44dc906ade8bb481f3c94a7c0328c8] volumes of regeneration solution.” Thus, mixtures of ethanol with NaOH or HCl represent an effective regeneration protocol for PFAS-loaded anion-exchange resins, achieving substantial desorption within a modest number of bed volumes.

However, these advantages are tempered by operational constraints. Aumeier et al. note that “[SOURCE_TEXT_OMITTED sha256=c8483dafaea8fd476ce79ff90bdf61318eb8a38eda0893cbeacdb215017833ba].” More broadly, Sanzana et al. remark that “[SOURCE_TEXT_OMITTED sha256=d6e0cf382d2a6920d7da1eddad7343ccfbffc6261d10acd6a307735dabbb534f] produced them,” underscoring the waste-management challenges associated with both aqueous and solvent-based regeneration.

Additional limitations and knowledge gaps are identified at the technology level. Aumeier et al. state that “[SOURCE_TEXT_OMITTED sha256=b2d1b5f3bf73d920569db49f04bce4792f59497d589375eeabd8ccd75b8fb4f5].” Coupled with Sanzana et al.’s statement that waste streams from aqueous or solvent-based regeneration “are dangerous, expensive to handle, and often incompatible” with the originating processes, this indicates that resin choice, fouling behavior, and downstream handling of regenerant waste are still significant open questions for practical deployment.

Beyond salts and conventional solvent mixtures, other regeneration strategies have been explored. Zheng et al. report that “cationic cetyltrimethylammonium bromide (CTAB) enabled the efficient desorption of PFOS from saturated ion-exchange resins (IERs), providing a practical regeneration strategy.” Importantly for reuse, “The regenerated IERs retained their adsorption efficiency over at least five reuse cycles.” This illustrates a surfactant-assisted desorption approach in which CTAB regeneration maintains resin performance over multiple cycles.

Across these studies, the evidence stresses that regeneration behavior is resin- and PFAS-specific. In Liu and Sun’s work, “PFAS-specific resins are non-regenerable … via the conventional regeneration approaches,” and they also observe that “simple salt solutions do not effectively release PFAS from resins.” As such, while various regenerants (simple chloride brines, solvent-containing mixtures such as ethanol with NaOH or HCl, and CTAB) have been reported or proposed, their practical usefulness is constrained by PFAS chemistry and chain length, resin structure and functionality, solvent-handling and waste-management requirements, and the still-incomplete understanding of optimal regeneration strategies.

### Unresolved or unsupported boundaries

- Specific contact times, flow rates, temperatures, and exact pH values used during the various regeneration procedures are not provided in the cited excerpts.
- The exact composition and concentration details of all regenerant mixtures beyond those explicitly named (e.g., detailed ethanol:water ratios or NaOH/HCl concentrations in Riegel et al.’s mixtures) are not available in the provided evidence.
- The full list of PFAS species beyond classes such as PFCA, PFECA, PFOS, and references to a 'wide range of PFAS' or 'short-chain PFAS anions' is not specified in the quoted text.
- Matrix details for some regeneration studies (e.g., whether Riegel et al. used real or synthetic water matrices) are not explicit in the supplied passages.
- Long-term resin stability (beyond the 'at least five reuse cycles' reported for CTAB regeneration) and any resin degradation phenomena are not described in the available excerpts.

### Complete approved source chunks

#### WF10_017_MMG001

- Role: `required_gold`
- Document: `2021 - Liu - Ion exchange removal and resin regeneration to treat per- and polyfluoroalkyl ether acids and other emerging PFAS in drinking water.pdf`
- Chunk: `37`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=16e8a95ac74c3d78fc776d34a3890ded0bae78810dcfc8e99390cc083d7f2607].

```text
[SOURCE_TEXT_OMITTED sha256=79871ce2bec05e8236830fbd4c941d9f8979e7ff273b022748331924b1e62a97]
```

#### WF10_017_MMG002

- Role: `negative_gold`
- Document: `2021 - Liu - Ion exchange removal and resin regeneration to treat per- and polyfluoroalkyl ether acids and other emerging PFAS in drinking water.pdf`
- Chunk: `39`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=8a94a9348c3b5f1c57845b0f400555c4495cbb751bf557e16191cdbf24d57af6].

```text
[SOURCE_TEXT_OMITTED sha256=c55da14d49f68a278756eacb14b25d8a4421fd2ea741cdb77eabbd1a951e5f37]
```

#### WF10_017_MMG003

- Role: `negative_gold`
- Document: `2021 - Liu - Ion exchange removal and resin regeneration to treat per- and polyfluoroalkyl ether acids and other emerging PFAS in drinking water.pdf`
- Chunk: `41`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=57830d81b65e8bc15fa00c600b587527cbca868f0dee85f1aefe70329c571fe6].

```text
[SOURCE_TEXT_OMITTED sha256=47b63d38f93cc5cc92f902a3beb5216a4a9a060e9ade23e2b54cf56045a69a53]
```

#### WF10_017_MMG004

- Role: `optional_gold`
- Document: `2021 - Liu - Ion exchange removal and resin regeneration to treat per- and polyfluoroalkyl ether acids and other emerging PFAS in drinking water.pdf`
- Chunk: `32`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=b60fd74ee35cff85bd46209af64938434839184c3ad89c6e5d125dc2a0888f40].

```text
[SOURCE_TEXT_OMITTED sha256=ef5835a5ebb88eb32d8c2d1a5b51f04b18cfbbbbdc9aeceec7a5f95691c91817] +
```

#### WF10_017_MMG005

- Role: `optional_gold`
- Document: `2021 - Liu - Ion exchange removal and resin regeneration to treat per- and polyfluoroalkyl ether acids and other emerging PFAS in drinking water.pdf`
- Chunk: `34`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=c63e528797741c3d1ba6817ae5a1eeda5bfe5398048614dae359f35b675ff2dc].

```text
[SOURCE_TEXT_OMITTED sha256=5c7f63d348efce1ddc7729b3e2fb21db2eb965b64bff5ef5aaa85f57535e62bf]
```

#### WF10_017_MMG006

- Role: `required_gold`
- Document: `2023 - Aumeier - Is sorption technology fit for the removal of persistent and mobile organic contaminants from water.pdf`
- Chunk: `16`
- Registered exact span: ([SOURCE_TEXT_OMITTED sha256=b9a11b1be6f76e9643c839f30d895bb52b1d53db6970e9f483cd2d912c7f9130].

```text
[SOURCE_TEXT_OMITTED sha256=054631dff4bcb2c023a5f9d63dad08152848e7391a51518fa6f199f22b00d0eb]
```

#### WF10_017_MMG007

- Role: `negative_gold`
- Document: `2025 - Sanzana - “A review of PFAS remediation - Separation and degradation technologies for water and wastewater treatment”.pdf`
- Chunk: `30`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=63d6743ed7d4cbdbd974ff47fe951f8a72efb1a907c3ec5721c3c70b48c80039].

```text
[SOURCE_TEXT_OMITTED sha256=73d6bf0aaee3bfe3f88bf4d606b0878e21d40186fd720d91ac32c5ee12ea550d]
```

#### WF10_017_MMG008

- Role: `required_gold`
- Document: `2026 - Zheng - Hydrated electron-based UV-advanced reduction processes for efficient PFAS destruction in water - Mechanistic insights and promising applications.pdf`
- Chunk: `33`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=1528828309ed9c09d97dbf4c2722aa7884fe613496c410a45a74b2fc54a14324]] .

```text
[SOURCE_TEXT_OMITTED sha256=1bbbf49871f0fa51c092894973c6c25dc01d8fd1d77b4f579332445af9ba95ba]
```

#### WF10_017_MMG009

- Role: `required_gold`
- Document: `2021 - Liu - Ion exchange removal and resin regeneration to treat per- and polyfluoroalkyl ether acids and other emerging PFAS in drinking water.pdf`
- Chunk: `42`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=eac2b1221bf6877dccce6c9e083b4838ca9a41ca366a6d24cfae81748dca948f] );

```text
[SOURCE_TEXT_OMITTED sha256=d4c4094bd9ba7befd67025c9715be30b257ae975ffcf2afbae78b1cc817bc9ba]
```

#### WF10_017_MMG010

- Role: `optional_gold`
- Document: `2023 - Aumeier - Is sorption technology fit for the removal of persistent and mobile organic contaminants from water.pdf`
- Chunk: `15`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=d3ac32a5c07222c868514a2e5f4869064bfcf33525d0550aadbaaea92a59c0e2] ;

```text
[SOURCE_TEXT_OMITTED sha256=c32760058e8373893dffa169e68efa7ff4a55cebca9431e65790ecc3d994da98]
```

---

## WF10_031

**Question:** For natural raw water membrane studies, what matrix features make PFAS removal harder to compare with simpler water matrices?

### Task components

- `WF10_031-T01`: Identify which features or characteristics of natural raw water matrices (as opposed to simpler or synthetic water matrices) make PFAS removal performance by membranes harder to compare across studies, emphasizing limitations, uncertainties, and caveats rather than general claims.
- `WF10_031-T02`: Describe how the behavior of small PFAS in these natural raw water matrices further complicates direct comparison of membrane PFAS removal results between different water matrices, focusing on negative or limiting evidence rather than universal treatment claims.

### Normative claim groups

#### WF10_031-G01

- Component: `WF10_031-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: Use of natural raw water in a membrane PFAS removal study, when other studies do not use natural raw water, hampers direct comparison of PFAS removal performance across studies.
- Full: Award full credit when the answer states that natural raw water was used in one study while other studies did not, and that this difference in matrix use is explicitly said to hamper or hinder direct comparisons of PFAS removal performance between studies.
- Partial: Award partial credit if the answer notes that differing water matrices (e.g., natural raw water vs. other matrices) complicate or affect comparability between PFAS membrane studies, but does not clearly mention that other studies did not use natural raw water or that this specifically hampers direct comparisons.
- Contradiction: Mark as contradictory if the answer claims that using natural raw water has no effect on comparability across studies, or that it improves or simplifies direct comparisons, contrary to the evidence that it hampers direct comparisons.
- Linked exact evidence:
  - `WF10_031_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=4365e07aa50921c03b865301b8784f82efe80ef8d8c7b614310790f615fa6a70].
    Supports: Directly supports that using natural raw water, when other studies do not, hampers direct comparisons between studies.

#### WF10_031-G02

- Component: `WF10_031-T01`
- Importance: `core`
- Scoring role: `required_content`
- Proposition: In complex real wastewater or natural-type matrices containing many pollutants, competition from multiple pollutants for adsorption or rejection by the membrane can reduce PFAS removal efficiency compared to simpler matrices, complicating comparison of PFAS removal across different water matrices.
- Full: Award full credit when the answer explains that complex matrices (e.g., real wastewater) contain multiple pollutants that compete for adsorption or rejection by the membrane, and that this competition can reduce the efficiency of PFAS removal compared to simpler matrices, thereby complicating direct comparisons.
- Partial: Award partial credit if the answer states that complex or real wastewater matrices contain other pollutants that interfere with or affect PFAS removal, without clearly mentioning competition for adsorption or rejection or reduced efficiency compared to simpler matrices.
- Contradiction: Mark as contradictory if the answer claims that the presence of multiple other pollutants in complex matrices does not affect PFAS removal efficiency or that it makes PFAS removal easier or more efficient compared to simpler matrices.
- Linked exact evidence:
  - `WF10_031_MMG002`
    > 11 pollutants that compete for adsorption or rejection by the membrane.
    Supports: Supports the statement that, in the studied complex matrix, many pollutants compete for adsorption or rejection by the membrane.
  - `WF10_031_MMG002`
    > This competition can reduce the efficiency of the membrane for PFAS removal compared to simpler matrices.
    Supports: Supports that such competition can reduce PFAS removal efficiency relative to simpler matrices, complicating comparisons.

#### WF10_031-X01

- Component: `WF10_031-T01`
- Importance: `core`
- Scoring role: `constraint_only`
- Proposition: The statement that natural raw water use hampers direct comparisons is specific to the cited study context and does not imply a universal rule for all membrane PFAS studies or all natural raw waters.
- Full: Use this constraint to prevent answers from converting the study-specific findings (natural raw water hampering comparisons and competition from multiple pollutants) into universal claims about all PFAS, all membranes, or all water matrices.
- Partial: Partially apply this constraint when answers somewhat overgeneralize but still acknowledge some study specificity.
- Contradiction: Flag as contradicting the constraint if the answer explicitly states or clearly implies that the described limitations apply universally to all PFAS membrane treatments and all water matrices.
- Linked exact evidence:
  - `WF10_031_MMG001`
    > [SOURCE_TEXT_OMITTED sha256=4365e07aa50921c03b865301b8784f82efe80ef8d8c7b614310790f615fa6a70].
    Supports: Shows that the limitation about comparability is framed relative to this specific study's use of natural raw water and other studies not using it, indicating a study-specific context.
  - `WF10_031_MMG002`
    > 11 pollutants that compete for adsorption or rejection by the membrane.
    Supports: Indicates that the described competition and reduced PFAS removal efficiency are observed for a particular complex matrix and should not automatically be generalized to all matrices.

### Latest independent review

Verdict: **clean**

### Non-normative reference prose

Across the available membrane PFAS studies, one key limitation for cross-study comparison is that some work uses natural raw water while many other studies do not. In the natural raw water study, the authors explicitly state that,

"[SOURCE_TEXT_OMITTED sha256=4365e07aa50921c03b865301b8784f82efe80ef8d8c7b614310790f615fa6a70]."

This means that the raw water matrix itself differs from the simpler or synthetic matrices used elsewhere, so differences in PFAS removal cannot be cleanly attributed to the membrane alone.

A second complicating feature of natural or real-world matrices is the presence of many other contaminants. In a study on PFAS removal from real wastewater, the matrix contained

"[SOURCE_TEXT_OMITTED sha256=00a2101f0f8a3a21289a69ff0b05ce8026de7f65ea2bf36f4eeef51656558092]."

Thus, in complex natural or wastewater matrices, multiple co-pollutants vie for adsorption or rejection at the membrane, so observed PFAS removals can be lower than in cleaner, simpler feed waters, making direct comparison across matrices uncertain. These findings should be interpreted as study-specific limitations on comparability, not as universal rules for all membranes, PFAS, or water types. The available evidence does not provide approved detail on how individual small PFAS behave differently in natural raw water versus simpler matrices, so such behavior cannot be specified beyond noting that matrix differences hamper comparisons.

### Unresolved or unsupported boundaries

- Which specific natural raw water characteristics (e.g., exact organic matter levels, inorganic composition) are responsible for the observed differences in PFAS removal are not detailed in the provided evidence.
- Quantitative comparisons of PFAS removal efficiencies between natural raw water and specific simpler or synthetic matrices (including exact percentages, concentrations, or performance metrics) are not given in the provided evidence.
- The approved evidence does not provide detailed, supported descriptions of how small PFAS (e.g., those with molecular weights below the membrane MWCO) behave differently across natural raw water versus simpler or synthetic matrices.

### Complete approved source chunks

#### WF10_031_MMG001

- Role: `required_gold`
- Document: `2019 - Franke - Efficient removal of per- and polyfluoroalkyl substances (PFASs) in drinking water treatment - nanofiltration combined with active carbon or anion.pdf`
- Chunk: `15`
- Registered exact span: [SOURCE_TEXT_OMITTED sha256=4365e07aa50921c03b865301b8784f82efe80ef8d8c7b614310790f615fa6a70].

```text
[SOURCE_TEXT_OMITTED sha256=b83765f1604b08653e2fde773f58d30193f5fd08033072f58793cf48a5cec112]
```

#### WF10_031_MMG002

- Role: `optional_gold`
- Document: `2025 - Minhas - MOF - Polydopamine-modified MXene based mixed matrix membrane for per- and polyfluoroalkyl substances removal from real wastewater.pdf`
- Chunk: `45`
- Registered exact span: 11 pollutants that compete for adsorption or rejection by the membrane.

```text
[SOURCE_TEXT_OMITTED sha256=e4335f3feb523a598e16500c24108ae75a881526df14c63fb0589c9f31fe5b81]
```

---

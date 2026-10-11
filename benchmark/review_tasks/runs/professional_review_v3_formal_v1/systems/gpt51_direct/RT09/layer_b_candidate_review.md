## 1. Conceptual framing: what “disappearance” can and cannot mean

When a target PFAS peak shrinks or vanishes in a chromatogram, that observation alone is ambiguous. It can reflect:

- **Physical processes**: dilution, sorption, volatilization, phase transfer, co-precipitation, encapsulation.
- **Chemical changes**: transformation to other organofluorine products, partial defluorination, or complete mineralization.
- **Analytical artifacts**: matrix suppression, transformation to unmonitored isomers or homologues, or conversion into non-ionized species outside the analytical window.

A rigorous evaluation of “PFAS destruction” therefore requires separating:

- **Removal / separation**: target PFAS is no longer in the measured phase, but its fluorine and carbon remain elsewhere.
- **Transformation**: parent converted to identifiable (and often still persistent/toxic) organofluorine products.
- **Defluorination**: cleavage of C–F bonds with inorganic fluoride formation.
- **Destruction / mineralization**: conversion of organofluorine carbon into inorganic carbon species (e.g., CO₂) plus fluoride, with no substantial residual organofluorine.

The core measurement challenge is to distinguish these outcomes using an internally consistent set of endpoints that track parent PFAS, transformation products (TPs), fluorine, carbon, and toxicity over time.

---

## 2. Comparing key endpoint classes

### 2.1 Parent-compound loss

**What it measures**

- Decrease in concentration of a target PFAS (often via LC–MS/MS) in a given phase (e.g., water).

**What it can support**

- **Evidence of removal from the monitored phase**.
- Evidence of **gross reactivity** if matched with other lines of evidence (e.g., concordant TP formation, fluoride release).

**What it cannot support by itself**

- Proof of **chemical destruction**, **defluorination**, or **mineralization**.
- Even proof of transformation, because:
  - The compound might be sorbed, volatilized, phase-partitioned, or sequestered.
  - The compound might adopt a form outside the analytical window (e.g., strong complexes, different ionization state).

**Critical limitations**

- **Phase specificity**: Reporting loss from water alone is compatible with simple sorption or phase transfer.
- **Isomer/homologue shifts**: Some treatments convert one PFAS to closely related species that may not be included in the MRM list or monitored retention windows.
- **Matrix dependence**: Ion suppression/enhancement can mimic decreases.

**Appropriate interpretation**

- “X% decrease of parent PFAS in [matrix]” or “removal from aqueous phase” – but not “X% destruction” without additional corroboration.

---

### 2.2 Transformation-product (TP) analysis

**What it measures**

- Concentrations of specified organofluorine TPs (e.g., shorter-chain PFAAs from precursor degradation, sulfonamides from sulfonamido precursors, intermediates like perfluoroalkyl carboxylates from sulfonates, etc.).

**What it can support**

- **Evidence of transformation pathways**: When stoichiometrically plausible and kinetically consistent.
- Identification of **intermediate accumulation vs. further degradation**.
- Qualitative indications of **oxidative vs. reductive vs. hydrolytic** mechanisms.

**What it cannot fully resolve**

- Complete mass balance of fluorine or carbon, because:
  - Only a limited TP list is usually monitored.
  - Many TPs are unidentified or analytically challenging (e.g., ultra-short chains, highly polar oligomers, volatile fluorocarbons).
- Toxicity implications, unless TPs are evaluated in parallel bioassays or known to be less / more hazardous.

**Critical limitations**

- **Analytical scope**:
  - Target lists are invariably incomplete; methods prioritize known PFAAs and a subset of precursors.
  - Very small, highly polar, volatile, or zwitterionic TPs may escape standard LC–MS methods.
- **Structural assignment uncertainty**: Suspect screening and non-target workflows can misassign or incompletely identify structures.
- **Quantitation uncertainty**:
  - Lack of authentic standards; semi-quantitative estimation using surrogate-response factors introduces large error.
  - Detection limits often higher for some TPs than parent PFAS.
- **Temporal bias**:
  - Early-time intermediates may be missed with sparse sampling.
  - Long-lived intermediates may require extended observation to see further degradation.

**Appropriate interpretation**

- “Parent transformation to measured organofluorine products A, B, C with [qualitative/quantitative] yields” and “substantial fraction of organofluorine remains unaccounted for” where applicable.
- TP patterns can **support transformation** but rarely prove **complete destruction** without fluorine and carbon balances.

---

### 2.3 Fluoride release (defluorination endpoints)

**What it measures**

- Increase in inorganic fluoride concentration (typically via ion chromatography or specific electrodes).

**What it can support**

- **Evidence of C–F bond cleavage**: net release of F⁻ indicates at least partial defluorination of one or more organofluorine compounds.
- Approximate **degree of defluorination**, if compared to the theoretical fluoride inventory from known PFAS (requires careful stoichiometric accounting).

**What it cannot support by itself**

- Identification of **which PFAS** were defluorinated, to what extent, or by what pathway.
- Proof of **complete mineralization**: remaining carbon may reside in non-fluorinated organics, partially fluorinated organics, or solid residues.
- Distinction between **partial degradation** (e.g., loss of some fluorines, stable partially fluorinated products) and **near-complete defluorination**.

**Critical limitations**

- **Analytical interference**:
  - Background fluoride in matrices (groundwater, wastewater, reagents, glassware).
  - Other fluoride sources or sinks (e.g., fluoride complexation or precipitation as CaF₂ at high pH or in hard waters).
- **Stoichiometric underestimation**:
  - If significant fluorine ends up in organofluorine solids, trapped phases, or volatile species not re-dissolved, measured fluoride underestimates true defluorination.
- **Temporal issues**:
  - Slow secondary defluorination can occur long after parent PFAS disappearance.
  - Short experiments may capture only early-stage fluoride release.

**Appropriate interpretation**

- “Net release of X% of theoretical fluoride from monitored PFAS in [matrix] under [conditions]” – explicitly framed as **partial defluorination** evidence, not full destruction, unless tied to comprehensive carbon and organofluorine analyses.

---

### 2.4 Fluorine mass balance (TOF / EOF vs. target PFAS + TPs)

**What it measures**

- **Total or extractable organofluorine (TOF/EOF)** in a sample (often by combustion ion chromatography), combined with:
  - Target PFAS + TP quantitation (as organofluorine equivalents).
  - Inorganic fluoride measurements.

**What it can support**

- **Fluorine-partition tracking**:
  - Fraction of total fluorine as inorganic F⁻ vs. organofluorine.
  - Fraction of organofluorine that is accounted for by measured PFAS/TPs vs. unidentified organofluorine.
- Assessment of **closing a fluorine balance**, particularly in treatment trains where several phases (water, solids, off-gas) are analyzed.

**What it cannot fully resolve**

- Structural identity, toxicity, or mobility of unidentified organofluorine.
- Carbon fate: EOF/TOF treats all organofluorine carbon equivalently (no distinction between short-chain PFAAs, intermediate fluorinated aromatics, or fluoropolymers).

**Critical limitations**

- **Extraction selectivity**:
  - “Extractable” organofluorine excludes strongly bound fluoropolymers or certain matrix-bound species.
  - Different methods capture different fractions (e.g., solid-phase extraction vs. total combustion).
- **Sensitivity**:
  - Detection limits for TOF/EOF can be relatively high; low-level residuals may go undetected.
- **Complex matrices**:
  - High organic loads (sludges, soils) complicate extraction and can yield partial recovery.
- **Multi-phase balances**:
  - Off-gas and solid-phase fluorine often poorly characterized; incomplete accounting can misrepresent total fluorine recovery.

**Appropriate interpretation**

- “X% of initial fluorine recovered as inorganic F⁻, Y% as identified organofluorine, Z% as unidentified organofluorine in [phases].”  
- If unidentified organofluorine remains significant, **destruction claims must be correspondingly conservative**.

---

### 2.5 Mineralization-related endpoints (carbon fate)

**What they measure**

- CO₂ production (often via TOC/IC, respirometry, or gas-phase analysis).
- Changes in total organic carbon (TOC) or dissolved organic carbon (DOC).
- Sometimes gas-phase carbon-containing products (CO, CH₄, low-molecular-weight organics).

**What they can support**

- **Carbon mineralization**: reduction in organic carbon combined with increased inorganic carbon suggests conversion of organic carbon to CO₂.
- Differentiation between:
  - Conversion of PFAS to non-fluorinated organic carbon vs.
  - Complete oxidation to CO₂ (requires tracing carbon from PFAS, e.g., isotopic labelling in rigorously designed studies).

**What they cannot support by themselves**

- The fluorine fate: mineralization of carbon does not guarantee complete defluorination, especially in systems where volatile or solid inorganic fluorides may be unmeasured.
- Exclusivity: TOC reduction can arise from sorption, stripping, or co-oxidation of non-PFAS organics in complex matrices.

**Critical limitations**

- **Non-specificity**:
  - TOC/DOC measures all organic carbon, not selectively PFAS-derived carbon.
  - Without isotopic or specific markers, co-contaminant degradation can dominate apparent mineralization.
- **Phase losses**:
  - Gas-phase organics may appear as TOC loss but represent volatilization, not destruction.
- **Temporal issues**:
  - Slow mineralization may lag behind rapid parent removal or TP formation.

**Appropriate interpretation**

- “X% reduction in DOC, Y% increase in inorganic carbon; however, contribution from PFAS vs. other organics remains uncertain unless specifically traced.”  
- Mineralization of PFAS requires **both** carbon-specific evidence (ideally) and fluorine-specific accounting.

---

## 3. How analytical scope, timing, detection limits, and unknowns affect interpretation

### 3.1 Analytical scope and method coverage

The **breadth and depth** of analytical coverage fundamentally constrain what can be concluded:

- **Narrow target lists**:
  - Risk underestimating TP formation and overinterpreting parent loss as destruction.
  - Particularly problematic for precursor-rich matrices (AFFF, industrial wastewaters, landfill leachates) where many unknown PFAS exist.
- **LC-only or MS-only limitations**:
  - Volatile and ultra-short-chain species may not be captured in standard LC–MS workflows.
  - Adsorbed or particle-bound PFAS and TPs may be underrepresented if sample preparation emphasizes dissolved phases.
- **Fluorine-only metrics (TOF/EOF)**:
  - Cannot distinguish benign from problematic organofluorine.
  - Useful for mass balance but not hazard assessment without structural information.

Result: The **smaller the analytical window**, the greater the need for interpretive caution. Claims should be constrained to the species and phases actually measured.

### 3.2 Sampling time scales and kinetics

Time-resolved data are critical:

- **Short experiments**:
  - Capture early parent loss and TP formation but may miss:
    - Slow TP degradation.
    - Long-term release of fluoride and carbon mineralization.
- **Single end-point sampling**:
  - Cannot distinguish transient vs. stable intermediates.
  - Obscures sequential pathways (e.g., precursor → intermediate PFAA → further defluorination).

Key design considerations:

- Capture multiple time points spanning:
  - Initial rapid transformations (minutes–hours) and
  - Longer-term processes (days–weeks) for biological or mild chemical treatments.
- For high-energy or thermal treatments, include:
  - Immediate products (including gases and particulates).
  - Potential reformation products downstream (e.g., cooling or off-gas handling systems).

Without appropriately long and frequent sampling, serious misinterpretation is likely—e.g., an observed fluoride plateau at short times may represent only early-stage defluorination.

### 3.3 Detection limits and quantification ranges

Detection and quantification limits shape conclusions:

- **High detection limits**:
  - Allow residual PFAS and TPs to evade detection.
  - Encourage overstatement of “removal” or “destruction” if reported simply as “not detected.”
- **Differential sensitivity across analytes**:
  - Parent PFAS often measured more sensitively than many TPs.
  - Apparent “no TP formation” may reflect poor detectability rather than true absence.
- **Non-target / suspect screening**:
  - Semi-quantitative results with high uncertainty; useful for revealing complexity, not for tight mass balances.

Interpretive practice:

- Always couple “not detected” with:
  - The corresponding detection limit.
  - The fraction of initial mass that the detection limit represents (e.g., <1% of initial parent mass).
- Avoid interpreting below-LOQ levels as zero, especially for hazard assessment or regulatory decisions.

### 3.4 Unidentified products and unresolved organofluorine

Even with advanced workflows, **a fraction of organofluorine will remain uncharacterized**:

- TOF/EOF minus known PFAS/TP fluorine provides an estimate of this “dark fluorine.”
- Unidentified organofluorine may reside in:
  - Novel TPs.
  - Matrix-bound residues.
  - Partially degraded high-mass species.
  - Polymer fragments or oligomers.

Implications:

- When a significant fraction of the initial fluorine remains as unidentified organofluorine, claims of “destruction” must be framed **as partial at best**.
- Qualitative improvements (e.g., reduction in toxicity, mobility, or bioaccumulation) cannot be assumed; they require direct assessment.

---

## 4. A defensible evidence hierarchy for PFAS “destruction”

A coherent hierarchy helps align claims with evidence quality. Below is a **conceptual ladder**, with each level requiring specific measurements and acknowledging limitations.

### Level 1 – Parent PFAS removal from a monitored phase

**Evidence**

- Decrease in parent PFAS concentration in a specific phase (e.g., water) below detection.

**Minimum data**

- Target PFAS in the treated phase (LC–MS/MS or equivalent).
- Basic quality controls (recovery, matrix effects).

**Interpretation**

- “Removal from [phase] under [conditions].”  
- No claim of transformation, defluorination, or destruction. The process may be **separative** (adsorption, phase transfer).

**Typical technologies at this level**

- Adsorption (e.g., activated carbon, resins).
- Membrane separation, foam fractionation, some co-precipitation approaches.

---

### Level 2 – Parent removal with identified TPs

**Evidence**

- Parent PFAS decrease concurrent with formation of identifiable TP(s), with plausible stoichiometry and kinetics.

**Minimum data**

- Parent and monitored TP concentrations across multiple time points.
- Aqueous-phase and, where relevant, solid-phase analyses.
- Recovery controls for both parent and TPs.

**Interpretation**

- “Parent transformed to specific TPs; net conversion X% of parent mass to measured TPs in [phase(s)].”  
- No global destruction claim; defluorination not established unless fluoride is quantified.

**Limitations**

- Unmonitored TPs and phases still represent unaccounted mass.
- Hazard may be unchanged or increased depending on TP properties.

---

### Level 3 – Demonstrated partial defluorination

**Evidence**

- Fluoride release measured, attributable to PFAS degradation, with at least approximate stoichiometry based on known PFAS inventory.

**Minimum data**

- Parent and key TPs in relevant phases.
- Inorganic fluoride concentration over time, with background/blank correction.
- Fluorine mass balance at least in the main reaction phase (initial PFAS fluorine vs. final inorganic fluoride + remaining organofluorine).

**Interpretation**

- “Net defluorination of X% of initial PFAS fluorine under [conditions], with Y% of fluorine remaining as organofluorine (Z% identified, (Y−Z)% unidentified).”  
- This supports **partial destruction of C–F bonds**, but not full mineralization or elimination of organofluorine.

**Limitations**

- Solid-phase and gas-phase fluorine may still be under-characterized.
- TPs may retain significant fluorine and toxicity.

---

### Level 4 – High-degree defluorination with constrained organofluorine residues

**Evidence**

- Large fraction of initial fluorine measured as inorganic fluoride.
- Residual organofluorine minimized and characterized to the extent possible.

**Minimum data**

- Multi-phase fluorine mass balance:
  - Inorganic F⁻ in water, solids, and where relevant, condensates.
  - TOF/EOF in residual phases, compared to initial fluorine.
- Target and non-target/suspect TP analysis to reduce the unknown organofluorine fraction.
- Time-resolved measurements confirming stable plateau (no rebound).

**Interpretation**

- “High-degree defluorination, with ≥X% of initial fluorine present as inorganic F⁻ and ≤Y% as residual organofluorine across [phases].”  
- Evidence of near-complete destruction of C–F bonds **in the measured system**, though carbon fate remains to be resolved.

**Limitations**

- Remaining organofluorine, though smaller, may still be environmentally relevant.
- Off-gas analyses may still be incomplete, especially for volatile organofluorine.

---

### Level 5 – Integrated fluorine and carbon fate (toward mineralization)

**Evidence**

- High-level defluorination plus robust evidence of PFAS-derived carbon mineralization or conversion to non-fluorinated organics with minimal residual fluorine.

**Minimum data**

- Level 4 fluorine accounting, plus:
  - TOC/DOC changes, ideally combined with isotopic or PFAS-specific carbon tracing where feasible.
  - Gas-phase carbon analysis (CO₂, CO, key organics) in thermal or advanced oxidation/reductive treatments.
- Demonstrated absence (or near-absence) of organofluorine in all relevant phases (within detection limits).

**Interpretation**

- “Substantial destruction of PFAS to inorganic fluoride and inorganic carbon, with ≤Z% of initial fluorine and carbon present as organofluorine above detection limits.”  
- This approaches a **mineralization claim**, but final wording must acknowledge:
  - Detection limits,
  - Unmonitored phases,
  - Potential non-fluorinated organic residues.

**Limitations**

- Isotopic or specific carbon attribution is challenging at scale.
- Co-contaminants complicate assigning observed carbon changes to PFAS.

---

### Level 6 – Destruction with toxicity and risk context

**Evidence**

- Level 5 mass balances plus toxicity-related measures.

**Minimum data**

- Acute/chronic toxicity assays (in vitro or in vivo) before and after treatment.
- Bioaccumulation-relevant endpoints for key residuals (if identified).
- For complex matrices, broader chemical screening for non-PFAS toxicants generated by treatment (e.g., disinfection byproducts).

**Interpretation**

- “PFAS treatment leads to substantial conversion to inorganic fluoride and inorganic carbon with reduced mixture toxicity in [bioassays], and no indication of new highly toxic organofluorine products within analytical detection limits.”  
- This recognizes that **environmental and health relevance** is not synonymous with “mass destruction,” and both must be addressed.

**Limitations**

- Bioassays often capture only a subset of endpoints.
- Scale-up may introduce new byproduct pathways not seen in controlled tests.

---

## 5. Preserving technology, matrix, and scale limitations in claims

### 5.1 Technology-specific considerations

Different classes of technologies inherently lend themselves to different maximum evidence levels:

- **Separations (adsorption, membranes, foam fractionation)**:
  - By design, move PFAS between phases without destruction.
  - Appropriate claim: “Removal/separation.”  
  - Additional destruction must be demonstrated in subsequent treatment of the concentrated residuals.

- **Moderate-energy oxidation/reduction (e.g., some AOPs, electrochemical systems, reductive treatments)**:
  - Commonly achieve parent loss and TP formation; partial defluorination possible.
  - Destruction claims should be bounded by measured fluoride release and organofluorine residues.
  - Attention needed for formation of shorter-chain, more mobile PFAAs.

- **High-energy or thermal treatments (e.g., advanced plasma, high-temperature incineration, pyrolysis under specific conditions)**:
  - Potential for high defluorination and carbon oxidation.
  - Require robust off-gas, particulate, and residue characterization; incomplete combustion/destruction can yield problematic volatile or semi-volatile fluorinated species.

### 5.2 Matrix effects

Matrix composition strongly influences both reaction pathways and measurement feasibility:

- **Aqueous matrices with low organic content**:
  - Easier mass balances, fewer co-contaminants.
  - More straightforward assignment of fluoride and TOC changes to PFAS.
- **High-organic or solid-rich matrices (sludges, soils, biosolids, AFFF residues)**:
  - Compete for reactive species.
  - Produce abundant non-PFAS TPs and byproducts that distort TOC and toxicity signals.
  - Extraction and combustion methods for TOF/EOF become less quantitative; solid-phase partitioning more complex.

Thus, **claims must remain matrix-specific**. A technology that achieves near-complete PFAS defluorination in clean water may do far less in real wastes unless demonstrated.

### 5.3 Scale-up limitations

Bench-scale successes may not translate directly to field:

- **Residence times and energy densities**: Often shorter or reduced at scale.
- **Hydrodynamics and mass transfer**: Non-ideal flow, short-circuiting, mixing inefficiencies.
- **Off-gas handling and secondary streams**:
  - Condensers, scrubbers, and filters can reconcentrate or transform PFAS-related species.
  - Scale-up may generate **new residual streams** not present at bench scale.

For scale-up evaluations:

- Multi-phase fluorine and carbon balances must encompass:
  - Feed, treated effluent, solid residues, off-gas, and scrubber/condensate streams.
- Any “destruction efficiency” metric should clearly specify:
  - System boundary (unit operation vs. full train),
  - Analytical coverage,
  - Uncertainties.

---

## 6. Key evidence gaps and future research needs

To more reliably distinguish **disappearance** from **transformation**, **defluorination**, and **destruction**, several areas need advancement:

1. **Improved comprehensive fluorine accounting**
   - Robust, matrix-tolerant TOF/EOF methods with lower detection limits and better phase coverage.
   - Standardized protocols for multi-phase fluorine budgets in treatment systems, including off-gas and fine particulates.

2. **Enhanced structural characterization and quantification of unknown TPs**
   - Systematic non-target/suspect workflows tailored for PFAS treatment studies.
   - Expansion of authentic standards and response-factor libraries for common TPs.
   - Better coverage of ultra-short-chain and highly polar species, as well as volatile organofluorine.

3. **Carbon-fate linkage to PFAS**
   - Methods to attribute TOC/DOC and CO₂ changes specifically to PFAS (e.g., isotopic labelling in representative systems).
   - Differentiating PFAS-derived carbon from co-contaminant carbon in complex matrices.

4. **Integrated toxicity and risk-based endpoints**
   - Routine inclusion of bioassays to understand whether treatment reduces or increases mixture toxicity.
   - Exploration of bioaccumulation and persistence of key TPs.

5. **Standardized reporting framework**
   - Consensus on minimal data sets for each level of evidence (from removal to mineralization).
   - Standard terminology distinguishing:
     - Removal vs. transformation vs. defluorination vs. destruction.
     - Analytical detection limits and phase boundaries for all claims.

6. **Scale-up demonstration studies with full balances**
   - Field- or pilot-scale demonstrations that:
     - Track fluorine and carbon across all outputs.
     - Characterize residual streams (ashes, brines, off-gas, concentrates) for both PFAS and non-PFAS byproducts.
   - Comparative assessments across technologies under realistic operating constraints.

---

## 7. Summary

Disappearance of a monitored PFAS from a given phase is **not** sufficient evidence of its destruction. To meaningfully distinguish among **parent removal**, **transformation**, **defluorination**, and **broader destruction**, studies must combine:

- **Parent and TP analyses** (for pathway insight),
- **Fluoride release and fluorine mass balance** (for C–F bond fate),
- **Carbon and mineralization-related endpoints** (for carbon fate),
- And, ideally, **toxicity-related measures** (for environmental relevance).

Interpretation is tightly constrained by analytical scope, sampling design, detection limits, and the fraction of unresolved products. A tiered evidence hierarchy provides a structured way to align claims with the strength of the underlying data, while preserving explicit recognition of technology, matrix, and scale limitations.

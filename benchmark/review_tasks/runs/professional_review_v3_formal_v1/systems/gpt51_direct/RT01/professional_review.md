## 1. Scope and framing

This review focuses on **how to choose an adsorption medium** (not how to destroy PFAS) for a given:

- PFAS profile (chain length, functional group, precursors)
- Water matrix (drinking water, groundwater, landfill leachate, industrial, wastewater effluent)
- Operating targets (regulatory levels, bed life, residual management)

All conclusions are **conditional** on those factors. No adsorbent is universally best.

---

## 2. PFAS chemistry and adsorption-relevant properties

### 2.1 PFAS structural features that control adsorption

Key PFAS attributes:

1. **Perfluoroalkyl chain length (hydrophobic tail)**
   - Longer chains (e.g., ≥ C7–C8) → more hydrophobic, stronger affinity for nonpolar surfaces (e.g., GAC, hydrophobic resins).
   - Short chains (C3–C6) → more hydrophilic, remain in bulk water, more difficult to adsorb via simple hydrophobic interactions.

2. **Functional group / headgroup**
   - **Perfluoroalkyl carboxylic acids (PFCAs, e.g., PFBA, PFHxA, PFOA)**  
     - Weaker acids than sulfonates; usually anionic at environmental pH.
     - Typically less strongly adsorbed than sulfonates of same chain length on hydrophobic adsorbents.
   - **Perfluoroalkane sulfonic acids (PFSAs, e.g., PFHxS, PFOS)**  
     - Stronger acids; fully anionic across most pH.
     - Usually show higher affinity than analogous PFCAs on many hydrophobic media.
   - **Other anionic species (e.g., GenX-like ether PFCAs)**  
     - Often shorter chain and more polar; poorer adsorption on conventional carbons; may require tailored resins or higher doses/contact times.
   - **Zwitterionic/neutral precursors (e.g., fluorotelomer sulfonamides, sulfonamidoacetic acids)**  
     - Less negative charge; stronger hydrophobic and specific interactions; sometimes adsorb more readily than their fully anionic daughter products.
     - But they may transform downstream to more mobile PFCAs.

3. **Precursor vs terminal PFAS**
   - **Precursors** (often surface-active; can be partially nonpolar) may partition efficiently to hydrophobic adsorbents.
   - **Terminal PFAAs** (e.g., PFOA, PFOS, PFHxA) are non-biodegradable under most adsorber conditions; adsorption simply transfers them to solids or brines.
   - Treatment trains must anticipate **precursor-to-PFAA conversion** (e.g., in biofilters or distribution systems) after adsorption steps.

4. **Ionization state (pH-dependent)**
   - Most environmentally relevant PFAS are anionic across typical waters (pH ~6–8).
   - A few precursors can exist in neutral or cationic forms under some pH; this strongly affects whether **electrostatic attraction or repulsion** dominates.

Engineering implication: media choice should always start from a **PFAS speciation table** (by chain length and headgroup) at the operational pH.

---

## 3. Adsorption mechanisms and material properties

Here the focus is on **separation/adsorption**, not chemical transformation. Adsorption does **not** degrade or destroy PFAS; it relocates them.

### 3.1 Activated carbons (GAC, PAC)

**Dominant mechanisms**

- **Hydrophobic interactions** between fluorinated tail and hydrophobic carbon surface.
- **π–π and dispersion interactions** with graphitic domains.
- **Electrostatic effects**: surface charge of carbon (depends on surface oxidation, pH, and preconditioning) can attract or repel anionic PFAS but is often secondary to hydrophobicity for long-chain species.
- **Pore-filling**: micro- and mesopores fill with PFAS plus water clusters; pore size distribution relative to PFAS molecular size is critical.

**Material properties that matter**

- **Specific surface area and micropore volume**
  - Micropores (sub-2 nm) favor strong adsorption of many organics; for PFAS, overly tight micropores can hinder diffusion, especially for bulky precursors or sulfonates.
- **Mesoporosity (2–50 nm)**
  - Enhances mass transfer; important for short empty bed contact times and high-flow systems.
- **Surface chemistry**
  - Oxidized surfaces are more hydrophilic and can decrease affinity for hydrophobic tails, but may introduce sites for hydrogen bonding with some precursors.
  - Less oxidized, more hydrophobic carbons usually perform better for long-chain PFAS in low-DOC waters.
- **Particle size**
  - PAC: higher kinetics, easier dose adjustment, but generates sludge and is difficult to regenerate in-situ.
  - GAC: fixed beds, regenerable (typically thermally), but kinetics slower; requires carefully designed EBCT.

**PFAS selectivity trends (generalized)**

- Long-chain PFSAs ≳ long-chain PFCAs >> short-chain PFAS.
- Precursors can adsorb strongly but may desorb or transform later if not removed or captured irreversibly.

### 3.2 Ion exchange (IX) resins

**Dominant mechanisms**

- **Electrostatic ion exchange** between negatively charged PFAS and positively charged functional groups (quaternary ammonium or others).
- **Hydrophobic and fluorophilic partitioning** into resin matrix (styrenic/divinylbenzene resins generally more hydrophobic than acrylics).
- **Size-exclusion and steric effects** in resin pores.

**Material properties**

- **Functional group type and density**
  - Strong-base anion resins (quaternary amines) capture anionic PFAS across wide pH.
  - Higher functional group density can increase capacity but also increases competition with other anions.
- **Matrix hydrophobicity**
  - Hydrophobic matrices (styrenic) can enhance sorption of long-chain PFAS and hydrophobic precursors.
  - More hydrophilic matrices may show relatively better performance toward short-chain PFAS (by reducing non-specific organic fouling), but this is highly system-dependent.
- **Porosity / crosslinking**
  - High crosslinking: robust, but smaller pores and slower intraparticle diffusion.
  - Lower crosslinking: faster sorption, but more swelling and potential mechanical issues.

**PFAS selectivity trends**

- Often stronger uptake of **PFSAs over PFCAs**, and long chain over short chain.
- Some tailored resins show improved performance for **short-chain PFCAs and ether-based PFAS**, but performance is very matrix-dependent.
- Resins efficiently capture anionic PFAS even in waters where GAC is challenged by high organic matter; however, they produce a **PFAS-rich brine or spent resin** that requires further management.

### 3.3 Emerging / modified carbonaceous and polymeric adsorbents

Examples (conceptual classes, not specific brands):

- **Surface-modified activated carbons** (e.g., with cationic or fluorophilic coatings)
  - Aim to combine hydrophobic and electrostatic attraction to better capture short-chain anions or specific PFAS families.
- **Fluorinated polymers, porous organic polymers, and tailored micro-/nanoporous materials**
  - Designed to exploit **fluorophilic interactions** (F–F, CF2–CF2 compatibility) and size/shape selectivity.
- **Organoclays and functionalized clays**
  - Surfactant-modified clays can bind PFAS via hydrophobic partitioning into the interlayer surfactant phase; more suited to high-strength or high-solids matrices.

These materials can significantly outperform conventional media for some PFAS/matrix combinations, but data sets are often limited, regeneration behavior is uncertain, and scale-up experience is less mature.

### 3.4 Inorganic sorbents (metal oxides, carbonates, etc.)

- Generally **less selective** for PFAS compared to carbon and IX, except in niche conditions.
- Mechanisms: electrostatic attraction on positively charged surfaces (at low pH), ligand exchange, or co-precipitation.
- Performance is often more sensitive to pH and competing ions; capacity for PFAS typically much lower than for conventional anions (phosphate, nitrate, etc.).

In most municipal PFAS remediation cases, these are secondary or polishing options, not primary PFAS adsorbents.

---

## 4. How water matrix and operating conditions modify PFAS adsorption

The same medium can perform very differently depending on matrix conditions. Below are the dominant modifiers and how they guide selection.

### 4.1 Dissolved organic matter (DOM / DOC)

**Effects on activated carbon**

- **Strong competition**: humic/fulvic substances occupy pores and active sites, especially in micropores.
- **Fouling**:
  - Reduces effective capacity and worsens kinetics for PFAS, particularly short-chain PFAS.
  - Can create a DOM coating that changes surface chemistry, often making it more hydrophilic and negatively charged.
- Implications:
  - In high-DOC waters, GAC may show **rapid breakthrough** of short-chain PFAS even if long-chain PFAS are well controlled.
  - PAC dosing must be much higher and may still be dominated by bulk DOC removal.

**Effects on ion exchange resins**

- **Macromolecular organic fouling**:
  - DOM can sorb to resin surfaces and within pores, blocking sites.
  - Hydrophobic styrenic resins may foul more strongly with hydrophobic DOM than more hydrophilic acrylic resins.
- **Strategies**:
  - Pre-treatment (coagulation, inline filtration) to reduce DOC prior to IX.
  - Periodic cleaning (e.g., high-salt or caustic rinses) to restore capacity.
- IX resins often maintain better **selectivity for PFAS over DOC** than GAC in high-DOC waters, but performance still degrades at high DOC loads.

### 4.2 Inorganic ions: sulfate, chloride, nitrate, bicarbonate, etc.

**For ion exchange**

- PFAS compete with other anions for exchange sites.
- High concentrations of **bicarbonate, sulfate, and other multivalent or strongly sorbing anions** can significantly reduce PFAS capacity and shift breakthrough earlier.
- Design implication:
  - In high-alkalinity or high-sulfate waters, IX bed life for PFAS will usually be **much shorter** than bench tests in simplified matrices suggest.
  - Brine regeneration can concentrate both PFAS and other anions, increasing brine volume and chemical demand.

**For activated carbon**

- Inorganic anions exert weaker direct competition compared to DOM but can influence:
  - PFAS speciation (through ionic strength and double-layer compression).
  - Surface charge and aggregation behavior of DOM.
- High ionic strength can reduce electrostatic repulsion between anionic PFAS and negatively charged surfaces, slightly favoring adsorption; however, this effect is usually secondary compared with DOC competition.

### 4.3 pH

- Most PFAAs are fully deprotonated anions at typical environmental pH.
- pH effects arise via:
  - **Surface charge** of the adsorbent:
    - Lower pH: more positively charged sites on carbons/oxides → stronger electrostatic attraction to anionic PFAS.
    - Higher pH: more negative surfaces → increased electrostatic repulsion; may decrease adsorption, especially for short-chain PFAS.
  - **Ion exchange functional group behavior**:
    - Strong-base resins less sensitive; weak-base or amphoteric media can lose capacity in certain pH ranges.

Engineering implication:

- For **pH ~6–8** (typical drinking water), both carbons and strong-base IX resins can be effective, but pH optimization (if possible) around mildly acidic conditions can sometimes improve performance for short-chain PFAS at the expense of metal solubility and corrosion challenges.
- In very high pH industrial streams, carbon/IX performance may be degraded and may require pH adjustment or pre-treatment.

### 4.4 Competing organic contaminants (e.g., NOM, surfactants, non-fluorinated organics)

- **Surfactants and co-solvents** can drastically change PFAS behavior:
  - Non-fluorinated surfactants may occupy hydrophobic sites and micelles, reducing PFAS adsorption.
  - Organic co-solvents (e.g., in industrial wastewaters) can increase PFAS solubility and reduce partitioning to hydrophobic adsorbents.
- **Co-contaminant removal priorities**:
  - If the same adsorbent must remove VOCs, pesticides, or taste/odor compounds and PFAS, GAC may be chosen for its broad spectrum even if IX would be more selective for PFAS alone.
  - Conversely, if PFAS are the main concern and DOC is moderate-to-high, IX or tailored polymeric media may be preferred to avoid capacity being spent on other organics.

### 4.5 Influent PFAS concentration and mixture composition

- At **very low influent concentrations** (ng/L range):
  - Adsorption is typically in the Henry’s-law/linear isotherm region; **kinetics and breakthrough behavior** determine performance more than ultimate capacity.
  - Strong, selective media (IX, tailored polymers) may show sharp breakthrough curves and longer bed life.
- At **higher PFAS concentrations** (µg/L–mg/L; e.g., landfill leachate, industrial sources):
  - Adsorption isotherms may become nonlinear; capacity and competition effects become critical.
  - GAC, resins, or organoclays may saturate quickly; treatment trains may need staged adsorption, pre-concentration, or alternative primary treatment (e.g., foam fractionation) followed by polishing adsorption.

- For **mixtures with both long- and short-chain PFAS**:
  - Long-chain PFAS often adsorb first and most strongly, potentially occupying sites that would otherwise be available for short-chain PFAS.
  - Bed breakthrough profiles often show:
    - Early breakthrough of short-chain PFAS even when long-chain PFAS remain well controlled.
  - Media that are specifically tuned for short-chain PFAS may still show strong uptake of long-chain PFAS; this can reduce effective bed life for the short-chain targets unless they are treated as the design basis.

---

## 5. Translating evidence into **conditional** media-selection criteria

Below is a practical selection framework by **PFAS profile and matrix**, emphasizing trade-offs, residual streams, and knowledge gaps. No universal ranking is implied.

### 5.1 Step 1 – Define the treatment goal and constraints

- Target PFAS list (by chain length and functionality); especially:
  - Regulatory drivers (e.g., PFOA + PFOS vs. sum of PFAAs vs. “total PFAS”).
  - Need to control short-chain PFAS (PFBA, PFPeA, PFHxA, PFBS, etc.).
- Matrix class:
  - Low-DOC drinking water / groundwater.
  - High-DOC surface water or wastewater effluent.
  - Industrial or landfill leachate (high DOC, high TDS, possibly high PFAS).
- Operational constraints:
  - Available footprint and EBCT.
  - Regeneration capability (on-site vs. off-site vs. single-use/disposal).
  - Residual handling budget and regulatory limitations (spent carbon, spent resin, brine).

### 5.2 Conditional guidance by matrix and PFAS profile

#### Case A: Low-DOC groundwater / drinking water; dominated by long-chain PFAAs

- Typical PFAS profile:
  - Long-chain PFSAs/PFCAs dominate; short-chain PFAS present but not the main regulatory driver.
- Matrix:
  - DOC typically low; inorganic ions at drinking-water levels; pH near neutral.

**Most suitable media (conditional)**

- **GAC (fixed beds)**:
  - Often cost-effective with well-documented performance.
  - Long-chain PFAAs can be reduced to very low levels with reasonable bed lives.
  - Short-chain PFAS will generally break through earlier; if they are not the main compliance driver, this may be acceptable.
  - Residual: spent carbon requiring off-site thermal regeneration or disposal; PFAS are transferred to regeneration off-gas or destruction facility.
- **Strong-base anion exchange resins**:
  - Can achieve longer bed lives and sharper PFAS breakthrough for long-chain PFAAs in many cases.
  - Particularly useful for very low MCLs or for utilities that need small footprint.
  - Residual: PFAS-rich spent resin and/or brine (if regenerated). Brine disposal or PFAS destruction step required.

**Selection trade-offs**

- If **capital/construction footprint** is constrained and short-chain PFAS are of concern, IX may be favored.
- If **simplicity and familiarity** are prioritized and short-chain PFAS are secondary, GAC may be adequate and cheaper.
- If **residual brine disposal** is problematic (e.g., no suitable discharge for high-salinity PFAS waste), GAC with off-site thermal regeneration might be simpler.

#### Case B: High-DOC surface water / wastewater effluent; mixed PFAS including short-chain

- PFAS profile:
  - Significant short-chain PFAS and precursors plus long-chain PFAAs.
- Matrix:
  - High DOC, possible elevated nutrients and other organics, moderate-high TDS.

**Most suitable media (conditional)**

- **Strong-base IX resins (often styrenic or tailored PFAS resins)**:
  - Typically outperform GAC for PFAS under high-DOC conditions, especially for short-chain PFAS, because DOC fouling is less dominant relative to ion-exchange selectivity.
  - Require robust pre-filtration to prevent particulate fouling.
- **Tailored polymeric/fluorophilic adsorbents**:
  - Can outperform conventional IX or GAC for specific PFAS profiles; promising for short-chain PFAS.
  - Scale-up experience and long-term fouling/cleaning behavior still being developed.
- **GAC**:
  - May still be used for pre-treatment DOM removal ahead of IX or advanced polishing.
  - On its own, GAC may struggle with maintaining low short-chain PFAS at high DOC without frequent changeouts.

**Selection trade-offs**

- IX/resin systems:
  - Higher upfront media cost but potentially lower operational cost per volume treated if bed life is long.
  - Residual management (spent resin or brine) becomes a key decision point.
- GAC + IX treatment train:
  - GAC as a **DOC management step** followed by IX for PFAS can balance costs and protect IX from fouling.
  - Increases complexity but may extend IX bed life substantially.

#### Case C: Landfill leachate or industrial streams with very high PFAS and co-contaminants

- PFAS profile:
  - Often contains precursors, long- and short-chain PFAS, and non-fluorinated surfactants; concentrations can be orders of magnitude higher than in drinking water.
- Matrix:
  - Very high DOC, high TDS, extreme pH possible, many competing contaminants.

**Most suitable media (conditional)**

- **Primary separation / pre-treatment before adsorption** often necessary:
  - Foam fractionation, membrane separation, or advanced oxidation (with caution regarding by-product formation) may be used to reduce PFAS load before polishing.
  - Adsorption used as a final polishing step, not the primary capture method for all PFAS mass.
- **Robust adsorbents** like:
  - GAC or organoclays for bulk organic removal and some PFAS removal.
  - Followed by IX or tailored resins for polishing to lower PFAS levels if a strict discharge limit must be met.

**Selection trade-offs**

- Using IX as the **sole primary treatment** for high-strength PFAS waters usually leads to very short bed lives and large volumes of highly contaminated brine.
- Combining **load-reduction technologies** with adsorption allows:
  - Smaller, more manageable adsorption systems.
  - Concentration of PFAS mass into smaller residual streams that can be sent to destruction.

### 5.3 Additional conditional criteria

#### Short-chain PFAS as primary regulatory target

- Favor:
  - Strong-base IX resins optimized for short-chain PFAS.
  - Tailored polymeric/fluorophilic adsorbents with demonstrated short-chain selectivity.
- Avoid relying solely on:
  - Conventional GAC in high-DOC matrices; it often cannot maintain low short-chain concentrations over realistic bed lives.
- Consider:
  - Hybrid systems: GAC for DOC and long-chain PFAS bulk removal, followed by IX for short-chain polishing.

#### High co-anion load (high alkalinity, sulfate, nitrate)

- IX capacity for PFAS will be **strongly affected**.
- In such cases, GAC may compare more favorably than expected if DOC is low/moderate, since GAC is less sensitive to inorganic ions.
- If IX is still preferred:
  - Design should explicitly account for competition using multi-component modeling or pilot data, not single-analyte batch tests.
  - Regeneration frequency and brine generation must be included in lifecycle assessments.

#### Stringent residuals management and PFAS destruction requirements

- **IX with brine regeneration**:
  - Produces concentrated liquid waste; potentially easier to feed into destructive technologies (e.g., advanced reduction or high-energy processes) than bulky solids, but brine composition (salts, organics) can interfere with destruction methods.
- **Single-use GAC / limited regeneration**:
  - Solid-phase PFAS waste may be stabilized but still needs eventual destruction or disposal; off-site thermal regeneration often implicitly becomes the PFAS destruction step.
- When destruction options are limited or uncertain:
  - Media and operating strategies that **minimize overall PFAS mass in residuals** (through pre-concentration, source control, or selective polishing of low-volume side streams) may be preferred over maximizing adsorption capacity alone.

---

## 6. Evidence gaps and practical recommendations for engineers

### 6.1 Evidence gaps

- **PFAS mixture behavior**:
  - Many datasets focus on a small number of legacy PFAS; performance for diverse emerging PFAS (ethers, sulfonamides, ultra-short chains) and precursors is often under-characterized.
- **Long-term fouling and regeneration behavior**:
  - Especially for newer polymeric and fluorophilic adsorbents, data on repeated regeneration, PFAS retention, and by-product formation are limited.
- **Complex matrices**:
  - Landfill leachate, concentrated industrial streams, and advanced-treatment sidestreams require more systematic studies linking matrix composition to adsorbent choice.
- **Coupled process trains**:
  - Few comparative data exist for integrated trains (e.g., GAC + IX, foam fractionation + IX + polishing GAC) optimized around residuals minimization and destruction-readiness.

### 6.2 Practical selection workflow

For an engineer tasked with designing PFAS adsorption:

1. **Characterize the influent**:
   - PFAS speciation: chain-length distribution, functional groups, estimated precursors.
   - Matrix: DOC, UV254, major anions/cations, pH, TDS, surfactants, co-contaminants.
   - PFAS concentration range and expected variability.

2. **Define performance and lifecycle criteria**:
   - Target effluent concentrations for each regulated PFAS.
   - Required reliability (e.g., how much safety factor on breakthrough).
   - Residuals management (solid vs liquid, on- vs off-site destruction).
   - Cost and footprint constraints.

3. **Pre-screen media classes** using conditional guidance:
   - Low DOC, long-chain PFAS dominant → GAC and/or IX both viable; compare lifecycle costs and residuals handling.
   - High DOC, mixed PFAS including short-chain → IX or tailored polymeric media as primary PFAS adsorbent; GAC as DOC pre-treatment.
   - High-strength, complex wastewaters → pre-concentration/separation plus adsorption polishing.

4. **Pilot testing under realistic conditions**:
   - Use representative influent (including DOC and competing ions).
   - Monitor full PFAS suite and mixture behavior, not just one or two analytes.
   - Evaluate breakthrough curves for short- and long-chain PFAS separately.

5. **Design for adaptability**:
   - Allow for media change or train reconfiguration as regulations expand to new PFAS.
   - Include ports for intermediate sampling and modular media beds.

6. **Integrate adsorption with destruction strategy**:
   - Select adsorbent and regeneration approach that yields a residual stream (spent media or brine) compatible with available destruction technologies.
   - Ensure that claims of “PFAS treatment” are correctly understood as **separation/transfer** in the adsorption step, followed by a distinct **destruction process** where applicable.

---

## 7. Concluding perspective

Selecting a PFAS adsorption medium is inherently **situation-specific**. The main determinants are:

- PFAS mixture (especially short- vs long-chain, sulfonate vs carboxylate, and presence of precursors),
- Matrix composition (DOM, inorganic ions, co-contaminants, pH),
- Operational context (target levels, footprint, cost, and residual management).

Within that context:

- **GAC** tends to be favorable when DOC is modest, long-chain legacy PFAS dominate, and utilities value established practice and solid-phase residual handling.
- **Ion exchange and tailored polymeric adsorbents** become increasingly advantageous as:
  - DOC and competing organics increase,
  - short-chain PFAS and emerging PFAS become primary regulatory drivers,
  - space is limited and sharp breakthrough behavior is critical.

Engineers should avoid seeking a universal “best” adsorbent and instead apply a **matrix- and PFAS-specific decision framework**, supported by targeted pilot testing and an explicit plan for managing PFAS-laden residuals and subsequent destruction.

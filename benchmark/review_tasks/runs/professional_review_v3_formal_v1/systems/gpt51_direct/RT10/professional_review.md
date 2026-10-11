## 1. Scope and Key Distinctions

Translation of PFAS treatment performance from clean laboratory water to real water requires explicit handling of *matrix effects*. These effects depend on:

- PFAS structure (chain length, head group, precursor vs terminal, zwitterionic/neutral vs anionic, branched vs linear).
- Treatment mechanism (physical separation vs chemical/electrochemical/thermal degradation).
- Concentration and speciation of organic matter, surfactants, inorganic ions, and other co-solutes.

Two conceptual points must be explicit throughout:

1. **Removal vs destruction**
   - **Physical separation** (adsorption, ion exchange, membranes, foam fractionation, precipitation) moves PFAS to another phase; it does *not* destroy PFAS.
   - **Transformation/degradation** changes parent molecules; **defluorination** releases F⁻; **mineralization** requires evidence for conversion of carbon to inorganic forms (e.g., CO₂), not just F⁻ release.
2. **Matrix effects are not universal**
   - No single matrix constituent (e.g., NOM, chloride) has a universally inhibitory or promotive effect across all PFAS and all treatment technologies.
   - Effects change with concentration, PFAS identity, pH/ionic strength, and operational conditions.

The review below is structured around (i) how different matrix components influence processes, (ii) how to conceptualize inhibitory/promotive/interactive effects, and (iii) a minimum framework for matrix characterization and matched controls.

---

## 2. How Matrix Components Affect PFAS Physical Separation and Degradation

### 2.1 Natural Organic Matter (NOM) and Other Dissolved Organic Matter (DOM)

#### 2.1.1 Impacts on Physical Separation

**Adsorption and ion exchange**

- **Competitive adsorption / site blocking (usually inhibitory)**
  - NOM typically has a broad distribution of hydrophobic, aromatic, and charged moieties that can occupy adsorption sites on activated carbon, polymer resins, and ion exchangers.
  - For many anionic PFAS, especially long-chain perfluoroalkyl sulfonates and carboxylates, NOM can:
    - Reduce apparent PFAS adsorption capacity and rate.
    - Shorten breakthrough times in column systems.
  - Extent depends strongly on:
    - NOM concentration and composition (aromaticity, charge density).
    - PFAS hydrophobicity and head-group charge.
    - Adsorbent surface chemistry (e.g., hydrophobic vs more polar, macroporous vs microporous).

- **Electrostatic and hydrophobic conditioning (inhibitory, neutral, or occasionally promotive)**
  - NOM adsorption on sorbent surfaces can:
    - Make surfaces more negatively charged → increased electrostatic repulsion with anionic PFAS (inhibitory).
    - Create a softer, more hydrophobic organic film that may retain hydrophobic PFAS (partially compensatory or even slightly promotive for certain PFAS).
  - These opposing mechanisms can yield net neutral effects at moderate NOM levels; strong inhibition tends to appear at higher NOM loadings or on sorbents with limited capacity.

**Membranes (nanofiltration, reverse osmosis, ultrafiltration)**

- **Fouling layer effects**
  - NOM causes fouling that:
    - Decreases flux.
    - Modifies membrane surface charge and hydrophobicity.
  - For PFAS:
    - Fouling can **inhibit** separation by increasing PFAS passage due to pore plugging by NOM and altered electrostatic screening, or
    - **Enhance apparent rejection** when a dense fouling cake forms, adding an additional barrier for PFAS.
  - The net effect depends on:
    - NOM type (highly humic vs more hydrophilic).
    - PFAS size and charge.
    - Pressure, crossflow conditions, and ionic strength.

- **Colloidal PFAS–NOM associations**
  - PFAS may associate with NOM macromolecules or colloids; these aggregates may be more easily rejected by membranes.
  - Conversely, if PFAS partition into dissolved NOM “micelle-like” domains, they may be transported through some membranes differently than free PFAS.

**Foam fractionation / air-based separations**

- NOM can:
  - Compete for the air–water interface.
  - Modify bubble surface properties.
- This can **inhibit** PFAS enrichment in foam (by occupying interfacial area) or, if NOM forms complexes with PFAS that remain surface-active, lead to complex, non-monotonic effects.

#### 2.1.2 Impacts on Degradation Processes

**Radical-based advanced oxidation (e.g., UV/H₂O₂, sulfate radicals, ozone-based AOPs)**

- **Scavenging of reactive species (typically inhibitory)**
  - NOM competes with PFAS for hydroxyl and other radicals.
  - Because most PFAS have low second-order rate constants with •OH, radical scavenging by NOM generally reduces PFAS transformation unless treatment conditions are extreme.
- **Light screening (inhibitory)**
  - Absorbing NOM attenuates UV or visible light, reducing photon flux for photolytic or photocatalytic processes.
- **Photosensitization and reactive intermediates (can be promotive for some pathways)**
  - NOM can generate reactive intermediates (e.g., triplet states, singlet oxygen) under irradiation, which might transform some PFAS precursors or co-contaminants but typically show limited direct reactivity with perfluoroalkyl acids.

**Electrochemical oxidation**

- NOM can:
  - Compete for oxidative capacity at the anode.
  - Form passivating layers on electrodes.
  - Generate intermediates that may change solution pH or redox, indirectly altering PFAS degradation.
- The balance of competition vs synergistic effects (e.g., generation of oxidants like free chlorine from chloride in the presence of NOM) is highly system-specific.

**Reductive processes (e.g., sulfite/UV, hydrated electrons, reductive electrochemistry)**

- NOM often **scavenges reducing species** (e.g., hydrated electrons), reducing PFAS defluorination efficiency.
- However, interactions are nuanced and depend on:
  - NOM redox activity.
  - PFAS structure (precursors vs terminal PFAS; aryl vs aliphatic PFAS).
  - Electron donor/acceptor chemistry.

**Thermal processes (incineration, pyrolysis, supercritical water)**

- In aqueous thermal processes (e.g., hydrothermal, supercritical water), DOM can:
  - Affect solution pH and ionic strength as it degrades.
  - Generate radicals at high temperature that might assist PFAS transformation.
- Evidence is limited, and predicting net effects without experiment is not reliable.

---

### 2.2 Surfactants and Co-surfactants

This includes synthetic detergents, biosurfactants, and other amphiphilic organics.

#### 2.2.1 Effects on Physical Separation

**Adsorption and ion exchange**

- **Competition for hydrophobic domains (often inhibitory)**
  - Non-fluorinated surfactants can outcompete PFAS for hydrophobic sites due to higher concentrations and stronger non-specific interactions.
- **Micelle formation and solubilization (inhibitory for many PFAS)**
  - Above critical micelle concentration (CMC), surfactants can solubilize PFAS inside micelles, reducing the effective free PFAS concentration available for adsorption or ion exchange.
- **Electrostatic screening and co-adsorption (interactive)**
  - Cationic surfactants may neutralize negative surface charges, reducing electrostatic repulsion for anionic PFAS (potentially promotive).
  - Anionic surfactants may enhance repulsion of anionic PFAS (inhibitory).
  - Zwitterionic surfactants may form mixed aggregates with PFAS, altering partitioning in complicated ways.

**Membranes**

- Surfactants:
  - Promote membrane fouling and pore blocking.
  - Change membrane surface charge and wetting behavior.
- Effects on PFAS rejection can be:
  - **Inhibitory** if surfactants increase PFAS passage via micellar transport or disrupt the rejection layer.
  - **Promotive** if a fouling layer forms that strongly retains surfactants and associated PFAS.

**Foam fractionation**

- Surfactants directly compete with PFAS for interfacial sites:
  - High-concentration non-fluorinated surfactants can dominate foam, diluting PFAS in the concentrate and reducing separation efficiency.
  - Under some conditions, mixed surfactant–PFAS films may still allow effective PFAS enrichment, but with altered selectivity across PFAS types.

#### 2.2.2 Effects on Degradation

**Radical-based and photochemical processes**

- Surfactants can:
  - Be strong radical scavengers or radical precursors, diverting oxidizing capacity away from PFAS (often inhibitory).
  - Alter PFAS microenvironment by micellization: PFAS inside micelles may be somewhat shielded from oxidants or located preferentially at interfaces where radical generation is higher.
- For short-chain PFAS with high water solubility, micellar effects may be weaker than for more hydrophobic PFAS.

**Electrochemical and thermal processes**

- Surfactants:
  - Increase organic loading, promoting competing oxidation and electrode fouling.
  - Can degrade to form smaller organic acids that consume oxidants or reducing species.
- Under some conditions, the breakdown of surfactants may produce intermediates that adjust pH or ionic strength in ways that change PFAS reaction pathways.

---

### 2.3 Inorganic Ions (Major Anions and Cations, Ionic Strength, Hardness)

#### 2.3.1 Effects on Physical Separation

**Electrostatic screening**

- Increased ionic strength (Na⁺, Cl⁻, etc.) compresses the electrical double layer:
  - This can **reduce electrostatic repulsion** between negatively charged sorbents/membranes and anionic PFAS → potentially *promoting* adsorption or membrane retention for some PFAS.
  - Conversely, it can also reduce attractive electrostatic interactions where present (e.g., cationic sorbents with anionic PFAS).
- The net effect is strongly dependent on:
  - PFAS charge state (e.g., sulfonates/carboxylates vs zwitterions/neutral).
  - Sorbent or membrane charge.
  - Ionic strength and specific ion effects.

**Specific complexation and cation bridging**

- Multivalent cations (Ca²⁺, Mg²⁺, Al³⁺, Fe³⁺) can:
  - Form bridges between negatively charged PFAS and surfaces, promoting adsorption or co-precipitation under some conditions.
  - Interact with NOM to form complexes that indirectly change PFAS partitioning (e.g., PFAS–NOM–metal clusters).

**Scaling and fouling**

- Hardness ions contribute to scaling on membranes and electrodes, which:
  - Can decrease flux and alter surface properties.
  - May create additional filtration layers that change PFAS rejection (either promoting or inhibiting).

#### 2.3.2 Effects on Degradation

**Radical generation and scavenging**

- Certain anions (chloride, bicarbonate, carbonate, nitrate, sulfate) influence radical chemistry:
  - Chloride, bicarbonate, carbonate can scavenge •OH and form less reactive radical species, often **inhibiting** PFAS transformation by nonselective radicals.
  - Sulfate can be precursor to sulfate radicals under some AOP conditions, potentially enhancing oxidative capacity.
- At high chloride, formation of free chlorine and reactive chlorine species can occur under UV or electrochemical conditions, which may:
  - Promote degradation of some PFAS precursors and co-contaminants.
  - Only modestly affect terminal perfluoroalkyl acids.

**pH and speciation**

- pH affects:
  - PFAS ionization (for certain functional groups and precursors).
  - Catalyst surface charge (e.g., for photocatalysts).
  - Relative production of different reactive species (e.g., HO₂• vs O₂•⁻).
- Buffer ions (phosphate, borate, carbonate) can both control pH and participate in radical chemistry, complicating extrapolation from buffered lab waters to natural waters.

**Electrochemical processes**

- Conductivity is critical; supporting electrolytes (e.g., Na₂SO₄, NaCl) are often added in lab studies:
  - These can significantly alter oxidant generation and side reactions compared to natural waters.
  - Chloride-containing supporting electrolytes may generate active chlorine, confounding mechanisms and making uncorrected extrapolation to chloride-poor waters unreliable.

**Reductive systems**

- Some anions (e.g., nitrate, oxygen) compete for electrons or reactive reducing species, **inhibiting** PFAS reduction.
- Metal ions can also:
  - Catalyze or inhibit redox processes.
  - Change the speciation of electron donors or acceptors.

---

### 2.4 Other Co-solutes and Co-contaminants

Examples: co-occurring organic micropollutants, bulk co-solvents (e.g., ethanol, methanol for lab dosing), industrial organics, dissolved gases.

#### 2.4.1 Physical Separation

- **Organic co-solvents (methanol, ethanol, acetonitrile)**
  - Added in lab experiments for PFAS stock preparation can:
    - Change PFAS sorption behavior (generally reducing adsorption by increasing solution organic content and altering PFAS hydrophobicity).
    - Affect foam fractionation by suppressing surface tension and altering interfacial partitioning.
- **Co-contaminant organics**
  - Pharmaceuticals, pesticides, hydrocarbons can:
    - Compete with PFAS for adsorption sites.
    - Modify fouling layers on membranes.
    - Influence NOM aggregation and thus PFAS partitioning.

#### 2.4.2 Degradation

- **Co-oxidant and co-reductant demand**
  - Co-contaminants often react faster with oxidants or reductants than PFAS:
    - They can dominate chemical demand, substantially lowering PFAS transformation rates unless oxidant doses are very high.
- **Radical generation/consumption**
  - Certain organics can promote radical production (e.g., acting as photosensitizers) or quench radicals.
- **Toxicity and transformation products**
  - Co-contaminants can form transformation products that:
    - Interfere with PFAS measurement.
    - Change toxicity, complicating attribution of toxicity changes to PFAS vs other components.

---

## 3. Classifying Matrix Effects: Inhibitory, Promotive, Neutral, Interactive

To interpret and report matrix effects in a way that can be generalized, the impact on PFAS behavior should be linked explicitly to:

- **Treatment mechanism** (e.g., hydrophobic adsorption, ion exchange, size exclusion, electrochemical oxidation, radical oxidation, reductive defluorination).
- **PFAS properties** (chain length, head-group functionality, charge state, precursor vs terminal, volatility).

### 3.1 Definitions

- **Inhibitory effect**: Matrix constituent decreases PFAS removal or destruction under fixed operating conditions (e.g., lower PFAS adsorption capacity or flux-normalized removal; lower degradation rate or extent).
- **Promotive effect**: Matrix constituent increases PFAS removal or destruction (e.g., enhanced adsorption or rejection; faster or more complete degradation).
- **Neutral effect**: Changes in matrix constituent concentration do not produce statistically or practically significant changes in performance.
- **Interactive effect**: Multiple constituents together produce non-additive effects (synergistic or antagonistic), or the effect of one depends on the level of another or on PFAS structure.

### 3.2 Relating Effects to Mechanisms and PFAS Properties

**Examples of mechanistic trends (not universal rules):**

- **Long-chain, hydrophobic PFAS (e.g., longer perfluoroalkyl sulfonates)**
  - Typically more sensitive to:
    - NOM and surfactant competition on hydrophobic sorbents (often inhibitory).
    - Micellar partitioning (which can reduce adsorption but may influence foam fractionation in complex ways).
- **Short-chain PFAS**
  - Less hydrophobic; adsorption often weaker:
    - High ionic strength and cation bridging can be relatively more important.
    - Separation through size exclusion and electrostatic interactions may dominate membrane behavior.
- **Precursors vs terminal PFAS**
  - Precursors may be more reactive in AOPs and redox systems.
  - Matrix components that enhance non-selective oxidation might strongly affect precursors while leaving terminal acids largely unchanged.
- **Zwitterionic or neutral PFAS (e.g., some fluorotelomer-based species)**
  - Sensitive to pH and ionic strength for speciation and charge.
  - Matrix effects on adsorption and membrane interactions may differ from those for strongly anionic PFAS.

Interpretation should rely on:

- Changes in PFAS-specific performance metrics (e.g., isotherm parameters, breakthrough curves, rate constants).
- Diagnostic measurements (e.g., zeta potential, radical probe compounds, fluorescence for NOM, surface tension, bubble size distribution) to clarify mechanisms.

---

## 4. Recommended Minimum Framework for Matrix Characterization and Matched-Control Design

To make PFAS treatment data more translatable and comparable, matrix effects should be handled with a standardized experimental and reporting framework.

### 4.1 Minimum Matrix Characterization

At a minimum, for each water tested, report:

1. **Bulk organic parameters**
   - Dissolved organic carbon (DOC) or total organic carbon (TOC).
   - UV₂₅₄ absorbance and specific UV absorbance (SUVA) if possible, as a proxy for NOM aromaticity.
   - Qualitative description of NOM source/type if known (e.g., wastewater effluent, surface water, landfill leachate, industrial).

2. **Major inorganic chemistry**
   - pH.
   - Conductivity or ionic strength.
   - Alkalinity (as CaCO₃).
   - Hardness (Ca²⁺, Mg²⁺).
   - Major anions (Cl⁻, SO₄²⁻, NO₃⁻, HCO₃⁻/CO₃²⁻).
   - Major cations (Na⁺, K⁺, Ca²⁺, Mg²⁺).
   - Presence/approximate levels of redox-active ions (Fe²⁺/Fe³⁺, Mn, etc.), if relevant to the treatment.

3. **Surfactants and surface-active materials**
   - A measure such as methylene blue active substances (MBAS), or other anionic/cationic surfactant proxies where surfactants are expected.
   - If direct surfactant data are not available, qualitative description (e.g., industrial detergent use, firefighting foam contamination).

4. **Physical parameters**
   - Temperature during treatment.
   - Turbidity and suspended solids where relevant to filtration or adsorption processes.
   - Basic particle size distribution for waters heavily impacted by colloids.

5. **PFAS characterization**
   - Initial concentrations of target PFAS, including:
     - A range of chain lengths.
     - Distinct head groups (carboxylates, sulfonates, others as applicable).
     - Precursors if studied.
   - When possible, total organofluorine metrics (e.g., extractable organofluorine) to help contextualize measured analytes.

This level of detail is generally feasible and essential for interpreting matrix effects.

### 4.2 Matched-Control Experimental Design

To allow defensible cross-study comparison and translation, each treatment evaluation should incorporate:

#### 4.2.1 Tiered Matrix Approach

1. **Baseline “clean water” matrix**
   - Ultrapure water or simple buffered solution with:
     - Known ionic strength and pH.
     - Minimal organic content.
   - Purpose: establish intrinsic treatment performance and mechanisms.

2. **Stepwise complexity matrices (synthetic)**
   - Start with clean matrix and add one group of constituents at environmentally relevant concentrations, e.g.:
     - + NOM (e.g., humic-like or representative NOM extract).
     - + Major ions (at levels approximating natural waters).
     - + Surfactants (if realistic for intended application).
   - Purpose: quantify isolated and combined effects under controlled, known composition.

3. **Real water matrices**
   - Surface water, groundwater, wastewater, landfill leachate, AFFF-impacted water, etc., with full characterization as above.
   - Purpose: validate performance under realistic conditions and identify interactions not captured by synthetic matrices.

Crucially, **PFAS composition and initial concentration should be matched** across matrices as closely as possible, or differences should be explicitly accounted for (e.g., normalized to initial PFAS mass).

#### 4.2.2 Controlled Process Conditions

- Keep process variables (dose, contact time, flux, current density, light intensity, temperature) identical when comparing different matrices.
- Include **matrix-only controls** (without PFAS spiking) where background PFAS may be present, to correct for initial concentrations.

#### 4.2.3 Distinguishing Removal from Transformation

For each condition:

- Measure PFAS in:
  - **Influent and effluent** (aqueous phase).
  - **Separated phases** (e.g., spent adsorbent, membrane concentrate, foam, sludge) to the extent feasible.
- For degradation-focused technologies:
  - Track **parent compound loss** and, where analytical capability exists:
    - Transformation products.
    - Fluoride release.
    - Changes in total organofluorine.
  - Do not equate fluoride release with mineralization without carbon fate information.

Separation-focused tests should clearly label performance as **capture/sequestration** and, where relevant, discuss the composition and volume of the residual waste stream.

#### 4.2.4 Quantifying Matrix Effects

Define and report metrics that clearly show matrix impacts, for example:

- Relative change in removal efficiency or capacity, e.g.:
  - Percent change in equilibrium adsorption capacity compared to clean water.
  - Shift in breakthrough volume or time.
- Change in kinetic parameters:
  - Apparent rate constants normalized by PFAS concentration.
  - Half-lives or time to achieve given removal fraction.
- For AOPs/electrochemical/redox:
  - Oxidant or electron demand (e.g., oxidant consumption) in different matrices.
  - Radical probe-based assessments of radical availability.

Report both **absolute performance values** (e.g., capacity, rejection, rate constants) and **relative matrix effects** (% inhibition or promotion) so that results can be rescaled to different technologies and contexts.

---

## 5. Practical Trade-offs, Residual Streams, and Scale-Up Considerations

### 5.1 Trade-offs Introduced by Matrix Constituents

- **NOM and surfactants**:
  - Often reduce effective PFAS removal or destruction efficiency.
  - Increase by-product formation, residual organic load in concentrates or spent media.
  - May require pre-treatment (e.g., NOM removal) that itself generates secondary wastes.

- **Inorganic ions**:
  - Improve conductivity for electrochemical systems but can drive formation of secondary oxidants (e.g., active chlorine) with distinct safety and by-product concerns.
  - Cause scaling on membranes/electrodes, raising maintenance requirements.

- **Complex co-contaminant mixtures**:
  - Increase oxidant demand and residuals management complexity.
  - May produce transformation products with unknown or higher toxicity.

### 5.2 Residual Streams

Every physical separation step yields a **concentrate**:

- Spent adsorbents or resins loaded with PFAS and co-adsorbed organics/inorganics.
- Brine from ion exchange regenerants.
- Membrane concentrates containing PFAS, NOM, salts, surfactants, and other pollutants.
- Foam concentrates from foam fractionation.

Matrix constituents heavily influence:

- The **volume** and **composition** of these residuals.
- Subsequent treatability (e.g., high NOM and surfactant loads can hinder thermal or electrochemical PFAS destruction).

Matrix-characterization and matched-controls should therefore extend, where possible, to residual streams, not only treated water.

---

## 6. Evidence Gaps and Priority Future Research

To make matrix effects on PFAS treatment performance more predictable and translatable, research should prioritize:

1. **Systematic, mechanism-based studies across PFAS classes**
   - Long- vs short-chain, sulfonates vs carboxylates, precursors vs terminal PFAS, zwitterions/neutral PFAS.
   - In controlled synthetic matrices and well-characterized real waters, using matched PFAS mixtures.

2. **Structure–property–matrix relationships**
   - Quantitative relationships linking PFAS physicochemical properties (e.g., pK_a for precursors, hydrophobicity metrics, molecular volume) and matrix descriptors (e.g., DOC, SUVA, ionic strength, MBAS) to:
     - Adsorption capacity/selectivity.
     - Membrane rejection and fouling behavior.
     - Degradation kinetics and defluorination extents.

3. **Role of specific NOM and surfactant chemistries**
   - Beyond bulk DOC and MBAS, better molecular-level characterization of organics (e.g., hydrophobic vs hydrophilic fractions, surfactant classes) to disentangle “NOM” as a heterogeneous entity.

4. **Matrix impacts on transformation products and toxicity**
   - Systematic tracking of:
     - PFAS transformation pathways in complex matrices.
     - The effect of co-solutes on transformation product formation and persistence.
     - Changes in mixture toxicity, not just parent PFAS removal or defluorination.

5. **Predictive modeling tools**
   - Models that incorporate matrix parameters and mechanistic understanding (e.g., competitive adsorption models; radical balance models; electrochemical kinetic models) to forecast real-water performance based on lab data.

---

## 7. Summary: Key Recommendations for Testing and Reporting Matrix Effects

- **Do not assume** that clean-water performance translates to real-water performance without explicit matrix characterization and matched-control experiments.
- **Explicitly distinguish**:
  - Physical separation (capture, concentration) from chemical transformation or destruction.
  - Parent PFAS removal, transformation, defluorination, mineralization, and toxicity changes.
- **Characterize matrices minimally but sufficiently**:
  - DOC/TOC, UV₂₅₄/SUVA, major ions, pH, alkalinity, hardness, conductivity, turbidity, surfactant proxies, and PFAS composition.
- **Use a tiered matrix strategy**:
  - Clean → synthetic with controlled additions → real waters, with matched PFAS and process conditions.
- **Quantify and report matrix effects as relative changes** in clearly defined metrics (capacity, rejection, rates, oxidant demand), and tie them mechanistically to PFAS properties and treatment processes.
- **Consider residual streams explicitly**:
  - Matrix components strongly affect the nature and treatability of PFAS-rich residuals; this must be part of performance assessment.

Following this framework will make PFAS treatment studies more comparable, help avoid overgeneralization from clean-water data, and support more reliable design and scale-up of treatment systems for complex, real-world waters.

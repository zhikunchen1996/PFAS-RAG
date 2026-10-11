## 1. Scope and terminology

This review focuses on *adsorptive removal* of PFAS from water and the translation of laboratory batch data to fixed-bed columns, pilot systems, and full-scale treatment. To keep concepts clear:

- **Removal / separation**: Decrease in dissolved PFAS concentration via transfer to a solid phase (e.g., GAC, ion-exchange resin). PFAS mass remains in the system.
- **Adsorption capacity**: Mass of PFAS taken up per mass of media (e.g., mg/g), typically reported at equilibrium.
- **Kinetics**: Rate at which PFAS mass is transferred from water to media.
- **Breakthrough**: Point at which PFAS concentration in the effluent exceeds a defined fraction of influent or a regulatory/performance target.
- **Service life / media lifetime**: Volume or time treated before adsorbent changeout or regeneration is required, conditional on a chosen breakthrough criterion.
- **Destruction / defluorination / mineralization**: Not the focus here; adsorption simply relocates PFAS to a residual solid stream.

The central question is: **When do batch adsorption results reliably inform column or scale-up performance for PFAS, and when do they not?**  

---

## 2. What different performance metrics actually tell you

### 2.1 Equilibrium capacity (isotherms)

Batch equilibrium tests (often modeled with Langmuir/Freundlich isotherms):

- **Information provided**
  - Relative *affinity* and *maximum loading* of different PFAS on an adsorbent under specific conditions (pH, ionic strength, competing solutes).
  - Rough ranking of adsorbents and qualitative selectivity patterns (e.g., long-chain vs short-chain, sulfonates vs carboxylates).
  - Thermodynamic limits: how much PFAS could be stored in the media if all relevant kinetics and mass transfer resistances were overcome.

- **What it does *not* provide**
  - **No direct prediction of column breakthrough time or media lifetime.**
  - No accounting for flow, hydrodynamics, film/pore diffusion, channeling, or mass transfer zone development.
  - No inclusion of influent variability or concentration history.

**Appropriate use:** Screening feasible media, understanding competitive sorption trends, building inputs for mechanistic column models that are later validated with experimental breakthrough data.

**Inappropriate use:** Claiming that an adsorbent with higher equilibrium capacity *will* yield longer bed life or fewer bed volumes in the field, without column evidence and explicit hydraulic assumptions.

---

### 2.2 Batch kinetics

Short-term batch kinetic tests (e.g., pseudo-first-order/pseudo-second-order fits):

- **Information provided**
  - Approximate intrinsic adsorption rate and the role of film vs intraparticle diffusion under well-mixed, small-scale conditions.
  - Qualitative time scales to approach a fraction of equilibrium under the test’s mixing and concentration conditions.
  - Relative comparison of “fast vs slow” media under *batch* mass transfer regimes.

- **What it does *not* provide**
  - Direct equivalence to hydraulic contact times in packed beds. A “fast” batch kinetic response does not directly guarantee sharp breakthrough or long service life at a given EBCT.
  - No representation of flow-induced gradients, incomplete mixing, or non-ideal hydrodynamics, which strongly affect fixed-bed performance.

**Appropriate use:**  
Determining whether adsorption is likely to be kinetically limited at practical EBCTs, and selecting candidate media/conditions worth column testing.

**Inappropriate use:**  
Treating the time to reach a certain batch removal percentage as a direct substitute for EBCT, or using pseudo-kinetic rate constants as standalone evidence of column lifecycle.

---

### 2.3 Fixed-bed breakthrough curves

Column tests (lab or pilot) producing breakthrough curves (C/C₀ vs. bed volumes or time):

- **Information provided**
  - Integrated performance under realistic *flow + packing* conditions: advection, dispersion, film and intraparticle transfer, and competitive adsorption.
  - Evolution of effluent concentrations, allowing definition of:
    - Initial breakthrough (e.g., 1–10% C/C₀),
    - Regulatory or design breakthrough (e.g., below a health advisory limit),
    - Exhaustion or near-equilibrium operation.
  - Bed volumes treated (BV) to any chosen breakthrough criterion.

- **Value relative to batch**
  - Captures **mass transfer zone (MTZ)** development, which determines how much of the bed is effectively used before the outlet concentration rises.
  - Translates equilibrium capacity into *usable capacity at a specified EBCT and flow regime*.  
    Two adsorbents can have similar equilibrium capacities but very different MTZ lengths and hence very different usable bed life.

- **Limitations**
  - Small lab columns may not capture full-scale hydrodynamic issues (short-circuiting, non-uniform distribution).
  - Usually tested with controlled influent quality; field variability may be under-represented.

**Appropriate use:**  
Primary basis, when combined with representative water matrices, to estimate field performance and to calibrate mechanistic models.

---

### 2.4 Bed volumes treated

“Bed volumes treated” to a stated breakthrough criterion (e.g., number of empty bed volumes processed until effluent exceeds a given threshold):

- **Information provided**
  - Normalized measure of service potential, independent of physical column size, assuming similar EBCT and hydrodynamics.
  - Intuitive scale-up parameter: multiply BV by actual bed volume to estimate total treated volume.

- **Caveats**
  - Highly sensitive to:
    - Breakthrough definition (e.g., 1% vs 50% vs a health-based concentration),
    - EBCT and flow distribution,
    - Influent PFAS profile and concentration dynamics.
  - Cannot be compared across studies without harmonizing these variables.

**Appropriate use:**  
Comparing adsorbents or conditions tested in the *same* system, under similar EBCT, influent, and breakthrough criteria, or as an output of validated column modeling.

---

### 2.5 Media lifetime

Media lifetime (time or volume treated before changeout/regeneration):

- **Information provided**
  - A directly actionable design quantity, provided it is clearly anchored to:
    - A target effluent concentration or C/C₀ threshold,
    - Defined influent conditions (distribution of PFAS, concentration statistics, co-contaminants),
    - Operating EBCT and flow distribution.

- **Dependencies**
  - For PFAS, lifetime is **PFAS-specific**:
    - Long-chain PFAS may saturate earlier but also may be easier to remove to very low effluent levels.
    - Short-chain PFAS often break through earlier for the same EBCT and bed, even when long-chain species remain controlled.
  - Competing sorbates (DOM, NOM, other organics, inorganic ions, co-contaminant organics) may reduce PFAS effective capacity over time.

- **Misuse to avoid**
  - Quoting a single “media life” without:  
    PFAS mixture description, influent variation, EBCT, breakthrough definition, or co-contaminant loads.  
  - Extrapolating pilot media life linearly to full-scale while ignoring hydrodynamics and influent differences.

---

## 3. When batch adsorption does and does not translate to column or field performance

### 3.1 Cases where batch results can be informative

Batch tests can **usefully inform** column design and performance expectations under these conditions:

1. **Same water matrix and PFAS mixture**
   - Batch tests conducted with *actual* site water, not just clean synthetic solutions.
   - Major competitive constituents (DOC, bicarbonate, sulfate, other organics) present at realistic levels.
   - PFAS mixture (chain-lengths, functional groups) representative of the target application.

2. **Consistent concentration ranges**
   - Equilibrium capacities determined in concentration ranges near expected operating conditions.  
   - If column influent PFAS concentrations are much lower than batch test levels, extrapolation of isotherms to low concentrations introduces uncertainty.

3. **Kinetic adequacy confirmed**
   - Batch kinetics show that near-equilibrium can be reached at timescales shorter than or comparable to planned EBCTs, indicating that the material is not strongly diffusion-limited for target PFAS.

4. **Use for mechanistic model input, not final claims**
   - Isotherm and kinetic parameters serve as inputs to validated column models (e.g., incorporating film and intraparticle diffusion) whose predictions are then checked against at least some breakthrough data in columns or pilots.

Under these conditions, batch data can:

- Narrow the set of adsorbents worth pilot testing.
- Indicate risk of poor performance for short-chain or branched PFAS.
- Provide bounding estimates of maximum achievable capacity that constrain design expectations.

However, **batch results alone are still insufficient** to claim field service life or guaranteed breakthrough behavior.

---

### 3.2 Cases where batch results fail to predict column or field behavior

Batch tests are typically **poor predictors** of column/pilot/full-scale performance when:

1. **Hydraulic and mass transfer conditions differ significantly**
   - High mixing in batch jars vs. laminar or non-uniform flow in packed beds.
   - Short-circuiting or unequal flow distribution in full-scale vessels.
   - Scale-dependent dispersion and channeling that are absent in well-mixed batch systems.

2. **PFAS mixture complexity and concentration dynamics are not represented**
   - Batch isotherms measured for single PFAS species, or simple binary mixtures, while real waters contain dozens of PFAS and unknown precursors.
   - Variable influent PFAS concentrations (seasonal, operational changes) leading to changes in driving force and adsorption front shape that batch tests do not reproduce.

3. **Competing sorbates are ignored or underrepresented**
   - Clean water batch tests do not capture competition from DOM/NOM or co-occurring organics (e.g., natural hydrocarbons, co-contaminant pesticides, solvents).
   - Presence of inorganic ions that affect electrostatic interactions and PFAS speciation (e.g., ionic strength, pH, divalent cations).
   - Progressive fouling or pore-blocking effects that accumulate over months/years and reduce accessible capacity.

4. **Media aging and hysteresis are neglected**
   - Batch tests typically use fresh media; full-scale beds see:
     - Aging of surface chemistry,
     - Irreversible fouling,
     - Changes in pore structure via biofilm or precipitates,
     - History-dependent occupation of sites (hysteresis) governing desorption.

5. **Residence time distribution is non-ideal in practice**
   - Full-scale beds may exhibit early breakthrough because parts of the bed are underutilized.
   - MTZ may broaden with scale or with fluctuating flows, reducing effective capacity relative to what equilibrium batch tests suggest.

In these conditions, relying on batch data to argue for specific service life, bed volumes treated, or field performance is not defensible.

---

## 4. Influence of flow, contact time, influent variability, competing constituents, and PFAS mixtures

### 4.1 Flow rate and EBCT

- **EBCT (empty bed contact time)** is a core design parameter controlling the contact time between PFAS and media.
- As flow increases (shorter EBCT):
  - External film mass transfer limitations become more important.
  - The MTZ often lengthens relative to bed depth, reducing the fraction of the bed that reaches near-equilibrium before breakthrough.
  - Short-chain PFAS, already weakly adsorbing, can show disproportionately earlier breakthrough.

**Implication for translation:**  
Any scale-up claim must specify EBCT; translating batch results to a different EBCT is non-trivial because kinetics and mass transfer dominate at short contact times.

---

### 4.2 Influent variability

Real-world influent often exhibits temporal variability in:

- PFAS total concentrations and relative species composition,
- DOC/NOM levels,
- pH, ionic strength, and temperature,
- Co-contaminant loads (e.g., hydrocarbons, solvents from episodic releases).

This variability affects:

- Driving force for adsorption (e.g., higher C₀ → faster front migration),
- Competition patterns (higher DOC → larger loss of capacity to NOM),
- Site-blocking or preferential sorption.

**Implication for translation:**  
Fixed-bed performance derived from constant, low-variability bench conditions will tend to underpredict breakthrough risk under real, fluctuating influent. Lifetime estimates should account for expected concentration distributions and potential high-load events.

---

### 4.3 Competing constituents

PFAS adsorption, especially for GAC and many polymeric media, is strongly influenced by:

- **Dissolved organic carbon (DOC/NOM)**
  - Competes for hydrophobic and π–π sites.
  - Can occupy pores and reduce accessibility for PFAS.
  - May preferentially displace shorter-chain PFAS, accelerating their breakthrough.

- **Inorganic ions**
  - Modulate electrostatic interactions with charged media (anion-exchange resins).
  - Affect PFAS speciation and effective charge screening.
  - Certain ions can compete for ion-exchange sites.

- **Co-contaminant organics**
  - May have higher affinity than PFAS for some media, limiting PFAS capacity.
  - Can cause long-term fouling or irreversible site occupation.

**Consequences:**

- A medium with high capacity in clean water can perform *much worse* in natural or industrial waters with high DOC and co-contaminants.
- Batch tests that do not replicate real water chemistry risk overestimating usable capacity by large factors.

---

### 4.4 PFAS mixtures and hierarchy of breakthrough

PFAS typically occur as mixtures of:

- Long-chain vs short-chain species,
- Sulfonates vs carboxylates,
- Branched vs linear isomers,
- Known and unknown precursors that can transform downstream.

Common patterns (general tendencies, site-specific verification needed):

- **Stronger sorbates (e.g., long-chain, sulfonates)** often:
  - Adsorb more strongly,
  - Break through later,
  - Can dominate occupancy of high-energy sites.

- **Weaker sorbates (e.g., short-chain, some carboxylates)** often:
  - Break through early, sometimes far earlier than long-chain analogs,
  - Are more sensitive to flow and competition.

Mixture effects can yield non-intuitive outcomes:

- A medium tested with a single PFAS may look excellent, but in mixtures, strong species can displace weak ones (or vice versa) leading to rearrangement along the bed.
- Short-chain PFAS might reach breakthrough limits while bulk PFAS mass removal remains high.

**Implication for translation:**  
Service-life claims must be PFAS-species-specific or tied to a composite performance metric (e.g., sum of target PFAS) and cannot be generalized from single-compound batch tests.

---

## 5. Minimum evidence needed for a defensible service-life or scale-up claim

To support a defensible claim about service life, bed volumes treated, or scale-up of PFAS adsorption, at least the following should be demonstrated.

### 5.1 Representative water and PFAS mixture characterization

1. **Influent characterization**
   - Concentration distributions (mean, range) of:
     - Target PFAS (species, chain lengths, functional groups),
     - Major co-occurring PFAS and suspected precursors,
     - DOC/NOM and UV-254 (for organic competition),
     - Major inorganic ions (e.g., hardness, chloride, sulfate),
     - Co-contaminant organics or inorganics, if present.
   - Temporal variability (at least seasonal or operational ranges).

2. **Statement of representativeness**
   - Evidence that the test water (lab-synthetic, spiked groundwater, real source water) is representative of the targeted full-scale scenario or, if not, clearly bracketed as best/worst-case.

---

### 5.2 Media characterization and operating conditions

1. **Media properties**
   - Type (GAC, PAC, ion-exchange resin, other porous sorbent),
   - Particle size distribution and density,
   - Surface chemistry / functional groups relevant to PFAS interactions (qualitatively described).

2. **Column or pilot conditions**
   - Bed depth and diameter (to infer aspect ratio and potential wall effects),
   - Hydraulic loading rate and EBCT,
   - Flow regime (upflow/downflow), pre-treatment steps (e.g., filtration),
   - Temperature range.

3. **Breakthrough definition**
   - Specific concentration or C/C₀ threshold for each PFAS (or composite metric) used to define:
     - Initial breakthrough,
     - Regulatory/compliance breakthrough,
     - Exhaustion.

---

### 5.3 Demonstrated column/pilot performance

At least one of the following should be presented:

1. **Lab or pilot column breakthrough curves**
   - For the representative water matrix and PFAS mixture.
   - Covering at least from influent start to:
     - Initial breakthrough for short-chain species,
     - Approach to near-exhaustion for long-chain species (or as far as practical).
   - Effluent monitoring over sufficient bed volumes to observe trend, not just single data points.

2. **Multiple EBCTs or flow rates**
   - Demonstrating whether performance is mass-transfer-limited and how sensitive breakthrough is to EBCT.
   - If only one EBCT is tested, explanation of why that EBCT bounds the likely operating window.

3. **Mass balance**
   - Approximate mass balance on PFAS across the bed (influent → effluent + adsorbed) where possible, to assess:
     - Utilized vs theoretical capacity,
     - Whether unaccounted losses suggest side processes (e.g., retention on upstream solids).

---

### 5.4 Modeling and extrapolation requirements

If lifetime and scale-up are derived by modeling rather than direct long-term experiments, then:

1. **Model structure and parameters**
   - Clear description of the model (e.g., advection–dispersion with film and intraparticle diffusion, or other appropriate framework).
   - Isotherm and kinetic parameters obtained from batch tests, but **validated** by fitting at least one set of column breakthrough data.

2. **Validation and sensitivity**
   - Demonstrated match (within reasonable error) between modeled and measured breakthrough curves for the representative conditions.
   - Sensitivity analysis for key parameters (e.g., DOC level, PFAS concentrations, EBCT) to show robustness of predicted lifetime.

3. **Extrapolation bounds and safety factors**
   - When predicting full-scale performance from lab/pilot and model:
     - Clearly state assumptions and bounds (e.g., range of influent concentrations, flows).
     - Apply appropriate safety factors (e.g., design at a fraction of modeled lifetime) to account for unmodeled scale effects (channeling, fouling, operational upsets).

---

### 5.5 Prohibited shortcuts (under the constraints of a defensible claim)

To stay within the task boundaries and avoid overstated conclusions:

- **Do not** treat high batch equilibrium capacity or fast batch kinetics as direct evidence of long column service life.
- **Do not** make scale-up claims without explicitly specifying:
  - Flow and EBCT,
  - PFAS mixture and concentration range,
  - Competing constituents (especially DOC/NOM),
  - Breakthrough criterion and its regulatory or operational basis,
  - Expected range of influent variability.

---

## 6. Practical trade-offs, residuals, and scale-up limitations

### 6.1 Practical trade-offs

- **High capacity vs kinetics**
  - Some media may offer high equilibrium capacity but slow intraparticle diffusion, yielding broad MTZs and early breakthrough at practical EBCTs.
  - Others with modest equilibrium capacity but faster kinetics may provide superior usable capacity (and thus longer lifetime) under typical column conditions.

- **PFAS selectivity vs NOM tolerance**
  - Highly hydrophobic or charged media may bind PFAS strongly but can also sorb NOM intensely, sacrificing PFAS capacity to organic fouling.
  - More selective ion-exchange resins may resist NOM to some degree, but their performance can be sensitive to inorganic composition and pH.

- **Short-chain vs long-chain control**
  - To meet stringent limits on short-chain PFAS, EBCTs must often be longer, or more specialized media used, increasing capital and operating costs.
  - Designs optimized for total PFAS mass removal may not control short-chain PFAS adequately.

---

### 6.2 Residual streams

All adsorption systems generate PFAS-laden residuals:

- **Spent media**
  - Contains concentrated PFAS and co-sorbed contaminants.
  - Requires regeneration (with PFAS recovery) or disposal (often incineration or high-containment landfilling).
  - Adsorption itself is **not degradation or destruction**; any PFAS removal from water appears as accumulation on solid residuals.

- **Backwash and regeneration streams (if applicable)**
  - Highly enriched PFAS in liquid form, requiring subsequent treatment or destruction.

Scale-up must factor the logistics, cost, and environmental implications of these residual streams.

---

### 6.3 Scale-up limitations

Limitations when moving from lab/pilot to full-scale include:

- **Hydrodynamics**
  - Non-uniform distribution manifolds and channeling reduce effective EBCT and capacity utilization.
  - Large-diameter beds may behave differently from small columns due to scale-dependent dispersion and velocity profiles.

- **Operational constraints**
  - Flow fluctuations from plant operation,
  - Maintenance shutdowns and restarts,
  - Temperature variation (seasonal) that can change kinetics and equilibrium.

- **Monitoring and control**
  - Lower sampling frequency in full-scale systems may miss early or transient breakthrough events.
  - Analytical uncertainties at very low PFAS concentrations can complicate detection of subtle breakthrough onset.

These factors typically **shorten practical media life** compared to idealized lab-derived estimates and must be covered by conservative design and monitoring.

---

## 7. Evidence gaps and future research needs

Several areas need better evidence to improve translation from batch to column/field for PFAS:

1. **Systematic comparison of batch and column under identical water matrices**
   - Quantifying how often batch-isotherm-based predictions overestimate usable capacity and by what factor under realistic operating EBCTs and DOC levels, across multiple PFAS classes.

2. **Role of complex PFAS mixtures and precursors**
   - Long-term columns with realistic mixtures, including precursor species that may transform downstream and alter perceived performance.

3. **DOC-type dependence and fouling mechanisms**
   - Distinguishing effects of different DOM types (e.g., humic vs proteinaceous) on PFAS capacity loss and kinetics.
   - Better mechanistic models for pore-blocking and irreversible fouling over multi-year timescales.

4. **Short-chain PFAS behavior at very low concentrations**
   - High-quality breakthrough data and isotherms in the low-ng/L to low-µg/L range for short-chain PFAS, where regulatory limits are tightening and thermodynamic/kinetic uncertainties are large.

5. **Scale-dependent hydrodynamics and model validation**
   - Studies directly comparing well-instrumented pilot-scale and full-scale beds to refine scaling of dispersion, MTZ behavior, and channeling impacts.

6. **Probabilistic lifetime prediction**
   - Moving from single “design life” estimates to probability distributions that explicitly incorporate influent variability, operational uncertainty, and model parameter uncertainty.

---

## 8. Concluding synthesis

- **Batch equilibrium and kinetic tests are essential tools**, but they primarily inform relative media ranking, thermodynamic limits, and potential mass-transfer constraints.
- **Fixed-bed breakthrough data under representative conditions are indispensable** for credible service-life and scale-up claims in PFAS treatment; they integrate hydraulics, kinetics, competitive sorption, and real-world variability.
- **Defensible scale-up** requires:
  - Clear specification of EBCT, influent PFAS mixture and variability, competing constituents, and breakthrough criteria,
  - Column or pilot evidence in representative waters,
  - Mechanistic modeling validated against measured breakthrough and adjusted with realistic safety factors.

Without these elements, claims that link batch PFAS adsorption performance directly to column breakthrough or field lifetime are not scientifically justified and risk underdesign or unexpected failure in practice.

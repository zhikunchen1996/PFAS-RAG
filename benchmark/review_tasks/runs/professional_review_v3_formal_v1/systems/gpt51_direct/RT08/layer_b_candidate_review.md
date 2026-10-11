## 1. Scope and framing

Electrochemical oxidation (EOx), non-thermal plasma (NTP), and sonolysis are often grouped as “PFAS destruction” technologies, but their reaction environments, feed requirements, and maturity are very different. Matching them to a PFAS‑rich liquid stream requires:

- Understanding where they have actually been evaluated (PFAS type, matrix, scale).
- Distinguishing **removal** from the bulk aqueous phase vs. **transformation**, **defluorination**, and **mineralization**.
- Recognizing that “PFAS-rich” usually implies:
  - Pre-concentrated waste (e.g., ion-exchange or foam fractionation regenerant, RO reject, AFFF rinse waters).
  - Complex matrices (saline, organic-rich, co-contaminants).

Below, each technology is reviewed in terms of mechanism, tested PFAS structures, feed/matrix constraints, operational and energy implications, and then integrated into conditional technology-selection criteria.

---

## 2. Reaction environments and feed requirements

### 2.1 Electrochemical oxidation (EOx)

**Reaction environment**

- Aqueous, conductive electrolyte between an anode and cathode.
- Direct electron transfer at the anode plus indirect oxidation via oxidants formed in situ (e.g., hydroxyl radicals, persulfate from sulfate, active chlorine from chloride).
- Reaction zone is strongly coupled to:
  - Electrode material (e.g., BDD and other high-oxygen-overpotential anodes vs. cheaper mixed-metal oxides).
  - Current density, cell potential, and hydrodynamics.
- Often near-ambient temperature and pressure, but ohmic heating can raise temperature substantially at high current densities or in poorly cooled reactors.

**Feed requirements**

- Needs sufficient conductivity (often ≥ a few mS/cm); PFAS alone rarely supplies enough ionic strength, so real-world applications typically rely on background ions or added electrolyte.
- Best suited to comparatively low-suspended-solid, low-oil matrices to avoid rapid electrode fouling or passivation.
- Typically applied to:
  - Concentrated PFAS waters (regenerant brines, RO concentrates, foam fractionation concentrates).
  - Moderately saline waters and some industrial wastewaters.

**PFAS structures evaluated**

- Most lab and pilot work has focused on:
  - Long-chain perfluorosulfonates (e.g., PFOS analogues).
  - Long-chain perfluorocarboxylates (e.g., PFOA-type).
- Increasing but still limited work on:
  - Short-chain perfluorocarboxylates and perfluorosulfonates.
  - Branched isomers.
  - Precursors (e.g., fluorotelomer sulfonates, perfluoroalkyl sulfonamides).
  - Emerging PFAS with ether linkages.
- PFAS often degrade stepwise via chain-shortening and partial defluorination; complete mineralization is rarely demonstrated unequivocally, especially for complex mixtures.

---

### 2.2 Non-thermal plasma (NTP)

**Reaction environment**

- Gas–liquid interface or gas-phase discharge above/bubbling through the liquid.
- Highly non-equilibrium environment with:
  - Energetic electrons.
  - Ions.
  - Excited neutrals and photons.
  - Secondary reactive species in the liquid (e.g., hydroxyl radicals, hydrogen peroxide, possibly solvated electrons depending on configuration).
- Reactor types include dielectric barrier discharges, pulsed corona discharges, plasma jets, and gliding arcs, usually near atmospheric pressure.

**Feed requirements**

- Requires a gas phase (often air, oxygen, nitrogen, or mixtures). Energy is coupled primarily to the gas; PFAS in the liquid are affected indirectly at the interface or via reactive species transported into the bulk.
- Works best in relatively clear, low-foam liquids to maintain stable gas–liquid contact and prevent arcing or discharge quenching.
- Conductivity and salinity affect discharge behavior and energy coupling but are not as strictly constrained as in EOx (though very high salinity can still perturb discharges).

**PFAS structures evaluated**

- Similar emphasis on legacy perfluorocarboxylates and perfluorosulfonates, particularly long-chain species.
- Evidence that PFAS accumulate at air–water interfaces is important; PFAS that are more surface-active (long-chain, sulfonates) tend to be treated more readily because the active zone is interfacial.
- Short-chain PFAS show more mixed results: removal from the liquid can be slower because they are less surface-active and spend more time in the bulk rather than at the interface.
- Evaluations of precursors and complex mixtures exist but are less systematically characterized; pathways can include oxidation, fragmentation, and formation of shorter-chain perfluoroacids.

---

### 2.3 Sonolysis

**Reaction environment**

- High-intensity ultrasound creates cavitation bubbles that:
  - Collapse violently, producing localized “hot spots” with extreme temperatures and pressures.
  - Generate radicals (primarily hydroxyl radicals from water), other reactive species, and interfacial zones with dramatic conditions.
- Chemistry is dominated by:
  - Bubble interior (gas phase).
  - Bubble–liquid interface.
  - Near-field liquid region.
- Typically carried out at low to moderate bulk temperatures but highly energy-intensive due to ultrasound generation.

**Feed requirements**

- Requires acoustic propagation; high turbidity or gas content can attenuate ultrasound.
- PFAS treatment is strongly tied to their **surface activity**:
  - Long-chain PFAS accumulate at the cavitation interface and are degraded preferentially.
  - Short-chain PFAS, being less surface-active, are treated more slowly or sometimes scarcely under similar conditions.
- Typically demonstrated in low- to moderate-conductivity water; high salinity can influence cavitation dynamics and radical yields.

**PFAS structures evaluated**

- Particularly effective for:
  - Long-chain perfluorocarboxylates and perfluorosulfonates, where interfacial accumulation is pronounced.
- Less effective, at least at similar energy inputs, for:
  - Short-chain PFAS.
  - Very polar or hydrophilic fluorinated species with poor interfacial affinity.
- Limited but growing work on precursors; often they are first transformed to perfluoroacids, which are then degraded more slowly.

---

## 3. Influence of concentration, salinity, co-contaminants, operation, kinetics, and energy

### 3.1 PFAS concentration

**Electrochemical oxidation**

- Higher PFAS concentrations:
  - Improve current efficiency to an extent, because PFAS compete better with water and other oxidizable species for anodic reaction sites.
  - Still, PFAS are typically minor sinks for electrons relative to background ions; energy can be wasted on parasitic reactions (e.g., oxygen evolution).
- Very dilute PFAS (e.g., <µg/L) are usually captured first (adsorption, IX, RO) and then EOx is applied to the concentrate, which may reach mg/L or higher. This improves the PFAS mass removed per unit energy but can be offset by higher ionic strength and competing species.

**Non-thermal plasma**

- Because the reactive zone is largely interfacial, **surface coverage** is often more important than bulk concentration:
  - Above a certain PFAS concentration, the interface may be near saturated, so further increases yield diminishing returns in rate per volume.
  - However, a higher bulk concentration still increases the total mass removed over time for the same reactor and operation.
- At very low concentrations, kinetics may be limited by PFAS transport to the interface and by competition from non-PFAS species for reactive intermediates.

**Sonolysis**

- Strongly enhanced with increasing concentration up to a level where interfacial sites are substantially filled:
  - For long-chain PFAS, rates often increase with concentration (within a certain window), due to higher interfacial density.
  - At very high concentration, micelle or aggregate formation can occur, which may alter interfacial behavior—this is not yet fully resolved.
- At very low PFAS concentrations, energy efficiency drops sharply, because cavitation energy is mostly dissipated on water and other solutes.

---

### 3.2 Salinity and background ions

**Electrochemical oxidation**

- Salinity is critical:
  - Moderate electrolyte levels can reduce ohmic losses and improve energy efficiency.
  - High chloride can lead to active chlorine formation, which can enhance PFAS transformation but also generate chlorinated byproducts (e.g., chlorate, perchlorate, chlorinated organics) and add complexity for residuals management.
  - High bicarbonate/carbonate can scavenge radicals and buffer pH, complicating indirect oxidation pathways.
- Very high salinity (e.g., regenerant brines) can increase conductivity but also:
  - Promote aggressive corrosion if materials are not carefully selected.
  - Change dominant reaction pathways (e.g., more halogen-mediated oxidation vs direct electron transfer).

**Non-thermal plasma**

- Salinity affects:
  - Discharge characteristics (e.g., conductivity of the liquid, formation of a conductive skin).
  - Composition of plasma-generated oxidants (e.g., reactive nitrogen and oxygen species).
- High chloride and nitrate can lead to complex aqueous-phase chemistry (e.g., chlorinated and nitrated oxidation products), but systematically quantified PFAS-plasma-salinity interactions remain limited.
- Overall, NTP appears less tightly constrained by conductivity than EOx, but energy efficiency and byproduct formation are still matrix-dependent.

**Sonolysis**

- Electrolytes modify:
  - Cavitation threshold.
  - Bubble dynamics.
  - Radical yields and lifetimes.
- High salinity can:
  - Suppress cavitation intensity or alter bubble collapse.
  - Quench radicals via ionic interactions.
- For PFAS-rich brines, sonolysis can be significantly less energy-efficient than in low-salinity water, and data on highly saline concentrates are limited.

---

### 3.3 Co-contaminants and natural organic matter (NOM)

**Electrochemical oxidation**

- Oxidizable organics, ammonia, nitrite, metals, and surfactants compete for anodic current and indirectly generated oxidants.
- NOM and oils can:
  - Adsorb onto electrode surfaces, causing fouling and reduced performance.
  - Generate a diverse suite of oxidation byproducts (e.g., aldehydes, carboxylic acids, chlorinated organics when chloride is present).
- In real-world wastewaters, PFAS are often a small fraction of total oxidizable load, so energy is often primarily spent on non-PFAS chemistry unless pre-treatment or pre-separation is used.

**Non-thermal plasma**

- Organics and NOM readily react with plasma-generated oxidants, consuming energy that could otherwise contribute to PFAS transformation.
- Surface-active co-contaminants (other surfactants, oils, proteins) can:
  - Compete for interfacial sites with PFAS.
  - Suppress PFAS accumulation at the gas–liquid interface.
- However, NTP may simultaneously reduce some co-contaminants (e.g., some organics, pathogens, certain metals), which can be beneficial depending on treatment goals.

**Sonolysis**

- NOM and surfactants:
  - Compete with PFAS at cavitation interfaces.
  - Scavenge radicals.
- Oily or highly surfactant-laden streams can:
  - Change cavitation behavior.
  - Form stable emulsions that hinder ultrasound propagation.
- For PFAS destruction, low-organic, PFAS-rich concentrates are more favorable; complex wastewaters generally require pre-treatment (e.g., coagulant, filtration, or prior separation) for efficient sonolysis.

---

### 3.4 Reactor operation, kinetics, and energy demand

Because there is no unified energy benchmark across studies, and primary data are not retrieved here, only qualitative comparisons can be made.

**Electrochemical oxidation**

- **Kinetics**:
  - Often approximated as pseudo-first-order with respect to PFAS at relevant concentrations; apparent rate constants depend on current density, electrode type, mass transfer, and matrix.
  - Long-chain PFAS tend to transform faster than short-chain analogues; sulfonates can behave differently from carboxylates depending on electrode and conditions.
- **Energy demand**:
  - Highly variable, but generally:
    - Improves with increasing PFAS concentration and optimized conductivity.
    - Worsens in complex matrices with high organic loads or high halides.
  - Scale-up can reduce specific energy use due to better current distribution and lower relative resistive losses, but only if fouling, byproducts, and maintenance are managed.
- **Operational issues**:
  - Electrode cost, lifetime, and replacement frequency.
  - Scale formation and fouling.
  - Management of off-gases (e.g., oxygen, potential fluorinated or chlorinated volatiles) and residual brine.

**Non-thermal plasma**

- **Kinetics**:
  - Often limited by transport to the interface and by plasma–liquid coupling.
  - Rates are strongly influenced by reactor geometry, gas flow rate, discharge frequency and voltage, and liquid mixing.
  - Typically faster for surface-active PFAS but can be slower than direct radical attack processes for highly soluble short chains.
- **Energy demand**:
  - Electrical energy is required to maintain the discharge; only a fraction couples effectively to aqueous-phase chemistry.
  - Energy efficiencies reported in literature vary widely; gas composition and power modulation (e.g., pulsed vs continuous) can improve performance.
- **Operational issues**:
  - Electrode and dielectric degradation.
  - Ozone, NOx, and other off-gas formation (often requiring off-gas treatment).
  - Scale-up is non-trivial because maintaining uniform plasma over large interfaces is challenging.

**Sonolysis**

- **Kinetics**:
  - For long-chain PFAS in simple matrices, degradation can be relatively rapid on a per-volume basis, driven by efficient interfacial focusing.
  - Short-chain PFAS degradation is typically slower; kinetic models often need to account for interfacial adsorption equilibria.
- **Energy demand**:
  - Generally high on a per-mass-removed basis; ultrasound generation is energy-intensive, and much of the energy is dissipated as heat and non-productive cavitation.
  - Optimizing frequency, power density, and reactor geometry can improve efficiency but likely does not close the gap with some other technologies for large volumes.
- **Operational issues**:
  - Reactor scaling: cavitation is strongly geometry- and frequency-dependent, and achieving uniform cavitation fields at scale is difficult.
  - Equipment wear (transducers, horns) and noise.
  - Heating of the bulk liquid; may need cooling at high power.

---

## 4. Removal vs. transformation, defluorination, and residuals

Across all three technologies:

- **Removal from the aqueous phase** can occur by:
  - Volatilization or aerosolization (particularly for NTP, potentially sonolysis).
  - Adsorption to reactor surfaces or gas bubbles.
  - Transformation to less surface-active or more hydrophilic intermediates that may partition differently.
- **Parent-compound loss does not guarantee**:
  - Complete **defluorination** (release of fluoride equal to the stoichiometric fluorine).
  - Complete **organofluorine removal** (e.g., EOF or TOF measurements).
  - **Mineralization** of carbon to CO₂.
- **Residual streams** and issues:

  - **Electrochemical oxidation**
    - Possible accumulation of shorter-chain perfluoroacids.
    - Generation of inorganic byproducts (chlorate, perchlorate, nitrate/nitrite interconversion) and oxidized organics.
    - Untreated or partially treated brine that still requires disposal.
    - Off-gas that could contain volatile fluorinated organics (rarely quantified comprehensively).

  - **Non-thermal plasma**
    - Potential stripping of PFAS or intermediates into the gas phase (e.g., aerosolized PFAS or volatile fluorinated fragments).
    - Formation of oxidized and nitrated organic byproducts in the liquid.
    - Off-gases containing ozone, NOx, possibly fluorinated organics; must be accounted for in mass balance.

  - **Sonolysis**
    - Accumulation of shorter-chain PFAS as intermediates.
    - Potential build-up of low-molecular-weight organic acids or inorganic species from side-reactions.
    - Unknowns in gas-phase emissions (e.g., CF₄, other volatile PFAS-related species are sometimes hypothesized but not always monitored).

Demonstrated **defluorination** is more robust where:

- Fluoride release is quantified.
- Total organofluorine is monitored (e.g., combustion ion chromatography, EOF).
- Carbon fate is at least partially characterized (inorganic carbon, CO₂, organic intermediates).
  
However, even when defluorination is high, **mineralization** (both carbon and fluorine to inorganic forms) is seldom fully proven, particularly for complex real-world mixtures.

---

## 5. Translating evidence into conditional technology-selection criteria

Below, the three technologies are compared in a **fit-for-purpose** framework, conditioned on:

- Feed type and PFAS profile.
- Matrix complexity.
- Desired endpoint (e.g., parent removal, defluorination, toxicity reduction).
- Scale and integration into treatment trains.

### 5.1 PFAS-rich regenerant brines (e.g., ion-exchange, foam fractionation)

**Features**

- High PFAS concentration (often mg/L–g/L).
- High salinity (e.g., NaCl, Na₂SO₄).
- Low to moderate organic content if upstream separation is efficient.

**Electrochemical oxidation**

- **Strengths**
  - High conductivity reduces ohmic losses.
  - PFAS concentrations are sufficiently high to justify destructive treatment vs disposal.
  - Some brine compositions can support beneficial indirect oxidants (e.g., sulfate to persulfate).
- **Limitations**
  - High chloride promotes active chlorine and chlorate/perchlorate formation; managing byproducts and residual brine is non-trivial.
  - Electrode corrosion and scaling in aggressive brines.
  - Requires robust evidence of defluorination and organofluorine mass balance before claiming destruction.
- **Best fit when**
  - Brines are relatively low in organic contaminants and metals.
  - There is tolerance for managing a concentrated inorganic residual (which may be reused or further polished).
  - Energy costs are acceptable for on-site treatment vs off-site disposal.

**Non-thermal plasma**

- **Strengths**
  - Less directly tied to ionic strength; may be used where conductivity or specific ion content makes EOx challenging.
- **Limitations**
  - High salinity affects discharge and may reduce energy efficiency.
  - Gas–liquid reactors can be challenging with dense brines (foaming, reduced bubble mobility).
  - Limited systematic data for heavily saline brines.
- **Best fit when**
  - EOx is infeasible due to materials constraints or regulatory concerns around electrochemical byproducts.
  - There is value in simultaneous oxidation of co-contaminants in the brine.

**Sonolysis**

- **Strengths**
  - Interfacial focusing of PFAS may still operate in brines, but evidence is limited.
- **Limitations**
  - High salt can suppress effective cavitation and increase energy consumption.
  - Large-scale ultrasonic reactors for dense brines are technically and economically challenging.
- **Best fit when**
  - Volumes are small, PFAS concentrations are very high, and other technologies are unsuitable (e.g., as a niche or polishing step for specialized waste streams).

**Conditional recommendation**  
For typical PFAS-rich regenerant brines, **electrochemical oxidation** is usually the first candidate among these three, provided electrode materials and byproduct management are addressed. NTP and sonolysis may play secondary or niche roles unless specific plant constraints favor them.

---

### 5.2 RO concentrate or nanofiltration reject from PFAS remediation

**Features**

- Enriched PFAS relative to feed but often with:
  - Moderate to high salinity.
  - Persistent NOM and co-contaminants.
- Volumes smaller than the feed but not negligible.

**Electrochemical oxidation**

- **Strengths**
  - Can be integrated downstream of membrane systems.
  - Brine conductivity is usually adequate.
- **Limitations**
  - NOM, organics, and halides all increase parasitic reactions and byproduct formation.
  - May need pre-treatment (e.g., carbon polishing) to reduce organic load, which adds cost and complexity.
- **Best fit when**
  - The primary disposal route for concentrate is problematic (e.g., no deep well, limited discharge options).
  - There is willingness to operate and maintain specialized electrochemical systems.

**Non-thermal plasma**

- **Strengths**
  - May tolerate more NOM than EOx, since reactions are interfacial and radical-driven.
  - Potential to simultaneously reduce organic co-contaminants.
- **Limitations**
  - Foaming and organic content can destabilize plasma–liquid interfaces.
  - Energy efficiency may be modest where PFAS are only a small fraction of the oxidizable load.
- **Best fit when**
  - A multi-contaminant oxidation step is desired (e.g., PFAS plus organics/pathogens).
  - Off-gas handling (ozone, NOx) is acceptable.

**Sonolysis**

- **Strengths**
  - Particularly effective for long-chain PFAS if NOM is not excessively high.
- **Limitations**
  - NOM and co-surfactants compete at bubble interfaces.
  - Energy-intensive, especially for moderate PFAS concentrations.
- **Best fit when**
  - Volumes are constrained (e.g., very small, high-strength streams).
  - Long-chain PFAS dominate and short-chain PFAS are less critical or can be managed separately.

**Conditional recommendation**  
For RO concentrate, **EOx** is often considered where regulated disposal is difficult and matrix conditions allow. **NTP** may be preferred in installations prioritizing simultaneous oxidation of organic co-contaminants. **Sonolysis** tends to be less attractive except for small-volume, long-chain-dominated concentrates where energy cost is secondary.

---

### 5.3 AFFF-impacted waters and high-surfactant matrices

**Features**

- Very complex surfactant mixtures, including PFAS and non-PFAS surfactants.
- High organic load, foaming tendency.
- Often moderate to high conductivity.

**Electrochemical oxidation**

- **Strengths**
  - Can degrade a wide array of organics and oxidizable co-contaminants.
- **Limitations**
  - High surfactant and organic loads mean PFAS are a minor share of electron demand; energy per mass PFAS destroyed is high.
  - Severe electrode fouling and foaming issues possible.
  - Byproduct formation is complex and not well-characterized.
- **Best fit when**
  - Applied to pre-concentrated and partially cleaned streams (e.g., after foam fractionation or adsorption), not directly to raw AFFF.

**Non-thermal plasma**

- **Strengths**
  - Plasma species can oxidize a broad spectrum of surfactants and organics, possibly aiding in AFFF breakdown prior to polishing.
- **Limitations**
  - Foaming and surface-active components complicate reactor operation.
  - PFAS-specific destruction is hard to disentangle from general surfactant oxidation.
- **Best fit when**
  - Employed as a general advanced oxidation step with PFAS considered among multiple organic targets, likely after partial PFAS separation.

**Sonolysis**

- **Strengths**
  - Cavitation is enhanced by some surfactants, but this is double-edged.
- **Limitations**
  - Strong competition at the bubble interface: non-PFAS surfactants outcompete PFAS for interfacial area.
  - PFAS destruction efficiency per energy is likely poor in raw AFFF solutions.
- **Best fit when**
  - AFFF streams have already been processed to isolate PFAS-rich fractions with reduced co-surfactants.

**Conditional recommendation**  
For raw or lightly treated AFFF-impacted waters, **none** of the three technologies is ideal as a primary treatment. PFAS **separation/concentration** (e.g., adsorption, IX, foam fractionation, membranes) should precede destructive steps. Among the three, **EOx** or **NTP** can be applied to resulting concentrates; sonolysis becomes more plausible only after strong pre-separation and volume reduction and when PFAS are highly surface-active.

---

### 5.4 Industrial PFAS manufacturing or process wastewaters

**Features**

- Can include:
  - Extremely high PFAS concentrations.
  - Complex mixtures (precursors, solvents, acids, metals).
  - Strong acids/bases and aggressive chemicals.

**Electrochemical oxidation**

- **Strengths**
  - Direct destruction at the point of generation, potentially reducing liability.
- **Limitations**
  - Corrosive matrices, solvents, and metals can shorten electrode life and complicate safety.
  - High co-contaminant loads make PFAS a secondary sink for current.
- **Best fit when**
  - Streams can be pre-conditioned (neutralization, removal of metals/solvents).
  - There is high incentive to minimize off-site disposal of PFAS wastes.

**Non-thermal plasma**

- **Strengths**
  - Can address multiple organics and some inorganics (e.g., nitrates) simultaneously.
  - Mostly ambient pressure operation.
- **Limitations**
  - Volatile organic components can dominate plasma chemistry and off-gas composition.
  - Reactor design must consider flammability, explosion risk, and off-gas capture.
- **Best fit when**
  - PFAS are part of a broader organic contamination portfolio and off-gas management is robust.

**Sonolysis**

- **Strengths**
  - Localized extreme conditions can promote tough bond scission.
- **Limitations**
  - High solvent content, high viscosity, or particulates can dampen cavitation.
  - Scale-up is particularly challenging and energy-intensive.
- **Best fit when**
  - Niche streams are small and especially recalcitrant, and the facility accepts high specific energy use for on-site destruction.

**Conditional recommendation**  
For industrial PFAS wastes, **pre-separation and segregation** of PFAS-rich, less complex fractions is critical. **Electrochemical oxidation** is a plausible targeted technology for such fractions when corrosivity and fouling are controlled. **NTP** may offer advantages where multi-contaminant oxidation is desired and off-gas management is already in place. **Sonolysis** remains largely experimental for such complex industrial feeds.

---

### 5.5 Short-chain-dominated vs long-chain-dominated PFAS profiles

**Long-chain PFAS–dominated streams**

- **Sonolysis** and **NTP** are favored by surface-active species that concentrate at interfaces:
  - Sonolysis: strong synergy with cavitation interfaces; potentially high per-mass rates for long-chain PFAS.
  - NTP: high interface enrichment aids treatment where plasma–liquid interface is the main reaction zone.
- **EOx** also works but is less sensitive to interfacial phenomena; performance depends more on electron transfer pathways and competing reactions.

**Short-chain PFAS–dominated streams**

- **EOx**:
  - Often more promising relative to NTP and sonolysis, because electron transfer does not rely on surface activity to the same extent.
  - Still, shorter chains tend to be more recalcitrant; rates and energy efficiency are lower than for long chains.
- **NTP** and **sonolysis**:
  - Both can be significantly less energy-efficient for short-chain species.
  - May still be used as polishing steps following prior destruction of long chains and precursors.

---

## 6. Scale-up limitations and evidence gaps

Across all technologies:

- **Scale-up challenges**
  - Translating lab-scale conditions (small volumes, well-controlled matrices) to:
    - Pilot or field-scale reactors with realistic hydraulic conditions.
    - Spatially uniform energy delivery (current distribution in EOx, discharge uniformity in NTP, cavitation field in sonolysis).
  - Managing fouling, scaling, and maintenance over long operational periods.
- **Evidence gaps**
  - Long-term performance with complex, variable matrices typical of field conditions.
  - Comprehensive mass balances including:
    - Fluoride release.
    - Total organofluorine in liquid and gas phases.
    - Carbon fate (CO₂ vs organic intermediates).
    - Formation and persistence of non-fluorinated toxic byproducts.
  - Robust life-cycle assessments comparing these technologies to:
    - Conventional disposal (e.g., incineration).
    - Emerging alternatives (e.g., supercritical water oxidation, reductive approaches).
  - Comparative energy and cost analyses under standardized conditions.

Because detailed numerical comparisons and verified study data are not retrieved here, any claim that one technology is universally superior would be unjustified. Performance is **strongly contingent** on:

- PFAS species distribution (chain length, functional groups, precursors).
- Matrix composition (ionic strength, NOM, co-surfactants, metals).
- Degree of pre-concentration and pre-treatment.
- Reactor design and scale.
- Target endpoint (e.g., >90% parent removal vs stoichiometric defluorination).

---

## 7. Practical, conditional selection guidance

Summarizing in decision-oriented terms:

1. **Always consider separation first**  
   For large-volume, low-concentration waters, use **adsorption/IX/RO/foam fractionation** to generate a PFAS-rich liquid. EOx, NTP, and sonolysis are best used on such concentrates.

2. **If the concentrate is saline but not excessively organic** (e.g., IX regenerant):

   - Start with **electrochemical oxidation**, provided that:
     - Electrode materials compatible with salinity and pH are available.
     - Regulatory and operational constraints on chlorinated byproducts can be managed.
   - Consider **NTP** if:
     - EOx is impractical (e.g., materials or regulatory constraints).
   - Reserve **sonolysis** for small, long-chain-rich streams where energy penalties are acceptable.

3. **If the concentrate has elevated organics/NOM and multiple co-contaminants:**

   - **EOx** is still viable but will likely have lower PFAS-specific energy efficiency.
   - **NTP** may be more attractive where simultaneous oxidation of organics is beneficial and off-gas management is feasible.
   - **Sonolysis** becomes less favorable unless co-contaminants are limited.

4. **If PFAS profile is long-chain-dominated and volume is modest:**

   - **Sonolysis** and **NTP** can be strong candidates, particularly for streams with manageable salinity and limited interfering surfactants.
   - **EOx** remains an option, especially for brines or when existing electrochemical infrastructure is available.

5. **If PFAS profile is short-chain-dominated:**

   - Prioritize **EOx** among these three, while acknowledging that short-chain PFAS remain challenging.
   - **NTP** and **sonolysis** may serve as polishing steps but are less intrinsically well-matched to short-chain species.

6. **If the treatment objective is full defluorination or near-mineralization:**

   - Demand **mass-balanced evidence** (fluoride, EOF, carbon) from pilot/field-relevant conditions.
   - Recognize that, for all three technologies, current evidence for complete defluorination under realistic conditions is limited, and parent loss alone is not a sufficient endpoint.

---

## 8. Specific future research needs

To enable rational selection and scale-up:

- **Standardized metrics and testing**
  - Common reporting of:
    - PFAS speciation (including precursors and short-chain fractions).
    - Energy per mass of PFAS defluorinated (not just removed as parent).
    - Byproduct formation and toxicity changes.
  - Benchmarks across EOx, NTP, and sonolysis under matched matrix conditions.

- **Realistic pilot and field trials**
  - Long-duration pilots on:
    - Regenerant brines.
    - RO concentrates.
    - Industrial PFAS-rich wastewaters.
  - Focus on fouling, material durability, maintenance, and process control.

- **Byproduct and gas-phase characterization**
  - Comprehensive investigation of:
    - Fluorinated and non-fluorinated intermediates in liquid.
    - Volatile and aerosol-phase PFAS-related compounds in off-gas.
    - Changes in mixture toxicity (e.g., bioassays).

- **Reactor design and hybridization**
  - Integrated systems that combine:
    - Separation (IX, RO, foam fractionation) with EOx, NTP, or sonolysis.
    - Potential synergies (e.g., plasma-enhanced electrochemistry, sonically enhanced EOx) if energy gains justify complexity.
  - Modular, field-deployable reactors with flexible operation for varying loads.

- **Life-cycle and techno-economic analysis**
  - Comparative assessment of these technologies against alternative destruction options, factoring:
    - Energy mix.
    - Capital and O&M costs.
    - Residual management and regulatory constraints.

---

### Closing perspective

Electrochemical oxidation, non-thermal plasma, and sonolysis each occupy distinct niches in the treatment of PFAS-rich liquids. Their relative value depends not on single performance benchmarks but on how well their **reaction environments** align with the **PFAS profile**, **matrix**, and **treatment goals**. None is universally superior; each requires careful, evidence-based matching to the specific waste stream and endpoint, with integrated separation and residual management strategies.

## 1. Scope and framing: membranes as separation, not destruction

Membrane processes for PFAS are **separation technologies**. They primarily:

- Partition PFAS between:
  - permeate (treated water)
  - retentate/concentrate (residual stream)
- Sometimes add **adsorbed PFAS** on or in the membrane itself

They do **not**, by themselves, achieve:
- chemical transformation,
- defluorination,
- mineralization, or
- destruction of PFAS,

unless a clearly demonstrated reactive function is integrated (e.g., reactive coatings, electrochemical reactions at electrodes). Even then, **separation and transformation must be disentangled analytically**.

This review focuses on how to **select among membrane options** for a given PFAS mixture, water matrix, and treatment objective, and how to interpret and compare reported performance without confusing separation with degradation.

---

## 2. Separation mechanisms by membrane class

### 2.1 Nanofiltration (NF)

**Dominant mechanisms**

- **Size exclusion / steric hindrance**  
  - NF pores typically in the ~0.5–2 nm range (conceptually).  
  - High rejection of long-chain anionic PFAS (e.g., C8 sulfonates) largely due to hydrated size and inability to penetrate dense selective layer.

- **Donnan (electrostatic) exclusion**  
  - Many NF membranes carry fixed charges (often negative) at realistic pH.  
  - Anionic PFAS are repelled; co-ions experience reduced partitioning into the membrane phase.  
  - Counter-ions (e.g., Na⁺) are attracted, but overall co-ion exclusion limits PFAS transport.

- **Hydrophobic interactions / limited adsorption**  
  - Fluorinated tails can weakly adsorb to polymer surfaces, sometimes increasing apparent rejection initially (adsorptive lag), then later decreasing as adsorption sites saturate.

**Key implication:** NF is a **combination of charge- and size-based partitioning**, with adsorption superimposed. Reported “rejection” at early times may partly reflect **adsorption plus steric rejection**, not only steady-state sieving.

---

### 2.2 Reverse osmosis (RO)

**Dominant mechanisms**

- **Solution–diffusion in dense polymer**  
  - RO membranes are effectively nonporous at the scale of PFAS.  
  - PFAS transport is controlled by solubility (partitioning) into the polymer plus diffusion across the dense layer.  
  - The very low solubility and relatively large size of PFAS generally yield **high rejection**.

- **Electrostatic effects**  
  - Surface and internal charges can still affect PFAS partitioning to the membrane; however, size/solubility dominate.

- **Adsorption to membrane surface and internal free volume**  
  - Hydrophobic and fluorophilic interactions can cause PFAS uptake into the membrane skin and support layer, especially at low feed concentrations, complicating mass balances and time-dependent flux.

**Key implication:** RO tends to provide **broader, more robust rejection across PFAS types** than NF, but at higher energy and with significant concentrate management needs. The mechanism is more “bulk” solution–diffusion, less pore-driven.

---

### 2.3 Adsorptive membranes

(Examples: membranes blended or coated with activated carbon, ion-exchange resins, MOFs, zeolites, or other sorbents; often operated at low TMP as micro/ultrafiltration-like modules.)

**Dominant mechanisms**

- **Sorption dominance over sieving**  
  - PFAS capture is mostly through sorption to embedded/attached functional materials:
    - hydrophobic interactions with sorbent domains,
    - electrostatic attraction (e.g., cationic functional groups binding anionic PFAS),
    - specific interactions in tailored sorbents.

- **Membrane as contactor and support**  
  - The polymer body primarily provides hydraulic permeability and structural support; the functional phase does the separation.  
  - Nominal pore size may be large relative to PFAS; PFAS are not significantly size-excluded.

- **Kinetics and capacity**  
  - Performance depends on mass transfer into sorbent domains and their finite capacity.  
  - Once sorption sites saturate, PFAS breakthrough occurs; steady-state rejection may fall to near zero unless the sorbent fraction is very high or regenerated.

**Key implication:** Adsorptive membranes are **more analogous to embedded GAC/IX columns** than to conventional pressure-driven membranes. Reported “rejection” is nearly always a **time-limited, capacity-limited** phenomenon.

---

### 2.4 Electrically assisted membranes

This class spans several variants:

- **Electrodialysis (ED) / Electrodialysis reversal (EDR)**
- **Membrane capacitive deionization (MCDI) and CDI with ion-exchange membranes**
- **Electro-NF / electro-RO (electrical potential applied across membrane stack)**

Mechanisms differ; conceptually:

#### 2.4.1 Electrodialysis-type systems

- **Ion-migration in an electric field**  
  - PFAS anions migrate toward anodes through anion-exchange membranes (AEM) into concentrate compartments.  
  - Cation-exchange membranes prevent back-diffusion of cations and PFAS.

- **Donnan partitioning in ion-exchange membranes**  
  - Semi-permanent charged groups in AEMs favor anions (including PFAS), but selectivity vs. competing anions (Cl⁻, SO₄²⁻, HCO₃⁻, NOM-derived anions) is critical.

- **No intrinsic destruction**  
  - PFAS accumulate in concentrate compartments, similar to RO/NF concentrate, unless coupled to destructive processes.

#### 2.4.2 CDI/MCDI and related

- **Electrosorption in electrical double layers**  
  - At applied voltage, PFAS anions are accumulated in EDLs or ion-exchange layers adjacent to electrodes.  
  - Performance strongly depends on competitive non-PFAS ions and NOM.

- **Reversibility and regeneration**  
  - Desorption occurs when voltage is reduced or reversed, yielding a PFAS-enriched brine or regenerant stream.

#### 2.4.3 Electrically assisted pressure-driven membranes

- **Enhanced electrostatic exclusion or attraction**  
  - Applied potentials can modulate surface charge, potentially increasing PFAS rejection or adsorption.  
  - However, hydraulic pressure remains the main driving force; transformation is rare without reactor-like electrodes and high potentials.

**Key implication:** Electrically assisted membranes can offer **ion-selective concentration control**, but still produce **concentrated PFAS streams** rather than destruction. Selectivity vs inorganic anions and NOM is a central constraint.

---

### 2.5 Hybrid configurations

Relevant hybrids include:

- **NF/RO + adsorptive pretreatment** (e.g., GAC, IX, powdered sorbents):
  - Reduces fouling and partial PFAS loading, stabilizes membrane performance.
- **NF/RO + post-polishing (GAC, IX, AEMs, resins)**:
  - Polishing low residual PFAS in permeate; main PFAS mass remains in RO/NF concentrate.
- **Membrane contactors with in situ regeneration**:
  - Adsorptive membranes coupled to electrochemical regeneration or chemical desorption.
- **ED/RO cascades**:
  - ED for bulk desalting and PFAS pre-concentration, followed by RO/NF or destructive treatment.

Mechanisms are combinations of those above; for selection, it is crucial to track **where the PFAS mass accumulates** and **how regeneration/concentrate handling is managed**.

---

## 3. Influence of PFAS properties on membrane selection

### 3.1 Chain length and hydrophobicity

- **Long-chain perfluoroalkyls (≥C8)**  
  - Generally exhibit higher rejection in NF and RO due to larger hydrated size and lower solubility.  
  - Stronger affinity for hydrophobic/fluorous domains (membranes and sorbents), enhancing adsorption but also fouling and lag effects.

- **Short-chain PFAS (≤C6)**  
  - Smaller and more hydrophilic; more challenging to remove by size or hydrophobic interactions.  
  - NF may show partial rejection; RO remains more robust, but not perfect.  
  - Adsorptive membranes require higher capacity or specialized sorbents to maintain breakthrough performance.

**Implication for selection:**  
- For **regulatory compliance dominated by long-chain PFAS**, NF may be sufficient, especially with polishing.  
- For **short-chain and ultra-short PFAS**, RO or very high-capacity/selective adsorptive systems are often necessary; ED-type technologies may help if selectivity vs other anions can be achieved.

---

### 3.2 Functional group and speciation

- **Carboxylates vs. sulfonates**  
  - Sulfonates are typically more strongly anionic and hydrophobic; often slightly higher rejection in NF and stronger adsorption.  
  - Carboxylates may be more problematic for NF and low-charge membranes.

- **Zwitterionic/neutral precursors**  
  - Neutral PFAS (e.g., some fluorotelomer alcohols or amides) may have weaker electrostatic exclusion and higher partitioning into hydrophobic membrane domains.  
  - Their rejection can be lower in NF and some RO formulations; adsorption can be higher.

- **Speciation dependence on pH and ionic strength**  
  - Most common PFAS are anionic at environmental pH, but precursors may change charge state with pH.  
  - ED and CDI performance is strongly tied to speciation; so is adsorption in ion-exchange-based membranes.

**Implication for selection:**  
Process choice should be based on **the actual PFAS composition (anionic vs. neutral vs precursor-rich)** rather than only on “total PFAS”. Electrically driven separations and Donnan-exclusion-based NF depend critically on anionic character.

---

### 3.3 Molecular architecture (branched vs linear, polymeric PFAS)

- **Branched isomers** may have slightly different partitioning and rejection due to altered hydrodynamic size and hydrophobicity, but these differences rarely drive process selection alone.
- **Polymeric PFAS** (e.g., fluorinated surfactant mixtures) can form micelles or aggregates at sufficient concentration; these can:
  - increase NF/RO rejection (larger effective size),
  - but also cause severe fouling or interfacial adsorption.

For complex industrial wastewaters, membrane selection must consider **colloidal or micellar PFAS forms** and the risk of surface-active fouling.

---

## 4. Membrane characteristics influencing PFAS separation

### 4.1 Pore size / effective MWCO

- For **NF**, a tighter MWCO generally yields higher PFAS rejection, especially for short-chain species. However:
  - Tighter NF behaves more like low-pressure RO, increasing energy and reducing flux.
  - PFAS rejection gains may plateau relative to losses in productivity.

- For **adsorptive membranes**, nominal pore size is primarily relevant for:
  - hydraulic permeability,
  - access to sorbent domains,
  - fouling behavior.

### 4.2 Surface charge and chemistry

- **Charge sign and density**  
  - More negative charge enhances electrostatic exclusion of anionic PFAS in NF.  
  - Cationic surfaces in adsorptive membranes promote binding of anionic PFAS but may also favor NOM adsorption and fouling.

- **Hydrophobicity / fluorophilicity**  
  - More hydrophobic membrane skins tend to adsorb PFAS more strongly—this can:
    - Improve early-time “rejection” (due to lag),
    - but reduce long-term resistance as adsorption sites saturate and desorption occurs.

- **Layered and mixed-matrix structures**  
  - Incorporation of zeolites, MOFs, or AEM particles can introduce additional, often more selective, sorption or Donnan exclusion domains—but often at the cost of lower permeability or mechanical robustness.

### 4.3 Mechanical robustness and cleanability

- Thinner, more permeable membranes can be attractive for energy savings but may be more prone to:
  - oxidative or chemical damage during aggressive cleaning (especially important if PFAS-laden fouling layers require removal),
  - compaction and performance decay at high TMP.

Robustness is particularly relevant when treating **highly fouling, industrial matrices** or when frequent chemical cleaning is anticipated.

---

## 5. Operating conditions and matrix effects

### 5.1 Pressure, flux, and recovery

- **Transmembrane pressure (TMP)**  
  - For RO/NF, higher TMP increases flux but can:
    - Increase concentration polarization, locally raising PFAS concentration at the membrane surface and potentially **lowering apparent rejection** (depending on PFAS and membrane).
    - Exacerbate fouling and compaction.

- **Flux**  
  - Higher flux increases water throughput but:
    - May shift the balance between diffusion and convection of PFAS, affecting rejection.
    - Can accelerate fouling and alter adsorption–desorption equilibrium.

- **Recovery (water recovery ratio)**  
  - Higher recovery increases bulk PFAS concentration in retentate and exacerbates concentration polarization.
  - For electrically driven systems (ED/CDI), recovery affects:
    - the degree of desalination in the diluate,
    - PFAS concentration in concentrate/regenerant streams,
    - overall energy use per unit treated water.

**Implication for comparability:**  
Performance data (rejection, energy) are **not comparable** if TMP, flux, recovery, and hydrodynamics differ substantially; these parameters strongly influence observed PFAS separation.

---

### 5.2 Competing ions and ionic strength

- **Inorganic anions (Cl⁻, SO₄²⁻, NO₃⁻, HCO₃⁻)**  
  - Compete with PFAS for:
    - Donnan exclusion “capacity” in NF and ion-exchange membranes,
    - electrosorption sites in CDI/MCDI,
    - transport pathways in ED.
  - High ionic strength can:
    - shrink electric double layers and reduce effective electrostatic exclusion in NF,
    - decrease PFAS selectivity in ED and CDI, as background ions dominate current.

- **Multivalent cations (Ca²⁺, Mg²⁺)**  
  - Can:
    - Promote scaling and inorganic fouling,
    - Complex with NOM, altering charge and conformation,
    - Change PFAS micellar behavior at higher concentrations.

**Process selection implications:**

- **RO** is less sensitive to ionic strength for PFAS rejection but more affected for energy consumption and scaling risk.
- **NF** may lose PFAS selectivity as ionic strength rises, making it less reliable for brackish or saline waters without additional steps.
- **ED/CDI-based systems** can be overwhelmed by non-PFAS ions in high-ionic-strength wastewaters, yielding poor PFAS selectivity and high energy use.

---

### 5.3 Natural organic matter (NOM) and co-contaminants

- **NOM effects**  
  - Competes for:
    - adsorption sites in adsorptive membranes,
    - membrane surface sites, enhancing fouling formations,
    - charge capacity in ED/CDI systems.
  - Can **shield** or associate with PFAS, altering:
    - apparent size and charge (e.g., PFAS–NOM complexes),
    - transport through NF/RO.

- **Surfactants and oils**  
  - Strongly affect interfacial behavior and can:
    - greatly increase fouling,
    - modify PFAS partitioning (e.g., co-micellization),
    - alter apparent rejection due to formation of surfactant-rich layers on the membrane.

**Implication for selection:**  
High NOM and co-surfactant matrices often require:
- pre-treatment (coagulation, adsorption, pre-filtration),
- more fouling-tolerant membranes or lower flux operation,
- explicit design for fouling control and cleaning.

---

## 6. Fouling and its interaction with PFAS separation

Fouling can shift the apparent separation mechanism:

- **Cake-enhanced rejection**  
  - A fouling layer (NOM, biofilm, colloids) can act as a secondary membrane with smaller effective pores, often increasing PFAS rejection.
  - However, this may co-occur with:
    - reduced flux,
    - higher TMP and energy,
    - temporal instability (cake layer can compress, slough off, or desorb PFAS).

- **Sorption and slow release from fouling layers**  
  - Fouling layers may adsorb PFAS, especially for long-chain and hydrophobic species.  
  - During cleaning or operational transients, PFAS can be released, causing:
    - Breakthrough in permeate despite apparently high average rejection,
    - Complicated mass balances.

- **Irreversible fouling and aging**  
  - Long-term fouling can irreversibly change membrane charge and hydrophobicity, altering PFAS partitioning characteristics.

**Implication for process selection:**  
Design should prioritize **steady-state performance under fouled conditions**, not pristine-membrane results. Fouling control strategy (pretreatment, flux, cleaning) is part of PFAS management, not just a productivity consideration.

---

## 7. Comparative roles of each membrane class

The following comparison is **conditional** on PFAS composition, feed matrix, and treatment objective; these processes cannot be meaningfully ranked in a general sense.

### 7.1 NF vs RO

- **When NF is appropriate**  
  - Objective:  
    - reduce long-chain anionic PFAS to meet a moderately stringent standard, and/or
    - bulk separation before polishing.
  - Feed:  
    - low to moderate salinity, moderate NOM, limited short-chain fraction.
  - Mechanism match:  
    - Donnan and steric exclusion sufficient; manageable fouling; concentrate volume acceptable.

- **When RO is preferred**  
  - Objective:  
    - high-level PFAS control including short-chain PFAS,  
    - potable reuse or very low regulatory limits.
  - Feed:  
    - variable or high salinity, unknown or complex PFAS mix, or presence of many short-chain species.
  - Mechanism match:  
    - highest barrier and broad PFAS rejection; less susceptible to loss of selectivity at high ionic strength.

**Trade-offs:**

- NF: lower energy, higher flux, but potentially lower short-chain PFAS rejection and higher sensitivity to ionic strength.
- RO: higher capital/energy and scaling risk; but more robust PFAS barrier.

---

### 7.2 Adsorptive membranes

Best suited when:

- PFAS concentrations are **relatively low** and dominated by more adsorbable species (e.g., long-chain sulfonates and carboxylates).
- Flowrates are modest and **membrane replacement or regeneration** is manageable.
- The objective is **compact, modular systems** (e.g., point-of-entry or small systems) where GAC/IX columns are constrained by footprint but can be integrated into membrane modules.

Limitations:

- Finite capacity and breakthrough; performance strongly time-dependent.
- Strong competition from NOM and co-anions; reduced efficiency in high-DOC or high-ionic-strength waters.
- Regeneration may generate PFAS-rich regenerant that still requires treatment.

---

### 7.3 Electrically assisted membranes (ED, CDI, etc.)

Most relevant when:

- Target water has significant ionic strength such that:
  - desalination and PFAS removal can be co-optimized,
  - or PFAS are a minor component of an ion-rich matrix and the goal is selective concentration.

- PFAS are predominantly **anionic**, and technology is tuned to distinguish them from dominant inorganic anions (which is difficult in practice).

Limitations:

- Selectivity vs. chloride, sulfate, and NOM is often poor; PFAS removal may be diluted by removal of abundant non-PFAS ions.
- Energy may become prohibitive if large current efficiencies are devoted to moving non-PFAS ions.
- As with RO/NF, concentrate or regenerant streams with high PFAS load must be managed.

---

### 7.4 Hybrids

Typical rational choices:

- **NF/RO + adsorptive polishing**:
  - Use RO (or tight NF) to capture most PFAS mass into a manageable concentrate volume.
  - Use GAC/IX/adsorptive membranes on permeate for polishing, where loadings are lower and capacity utilization is high.
  - Appropriate for high-stringency drinking water targets with dominated anionic PFAS.

- **Adsorptive pretreatment + RO/NF**:
  - Remove fouling-prone organics and some PFAS upfront.
  - Stabilize membrane performance and reduce fouling, especially in high-DOC waters.

- **ED as pre-concentrator + destructive treatment**:
  - Use ED to concentrate PFAS (with other ions) into a smaller volume.
  - Apply destructive treatment (e.g., advanced oxidation/reduction outside the membrane scope) to concentrate.

**Key principle:**  
Hybrids are evaluated not only on separation performance but on **how they partition PFAS mass among permeate, concentrate, sorbents, and fouling layers**, and whether a **credible downstream fate** exists for those retained PFAS.

---

## 8. Interpreting and comparing reported performance

A central requirement is to know **when reported rejection, adsorption, permeability, and energy results are sufficiently comparable to guide process selection**.

### 8.1 Meaning of “rejection” in different contexts

- **NF/RO steady-state rejection**  
  - Defined as (1 – Cp/Cf) at pseudo-steady operating conditions:
    - constant flux/TMP,
    - stabilized fouling layer,
    - negligible short-term adsorption–desorption transients.
  - **Comparable** only if:
    - Same or similar PFAS species (or at least same chain-length category and functional group),
    - Similar salinity and NOM levels,
    - Similar flux and recovery (or clearly reported and corrected for concentration polarization).

- **Adsorptive membrane “rejection”**  
  - Typically time-dependent, representing a moving-front behavior:
    - early-time apparent rejection can be near 100% due to available sorption capacity,
    - eventually breakthrough occurs as capacity is consumed.
  - **Comparable** only if:
    - Breakthrough curves are reported (e.g., capacity at a defined breakthrough criterion),
    - Feed concentration, flow, and bed/membrane mass are specified,
    - NOM and competing sorbates are similar.

- **ED/CDI PFAS removal**  
  - Often reported as decrease in PFAS concentration in the diluate (treated) stream.
  - **Comparable** only if:
    - Ionic strength and co-ion composition are similar,
    - Applied voltage/current and recovery are similar,
    - Membrane/electrode properties and stack geometry are reported.

**Non-comparable situations:**

- Comparing long-chain PFAS rejection in low-salinity lab water at low flux with short-chain PFAS rejection in high-salinity natural water at high flux.
- Comparing early-time adsorptive membrane removal to steady-state RO rejection.

---

### 8.2 Adsorption vs. true permeation control

To use data for process selection, it is crucial to distinguish:

- **Adsorption-dominated removal**:
  - PFAS mass balance shows accumulation on/in membrane or fouling layer.
  - Permeate concentrations may rise over time as sites saturate.
  - Relevant for adsorptive membranes and early operation of NF/RO.

- **Permeation-limited separation**:
  - PFAS transport controlled by steady-state mechanism (size/charge/solution–diffusion).
  - Membrane mass balance stable; minimal ongoing accumulation.

**Evidence needed to be confident:**

- Time-dependent flux and concentration profiles demonstrating stable rejection after an initial conditioning period.
- Ex-situ PFAS extraction from membranes/fouling layers, showing whether significant mass is sequestered.
- Multi-cycle operation with repeated cleaning/regeneration to test reversibility.

Without such information, high initial rejection cannot be reliably generalized to long-term process performance.

---

### 8.3 Permeability and energy metrics

**Permeability (A, L m⁻² h⁻¹ bar⁻¹, etc.) and energy consumption become comparable only when:**

- Transmembrane pressure, temperature, and water recovery are stated.
- Fouling state is controlled:
  - Data at constant, representative fouling state (e.g., after realistic runtime, with typical cleaning schedule).
- Salinity / osmotic pressure are comparable:
  - RO energy at very low TDS is fundamentally lower than at seawater salinity; PFAS removal performance alone cannot be compared across these contexts.

For **ED/CDI**, energy metrics are comparable only if:

- Current efficiency (fraction of charge used to move target species vs. background ions) is reported or constrained.
- Operating voltage and recovery are in similar ranges.
- System configuration (spacer thickness, membrane area, etc.) and mass-transport limitations are similar.

---

### 8.4 Minimal comparability criteria for process selection

For **practical, engineering-level process selection**, data sets are sufficiently comparable when the following are aligned or explicitly accounted for:

1. **PFAS scope:**
   - At minimum, chain-length distribution and functional group (e.g., “C4–C12 perfluoroalkyl sulfonates and carboxylates”) are similar.
2. **Feed matrix:**
   - Ionic strength within the same order of magnitude, similar dominant anions,
   - DOC/NOM concentration in a comparable range,
   - Similar presence/absence of problematic surfactants or oils.
3. **Operating point:**
   - For RO/NF: flux within ~factor 2, water recovery in same range (e.g., 70–85%), temperature comparable.
   - For adsorptive membranes: influent concentration, surface loading rate, and breakthrough criterion defined similarly.
   - For ED/CDI: voltage/current density, recovery, and ion background comparable.
4. **Membrane properties:**
   - Comparable MWCO/nominal “tightness” for NF,
   - Similar membrane chemistry or at least same broad class (e.g., polyamide RO vs. another polyamide RO).
5. **Endpoint definition:**
   - Same metric (e.g., percent rejection at steady state, or capacity at 10% breakthrough),
   - Same time scale (initial transients vs. stable long-term performance).

Absent these alignments, quantitative ranking (e.g., “Process A is better than Process B”) is unreliable; only **qualitative trends** should be inferred.

---

## 9. Practical selection strategy linked to objectives

### 9.1 Objective: drinking water / potable reuse

Typical requirements:

- Very low PFAS concentrations (in the low ng/L range),
- Multiple PFAS of varying chain length (including short-chain),
- Co-existing NOM and moderate ionic strength.

Indicative strategy:

- **Primary barrier:** RO or tight NF, depending on composition and regulatory stringency for short-chain PFAS.
- **Polishing:** GAC/IX/adsorptive membranes on permeate, especially for:
  - short-chain or neutral PFAS poorly rejected by NF,
  - residuals after RO.
- **Concentrate management:**  
  - Plan for volume minimization, possible ED-assisted reconcentration, or coupling to destructive technology (outside membrane scope).

---

### 9.2 Objective: industrial wastewater pre-treatment or mass capture

Requirements:

- Higher PFAS concentrations,
- Often high salinity and co-contaminant load,
- Goal to reduce PFAS load before biological or other treatment, or to capture PFAS mass in a smaller stream.

Indicative strategy:

- **Primary PFAS captor:**  
  - NF or RO, chosen based on salinity and PFAS composition:
    - NF if long-chain PFAS dominate and salinity is manageable,
    - RO if significant short-chain fraction or high salinity.
- **Alternative concentration route:**  
  - ED to pre-concentrate PFAS along with salts, if energy and selectivity can be justified.
- **Polishing:**  
  - Adsorptive membranes or columns on effluent if necessary.
- **Residual streams:**  
  - PFAS-rich concentrate or regenerant must be routed to destruction or secure disposal; selection should consider total PFAS mass and volume of this stream.

---

### 9.3 Objective: small-scale / point-of-use systems

Requirements:

- Intermittent operation,
- Simplicity and low maintenance,
- Focus on a subset of PFAS (often long-chain).

Indicative strategy:

- **Adsorptive membranes or compact IX/GAC cartridges:**
  - Provide high initial removal at low flowrates.
  - Replacement interval designed from realistic capacities including NOM competition.
- **NF/RO under sink systems:**
  - For broad-spectrum PFAS barrier, with periodic cartridge replacement and concentrate disposal to sewer.
- **Data needs:**
  - Long-term breakthrough and capacity data at representative tap water compositions are essential; lab tests with single-PFAS, low-DOC water are insufficient for product selection.

---

## 10. Evidence gaps and future research needs

Key gaps limiting robust process selection include:

1. **Systematic, multi-PFAS, multi-matrix comparisons**  
   - Studies often focus on single compounds in simplified matrices.  
   - There is a need for datasets where NF, RO, adsorptive membranes, and ED/CDI are compared side-by-side for the **same PFAS suite, same water, and harmonized operating conditions**.

2. **Short-chain and emerging PFAS behavior**  
   - More rigorous understanding of solution–diffusion partitioning for very short-chain and novel PFAS structures in RO/NF polymers.
   - Adsorptive membrane design specifically tuned to these species.

3. **Coupled fouling–PFAS dynamics**  
   - Detailed time-resolved studies examining how fouling layers build, sorb PFAS, and release them during cleaning or operational changes.
   - Methods to distinguish PFAS sequestered in foulants vs. membranes vs. concentrates.

4. **Electrically assisted selectivity**  
   - Improved AEMs and ion-selective materials that favor PFAS over abundant inorganic anions or NOM-derived ions.
   - Quantitative selectivity and energy trade-offs in realistic waters.

5. **Robust mass balances and fate analysis**  
   - For all membrane processes, consistent accounting of PFAS in:
     - permeate,
     - retentate/concentrate/regenerant,
     - sorbed on/in membranes and fouling layers,
     - lost due to sampling and analytical limitations.
   - Without such balances, claims about “removal” cannot be mapped to true risk reduction.

---

## 11. Concluding guidance

- Membrane processes for PFAS are **separation technologies**; they move PFAS from one phase or stream to another. Transformation or destruction must be separately demonstrated.
- Process selection must:
  - Match **separation mechanism** (size, charge, adsorption, electrosorption) to **PFAS properties** and **matrix characteristics**.
  - Address **fouling and concentrate management** explicitly.
  - Use performance data that are **comparable in PFAS scope, feed matrix, operating point, and endpoint definitions**.

When these conditions are met, nanofiltration, reverse osmosis, adsorptive membranes, and electrically assisted membranes can each occupy well-defined niches in PFAS management strategies, frequently in **hybrid trains** rather than as stand-alone solutions.

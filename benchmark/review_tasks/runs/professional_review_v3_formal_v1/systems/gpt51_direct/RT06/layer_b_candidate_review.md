## 1. Scope and context

Foam fractionation (or foam flotation) for PFAS is an **air–water separation** process, not a degradation technology. PFAS accumulate at the gas–liquid interface, are swept into foam, and are separated into a small “foamate” volume. Performance depends strongly on:

- PFAS molecular properties
- Water chemistry (co-surfactants, organic matter, salts, other constituents)
- Reactor operation (gas flow, bubble size, residence time, recycle, foam handling, configuration)

Throughout this review, the following performance measures are treated as **distinct**:

- **Removal**: decrease of a PFAS concentration in the feed/bulk water.
- **Recovery**: fraction of the PFAS mass transferred from feed into foamate.
- **Enrichment (concentration factor)**: PFAS concentration in foamate relative to feed.
- **Mass balance**: closure of the PFAS and total organofluorine mass accounting (feed vs permeate/treated water vs foamate vs any other streams).
- **Volume reduction**: ratio between initial water volume and final foamate or concentrated volume.

These metrics can move in different directions under the same conditions; they are not interchangeable.

---

## 2. PFAS molecular properties and their control on foam fractionation

### 2.1 Chain length and hydrophobic tail

For classical perfluoroalkyl acids (PFAAs):

- **Longer-chain PFAS (e.g., C8 and above)**  
  - Stronger surface activity and lower critical micelle-like aggregation tendencies in mixed systems.  
  - Tend to show:
    - **Higher removal** from bulk water under the same conditions.
    - **Higher recovery**, because they more readily partition to the bubble interface.
    - **Higher enrichment factors**, since they concentrate more strongly into the foam phase.
  - In many, but not all, matrices this leads to **near-complete removal of longer-chain PFAAs** at relatively modest gas throughput, though actual degrees depend on matrix and operation.

- **Shorter-chain PFAS (e.g., C3–C6 PFAAs and many short-chain alternatives)**  
  - Much less surface active, more soluble, weaker tendency to accumulate on bubble surfaces.
  - Common patterns:
    - **Lower removal** for the same operational settings.
    - **Incomplete recovery** even when longer chains are almost fully recovered.
    - **Lower enrichment**, often only modestly above feed concentrations.
  - In some matrices, short-chain PFAS may require substantially higher gas volumes, multistage operation, or co-surfactant manipulation to achieve significant removal.

These trends are generally robust, but **quantitative values** depend on specific PFAS, water chemistry, and column design; without primary data, specific thresholds (e.g., which carbon number is “short” vs “long” in a given system) cannot be assigned.

### 2.2 Functional group and ionization state

PFAS headgroup chemistry affects:

- **Charge** (anionic vs zwitterionic vs cationic at a given pH).
- **Hydrogen bonding capacity and hydration shell**.
- **Affinity to bubbles, co-surfactants, and metal ions.**

Some key distinctions:

- **Perfluoroalkyl carboxylates vs sulfonates**  
  - Sulfonates of the same chain length are typically more surface active than carboxylates in simple systems.  
  - Result: sulfonates often show **higher removal and recovery** and **higher enrichment** than same-chain carboxylates at identical operating conditions, especially in low-organic, moderate-ionic-strength matrices.
  - In complex waters (high NOM, co-surfactants, or particulate matter), this relative advantage can be diminished or altered, depending on competitive adsorption and complexation.

- **Zwitterionic and cationic PFAS**  
  - Their net charge and speciation shift with pH and ionic strength.
  - They may interact strongly with NOM, mineral surfaces, or oppositely charged co-surfactants, forming complexes that can either:
    - Enhance apparent surface activity (if complexes are surface-active), or  
    - Suppress it (if complexes stay in bulk or are particle-bound).
  - Resulting **removal and recovery** behaviors can deviate strongly from classical PFAAs; direct extrapolation from anionic PFAAs is not justified without matrix-specific data.

- **Neutral and precursor PFAS (e.g., fluorotelomer alcohols, some sulfonamides)**  
  - Much more hydrophobic and often highly surface-active.  
  - They can show:
    - Very efficient **transfer into foam** (high recovery and enrichment) if present mostly in dissolved, unbound form.
    - However, their **transformation** (e.g., to PFAAs during aeration or storage) complicates mass balance and risk interpretation. Foam fractionation itself does not guarantee transformation; any observed change in speciation must be experimentally verified, not assumed.

### 2.3 Branching and molecular architecture

- Branched isomers, or PFAS with multiple perfluoroalkyl arms or ether linkages, may have:
  - Different surface packing efficiencies.
  - Different aggregation behaviors with NOM or co-surfactants.
- These subtleties can influence **relative removal and recovery among isomers**, but data are sparse and often system-specific. It is unsafe to generalize a single operational trend (e.g., “branching always reduces removal”) across all matrices.

---

## 3. Water chemistry effects

### 3.1 Co-surfactants (including non-fluorinated surfactants)

Non-fluorinated surfactants and other surface-active agents (e.g., detergents, biosurfactants, some NOM fractions) can drastically alter foam fractionation:

- **Competition at the gas–water interface**  
  - Strongly surface-active co-surfactants can occupy much of the available interfacial area.
  - Possible consequences:
    - **Decrease** in PFAS **enrichment**, because PFAS represent a smaller fraction of interfacial species.
    - Depending on conditions, **removal** may still be high if total interface is increased (e.g., higher foam stability), but **recovery** into foamate may be shared with non-PFAS organics.
    - Foam can be stabilized even when PFAS alone would not form persistent foam, indirectly enhancing PFAS capture but diluting the PFAS fraction within the foamate.

- **Mixed micelle or aggregate formation in bulk**  
  - Co-surfactants can form mixed micelles with PFAS, potentially **reducing free monomer activity** of some PFAS and thus reducing their gas–water interfacial accumulation.
  - This tends to **lower removal and recovery** at a given gas throughput, especially for shorter-chain PFAS that rely more on co-assembly for interfacial enrichment.

- **Foam quality and stability**  
  - Co-surfactants that stabilize small, persistent bubbles may:
    - Increase **interfacial area** and **contact time**, potentially enhancing PFAS capture (higher recovery).
    - Increase **water carryover** in the foam, which can **reduce enrichment** and **reduce volume reduction**.
  - In contrast, co-surfactants that cause large, unstable bubbles can:
    - Reduce **removal and recovery**, but
    - Yield **drier foam** with potentially higher **enrichment** of PFAS per foamate volume (if PFAS still partition effectively).

The impact is highly matrix- and formulation-specific; the same surfactant class could help or hinder PFAS fractionation depending on concentration, PFAS suite, and reactor operation.

### 3.2 Natural organic matter (NOM) and dissolved organic carbon (DOC)

NOM influences PFAS behavior via:

- **Bulk-phase association**  
  - Hydrophobic and electrostatic interactions can bind PFAS to colloidal or high-molecular-weight NOM.
  - If NOM-bound PFAS remain in the bulk, this can **decrease true interfacial PFAS activity**, leading to lower **removal, recovery, and enrichment**.

- **Surface activity of NOM itself**  
  - Some NOM fractions adsorb to bubble surfaces, forming organic coatings. These can:
    - Compete with PFAS for interface (lowering PFAS enrichment).
    - But also stabilize foam, potentially increasing overall gas–liquid contact and thereby partially offsetting competition.

- **Fouling and viscosity changes**  
  - High NOM can increase foam viscosity or promote stable, wet foams:
    - This may increase **water entrainment** and reduce **volume reduction**.
    - Mass balancing becomes harder: PFAS can be split between foamate, residual colloids in the treated water, and possibly stuck on column surfaces.

Effects observed in groundwater with low DOC can be quite different from those in landfill leachate or industrial wastewaters with high DOC and co-surfactants; extrapolation should always specify the type and level of NOM/DOC.

### 3.3 Salts and ionic strength

Ionic strength (e.g., NaCl, Ca2+, Mg2+, other salts) affects:

- **Electrostatic screening**  
  - Screening reduces repulsion among anionic headgroups at the interface, typically **enhancing PFAS surface activity** up to some limit.
  - Commonly leads to:
    - Improved **removal and recovery** for anionic PFAS at moderate salinities.
    - Potentially higher **enrichment**, if foam does not become excessively wet.

- **Specific ion effects and complexation**  
  - Divalent cations can complex with anionic PFAS or co-surfactants, sometimes forming surface-active ion pairs, but under other conditions may promote precipitation with NOM or minerals.
  - High salinity can change bubble size distribution and coalescence behavior.

- **High-salinity trade-offs**  
  - At very high salinity (e.g., brines), strong screening and density changes can:
    - Improve or deteriorate foam stability depending on co-contaminants.
    - Complicate **volume reduction** (foams may be extremely stable or collapse poorly).
    - Increase corrosion and scaling, creating operational constraints that indirectly affect achievable hydrodynamics.

Again, changes seen at modest ionic strength in relatively clean waters cannot be simply generalized to seawater or industrial brines.

### 3.4 Other constituents (metals, colloids, oils, particulates)

- **Metals and inorganic colloids**  
  - Multivalent metals can form complexes or precipitates with NOM, potentially sequestering PFAS in colloidal phases.
  - These phases may or may not be surface-active. In some cases they can be scavenged into foam, but in others they remain suspended and pass through.
  - This affects **recovery** and **mass balance closure**, as PFAS mass can be split between foam and non-dissolved phases.

- **Oils and hydrophobic organics**  
  - Oils are strongly surface-active and foam-forming; they can:
    - Dominate the interface, decreasing **PFAS enrichment**.
    - Drag PFAS along into the foam through partitioning into the oil-rich film, increasing **recovery** but complicating downstream management.

- **Suspended solids**  
  - Can dampen bubble coalescence or clog spargers, altering bubble size distribution and **gas–liquid contact time**.
  - Can also adsorb PFAS, providing competing sinks and complicating **mass balances**.

---

## 4. Reactor operation: hydrodynamics and process configuration

### 4.1 Gas flow rate and superficial gas velocity

Gas flow rate has multiple, often competing, impacts:

- **Higher gas flow / superficial velocity**  
  - Increases the number of bubbles and total interfacial area per unit time.
  - Typically:
    - Increases **removal rate** (faster decrease in PFAS concentration in the bulk).
    - Increases **total PFAS recovery** over a fixed treatment time, up to a point.
  - However:
    - Can produce **larger bubbles** (depending on sparger and liquid properties) and promote coalescence, which may decrease specific interfacial area per unit gas volume.
    - Often leads to **wetter foam**, increasing water entrainment into the foamate.

Implications for performance metrics:

- **Removal**: Usually improved initially with increasing gas flow, but can reach diminishing returns.
- **Recovery**: Often increases, but may plateau if bubble size/coalescence limit interfacial area.
- **Enrichment**: Can **decrease** with higher gas flow, because more water is carried into the foam and PFAS are spread over a larger foamate volume.
- **Volume reduction**: Typically **worsens** with high gas flow (larger foamate volume relative to treated water).
- These trade-offs are **strongly dependent on matrix**: in low-NOM waters, modest gas rates can yield dry foam and high enrichment; in surfactant-rich wastes, higher gas rates may simply generate large volumes of dilute foam.

### 4.2 Bubble size and interfacial area

Bubble size is controlled by sparger design, gas properties, surfactant levels, and column conditions:

- **Smaller bubbles**  
  - Higher interfacial area per unit volume of gas.
  - Longer residence times in the column for a given height (slower rise velocity).
  - Typically:
    - Improve **removal** and **recovery**, especially for less surface-active, short-chain PFAS.
    - Can increase foam stability; depending on co-constituents, this may yield more stable or wetter foam.

- **Larger bubbles**  
  - Lower interfacial area, faster rise.
  - Often:
    - Reduce **removal and recovery**, particularly for weakly surface-active PFAS.
    - Generate drier but more fragile foam; this can enhance **enrichment** when removal remains acceptable, but is often at the cost of incomplete PFAS removal from the bulk.

Because PFAS surface activity differs by chain length and headgroup, **the benefit of bubble-size reduction is PFAS- and matrix-specific**. For example, fine bubbles may provide substantial benefits for short-chain carboxylates in low-NOM water, whereas long-chain sulfonates in surfactant-rich matrices may already approach interfacial saturation with coarser bubbles.

### 4.3 Gas–liquid contact time and column residence time

Residence time is governed by column height, gas and liquid flow rates, and mixing:

- **Longer residence time (taller columns, lower superficial velocities, or recirculation)**  
  - Increases opportunities for PFAS to reach the interface and be transferred into rising bubbles.
  - Mostly improves **removal** and **recovery**, especially for slow-adsorbing or weakly surface-active PFAS.
  - However:
    - Returns can diminish once interfacial equilibrium or near-equilibrium is approached.
    - Very long residence times may encourage coalescence and drainage patterns that alter foam quality.

- **Short residence time**  
  - Limits interfacial contact; may achieve high **enrichment** from PFAS that are extremely surface-active (e.g., longer-chain sulfonates) because only the most surface-active fraction is captured.
  - But bulk **removal and recovery** can be poor for less surface-active PFAS.

Short-chain PFAS, zwitterions, or strongly NOM-bound PFAS often require **longer effective contact times** to achieve meaningful removal, whereas long-chain anionic PFAS can approach high removal at shorter times.

### 4.4 Liquid recycle and multistage operation

Recycle and staging offer ways to decouple removal from enrichment and volume reduction:

- **Liquid recycle (reintroducing partially treated water)**  
  - Increases the **cumulative exposure** of PFAS to bubbles without increasing column height.
  - Can significantly enhance **overall recovery and removal**, including for short-chain PFAS.
  - But:
    - May increase energy use and operational complexity.
    - Extends the time for possible transformation of precursors (positive or negative effects on risk).
    - Foam properties can drift over time as co-constituent concentrations change.

- **Multistage columns (serial or cascade)**  
  - Early stages may target bulk removal of highly surface-active PFAS with wetter foam (high recovery, modest enrichment, modest volume reduction).
  - Later stages can operate under conditions that favor **high enrichment** and **greater volume reduction** for the remaining lower-concentration PFAS.
  - This allows tailored trade-offs:
    - High **removal and recovery** overall.
    - Carefully controlled **enrichment** steps for downstream concentrate management.

Reported benefits of staging for one PFAS mixture or matrix cannot be assumed universal; the relative contribution of each stage depends on where each PFAS species sits on the surface activity spectrum in that specific water chemistry.

### 4.5 Foam collection strategy and foam “dryness”

Foam handling is central to translating interface partitioning into a usable separation:

- **Wet vs dry foam**  
  - **Wet foam** (high liquid content):
    - Larger foamate volumes (poor **volume reduction**).
    - Lower **enrichment** (PFAS mass diluted in more water).
    - Often associated with high gas rates or strong co-surfactant presence.
  - **Dry foam** (low liquid content):
    - Smaller foamate volume (better **volume reduction**).
    - Higher **enrichment**.
    - May require carefully controlled gas flow, bubble size, and column design to promote drainage.

- **Foam skimming vs overflow**  
  - Skimming at the top vs overflowing through standpipes influences:
    - The amount of entrained liquid dragged off with foam.
    - The effective “cut point” between drained liquid returning to the column and concentrate removed as foamate.
  - Poor foam collection can cause:
    - Underestimation of **recovery** (foam collapsing back into the bulk).
    - Poor **mass balance closure**, as PFAS remain in films adhering to internal surfaces.

- **Foam collapse methods (mechanical, thermal, vacuum)**  
  - Affect the degree to which:
    - Additional PFAS-laden liquid drains back to the main tank.
    - Volatile or semi-volatile PFAS (if present) might partition into the gas phase and potentially escape capture if not properly controlled.
  - Collapse strategy thus influences **recovery**, **enrichment**, and the form of the **residual stream** (e.g., concentrated liquid vs scum vs condensate).

### 4.6 Reactor configuration (batch, semi-batch, continuous, hybrid)

- **Batch fractionation**  
  - Fixed volume treated until target concentration is reached.
  - Allows clearer interpretation of **removal**, **recovery**, and **mass balance**, provided sampling is robust.
  - Better suited for mechanistic studies and parameter optimization.
  - Operationally limited in throughput; more useful for polishing or side-stream treatment than for very large flows.

- **Continuous flow**  
  - Constant feed and discharge; foamate collected continuously.
  - Performance is typically expressed at steady state.
  - Trade-offs:
    - Easier integration into full-scale treatment trains.
    - Harder to maintain consistent foam characteristics over time, especially with variable influent composition.
    - **Mass balance** can be more challenging; accurate accounting of transient behavior and internal holdup is needed.

- **Hybrid/staged configurations**  
  - May include pre-treatment units (e.g., pH adjustment, coagulants) before foam fractionation, or follow-on polishing units (GAC, ion exchange, advanced oxidation).
  - Each configuration leads to unique distributions of PFAS among streams:
    - Pre-treatment can remove or transform surfactants/NOM that otherwise suppress PFAS separation.
    - Post-treatment needs to handle residual PFAS and any newly formed species.

Because PFAS behavior is highly matrix-dependent, **operational “rules-of-thumb” from one configuration and matrix should not be assumed to hold in another without specific validation.**

---

## 5. Distinguishing performance metrics: interpretation and trade-offs

### 5.1 Removal vs recovery

- **Removal**:  
  - Defined as the **fractional decrease** in PFAS concentration in the treated water (influent vs effluent).
  - High removal indicates that PFAS have been transferred out of the main water phase.
- **Recovery**:  
  - Defined as the **fraction of initial PFAS mass captured in the foamate** (or other designated concentrate).

They are related but distinct:

- High **removal** with low **recovery** can occur if:
  - Significant PFAS mass is sorbed onto reactor surfaces, retained in stagnant zones, attached to solids, or volatilized (for some precursors).
- High **recovery** with modest **removal** can occur if:
  - Treatment time is short and only a fraction of the bulk volume has undergone effective contact, even though foamate is highly enriched.

In a well-designed foam fractionation system for non-volatile PFAS, removal and recovery should converge if mass balances are tight and non-foamate sinks are minimized.

### 5.2 Enrichment (concentration factor)

- **Enrichment** is the **ratio of PFAS concentration in foamate to that in feed water**.
- High enrichment:
  - Useful for creating a manageable, smaller volume for downstream destruction or disposal.
  - Does not by itself indicate high removal; a small foamate volume can be highly enriched while most PFAS mass remains in the bulk if recovery is low.
- Operational strategies that promote **dry foam** and **selective surface capture** often increase enrichment, sometimes at the expense of total recovery.

For short-chain PFAS, even modest enrichment can be meaningful if combined with high **recovery** and effective post-treatment of foamate.

### 5.3 Mass balance and total organofluorine

- Mass balance requires tracking PFAS in:
  - Feed water.
  - Treated water (post-fractionation).
  - Foamate (and any collapsed foam liquid).
  - Side streams (e.g., backwash, purge, condensate).
  - Potentially, internal deposition (scales, films) or volatilized fractions.

Challenges:

- Analytical coverage:  
  - Targeted PFAS lists rarely cover all PFAS present. Unmeasured PFAS (including precursors) can cause apparent mass loss or gain as they transform.
- Transformation vs redistribution:  
  - Aeration and prolonged residence can promote transformation of some precursors to terminal PFAAs.
  - Without direct evidence of carbon fate, **defluorination or mineralization must not be assumed**. Foam fractionation is, by design, a separation process; any observed changes in total organofluorine or specific PFAS patterns must be experimentally confirmed.

Robust mass balance is crucial to distinguish whether a given operational improvement in “removal” reflects genuine **transfer into foamate** or simply redistribution into unaccounted compartments.

### 5.4 Volume reduction

- **Volume reduction** describes how much the treated water volume exceeds the foamate volume.  
  - For example, treating 100 m³ of water and generating 0.1 m³ of foamate gives a 1000× volume reduction.
- It is not a direct indicator of removal or recovery:
  - A process can achieve excellent volume reduction (very small foamate volume) but poor removal/recovery if only a small fraction of PFAS is transferred.
  - Conversely, large foamate volumes (poor volume reduction) can correspond to excellent removal and recovery but pose challenges for downstream management.

Volume reduction interacts with **enrichment**:

- For a given recovered PFAS mass:
  - Higher enrichment requires either greater volume reduction or higher PFAS loading per unit foam volume.
- Matrix composition strongly influences how low foamate volume can go before foam stability breaks down or entrained water becomes dominant.

---

## 6. Practical trade-offs, residual streams, and scale-up considerations

### 6.1 Trade-offs among metrics and controls

Operational changes almost always involve compromise:

- Increasing **gas flow**:
  - Improves **removal** and often **recovery**, but can reduce **enrichment** and **volume reduction**.
- Driving towards **very dry foam**:
  - Improves **enrichment** and **volume reduction**, but may lower **recovery** if foam collapses prematurely or drainage sends PFAS back to the bulk.
- Optimizing for **short-chain PFAS**:
  - Requires more aggressive conditions (finer bubbles, higher gas volumes, longer residence, or staging), which can:
    - Increase energy and capital demands.
    - Magnify foaming problems if co-surfactants are abundant.
- Adjusting **salinity or adding co-surfactants** to boost PFAS surface activity:
  - May improve **removal and recovery**, but can increase complexity and cost of managing the resulting concentrate and complicate downstream treatment.

### 6.2 Residual streams and downstream management

Foam fractionation produces a **concentrated residual** that must be managed:

- **Foamate/concentrate**:
  - Contains most of the recovered PFAS mass plus co-enriched surfactants, NOM, salts, metals, and potentially oils.
  - Typically treated further by:
    - High-temperature destruction (incineration after dewatering or drying).
    - Advanced oxidation/reduction (electrochemical, plasma, etc.) on the concentrate.
    - Sorptive polishing (GAC/IX) before destruction.
  - The effectiveness and cost of these steps depend strongly on:
    - PFAS mixture (chain-length distribution, headgroups).
    - Co-constituent load (which can quench oxidants or foul electrodes/sorbents).

- **Off-gas and condensate**:
  - If any PFAS (especially volatile precursors) are stripped, they may appear in off-gas and subsequent condensate in gas-treatment systems.
  - These streams must be considered in **mass balance** and risk assessment; foam fractionation alone may not capture them.

- **Internal deposits or sludges**:
  - PFAS may accumulate on internal surfaces, in particulate sludge, or in scale.
  - Periodic cleaning or backwashing generates secondary waste streams that require characterization.

### 6.3 Scale-up limitations

Moving from bench/pilot to full scale reveals additional constraints:

- **Hydrodynamic similarity**:
  - Achieving the same bubble size, gas–liquid contact pattern, and foam behavior at large scale is non-trivial.
  - Scale-up may change:
    - Interfacial area distribution.
    - Residence time distribution.
    - Foam drainage patterns.
  - Consequently, performance for specific PFAS and matrices at lab scale may not translate linearly to full scale.

- **Variable influent composition**:
  - Real-world systems (landfill leachates, industrial effluents) exhibit strong temporal variation in PFAS composition, surfactants, NOM, and salinity.
  - Operational settings optimized for one condition may fail or produce excessive foaming under another.
  - Dynamic control strategies and real-time monitoring are largely underdeveloped.

- **Monitoring and analytics**:
  - Routine full-scale operation cannot yet rely on comprehensive PFAS speciation and total organofluorine monitoring, limiting how finely performance can be tuned.
  - Without robust, frequent measurement, optimizing multi-variable parameters (gas flow, recycle, staging) remains partly empirical.

---

## 7. Evidence gaps and research needs

Several areas warrant focused investigation:

1. **Structure–property–separation relationships**
   - Systematic studies across diverse PFAS structures (including ether PFAS, cationic/zwitterionic species, and novel alternatives) in controlled matrices to quantify:
     - Surface activity.
     - Adsorption kinetics to bubbles in the presence of realistic co-constituents.
   - Development of predictive models linking PFAS structure and water chemistry to expected foam fractionation performance.

2. **Co-surfactant and NOM effects under realistic conditions**
   - Multi-component, realistic mixtures in which multiple surfactants and high DOC are present.
   - Mechanistic understanding of when co-surfactants enhance vs suppress PFAS capture.
   - Better characterization of NOM fractions that most strongly impact PFAS behavior.

3. **Optimization for short-chain PFAS and precursors**
   - Identification of operational windows where meaningful removal of short-chain PFAS is achieved without unsustainable energy use or foam management issues.
   - Understanding of precursor transformation or redistribution during extended aeration, including carbon and fluorine fate.

4. **Advanced reactor configurations**
   - Multistage, counter-current, or hybrid foam fractionation designs tuned separately for:
     - Bulk removal (first stages).
     - High enrichment/volume reduction (later stages).
   - Integration with downstream destruction technologies, considering how foam fractionation–induced co-concentration of non-PFAS species affects destruction efficiency and byproduct formation.

5. **Full mass balances and total organofluorine tracking**
   - Systematic accounting of PFAS mass in all streams, including off-gas, solids, and internal deposits.
   - Use of total organofluorine metrics (with appropriate caveats) to detect unmeasured PFAS classes and potential transformation, always with care not to equate defluorination with mineralization without explicit carbon fate data.

6. **Control and automation for variable influent**
   - Development of process-control schemes that adjust gas flow, recycle, and foam collection in response to changing foaming behavior and surrogate indicators of surface activity.
   - Exploration of online proxies (e.g., conductivity, surfactant activity) to guide operation.

---

## 8. Concluding remarks

Foam fractionation is fundamentally a **structure- and matrix-sensitive separation** method for PFAS. Chain length, headgroup chemistry, co-surfactants, NOM, and salts all control how individual PFAS partition to gas–water interfaces and into foam. Reactor operation—gas flow, bubble size, residence time, recycle, foam collection, and configuration—then determines how that interfacial behavior is translated into distinct outcomes: **removal, recovery, enrichment, mass balance closure, and volume reduction**.

Because these performance metrics respond differently to operational changes, and because PFAS responses vary widely across structures and water matrices, careful, condition-specific evaluation is essential. Treating these metrics as interchangeable or assuming that trends observed for one PFAS class or matrix apply universally risks misdesign and misinterpretation. Addressing the highlighted evidence gaps, particularly for short-chain and emerging PFAS in realistic waters, will be key to making foam fractionation a predictable and optimizable component of PFAS treatment trains.

### 1. Scope and key message

This review focuses on how to *select* an adsorption medium for a given PFAS profile and water matrix, based strictly on the verified studies provided. All processes discussed are sorption-based phase transfer; none of the cited work demonstrates PFAS degradation, defluorination, or mineralization.

Across the evidence:

- Sorption strength increases with PFAS chain length on both activated carbons and ion‑exchange resins in the studied systems [WEB01, WEB03, WEB04, WEB06].
- PFAS functional group and resin/adsorbent chemistry strongly control selectivity and matrix sensitivity, particularly for:
  - Perfluoroalkyl carboxylates (PFCAs) vs sulfonates (PFSAs).
  - Long‑chain vs short‑chain PFAS.
- Background inorganic ions, pH, temperature, co‑contaminant PFAS, and matrix complexity all modulate performance.

The evidence supports **conditional** media-selection rules; no sorbent class is universally best.

---

### 2. Mechanisms and material properties vs PFAS structure

#### 2.1 Activated carbon (granular, powdered, colloidal)

**Chain-length dependence**

- Pulverized GAC in demineralized water showed systematically increasing Freundlich capacity (K_F) from PFBA to PFOA at 6 µg/L, indicating stronger sorption for longer PFCAs [WEB01-E01].
- In contaminated groundwater, PAC sorption coefficients (log K_iF) at ng/L levels were ≈4.0 for PFOS and ≈3.8 for PFOA, while GAC coefficients were lower (≈2.7 PFOS, ≈2.3 PFOA), again consistent with strong sorption of long-chain PFAS and stronger affinity on PAC than GAC [WEB04-E02].
- Colloidal activated carbon (CAC) in soil–water slurries showed higher distribution coefficients (Kd) for longer-chain PFAS and for FOSA (a sulfonamide), with non‑linear isotherms indicating stronger sorption at lower aqueous concentrations, particularly for longer chains [WEB06-E05].

**Functional group effects (PFCAs vs PFSAs vs sulfonamides)**

- Hansen et al. reported that K_iF increased with chain length and that chain‑length dependence was stronger for sulfonates than for carboxylates on activated carbon, though PFAS were not fully enumerated in the abstract [WEB04-E03].
- In the CAC system, FOSA and longer‑chain PFAS were most strongly removed (e.g., 99.8% removal for FOSA at 0.002 mmol/L in single‑solute tests, vs 41% minimum removal for PFOS at 0.05 mmol/L) [WEB06-E04]. This supports preferential uptake of more hydrophobic, neutral or less strongly hydrated species (e.g., FOSA) relative to high-charge-density PFSAs at higher concentration.
- These patterns imply that on carbonaceous media, **hydrophobic and π‑type interactions with the fluorinated chain and non‑polar groups** are important, with electrostatics superimposed but not dominant at the conditions studied.

**Material and configuration: PAC vs GAC vs CAC**

- At equal groundwater matrix and PFAS set, PAC showed higher sorption coefficients and much higher short‑contact-time removal (60–90% in 10 min) than GAC (20–40% in 10 min) [WEB04-E02, WEB04-E04]. This argues for:
  - **PAC** where high kinetic rates and short contact times are critical (e.g., rapid mixing, inline dosing).
  - **GAC** where fixed-bed operation and lower solids handling are prioritized, accepting lower short‑contact performance under similar conditions.
- CAC (PlumeStop) used at 0.2% w/w in soil–water slurries achieved a mean 77% ± 7.8% removal across seven PFAS in single‑solute systems and 67% ± 7.1% in mixtures [WEB06-E03]; maximum single‑solute removal was 99.8% (FOSA, low C0) and minimum 41% (PFOS at 0.05 mmol/L) [WEB06-E04]. CAC is thus effective as a **distributed sorbent phase in porous media**, but performance is concentration‑ and compound‑specific.

#### 2.2 Polymeric anion‑exchange resins (AERs)

**Chain length and resin functional group**

Lesmeister et al. systematically tested eight PFAAs (PFPrA–PFOA, PFBS–PFOS) on three polystyrenic AERs [WEB03-E01]:

- Adsorption affinity increased with PFAS alkyl chain length for all three resins [WEB03-E03].
- Across resins, affinity followed:
  - **A111 (weak‑base dimethylamine) < M600 (strong‑base dimethylethanolamine) < PSR2Plus (strong‑base PFAS‑selective with tributylamine)** [WEB03-E03].
- This ranking links **longer and more hydrophobic resin functional-group alkyl chains** and strong-base character to higher PFAS affinity. It is particularly relevant for short-chain PFCAs, which are difficult to capture on generic media.

**PFSA vs PFCA selectivity and pore structure**

Parvin et al. provide more detailed insight for one strong‑base resin (HPA25M) [WEB02]:

- In pure water with 100 mg/L PFOA, HPA25M reached an equilibrium capacity q_e of 931 mg/g (pseudo-second-order model) [WEB02-E02].
- In groundwater at the same nominal initial concentration, q_e for PFOA decreased to ~348 mg/g, while PFOS capacity remained high (~929 mg/g vs 1007 mg/g in pure water) [WEB02-E03].
- HPA25M had high porosity and a substantial fraction of 1–10 nm pores [WEB02-E04], and PFOS capacity in groundwater remained close to pure‑water values (~929 vs 1007 mg/g) [WEB02-E03].

Taken together, this indicates:

- Strong‑base, macroporous/mesoporous AERs with **1–10 nm pores** and hydrophobic backbone can maintain **very high PFOS capacities** even in competitive groundwater, while PFOA is more susceptible to matrix suppression.
- PFSA–selective behavior is consistent with the higher anionic charge density and potentially stronger electrostatic and hydrophobic interactions of PFOS.

**Mechanism (supported)**

- XPS/FTIR showed CF₂‑related peaks on AER surfaces after PFOS/PFOA adsorption, with strongest signals on HPA25M and PA312, supporting a mechanism of **electrostatic anion exchange plus hydrophobic interactions in resin pores** [WEB02-E05]. No transformation products were reported in the excerpts.

#### 2.3 Amine‑functionalized diatomite (APTES‑DE)

Bano et al. tested APTES‑functionalized diatomite granules in fixed‑bed configuration for PFOS and PFBS from aqueous solution [WEB07-E01]:

- Maximum removal efficiencies under optimized conditions were about 92.4% for PFOS and 89.9% for PFBS [WEB07-E02].
- Freundlich isotherms fit best, indicating heterogeneous, multilayer adsorption [WEB07-E02].
- The authors attribute performance to **positively charged amine groups** providing strong electrostatic attraction to anionic PFAS, supplemented by hydrophobic interactions especially for PFOS [WEB07-E04].

This medium therefore primarily leverages **surface amine charge and moderate hydrophobicity**; it functionally resembles a granular weak/strong‑base sorbent, but with a mineral backbone rather than a polymer.

---

### 3. Matrix and operating-condition effects

#### 3.1 Dissolved organic matter (DOM) and matrix complexity

Direct quantitative DOM effects are not reported in these excerpts. However:

- Parvin et al. observed a large drop in PFOA capacity on HPA25M from 931 mg/g in pure water to ~348 mg/g in groundwater at 100 mg/L, while PFOS capacity remained high (~929 mg/g) [WEB02-E02, WEB02-E03]. The reduction for PFOA is clearly a **matrix effect** (from co‑constituents in groundwater), even though specific competitors (DOM vs ions) are not resolved in the cited text.
- Several studies specifically note that NOM or complex matrices were *not* included in their batch systems—for example, Lesmeister et al. focused on inorganic anions in relatively simple solutions, not NOM [WEB03-E02], and Qian et al. worked in simple PFOS and PFOS–phosphate solutions [WEB05-E01].

For engineering decisions, this means:

- **Batch or column data in demineralized or “simple” solutions will overestimate capacity** in natural waters, particularly for PFCAs.
- The magnitude of suppression can differ strongly by PFAS class: PFOS capacities on a well‑designed AER can remain high in groundwater, while PFOA can be substantially reduced [WEB02-E02, WEB02-E03].

#### 3.2 Inorganic ions and anion competition

**Chloride and sulfate on AERs**

- In batch tests on A111, M600, and PSR2Plus, NaCl and Na₂SO₄ were varied jointly from 0.5 to 3.8 mM to represent typical drinking‑water anion levels [WEB03-E02].
- When both chloride and sulfate were present, **sulfate caused stronger inhibition of PFAA adsorption on all resins**, with adsorption of short-chain PFCAs (C3–C4) particularly sensitive [WEB03-E04].
- This pattern held across resin types (weak and strong base), though absolute affinity was highest for the PFAS‑selective PSR2Plus [WEB03-E03, WEB03-E04].

**Phosphate competition on PAC**

- Qian et al. studied PFOS adsorption on PAC in single‑solute and PFOS–phosphate binary systems [WEB05-E01]. While abstract excerpts do not give quantitative competition coefficients, they show:
  - Langmuir isotherms still fit PFOS adsorption in the presence of phosphate [WEB05-E03].
  - Thermodynamic signatures (positive enthalpy/entropy, negative Gibbs free energy) remained consistent with spontaneous, endothermic adsorption [WEB05-E03].
  - Higher temperature increased PFOS adsorption in both single and PFOS–phosphate systems [WEB05-E02, WEB05-E03].

The evidence supports that *common anions can significantly compete for ion‑exchange/charged sites*, especially for short-chain PFCAs on AERs, and for PFOS on PAC when phosphate is elevated, but carbonaceous sorbents retain substantial capacity.

**Divalent cations and background salts**

- CAC slurries were run in Milli‑Q water with 1 mM CaCl₂ at L/S 20 [WEB06-E02]. The presence of Ca²⁺ provided ionic strength and potentially influenced PFAS speciation and electrostatics, but specific effects vs no‑salt controls are not quantified.

#### 3.3 pH and temperature

From Qian et al. (PFOS on PAC in simple solutions) [WEB05]:

- **pH:** In single‑solute systems, PFOS adsorption decreased as pH increased [WEB05-E04].
- **Temperature:** Higher temperature increased PFOS adsorption in both single‑solute and PFOS–phosphate systems [WEB05-E02].
- **Thermodynamics:** Positive enthalpy and entropy with negative ΔG indicated spontaneous, endothermic adsorption [WEB05-E03].

These results support the generic guidance that:

- Adsorption of anionic PFAS to PAC is **stronger at lower pH** (greater electrostatic attraction/protonation of surface sites) and **favored by higher temperature** in these test ranges.
- However, the exact pH and temperature values are not given in the abstract, so numeric design targets cannot be inferred.

#### 3.4 Competing PFAS (mixture effects)

Niarchos et al. quantified competition in CAC–soil slurries [WEB06]:

- Average PFAS removal in single‑solute systems was 77% ± 7.8%; in the seven‑compound mixture it dropped to 67% ± 7.1%, i.e., about a 10% reduction in average removal [WEB06-E03].
- Extremes:
  - FOSA: 99.8% in single‑solute at 0.002 mmol/L and 99.8% in mixture at 0.0003 mmol/L [WEB06-E04].
  - PFOS: 41% in single‑solute at 0.05 mmol/L and 44% in mixture at 0.007 mmol/L [WEB06-E04].
- Kd values were higher for longer chains and FOSA, and sorption was often non‑linear, indicative of concentration‑dependent competition [WEB06-E05].

Thus, competition among PFAS reduces average removal, but **high‑affinity species (e.g., FOSA, longer chains) can still be almost completely removed at lower concentrations**, whereas higher‑concentration PFOS is more poorly captured.

#### 3.5 Influent concentration and scale

Concentration regimes in the evidence span:

- **Trace levels (ng/L):** PAC/GAC sorption coefficients for PFOS and PFOA in contaminated groundwater; n ≈ 0.5, indicating non‑linearity [WEB04-E02, WEB04-E03].
- **Low µg/L:** GAC pilot treating groundwater with short-chain PFCAs; performance reported as bed volumes to 10% breakthrough [WEB01-E03, WEB01-E04].
- **High mg/L:** AER batch tests at 100 mg/L PFOA/PFOS [WEB02-E01–E03].

Across this span:

- Non‑linear Freundlich behavior (n ≈ 0.5) on activated carbon implies **much higher K_d at lower concentrations** [WEB04-E03].
- Very high capacities reported for HPA25M at 100 mg/L (e.g., 931 mg/g for PFOA in pure water, ~348 mg/g in groundwater, 1007/ ~929 mg/g for PFOS) [WEB02-E02, WEB02-E03] are *upper‑bound capacities* at high loading, not directly transferable to ng/L design without applying non‑linear isotherm fits.
- For GAC in pilot groundwater, breakthrough behavior clearly depends on PFAS chain length even at environmental levels: 10% breakthrough at about 6,000–23,000 bed volumes for PFBA–PFOA [WEB01-E03], with corresponding loadings of roughly 2.4–29 µg/g [WEB01-E04].

---

### 4. Translating evidence into conditional media-selection criteria

Below, “media” refers to the *adsorbent class + configuration* (e.g., PAC slurry, strong‑base AER column). All recommendations are conditional on PFAS composition, matrix, and operating conditions.

#### 4.1 Define your PFAS profile

Based on the evidence, key distinctions for selection are:

1. **Dominant PFAS class**
   - Long-chain PFSAs (e.g., PFOS).
   - Long-chain PFCAs (e.g., PFOA).
   - Short-chain PFCAs (C3–C6; e.g., PFBA, PFPeA, PFHxA).
   - Short-chain PFSAs (e.g., PFBS).
   - Neutral/precursor-type compounds (e.g., FOSA).

2. **Concentration regime**
   - Regulatory‑level ng/L in drinking water.
   - µg/L–low mg/L (typical of impacted groundwater or treatment residuals).
   - High mg/L (industrial wastewaters or experimental systems; e.g., 100 mg/L in Parvin et al. [WEB02]).

3. **Mixture complexity**
   - Single dominant PFAS vs diverse mixture.
   - Presence of strongly adsorbing species (PFOS, FOSA) alongside short-chain PFCAs.

#### 4.2 Define your water matrix

Key matrix dimensions supported by the evidence:

- **Groundwater with natural inorganic background** (Riegel GAC/IEX pilot; Parvin AER groundwater) [WEB01, WEB02].
- **Synthetic/simple solutions with controlled anions** (Lesmeister AERs, Qian PAC, Bano APTES‑DE) [WEB03, WEB05, WEB07].
- **Soil–porewater–CAC system (barrier or in situ treatment)** [WEB06].
- **Contaminated groundwater at trace PFAS with minimal lab manipulation** (Hansen PAC/GAC) [WEB04].

You should explicitly characterize or at least bracket:

- Dominant anions (Cl⁻, SO₄²⁻, PO₄³⁻).
- Ionic strength (approximated by major cations/anions).
- Presence/absence of significant DOC/NOM (not quantified in the excerpts, but likely important).
- pH range and temperature.

#### 4.3 Conditional selection: drinking water / groundwater treatment

**Case A: Groundwater with short- to mid‑chain PFCAs (C4–C8), modest NOM, and “typical” inorganic background**

Evidence: Riegel pilot GAC vs weak‑base IEX D5706 on the same contaminated groundwater [WEB01-E03, WEB01-E05].

- In the 1 m GAC column at 7.5 m/h, 10% breakthrough bed volumes (approximate) increased with PFCA chain length:
  - PFBA ~6,000 BV; PFPeA ~11,000 BV; PFHxA ~16,000 BV; PFHpA ~20,000 BV; PFOA ~23,000 BV [WEB01-E03].
- Corresponding GAC loadings at 10% breakthrough ranged from roughly 2.4 µg/g (PFBA) to 29 µg/g (PFOA) [WEB01-E04].
- In the weak‑base IEX column (EBCT 2.4–6 min), 10% breakthrough occurred at about 4,000 BV for PFBA, ~10,000 BV for PFPeA, and ~25,000 BV for PFHxA [WEB01-E05].

**Implications:**

- Under this specific water chemistry:

  - For **very short-chain PFBA**, GAC gave longer EBCT‑normalized run (≈6,000 BV) than weak-base IEX (≈4,000 BV) [WEB01-E03, WEB01-E05].
  - For **intermediate PFPeA**, run lengths were similar (≈11,000 BV GAC vs ≈10,000 BV IEX).
  - For **PFHxA**, weak‑base IEX substantially outperformed GAC (~25,000 vs ~16,000 BV) [WEB01-E03, WEB01-E05].

- Conditional design guidance:

  - If your regulated targets are dominated by **C6 and above PFCAs**, and your matrix resembles this groundwater (moderate inorganic strength, some NOM), **weak‑base AER (like D5706)** may give longer run lengths per bed volume, especially for C6.
  - If **PFBA is a key driver**, **GAC** may be preferable under similar conditions, as it gave longer run length for PFBA in this study [WEB01-E03, WEB01-E05].
  - For **mixed C4–C8 PFCA profiles**, a **dual‑media or staged GAC + AER configuration** could be justified: GAC first for broader removal including PFBA, followed by AER polishing for residual C6–C8.

**Case B: Groundwater with PFOS/PFOA at elevated mg/L (e.g., remediation streams)**

Evidence: HPA25M and related strong‑base AERs at 100 mg/L in pure water and groundwater [WEB02].

- HPA25M q_e for PFOA:
  - 931 mg/g in pure water; ~348 mg/g in groundwater [WEB02-E02, WEB02-E03].
- PFOS q_e on HPA25M:
  - 1007 mg/g in pure water; ~929 mg/g in groundwater [WEB02-E02, WEB02-E03].

**Implications:**

- For **high‑strength PFOS streams**, a **strong‑base macroporous AER like HPA25M** can maintain **very high capacity even in groundwater**, making it a strong candidate for primary treatment or polishing after other steps.
- For **PFOA at similar levels**, the same resin experiences substantial matrix‑induced capacity loss; you may need:
  - Higher resin dose or more frequent regeneration.
  - Additional upstream conditioning (e.g., softening, anion reduction; not quantified here).
  - Complementary media (e.g., carbon) to share loading.

**Case C: Low‑concentration PFOS/PFOA polishing at ng/L–µg/L**

Evidence: PAC vs GAC in contaminated groundwater [WEB04].

- For PFOS and PFOA, log K_iF were about 4.0/3.8 on PAC, 2.7/2.3 on GAC, with n ≈ 0.5 [WEB04-E02, WEB04-E03].
- Short (10 min) contact led to 60–90% removal with PAC vs 20–40% with GAC [WEB04-E04].

**Implications:**

- For **polishing applications with short contact times** (e.g., post‑treatment barrier for PFOS/PFOA), **PAC** dosed into a contactor can achieve substantially higher removal per contact time than GAC in batch.
- This must be weighed against:
  - Solids handling and PAC separation requirements (settling, filtration).
  - Production of PAC‑rich residual sludge.

A reasonable strategy is:

- **GAC fixed beds** for baseline PFAS reduction and NOM control.
- **Intermittent or continuous PAC dosing** for short‑term response or polishing for PFOS/PFOA spikes, particularly when adding new GAC basins is impractical.

#### 4.4 Conditional selection: surface water or waters with elevated sulfate/chloride

When sulfate is significant (0.5–3.8 mM range typical of Lesmeister tests [WEB03-E02]):

- AERs (A111, M600, PSR2Plus) all exhibit **stronger inhibition of PFAA adsorption by sulfate than by chloride**, particularly for short-chain PFCAs (C3–C4) [WEB03-E04].
- Among these:
  - **PSR2Plus**, with tributylamine groups, has the highest affinity across PFAS and is PFAS‑selective [WEB03-E03].
  - **M600** (dimethylethanolamine) is intermediate.
  - **A111** (dimethylamine) is lowest [WEB03-E03].

**Implications:**

- In **high‑sulfate drinking waters** where short-chain PFCA removal is critical, prefer **PFAS‑selective or strongly hydrophobic strong‑base resins (like PSR2Plus or M600)** over weak‑base AERs.
- Be prepared for **reduced capacity and earlier breakthrough** for C3–C4 PFCAs due to inorganic competition—design EBCT and bed volume allowances accordingly, and consider sulfate reduction upstream if feasible.

#### 4.5 Conditional selection: industrial or engineered systems with simple matrices

**PFOS or PFBS in synthetic waters (e.g., industrial effluents after pretreatment)**

Evidence: APTES‑DE in fixed‑bed tests [WEB07].

- Achieved ~92.4% PFOS and ~89.9% PFBS removal under optimized conditions in aqueous solution [WEB07-E02].

**Implications:**

- For **single‑PFSA‑dominated, relatively clean streams** (e.g., PFOS from a point source with limited NOM), an **amine‑functionalized mineral medium** can provide high removals and be regenerated with modest capacity loss over at least five cycles (~4.6% loss for PFOS, ~3.6% for PFBS after the fifth cycle) [WEB07-E03].
- At this stage, evidence does not support extrapolating this material’s performance to:
  - Complex matrices with significant NOM or multivalent metals.
  - Other PFAS classes.

A cautious use case is as a **polishing or specialty medium in controlled industrial settings**, with pilot verification in real effluents.

#### 4.6 Conditional selection: in situ or ex situ soil/plume stabilization

Evidence: Soil–CAC slurries [WEB06].

- CAC at 0.2% w/w with low‑organic soil (0.6% OC) and 1 mM CaCl₂ achieved:
  - Average 77% removal across seven PFAS in single‑solute tests (0.002–0.05 mmol/L).
  - Average 67% removal in a seven‑PFAS mixture.
  - Strong sorption of FOSA and longer‑chain PFAS (FOSA 99.8% removal at low C0; PFOS 41–44% at higher C0) [WEB06-E03, WEB06-E04].
- Kd generally increased with chain length and for FOSA, with non‑linear isotherms [WEB06-E05].

**Implications:**

- For **in situ plume stabilization or ex situ soil flushing** where PFAS are in the µM range and soil organic carbon is low, CAC offers meaningful reductions across multiple PFAS, especially longer chains and sulfonamides.
- However:
  - Removal of high‑concentration PFOS is incomplete under the tested dose and conditions.
  - Competition in mixtures reduces average removal by ~10% compared to single‑solute systems [WEB06-E03].

Designers should therefore:

- Adjust CAC dose based on desired residual levels and specific PFAS of concern.
- Recognize that **CAC is a stabilization/containment tool**, not a polishing medium to sub‑ng/L; a downstream water treatment train may still be needed.

---

### 5. Trade‑offs, residual streams, and scale‑up limitations

Across all studies:

- PFAS are **removed by adsorption/partitioning**, not transformed or destroyed, and no inorganic fluoride release is reported in the excerpts. All media will generate PFAS‑laden residuals (spent GAC/PAC, resins, CAC‑amended soils, or APTES‑DE) requiring safe management.

Key trade‑offs:

1. **Capacity vs matrix robustness**
   - Strong‑base, highly porous AERs (e.g., HPA25M) maintain high PFOS capacities in groundwater but show significant PFOA capacity loss relative to pure water [WEB02-E02, WEB02-E03].
   - PFAS‑selective resins (PSR2Plus) can have highest intrinsic affinity but are more sensitive to sulfate for short-chain PFAS [WEB03-E03, WEB03-E04].

2. **Kinetics vs handling**
   - PAC offers higher apparent sorption coefficients and rapid removal (60–90% in 10 min vs 20–40% for GAC) [WEB04-E04], but introduces slurry handling and solid–liquid separation challenges.
   - GAC and fixed‑bed resins simplify operation but require larger vessels or longer EBCT to achieve similar performance.

3. **Regeneration and durability**
   - APTES‑DE granules retained most capacity over five adsorption–desorption cycles (≈3.6–4.6% performance loss) [WEB07-E03], suggesting feasible regeneration for PFOS/PFBS in simple matrices.
   - Resin regeneration is not detailed in the available AER studies, and CAC in soil is typically intended as a long‑term immobilization rather than a regenerable medium.

4. **Selectivity vs breadth of capture**
   - PFAS‑selective resins (PSR2Plus) maximize removal per bed volume for targeted PFAAs but may over‑optimize for a narrow suite of PFAS.
   - GAC/PAC provide broad but less selective capture across PFAS (and co‑contaminants like NOM), with pronounced chain-length dependence [WEB01, WEB04, WEB06].

---

### 6. Evidence gaps and priority research areas

The current evidence base leaves several important gaps for engineering design:

- **DOM/NOM effects on AERs and functionalized mineral sorbents.** Most AER and APTES‑DE tests relied on pure water or simplified matrices; systematic NOM competition at environmentally relevant DOC has not been quantified in the provided literature.
- **Trace‑level performance of AERs and APTES‑DE.** Parvin et al. worked at 100 mg/L PFOA/PFOS [WEB02-E01], far above drinking‑water levels; capacities and breakthrough behavior at ng/L–µg/L remain uncertain.
- **Comprehensive PFAS mixtures including emerging PFAS and precursors.** Lesmeister et al. cover eight PFAAs [WEB03-E01], and Niarchos et al. cover seven PFAS including a sulfonamide [WEB06-E02], but many short‑chain PFAS and precursors are absent.
- **Dynamic column data under high-sulfate and high‑phosphate conditions.** Existing data are batch-based [WEB03, WEB05]; direct fixed‑bed breakthrough tests in realistic high‑anion matrices would greatly reduce uncertainty.
- **Scale-up of CAC systems.** Soil–slurry experiments [WEB06] provide a good mechanistic base, but translating to in situ barriers requires field-scale trials, hydraulic transport studies, and long‑term monitoring.
- **End‑of‑life treatment of spent media.** None of the cited studies address destruction or safe stabilization of PFAS‑loaded sorbents, though this is central for lifecycle risk management.

---

### 7. Practical engineering workflow for media selection

Based on the above evidence and caveats, an engineer designing a PFAS adsorption step should:

1. **Characterize inflow PFAS and matrix** (profile, concentration band, major anions, pH, DOC).
2. **Map the case to analogous evidence domains**:
   - Short-chain PFCAs in groundwater → Riegel GAC/IEX pilot [WEB01].
   - PFOS/PFOA in groundwater, high C0 → Parvin AERs [WEB02].
   - PFOS/PFOA at ng/L levels → Hansen PAC/GAC [WEB04].
   - Multi‑PFAS mixtures in low‑DOC porewater → Niarchos CAC [WEB06].
   - PFOS/PFBS in simple industrial streams → Bano APTES‑DE [WEB07].
   - High sulfate/chloride with PFAAs → Lesmeister AERs [WEB03].
   - PFOS with elevated phosphate and variable pH/T → Qian PAC [WEB05].
3. **Screen media classes conditionally**:
   - Choose **strong‑base, hydrophobic AERs or PFAS‑selective resins** where long‑chain PFAS (especially PFOS) dominate and inorganic competition is moderate.
   - Choose **GAC/PAC** where:
     - Mixed PFAS with significant short-chain content must be captured broadly, and
     - NOM and organic co‑contaminants must also be controlled.
   - Consider **specialized media** (APTES‑DE, CAC) for:
     - In situ stabilization or soil systems (CAC) [WEB06].
     - Single‑PFSA dominant and relatively clean industrial effluents (APTES‑DE) [WEB07].
4. **Refine choice with matrix sensitivity**:
   - If sulfate or phosphate are high, adjust upward the safety factors for AER capacity and consider PAC or hybrid beds.
   - If pH is high, anticipate reduced PFOS sorption on PAC based on Qian et al. [WEB05-E04].
5. **Pilot under representative conditions** before full‑scale deployment, paying attention to:
   - Breakthrough curves by PFAS class.
   - Competing anion profiles.
   - Regeneration feasibility and residual handling.

This conditional, matrix‑aware approach—rather than assuming a single “best” adsorbent class—aligns with the available evidence and avoids over‑generalization beyond what the cited studies support.

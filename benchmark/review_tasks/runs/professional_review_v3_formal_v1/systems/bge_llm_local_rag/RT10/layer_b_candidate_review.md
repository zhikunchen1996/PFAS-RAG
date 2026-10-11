## 1. Overview: Why matrix effects must be explicitly engineered and reported

Across the evidence base, the same treatment process behaves very differently in clean laboratory water versus real waters that contain natural organic matter (NOM/EfOM), surfactants, inorganic ions, co‑contaminants, and biological solids. Yet matrix conditions are often inadequately characterized, or varied without matched controls.

The studies here span adsorption (ion exchange, GAC, biochar, specialty media), physical separation (coagulation/filtration, foam fractionation, electrocoagulation, RO), and destructive processes (ultrasonication, non‑thermal plasma, UV–sulfite, electrochemical oxidation), in matrices from buffered Type 1 water to tap water, surface water, wastewaters, seawater, and contaminated groundwater. They collectively show that:

- Matrix effects are highly **mechanism‑ and PFAS‑specific**; the same constituent (e.g., Ca²⁺, NOM) can promote or inhibit treatment depending on process and PFAS structure.
- Clean‑water performance generally **overestimates** field performance unless matrix composition is controlled or explicitly accounted for.
- Many “degradation” studies measure **parent loss only**, not defluorination or mineralization.

Below I synthesize how specific matrix components affect PFAS treatment and then propose a minimum framework for designing and reporting matrix‑representative experiments.

---

## 2. Organic matter and surfactants: competition, pore blockage, and indirect biological effects

### 2.1 Ion exchange and GAC adsorption

**Reference NOM and EfOM**

A set of carefully controlled ion‑exchange (IX) and GAC isotherm studies is particularly informative.

- In DI water, a strong‑base polyacrylic anion‑exchange resin removed PFOA and PFOS effectively at environmentally relevant ng–µg/L levels [R01]. When 5 mg C/L of reference NOM isolates (SRNOM, SRFA, PLFA, SRHA) were added, PFOA/PFOS uptake decreased, and simultaneous DOC uptake demonstrated **direct competition** for exchange sites [R01].
- For the same resin, **NOM characteristics** mattered: higher molecular‑weight, more humic isolates (e.g., SRHA) caused stronger performance deterioration and violated key assumptions of the equivalent background concentration (EBC) model, consistent with **pore blockage and size‑exclusion** in addition to competition [R01].
- When the same resin was applied to microfiltered/ultrafiltered secondary effluent and synthetic wastewaters at ~5 mg C/L DOC, PFAS removal and model behavior again reflected competition from EfOM and inorganic ions, but individual contributions could not be decoupled because ions and EfOM were not varied independently [R01].

For GAC (Filtrasorb 400), Abulikemu et al. developed a standardized Type 1 water baseline and then imposed matrix modifications stepwise [R02]:

- In **NOM‑free buffered Type 1 water**, single‑species isotherms gave higher PFAS qe than multispecies isotherms, showing **competitive sorption among PFAS** themselves [R02].
- Adding NOM (co‑loaded with PFAS) reduced PFAS qe; when NOM was **preloaded** onto GAC, percent qe differences became more negative, especially for PFHxS, PFOS, and PFNA, consistent with NOM filling pores and blocking PFAS access, not just competing for surface sites [R02].
- The same NOM plus CaSO₄ further modulated qe (see Section 3.2), illustrating that “organic matter effects” cannot be interpreted without ionic context.

**Direction of effect**

- For IX and GAC, at the DOC levels tested (5 mg C/L), NOM/EfOM effects are consistently **inhibitory** to PFOA/PFOS uptake, but the **magnitude** of inhibition depends on NOM type (humic vs fulvic, molecular‑weight distribution) and PFAS structure (e.g., PFHxS and PFOS more strongly affected than some others) [R01, R02].
- Preloading NOM onto media (simulating aged filters) produces **stronger inhibition** than co‑loading, implicating pore blockage as a distinct mechanism [R02].

### 2.2 Organic matter in real and synthetic wastewaters

When moving from synthetic NOM waters to real wastewaters, matrix complexity increases and effects become less quantifiable but still clearly inhibitory for adsorption:

- In a PFAS/Cd(II) adsorption study, PFAS removal in groundwater (Brittany, France) remained similar to or better than in Milli‑Q water, whereas removal declined substantially in two laundry wastewaters from Gard, France, particularly for PFOA [R03]. The authors attributed this to **dissolved organic matter competitively occupying adsorption sites**, with reduced PFOA sorption more pronounced than PFOS or GenX [R03].
- The same work shows that even in wastewater, PFOS and PFOA can reach capacities of ~16.1 and 7.7 mg/g, respectively, on AC/wood biochar, but those values are lower than in cleaner matrices and do not resolve individual contributions of NOM vs other co‑solutes because matrix characterization is summarized only in a separate table [R03].

### 2.3 Biological organic matter and surfactant‑like PFAS: coagulation and membrane fouling

Organic matter can also mediate **indirect matrix effects** via biological responses.

- Chen et al. spiked PFOS or PFOA (0.1–10 µg/L) into a real surface water (algae‑containing drinking‑water source) and observed that at 0.1 µg/L:
  - Floc size after PACl coagulation increased 1.6‑fold vs the PFAS‑free control [R04].
  - UF flux declined by >10% relative to the control, indicating **increased membrane fouling** [R04].
- Parallel algal toxicity assays in buffered suspensions (C. pyrenoidosa) showed PFOS/PFOA‑induced oxidative stress (increased ROS, shifts in SOD/CAT and glutathione system, lipid peroxidation) and cell damage [R04]. The authors link this to increased secretion of extracellular polysaccharides, which then change floc structure and membrane fouling, rather than PFAS directly accumulating on the membrane [R04].

Here, low‑level PFOS/PFOA in a **natural organic/biological matrix** produced a **promotive effect on coagulation (larger flocs)** but an **inhibitory effect on downstream UF (fouling)**. That trade‑off would not be observable in PFAS‑only DI water.

### 2.4 AFFF/FF and surfactant mixtures in degradation processes

In destructive treatments, the water matrix includes **PFAS‑rich surfactant mixtures** themselves:

- UV–sulfite treatment of diluted AFFF in laboratory water showed that PFOS and PFOA were degraded by 98% and 93% as parent compounds, but shorter‑chain PFSAs (PFHxS, PFPeS, PFBS, PFPrS) initially increased due to precursor transformation [R05]. The work explicitly noted that results were generated in “well‑defined laboratory water matrices,” and future work is needed for natural waters with eₐq⁻ scavengers such as NO₂⁻/NO₃⁻ and AFFF co‑contaminants [R05].
- Ultrasonication of concentrated AFFF and foam fractionate (FF) spiked into Milli‑Q and creek water (CW) yielded apparent defluorination >100%, while seawater (SW) showed lower defluorination (72% and 81% for AFFF and FF) [R06]. Apparent >100% defluorination reflects **complex mixture chemistry and mass‑balance artifacts**, not true mineralization [R06]. Organic constituents in AFFF/FF thus both supply PFAS and alter cavitation and interfacial partitioning.

### 2.5 NOM and specialty adsorbents in field systems

A field‑scale canal filtration system with specialty media (CPS, ZIPGEM) illustrates how **uncontrolled NOM and co‑ions confound interpretation**:

- Short‑ and long‑chain PFAS removal efficiencies were **negatively correlated with proton concentration** (i.e., removal decreased as pH decreased), with stronger sensitivity for short‑chain PFAS, interpreted as protonation of media and NOM sites suppressing electrostatic adsorption and cation bridging [R07].
- Correlations indicated that increasing effluent ammonia (NH₄⁺) and proton exchange among DOC, ammonium, and media functional groups affected surface charge and PFAS adsorption; short‑chain PFBA/PFBS showed relatively stable removal, while other PFAS exhibited desorption events [R07].

Because DOC composition and inorganic ions were not systematically varied, these interpretations are necessarily indirect.

---

## 3. Inorganic ions, ionic strength, and cations: multiple, mechanism‑dependent roles

### 3.1 GAC adsorption: ionic strength and divalent ions

In buffered Type 1 water, Abulikemu et al. varied **ionic strength and CaSO₄** at fixed temperature and GAC type [R02]:

- Decreasing ionic strength from 10 to 2 mM **substantially increased qe by 79–146%** for PFAS, relative to the 10 mM condition [R02]. Here, higher ionic strength is **inhibitory**, likely via compression of electrostatic interactions and competition from background ions.
- At constant ionic strength, adding Ca²⁺/SO₄²⁻ (as CaSO₄) **increased qe by 43–140%** [R02]. This promotive effect is consistent with:
  - Ca²⁺ acting as a bridge between negatively charged PFAS and deprotonated GAC surface sites.
  - Possible salting‑out effects that increase hydrophobic interactions.

These experiments show that **ionic strength and divalent ions cannot be lumped** into a single “salt effect.” The sign and magnitude depend on how they are introduced (changing I vs swapping monovalent for divalent cations) and on the underlying adsorption mechanism.

### 3.2 Ion exchange: inorganic ions vs EfOM

For IX, inorganic ions were included implicitly:

- In synthetic and real wastewaters, the EBC model was extended to include EfOM and inorganic ions as co‑sorbates [R01]. The authors note previous work where inorganic anions can be strong competitors at the same resin, and in this study they model competition from EfOM plus inorganic ions together rather than as separate terms [R01].
- Because inorganic ion concentrations were not varied independently, **their individual effect remains partially confounded with EfOM** in this dataset.

### 3.3 Electrolytes in foam fractionation

In foam fractionation (FF) with laboratory‑spiked water (no explicit NOM), Wang et al. varied inorganic electrolyte concentration (2–20 mM) at fixed air flow [R08]:

- PFAS removal efficiency for PFOA, 6:2 FTS, and PFOS **increased with electrolyte addition**, while enrichment factors in the foam remained mostly unchanged [R08].
- The authors attribute this promotive effect to:
  - Salts strengthening foam by preventing bubble coalescence and film drainage, reducing PFAS return to the bulk solution.
  - Reduced electrostatic repulsion of PFAS headgroups, allowing closer packing at the air–water interface and enhanced interfacial adsorption [R08].

Here, increasing ionic strength **promotes** separation by stabilizing foam and altering surfactant packing—a different mechanism from adsorption onto solids.

### 3.4 Ionic background in ultrasonication

In the ultrasonication study, ionic composition played almost the opposite role:

- Individual PFAS and AFFF/FF showed highest defluorination in **Milli‑Q and creek water**, with ranges of 47–86% and 28–85%, respectively, but only 2.3–56% in synthetic seawater for individual PFAS and 72–81% for AFFF/FF [R06].
- High salinity in SW is proposed to:
  - Increase cavitation threshold, requiring higher acoustic intensity to form bubbles.
  - Alter bubble growth/collapse dynamics and radical generation.
  - Potentially change PFAS and radical distribution at the bubble–water interface [R06].

In creek water, TOC (including humic substances) might **accumulate at the bubble–water interface and enhance PFAS accumulation there**, partly compensating radical scavenging and yielding defluorination similar to Milli‑Q [R06].

Thus, **high salinity is strongly inhibitory for ultrasonication defluorination**, while moderate TOC in low‑salinity water can have a net neutral or even promotive effect under certain conditions.

### 3.5 Non‑thermal plasma in distilled water vs groundwater

For NTP treatment:

- PFOA in distilled water with air bubbling showed >50%, ~70%, and ~90% parent loss at 10, 30, and 60 min, largely independent of initial concentration (0.1–10 µg/L) [R09].
- In real groundwater containing multiple PFAS (total 0.520 µg/L) plus unspecified co‑contaminants, overall PFAS parent loss was ~50% at 10 min and slightly >70% at 60 min—substantially lower than distilled‑water removal under nominally similar reactor settings [R09].
- The study notes that the **chemical and physical properties of PFAS‑contaminated groundwater can vary greatly** across sites, and does not provide detailed ionic composition in the excerpt [R09].

Given the lack of matched ionic‑strength and co‑contaminant controls, we can say only that the composite groundwater matrix **inhibited parent loss relative to distilled water**, but not which constituents were responsible.

### 3.6 Cation adsorption and PZC shifts in field media

Field‑exposed specialty adsorbents showed clear **matrix‑induced surface‑charge shifts**:

- After exposure in canal water, the PZC of ZIPGEM shifted from 8.5 to 9.5 and that of CPS from 7.2 to 7.8, attributed to adsorption of cations (notably Ca²⁺) onto media [R07].
- The authors caution that PZC measured in simple electrolytes (H⁺/OH⁻ as only potential‑determining ions) may be misleading for predicting PFAS adsorption in real waters [R07].

This underscores that **inorganic ions can change media properties over time**, altering PFAS adsorption behaviour relative to clean‑water characterizations.

---

## 4. Co‑contaminants and PFAS–PFAS interactions

### 4.1 Metal co‑contaminants: synergistic and antagonistic effects

In batch adsorption with carbonaceous sorbents in DI or Milli‑Q water:

- At 10 mg/L each PFAS and 10 mg/L Cd(II), Cd(II) **enhanced PFOS and PFOA sorption** onto activated carbon and wood biochar, but **inhibited GenX sorption** [R03].
- The authors interpret this as:
  - For PFOS/PFOA: synergistic interactions (possibly via complexation or charge‑balancing) that favour co‑adsorption.
  - For GenX: competition for adsorption sites due to structural differences and weaker hydrophobicity [R03].

This is a clear **interactive matrix effect** between metal ions and PFAS that depends on PFAS class (sulfonate vs carboxylate vs ether carboxylate).

### 4.2 PFAS–PFAS competition on adsorbents

Several studies demonstrate **competitive adsorption among PFAS**:

- Multispecies GAC isotherms in Type 1 water had lower qe than single‑species isotherms [R02].
- GAC and biochar capacities for PFOA, PFOS, and GenX in mixed systems follow PFOS > PFOA > GenX across matrices, emphasizing that less strongly sorbing species (e.g., GenX) may experience earlier breakthrough or lower uptake in competitive environments [R03].
- GAC pilot data in contaminated groundwater show desorption of short‑chain PFAS such as PFBA and even PFOA as higher affinity PFAS displace them, producing C/C₀ > 1 (chromatographic effect) [R10].

### 4.3 Mixture dynamics in non‑thermal plasma

In NTP‑treated **binary PFOA/PFOS mixtures** in distilled water:

- Mixture degradation dynamics were “constrained by PFOA,” meaning PFOS degradation in the mixture followed the slower behaviour of PFOA rather than its faster single‑compound kinetics [R09].
- This suggests negative **kinetic interference**: co‑presence of a more recalcitrant PFAS can slow removal of a more labile one under NTP conditions.

### 4.4 Co‑contaminants in electrochemical and AO–MBR–RO systems

In electrochemical DDW proof‑of‑concepts, some non‑PFAS FOCs were chemically degraded with fluoride production, whereas PFAS in tap water were removed mainly by electrocoagulation (phase separation) [R11]. The tap‑water matrix—containing background ions and co‑solutes—shifted the dominant mechanism from degradation to physical removal.

In the full‑scale AO–MBR–RO WWTP, many **co‑contaminants** are present, though not detailed in the excerpts. Observed PFAS behaviour—e.g., PFOS spikes post‑AO, PF4OPeA enrichment in sludge and persistence through RO—reflects a combination of:

- Sorption and separation (sludge vs aqueous).
- Precursor transformation during biological and sludge‑line treatment [R12].

However, without speciation of co‑contaminants, specific interactive effects cannot be separated from general matrix complexity.

---

## 5. Distinguishing inhibitory, promotive, neutral, and interactive effects by mechanism and PFAS properties

The evidence shows that **no single matrix constituent has a universal effect**; impacts depend on both PFAS properties and treatment mechanism.

### 5.1 Adsorptive and separation processes

**Inhibitory effects**

- **NOM/EfOM**: consistently decreases PFOA/PFOS uptake on IX and GAC (and biochar) via site competition and pore blockage, especially for humic, high‑MW NOM; effects are stronger for some PFAS (PFHxS, PFOS, PFNA) [R01, R02, R03].
- **Higher ionic strength (for GAC)**: increasing ionic strength from 2 to 10 mM reduced qe (i.e., high I was inhibitory) [R02].
- **Short‑chain PFAS in EC and GAC**: PFBA remains poorly removed (~20% efficiency) in EC systems where longer‑chain PFAS are almost completely removed [R11]; short‑chain PFAS also desorb earlier from GAC columns [R10].

**Promotive effects**

- **Ca²⁺ and SO₄²⁻ at constant ionic strength**: increased GAC qe by 43–140% [R02].
- **Foam‑stabilizing electrolytes**: increasing electrolyte concentration in FF improved PFOA/6:2 FTS/PFOS removal by stabilizing foam and allowing closer surfactant packing [R08].
- **Low levels of PFOS/PFOA in algal surface water**: increased floc size during coagulation (potentially beneficial for clarification) [R04].

**Neutral or mixed effects**

- **TOC in creek water for ultrasonication**: despite TOC, CW defluorination of PFOA and other PFAS was similar to Milli‑Q for individual PFAS, suggesting that humic accumulation at bubble interfaces may counteract radical scavenging under the tested conditions [R06].

**Interactive effects**

- **Cd(II) co‑contamination in adsorption**: enhances PFOS/PFOA sorption but inhibits GenX; PFAS effects on Cd(II) uptake are also concentration‑dependent [R03].
- **NOM preloading vs co‑loading**: shifts mechanism from mostly competition to combined competition and pore blockage, with larger negative impacts on qe for certain PFAS [R02].
- **Ammonia, pH, and DOC in field media**: PFAS removal correlated negatively with proton and ammonium concentration, with short‑chain PFAS more sensitive to pH‑driven changes in media charge and cation‑bridging capacity than long‑chain PFAS [R07].

### 5.2 Degradation processes

**Inhibitory effects**

- **High salinity (SW) for ultrasonication**: strongly reduces defluorination of individual PFAS and AFFF/FF relative to Milli‑Q and CW [R06].
- **Real groundwater matrix for NTP**: lowers PFAS parent‑loss efficiency relative to distilled water; co‑contaminant composition is not resolved but is clearly important [R09].

**Promotive or conditional effects**

- **Moderate TOC in low‑salinity CW**: CW defluorination comparable to Milli‑Q, possibly via enhanced PFAS concentration at bubble interfaces [R06].
- **Air bubbling in NTP**: reduces conductivity increase and improves PFOA removal in distilled water; high conductivity without bubbling is associated with worse performance [R09].

**Interactive effects**

- **Transformation vs removal balance**:
  - UV–sulfite of AFFF in lab water converts precursors to PFOS/PFOA and other PFSAs/PFCAs; mass‑balance across parent, transformation products, total fluorine, and fluoride shows that parent loss alone overestimates mineralization [R05].
  - Ultrasonication defluorination rates were consistently lower than overall PFAS removal, indicating persistent fluorinated intermediates and incomplete mineralization in MQ/SW/CW and real GW [R06].

Crucially, several degradation studies—including NTP and some ultrasonication datasets—refer to “degradation” but report only **parent concentration loss** without full fluorine/carbon balances [R09, R06]. For matrix‑effect work, these endpoints must be labelled explicitly (parent‑loss vs defluorination vs mineralization) to avoid conflating improved separation with actual destruction.

---

## 6. Recommended minimum framework for matrix characterization and matched controls

Given the heterogeneity and sometimes ambiguous matrix definitions in the current literature, it is difficult to quantitatively translate clean‑water performance to real waters without additional experiments. The studies that most clearly isolate matrix effects share several design features:

- **Well‑defined baseline matrix** (e.g., Type 1 or Milli‑Q water with known buffer and ionic composition) [R02, R03].
- **One‑factor‑at‑a‑time matrix modifications** (e.g., ionic strength, pH, Ca²⁺/SO₄²⁻, NOM) at fixed treatment conditions [R02, R08].
- **Parallel real‑water tests** (groundwater, wastewaters, environmental waters) run under the same operating conditions as baselines to quantify net matrix penalties [R03, R08, R09].

Building on these, a **minimum matrix‑characterization and control framework** for defensible cross‑study comparison should include:

### 6.1 Matrix characterization

At a minimum, for each experimental matrix (clean, synthetic, or real), report:

1. **Bulk water chemistry**
   - pH and temperature.
   - Ionic strength and major ions (at least Na⁺, Ca²⁺, Mg²⁺, Cl⁻, SO₄²⁻, alkalinity); if limited, report at least Na⁺, Ca²⁺, and SO₄²⁻ where cation‑bridging or foam/sonochemical processes are studied [R02, R08, R06, R07].
   - Conductivity and, where relevant, background oxidants/scavengers for radical‑based processes (e.g., NO₃⁻, NO₂⁻ for UV–sulfite) as highlighted by Tenorio et al. [R05].

2. **Organic carbon and biota**
   - DOC (mg C/L) and, if possible, characterization of NOM/EfOM type (e.g., reference isolates vs real EfOM vs AFFF background organics) [R01, R02, R03, R12].
   - Presence of algae or biomass where relevant, including approximate cell density and species, because biological responses (e.g., polysaccharide secretion) can modulate treatment outcomes [R04].

3. **PFAS speciation and concentration**
   - Individual PFAS concentrations and totals (ΣPFAS), stating whether “total PFAS” is a simple sum of monitored analytes [R12, R09, R10].
   - Presence of known precursors or PFAS classes (e.g., PFSAs, PFCAs, PFECAs, FTS) [R05, R12].

4. **Other co‑contaminants**
   - Concentrations of key **co‑sorbates** (e.g., Cd(II) in adsorption studies [R03]) and **co‑reactants** (e.g., surfactants, AFFF, co‑solvents).
   - For field samples (e.g., contaminated groundwater, WWTP effluents), provide at least a summary table of major organics and inorganics, and refer to it explicitly when interpreting matrix effects [R03, R12, R09].

### 6.2 Matched‑control design

To translate results beyond clean water without conflating separation and destruction, designs should incorporate the following **matched controls and comparisons**:

1. **Clean‑water benchmark vs real water under identical operating conditions**
   - Use a **standardized Type 1 or Milli‑Q matrix** as a baseline for adsorption isotherms or degradation kinetics [R02, R03, R06].
   - For each real water tested (groundwater, wastewater, environmental sample), rerun the **same PFAS spike levels, contact time, treatment intensity, and media dose** used in clean water [R03, R08, R09].
   - Explicitly report **relative performance changes** (e.g., percent qe loss, percent removal loss, fold‑change in rate constants) rather than only absolute capacities or final concentrations.

2. **One‑parameter‑at‑a‑time matrix variation**
   - To isolate specific matrix effects, vary one factor (e.g., pH, ionic strength, Ca²⁺, NOM loading) while holding others fixed, as in:
     - FF electrolyte series at fixed air flow [R08].
     - GAC isotherms across pH and ionic strength with constant PFAS loading and GAC type [R02].
   - For complex matrices, complement these with **synthetic analogues** that reproduce key features (e.g., same DOC and Ca²⁺ but simplified inorganic background) to deconvolve effects.

3. **Preloading vs co‑loading scenarios for NOM and co‑sorbates**
   - Implement **NOM‑preloaded media** vs NOM‑co‑loaded experiments to disentangle direct competition from pore blockage [R02].
   - When co‑contaminants such as metals or surfactants are present, perform:
     - PFAS‑only and metal‑only controls.
     - Mixed PFAS+metal tests at the same total ionic strength and media dose, to quantify interaction terms (synergy vs competition) [R03].

4. **Controls for physical separation vs chemical destruction**
   - For processes that can both separate and transform PFAS (e.g., EC, NTP, ultrasonication, UV–sulfite), distinguish among:
     - **Removal from the treated phase** (e.g., PFAS load in sludge/foam/brine/precipitate) [R11, R08, R12].
     - **Parent‑compound loss** in the solution phase [R06, R09, R05].
     - **Defluorination** (fluoride release relative to PFAS fluorine content) [R06, R05].
     - **Total fluorine and carbon fate** where feasible [R05].
   - At minimum, design parallel experiments that:
     - Quantify parent PFAS in all relevant phases (water, solids, foam, brine).
     - Measure fluoride (and, ideally, total organofluorine) to separate destruction from mere phase transfer.

5. **Field–lab linkage**
   - When interpreting field systems (GAC pilots, field filtration cells, full‑scale WWTPs), **anchor interpretation** in laboratory tests using site water (e.g., batch isotherms or kinetic tests with the actual groundwater or effluent) under controlled conditions [R10, R01].
   - Avoid generalizing laboratory clean‑water data to real water without:
     - Matching matrix composition where possible (e.g., 5 mg C/L DOC in synthetic NOM chosen to match recycled wastewater DOC [R01]).
     - Explicitly quantifying how qe or removal differs between DI and real matrices.

### 6.3 Reporting conventions for comparability

To enable robust cross‑study comparison, reports should:

- **Define endpoints explicitly**:
  - “Removal” or “separation” should refer to mass transfer from one phase to another (e.g., aqueous to solids, foam, brine).
  - “Parent‑compound loss” should be reserved for reduced parent PFAS concentration in the relevant phase.
  - “Defluorination” must be backed by fluoride measurements relative to PFAS fluorine content [R06, R05].
  - “Mineralization” should not be claimed without carbon‑fate data.

- **Normalize to relevant denominators**:
  - Adsorption: report qe (mg/g) along with PFAS speciation, co‑solutes, and the mass of competing sorbates (DOC, metals) [R03, R01, R02].
  - Separation: report both percent removal and enrichment factors (e.g., FF foam enrichment) [R08].
  - Degradation: report both parent‑loss and defluorination percentages, and, where AFFF/FF or real waters are used, clarify which PFAS are monitored vs unquantified precursors [R06, R05].

- **Quantify uncertainty and model limitations**:
  - Note where models (EBC, IAST, dose‑response) fit poorly in particular matrices (e.g., SRHA) and explicitly connect this to hypothesized mechanisms such as pore blockage [R01, R02].
  - When machine‑learning models aggregate heterogeneous NF/RO datasets with diverse matrices, acknowledge that modeled “matrix effects” are statistical, not controlled comparisons [R13].

---

## 7. Priority research gaps

The assembled evidence highlights several specific needs:

1. **Systematic ion–NOM–PFAS interaction studies.** Existing work often varies NOM or ions but not both in a factorial design. Experiments that systematically combine NOM type, DOC level, ionic strength, and divalent cations could better map regions where NOM inhibition is partially offset by Ca²⁺‑bridging, as hinted for GAC [R02] and field adsorbents [R07].

2. **Short‑chain and emerging PFAS.** Short‑chain PFAS and PFECAs (e.g., GenX, PFBA, PF4OPeA) are consistently more mobile and less strongly adsorbed [R03, R11, R10, R12], but matrix‑dependent removal data remain sparse. Future studies should prioritize short‑chain PFAS in matrix‑effect designs rather than focusing mainly on PFOS/PFOA.

3. **Bridging laboratory defluorination to real matrices.** Ultrasonication and NTP show promising defluorination/removal in clean waters, but high salinity and complex co‑contaminants in real waters substantially inhibit performance and complicate mass balance [R06, R09]. Carefully matrix‑matched controls and comprehensive fluorine balances are needed to determine when these technologies deliver true mineralization vs partial transformation.

4. **Scaling adsorption results to breakthrough.** Bench isotherms in Type 1 water or simplified matrices must be translated to full‑scale column behaviour using mechanistic or well‑validated empirical models that incorporate competition, desorption, and mass‑transfer limitations, as highlighted by Croll et al. [R10] and Abulikemu et al. [R02].

5. **Matrix‑aware machine learning for membranes.** ML models aggregating NF/RO data acknowledge pH, ionic ions, and PFAS concentration as key inputs, but the underlying dataset has diverse, often poorly harmonized matrices [R13]. Future modeling should either (i) standardize matrix descriptors across studies or (ii) generate targeted datasets where water quality is varied under controlled membrane and PFAS conditions.

---

### 8. Concluding remarks

The studies reviewed here demonstrate that water‑matrix constituents can **promote, inhibit, or qualitatively change** PFAS treatment mechanisms, and that these effects are tightly coupled to PFAS chemistry and process physics. Without explicit matrix characterization and matched‑control designs, it is not scientifically defensible to extrapolate clean‑water performance to real waters or to compare technologies across studies.

A common experimental and reporting framework—centered on standardized baselines, one‑factor‑at‑a‑time matrix variations, parallel real‑water tests, and clear endpoint definitions—would greatly improve our ability to design, select, and scale PFAS treatments for the varied matrices encountered in practice.

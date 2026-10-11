## 1. Overview: Why matrix effects must be designed into PFAS treatment studies

Across the extracted studies, PFAS removal and degradation differ markedly between simplified aqueous solutions and more complex waters containing organic matter, surfactants, inorganic ions, and co-contaminants. These matrix constituents influence:

- **Physical separation** (adsorption, coagulation, nanofiltration/RO) by changing PFAS partitioning, electrostatic interactions, competition for sorbent sites, and fouling.
- **Degradation/destruction** (sonolysis, VUV/Fe, UV–persulfate, cold plasma) by scavenging or generating reactive species, altering radical speciation, or shifting pathways and byproducts.

The evidence base is heterogeneous and often qualitative, but it is sufficient to derive *principled guidance* on how matrix effects should be tested and reported so that performance in clean water is not misinterpreted as field-relevant.

---

## 2. Matrix effects on physical separation processes

### 2.1 Organic matter and surfactants

#### Adsorption to activated carbon and nanosorbents

Multiple studies show **inhibitory effects of dissolved organic matter (DOM/NOM)** on PFAS adsorption:

- **GAC (Filtrasorb 400):** Natural organic matter reduced equilibrium PFAS capacities; this negative effect was *partially mitigated* when Ca²⁺ and sulfate were present at constant ionic strength, consistent with competitive sorption/pore blocking by NOM and charge screening by divalent ions [R01, R01]. This is explicitly a *matrix–mechanism interaction* (competition + electrostatics).
- **Multispecies conditions:** Competitive isotherms with co-occurring PFAS and other solutes yielded lower capacities than single-solute isotherms [R01], showing that even PFAS themselves act as “matrix competitors.”
- **Groundwater with TOC:** In CAC systems, total organic carbon had the strongest negative impact on **long‑chain PFAA** adsorption when individual solutes were added to unimpacted groundwater [R02, R02].
- **Short-chain PFAA:** The same groundwater work reports additive inhibitory effects from *multiple* solutes on short‑chain PFAA adsorption to CAC [R02, R02], implying that short chains are more sensitive to matrix complexity.

**Surfactants** can be particularly disruptive:

- For CAC, addition of an AFFF surfactant (diethylene glycol butyl ether) at 10–100 mg/L decreased PFOS and PFOA adsorption, indicating strong inhibition by surfactants [R03, R03].
- In surfactant-enhanced coagulation, a cationic surfactant is used intentionally to form PFAS–surfactant–coagulant assemblies and improve removal from surface water [R04, R04, R04]. Here, the surfactant is *promotive* relative to a coagulation baseline, but would almost certainly be *inhibitory* if evaluated as a competitor in a carbon or resin system.

For **nanoscale sorbents**, batch tests and columns with polyethyleneimine-coated iron oxide nanocrystals show that:

- Solution pH, ionic composition/strength, and NOM all “significantly modulate” PFOA/PFOS sorption performance [R05, R05].
- In bench‑scale columns, NOM and competing ions decreased breakthrough times (earlier PFAS breakthrough) compared with matched clean-water columns [R05, R05].

Taken together, organic matter and surfactants:

- **Inhibit adsorption** to GAC/CAC and many resins by:
  - Direct competition for hydrophobic pores or electrostatic sites.
  - Fouling or pore blocking.
- **Promote separation** in surfactant-enhanced coagulation by creating PFAS-rich aggregates that can be removed physically [R04].

These effects are strongly **mechanism-dependent** (adsorbent type, charge, hydrophobicity) and **PFAS-structure-dependent** (short vs long chain), so they cannot be generalized across technologies.

#### Coagulation/flocculation

In real surface water, conventional coagulation/flocculation removes some PFAS, primarily via partitioning into flocs or associated solids [R04]. When a cationic surfactant is added:

- PFAS removal by coagulation/flocculation improves relative to the no-surfactant baseline on the same matrix [R04, R04].
- The mechanism is attributed to electrostatic and hydrophobic interactions among PFAS, surfactant, and bulk organic matter [R04].

**Matrix implication:** bulk organic matter, normally treated as a nuisance for adsorption, becomes an active participant in surfactant–PFAS–coagulant complexes for coagulation-based separation.

### 2.2 Inorganic ions and ionic strength

#### Monovalent background electrolyte / ionic strength

Ionic strength often modulates electrostatic interactions:

- **Filtrasorb 400 GAC:** Reducing ionic strength from 10 to 2 mM increased equilibrium PFAS capacities by ~79–146% [R01, R01], indicating that higher ionic strength was **inhibitory** to adsorption.
- **CAC (PFOS/PFOA):** In contrast, increasing ionic strength from 1–100 mM **increased** PFOS and PFOA affinity to CAC [R03, R03].

These opposite trends highlight that:

- For **hydrophobically dominated CAC**, screening of repulsive electrostatics and “salting-out” may enhance PFOS/PFOA adsorption.
- For **GAC with different surface chemistry and PFAS mix**, increased ionic strength may reduce adsorption via competition for charged sites or altered PFAS speciation.

Therefore, *ionic strength cannot be assigned a universal inhibitory or promotive role*; its effect is conditional on sorbent surface charge, PFAS speciation, and whether hydrophobic vs electrostatic interactions dominate.

#### Divalent cations and specific ions

- **Ca²⁺ with CAC:** Increasing Ca²⁺ to 2 mM enhanced PFOS/PFOA affinity to CAC [R03, R03] — a *promotive* effect, likely via charge screening/bridging on negatively charged carbon surfaces.
- **Ca²⁺/sulfate with GAC:** In GAC systems, Ca²⁺ and sulfate partially offset NOM-induced capacity loss at constant ionic strength [R01, R01], again indicative of charge screening / aggregation effects.
- **CaCl₂ competition on carbons/resins:** In a short‑/ultrashort‑chain PFAS adsorption study, added CaCl₂ caused an average ~20‑fold decrease in adsorption of three PFAS [R06, R06]. Here Ca²⁺ is **strongly inhibitory**, presumably because it competes for charged sites on anion exchange resins and/or alters PFAS hydration and approach to the surface.

For **anion exchange resins in fixed beds**:

- DOM and major inorganic anions (bicarbonate, chloride, sulfate, nitrate) systematically reduced uptake capacity KIX relative to cleaner matrices, particularly for shorter‑chain and ether PFAS [R07, R07, R07]. DOM and inorganic anions act jointly as inhibitors via competitive electrostatics and steric effects.

#### Membranes (NF/RO)

For nanofiltration and RO:

- PFAS rejection is often high (>95% in many cases), but **complex matrices with higher ionic strength and DOC generally reduce rejection** compared with clean laboratory solutions [R08, R08, R08].
- Mechanisms: electrostatic repulsion and pore-size exclusion dominate; matrix-induced changes in pH, ionic strength, and organic fouling alter surface charge and effective pore size [R08, R08].

Thus, inorganic ions and DOC act as **indirect inhibitors** of PFAS separation by modifying membrane surface properties or fouling layers, rather than directly competing for “sites” in the same way as for sorbents.

### 2.3 Organic co-solutes and co-contaminants

Several studies directly introduce **non-PFAS organic co-contaminants**:

- **CAC + benzene/TCE:** Benzene (0.5–4.8 mg/L) and TCE (0.5–8 mg/L) reduced PFOS adsorption, with PFOS adsorption decreased about twenty‑fold at the highest TCE level, while PFOA effects ranged from neutral to slightly **promotive** [R03, R03]. This is a clear example of:
  - Strong **competitive inhibition** for PFOS.
  - Matrix-induced **PFAS‑specific behavior** (PFOA not similarly inhibited).
- **NOM + Ca²⁺/sulfate:** As above, NOM reduces adsorption, while Ca²⁺/sulfate partially mitigate that inhibition [R01, R01].
- **DOM and phosphate vs GAC/IX:** A competitive-adsorption study (GAC vs strong-base IX) reports that:
  - DOM causes “pronounced inhibition and displacement” of PFAS on GAC.
  - The ion-exchange resin maintains higher PFAS selectivity but is more susceptible to **phosphate-induced displacement** [R09, R09, R09].
- **Mixed PFAS:** Multispecies PFAS conditions systematically reduce observed capacities relative to single-solute cases [R01, R09, R01, R09].

**Key point:** Co-solutes can be strongly inhibitory for one PFAS and neutral or even slightly promotive for another under identical conditions [R03]. Competitor effects must therefore be interpreted *at the PFAS‑structure level*, not just at the “total PFAS” level.

### 2.4 Complex matrices and hybrid trains

When moving from controlled lab solutions to **real waters and conditioned matrices**, several patterns emerge:

- **Wastewater effluent adsorption:** Elevated effluent organic matter and other background constituents “negatively impact” PFAS adsorption by GAC and IX [R10, R10]. When wastewater effluent is first treated by nanofiltration to reduce PFAS, effluent organic matter, and selected inorganic ions, downstream GAC/IX show improved PFAS removal and delayed breakthrough relative to direct adsorption of raw effluent [R10, R10, R10]. NF here acts as a **matrix-conditioning step**.
- **Groundwater vs synthetic waters:** For CAC barriers in groundwater, major ions and dissolved organic solutes “strongly affect adsorption, particularly for short-chain PFAA,” and thereby control barrier longevity [R11, R11, R11].

In all these cases, treatment performance **cannot** be extrapolated from clean water alone; performance in real matrices deviates in direction and magnitude depending on which solutes dominate.

---

## 3. Matrix effects on degradation and destruction processes

### 3.1 Sonolysis with carbonate radicals

A well-controlled sonochemical PFOA study provides clear clean‑water vs matrix‑modified comparisons:

- **Clean water (no carbonate):** At 150 W and 40 kHz with or without N₂ saturation, PFOA degradation after 4 h was <25% [R12, R12]. This establishes a **low‑efficiency baseline** in a simplified matrix.
- **With NaHCO₃ (carbonate radicals):**
  - At ~30 mM NaHCO₃ under N₂ saturation and pH ~8.7, PFOA underwent “complete degradation” within 4 h [R12, R12, R12] — a **strongly promotive matrix effect** on parent loss.
  - Defluorination was greatly increased, with no detectable shorter‑chain perfluorocarboxylic acids and near‑complete conversion of organofluorine to inorganic fluoride [R12, R12, R12].
  - The authors interpret this as “near-complete mineralization to fluoride,” but the direct evidence is defluorination and absence of shorter-chain acids. Carbon fate is not fully resolved; thus the measured endpoint is **extensive defluorination**, not fully demonstrated mineralization.

Here, the **matrix constituent (carbonate)** is both a radical precursor and a scavenger. Under the specific conditions used, its net effect is strongly **promotive** for both degradation and defluorination, illustrating that an inorganic ion frequently considered inhibitory in other AOPs can be beneficial in sonochemistry.

### 3.2 VUV/Fe(III) photodecomposition: anion and oxidant effects

In VUV/Fe(III) systems:

- **Inorganic anions (HCO₃⁻, SO₄²⁻, NO₃⁻, Cl⁻, ClO₄⁻):**
  - These hinder PFOA defluorination in the order HCO₃⁻ > SO₄²⁻ > NO₃⁻ ≈ Cl⁻ > ClO₄⁻ [R13, R13].
  - This reflects **inhibitory** effects via scavenging of reactive species, particularly strong for carbonate and sulfate.
- **Persulfate addition:** In the same VUV/Fe(III) configuration, persulfate inhibited PFOA defluorination relative to persulfate‑free conditions [R13, R13]. This is notable because persulfate is usually an oxidant; here, it acts as a **negative matrix modifier**, altering radical speciation so that net defluorination decreases.

This study shows that:

- The same inorganic anion (carbonate, sulfate, chloride) can be *promotive* or *inhibitory* in different advanced oxidation configurations.
- Oxidants themselves (persulfate) can act as matrix interferents when superimposed on another AOP (VUV/Fe).

### 3.3 UV–persulfate AOP: chloride and carbonate as co-ions

The UV–persulfate PFOA study systematically examines water samples with different co‑ions:

- **Degradation and defluorination/mineralization:** PFOA destruction is analyzed via pseudo‑first‑order kinetics, degree of defluorination (fluoride release) and degree of mineralization (organic carbon to inorganic) across water samples and co-ion conditions [R14, R14].
- **Chloride and carbonate:** QR (quenching‑rate) analyses quantify how chloride and carbonate “inhibit sulfate‑radical reactions” and thereby slow PFOA degradation in realistic matrices [R14, R14].
  - PFOA degradation rate decreased in the presence of chloride [R14, R14], an **inhibitory** effect linked mechanistically to sulfate-radical scavenging.
  - Carbonate species similarly quench sulfate radicals, decreasing degradation efficiency [R14, R14].

Thus, in UV–persulfate systems, common anions (chloride, carbonate) are **inhibitory co‑solutes**, in contrast to their promotive role in carbonate‑radical sonolysis.

### 3.4 Cold plasma processes: water matrix and co-solutes

Two cold‑plasma PFAS studies provide complementary evidence:

#### Dielectric barrier discharge (DBD) and bubble plasma (PFOA)

- Matrix composition influences dominant reactive species and degradation pathways; certain ions and organics act as **scavengers that decrease PFOA removal**, whereas other conditions favor stronger oxidative environments [R15, R15, R15].
- While specific constituents are not named in the snippets, the qualitative pattern is that real-matrix ions and organics often **inhibit** PFOA degradation by consuming key radicals.

#### Cold atmospheric pressure plasma jet (PFAS in multiple waters)

- PFAS degradation was evaluated in deionized water, tap water, and a synthetic effluent under **identical plasma conditions** [R16, R16, R16].
- In real waters (tap + synthetic effluent), overall PFAS degradation dropped to about 8–50% under the same operating conditions, substantially lower than in deionized water [R16, R16].
- Transformation products and residual species profiles differed among matrices, indicating matrix‑dependent reaction networks [R16, R16].

Cold plasma thus exhibits **strongly matrix‑sensitive degradation performance**:

- Simpler matrices (e.g., deionized water) support higher apparent PFAS loss.
- Real waters with co-solutes shift both **extent of parent loss (inhibited)** and **byproduct spectrum**.

### 3.5 Summary of degradation matrix effects

Across sonolysis, VUV/Fe, UV–persulfate, and plasma:

- **Carbonate**:
  - *Promotive* in carbonate‑radical sonolysis (enhanced PFOA degradation/defluorination) [R12].
  - *Strongly inhibitory* in UV–persulfate via sulfate-radical quenching [R14].
- **Chloride**:
  - Inhibits UV–persulfate degradation via sulfate-radical scavenging [R14].
  - Has less pronounced, but still inhibitory, effect on VUV/Fe defluorination compared with carbonate and sulfate [R13].
- **Organic matter and unidentified organics**:
  - In plasma and photochemical systems, organics often **scavenge reactive species**, lowering PFAS degradation and altering byproduct profiles [R13; R15; R16; R16].
- **Oxidants (persulfate) as co-solutes**:
  - Can be **inhibitory** in VUV/Fe(III) [R13], reinforcing the need to consider oxidant–matrix interactions rather than assuming monotonic benefits.

These findings underscore that **no single inorganic or organic constituent can be assigned a universal effect** on PFAS degradation; effects are mechanism‑specific.

---

## 4. Distinguishing inhibitory, promotive, neutral, and interactive effects

### 4.1 Adsorption and separation processes

Using the studies above, effects can be categorized *conditional on mechanism and PFAS properties*:

- **Inhibitory effects**
  - NOM/DOM on GAC and CAC: reduced capacities (competition, pore blocking) [R01; R02].
  - AFFF surfactant on CAC: decreased PFOS/PFOA adsorption [R03].
  - DOM and co‑solutes on GAC/IX in wastewater: reduced adsorption performance [R10].
  - High ionic strength on GAC: ~79–146% lower capacity compared with lower ionic strength [R01].
  - CaCl₂ in short‑chain PFAS systems: ~20‑fold decrease in adsorption of three PFAS [R06].
  - Co-contaminants benzene/TCE: up to ~20‑fold reduction in PFOS adsorption, while PFOA not comparably inhibited [R03].

- **Promotive effects**
  - Increased ionic strength and Ca²⁺ promoting PFOS/PFOA adsorption to CAC [R03].
  - Ca²⁺ and sulfate mitigating NOM inhibition on GAC adsorption [R01].
  - Cationic surfactant addition enabling improved PFAS removal via coagulation/flocculation in surface water compared with no surfactant [R04, R04].

- **Neutral or weak effects**
  - For PFOA in the presence of benzene/TCE at certain levels, matrix effects ranged from neutral to slightly **promotive**, even though PFOS was strongly inhibited under the same conditions [R03].
  - pH changes around 7.7–9 produced only modest GAC capacity shifts (up to ~19%) in one study [R01, R01] — a *weak inhibitory* effect.

- **Interactive effects**
  - NOM plus Ca²⁺/sulfate: negative NOM effect partly canceled by divalent cations [R01].
  - Mixed groundwater solutes causing additive inhibition for short‑chain PFAA on CAC [R02].
  - Multi-PFAS and non‑PFAS solutes in competitive isotherms: complex, PFAS‑structure‑dependent capacity reductions [R01; R09].

These data emphasise that **PFAS functional group and chain length matter**:

- Shorter-chain and ether PFAS are more strongly inhibited by background matrix in anion-exchange columns [R07].
- Short‑chain and ultrashort‑chain PFAS show stronger sensitivity to CaCl₂ and matrix components in resin/carbon systems [R06–E03].
- Short‑chain PFAS are predicted to break through CAC barriers first [R03], and groundwater solutes particularly affect their adsorption [R11; R11].

### 4.2 Degradation processes

For degradation/destruction, we can similarly categorize:

- **Inhibitory**
  - Inorganic anions (HCO₃⁻, SO₄²⁻, Cl⁻, etc.) on VUV/Fe(III) defluorination [R13].
  - Persulfate in VUV/Fe(III) [R13].
  - Chloride and carbonate species in UV–persulfate systems [R14, R14].
  - Matrix organics and ions in plasma jets and DBD, which lower PFAS degradation (8–50% in tap/effluent vs higher in DI water) [R16, R16, R15].

- **Promotive**
  - NaHCO₃ (carbonate radicals) in sonolysis: complete PFOA degradation and near-complete defluorination vs <25% in clean water [R12; R12; R12].
  - Slightly alkaline pH (~8.7) as an optimum for carbonate radical assisted sonolysis [R12].

- **Interactive**
  - Oxidant type and co‑ions in VUV/Fe and UV–persulfate (e.g., persulfate + Fe(III) + inorganic anions; chloride + persulfate): complex radical networks where the same constituent can be beneficial or harmful depending on context [R13; R14].
  - Different matrices in plasma treatments not only change PFAS loss but also reshape byproduct distributions [R16; R15].

### 4.3 Mechanism–matrix–PFAS triangulation

To make results transportable:

1. **Identify the primary removal mechanism** (e.g., hydrophobic partitioning vs electrostatic sorption vs radical oxidation vs phase separation).
2. **Map matrix constituents to that mechanism**:
   - Competing for charged sites (e.g., Ca²⁺, NO₃⁻, DOM on resins).
   - Scavenging radicals (e.g., HCO₃⁻, Cl⁻, organics in AOPs).
   - Modifying microenvironment (pH, ionic strength, viscosity).
3. **Map PFAS properties**:
   - Chain length and hydrophobicity.
   - Functional group (carboxylate vs sulfonate; ether linkages).
   - Charge state at operating pH.

The same constituent may be **inhibitory for short-chain PFAA on AER**, **promotive for long‑chain PFOS on CAC**, and **strongly inhibitory for PFOA degradation in UV–persulfate**. This variability is mechanistically expected and must be made explicit in both experiment design and reporting.

---

## 5. Designing and reporting matrix-representative experiments

### 5.1 Matched-control framework

Across the better‑designed studies, robust matrix inferences came from **matched sets**:

- **Same PFAS & treatment conditions**, with and without a specific matrix modifier (NaHCO₃ vs none [R12]; inorganic anions vs none [R13]; CaCl₂ vs none [R06]).
- **Clean(er) water vs realistic water** under matched operation:
  - Clean vs NOM/ion‑rich matrices for nanosorbent columns [R05].
  - Deionized vs tap vs synthetic effluent in plasma [R16–E03].
  - Raw wastewater effluent vs NF‑conditioned permeate for subsequent GAC/IX [R10–E03].
  - Groundwater vs synthetic matrix variants for CAC barriers [R11].

These designs allow clear classification of matrix effects as inhibitory, promotive, or neutral.

**Minimum control framework for future work:**

1. **Baseline condition**  
   - A *well-characterized* low-interference matrix (not necessarily ultrapure water, but with fully reported composition) containing the PFAS suite.
   - For degradation studies: baseline radical system without added matrix modifiers.

2. **Single-modifier tests**  
   - Systematically add individual matrix components (e.g., DOM at defined mg C/L; Ca²⁺ at defined mM; Cl⁻, HCO₃⁻ at defined levels; specific surfactants).
   - Keep all other factors (PFAS load, pH, reactor power/fluence, sorbent dose, contact time, flow) constant.

3. **Composite/realistic matrices**  
   - Test realistic surface water, groundwater, effluent, or targeted synthetic mixtures at reported DOC, ionic strength, major anions/cations, and relevant co-contaminants.
   - Where possible, link field samples back to simplified surrogates (e.g., DOM-only, ions-only) to separate overlapping effects.

4. **Matched dynamic vs equilibrium systems**  
   - For sorbents, pair batch isotherms (intrinsic affinity) with dynamic column tests (breakthrough, fouling).
   - For AOPs/plasma, pair kinetic measurements in simple and complex matrices with appropriate radical-quenching or probe experiments (e.g., QR analysis) to interpret matrix effects mechanistically [R14].

### 5.2 Minimum matrix characterization to report

At a minimum, to enable cross‑study interpretation, authors should report for each tested condition:

**For all water matrices (including “clean” solutions):**

- **Inorganic chemistry**
  - Major cations (Na⁺, K⁺, Ca²⁺, Mg²⁺) and major anions (Cl⁻, SO₄²⁻, NO₃⁻, HCO₃⁻/CO₃²⁻); at least approximate ranges (e.g., mM).
  - Ionic strength.
  - pH and alkalinity (or sufficient carbonate speciation).
- **Organic matter**
  - DOC (mg C/L) and, if used, source/type (e.g., Suwannee River fulvic acid as in R03/R01; wastewater effluent organic matter).
- **Specific added modifiers**
  - Surfactants (type and concentration) [R03; R04].
  - Co-contaminants (benzene, TCE, phosphate, oxidants such as persulfate) [R03; R09; R13; R14].
- **Matrix category**
  - Synthetic lab solution, real groundwater, surface water, or effluent; and any conditioning (e.g., NF-permeate vs raw effluent [R10]).

**For PFAS and treatment conditions:**

- PFAS identities (including chain length and functional group); at least grouped as short-, long‑chain, ether, etc. [R07; R09; R06; R02].
- Influent PFAS concentrations and loading rate (for columns, per bed mass).
- Treatment conditions relevant to mechanism:
  - Sorbent dose and solid type (surface chemistry, pore structure).
  - Column EBCT/flow for dynamic tests.
  - AOP parameters (UV fluence, oxidant dose, Fe(III) level).
  - Sonolysis power/frequency [R12].
  - Plasma power, gas type, and reactor configuration [R15; R16].

### 5.3 Reporting endpoints clearly and non‑confoundingly

To avoid conflating separation and destruction:

- **Distinguish endpoints explicitly**:
  - Adsorption/separation: sorbed mass or breakthrough (PFAS mass transfer from water to solid or floc).
  - Parent-compound loss: decrease in target PFAS concentration.
  - Defluorination: fluoride release relative to organofluorine content [R12; R13; R14].
  - Mineralization: organic carbon to inorganic carbon (CO₂) where measured [R14].
  - Byproducts: transformation products (shorter-chain PFAS, organofluorine intermediates, chlorate, etc.) [R13; R14; R16].

- **Do not label adsorption as degradation.**  
  Many adsorption and membrane studies only move intact PFAS to another phase and record no transformation products [e.g., R01; R07; R10]. They should be reported as **removal/separation**, not “destruction” or “mineralization.”

- **Quantify matrix effects as ratios or deltas under matched conditions**, e.g.:
  - Capacity in presence vs absence of NOM (e.g., percent loss).
  - Rate constants or half-lives in the presence vs absence of specific ions.
  - Breakthrough time shifts between clean and complex matrices.

Where data or access constraints prevent reporting exact numbers (as in several abstract‑only records), authors should still state **direction and approximate magnitude categories** (e.g., <2× change, 2–10×, >10×) and make the comparison basis explicit.

### 5.4 Study design priorities and evidence gaps

The available evidence reveals several gaps that future work should address:

1. **Explicit clean‑matrix baselines for degradation studies:**  
   Sonolysis (R12) and UV–persulfate (R14) provide relatively good baselines. VUV/Fe(III) and plasma studies often compare only across variable matrices without a well-described low-interference control.

2. **Short‑chain and emerging PFAS across treatment types:**  
   Short‑chain and ether PFAS are more sensitive to matrix in adsorption systems [R07; R02; R06], but much less is known about their behavior in sonolysis, UV–persulfate, or plasma.

3. **Systematic interactions among multiple constituents:**  
   Only a few studies break out interactions (e.g., NOM + Ca²⁺ [R01]; additive inhibition by multiple solutes [R02]). Designs that vary DOC and a key ion factorially at controlled levels are still rare.

4. **Linking radical diagnostics to performance in real matrices:**  
   QR analysis for chloride and carbonate [R14] is a strong example; similar mechanistic quantification is largely missing from plasma and VUV studies.

5. **Hybrid trains and preconditioning:**  
   The NF–adsorption hybrid [R10] shows the value of preconditioning to “tame” the matrix. More work should explore such strategies (e.g., softening, partial DOC removal, pre-oxidation) with explicit before/after matrix characterization.

---

## 6. Concluding recommendations

To translate PFAS treatment performance beyond clean laboratory water, studies should:

1. **Design experiments around matrix contrasts, not treat them as afterthoughts.**  
   At least one low‑interference baseline and a set of controlled matrix modifications (single constituents and realistic mixtures) must be included, with all other treatment parameters held constant.

2. **Report matrix chemistry and PFAS properties with enough detail to interpret mechanisms.**  
   Without DOC, ionic strength, key ions, and co-contaminant levels, matrix effects cannot be generalized across studies.

3. **Classify matrix effects explicitly as inhibitory, promotive, neutral, or interactive for each PFAS–mechanism pair.**  
   Use matched-condition comparisons and clearly state that these classifications are **conditional** (e.g., “carbonate is promotive in carbonate-radical sonolysis, but inhibitory in UV–persulfate”).

4. **Separate separation from destruction in both language and measurement.**  
   Adsorption, coagulation, and membrane rejection are phase-transfer processes; AOPs, sonolysis, UV–persulfate, and plasma are (potentially) destructive. Endpoints should reflect this distinction to avoid overclaiming destruction when only removal has been measured.

5. **Use matrix-aware performance metrics.**  
   For example, adsorption capacity normalized to clean-matrix capacity (K/K_clean), or degradation rate constants plotted vs a matrix parameter (e.g., DOC, HCO₃⁻).

Only with such a **matched-control, matrix‑explicit framework** can PFAS treatment data from clean water be meaningfully extrapolated to groundwater, surface water, and wastewater — and can the community avoid misleading generalizations that ignore the decisive role of the water matrix.

# Blinded Dev13 adequacy calibration

Status: **26 labels pending**

Do not open `sealed_mapping/` or any L3 scoring result before all
labels are finalized. System identity, L3 score, claim-level judge
status, and candidate pairing are intentionally withheld.

Judge each answer independently. Use the question, task boundaries,
and non-exhaustive reference evidence. Do not count claim groups or
estimate an L3 score.

Record `yes` only when the answer is scientifically correct,
sufficiently addresses the central researcher task, respects scope
and endpoint distinctions, and has no material error. Record `no`
when a central requirement is missing, endpoints are materially
conflated, the answer overclaims, or a material scientific error
makes it unsuitable. Use `uncertain` only for cases requiring
adjudication before threshold calibration.

## D13-A001

**Question ID:** `WF10_004b`

**Question:** How can PFAS compound class or headgroup affect treatment performance or equilibrium behavior?

**Must include:** Compare studies only on matched compounds, matrices, endpoints, and conditions; avoid ranking technologies when the evidence is not comparable.

**Must not claim:** Do not convert a condition-specific finding into a universal PFAS treatment claim.

### Reference evidence

**WF10_004b_MMG001**

> from landfill leachate within seven hours of operation, with 98.3 % of perfluorosulfonic acids (PFSA) and 85.5 % of perfluorocarboxylic acids (PFCA) removed from the leachate.

**WF10_004b_MMG002**

> were significantly lower at higher GenX concentrations, with 1.00 mM and 2.00 mM achieving only (69.0 � 4.5) and (39.0 � 4.5) % defluorination, respectively. This suggests that either the adsorption of GenX on the anode or the concentration of generated oxidants was limiting for the cleavage of GenX C  F bonds. We have observed a similar concentration dependence of the defluorination of PFOS. [41] This indicates that the chemical identity of the PFAS headgroup did not govern the PFAS adsorption at laser-made [Ni 0.75 Fe 0.25 ]-(OH) 2 –hydrophilic carbon fiber paper anodes, but that anode characteristics, i. e. available adsorbent sites and particularly the generation of oxidant species (O *  ), are posing an upper limit to concentration for efficient PFAS defluorination. The equilibrium amount of adsorbed molecules increases with increasing solute concentration. [50–52] A higher number of adsorbed PFAS mole- cules contributes only to defluorination efficiency until all available adsorbent sites are saturated or all generated oxidant species are consumed within the anode microenvironment. The ability to defluorinate low PFAS concentrations is essential for practical applications. [1] Nevertheless, the chemical identity of the PFAS headgroup and the PFAS structure affect the bond

**WF10_004b_MMG003**

> Because FHxSA is likely neutral at pH 7.3 ( Nguyen et al., 2020 ) due to the sulfonamide headgroup, rejection by NF was consistently lower than the anionic analogue, PFHxS, attributed to the lack of an electrostatic repulsion rejection mechanism for this compound ( Fig.

**WF10_004b_MMG004**

> The adsorption capacity and affinity of the zeolite β are lower for the sulfonic acids than for the carboxylic acids, which is due to the more polar nature of the sulfonic moiety and the unlikely formation of sulfonic acid dimers.

**WF10_004b_MMG005**

> For example, the removal of PFHeA (55%, overall) was much less than that of PFHeS (96%, overall), and PFHxA was removed Y.

**WF10_004b_MMG006**

> Batch tests revealed that perfluorosulfonic acids (PFSAs) were more efficiently removed, with up to 94% removal, compared to perfluorocarboxylic acids (PFCAs), which showed up to 60% removal when using either ZVI or ZVI + BC.

**WF10_004b_MMG007**

> Similar to the behavior observed in batch mode, the column treatment demon - strated higher retention of sulfonate PFAS than carboxylate ones with equal perfluorocarbon chain lengths (e.g., 84 % PFOS versus 72 % PFNA removal, or 64 % PFHxS versus 44 % PFHpA), likely due to the greater effect of the sulfonate functional group.

### Anonymous candidate answer

1. Answerability 
partially_answerable – Several studies directly relate PFAS headgroup/functional class to adsorption, partitioning, and removal, but effects are treatment‑specific and not comprehensively quantified for all PFAS classes or technologies.

2. Answer 

Headgroup and compound class influence PFAS behavior mainly through charge, steric hindrance, polarity, and molar volume, which change electrostatic and nonelectrostatic interactions with treatment media.

Key patterns by treatment type:

**A. Ion exchange resins (IX, AERs)** 

- **Anionic PFAAs (carboxylates, sulfonates) generally adsorb more strongly than zwitterionic or cationic PFAS at the same chain length.** 
 – In AFFF-impacted waters, suspect PFAS with **bulkier and/or zwitterionic headgroups** showed markedly lower adsorption and lower log K_ex than anionic PFAAs with similar perfluoroalkyl chain lengths. 
 – Zwitterionic PFAS typically had 1–60 % adsorption to strong‑base AERs, with <30 % for most resin–PFAS combinations, while PFAS with **cationic headgroups** adsorbed even less (1–22 %), and these zwitterionic/cationic classes had the lowest log K_ex among 21 suspect PFAS classes. 
 – Interpretation: electrostatic attraction between anionic headgroups and quaternary ammonium sites is strong; internal charge compensation (zwitterions) or net positive charge (cationic PFAS) reduce this driving force, leaving only weaker hydrophobic/van der Waals interactions.

- **Headgroup identity within anionic PFAS still matters.** 
 – Replacing a simple carboxylate (PFPeA) with a more complex amide headgroup on the same tail markedly decreased log K_ex to AERs. 
 – Similarly, replacing a sulfonate (PFHxS) with sulfonamide or sulfonamidoacetic headgroups (FHxSA, MeFASAA) reduced adsorption to AERs. 
 – Bulkier, more sterically hindered, and less strongly anionic headgroups reduce effective electrostatic binding and packing at resin sites.

- **General IX conclusion:** 
 – Strongest IX removal: **anionic sulfonates/carboxylates** with longer perfluoroalkyl tails. 
 – Weaker: **sulfonamides, amides, zwitterionic, and cationic** classes, even at similar chain length, due to reduced net anionic character or steric hindrance. 

**B. Adsorption to porous carbons and mineral/soil surfaces** 

1. **Activated carbon (e.g., colloidal activated carbon, CAC)** 

- **Sulfonates vs carboxylates (same chain length):** 
 – PFBS (PFSA, C4) showed higher adsorption affinity to CAC than PFPeA (PFCA, C4) under identical conditions. 
 – Mechanistic explanation: PFSAs have **higher molar volumes** than corresponding PFCAs, giving stronger van der Waals interactions with carbon surfaces. 
 – Thus, for equal perfluorocarbon length, **PFSA > PFCA** in CAC adsorption capacity/affinity.

2. **Clay minerals and humic soil components** 

- For PFOS vs PFOA, which share the same tail, the **larger sulfonate headgroup of PFOS coordinates more favorably to the clay surface** than the carboxylate headgroup of PFOA, enhancing adsorption. 
- Molecular simulations show adsorption is dominated by tail–surface hydrophobic interactions, but headgroup size/coordination modifies the depth and shape of the adsorption energy well, thereby affecting equilibrium affinity and kinetics.

**C. Nanofiltration (NF) membranes** 

- For PFAS with the same headgroup, adsorption correlates strongly with chain length and hydrophobicity (MW/log K_ow). But **headgroup type also modulates adsorption strength.** 
- Using compounds with different functional groups, the relative effect of headgroup on adsorption strength decreased in the order: 
 **–C(O)O– > –CO– > –HCON– > –CH₃**. 
 – This suggests more polar, more strongly interacting functional groups (e.g., carboxylate carbonyl) yield stronger adsorption to NF membranes than less polar or more hydrophobic termini, at comparable size.

**D. Partitioning and fate in wastewater/sludge systems** 

- In a full‑scale AO–MBR–RO WWTP, **terminal sulfonates (e.g., PFOS) strongly enriched in sludge**, while some emerging ether carboxylates (e.g., PF4OPeA) remained relatively mobile and behaved more like short‑chain PFAS. 
- Overall, **chain length, functional group, and molecular polarity jointly governed partitioning**, with longer-chain and sulfonate PFAS tending to sorb more strongly and accumulate in solids, whereas more polar, carboxylate‑type or ether acids remained in the aqueous phase. 
- This directly affects apparent treatment performance: processes that remove solids (sludge wasting, media filtration) will preferentially remove sulfonates and longer‑chain classes.

**E. General structural principles for headgroup effects**

Integrating across studies:

- **Charge state and distribution** 
 – Strong anionic headgroups (carboxylates, sulfonates) favor: 
 • IX removal on AERs (electrostatic attraction). 
 • Cationic or metal‑modified sorbents (e.g., Fe‑modified peat) where higher negative charge density of sulfonate oxygens gives stronger binding than carboxylates. 
 – Zwitterionic or cationic headgroups substantially reduce adsorption to AERs and similar anion‑selective systems.

- **Headgroup type: sulfonate vs carboxylate** 
 – On several sorbents (iron‑modified peat, granular peat; CAC), **PFSAs show higher removal/adsorption than PFCAs of the same chain length**, attributed to higher charge density per oxygen and additional oxygen atoms in PFSAs, plus larger molar volume and stronger van der Waals interactions.

- **Steric hindrance / bulkiness** 
 – Complex amide/sulfonamide headgroups on the same tail reduce adsorption to AERs relative to simple carboxylate/sulfonate headgroups, likely by steric hindrance and altered ionization behavior.

- **Molecular polarity and hydrophobicity** 
 – Headgroups that lower overall polarity (e.g., some amide, sulfonamide, fluorotelomer structures) reduce electrostatic interactions but can still allow hydrophobic tail adsorption; equilibrium then shifts toward weaker, more reversible sorption with greater mobility.

3. Uncertainty and limitations 

- Effects are **treatment‑specific**: a headgroup that enhances adsorption to clay or activated carbon may not enhance IX, and vice versa; quantitative rankings are not transferable across media. 
- Most evidence is for a limited set of classes (legacy PFCAs/PFSAs, some sulfonamides/fluorotelomers, a few ether acids); many emerging PFAS classes lack systematic headgroup–performance data. 
- Some systems are governed more by **reactor or electrode properties** or oxidant generation than by headgroup chemistry, so headgroup effects on degradation (as opposed to adsorption/partitioning) may be minor or indirect in those cases (e.g., some electrochemical systems). 
- pK_a predictions for complex headgroups can be uncertain; actual speciation at environmental pH may differ, affecting true “headgroup effect.”

4. Practical takeaway 

For treatment design and equilibrium modeling, PFAS compound class and headgroup should be treated explicitly: anionic sulfonates tend to sorb and partition much more strongly than carboxylates of the same chain length, while bulkier, zwitterionic, or cationic headgroups and ether/amide variants typically show weaker IX removal and more mobile behavior, so resin selection, media choice, and process expectations should be tailored to the predominant PFAS headgroup classes in the target water.

### Human label

- Adequate (`yes` / `no` / `uncertain`):
- Material scientific error (`yes` / `no` / `uncertain`):
- Confidence (`high` / `medium` / `low`):
- Notes:

---

## D13-A002

**Question ID:** `NQ23`

**Question:** What energy-consumption or energy-efficiency evidence is available for PFAS degradation methods, and can values be compared across studies?

**Must include:** Must identify the energy metric used, such as EEO, EEM, kWh/m3, kWh/g, electrical input, or energy per mass removed; must explain comparability limits.

**Must not claim:** Must not claim one universal energy-consumption number fairly represents all PFAS degradation methods.

### Reference evidence

**NQ23_MMG001**

> The comparison between the NTP technologies and the other AOPs from the viewpoint of energy consumption (evaluated in term of elec - trical energy per order values - E EO ), classifies the NTP processes in a central zone with median energy consumptions in the 1 – 100 kWh/m 3 range, at the same level of photo-Fenton and pure electrolytic AOPs.

**NQ23_MMG002**

> where E (kWh) is the energy consumed by the high-voltage power supplies, gas and liquid pumps, and rotating spark gap, V (L) is the treatment volume for each experimental condition, and C i and Cf are the initial and ﬁnal concentrations (below the USEPA HAL), respectively, of PFOA and PFOS (ng/L).

**NQ23_MMG003**

> The energy consumption of EO can be calculated as described previously 15 and as presented in eq S18.

**NQ23_MMG004**

> A. Kumar et al. Chemical Engineering Journal Advances 25 (2026) 101046 11 results, enabling a more robust fluoride mass balance and interpretation of degradation pathways. In contrast, results obtained at lower initial concentrations were subject to greater uncertainty, likely influenced by sorption losses and interfacial effects, which complicate quantitative interpretation. The findings demonstrate the capability of the orifice- based HC system to induce PFOS degradation and defluorination, with the higher-concentration experiments offering stronger evidence for effective destruction rather than incomplete transformation. The EEO ranged from 7 to 598 kWh/m³/order, while the energy yield varied between 17 and 286 mg/kWh. The overall energy input for PFOS degradation ranged from 1 to 75 kWh/m³, depending on the initial PFOS concentration and the extent of degradation.. These results indicate that HC enables effective PFOS degradation with lower energy requirements compared to most reported studies and conventional treatment methods. The extreme physicochemical conditions generated during bubble implosion indicate that PFOS reaching the cavitation bubble undergoes near-complete mineralization, with subsequent decomposi - tion of intermediates into fluoride ions. Overall, this study demonstrates that HC is a promising, non- thermal, energy-efficient, and scalable technology for PFAS degrada - tion. It presents a viable alternative to conventional treatment methods and lays the groundwork for sustainable, large-scale PFAS remediation

**NQ23_MMG005**

> However, the primary challenge with N 2 plasma is its low PFAS degradation efficiency (45 % for PFOA and 60 % for PFDA) combined with high energy consumption (EEO values of 370 kWh/m 3 for PFOA and 260 kWh/m 3 for PFDA).

**NQ23_MMG006**

> It can be observed that the reported ranges show a high variability, reflecting the uncertainty and nonuniformity of experimental conditions in the respective studies (Table 1).

**NQ23_MMG007**

> Application potential A consolidated comparison of reported EE/O values, together with key experimental parameters such as water type, initial PFAS concen - tration, reactor scale, reaction time, and removal/defluorination effi - ciency, is provided in Table S1 to support a transparent and context- aware evaluation across technologies.

### Anonymous candidate answer

1. Answerability 
general_framework_only – Energy use is routinely reported for PFAS destruction technologies, but without access to specific datasets only general patterns, metrics, and comparability constraints can be described, not method‐ or study‑specific numbers.

---

2. Answer 

**A. What “energy evidence” is typically reported for PFAS degradation?** 

Across PFAS destruction/desorption/degradation methods, energy use is usually characterized with a mix of:

1. **Process‑scale energy metrics** 
 - **kWh per m³ of water/gas/soil treated** (or per kg of solids). 
 - **kWh per kg PFAS degraded** (less common, but the most directly relevant to PFAS). 
 - **kWh per log‑removal (EE/O)** for advanced oxidation/reduction and plasma processes. 
 - **Specific energy input (SEI)** in plasma systems (e.g., J/L, J/g of gas).

2. **Performance‑linked energy metrics** 
 - **Energy per log removal** of a target PFAS (e.g., kWh for 1‑log or 2‑log reduction). 
 - **Energy per % defluorination** or per mole of fluoride released (for destruction rather than mere disappearance of parent compound). 
 - **Energy per unit TOF/TOC reduction**, if mineralization is targeted.

3. **Equipment/operating metrics** (inputs to energy calculations) 
 - **Power density** (e.g., W/L of reactor, W/cm² of UV lamp, W/cm of plasma electrode). 
 - **Reaction time / hydraulic retention time**. 
 - **Voltage and current** (for electrochemical, plasma, conductive heating). 
 - **Temperature & pressure profiles** (for thermal, supercritical water, etc.). 
 - **Gas flows** (for plasma, incineration) that affect energy per unit treated.

4. **Economic surrogates** 
 - **Operating cost per volume or mass treated**, with energy cost as the major component. These are derived from energy metrics but also include consumables (electrodes, oxidants, catalysts) and sometimes amortized capital.

**By technology class, the evidence usually looks like this:**

- **UV‑based AOPs (UV/H₂O₂, UV/sulfite, UV/persulfate, UV‑photolysis of PFAS precursors)** 
 - Common: **EE/O** (kWh/m³/order) for target PFAS or surrogates. 
 - Sometimes: kWh/m³ at a set flow and lamp power; less often normalized to PFAS mass. 

- **Electrochemical oxidation/reduction (e.g., BDD, Ti/RuO₂, gas‑diffusion cathodes)** 
 - Common: cell voltage, current density, time → **kWh/m³** or kWh per mass PFAS or per % removal. 
 - Occasionally: energy per mole of F⁻ released or per log reduction. 

- **Plasma (DBD, gliding arc, corona, plasma‑water interface)** 
 - Often: **specific energy input** (J/L) and an implied “energy per % or log removal.” 
 - Often missing: clear normalization to actual PFAS mass/fluorine mineralized.

- **Thermal and hydrothermal (incineration, pyrolysis, thermal desorption + off‑gas treatment, supercritical water oxidation)** 
 - Sometimes: energy per kg of material treated (kWh/kg sludge, soil, adsorbent). 
 - Sometimes: energy for achieving a specified temperature–time profile. 
 - Rare: energy per mass of PFAS mineralized; often it’s per mass of bulk matrix.

- **Sonolysis, photocatalysis, reactive electrochemical membranes, etc.** 
 - Similar to UV‑AOPs and electrochemical: power, time, volume → kWh/m³ and sometimes EE/O.

So there **is** energy evidence, but it is highly heterogeneous in how it is reported.

---

**B. Can energy values be compared across studies and technologies?** 

They can be compared **only under very strict and often unmet conditions**. In practice, **most reported values are not directly comparable** because:

1. **Different normalization bases and endpoints** 
 - Some studies report **kWh/m³ treated** regardless of how much PFAS is present or degraded. 
 - Others use **EE/O** (kWh/m³ per order of concentration reduction). 
 - Few normalize to **mass of PFAS or fluorine mineralized** (e.g., kWh/g PFAS destroyed). 
 - “Degradation” may mean:
 - Disappearance of parent PFAS, 
 - Transformation to unknown/intermediate species, 
 - Partial defluorination, or 
 - Near‑complete mineralization (CO₂ + F⁻). 
 - Energy per “removal” of parent PFAS cannot be equated to energy per **destruction** or per **defluorination**.

2. **Different matrices and concentrations** 
 - **Matrix** (pure water vs groundwater vs wastewater vs concentrate vs sludge/soil) strongly affects energy:
 - Scavengers and natural organic matter can increase energy demand for radical‑based treatments. 
 - High solids or DOC can shield PFAS from UV/plasma or electrode surfaces. 
 - **Initial PFAS concentrations** span µg/L to mg/L; the same **kWh/m³** can represent very different **kWh/g PFAS**. 
 - Comparing EE/O across orders of magnitude different starting concentrations is misleading unless normalized explicitly to **PFAS mass removed**.

3. **Different PFAS chemistries and mixtures** 
 - C‑F bond strength and degradation behavior differ for:
 - Perfluoroalkyl carboxylates vs sulfonates, 
 - Chain length (short vs long), 
 - Branched vs linear isomers, 
 - Precursors vs terminal PFAS. 
 - Energy demand to destroy a long‑chain PFAA at mg/L in DI water is not comparable to destroying diverse short‑ and long‑chain PFAS at µg/L in complex waste brine.

4. **Different performance targets and time scales** 
 - Some studies report energy to achieve **1–2 log removal**; others run to **near‑complete disappearance** or measure only early‑stage rates. 
 - Energy efficiency tends to vary with **conversion**; early removal of a small fraction can appear very energy‑efficient compared to pushing to high mineralization or defluorination. 
 - Without a common **endpoint definition** (e.g., 90% parent removal vs 90% defluorination), values are not comparable.

5. **Different reactor scales and designs** 
 - Bench‑scale systems often **under‑represent parasitic losses** (e.g., lamp ballasts, heat losses, pumping, gas compression). 
 - Pilot and full‑scale systems include many additional loads; their energy use per volume can be higher or lower depending on engineering design. 
 - Geometry, mass transfer, mixing, and hydrodynamics can change apparent “intrinsic” energy efficiency.

6. **Different inclusion of ancillary processes** 
 - Some studies count **only the destruction step** (e.g., energy to run an electrochemical cell or plasma reactor). 
 - Others include **pre‑concentration** (e.g., GAC, IX, membranes), **pumping**, **heating**, or **off‑gas treatment**. 
 - Comparing destruction‑only energy with “treatment train” energy is not fair.

---

**C. When and how *can* energy values be reasonably compared?** 

Energy efficiency comparisons are most meaningful when:

1. **Normalization is consistent and physically relevant**, e.g.: 
 - **kWh per gram of PFAS (or per mole of C–F) mineralized** under a defined endpoint (e.g., ≥90% defluorination). 
 - If mineralization data are lacking, clearly defined **kWh per gram PFAS removed** with mass balance on transformation products. 

2. **Conditions are closely matched**: 
 - Similar matrix type (e.g., all in surface water with similar DOC and ionic strength). 
 - Comparable initial PFAS concentrations and mixture composition. 
 - Comparable performance target (e.g., 2‑log parent removal or 80% defluorination).

3. **System boundaries are explicitly defined**: 
 - Make clear whether energy covers:
 - Only the reactive step vs 
 - The entire treatment train, including pre‑concentration and post‑treatment. 
 - If they differ, adjust or at least describe the difference before comparison.

4. **Scaling and design differences are accounted for**: 
 - Compare either:
 - Technologies at similar **technology readiness and scale** (e.g., all bench‑scale), or 
 - Explicitly separate comparisons of **fundamental energy efficiency** (bench) from **practical, engineered energy use** (pilot/full‑scale).

5. **Explicit recognition of what is being “destroyed”**: 
 - Parent PFAS only vs PFAS plus precursors vs full fluorine content. 
 - Include fluoride accounting where possible to interpret defluorination and mineralization.

Under those controlled conditions, **relative rankings** (e.g., “Technology A requires less kWh per mol of C–F broken than Technology B under these specific conditions”) are possible. Outside those conditions, apparent comparisons are mostly artifacts of differing assumptions.

---

3. Uncertainty and limitations 

- Without actual datasets, no specific numeric ranges or technology rankings can be given. 
- Many PFAS degradation studies still do not fully report:
 - Energy normalized to PFAS mass or fluorine content, 
 - Complete mass balances (including intermediates and fluoride). 
- Energy metrics often neglect ancillary processes (pre‑concentration, gas handling, heating), so reported values may underestimate real‑world energy demand. 
- Heterogeneity in reactor design, PFAS mixtures, and matrices makes cross‑study meta‑comparison intrinsically uncertain, even with better reporting.

---

4. Practical takeaway 

Energy evidence for PFAS destruction exists but is reported with inconsistent metrics, endpoints, and system boundaries; meaningful cross‑study comparisons require re‑expressing results on a common basis (ideally kWh per unit PFAS or C–F mineralized under similar matrices and performance targets) and explicitly documenting what portion of the treatment train and what degree of destruction the reported energy actually represents.

### Human label

- Adequate (`yes` / `no` / `uncertain`):
- Material scientific error (`yes` / `no` / `uncertain`):
- Confidence (`high` / `medium` / `low`):
- Notes:

---

## D13-A003

**Question ID:** `NQ24`

**Question:** How do reported activated-carbon PFAS adsorption capacities differ between batch and column studies?

**Must include:** Must distinguish carbon type, PFAS chain length or compound, test conditions, endpoint, capacity units, and capacity values when values are presented.

**Must not claim:** Must not claim activated carbon has one fixed PFAS adsorption capacity across compounds and matrices.

### Reference evidence

**NQ24_L3CTX001**

> Journal of Water Process Engineering 54 (2023) 103965 Available online 29 June 2023 2214-7144/© 2023 Elsevier Ltd. All rights reserved. PFOA remediation from aqueous media using CTAB impregnated activated carbon: A closed-loop sustainable study with comprehensive selectivity analysis Mohd Ahmed Naim Shaikh, Paulami Sarkar, Tabish Nawaz * Environmental Science and Engineering Department (ESED), IIT Bombay, Powai, Mumbai 400 076, India ARTICLE INFO Keywords: Biochar PFAS Emerging contaminants Adsorbent synthesis ABSTRACT PFASs have been attracting worldwide attention in recent years. In this study, a novel surface-impregnated activated carbon (AC) has been optimally synthesized utilizing waste Karanja shells. Surface functional group modification has been performed using Cetyltrimethylammonium bromide (CTAB). PFOA-selectivity analysis of the adsorbent against different background species present at typical river water concentration was performed. To make the process sustainable, the development of regenerant specifications as well as recovery of the regenerant and PFOA from the spent regenerant solution were investigated. A biomass/acid ratio of 1:2.5, temperature 450 ◦ C, and 1 % CTAB solution was found to be optimum synthesis parameters for the CTAB- modified AC (CTAB_K-AC) for PFOA removal. By CTAB-impregnation, the PFOA uptake capacity of the adsor - bent increased up to threefold.

**NQ24_MMG001**

> max ob - tained through the Thomas model was 5.71 mg/g, which was marginally lower as compared to the Q e obtained through Langmuir isotherm model (6.85 mg/g) mainly due to two reasons (a) the presence of the back - ground water matrix during the column run and (b) the size of the adsorbent was bigger (125 – 500 μ m) than used in the batch equilibrium and kinetic study (125 – 250 μ m).

### Anonymous candidate answer

1. Answerability 
partially_answerable – General scientific expectations about batch vs column adsorption capacities can be described, but quantitative “reported” differences require literature data that I do not have.

---

2. Answer 

Conceptually and in most reported work, PFAS adsorption capacities for activated carbon tend to appear:

- **Higher in batch tests** (per mass of carbon, e.g., mg PFAS/g carbon at equilibrium) 
- **Lower in column tests** (often expressed as dynamic capacity at a given breakthrough criterion, bed volumes to breakthrough, or mg/g to a set effluent concentration)

for the same PFAS–carbon–water system and comparable influent concentrations.

Key reasons and patterns:

**1. Equilibrium vs. mass-transfer-limited operation**

- **Batch tests**
 - Typically run with long contact times and vigorous mixing.
 - Aim to approach equilibrium, so the reported capacity is close to the **equilibrium uptake** at the tested concentration.
 - Minimized external mass-transfer limitations (thin boundary layer) and enough time for intra-particle diffusion.

- **Column tests**
 - Operate under **flow**, with finite contact time (controlled by EBCT/empty-bed contact time) and realistic hydraulic conditions.
 - PFAS breakthrough generally occurs **before full equilibrium** loading is reached because of:
 - Film diffusion limitations
 - Intraparticle diffusion limitations
 - Shorter effective contact times and non-ideal flow patterns
 - Result: **dynamic capacity at breakthrough is systematically lower** than batch equilibrium capacity for the same initial concentration.

**2. Differences in how “capacity” is defined and reported**

- **Batch studies**
 - Typically report **equilibrium capacity** (qe, mg PFAS/g carbon) at a given initial and equilibrium concentration.
 - Sometimes fit isotherms; the maximum capacity (e.g., a Langmuir qmax) is often reported, which may represent an upper bound not reached in practice.

- **Column studies**
 - Often report:
 - **Bed volumes to a specific breakthrough criterion** (e.g., 5–10% of influent concentration).
 - **Dynamic capacity** at that breakthrough point (integrated mass removed divided by carbon mass).
 - This “capacity” is **operational**: it depends strongly on breakthrough definition, influent concentration, EBCT, and water matrix.
 - If converted to mg/g, these values will typically be **lower** than the batch qe (sometimes substantially).

**3. Role of influent concentration and water matrix**

- **Batch**
 - Often use single-solute or simplified matrices; background DOC/competitors may be lower or absent.
 - Capacities can be higher because:
 - Fewer co-adsorbates competing for sites.
 - Higher PFAS concentrations used to define isotherms.

- **Column**
 - Commonly use more realistic waters (natural groundwater, surface water, or secondary effluent) with:
 - DOC
 - Competing organic micropollutants
 - Inorganic ions affecting speciation or competition
 - This **competition and fouling** reduces effective capacity and speeds breakthrough, lowering the dynamic capacity relative to batch equilibrium values in clean systems.

**4. PFAS- and GAC-specific behavior**

While details depend on:

- PFAS chain length and functional group (e.g., PFOA vs PFOS vs short-chain PFAS),
- Carbon type (GAC vs PAC, surface chemistry, pore size distribution),

the qualitative pattern remains:

- **Longer-chain PFAS** often show relatively **higher capacity** and sharper advantage in batch studies than short-chain PFAS.
- In column tests, the **relative gap** between batch and dynamic capacity can be especially marked for more strongly adsorbed PFAS, because columns are operated below equilibrium to maintain low effluent levels.

**5. Practical interpretation**

- **Batch equilibrium capacities** are best interpreted as:
 - Upper bounds for performance at a particular concentration and matrix.
 - Useful for **screening** adsorbents and understanding trends (e.g., chain-length dependence).

- **Column dynamic capacities**:
 - More representative of **practical design values** for treatment systems.
 - Better suited to sizing GAC beds and estimating changeout frequency.
 - Expected to be **lower than batch capacities**, often substantially, due to both hydraulic and competitive effects.

---

3. Uncertainty and limitations 

- Without specific data compilations, I cannot quantify the typical ratio or numerical difference between batch and column capacities for PFAS on activated carbon. 
- The magnitude and even direction of differences could be altered in atypical test designs (e.g., very long EBCT or artificially simple column matrices) where near-equilibrium is reached. 
- Differences among PFAS species, carbon types, and water chemistries can be large enough that no single “correction factor” from batch to column is reliable.

---

4. Practical takeaway 

Expect activated-carbon PFAS capacities reported from batch tests to overestimate what is achievable in real columns; for design or performance prediction, preferentially use dynamic column data at relevant EBCT, matrix, and breakthrough criteria, and treat batch capacities only as upper bounds or screening metrics.

### Human label

- Adequate (`yes` / `no` / `uncertain`):
- Material scientific error (`yes` / `no` / `uncertain`):
- Confidence (`high` / `medium` / `low`):
- Notes:

---

## D13-A004

**Question ID:** `NQ10`

**Question:** How are PFAS samples preconcentrated before mass spectrometry, and how do protocols vary by matrix, analyte, or method?

**Must include:** Must connect SPE selection to matrix and analyte scope; must mention recovery or chemistry-dependent suitability when supported.

**Must not claim:** Must not claim one exact SPE cartridge and elution protocol is universally correct for all PFAS environmental samples.

### Reference evidence

**NQ10_MMG001**

> Conclusion An eﬃcient and convenient SPME method was developed for PFAS in aqueous matrices and applied to river, lake, tap and bottled water samples.

**NQ10_MMG002**

> 3 ng L − 1 ∗∗ 40 – 160 ng L − 1 ∗∗∗∗ [39] Drinking water (EPA method 8327) Dilute and Shoot N/A 24 PFAS compounds

**NQ10_MMG003**

> So far, to detect parts-per-trillion level PFAS, pre-concentration has been accomplished by either solid phase extraction (SPE) or liquid-liquid extraction (LLE) [ 9 , 34 , 40 ].

**NQ10_MMG004**

> Obtained results showed that, with 150 mg cartridges, recoveries clearly decreased when the sample volume was increased from 10 to 100 mL.

**NQ10_MMG005**

> (C8–C14), with values above 61% for all of them and close to 100% in the case of PFOS or PFNA.

**NQ10_MMG006**

> Eluted methanolic sample extracts of 0.5 mL resulted in an effective 500-fold concentration of target analytes from the initial sampling.

**NQ10_MMG007**

> for analysis [67–70]. However, SBSE coupled with GC-MS is yet to be developed. This study aimed to develop and validate a simple, sensitive, and efficient method by integrating green chemistry-based stir bar sorptive extraction (SBSE) with thermal desorption–gas chromatography–mass spectrometry (TD-GC-MS) specifically for the anal- ysis of perfluorocarboxylic acids (PFCAs), a significant subgroup of PFAS. The novelty of this research lies in its solvent-free approach, which reduces environmental impact and costs while enhancing the sensitivity and accuracy of PFCA detection by minimizing potential contamination and analyte loss. Unlike traditional methods such as LC-MS/MS, which often require complex, labor-intensive, and costly procedures, our SBSE-TD-GC-MS method offers a more efficient, cost-effective, and environmentally friendly alternative. This method was applied to analyze water samples from various sources, including tap water and influents and effluents from local municipal wastewater treatment facilities. To the best of our knowledge, this is the first study to combine SBSE with TD-GC-M for PFCA extraction followed by solvent-free desorption using a thermal desorption unit prior to GC-MS analysis. These aspects not only fill a significant gap in the existing literature but

**NQ10_MMG008**

> 23 Briefly, the diluted samples were mixed with aqueous ammonium hydroxide solution, isopropyl alcohol, trifluoroethanol, water, internal standards, and methanol before being injected into a SCIEX ExionLC high- pressure liquid chromatography (HPLC) system.

**NQ10_MMG009**

> (at LOQ). to methods that require very fast sample processing such as dilute and shoot, our method provides higher preconcentration and limits occurrence of matrix effects. To investigate the applicability of the developed SPME protocol to environmental samples, lake, river, tap and bottled water were analyzed and their matrix effects evaluated. Results shown in Fig. S14 , reveal that none of the model PFAS were detected in the an- alyzed matrices. The occurrence of matrix effects was also evalu- ated by testing, for each matrix collected, the accuracy of samples spiked at concentration levels of 15, 50 and 250 ng L − 1 , using the calibration curve equation obtained from the ultra-pure water calibration. As demonstrated in Table S4 , all points fall within the established line of best ﬁt for the calibration performed in ultra- pure water, accuracy being between 70 and 130% for all the spiked samples and RSD being less than 10% for most analytes. PFOA and PFOS had accuracy values lower or higher than the acceptable lim- its for some water samples. For PFOA, values at 15 ng L − 1 for bottled, lake and tap water while at 50 ng L − 1 for bottled, lake and river water samples and that of PFOS was lake water at 15 ng L − 1 .

**NQ10_MMG010**

> Furthermore, substantial matrix effects can occur from the samples during analysis, mak- ing the method not suitable and robust for such complex samples.

### Anonymous candidate answer

1. Answerability 
answerable – General principles and common preconcentration approaches for PFAS before MS are well established, but matrix- and method-specific details are variable and protocol-level parameters cannot be specified without literature.

---

2. Answer 

PFAS are typically preconcentrated to (1) enrich analytes from large or complex sample volumes, (2) remove matrix components that cause ion suppression, and (3) convert analytes into a form compatible with LC–MS(/MS) or GC–MS. The dominant tools are solid-phase extraction (SPE), liquid–liquid extraction (LLE), dispersive extraction/cleanup, and, for some methods, instrumental preconcentration (e.g., online SPE).

Below is how this breaks down by matrix, analyte class, and MS method.

---

### 2.1. Core preconcentration strategies

Across matrices, the main strategies are:

- **Off‑line SPE** (most common for PFAS)
 - Load a relatively large sample volume (mL to L) onto an SPE cartridge or disk.
 - Retain PFAS by hydrophobic, ionic, or mixed‑mode interactions.
 - Wash to remove matrix interferences.
 - Elute PFAS in a small volume of strong solvent (e.g., organic with modifier) compatible with LC–MS/MS.
- **Online SPE / trap cartridges**
 - A smaller-volume SPE performed automatically within the LC system.
 - Sample is injected, PFAS retained on a trap, then back‑flushed onto the analytical column.
- **Liquid–liquid extraction (LLE) / dispersive extraction**
 - Partition PFAS into an organic phase (more common for nonionic or neutral precursors and shorter chain compounds, and in GC‑amenable workflows).
- **Protein precipitation + cleanup**
 - For biological fluids: add organic solvent, precipitate proteins, then perform SPE or direct injection with further cleanup.
- **Evaporation and reconstitution**
 - After SPE/LLE, eluent is concentrated by gentle evaporation and reconstituted in a smaller volume of LC‑compatible solvent to increase analyte concentration.

---

### 2.2. How protocols vary by matrix

#### (a) Drinking water and ground/surface water

**Goals:** High preconcentration factor, minimal background; matrices are relatively clean but PFAS at very low ng/L or pg/L.

- **Approach:**
 - Large‑volume **off‑line SPE** with weakly basic/anion‑exchange or reversed‑phase cartridges is typical.
 - Sample pH, ionic strength, and organic carbon content are controlled because ionization state (anionic vs neutral) affects retention.
 - Final elution in a small volume (hundreds of µL) of organic solvent, sometimes with ammonium-based modifiers, then partial evaporation and reconstitution for LC–MS/MS.
- **Variation factors:**
 - **Anionic PFAS (PFCAs/PFSAs):** Strong or weak anion exchange or mixed‑mode cartridges are common.
 - **Zwitterionic/neutral or emerging PFAS:** More reliance on mixed‑mode or more hydrophobic sorbents; sometimes dual‑cartridge schemes.
 - **Targeted vs suspect/non‑target:** For broad screening, conditions are often less aggressive in pH and wash strength to retain a wider polarity range, with some sacrifice in cleanliness.

#### (b) Wastewater, industrial effluents, landfill leachate

**Goals:** High preconcentration, but also aggressive **matrix cleanup** because of organics and surfactants.

- **Approach:**
 - Often pre‑filtration and sometimes dilution to control foaming and particulate load.
 - **Off‑line SPE** is still primary, but:
 - Stronger or additional wash steps to remove organic matter and surfactants.
 - pH adjustment optimized to keep PFAS in charged form where desired.
 - Post‑SPE: evaporation and reconstitution in LC solvent.
- **Variation factors:**
 - Stronger washes and/or sequential sorbents (e.g., first capture bulk organics, then PFAS) for very dirty matrices.
 - For volatile/semivolatile PFAS or certain precursors, LLE or headspace techniques may be added.

#### (c) Serum, plasma, whole blood

**Goals:** Remove proteins, phospholipids, and endogenous lipids; avoid PFAS loss to tube and protein binding; moderate enrichment.

- **Approach:**
 - **Protein precipitation:** Add organic solvent (e.g., acetonitrile or methanol), vortex, centrifuge; supernatant contains PFAS.
 - Often followed by **SPE** on the supernatant to further clean and concentrate.
 - Final extract volume is typically small (tens to hundreds of µL) for LC–MS/MS.
- **Variation factors:**
 - Choice of precipitation solvent and ratio affects recovery of long‑ vs short‑chain PFAS and precursors.
 - Some workflows use **dilute‑and‑shoot** (no SPE) when sensitivity allows, sacrificing some matrix cleanup.
 - Different protocols for **plasma vs serum** due to clotting factors and protein content.

#### (d) Tissues, organs, biota (fish, liver, etc.)

**Goals:** Release PFAS from solid matrices, remove lipids and proteins, then concentrate.

- **Approach:**
 - **Homogenization** with aqueous/organic mixtures; sometimes enzymatic digestion.
 - Followed by:
 - **LLE** into an organic phase, and/or
 - **SPE** from an aqueous-organic mixture after dilution.
 - Additional **lipid removal** (e.g., dispersive sorbents or gel permeation) may precede SPE.
- **Variation factors:**
 - High‑fat matrices require more aggressive lipid cleanup, which can lower recovery of some PFAS if conditions are too strong.
 - Short-chain PFAS can be lost if extraction is tuned only for long-chain compounds.

#### (e) Soil, sediment, sludge, biosolids

**Goals:** Extract strongly sorbed PFAS from solids; reduce co‑extracted organic matter; achieve reasonable enrichment.

- **Approach:**
 - Weigh solid, add extraction solvent (often aqueous/organic with pH control), shake/sonicate or use pressurized liquid extraction.
 - Centrifuge/decant extract; sometimes repeat and combine.
 - Dilute and apply **SPE** for cleanup and further preconcentration.
- **Variation factors:**
 - Extraction solvent composition and pH to mobilize both ionic and neutral PFAS from mineral and organic phases.
 - Additional cleanup (e.g., dispersive sorbents) for high‑organic soils and sludges.

#### (f) Air, dust

**Goals:** Capture PFAS from air or particulate matrices; concentrate into small volumes.

- **Approach (air):**
 - Collection on filters and/or sorbent media (e.g., adsorbent tubes) followed by **solvent extraction** (Soxhlet, ultrasonic, or pressurized).
 - Extract often then subjected to **SPE** for cleanup/preconcentration prior to LC–MS/MS or GC–MS.
- **Approach (dust):**
 - Weigh dust, extract with solvent (often organic or mixed), centrifuge, then **SPE** cleanup and concentration.
- **Variation factors:**
 - Volatile/semi‑volatile PFAS and neutral precursors may be treated more with GC‑compatible workflows and volatility‑preserving collection.

#### (g) Food, consumer products

**Goals:** Extract PFAS from complex matrices, remove fats, proteins, pigments; achieve moderate enrichment.

- **Approach:**
 - Extraction (often similar to QuEChERS‑style or aqueous/organic mixtures).
 - Cleanup with dispersive sorbents (e.g., for pigments and lipids), then **SPE** for PFAS enrichment.
- **Variation factors:**
 - Fat content and water content dictate extraction solvent mix.
 - Protocols vary to balance recovery of very polar, very hydrophobic, and precursor PFAS.

---

### 2.3. Variation by analyte type

#### (a) Anionic perfluoroalkyl acids (PFAAs: PFCAs, PFSAs)

- Typically targeted by **anion-exchange or mixed-mode SPE** from aqueous matrices.
- In complex matrices, additional steps (protein precipitation, lipid removal) precede the PFAS-specific extraction.
- Shorter-chain PFAAs are more polar and can be more difficult to retain; protocols often adjust pH, ionic strength, and loading volume to improve capture.

#### (b) Zwitterionic, cationic, and neutral PFAS

- Often require **mixed-mode** or modified reversed-phase sorbents to capture both ionic and hydrophobic contributions.
- Some neutral precursors may be more amenable to LLE than strongly ionic compounds.
- Preconcentration must be tuned so that:
 - pH does not cause analyte loss (e.g., making a zwitterion unretained), and
 - elution solvent is strong enough to desorb both ionic and hydrophobic species without causing precipitation or sample loss.

#### (c) Polyfluoroalkyl precursors and polymers

- For **oxidizable precursors** (e.g., in total oxidizable precursor (TOP) assays), the preconcentration is often done **before oxidation** on the native precursors or **after oxidation** on the resulting PFAAs, with protocols chosen accordingly.
- **Polymeric PFAS** may not preconcentrate well via typical SPE; specialized large-molecule or size-exclusion approaches may be used, or they may require separate workflows (including combustion and total F or EOF/AOF methods).

---

### 2.4. Variation by MS method and analytical approach

#### (a) LC–MS/MS (targeted)

- Dominant method for ionic and polar PFAS.
- Preconcentration emphasizes:
 - Efficient **capture and cleanup** to minimize ion suppression.
 - Final extract in LC‑compatible solvent (water/organic with volatile buffers).
- For targeted analyses, conditions can be optimized to maximize recovery of a defined analyte list, potentially sacrificing more exotic PFAS.

#### (b) LC–HRMS (suspect/non‑target)

- Wider analyte space and unknowns.
- Preconcentration is often **less aggressive** in washes and pH extremes to avoid losing unknown PFAS.
- Cleanup must be sufficient to control matrix effects but not so selective that it excludes classes of interest; mixed-mode and broader-scope sorbents are common.

#### (c) GC–MS / GC–MS/MS

- Used for more volatile or derivatized PFAS (e.g., some fluorotelomer alcohols, sulfonamides).
- Preconcentration often relies on:
 - **LLE** and solvent exchange to a low‑polarity GC‑compatible solvent.
 - Sometimes **solid-phase microextraction (SPME)** or sorbent tubes followed by thermal desorption.
- Derivatization steps may be included pre‑ or post‑extraction to enhance volatility.

#### (d) Total fluorine / EOF / AOF workflows

- When measuring extractable or adsorbable organic fluorine, preconcentration can involve:
 - **Broad‑spectrum extraction** (solid or aqueous phase) with minimal selectivity.
 - Combustion of extracts followed by fluoride detection.
- Preconcentration is less about individual PFAS and more about capturing as much organic F as possible; typically less selective cleanup, but still some steps to remove inorganic fluoride and matrix.

---

3. Uncertainty and limitations 

- Specific cartridge chemistries, pH values, solvent compositions, and volumes are highly method- and lab-dependent and cannot be reliably specified without direct literature or SOP access. 
- Recovery, matrix effects, and selectivity can vary markedly between protocols; even within a matrix type (e.g., “wastewater”), no single preconcentration strategy is universally optimal. 
- Emerging PFAS classes and highly polar or high‑molecular‑weight compounds may not be well captured by conventional preconcentration methods, and approaches are actively evolving.

---

4. Practical takeaway 

PFAS preconcentration before MS is dominated by SPE (often combined with protein precipitation, extraction, and cleanup) but the specific protocol is strongly tailored to the matrix (water vs biological vs solid), the PFAS classes targeted (ionic acids vs neutrals/precursors vs total fluorine), and the MS method (LC–MS/MS vs LC‑HRMS vs GC–MS); choosing or developing a method requires matrix‑specific optimization of sorbent chemistry, pH, wash strength, and elution/evaporation steps to balance recovery, breadth, and matrix suppression.

### Human label

- Adequate (`yes` / `no` / `uncertain`):
- Material scientific error (`yes` / `no` / `uncertain`):
- Confidence (`high` / `medium` / `low`):
- Notes:

---

## D13-A005

**Question ID:** `NQ12`

**Question:** What chain-length-related differences in PFAS analytical sensitivity or LOD/LOQ have been reported, and how do method or instrument settings affect them?

**Must include:** Must recognize compound-dependent analytical behavior; must connect calculation or interpretation to method/instrument conditions.

**Must not claim:** Must not claim one universal LOD/LOQ calculation or performance pattern applies identically to all PFAS chain lengths.

### Reference evidence

**NQ12_MMG001**

> In the same way, satisfactory repeatability was observed, with RSD values below 22% for intra-day precision, and in the range of 17–29% for inter-day precision, except in the case of PFOA, where lower precision between independent days was observed (38%). Nanomaterials 2022, 12, 1441 11 of 16 Table 2. Analytical ﬁgures of merit of the developed SPE-UHPLC-MS/MS method for C8–C14 PFASs from water samples. Compound Linearity a (µg L−1) Sensitivity (ng L−1) Extraction Efﬁciency (%) EF Repeatability RSD (%) LOD LOQ Intra-Day Inter-Day PFOA 2–50 4 12 66 ± 20 132 22 38 PFNA 4–50 7 22 110 ± 30 212 16 28 PFOS 2–50 3 9 110 ± 30 212 19 29 PFDA 5–50 8 24 77 ± 16 154 15 21 PFUnDA 4–50 7 21 73 ± 15 145 17 21 PFDS 2–50 3 11 67 ± 14 134 21 21 PFDoDA 4–50 6 18 75 ± 13 151 13 17 PFTrDA 5–50 8 25 68 ± 17 136 14 25 PFTeDA 2–50 3 11 61 ± 14 121 18 23 a Referred to the ﬁnal injection solution. Table 3.

**NQ12_MMG002**

> Overall, our developed method maintains a balance between methodological simplicity and analytical performance, avoiding the need for more complex and costly MS/MS systems. Table 2. Performance parameters of SBSE-TD-GC-MS for PFCA analysis: linearity, recovery, and sensitivity data. Analyte Retention Time (min) Parent Ion (m/z) Coefficient of Determination (R2) % Recovery (±SD) LOD (ng/L) LOQ (ng/L) MDL (ng/L) PFHpA 5.884 405 0.9984 97 ( ±11) 21.17 138.27 293.96 PFOA 6.640 455 0.9948 94 ( ±11) 21.20 103.13 495.37 PFNA 7.614 505 0.9956 86 ( ±5) 30.12 90.80 980.37 PFDA 8.448 555 0.9893 91 ( ±10) 54.29 169.85 888.30 PFUnA 9.416 605 0.9892 88 ( ±10) 34.39 132.90 1227.97 PFDoA 10.002 655 0.9925 85 ( ±8) 73.96 192.01 1458.84 PFTeDA 11.422 755 0.9906 85 ( ±3) 35.02 107.10 925.13

**NQ12_MMG003**

> As expected, in-source fragmentation of the carboxylic acids was instead influenced by the voltage of the fragmentor: with 60 V, the signal of short-chain PFAS (C < 5) was almost lost, so 60 V was discarded;

### Anonymous candidate answer

1. Answerability 
partially_answerable – Some specific chain-length effects on PFAS LOD/LOQ and qualitative method‑dependence are documented, but data are sparse and not consistent enough to define a universal trend.

2. Answer 

Reported chain‑length effects on sensitivity (LOD/LOQ) 

- In an SBSE–TD–GC–MS method for PFCAs (C7–C14), LODs and LOQs varied with chain length but did not follow a simple monotonic pattern. 
 - PFHpA (C7): LOD 21.17 ng/L; LOQ 138.27 ng/L. 
 - PFOA (C8): LOD 21.20 ng/L; LOQ 103.13 ng/L. 
 - PFNA (C9): LOD 30.12 ng/L; LOQ 90.80 ng/L. 
 - PFDA (C10): LOD 54.29 ng/L; LOQ 169.85 ng/L. 
 - PFUnA (C11): LOD 34.39 ng/L; LOQ 132.90 ng/L. 
 - PFDoA (C12): LOD 73.96 ng/L; LOQ 192.01 ng/L. 
 - PFTeDA (C14): LOD 35.02 ng/L; LOQ 107.10 ng/L. 
 - Across these, LODs ranged from 21.17–73.96 ng/L and LOQs were all <200 ng/L. 
 Interpretation: for this GC–MS method with SBSE preconcentration, mid‑to‑long chain PFCAs showed comparable ppt‑level sensitivity, but with somewhat higher LOD/LOQ around C10–C12; there is no simple “longer is always more sensitive” rule in this configuration.

- In an LC–MS/MS method used for PFAS adsorption studies, most PFAS had an LOQ of 0.01 µg/L, but the LOQ was substantially worse for the very short‑chain carboxylates: 
 - PFBA (C4 PFCA): LOQ 0.1 µg/L. 
 - PFPeA (C5 PFCA): LOQ 0.02 µg/L. 
 - All other PFAS except PFOS: LOQ 0.01 µg/L. 
 - PFOS (a long‑chain sulfonate) also had a higher LOQ (0.02 µg/L) under the same method. 
 Interpretation: under this reversed‑phase LC–MS/MS setup, the shortest‑chain PFCAs (C4, C5) required higher reporting limits than C6+ homologues, consistent with lower analytical sensitivity for short‑chain PFAS in a standard method; PFOS also showed somewhat poorer sensitivity than most other PFAS in this panel.

- A surface‑science/meta‑analysis paper notes that air‑water interfacial partition coefficients (K_aw) increase with PFAS chain length, and explicitly connects this to analytical sensitivity: 
 - K_aw is proportional to chain length or molecular size. 
 - As a result, “measurement sensitivity may vary across PFAS, and in particular may be more limited for shorter‑chain PFAS in systems with smaller [specific interfacial area].” 
 - In several studies, this limited sensitivity for shorter‑chain PFAS manifested as enrichment factors that were indistinguishable from 1 within measurement uncertainty. 
 Interpretation: in air‑water interface measurement systems with limited interfacial area, shorter‑chain PFAS produce weaker signals (smaller mass at the interface), effectively raising their practical LOD relative to longer‑chain analogues.

Collectively, these examples support two recurring but method‑dependent patterns:

- Very short‑chain PFAS (especially C4–C5 PFCAs and ultrashort PFAS) tend to have worse sensitivity (higher LOQ/LOD) than C6+ homologues under standard reversed‑phase LC–MS/MS and some interfacial measurement setups. 
- For mid‑to‑long‑chain PFCAs in a GC–MS method with sorptive preconcentration, sensitivity differences with chain length exist but are modest and not strictly monotonic. 

Influence of method and instrument settings 

- Preconcentration and sample preparation 
 - Parts‑per‑trillion (low ng/L) PFAS detection typically relies on preconcentration by SPE or LLE; omitting these or using “dilute‑and‑shoot” sacrifices sensitivity. 
 - Because short‑chain PFAS are more polar and less retained, insufficiently strong extraction/preconcentration tends to hurt their recoveries and thus their LOD/LOQ disproportionately, which is consistent with the higher LOQs for PFBA and PFPeA under the same LC–MS/MS method.

- Chromatographic conditions and column chemistry 
 - One study explicitly used different LC columns for different chain‑length ranges: a C18 column for PFAS with C4 and above, and a Polar‑X column for ultrashort‑chain PFAS (C ≤ 3). 
 - This implies that standard reversed‑phase conditions are inadequate for very short‑chain PFAS retention/separation, necessitating tailored stationary phase and gradient design to obtain usable signal (i.e., practical sensitivity) for C1–C3 compounds. 
 - In the GC method, SBSE preconcentration plus thermal desorption was critical to reach ppt‑range LODs for C7–C14 PFCAs with a single‑quadrupole MS; without this strong sorptive preconcentration, LODs would be substantially higher.

- Mass spectrometer mode and acquisition parameters 
 - In LC–MS/MS studies, PFAS are commonly measured in negative electrospray ionization with MRM transitions; for some analytes (e.g., zwitterionic PFAS) positive mode and different transitions are required, which changes sensitivity compound‑by‑compound (though the provided chunk only notes mode switching, not LOD by chain). 
 - LOD and LOQ in one LC/q‑TOF method were defined based on deprotonated‑ion signal‑to‑noise ratios of 3 and 10, respectively, so any change in MS tuning, background noise, or transition choice directly affects numeric LOD/LOQ for each PFAS in the panel. 
 - In the SBSE–TD–GC–MS PFCA method, a single‑quadrupole MS (not MS/MS) was used; despite that, careful optimization of preconcentration and desorption allowed ppt‑range LODs across C7–C14, indicating that sensitivity differences across homologues there are dominated more by extraction/desorption and chromatographic behavior than by MS stage count.

- Geometric/phase‑ratio settings in interfacial measurements 
 - For air‑water interface adsorption experiments, analytical sensitivity is a function of both K_aw and the specific interfacial area (surface‑area‑to‑volume ratio); smaller resolved interface thickness (i.e., larger SAV) yields higher sensitivity. 
 - Because K_aw increases with chain length, longer‑chain PFAS benefit more from a given SAV than short‑chain PFAS; conversely, in systems with small SAV, shorter‑chain PFAS may fall below practical detection even when longer‑chain analogues are quantifiable.

3. Uncertainty and limitations 

- The provided data cover limited sets of compounds (mostly PFCAs and a small panel in one LC–MS/MS study) and specific instruments; they do not establish universal numeric relationships between chain length and LOD/LOQ across all PFAS classes or platforms. 
- Observed trends (e.g., poorer sensitivity for PFBA/PFPeA) may reflect combined effects of extraction efficiency, chromatographic retention, ionization, and background contamination under that particular method; they are not guaranteed to generalize to differently optimized methods. 
- No supplied chunk reports a full, chain‑resolved LOD/LOQ series for both very short, medium, and very long chains within the same LC–MS/MS method, so fine‑grained quantitative comparison of chain‑length effects is not possible here.

4. Practical takeaway 

Within specific analytical methods, very short‑chain PFAS often show higher LOQs/LODs (lower sensitivity) than C6+ homologues, and sensitivity across a PFAS series is strongly shaped by preconcentration strategy, column chemistry, phase ratios, and MS acquisition settings; optimizing these components—especially for retention and extraction of short‑chain PFAS—is essential if comparable sensitivity across chain lengths is required.

### Human label

- Adequate (`yes` / `no` / `uncertain`):
- Material scientific error (`yes` / `no` / `uncertain`):
- Confidence (`high` / `medium` / `low`):
- Notes:

---

## D13-A006

**Question ID:** `WF10_004b`

**Question:** How can PFAS compound class or headgroup affect treatment performance or equilibrium behavior?

**Must include:** Compare studies only on matched compounds, matrices, endpoints, and conditions; avoid ranking technologies when the evidence is not comparable.

**Must not claim:** Do not convert a condition-specific finding into a universal PFAS treatment claim.

### Reference evidence

**WF10_004b_MMG001**

> from landfill leachate within seven hours of operation, with 98.3 % of perfluorosulfonic acids (PFSA) and 85.5 % of perfluorocarboxylic acids (PFCA) removed from the leachate.

**WF10_004b_MMG002**

> were significantly lower at higher GenX concentrations, with 1.00 mM and 2.00 mM achieving only (69.0 � 4.5) and (39.0 � 4.5) % defluorination, respectively. This suggests that either the adsorption of GenX on the anode or the concentration of generated oxidants was limiting for the cleavage of GenX C  F bonds. We have observed a similar concentration dependence of the defluorination of PFOS. [41] This indicates that the chemical identity of the PFAS headgroup did not govern the PFAS adsorption at laser-made [Ni 0.75 Fe 0.25 ]-(OH) 2 –hydrophilic carbon fiber paper anodes, but that anode characteristics, i. e. available adsorbent sites and particularly the generation of oxidant species (O *  ), are posing an upper limit to concentration for efficient PFAS defluorination. The equilibrium amount of adsorbed molecules increases with increasing solute concentration. [50–52] A higher number of adsorbed PFAS mole- cules contributes only to defluorination efficiency until all available adsorbent sites are saturated or all generated oxidant species are consumed within the anode microenvironment. The ability to defluorinate low PFAS concentrations is essential for practical applications. [1] Nevertheless, the chemical identity of the PFAS headgroup and the PFAS structure affect the bond

**WF10_004b_MMG003**

> Because FHxSA is likely neutral at pH 7.3 ( Nguyen et al., 2020 ) due to the sulfonamide headgroup, rejection by NF was consistently lower than the anionic analogue, PFHxS, attributed to the lack of an electrostatic repulsion rejection mechanism for this compound ( Fig.

**WF10_004b_MMG004**

> The adsorption capacity and affinity of the zeolite β are lower for the sulfonic acids than for the carboxylic acids, which is due to the more polar nature of the sulfonic moiety and the unlikely formation of sulfonic acid dimers.

**WF10_004b_MMG005**

> For example, the removal of PFHeA (55%, overall) was much less than that of PFHeS (96%, overall), and PFHxA was removed Y.

**WF10_004b_MMG006**

> Batch tests revealed that perfluorosulfonic acids (PFSAs) were more efficiently removed, with up to 94% removal, compared to perfluorocarboxylic acids (PFCAs), which showed up to 60% removal when using either ZVI or ZVI + BC.

**WF10_004b_MMG007**

> Similar to the behavior observed in batch mode, the column treatment demon - strated higher retention of sulfonate PFAS than carboxylate ones with equal perfluorocarbon chain lengths (e.g., 84 % PFOS versus 72 % PFNA removal, or 64 % PFHxS versus 44 % PFHpA), likely due to the greater effect of the sulfonate functional group.

### Anonymous candidate answer

1. Answerability 
answerable – The question can be answered at the level of general principles and mechanistic trends, but not with compound‑specific quantitative data.

2. Answer 

PFAS class (chain length, linear vs branched, functional headgroup, polymeric vs nonpolymeric) strongly influences both equilibrium behavior (e.g., sorption, partitioning) and treatment performance (e.g., adsorption, separation, degradation). The key effects are:

**A. Effect on equilibrium behavior**

1. **Hydrophobicity vs polarity (chain length and functional group)** 
 - **Long‑chain perfluoroalkyl acids (PFAAs)** (e.g., long‑chain PFCAs and PFSAs) are more hydrophobic and surface active than short‑chain analogues. 
 - **Long‑chain sulfonates (PFSAs)** are generally more hydrophobic and surface‑active than perfluorocarboxylates (PFCAs) of the same chain length. 
 Consequences:
 - **Stronger sorption to organic matter and GAC/resin** for long‑chain, especially sulfonates. 
 - **Greater air–water interfacial adsorption** for longer‑chain and sulfonate PFAS (important for foam fractionation, air sparging, column tailing, etc.). 
 - **Short‑chain PFAS** remain more mobile in groundwater, have lower sorption coefficients, and break through faster in adsorbers.

2. **Ionic form and headgroup charge** 
 - Most PFAAs exist as **anions** at environmental pH. 
 - Headgroup type (sulfonate vs carboxylate vs sulfonamide/sulfonamidoacetic vs zwitterionic/neutral) changes polarity, pKa (if any), and charge distribution. 
 Consequences:
 - **Anionic headgroups** drive strong electrostatic attraction to **strong‑base anion exchange resins**; sorption depends on both hydrophobic tail and charge interactions. 
 - **Zwitterionic or neutral PFAS precursors** (e.g., some FTOHs, some betaines) sorb more like nonionic organics: more dependent on hydrophobic interactions, less on ion exchange. 
 - Speciation‑sensitive PFAS (if present) may change sorption with pH, ionic strength, and competing anions.

3. **Linear vs branched isomers** 
 - Branched isomers typically have **slightly lower hydrophobicity and different molecular packing** than linear analogues. 
 Consequences:
 - **Weaker sorption and earlier breakthrough** on GAC/resins compared with linear isomers of the same chain length. 
 - Slightly **different air–water interfacial behavior**, potentially affecting foam‑based separations and chromatographic retention.

4. **Polymeric vs nonpolymeric PFAS** 
 - Side‑chain fluorinated polymers and fluoropolymers behave differently from small‑molecule PFAS. 
 Consequences:
 - Apparent “PFAS” may be dominated by **polymer‑bound side chains** that are not readily sorbed or separated like small PFAAs. 
 - Polymers act as **precursor reservoirs**, slowly releasing small PFAAs over time; equilibrium is then governed by both polymer–water partitioning and transformation.

5. **Micelle and aggregate formation** 
 - At high concentrations, surface‑active PFAS (especially long‑chain PFSAs) can form **micelles or aggregates**. 
 Consequences:
 - Changes in **apparent solubility** and **activity coefficient**, altering effective partitioning to sorbents, membranes, and interfaces. 
 - Non‑ideal behavior in equilibrium models that assume monomeric species.

**B. Effect on treatment performance**

1. **Adsorption (GAC, PAC, resins, natural sorbents)** 
 - **Long‑chain > short‑chain** for adsorption capacity and affinity on most carbonaceous sorbents. 
 - **PFSAs > PFCAs** of equal chain length in sorption strength. 
 - Anion exchange:
 - Strong‑base resins: **anionic PFAAs** (especially long chain) are well removed; short‑chain are less but still often better than on GAC. 
 - Neutral/zwitterionic precursors may pass through unless the resin has specific hydrophobic domains. 
 - Branched isomers tend to **break through earlier** than linear isomers. 

2. **Membrane processes (RO, NF, UF, MF)** 
 - **RO/NF**: Rejection generally increases with **chain length** and **charge density**. Short‑chain PFAAs and neutral precursors are harder to reject than long‑chain anionic PFAS. 
 - **Headgroup**:
 - Anionic PFAS are rejected by both **size exclusion and charge repulsion** (if membrane is negatively charged). 
 - Neutral/zwitterionic PFAS rely more on size/hydrophobic interactions; rejection may be lower. 
 - **UF/MF** generally do not directly remove dissolved PFAS, but polymeric PFAS, PFAS‑colloid complexes, or foam/air‑water interfaces may be partially rejected depending on aggregation behavior.

3. **Foam fractionation and air‑based processes** 
 - Efficiency scales strongly with **surface activity**:
 - Long‑chain, especially sulfonates, are efficiently enriched in foam. 
 - Short‑chain PFAAs and more polar/neutral PFAS exhibit poorer enrichment. 
 - Branched vs linear can alter foam stability and enrichment but less strongly than chain length and headgroup.

4. **Oxidation, reduction, and other destructive treatments** 
 - **Headgroup** strongly influences reaction pathways:
 - Carboxylate vs sulfonate vs sulfonamide have different bond dissociation energies and intermediates. 
 - **Perfluorinated headgroup PFAAs** (fully fluorinated tail, carboxylate/sulfonate) are often more chemically persistent than many **precursors** that bear ether, sulfonamide, or unsaturated moieties. 
 - Some oxidative processes preferentially transform precursors to PFAAs without complete mineralization. 
 - For reductive/advanced reduction processes, the **electron distribution around the headgroup** can alter initial electron attack and defluorination efficiency.

5. **Biological treatment** 
 - **Small, nonionic/less polar precursors** (e.g., some FTOHs, sulfonamides) are more susceptible to biological transformation than terminal PFAAs. 
 - Headgroup dictates the biotransformation pathway and the **identity of stable end‑products** (often PFCAs or PFSAs). 
 - Terminal PFAAs (especially long‑chain) are generally **poorly biodegradable**, with removal mainly governed by sorption to sludge or biofilms, which again depends on chain length and headgroup (PFSAs > PFCAs).

6. **Co‑contaminant and matrix effects mediated by PFAS class** 
 - **Competition with other anions** (sulfate, nitrate, DOC) affects anion exchange performance differently for PFAS depending on headgroup charge density and hydrophobicity. 
 - **DOC and surfactants** can solubilize or complex some PFAS classes, reduce effective sorption, or alter air–water interfacial behavior. 
 - PFAS that are **more strongly sorbed to solids or biomass** (long‑chain sulfonates) may show delayed breakthrough and slow desorption tails, while more mobile classes track more closely with bulk water.

3. Uncertainty and limitations 

- These are generalized mechanistic trends; actual behavior depends on specific PFAS structures (including ethers, multiple headgroups), environmental conditions (pH, ionic strength, DOC), and material properties (e.g., resin functionalization, carbon pore distribution). 
- No quantitative adsorption coefficients, rejection values, or rate constants can be provided under the evidence constraint; relative rankings and qualitative patterns are used instead. 
- Some newer PFAS classes (e.g., diverse ether acids, cationic/zwitterionic PFAS) may deviate from the patterns derived mostly from classic PFSAs and PFCAs.

4. Practical takeaway 

When screening or designing PFAS treatment, explicitly classify target PFAS by chain length, headgroup type/charge, and branching: long‑chain anionic sulfonates will generally be easiest to remove by adsorption and interfacial methods, while short‑chain, neutral/zwitterionic, and some branched or polymeric PFAS will be more mobile, less adsorbable, and may require higher‑pressure membranes or destructive processes tailored to their specific headgroup chemistry.

### Human label

- Adequate (`yes` / `no` / `uncertain`):
- Material scientific error (`yes` / `no` / `uncertain`):
- Confidence (`high` / `medium` / `low`):
- Notes:

---

## D13-A007

**Question ID:** `NQ12`

**Question:** What chain-length-related differences in PFAS analytical sensitivity or LOD/LOQ have been reported, and how do method or instrument settings affect them?

**Must include:** Must recognize compound-dependent analytical behavior; must connect calculation or interpretation to method/instrument conditions.

**Must not claim:** Must not claim one universal LOD/LOQ calculation or performance pattern applies identically to all PFAS chain lengths.

### Reference evidence

**NQ12_MMG001**

> In the same way, satisfactory repeatability was observed, with RSD values below 22% for intra-day precision, and in the range of 17–29% for inter-day precision, except in the case of PFOA, where lower precision between independent days was observed (38%). Nanomaterials 2022, 12, 1441 11 of 16 Table 2. Analytical ﬁgures of merit of the developed SPE-UHPLC-MS/MS method for C8–C14 PFASs from water samples. Compound Linearity a (µg L−1) Sensitivity (ng L−1) Extraction Efﬁciency (%) EF Repeatability RSD (%) LOD LOQ Intra-Day Inter-Day PFOA 2–50 4 12 66 ± 20 132 22 38 PFNA 4–50 7 22 110 ± 30 212 16 28 PFOS 2–50 3 9 110 ± 30 212 19 29 PFDA 5–50 8 24 77 ± 16 154 15 21 PFUnDA 4–50 7 21 73 ± 15 145 17 21 PFDS 2–50 3 11 67 ± 14 134 21 21 PFDoDA 4–50 6 18 75 ± 13 151 13 17 PFTrDA 5–50 8 25 68 ± 17 136 14 25 PFTeDA 2–50 3 11 61 ± 14 121 18 23 a Referred to the ﬁnal injection solution. Table 3.

**NQ12_MMG002**

> Overall, our developed method maintains a balance between methodological simplicity and analytical performance, avoiding the need for more complex and costly MS/MS systems. Table 2. Performance parameters of SBSE-TD-GC-MS for PFCA analysis: linearity, recovery, and sensitivity data. Analyte Retention Time (min) Parent Ion (m/z) Coefficient of Determination (R2) % Recovery (±SD) LOD (ng/L) LOQ (ng/L) MDL (ng/L) PFHpA 5.884 405 0.9984 97 ( ±11) 21.17 138.27 293.96 PFOA 6.640 455 0.9948 94 ( ±11) 21.20 103.13 495.37 PFNA 7.614 505 0.9956 86 ( ±5) 30.12 90.80 980.37 PFDA 8.448 555 0.9893 91 ( ±10) 54.29 169.85 888.30 PFUnA 9.416 605 0.9892 88 ( ±10) 34.39 132.90 1227.97 PFDoA 10.002 655 0.9925 85 ( ±8) 73.96 192.01 1458.84 PFTeDA 11.422 755 0.9906 85 ( ±3) 35.02 107.10 925.13

**NQ12_MMG003**

> As expected, in-source fragmentation of the carboxylic acids was instead influenced by the voltage of the fragmentor: with 60 V, the signal of short-chain PFAS (C < 5) was almost lost, so 60 V was discarded;

### Anonymous candidate answer

1. Answerability 
partially_answerable – General mechanistic and methodological patterns are well understood, but specific “reported” LOD/LOQ values and study‑to‑study comparisons require literature I cannot access here.

---

2. Answer 

Below is what can be stated reliably at a principle/mechanism level about chain length vs sensitivity, and how method/instrument settings modulate those effects.

### A. General chain‑length trends in LC‑MS(/MS) sensitivity for PFAS

For typical reversed‑phase LC–ESI–MS(/MS) methods used in water and biota:

1. **Short‑chain PFAS (very polar, e.g., C2–C4 perfluorocarboxylates or very short sulfonates)** 
 Common issues that *tend to* worsen LOD/LOQ:
 - **Poor chromatographic retention** on conventional C18 or similar phases 
 - Elute very early, often near the void volume. 
 - Co‑elute with a large portion of the matrix, leading to strong **ion suppression**. 
 - **Strong dependence on mobile phase composition** 
 - If the early‑time mobile phase is highly aqueous with significant salts/buffers, the matrix ions can dominate and suppress signal. 
 - **Limited preconcentration by SPE** on common reversed‑phase or weak‑anion exchange sorbents 
 - Recoveries are often lower and more variable, restricting how much sample can effectively be loaded and thereby limiting sensitivity.

 Net practical effect: in many routine methods, **LODs/LOQs are often higher (worse) for the very short‑chain PFAS than for mid‑chain analogues**, unless the method is specifically optimized for them (e.g., HILIC, tailored SPE, or careful early‑gradient control).

2. **Mid‑chain PFAS (often regulatory targets, e.g., C6–C9 PFCAs, C4–C8 PFSAs)** 
 These often show **the best combination of chromatographic behavior and ionization efficiency**:
 - **Adequate hydrophobicity** for retention and separation from early‑eluting matrix, reducing ion suppression. 
 - Still sufficiently polar to ionize efficiently in negative‑mode ESI with appropriate buffers. 
 - SPE and other preconcentration approaches perform relatively well. 

 Net effect: for many “generalist” PFAS LC‑MS/MS methods, **mid‑chain PFAS frequently exhibit the lowest (best) LODs/LOQs** in the analyte panel.

3. **Long‑chain PFAS (e.g., ≥C10 PFCAs, ≥C8 PFSAs, fluorotelomer sulfonates/alcohols)** 
 Potential issues that can **degrade sensitivity despite strong retention**:
 - **Surface adsorption / memory effects** 
 - Strong binding to tubing, vials, and column can lead to sample loss and carryover. 
 - **Broader or tailing peaks** 
 - Increases noise relative to peak height, impacting signal‑to‑noise (S/N) and practical LOQ. 
 - **Ionization behavior may plateau or decrease** with increasing chain length in some systems. 
 - **Slower desorption from droplets** in ESI and more involvement of non‑covalent aggregates can reduce effective ion yield. 

 Net effect: **long‑chain PFAS do not necessarily have the best (lowest) LODs**, even though they retain strongly; sensitivity can be limited by adsorption and less favorable ionization or peak shape.

4. **Functional group differences overlaid on chain length** 
 At a given chain length:
 - **Sulfonates (PFSAs)** often ionize somewhat more strongly than analogous **carboxylates (PFCAs)** in negative ESI, which can yield better S/N and lower LODs/LOQs under the same conditions. 
 - **Neutral or zwitterionic precursors (e.g., some fluorotelomer alcohols, sulfonamides)** often show poorer ionization in standard negative‑mode LC‑ESI methods, with higher LODs, unless positive mode or different ionization conditions are optimized.

---

### B. How method and instrument settings shape these chain‑length effects

1. **Chromatographic mode and column selection**

 - **Reversed‑phase (RP) C18 or similar** 
 - Tends to favor **mid‑ to long‑chain PFAS**: strong retention, separation from early matrix. 
 - Short‑chain PFAS often elute near the void; this amplifies the intrinsic chain‑length trend (short‑chain having worse LODs).
 - Adjusting **column chemistry** (e.g., polar‑embedded C18, mixed‑mode anion‑exchange) can improve **retention and peak shape of short‑chain PFAS**, lowering their LODs relative to standard C18.

 - **Hydrophilic interaction chromatography (HILIC) or mixed‑mode (anion exchange + RP)** 
 - Can markedly **improve retention and separation** of very short‑chain PFAS from matrix ions, improving their sensitivity.
 - Might modestly diminish retention of very long‑chain PFAS or alter elution order, which can change where suppression occurs.

 Practical implication: **Column and mode choice are often the most powerful levers for flattening chain‑length differences in LOD/LOQ**, particularly improving very short‑chain analytes.

2. **Mobile phase composition and gradient**

 - **Initial % organic** 
 - Higher initial organic (in RP) can reduce retention of short‑chain PFAS and worsen their co‑elution with matrix. 
 - Lower initial organic and a slower early gradient can let short chains separate from the immediate matrix front, improving S/N.

 - **Buffer type and ionic strength** 
 - PFAS typically rely on **negative‑mode ESI**, so **volatile ammonium buffers at modest ionic strength** are commonly used. 
 - High salt or excessive buffer can:
 - Increase competition in the ESI process, often **worsening sensitivity of early‑eluting, short‑chain analytes** already in matrix‑heavy regions.
 - Differentially affect ionization efficiency across chain lengths, sometimes altering relative responses.

 - **pH** 
 - Most PFAS acids are strongly acidic and deprotonated even at moderately low pH; chain‑length differences in ionization state are minimal in usual LC pH ranges. 
 - However, pH can strongly affect **matrix components**, altering suppression patterns at different retention times.

3. **Sample preparation and preconcentration**

 - **Solid‑phase extraction (SPE) sorbent type and conditions** 
 - **Reversed‑phase or weak‑anion‑exchange SPE** often shows decreasing recovery as PFAS become very short‑chain, worsening their effective LOD/LOQ relative to mid‑chain analytes. 
 - **Stronger anion exchange or specialized sorbents** can improve short‑chain retention and recovery, reducing chain‑length bias. 
 - Very long‑chain PFAS may have nearly quantitative recoveries but suffer from carryover and blank issues, effectively constraining LOD/LOQ.

 - **Sample volume and elution volume** 
 - Increasing sample volume primarily helps compounds with good and consistent recoveries (often mid‑chain). 
 - For short‑chain PFAS with poor recoveries, simply increasing volume may not proportionally improve LOD/LOQ unless recovery issues are solved.

 - **Matrix cleanup** 
 - Better removal of co‑extractives particularly benefits **early‑eluting short chains** where suppression is strongest. 
 - Long‑chain PFAS, being better separated chromatographically, can be less affected by residual matrix, though adsorptive losses may still dominate.

4. **Ionization source type and parameters**

 - **Electrospray ionization (ESI) in negative mode** is standard for ionic PFAS:
 - **Short‑chain PFAS**:
 - Sensitive to **source conditions that influence droplet desolvation and competition**: high matrix load at early retention times can strongly suppress them.
 - Optimizing **nebulizer gas, temperature, and desolvation** improves drying of small droplets and can partially alleviate suppression.
 - **Long‑chain PFAS**:
 - Strong surfactant character; can accumulate at droplet surfaces. 
 - Certain source settings (e.g., very high temperatures, high sheath gas) can promote or destabilize micelle‑like assemblies in droplets, affecting their ionization efficiency relative to mid‑chain compounds.

 - **Alternative sources (e.g., APCI, APPI)** 
 - Less commonly used for ionic PFAS, but when used, relative response by chain length can differ from ESI because ionization mechanisms differ; can sometimes benefit less polar precursors.

5. **Mass analyzer type, resolution, and acquisition strategy**

 - **Triple quadrupole in MRM mode (LC‑MS/MS)** 
 - Chain length sensitivity differences are directly reflected in **transition‑specific response**:
 - Different PFAS (and chain lengths) produce different predominant fragments and relative abundance patterns; selecting **high‑yield transitions with optimized collision energy** can improve LOD/LOQ for particular chain lengths. 
 - **Dwell time and cycle time** allocation affects S/N: if many MRM transitions are monitored simultaneously, short dwell times can worsen LODs, often hitting lower‑response analytes (which may be very short‑ or very long‑chain) hardest.

 - **High‑resolution MS (Orbitrap, TOF)** 
 - Typically **full‑scan or targeted SIM/PRM** modes:
 - Full‑scan acquisition spreads ion current over a wide m/z range, raising LOD compared to targeted MRM, but high resolving power can reduce background noise and interference. 
 - Chain length effects arise from:
 - Intrinsic ionization efficiency and gas‑phase stability of each homolog.
 - Where in the time‑of‑flight or orbital frequency spectrum the m/z lies (small effects).
 - **Targeted SIM/PRM** at high resolution can partially mitigate chain‑length sensitivity differences by improving S/N for weaker‑responding analytes.

6. **Injection volume and on‑column loading**

 - **Larger injection volumes** can lower LODs for analytes with:
 - Good chromatographic retention and peak shape. 
 - Minimal breakthrough or fronting.
 - For **short‑chain PFAS** with marginal retention:
 - Increasing injection volume can cause early peak broadening or breakthrough and **worsen** S/N, negating gains in mass loaded.
 - For **long‑chain PFAS**:
 - Excessive loading can increase tailing and carryover, complicating quantitation and blank levels more than it improves LOD.

---

3. Uncertainty and limitations 

- The above patterns are **general and mechanistic**, not based on any single study, and exceptions exist depending on matrix, instrument, and detailed method conditions. 
- No specific “reported” LOD/LOQ values, fold‑differences, or rank‑ordered sensitivity lists can be reliably cited without direct literature access. 
- Relative sensitivity across chain lengths for **precursor PFAS (e.g., fluorotelomer alcohols, sulfonamides)** is more method‑dependent than for ionic end‑products, and the generalizations given for ionic PFAS may not fully apply. 
- Matrix effects can **override intrinsic chain‑length trends** in practical methods; for example, a matrix with strong interference at the retention time of a particular mid‑chain PFAS can produce worse LOD than for a short‑chain congener in that specific setup.

---

4. Practical takeaway 

In typical LC‑ESI‑MS/MS PFAS methods, **mid‑chain PFCAs/PFSAs often exhibit the best LOD/LOQ, very short‑chain and very long‑chain PFAS often show poorer sensitivity**, and this pattern is strongly shaped by chromatographic retention, matrix co‑elution, extraction recoveries, and ion source/acquisition settings; flattening these chain‑length biases generally requires deliberate optimization of column chemistry, gradient, SPE, and MS parameters specifically for the weak‑responding ends of the homolog series.

### Human label

- Adequate (`yes` / `no` / `uncertain`):
- Material scientific error (`yes` / `no` / `uncertain`):
- Confidence (`high` / `medium` / `low`):
- Notes:

---

## D13-A008

**Question ID:** `WF10_036`

**Question:** Does longer empty-bed contact time necessarily translate into better PFAS performance in granular activated carbon systems?

**Must include:** Use limitation, uncertainty, caveat, and negative evidence to avoid overclaiming beyond the reported study scope.

**Must not claim:** Do not convert a condition-specific finding into a universal PFAS treatment claim.

### Reference evidence

**WF10_036_MMG001**

> 5 B), which means that the apparent adsorption capacity did not change as EBCT increased.

**WF10_036_MMG002**

> Table S8 shows that the ratios for the Lead + Lag to Lead column for q ΣPFAS were only slightly different from unity (1.07 ± 0.12), implying that adsorption mechanisms are inde- pendent of EBCT.

**WF10_036_MMG003**

> This indicates that longer EBCTs do not suffer from competing adsorbates (e.g., ionic species, DOC), and the similar breakthrough curve shapes suggest shorter EBCTs (i.e., ~2 –5 min) capture the mass transfer zone.

**WF10_036_MMG004**

> Although break- through curves for individual PFAAs did not perfectly overlap at the two EBCTs, consistent trends suggesting that either shorter or longer EBCTs resulted in lower CURs were not observed.

### Anonymous candidate answer

1. Answerability 
answerable – Multiple experimental and full‑scale GAC studies have directly examined how changing EBCT affects PFAS breakthrough and apparent capacity.

2. Answer 
Longer empty‑bed contact time (EBCT) does not necessarily translate into better PFAS performance in granular activated carbon systems.

- In controlled column tests with bituminous GAC (F400), increasing EBCT produced *steeper* PFAS breakthrough curves when plotted versus throughput (bed volumes treated), but the half‑breakthrough bed volume (BV₅₀, a proxy for apparent adsorption capacity) was essentially unchanged across EBCTs. This means longer EBCT altered the shape of breakthrough but did not increase the total volume of water treated per unit carbon before breakthrough.
- In full‑scale GAC adsorbers treating groundwater, no consistent differences in PFAS adsorption capacity were observed between EBCTs of 13 and 26 minutes. Again, doubling EBCT did not reliably improve bed volumes treated to a given breakthrough criterion.
- At a full‑scale plant, reducing flow (thus increasing EBCT) improved PFAS removal in an “older” GAC filter that was more diffusion‑limited, and was beneficial up to a point; however, further lowering flow (increasing EBCT beyond a threshold) did not increase PFAS removal in a “young” GAC filter, indicating that once kinetic limitations are overcome, performance becomes thermodynamically controlled and additional EBCT gives little or no gain.

Collectively, these findings support a nuanced interpretation:
- EBCT must be long enough to avoid kinetic limitations (especially in older, fouled beds) and to achieve target effluent concentrations at a given flow; in that regime, increasing EBCT can improve short‑term removal efficiency. 
- However, once intraparticle diffusion and film transfer are no longer rate‑limiting, increasing EBCT mainly changes how quickly breakthrough appears in *time* units, not whether or how many bed volumes can be treated before breakthrough; PFAS capacity and bed life are then governed more by carbon properties, PFAS chemistry, and background organics than by EBCT itself.

3. Uncertainty and limitations 
- Available data cover limited EBCT ranges (roughly 5–30 min) and specific waters (mainly groundwater, some full‑scale plants); extreme EBCTs or very different matrices could behave differently. 
- PFAS mixtures, concentrations, and NOM characteristics vary widely; some systems may be more or less diffusion‑limited than those studied, shifting the EBCT where “extra” contact time stops providing benefit.

4. Practical takeaway 
Longer EBCT can improve PFAS removal when kinetics are limiting, but beyond that threshold it does not necessarily increase PFAS bed life or adsorption capacity; EBCT should be optimized rather than maximized, and design should be based on pilot/RSSCT data that capture both kinetics and equilibrium for the specific water.

### Human label

- Adequate (`yes` / `no` / `uncertain`):
- Material scientific error (`yes` / `no` / `uncertain`):
- Confidence (`high` / `medium` / `low`):
- Notes:

---

## D13-A009

**Question ID:** `WF10_004a`

**Question:** How does PFAS chain length affect reported treatment performance or adsorption behavior?

**Must include:** Compare studies only on matched compounds, matrices, endpoints, and conditions; avoid ranking technologies when the evidence is not comparable.

**Must not claim:** Do not convert a condition-specific finding into a universal PFAS treatment claim.

### Reference evidence

**WF10_004a_MMG001**

> The removal efficiency of long- chain PFAS is higher than that of short-chain PFAS across all sorbents (Fig.

**WF10_004a_MMG002**

> The removal efficiency of PFOA (73% ± 24%) and PFOS (89% ± 35%) is higher than that of PFBA (30% ± 11%) and PFBS (55% ± 18%) in all three adsorbents (Figure 3a), as long-chain PFAS are more adsorbed on carbonaceous-based adsorbents than short-chain PFAS.

**WF10_004a_MMG003**

> Compared to the removal of long-chain PFAS, e.g., 98.8% for PFOS and 87.6% for PFOA, the overall removal efficiency of short-chain PFAS is much lower than that of long-chain PFAS, highlighting once again the challenges of the removal of these short-chain substances from aqueous solutions because of their low hydrophobicity.

**WF10_004a_MMG004**

> longer-chain PFAS are more hydrophobic and less water-soluble, leading to higher adsorption capacities onto adsorbents [ 67, 68, 82, 89, 90].

**WF10_004a_MMG005**

> Long-chain PFASs can interact via hydrophobic tails through hydrophobic interactions, and the chain length and orientation of PFAS molecules signif- icantly influence the adsorption process.

**WF10_004a_MMG006**

> length, carboxylic/sulfonic groups, branched/linear structure and adsorb- ents’ ages on PFAS removal, although there are some agreement to certain extent (e.g., removal efficiencies are often better for long-chained, carbox- ylic, and linear PFAS), many other factors that can influence the large-scale removal efficiencies remain largely unknown (e.g., effects of water/waste- water organic and inorganic content) and contradictory results are often reported for different water/wastewater, adsorbents, and experimental con- ditions, which warrants further investigation.

### Anonymous candidate answer

1. Answerability 
answerable – General, literature‑consistent trends relating PFAS chain length to treatment and adsorption behavior are well established, even though method‑ and matrix‑specific quantitative values cannot be provided.

---

2. Answer 

PFAS chain length strongly influences adsorption and many treatment outcomes, mainly through hydrophobicity, sorption affinity, and mobility. The main general trends are:

**A. Adsorption to solids (GAC, anion exchange resins, soils, sediments)** 

1. **Longer perfluoroalkyl chains adsorb more strongly.** 
 - As the number of CF₂ units increases, hydrophobicity and “fluorous” character increase. 
 - For both perfluorosulfonic acids (PFSAs) and perfluorocarboxylic acids (PFCAs), sorption affinity generally increases with chain length. 
 - Practical implication: 
 - Long‑chain PFAS (e.g., ≥C8 PFCAs, ≥C6 PFSAs) are typically well removed by granular activated carbon (GAC) and many ion‑exchange resins under typical drinking water conditions. 
 - Short‑chain PFAS (e.g., C4–C6 PFCAs, C3–C4 PFSAs) break through earlier and are more difficult to control by simple sorption.

2. **Order of sorption strength (within a headgroup series).** 
 - For a given functional group, sorption affinity typically increases with carbon number. 
 - In conceptual terms, for PFCAs: C4 < C5 < C6 < … < C10 (weak to strong sorption). 
 - The same monotonic trend usually applies for PFSAs across their chain lengths.

3. **Headgroup matters, but chain length trend still holds.** 
 - Sulfonates (PFSAs) of a given chain length usually adsorb more strongly than carboxylates (PFCAs) of the same perfluoroalkyl length, because PFSAs are more acidic and more strongly anionic at environmental pH, with different polarities and hydration. 
 - Within each headgroup family, chain length is a primary driver of differences in adsorption performance.

4. **Soils, sediments, and organic matter show similar trends.** 
 - Longer‑chain PFAS partition more strongly to organic carbon and mineral surfaces. 
 - Short‑chain PFAS remain more mobile and are more likely to stay dissolved, causing deeper groundwater penetration and wider plumes.

---

**B. Behavior in common engineered treatments**

1. **Granular Activated Carbon (GAC)** 
 - Long‑chain PFAS: 
 - High affinity; GAC breakthrough curves show later and steeper breakthrough. 
 - Bed life is often controlled by shorter‑chain PFAS, not by long‑chain species. 
 - Short‑chain PFAS: 
 - Lower affinity; early breakthrough and lower removal at the same empty bed contact time. 
 - As chain length increases, PFAS are more effectively captured and retained on GAC.

2. **Polymeric Anion Exchange (AIX) Resins** 
 - Removal is driven by both electrostatic attraction (anionic headgroup) and hydrophobic/fuorous interactions with the resin matrix. 
 - Longer‑chain PFAS: higher overall affinity, generally higher removal and slower breakthrough. 
 - Short‑chain PFAS: more weakly held; greater competition from inorganic anions (e.g., sulfate, nitrate, bicarbonate), so they often show earlier breakthrough. 
 - Hydrophobic resins (e.g., styrenic) tend to exaggerate the chain‑length effect more than very hydrophilic resins.

3. **Membrane processes (NF/RO/UF)** 
 - Nanofiltration (NF) and reverse osmosis (RO): 
 - Rejection is high for most PFAS, but chain length still matters. 
 - Longer‑chain PFAS (and sulfonates) typically have higher rejection; short‑chain PFCAs and zwitterionic/neutral precursors are more likely to have slightly reduced rejection. 
 - Ultrafiltration (UF): 
 - UF membranes do not effectively reject dissolved PFAS by size alone, regardless of chain length; PFAS are much smaller than the pore sizes. 
 - UF can indirectly remove PFAS if they are associated with colloids or organic matter; again, long‑chain PFAS are more likely to be particle‑associated.

4. **Foam fractionation / air stripping / surfactant behavior** 
 - Surface activity increases with chain length (up to a point). 
 - Longer‑chain PFAS concentrate more strongly at air–water interfaces and in foam. 
 - Foam fractionation and related air‑contact processes therefore preferentially remove long‑chain, strongly surface‑active PFAS. 
 - Short‑chain PFAS tend to remain in the bulk aqueous phase and are removed less efficiently in foam‑based systems.

---

**C. Influence on transformation and destructive treatments**

Here the chain‑length trend is more nuanced and more method‑dependent than for adsorption:

1. **Advanced oxidation processes (AOPs) in water** 
 - Many conventional AOPs (e.g., UV/H₂O₂, ozone, hydroxyl radical–dominated processes) do not significantly degrade most perfluoroalkyl acids, regardless of chain length. 
 - When partial degradation occurs (for precursors or side chains), shorter‑chain perfluoroalkyl acids are often end‑products and are more persistent; chain length mainly affects what accumulates, not destruction efficiency of the acids themselves.

2. **Reductive / electrochemical / high‑energy processes** 
 - For methods that can cleave C–F bonds (e.g., high‑voltage electrochemical oxidation, some reductive systems, plasma, high‑temperature incineration or supercritical treatments), chain length can influence reaction rates and pathways, but the trends are not as simple as “longer is easier/harder.” 
 - Long chains may initially attack at the headgroup or terminal CF₂ units, forming shorter‑chain PFAS as intermediates; short‑chain PFAS formed are often more persistent residuals. 
 - In practice: many destructive technologies reduce long‑chain PFAS concentrations faster than short‑chain residues, so residual PFAS after treatment skew toward shorter chain lengths.

3. **Biological treatment** 
 - Perfluoroalkyl acids are generally recalcitrant to biodegradation, regardless of chain length. 
 - Biodegradation primarily affects precursors (e.g., fluorotelomers, sulfonamides), often yielding perfluoroalkyl acids. 
 - For precursors, chain length can affect bioaccumulation and biotransformation rates, but robust general rules are weaker than for sorption.

---

**D. Mobility, bioaccumulation, and implications for treatment**

1. **Mobility in water systems** 
 - Short‑chain PFAS: more mobile, less sorbed; plumes extend farther; more difficult to capture with standard sorbents. 
 - Long‑chain PFAS: more strongly retained in soils and on treatment media, leading to localized accumulation and longer filter lifetimes determined by short‑chain species.

2. **Bioaccumulation and partitioning** 
 - Long‑chain PFAS tend to bioaccumulate more in aquatic and terrestrial organisms than short‑chain analogs. 
 - This affects: 
 - Partitioning between water and biota/sludge. 
 - Where removal happens (e.g., in biosolids vs. effluent) and what remains in the treated water (often shorter chain PFAS).

3. **Treatment design consequences** 
 - Systems sized and optimized for legacy long‑chain PFAS can underperform when influent is dominated by short‑chain replacements. 
 - Designers increasingly must assume that: 
 - Short‑chain PFAS will limit GAC and AIX performance lifetimes. 
 - Tighter membranes (RO) or combined treatment trains may be required to control both long‑ and short‑chain PFAS. 

---

3. Uncertainty and limitations 

- Quantitative relationships (e.g., exact distribution coefficients, breakthrough times, or rejection percentages vs. chain length) depend strongly on pH, ionic strength, co‑solutes, media type, and operating conditions and cannot be generalized without data. 
- Different PFAS subclasses (PFCAs vs. PFSAs vs. fluorotelomers vs. ether PFAS) can deviate from simple “longer is stronger” trends, particularly where steric effects, branching, and ether oxygens alter polarity and conformation. 
- For destructive technologies, chain length effects are highly technology‑specific; without method‑specific experimental data, only qualitative patterns about intermediate formation and persistence can be offered. 
- Emerging PFAS chemistries (e.g., short‑chain ether acids) may not follow all the trends observed for classical straight‑chain PFCAs and PFSAs.

---

4. Practical takeaway 

For most conventional separation‑based PFAS treatments (GAC, ion exchange, sorption to soils/sediments, foam fractionation, and to a lesser extent membranes), increasing PFAS chain length generally increases adsorption affinity, decreases mobility, and improves apparent removal, whereas short‑chain PFAS remain more mobile, less adsorptive, and more challenging to capture—so any treatment design should explicitly evaluate performance separately for short‑ and long‑chain PFAS rather than assuming uniform behavior.

### Human label

- Adequate (`yes` / `no` / `uncertain`):
- Material scientific error (`yes` / `no` / `uncertain`):
- Confidence (`high` / `medium` / `low`):
- Notes:

---

## D13-A010

**Question ID:** `WF10_021`

**Question:** When screening activated-carbon or biochar PFAS adsorption studies, what matrix and regeneration gaps should be checked?

**Must include:** Use limitation, uncertainty, caveat, and negative evidence to avoid overclaiming beyond the reported study scope.

**Must not claim:** Do not convert a condition-specific finding into a universal PFAS treatment claim.

### Reference evidence

**WF10_021_MMG001**

> How - ever, the extent of this impact varies depending on the type and concentration of OM, with some studies indicating min- imal interference at environmentally relevant OM concen - trations, while others report substantial reductions in PFAS sorption, highlighting the need for further research on opti - mizing biochar performance under diverse water matrices.

**WF10_021_MMG002**

> However, biochar regeneration faces sig- nificant challenges as this simply has not been attempted frequently enough in the past to draw definitive conclusions on efficacy.

**WF10_021_MMG003**

> Sustainable regeneration and reusability of biochar Bio- char regeneration is crucial for reducing costs, but each regeneration cycle alters its characteristics, such as surface morphology, functionalities, and porosity, necessitating thorough investigation.

### Anonymous candidate answer

1. Answerability 
answerable – The question asks for conceptual screening criteria, which can be supported by the supplied evidence and general PFAS adsorption knowledge.

---

2. Answer 

When you triage activated-carbon or biochar PFAS adsorption papers, you can quickly flag important *matrix* and *regeneration* gaps with a focused checklist.

### A. Matrix-related gaps to check

1. **Matrix type and realism**
 - Uses only ultrapure/DI water or very simple electrolyte solutions, with no tests in real waters (groundwater, wastewater, reclaimed water, landfill leachate, surface water). 
 - Many recent studies emphasize the need for real‑world condition testing and site‑scale evaluation for biochar PFAS removal, which is still uncommon. 
 - More robust studies explicitly test in realistic matrices such as groundwater, wastewater, or reclaimed water to evaluate upscaling potential.

2. **Natural organic matter (NOM) / effluent organic matter**
 - Little or no characterization of DOC/NOM or effluent organic matter (EOM), and no experiments with and without NOM.
 - Competitive adsorption by organic matter can strongly suppress PFAS uptake (e.g., large PFOS removal drop when synthetic effluent organic matter was added). 
 - For screening: downgrade studies that:
 - Report high removal only in NOM‑free DI water.
 - Do not test at any realistic DOC level for the intended application.

3. **Ionic strength and co‑ions**
 - No data on background ions (e.g., Ca²⁺, Mg²⁺, Na⁺, Cl⁻, SO₄²⁻) or ionic strength, even though matrix ion content is known to affect PFAS sorption to biochar.
 - For screening: note if the study
 - Omits ionic strength variations.
 - Doesn’t report actual ion composition for real matrices.

4. **pH and temperature range**
 - Only a single pH, often near neutral, with no exploration of pH dependence even though both PFAS speciation and surface charge matter.
 - Temperature often fixed and not justified, although temperature can influence PFAS aggregation and diffusion and thus adsorption. 
 - For screening: flag studies that:
 - Do not report pH, or
 - Do not test the plausible pH band for the target application (e.g., 5–9 for most waters).

5. **PFAS species coverage**
 - Focus only on legacy long‑chain PFOS/PFOA; no short‑chain PFAS or replacement chemistries (e.g., GenX, F‑53B), despite explicit recognition that data on newer substitutes are limited.
 - For screening: mark as incomplete if:
 - Target application includes short‑chain or substitutes but the study tests only PFOS/PFOA.
 - No explanation is given for PFAS selection.

6. **Co‑contaminants / mixed systems**
 - No tests with relevant co‑contaminants (e.g., metals like Cd, other organics, surfactants), even though co‑contaminant interactions can change sorption behavior.
 - For screening: note as a gap when application waters are known to contain significant metals/organics but are not represented.

7. **Concentration levels and contact conditions**
 - PFAS concentrations far above environmental levels (e.g., mg/L) with no tests in the ng–µg/L range relevant to drinking water or many wastewaters.
 - Batch tests only, no column or flow‑through data when the claimed use is continuous treatment.
 - For screening: flag when
 - High-concentration results are extrapolated to trace‑level treatment without supporting data.
 - Contact times are unrealistically long for full‑scale operation.

### B. Regeneration-related gaps to check

1. **Absence of any regeneration or reusability data**
 - Many biochar PFAS studies do not attempt regeneration at all, and reviews highlight that regeneration has “not been attempted frequently enough… to draw definitive conclusions on efficacy.” 
 - For screening: classify such work as “single‑use only” unless the authors explicitly address end‑of‑life management.

2. **Regeneration method description and realism**
 - Method not specified beyond a vague label (“thermal regeneration”, “chemical regeneration”) with no conditions (temperature, atmosphere, chemical concentration).
 - Review work identifies five main regeneration categories—thermal, solvent-based, chemical, hybrid, and emerging methods—with thermal regeneration most established for carbonaceous adsorbents. 
 - For screening: consider as a gap when:
 - Regeneration conditions are poorly specified.
 - Conditions are clearly unrealistic for the intended scale (e.g., extreme temperatures or solvents not feasible for utility‑scale operation) with no discussion of practicality.

3. **Number of regeneration cycles and capacity retention**
 - Only one regeneration cycle tested, or sorption isotherms reported only for the fresh material.
 - Little to no tracking of capacity loss (e.g., % of initial capacity retained after each cycle).
 - For screening: down‑weight studies that:
 - Don’t go beyond 1 cycle.
 - Fail to quantify performance decline over cycles.

4. **PFAS mass balance and fate during regeneration**
 - No accounting of where PFAS go during regeneration (e.g., desorbed into regenerant, volatilized, decomposed).
 - Thermal regeneration of carbonaceous adsorbents can produce volatile organic fluorine and shorter-chain products, yet many studies do not measure off‑gas or transformation products.
 - For screening: flag as a major gap when:
 - PFAS are “removed from adsorbent” without measuring or at least qualitatively tracking them in off‑gas, regenerant, or residual solids.

5. **Secondary waste and environmental risk**
 - Regeneration produces concentrated PFAS brines or off‑gases, but there is no discussion of how these will be managed or treated, despite known concerns with incineration and landfilling of spent carbon.
 - For screening: note absence of:
 - Any proposed management for the regenerant stream.
 - Any consideration of by‑product toxicity or fluorinated emissions.

6. **Biochar vs. activated carbon–specific issues**
 - Reviews emphasize that biochar regeneration is less studied and more problematic than activated carbon, with significant uncertainty on long‑term efficacy.
 - For screening: differentiate:
 - GAC studies that build on an established regeneration practice (even if still imperfect) from
 - Biochar studies where regeneration strategy, structural stability, and potential ash or surface oxidation effects are largely untested.

7. **Energy, cost, and scalability signals**
 - Thermal regeneration typically occurs at 400–900 °C for carbonaceous materials, restoring most of the initial capacity, but energy and cost are rarely quantified.
 - For screening: at minimum, note whether the paper:
 - Discusses energy demand or cost implications of its regeneration scheme.
 - Mentions pilot‑scale or life‑cycle assessment needs.

---

3. Uncertainty and limitations 

- The evidence base on PFAS regeneration, especially for biochar, is explicitly incomplete; recommended screening checks identify likely gaps rather than strict requirements. 
- Different application contexts (e.g., drinking water vs. agricultural reuse vs. industrial wastewater) demand different matrix realism; the checklist should be adapted accordingly. 
- Many studies are lab‑scale; absence of certain details (e.g., mass balance, energy analysis) may partly reflect space limits, not necessarily poor practice, so these are flags, not absolute exclusion criteria.

---

4. Practical takeaway 

When screening AC/biochar PFAS adsorption papers, downgrade or flag studies that (i) only show high removal in simple, NOM‑free DI water with no realistic matrix, ion, or pH coverage and limited PFAS species, and (ii) lack explicit, multi‑cycle regeneration testing with quantified capacity retention, PFAS mass balance, and at least qualitative consideration of secondary wastes and scalability.

### Human label

- Adequate (`yes` / `no` / `uncertain`):
- Material scientific error (`yes` / `no` / `uncertain`):
- Confidence (`high` / `medium` / `low`):
- Notes:

---

## D13-A011

**Question ID:** `NQ24`

**Question:** How do reported activated-carbon PFAS adsorption capacities differ between batch and column studies?

**Must include:** Must distinguish carbon type, PFAS chain length or compound, test conditions, endpoint, capacity units, and capacity values when values are presented.

**Must not claim:** Must not claim activated carbon has one fixed PFAS adsorption capacity across compounds and matrices.

### Reference evidence

**NQ24_L3CTX001**

> Journal of Water Process Engineering 54 (2023) 103965 Available online 29 June 2023 2214-7144/© 2023 Elsevier Ltd. All rights reserved. PFOA remediation from aqueous media using CTAB impregnated activated carbon: A closed-loop sustainable study with comprehensive selectivity analysis Mohd Ahmed Naim Shaikh, Paulami Sarkar, Tabish Nawaz * Environmental Science and Engineering Department (ESED), IIT Bombay, Powai, Mumbai 400 076, India ARTICLE INFO Keywords: Biochar PFAS Emerging contaminants Adsorbent synthesis ABSTRACT PFASs have been attracting worldwide attention in recent years. In this study, a novel surface-impregnated activated carbon (AC) has been optimally synthesized utilizing waste Karanja shells. Surface functional group modification has been performed using Cetyltrimethylammonium bromide (CTAB). PFOA-selectivity analysis of the adsorbent against different background species present at typical river water concentration was performed. To make the process sustainable, the development of regenerant specifications as well as recovery of the regenerant and PFOA from the spent regenerant solution were investigated. A biomass/acid ratio of 1:2.5, temperature 450 ◦ C, and 1 % CTAB solution was found to be optimum synthesis parameters for the CTAB- modified AC (CTAB_K-AC) for PFOA removal. By CTAB-impregnation, the PFOA uptake capacity of the adsor - bent increased up to threefold.

**NQ24_MMG001**

> max ob - tained through the Thomas model was 5.71 mg/g, which was marginally lower as compared to the Q e obtained through Langmuir isotherm model (6.85 mg/g) mainly due to two reasons (a) the presence of the back - ground water matrix during the column run and (b) the size of the adsorbent was bigger (125 – 500 μ m) than used in the batch equilibrium and kinetic study (125 – 250 μ m).

### Anonymous candidate answer

1. Answerability 
partially_answerable – The evidence gives qualitative relationships and metrics used in batch vs column PFAS adsorption on activated carbon, but does not provide systematic, numeric side‑by‑side capacity comparisons.

2. Answer 
Reported activated‑carbon PFAS “capacities” differ between batch and column studies in three main ways: how they are defined, the concentration ranges and conditions used, and the magnitudes inferred under those conditions.

**a. Different capacity metrics and units**

- Batch tests usually report: 
 • Equilibrium solid‑phase loading (qₑ, e.g., μg PFAS/g AC) and isotherm parameters (e.g., Freundlich K_F, 1/n). Batch isotherms for PFAS on GAC are commonly fit with Freundlich or Langmuir models based on equilibrium sorption data across a wide concentration range. 
- Column tests generally report “apparent” dynamic capacities, such as: 
 • Bed volumes treated at a given breakthrough (e.g., BV₁₀, BV₅₀); BV₅₀ is used explicitly as an indicator of apparent adsorption capacity for PFAS. 
 • Apparent capacity terms like K* (or log K*), calculated from BV₅₀, bed volume, and GAC mass, and interpreted as a partition‑like measure of affinity. 

Because qₑ/K_F and BV₅₀/K* are not directly interchangeable, reported “capacities” from batch and column studies are rarely numerically comparable even for the same PFAS–carbon pair.

**b. Concentration ranges and operating conditions**

- Batch PFAS isotherms and kinetic tests often use much higher PFAS concentrations and long contact times to reach equilibrium, minimizing transport limitations and emphasizing intrinsic sorption affinity. For ion‑exchange resins, batch studies commonly span 1–1000 mg/L PFAS, whereas continuous‑flow tests use 10–10 000 ng/L; this mismatch in concentration range is highlighted as a core reason that batch and column capacities are not directly comparable. The same pattern (high mg/L in batch, low ng/L–μg/L in columns) also exists in many PFAS–AC studies. 
- Column studies operate under finite empty bed contact times (EBCTs) and realistic influent concentrations. Apparent PFAS capacities (BV₅₀, K*) reflect not just equilibrium affinity, but also film/intraparticle mass transfer and competitive adsorption from natural organic matter and co‑contaminants. Hydrophobicity, AC surface charge, and microporosity control these apparent capacities in columns. 

**c. Relative magnitude and consistency of trends**

- In general, batch equilibrium capacities (e.g., K_F, qₑ at a given Cₑ) tend to be larger than the *effective* capacities inferred from column breakthrough, because columns are limited by kinetics, concentration fronts, and competitive displacement; a portion of the theoretical equilibrium capacity is not utilized before the effluent reaches the breakthrough criterion. 
- However, qualitative *trends* with PFAS and carbon properties are often consistent between batch and column tests: 
 • The same study that measured both batch isotherms and rapid small‑scale column tests (RSSCTs) for eight PFAS on four GACs found that AC surface charge and pore structure controlled capacities in both modes, and that the relative performance ranking of carbons (e.g., positively charged vs neutral, microporous vs mesoporous) was similar. 
 • That study also showed that UV₂₅₄–PFAS removal correlations derived from batch could reasonably predict PFAS removal in GAC columns, implying that batch‑derived relationships capture key sorption behavior even though dynamic capacities differ. 
 • Column apparent capacities (BV₅₀, K*) increase with PFAS hydrophobicity (longer chain length, higher log D_ow) and with favorable AC properties (positive surface charge, higher micropore area) in groundwater and drinking water columns, which mirrors hydrophobicity and charge effects observed in batch isotherms. 

**d. What can be said about “differences” in reported capacities**

On the basis of the available evidence and broader practice:

- Batch studies usually report higher apparent maximum loadings per gram (and higher K_F at the same equilibrium concentration range) than would be *effectively realized* in columns at drinking‑water‑level influent concentrations, because: 
 • batch tests operate at high C₀ and long contact times (closer to full equilibrium), 
 • columns run at low C₀, finite EBCT, and are affected more strongly by mass‑transfer limitations and competitive sorption, 
 • and breakthrough based design criteria (e.g., 5–10% of influent) purposely utilize only the front portion of the isotherm. 
- Continuous‑flow PFAS studies on ion‑exchange resins explicitly note that it is unclear how kinetic constants and adsorption capacity terms from batch relate quantitatively to those from column models, despite using similar isotherm types; the same conceptual limitation applies to AC: numeric batch capacities cannot be simply substituted into column design without accounting for kinetics and competition. 
- Therefore, reported batch and column capacities for PFAS on AC are better treated as complementary: 
 • Batch: intrinsic, equilibrium affinity and capacity; useful for screening carbons and parameterizing isotherms. 
 • Columns (including RSSCTs): *usable* dynamic capacity and bed life under realistic loadings and competition (BV₅₀, K*, breakthrough curves). 

3. Uncertainty and limitations 

- The retrieved AC studies do not provide systematic side‑by‑side numeric comparisons (e.g., “batch K_F = X; column K* = Y for the same system”), so only qualitative differences and general expectations can be described. 
- Most explicit evidence on the disconnect between batch and continuous capacities comes from ion‑exchange PFAS studies, though the same physical reasons (concentration dependence, nonlinearity, kinetics, competition) apply to AC; extrapolation of magnitude differences remains uncertain. 
- Reported capacities are highly sensitive to water matrix (DOC, competing solutes), PFAS mixture, carbon type, and study design; no single “factor difference” between batch and column can be generalized.

4. Practical takeaway 

Batch AC studies typically report higher equilibrium PFAS capacities and use them to characterize intrinsic affinity, while column/RSSCT studies report lower, dynamic “apparent capacities” (BV₅₀, K*) that incorporate mass‑transfer and competition; trends vs PFAS hydrophobicity and AC properties are broadly consistent between the two, but the numeric capacities are not directly comparable and must be linked through kinetic modeling or matched‑condition experiments.

### Human label

- Adequate (`yes` / `no` / `uncertain`):
- Material scientific error (`yes` / `no` / `uncertain`):
- Confidence (`high` / `medium` / `low`):
- Notes:

---

## D13-A012

**Question ID:** `NQ23`

**Question:** What energy-consumption or energy-efficiency evidence is available for PFAS degradation methods, and can values be compared across studies?

**Must include:** Must identify the energy metric used, such as EEO, EEM, kWh/m3, kWh/g, electrical input, or energy per mass removed; must explain comparability limits.

**Must not claim:** Must not claim one universal energy-consumption number fairly represents all PFAS degradation methods.

### Reference evidence

**NQ23_MMG001**

> The comparison between the NTP technologies and the other AOPs from the viewpoint of energy consumption (evaluated in term of elec - trical energy per order values - E EO ), classifies the NTP processes in a central zone with median energy consumptions in the 1 – 100 kWh/m 3 range, at the same level of photo-Fenton and pure electrolytic AOPs.

**NQ23_MMG002**

> where E (kWh) is the energy consumed by the high-voltage power supplies, gas and liquid pumps, and rotating spark gap, V (L) is the treatment volume for each experimental condition, and C i and Cf are the initial and ﬁnal concentrations (below the USEPA HAL), respectively, of PFOA and PFOS (ng/L).

**NQ23_MMG003**

> The energy consumption of EO can be calculated as described previously 15 and as presented in eq S18.

**NQ23_MMG004**

> A. Kumar et al. Chemical Engineering Journal Advances 25 (2026) 101046 11 results, enabling a more robust fluoride mass balance and interpretation of degradation pathways. In contrast, results obtained at lower initial concentrations were subject to greater uncertainty, likely influenced by sorption losses and interfacial effects, which complicate quantitative interpretation. The findings demonstrate the capability of the orifice- based HC system to induce PFOS degradation and defluorination, with the higher-concentration experiments offering stronger evidence for effective destruction rather than incomplete transformation. The EEO ranged from 7 to 598 kWh/m³/order, while the energy yield varied between 17 and 286 mg/kWh. The overall energy input for PFOS degradation ranged from 1 to 75 kWh/m³, depending on the initial PFOS concentration and the extent of degradation.. These results indicate that HC enables effective PFOS degradation with lower energy requirements compared to most reported studies and conventional treatment methods. The extreme physicochemical conditions generated during bubble implosion indicate that PFOS reaching the cavitation bubble undergoes near-complete mineralization, with subsequent decomposi - tion of intermediates into fluoride ions. Overall, this study demonstrates that HC is a promising, non- thermal, energy-efficient, and scalable technology for PFAS degrada - tion. It presents a viable alternative to conventional treatment methods and lays the groundwork for sustainable, large-scale PFAS remediation

**NQ23_MMG005**

> However, the primary challenge with N 2 plasma is its low PFAS degradation efficiency (45 % for PFOA and 60 % for PFDA) combined with high energy consumption (EEO values of 370 kWh/m 3 for PFOA and 260 kWh/m 3 for PFDA).

**NQ23_MMG006**

> It can be observed that the reported ranges show a high variability, reflecting the uncertainty and nonuniformity of experimental conditions in the respective studies (Table 1).

**NQ23_MMG007**

> Application potential A consolidated comparison of reported EE/O values, together with key experimental parameters such as water type, initial PFAS concen - tration, reactor scale, reaction time, and removal/defluorination effi - ciency, is provided in Table S1 to support a transparent and context- aware evaluation across technologies.

### Anonymous candidate answer

1. Answerability 
answerable – Multiple studies report quantitative energy-use metrics for PFAS destruction and comment on comparability, but cross‑study comparisons are only partially valid because metrics and conditions differ.

2. Answer 

**a. What energy-consumption / energy-efficiency evidence is available?**

Studies use several energy metrics for PFAS destruction, most commonly:

- **EE/O (electrical energy per order)**, typically in kWh·m⁻³·order⁻¹ (sometimes shortened to kWh/m³ or kWh/m³/order in the text) 
- **Specific energy per volume treated**, kWh/m³ 
- **Specific energy per mass degraded**, kWh/kg degraded (or kWh/g) 
- **Energy yield**, mg removed per kWh 
- **Input power density**, W/L

Examples across technologies:

**Nonthermal plasma and other AOPs**

- Water-film / mesoporous / reverse‑vortex / plasma–ozonation systems for PFAS show EE/O ranges of: 
 - Mesoporous plasma: 188–205 kWh/m³ (per order) 
 - Reverse vortex flow gliding arc plasma: 23.2–213.4 kWh/m³ 
 - Nonthermal plasma–ozonation cascade: 90–180 kWh/m³ 
 - Overall plasma treatment of PFAS reported over 1.7–830 kWh/m³, comparable to electrochemical (205–343 kWh/m³) and photoreductive processes (102.1–539.8 kWh/m³), but much lower than microwave (7319.3 kWh/m³), ultrasonic (502–1644 kWh/m³), and photocatalytic (13 074.8 kWh/m³) PFAS degradation in the same compilation.

**Hydrodynamic cavitation (HC)**

- For PFOS in an orifice‑based hydrodynamic cavitation reactor, authors report: 
 - EE/O: 7–598 kWh/m³/order depending on concentration and extent of degradation. 
 - Energy yield: 17–286 mg PFOS removed per kWh. 
 - Overall specific energy input: 1–75 kWh/m³ for PFOS degradation. 
 - They interpret HC as having lower energy requirements than most reported PFAS destruction methods and conventional treatments.

**UV–sulfite advanced reduction (pilot scale)**

- In a pilot NF + UV–sulfite train: recalculated EE/O for the UV reactor alone would be about 64.4 kWh/m³ for PFOA and 71.2 kWh/m³ for PFOS (based on UV‑reactor volume). 
- Authors explicitly note that PFAS destruction is “highly energy intensive” relative to seawater RO (2.5–4 kWh/m³).

**Electrochemical oxidation (EO), including pilot scale and Fenton‑assisted**

- Pilot EO treatment of PFAS-contaminated water and foam: 
 - Total energy consumption after 9 h was ~270 kWh/m³ for 50 L runs and 93 kWh/m³ for 150 L runs. 
 - Normalized energy consumption per log removal of PFOA averaged 240 and 160 kWh/m³, respectively.

- Fenton‑assisted EO of 29 PFAS: 
 - For Ti/BDD at 5 mA/cm² and 120 min, average PFAS removal ~96.6 % with overall energy consumption 9.0 kWh/m³. 
 - Normalized per log removal, energy ranged from 4.43 to 39.43 kWh/m³ across individual PFAS.

- Magnéli‑phase EO vs EO + electro‑Fenton: 
 - At 2 mg/L: PFOA by EO alone: 14.91 kWh/m³; adding electro‑Fenton reduced energy to 3.95 kWh/m³ (3.7× lower). 
 - PFOS by EO alone: 5.14 kWh/m³ (≈3× lower than PFOA under same conditions); energy also reduced when coupled with electro‑Fenton. 
 - Authors explicitly state that it is difficult to compare their energy consumption values with literature because of many differing parameters.

**Electro-oxidation vs UV/KI–sulfite (bench-scale comparison)**

- In a side‑by‑side comparison for PFOA: 
 - Flow‑through EO system: input power density ≈4.2 W/L, EE/O ≈5.2 kWh/m³ for PFOA (pump energy neglected). 
 - UV/KI–SO₃²⁻ process: input power density 60 W/L, EE/O 48.5 kWh/m³ for PFOA. 
 - Thus, UV/KI–sulfite was faster kinetically but roughly an order of magnitude less energy‑efficient.

**Sonolysis (ultrasound)**

- For PFAS mixtures and single compounds, the study calculates both EE/O and mass‑normalized energy (E_EM): 
 - For 23 mg/L HFPO‑DA: mineralization consumed 203 kWh/g (E_EM) or 4.8 MWh·m⁻³·order⁻¹ (EE/O). 
 - For 873 µg/L HFPO‑DA: degradation required ~1.3 MWh·m⁻³·order⁻¹ (EE/O). 
 - For investigation‑derived waste (IDW): 3–76 kWh/g (E_EM) vs 14–8 MWh·m⁻³·order⁻¹ using EE/O based only on identified PFAS. 
 - Authors conclude that E_EM (kWh per mass degraded) better reflects energy consumption for complex, high‑concentration mixtures than EE/O.

**Cross-technology review data**

- A review compiles “specific energy use” across PFAS destruction technologies and notes very high variability and nonuniformity of experimental conditions. Example entries: 
 - Electrochemical oxidation of PFHxA at 870,000 µg/L (1 L reactor, 1.5 h, 90 % destruction): 19 kWh/kg degraded. 
 - For mixed PFAS at 450–4650 µg/L: 1.6–3.3 × 10⁵ kWh/kg degraded for 76.5–99.7 % destruction. 
 - For PFOS (4400–15 200 µg/L): 0.78–2.2 × 10⁷ kWh/kg degraded for 87.8–97.6 % destruction. 
- The review explicitly notes the broad ranges and the resulting uncertainty in comparing energy efficiency across studies.

**b. Can values be compared across studies? Under what conditions?**

Evidence and authors’ own comments indicate **limited and conditional comparability**:

- **Different metrics and normalizations**
 - Studies use EE/O (kWh·m⁻³·order⁻¹), kWh/m³, kWh/kg (or kWh/g), mg/kWh, and W/L, often within the same paper. 
 - EE/O normalizes to log removal of a *specific solute concentration* and assumes pseudo‑first‑order kinetics; energy per m³ reflects overall treatment energy regardless of removal extent; kWh/kg depends strongly on initial concentration and mass degraded. 
 - A sonolysis study explicitly shows that EE/O and kWh/g can differ by orders of magnitude for the same system, and concludes that choice of metric affects how “efficient” a process appears, especially for complex mixtures.

- **Different PFAS targets and mixtures**
 - Energy requirements differ between compounds even under the same conditions (e.g., PFOS requiring less energy and degrading faster than PFOA in EO systems). 
 - Some studies target single PFAS (e.g., PFOS, PFOA, HFPO‑DA), others complex AFFF or waste mixtures, altering both kinetics and “mass degraded” baselines.

- **Different water matrices and scales**
 - Experiments vary from bench‑scale in DI water to pilot‑scale groundwater, foam fractions, and industrial wastewaters, with very different background organic load, scavengers, and conductivity. 
 - Pilot UV–sulfite data are sensitive to whether energy is normalized to the *total* flow through the train or just the UV concentrate stream, giving a 10× difference in EE/O for the same reactor. 
 - EO pilot work notes energy per m³ is largely driven by treated volume at a given power, not just PFAS removal, complicating comparison to lab studies.

- **Different endpoints: removal vs mineralization vs defluorination**
 - Some metrics are based on parent PFAS concentration decrease (often ≤1–2 orders of magnitude), others on mineralization or fluoride release. 
 - A sonolysis study reports energy for complete mineralization of HFPO‑DA vs partial degradation at lower concentration, with large differences in EE/O and kWh/g. 
 - Plasma and EO studies sometimes compare energy at “high degradation efficiencies” but do not consistently distinguish between parent removal and full defluorination.

- **Different operating conditions and reactor designs**
 - Power density, residence time, electrode material, current density, and reactor geometry differ substantially, even within the same technology class. 
 - One EO–electro‑Fenton paper states explicitly that it is difficult to compare their energy consumption to literature because “the number of different parameters” affecting energy is high. 
 - A review similarly highlights the “high variability” of reported specific energy use and attributes it to non‑uniform experimental conditions, warning against overinterpreting cross‑study differences.

**So, when can you compare values?**

- **More defensible comparisons** are those that:
 - Use the **same metric and normalization** (e.g., EE/O in kWh·m⁻³·order⁻¹, or kWh/m³ at a stated % removal). 
 - Target the **same PFAS (or similar homologs)** in **similar matrices** (e.g., groundwater vs AFFF vs industrial waste). 
 - Report **similar removal / mineralization endpoints** (e.g., 90–99 % parent removal vs near‑complete mineralization). 
 - Use **clearly stated power input and scale** so system‑level vs solute‑level efficiencies can be distinguished.

Under those constraints, qualitative ranking is possible—for example, in one side‑by‑side study, EO for PFOA (EE/O ~5.2 kWh/m³) was an order of magnitude more energy‑efficient than a UV/KI–sulfite system (48.5 kWh/m³) under the same solution chemistry and concentration. Similarly, the hydrodynamic cavitation study situates its 1–75 kWh/m³ and 7–598 kWh/m³/order in the lower end of the wide range reported for PFAS AOPs, suggesting comparatively favorable energy use under its specific conditions.

However, broad cross‑technology ranges such as “plasma 1.7–830 kWh/m³ vs electrochemical 205–343 kWh/m³ vs photoreductive 102–540 kWh/m³ vs ultrasonic 502–1644 kWh/m³” or “electrochemical PFOS destruction 0.78–2.2 × 10⁷ kWh/kg degraded” should be interpreted as **indicative of order‑of‑magnitude differences and variability**, not as precise rankings.

3. Uncertainty and limitations 

- Reported values span several orders of magnitude, and many are sensitive to experimental choices (initial concentration, endpoint definition, normalization volume, and whether ancillary energy uses—pumps, pH adjustment—are included). 
- Metrics are not standardized; EE/O is sometimes reported simply as kWh/m³ without explicitly indicating “per order,” and mass‑based metrics depend heavily on concentration and mixture composition. 
- Comparisons across technologies, compounds, and matrices are largely qualitative unless designed as controlled side‑by‑side tests. 
- Many values come from bench‑scale systems; scale‑up may shift energy performance due to improved hydraulics but also added balance‑of‑plant loads.

4. Practical takeaway 

There is substantial quantitative evidence on energy use for PFAS destruction (plasma, cavitation, EO, Fenton‑assisted EO, UV–sulfite, sonolysis, and others), but values are only meaningfully comparable when the same metric, PFAS, matrix, and removal endpoint are used; for cross‑literature assessments, treat reported energy figures as order‑of‑magnitude indicators rather than directly comparable performance benchmarks and, where possible, recalculate them to a common metric (e.g., EE/O or kWh/kg degraded) for a specific PFAS in a defined matrix.

### Human label

- Adequate (`yes` / `no` / `uncertain`):
- Material scientific error (`yes` / `no` / `uncertain`):
- Confidence (`high` / `medium` / `low`):
- Notes:

---

## D13-A013

**Question ID:** `NQ15`

**Question:** How do electrolyte composition and pH-control choices affect interpretation of PFAS removal or degradation experiments?

**Must include:** Must treat buffer choice as a balance between pH control and interference risk; must connect to system or mechanism dependence.

**Must not claim:** Must not claim one exact buffer is universally correct for all PFAS removal experiments.

### Reference evidence

**NQ15_MMG001**

> If only relying on the initial pH for its effects on the degradation of PFAS, it is likely to lead to a false interpretation.

**NQ15_MMG002**

> There is no reported consensus on the effects of pH to date.

**NQ15_MMG003**

> ting  the  degradation  performance  of  PFAS  (Radjenovic et al., 2020). In  addition,  increased  electrolyte  viscosity and surface tension may decrease the electrode wettability and  thus  also  may  inhibit  the  electro-oxidative degradation of PFAS (Wu et al., 2004). Zhuo et al. (2014) compared  the  effects  of  three  electrolytes  on  the degradation of 6:2 fluorotelomer sulfonic acid (20 mg/L) on  a  Ti/SnO2-Sb2O5-Bi2O3  anode. They  found  that  its degradation  declined  along  with  the  trend  of  the electrolytes  NaClO4  >  NaCl  >  Na2SO4. Barisci et al. (2021) also showed a higher removal of PFOA and PFOS (100  μg/L)  in  NaCl  than  in  a  Na2SO4  electrolyte. Linear sweep  voltammetry  curves  showed  that  the  oxygen overpotential  on  the  Ti/RuO2  anode  was  higher  in  the NaCl electrolyte, suggesting its higher oxidation potential resulted in the increased degradation efficiency, although the  presence  of  halide  ions  may  lead  to  the  formation  of toxic byproducts (e.g., Cl2, HClO, and ClOx–) during the electrochemical  oxidation  (Azizi et al., 2011; Yang et al., 2019). This  risk  needs  to  be  mitigated,  especially  when high  electrolyte  concentration  and  high  potential  are employed  in  the  electro-oxidation  systems. Due  to  the

**NQ15_MMG004**

> Electrochemical decontamination of perfluorinated compounds 11 4.2.3    Electrolyte type The chemical components in an electrolyte can also affect the  removal  of  PFAS  through  different  influencing mechanisms in an electro-coagulation process. Yang et al. (2016)  investigated  the  removal  of  PFOS  by  a  Fe  anode with  four  different  types  of  electrolytes,  i.e.,  NaCl, Na2SO4, NaNO 3, and NaH2PO4. The results showed that the  removal  performance  follows  the  following  trend: NaCl  (99.6%)  >  Na2SO4  (93.7%)  >  NaNO3  (63.5%)  > NaH2PO4  (45.4%). Studies  have  shown  that  the immersion  of  metallic  Fe  in  water  at  open  circuit conditions would result in the generation of impenetrable passive  ferric  oxide  film  that  restricts  the  anodic dissolution  of  Fe. With  the  presence  of  Cl–,  the passivation of the Fe electrode could be delayed due to its catalytic  action  (Amani-Ghadim et al., 2011). However, high  concentrations  of  Cl–  may  lead  to  secondary pollutants  (e.g.,  Cl2  and  ClO–). Meanwhile,  the  NO3– could be adsorbed on the surfaces of the Fe anode and the Fe  hydroxide  precipitates,  which  effectively  reduce  the electrochemical  dissolution  and  polymerization  of  the

**NQ15_MMG005**

> As the conductivity of the electrolyte solution and the surface water were comparable (300 µ S/cm versus 320 µ S/cm), the composition of the cations and anions in the surface water was then considered a possible cause of the differing breakdown rates.

### Anonymous candidate answer

1. Answerability 
answerable – This is a conceptual/methodological question that can be addressed using general electrochemistry, surface chemistry, and PFAS behavior principles without specific literature.

---

2. Answer 

Electrolyte composition and pH-control choices can strongly change what you *think* you are measuring in PFAS experiments—removal vs. true degradation, reaction mechanism, rates, and byproduct profiles—without you realizing it. Key ways this happens:

### A. Electrolyte composition

#### 1. Competing adsorption and surface coverage
- Many PFAS treatment processes depend on adsorption (e.g., onto activated carbon, mineral surfaces, catalysts, or reactor walls) or on interfacial reactions (e.g., at electrodes, gas–liquid interfaces, or catalysts).
- Electrolyte ions that adsorb strongly (e.g., certain anions, multivalent cations) can:
 - Compete with PFAS for surface sites, reducing apparent “removal” that is actually only adsorption.
 - Change the surface charge, zeta potential, and hydrophobicity, shifting PFAS adsorption equilibria.
- Interpretation risk:
 - An observed change in PFAS concentration may be mainly due to altered adsorption equilibrium caused by ionic strength or specific ions, not due to changes in degradation chemistry.
 - Differences in “performance” across treatments may reflect differences in background electrolyte, not the PFAS treatment process itself.

#### 2. Ionic strength and activity coefficients
- Ionic strength affects:
 - PFAS speciation (for borderline pKa species or zwitterions).
 - Activity coefficients of PFAS, oxidants/reductants, and intermediate radicals.
 - Double-layer thickness and interfacial potential at electrodes or particles.
- Interpretation risk:
 - Apparent rate constants or removal extents can change simply because ion activities and interfacial fields change with ionic strength.
 - Comparing experiments at different electrolyte strengths can misattribute changes in kinetics to the process (e.g., catalyst, electrode material) instead of to ionic strength.

#### 3. Radical scavenging and oxidant/reductant pathways
- Many electrolytes participate in side reactions:
 - Carbonate/bicarbonate, chloride, and natural organic matter can scavenge hydroxyl radicals or other transients.
 - Chloride, nitrate, sulfate, and others can generate secondary oxidants (e.g., chlorine radicals, sulfate radicals, nitrogen oxides) under advanced oxidation or electrochemical conditions.
- Interpretation risk:
 - Changing the electrolyte can shift the dominant oxidative (or reductive) pathway, altering which PFAS are degraded, which bonds break, and what byproducts form.
 - Without recognizing changes in radical speciation, you may misinterpret mechanism (e.g., attributing degradation to •OH when halogen radicals or other species are dominant).

#### 4. Complexation and aggregation
- Multivalent cations (e.g., Ca²⁺, Mg²⁺, Fe³⁺, Al³⁺) can:
 - Form complexes with PFAS or with co-contaminants.
 - Promote PFAS aggregation, co-precipitation, or partitioning into colloidal phases.
- Interpretation risk:
 - PFAS “removal” may be enhanced by precipitation or flocculation rather than chemical degradation.
 - Apparent rapid loss of PFAS from solution can be mistaken for destruction if solid-phase mass balances and fluoride release are not measured.

#### 5. Background carbon and organic matter
- Electrolytes containing organic buffers or organic impurities add:
 - Additional carbon sources that can be oxidized or reduced.
 - Additional radical scavengers and surfaces for sorption.
- Interpretation risk:
 - Competing consumption of oxidants/reductants can slow PFAS degradation without changes in measured bulk oxidant concentration (if not appropriately monitored).
 - Organic electrolytes may themselves produce fluorinated or non-fluorinated byproducts that complicate interpretation of PFAS product scans.

### B. pH and pH-control strategies

#### 1. pH-dependent PFAS speciation and interfacial behavior
- Most perfluoroalkyl carboxylates and sulfonates are fully deprotonated across typical environmental pH, but:
 - Some precursor PFAS, zwitterionic species, and short-chain analogues have pH-sensitive speciation.
 - Interfacial accumulation, micellization, and adsorption can be pH-dependent due to electrostatic interactions and surface charge.
- Interpretation risk:
 - Changes in “removal” observed when pH drifts during a run may be due to altered sorption or aggregation, not to kinetic changes in bond-breaking.
 - Comparing experiments at different pH without accounting for speciation can mix kinetic and equilibrium effects.

#### 2. Electrode potentials, redox chemistry, and radical generation
- pH shifts:
 - Standard redox potentials of common oxidants/reductants (e.g., O₂/H₂O₂, HO•/H₂O).
 - Competition between water oxidation/reduction and target PFAS reactions at electrodes.
 - The distribution of radical species (e.g., HO• vs. O•⁻ vs. H•).
- Interpretation risk:
 - The same applied potential can produce different reactive species at different pH, so kinetics and pathways shift.
 - If pH is not controlled or reported, the “same” electrochemical or AOP conditions become non-comparable between runs or studies.

#### 3. Buffer choice vs. continuous pH adjustment

**Using buffers (e.g., phosphate, borate, carbonate, Good’s buffers):**
- Pros:
 - Stabilizes pH, limiting drift that affects speciation and rates.
- Cons:
 - Many buffers are radical scavengers, metal complexants, or surface-active.
 - Phosphate, carbonate, and others can change:
 - Radical lifetimes and yields.
 - Metal catalyst surface structure/speciation.
 - Adsorption equilibria and double-layer structure.
- Interpretation risk:
 - You may be characterizing “the effect of the buffer” more than the intrinsic PFAS degradation process.
 - Comparison across buffers (or vs. unbuffered systems) can change apparent kinetics and mechanisms even at identical pH.

**Using strong acid/base titration to hold pH:**
- Pros:
 - Avoids organic buffering species that act as radical scavengers.
- Cons:
 - Requires active monitoring and frequent addition, which:
 - Changes ionic strength and counterion composition over time (e.g., increasing Na⁺, Cl⁻, NO₃⁻).
 - Can introduce halides or other ions that alter radical pathways or electrode reactions.
- Interpretation risk:
 - Evolution of ionic strength and composition during the experiment can gradually alter kinetics and mechanisms.
 - If only initial pH is reported, changes in system chemistry over time are hidden.

#### 4. pH drift as a mechanistic signal vs. confounder
- PFAS degradation, co-contaminant reactions, and electrode processes can consume or produce H⁺/OH⁻, causing pH drift.
- pH drift can itself:
 - Change PFAS speciation, adsorption, and interfacial accumulation.
 - Shift radical speciation and electrode overpotentials.
- Interpretation risk:
 - Observed changes in rate during the experiment (e.g., slowing or acceleration) may reflect pH drift, not intrinsic kinetics.
 - However, the direction and magnitude of pH drift can be a useful mechanistic indicator if measured and interpreted correctly.

### C. Distinguishing “removal” from “degradation”

Electrolyte and pH choices particularly affect whether you are observing:

- **Physical/chemical separation:**
 - Adsorption to solids, reactor walls, or bubbles.
 - Co-precipitation with metal hydroxides or salts.
 - Micellization or transfer to an unmonitored phase.
- **Chemical transformation:**
 - Partial defluorination, chain-shortening, or functional group modification.
 - Complete defluorination and mineralization (endpoints like F⁻ and CO₂).

Because electrolytes and pH control:
- Sorption equilibria.
- Aggregation and phase behavior.
- Radical and redox speciation.
You must design and interpret experiments so that:

1. **Aqueous concentration changes are not automatically equated with degradation.** 
 Controls are needed to detect sorption, precipitation, and phase transfer.

2. **Defluorination and product formation are measured separately.** 
 - Fluoride release, carbon balances, and transformation products help distinguish true degradation from mere removal.

3. **Mass balances across all phases** (solution, solids, headspace) are considered, especially when electrolytes promote sorption or precipitation.

### D. Implications for experimental design and interpretation

To reduce misinterpretation caused by electrolyte and pH choices:

1. **Standardize or carefully document electrolyte conditions.**
 - Report identity, concentration, ionic strength, and rationale for each component.
 - Avoid unnecessary ions that have strong surface, redox, or radical chemistry, unless they represent realistic matrices you are intentionally testing.

2. **Use minimal, mechanistically appropriate pH control.**
 - Choose buffers or titrants with known and acknowledged influences on redox and radical chemistry.
 - Report both initial and final pH, and ideally the pH evolution over time.

3. **Include matrix and electrolyte controls.**
 - Control experiments with electrolyte and pH control but no reactive treatment (e.g., no current, no light, no catalyst) to quantify sorption and matrix-driven removal.
 - If testing different electrolytes, keep ionic strength as constant as possible when isolating “specific ion” effects.

4. **Explicitly separate performance metrics.**
 - Report at least:
 - PFAS disappearance from the monitored phase.
 - Inorganic fluoride formation.
 - Identified transformation products.
 - Interpret differences across electrolytes and pH first in terms of these separate endpoints, not as a single “removal efficiency.”

---

3. Uncertainty and limitations 

- Quantitative magnitudes of electrolyte and pH effects (e.g., exact changes in rate constants, radical yields, or adsorption coefficients) depend on specific PFAS, matrices, and technologies and cannot be generalized without system-specific data. 
- Some PFAS classes (e.g., short-chain, zwitterionic, precursors, fluorotelomers) have more complex pH-dependent behavior than long-chain anionic PFAS, which can alter the relative importance of the mechanisms described. 
- Real waters (groundwater, wastewater, seawater) include multiple inorganic and organic components whose combined effects may be non-additive and are not predictable from simple electrolyte models.

---

4. Practical takeaway 

When designing or interpreting PFAS removal/degradation experiments, treat electrolyte composition and pH-control strategy as central reaction variables—document and control them explicitly, use appropriate matrix controls and mass balances, and avoid interpreting loss from the aqueous phase as chemical degradation without independent evidence of defluorination and transformation products.

### Human label

- Adequate (`yes` / `no` / `uncertain`):
- Material scientific error (`yes` / `no` / `uncertain`):
- Confidence (`high` / `medium` / `low`):
- Notes:

---

## D13-A014

**Question ID:** `WF10_004a`

**Question:** How does PFAS chain length affect reported treatment performance or adsorption behavior?

**Must include:** Compare studies only on matched compounds, matrices, endpoints, and conditions; avoid ranking technologies when the evidence is not comparable.

**Must not claim:** Do not convert a condition-specific finding into a universal PFAS treatment claim.

### Reference evidence

**WF10_004a_MMG001**

> The removal efficiency of long- chain PFAS is higher than that of short-chain PFAS across all sorbents (Fig.

**WF10_004a_MMG002**

> The removal efficiency of PFOA (73% ± 24%) and PFOS (89% ± 35%) is higher than that of PFBA (30% ± 11%) and PFBS (55% ± 18%) in all three adsorbents (Figure 3a), as long-chain PFAS are more adsorbed on carbonaceous-based adsorbents than short-chain PFAS.

**WF10_004a_MMG003**

> Compared to the removal of long-chain PFAS, e.g., 98.8% for PFOS and 87.6% for PFOA, the overall removal efficiency of short-chain PFAS is much lower than that of long-chain PFAS, highlighting once again the challenges of the removal of these short-chain substances from aqueous solutions because of their low hydrophobicity.

**WF10_004a_MMG004**

> longer-chain PFAS are more hydrophobic and less water-soluble, leading to higher adsorption capacities onto adsorbents [ 67, 68, 82, 89, 90].

**WF10_004a_MMG005**

> Long-chain PFASs can interact via hydrophobic tails through hydrophobic interactions, and the chain length and orientation of PFAS molecules signif- icantly influence the adsorption process.

**WF10_004a_MMG006**

> length, carboxylic/sulfonic groups, branched/linear structure and adsorb- ents’ ages on PFAS removal, although there are some agreement to certain extent (e.g., removal efficiencies are often better for long-chained, carbox- ylic, and linear PFAS), many other factors that can influence the large-scale removal efficiencies remain largely unknown (e.g., effects of water/waste- water organic and inorganic content) and contradictory results are often reported for different water/wastewater, adsorbents, and experimental con- ditions, which warrants further investigation.

### Anonymous candidate answer

1. Answerability 
answerable – Multiple studies directly evaluate how PFAS perfluoroalkyl chain length influences adsorption and column treatment performance on common sorbents.

2. Answer 

Across adsorbents and treatment configurations, longer perfluoroalkyl chain length consistently improves PFAS adsorption strength and practical removal, while short‑chain PFAS are more weakly retained and break through earlier.

Key patterns:

- **Thermodynamics and molecular interaction**
 - Computational work shows that as the number of fluorinated carbons increases, the Gibbs free energy of adsorption (ΔG) becomes more negative, indicating that longer‑chain PFAS are thermodynamically favored to adsorb regardless of functional group.
 - Longer chains have higher hydrophobicity (e.g., higher log K_ow or log D), which strengthens hydrophobic and van der Waals interactions with sorbent surfaces; short‑chain PFAS, with fewer fluorinated carbons, have reduced hydrophobic interactions and lower sorption affinity.
 - A strong correlation (r² ≈ 0.97) has been reported between sorption coefficient (K_F) and log K_ow across PFAS, directly linking increasing hydrophobicity (and thus chain length) to increasing adsorption strength.

- **General adsorption behavior (GAC, PAC, CAC, sludge, etc.)**
 - Short‑chain PFAS are more hydrophilic, smaller, and more mobile, giving them a low adsorption potential and making them harder to adsorb.
 - On activated carbons, sorption affinity increases with chain length: for example, batch isotherms on GAC show the order PFOA > PFHxA > PFPeA > PFBA, with higher Freundlich K_F and lower n as chain length increases, indicating stronger and more nonlinear sorption for longer chains.
 - In wastewater sludge, sorption capacity increased with C–F chain length, reaching about 90 % removal for long‑chain PFUnDA (C10) but only ~33 % for PFOA, consistent with hydrophobicity‑driven sorption and weaker capture of shorter‑chain PFAS.
 - Field and lab studies with colloidal activated carbon (CAC) indicate that sorption strength scales with perfluoroalkyl tail length; longer‑chain PFAS sorb more strongly, while short‑chain PFCAs and PFSAs remain more mobile and are less effectively stabilized.

- **Column performance and breakthrough behavior (GAC and ion exchange)**
 - In packed‑bed GAC and ion exchange (IX) columns treating groundwater, long‑chain PFAS (e.g., PFOA, PFOS) are preferentially removed over short‑chain species when normalized to influent concentration.
 - Within PFSA or PFCA classes, shorter‑chain PFAS always break through before longer‑chain PFAS; PFAS with higher hydrophobicity and molecular weight are statistically more amenable to GAC adsorption.
 - Detailed GAC and anion exchange column tests across C3–C14 PFCAs and C4–C8 PFSAs found:
 - A clear positive relationship between perfluorocarbon chain length and removal efficiency for both GAC and AE.
 - Time to column breakthrough increased with chain length.
 - Shorter‑chain PFCAs (e.g., PFBA, PFPeA, PFHxA) showed desorption behavior, while longer‑chain PFAS showed sustained removal.
 - Another study with GAC and IX found that IX resins outperformed GAC overall but were not effective for short‑chain PFCAs, and again, within each functional class, shorter‑chain PFAS broke through first.

- **Functional group and chain length interplay**
 - For a given carbon length, PFSAs tend to sorb more strongly than PFCAs (e.g., PFOS > PFOA; PFHxS > PFHxA; PFBS > PFBA), reflecting an additional hydrophobic CF₂ in PFSAs and their higher log D.
 - Column data from landfill leachate treatment show that breakthrough volumes (BV₅₀) increase with both log D and chain length, and within equal‑chain pairs (PFBA vs PFBS, PFHxA vs PFHxS, PFOA vs PFOS), the sulfonates always had higher BV₅₀, again indicating stronger hydrophobic interactions layered on top of the chain‑length effect.

- **Short‑chain–specific behavior and design responses**
 - Short‑chain PFAS removal is often limited by their high hydrophilicity and dependence on electrostatic interactions; their adsorption mechanism is dominated by interactions between anionic head groups and cationic sites on the adsorbent, rather than strong tail‑driven hydrophobic partitioning.
 - To compensate, sorbents with enhanced positive surface charge (e.g., PEI‑modified nanofibers) have been developed, achieving relatively high capacities for short‑chain PFBA and PFBS specifically by boosting electrostatic attraction.

3. Uncertainty and limitations 

- Most evidence is for anionic PFCAs and PFSAs and common sorbents (GAC, IX, CAC, sludge); behavior of many polyfluorinated precursors, zwitterionic, or cationic PFAS may deviate from these trends. 
- Quantitative relationships (e.g., exact breakthrough volumes or K_F values) are system‑specific and depend on water matrix, co‑solutes, and sorbent properties; cited patterns are comparative within each study, not universal numerical rules. 
- At very high surface loadings, aggregation or bilayer formation of long‑chain PFAS can alter adsorption behavior in ways not fully characterized, and most data are at environmentally relevant but not extremely high concentrations.

4. Practical takeaway 

For adsorption‑based PFAS treatment, longer perfluoroalkyl chains consistently show stronger, hydrophobically driven sorption and later breakthrough, whereas short‑chain PFAS are more mobile, more weakly adsorbed, and often require tailored sorbent chemistry (e.g., strong cationic surfaces) or complementary processes to achieve comparable removal.

### Human label

- Adequate (`yes` / `no` / `uncertain`):
- Material scientific error (`yes` / `no` / `uncertain`):
- Confidence (`high` / `medium` / `low`):
- Notes:

---

## D13-A015

**Question ID:** `WF10_030`

**Question:** Under what conditions might supercritical water oxidation leave uncertainty about fluorinated products?

**Must include:** Use limitation, uncertainty, caveat, and negative evidence to avoid overclaiming beyond the reported study scope.

**Must not claim:** Do not convert a condition-specific finding into a universal PFAS treatment claim.

### Reference evidence

**WF10_030_MMG001**

> Trifluoroacetic acid (TFA) was found to be the most recalcitrant intermediate product in the effluent, persisting at T = 600 ◦ C and residence time of ~ 32 s, emphasizing the need for TFA monitoring in SCWO treatment of PFAS-impacted matrices.

**WF10_030_MMG002**

> However, a low fluorine mass balance at temperatures of 425 and 450 ◦ C may indicate the ex - istence of fluorinated species in the gaseous and/or liquid product which are not detected by targeted analysis.

**WF10_030_MMG003**

> However, SCWO experimental studies on identifying PFAS degradation intermediates are still incomplete.

### Anonymous candidate answer

1. Answerability 
answerable – Supplied studies and reviews directly describe SCWO conditions under which fluorinated products are incompletely characterized.

2. Answer 
Uncertainty about what fluorinated products are formed or remain after SCWO is greatest under conditions where:

- **Defluorination lags parent-PFAS destruction (moderate T, short residence)** 
 In continuous-flow SCWO, PFAS “destruction and removal efficiency” can be ≥99.999% at >610 °C and ~30 s residence, but measured fluoride recovery lags PFAS destruction at 510 °C, only exceeding 100% above 610 °C. This lag in fluoride vs. parent removal, and the authors’ note that “Defluorination efficiency lags destruction suggesting formation of intermediate species,” indicates that at lower SCWO temperatures and/or insufficient residence times, substantial organofluorinated intermediates (liquid or gaseous) are present but not fully identified.

- **Only parent PFAS and inorganic fluoride are measured (no total organofluorine / nontarget)** 
 Studies emphasize the need for total organofluorine, total oxidizable precursor, and/or nontargeted analyses to “comprehensively assess fluorine content within wastes to be treated/disposed,” noting that SCWO mineralized “fluorine compounds that were not identified.” When analytical scope is limited to parent PFAS and fluoride, especially at less‑severe conditions, the distribution between inorganic fluoride and unknown organofluorine products remains uncertain.

- **Incomplete gas-phase characterization, especially for volatile organofluorines** 
 Existing SCWO studies often lack gas analysis data “due to the dilute nature of emission from the large SCWO systems and … challenges related to the analysis methods and the lack of gaseous VOF libraries.” Reviews further note that stepwise SCWO destruction can generate small volatile organofluorine byproducts such as trifluoromethane and shorter perfluorocarboxylic acids. When off-gas is not fully speciated, the identity and mass fraction of volatile fluorinated products are uncertain.

- **Substantial destruction but only partial defluorination** 
 Field validation trials report >99.999% destruction/removal of 12 PFAAs but an overall defluorination of only ~62.6%. Under such conditions—high parent removal but moderate fluoride yield—there is clear evidence that a large portion of fluorine remains in uncharacterized organofluorinated forms.

- **Limited mechanistic understanding and short experimental timescales** 
 It is recognized that, although SCWO can effectively degrade fluorinated compounds, “there is a notable lack of research on the reaction mechanisms of PFAS under these conditions,” which hinders full understanding of product evolution. Simulations and batch experiments show that fluorine conversion can be incomplete at 500 °C over certain timescales (e.g., PFOS fluorine conversion ~78% after 60 min at 500 °C), reinforcing that under some temperature–time–oxygen combinations, partially transformed fluorinated species persist.

- **Supercritical vs subcritical comparisons showing more volatile fluorinated byproducts** 
 Under supercritical conditions with added Fe, PFAS degradation is enhanced relative to subcritical water, but more CF₃H (trifluoromethane), a long‑lived greenhouse gas, is produced. Where monitoring does not specifically target such small fluorinated gases, their presence and quantities remain uncertain.

Overall, uncertainty about fluorinated products is most pronounced when SCWO is operated at moderate temperatures or short residence times, with limited analyte lists (parent PFAS and fluoride only) and sparse or no gas-phase and total organofluorine analyses, especially given the current incomplete mechanistic understanding.

3. Uncertainty and limitations 
- Many studies are lab or pilot scale and may not capture byproduct profiles at full scale. 
- Quantitative distributions of specific intermediates (e.g., individual short-chain PFAAs or specific volatile organofluorines) are often not reported, so statements about their presence are qualitative. 
- Evidence is stronger for a few model PFAS; behavior of broader PFAS classes under varied SCWO conditions is less certain.

4. Practical takeaway 
SCWO can nearly eliminate target PFAS, but unless you operate at sufficiently high temperature/residence and perform comprehensive aqueous and gas-phase fluorine speciation (including TOF/TOX and targeted/nontargeted volatile analyses), you should assume significant uncertainty about the identity and amount of fluorinated intermediate and byproduct species.

### Human label

- Adequate (`yes` / `no` / `uncertain`):
- Material scientific error (`yes` / `no` / `uncertain`):
- Confidence (`high` / `medium` / `low`):
- Notes:

---

## D13-A016

**Question ID:** `WF10_025`

**Question:** How should contact time be planned when powder activated carbon is used for both short- and long-chain PFAS?

**Must include:** Identify the relevant protocol steps, reagents/materials, operating conditions, matrix, target compounds, and reported limitations.

**Must not claim:** Do not convert a condition-specific finding into a universal PFAS treatment claim.

### Reference evidence

**WF10_025_MMG001**

> acids (PFCAs) and three perﬂuoroalkyl sulfonic acids (PFSAs), were tested to ﬁnd their adsorption selectivity from surface water and the feasibility of the powder activated carbon (PAC) process between the perchlorination and coagulation processes by operating parameters such as mixing intensity, dosage, contact time, initial pH, and concentration of perchlorination. The removal eﬃciency of four types of PAC revealed that the coal-based activated carbon was clearly advanced for all of the PFASs, and the thermal regenerated PAC did not exhibit a signiﬁcant reduction in adsorption capacity. The longer carbon chain or the higher molecular weight (MW) obtained a higher adsorption capacity and the MW exhibited a more proportional relationship with the removal eﬃciency than the carbon chain number, regardless of the PFCA and PFSA species. Approximately 80% and 90% equilibria were accomplished within 60 and 120 min for the long chain carbon PFAS, respectively, while for the short chain PFAS, 240 min was required to reach 85% equilibrium. The eﬀect of mixing intensity (rpm) was not considered for the removal of the PFAS, although it was relatively inﬂuenced in the short PFAS species. Due to the surface charge of the PAC and the properties of protonation of the PFASs, the acid condition increased the PFASs’ adsorption capacity. The prechlorination decreased

### Anonymous candidate answer

1. Answerability 
partially_answerable – General design principles for PAC contact time are known, but compound‑specific kinetic data needed for exact values are not available here.

2. Answer 
For PAC used to treat both long‑ and short‑chain PFAS, contact time should be planned and evaluated explicitly around the *slowest* (short‑chain) adsorbing species, not just the easiest (long‑chain) ones:

- **Design for short‑chain breakthrough, not long‑chain:** 
 - Long‑chain PFAS (e.g., PFOS, long‑chain PFCAs) adsorb faster and stronger to PAC than short‑chain PFAS. 
 - If contact time is set only to achieve high removal of long‑chain PFAS, short‑chains will typically be under‑treated. 
 - Therefore, the target hydraulic residence time (HRT) or mixing time in PAC contactors should be based on achieving the desired removal for the *most persistent short‑chain PFAS* in the mixture.

- **Use staged or extended contact where possible:** 
 - **Increase overall contact time** (longer HRT, larger basins, or multiple contact tanks in series) until additional time no longer improves short‑chain removal. 
 - **Staged PAC dosing (multiple addition points)** can help: an initial dose to capture hydrophobic, long‑chain species and organics, followed by a later dose with “freer” sites that are more available for short‑chains. 
 - Avoid very short, high‑shear contact (e.g., flash mixing only) as the main contact time; provide a quiescent or gently mixed period to approach adsorption equilibrium, especially for short‑chain PFAS.

- **Plan contact time jointly with PAC dose and competing organics:** 
 - Higher background DOC and other organics increase competition and slow effective PFAS uptake, which functionally increases the contact time needed for a given removal. 
 - In design and piloting, vary both PAC dose and contact time to find the combination that meets short‑chain PFAS goals without over‑designing solely on dose.

- **Verify with site‑specific kinetics and breakthrough testing:** 
 - Perform jar tests or pilot contactors with your actual water/wastewater and PFAS mixture. 
 - Measure removal of representative long‑ and short‑chain PFAS at multiple contact times (e.g., several points from “few minutes” up to the longest practical HRT). 
 - Select operational contact time as the minimum that consistently meets targets for **both** classes under worst‑case conditions (high flow, high PFAS/DOC).

3. Uncertainty and limitations 
- The optimal contact time depends strongly on the specific PAC product, PFAS mixture, DOC and co‑contaminant levels, mixing intensity, and temperature. 
- Without compound‑ and site‑specific kinetic data, only qualitative guidance (design for short‑chains, stage contact, and pilot‑test) is reliable; numeric HRT recommendations would be speculative.

4. Practical takeaway 
Plan and optimize PAC contact time around short‑chain PFAS removal—using extended or staged contact validated by site‑specific tests—because long‑chain PFAS will usually be controlled at equal or shorter times, while short‑chains require the most conservative design.

### Human label

- Adequate (`yes` / `no` / `uncertain`):
- Material scientific error (`yes` / `no` / `uncertain`):
- Confidence (`high` / `medium` / `low`):
- Notes:

---

## D13-A017

**Question ID:** `WF10_002`

**Question:** When comparing membrane filtration, gliding arc plasma, and supercritical water oxidation for PFAS treatment, which reported endpoints should be kept separate?

**Must include:** Keep removal, separation, adsorption, degradation, defluorination, mineralization, destruction, byproduct formation, and mass-balance evidence separate.

**Must not claim:** Do not convert a condition-specific finding into a universal PFAS treatment claim.

### Reference evidence

**WF10_002_L3X001**

> Among different approaches, high-pressure membrane filtration pro - cesses that utilize nanoporous membranes like nanofiltration (NF) and reverse osmosis (RO) have proven to be highly effective in separating both short- and long-chain PFAS compounds with rejection efficiencies typically exceeding 90 % [ 24 , 25 ].

**WF10_002_L3X002**

> Membrane‑assisted chemical degradation Generally, the abovementioned treatment methods (filtra- tion, adsorption, and membrane distillation) can only con- centrate PFAS.

**WF10_002_L3X003**

> However, a low fluorine mass balance at temperatures of 425 and 450 ◦ C may indicate the ex - istence of fluorinated species in the gaseous and/or liquid product which are not detected by targeted analysis.

**WF10_002_MMG001**

> Results and discussion To demonstrate that the engineered GAP system is an effec- tive treatment system for PFAS contaminated water the disap- pearance of the target analyte Ĳs), formation of degradation products, defluorination, and energy costs were measured and calculated.

**WF10_002_MMG002**

> Non-plasma-based PFAS treatment technolo- gies where high temperature make an important contribution to PFAS degradation, such as sonolysis [23,27] and supercritical water oxidation (SCWO) [6], have shown excellent potential in mineralizing PFAS with minimal short-chain PFAS formation, and increased mineralization with a rise in reaction temperatures has been observed in SCWO [ 6,28].

### Anonymous candidate answer

1. Answerability 
answerable – The question is conceptual and the available evidence directly addresses the key endpoints used for membrane, plasma, and SCWO PFAS treatments.

2. Answer 
When comparing membrane filtration (phase-transfer) with gliding arc plasma and supercritical water oxidation (destructive), keep the following reported endpoints clearly separated:

- **Phase-transfer vs destruction endpoints**
 - **PFAS rejection / separation / removal from water (membranes)** 
 - Metrics such as “rejection,” “removal,” or “separation” by RO/NF indicate transfer of PFAS from the feed to a concentrate stream, not chemical breakdown. 
 - **Destruction / degradation / mineralization (plasma, SCWO)** 
 - Metrics such as “percent destruction,” “destruction and removal efficiency (DRE),” “degradation,” or “mineralization” refer to chemical transformation of PFAS, not just physical separation.

- **Destruction vs defluorination / mineralization**
 - **Destruction / disappearance of parent PFAS** 
 - Disappearance of target analytes (e.g., PFOS, PFOA) or high DRE values indicate breakdown of the parent molecule. 
 - **Defluorination efficiency** 
 - Release of fluoride (or % defluorination) reflects how completely the C–F bonds are broken; this can lag behind destruction and indicate formation of fluorinated intermediates. 
 - **Mineralization** 
 - Often defined as near-complete conversion to inorganic products (CO₂, F⁻, etc.) and is more stringent than simple “destruction” or “degradation.”

- **Parent removal vs byproduct formation**
 - **Parent PFAS removal** (by any technology) 
 - Disappearance from the measured matrix (feed water, effluent, off‑gas). 
 - **Formation and fate of transformation products** 
 - Identification/quantification of degradation products is a distinct endpoint and must not be assumed from parent loss alone.

- **Energy and performance metrics**
 - **Energy use per volume treated** (e.g., kWh/m³, W/L; common for membranes and some plasma systems). 
 - **Energy yield / cost per mass degraded or per log DRE** (e.g., mg/kWh; more relevant for destructive processes). 
 These are not directly interchangeable and should be compared on the same basis before drawing conclusions.

In summary, do not collapse:
- membrane rejection/separation ↔ chemical destruction,
- parent PFAS destruction/DRE ↔ defluorination/mineralization,
- parent loss ↔ absence of harmful intermediates,
- energy per volume treated ↔ energy per mass of PFAS destroyed.

3. Uncertainty and limitations 
- The evidence provides representative endpoints but not a complete catalog; different studies may define “destruction,” “mineralization,” or “defluorination” differently. 
- Quantitative comparability across technologies is limited by differing matrices, PFAS mixtures, and reactor scales.

4. Practical takeaway 
When comparing membrane filtration with gliding arc plasma and SCWO, interpret and report: (1) separation/removal, (2) chemical destruction/DRE, (3) defluorination/mineralization, (4) byproduct formation, and (5) energy metrics as distinct endpoints, and avoid treating any one of these as a surrogate for the others.

### Human label

- Adequate (`yes` / `no` / `uncertain`):
- Material scientific error (`yes` / `no` / `uncertain`):
- Confidence (`high` / `medium` / `low`):
- Notes:

---

## D13-A018

**Question ID:** `NQ26`

**Question:** What membrane-based PFAS treatment routes are described, and which routes separate or concentrate PFAS rather than destroy or transform them?

**Must include:** Must distinguish pressure-driven separation, NF/RO, modified membranes, electrical membranes, and any destructive membrane-coupled process.

**Must not claim:** Must not equate membrane separation or retention with PFAS destruction.

### Reference evidence

**NQ26_MMG001**

> Beside regenerable IX-R, other traditional separation technologies such as reverse osmosis and nanofiltration, which produce a concentrated PFAS waste stream, have also been demonstrated in tandem with a destruction technology for effective remediation of PFAS [ 23 , 25 ].

**NQ26_MMG002**

> Membrane‑assisted chemical degradation Generally, the abovementioned treatment methods (filtra- tion, adsorption, and membrane distillation) can only con- centrate PFAS.

**NQ26_MMG003**

> Another severe limitation of membrane-based processes is that they do not degrade PFAS;

**NQ26_MMG004**

> Among different approaches, high-pressure membrane filtration pro - cesses that utilize nanoporous membranes like nanofiltration (NF) and reverse osmosis (RO) have proven to be highly effective in separating both short- and long-chain PFAS compounds with rejection efficiencies typically exceeding 90 % [ 24 , 25 ].

**NQ26_MMG005**

> To treat PFAS-contaminated water more effectively, research should be conducted on combining degradation (e.g., electrodegradation, biodegradation, etc.) and con- centration (e.g., filtration, membrane distillation, forward osmosis, etc.) treatments.

**NQ26_MMG006**

> Membrane-assisted degradation differs from simple deg- radation in that PFAS are first adsorbed onto a membrane (to which catalysts may be added) and then degraded under light or an electric field (Fig.

**NQ26_MMG007**

> Of note, low-pressure membranes such as microfiltration and ultrafiltration poorly remove PFAS and are not discussed in this review (Glover et al., 2018;

**NQ26_MMG008**

> carbon is incinerated, whereas in the membrane processes, the con- centrate is sent to an evaporation pool where the residue can be then collected and incinerated.

### Anonymous candidate answer

1. Answerability 
answerable – The passages describe several specific membrane-based PFAS treatment routes and clearly indicate which are separation/concentration versus degradation-focused.

2. Answer 

Membrane-based PFAS treatment routes described in the evidence

Primarily separation / concentration (do not destroy PFAS)

- **Pressure-driven membrane filtration (NF and RO)** 
 - Identified as the most commonly used membrane-based PFAS treatment; commercial NF/RO can reach ~99% PFAS removal from the permeate. 
 - Filtration is explicitly stated to “concentrate, but not destroy, PFAS.” 
 - NF and RO (and also nanofiltration/reverse osmosis generally) are listed among separation-based methods that “can be applied in the separation of PFAS from drinking water” and “do not eliminate them, resulting in secondary waste streams.”

- **Membrane distillation (MD)** 
 - Listed as a membrane-based treatment method and as a thermal-driven membrane process for PFAS removal. 
 - MD is described as an evaporative separation technique that can “effectively concentrate PFAS from liquid solutions” because PFAS have low vapor pressure. 
 - In a broader classification, MD is grouped with NF and RO as a membrane separation route, where “membrane separation of PFAS requires further treatment of the rejected PFAS in the concentrate stream,” indicating separation rather than destruction. 
 - MD is described as a separation-based technology with high PFAS rejection but not a destruction method.

- **Forward osmosis (FO)** 
 - Mentioned as a concentration treatment (along with filtration and membrane distillation) to pre‑concentrate PFAS. 
 - As a concentration/separation step, it does not by itself destroy PFAS.

- **Electrodialysis (ED) used as a concentration/separation step** 
 - ED is presented as suitable for treating short-chain PFAS “because contaminants need to pass through a membrane for the contaminant solution to become concentrated.” 
 - In this mode, ED functions as a membrane-based concentration route, not a destruction step.

- **General membrane separation / nanofiber and adsorptive membranes** 
 - Membrane separation technologies beyond NF/RO include membrane distillation and nanofiber membranes as emerging routes for PFAS removal. 
 - Separation-based methods, including “several membrane processes,” are said to remove PFAS from water but “do not eliminate them,” producing secondary concentrated waste streams. 
 - Membrane separation (NF, RO, MD) combined with non-destructive adsorption/ion exchange is specifically classified as “membrane technology integrated with non-destructive processes,” i.e., purely separation and concentration.

- **Membrane-assisted concentration as pretreatment for destruction** 
 - Filtration, membrane distillation, and forward osmosis are recommended as concentration steps prior to energy-intensive electrochemical degradation. 
 - These steps are explicitly identified as concentration, not destruction.

Primarily destruction / transformation (membrane-associated degradation routes)

- **Membrane-assisted chemical degradation (catalytic membranes)** 
 - “Membrane-assisted degradation differs from simple degradation in that PFAS are first adsorbed onto a membrane (to which catalysts may be added) and then degraded under light or an electric field.” 
 - Examples include: 
 - A catalyst-containing membrane used to degrade PFOA via a microwave-Fenton-like reaction (incomplete; PFPeA remained). 
 - Photocatalysis applied to PFOA previously adsorbed on a membrane. 
 - These routes combine a membrane (for adsorption/local concentration) with a destructive process (Fenton-like, photocatalytic).

- **Electrical treatment / electrochemical degradation in membrane systems** 
 - Electrical treatment is distinguished from filtration: “Electrical treatment can degrade PFAS, whereas filtration can concentrate but not eliminate PFAS.” 
 - Membranes (e.g., in electrodialysis–electrosorption configurations) are used together with electrochemical processes; in such hybrids, the electrical step is destructive, the membrane step is separative.

- **Hybrid membrane + destructive processes (AOPs and related)** 
 - The review on membrane technologies notes a class of “membrane technology with a destructive treatment process,” such as combining membrane separation with advanced oxidation or other destructive routes. 
 - Destruction-based methods (AOPs, electro-oxidation, plasma) are generally contrasted with separation-based techniques; they aim to chemically break down PFAS and potentially achieve mineralization, though with high energy demand and by‑product concerns.

Summary classification

- **Membrane routes that separate/concentrate PFAS (non-destructive):** 
 - Pressure-driven membrane filtration (NF, RO) 
 - Membrane distillation (MD, including evaporative separation) 
 - Forward osmosis (FO) 
 - Electrodialysis when used to concentrate PFAS (short-chain PFAS treatment) 
 - Nanofiber/adsorptive membranes used purely for separation/adsorption (non-destructive) 
 - Hybrid systems where membranes are combined with non-destructive processes (adsorption, ion exchange)

- **Membrane-associated routes that destroy or transform PFAS:** 
 - Membrane-assisted chemical degradation (catalyst-bearing membranes under light, electric field, or microwave-Fenton-like conditions) 
 - Electrical treatment/electrochemical degradation used with membranes (e.g., electrodialysis–electrosorption hybrids), where the electrical step degrades PFAS 
 - Hybrid membrane processes explicitly integrated with destructive treatments such as AOPs, EO, or plasma (membrane + destructive process class)

3. Uncertainty and limitations 

- The evidence mostly classifies at the mechanism level (separation vs destruction) and does not systematically quantify defluorination or mineralization; some “degradation” examples are incomplete (e.g., PFOA → PFPeA), so transformation does not necessarily mean full destruction. 
- Electrodialysis and other electrically driven membrane processes can be configured as purely separative or partially destructive depending on cell design; the passages only clearly distinguish these in a few examples. 
- Not all membrane-based PFAS approaches in the broader literature appear in these specific chunks; the list reflects only what is described here.

4. Practical takeaway 

Within the evidence, classical membrane operations—NF/RO, MD, FO, and electrodialysis—are used mainly to separate and concentrate PFAS, generating a PFAS-rich stream requiring further management, whereas PFAS destruction or transformation arises only when membranes are explicitly coupled with catalytic, electrical, or advanced oxidation steps (membrane-assisted degradation or hybrid membrane–AOP/EO/plasma systems).

### Human label

- Adequate (`yes` / `no` / `uncertain`):
- Material scientific error (`yes` / `no` / `uncertain`):
- Confidence (`high` / `medium` / `low`):
- Notes:

---

## D13-A019

**Question ID:** `NQ26`

**Question:** What membrane-based PFAS treatment routes are described, and which routes separate or concentrate PFAS rather than destroy or transform them?

**Must include:** Must distinguish pressure-driven separation, NF/RO, modified membranes, electrical membranes, and any destructive membrane-coupled process.

**Must not claim:** Must not equate membrane separation or retention with PFAS destruction.

### Reference evidence

**NQ26_MMG001**

> Beside regenerable IX-R, other traditional separation technologies such as reverse osmosis and nanofiltration, which produce a concentrated PFAS waste stream, have also been demonstrated in tandem with a destruction technology for effective remediation of PFAS [ 23 , 25 ].

**NQ26_MMG002**

> Membrane‑assisted chemical degradation Generally, the abovementioned treatment methods (filtra- tion, adsorption, and membrane distillation) can only con- centrate PFAS.

**NQ26_MMG003**

> Another severe limitation of membrane-based processes is that they do not degrade PFAS;

**NQ26_MMG004**

> Among different approaches, high-pressure membrane filtration pro - cesses that utilize nanoporous membranes like nanofiltration (NF) and reverse osmosis (RO) have proven to be highly effective in separating both short- and long-chain PFAS compounds with rejection efficiencies typically exceeding 90 % [ 24 , 25 ].

**NQ26_MMG005**

> To treat PFAS-contaminated water more effectively, research should be conducted on combining degradation (e.g., electrodegradation, biodegradation, etc.) and con- centration (e.g., filtration, membrane distillation, forward osmosis, etc.) treatments.

**NQ26_MMG006**

> Membrane-assisted degradation differs from simple deg- radation in that PFAS are first adsorbed onto a membrane (to which catalysts may be added) and then degraded under light or an electric field (Fig.

**NQ26_MMG007**

> Of note, low-pressure membranes such as microfiltration and ultrafiltration poorly remove PFAS and are not discussed in this review (Glover et al., 2018;

**NQ26_MMG008**

> carbon is incinerated, whereas in the membrane processes, the con- centrate is sent to an evaporation pool where the residue can be then collected and incinerated.

### Anonymous candidate answer

1. Answerability 
partially_answerable – The main membrane routes and their separation vs. destruction roles can be described from general technical knowledge, but I cannot tie them to specific studies or quantify performance without literature.

2. Answer 

The major membrane-based routes used or proposed for PFAS treatment, and whether they primarily **separate/concentrate** PFAS vs. **destroy/transform** them, can be grouped as follows:

**A. Pressure-driven membranes (almost entirely separation/concentration)** 
These operate by size/charge exclusion and do not chemically alter PFAS; PFAS are concentrated in the reject stream or retained phase. 
- **Reverse osmosis (RO)** – High-pressure dense membranes; PFAS (especially long-chain) are largely rejected and end up in the concentrate. 
- **Nanofiltration (NF)** – Similar to RO but somewhat more permeable; PFAS mainly rejected and concentrated in the retentate. 
- **Ultrafiltration (UF)** – Pore-size-based separation; most dissolved PFAS (molecular-scale) pass through, so UF is not a PFAS barrier by itself. Any PFAS retention is via association with particulates/colloids that are rejected (still separation, not destruction). 
- **Microfiltration (MF)** – Even larger pores; dissolved PFAS pass through. Only PFAS attached to particles or emulsions can be retained (again, separation only). 

→ **Function**: RO/NF are core PFAS **separation and concentration** technologies; UF/MF can indirectly separate particulate-bound PFAS. None of these destroy PFAS.

**B. Osmotically/thermally driven membranes (separation/concentration)** 
These rely on phase change or osmotic gradients; PFAS are physically separated and concentrated. 
- **Forward osmosis (FO)** – PFAS in feed are largely rejected by the FO membrane and concentrated in the feed/concentrate side; water moves osmotically. 
- **Membrane distillation (MD)** – Hydrophobic membrane passes water vapor; non-volatile PFAS remain in the feed and become concentrated. 
→ **Function**: PFAS remain chemically intact and are **concentrated**, not destroyed.

**C. Electromembrane processes (separation/concentration)** 
Ion migration across ion-exchange membranes under an electric field. 
- **Electrodialysis (ED) and related processes (EDR, BPM-ED, etc.)** – Charged PFAS (especially ionized PFAS acids) are transported and separated into concentrate compartments. 
→ **Function**: PFAS are **separated/repartitioned and concentrated** in specific streams; no inherent destruction.

**D. Ion-exchange and adsorption membranes (separation/concentration)** 
Membranes functionalized with sorbent/ion-exchange sites. 
- **Ion-exchange membranes** – Fixed charged groups attract and retain ionic PFAS; membranes act like immobilized ion-exchange resins. 
- **Adsorptive/affinity membranes** – PFAS sorb into/onto the membrane material (e.g., hydrophobic, fluorous, or electrostatic interactions). 
→ **Function**: PFAS are **captured and concentrated in the membrane phase** until regeneration/disposal; retention is not destruction.

**E. Membrane bioreactors (MBRs) and coupled biological systems (indirect, usually still separation)** 
- **Conventional MBRs (UF/MF membranes with a bioreactor)** – Biological processes may transform some co-contaminants, but current evidence indicates most PFAS (especially perfluoroalkyl acids) pass through unchanged; membranes mainly retain solids and biomass (separation). 
→ **Function**: The membrane part is **separation**; meaningful PFAS destruction is not reliably achieved with typical municipal/industrial MBR biology.

**F. Reactive or catalytic membranes (aimed at transformation/destruction, generally emerging)** 
These are membrane systems explicitly designed to chemically modify PFAS while providing separation. Examples include: 
- **Photocatalytic membranes** – Membranes incorporating photocatalysts (e.g., metal oxides) irradiated with UV/visible light; intended to oxidize or reductively defluorinate PFAS while they are retained at/within the membrane. 
- **Electrochemical/reactive membranes** – Conductive or catalytic membranes used as electrodes or supports for in situ electrooxidation/reduction, aiming to oxidize or reductively transform PFAS. 
- **Membranes coupled to advanced oxidation/reduction (AOPs/ARPs) inside the membrane module** – For example, membranes that deliver oxidants, radicals, hydrated electrons, or plasma-generated species in or near the membrane pores. 

→ **Function**: These systems attempt **PFAS transformation or destruction** (e.g., partial or full defluorination, chain shortening). In practice: 
- They often **still rely on a separation step** (enrich PFAS at the membrane surface or in a small volume) followed by **in situ chemical transformation**. 
- The membrane by itself is not destructive; it is the embedded or coupled reactive process that performs transformation.

**G. Hybrid “concentrate + destruction” trains (separation first, then destruction)** 
Though not a single membrane unit, many practical routes use membranes as **front-end concentrators** and then apply a separate destructive technology: 
- RO/NF/FO/MD/ED used to concentrate PFAS into a small waste stream. 
- The concentrate then treated with non-membrane destruction methods (e.g., high-energy oxidation, reduction, plasma, supercritical water, thermal, etc.). 

→ **Function**: In these trains, the membrane step is **purely separation and concentration**; destruction is downstream.

**Summary classification**

- **Routes that primarily SEPARATE/CONCENTRATE PFAS (not destroy/transform):** 
 - Reverse osmosis (RO) 
 - Nanofiltration (NF) 
 - Ultrafiltration (UF) and microfiltration (MF) (for particulate/colloid-associated PFAS) 
 - Forward osmosis (FO) 
 - Membrane distillation (MD) 
 - Electrodialysis and related electromembrane processes 
 - Ion-exchange membranes 
 - Adsorptive/affinity membranes 
 - Membrane bioreactors (membrane role only) 
 - Any membrane-only step in a hybrid train prior to a separate destruction process 

- **Routes that can DESTROY/TRANSFORM PFAS (beyond separation):** 
 - Photocatalytic membranes 
 - Electrochemical/reactive membranes 
 - Membranes integrated with in situ advanced oxidation/reduction or plasma processes 

3. Uncertainty and limitations 

- I cannot provide technology-specific performance data, reaction pathways, or quantitative mineralization/defluorination extents for any of these routes without literature. 
- Many “reactive membrane” systems are still at lab/pilot scale; their real-world PFAS destruction levels, energy demands, and byproduct profiles are not well constrained here. 
- For biologically coupled membranes (MBRs), the degree of PFAS biotransformation is compound- and condition-specific and often minimal for perfluoroalkyl acids; detailed behavior cannot be quantified here.

4. Practical takeaway 

Most established membrane-based PFAS treatments (RO, NF, FO, MD, ED, ion-exchange/adsorptive membranes, and MBR membranes) are **separation/concentration steps**, producing a PFAS-rich stream or phase that still requires **downstream destruction**; only **reactive or catalytic membrane systems** (photocatalytic, electrochemical, AOP-integrated) are designed to actually **transform or destroy PFAS**, and these remain emerging rather than standard practice.

### Human label

- Adequate (`yes` / `no` / `uncertain`):
- Material scientific error (`yes` / `no` / `uncertain`):
- Confidence (`high` / `medium` / `low`):
- Notes:

---

## D13-A020

**Question ID:** `WF10_021`

**Question:** When screening activated-carbon or biochar PFAS adsorption studies, what matrix and regeneration gaps should be checked?

**Must include:** Use limitation, uncertainty, caveat, and negative evidence to avoid overclaiming beyond the reported study scope.

**Must not claim:** Do not convert a condition-specific finding into a universal PFAS treatment claim.

### Reference evidence

**WF10_021_MMG001**

> How - ever, the extent of this impact varies depending on the type and concentration of OM, with some studies indicating min- imal interference at environmentally relevant OM concen - trations, while others report substantial reductions in PFAS sorption, highlighting the need for further research on opti - mizing biochar performance under diverse water matrices.

**WF10_021_MMG002**

> However, biochar regeneration faces sig- nificant challenges as this simply has not been attempted frequently enough in the past to draw definitive conclusions on efficacy.

**WF10_021_MMG003**

> Sustainable regeneration and reusability of biochar Bio- char regeneration is crucial for reducing costs, but each regeneration cycle alters its characteristics, such as surface morphology, functionalities, and porosity, necessitating thorough investigation.

### Anonymous candidate answer

1. Answerability 
answerable – This can be addressed from general adsorption and PFAS behavior principles without specific literature.

---

2. Answer 

Below is a screening checklist focused on *gaps* in matrix coverage and regeneration that commonly limit how transferable PFAS adsorption results are.

### A. Matrix-related gaps to check

When you review a study, ask whether the tested matrix realistically brackets the intended application(s), and flag gaps where it does not.

**1. Type and complexity of water matrix**

Check whether the study is limited to:
- Ultrapure / DI water only 
- Simple electrolyte solutions (e.g., NaCl, buffer) 
- Or includes realistic matrices such as:
 - Groundwater
 - Surface water
 - Drinking water (treated)
 - Municipal wastewater (secondary/tertiary effluent)
 - Industrial wastewater
 - Landfill leachate
 - AFFF-impacted waters

**Gap to flag:** Adsorption studied only in DI or very simple matrices when your target is complex waters (wastewater, leachate, AFFF, etc.).

---

**2. Natural organic matter / DOC**

Identify whether the study reports:
- DOC (or TOC) level 
- Source/composition of organic matter (e.g., humic/fulvic, wastewater-derived) 
- Systematic evaluation of PFAS adsorption with increasing DOC

**Gaps to flag:**
- No DOC or organic matter present or quantified 
- No competitive adsorption assessment from natural organic matter, despite real waters expected to have significant DOC.

---

**3. Background ions and ionic strength**

Look for:
- Major cations/anions present (Ca²⁺, Mg²⁺, Na⁺, K⁺, Cl⁻, SO₄²⁻, HCO₃⁻, etc.) 
- Ionic strength range tested 
- Specific assessment of electrostatic screening or salting-out effects on PFAS uptake

**Gaps to flag:**
- Only very low ionic strength systems 
- No exploration of divalent cation effects where groundwater or hard water applications are claimed.

---

**4. pH conditions**

Check:
- pH range tested and control method 
- Any sensitivity analysis (e.g., pH 5–9) relevant to environmental waters

**Gaps to flag:**
- Single pH (often neutral) with no justification 
- No evaluation of pH dependence when the material has pH-sensitive surface groups (e.g., biochar with oxygenated functional groups) or when application environments vary in pH.

---

**5. Co-contaminants and competitive sorbates**

Check whether the study includes:
- Inorganic co-contaminants (e.g., phosphate, nitrate, sulfate, metals) 
- Organic co-contaminants (e.g., non-fluorinated surfactants, petroleum hydrocarbons, chlorinated solvents, bulk organics) 
- Surfactants and AFFF components, if the application is fire-fighting foam-impacted water

**Gaps to flag:**
- Single-solute PFAS tests with no co-contaminants, yet broad performance claims for real wastewaters or AFFF sites. 
- No examination of competitive adsorption from common organics in the relevant matrix.

---

**6. PFAS mixture composition vs real-world profiles**

Verify whether:
- Only 1–2 model PFAS are tested, often long-chain (e.g., PFOS, PFOA) 
- Short-chain, ultrashort-chain, branched isomers, and precursors are included when those are expected in your target matrix 
- Concentrations tested are environmentally relevant versus orders-of-magnitude higher

**Gaps to flag:**
- Adsorption evaluated only for a few long-chain PFAS, but conclusions generalized to all PFAS. 
- No data on short-chain PFAS where these dominate regulatory concern or influent composition.

---

**7. Hydrodynamic conditions and configuration**

Note:
- Batch vs column (fixed-bed) tests 
- Empty bed contact time (EBCT) / hydraulic loading in column studies 
- Particle size and mixing/flow conditions

**Gaps to flag:**
- Only batch equilibrium tests used to predict full-scale column performance 
- No realistic EBCT or breakthrough curve data when the study implies treatment-system design.

---

### B. Regeneration-related gaps to check

Focus on whether regeneration is realistic, repeatable, and preserves performance while managing PFAS-laden regenerant responsibly.

**1. Number of regeneration cycles and performance tracking**

Check:
- How many adsorption–regeneration cycles are tested 
- Whether capacity and kinetics are quantified per cycle (e.g., breakthrough curves, isotherms)

**Gaps to flag:**
- Only a single regeneration cycle 
- Performance reported as “regenerable” without quantitative tracking of capacity loss over multiple cycles.

---

**2. Regeneration method realism**

Identify:
- Method used (thermal, solvent, alkaline, acid, surfactant, advanced oxidation, etc.) 
- Whether the conditions are technically and economically plausible at scale (e.g., very high temperatures, exotic solvents, extreme pH)

**Gaps to flag:**
- Regeneration conditions that would be impractical, unsafe, or prohibitively costly in real treatment systems 
- No discussion of energy inputs or chemical demand.

---

**3. Desorption completeness and mass balance**

Check:
- Quantification of PFAS in solid vs liquid before and after regeneration 
- Mass balance closure (PFAS remaining on adsorbent + PFAS in regenerant ≈ initial PFAS adsorbed)

**Gaps to flag:**
- Desorption efficiency not quantified, or only inferred qualitatively 
- No mass balance; unclear whether “regeneration” is partial or simply surface rinsing.

---

**4. Fate and management of the regenerant**

Look for:
- Characterization of PFAS concentration in the regenerant stream 
- Any follow-up treatment or destruction step for the recovered PFAS 
- A clear distinction between PFAS transfer (from solid to liquid) and PFAS destruction/defluorination

**Gaps to flag:**
- No plan or evaluation for managing PFAS-rich regenerant, implying unresolved secondary-waste issues 
- Language suggesting “treatment” when the process only accomplishes transfer, not destruction.

---

**5. Change in adsorbent properties after regeneration**

Check whether:
- Surface area, pore size distribution, and surface chemistry are measured pre- and post-regeneration 
- Structural damage, pore collapse, or ash/functional-group changes are assessed (especially for biochars and high-temperature regeneration)

**Gaps to flag:**
- No material characterization after regeneration 
- Declines in performance reported with no investigation of structural or chemical changes.

---

**6. Selectivity shifts across PFAS classes**

See if:
- Regeneration studies report PFAS-specific behavior (e.g., long-chain vs short-chain, sulfonates vs carboxylates) over cycles 
- Preferential desorption or retention of certain PFAS is addressed

**Gaps to flag:**
- Only total PFAS or a single target tracked across cycles 
- Potential accumulation of poorly desorbing species on the adsorbent not evaluated.

---

**7. Matrix effects during regeneration**

Evaluate:
- Whether regeneration is tested in realistic matrices or only in clean solvents/solutions 
- Impacts of co-contaminants, scaling, or fouling on regeneration efficiency

**Gaps to flag:**
- Regeneration tested only with clean eluent after exposure to simple PFAS solutions, while real use would involve fouled media and complex influents. 

---

3. Uncertainty and limitations 

- Without specific studies, this checklist cannot identify which gaps are most common numerically; it only outlines what should be checked. 
- Some gaps may be acceptable depending on the study’s stated scope (e.g., fundamental mechanistic work vs application-ready performance data).

---

4. Practical takeaway 

When screening activated-carbon or biochar PFAS adsorption papers for applicability, prioritize identifying (1) unrealistic or oversimplified matrices relative to your target water and PFAS profile, and (2) regeneration studies that do not quantify multi-cycle performance, desorption completeness, material changes, or downstream management of PFAS-laden regenerant.

### Human label

- Adequate (`yes` / `no` / `uncertain`):
- Material scientific error (`yes` / `no` / `uncertain`):
- Confidence (`high` / `medium` / `low`):
- Notes:

---

## D13-A021

**Question ID:** `WF10_030`

**Question:** Under what conditions might supercritical water oxidation leave uncertainty about fluorinated products?

**Must include:** Use limitation, uncertainty, caveat, and negative evidence to avoid overclaiming beyond the reported study scope.

**Must not claim:** Do not convert a condition-specific finding into a universal PFAS treatment claim.

### Reference evidence

**WF10_030_MMG001**

> Trifluoroacetic acid (TFA) was found to be the most recalcitrant intermediate product in the effluent, persisting at T = 600 ◦ C and residence time of ~ 32 s, emphasizing the need for TFA monitoring in SCWO treatment of PFAS-impacted matrices.

**WF10_030_MMG002**

> However, a low fluorine mass balance at temperatures of 425 and 450 ◦ C may indicate the ex - istence of fluorinated species in the gaseous and/or liquid product which are not detected by targeted analysis.

**WF10_030_MMG003**

> However, SCWO experimental studies on identifying PFAS degradation intermediates are still incomplete.

### Anonymous candidate answer

1. Answerability 
answerable – General principles of supercritical water oxidation (SCWO) and fluorinated-organic chemistry are sufficient to specify when uncertainty about fluorinated products is likely, even without specific experimental datasets.

2. Answer 
Uncertainty about what fluorinated products are formed or remain after SCWO is most likely under conditions where degradation and product speciation are not driven to completion or not well constrained analytically. Key conditions include:

- **Suboptimal reaction severity (temperature, pressure, residence time)** 
 - **Temperatures near the lower end of “supercritical” (just above 374 °C)** or with only modest excess oxidant can favor **partial oxidation** of fluorinated organics rather than full mineralization to HF/fluoride and CO₂. 
 - **Short residence times** or insufficient mixing (poor contact between oxidant and organics) increase the chance that **partially oxidized fluorinated intermediates** (e.g., shorter-chain perfluoroalkyls, fluorinated carboxylates, or other F‑containing fragments) persist but are not fully characterized. 
 - Operation chosen for energy efficiency rather than complete destruction (e.g., milder conditions to reduce corrosion or fuel use) can intentionally trade off certainty in complete mineralization.

- **High organic load or complex matrices** 
 - **High TOC or co-contaminants** (oils, surfactants, polymers) can create **competition for oxidant** and alter radical chemistry, making fluorinated compound pathways less predictable. 
 - **Matrices rich in radical scavengers** (e.g., certain organics, salts, ammonia) can suppress radical-driven steps necessary to break strong C–F bonds, favoring a spectrum of intermediate fluorinated products. 
 - **Heterogeneous feed** (sludges, biosolids) can cause local zones with different temperature/oxidant availability, so some portions see harsher conditions than others, complicating product distribution.

- **Salt formation, phase behavior, and mass transfer limitations** 
 - At supercritical conditions, water becomes more nonpolar; **salt precipitation (e.g., NaF, CaF₂, carbonates, sulfates)** can create solids that: 
 - change local hydrodynamics and mixing, 
 - occlude organics or HF near solid surfaces, 
 - or sequester fluoride into **poorly characterized solid phases**. 
 - In multiphase regimes (e.g., organic-rich droplets, gas bubbles, or salt slurries), mass transfer limits can mean some fluorinated species are **shielded from the oxidant**, leading to partial degradation and unknown product spectra in those microenvironments.

- **Non-ideal oxidant dosing or distribution** 
 - **Under-dosing oxidant** (stoichiometric or slight excess relative to total organic load) can push the system into a regime where the **oxidation stops at intermediate fluorinated products**. 
 - Poor oxidant injection design or inadequate turbulence may cause **zones of oxidant depletion**, again promoting incomplete defluorination.

- **Corrosion and materials constraints on operating window** 
 - To limit corrosion from **HF and hot, oxidizing conditions**, operators may need to: 
 - cap maximum temperature, 
 - restrict residence time, 
 - or limit oxidant excess. 
 - These pragmatic constraints can prevent reaching the severity needed for complete C–F bond destruction, increasing uncertainty about persistent fluorinated intermediates and solid fluoride phases.

- **Incomplete chemical speciation and analytical coverage** 
 Even if the process conditions are severe, **uncertainty in products can persist purely from measurement limits**, especially under these circumstances: 
 - **Limited target lists** (e.g., measuring only a few perfluoroalkyl acids and inorganic fluoride) leave many possible fluorinated intermediates (short-chain acids, unsaturated fluorocarbons, perfluoroethers, oligomers) unmeasured. 
 - Relying on **total organic carbon (TOC) decrease or COD removal** without fluorine-specific analysis (e.g., total organofluorine, fluoride, non-targeted mass spectrometry) cannot rule out low-level or novel fluorinated products. 
 - **High ionic strength, suspended solids, or HF/salt matrices** can interfere with extraction and detection, especially for: 
 - very polar or inorganic F species, 
 - volatile fluorinated compounds (which may partition to gas), 
 - or particle-bound F species. 
 - Incomplete closure of a **fluorine mass balance** (e.g., not accounting for gas phase, aqueous, and solids simultaneously) leaves ambiguity about where the fluorine ended up and in what form.

- **Formation or loss of volatile fluorinated species** 
 - Under high temperature and supercritical conditions, some degradation pathways may form **volatile fluorinated species** (e.g., small fluorocarbons or inorganic F gases). 
 - If off-gas is not comprehensively characterized, or if gas sampling systems cause loss or transformation of reactive fluorinated gases, **there is residual uncertainty** about gaseous fluorinated products, even if aqueous fluoride appears high.

- **Dynamic or transient operation rather than steady state** 
 - During **startup, shutdown, or load changes**, temperature and oxidant concentration vary, and the system may pass through regimes where intermediates are formed but not fully destroyed. 
 - Without time-resolved sampling that spans these transients, there can be uncertainty about what fluorinated species were present or emitted during those periods.

3. Uncertainty and limitations 
- Without experimental data, it is not possible to specify which particular intermediates form under given SCWO conditions, only that certain operating regimes are more conducive to partial oxidation or incomplete defluorination. 
- Different fluorinated chemistries (e.g., perfluoroalkyl acids, fluorotelomers, perfluoroethers, side-chain fluorinated polymers) may behave differently; the conditions above increase uncertainty in general but do not predict outcomes for each structure. 
- Real systems may combine several complicating factors simultaneously (e.g., high salt, complex organics, corrosion limits), making product distributions more complex than any single-factor reasoning suggests.

4. Practical takeaway 
Uncertainty about fluorinated products from SCWO is most likely when the process is run at marginal severity, with complex or salty feeds, constrained by corrosion, and/or characterized with incomplete fluorine-speciation analytics; reducing this uncertainty requires both more aggressive and well-controlled operating conditions and comprehensive, phase-resolved fluorine mass balance measurements.

### Human label

- Adequate (`yes` / `no` / `uncertain`):
- Material scientific error (`yes` / `no` / `uncertain`):
- Confidence (`high` / `medium` / `low`):
- Notes:

---

## D13-A022

**Question ID:** `WF10_002`

**Question:** When comparing membrane filtration, gliding arc plasma, and supercritical water oxidation for PFAS treatment, which reported endpoints should be kept separate?

**Must include:** Keep removal, separation, adsorption, degradation, defluorination, mineralization, destruction, byproduct formation, and mass-balance evidence separate.

**Must not claim:** Do not convert a condition-specific finding into a universal PFAS treatment claim.

### Reference evidence

**WF10_002_L3X001**

> Among different approaches, high-pressure membrane filtration pro - cesses that utilize nanoporous membranes like nanofiltration (NF) and reverse osmosis (RO) have proven to be highly effective in separating both short- and long-chain PFAS compounds with rejection efficiencies typically exceeding 90 % [ 24 , 25 ].

**WF10_002_L3X002**

> Membrane‑assisted chemical degradation Generally, the abovementioned treatment methods (filtra- tion, adsorption, and membrane distillation) can only con- centrate PFAS.

**WF10_002_L3X003**

> However, a low fluorine mass balance at temperatures of 425 and 450 ◦ C may indicate the ex - istence of fluorinated species in the gaseous and/or liquid product which are not detected by targeted analysis.

**WF10_002_MMG001**

> Results and discussion To demonstrate that the engineered GAP system is an effec- tive treatment system for PFAS contaminated water the disap- pearance of the target analyte Ĳs), formation of degradation products, defluorination, and energy costs were measured and calculated.

**WF10_002_MMG002**

> Non-plasma-based PFAS treatment technolo- gies where high temperature make an important contribution to PFAS degradation, such as sonolysis [23,27] and supercritical water oxidation (SCWO) [6], have shown excellent potential in mineralizing PFAS with minimal short-chain PFAS formation, and increased mineralization with a rise in reaction temperatures has been observed in SCWO [ 6,28].

### Anonymous candidate answer

1. Answerability 
general_framework_only – The question is about how to conceptually separate endpoints when comparing technologies, which can be answered from general principles but not with technology‑specific study data.

2. Answer 
When comparing membrane filtration, gliding arc plasma, and supercritical water oxidation (SCWO) for PFAS treatment, you should keep the following endpoint types clearly separated and not treat them as equivalent:

**A. Phase separation vs chemical transformation**

- **Membrane filtration**
 - *Separation endpoints* 
 - Percent reduction of PFAS concentration in the *permeate* 
 - PFAS rejection rate (retentate vs feed) 
 - Mass balance of PFAS between feed, permeate, and concentrate 
 - These describe **physical separation / concentration**, not destruction.

- **Gliding arc plasma and SCWO**
 - *Transformation endpoints* 
 - Percent decrease of parent PFAS in the treated bulk phase 
 - Degradation rate constants or half‑lives 
 - These are **chemical transformation / destruction** endpoints.

**Keep separate:** 
- “Permeate removal” (membrane) vs “bulk degradation/destruction” (plasma, SCWO). 
- “PFAS in concentrate/retentate” (membrane) vs “PFAS mineralized/defluorinated” (plasma, SCWO).

---

**B. Parent compound removal vs total PFAS metrics**

Across all three technologies, distinguish:

- **Parent PFAS concentration**
 - E.g., reduction in a specific compound (e.g., a single sulfonate or carboxylate).
- **Sum of targeted PFAS**
 - Sum of a defined list of analytes.
- **Broader indices**
 - Total organic fluorine (TOF) or extractable organic fluorine (EOF) 
 - Total oxidizable precursor (TOP) assay response 
 - Total organic carbon (TOC).

**Keep separate:** 
- “Removal of a specific parent PFAS” vs “change in summed PFAS” vs “change in TOF/EOF/TOP or TOC.” 
- Membrane: often good for *parent PFAS in permeate* but no destruction; 
- Plasma/SCWO: may reduce TOF/TOC along with parent PFAS.

---

**C. Destruction vs defluorination vs mineralization (plasma and SCWO)**

For plasma and SCWO specifically, do not collapse these:

- **Parent PFAS degradation** 
 - Loss of the original PFAS molecule.
- **Defluorination** 
 - Release of fluoride ion (F⁻) relative to theoretical maximum.
- **Mineralization / total oxidation** 
 - Conversion of organic carbon to CO₂ (and other inorganic species), often tracked via TOC or CO₂ production.

**Keep separate:** 
- “% parent PFAS decrease” vs “% of C converted to CO₂” vs “% of F recovered as inorganic fluoride.” 
- A technology can show high parent removal but incomplete defluorination and mineralization.

---

**D. Product and byproduct endpoints**

All three approaches can generate different “outputs” that require distinct endpoints:

- **Membrane filtration**
 - PFAS concentration and mass in:
 - Permeate 
 - Retentate/concentrate 
 - Volume reduction factor (how much waste is concentrated).

- **Gliding arc plasma**
 - Concentrations of shorter‑chain PFAS formed 
 - Inorganic fluoride produced 
 - Other organic byproducts (e.g., small acids) 
 - Off‑gas composition if relevant.

- **SCWO**
 - Inorganic fluoride production 
 - CO₂ formation / TOC removal 
 - Short‑chain PFAS or intermediates in effluent 
 - Solid residues (e.g., precipitated salts).

**Keep separate:** 
- “Removal in treated water” vs “accumulation in a waste stream (retentate, off‑gas, solids).” 
- “PFAS destroyed” vs “PFAS transformed to other organofluorines.”

---

**E. Matrix and operational endpoints vs treatment performance**

Do not conflate performance with conditions:

- **Operational/matrix endpoints**
 - Temperature, pressure, and oxidant presence (SCWO) 
 - Discharge power, gas composition (plasma) 
 - Transmembrane pressure, recovery, fouling rates (membranes) 
 - Co‑contaminant concentrations, ionic strength, pH.

- **Performance endpoints**
 - PFAS concentration changes, defluorination, TOC removal, byproducts.

**Keep separate:** 
- “Operating condition” variables vs “treatment outcome” metrics when comparing technologies.

3. Uncertainty and limitations 
- No specific experimental datasets, compound lists, or numerical thresholds can be cited here, so the distinctions are conceptual rather than tied to particular studies. 
- Actual studies may define or calculate some of these endpoints differently (e.g., different TOF methods, different PFAS target lists), which must be checked case by case when doing a quantitative comparison.

4. Practical takeaway 
When comparing membrane filtration with gliding arc plasma and SCWO for PFAS treatment, distinguish (i) physical separation vs chemical destruction, (ii) parent PFAS vs total PFAS vs total fluorine/carbon metrics, and (iii) degradation vs defluorination vs mineralization and byproduct formation, and do not aggregate these differing endpoints into a single “removal” measure.

### Human label

- Adequate (`yes` / `no` / `uncertain`):
- Material scientific error (`yes` / `no` / `uncertain`):
- Confidence (`high` / `medium` / `low`):
- Notes:

---

## D13-A023

**Question ID:** `WF10_036`

**Question:** Does longer empty-bed contact time necessarily translate into better PFAS performance in granular activated carbon systems?

**Must include:** Use limitation, uncertainty, caveat, and negative evidence to avoid overclaiming beyond the reported study scope.

**Must not claim:** Do not convert a condition-specific finding into a universal PFAS treatment claim.

### Reference evidence

**WF10_036_MMG001**

> 5 B), which means that the apparent adsorption capacity did not change as EBCT increased.

**WF10_036_MMG002**

> Table S8 shows that the ratios for the Lead + Lag to Lead column for q ΣPFAS were only slightly different from unity (1.07 ± 0.12), implying that adsorption mechanisms are inde- pendent of EBCT.

**WF10_036_MMG003**

> This indicates that longer EBCTs do not suffer from competing adsorbates (e.g., ionic species, DOC), and the similar breakthrough curve shapes suggest shorter EBCTs (i.e., ~2 –5 min) capture the mass transfer zone.

**WF10_036_MMG004**

> Although break- through curves for individual PFAAs did not perfectly overlap at the two EBCTs, consistent trends suggesting that either shorter or longer EBCTs resulted in lower CURs were not observed.

### Anonymous candidate answer

1. Answerability 
answerable – This is a conceptual design/interpretation question that can be addressed from general adsorption and reactor principles without specific literature.

2. Answer 
No. Longer empty-bed contact time (EBCT) does not *necessarily* translate into better PFAS performance in granular activated carbon (GAC) systems, although it often helps under typical design conditions.

Key points:

- **What EBCT actually controls** 
 EBCT is a hydraulic parameter (bed volume / flow rate). Increasing EBCT:
 - Lowers superficial velocity.
 - Increases water residence time in the bed.
 - Improves mass transfer opportunity for PFAS to reach and load GAC particles. 
 Under many realistic conditions (non‑equilibrium, mass‑transfer limited), this tends to:
 - Delay breakthrough (higher treated volume before effluent concentration rises).
 - Improve short‑term PFAS removal.

- **When longer EBCT improves performance**
 Longer EBCT is beneficial when:
 - **Mass transfer is limiting** (e.g., short beds, high flow velocities, small contact times, or poorly wetted media).
 - **PFAS have not reached near‑equilibrium adsorption** at the current EBCT.
 - **Co‑contaminants** compete for sites and slower flow allows somewhat better selective loading of PFAS.
 In this regime, increasing EBCT usually:
 - Decreases effluent PFAS concentration at a given bed life, and/or
 - Increases bed life (more bed volumes treated before PFAS breakthrough).

- **When longer EBCT does *not* give better PFAS performance**
 Cases where a further increase in EBCT offers little or no improvement:

 1. **System already near equilibrium** 
 If, at the existing EBCT, PFAS adsorption has essentially reached the equilibrium curve for the loaded bed, then:
 - Lengthening EBCT will not meaningfully lower effluent PFAS concentrations.
 - Performance is now controlled by **available capacity**, not contact time.

 2. **Bed capacity is exhausted (saturation / breakthrough reached)** 
 Once a substantial portion of the GAC column is saturated for a given PFAS:
 - Effluent concentration is set by the mass transfer zone’s position and equilibrium, not by additional hydraulic residence time.
 - Longer EBCT on a **spent bed** does not restore performance.

 3. **Poor GAC–PFAS affinity dominates** 
 For short‑chain PFAS or PFAS with inherently weak adsorption on the chosen GAC:
 - Adsorption capacity is low regardless of contact time.
 - Even very long EBCTs will not reach low effluent concentrations or long bed life.

 4. **Mass transfer is not the bottleneck** 
 If:
 - Particle size is already small enough,
 - Flow is sufficiently low,
 - Film and intraparticle diffusion are relatively fast, 
 then PFAS removal is capacity‑/equilibrium‑limited, and further increasing EBCT has diminishing returns.

 5. **Maldistribution or short‑circuiting** 
 If there are hydraulic problems (channeling, bypassing, gas binding):
 - Increasing nominal EBCT does not fix poor contact in underutilized regions of the bed.
 - Real (effective) EBCT experienced by much of the water may not increase.

 6. **Design objectives other than “absolute best PFAS removal”** 
 Longer EBCT:
 - Increases vessel size and capital cost.
 - Can increase overall footprint and head loss constraints. 
 In practice, “better performance” usually means “meeting a target concentration for a target run time at acceptable cost,” which is not monotonic with EBCT.

- **How to think about “optimal EBCT” for PFAS**
 In PFAS‑focused GAC design, EBCT should be chosen to:
 - Ensure **mass transfer is not the limiting factor** at the desired effluent PFAS target.
 - Recognize that **PFAS chain length and competition** (DOC, other organics, sulfate, etc.) control equilibrium capacity and breakthrough behavior.
 - Align with **regeneration or replacement frequency**, waste handling constraints, and cost.

 In practice:
 - There is often an **EBCT range** (e.g., a few to several minutes) beyond which PFAS breakthrough curves change only modestly for a given GAC, water matrix, and target compounds.
 - Beyond that range, additional EBCT mainly increases capital cost without proportional gains in PFAS control.

3. Uncertainty and limitations 
- The precise EBCT at which “diminishing returns” occur depends on:
 - Specific PFAS (chain length, functional group).
 - Water matrix (DOC, competing organics/ions).
 - GAC type, particle size, and preloading history.
 - Column configuration (single vs. lead–lag). 
- Quantitative performance predictions (e.g., breakthrough times vs. EBCT) require site‑specific data, pilot testing, or adsorption modeling; they cannot be deduced from general principles alone.

4. Practical takeaway 
Use EBCT as a design lever to remove mass‑transfer limitations but do not assume “longer is always better”; for PFAS‑targeted GAC systems, determine an optimal EBCT range through modeling or pilot testing, recognizing that beyond a certain point additional EBCT yields minimal PFAS performance gains relative to cost.

### Human label

- Adequate (`yes` / `no` / `uncertain`):
- Material scientific error (`yes` / `no` / `uncertain`):
- Confidence (`high` / `medium` / `low`):
- Notes:

---

## D13-A024

**Question ID:** `NQ15`

**Question:** How do electrolyte composition and pH-control choices affect interpretation of PFAS removal or degradation experiments?

**Must include:** Must treat buffer choice as a balance between pH control and interference risk; must connect to system or mechanism dependence.

**Must not claim:** Must not claim one exact buffer is universally correct for all PFAS removal experiments.

### Reference evidence

**NQ15_MMG001**

> If only relying on the initial pH for its effects on the degradation of PFAS, it is likely to lead to a false interpretation.

**NQ15_MMG002**

> There is no reported consensus on the effects of pH to date.

**NQ15_MMG003**

> ting  the  degradation  performance  of  PFAS  (Radjenovic et al., 2020). In  addition,  increased  electrolyte  viscosity and surface tension may decrease the electrode wettability and  thus  also  may  inhibit  the  electro-oxidative degradation of PFAS (Wu et al., 2004). Zhuo et al. (2014) compared  the  effects  of  three  electrolytes  on  the degradation of 6:2 fluorotelomer sulfonic acid (20 mg/L) on  a  Ti/SnO2-Sb2O5-Bi2O3  anode. They  found  that  its degradation  declined  along  with  the  trend  of  the electrolytes  NaClO4  >  NaCl  >  Na2SO4. Barisci et al. (2021) also showed a higher removal of PFOA and PFOS (100  μg/L)  in  NaCl  than  in  a  Na2SO4  electrolyte. Linear sweep  voltammetry  curves  showed  that  the  oxygen overpotential  on  the  Ti/RuO2  anode  was  higher  in  the NaCl electrolyte, suggesting its higher oxidation potential resulted in the increased degradation efficiency, although the  presence  of  halide  ions  may  lead  to  the  formation  of toxic byproducts (e.g., Cl2, HClO, and ClOx–) during the electrochemical  oxidation  (Azizi et al., 2011; Yang et al., 2019). This  risk  needs  to  be  mitigated,  especially  when high  electrolyte  concentration  and  high  potential  are employed  in  the  electro-oxidation  systems. Due  to  the

**NQ15_MMG004**

> Electrochemical decontamination of perfluorinated compounds 11 4.2.3    Electrolyte type The chemical components in an electrolyte can also affect the  removal  of  PFAS  through  different  influencing mechanisms in an electro-coagulation process. Yang et al. (2016)  investigated  the  removal  of  PFOS  by  a  Fe  anode with  four  different  types  of  electrolytes,  i.e.,  NaCl, Na2SO4, NaNO 3, and NaH2PO4. The results showed that the  removal  performance  follows  the  following  trend: NaCl  (99.6%)  >  Na2SO4  (93.7%)  >  NaNO3  (63.5%)  > NaH2PO4  (45.4%). Studies  have  shown  that  the immersion  of  metallic  Fe  in  water  at  open  circuit conditions would result in the generation of impenetrable passive  ferric  oxide  film  that  restricts  the  anodic dissolution  of  Fe. With  the  presence  of  Cl–,  the passivation of the Fe electrode could be delayed due to its catalytic  action  (Amani-Ghadim et al., 2011). However, high  concentrations  of  Cl–  may  lead  to  secondary pollutants  (e.g.,  Cl2  and  ClO–). Meanwhile,  the  NO3– could be adsorbed on the surfaces of the Fe anode and the Fe  hydroxide  precipitates,  which  effectively  reduce  the electrochemical  dissolution  and  polymerization  of  the

**NQ15_MMG005**

> As the conductivity of the electrolyte solution and the surface water were comparable (300 µ S/cm versus 320 µ S/cm), the composition of the cations and anions in the surface water was then considered a possible cause of the differing breakdown rates.

### Anonymous candidate answer

1. Answerability 
answerable – The chunks provide direct information on how pH and electrolyte choices influence PFAS electrochemical behavior and why this complicates interpretation.

2. Answer 

Electrolyte composition and pH-control choices can change both *what is actually happening* in a PFAS experiment and *what you think is happening* when you interpret removal, degradation, or defluorination data. Key issues:

**A. Local vs bulk pH: misinterpreting “pH effects”**

- Under the high current densities/potentials typically needed for PFAS electrooxidation, the pH in the vicinity of the anode becomes highly acidic, even when bulk pH is not strongly acidic. 
- This local acidification can protonate PFAS at the anode surface and change their adsorption, electron‑transfer pathways, and reaction rates. 
- Bulk pH measurements (or reporting only initial pH) therefore do not reflect the actual pH conditions experienced by PFAS at the reactive interface; relying only on initial pH can lead to false interpretation of “pH effects.” 
- pH also affects electrode wettability and electrical conductivity, altering apparent degradation performance independently of intrinsic reaction kinetics. 

Implication for interpretation: 
Apparent pH dependencies (e.g., “degradation is faster at pH 5 than 9”) may largely reflect changes in local interfacial pH, surface charge, and mass transfer, not simply PFAS speciation in bulk. Comparisons across studies that control only bulk pH, or that do not report current density and potential, are unreliable.

**B. Electrolyte conductivity, ohmic drop, and mass transfer**

- The supporting electrolyte provides ionic conductivity and controls the ohmic potential drop; low conductivity increases solution resistance and limits effective potential at the electrode, deteriorating PFAS degradation performance. 
- Increasing electrolyte concentration reduces ohmic loss, but can also change anode potential and thus PFAS removal; e.g., in one system 0.15 M Na₂SO₄ gave higher anode potential and better PFOA removal than 0.3 M, illustrating that conductivity and potential are jointly important. 
- In porous/3D electrodes, insufficient conductivity can limit reactivity with depth in the electrode; adding a supporting electrolyte (e.g., 100 mM NaClO₄) was required so ionic conductivity did not limit PFAS oxidation in groundwater. 
- Higher ionic strength in concentrated waste streams also alleviates ionic limitations and effectively increases the active area, improving removal and energy efficiency compared to dilute groundwater. 

Implication for interpretation: 
Differences in removal or “rate constants” between conditions or studies may be dominated by changes in solution resistance and effective electrode potential rather than intrinsic reaction kinetics. Energy‑use metrics and apparent kinetics are not directly comparable across different electrolytes or conductivities unless ohmic conditions and actual anode potentials are accounted for.

**C. Electrolyte identity: radical pathways, side reactions, and byproducts**

- Different electrolyte anions can participate in or generate distinct oxidizing species. Sulfate electrolytes can yield electrochemically produced SO₄•⁻ radicals that boost PFOA degradation, increasing removal efficiencies, enhancing reaction rates 2.3–3.4×, and reducing energy consumption relative to nitrate and perchlorate electrolytes. 
- Na₂SO₄ can improve PFOA removal and defluorination compared with NaCl, and generates fewer harmful byproducts such as perchlorate that may form in chloride media. 
- “Inert” electrolytes such as NaClO₄ are sometimes chosen specifically because they are not significantly oxidized under the applied conditions, making it easier to attribute observed PFAS transformation to direct electrooxidation and generic •OH rather than to secondary oxidants. 

Implication for interpretation: 
- A system using sulfate can show higher “degradation efficiency” partly because SO₄•⁻ is contributing; this is not equivalent to a perchlorate or nitrate system at the same apparent potential or current. 
- Different electrolytes can lead to different transformation pathways, product spectra, and defluorination extents, even if PFAS disappearance is similar. 
- Comparing “removal percentages” across electrolytes without considering radical chemistry and byproduct formation can obscure whether PFAS are being mineralized, transformed to shorter‑chain PFAS, or partially oxidized.

**D. Interdependence of pH, electrolyte, ionic strength, and PFAS concentration**

- It is very challenging to distinguish the interrelated effects of ionic strength, electrolyte type, pH, and PFAS concentration; these effects also vary from one PFAS to another. 
- PFAS dissociation (pKₐ) and aggregation depend strongly on experimental conditions (cosolvents, micelles, interfaces), complicating predictions of speciation and charge at given bulk pH. 
- Water‑matrix constituents such as Ca²⁺, Mg²⁺ and dissolved organics can further influence electrochemical oxidation of PFAS, but data remain sparse; overall there is limited mechanistic information on interfering species and product formation beyond empirical observations. 

Implication for interpretation: 
Reported pH and electrolyte “trends” at mg/L model concentrations may not extrapolate to ng–µg/L environmental concentrations, or among different PFAS subclasses. Observed performance can be a composite of changes in PFAS speciation, aggregation, adsorption, interfacial pH, and radical chemistry, rather than a single “pH effect” or “electrolyte effect.”

**E. Practical interpretation pitfalls**

When evaluating or designing PFAS experiments:

- **Do not equate removal with degradation or mineralization.** 
 Different electrolytes and pH conditions affect adsorption to the electrode, micelle formation, and foam generation, which can cause apparent concentration reductions without corresponding defluorination or mineralization.

- **Be cautious with energy‑performance metrics.** 
 Metrics such as E_EO per log removal depend strongly on conductivity, ohmic drop, and electrolyte identity. Comparisons across different electrolytes, pH, and matrices may largely reflect differing solution resistances and radical pathways rather than intrinsic electrode activity.

- **Consider environmentally relevant conditions.** 
 High electrolyte concentrations and idealized matrices are often used to maximize removal and simplify mechanistic studies, but these conditions may mask mass‑transfer limitations, competitive reactions, and byproduct issues that will be present in real waters. Interpretation for field relevance requires explicit discussion of these differences.

3. Uncertainty and limitations 

- Most evidence is from electrochemical oxidation of PFOA and a subset of PFAS; behavior of other classes (short‑chain, fluorotelomers, zwitterionic PFAS) under different pH/electrolyte conditions can differ. 
- Quantitative relationships (e.g., exact dependence of rate constants on ionic strength or local pH) are not well constrained and are highly system‑specific. 
- Effects of common groundwater constituents (e.g., Ca²⁺, Mg²⁺, NOM) on electrolyte‑ and pH‑dependent behavior are still poorly characterized. 

4. Practical takeaway 

For credible interpretation of PFAS removal or degradation experiments, electrolyte type and concentration, bulk and interfacial pH, and matrix composition must be treated as central experimental variables—reported clearly, controlled or monitored (especially local pH and conductivity), and explicitly considered when attributing observed PFAS loss to specific mechanisms or when comparing across studies.

### Human label

- Adequate (`yes` / `no` / `uncertain`):
- Material scientific error (`yes` / `no` / `uncertain`):
- Confidence (`high` / `medium` / `low`):
- Notes:

---

## D13-A025

**Question ID:** `WF10_025`

**Question:** How should contact time be planned when powder activated carbon is used for both short- and long-chain PFAS?

**Must include:** Identify the relevant protocol steps, reagents/materials, operating conditions, matrix, target compounds, and reported limitations.

**Must not claim:** Do not convert a condition-specific finding into a universal PFAS treatment claim.

### Reference evidence

**WF10_025_MMG001**

> acids (PFCAs) and three perﬂuoroalkyl sulfonic acids (PFSAs), were tested to ﬁnd their adsorption selectivity from surface water and the feasibility of the powder activated carbon (PAC) process between the perchlorination and coagulation processes by operating parameters such as mixing intensity, dosage, contact time, initial pH, and concentration of perchlorination. The removal eﬃciency of four types of PAC revealed that the coal-based activated carbon was clearly advanced for all of the PFASs, and the thermal regenerated PAC did not exhibit a signiﬁcant reduction in adsorption capacity. The longer carbon chain or the higher molecular weight (MW) obtained a higher adsorption capacity and the MW exhibited a more proportional relationship with the removal eﬃciency than the carbon chain number, regardless of the PFCA and PFSA species. Approximately 80% and 90% equilibria were accomplished within 60 and 120 min for the long chain carbon PFAS, respectively, while for the short chain PFAS, 240 min was required to reach 85% equilibrium. The eﬀect of mixing intensity (rpm) was not considered for the removal of the PFAS, although it was relatively inﬂuenced in the short PFAS species. Due to the surface charge of the PAC and the properties of protonation of the PFASs, the acid condition increased the PFASs’ adsorption capacity. The prechlorination decreased

### Anonymous candidate answer

1. Answerability 
answerable – The supplied studies give quantitative PAC contact-time data for mixed short- and long‑chain PFAS, enough to outline planning principles.

2. Answer 
- In mixed PFAS, long‑chain compounds adsorb faster and more strongly than short‑chain ones, so contact time should be set by the slowest/least sorbing short‑chain target. 
- In Son et al.’s PAC study (real surface water, 9 PFAS, 10 mg/L PAC), about 70% of total PFAS removal occurred within 30 min for all species. Long‑chain PFAS reached ~80% and ~90% of equilibrium by 60 and 120 min, respectively, while short‑chain PFAS required ~240 min to reach ~85% of equilibrium. Overall “constant” removal (practical equilibrium) was observed at ~240 min. 
- They also showed that regulatory levels for long‑chain PFAS (e.g., PFOA/PFOS) were easily met with 30 mg/L PAC and only 30 min contact time, but short‑chain PFAS required higher PAC doses and benefitted more from increased contact time. 
- Reviews and broader assessments confirm that: 
 - PAC (and other carbons) generally underperform for short‑chain PFAS even at elevated doses and extended contact times, 
 - Increasing both PAC dose and contact time improves removal, with long‑chain PFAS always easier to remove. 

Practical planning implications for PAC contact time when both short- and long-chain PFAS matter: 
- **Base CT on short‑chain performance, not long‑chain.** A CT that is sufficient for long‑chain PFAS (e.g., 15–30 min) will typically not bring short‑chain species anywhere near equilibrium or high removal. 
- **Expect at least several hours for near‑equilibrium short‑chain removal in batch/mix contactors.** Lab data suggest ~4 h is a reasonable starting design value to approach ~80–85% of short‑chain equilibrium removal, while long‑chain PFAS are already near equilibrium within 1–2 h under the same conditions. 
- **Use CT–dose tradeoffs.** If hydraulic constraints limit CT (e.g., <1 h), higher PAC doses can still achieve good long‑chain removal but are likely to yield modest and variable short‑chain removal; short‑chain control at low CT should be treated as uncertain and site‑specific. 
- **Pilot under realistic conditions.** Because competition by NOM and co‑contaminants can slow and suppress PFAS adsorption, CT should ultimately be set based on pilot tests in the actual water, targeting the “worst” PFAS (shortest chain / lowest affinity) at the required effluent goal. 
- **Design margin.** For full‑scale planning, select a CT that: 
 - Achieves target removal for the slowest short‑chain PFAS in pilot tests, and 
 - Includes safety margin for seasonal NOM changes and PAC property variability (e.g., 1.5–2× the pilot‑determined minimum CT). 

3. Uncertainty and limitations 
- Kinetic data are from specific waters, PAC types, and doses; absolute CT values will shift with PAC properties, mixing, competing organics, and influent PFAS levels. 
- There is no universal CT that guarantees a given removal for all short‑chain PFAS; behavior varies markedly across compounds (e.g., PFBA vs PFHxS vs PFBS) and matrices. 
- Most available data are batch or semi‑batch; translation to continuous flow systems (e.g., contact basins with feed/withdrawal) needs pilot confirmation.

4. Practical takeaway 
Plan PAC contact time based on the slowest‑adsorbing short‑chain PFAS, using pilot tests in site water; as an initial expectation, long‑chain PFAS can be well controlled at ≤1–2 h, but achieving strong short‑chain removal generally requires substantially longer CT (on the order of hours) or accepting lower short‑chain performance or higher PAC doses.

### Human label

- Adequate (`yes` / `no` / `uncertain`):
- Material scientific error (`yes` / `no` / `uncertain`):
- Confidence (`high` / `medium` / `low`):
- Notes:

---

## D13-A026

**Question ID:** `NQ10`

**Question:** How are PFAS samples preconcentrated before mass spectrometry, and how do protocols vary by matrix, analyte, or method?

**Must include:** Must connect SPE selection to matrix and analyte scope; must mention recovery or chemistry-dependent suitability when supported.

**Must not claim:** Must not claim one exact SPE cartridge and elution protocol is universally correct for all PFAS environmental samples.

### Reference evidence

**NQ10_MMG001**

> Conclusion An eﬃcient and convenient SPME method was developed for PFAS in aqueous matrices and applied to river, lake, tap and bottled water samples.

**NQ10_MMG002**

> 3 ng L − 1 ∗∗ 40 – 160 ng L − 1 ∗∗∗∗ [39] Drinking water (EPA method 8327) Dilute and Shoot N/A 24 PFAS compounds

**NQ10_MMG003**

> So far, to detect parts-per-trillion level PFAS, pre-concentration has been accomplished by either solid phase extraction (SPE) or liquid-liquid extraction (LLE) [ 9 , 34 , 40 ].

**NQ10_MMG004**

> Obtained results showed that, with 150 mg cartridges, recoveries clearly decreased when the sample volume was increased from 10 to 100 mL.

**NQ10_MMG005**

> (C8–C14), with values above 61% for all of them and close to 100% in the case of PFOS or PFNA.

**NQ10_MMG006**

> Eluted methanolic sample extracts of 0.5 mL resulted in an effective 500-fold concentration of target analytes from the initial sampling.

**NQ10_MMG007**

> for analysis [67–70]. However, SBSE coupled with GC-MS is yet to be developed. This study aimed to develop and validate a simple, sensitive, and efficient method by integrating green chemistry-based stir bar sorptive extraction (SBSE) with thermal desorption–gas chromatography–mass spectrometry (TD-GC-MS) specifically for the anal- ysis of perfluorocarboxylic acids (PFCAs), a significant subgroup of PFAS. The novelty of this research lies in its solvent-free approach, which reduces environmental impact and costs while enhancing the sensitivity and accuracy of PFCA detection by minimizing potential contamination and analyte loss. Unlike traditional methods such as LC-MS/MS, which often require complex, labor-intensive, and costly procedures, our SBSE-TD-GC-MS method offers a more efficient, cost-effective, and environmentally friendly alternative. This method was applied to analyze water samples from various sources, including tap water and influents and effluents from local municipal wastewater treatment facilities. To the best of our knowledge, this is the first study to combine SBSE with TD-GC-M for PFCA extraction followed by solvent-free desorption using a thermal desorption unit prior to GC-MS analysis. These aspects not only fill a significant gap in the existing literature but

**NQ10_MMG008**

> 23 Briefly, the diluted samples were mixed with aqueous ammonium hydroxide solution, isopropyl alcohol, trifluoroethanol, water, internal standards, and methanol before being injected into a SCIEX ExionLC high- pressure liquid chromatography (HPLC) system.

**NQ10_MMG009**

> (at LOQ). to methods that require very fast sample processing such as dilute and shoot, our method provides higher preconcentration and limits occurrence of matrix effects. To investigate the applicability of the developed SPME protocol to environmental samples, lake, river, tap and bottled water were analyzed and their matrix effects evaluated. Results shown in Fig. S14 , reveal that none of the model PFAS were detected in the an- alyzed matrices. The occurrence of matrix effects was also evalu- ated by testing, for each matrix collected, the accuracy of samples spiked at concentration levels of 15, 50 and 250 ng L − 1 , using the calibration curve equation obtained from the ultra-pure water calibration. As demonstrated in Table S4 , all points fall within the established line of best ﬁt for the calibration performed in ultra- pure water, accuracy being between 70 and 130% for all the spiked samples and RSD being less than 10% for most analytes. PFOA and PFOS had accuracy values lower or higher than the acceptable lim- its for some water samples. For PFOA, values at 15 ng L − 1 for bottled, lake and tap water while at 50 ng L − 1 for bottled, lake and river water samples and that of PFOS was lake water at 15 ng L − 1 .

**NQ10_MMG010**

> Furthermore, substantial matrix effects can occur from the samples during analysis, mak- ing the method not suitable and robust for such complex samples.

### Anonymous candidate answer

1. Answerability 
answerable – The chunks give multiple concrete PFAS preconcentration protocols across aqueous matrices and methods, enough to describe how it is generally done and how it varies.

---

2. Answer 

**General concept**

PFAS are typically at ng L⁻¹–µg L⁻¹ levels and often in complex matrices, so they are almost always **preconcentrated and cleaned up before LC‑MS/MS**. The dominant approaches are:

- **Off‑line solid‑phase extraction (SPE)** on weak‑anion‑exchange (WAX) or other sorbents 
- **Solid‑phase microextraction (SPME)** for ultra‑trace aqueous work 
- Occasionally, **no preconcentration** (dilute‑and‑shoot) for very high‑concentration samples or screening

---

### 1. Solid‑phase extraction (SPE): the workhorse

Across many water‑based matrices, preconcentration uses **anion‑exchange SPE cartridges** (most often Oasis WAX) with similar steps:

1. **Filtration / coarse cleanup** 
 - Environmental and industrial waters are filtered (0.8 µm or glass microfiber) to remove suspended solids before SPE.

2. **Cartridge conditioning** 
 - Typical sequence: 
 - Basic methanol (e.g., 0.1–0.5 % NH₄OH in MeOH) 
 - Pure methanol 
 - Water (Milli‑Q/ultrapure) 
 - This activates both the hydrophobic and anion‑exchange sites.

3. **Sample loading (preconcentration step)** 
 - Large volumes of water (10–500 mL) are passed through the SPE to concentrate PFAS onto a small sorbent bed. 
 - Examples: 
 - 500 mL drinking water loaded dropwise onto Oasis WAX (500 mg) after filtration. 
 - 20 mL chromium‑plating wastewater on Oasis WAX (150 mg) at ~2 mL min⁻¹. 
 - 10 mL synthetic ion‑exchange regeneration waste on Oasis WAX (60 mg) at ~2 drops s⁻¹. 
 - For some methods, the entire sample is loaded to maximize enrichment, then evaporated to a few hundred microliters.

4. **Washing (matrix cleanup)** 
 - Aqueous **ammonium/sodium acetate buffer (~25 mM)** is commonly used to remove salts and weakly retained interferences while keeping PFAS bound.

5. **Elution (desorption into small volume)** 
 - Sequential elution with **methanol** and **basic methanol** (e.g., 0.1–0.5 % NH₄OH in MeOH) is routine: 
 - Methanol alone or followed by NH₄OH/MeOH. 
 - 4 mL MeOH then 4 mL 0.5 % NH₄OH/MeOH; or larger volumes as needed. 
 - Some protocols rinse sample bottles with MeOH and pull this through the cartridge to recover wall‑adsorbed PFAS; total extract is ∼8 mL from 250 mL feed, giving a 32‑fold concentration factor.

6. **Post‑elution concentration and transfer** 
 - Extracts are often **evaporated under nitrogen** to a small final volume (e.g., 0.5 mL) before LC‑MS/MS. 
 - Final extracts are filtered (0.22 µm) into autosampler vials.

7. **Internal standards and injection** 
 - Isotopically labeled PFAS IS are added before or after SPE for quantitative correction.

**Variation with matrix and purpose**

- **Drinking water / surface water (clean matrices)** 
 - Large sample volumes (100–500 mL) to reach ng L⁻¹ LOQs. 
 - WAX SPE with relatively standard conditioning, acetate wash, and MeOH / NH₄OH‑MeOH elution. 
 - Evaporation to ≤1 mL for strong preconcentration (e.g., 100‑fold).

- **Industrial and high‑ionic‑strength waters (plating wastewater, IEX regenerants)** 
 - SPE is used explicitly to **remove high salt and metals** as well as concentrate PFAS. 
 - Sample volumes are smaller (e.g., 10–20 mL) because PFAS and matrix loadings are higher. 
 - WAX still dominant, but conditioning and washing become more critical to prevent breakthrough or suppression; acetate buffer wash is retained.

- **Groundwater and remediation studies** 
 - Effluent samples either **diluted into calibration range** (if PFAS are high) or **preconcentrated via WAX SPE** when at lower levels or when matrix interferences must be removed. 
 - Choice between dilution vs SPE is driven by: expected PFAS concentration, need for low LOQs, and matrix complexity.

- **Post‑oxidation / TOP assay extracts** 
 - After oxidation and pH adjustment, samples are also subjected to SPE cleanup before LC‑MS/MS. 
 - The oxidation step may impose specific pH targets for best PFAS retention on WAX (often mildly acidic/neutral).

- **Custom SPE sorbents** 
 - Iron‑doped mesoporous silica sorbents have been used for SPE of long‑chain PFAS (C8–C14) from up to 100 mL water; nitrogen evaporation to small volumes provides the preconcentration.

---

### 2. Solid‑phase microextraction (SPME)

For ultra‑trace PFAS in relatively clean **aqueous matrices** (river, lake, tap, bottled waters), ion‑exchange **SPME** can serve as both extraction and preconcentration:

- A HLB‑WAX/PAN SPME phase provides hydrophobic plus anion‑exchange retention of PFAS. 
- Using only **1.5 mL sample**, the protocol achieved LOQs of 1–2.5 ng L⁻¹ for model analytes, reflecting substantial enrichment versus direct injection. 
- The improvement in sensitivity over **dilute‑and‑shoot** methods is explicitly attributed to the preconcentration effect of SPME. 
- Designed for water matrices; authors note potential extension to **more complex samples** for biomonitoring.

---

### 3. Cases with little or no preconcentration

- When PFAS concentrations are **well above detection limits**, some labs **dilute samples only** (“dilute‑and‑shoot”) into the calibration range (~10 µg L⁻¹) without SPE. 
- Regulatory or screening contexts may prefer this for throughput, accepting higher LOQs and more matrix effects.

---

3. Uncertainty and limitations 

- The evidence is almost entirely for **aqueous matrices** (drinking water, surface water, groundwater, industrial wastewater, synthetic brines); protocols for **serum, tissue, solids, or aerosols** are not covered here. 
- PFAS classes beyond the common anionic sulfonates and carboxylates (e.g., zwitterionic, cationic, polymeric PFAS) may require modified sorbents or conditions; such adaptations are not detailed in these chunks. 
- Specific recovery data by chain length and head group are sparse in the provided text, so detailed analyte‑by‑analyte optimization cannot be described.

---

4. Practical takeaway 

For most PFAS LC‑MS/MS analyses, especially at environmental levels, samples are preconcentrated by **anion‑exchange SPE (commonly Oasis WAX)** or, in ultra‑trace aqueous work, by **ion‑exchange SPME**; the main protocol levers that vary with matrix and analyte are the **sample volume (and thus enrichment factor), sorbent type and mass, conditioning and washing solvents to manage salts and organics, and the final evaporation volume** before mass spectrometric injection.

### Human label

- Adequate (`yes` / `no` / `uncertain`):
- Material scientific error (`yes` / `no` / `uncertain`):
- Confidence (`high` / `medium` / `low`):
- Notes:

---

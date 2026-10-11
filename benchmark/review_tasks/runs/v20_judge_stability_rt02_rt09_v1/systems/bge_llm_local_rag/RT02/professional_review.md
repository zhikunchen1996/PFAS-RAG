### 1. Overview: What batch tests vs columns actually tell us

Across the evidence set, adsorption performance is characterized with several distinct metrics:

- **Batch equilibrium capacity / isotherm parameters**  
  - Freundlich K_F, 1/n and K_d from isotherms or long-contact batch tests (Cantoni [S02]; Abulikemu [S03]; Xiao [S14]; Shapiro [S08]).  
  - These quantify *equilibrium sorbed mass per mass of media at a given aqueous concentration*.

- **Batch kinetics**  
  - Pseudo‑second‑order or related rate constants, k_ads, from time‑series batch tests (Shapiro [S08]; Xiao [S14]).  
  - These describe how fast a well‑mixed suspension approaches equilibrium.

- **Column / RSSCT breakthrough metrics**  
  - **C/C₀ vs bed volumes (BV)**, with defined thresholds (e.g., 10%, 50%, ~60% “BV60%”, or MCL exceedance) as capacity surrogates (Cantoni [S02]; Zeng [S04]; Pannu [S05]; Park [S06]; Murray [S07]; Griffin [S09]; Kempisty [S12]; McCleaf [S15]; Hara [S11]).  
  - Metrics include BV₁₀, BV₅₀, BV_MCL, BV₆₀%, or general “bed volumes to detection/breakthrough.”

- **Media usage rate / carbon use rate (CUR, MUR)**  
  - Mass of media per volume of water treated to a chosen breakthrough limit (Griffin [S09]; Kempisty [S12]; Murray [S07]).

These metrics are *not* interchangeable:

- **Equilibrium capacity and batch kinetics describe potential and intrinsic rates under well‑mixed, high‑contact conditions.**
- **Breakthrough bed volumes and media usage rates integrate equilibrium, mass transfer, hydraulics, and competitive effects under continuous flow.**

The studies collectively show that:

- Batch equilibrium metrics can sometimes correlate with column capacity rank order for individual PFAS under fixed conditions, but
- **They do not reliably predict absolute breakthrough times, bed volumes, or media lifetime across realistic waters, contact times, and PFAS mixtures.**

Below, I synthesize when each metric is informative for scale‑up and where it fails, then lay out the minimal evidence base needed for defensible service‑life claims.

---

### 2. When batch equilibrium and kinetics fail to predict column or field performance

#### 2.1. Resin case: single‑use vs regenerable AERs in PFAS‑impacted groundwater

In Ellis et al.’s field pilot with PFAS‑selective anion exchange resins (AERs) treating AFFF‑impacted groundwater:

- **Batch equilibrium differences did not translate to column lifetime.**
  - A macroporous single‑use resin (CalRes 2301) showed a **maximum PFOS batch capacity >4×** higher than two gel‑type single‑use resins, yet **PFOS pilot breakthrough was similar for all three** [S01-E03].  
  - This is an explicit example where **maximum batch capacity did not manifest as longer field service life**.

- **Polyacrylic A860 vs polystyrene resins**  
  - Prior batch/bench studies had reported effective PFAS removal by A860 under longer contact times and different NOM conditions [S01-E01, S01-E03].  
  - In the pilot, operated at ~2 min combined EBCT for the first two vessels, **A860 exhibited near‑immediate breakthrough (<1,000 BVs) for the PFAS mixture** [S01-E05].  
  - The authors attribute the discrepancy to **short EBCT and absence of the high‑NOM, long‑contact conditions** that had favored A860 in batch settings [S01-E03, S01-E05].  

- **Regenerable A520E vs single‑use resins**  
  - Under the same groundwater and EBCT, A520E reached reported breakthrough much earlier (on the order of 31,000 bed volumes, with that exact value not firmly tied to “total PFAS” in the excerpt) than the single‑use resins, for which long‑chain PFSAs remained below detection through ≥150,000 BVs [S01-E05].  
  - Despite broadly similar backbone chemistry (polystyrene) and quaternary amines, field behavior differed markedly; **batch data alone did not allow assuming similar column service lives**.

- **Batch affinity vs field BVs**  
  - Ellis et al. report strong empirical correlations between batch PFAS–Cl⁻ exchange coefficients (log K_ex) and **bed volumes to 50% breakthrough** for single‑use AERs, but explicitly caution that such correlations “**need further validation**” before use for field‑scale design [S01-E06].  
  - This underscores that even when batch/column correlations are observed, **they are not yet validated design tools**.

**Implication:** For ion exchange resins, both the magnitude and even the *direction* of scale‑up error can be wrong if one infers “better batch capacity ⇒ longer field life.” Contact time, NOM, and PFAS mixture alter performance enough that batch isotherms and kinetics are, at best, screening tools.

#### 2.2. GAC case: batch Kd vs pilot‑derived Kd and breakthrough

Liu et al. compared:

- **Kd from small‑scale batch tests on a microporous carbon (F300)** from Xiao et al. [S13-E02 referencing S14], with
- **Kd fitted from pilot‑scale equilibrium modeling** for four different GACs treating real PFAS‑contaminated groundwater [S13-E02].

They report:

- **Batch‑derived Kd values were smaller for short‑chain PFAS and larger for long‑chain PFAS** than pilot‑derived Kd [S13-E02].  
- Thus, using batch Kd directly for design would tend to:
  - **Overpredict time to breakthrough (capacity) for long‑chain PFAS such as PFOA and PFOS**, and  
  - **Underpredict time to breakthrough for shorter‑chain PFAS** [S13-E02].

Liu et al. also emphasize that:

- Batch studies typically use **higher PFAS concentrations (high µg/L–mg/L)**, while practical systems operate at ng/L–low µg/L; extrapolating isotherms beyond their measured range **substantially overestimated removal at low concentrations** for other contaminants [S13-E01].  
- Use of **pulverized GAC** in batch tests and some RSSCTs increases exposed surface area and can **alleviate DOC pore blocking**, which will **overestimate breakthrough times and adsorption capacities** relative to pilot/full‑scale systems using larger particles [S13-E01].

**Implication:** Even when batch Kd is used as an input to mechanistic models, scale and concentration mismatches introduce systematic bias into predicted bed volumes and service life, especially for long‑chain PFAAs.

#### 2.3. Batch isotherms alone cannot yield service life without validated models

Abulikemu et al. provide an explicit limitation statement for a comprehensive isotherm study of nine PFAS on GAC:

- **Equilibrium isotherms “do not directly evaluate adsorption breakthrough in full‑ or pilot‑scale GAC treatment systems”**, and **modeling (e.g., AdDesignS) is required** to relate isotherm parameters to column performance [S03-E05].
- Isotherm parameters were obtained with **ground GAC**, and the authors state these **“may need to be adjusted”** for full‑ or pilot‑scale systems because of particle‑size reduction effects [S03-E05].
- They also highlight that:
  - Ideal adsorbed solution theory (IAST) **performed poorly for PFAS mixtures**, with and without NOM; “using IAST as currently implemented may lead to errors in predicting performance for trace PFAS in mixtures” [S03-E07].  
  - **Kinetics and column‑scale behavior were not explored**, and the authors call for **small and pilot‑scale column tests with simultaneous modeling** to improve predictive capability [S03-E06, S03-E07].

**Implication:** A defensible service‑life claim cannot stop at isotherms; at minimum, it requires mechanistic modeling plus validation against continuous‑flow data that includes both PFAS mixtures and the relevant source‑water matrix.

#### 2.4. Batch kinetics vs column kinetics for a novel polymer adsorbent

Shapiro et al. evaluated PFAS and pharmaceuticals on a β‑cyclodextrin polymer (StyDex) in municipal wastewater using both batch and RSSCT columns [S08]:

- **Batch tests showed rapid sorption kinetics**, and kinetic constants k_ads could be estimated.  
- However, **“batch sorption kinetic constants did not match column breakthrough kinetics, due to an inability to describe complex flow‑through behaviors”** [S08-E02, S08-E08].
- Column data showed:
  - BV₅₀ for PFOA and PFHxS increased markedly with increasing contact time; at 10 min contact, BV₅₀ was not reached over ~78,000 BVs, but at 3 min contact, BV₅₀ for PFOA and PFHxS dropped to 21,000 and 27,000 BVs, respectively [S08-E06].  
  - Several trace organics had BV₅₀ of only 20,000–25,000 BVs even at longer contact times [S08-E06].
- The authors conclude that **batch‑derived kinetics were insufficient to predict column breakthrough**, and that non‑ideal competitive sorption–desorption behaviors and contact‑time dependence mean **simple scaling of RSSCT results to pilot scale may be inaccurate**, particularly for PFAS + co‑contaminant mixtures [S08-E02, S08-E06, S08-E07].

**Implication:** Rapid batch kinetics do **not** guarantee adequate performance at short EBCT in columns, and do not in themselves justify a claim of service life.

#### 2.5. Pure modeling based on batch calibration cannot substitute for column verification

Xiao et al. calibrated an intraparticle diffusion‑limited transport model for a full‑scale GAC system (two 28.5 m³ vessels in series at 1.5 m³/min, each with a 2.7 m GAC bed) treating AFFF‑impacted water [S14-E02]. Model inputs were batch‑derived K_d and kinetics for multiple AFFF‑derived PFAS.

Key limitations explicitly noted:

- Several PFAS had equilibrium K_d estimated with a **linearized pseudo‑second‑order model known to *underestimate* equilibrium K_d**, especially when far from equilibrium [S14-E02].
- The model assumes **intraparticle diffusion‑limited kinetics** parameterized via an apparent tortuosity; competition with DOC and among PFAS was only partially represented [S14-E01, S14-E02].
- The authors state that:
  - **Competition among PFAS and between PFAS and DOC may affect breakthrough differently in actual systems than predicted** [S14-E01].  
  - Smaller PFAS can initially access virgin carbon before DOC or larger PFASs, making them **susceptible to later remobilization**, a dynamic only qualitatively represented [S14-E01, S14-E02].  
  - Although forward simulations produced bed volumes to breakthrough of the same order as a previously monitored field GAC system, **“pilot-scale column verification experiments should be conducted when sufficient water quantities are available”** [S14-E08].

**Implication:** Even sophisticated models rooted in batch data must be verified with pilot or field column studies; otherwise, they provide at best qualitative guidance on PFAS treatability and relative breakthrough order.

---

### 3. When column‑scale data (RSSCT, pilot, full‑scale) do and do not translate across scales

#### 3.1. RSSCTs as surrogates for pilot/full‑scale GAC and IX

Several studies use RSSCTs with defined similitude models to approximate pilot/full‑scale fixed beds:

- **Park (bituminous GAC, groundwater, CD‑RSSCT)**  
  - Demonstrated that, under low hydraulic loading (3.8 m/h) and conditions where intraparticle diffusion was independent of GAC particle size, the **constant‑diffusivity (CD) RSSCT model** was appropriate [S06-E01, S06-E02, S06-E06].  
  - BV₅₀ (as a capacity indicator) correlated monotonically with PFAS Log D_ow, showing hydrophobicity‑controlled breakthrough ranking [S06-E02].  
  - However, they stress that **pilot testing remains the most representative** of full‑scale operation because it captures **adsorbent size heterogeneity and pore blocking by DOM**, which bench RSSCTs and numerical simulations cannot reproduce [S06-E05, S06-E07].

- **Kempisty (PD‑RSSCT vs full‑scale GW and pilot SW GAC)**  
  - Proportional‑diffusivity (PD) RSSCTs for Minnesota groundwater **consistently overpredicted full‑scale capacity**, with mean RSSCT/full‑scale BV ratios of 1.7 (range 1.4–2.0; n = 8) for 10 % and 50 % breakthrough [S12-E02, S12-E07].  
  - Overprediction was attributed to **pore blockage by DOM near external GAC surfaces**, which affects full‑scale (larger particles) more than RSSCT particles [S12-E02].  
  - For North Carolina surface water, the same PD‑RSSCT design **matched pilot‑scale breakthrough more closely** [S12-E01, S12-E02], highlighting matrix dependence.  
  - Authors explicitly state that **PD‑RSSCT data “cannot be used without adjustment” to predict full‑ or pilot‑scale PFAA removal performance** because of systematic overprediction in groundwater [S12-E04].

- **Zeng (CD‑RSSCT for GAC and IX, PFAS‑impacted groundwaters)**  
  - CD‑RSSCTs treated six PFAS‑impacted groundwaters, achieving adsorption capacities q_ΣPFAS from 10.3–228 ng/mg after ~100,000 BVs [S04-E02].  
  - CD‑RSSCTs exhibited **earlier breakthrough than PD‑RSSCTs**, and using CD to design full‑scale systems is described as **“conservative”**, likely overestimating replacement frequency and cost [S04-E06].  
  - Authors further note that **very long run times (years) would be required to see detectable PFAS breakthrough in full‑scale systems**, so RSSCTs must stand in despite **limited direct comparisons to pilot/full scale** [S04-E06].

- **Murray (CD‑RSSCT for multiple adsorbents and matrices)**  
  - CD‑RSSCTs were explicitly scaled from crushed media to full‑scale by a fixed particle‑size ratio and scale‑up factor [S05-E01, S05-E08].
  - For **bituminous GACs**, Well‑4 groundwater RSSCTs and complementary pilot results (Medina et al., 2022, as cited) generally agreed at **BV₆₀%**, although RSSCT predictions were more conservative at initial breakthrough [S05-E04, S05-E05].  
  - For **FS200 alternative adsorbent**, RSSCT severely **under‑predicted breakthrough**, projecting much longer media life than observed in the pilot at both initial and BV₆₀% breakthrough [S05-E05]. Authors call for further work to evaluate whether constant‑diffusivity assumptions and RSSCT methods are valid for this adsorbent [S05-E05].  
  - Murray also shows how **higher influent PFAA concentration (GW2 vs GW1) resulted in ~3× faster breakthrough** for GAC and IX in RSSCTs, despite similar background water quality [S07-E07].  

**Implications:**

- RSSCTs are powerful for **relative ranking** of adsorbents and conditions, and—when similitude assumptions hold and matrices are matched—can **approximate pilot behaviour within a factor** (e.g. ~1.7 for GW in Kempisty).  
- However:
  - Scaling errors can be **compound‑ and matrix‑specific**, and even the *sign* of error (conservative vs non‑conservative) can flip depending on adsorbent (e.g. FS200 vs GAC in Murray [S05-E05]).  
  - **DOM‑induced pore blocking** and long‑term fouling are under‑represented in RSSCTs and absent from batch tests; these are central to why batch/RSSCT often overpredict full‑scale capacity.

#### 3.2. Full‑scale and pilot evidence on EBCT and media life

- **Full‑scale GW GAC (Kempisty)**  
  - Two full‑scale lead–lag GAC vessels (EBCT 13 min each, 12 m/h HLR) treating low‑TOC groundwater showed:
    - PFAA adsorbability increasing with chain length; PFSAs more adsorbable than PFCAs of same length [S12-E04, S12-E05].  
    - **No consistent effect of doubling EBCT from 13 to 26 min on carbon use rate (CUR)** in this groundwater [S12-E04].  
  - Using CUR ≤25 mg GAC/L as a feasibility threshold, GAC was considered viable for PFAAs with **five or more carbons** in this GW (TOC = 0.7 mg/L) [S12-E04].

- **Pilot‑scale SW GAC (Kempisty)**  
  - Same GAC in coagulated surface water (TOC 2.0–2.7 mg/L) had higher CURs (less favorable) and smaller bed volumes to breakthrough; SW volume treatable to 10 % or 50 % breakthrough was only **50–60 % of GW volume** when comparing pilot SW vs full‑scale GW [S12-E07].  
  - At CUR ≤25 mg/L criterion, GAC was viable only for PFAAs with **six or more carbons** in this SW [S12-E04].

- **Pilot GAC in PFAS‑impacted groundwater (Liu)**  
  - A seven‑month pilot with four commercial GACs treating real contaminated groundwater showed **chain‑length‑dependent breakthrough** for PFCAs and PFSAs and broadly similar performance across the four GACs [S13-E05].  
  - Authors argue that such pilot‑scale data are necessary because **most prior PFAS–GAC work was batch or RSSCT with synthetic waters that “poorly approximate” full‑scale conditions** [S13-E05, S13-E06].

- **Full‑scale landfill leachate GAC (Hara)**  
  - A full‑scale leachate plant (80 m³/d, 0.9 t GAC) showed long‑term PFAS removal with BV₅₀ strongly positively correlated with PFAS log D (r = 0.94 overall; 0.97 within PFCAs and PFSAs) [S11-E07].  
  - However, DOC in the field system averaged 4.39 mg/L vs 58.63 mg/L in lab columns; the authors explicitly state **direct quantitative comparison between lab and field is not feasible** because DOC and influent PFAS differ, and uncharacterized organics are present [S11-E02, S11-E05].

**Implications:**

- EBCT effects are matrix and system specific: in low‑TOC groundwater doubling EBCT did not clearly improve CUR, while in leachate and SW the presence of NOM makes longer contact and larger transport pores more important.
- Translation of breakthrough BVs and CUR from one system to another requires matching **TOC, DOM character, PFAS spectrum, GAC type and size**, and EBCT; even then, only approximate scale‑up (within a factor) is justified.

---

### 4. Role of contact time, flow, and hydraulics in translating batch to columns and across scales

#### 4.1. EBCT and mass‑transfer zone development

Park’s CD‑RSSCT study demonstrates EBCT‑driven changes in breakthrough shape:

- Increasing EBCT_LC from 5 to 10 to 20 min on F400 GAC:
  - For the **weakly adsorbing PFBA**, breakthrough curves became **shallower** as EBCT increased—indicating a broader mass transfer zone at longer contact times [S06-E03].  
  - More favorably adsorbing PFPeA and PFHxA showed **smaller differences** across EBCT, confirming that **EBCT sensitivity is compound‑dependent** [S06-E03].
- Longer EBCTs caused **more pronounced chromatographic overshoot** for hydrophilic PFBA and PFPeA due to accumulation and later desorption [S06-E02, S06-E03].

In Shapiro’s StyDex columns:

- Reducing CT_LC from 5 to 3 min reduced BV₅₀ for PFOA from ~44,000 BVs to 21,000, and for PFHxS from ~44,000 to 27,000 BVs [S08-E06].  
- At 7.5–10 min CT, BV₅₀ for these PFAS was not reached within ~72,000–78,000 BVs [S08-E06].

Ellis’s AER pilot intentionally used short EBCTs (30 s per lead vessel; 2 min combined for first two vessels), explicitly contrasting with prior “lengthy batch reactions” [S01-E07, S01-E05]. Under these short contact times:

- Polyacrylic A860 had **<1,000 BVs** to observed PFAS breakthrough, while polystyrene single‑use resins maintained PFOS non‑detect through ≥75,000 BVs [S01-E05].

Hara’s landfill‑leachate columns show that **higher flow (shorter effective contact time) causes earlier breakthrough**, with short‑term tests at 1.0 vs 5.0 mL/min used specifically to probe contact‑time effects [S11-E03, S11-E08].

**Implications for translation:**

- **Batch systems operate effectively at EBCT→∞** (hours–days of contact), so they cannot reveal whether a sorbent will meet target breakthrough at 2–10 min EBCT.  
- Column and RSSCT data must explicitly specify EBCT (or CT_LC) and HLR; **claims of service life are meaningless without these.**
- EBCT interacts with PFAS hydrophobicity and kinetics; scaling EBCT between bench and full scale must preserve superficial velocity and bed‐height relationships used in the chosen similitude model (CD vs PD).

#### 4.2. Particle size and intraparticle diffusion

- Park found that **PFAS breakthrough on F400 coincided for three GAC particle sizes** at the same EBCT_LC, supporting the CD model and suggesting **intraparticle diffusion was independent of particle size** under their groundwater conditions [S06-E06]. However, they caution that this is not conclusive for more strongly adsorbing PFAS (PFOA, PFDA, PFDoDA, PFOS) whose full breakthrough was not observed [S06-E06].
- Kempisty and Liu both emphasize that **pulverized or crushed GAC** (RSSCT and batch) experiences **less pore blocking** and different mass‑transfer regimes than full‑scale GAC, contributing to overprediction of capacity [S12-E06, S13-E01].

**Implication:** Any attempt to use isotherm‑derived parameters or RSSCT results for scale‑up must identify and justify the **particle‑size scaling assumption** (CD vs PD) and recognize that DOM and fouling can break similitude.

---

### 5. Influence of influent variability, NOM, competing constituents, and PFAS mixtures

#### 5.1. Natural organic matter (DOM/NOM) and anions

Multiple studies pinpoint DOM and inorganic anions as dominant factors in PFAS adsorption performance:

- Abulikemu’s isotherm study shows **preloaded NOM reduced PFAS q_e more than co‑loaded NOM**, consistent with direct competition and pore blockage [S03-E05].
- Murray’s RSSCTs across matrices (groundwater, wastewater, landfill leachate, membrane concentrate) show:
  - Higher DOC and anions (WW, LL, MC) caused **earlier breakthrough and higher adsorbent use rates** for all PFAA subclasses except long‑chain PFSAs [S07-E03].  
  - Even IX and SMC, which experienced **less pronounced inhibition than GAC**, still had **higher use rates in wastewater than groundwater**, demonstrating that even selective adsorbents are negatively impacted by DOC and anions [S07-E03].
- Kempisty found that CURs were **lower (better) in low‑TOC GW (0.7 mg/L) than in SW (2.0–2.7 mg/L)**, and that GAC with larger mesopore volume performed better in SW, indicating that **DOM and pore structure jointly control effective capacity** [S12-E04, S12-E07].
- Griffin’s NF–adsorbent train explicitly uses NF to remove EfOM and inorganic ions prior to GAC/IX, because **EfOM and co‑adsorbing inorganic ions inhibit adsorption** [S09-E01, S09-E08]. Their subsequent RSSCTs systemically compare adsorption in wastewater effluent vs NF permeate vs PFAS‑spiked NF permeate to isolate matrix effects [S09-E01, S09-E06].

**Implication:** DOM and co‑ions are primary determinants of real‑world capacity. Batch tests in simplified or single‑matrix conditions must not be generalized to different NOM/inorganic regimes without supporting data.

#### 5.2. Competitive PFAS mixtures and chromatographic displacement

Evidence for competition and chromatographic effects is consistent and strong:

- **Ellis AER pilot:** Post‑mortem profiling showed:
  - Long‑chain PFSAs and PFCAs concentrated in upstream column sections;  
  - Short‑chain PFCAs were **displaced toward later sections and into effluent**, with effluent concentrations of these short‑chains **exceeding influent values** [S01-E02, S01-E04].  
- **Cantoni GAC RSSCTs and full scale:**  
  - A “chromatographic effect” where **hydrophilic PFAS effluent concentrations exceeded influent**, due to displacement by more hydrophobic PFAS and DOM, was observed both in RSSCTs and full‑scale adsorbers [S02-E06, S02-E08].
- **Park GAC RSSCTs:**  
  - Hydrophilic PFBA and PFPeA showed **overshoot (C/C₀ >1)**; overshoot was more pronounced at longer EBCTs [S06-E02, S06-E03].  
- **Hara full‑scale leachate GAC:**  
  - Occasional **negative removal efficiencies** (C_out > C_in) for some PFASs were noted in the Gompertz‑fitted breakthrough profiles [S11-E04, S11-E07].
- **Shapiro StyDex RSSCTs:**  
  - PFBA in both multi‑component and two‑component PFOA+PFBA experiments exhibited **desorption with C/C₀ up to 1.21 over 7,400–44,620 BVs** [S08-E07].  
  - Authors emphasize that **co‑occurrence of PFBA and longer‑chain PFAS is a major challenge** because competitive adsorption–desorption can remobilize PFBA [S08-E07].

**Implications:**

- **Single‑solute batch isotherms inherently miss chromatographic displacement.**  
- Overshoot and C_out>C_in imply that **“breakthrough” is not a monotonic approach to C/C₀=1**; service‑life predictions must consider both initial and desorptive phases.
- PFAS chain‑length hierarchy (long‑chain PFSA>long‑chain PFCA>short‑chain PFAS) remains broadly valid, but competition may reorder apparent capacity for shorter‑chain species over time.

#### 5.3. Influent PFAS concentration and variability

- **Murray GW1 vs GW2:**  
  - GW2 had PFAA concentrations **multiple orders of magnitude higher** than GW1 but similar background water quality [S07-E07].  
  - GAC and IX experienced **~3× faster PFAA breakthrough** in GW2 than GW1 [S07-E07].  
  - Authors suggest this may reflect **higher concentration gradients driving mass transfer and aggregation of long‑chain PFAAs at the adsorbent surface** [S07-E03, S07-E07].
- **Ellis and Liu** both note that **site‑specific influent PFAS concentrations and histories** influence how much PFAS mass is adsorbed before breakthrough; pilot‑scale results at high‑concentration AFFF sites cannot be directly extrapolated to lower‑concentration sites, and vice versa [S01-E03, S01-E05; S13-E07].

**Implication:** Service‑life claims must explicitly state influent PFAS concentrations and recognize that higher influent can both **reduce BVs to breakthrough** and alter competitive dynamics, independent of equilibrium capacities.

---

### 6. Comparing the information content of different metrics

#### 6.1. Equilibrium capacity and Kd

- **What it tells you:**  
  - Rank order of PFAS affinity to a given sorbent under a specific matrix and concentration range.  
  - Useful for **screening sorbents** and parameterizing models.

- **What it does *not* reliably tell you:**  
  - BVs to breakthrough at realistic EBCT and particle size.  
  - Impact of DOM, co‑ions, and competition at low ng/L.  
  - Long‑term fouling and desorption behavior.

Abulikemu [S03], Cantoni [S02], Xiao [S14], and Liu [S13] all support this conclusion.

#### 6.2. Batch kinetics (k_ads) and short‑term uptake

- **What it tells you:**  
  - Whether sorption is “fast enough” in a well‑mixed system, often suggesting whether mass transfer might limit performance at short EBCT.

- **Limitations:**  
  - Shapiro shows that even when batch kinetics appear rapid, **column breakthrough at 3 min CT was dramatically worse** than at 5–10 min CT, and **batch kinetic constants did not match column kinetics** [S08-E02, S08-E06].  
  - Xiao notes kinetic model forms used for PFAS that had not equilibrated **underestimate equilibrium K_d**, adding uncertainty [S14-E02].

On their own, batch kinetics cannot guarantee column performance or media life at a given EBCT.

#### 6.3. Fixed‑bed breakthrough metrics (BV₁₀, BV₅₀, BV₆₀%, BVMCL)

- **What they tell you:**  
  - Integrated effect of equilibrium, kinetics, competitive interactions, and hydraulics for a specific set of conditions.  
  - Empirical bed volumes to a defined breakthrough threshold—effectively, a **direct proxy for service life** under the tested conditions.

- **Limitations:**  
  - Scale‑dependence: PD/CD‑RSSCT vs pilot vs full-scale differences (overprediction factors, conservative vs non‑conservative outcomes).  
  - Sensitivity to choice of breakthrough criterion (10%, 50%, 60%, MCL); different stakeholders may require different criteria.

Nevertheless, **breakthrough‑based metrics are the only ones that consistently correspond to “media lifetime” in practical terms**, and they must be the core of any scale‑up argument.

#### 6.4. Media usage rate (MUR/CUR) and economic metrics

- Translate BVs and breakthrough to **mass of media per volume treated** (e.g., mg GAC/L, lb/MG).  
- Allow cross‑comparison of adsorbents in techno‑economic analyses (Griffin [S09]; Kempisty [S12]; Murray [S07]).  
- These require:
  - Defined breakthrough criterion (e.g., BV_MCL, BV₆₀%).  
  - Media density, bed geometry, and plant flow.

They are meaningful only if **based on column data in the target or a closely analogous matrix**; batch capacities alone are insufficient to estimate CUR/MUR.

---

### 7. Minimum evidence needed for a defensible service‑life or scale‑up claim

Based on the collective evidence and explicit limitations reported, a **defensible claim** about service life or full‑scale performance for PFAS adsorption should, at minimum, include:

1. **Well‑defined water matrix and quality:**
   - Source description (e.g., PFAS‑impacted groundwater, landfill leachate, wastewater effluent, SW) and key parameters: DOC/TOC, major anions, pH, ionic strength where relevant (Abulikemu [S03]; Kempisty [S12]; Murray [S07]; Hara [S11]; Griffin [S09]).

2. **PFAS mixture and concentrations:**
   - List of target PFAS (at least by subclass: short‑/long‑chain PFCAs and PFSAs; precursors if present) and influent levels (Ellis [S01]; Zeng [S04]; McCleaf [S15]; Shapiro [S08]; Hara [S11]).

3. **Adsorbent identity and form:**
   - Material (e.g., bituminous vs coconut GAC; polystyrene vs polyacrylic AER; novel polymers; SMC vs IX vs GAC) and **particle size** (as‑received vs crushed vs pulverized) (Cantoni [S02]; Park [S06]; Kempisty [S12]; Murray [S07]; Shapiro [S08]; Xiao [S14]).

4. **Column configuration and hydraulics:**
   - EBCT or CT_LC, bed height, superficial velocity, hydraulic loading rate, and vessel geometry (H/D) to guard against wall effects (Ellis [S01-E01]; Park [S06]; Kempsity [S12]; McCleaf [S15]; Hara [S11]).  
   - For RSSCT‑based claims, the **similitude model (CD vs PD)** and scaling relationships must be stated (Park [S06]; Zeng [S04]; Kempisty [S12]; Murray [S05]; Griffin [S09]).

5. **Breakthrough definition and duration:**
   - Exact metric used: BV₁₀, BV₅₀, BV₆₀%, BV_MCL, or “first detection” (C/C₀=0.1; 0.5; ~0.6; MCL exceedance) [S02-E03; S04-E02; S05-E02; S09-E02; S12-E01; S15-E02].  
   - Evidence that the test ran sufficiently long to capture the relevant breakpoint (e.g., Hara’s leachate plant over months, Kempisty’s 4.8‑year operation, Ellis’ ≥150,000 BVs, Shapiro’s ~78,000 BVs at longest CT) [S11-E03; S12-E03; S01-E05; S08-E06].

6. **Matrix comparability for scale‑up:**
   - For translations (batch → RSSCT → pilot → full scale), **at least one intermediate continuous‑flow step under representative water quality** is needed to validate model parameters (Abulikemu [S03]; Xiao [S14]; Liu [S13]; Kempisty [S12]; Park [S06]; Griffin [S09]).  
   - Overprediction factors (e.g., 1.7× for PD‑RSSCT vs full scale in GW [S12-E02]) should be quantified where possible, with clear indication whether they are conservative (overpredicting life) or non‑conservative (underpredicting) for each adsorbent/matrix (Murray FS200 case [S05-E05]).

7. **Account of competitive and desorptive behaviors:**
   - Evidence (experimental or modeled) that competitive displacement and chromatographic overshoot have been considered in defining acceptable service life, especially for short‑chain PFAS (Ellis [S01]; Cantoni [S02]; Park [S06]; Shapiro [S08]; Croll [S10]; McCleaf [S15]).

8. **Explicit exclusion of unsupported extrapolations:**
   - Authors should acknowledge, as Abulikemu, Liu, Xiao, and Shapiro do, that:
     - **Isotherms and batch kinetics alone do not evaluate breakthrough** [S03-E05; S13-E01; S08-E02].  
     - **Models calibrated solely on batch data require pilot/field verification before being used for design** [S14-E02, S14-E08].  
     - **RSSCT overprediction or underprediction factors are matrix‑ and sorbent‑specific** [S12-E02; S05-E05].

Without this level of evidence, any claim that “equilibrium capacity X mg/g corresponds to Y years of full‑scale operation” is not defensible.

---

### 8. Practical guidance on using batch adsorption data in PFAS treatment design

Synthesizing across studies:

- **Appropriate uses of batch data:**
  - **Screening and ranking sorbents** for a given matrix and PFAS suite (Cantoni [S02]; Xiao [S14]; Abulikemu [S03]).  
  - Deriving **initial parameters** (K_F, K_d, k_ads) for mechanistic models and to inform RSSCT and pilot test design (Abulikemu [S03]; Xiao [S14]; Shapiro [S08]).  
  - Establishing **structure–reactivity trends** (e.g., chain length, PFSA vs PFCA) that are generally consistent across scales (Park [S06]; Kempisty [S12]; Hara [S11]; Liu [S13]).

- **Inappropriate uses (per the evidence and task constraints):**
  - Presenting **batch capacity or short‑term kinetics as direct proof of column breakthrough times or full‑scale media lifetime**—the resin and GAC examples above show this can be off by factors >1.5–2 and even wrong in direction.  
  - Making scale‑up claims **without specifying EBCT/contact time, flow/HLR, influent variability, competing constituents, PFAS mixture, and breakthrough definition**—each of these factors demonstrably affects translation across scales.

A robust design or service‑life estimate should therefore combine:

1. **Matrix‑specific batch tests** → sorbent screening and model parameterization.  
2. **RSSCTs under representative EBCT and particle size** → preliminary capacity and selectivity, and estimation of over/under‑prediction factors relative to known pilot/full‑scale analogues.  
3. **Pilot‑scale or long‑running full‑scale monitoring** in the target or a closely analogous matrix → validation and refinement of breakthrough models and CUR/MUR.

Only with this evidence chain can equilibrium and kinetic data be legitimately tied to predictions of full‑scale PFAS treatment performance.

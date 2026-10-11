### 1. Overview and scope

Across the evidence base, batch adsorption tests, RSSCTs, pilot studies, and full‑scale systems each provide **different, often non‑equivalent information** about PFAS treatment by GAC, ion exchange, and novel sorbents. The studies consistently show that:

- **Equilibrium batch capacity and short‑term kinetics are useful for ranking sorbents and understanding mechanisms**, but by themselves *do not* reliably predict column breakthrough times, bed volumes treated, or media lifetime under field conditions.
- **Column‑scale metrics**—bed volumes to specified breakthrough, BV‑based capacities, and media use rate—are the direct descriptors of service life, but are strongly conditioned by EBCT, hydraulic loading, influent variability, competing constituents, and PFAS mixture.

Below, I first compare what each metric actually tells you, then synthesize how operating conditions and water chemistry control translation across scales, and close with a concrete statement of the minimum evidence needed for a defensible service‑life or scale‑up claim.

---

## 2. What different metrics do—and do not—tell you

### 2.1 Equilibrium capacity and batch sorption parameters

Several studies report **equilibrium isotherm parameters or Kd values**:

- Abulikemu et al. measured isotherm‑based capacities and Kd for nine PFAS on ground GAC under drinking‑water‑relevant conditions and varied NOM, ions, and co‑occurring PFAS, specifically to support later column modeling rather than to claim direct breakthrough predictions [R01]. They explicitly note that **isotherms “do not directly evaluate adsorption breakthrough,” and must be coupled with tools such as AdDesignS for column design** [R01‑E05].
- Xiao et al. measured 20‑day log Kd values for 30 PFAS on GAC and biochars in AFFF‑impacted groundwater, and used these data to calibrate an intraparticle diffusion model [R02]. The authors emphasize that **for PFAS that had not reached equilibrium, Kd estimates from pseudo‑second‑order fits can be biased low** [R02‑E02].
- Cantoni et al. developed Freundlich isotherms for eight PFAS on PACs ground from full‑scale GACs (KF, 1/n) in tap water with DOM [R03‑E02]; batch data were intended to be *correlated* with RSSCT and full‑scale behavior, not taken as service life per se [R03‑E01].
- Cheng et al. determined Kd values for individual components of a biochar‑based composite (BIPGEM) in batch [R04‑E06, R04‑E08].

These batch parameters:

- **Characterize affinity and capacity under a defined matrix and contact time.**
- Enable **mechanistic interpretation** (e.g., hydrophobic vs electrostatic contributions, NOM competition) [R01; R02; R04].
- Provide inputs to **column models** (e.g., Abulikemu: isotherms feeding AdDesignS; Xiao: diffusion‑limited transport; Cantoni: Lin & Huang model for RSSCT) [R03; R01; R02].

However, field‑connected studies show that **batch capacity alone is not a service‑life predictor**:

- In the Ellis AER pilot, a macroporous single‑use resin had a **>4‑fold higher maximum PFOS batch capacity than two gel‑type resins**, yet **PFOS breakthrough in the pilot columns was similar for all three** [R05‑E03]. The authors conclude that **“other factors beyond maximum adsorption capacity” control continuous‑flow uptake** [R05‑E03].
- Ellis also shows that the polyacrylic A860 resin looked favorable in earlier bench studies with higher NOM and much longer contact times, but exhibited near‑immediate PFAS breakthrough at the short EBCT used in the pilot [R05‑E05, R05‑E03].
- Abulikemu et al. explicitly caution that **isotherm parameters measured on ground GAC “may need to be adjusted” for full‑scale GAC due to particle‑size and kinetic differences**, and that their isotherm results “do not replace a site‑specific pilot or other study to determine GAC’s breakthrough performance” [R01‑E05, R01‑E07].

Taken together, **batch equilibrium capacity is at best a first‑pass screening metric** and a model input. It is not, on its own, defensible evidence of column bed volumes or media life.

### 2.2 Batch kinetics

Batch kinetic tests quantify how fast sorption approaches equilibrium. Two studies explicitly compare these to column behavior:

- Shapiro et al. report that for a cyclodextrin‑based polymer (StyDex), **the “kinetics observed in batch adsorption tests are maintained” qualitatively in RSSCTs**, but **batch kinetic constants did not match column breakthrough kinetics**, i.e., they were unable to describe complex flow‑through behavior [R06‑E02, R06‑E08].
- Xiao et al. derived kinetic parameters (e.g., apparent tortuosity) from batch time‑series data to build a diffusion‑limited GAC model, and then forward‑simulated full‑scale breakthrough [R02‑E02]. The model reproduced breakthrough *orders* and approximate bed volumes for many PFAS, but the authors emphasize the need for **pilot‑scale verification** where water volume is available [R02‑E08].

So, **batch kinetics can reveal whether a sorbent is fast enough to merit column testing and help parametrize models**, but even when the same adsorbent and water are used, **batch rate constants have not been shown to quantitatively reproduce RSSCT or pilot breakthrough curves** [R02; R06].

### 2.3 Fixed‑bed breakthrough metrics and bed volumes treated

Fixed‑bed systems directly report the performance metrics needed for design:

- **Bed volumes to specified breakthrough** (e.g., BV10, BV50, BV60, or C/C0 = 0.1).
- **Bed volumes to regulatory or health‑based thresholds** (BVMCL).
- **Media use rates** (e.g., lb/MG at BVMCL).

Examples:

- Ellis et al. report **bed volumes to 50% breakthrough** for individual PFAAs on various AERs at a 30‑s EBCT per lead vessel (2 min for first two vessels) treating high‑PFAS AFFF‑impacted groundwater [R05‑E07]. They use BV50 as a continuous‑flow performance indicator and relate it empirically to batch exchange coefficients [R05‑E06].
- Cantoni et al. define **BV50** from RSSCT breakthrough curves via the Lin & Huang model and treat it as an adsorption capacity metric, then compare BV50 to full‑scale median removals and solid‑phase loadings [R03‑E03, R03‑E05].
- Shapiro et al. use **BV50** for different PFAS at contact times of 3–10 min to define “treatable bed volumes” in RSSCT columns [R06‑E06]. For most contaminants BV50 was 20,000–25,000 BVs, but PFOA and PFHxS showed much higher BV50 at longer contact times [R06‑E06].
- Murray et al. and Pannu et al. use **BV60%** (C/C0 = 0.6) as a “significant breakthrough” metric for GACs, IX, and an alternative adsorbent in RSSCTs, and explicitly compare BV60% between RSSCT and pilot for both GACs and the alumina‑based FS200 media [R07‑E02, R07‑E04, R07‑E05].
- Griffin et al. define **BV10, BV50, and BVMCL** for GAC and IX RSSCTs fed with wastewater effluent and NF permeates; BVMCL is tied to first exceedance of EPA MCLs and is used to derive **media usage rate (lb/MG)** [R08‑E02].
- McCleaf et al. and Kempisty et al. use **C/C0 = 0.1** as their breakthrough definition in bench GAC and AE columns [R09‑E02], and full/pilot GAC systems, respectively. Kempisty express performance in **bed volumes to 10% and 50% breakthrough** and relate this to carbon use rate across scales [R10‑E04, R10‑E07].
- Hara et al. use **BV50 (from Gompertz fits) and full breakthrough profiles** to compare landfill leachate columns and a full‑scale GAC plant [R11‑E02, R11‑E03, R11‑E07].
- Croll et al. similarly fit pilot GAC pilot data with adapted dose–response models and use these to estimate **media life to predetermined breakthrough criteria** and to predict maximum effluent concentrations during desorption [R12‑E02, R12‑E07].

These BV‑based endpoints are **direct measures of separation performance in a given hydraulic and chemical context**, and they can support scale‑up *if* the underlying similitude assumptions (e.g., RSSCT CD or PD model) are valid and if matrix and PFAS composition are comparable.

Crucially, none of these studies justify media life solely from batch capacities or short‑term kinetics; **they rely on breakthrough data (or validated models) with specified EBCT, influent quality, and PFAS mixtures.**

---

## 3. How operating conditions and water chemistry control translation

### 3.1 Flow and empty bed contact time (EBCT)

Evidence shows **contact time strongly shapes breakthrough curves**, but not always in the way naive intuition suggests.

- **Short EBCT and under‑utilized beds.** Ellis’s pilot AER columns operated at a **30‑s EBCT per vessel (2 min across two vessels)** yet treated **>750,000 bed volumes** through the lead vessel [R05‑E07]. For long‑chain PFSAs, effluent remained non‑detect for extended operation, but short‑chain PFCAs experienced early breakthrough and displacement [R05‑E02, R05‑E04]. Here, **EBCT is short compared to many GAC designs**, yet strong‑affinity PFAS were effectively captured.
- **EBCT affects curve shape more than BV50 in some systems.** Park et al. varied EBCT (5, 10, 20 min, as EBCTLC) for F400 GAC RSSCTs at fixed superficial velocity. For weakly adsorbing PFBA, longer EBCT produced *shallower* breakthrough (more developed mass transfer zone), but **BV50 values remained similar for PFPeA and PFHxA** across EBCTs [R13‑E03]. Longer EBCT chiefly affected **shape and overshoot**, not apparent capacity in terms of BVs [R13‑E02, R13‑E03].
- **Contact time dependence can be PFAS‑specific.** Shapiro et al. found that decreasing contact time from 5 to 3 min reduced BV50 for PFOA from ~44,000 to 21,000 and for PFHxS from ~44,000 to 27,000, while many other contaminants showed relatively stable BV50 across 3–10 min [R06‑E06]. For PFOA and PFHxS, **longer contact times allowed much greater treatable bed volumes** before 50% breakthrough [R06‑E06].
- **Full‑scale EBCT not always predictive of capacity changes.** In Kempisty’s full‑scale GAC adsorbers, increasing EBCT from 13 to 26 min **did not consistently change carbon use rates** or adsorption capacity in Minnesota groundwater [R10‑E04, R10‑E07]. This suggests that once EBCT exceeds a certain threshold, other constraints (e.g., pore blocking by DOM) may dominate.
- **Flow‑rate effects in high‑matrix leachate.** Hara et al. operated landfill‑leachate GAC columns at 1.0 and 5.0 mL/min over 0–55 bed volumes and a long‑term run at 5.0 mL/min over 0–1800 BV [R11‑E03]. They report that lower flow (longer contact time) improved removal but note trade‑offs: **reducing flow requires larger reactor volumes or parallel lines** and practical designs must balance performance, energy, and hydraulics [R11‑E08].
- **RSSCT similitude choices.** Park selected the constant‑diffusivity (CD) RSSCT model after showing that PFAS breakthrough on F400 was independent of GAC particle size under their conditions [R13‑E06]. Zeng, by contrast, compared CD and proportional‑diffusivity (PD) RSSCTs and found **CD RSSCTs gave earlier PFAS breakthrough than PD RSSCTs**, implying CD designs are conservative for full‑scale cost estimates [R14‑E06]. Pannu/Murray adopted CD RSSCT for PFAS to be conservative on breakthrough curve shape [R07‑E08].

**Implication for scale‑up:** service‑life claims must specify the **EBCT (or contact time), hydraulic loading rate, and similitude model** and recognize that:

- PFAS of different hydrophobicity and functionality may respond differently to EBCT changes [R13; R06].
- Longer EBCT does *not* universally extend effective bed volumes (e.g., Kempisty’s full‑scale GAC) [R10‑E04, R10‑E07].
- RSSCT EBCTs (seconds) are designed to mirror specific full‑scale EBCTs (minutes) via CD or PD models; using them outside their intended EBCT regime is non‑defensible [R03‑E03; R07‑E08; R13‑E02].

### 3.2 Influent variability and concentration

Influent PFAS concentration and temporal variability strongly affect translation from batch and RSSCT to field:

- **Concentration level:** Ellis highlight that their pilot site’s total PFAS (30–55 μg/L) is “more than 400 times” the former EPA advisory for PFOS+PFOA [R05‑E01]. They note that **other pilots at lower‑concentration sites experienced complete breakthrough after adsorption of much lower total PFAS mass**, underscoring that **capacity in ng PFAS per g media cannot be simply extrapolated across sites with different influent levels** [R05‑E03].
- **Order‑of‑magnitude concentration differences:** Murray’s GW2 groundwater had PFAA concentrations “multiple orders of magnitude higher than GW1” yet similar background water quality; in RSSCTs, **PFAA breakthrough on GAC and IX in GW2 occurred ~3× faster (in bed volumes) than in GW1** [R15‑E07], even though bed design and EBCT were held constant. This is direct evidence that **influent concentration affects bed volumes to breakthrough non‑linearly**.
- **Grab‑sample vs time‑varying feeds:** Zeng’s RSSCTs used single grab samples from six Arizona wells; the authors explicitly note that **RSSCTs operate on a “grab” water sample whereas full‑scale systems see temporal variability in influent quality**, a limitation for direct full‑scale prediction [R14‑E06]. Abulikemu likewise stress that **isotherms done under controlled, static conditions cannot substitute for pilot tests that reflect real source variability** [R01‑E01, R01‑E07].
- **Wastewater NF feed:** Griffin’s NF pilot treated tertiary effluent over >45 days, but PFAS were only periodically spiked during batch rejection tests; the authors acknowledge that **continuous PFAS exposure and adsorption to the membrane were not captured**, and recommend additional work in a continuously PFAS‑impacted stream [R08‑E04, R08‑E05].

**Implication:** claims that a given sorbent will achieve X bed volumes to breakthrough must specify and justify:

- The **PFAS concentration range** and mixture used to generate that BV.
- How **different or variable influent levels** will change loading rate and competitive behavior.
- Whether data come from **steady‑state spikes or time‑varying natural contamination.**

### 3.3 Competing constituents, PFAS mixtures, and chromatographic effects

Virtually all column studies with PFAS mixtures report **competitive effects, displacement, and in many cases, chromatographic overshoot (C/C0 > 1).**

**Competition with NOM and inorganic ions**

- Abulikemu show that **NOM and major ions reduce GAC PFAS capacity through a combination of direct competition and pore blockage**, with larger decreases under NOM pre‑loading vs co‑loading [R01‑E05].
- Murray find that in high‑DOC, high‑anion waters (wastewater, landfill leachate, membrane concentrate), **adsorbent use rates increase and breakthrough accelerates** for all PFAA subclasses (except some long‑chain PFSAs), even for selective SMC and IX [R15‑E03]. This demonstrates that **matrix complexity degrades performance even when lab batch tests in cleaner matrices look promising.**
- Griffin’s NF–adsorbent work is motivated by the observation that **EfOM and co‑adsorbing inorganic ions inhibit PFAS adsorption by GAC and IX**; NF pretreatment is used specifically to lower these nontarget constituents before RSSCTs [R08‑E01, R08‑E08].

**Chromatographic elution and C/C0 > 1**

- Ellis: post‑mortem analysis of AER columns shows **PFSAs and long‑chain PFCAs are concentrated in early sections**, while short‑chain PFCAs are **displaced downstream and into effluent, sometimes to concentrations exceeding influent values** [R05‑E02, R05‑E04].
- Cantoni: in both RSSCTs and full‑scale GAC, **hydrophilic and marginally hydrophobic PFAS showed negative removals (Cout > Cin) due to competitive displacement by hydrophobic PFAS and DOM**, especially on reactivated bituminous AC [R03‑E06, R03‑E08].
- Shapiro: RSSCT breakthrough curves with StyDex show **PFBA reaching C/C0 > 1.2 and pronounced desorption at longer contact times**, increasing with longer contact times and in multisolute mixtures [R06‑E06, R06‑E07].
- Croll: pilot GAC data exhibit **desorption leading to C/C0 > 1** for shorter‑chain PFAS, motivating modified dose‑response models that explicitly handle **chromatographic peaks** [R12‑E06, R12‑E07].
- Hara: full‑scale landfill leachate GAC occasionally shows **negative removal efficiencies**, particularly for some PFAS with irregular behavior; authors warn that fitted parameters for such cases are only reference values [R11‑E04, R11‑E02].
- Murray and Cheng both observe that **short‑chain PFAS break through early and remain in effluent at higher concentrations when long‑chain PFAS are also present**, consistent with competitive displacement by more hydrophobic PFAS [R15‑E03; R04‑E04, R04‑E05].

These findings have two crucial implications:

1. **Single‑solute batch isotherms systematically overstate the security of short‑chain PFAS removal** in columns handling mixtures; they cannot capture displacement and overshoot.
2. **Breakthrough criteria based solely on long‑chain PFAS (or ΣPFAS) can miss periods of elevated short‑chain PFAS exposure.** Croll’s health‑index modeling and the BVMCL approach in Griffin’s work show attempts to address this by integrating multiple PFAS [R08‑E02; R12‑E02].

---

## 4. When and how batch results can inform column and full‑scale performance

Despite these limitations, several studies show **conditional, empirical linkages** between batch metrics and column behavior.

### 4.1 Empirical correlations between batch affinity and BV50/BV10

- **Ellis et al. (AERs, groundwater):** For each PFAS–resin pair, the authors correlate **50% breakthrough bed volumes** with **batch‑derived PFAS–Cl⁻ exchange coefficients (log Kex)** and find reasonably strong linear relationships for the single‑use resins [R05‑E06]. They propose that **field performance of new resins might be “roughly estimated” from batch log Kex plus existing pilot data**, but explicitly state that **these correlations require further validation before being used for new resins** [R05‑E06].
- **Park et al. (GAC, groundwater):** For F400 GAC, **BV50 correlates monotonically with PFAS Log Dow at pH 7**, indicating that **hydrophobicity is the primary factor controlling apparent BV‑based capacity** under their conditions [R13‑E02, R13‑E04]. An empirical equation for BV10 is derived, which could be used to predict early breakthrough for untested PFAS of known Log Dow, *within* the tested system [R13‑E02].
- **Hara et al. (GAC, landfill leachate):** In columns with actual leachate, **BV50 correlates strongly with log D (distribution coefficient) for nine PFAS (r = 0.94)**, with r = 0.97 within PFCA and PFSA subgroups [R11‑E07]. This reinforces that **hydrophobicity is a robust predictor of relative breakthrough order** in that high‑DOC leachate system.
- **Cantoni et al. (GAC, drinking water):** Batch Freundlich KF and RSSCT BV50 values consistently favor **positively charged ACs** over neutral AC, and microporous vs mesoporous performance shifts with PFAS hydrophobicity [R03‑E02, R03‑E06]. The same AC ranking is observed in full‑scale GAC adsorbers for hydrophilic and marginally hydrophobic PFAS [R03‑E06, R03‑E08].

These relationships show that **batch affinity metrics (Kd, KF, log Kex, log Dow/log D) can reliably indicate:**

- Which PFAS will **break through first vs last** in a given medium.
- Which adsorbent is **likely to outperform another under similar hydraulic and matrix conditions.**

However, even in these best‑case examples, authors do *not* claim that batch parameters alone can specify **absolute bed volumes** or **media life** without model‑based or pilot‑based calibration.

### 4.2 Batch‑calibrated column models

- Xiao et al. calibrate an intraparticle diffusion‑limited GAC model using batch Kd and kinetic data for a suite of AFFF‑derived PFAS, then simulate a **real full‑scale GAC system (two 28.5 m³ vessels in series at 1.5 m³/min, 2.7‑m bed depth)** [R02‑E02]. The model produces **predicted bed volumes to breakthrough** and breakthrough orders consistent with prior column observations for most PFAS [R02‑E01, R02‑E02]. Still, the authors frame this as qualitative—**forward modeling provides insight but requires pilot verification** [R02‑E08].
- Abulikemu recommend using **batch isotherms plus modeling tools like AdDesignS** to relate isotherm parameters to breakthrough in full or pilot GAC systems [R01‑E05], and encourage combining such modeling with RSSCT or pilot tests to improve accuracy [R01‑E06].
- Shapiro fit Thomas models to StyDex RSSCT data to derive column capacities (qm) and compare them to batch kinetic constants; hydrophobicity trends matched, but **batch kinetics still did not predict column breakthrough quantitatively** [R06‑E07, R06‑E02].

In all cases, **a calibrated transport model plus site‑specific column data is needed to move from batch capacity to service‑life estimates**.

### 4.3 Cross‑scale validation of RSSCTs against pilot and full‑scale

Though RSSCTs are not batch tests, they are a common **intermediate scale used with batch data**. The evidence on their predictive quality is mixed but informative.

- **Kempisty et al. (PD‑RSSCT vs full‑scale/pilot GAC):**
  - For Minnesota groundwater, PD‑RSSCTs **overpredicted full‑scale bed volumes to 10% and 50% PFAA breakthrough by an average factor of 1.7 (range 1.4–2.0)** [R10‑E02]. The leading hypothesis is **pore blockage by DOM near the external surface in larger full‑scale particles**, which RSSCTs with crushed GAC do not fully capture [R10‑E02].
  - For North Carolina surface water, **PD‑RSSCTs matched pilot‑scale breakthrough more closely** than in groundwater [R10‑E01], but the extracted text does not quantify prediction errors.
- **Pannu/Murray (CD‑RSSCT vs pilot for GACs and FS200):**
  - For multiple GACs treating a given groundwater, **RSSCT‑predicted media life at BV60% agreed well with pilot‑scale breakthrough**, and initial breakthrough was conservatively early in RSSCTs [R07‑E04, R07‑E05].
  - For the alumina‑based FS200, **RSSCT “predicted a much larger media life” at BV60% than observed in the pilot**, i.e., RSSCT was *non‑conservative*; the authors call for further work to assess CD‑RSSCT applicability and Thomas‑model assumptions for this adsorbent [R07‑E05].
- **Cantoni et al. (CD‑RSSCT vs full‑scale GAC):** RSSCT BV50 values and shape of chromatographic effects matched full‑scale GAC behavior; **median full‑scale removals and estimated solid‑phase loadings were in “overall agreement” with RSSCT‑derived capacities** [R03‑E05, R03‑E08].
- **Zeng et al. (CD vs PD RSSCT, no full‑scale):** CD‑RSSCTs gave **earlier breakthrough** than PD, and the authors recommend CD design as conservative for full‑scale cost estimation [R14‑E06].
- **Griffin et al.:** adopt CD RSSCTs for GAC and IX on wastewater effluent and NF permeate, noting that **RSSCT breakthrough data have been shown to be representative of pilot performance in the literature** and are more practical than pilots for multiple feedwaters [R08‑E06].

The overall pattern:

- **RSSCTs can be reasonably predictive for PFAS on GAC and some IX resins when similitude is well chosen and DOM effects are modest** [R03; R14; R08; R10].
- **They can fail badly for alternative media (FS200) or for matrices with strong particle‑size‑dependent fouling**, unless calibrated with pilot data [R07; R10].

---

## 5. When batch results *do not* predict column or field performance

The strongest cautionary examples include:

- **Capacity–breakthrough disconnect (PFOS on AERs).** Ellis shows that a resin with **>4× batch PFOS capacity** does *not* yield meaningfully longer bed volumes to PFOS breakthrough than two lower‑capacity resins under identical pilot conditions, making it explicit that **maximum batch capacity is not a predictor of continuous‑flow PFAS removal** [R05‑E03].
- **NOM and contact‑time dependence (A860 vs polystyrene AERs).** The polyacrylic A860 performed well in batch and some bench studies at higher NOM and longer contact times, but **showed <1,000 BVs of PFOS removal (near‑immediate breakthrough)** in the field pilot at 30‑s EBCT, whereas four polystyrene AERs removed PFSAs through ≥40,000 BVs with PFOS removed through ≥75,000 BVs [R05‑E05]. This is a direct demonstration that **favorable batch results at long contact time in different NOM conditions can be misleading for field designs.**
- **IAST failure for PFAS mixtures.** Abulikemu systematically tested IAST for PFAS mixtures with and without NOM and conclude that **IAST “performed poorly” and can become insensitive for trace PFAS**, such that even large changes in PFAS concentration produce negligible modeled changes [R01‑E02, R01‑E07]. Using IAST as currently implemented can yield **significant errors in predicted GAC performance from batch data** [R01‑E07].
- **Short‑chain PFAS behavior and chromatographic overshoot.** Cantoni, Ellis, Shapiro, Croll, Hara, and Cheng all report **chromatographic peaks and negative removals** for hydrophilic PFAS in columns and full‑scale systems that are not anticipated by single‑solute batch isotherms [R05‑E02; R03‑E06, R03‑E08; R06‑E06, R06‑E07; R12‑E06, R12‑E07; R11‑E04; R04‑E04]. **Batch isotherms cannot capture these dynamic, competitive displacement phenomena.**
- **Mismatch of batch kinetics vs column breakthrough.** StyDex batch kinetics, although rapid, did **not produce kinetic constants that matched RSSCT breakthrough**; even when basic hydrophobicity ranking carried over, quantitative predictions failed [R06‑E02].
- **RSSCT mis‑predicting alternative adsorbent life.** FS200’s RSSCT‑predicted BV60% media life was **much larger than pilot‑scale reality**, in contrast to the conservative behavior for GACs [R07‑E05]. This shows that **even column‑scale lab tests calibrated on batch isotherms can mispredict media life if transport assumptions do not match the actual sorbent.**

---

## 6. Minimum evidence for a defensible service‑life or scale‑up claim

Drawing on the above, a **defensible claim** that “sorbent X will achieve Y bed volumes (or Z years) of PFAS treatment” at full or pilot scale must be grounded in more than batch capacity or short‑time kinetics. At minimum, evidence should include:

### 6.1 Representative hydraulics and breakthrough metrics

1. **Column data (RSSCT, pilot, or full‑scale) for the same or a closely matching matrix and sorbent**, reporting:
   - **EBCT or contact time** (e.g., Ellis 30‑s EBCT, 2‑min dual‑vessel; Park 5–20 min EBCTLC; McCleaf 6.1 min GAC, 4.9 min AE; Kempisty 13 vs 26 min EBCT; Shapiro 3–10 min CTLC) [R05‑E07; R13‑E03; R09‑E03; R10‑E03; R06‑E03, R06‑E06].
   - **Hydraulic loading rate or flow per bed cross‑section** where relevant (e.g., Park 3.8 m/h; Kempisty ~12 m/h) [R13‑E01; R10‑E03].
   - **Breakthrough criterion** (e.g., C/C0 = 0.1, BV10, BV50, BV60%, BVMCL) and **bed volumes to that criterion** [R03‑E05; R07‑E02; R08‑E02; R12‑E02; R11‑E07; R10‑E04; R09‑E02].

2. For **RSSCT‑based predictions**, **clear declaration of the similitude model (CD vs PD) and target full‑scale EBCT**, with at least **one validation data set**:
   - Kempisty’s PD‑RSSCT vs full‑scale GW showing a consistent 1.4–2.0× overprediction [R10‑E02].
   - Pannu/Murray’s CD‑RSSCT vs pilot GAC showing good match at BV60% [R07‑E04, R07‑E05].
   - Cantoni’s CD‑RSSCT vs full‑scale GAC showing consistent BV50–capacity alignment [R03‑E05, R03‑E08].

Without such column data and model calibration, a service‑life claim cannot be considered robust.

### 6.2 Matrix and influent characterization

3. **Influent PFAS mixture and concentration range**:
   - Specified PFAS (e.g., PFOS, PFOA, PFHxS, PFBA, PFBS, GenX) and whether they are present as a **mixture** at trace ng/L or μg/L levels [R05‑E01; R03‑E02; R14‑E02; R15‑E01; R06‑E04; R08‑E01; R11‑E01; R09‑E03].
   - Typical **concentration ranges** (e.g., Zeng’s ΣPFAS 156–7,044 ng/L; Murray’s GW1 vs GW2 with order‑of‑magnitude differences; Ellis’s 30–55 μg/L AFFF‑impacted groundwater) [R14‑E02; R15‑E01, R15‑E07; R05‑E01].

4. **Competing constituents and matrix characteristics**:
   - **DOC/TOC levels** and type (e.g., 0.7 mg/L in MN GW vs 2.0–2.7 mg/L in NC SW; 58.63 mg/L DOC in landfill column influent vs 4.39 mg/L in full‑scale landfill leachate; elevated EfOM in wastewater) [R10‑E04, R10‑E07; R11‑E05; R08‑E01].
   - **Major anions and ionic strength** when shown to influence competition (e.g., Murray’s finding that high anions plus DOC in wastewater/landfill leachate accelerate breakthrough even for SMC and IX) [R15‑E03].
   - Whether **NOM or other organics were pre‑loaded or co‑loaded** (e.g., Abulikemu’s NOM pre‑loading vs co‑loading; McCleaf’s two‑phase behavior possibly tied to DOC loading and PFAS agglomeration) [R01‑E05; R09‑E04, R09‑E06].

A claim that omits DOC, background ions, or co‑contaminants is incomplete, because these constituents demonstrably alter capacity and breakthrough across scales.

### 6.3 Role of batch data: comparative, not determinative

5. **Batch isotherm or kinetic data in the *same or similar matrix***, used to:

   - Rank sorbents or PFAS by affinity (e.g., Ellis’s log Kex; Park’s BV50 vs Log Dow; Hara’s BV50 vs log D; Cheng’s Kd ranking of BIPGEM components) [R05‑E06; R13‑E02, R13‑E04; R11‑E07; R04‑E06, R04‑E08].
   - Parametrize a **column or full‑scale model** that is then validated against column data (e.g., Xiao’s GAC model, Abulikemu’s envisioned AdDesignS use) [R02‑E02; R01‑E05].

However, **batch data must be clearly identified as supportive or comparative, not as direct evidence of bed volumes or field lifetime.** The Ellis, Abulikemu, Xiao, Shapiro, and Cantoni studies all explicitly or implicitly make this distinction [R05‑E03; R01‑E05, R01‑E07; R02‑E02, R02‑E08; R06‑E02; R03‑E01].

### 6.4 Demonstration of competitive and non‑ideal behavior

6. At least one of the following should be addressed in the evidence base:

   - **Short‑chain PFAS breakthrough and potential C/C0 > 1** under multisolute conditions, or justification for why competition is minimal (e.g., single‑PFAS applications) [R05‑E02; R03‑E06, R03‑E08; R06‑E06; R12‑E06; R11‑E04; R04‑E04].
   - **Effect of EBCT and flow on breakthrough curve shape and overshoot**; for example, Park’s EBCT dependency and Shapiro’s contact‑time dependence [R13‑E03; R06‑E06].
   - **Evidence that the chosen similitude model (CD or PD) adequately reflects intraparticle diffusion and pore blocking** for the sorbent and matrix of interest (e.g., Park’s particle‑size independence; Kempisty’s pore‑blocking hypothesis and quantified overprediction factor; Pannu’s FS200 mismatch) [R13‑E06; R10‑E02; R07‑E05].

Ignoring these real non‑idealities and simply scaling batch Kd or qmax to “design bed volumes” would be inconsistent with the collected evidence.

---

## 7. Synthesis: When batch adsorption does and does not predict real‑system PFAS performance

**Batch adsorption results are most predictive when:**

- They are **performed in a matrix similar to the target water**, including PFAS mixtures and relevant DOC/ions [R03‑E01; R01‑E07; R02‑E05].
- They are used to derive **relative affinity rankings** (which PFAS and which sorbents are strongest) and those rankings are then **validated against column BV50/BV10** (Ellis, Park, Hara) [R05‑E06; R13‑E02, R13‑E04; R11‑E07].
- A **column model calibrated on batch data** is used to reproduce and interpret actual breakthrough curves from RSSCT, pilot, or full‑scale systems (Xiao, Abulikemu, Shapiro) [R02‑E02, R02‑E08; R01‑E05; R06‑E07].
- The goal is **screening and ranking** or **approximate prediction of breakthrough order and relative capacities**, not exact media life.

**Batch adsorption results do *not* reliably predict pilot or full‑scale service life when:**

- They are used **without column data**, or without specifying EBCT, flow, influent PFAS concentrations, and matrix composition.
- They are conducted under **single‑solite or very clean conditions** that do not reflect multisolute competitive displacement, DOC and ion competition, or time‑varying influent.
- They are interpreted as **direct surrogates for bed volumes to breakthrough or years of operation**—a practice that Ellis, Abulikemu, Xiao, Shapiro, Cantoni, Kempisty, and others collectively contradict.

In practice, **robust scale‑up relies on an integrated evidence chain**:

1. **Batch isotherms and kinetics** for sorbent and PFAS mixtures in representative water to understand affinity, capacity, and key competitors [R03; R01; R02; R04].
2. **RSSCT or pilot column tests** under realistic EBCT and quality conditions to generate breakthrough curves and BV‑based metrics [R05; R03; R14; R07; R13; R15; R06; R08; R12; R11; R10; R09].
3. **Validated models** that link batch and column data and can be used to interpolate within this space, with due acknowledgment of uncertainties and matrix specificity.

Designers and regulators should treat **claims based solely on batch capacity or on unvalidated RSSCTs for novel adsorbents as provisional at best**, and insist on explicit reporting of EBCT, flow, influent variability, competing constituents, PFAS mixture, and breakthrough definitions when evaluating service‑life or scale‑up claims.

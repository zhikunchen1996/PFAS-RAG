### Overview

Evidence across the table shows that batch adsorption tests (equilibrium isotherms and short-term kinetics) are useful for **qualitative insight**—e.g., chain‑length trends and relative media affinity—but are **not sufficient on their own** to predict fixed‑bed breakthrough, bed volumes treated, or full‑scale media lifetime. Column‑scale evidence (RSSCTs, pilot, full‑scale) and modeling studies repeatedly demonstrate that hydrodynamics, mass transfer, background water quality, and PFAS mixtures cause systematic deviations between batch expectations and actual service life.

Below I synthesize what each type of metric tells us, how operating and water‑quality factors affect translation across scales, and what minimum evidence is needed to make defensible service‑life or scale‑up claims.

---

## 1. Information content of different performance metrics

### 1.1 Batch equilibrium capacity and selectivity

**What it captures**

- Fatima et al. conducted batch kinetic/isotherm tests for five PFAS and fit pseudo‑first‑order (PFO) and pseudo‑second‑order (PSO) models, with higher R² for PSO (0.92 vs 0.88), and used these batch results to infer sorption behavior and isotherm‑based predictions [WEB01].  
- In the ion‑exchange space, Cheng & Meng developed an uptake capacity parameter \(K_{IX}\) for 23 PFAS in fixed‑bed ion‑exchange resins, as a function of PFAS structure and background matrix constituents [WEB05]. A QSPR model predicted \(K_{IX}\) from normalized chain length (NCL) [WEB05].  
- Smith et al. compared pilot‑scale ion‑exchange elution order to **previously reported batch‑derived selectivity coefficients \(K_{x/Cl}\)** and found general agreement in which PFAS eluted first vs later [WEB06].

Across these studies, equilibrium/affinity metrics:

- Capture **relative selectivity and chain‑length trends**:
  - GAC and anion exchange show preferential removal of longer‑chain PFAS and sulfonates in full‑scale systems [WEB10, WEB11].
  - AER outperformed GAC for all PFAS in Fatima et al.’s study, consistent with higher affinity in batch [WEB01].
  - The order of breakthrough in the full‑scale GAC plant (PFBA < PFPeA < PFHxA < PFBS < PFOA) [WEB11] is consistent with higher affinity for longer chains and sulfonates, which mirrors batch selectivity patterns.

**Where it falls short**

Two independent lines of evidence show that equilibrium/selectivity information is **not enough to predict time‑to‑breakthrough or bed volumes**:

- **Underprediction of column service life from isotherms**  
  Fatima et al. report that isotherm‑based predictions captured chain‑length trends but **underpredicted the actual service life** of the fixed‑bed continuous‑flow columns [WEB01]. This shows that even reasonably fit isotherms and kinetic models did not translate quantitatively into column lifetime for those PFAS and media.

- **Mismatch between batch selectivity and BV10**  
  In pilot ion‑exchange columns, Smith et al. found that elution order generally matched batch‑derived \(K_{x/Cl}\), but **bed volumes to early breakthrough (BV10) deviated for some PFAS**, with deviations attributed to **molecular size‑exclusion kinetic limitations** [WEB06]. That is, batch affinity identified which PFAS would be weakly vs strongly retained, but **did not correctly predict how soon 10% breakthrough occurred.**

Collectively, these studies indicate: **batch equilibrium capacity and selectivity can identify promising media and rank PFAS qualitatively but should not be treated as direct predictors of breakthrough time, bed volumes treated, or service life.**

### 1.2 Batch or short‑term kinetic tests

Batch kinetics can reveal whether uptake is rapid and whether intra‑particle diffusion or film diffusion might limit rates:

- Fatima et al. used PFO and PSO fits to infer a chemisorption‑dominated mechanism [WEB01].
- Fagbayigbo’s fixed‑bed study of PFOA and PFOS on leaf biomass interprets steeper breakthrough curves at higher flow as indicating a short mass‑transfer zone and **intra‑particle diffusion control** of adsorption in the fixed bed [WEB07].
- For ion exchange, Cheng & Knappe highlight that PFAS uptake capacity depends on **Sherwood number and particle shape factor**, and that **film diffusion plays an important role in controlling uptake rates** [WEB04].

These results show that kinetic parameters (and qualitative assessments of rate limitation) are essential for designing contact times and understanding media utilization. However:

- The **Fatima** study still found that isotherm‑plus‑kinetics predictions **underpredicted column service life** [WEB01], reinforcing that even good kinetic fits in batch are insufficient to forecast breakthrough without explicit fixed‑bed hydrodynamics and competitive effects.
- Fagbayigbo and de Araujo et al. rely on column kinetic models (Bohart–Adams, Thomas, Yoon–Nelson) to fit breakthrough [WEB07, WEB08], but these are again **column metrics**, not batch; they require breakthrough data.

So, **short kinetic tests without column geometry and flow do not define service life**.

### 1.3 Fixed‑bed breakthrough metrics

Fixed‑bed columns—RSSCTs, pilot, and full‑scale—report performance via **breakthrough curves (C/Co vs time or bed volumes)** and derived metrics like BV10, BV50, BV80, and carbon use rate.

Key examples:

- **BV‑based metrics**
  - Hopkins & Knappe used RSSCTs to predict **BV50** (bed volumes at 50% breakthrough) in pilot GAC adsorbers. Constant‑diffusivity RSSCTs predicted BV50 reasonably, whereas proportional‑diffusivity designs **overpredicted BV50 by about 2–3×** [WEB03].  
  - Zhang et al. report **BV to 10%, 50%, and 80% breakthrough for PFOA** in an RSSCT simulating a PFA694E bed fed with untreated fluorochemical wastewater (0.39×10³, 0.54×10³, and 0.66×10³ BV, respectively) [WEB13]. In a simulated solution, BV80 was about 15×10³ BV, much larger than in the complex wastewater [WEB13].
  - de Araujo et al. show PFBS and PFOS breakthrough curves in fixed‑bed APTES‑modified diatomite columns in which **none of the systems reached full bed saturation (Ct/Co = 1) during the test duration** [WEB08]. This means that **complete breakthrough and media lifetime were not observed**; lifetime must be extrapolated or tested longer.

- **Early breakthrough (BV10) and chain‑length effects**  
  - Smith et al. explicitly discuss **bed volumes to BV10** as an early breakthrough measure in pilot ion‑exchange columns operated at EBCTs of 0.5–2.5 min [WEB06].  
  - In the full‑scale GAC plant in Italy, **treated bed volumes at complete breakthrough (saturation)** ranged from 7,100 for PFBA to 50,900 for PFOA [WEB11]. This is a true **lifetime metric** for those operating conditions.

- **Percent breakthrough vs bed volumes across media**  
  - Tisler et al. report that five GACs and one ion‑exchange resin treating groundwater all had **<6% breakthrough for all detected features at <3,200 bed volumes**, while for a micro‑granular activated carbon (µGAC) material, breakthrough increased to 79% after 69,000 bed volumes and seven months of operation [WEB09]. For the shortest PFAS (PFBA and PFPeA), **most media broke through completely**, except a proprietary blended GAC with only 19% PFPeA breakthrough at 15,700 bed volumes [WEB09].

These BV‑based metrics are explicitly **column‑ and condition‑specific**. They are the direct basis for:

- **Service‑life definitions** (e.g., BV10 or BV50 as replacement criteria).
- **Carbon use rate metrics**, such as the feasibility criterion of **<25 mg GAC L⁻¹ treated** used by Kempisty et al. for ground and surface waters [WEB02].

### 1.4 Media lifetime and capacity at saturation

Full‑scale and long‑running pilot studies provide the clearest evidence on **media lifetime**:

- **Full‑scale GAC plant (Italy)**  
  Bertanza et al. calculated **PFAS adsorption capacity of GAC at complete breakthrough (saturation)** in a full‑scale groundwater plant, reporting capacities of 1.71 g/t for PFBA and 24.6 g/t for PFOA, and **treated bed volumes at saturation of 7,100 (PFBA) to 50,900 (PFOA)** [WEB11]. These are **true operational capacities and lifetimes**, integrating real flow regimes, low TOC (mostly <0.5 mg/L), and a mixed PFAS suite.

- **Pilot GAC and ion‑exchange filters (groundwater)**  
  Tisler et al. tracked breakthrough over up to 69,000 BV, revealing strong **short‑chain PFAS limitations and media‑specific BV behavior** [WEB09].

- **Ion‑exchange pilot columns**  
  Smith et al. did not report absolute lifetimes, but their BV10 data at multiple EBCTs and NOM conditions, coupled with fitted mass transfer and diffusion parameters, provide a basis for **predictive lifetime modeling** under similar conditions [WEB06].

By contrast, most batch studies lack any time‑integrated lifetime metric. The Bertanza full‑scale data demonstrate that a meaningful “capacity” for design is **column capacity at a defined breakthrough**, not equilibrium capacity from a batch suspension.

---

## 2. How operating conditions and water quality control scale‑translation

### 2.1 Flow rate and contact time

**Empty‑bed contact time (EBCT) and flow strongly control breakthrough, independent of batch capacity.**

- **Ion exchange pilot columns (Smith et al.)**  
  Four EBCTs (0.5, 1.0, 1.5, 2.5 min) were tested [WEB06]. Although detailed BV10 values are not given in the table, the study uses these EBCT variations to fit mass transfer coefficients \(k_L\) and intraparticle diffusion coefficients \(D_s\), showing that **hydraulics and film diffusion significantly influence breakthrough**, beyond equilibrium selectivity [WEB06].

- **APTES‑modified diatomite columns**  
  de Araujo et al. explicitly vary **bed height and flow rate**, demonstrating that optimizing both is essential to improve adsorption efficiency, particularly for short‑chain PFBS [WEB08]. Steeper or shallower breakthrough curves under different flows reflect changes in **mass‑transfer zone length**.

- **Leaf‑biomass fixed‑bed (Fagbayigbo)**  
  The authors note that flow rate affects breakthrough‑curve steepness and that shorter mass‑transfer zones under certain conditions imply intra‑particle diffusion control [WEB07]. Again, kinetics and hydrodynamics, not just capacity, dictate how quickly breakthrough is reached.

Take‑home: **equilibrium capacity does not incorporate EBCT or flow**. Predictive translation across scales must explicitly account for these factors via column models or empirically calibrated RSSCTs.

### 2.2 Scale effects: RSSCTs, bench, pilot, and full‑scale

**Rapid small‑scale column tests (RSSCTs)** are specifically designed to accelerate column experiments while preserving similarity:

- **GAC – PFAS in surface water and groundwater (Hopkins; Kempisty; Schaefer)**  
  - Hopkins & Knappe show that **constant‑diffusivity RSSCTs** predict pilot‑scale BV50 for 7–11 PFAS per column, whereas **proportional‑diffusivity designs overpredict BV50 by ~2–3×** [WEB03]. This demonstrates that **choice of scale‑up protocol itself affects lifetime prediction**, even with the same batch and media properties.  
  - Kempisty et al. applied **proportional‑diffusivity RSSCTs** to evaluate whether bench‑scale tests can predict pilot/full‑scale GAC performance and interpreted feasibility via a **carbon‑use‑rate threshold of <25 mg GAC L⁻¹ treated** [WEB02]. While specific BV and breakthrough criteria are not in the abstract, the study treats RSSCT‑derived carbon use rates as proxies for longer‑scale performance.  
  - Schaefer et al. used RSSCTs with ground media and compared them to bench‑scale columns with ground and unground AERs and GACs in high‑organic‑carbon groundwater. PFAA migration through both AER and GAC columns was **well described by the Thomas model and a constant‑diffusivity transport model** [WEB12]. This supports the idea that **properly designed RSSCTs can mimic larger columns**, but only when hydrodynamic and mass transfer scaling are respected.

- **Ion exchange – PFAS (Cheng & Knappe; Cheng & Meng)**  
  - Cheng & Knappe use RSSCT data to scale to pilot/full‑scale packed‑bed ion‑exchange contactors. Highlights state that **PFAS breakthrough curves were independent of influent PFAS concentration** in the tested systems and that uptake depends on Sherwood number and particle shape factor, with film diffusion important [WEB04].  
  - Cheng & Meng conducted rapid small‑scale fixed‑bed tests with two resins and 18 water matrices, developing **pseudo‑single‑solute models** that predict PFAS breakthrough in fixed beds from **NCL and influent TOC and nitrate** [WEB05]. These models transform batch‑like structure–property insights into actual fixed‑bed performance predictions under explicitly defined hydraulic and water‑quality conditions.

- **Industrial wastewater RSSCT (Zhang et al.)**  
  Zhang et al. use constant‑diffusivity RSSCTs to simulate a full‑scale PFA694E bed. They report BV80 for PFOA of approximately 15×10³ BV in a **simulated solution**, but only about 0.66×10³ BV to 80% breakthrough when fed **untreated fluorochemical wastewater** [WEB13]. The nearly **order‑of‑magnitude difference in BV80 between clean and complex matrices**—with identical resin and design method—shows that **scaling from idealized batch or simple matrices to real wastewaters is risky without explicit column testing under representative conditions.**

- **Full‑scale GAC and pilot filters (Bertanza; Tisler; Appleman)**  
  - Bertanza et al. provide full‑scale capacities and bed volumes at saturation for several PFAS in low‑TOC groundwater [WEB11].  
  - Tisler et al. report pilot‑scale breakthrough of PFAS in groundwater for five GACs and one resin, highlighting early and near‑complete breakthrough of the shortest PFAS (PFBA, PFPeA) on most media [WEB09].  
  - Appleman et al. show that in U.S. full‑scale systems, **anion exchange and GAC preferentially removed longer‑chain PFAS and PFSAs compared to PFCAs**, while many conventional processes were mostly ineffective [WEB10].

Across these datasets, **RSSCTs and bench columns are effective bridges between batch and pilot/full‑scale** when:

- The RSSCT design (constant vs proportional diffusivity) is validated against pilot/full‑scale breakthrough for the same media and matrix [WEB03, WEB12].
- Breakthrough endpoints (e.g., BV50, BV80, BV10, or carbon use rate thresholds) are clearly defined and consistently applied [WEB02, WEB03, WEB11, WEB13].

### 2.3 Influent variability, NOM, and competing constituents

The table provides several clear examples of **matrix effects** undermining direct translation from batch:

- **NOM and anions in ion exchange columns (Smith; Cheng & Meng)**  
  - Smith et al. deliberately compare PFAS breakthrough in pilot ion‑exchange columns **with and without added reconstituted Ohio River NOM**, using the same EBCT range [WEB06]. While elution order follows batch selectivity, NOM and kinetic size‑exclusion effects cause deviations in BV10 [WEB06].  
  - Cheng & Meng’s models use **influent total organic carbon and nitrate concentration** along with NCL as inputs to predict PFAS breakthrough [WEB05]. They derived these relationships from 18 water matrices with varied DOM and major anions (bicarbonate, chloride, sulfate, nitrate) [WEB05]. This explicitly embeds background water composition into fixed‑bed predictions—something equilibrium batch tests in a single matrix cannot provide.

- **Organic carbon effects in GAC and AER columns (Schaefer; Hopkins; Bertanza)**  
  - Schaefer et al. worked in groundwater with **elevated naturally occurring organic carbon**, and their modeling of PFAA transport via Thomas and constant‑diffusivity models reflects that context [WEB12].  
  - Hopkins and Knappe’s pilot GAC adsorbers were fed **coagulated/settled surface water with TOC = 2.3 mg/L** [WEB03], so predictive performance of RSSCTs is anchored to that NOM level.  
  - Bertanza’s full‑scale groundwater plant had low TOC (<0.5 mg/L) [WEB11], likely contributing to the relatively high BV at saturation for longer‑chain PFAS.

- **Industrial wastewater vs simulated solution (Zhang)**  
  For PFOA, BV80 in a clean simulated solution (~15×10³ BV) dropped to 0.66×10³ BV in untreated fluorochemical wastewater [WEB13]—a **>20‑fold decrease**. The difference is attributable to **co‑contaminants, high PFAS load, and matrix complexity**, none of which are resolved in simple batch tests.

These studies collectively show that **NOM, major anions, and broader co‑contaminant suites strongly modify effective capacity and breakthrough**. Batch tests in distilled or single‑salt solutions cannot be extrapolated to real waters without incorporating these matrix effects via models or validated column data.

### 2.4 PFAS mixtures and competitive uptake

Most column and full‑scale systems treat **PFAS mixtures**, not single compounds:

- The Bertanza full‑scale plant handled multiple PFCA and PFSA species simultaneously, with breakthrough ordered by chain length and headgroup [WEB11].
- Tisler et al. evaluated a broad set of contaminants including PFAS, reporting specific behavior for PFBA and PFPeA within a mixture [WEB09].
- Hopkins’s pilot GAC columns had **7–11 PFAS breakthrough curves per column** [WEB03]; Zhang’s treatment train tracked 107 PFAS and TOF [WEB13].

Cheng & Meng’s 23‑PFAS dataset and pseudo‑single‑solute models implicitly **bundle competitive effects into an effective capacity parameter \(K_{IX}\)** that is calibrated under multi‑PFAS conditions and multiple background matrices [WEB05]. This is more realistic than single‑PFAS batch isotherms, but still requires validation in true multicomponent fixed beds.

The practical implication is that **mixture behavior can’t be deduced from single‑PFAS batch isotherms**; we need either:

- Multi‑PFAS batch tests in representative matrices; or
- Column tests (RSSCT, pilot) under realistic mixtures, with explicit breakthrough statistics for each PFAS, as in Hopkins [WEB03], Tisler [WEB09], Bertanza [WEB11], Zhang [WEB13].

---

## 3. When batch results *do* and *do not* predict column or field performance

### 3.1 Situations where batch is qualitatively predictive

The evidence supports several **qualitative, not quantitative** uses of batch data:

1. **Ranking media and PFAS by affinity**
   - AER vs GAC: Fatima et al. report that **AER consistently outperformed GAC** for all five PFAS in column tests [WEB01], consistent with higher affinity expected from batch behavior.  
   - Full‑scale data (Appleman; Bertanza; Tisler) show that longer‑chain PFAS and PFSAs are preferentially removed by both GAC and anion exchange [WEB10, WEB11, WEB09], aligning with chain‑length and headgroup trends from batch.

2. **Predicting elution order (but not BV)**
   - In Smith et al., **pilot column elution order generally matched batch‑derived \(K_{x/Cl}\)** [WEB06], indicating that batch selectivity is informative about which PFAS will break through first.

3. **Capturing chain‑length trends**
   - Fatima et al. explicitly note that **isotherm predictions reproduced chain‑length dependent trends observed in columns**, even though they underpredicted service life [WEB01].  
   - Cheng & Meng’s NCL‑based QSPR for \(K_{IX}\) and subsequent breakthrough models show that normalized chain length is a key predictor of relative capacity and breakthrough behavior across PFAS [WEB05].

These are **appropriate uses of batch/isotherm information**: screening media, selecting promising technologies, and anticipating which PFAS are likely to be limiting.

### 3.2 Situations where batch fails or is unsafe to extrapolate

The table points to multiple systematic failures when batch or short kinetic tests were treated as though they directly defined column performance:

- **Underestimated service life from isotherms**  
  - Fatima et al. specifically report that **batch isotherm‑based predictions underpredicted the service life of fixed‑bed continuous‑flow columns** [WEB01]. Relying on such predictions to size full‑scale units would have produced overly conservative designs in that case; in other systems, the bias could go the other way.

- **Batch selectivity vs BV10 mismatch**  
  - Smith et al. found meaningful **deviations between batch‑derived selectivity coefficients and BV10 values** in pilot ion‑exchange columns, due to **kinetic and size‑exclusion effects** [WEB06]. Thus, batch selectivity alone did not capture the rate at which columns exhausted for individual PFAS.

- **Matrix‑induced collapse of BV80**  
  - Zhang et al. show that PFOA BV80 fell from ~15×10³ BV in a simple simulated solution to 0.66×10³ BV in real fluorochemical wastewater [WEB13]. Any design based solely on clean‑matrix batch or column data would dramatically overpredict service life in this wastewater.

- **Dominance of batch literature vs limited column data**  
  - de Araujo et al. explicitly state that **most PFAS removal data are from batch adsorption experiments**, with limited fixed‑bed column data that better reflect practical treatment [WEB08]. Their own columns did not reach saturation within test duration, underlining how long‑term breakthrough behavior is largely unknown for many new media.

Given these findings, **presenting batch capacity or short kinetic performance as direct evidence of column breakthrough or field lifetime would violate the evidentiary record** in this corpus.

---

## 4. Minimum evidence needed for defensible service‑life or scale‑up claims

Drawing on the cross‑study evidence, a **defensible claim** about PFAS service life or scale‑up (e.g., “X bed volumes to BV10 for PFOA at full scale” or “RSSCT predicts pilot BV50 within a factor Y”) requires, at minimum, the following elements.

### 4.1 For fixed‑bed performance claims at any scale

To support a claim about **service life or breakthrough behavior** of a given system, the record should provide:

1. **Breakthrough endpoint and definition**
   - Clear statement of the **breakthrough criterion** (e.g., BV10, BV50, BV80, complete saturation).  
     - Examples: BV50 in Hopkins [WEB03]; BV10 in Smith [WEB06]; BV80 in Zhang [WEB13]; complete saturation in Bertanza [WEB11].

2. **Bed volumes or time to that breakpoint**
   - The **bed volumes treated** or filter runtime corresponding to the chosen breakthrough percentage.  
     - Examples: 7,100–50,900 BV at saturation for PFBA–PFOA [WEB11]; 0.39×10³–0.66×10³ BV to 10–80% PFOA breakthrough in wastewater [WEB13]; 15,700 BV at 19% PFPeA breakthrough in pilot GAC [WEB09].

3. **Hydraulic conditions**
   - Either EBCT (min) or flow rate and bed dimensions sufficient to compute EBCT.  
     - Smith provides EBCTs (0.5–2.5 min) [WEB06]; Hopkins reports two EBCTs at pilot scale [WEB03] (values not in table, but the multiplicity is).  
   - Evidence from this review shows that **different EBCTs materially affect breakthrough and mass transfer coefficients** [WEB06, WEB07, WEB08].

4. **Influent water quality and PFAS mixture**
   - At least key descriptors of the matrix:
     - TOC/NOM (e.g., 2.3 mg/L in Hopkins [WEB03]; <0.5 mg/L in Bertanza [WEB11]).
     - Major competing anions for ion exchange (as modeled by Cheng & Meng [WEB05]).
     - Distinction between **drinking water** vs **industrial wastewater**, as in Zhang [WEB13].  
   - PFAS species monitored and whether they are present as a mixture (e.g., 23 PFAS in Cheng & Meng [WEB05]; 7–11 PFAS per column in Hopkins [WEB03]; 107 PFAS in Zhang’s treatment train [WEB13]).

Without this contextual information, it is **not possible to generalize** service life from one setting to another.

### 4.2 For scale‑up / translation claims (RSSCT → pilot/full‑scale or bench → pilot)

For a claim that **small‑scale tests predict larger‑scale performance**, the following additional evidence is needed:

1. **Design basis for similarity**
   - Specification of the **RSSCT design (constant vs proportional diffusivity)** and media preparation (ground vs unground) [WEB03, WEB12].  
   - Demonstration that chosen design yields **similar breakthrough curves at a chosen metric** (e.g., BV50) in pilot or full‑scale units for at least several PFAS [WEB03, WEB12].

2. **Quantitative comparison**
   - Reported ratio or error between **predicted and observed** bed volumes or breakthrough percentages.  
     - Hopkins shows proportional‑diffusivity RSSCTs **overpredicted BV50 by ~2–3×**, whereas constant‑diffusivity designs performed well [WEB03].  
     - Zhang’s constant‑diffusivity RSSCTs are explicitly used to simulate a full‑scale PFA694E bed, with BV80 specified [WEB13].

3. **Matrix and hydraulic consistency**
   - The predictive relationship must be validated under **the same or very similar water quality and EBCT range** as the target application; otherwise, the type of discrepancy seen between simulated solutions and actual wastewater (Zhang) could occur [WEB13].

4. **Explicit limitation of applicability**
   - As recognized in multiple studies (e.g., Schaefer [WEB12], Zhang [WEB13], Cheng & Knappe [WEB04]), conclusions are conditional on the **tested resins/carbons and matrices**. A defensible claim should specify that the scale‑up is validated for these media and water qualities only, and that extrapolation to different waters or PFAS mixes requires further validation.

### 4.3 What is *not* sufficient

Based on this evidence set, **the following are insufficient on their own** to support service‑life or scale‑up claims:

- A **single batch isotherm‑derived capacity** in clean water, without any column data, EBCT, or water‑quality detail.  
- **Short‑term batch kinetic tests** (e.g., PSO/PFO fits) used to infer that “equilibrium will be reached within X minutes,” then extrapolated to fixed‑bed performance without mass‑transfer and hydrodynamic modeling.  
- **Unvalidated RSSCTs** lacking explicit comparison to pilot/full‑scale behavior at a defined breakthrough criterion.

Using any of these as the primary basis for claims about full‑scale media lifetime or field performance would conflict with the patterns observed in Fatima [WEB01], Smith [WEB06], de Araujo [WEB08], Hopkins [WEB03], and Zhang [WEB13].

---

## 5. Practical implications and research needs

### 5.1 Practical trade‑offs and design implications

- **Designers should treat batch tests as screening tools**, not sizing tools. Batch data can help select between GAC vs AER/IX, identify promising media and PFAS of concern, and inform initial model parameters, but columns (RSSCT, pilot) are needed before committing to full‑scale designs.
- **Early‑breakthrough criteria (BV10) are critical** for health‑based PFAS treatment goals and economically meaningful lifetimes. Studies that only reach modest breakthrough (e.g., not to Ct/Co = 1) still provide useful early‑breakthrough data, but extrapolation to saturation must be clearly qualified (de Araujo [WEB08]).
- **Short‑chain PFAS (PFBA, PFPeA)** are consistently problematic in columns (Tisler [WEB09], Bertanza [WEB11]); any scale‑up or lifetime claim should highlight whether it is based on short‑chain, long‑chain, or a mixture and what replacement criterion is assumed.

### 5.2 Key evidence gaps and research needs

1. **Systematic batch–column paired studies**  
   There are very few cases (Fatima [WEB01], Smith [WEB06]) where batch selectivity or isotherms are explicitly compared to column breakthrough for the same media and water. More controlled batch/column pairs across NOM levels, PFAS suites, and contact times are needed.

2. **Explicit reporting of EBCT, breakthrough criteria, and bed volumes**  
   Several abstracts and summaries omit EBCTs, breakthrough definitions, and BV at those criteria, constraining cross‑study comparison (Kempisty [WEB02], Tisler [WEB09], Bertanza summary [WEB11]). Standardized reporting would greatly improve the ability to generalize.

3. **Broader validation of structure–property breakthrough models**  
   The QSPR‑based \(K_{IX}\) and pseudo‑single‑solute breakthrough models by Cheng & Meng [WEB05] are promising, but their calibration is limited to two resins and 18 matrices. Similar modeling frameworks for GAC and other IX resins, with validation in pilot and full‑scale systems, would strengthen predictive capacity.

4. **Industrial vs drinking‑water matrices**  
   Zhang’s fluorochemical wastewater work [WEB13] demonstrates that **industrial matrices behave very differently from drinking water**. More data linking batch, RSSCT, and full‑scale behavior in diverse industrial settings are needed before extrapolating from drinking‑water‑based designs.

---

### Concluding remarks

Across the compiled evidence, **equilibrium capacities and batch kinetics provide essential but incomplete information**. They reliably indicate **which PFAS and which media are likely to be problematic or effective**, but **they do not, by themselves, define column breakthrough, bed volumes treated, or full‑scale media lifetime**. Those performance metrics emerge only when **flow, EBCT, mass transfer, water quality, and mixtures** are explicitly accounted for through validated column tests (RSSCT, pilot) and mechanistic models.

Any defensible service‑life or scale‑up claim for PFAS adsorption or ion exchange therefore must:

- Be grounded in **breakthrough‑based column data** at clearly defined EBCT, water quality, and PFAS mixtures, and
- Use batch data and equilibrium capacities as **supporting context**, not as standalone predictors of field performance.

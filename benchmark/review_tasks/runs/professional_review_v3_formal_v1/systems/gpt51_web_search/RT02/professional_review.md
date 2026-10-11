## Overview

Across the evidence base, batch adsorption tests provide useful **equilibrium and qualitative selectivity information**, but they do **not on their own** provide defensible predictions of **fixed‑bed breakthrough, bed volumes treated, or media lifetime** for PFAS treatment. Column, pilot, and full‑scale behavior depend strongly on **flow and contact time, kinetics, influent composition (including NOM/DOM), and PFAS mixtures**, which are only partially captured by batch metrics.

The studies summarized below collectively show:

- Batch isotherms can reproduce **relative sorption trends** (e.g., chain length) and, in some settings, yield sorption coefficients consistent with column‑derived values [WEB01; WEB05].
- **Column and pilot tests** consistently show **earlier breakthrough of short‑chain PFAS** relative to long‑chain analogs under otherwise identical conditions [WEB03; WEB06; WEB08; WEB12; WEB13].
- Several studies explicitly demonstrate that **kinetic limitations and competition**, rather than equilibrium capacity alone, can control breakthrough under flow [WEB02; WEB07].
- Predictive frameworks that achieve reasonably accurate **service‑life estimates** are all **calibrated to column data** (RSSCTs, pilot, or full‑scale) and are explicitly tied to **breakthrough criteria, EBCT/flow, and matrix‑specific factors** [WEB03; WEB04; WEB07; WEB09; WEB14].

Below, I address the three requested components in turn.

---

## 1. What different adsorption metrics do – and do not – tell us about treatment performance

### 1.1 Equilibrium capacity from batch tests

Batch equilibrium/isotherm tests (including those fit with standard models) primarily quantify **maximum sorbed mass per mass of media at a given aqueous concentration** under well‑mixed, often long‑contact‑time conditions.

Relevant evidence:

- Fatima et al. obtained **isotherm parameters** from batch tests for five PFAS on GAC and an anion exchange resin (AER) [WEB01]. When those isotherms were used to predict fixed‑bed service life, the **chain‑length–dependent trends** in adsorption were captured, but the **absolute fixed‑bed service life was underpredicted** [WEB01]. This directly demonstrates that matching batch isotherms is **not sufficient** to predict column lifetime.
- Brusseau et al. compared batch and column measurements of PFOS and PFOA sorption to three natural porous geomedia and reported that **adsorption isotherms determined from column and batch methods matched very well** [WEB05]. This shows that, at least for these PFAS–geomedia systems, batch tests can reproduce column‑consistent **equilibrium sorption parameters**, but the study **does not address treatment-column breakthrough or service life** [WEB05].
- Crawford et al. used **batch-equilibration reactors** with activated carbon (AC) and ion‑exchange (IX) media on PFAS‑impacted groundwater to compare removal efficiency, with emphasis on shorter chain PFAS [WEB12]. Only qualitative “removal efficiency” is reported at batch equilibrium; no column design metrics can be derived from the abstract [WEB12].
- The NOM–GAC preprint used batch tests to show that **short‑chain PFAS adsorption is significantly inhibited by a <3 kDa hydrophilic NOM fraction**, while **long‑chain PFAS adsorption is reduced by a hydrophobic neutral (HON) NOM fraction** [WEB02]. These results characterize **capacity loss and competition in batch**, but not column breakthrough directly.

Taken together:

- Batch equilibrium tests are well‑suited for:
  - Ranking media or PFAS by **relative affinity**.
  - Quantifying **isotherm shape** and sorption coefficients.
  - Identifying **competitive effects** of defined co‑solutes (e.g., specific NOM fractions).

- They are **not direct evidence** of:
  - **Breakthrough time** or **bed volumes to a given C/C₀**.
  - **Media lifetime** under realistic flows and mixtures.
  - Performance under **fluctuating influent** or **non‑equilibrium** conditions.

Where batch–column isotherms agree (Brusseau [WEB05]) and where they do not predict service life (Fatima [WEB01]), the evidence converges on the same point: **even when equilibrium parameters are consistent, breakthrough behavior still depends on kinetics and transport**.

### 1.2 Batch kinetics

Batch kinetic tests characterize **rates of approach to equilibrium** under well‑mixed conditions.

- Fatima et al. reported that PFAS kinetic data for GAC and AER were better fit by a **pseudo‑second‑order (PSO) model (R² = 0.92) than a pseudo‑first‑order model (R² = 0.88)** in batch tests [WEB01]. This shows relatively good PSO representation of batch uptake rates but does not by itself link to a specific EBCT or breakthrough time.
- The NOM–GAC preprint used **isotherm, batch kinetic, and column data together** for modeling and concluded that **slower adsorption kinetics, rather than equilibrium capacity, predominantly control the breakthrough of long‑chain PFAS** in GAC columns [WEB02]. This explicitly shows that **kinetic limitations are controlling under flow**, even when equilibrium capacity may appear sufficient in batch.

Thus, batch kinetics can highlight that **diffusion or reaction is rate‑limiting**, and provide parameters for transport models, but:

- They **must be embedded in a column model (e.g., PSDM)** with appropriate hydrodynamics and external mass transfer to say anything about breakthrough [WEB02; WEB07; WEB14].
- Stand‑alone batch kinetic performance (e.g., “fast uptake in batch”) cannot be treated as direct evidence that **short EBCTs will suffice** in fixed beds.

### 1.3 Fixed‑bed breakthrough curves, bed volumes treated, and service life

Column and pilot studies provide **direct measurements** of PFAS removal as a function of **time or bed volumes treated** under flow.

Key quantitative example:

- Hopkins et al. (2023) operated a **pilot‑scale GAC adsorber** on PFAS‑contaminated groundwater and reported **PFAS‑specific bed volumes (BV)** at first observable breakthrough, **10% breakthrough (C/C₀ = 0.1)**, and near exhaustion (C/C₀ ≈ 1) [WEB03]. For PFBA:
  - First observable breakthrough at **5,000 BV** [WEB03].
  - **10% breakthrough** at **6,000 BV** [WEB03].
  - Exhaustion (C/C₀ ≈ 1) at **11,000 BV** [WEB03].
  For longer‑chain PFAAs (PFPeA, PFHxA, PFHpA, PFOA), **10% breakthrough** occurred progressively later: **11,000, 16,000, 20,000, and 23,000 BV, respectively** [WEB03]. These BVs directly define the **run length** of the pilot adsorber at the specified 10% criterion.

Other column/pilot evidence:

- The same Hopkins study used **GAC selection columns (GCS tests)** with breakthrough curves for PFBA and PFOA to compare adsorption capacities across GAC types [WEB03].
- Tang et al. modeled **pilot‑parameterized GAC columns** under different DOM pretreatment scenarios and explicitly used **10% and 50% breakthrough** thresholds to estimate bed volumes treatable [WEB04].
- Pannu et al. ran **pilot‑scale columns** with one alternative adsorbent and five IX resins on groundwater for **up to 19 months** at EBCTs “representative of full‑scale treatment” [WEB06]. They report that:
  - Long‑chain PFAS (PFOA, PFOS, PFHxS) were “well removed,” with **only PFOA eventually breaking through as the media became exhausted** [WEB06].
  - PFBS was also well removed, while **short‑chain PFCAs (PFPeA, PFBA) were not removed (immediate breakthrough)** [WEB06].
  This provides **direct evidence of long‑term column behavior**, especially the impossibility of inferring short‑chain removal from long‑chain performance alone.
- Crawford et al. used **column flushing apparatus experiments** with PFAS‑impacted groundwater to compare **breakthrough and longevity** of AC and IX media, with emphasis on **early breakthrough of shorter chain PFAS** [WEB12]. The abstract does not provide numerical BVs or EBCTs.
- Westreich et al. conducted an **RSSCT comparative column study** with re‑agglomerated bituminous GACs and showed that **PFBA reached breakthrough far more quickly than all other PFAS**, while GACs effectively removed PFAS with **four or more perfluorinated carbons** [WEB13].
- The 2021 GAC vs IX segmented‑column study applied **continuous‑flow segmented columns with full‑scale media**; the authors explicitly state that **long‑term column tests are needed to generate PFAS treatability data and calculate adsorption capacities and treatment longevity for long‑ and short‑chain PFAAs** [WEB08]. This statement underscores that **column data over extended run times, not batch capacities, underlie meaningful service‑life estimates**.
- Liu et al. performed **pilot‑scale GAC treatment of PFAS‑contaminated groundwater with breakthrough modeling**, but the accessible text does not provide BVs or conditions [WEB09].

Summary:

- **Breakthrough curves and BVs** are the **primary empirical basis** for service‑life claims.
- They must be interpreted together with:
  - **Breakthrough criteria** (e.g., 10% C/C₀, regulatory threshold).
  - **EBCT, bed depth, and hydraulic loading rate**.
  - **PFAS mixture and influent concentrations**.
  - **Matrix composition (NOM, co‑contaminants)**.
- Without these, any “lifetime” derived from breakthrough is not portable to other systems.

### 1.4 Modeling frameworks and media lifetime

Several studies use **transport models** to link different column scales and to estimate media lifetime:

- Tang et al. used a **pore‑ and surface‑diffusion model (PSDM)** with a **scaled‑particle diffusion–film transfer relation (SPDFR_full‑scale)** and **pilot‑column parameters** to generate **scaled‑up PFAS breakthrough curves** and predict **BVs to 10% and 50% breakthrough** for various DOM pretreatments [WEB04].
- The RSSCT→pilot Water Research study used a **PSDM** and found that **intraparticle diffusivity is proportional to (dp)⁰·²⁵ when considering data up to about 70% PFAS breakthrough** [WEB07]. This gives an empirically supported kinetic scaling rule for GAC particle size, but explicitly **only up to ~70% breakthrough**; extrapolating to full exhaustion is not supported [WEB07].
- The ChemRxiv NOM–GAC preprint combined **isotherm, batch kinetics, and column data** to model PFAS breakthrough and concluded that **slower adsorption kinetics, not equilibrium capacity, predominantly control long‑chain breakthrough** [WEB02].
- Hopkins et al. (2022) developed a **model‑fitting framework** that uses pilot or RSSCT or full‑scale column breakthrough data to fit parameters, then **predict pilot column performance against a multi‑PFAS treatment objective and evaluate uncertainties** [WEB14]. The authors explicitly state that using such column data as the modeling basis **“provides less certainty about the true isotherm parameters but does capture all the other factors that impact the breakthrough for that system”** [WEB14]. This is a deliberate **shift away from relying on batch isotherms** to infer full‑scale behavior.

Collectively, these modeling efforts support two conclusions:

- **Reliable service‑life predictions are anchored to column data**, not to batch alone.
- Model validity is inherently **bounded** (e.g., only up to a specified breakthrough, or for a given matrix and PFAS mixture) [WEB04; WEB07; WEB14], so claims must clearly note these boundaries.

---

## 2. How operating and water‑quality factors govern translation across scales

### 2.1 Flow and contact time (EBCT, hydraulics)

Flow regime and EBCT are **central** to translating adsorption performance across scales:

- Pannu et al. operated pilot columns with EBCTs described as **“representative of full-scale treatment”** [WEB06]. Under these EBCTs, long‑chain PFAS were well removed for extended periods, with only PFOA eventually breaking through, while PFPeA and PFBA experienced immediate breakthrough [WEB06]. The identical EBCT for all PFAS highlights that **mass‑transfer and affinity limitations are PFAS‑specific**.
- Hopkins et al. (2023) used a **pilot GAC adsorber** to determine **operation time of a full‑scale GAC adsorber**, explicitly basing design on **measured breakthrough at different bed depths and BVs** [WEB03].
- Tang et al. relied on **full‑scale hydraulic information (SPDFR_full‑scale)** combined with **pilot‑column parameters** to predict full‑scale breakthrough [WEB04]. This necessarily assumes that **hydrodynamic similarity and EBCT scaling** are adequately captured in SPDFR and the PSDM.
- The RSSCT→pilot Water Research study targeted **prediction of pilot‑scale breakthrough curves from RSSCT data**, using PSDM and an empirical **dp⁰·²⁵ diffusivity scaling** valid up to ~70% breakthrough [WEB07]. This is explicitly a **flow‑ and scale‑sensitive** relationship.
- Westreich et al. used RSSCTs with groundwater to compare GACs [WEB13]. While EBCT values are not reported in the abstract, RSSCT design inherently links small‑scale column EBCT to full‑scale analogs, again highlighting that **contact time must be explicitly treated in scale‑up**.

Since most batch tests are run at relatively **long contact times and negligible hydrodynamic limitations**, any translation to continuous flow must:

- Explicitly account for **film and intraparticle diffusion**, and
- Recognize that **short EBCTs can cause kinetic limitations** even when batch equilibrium capacity appears ample [WEB02; WEB07].

### 2.2 Influent variability and PFAS mixture effects

PFAS are rarely present as single compounds; mixtures significantly alter breakthrough behavior:

- The Hopkins pilot GAC study measured PFBA, PFPeA, PFHxA, PFHpA, and PFOA concurrently and showed a **clear ordering of 10% breakthrough BVs** (PFBA earliest, PFOA latest) under the same flow and matrix conditions [WEB03]. This evidences **co‑sorption and competitive effects** under realistic mixtures.
- Pannu et al. report six PFAS in the pilot feed (PFOA, PFOS, PFHxS, PFBS, PFPeA, PFBA) and observed **selective breakthrough**: only PFOA broke through among long‑chain PFAS, whereas short‑chain PFPeA and PFBA were never removed (immediate breakthrough) [WEB06].
- Westreich et al. demonstrated that in a **multi‑PFAS RSSCT**, **PFBA broke through much earlier** than all other PFAS, while PFAS with four or more perfluorinated carbons were effectively removed by GAC [WEB13].
- Crawford et al. assessed breakthrough and longevity for multiple PFAS in AC and IX columns with PFAS‑impacted groundwater, emphasizing **early breakthrough of shorter chain PFAS** [WEB12].
- The segmented GAC/IX column study refers to **rapid breakthrough of short-chain PFAS by GAC** as a practical challenge, even though GAC remains widely used due to cost and operability [WEB08].

Batch studies cannot capture **dynamic mixture effects on breakthrough** unless:

- The mixture composition and competitive sorption are explicitly built into a **column model**, and
- The model is calibrated with **mixture breakthrough data** (as in Hopkins 2022’s multi‑PFAS model objective [WEB14]).

### 2.3 Competing constituents (NOM/DOM and pretreatment)

Competing organic matter is a major determinant of how well batch results translate:

- The NOM–GAC preprint provides one of the clearest lines of evidence:
  - In batch, **<3 kDa hydrophilic NOM** significantly inhibits adsorption of **short‑chain PFAS**, while **HON fraction** reduces adsorption of **long‑chain PFAS** [WEB02].
  - In **column experiments**, **HON not only reduced long‑chain PFAS adsorption but also that of short‑chain PFAS**, an effect **not observed in batch experiments** [WEB02]. This is a direct demonstration that **batch competition patterns can change under flow**, owing to differential kinetics and mass‑transfer pathways.
  - Modeling showed that **slower adsorption kinetics, not equilibrium capacity, predominantly control long‑chain PFAS breakthrough** in the presence of NOM [WEB02].
- Tang et al. systematically evaluated **DOM concentration and pretreatment methods** (CFS, CFS–O₃, CFS–O₃–BAC, plus jar tests) and used pilot‑parameterized PSDM to show how pretreatment changes **GAC use rates and BVs to 10% and 50% breakthrough** [WEB04]. This ties **DOM removal** directly to **extended media life** under otherwise similar conditions.
- Westreich et al. and the Hopkins and Pannu pilot studies all used **site‑specific groundwaters**, where **NOM and co‑contaminants are implicitly controlling** PFAS breakthrough, though they are not quantified in the excerpts [WEB03; WEB06; WEB13].
- The GAC/IX segmented‑column study emphasizes, in general terms, that **long-term column tests are needed** to characterize how full‑scale GAC and IX behave for long‑ and short‑chain PFAAs, thereby capturing cumulative effects of NOM and co‑contaminants on capacity and longevity [WEB08].

The key implication is that **batch tests conducted in clean water or with simplified NOM do not by themselves bound column behavior in real waters**. At minimum, translation requires:

- Matrix‑specific NOM characterization or pretreatment description [WEB02; WEB04].
- Column or pilot data in that matrix to calibrate the impact of NOM on **apparent capacity and kinetics**.

### 2.4 PFAS mixtures, selectivity, and chain length

Across column, pilot, and RSSCT studies, there is consistent **qualitative agreement** on relative treatability:

- **Short-chain PFCAs** (PFBA, PFPeA) exhibit **the earliest or even immediate breakthrough**:
  - Immediate breakthrough for PFPeA and PFBA in Pannu’s pilot IX/AA columns [WEB06].
  - Early PFBA breakthrough in Hopkins’s pilot GAC adsorber (10% at 6,000 BV, much earlier than PFOA at 23,000 BV) [WEB03].
  - PFBA “far more quickly than all other PFAS” in Westreich RSSCTs [WEB13].
  - Short‑chain PFAS highlighted for “early breakthrough” in Crawford’s column flushing experiments [WEB12], and “rapid breakthrough of short chain PFAS by GAC” referenced in the GAC/IX segmented‑column article [WEB08].
- **Longer‑chain PFAAs and PFSAs** are **more strongly retained** under comparable conditions:
  - Longer BVs to 10% breakthrough in Hopkins’ pilot column (PFPeA < PFHxA < PFHpA < PFOA) [WEB03].
  - Effective removal of PFOA, PFOS, PFHxS and PFBS in Pannu’s pilot until near media exhaustion, with only PFOA eventually breaking through [WEB06].
  - Effective removal of PFAS with ≥4 perfluorinated carbons by multiple GACs in Westreich RSSCTs [WEB13].

Batch results (e.g., chain‑length dependence of PFAS adsorption on GAC and AER in Fatima’s work [WEB01]) qualitatively agree with these column observations, but **column data quantify the severity of early breakthrough and the practical loss in run length**.

---

## 3. Minimum evidence needed for a defensible service‑life or scale‑up claim

Given the above, the **minimum defensible evidence** for a claim about PFAS adsorber service life or for scaling from lab to pilot/full‑scale must include:

### 3.1 Direct column or pilot data anchored to a clear breakthrough definition

- At least one **column or pilot breakthrough curve** under representative conditions, with:
  - **Breakthrough criterion** explicitly defined (e.g., **10% C/C₀** as in Hopkins [WEB03] and Tang [WEB04], or regulatory threshold), and, ideally, data through late breakthrough (e.g. up to C/C₀ ≈ 1 or ~70% for PSDM parametrization [WEB07]).
  - **Bed volumes (or time) at that criterion** for each PFAS of concern.
- These data should reflect the **full PFAS mixture** expected in practice; designs based only on a subset of PFAS risk underestimating early breakthrough of short‑chain species [WEB03; WEB06; WEB12; WEB13].

Statements claiming that media will last a given time or treat a certain number of BV for PFAS should **not be based solely on batch capacities or short kinetic tests**, given direct evidence that such predictions can **underpredict service life** [WEB01] or **miss kinetic and mixture limitations** [WEB02].

### 3.2 Specification of flow and contact time

Any service‑life or scale‑up claim must specify:

- **EBCT or hydraulic loading rate** and **bed depth/particle size** for the reference system and the target system.
- Whether the scale‑up maintains **hydrodynamic similarity** (e.g., through RSSCT design or SPDFR scaling as in Tang [WEB04] and the RSSCT→pilot study [WEB07]).
- The **range of breakthrough** over which model calibration was performed (e.g., **dp⁰·²⁵ scaling valid up to ~70% breakthrough** [WEB07]), so extrapolation beyond that is not implied without evidence.

Hopkins 2023’s use of pilot BVs at 10% breakthrough to determine full‑scale adsorber operation time [WEB03] and Tang’s use of pilot‑based PSDM + SPDFR_full‑scale to predict full‑scale BVs to 10% and 50% [WEB04] both meet this minimum by explicitly linking **flow/contact time** and **breakthrough criterion**.

### 3.3 Matrix and competing constituents

Defensible claims must state:

- The **water matrix** (e.g., contaminated groundwater vs surface water; PFAS‑impacted groundwater is explicit in several studies [WEB03; WEB06; WEB09; WEB12; WEB13]).
- The presence and treatment status of **NOM/DOM** and major co‑contaminants.
  - Example: Tang’s explicit DOM pretreatment trains (CFS, CFS–O₃, CFS–O₃–BAC) and their role in changing GAC use rates and breakthrough [WEB04].
  - Example: NOM fractions (<3 kDa, HON) and their very different batch vs column competition patterns in the ChemRxiv study [WEB02].
- A statement that the service‑life estimate pertains to **those boundary conditions**; Hopkins 2023 explicitly notes that GAC effectiveness and operation times are conditioned on **initial PFAS concentrations and a 10% breakthrough limit** [WEB03].

Without specifying the matrix and its treatment, the **impact of NOM on apparent capacity and kinetics** is unknown and any capacity‑based scale‑up is speculative.

### 3.4 PFAS mixture and target compounds

Claims must identify:

- The specific **PFAS (and chain lengths)** for which the service life is asserted.
  - Hopkins 2023 reports separate BVs for PFBA, PFPeA, PFHxA, PFHpA, PFOA [WEB03].
  - Pannu 2024 distinguishes behavior of PFOA, PFOS, PFHxS, PFBS, PFPeA, PFBA [WEB06].
  - Westreich 2020 highlights PFBA vs PFAS with ≥4 perfluorinated carbons [WEB13].
- Whether the claim is for a **multi‑PFAS treatment objective** (as in Hopkins 2022’s modeling [WEB14]) or for individual PFAS.

Because short‑chain PFAS often exhibit **much shorter run lengths**, full‑scale design cannot safely be based on long‑chain performance alone [WEB03; WEB06; WEB08; WEB12; WEB13].

### 3.5 Evidence that kinetics and competition are adequately captured

To move from batch to reliable column prediction, the following are minimally needed:

- **Kinetic and isotherm parameters** embedded in a transport model, **and**
- **Calibration against at least one column dataset** in a similar matrix.

The ChemRxiv NOM–GAC modeling work and RSSCT→pilot PSDM study both show that:

- **Breakthrough can be controlled by kinetics rather than capacity** for long‑chain PFAS [WEB02].
- Empirical **kinetic scaling (dp⁰·²⁵)** is only validated **up to ~70% breakthrough** [WEB07].

Hopkins 2022’s modeling framework emphasizes that using **pilot/RSSCT/full‑scale column data** as the fitting basis captures **“all the other factors that impact breakthrough for that system”** but leaves **greater uncertainty in true isotherm parameters** [WEB14]. This implicitly prioritizes **column fidelity over batch parameter purity** for design purposes—a reasonable trade‑off when the engineering goal is service‑life prediction.

### 3.6 Explicit limitations on extrapolation

Finally, a defensible claim should explicitly state:

- The **range of breakthrough** over which the model/test is validated (e.g., to 10% or 50% C/C₀ [WEB03; WEB04], or up to ~70% for PSDM scaling [WEB07]).
- Whether results are from **laboratory columns, RSSCTs, or pilot systems**, and that **full‑scale uncertainties remain**:
  - Tang notes that full‑scale PFAS breakthrough behavior is inferred via PSDM rather than directly measured [WEB04].
  - The 2021 GAC/IX segmented‑column article stresses the need for **long‑term column tests** for treatability and capacity estimates [WEB08].
  - Crawford’s and Pannu’s pilot studies illustrate that **short pilots stopping at initial breakthrough** can misrepresent long‑term exhaustion patterns [WEB06; WEB12].

---

## 4. Synthesis: When batch results are informative – and when they fail

**When batch results help:**

- **Relative rankings and trends.** Batch isotherms and removal efficiencies can reliably indicate that:
  - Longer‑chain PFAS have higher affinity than shorter chain analogs [WEB01; WEB12].
  - Certain NOM fractions strongly inhibit specific PFAS classes [WEB02].
- **Parameterization for models.** Batch isotherm and kinetic data provide starting values for PSDM or similar column models [WEB01; WEB02; WEB07; WEB14].
- **Geomedia contexts.** For PFOS and PFOA sorption to geomedia, batch and column isotherms and sorption coefficients matched well [WEB05], suggesting that, at least in some simple systems, batch measures can approximate column equilibrium behavior.

**Where batch results do not predict column or full‑scale performance:**

- **Service life and bed volumes treated.** Fatima’s study explicitly shows isotherm‑based predictions **underpredicted observed fixed‑bed service life**, even though chain‑length trends were captured [WEB01]. This is a direct refutation of “equilibrium capacity = lifetime.”
- **Kinetics‑limited breakthrough.** Modeling in the NOM–GAC preprint identified **slower adsorption kinetics as the dominant control** for long‑chain PFAS breakthrough, not equilibrium capacity, under column conditions [WEB02].
- **NOM competition under flow.** In columns, the HON NOM fraction reduced adsorption of both long‑ and short‑chain PFAS, whereas in batch it mainly affected long‑chain PFAS [WEB02]. This difference arises from **flow‑dependent competition** not evident from batch tests.
- **Short‑chain PFAS behavior.** Multiple column and pilot studies show **early or immediate breakthrough of short‑chain PFCAs** despite acceptable batch removal or long‑chain performance [WEB03; WEB06; WEB08; WEB12; WEB13]. Without column data, batch tests would **over‑estimate** protection for short chains.

In practical terms, **batch tests are necessary but not sufficient**. For PFAS treatment with GAC or IX, any claim that a medium will achieve a given service life, or that a batch‑derived capacity translates directly to bed volumes treated, is **not supportable** under the evidence here unless:

- It is backed by **column or pilot data** at relevant EBCTs and water quality, **and**
- The associated **breakthrough definitions, flow, influent variability, competing constituents, and PFAS mixture** are clearly specified.

---

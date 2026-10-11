### 1. Conceptual distinctions

Across the studies in the ledger, four distinct phenomena are measured or inferred:

- **Parent‑compound loss:** decrease of the targeted PFAS concentration (e.g., PFOA, PFOS).
- **Transformation:** formation of new organofluorine species from the parent (often shorter‑chain PFCAs).
- **Defluorination:** release of inorganic fluoride or HF, indicating C–F bond cleavage.
- **“Destruction” / “mineralization”:** broad language used by authors to suggest conversion to inorganic products (fluoride, CO₂, etc.), but very rarely supported by full carbon and fluorine mass balances.

A defensible interpretation must keep these separate. Parent disappearance alone never proves complete defluorination or mineralization; even near‑stoichiometric fluoride release may not track carbon fate.

Below, I compare the key endpoint types, then evaluate how analytical design affects interpretation, and finally propose an evidence hierarchy for destruction claims.

---

### 2. Comparison of endpoint types

#### 2.1 Parent-compound loss

**What is measured**

Parent PFAS loss is typically measured by LC–MS/MS or HPLC–MS:

- Hydrothermal alkaline treatment (HALT) of high‑TDS aqueous PFAS mixtures quantified ultra short‑, short‑, and long‑chain PFAS by targeted LC–MS/MS and described their disappearance as “degradation” [R01].
- Activated persulfate oxidation of PFOA reported a “PFOA degradation efficiency” of 89.9% by HPLC–MS [R02].
- The HALT treatment of PFAS‑laden GAC used LC–MS/MS to quantify PFOS and PFHpS remaining in solution and on GAC [R03].
- Plasma GAP and electrochemical studies speak of PFAS “degradation,” but the ledgered evidence focuses more on mechanisms and fluorine balances than on specific time‑concentration curves [R04; R05].

**What it does and does not show**

- Parent loss shows that the monitored target is transformed, but not:
  - whether fluorine has been released as inorganic fluoride/HF,
  - what transformation products form,
  - whether carbon is fully oxidized.

The Yin persulfate study makes this explicit: 89.9% PFOA loss corresponds to only 23.9% defluorination [R02]. Most lost PFOA mass therefore remains as organofluorine—not as inorganic fluoride or CO₂.

**Implication for practice**

Parent loss is a **minimum** indicator of chemical change, but should not be equated with destruction, defluorination, or mineralization. It must be combined with transformation‑product and fluorine endpoints to interpret PFAS fate.

---

#### 2.2 Transformation-product analysis

**What is measured**

Several studies explicitly track organofluorine products:

- **Activated persulfate, PFOA in groundwater:** one‑CF₂‑unit‑shortened PFCAs (Cn‑1F₂n‑1COOH) are observed and mechanistically attributed to SO₄•−‑triggered decarboxylation followed by HF elimination [R02].
- **Activated persulfate, PFOS in water:** PFOS defluorination yields CF₃(CF₂)nCOOH (n = 0–6) detected by LC/MS/MS [R06].
- **Plasma GAP in water:** the study emphasizes the existence of degradation products, including shorter‑chain PFAS, as a key concern; the available text notes that PFAS can degrade to shorter‑chain PFAS that remain recalcitrant [R04].
- **Electrochemical PFOA oxidation:** short‑chain PFCAs are reported as byproducts; their formation increases at higher temperatures and their subsequent degradation accelerates with higher reaction rates [R05].

**Strengths**

- Product analysis demonstrates that parent loss frequently reflects **re‑distribution of fluorine within organofluorine pools**, not outright destruction.
- Mechanistic hypotheses (e.g., decarboxylation + HF elimination for PFOA under persulfate [R02]) highlight reaction channels that can be tuned to favor or disfavor certain intermediates.

**Limitations**

- Analytical scope is typically narrow:
  - Yin and Yang (persulfate) focus on perfluorocarboxylic acids; non‑PFCA organofluorine or volatile products are not comprehensively characterized [R02; R06].
  - Plasma and electrochemical studies recognize short‑chain PFCAs but, in the available text, do not close an organofluorine mass balance [R04; R05].
- Even when major PFCAs are measured, there is usually an **unassigned fraction** of fluorine not resolved into specific products.

**Implication**

Transformation‑product data are essential to avoid misclassifying parent loss as destruction, but without broader analytical coverage and total fluorine tracking, they still cannot quantify destruction.

---

#### 2.3 Fluoride release and defluorination endpoints

**What is measured**

Defluorination is generally derived from inorganic fluoride (or HF) measurements:

- **PFOA + activated persulfate:** a “defluorination ratio” of 23.9%—fluoride released relative to theoretical fluoride from degraded PFOA [R02].
- **PFOS + activated persulfate:** fluoride is measured by ion‑selective electrode, and “defluorination efficiency” is reported qualitatively; defluorination ranking across activation methods (HT > UV > Fe²⁺ > US) is given without numerical values in the extracted text [R06].
- **HALT, aqueous high‑TDS PFAS mixtures:** dissolved fluoride is measured; near‑stoichiometric fluoride production at optimized conditions is reported [R01].
- **HALT, PFAS‑laden GAC (patent):** fluoride in reactor liquid measured by ISE; together with PFOS/PFHpS fluorine equivalents, this yields a fluorine mass balance that “remained at or near 100%,” leading the authors to conclude full defluorination of PFOS on GAC [R03].
- **Mechanochemical phosphate treatment of neat PFAS:** organic fluorine is converted to inorganic fluoride salts (KF, K₂PO₃F or tetraalkylammonium fluorides); near‑quantitative conversion of organic fluorine to inorganic fluoride is reported [R07].
- **Simulated incineration (CIC):** fluorine recovery as HF is used to evaluate “fluorine mineralization,” but authors stress that HF recovery is controlled by matrix composition and analytical limitations, not only mineralization [R08].

**What it shows**

- Fluoride/HF release directly demonstrates **C–F bond cleavage**, i.e., defluorination, at least for the fraction of fluorine recovered as inorganic F.
- When combined with parent loss, defluorination clarifies whether transformation is mostly to shorter‑chain organofluorines (low fluoride yield) or towards inorganic F (high yield). The PFOA persulfate case—large gap between 89.9% parent loss and 23.9% defluorination—illustrates extensive transformation but limited defluorination [R02].

**Caveats**

Interpreting defluorination requires attention to:

- **Matrix and protocol dependence:** CIC work shows that fluorine recovery as HF is strongly influenced by material composition, moisture, and combustion protocol; single‑pass combustion of calcium‑rich matrices underestimates fluorine release, while multi‑step protocols improve it [R08].
- **Phase coverage:** aqueous fluoride is measured in most wet treatments, but:
  - metal‑associated fluoride or other solid‑phase inorganic F may not be captured (CIC clearly shows metal associations can trap fluorine [R08]),
  - gaseous HF or volatile inorganic F may be unmeasured in some reactor designs.
- **Analytical limits:** plasma GAP experiments define an “unquantified fluorine” fraction that includes volatile organofluorine and gaseous HF, underscoring that fluoride alone does not resolve all defluorinated fluorine [R04].

**Implication**

Fluoride endpoints elevate evidence above mere parent loss, yet without a **well‑designed fluorine mass balance** and explicit protocol details, they cannot by themselves prove complete defluorination or destruction.

---

#### 2.4 Fluorine mass balance and total organofluorine change

**What is measured**

Stronger studies attempt to track all fluorine, not just a subset:

- **Aqueous HALT (high‑TDS matrix):** targeted LC–MS/MS, free fluoride, and total organic fluorine (TOF) are combined to close a near‑stoichiometric fluorine mass balance; the multiple‑lines‑of‑evidence approach “strongly suggests … minimal undesired organofluorine byproduct formation” [R01]. Authors report complete conversion of PFAS to inorganic dissolved fluoride under optimized conditions [R01‑E04].
- **HALT on PFAS‑laden GAC (patent):** PFOS and PFHpS fluorine equivalents plus fluoride in the reactor liquid yield a fluorine mass balance near 100%; with no fluorinated organic intermediates detected in GAC extracts or liquid, the authors conclude full PFOS defluorination [R03–E03]. This mass balance is constructed from targeted analytes and liquid‑phase fluoride.
- **Mechanochemical phosphate treatment:** fluorine mass balance is closed using fluoride yields and solid‑state ¹⁹F NMR, showing near‑quantitative conversion of organic fluorine in neat PFAS solids to inorganic fluoride salts [R07, R07].
- **Simulated incineration (CIC):** total fluorine recovery as HF is an analytical mass‑balance endpoint; authors emphasize that gaps can arise when mineralization is incomplete or when unknown products of incomplete destruction and inorganic byproducts form, as well as from background fluorine [R08].
- **Plasma GAP:** fluoride plus “unquantified fluorine” are said to make up the majority of the fluorine mass balance, with unquantified fluorine including volatile organofluorine fragments and gaseous HF [R04].
- **Electrochemical PFOA oxidation:** the study is explicitly framed as using a “quantitative fluorine mass balance framework” to elucidate degradation pathways and fluorine fate [R05], though detailed numbers are not accessible in the ledger.

**Strengths**

- Mass‑balance approaches directly confront the question: *Where did the fluorine go?*
- When the balance is near stoichiometric and most fluorine is measured as inorganic F, **defluorination is strongly supported**. The HALT aqueous study and mechanochemical phosphate treatment represent the strongest fluorine‑fate evidence in this set [R01; R07], with the patent GAC HALT experiment providing a more limited but still coherent balance [R03].
- Mass‑balance gaps, as in CIC and plasma GAP, are equally informative: they signal unresolved fluorine species, PIDs, or analytical artifacts [R08; R04].

**Limitations**

- **Analytical scope:** 
  - Aqueous HALT infers minimal undesired organofluorine byproducts but does not fully speciate any residual organofluorine [R01].
  - The HALT–GAC patent does not characterize volatile organofluorine or inorganic fluoride on solids other than GAC [R03].
  - CIC focuses on HF; it does not resolve individual organofluorine PIDs [R08].
- **Phase and matrix coverage:** As CIC shows, matrix‑bound fluorine and background F can mask true defluorination [R08]. Plasma GAP explicitly acknowledges “unquantified fluorine” [R04].
- **Time resolution:** Mechanochemical and HALT studies close balances at end points; transient intermediates during treatment are not tracked with high time resolution [R01; R07].

**Implication**

Carefully designed fluorine mass balances are the **current best practice** for distinguishing disappearance from defluorination. However, claims of “complete destruction” require not only fluorine closure but also at least qualitative accounting of carbon fate and unresolved fluorine fractions.

---

#### 2.5 Mineralization-related endpoints

None of the ledgered studies provides a fully resolved carbon mass balance (e.g., CO₂ evolution plus dissolved inorganic and organic carbon speciation) linked to PFAS carbon.

- **Yin (PFOA + persulfate)** explicitly *proposes* that repeated decarboxylation and HF elimination would “eventually lead to the complete mineralization” of all PFCAs [R02]; there is no direct mineralization measurement in the extracted text.
- **Mechanochemical phosphate treatment** is described as a “mineralization process” enabling fluorine recovery as KF/K₂PO₃F [R07]. The measurements, however, document fluorine transfer and closure of the fluorine mass balance, not carbon products.
- **Plasma GAP** uses “mineralization” language, and scavenger tests distinguish PFAS degradation from what authors label mineralization; yet the available evidence points to fluoride and “unquantified fluorine” endpoints rather than tracked CO₂ or total carbon [R04, R04].
- **CIC work** refers to HF as an indicator of “fluorine mineralization” [R08], but again, this is fluorine‑centric and does not quantify carbon fate.
- Aqueous HALT and HALT–GAC patent materials use “destruction” and “mineralization” language [R01; R03], but the measured endpoints are fluorine balances and TOF, not direct carbon balances.

**Implication**

In this evidence set, “mineralization” is almost always **used more broadly than the measurements support**. The defensible, measured endpoints are defluorination and fluorine mass balance. Mineralization—sensu stricto carbon conversion to CO₂/inorganic carbon—remains largely inferred.

---

### 3. How analytical design and data gaps affect interpretation

#### 3.1 Analytical scope and detection limits

- **Target list bias:** Persulfate and electrochemical studies target PFOA and a set of PFCAs [R02; R06; R05]. Non‑PFCA products, polymeric fragments, or volatile organofluorines may escape detection, leaving an unquantified organofluorine pool.
- **Total organofluorine vs targeted analytes:** HALT in high‑TDS solutions brings TOF into the mass balance, mitigating target‑list bias and supporting “minimal undesired organofluorine byproduct formation” [R01]. By contrast, PFOA persulfate oxidation and PFOS persulfate defluorination infer defluorination only from inorganic fluoride; total fluorine is not closed [R02; R06].
- **Fluorine versus carbon tracking:** Even where fluorine is well accounted for (HALT, mechanochemical phosphate, CIC), the carbon side of the mass balance is not similarly resolved [R01; R07; R08]. This precludes strong mineralization claims.

Detection limits are particularly important for:

- **“No intermediates detected” claims:** In the HALT–GAC patent, a lack of fluorinated organic intermediates in GAC extracts and reactor liquid is used to support full PFOS defluorination [R03]. Without explicit reporting of limits of detection and analyte coverage, “non‑detection” cannot be equated with absence.
- **Unquantified fluorine:** Plasma GAP explicitly recognizes unquantified fluorine formed via charge‑transfer and thermal processes, including volatile organofluorine and gaseous HF [R04]. This is a model example of acknowledging analytical blind spots.

#### 3.2 Sampling time and transient species

- **Batch end‑point vs kinetic resolution:** Many experiments (HALT, mechanochemical phosphate, HALT–GAC patent) emphasize end‑point balances [R01; R03; R07]. Transient organofluorine intermediates may transiently accumulate but be unobserved if only early and final timepoints are analyzed.
- **Sampling protocols:** Yin’s persulfate PFOA study quenches reactions with ethanol at designated times and measures PFOA and products [R02], but the extracted text does not detail a dense time series. Minimal temporal resolution obscures peak intermediate concentrations and short‑lived species.
- **Plasma GAP:** source limitations (outside the locator‑verified endpoints) note constraints in sampling times and detection limits for intermediates, consistent with the explicit recognition of “unquantified fluorine” [R04]. Time‑dependent partitioning among fluoride, volatile organofluorines, and aqueous intermediates is therefore only partially resolved.

**Implication**

Coarse sampling and incomplete analytical coverage lead to:

- Underestimation of intermediate pools.
- Over‑reliance on parent loss and terminal fluoride as surrogates for destruction.
- Ambiguity between *apparent* mass‑balance closure and true absence of PIDs.

#### 3.3 Matrix and scale effects

- **High‑TDS aqueous matrices:** HALT shows fluorine mass balance closure in ~10 wt% TDS brines [R01], but the authors caution that these conditions are optimized and may not generalize to other matrices or less optimized conditions [R01].
- **Solid PFAS wastes and sorbents:** HALT on GAC [R03] and mechanochemical phosphate treatment of neat PFAS [R07] address solids rather than dilute waters. CIC further demonstrates that matrix composition (e.g., calcium‑rich solids) can trap fluorine and affect measured fluorine release [R08].
- **Water treatment at bench scale:** Persulfate and electrochemical studies in groundwater or simple aqueous matrices [R02; R06; R05] and plasma GAP in water [R04] provide mechanistic but not scale‑transferrable destruction data. Their conditions (pH, oxidant dose, plasma configuration) are not directly comparable without more detailed reporting.

**Implication**

Endpoints must always be interpreted *in the context of matrix and scale*. For example, near‑stoichiometric fluoride release in neat solids under mechanochemical conditions [R07] is not directly analogous to fluoride release in dilute waters or complex sludges.

---

### 4. Evidence hierarchy for PFAS “destruction” claims

Drawing on these studies, a defensible hierarchy for PFAS destruction evidence can be articulated. Each higher tier incorporates the measurements below it and adds new constraints. The hierarchy must always be interpreted with explicit reference to **technology, matrix, and scale**.

#### Level 0 – Parent loss only

- **Endpoint:** Target PFAS concentration decrease.
- **Evidence:** e.g., “PFOA degradation efficiency 89.9%” by HPLC–MS [R02].
- **Limitations:** Cannot distinguish among transformation, partial defluorination, and true destruction; short‑chain PFAS and other organofluorines can dominate residual toxicity.
- **Use:** Only suitable for screening or preliminary kinetics. **Not acceptable** to claim destruction, defluorination, or mineralization.

#### Level 1 – Parent loss + targeted transformation products

- **Endpoint:** Parent loss plus formation of defined PFCAs or other PFAS.
- **Evidence:** PFOA → shortened PFCAs via decarboxylation/HF elimination under persulfate [R02]; PFOS → CF₃(CF₂)nCOOH (n = 0–6) under persulfate [R06]; short‑chain PFCAs as byproducts in electrochemical and plasma treatments [R04; R05].
- **Limitations:** Typically lacks coverage of non‑PFCA products and total fluorine; unquantified organofluorine remains.
- **Use:** Mechanistic insight; supports statements like “PFOA is transformed to shorter‑chain PFCAs under condition X.” Still **insufficient** for destruction claims.

#### Level 2 – Parent loss + inorganic fluoride endpoint (defluorination) without closed fluorine balance

- **Endpoint:** Parent loss, targeted products, and inorganic fluoride or HF.
- **Evidence:** 23.9% defluorination ratio for PFOA persulfate vs 89.9% degradation [R02]; PFOS defluorination efficiencies under different persulfate activation methods [R06]; fluoride formation in plasma GAP and electrochemical systems (implicitly, via fluorine mass balance frameworks [R04; R05]); HF recovery in CIC as a defluorination signal [R08].
- **Limitations:** No explicit accounting of:
  - all organofluorine intermediates,
  - fluorine partitioning between aqueous, solid, and gas phases,
  - analytical biases (e.g., CIC matrix effects [R08]).
- **Use:** Supports statements such as “X% of PFOA fluorine has been released as inorganic fluoride under conditions Y,” *not* “PFOA is fully destroyed.” 

#### Level 3 – Partial fluorine mass balance

- **Endpoint:** Combination of targeted PFAS, selected transformation products, and fluoride/HF, but some fluorine remains unassigned.
- **Evidence:** Plasma GAP, where “fluoride and unquantified fluorine make up a majority of the fluorine mass balance,” with unquantified fluorine including volatile organofluorine and gaseous HF [R04]. CIC, where incomplete mineralization and PIDs lead to mass‑balance gaps and matrix‑associated fluorine [R08, R08].
- **Limitations:** Unquantified fractions can be sizable and may include persistent PFAS or toxic organofluorines; destruction cannot be inferred for that portion.
- **Use:** Appropriate for nuanced statements: e.g., “Most fluorine is converted to fluoride or volatile fluorine species under these GAP conditions; an unquantified fluorine fraction remains and may reflect PIDs or analytical loss.”

#### Level 4 – Near-complete fluorine mass balance with strong defluorination evidence

- **Endpoint:** Near‑stoichiometric recovery of fluorine, predominantly as inorganic fluoride, supported by multiple analytical lines.
- **Evidence:**
  - Aqueous HALT closes the fluorine mass balance using targeted LC–MS/MS, free fluoride, and TOF; near‑stoichiometric dissolved fluoride at optimized conditions indicates effective defluorination with “minimal undesired organofluorine byproduct formation” [R01, R01]. Authors report complete conversion of PFAS to inorganic dissolved fluoride under those conditions [R01‑E04].
  - HALT–GAC patent experiment constructs a fluorine mass balance from PFOS/PFHpS equivalents and aqueous fluoride; mass balance near 100% plus non‑detection of fluorinated organics in GAC extracts and liquid is interpreted as full PFOS defluorination [R03–E03].
  - Mechanochemical phosphate treatment achieves near‑quantitative conversion of organic fluorine in neat PFAS solids into inorganic fluoride salts (KF, K₂PO₃F or tetraalkylammonium fluorides), with closure supported by fluoride yields and solid‑state ¹⁹F NMR [R07, R07].
  - Electrochemical PFOA study adopts a quantitative fluorine mass balance framework but detailed closure metrics are not available in the accessible text [R05].
- **Limitations:**
  - Aqueous HALT does not fully speciate any remaining organofluorine and is demonstrated for specific high‑TDS brines under optimized T/NaOH ranges [R01].
  - HALT–GAC mass balance is limited to the targeted PFAS and aqueous fluoride; fluoride bound to reactor materials or alternate solids is unmeasured [R03].
  - Mechanochemical work addresses neat solids, not environmental matrices, and focuses on fluorine rather than carbon balance [R07].
- **Use:** Supports strong statements of **near‑complete defluorination** under the specific test conditions and matrices, e.g., “Under optimized HALT conditions in ~10 wt% TDS brine, fluorine is almost entirely recovered as dissolved fluoride, indicating near‑complete defluorination of ultra short‑ to long‑chain PFASs” [R01]. Still does **not** alone demonstrate carbon mineralization.

#### Level 5 – Full fluorine *and* carbon mass balance (not demonstrated in this ledger)

- **Endpoint:** Closed fluorine mass balance (including inorganic F and all organofluorine phases) plus a quantitative carbon balance (CO₂, dissolved inorganic carbon, residual organics) explicitly linked to PFAS carbon.
- **Evidence:** Not present in the verified table.
- **Use:** This level would be required to claim **complete PFAS mineralization** in a strict sense.

---

### 5. Technology-, matrix-, and scale-specific nuances

Within the hierarchy above, destruction evidence must be contextualized:

- **Hydrothermal alkaline treatment (HALT) in aqueous high‑TDS matrices [R01]:**
  - Provides among the strongest aqueous‑phase defluorination evidence, with multi‑technique fluorine mass balance.
  - Demonstrated for synthetic ~10 wt% TDS brines and specific PFAS mixtures; generalization to dilute waters or different TDS compositions requires caution.

- **HALT of PFAS‑laden GAC [R03]:**
  - Extends HALT to sorbent regeneration with a coherent but more limited fluorine balance.
  - Leaves questions about volatile fluorine and non‑GAC solids.

- **Mechanochemical phosphate treatment of neat PFAS solids [R07]:**
  - Provides strong fluorine‑fate evidence and a circular fluorine concept, but:
    - applies to neat PFAS or concentrated solid wastes, not dilute environmental waters,
    - lacks carbon‑product detail.

- **Persulfate and electrochemical oxidation in water [R02; R06; R05]:**
  - Illustrate that high parent removal can coincide with low defluorination, and that shorter‑chain PFCAs form readily.
  - Emphasize the importance of fluorine mass balance frameworks and strategies to limit short‑chain byproducts [R05].

- **Plasma GAP in water [R04]:**
  - Mechanistic scavenger studies distinguish between PFAS degradation and what authors call mineralization, but measured endpoints in the excerpts are fluorine‑centric and include an explicit “unquantified fluorine” pool [R04].
  - Highlights the persistence of volatile organofluorine and the difficulty of closing mass balances in gas–liquid plasma systems.

- **Thermal treatment via CIC simulated incineration [R08]:**
  - Shows that HF recovery is strongly matrix‑dependent and that incomplete fluorine release from calcium‑rich matrices can bias fluorine mass balance and apparent “mineralization” [R08, R08].
  - Demonstrates that analytical protocol (single‑pass vs multi‑step combustion) can mimic or obscure true destruction performance.

---

### 6. Recommendations and future research needs

#### 6.1 Reporting and measurement standards

To reliably distinguish parent disappearance, transformation, defluorination, and destruction:

1. **Always report at least:**
   - Parent PFAS concentration vs time.
   - Inorganic fluoride (or HF) formation vs time.
   - Clear analytical detection limits and analyte scope.

2. **Incorporate fluorine mass balance wherever feasible:**
   - Combine targeted PFAS, key transformation products, and inorganic F.
   - Extend to TOF and/or total fluorine where possible, as in the HALT study [R01].

3. **Characterize transformation products beyond PFCAs:**
   - Expand LC–MS/MS target lists.
   - Include screening for perfluoroacyl fluorides and volatile organofluorines, informed by evidence from plasma and incineration work [R08; R04].

4. **Separate fluorine and carbon claims:**
   - Treat fluorine‑centric endpoints (fluoride, HF, fluorine mass balance) explicitly as **defluorination metrics**, not as mineralization proxies.
   - Reserve “mineralization” for cases with supporting carbon‑fate measurements.

#### 6.2 Design of mass-balance experiments

- **Phase-resolved sampling:** Capture aqueous, solid, and gas/vapor phases (including off‑gas scrubbing) to reduce “unquantified fluorine” fractions, taking plasma GAP and CIC findings as cautionary examples [R08; R04].
- **Matrix‑aware protocols:** Account for metal‑associated fluorine and other matrix effects, as CIC work shows these can significantly bias HF‑based mass balances [R08].
- **Temporal resolution:** Increase sampling density early in treatment to capture transient intermediates and refine degradation pathway models.

#### 6.3 Technology comparison and scale-up

- Apply the **evidence hierarchy** when comparing technologies:
  - Do not equate a Level 0/1 technology (parent loss, limited product speciation) with a Level 4 system (near‑closed fluorine mass balance).
  - Explicitly state the matrix (high‑TDS brine vs groundwater vs neat solids vs sorbent vs soils) and scale (bench, simulated, etc.) alongside destruction claims.

- For scale‑up:
  - Use high‑quality mass‑balance studies such as HALT aqueous [R01], mechanochemical phosphate [R07], and CIC [R08] as reference cases for designing pilot‑ and full‑scale monitoring programs.
  - Incorporate lessons on matrix‑dependent fluorine release and analytical artifacts (CIC) to avoid over‑ or under‑estimating destruction.

---

### 7. Concluding perspective

Within the verified evidence set, the most robust distinction between PFAS disappearance, transformation, and destruction comes from:

- Mass‑balanced defluorination in HALT aqueous systems and neat‑solid mechanochemical treatments [R01; R07].
- Contrasting examples where high parent loss but modest defluorination (e.g., PFOA persulfate) directly show that disappearance alone is misleading [R02].
- Studies that explicitly acknowledge unquantified fluorine and matrix or analytical limitations (CIC, plasma GAP) [R08; R04].

A rigorous PFAS destruction claim therefore requires, at minimum, near‑complete fluorine mass balance with dominant inorganic fluoride, explicit attention to unresolved fluorine, and—ideally—parallel carbon‑fate evidence. Anything less should be described as **transformation with partial defluorination**, not as complete destruction or mineralization.

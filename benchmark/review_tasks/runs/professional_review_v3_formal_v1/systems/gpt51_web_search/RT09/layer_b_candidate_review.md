## 1. Conceptual frame: what “disappearance” can and cannot tell us

Across the evidence set, four distinct types of measurements recur:

- **Parent-compound loss** (target PFAS concentration ↓)
- **Transformation-product analysis** (new PFAS or organofluorines ↑)
- **Fluoride release / defluorination** (F⁻ from cleaved C–F bonds)
- **Fluorine mass balance** (parent PFAS + known organofluorines + F⁻ ± other fluorine pools)
- **Carbon- or mineralization-related indicators** (rarely measured directly)

The key lesson from these studies is that **none of these measurements alone, including 100% parent loss, is sufficient to prove complete destruction or mineralization of PFAS.** Each quantifies a different slice of the fate of fluorinated carbon.

Below, I compare these endpoint types, evaluate how analytical design shapes interpretation, and propose an evidence hierarchy for claiming “destruction,” with clear limits by technology, matrix, and scale.

---

## 2. Comparing endpoint types

### 2.1 Parent-compound loss

**What is measured**

Most studies monitor loss of the target PFAS (e.g., PFOS, PFOA) by LC‑MS/MS or similar targeted methods.

Examples:

- **UV/sulfite (PFOA)**: PFOA in a synthetic/complex aqueous matrix drops below a 10 µg/L detection limit (from 10 mg/L) after 1 h at pH 10, 10 mM sulfite [R01‑E01]. At pH 12, 100% degradation of PFOA is reported after 24 h [R01‑E01].
- **UV/sulfite/iodide (PFOS, PFOA, 6:2 FTS, PFBS)**: 100% degradation of PFOS, PFOA, and 6:2 FTS, but incomplete degradation of PFBS in the “initial” configuration [R02‑E02]; >99.9% “destruction” of PFBS in an optimized protocol [R02‑E04].
- **Sonolysis (PFOS)**: complete PFOS degradation at 400 and 500 kHz (after several hours) is reported [R03‑E02, R03‑E05].
- **SCWO (PFOS, PFHpS, PFOA)**: 99.999% “destruction” of all measured PFAS at 650 °C and ~30 s [R04‑E01].
- **Smoldering soil treatment**: targeted PFAS in soil reduced by >99.9%, below quantitation in nearly all tests [R05‑E01].

**What this actually tells us**

These measurements are **necessary but not sufficient** to infer destruction:

- They quantify **parent-compound loss in a given phase**, not total PFAS fate.
- They are constrained by **detection limits** and targeted analyte lists.
- They cannot distinguish between:
  - benign mineral products (e.g., CO₂, F⁻, CaF₂),
  - shorter-chain or partially defluorinated PFAS,
  - non-extractable or sorbed organofluorine,
  - volatile organofluorines in the gas phase.

For instance, PFOA below 10 µg/L does not mean zero PFOA, and tells us nothing about transformation products or gas-phase species [R01‑E01]. Treating “100% degradation” on this basis as proof of complete PFAS destruction would violate the task boundary.

**Crucially:** Across all studies, **disappearance of the monitored parent PFAS never, by itself, demonstrates complete defluorination or mineralization.**

---

### 2.2 Transformation-product analysis

**What is measured**

Several studies monitor specific transformation products:

- **UV/sulfite (PFOA):** short-chain PFCAs (C<7), hydrogen‑substituted PFAS, and sulfonated and unsaturated intermediates are detected during treatment [R01‑E03]. This confirms chain‑shortening and H/F exchange, i.e., **stepwise transformation**, not direct mineralization.
- **UV/sulfite/iodide (PFOS):** novel –F/+H PFPS and PFES and isomeric –F/+H PFOS species are identified [R02‑E03], confirming C–C bond cleavage and suggesting C–F cleavage along the chain.
- **Sonolysis (PFOS):** trace short‑chain PFAAs are found at all frequencies; total mass of these species is <1% of total yield [R03‑E03].

SCWO and HALT studies largely address transformation in more aggregate terms (e.g., “degradation” of mixtures, gas-phase volatile organofluorines) rather than detailed speciation across many products [R06‑E01, R06‑E05; R04‑E04, R04‑E05].

**What this tells us**

Transformation-product measurements:

- **Demonstrate that parent loss proceeds through intermediate organofluorines**, even when parent removal and defluorination are high.
  - UV/sulfite shows co‑occurrence of PFOA loss with short‑chain PFCAs and hydrogen‑substituted intermediates [R01‑E03].
  - UV/sulfite/iodide produces partially hydrogen‑substituted sulfonates (PFPS, PFES, –F/+H PFOS isomers) [R02‑E03].
- Show that **identifiable short‑chain PFAAs can be a very small fraction of the fluorine mass**:
  - Under sonolysis, all measured short‑chain PFAAs together are <1% of the mass balance [R03‑E03].

However, these analyses are usually **highly targeted**:

- They cover a narrow suite of possible products.
- Unresolved organofluorine may remain as non‑target PFAS, oligomers, or non‑ionic fluorinated organics.
- For gas‑phase intermediates (volatile organofluorines, VOFs), SCWO identifies their presence semi‑qualitatively but not as a closed mass balance [R04‑E04, R04‑E05].

Thus, transformation-product analysis is **critical to show that disappearance ≠ instantaneous destruction**, but alone it does not quantify total destruction or defluorination.

---

### 2.3 Fluoride release and defluorination

**What is measured**

Many studies quantify inorganic fluoride (mostly aqueous F⁻; in soils sometimes HF or solid fluorides) to infer C–F bond cleavage:

- **UV/sulfite (PFOA):**
  - 89% defluorination after 24 h at pH 10 [R01‑E01].
  - 98% defluorination after 24 h at pH 12 [R01‑E01].
- **UV/sulfite/iodide:**
  - >90% defluorination for PFOS, PFOA, 6:2 FTS in the initial configuration [R02‑E02].
  - “Complete quantitative defluorination” of PFBS under the optimized protocol [R02‑E04, R02‑E06].
- **Sonolysis (PFOS):**
  - Stoichiometric fluoride release at 400, 500, 1000 kHz to the theoretical yield for 100% PFOS defluorination (315.9 µM, 6.001 mg/L) [R03‑E01, R03‑E02].
- **SCWO (PFOS, PFHpS, PFOA):**
  - Complete defluorination at 650 °C and ~30 s, based on aqueous fluoride and fluorine mass balance [R04‑E01, R04‑E02].
- **HALT, high‑TDS aqueous mixtures:** free fluoride is used with targeted PFAS and total organic fluorine to close a near‑stoichiometric fluorine mass balance and infer complete defluorination under optimized conditions [R06‑E01, R06‑E02].
- **Commercial HALT on industrial wastewater:** dissolved inorganic fluoride is the “final reaction product” at higher temperature, with near‑complete fluorine mass balance closure [R07‑E03].
- **Smoldering soil:** HF in emissions and formation of CaF₂ in CaO‑amended soils represent major inorganic fluoride sinks; HF mass exceeds emitted targeted PFAS mass [R05‑E03, R05‑E05, R05‑E06].

**What this tells us**

Fluoride release:

- **Directly tracks C–F bond cleavage** from measured PFAS but only for fluorine that ends up as detectable inorganic fluoride in sampled phases.
- High or stoichiometric fluoride yields, especially combined with very low levels of measured organofluorines, give **strong evidence of extensive defluorination**, as in:
  - Sonolysis of PFOS at ≥400 kHz [R03‑E01, R03‑E02].
  - SCWO at 650 °C [R04‑E01, R04‑E02].
  - HALT under optimized bench conditions [R06‑E01, R06‑E02].
  - UV/sulfite/iodide optimized PFBS treatment [R02‑E04, R02‑E06].
  - Smoldering + CaO, where XPS indicates conversion of >98% of PFAS mass to CaF₂ and HF+residual organic F account for <2% of original F [R05‑E05, R05‑E06].

But fluoride alone cannot tell us:

- Whether **all fluorine has been accounted for** (e.g., some may be in unmeasured organofluorines, mineral fluorides, or volatile products).
- Anything about **carbon fate**—high defluorination could coexist with organic carbon fragments that are toxic or persistent.

The industrial HALT and SCWO studies show why: both needed **explicit fluorine mass balances and gas‑phase screening** to argue that unmeasured fluorinated byproducts are limited [R06‑E02; R07‑E03; R04‑E02, R04‑E04]. Even then, unresolved fractions (e.g., VOFs in SCWO at lower T [R04‑E04, R04‑E05]; inert 1H‑perfluoroalkane VOFs in HALT at some conditions [R07‑E03]) demonstrate that high fluoride does not guarantee absence of other fluorinated products.

---

### 2.4 Fluorine mass balance and total fluorine / organofluorine

**What is measured**

Different systems extend beyond F⁻ and parent PFAS to track more of the fluorine pool:

- **HALT (high‑TDS bench scale)**:
  - Combines targeted LC–MS/MS for multiple PFAS classes, free fluoride, and total organic fluorine (TOF), achieving near‑stoichiometric fluorine mass balances under optimized conditions [R06‑E01, R06‑E02, R06‑E04].
  - Authors infer minimal undesired organofluorine byproducts from this multi‑endpoint closure [R06‑E02].
- **HALT (industrial wastewater)**:
  - Constructs a fluorine mass balance including inorganic fluoride and volatile organofluorines, with near‑complete closure at higher temperature and no observable VOF generation [R07‑E03].
- **Smoldering soil**:
  - Uses PIGE to measure total fluorine in soil pre‑ and post‑treatment; 96–99% F removal in no‑CaO tests, with 0.5–3.3 mg F/kg residual [R05‑E02].
  - Overall fluorine mass balances (soil + emissions + burnout tests) yield 68–128% recovery [R05‑E04].
  - In CaO‑amended tests, XPS shows CaF₂ formation; authors infer >98% of pretreatment PFAS mass mineralized to CaF₂, while HF+organic F in soil total <2% of initial F [R05‑E05, R05‑E06].
- **SCWO (PFOS, PFHpS, PFOA)**:
  - Fluorine mass balance based on Sum(PFAS) and fluoride shows >100% F recovery at T > 580 °C and deficits at lower T [R04‑E02, R04‑E03], indicating both analytical uncertainty and potential untracked fluorine pools at lower T.
  - Gas-phase GC/MS indicates volatile organofluorines at lower T, and non-detection of gaseous F‑containing compounds at 580 °C [R04‑E04].

**What this tells us**

Where well executed, fluorine mass balances substantially raise the level of evidence:

- **HALT bench‑scale:** Near‑stoichiometric closure using three lines of evidence (target PFAS, F⁻, TOF) under optimized conditions is strong support that **most fluorine is either in measured inorganic fluoride or in organofluorine captured by TOF**, with little room for major unmeasured organofluorine byproducts [R06‑E02].
- **Smoldering + CaO:** Converging measures—>99.9% targeted PFAS loss [R05‑E01], 96–99% total F removal in no‑CaO configuration [R05‑E02], small HF+organic F residuals (<2% of initial F) [R05‑E05], and the appearance of CaF₂ by XPS [R05‑E06]—point to **extensive defluorination with fluorine captured in solid CaF₂**.

At the same time, mass balances reveal unresolved fractions and uncertainty:

- **Smoldering:** Fluorine mass balance recoveries from 68–128% show significant uncertainty, limiting precise quantification of defluorination and destruction [R05‑E04].
- **SCWO:** F‑balance >100% at high T [R04‑E03] reflects measurement scatter or unaccounted fluorine sources/sinks; deficits at lower T indicate unmeasured fluorinated species—consistent with VOF observations [R04‑E04, R04‑E05].

Note also that:

- PIGE and total F/TOF measurements do **not distinguish organic versus inorganic fluorine** at the measurement step [R05‑E02; R06‑E02]. Interpretation of organofluorine versus inorganic pools depends on combining multiple endpoints, not on PIGE alone.

---

### 2.5 Mineralization-related endpoints (carbon fate)

There is **very limited direct evidence** on carbon mineralization in the table:

- **UV/sulfite/iodide (O’Connor thesis, Chapter 3)** explicitly defines “destruction” as loss of initial PFAS plus quantitative fluoride recovery [R02‑E06]. This is a **composite PFAS+F⁻ metric**, not a direct carbon‑fate or CO₂ measurement.
- The optimized PFBS protocol claims >99.9% “destruction” with “complete quantitative defluorination” [R02‑E04, R02‑E06], again without explicit carbon balance.
- **SCWO** reports 99.9999% “mineralization” at T > 650 °C [R04‑E03], but the table notes that this is inferred principally from PFAS loss and fluorine mass balance and that a complete carbon balance is not documented in the provided text [R04‑E02, R04‑E03].
- **Smoldering** studies interpret conversion of PFAS F to CaF₂ with minimal HF and organic F residuals (<2% of original F) as “mineralization” [R05‑E05, R05‑E06]; however, the direct measurements are fluorine partitioning and CaF₂ formation, not CO₂ quantification or a full carbon balance.
- **UV/sulfite + iodide in complex matrices (O’Connor thesis, Chapter 4)** uses the term “mineralize PFAS” in the chapter title [R08‑E01] but the excerpt does not show what measurements (e.g., TOC, CO₂) were used [R08‑E01–E03].

Therefore, across this evidence set, **“mineralization” is generally a claim built from PFAS loss + fluoride recovery ± fluorine mass balance, not from direct carbon‑fate measurements**. Under the task rules, these data support **defluorination and parent loss**, but **do not demonstrate mineralization in the strict sense** (conversion of PFAS carbon to inorganic carbon such as CO₂) unless explicit carbon-balance evidence is presented—which is not visible in the retained excerpts.

---

## 3. How analytical design, timing, and scope affect interpretation

### 3.1 Analytical scope and unidentified products

**Target list constraints**

Many studies use relatively narrow targeted PFAS lists for parents and transformation products:

- UV/sulfite studies measure PFOA and a limited suite of short‑chain PFCAs and some specific intermediates [R01‑E03].
- Sonolysis work tracks PFOS and several short‑chain PFAAs, but those account for <1% of mass [R03‑E03].
- Smoldering soil treatment uses targeted LC‑MS/MS for PFAS but PIGE total F indicates that **fluorinated species outside the targeted analyte scope** likely account for the difference between >99.9% targeted PFAS removal and only 96–99% total F removal [R05‑E02].
- HALT bench‑scale extends the scope via TOF, which captures organofluorine beyond the targeted list but still does not speciate every compound [R06‑E02].

**Gas-phase and volatile organofluorines**

Several technologies can create **volatile or semi‑volatile organofluorines** (VOFs):

- SCWO detects VOF ion fragments in off‑gas at lower temperatures [R04‑E04], and notes that VOFs can be more persistent than PFCAs in effluent [R04‑E05].
- Industrial HALT generates inert 1H‑perfluoroalkane VOFs at lower temperature, lower NaOH, and higher throughput, while at higher temperature no VOFs were observed and the mass balance closes with dissolved inorganic fluoride [R07‑E03].

If gas‑phase species are not fully captured and quantified, **fluorine mass balances built only on aqueous PFAS and F⁻ will overestimate “destruction”**, because some fluorine resides in VOFs.

**Non-extractable or solid-phase organofluorine**

- Smoldering studies indicate that without CaO, a residual 0.5–3.3 mg F/kg soil remains after treatment [R05‑E02], but its speciation (unreacted PFAS, transformation products, inorganic fluoride) is unresolved.
- With CaO, XPS detects CaF₂ in post‑treatment soils where it was absent before [R05‑E06], supporting conversion of PFAS fluorine to solid CaF₂. However, the XPS is semi‑quantitative, and its translation to a precise >98% fraction carries analytical uncertainty [R05‑E06].

In both cases, **incomplete knowledge of solid-phase speciation limits certainty** about residual risk; even when most fluorine is inorganic, some organofluorine may persist below detection or outside the monitoring suite.

### 3.2 Sampling time and kinetic considerations

Interpretation depends heavily on **when** samples are taken:

- UV/sulfite PFOA:
  - Parent loss is essentially complete (<DL) after 1 h at pH 10 [R01‑E01], but **defluorination at 24 h is only 89%** [R01‑E01], implying that substantial organic fluorine persists for many hours after PFOA is gone.
- UV/sulfite/iodide:
  - Reported 100% degradation and >90% defluorination for some PFAS [R02‑E02], but time to reach these endpoints is not specified in the excerpt; thus we cannot resolve whether transient transformation products accumulate at intermediate times.
- Sonolysis:
  - PFOS degradation and stoichiometric fluoride release are evaluated at 4 h [R03‑E01, R03‑E05]. Within the first 2 h, kinetic analysis shows varying agreement with zero‑order behavior across frequencies [R03‑E04], indicating that rates and intermediate build‑up can differ substantially before the 4‑h endpoint.
- SCWO:
  - At high T (~650 °C) and ~30 s, F‑balance >100% and authors assert complete defluorination and near‑complete PFAS loss [R04‑E01, R04‑E03]. At lower T (<580 °C), F‑balance deficits and VOF detection indicate incomplete accounting for fluorine [R04‑E03, R04‑E04]. Thus, statements about destruction are **strongly time–temperature dependent**.

For robust inference, **time‑resolved measurements of parent PFAS, key transformation products, and fluoride** are needed. Single end‑points (e.g., 24 h for UV/sulfite, 4 h for sonolysis, one residence time in SCWO) risk missing intermediate plateaus where transformation products and undefined organofluorines may peak.

### 3.3 Detection limits and analytical sensitivity

Detection limits control when authors can declare “complete degradation”:

- UV/sulfite PFOA uses a relatively high detection limit of 10 µg/L [R01‑E01], while initial concentration is 10 mg/L. Reporting PFOA as “below detection” implies >2.7 log removal—but:
  - Residual PFOA up to 10 µg/L is still possible.
  - More importantly, **PFAS below this DL may still be environmentally relevant**, especially if extrapolated to field scenarios with lower starting levels.
- Smoldering’s PIGE total fluorine has relatively high detection limits; the standard uncertainty is reflected in the 68–128% F‑balance range [R05‑E04]. Assertions of “<2% residual HF + organic F” are based on the fraction of F mass they can quantify, not on absolute absence of organofluorine below those thresholds [R05‑E05].

Where DLs are high or unspecified, conservative interpretation requires:

- Not equating “not detected” with zero (both for PFAS and gaseous fluorinated species).
- Recognizing that **unmeasured or sub‑trace PFAS and VOFs could still be toxicologically significant**, especially in dilute environmental settings.

### 3.4 Matrix and scale effects

Matrix complexity affects both performance and measurement:

- UV/sulfite PFOA:
  - Carbonate (>5 mM), nitrate (>2 mM), and humic acid (>25 mg/L) significantly impede PFOA degradation via UV blocking and electron scavenging [R01‑E05].
  - The study itself notes that PFAS in real waters are typically ng/L–µg/L, and pretreatment (membrane, sorption) is recommended before UV/sulfite [R01‑E06].
  - These conditions complicate destruction assessments at environmentally relevant concentrations.
- UV/sulfite/iodide:
  - Bench-scale work is in bicarbonate‑buffered alkaline solutions [R02‑E01]; destruction claims rely on parent loss + F⁻ recovery [R02‑E02, R02‑E04, R02‑E06], primarily in relatively simple matrices (except for later thesis work in complex matrices where quantitative data are not excerpted [R08‑E01–E03]).
- HALT:
  - Bench-scale study uses synthetic high‑TDS (~10 wt%) aqueous brines [R06‑E01, R06‑E03]; commercial‑scale study treats a specific industrial ion‑exchange regeneration brine [R07‑E01, R07‑E04]. Generalization to other brines, sludges, or dilute waters must be cautious.
- Smoldering:
  - PFAS‑impacted soils (spiked with PFAS mixtures) show good removal and defluorination under smoldering conditions with or without CaO [R05‑E01–E03, R05‑E06], but soil type, moisture, and CaO dosing are system‑specific.
- SCWO:
  - Operates on defined aqueous PFAS mixtures at relatively high concentrations, with ethanol co‑fuel [R04‑E01, R04‑E02]. These conditions are not universally representative of all PFAS wastes.

Scale‑up from bench reactors to commercial systems (HALT industrial [R07], smoldering tests [R05], SCWO’s continuous reactor [R04]) introduces additional **hydraulic, thermal, and sampling challenges** that can obscure phase-specific mass balances, especially for VOFs and solid fluorides.

---

## 4. Evidence hierarchy for “destruction” claims

Given the above, a defensible hierarchy for PFAS “destruction” evidence should explicitly distinguish:

- **Parent loss** (LC‑MS/MS disappearance)
- **Transformation** (formation and fate of organofluorines)
- **Defluorination** (fluoride release and fluorine partitioning)
- **Mineralization** (carbon fate)

Below is a proposed hierarchy, with examples illustrating what the current evidence *can* and *cannot* support. Percentages are those reported by authors, but the *interpretive tier* is constrained by what was actually measured.

### Level A: Parent-compound removal only

**Definition:** Evidence is limited to reduction of target PFAS concentrations (often to below DL) in a given phase.

**Measurement set:**

- Targeted PFAS (parent) pre/post.
- Little or no systematic measurement of F⁻, transformation products, or fluorine mass balance.

**Interpretation:**

- Supports **removal of monitored parent PFAS from the sampled phase**.
- Does **not** support claims about defluorination, transformation pathways, or mineralization.
- Vulnerable to misinterpretation when coupled to terms like “destruction.”

**Examples from table:**

- Portions of the UV/sulfite PFOA study, if read in isolation of the fluoride and transformation data, could fall here [R01‑E01, R01‑E03].
- Any study that reports only “100% degradation” with no fluoride or product analysis would be Level A (fortunately, most records here go beyond that).

### Level B: Parent loss + partial evidence of transformation

**Definition:** Parent PFAS loss is documented, and some transformation products are monitored qualitatively or semi‑quantitatively, without fluoride or mass balance closure.

**Measurement set:**

- Parent PFAS + a limited suite of transformation products.
- No or minimal inorganic fluoride data; no overall F‑balance.

**Interpretation:**

- Demonstrates that disappearance corresponds to **chemical transformation**, not just phase transfer.
- Cannot quantify defluorination or rule out significant hidden organofluorine pools.

**Examples:**

- O’Connor Chapter 4 qualitative discussion of “mineralization” and robustness in complex matrices without quantified fluoride or product data in the excerpt [R08‑E01–E03].
- Hypothetical early‑stage development tests; none of the main quantitative studies in this table are restricted solely to this level, but several mineralization claims in thesis text sit here analytically.

### Level C: Parent loss + fluoride release (defluorination) without closed fluorine balance

**Definition:** Parent PFAS loss and substantial fluoride release are both measured, but a complete fluorine mass balance (including all relevant phases and organofluorine) is not demonstrated.

**Measurement set:**

- Parent PFAS concentrations.
- Inorganic fluoride (usually aqueous, sometimes gas-phase HF).
- Some targeted transformation products.
- No formal closure of total fluorine, TOF, or solid-phase fluorine, or only partial.

**Interpretation:**

- Supports **extensive defluorination of the measured PFAS**, often to near‑stoichiometric levels.
- Unmeasured organofluorines may still exist (e.g., non‑targeted products, sorbed species, VOFs).
- **Does not** by itself establish total PFAS destruction or mineralization.

**Examples:**

- **UV/sulfite PFOA**: 89–98% defluorination with PFOA loss and detection of short‑chain PFCAs and other intermediates [R01‑E01, R01‑E03]. The study does not close a total fluorine balance or quantify gas‑phase products [R01 source limitations], so results sit at Level C.
- **UV/sulfite/iodide initial system**: 100% degradation and >90% defluorination for PFOS, PFOA, 6:2 FTS [R02‑E02], with transformation products characterized for PFOS [R02‑E03]. Destruction is defined as loss + fluoride [R02‑E06], but total fluorine and carbon balances are not documented; this also fits Level C.
- **Sonolysis of PFOS**: Stoichiometric fluoride release plus complete PFOS degradation and only trace short‑chain PFAAs (<1% mass) [R03‑E01–E03]. Fluorine mass balance is built only from F⁻ and several PFAAs; volatile and non-target organofluorines are not comprehensively accounted for [R03 source limitations]. This is high‑quality Level C evidence.

**Appropriate language:** “Extensive defluorination and parent PFAS degradation” is supportable; “complete destruction” or “mineralization” is not, without additional mass‑balance or carbon‑fate data.

### Level D: Parent loss + high defluorination + near‑stoichiometric fluorine mass balance

**Definition:** Parent loss and high defluorination are accompanied by a well‑designed fluorine mass balance across relevant phases (aqueous, solid, gas as appropriate), often including TOF or total F, such that unaccounted fluorine is small and characterized.

**Measurement set:**

- Parent PFAS (often multiple classes).
- Inorganic fluoride (in water, emissions, or both).
- At least one *bulk* fluorine metric beyond F⁻ and targeted PFAS:
  - TOF in solution or total F by PIGE in solids.
- Explicit fluorine mass balance with clear accounting for solids, water, and gases; gas-phase VOFs measured or bounded.

**Interpretation:**

- Strong evidence that **most fluorine originally bound in PFAS ends up as inorganic fluoride or measured organofluorine**, with minimal unmeasured fluorine in any phase.
- Supports robust claims of **PFAS defluorination on a mass‑balance basis**.
- Still does **not guarantee carbon mineralization**, unless CO₂/TOC balances are also measured.

**Examples:**

- **HALT bench‑scale (high‑TDS aqueous mixtures):**
  - Degradation and defluorination of ultra short‑, short‑, and long‑chain PFAS are quantified over a range of T and NaOH [R06‑E01, R06‑E03].
  - A multiple‑lines‑of‑evidence approach (targeted LC‑MS/MS, free fluoride, TOF) demonstrates near‑stoichiometric fluorine mass balance and suggests minimal undesired organofluorine byproducts at optimized conditions [R06‑E02, R06‑E04].
  - This is close to textbook Level D for fluorine.
- **HALT commercial system (industrial wastewater):**
  - Near‑100% degradation of target FCAs across 300–350 °C, 0.1–0.5 M NaOH [R07‑E02].
  - At higher temperature, fluorine mass balance closes near completely with dissolved inorganic fluoride as the final product and no observable VOFs [R07‑E03].
  - At lower T/NaOH and higher throughput, VOFs appear [R07‑E03], explicitly flagging a fluorine compartment outside the aqueous phase.
  - At best conditions, this approximates Level D, but unresolved sub‑trace VOFs remain a caveat [R07‑E03].
- **Smoldering soil with CaO:**
  - Targeted PFAS >99.9% removed [R05‑E01].
  - HF+organic F residuals <2% of original fluorine mass [R05‑E05].
  - XPS shows CaF₂ formation, interpreted as >98% of pretreatment PFAS mass converted to CaF₂ [R05‑E06].
  - Fluorine mass balance across soil and emissions has significant uncertainty (68–128%) [R05‑E04].
  - Despite uncertainty, converging evidence supports extensive defluorination with CaF₂ as the primary sink—higher Level C to lower Level D, depending on how strictly one weights the mass‑balance uncertainty.

- **SCWO:** 
  - At 650 °C and ~30 s, complete defluorination and 99.999% PFAS destruction are reported [R04‑E01], with F‑balance >100% at T > 580 °C and deficits at lower T [R04‑E03].
  - VOFs are semi‑qualitatively observed at lower T [R04‑E04], and absent (not detected) in gas at 580 °C [R04‑E04].
  - Within the available excerpts, this system fits **upper Level C / lower Level D** for fluorine: strong aqueous defluorination with some uncertainty about gas‑phase fluorine at all conditions.

**Appropriate language:** “Near‑complete defluorination with near‑stoichiometric fluorine mass balance and minimal unmeasured organofluorine” is supportable for the best HALT conditions [R06‑E02, R06‑E03] and for CaO‑smoldering in terms of fluorine [R05‑E05, R05‑E06]; “complete PFAS destruction” or “mineralization” still requires explicit carbon‑fate evidence.

### Level E: Fluorine mass balance + carbon-fate (mineralization) evidence

**Definition:** All Level D evidence plus **direct measurements of carbon fate** (e.g., TOC reduction, CO₂ yield, carbon mass balance across phases) that show conversion of PFAS carbon to inorganic carbon with minimal residual organic carbon associated with fluorine.

**Measurement set:**

- All Level D fluorine endpoints.
- Gas‑phase CO₂ quantification linked to PFAS carbon.
- TOC/DOC tracking and/or total carbon balances.

**Interpretation:**

- Supports robust claims of **near‑complete mineralization** of PFAS (for both fluorine and carbon).
- To be credible, this level requires demonstration that **carbon and fluorine balances are closed (or nearly so)** across water, solids, and gas.

**Examples from current table:**

- None of the retained records provide a fully documented carbon mass balance.  
  - SCWO and UV/sulfite/iodide use the term “mineralization,” but in the table this is shown to be inferred from PFAS loss plus fluorine behavior [R02‑E06; R04‑E03], without explicit CO₂ or total carbon closure.
  - The thesis Chapter 4 title promises “mineralization” in complex matrices [R08‑E01], but the provided excerpts contain no supporting carbon‑fate measurements.

**Implication:** In the current evidence set, **no technology can be said to have demonstrated Level E mineralization** on the basis of the verified data alone. Destruction claims should therefore be framed as **high defluorination with strong fluorine mass-balance support**, not as proven carbon mineralization.

---

## 5. Practical implications and research needs

### 5.1 Avoid conflating endpoints in technology evaluation

- **Do not treat parent PFAS disappearance as destruction.**  
  PFOA or PFOS “100% degradation” in UV or sonolysis studies [R01‑E01; R03‑E02] is compatible with substantial organic fluorine remaining in shorter‑chain PFAS or other organofluorines.
- **Fluoride release alone is not enough.**  
  Stoichiometric F⁻ production (e.g., sonolysis [R03‑E01–E02], SCWO [R04‑E01], some UV/sulfite/iodide protocols [R02‑E02, R02‑E04]) documents C–F bond cleavage, but total organofluorine may persist as transformation products or VOFs [R04‑E04, R04‑E05; R07‑E03].
- **Fluorine mass balances must account for all phases.**  
  HALT and SCWO show that neglecting VOFs can lead to overconfidence in aqueous‑only mass balances [R06‑E02; R07‑E03; R04‑E04]. Smoldering demonstrates the importance of solid fluoride sinks such as CaF₂ [R05‑E06].

### 5.2 Design of measurement suites for future work

To move more technologies toward Level D and eventually Level E:

1. **Minimum fluorine endpoints for any “destruction” claim in water matrices:**
   - Parent PFAS and major expected transformation products.
   - Aqueous F⁻.
   - At least one total fluorine metric (TOF or equivalent).
   - Gas‑phase sampling for fluorinated species when thermal or oxidative processes are used (e.g., SCWO, HALT).

2. **For solid matrices (soils, sludges):**
   - Targeted PFAS and transformation products in solids and leachates.
   - Total fluorine by PIGE or comparable technique, pre‑ and post‑treatment [R05‑E02].
   - Speciation of dominant inorganic fluoride phases (e.g., CaF₂, MgF₂) [R05‑E06; R07‑E05].
   - HF and VOFs in off‑gas.

3. **For mineralization claims:**
   - Continuous or batch‑integrated CO₂ monitoring tied to PFAS carbon.
   - TOC/DOC tracking and mass balance across water/solid/gas.
   - Integration of carbon and fluorine balances to distinguish complete mineralization from partial oxidation/fragmentation.

### 5.3 Specific gaps highlighted by existing studies

- **UV/e⁻–based reduction systems (UV/sulfite, UV/sulfite/iodide):**
  - Need full fluorine mass balances and gas-phase screening in both simple and complex matrices (e.g., AFFF concentrates [R08‑E01–E03]).
  - Detection limits should be improved for both parent PFAS and transformation products; high DLs (10 µg/L) [R01‑E01] are not sufficient for extrapolation to ng/L scenarios.
- **Hydrothermal systems (HALT, SCWO):**
  - Already relatively advanced in fluorine accounting, but still need:
    - More comprehensive VOF quantitation (not just semi‑qualitative GC/MS) [R04‑E04, R04‑E05].
    - Coordinated carbon balances (TOC, CO₂) to validate mineralization assertions.
- **Thermal soil treatments (smoldering with/without CaO):**
  - PIGE and XPS show promising defluorination to CaF₂ [R05‑E02, R05‑E06], but:
    - Fluorine mass balance uncertainty is large (68–128% recovery) [R05‑E04]; improved analytical precision and gas‑phase accounting are needed.
    - Identification and quantification of trace products in emissions remain incomplete [R05 source limitations].

---

## 6. Summary

Across UV/sulfite, UV/sulfite/iodide, sonolysis, HALT, smoldering, and SCWO, the evidence shows that:

- **Parent PFAS disappearance is routinely achieved**, often to below detection, but **disappearance alone is never proof of destruction or mineralization.**
- **Transformation-product monitoring** consistently reveals organofluorine intermediates—even when parent loss and defluorination are high—reinforcing that **stepwise transformation dominates** rather than instantaneous mineralization.
- **Fluoride release and defluorination metrics** are powerful but must be interpreted with awareness of unmeasured organofluorine and other fluorine sinks (solids, VOFs).
- **Fluorine mass balances that combine targeted PFAS, F⁻, and total F/TOF are currently the strongest lines of evidence for PFAS destruction** (in the sense of extensive defluorination and minimal residual organofluorine), as shown most clearly for HALT [R06‑E01–E03] and CaO‑smoldering [R05‑E05, R05‑E06].
- **Carbon mineralization is not convincingly demonstrated by the extracted data** for any technology; claims of “complete mineralization” are, in practice, statements about high defluorination plus parent loss, not about full carbon-fate closure.

A robust evidence hierarchy for PFAS destruction should therefore:

1. **Explicitly separate parent loss, transformation, defluorination, fluorine mass balance, and carbon mineralization;**
2. **Require at least Level C (parent + fluoride + some product data)** to speak of PFAS “destruction” even in a limited sense; and
3. **Reserve true “mineralization” language for systems that demonstrate both fluorine and carbon mass-balance closure across all relevant phases.**

This hierarchy preserves clarity across technologies, matrices, and scales, and prevents over‑interpreting parent disappearance as proof of complete PFAS destruction.

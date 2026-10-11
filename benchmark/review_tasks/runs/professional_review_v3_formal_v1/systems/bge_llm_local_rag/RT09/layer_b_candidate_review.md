## 1. Distinguishing PFAS disappearance, transformation, defluorination, and destruction: what is actually measured?

Across the dataset, five main endpoint families appear:

1. **Parent-compound loss / “destruction”** – decrease of targeted PFAS concentrations in a given phase.  
2. **Transformation-product (TP) analysis** – detection of intermediates, including shorter-chain PFCAs, PFSAs, fluorotelomers, and other PFAS-like structures.  
3. **Fluoride release (defluorination)** – appearance of inorganic F⁻ in water, occasionally coupled with estimates of defluorination efficiency.  
4. **Fluorine mass balance / total organofluorine change** – accounting of fluorine between parent PFAS, transformation products, F⁻, and sometimes TOF/EOF.  
5. **Mineralization-related endpoints** – primarily TOC removal, very rarely supported by more complete fluorine+carbon closure.

These are often conflated in the literature but are conceptually distinct. The structured evidence shows that **no single endpoint on its own is sufficient to claim complete PFAS destruction or mineralization**; the more complete studies deliberately combine several endpoint types and still leave unresolved fractions.

Below, the endpoints are compared and then used to build an evidence hierarchy.

---

## 2. Comparison of key endpoint types

### 2.1 Parent-compound loss (“destruction”, DRE)

Parent loss is universally reported and is often labeled “destruction”:

- **SCWO (continuous/batch)**
  - Batch PFOS SCWO reaches 70% PFOS conversion at 500 °C, 60 min; defluorination is 78.2% under the same condition, with total F recovery >75% only at ≥475 °C [R01].  
  - Continuous-flow SCWO mixture studies report DRE >99.999% for PFOS/PFOA/PFHpS at 650 °C, ~30 s [R02, R03], and for a 12‑PFAA AFFF suite at field scale [R04].  
  - Pilot systems treating diluted AFFF (Aquarden, Battelle, 374Water) show >99.99% PFOS removal and large PFOA reductions [R05].

- **Hydrothermal alkaline treatment (HALT)**
  - Bench-scale AFFF HALT at 350 °C, ≥2 h and 5 M NaOH yields >99% reduction in total detected PFAS across 40 analytes, with no new targeted PFAS observed [R06].
  - Pilot HALT on industrial wastewater reports %Degradation based on targeted PFAS concentration loss, but does not publish numeric values in the excerpts [R07].

- **Plasma and cavitation**
  - Reverse-vortex gliding arc plasma (GAP) gives 21% PFOA loss at 20 min, 150 W (in the “most energy-efficient” regime discussed) [R08].
  - Hydrodynamic cavitation (HC) of PFOS shows gradual parent loss; degradation per pass peaks at ~1.6% and totals ~20% defluorination by the end of the experiment [R09].

- **Ultrasonication**
  - Bench ultrasonication of PFOA, PFOS and 6:2 FTS routinely achieves >80–100% parent loss in MQ, CW and SW [R10].
  - In real groundwater, total measured PFAS drop from ~111 ppb to 16.6 ppb (~85% removal) but PFHxS and PFOS remain [R10].

- **Electrochemical treatment**
  - Batch proof-of-concept EC treatment in deionized/distilled water (DDW) yields 95–98% PFOA/PFOS “removal” in 1 h, but with no F⁻ detected [R11].
  - Continuous EC for PFAS mixtures in tap water reduces most PFAS by 1–2 orders of magnitude at 80 min, with PFBA largely persisting [R11].

- **Mechanochemical destruction (ball milling)**
  - BN-assisted ball milling of undiluted AFFF reports disappearance of 6:2/8:2 FTS, PFHxA, PFOA and other n = 6–7 precursors within 6 h [R12].
  - Quartz-sand MCD of AFFF and contaminated soil achieves 99.88–100% loss of targeted PFAS subgroups, including PFHxS and PFOS [R13].

- **Photocatalysis (CS@g‑C₃N₄)**
  - For PFOA in DI water, 93% parent loss in 120 min; for PFOS, 88% [R14].

Across technologies, **parent loss alone consistently overstates the degree of PFAS destruction** because:

- Shorter-chain PFAS or other TPs often rise as parents drop (e.g., PFHxA/PFPeA/PFBA in SCWO and ultrasonication [R02, R10]; PFDA/PFTrDA and 6:2 FTS in SCWO [R05]; shorter PFCAs in plasma [R08]).
- Fluorine balances frequently show large unrecovered fractions (see §3).

Therefore, parent loss is a necessary but not sufficient condition for destruction, and absolutely not for mineralization.

---

### 2.2 Transformation-product analysis

Studies with targeted or high-resolution TP analysis show that loss of monitored parents frequently reflects **redistribution within the PFAS chemical space**:

- **PFOS SCWO in continuous-flow (single compound)**  
  PFOS yields a suite of PFCAs (PFOA, PFHxA, PFPeA, PFBA, PFPrA, TFA) at 420–600 °C, with TFA persisting even at 600 °C, 32 s [R02]. Volatile organofluorines (VOFs, including 1H‑perfluorohexane) are detected in gas-phase products [R02].

- **SCWO of AFFF matrices**  
  - Battelle continuous SCWO: PFDA increases in effluent; PFTrDA and 6:2 FTS are below MDL in influent but above MDL in effluent [R05], i.e. clearly formed in the reactor.  
  - Continuous-flow SCWO on PFAS mixtures at 510 °C: all PFCAs go below MDL, but PFOS/PFHpS remain; PFHxS appears in effluent even though it was below MDL in stock, implying low-level presence rather than in‑reactor formation at the measured conditions [R03].

- **Ultrasonication**  
  - PFOA, PFOS and 6:2 FTS degrade to PFPeA, PFHxA, PFHpA, PFHpS in various water matrices [R10].  
  - For AFFF and foam fractionate and for contaminated groundwater, TOP assay and targeted panels show decrease of parent PFAS with likely formation of ultrashort PFCAs (TFA, PFPrA) that are not well captured by standard methods [R10].

- **Plasma GAP**  
  - Cross-formation of PFOA from PFOS and PFOS from 8:2 FTS confirms headgroup cleavage and telomer degradation [R08].  
  - Shorter-chain PFCAs and chain-length reduction are observed by UV–vis and LC‑MS/MS/QTOF [R08].

- **Mechanochemical destruction (MCD)**  
  - In AFFF and impacted soil, C₆–C₉ PFCAs (PFHxA, PFPeA, PFBA) rise and fall over milling time, clearly acting as intermediates from fluorotelomers and other precursors [R13].
  - PFOS itself behaves as a transient intermediate in soil (formation then disappearance) [R13].

- **Photocatalysis**  
  - The PFOA study infers short-chain PFCAs and partially oxidized intermediates from ATR‑FTIR and mass balance; direct LC‑MS TP identification was not completed [R14]. For PFOS, short-chain fluorinated products are also inferred rather than comprehensively quantified [R14].

- **Electrochemical oxidation (landfill leachate & groundwater)**  
  - High-resolution suspect/non‑target screening reveals numerous novel PFAS classes (e.g., FASHN, MeOH‑FASA, H‑PFSA, PFPrES, multiple sulfonamide/sulfonate-related PFAS) plus chlorinated/brominated byproducts [R15].

Transformation-product analysis therefore shows that **disappearance of a targeted parent almost never corresponds to immediate defluorination or mineralization**; it often coincides with formation of other PFAS (sometimes more mobile or unregulated).

---

### 2.3 Fluoride release and defluorination

Fluoride measurements span a wide methodological rigor—from absence/presence to nearly quantitative fluorine balances.

**Nearly complete or very high defluorination in liquids**

- **BN–ball milling of AFFF**  
  - 99.7% defluorination (DeF) for 100 µL undiluted AFFF in 6 h; >98% for 200 µL in 8 h [R12]. DeF is based on IC‑measured F⁻ and [TOF]₀ from CIC/IC [R12].  
  - Authors equate “near-complete defluorination” with mineralization and risk mitigation, but only fluorine (not carbon) is tracked [R12].

- **HALT single 2 h run on 10× AFFF**  
  - Measured F⁻ corresponds to 120.5% of theoretical fluorine from 40 quantified PFAS [R06]; authors correctly note the theoretical fluorine underestimates actual fluorine because of unmeasured PFAS. This is strong evidence that **at least** all fluorine bound in the quantified PFAS plus some additional fluorine from unquantified PFAS is released as F⁻ in the liquid phase.

- **PFOS SCWO (batch & continuous)**  
  - Batch PFOS at 500 °C, 60 min: defluorination 78.2%, with total fluorine mass balance >75% at high temperatures [R01].  
  - Continuous single‑compound PFOS SCWO: “complete defluorination” at 650 °C, 30 s as measured by IC fluoride [R02].

- **PFOS/PFOA/PFHpS continuous SCWO mixture**  
  - At 650 °C, 30 s, authors report complete defluorination with DRE >99.999% [R03]. The text affirms fluoride increases with temperature and PFAS loss, but detailed fluorine-balance closure is not in the excerpts [R03].

- **Field-scale SCWO on 12 PFAAs (AFFF waste)**  
  - Average overall defluorination ratio ~62.6%; partial fluorine balance leaves ~28.1% of theoretical fluorine unrecovered in measured fluoride [R04], so defluorination is substantial but incomplete at the system level.

**Modest or lagging defluorination**

- **Hydrodynamic cavitation (PFOS)**  
  - Defluorination rises to ~20% of initial fluorine at 5 mg/L PFOS [R09], with fluorine mass balance 97–104% across time, indicating that most fluorine remains in PFOS or unobserved intermediates, not as F⁻.

- **GAP plasma (PFOA)**  
  - 17% defluorination vs 21% parent loss in the “energy-efficient” 20 min, 150 W experiment [R08]. Longer runs generate more F⁻ but still lag parent destruction [R08].

- **Photocatalysis (PFOA, PFOS)**  
  - For PFOA in DI water, aqueous F⁻ is only 0.0256 mg of 2.568 mg input (~1% of fluorine) after 120 min; total recovered fluorine (F⁻, residual PFOA, identified TPs, adsorbed) is 2.35% of initial [R14].  
  - PFOS shows similar pattern: 88% parent loss, 23% TOC removal, and reduced fluoride formation in natural matrices [R14].

- **Ultrasonication (PFAS in MQ/SW/CW)**  
  - For 10 ppm PFOA, defluorination reaches 56–86% depending on matrix and salt, while parent loss is higher (often 100%) [R10]. PFOS and 6:2 FTS show the same “removal > defluorination” relationship [R10].  
  - Real GW shows 85% parent loss and lower, unspecific defluorination; mass balance cannot be closed [R10].

- **SCWO of AFFF (Aquarden field demo)**  
  - Fluoride increases from 26.0 mg/L to 97.5 mg/L, while fluorine in 28 targeted PFAS drops from 2.78 mg/L to 0.006 mg/L [R05]. The stoichiometric expectation based on targeted PFAS is 25.9 mg/L F⁻; measured F⁻ is 97.5 mg/L, so targeted PFAS account for only 27% of F⁻. This simultaneously shows strong defluorination of a broader organofluorine pool and large unresolved organofluorine in the influent [R05].

**No F⁻ detected**

- **Electrochemical treatment in DDW**  
  - PFOA and PFOS removal >95% in 1 h, but no fluoride observed for PFAS systems, while non‑PFAS FOCs show substantial F⁻ yields [R11]. This strongly indicates **physical removal (electrocoagulation)** or sequestration, not destruction, under these conditions.

- **Ultrasonic field demonstration**  
  - F⁻ rises as PFAS and AOF decrease, but increase in F⁻ is substantially smaller than decrease in AOF; a significant fraction of organic fluorine is neither remobilized as F⁻ nor accounted for in the targeted PFAS set [R16]. The authors explicitly note that organic fluorine mineralized to F⁻ “did not equate to the total decrease in moles of AOF” [R16].

Collectively, fluoride measurements make clear that **defluorination frequently lags parent destruction**; even when defluorination is high at the scale of a run with analytical PFAS, field- or mixture‑level fluorine balances often reveal large unrecovered fractions.

---

### 2.4 Fluorine mass balance and “total organofluorine” change

Relatively few studies attempt a structured fluorine mass balance; when they do, unresolved fractions are common and informative.

- **HALT 2 h AFFF (bench)**  
  - Theoretical fluorine from 40 PFAS analytes: ~21 887 mg/L; measured fluoride = 120.5% of that value [R06]. Because theory underestimates actual fluorine, this strongly indicates near‑complete defluorination of **both** measured and additional, previously unmeasured PFAS—but gives no carbon speciation.

- **HALT industrial wastewater (pilot)**  
  - Formal definitions for %Defluorination and %F mass recovery based on [IF] and [TOF] are given, and the system measures IF, TOF, and volatile organofluorines (VOFs) [R07]. The excerpts, however, do not provide final %DeF or %F recovery values; conceptually, this is one of the few studies attempting full fluorine partitioning (liquid TOF, IF, VOF) at pilot scale.

- **Hydrodynamic cavitation**  
  - For 5 mg/L PFOS, fluorine mass balance ([F⁻] + PFOS‑bound F) stays within 97–104% of initial fluorine throughout the run [R09]. This is a rare example where **nearly all fluorine remains accounted for in either PFOS or F⁻**, and shorter-chain PFCAs are not detected above 0.05 mol% [R09].

- **Photocatalysis (PFOA)**  
  - The PFOA fluorine balance after 120 min accounts for only 2.35% of the theoretical fluorine across aqueous F⁻, residual PFOA, TPs and catalyst-adsorbed F [R14]. The authors interpret this as strong evidence that most fluorine remains in uncharacterized organofluorine pools and/or analytical blind spots rather than as F⁻.

- **Field-scale SCWO (McDonough)**  
  - Partial balance: theoretical influent organic F (~8 465 mg/L corrected to ~8.47 g/L) versus liquid-phase F⁻ and PFAAs shows average defluorination ~62.6%; ~28.1% of fluorine remains unrecovered [R04].

- **Aquarden SCWO on 100× AFFF**  
  - Stoichiometric F from detected PFAS (influent) explains only 27% of measured effluent F⁻ [R05]. This shows that most F⁻ released derives from PFAS and organofluorine **outside** the targeted list, confirming the incompleteness of targeted panels and the need for TOF/EOF/TOP.

- **FSE method paper**  
  - Evaluates fluoride measurement only, with no PFAS measurements, and stresses that increased F⁻ is a strong but non‑exclusive indicator of PFAS degradation; multiple transformation pathways and incomplete PFAS characterization mean that F⁻ cannot be equated with complete mineralization [R17].

Together, these balances show that **fluorine accounting is essential to distinguish “true destruction” from mere parent loss**, but even the best current implementations leave non‑trivial unresolved fractions.

---

### 2.5 Mineralization-related endpoints

Under the task boundaries, “mineralization” requires at least some carbon‑fate evidence, not just defluorination:

- **TOC as mineralization proxy**
  - Photocatalysis: TOC removal is 27.1% for PFOA (vs 93% parent loss) and 23% for PFOS (vs 88% parent loss) after 120 min [R14]. This unambiguously demonstrates that **most organic carbon from PFAS remains in organic form**, even where authors refer to mineralization.
  - BN‑ball milling of AFFF: ~50% of TOC remains after BN‑BM treatment [R12], again showing that near‑complete defluorination of the fluorine pool does not equate to carbon mineralization.

- **SCWO / HALT**
  - Several SCWO and HALT papers use “mineralize” conceptually but do not report CO₂ or inorganic carbon data in the provided text [R01, R03, R02, R04, R06, R05]. Their strongest support for “mineralization” is combination of high PFAS DRE, substantial fluorine release, and in some cases COD reduction (e.g., from 4 750 to 5.17 mg/L in Aquarden’s effluent [R05]). COD reduction does indicate oxidation of organic matter but not necessarily complete conversion of PFAS carbon to CO₂ vs other oxidized organics.

- **Hydrodynamic cavitation & GAP**  
  - The HC and GAP studies interpret high fluoride yield per degraded PFOS/PFOA (where present) and absence of shorter-chain intermediates above low detection limits as “near-complete mineralization” of the fraction that enters reaction zones [R09, R08]. However, neither measures CO₂ or total carbon balances. By the present rubric these are **strong defluorination/fluorine-balance endpoints but not proven mineralization**.

- **Ultrasonication field study**  
  - Authors explicitly frame high-frequency ultrasound as “mineralizing” PFAS to F⁻ and CO₂ based on prior bench work [R16], but in the field trial they measure only PFAS, AOF and F⁻; CO₂ or carbon balances are absent, and AOF vs F⁻ changes demonstrate incomplete conversion of organic fluorine to F⁻.

In sum, TOC and COD provide partial mineralization information, but **no study in this table closes both fluorine and carbon mass balances sufficiently to claim complete mineralization of a complex PFAS mixture**.

---

## 3. How analytical scope, sampling time, and detection limits condition interpretation

### 3.1 Analytical scope

- **Target list limitations**  
  - AFFF and industrial matrices contain many more PFAS than appear in typical 12‑, 24‑, 28‑ or 40‑analyte panels; this is explicit in SCWO [R05], HALT [R06], MCD [R13], HALT pilot [R07], EO [R15], and multiple ultrasonication studies [R10].
  - Significant portions of fluoride and organofluorine cannot be linked back to identified PFAS because TF or TOF is not measured (e.g., SCWO continuous‑mixture [R03, R02], many plasma and ultrasonic runs [R10, R08]).

- **Transformation-product coverage**  
  - Even in high‑resolution LC‑HRMS/QTOF regimes (photocatalysis [R14], EO [R15], ultrasonication [R10], plasma [R08]), ultrashort PFCAs (TFA, PFPrA) and non‑PFAS organofluorines are challenging to detect and quantify in complex matrices [R10, R14, R15].  
  - EO and non‑target studies highlight that **numerous novel PFAS classes and other halogenated compounds** can form during treatment [R15], underscoring that focusing only on a familiar PFAS suite is inadequate.

### 3.2 Sampling time / kinetics

- Several technologies exhibit **decoupled kinetics**:
  - BN‑ball milling: defluorination shows an “incubation period” before a sharp increase; PFAS loss precedes F⁻ release [R12].  
  - GAP plasma: PFOA destruction proceeds faster than defluorination [R08].  
  - Ultrasonication: PFOA/PFOS/6:2 FTS degradation efficiencies exceed defluorination across matrices [R10].  
  - SCWO: defluorination lags DRE at intermediate temperatures [R03].

Early‑time sampling may thus show high DRE but modest defluorination, misleadingly suggesting effective “destruction” if fluorine endpoints are not systematically sampled over time.

### 3.3 Detection limits and censoring

- **Fluoride detection limits**  
  - IC LOD for F⁻ in ball‑milling and SCWO work is ~50 µg/L [R12, R06, R05]. FSE low‑spike MDL is ~0.2 mg/L [R17]. If expected defluorination corresponds to F⁻ below these thresholds, lack of detection is not strong evidence of no defluorination.

- **PFAS MDLs and LOQs**  
  - SCWO single‑compound and mixture studies use LC‑MS/MS LODs down to 0.05 ppb, LOQs 0.01–0.1 µg/L, and targeted 24–40 analyte lists [R02, R08]. Even so, PFHxS and other PFAS can be “present but <MDL”, which appears as “not detected” yet still contributes fluorine [R03].  
  - Ultrasonication, HALT, and electrochemical work likewise acknowledge that TBD ultrashort PFAS and unknown precursors fall below routine MDLs [R07, R11, R10, R14].

Because of this, **“PFOA not detected” or “PFAS below MDL” cannot be conflated with destruction**, particularly when product suites and fluorine/TOC balances are incomplete.

### 3.4 Unidentified products and unmeasured phases

- **Unmeasured gaseous or sorbed fractions** arise repeatedly:
  - Batch PFOS SCWO: poor fluorine balance at 425–450 °C is attributed to lower MW fluorinated species in gas and/or liquid phases that are not analyzed [R01]. Gases are explicitly not analyzed [R01].  
  - Field-scale SCWO and Krause’s AFFF demos: small volatile organofluorines and smaller PFCAs are known possible byproducts but are not comprehensively quantified in each demo [R04, R05].  
  - Plasma, ultrasonication and photodegradation create particulate or polymerized products requiring filtration before LC analysis [R08, R14], implying that some fluorine resides in non‑dissolved fractions that are rarely characterized.  
  - EO (Boron‑doped diamond) clearly forms numerous previously unrecognized PFAS and halogenated TPs [R15].

The **presence of these unresolved fractions is the main reason that strong parent loss plus F⁻ cannot be upgraded to “complete destruction” without direct measurement**.

---

## 4. A defensible evidence hierarchy for PFAS destruction and mineralization

Based strictly on the reported metrics and their limitations, an evidence hierarchy can be constructed.

### Level 0 – Parent-compound loss only

**What is measured:** Decrease in targeted PFAS concentrations in a given phase.

**Strengths:**  
- Demonstrates removal of monitored PFAS from the measured phase.  
- Essential for regulatory compliance against concentration limits.

**Limitations:**  
- Does not distinguish between:
  - Transformation to other PFAS / organofluorine.
  - Phase transfer (e.g., sorption, volatilization, coagulation).
  - True chemical destruction.  
- Completely silent on fluorine fate and carbon mineralization.

**Examples:**  
- EC in DDW (PFOA/PFOS removal with no F⁻) [R11].  
- Many electrochemical, ultrasonic and plasma continuous runs that don’t report fluoride or TPs.

**Appropriate interpretation:**  
- “Parent PFAS X decreased by Y% in phase Z under condition C.”  
- No claims of defluorination, mineralization, or overall destruction.

---

### Level 1 – Parent loss + qualitative TP evidence

**What is measured:** Parent PFAS loss plus observation of selected transformation products, often shorter-chain PFCAs/PFSAs or structural analogues.

**Strengths:**  
- Demonstrates that PFAS are chemically transformed rather than only removed.  
- Identifies potential daughter PFAS and byproducts.

**Limitations:**  
- Mass fractions in TPs often small relative to parent loss; large unaccounted fluorine remains.  
- Usually no quantitative fluorine balance or TOC.

**Examples:**  
- GAP plasma: PFOA from PFOS, PFOS from 8:2 FTS; chain-shortening PFCAs [R08].  
- Ultrasonication: PFPeA, PFHxA, PFHpA & PFHpS from PFOA/PFOS/6:2 FTS [R10].  
- EO: new PFAS classes and halogenated TPs in landfill leachate and groundwater [R15].  
- SCWO continuous PFOS: suite of PFCAs plus VOFs [R02].  
- MCD of AFFF/soil: transient PFCA intermediates, PFOS as intermediate from precursors [R13].

**Appropriate interpretation:**  
- “Parent PFAS X is transformed to intermediate suite Y under condition C; significant transformation-product burden remains.”  
- Still not evidence for full defluorination or mineralization.

---

### Level 2 – Parent loss + F⁻ measurement (defluorination) without fluorine balance

**What is measured:** Parent PFAS loss and aqueous F⁻; DeF (%) relative to initial parent-bound fluorine; no attempt to close total F.

**Strengths:**  
- Shows that a defined fraction of PFAS-bound fluorine is released as F⁻.  
- Confirms C–F bond cleavage.

**Limitations:**  
- No accounting for:
  - Fluorine still in TPs and precursors.  
  - Fluorine in gases/solids or unidentified organofluorines.  
- Cannot quantify how close the system is to complete defluorination.

**Examples:**  
- Batch PFOS SCWO (DeF up to 78.2%) [R01].  
- PFOA GAP plasma (17% DeF at 20 min vs 21% destruction) [R08].  
- HC of PFOS (~20% DeF, 97–104% mass balance for parent+F⁻ but no TP F) [R09].  
- Plasma, photocatalysis, ultrasonication with F⁻ reported but without holistic F mass balances [R10, R08, R14].

**Appropriate interpretation:**  
- “Treatment produces X% conversion of parent-bound fluorine to aqueous F⁻; substantial fluorine remains in organic form or other phases.”

---

### Level 3 – Partial fluorine mass balance (parent + some TPs + F⁻)

**What is measured:** Parent PFAS, a limited set of TPs (e.g., PFCAs, PFSAs, FtS), and aqueous F⁻. Sometimes COD/TOC.

**Strengths:**  
- Can partition fluorine between parent, targeted TPs, and F⁻.  
- Can identify trends where defluorination lags parent loss.  
- COD/TOC reductions give some carbon-oxidation context.

**Limitations:**  
- Target list is incomplete; non‑target PFAS and non‑PFAS organofluorine not captured.  
- Gas phase, sorbed phases, and polymerized solids are often unmeasured.  
- Total closure is rarely achieved; unresolved fractions persist.

**Examples:**  
- PFOA fluorine mass balance under photocatalysis (2.35% of F accounted; remainder in uncharacterized pools) [R14].  
- PFOA and other PFAS in GAP reactor: low fraction of parent lost appears as TPs; defluorination slower than destruction [R08].  
- PFOA mass balance in GAP showing parent loss from 70 100 to 52 800 µg/L with low TP F [R08].  
- Continuous SCWO mixture (Austin, Li) – overall fluorine balance is discussed qualitatively; specific closure values incomplete in excerpts [R03, R02].

**Appropriate interpretation:**  
- “Within the measured PFAS and fluoride pools, X% of initial fluorine is accounted for; unresolved fluorine likely resides in unmeasured organofluorines or phases.”

---

### Level 4 – Near-closed fluorine balance

**What is measured:** Parent PFAS, F⁻, and (ideally) all fluorine-bearing species at least in the aqueous phase or across liquid and solid phases; mass balance closure ~100%.

**Strengths:**  
- Strongest available evidence for defluorination and absence of significant fluorinated intermediates in measured phases.  
- If accompanied by broad PFAS/TOP/TOF/EOF coverage, can substantially constrain unmeasured PFAS burdens.

**Limitations:**  
- Few examples; often still lack full carbon balance and gas-phase analysis.  
- Closure may be limited to specific conditions (e.g., single PFAS at moderate concentration) and may not extrapolate to complex mixtures.

**Examples:**  
- HC PFOS at 5 mg/L: fluorine mass balance 97–104% using PFOS‑F + F⁻; no chain-shortened PFCAs >0.05 mol% detected in water [R09]. This implies that nearly all fluorine remains as PFOS or F⁻ in the aqueous system under those conditions, but does not rule out minor gaseous/solid-phase fluorine.  
- HALT single 2 h run on AFFF: fluoride at 120.5% of theoretical PFAS-derived fluorine; because theoretical fluorine is an underestimate, this is consistent with essentially complete defluorination of both measured and unmeasured PFAS into aqueous F⁻ [R06]. However, carbon fate is not resolved.

**Appropriate interpretation:**  
- “Within the measured system, nearly all fluorine initially bound in PFAS has been liberated as F⁻; carbon fate remains unresolved and some fluorine may be in unmeasured phases.”

---

### Level 5 – Joint fluorine and carbon mineralization evidence (not yet achieved here)

**What would be required (not present in this evidence set):**

- Closed fluorine mass balance (F⁻ plus measured TOF/EOF/TOP and gas/solid fractions).  
- Near-closed carbon balance, including CO₂ or inorganic carbon quantification, TOC reduction to near‑background, and characterization of residual organics.  
- Demonstration that residual organic carbon is not fluorinated or toxicologically problematic.

None of the retained studies fully meet this standard; even the strongest (HALT and selected SCWO cases) stop at high defluorination plus parent loss and COD/TOC reductions, with unresolved fluorine or carbon.

---

## 5. Practical implications and research priorities

### 5.1 Technology- and scale-specific trade‑offs

- **SCWO and HALT** are currently the most advanced in terms of combining parent loss, defluorination, and (in some cases) COD/TOC reduction—particularly for concentrated waste streams (AFFF, industrial brines) [R01, R03, R02, R04, R06, R05]. However:
  - Field‑scale SCWO still leaves 20–30% of fluorine unresolved, and shorter-chain PFAAs/VOFs can appear as products [R01, R02, R04, R05].  
  - HALT bench and pilot cases demonstrate high defluorination and near‑complete PFAS disappearance, but TOC and TP characterization are incomplete, especially for ultrashort PFAS [R07, R06].

- **Ball milling and mechanochemistry** show that near‑complete defluorination of AFFF and very high targeted PFAS destruction are possible in solids and undiluted foams [R12, R13], but:
  - Only one AFFF BN–BM study reports defluorination with solid‑phase fluorine artifacts (e.g., Si–F) explicitly considered [R12].  
  - Carbon fate and scalability remain open questions; TOC suggests substantial residual organic carbon [R12].

- **Plasma, ultrasound, photocatalysis, and hydrodynamic cavitation**:
  - Can achieve rapid parent PFAS loss, but often display defluorination lag and persistent short-chain/intermediate PFAS [R09, R10, R08, R14].  
  - Very little work closes even a liquid‑phase fluorine balance, and carbon mineralization is limited (TOC reductions ≪ parent loss) [R10, R14].

- **Electrochemical oxidation (PFAS mixtures)**:
  - Proof-of-concept EC in DDW is a cautionary example: near‑quantitative parent removal with zero F⁻ indicates pure separation rather than destruction [R11].  
  - EO with BDD anodes on landfill leachate shows broad transformation to many novel PFAS and other halogenated products but no fluorine mass balance [R15].

### 5.2 Priority measurement needs to differentiate disappearance, defluorination, and destruction

To avoid over‑interpreting parent loss as destruction or mineralization, future PFAS destruction work should, at a minimum:

1. **Always pair parent PFAS DRE with F⁻ measurements** in relevant phases (aqueous, and gas when expected), with detection limits and calibration ranges clearly reported.

2. **Implement fluorine mass balances** wherever possible:
   - At least: parent PFAS, major TPs, F⁻ in water, and solid/gas fractions when plausible.  
   - Preferably: TOF/EOF/TOP to capture non‑target PFAS and organofluorines.

3. **Include TOC (and where feasible, CO₂) measurements**, especially for technologies claiming mineralization. TOC markedly below parent loss is strong evidence for incomplete carbon destruction [R12, R14].

4. **Use transformation-product screening beyond a narrow target list**:
   - High-resolution LC–HRMS suspect/non‑target workflows (as in EO work [R15]) should be integrated into destruction trials.  
   - Mechanistic coverage should specifically include short- and ultrashort-chain PFCAs/PFSAs (TFA, PFPrA, etc.), which current routine methods often miss [R10, R17, R14].

5. **Account for matrix effects and sampling times**:
   - Report time‑resolved PFAS, F⁻, TOC and key TPs to capture lagging defluorination and transient increases in intermediates [R12, R01, R10, R08].  
   - Evaluate representative real matrices, not only clean waters; natural organic matter, salinity, competing anions and co‑contaminants clearly suppress defluorination and mineralization [R07, R10, R14, R15].

6. **Characterize residual streams explicitly**:
   - For solids (e.g., ball‑milled powders, sorbents, precipitates), measure residual organofluorine and leachable F⁻.  
   - For gas streams (SCWO, plasma, EO), deploy standardized methods (e.g., OTM‑45, dedicated VOF/F‑sampling) and include them in mass balances [R03, R04, R17, R05].

### 5.3 A concise decision framework for interpreting reported data

Given the above hierarchy, a defensible practice is:

- **If only parent PFAS loss is reported** → conclude removal or transformation of monitored species only; **do not** infer defluorination or mineralization.

- **If parent loss + F⁻ are reported but no fluorine balance** → quantify the fraction of parent fluorine converted to F⁻. Conclude partial defluorination; avoid claims of complete destruction.

- **If partial fluorine balance is available (parent+TPs+F⁻)** → quantify accounted fluorine; explicitly report the unresolved fraction and hypothesize but do not assert its form.

- **If near-closed fluorine balance is shown** → cautiously infer near‑complete defluorination within the measured system, while still requiring carbon data before asserting mineralization.

- **Only when both fluorine and carbon balances are near‑closed, and TPs are fully constrained** would it be justified to describe PFAS “complete destruction and mineralization” in a strict sense. No current case fully meets this bar.

---

## 6. Summary

The structured evidence confirms that:

- **Parent PFAS disappearance is the weakest and most easily misinterpreted endpoint**; by itself it neither guarantees defluorination nor the absence of equally or more problematic transformation products.
- **Fluoride release is essential but not sufficient**: it measures defluorination of some fraction of the fluorine pool but says nothing about carbon fate or about fluorine in untracked PFAS and phases.
- **Fluorine mass balance and TOC (or carbon balances) provide the strongest evidence gradient toward true destruction**, yet even state‑of‑the‑art studies usually leave a consequential unidentified fluorine and/or carbon fraction.
- **Analytical scope, detection limits, matrix complexity, and sampling design fundamentally control interpretability**. Unidentified products and unmeasured phases are ubiquitous and must be assumed unless disproven by comprehensive balances.

A cautious, hierarchy‑based interpretation—explicitly tied to which of parent loss, TPs, F⁻, fluorine balance, and carbon endpoints are actually measured—is essential to avoid overstating PFAS “destruction” or “mineralization” and to identify where technologies genuinely approach end‑of‑life treatment for PFAS versus where they mainly redistribute fluorine within and between phases.

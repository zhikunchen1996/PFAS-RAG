### 1. Scope and decision context

This review focuses on **selecting among membrane-based PFAS separation processes**—nanofiltration (NF), reverse osmosis (RO), adsorptive/“dual-function” membranes, electrically assisted or stimulus‑responsive membranes, and hybrid membrane–sorbent configurations—for specific **PFAS mixtures, water matrices, and treatment objectives**.

Across the evidence set, PFAS are present in:

- **Groundwater (AFFF‑impacted)** at ng/L–µg/L levels [S08, S09, S03].
- **Drinking-water groundwater** with mixed PFAS at low ng/L [S10, S01].
- **Tertiary wastewater effluent** [S07].
- **Canal surface water** [S13].
- **Industrial wastewaters**, notably **semiconductor fab wastewater** [S14] and mixed industrial wastewater [S11].
- **Synthetic waters** used to isolate mechanisms [S04, S05, S06, S11, S12].

Treatment objectives range from meeting **drinking-water PFAS limits** [S10, S06, S09], to producing **reuse-quality permeate from wastewater** [S07, S14], to **concentrate production for downstream destruction** [S09, S10, S14] or adsorptive polishing [S07].

Below, I first contrast **separation mechanisms** by technology class, then evaluate how PFAS and matrix properties plus operating conditions shape performance, and finally define **when data are sufficiently comparable** to support process selection.

---

### 2. Separation mechanisms: NF, RO, adsorptive & hybrid membranes

#### 2.1 Conventional NF and RO (size and charge–based separation)

**Size exclusion and electrostatic interactions** are consistently identified as dominant for NF/RO PFAS rejection:

- In synthetic matrices, NF90 and BW30 RO rejections tracked **PFAS molecular weight (213–499 g/mol)** and charge; **size exclusion** dominated for longer‑chain PFAS, with **electrostatic effects** especially important when PFAS size approached or was below NF pore size [S06-E06, S06-E02].
- **RO (BW30‑2540)** achieved **>99% rejection** of most tested PFAS across chain lengths when operated at high pressure [S06-E04].
- **NF90‑2540** provided **90–99% rejection** for most PFAS, with somewhat lower rejection for the smallest species [S06-E06, S06].

For **commercial NFs** spanning a wide MWCO range, a systematic stirred‑cell study showed:

- Across five NF membranes, rejection of 12 PFAS (legacy + PFEA + FTS) ranged from **66.0% to >99.9%** [S05-E05, S05].
- Membrane performance ranked **DK > NF90 > XN45 > NF270 > DL** under identical synthetic groundwater conditions (100 µg/L each PFAS, 7 bar, pH ≈5.5) [S05-E05, S05-E07].
- Correlation analysis found **membrane MWCO, water permeability, and MgSO₄ rejection** more predictive of PFAS removal than surface hydrophilicity or charge, indicating **steric hindrance** as the primary control [S05-E03, S05-E08].

**Implication for selection:** For a given matrix, **tight NF (low MWCO) and RO** behave predominantly as size/charge sieves; high rejections for ≥C4 PFAS are robustly supported, whereas short‑ and ultrashort‑chain performance is more variable and sensitive to matrix.

#### 2.2 Loose NF and “direct NF” for drinking water and wastewater

Multiple pilot and bench systems use relatively **loose NF** as a compromise between energy and PFAS rejection:

- **NF270 on tertiary wastewater effluent**: at **90% recovery**, a pilot NF270 achieved
  - **>92% rejection** of **C ≥ 4 PFAAs**,
  - **>98% rejection** of **GenX**,
  - **63–92% rejection** of ultrashort‑chain PFAS [S07-E04].
- **NF270 on AFFF‑impacted groundwater** (pilot, semi‑batch): NF270 provided **92–98% rejection** for a 12‑PFAS suite at **90% recovery** [S09-E04, S09].
- **NF in drinking‑water groundwater**: a two‑stage NF90‑400/NF270‑400 pilot on Swedish groundwater achieved **>98% PFAS removal** (Σ11 PFAS) with **80% recovery** [S10-E06, S10]. PFHxA accumulated in the NF concentrate from **4.5 ng/L in raw water** to **25 ng/L** [S10-E05], illustrating separation rather than destruction.
- **Loose NF in surface water (Florida canal)**: a polypiperazine amide NF (MWCO 500 Da, isoelectric point ~4) removed long‑chain PFOA and PFOS more effectively than short‑chain PFBA and PFBS from canal water; short‑chain removal improved when combined with sorption pretreatment (see §3.4) [S13-E04, S13-E02].

These results indicate that **loose NF can be sufficient for regulatory control of long/medium‑chain PFAS in many drinking‑water and reuse applications**, but **short‑ and ultrashort‑chain species (PFBA, PFBS, TFA, TFMS)** remain more challenging.

#### 2.3 Adsorptive / dual‑functional NF membranes

Two lines of work explicitly add **adsorptive functionality** to pressure‑driven membranes.

**(a) PNIPAm‑functionalized NF (NF‑PNIPAm‑PVDF)**

- NF‑PNIPAm‑PVDF consists of a polyamide NF layer over a **PNIPAm‑functionalized PVDF support** [S04-E04].
- In **cross‑flow NF** (type‑I water, 70 µg/L each PFOA, GenX, PFBA; 2 mM CaCl₂; pH ~5.7; 7 bar; ~100 L/m²·h):
  - Steady‑state rejection was **~70%** for **PFOA and GenX**, and **~50%** for **PFBA** [S04-E01, S04-E05].
- In **batch adsorption** at much higher concentration (PFOA 70 mg/L), the same membrane had an adsorption capacity **qₑ = 178 mg/m²**, with **≈26%** of this capacity regenerable by water at 22 °C [S04-E03, S04-E08, S04].

The authors interpret performance as combining NF exclusion with **significant PFOA sorption** in the PNIPAm‑PVDF support [S04-E03, S04-E08]. However, mechanistic apportionment between convective rejection and adsorption at environmental ng–µg/L remains only qualitatively supported.

**(b) QA‑grafted PVDF “pH‑swing” adsorptive membranes**

Wan et al. grafted **quaternary ammonium (QA) anion‑exchange brushes** onto PVDF to create a **high‑permeability, adsorptive membrane** operated in dead‑end mode [S12-E01, S12-E02]:

- In **synthetic groundwater (1 mM NaH₂PO₄, 5 mM NaCl, 0.24 µM PFOA)**, QA‑grafted membranes (QA loading 1.1 mmol/g) achieved:
  - **>90% PFOA removal** at a **treatment capacity of 570 L/m²**, with water permeability **165.6 L/m²·h·bar** [S12-E05].
  - **>97% desorption** of PFOA during regeneration at **pH 12.5 with 5% methanol**, enabling **≈10‑fold enrichment** of PFOA in the regenerant across cycles [S12-E04, S12-E05].
  - Across **three adsorption/regeneration cycles** and cumulative treated volume **2930 L/m²**, total PFOA removal was reported in the low‑80s% range, with two discrepant values (82.4% and 84.7%) in different sections [S12-E03, S12-E05]; only the **order of magnitude** (≈80–85%) is securely supported.

Separate batch isotherms yielded **maximum capacities Qₘ = 0.65 mmol/g for PFOS and 0.44 mmol/g for PFOA**, highlighting strong **sorption‑dominated separation** and increased capacity for the more hydrophobic PFOS [S12-E05, S12].

**Key distinction:** In NF‑PNIPAm‑PVDF, adsorption is **secondary and transient** under convective operation (modest steady‑state rejection at low µg/L); in QA‑PVDF, adsorption is the **primary removal mechanism**, with deliberate **pH‑swing desorption** to produce a concentrated PFAS stream.

#### 2.4 Mixed‑matrix membranes (MMM) with MOF/MXene fillers

Minhas et al. embedded **PD@Ti₃C₂Tx‑MOF(Fe) nanocomposite (“DMMIL”)** in a cellulose acetate membrane [S11-E01, S11-E04]:

- In **synthetic 10‑ppm PFOA solution** (unbuffered) at **3.5 bar**, the 50%DMMIL/CA MMM achieved **91.4% PFOA removal** [S11-E01].
- **DI water permeability** reached **7.8 L/m²·h·bar** for a 20%DMMIL/CA variant [S11-E01].
- In **real wastewater** with ∼1 ppm total PFAS, the 50%DMMIL/CA membrane removed **PFOA 60%, PFHpA 57%, PFHxA 55%**, with **wastewater permeability 3.9 ± 0.5 L/m²·h·bar** [S11-E04, S11-E07, S11].
- Flux‑recovery tests showed **substantial reversible fouling**, with a 20%DMMIL/CA membrane maintaining **68% cumulative FRR over 5 cycles** in 10 ppm PFOA [S11-E05].

These MMMs behave as **low‑pressure NF/UF‑like membranes with significant adsorption sites** in the nanocomposite phase; removal in real wastewater is clearly **adsorption‑limited by matrix competition** [S11-E06], not purely size exclusion.

#### 2.5 Forward osmosis / pressure‑stimuli NF (PSRNF)

Aedan et al. evaluated a **pressure‑stimuli‑responsive NF (PSRNF) membrane** operated in **forward osmosis (FO) mode** with seawater draw and **0–4 bar** applied on the feed [S03-E04, S03-E06]:

- For PFAS‑contaminated groundwater containing a wide suite from **TFA and TFMS** up to **PFDA** [S03-E01]:
  - At **pH 4 and 0 bar**, **long‑chain PFAS rejection 97.9%**, **short‑chain 93.3%** [S03-E05].
  - **Adsorption at the membrane surface** was highest for long‑chain PFAS and decreased with increasing pressure and pH; under alkaline, high‑pressure conditions, adsorption of short/ultrashort PFAS was **not detectable** [S03-E06, S03-E08].
- FO‑PSRNF showed **high flux** (e.g., 48.95 L/m²·h with DI water at 4 bar, 90% recovery [S03-E06]) and **moderate fouling mostly reversible** by warm DI water cleaning [S03-E05, S03].

Mechanistically, PSRNF combines **osmotic plus low hydraulic driving force**, NF‑scale pores (~21.3 nm apparent from FO modeling [S03-E06]) and **chain‑length dependent adsorption** that can be suppressed at higher pH/pressure.

#### 2.6 Electrically assisted membranes

None of the verified records include **electrically driven transport (e.g., electrodialysis, electro‑NF)**; “electrically assisted membranes” therefore remain **an evidence gap** in this dataset. Selection guidance for such systems cannot be grounded in these studies.

#### 2.7 Hybrid NF + adsorbents

Two scales are represented:

- **NF + GAC/IX for drinking water**: At the Bäcklösa DWTP, NF90/NF270 NF produced a **concentrate stream ≳10% of feed volume** with elevated PFAS [S10-E06, S10-E01]. This concentrate was then treated with GAC or AIX in column tests; NF + adsorbents was economically favorable under certain discharge limits [S10-E07].
- **Loose NF + GAC/IX for tertiary wastewater**: In the Colorado study, NF270 pretreatment (90% recovery) reduced PFAS, effluent organic matter (EfOM), and interfering ions prior to GAC/IX, significantly improving PFAS breakthrough profiles in the downstream adsorbents [S07-E04, S07-E07].

These hybrids exploit **size/charge separation in NF** to simplify the matrix for **downstream adsorption**, rather than relying on membrane adsorption.

**Caution:** In pilot and field systems, PFAS also **sorb irreversibly to non‑designed surfaces** (filters, membrane elements, resins, greensand), creating residual PFAS reservoirs that need management [S08-E03, S08-E07].

---

### 3. Effects of PFAS properties, membrane characteristics, and operating conditions

#### 3.1 PFAS chain length and functional group

Across multiple studies, **longer chains and sulfonates are more easily rejected and more strongly sorbed**:

- NF and RO: DK and NF90 showed **excellent removal of short‑chain C3–C4 PFAS**, but overall, longer‑chain PFEA/FTS still had **higher rejection** (up to >99.9%) [S05-E06].
- In NF270 wastewater effluent, **C ≥ 4 PFAAs had >92% rejection**, while **ultrashort PFAS only 63–92%** under the same conditions [S07-E04].
- NF90 and BW30 in AFFF‑groundwater: **PFAS rejection increased with perfluoroalkyl chain length**; NF90 achieved **97.9–99.8%** across C4–C8 PFCAs/PFSAs [S08-E03]; BW30 gave **>99% specific rejection** but with high energy cost [S08-E03, S08].
- Adsorptive QA‑PVDF: **Qₘ was higher for PFOS (0.65 mmol/g) than PFOA (0.44 mmol/g)**, supporting a strong **hydrophobic contribution** beyond electrostatics [S12-E05].
- DMMIL/CA MMM: long‑chain PFOA removal (both synthetic and real wastewater) exceeded that for PFHpA and PFHxA under identical conditions [S11-E04, S11-E06, S11-E07].

**Functional group** also matters:

- In NF90/NF270 systems, **PFSAs often show slightly higher rejection than PFCAs of the same chain length**, but substituted FTS can have lower rejection than PFOS [S05-E06].
- In NF90 NF for fab wastewater, **ultrashort PFCA (TFA) showed the lowest rejection (93.7%) among the measured PFAS**, while TFMS and PFBS were slightly higher (95–96.5%) [S14-E08].

**Selection implication:** For feeds dominated by long‑chain PFOS/PFOA and analogues, **loose NF (NF270) or tight NF (NF90, DK) is often adequate**. Where **short/ultrashort PFAS (TFA, PFBA, PFBS)** dominate, **tighter NF/RO** or **adsorptive membranes/pretreatment** are usually necessary if very low permeate targets are required.

#### 3.2 Membrane MWCO, pore size, and structural changes

- **Bench NF membrane set (MWCO 150–1200 Da)**: lower MWCO correlated strongly with higher PFAS rejection across 12 PFAS [S05-E03, S05-E08].
- **NF90 pore expansion under high salinity:** For NF90, pristine pore radius was **0.45 ± 0.07 nm**; after **24 h filtration of 1000 mM NaCl**, pore radius increased to **0.64 ± 0.06 nm** [S06-E03]. This implies potential **loss of selectivity for smaller PFAS** at very high ionic strength.
- **Loose NF for canal water:** The polypiperazine NF (MWCO 500 Da) is explicitly described as a **“rather loose NF membrane”**, chosen so that Donnan effects and matrix interactions could be studied; as expected, it did not fully reject short‑chain PFBA/PFBS [S13-E04, S13-E07, S13-E08].

**Selection implication:** For **highly saline feeds** or long‑term operation at high ionic strength, NF pore expansion must be considered; **RO or very tight NF** may be warranted where small PFAS must remain below detection across years of operation.

#### 3.3 Pressure, flux, and recovery

**RO (BW30) and NF (NF90/NF270)**:

- **RO BW30:** Flux increased roughly linearly with pressure until **~41.37 bar**, above which flux plateaued near **100 L/m²·h**, attributed to **compaction of water transport pathways** [S06-E04]. PFAS rejection remained >99% across this range [S06-E04].
- **NF90 (Ma et al.)**: NF rejection was 90–99% for most PFAS, with electrostatics particularly important for the shorter chains [S06-E06, S06].
- **NF270/NF vs RO (Liu et al.)**:
  - At **18.8 LMH** and **90% total recovery**, NF270 provided 92–98% PFAS rejection [S09-E04].
  - In the same matrix, an RO (ESPA) membrane maintained **≥99% rejection** of all PFAS even at **97% recovery** [S09-E02, S09-E08]. NF270 rejection of **short‑chain PFSAs decreased** between 90 and 97% recovery [S09-E02, S09].

**Closed‑circuit RO vs tight NF (Masters et al.)**:

- In a **CCMS on AFFF‑groundwater**, NF90 achieved **97.9–99.8%** PFAS rejection at **80–90% recovery**, with lower net driving pressure and higher temperature‑corrected flux than BW30 RO [S08-E03, S08-E04, S08].
- BW30 RO had **>99% specific rejection** but **overall PFAS rejection declined between 85–90% recovery**, with permeate quality clearly degrading beyond ~87% recovery [S08-E03, S08].

**Forward osmosis PSRNF**:

- FO‑PSRNF at 4 bar achieved **48.95 L/m²·h** in DI water and **40.2 L/m²·h** in contaminated groundwater at 90% recovery [S03-E06]. Increasing applied pressure from 0→4 bar tended to **reduce PFAS adsorption** but did not eliminate high rejection at favorable pH [S03-E05, S03-E08].

**Selection implication:**

- If **very high system recoveries (>90–95%)** are required, **RO** is more robust in maintaining rejection than NF, but at significantly higher energy cost and potential compaction.
- For **moderate recovery (80–90%)**, **tight NF (NF90, DK)** may offer **near‑RO PFAS rejection with lower pressure**; **loose NF (NF270)** will often be sufficient for long‑chain PFAS but not for small PFAS in stringent applications.
- FO/PSRNF provides **high flux at low hydraulic pressure**, but PDFS data are currently limited to a single membrane and groundwater matrix [S03].

#### 3.4 Ions, organic matter, and fouling

**Electrolytes and ionic strength**

- In NF/RO PFAS rejection (Ma et al.), **NaCl 0–1000 mM** and pH 4–10 modulated electrostatic interactions; **high ionic strength** reduced electrostatic repulsion and, at 1000 mM NaCl, physically modified NF90 pores [S06-E03, S06-E06].
- In QA‑PVDF membranes, **co‑ions** (e.g., other anions) competently **reduced removal efficiency by 10–20%**, reflecting competition for exchange sites and compression of the electric double layer [S12-E03, S12-E06].
- In the DMMIL/CA MMM, **NH₄⁺ and Mg²⁺** were significantly adsorbed (94% and 46% removal, respectively), while phosphate removal (66%) was limited both by charge shielding and low initial concentration [S11-E08].

**Natural organic matter (NOM) and EfOM**

- NF270 pilot on wastewater effluent: permeability declined over 45 days due to **EfOM/inorganic fouling**, but **PFAS rejection remained stable** across at least the first 30 days [S07-E03, S07-E06].
- NF270 groundwater pilot: in 30‑day operation at 90% recovery, a **52.7% drop in specific flux** attributed to NOM cake formation was observed in QA‑PVDF experiments [S12-E03]; again, PFAS rejection for NF270 in Liu et al. did not change significantly over 30 days, though their groundwater had minimal organic fouling [S09-E04, S09-E06].
- In canal water NF, loose NF experienced **limited flux decline** over 24 h at 100 psi and 0.18 m/s, with only minor flux improvement upon GSM pretreatment [S13-E06, S13-E07]. This was ascribed to the membrane’s **loose character, modest pressure, cross‑flow hydraulics, negative charge, and relatively low foulant load**.

**Fouling behavior of modified membranes**

- MXene‑TiO₂‑modified RO (M3) showed substantially less **permeance decline under compaction (2.5% vs 16% from 8→20 bar)** [S02-E08] and better flux recovery after HA/BSA fouling [S02-E03, S02-E07], indicating improved structural and antifouling robustness.
- DMMIL/CA MMM displayed **better FRR and lower irreversible fouling** than pristine CA in 10 ppm PFOA, due to high porosity and negative surface charge limiting PFOA adsorption [S11-E05].

**Selection implication:**

- In **EfOM‑rich or NOM‑rich waters**, **NF270 and NF90 can retain PFAS performance while fouling degrades flux**, but lifetime and cleaning strategies must be designed.
- **Adsorptive membranes** in complex matrices (DMMIL/CA, QA‑PVDF) suffer strong **competitive adsorption and fouling**, reducing effective PFAS removal relative to clean synthetic waters [S11-E06, S12-E03]. These are better suited as **polishing or preconcentration** steps, not as sole barriers in complex wastewater.

---

### 4. Hybrid configurations and pretreatment impacts

#### 4.1 NF + adsorbents for wastewater effluent and groundwater

- **Tertiary wastewater effluent (NF270 + GAC/IX)**: NF270 at 90% recovery served as a **primary barrier**, reducing PFAS and EfOM; GAC and PFAS‑selective IX then achieved deeper PFAS removal, with NF pretreatment substantially extending adsorbent bed life [S07-E04, S07-E07].
- **Groundwater (NF + GAC/AIX for NF concentrate)**: At Bäcklösa DWTP, NF concentrate (≈10% of feed volume) with elevated PFAS was treated by GAC or AIX; NF + adsorbent trains were cost‑competitive depending on discharge targets [S10-E06, S10-E07].

#### 4.2 Green sorption media (GSM) + NF for canal water

Islam et al. combined **CPS or ZIPGEM green sorption media** with the loose NF [S13-E01, S13-E08]:

- **CPS‑NF**: overall removal of **PFOS and PFOA** was **significantly higher (p<0.05)** than NF alone [S13-E02]. For **short‑chain PFBA/PFBS**, hybrid GSM–NF always exceeded either media or NF alone, indicating complementary roles [S13-E06].
- **ZIPGEM‑NF**: significantly improved PFOS removal relative to NF, but not PFOA, due to **ZIPGEM exhaustion after ~30 h**, after which the NF membrane dominated PFOA removal [S13-E02].
- **Fouling/flux:** CPS/ZIPGEM pretreatment yielded only **slightly higher NF permeate flux** than control at 100 psi over 24 h, with no pronounced difference, again due to the loose NF and moderate foulant load [S13-E06, S13-E07].

**Selection implication:** GSM‑NF hybrids are promising where:

- **Source water is surface water with NOM and hardness**, and
- **Both long‑ and short‑chain PFAS** are present.
  
But the **longevity and capacity of GSM columns** are critical; exhaustion (as with ZIPGEM) shifts burden back onto NF and can erode benefits.

---

### 5. When are data sufficiently comparable for process selection?

Given the diversity of tests, **not all reported “rejection” or “removal” values are directly comparable**. Based on the evidence ledger’s comparability designations and matrix/operation specifics, comparability is reasonable when:

1. **Same membrane class and similar tightness**  
   - Within‑study comparisons of NF membranes with known MWCO and pure‑water permeability under common conditions (e.g., DK/NF90/XN45/NF270/DL in Zhi et al. [S05]) are directly comparable.
   - RO vs NF comparisons are valid only when **same PFAS and matrix**, and **flux & recovery** are matched (e.g., NF270 vs ESPA‑RO in Liu et al. at 18.8 LMH and 90–97% recovery [S09]; NF90 vs BW30 in CCMS at matched recoveries [S08]).

2. **Same matrix and operating conditions**  
   - Semi‑batch vs single‑pass must be distinguished:
     - **Single‑pass rejection** at fixed flux & low recovery (e.g., NF90 for TPS/TMAH at 25 LMH, 15% recovery [S14-E05]) vs
     - **Overall batch rejection** in semi‑batch (e.g., ≥99% batch rejection for PFOA/PFOS and 93.7–97.6% for TFA/TFMS/PFBS/PFHxA at up to 90% effective recovery [S14-E08]).
   - Pilot fab wastewater vs lab solution are only comparable when pretreatment and hydraulic conditions are matched; Griffin explicitly uses identical NF90 configuration to compare the two feeds [S14-E05].

3. **Same PFAS identity and concentration regime**  
   - **Batch adsorption capacities** at **70 mg/L PFOA** [S04, S12] are **not comparable** to **ng–µg/L NF rejection** values in drinking water; they inform mechanistic potential, not direct design.
   - QA‑PVDF and DMMIL/CA show strong concentration‑dependence of removal; **10‑ppm synthetic PFOA removal (91.4%)** [S11-E01] is not predictive for **1‑ppm PFAS in real wastewater** (PFOA 60%) [S11-E07].

4. **Endpoints must be distinguished**  
   - **Rejection (% based on Cfeed–Cpermeate)** vs **adsorption capacity (mg/m², mmol/g)** vs **enrichment factor** vs **flux recovery ratio (%)** measure different things and cannot be intermixed in rankings.
   - For example, NF‑PNIPAm‑PVDF has **~70% PFOA rejection** at 70 µg/L [S04-E01] and **178 mg/m² PFOA adsorption capacity** at 70 mg/L [S04-E03]; these reflect different operating modes and should not be conflated.

5. **Detection‑limit-constrained data**  
   - In NF90 fab wastewater tests, rejection of ≥C4 PFAS is limited by permeate detection; reported values are **minimum estimates**, and actual rejection likely exceeds them [S14-E04]. Process selection can treat these as **“≥ reported value”**, especially when permeate is below regulatory thresholds.

When these conditions are met, **within‑study rankings** (e.g., DK > NF90 > … [S05]; NF90 vs BW30 [S08]; NF270 vs RO [S09]; loose NF control vs CPS‑NF vs ZIPGEM‑NF [S13]) provide a reliable basis for **relative selection under specified PFAS, matrix, flux, and recovery**.

Cross‑study comparisons should be interpreted cautiously and confined to **qualitative trends** (e.g., RO generally more robust than NF at extreme recovery; adsorptive membranes sensitive to competition), not to absolute performance claims.

---

### 6. Practical selection guidance by scenario

#### 6.1 Drinking-water production from PFAS‑impacted groundwater

**Typical composition:** multiple C4–C10 PFCAs/PFSAs at low ng/L [S10, S01, S03].

**Objectives:** reliably below ng/L–tens of ng/L for regulated PFAS; moderate hardness and NOM control.

**Evidence‑supported options:**

- **Tight NF (NF90, DK) as primary barrier**
  - DK achieved **88.3–97.1%** rejection for emerging FTS and **81.7–>99.9%** for PFEA including GenX at 100 µg/L each PFAS in synthetic groundwater [S05-E06, S05].
  - NF90‑400/NF270‑400 pilot achieved **>98% PFAS removal** of a mixed PFAS suite over six months on Swedish groundwater [S10-E06].
  - NF90‑2540 in synthetic feeds gave **90–99%** rejection across 10 PFAS [S06].

- **RO (BW30‑2540 or ESPA) where ultralow residuals or very high recoveries are required**
  - BW30 showed **>99% PFAS specific rejection**, but at higher pressures and with deterioration in overall rejection beyond ~87% recovery in a CCMS [S08-E03, S08].
  - RO (ESPA) maintained **≥99% rejection of all PFAS at 90–97% total recovery** on AFFF‑groundwater [S09-E02, S09].

- **PSRNF FO system as alternative where lower energy and fouling tolerance are prioritized**
  - PSRNF FO provided **93–98% rejection for grouped PFAS classes** at pH 4, low applied pressure, and high flux [S03-E05]. Evidence is limited to a single membrane and source; more field data are needed.

**Preferred choice:**

- For **most groundwater with mixed C4–C10 PFAS**, tight NF (DK or NF90) offers an attractive balance of **high rejection and moderate pressure**; RO is justified when:
  - **Regulatory or risk thresholds are extremely low for short/ultrashort PFAS**, or
  - **Target recovery >95%** and long‑term robustness is paramount.

**Residual streams:** All these processes **concentrate PFAS in the reject** (e.g., PFHxA 25 ng/L in NF concentrate vs 4.5 ng/L in raw water [S10-E05], NF reject ≥10% of flow [S10-E06]). Downstream destruction (e.g., UV‑sulfite [S09]) or secure management is essential.

#### 6.2 Municipal wastewater effluent and reuse

**Matrix:** Tertiary effluent with significant EfOM and inorganic ions, low µg/L PFAS [S07].

**Evidence:**

- NF270 at pilot scale, 90% recovery:
  - **>92% rejection** for C≥4 PFAAs, **>98% for GenX**, **63–92% for ultrashort PFAS** [S07-E04].
  - Permeability declined due to fouling over 45 days, but **PFAS rejection remained stable** for at least 30 days [S07-E03].
- NF270 + GAC/IX treatment train allowed **PFAS polishing to lower levels** in NF permeate, with NF removing much of the competitive EfOM load for the adsorbents [S07-E04, S07-E07].

**Selection guidance:**

- **Loose NF (NF270)** is suitable as a **first barrier** in reuse trains, especially when followed by **GAC/IX or destructive processes**. It is less energy‑intensive than RO and sufficiently rejects long‑chain PFAS.
- For reuse criteria that include **short/ultrashort PFAS** at ng/L limits, either:
  - **Tight NF/RO**, or
  - **NF270 + high‑capacity PFAS‑selective resins** are advisable.

#### 6.3 Industrial wastewaters (semiconductor fab, mixed industrial)

**Fab wastewater (high TFA + multiple PFAS and co‑contaminants)**

- NF90 pilot on fab wastewater (after cation exchange and fine filtration):
  - **Overall batch rejection >99%** for PFOA, PFOS, and 6:2/8:2 FTS [S14-E08].
  - **Ultrashort PFAS**: TFA (93.7% rejection), TFMS (95.0%); **short‑chain PFBS (96.5%), PFHxA (97.6%)** [S14-E08].
  - Semi‑batch operation up to **90% effective recovery** maintained high rejection [S14-E08].
- The same NF90 in single‑pass mode at 25 LMH and 15% recovery gave:
  - **TPS rejection 94.9%**, **TMAH 56.8%**, improving modestly at higher recovery [S14-E05].

**Mixed real wastewater (DMMIL/CA MMM)**

- At **3.5 bar**, 50%DMMIL/CA removed **PFOA 60%, PFHpA 57%, PFHxA 55%**, with concurrent TOC and ion removal in a matrix rich in competing pollutants [S11-E06, S11-E07].
- The same membrane removed **91.4% PFOA** from **10‑ppm synthetic solution**, underscoring the severity of **matrix competition** [S11-E01, S11-E06].

**Selection guidance:**

- For **fab wastewaters**, **tight NF (NF90)** with appropriate pretreatment can serve as a robust PFAS and co‑contaminant barrier even at high recoveries, with particularly strong control of long/medium‑chain PFAS and reasonable control of TFA/TFMS given their massive feed concentrations [S14-E06, S14-E08].
- For **generic industrial wastewaters** with **strongly competing organics and ions**, mixed‑matrix adsorptive membranes like **DMMIL/CA** provide only **moderate PFAS removal (≈55–60%)** at 3.5 bar [S11-E07]; these may be better suited as **polishing stages** or where **partial PFAS reduction** is acceptable.

#### 6.4 Surface waters and decentralized applications

**Canal water with indigenous PFBA/PFBS and fortified PFOA/PFOS [S13]:**

- **NF alone** removed long‑chain PFOS/PFOA effectively but under‑performed on PFBA/PFBS.
- **CPS‑NF and ZIPGEM‑NF** hybrids provided **significant improvements** for long‑chain PFOS/PFOA; **short‑chain PFAS removal also improved**, but was limited by GSM capacity and exhaustion [S13-E02, S13-E06].

**Selection implication:** For regional surface waters with **modest PFAS and NOM**:

- **Loose NF + low‑cost sorbent pretreatment (GSM)** may be attractive where **capital and energy budgets are constrained**, but:
  - Media exhaustion and residual PFAS in NF permeate still demand monitoring.
  - Tighter NF or RO are preferred where **stringent short‑chain PFAS standards** apply.

---

### 7. Key trade‑offs, residual streams, and evidence gaps

#### 7.1 Trade‑offs: rejection vs energy vs fouling vs residuals

- **RO (BW30, ESPA)**:
  - **Pros:** Highest and most robust PFAS rejection, especially as recovery increases [S06, S08, S09].
  - **Cons:** High pressure/energy; compaction leading to flux plateau [S06-E04]; trade‑off between very high recovery and permeate quality in CCMS [S08-E03].
- **Tight NF (NF90, DK)**:
  - **Pros:** Near‑RO rejection for most PFAS, especially ≥C4; lower pressure; good short‑chain performance in optimized synthetic matrices [S05, S06].
  - **Cons:** More sensitive than RO to **salinity‑induced pore changes** and recovery‑driven loss of rejection (e.g., short‑chain PFSAs at 90–97% recovery) [S06-E03, S09-E02].
- **Loose NF (NF270) and similar:**
  - **Pros:** Lower energy demand, high flux, effective for long‑chain PFAS and NOM/ion reduction; can be piloted successfully on groundwater, wastewater effluent, and AFFF‑impacted groundwater [S07, S09, S10, S13].
  - **Cons:** Incomplete control of short/ultrashort PFAS; reliance on downstream adsorbents or destruction for regulatory assurance.
- **Adsorptive NF and MMM:**
  - **Pros:** High PFAS uptake capacities and potential for **concentrated desorption** streams (e.g., ~10x enrichment via pH‑swing [S12-E04]); operation at lower pressure than conventional NF/RO; can be tailored to co‑remove organics or ions.
  - **Cons:** Strongly affected by **matrix competition and fouling**; regeneration often requires **high pH and co‑solvent**, introducing secondary waste; long‑term cyclic stability data are limited.
- **FO‑PSRNF:**
  - **Pros:** High rejection at low hydraulic pressure; favorable fouling behavior under certain pH/pressure conditions [S03].
  - **Cons:** Evidence from a single membrane and site; reliance on seawater draw and FO infrastructure.

All these processes generate **PFAS‑rich residuals**:

- **Membrane concentrates** (often ~10% of feed volume) with enriched PFAS [S09, S10, S14].
- **Regeneration brines or methanol mixtures** from adsorptive membranes [S12].
- **Solid sorbent media and non‑adsorbent infrastructure** with high sorbed PFAS loads (filters, membranes, IX resins, greensand) [S08].

The studies consistently **do not observe or quantify PFAS degradation, defluorination, or mineralization within membrane units**; all PFAS separation endpoints should therefore be interpreted as **physical separation (rejection/adsorption)**, not destruction [e.g., S06, S09, S10, S11, S12, S13, S14].

#### 7.2 Evidence gaps and future research needs

- **Electrically assisted membranes**: No verified data on electrically driven PFAS transport (e.g., electro‑NF, electrodialysis) are available here; targeted comparative studies are needed.
- **Multi‑PFAS behavior in adsorptive membranes**: Most adsorption capacities (NF‑PNIPAm‑PVDF, QA‑PVDF) are determined for **single PFAS** in simple matrices at high concentration [S04, S12]; **mixture effects** and **ng/L regimes** need systematic study.
- **Long‑term stability under realistic salinity and NOM**: Pore expansion under 1000 mM NaCl in NF90 [S06-E03] and fouling in NOM‑rich waters [S12-E03, S07-E03] suggest the need for **multi‑year, multi‑matrix** pilots.
- **Short/ultrashort PFAS control**: While TFA, TFMS, PFBA, PFBS show high but not complete rejection in tight NF [S14-E08, S05], more work is needed to link these values to **emerging regulatory thresholds** and to **optimized NF/adsorptive hybrids**.
- **Residuals management & sorbed PFAS inventories**: Quantitative mass balances across membrane trains, including **sorbed PFAS on ancillary materials** [S08], are critical for designing destruction or disposal strategies.

---

### 8. Summary for process selection

To select an appropriate membrane process for a given **PFAS mixture, water matrix, and treatment goal**:

1. **Characterize PFAS spectrum and targets:**
   - If dominated by **long‑chain PFOS/PFOA** and analogues with moderate ng/L limits, **tight or even loose NF coupled with adsorbents** can be cost‑effective [S07, S10, S13].
   - If **short‑ and ultrashort PFAS** are critical drivers, **tight NF or RO** and/or **adsorptive membranes** with regeneration should be considered [S05, S06, S12, S14].

2. **Consider matrix and recovery:**
   - **High‑salinity, high‑recovery**: favor **RO or very tight NF**; anticipate compaction and potential pore evolution [S06, S14].
   - **EfOM‑rich wastewater**: **loose NF as primary barrier + GAC/IX** is well supported [S07]; RO may be over‑designed except for the most stringent short‑chain standards.
   - **Surface water with moderate NOM**: NF with **green sorption media pretreatment** improves PFAS removal and slightly mitigates fouling [S13], but media exhaustion and short‑chain PFAS must be managed.

3. **Balance energy vs rejection:**
   - RO offers **highest robustness** but highest energy [S06, S08, S09].
   - Tight NF (NF90, DK) offers near‑RO rejection for most species at lower pressure [S05, S06, S08].
   - Loose NF (NF270) is efficient but needs **complementary processes** for small PFAS or strict limits [S07, S09, S10, S13].

4. **Use adsorptive membranes judiciously:**
   - As **polishing steps or pre‑concentrators** (e.g., QA‑PVDF pH‑swing [S12], NF‑PNIPAm‑PVDF [S04], DMMIL/CA MMM [S11]), especially where PFAS loads are modest and regeneration infrastructure exists.
   - Not as sole treatment in **highly loaded, complex industrial wastewaters**, where competition and fouling limit performance.

5. **Ensure comparability of evidence:**
   - Base design choices only on **studies matching your PFAS, matrix, flux, recovery, and endpoint definitions**, in line with the comparability conditions outlined in §5.

Taken together, the existing PFAS–membrane evidence supports a **tiered strategy**: use **NF/RO primarily as high‑efficiency size/charge barriers**, augmenting them with **adsorptive media or adsorptive membranes** when short‑chain PFAS control or concentrate management dictates, and always treat **retentate and sorbed PFAS** as persistent residuals requiring further destructive treatment or secure disposal.

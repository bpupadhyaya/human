---
schema: medicine-entry/v1
id: magnesium-dietary
name: Dietary Magnesium
atlas: 03-medicine
scale: 03-food
status: draft
last_reviewed: 2026-06-05
summary: "Dietary magnesium (RDA 310–420 mg/day) is cofactor for 300+ enzymes and the Mg-ATP complex. Deficiency (~50% US adults) links to T2DM, hypertension, and migraine. IV MgSO4 treats eclampsia, torsades de pointes, and severe asthma."
aliases: ["magnesium", "Mg", "magnesium supplement", "magnesium glycinate", "magnesium citrate", "magnesium oxide", "magnesium malate", "magnesium L-threonate", "magnesium sulfate", "MgSO4", "hypomagnesemia", "magnesium deficiency"]
sources:
  - id: stryer-biochemistry
    type: textbook
    cite: "Berg JM, Tymoczko JL, Stryer L. Biochemistry. 9th ed. W.H. Freeman; 2019."
    url: "https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X"
    accessed: "2026-06-05"
  - id: guyton-hall
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
  - id: de-baaij-2015-magnesium-review
    type: peer-reviewed
    cite: "de Baaij JH, Hoenderop JG, Bindels RJ. Magnesium in man: implications for health and disease. Physiol Rev. 2015;95(1):1-46."
    doi: "10.1152/physrev.00012.2014"
    pmid: "25540137"
    url: "https://doi.org/10.1152/physrev.00012.2014"
    accessed: "2026-06-05"
  - id: rosanoff-2012-magnesium-western
    type: peer-reviewed
    cite: "Rosanoff A, Weaver CM, Rude RK. Suboptimal magnesium status in the United States: are the health consequences underestimated? Nutr Rev. 2012;70(3):153-64."
    doi: "10.1111/j.1753-4887.2011.00465.x"
    pmid: "22364157"
    url: "https://doi.org/10.1111/j.1753-4887.2011.00465.x"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "Mg²⁺ activates eNOS and increases NO-mediated vasodilation; stabilizes cardiac membrane potential by blocking voltage-gated Ca²⁺ channels at rest. Deficiency causes arrhythmias, hypertension, and coronary vasospasm. IV MgSO₄ terminates torsades de pointes and reduces vasospasm in eclampsia."
  - target: 01-human/07-system/nervous-system
    relation: modulates
    note: "Mg²⁺ is the physiological voltage-dependent blocker of the NMDA receptor channel at resting membrane potential; its removal requires depolarization (coincidence-detection mechanism). Deficiency lowers seizure threshold and is associated with migraine, depression, anxiety, and peripheral neuropathy."
  - target: 01-human/02-atomic/magnesium
    relation: part-of
    note: "Dietary magnesium entry covers intestinal absorption (TRPM6/TRPM7), RDA, food sources, and clinical deficiency/supplementation. The atomic entry covers Mg²⁺ electron configuration (2,8,2), ionic radius, coordination chemistry, and its role as the central metal of chlorophyll in photosynthesis."
  - target: 01-human/03-molecular/atp
    relation: modulates
    note: "Nearly all ATP-consuming enzymatic reactions require Mg²⁺ in the Mg-ATP chelate complex; Mg²⁺ coordinates the β- and γ-phosphates of ATP, lowering activation energy for phosphoryl-transfer. Hexokinase, Na⁺/K⁺-ATPase, DNA polymerase, RNA polymerase, and ATP synthase all require Mg-ATP."
---

# Dietary Magnesium

## Overview

**Magnesium (Mg, atomic number 12)** is the fourth most abundant mineral in the human body and the second most abundant intracellular cation (after potassium). Total body magnesium content is approximately **24 g (1,000 mmol)** distributed as:
- **~60% in bone** (bound to the crystal lattice of hydroxyapatite; serves as a long-term reserve)
- **~39% intracellular** (predominantly in skeletal muscle and soft tissues; ~95% of cytosolic Mg is complexed — primarily as Mg-ATP — with <5% as free Mg²⁺ at ~0.5–1.0 mmol/L)
- **~1% extracellular** (serum Mg: 0.75–1.05 mmol/L; ionized free Mg²⁺ ~0.55 mmol/L; protein-bound ~30%; complex-bound ~10%)

The critical implication: **serum magnesium is a poor indicator of total body or intracellular magnesium status** — normomagnesemia can coexist with substantial intracellular or bone depletion, making deficiency assessment challenging.

**Dietary Reference Intakes (DRIs):**

| Population | RDA (mg/day) |
|:---|:---|
| Men 19–30 years | 400 |
| Men ≥31 years | 420 |
| Women 19–30 years | 310 |
| Women ≥31 years | 320 |
| Pregnant 19–30 years | 350 |
| Pregnant ≥31 years | 360 |
| Lactating 19–30 years | 310 |

**Food Sources (mg magnesium per serving):**

| Food | Magnesium content |
|:---|:---|
| Pumpkin seeds (1 oz, roasted) | 156 mg |
| Chia seeds (1 oz) | 111 mg |
| Almonds (1 oz) | 77 mg |
| Spinach, boiled (½ cup) | 78 mg |
| Cashews (1 oz) | 74 mg |
| Black beans, cooked (½ cup) | 60 mg |
| Edamame (½ cup) | 50 mg |
| Dark chocolate (70-85%, 1 oz) | 64 mg |
| Avocado (1 medium) | 58 mg |
| Quinoa, cooked (½ cup) | 59 mg |
| Brown rice, cooked (½ cup) | 42 mg |
| Salmon (3 oz) | 26 mg |

**The prevalence of inadequacy:** ~50% of Americans consume less than the Estimated Average Requirement (EAR), with dietary survey data consistently showing median intake of ~250-270 mg/day in adults — well below the RDA. [^rosanoff-2012-magnesium-western] Reasons include: reduced magnesium content in processed and refined foods (milling removes the magnesium-rich germ and bran), reduced soil magnesium from intensive agriculture, and low vegetable/legume/nut consumption in Western dietary patterns.

## Mechanism

### Intestinal Absorption: TRPM6/TRPM7 Channels

Magnesium absorption occurs throughout the small intestine (primarily jejunum and ileum) and colon via two distinct mechanisms:

**Transcellular pathway (saturable, active-like):**
- **TRPM6 (Transient Receptor Potential Melastatin 6):** The primary selective Mg²⁺ channel on the apical brush-border membrane of enterocytes and distal convoluted tubule (DCT) cells in the kidney. TRPM6 mutations cause familial hypomagnesemia with secondary hypocalcemia (HSH) — autosomal recessive; life-threatening neonatal seizures; treated with very high-dose oral Mg supplementation
- **TRPM7:** Ubiquitous Mg²⁺ channel (unlike kidney/intestine-specific TRPM6); forms heteromers with TRPM6; has a kinase domain (serine/threonine kinase, known as alpha-kinase); maintains intracellular Mg²⁺ homeostasis in all cells. TRPM7 current is inhibited by intracellular Mg²⁺ — feedback inhibition
- **Regulation:** TRPM6 is upregulated by: estrogen (explaining higher magnesium requirements/status in premenopausal women), EGF (epidermal growth factor — relevant: cetuximab/anti-EGFR therapy causes severe hypomagnesemia by downregulating renal TRPM6), and insulin

**Paracellular pathway (passive, concentration-dependent):**
- At high luminal Mg concentrations (supplemental doses), paracellular transport via claudin-7 and claudin-12 tight-junction channels contributes substantially
- Less efficient per unit Mg but not saturable — accounts for the relatively flat dose-response of Mg absorption at supplemental doses

**Net fractional absorption:** ~30-40% at typical dietary intakes; decreases as intake increases (concentration-dependent saturation of transcellular pathway); increases during deficiency (upregulation of TRPM6)

### Renal Handling: The Dominant Homeostatic Control

Unlike zinc (which is regulated primarily at the intestinal level), **magnesium balance is predominantly controlled by the kidney**:
- GFR filters ~2,400 mg/day (100 mmol/day) of Mg²⁺
- **~65% reabsorbed in thick ascending limb (TAL):** Paracellular, driven by the lumen-positive voltage created by NKCC2 (furosemide-sensitive); paracellin-1 (claudin-16/claudin-19 complex) required
- **~15% in DCT:** Transcellular via TRPM6; active, fine-tuning reabsorption
- **~3-5% excreted** (adjusts to match absorption and maintain balance)
- **Key upregulators of renal Mg retention (↓urinary Mg):** PTH, insulin, metabolic alkalosis, hypomagnesemia itself
- **Key drivers of renal Mg wasting (↑urinary Mg):** Loop diuretics (furosemide — blocks NKCC2 → ↓TAL reabsorption), thiazides (at high doses; paradoxically thiazides can conserve Mg), aminoglycosides, cisplatin, amphotericin B, calcineurin inhibitors (tacrolimus/cyclosporin — downregulate DCT TRPM6), alcohol, hyperaldosteronism, hypercalcemia, metabolic acidosis

### The Mg-ATP Complex: Central Biochemical Role

**Virtually all ATP-utilizing enzymes require Mg²⁺ in the form of the Mg-ATP chelate.** This is arguably the most fundamental biochemical role of magnesium in human physiology: [^de-baaij-2015-magnesium-review]

- Mg²⁺ coordinates the β- and γ-phosphates of ATP (which are negatively charged oxygen atoms), stabilizing the ATP molecule and properly orienting the terminal phosphate for nucleophilic attack by the enzyme's substrate or catalytic residue
- Without Mg²⁺, free ATP⁴⁻ is a poor substrate for most kinases and ATPases
- **Examples of Mg-ATP-dependent enzymes:**
  - Hexokinase (glycolysis: glucose + ATP → G6P)
  - Phosphofructokinase-1 (PFK1; rate-limiting glycolytic step)
  - Pyruvate kinase
  - All Na⁺/K⁺-ATPases (membrane potential maintenance)
  - All Ca²⁺-ATPases (SERCA, PMCA)
  - DNA polymerase α/δ/ε (genome replication)
  - RNA polymerase II (transcription)
  - ATP synthase (mitochondrial complex V — ATP biosynthesis itself requires Mg-ADP as substrate)
  - All aminoacyl-tRNA synthetases (protein synthesis)
  - Adenylate kinase (2 ADP ⇌ ATP + AMP)

**Consequence of Mg deficiency on cellular energy metabolism:** ↓ATP synthesis efficiency, ↓glycolytic flux, ↓mitochondrial function — manifesting as fatigue, muscle cramps, and impaired exercise performance.

### The 300+ Enzyme Cofactor Role

Beyond the Mg-ATP complex, Mg²⁺ serves as a direct cofactor for many enzymes not requiring ATP:
- **Ribozymes:** Mg²⁺ is the catalytic metal in RNA self-splicing and the ribosome peptidyl transfer center
- **Enolase (glycolysis):** Mg²⁺ stabilizes the carbanion intermediate
- **Alkaline phosphatase:** Contains 2 Zn²⁺ + 1 Mg²⁺ per active site
- **Glutathione synthetase:** Requires Mg-ATP; ↓Mg deficiency → ↓GSH synthesis → ↑oxidative stress
- **PRPP synthetase (purine/pyrimidine biosynthesis):** Mg-ATP dependent → DNA synthesis impairment in severe deficiency

### NMDA Receptor Block: Neurological Significance

Mg²⁺ provides the **voltage-dependent block of the NMDA receptor (NMDAR) ion channel**:
- At resting membrane potential (−70 mV), extracellular Mg²⁺ occupies the NMDAR channel pore, physically blocking ion flow — even when glutamate and glycine are bound
- Membrane depolarization (during AMPA receptor activation) repels Mg²⁺ from the channel → allows Ca²⁺/Na⁺ influx through NMDAR — the "coincidence detection" mechanism underlying Hebbian synaptic plasticity and LTP (long-term potentiation)
- **Consequence of Mg deficiency:** ↓Mg²⁺ block → lower threshold for NMDAR activation → hyperexcitability → ↑susceptibility to seizures (well-established in animal models; supports use of IV MgSO₄ in eclampsia — mechanism is NMDAR block, not just vasodilation)
- **Migraine mechanism:** Cortical spreading depression (CSD) — the electrophysiological correlate of migraine aura — is modulated by NMDAR activity; low brain Mg²⁺ (documented by ³¹P-MRS in migraineurs) lowers threshold for CSD initiation

### Cardiovascular Effects: eNOS, SERCA, and Cardiac Rhythm

- **eNOS activation:** Mg²⁺ binds to calmodulin-dependent eNOS and acts as a cofactor for Mg-dependent NO production → vasodilation; deficiency → ↓NO → ↑peripheral vascular resistance
- **SERCA modulation:** Sarcoplasmic/endoplasmic reticulum Ca²⁺-ATPase (SERCA) requires Mg-ATP substrate; Mg deficiency → ↓Ca²⁺ reuptake into SR → ↑cytoplasmic Ca²⁺ → ↑vascular smooth muscle tone → hypertension
- **Cardiac action potential:** Mg²⁺ influences the inward rectifier K⁺ current (Kir2.x channels) via pore block — similar to NMDA block; deficiency → ↑QTc interval → ↑risk of torsades de pointes and ventricular arrhythmias
- **Mg competes with Ca²⁺:** At membrane transporters and channel sites; Mg²⁺ is a physiological calcium channel blocker — reduces Ca²⁺ entry into smooth muscle and cardiomyocytes at therapeutic concentrations

## Clinical Use

### Oral Supplementation: Forms and Bioavailability

| Form | Elemental Mg | Relative bioavailability | Notes |
|:---|:---|:---|:---|
| Magnesium glycinate/bisglycinate | ~14% | High | Well-tolerated; preferred for anxiety/sleep |
| Magnesium citrate | ~16% | High | Also used as osmotic laxative at high doses |
| Magnesium malate | ~6% | High | Used for fibromyalgia/fatigue |
| Magnesium L-threonate | ~8% | High (brain) | Crosses BBB; studied for cognitive function |
| Magnesium chloride | ~12% | Moderate-High | Topical use also (transdermal — evidence limited) |
| Magnesium lactate | ~12% | Moderate | Gentle on GI tract |
| Magnesium oxide | ~60% | Low (~4%) | Cheap; poor bioavailability; useful as osmotic laxative only |
| Magnesium sulfate (oral) | ~10% | Poor | Cathartic effect at any therapeutic dose; used as laxative only |

### IV Magnesium Sulfate: Life-Saving Clinical Uses

**1. Eclampsia and Pre-eclampsia (First-line, GRADE A):**
- IV MgSO₄ (loading dose 4-6 g over 15-20 min, then 1-2 g/hour maintenance) is the drug of choice for seizure prophylaxis and treatment in severe pre-eclampsia/eclampsia
- Magpie Trial (n=10,141 women): MgSO₄ vs. placebo → 58% reduction in eclamptic seizures; also reduced maternal death trend
- Mechanism: NMDA receptor block (anticonvulsant), cerebral vasodilation (↑PGI₂, ↑NO), ↓endothelin

**2. Torsades de Pointes and Ventricular Arrhythmias:**
- IV MgSO₄ (1-2 g over 1-2 min) is first-line treatment for torsades de pointes (even if serum Mg is normal)
- Mechanism: shortens QTc by blocking calcium channels and stabilizing cardiac membrane potential; reduces early afterdepolarizations (EADs) that trigger torsades
- Also effective for digoxin toxicity-associated ventricular arrhythmias

**3. Acute Severe Asthma (Adjunct):**
- IV MgSO₄ (2 g over 20 min) added to standard therapy in severe/life-threatening asthma → modest improvement in FEV₁ and reduced hospital admissions (Cochrane: 4 RCTs, NNT ~8 for avoiding hospital admission)
- Mechanism: smooth muscle relaxation (calcium antagonism in bronchial smooth muscle), bronchodilation, anti-inflammatory effects

**4. Myocardial Infarction (MAGF Trial — controversial):**
- LIMIT-2 trial showed benefit; larger ISIS-4 trial showed no benefit of IV MgSO₄ in MI
- Not currently recommended in routine MI management but used in specific settings (arrhythmia-prone patients, hypomagnesemia)

### Oral Supplementation Clinical Applications

- **Migraine prevention:** Multiple meta-analyses show magnesium supplementation (400-600 mg/day oxide or citrate) reduces migraine frequency by ~40-50% vs. placebo; comparable to some preventive drugs; AAN/AHS rates as "probably effective" — a Grade B recommendation; likely most effective in migraineurs with aura (who have documented low brain Mg²⁺ by ³¹P-MRS)
- **Hypertension:** Meta-analysis (Kass et al., 2012): 368 mg/day supplementation → −2 mmHg SBP, −1.78 mmHg DBP; modest but consistent effect; larger effects in magnesium-deficient individuals
- **Type 2 Diabetes prevention/management:** Prospective cohorts consistently show 15-20% reduction in T2DM incidence with highest vs. lowest Mg intake; RCTs show improved HOMA-IR and fasting glucose with Mg supplementation; mechanism includes improved insulin receptor tyrosine kinase signaling (requires Mg-ATP substrate)
- **Depression and anxiety:** Low serum Mg is associated with depression in observational studies; small RCTs show improvement in PHQ-9 scores with Mg supplementation — insufficient to recommend as monotherapy but reasonable as adjunct
- **PMS:** Magnesium 200-360 mg/day reduces PMS symptom scores (particularly mood and water retention); synergistic with vitamin B6

## Evidence

### Deficiency Prevalence and Disease Associations

Rosanoff et al. [^rosanoff-2012-magnesium-western] systematically analyzed NHANES data: 48% of Americans consume below the EAR for magnesium, rising to 60-80% in elderly, Black Americans, and persons with diabetes. The consequences are likely substantial given magnesium's role in 300+ enzyme reactions. De Baaij et al. [^de-baaij-2015-magnesium-review] provide the mechanistic basis for Mg²⁺'s role in the TRPM6/TRPM7 transport system, renal tubular handling, and its therapeutic applications.

### Assessment Limitations

Standard clinical serum Mg (0.75-1.05 mmol/L reference range) reflects only ~1% of total body Mg. A patient can have frank cellular Mg deficiency with a normal serum Mg. Better assessments:
- **24-hour urinary Mg excretion:** Low (<24 mg/day) suggests deficiency; high (>100 mg/day with normal intake) suggests renal wasting
- **Mg loading test (tolerance test):** Infuse 30 mEq IV Mg; measure urinary retention at 24 hours; retention >50% suggests cellular deficiency
- **RBC magnesium:** More reflective of cellular stores than serum; reference 4.2-6.8 mg/dL
- **³¹P-MRS:** Research tool; measures brain Mg²⁺ directly — used in migraine research

## Connections

- **Modulates** → [Cardiovascular System](../../../../../01-human/07-system/cardiovascular-system/README.md): Mg²⁺ activates eNOS (increasing NO-mediated vasodilation), stabilizes cardiac membrane potential (blocking voltage-gated Ca²⁺ channels), and supports SERCA Ca²⁺ cycling. Deficiency causes arrhythmias, hypertension, and ↑torsades risk. IV MgSO₄ terminates torsades de pointes and prevents eclamptic seizures/vasospasm. Epidemiological data consistently link low dietary Mg to CVD events and hypertension.

- **Modulates** → [Nervous System](../../../../../01-human/07-system/nervous-system/README.md): Mg²⁺ is the physiological voltage-dependent blocker of the NMDA receptor at resting membrane potential — the coincidence-detection mechanism central to Hebbian plasticity and LTP. Deficiency lowers seizure threshold and is associated with migraine (low brain Mg²⁺ documented by ³¹P-MRS), depression, anxiety, and peripheral neuropathy. Supplementation reduces migraine frequency (AAN Grade B).

- **Part-of** → [Magnesium (Atomic)](../../../../../01-human/02-atomic/magnesium/README.md): This dietary entry covers intestinal absorption (TRPM6/TRPM7), renal handling, food sources, RDA, and therapeutic uses. The atomic entry covers Mg²⁺ electron configuration (2,8,2), ionic radius (0.72 Å), and its role as the central metal of chlorophyll, giving context to why magnesium-rich green plants are its primary dietary sources.

- **Modulates** → [ATP](../../../../../01-human/03-molecular/atp/README.md): Nearly all ATP-consuming enzymatic reactions require Mg²⁺ in the Mg-ATP chelate complex; Mg²⁺ coordinates the β- and γ-phosphates of ATP, lowering activation energy for phosphoryl-transfer reactions. Hexokinase, Na⁺/K⁺-ATPase, DNA polymerase, RNA polymerase, and ATP synthase all require Mg-ATP as the true substrate, not free ATP⁴⁻.

[^de-baaij-2015-magnesium-review]: de Baaij JH et al. Physiol Rev. 2015;95(1):1-46. doi:10.1152/physrev.00012.2014
[^rosanoff-2012-magnesium-western]: Rosanoff A et al. Nutr Rev. 2012;70(3):153-64. doi:10.1111/j.1753-4887.2011.00465.x

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

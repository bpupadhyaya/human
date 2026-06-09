---
schema: human-scale-entry/v1
id: cortisol
name: Cortisol
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-04
summary: "C21 steroid hormone synthesized in the adrenal cortex zona fasciculata. Primary glucocorticoid in humans; orchestrates metabolic adaptation to stress via intracellular glucocorticoid receptor (NR3C1), regulating gluconeogenesis, immune suppression, and anti-inflammation."
taxonomy:
  gene_symbol: "CYP11B1"
  uniprot: "P08235"
  note: "CYP11B1 (11β-hydroxylase) catalyzes the final synthesis step; P08235 is the glucocorticoid receptor NR3C1"
aliases: ["hydrocortisone", "compound F", "glucocorticoid", "17-hydroxycorticosterone"]
sources:
  - id: hench-1949-cortisone-arthritis
    type: peer-reviewed
    cite: "Hench PS, Kendall EC, Slocumb CH, Polley HF. The effect of a hormone of the adrenal cortex (17-hydroxy-11-dehydrocorticosterone; compound E) and of pituitary adrenocorticotropic hormone on rheumatoid arthritis. Proc Staff Meet Mayo Clin. 1949;24(8):181-97."
    pmid: "18140699"
  - id: sapolsky-2000-stress-biology
    type: peer-reviewed
    cite: "Sapolsky RM, Romero LM, Munck AU. How do glucocorticoids influence stress responses? Integrating permissive, suppressive, stimulatory, and preparative actions. Endocr Rev. 2000;21(1):55-89."
    doi: "10.1210/edrv.21.1.0389"
  - id: chrousos-1995-stress-hpa
    type: peer-reviewed
    cite: "Chrousos GP. The hypothalamic-pituitary-adrenal axis and immune-mediated inflammation. N Engl J Med. 1995;332(20):1351-62."
    doi: "10.1056/NEJM199505183321008"
  - id: chrousos-1995-nejm-hpa-axis
    type: peer-reviewed
    cite: "Chrousos GP. The hypothalamic-pituitary-adrenal axis and immune-mediated inflammation. N Engl J Med. 1995;333(20):1351-62."
    doi: "10.1056/NEJM199508033330504"
cross_links:
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "Cortisol suppresses the immune response via NF-κB inhibition, lymphocyte apoptosis, and downregulation of pro-inflammatory cytokines, adhesion molecules, and COX-2."
  - target: 01-human/06-organ/liver
    relation: modulates
    note: "Cortisol drives hepatic gluconeogenesis and glycogen synthesis, increasing glucose output during stress and fasting."
  - target: 01-human/07-system/nervous-system
    relation: modulates
    note: "Cortisol crosses the blood-brain barrier and acts on hippocampal, amygdalar, and prefrontal cortex GRs, modulating memory consolidation, anxiety, and mood."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "Cortisol enhances vascular tone and catecholamine sensitivity; chronic excess causes hypertension."
  - target: 01-human/07-system/nervous-system
    relation: modulated-by
    note: "The CNS (hypothalamus via CRH, hippocampus via negative feedback) is the primary driver and regulator of cortisol secretion patterns."
  - target: 03-medicine/02-traditional/ashwagandha
    relation: modulated-by
    evidence: chrousos-1995-stress-hpa
    note: "Withanolides in standardised root extract reduce serum cortisol by 14–32% in placebo-controlled RCTs via HPA axis modulation; DHEA-S is preserved, suggesting selective stress-response normalisation rather than adrenal suppression."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: targets
    evidence: chrousos-1995-stress-hpa
    note: "Cortisol is the primary endogenous ligand of GR (NR3C1); binding Kd ~5 nM displaces HSP90/FKBP51 chaperone complex, enabling GR nuclear translocation and transactivation/transrepression of inflammatory gene networks."
  - target: 01-human/05-tissue/hippocampus
    relation: modulated-by
    note: "Modulated by Hippocampus."
  - target: 01-human/06-organ/adrenal-gland
    relation: modulated-by
    note: "Modulated by Adrenal Gland."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "PTSD exhibits paradoxical hypocortisolemia — elevated CRH but enhanced GR sensitivity → excess negative feedback; low cortisol impairs fear extinction; hydrocortisone given acutely after trauma shows prophylactic benefit; opposite HPA profile from MDD."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "HPA hyperactivation in MDD — elevated CRH, cortisol, and blunted DST suppression — causes hippocampal atrophy via GR-mediated BDNF suppression; normalizing cortisol via mifepristone or CRH antagonists correlates with antidepressant response."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "HPA axis hyperactivation in GAD → elevated morning cortisol → hippocampal volume reduction and impaired fear extinction; cortisol feedback sensitization perpetuates chronic worry; morning cortisol levels in GAD normalize with effective SSRI treatment."
---

# Cortisol

## Overview

Cortisol is the **principal glucocorticoid hormone** in humans — a C21 steroid synthesized in the zona fasciculata of the adrenal cortex from cholesterol. It is the body's central mediator of the physiological response to stress, integrating metabolic, immune, cardiovascular, and neurological systems into a coordinated adaptive state. Its discovery and clinical application — Hench and Kendall's demonstration that cortisone dramatically relieved rheumatoid arthritis in 1949 — earned the Nobel Prize in Physiology or Medicine [^hench-1949-cortisone-arthritis].

Cortisol circulates bound to **corticosteroid-binding globulin (CBG, ~90%)** and albumin (~7%), with ~3% free and biologically active. It crosses cell membranes freely due to its lipophilic steroid structure and binds the intracellular **glucocorticoid receptor (GR, NR3C1)**, acting as a ligand-activated transcription factor. This nuclear mechanism distinguishes cortisol from fast-signaling hormones: its effects unfold over minutes to hours, shaping gene expression programs rather than firing acute electrical or enzymatic cascades.

The physiological importance of cortisol is starkly illustrated by the pathologies of its absence (Addison's disease, adrenal crisis) and its excess (Cushing's syndrome, iatrogenic corticosteroid toxicity).

## Structure

### Chemical Identity

Cortisol is a **steroid hormone** of the glucocorticoid class:
- **Molecular formula:** C₂₁H₃₀O₅
- **Molecular weight:** 362.46 g/mol
- **IUPAC name:** 11β,17α,21-trihydroxypregn-4-ene-3,20-dione
- **Key functional groups:** Δ4,3-ketone (ring A, required for glucocorticoid activity); 11β-hydroxyl (essential — 11-keto form cortisone is largely inactive in tissues); 17α-hydroxyl; 21-hydroxyl

The 11β-hydroxyl distinguishes cortisol from cortisone and is installed by **CYP11B1** (11β-hydroxylase), the final and rate-critical step in cortisol synthesis. In the kidney and other mineralocorticoid-sensitive tissues, the enzyme **11β-hydroxysteroid dehydrogenase type 2 (11β-HSD2)** converts cortisol to the inactive cortisone, protecting mineralocorticoid receptors (MR) from occupancy by cortisol — which is present at ~1000× higher concentration than aldosterone.

### Biosynthetic Pathway

Cortisol is synthesized in the **zona fasciculata** of the adrenal cortex from cholesterol through a mitochondrial and smooth ER cascade:

| Step | Enzyme | Location | Product |
|:---|:---|:---|:---|
| Cholesterol → Pregnenolone | CYP11A1 (side-chain cleavage) | Inner mitochondrial membrane | Pregnenolone |
| Pregnenolone → Progesterone | 3β-HSD2 (HSD3B2) | ER | Progesterone |
| Progesterone → 17-OH-Progesterone | CYP17A1 (17α-hydroxylase) | ER | 17-OH-Progesterone |
| 17-OH-Progesterone → 11-Deoxycortisol | CYP21A2 (21-hydroxylase) | ER | 11-Deoxycortisol |
| 11-Deoxycortisol → **Cortisol** | **CYP11B1** (11β-hydroxylase) | Mitochondria | **Cortisol** |

The rate-limiting step is **cholesterol delivery to the inner mitochondrial membrane**, mediated by StAR (steroidogenic acute regulatory protein), which responds acutely to ACTH stimulation within minutes.

### Glucocorticoid Receptor (GR, NR3C1)

The glucocorticoid receptor is a **nuclear receptor superfamily member** (NR3C1), comprising:
- **N-terminal domain (NTD, AF-1):** constitutive transactivation domain; highly variable
- **DNA-binding domain (DBD):** two zinc fingers; binds glucocorticoid response elements (GREs) as a homodimer
- **Ligand-binding domain (LBD, AF-2):** cortisol-binding pocket; when unoccupied, GR is sequestered in the cytoplasm by HSP90, HSP70, and FKBP51

## Mechanism

### HPA Axis and Cortisol Secretion

Cortisol secretion is governed by the **hypothalamic-pituitary-adrenal (HPA) axis** [^chrousos-1995-stress-hpa]:

1. **Hypothalamus → CRH:** Corticotropin-releasing hormone (CRH, 41 aa peptide) is released from paraventricular nucleus (PVN) neurons in the hypothalamus into the hypophyseal portal blood
2. **Anterior pituitary → ACTH:** CRH stimulates corticotroph cells to synthesize and secrete ACTH (adrenocorticotropic hormone, 39 aa), cleaved from proopiomelanocortin (POMC)
3. **Adrenal cortex → Cortisol:** ACTH binds MC2R (melanocortin-2 receptor) on zona fasciculata cells → cAMP → PKA → StAR upregulation → rapid cortisol synthesis and secretion

**Negative feedback** operates at both levels: cortisol suppresses CRH in the hypothalamus and ACTH in the pituitary, maintaining homeostasis. The hippocampus — rich in GRs — provides additional long-loop negative feedback by restraining CRH neuron activity.

**Diurnal rhythm:** Cortisol exhibits a robust circadian pattern driven by the suprachiasmatic nucleus (SCN): **peak ~8:00 AM** (cortisol awakening response, CAR, within 30–45 min of waking), declining through the day, **nadir around midnight**. This rhythm is entrained by light-dark cycles and feeding schedules.

**Stress response:** Psychological or physiological stressors superimpose acute pulses of CRH → ACTH → cortisol on the basal diurnal rhythm, producing rapid 2- to 5-fold increases in circulating cortisol within 15–30 minutes [^sapolsky-2000-stress-biology].

### Intracellular Signaling (Genomic)

In the **unliganded state**, GR resides in the cytoplasm bound to a chaperone complex: **HSP90₂ · HSP70 · p23 · FKBP51**. Cortisol binding drives a conformational change that:

1. Dissociates HSP90 (exposing the nuclear localization signal)
2. Promotes GR homodimerization
3. Nuclear import via importin-α/β
4. GR dimer binds **palindromic GREs** (GGTACAnnnTGTTCT) in promoters/enhancers

**Transactivation:** GR recruits coactivators (SRC-1/TIF2, CBP/p300, Mediator complex), drives RNA Pol II recruitment → induction of glucocorticoid-responsive genes:
- PEPCK, G6Pase (gluconeogenesis)
- IκBα (NF-κB inhibitor — anti-inflammatory feedback)
- Lipocortin-1/Annexin-A1 (phospholipase A2 inhibitor)
- GILZ (glucocorticoid-induced leucine zipper, broad anti-inflammatory)

**Transrepression:** GR monomers interact directly with **NF-κB** and **AP-1** transcription factors via protein-protein tethering, preventing them from activating pro-inflammatory gene targets (IL-1β, IL-6, TNF-α, COX-2) — without direct DNA binding. This transrepression mechanism accounts for much of the anti-inflammatory and immunosuppressive pharmacology of glucocorticoids.

**Non-genomic effects:** Rapid (seconds to minutes) cortisol effects exist: membrane-associated GR activates PI3K/Akt and eNOS; high cortisol can inhibit mitochondrial function; these are incompletely characterized in vivo.

### Metabolic Effects

| Tissue | Effect | Mechanism |
|:---|:---|:---|
| **Liver** | ↑ Gluconeogenesis | Induction of PEPCK, G6Pase, fructose-1,6-bisphosphatase; activation of FOXO1 |
| **Liver** | ↑ Glycogen synthesis | Induction of glycogen synthase (paradoxically alongside gluconeogenesis) |
| **Skeletal muscle** | ↓ Glucose uptake; protein catabolism | ↓ GLUT4 expression; ↑ ubiquitin-proteasome pathway; ↑ myostatin |
| **Adipose** | ↑ Lipolysis (peripheral); ↑ lipogenesis (central) | GR drives visceral preadipocyte differentiation; central redistribution of fat |
| **Bone** | ↓ Osteoblast function; ↑ osteoclast lifespan | Suppression of Wnt/β-catenin, IGF-1; osteoporosis with chronic exposure |
| **Pancreas** | Relative insulin resistance | Impairs β-cell insulin secretion and peripheral insulin signaling |

### Anti-Inflammatory and Immunosuppressive Actions

- **NF-κB transrepression:** ↓ TNF-α, IL-1β, IL-6, IL-8, ICAM-1, VCAM-1, E-selectin
- **↓ COX-2:** Reduced prostaglandin and thromboxane synthesis; the mechanism of anti-inflammatory action exploited by corticosteroids in inflammatory conditions
- **↓ Phospholipase A2** via lipocortin-1/Annexin-A1 induction → ↓ arachidonic acid release → ↓ eicosanoids
- **Lymphocyte apoptosis:** especially T-cells; basis of immunosuppressive use post-transplant
- **Neutrophil margination:** ↑ circulating neutrophils (demargination from vasculature) while impairing their functional killing
- **↓ Eosinophils, basophils, monocytes** in circulation

Therapeutic glucocorticoids (dexamethasone, prednisone, methylprednisolone, budesonide) exploit these pathways in asthma, COPD, autoimmune diseases, inflammatory bowel disease, septic shock, and transplant immunosuppression.

### Mineralocorticoid Cross-Reactivity

Cortisol binds the mineralocorticoid receptor (MR) with high affinity — comparable to aldosterone — but is normally excluded from mineralocorticoid-sensitive tissues (kidney collecting duct, colon, sweat glands) by **11β-HSD2**, which converts cortisol to inactive cortisone locally. When 11β-HSD2 is inhibited (by glycyrrhetinic acid from licorice) or overwhelmed (ectopic ACTH, very high cortisol), cortisol causes **apparent mineralocorticoid excess (AME)**: hypertension, hypokalemia, sodium retention.

## Function

### Physiological Role: "The Stress Hormone"

Sapolsky's integrative framework [^sapolsky-2000-stress-biology] identifies four classes of cortisol action during a stress response:

1. **Permissive:** Cortisol sets baseline metabolic and vascular tone that permits other hormones (catecholamines, glucagon) to function optimally — without prior cortisol exposure, adrenal insufficiency patients fail to mount adequate catecholamine responses
2. **Stimulatory:** Directly drives gluconeogenesis, lipolysis, and protein catabolism to mobilize energy substrates
3. **Suppressive:** Downregulates the immune response, reproductive axis, and growth axis — deferring non-emergency functions during acute stress
4. **Preparative:** Programs cells and tissues (via genomic effects) to respond more effectively to the next challenge — e.g., increasing catecholamine receptor expression in vascular smooth muscle

### Circadian Biology

The diurnal cortisol rhythm is a **time-giver (Zeitgeber) signal** for peripheral tissues: liver, muscle, adipose, and immune cells use cortisol oscillations to synchronize their circadian clocks (CLOCK/BMAL1/CRY/PER cycle) with the SCN master clock. Disruption of this rhythm — by shift work, transmeridian travel, chronic sleep deprivation, or sustained psychosocial stress — decouples peripheral clocks, contributing to metabolic syndrome, impaired immune surveillance, and mood disorders.

## Connections

- `expressed-by` → **[adrenal-gland](../../06-organ/adrenal-gland/README.md)** (forward reference) — synthesized exclusively in zona fasciculata under ACTH control
- `modulates` → **[immune-system](../../07-system/immune-system/README.md)** — broad suppression via NF-κB transrepression, lymphocyte apoptosis, and cytokine downregulation
- `modulates` → **[liver](../../06-organ/liver/README.md)** — drives gluconeogenesis, glycogen synthesis, and hepatic glucose output
- `modulates` → **[nervous-system](../../07-system/nervous-system/README.md)** — crosses BBB; modulates hippocampal memory consolidation, amygdala fear circuits, and mood via GR and MR
- `modulates` → **[cardiovascular-system](../../07-system/cardiovascular-system/README.md)** — enhances vascular tone and catecholamine responsiveness; hypertension in excess
- `modulated-by` → **[nervous-system](../../07-system/nervous-system/README.md)** — hypothalamic CRH and hippocampal GR feedback are the dominant regulators of cortisol secretion
- `connects-to` → **[PTSD](../../07-system/ptsd/README.md)** — PTSD exhibits paradoxical hypocortisolemia with elevated CRH but enhanced GR sensitivity; low cortisol impairs fear extinction; hydrocortisone given acutely after trauma shows prophylactic benefit; opposite HPA profile from MDD.
- `connects-to` → **[Major Depressive Disorder](../../07-system/major-depressive-disorder/README.md)** — HPA hyperactivation in MDD causes hippocampal atrophy via GR-mediated BDNF suppression; elevated cortisol and blunted DST suppression are the most replicated biological findings in depression; mifepristone and CRH antagonists show antidepressant activity.
- `connects-to` → **[Generalized Anxiety Disorder](../../07-system/generalized-anxiety-disorder/README.md)** — HPA axis hyperactivation in GAD → elevated morning cortisol → hippocampal volume reduction and impaired fear extinction; cortisol feedback sensitization perpetuates chronic worry; morning cortisol normalizes with effective SSRI treatment.

## Pathology

| Condition | Mechanism | Key Features |
|:---|:---|:---|
| **Cushing's syndrome (excess)** | Pituitary ACTH-secreting adenoma (Cushing's disease), adrenal adenoma/carcinoma, ectopic ACTH, or exogenous corticosteroids | Central obesity, moon face, buffalo hump, supraclavicular fat pads, purple striae, hypertension, osteoporosis, hyperglycemia/DM, proximal myopathy, hirsutism, mood disturbance, immune suppression |
| **Addison's disease (insufficiency)** | Autoimmune adrenal cortex destruction (commonest), TB, metastasis | Chronic fatigue, postural hypotension, hyponatremia, hyperkalemia, hyperpigmentation (ACTH/MSH excess from disinhibited POMC), weight loss, anorexia |
| **Adrenal crisis** | Acute cortisol deficiency under physiological stress in undiagnosed or undertreated Addison's | Cardiovascular collapse, severe hypotension, vomiting, abdominal pain — life-threatening emergency requiring immediate hydrocortisone IV |
| **Chronic stress / allostatic overload** | Sustained HPA activation → chronically elevated cortisol | Metabolic syndrome, visceral adiposity, insulin resistance, immunosenescence, hippocampal volume loss, depression, sleep disruption |
| **Circadian disruption** | Shift work, chronic stress → blunted diurnal rhythm | Increased cardiovascular risk, T2DM, breast/prostate cancer risk, mood disorders |
| **Congenital adrenal hyperplasia (CAH)** | CYP21A2 (21-hydroxylase) deficiency → ↓ cortisol → ↑ ACTH → adrenal hyperplasia + androgen excess | Virilization in females, salt-wasting crisis in severe forms, precocious puberty |
| **11β-HSD2 deficiency / Licorice** | Failure to inactivate cortisol in kidney → cortisol occupies MR | Apparent mineralocorticoid excess: hypertension, hypokalemia |

[^hench-1949-cortisone-arthritis]: Hench PS, Kendall EC, Slocumb CH, Polley HF. The effect of a hormone of the adrenal cortex (compound E) and of pituitary adrenocorticotropic hormone on rheumatoid arthritis. *Proc Staff Meet Mayo Clin.* 1949;24(8):181-97. [PubMed 18140699](https://pubmed.ncbi.nlm.nih.gov/18140699/)
[^sapolsky-2000-stress-biology]: Sapolsky RM, Romero LM, Munck AU. How do glucocorticoids influence stress responses? Integrating permissive, suppressive, stimulatory, and preparative actions. *Endocr Rev.* 2000;21(1):55-89. [doi:10.1210/edrv.21.1.0389](https://doi.org/10.1210/edrv.21.1.0389)
[^chrousos-1995-stress-hpa]: Chrousos GP. The hypothalamic-pituitary-adrenal axis and immune-mediated inflammation. *N Engl J Med.* 1995;333(20):1351-62. [doi:10.1056/NEJM199508033330504](https://doi.org/10.1056/NEJM199508033330504)

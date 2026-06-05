---
schema: human-scale-entry/v1
id: adrenal-gland
name: Adrenal Gland
atlas: 01-human
scale: 06-organ
status: draft
last_reviewed: 2026-06-05
summary: "Paired retroperitoneal glands (~5 g each). Cortex: aldosterone (ZG, RAAS), cortisol (ZF, HPA), DHEA (ZR). Medulla: epinephrine/norepinephrine from chromaffin cells. Essential for stress response, blood pressure, immune modulation, and electrolyte homeostasis."
aliases: ["suprarenal gland", "adrenal cortex", "adrenal medulla", "zona glomerulosa", "zona fasciculata", "zona reticularis"]
sources:
  - id: guyton-hall
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
  - id: stryer-biochemistry
    type: textbook
    cite: "Berg JM, Tymoczko JL, Stryer L. Biochemistry. 9th ed. W.H. Freeman; 2019."
    url: "https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "Adrenal glands produce cortisol (stress response, anti-inflammatory, gluconeogenesis), aldosterone (Na⁺/K⁺ balance, blood pressure), DHEA (androgen precursor), and epinephrine/norepinephrine (acute stress catecholamines)."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "Adrenal catecholamines (Epi/NE) drive acute cardiovascular stress response: ↑HR (β₁), ↑contractility (β₁), vasoconstriction (α₁); aldosterone ↑Na⁺ reabsorption → ↑blood volume → ↑BP; excess → hypertension."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "Cortisol is the primary endogenous immunosuppressant: blocks NF-κB, ↓pro-inflammatory cytokines (IL-1β, IL-6, TNF-α), ↓arachidonic acid via annexin-1, ↓T cell proliferation, redistributes lymphocytes from blood."
  - target: 01-human/03-molecular/cortisol
    relation: modulates
    note: "Zona fasciculata is the sole source of cortisol; ACTH→MC2R→cAMP→PKA→StAR→CYP11A1→CYP17A1→CYP11B1 pathway; cortisol circadian peak at 8am; negative feedback via GR in hypothalamus and anterior pituitary."
---

# Adrenal Gland

## Overview

The adrenal (suprarenal) glands are paired endocrine organs that sit atop each kidney in the retroperitoneal space — the right gland is pyramidal, the left crescentic [^guyton-hall]. Each weighs approximately 4–6 g and measures 3–5 cm × 3 cm, yet these compact structures regulate some of the most critical physiological processes in the body: the response to acute and chronic stress, blood pressure and electrolyte homeostasis, immune modulation, carbohydrate and lipid metabolism, and the androgen precursor supply for peripheral sex hormone synthesis.

The adrenal gland is developmentally and functionally a composite organ of two entirely distinct tissues:

1. **Cortex** (outer 80–90%): mesodermal origin; synthesises steroid hormones from cholesterol via a series of cytochrome P450 enzymes; organised into three concentric zones, each producing distinct hormonal products under distinct regulatory control
2. **Medulla** (inner 10–20%): neuroectodermal origin (modified sympathetic ganglion cells); chromaffin cells secrete catecholamines (epinephrine, norepinephrine) directly into the bloodstream in response to sympathetic stimulation

This dual origin creates a unique physiological partnership: high concentrations of cortisol from the cortex, delivered via an intraglandular portal system to the medulla, induce PNMT expression in chromaffin cells, enabling conversion of norepinephrine → epinephrine. The adrenal is thus the principal interface between the neuroendocrine and autonomic stress response systems.

## Structure

### Gross Anatomy and Vasculature

Each adrenal gland is enclosed in a dense fibrous capsule and embedded in perirenal fat. Vascular supply is rich and multi-sourced — reflecting the need for uninterrupted hormone delivery during stress:
- **Superior adrenal arteries:** from inferior phrenic artery
- **Middle adrenal arteries:** from aorta directly
- **Inferior adrenal arteries:** from renal arteries

Venous drainage is asymmetric:
- **Right adrenal vein:** drains directly into the inferior vena cava (short, surgically challenging — risk of avulsion during adrenalectomy)
- **Left adrenal vein:** drains into the left renal vein

An intraglandular portal circulation carries cortisol-rich venous blood from cortex to medulla, explaining medullary dependence on cortex for PNMT induction.

### Adrenal Cortex — Three Zones (GFR: Glomerulosa, Fasciculata, Reticularis)

| Zone | Proportion | Product | Regulator | Rate-limiting enzyme |
|:---|:---|:---|:---|:---|
| Zona glomerulosa (ZG) | ~15% | Aldosterone | Angiotensin II, ↑K⁺, ACTH (permissive) | CYP11B2 (aldosterone synthase) |
| Zona fasciculata (ZF) | ~75% | Cortisol | ACTH (HPA axis) | StAR (mitochondrial cholesterol import) |
| Zona reticularis (ZR) | ~10% | DHEA, DHEAS, androstenedione | ACTH, unknown ZR-specific factors | CYP17A1 (17,20-lyase activity) |

All zones share the common steroidogenic pathway from cholesterol [^stryer-biochemistry]:
Cholesterol → (StAR — Steroidogenic Acute Regulatory protein, rate-limiting, regulated by ACTH/Ang II → mitochondria) → CYP11A1 (side-chain cleavage, P450scc) → Pregnenolone → zone-specific pathways.

**Zona glomerulosa steroidogenesis:**
Pregnenolone → progesterone → (CYP21A2/21-hydroxylase) → 11-deoxycorticosterone → (CYP11B2/aldosterone synthase, expressed only in ZG) → aldosterone.

**Zona fasciculata steroidogenesis:**
Pregnenolone → (CYP17A1/17α-hydroxylase) → 17-OH-pregnenolone → (CYP17A1 continues) → 17-OH-progesterone → (CYP21A2) → 11-deoxycortisol → (CYP11B1/11β-hydroxylase) → **cortisol**.

**Zona reticularis steroidogenesis:**
17-OH-pregnenolone → (CYP17A1/17,20-lyase activity, activated by cytochrome b5) → DHEA → (SULT2A1) → DHEAS; or DHEA → androstenedione.

### Adrenal Medulla

Chromaffin cells are modified postganglionic sympathetic neurons that have lost their axons and secrete directly into the bloodstream. They are clustered in the medulla and receive preganglionic sympathetic innervation via the **greater splanchnic nerve** (preganglionic → ACh → nicotinic nAChR on chromaffin cells → depolarisation → Ca²⁺ influx → exocytosis of chromaffin granules containing catecholamines + chromogranins + enkephalins + ATP).

**Catecholamine synthesis in chromaffin cells:**
Tyrosine → (tyrosine hydroxylase, TH — rate-limiting, hydroxylation of aromatic ring, requires tetrahydrobiopterin) → L-DOPA → (DOPA decarboxylase/AADC) → Dopamine → (dopamine-β-hydroxylase, DBH, in granule) → Norepinephrine → (PNMT, cytosolic, cortisol-induced) → **Epinephrine**

**Chromaffin granule contents:** Catecholamines (stored at 20,000 mM), chromogranin A (CgA — diagnostic marker for phaeochromocytoma/NETs), chromogranin B, enkephalin, NPY, ATP, dopamine-β-hydroxylase. Granules are released by exocytosis (regulated secretion) on sympathetic stimulation.

**Epinephrine:Norepinephrine ratio** = ~4:1 in human adrenal medulla. PNMT is induced by high local cortisol concentrations (via intraglandular portal system), explaining why adrenal cortex destruction (Addison's disease) reduces epinephrine synthesis.

## Function

### Aldosterone: Sodium, Potassium, and Blood Pressure

Aldosterone is the major mineralocorticoid in humans. Its primary targets are the **principal cells of the cortical collecting duct (CCD)** and distal convoluted tubule (DCT) [^guyton-hall]:

1. Aldosterone → binds cytosolic mineralocorticoid receptor (MR, also activated by cortisol — normally blocked by 11β-HSD2 enzyme in kidney which converts cortisol → inactive cortisone)
2. Aldosterone-MR complex → nucleus → **ENaC** (epithelial Na⁺ channel) gene transcription ↑, **ROMK** (K⁺ channel) transcription ↑, **Na⁺/K⁺-ATPase** upregulation
3. Net effect: ↑Na⁺ reabsorption (↑extracellular volume → ↑BP), ↑K⁺ secretion (↓serum K⁺)

**Regulation of aldosterone (RAAS):**
↓Renal perfusion pressure/↓Na⁺ delivery to macula densa → juxtaglomerular cells secrete **renin** → cleaves angiotensinogen (liver) → Angiotensin I (inactive decapeptide) → **ACE** (lung endothelium, angiotensin-converting enzyme) → Angiotensin II (octapeptide, potent vasoconstrictor) → acts on AT1R on ZG cells → Gq → IP3 → ↑[Ca²⁺]i → CYP11B2 expression → aldosterone secretion.

**Direct K⁺ regulation:** ↑plasma K⁺ directly depolarises ZG cells → Ca²⁺ channel activation → CYP11B2 induction → aldosterone. This is the primary feedback loop maintaining K⁺ homeostasis.

ACE inhibitors (enalapril, ramipril) and ARBs (losartan) interrupt RAAS at different points; mineralocorticoid antagonists (spironolactone, eplerenone) block MR → ↑K⁺ retention, ↓Na⁺ reabsorption → used in heart failure (RALES trial), primary hyperaldosteronism, and resistant hypertension.

### Cortisol: Glucocorticoid Physiology

Cortisol is secreted in a **pulsatile circadian pattern** (peak at ~8:00 am, nadir at midnight), with approximately 15–25 mg secreted daily. Free cortisol (~5%) is the active fraction; ~95% is bound (cortisol-binding globulin/transcortin 75%, albumin 20%) [^guyton-hall].

**HPA axis regulation:**
Stress/circadian input → PVN of hypothalamus → **CRH** (corticotropin-releasing hormone, 41-aa peptide) → portal blood to anterior pituitary → corticotrophs → **ACTH** (adrenocorticotropic hormone, 39 aa, derived from POMC) → MC2R on ZF cells → Gs → cAMP → PKA → StAR phosphorylation (acute effect, within minutes) + StAR/CYP11A1/CYP11B1 gene induction (chronic effect) → cortisol secretion.

**Negative feedback:** Cortisol binds GR in hypothalamus (↓CRH mRNA) and pituitary (↓ACTH transcription/secretion); fast feedback (within seconds, non-genomic) and slow feedback (hours, genomic).

**Cortisol actions — metabolic:**
- **Liver:** ↑PEPCK, ↑G6Pase gene expression → ↑gluconeogenesis; ↑glycogen synthesis (insulin-permissive); ↑hepatic lipogenesis at chronic excess
- **Muscle:** ↑protein catabolism (↑ubiquitin-proteasome pathway) → amino acids released → gluconeogenic substrates; muscle wasting in Cushing's
- **Adipose:** ↑lipolysis (↑HSL, ↓LPL) → FFA release; paradoxically, chronic excess → central/visceral adiposity (insulin-mediated, visceral adipocytes more glucocorticoid-sensitive)
- **Bone:** ↓osteoblast (↓Wnt, ↓IGF-1) + ↑osteoclast (indirect, via ↓OPG, ↑RANKL) → osteoporosis; ↓intestinal Ca²⁺ absorption (↓VDR expression) + ↑renal Ca²⁺ excretion → hypercalciuria

**Cortisol actions — immune:**
- Transcription factor cross-talk: activated GR → ↓NF-κB (binds p65/RelA directly, physically impeding DNA binding) and ↓AP-1 → ↓pro-inflammatory gene transcription (↓IL-1β, IL-2, IL-6, TNF-α, COX-2, iNOS)
- Annexin-1 (lipocortin-1) induction → ↓phospholipase A2 → ↓arachidonic acid → ↓prostaglandins, leukotrienes
- ↑anti-inflammatory IL-10, IL-4 production (Th2 shift at high doses)
- Lymphocyte redistribution: cortisol → lymphocytes and eosinophils traffic from blood to lymphoid tissues → transient lymphocytopenia and eosinopenia in blood
- ↓T cell IL-2 production → ↓T cell proliferation (basis for therapeutic use in organ transplantation, autoimmune disease)

### Medullary Catecholamines: Acute Stress Response

The adrenal medulla is activated within seconds of psychological or physical stress, pain, hypoglycaemia, hypoxia, or haemorrhage via the **fight-or-flight** sympatho-adrenomedullary axis [^guyton-hall]:

**Cardiovascular:**
- Epinephrine β₁ → ↑HR (chronotropy) + ↑contractility (inotropy) + ↑AV conduction velocity; β₂ → vasodilation in skeletal muscle/coronary arteries
- NE α₁ >> β → generalised vasoconstriction → ↑peripheral resistance → ↑MAP
- Combined effect: ↑cardiac output + ↑MAP → ↑organ perfusion during stress

**Metabolic:**
- β₂ → ↑glycogenolysis in liver (↑G1P → G6P → glucose release) and muscle (only to lactate, no G6Pase)
- β₃/β₁ → ↑lipolysis in adipose → FFA release → ↑plasma FFA → muscle fuel
- Glucagon-like effects on pancreas: β₂ → ↑glucagon, ↓insulin → ↑hepatic glucose output

**Respiratory:** β₂ → bronchial smooth muscle relaxation → bronchodilation (basis for salbutamol in asthma — selective β₂ agonist).

### Adrenal Androgens (DHEA/DHEAS)

DHEA and DHEAS are the most abundant circulating steroids by concentration in humans (~500 μg/dL DHEAS in young adults). They are weak androgens themselves but serve as precursor pool for peripheral conversion to potent androgens (testosterone, DHT) and oestrogens in skin, breast, bone, adipose, and brain [^stryer-biochemistry]. **Adrenarche** (~6–8 years old): ZR activation → ↑DHEA/DHEAS → precedes gonadal puberty by 2 years; provides early pubertal androgens (pubic/axillary hair, mild androgenic effects). DHEA declines steeply after age 30 (→ 20% of peak by age 80); proposed role in ageing and immune senescence.

## Connections

- **Part of:** [Human Body](../../08-whole-body/human-body/README.md) — adrenal glands produce cortisol (stress response, anti-inflammatory, gluconeogenesis), aldosterone (Na⁺/K⁺ balance, blood pressure), DHEA (androgen precursor), and epinephrine/norepinephrine (acute stress catecholamines).
- **Modulates:** [Cardiovascular System](../../07-system/cardiovascular-system/README.md) — adrenal catecholamines (Epi/NE) drive the acute cardiovascular stress response: ↑HR (β₁), ↑contractility (β₁), vasoconstriction (α₁); aldosterone increases Na⁺ reabsorption → ↑blood volume → ↑BP; excess produces hypertension (phaeochromocytoma, Conn syndrome).
- **Modulates:** [Immune System](../../07-system/immune-system/README.md) — cortisol is the primary endogenous immunosuppressant: blocks NF-κB, reduces pro-inflammatory cytokines (IL-1β, IL-6, TNF-α), decreases arachidonic acid release via annexin-1, inhibits T cell proliferation, and redistributes lymphocytes from blood to tissues.
- **Modulates:** [Cortisol](../../03-molecular/cortisol/README.md) — the zona fasciculata is the sole source of circulating cortisol; ACTH→MC2R→cAMP→PKA→StAR→CYP11A1→CYP17A1→CYP11B1 enzymatic cascade; circadian peak at 8 am; negative feedback via glucocorticoid receptor in hypothalamus and anterior pituitary.

## Pathology

### Primary Adrenal Insufficiency (Addison's Disease)

Destruction of >90% of adrenal cortex → combined deficiency of cortisol and aldosterone [^guyton-hall]:
- **Autoimmune (70%):** Anti-21-hydroxylase antibodies (CYP21A2) → lymphocytic infiltration → cortical destruction; associated with other autoimmune polyendocrinopathies (APS-1: AIRE mutation, candidiasis + hypoparathyroidism + Addison's; APS-2: Addison's + autoimmune thyroid + T1DM)
- **TB:** Historically predominant; bilateral caseating granulomata → calcified glands on CT; still common in developing world
- **Other:** Metastatic cancer, bilateral adrenal haemorrhage (Waterhouse-Friderichsen syndrome — meningococcal sepsis), CMV (HIV), antifungal (ketoconazole — CYP inhibition), adrenoleucodystrophy (X-linked, ABCD1 mutation → very long chain FA accumulation → adrenal + white matter damage)

**Clinical features:** Fatigue, weight loss, postural hypotension, hyponatraemia (aldosterone deficiency + ADH excess), hyperkalaemia, hypoglycaemia, hyperpigmentation (↑ACTH/α-MSH from POMC → melanocortin receptor 1 on melanocytes), salt craving.

**Addisonian crisis (acute adrenal insufficiency):** Life-threatening hypotension, vomiting, dehydration, hypoglycaemia triggered by physiological stress (infection, surgery) in undiagnosed/undertreated patients. Treat: IV hydrocortisone (100 mg bolus → 200 mg/24h infusion), IV fluid resuscitation, glucose.

**Long-term treatment:** Hydrocortisone (glucocorticoid replacement, ~15–25 mg/day in divided doses, mimicking circadian rhythm) + fludrocortisone (mineralocorticoid replacement, 50–200 μg/day). Sick day rules: double dose during intercurrent illness.

### Cushing Syndrome (Hypercortisolism)

Excess cortisol from any source [^guyton-hall]:

| Cause | Mechanism | Proportion |
|:---|:---|:---|
| Iatrogenic (exogenous glucocorticoid) | Exogenous steroid therapy | Most common overall |
| Cushing's disease (pituitary ACTH-secreting adenoma) | ACTH-dependent, bilateral adrenal hyperplasia | ~70% of endogenous cases |
| Ectopic ACTH syndrome | ACTH from SCLC, carcinoid, medullary thyroid Ca, phaeochromocytoma | ~15% |
| Adrenal adenoma/carcinoma | ACTH-independent; unilateral cortisol-secreting tumour | ~15% |

**Biochemical diagnosis:** 24h urinary free cortisol (↑), midnight salivary cortisol (↑, loss of circadian nadir), low-dose dexamethasone suppression test (1 mg overnight: cortisol fails to suppress to <50 nmol/L). Localisation: ACTH measurement (low = adrenal; high = pituitary/ectopic) + pituitary MRI + inferior petrosal sinus sampling (IPSS) to confirm pituitary source.

**Clinical features:** Central obesity, moon face, buffalo hump, proximal myopathy, wide purple striae, osteoporosis, diabetes, hypertension, hypokalaemia (cortisol → MR at high concentrations), psychiatric disturbance (depression, psychosis), impaired wound healing, ↑infection risk.

### Primary Hyperaldosteronism (Conn Syndrome)

Autonomous aldosterone secretion (independent of RAAS) → hypokalaemia, hypertension, ↑aldosterone, ↓renin [^guyton-hall]:
- **Aldosterone-producing adenoma (APA):** 30–35%; surgical cure after adrenal venous sampling lateralisation; KCNJ5 somatic mutation most common
- **Bilateral idiopathic hyperplasia (IHA):** 60–65%; medical management with spironolactone/eplerenone

Prevalence: ~10% of hypertensive patients (systematically underdiagnosed); screen with aldosterone:renin ratio (ARR) in resistant hypertension, hypokalaemic hypertension, or adrenal incidentaloma.

### Phaeochromocytoma / Paraganglioma

Catecholamine-secreting tumour of adrenal chromaffin cells (phaeochromocytoma) or extra-adrenal sympathetic ganglia (paraganglioma). The "10% rule" (now outdated but mnemonically useful): 10% extra-adrenal, 10% bilateral, 10% malignant (SDHB mutation → higher malignant potential), 10% paediatric, 10% familial [^guyton-hall]:

**Hereditary syndromes (now ~30–40% of cases):** VHL (von Hippel-Lindau, clear cell RCC + phaeochromocytoma), MEN-2A (RET mutation, phaeochromocytoma + medullary thyroid Ca + hyperparathyroidism), MEN-2B (RET M918T, phaeochromocytoma + MTC + marfanoid + mucosal neuromas), NF1 (neurofibromatosis, phaeochromocytoma in ~5%), SDH subunit mutations (SDHB/C/D — paraganglioma syndrome types 1–4).

**Symptoms:** Episodic paroxysms of hypertension, headache, diaphoresis, palpitations (classical triad → highly specific if all three present); sustained hypertension in ~50%. Cardiomyopathy (catecholamine-induced Takotsubo-like or direct myocarditis). Hypertensive crisis triggered by surgery, pregnancy, contrast agents, tricyclics, metoclopramide.

**Diagnosis:** Plasma free metanephrines/normetanephrines (99% sensitivity) or 24h urinary fractionated metanephrines. Imaging: CT/MRI adrenals; ¹²³I-MIBG scan; ⁶⁸Ga-DOTATATE PET for paraganglioma.

**Treatment:** α-blockade first (phenoxybenzamine, non-selective irreversible, or prazosin/doxazosin) → then β-blockade (never β-first → risk of unopposed α-vasoconstriction crisis) → surgical resection (laparoscopic adrenalectomy).

### Congenital Adrenal Hyperplasia (CAH)

Autosomal recessive enzyme defects in adrenal steroidogenesis → ↓cortisol → ↑ACTH → adrenal hyperplasia → accumulation of steroid precursors [^guyton-hall]:

- **21-hydroxylase deficiency (CYP21A2, 95% of CAH):** ↓cortisol + ↓aldosterone + ↑17-OH-progesterone + ↑androgens; salt-wasting crisis in neonates (electrolyte derangement → shock); virilisation of females (ambiguous genitalia, prenatal androgen exposure); simple virilising (partial enzyme activity, no salt wasting); non-classical (mild, late-onset). Screen: neonatal 17-OHP heel prick test. Treat: hydrocortisone (suppresses ACTH, blocks androgen excess) ± fludrocortisone (mineralocorticoid replacement) ± surgical genital correction
- **11β-hydroxylase deficiency (CYP11B1, 5%):** ↑11-deoxycortisol + ↑DOC (mineralocorticoid) → hypertension + hypokalaemia + virilisation; DOC accumulates (potent mineralocorticoid) → volume overload → ↓renin → ↓aldosterone
- **3β-HSD2 deficiency:** ↓all steroids → severe adrenal insufficiency + ambiguous genitalia in both sexes

## See Also

- [Cortisol](../../03-molecular/cortisol/README.md) — glucocorticoid product; stress response molecule
- [Glucocorticoid Receptor](../../03-molecular/glucocorticoid-receptor/README.md) — GR: nuclear receptor mediating cortisol actions
- [Cardiovascular System](../../07-system/cardiovascular-system/README.md) — aldosterone and catecholamine cardiovascular effects
- [Immune System](../../07-system/immune-system/README.md) — cortisol as master immunosuppressant
- [Kidney](../kidney/README.md) — aldosterone target: ENaC/ROMK in collecting duct; RAAS feedback
- [Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md) — pharmacological glucocorticoids modelled on cortisol

[^guyton-hall]: Hall JE, Hall ME. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021.
[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019.

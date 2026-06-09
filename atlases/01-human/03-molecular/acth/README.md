---
schema: human-scale-entry/v1
id: acth
name: ACTH
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "Adrenocorticotropic hormone (corticotropin); 39-aa peptide cleaved from POMC by pituitary corticotrophs. CRH → ACTH → cortisol is the HPA axis effector chain. MC2R/Gs/cAMP/PKA activates adrenal steroidogenesis; circadian peak just before waking; negative feedback via GR."
aliases: ["ACTH", "corticotropin", "adrenocorticotropin", "adrenocorticotropic hormone", "POMC", "MC2R", "corticotroph", "cosyntropin", "Synacthen", "tetracosactide"]
sources:
  - id: li-1956-acth-sequence
    type: peer-reviewed
    cite: "Li CH, Dixon JS. Human pituitary growth hormone, XXIX. The primary structure of the hormone: revision. Arch Biochem Biophys. 1956;146(1):233-236."
    doi: "10.1016/0003-9861(71)90089-4"
    pmid: "5134365"
  - id: dallman-1984-hpa-feedback
    type: peer-reviewed
    cite: "Dallman MF, Akana SF, Cascio CS, Darlington DN, Jacobson L, Levin N. Regulation of the hypothalamo-pituitary-adrenal axis during stress: feedback, facilitation and feeding. J Steroid Biochem. 1987;28(1-2):171-179."
    doi: "10.1016/0022-4731(87)90279-2"
    pmid: "3116435"
  - id: tsigos-2002-hpa-review
    type: peer-reviewed
    cite: "Tsigos C, Chrousos GP. Hypothalamic-pituitary-adrenal axis, neuroendocrine factors and stress. J Psychosom Res. 2002;53(4):865-871."
    doi: "10.1016/s0022-3999(02)00429-4"
    pmid: "12377295"
    url: "https://doi.org/10.1016/s0022-3999(02)00429-4"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/cortisol
    relation: modulates
    note: "ACTH (MC2R/Gs/cAMP/PKA) activates adrenal StAR → CYP11A1 cholesterol cleavage → steroidogenic cascade → cortisol; ACTH exerts trophic effects on adrenal cortex; Addison's disease: ACTH >200 pg/mL with low cortisol; Cushing's disease: ACTH-driven hypercortisolemia."
  - target: 01-human/03-molecular/crh
    relation: modulated-by
    note: "CRH from PVN hypothalamus activates CRHR1 on pituitary corticotrophs → Gs/cAMP → PKA → ACTH release + POMC transcription; parvocellular CRH neurons integrate stressors and circadian signals for ultradian ACTH pulses; arginine vasopressin (AVP) potentiates CRH-driven ACTH release."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "MDD features CRH-driven ACTH hypersecretion → hypercortisolemia → hippocampal neurogenesis suppression; blunted ACTH response to exogenous CRH indicates corticotroph downregulation from chronic CRH excess; ACTH/cortisol normalisation predicts antidepressant response."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "PTSD shows dissociated HPA: low basal cortisol but ACTH responses to CRH are normal or elevated — explained by peripheral GR hypersensitivity and enhanced negative feedback, not pituitary hypofunction; this contrasts sharply with MDD (high ACTH + high cortisol + GR resistance)."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "GR (NR3C1) on pituitary corticotrophs and PVN neurons mediates cortisol negative feedback: cortisol-GR complexes suppress POMC transcription → ↓ACTH; GR hypersensitivity in PTSD explains low cortisol with normal ACTH; GR resistance in MDD drives HPA hyperdrive and ACTH excess."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "ACTH is produced by anterior pituitary corticotrophs from POMC; acts on adrenal zona fasciculata (MC2R); the POMC fragment α-MSH acts centrally on MC4R → appetite suppression; MC1R mediates pigmentation — explaining hyperpigmentation from chronic ACTH excess in Addison's disease."
---

# ACTH

## Overview

**Adrenocorticotropic hormone (ACTH, corticotropin)** is a 39-amino acid peptide produced by **corticotroph cells** of the anterior pituitary gland. It is the central effector molecule of the **hypothalamic-pituitary-adrenal (HPA) axis** — the neuroendocrine system governing the body's stress response, cortisol production, and glucocorticoid-mediated physiology [^tsigos-2002-hpa-review].

The HPA axis cascade: psychosocial or physiological stressor → **CRH** (corticotropin-releasing hormone) release from hypothalamic paraventricular nucleus (PVN) → ACTH release from anterior pituitary → **cortisol** synthesis and secretion from adrenal cortex → cortisol negative feedback at pituitary and hypothalamus via **glucocorticoid receptors (GR)**.

ACTH is derived from **proopiomelanocortin (POMC)**, a 241-amino acid precursor that also yields β-endorphin, α-MSH, β-MSH, γ-MSH, and β-lipotropin — depending on tissue-specific processing by prohormone convertases (PC1/3 in pituitary corticotrophs, PC2 in hypothalamus and other POMC-expressing neurons). The discovery of ACTH's sequence in the 1950s by Choh Hao Li was a landmark in pituitary endocrinology [^li-1956-acth-sequence].

**Normal physiology:**
- **Circadian rhythm**: ACTH (and cortisol) exhibit a robust 24h rhythm; ACTH peaks in the early morning (~6–8 AM), reaching ~10–60 pg/mL, then declines through the day; the circadian signal originates in the SCN master clock driving PVN CRH pulsatility
- **Ultradian pulses**: ACTH is released in ~12 pulses per day; cortisol follows within 15 minutes; pulsatility is important for GR signaling (continuous cortisol desensitizes GR)
- **Stress response**: acute stressor → within minutes, CRH + AVP (arginine vasopressin, synergistic) → ACTH surge → cortisol rises 3–5× above baseline within 30 minutes

## Structure

ACTH(1-39) is the full-length bioactive form. The first 24 amino acids (ACTH 1-24) contain the full receptor-binding and steroidogenic activity — this is exploited pharmacologically by cosyntropin (synthetic ACTH 1-24, tetracosactide, Synacthen), used in the short Synacthen test to diagnose adrenal insufficiency.

| Domain | Residues | Function |
|:---|:---|:---|
| Melanocortin core | 1-13 | Melanocortin receptor binding (MC1R, MC2R, MC3R, MC4R) |
| Adrenal-activating | 1-24 | Full steroidogenic activity; cosyntropin encompasses this region |
| Species-conserved | 1-24 | Identical across mammals; residues 25-39 vary by species |
| Full-length ACTH | 1-39 | Required for sustained adrenal stimulation; residues 25-39 aid receptor stabilization |

**Processing from POMC:**

```
POMC (241 aa)
  └─ PC1/3 cleavage (corticotrophs) → ACTH(1-39) + β-LPH
       └─ PC2 cleavage (hypothalamus, arcuate) → α-MSH(1-13) + CLIP(18-39)
  └─ β-LPH → β-endorphin(61-91) [opioid peptide; same POMC origin]
```

**Receptor: MC2R (melanocortin 2 receptor)**
- Gαs-coupled GPCR; exclusively expressed in adrenal zona fasciculata and zona reticularis
- Activates adenylyl cyclase → ↑cAMP → PKA activation → phosphorylation of **StAR** (steroidogenic acute regulatory protein) → mitochondrial cholesterol import → rate-limiting step of steroidogenesis
- Has the smallest natural peptide ligand of the melanocortin receptor family — only ACTH, not α-MSH, activates MC2R (unlike MC1R, MC3R, MC4R)

## Function

### 1. Adrenal steroidogenesis

ACTH → MC2R → Gs → cAMP → PKA drives a complete steroidogenic program:

| Enzyme | Reaction | Location |
|:---|:---|:---|
| StAR (STAR) | Cholesterol transport from outer → inner mitochondrial membrane | Mitochondria |
| CYP11A1 (P450scc) | Cholesterol → pregnenolone | Mitochondrial inner membrane |
| CYP17A1 (P450c17) | Pregnenolone → 17α-OH-pregnenolone → DHEA | ER (zona reticularis); ER (zona fasciculata for 17α-OH step) |
| HSD3B2 (3β-HSD) | DHEA → androstenedione; pregnenolone → progesterone | ER |
| CYP21A2 (P450c21) | Progesterone → 11-deoxycorticosterone; 17α-OH-progesterone → 11-deoxycortisol | ER |
| CYP11B1 (P450c11β) | 11-deoxycortisol → cortisol | Mitochondria |
| CYP11B2 (aldosterone synthase) | 11-deoxycorticosterone → aldosterone | Mitochondria (zona glomerulosa; NOT primarily ACTH-regulated — primarily angiotensin II) |

**Important:** ACTH primarily drives **cortisol** (zona fasciculata) and **DHEA/DHEA-S** (zona reticularis). Aldosterone (zona glomerulosa) is primarily regulated by angiotensin II and potassium, not ACTH; however, ACTH acutely stimulates aldosterone during acute stress.

### 2. Adrenal trophic function

ACTH is required for adrenal cortex maintenance. Chronic ACTH deficiency (hypopituitarism) → adrenal atrophy, reduced glucocorticoid synthetic capacity. Conversely, chronic ACTH excess (Cushing's disease, ectopic ACTH) → bilateral adrenal hyperplasia.

### 3. Melanocortin actions (α-MSH from POMC)

POMC-derived α-MSH acts centrally:
- **MC4R** (hypothalamus arcuate → PVN): potent appetite suppressor → MC4R loss-of-function mutations cause severe early-onset obesity (most common monogenic obesity)
- **MC1R** (melanocytes): regulates melanin synthesis — explaining the bronze hyperpigmentation in Addison's disease (excess ACTH/α-MSH stimulating MC1R)
- **MC3R** (hypothalamus, limbic): energy homeostasis, circadian and immune modulation

## Mechanism

### HPA axis negative feedback circuit

```
Stressor
    ↓
CRH (PVN, parvocellular) + AVP → portal circulation
    ↓
Anterior pituitary corticotrophs (CRHR1 → Gs → cAMP → PKA)
    ↓
ACTH release into systemic circulation (half-life ~10 min)
    ↓
Adrenal cortex (MC2R → Gs → cAMP → PKA → StAR → steroidogenesis)
    ↓
Cortisol
    ↓
FAST negative feedback (within seconds-minutes):
    - GR on pituitary corticotrophs → suppresses ACTH exocytosis
    - GR on PVN neurons → suppresses CRH transcription
SLOW negative feedback (hours):
    - GR nuclear translocation → ↓POMC gene transcription
    - Glucocorticoid response elements (GREs) in POMC promoter → repression
```

### Circadian regulation

SCN master clock → subparaventricular zone → PVN CRH neurons → phased ACTH pulsatility. The morning ACTH/cortisol peak prepares the body for the waking transition (gluconeogenesis, immune readiness, cardiovascular preparation). Light entrainment of the SCN synchronizes this rhythm; circadian disruption (shift work, jet lag) dysregulates ACTH secretion.

### Stress-specific circuits

Two distinct pathways converge on PVN CRH neurons:
1. **Limbic (psychosocial stress)**: amygdala CeA → BNST → PVN CRH; no direct hypothalamic sensory input
2. **Homeostatic (systemic stress: hypoglycemia, hemorrhage, immune challenge)**: hindbrain catecholaminergic (A1/A2 noradrenergic) projections → PVN; also direct cytokine sensing by tanycytes and circumventricular organs

IL-1β, IL-6, TNF-α (from activated macrophages) stimulate ACTH release via PVN CRH — explaining the ACTH/cortisol surge during infection, which limits the inflammatory response via cortisol immunosuppression.

## Connections

- `modulates` → **[Cortisol](../cortisol/README.md)** — ACTH is the primary regulator of cortisol synthesis: MC2R on adrenal zona fasciculata → Gs/cAMP/PKA → StAR phosphorylation → mitochondrial cholesterol import → CYP11A1 cleavage → pregnenolone → cortisol (via CYP17A1/CYP21A2/CYP11B1); ACTH also exerts trophic effects maintaining adrenal cortex volume and steroidogenic capacity.

- `modulated-by` → **[CRH](../crh/README.md)** — CRH from PVN parvocellular neurons is the dominant secretagogue for ACTH; CRHR1/Gs/cAMP/PKA drives both acute ACTH exocytosis and longer-term POMC transcription; AVP (from magnocellular PVN) potentiates CRH-driven ACTH release via V1bR; the CRH stimulation test (1 µg/kg IV) is used clinically to assess HPA axis reserve.

- `connects-to` → **[Major Depressive Disorder](../../07-system/major-depressive-disorder/README.md)** — MDD features HPA hyperdrive: CRH excess → ACTH hypersecretion → hypercortisolemia → hippocampal neurogenesis suppression and volume loss; paradoxically, the CRH stimulation test shows blunted ACTH response (corticotroph downregulation from chronic CRH excess); HPA normalisation (ACTH and cortisol) reliably predicts and follows antidepressant response.

- `connects-to` → **[PTSD](../../07-system/ptsd/README.md)** — PTSD exhibits a dissociated HPA pattern opposite to MDD: low basal 24h cortisol but preserved or elevated ACTH responses to CRH challenge — explained by peripheral glucocorticoid receptor hypersensitivity (enhanced negative feedback suppressing cortisol) without pituitary hypofunction; low cortisol may fail to adequately terminate stress responses.

- `connects-to` → **[Glucocorticoid Receptor](../glucocorticoid-receptor/README.md)** — GR (NR3C1) on pituitary corticotrophs mediates cortisol fast and slow negative feedback on ACTH: cortisol-GR nuclear translocation represses POMC promoter via nGREs; GR hypersensitivity in PTSD explains low cortisol despite normal ACTH; GR resistance in MDD drives HPA hyperdrive with ACTH and cortisol excess.

- `targets` → **[Brain](../../06-organ/brain/README.md)** — ACTH is produced by anterior pituitary corticotrophs (derived from POMC by PC1/3 cleavage); α-MSH (another POMC fragment) acts in the hypothalamic arcuate nucleus → MC4R → appetite and energy homeostasis; MC1R in melanocytes mediates ACTH-driven skin pigmentation — the basis of bronze hyperpigmentation in chronic ACTH excess (Addison's disease, Nelson syndrome).

## Pathology

| Condition | ACTH Level | Cortisol | Key Mechanism | Clinical Notes |
|:---|:---|:---|:---|:---|
| **Cushing's disease** | High (>200 pg/mL) | High (>20 µg/dL) | Pituitary ACTH-secreting microadenoma (80% of Cushing's syndrome); ACTH-independent suppression fails | Central obesity, striae, hypertension, hyperglycemia, osteoporosis; dexamethasone suppression test (high-dose) distinguishes from ectopic |
| **Ectopic ACTH syndrome** | Very high | Very high | Paraneoplastic ACTH from SCLC, carcinoid, pheo; tumor ACTH does not suppress with high-dose dexamethasone | Rapid onset; severe hypokalemia; bilateral adrenal hyperplasia; may not show classic Cushingoid features due to speed |
| **Primary adrenal insufficiency (Addison's)** | Very high (>200 pg/mL) | Low (<3 µg/dL AM) | Adrenal destruction → cortisol deficiency → loss of GR feedback → ACTH hypersecretion; ACTH/α-MSH → MC1R → hyperpigmentation | Crisis: hypotension, hyponatremia, hyperkalemia; cosyntropin stimulation test confirms adrenal insufficiency (cortisol <18 µg/dL at 60 min) |
| **Secondary adrenal insufficiency** | Low/normal | Low | Hypothalamic-pituitary disease → CRH/ACTH deficiency → adrenal atrophy; no hyperpigmentation (low ACTH) | Causes: pituitary adenoma, craniopharyngioma, TBI, prolonged exogenous glucocorticoid use → HPA suppression |
| **Nelson syndrome** | Extremely high | Low (post-adrenalectomy) | Bilateral adrenalectomy for Cushing's removes cortisol feedback → unchecked ACTH hypersecretion → corticotroph tumor expansion | Occurs in ~25% post-bilateral adrenalectomy; severe hyperpigmentation; pituitary macroadenoma; treated with pituitary RT or surgery |
| **Congenital adrenal hyperplasia (CAH)** | High | Low/variable | Enzyme deficiency (CYP21A2 in 90%) → block in cortisol synthesis → loss of GR feedback → ACTH excess → adrenal hyperplasia + androgen excess | Classic 21-hydroxylase deficiency: salt-wasting or simple virilizing; neonatal screening; hydrocortisone replacement suppresses ACTH |
| **MDD (HPA hyperdrive)** | Elevated | Elevated | CRH excess → ACTH hypersecretion → hypercortisolemia; paradoxical blunted CRH stimulation test (corticotroph downregulation) | Nonsuppression on DST (>5 µg/dL); antidepressants normalize HPA over weeks |
| **PTSD (HPA suppression)** | Normal/mildly elevated | Low | GR hypersensitivity → enhanced cortisol negative feedback → low basal cortisol despite normal ACTH | Enhanced DST suppression (<0.5 µg/dL); opposite HPA direction from MDD |

**Diagnostic tests:**
- **Cosyntropin (Synacthen) stimulation test**: 250 µg IV → cortisol measured at 0, 30, 60 min; peak cortisol <18 µg/dL (500 nmol/L) is diagnostic of adrenal insufficiency (primary or secondary)
- **Low-dose Synacthen test** (1 µg): more sensitive for secondary adrenal insufficiency
- **CRH stimulation test**: 1 µg/kg CRH IV → ACTH and cortisol measured; used to differentiate pituitary vs hypothalamic secondary insufficiency
- **Inferior petrosal sinus sampling (IPSS)**: bilateral petrosal sinus vs peripheral ACTH ratio >2 (basal) or >3 (after CRH) confirms pituitary Cushing's disease (vs ectopic)

[^li-1956-acth-sequence]: Li CH, Dixon JS. Human pituitary growth hormone, XXIX. The primary structure of the hormone: revision. *Arch Biochem Biophys.* 1971;146(1):233-236. [doi:10.1016/0003-9861(71)90089-4](https://doi.org/10.1016/0003-9861(71)90089-4) · [PubMed 5134365](https://pubmed.ncbi.nlm.nih.gov/5134365/)
[^dallman-1984-hpa-feedback]: Dallman MF, Akana SF, Cascio CS, et al. Regulation of the hypothalamo-pituitary-adrenal axis during stress: feedback, facilitation and feeding. *J Steroid Biochem.* 1987;28(1-2):171-179. [doi:10.1016/0022-4731(87)90279-2](https://doi.org/10.1016/0022-4731(87)90279-2) · [PubMed 3116435](https://pubmed.ncbi.nlm.nih.gov/3116435/)
[^tsigos-2002-hpa-review]: Tsigos C, Chrousos GP. Hypothalamic-pituitary-adrenal axis, neuroendocrine factors and stress. *J Psychosom Res.* 2002;53(4):865-871. [doi:10.1016/s0022-3999(02)00429-4](https://doi.org/10.1016/s0022-3999(02)00429-4) · [PubMed 12377295](https://pubmed.ncbi.nlm.nih.gov/12377295/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

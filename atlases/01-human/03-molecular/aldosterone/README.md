---
schema: human-scale-entry/v1
id: aldosterone
name: Aldosterone
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Principal mineralocorticoid steroid (zona glomerulosa) that activates MR to upregulate ENaC/Na⁺-K⁺-ATPase, mediating renal Na⁺ retention and K⁺ excretion. Excess aldosterone drives hypertension, cardiac fibrosis, hypokalemia in HF, CKD, and Conn's syndrome."
aliases: ["mineralocorticoid", "MR agonist", "RAAS effector", "11β,21-dihydroxy-3,20-dioxopregn-4-en-18-al"]
sources:
  - id: pitt-1999-rales
    type: peer-reviewed
    cite: "Pitt B, Zannad F, Remme WJ, et al. The effect of spironolactone on morbidity and mortality in patients with severe heart failure. Randomized Aldactone Evaluation Study Investigators. N Engl J Med. 1999;341(10):709-717."
    doi: "10.1056/NEJM199909023411001"
    pmid: "10471456"
  - id: pitt-2003-ephesus
    type: peer-reviewed
    cite: "Pitt B, Remme W, Zannad F, et al. Eplerenone, a selective aldosterone blocker, in patients with left ventricular dysfunction after myocardial infarction. N Engl J Med. 2003;348(14):1309-1321."
    doi: "10.1056/NEJMoa030207"
    pmid: "12668699"
  - id: funder-2016-aldosterone-review
    type: peer-reviewed
    cite: "Funder JW. Mineralocorticoid receptors: distribution and activation. Heart Fail Rev. 2005;10(1):15-22."
    doi: "10.1007/s10741-005-2344-3"
    pmid: "15947883"
  - id: conn-1955-primary-aldosteronism
    type: peer-reviewed
    cite: "Conn JW. Primary aldosteronism, a new clinical syndrome. J Lab Clin Med. 1955;45(1):3-17."
    pmid: "13233623"
cross_links:
  - target: 01-human/03-molecular/angiotensin-ii
    relation: modulated-by
    note: "Angiotensin II is the primary stimulus for aldosterone synthesis and secretion from the zona glomerulosa via AT1R → phospholipase C → PKC → CYP11B2 upregulation."
  - target: 01-human/03-molecular/cortisol
    relation: modulates
    note: "Cortisol and aldosterone share affinity for the mineralocorticoid receptor; 11β-HSD2 in mineralocorticoid target tissues converts cortisol to inactive cortisone, preventing cortisol from flooding MR."
  - target: 01-human/03-molecular/vasopressin
    relation: modulates
    note: "Aldosterone and vasopressin (ADH) coordinate renal water and sodium retention; aldosterone increases luminal Na⁺ that drives aquaporin-mediated water reabsorption synergistically with ADH."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: modulates
    note: "MR activation in cardiomyocytes and cardiac fibroblasts promotes myocardial fibrosis, inflammation, and adverse remodeling; target of MR antagonist benefit in HFrEF (RALES, EPHESUS trials)."
  - target: 01-human/06-organ/kidney
    relation: modulates
    note: "Aldosterone acts on principal cells of the collecting duct: upregulates ENaC (Na⁺ absorption) and ROMK (K⁺ secretion) via transcriptional mechanisms, driving K⁺ wasting and Na⁺ retention."
  - target: 01-human/06-organ/heart
    relation: modulates
    note: "Excess aldosterone drives cardiac fibrosis (collagen I/III deposition), diastolic dysfunction, and increased risk of sudden cardiac death; MR antagonists reduce cardiac mortality in HF."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "Aldosterone is a key RAAS effector for blood pressure homeostasis; hyperaldosteronism is found in 5–10% of hypertensive patients and is the most common cause of secondary hypertension."
  - target: 01-human/07-system/renal-system
    relation: modulates
    note: "Aldosterone is the principal hormone controlling final sodium balance in the collecting duct; chronic excess causes hypokalemia, metabolic alkalosis, and accelerated CKD progression."
---

# Aldosterone

## Overview

Aldosterone is the principal **mineralocorticoid steroid hormone** of the human adrenal cortex, synthesized exclusively in the **zona glomerulosa** by the terminal enzyme **aldosterone synthase (CYP11B2)**. It is the final RAAS effector for sodium-potassium homeostasis, acting on principal cells of the renal collecting duct to retain sodium and excrete potassium via the mineralocorticoid receptor (MR, NR3C2).

First described clinically by Jerome Conn in 1955 [^conn-1955-primary-aldosteronism] — leading to "Conn's syndrome" (primary hyperaldosteronism) — aldosterone's role has since expanded dramatically from its classical view as a renal volume regulator to a **pro-fibrotic, pro-inflammatory cardiovascular hormone** whose excess is causally linked to cardiac fibrosis, heart failure progression, and adverse cardiovascular outcomes. This paradigm shift was established by two landmark randomized trials: **RALES** (1999) [^pitt-1999-rales] and **EPHESUS** (2003) [^pitt-2003-ephesus], which demonstrated that MR antagonists (spironolactone and eplerenone) significantly reduce morbidity and mortality in heart failure — even in patients on optimal RAAS blockade.

## Structure

### Chemical identity

Aldosterone is a **C21 steroid** (pregnane backbone) with three distinctive features that determine its unique mineralocorticoid activity:

| Feature | Chemical detail | Functional significance |
|:---|:---|:---|
| **C18 aldehyde** | C18 substituent is an aldehyde (–CHO), not a methyl group | Unique among steroid hormones; participates in an intramolecular hemiacetal with C11-OH |
| **C11 hemiacetal** | Intramolecular cyclization with C11-OH and C18-CHO | Structural feature detected in plasma; aldehyde form is the active receptor-binding species |
| **Δ4-3-ketone** | Conjugated enone at C3–C4 | Required for high-affinity MR binding |
| **11β,21-diols** | Hydroxyl groups at C11β and C21 | Mineralocorticoid selectivity; contrast with glucocorticoids (C17 hydroxyl) |

Molecular formula: C₂₁H₂₈O₅; MW: 360.44 g/mol. Plasma half-life: ~20 minutes. Circulating concentration (normal): 80–400 pmol/L (supine), up to 800 pmol/L (upright).

### Biosynthesis

Aldosterone is synthesized from cholesterol through the steroidogenic cascade, exclusively in the zona glomerulosa:

| Step | Enzyme | Product |
|:---|:---|:---|
| Cholesterol → Pregnenolone | CYP11A1 (mitochondria) | Pregnenolone |
| → Progesterone | 3β-HSD2 (SER) | Progesterone |
| → 11-Deoxycorticosterone | CYP21A2 (SER) | 11-Deoxycorticosterone |
| → Corticosterone | CYP11B1 (mitochondria) | Corticosterone |
| → 18-Hydroxycorticosterone | CYP11B2 (mitochondria) | 18-OH-corticosterone |
| → **Aldosterone** | **CYP11B2** (aldosterone synthase) | **Aldosterone** |

CYP11B2 catalyzes the final three steps (11β-hydroxylation, 18-hydroxylation, 18-oxidation) and is expressed only in the zona glomerulosa — whereas CYP11B1 (11β-hydroxylase) is expressed in the zona fasciculata and makes cortisol. This compartmentalization determines the separate regulation of cortisol vs. aldosterone production.

## Function

### Classical renal actions (principal cells, collecting duct)

Aldosterone acts via a **genomic mechanism** (latency: 30–60 min) to increase apical Na⁺ entry and basolateral Na⁺ export:

1. **ENaC upregulation**: Aldosterone increases expression and membrane trafficking of the epithelial sodium channel (ENaC; SCNN1A/B/G subunits) on the luminal membrane → ↑Na⁺ entry
2. **Na⁺-K⁺-ATPase**: Increases basolateral Na⁺-K⁺-ATPase expression → ↑Na⁺ extrusion into the interstitium
3. **ROMK (Kir1.1)**: Increases apical K⁺ secretion via renal outer medullary K⁺ channel → K⁺ excretion in urine
4. **SGK1 (serum- and glucocorticoid-regulated kinase 1)**: Primary early-response aldosterone target gene; SGK1 phosphorylates and inactivates **NEDD4-2** (ENaC ubiquitin ligase), stabilizing ENaC at the surface

Net: **Na⁺ retention → volume expansion → blood pressure increase; K⁺ excretion → hypokalemia (excess)**.

### Non-epithelial (extra-renal) actions

MR is expressed in multiple non-renal tissues, and aldosterone has important non-epithelial effects [^funder-2016-aldosterone-review]:

- **Heart**: MR activation in cardiomyocytes and fibroblasts → pro-fibrotic gene expression (collagen I/III, TGF-β1), oxidative stress, impaired calcium handling
- **Brain**: MR in hippocampus and autonomic centers regulates cortisolism response and sympathetic tone; excess aldosterone → sympathetic activation
- **Vascular wall**: MR in endothelial and smooth muscle cells → reduced NO bioavailability, increased oxidative stress, endothelial dysfunction
- **Adipose tissue**: MR in adipocytes promotes adipogenesis; links metabolic syndrome to hyperaldosteronism

## Mechanism

### Genomic (nuclear) MR signaling

1. **Aldosterone entry**: Lipophilic steroid diffuses across plasma membrane
2. **MR activation**: Aldosterone binds cytosolic MR (Kd ~0.5 nM) → displacement of heat-shock proteins → MR conformational change → nuclear translocation
3. **GRE/MRE binding**: MR homodimers (or MR-GR heterodimers) bind glucocorticoid/mineralocorticoid response elements (GRE/MRE) in target gene promoters
4. **Transcriptional induction**: ENaC subunits (SCNN1A/B/G), SGK1, GILZ, Na⁺-K⁺-ATPase, NF-κB p65 (in non-epithelial contexts), collagen I/III, TGF-β1

**MR selectivity from glucocorticoids**: MR has equal affinity for aldosterone and cortisol (~Kd 0.5 nM each). In aldosterone-target tissues (kidney, colon), the enzyme **11β-hydroxysteroid dehydrogenase type 2 (11β-HSD2)** converts cortisol (100-fold more abundant) to inactive cortisone, protecting MR from glucocorticoid occupancy. When 11β-HSD2 is inhibited (liquorice-derived glycyrrhizin, apparent mineralocorticoid excess syndrome), cortisol causes MR-dependent hypertension and hypokalemia.

### Non-genomic signaling

Aldosterone also activates rapid (seconds to minutes) signaling:
- **EGFR transactivation**: Aldosterone → MR → c-Src → EGFR → ERK1/2 → rapid ENaC trafficking
- **IP3/Ca²⁺**: MR-independent rapid aldosterone effects via membrane receptors (proposed GPER or GPR30)
- **MAPK activation**: In cardiac fibroblasts, rapid ERK activation precedes genomic responses

## Connections

- `modulated-by` → **[Angiotensin II](../angiotensin-ii/README.md)** — primary stimulus for aldosterone synthesis via AT1R → CYP11B2 upregulation
- `modulates` → **[Kidney](../../06-organ/kidney/README.md)** — collecting duct ENaC/ROMK regulation; final determinant of urinary Na⁺/K⁺ balance
- `modulates` → **[Heart](../../06-organ/heart/README.md)** — MR-mediated cardiac fibrosis; target of RALES/EPHESUS-proven MR antagonist therapy
- `modulates` → **[Cardiovascular System](../../07-system/cardiovascular-system/README.md)** — blood pressure regulation; endothelial dysfunction; hyperaldosteronism is the most common secondary hypertension cause
- `modulates` → **[Renal System](../../07-system/renal-system/README.md)** — sodium-potassium-water homeostasis; excess → hypokalemia, metabolic alkalosis, CKD progression

## Pathology

| Condition | Aldosterone role | Clinical features | Treatment |
|:---|:---|:---|:---|
| **Primary aldosteronism (Conn's syndrome)** | Autonomous excess (adenoma or bilateral hyperplasia) | Hypertension, hypokalemia, suppressed renin, metabolic alkalosis | Adrenalectomy (adenoma); MR antagonists (bilateral hyperplasia) |
| **Secondary hyperaldosteronism** | Renin-driven excess (renal artery stenosis, heart failure, cirrhosis, nephrotic syndrome) | Edema, hypokalemia; underlying disease drives presentation | Treat underlying cause; MR antagonists cautiously (hyperkalemia risk in CKD) |
| **Heart failure (HFrEF)** | Elevated aldosterone → cardiac fibrosis, arrhythmias, K⁺ loss (worsens digoxin toxicity) | RALES: spironolactone 30% ↓ mortality in NYHA III–IV HF [^pitt-1999-rales] | Spironolactone, eplerenone (EF ≤35%); finerenone (non-steroidal MRA) |
| **Post-MI LV dysfunction** | Excess aldosterone → adverse LV remodeling, fibrosis | EPHESUS: eplerenone 15% ↓ mortality in post-MI EF ≤40% [^pitt-2003-ephesus] | Eplerenone commenced within 3–14 days post-MI |
| **CKD / Diabetic nephropathy** | Aldosterone-driven glomerulosclerosis and tubular fibrosis | Proteinuria, accelerated GFR decline | Finerenone (FIDELIO-DKD: reduced CKD progression and CV events) |
| **Apparent mineralocorticoid excess (AME)** | 11β-HSD2 deficiency → cortisol occupies MR → aldosterone-like syndrome | Severe early-onset hypertension, hypokalemia; low renin, low aldosterone | Dexamethasone (suppress ACTH → reduce cortisol); MR antagonists |
| **Glucocorticoid-remediable aldosteronism (GRA)** | CYP11B2 under ACTH control (chimeric gene) → ACTH-driven aldosterone excess | Familial hypertension, low-renin, normal/mild K+ | Low-dose dexamethasone; MR antagonists |

[^pitt-1999-rales]: Pitt B, Zannad F, Remme WJ, et al. The effect of spironolactone on morbidity and mortality in patients with severe heart failure. *N Engl J Med.* 1999;341(10):709-717. [doi:10.1056/NEJM199909023411001](https://doi.org/10.1056/NEJM199909023411001) · [PubMed 10471456](https://pubmed.ncbi.nlm.nih.gov/10471456/)
[^pitt-2003-ephesus]: Pitt B, Remme W, Zannad F, et al. Eplerenone, a selective aldosterone blocker, in patients with left ventricular dysfunction after myocardial infarction. *N Engl J Med.* 2003;348(14):1309-1321. [doi:10.1056/NEJMoa030207](https://doi.org/10.1056/NEJMoa030207) · [PubMed 12668699](https://pubmed.ncbi.nlm.nih.gov/12668699/)
[^funder-2016-aldosterone-review]: Funder JW. Mineralocorticoid receptors: distribution and activation. *Heart Fail Rev.* 2005;10(1):15-22. [doi:10.1007/s10741-005-2344-3](https://doi.org/10.1007/s10741-005-2344-3) · [PubMed 15947883](https://pubmed.ncbi.nlm.nih.gov/15947883/)
[^conn-1955-primary-aldosteronism]: Conn JW. Primary aldosteronism, a new clinical syndrome. *J Lab Clin Med.* 1955;45(1):3-17. · [PubMed 13233623](https://pubmed.ncbi.nlm.nih.gov/13233623/)

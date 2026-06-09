---
schema: human-scale-entry/v1
id: prolactin
name: Prolactin
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "23 kDa pituitary lactotroph hormone suppressed by tuberoinfundibular dopamine (TIDA-D2R); suckling and TRH stimulate secretion; drives lactation (JAK2/STAT5) and suppresses GnRH → infertility; treated with cabergoline (D2 agonist) for prolactinoma."
aliases: ["PRL", "prolactin", "lactotropin", "hyperprolactinemia", "prolactinoma", "cabergoline", "galactorrhea", "lactation hormone", "TIDA"]
sources:
  - id: freeman-2000-prolactin-review
    type: peer-reviewed
    cite: "Freeman ME, Kanyicska B, Lerant A, Nagy G. Prolactin: structure, function, and regulation of secretion. Physiol Rev. 2000;80(4):1523-1631."
    doi: "10.1152/physrev.2000.80.4.1523"
    pmid: "11015620"
    url: "https://doi.org/10.1152/physrev.2000.80.4.1523"
    accessed: "2026-06-08"
  - id: melmed-2011-prolactinoma
    type: peer-reviewed
    cite: "Melmed S, Casanueva FF, Hoffman AR, et al. Diagnosis and treatment of hyperprolactinemia: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab. 2011;96(2):273-288."
    doi: "10.1210/jc.2010-1692"
    pmid: "21296991"
    url: "https://doi.org/10.1210/jc.2010-1692"
    accessed: "2026-06-08"
  - id: bole-feysot-1998-prlr
    type: peer-reviewed
    cite: "Bole-Feysot C, Goffin V, Edery M, Binart N, Kelly PA. Prolactin (PRL) and its receptor: actions, signal transduction pathways and phenotypes observed in PRL receptor knockout mice. Endocr Rev. 1998;19(3):225-268."
    doi: "10.1210/edrv.19.3.0334"
    pmid: "9626554"
    url: "https://doi.org/10.1210/edrv.19.3.0334"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/dopamine
    relation: modulated-by
    note: "Tuberoinfundibular dopamine (TIDA) neurons in the arcuate nucleus tonically inhibit lactotroph prolactin secretion via D2R/Gi; this is the dominant inhibitory brake on prolactin; cabergoline (D2 agonist) normalizes prolactin in 80-90% of prolactinoma patients."
  - target: 01-human/03-molecular/serotonin
    relation: modulated-by
    note: "5-HT2A and 5-HT2B receptors on pituitary lactotrophs stimulate prolactin release; SSRIs elevate prolactin via serotonin excess → galactorrhea in 2-5% of users; 5-HT-mediated prolactin elevation also occurs acutely after psychedelic 5-HT2A agonism."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Suckling simultaneously triggers oxytocin (milk ejection via myoepithelial contraction) and prolactin (milk synthesis via JAK2/STAT5 in alveolar cells); OT and PRL are the dual hormonal drivers of lactation; they share nipple sensory inputs to the hypothalamus."
  - target: 01-human/07-system/schizophrenia
    relation: connects-to
    note: "Antipsychotic D2 blockade removes TIDA inhibition → hyperprolactinemia; risperidone causes greatest elevation (45-100 ng/mL); resulting galactorrhea, sexual dysfunction, and bone loss are key drivers of antipsychotic non-adherence in schizophrenia."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Antipsychotic-induced hyperprolactinemia causes sexual dysfunction and anhedonia, driving medication non-adherence; postpartum prolactin decline may modulate MDD vulnerability via dopaminergic systems; cabergoline shows adjunctive antidepressant effects in preliminary trials."
  - target: 01-human/06-organ/brain
    relation: expressed-by
    note: "Anterior pituitary lactotrophs (~15% of cells) secrete prolactin under hypothalamic TIDA dopaminergic inhibition; PRLR is expressed in hippocampus and cortex (neuroplasticity); hypothyroidism raises TRH → cross-stimulates lactotrophs → secondary hyperprolactinemia."
---

# Prolactin

## Overview

**Prolactin (PRL)** is a 23 kDa polypeptide hormone secreted by **lactotroph cells** of the anterior pituitary, constituting approximately 15–20% of the gland's secretory cell population. It is named for its primary discovered function — stimulating lactation — but is now recognized as a **pleiotropic neuroendocrine hormone** with over 300 distinct biological actions, including roles in reproduction, immune modulation, osmoregulation, neuroplasticity, and behavior [^freeman-2000-prolactin-review].

**Key quantitative facts:**
- Normal serum prolactin: 2–25 ng/mL (women); 2–18 ng/mL (men)
- Pregnancy: prolactin rises progressively from ~25 ng/mL to 200–400 ng/mL at term
- Nursing mothers: prolactin 50–150 ng/mL; suckling pulses elevate by 2–10× within 30 min
- Prolactinoma: serum prolactin >100 ng/mL (macroadenoma) or 25–100 ng/mL (microadenoma)
- Hyperprolactinemia threshold (symptomatic): >25 ng/mL in most laboratories

Uniquely among anterior pituitary hormones, prolactin is subject to **tonic inhibition** rather than tonic stimulation from the hypothalamus — dopamine from the arcuate TIDA (tuberoinfundibular dopaminergic) neurons constitutes the principal inhibitory brake, which must be removed for prolactin secretion to increase. This architecture explains why virtually any hypothalamic-pituitary stalk lesion (which severs dopamine delivery) — as well as any dopamine-blocking drug — causes hyperprolactinemia.

## Structure

### Molecular identity

Prolactin is a **single-chain globular polypeptide** of 199 amino acids (MW ~23 kDa in humans). It is encoded by the **PRL gene** on chromosome 6p22.3 and belongs to the **cytokine superfamily (hematopoietic growth factor family)**, sharing structural homology with growth hormone (GH) and placental lactogen (PL) — all three evolved from a common ancestral gene via duplication.

**Post-translational forms:**
- **Little PRL (23 kDa):** The biologically dominant monomeric form; constitutes ~60–80% of circulating prolactin; full receptor-binding and signaling activity
- **Big PRL (50–60 kDa):** Dimeric; reduced bioactivity; elevated in macroprolactinemia (a benign cause of apparent hyperprolactinemia)
- **Big-big PRL (>100 kDa):** Aggregated with IgG antibodies (macro-prolactin); low bioactivity; important to identify by PEG precipitation before diagnosing true prolactinoma — macro-prolactinemia does not require treatment

**Glycosylation:** ~16–17 kDa glycosylated variant exists (Asn31 glycosylation); constitutes ~25% of anterior pituitary PRL; less receptor-binding affinity than the unglycosylated form.

**16K prolactin fragment:** Plasmin or cathepsin D cleaves prolactin → N-terminal 16 kDa fragment with **anti-angiogenic** activity (unlike full-length PRL); plays a role in peripartum cardiomyopathy pathogenesis.

### Prolactin receptor (PRLR)

PRLR is a **class I cytokine receptor** — a single transmembrane domain with no intrinsic kinase activity [^bole-feysot-1998-prlr]:

| Property | Detail |
|:---|:---|
| **Gene** | PRLR (chromosome 5p14-p13) |
| **Structure** | Type I cytokine receptor; extracellular domain + single TM domain + intracellular domain |
| **Signal activation** | One PRL molecule cross-links two PRLR monomers → dimerization → JAK2 transphosphorylation |
| **Downstream cascade** | JAK2 → STAT5a/b phosphorylation → nuclear translocation → target gene transcription |
| **Isoforms** | Long form (signaling); short form (regulatory); intermediate; soluble (serum PRL-binding protein) |
| **Expression** | Mammary gland, ovary, testis, liver, kidney, adipose, adrenal, immune cells, brain (hippocampus, cerebral cortex, choroid plexus) |

**Prolactin signaling cascade:**
1. PRL binds PRLR extracellular domain
2. Receptor homodimerization → JAK2 transphosphorylation → Y→pY
3. STAT5a/b phosphorylation → STAT5 homodimerization
4. Nuclear translocation → GAS element binding → transcription of milk protein genes (αS1-casein, β-casein, whey acidic protein), immune genes, and anti-apoptotic genes
5. Also activates: MAPK/ERK (cell proliferation), PI3K/AKT (survival), SRC family kinases

## Function

### Lactation

Prolactin's classical and best-characterized role is orchestrating **mammary gland development and milk production**:

**Mammary gland development (lobuloalveolar growth):**
- During pregnancy: rising estrogen + progesterone + PRL (from pituitary + placenta) drive ductal elongation and alveolar proliferation
- After parturition: progesterone withdrawal unmasks prolactin-driven milk secretion
- Prolactin → JAK2/STAT5 in mammary epithelium → transcription of α-lactalbumin (enables lactose synthesis), caseins, and fatty acid synthase → milk composition

**Milk ejection vs. milk synthesis (two-hormone model):**
- **Oxytocin:** Milk ejection — acts on myoepithelial cells surrounding alveoli → contraction → milk into ducts → nipple
- **Prolactin:** Milk synthesis — acts on alveolar epithelial cells → milk protein and fat production; suckling-induced PRL surge sustains supply

**Lactational amenorrhea:**
- High prolactin → suppresses GnRH pulse generator (via direct action on GnRH neurons and via endogenous opioids including β-endorphin) → ↓ FSH/LH → anovulation
- Provides up to 98% contraceptive protection for ~6 months postpartum in fully breastfeeding women
- Used in traditional societies as natural birth spacing; mechanism is dose-dependent on suckling frequency

### Reproductive modulation

Hyperprolactinemia at any time — whether from prolactinoma, drugs, or stress — suppresses the HPG axis [^melmed-2011-prolactinoma]:
- PRL → inhibits GnRH pulse frequency (via kisspeptin-NKB-dynorphin neuronal inhibition in ARC)
- ↓ GnRH → ↓ LH/FSH → anovulation/oligomenorrhea (women) or ↓ testosterone (men)
- Biochemical cascade: prolactinoma → amenorrhea, infertility, reduced libido, osteoporosis (estrogen deficiency)

### Immune modulation

Prolactin functions as a **cytokine-like immunomodulator**:
- PRLR expressed on T cells, B cells, NK cells, dendritic cells, and macrophages
- Promotes Th1 responses (IL-2, IFN-γ production) and NK cell cytotoxicity
- Autoimmune diseases: females (who have higher PRL) develop SLE, RA, and MS at higher rates; cabergoline has shown immune-modulating effects in SLE animal models
- PRL required for normal T-cell function: PRLR knockout mice show impaired T-cell proliferative responses

### Neuroplasticity and neuroprotection

Prolactin and PRLR are expressed in **hippocampus, cortex, and choroid plexus**:
- Promotes adult neurogenesis in the subventricular zone (SVZ) and possibly hippocampus during pregnancy
- PRLR KO female mice show impaired olfactory neurogenesis — relevant to maternal recognition of offspring
- Neuroprotection: PRL reduces kainate-induced seizure activity in rodent models; modulates hypothalamic neural circuits underlying feeding and body weight
- May contribute to the neural plasticity of maternal brain (maternal bonding circuits)

## Mechanism

### Hypothalamic control of prolactin secretion

Unlike other anterior pituitary hormones, prolactin is regulated primarily by **tonic inhibition** via the **hypothalamic-pituitary portal system**:

**Inhibitory control (dominant):**
- **Dopamine (DA):** Produced by **TIDA neurons** (tuberoinfundibular dopaminergic neurons) in the arcuate nucleus (ARC) → axons terminate in the median eminence → DA released into hypothalamic-pituitary portal blood → reaches lactotrophs → **D2R/Gαi → adenylyl cyclase inhibition → ↓ cAMP → ↓ PRL secretion**
- TIDA neuron activity is high under baseline conditions (non-pregnant, non-lactating); suckling-induced NE and oxytocin reduce TIDA activity → DA release drops → lactotrophs disinhibited → PRL surge

**Stimulatory signals:**
| Signal | Source | Mechanism |
|:---|:---|:---|
| **TRH (thyrotropin-releasing hormone)** | Hypothalamic PVN | TRH-R1 (Gq/PLC/IP3/PKC) → PRL exocytosis; explains hyperprolactinemia in hypothyroidism |
| **Suckling reflex** | Nipple mechanoreceptors → spinal cord → hypothalamus | Reduces TIDA DA release; increases oxytocin, VIP, and β-endorphin input to lactotrophs |
| **Serotonin** | Raphe → pituitary | 5-HT2A/2B on lactotrophs → Gq/IP3 → PRL release; SSRIs → galactorrhea |
| **Estrogen** | Ovary | ERα on lactotrophs → upregulates PRL gene transcription + lactotroph proliferation; explains sex difference and lactotroph hyperplasia in pregnancy |
| **VIP (vasoactive intestinal peptide)** | Hypothalamic neurons | VPAC1 → Gs/cAMP/PKA → PRL release |
| **Oxytocin** | PVN neurons | OTR on lactotrophs → facilitates PRL release (minor direct effect; primarily via suckling reflex) |
| **Stress/CRH** | Stress circuits | Acute stress elevates PRL (part of stress hormone response); mechanism involves CRH → serotonin and β-endorphin; chronic stress may suppress via DA |

### Feedback regulation

Prolactin has **ultrashort-loop negative feedback** on its own secretion:
1. PRL released → acts on TIDA neurons (which express PRLR) → activates TIDA → ↑ DA release → ↓ subsequent PRL secretion
2. Also acts at the pituitary level (short loop) and possibly at the CNS (long loop via systemic circulation)

This feedback circuit ensures that prolactin remains within physiological range and prevents runaway hyperprolactinemia under normal conditions.

### JAK2/STAT5 signaling in mammary gland

In the lactating mammary gland, PRL → PRLR → JAK2/STAT5 pathway activates:
- **β-casein promoter:** Mammary-specific STAT5 binding → milk protein synthesis
- **GLUT1 upregulation:** Ensures glucose delivery for lactose synthesis
- **Fatty acid synthase (FAS):** Supports milk fat production
- **Anti-apoptotic genes (Bcl-xL):** Maintains lactocyte viability during lactation
- **Insulin cooperation:** Insulin/IGF-1 co-stimulation of PRLR signaling amplifies milk yield; diabetic mothers often have reduced milk production

## Connections

- `modulated-by` → **[Dopamine](../dopamine/README.md)** — tuberoinfundibular dopamine (TIDA) neurons in the arcuate nucleus tonically inhibit lactotroph prolactin secretion via D2R/Gi; the dominant inhibitory brake on prolactin; cabergoline (D2 agonist) normalizes prolactin in 80-90% of prolactinoma patients.
- `modulated-by` → **[Serotonin](../serotonin/README.md)** — 5-HT2A and 5-HT2B receptors on pituitary lactotrophs stimulate prolactin release; SSRIs elevate prolactin via serotonin excess → galactorrhea in 2-5% of users; 5-HT-mediated prolactin elevation also occurs acutely after psychedelic 5-HT2A agonism.
- `connects-to` → **[Oxytocin](../oxytocin/README.md)** — suckling simultaneously triggers oxytocin (milk ejection via myoepithelial contraction) and prolactin (milk synthesis via JAK2/STAT5 in alveolar cells); OT and PRL are the dual hormonal drivers of lactation; they share nipple sensory inputs to the hypothalamus.
- `connects-to` → **[Schizophrenia](../../07-system/schizophrenia/README.md)** — antipsychotic D2 blockade removes TIDA inhibition → hyperprolactinemia; risperidone causes greatest elevation (45-100 ng/mL); resulting galactorrhea, sexual dysfunction, and bone loss are key drivers of antipsychotic non-adherence in schizophrenia.
- `connects-to` → **[Major Depressive Disorder](../../07-system/major-depressive-disorder/README.md)** — antipsychotic-induced hyperprolactinemia causes sexual dysfunction and anhedonia, driving medication non-adherence; postpartum prolactin decline may modulate MDD vulnerability via dopaminergic systems; cabergoline shows adjunctive antidepressant effects in preliminary trials.
- `expressed-by` → **[Brain](../../06-organ/brain/README.md)** — anterior pituitary lactotrophs (~15% of cells) secrete prolactin under hypothalamic TIDA dopaminergic inhibition; PRLR is expressed in hippocampus and cortex (neuroplasticity); hypothyroidism raises TRH → cross-stimulates lactotrophs → secondary hyperprolactinemia.

## Pathology

| Condition | Mechanism | Key features |
|:---|:---|:---|
| **Prolactinoma (microadenoma <10 mm)** | Clonal lactotroph expansion; PRL 25-200 ng/mL | Oligomenorrhea, infertility, galactorrhea; cabergoline first-line (80-90% response); 95% shrink |
| **Prolactinoma (macroadenoma ≥10 mm)** | Larger clonal mass; PRL often >200 ng/mL | Mass effects: visual field loss (chiasm compression), headache, hypopituitarism; cabergoline ± surgery |
| **Drug-induced hyperprolactinemia** | D2 receptor blockade (antipsychotics, metoclopramide, domperidone) | Most common cause of pathological hyperprolactinemia; risperidone > haloperidol > olanzapine; clozapine/quetiapine relatively prolactin-sparing |
| **Hypothyroidism** | ↑ TRH → cross-stimulates PRLR on lactotrophs | Often mild elevation 25-50 ng/mL; resolves with thyroid hormone replacement |
| **Stalk compression** | Tumor, craniopharyngioma, granuloma severing portal blood → DA loss | "Disconnection" hyperprolactinemia; usually <150 ng/mL (vs. >200 in true prolactinoma) |
| **Macroprolactinemia** | PRL-IgG complexes (>100 kDa); reduced clearance | Asymptomatic; PEG precipitation confirms; no treatment needed |
| **Peripartum cardiomyopathy** | 16K PRL fragment (antiangiogenic) damages cardiac endothelium | Bromocriptine/cabergoline adjunct in cases with elevated oxidized PRL |
| **Lactational amenorrhea** | PRL → GnRH pulse suppression → anovulation | Natural contraception (98% efficacy with full breastfeeding ≤6 months postpartum) |

[^freeman-2000-prolactin-review]: Freeman ME, Kanyicska B, Lerant A, Nagy G. Prolactin: structure, function, and regulation of secretion. *Physiol Rev.* 2000;80(4):1523-1631. [doi:10.1152/physrev.2000.80.4.1523](https://doi.org/10.1152/physrev.2000.80.4.1523) · [PubMed 11015620](https://pubmed.ncbi.nlm.nih.gov/11015620/)
[^melmed-2011-prolactinoma]: Melmed S, Casanueva FF, Hoffman AR, et al. Diagnosis and treatment of hyperprolactinemia: an Endocrine Society clinical practice guideline. *J Clin Endocrinol Metab.* 2011;96(2):273-288. [doi:10.1210/jc.2010-1692](https://doi.org/10.1210/jc.2010-1692) · [PubMed 21296991](https://pubmed.ncbi.nlm.nih.gov/21296991/)
[^bole-feysot-1998-prlr]: Bole-Feysot C, Goffin V, Edery M, Binart N, Kelly PA. Prolactin (PRL) and its receptor: actions, signal transduction pathways and phenotypes observed in PRL receptor knockout mice. *Endocr Rev.* 1998;19(3):225-268. [doi:10.1210/edrv.19.3.0334](https://doi.org/10.1210/edrv.19.3.0334) · [PubMed 9626554](https://pubmed.ncbi.nlm.nih.gov/9626554/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

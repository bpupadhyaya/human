---
schema: human-scale-entry/v1
id: growth-hormone
name: Growth Hormone
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "22 kDa pituitary somatotroph hormone regulated by GHRH and somatostatin; drives hepatic IGF-1 (JAK2/STAT5b), growth, muscle anabolism, and lipolysis; acromegaly from GH-secreting adenoma; GH deficiency causes growth failure and metabolic syndrome."
aliases: ["GH", "growth hormone", "somatotropin", "hGH", "somatotroph", "acromegaly", "gigantism", "GH deficiency", "GHRH", "somatostatin", "IGF-1 axis", "pegvisomant"]
sources:
  - id: melmed-2019-acromegaly-review
    type: peer-reviewed
    cite: "Melmed S. Acromegaly pathogenesis and treatment. J Clin Invest. 2009;119(11):3189-3202."
    doi: "10.1172/JCI39375"
    pmid: "19884662"
    url: "https://doi.org/10.1172/JCI39375"
    accessed: "2026-06-08"
  - id: van-cauter-2000-gh-sleep
    type: peer-reviewed
    cite: "Van Cauter E, Plat L, Scharf MB, et al. Simultaneous stimulation of slow-wave sleep and growth hormone secretion by gamma-hydroxybutyrate in normal young men. J Clin Invest. 1997;100(3):745-753."
    doi: "10.1172/JCI119587"
    pmid: "9239424"
    url: "https://doi.org/10.1172/JCI119587"
    accessed: "2026-06-08"
  - id: jorgensen-1989-gh-deficiency
    type: peer-reviewed
    cite: "Jørgensen JO, Pedersen SA, Thuesen L, et al. Beneficial effects of growth hormone treatment in GH-deficient adults. Lancet. 1989;1(8649):1221-1225."
    doi: "10.1016/s0140-6736(89)92328-7"
    pmid: "2566796"
    url: "https://doi.org/10.1016/s0140-6736(89)92328-7"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/igf-1
    relation: modulates
    note: "GH stimulates hepatic IGF-1 synthesis via JAK2/STAT5b (somatotropic axis effector); IGF-1 feeds back to suppress pituitary GH and hypothalamic GHRH; IGF-1 mediates GH anabolic actions on muscle, bone, and cartilage; serum IGF-1 is the gold-standard screening test for acromegaly."
  - target: 01-human/06-organ/brain
    relation: expressed-by
    note: "Pituitary somatotrophs secrete GH under GHRH (stimulatory) and somatostatin (inhibitory) control; GH-secreting adenoma causes acromegaly; somatostatin analogues (octreotide, lanreotide) are first-line therapy; pegvisomant (GHR antagonist) normalises IGF-1 in refractory cases."
  - target: 01-human/03-molecular/dopamine
    relation: modulated-by
    note: "Dopamine agonists (apomorphine, bromocriptine) stimulate GH via D2R on somatotrophs; paradoxically, in acromegaly D2 agonists suppress GH in ~75% — exploited therapeutically with cabergoline; dopaminergic tone explains part of the GH response to vigorous exercise."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "GH secretion is coupled to slow-wave sleep (SWS): 70-80% of daily output occurs in the first SWS episode within 1 hour of sleep onset; insomnia fragments SWS → suppresses GH; GH deficiency impairs sleep quality; recombinant GH therapy partially restores SWS architecture."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "GH deficiency increases visceral adiposity and dyslipidemia, phenocopying metabolic syndrome; GH therapy reduces visceral fat ~15-20% in deficient adults; leptin resistance in obesity suppresses GHRH pulsatility → blunted GH amplitude; weight loss restores GH secretory dynamics."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "GH raises plasma glucose via hepatic output and insulin resistance (GHR/STAT5 → IRS-1 serine phosphorylation); acromegaly causes T2DM in 25-40%; exogenous GH raises insulin requirements; declining GH/IGF-1 with aging contributes to metabolic inflexibility and insulin resistance."
---

# Growth Hormone

## Overview

**Growth hormone (GH; somatotropin)** is a **22 kDa single-chain polypeptide** hormone secreted by **somatotroph cells** of the anterior pituitary — the most abundant cell type, constituting ~50% of the gland. Named for its essential role in longitudinal growth during childhood, GH is now recognized as a **pleiotropic metabolic hormone** that remains active throughout life, regulating body composition, intermediary metabolism, bone density, cardiovascular function, immune modulation, and cognitive performance in adults [^jorgensen-1989-gh-deficiency].

**GH-IGF-1 axis (somatotropic axis):**
Hypothalamic GHRH (arcuate nucleus) → portal blood → pituitary somatotroph GHRH-R → GH exocytosis. Somatostatin (periventricular nucleus) suppresses GH release. GH → peripheral GH receptor (GHR, liver >> bone, muscle, fat) → JAK2/STAT5b → transcriptional activation → **IGF-1 synthesis**. IGF-1 feeds back at both pituitary (suppresses GH) and hypothalamus (stimulates somatostatin, reduces GHRH) — the classic negative feedback loop.

GH secretion is **pulsatile** (4-6 pulses/day) with the largest pulse occurring within 1 hour of sleep onset during slow-wave sleep (SWS). Basal GH between pulses is essentially undetectable in healthy adults. Total daily GH output peaks in puberty and then declines ~14%/decade after age 30.

**Normal serum GH:** <5 µg/L in healthy adults (between pulses); IGF-1 (age/sex-normalized) is the preferred surrogate marker because it integrates GH pulsatility over hours.

## Structure

### Molecular identity

GH is a **single-chain 191-amino acid polypeptide** (MW ~22 kDa) with two intrachain disulfide bonds, encoded by the **GH1 gene** on chromosome 17q23.3. The GH gene cluster includes GH1 (pituitary), GH2 (placenta), CSH1 and CSH2 (placental lactogens), and CSHL1.

**GH isoforms:**
- **22 kDa (major):** Monomeric; full receptor-binding activity; 75% of pituitary GH
- **20 kDa (minor):** Alternative splicing (exon 3 deletion); 5-10% of pituitary GH; reduced diabetogenic activity but full growth-promoting activity; may explain differential GH actions
- **Oligomers:** Dimers and polymers of 22 kDa; reduced bioactivity; contribute to immunoreactive GH without equivalent bioactivity

### GH receptor (GHR) and JAK2/STAT5 signaling

GHR is a **class I cytokine receptor** (type 1 cytokine receptor superfamily), structurally related to PRLR:

| Feature | Detail |
|:---|:---|
| **Activation** | One GH molecule cross-links two GHR monomers (sequential binding via Site 1, then Site 2) → receptor homodimerization |
| **JAK2 activation** | Constitutively associated JAK2 transphosphorylates each other → Y→pY in intracellular domains |
| **STAT5b** | Primary GH-activated STAT; pY-STAT5b homodimerizes → nucleus → IGF-1 gene transcription |
| **Other signals** | MAPK/ERK (proliferation); PI3K/Akt (survival); SOCS proteins provide feedback inhibition |
| **Liver** | Primary site of IGF-1 synthesis (~75% of circulating IGF-1 from hepatocytes); also the major GH metabolic action site |

**STAT5b in sex-specific gene expression:**
Pulsatile (male-pattern) vs. continuous (female-pattern) GH stimulation of STAT5b generates sexually dimorphic hepatic gene expression — including CYP450 enzymes, IGFBP-3, and other metabolic proteins. This explains why males and females have different GH secretion patterns and body composition responses.

### Hypothalamic regulation

| Regulator | Source | Receptor | Effect |
|:---|:---|:---|:---|
| **GHRH** | Arcuate nucleus (NPY/GHRH neurons) | GHRH-R (Gs/cAMP/PKA) | Stimulates GH synthesis and release |
| **Somatostatin (SST)** | Periventricular nucleus | SST-R2 and SST-R5 (Gi/cAMP) | Inhibits GH release (gates GH pulses) |
| **Ghrelin** | Gastric A-like cells (also hypothalamus) | GHS-R1a | Potent GH secretagogue; co-operates with GHRH; stimulates appetite independently |
| **IGF-1** | Liver (blood-born) | IGF-1R on somatotrophs | Negative feedback; reduces GH pulsatility |
| **Glucose** | Blood glucose | Somatotroph glucose sensing | Acute hyperglycemia suppresses GH; hypoglycemia stimulates GH — the basis of the insulin tolerance test (ITT) |

## Function

### Growth and skeletal development

GH drives **longitudinal bone growth** in prepubertal children via:
1. GH → periosteal and epiphyseal chondrocytes → direct stimulation
2. GH → hepatic IGF-1 → systemic + local IGF-1 → chondrocyte and osteoblast proliferation
3. Both "dual effector theory" pathways operate in parallel

**Growth hormone deficiency in children:** Growth velocity <4 cm/year; GH provocation test (ITT or arginine) confirms: peak GH <10 µg/L (WHO threshold) or <8-10 µg/L (country-specific). Recombinant hGH (rhGH) therapy begun before epiphyseal closure achieves near-normal adult height.

### Adult GH actions (body composition)

Beyond childhood growth, GH maintains:
- **Muscle mass:** GH → IGF-1 → Akt/mTOR → protein synthesis; GH-deficient adults lose lean mass
- **Lipolysis:** GH directly activates hormone-sensitive lipase in adipose → FFA release → counter-regulatory during fasting
- **Bone density:** GH/IGF-1 stimulates osteoblasts; adult GH deficiency reduces BMD → osteoporosis risk
- **Cardiac function:** GH promotes cardiomyocyte hypertrophy; GH deficiency → reduced cardiac mass, ejection fraction, exercise capacity
- **Immune function:** GH promotes T-cell and NK-cell activity; immune senescence correlates with GH/IGF-1 decline

### Counter-regulatory metabolism

GH is one of the four **counter-regulatory hormones** (alongside glucagon, epinephrine, cortisol) that oppose insulin-mediated glucose disposal:
- GH raises plasma glucose by stimulating hepatic glycogenolysis and gluconeogenesis
- GH causes peripheral insulin resistance via GHR-STAT5 → upregulation of SOCS3 → IRS-1 serine phosphorylation → PI3K uncoupling
- This action is physiologically appropriate during fasting (preserving glucose for the brain) but becomes pathological in acromegaly or with pharmacological GH excess

### Sleep-linked secretion

GH secretion is tightly synchronized with **slow-wave sleep (SWS; NREM stage N3)** via mechanisms that include:
- GHRH and somatostatin coordination: highest GHRH pulse amplitude accompanies first SWS onset; somatostatin withdrawal at sleep onset disinhibits GH
- Sleep onset → GHRH surge → combined with ghrelin (which peaks with hunger/fasting and at sleep onset) → maximal GH pulse
- **~70-80% of the 24-hour GH total is secreted in the first 2 hours of sleep** [^van-cauter-2000-gh-sleep]
- Practical consequence: sleep disruption, shift work, or untreated sleep apnea significantly suppresses GH and accelerates age-related GH decline

## Mechanism

### Acromegaly and gigantism: GH excess

**Source:** GH-secreting pituitary adenoma (somatotropinoma) — 95% sporadic; ~30% have somatic *GNAS* mutations (Gs-α R201 → constitutive cAMP → somatotroph proliferation + GH hypersecretion); MEN1 and AIP mutations account for minority of cases.

**Clinical features of acromegaly (post-epiphyseal fusion):**
- Acral overgrowth: enlarged hands, feet, jaw (prognathism), frontal bossing
- Organomegaly: cardiomegaly (causes ~25% of mortality), hepatomegaly
- Soft-tissue changes: thick skin, skin tags, coarsened features
- Metabolic: T2DM (25-40%), hypertension, hyperlipidemia
- Colonic polyps → 2-3× colorectal cancer risk → colonoscopy surveillance required
- Carpal tunnel syndrome; sleep apnea

**Diagnosis:**
1. Serum IGF-1 (age/sex-normalized): elevated in >90%
2. Glucose suppression test (75g OGTT): GH fails to suppress below 1 µg/L (normal) in acromegaly
3. MRI pituitary: identifies adenoma size and cavernous sinus invasion

**Treatment:**
| Approach | Agents | Response |
|:---|:---|:---|
| **Surgery (first-line)** | Transsphenoidal adenomectomy | 60-80% cure rate (microadenomas); 40-60% macroadenomas |
| **Somatostatin analogues** | Octreotide LAR, lanreotide Autogel | IGF-1 normalization in 50-60%; suppress GH to <2.5 µg/L in 60-70% |
| **GHR antagonist** | Pegvisomant (SC injection) | IGF-1 normalization in >90%; does not suppress GH; risk of adenoma growth |
| **D2 agonist** | Cabergoline | GH normalization in ~35% (best for mixed GH/PRL tumors); oral, low cost |
| **Radiotherapy** | Stereotactic radiosurgery (Gamma Knife) | 50-60% normalization over 10+ years; hypopituitarism risk |

### Growth hormone deficiency (GHD)

**Causes:**
- **Childhood-onset (CO-GHD):** Pituitary aplasia/hypoplasia; craniopharyngioma (most common pituitary tumor of childhood); radiation; idiopathic
- **Adult-onset (AO-GHD):** Non-functional pituitary adenoma or treatment; Sheehan syndrome (postpartum pituitary infarction); traumatic brain injury; idiopathic
- **Isolated GHD vs. panhypopituitarism:** GHD often occurs with other pituitary deficiencies (TSH, ACTH, LH/FSH, ADH); any 2+ pituitary deficiencies → always test for GHD

**GH provocation tests (required for diagnosis):**
- **Insulin tolerance test (ITT):** Gold standard; insulin → hypoglycemia → peak GH <3-5 µg/L = severe GHD; contraindicated in epilepsy, ischemic heart disease
- **Glucagon stimulation test (GST):** Alternative; IV glucagon → hypoglycemia→GH release; safer
- **GHRH-arginine test:** Arginine potentiates GHRH → GH peak; body weight-dependent thresholds

**Treatment:** rhGH (recombinant hGH) SC injection once daily; dose titrated by IGF-1 response; improves lean mass, bone density, lipid profile, quality of life, and cardiovascular risk in GHD adults [^jorgensen-1989-gh-deficiency].

## Connections

- `modulates` → **[IGF-1](../igf-1/README.md)** — GH stimulates hepatic IGF-1 synthesis via JAK2/STAT5b (somatotropic axis effector); IGF-1 feeds back to suppress pituitary GH and hypothalamic GHRH; IGF-1 mediates GH anabolic actions on muscle, bone, and cartilage; serum IGF-1 is the gold-standard screening test for acromegaly.
- `expressed-by` → **[Brain](../../06-organ/brain/README.md)** — pituitary somatotrophs secrete GH under GHRH (stimulatory) and somatostatin (inhibitory) control; GH-secreting adenoma causes acromegaly; somatostatin analogues (octreotide, lanreotide) are first-line therapy; pegvisomant (GHR antagonist) normalises IGF-1 in refractory cases.
- `modulated-by` → **[Dopamine](../dopamine/README.md)** — dopamine agonists (apomorphine, bromocriptine) stimulate GH via D2R on somatotrophs; paradoxically, in acromegaly D2 agonists suppress GH in ~75% — exploited therapeutically with cabergoline; dopaminergic tone explains part of the GH response to vigorous exercise.
- `connects-to` → **[Insomnia Disorder](../../07-system/insomnia-disorder/README.md)** — GH secretion is coupled to slow-wave sleep (SWS): 70-80% of daily output occurs in the first SWS episode within 1 hour of sleep onset; insomnia fragments SWS → suppresses GH; GH deficiency impairs sleep quality; recombinant GH therapy partially restores SWS architecture.
- `connects-to` → **[Obesity](../../07-system/obesity/README.md)** — GH deficiency increases visceral adiposity and dyslipidemia, phenocopying metabolic syndrome; GH therapy reduces visceral fat ~15-20% in deficient adults; leptin resistance in obesity suppresses GHRH pulsatility → blunted GH amplitude; weight loss restores GH secretory dynamics.
- `connects-to` → **[Type 2 Diabetes](../../07-system/type-2-diabetes/README.md)** — GH raises plasma glucose via hepatic output and insulin resistance (GHR/STAT5 → IRS-1 serine phosphorylation); acromegaly causes T2DM in 25-40%; exogenous GH raises insulin requirements; declining GH/IGF-1 with aging contributes to metabolic inflexibility and insulin resistance.

## Pathology

| Condition | Mechanism | Key features |
|:---|:---|:---|
| **Acromegaly** | GH-secreting pituitary adenoma (often *GNAS* Gs-α mutation) | Acral overgrowth, organomegaly, T2DM, cardiomegaly; IGF-1 elevated; glucose suppression test; surgery (first-line), octreotide, pegvisomant |
| **Gigantism** | GH adenoma before epiphyseal closure | Excess height (>7 feet possible); same adenoma etiology as acromegaly |
| **Growth hormone deficiency (childhood)** | Pituitary aplasia, craniopharyngioma, radiation, idiopathic | Growth velocity <4 cm/year; peak GH <10 µg/L on provocation; rhGH therapy → near-normal height |
| **Adult GHD** | Non-functional pituitary adenoma, radiation, Sheehan syndrome | Reduced lean mass, increased visceral fat, low BMD, fatigue, impaired QoL; rhGH therapy reverses metabolic features |
| **MEN1-associated GH adenoma** | MEN1 (menin) LOF → pituitary, parathyroid, pancreatic neuroendocrine tumors | GH adenoma + hypercalcemia (parathyroid) + pancreatic NET |
| **McCune-Albright syndrome** | GNAS somatic mosaic mutations → activating Gs-α | Polyostotic fibrous dysplasia + café-au-lait spots + GH excess (acromegaly/gigantism); diagnosis of exclusion |
| **IGF-1 deficiency (Laron syndrome)** | GHR loss-of-function → elevated GH, undetectable IGF-1 | Severe growth failure; recombinant IGF-1 (mecasermin) is the treatment |

[^melmed-2019-acromegaly-review]: Melmed S. Acromegaly pathogenesis and treatment. *J Clin Invest.* 2009;119(11):3189-3202. [doi:10.1172/JCI39375](https://doi.org/10.1172/JCI39375) · [PubMed 19884662](https://pubmed.ncbi.nlm.nih.gov/19884662/)
[^van-cauter-2000-gh-sleep]: Van Cauter E, Plat L, Scharf MB, et al. Simultaneous stimulation of slow-wave sleep and growth hormone secretion by gamma-hydroxybutyrate in normal young men. *J Clin Invest.* 1997;100(3):745-753. [doi:10.1172/JCI119587](https://doi.org/10.1172/JCI119587) · [PubMed 9239424](https://pubmed.ncbi.nlm.nih.gov/9239424/)
[^jorgensen-1989-gh-deficiency]: Jørgensen JO, Pedersen SA, Thuesen L, et al. Beneficial effects of growth hormone treatment in GH-deficient adults. *Lancet.* 1989;1(8649):1221-1225. [doi:10.1016/s0140-6736(89)92328-7](https://doi.org/10.1016/s0140-6736(89)92328-7) · [PubMed 2566796](https://pubmed.ncbi.nlm.nih.gov/2566796/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

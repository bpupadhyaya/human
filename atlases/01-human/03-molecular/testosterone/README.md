---
schema: human-scale-entry/v1
id: testosterone
name: Testosterone
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "19-carbon androgen from Leydig cells via CYP17A1; binds androgen receptor → spermatogenesis, muscle anabolism, bone density, and libido; 5α-reductase converts to DHT; aromatase to estradiol; hypogonadism causes osteoporosis; prostate cancer driven by testosterone-AR signaling."
aliases: ["T", "17β-testosterone", "total testosterone", "free testosterone", "androgen", "male sex hormone", "TRT", "testosterone replacement therapy"]
sources:
  - id: bhasin-2010-jcem-testosterone
    type: peer-reviewed
    cite: "Bhasin S, Cunningham GR, Hayes FJ, et al. Testosterone therapy in men with androgen deficiency syndromes: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab. 2010;95(6):2536-2559."
    doi: "10.1210/jc.2009-2354"
    pmid: "20525905"
    url: "https://doi.org/10.1210/jc.2009-2354"
  - id: sattler-2004-bone-testosterone
    type: peer-reviewed
    cite: "Sattler FR, Castaneda-Sceppa C, Binder EF, et al. Testosterone and growth hormone improve body composition and muscle performance in older men. J Clin Endocrinol Metab. 2009;94(6):1991-2001."
    doi: "10.1210/jc.2008-2338"
    pmid: "19293261"
    url: "https://doi.org/10.1210/jc.2008-2338"
  - id: shores-2004-testosterone-depression
    type: peer-reviewed
    cite: "Shores MM, Kivlahan DR, Sadak TI, Li EJ, Matsumoto AM. A randomized, double-blind, placebo-controlled study of testosterone treatment in hypogonadal older men with subthreshold depression (dysthymia or minor depression). J Clin Psychiatry. 2009;70(7):1009-1016."
    doi: "10.4088/JCP.07m03856"
    pmid: "19538904"
    url: "https://doi.org/10.4088/JCP.07m03856"
cross_links:
  - target: 01-human/03-molecular/androgen-receptor
    relation: targets
    note: "Testosterone and DHT bind AR LBD (DHT 3× higher affinity); ligand-AR complex → AREs → spermatogenesis, muscle anabolism, bone density, erythropoiesis; AR amplification and LBD mutations permit CRPC growth at castrate testosterone; 5α-reductase irreversibly converts T to DHT."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "AR and ERα in hypothalamus/limbic cortex mediate testosterone effects on libido, aggression, and mood; aromatization to estradiol required for male brain masculinization; testosterone deficiency → depressive symptoms and cognitive slowing; hippocampal AR regulates BDNF."
  - target: 01-human/07-system/prostate-cancer
    relation: connects-to
    note: "Testosterone fuels AR-driven prostate cancer; ADT (GnRH agonists/antagonists) is first-line for advanced disease; castration resistance arises via AR amplification, AR-V7, and adrenal androgen synthesis; abiraterone (CYP17A1 inhibitor) blocks residual androgens in CRPC."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Male hypogonadism (T <300 ng/dL) predicts MDD risk; testosterone deficiency causes fatigue, anhedonia, and low libido indistinguishable from MDD; TRT has adjunctive antidepressant efficacy in hypogonadal men; SSRI-treated men with residual anhedonia benefit from TRT augmentation."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Male hypogonadism (T <300 ng/dL) is a leading cause of secondary male osteoporosis; testosterone maintains BMD via AR on osteoblasts and aromatization to estradiol; ADT causes 2-5% BMD loss/year; denosumab or zoledronate co-administered with ADT prevents fractures."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Visceral adiposity suppresses testosterone via aromatase upregulation and SHBG reduction; hypogonadal-obesity cycle: T deficiency worsens adiposity, which further suppresses T; 5-10% weight loss raises testosterone 2-3 nmol/L without TRT; TRT reduces fat mass ~3 kg."
---

# Testosterone

## Overview

**Testosterone** is the principal male androgen — a **C19 steroid hormone** synthesized primarily by **testicular Leydig cells** (~95% of circulating testosterone) and, to a minor extent, by adrenal zona reticularis and ovarian theca cells in females. It is the biological effector of the **hypothalamic-pituitary-gonadal (HPG) axis**: hypothalamic GnRH → anterior pituitary LH → Leydig cell CYP17A1 and StAR → testosterone [^bhasin-2010-jcem-testosterone].

Testosterone acts through two principal mechanisms:
1. **Direct AR activation** — testosterone binds the androgen receptor (AR, NR3C4) with moderate affinity and drives spermatogenesis, muscle anabolism, bone density, erythropoiesis, and secondary sex characteristics
2. **5α-reduction to DHT** — 5α-reductase (SRD5A1/SRD5A2) converts testosterone to **dihydrotestosterone (DHT)**, which binds AR with 3× higher affinity and lower dissociation rate; DHT mediates prostate growth, male pattern baldness, and external genital virilization
3. **Aromatization to estradiol (E2)** — aromatase (CYP19A1) converts testosterone to **17β-estradiol** in adipose, liver, bone, and brain; estradiol is essential for male bone mass, libido, and brain masculinization

**Normal physiology in males:**
- Morning serum total testosterone: **300–1000 ng/dL** (10.4–34.7 nmol/L); declines 1-2% per year after age 30 (age-related hypogonadism, "late-onset hypogonadism")
- **Pulsatile secretion** driven by LH pulses every 60-90 min; diurnal variation with peak at 8:00 AM and trough in the evening (~25% difference)
- **Transport:** ~44% bound to sex hormone-binding globulin (SHBG, high affinity), ~54% bound to albumin (low affinity), ~2% free; bioavailable testosterone = free + albumin-bound
- **Half-life:** 10-100 minutes (testosterone itself); metabolized by 5α-reductase, 5β-reductase, and aromatase in liver, prostate, skin, and adipose

**Testosterone in females:**
- Normal female serum testosterone: 15–70 ng/dL (~10–15% of male levels)
- Sources: ovarian theca (50%), adrenal (25%), peripheral conversion (25%)
- Required for female libido, bone density, and muscle mass; excess testosterone (PCOS, congenital adrenal hyperplasia) → hirsutism, acne, anovulation

## Structure

### Biosynthetic pathway — steroidogenesis

Testosterone is synthesized from cholesterol via the steroidogenesis cascade:

| Step | Enzyme | Substrate → Product | Location |
|------|--------|---------------------|----------|
| Cholesterol uptake | StAR (steroidogenic acute regulatory protein) | Cholesterol (outer → inner mitochondrial membrane) | Leydig cell mitochondria |
| Pregnenolone synthesis | CYP11A1 (P450scc) | Cholesterol → Pregnenolone | Mitochondria |
| Pregnenolone → Progesterone | HSD3B2 (3β-HSD) | Pregnenolone → Progesterone | ER |
| Androstenedione via Δ4 | CYP17A1 (17α-hydroxylase/lyase) | Progesterone → 17-OH progesterone → Androstenedione | ER |
| Testosterone | HSD17B3 (17β-HSD3) | Androstenedione → Testosterone | ER |
| DHT | SRD5A1/SRD5A2 (5α-reductase) | Testosterone → DHT | Prostate, skin, liver |
| Estradiol | CYP19A1 (Aromatase) | Testosterone → Estradiol | Adipose, bone, brain, ovary |

**Rate-limiting steps:**
- **StAR transport** of cholesterol to the inner mitochondrial membrane is the acute rate-limiting step (stimulated by LH → cAMP → PKA → StAR phosphorylation)
- **CYP17A1** is the critical enzymatic step in androgen synthesis — target of **abiraterone acetate** (irreversible CYP17A1 inhibitor) in prostate cancer

### Molecular structure

Testosterone is a **C19 steroid** (molecular weight 288 Da):
- **A-ring:** Δ4,3-ketone (conjugated enone) — essential for AR binding
- **D-ring:** 17β-hydroxyl group — required for biological activity; 5α-reductase converts 3-keto-Δ4 to 3-keto-5α (DHT) for higher-affinity AR binding
- **Aromatization:** CYP19A1 removes C10-methyl group and aromatizes A-ring → estradiol

## Function

### Physiological actions by tissue

| Tissue | Primary mediator | Key functions |
|--------|----------------|---------------|
| Testis (Sertoli cells) | AR | Spermatogenesis support; Sertoli cell tight junctions (blood-testis barrier) |
| Bone | AR + E2 (aromatized) | Osteoblast function; closure of epiphyseal plates; inhibition of osteoclastogenesis |
| Muscle | AR | Myoblast proliferation and differentiation; protein synthesis; IGF-1 upregulation |
| Prostate | DHT/AR | Prostate growth, secretory function (PSA, KLK3); benign prostatic hyperplasia (BPH) |
| Brain | AR + E2 | Libido, aggression, spatial cognition, mood regulation, neuroprotection |
| Bone marrow | AR + EPO synergy | Erythropoiesis (men have ~1 g/dL higher hemoglobin than women) |
| Skin | DHT/AR | Sebum production; hair follicle miniaturization (male pattern baldness) |
| Cardiovascular | AR | Vasodilation, coronary vasorelaxation; excess testosterone → polycythemia risk |
| Liver | AR | SHBG suppression; reduced HDL synthesis |

### HPG axis regulation

```
Hypothalamus → GnRH (pulsatile, 60-90 min) → Anterior pituitary
  → LH → Leydig cells → Testosterone
  → FSH → Sertoli cells → Inhibin B (feeds back to suppress FSH)

Testosterone negative feedback:
  Testosterone → hypothalamus + pituitary → suppresses GnRH pulses + LH secretion
  E2 (aromatized T) → potent hypothalamic negative feedback (more potent than T itself)
  DHT → pituitary → LH suppression (DHT does not cross-convert to E2)
```

**Clinical implications of feedback:**
- **Exogenous TRT** → suppresses HPG axis → LH↓, FSH↓ → testicular atrophy and azoospermia; fertility requires hCG (LH analogue) co-administration
- **Clomiphene citrate** (SERM) → blocks ER feedback at hypothalamus/pituitary → increased GnRH/LH pulses → endogenous testosterone stimulation
- **ADT** (GnRH agonists/antagonists) → suppresses LH → Leydig cell involution → testosterone < 50 ng/dL (castrate level)

## Mechanism

### AR signaling — genomic pathway

1. **Testosterone (or DHT) diffuses** across plasma membrane into cytoplasm (lipophilic)
2. **Ligand binds AR LBD** → conformational change → release from Hsp90/Hsp70 chaperone complex
3. **AR dimerization** via NTD-to-LBD (N/C) interaction → nuclear translocation via importin-α
4. **AR-DNA binding:** DBD zinc fingers bind androgen response elements (AREs; consensus 5'-TGTTCT-3') as AR homodimers
5. **Coactivator recruitment:** NTD AF-1 domain recruits p300, SRC-1, CBP (histone acetyltransferases) → chromatin remodeling → transcription of AR target genes

**Key AR target genes:**
- **PSA/KLK3** — kallikrein serine protease; clinical biomarker for prostate cancer
- **TMPRSS2** — transmembrane serine protease 2 (also SARS-CoV-2 priming factor); site of ETS gene fusions in prostate cancer
- **NKX3-1** — prostate-specific homeobox transcription factor; tumor suppressor in early PCa
- **FKBP5** — FK506-binding protein; modulates glucocorticoid signaling
- **MYOD1, IGF-1R** — muscle differentiation genes
- **EPAS1, EPO receptor** — erythropoiesis

### Non-genomic testosterone signaling

- **Membrane AR (mAR):** Testosterone rapidly activates MAPK/ERK, PI3K/AKT, and intracellular Ca²⁺ within seconds-minutes (too fast for genomic transcription)
- **Src kinase activation:** AR → Src → EGFR transactivation → MAPK → proliferative signaling (relevant in CRPC)
- **ZIP9 receptor:** Membrane zinc transporter that functions as a testosterone receptor → G-protein signaling
- **Estradiol receptors (ERα, ERβ):** Aromatized testosterone signals via ER in bone, brain, and cardiovascular tissue

## Pathology

| Condition | Mechanism | Key Features | Treatment |
|-----------|-----------|--------------|-----------|
| **Male hypogonadism (primary)** | Leydig cell failure (Klinefelter, orchitis, trauma) | Low T, elevated LH/FSH, infertility, osteoporosis | TRT (gel, IM injection, patch) |
| **Male hypogonadism (secondary)** | HPG axis suppression (pituitary adenoma, opioids, exogenous steroids) | Low T, low/normal LH/FSH | Treat cause; TRT or clomiphene |
| **Late-onset hypogonadism (LOH)** | Age-related Leydig cell decline + SHBG increase | Testosterone 200-350 ng/dL; fatigue, low libido, depression | TRT if symptomatic |
| **Anabolic steroid abuse** | Exogenous androgens suppress HPG axis | Testicular atrophy, azoospermia, polycythemia, hepatotoxicity | Withdrawal; hCG/clomiphene to restore axis |
| **Polycystic ovary syndrome (PCOS)** | LH hypersecretion → ovarian theca hyperandrogenism | Hirsutism, acne, anovulation, insulin resistance | Metformin, anti-androgens, OCPs |
| **Prostate cancer** | Testosterone → AR drives PCa growth | Asymptomatic (early) to bone metastases; PSA elevated | ADT → abiraterone/enzalutamide → chemotherapy |
| **Congenital adrenal hyperplasia (CAH)** | CYP21A2 deficiency → cortisol deficit → ACTH excess → androgen excess | Female virilization, salt wasting (classic); hirsutism (non-classic) | Glucocorticoid replacement ± fludrocortisone |
| **5α-reductase deficiency** | SRD5A2 mutation → testosterone not converted to DHT | 46,XY intersex — female external genitalia at birth, virilize at puberty; prostate is small and does not develop BPH | Supportive; gender-affirming care |

## Connections

- `targets` → **[Androgen Receptor](../androgen-receptor/README.md)** — Testosterone and DHT bind AR LBD (DHT 3× higher affinity); ligand-AR complex → AREs → spermatogenesis, muscle anabolism, bone density, erythropoiesis; AR amplification and LBD mutations permit CRPC growth at castrate testosterone; 5α-reductase irreversibly converts T to DHT.

- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — AR and ERα in hypothalamus/limbic cortex mediate testosterone effects on libido, aggression, and mood; aromatization to estradiol required for male brain masculinization; testosterone deficiency → depressive symptoms and cognitive slowing; hippocampal AR regulates BDNF.

- `connects-to` → **[Prostate Cancer](../../07-system/prostate-cancer/README.md)** — Testosterone fuels AR-driven prostate cancer; ADT (GnRH agonists/antagonists) is first-line for advanced disease; castration resistance arises via AR amplification, AR-V7, and adrenal androgen synthesis; abiraterone (CYP17A1 inhibitor) blocks residual androgens in CRPC.

- `connects-to` → **[Major Depressive Disorder](../../07-system/major-depressive-disorder/README.md)** — Male hypogonadism (T <300 ng/dL) predicts MDD risk; testosterone deficiency causes fatigue, anhedonia, and low libido indistinguishable from MDD; TRT has adjunctive antidepressant efficacy in hypogonadal men; SSRI-treated men with residual anhedonia benefit from TRT augmentation.

- `connects-to` → **[Osteoporosis](../../07-system/osteoporosis/README.md)** — Male hypogonadism (T <300 ng/dL) is a leading cause of secondary male osteoporosis; testosterone maintains BMD via AR on osteoblasts and aromatization to estradiol; ADT causes 2-5% BMD loss/year; denosumab or zoledronate co-administered with ADT prevents fractures.

- `connects-to` → **[Obesity](../../07-system/obesity/README.md)** — Visceral adiposity suppresses testosterone via aromatase upregulation and SHBG reduction; hypogonadal-obesity cycle: T deficiency worsens adiposity, which further suppresses T; 5-10% weight loss raises testosterone 2-3 nmol/L without TRT; TRT reduces fat mass ~3 kg.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

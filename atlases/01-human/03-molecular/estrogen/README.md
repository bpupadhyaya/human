---
schema: human-scale-entry/v1
id: estrogen
name: Estrogen
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "C18 steroid from ovarian granulosa cells via CYP19A1; 17β-estradiol (E2) is the principal form; binds ERα/ERβ → reproductive cyclicity, bone density, serotonin modulation, and neuroprotection; estrogen deficiency causes osteoporosis; ERα drives ~70% of breast cancers."
aliases: ["17β-estradiol", "E2", "estradiol", "oestrogen", "estrone", "estriol", "ERα", "ERβ", "estrogen receptor", "aromatase substrate"]
sources:
  - id: nilsson-2001-estrogen-receptors
    type: peer-reviewed
    cite: "Nilsson S, Mäkelä S, Treuter E, et al. Mechanisms of estrogen action. Physiol Rev. 2001;81(4):1535-1565."
    doi: "10.1152/physrev.2001.81.4.1535"
    pmid: "11581496"
    url: "https://doi.org/10.1152/physrev.2001.81.4.1535"
  - id: gruber-2002-estrogen-menopause
    type: peer-reviewed
    cite: "Gruber CJ, Tschugguel W, Schneeberger C, Huber JC. Production and actions of estrogens. N Engl J Med. 2002;346(5):340-352."
    doi: "10.1056/NEJMra000471"
    pmid: "11807149"
    url: "https://doi.org/10.1056/NEJMra000471"
  - id: soares-2014-estrogen-depression
    type: peer-reviewed
    cite: "Soares CN. Depression and menopause: current knowledge and clinical recommendations for a critical window. Psychiatr Clin North Am. 2017;40(2):239-254."
    doi: "10.1016/j.psc.2017.01.007"
    pmid: "28477651"
    url: "https://doi.org/10.1016/j.psc.2017.01.007"
cross_links:
  - target: 01-human/03-molecular/serotonin
    relation: modulates
    note: "Estrogen upregulates TPH2 and 5-HT1A density in raphe nuclei; estradiol enhances SERT downregulation by SSRIs; estrogen withdrawal at menopause → 5-HT decline → perimenopausal depression; transdermal estradiol has antidepressant efficacy in perimenopausal MDD."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "ERα in hippocampus promotes synaptic plasticity and BDNF; hippocampal aromatase (CYP19A1) produces local estradiol; estrogen deficiency → cognitive decline; estrogen neuroprotection established in animal models but the HRT critical-window hypothesis remains unproven clinically."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "ERα (ESR1) drives ~70-75% of breast cancers; aromatase inhibitors (anastrozole, letrozole) are first-line adjuvant for postmenopausal ER+ disease; fulvestrant (SERD) degrades ERα; ESR1 LBD mutations (D538G, Y537S) cause AI resistance in metastatic HR+ disease."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Estrogen deficiency at menopause → reduced OPG → RANKL excess → osteoclast hyperactivation → 3-5% trabecular bone loss/year; HRT reduces fracture risk ~35%; SERMs (raloxifene) preserve bone without uterine stimulation; bisphosphonates preferred over HRT for fracture prevention."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Perimenopausal estrogen fluctuations trigger or worsen MDD; transdermal estradiol (100 mcg/day patch) has antidepressant efficacy in perimenopausal women; PMDD involves abnormal CNS sensitivity to allopregnanolone (progesterone metabolite) fluctuations, not estrogen deficiency."
  - target: 01-human/07-system/endometrial-cancer
    relation: connects-to
    note: "Unopposed estrogen drives endometrial hyperplasia → EIN → type 1 endometrioid cancer; obesity → adipose aromatase → androgen-to-estrogen conversion → ~3× EC risk at BMI >30; aromatase inhibitors active in ER+ endometrial cancer; combined HRT (with progestogen) prevents EC risk."
---

# Estrogen

## Overview

**Estrogen** refers to a family of **C18 steroid hormones** sharing a phenolic A-ring that confers high-affinity binding to **estrogen receptors (ERα and ERβ)**. The principal circulating estrogen in premenopausal women is **17β-estradiol (E2)**, synthesized by **ovarian granulosa cells** via the aromatase enzyme (CYP19A1) from testosterone. During pregnancy, the placenta is the dominant source (producing estriol, E3). After menopause, the primary estrogen becomes **estrone (E1)**, produced by peripheral aromatization of adrenal androstenedione in adipose tissue [^gruber-2002-estrogen-menopause].

Estrogens act via two mechanisms:
1. **Nuclear receptor signaling (genomic):** ERα/ERβ → chromatin binding at estrogen response elements (EREs; GGTCAnnnTGACC) → transcription of target genes (hours to days)
2. **Membrane-associated signaling (non-genomic):** Membrane ERα/GPER (GPR30) → rapid PKA/MAPK/PI3K activation → vasodilation, neuroprotection, and immune modulation (seconds to minutes)

**Three biologically relevant estrogens:**
- **E1 (Estrone):** Weakest; dominant post-menopause; produced by adipose aromatase from androstenedione; the source of ER+ breast cancer estrogen in postmenopausal women
- **E2 (17β-Estradiol):** Most potent; ovarian granulosa cell product; drives menstrual cycle, secondary sex characteristics, and bone density
- **E3 (Estriol):** Weakest; predominantly placental; lowest carcinogenic potential; used in vaginal creams for local atrophy without systemic effects

**Normal production in females:**
- **Follicular phase:** Rising FSH → granulosa cells → aromatase → E2 synthesis; E2 peaks before LH surge (~200–500 pg/mL peak)
- **Luteal phase:** Corpus luteum → E2 + progesterone; progesterone withdrawal at luteolysis triggers menstruation
- **Postmenopause:** Ovarian estrogen production ceases; serum E2 < 20 pg/mL; peripheral aromatization of adrenal androstenedione to estrone (E1) becomes dominant

**Estrogen in males:**
- Males produce ~30–40 ng/day of E2 from aromatization of testosterone (CYP19A1 in adipose, brain, bone, liver)
- Male E2 is critical for bone density, libido, and brain function — male ERα knockout mice are infertile and obese
- Excess E2 in men (aromatase excess syndrome, obesity): gynecomastia, reduced spermatogenesis

## Structure

### Steroid backbone and receptor binding

Estrogens are **C18 steroids** derived from androgen precursors by the action of **aromatase (CYP19A1)**:

**Aromatase reaction:**
1. Three successive hydroxylations of the C19 methyl group of the androgen A-ring
2. Elimination of the C19 methyl group as formate
3. Aromatization of the A-ring → phenolic group (3-OH) → hallmark of all estrogens
4. Net reaction: Testosterone → Estradiol; Androstenedione → Estrone

**Estrogen receptor structure:**
- **ERα (ESR1, located on chromosome 6q24-27):** 595 aa; dominant in breast, uterus, pituitary, hypothalamus, liver, bone; the primary oncogenic driver in breast/endometrial cancer
- **ERβ (ESR2, chromosome 14q22-24):** 530 aa; dominant in ovary, prostate, lung, GI tract, immune cells, brain; often opposes ERα's proliferative effects; acts as tumor suppressor in some contexts
- **GPER/GPR30:** Membrane G-protein coupled receptor; mediates rapid non-genomic estrogen signaling; expressed in heart, CNS, immune cells; no structural homology to ERα/ERβ

**ER domain architecture:**
| Domain | Function |
|--------|----------|
| A/B (NTD, AF-1) | Ligand-independent transactivation; cofactor binding |
| C (DBD) | Zinc fingers bind ERE palindromes |
| D (Hinge) | Nuclear localization signal; Hsp90 binding |
| E (LBD, AF-2) | Ligand-binding pocket; coactivator (LXXLL motif) binding |
| F (CTD) | Modulates AF-2 activity; SRC-1 interaction |

## Function

### Tissue-specific estrogen actions

| Tissue | Receptor | Key functions |
|--------|----------|---------------|
| Uterus | ERα | Endometrial proliferation; spiral artery development; cervical mucus |
| Breast | ERα | Ductal development; mammary gland proliferation; lactation preparation |
| Bone | ERα + ERβ | Inhibits osteoclastogenesis (via OPG upregulation); closes epiphyseal plates; suppresses RANKL |
| Hypothalamus/pituitary | ERα | Negative feedback on GnRH/LH pulsatility; LH surge (positive feedback mid-cycle at ERα in ARC) |
| Brain | ERα + ERβ | Synaptic plasticity; BDNF; neuroprotection; mood regulation; hippocampal neurogenesis |
| Liver | ERα | SHBG production; coagulation factors; CRP modulation; TG synthesis |
| Cardiovascular | ERα + GPER | Endothelial NO production; vasodilation; anti-atherogenic effects pre-menopause |
| Immune system | ERβ | Anti-inflammatory cytokine regulation; B-cell maturation; modulates autoimmunity |
| Skin | ERα + ERβ | Collagen synthesis; skin thickness; moisture retention |
| Adipose tissue | ERβ | Regulates fat distribution (pre-menopausal: subcutaneous-predominant; post-menopausal: visceral-dominant shift) |

### Menstrual cycle regulation

The menstrual cycle (typically 28 days) is governed by ovarian estrogen and progesterone feedback on the HPG axis:

```
Days 1-13 (Follicular phase):
  FSH → granulosa cell CYP19A1 → E2 ↑
  E2 → endometrial proliferation (glands, stroma)
  E2 → negative feedback on FSH; cervical mucus liquefaction

Day 14 (LH surge → ovulation):
  Rising E2 exceeds threshold → positive feedback → GnRH/LH surge
  Ovulation triggered ~36 hours after LH peak

Days 15-28 (Luteal phase):
  Corpus luteum → E2 + progesterone → endometrial secretory transformation
  If no implantation → corpus luteum luteolysis → E2 + P4 fall → menstruation
  If implantation → hCG from trophoblast → corpus luteum rescue → E2 + P4 maintained
```

## Mechanism

### Genomic signaling pathway

1. **E2 diffuses** across plasma membrane (lipophilic)
2. **E2 binds ERα or ERβ LBD** → conformational change → helix 12 closure over ligand-binding pocket → release from Hsp90 chaperone complex
3. **ER dimerization** (ERα/ERα, ERβ/ERβ, or ERα/ERβ heterodimers) → nuclear translocation via importin-α
4. **ERE binding:** DBD zinc fingers bind palindromic EREs (GGTCAnnnTGACC) in gene promoters; ER also signals via AP-1 and Sp1 sites (tethered signaling, not direct DNA binding)
5. **Coactivator recruitment:** AF-2 surface recruits SRC-1, SRC-2, SRC-3 (p160 family); these recruit p300/CBP (HAT) → histone acetylation → chromatin opening → transcription

**Key ERα target genes:**
- **PR (progesterone receptor)** — upregulated by E2; its expression confirms functional ERα signaling in breast cancer
- **TFF1 (pS2)** — trefoil factor 1; ERE-containing promoter; marker of ERα activity in breast cancer
- **CCND1 (cyclin D1)** — drives cell cycle G1→S; major proliferative effector of E2 in breast
- **BCL2** — anti-apoptotic; upregulated by ERα → ER+ breast cancer survival advantage
- **VEGF** — angiogenesis; upregulated by E2 via ERE and AP-1 in breast and uterine epithelium

### SERD mechanism (fulvestrant)

**Selective estrogen receptor degraders (SERDs)** bind ERα but induce a distinct conformational change that:
- Prevents ER dimerization
- Blocks nuclear localization
- Recruits ubiquitin-proteasome machinery → ERα degradation
- Net effect: complete ER elimination (vs. tamoxifen which blocks ER but leaves receptor intact)

**Oral SERDs:** Elacestrant (Orserdu), camizestrant, giredestrant target ESR1-mutant metastatic breast cancer resistant to aromatase inhibitors.

## Pathology

| Condition | Mechanism | Key Features | Treatment |
|-----------|-----------|--------------|-----------|
| **Menopausal transition** | Ovarian follicle depletion → E2 deficiency | Hot flashes, night sweats, urogenital atrophy, bone loss | HRT (E2 ± progestogen); SERMs; ospemifene for vulvovaginal atrophy |
| **ER+ Breast Cancer** | ERα drives proliferation via cyclin D1, BCL2 | HR+/HER2- most common subtype (40%); treated endocrinologically | Tamoxifen; AIs + CDK4/6i; SERDs (elacestrant for ESR1-mutant) |
| **Endometrial cancer (Type I)** | Unopposed estrogen → endometrial hyperplasia → EIN | Well-differentiated; good prognosis; PTEN, PIK3CA mutations | Surgery; progestins; letrozole in ER+ recurrent |
| **PMDD** | CNS hypersensitivity to allopregnanolone during luteal phase | Severe mood symptoms cyclically; not estrogen per se | SSRIs (continuous or luteal-phase); combined OCP; GnRH agonist |
| **Aromatase deficiency** | CYP19A1 mutations (rare) | Tall stature (open epiphyses), osteoporosis, virilization in females | E2 replacement |
| **Aromatase excess syndrome** | CYP19A1 overexpression (gonadal, tumor) | Gynecomastia (males), feminization; sexual precocity | Aromatase inhibitors |
| **Ovarian hyperstimulation** | Excessive E2 during IVF stimulation | Vascular leak, ascites, thromboembolism | GnRH antagonist trigger; cabergoline |
| **Hormone replacement therapy risks** | Combined HRT (E2+progestogen) → WHI findings | Modest increase in breast cancer risk (~8 extra cases/10,000 women/year); VTE, stroke risk | Individualized risk-benefit; transdermal preferred (lower VTE than oral) |

## Connections

- `modulates` → **[Serotonin](../serotonin/README.md)** — Estrogen upregulates TPH2 and 5-HT1A density in raphe nuclei; estradiol enhances SERT downregulation by SSRIs; estrogen withdrawal at menopause → 5-HT decline → perimenopausal depression; transdermal estradiol has antidepressant efficacy in perimenopausal MDD.

- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — ERα in hippocampus promotes synaptic plasticity and BDNF; hippocampal aromatase (CYP19A1) produces local estradiol; estrogen deficiency → cognitive decline; estrogen neuroprotection established in animal models but the HRT critical-window hypothesis remains unproven clinically.

- `connects-to` → **[Breast Cancer](../../07-system/breast-cancer/README.md)** — ERα (ESR1) drives ~70-75% of breast cancers; aromatase inhibitors (anastrozole, letrozole) are first-line adjuvant for postmenopausal ER+ disease; fulvestrant (SERD) degrades ERα; ESR1 LBD mutations (D538G, Y537S) cause AI resistance in metastatic HR+ disease.

- `connects-to` → **[Osteoporosis](../../07-system/osteoporosis/README.md)** — Estrogen deficiency at menopause → reduced OPG → RANKL excess → osteoclast hyperactivation → 3-5% trabecular bone loss/year; HRT reduces fracture risk ~35%; SERMs (raloxifene) preserve bone without uterine stimulation; bisphosphonates preferred over HRT for fracture prevention.

- `connects-to` → **[Major Depressive Disorder](../../07-system/major-depressive-disorder/README.md)** — Perimenopausal estrogen fluctuations trigger or worsen MDD; transdermal estradiol (100 mcg/day patch) has antidepressant efficacy in perimenopausal women; PMDD involves abnormal CNS sensitivity to allopregnanolone (progesterone metabolite) fluctuations, not estrogen deficiency.

- `connects-to` → **[Endometrial Cancer](../../07-system/endometrial-cancer/README.md)** — Unopposed estrogen drives endometrial hyperplasia → EIN → type 1 endometrioid cancer; obesity → adipose aromatase → androgen-to-estrogen conversion → ~3× EC risk at BMI >30; aromatase inhibitors active in ER+ endometrial cancer; combined HRT (with progestogen) prevents EC risk.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

---
schema: human-scale-entry/v1
id: progesterone
name: Progesterone
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "C21 progestogen secreted by corpus luteum via CYP11A1/3β-HSD; prepares endometrium for implantation and maintains pregnancy; metabolized to allopregnanolone (GABA-A PAM); PR antagonism by mifepristone induces abortion; deficiency causes luteal phase dysfunction."
aliases: ["P4", "progesterone", "progestogen", "progestin", "allopregnanolone", "THPROG", "PR", "progesterone receptor", "corpus luteum hormone", "luteal hormone"]
sources:
  - id: lydon-1995-progesterone-receptor
    type: peer-reviewed
    cite: "Lydon JP, DeMayo FJ, Funk CR, et al. Mice lacking progesterone receptor exhibit pleiotropic reproductive abnormalities. Genes Dev. 1995;9(18):2266-2278."
    doi: "10.1101/gad.9.18.2266"
    pmid: "7557380"
    url: "https://doi.org/10.1101/gad.9.18.2266"
  - id: meltzer-brody-2018-brexanolone
    type: peer-reviewed
    cite: "Meltzer-Brody S, Colquhoun H, Riesenberg R, et al. Brexanolone injection in post-partum depression: two multicentre, double-blind, randomised, placebo-controlled, phase 3 trials. Lancet. 2018;392(10152):1058-1070."
    doi: "10.1016/S0140-6736(18)31551-4"
    pmid: "30177236"
    url: "https://doi.org/10.1016/S0140-6736(18)31551-4"
  - id: schindler-2004-progestogens
    type: peer-reviewed
    cite: "Schindler AE, Campagnoli C, Druckmann R, et al. Classification and pharmacology of progestins. Maturitas. 2003;46 Suppl 1:S7-16."
    doi: "10.1016/j.maturitas.2003.09.014"
    pmid: "14670641"
    url: "https://doi.org/10.1016/j.maturitas.2003.09.014"
cross_links:
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Progesterone and estrogen exert opposing effects on the endometrium: estrogen drives proliferation, progesterone drives secretory transformation; unopposed estrogen without progesterone → endometrial hyperplasia → EC risk; combined HRT (E2+P4) reduces EC risk to near baseline."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "Progesterone metabolizes to allopregnanolone (GABA-A PAM); luteal phase allopregnanolone fluctuations → GABA sensitivity changes; brexanolone (synthetic allopregnanolone) IV is FDA-approved for postpartum depression; GABA-A delta subunit receptors are particularly sensitive."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Luteal allopregnanolone fluctuations drive PMDD and PPD; declining P4 post-delivery triggers PPD; brexanolone (IV allopregnanolone) and zuranolone (oral) treat PPD; PMDD responds to SSRIs, combined OCP, or GnRH agonist; progesterone withdrawal worsens anxiety."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "PR+ breast cancers have better prognosis than PR- tumors; combined E2+progestogen HRT (WHI) increased breast cancer risk vs. estrogen-only; progestins in combined OCP contribute to VTE risk; PR agonists (megestrol, medroxyprogesterone) treat endometrial hyperplasia and EC."
  - target: 01-human/07-system/endometrial-cancer
    relation: connects-to
    note: "Progesterone drives endometrial secretory transformation opposing estrogen proliferation; mifepristone (PR/GR antagonist) blocks P4 receptor → decidual breakdown → pregnancy termination; progesterone supplementation treats luteal phase deficiency and recurrent miscarriage."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Allopregnanolone (progesterone metabolite) is a potent GABA-A PAM via delta subunit extrasynaptic receptors → sedation, anxiolysis, anticonvulsant; progesterone withdrawal → allopregnanolone decline → GABA-A downregulation → seizure threshold reduction in catamenial epilepsy."
---

# Progesterone

## Overview

**Progesterone (P4)** is the principal endogenous **progestogen** — a C21 steroid hormone synthesized primarily by the **corpus luteum** of the ovary after ovulation, and, during pregnancy, by the **placenta** (from ~week 8 onward, replacing the corpus luteum as the dominant source). Small amounts are produced by the adrenal cortex in both sexes and by testicular Leydig cells in males. Progesterone is also the biosynthetic precursor for all other steroid hormones (glucocorticoids, mineralocorticoids, androgens, and estrogens) [^lydon-1995-progesterone-receptor].

Progesterone acts via two mechanisms:
1. **Nuclear progesterone receptor (PR, NR3C3):** PR-A and PR-B isoforms bind progesterone → genomic transcription of progestogenic target genes regulating endometrial differentiation, breast epithelial quiescence, and myometrial relaxation
2. **Membrane receptor and neurosteroid signaling:** Progesterone and its active metabolite **allopregnanolone (3α,5α-THPROG)** bind GABA-A receptors as positive allosteric modulators (PAMs) → rapid inhibitory CNS effects (anxiolysis, sedation, anticonvulsant activity)

**Progesterone in the menstrual cycle:**
- **Luteal phase (days 15-28):** Corpus luteum secretes P4 → endometrial secretory transformation (glands become tortuous, stromal edema, pinopodes develop) → prepares endometrium for blastocyst implantation
- If no fertilization: corpus luteum involutes → P4 fall → endometrial shedding (menstruation); progesterone withdrawal also reduces GABA-A receptor delta subunit expression → increased CNS excitability
- If fertilization occurs: trophoblast secretes hCG → corpus luteum rescued → P4 maintained through week 8 → placenta takes over P4 production for remainder of pregnancy

**Normal levels:**
- Follicular phase: <1 ng/mL (3.2 nmol/L)
- Mid-luteal peak: 5-20 ng/mL (16-64 nmol/L)
- 1st trimester pregnancy: 10-44 ng/mL
- 3rd trimester: 48-150 ng/mL

**Progesterone in males:**
- Serum P4 < 0.5 ng/mL in males (vs. 10-20 ng/mL in luteal phase females)
- Adrenal precursor to cortisol; Leydig cell intermediate toward testosterone

## Structure

### Progesterone biosynthesis and metabolism

**Biosynthesis (corpus luteum and adrenal):**
1. **Cholesterol → Pregnenolone:** CYP11A1 (P450scc) in inner mitochondrial membrane; rate-limited by StAR transport
2. **Pregnenolone → Progesterone:** 3β-HSD (HSD3B2) converts 3β-OH-Δ5 to 3-keto-Δ4 → progesterone (the first committed steroid product)
3. **Progesterone is the branch-point:** CYP17A1 converts P4 → androgens; CYP21A2 converts P4 → deoxycorticosterone (mineralocorticoid precursor); CYP11B1 → cortisol

**Active metabolites:**
- **Allopregnanolone (3α,5α-THPROG):** 5α-reductase → 5α-dihydroprogesterone → 3α-HSD → allopregnanolone; highly CNS-active GABA-A PAM; serum levels parallel P4 (peak mid-luteal); synthesized de novo in CNS astrocytes and neurons
- **Pregnanediol:** Major inactive urinary metabolite (glucuronide); used historically to confirm corpus luteum function
- **Allopregnane-3α-ol-20-one (same as allopregnanolone):** The neurosteroid responsible for progesterone's anxiolytic and anticonvulsant CNS effects

**Synthetic progestins (not identical to natural progesterone):**

| Class | Examples | Properties |
|-------|----------|-----------|
| 19-Nortestosterone derivatives | Norethindrone, levonorgestrel, desogestrel | Moderate androgenicity; some AR activity; used in OCPs |
| Spirolactone derivatives | Drospirenone | Anti-androgenic, anti-mineralocorticoid; used in OCPs for PCOS/PMDD |
| Retroprogesterone derivatives | Dydrogesterone | Highly PR-selective; minimal anti-androgenic or androgenic effects |
| 17-Hydroxyprogesterone derivatives | Medroxyprogesterone acetate (MPA), megestrol | PR agonism; weak GR activity; used in HRT and cancer treatment |

**Natural micronized progesterone (Prometrium, Utrogestan):** Identical to endogenous P4; converted to allopregnanolone → sedative/anxiolytic; preferred over synthetic progestins in HRT for lower cardiovascular and breast risk profile.

### Progesterone receptor (PR) structure

PR exists as two isoforms transcribed from the same gene (PGR, chromosome 11q22):
- **PR-A (94 kDa):** Lacks the first 164 aa of PR-B's NTD; acts as a transcriptional repressor of PR-B (and of ERα, GR, MR); dominant in fallopian tube and myometrium
- **PR-B (120 kDa):** Full-length; transcriptional activator; dominant in mammary gland and uterus; regulated by estrogen (ERE → PR gene transcription)

**PR domain architecture:** NTD (AF-1) → DBD (C4 zinc fingers → PRE: TGTYCT nnnRGACA) → hinge region (NLS) → LBD (AF-2, Hsp90 binding until ligand)

## Function

### Tissue-specific progesterone actions

| Tissue | Receptor | Key functions |
|--------|----------|---------------|
| Uterus (endometrium) | PR-A, PR-B | Secretory transformation; suppresses ERα → limits estrogen proliferative drive; decidualization |
| Uterus (myometrium) | PR-A | Myometrial relaxation (tocolysis); PR-A withdrawal at term → uterine contractions; synthetic progestins prevent preterm labor |
| Cervix | PR | Cervical mucus thickening → sperm penetration barrier (contraceptive effect) |
| Breast | PR-B | Alveolar morphogenesis; opposes estrogen-driven ductal proliferation; PR+ status indicates intact ER signaling |
| Brain | mPR, nPR, GABA-A δ | Allopregnanolone → anxiolysis, sedation, anticonvulsant; neuroprotection; myelination |
| Hypothalamus | PR | Positive feedback on GnRH/LH surge (synergizes with estrogen); negative feedback in luteal phase |
| Immune system | PR | Anti-inflammatory effects; Th2 polarization; immune tolerance in pregnancy |
| Bone | PR | PR agonism promotes osteoblast differentiation (controversial; less well-defined than estrogen effects) |

### Allopregnanolone as GABA-A PAM

Allopregnanolone acts at a **steroid-binding site** on GABA-A receptors that is distinct from benzodiazepine and barbiturate binding sites:
- At **nanomolar concentrations:** Allosteric potentiation of GABA-evoked Cl⁻ current → increases frequency and duration of GABA-A channel opening → reduced neuronal excitability
- At **micromolar concentrations:** Direct (GABA-independent) activation of GABA-A channels
- **Preferred receptor subtype:** δ-subunit containing receptors (α4β3δ, α6β3δ) located extrasynaptically → tonic inhibition; particularly abundant in dentate gyrus and cerebellar granule cells
- **Neurosteroid sensitivity:** δ-subunit containing receptors are ~100× more sensitive to allopregnanolone than γ2-containing synaptic receptors (targeted by benzodiazepines)

**Clinical application:**
- **Brexanolone (Zulresso, IV, 2019):** Synthetic allopregnanolone for postpartum depression; 60-hour infusion; rapid symptom resolution (within 24-48h); mechanism is direct GABA-A PAM normalizing the allopregnanolone withdrawal state post-delivery
- **Zuranolone (Zurzuvae, oral, 2023):** Oral allopregnanolone analogue (BIIB125); 14-day treatment; FDA approved for MDD and PPD; well-absorbed orally (unlike allopregnanolone itself which has poor bioavailability)
- **Ganaxolone:** Oral neurosteroid (3β-methyl-allopregnanolone) approved for CDKL5-deficiency disorder (CDD) in pediatric epilepsy

## Mechanism

### Genomic PR signaling

1. **Progesterone diffuses** across plasma membrane (lipophilic steroid)
2. **Binds PR LBD** → conformational change → Hsp90/Hsp70 chaperone release → PR homodimerization (PR-A/A, PR-B/B, or PR-A/PR-B heterodimer)
3. **Nuclear translocation** via importin-α → binding to **progesterone response elements (PREs; 5'-TGTYCT nnn RGACA-3')** in gene promoters
4. **Coactivator recruitment:** AF-1 (PR-B NTD) and AF-2 (LBD) recruit SRC-1, SRC-2, p300 → histone acetylation → transcriptional activation

**Key PR target genes:**
- **HAND2 (heart and neural crest derivatives expressed 2):** Suppresses stromal FGFs → limits epithelial proliferation; critical uterine PR output
- **IHHL2, LEFTY2:** Decidualization genes; stromal-to-decidual cell transformation
- **MMP3/9 inhibitors, PAI-1:** Remodeling of extracellular matrix in late luteal phase before menstruation
- **FOXO1:** Decidualization transcription factor; progesterone-regulated in endometrial stromal cells

### PR-A as transcriptional repressor

PR-A acts as a dominant negative regulator of PR-B by competing for coactivator binding (SRC-1) and by recruiting NCoR/SMRT corepressors. PR-A also suppresses:
- **ERα signaling** → limits estrogen-driven endometrial proliferation in the luteal phase
- **GR signaling** → modulates glucocorticoid immune responses during pregnancy
- **AR signaling** → in breast epithelium

### Non-genomic membrane progesterone receptor signaling

- **mPRα (PAQR7):** G-protein coupled membrane receptor → Gi/Go → ↓cAMP → myometrial relaxation; rapid non-transcriptional effects in sperm capacitation and oocyte maturation
- **PGRMC1/2 (progesterone receptor membrane component):** Heme-binding sigma-like receptor; involved in rapid progesterone effects on cell survival, lipid transport, and iron homeostasis

## Pathology

| Condition | Mechanism | Key Features | Treatment |
|-----------|-----------|--------------|-----------|
| **Luteal phase deficiency** | Insufficient corpus luteum P4 production | Short luteal phase; recurrent implantation failure; miscarriage | Progesterone supplementation (vaginal, IM) |
| **Premenstrual dysphoric disorder (PMDD)** | CNS hypersensitivity to normal allopregnanolone fluctuations (not P4 deficiency) | Severe mood symptoms, irritability, dysphoria cyclically (days -7 to -1 of cycle) | SSRIs (continuous or luteal-phase); combined OCP; GnRH agonist; zuranolone |
| **Postpartum depression (PPD)** | Abrupt post-partum P4/allopregnanolone fall → GABA-A withdrawal state | Depressive episode within 4 weeks of delivery; 10-15% of mothers | Brexanolone IV; zuranolone oral; SSRIs |
| **Catamenial epilepsy** | Perimenstrual P4/allopregnanolone decline → GABA-A downregulation → increased seizure susceptibility | Seizure cluster in perimenstrual phase; can be purely catamenial or exacerbated | Progesterone supplementation (luteal phase); ganaxolone; menstrual tracking |
| **Endometrial hyperplasia** | Unopposed estrogen → proliferative endometrium; inadequate P4 | Abnormal uterine bleeding; precursor to type 1 EC | Levonorgestrel IUS; oral progestins (medroxyprogesterone, norethindrone) |
| **Mifepristone-induced abortion** | Mifepristone (PR + GR antagonist) blocks P4 at PR | Decidual breakdown, uterine contractions → expulsion | 200 mg oral mifepristone + misoprostol (prostaglandin); >95% complete abortion <10 weeks |
| **Preterm labor** | P4 withdrawal (functional) → myometrial PR-A dominance → uterine contractions | Cervical shortening; preterm birth risk | Vaginal micronized progesterone or 17-OHPC IM (cerclage is complementary) |

## Connections

- `connects-to` → **[Estrogen](../estrogen/README.md)** — Progesterone and estrogen exert opposing effects on the endometrium: estrogen drives proliferation, progesterone drives secretory transformation; unopposed estrogen without progesterone → endometrial hyperplasia → EC risk; combined HRT (E2+P4) reduces EC risk to near baseline.

- `connects-to` → **[GABA](../gaba/README.md)** — Progesterone metabolizes to allopregnanolone (GABA-A PAM); luteal phase allopregnanolone fluctuations → GABA sensitivity changes; brexanolone (synthetic allopregnanolone) IV is FDA-approved for postpartum depression; GABA-A delta subunit receptors are particularly sensitive.

- `connects-to` → **[Major Depressive Disorder](../../07-system/major-depressive-disorder/README.md)** — Luteal allopregnanolone fluctuations drive PMDD and PPD; declining P4 post-delivery triggers PPD; brexanolone (IV allopregnanolone) and zuranolone (oral) treat PPD; PMDD responds to SSRIs, combined OCP, or GnRH agonist; progesterone withdrawal worsens anxiety.

- `connects-to` → **[Breast Cancer](../../07-system/breast-cancer/README.md)** — PR+ breast cancers have better prognosis than PR- tumors; combined E2+progestogen HRT (WHI) increased breast cancer risk vs. estrogen-only; progestins in combined OCP contribute to VTE risk; PR agonists (megestrol, medroxyprogesterone) treat endometrial hyperplasia and EC.

- `connects-to` → **[Endometrial Cancer](../../07-system/endometrial-cancer/README.md)** — Progesterone drives endometrial secretory transformation opposing estrogen proliferation; mifepristone (PR/GR antagonist) blocks P4 receptor → decidual breakdown → pregnancy termination; progesterone supplementation treats luteal phase deficiency and recurrent miscarriage.

- `connects-to` → **[Epilepsy](../../07-system/epilepsy/README.md)** — Allopregnanolone (progesterone metabolite) is a potent GABA-A PAM via delta subunit extrasynaptic receptors → sedation, anxiolysis, anticonvulsant; progesterone withdrawal → allopregnanolone decline → GABA-A downregulation → seizure threshold reduction in catamenial epilepsy.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

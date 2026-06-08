---
schema: human-scale-entry/v1
id: il-36
name: IL-36
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "IL-36 cytokines (IL-36α/β/γ, chr2q12) signal via IL-36R/IL-1RAcP → NF-κB; IL-36Ra antagonist limits signaling. IL36RN loss-of-function drives generalized pustular psoriasis (GPP); spesolimab (anti-IL-36R; FDA 2022) targets GPP. Amplifies IL-17/IL-23 axis in skin and entheses."
aliases: ["IL-36 alpha", "IL-36 beta", "IL-36 gamma", "IL-36Ra", "IL1F6", "IL1F8", "IL1F9", "IL36RN"]
sources:
  - id: marrakchi-2011-il36rn-gpp
    type: peer-reviewed
    cite: "Marrakchi S, Guigue P, Renshaw BR, et al. Interleukin-36-receptor antagonist deficiency and generalized pustular psoriasis. N Engl J Med. 2011;365(7):620-628."
    doi: "10.1056/NEJMoa1013068"
    pmid: "21848462"
  - id: bachelez-2021-spesolimab-effisayil1
    type: peer-reviewed
    cite: "Bachelez H, Choon SE, Marrakchi S, et al. Spesolimab for generalized pustular psoriasis. N Engl J Med. 2021;385(26):2431-2440."
    doi: "10.1056/NEJMoa2103927"
    pmid: "34941024"
  - id: gresnigt-2013-il36-review
    type: peer-reviewed
    cite: "Gresnigt MS, van de Veerdonk FL. Biology of IL-36 cytokines and their role in disease. Semin Immunol. 2013;25(6):458-465."
    doi: "10.1016/j.smim.2013.11.003"
    pmid: "24289416"
  - id: ritchlin-2017-psa-review
    type: peer-reviewed
    cite: "Ritchlin CT, Colbert RA, Gladman DD. Psoriatic arthritis. N Engl J Med. 2017;376(10):957-970."
    doi: "10.1056/NEJMra1505557"
    pmid: "28273019"
cross_links:
  - target: 01-human/07-system/psoriatic-arthritis
    relation: connects-to
    note: "IL-36α/β/γ overexpressed in PsA skin lesions and synovium → NF-κB → IL-6/CXCL8/CCL20 → neutrophil and DC recruitment at entheses; IL36RN mutations link GPP to PsA; spesolimab (anti-IL-36R; FDA 2022) under investigation in PsA."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-36 and IL-17A form an amplification loop in psoriatic skin: IL-17A induces keratinocyte IL-36 release → IL-36 drives CXCL1/8 and antimicrobials → neutrophil/T-cell recruitment; both converge on NF-κB/MAPK; disrupted by anti-IL-17A biologics."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "IL-23 drives IL-17A which induces keratinocyte IL-36 release; IL-36 stimulates DC IL-23 production → feedforward loop in psoriasis/PsA; IL-23 inhibition (guselkumab, risankizumab) reduces both the Th17 and IL-36 inflammatory axes."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF-α synergizes with IL-36 in keratinocyte and synoviocyte NF-κB activation; anti-TNF therapy reduces IL-36 expression in psoriatic skin, demonstrating cross-talk; co-stimulation by TNF-α + IL-36 amplifies CXCL8 and CCL20 beyond either alone."
  - target: 01-human/03-molecular/nf-kb
    relation: modulates
    note: "IL-36α/β/γ bind IL-36R/IL-1RAcP → MyD88 → IRAK4 → TRAF6 → TAK1 → NF-κB p65 nuclear translocation and IKK → IκBα phosphorylation; downstream: IL-6, CXCL1/8, CCL20, S100A proteins, defensins — neutrophil attractants in pustular psoriasis."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "IL-36α/β/γ are predominantly expressed by keratinocytes; skin-restricted over-signaling due to IL36RN loss-of-function → GPP flares with lakes of neutrophils; spesolimab (anti-IL-36R) restores homeostatic IL-36Ra/IL-36 balance in affected skin."
  - target: 01-human/07-system/ankylosing-spondylitis
    relation: connects-to
    note: "IL-36 is detected at entheses in SpA; IL-36 and IL-17A/IL-23 share NF-κB activation; gut dysbiosis in SpA may drive intestinal epithelial IL-36 release, linking gut inflammation to axial and peripheral joint disease in spondyloarthropathies."
---

# IL-36

## Overview

IL-36 cytokines are a subset of the IL-1 superfamily comprising three agonists — **IL-36α** (IL-1F6), **IL-36β** (IL-1F8), and **IL-36γ** (IL-1F9) — and one antagonist, **IL-36Ra** (IL-1F5, encoded by *IL36RN*) [^gresnigt-2013-il36-review]. All four are encoded on chromosome 2q12 in a gene cluster alongside *IL-1A*, *IL-1B*, and *IL-1Ra*. Unlike IL-1β, IL-36 cytokines are constitutively expressed in epithelial and barrier tissues — especially keratinocytes, bronchial epithelium, and intestinal epithelium — where they serve as sentinels of innate danger.

IL-36 gained clinical significance from the discovery that loss-of-function mutations in *IL36RN* cause **generalized pustular psoriasis (GPP)**, a rare but life-threatening neutrophilic skin disorder [^marrakchi-2011-il36rn-gpp]. This established IL-36 as a druggable skin immunology target, leading to **spesolimab** (anti-IL-36R), the first approved therapy for GPP [^bachelez-2021-spesolimab-effisayil1].

## Structure

### Gene Organization

| Gene | Protein | Chromosome | MW | Function |
|:-----|:--------|:-----------|:---|:---------|
| *IL36A* | IL-36α | 2q12 | ~17 kDa | Pro-inflammatory agonist |
| *IL36B* | IL-36β | 2q12 | ~18 kDa | Pro-inflammatory agonist (weakest) |
| *IL36G* | IL-36γ | 2q12 | ~17 kDa | Pro-inflammatory agonist (most potent) |
| *IL36RN* | IL-36Ra | 2q12 | ~17 kDa | Competitive antagonist at IL-36R |

### Receptor Complex

IL-36 signals through a heterodimeric receptor: **IL-36R** (IL1RL2) paired with the shared co-receptor **IL-1RAcP** (IL-1 receptor accessory protein). IL-36Ra competitively occupies the orthosteric binding site on IL-36R without recruiting IL-1RAcP, preventing signaling. The ratio of IL-36Ra to IL-36 agonists determines net signaling output — a steep dose-response that amplifies small perturbations.

### Activation by Proteolysis

Unlike IL-1β which requires caspase-1 cleavage for secretion, IL-36 cytokines are released as full-length propeptides from damaged keratinocytes. Extracellular **neutrophil elastase**, **cathepsin G**, and **proteinase 3** cleave N-terminal prodomains to generate the fully active forms (~3-10 fold increase in potency). This creates a neutrophil-IL-36 positive-feedback loop: IL-36 recruits neutrophils → neutrophil serine proteases activate more IL-36.

## Function

### Downstream Signaling (IL-36R → NF-κB/MAPK)

IL-36R/IL-1RAcP complex → **MyD88** recruitment → **IRAK4** → **TRAF6** → **TAK1** bifurcation:
1. **NF-κB arm**: IKKβ → IκBα phosphorylation and degradation → p65/p50 nuclear translocation → IL-6, IL-8 (CXCL8), CCL20, TNF-α, S100A8/9 transcription
2. **MAPK arm**: ERK1/2, p38, JNK activation → AP-1 → antimicrobial peptides (β-defensins, cathelicidins), CXCL1

### Key Biological Outputs

| Downstream product | Cell source | Role in skin inflammation |
|:------------------|:------------|:--------------------------|
| CXCL1, CXCL8 | Keratinocytes | Neutrophil chemotaxis |
| CCL20 | Keratinocytes | Recruitment of CCR6⁺ Th17 and DCs |
| IL-6 | Keratinocytes, DCs | Systemic acute phase; promotes Th17 differentiation |
| S100A8/9 | Keratinocytes | DAMPs; amplify innate signaling |
| β-defensins | Keratinocytes | Antimicrobial; TLR4 adjuvant activity |
| IL-23 | Myeloid DCs (stimulated by IL-36) | Th17 maintenance → IL-17A → more IL-36 |

### The IL-36 ↔ IL-17A Amplification Loop

IL-17A induces keratinocyte *IL36G* expression; IL-36γ then drives CXCL8 and CCL20 → recruits CLA⁺ Th17 cells back to skin, which produce more IL-17A. This feedforward loop is a major mechanism of chronic plaque psoriasis and its explosive manifestation in GPP [^gresnigt-2013-il36-review].

## Mechanism

### Generalized Pustular Psoriasis — IL36RN Loss-of-Function

*IL36RN* encodes IL-36Ra. Homozygous or compound heterozygous loss-of-function mutations (most common: p.Leu27Pro, p.Ser113Leu) eliminate the competitive antagonist → unrestrained IL-36 signaling → massive keratinocyte activation → CXCL8/CCL20 surge → lakes of neutrophils under the stratum corneum [^marrakchi-2011-il36rn-gpp].

GPP is clinically distinct from plaque psoriasis:
- Widespread erythema with **macropustules** that coalesce
- Systemic features: fever, leukocytosis, elevated CRP — can be fatal
- Triggers: pregnancy, systemic steroid withdrawal, infections
- Genetics: *IL36RN* (most common), *CARD14* GOF, *AP1S3* mutations also cause GPP

### Therapeutic Targeting — Spesolimab

**Spesolimab** (Spevigo; Boehringer Ingelheim) is a humanized anti-IL-36R IgG1 mAb that blocks binding of all three IL-36 agonists. The **EFFISAYIL-1** phase 2 trial (N=53) demonstrated:
- **GPPGA score of 0 or 1** (clear/almost clear skin) at week 1: **54% vs 6%** (placebo) [^bachelez-2021-spesolimab-effisayil1]
- FDA accelerated approval: **September 2022** for GPP
- Ongoing EFFISAYIL-2 (maintenance dosing for flare prevention)

Spesolimab is administered IV 900 mg × 1 during acute GPP flare, then 300 mg SC q4w for maintenance.

### IL-36 in Psoriatic Arthritis

IL-36γ protein and mRNA are elevated in PsA synovial tissue compared with OA controls. Synovial DCs and macrophages — primed by IL-36 — produce IL-23, which sustains the local Th17 response driving enthesitis and synovitis. Elevated IL-36γ in PsA synovial fluid correlates with disease activity scores [^ritchlin-2017-psa-review].

## Connections

- `connects-to` → **[Psoriatic Arthritis](../../07-system/psoriatic-arthritis/README.md)** — IL-36α/β/γ overexpressed in PsA skin lesions and synovium → NF-κB → IL-6/CXCL8/CCL20 → neutrophil and DC recruitment at entheses; IL36RN mutations link GPP to PsA; spesolimab under investigation in PsA.
- `connects-to` → **[IL-17A](../il-17a/README.md)** — IL-36 and IL-17A form an amplification loop in psoriatic skin: IL-17A induces keratinocyte IL-36 release → IL-36 drives CXCL1/8 and antimicrobials → neutrophil/T-cell recruitment; disrupted by anti-IL-17A biologics.
- `connects-to` → **[IL-23](../il-23/README.md)** — IL-23 drives IL-17A which induces keratinocyte IL-36 release; IL-36 stimulates DC IL-23 production → feedforward loop in psoriasis/PsA; IL-23 inhibition (guselkumab, risankizumab) blunts both axes.
- `connects-to` → **[TNF-α](../tnf-alpha/README.md)** — TNF-α synergizes with IL-36 in keratinocyte NF-κB activation; anti-TNF therapy reduces IL-36 expression in psoriatic skin; co-stimulation amplifies CXCL8 and CCL20.
- **Modulates** → **[NF-κB](../nf-kb/README.md)** — IL-36R/IL-1RAcP → MyD88 → IRAK4 → TRAF6 → TAK1 → NF-κB p65; downstream: IL-6, CXCL8, CCL20, S100A proteins — neutrophil attractants in pustular psoriasis.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — IL-36α/β/γ predominantly expressed by keratinocytes; IL36RN loss-of-function → GPP with lakes of neutrophils; spesolimab restores homeostatic IL-36Ra/IL-36 balance.
- `connects-to` → **[Ankylosing Spondylitis](../../07-system/ankylosing-spondylitis/README.md)** — IL-36 detected at entheses in SpA; IL-36/IL-17A/IL-23 share NF-κB activation; gut dysbiosis drives intestinal epithelial IL-36 release, linking gut to axial/peripheral joint disease.

[^marrakchi-2011-il36rn-gpp]: Marrakchi S, et al. Interleukin-36-receptor antagonist deficiency and generalized pustular psoriasis. *N Engl J Med.* 2011;365(7):620-628. [doi:10.1056/NEJMoa1013068](https://doi.org/10.1056/NEJMoa1013068) · [PubMed 21848462](https://pubmed.ncbi.nlm.nih.gov/21848462/)
[^bachelez-2021-spesolimab-effisayil1]: Bachelez H, et al. Spesolimab for generalized pustular psoriasis. *N Engl J Med.* 2021;385(26):2431-2440. [doi:10.1056/NEJMoa2103927](https://doi.org/10.1056/NEJMoa2103927) · [PubMed 34941024](https://pubmed.ncbi.nlm.nih.gov/34941024/)
[^gresnigt-2013-il36-review]: Gresnigt MS, van de Veerdonk FL. Biology of IL-36 cytokines and their role in disease. *Semin Immunol.* 2013;25(6):458-465. [doi:10.1016/j.smim.2013.11.003](https://doi.org/10.1016/j.smim.2013.11.003) · [PubMed 24289416](https://pubmed.ncbi.nlm.nih.gov/24289416/)
[^ritchlin-2017-psa-review]: Ritchlin CT, Colbert RA, Gladman DD. Psoriatic arthritis. *N Engl J Med.* 2017;376(10):957-970. [doi:10.1056/NEJMra1505557](https://doi.org/10.1056/NEJMra1505557) · [PubMed 28273019](https://pubmed.ncbi.nlm.nih.gov/28273019/)

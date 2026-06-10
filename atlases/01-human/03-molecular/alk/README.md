---
schema: human-scale-entry/v1
id: alk
name: ALK
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Receptor tyrosine kinase; EML4-ALK fusions in ~3-5% of NSCLC drive constitutive ALK signaling → RAS-MAPK and PI3K-AKT; NPM-ALK defines ALK+ anaplastic large cell lymphoma; crizotinib, alectinib, brigatinib, and lorlatinib are ALK inhibitors with improving CNS penetration."
aliases: ["ALK", "anaplastic lymphoma kinase", "EML4-ALK", "NPM-ALK", "ALK fusion", "ALK rearrangement", "ALK+ NSCLC", "CD246"]
sources:
  - id: shaw-2013-crizotinib
    type: peer-reviewed
    cite: "Shaw AT, Kim DW, Nakagawa K, et al. Crizotinib versus chemotherapy in advanced ALK-positive lung cancer. N Engl J Med. 2013;368(25):2385-2394."
    doi: "10.1056/NEJMoa1214886"
    pmid: "23724913"
    url: "https://doi.org/10.1056/NEJMoa1214886"
  - id: peters-2017-alectinib
    type: peer-reviewed
    cite: "Peters S, Camidge DR, Shaw AT, et al. Alectinib versus crizotinib in untreated ALK-positive non-small-cell lung cancer. N Engl J Med. 2017;377(9):829-838."
    doi: "10.1056/NEJMoa1704795"
    pmid: "28586279"
    url: "https://doi.org/10.1056/NEJMoa1704795"
cross_links:
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "ALK → GRB2 → SOS → RAS-MEK-ERK → proliferation; KRAS co-mutations are rare in ALK+ NSCLC (mutually exclusive with ALK fusions); ERK reactivation (via KRAS amplification) is a resistance mechanism to ALK TKIs; combined ALK + MEK inhibition under study for ALK TKI-resistant NSCLC."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "NPM-ALK fusion in ALCL directly phosphorylates STAT3 → BCL-XL, MYC, survivin → T-cell lymphoma growth and immune evasion; STAT3 is more prominently activated in ALK+ ALCL than in ALK+ NSCLC; JAK inhibitors (ruxolitinib) studied in STAT3-driven ALCL."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "ALK → PI3K-AKT → mTOR → S6K and 4EBP1 → ribosome biogenesis; mTOR activation is a major ALK effector in NSCLC; mTOR inhibition synergizes with ALK TKIs in preclinical models; PI3K-AKT-mTOR pathway is activated as a bypass mechanism during ALK TKI resistance."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "ALK and EGFR fusions are mutually exclusive in NSCLC; EGFR pathway reactivation (via SOS1, ERBB3) mediates resistance to ALK TKIs; alectinib + erlotinib studied in ALK+ NSCLC; combined EGFR+ALK targeting investigated in rare EGFR-co-mutated ALK+ cases."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "EML4-ALK fusions in ~3-5% of lung adenocarcinoma; enriched in never-smokers; mutually exclusive with KRAS/EGFR mutations; sequential TKI therapy (alectinib → lorlatinib on progression) achieves median OS >7 years, transforming ALK+ NSCLC into a chronic manageable disease."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "ALK+ NSCLC has high propensity for brain metastases (~50% on crizotinib within 1-2 years); lorlatinib achieves 72% intracranial ORR (highest CNS penetrance); CNS progression is the primary failure mode of 1st/2nd-gen ALK TKIs; brain-penetrant TKI selection is critical."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "ALK fusions activate PI3K via p85 binding → PIP3 → AKT → mTOR; PI3K-AKT-mTOR is the most common bypass pathway for acquired ALK TKI resistance; PIK3CA co-mutations occasionally co-occur in ALK+ NSCLC; combined ALK+PI3K inhibition is under preclinical investigation."
---

# ALK

## Overview

**ALK (anaplastic lymphoma kinase, CD246)** is a receptor tyrosine kinase normally expressed primarily in the developing nervous system (where it promotes neuronal differentiation and survival via MIDKINE and pleiotrophin ligands in the mouse; the physiological ligand in humans remains under study). In cancer, ALK is activated primarily through **chromosomal rearrangements** that fuse the ALK kinase domain to partner genes encoding dimerization domains — creating constitutively active fusion oncoproteins that signal in the cytoplasm [^shaw-2013-crizotinib].

**ALK in cancer:**
- **ALK+ non-small cell lung cancer (NSCLC):** EML4-ALK fusion (echinoderm microtubule-associated protein-like 4 — ALK) from inv(2p) — by far the most common in NSCLC (~3-5% of lung adenocarcinoma); enriched in never-smokers, younger patients; exclusive with KRAS/EGFR mutations; defining ALK inhibitor-targetable driver; alectinib (ALEX trial) → 5-year PFS 43%; median OS >7 years with sequential TKI therapy
- **ALK+ anaplastic large cell lymphoma (ALCL):** NPM-ALK (nucleophosmin-ALK, t(2;5)) in ~70-80% of ALK+ ALCL; CD30+ T-cell lymphoma; excellent prognosis (5-year OS ~80% with CHOP-based therapy + brentuximab vedotin); also treated with ALK inhibitors at relapse
- **Neuroblastoma:** ALK point mutations (F1174L, R1275Q) — gain-of-function — in ~8-10% of neuroblastoma (especially high-risk); crizotinib/ceritinib/lorlatinib active in ALK-mutant neuroblastoma; ALK germline mutations in familial neuroblastoma
- **Inflammatory myofibroblastic tumor (IMT):** ALK fusions (multiple partners) in ~50-60%; alectinib and crizotinib active; basket trial approvals

**ALK vs. other lung cancer drivers:**
| Driver | Frequency | First-line TKI | 5-yr OS |
|--------|-----------|----------------|---------|
| EGFR mutation | ~15% (US) | Osimertinib | ~65% |
| ALK fusion | ~3-5% | Alectinib/lorlatinib | >70% |
| ROS1 fusion | ~1-2% | Entrectinib/crizotinib | ~60% |
| RET fusion | ~1-2% | Selpercatinib | ~70% |
| METex14 | ~3-4% | Capmatinib/tepotinib | ~50% |

## Structure

### ALK protein architecture

ALK is a 1,620-amino-acid, 200 kDa single-pass transmembrane RTK:

**Extracellular domain (ECD, 1-1037):**
- Signal peptide (1-26) → N-terminal MAM domain (meprin/A5/mu) + LDL-A (low-density lipoprotein-A) domain + MAM domain (ECD structural core)
- Glycine-rich region (GRD, 264-421): Heparan sulfate proteoglycan binding → restrains ALK in the ECM; also site for MIDKINE/pleiotrophin (putative ligands) binding
- Normal ALK is monomeric in the absence of ligand; ligand binding induces homodimerization → kinase activation

**Transmembrane domain (TM, 1038-1059):** Single pass

**Intracellular kinase domain (1060-1620):**
- Juxtamembrane domain → regulatory
- Kinase domain: Y1282/Y1283 — primary activation loop phosphorylation sites; Y1604 — autophosphorylation
- **F1174 (activation loop):** Neuroblastoma hotspot F1174L/I — increases kinase affinity; also located at the interface of activation loop and αC-helix — F1174L shifts kinase toward active conformation
- **R1275 (αC helix region):** Neuroblastoma hotspot R1275Q — disrupts the conserved arginine salt bridge → destabilizes inactive conformation → constitutive activation

### ALK fusion oncoproteins

**Mechanism of fusion activation:**
Chromosomal rearrangements fuse a partner gene's 5' sequence (including its promoter and dimerization domain) to the 3' ALK kinase domain → fusion protein:
- Lacks ALK extracellular domain (no ligand dependence)
- Contains partner-derived dimerization domain → constitutive homodimerization → constitutive trans-autophosphorylation → constitutive kinase activity
- Cytoplasmic localization (no TM domain) → cytoplasmic signaling

**Major ALK fusion partners:**

| Fusion | Partner | Gene location | Mechanism | Cancer |
|--------|---------|---------------|-----------|--------|
| EML4-ALK (variant 1: E13;A20) | EML4 | inv(2p21;p23) | EML4 HELP/EMS dimerization | NSCLC |
| EML4-ALK (variant 3: E6;A20) | EML4 | inv(2p21;p23) | Same | NSCLC |
| NPM-ALK | NPM1 | t(2;5)(p23;q35) | NPM oligomerization | ALCL |
| RANBP2-ALK | RANBP2 | inv(2)(p23;q13) | RANBP2 coiled-coil | IMT |
| TFG-ALK | TFG | t(2;3)(p23;q12) | TFG coiled-coil | IMT, ALCL |

**EML4-ALK variants in NSCLC:**
- Variant 1 (E13;A20): 33% of EML4-ALK; sensitive to all ALK TKIs
- Variant 3 (E6;A20): 29%; higher risk of resistance and brain metastasis; associated with shorter lorlatinib PFS in some analyses
- Variants 2, 5, 7: Less common

## Function

### Normal ALK signaling

Normal ALK (without dimerization) is autoinhibited in the absence of ligand. When activated by midkine/pleiotrophin:
- ALK homodimerization → trans-phosphorylation at Y1282/Y1283 → SHC/IRS-1/GRB2 → RAS-ERK1/2 → neuronal differentiation
- PI3K-AKT → neuronal survival (anti-apoptotic)
- STAT3 → JAK-independent STAT3 activation in embryonic neuroblasts

**Physiological roles:**
- Required for early embryonic neurogenesis (mouse data); postnatal ALK expression is mostly restricted to CNS
- Loss of normal ALK → neurological phenotypes in mouse models (learning/memory deficits, anxiety)

### ALK fusion signaling in cancer

EML4-ALK activates multiple oncogenic pathways simultaneously:
1. **RAS-MEK-ERK:** GRB2-SOS → KRAS/NRAS → MEK1/2 → ERK → proliferation and survival
2. **PI3K-AKT-mTOR:** Y1604-PI3K interaction → AKT → mTOR → ribosome biogenesis, anti-apoptosis
3. **STAT3 (via JAK-independent route):** ALK directly phosphorylates STAT3 at Y705 → STAT3 homodimerization → BCL-XL, MYC, cyclin D1
4. **PLCγ:** → IP3 → Ca²⁺ → PKC → cell migration
5. **SRC family kinases:** HCK/LYN activation in ALCL

## Mechanism

### ALK inhibitor generations

**First generation (crizotinib, Xalkori — ATP competitive, MET+ROS1+ALK):** [^shaw-2013-crizotinib]
- PROFILE 1014 trial: PFS 10.9 vs. 7.0 months vs. chemotherapy in 1st-line ALK+ NSCLC
- Limited CNS penetration (P-glycoprotein substrate) → brain metastases emerge in ~50% within 1-2 years
- Resistance: secondary ALK mutations (G1202R, L1196M), ALK bypass (EGFR, KRAS, ERBB3)
- Also approved for ROS1-rearranged NSCLC and METex14-skipping NSCLC

**Second generation (alectinib, Alecensa; brigatinib, Alunbrig; ceritinib, Zykadia):**
- Better CNS penetration; 10-100× more potent than crizotinib vs. ALK
- **Alectinib (ALEX trial):** [^peters-2017-alectinib] PFS 25.7 vs. 10.4 months vs. crizotinib; CNS response rate 86% vs. 45%; 5-year PFS 43%; now standard first-line in many regions
- **Brigatinib (ALTA-1L trial):** PFS 24.0 vs. 11.0 months vs. crizotinib; CNS activity similar to alectinib; first-line option
- Resistance: G1202R (most common, solvent front mutation) → resistant to most 2nd-gen; compound mutations → resistant to 3rd-gen

**Third generation (lorlatinib, Lorbrena — macrocyclic):**
- Most CNS-penetrant; activity against most 1st- and 2nd-gen resistance mutations including G1202R
- **CROWN trial:** Lorlatinib vs. crizotinib first-line → PFS not reached vs. 9.3 months at 3 years; 72% vs. 49% 3-year PFS rate; high intracranial ORR
- FDA approved 2021 for first-line ALK+ NSCLC; most active ALK inhibitor available
- Resistance: compound mutations (G1202R+L1196M, G1202R+G1269A); complete loss of ALK dependency

### ALK in ALCL

**ALK+ ALCL (CD30+/ALK+):**
- Frontline: BV-CHP (brentuximab vedotin + CHP); ECHELON-2 trial → superior PFS vs. CHOP (48.2 vs. 20.8 months); brentuximab vedotin is an ADC targeting CD30 (highly expressed on ALCL)
- ALK inhibitor at relapse: crizotinib active (ORR ~90%); alectinib/lorlatinib also active
- Prognosis: ALK+ ALCL has far better prognosis than ALK- ALCL (5-year OS ~80% vs. ~50%)

**ALK- ALCL:**
- Less responsive to ALK inhibitors
- CD30+ → brentuximab vedotin active; prognosis worse
- DUSP22 rearrangement (gene fusion) in a subset → favorable prognosis
- TP63 rearrangement → very poor prognosis

## Connections

- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — ALK → GRB2 → SOS → RAS-MEK-ERK → proliferation; KRAS co-mutations are rare in ALK+ NSCLC (mutually exclusive with ALK fusions); ERK reactivation (via KRAS amplification) is a resistance mechanism to ALK TKIs; combined ALK + MEK inhibition under study for ALK TKI-resistant NSCLC.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — NPM-ALK fusion in ALCL directly phosphorylates STAT3 → BCL-XL, MYC, survivin → T-cell lymphoma growth and immune evasion; STAT3 is more prominently activated in ALK+ ALCL than in ALK+ NSCLC; JAK inhibitors (ruxolitinib) studied in STAT3-driven ALCL.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — ALK → PI3K-AKT → mTOR → S6K and 4EBP1 → ribosome biogenesis; mTOR activation is a major ALK effector in NSCLC; mTOR inhibition synergizes with ALK TKIs in preclinical models; PI3K-AKT-mTOR pathway is activated as a bypass mechanism during ALK TKI resistance.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — ALK and EGFR fusions are mutually exclusive in NSCLC; EGFR pathway reactivation (via SOS1, ERBB3) mediates resistance to ALK TKIs; alectinib + erlotinib studied in ALK+ NSCLC; combined EGFR+ALK targeting investigated in rare EGFR-co-mutated ALK+ cases.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — EML4-ALK fusions in ~3-5% of lung adenocarcinoma; enriched in never-smokers; mutually exclusive with KRAS/EGFR mutations; sequential TKI therapy (alectinib → lorlatinib on progression) achieves median OS >7 years, transforming ALK+ NSCLC into a chronic manageable disease.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — ALK+ NSCLC has high propensity for brain metastases (~50% on crizotinib within 1-2 years); lorlatinib achieves 72% intracranial ORR (highest CNS penetrance); CNS progression is the primary failure mode of 1st/2nd-gen ALK TKIs; brain-penetrant TKI selection is critical.
- `connects-to` → **[PIK3CA](../pik3ca/README.md)** — ALK fusions activate PI3K via p85 binding → PIP3 → AKT → mTOR; PI3K-AKT-mTOR is the most common bypass pathway for acquired ALK TKI resistance; PIK3CA co-mutations occasionally co-occur in ALK+ NSCLC; combined ALK+PI3K inhibition is under preclinical investigation.

[^shaw-2013-crizotinib]: Shaw AT, Kim DW, Nakagawa K, et al. Crizotinib versus chemotherapy in advanced ALK-positive lung cancer. *N Engl J Med.* 2013;368(25):2385-2394. [doi:10.1056/NEJMoa1214886](https://doi.org/10.1056/NEJMoa1214886) · [PubMed 23724913](https://pubmed.ncbi.nlm.nih.gov/23724913/)
[^peters-2017-alectinib]: Peters S, Camidge DR, Shaw AT, et al. Alectinib versus crizotinib in untreated ALK-positive non-small-cell lung cancer. *N Engl J Med.* 2017;377(9):829-838. [doi:10.1056/NEJMoa1704795](https://doi.org/10.1056/NEJMoa1704795) · [PubMed 28586279](https://pubmed.ncbi.nlm.nih.gov/28586279/)

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

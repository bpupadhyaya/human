---
schema: human-scale-entry/v1
id: yap1
name: YAP1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "YAP1 (Yes-Associated Protein 1) is a transcriptional co-activator held cytoplasmic by LATS1/2-mediated Ser127 phosphorylation; NF2/merlin LOF → LATS inactive → nuclear YAP1-TEAD → CTGF/CYR61/survivin target genes; oncogenic in mesothelioma, schwannoma, and KRAS-mutant tumors."
aliases: ["YAP1", "YAP", "Yes-Associated Protein 1", "YAP1 Hippo", "YAP TEAD", "YAP1 NF2", "YAP1 mesothelioma", "YAP1 mechanosensing", "Hippo YAP effector"]
sources:
  - id: zanconato-2016-yap-cancer
    type: peer-reviewed
    cite: "Zanconato F, Cordenonsi M, Piccolo S. YAP/TAZ at the roots of cancer. Cancer Cell. 2016;29(6):783-803."
    doi: "10.1016/j.ccell.2016.05.005"
    pmid: "27300434"
    url: "https://doi.org/10.1016/j.ccell.2016.05.005"
  - id: harvey-2013-hippo-cancer
    type: peer-reviewed
    cite: "Harvey KF, Zhang X, Thomas DM. The Hippo pathway and human cancer. Nat Rev Cancer. 2013;13(4):246-257."
    doi: "10.1038/nrc3458"
    pmid: "23467301"
    url: "https://doi.org/10.1038/nrc3458"
cross_links:
  - target: 01-human/03-molecular/nf2
    relation: connects-to
    note: "NF2/merlin activates the Hippo kinase cascade (MST1/2 → LATS1/2) to phosphorylate YAP1 Ser127 → 14-3-3 binding → cytoplasmic retention; NF2 LOF in schwannoma, meningioma, and mesothelioma → nuclear YAP1/TAZ → TEAD-driven proliferation and CTGF/CYR61 upregulation."
  - target: 01-human/07-system/neurofibromatosis-type-2
    relation: connects-to
    note: "NF2 disease (germline NF2 LOF) → bilateral vestibular schwannomas, meningiomas, ependymomas; nuclear YAP1 is the downstream effector of NF2 LOF → TEAD target genes drive schwannoma/meningioma proliferation; TEAD/YAP inhibitors in NF2-associated tumor trials."
  - target: 01-human/07-system/mesothelioma
    relation: connects-to
    note: "NF2 somatic LOF is the most common alteration in mesothelioma (~50%); NF2 loss → nuclear YAP1/TAZ → TEAD → CTGF, CYR61, BIRC5 (survivin) → cell survival and proliferation; TEAD inhibitors (K-975, VT3989) in clinical trials for NF2-deficient mesothelioma."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "YAP1/TAZ-TEAD drives MYC and MYCN transcriptional upregulation; YAP-MYC co-activation in KRAS-mutant cancers (NSCLC, CRC) creates co-dependencies; YAP1 and MYC together amplify G1 cell cycle progression via CCND1 and CDK4 upregulation in multiple tumor types."
---

# YAP1

## Overview

**YAP1** (Yes-Associated Protein 1) is a 504 amino acid (65 kDa) **transcriptional co-activator** and the central nuclear effector of the **Hippo tumor suppressor pathway** in mammals. YAP1 has no sequence-specific DNA binding domain; instead it functions as a **co-activator of TEAD1/2/3/4** transcription factors, driving expression of target genes that promote cell survival, proliferation, and organ growth (CTGF, CYR61, ANKRD1, BIRC5/survivin, CCND1). YAP1 activity is gated by the Hippo kinase cascade: when Hippo is active (high cell density, contact inhibition, proper apical junctions, mechanical compression), LATS1/2 phosphorylate YAP1 at Ser127 → cytoplasmic sequestration by 14-3-3 proteins → growth arrest. When Hippo is inactive (low cell density, NF2/merlin LOF, mechanical stretch, GPCR signaling) → YAP1 dephosphorylated → nuclear → TEAD target gene activation → proliferation. YAP1 was initially characterized as an oncogene by Zanconato, Piccolo, and colleagues and comprehensively reviewed in the context of cancer by Harvey, Zhang, and Thomas in 2013 [^zanconato-2016-yap-cancer] [^harvey-2013-hippo-cancer].

**Hippo pathway — canonical vertebrate cascade:**

```
Contact inhibition ON                   Contact inhibition OFF
Cell-cell adhesion (E-cadherin)         Low density, mechanical stretch
NF2/merlin activated (head-to-tail)     NF2/merlin in open/inactive state
      ↓                                       ↓
MST1/2 kinases (SARAH domain)           MST1/2 inactive
      ↓ (phosphorylate MOB1, LATS)             ↓
LATS1/2 kinases activated               LATS1/2 inactive (not phosphorylated)
      ↓                                       ↓
YAP1 Ser127 phosphorylated              YAP1 Ser127 not phosphorylated
      ↓                                       ↓
14-3-3 binding → cytoplasmic            YAP1 nuclear
      ↓                                       ↓
YAP1 degraded (Ser381 → βTRCP)         YAP1-TEAD complex forms
No TEAD target gene activation          ↓
Growth arrest / contact inhibition      CTGF, CYR61, BIRC5, CCND1, MYC
                                        Proliferation, survival, invasion
```

## Structure

### YAP1 protein domains

**N-terminal TEAD-binding domain (TBD; aa 1-84):**
- YAP1 interacts with TEAD1/2/3/4 primarily via its N-terminal domain; a 9-amino acid Ω-loop ("paddle" or "ΩL" motif) from YAP1 inserts into a hydrophobic pocket in the TEAD Y-H fold (the TBD-TEAD interface); this interaction is the primary driver of YAP1 transcriptional activity
- **TEAD inhibitors target this interface**: verteporfin (a photosensitizer repurposed as TEAD inhibitor), K-975 (Pfizer; covalently binds palmitate-binding pocket on TEAD4), IK-930 (Relay Therapeutics), VT3989 (Vivace Therapeutics) — all block YAP1/TAZ–TEAD interaction
- TAZ (WW domain-containing transcription regulator 1; WWTR1): paralog of YAP1 (46% identity); also binds TEAD; shares the same LATS1/2-mediated phosphorylation regulation; often functions redundantly with YAP1 but has distinct tissue specificities and protein interactions

**WW domains (WW1: aa 170-202; WW2: aa 204-236):**
- Bind PPXY (PY) motifs on multiple protein partners
- LATS1/2 PPxY motifs: LATS kinases dock on YAP1 WW domains → positioning of LATS kinase domain to phosphorylate Ser127 and Ser381
- AMOT (Angiomotin) PPxY: AMOT directly sequesters YAP1 via WW domain interaction → cytoplasmic retention independent of phosphorylation; AMOT is a major YAP1 inhibitor in tight junctions and apical junctions
- RUNX2, RUNX3: PPxY-bearing transcription factors that co-activate YAP1-TEAD at bone/epithelial gene promoters

**SH3-binding domain and linker (aa 237-291):**
- Contains Ser127 (primary LATS phosphorylation site): pSer127 recruits 14-3-3 proteins → cytoplasmic sequestration
- Contains Ser381 (secondary LATS phosphorylation site): pSer381 → priming for CK1δ/ε phosphorylation of Ser384/Ser387 → phosphodegron recognized by βTRCP E3 ubiquitin ligase → YAP1 polyubiquitination and proteasomal degradation

**Transcriptional activation domain (TAD; aa 292-504):**
- C-terminal; contains interactions with transcriptional coactivators (p300/CBP, SMAD2/3 in some contexts)
- PDZ-binding motif (very C-terminal: -FLWT): binds PDZ domain proteins including SCRIBBLE, LIN7C; coupling of YAP1 to polarity complexes — loss of polarity (e.g., in ErbB2-driven breast cancer) → YAP1 liberated from polarity protein sequestration → nuclear

### YAP1 phosphorylation at Ser127 — molecular mechanism

LATS1/2 are NDR family kinases activated by MST1/2 (STE20-like kinases) via LATS phosphorylation at T1079 (LATS1) and T1041 (LATS2). The activated LATS kinase phosphorylates YAP1 at:
- **Ser127**: major regulatory site; creates a 14-3-3 binding motif (RSXpS); 14-3-3 proteins dimerize and mask the nuclear import signal of YAP1 → cytoplasmic retention
- **Ser381**: secondary site; promotes SCFβTRCP-mediated ubiquitination → YAP1 proteasomal degradation (total protein reduction)

Dephosphorylation of YAP1 pSer127 by PP1A and PP2A phosphatases restores nuclear YAP1 under low-density or mechanical stretch conditions. The PP2A-YAP1 axis is regulated by the Tribbles pseudokinase TRRIB and by SFK (SRC family kinases): SRC phosphorylates YAP1 Tyr357 → prevents pSer127-mediated 14-3-3 binding despite LATS activity → nuclear YAP1 even in "Hippo-on" conditions.

## Function

### YAP1 in organ size control and tissue homeostasis

YAP1 is the principal executor of the Hippo pathway's organ size control function in vertebrates:
- Liver: conditional Yap1 overexpression in mouse liver → massive hepatomegaly (10-20× liver mass increase) via TEAD-driven hepatocyte proliferation; Lats1/2 liver knockout → nuclear YAP → similar phenotype
- Intestine: YAP1 drives intestinal stem cell expansion after injury (IRE → regenerative YAP1 nuclear); in colon, APC mutation + YAP1 nuclear → Wnt-YAP cooperativity → adenoma formation
- Lung: YAP1 nuclear in alveolar type II cells after damage → AT2 → AT1 differentiation programs
- Heart: YAP1 activation promotes cardiomyocyte proliferation → cardiac regeneration after injury (neonatal mice); loss of Hippo → cardiac hypertrophy and failure in adults

### YAP1 as mechanosensor

YAP1 is a key sensor and transducer of **mechanical forces**:
- **Stiff matrix / high tension** → integrin-FAK → RhoA → actin cytoskeleton tension → inhibition of LATS1/2 (via F-actin-mediated sequestration of AMOTL2 away from YAP1) → YAP1 nuclear → proliferative response
- **Soft matrix / low tension** → YAP1 cytoplasmic → quiescence
- **Tumor microenvironment stiffening** (desmoplasia in pancreatic cancer, breast cancer): increased matrix stiffness → YAP1 nuclear → tumor cell proliferation and immune exclusion (YAP1 drives TGF-β, CTGF → fibrosis amplification)

### YAP1 in cancer

**NF2-deficient tumors (mesothelioma, schwannoma, meningioma):**
NF2/merlin LOF → failed MST1/2 activation → LATS1/2 inactive → YAP1/TAZ nuclear. This is the primary oncogenic mechanism in:
- Mesothelioma: NF2 LOF (~50%); LATS1/2 LOF (~5-10%); YAP1 amplification in some; essentially all mesotheliomas have nuclear YAP1
- Schwannoma/meningioma: NF2 germline or somatic LOF → nuclear YAP → TEAD-CTGF/CYR61 → proliferation of Schwann cells / arachnoid cells

**KRAS-mutant cancers:**
- KRAS-driven RAS-MAPK signaling activates YAP1 via multiple mechanisms (RAL-GTPases, RASSF-MST pathway disruption, MAPK-LATS crosstalk)
- YAP1 creates acquired resistance to KRAS/MEK inhibitors in NSCLC and CRC; co-inhibition of KRAS/MEK + TEAD/YAP1 → synthetic lethality in preclinical models
- YAP1/TAZ amplification: 11q22 amplification (YAP1 locus) in HNSCC (~24%), gastric cancer, liver cancer; YAP1 gene fusions with MAML2 or other partners in some epithelioid hemangioendotheliomas

**YAP1-MAML2 fusion in cystic mucoepidermoid carcinoma:**
- t(11;19) translocation → CRTC1-MAML2 fusion (common) or YAP1-MAML2 fusion (rarer); YAP1-MAML2 is an oncogenic fusion driver in a subset of salivary gland mucoepidermoid carcinoma and some sclerosing epithelioid fibrosarcoma

## Mechanism

### YAP1-TEAD transcriptional target genes

YAP1-TEAD drives a set of target genes with distinct biological roles:
- **CTGF (CCN2)**: extracellular matrix protein → fibrosis, desmoplasia, mechanotransduction feedback
- **CYR61 (CCN1)**: matricellular protein → angiogenesis, invasion, survival
- **BIRC5 (Survivin)**: IAP family anti-apoptotic protein → cancer cell survival
- **CCND1 (Cyclin D1)**: G1 cell cycle progression → proliferation
- **MYC**: amplified by YAP-TEAD directly (binding sites in MYC promoter)
- **ANKRD1 (Cardiac ankyrin repeat kinase)**: mechanosensing gene; induced by stretch
- **AMOTL2**: negative feedback loop — YAP induces AMOTL2, which then sequesters YAP back to cytoplasm

**Therapeutic targeting of YAP1-TEAD:**

| Agent | Mechanism | Development stage |
|---|---|---|
| Verteporfin | Disrupts YAP1-TEAD protein interaction | Repurposed; preclinical/early clinical |
| K-975 (Pfizer) | Covalent inhibitor binding TEAD palmitate pocket | Phase II (mesothelioma) |
| IK-930 (Relay Therapeutics) | TEAD palmitoylation site inhibitor | Phase I |
| VT3989 (Vivace Therapeutics) | TEAD allosteric inhibitor | Phase II (mesothelioma, NSCLC) |
| GS-9521 | YAP1-TEAD inhibitor | Preclinical |

TEAD auto-palmitoylation (Cys palmitoylation in a hydrophobic pocket in TEAD's YBD domain) is required for TEAD stability and YAP1 interaction → palmitoyl pocket inhibitors displace the lipid → conformational change → reduced YAP1 binding → YAP1-TEAD disruption.

## Connections

- `connects-to` → **[NF2](../../03-molecular/nf2/README.md)** — NF2/merlin activates the Hippo kinase cascade (MST1/2 → LATS1/2) to phosphorylate YAP1 Ser127 → 14-3-3 binding → cytoplasmic retention; NF2 LOF in schwannoma, meningioma, and mesothelioma → nuclear YAP1/TAZ → TEAD-driven proliferation and CTGF/CYR61 upregulation.
- `connects-to` → **[Neurofibromatosis Type 2](../../07-system/neurofibromatosis-type-2/README.md)** — NF2 disease (germline NF2 LOF) → bilateral vestibular schwannomas, meningiomas, ependymomas; nuclear YAP1 is the downstream effector of NF2 LOF → TEAD target genes drive schwannoma/meningioma proliferation; TEAD/YAP inhibitors in NF2-associated tumor trials.
- `connects-to` → **[Mesothelioma](../../07-system/mesothelioma/README.md)** — NF2 somatic LOF is the most common alteration in mesothelioma (~50%); NF2 loss → nuclear YAP1/TAZ → TEAD → CTGF, CYR61, BIRC5 (survivin) → cell survival and proliferation; TEAD inhibitors (K-975, VT3989) in clinical trials for NF2-deficient mesothelioma.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — YAP1/TAZ-TEAD drives MYC and MYCN transcriptional upregulation; YAP-MYC co-activation in KRAS-mutant cancers (NSCLC, CRC) creates co-dependencies; YAP1 and MYC together amplify G1 cell cycle progression via CCND1 and CDK4 upregulation in multiple tumor types.

[^zanconato-2016-yap-cancer]: Zanconato F, Cordenonsi M, Piccolo S. YAP/TAZ at the roots of cancer. *Cancer Cell.* 2016;29(6):783-803. [doi:10.1016/j.ccell.2016.05.005](https://doi.org/10.1016/j.ccell.2016.05.005) · [PubMed 27300434](https://pubmed.ncbi.nlm.nih.gov/27300434/)
[^harvey-2013-hippo-cancer]: Harvey KF, Zhang X, Thomas DM. The Hippo pathway and human cancer. *Nat Rev Cancer.* 2013;13(4):246-257. [doi:10.1038/nrc3458](https://doi.org/10.1038/nrc3458) · [PubMed 23467301](https://pubmed.ncbi.nlm.nih.gov/23467301/)

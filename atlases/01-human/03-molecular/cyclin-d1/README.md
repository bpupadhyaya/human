---
schema: human-scale-entry/v1
id: cyclin-d1
name: Cyclin D1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Cell cycle G1/S accelerator; Wnt/RAS-MAPK/oncogene signaling → cyclin D1-CDK4/6 → Rb phosphorylation → E2F-S phase entry. Amplified in breast, HNSCC, and bladder cancers; cyclin D1-CDK4/6 complex is the direct molecular target of palbociclib, ribociclib, and abemaciclib."
aliases: ["CCND1", "cyclin D1", "BCL1", "PRAD1", "D11S287E", "PCNA-associated protein"]
sources:
  - id: sherr-1994-cyclins-review
    type: peer-reviewed
    cite: "Sherr CJ. G1 phase progression: cycling on cue. Cell. 1994;79(4):551-555."
    doi: "10.1016/0092-8674(94)90540-1"
    pmid: "7954821"
    url: "https://doi.org/10.1016/0092-8674(94)90540-1"
  - id: weinberg-1995-rb-review
    type: peer-reviewed
    cite: "Weinberg RA. The retinoblastoma protein and cell cycle control. Cell. 1995;81(3):323-330."
    doi: "10.1016/0092-8674(95)90385-2"
    pmid: "7736585"
    url: "https://doi.org/10.1016/0092-8674(95)90385-2"
  - id: dickson-1995-cyclin-d1-cancer
    type: peer-reviewed
    cite: "Dickson C, Fantl V, Gillett C, et al. Amplification of chromosome band 11q13 and a role for cyclin D1 in human breast cancer. Cancer Lett. 1995;90(1):43-50."
    doi: "10.1016/0304-3835(94)03676-A"
    pmid: "7882378"
    url: "https://doi.org/10.1016/0304-3835(94)03676-A"
cross_links:
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Cyclin D1 is the regulatory partner of CDK4 and CDK6; cyclin D1-CDK4/6 phosphorylates Rb Ser780/795 → E2F release → S-phase transcription; CDK4/6 inhibitors (palbociclib, ribociclib, abemaciclib) compete at the CDK4/6-cyclin D1 interface → catalytic inactivation."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "MYC transcriptionally activates CCND1; cyclin D1 feeds back to stabilize MYC Ser62 via CDK4-RSK phosphorylation; MYC and cyclin D1 amplification rarely co-occur (functional redundancy); both drive G1-S progression via Rb hyperphosphorylation and E2F release."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Wnt-beta-catenin directly activates CCND1 transcription via beta-catenin-TCF binding to the CCND1 promoter — a primary oncogenic effector of Wnt; cyclin D1 is a canonical Wnt target gene and readout of pathway activity; APC-mutant CRC overexpresses cyclin D1."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "p53 represses CCND1 transcription directly and via p21 (CDKN1A) induction → CDK4/6 inhibition → cyclin D1-CDK4/6 complex dissociation; loss of p53 → cyclin D1 derepression → accelerated G1-S; p53-null tumors depend on cyclin D1-CDK4/6 for unchecked proliferation."
---

# Cyclin D1

## Overview

**Cyclin D1 (CCND1)** is the **rate-limiting regulatory subunit** of the **CDK4/CDK6 complex** — the molecular machine that drives cells from G1 phase into S phase by phosphorylating and inactivating the **retinoblastoma protein (Rb)**. Cyclin D1 is a **sensor and integrator of mitogenic signals**: its synthesis is induced by growth factors, oncogenes (RAS, MYC), and developmental signals (Wnt), and its rapid degradation (half-life ~20-30 min) means cyclin D1 levels rapidly reflect the current mitogenic status of the cell [^sherr-1994-cyclins-review].

**The D-type cyclins (D1, D2, D3):**
- **Cyclin D1 (CCND1):** Ubiquitous; most important in epithelial cancers; chromosome 11q13; most frequently amplified cyclin in cancer
- **Cyclin D2 (CCND2):** Hematopoietic cells; T cells, B cells, astrocytes; important in testicular germ cell tumors
- **Cyclin D3 (CCND3):** Lymphocytes; T-ALL (CCND3 R286 hotspot mutation stabilizes cyclin D3 → cyclin D3-CDK6 → T cell proliferation)
- All three D-type cyclins share functional redundancy for Rb phosphorylation but have tissue-specific expression and partner preferences (CDK4 vs. CDK6)

**Cyclin D1 as an oncogene:**
- **CCND1 amplification:** Chromosome 11q13.3 amplification is one of the most frequent focal amplifications in human cancer — found in ~15-25% of breast cancer (especially luminal B), 30-50% of head and neck squamous cell carcinoma (HNSCC), 15-20% of bladder cancer, and esophageal/gastric adenocarcinoma
- **PRAD1 (parathyroid adenoma 1):** Original discovery of CCND1 as an oncogene from cloning the chromosomal translocation breakpoint in parathyroid adenomas — inv(11)(p15;q13) → CCND1 under PTH promoter → cyclin D1 overexpression
- **CCND1 t(11;14) translocation in mantle cell lymphoma (MCL):** Constitutive CCND1 expression under the IGH enhancer → cyclin D1-CDK4/6 → Rb inactivation → proliferating mantle cell lymphocytes; CCND1 overexpression is the defining molecular feature of MCL; detected by FISH or IHC

## Structure

### Cyclin D1 molecular interactions [^weinberg-1995-rb-review]

**Cyclin box domain (cyclin fold):**
- ~100 aa cyclin box × 2 (tandem cyclin fold) → CDK4/6 binding interface; common to all cyclins; positions CDK substrate in active site
- **LXCXE motif:** Cyclin D1 contains an LXCXE motif (Leu-X-Cys-X-Glu) → direct binding to Rb pocket domain → Rb phosphorylation; same motif used by viral oncoproteins (E7 from HPV, E1A from adenovirus) to inactivate Rb — convergent evolution of viral and oncogenic Rb inactivation strategies

**Regulation of cyclin D1 abundance:**
- **Synthesis (transcriptional induction):** Wnt → TCF/LEF → CCND1 promoter activation; RAS-ERK → AP-1 (FOS/JUN) → CCND1 transcription; MYC E-box binding → CCND1 activation; NF-kB → CCND1 in inflammation-driven proliferation
- **Degradation (ubiquitin-proteasome):**
  - **CRL1-FBXW8:** GSK-3β phosphorylates cyclin D1 Thr286 → FBXW8 (F-box protein) recognition → polyubiquitination → 26S proteasome; this is the primary cyclin D1 degradation pathway; AKT → GSK-3β inhibition → reduced Thr286 phosphorylation → cyclin D1 stabilization → a secondary mechanism by which PI3K-AKT drives cell cycle progression
  - **CRL4-VPRBP:** DNA damage → cyclin D1 rapid degradation via Cul4A-DDB1-VPRBP E3 ligase → clearance of cyclin D1 from S-phase nuclei (excess cyclin D1 in S-phase inhibits DNA replication by inhibiting PCNA)
  - Cyclin D1 Thr286A mutation (non-degradable) → constitutively nuclear → cancer model; Thr286 phosphorylation also promotes cytoplasmic cyclin D1 export in G1 → nuclear cyclin D1 only when AKT is active and GSK-3β is inhibited

**CDK4/6 activation (cyclin D1-CDK4/6 complex):**
- Cyclin D1 binding to CDK4/6 is not sufficient for full kinase activity; requires removal of CIP/KIP CDK inhibitors (p21, p27, p57) and activation loop phosphorylation by CDK-activating kinase (CAK = cyclin H-CDK7-MAT1)
- **INK4 CDK inhibitors (p16/CDKN2A, p15, p18, p19):** Specifically block CDK4/6 by occupying the cyclin D1 binding site → competitive inhibition; p16/CDKN2A is the natural cellular brake on cyclin D1-CDK4/6 and is frequently deleted in cancer

### Rb phosphorylation — the G1/S transition [^weinberg-1995-rb-review]

**Rb pocket proteins (Rb, p107, p130):**
- In G0/early G1: hypophosphorylated Rb → binds E2F/DP heterodimers → represses E2F target genes (cyclin E, cyclin A, dihydrofolate reductase, DNA polymerase alpha) → G1 arrest
- **Cyclin D1-CDK4/6 phosphorylation cascade:**
  1. Cyclin D1-CDK4/6 → Rb Ser780, Ser795 monophosphorylation (partial Rb inactivation; initial)
  2. Cyclin E-CDK2 → Rb Ser567, Thr373 additional phosphorylation → full Rb hyperphosphorylation → E2F release → positive feedback (E2F activates cyclin E → more CDK2 → more Rb phosphorylation → committed S-phase entry)
  3. **Restriction point:** Once Rb is fully hyperphosphorylated and S-phase transcription begins, cells are committed to complete the cell cycle independent of continued mitogenic signals — this irreversible commitment is the molecular restriction point

**CDK4/6 inhibitor mechanism:**
- Palbociclib, ribociclib, abemaciclib → occupy CDK4/6 ATP-binding site → compete with ATP → prevent Rb phosphorylation → Rb remains hypophosphorylated → E2F repressed → G1 arrest; **biomarker:** Rb-positive tumors required for CDK4/6 inhibitor activity (Rb-null tumors are intrinsically resistant); p16-null or cyclin D1-amplified tumors have highest dependence on CDK4/6

## Function

### Cyclin D1 in cancer [^dickson-1995-cyclin-d1-cancer]

**Breast cancer (luminal subtypes):**
- Cyclin D1 is overexpressed in ~50% and amplified in ~15-20% of breast cancer; CCND1 amplification is a key luminal B feature; ER-driven cyclin D1 transcription is the primary proliferative signal in luminal A/B breast cancer; CDK4/6 inhibitors (palbociclib + letrozole, PALOMA-2: PFS 24.8 vs. 14.5 months) specifically target this dependency
- CCND1-amplified tumors are more sensitive to CDK4/6 inhibitors (though all Rb-positive HR+ tumors benefit)

**Head and neck squamous cell carcinoma (HNSCC):**
- CCND1 amplification at 11q13 in 30-50% of HNSCC (oral cavity, oropharynx, hypopharynx); co-occurs with FGFR1 and FGFR3 at 11q13; cyclin D1 overexpression correlates with poor prognosis and reduced benefit from platinum-based chemotherapy; therapeutic target for CDK4/6 inhibitors in recurrent/metastatic HNSCC (clinical trials: ribociclib + cetuximab)

**Mantle cell lymphoma (MCL):**
- t(11;14)(q13;q32) → CCND1-IGH → constitutive cyclin D1 → CDK4-Rb pathway addiction; MCL cells strongly dependent on CDK4/6; ibrutinib (BTK inhibitor) + palbociclib (MCL clinical trials); venetoclax + ibrutinib + palbociclib triplet under investigation

**Non-canonical cyclin D1 functions:**
- **Transcriptional co-regulator (nucleus):** Cyclin D1 interacts with >30 transcription factors independent of CDK4/6 — including AR (androgen receptor) → repression → prostate cancer controversy; ESR1 → co-activation → ER-driven gene programs; CBP/p300 → histone acetyltransferase regulation → chromatin remodeling
- **Cytoplasmic cyclin D1:** In S phase, Thr286-phosphorylated cyclin D1 translocates to cytoplasm → avoids DNA replication inhibition (PCNA binding); cytoplasmic cyclin D1 activates RAC1-PAK1 → cell migration and invasion → pro-metastatic function

### Cell cycle re-entry and senescence escape

**CCND1 in oncogene-induced senescence bypass:**
- Normal: KRAS → initial cyclin D1 upregulation → proliferation → eventually OIS (oncogene-induced senescence) via p16/ARF-p53 → cyclin D1-CDK4/6 blocked by p16 → arrest
- Cancer: p16/CDKN2A deletion (co-occurring with KRAS) → p16 absent → cyclin D1-CDK4/6 unchecked → bypass of OIS → continued proliferation; this explains why p16 deletion and KRAS amplification are co-drivers in many cancers

## Mechanism

### CDK4/6 inhibitors — clinical impact

**FDA-approved CDK4/6 inhibitors (all in HR+/HER2- breast cancer):**
- **Palbociclib (Ibrance):** First approved CDK4/6 inhibitor (2015); + letrozole (PALOMA-2: mPFS 24.8 vs. 14.5 months vs. letrozole alone); + fulvestrant (PALOMA-3); oral, once daily 21 days on / 7 days off; neutropenia dose-limiting (no cardiotoxicity)
- **Ribociclib (Kisqali):** + letrozole (MONALEESA-2: OS 63.9 vs. 51.4 months); OS benefit confirmed in pre/perimenopausal women (MONALEESA-7); continuous dosing; QT prolongation monitoring required; cardiac safe otherwise
- **Abemaciclib (Verzenio):** Continuous dosing; more selective CDK4 > CDK6 → less neutropenia, more diarrhea; + anastrozole/letrozole (MONARCH-3); + fulvestrant (MONARCH-2); adjuvant monarchE (high-risk early-stage: DFS HR 0.68, invasive DFS 81.3% vs. 72.2% at 4 years) → first CDK4/6 inhibitor in adjuvant setting

**Resistance to CDK4/6 inhibitors:**
- **Primary resistance:** Rb loss (CCND1-CDK4/6 → Rb → E2F signaling absent; Rb-null tumors don't respond); amplification of cyclin E1 (CCNE1) → CDK2-dependent Rb phosphorylation bypasses CDK4/6 requirement
- **Acquired resistance:** ESR1 mutations → endocrine therapy resistance (often co-occurring); CDK6 amplification; loss of p16/CDKN2A; CCND1 amplification (increased cyclin D1 → outcompete inhibitor); PI3K pathway amplification → AKT → cyclin D1 stabilization (GSK3beta inhibition)
- **Combinations to overcome resistance:** CDK4/6 + PI3K/AKT (alpelisib + palbociclib), CDK4/6 + mTOR (everolimus + ribociclib COMPLEEMENT-1 trial), CDK4/6 + SERDs (elacestrant — EMERALD), CDK4/6 + HER2 (in HER2+/HR+ tumors)

## Connections

- `connects-to` → **[CDK4/6](../cdk4-6/README.md)** — Cyclin D1 is the regulatory partner of CDK4/CDK6; cyclin D1-CDK4/6 phosphorylates Rb Ser780/795 → E2F release → S-phase transcription; CDK4/6 inhibitors (palbociclib, ribociclib, abemaciclib) compete at the CDK4/6-cyclin D1 interface to restore G1 arrest.
- `connects-to` → **[MYC](../myc/README.md)** — MYC transcriptionally activates CCND1; cyclin D1 feeds back to stabilize MYC Ser62 via CDK4-RSK; MYC and cyclin D1 amplification rarely co-occur (functional redundancy); both drive G1-S progression via Rb hyperphosphorylation and E2F target gene induction.
- `connects-to` → **[Wnt/beta-catenin](../wnt-beta-catenin/README.md)** — Wnt-beta-catenin directly activates CCND1 transcription via beta-catenin-TCF at the CCND1 promoter — a primary oncogenic effector; cyclin D1 is a canonical Wnt target gene and downstream readout; APC-mutant CRC overexpresses cyclin D1.
- `connects-to` → **[p53](../p53/README.md)** — p53 represses CCND1 transcription directly and via p21 induction → CDK4/6 inhibition → cyclin D1-CDK4/6 dissociation; p53 loss → cyclin D1 derepression; p53-null tumors depend on cyclin D1-CDK4/6 for unchecked proliferation.

[^sherr-1994-cyclins-review]: Sherr CJ. G1 phase progression: cycling on cue. *Cell.* 1994;79(4):551-555. [doi:10.1016/0092-8674(94)90540-1](https://doi.org/10.1016/0092-8674(94)90540-1) · [PubMed 7954821](https://pubmed.ncbi.nlm.nih.gov/7954821/)
[^weinberg-1995-rb-review]: Weinberg RA. The retinoblastoma protein and cell cycle control. *Cell.* 1995;81(3):323-330. [doi:10.1016/0092-8674(95)90385-2](https://doi.org/10.1016/0092-8674(95)90385-2) · [PubMed 7736585](https://pubmed.ncbi.nlm.nih.gov/7736585/)
[^dickson-1995-cyclin-d1-cancer]: Dickson C, Fantl V, Gillett C, et al. Amplification of chromosome band 11q13 and a role for cyclin D1 in human breast cancer. *Cancer Lett.* 1995;90(1):43-50. [doi:10.1016/0304-3835(94)03676-A](https://doi.org/10.1016/0304-3835(94)03676-A) · [PubMed 7882378](https://pubmed.ncbi.nlm.nih.gov/7882378/)

---
schema: human-scale-entry/v1
id: lmp1
name: LMP1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "EBV LMP1 (latent membrane protein 1; 386 aa; 6 TM domains) mimics constitutively active CD40; CTAR1 → TRAF1/2/3 → NF-κB (alternative); CTAR2 → TRADD/TRAF6 → NF-κB (canonical); drives B cell immortalization, BCL-2, IL-6; oncogene in Hodgkin lymphoma and NPC."
aliases: ["LMP1", "latent membrane protein 1", "LMP-1", "EBV LMP1", "BNLF1", "EBV oncoprotein", "constitutively active CD40", "CTAR1", "CTAR2", "EBV immortalization", "EBV NF-kB"]
sources:
  - id: wang-1985-lmp1-discovery
    type: peer-reviewed
    cite: "Wang D, Liebowitz D, Kieff E. An EBV membrane protein expressed in immortalized lymphocytes transforms established rodent cells. Cell. 1985;43(3 Pt 2):831-840."
    doi: "10.1016/0092-8674(85)90256-9"
    pmid: "3000618"
    url: "https://doi.org/10.1016/0092-8674(85)90256-9"
    accessed: "2026-06-08"
  - id: mosialos-1995-lmp1-traf
    type: peer-reviewed
    cite: "Mosialos G, Birkenbach M, Yalamanchili R, VanArsdale T, Ware C, Kieff E. The Epstein-Barr virus transforming protein LMP1 engages signaling proteins for the tumor necrosis factor receptor family. Cell. 1995;80(3):389-399."
    doi: "10.1016/0092-8674(95)90489-1"
    pmid: "7859281"
    url: "https://doi.org/10.1016/0092-8674(95)90489-1"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/07-system/epstein-barr-virus
    relation: connects-to
    note: "LMP1 is EBV's primary oncoprotein expressed in latency II/III; constitutively active CD40 mimic; 6 TM domain aggregation enables ligand-independent TRAF signaling; drives B cell immortalization, EBV latency III growth program, and EBV-associated lymphomagenesis."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "LMP1 CTAR1 (aa 186-231) binds TRAF1/2/3 → NIK → IKKα → p52/RelB (alternative NF-κB); CTAR2 (aa 352-386) binds TRADD → TRAF6 → IKKβ → p65/p50 (canonical NF-κB); dual pathway activation → BCL-2, ICAM-1, IL-6, CD23, TRAF1 → B cell survival and proliferation."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "LMP1 → NF-κB → MDM2 transcription → p53 ubiquitination; LMP1 → BCL-2/BCL-XL → resistance to p53-dependent apoptosis; EBNA3C (distinct protein) is the primary EBV p53 antagonist (Skp2 pathway); LMP1 and EBNA3C cooperate to prevent p53-mediated tumor suppression."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "LMP1 → NF-κB → TGF-β1 transcription in EBV-infected B cells; LMP1 can block SMAD2/3 nuclear translocation → prevents TGF-β growth arrest; exosomal LMP1 shed from tumor cells modulates TGF-β in stromal fibroblasts and T cells in the tumor microenvironment."
---

# LMP1

## Overview

**Latent membrane protein 1 (LMP1)**, encoded by the EBV **BNLF1** gene, is the primary **transforming oncoprotein** of Epstein-Barr virus. Identified by Elliott Kieff's laboratory in 1985 as the first EBV protein capable of transforming rodent fibroblasts [^wang-1985-lmp1-discovery], LMP1 is a **386-amino acid type III integral membrane protein** with **six transmembrane (TM) domains** that constitutively aggregates in the cell membrane to recruit tumor necrosis factor receptor-associated factors (TRAFs) and activate **NF-κB**, **AP-1**, **MAPK**, and **JAK-STAT** signaling pathways without requiring any ligand [^mosialos-1995-lmp1-traf].

**LMP1 is the master driver of EBV-induced B cell immortalization** — it is the sole EBV gene product sufficient to rescue BCR-negative "death-committed" B cells from apoptosis and is required for the B cell immortalization that defines EBV latency III (the growth program seen in lymphoblastoid cell lines and PTLD). Mechanistically, LMP1 functions as a **constitutively active, ligand-independent CD40 mimic**: CD40 on B cells normally requires CD40L (CD154) on activated T helper cells to drive B cell survival and proliferation in germinal centers; LMP1 substitutes for this T cell signal, enabling EBV-infected B cells to proliferate and survive independently of cognate T cell help.

**Clinical relevance:** LMP1 is expressed in **EBV latency II** (Reed-Sternberg cells in Hodgkin lymphoma, nasopharyngeal carcinoma) and **latency III** (PTLD, lymphoblastoid cell lines). LMP1-driven NF-κB is the essential survival signal for Reed-Sternberg cells — tumor cells that have lost functional BCR expression and would otherwise undergo death-by-neglect apoptosis. LMP1 is therefore both a diagnostic biomarker and a potential therapeutic target in EBV-associated malignancies.

## Structure

### Protein architecture

LMP1 (386 aa) is a **type III polytopic integral membrane protein** — it lacks a signal peptide and inserts into membranes via multiple TM helices without a single N-terminal TM anchor:

**N-terminal cytoplasmic domain (NTD; aa 1-23):**
- Short; important for membrane localization targeting to lipid rafts
- Required for lipid raft association — LMP1 concentrates in sphingomyelin/cholesterol-rich membrane microdomains which are critical for efficient TRAF signaling
- Interacts with vimentin cytoskeleton

**Six transmembrane domains (aa 24-186):**
- Six amphipathic α-helices spanning the membrane
- TM domains drive **constitutive self-aggregation** in the plasma membrane → patches of clustered LMP1 (~50 molecules) that nucleate TRAF recruitment without ligand
- The clustering mimics **ligand-induced CD40 receptor aggregation** — but constitutively, because there is no ligand/receptor/off-switch
- Critical mutations in TM4 (I129S) and TM6 (L168G) abolish membrane aggregation → abolish signaling → abolish transformation

**C-terminal activating regions (CTAR):**

| Domain | Location | Binding Partners | Pathways Activated |
|--------|----------|-----------------|-------------------|
| **CTAR1** | aa 186-231 | TRAF1, TRAF2, TRAF3 | Alternative NF-κB (NIK → IKKα → p100 → p52/RelB); also PI3K, MAPK |
| **CTAR2** | aa 352-386 | TRADD → RIP1, TRAF2, TRAF6 | Canonical NF-κB (IKKβ → IκBα → p65/p50); JNK/AP-1; STAT3 (via JAK3) |
| **CTAR3** | aa 275-330 | SUMO modification | STAT1/2 activation; contributes to JAK-STAT signaling |

**Comparison with CD40:**
- Normal CD40: homotrimeric → CD40L (CD154, on Th cells) trimer → CD40 clustering → TRAF binding → NF-κB/MAPK activation; requires cognate T cell help; transient
- LMP1: TM aggregation-driven clustering without ligand → same TRAF recruitment → same downstream pathways → constitutive, sustained

## Function

### NF-κB activation — dual pathway mechanism

**Alternative (non-canonical) NF-κB via CTAR1 [^mosialos-1995-lmp1-traf]:**
1. LMP1 CTAR1 → recruits TRAF1/TRAF2 (via PXQXT motif) and TRAF3 (via PVQLSY motif)
2. TRAF3 normally inhibits NIK (NF-κB-inducing kinase; MAP3K14) by promoting NIK ubiquitination/degradation
3. LMP1-bound TRAF3 is sequestered → NIK accumulates and is stabilized
4. NIK → phosphorylates and activates **IKKα** → **p100 processing → p52/RelB** homodimer → nuclear translocation → alternative NF-κB target genes
5. Alternative NF-κB → **BAFF, APRIL** (B cell survival factors); **BCMA** (B cell maturation antigen); long-lived B cell survival

**Canonical NF-κB via CTAR2:**
1. LMP1 CTAR2 → recruits **TRADD** (via C-terminal PVYLHY/Y383 motif)
2. TRADD → recruits **RIP1** (RIPK1) + **TRAF6**
3. TRAF6 → K63-linked polyubiquitin chains → recruits **TAK1** → TAK1 activates **IKKβ/IKKγ** complex
4. **IKKβ → IκBα Ser32/Ser36 phosphorylation → IκBα ubiquitination → proteasomal degradation → p65/p50** released → nuclear translocation
5. Canonical NF-κB → **BCL-2, BCL-XL** (anti-apoptotic); **ICAM-1** (adhesion); **IL-6** (autocrine growth factor); **CD23** (low-affinity IgE receptor; B cell activation marker); **TRAF1** (NF-κB feedback amplifier)

**Dual pathway significance:** Simultaneous activation of both canonical and alternative NF-κB by a single viral protein is virtually unique to LMP1 — CD40 normally activates both but sequentially and with lower amplitude. LMP1 drives constitutive, sustained, high-amplitude NF-κB activity that greatly exceeds normal CD40-mediated signaling.

### AP-1 and MAPK activation

LMP1 CTAR2 → TRAF6 → TAK1 → **JNK** → **c-Jun phosphorylation** → AP-1 heterodimerization (c-Jun/c-Fos or c-Jun/ATF-2) → AP-1 target genes:
- **Matrix metalloproteinases (MMP-1, MMP-9)**: Invasion and metastasis in NPC
- **IL-8**: Neutrophil recruitment
- **VEGF**: Angiogenesis
- **CD44**: Cell adhesion; promotes invasion

### JAK-STAT activation

LMP1 CTAR3 (and indirectly via CTAR2) → **JAK3 → STAT3 Tyr705 phosphorylation** → pSTAT3 dimerization → nuclear translocation → STAT3 target genes:
- **BCL-XL**: Anti-apoptosis
- **Cyclin D1**: G1 progression
- **c-Myc**: Proliferation (LMP1-driven c-Myc is more modest than EBNA2-driven)
- **VEGF**: Angiogenesis

STAT3 activation by LMP1 is particularly important in **NPC** where STAT3 correlates with advanced disease and poor prognosis.

### Downstream oncogenic consequences

**B cell immortalization program:**
1. LMP1 → BCL-2/BCL-XL → block of intrinsic apoptosis → indefinite survival
2. LMP1 → ICAM-1, LFA-3 → adhesion molecule upregulation → improved antigen presentation
3. LMP1 → IL-6 autocrine loop → B cell growth factor
4. LMP1 → TNFR2 upregulation → further NF-κB positive feedback
5. LMP1 → A20 (TNFAIP3; NF-κB target) → limits TNF-induced death → cell survival

**Epithelial cell (NPC) effects:**
- LMP1 → vimentin, E-cadherin loss → epithelial-mesenchymal transition (EMT) → invasive phenotype
- LMP1 → EGFR transactivation via AP-1 → growth advantage
- LMP1 → TGF-β production → immune suppression in NPC microenvironment

### Exosomal LMP1

LMP1 is actively packaged into **exosomes** released by EBV-infected B cells and tumor cells:
- Exosomal LMP1 → taken up by uninfected T cells, NK cells, DCs, and fibroblasts
- **Immunosuppressive**: Exosomal LMP1 → NF-κB activation in T cells → IL-10 production → suppression of anti-EBV CTL response
- **Paracrine signaling**: Exosomal LMP1 → fibroblast activation → TGF-β1 secretion → tumor microenvironment remodeling
- Clinical relevance: LMP1 in plasma exosomes is measurable in PTLD and EBV+ lymphoma patients

## Mechanism

### LMP1 as a driver of Reed-Sternberg cell survival

Reed-Sternberg (RS) cells in EBV+ Hodgkin lymphoma are crippled germinal center B cells that have acquired crippling BCR mutations (non-functional BCR) — cells that would normally be eliminated by apoptosis:
1. EBV LMP1 expression in RS cells → constitutive NF-κB → BCL-2/TRAF1/A20 → survival signal replacing lost BCR
2. LMP1 → IL-13/IL-10/CCL5/TARC (CCL17) secretion → attraction and polarization of surrounding reactive cells (T cells, eosinophils, macrophages)
3. LMP1 → PD-L1 upregulation → immune checkpoint activation → CTL exhaustion → escape from immune surveillance

### LMP1 as a therapeutic target

LMP1 is not directly targetable with current drugs (no extracellular domain for antibody binding; TM domains not conventional targets). Indirect therapeutic approaches:
- **NF-κB inhibitors**: Bortezomib (proteasome inhibitor) → inhibits IκBα degradation → blocks LMP1-driven NF-κB → tested in PTLD and EBV+ DLBCL
- **JAK inhibitors**: Ruxolitinib (JAK1/2) → block LMP1-driven STAT3 → under investigation in EBV+ lymphomas
- **Rituximab (anti-CD20)**: Targets CD20+ B cells in PTLD/EBV-DLBCL; effectively clears EBV-infected B cell population
- **EBV-specific CTL therapy**: Adoptive transfer of LMP1/LMP2-specific CTLs → directly kill latency II/III EBV+ tumor cells; clinical success in PTLD (complete responses in ~70-80% of chemotherapy-naive PTLD)
- **LMP1-directed CAR-T cells**: Extracellular LMP1 loop-targeting CARs — experimental; challenged by limited extracellular accessibility

## Connections

**→ [Epstein-Barr Virus](../../../07-system/epstein-barr-virus/)**: LMP1 is EBV's primary oncoprotein expressed in latency II/III; constitutively active CD40 mimic; TM domain aggregation enables ligand-independent TRAF signaling; drives B cell immortalization, EBV latency III growth program, and lymphomagenesis in Hodgkin lymphoma, NPC, and PTLD.

**→ [NF-κB](../nf-kb/)**: LMP1 CTAR1 → TRAF1/2/3 → NIK → IKKα → p100 → p52/RelB (non-canonical NF-κB); CTAR2 → TRADD → TRAF6 → TAK1 → IKKβ → IκBα degradation → p65/p50 (canonical NF-κB); simultaneous dual-pathway NF-κB activation by one viral protein → BCL-2, ICAM-1, IL-6, CD23, TRAF1 → B cell survival.

**→ [p53](../p53/)**: LMP1 → NF-κB → MDM2 transcription → p53 destabilization; LMP1 → BCL-2/BCL-XL → resistance to p53-dependent apoptosis; EBNA3C (distinct EBV protein) is the primary EBV p53 antagonist (recruits Skp2 E3 ligase → p53 ubiquitination); LMP1 and EBNA3C cooperate to prevent p53-mediated tumor suppression in EBV malignancies.

**→ [TGF-β](../tgf-beta/)**: LMP1 → NF-κB → TGF-β1 transcription in infected B cells and NPC tumor cells; LMP1 can block SMAD2/3 nuclear translocation → prevents TGF-β-induced growth arrest in EBV-infected cells; exosomal LMP1 modulates TGF-β signaling in stromal fibroblasts; TGF-β in EBV+ lymphoma microenvironment is partly LMP1-driven and contributes to immune suppression.

[^wang-1985-lmp1-discovery]: Wang D, Liebowitz D, Kieff E. An EBV membrane protein expressed in immortalized lymphocytes transforms established rodent cells. *Cell.* 1985;43(3 Pt 2):831-840. [doi:10.1016/0092-8674(85)90256-9](https://doi.org/10.1016/0092-8674(85)90256-9) · [PubMed 3000618](https://pubmed.ncbi.nlm.nih.gov/3000618/)
[^mosialos-1995-lmp1-traf]: Mosialos G, Birkenbach M, Yalamanchili R, VanArsdale T, Ware C, Kieff E. The Epstein-Barr virus transforming protein LMP1 engages signaling proteins for the tumor necrosis factor receptor family. *Cell.* 1995;80(3):389-399. [doi:10.1016/0092-8674(95)90489-1](https://doi.org/10.1016/0092-8674(95)90489-1) · [PubMed 7859281](https://pubmed.ncbi.nlm.nih.gov/7859281/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

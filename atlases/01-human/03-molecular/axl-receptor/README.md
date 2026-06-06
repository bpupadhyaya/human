---
schema: human-scale-entry/v1
id: axl-receptor
name: AXL Receptor Tyrosine Kinase
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "TAM family receptor tyrosine kinase (TYRO3/AXL/MERTK) activated by GAS6/Protein S. Mediates efferocytosis, innate immune suppression via SOCS1/3, and serves as viral entry receptor for ZIKA, dengue, Ebola, and other enveloped viruses. Overexpressed in multiple cancers."
aliases: ["AXL", "UFO receptor", "Ark", "Tyro7", "GAS6 receptor"]
sources:
  - id: bhatt-2013-dengue-axl
    type: peer-reviewed
    cite: "Bhatt S, Gething PW, Brady OJ, et al. The global distribution and burden of dengue. Nature. 2013;496(7446):504-507."
    doi: "10.1038/nature12060"
    pmid: "23563266"
  - id: hamel-2015-zika-axl
    type: peer-reviewed
    cite: "Hamel R, Dejarnac O, Wichit S, et al. Biology of Zika virus infection in human skin cells. J Virol. 2015;89(17):8880-8896."
    doi: "10.1128/JVI.00354-15"
    pmid: "26085147"
  - id: lemke-2013-tam-review
    type: peer-reviewed
    cite: "Lemke G, Rothlin CV. Immunobiology of the TAM receptors. Nat Rev Immunol. 2008;8(5):327-336."
    doi: "10.1038/nri2303"
    pmid: "18421305"
  - id: rothlin-2007-tam-immune-homeostasis
    type: peer-reviewed
    cite: "Rothlin CV, Ghosh S, Zuniga EI, Oldstone MB, Lemke G. TAM receptors are pleiotropic inhibitors of the innate immune response. Cell. 2007;131(6):1124-1136."
    doi: "10.1016/j.cell.2007.10.034"
    pmid: "18083102"
cross_links:
  - target: 01-human/04-cellular/dendritic-cell
    relation: expressed-by
    note: "AXL is highly expressed on plasmacytoid and conventional dendritic cells; GAS6-AXL signaling suppresses TLR-driven IFN-I production, enabling immune homeostasis and exploited by viruses."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "AXL/MERTK signaling drives SOCS1/SOCS3 expression, dampening TLR- and cytokine-driven innate immune activation; central to innate immune resolution and tolerance of apoptotic cell clearance."
  - target: 01-human/03-molecular/il-6
    relation: modulates
    note: "AXL activation suppresses TLR-driven IL-6 and TNF-α production via SOCS1/3-mediated JAK/STAT inhibition; viral exploitation of AXL impairs early cytokine responses."
  - target: 01-human/03-molecular/stat3
    relation: modulates
    note: "AXL activates STAT3 via JAK1/2 in cancer cells, promoting survival, EMT, and therapy resistance; AXL-STAT3 axis is a driver of acquired resistance to targeted therapies."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: expressed-by
    note: "AXL is expressed on cardiac endothelium and cardiomyocytes; ZIKA-mediated AXL entry causes direct myocardial injury in fetal and adult cardiac contexts."
  - target: 01-human/07-system/respiratory-system
    relation: modulates
    note: "AXL on alveolar macrophages and endothelial cells mediates efferocytosis of apoptotic cells; SARS-CoV-2 has been proposed to use AXL as an alternative entry receptor in lung cells."
---

# AXL Receptor Tyrosine Kinase

## Overview

AXL (also known as UFO, Ark, or Tyro7) is a **receptor tyrosine kinase** belonging to the **TAM family** — a three-member subfamily (TYRO3, AXL, MERTK) defined by a shared extracellular architecture and the vitamin K-dependent ligands **GAS6** (growth arrest-specific gene 6) and **Protein S**. The TAM receptors were originally identified as regulators of platelet aggregation and cell survival, but their dominant function in modern immunology is as **homeostatic suppressors of innate immunity** — essential brakes on TLR-driven and cytokine-driven inflammation that prevent autoimmunity and resolve acute responses [^lemke-2013-tam-review].

AXL has attracted intense biomedical interest for two converging reasons: (1) it serves as a **viral entry receptor** for multiple clinically important enveloped viruses, including ZIKA virus [^hamel-2015-zika-axl], dengue virus [^bhatt-2013-dengue-axl], Ebola, HIV, and potentially SARS-CoV-2 — a role that depends on its ability to bind phosphatidylserine (PS)-exposing viral envelopes via the ligand GAS6; and (2) it is **overexpressed in a wide range of human cancers** (lung, breast, gastric, AML, glioblastoma) and drives tumor cell survival, epithelial-to-mesenchymal transition (EMT), metastasis, and acquired resistance to kinase inhibitors and immunotherapy.

## Structure

### TAM receptor family comparison

| Receptor | Gene | Preferred ligand | Affinity | Primary expression |
|:---|:---|:---|:---|:---|
| **TYRO3** | *TYRO3* | Protein S > GAS6 | High (Protein S) | CNS neurons, Sertoli cells, platelets |
| **AXL** | *AXL* | GAS6 >> Protein S | High (GAS6: Kd ~1 nM) | Widespread: DCs, monocytes, endothelium, cancer cells |
| **MERTK** | *MERTK* | Protein S > GAS6 | High (Protein S) | Macrophages, retinal pigment epithelium, DCs |

### AXL protein architecture

AXL encodes a **894 amino acid, ~140 kDa** (with glycosylation) type I transmembrane receptor:

**Extracellular domain (ECD):**
- **Two Ig-like domains (IgD1, IgD2)**: Membrane-distal; IgD1 directly contacts GAS6 LG domain; mediates high-affinity GAS6 binding (Kd ~1 nM)
- **Two fibronectin type III (FNIII) domains**: Membrane-proximal; structural support; mediate AXL homo/heterodimerization
- **N-glycosylation sites**: 9 potential sites; glycosylation influences ligand binding and receptor trafficking

**Transmembrane domain**: Single α-helix; hydrophobic (residues ~460–480)

**Intracellular domain (ICD):**
- **Juxtamembrane region**: Contains regulatory phosphorylation sites (Y702, Y703)
- **Kinase domain**: Canonical tyrosine kinase (DFG motif); activation loop Tyr779/Tyr821 bisphosphorylation for full activity
- **C-terminal tail**: SH2 docking sites; Y866 (GRB2), Y779 (PI3K p85), Y821 (Src)

### Ligand — GAS6

GAS6 is a **vitamin K-dependent extracellular protein** (727 aa; ~80 kDa) structurally related to Protein S, consisting of:
- N-terminal Gla domain: Binds phosphatidylserine (PS) on apoptotic cell surfaces; requires vitamin K-dependent γ-carboxylation of Glu residues
- EGF-like domains (4×)
- C-terminal LG (laminin G) domain pair: Directly binds AXL IgD1 (nanomolar affinity)

This bifunctional structure enables GAS6 to act as a **"bridging molecule"**: it simultaneously binds PS on apoptotic cells and AXL on phagocytes, enabling **efferocytosis** (phagocytosis of apoptotic cells). Enveloped viruses exploit this same mechanism — their PS-rich envelopes mimic apoptotic cells, recruiting GAS6 to bridge viral PS to AXL on the host cell surface.

## Function

### Efferocytosis and apoptotic cell clearance

The canonical physiological function of AXL (and MERTK) is to mediate **efferocytosis** — the phagocytic clearance of apoptotic cells before they release pro-inflammatory intracellular contents [^rothlin-2007-tam-immune-homeostasis]:

1. Apoptotic cell exposes PS on the outer leaflet
2. GAS6 (or Protein S) Gla domain binds PS → LG domain recruits AXL on the phagocyte
3. AXL signaling activates Rac1 and cytoskeletal remodeling → phagosome formation → apoptotic cell internalization
4. Post-efferocytosis: AXL drives anti-inflammatory gene expression (IL-10, TGF-β), resolving inflammation

Failure of efferocytosis (AXL/MERTK deficiency) leads to accumulation of secondary necrotic cells and systemic autoimmunity (lupus-like phenotype in triple TAM knockout mice).

### Innate immune suppression

AXL is a **feedback inhibitor of innate immune activation** [^rothlin-2007-tam-immune-homeostasis]:

- TLR/IFN signaling upregulates AXL expression (STAT1-driven transcription)
- GAS6-AXL activation → SOCS1 and SOCS3 induction → JAK1/2 inhibition → attenuated IFN-I and proinflammatory cytokine production
- AXL also suppresses TRIF-dependent TLR4 signaling and type I IFN receptor signaling via SOCS1

This creates a **self-limiting inflammatory circuit**: TLR activation first induces AXL, which then brakes itself. This elegant design is exploited by enveloped viruses — by triggering GAS6-AXL, they suppress the very IFN-I response needed to eliminate them.

### Cancer biology

AXL is overexpressed in >20 cancer types and drives multiple oncogenic programs:
- **Survival**: PI3K/Akt and MEK/ERK activation → resistance to apoptosis
- **EMT and metastasis**: AXL → Twist/Snail → EMT; activates Rho GTPases for invasive migration
- **Immunosuppression in TME**: AXL on tumor-associated macrophages and DCs suppresses T cell activation via SOCS pathway
- **Therapy resistance**: AXL upregulation is a pan-cancer resistance mechanism to EGFR inhibitors (erlotinib/gefitinib), BRAF inhibitors (vemurafenib), anti-HER2 therapy, and checkpoint inhibitors

## Mechanism

### Viral entry via AXL (apoptotic mimicry)

Multiple enveloped viruses exploit the GAS6-AXL efferocytosis pathway for cellular entry [^hamel-2015-zika-axl]:

1. **PS exposure**: Viral envelope contains PS in the outer leaflet (acquired during budding from host cell)
2. **GAS6 bridging**: Plasma GAS6 or locally secreted GAS6 binds viral PS and AXL on the target cell simultaneously
3. **AXL-mediated uptake**: AXL signals to drive endocytosis of virus-GAS6 complex → endosomal acidification → membrane fusion and genome release
4. **IFN-I suppression**: Simultaneously, AXL activation suppresses antiviral IFN-I, giving the virus a critical early advantage

**ZIKA virus (ZIKV)**: AXL is the primary entry receptor for ZIKV in human skin dendritic cells, fibroblasts, and neural progenitor cells [^hamel-2015-zika-axl]. ZIKV tropism for fetal brain neural progenitors (mediating microcephaly) depends substantially on their high AXL expression.

**Dengue virus (DENV)**: AXL (and TYRO3) facilitate DENV entry in skin cells and DCs; AXL-mediated IFN-I suppression is critical for viral dissemination. Dengue's global burden — ~390 million infections/year [^bhatt-2013-dengue-axl] — is partly enabled by this immune evasion.

**Other viruses**: SARS-CoV-2 (alternative AXL-dependent entry), Ebola (NPC1 primary; AXL facilitates), HIV, West Nile, Sindbis.

### Kinase activation cascade

1. GAS6 binding → AXL dimerization (via FNIII domains) → transphosphorylation of activation loop (Y779, Y821)
2. Y779 recruits PI3K p85 → PI3K → PIP3 → PDK1 → Akt (survival, proliferation)
3. Y821 recruits Grb2 → SOS → Ras → MEK → ERK (proliferation, differentiation)
4. Y866 recruits Src → FAK → cytoskeletal remodeling (migration)
5. AXL → SOCS1/3 upregulation → negative feedback on JAK/STAT signaling

## Connections

- `expressed-by` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — high AXL expression mediates viral entry and IFN-I suppression in DCs
- `modulates` → **[Immune System](../../07-system/immune-system/README.md)** — TAM-mediated innate immune homeostasis via SOCS1/3; efferocytosis; resolution of inflammation
- `modulates` → **[IL-6](../il-6/README.md)** — AXL/SOCS1 suppresses TLR-driven IL-6 production; attenuates early inflammatory cytokine response
- `modulates` → **[STAT3](../stat3/README.md)** — AXL activates STAT3 in cancer cells driving survival and EMT; STAT3 reciprocally regulates AXL expression

## Pathology

| Disease | AXL role | Therapeutic implication |
|:---|:---|:---|
| **ZIKA infection / congenital microcephaly** | AXL primary entry receptor in neural progenitors and skin DCs; IFN-I suppression enables viremia | AXL blockade (bemcentinib) as antiviral strategy; in preclinical and early clinical investigation |
| **Dengue fever / DHF** | AXL/TYRO3 facilitate skin-to-DC dissemination; IFN-I suppression amplifies viremia | Pan-AXL/TAM inhibitors being evaluated; DENV vaccines (Dengvaxia, TAK-003) |
| **Ebola** | AXL facilitates macrophage/DC entry; SOCS suppression of IFN-I is catastrophic in hemorrhagic fever | Monoclonal antibodies (Inmazeb); AXL inhibitors adjunctive role under study |
| **Non-small cell lung cancer (NSCLC)** | AXL overexpressed; drives erlotinib/osimertinib resistance via bypass signaling | Bemcentinib + erlotinib trials; cabozantinib (multi-kinase); SXC-9819 |
| **Acute myeloid leukemia (AML)** | AXL overexpressed on AML blasts; promotes survival, evasion of chemotherapy | Gilteritinib (FLT3/AXL inhibitor) — FDA-approved for FLT3+ AML |
| **Glioblastoma** | AXL drives invasion, temozolomide resistance, immune suppression | AXL-targeted ADCs; RNAi-nanoparticle approaches |
| **Autoimmune disease (deficiency)** | TAM triple-knockout → lupus-like syndrome; AXL/MERTK required for tolerance | Paradoxically, AXL inhibitors do not strongly induce autoimmunity in cancer patients (likely compensated by Protein S/MERTK) |
| **COVID-19** | AXL as alternative SARS-CoV-2 entry receptor in ACE2-low cells (lung type II-related); AXL-mediated IFN-I suppression may amplify early viral replication | AXL inhibitors being evaluated in COVID-19 trials |

[^bhatt-2013-dengue-axl]: Bhatt S, Gething PW, Brady OJ, et al. The global distribution and burden of dengue. *Nature.* 2013;496(7446):504-507. [doi:10.1038/nature12060](https://doi.org/10.1038/nature12060) · [PubMed 23563266](https://pubmed.ncbi.nlm.nih.gov/23563266/)
[^hamel-2015-zika-axl]: Hamel R, Dejarnac O, Wichit S, et al. Biology of Zika virus infection in human skin cells. *J Virol.* 2015;89(17):8880-8896. [doi:10.1128/JVI.00354-15](https://doi.org/10.1128/JVI.00354-15) · [PubMed 26085147](https://pubmed.ncbi.nlm.nih.gov/26085147/)
[^lemke-2013-tam-review]: Lemke G, Rothlin CV. Immunobiology of the TAM receptors. *Nat Rev Immunol.* 2008;8(5):327-336. [doi:10.1038/nri2303](https://doi.org/10.1038/nri2303) · [PubMed 18421305](https://pubmed.ncbi.nlm.nih.gov/18421305/)
[^rothlin-2007-tam-immune-homeostasis]: Rothlin CV, Ghosh S, Zuniga EI, Oldstone MB, Lemke G. TAM receptors are pleiotropic inhibitors of the innate immune response. *Cell.* 2007;131(6):1124-1136. [doi:10.1016/j.cell.2007.10.034](https://doi.org/10.1016/j.cell.2007.10.034) · [PubMed 18083102](https://pubmed.ncbi.nlm.nih.gov/18083102/)

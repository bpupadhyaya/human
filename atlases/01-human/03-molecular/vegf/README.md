---
schema: human-scale-entry/v1
id: vegf
name: VEGF
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Primary angiogenic cytokine; VEGF-A binds VEGFR-2 on endothelial cells triggering proliferation, migration, and tube formation. Upregulated by HIF-1α in hypoxia; targeted by bevacizumab in metastatic cancer and ranibizumab in neovascular macular degeneration."
aliases: ["VEGF-A", "vascular endothelial growth factor", "VEGF165", "VEGFR ligand"]
sources:
  - id: ferrara-2003-vegf
    type: peer-reviewed
    cite: "Ferrara N, Gerber HP, LeCouter J. The biology of VEGF and its receptors. Nat Med. 2003;9(6):669-676."
    doi: "10.1038/nm0603-669"
    pmid: "12778165"
    url: "https://doi.org/10.1038/nm0603-669"
  - id: hurwitz-2004-bevacizumab
    type: peer-reviewed
    cite: "Hurwitz H, Fehrenbacher L, Novotny W, et al. Bevacizumab plus irinotecan, fluorouracil, and leucovorin for metastatic colorectal cancer. N Engl J Med. 2004;350(23):2335-2342."
    doi: "10.1056/NEJMoa032691"
    pmid: "15175435"
    url: "https://doi.org/10.1056/NEJMoa032691"
  - id: brown-2006-ranibizumab
    type: peer-reviewed
    cite: "Brown DM, Kaiser PK, Michels M, et al. Ranibizumab versus verteporfin for neovascular age-related macular degeneration. N Engl J Med. 2006;355(14):1432-1444."
    doi: "10.1056/NEJMoa062655"
    pmid: "17021319"
    url: "https://doi.org/10.1056/NEJMoa062655"
cross_links:
  - target: 01-human/04-cellular/endothelial-cell
    relation: modulates
    note: "VEGF-A binds VEGFR-2 (KDR/Flk-1) on endothelial cells — the primary angiogenic signal; downstream signaling (PLCγ→PKC→ERK, PI3K→Akt→eNOS) drives endothelial cell proliferation, survival, migration, and nitric oxide-mediated vasodilation."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "VEGF-A activates eNOS via VEGFR-2→PI3K→Akt signaling → nitric oxide production in endothelial cells → vasodilation and vascular permeability; NO-dependent permeability is a key feature of VEGF-driven tumor vasculature (leaky, dysfunctional vessels)."
  - target: 01-human/06-organ/lung
    relation: modulates
    note: "VEGF-A is highly expressed by type II pneumocytes and is critical for pulmonary vascular maintenance; reduced VEGF signaling contributes to endothelial apoptosis and alveolar destruction in emphysema; VEGF is elevated in the lungs of patients with pulmonary edema."
---

# VEGF

## Overview

**Vascular endothelial growth factor (VEGF-A)**, commonly referred to as simply VEGF, is the **master regulator of angiogenesis** — the formation of new blood vessels from existing vasculature. It is the dominant pro-angiogenic signal in development, wound healing, tissue repair, and tumor growth, acting primarily through its high-affinity receptor **VEGFR-2 (KDR/Flk-1)** on endothelial cells to drive their proliferation, migration, and tube formation [^ferrara-2003-vegf].

The VEGF family comprises five secreted dimeric glycoproteins: **VEGF-A** (the prototypical isoform, usually referred to as "VEGF"), VEGF-B, VEGF-C, VEGF-D, and **PlGF** (placental growth factor). VEGF-A is the dominant angiogenic factor; VEGF-C/D regulate lymphangiogenesis via VEGFR-3.

VEGF has become one of the most therapeutically important molecules in medicine: **anti-VEGF therapy** (bevacizumab, ranibizumab, aflibercept) is a cornerstone of treatment for:
- Metastatic colorectal, lung, breast, and renal cell carcinoma
- Neovascular (wet) age-related macular degeneration (nAMD) and diabetic retinopathy
- Hemangioblastoma (von Hippel-Lindau disease)

## Structure

### VEGF-A gene and isoforms

The human VEGF-A gene (chromosome 6p21.1) contains 8 exons; alternative splicing produces multiple isoforms differing in their heparin-binding affinity and tissue distribution:

| Isoform | AA length | Heparin binding | ECM sequestration | Bioavailability |
|:---|:---|:---|:---|:---|
| VEGF₁₂₁ | 121 | None | None | Freely diffusible |
| VEGF₁₆₅ | 165 | Moderate | Partial (heparan sulfate) | Balanced; dominant form |
| VEGF₁₈₉ | 189 | High | Strongly sequestered | Primarily cell-surface/ECM |
| VEGF₂₀₆ | 206 | High | Strongly sequestered | Primarily ECM |

**VEGF₁₆₅** is the most abundant and biologically potent isoform; it is both diffusible and heparan sulfate-binding, allowing gradient formation and VEGFR-2 signal amplification via co-receptor neuropilin-1 (NRP-1).

VEGF-A is secreted as a **disulfide-linked homodimer** (each monomer ~22-24 kDa); the receptor-binding domain lies in the N-terminal portion; the C-terminal heparin-binding domain determines ECM association.

### VEGF receptors

Three receptor tyrosine kinases (RTKs) mediate VEGF signaling:

- **VEGFR-1 (Flt-1):** High affinity for VEGF-A but weak kinase activity; functions primarily as a **decoy receptor** sequestering VEGF; also on macrophages (VEGF-B/PlGF chemotaxis); soluble sFlt-1 is the major endogenous VEGF inhibitor (elevated in preeclampsia)
- **VEGFR-2 (KDR/Flk-1):** The **primary angiogenic signal transducer**; lower VEGF affinity than VEGFR-1 but superior kinase activity; expressed on endothelial cells, tumor vasculature, and some progenitor cells; dimerizes upon VEGF binding → transphosphorylation → downstream signaling
- **VEGFR-3 (Flt-4):** Binds VEGF-C and VEGF-D; expressed on lymphatic endothelial cells → **lymphangiogenesis**; also expressed on tumor blood vessels in hypoxic regions

## Function

### Angiogenesis: the tip-stalk cell mechanism

VEGF-A drives angiogenesis through coordinated selection of **tip cells and stalk cells** from the existing vascular plexus [^ferrara-2003-vegf]:

1. **Tip cell selection:** Highest VEGF gradient → VEGFR-2 activation → Dll4 expression → Notch1 signaling in adjacent cells → VEGFR-1 upregulation and VEGFR-2 downregulation → stalk cell identity; only the highest-VEGF-sensing cell becomes the tip
2. **Tip cell migration:** VEGF-induced cytoskeletal reorganization (via VEGFR-2→RhoA/Rac1→filopodia extension); tip cells extend filopodia along VEGF gradients
3. **Stalk cell proliferation:** VEGF drives stalk cell proliferation (via VEGFR-2→ERK1/2→cyclin D1) to extend the nascent vessel
4. **Lumen formation:** Pinocytic vacuoles coalesce → lumen; integrins and VE-cadherin organize endothelial junctions
5. **Vessel stabilization:** PDGF-B recruits pericytes → coverage → reduced VEGF-dependence → vessel maturation

**Tumor angiogenesis:** Solid tumors >1-2 mm depend on angiogenesis for oxygen and nutrient supply. HIF-1α-driven VEGF secretion by hypoxic tumor cells creates a chronic pro-angiogenic signal → chaotic, leaky, high-pressure tumor vasculature with arteriovenous shunts → heterogeneous perfusion, hypoxia, elevated interstitial pressure (impairing drug delivery).

### VEGF and vascular permeability

VEGF-A was originally called **"vascular permeability factor" (VPF)** for its ability to rapidly increase vascular permeability:
- VEGFR-2 → Src kinase → VE-cadherin phosphorylation → junction opening → paracellular permeability
- VEGFR-2 → PI3K → Akt → eNOS → NO → cGMP → smooth muscle relaxation + permeability
- VEGFR-2 → PLCγ → PKC → MAPK → transcriptional programs (angiopoietin-2, plasminogen activators)

Consequences: edema in tumors and wounds; macular edema in diabetic retinopathy; pulmonary edema in high-altitude sickness and ARDS (VEGF-A elevated in bronchoalveolar lavage).

### Physiological roles beyond angiogenesis

- **Endothelial survival:** Constitutive VEGFR-2 signaling (via autocrine loops or lumenal VEGF) is required for endothelial cell survival at rest; VEGF withdrawal → endothelial apoptosis
- **Neuroprotection:** VEGF-A has direct neuroprotective effects on motor neurons (VEGFR-2 expressed on neurons); reduced VEGF hypoxia response (polymorphism in VEGF HRE) is associated with ALS susceptibility
- **Bone remodeling:** VEGF promotes osteoblast activity and capillary invasion into cartilage during endochondral ossification

## Mechanism

### HIF-1α-VEGF axis (hypoxic induction)

The primary physiological inducer of VEGF is **hypoxia** acting via HIF-1α:
1. Reduced O₂ → prolyl hydroxylase (PHD) inactivity → VHL cannot bind HIF-1α → HIF-1α stabilizes
2. HIF-1α/HIF-1β dimer binds VEGF hypoxia response element (HRE) in VEGF promoter
3. Transcriptional activation → 10–100-fold increase in VEGF mRNA; VEGF mRNA also stabilized by HIF-2α
4. Resulting VEGF gradient → tip cell selection → sprouting angiogenesis → restored perfusion

Additional VEGF inducers: oncogene activation (Ras→Raf→VEGF); mutant p53 (via VEGF promoter); PI3K/mTOR pathway; COX-2-derived prostaglandins; ROS; mechanical stress.

### Anti-VEGF therapeutics

**Bevacizumab (Avastin, Genentech):** First anti-VEGF antibody approved (2004); humanized anti-VEGF-A IgG1; binds all VEGF-A isoforms → blocks VEGFR-1/2 binding; approved for metastatic colorectal cancer (+ FOLFOX/FOLFIRI), non-squamous NSCLC, glioblastoma, metastatic breast, ovarian, renal cell carcinoma. Overall survival benefit typically modest (2–5 months additional); can normalize tumor vasculature (improves chemotherapy delivery) [^hurwitz-2004-bevacizumab].

**Ranibizumab (Lucentis, Novartis/Genentech):** Anti-VEGF-A Fab fragment (smaller, better ocular penetration); FDA-approved 2006 for neovascular AMD; intravitreal injection every 4–8 weeks; MARINA/ANCHOR trials demonstrated 90% of patients maintained vision vs 60% on PDT [^brown-2006-ranibizumab].

**Aflibercept (Eylea/Zaltrap):** VEGF trap — fusion of VEGFR-1 D2 + VEGFR-2 D3 + Fc; binds VEGF-A, VEGF-B, and PlGF with sub-picomolar affinity; intravitreal for nAMD/DME; IV for colorectal cancer.

**Small molecule VEGFR kinase inhibitors (TKIs):** Sorafenib, sunitinib, pazopanib, cabozantinib — multi-kinase inhibitors blocking VEGFR-2 ATP binding site; used in RCC, hepatocellular carcinoma, thyroid cancer.

**Anti-VEGF resistance mechanisms:** Tumor cells upregulate alternative pro-angiogenic factors (FGF, PDGF, Ang-2) → resistance; hypoxia-independent VEGF production; pericyte-covered "normalized" vessels; tumor cell epithelial-mesenchymal transition.

## Connections

- `acts-on` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — VEGF-A binding to VEGFR-2 is the primary angiogenic signal; endothelial cells respond with tip/stalk cell selection, proliferation, migration, and tube formation — the cellular events underlying new blood vessel growth.
- `connects-to` → **[Nitric Oxide](../nitric-oxide/README.md)** — VEGF activates eNOS via VEGFR-2→PI3K→Akt, producing NO that mediates VEGF-dependent vasodilation and increased vascular permeability; eNOS-derived NO also promotes endothelial cell survival.
- `modulates` → **[Lung](../../06-organ/lung/README.md)** — VEGF-A is essential for pulmonary vascular maintenance; reduced VEGF contributes to emphysema; VEGF elevation drives pulmonary edema in ARDS and high-altitude pulmonary edema.

[^ferrara-2003-vegf]: Ferrara N, Gerber HP, LeCouter J. The biology of VEGF and its receptors. *Nat Med.* 2003;9(6):669-676. [doi:10.1038/nm0603-669](https://doi.org/10.1038/nm0603-669) · [PubMed 12778165](https://pubmed.ncbi.nlm.nih.gov/12778165/)
[^hurwitz-2004-bevacizumab]: Hurwitz H, Fehrenbacher L, Novotny W, et al. Bevacizumab plus irinotecan, fluorouracil, and leucovorin for metastatic colorectal cancer. *N Engl J Med.* 2004;350(23):2335-2342. [doi:10.1056/NEJMoa032691](https://doi.org/10.1056/NEJMoa032691) · [PubMed 15175435](https://pubmed.ncbi.nlm.nih.gov/15175435/)
[^brown-2006-ranibizumab]: Brown DM, Kaiser PK, Michels M, et al. Ranibizumab versus verteporfin for neovascular age-related macular degeneration. *N Engl J Med.* 2006;355(14):1432-1444. [doi:10.1056/NEJMoa062655](https://doi.org/10.1056/NEJMoa062655) · [PubMed 17021319](https://pubmed.ncbi.nlm.nih.gov/17021319/)

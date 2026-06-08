---
schema: human-scale-entry/v1
id: fibronectin
name: Fibronectin
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "Fibronectin (FN1, chr2q35) is a major ECM glycoprotein; plasma FN is a soluble dimer from hepatocytes; cellular FN assembles into insoluble fibrils. Integrin α5β1 and αvβ3 bind via RGD → cell adhesion, migration, and fibrosis. Central provisional matrix scaffold in wound healing."
aliases: ["FN", "FN1", "plasma fibronectin", "cellular fibronectin", "EDA fibronectin", "EDB fibronectin"]
sources:
  - id: hynes-2002-fibronectins
    type: peer-reviewed
    cite: "Hynes RO. Fibronectins. Springer; 1990. Science. 2002;298(5601):2133-2137 (Integrins: bidirectional, allosteric signaling machines review)."
    doi: "10.1126/science.1069806"
    pmid: "12481136"
    url: "https://doi.org/10.1126/science.1069806"
  - id: pankov-2002-fibronectin-review
    type: peer-reviewed
    cite: "Pankov R, Yamada KM. Fibronectin at a glance. J Cell Sci. 2002;115(Pt 20):3861-3863."
    doi: "10.1242/jcs.00059"
    pmid: "12244122"
    url: "https://doi.org/10.1242/jcs.00059"
  - id: wierzbicka-patynowski-2003-fn-assembly
    type: peer-reviewed
    cite: "Wierzbicka-Patynowski I, Schwarzbauer JE. The ins and outs of fibronectin matrix assembly. J Cell Sci. 2003;116(Pt 16):3269-3276."
    doi: "10.1242/jcs.00670"
    pmid: "12840063"
    url: "https://doi.org/10.1242/jcs.00670"
cross_links:
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Plasma FN is cross-linked into fibrin clots → provisional scaffold for platelets, neutrophils, and fibroblasts; cellular FN from fibroblasts drives granulation tissue; FN-integrin α5β1 → fibroblast migration and myofibroblast differentiation → wound contraction and closure."
  - target: 01-human/04-cellular/endothelial-cell
    relation: modulates
    note: "Fibronectin is a major component of the subendothelial basement membrane; endothelial cells secrete FN and adhere to it via integrin α5β1 and αvβ3; FN → endothelial cell migration and tube formation in angiogenesis; plasma FN supports endothelial barrier function."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β → ↑fibronectin transcription (FN1 promoter Smad binding site) and ↑EDA-FN splice isoform in activated fibroblasts; EDA-FN binds TLR4 and integrin α4β7 → amplifies TGF-β-driven fibrogenesis; FN matrix stiffness → mechano-sensing → ↑TGF-β activation → progressive fibrosis."
---

# Fibronectin

## Overview

**Fibronectin (FN)**, encoded by a single gene (*FN1*, chromosome 2q35), is one of the most abundant and multifunctional glycoproteins of the **extracellular matrix (ECM)** and blood plasma. It exists in two principal forms:
- **Plasma fibronectin (pFN):** Soluble disulfide-linked dimer (~440 kDa) secreted predominantly by hepatocytes into blood at ~300 µg/mL; a key component of the provisional ECM at wound sites and in fibrin clots
- **Cellular fibronectin (cFN):** Insoluble fibrillar matrix assembled by fibroblasts, endothelial cells, smooth muscle cells, and other adherent cells; the dominant form in connective tissue and basement membranes; undergoes alternative splicing to include extra domains EDA and EDB [^pankov-2002-fibronectin-review]

FN is a master **cell adhesion and migration** molecule: it contains binding sites for **integrins** (primarily α5β1 and αvβ3 via the RGD motif in type III repeat 10), **collagen/gelatin** (type I repeats), **heparan sulfate/fibrin** (type I/III repeats), and **other ECM proteins**. Through these multi-domain interactions, FN acts as a central scaffold that bridges cells to the ECM, transmits mechanical signals, and orchestrates tissue assembly, wound healing, and fibrosis [^hynes-2002-fibronectins].

**Alternative splicing:** The *FN1* pre-mRNA undergoes extensive alternative splicing at three regions:
- **EDA (extra domain A, type III repeat):** Absent from plasma FN; present in cellular FN; upregulated in wound healing, cancer stroma, and fibrosis; binds TLR4 and integrin α9β1
- **EDB (extra domain B):** Absent from normal adult plasma FN and normal tissue; present only in angiogenic/tumor vasculature and fetal tissue → used as a target for antibody-drug conjugates in cancer (e.g., L19 anti-EDB antibody)
- **IIICS (type III connecting segment):** Variable; contains CS-1 sequence that binds integrin α4β1

**Clinical relevance:** FN is central to wound healing (provisional matrix scaffold), fibrosis (EDA-FN amplifies TGF-β signaling), cancer invasion (FN-integrin signaling promotes EMT and tumor cell migration), and cardiovascular disease (atherosclerotic plaques contain abundant FN; FN-collagen crosslinks determine plaque stability). Plasma FN levels fall in sepsis (FN consumption) and predict clinical outcomes in trauma and critical illness.

## Structure

**Domain architecture (N→C of each monomer):**
Each FN monomer (~250 kDa) is composed of three types of repeating modules:
- **Type I repeats (FNI, 45 aa, ~5 kDa):** 12 per monomer; characteristic double-loop structure stabilized by 2 disulfide bonds; FNI 1-5 bind fibrin and heparin (N-terminal assembly domain); FNI 6-9 bind gelatin/denatured collagen; FNI 10-12 are in the C-terminal dimerization domain
- **Type II repeats (FNII, 60 aa, ~8 kDa):** 2 per monomer; collagen/gelatin-binding domain; also bind heparin
- **Type III repeats (FNIII, 90 aa, ~10 kDa):** 15-17 per monomer (depending on splice variants); β-sheet structure (no disulfide bonds; similar fold to immunoglobulin C2 domains); FNIII7-10 contains the **central cell-binding domain (CCBD)** including the **RGD motif (FNIII10)** for integrin α5β1/αvβ3 binding and PHSRN synergy site (FNIII9) that enhances α5β1 affinity 10-100×
- **C-terminal disulfide knot:** 2 monomers linked by 2 interchain disulfide bonds near the C-terminus → antiparallel dimer; each monomer thus presents two integrin-binding sites

**Key binding sites:**
| Domain | Binding partners |
|:---|:---|
| FNI 1-5 (N-terminal) | Fibrin, heparin/heparan sulfate, F-actin, bacteria (Staphylococcus aureus FnBP) |
| FNI 6-9 + FNII | Collagen types I, II, III, IV (denatured/gelatin) |
| FNIII7-10 (CCBD) | Integrins α5β1, αvβ3, αIIbβ3 via RGD (FNIII10) + PHSRN (FNIII9) |
| EDA domain | TLR4, integrin α4β7, α9β1 |
| FNIII12-14 | Heparin/heparan sulfate (C-terminal heparin-binding domain, HepII) |
| FNI 10-12 | C-terminal fibrin-binding; fibrin cross-linking by FXIIIa (transglutaminase) |

**FN matrix assembly (fibrillogenesis):** [^wierzbicka-patynowski-2003-fn-assembly]
FN fibrillogenesis requires integrin α5β1 engagement:
1. Secreted FN dimers bind integrin α5β1 on the cell surface (CCBD + HepII)
2. Integrin clustering → inside-out activation → actomyosin tension transmitted to FN through the integrin → FN conformational extension (N-terminal FNI modules become accessible)
3. N-terminal FNI of adjacent FN dimers associate head-to-tail → fibril nucleation
4. Fibril elongation → insoluble FN matrix deposition; FXIII cross-links FN to fibrin in wound clots

## Function

**Integrin signaling via fibronectin:**

**α5β1 (fibronectin receptor):**
- Binds RGD (FNIII10) + PHSRN synergy site (FNIII9) → bidirectional signaling
- Intracellular clustering → Talin → kindlin → FAK (focal adhesion kinase) → Src → **Paxillin/vinculin** → stress fiber formation → **focal adhesion** assembly
- FAK → PI3K → Akt (cell survival); FAK → Ras → MEK → ERK (proliferation); FAK → Rac1/Cdc42 → lamellipodia/filopodia (migration)
- **Fibrillar adhesion formation:** After maturation of focal complexes, α5β1-FN fibrillar adhesions form — long streaks aligned with FN fibrils; required for FN fibrillogenesis; key in ECM stiffness mechanosensing (via myosin II tension)

**αvβ3 (vitronectin/RGD receptor):**
- Also binds RGD in FNIII10 (lower affinity than α5β1 for FN but major αvβ3 ligand in angiogenesis); overlapping specificity with vitronectin, osteopontin, thrombospondin, fibrinogen
- αvβ3 → FAK/Src → MAPK → endothelial tip cell motility; important in tumor angiogenesis

**α4β1 binding to EDA-FN:**
- EDA-FN in wound/fibrotic tissue binds α4β1 on monocytes/macrophages → recruitment to sites of fibrosis; also activates TLR4 → NF-κB → pro-inflammatory cytokines

**FN in immunity:**
- Plasma FN coats bacteria (opsonization-like); FN cross-linked to fibrin clots → provisional matrix that traps bacteria and promotes neutrophil/macrophage access
- Staphylococcus aureus and Streptococcus pyogenes express FN-binding proteins (FnBPA, FnBPB, protein F1) → exploit FN as a molecular bridge for internalization into non-phagocytic cells → persistence
- FN sepsis consumption: In gram-negative sepsis, FN is proteolytically degraded → fibronectin deficiency → impaired reticuloendothelial clearance; iv FN supplementation studied as adjunct in neonatal sepsis

**EDA-FN in fibrosis:**
- TGF-β → Smad3 → ↑EDA-FN transcription + ↑fibronectin secretion; EDA-FN stimulates fibroblast TLR4 and integrin α4β7 → ↑TGF-β release (autocrine loop) → myofibroblast differentiation → α-SMA + collagen I production → progressive tissue fibrosis in IPF, NASH, cardiac fibrosis, and CKD

## Mechanism

**FN in wound healing (temporal sequence):**

**Phase 1 (0-24h) — Provisional matrix:**
- Vascular injury → fibrin clot forms; plasma FN cross-linked into clot by FXIIIa (transglutaminase) → fibrin-FN provisional matrix provides structural scaffold and chemotactic gradient
- FN from α-granule degranulation of platelets → local FN deposit at wound edge; platelet α5β1/αIIbβ3 adhere to FN → platelet aggregation amplification
- FN in clot binds PDGF, FGF, fibronectin-binding integrins on neutrophils → neutrophil migration into wound (haptotaxis along FN gradient)

**Phase 2 (1-7 days) — Granulation tissue:**
- Fibroblasts invade provisional matrix via α5β1-FN haptotaxis (sensing of FN gradient) and α5β1-mediated MMP production (MMP-1, -2, -9 cleave FN and collagen I → path-clearing)
- Fibroblast FN secretion → assembly of cellular FN matrix → provides provisional scaffold for collagen I deposition
- FN → fibroblast-to-myofibroblast differentiation: EDA-FN + integrin α5β1 + mechanical tension → α-SMA expression + stress fiber formation → wound contraction
- Endothelial cells use αvβ3/α5β1-FN for angiogenic sprouting into the wound bed → granulation tissue vascularization

**Phase 3 (weeks-months) — Remodeling:**
- As collagen I matrix matures, FN is progressively displaced by collagen cross-links; MMP-2, -9 cleave FN; fibroblast apoptosis; α-SMA downregulation
- In chronic wounds (diabetic ulcers, pressure ulcers): FN is proteolytically degraded by elevated wound fluid proteases (elastase, MMP-8) faster than it can be deposited → deficient provisional matrix → impaired fibroblast migration → healing failure

## Connections

- `connects-to` → **[Wound Healing](../../07-system/wound-healing/README.md)** — Plasma FN is cross-linked into fibrin clots → provisional scaffold for platelets, neutrophils, and fibroblasts; cellular FN from fibroblasts drives granulation tissue; FN-integrin α5β1 → fibroblast migration and myofibroblast differentiation → wound contraction and closure.
- `modulates` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Fibronectin is a major component of the subendothelial basement membrane; endothelial cells secrete FN and adhere to it via integrin α5β1 and αvβ3; FN → endothelial cell migration and tube formation in angiogenesis; plasma FN supports endothelial barrier function.
- `connects-to` → **[TGF-β](../tgf-beta/README.md)** — TGF-β → ↑fibronectin transcription (FN1 promoter Smad binding site) and ↑EDA-FN splice isoform in activated fibroblasts; EDA-FN binds TLR4 and integrin α4β7 → amplifies TGF-β-driven fibrogenesis; FN matrix stiffness → mechano-sensing → ↑TGF-β activation → progressive fibrosis.

[^hynes-2002-fibronectins]: Hynes RO. Integrins: bidirectional, allosteric signaling machines. *Science.* 2002;298(5601):2133-2137. [doi:10.1126/science.1069806](https://doi.org/10.1126/science.1069806) · [PubMed 12481136](https://pubmed.ncbi.nlm.nih.gov/12481136/)
[^pankov-2002-fibronectin-review]: Pankov R, Yamada KM. Fibronectin at a glance. *J Cell Sci.* 2002;115(Pt 20):3861-3863. [doi:10.1242/jcs.00059](https://doi.org/10.1242/jcs.00059) · [PubMed 12244122](https://pubmed.ncbi.nlm.nih.gov/12244122/)
[^wierzbicka-patynowski-2003-fn-assembly]: Wierzbicka-Patynowski I, Schwarzbauer JE. The ins and outs of fibronectin matrix assembly. *J Cell Sci.* 2003;116(Pt 16):3269-3276. [doi:10.1242/jcs.00670](https://doi.org/10.1242/jcs.00670) · [PubMed 12840063](https://pubmed.ncbi.nlm.nih.gov/12840063/)

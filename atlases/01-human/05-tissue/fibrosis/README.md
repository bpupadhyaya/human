---
schema: human-scale-entry/v1
id: fibrosis
name: Fibrosis
atlas: 01-human
scale: 05-tissue
status: draft
last_reviewed: 2026-06-06
summary: "Pathological ECM accumulation (collagen I/III) replacing functional parenchyma. Driven by TGF-β1/SMAD3: injury → macrophage/epithelial TGF-β → myofibroblast activation → collagen deposition. Affects liver, lung, kidney, heart, skin."
aliases: ["fibrosis", "tissue fibrosis", "myofibroblast activation", "pulmonary fibrosis", "hepatic fibrosis", "renal fibrosis"]
sources:
  - id: wynn-2008-fibrosis
    type: peer-reviewed
    cite: "Wynn TA. Cellular and molecular mechanisms of fibrosis. J Pathol. 2008;214(2):199-210."
    doi: "10.1002/path.2277"
    pmid: "18161745"
    url: "https://doi.org/10.1002/path.2277"
  - id: henderson-2020-fibrosis-review
    type: peer-reviewed
    cite: "Henderson NC, Rieder F, Wynn TA. Fibrosis: from mechanisms to medicines. Nature. 2020;587(7835):555-566."
    doi: "10.1038/s41586-020-2938-9"
    pmid: "33239795"
    url: "https://doi.org/10.1038/s41586-020-2938-9"
cross_links:
  - target: 01-human/03-molecular/tgf-beta
    relation: modulated-by
    note: "TGF-β1/SMAD3 is the master pro-fibrotic signal: secreted by macrophages, platelets, and injured epithelial cells, it drives myofibroblast transdifferentiation, collagen I/III synthesis, and inhibits matrix metalloprotease-mediated ECM degradation."
  - target: 01-human/04-cellular/macrophage
    relation: modulated-by
    note: "Macrophages are the primary source of TGF-β1 in fibrotic lesions; M2-polarized macrophages produce pro-fibrotic mediators (TGF-β, PDGF, IL-13) while M1 macrophages drive the initial injury response that initiates fibrogenesis."
  - target: 01-human/04-cellular/fibroblast
    relation: contains
    note: "Activated fibroblasts (myofibroblasts, marked by alpha-smooth muscle actin) are the principal ECM-secreting cells in fibrotic tissue; they arise from resident fibroblasts, epithelial-mesenchymal transition (EMT), and circulating fibrocytes."
  - target: 01-human/03-molecular/surfactant
    relation: connects-to
    note: "SFTPC mutations (L188Q, Δexon4) cause SP-C misfolding → ER stress → type II pneumocyte apoptosis → IPF; TGF-β1 (the master fibrosis driver) suppresses SFTPB/SFTPC transcription; surfactant dysfunction is an early feature of SFTPC-mutation familial IPF."
---

# Fibrosis

## Overview

Fibrosis is the **pathological accumulation of extracellular matrix (ECM)** — predominantly collagen type I and III — within an organ, replacing functional parenchymal cells with scar tissue. It is the common endpoint of chronic tissue injury and dysregulated wound healing, and represents a major global health burden: fibrotic diseases are estimated to account for up to 45% of all deaths in the developed world [^wynn-2008-fibrosis].

Fibrosis occurs in virtually every organ — lung (idiopathic pulmonary fibrosis, IPF), liver (cirrhosis), kidney (chronic kidney disease progression), heart (post-MI cardiac fibrosis), skin (systemic sclerosis/scleroderma), gut (Crohn's disease strictures), and bone marrow (myelofibrosis). The initiating stimulus varies (viruses, alcohol, autoimmunity, mechanical injury, radiation), but the downstream cellular and molecular mechanisms converge on a shared pathway driven predominantly by **TGF-β1** [^henderson-2020-fibrosis-review].

## Structure

### Extracellular Matrix in Fibrosis

In normal tissue, ECM is a dynamic scaffold with tightly regulated composition and turnover. In fibrotic tissue, this balance shifts profoundly:

**Normal interstitial ECM:**
- Collagen I (~65%), collagen III (~15%), fibronectin, laminin, proteoglycans, glycoproteins
- Turnover: matrix metalloproteinases (MMP2, MMP9, MMP13) balanced by tissue inhibitors of metalloproteinases (TIMPs)

**Fibrotic ECM (pathological state):**
- Massive upregulation of collagen I and III deposition (5–15-fold increase in IPF; 10-fold in cirrhosis)
- Increased fibronectin, fibrillin, hyaluronan, versican, periostin
- TIMP overexpression → reduced MMP activity → impaired ECM degradation → net collagen accumulation
- Progressive cross-linking of collagen by lysyl oxidase (LOX) → increased tissue stiffness → mechanosensitive signaling amplifies fibrogenesis (positive feedback loop)

### Myofibroblast — The Effector Cell

The **myofibroblast** is the principal ECM-secreting cell type in all fibrotic tissues. Myofibroblasts are activated fibroblast-lineage cells characterized by:
- Expression of **alpha-smooth muscle actin (αSMA)** — incorporated into contractile stress fibers
- High collagen I, III, and fibronectin secretion
- Expression of PDGF receptors (α and β) — enabling proliferative responses to PDGF
- Reduced sensitivity to apoptosis (sustained in the fibrotic milieu by TGF-β, FAK/PI3K survival signals)

**Origins of myofibroblasts vary by organ:**
| Organ | Myofibroblast origin |
|:---|:---|
| Liver | Hepatic stellate cells (HSCs, activated from quiescent vitamin-A-storing state) |
| Lung | Resident fibroblasts, alveolar epithelial cells (via EMT), pericytes |
| Kidney | Tubular epithelial cells (EMT), pericytes, resident cortical fibroblasts |
| Heart | Cardiac fibroblasts, EndMT from endothelial cells |
| Skin | Dermal fibroblasts, fibrocytes (circulating bone marrow-derived cells) |

## Function

### Normal Wound Healing (Physiological Fibrosis)

Physiological fibrosis is an essential component of normal tissue repair. After injury:

1. **Hemostasis** — platelet activation, provisional fibrin/fibronectin matrix
2. **Inflammatory phase** — neutrophils then macrophages debride dead tissue; pro-inflammatory cytokines (TNF-α, IL-1β) attract fibroblasts
3. **Proliferative phase** — TGF-β1 from macrophages/platelets → fibroblast-to-myofibroblast transition → collagen deposition → wound closure
4. **Remodeling phase** (physiological) — myofibroblast apoptosis, MMP-mediated ECM degradation → restoration of near-normal architecture

**Pathological fibrosis** occurs when this remodeling phase fails — persistent inflammatory stimuli, sustained TGF-β signaling, or myofibroblast resistance to apoptosis maintain ECM deposition indefinitely, resulting in progressive architectural distortion.

### Consequences of Excess ECM Deposition

- **Mechanical stiffening** — collagen crosslinking increases tissue Young's modulus; stiff matrix activates integrin-FAK-YAP/TAZ mechanosensing → further TGF-β release (fibrogenic positive feedback)
- **Parenchymal cell loss** — compressive and ischemic effects of fibrotic scar; hepatocyte loss in cirrhosis; alveolar epithelial cell loss in IPF
- **Vascular dysfunction** — portal hypertension in liver cirrhosis; pulmonary vascular remodeling in IPF; glomerulosclerosis in renal fibrosis
- **Organ failure** — end-stage fibrosis eliminates sufficient functional tissue mass; the mechanism of death in IPF, cirrhosis, CKD

## Connections

- `modulated-by` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — master pro-fibrotic cytokine driving SMAD3-mediated collagen synthesis and myofibroblast activation across all organs
- `modulated-by` → **[Macrophage](../../04-cellular/macrophage/README.md)** — primary source of TGF-β1, PDGF, and IL-13 that initiate and sustain myofibroblast activation
- `contains` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — resident fibroblasts are the primary precursors of activated myofibroblasts and the principal collagen-secreting cells in fibrotic tissue
- `connects-to` → **[Pulmonary Surfactant](../../03-molecular/surfactant/README.md)** — SFTPC mutations cause SP-C misfolding → type II pneumocyte apoptosis → IPF; TGF-β1 suppresses SFTPB/SFTPC transcription; surfactant dysfunction is an early feature of SFTPC-mutation familial IPF.

[^wynn-2008-fibrosis]: Wynn TA. Cellular and molecular mechanisms of fibrosis. *J Pathol.* 2008;214(2):199-210. [doi:10.1002/path.2277](https://doi.org/10.1002/path.2277) · [PubMed 18161745](https://pubmed.ncbi.nlm.nih.gov/18161745/)
[^henderson-2020-fibrosis-review]: Henderson NC, Rieder F, Wynn TA. Fibrosis: from mechanisms to medicines. *Nature.* 2020;587(7835):555-566. [doi:10.1038/s41586-020-2938-9](https://doi.org/10.1038/s41586-020-2938-9) · [PubMed 33239795](https://pubmed.ncbi.nlm.nih.gov/33239795/)

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

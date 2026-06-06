---
schema: human-scale-entry/v1
id: tgf-beta
name: Transforming Growth Factor Beta
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Pleiotropic cytokine superfamily (TGF-β1/2/3) that signals via SMAD2/3 to drive fibrosis, immune tolerance, Treg induction, EMT, and cancer immune evasion. Context-dependent: tumor suppressor early, promoter late in cancer."
aliases: ["TGF-β", "TGF-beta", "TGF-β1", "transforming growth factor beta", "TGFB1"]
sources:
  - id: massague-2012-tgfb-cancer
    type: peer-reviewed
    cite: "Massagué J. TGFβ signalling in context. Nat Rev Mol Cell Biol. 2012;13(10):616-630."
    doi: "10.1038/nrm3434"
    pmid: "22992590"
  - id: derynck-2019-tgfb-review
    type: peer-reviewed
    cite: "Derynck R, Turley SJ, Akhurst RJ. TGFβ biology in cancer progression and immunotherapy. Nat Rev Clin Oncol. 2021;18(1):9-34."
    doi: "10.1038/s41571-020-0403-1"
    pmid: "32710082"
  - id: hinz-2012-fibrosis-tgfb
    type: peer-reviewed
    cite: "Hinz B. Mechanical aspects of lung fibrosis: a spotlight on the myofibroblast. Proc Am Thorac Soc. 2012;9(3):137-147."
    doi: "10.1513/pats.201202-017AW"
    pmid: "22802287"
  - id: chen-2016-treg-tgfb
    type: peer-reviewed
    cite: "Chen W, Konkel JE. Development of thymic Foxp3(+) regulatory T cells: TGF-β matters. Eur J Immunol. 2015;45(4):958-965."
    doi: "10.1002/eji.201444999"
    pmid: "25678205"
cross_links:
  - target: 01-human/03-molecular/il-6
    relation: modulates
    note: "TGF-β together with IL-6 drives Th17 differentiation; in the absence of IL-6, TGF-β alone induces Foxp3+ Treg polarization — context-dependent immune fate decision."
  - target: 01-human/03-molecular/nf-kb
    relation: modulates
    note: "TGF-β/SMAD3 can suppress NF-κB-driven inflammatory gene transcription; crosstalk is context-dependent and cell-type-specific."
  - target: 01-human/03-molecular/cortisol
    relation: modulated-by
    note: "Glucocorticoids suppress TGF-β signaling partially via GR-SMAD interaction; used therapeutically to reduce TGF-β-driven fibrosis in some contexts."
  - target: 01-human/04-cellular/t-helper-cell
    relation: modulates
    note: "TGF-β is the master inducer of Foxp3+ Treg differentiation from naive CD4+ T cells (with retinoic acid in gut); also promotes Th17 polarization when co-present with IL-6."
  - target: 01-human/04-cellular/dendritic-cell
    relation: modulates
    note: "TGF-β induces tolerogenic dendritic cell phenotype (reduced MHC-II, IL-12 production), suppressing antigen-specific T cell priming in tumor and mucosal environments."
  - target: 01-human/06-organ/lung
    relation: modulates
    note: "TGF-β1 is the central driver of pulmonary fibrosis (IPF): activates lung myofibroblasts, induces collagen I/III deposition, promotes EMT of alveolar epithelial cells."
  - target: 01-human/06-organ/kidney
    relation: modulates
    note: "TGF-β1 drives renal fibrosis in CKD: mesangial expansion, tubular EMT, interstitial myofibroblast activation, and glomerulosclerosis."
  - target: 01-human/06-organ/liver
    relation: modulates
    note: "TGF-β1 produced by Kupffer cells activates hepatic stellate cells into collagen-secreting myofibroblasts, the primary driver of hepatic fibrosis in NASH and chronic hepatitis."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "TGF-β is a master immune-regulatory cytokine: suppresses NK cells, B cell differentiation, macrophage activation, and cytotoxic T cell responses in tumors and mucosal tissues."
  - target: 01-human/03-molecular/stat3
    relation: modulates
    note: "TGF-β/SMAD signaling interacts with STAT3 pathway in cancer cells to drive EMT and metastatic programming; both pathways converge in cancer-associated fibroblasts."
---

# Transforming Growth Factor Beta (TGF-β)

## Overview

Transforming Growth Factor Beta (TGF-β) is a **pleiotropic cytokine** belonging to the TGF-β superfamily — a large evolutionary conserved group that includes BMPs, activins, GDFs, and inhibins. Three TGF-β isoforms exist in mammals (TGF-β1, TGF-β2, TGF-β3), of which **TGF-β1** is the predominant and best-characterized form in immunity and fibrosis.

TGF-β occupies a unique position in cell biology: it is simultaneously a potent **tumor suppressor** (in normal epithelia and early tumorigenesis), an indispensable driver of **immune tolerance** (via Treg induction and immune suppression), and a master **pro-fibrotic signal** (inducing myofibroblast differentiation and extracellular matrix deposition across virtually every organ). This context-dependency, elegantly reviewed by Massagué [^massague-2012-tgfb-cancer], makes TGF-β one of the most complex and therapeutically challenging targets in medicine.

The clinical relevance of TGF-β spans an enormous range: from idiopathic pulmonary fibrosis (IPF) and liver cirrhosis to tumor immune evasion, allograft tolerance, and autoinflammatory disease. Anti-TGF-β therapies are under active investigation for fibrosis and cancer, with recent approval of TGF-β pathway inhibitors in combination with checkpoint blockade.

## Structure

### Isoforms and gene products

| Isoform | Gene | Chr | Primary expression | Knockout phenotype |
|:---|:---|:---|:---|:---|
| **TGF-β1** | *TGFB1* | 19q13.2 | Ubiquitous; immune cells, platelets | Multifocal inflammatory disease; autoimmunity; early lethality |
| **TGF-β2** | *TGFB2* | 1q41 | Heart, lung, kidney, neural | Cardiac, skeletal, neural defects |
| **TGF-β3** | *TGFB3* | 14q24.3 | Lung, palate, dermis | Cleft palate; pulmonary defects |

### Protein structure and latency

TGF-β is secreted as a **latent complex** — a critical regulatory mechanism:

1. **Mature TGF-β** (12.5 kDa monomer → 25 kDa homodimer, disulfide-linked): The biologically active cytokine, member of the cystine-knot superfamily with characteristic 9-cysteine pattern
2. **Latency-associated peptide (LAP)**: Non-covalently shields the mature domain; constitutes the "small latent complex" (SLC) = LAP + mature TGF-β
3. **Latent TGF-β binding proteins (LTBPs 1–4)**: Covalently (disulfide) link LAP to ECM via fibrillin; constitute the "large latent complex" (LLC)

**Activation of latent TGF-β** is the rate-limiting step and occurs via:
- **Integrin αvβ6 / αvβ8**: Mechanical force on the LAP RGD motif releases mature TGF-β (key in lung and gut epithelium)
- **Matrix metalloproteases** (MMP2, MMP9, MMP13): Proteolytic cleavage of LAP
- **Thrombospondin-1 (TSP-1)**: LSKL sequence interaction with LAP; major physiological activator
- **Reactive oxygen species / low pH**: Oxidative LAP cleavage in tumor/inflammation contexts
- **Furin-like convertases**: Process pro-TGF-β in the trans-Golgi

## Function

TGF-β exerts profoundly different effects depending on cell type, developmental stage, and inflammatory context:

### Fibrosis and wound healing

| Cell type | TGF-β effect | Outcome |
|:---|:---|:---|
| **Fibroblasts / myofibroblasts** | Transdifferentiation (↑αSMA, ↑collagen I/III, ↑fibronectin) | Scarring, fibrosis |
| **Epithelial cells** | EMT induction (↓E-cadherin, ↑vimentin, ↑N-cadherin) | Fibrosis amplification; metastatic priming |
| **Endothelial cells** | EndMT; angiostasis in advanced fibrosis | Impaired tissue repair, vessel rarefaction |
| **Macrophages** | M2 polarization; reduced pro-inflammatory cytokine production | Anti-inflammatory in wound closure |

### Immune regulation

TGF-β is an essential immune-regulatory cytokine [^chen-2016-treg-tgfb]:
- **Treg induction**: TGF-β + retinoic acid (gut context) → Foxp3+ pTreg differentiation from naive CD4+ T cells via SMAD3-driven *Foxp3* promoter activation
- **Th17 polarization**: TGF-β + IL-6 → RORγt+ Th17 cells (inflammatory context)
- **Cytotoxic T cell suppression**: Reduces granzyme B, perforin, and IFN-γ production by CD8+ T cells
- **NK cell suppression**: Reduces NK cytotoxicity and IFN-γ; major mechanism of tumor immune evasion
- **B cell class switching**: Drives IgA class switching in Peyer's patches (with IL-10)

### Cancer — dual role

TGF-β shows a **stage-dependent "TGF-β paradox" in cancer** [^massague-2012-tgfb-cancer]:
- **Early/normal epithelium**: Tumor-suppressive (growth arrest via p21/p15 upregulation, apoptosis induction)
- **Advanced tumors**: Pro-tumorigenic (immune evasion via Treg expansion, NK/CD8 suppression; EMT and metastasis; cancer-associated fibroblast activation)

## Mechanism

### Canonical SMAD signaling

1. **Ligand binding**: TGF-β homodimer binds TβRII (constitutively active kinase) → TβRI (ALK5) is recruited and transphosphorylated in the GS domain (Ser/Thr-rich)
2. **R-SMAD phosphorylation**: Activated TβRI phosphorylates SMAD2 and SMAD3 at C-terminal SxS motif
3. **SMAD complex formation**: p-SMAD2/3 associates with SMAD4 → trimeric complex translocates to nucleus
4. **Transcriptional regulation**: SMAD complex binds SMAD-binding elements (SBE: GTCT/AGAC) with co-factors (AP-1, Sp1, Snail, Twist, FOXP3); drives fibrotic, immune-regulatory, or anti-proliferative gene programs
5. **Inhibitory feedback**: I-SMADs (SMAD6, SMAD7) are TGF-β target genes that compete with R-SMADs for TβRI binding and recruit SMURF ubiquitin ligases to degrade receptor complexes

### Non-SMAD (non-canonical) pathways

TGF-β also activates (depending on context):
- **MAP kinases**: ERK, JNK, p38 (via ShcA/Grb2 or TRAF6/TAK1)
- **PI3K/Akt/mTOR**: Promotes cell survival and EMT
- **Rho GTPases (RhoA, Cdc42)**: Cytoskeletal remodeling, EMT
- **FAK/Src**: Focal adhesion dynamics during fibroblast activation

### Regulation by TβRIII (betaglycan) and endoglin

TβRIII (betaglycan) is a co-receptor that presents TGF-β2 (low-affinity TβRII ligand) to the signaling complex, dramatically enhancing TGF-β2 potency. Endoglin (TβRIII homolog expressed on endothelial cells) modulates TGF-β signaling toward ALK1 (BMP-like, pro-angiogenic) rather than ALK5 (fibrotic). Mutations in endoglin cause hereditary hemorrhagic telangiectasia (HHT).

## Connections

- `modulates` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — master inducer of Foxp3+ Tregs; co-drives Th17 with IL-6
- `modulates` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — tolerogenic DC phenotype induction; suppresses IL-12 and T cell priming
- `modulates` → **[Lung](../../06-organ/lung/README.md)** — central driver of IPF and alveolar EMT; major ARDS-related fibroproliferative signal
- `modulates` → **[Kidney](../../06-organ/kidney/README.md)** — drives renal fibrosis in CKD; major mediator of diabetic glomerulosclerosis
- `modulates` → **[Liver](../../06-organ/liver/README.md)** — hepatic stellate cell activation; cirrhosis driver
- `modulates` → **[Immune System](../../07-system/immune-system/README.md)** — master immune tolerance regulator

## Pathology

| Disease | TGF-β role | Clinical/therapeutic implication |
|:---|:---|:---|
| **Idiopathic pulmonary fibrosis (IPF)** | TGF-β1 from alveolar macrophages → myofibroblast activation → irreversible lung fibrosis | Pirfenidone (anti-TGF-β mechanism); nintedanib (PDGFR/VEGFR/FGFR kinase inhibitor) |
| **Liver cirrhosis (NASH, HCV, EtOH)** | Kupffer cell TGF-β → hepatic stellate cell (HSC) activation → collagen deposition | TGF-β receptor inhibitors in clinical trials (galunisertib) |
| **Renal fibrosis / CKD** | Tubular TGF-β1 → EMT → interstitial fibroblast activation → progressive nephron loss | ACE inhibitors/ARBs reduce TGF-β output; anti-TGF-β Ab (fresolimumab) in trials |
| **Systemic sclerosis (scleroderma)** | Sustained TGF-β overactivation → widespread fibrosis of skin, lungs, gut, kidney | Nintedanib approved; anti-TGF-β strategies being investigated |
| **Cancer immune evasion** | Tumor-derived TGF-β suppresses CD8+ T cells, NK cells; expands Tregs in TME [^derynck-2019-tgfb-review] | Anti-TGF-β × anti-PD-L1 bispecifics (bintrafusp alfa); TβRI kinase inhibitors (vactosertib) |
| **Marfan syndrome** | FBN1 mutations impair LTBP binding → uncontrolled TGF-β activation in aortic wall | Losartan (AT1R blocker reduces TGF-β signaling) in trials |
| **Camurati-Engelmann disease** | Gain-of-function *TGFB1* mutations → excessive bone sclerosis | Anti-TGF-β antibodies; losartan |

[^massague-2012-tgfb-cancer]: Massagué J. TGFβ signalling in context. *Nat Rev Mol Cell Biol.* 2012;13(10):616-630. [doi:10.1038/nrm3434](https://doi.org/10.1038/nrm3434) · [PubMed 22992590](https://pubmed.ncbi.nlm.nih.gov/22992590/)
[^derynck-2019-tgfb-review]: Derynck R, Turley SJ, Akhurst RJ. TGFβ biology in cancer progression and immunotherapy. *Nat Rev Clin Oncol.* 2021;18(1):9-34. [doi:10.1038/s41571-020-0403-1](https://doi.org/10.1038/s41571-020-0403-1) · [PubMed 32710082](https://pubmed.ncbi.nlm.nih.gov/32710082/)
[^hinz-2012-fibrosis-tgfb]: Hinz B. Mechanical aspects of lung fibrosis: a spotlight on the myofibroblast. *Proc Am Thorac Soc.* 2012;9(3):137-147. [doi:10.1513/pats.201202-017AW](https://doi.org/10.1513/pats.201202-017AW) · [PubMed 22802287](https://pubmed.ncbi.nlm.nih.gov/22802287/)
[^chen-2016-treg-tgfb]: Chen W, Konkel JE. Development of thymic Foxp3(+) regulatory T cells: TGF-β matters. *Eur J Immunol.* 2015;45(4):958-965. [doi:10.1002/eji.201444999](https://doi.org/10.1002/eji.201444999) · [PubMed 25678205](https://pubmed.ncbi.nlm.nih.gov/25678205/)

---
schema: human-scale-entry/v1
id: osteopontin
name: Osteopontin
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "Osteopontin (OPN/SPP1) is a phosphoprotein DAMPs secreted by macrophages, osteoclasts, and tubular epithelium; integrin αvβ3/CD44 → NF-κB → fibrosis and inflammation; urinary OPN is a CKD progression biomarker; OPN promotes kidney stone formation and renal tubular repair."
aliases: ["osteopontin", "OPN", "SPP1", "secreted phosphoprotein 1", "bone sialoprotein-1", "eta-1", "urinary OPN", "CD44 ligand"]
cross_links:
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "OPN is upregulated in injured renal tubular epithelium → integrin αvβ3 on macrophages → macrophage recruitment and pro-inflammatory activation → tubulointerstitial fibrosis; urinary OPN predicts CKD progression; OPN inhibits calcium oxalate crystal adhesion (stone inhibitor)."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "OPN and TGF-β1 are co-expressed in activated macrophages and fibrotic tissue; OPN → integrin αvβ3 → FAK → NF-κB → TGF-β1 production; TGF-β1 → SMAD3 → OPN gene transcription (reciprocal amplification loop); combined OPN + TGF-β1 drives renal and hepatic fibrosis."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "Osteoclasts constitutively express OPN; OPN binds integrin αvβ3 on osteoclasts → formation of the sealing zone (actin ring) essential for bone resorption; OPN knockout mice show impaired osteoclast function and resistance to bone loss; OPN also anchors osteoclasts to bone matrix."
  - target: 01-human/07-system/multiple-sclerosis
    relation: connects-to
    note: "OPN is highly elevated in CSF and serum of MS patients; OPN promotes Th1/Th17 polarization via CD44 → IL-12 and IL-17; OPN inhibits apoptosis of autoreactive T cells; serum OPN correlates with MS relapse rate and MRI lesion burden."
sources:
  - id: denhardt-1993-osteopontin
    type: peer-reviewed
    cite: "Denhardt DT, Guo X. Osteopontin: a protein with diverse functions. FASEB J. 1993;7(15):1475-1482."
    doi: "10.1096/fasebj.7.15.8262332"
    pmid: "8262332"
    url: "https://doi.org/10.1096/fasebj.7.15.8262332"
  - id: wolak-2014-opn-ckd
    type: peer-reviewed
    cite: "Wolak T. Osteopontin — a multi-modal marker and mediator in atherosclerotic vascular disease. Atherosclerosis. 2014;236(2):327-337."
    doi: "10.1016/j.atherosclerosis.2014.07.004"
    pmid: "25104542"
    url: "https://doi.org/10.1016/j.atherosclerosis.2014.07.004"
---

# Osteopontin

## Overview

**Osteopontin (OPN)** (gene *SPP1* — secreted phosphoprotein 1, chromosome 4q22.1) is a **highly phosphorylated, non-collagenous acidic glycoprotein** (~41 kDa protein backbone, post-translationally modified to 44–75 kDa) expressed constitutively in **bone, kidney, macrophages, and dendritic cells**, and inducibly in **activated T cells, osteoclasts, vascular smooth muscle, and cancer cells**. First identified as a bone matrix protein (hence "osteopontin" = bone bridge), it is now recognized as a **multifunctional integrin ligand, macrophage cytokine, and anti-biomineralization inhibitor** with critical roles in inflammation, fibrosis, immunity, and stone disease [^denhardt-1993-osteopontin].

OPN has no single defining function but is best understood as a **molecular hub that links mechanical, metabolic, and inflammatory signals to integrin-mediated cell behavior**. Its central structural feature is an **RGD (Arg-Gly-Asp) integrin-binding motif** flanked by phosphoserine clusters — enabling simultaneous binding to integrins (αvβ3, αvβ1, α8β1, α9β1) and to CD44 — which allows it to coordinate cell attachment, migration, and survival across diverse tissue contexts.

**Three major biological contexts:**
1. **Bone and mineral metabolism:** OPN anchors osteoclasts to bone matrix (via αvβ3 sealing zone); inhibits calcium salt precipitation → kidney stone prevention; regulated by calcitriol
2. **Macrophage-driven inflammation and fibrosis:** Macrophage OPN amplifies NF-κB/TGF-β signaling → renal, hepatic, and pulmonary fibrosis
3. **Immune modulation:** OPN → Th1/Th17 polarization via CD44/IL-12; anti-apoptotic for T cells → autoimmune disease amplification (MS, SLE, RA)

## Structure

**Domain organization (OPN mature protein, ~301 aa after signal peptide cleavage):**

**N-terminal signal peptide (aa 1–16):** Directs ER entry; cleaved → secreted OPN

**N-terminal thrombin cleavage site (aa 167–168, Arg-Ser):** Thrombin cleaves OPN into:
- **N-OPN (aa 1–167):** Contains RGD, SVVYGLR (αvβ3/α9β1 binding), and the primary CD44 epitope
- **C-OPN (aa 168–301):** Contains a second CD44-binding region (ELVTDFPTDLPAT); retained in bone matrix

**Key motifs:**
- **RGD (Arg-Gly-Asp, aa 159–161):** Canonical integrin-binding motif; binds αvβ3, αvβ1, αvβ5, α8β1 with Kd 0.1–1 μM; blocked by cilengitide (integrin antagonist) and echistatin (RGD peptide from snake venom)
- **SVVYGLR (aa 162–168):** Cryptic integrin-binding motif exposed only in thrombin-cleaved N-OPN; uniquely binds α9β1 and α4β1 (key for macrophage chemotaxis and angiogenesis)
- **Phosphoserine clusters (multiple Ser residues, ≥29 phosphorylation sites):** Highly acidic; binds calcium and hydroxyapatite; inhibits calcium oxalate and calcium phosphate crystal growth — the stone-inhibitory mechanism
- **Heparin-binding domain:** Binds CD44 and heparan sulfate proteoglycans

**Post-translational modifications (critical for function):**
- **Phosphorylation** (Ser, Thr): by CK2, CKII, FAM20C; ~29 sites in human OPN; regulates hydroxyapatite affinity and integrin binding; calcitriol induces FAM20C → increased OPN phosphorylation → increased stone inhibition in the kidney
- **Glycosylation** (N- and O-linked): Asn76 (N-glycosylation); multiple O-sites; affects serum stability and CD44 affinity
- **Sialylation:** Modulates negative charge and integrin binding selectivity

## Function

**Bone and mineral homeostasis:**
- Osteoclasts constitutively express high OPN; OPN → integrin αvβ3 on osteoclast ruffled border → Syk → RhoA → actin ring (sealing zone) formation → essential for lacunar resorption; OPN also recruits osteoclast precursors to bone surfaces
- OPN in mineralized matrix: phospho-OPN binds nucleating calcium phosphate crystals → inhibits hydroxyapatite crystal growth → limits uncontrolled mineralization and keeps bone mineralization spatially organized
- OPN knockout mice develop abnormal bone (larger hydroxyapatite crystals; impaired repair response) confirming its role in matrix organization
- Calcitriol (1,25-OH₂D₃) is a potent inducer of OPN transcription via VDR in renal tubular cells and osteoblasts → this links Vitamin D status to stone risk and bone matrix OPN content

**Renal tubular functions and kidney stones:**
- Distal tubular cells constitutively secrete OPN into the tubular lumen → urinary OPN is the primary inhibitor of calcium oxalate (CaOx) and calcium phosphate crystal adhesion to tubular epithelium
- OPN phosphoserine clusters bind CaOx crystal surfaces → inhibit crystal growth and aggregation → reduce stone nucleation and attachment
- In CKD: tubular injury → OPN upregulation → paradoxical macrophage recruitment (pro-fibrotic) but also promotes tubular repair (OPN → CD44 → tubular cell survival and proliferation)
- Urinary OPN levels reflect tubular injury severity → biomarker of CKD progression

**Macrophage activation and fibrosis:**
1. Tissue injury → macrophages upregulate OPN in response to M-CSF, IL-1β, TGF-β, LPS, and calcium (all stimulate OPN transcription)
2. Secreted OPN → autocrine/paracrine → αvβ3 and CD44 on macrophages → PI3K → Akt → NF-κB → TNF-α, IL-6, IL-12 production → sustained inflammation
3. OPN → αvβ3 → FAK → Src → NF-κB → TGF-β1 production; TGF-β1 → SMAD3 → OPN promoter → amplification loop
4. Macrophage OPN → promotes myofibroblast differentiation → collagen I/III deposition → fibrosis in kidney, liver, and lung

**Immune function — Th1/Th17 polarization:**
- Dendritic cells secrete OPN in response to TLR4 signaling; OPN → CD44 on naive T cells → IL-12 induction → Th1 polarization (IFN-γ)
- OPN → anti-apoptotic in T cells (Bcl-xL upregulation via CD44 → PI3K/Akt) → prolongs autoreactive T cell survival → autoimmune disease amplification
- OPN → IL-17 production from CD4+ T cells → Th17 pathology in MS and SLE
- B cells: OPN → CD44 → B cell survival and antibody class switching → autoantibody production (SLE association)

## Mechanism

**OPN in CKD — tubulointerstitial fibrosis pathway:**

1. Tubular epithelial injury (hypoxia, proteinuria, crystals, toxins) → HIF-1α and NF-κB → OPN transcription in tubular cells
2. Tubular OPN is secreted apically (into urine) AND basolaterally (into interstitium)
3. Interstitial OPN → αvβ3 on interstitial macrophages → macrophage chemotaxis and activation → M1/M2 mixed phenotype → TNF-α, IL-1β, TGF-β1 → tubular apoptosis and fibroblast activation
4. TGF-β1 → fibroblast → myofibroblast → collagen deposition → interstitial fibrosis → further nephron loss
5. Urinary OPN reflects tubular OPN secretion proportional to tubular injury → CKD progression biomarker

**OPN in kidney stone disease:**
- Normal: distal tubule OPN → urine OPN >15 μg/mmol creatinine → inhibits CaOx adhesion to tubular epithelium
- Low urinary OPN (genetic deficiency, low calcitriol): reduced crystal inhibition → CaOx adhesion → tubular injury → inflammation → stone nidus
- OPN knockout mice develop spontaneous calcium oxalate crystals in kidney tubules under stone-promoting conditions
- Clinical: urinary OPN is lower in recurrent stone formers vs. non-formers — supports a protective/deficit model

**OPN in atherosclerosis [^wolak-2014-opn-ckd]:**
- Macrophage-derived OPN accumulates in atherosclerotic plaques; OPN → αvβ3 on VSM cells → VSM migration into intima; OPN promotes MMP-2 and MMP-9 secretion → plaque destabilization
- Elevated plasma OPN correlates with coronary artery disease severity and plaque vulnerability; OPN is enriched in calcified plaques (inhibits calcification at normal concentrations; overwhelmed in severe disease)

**OPN in multiple sclerosis:**
- OPN is 5–10× elevated in CSF during MS relapses vs. remission; produced by activated microglia, macrophages, and astrocytes at lesion borders
- OPN promotes Th17 differentiation → IL-17 → BBB disruption → amplifies CNS inflammation
- OPN anti-apoptotic effect → autoreactive T cell accumulation in CNS plaques → lesion persistence
- Genetic studies: *SPP1* promoter variant (rs11730582) associated with MS susceptibility and relapse rate

## Connections

OPN is upregulated in injured renal tubular epithelium → integrin αvβ3 on macrophages → macrophage recruitment and pro-inflammatory activation → tubulointerstitial fibrosis; urinary OPN predicts CKD progression; OPN inhibits calcium oxalate crystal adhesion (stone inhibitor).

OPN and TGF-β1 are co-expressed in activated macrophages and fibrotic tissue; OPN → integrin αvβ3 → FAK → NF-κB → TGF-β1 production; TGF-β1 → SMAD3 → OPN gene transcription (reciprocal amplification loop); combined OPN + TGF-β1 drives renal and hepatic fibrosis.

Osteoclasts constitutively express OPN; OPN binds integrin αvβ3 on osteoclasts → formation of the sealing zone (actin ring) essential for bone resorption; OPN knockout mice show impaired osteoclast function and resistance to bone loss; OPN also anchors osteoclasts to bone matrix.

OPN is highly elevated in CSF and serum of MS patients; OPN promotes Th1/Th17 polarization via CD44 → IL-12 and IL-17; OPN inhibits apoptosis of autoreactive T cells; serum OPN correlates with MS relapse rate and MRI lesion burden.

[^denhardt-1993-osteopontin]: Denhardt DT, Guo X. Osteopontin: a protein with diverse functions. *FASEB J.* 1993;7(15):1475-1482. [doi:10.1096/fasebj.7.15.8262332](https://doi.org/10.1096/fasebj.7.15.8262332) · [PubMed 8262332](https://pubmed.ncbi.nlm.nih.gov/8262332/)
[^wolak-2014-opn-ckd]: Wolak T. Osteopontin — a multi-modal marker and mediator in atherosclerotic vascular disease. *Atherosclerosis.* 2014;236(2):327-337. [doi:10.1016/j.atherosclerosis.2014.07.004](https://doi.org/10.1016/j.atherosclerosis.2014.07.004) · [PubMed 25104542](https://pubmed.ncbi.nlm.nih.gov/25104542/)

---
schema: human-scale-entry/v1
id: rankl
name: RANKL
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "RANKL (TNFSF11, chr13q14) is a TNF family ligand driving osteoclastogenesis; RANK → TRAF6 → NF-κB → NFATc1 → osteoclast differentiation; OPG is the decoy receptor; denosumab (anti-RANKL) reduces vertebral fractures 68% (FREEDOM) and prevents bone metastasis skeletal events."
aliases: ["RANKL", "TNFSF11", "TRANCE", "ODF", "OPGL", "SOFA", "CD254", "osteoclast differentiation factor"]
cross_links:
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "RANKL → RANK on osteoclast precursors → NFATc1 → osteoclast differentiation → bone resorption; estrogen deficiency → RANKL surge → postmenopausal bone loss; denosumab (anti-RANKL) reduces vertebral fractures 68% and hip fractures 40% (FREEDOM trial 3-year)."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "RANKL is the essential differentiation signal for osteoclasts: RANK → TRAF6 → NF-κB + AP-1 → NFATc1 → c-Fos, cathepsin K, TRAP gene programs → mature osteoclasts; OPG decoy receptor blocks RANKL; denosumab mimics OPG with superior binding affinity and bone protection."
  - target: 01-human/07-system/multiple-myeloma
    relation: connects-to
    note: "MM cells produce RANKL → osteoclast activation → osteolytic lesions; MM cells express OPG receptors (TRAIL-decoy function → MM survival); Xgeva (denosumab 120 mg Q4W) reduces skeletal-related events in MM patients with bone disease."
sources:
  - id: lacey-1998-rankl
    type: peer-reviewed
    cite: "Lacey DL, Timms E, Tan HL, et al. Osteoprotegerin ligand is a cytokine that regulates osteoclast differentiation and activation. Cell. 1998;93(2):165-176."
    doi: "10.1016/S0092-8674(00)81569-X"
    pmid: "9568710"
    url: "https://doi.org/10.1016/S0092-8674(00)81569-X"
  - id: cummings-2009-denosumab-freedom
    type: peer-reviewed
    cite: "Cummings SR, San Martin J, McClung MR, et al. Denosumab for prevention of fractures in postmenopausal women with osteoporosis. N Engl J Med. 2009;361(8):756-765."
    doi: "10.1056/NEJMoa0809493"
    pmid: "19671655"
    url: "https://doi.org/10.1056/NEJMoa0809493"
cross_links:
  - target: 01-human/07-system/ankylosing-spondylitis
    relation: connects-to
    note: "In AS, entheseal IL-17A + TNF-α upregulate RANKL on stromal cells → osteoclast-mediated bone erosion at sacroiliac joints and vertebral corners; subsequent WNT-driven syndesmophyte formation leads to ankylosis; denosumab reduces erosion but does not prevent new bone formation."
---

# RANKL

## Overview

**RANKL** (receptor activator of NF-κB ligand; gene *TNFSF11*, chromosome 13q14.11) is a **type II transmembrane protein of the TNF superfamily** that functions as the **essential and sufficient signal for osteoclast differentiation** from mononuclear precursors — making it the master regulator of bone resorption. Also known as TRANCE (TNF-related activation-induced cytokine), OPGL (osteoprotegerin ligand), and ODF (osteoclast differentiation factor), it was discovered simultaneously by multiple groups in 1997-1998 [^lacey-1998-rankl] while searching for the unknown osteoclastogenesis signal that could be blocked by OPG (osteoprotegerin).

The **RANKL/RANK/OPG triad** constitutes the central endocrine axis of skeletal remodeling:
- **RANKL** (from osteoblasts, stromal cells, T cells, B cells) → activates **RANK** on osteoclast precursors → osteoclast differentiation and activation → bone resorption
- **OPG (osteoprotegerin; TNFRSF11B)** — secreted decoy receptor from osteoblasts — binds RANKL with high affinity (Kd ~0.1 nM) → prevents RANK activation → anti-osteoclastic
- The **OPG/RANKL ratio** sets the net bone resorption rate; estrogen → ↑OPG + ↓RANKL; parathyroid hormone → ↓OPG + ↑RANKL (explaining PTH-driven bone resorption in hyperparathyroidism)

**Denosumab** (Prolia/Xgeva; fully human anti-RANKL IgG2 mAb) is the pharmacological equivalent of OPG — with 5× greater RANKL affinity and longer dosing interval; it transformed osteoporosis management and bone metastasis prevention.

## Structure

**RANKL protein:**
- 317 aa type II transmembrane protein: short N-terminal cytoplasmic tail (aa 1–48) + single TM helix (aa 49–72) + C-terminal extracellular domain (aa 73–317, TNF homology domain CHD)
- **THD (TNF Homology Domain):** Forms **parallel homotrimer** → three-bladed propeller structure typical of TNF family (shared with TNF-α, TRAIL, FasL, CD40L); each monomer contributes one "blade" of the receptor-binding surface
- **Soluble RANKL (sRANKL):** Metalloprotease cleavage (MMP-14/MT1-MMP, ADAM10) at Glu282/Ala283 → shed 35-kDa extracellular fragment; circulates in blood (~0.2-3 pmol/L normal); elevated in postmenopausal osteoporosis, myeloma, and inflammatory bone disease
- **Receptor (RANK; TNFRSF11A, chr18q22.1):** TNFR superfamily member; type I single-pass TM; 4 cysteine-rich pseudorepeats (CRDs) in ectodomain; associates with TNF-receptor-associated factors (TRAFs)

**RANK signaling → osteoclastogenesis:**
1. RANKL trimer → RANK clustering → **TRAF6 recruitment** (primary adaptor; polyubiquitin K63-linked chain → TAK1 → IKK → **NF-κB p65/p50** nuclear translocation) + TRAF2/5 → **MAP3K7/TAK1 → JNK → AP-1 (c-Fos)**
2. NF-κB + AP-1 co-drive **NFATc1** (nuclear factor of activated T cells c1) transcription → NFATc1 is the master osteoclast transcription factor
3. NFATc1 → **cathepsin K** (bone-degrading protease), **TRAP** (tartrate-resistant acid phosphatase, osteoclast marker), **calcitonin receptor** (CTR), **integrin β3** (αvβ3 for osteoclast attachment) → mature resorbing osteoclast
4. **c-Src → PI3K → Akt → PDK1 → PKCδ:** Osteoclast survival and ruffled border formation
5. **NFATc2/Ca²⁺ oscillations:** M-CSF + RANKL → Ca²⁺ oscillations → calcineurin → NFATc2/NFATc1 nuclear translocation → sustained osteoclast activation

**OPG (decoy receptor):**
- Secreted soluble glycoprotein; 380 aa; contains N-terminal CRD domain (RANKL binding) + C-terminal death domain-like region
- Binds RANKL homotrimer (1:1 per RANKL chain) with Kd ~0.1 nM (10× higher affinity than RANK ectodomain alone)
- Also binds TRAIL (TNFSF10) → tumor cell anti-apoptotic effect; multiple myeloma cells express OPG-binding TRAIL receptors → myeloma cells hijack OPG as survival factor (explains why high OPG in bone marrow is bad for MM)
- Estrogen → osteoblast OPG transcription ↑ → protective against postmenopausal bone loss

## Function

**Osteoclast biology:**
- Mononuclear osteoclast precursors (monocyte/macrophage lineage, c-Fms+/CXCR4+) arrive at bone surfaces → M-CSF (from osteoblasts) → survival + RANK upregulation → RANKL binding → NFATc1 → multinucleated osteoclast fusion (via DC-STAMP, OC-STAMP)
- Mature osteoclast: polarized cell; apical membrane faces bone → **sealing zone (actin ring)** + **ruffled border** → acidified resorption lacuna (H⁺ ATPase pumps protons → pH ~4) → HCl dissolves hydroxyapatite; cathepsin K (pH optimum 6.0) digests type I collagen → CTX/NTX bone resorption markers released
- **Regulation of RANKL expression:** Estrogen → ERα on osteoblasts → ↑OPG + ↓RANKL; PTH (chronic) → PTH1R on osteoblasts → cAMP → ↓OPG + ↑RANKL; IL-6/IL-11 → JAK/STAT3 → RANKL in bone marrow stromal cells; prostaglandin E2 (inflammation) → ↑RANKL

**Inflammatory bone loss:**
- T cell-derived RANKL (TNF-α + IL-17A → Th17 cells → RANKL) → periarticular bone erosion in RA, periodontitis, psoriatic arthritis
- In RA: activated T cells → RANKL direct osteoclast activation (independent of osteoblasts) → juxta-articular osteopenia and erosions; denosumab reduces RA joint erosions (not approved for RA but studied)
- In periodontitis: Porphyromonas gingivalis → TLR2/4 → RANKL from gingival fibroblasts → alveolar bone destruction

**Bone metastasis:**
- Breast and prostate cancer cells produce **PTHrP** (PTH-related protein) and RANKL → osteolytic lesions (breast) or mixed osteolytic/osteoblastic (prostate)
- **Osteolytic niche:** Tumor-derived PTHrP → osteoblast RANKL ↑ → osteoclast activation → bone matrix release of TGF-β, IGF-1, FGF → tumor growth factors (vicious cycle)
- Xgeva (denosumab): phase 3 HALT-BC trial → delays SRE by median 8.5 months in breast cancer bone metastases vs. zoledronate; superior to bisphosphonate in some settings (NSCLC, MM, breast cancer)

## Mechanism

**Denosumab (Prolia/Xgeva) in postmenopausal osteoporosis [^cummings-2009-denosumab-freedom]:**
- **FREEDOM trial (2009):** 7,868 postmenopausal women with osteoporosis; denosumab 60 mg SC Q6M vs. placebo; 36-month follow-up
- Vertebral fractures: **68% RRR** (RR 0.32; 95% CI 0.26–0.41; p<0.001)
- Non-vertebral fractures: 20% RRR; Hip fractures: 40% RRR (in women with T-score ≤-2.5 at femoral neck)
- BMD: +9.2% lumbar spine, +6.0% total hip at 36 months; sustained increases with long-term extension (FREEDOM extension: 10 years data)
- **Rebound effect (critical limitation):** Denosumab suppresses osteoclast differentiation (not just activity); upon discontinuation, rapid surge in osteoclast precursors → rebound bone resorption → multiple vertebral fractures in some patients; transition to bisphosphonate REQUIRED after denosumab cessation

**RANKL in multiple myeloma (Xgeva indication):**
- MM bone disease: ~80% of MM patients develop bone lesions; osteolytic lesions from RANKL-driven osteoclast hyperactivation + BMP/Wnt blockade impairing osteoblast activity → net bone loss
- Xgeva (120 mg SC Q4W): non-inferior to zoledronate for SRE prevention; superior in subgroup analysis for time to first SRE in some MM studies; does NOT have renal dose-adjustment requirement (unlike zoledronate)

## Connections

RANKL → RANK on osteoclast precursors → NFATc1 → osteoclast differentiation → bone resorption; estrogen deficiency → RANKL surge → postmenopausal bone loss; denosumab (anti-RANKL) reduces vertebral fractures 68% and hip fractures 40% (FREEDOM trial 3-year).

RANKL is the essential differentiation signal for osteoclasts: RANK → TRAF6 → NF-κB + AP-1 → NFATc1 → c-Fos, cathepsin K, TRAP gene programs → mature osteoclasts; OPG decoy receptor blocks RANKL; denosumab mimics OPG with superior binding affinity and bone protection.

MM cells produce RANKL → osteoclast activation → osteolytic lesions; MM cells express OPG receptors (TRAIL-decoy function → MM survival); Xgeva (denosumab 120 mg Q4W) reduces skeletal-related events in MM patients with bone disease.

In AS, entheseal IL-17A + TNF-α upregulate RANKL on stromal cells → osteoclast-mediated bone erosion at sacroiliac joints and vertebral corners; subsequent WNT-driven syndesmophyte formation leads to ankylosis; denosumab reduces erosion but does not prevent new bone formation.

[^lacey-1998-rankl]: Lacey DL, Timms E, Tan HL, et al. Osteoprotegerin ligand is a cytokine that regulates osteoclast differentiation and activation. *Cell.* 1998;93(2):165-176. [doi:10.1016/S0092-8674(00)81569-X](https://doi.org/10.1016/S0092-8674(00)81569-X) · [PubMed 9568710](https://pubmed.ncbi.nlm.nih.gov/9568710/)
[^cummings-2009-denosumab-freedom]: Cummings SR, San Martin J, McClung MR, et al. Denosumab for prevention of fractures in postmenopausal women with osteoporosis. *N Engl J Med.* 2009;361(8):756-765. [doi:10.1056/NEJMoa0809493](https://doi.org/10.1056/NEJMoa0809493) · [PubMed 19671655](https://pubmed.ncbi.nlm.nih.gov/19671655/)

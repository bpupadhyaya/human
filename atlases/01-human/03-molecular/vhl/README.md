---
schema: human-scale-entry/v1
id: vhl
name: VHL
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "VHL tumor suppressor targets HIF-1α for proteasomal degradation under normoxia; VHL loss → constitutive HIF activation → VEGF, PDGF, and EPO. Biallelic VHL inactivation causes clear cell RCC (~75%) and von Hippel-Lindau syndrome (hemangioblastomas, pheochromocytoma)."
aliases: ["VHL", "von Hippel-Lindau", "VHL tumor suppressor", "HIF regulation", "E3 ubiquitin ligase", "clear cell RCC", "von Hippel-Lindau disease", "VBC complex"]
sources:
  - id: kaelin-2008-vhl-hif
    type: peer-reviewed
    cite: "Kaelin WG Jr. The von Hippel-Lindau tumour suppressor protein: O2 sensing and cancer. Nat Rev Cancer. 2008;8(11):865-873."
    doi: "10.1038/nrc2502"
    pmid: "18923434"
    url: "https://doi.org/10.1038/nrc2502"
  - id: choueiri-2021-belzutifan
    type: peer-reviewed
    cite: "Choueiri TK, Bauer TM, Papadopoulos KP, et al. Inhibition of hypoxia-inducible factor-2alpha in renal cell carcinoma with belzutifan. N Engl J Med. 2021;385(22):2059-2071."
    doi: "10.1056/NEJMoa2109635"
    pmid: "34818478"
    url: "https://doi.org/10.1056/NEJMoa2109635"
cross_links:
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "VHL E3 ubiquitin ligase binds hydroxylated HIF-1α/HIF-2α ODD domain → ubiquitination → proteasomal degradation; VHL loss → constitutive HIF stabilization → hypoxic gene program in normoxia; belzutifan (HIF-2α inhibitor) FDA-approved for VHL disease and 3rd-line ccRCC."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "HIF-1α/HIF-2α → VEGF transcription → VEGFR2 on endothelial cells → angiogenesis in ccRCC; VEGFR TKIs (sunitinib, pazopanib, cabozantinib, axitinib) target this axis; belzutifan directly inhibits HIF-2α → VEGF suppression without VEGFR targeting."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTORC1 phosphorylates 4EBP1 → HIF-1α mRNA translation; VHL loss and mTOR activation co-drive ccRCC angiogenesis; everolimus and temsirolimus (mTOR inhibitors) approved for 2nd-line RCC; mTOR pathway is activated by VEGFR-signaling feedback and PTEN loss in RCC."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K-AKT-mTOR pathway activated in ~30% of RCC via PTEN loss (~5%) or PIK3CA mutation; parallel to VHL-HIF axis; AKT phosphorylation → mTOR → HIF-1α mRNA translation → VEGF; combined VEGFR + mTOR inhibition (lenvatinib+everolimus) approved for 2nd-line RCC."
---

# VHL

## Overview

**VHL (von Hippel-Lindau)** is a classical tumor suppressor that functions as the substrate-recognition subunit of a **CRL2-VBC E3 ubiquitin ligase complex** (composed of VHL, Elongin B, Elongin C, Cullin 2, and RBX1). Under normoxia, VHL recognizes **hydroxylated HIF-1α and HIF-2α** at specific proline residues in the oxygen-dependent degradation domain (ODD) — hydroxylation catalyzed by **prolyl hydroxylase domain (PHD) enzymes** that require O₂ and α-ketoglutarate — and targets them for ubiquitination and proteasomal degradation. When oxygen is limited (hypoxia) or when VHL is lost (cancer), HIF-α accumulates, dimerizes with HIF-1β (ARNT), and transcriptionally activates hundreds of genes including VEGF, GLUT1, EPO, PDGF, and TGF-α [^kaelin-2008-vhl-hif].

**VHL in cancer:**
- **Clear cell renal cell carcinoma (ccRCC, ~75% of RCC):** Biallelic VHL inactivation in >90% of ccRCC (mutation + LOH or promoter methylation); without VHL, HIF-2α accumulates → constitutive activation of VEGF/PDGF/TGF-α angiogenic program → highly vascular tumors with exceptional VEGFR TKI sensitivity; ccRCC is the canonical HIF-driven tumor
- **Von Hippel-Lindau (VHL) syndrome:** Germline VHL mutation → autosomal dominant; CNS hemangioblastomas (cerebellum, spinal cord, brainstem), retinal hemangiomas, clear cell RCC (bilateral, multifocal), pheochromocytoma, pancreatic serous cystadenomas, and endolymphatic sac tumors; Type 1 (no pheo) vs. Type 2 (pheo — especially missense mutations)
- **Belzutifan (Welireg):** First-in-class HIF-2α (EPAS1) inhibitor; FDA approved 2021 for VHL disease-associated non-metastatic ccRCC, hemangioblastoma, and pancreatic serous cystadenoma; FDA approved 2023 for ccRCC after prior anti-PD-1 + anti-VEGFR therapy (LITESPARK-005 trial) [^choueiri-2021-belzutifan]

**2019 Nobel Prize:**
William Kaelin Jr, Peter Ratcliffe, and Gregg Semenza shared the 2019 Nobel Prize in Physiology or Medicine for discovering how cells sense oxygen — specifically, the VHL-HIF-PHD oxygen-sensing axis.

## Structure

### VHL protein architecture

VHL is a 213-amino-acid, 24-30 kDa (β-domain) or 30-kDa (α-domain) protein existing in two isoforms due to alternative translation start sites:

**Alpha (α) domain (1-54):**
- Connects to HIF-ODD binding groove (β-domain) via flexible linker
- Interaction surface with Elongin C within VBC complex
- VHL type 2C mutations (in α-domain) → pheo without RCC (attenuate HIF recognition but preserve Elongin C binding)

**Beta (β) domain (54-213):**
- Substrate-recognition domain that contacts hydroxylated HIF-1α/HIF-2α ODD
- Contains the HIF binding groove: recognizes hydroxyl-Pro residue (Pro564 in HIF-1α, Pro405/Pro531 in HIF-2α) — the "two-pronged plug"
- Cancer mutations (missense, truncating, deletion) cluster in β-domain and α-domain; all pathogenic VHL mutations abrogate either HIF binding or Elongin C interaction

**VBC complex:**
VHL + Elongin B + Elongin C → core ubiquitin adaptor; Cullin 2 (scaffold) + RBX1 (RING E3) → complete CRL2-VBC E3 ligase; recruits E2 ubiquitin-conjugating enzyme → polyubiquitinates HIF-α at Lys residues → proteasomal degradation.

### Oxygen-sensing pathway

**Normoxia (O₂ present):**
1. PHD1/2/3 (prolyl hydroxylase domain proteins) hydroxylate HIF-α Pro residues (requires O₂ + α-KG + Fe²⁺)
2. VHL recognizes hydroxyl-Pro → VBC → ubiquitination → proteasomal degradation → no HIF transcription

**Hypoxia or VHL loss:**
1. PHD enzymes inhibited (no O₂) or VHL mutated → HIF-α not recognized/degraded
2. HIF-α accumulates → nuclear translocation → dimerizes with HIF-1β → binds HRE (hypoxia response element, 5'-RCGTG-3') → activates VEGF, GLUT1, EPO, BNIP3, TWIST, LOX, LDHA, and hundreds of other hypoxia-response genes

**FIH (Factor Inhibiting HIF):**
Asparagyl hydroxylase that hydroxylates HIF-1α Asn803 in the C-TAD → blocks CBP/p300 coactivator interaction → partial repression of HIF transcriptional activity even when HIF is stabilized (second layer of O₂-dependent regulation)

## Function

### Normal VHL roles

**Oxygen homeostasis:**
VHL-HIF-EPO axis is the primary systemic oxygen-sensing pathway: hypoxia → EPO transcription in renal cortical interstitial cells (HIF-2α-dependent) → erythropoiesis → increased O₂-carrying capacity. VHL mutations in renal cells → constitutive EPO → polycythemia (some VHL mutations cause familial polycythemia without RCC).

**Cilia and mitotic spindle:**
VHL also functions in primary cilia maintenance (independent of HIF) and proper orientation of mitotic spindle; VHL-deficient cells have primary cilia defects → may contribute to tumor growth independent of HIF signaling.

**Non-HIF VHL substrates:**
- Atypical protein kinase C (aPKC): VHL promotes cytoskeletal polarity
- CARD9: VHL-dependent inflammation regulation
- Aurora A kinase: VHL promotes Aurora A degradation; VHL loss → mitotic instability (distinct from HIF pathway)

### ccRCC molecular biology

**HIF-2α as primary oncogenic driver in ccRCC:**
Although both HIF-1α and HIF-2α are stabilized by VHL loss, HIF-2α (EPAS1) drives ccRCC more than HIF-1α:
- HIF-2α expression correlates with tumor grade and invasiveness in ccRCC
- HIF-2α but not HIF-1α is required for xenograft growth in VHL-null RCC cell lines
- HIF-1α is sometimes lost or mutated in advanced ccRCC (potential tumor suppressor function in late-stage)
- Belzutifan selectively inhibits HIF-2α PAS-B domain → blocks HIF-2α/HIF-1β dimerization → suppresses VEGF, CCND1, and EGFR transcription in ccRCC

**Co-mutations in ccRCC (TCGA, 2013):**
- PBRM1 (~40%): SWI/SNF subunit; chromatin remodeling; prognostic
- BAP1 (~15%): Deubiquitinase; aggressive prognosis; associated with sarcomatoid features
- SETD2 (~15%): Histone H3K36 trimethyltransferase
- PTEN loss (~5%), KDM5C (~7%), TP53 (~10% sarcomatoid)
- Copy number: 3p loss (VHL locus) universal; 5q gain common

## Mechanism

### HIF-2α inhibitors

**Belzutifan (PT2977, Welireg — Merck):** [^choueiri-2021-belzutifan]
- First-in-class allosteric HIF-2α inhibitor; binds PAS-B domain hydrophobic cavity → disrupts HIF-2α/HIF-1β (ARNT) dimerization → no HRE binding → VEGF/EPO suppression
- **LITESPARK-004 (VHL disease):** ORR 64% in RCC, 50% in hemangioblastoma, 77% in PNST; DOR not reached; FDA approved 2021
- **LITESPARK-005 (3rd-line ccRCC):** PFS 5.6 vs. 3.5 months vs. everolimus; FDA approved October 2023; ORR 22%; first new agent beyond VEGFR TKIs approved in ccRCC since nivolumab
- Toxicities: Anemia (VHL disease-specific: HIF-2α drives EPO → belzutifan → reduced erythropoiesis); fatigue, dizziness, increased SCr; manageable

**PHD inhibitors (HIF activators — not RCC treatment):**
Roxadustat, daprodustat, vadadustat (PHD inhibitors) → HIF stabilization → EPO → used for **anemia of CKD**; mechanism is opposite to belzutifan; exploit normal PHD-VHL pathway to stimulate erythropoiesis without exogenous EPO

### Resistance to VEGFR TKIs in VHL-null ccRCC

**Primary resistance (~20-30%):**
- High SETD2 loss or sarcomatoid differentiation → epithelial-mesenchymal transition → reduced VEGFR dependence
- BAP1 mutation → enhanced PI3K-AKT-mTOR → alternative growth signals
- High c-MET or AXL expression → alternative RTK bypass

**Acquired resistance:**
- Upregulation of alternative angiogenic factors (FGF, ANG2)
- AXL (receptor tyrosine kinase) upregulation → cabozantinib (VEGFR+MET+AXL inhibitor) partially overcomes this
- PI3K-AKT activation as bypass: lenvatinib+everolimus exploits this by combining VEGFR+FGFR+mTOR inhibition

## Connections

- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — VHL E3 ubiquitin ligase binds hydroxylated HIF-1α/HIF-2α ODD domain → ubiquitination → proteasomal degradation; VHL loss → constitutive HIF stabilization → hypoxic gene program in normoxia; belzutifan (HIF-2α inhibitor) FDA-approved for VHL disease and 3rd-line ccRCC.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — HIF-1α/HIF-2α → VEGF transcription → VEGFR2 on endothelial cells → angiogenesis in ccRCC; VEGFR TKIs (sunitinib, pazopanib, cabozantinib, axitinib) target this axis; belzutifan directly inhibits HIF-2α → VEGF suppression without VEGFR targeting.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTORC1 phosphorylates 4EBP1 → HIF-1α mRNA translation; VHL loss and mTOR activation co-drive ccRCC angiogenesis; everolimus and temsirolimus (mTOR inhibitors) approved for 2nd-line RCC; mTOR pathway is activated by VEGFR-signaling feedback and PTEN loss in RCC.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K-AKT-mTOR pathway activated in ~30% of RCC via PTEN loss (~5%) or PIK3CA mutation; parallel to VHL-HIF axis; AKT phosphorylation → mTOR → HIF-1α mRNA translation → VEGF; combined VEGFR + mTOR inhibition (lenvatinib+everolimus) approved for 2nd-line RCC.

[^kaelin-2008-vhl-hif]: Kaelin WG Jr. The von Hippel-Lindau tumour suppressor protein: O2 sensing and cancer. *Nat Rev Cancer.* 2008;8(11):865-873. [doi:10.1038/nrc2502](https://doi.org/10.1038/nrc2502) · [PubMed 18923434](https://pubmed.ncbi.nlm.nih.gov/18923434/)
[^choueiri-2021-belzutifan]: Choueiri TK, Bauer TM, Papadopoulos KP, et al. Inhibition of hypoxia-inducible factor-2alpha in renal cell carcinoma with belzutifan. *N Engl J Med.* 2021;385(22):2059-2071. [doi:10.1056/NEJMoa2109635](https://doi.org/10.1056/NEJMoa2109635) · [PubMed 34818478](https://pubmed.ncbi.nlm.nih.gov/34818478/)

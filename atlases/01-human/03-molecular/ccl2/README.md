---
schema: human-scale-entry/v1
id: ccl2
name: CCL2
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "CCL2 (MCP-1, chr17q12) is the dominant monocyte chemoattractant; CCR2 → Gαi → PI3K/Akt + MAPK → directed migration; drives atherosclerotic plaque monocyte infiltration, NASH-associated macrophage (Kupffer cell) activation, and IgA nephropathy tubulointerstitial fibrosis."
aliases: ["CCL2", "MCP-1", "monocyte chemoattractant protein-1", "MCAF", "HC11", "SMC-CF", "JE protein", "CCR2 ligand"]
cross_links:
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "CCL2 from endothelium/macrophages → CCR2 on monocytes → subendothelial monocyte recruitment → foam cell formation → atherosclerotic plaque; CCL2/CCR2 inhibition reduces plaque in murine models; serum CCL2 correlates with cardiovascular event risk in the MRFIT and EPIC cohorts."
  - target: 01-human/07-system/iga-nephropathy
    relation: connects-to
    note: "Mesangial IgA immune complex deposition → complement + cytokine activation → CCL2 from mesangial cells + tubular epithelial cells → CCR2+ monocyte/macrophage infiltration → tubulointerstitial inflammation → fibrosis → CKD progression; urine CCL2 tracks IgAN disease activity."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "Hepatocyte lipotoxicity + DAMPs → Kupffer cell CCL2; elevated hepatic CCL2 → CCR2+ monocyte-derived macrophage recruitment → NLRP3 → IL-1β + TNF-α → stellate cell activation → fibrosis; cenicriviroc (CCR2/CCR5 dual antagonist) studied in CENTAUR/AURORA trials."
sources:
  - id: yoshimura-1987-mcp1
    type: peer-reviewed
    cite: "Yoshimura T, Matsushima K, Tanaka S, et al. Purification of a human monocyte chemoattractant produced by phytohemagglutinin-stimulated human blood mononuclear leukocytes. J Immunol. 1987;139(3):788-793."
    pmid: "2955805"
    doi: "10.4049/jimmunol.139.3.788"
    url: "https://doi.org/10.4049/jimmunol.139.3.788"
  - id: boring-1998-ccl2-atherosclerosis
    type: peer-reviewed
    cite: "Boring L, Gosling J, Cleary M, Charo IF. Decreased lesion formation in CCR2-/- mice reveals a role for chemokines in the initiation of atherosclerosis. Nature. 1998;394(6696):894-897."
    doi: "10.1038/29788"
    pmid: "9732872"
    url: "https://doi.org/10.1038/29788"
---

# CCL2

## Overview

**CCL2** (C-C motif chemokine ligand 2; gene *CCL2*, chromosome 17q12; also called **MCP-1**, monocyte chemoattractant protein-1) is the **most potent and specific chemoattractant for CCR2-expressing monocytes, macrophages, and dendritic cells** among the entire chemokine family. It is the prototypical member of the CC chemokine subfamily and was the first human chemokine discovered for monocyte recruitment [^yoshimura-1987-mcp1].

CCL2 is produced by a remarkably broad array of cell types under inflammatory conditions: endothelial cells, smooth muscle cells, monocytes/macrophages, fibroblasts, adipocytes, hepatocytes, mesangial cells, tubular epithelial cells, and keratinocytes. Its expression is transcriptionally driven by **NF-κB** (in response to TNF-α, IL-1β, LPS, and oxLDL) and **AP-1** (in response to growth factors and shear stress). The resulting CCL2 protein acts as the master chemotactic signal for **classical CD14⁺⁺CD16⁻ monocytes** — which constitutively express CCR2 at high levels — directing them from blood into inflamed tissues.

The **CCL2/CCR2 axis** is a central pathway in the pathogenesis of chronic inflammatory and metabolic diseases:
- **Atherosclerosis:** Monocyte recruitment to vascular lesions → foam cell formation
- **NASH/MASH:** Hepatic macrophage (Kupffer cell) activation and recruitment → fibrosis
- **Rheumatoid arthritis:** Synovial monocyte/macrophage infiltration → pannus formation
- **IgA nephropathy and CKD:** Tubulointerstitial macrophage infiltration → progressive fibrosis
- **Type 2 diabetes:** Adipose tissue macrophage (ATM) infiltration → insulin resistance

Multiple drugs targeting CCR2 (and sometimes CCR5 simultaneously) have been evaluated, underscoring the broad therapeutic relevance of this pathway.

## Structure

**CCL2 protein:**
- 99 aa (after signal peptide cleavage from 148-aa pre-protein); molecular weight ~13 kDa (monomer); circulates as both monomers and non-covalent dimers (physiological at concentrations >1 µg/mL)
- **CC chemokine fold:** Two N-terminal cysteines at positions 11 and 36 are adjacent (CC motif, unlike CXC chemokines with one intervening residue); four-stranded antiparallel β-sheet + single C-terminal α-helix → Greek-key topology; 2 conserved disulfide bonds (Cys11-Cys36; Cys12-Cys52) essential for structure
- **Glycosaminoglycan (GAG) binding:** CCL2 binds heparan sulfate on endothelial cell surfaces and extracellular matrix via its BBXB motif (Lys49-Arg52-Arg55) → creates a chemotactic gradient on the endothelial surface rather than diffusing freely; this "haptotactic" gradient is necessary for effective monocyte transmigration in vivo
- **GAG-binding mutations:** CCL2 P8A mutant binds CCR2 but fails to bind GAGs → cannot establish gradient in vivo → dominant-negative effect in mouse models → attenuates monocyte recruitment (potential therapeutic strategy)
- **Dimerization:** CCL2 forms head-to-head dimers at elevated concentrations; dimerization reduces receptor signaling potency but enhances GAG binding and gradient-forming capacity

**CCR2 receptor:**
- **CCR2** (gene *CCR2*, chr3p21.31; CCR2A 374 aa and CCR2B 360 aa splice variants — CCR2B dominant in monocytes): Class A GPCR; 7 TM helices; N-terminus contains sulfated tyrosine (Tyr26) critical for high-affinity CCL2 binding (Kd ~1-3 nM at CCR2B)
- **Signal transduction:** CCL2 → CCR2B → Gαi (dominant) → ↓cAMP + Gβγ → **PI3Kγ → Akt → mTORC1** (survival + metabolic reprogramming of monocytes toward inflammatory M1 phenotype) + **PLC-β → IP₃ → Ca²⁺ oscillations → actin reorganization** (cytoskeletal polarization for migration); **β-arrestin 2** → CCR2 desensitization and internalization + MAPK/ERK signaling
- **Biased agonism:** Different CCR2 ligands (CCL2, CCL7, CCL12) show distinct Gαi vs. β-arrestin signaling profiles; CCL7 is more β-arrestin-biased → potential for biased CCR2 agonists/antagonists with improved therapeutic windows
- **CCR5 co-expression:** CCR2 is commonly co-expressed with CCR5 on inflammatory monocytes; CCL2/CCR2 drives initial tissue entry while CCL5/CCR5 maintains subsequent macrophage activation; dual CCR2/CCR5 antagonism (cenicriviroc) was developed for synergistic anti-inflammatory and anti-fibrotic effect

**Upstream regulation of CCL2 expression:**
- **Transcriptional:** NF-κB (p65/p50; activated by TNF-α, IL-1β, LPS, reactive oxygen species, oxLDL) → CCL2 proximal promoter κB sites; AP-1 (c-Fos/c-Jun; activated by growth factors, shear stress, LPA) → CRE element in CCL2 promoter; SP1 constitutive baseline expression; hypoxia → HIF-1α → CCL2 in tumors and ischemic tissues
- **Post-transcriptional:** CCL2 mRNA is stabilized by ARE (AU-rich element)-binding proteins (HuR) under inflammatory conditions; TNF-α → HuR nuclear export → CCL2 mRNA stabilization
- **Inhibitors of CCL2:** IL-10, IL-13, IL-4 → STAT6/STAT3 → transcriptional repression; glucocorticoids → GR → AP-1 transrepression → CCL2 ↓; statins → Rho/ROCK inhibition + NF-κB suppression → reduced endothelial CCL2; metformin → AMPK → ↓NF-κB → CCL2 reduction in NASH models

## Function

**Monocyte/Macrophage recruitment:**
- Classical (inflammatory) monocytes: CD14⁺⁺CD16⁻; CCR2high; CX3CR1low; rapidly egress from bone marrow in response to CCL2 gradient; differentiate in tissues into M1 macrophages, foam cells, DCs
- CCL2 chemotaxis: Bound to endothelial heparan sulfate → monocyte CCR2 → PI3Kγ → Rac1 → lamellipodia → amoeboid migration through sub-endothelial space; CCL2 also activates integrin αLβ2 (LFA-1) and α4β1 (VLA-4) → firm adhesion; then chemokinesis toward the gradient

**Atherosclerosis — foam cell genesis:**
- Oxidized LDL (oxLDL) → endothelial NF-κB → VCAM-1, E-selectin, CCL2; monocyte rolling → arrest (VCAM-1/VLA-4) → transmigration → uptake of oxLDL via scavenger receptors (SR-A, CD36) → foam cell; CCL2/CCR2 drives the initial monocyte recruitment that seeds the plaque; genetic CCL2/CCR2 knockout or pharmacological CCR2 inhibition in ApoE⁻/⁻ mice reduces atherosclerotic lesion area 40-60% [^boring-1998-ccl2-atherosclerosis]
- Established human data: elevated plasma CCL2 in patients with coronary artery disease; correlates with major adverse cardiovascular events (MACE) in the MRFIT and EPIC-Norfolk cohort studies

**NASH/MASH — hepatic macrophage activation:**
- In NASH: hepatocyte lipotoxicity (palmitate, ceramide) → mitochondrial damage + NLRP3 → DAMPs (HMGB1, ATP) → Kupffer cell TLR4 → NF-κB → CCL2 + TGF-β; CCL2 recruits bone marrow-derived CCR2⁺ monocyte-derived macrophages (MoMFs) to supplement resident Kupffer cells → MoMF = major IL-1β, TNF-α source → hepatocyte apoptosis + hepatic stellate cell (HSC) activation → fibrosis
- **Cenicriviroc** (CCR2/CCR5 dual antagonist): CENTAUR trial (Phase 2b, N=289): CVC vs. adarotene (arachidonic acid antagonist); 20% vs. 10% fibrosis improvement without worsening of NASH at 1 year (not statistically significant at primary endpoint); AURORA trial (Phase 3) terminated early due to failure at interim analysis — highlight of the clinical translational challenge in NASH despite compelling preclinical data

**IgA nephropathy — tubulointerstitial damage:**
- IgA1 immune complexes deposit in mesangium → mesangial CCR2⁺ activation + complement C3b → local inflammation → mesangial and tubular epithelial cell CCL2 secretion → cortical interstitial macrophage (CCR2⁺) infiltration → TGF-β → fibrosis → tubular atrophy → eGFR decline; urinary CCL2 (urine CCL2/creatinine ratio) correlates with CKD progression rate in IgAN and is being explored as a biomarker for treatment response

**Type 2 diabetes and adipose tissue inflammation:**
- Adipocyte hypertrophy → ER stress + HIF-1α → CCL2 → ATM (adipose tissue macrophage) CCR2-mediated recruitment; ATMs produce TNF-α, IL-6, and IL-1β → JNK → IRS-1 Ser307 phosphorylation → insulin resistance; adipose CCL2 gene expression correlates with BMI, insulin resistance, and visceral fat mass in obese humans; metformin and pioglitazone reduce adipose CCL2 expression

## Mechanism

**CCR2 inhibitors — clinical development:**

*Cenicriviroc (CCR2/CCR5 dual antagonist):*
- Oral, once-daily; Kd ~3 nM CCR2, Kd ~9 nM CCR5; developed by Allergan/AbbVie for NASH
- **CENTAUR (Phase 2b, 2016):** 289 adults with NASH + fibrosis; CVC 150 mg QD vs. placebo × 1 year; fibrosis ≥1 stage improvement without NASH worsening: 20% vs. 10% (p=0.02 secondary endpoint at year 1); anti-fibrotic signal confirmed; anti-steatohepatitis effect not significant
- **AURORA (Phase 3):** 2019 enrollment; interim futility analysis 2020 → terminated (failed to show superiority for the combined NASH resolution + fibrosis improvement co-primary endpoint); highlights difficulty of translating CCL2/CCR2 biology to clinical benefit in NASH

*CCX872 (ChemoCentryx; CCR2 antagonist):*
- BEAT (Phase 2, pancreatic cancer): CCX872 + nab-paclitaxel + gemcitabine → 29% 1-year OS vs. 19% historical control; rationale: tumor-associated macrophage (TAM) CCR2-dependent recruitment — tumor microenvironment immunosuppression; early signal

*Propagermanium (CCR2 antagonist; Japan-approved hepatitis B):*
- Oral organoger compound; reduces CCL2-driven HBV liver injury; approved in Japan for HBV-associated hepatitis; not widely used

*Anti-CCL2 antibodies (carlumab, MLN1202):*
- Carlumab (anti-CCL2 mAb; Janssen): Phase 2 in metastatic CRPC and RA — failed primary endpoints; CCL2 rebound after antibody-mediated clearance may have enhanced metastasis paradoxically
- MLN1202 (anti-CCR2 mAb): Phase 2 in RA — modest signal but insufficient for further development

**CCL2 in other diseases:**
- **Rheumatoid arthritis:** CCL2 is markedly elevated in synovial fluid and serum of RA patients; correlates with DAS28 score; drives monocyte recruitment to synovium → pannus macrophage → RANKL, TNF-α → bone erosion; MTX and anti-TNF therapy reduce synovial CCL2
- **COVID-19 cytokine storm:** Severe COVID-19 → marked CCL2 elevation (monocyte activation) → monocyte-derived macrophage (MoMF) pulmonary infiltration → ARDS; CCL2 + IL-6 + CXCL10 = signature cytokine pattern of severe COVID-19

## Connections

CCL2 from endothelium/macrophages → CCR2 on monocytes → subendothelial monocyte recruitment → foam cell formation → atherosclerotic plaque; CCL2/CCR2 inhibition reduces plaque in murine models; serum CCL2 correlates with cardiovascular event risk in the MRFIT and EPIC cohorts.

Mesangial IgA immune complex deposition → complement + cytokine activation → CCL2 from mesangial cells + tubular epithelial cells → CCR2+ monocyte/macrophage infiltration → tubulointerstitial inflammation → fibrosis → CKD progression; urine CCL2 tracks IgAN disease activity.

Hepatocyte lipotoxicity + DAMPs → Kupffer cell CCL2 + TGF-β production; elevated hepatic CCL2 → CCR2+ monocyte-derived macrophage recruitment → NLRP3 → IL-1β + TNF-α → stellate cell activation → fibrosis; cenicriviroc (CCR2/CCR5 dual antagonist) was studied in CENTAUR/AURORA trials.

- `connects-to` → **[Atherosclerosis](../../07-system/atherosclerosis/README.md)** — CCL2 from endothelium/macrophages → CCR2 on monocytes → subendothelial monocyte recruitment → foam cell formation → atherosclerotic plaque; CCL2/CCR2 inhibition reduces plaque in murine models; serum CCL2 correlates with cardiovascular event risk in the MRFIT and EPIC cohorts.
- `connects-to` → **[IgA Nephropathy](../../07-system/iga-nephropathy/README.md)** — Mesangial IgA immune complex deposition → complement + cytokine activation → CCL2 from mesangial cells + tubular epithelial cells → CCR2+ monocyte/macrophage infiltration → tubulointerstitial inflammation → fibrosis → CKD progression; urine CCL2 tracks IgAN disease activity.
- `connects-to` → **[NASH](../../07-system/nash/README.md)** — Hepatocyte lipotoxicity + DAMPs → Kupffer cell CCL2 + TGF-β production; elevated hepatic CCL2 → CCR2+ monocyte-derived macrophage recruitment → NLRP3 → IL-1β + TNF-α → stellate cell activation → fibrosis; cenicriviroc (CCR2/CCR5 dual antagonist) was studied in CENTAUR/AURORA trials.

[^yoshimura-1987-mcp1]: Yoshimura T, Matsushima K, Tanaka S, et al. Purification of a human monocyte chemoattractant produced by phytohemagglutinin-stimulated human blood mononuclear leukocytes. *J Immunol.* 1987;139(3):788-793. [doi:10.4049/jimmunol.139.3.788](https://doi.org/10.4049/jimmunol.139.3.788) · [PubMed 2955805](https://pubmed.ncbi.nlm.nih.gov/2955805/)
[^boring-1998-ccl2-atherosclerosis]: Boring L, Gosling J, Cleary M, Charo IF. Decreased lesion formation in CCR2-/- mice reveals a role for chemokines in the initiation of atherosclerosis. *Nature.* 1998;394(6696):894-897. [doi:10.1038/29788](https://doi.org/10.1038/29788) · [PubMed 9732872](https://pubmed.ncbi.nlm.nih.gov/9732872/)

---
schema: human-scale-entry/v1
id: bap1
name: BAP1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "BAP1 (BRCA1-associated protein 1) is a nuclear deubiquitinase that removes H2AK119 ubiquitin → opposes PRC1 repression; germline BAP1 mutations cause BAP1 tumor predisposition syndrome (mesothelioma, uveal melanoma, ccRCC); somatic BAP1 loss in ~50-60% of mesothelioma."
aliases: ["BAP1", "BRCA1-associated protein 1", "BAP1 tumor predisposition syndrome", "BAP1-TPDS", "BAP1 mesothelioma", "BAP1 uveal melanoma", "BAP1 deubiquitinase", "H2AK119 BAP1", "PR-DUB complex"]
sources:
  - id: testa-2011-bap1-germline
    type: peer-reviewed
    cite: "Testa JR, Cheung M, Pei J, et al. Germline BAP1 mutations predispose to malignant mesothelioma. Nat Genet. 2011;43(10):1022-1025."
    doi: "10.1038/ng.912"
    pmid: "21874000"
    url: "https://doi.org/10.1038/ng.912"
  - id: bott-2011-bap1-somatic
    type: peer-reviewed
    cite: "Bott M, Brevet M, Taylor BS, et al. The nuclear deubiquitinase BAP1 is commonly inactivated by somatic mutations and putative germline variants in sporadic malignant mesothelioma. Nat Genet. 2011;43(7):668-672."
    doi: "10.1038/ng.855"
    pmid: "21642991"
    url: "https://doi.org/10.1038/ng.855"
cross_links:
  - target: 01-human/03-molecular/brca1
    relation: connects-to
    note: "BAP1 was named for its interaction with the BRCA1 C-terminal RING domain; BAP1 co-localizes with BRCA1 at DSBs for HR repair; germline BAP1 mutations cause BAP1-TPDS, a cancer predisposition syndrome with penetrance comparable to BRCA1/2."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "BAP1 (PR-DUB complex, H2AK119 deubiquitinase) antagonizes PRC1 H2AK119 ubiquitination; EZH2 (PRC2) writes H3K27me3 reinforcing PRC1 repression; BAP1 loss + EZH2 gain both drive polycomb reprogramming toward epigenetic silencing of tumor suppressors."
  - target: 01-human/03-molecular/vhl
    relation: connects-to
    note: "BAP1 and VHL are co-mutated tumor suppressors in ccRCC; BAP1-mutant ccRCC (~10%) has poorer prognosis than VHL-only; BAP1 mutations define a distinct epigenetic ccRCC subgroup; BAP1+VHL co-loss confers increased metastatic risk and poorer OS in ccRCC cohorts."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "BAP1 deubiquitinates H2AK119ub → opens polycomb-repressed chromatin, counteracting MYC-driven proliferative programs; BAP1 loss → polycomb silencing of tumor suppressors + MYC target gene upregulation; this axis is active in mesothelioma and uveal melanoma."
---

# BAP1

## Overview

**BAP1 (BRCA1-Associated Protein 1)** is a nuclear deubiquitinase (DUB) of the ubiquitin C-terminal hydrolase (UCH) family that catalyzes the removal of monoubiquitin from **histone H2A at lysine 119 (H2AK119ub1)** — the repressive histone mark written by Polycomb Repressive Complex 1 (PRC1). By removing H2AK119ub1, BAP1 opposes polycomb-mediated gene silencing and maintains open chromatin at the promoters of tumor suppressor genes, differentiation factors, and DNA repair genes. BAP1 is the catalytic subunit of the **PR-DUB (Polycomb Repressive DeUBiquitinase) complex**, which also contains ASXL1, ASXL2, or ASXL3 (scaffold subunits), FOXK1/FOXK2, and OGT (O-GlcNAc transferase). BAP1 also participates directly in DNA double-strand break (DSB) repair (via interaction with BRCA1) and transcriptional regulation (deubiquitination of non-histone substrates including HCF-1, KLF5, and BRCA1 itself). In cancer, **somatic BAP1 loss** is a hallmark of mesothelioma (~50-60%), uveal melanoma (~82%), and clear cell RCC (~10%), while **germline BAP1 mutations** cause **BAP1 Tumor Predisposition Syndrome (BAP1-TPDS)** — one of the most penetrant hereditary cancer syndromes with lifetime risk of mesothelioma, uveal melanoma, ccRCC, and cutaneous melanocytic tumors [^testa-2011-bap1-germline] [^bott-2011-bap1-somatic].

**BAP1 in cancer:**
- **Mesothelioma:** BAP1 loss (deletion/mutation/loss of heterozygosity) in ~50-60% of pleural mesothelioma; more common in epithelioid subtype; IHC nuclear loss → diagnostic marker; epithelioid BAP1-loss mesothelioma → better prognosis (more immune infiltration); sarcomatoid mesothelioma: BAP1 retained but CDKN2A/NF2 lost
- **Uveal melanoma:** BAP1 somatic mutations in ~82%; primary predictor of metastatic risk (BAP1 loss → class 2 → >50% metastasis at 5 years); IHC nuclear BAP1 loss → class 2 designation; no approved targeted therapy for BAP1-mutant UM; tebentafusp (TCR bispecific, HLA-A*02:01) approved for UM regardless of BAP1
- **Clear cell RCC (ccRCC):** BAP1 somatic mutations in ~10% of ccRCC; mutually exclusive with PBRM1 mutation in most cases; BAP1-mutant ccRCC → worse prognosis than PBRM1-mutant ccRCC (mOS ~1.9 years vs ~4.7 years); BAP1-mutant ccRCC responds similarly to VHL/HIF-pathway-targeted agents and IO
- **Intrahepatic CCA:** BAP1 mutations in ~20%; poor prognosis; epigenetic deregulation
- **BAP1-TPDS (germline):** Autosomal dominant; near-full penetrance for ≥1 BAP1-related cancer; surveillance: annual MRI brain+orbit, annual skin exam, periodic CT chest (mesothelioma), annual ophthalmology (uveal melanoma); germline testing recommended for early-onset or bilateral uveal melanoma, mesothelioma without asbestos exposure

## Structure

### BAP1 protein architecture

BAP1 is an 839-amino-acid, 91 kDa nuclear protein:

**UCH domain (1-240, ubiquitin C-terminal hydrolase):**
- Catalytic DUB domain; Cys91 nucleophile (catalytic cysteine); cleaves isopeptide bond between ubiquitin C-terminus (Gly76) and H2AK119 ε-amino group
- BAP1 UCH domain is atypical: lacks the active-site loop found in other UCH enzymes (no UCHL3-like catalytic loop) → BAP1 UCH alone has minimal intrinsic activity; requires ASXL1/2/3 binding for full activation → ASXL1/2/3 interaction induces conformational change → active DUB
- Specificity: BAP1 UCH acts on Lys119 monoubiquitinated H2A; does not cleave polyubiquitin chains; the PR-DUB complex achieves nucleosomal selectivity via ASXL scaffold interaction with H2B

**BRCA1/2-interacting domain (BARD domain, 240-400):**
- Contains BARD motif (BRCA1 C-terminal associated-related domain); physically interacts with BRCA1 RING/BARD1 complex
- BAP1 is recruited to DNA DSBs via BRCA1 → BAP1 deubiquitinates H2AK119ub at DSBs → relaxed chromatin → facilitates BRCA1-mediated homologous recombination repair
- BAP1-BRCA1 interaction may partially explain the elevated cancer risk (mesothelioma, UM, RCC) in BAP1-TPDS, analogous to BRCA1/2 cancer predisposition

**HCF-1 binding domain (400-530):**
- BAP1 interacts with host cell factor 1 (HCF-1) → deubiquitinates HCF-1 → regulates cell cycle progression (HCF-1 is an E2F-target gene activator); BAP1-HCF-1 interaction links BAP1 to cell cycle control

**ASXL1/2/3 interaction domain (C-terminal ~550-839):**
- Direct binding to ASXL1 (or ASXL2/3) via C-terminal region → essential for PR-DUB complex assembly and catalytic activation of BAP1 UCH
- ASXL1 (mutated in ~20% of MDS, ~5% of AML) contains PHD domain + ASX homology domain → bridges BAP1 to chromatin; ASXL1 mutations in MDS/AML disrupt PR-DUB → impaired H2AK119 deubiquitination → increased polycomb repression

### BAP1 substrates and signaling

**H2AK119ub1 (primary substrate):**
PRC1 complex (RING1A/B catalytic) mono-ubiquitinates H2A at K119 → H2AK119ub1 mark → represses transcription by interfering with RNA Pol II elongation and recruiting additional PRC1/PRC2 subunits; BAP1-PR-DUB removes H2AK119ub1 at specific genomic loci → derepresses gene expression at tumor suppressor and differentiation gene promoters.

**Non-histone substrates:**
- BRCA1 ubiquitination (K6, K1268): BAP1 deubiquitinates BRCA1 → regulates BRCA1 stability and function in HR repair
- HCF-1 ubiquitination: Regulates cell cycle S-phase entry
- KLF5 ubiquitination: BAP1 deubiquitinates KLF5 → KLF5 stability → epithelial differentiation; BAP1 loss → KLF5 degradation → mesenchymal transition

**BAP1 and Polycomb biology:**
In mesothelioma: BAP1 loss → increased H2AK119ub1 globally at CpG islands → PRC2/EZH2 reinforcement of H3K27me3 at same loci (PRC1 recruits PRC2 via H2AK119ub "reader" domains) → synergistic polycomb silencing of CDKN2A (p16/p14ARF), RASSF1, PTEN, WT1, and other tumor suppressors → mesothelioma epigenetic landscape dominated by polycomb repression.

## Function

### Normal BAP1 roles

**Polycomb balance in stem cells and differentiation:**
BAP1-PR-DUB maintains gene-expression competence at poised (bivalent H3K27me3+H3K4me3) developmentally regulated genes in stem cells; upon differentiation signals, BAP1 deubiquitinates H2AK119ub at lineage-specific gene promoters → allows RNA Pol II progression → differentiation gene expression. BAP1 knockout in mice → early embryonic lethality (E13.5); conditional knockout → impaired hematopoietic progenitor differentiation (BCR signaling defect in B-cells), impaired epidermal differentiation.

**DNA damage response:**
BAP1 recruited to γH2AX foci at DSBs via BRCA1 → H2AK119 deubiquitination at DSB flanking chromatin → chromatin decompaction → nucleosome repositioning → BRCA1-dependent resection and HR. BAP1-null cells → impaired HR efficiency → NHEJ predominance → genomic instability; BAP1-null mesothelioma cells have elevated mutational burden and chromosomal instability (consistent with HR repair defect).

**Circadian gene regulation:**
BAP1 deubiquitinates the circadian clock transcription factor CLOCK → modulates CLOCK-BMAL1 transcriptional activity → circadian rhythm regulation; BAP1 oscillates in expression with circadian periodicity; this may link BAP1 loss to circadian disruption and cancer metabolism.

### BAP1 in BAP1-TPDS

**Penetrance and surveillance:**
BAP1-TPDS is among the highest-penetrance cancer predisposition syndromes (comparable to BRCA1/2); estimated cumulative cancer risks by age 75: mesothelioma ~50%, uveal melanoma ~30-45%, cutaneous MelanoCytic BAP1-inactivated Proliferations (MBAPs) ~60%, ccRCC ~10-15%, intrahepatic CCA ~5%; other reported: cutaneous melanoma, Merkel cell carcinoma, adenocarcinoma of various sites.

**MBAPs (Melanocytic BAP1-inactivated Proliferations):**
Atypical nevi with intranuclear epithelioid cells (Wiesner nevi) → loss of BAP1 IHC → benign/borderline cutaneous melanocytic proliferations; virtually pathognomonic for BAP1-TPDS when present; serve as a diagnostic clue for germline BAP1 testing.

## Mechanism

### BAP1 loss and therapeutic implications

**No direct BAP1-targeted therapy:**
There is currently no approved drug that restores BAP1 function or directly targets BAP1-null tumors. Research approaches:
- **EZH2 inhibition:** BAP1 loss → H2AK119ub accumulation → PRC2/EZH2 reinforcement → H3K27me3 increase → tazemetostat (EZH2 inhibitor) may partially restore gene expression at polycomb-silenced tumor suppressors; tazemetostat active in BAP1-null mesothelioma preclinical models; clinical trials ongoing in mesothelioma
- **PARP inhibitors:** BAP1 participates in HR repair → BAP1-null tumors may have HRD phenotype; rucaparib, olaparib investigated in BAP1-null cancers; results modest in mesothelioma
- **Immunotherapy:** BAP1-null mesothelioma (epithelioid) has higher tumor-infiltrating lymphocytes and PD-L1 → potentially more immunogenic → nivolumab + ipilimumab most active in this subgroup; BAP1-null ccRCC → higher immune infiltration (checkpoint inhibitor responsive subgroup)
- **MAT2A inhibitors (for MTAP-deleted tumors):** CDKN2A locus deletion (9p21) co-occurs with BAP1 loss in ~50-70% of mesothelioma; MTAP deletion in 9p21 region → MAT2A dependency → AG-270 (MAT2A inhibitor) under investigation in MTAP-deleted mesothelioma

**BAP1 IHC as diagnostic marker:**
In mesothelioma: Combined BAP1 IHC (nuclear loss) + CDKN2A FISH (homozygous deletion) achieves ~90% specificity for malignant mesothelioma vs. reactive mesothelial hyperplasia; allows definitive diagnosis on small biopsies (CT-guided, VATS, pleural effusion cell blocks). In uveal melanoma: BAP1 IHC loss (nuclear) → high risk of metastasis (Class 2 equivalent) → intensive surveillance (liver MRI q3-6 months).

## Connections

- `connects-to` → **[BRCA1](../../03-molecular/brca1/README.md)** — BAP1 was named for its interaction with the BRCA1 C-terminal RING domain; BAP1 co-localizes with BRCA1 at DSBs for HR repair; germline BAP1 mutations cause BAP1-TPDS, a cancer predisposition syndrome with penetrance comparable to BRCA1/2.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — BAP1 (PR-DUB complex, H2AK119 deubiquitinase) antagonizes PRC1 H2AK119 ubiquitination; EZH2 (PRC2) writes H3K27me3 reinforcing PRC1 repression; BAP1 loss + EZH2 gain both drive polycomb reprogramming toward epigenetic silencing of tumor suppressors.
- `connects-to` → **[VHL](../../03-molecular/vhl/README.md)** — BAP1 and VHL are co-mutated tumor suppressors in ccRCC; BAP1-mutant ccRCC (~10%) has poorer prognosis than VHL-only; BAP1 mutations define a distinct epigenetic ccRCC subgroup; BAP1+VHL co-loss confers increased metastatic risk and poorer OS in ccRCC cohorts.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — BAP1 deubiquitinates H2AK119ub → opens polycomb-repressed chromatin, counteracting MYC-driven proliferative programs; BAP1 loss → polycomb silencing of tumor suppressors + MYC target gene upregulation; this axis is active in mesothelioma and uveal melanoma.

[^testa-2011-bap1-germline]: Testa JR, Cheung M, Pei J, et al. Germline BAP1 mutations predispose to malignant mesothelioma. *Nat Genet.* 2011;43(10):1022-1025. [doi:10.1038/ng.912](https://doi.org/10.1038/ng.912) · [PubMed 21874000](https://pubmed.ncbi.nlm.nih.gov/21874000/)
[^bott-2011-bap1-somatic]: Bott M, Brevet M, Taylor BS, et al. The nuclear deubiquitinase BAP1 is commonly inactivated by somatic mutations and putative germline variants in sporadic malignant mesothelioma. *Nat Genet.* 2011;43(7):668-672. [doi:10.1038/ng.855](https://doi.org/10.1038/ng.855) · [PubMed 21642991](https://pubmed.ncbi.nlm.nih.gov/21642991/)

---
schema: human-scale-entry/v1
id: fgfr
name: FGFR
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Receptor tyrosine kinase family (FGFR1-4) binding FGF ligands → RAS-MAPK and PI3K-AKT → proliferation, angiogenesis, and differentiation. Amplified in breast/gastric, mutated in bladder/cholangiocarcinoma; erdafitinib (FGFR3) and pemigatinib (FGFR1-3) are approved inhibitors."
aliases: ["FGFR1", "FGFR2", "FGFR3", "FGFR4", "fibroblast growth factor receptor", "FGF receptor", "FGFR family", "FGF signaling"]
sources:
  - id: loriot-2019-erdafitinib
    type: peer-reviewed
    cite: "Loriot Y, Necchi A, Park SH, et al. Erdafitinib in locally advanced or metastatic urothelial carcinoma. N Engl J Med. 2019;381(4):338-348."
    doi: "10.1056/NEJMoa1817323"
    pmid: "31340094"
    url: "https://doi.org/10.1056/NEJMoa1817323"
  - id: abou-alfa-2020-pemigatinib
    type: peer-reviewed
    cite: "Abou-Alfa GK, Sahai V, Hollebecque A, et al. Pemigatinib for previously treated, locally advanced or metastatic cholangiocarcinoma. Lancet Oncol. 2020;21(5):671-684."
    doi: "10.1016/S1470-2045(20)30109-1"
    pmid: "32203698"
    url: "https://doi.org/10.1016/S1470-2045(20)30109-1"
cross_links:
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "FGFR and VEGFR co-regulate tumor angiogenesis; FGF2 → FGFR1 activates alternative angiogenesis, conferring bevacizumab resistance; lenvatinib and ponatinib target both FGFR and VEGFR; FGFR1-overexpressing endothelial cells resist anti-VEGF therapy through sustained ERK signaling."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "FGFR signals through PI3K-AKT → mTORC1 → protein synthesis and cell survival; mTOR inhibitors combined with FGFR inhibitors synergize in FGFR2-amplified gastric and breast cancer models; FGFR2 amplification activates mTORC1 independently of AKT in some gastric cancers."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "FGFR amplification and KRAS mutation co-occur in bladder and lung cancers; FGFR1 amplification can substitute for KRAS mutation in NSCLC; FGFR-KRAS converge on ERK → cyclin D1 → G1/S entry; FGFR3-KRAS co-alterations in bladder cancer portend worse prognosis."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "FGFR1/2/3 and EGFR share downstream RAS-MAPK and PI3K-AKT; FGF2-FGFR1 mediates resistance to EGFR TKIs in NSCLC and cetuximab in colorectal cancer; dual FGFR+EGFR inhibition restores TKI sensitivity in FGFR-driven EGFR-TKI-resistant NSCLC in preclinical models."
  - target: 01-human/03-molecular/fgf23
    relation: connects-to
    note: "FGF23 signals via FGFR1c/αKlotho in kidney (phosphate excretion) and parathyroid (PTH suppression); FGFR4 drives cardiac hypertrophy in CKD at high FGF23 concentrations; FGFR inhibitors (erdafitinib) block FGF23/FGFR1 → hyperphosphatemia requiring phosphate management."
  - target: 01-human/07-system/bladder-cancer
    relation: connects-to
    note: "FGFR3 mutations (S249C, R248C, K652E) and FGFR3-TACC3 fusions drive ~25-35% of urothelial carcinoma; erdafitinib (pan-FGFR inhibitor) FDA-approved for FGFR3-altered metastatic bladder cancer (THOR: OS 12.1 vs. 7.8 months vs. pembrolizumab in FGFR-selected patients)."
  - target: 01-human/07-system/cholangiocarcinoma
    relation: connects-to
    note: "FGFR2 fusions/rearrangements in ~15-20% of intrahepatic cholangiocarcinoma; pemigatinib (FIGHT-202: ORR 36%) and futibatinib (FOENIX-CCA2: ORR 42%) are FDA-approved; covalent futibatinib overcomes gatekeeper V564F resistance to reversible pemigatinib."
---

# FGFR

## Overview

**Fibroblast growth factor receptors (FGFRs)** are a family of four transmembrane receptor tyrosine kinases (FGFR1-4) that bind the 22-member **FGF (fibroblast growth factor) ligand family** → intracellular signaling → cell proliferation, survival, migration, angiogenesis, wound healing, and embryonic development. FGFRs are among the most frequently altered RTKs in human cancer: amplification, activating point mutations, and gene fusions/rearrangements occur across many cancer types and are actionable with approved targeted inhibitors [^loriot-2019-erdafitinib] [^abou-alfa-2020-pemigatinib].

**Physiological roles:**
- **Embryogenesis:** FGFR1/2 regulate mesoderm, limb, and CNS development; FGFR1 null mice are embryonic lethal (gastrulation defect); FGFR2 null mice die at blastocyst implantation (trophoblast failure)
- **Skeletal development:** FGFR3 restrains chondrocyte proliferation → gain-of-function mutations → achondroplasia (FGFR3 G380R — most common skeletal dysplasia); FGFR3 G380R inhibited by vosoritide (BMN 111 — CNP analogue) and recently by acoramidis/infigratinib (for achondroplasia)
- **Angiogenesis:** FGF1/2 via FGFR1 → endothelial proliferation and migration; FGFR1 and VEGFR2 co-expressed on endothelial cells — functional redundancy underlies bevacizumab resistance
- **Wound healing:** FGF7/10 via FGFR2-IIIb → keratinocyte proliferation → re-epithelialization; FGF23 (bone-derived) via FGFR1 + co-receptor Klotho → renal phosphate excretion (FGF23 excess → hypophosphatemia; loss → hyperphosphatemia/aging phenotype)
- **Hematopoiesis:** FGFR1 is required for mast cell and basophil development; FGFR1 fusions (8p11 syndrome) → myeloproliferative neoplasm with eosinophilia

**Cancer alterations (frequencies in selected tumors):**
| Tumor type | FGFR alteration | Frequency | FDA-approved agent |
|-----------|----------------|----------|------------------|
| **Urothelial carcinoma (bladder)** | FGFR3 mutation (S249C, R248C, Y375C, K652E) or FGFR3 fusion (FGFR3-TACC3) | ~25-35% | Erdafitinib |
| **Intrahepatic cholangiocarcinoma** | FGFR2 fusion/rearrangement (FGFR2-BICC1, FGFR2-PPHLN1) | ~15-20% | Pemigatinib, futibatinib |
| **Breast cancer (HR+/HER2-)** | FGFR1 amplification (8p11-12) | ~10-15% | None (clinical trials) |
| **Gastric cancer** | FGFR2 amplification | ~5-10% | None (clinical trials) |
| **Multiple myeloma** | FGFR3 mutation/translocation (t(4;14) → MMSET + FGFR3) | ~15% | None (under study) |
| **Endometrial cancer** | FGFR2 mutation (N549K, K310R) | ~10-15% | None (clinical trials) |
| **NSCLC** | FGFR1 amplification (squamous) | ~15-20% | None (clinical trials) |

## Structure

### FGFR protein architecture

All four FGFRs share the same three-domain architecture, with splice variants adding specificity:

**Extracellular domain (ECD):**
- Three immunoglobulin-like domains (D1, D2, D3) — D2 and D3 are the FGF binding domains; D1 is an autoinhibitory domain (acid box in the D1-D2 linker suppresses receptor activation in the absence of FGF and heparan sulfate)
- **Alternative splicing of D3 (exon 8 or 9):** FGFR1/2/3 each produce IIIb (epithelial-expressed) and IIIc (mesenchymal-expressed) isoforms with different FGF ligand specificity; IIIb vs. IIIc splicing is a key determinant of which FGF ligands activate which tissues
- **Heparan sulfate (HS) co-receptor requirement:** FGF ligands form a ternary complex with FGFR + HS proteoglycans (SDC4, GPC1); HS promotes FGF dimerization and FGFR activation → explains why FGF signaling is often tissue-specific (HS composition varies by tissue)

**Transmembrane domain:**
- Single-pass alpha-helix; transmembrane domain mutations rare in cancer; receptor dimerization through transmembrane domain in some constitutively active mutants (FGFR3 A391E in Crouzon syndrome)

**Intracellular domain:**
- **Juxtamembrane domain:** Contains regulatory phosphorylation sites; interacts with FRS2α (FGFR substrate 2 alpha) — the central scaffold for FGFR signal propagation
- **Kinase domain:** Classic bilobal tyrosine kinase; contains the activation loop (DFG motif); **pY653/Y654** in the A-loop = the primary activation phosphorylations; FGFR kinase domain is structurally similar to other RTKs (VEGFR, PDGFR) → multi-kinase inhibitors (lenvatinib, ponatinib) target FGFR
- **C-terminal tail:** Contains additional phosphorylation sites; PLCγ directly binds FGFR kinase C-lobe (distinct from other RTKs)

**FGFR oncogenic alterations:**
- **Point mutations (FGFR2 bladder: S249C, R248C; FGFR3 endometrial: N549K):** Cysteine mutations create unpaired cysteines → aberrant disulfide bonds → constitutive receptor homodimerization without ligand (similar to HER2 V659E); kinase domain mutations (K650E) → constitutive kinase activation
- **Gene fusions:** The most actionable class; FGFR2 fusions (intrahepatic CCA) and FGFR3 fusions (bladder, glioblastoma) retain the kinase domain fused to a dimerization-promoting partner → constitutive kinase activity; most common: FGFR2-BICC1, FGFR2-PPHLN1, FGFR3-TACC3
- **Amplification:** FGFR1 8p11-12 amplification → gene copy gain → protein overexpression → receptor homodimerization (paracrine FGF2 in tumor microenvironment); FGFR2 17q22-23 amplification in gastric cancer

## Function

### FGFR downstream signaling

**FRS2α-GRB2-SOS → RAS-MAPK axis:**
- FGFR autophosphorylation → FRS2α Y196/Y306/Y349/Y392 phosphorylation → GRB2 SH2 binding → SOS → RAS-GTP → RAF-MEK-ERK → proliferation
- FRS2α also recruits GRB2-GAB1 → PI3K → PIP3 → AKT
- FRS2α is the unique FGFR signaling adaptor (not used by EGFR/VEGFR) → makes FGFR signaling partially distinct

**PLCγ-PKC-DAG axis:**
- Activated FGFR directly phosphorylates PLCγ Y771/Y783 (via a unique C-lobe docking site) → PLCγ hydrolyzes PIP2 → DAG + IP3; DAG → PKCδ activation → MAPK; IP3 → ER calcium release → calmodulin-kinase activation → MAPK
- This PLCγ pathway is a uniquely strong axis in FGFR signaling (compared to EGFR which uses Grb2/Shc primarily)

**STAT signaling:**
- FGFR activates STAT1 and STAT3 in a JAK-independent manner → direct FGFR-STAT complex; STAT1 mediates anti-proliferative FGF signaling in some contexts; STAT3 mediates survival; FGFR1-STAT3 axis active in NSCLC with FGFR1 amplification

**Wnt pathway interaction:**
- FGF signaling stabilizes β-catenin through GSK3β inhibition (via AKT) → synergy with Wnt in stem cell maintenance and cancer; FGF-Wnt interactions regulate embryonic patterning (e.g., limb bud outgrowth: FGF10 from mesenchyme → FGFR2-IIIb in ectoderm → FGF8 → FGF10 loop)

### FGF ligand-receptor pairing

The 22 FGF ligands fall into 6 subfamilies with specific FGFR preferences:

| FGF subfamily | Key members | Receptor specificity | Biological role |
|-------------|-------------|---------------------|----------------|
| FGF1 | FGF1, FGF2 | All FGFRs (promiscuous) | Angiogenesis, wound healing |
| FGF4 | FGF4, FGF5, FGF6 | FGFR1c, FGFR2c | Embryogenesis |
| FGF7 | FGF7 (KGF), FGF10 | FGFR2-IIIb (keratinocytes) | Epithelial repair |
| FGF8 | FGF8, FGF17, FGF18 | FGFR3c, FGFR4 | CNS patterning |
| FGF19 | FGF19, FGF21, FGF23 | FGFR1 + Klotho (endocrine) | Metabolism, phosphate, bile acid |
| FGF11 (intracrine) | FGF11-14 | No FGFR binding | Intracellular (voltage-gated Na+ channel) |

**FGF19-FGFR4 axis in cancer:**
- FGF19 (hepatotropic hormone regulating bile acid synthesis) overexpressed in HCC (~25% of HCC); FGF19-FGFR4 → β-catenin → HCC proliferation; fisogatinib (FGFR4-selective) and roblitinib (FGFR4-selective) in clinical trials for FGFR4-positive HCC; KLOTHO-beta co-receptor required

## Mechanism

### FGFR inhibitors

**Erdafitinib (Balversa):**
- Pan-FGFR1/2/3/4 inhibitor (Type I, ATP-competitive); FDA-approved April 2019 for FGFR2/3-altered metastatic urothelial carcinoma
- THOR trial (2023): Erdafitinib vs. pembrolizumab in FGFR-altered cisplatin-pretreated urothelial carcinoma → OS 12.1 vs. 7.8 months; erdafitinib superior to immunotherapy in this selected population [^loriot-2019-erdafitinib]
- **Toxicity:** Hyperphosphatemia (FGF23/FGFR1 inhibition → reduced renal phosphate excretion → serum phosphate elevation; requires phosphate restriction and binders), central serous retinopathy (CSR), dry mouth, alopecia

**Pemigatinib (Pemazyre):**
- FGFR1/2/3-selective inhibitor; FDA-approved April 2020 for FGFR2 fusion/rearrangement-positive advanced cholangiocarcinoma (FIGHT-202 trial: ORR 36%, DCR 82%) [^abou-alfa-2020-pemigatinib]
- Also approved for FGFR1-rearranged myeloproliferative neoplasm (8p11 syndrome; ORR 79%)
- Toxicity: Hyperphosphatemia, alopecia, nail changes, stomatitis; ocular toxicity (CSR)

**Futibatinib (Lytgobi):**
- Covalent (irreversible) FGFR1/2/3/4 inhibitor; FDA-approved September 2022 for FGFR2 fusion/rearrangement-positive CCA (FOENIX-CCA2: ORR 42%)
- Covalent binding overcomes acquired point mutations (FGFR2 gatekeeper V564F, etc.) that cause resistance to reversible inhibitors (pemigatinib) → positioned for post-pemigatinib therapy

**Acquired resistance to FGFR inhibitors:**
- **Gatekeeper mutations (V564F/L, N550H/K in FGFR2):** Most common mechanism in CCA; sterically prevent inhibitor binding; futibatinib (covalent) and next-gen inhibitors (lirafugratinib, RLY-4008) designed to overcome V564 resistance
- **FGFR amplification:** Selection of high-copy amplified tumor cells resistant to current doses
- **Polyclonal resistance:** Multiple concurrent FGFR2 mutations identified in circulating tumor DNA → disease heterogeneity
- **Bypass signals:** Activation of KRAS, EGFR, or MET → FGFR-independent proliferation

**Combination strategies:**
- FGFR inhibitor + anti-PD-1: Rationale — FGFR signaling suppresses anti-tumor immune responses; combinations in clinical trials for bladder CCA
- FGFR inhibitor + CDK4/6 inhibitor: FGFR1 amplification in breast cancer + cell cycle; FGFR-dependent cyclin D1 upregulation → CDK4/6 dependence
- FGFR inhibitor + mTOR inhibitor: Dual blockade of FGFR1/2 and downstream mTORC1 in gastric cancer

## Connections

- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — FGFR and VEGFR co-regulate tumor angiogenesis; FGF2 → FGFR1 activates alternative angiogenesis, conferring bevacizumab resistance; lenvatinib and ponatinib target both FGFR and VEGFR; FGFR1-overexpressing endothelial cells resist anti-VEGF therapy through sustained ERK signaling.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — FGFR signals through PI3K-AKT → mTORC1 → protein synthesis and cell survival; mTOR inhibitors combined with FGFR inhibitors synergize in FGFR2-amplified gastric and breast cancer models; FGFR2 amplification activates mTORC1 independently of AKT in some gastric cancers.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — FGFR amplification and KRAS mutation co-occur in bladder and lung cancers; FGFR1 amplification can substitute for KRAS mutation in NSCLC; FGFR-KRAS converge on ERK → cyclin D1 → G1/S entry; FGFR3-KRAS co-alterations in bladder cancer portend worse prognosis.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — FGFR1/2/3 and EGFR share downstream RAS-MAPK and PI3K-AKT; FGF2-FGFR1 mediates resistance to EGFR TKIs in NSCLC and cetuximab in colorectal cancer; dual FGFR+EGFR inhibition restores TKI sensitivity in FGFR-driven EGFR-TKI-resistant NSCLC in preclinical models.
- `connects-to` → **[FGF23](../../03-molecular/fgf23/README.md)** — FGF23 signals via FGFR1c/αKlotho in kidney (phosphate excretion) and parathyroid (PTH suppression); FGFR4 drives cardiac hypertrophy in CKD at high FGF23 concentrations; FGFR inhibitors (erdafitinib) block FGF23/FGFR1 → hyperphosphatemia requiring phosphate management.
- `connects-to` → **[Bladder Cancer](../../07-system/bladder-cancer/README.md)** — FGFR3 mutations (S249C, R248C, K652E) and FGFR3-TACC3 fusions drive ~25-35% of urothelial carcinoma; erdafitinib (pan-FGFR inhibitor) FDA-approved for FGFR3-altered metastatic bladder cancer (THOR: OS 12.1 vs. 7.8 months vs. pembrolizumab in FGFR-selected patients).
- `connects-to` → **[Cholangiocarcinoma](../../07-system/cholangiocarcinoma/README.md)** — FGFR2 fusions/rearrangements in ~15-20% of intrahepatic cholangiocarcinoma; pemigatinib (FIGHT-202: ORR 36%) and futibatinib (FOENIX-CCA2: ORR 42%) are FDA-approved; covalent futibatinib overcomes gatekeeper V564F resistance to reversible pemigatinib.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^loriot-2019-erdafitinib]: Loriot Y, Necchi A, Park SH, et al. Erdafitinib in locally advanced or metastatic urothelial carcinoma. *N Engl J Med.* 2019;381(4):338-348. [doi:10.1056/NEJMoa1817323](https://doi.org/10.1056/NEJMoa1817323) · [PubMed 31340094](https://pubmed.ncbi.nlm.nih.gov/31340094/)
[^abou-alfa-2020-pemigatinib]: Abou-Alfa GK, Sahai V, Hollebecque A, et al. Pemigatinib for previously treated, locally advanced or metastatic cholangiocarcinoma. *Lancet Oncol.* 2020;21(5):671-684. [doi:10.1016/S1470-2045(20)30109-1](https://doi.org/10.1016/S1470-2045(20)30109-1) · [PubMed 32203698](https://pubmed.ncbi.nlm.nih.gov/32203698/)

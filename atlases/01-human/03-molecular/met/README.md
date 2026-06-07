---
schema: human-scale-entry/v1
id: met
name: MET
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Receptor tyrosine kinase for hepatocyte growth factor (HGF); MET amplification drives EGFR TKI resistance in NSCLC (~5-15% of acquired resistance); MET exon 14 skipping (~3-4% NSCLC) is a primary driver; capmatinib and tepotinib are approved MET inhibitors in METex14 NSCLC."
aliases: ["MET", "c-MET", "HGFR", "hepatocyte growth factor receptor", "METex14", "MET exon 14 skipping", "MET amplification"]
sources:
  - id: wolf-2020-capmatinib
    type: peer-reviewed
    cite: "Wolf J, Seto T, Han JY, et al. Capmatinib in MET exon 14-mutated or MET-amplified non-small-cell lung cancer. N Engl J Med. 2020;383(10):944-957."
    doi: "10.1056/NEJMoa2002787"
    pmid: "32877583"
    url: "https://doi.org/10.1056/NEJMoa2002787"
  - id: abou-alfa-2018-cabozantinib-hcc
    type: peer-reviewed
    cite: "Abou-Alfa GK, Meyer T, Cheng AL, et al. Cabozantinib in patients with advanced and progressing hepatocellular carcinoma. N Engl J Med. 2018;379(1):54-63."
    doi: "10.1056/NEJMoa1717002"
    pmid: "29972759"
    url: "https://doi.org/10.1056/NEJMoa1717002"
cross_links:
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "MET → GRB2/SOS → RAS-MAPK → ERK → proliferation; MET amplification in KRAS-wild-type colorectal cancer and NSCLC → RAS-ERK bypass loop; RAS mutation renders MET inhibition less effective; combined MET+MEK inhibition under study in MET-amplified GI cancers."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "HGF-MET → PI3K-AKT → mTOR → S6K → ribosomal biogenesis and cell growth; mTOR is a key effector of MET oncogenic signaling in MET-amplified cancers; MET inhibitors (capmatinib) + mTOR inhibitors studied in MET-amplified HCC and gastric cancer as combination approaches."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "MET activation → HIF-1alpha stabilization → VEGF secretion → paracrine angiogenesis; HGF and VEGF are co-upregulated in malignant ascites; cabozantinib (MET+VEGFR2 inhibitor) approved for HCC and RCC — dual targeting more effective than monotherapy in these tumors."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "MET amplification is a major mechanism of acquired EGFR TKI resistance; MET bypasses EGFR → PI3K-AKT + RAS-MAPK independently; amivantamab (EGFR+MET bispecific) approved for EGFR exon 20 NSCLC; osimertinib+savolitinib studied in MET-amplified osimertinib-resistant NSCLC."
---

# MET

## Overview

**MET (also called c-MET or HGFR — hepatocyte growth factor receptor)** is a receptor tyrosine kinase encoded at chromosome 7q31 that is the sole high-affinity receptor for **hepatocyte growth factor (HGF, also called scatter factor)**. Under normal physiology, MET-HGF signaling governs branching morphogenesis (kidney, mammary gland, lung), liver regeneration, wound healing, and epithelial-mesenchymal transition (EMT) during development. In cancer, MET is activated via multiple mechanisms — point mutations (exon 14 skipping), amplification, overexpression, and autocrine HGF loops — driving proliferation, survival, invasion, and metastasis [^wolf-2020-capmatinib].

**MET in cancer:**
- **MET exon 14 skipping (METex14, ~3-4% of NSCLC):** Splice-site mutations at intron 13-14 or exon 14 splice acceptor → exon 14 deletion → loss of Y1003 (CBL ubiquitin ligase binding site) → impaired MET degradation → prolonged kinase signaling; primary oncogenic driver in lung adenocarcinoma (enriched in elderly, female, never-smokers); **capmatinib and tepotinib FDA approved** as first-line targeted therapy [^wolf-2020-capmatinib]
- **MET amplification:** Secondary/acquired driver; MET gene copy number gain (focal amplification) → constitutive MET signaling without mutation; most important as **acquired resistance mechanism to EGFR TKIs** in NSCLC (~5-15% of osimertinib resistance); also primary driver in a subset of gastric, esophageal, and HCC
- **MET overexpression:** Without amplification; very common in many cancers (breast, colorectal, HCC, gastric) but biologically heterogeneous
- **MET mutations (other than exon 14):** D1228N/H, Y1230C/H/S (kinase domain) — selected by MET inhibitors; activation loop mutations in MTC and sporadic papillary renal cell carcinoma
- **NSCLC:** Capmatinib or tepotinib approved for METex14-skipping NSCLC; MET-directed amivantamab+lazertinib for EGFR mutant NSCLC with MET resistance
- **HCC:** MET overexpressed in ~50% of HCC; cabozantinib (MET+VEGFR2+AXL inhibitor) approved second-line; tivantinib (selective MET inhibitor) failed phase III in MET-high HCC
- **Gastric cancer:** MET amplification in ~10-20%; amivantamab (EGFR+MET) under evaluation

## Structure

### MET protein architecture

MET is a 190 kDa single-chain heterodimer (after cleavage of precursor into α and β chains linked by disulfide):

**Extracellular domain (ECD):**
- **α-chain (N-terminal, 1-307):** Contains a **Sema domain** (semaphorin homology) that forms the HGF binding site; Sema domain of MET undergoes conformational change upon HGF binding → receptor homodimerization
- **β-chain ECD (308-932):** Plexin-semaphorin-integrin (PSI) domain + four IPT (immunoglobulin-plexin-transcription factor) domains → structural scaffolding and co-receptor interaction

**Transmembrane domain (TM, ~933-956):** Single pass

**Intracellular domain:**
- **Juxtamembrane domain (JM, ~957-1009):** Contains **Y1003** — docking site for CBL E3 ubiquitin ligase → MET ubiquitination and lysosomal degradation; **exon 14 encodes Y1003-containing JM segment** → METex14 skipping eliminates Y1003 → impaired MET degradation → protein accumulation
- **Kinase domain (~1010-1275):** Bilobal kinase; activation loop Y1234/Y1235 → trans-autophosphorylation; gatekeeper residue L1193; **D1228** and **Y1230** in kinase domain — mutation hotspots for secondary resistance to type I MET inhibitors (capmatinib, tepotinib); type II inhibitors (cabozantinib) retain activity against some KD resistance mutants
- **C-terminal docking site (~1349-1390):** Multi-substrate docking region containing Y1349 and Y1356; phosphorylated upon activation → recruits GRB2, SHC, GAB1, PI3K, SRC, STAT3, PLCγ → divergent downstream signaling

### METex14 molecular mechanism

**Normal exon 14 splicing:** Exon 14 encodes amino acids ~963-1009 (the juxtamembrane region including Y1003); normal splicing retains exon 14 → Y1003 expressed → CBL binding → ubiquitination → proteasomal/lysosomal degradation → MET signal termination

**METex14 skipping mutations:**
- Splice site mutations at 3' end of intron 13 (polypyrimidine tract, branch point) or 5' end of intron 14 → altered splice site recognition → skipping of exon 14
- Also: in-frame deletions within exon 14 that remove Y1003 → same effect
- Result: MET protein lacking the JM degradation signal → extended plasma membrane residence → prolonged kinase activity → oncogenic gain

## Function

### Normal HGF-MET signaling

**HGF binding and receptor activation:**
HGF (a two-chain scatter factor cleaved by serine proteases) binds with high affinity to the Sema domain of MET → MET homodimerization → trans-autophosphorylation at Y1234/Y1235 → docking domain phosphorylation (Y1349/Y1356) → adaptor recruitment:

- **GAB1 (GRB2-associated binder 1):** Primary docking adaptor; GAB1 amplifies PI3K (p85 binding) and SHP2 → RAS-MAPK; GAB1 binding is essential for invasive branching morphogenesis
- **GRB2-SOS:** → RAS → MEK → ERK → proliferation and survival
- **PI3K-AKT-mTOR:** → growth, survival, glucose metabolism
- **STAT3:** Direct MET-STAT3 phosphorylation → immune evasion, invasion
- **SRC-FAK:** → actin cytoskeleton remodeling, integrin co-signaling → invasion and migration
- **PLCγ:** → PKC → motility

**Physiological roles of HGF-MET:**
- **Liver regeneration:** HGF is the primary hepatotrophic growth factor; hepatectomy → massive HGF release → MET-driven hepatocyte proliferation → regeneration within days
- **Kidney development:** MET on ureteric bud → HGF from mesenchyme → branching morphogenesis; MET KO → renal hypoplasia
- **Muscle progenitor migration:** MET-HGF → limb muscle precursor migration from somites → limb muscle development; conditional MET KO → diaphragm and limb muscle defects
- **Wound healing:** MET → keratinocyte migration → re-epithelialization

## Mechanism

### MET inhibitors

**Selective type Ib MET inhibitors (ATP-competitive):**

**Capmatinib (INC280, Tabrecta):**
- Highly selective; binds active conformation of MET kinase
- **GEOMETRY mono-1 trial:** [^wolf-2020-capmatinib] METex14-skipping NSCLC:
  - Treatment-naive: ORR 68%, median DOR 12.6 months
  - Previously treated: ORR 41%, median DOR 9.7 months
- FDA approved 2020 for METex14-skipping NSCLC
- Active against MET amplification (gene copy number ≥10)
- Resistance: D1228N/H, Y1230C/H → kinase domain mutations within binding site

**Tepotinib (MSC2156119J, Tepmetko):**
- Selective type Ib; similar profile to capmatinib
- **VISION trial:** METex14 NSCLC: ORR 46% liquid biopsy, 48% tissue biopsy
- FDA approved 2021 for METex14-skipping NSCLC

**Non-selective (type II) MET inhibitors:**

**Cabozantinib (XL184, Cabometyx, Cometriq):**
- Multikinase: MET + VEGFR2 + AXL + KIT + RET + FLT3
- **HCC (CELESTIAL trial):** [^abou-alfa-2018-cabozantinib-hcc] OS 10.2 vs. 8.0 months after sorafenib; ORR 4%; approved 2019 for second-line HCC
- Also approved: advanced RCC (first-line in combination with nivolumab; CABOSUN trial), medullary thyroid cancer, pheochromocytoma/paraganglioma (compassionate use)
- Overcomes some type Ib resistance mutations (D1228N) due to different binding mode

**Savolitinib (AZD6094):**
- Selective; under study in NSCLC: osimertinib + savolitinib in MET-amplified osimertinib-resistant NSCLC (TATTON trial → ORR ~67% in MET-amplified arm)

### Amivantamab (EGFR×MET bispecific antibody)

Amivantamab (JNJ-6372) is a human IgG1-based bispecific antibody targeting EGFR and MET extracellular domains:
- Blocks ligand (EGF and HGF) binding to respective receptors
- Induces receptor downregulation (trogocytosis-mediated)
- ADCC and ADCP via Fc-FcγRIII interactions → immune-mediated tumor cell killing
- **PAPILLON trial:** Amivantamab + chemotherapy in EGFR exon 20 insertion NSCLC → PFS 11.4 vs. 6.7 months; FDA approved 2024 as first-line for EGFR exon 20 insertions
- **MARIPOSA-2 trial:** Amivantamab + chemotherapy ± lazertinib in osimertinib-resistant EGFR-mutant NSCLC with EGFR or MET alterations

### MET resistance mechanisms

**Primary resistance to METex14 inhibitors:**
- MET Y1230C/H: Alters drug-binding position in activation loop; particularly resistant to type Ib inhibitors
- MET D1228N/H: Affects hydrophobic interaction with capmatinib/tepotinib
- KRAS mutations: Downstream bypass — MET inhibition ineffective if RAS already mutated
- MET-independent signaling through EGFR, ERBB3

**Acquired resistance:**
- Kinase domain mutations (above)
- MET amplification in already-amplified tumors (super-amplification)
- Alternative pathway activation (KRAS/BRAF secondary mutations, EGFR overexpression)

## Connections

- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — MET → GRB2/SOS → RAS-MAPK → ERK → proliferation; MET amplification in KRAS-wild-type colorectal cancer and NSCLC → RAS-ERK bypass loop; RAS mutation renders MET inhibition less effective; combined MET+MEK inhibition under study in MET-amplified GI cancers.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — HGF-MET → PI3K-AKT → mTOR → S6K → ribosomal biogenesis and cell growth; mTOR is a key effector of MET oncogenic signaling in MET-amplified cancers; MET inhibitors (capmatinib) + mTOR inhibitors studied in MET-amplified HCC and gastric cancer as combination approaches.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — MET activation → HIF-1alpha stabilization → VEGF secretion → paracrine angiogenesis; HGF and VEGF are co-upregulated in malignant ascites; cabozantinib (MET+VEGFR2 inhibitor) approved for HCC and RCC — dual targeting more effective than monotherapy in these tumors.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — MET amplification is a major mechanism of acquired EGFR TKI resistance; MET bypasses EGFR → PI3K-AKT + RAS-MAPK independently; amivantamab (EGFR+MET bispecific) approved for EGFR exon 20 NSCLC; osimertinib+savolitinib studied in MET-amplified osimertinib-resistant NSCLC.

[^wolf-2020-capmatinib]: Wolf J, Seto T, Han JY, et al. Capmatinib in MET exon 14-mutated or MET-amplified non-small-cell lung cancer. *N Engl J Med.* 2020;383(10):944-957. [doi:10.1056/NEJMoa2002787](https://doi.org/10.1056/NEJMoa2002787) · [PubMed 32877583](https://pubmed.ncbi.nlm.nih.gov/32877583/)
[^abou-alfa-2018-cabozantinib-hcc]: Abou-Alfa GK, Meyer T, Cheng AL, et al. Cabozantinib in patients with advanced and progressing hepatocellular carcinoma. *N Engl J Med.* 2018;379(1):54-63. [doi:10.1056/NEJMoa1717002](https://doi.org/10.1056/NEJMoa1717002) · [PubMed 29972759](https://pubmed.ncbi.nlm.nih.gov/29972759/)

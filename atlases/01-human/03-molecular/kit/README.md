---
schema: human-scale-entry/v1
id: kit
name: KIT
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "KIT (CD117) is a type III RTK activated by SCF; KIT gain-of-function mutations in ~85% of GIST (exon 11 juxtamembrane most common) and KIT D816V in systemic mastocytosis; imatinib is first-line for GIST; avapritinib is approved for PDGFRA D842V and systemic mastocytosis."
aliases: ["KIT", "c-KIT", "CD117", "SCFR", "stem cell factor receptor", "KIT mutation", "KIT D816V", "imatinib GIST", "tyrosine kinase KIT", "gastrointestinal stromal tumor KIT"]
sources:
  - id: demetri-2002-imatinib-gist
    type: peer-reviewed
    cite: "Demetri GD, von Mehren M, Blanke CD, et al. Efficacy and safety of imatinib mesylate in advanced gastrointestinal stromal tumors. N Engl J Med. 2002;347(7):472-480."
    doi: "10.1056/NEJMoa020461"
    pmid: "12181401"
    url: "https://doi.org/10.1056/NEJMoa020461"
  - id: joensuu-2012-ssg18
    type: peer-reviewed
    cite: "Joensuu H, Eriksson M, Sundby Hall K, et al. One vs three years of adjuvant imatinib for operable gastrointestinal stromal tumor: a randomized trial. JAMA. 2012;307(12):1265-1272."
    doi: "10.1001/jama.2012.347"
    pmid: "22453568"
    url: "https://doi.org/10.1001/jama.2012.347"
cross_links:
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "PDGFRA (type III RTK paralog of KIT) is mutated in ~10% of GIST; PDGFRA D842V (exon 18) → imatinib-resistant; avapritinib (NAVIGATOR trial: ORR 84%) is FDA approved for PDGFRA D842V GIST; KIT and PDGFRA are mutually exclusive in GIST."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "KIT → PI3K-δ → AKT → mTOR → cell survival and growth in GIST; mTOR activation is a resistance mechanism to imatinib in KIT-mutant GIST; everolimus + imatinib combination studied in R/R GIST; mTOR/PI3K inhibitors synergize with KIT inhibitors in GIST models."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "KIT → GRB2-SOS → RAS → RAF → MEK → ERK1/2 → proliferation in GIST; ERK1/2 activity is a surrogate marker for KIT inhibition; rebound ERK activation via feedback RAF → MEK → ERK is a resistance mechanism; MEK+KIT dual inhibition studied in imatinib-resistant GIST."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC kinase is activated downstream of KIT Tyr568/570 → FAK-SRC complex → invasion in GIST; SRC mediates KIT-independent survival in imatinib-resistant GIST; dasatinib (KIT+SRC) studied in imatinib-resistant GIST; SRC contributes to resistance to selective KIT inhibitors."
---

# KIT

## Overview

**KIT (c-KIT, CD117)** is a type III receptor tyrosine kinase (RTK) that serves as the receptor for **stem cell factor (SCF, also called KITLG or Steel factor)**. KIT belongs to the same RTK subfamily as PDGFRA, PDGFRB, FLT3, and CSF1R — all sharing an extracellular immunoglobulin-like domain structure and cytoplasmic split kinase domain. Physiologically, KIT signaling is essential for: hematopoietic stem cell (HSC) self-renewal and survival, mast cell development and function, interstitial cell of Cajal (ICC) differentiation in the GI tract (the pacemaker cells of gut motility), germ cell (spermatogonia/oogonia) development, and melanocyte migration from neural crest. In cancer, **KIT gain-of-function mutations** create constitutively active receptor dimers independent of SCF ligand, driving uncontrolled proliferation of KIT-expressing cells — most importantly in **gastrointestinal stromal tumors (GIST)** where KIT mutations define the vast majority of cases. Imatinib mesylate (Gleevec), developed initially for BCR-ABL1 in CML, was found to potently inhibit KIT → first FDA approval for GIST in 2002 [^demetri-2002-imatinib-gist].

**KIT in cancer:**
- **GIST:** KIT exon 11 (juxtamembrane) ~70%; exon 9 (extracellular) ~10%; exon 13/17 (kinase domain) ~3-5%; imatinib highly active for exon 11 (ORR ~80%); exon 9 requires higher-dose imatinib (800 mg/day) or sunitinib
- **Systemic mastocytosis:** KIT D816V (exon 17, activation loop) in >90%; constitutive KIT → mast cell proliferation; imatinib-resistant (D816V changes binding pocket); avapritinib (allosteric KIT D816V inhibitor) FDA approved 2021 for advanced systemic mastocytosis (PATHFINDER trial: ORR 75%)
- **Acute myeloid leukemia (AML):** KIT exon 17 mutations in ~4% of AML; especially core-binding factor AML [t(8;21) + inv(16)]; adverse prognostic impact; midostaurin active
- **Melanoma (mucosal/acral):** KIT mutations/amplifications ~15-20% of mucosal melanoma; imatinib/sunitinib active in KIT-mutant mucosal melanoma (~20% ORR); rare compared to BRAF-mutant cutaneous melanoma
- **Seminoma/germ cell tumors:** KIT mutations (exon 11/17) in ~20% of seminoma; associated with bilateral germ cell tumors

## Structure

### KIT receptor architecture

KIT is a 976-amino-acid, 145 kDa single-pass transmembrane glycoprotein:

**Extracellular domain (ECD, 1-521):**
- 5 immunoglobulin-like (Ig-like) domains (D1-D5): D1-D3 form the ligand-binding module; D4-D5 mediate receptor dimerization; SCF binding → homotypic D4-D4 and D5-D5 KIT dimerization → receptor clustering
- Exon 9 mutations (Ala502_Tyr503dup): Duplications in D5 → constitutive dimerization without SCF; ~10% of GIST; extracellular-domain activation mechanism

**Transmembrane domain (TM, 522-544):** Single helix pass

**Juxtamembrane domain (JMD, 545-582):**
- Autoinhibitory segment; restrains KIT kinase domain in inactive conformation
- **Exon 11 mutations (~70% of GIST):** Point mutations, in-frame deletions (del557-558 most common), or insertions in JMD → relieve JMD autoinhibition → constitutive kinase activity; highest imatinib sensitivity (ORR >80%)
- W557, V559, L576P, del557-558: Most common oncogenic exon 11 mutations

**Kinase domain — KD1 (583-665), ATP-binding cleft and KD2 (665-936):**
- Split kinase domain (KD1 + KD2) separated by kinase insert domain (KID, 665-740): Characteristic of type III RTKs
- Activation loop (A-loop): Tyr823; phosphorylation → kinase activation; **KIT D816V** (Asp816→Val in A-loop) → A-loop adopts activated conformation without phosphorylation → constitutive activity; imatinib binds inactive KIT conformation (DFG-out) → D816V preferentially adopts DFG-in → imatinib cannot bind
- Exon 13 (V654A): Gatekeeper mutation → acquired imatinib resistance; sunitinib partially active
- Exon 17 (D816V, D820G, N822K): Activation loop mutations → primary or acquired resistance; avapritinib (type I1/2 inhibitor) active against D816V

### KIT signaling downstream

**SCF binding → KIT dimerization → autophosphorylation cascade:**
1. Tyr568/570 (JMD): SRC family kinase (LYN, FYN) docking → SRC activation → STAT3/STAT5
2. Tyr703/721 (KID): SHP2/PI3K regulatory subunit (p85) docking → PI3K-δ → PIP3 → AKT → mTOR
3. Tyr936 (KD2): GRB2 → SOS → RAS → RAF → MEK → ERK1/2
4. Tyr805/821/823: Additional scaffolding; PLCγ → IP3 → Ca²⁺; CBL E3 ubiquitin ligase → KIT ubiquitination → endocytosis (receptor downregulation)

**KIT gain-of-function → constitutive activation of all downstream arms:**
PI3K-AKT-mTOR: cell growth and survival; RAS-ERK: proliferation; STAT3/5: anti-apoptosis; inhibition of all arms by upstream KIT inhibition → KIT addiction.

## Function

### Normal KIT roles

**Interstitial cells of Cajal (ICC) — GI pacemaker:**
ICC are the pacemaker cells of the GI tract, generating slow electrical waves that coordinate smooth muscle contraction and peristalsis. ICC require KIT-SCF signaling for development, survival, and maintenance — ICC are absent in KIT-deficient (White Spotting, W/Wv) mice → intestinal pseudo-obstruction. GIST arises from ICC or ICC precursors → both normal ICC and GIST cells are CD117+/DOG1+.

**Hematopoiesis:**
SCF-KIT signaling maintains HSC self-renewal and early progenitor (mast cell, megakaryocyte-erythroid) proliferation. KIT-SCF mediates the HSC niche interaction (BM stroma secretes membrane-bound SCF → KIT on HSC → retention in BM niche + self-renewal). c-Kit W-sash (W/Wv) mice: Defective mast cells, anemia (impaired erythropoiesis), sterility (germ cell failure).

**Mast cell development:**
Mast cells are uniquely KIT-dependent — all mast cells constitutively express high-surface KIT; SCF → KIT → proliferation, survival, and IgE receptor upregulation; mast cell activation (IgE-allergen crosslink) is the effector arm of allergy/anaphylaxis. Mastocytosis: KIT D816V → constitutive mast cell proliferation independent of SCF.

### KIT inhibitor selectivity and resistance

**Imatinib selectivity:**
Imatinib binds the ATP-binding cleft in the KIT kinase domain (DFG-out inactive conformation); inhibits KIT Km for ATP; also inhibits PDGFRA, PDGFRB, ABL1, and BCR-ABL1 via structural homology; IC50 KIT exon 11 WT: ~0.1 μM; much less active against KIT D816V (active/DFG-in conformation).

**Sunitinib (multitarget TKI: KIT, VEGFR1/2/3, PDGFRA/B, FLT3, CSF1R):**
Active against KIT exon 13 (V654A), exon 14 (T670I — gatekeeper), and exon 9 mutations (partial activity); second-line GIST after imatinib progression; median PFS 27 weeks vs. 6 weeks placebo; FDA approved 2006.

**Ripretinib (switch-pocket inhibitor: KIT + PDGFRA):**
Novel mechanism: binds both the ATP site AND the switch pocket (DFG switch → B helix) → locks KIT in inactive DFG-out/A-loop-up conformation; active against primary and secondary KIT exon 11/17 resistance mutations; FDA approved 2020 for 4th-line GIST.

**Avapritinib (PDGFRA D842V + KIT D816V):**
Type I1/2 allosteric inhibitor; binds DFG-in active conformation; active against KIT D816V (mastocytosis) and PDGFRA D842V (GIST); FDA approved 2020 for PDGFRA D842V GIST and 2021 for systemic mastocytosis.

## Mechanism

### Imatinib resistance in GIST

**Primary resistance (~10-15% of patients):**
- PDGFRA D842V → imatinib IC50 100-fold higher than exon 11; → avapritinib
- SDH-deficient GIST (SDHB-/+, KIT/PDGFRA WT): Imatinib ineffective; succinate dehydrogenase complex loss → HIF-2α activation → VEGF; no standard molecular target
- NF1-mutant GIST: NF1 loss → RAS activation; no KIT/PDGFRA mutation; MEK inhibitor activity shown

**Acquired resistance (~50-60% after 2 years of imatinib):**
- Secondary KIT kinase domain mutations (exon 13: V654A; exon 17: D820G, N822K, Y823D) → reduced imatinib binding
- Secondary KIT A-loop mutations → DFG-in conformation → resistant to imatinib (DFG-out binder)
- Heterogeneous clonal resistance: Multiple different secondary mutations in different metastatic sites; pan-KIT approach (ripretinib) or avapritinib for D816V-like mutations

## Connections

- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — PDGFRA (type III RTK paralog of KIT) is mutated in ~10% of GIST; PDGFRA D842V (exon 18) → imatinib-resistant; avapritinib (NAVIGATOR trial: ORR 84%) is FDA approved for PDGFRA D842V GIST; KIT and PDGFRA are mutually exclusive in GIST.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — KIT → PI3K-δ → AKT → mTOR → cell survival and growth in GIST; mTOR activation is a resistance mechanism to imatinib in KIT-mutant GIST; everolimus + imatinib combination studied in R/R GIST; mTOR/PI3K inhibitors synergize with KIT inhibitors in GIST models.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — KIT → GRB2-SOS → RAS → RAF → MEK → ERK1/2 → proliferation in GIST; ERK1/2 activity is a surrogate marker for KIT inhibition; rebound ERK activation via feedback RAF → MEK → ERK is a resistance mechanism; MEK+KIT dual inhibition studied in imatinib-resistant GIST.
- `connects-to` → **[SRC kinase](../../03-molecular/src-kinase/README.md)** — SRC kinase is activated downstream of KIT Tyr568/570 → FAK-SRC complex → invasion in GIST; SRC mediates KIT-independent survival in imatinib-resistant GIST; dasatinib (KIT+SRC inhibitor) studied in imatinib-resistant GIST; SRC contributes to resistance to selective KIT inhibitors.

[^demetri-2002-imatinib-gist]: Demetri GD, von Mehren M, Blanke CD, et al. Efficacy and safety of imatinib mesylate in advanced gastrointestinal stromal tumors. *N Engl J Med.* 2002;347(7):472-480. [doi:10.1056/NEJMoa020461](https://doi.org/10.1056/NEJMoa020461) · [PubMed 12181401](https://pubmed.ncbi.nlm.nih.gov/12181401/)
[^joensuu-2012-ssg18]: Joensuu H, Eriksson M, Sundby Hall K, et al. One vs three years of adjuvant imatinib for operable gastrointestinal stromal tumor: a randomized trial. *JAMA.* 2012;307(12):1265-1272. [doi:10.1001/jama.2012.347](https://doi.org/10.1001/jama.2012.347) · [PubMed 22453568](https://pubmed.ncbi.nlm.nih.gov/22453568/)

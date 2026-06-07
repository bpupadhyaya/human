---
schema: human-scale-entry/v1
id: jak2
name: JAK2
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "JAK2 non-receptor tyrosine kinase mediates EPO, TPO, and cytokine receptor signaling via STAT5/STAT3; JAK2 V617F pseudokinase domain mutation causes constitutive kinase activity in polycythemia vera (>95%), essential thrombocythemia, and myelofibrosis; ruxolitinib is approved."
aliases: ["JAK2", "Janus kinase 2", "JAK2 V617F", "ruxolitinib", "JAK-STAT signaling", "polycythemia vera JAK2", "myeloproliferative neoplasm JAK2"]
sources:
  - id: baxter-2005-jak2-v617f
    type: peer-reviewed
    cite: "Baxter EJ, Scott LM, Campbell PJ, et al. Acquired mutation of the tyrosine kinase JAK2 in human myeloproliferative disorders. Lancet. 2005;365(9464):1054-1061."
    doi: "10.1016/S0140-6736(05)71142-9"
    pmid: "15781101"
    url: "https://doi.org/10.1016/S0140-6736(05)71142-9"
  - id: verstovsek-2012-ruxolitinib-mf
    type: peer-reviewed
    cite: "Verstovsek S, Mesa RA, Gotlib J, et al. A double-blind, placebo-controlled trial of ruxolitinib for myelofibrosis. N Engl J Med. 2012;366(9):799-807."
    doi: "10.1056/NEJMoa1110557"
    pmid: "22375971"
    url: "https://doi.org/10.1056/NEJMoa1110557"
cross_links:
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "JAK2 → STAT5 (primary) and STAT3 → BCL-XL, MYC, cyclin D1 → proliferation; V617F → constitutive STAT5 phosphorylation → EPO-independent erythropoiesis in PV; STAT5 is the primary effector of JAK2-driven erythropoiesis and thrombocytopoiesis."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "EPO → EPOR → JAK2 trans-autophosphorylation at Tyr1007/1008 → STAT5 → erythroid differentiation; JAK2 V617F mimics EPO-occupied receptor → constitutive erythroid proliferation without EPO in PV; serum EPO is suppressed in PV and elevated in secondary polycythemia."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 → IL-6R/gp130 → JAK1/JAK2 → STAT3 phosphorylation → acute phase response and inflammatory cytokines; MF is characterized by elevated IL-6, IL-8, TNF-α (JAK2-driven cytokine storm); ruxolitinib reduces circulating inflammatory cytokines in MF."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "JAK2 → PI3K → AKT → mTOR signaling in MPN; JAK2 V617F activates mTORC1 independent of insulin signaling; mTOR inhibitors (everolimus) showed modest single-agent activity in MF; combined JAK+mTOR inhibition studied in high-risk MPN."
---

# JAK2

## Overview

**JAK2 (Janus Kinase 2)** is a non-receptor tyrosine kinase of the Janus kinase (JAK) family, essential for cytokine receptor signaling in hematopoiesis — particularly erythropoietin (EPO/EPOR), thrombopoietin (TPO/MPL), granulocyte colony-stimulating factor (G-CSF/GCSFR), and growth hormone (GH/GHR) signal transduction. JAK2 associates constitutively with the intracellular domains of these receptors and undergoes trans-autophosphorylation upon ligand binding, leading to phosphorylation and activation of STAT5 (primary), STAT3, and downstream PI3K/AKT/mTOR and RAS/MAPK pathways. The discovery of the **JAK2 V617F mutation** in 2005 was a landmark, revealing that a single somatic mutation in the pseudokinase domain drives constitutive JAK2 activation and three distinct myeloproliferative neoplasms (MPN): polycythemia vera (PV), essential thrombocythemia (ET), and myelofibrosis (MF) [^baxter-2005-jak2-v617f]. Ruxolitinib (Jakafi), a JAK1/2 inhibitor, became the first approved targeted therapy for MF in 2011 and for PV in 2014 [^verstovsek-2012-ruxolitinib-mf].

**JAK2 in cancer and hematologic disease:**
- **Polycythemia vera (PV):** JAK2 V617F in >95%; exon 12 mutations in ~3% of JAK2 V617F-negative PV; constitutive erythropoiesis → elevated RBC mass/hematocrit; thrombosis risk; ruxolitinib or hydroxyurea
- **Essential thrombocythemia (ET):** JAK2 V617F ~55%, CALR (calreticulin) mutations ~25%, MPL W515L/K ~5%; platelet overproduction → thrombosis and hemorrhage
- **Primary myelofibrosis (MF):** JAK2 V617F ~60%, CALR ~25%, MPL ~5%; fibrotic marrow → cytopenias, splenomegaly, constitutional symptoms; ruxolitinib for symptoms; alloSCT for high-risk
- **AML transformation:** MPN → blast-phase AML in ~5-10% (JAK2 mutation alone insufficient; requires additional mutations — IDH1/2, ASXL1, TP53)
- **JAK2 amplification:** Some T-ALL, B-ALL cases; Ph-like ALL (JAK2 rearrangements → CRLF2-JAK2, PCM1-JAK2)

**Driver mutation landscape (triple-negative MPN):**
~10-15% of ET/MF are "triple-negative" (no JAK2/CALR/MPL) → may have CSF3R, LNK (SH2B3), or EPOR mutations; JAK-STAT pathway still activated via downstream mechanisms.

## Structure

### JAK2 protein architecture

JAK2 is a 131 kDa cytoplasmic kinase, 1132 amino acids, organized into 7 JAK homology (JH) domains:

**FERM domain (JH6-JH7, N-terminal):**
- Four-point-one-Ezrin-Radixin-Moesin domain; mediates constitutive association with cytokine receptor box1/box2 motifs
- FERM domain mutations in AT-polycythemia (JAK2 FERM mutants impair receptor association)

**SH2-like domain (JH5):**
- Non-canonical SH2; not phosphotyrosine-binding; structural role in FERM-kinase coupling

**Pseudokinase domain (JH2):**
- Catalytically impaired kinase domain; primary autoinhibitory role — JH2 suppresses JH1 (active kinase) by stabilizing inactive conformation
- **JAK2 V617F (Val617→Phe):** Gain-of-function mutation in the JH2 hydrophobic interface → disrupts JH2-mediated autoinhibition → JH1 constitutively active even in absence of cytokine
- V617F located in JH2 αC helix equivalent; found in >95% of PV, ~55% of ET, ~60% of MF

**Kinase domain (JH1):**
- Active tyrosine kinase domain; Tyr1007/Tyr1008 in activation loop — primary autophosphorylation sites (equivalent to SRC Tyr527/Tyr530 regulation but auto-activating)
- ATP-binding site: ruxolitinib, fedratinib, pacritinib bind the ATP-binding cleft; type I inhibitors (bind active conformation); type II inhibitors under development

### JAK2 V617F molecular mechanism

**Normal JAK2 (OFF state):**
EPOR (unliganded) → JAK2 FERM bound to receptor → JH2 (pseudokinase) contacts JH1 (kinase) → autoinhibitory interaction maintains JH1 in inactive conformation → no STAT5 phosphorylation.

**Normal JAK2 (EPO-stimulated ON state):**
EPO → EPOR dimerization → JAK2 dimerization → trans-autophosphorylation at JH1 Tyr1007/1008 → JH2 autoinhibition relieved → STAT5 Tyr694 phosphorylation → STAT5 dimerization → nuclear translocation → GATA1, BCL-XL, PIM1, cyclin D1 transcription → erythroid proliferation and survival.

**JAK2 V617F (constitutive ON state):**
V617F Phe substitution in JH2 → bulkier side chain → steric disruption of JH2 autoinhibitory interaction with JH1 → JH1 constitutively active → autonomous STAT5/STAT3/ERK/PI3K phosphorylation → EPO/TPO-independent proliferation → MPN phenotype.

### JAK inhibitor binding

**Ruxolitinib (Jakafi — Incyte):**
Type I JAK1/2 inhibitor; binds ATP-binding pocket (binds both JAK1 and JAK2 active conformation); IC50: JAK1 3.3 nM, JAK2 2.8 nM; potent STAT3/STAT5 dephosphorylation; reduces spleen volume and constitutional symptoms in MF; toxicities: anemia and thrombocytopenia (on-target EPO/TPO signaling suppression), cytopenias, opportunistic infections (PJP, reactivation herpes zoster, HBV)

**Fedratinib (Inrebic — BMS):**
JAK2-selective inhibitor (JAK2 > JAK1); FDA approved 2019 for MF; active after ruxolitinib failure; risk of Wernicke encephalopathy (monitor thiamine levels)

**Pacritinib (Vonjo — CTI BioPharma):**
JAK2/FLT3/IRAK1 inhibitor; FDA approved 2022 for MF with platelet count <50 × 10⁹/L (PERSIST-2, PAC203 trials); spares JAK1 → less immunosuppression; useful for patients too cytopenic for ruxolitinib

**Momelotinib (Ojjaara — GSK):**
JAK1/2/ACVR1 inhibitor; FDA approved 2023 for MF with anemia; ACVR1 inhibition → blocks hepcidin induction → improves anemia independent of EPO pathway; MOMENTUM trial showed superior TSS reduction vs danazol

## Function

### Normal JAK2 hematopoietic signaling

**Erythropoiesis (EPO-EPOR-JAK2-STAT5):**
Hypoxia → EPO synthesis in renal cortical interstitial cells (HIF-2α-dependent) → EPO binds preformed EPOR homodimer → JAK2 trans-autophosphorylation → STAT5 phosphorylation → GATA1 target genes → BFU-E → CFU-E → reticulocyte → erythrocyte. Without JAK2 (mouse knockout), embryonic death from failure of definitive erythropoiesis.

**Thrombopoiesis (TPO-MPL-JAK2-STAT5):**
TPO → MPL (thrombopoietin receptor, CD110) → JAK2 → STAT5 → megakaryocyte differentiation → platelet biogenesis. MPL mutations (W515L/K) in JAK2/CALR-negative ET/MF → constitutive TPO-independent megakaryopoiesis.

**JAK2 downstream effectors:**
1. STAT5 (primary): ERK → survival; BCL-XL, BCL-2 → anti-apoptosis; PIM1, PIM2 kinases → additional survival signals
2. STAT3: Inflammatory cytokine production; overlap with IL-6 signaling
3. PI3K → AKT → mTOR: Cell growth, translation
4. RAS → MEK → ERK: Proliferation

### JAK2 V617F allele burden and MPN phenotype

The same V617F mutation produces different MPN phenotypes depending on allele burden and cellular context:
- **Heterozygous V617F:** ET phenotype (predominant platelet expansion)
- **Homozygous V617F (uniparental disomy 9p):** PV phenotype (erythrocyte expansion); ~25-30% of PV are homozygous V617F
- CALR mutations (ET/MF) → activate MPL → megakaryocyte-dominant phenotype without erythrocytosis

## Mechanism

### Ruxolitinib in MPN

**Myelofibrosis (COMFORT-I/II trials):** [^verstovsek-2012-ruxolitinib-mf]
- COMFORT-I: Ruxolitinib vs. placebo; spleen volume reduction ≥35% at 24 weeks: 41.9% vs. 0.7%; symptom improvement; OS benefit at 3 years; FDA approved 2011
- COMFORT-II: Ruxolitinib vs. best available therapy; spleen volume reduction ≥35%: 28% vs. 0%; maintained at 48 weeks
- Toxicity: Anemia (on-target EPO suppression) → transfusion support; thrombocytopenia; infection; JAK inhibitor withdrawal syndrome (cytokine rebound) — must taper slowly

**Polycythemia vera (RESPONSE trial):**
- Ruxolitinib vs. best available therapy in hydroxyurea-resistant/intolerant PV; primary endpoint (HCT control + spleen volume reduction): 21% vs. 1%; complete hematological remission; FDA approved for PV 2014

**Transition from ruxolitinib failure:**
- Fedratinib: ORR in ruxolitinib-refractory MF ~35% (JAKARTA-2); approved 2nd-line
- Navitoclax + ruxolitinib (TRANSFORM-1 trial): Phase III; navitoclax (BCL-2/BCL-XL inhibitor) + ruxolitinib vs. ruxolitinib; spleen volume reduction primary endpoint; ongoing (aims to overcome BCL-XL-mediated resistance)
- AlloSCT: Only curative approach for MF; DIPSS-plus risk stratification (high-risk → alloSCT eligible); reduced-intensity conditioning; 5-year OS ~50% for allografted MF

### Resistance mechanisms

**Ruxolitinib resistance in MF:**
- JAK2 V617F re-activation via heterodimer JAK2/JAK1 or JAK2/TYK2 (kinase domain mutations uncommon unlike EGFR/ALK)
- LNK (SH2B3) mutations → dampened negative regulation of JAK2
- PI3K-AKT bypass activation
- Clonal evolution: New mutations in ASXL1, EZH2, IDH1/2, TP53 → disease acceleration/transformation; not inhibited by ruxolitinib

## Connections

- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — JAK2 → STAT5 (primary) and STAT3 → BCL-XL, MYC, cyclin D1 → proliferation; V617F → constitutive STAT5 phosphorylation → EPO-independent erythropoiesis in PV; STAT5 is the primary effector of JAK2-driven erythropoiesis and thrombocytopoiesis.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — EPO → EPOR → JAK2 trans-autophosphorylation at Tyr1007/1008 → STAT5 → erythroid differentiation; JAK2 V617F mimics EPO-occupied receptor → constitutive erythroid proliferation without EPO in PV; serum EPO is suppressed in PV and elevated in secondary polycythemia.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — IL-6 → IL-6R/gp130 → JAK1/JAK2 → STAT3 phosphorylation → acute phase response and inflammatory cytokines; MF is characterized by elevated IL-6, IL-8, TNF-α (JAK2-driven cytokine storm); ruxolitinib reduces circulating inflammatory cytokines in MF.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — JAK2 → PI3K → AKT → mTOR signaling in MPN; JAK2 V617F activates mTORC1 independent of insulin signaling; mTOR inhibitors (everolimus) showed modest single-agent activity in MF; combined JAK+mTOR inhibition studied in high-risk MPN.

[^baxter-2005-jak2-v617f]: Baxter EJ, Scott LM, Campbell PJ, et al. Acquired mutation of the tyrosine kinase JAK2 in human myeloproliferative disorders. *Lancet.* 2005;365(9464):1054-1061. [doi:10.1016/S0140-6736(05)71142-9](https://doi.org/10.1016/S0140-6736(05)71142-9) · [PubMed 15781101](https://pubmed.ncbi.nlm.nih.gov/15781101/)
[^verstovsek-2012-ruxolitinib-mf]: Verstovsek S, Mesa RA, Gotlib J, et al. A double-blind, placebo-controlled trial of ruxolitinib for myelofibrosis. *N Engl J Med.* 2012;366(9):799-807. [doi:10.1056/NEJMoa1110557](https://doi.org/10.1056/NEJMoa1110557) · [PubMed 22375971](https://pubmed.ncbi.nlm.nih.gov/22375971/)

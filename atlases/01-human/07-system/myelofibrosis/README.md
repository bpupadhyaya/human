---
schema: human-scale-entry/v1
id: myelofibrosis
name: Myelofibrosis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Myelofibrosis is a MPN with BM fibrosis, megakaryocyte dysplasia, and splenomegaly; drivers JAK2 V617F ~60%, CALR exon 9 ~20-25%, MPL ~8%; ruxolitinib (COMFORT-I/II), fedratinib, pacritinib, momelotinib (MOMENTUM) approved; allo-SCT is the only curative option."
aliases: ["myelofibrosis", "MF", "PMF", "primary myelofibrosis", "post-ET MF", "post-PV MF", "myeloproliferative neoplasm fibrosis", "JAK inhibitor myelofibrosis"]
sources:
  - id: verstovsek-2012-comfort1
    type: peer-reviewed
    cite: "Verstovsek S, Mesa RA, Gotlib J, et al. A double-blind, placebo-controlled trial of ruxolitinib for myelofibrosis. N Engl J Med. 2012;366(9):799-807."
    doi: "10.1056/NEJMoa1110557"
    pmid: "22375971"
    url: "https://doi.org/10.1056/NEJMoa1110557"
  - id: harrison-2012-comfort2
    type: peer-reviewed
    cite: "Harrison C, Kiladjian JJ, Al-Ali HK, et al. JAK inhibition with ruxolitinib versus best available therapy for myelofibrosis. N Engl J Med. 2012;366(9):787-798."
    doi: "10.1056/NEJMoa1110556"
    pmid: "22375970"
    url: "https://doi.org/10.1056/NEJMoa1110556"
cross_links:
  - target: 01-human/03-molecular/calr
    relation: connects-to
    note: "CALR exon 9 frameshift mutations drive ~20-25% of PMF; type 1 del52 → PMF phenotype with higher fibrosis grade and AML transformation risk; type 2 ins5 → ET phenotype; CALR-mutant MF responds to ruxolitinib with similar spleen/symptom benefit as JAK2 V617F MF."
  - target: 01-human/03-molecular/jak2
    relation: connects-to
    note: "JAK2 V617F occurs in ~60% of PMF and drives constitutive JAK-STAT signaling; JAK2 V617F allele burden correlates with splenomegaly and constitutional symptoms; ruxolitinib and other JAK inhibitors all target JAK2 kinase activity; JAK2 V617F is the primary molecular target in MF."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Ruxolitinib is first-line standard of care for intermediate-2 and high-risk MF; momelotinib inhibits JAK1/JAK2 plus ACVR1 → reduces hepcidin → anemia benefit; JAK1 inhibition reduces inflammatory cytokine burden (IL-6, TNF-α) driving constitutional symptoms."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β1 secreted by CALR/JAK2-mutant megakaryocytes is the primary driver of BM fibrosis in MF; TGF-β activates fibroblasts → collagen/reticulin deposition; serum TGF-β1 correlates with MF grade; TGF-β pathway inhibition is a therapeutic target in preclinical MF models."
  - target: 01-human/03-molecular/thrombopoietin
    relation: connects-to
    note: "MPL W515L/K activates JAK2 constitutively independent of TPO → megakaryocyte dysplasia and marrow fibrosis; ruxolitinib suppresses JAK-STAT; thrombocytopenia in high-risk MF limits JAK inhibitor dosing; pacritinib/momelotinib approved for MF with thrombocytopenia."
---

# Myelofibrosis

## Overview

**Myelofibrosis (MF)** is a BCR-ABL1-negative myeloproliferative neoplasm (MPN) characterized by clonal hematopoiesis, progressive bone marrow fibrosis, extramedullary hematopoiesis (splenomegaly, hepatomegaly), and constitutional symptoms (fatigue, night sweats, weight loss, pruritus). MF arises as **primary myelofibrosis (PMF)** de novo or as **post-ET MF** and **post-PV MF** from prior essential thrombocythemia or polycythemia vera. Incidence: ~1-2/100,000/year; median age at diagnosis ~65 years; male slight predominance. MF carries the worst prognosis among the classic MPNs — median OS ~5-7 years for intermediate/high-risk disease — and is uniquely characterized by profound constitutional symptom burden often exceeding that of solid organ malignancies. **JAK2 V617F** (~60%), **CALR exon 9 mutations** (~20-25%), and **MPL W515L/K** (~8%) are the three canonical driver mutations, all converging on constitutive JAK-STAT pathway activation [^verstovsek-2012-comfort1][^harrison-2012-comfort2]. JAK inhibitors (ruxolitinib, fedratinib, pacritinib, momelotinib) have transformed symptom management; **allogeneic SCT** remains the only potentially curative therapy.

**MF subtypes:**
- **Primary MF (PMF):** De novo; no antecedent MPN; median OS ~5-7 years (high-risk)
- **Post-ET MF:** ~0.5-1%/year transformation rate from ET; overall ~10-15% at 15 years; better prognosis than PMF
- **Post-PV MF:** ~0.5-0.8%/year transformation rate from PV; OS slightly worse than post-ET MF

## Structure

### Driver mutations and molecular architecture

**JAK2 V617F (~60% PMF, ~55% post-PV MF, ~50% post-ET MF):**
Acquired point mutation (V617F) in the pseudokinase domain of JAK2 → releases autoinhibition → constitutive kinase activity → downstream STAT3/STAT5, PI3K-AKT, MAPK activation; higher allele burden (>50% VAF) in PV and MF vs. ET; homozygosity through mitotic recombination correlates with fibrosis progression.

**CALR exon 9 mutations (~20-25% PMF, ~25% ET→MF):**
Type 1 (del52bp) predominates in PMF (3:1 over type 2 ins5bp); type 1 confers stronger MPL activation and HSC self-renewal → PMF phenotype; both respond to JAK inhibitors; allele burden trackable by ddPCR/NGS. See [CALR](../../03-molecular/calr/README.md) for detailed mechanism.

**MPL W515L/K (~8% PMF):**
Activating mutations in the juxtamembrane domain of the thrombopoietin receptor MPL → constitutive JAK2 activation independent of TPO; clinically similar to JAK2-mutant MF; responds to ruxolitinib.

**Triple-negative MF (~8-10%):**
Absence of JAK2, CALR, and MPL mutations; higher rate of IDH1/2, ASXL1 adverse mutations; worst prognosis among driver mutation groups; allo-SCT strongly indicated.

### High-risk co-mutations (MIPSS70 adverse molecular markers)

| Gene | Frequency | Effect |
|------|-----------|--------|
| ASXL1 | ~35-40% | Epigenetic dysregulation; adverse prognosis |
| SRSF2 | ~15-20% | Aberrant splicing; monocytic skewing; adverse |
| EZH2 | ~7-10% | PRC2 loss; adverse |
| IDH1/2 | ~5% | 2-HG production; AML transformation risk |
| U2AF1 Q157 | ~8-10% | Splicing; Q157 is specifically adverse (vs S34) |
| TP53 | ~5% | Bi-allelic → very adverse; blastic transformation |

**MIPSS70 (Mutation-Enhanced IPSS at age 70):** Incorporates driver mutation type, adverse co-mutations, and karyotype; stratifies PMF into 5 risk tiers; guides allo-SCT timing.

### Bone marrow pathology

**WHO 2022 criteria for PMF:**
Major: (1) megakaryocytic proliferation + atypia (cloud-like nuclei, bulbous nuclear lobes, bare megakaryocyte nuclei in sinusoids) WITH reticulin and/or collagen fibrosis grade 1-3; (2) WHO criteria not met for another MPN, MDS, or BCR-ABL1+ CML; (3) JAK2/CALR/MPL mutation or other clonal marker.
Minor: (1) anemia; (2) leukocytosis ≥11×10⁹/L; (3) palpable splenomegaly; (4) elevated LDH; (5) leukoerythroblastosis (teardrop cells/dacrocytes + nucleated RBCs + immature myeloid cells).

**Fibrosis grading (European consensus):**
- MF-0 (prefibrotic): Scattered linear reticulin, no coarse fibers (→ pre-PMF, often misdiagnosed as ET)
- MF-1: Loose network of reticulin with some intersections
- MF-2: Diffuse dense reticulin + coarse collagen bundles
- MF-3: Dense reticulin + collagen + osteosclerosis

**Prefibrotic PMF (pre-PMF):** Megakaryocyte atypia without significant fibrosis (MF-0/1); mimics ET; prognosis intermediate between ET and overt MF; important to distinguish clinically because transformation risk is higher than true ET.

### Peripheral blood and clinical findings

- **Leukoerythroblastosis:** Teardrop cells (dacrocytes), nucleated RBCs (nRBC), immature myeloid cells (myelocytes, metamyelocytes) → hallmark of extramedullary hematopoiesis
- **Anemia:** Multifactorial — ineffective erythropoiesis, splenomegaly (hypersplenism), hepcidin upregulation (JAK-IL-6 axis) → transfusion dependence in ~40-50% high-risk MF
- **Splenomegaly:** Near-universal; massive (>5 cm below costal margin) in ~50% symptomatic; splenic sequestration + EMH; portal hypertension in severe cases
- **Cytokine storm:** Elevated IL-6, TNF-α, IL-8, CXCL10 → constitutional symptoms; inflammatory cytokines are the primary drivers of MF symptom burden (NOT blast proliferation)

## Function

### Normal megakaryocyte and BM stromal biology

**Megakaryocyte-stromal crosstalk in MF:**
Normal megakaryocytes (MK) secrete TGF-β1 at controlled amounts → fibroblast activation in proportion to MK mass. In MF, CALR/JAK2-mutant MKs are hyperproliferative and release excess TGF-β1, PDGF, VEGF, and FGF from α-granules → fibroblast proliferation + collagen deposition → reticulin → collagen fibrosis → osteosclerosis. This is a paracrine (not cell-intrinsic) mechanism of fibrosis — the fibroblasts in MF are polyclonal (not part of the MPN clone); they respond to cytokine signals from malignant MKs.

**Extramedullary hematopoiesis:**
As BM fibrosis displaces hematopoietic stem/progenitor cells (HSPCs) → HSPCs mobilize to spleen, liver, lungs → massive splenomegaly; spleen becomes major site of blood production (erythropoiesis, myelopoiesis); spleen-derived hematopoiesis is dysplastic → peripheral blood leukoerythroblastosis.

## Pathology

### Prognostic scoring systems

**IPSS (International Prognostic Scoring System — diagnosis only):**
Points for: age >65, WBC >25×10⁹/L, Hgb <10 g/dL, blasts ≥1%, constitutional symptoms
Risk groups: Low (0), Int-1 (1), Int-2 (2), High (≥3); median OS: 135, 95, 48, 27 months

**DIPSS (Dynamic IPSS — any time point):**
Same variables with double weight for Hgb <10 g/dL; updated real-time assessment during follow-up.

**MIPSS70 (Molecular IPSS):**
Adds adverse co-mutations (ASXL1, SRSF2, EZH2, IDH1/2, U2AF1 Q157) + karyotype + BM fibrosis grade; 5 risk groups; guides allo-SCT decision in patients ≤70 years.

### Blast phase transformation (BP-MF / AML)

- AML transformation in MF: ~10-20% overall; ~3-5%/year in high-risk MIPSS; median OS post-transformation ~3.5 months with chemotherapy alone
- Molecular harbingers: IDH1/2 mutation acquisition, TP53 biallelic, RUNX1 mutation, NRAS mutation
- Treatment: venetoclax + azacitidine (preferred in fit patients); HMA alone; intensive chemotherapy rarely used; allo-SCT if CR/CRi achieved

### Treatment

**JAK inhibitors (first-line intermediate-2 / high-risk MF):**

| Drug | Mechanism | Key Trial | Key Result |
|------|-----------|-----------|------------|
| Ruxolitinib | JAK1/2 inhibitor | COMFORT-I (placebo) / COMFORT-II (BAT) | SVR35 ~42% vs 0-1%; symptom score ≥50% reduction ~46% vs 5%; OS benefit at 5-year follow-up |
| Fedratinib | JAK2-selective | JAKARTA | SVR35 ~47%; active after ruxolitinib failure (JAKARTA-2) |
| Pacritinib | JAK2/FLT3/ACVR1 | PERSIST-2 / PAC203 | Platelet-sparing; SVR35 ~29% in platelets <50×10⁹/L; FDA 2022 for cytopenic MF |
| Momelotinib | JAK1/2/ACVR1 | MOMENTUM | SVR35 ~23% vs 3%; TSS50 ~24% vs 9%; transfusion independence ~31% vs 20%; FDA 2023 for symptomatic + anemic MF |

**Ruxolitinib mechanism of anemia (adverse effect):**
JAK1/2 inhibition → reduced EPO signaling → anemia; also reduced ACVR1/hepcidin inhibition; momelotinib adds ACVR1 inhibition → reduced hepcidin → improved erythropoiesis → anemia benefit.

**Ruxolitinib discontinuation syndrome:**
Abrupt ruxolitinib cessation → cytokine rebound → fever, splenomegaly surge, hypotension, hemodynamic instability; always taper over 1-2 weeks; have steroids ready.

**Anemia-targeted agents:**
- **Luspatercept** (ACVR2B-Fc trap; traps TGF-β superfamily ligands → activin pathway inhibition → promotes late-stage erythropoiesis): EMPOWER-MF trial; transfusion independence in ~27% of MF patients with anemia; FDA pending
- **Danazol** (androgen): modest anemia benefit; hepatotoxicity
- **Thalidomide/lenalidomide** (immunomodulatory): anemia and splenomegaly; limited use due to toxicity

**Combination investigational strategies:**
- **Ruxolitinib + navitoclax (BCL-2/BCL-XL):** REFINE trial; SVR35 ~63% vs ~38% ruxolitinib; navitoclax causes thrombocytopenia (BCL-XL platelets)
- **Ruxolitinib + pelabresib (BET inhibitor, CPI-0610):** MANIFEST-2 (randomized Ph3): SVR35 primary endpoint met; bone marrow fibrosis improvement; spleen + symptom co-primary endpoints pending full publication
- **Imetelstat (telomerase inhibitor):** IMpact-MF (randomized Ph3, ruxolitinib-relapsed MF): anemia reduction; awaiting OS data

**Allogeneic SCT (only curative therapy):**
- Indicated for intermediate-2 / high-risk MF (MIPSS70) in eligible patients (typically age ≤70)
- 5-year OS post-allo-SCT: ~50-60% (myeloablative conditioning) vs ~35-45% (reduced intensity)
- BM fibrosis resolves post-engraftment over 3-6 months
- Timing: before blast phase transformation; higher-risk co-mutations (IDH, TP53) → earlier SCT
- Relapse post-SCT: ~20-30%; DLI and molecular monitoring (JAK2/CALR VAF)

## Connections

- `connects-to` → **[CALR](../../03-molecular/calr/README.md)** — CALR exon 9 frameshift mutations drive ~20-25% of PMF; type 1 del52 → PMF phenotype with higher fibrosis grade and AML transformation risk; type 2 ins5 → ET phenotype; CALR-mutant MF responds to ruxolitinib with similar spleen/symptom benefit as JAK2 V617F MF.
- `connects-to` → **[JAK2](../../03-molecular/jak2/README.md)** — JAK2 V617F occurs in ~60% of PMF and drives constitutive JAK-STAT signaling; JAK2 V617F allele burden correlates with splenomegaly and constitutional symptoms; ruxolitinib and other JAK inhibitors all target JAK2 kinase activity; JAK2 V617F is the primary molecular target in MF.
- `connects-to` → **[JAK1-2](../../03-molecular/jak1-2/README.md)** — Ruxolitinib is first-line standard of care for intermediate-2 and high-risk MF; momelotinib inhibits JAK1/JAK2 plus ACVR1 → reduces hepcidin → anemia benefit; JAK1 inhibition reduces inflammatory cytokine burden (IL-6, TNF-α) driving constitutional symptoms.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — TGF-β1 secreted by CALR/JAK2-mutant megakaryocytes is the primary driver of BM fibrosis in MF; TGF-β activates fibroblasts → collagen/reticulin deposition; serum TGF-β1 correlates with MF grade; TGF-β pathway inhibition is a therapeutic target in preclinical MF models.
- `connects-to` → **[Thrombopoietin](../../03-molecular/thrombopoietin/README.md)** — MPL W515L/K activates JAK2 constitutively independent of TPO → megakaryocyte dysplasia and marrow fibrosis; ruxolitinib suppresses JAK-STAT; thrombocytopenia in high-risk MF limits JAK inhibitor dosing; pacritinib/momelotinib approved for MF with thrombocytopenia.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^verstovsek-2012-comfort1]: Verstovsek S, Mesa RA, Gotlib J, et al. A double-blind, placebo-controlled trial of ruxolitinib for myelofibrosis. *N Engl J Med.* 2012;366(9):799-807. [doi:10.1056/NEJMoa1110557](https://doi.org/10.1056/NEJMoa1110557) · [PubMed 22375971](https://pubmed.ncbi.nlm.nih.gov/22375971/)
[^harrison-2012-comfort2]: Harrison C, Kiladjian JJ, Al-Ali HK, et al. JAK inhibition with ruxolitinib versus best available therapy for myelofibrosis. *N Engl J Med.* 2012;366(9):787-798. [doi:10.1056/NEJMoa1110556](https://doi.org/10.1056/NEJMoa1110556) · [PubMed 22375970](https://pubmed.ncbi.nlm.nih.gov/22375970/)

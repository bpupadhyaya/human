---
schema: human-scale-entry/v1
id: il-5
name: Interleukin-5
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "IL-5 (IL5, chr5q31.1) is a Th2 homodimer cytokine selectively driving eosinophil differentiation, survival, and recruitment via IL-5Rα/βc → JAK1/JAK2 → STAT5; mepolizumab and benralizumab (anti-IL-5/IL-5Rα) reduce eosinophilic asthma exacerbations 47-50%."
aliases: ["IL-5", "interleukin-5", "IL5", "eosinophil colony-stimulating factor", "EDF", "BCGF-II", "B cell growth factor II"]
cross_links:
  - target: 01-human/07-system/asthma
    relation: connects-to
    note: "IL-5 drives eosinophilic airway inflammation; blood eosinophils ≥300/μL identifies biologic candidates; mepolizumab (MENSA 47% RRR) and benralizumab (CALIMA 28-36% RRR) block IL-5 or IL-5Rα to reduce exacerbations in severe eosinophilic asthma."
  - target: 01-human/07-system/atopic-dermatitis
    relation: connects-to
    note: "IL-5 sustains tissue eosinophilia in atopic dermatitis lesions; Th2 and ILC2 produce IL-5 → bone marrow eosinophil production → CCR3-mediated skin recruitment; eosinophil MBP and ECP amplify IL-31 sensitization and intractable itch in moderate-severe AD."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "IL-5 and IgE co-amplify type 2 disease: Th2 cells co-produce IL-4 (IgE class switch) and IL-5 (eosinophilia); eosinophil MBP potentiates mast cell FcεRI → amplified degranulation; blood eosinophils ≥300 and elevated IgE both predict biologic response in asthma."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "IL-5 and IL-4 are co-expressed from the Th2 cytokine gene cluster (chr5q31.1); IL-4 drives Th2 polarization and IgE production while IL-5 drives eosinophil proliferation and survival; both are induced by GATA-3 but IL-5 signals via STAT5, IL-4 via STAT6."
sources:
  - id: ortega-2014-mensa
    type: peer-reviewed
    cite: "Ortega HG, Liu MC, Pavord ID, et al. Mepolizumab treatment in patients with severe eosinophilic asthma. N Engl J Med. 2014;371(13):1198-1207."
    doi: "10.1056/NEJMoa1403290"
    pmid: "25199059"
    url: "https://doi.org/10.1056/NEJMoa1403290"
  - id: fitzgerald-2016-calima
    type: peer-reviewed
    cite: "FitzGerald JM, Bleecker ER, Nair P, et al. Benralizumab, an anti-interleukin-5 receptor α monoclonal antibody, as add-on treatment for patients with severe, uncontrolled, eosinophilic asthma (CALIMA): a randomised, double-blind, placebo-controlled phase 3 trial. Lancet. 2016;388(10056):2115-2127."
    doi: "10.1016/S0140-6736(16)31322-8"
    pmid: "27609408"
    url: "https://doi.org/10.1016/S0140-6736(16)31322-8"
---

# Interleukin-5

## Overview

**Interleukin-5 (IL-5)** (gene *IL5*, chromosome 5q31.1) is a **15 kDa homodimeric Th2 cytokine** and the primary regulator of **eosinophil biology** — governing eosinophil proliferation and differentiation from bone marrow progenitors, peripheral survival, activation, and tissue recruitment. Encoded within the **Th2 cytokine gene cluster** alongside IL-4, IL-13, IL-3, and GM-CSF on chromosome 5q31.1, IL-5 is distinguished from its neighbors by its **exquisite lineage specificity for eosinophils** — the IL-5 receptor α chain (IL-5Rα; CD125) is expressed at high density on eosinophils and basophils, with negligible expression on other hematopoietic cells.

IL-5 was first identified in the 1980s as "eosinophil differentiation factor" (EDF) and "B cell growth factor II" (BCGF-II) — reflecting the then-unresolved discovery that the same molecule promoted eosinophil development AND B cell proliferation in rodents. In humans, the eosinophil-selective biology dominates clinically: IL-5 is the master cytokine of **eosinophilic airway disease**, with blood eosinophil counts (≥300/μL threshold) serving as the primary biomarker for biologic response prediction in asthma.

**Three major IL-5-driven disease contexts:**
1. **Severe eosinophilic asthma** — blood eosinophils ≥300/μL; mepolizumab (anti-IL-5) and benralizumab (anti-IL-5Rα) reduce exacerbations 47–50%; most effective biologic for late-onset, non-allergic eosinophilic phenotype
2. **Eosinophilic granulomatosis with polyangiitis (EGPA)** — rare ANCA-associated vasculitis with asthma, nasal polyps, and tissue eosinophilia; mepolizumab approved (MIRRA trial: 28-week remission RR 5.91 vs. placebo)
3. **Hypereosinophilic syndrome (HES)** — idiopathic eosinophilia ≥1,500/μL ≥6 months with organ damage; mepolizumab FDA-approved 2020 for non-FIP1L1-PDGFRA HES

## Structure

**Protein architecture:**
IL-5 is a **parallel homodimer** — two identical 134-aa polypeptide chains (after 22-aa signal peptide cleavage) cross-linked by a single intermolecular disulfide bond between **Cys44 of one chain and Cys86 of the partner chain** (the "crossed" dimer configuration). This crisscross arrangement is unique among cytokines and is required for receptor binding; the IL-5 monomer has negligible biological activity.

**4-helix bundle topology:**
Each monomer adopts a compact 4-helix bundle (helices A-D) typical of the hematopoietin cytokine superfamily, but arranged in an **antiparallel head-to-tail orientation** in the dimer — placing helix A of one chain adjacent to helix D of the other. The composite dimer surface presents two symmetrical receptor binding sites, though only **one IL-5Rα chain binds per dimer** (monovalent receptor engagement), with the βc chain bridging asymmetrically.

**IL-5 receptor complex (IL-5R):**
- **IL-5Rα chain (CD125; IL5RA gene, chr3p26.2):** High-affinity IL-5-specific binding subunit (Kd ~1 nM for IL-5 alone); type I cytokine receptor ectodomain with cytokine-binding homology module (CHM); expressed densely on eosinophils (>100,000 copies/cell), basophils, and mast cells; NOT expressed on neutrophils, T cells, or B cells in humans
- **βc chain (CD131; CSF2RB gene, chr22q12.3):** Shared signaling subunit for IL-5, IL-3, and GM-CSF; low-affinity IL-5 binding alone (Kd ~1 μM); assembly with IL-5Rα creates high-affinity complex (Kd ~10–30 pM) and activates JAK kinases
- **Assembly sequence:** IL-5 binds IL-5Rα first (site I) → IL-5Rα/IL-5 complex recruits βc → hexameric signaling complex [(IL-5Rα/βc)₂·IL-5₂] may form at higher receptor densities

**Signaling cascade:**
1. IL-5Rα associated with **JAK2**; βc associated with **JAK1** (some sources report Tyk2) — receptor assembly → JAK transphosphorylation
2. JAK1/JAK2 → **STAT5a/b phosphorylation** (primary transcription factor axis): STAT5 → eosinophil anti-apoptotic genes (*BCL2*, *BCL-xL*, *MCL1*), proliferation genes
3. **PI3K/Akt branch:** pTyr recruitment of PI3K p85 regulatory subunit → Akt → mTORC1 → protein synthesis → eosinophil activation and degranulation priming
4. **MAPK/ERK branch:** SOS/Grb2 → Ras → Raf → MEK → ERK → eosinophil survival and cytokine production (CCL5/RANTES, LTC4)
5. **STAT1 (secondary):** IFN-γ-like transcriptional programs in eosinophils during helminth infection

**Benralizumab mechanism (anti-IL-5Rα, afucosylated IgG1):**
Benralizumab binds IL-5Rα on eosinophil surfaces → blocks IL-5 signaling AND recruits NK cells/macrophages via FcγRIIIa (high-affinity due to afucosylation) → **ADCC (antibody-dependent cellular cytotoxicity)** → eosinophil depletion within 24 hours; this ADCC mechanism is faster and more complete than mepolizumab's ligand neutralization.

## Function

**Bone marrow eosinophiesis:**
- IL-5 acts at the **IL-5Rα-expressing eosinophil progenitor** stage (EoP, CD34⁺IL-5Rα⁺) → drives eosinophil colony formation; IL-3 and GM-CSF (sharing βc) provide earlier progenitor support
- IL-5 → STAT5 → GATA-1 and C/EBPα maintenance → eosinophil-specific granule protein gene transcription (MBP1/*PRG2*, ECP/*RNASE3*, EDN/*RNASE2*, EPX/*RNASE7*)
- IL-5-driven eosinophiesis takes 3–4 days from progenitor to mature circulating eosinophil; mepolizumab reduces blood eosinophils by ~75% within 1 week as marrow output drops

**Eosinophil survival and anti-apoptotic effects:**
- Without survival signals, circulating eosinophils undergo spontaneous apoptosis within 8–18 hours
- IL-5 binding → STAT5 → BCL-2 and BCL-xL upregulation → prevents mitochondrial apoptosis; in tissue, IL-5 cooperates with eotaxin-1/CCL11 (CCR3 signaling) and GM-CSF to extend eosinophil half-life to 1–14 days in inflamed tissue
- This prolonged tissue survival underlies chronic eosinophil infiltration in asthmatic bronchi and skin lesions

**Eosinophil recruitment:**
- IL-5 → upregulates **CCR3** on eosinophils → increased responsiveness to eotaxins (CCL11, CCL24, CCL26) produced by airway epithelium and fibroblasts
- IL-5 primes eosinophils for **CD18/CD11b** (Mac-1) upregulation → increased adhesion to VCAM-1 on endothelium → diapedesis into tissue
- IL-5 + eotaxin-1 synergize in a "two-signal" model: IL-5 provides survival + CCR3 upregulation; eotaxin-1 provides directional chemotaxis

**Eosinophil effector functions (IL-5-driven):**
- **Degranulation:** Eosinophil granules contain major basic protein (MBP, crystalloid core), eosinophil cationic protein (ECP), eosinophil-derived neurotoxin (EDN), and eosinophil peroxidase (EPX) → damage epithelium; MBP directly blocks muscarinic M2 receptors → enhanced vagal bronchoconstriction
- **Lipid mediators:** IL-5-primed eosinophils produce LTC4 (potent bronchoconstrictor), PGE2, PAF (platelet-activating factor) → inflammatory amplification
- **Cytokine secretion:** IL-5-activated eosinophils secrete TGF-β (airway remodeling), IL-13 (goblet cell hyperplasia), VEGF (angiogenesis), and NGF (neurotrophin)

## Mechanism

**Mepolizumab (Nucala) — anti-IL-5 IgG1κ [^ortega-2014-mensa]:**
- **MENSA trial (2014):** 576 patients with severe eosinophilic asthma (≥2 exacerbations/year + blood Eos ≥150/μL at screening or ≥300/μL at any prior 12-month period); mepolizumab 75 mg IV Q4W vs. 100 mg SC Q4W vs. placebo
- 100 mg SC: **47% reduction in clinically significant exacerbation rate** (RR 0.53, 95% CI 0.37–0.75); 75 mg IV: 52% reduction
- Blood eosinophil reduction: ~75% at week 4; maintained through 32 weeks
- Subsequent approvals: EGPA (MIRRA trial 2017), HES (2020), CRSwNP with nasal polyps (2021)
- Dosing: 100 mg SC Q4W (asthma, HES); 300 mg SC Q4W (EGPA)

**Benralizumab (Fasenra) — anti-IL-5Rα afucosylated IgG1 [^fitzgerald-2016-calima]:**
- **CALIMA trial (2016):** 1,306 patients with severe eosinophilic asthma + blood Eos ≥300/μL; benralizumab 30 mg SC Q4W × 3 then Q8W vs. Q4W throughout vs. placebo
- Q4W/Q8W regimen: **28% reduction in exacerbation rate** (RR 0.72); pre-specified population (blood Eos ≥300): **36% reduction** (RR 0.64)
- SIROCCO trial (complementary): 28-51% exacerbation reduction at different eosinophil thresholds
- Near-complete eosinophil depletion (<10/μL) within 24 hours (vs. 75% reduction with mepolizumab) — due to ADCC mechanism
- Dosing: 30 mg SC Q4W × 3 doses (loading), then Q8W (maintenance)

**Biologic selection in severe eosinophilic asthma:**
| Feature | Mepolizumab | Benralizumab | Reslizumab |
|---|---|---|---|
| Target | IL-5 (ligand) | IL-5Rα (receptor) | IL-5 (ligand) |
| Dosing route | SC Q4W | SC Q4W×3, then Q8W | IV Q4W (weight-based) |
| Eosinophil depletion | ~75% | Near-complete (ADCC) | ~75% |
| Blood Eos threshold | ≥150–300/μL | ≥150–300/μL | ≥400/μL |
| EGPA/HES approval | Yes | No | No |

**IL-5 in eosinophilic esophagitis (EoE):**
- Esophageal epithelium in EoE produces **eotaxin-3 (CCL26)** in response to food allergens → CCR3 on IL-5-primed eosinophils → >15 eos/hpf in esophageal biopsy (diagnostic criterion)
- IL-5 blockade with mepolizumab modestly reduces esophageal eosinophil counts but has not met regulatory endpoints for EoE — suggesting eotaxin-3 and local factors independent of systemic IL-5 drive EoE pathology

## Connections

IL-5 drives eosinophilic airway inflammation; blood eosinophils ≥300/μL identifies biologic candidates; mepolizumab (MENSA 47% RRR) and benralizumab (CALIMA 28-36% RRR) block IL-5 or IL-5Rα to reduce exacerbations in severe eosinophilic asthma.

IL-5 sustains tissue eosinophilia in atopic dermatitis lesions; Th2 and ILC2 produce IL-5 → bone marrow eosinophil production → CCR3-mediated skin recruitment; eosinophil MBP and ECP amplify IL-31 sensitization and intractable itch in moderate-severe AD.

IL-5 and IgE co-amplify type 2 disease: Th2 cells co-produce IL-4 (IgE class switch) and IL-5 (eosinophilia); eosinophil MBP potentiates mast cell FcεRI → amplified degranulation; blood eosinophils ≥300 and elevated IgE both predict biologic response in asthma.

IL-5 and IL-4 are co-expressed from the Th2 cytokine gene cluster (chr5q31.1); IL-4 drives Th2 polarization and IgE production while IL-5 drives eosinophil proliferation and survival; both are induced by GATA-3 but IL-5 signals via STAT5, IL-4 via STAT6.

[^ortega-2014-mensa]: Ortega HG, Liu MC, Pavord ID, et al. Mepolizumab treatment in patients with severe eosinophilic asthma. *N Engl J Med.* 2014;371(13):1198-1207. [doi:10.1056/NEJMoa1403290](https://doi.org/10.1056/NEJMoa1403290) · [PubMed 25199059](https://pubmed.ncbi.nlm.nih.gov/25199059/)
[^fitzgerald-2016-calima]: FitzGerald JM, Bleecker ER, Nair P, et al. Benralizumab, an anti-interleukin-5 receptor α monoclonal antibody, as add-on treatment for patients with severe, uncontrolled, eosinophilic asthma (CALIMA): a randomised, double-blind, placebo-controlled phase 3 trial. *Lancet.* 2016;388(10056):2115-2127. [doi:10.1016/S0140-6736(16)31322-8](https://doi.org/10.1016/S0140-6736(16)31322-8) · [PubMed 27609408](https://pubmed.ncbi.nlm.nih.gov/27609408/)

---
schema: human-scale-entry/v1
id: epas1
name: EPAS1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "EPAS1 encodes HIF-2α (bHLH-PAS TF) stabilized under hypoxia or VHL loss; PHD2 hydroxylation → VHL-mediated degradation; activates EPO/VEGF; belzutifan (HIF-2α inhibitor) FDA-approved for VHL disease-associated RCC; EPAS1 GOF mutations cause hereditary erythrocytosis."
aliases: ["EPAS1", "HIF-2alpha", "HIF-2α", "HIF2A", "hypoxia-inducible factor 2", "belzutifan target", "VHL-HIF axis", "EPAS1 erythrocytosis"]
sources:
  - id: jonasch-2021-belzutifan
    type: peer-reviewed
    cite: "Jonasch E, Donskov F, Iliopoulos O, et al. Belzutifan for renal cell carcinoma in von Hippel-Lindau disease. N Engl J Med. 2021;385(22):2036-2046."
    doi: "10.1056/NEJMoa2103979"
    pmid: "34818478"
    url: "https://doi.org/10.1056/NEJMoa2103979"
  - id: choueiri-2023-litespark005
    type: peer-reviewed
    cite: "Choueiri TK, Powles T, Albiges L, et al. Belzutifan versus everolimus for advanced renal-cell carcinoma. N Engl J Med. 2023;388(10):869-881."
    doi: "10.1056/NEJMoa2212875"
    pmid: "36827464"
    url: "https://doi.org/10.1056/NEJMoa2212875"
cross_links:
  - target: 01-human/03-molecular/vhl
    relation: connects-to
    note: "VHL E3 ubiquitin ligase targets PHD2-hydroxylated HIF-2α for proteasomal degradation; VHL loss → HIF-2α stabilization → EPO/VEGF activation; belzutifan is FDA-approved for VHL disease-associated RCC, hemangioblastoma, and pNET."
  - target: 01-human/03-molecular/jak2
    relation: connects-to
    note: "HIF-2α drives EPO transcription → JAK2/STAT5 activation in erythroid progenitors; JAK2 V617F in PV constitutively activates erythropoiesis, mimicking EPO-independent signaling; ruxolitinib suppresses HIF-2α expression in myeloid cells."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTORC1 promotes HIF-2α translation via S6K/4E-BP1 phosphorylation; HIF-2α activates VEGF → PI3K-AKT-mTOR → angiogenesis; everolimus has activity in VHL-mutant RCC; dual HIF-2α+mTOR inhibition explored in ccRCC."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "HIF-2α is the principal transcriptional activator of VEGF in VHL-mutant RCC; EPAS1 binds HRE upstream of VEGF promoter → VEGF secretion → angiogenesis; belzutifan targets HIF-2α upstream, suppressing VEGF production in RCC."
  - target: 01-human/03-molecular/egln1
    relation: connects-to
    note: "EGLN1 (PHD2) hydroxylates HIF-2α at Pro405/Pro531 → VHL-mediated degradation; Tibetan EGLN1 D4E/C127S increases HIF-2α hydroxylation → blunted EPO at altitude; PHD inhibitors stabilize HIF-2α → EPO upregulation for CKD anemia."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "HIF-2α (EPAS1) is the dominant oncogenic driver in VHL-mutant clear cell RCC (~90% have VHL LOF); activates VEGF, TGF-α, CCND1, OCT4 → tumor angiogenesis and stemness; belzutifan (PAS-B allosteric inhibitor) FDA-approved for advanced ccRCC after PD-1 + VEGFR TKI (LITESPARK-005)."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "HIF-2α is the principal EPO activator in renal peritubular cells; EPAS1 GOF mutations → HIF-2α resistant to PHD2 hydroxylation → hereditary erythrocytosis; Chuvash polycythemia (VHL R200W) stabilizes HIF-2α → EPO excess; PHD inhibitors target the HIF-2α/EPO axis for CKD anemia."
---

# EPAS1

## Overview

**EPAS1 (Endothelial PAS Domain Protein 1)** encodes **HIF-2α (Hypoxia-Inducible Factor 2α)**, a member of the bHLH-PAS transcription factor family that functions as the principal oxygen-sensitive subunit mediating hypoxic gene activation. Under normoxia, prolyl hydroxylase domain proteins (PHD1-3/EGLN1-3) use O₂ and α-ketoglutarate to hydroxylate conserved prolines (Pro405, Pro531) in HIF-2α's oxygen-dependent degradation domain (ODD) → VHL E3 ubiquitin ligase recognition → polyubiquitination → proteasomal degradation. Under hypoxia or with **VHL loss-of-function**, PHD activity is suppressed → HIF-2α stabilizes → heterodimerizes with ARNT (HIF-1β) → binds hypoxia response elements (HREs, 5'-RCGTG-3') → activates EPO, VEGF, CCND1, and SLC2A1. HIF-2α is the dominant oncogenic driver in **VHL-mutant clear cell RCC** and the therapeutic target of **belzutifan (Welireg)**, the first FDA-approved HIF-2α allosteric inhibitor [^jonasch-2021-belzutifan][^choueiri-2023-litespark005]. Germline and somatic **EPAS1 gain-of-function mutations** targeting PHD2 hydroxylation sites cause hereditary erythrocytosis and paraganglioma/pheochromocytoma.

**EPAS1 disease roles:**
- **VHL disease (germline VHL mutations):** Clear cell RCC (60-70% lifetime risk), CNS/retinal hemangioblastoma, pheochromocytoma/paraganglioma, pNET → belzutifan approved 2021 for all VHL-associated solid tumors
- **Sporadic ccRCC:** VHL biallelic inactivation ~90% → HIF-2α constitutively active; HIF-2α is the critical downstream driver (HIF-1α may be tumor-suppressive in RCC)
- **Hereditary erythrocytosis:** Germline EPAS1 GOF mutations → HIF-2α resistant to PHD2 hydroxylation → EPO excess → erythrocytosis; phenotype: low/normal serum EPO, normal JAK2, family history; must be distinguished from JAK2 V617F PV
- **Paraganglioma/pheochromocytoma:** Somatic EPAS1 mutations in ~9%; PHD2/EGLN1 and SDHA/B/C/D mutations also activate HIF-2α indirectly (loss of Krebs cycle metabolites → α-KG depletion → PHD inhibition)
- **Chuvash polycythemia:** Germline homozygous VHL R200W → impaired VHL-HIF-2α interaction → EPO excess → erythrocytosis; autosomal recessive; not associated with renal or CNS tumors

## Structure

### HIF-2α protein architecture

HIF-2α is an 870-amino-acid protein with a modular domain organization:

**N-terminal bHLH domain (1-70):**
Basic helix-loop-helix domain required for DNA binding to HRE core sequence (5'-CGTG-3'); bHLH dimerizes with ARNT bHLH for high-affinity HRE binding; mutations in bHLH domain abolish DNA binding without affecting protein stability.

**PAS-A domain (85-166) and PAS-B domain (240-350):**
Period-ARNT-Single-minded domains mediate heterodimerization with ARNT (HIF-1β); **PAS-B domain contains the belzutifan binding pocket** — a hydrophobic cavity between β-strands and α-helices of PAS-B → belzutifan occupies this pocket → steric disruption of HIF-2α PAS-B/ARNT PAS-B heterodimerization → loss of transcriptional complex assembly; HIF-2α PAS-B conformation differs from HIF-1α PAS-B (explains belzutifan selectivity for HIF-2α over HIF-1α).

**Oxygen-dependent degradation domain (ODD, 400-603):**
Contains **N-TAD** (N-terminal transactivation domain, within ODD) and flanking Pro405/Pro531 hydroxylation sites; PHD2 (EGLN1) is the primary hydroxylase for Pro531 → VHL binding → ubiquitination; Pro405 is a secondary site; both must be hydroxylated for complete VHL recognition; ODD mutations at Pro405/Pro531 → constitutive HIF-2α stability (found in hereditary erythrocytosis).

**C-terminal transactivation domain (C-TAD, 819-870):**
Recruits p300/CBP via Asn847 hydroxylation (by factor inhibiting HIF-1/FIH) → full transcriptional activation; under hypoxia, FIH is also inhibited → C-TAD hyperactive; C-TAD interactions with Mediator complex and SRC coactivators → chromatin remodeling at HRE loci.

### VHL-HIF-EPAS1 pathway

**Normoxia:**
PHD2 (EGLN1) + O₂ + α-KG → Trans-4-hydroxyproline at Pro405/Pro531 in HIF-2α ODD → VHL (substrate recognition F-box) → VHL-ELONGIN B-ELONGIN C-CUL2-RBX1 complex → K48-linked polyubiquitin on HIF-2α Lys residues → 26S proteasomal degradation; T½ < 5 minutes under normoxia.

**Hypoxia or VHL loss:**
PHD2 activity drops (O₂ limiting or succinate/fumarate accumulation from SDH/FH mutations → competitive α-KG inhibition) → HIF-2α proline remains unhydroxylated → VHL cannot bind → HIF-2α accumulates → ARNT heterodimerization → HRE-driven transcription; HIF-2α half-life extends to hours.

**VHL disease genetic classes:**
- Type 1 (truncating/deletion): High RCC + hemangioblastoma risk; low pheochromocytoma; VHL protein absent
- Type 2A (missense, e.g., Y98H): Pheochromocytoma + hemangioblastoma; low RCC risk; partial VHL function retained
- Type 2B (missense, e.g., C162F, W117R): Pheochromocytoma + hemangioblastoma + high RCC risk; severe VHL dysfunction
- Type 2C (missense, e.g., L188V): Pheochromocytoma only; VHL retains HIF-binding function, lacks JADE1 interaction

## Function

### EPO transcription and erythropoiesis

**HIF-2α is the dominant regulator of renal EPO production:**
Renal interstitial fibroblasts (peritubular cells) express HIF-2α, which directly activates the EPO gene via HRE in EPO 3' enhancer → EPO secretion → circulation → erythroid progenitor EPO receptor (EPOR) → JAK2/STAT5 → BFU-E/CFU-E survival and differentiation. Hepatocytes also produce EPO via HIF-2α (fetal primary site). HIF-1α is NOT the primary EPO transcription factor in kidney (HIF-1α activates EPO in hepatocytes but not renal interstitium).

**HIF-2α in iron-deficiency response:**
HIF-2α activates DMT1 (SLC11A2, duodenal iron transporter) and DCYTB (iron reductase) → upregulates iron absorption from diet; HIF-2α also activates hepcidin repressors (TMPRSS6 target gene EPB42 and erythroferrone ERFE) → reduced hepcidin → ferroportin stability → iron mobilization → erythropoiesis support.

### VEGF, angiogenesis, and metabolic reprogramming

**VEGF (VEGF-A):** HIF-2α binds HRE in VEGF-A promoter/enhancer → VEGF-A secretion → VEGFR2 on endothelium → tumor angiogenesis in RCC; VEGFR-TKIs (sunitinib, cabozantinib, axitinib) exploit VEGF dependency; belzutifan eliminates VEGF transcription upstream.

**Metabolic targets:** HIF-2α activates GLUT1 (SLC2A1) → glucose uptake; HIF-2α has less glycolytic gene activation than HIF-1α; HIF-2α preferentially activates fatty acid oxidation and lipid storage genes in renal tubular cells → clear cell RCC lipid-rich phenotype; HIF-2α activates OCT4 (stem cell TF) → tumor cell dedifferentiation and self-renewal.

### HIF-2α target gene repertoire

Key HIF-2α-selective targets (vs HIF-1α-shared or HIF-1α-selective):
- **EPO** (HIF-2α selective in kidney)
- **OCT4 (POU5F1)** (stem cell identity)
- **VEGF-A** (shared with HIF-1α; HIF-2α dominant in RCC)
- **CCND1** (cyclin D1, G1/S cell cycle)
- **TGF-α** (EGFR ligand → autocrine signaling in RCC)
- **TWIST1** (EMT)
- **FN1** (fibronectin, matrix remodeling)

## Mechanism

### Belzutifan — HIF-2α PAS-B allosteric inhibitor

**Mechanism of action:**
Belzutifan (PT2977, MK-6482) is a first-in-class small molecule that binds the PAS-B hydrophobic pocket of HIF-2α → disrupts HIF-2α/ARNT PAS-B heterodimerization without affecting VHL-mediated degradation; HIF-2α protein accumulates but is transcriptionally inactive (cannot form functional heterodimer); selective for HIF-2α over HIF-1α due to distinct PAS-B cavity geometry.

**Class effects:**
- Anemia: belzutifan reduces EPO transcription → erythropoiesis suppression → dose-dependent anemia requiring EPO monitoring and dose adjustment or ESA support
- Hypoxia-like response: HIF-2α suppression mimics a cellular "normoxia" signal; peripheral O₂ monitoring recommended (risk of hypoxia-related symptoms)
- Does NOT inhibit VHL tumor suppressor itself → no interference with VHL's non-HIF functions (JADE1 histone acetylation, mitotic checkpoint)

**Clinical results — VHL disease (LITESPARK-002, Phase 2, N=61):**
Germline VHL mutations; belzutifan 120 mg daily; primary endpoint ORR for RCC 49%; ORR hemangioblastoma 30%; ORR pNET 78%; responses durable (median not reached); FDA approved August 2021 [^jonasch-2021-belzutifan]

**Clinical results — Advanced RCC (LITESPARK-005, Phase 3, N=746):**
Belzutifan vs everolimus in RCC after PD-1 inhibitor + VEGFR-TKI; PFS HR 0.75 (95% CI 0.63-0.90, p<0.001); ORR 22% vs 4%; OS HR 0.88 (p=0.27, NS at interim); FDA approved December 2023 for advanced RCC after prior PD-1 and VEGFR therapy [^choueiri-2023-litespark005]

**Next-generation HIF-2α combinations:**
Belzutifan + cabozantinib (LITESPARK-003/COSMIC-313 comparison cohort): Phase 1/2 favorable; belzutifan + lenvatinib (LITESPARK-008): Phase 3 vs standard of care in frontline RCC; HIF-2α + PD-1 blockade combinations in VHL disease are exploratory.

### EPAS1 mutations in hereditary erythrocytosis and paraganglioma

**EPAS1 GOF mutations causing erythrocytosis:**
Heterozygous germline mutations in EPAS1 at or near PHD2 hydroxylation sites (Pro405 region, Pro531 region) → HIF-2α unable to be hydroxylated → constitutively active → EPO overproduction → secondary erythrocytosis; phenotype: high Hgb/Hct, low serum EPO, normal JAK2 V617F; some have concurrent pheochromocytoma or somatostatinoma (rare PPGL association); treatment: phlebotomy, hydroxyurea; belzutifan theoretically applicable (clinical data limited).

**EPAS1 mutations in paraganglioma/pheochromocytoma (PPGL):**
Somatic EPAS1 mutations in ~9% sporadic PPGL; often large deletions or missense at PHD interaction surface; associated with multifocal and metastatic disease; EPAS1-mutant PPGL → high HIF-2α → EPO overproduction → erythrocytosis as a presenting symptom; work-up: catecholamines + genetic testing (EPAS1, SDHA/B/C/D, RET, NF1, VHL, MAX, TMEM127).

## Connections

- `connects-to` → **[VHL](../../03-molecular/vhl/README.md)** — VHL E3 ubiquitin ligase targets PHD2-hydroxylated HIF-2α for proteasomal degradation; VHL loss → HIF-2α stabilization → EPO/VEGF activation; belzutifan is FDA-approved for VHL disease-associated RCC, hemangioblastoma, and pNET.
- `connects-to` → **[JAK2](../../03-molecular/jak2/README.md)** — HIF-2α drives EPO transcription → JAK2/STAT5 activation in erythroid progenitors; JAK2 V617F in PV constitutively activates erythropoiesis, mimicking EPO-independent signaling; ruxolitinib suppresses HIF-2α expression in myeloid cells.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTORC1 promotes HIF-2α translation via S6K/4E-BP1 phosphorylation; HIF-2α activates VEGF → PI3K-AKT-mTOR → angiogenesis; everolimus has activity in VHL-mutant RCC; dual HIF-2α+mTOR inhibition explored in ccRCC.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — HIF-2α is the principal transcriptional activator of VEGF in VHL-mutant RCC; EPAS1 binds HRE upstream of VEGF promoter → VEGF secretion → angiogenesis; belzutifan targets HIF-2α upstream, suppressing VEGF production in RCC.
- `connects-to` → **[EGLN1](../../03-molecular/egln1/README.md)** — EGLN1 (PHD2) hydroxylates HIF-2α at Pro405/Pro531 → VHL-mediated degradation; Tibetan EGLN1 D4E/C127S increases HIF-2α hydroxylation → blunted EPO at altitude; PHD inhibitors stabilize HIF-2α → EPO upregulation for CKD anemia.
- `connects-to` → **[Renal Cell Carcinoma](../../07-system/renal-cell-carcinoma/README.md)** — HIF-2α (EPAS1) is the dominant oncogenic driver in VHL-mutant clear cell RCC (~90% have VHL LOF); activates VEGF, TGF-α, CCND1, OCT4 → tumor angiogenesis and stemness; belzutifan (PAS-B allosteric inhibitor) FDA-approved for advanced ccRCC after PD-1 + VEGFR TKI (LITESPARK-005).
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — HIF-2α is the principal EPO activator in renal peritubular cells; EPAS1 GOF mutations → HIF-2α resistant to PHD2 hydroxylation → hereditary erythrocytosis; Chuvash polycythemia (VHL R200W) stabilizes HIF-2α → EPO excess; PHD inhibitors target the HIF-2α/EPO axis for CKD anemia.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^jonasch-2021-belzutifan]: Jonasch E, Donskov F, Iliopoulos O, et al. Belzutifan for renal cell carcinoma in von Hippel-Lindau disease. *N Engl J Med.* 2021;385(22):2036-2046. [doi:10.1056/NEJMoa2103979](https://doi.org/10.1056/NEJMoa2103979) · [PubMed 34818478](https://pubmed.ncbi.nlm.nih.gov/34818478/)
[^choueiri-2023-litespark005]: Choueiri TK, Powles T, Albiges L, et al. Belzutifan versus everolimus for advanced renal-cell carcinoma. *N Engl J Med.* 2023;388(10):869-881. [doi:10.1056/NEJMoa2212875](https://doi.org/10.1056/NEJMoa2212875) · [PubMed 36827464](https://pubmed.ncbi.nlm.nih.gov/36827464/)

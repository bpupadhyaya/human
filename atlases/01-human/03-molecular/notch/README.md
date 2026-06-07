---
schema: human-scale-entry/v1
id: notch
name: NOTCH
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Juxtacrine pathway: Jagged/DLL ligands → NICD nuclear translocation → HES/HEY transcription → cell fate decisions. NOTCH1 gain-of-function mutations drive >60% of T-ALL and triple-negative breast cancer; gamma-secretase inhibitors block NOTCH processing."
aliases: ["Notch signaling", "NOTCH1", "NOTCH2", "NOTCH3", "NOTCH4", "HES1", "NICD", "Delta-like ligand", "Jagged", "DLL", "CSL", "RBPJ", "gamma-secretase"]
sources:
  - id: artavanis-1999-notch-review
    type: peer-reviewed
    cite: "Artavanis-Tsakonas S, Rand MD, Lake RJ. Notch signaling: cell fate control and signal integration in development. Science. 1999;284(5415):770-776."
    doi: "10.1126/science.284.5415.770"
    pmid: "10221902"
    url: "https://doi.org/10.1126/science.284.5415.770"
  - id: kopan-2009-notch-mechanism
    type: peer-reviewed
    cite: "Kopan R, Ilagan MX. The canonical Notch signaling pathway: unfolding the activation mechanism. Cell. 2009;137(2):216-233."
    doi: "10.1016/j.cell.2009.03.045"
    pmid: "19379690"
    url: "https://doi.org/10.1016/j.cell.2009.03.045"
  - id: ferrando-2009-notch-tall
    type: peer-reviewed
    cite: "Ferrando AA. The role of NOTCH1 signaling in T-ALL. Hematology Am Soc Hematol Educ Program. 2009;2009:353-361."
    doi: "10.1182/asheducation-2009.1.353"
    pmid: "20008218"
    url: "https://doi.org/10.1182/asheducation-2009.1.353"
cross_links:
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "NOTCH and Wnt-beta-catenin co-regulate stem cell self-renewal; opposing roles in intestinal crypt homeostasis (NOTCH → goblet cell suppression; Wnt → crypt stem cells); co-activation in colorectal and triple-negative breast cancer promotes stemness and therapy resistance."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "NOTCH1 directly activates MYC transcription via intragenic NOTCH-binding elements in T-ALL; MYC is the primary oncogenic effector downstream of NOTCH1 in T-cell lymphoma; pharmacological NOTCH inhibition → MYC downregulation → T-ALL cell cycle arrest."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "NOTCH1 activates p19ARF → p53 stabilization in MEF cells (tumor suppressive context); in squamous cell carcinoma, NOTCH1 loss promotes tumor growth; context-dependent NOTCH-p53 crosstalk determines oncogenic vs. suppressive outcome across cancer types."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "NOTCH and KRAS cooperate in PDAC: KRAS drives NOTCH1/2 ligand expression; combined NOTCH + MEK inhibition has preclinical synergy in PDAC and KRAS-mutant lung adenocarcinoma; NOTCH pathway reactivation is a KRAS-driven adaptive resistance mechanism."
---

# NOTCH

## Overview

**NOTCH signaling** is a conserved **juxtacrine cell-to-cell communication pathway** that controls **cell fate decisions, differentiation, proliferation, and apoptosis** during development and tissue homeostasis. Unlike most signaling pathways that rely on secreted ligands, NOTCH requires direct cell-cell contact: transmembrane ligands (Delta-like: DLL1, DLL3, DLL4; Jagged: JAG1, JAG2) on signal-sending cells bind NOTCH receptors (NOTCH1-4) on signal-receiving cells → receptor proteolytic cleavage → transcriptional output [^artavanis-1999-notch-review].

**Four mammalian NOTCH receptors and their biological roles:**
- **NOTCH1:** T cell development (essential for T-cell lineage commitment from common lymphoid progenitor); gain-of-function mutations in >60% of T-cell acute lymphoblastic leukemia (T-ALL); also breast cancer, CLL
- **NOTCH2:** B cell marginal zone development; gain-of-function in marginal zone lymphoma and diffuse large B cell lymphoma (DLBCL)
- **NOTCH3:** Vascular smooth muscle differentiation; gain-of-function in CADASIL (cerebral autosomal-dominant arteriopathy with subcortical infarcts and leukoencephalopathy — NOTCH3 EGF domain mutations); breast and ovarian cancer
- **NOTCH4:** Endothelial biology and mammary gland development; rarely mutated in cancer

**NOTCH as tumor suppressor vs. oncogene (context-dependent):**
- **Oncogenic:** NOTCH1/2/3 gain-of-function → T-ALL, B-cell lymphoma, breast cancer, colorectal cancer
- **Tumor suppressive:** NOTCH1 loss-of-function mutations in squamous cell carcinomas (skin, head and neck, esophagus — ~15-20% of HNSCC) and bladder cancer; NOTCH acts as a tumor suppressor in stratifying squamous epithelium
- **Context principle:** NOTCH is a lineage-context-dependent master regulator — the same pathway promotes proliferation in T cells but differentiation (and growth arrest) in skin epithelial cells

## Structure

### NOTCH receptor structure and cleavage cascade [^kopan-2009-notch-mechanism]

NOTCH receptors are **single-pass type I transmembrane proteins** (~300 kDa) with a characteristic modular architecture:

**Extracellular domain (ECD):**
- **EGF-like repeats (29-36 depending on receptor):** Ligand-binding domain; EGF repeats 11-12 contact DLL/JAG ligands; O-fucosylation by POFUT1 and further glycosylation by FRINGE proteins (LFNG, MFNG, RFNG) modulate ligand affinity (FRINGE → DLL > JAG preference)
- **Negative regulatory region (NRR):** LNR-HD domain → prevents ligand-independent (metalloprotease) cleavage in the absence of ligand; NRR mutations in T-ALL (HD domain mutations) → ligand-independent activation; NRR is the target of therapeutic antibodies (tarextumab anti-NOTCH2/3, demcizumab anti-DLL4)
- **PEST domain (intracellular):** Rich in Pro-Glu-Ser-Thr → ubiquitination target for FBXW7/Sel10 E3 ligase → NICD proteasomal degradation; PEST domain frameshift/nonsense mutations in T-ALL → prolonged NICD half-life → constitutive NOTCH output

**Three sequential cleavages to generate NICD:**
1. **S1 cleavage (furin, trans-Golgi):** Generates heterodimeric receptor at cell surface; ECD non-covalently bound to transmembrane+intracellular fragment
2. **S2 cleavage (ADAM10/17, extracellular):** Ligand binding → conformational change in NRR → ADAM10 cleaves juxtamembrane domain → membrane-tethered NOTCH extracellular truncation (NEXT)
3. **S3/S4 cleavage (gamma-secretase complex, transmembrane):** NEXT substrate for gamma-secretase (presenilin-1/2 + APH1 + PEN2 + nicastrin) → releases **NICD (Notch intracellular domain)** from membrane → nuclear translocation

**NICD nuclear function:**
- NICD translocates to nucleus → binds **CSL/RBPJ** (CBF-1/Suppressor of Hairless/Lag-2; RBP-Jkappa in mammals) — the key transcriptional mediator
- In absence of NICD: CSL/RBPJ recruits corepressors (SMRT, NCoR, SHARP/MINT, KyoT2) → HES/HEY target genes silenced
- In presence of NICD: NICD → displaces corepressors from CSL → recruits coactivators (MAML1/2/3 — Mastermind-like; p300/CBP) → transcriptional activation of primary NOTCH targets: **HES1, HES5, HEY1, HEY2, HES-related HEYs**

**Primary NOTCH target genes:**
- **HES1 (Hairy/Enhancer of Split 1):** bHLH repressor → represses proneural genes (MATH1, NEUROG), FOXN1, and p21 → proliferation over differentiation
- **HES5:** Neural progenitor maintenance
- **HEY1/HEY2:** Cardiovascular development (heart, vasculature)
- **MYC:** Direct NOTCH1 target in T-ALL via N-Me intronic enhancer — the key oncogenic output
- **CYCLIN D1:** Via NICD-mediated transcription → G1-S transition
- **CD44, ALDH1:** Cancer stem cell markers regulated by NOTCH

## Function

### NOTCH in cancer [^ferrando-2009-notch-tall]

**T-ALL (T-cell acute lymphoblastic leukemia):**
- >60% harbor activating NOTCH1 mutations: either HD domain mutations (ligand-independent S2 cleavage) or PEST domain mutations (prolonged NICD half-life), or both → constitutive HES1 and MYC transcription → T-cell blast proliferation
- **FBXW7 loss (~15% of T-ALL):** Inactivation of E3 ubiquitin ligase for NICD → accumulation of all four NICD proteins → pan-NOTCH activation; FBXW7 is also a common tumor suppressor across many cancers (CRC, cholangiocarcinoma, endometrial)
- Treatment: gamma-secretase inhibitors (GSIs, e.g., compound E, RO4929097) suppress NOTCH in T-ALL but cause GI toxicity (goblet cell metaplasia — NOTCH normally suppresses goblet cell differentiation in intestinal crypts); GI toxicity mitigated by glucocorticoids; clinical trials combining GSI + corticosteroids + BET inhibitors (MYC suppression) ongoing

**Triple-negative breast cancer (TNBC):**
- NOTCH1/2/3 amplification or overexpression in 20-30% of TNBC; NOTCH drives cancer stem cell (CD44high/CD24low) self-renewal; NOTCH3 specifically correlates with resistance to chemotherapy; clinical trials: tarextumab (anti-NOTCH2/3) + nab-paclitaxel; demcizumab (anti-DLL4) + chemotherapy

**Pancreatic ductal adenocarcinoma (PDAC):**
- NOTCH-KRAS cooperation: KRAS-mutant acinar cells activate NOTCH during acinar-to-ductal metaplasia (ADM) → pancreatic intraepithelial neoplasia (PanIN); combined KRAS + NOTCH inhibition is additive preclinically; NOTCH blockade reverses ADM in experimental models

**Colorectal cancer:**
- NOTCH and Wnt cooperate: APC loss (Wnt activation) + NOTCH upregulation → expanded crypt progenitor compartment; NOTCH1 overexpression in ~30% of CRC; anti-DLL4 (navicixizumab) in clinical trials targeting NOTCH in CRC

**Squamous cell carcinoma (tumor suppressor role):**
- NOTCH1/2 loss-of-function mutations in HNSCC (~15%), esophageal SCC (~10%), skin SCC → loss of squamous differentiation program → poorly differentiated aggressive SCC; NOTCH is the most frequently mutated pathway in esophageal SCC after TP53

### NOTCH in development and homeostasis

**Hematopoiesis:** NOTCH1 → T-cell lineage commitment (DLL4 on thymic epithelium → NOTCH1 on progenitor); NOTCH2 → marginal zone B cells, plasmacytoid DC subset; NOTCH1 downregulation → NK cell differentiation

**Vascular biology:** DLL4-NOTCH1 signaling in tip vs. stalk cell selection during angiogenesis; DLL4 (on tip cells) → NOTCH1 on neighboring cells → stalk cell fate; anti-DLL4 → tip cell sprouting but non-productive vessels → paradoxical tumor angiogenesis inhibition; navicixizumab (anti-DLL4+VEGFA bispecific) in trials

**Neural development:** DLL1/3/4 → NOTCH1/2 → HES1 → lateral inhibition (prevents all cells differentiating simultaneously) → neurogenesis from progenitor pool; HES1 oscillations (20-30 min period) coordinate neural progenitor differentiation timing

## Mechanism

### Therapeutic targeting

**Gamma-secretase inhibitors (GSIs):**
- Block S3 cleavage → inhibit NICD release from all 4 NOTCH receptors; pan-NOTCH inhibitors; GI toxicity (goblet cell metaplasia from NOTCH inhibition in intestinal crypts) → intermittent dosing or glucocorticoid co-administration; clinical trials in T-ALL, TNBC, PDAC, desmoid tumors (sporadic and FAP-associated; NOTCH3 signature)

**Antibody-based NOTCH inhibitors:**
- **Anti-DLL4 (demcizumab, navicixizumab):** Blocks DLL4-NOTCH1 → anti-angiogenic + direct anti-tumor; combination with chemotherapy in NSCLC, ovarian cancer Phase 2
- **Anti-NOTCH2/3 (tarextumab):** Blocks NOTCH2 and NOTCH3 → cancer stem cell reduction in pancreatic and small cell lung cancer; Phase 2 trials showed limited single-agent activity

**MAML dominant-negative:**
- Stapled peptides mimicking dominant-negative MAML1 (SAHM1) → disrupt NICD-CSL-MAML ternary complex → block NOTCH transcriptional output without GSI-associated GI toxicity; preclinical efficacy in T-ALL; represents a next-generation NOTCH targeting strategy

## Connections

- `connects-to` → **[Wnt/beta-catenin](../wnt-beta-catenin/README.md)** — NOTCH and Wnt co-regulate stem cell self-renewal; opposing roles in intestinal crypt homeostasis (NOTCH → enterocyte fate; Wnt → crypt stem cells); co-activation promotes stemness and therapy resistance in colorectal and triple-negative breast cancer.
- `connects-to` → **[MYC](../myc/README.md)** — NOTCH1 directly activates MYC transcription via intragenic NOTCH-binding elements in T-ALL; MYC is the primary oncogenic effector downstream of NOTCH1 in T-cell lymphoma; NOTCH inhibition → MYC downregulation → T-ALL cell cycle arrest.
- `connects-to` → **[p53](../p53/README.md)** — NOTCH1 activates p19ARF → p53 stabilization in normal cells; in squamous cell carcinoma, NOTCH1 loss promotes tumor growth; context-dependent NOTCH-p53 crosstalk determines oncogenic vs. suppressive outcome across cancer types.
- `connects-to` → **[KRAS](../kras/README.md)** — NOTCH and KRAS cooperate in PDAC: KRAS drives NOTCH1/2 ligand expression; combined NOTCH + MEK inhibition has preclinical synergy in PDAC and KRAS-mutant lung adenocarcinoma; NOTCH pathway reactivation is a KRAS-driven adaptive resistance mechanism.

[^artavanis-1999-notch-review]: Artavanis-Tsakonas S, Rand MD, Lake RJ. Notch signaling: cell fate control and signal integration in development. *Science.* 1999;284(5415):770-776. [doi:10.1126/science.284.5415.770](https://doi.org/10.1126/science.284.5415.770) · [PubMed 10221902](https://pubmed.ncbi.nlm.nih.gov/10221902/)
[^kopan-2009-notch-mechanism]: Kopan R, Ilagan MX. The canonical Notch signaling pathway: unfolding the activation mechanism. *Cell.* 2009;137(2):216-233. [doi:10.1016/j.cell.2009.03.045](https://doi.org/10.1016/j.cell.2009.03.045) · [PubMed 19379690](https://pubmed.ncbi.nlm.nih.gov/19379690/)
[^ferrando-2009-notch-tall]: Ferrando AA. The role of NOTCH1 signaling in T-ALL. *Hematology Am Soc Hematol Educ Program.* 2009;2009:353-361. [doi:10.1182/asheducation-2009.1.353](https://doi.org/10.1182/asheducation-2009.1.353) · [PubMed 20008218](https://pubmed.ncbi.nlm.nih.gov/20008218/)

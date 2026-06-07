---
schema: human-scale-entry/v1
id: ptpn11
name: PTPN11
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "PTPN11 (SHP2) is a non-receptor protein tyrosine phosphatase that activates RAS-MAPK signaling via GAB1/IRS-1 dephosphorylation; germline GOF mutations → Noonan syndrome; somatic PTPN11 GOF → JMML and AML; SHP2 inhibitors (SHP099, RMC-4630) are in clinical development."
aliases: ["PTPN11", "SHP2", "SHP-2", "PTPN11 Noonan", "SHP2 Noonan", "PTPN11 JMML", "SHP2 RAS", "PTPN11 leukemia", "SHP2 inhibitor", "RASopathy PTPN11"]
sources:
  - id: tartaglia-2001-ptpn11-noonan
    type: peer-reviewed
    cite: "Tartaglia M, Mehler EL, Goldberg R, et al. Mutations in PTPN11, encoding the protein tyrosine phosphatase SHP-2, cause Noonan syndrome. Nat Genet. 2001;29(4):465-468."
    doi: "10.1038/ng772"
    pmid: "11704759"
    url: "https://doi.org/10.1038/ng772"
  - id: loh-2004-ptpn11-jmml
    type: peer-reviewed
    cite: "Loh ML, Vattikuti S, Schubbert S, et al. Mutations in PTPN11 implicate the SHP-2 phosphatase in leukemogenesis. Blood. 2004;103(6):2325-2331."
    doi: "10.1182/blood-2003-09-3287"
    pmid: "14644997"
    url: "https://doi.org/10.1182/blood-2003-09-3287"
cross_links:
  - target: 01-human/07-system/noonan-syndrome
    relation: connects-to
    note: "Germline PTPN11 GOF mutations are the most common cause of Noonan syndrome (~50%); SHP2 hyperactivation → RAS-MAPK overactivation → growth restriction, cardiac development defects, and hematologic abnormalities; JMML risk elevated ~150-fold in Noonan syndrome."
  - target: 01-human/03-molecular/lztr1
    relation: connects-to
    note: "PTPN11 and LZTR1 are both RASopathy genes causing Noonan syndrome: PTPN11 GOF hyperactivates SHP2/RAS signaling; LZTR1 LOF prevents CUL3-mediated RAS ubiquitination → RAS accumulation; both disorders share short stature, pulmonary stenosis, and HCM features."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "PTPN11 (SHP2) activates RAS by dephosphorylating GAB1 and IRS-1 → increased RAS-GTP; SHP2 and oncogenic KRAS both hyperactivate ERK1/2 → cell proliferation; SHP2 inhibitors synergize with MEK/ERK inhibitors to block KRAS-driven cancers; KRAS G12C cancers are SHP2-dependent."
  - target: 01-human/03-molecular/nf1
    relation: connects-to
    note: "PTPN11 (SHP2) and NF1 regulate RAS activity by opposing mechanisms: SHP2 activates RAS via GAP dephosphorylation; NF1 inactivates RAS as a GTPase-activating protein; both are RAS-MAPK pathway nodes; SHP2 GOF (Noonan) and NF1 LOF (neurofibromatosis) both cause RASopathies."
---

# PTPN11

## Overview

**PTPN11** (protein tyrosine phosphatase non-receptor type 11; also **SHP2**, SH2 domain-containing phosphatase 2) is a 593 amino acid (68 kDa) **non-receptor protein tyrosine phosphatase** that serves as a central positive regulator of the **RAS-MAPK signaling cascade**. SHP2 contains two N-terminal SH2 domains (N-SH2, C-SH2) that mediate binding to phosphotyrosine-containing scaffolds (GAB1, IRS-1, GRB2-associated binder proteins), and a C-terminal catalytic phosphatase domain (PTP domain). In the inactive (autoinhibited) state, the N-SH2 domain occludes the PTP active site by intramolecular binding; upon engagement of phosphotyrosine-containing scaffolds, the N-SH2 releases the PTP domain → activated SHP2 dephosphorylates negative regulatory phosphosites on RAS exchange factors and GAP docking proteins → net effect: **RAS-GTP accumulation → ERK1/2 activation → cell proliferation, survival, and differentiation**. SHP2 is thus an obligate component of growth factor receptor signaling (EGFR, FGFR, MET, KIT, PDGFRβ) and is required for full ERK activation downstream of these receptors.

PTPN11 gain-of-function (GOF) germline mutations were identified as the most common cause of **Noonan syndrome (NS)** by Tartaglia et al. in 2001 — the first RASopathy gene identified [^tartaglia-2001-ptpn11-noonan]. PTPN11 GOF mutations cluster in two "hot spot" regions that destabilize the autoinhibitory conformation (typically N-SH2 or PTP domain interface residues: N308D, T468M, E76K, D61Y, A72V being the most common). Somatic PTPN11 GOF mutations (often distinct from NS mutations; highest gain-of-function activity) are found in **juvenile myelomonocytic leukemia (JMML)** (~35% of cases) and **AML** (~5%), established by Loh et al. in 2004 [^loh-2004-ptpn11-jmml]. SHP2 has emerged as an important oncology drug target: allosteric SHP2 inhibitors (SHP099, RMC-4630, JAB-3068) that stabilize the autoinhibited conformation are in clinical trials for KRAS-mutant and RAS-MAPK-dependent cancers.

**PTPN11 germline mutations across RASopathies:**

| Mutation cluster | Syndrome | LOF/GOF | Mechanism |
|---|---|---|---|
| N-SH2 (D61Y, E76K, Y63C) | Noonan syndrome | GOF | Disrupts N-SH2/PTP autoinhibition → constitutive PTP activity |
| PTP domain (T468M, I282V) | Noonan syndrome | GOF | Reduces PTP domain engagement with N-SH2 → less autoinhibited |
| Scattered PTP domain (T468M, Q510E, G503R) | LEOPARD (Noonan with lentigines) | LOF (paradox) | Reduced catalytic activity → unclear GOF signaling mechanism |
| Somatic (E76K, E69K, highly activating) | JMML, AML | GOF (high activity) | Higher catalytic activity than germline; leukemogenic |

## Structure

### PTPN11 protein domains

**N-SH2 domain (aa 1-104):**
- First SH2 domain; directly occludes the PTP active site in the autoinhibited conformation via a "wedge" interaction at the PTP catalytic cleft
- Phosphotyrosine binding: N-SH2 binds pY-containing scaffolds (GAB1 pY627, IRS-1 pY896, etc.) → releases PTP domain from autoinhibition → activates SHP2
- **Hot spot for Noonan GOF mutations**: residues at the N-SH2/PTP interface (D61, E76, Y63, A72, G60) — mutation of these residues destabilizes the autoinhibitory contact → constitutive basal PTP activity elevated 2-10x
- The D61Y mutation (most common Noonan-causing PTPN11 variant): Asp61 forms a key hydrogen bond with the PTP domain in the closed conformation; D61Y eliminates this bond → SHP2 predominantly in open conformation

**C-SH2 domain (aa 112-216):**
- Second SH2 domain; less directly involved in autoinhibition than N-SH2; primarily mediates protein-protein interaction with phosphotyrosine scaffolds (EGFR pY992, PDGFRβ pY716, GAB2)
- Required for full SHP2 activation: tandem SH2 engagement with doubly-phosphorylated scaffolds (diphosphotyrosyl peptides) → more efficient PTP domain release than single pY engagement
- C-SH2 mutations cause a smaller subset of Noonan syndrome cases

**PTP catalytic domain (aa 217-525):**
- Classic PTP fold; contains the signature motif (H/V)C(X)5R → Cys459 is the active-site nucleophile that attacks phosphotyrosine → phosphoenzyme intermediate → water-mediated hydrolysis → dephosphorylation
- PTP domain occludes its own active site in the closed conformation by contact with the N-SH2 wedge; in the open conformation, the active site is fully accessible
- **LEOPARD syndrome (LOF) mutations**: T468M is the most common; LEOPARD syndrome paradoxically involves PTPN11 mutations with REDUCED catalytic activity (T468M is a catalytic dead-mutant-like variant) → dominant negative effect? Or alternative gain-of-function signaling? The precise mechanism of how PTP LOF mutations cause a distinct GOF-like phenotype remains debated; scaffold function of SHP2 (independent of catalysis) may be relevant
- **SHP2 allosteric inhibitors**: bind a cryptic pocket in the PTP domain adjacent to the N-SH2/PTP interface → stabilize closed conformation → SHP2 locked in autoinhibited state; SHP099 (tool compound), RMC-4630 (first-in-class clinical allosteric SHP2 inhibitor, Relay Therapeutics), JAB-3068, TNO155

**C-terminal tail (aa 526-593):**
- Contains two tyrosine phosphorylation sites (Tyr542, Tyr580): phosphorylated by activated receptor tyrosine kinases → creates SH2 docking sites for GRB2 and other adaptors → amplification loop; pTyr542 binds GRB2 → SOS1 recruitment → additional RAS-GEF activity
- This C-terminal phosphorylation creates a positive feedback loop: RTK → SHP2 activation → SHP2 pTyr542/580 → GRB2-SOS1 → RAS-GEF → more ERK activation

### PTPN11 in the RAS-MAPK signaling cascade

**SHP2 activation by growth factor receptors:**
1. EGF/FGF/HGF/SCF → receptor tyrosine kinase (RTK) autophosphorylation → pTyr sites recruit GAB1/IRS-1 scaffold proteins
2. GAB1 pY627 → recruits SHP2 N-SH2 → SHP2 activated (N-SH2 releases PTP domain)
3. Active SHP2 dephosphorylates negative regulatory sites on GAB1 (restores SHP2 binding capacity) and on RasGAP docking proteins (prevents RasGAP recruitment) → net: increased RAS-GTP
4. Activated RAS → RAF → MEK1/2 → ERK1/2 → nuclear transcription (Fos, Jun, Elk-1) → proliferation, survival, differentiation
5. SHP2 is also required for full SOS1-GRB2 activity (via C-terminal pTyr scaffold function) — dual mechanism of RAS activation

**SHP2 substrates (direct dephosphorylation targets):**
- GAB1 pY659/pY627: dephosphorylation maintains GAB1-SHP2 interaction (feedback)
- Sprouty proteins (SPRY1/2): SPRY normally inhibits GRB2-SOS1 by sequestering GRB2; SHP2 dephosphorylates SPRY → relieves SPRY inhibition → allows GRB2-SOS1 to activate RAS
- Paxillin: dephosphorylation modulates cell adhesion (SHP2 at focal adhesions)
- RET (when dephosphorylated by SHP2 at pY1062, abrogates SHP2-IRS-1 signaling)
- **PTPN11 GOF net effect**: all substrates dephosphorylated faster → net: less SPRY activity, more RAS-GEF activity, more RAS-GTP, more ERK

## Function

### PTPN11 in development

**Developmental functions:**
- PTPN11 is expressed throughout embryogenesis; required for early gastrulation, trophoblast differentiation (Ptpn11 null mice die at E8.5)
- FGF-SHP2 signaling is required for mesoderm induction and neural crest migration; PTPN11 is the key transducer of FGF signals in the early embryo
- RAS-MAPK pathway via SHP2 mediates: cardiac outflow tract development (defective in Noonan syndrome → pulmonary stenosis, HCM); craniofacial morphogenesis (FGF-SHP2 in neural crest); chondrocyte differentiation and long-bone growth (FGFR3-SHP2 regulates chondrogenesis)
- PTPN11 in hematopoiesis: required for normal erythroid, myeloid, and megakaryocyte differentiation; SHP2 downstream of EPO receptor (EPOR) and SCF receptor (KIT); PTPN11 GOF → myeloid hyperproliferation (JMML phenotype)

### PTPN11 GOF in Noonan syndrome pathogenesis

**Developmental consequences of SHP2 hyperactivation:**
- **Short stature**: SHP2 hyperactivation in chondrocytes → constitutive ERK1/2 → premature chondrocyte hypertrophy → reduced epiphyseal growth plate activity → growth restriction; GH axis intact but GH response (via JAK2-STAT5 and MAPK) is partially dysregulated
- **Congenital heart defects**: SHP2 GOF in endocardial cells → ERK-mediated dysregulation of endocardial cushion development → pulmonary valve stenosis and HCM (particularly E76K, D61G mutations → more severe cardiac phenotype)
- **Facial dysmorphia**: SHP2 in neural crest cells → abnormal craniofacial morphogenesis → hypertelorism, low-set posteriorly-rotated ears, ptosis
- **Hematologic**: myeloproliferation and transient myeloproliferative disorders in neonatal Noonan; JMML in ~5% of Noonan syndrome patients with PTPN11 mutations (dramatically elevated risk vs. general population)
- **Lymphedema**: SHP2 in lymphatic endothelial cells; lymphedema/lymphatic vessel anomalies in subset of Noonan patients

**LEOPARD syndrome (Noonan with multiple lentigines, OMIM #151100):**
- Multiple lentigines (dark spots on skin, face, trunk), ECG conduction defects, Ocular hypertelorism, Pulmonary stenosis, Abnormal genitalia, Retardation of growth, Deafness (sensorineural) — LEOPARD mnemonic
- Caused by PTPN11 PTP domain LOF mutations (T468M, Q510E, G503R) — paradoxically GOF phenotype
- Lentigines are the pathognomonic feature (not melanocytic nevi; different pathology from Peutz-Jeghers/Carney complex lentigines)
- Cardiac: predominantly HCM (not pulmonary stenosis as in classic Noonan)
- Mechanism: T468M SHP2 cannot dephosphorylate substrates catalytically but retains scaffold function; may act as dominant negative trapping SHP2 substrates while blocking normal SHP2 function → net altered signal; the distinct phenotype (lentigines, HCM predominance) vs. classic Noonan (PS) reflects different signaling output

### PTPN11 somatic mutations in leukemia

**JMML (juvenile myelomonocytic leukemia):**
- PTPN11 somatic GOF mutations in ~35% of JMML (most common single driver); somatic mutations are often highly activating (E69K, E76K, E69V) — higher basal activity than germline Noonan mutations
- JMML: childhood myeloproliferative neoplasm (age <4 years); monocytosis, splenomegaly, hypersensitivity to GM-CSF, immature myeloid cells in peripheral blood; aggressive; standard treatment is allogeneic stem cell transplant
- Other JMML genes: NF1 LOF (~15%), KRAS/NRAS mutations (~30%), CBL mutations (~15%)
- All JMML mutations converge on RAS-MAPK hyperactivation
- PTPN11 E76K: somatic JMML mutation with ~10x higher basal PTP activity than wildtype; also found in some Noonan syndrome patients (germline) who have very high JMML risk

**AML (~5%):**
- PTPN11 mutations found in 5-7% of AML, particularly in certain subtypes; often co-occurs with FLT3 ITD or NPM1 mutations; may confer poor prognosis
- Mechanism: SHP2 GOF → constitutive RAS-ERK in AML blasts → proliferation/survival advantage

## Mechanism

### Allosteric SHP2 inhibition — therapeutic strategy

**Rationale for SHP2 inhibition in KRAS-driven cancers:**
- KRAS-mutant cancers (G12C, G12D, G12V) are RAS-GTP-dependent; SHP2 is required for upstream signal amplification to RAS even when KRAS is constitutively active
- KRAS G12C inhibitors (sotorasib, adagrasib) → adaptive resistance via reactivation of upstream RTK signaling → SHP2 becomes a key resistance mechanism; combining KRAS G12C + SHP2 inhibitor → prevents upstream RTK-driven resistance bypass
- KRAS G12D/V (non-G12C): no direct inhibitor approved; SHP2 inhibition reduces RAS-GTP cycling in these tumors
- SHP2 required for feedback loop: MEK inhibitor → RTK upregulation → RAS → SHP2 → ERK reactivation; SHP2 inhibitor breaks this feedback

**SHP2 allosteric inhibitor mechanism:**
- Bind a cryptic tunnel between the N-SH2 and PTP domains (only accessible in open/active conformation)
- Stabilize the closed (autoinhibited) conformation → SHP2 locked inactive
- Examples: SHP099 (preclinical tool), TNO155 (Novartis, Phase I: NCT03114319), RMC-4630 (Relay/Sanofi, Phase I/II), JAB-3068 (Phase I)
- Combination trials: RMC-4630 + sotorasib (KRAS G12C); TNO155 + MRTX849; TNO155 + ribociclib (CDK4/6 inhibitor)

**GH treatment in Noonan syndrome:**
- Recombinant human GH (rhGH, 0.05 mg/kg/day) approved for Noonan syndrome-associated short stature
- Mechanism: SHP2 LOF (not GOF) would be expected to impair GH-MAPK signaling; GOF SHP2 paradoxically impairs GH signaling in chondrocytes via ERK-mediated negative feedback on IGF-1 action; rhGH treatment achieves modest height improvement (~4-5 cm final adult height gain vs. untreated)
- MEK inhibitor (trametinib) trials in Noonan syndrome: cardiac HCM response; height effect under investigation; potential future disease-modifying therapy

**PTPN11 as biomarker:**
- Noonan syndrome genetic panels: PTPN11 sequencing first (~50% diagnostic yield); followed by SOS1, RAF1, KRAS, LZTR1, RIT1, BRAF, MAP2K1, NRAS, SHOC2, CBL if PTPN11 negative
- JMML: somatic PTPN11 sequencing (E76K, E69 region) from bone marrow; tumor allele frequency reflects clone size; serial monitoring for clonal evolution
- AML: part of myeloid mutation panels; prognostic significance in combination with other mutations (FLT3, NPM1, TP53)

## Connections

- `connects-to` → **[Noonan Syndrome](../../07-system/noonan-syndrome/README.md)** — Germline PTPN11 GOF mutations are the most common cause of Noonan syndrome (~50%); SHP2 hyperactivation → RAS-MAPK overactivation → growth restriction, cardiac development defects, and hematologic abnormalities; JMML risk elevated ~150-fold in Noonan syndrome.
- `connects-to` → **[LZTR1](../../03-molecular/lztr1/README.md)** — PTPN11 and LZTR1 are both RASopathy genes causing Noonan syndrome: PTPN11 GOF hyperactivates SHP2/RAS signaling; LZTR1 LOF prevents CUL3-mediated RAS ubiquitination → RAS accumulation; both disorders share short stature, pulmonary stenosis, and HCM features.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — PTPN11 (SHP2) activates RAS by dephosphorylating GAB1 and IRS-1 → increased RAS-GTP; SHP2 and oncogenic KRAS both hyperactivate ERK1/2 → cell proliferation; SHP2 inhibitors synergize with MEK/ERK inhibitors to block KRAS-driven cancers; KRAS G12C cancers are SHP2-dependent.
- `connects-to` → **[NF1](../../03-molecular/nf1/README.md)** — PTPN11 (SHP2) and NF1 regulate RAS activity by opposing mechanisms: SHP2 activates RAS via GAP dephosphorylation; NF1 inactivates RAS as a GTPase-activating protein; both are RAS-MAPK pathway nodes; SHP2 GOF (Noonan) and NF1 LOF (neurofibromatosis) both cause RASopathies.

[^tartaglia-2001-ptpn11-noonan]: Tartaglia M, Mehler EL, Goldberg R, et al. Mutations in PTPN11, encoding the protein tyrosine phosphatase SHP-2, cause Noonan syndrome. *Nat Genet.* 2001;29(4):465-468. [doi:10.1038/ng772](https://doi.org/10.1038/ng772) · [PubMed 11704759](https://pubmed.ncbi.nlm.nih.gov/11704759/)
[^loh-2004-ptpn11-jmml]: Loh ML, Vattikuti S, Schubbert S, et al. Mutations in PTPN11 implicate the SHP-2 phosphatase in leukemogenesis. *Blood.* 2004;103(6):2325-2331. [doi:10.1182/blood-2003-09-3287](https://doi.org/10.1182/blood-2003-09-3287) · [PubMed 14644997](https://pubmed.ncbi.nlm.nih.gov/14644997/)

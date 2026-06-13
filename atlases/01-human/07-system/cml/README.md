---
schema: human-scale-entry/v1
id: cml
name: Chronic Myeloid Leukemia
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Clonal myeloid leukemia driven by t(9;22)/BCR-ABL (Philadelphia chromosome); imatinib (IRIS trial) transformed CML from fatal to chronic; 5-year OS >85%. TKI-refractory T315I → ponatinib or asciminib; treatment-free remission achievable in ~50% of deep molecular responders."
aliases: ["CML", "chronic myelogenous leukemia", "Philadelphia chromosome leukemia", "BCR-ABL leukemia"]
sources:
  - id: druker-2006-iris-5year
    type: peer-reviewed
    cite: "Druker BJ, Guilhot F, O'Brien SG, et al. Five-year follow-up of patients receiving imatinib for chronic myeloid leukemia. N Engl J Med. 2006;355(23):2408-2417."
    doi: "10.1056/NEJMoa062867"
    pmid: "17151364"
    url: "https://doi.org/10.1056/NEJMoa062867"
  - id: hochhaus-2019-dasatinib
    type: peer-reviewed
    cite: "Hochhaus A, Saglio G, Hughes TP, et al. Long-term benefits and risks of frontline nilotinib vs imatinib for chronic myeloid leukemia in chronic phase: 5-year update of the randomized ENESTnd trial. Leukemia. 2016;30(5):1044-1054."
    doi: "10.1038/leu.2016.5"
    pmid: "26816503"
    url: "https://doi.org/10.1038/leu.2016.5"
cross_links:
  - target: 01-human/03-molecular/abl1
    relation: connects-to
    note: "CML is caused by BCR-ABL fusion (t(9;22)); ABL1 kinase domain is the drug target; imatinib/dasatinib/nilotinib/bosutinib inhibit ABL1; T315I gatekeeper → ponatinib or asciminib (STAMP); MR4.5 molecular response enables treatment-free remission attempts."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "BCR-ABL constitutively phosphorylates STAT5 (and STAT3) → transcription of BCL-XL, MYC, and cyclin D1 → blast survival and proliferation; STAT5 activation is a dominant signaling output of BCR-ABL; TKI response correlates with STAT5 dephosphorylation."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "BCR-ABL → PI3K-AKT → mTORC1 → S6K and 4EBP1 → protein synthesis and survival; mTOR pathway activation mediates imatinib resistance in some CML clones; dual PI3K-mTOR inhibitors studied as combination with TKIs in BCR-ABL-positive blast crisis."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "BCR-ABL activates SRC-family kinases (LYN, HCK, FGR) in CML; SRC kinases promote blast crisis transformation and TKI resistance; dasatinib and bosutinib inhibit both ABL and SRC-family kinases — dual ABL/SRC inhibition relevant in lymphoid blast crisis."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "BCR-ABL → PI3K → AKT → mTOR → S6K/4EBP1 → protein synthesis and cell survival; AKT phosphorylates BAD → prevents apoptosis in CML cells; imatinib resistance associated with PI3K/AKT activation independent of BCR-ABL; AKT inhibition synergizes with TKIs in blast crisis CML."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "BCR-ABL → STAT5/NF-κB → MYC transcription → G1/S acceleration; MYC amplification is common in blast crisis transformation; MYC overexpression promotes self-renewal of CML LSCs; BRD4 inhibitors (JQ1) reduce MYC expression and overcome TKI resistance in CML blast crisis models."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "RB1 inactivated in CML blast crisis via CDK4/6 hyperactivation; E2F release drives myeloid or lymphoid blast transformation; BCR-ABL accelerates CDK2-mediated RB1 inactivation; palbociclib (CDK4/6 inhibitor) re-engages RB1 and sensitizes TKI-resistant blast crisis to apoptosis."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "CML is defined by uncontrolled expansion of the neutrophil lineage: BCR-ABL drives massive leukocytosis with granulocytes at all maturation stages and hallmark basophilia; unlike normal neutrophils they retain function early, so infection is not the initial problem."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "The CML marrow is markedly hypercellular with a high myeloid:erythroid ratio and 'dwarf' megakaryocytes; the Philadelphia chromosome t(9;22) is detected here, and marrow blast percentage defines chronic phase (<10%), accelerated (10-19%), and blast crisis (≥20%)."
  - target: 01-human/07-system/cll
    relation: connects-to
    note: "CLL and CML are the two chronic adult leukemias from opposite lineages: CLL is a B-lymphoid accumulation of mature CD5+ cells driven by BCR/BTK signaling, while CML is a myeloid proliferation driven by the BCR-ABL fusion kinase — different cells, drivers, and targeted drugs."
  - target: 01-human/07-system/myeloproliferative-neoplasms
    relation: connects-to
    note: "CML is the BCR-ABL1-positive classic myeloproliferative neoplasm: like PV, ET and myelofibrosis it is a clonal stem-cell overproduction of mature myeloid cells, but its Philadelphia chromosome and exquisite TKI sensitivity set it apart from the JAK2/CALR-driven MPNs."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "CML's natural history is progression to acute leukemia: untreated, the chronic phase accelerates into a blast crisis that behaves like acute leukemia—myeloid (AML-like) in ~70%, lymphoid in the rest—so TKI therapy aims to prevent this transformation, which remains hard to treat."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Splenomegaly is a hallmark of CML: massive extramedullary myeloid proliferation enlarges the spleen, causing early satiety and left-upper-quadrant pain at presentation; spleen size featured in old prognostic scores and shrinks rapidly once tyrosine-kinase inhibitors control it."
---

# Chronic Myeloid Leukemia

## Overview

**Chronic myeloid leukemia (CML)** is a clonal myeloproliferative neoplasm defined by the **Philadelphia chromosome** — the translocation t(9;22)(q34;q11.2) — which fuses the *BCR* gene on chromosome 22 with the *ABL1* gene on chromosome 9, creating the **BCR-ABL1 fusion oncoprotein**. The Philadelphia chromosome is present in >95% of CML and is both the defining molecular event and the therapeutic target [^druker-2006-iris-5year].

**Epidemiology:**
- Incidence: ~2/100,000 per year; ~9,000 new cases/year in the United States
- Median age at diagnosis: ~55-60 years; can occur at any age
- Accounts for ~15% of all adult leukemias

**Natural history (without treatment):**
- **Chronic phase (CP):** Most patients present here (~90%); WBC markedly elevated with left-shifted myeloid maturation; splenomegaly; blasts <10% in blood/marrow; relatively indolent, median duration 3-5 years without effective treatment
- **Accelerated phase (AP):** Blasts 10-19% in blood/marrow, basophilia >20%, thrombocytopenia unrelated to therapy, clonal evolution; intermediate
- **Blast crisis (BC):** Blasts ≥20% in blood/marrow; myeloid BC (~70%) or lymphoid BC (~30%); resembles acute leukemia; historically median survival <6 months without allogenic SCT

**Treatment-free remission (TFR):**
Following the imatinib revolution, the current frontier is achieving **deep molecular response (DMR)**: MR4 (BCR-ABL1/ABL1 ≤0.01% IS) or MR4.5 (≤0.0032% IS). Approximately 50% of patients who discontinue imatinib after sustained DMR maintain molecular remission — true functional cure without continued TKI. Second-generation TKIs (nilotinib, dasatinib) achieve DMR faster → higher TFR rates.

## Structure

### Disease biology

**The Philadelphia chromosome:**
- **t(9;22)(q34;q11.2):** Translocation places ABL1 exons 2+ under control of BCR regulatory sequences → BCR-ABL1 fusion mRNA
- **p210 BCR-ABL:** Most common; BCR breakpoint in major breakpoint cluster region (M-bcr, exons 13-14); 210 kDa; characteristic of CML and ~25% of adult ALL
- **p190 BCR-ABL:** BCR breakpoint in minor bcr (e1); 190 kDa; more common in Ph+ ALL; higher constitutive kinase activity → more aggressive

**BCR-ABL signaling pathways:**
1. **RAS-MAPK:** GRB2 binds pY177-BCR → SOS → RAS-GTP → ERK1/2 → proliferation
2. **STAT5:** BCR-ABL directly phosphorylates STAT5 → BCL-XL, MCL-1, MYC → survival and self-renewal of LSCs
3. **PI3K-AKT-mTOR:** PI3K recruitment via BCR-ABL/IRS-1 → AKT → mTOR → protein synthesis
4. **SRC-family kinases:** BCR-ABL activates LYN, HCK, FGR → additional survival signals

### Bone marrow pathology

**Peripheral blood:** Leukocytosis (WBC typically 50,000-500,000/μL), left-shifted granulocytes (all stages), basophilia (hallmark), thrombocytosis in ~50%, anemia
**Bone marrow:** Hypercellular (>90%), myeloid:erythroid ratio markedly elevated, megakaryocyte dysplasia ("dwarf" megakaryocytes), minimal blast increase in CP
**Cytogenetics:** Ph+ in >95% (FISH or karyotype); ~5% have variant translocations involving additional chromosomes

### Molecular monitoring

**BCR-ABL1 quantitative PCR (qPCR):**
- Reported on the **International Scale (IS)** as BCR-ABL1/ABL1 % transcript ratio
- Standardized so that 100% IS = pre-treatment CML
- **Major molecular response (MMR, MR3):** ≤0.1% IS — 3-log reduction; durability correlates with OS
- **MR4:** ≤0.01% IS (4-log reduction)
- **MR4.5:** ≤0.0032% IS (4.5-log reduction) — threshold for TFR attempt eligibility

## Function

### Normal BCR and ABL1 physiology

**Normal ABL1:**
- Non-receptor tyrosine kinase; regulated by N-terminal myristoyl cap folding into hydrophobic pocket → autoinhibition
- Functions in DNA damage response, cytoskeletal remodeling, cell migration
- Shuttles between nucleus (DNA repair) and cytoplasm (actin dynamics)

**Normal BCR:**
- BCR protein has RAS-GAP activity → normally attenuates RAS signaling
- In BCR-ABL, BCR contributes: coiled-coil dimerization (constitutive activation), pY177-GRB2 docking (RAS activation), but loses GAP function

**BCR-ABL constitutive activation:**
- Myristoyl cap cannot engage kinase → always active
- Coiled-coil dimerization → trans-autophosphorylation → further activation
- BCR-ABL is cytoplasmic (unlike nuclear ABL) → signal transduction bias

## Pathology

### Disease progression and blast crisis

**Mechanisms of progression to blast crisis:**
- Acquisition of additional cytogenetic abnormalities ("clonal evolution"): +8 (most common), i(17q), +Ph, +19
- Epigenetic silencing of differentiation factors (GATA2, C/EBPα)
- TP53 mutation, CDKN2A deletion, RUNX1 mutation
- BCR-ABL kinase domain mutation (conferring TKI resistance) + genetic instability from genomic crisis
- **Lymphoid BC:** Acquisition of IKZF1 deletions (Ikaros) → lymphoid blast crisis mimicking Ph+ ALL

**Leukemic stem cell (LSC) persistence:**
- Quiescent CD34+CD38- CML LSCs are relatively TKI-insensitive (not cycling → reduced dependence on BCR-ABL kinase)
- LSC persistence → molecular relapse upon TKI discontinuation in ~50% of patients
- LSC-targeting strategies: BCL-2 inhibitors (venetoclax), smoothened inhibitors (hedgehog pathway), combination immunotherapy — under investigation

### TKI resistance mechanisms

**Kinase domain mutations:**
- **T315I ("gatekeeper"):** Loss of imatinib/nilotinib/dasatinib/bosutinib contact threonine → resistance to all first/second-generation TKIs; requires ponatinib or asciminib (allosteric STAMP); frequency ~15-20% of resistant patients
- **F317L/V:** Dasatinib resistance; imatinib or nilotinib active
- **Y253H/E255K:** Nilotinib resistance; dasatinib active
- **F359V:** Nilotinib resistance; dasatinib active
- Compound mutations (e.g., T315I + V299L): ponatinib resistance; asciminib may retain activity

**BCR-ABL kinase-independent resistance:**
- SRC-family kinase overexpression (LYN amplification)
- Epigenetic silencing of drug transport (MDR1/ABCB1 upregulation, OCT1/SLC22A1 downregulation → reduced imatinib uptake)
- LSC quiescence (kinase-independent survival)

### Clinical presentations and complications

**Splenomegaly:** Result of extramedullary hematopoiesis in CML; can be massive (10-20 cm below costal margin); resolves with TKI; hydroxyurea used for cytoreduction prior to TKI initiation in symptomatic leukocytosis

**Leukostasis:** WBC >300,000/μL → slugging in microvasculature → pulmonary, cerebral ischemia; leukapheresis as bridge

**TKI-specific toxicities:**
- Imatinib: fluid retention, periorbital edema, myalgias, hepatotoxicity, QTc (rare); well-tolerated long-term
- Nilotinib: cardiovascular (PAD, AMI, stroke) — "off-target" PDGFR/c-KIT inhibition → metabolic syndrome risk; QTc prolongation; pancreatitis
- Dasatinib: pleural effusion (~20-35% cumulative), pulmonary arterial hypertension (rare, ~0.5%); platelet dysfunction; lymphocytosis (NK/T expansion → immune-mediated benefit in TFR)
- Ponatinib: arterial thrombosis (major concern); dose-optimization (45mg → 15mg after MR) reduces CV risk; pancreatitis; hypertension
- Asciminib: well-tolerated; hypertension; increased lipase; rare cardiovascular events

## Connections

- `connects-to` → **[ABL1](../../03-molecular/abl1/README.md)** — CML is caused by BCR-ABL fusion (t(9;22)); ABL1 kinase domain is the drug target; imatinib/dasatinib/nilotinib/bosutinib inhibit ABL1; T315I gatekeeper → ponatinib or asciminib (STAMP); MR4.5 molecular response enables treatment-free remission attempts.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — BCR-ABL constitutively phosphorylates STAT5 (and STAT3) → transcription of BCL-XL, MYC, and cyclin D1 → blast survival and proliferation; STAT5 activation is a dominant signaling output of BCR-ABL; TKI response correlates with STAT5 dephosphorylation.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — BCR-ABL → PI3K-AKT → mTORC1 → S6K and 4EBP1 → protein synthesis and survival; mTOR pathway activation mediates imatinib resistance in some CML clones; dual PI3K-mTOR inhibitors studied as combination with TKIs in BCR-ABL-positive blast crisis.
- `connects-to` → **[SRC kinase](../../03-molecular/src-kinase/README.md)** — BCR-ABL activates SRC-family kinases (LYN, HCK, FGR) in CML; SRC kinases promote blast crisis transformation and TKI resistance; dasatinib and bosutinib inhibit both ABL and SRC-family kinases — dual ABL/SRC inhibition relevant in lymphoid blast crisis.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — BCR-ABL → PI3K → AKT → mTOR → S6K/4EBP1 → protein synthesis and cell survival; AKT phosphorylates BAD → prevents apoptosis in CML cells; imatinib resistance associated with PI3K/AKT activation independent of BCR-ABL; AKT inhibition synergizes with TKIs in blast crisis CML.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — BCR-ABL → STAT5/NF-κB → MYC transcription → G1/S acceleration; MYC amplification is common in blast crisis transformation; MYC overexpression promotes self-renewal of CML LSCs; BRD4 inhibitors (JQ1) reduce MYC expression and overcome TKI resistance in CML blast crisis models.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — RB1 inactivated in CML blast crisis via CDK4/6 hyperactivation; E2F release drives myeloid or lymphoid blast transformation; BCR-ABL accelerates CDK2-mediated RB1 inactivation; palbociclib (CDK4/6 inhibitor) re-engages RB1 and sensitizes TKI-resistant blast crisis to apoptosis.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — CML is defined by uncontrolled expansion of the neutrophil lineage: BCR-ABL drives massive leukocytosis with granulocytes at all maturation stages and hallmark basophilia; unlike normal neutrophils they retain function early, so infection is not the initial problem.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — The CML marrow is markedly hypercellular with a high myeloid:erythroid ratio and 'dwarf' megakaryocytes; the Philadelphia chromosome t(9;22) is detected here, and marrow blast percentage defines chronic phase (<10%), accelerated (10-19%), and blast crisis (≥20%).
- `connects-to` → **[CLL](../cll/README.md)** — CLL and CML are the two chronic adult leukemias from opposite lineages: CLL is a B-lymphoid accumulation of mature CD5+ cells driven by BCR/BTK signaling, while CML is a myeloid proliferation driven by the BCR-ABL fusion kinase — different cells, drivers, and targeted drugs.
- `connects-to` → **[Myeloproliferative Neoplasms](../myeloproliferative-neoplasms/README.md)** — CML is the BCR-ABL1-positive classic myeloproliferative neoplasm: like PV, ET and myelofibrosis it is a clonal stem-cell overproduction of mature myeloid cells, but its Philadelphia chromosome and exquisite TKI sensitivity set it apart from the JAK2/CALR-driven MPNs.
- `connects-to` → **[AML](../aml/README.md)** — CML's natural history is progression to acute leukemia: untreated, the chronic phase accelerates into a blast crisis that behaves like acute leukemia—myeloid (AML-like) in ~70%, lymphoid in the rest—so TKI therapy aims to prevent this transformation, which remains hard to treat.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Splenomegaly is a hallmark of CML: massive extramedullary myeloid proliferation enlarges the spleen, causing early satiety and left-upper-quadrant pain at presentation; spleen size featured in old prognostic scores and shrinks rapidly once tyrosine-kinase inhibitors control it.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^druker-2006-iris-5year]: Druker BJ, Guilhot F, O'Brien SG, et al. Five-year follow-up of patients receiving imatinib for chronic myeloid leukemia. *N Engl J Med.* 2006;355(23):2408-2417. [doi:10.1056/NEJMoa062867](https://doi.org/10.1056/NEJMoa062867) · [PubMed 17151364](https://pubmed.ncbi.nlm.nih.gov/17151364/)
[^hochhaus-2019-dasatinib]: Hochhaus A, Saglio G, Hughes TP, et al. Long-term benefits and risks of frontline nilotinib vs imatinib for chronic myeloid leukemia in chronic phase: 5-year update of the randomized ENESTnd trial. *Leukemia.* 2016;30(5):1044-1054. [doi:10.1038/leu.2016.5](https://doi.org/10.1038/leu.2016.5) · [PubMed 26816503](https://pubmed.ncbi.nlm.nih.gov/26816503/)

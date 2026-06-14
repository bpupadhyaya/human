---
schema: human-scale-entry/v1
id: idh-mutant-glioma
name: IDH-Mutant Glioma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "IDH-mutant glioma (Grade 2-3) defined by IDH1/2 mutations; 2-HG → TET2 inhibition → G-CIMP hypermethylation; WHO 2021 separates astrocytoma (ATRX LOF) from oligodendroglioma (1p/19q codeletion); vorasidenib FDA-approved August 2024 (INDIGO trial); median OS ~10-15 years."
aliases: ["IDH-mutant glioma", "IDH glioma", "IDH mutant astrocytoma", "IDH mutant oligodendroglioma", "lower grade glioma", "LGG", "diffuse glioma IDH", "IDH1 glioma", "IDH1 R132H glioma", "Grade 2 glioma vorasidenib"]
sources:
  - id: mellinghoff-2023-vorasidenib-lgg
    type: peer-reviewed
    cite: "Mellinghoff IK, van den Bent MJ, Blumenthal DT, et al. Vorasidenib in IDH1- or IDH2-mutant low-grade glioma. N Engl J Med. 2023;389(7):589-601."
    doi: "10.1056/NEJMoa2304194"
    pmid: "37272530"
    url: "https://doi.org/10.1056/NEJMoa2304194"
  - id: jiao-2012-atrx-glioma
    type: peer-reviewed
    cite: "Jiao Y, Killela PJ, Reitman ZJ, et al. Frequent ATRX, CIC, FUBP1 and IDH mutations refine the classification of malignant gliomas. Oncotarget. 2012;3(7):709-722."
    doi: "10.18632/oncotarget.588"
    pmid: "22869205"
    url: "https://doi.org/10.18632/oncotarget.588"
cross_links:
  - target: 01-human/03-molecular/atrx
    relation: connects-to
    note: "ATRX LOF defines the astrocytoma lineage in IDH-mutant glioma (vs 1p/19q codeletion in oligodendroglioma); ~80% of IDH-mutant astrocytoma Grade 3/4 harbor ATRX LOF; ATRX LOF IHC (nuclear staining lost) used diagnostically; ATRX LOF + TP53 = canonical astrocytoma signature."
  - target: 01-human/03-molecular/idh1
    relation: connects-to
    note: "IDH1 R132H mutation (>90% of IDH-mutant gliomas) → 2-hydroxyglutarate → TET2/KDM inhibition → G-CIMP; vorasidenib (IDH1/2 inhibitor) FDA-approved August 2024 for IDH-mutant Grade 2 glioma (INDIGO trial: PFS HR 0.39); IDH1 IHC (anti-R132H) is the initial diagnostic test."
  - target: 01-human/03-molecular/tet2
    relation: connects-to
    note: "ATRX LOF + IDH1 → 2-HG → TET2 inhibition → DNA hypermethylation (G-CIMP); ATRX-DAXX deposits H3.3 at telomeric chromatin; ATRX LOF impairs H3.3 telomeric deposition → ALT mechanism → telomere lengthening independent of TERT; ATRX and TET2 cooperate in chromatin maintenance."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A homozygous deletion occurs in ~50-70% of IDH-mutant astrocytoma Grade 4; CDK4/6 hyperactivation → RB1 → E2F proliferation; CDKN2A deletion defines WHO Grade 4 IDH-mutant astrocytoma (from Grade 3); ATRX LOF + CDKN2A deletion → worst IDH-mutant glioma prognosis."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "IDH-mutant gliomas are diffuse, infiltrative brain tumors (astrocytoma favors frontal lobe, oligodendroglioma frontotemporal) that cannot be fully excised; maximal safe resection — often via awake craniotomy with cortical mapping — improves PFS and delays transformation."
  - target: 01-human/07-system/glioblastoma
    relation: connects-to
    note: "IDH status is the great divide in adult diffuse glioma: IDH-mutant tumors run a far more indolent course (median OS ~10-15 years) than IDH-wildtype glioblastoma (~15 months); WHO 2021 reserves the name 'glioblastoma' for IDH-wildtype tumors only."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "IDH-mutant astrocytoma is the glial-lineage arm of the family (ATRX LOF + TP53, 1p/19q intact), as opposed to oligodendroglioma; IDH mutation creates a neural-progenitor-like epigenetic state (G-CIMP) that blocks normal astrocytic differentiation."
  - target: 01-human/07-system/medulloblastoma
    relation: connects-to
    note: "IDH-mutant glioma and medulloblastoma are both molecularly classified brain tumors at opposite poles: IDH-mutant glioma is a slow, diffuse hemispheric tumor of adults driven by 2-HG epigenetics, while medulloblastoma is a fast embryonal cerebellar tumor of children (SHH/WNT/MYC)."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "IDH-mutant glioma and IDH-mutant AML share the same driver: IDH1/2 mutation produces 2-hydroxyglutarate that blocks TET/KDM demethylases, hypermethylating DNA and blocking differentiation; the same drugs cross over — ivosidenib (IDH1) and enasidenib treat both glioma and AML."
  - target: 01-human/07-system/cholangiocarcinoma
    relation: connects-to
    note: "IDH-mutant glioma and cholangiocarcinoma are distant cancers united by IDH1 mutation and 2-HG: ~15-20% of intrahepatic CCA carries IDH1 R132, and ivosidenib — first approved in IDH1-mutant AML — is now used in both IDH1-mutant cholangiocarcinoma and grade 2 IDH-mutant glioma."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "Oligodendroglioma is the IDH-mutant glioma defined by oligodendrocyte-like cells: IDH mutation plus 1p/19q codeletion marks this tumor, whose round 'fried-egg' cells resemble oligodendrocytes and whose codeletion predicts good PCV-chemo response and long survival."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Seizures are the commonest presentation of IDH-mutant glioma: these slow-growing, cortically-based tumors irritate neurons—partly via the oncometabolite 2-hydroxyglutarate altering glutamate—so new focal epilepsy in a young adult often first reveals the glioma."
  - target: 01-human/07-system/diffuse-midline-glioma
    relation: connects-to
    note: "IDH-mutant glioma and diffuse midline glioma sit at opposite ends of glioma biology: both are diffuse gliomas defined by a single metabolic/epigenetic driver, but IDH-mutant gliomas (adults, better prognosis) contrast with H3 K27M DMG (children, dismal prognosis)."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photon radiotherapy is standard for IDH-mutant glioma: after maximal resection, radiation plus PCV or temozolomide markedly extends survival in these slower-growing gliomas, and the new IDH inhibitor vorasidenib can now delay when radiation is needed."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "IDH-mutant glioma and Li-Fraumeni intersect at p53: many IDH-mutant astrocytomas carry TP53 mutations, and germline TP53 loss in Li-Fraumeni predisposes to gliomas in young adults—so the metabolic IDH lesion and loss of the genome's guardian often co-occur in one tumor."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "IDH-mutant gliomas integrate into neural circuits: their tumor cells form functional synapses with neurons, and the seizures these gliomas commonly cause reflect this electrical coupling—so neuronal activity both signals and may feed the slow-growing tumor."
  - target: 01-human/03-molecular/idh2
    relation: connects-to
    note: "IDH2 mutation is the rarer twin of IDH1 in glioma: both produce the oncometabolite 2-hydroxyglutarate that reprograms the epigenome, so IDH2 defines the same favorable-prognosis glioma class and is targetable by the same IDH inhibitors as IDH1."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 and ATRX mutation define the astrocytoma arm of IDH-mutant glioma: when an IDH-mutant tumor also loses p53 and ATRX it is an astrocytoma, whereas 1p/19q-codeleted TERT-mutant tumors are oligodendrogliomas—so p53 status splits the two IDH-glioma lineages."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "TERT promoter mutation marks the oligodendroglioma arm of IDH-mutant glioma: combined with 1p/19q codeletion it defines oligodendroglioma, the most treatment-responsive glioma—so TERT status, opposite TP53/ATRX, separates the two IDH-mutant subtypes."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Proton therapy suits IDH-mutant glioma's long survivors: because these lower-grade gliomas strike younger patients who live many years, protons' reduced dose to surrounding brain helps limit late cognitive and endocrine toxicity from radiation."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "IDH-mutant glioma is built on a carbon-metabolism quirk: the mutant enzyme converts a Krebs-cycle intermediate into the carbon oncometabolite 2-hydroxyglutarate, which reprograms DNA and histone methylation to drive these gliomas—and is now a drug target."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "IDH-mutant gliomas are the more indolent diffuse tumors of the nervous system: they infiltrate the brain like glioblastoma but, being IDH-mutant, grow slower and respond better to treatment—so molecular status, not just appearance, predicts the course."
  - target: 01-human/07-system/hlrcc
    relation: connects-to
    note: "IDH-mutant glioma and HLRCC are sibling oncometabolite cancers: IDH mutation makes 2-hydroxyglutarate while FH loss makes fumarate, and both metabolites block the same dioxygenases to rewire epigenetics—so distinct enzymes converge on one cancer mechanism."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "IDH-mutant glioma is a vaccine target for T cells: the shared IDH1-R132H mutation creates a public neoantigen, and a peptide vaccine has induced cytotoxic T-cell responses against it—an early step toward immunotherapy for these gliomas."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "IDH-mutant gliomas drive seizures through glutamate: the 2-HG oncometabolite resembles glutamate and the tumor disturbs glutamate balance, so epilepsy is an early, common presenting symptom—seizure control is part of routine care."
---

# IDH-Mutant Glioma

## Overview

**IDH-mutant glioma** encompasses a family of diffuse glial brain tumors defined by somatic mutations in **IDH1** (most commonly R132H, >90%) or **IDH2** (R172K/M, ~5-8%). These mutations convert α-ketoglutarate to **2-hydroxyglutarate (2-HG)**, an oncometabolite that competitively inhibits α-KG-dependent dioxygenases including **TET2** (DNA demethylase) and histone KDMs → DNA hypermethylation (G-CIMP) → epigenetic silencing of tumor suppressor loci. Under the **WHO 2021 CNS tumor classification**, IDH-mutant diffuse gliomas are divided into two lineages by molecular markers: **astrocytoma** (ATRX LOF + TP53 mutation, 1p/19q intact) and **oligodendroglioma** (1p/19q codeletion + TERT promoter mutation, ATRX intact). IDH-mutant gliomas have a markedly better prognosis than IDH-wildtype glioblastoma (median OS ~10-15 years for Grade 2 vs ~15 months for GBM). **Vorasidenib**, a brain-penetrant IDH1/2 inhibitor, was FDA-approved in August 2024 for Grade 2 IDH-mutant glioma following the INDIGO trial [^mellinghoff-2023-vorasidenib-lgg] [^jiao-2012-atrx-glioma].

**Epidemiology:**
- Incidence: ~5,000-6,000 IDH-mutant glioma cases/year USA (~Grade 2: 2,500-3,000; Grade 3: 2,000; Grade 4 IDH-mutant astrocytoma: ~500-700)
- Median age: Grade 2 ~35-40 years; Grade 3 ~40-50 years; Grade 4 IDH-mutant astrocytoma ~45-55 years (significantly younger than IDH-wildtype GBM, median age ~64 years)
- IDH1 R132H: ~90% of IDH-mutant gliomas; IDH1 non-R132H variants: ~3-5%; IDH2 mutations: ~5-8%; exclusively IDH2 in some Grade 3 oligodendrogliomas
- Geographic distribution: no significant ethnic variation; incidence ~5 per 100,000 for all diffuse gliomas combined

**IDH-mutant glioma molecular subtypes (WHO 2021):**

| Feature | IDH-mutant Astrocytoma | IDH-mutant Oligodendroglioma |
|---|---|---|
| ATRX | LOST (LOF) | INTACT |
| 1p/19q | Intact | Codeleted |
| TP53 | Mutated (~80%) | Usually wildtype |
| TERT promoter | Rare | Mutated (~90%) |
| Grade range | 2, 3, 4 | 2, 3 |
| CDKN2A deletion | Grade 4 defining | Rare |
| Median OS (Grade 2) | ~12-15 yrs | ~15-18 yrs |
| Chemotherapy | PCV or TMZ | PCV preferred |

## Structure

### 2-HG oncometabolite mechanism

**IDH1/2 neomorphic activity:**
Normal IDH1 (cytoplasm) and IDH2 (mitochondria): oxidative decarboxylation of isocitrate → α-ketoglutarate + CO2 + NADPH; oncogenic IDH1/2: gain-of-function neomorphic activity → uses NADPH to reduce α-ketoglutarate → 2-hydroxyglutarate (2-HG); 2-HG accumulates to millimolar concentrations in IDH-mutant gliomas; 2-HG can be measured by MR spectroscopy (non-invasive) or HPLC/mass spec (tissue)

**2-HG targets:**
- **TET2** (5-methylcytosine dioxygenase): converts 5mC → 5hmC → active DNA demethylation; 2-HG competitively inhibits TET2 at the α-KG cofactor site → DNA hypermethylation → G-CIMP (glioma CpG island methylator phenotype) → silencing of MGMT (promoter methylated in ~85% IDH-mutant gliomas), CDKN2A, and other TSGs
- **KDMs** (histone lysine demethylases, KDM4A, KDM5C, KDM6A): α-KG-dependent demethylases; 2-HG inhibition → histone hypermethylation (H3K9me3, H3K27me3, H3K36me3); epigenetic silencing beyond DNA methylation
- **ALKBH** enzymes: DNA/RNA demethylases; 2-HG inhibition → elevated N6-methyladenosine (m6A) in RNA → altered mRNA stability

**G-CIMP:**
G-CIMP (glioma CpG island methylator phenotype): concerted hypermethylation of >1000 CpG island promoters in IDH-mutant gliomas; G-CIMP is pathognomonic for IDH-mutant diffuse gliomas; includes MGMT (predictive of alkylating agent sensitivity), CDKN2A, RASSF1A, and other TSGs; G-CIMP can be measured by methylation arrays (450K/EPIC); DNA methylation profiling is now part of integrated WHO 2021 diagnosis

### MGMT promoter methylation

**MGMT in IDH-mutant glioma:**
MGMT (O6-methylguanine-DNA methyltransferase) repairs O6-methylguanine adducts created by alkylating agents (temozolomide); MGMT promoter methylated in ~85% of IDH-mutant Grade 2-3 gliomas (downstream of G-CIMP) → MGMT protein absent → alkylating agent DNA damage not repaired → tumor cell death; MGMT methylation predicts temozolomide benefit; unmethylated MGMT (rare in IDH-mutant glioma) associated with alkylating agent resistance

## Function

### Molecular consequences of IDH mutation

**Epigenetic reprogramming:**
IDH mutation is an early (possibly initiating) event in gliomagenesis: IDH1 R132H creates the G-CIMP state → neural progenitor-like epigenetic landscape → blocked differentiation; IDH mutation precedes ATRX LOF and TP53 in the evolutionary sequence of astrocytoma; IDH mutation is the defining event from which astrocytoma and oligodendroglioma diverge (ATRX vs 1p/19q)

**Metabolic consequences:**
2-HG accumulation → NADPH consumption (reversal of normal IDH reaction) → oxidative stress; IDH-mutant glioma cells are more vulnerable to oxidative stress than IDH-wildtype; IDH mutant cells show impaired glutamine metabolism; 2-HG acts as an HIF prolyl hydroxylase activator → pseudonormoxic signaling; IDH-mutant tumor microenvironment is relatively immunosuppressed

**Immune evasion:**
IDH-mutant gliomas are immunologically "cold": low TMB (IDH-mutant gliomas have low mutation burden, ~1-2 mut/Mb), low PD-L1 expression; G-CIMP suppresses inflammatory gene expression including cytokine signaling; 2-HG is directly immunosuppressive: inhibits T cell proliferation and NK cell activity at physiological 2-HG concentrations; immunotherapy (pembrolizumab, bevacizumab + pembrolizumab) has not shown significant benefit in IDH-mutant glioma trials

## Pathology

### Diagnosis and grading

**WHO 2021 CNS Grade system:**
IDH-mutant astrocytoma:
- **Grade 2**: IDH-mutant + ATRX LOF + TP53 mutation + no CDKN2A deletion + no necrosis/microvascular proliferation; most favorable; 10-year OS ~70-80%
- **Grade 3**: above + anaplasia (increased mitoses, cellularity); some CDKN2A deletion; 10-year OS ~50-60%
- **Grade 4**: IDH-mutant astrocytoma with CDKN2A homozygous deletion AND/OR necrosis+microvascular proliferation; no EGFR amp, no TERT mutation; 10-year OS ~30-40%

IDH-mutant oligodendroglioma:
- **Grade 2**: IDH-mutant + 1p/19q codeleted + TERT promoter mutation; ATRX intact; 10-year OS ~80-90%
- **Grade 3**: above + anaplastic features; 10-year OS ~65-75%
- Note: no Grade 4 in oligodendroglioma (1p/19q codeletion blocks GBM-like progression)

**Diagnostic workup:**
1. MRI brain: IDH-mutant glioma: T2/FLAIR hyperintense cortical/subcortical infiltrative mass, minimal enhancement (Grade 2-3); frontal lobe predilection (astrocytoma), frontotemporal (oligodendroglioma)
2. IDH1 R132H IHC (anti-IDH1 R132H clone H09): positive in ~90% IDH-mutant; negative → IDH1/2 sequencing
3. ATRX IHC: lost = astrocytoma lineage; intact = oligodendroglioma lineage
4. FISH: 1p/19q codeletion (oligodendroglioma) vs intact (astrocytoma)
5. TERT promoter sequencing (C228T, C250T): mutated in ~90% oligodendroglioma
6. CDKN2A FISH or CNV array: homozygous deletion = WHO Grade 4 astrocytoma
7. DNA methylation profiling (EPIC array): G-CIMP confirmation; classifier at molecularneuropathology.org for CNS tumor subtype

### Standard treatment

**Surgery:**
Maximum safe resection is first-line for newly diagnosed IDH-mutant glioma; gross total resection associated with PFS benefit; eloquent cortex involvement limits resection; awake craniotomy for language/motor mapping; extent of resection correlates with OS and time to malignant transformation in Grade 2

**Radiation:**
- Grade 2: RT 50.4-54 Gy in 1.8 Gy fractions; delayed RT vs immediate RT (RTOG 9802, EORTC 22845): no OS difference; immediate RT improves PFS by ~3 years
- Grade 3: RT 60 Gy + PCV or TMZ; CATNON trial: RT + TMZ (concurrent + adjuvant) improved OS in IDH-mutant Grade 3 (5-yr OS 55% vs 44%)
- Grade 4: 60 Gy + TMZ (Stupp protocol, adapted); CDKN2A-deleted Grade 4 IDH-mutant has similar treatment as GBM

**Chemotherapy:**
- **PCV** (procarbazine + CCNU/lomustine + vincristine): Phase 3 RTOG 9802 (Grade 2 with RF): RT + PCV improved 10-yr OS (60% vs 40%) and PFS (10.4 yr vs 4.0 yr); PCV preferred for oligodendroglioma (1p/19q codeleted)
- **Temozolomide (TMZ)**: alkylating agent; MGMT methylated (~85% IDH-mutant) → high sensitivity; oral daily 75 mg/m² concurrent + adjuvant 150-200 mg/m² ×5d/28d ×12 cycles; CATNON Phase 3 (IDH-mutant Grade 3): RT + adjuvant TMZ improved OS

**Vorasidenib (FDA-approved August 2024):** [^mellinghoff-2023-vorasidenib-lgg]
- Mechanism: brain-penetrant, dual IDH1/2 inhibitor; 40 mg oral once daily; suppresses 2-HG production → reverses epigenetic reprogramming (partial); crosses blood-brain barrier (Kp,uu ~0.6 for mouse brain)
- INDIGO Phase 3 trial (N=331 Grade 2 IDH-mutant glioma after surgery): vorasidenib vs placebo; primary endpoint PFS; vorasidenib median PFS 27.7 months vs 11.1 months (HR 0.39, p<0.001); time to next intervention HR 0.26; OS data immature at primary analysis
- Eligibility: residual/recurrent Grade 2 IDH-mutant (IDH1/2) glioma; after at least one prior surgery; no prior RT or chemo required (RT/chemo-naive population)
- FDA indication (August 2024): adults with residual or recurrent Grade 2 IDH1- or IDH2-mutant glioma
- Toxicity: transaminase elevation (Gr3: ~10%), grade 1-2 nausea/fatigue; liver function monitoring required
- Note: not yet studied in Grade 3-4 IDH-mutant glioma; trials ongoing

**Olutasidenib (IDH1 inhibitor):**
Olutasidenib 150 mg BID: FDA-approved October 2022 for IDH1-mutant AML (relapsed/refractory); not approved for glioma; Phase 2 glioma study ongoing; less brain-penetrant than vorasidenib; ORR ~35% in IDH1-mutant AML

**MGMT-based temozolomide sensitivity:**
IDH-mutant glioma with MGMT methylation shows strong alkylating agent sensitivity; TMZ + RT remains standard for Grade 3-4; MGMT unmethylated IDH-mutant glioma: PCV may be preferred (not dependent on MGMT for efficacy — different mechanism via inter-strand cross-links)

### Recurrent disease

**Patterns of progression:**
- Grade 2 → Grade 3 transformation: ~30-40% over 5-10 years; acquisition of CDKN2A deletion, EGFR, or other alterations
- Grade 3 → Grade 4 transformation: additional molecular events
- Malignant transformation (MT): when IDH-mutant glioma acquires GBM-like features (necrosis, MGMT loss, EGFR amplification); MT associated with dismal prognosis; re-biopsy important to confirm

**Salvage options at recurrence:**
- Rechallenge with TMZ or lomustine (if MGMT methylated)
- Bevacizumab: ORR ~25-30% radiographic response in recurrent glioma; FDA-approved for GBM; used off-label in IDH-mutant glioma recurrence
- Clinical trials: CDK4/6 inhibitors (palbociclib for CDKN2A-deleted Grade 4), ONC201 (H3K27M-negative IDH-mutant; exploratory), mTOR inhibitors, immunotherapy (pembrolizumab)
- Vorasidenib continuation after RT/chemo: INDIGO 2 trial design ongoing

**Prognosis by molecular subtype:**
- IDH-mutant oligodendroglioma Grade 2: median OS ~18-20 years; best among gliomas
- IDH-mutant astrocytoma Grade 2: median OS ~12-15 years
- IDH-mutant astrocytoma Grade 3: median OS ~7-9 years
- IDH-mutant astrocytoma Grade 4 (CDKN2A-deleted): median OS ~3-5 years (significantly worse than Grade 3 but better than IDH-wildtype GBM)

## Connections

- `connects-to` → **[ATRX](../../03-molecular/atrx/README.md)** — ATRX LOF defines the astrocytoma lineage in IDH-mutant glioma (vs 1p/19q codeletion in oligodendroglioma); ~80% of IDH-mutant astrocytoma Grade 3/4 harbor ATRX LOF; ATRX LOF IHC (nuclear staining lost) used diagnostically; ATRX LOF + TP53 = canonical astrocytoma signature.
- `connects-to` → **[IDH1](../../03-molecular/idh1/README.md)** — IDH1 R132H mutation (>90% of IDH-mutant gliomas) → 2-hydroxyglutarate → TET2/KDM inhibition → G-CIMP; vorasidenib (IDH1/2 inhibitor) FDA-approved August 2024 for IDH-mutant Grade 2 glioma (INDIGO trial: PFS HR 0.39); IDH1 IHC (anti-R132H) is the initial diagnostic test.
- `connects-to` → **[TET2](../../03-molecular/tet2/README.md)** — ATRX LOF + IDH1 → 2-HG → TET2 inhibition → DNA hypermethylation (G-CIMP); ATRX-DAXX deposits H3.3 at telomeric chromatin; ATRX LOF impairs H3.3 telomeric deposition → ALT mechanism → telomere lengthening independent of TERT; ATRX and TET2 cooperate in chromatin maintenance.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A homozygous deletion occurs in ~50-70% of IDH-mutant astrocytoma Grade 4; CDK4/6 hyperactivation → RB1 → E2F proliferation; CDKN2A deletion defines WHO Grade 4 IDH-mutant astrocytoma (from Grade 3); ATRX LOF + CDKN2A deletion → worst IDH-mutant glioma prognosis.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — IDH-mutant gliomas are diffuse, infiltrative brain tumors (astrocytoma favors frontal lobe, oligodendroglioma frontotemporal) that cannot be fully excised; maximal safe resection — often via awake craniotomy with cortical mapping — improves PFS and delays transformation.
- `connects-to` → **[Glioblastoma](../glioblastoma/README.md)** — IDH status is the great divide in adult diffuse glioma: IDH-mutant tumors run a far more indolent course (median OS ~10-15 years) than IDH-wildtype glioblastoma (~15 months); WHO 2021 reserves the name 'glioblastoma' for IDH-wildtype tumors only.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — IDH-mutant astrocytoma is the glial-lineage arm of the family (ATRX LOF + TP53, 1p/19q intact), as opposed to oligodendroglioma; IDH mutation creates a neural-progenitor-like epigenetic state (G-CIMP) that blocks normal astrocytic differentiation.
- `connects-to` → **[Medulloblastoma](../medulloblastoma/README.md)** — IDH-mutant glioma and medulloblastoma are both molecularly classified brain tumors at opposite poles: IDH-mutant glioma is a slow, diffuse hemispheric tumor of adults driven by 2-HG epigenetics, while medulloblastoma is a fast embryonal cerebellar tumor of children (SHH/WNT/MYC).
- `connects-to` → **[AML](../aml/README.md)** — IDH-mutant glioma and IDH-mutant AML share the same driver: IDH1/2 mutation produces 2-hydroxyglutarate that blocks TET/KDM demethylases, hypermethylating DNA and blocking differentiation; the same drugs cross over — ivosidenib (IDH1) and enasidenib treat both glioma and AML.
- `connects-to` → **[Cholangiocarcinoma](../cholangiocarcinoma/README.md)** — IDH-mutant glioma and cholangiocarcinoma are distant cancers united by IDH1 mutation and 2-HG: ~15-20% of intrahepatic CCA carries IDH1 R132, and ivosidenib — first approved in IDH1-mutant AML — is now used in both IDH1-mutant cholangiocarcinoma and grade 2 IDH-mutant glioma.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — Oligodendroglioma is the IDH-mutant glioma defined by oligodendrocyte-like cells: IDH mutation plus 1p/19q codeletion marks this tumor, whose round 'fried-egg' cells resemble oligodendrocytes and whose codeletion predicts good PCV-chemo response and long survival.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Seizures are the commonest presentation of IDH-mutant glioma: these slow-growing, cortically-based tumors irritate neurons—partly via the oncometabolite 2-hydroxyglutarate altering glutamate—so new focal epilepsy in a young adult often first reveals the glioma.
- `connects-to` → **[Diffuse Midline Glioma](../diffuse-midline-glioma/README.md)** — IDH-mutant glioma and diffuse midline glioma sit at opposite ends of glioma biology: both are diffuse gliomas defined by a single metabolic/epigenetic driver, but IDH-mutant gliomas (adults, better prognosis) contrast with H3 K27M DMG (children, dismal prognosis).
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photon radiotherapy is standard for IDH-mutant glioma: after maximal resection, radiation plus PCV or temozolomide markedly extends survival in these slower-growing gliomas, and the new IDH inhibitor vorasidenib can now delay when radiation is needed.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — IDH-mutant glioma and Li-Fraumeni intersect at p53: many IDH-mutant astrocytomas carry TP53 mutations, and germline TP53 loss in Li-Fraumeni predisposes to gliomas in young adults—so the metabolic IDH lesion and loss of the genome's guardian often co-occur in one tumor.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — IDH-mutant gliomas integrate into neural circuits: their tumor cells form functional synapses with neurons, and the seizures these gliomas commonly cause reflect this electrical coupling—so neuronal activity both signals and may feed the slow-growing tumor.
- `connects-to` → **[IDH2](../../03-molecular/idh2/README.md)** — IDH2 mutation is the rarer twin of IDH1 in glioma: both produce the oncometabolite 2-hydroxyglutarate that reprograms the epigenome, so IDH2 defines the same favorable-prognosis glioma class and is targetable by the same IDH inhibitors as IDH1.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 and ATRX mutation define the astrocytoma arm of IDH-mutant glioma: when an IDH-mutant tumor also loses p53 and ATRX it is an astrocytoma, whereas 1p/19q-codeleted TERT-mutant tumors are oligodendrogliomas—so p53 status splits the two IDH-glioma lineages.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — TERT promoter mutation marks the oligodendroglioma arm of IDH-mutant glioma: combined with 1p/19q codeletion it defines oligodendroglioma, the most treatment-responsive glioma—so TERT status, opposite TP53/ATRX, separates the two IDH-mutant subtypes.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Proton therapy suits IDH-mutant glioma's long survivors: because these lower-grade gliomas strike younger patients who live many years, protons' reduced dose to surrounding brain helps limit late cognitive and endocrine toxicity from radiation.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — IDH-mutant glioma is built on a carbon-metabolism quirk: the mutant enzyme converts a Krebs-cycle intermediate into the carbon oncometabolite 2-hydroxyglutarate, which reprograms DNA and histone methylation to drive these gliomas—and is now a drug target.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — IDH-mutant gliomas are the more indolent diffuse tumors of the nervous system: they infiltrate the brain like glioblastoma but, being IDH-mutant, grow slower and respond better to treatment—so molecular status, not just appearance, predicts the course.
- `connects-to` → **[Hereditary Leiomyomatosis and Renal Cell Carcinoma](../hlrcc/README.md)** — IDH-mutant glioma and HLRCC are sibling oncometabolite cancers: IDH mutation makes 2-hydroxyglutarate while FH loss makes fumarate, and both metabolites block the same dioxygenases to rewire epigenetics—so distinct enzymes converge on one cancer mechanism.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — IDH-mutant glioma is a vaccine target for T cells: the shared IDH1-R132H mutation creates a public neoantigen, and a peptide vaccine has induced cytotoxic T-cell responses against it—an early step toward immunotherapy for these gliomas.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — IDH-mutant gliomas drive seizures through glutamate: the 2-HG oncometabolite resembles glutamate and the tumor disturbs glutamate balance, so epilepsy is an early, common presenting symptom—seizure control is part of routine care.

[^mellinghoff-2023-vorasidenib-lgg]: Mellinghoff IK, van den Bent MJ, Blumenthal DT, et al. Vorasidenib in IDH1- or IDH2-mutant low-grade glioma. *N Engl J Med.* 2023;389(7):589-601. [doi:10.1056/NEJMoa2304194](https://doi.org/10.1056/NEJMoa2304194) · [PubMed 37272530](https://pubmed.ncbi.nlm.nih.gov/37272530/)
[^jiao-2012-atrx-glioma]: Jiao Y, Killela PJ, Reitman ZJ, et al. Frequent ATRX, CIC, FUBP1 and IDH mutations refine the classification of malignant gliomas. *Oncotarget.* 2012;3(7):709-722. [doi:10.18632/oncotarget.588](https://doi.org/10.18632/oncotarget.588) · [PubMed 22869205](https://pubmed.ncbi.nlm.nih.gov/22869205/)

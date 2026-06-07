---
schema: human-scale-entry/v1
id: alzheimers-disease
name: Alzheimer's Disease
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Neurodegenerative disease defined by amyloid-β plaques and tau tangles; progressive memory loss and dementia. APOE4 is the major genetic risk factor. Anti-amyloid antibodies (lecanemab, donanemab) slow early-stage progression; symptomatic treatment with cholinesterase inhibitors."
aliases: ["AD", "Alzheimer disease", "senile dementia", "LOAD", "late-onset Alzheimer's"]
sources:
  - id: selkoe-2016-alzheimer
    type: peer-reviewed
    cite: "Selkoe DJ, Hardy J. The amyloid hypothesis of Alzheimer's disease at 25 years. EMBO Mol Med. 2016;8(6):595-608."
    doi: "10.15252/emmm.201606210"
    pmid: "27025652"
    url: "https://doi.org/10.15252/emmm.201606210"
  - id: jack-2018-nia-aa
    type: peer-reviewed
    cite: "Jack CR Jr, Bennett DA, Blennow K, et al. NIA-AA Research Framework: Toward a biological definition of Alzheimer's disease. Alzheimers Dement. 2018;14(4):535-562."
    doi: "10.1016/j.jalz.2018.02.018"
    pmid: "29653606"
    url: "https://doi.org/10.1016/j.jalz.2018.02.018"
  - id: van-dyck-2023-lecanemab
    type: peer-reviewed
    cite: "van Dyck CH, Swanson CJ, Aisen P, et al. Lecanemab in Early Alzheimer's Disease. N Engl J Med. 2023;388(1):9-21."
    doi: "10.1056/NEJMoa2212948"
    pmid: "36449413"
    url: "https://doi.org/10.1056/NEJMoa2212948"
cross_links:
  - target: 01-human/06-organ/brain
    relation: targets
    note: "Alzheimer's atrophies hippocampus and entorhinal cortex first (tau Braak staging I-IV), spreading to association cortex; Aβ plaques and tau tangles disrupt synaptic transmission, activate microglia, and drive progressive neuronal death from medial temporal outward."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Disease-associated microglia (DAM) upregulate TREM2 and ApoE → phagocytose Aβ plaques; sustained activation → NLRP3 inflammasome → IL-1β/IL-18 → neuroinflammation and tau spread; TREM2 R47H variant is a major AD risk factor with 2-3× elevated risk."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Aβ fibrils activate NLRP3 inflammasome in microglia → caspase-1 → IL-1β and pyroptosis → neuroinflammation and tau phosphorylation; NLRP3 inhibition (MCC950) reduces tau pathology and cognitive decline in AD mouse models."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy clears APP fragments and aggregated tau; autophagic flux declines in aging and AD; rapamycin-induced autophagy reduces plaques and tangles in mouse models; lysosomal dysfunction (impaired v-ATPase, cathepsins) is a primary AD pathomechanism."
  - target: 01-human/03-molecular/apoe
    relation: connects-to
    note: "APOE4 (frequency ~15%) confers 3-4x heterozygous and 8-12x homozygous risk for late-onset AD; APOE4 impairs microglial Aβ phagocytosis, promotes Aβ aggregation, and worsens tau pathology; APOE4 homozygotes develop AD ~10 years earlier than APOE3 carriers."
---

# Alzheimer's Disease

## Overview

**Alzheimer's disease (AD)** is the most common cause of dementia — a progressive, ultimately fatal neurodegenerative disorder characterized by the pathological accumulation of **amyloid-β (Aβ) plaques** (extracellular) and **tau neurofibrillary tangles (NFTs)** (intraneuronal) in the cerebral cortex and hippocampus, leading to synaptic dysfunction, neuroinflammation, neuronal death, and cognitive decline [^selkoe-2016-alzheimer].

AD is the **sixth leading cause of death in the United States** (~6.9 million Americans, 2024; ~50 million worldwide) and the most expensive disease in terms of societal cost. Absent prevention or cure, prevalence is projected to triple by 2050 as the global population ages.

**Classification:**
- **Late-onset AD (LOAD, >65 years):** ~95% of cases; complex polygenic with APOE4 as the major risk allele; likely decades of preclinical amyloid accumulation before symptom onset
- **Early-onset AD (EOAD, <65 years):** ~5%; often familial (FAD) with autosomal dominant mutations in APP (amyloid precursor protein), PSEN1 (presenilin-1), or PSEN2 (presenilin-2) → constitutively elevated Aβ42 production

**The amyloid cascade hypothesis** (Hardy and Higgins, 1992; Selkoe and Hardy, 2016): Aβ42 overproduction or underclearing → Aβ aggregation → oligomers (toxic) → plaques (less toxic, more stable) → neuroinflammation → tau hyperphosphorylation and tangle formation → synapse loss → neurodegeneration → dementia [^selkoe-2016-alzheimer]. While this remains the dominant framework, debate continues about relative pathogenic contribution of Aβ vs. tau vs. neuroinflammation.

**Biological definition (NIA-AA A/T/(N) Framework, 2018):** AD defined by biomarkers [^jack-2018-nia-aa]:
- **A (amyloid):** Positive CSF Aβ42, or amyloid PET (florbetapir, florbetaben) — marks amyloid pathology
- **T (tau):** Positive CSF phospho-tau181, or tau PET (flortaucipir) — marks tau pathology
- **(N) (neurodegeneration):** CSF total tau, FDG-PET, brain MRI atrophy — marks neurodegeneration

## Structure

### Amyloid-β: production and aggregation [^selkoe-2016-alzheimer]

**Amyloid precursor protein (APP, 695-770 aa depending on isoform):**
- Type I transmembrane glycoprotein; expressed in neurons, synapses
- **Non-amyloidogenic pathway (normal):** α-secretase (ADAM10/ADAM17) cleaves within Aβ domain → sAPPα (soluble, neuroprotective) + C83 → γ-secretase → p3 peptide (harmless)
- **Amyloidogenic pathway (AD):** β-secretase (BACE1) cleaves APP → sAPPβ + C99 → γ-secretase (PSEN1/PSEN2 complex) → Aβ40 (more common, less pathogenic) and **Aβ42** (minority, more hydrophobic → aggregation-prone → toxic)

**Aβ aggregation cascade:**
1. Aβ42 monomers → soluble oligomers (dimers to ~50-mers) — **most neurotoxic form** (impair LTP, cause synaptic dysfunction)
2. Oligomers → protofibrils → insoluble fibrillar plaques (neuritic/senile plaques) — detectable by PET, less acutely toxic but markers of disease
3. Plaques → activate microglia and astrocytes → neuroinflammation → amplify Aβ production and tau phosphorylation

**Key genetic determinants of Aβ:**
- **APP duplication (Down syndrome/trisomy 21):** 3 copies of APP → 1.5× Aβ production → essentially universal early-onset AD by age 50-60
- **APP mutations (familial AD):** V717I (London), K670N/M671L (Swedish) → elevated Aβ42/40 ratio
- **PSEN1 mutations:** >300 known pathogenic mutations → altered γ-secretase cleavage → elevated Aβ42/40; most aggressive FAD

### Tau pathology

**Tau (MAPT gene):** Microtubule-associated protein; 6 isoforms in adult human brain (3R and 4R); normally stabilizes axonal microtubules and facilitates axonal transport.

**Hyperphosphorylation in AD:**
- Aβ oligomers → activate CDK5/p25, GSK-3β → tau hyperphosphorylation at Ser202, Thr205, Ser396, Ser404 → tau detaches from microtubules → axonal transport failure → tau aggregates into paired helical filaments (PHFs) → neurofibrillary tangles (NFTs)
- Prion-like spreading: tau aggregates released from degenerating neurons → internalized by connected neurons → seed new NFTs → Braak staging (I-VI, hippocampus → association cortex → primary cortex)

**Braak staging:** Anatomical progression of NFT spreading from entorhinal cortex (I-II) → hippocampus/amygdala (III-IV) → isocortex (V-VI); correlates better with symptom severity than amyloid burden.

## Function

### Clinical progression

**Preclinical AD:** Normal cognition; amyloid PET positive; Aβ42 in CSF low; no symptoms; may persist 10-15 years

**Mild cognitive impairment (MCI) due to AD:** Objective memory impairment (especially episodic memory — recent events) with preserved functional independence; positive amyloid biomarker; ~15% per year convert to AD dementia; target stage for anti-amyloid therapy

**AD dementia:**
- **Mild:** Memory loss affecting daily function; language, orientation, visuospatial deficits emerging; MMSE 18-24
- **Moderate:** Severe memory loss; unable to recognize family; behavioral disturbances (agitation, psychosis, wandering); requires assistance with ADLs; MMSE 10-17
- **Severe:** Bed-bound; complete ADL dependence; dysphagia → aspiration pneumonia (leading cause of death); MMSE <10

### Neuroinflammation and TREM2

Microglia play a central, dual role in AD:
- **Protective:** Disease-associated microglia (DAM) — upregulate TREM2 (triggering receptor expressed on myeloid cells 2), ApoE, and phagocytic genes → clear Aβ plaques and apoptotic neurons
- **Pathological:** Sustained activation → NLRP3 inflammasome → IL-1β, IL-18 → neuroinflammation → tau phosphorylation → neuronal death

**TREM2 as AD risk gene:** TREM2 R47H variant → 2-3× increased AD risk (comparable to one APOE4 copy); TREM2 deficiency → impaired microglial Aβ phagocytosis → increased amyloid burden in mouse models; TREM2-activating antibodies (AL002c) in Phase II trials for early AD.

**APOE4:** APOE ε4/ε4 → 8-12× increased LOAD risk vs. ε3/ε3; mechanism: ApoE4 → impaired Aβ clearance (ApoE helps LRP1-mediated Aβ transport across BBB), promotes Aβ aggregation, associated with increased tau propagation; APOE4 carriers have shorter preclinical period and younger symptom onset.

## Pathology

### Diagnosis

**Biomarker-based (research/specialist):**
- CSF: Aβ42 ↓, p-tau181/p-tau231 ↑, total tau ↑; Aβ42/Aβ40 ratio most accurate
- PET: Amyloid PET (florbetapir/florbetaben/flutemetamol) — FDA approved for clinical use; tau PET (flortaucipir, FDA approved 2020) — detects NFT staging
- Blood biomarkers (emerging, high-throughput): Plasma p-tau217 and p-tau231 — high sensitivity/specificity for amyloid and tau pathology; plasma Aβ42/Aβ40 ratio (Simoa, IP-MS); NfL (neurofilament light chain) — non-specific neurodegeneration marker

**Clinical (traditional):**
- MMSE (Mini-Mental State Examination): 0-30; ≥24 normal; 18-23 mild; 10-17 moderate; <10 severe
- MoCA (Montreal Cognitive Assessment): More sensitive for mild impairment; ≥26/30 normal; detects MCI better than MMSE
- Neuropsychological battery: verbal learning (HVLT-R), executive function (Trails-B), language (category/letter fluency), visuospatial (Rey figure)

### Treatment [^van-dyck-2023-lecanemab]

**Disease-modifying (anti-amyloid):**
- **Lecanemab (Leqembi, anti-Aβ protofibrils, BioArctic/Eisai):** FDA approved (accelerated 2023, traditional 2024, first traditional approval for an anti-amyloid therapy); CLARITY-AD Phase III: 27% slowing of clinical decline (CDR-SB) at 18 months vs. placebo in early AD (MCI/mild AD); ARIA (amyloid-related imaging abnormalities: ARIA-E edema in 12.6%, ARIA-H microhemorrhages in 17.3%) is dose-limiting
- **Donanemab (Kisunla, anti-Aβ plaque, Eli Lilly):** FDA approved July 2024; TRAILBLAZER-ALZ-2: 35% slower decline (iADRS) vs. placebo; similar ARIA rates; unique: treatment discontinued once amyloid cleared on PET (median 12 months)
- **Aducanumab (Aduhelm, Biogen):** Controversial accelerated approval 2021 (reduced amyloid on PET); withdrawn from EU; most payers limit coverage; Phase III results discordant

**Symptomatic:**
- **Cholinesterase inhibitors** (donepezil, rivastigmine, galantamine): Inhibit acetylcholinesterase → increases synaptic ACh → modest improvement in cognition/behavior; first-line for mild-moderate AD; minimal disease modification
- **Memantine (NMDA antagonist):** Moderate uncompetitive NMDA blocker → reduces glutamate excitotoxicity; approved for moderate-severe AD; combined with donepezil (Namzaric)
- **Behavioral symptoms:** Selective SSRIs for depression/anxiety; low-dose antipsychotics (aripiprazole, quetiapine) for agitation (black box warning for elderly); avoid anticholinergics
- **Non-pharmacological:** Cognitive stimulation, physical exercise (aerobic → hippocampal neurogenesis), caregiver support

## Connections

- `targets` → **[Brain](../../06-organ/brain/README.md)** — Alzheimer's preferentially atrophies the hippocampus and entorhinal cortex; amyloid plaques and tau tangles disrupt synaptic transmission, cause microglial neuroinflammation, and drive progressive neuronal death from medial temporal lobe outward.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — microglia phagocytose Aβ plaques via TREM2; sustained microglial activation drives NLRP3 inflammasome and neuroinflammation; TREM2 loss-of-function variants are major risk factors for late-onset AD.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Aβ fibrils activate NLRP3 in microglia → IL-1β and pyroptosis → neuroinflammation and tau propagation; NLRP3 inhibition reduces AD pathology in mouse models.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — autophagy clears APP fragments and aggregated tau; declining autophagic flux in aging and AD contributes to plaque and tangle accumulation; lysosomal dysfunction is a primary AD pathomechanism; rapamycin-induced autophagy is neuroprotective in mouse models.
- `connects-to` → **[APOE](../../03-molecular/apoe/README.md)** — APOE4 (frequency ~15%) confers 3-4x heterozygous and 8-12x homozygous risk for late-onset AD; APOE4 impairs microglial Aβ phagocytosis, promotes Aβ aggregation, and worsens tau pathology; APOE4 homozygotes develop AD ~10 years earlier than APOE3 carriers.

[^selkoe-2016-alzheimer]: Selkoe DJ, Hardy J. The amyloid hypothesis of Alzheimer's disease at 25 years. *EMBO Mol Med.* 2016;8(6):595-608. [doi:10.15252/emmm.201606210](https://doi.org/10.15252/emmm.201606210) · [PubMed 27025652](https://pubmed.ncbi.nlm.nih.gov/27025652/)
[^jack-2018-nia-aa]: Jack CR Jr, Bennett DA, Blennow K, et al. NIA-AA Research Framework: Toward a biological definition of Alzheimer's disease. *Alzheimers Dement.* 2018;14(4):535-562. [doi:10.1016/j.jalz.2018.02.018](https://doi.org/10.1016/j.jalz.2018.02.018) · [PubMed 29653606](https://pubmed.ncbi.nlm.nih.gov/29653606/)
[^van-dyck-2023-lecanemab]: van Dyck CH, Swanson CJ, Aisen P, et al. Lecanemab in Early Alzheimer's Disease. *N Engl J Med.* 2023;388(1):9-21. [doi:10.1056/NEJMoa2212948](https://doi.org/10.1056/NEJMoa2212948) · [PubMed 36449413](https://pubmed.ncbi.nlm.nih.gov/36449413/)

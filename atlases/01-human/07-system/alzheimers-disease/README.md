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
  - target: 01-human/03-molecular/app
    relation: connects-to
    note: "APP FAD mutations (V717I, Swedish K670N/M671L) and trisomy 21 increase Aβ42 via β/γ-secretase cleavage; Aβ42 oligomers are synaptotoxic and seed amyloid plaques; lecanemab (anti-Aβ protofibrils) slows cognitive decline 27% in MCI and mild AD."
  - target: 01-human/03-molecular/mapt
    relation: connects-to
    note: "Tau hyperphosphorylation at Thr181, Ser202/Thr205, Ser396 → PHF → NFT formation; Braak staging I–VI tracks NFT spread from entorhinal cortex to isocortex and correlates with cognitive decline; tau-PET (flortaucipir) predicts cognitive trajectory and guides clinical staging in AD."
  - target: 01-human/07-system/lewy-body-dementia
    relation: connects-to
    note: "DLB is commonly mistaken for AD; 50-70% of DLB cases have concurrent Aβ plaque and tau co-pathology; both share APOE4 risk; neuroleptic sensitivity in DLB is fatal (~50%) while not a concern in AD; occipital FDG-PET hypometabolism and DAT-SPECT distinguish DLB from AD."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β hyperactivation in AD hippocampus phosphorylates tau at PHF-1 (Ser396/404) and Thr231 → neurofibrillary tangles; promotes amyloid-β via APP processing; insulin resistance activates GSK-3β; tideglusib (GSK-3β inhibitor) failed Phase 2 AD trials in 2013."
  - target: 01-human/03-molecular/snca
    relation: connects-to
    note: "Alpha-synuclein (SNCA) and amyloid-β co-aggregate in DLB, an AD/PD overlap syndrome; SNCA Lewy pathology accelerates tau spreading via prion-like mechanisms; ~10-15% of AD patients have concurrent Lewy body pathology; alpha-synuclein SAA distinguishes DLB from AD."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Melatonin production declines in Alzheimer disease due to SCN atrophy; disrupted circadian rhythm → sundowning (late-day agitation); exogenous melatonin (0.5-6 mg bedtime) modestly improves AD sleep; melatonin is antioxidant and reduces Aβ aggregation in preclinical models."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Impaired brain insulin signalling (\"type 3 diabetes\") is implicated in AD: INSR hyposensitivity → reduced Akt → ↑GSK-3β → tau hyperphosphorylation; intranasal insulin improves memory in MCI/AD Phase 2 trials; T2DM doubles AD risk; GLP-1 agonists are under Phase 3 investigation."
  - target: 01-human/03-molecular/tdp-43
    relation: connects-to
    note: "LATE (limbic-predominant age-related TDP-43 encephalopathy) affects ~20% of octogenarians and mimics AD clinically; TDP-43 co-pathology in ~57% of AD brains worsens cognitive trajectory; nuclear loss → TDPBP cryptic exon inclusion in hippocampal neurons."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "GLP-1R activation reduces amyloid-β, tau phosphorylation, and neuroinflammation in preclinical AD models; semaglutide EVOKE Phase 3 trial targets early AD; GLP-1R agonists may address brain insulin resistance via Akt → reduced GSK-3β → less tau hyperphosphorylation."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Age-related IGF-1 decline contributes to AD risk: low IGF-1 impairs hippocampal neurogenesis and synaptic plasticity; INSR/IGF-1R resistance in AD neurons → reduced Akt → ↑GSK-3β → tau phosphorylation; IGF-1 restores cognition in preclinical AD models and reduces Aβ plaque load."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "Alzheimer's and Parkinson's are the two commonest neurodegenerative diseases that overlap in pathology: both involve misfolded-protein aggregation (amyloid/tau vs α-synuclein) and can co-occur, with Lewy bodies in many Alzheimer brains—a proteinopathy spectrum."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Alzheimer's disease is ultimately the death of neurons and their synapses: amyloid plaques and tau tangles disrupt synaptic function and trigger neuronal loss, especially of cholinergic and hippocampal neurons—and synapse loss correlates best with the dementia."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Alzheimer's disease is sometimes called 'type 3 diabetes' for its link to insulin resistance: impaired brain insulin signaling promotes amyloid and tau pathology, and type 2 diabetes raises Alzheimer's risk—why GLP-1 drugs are being tested against dementia."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Alzheimer's classically depletes acetylcholine: early loss of basal-forebrain cholinergic neurons impairs memory, and the only long-standing symptomatic drugs—cholinesterase inhibitors—work by preserving this neurotransmitter, though they do not slow the disease."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "The hippocampus is where Alzheimer's begins: tau tangles and atrophy strike this memory-forming structure first, explaining the early loss of recent memory, and hippocampal shrinkage on MRI is among the earliest imaging signs of the disease."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Astrocytes shape Alzheimer's neuroinflammation: reactive astrocytes cluster around amyloid plaques, and while they can help clear amyloid, their chronic activation alongside microglia releases inflammatory mediators that damage neurons and synapses."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement drives synapse loss in Alzheimer's: C3 and C1q tag vulnerable synapses, prompting microglia to prune them, so reactivating this developmental 'eat-me' signal helps explain the early synaptic loss that best correlates with memory decline."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Vascular disease and Alzheimer's intertwine: atherosclerosis and small-vessel disease reduce brain perfusion and clearance of amyloid, so most late-life dementia is 'mixed', and controlling blood pressure, cholesterol, and diabetes lowers dementia risk."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Depression and Alzheimer's are tangled: late-life depression can be an early prodrome of dementia and is also an independent risk factor, while AD itself often presents with apathy and low mood—so new depression in an older adult warrants cognitive assessment."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Alzheimer's overexcites neurons through glutamate: amyloid and tau disrupt glutamate clearance, causing excitotoxic overstimulation of NMDA receptors that damages synapses—the rationale for memantine, which dampens this glutamate signaling."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Alzheimer's recruits cytotoxic T cells into the brain: CD8 T cells accumulate around plaques and tau pathology, and this adaptive-immune infiltration is increasingly seen as an active contributor to neurodegeneration, not a bystander."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Metal ions like zinc shape Alzheimer's amyloid: zinc and copper bind amyloid-beta, promoting its aggregation and generating oxidative stress, so disturbed brain metal balance is one hypothesis for how plaques form and injure neurons."
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
- `connects-to` → **[APP](../../03-molecular/app/README.md)** — APP FAD mutations (V717I, Swedish K670N/M671L) and trisomy 21 increase Aβ42 via β/γ-secretase cleavage; Aβ42 oligomers are synaptotoxic and seed amyloid plaques; lecanemab (anti-Aβ protofibrils) slows cognitive decline 27% in MCI and mild AD.
- `connects-to` → **[MAPT](../../03-molecular/mapt/README.md)** — tau hyperphosphorylation at Thr181, Ser202/Thr205, Ser396 → PHF → NFT formation; Braak staging I–VI tracks NFT spread from entorhinal cortex to isocortex and correlates with cognitive decline; tau-PET (flortaucipir) predicts cognitive trajectory and guides clinical staging in AD.
- `connects-to` → **[Lewy Body Dementia](../lewy-body-dementia/README.md)** — DLB is commonly mistaken for AD; 50-70% of DLB cases have concurrent Aβ plaque and tau co-pathology; both share APOE4 risk; fatal neuroleptic sensitivity in DLB (~50%) is critical to distinguish from AD where antipsychotics are used; occipital FDG-PET hypometabolism and DAT-SPECT distinguish DLB from AD.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β hyperactivation in AD hippocampus phosphorylates tau at PHF-1 (Ser396/404) and Thr231 → neurofibrillary tangles; promotes amyloid-β via APP processing; insulin resistance activates GSK-3β; the GSK-3β inhibitor tideglusib failed Phase 2 AD trials in 2013.
- `connects-to` → **[SNCA](../../03-molecular/snca/README.md)** — alpha-synuclein (SNCA) and amyloid-β co-aggregate in DLB, an AD/PD overlap syndrome; SNCA Lewy pathology accelerates tau spreading via prion-like mechanisms; ~10-15% of AD patients have concurrent Lewy body pathology; alpha-synuclein SAA distinguishes DLB from AD.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Melatonin production declines in Alzheimer disease due to SCN atrophy; disrupted circadian rhythm → sundowning (late-day agitation); exogenous melatonin (0.5-6 mg bedtime) modestly improves AD sleep; melatonin is antioxidant and reduces Aβ aggregation in preclinical models.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — impaired brain insulin signalling ("type 3 diabetes") is implicated in AD: INSR hyposensitivity → reduced Akt → ↑GSK-3β → tau hyperphosphorylation; intranasal insulin improves memory in MCI/AD Phase 2 trials; T2DM doubles AD risk; GLP-1 agonists are under Phase 3 investigation.
- `connects-to` → **[TDP-43](../../03-molecular/tdp-43/README.md)** — LATE (limbic-predominant age-related TDP-43 encephalopathy) affects ~20% of octogenarians and mimics AD clinically; TDP-43 co-pathology in ~57% of AD brains worsens cognitive trajectory; nuclear TDP-43 loss → cryptic exon inclusion in hippocampal neurons via TDPBP splicing suppression loss.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — GLP-1R activation reduces amyloid-β, tau phosphorylation, and neuroinflammation in preclinical AD models; semaglutide EVOKE Phase 3 trial targets early AD; GLP-1R agonists may address brain insulin resistance via Akt → reduced GSK-3β → less tau hyperphosphorylation.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — age-related IGF-1 decline contributes to AD risk: low IGF-1 impairs hippocampal neurogenesis and synaptic plasticity; INSR/IGF-1R resistance in AD neurons → reduced Akt → ↑GSK-3β → tau phosphorylation; IGF-1 restores cognition in preclinical AD models and reduces Aβ plaque load.
- `connects-to` → **[Parkinson's Disease](../parkinsons-disease/README.md)** — Alzheimer's and Parkinson's are the two commonest neurodegenerative diseases that overlap in pathology: both involve misfolded-protein aggregation (amyloid/tau vs α-synuclein) and can co-occur, with Lewy bodies in many Alzheimer brains—a proteinopathy spectrum.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Alzheimer's disease is ultimately the death of neurons and their synapses: amyloid plaques and tau tangles disrupt synaptic function and trigger neuronal loss, especially of cholinergic and hippocampal neurons—and synapse loss correlates best with the dementia.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Alzheimer's disease is sometimes called 'type 3 diabetes' for its link to insulin resistance: impaired brain insulin signaling promotes amyloid and tau pathology, and type 2 diabetes raises Alzheimer's risk—why GLP-1 drugs are being tested against dementia.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Alzheimer's classically depletes acetylcholine: early loss of basal-forebrain cholinergic neurons impairs memory, and the only long-standing symptomatic drugs—cholinesterase inhibitors—work by preserving this neurotransmitter, though they do not slow the disease.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — The hippocampus is where Alzheimer's begins: tau tangles and atrophy strike this memory-forming structure first, explaining the early loss of recent memory, and hippocampal shrinkage on MRI is among the earliest imaging signs of the disease.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Astrocytes shape Alzheimer's neuroinflammation: reactive astrocytes cluster around amyloid plaques, and while they can help clear amyloid, their chronic activation alongside microglia releases inflammatory mediators that damage neurons and synapses.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement drives synapse loss in Alzheimer's: C3 and C1q tag vulnerable synapses, prompting microglia to prune them, so reactivating this developmental 'eat-me' signal helps explain the early synaptic loss that best correlates with memory decline.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Vascular disease and Alzheimer's intertwine: atherosclerosis and small-vessel disease reduce brain perfusion and clearance of amyloid, so most late-life dementia is 'mixed', and controlling blood pressure, cholesterol, and diabetes lowers dementia risk.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Depression and Alzheimer's are tangled: late-life depression can be an early prodrome of dementia and is also an independent risk factor, while AD itself often presents with apathy and low mood—so new depression in an older adult warrants cognitive assessment.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — Alzheimer's overexcites neurons through glutamate: amyloid and tau disrupt glutamate clearance, causing excitotoxic overstimulation of NMDA receptors that damages synapses—the rationale for memantine, which dampens this glutamate signaling.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Alzheimer's recruits cytotoxic T cells into the brain: CD8 T cells accumulate around plaques and tau pathology, and this adaptive-immune infiltration is increasingly seen as an active contributor to neurodegeneration, not a bystander.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Metal ions like zinc shape Alzheimer's amyloid: zinc and copper bind amyloid-beta, promoting its aggregation and generating oxidative stress, so disturbed brain metal balance is one hypothesis for how plaques form and injure neurons.

[^selkoe-2016-alzheimer]: Selkoe DJ, Hardy J. The amyloid hypothesis of Alzheimer's disease at 25 years. *EMBO Mol Med.* 2016;8(6):595-608. [doi:10.15252/emmm.201606210](https://doi.org/10.15252/emmm.201606210) · [PubMed 27025652](https://pubmed.ncbi.nlm.nih.gov/27025652/)
[^jack-2018-nia-aa]: Jack CR Jr, Bennett DA, Blennow K, et al. NIA-AA Research Framework: Toward a biological definition of Alzheimer's disease. *Alzheimers Dement.* 2018;14(4):535-562. [doi:10.1016/j.jalz.2018.02.018](https://doi.org/10.1016/j.jalz.2018.02.018) · [PubMed 29653606](https://pubmed.ncbi.nlm.nih.gov/29653606/)
[^van-dyck-2023-lecanemab]: van Dyck CH, Swanson CJ, Aisen P, et al. Lecanemab in Early Alzheimer's Disease. *N Engl J Med.* 2023;388(1):9-21. [doi:10.1056/NEJMoa2212948](https://doi.org/10.1056/NEJMoa2212948) · [PubMed 36449413](https://pubmed.ncbi.nlm.nih.gov/36449413/)

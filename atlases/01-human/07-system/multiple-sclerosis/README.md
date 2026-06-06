---
schema: human-scale-entry/v1
id: multiple-sclerosis
name: Multiple Sclerosis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Autoimmune demyelinating CNS disease mediated by autoreactive Th1/Th17 and CD8+ T cells attacking myelin; relapsing-remitting in 85% at onset. Natalizumab, ocrelizumab, and cladribine are high-efficacy DMTs; early aggressive therapy improves long-term disability outcomes."
aliases: ["MS", "multiple sclerosis", "RRMS", "PPMS", "clinically isolated syndrome", "CIS"]
sources:
  - id: compston-2008-ms-review
    type: peer-reviewed
    cite: "Compston A, Coles A. Multiple sclerosis. Lancet. 2008;372(9648):1502-1517."
    doi: "10.1016/S0140-6736(08)61620-7"
    pmid: "18970977"
    url: "https://doi.org/10.1016/S0140-6736(08)61620-7"
  - id: kappos-2006-natalizumab
    type: peer-reviewed
    cite: "Polman CH, O'Connor PW, Havrdova E, et al. A randomized, placebo-controlled trial of natalizumab for relapsing multiple sclerosis. N Engl J Med. 2006;354(9):899-910."
    doi: "10.1056/NEJMoa044397"
    pmid: "16510744"
    url: "https://doi.org/10.1056/NEJMoa044397"
  - id: montalban-2017-ocrelizumab-ppms
    type: peer-reviewed
    cite: "Montalban X, Hauser SL, Kappos L, et al. Ocrelizumab versus Placebo in Primary Progressive Multiple Sclerosis. N Engl J Med. 2017;376(3):209-220."
    doi: "10.1056/NEJMoa1606468"
    pmid: "28002688"
    url: "https://doi.org/10.1056/NEJMoa1606468"
cross_links:
  - target: 01-human/06-organ/brain
    relation: targets
    note: "MS lesions develop in periventricular white matter and cortical grey matter; demyelination disrupts saltatory conduction; chronic inflammation causes axonal transection and atrophy; brain volume loss on MRI correlates with long-term disability."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "Oligodendrocytes are the primary MS target; autoreactive T cells and complement attack myelin sheaths → demyelination and OPC exhaustion; remyelination is incomplete in progressive MS due to OPC failure and inhibitory myelin debris accumulation."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Th1 (IFN-gamma) and Th17 (IL-17) cells are the primary MS pathogenic T cells; Th17 breach the BBB via CCR6/CCL20; both subsets attack myelin directly and activate resident microglia; natalizumab blocks VLA-4→VCAM-1, preventing T cell CNS trafficking."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Astrocytes form glial scar in MS lesions (GFAP+), impeding OPC remyelination; but astrocytes also sustain BBB integrity and produce CNTF/LIF supporting oligodendrocyte survival; astrocyte dysfunction drives progressive MS and lesion repair failure."
---

# Multiple Sclerosis

## Overview

**Multiple sclerosis (MS)** is the most common **autoimmune demyelinating disease of the central nervous system** — a chronic, inflammatory condition in which autoreactive T cells and B cells breach the blood-brain barrier and attack **myelin**, the lipid-rich insulating sheath produced by oligodendrocytes. The result is **demyelinating plaques** (sclerotic lesions) in white matter and grey matter, causing disrupted saltatory conduction → neurological symptoms; over time, axonal loss and cortical atrophy → permanent disability [^compston-2008-ms-review].

MS affects approximately **2.8 million people worldwide** (~1 million in the US), with an incidence of ~20-30 per 100,000 in high-risk regions (Northern Europe, Canada, New Zealand). Female:male ratio ~3:1; peak onset 20-40 years. It is the leading non-traumatic cause of neurological disability in young adults.

**MS subtypes:**
- **Relapsing-remitting MS (RRMS, ~85% at onset):** Discrete episodes (relapses/exacerbations) of neurological worsening over days-weeks → partial or complete recovery; MRI shows new or enhancing lesions; treatable with disease-modifying therapies (DMTs)
- **Secondary progressive MS (SPMS):** Develops in 50-80% of RRMS after 20+ years; steady accumulation of disability with or without relapses; less MRI activity but ongoing axonal loss; some DMTs (siponimod, cladribine) modestly effective
- **Primary progressive MS (PPMS, ~15%):** Insidious, continuous neurological deterioration from onset without clear relapses; predominantly spinal cord involvement → progressive paraplegia; until 2017, no approved therapy; ocrelizumab FDA approved 2017 [^montalban-2017-ocrelizumab-ppms]
- **Clinically isolated syndrome (CIS):** First clinical event consistent with MS (optic neuritis, myelitis, brainstem/cerebellar syndrome); 70-80% progress to MS within 20 years if MRI reveals disseminated lesions; early DMT initiation after CIS reduces conversion

**Risk factors:**
- **HLA-DRB1*15:01:** Strongest genetic risk factor (~3× increased risk); in linkage disequilibrium with HLA-DQB1*06:02; presents myelin peptides (MBP, MOG, PLP) to autoreactive CD4+ T cells
- **Epstein-Barr virus (EBV):** Nearly all MS patients are EBV+; longitudinal military cohort: EBV seroconversion → 32× increased MS risk; molecular mimicry between EBNA-1 and GlialCAM (myelin antigen) proposed mechanism; anti-EBNA-1 antibodies cross-react with CNS proteins
- **Vitamin D deficiency:** Low 25-OH-vitamin D → increased MS risk; VDR binding site in HLA-DRB1*15:01 promoter; latitude gradient of MS correlates with sunlight exposure
- **Smoking:** 1.5× increased MS risk; accelerates disability progression
- **Gut microbiome:** Dysbiosis in MS patients; Akkermansia muciniphila and Prevotella overrepresented; germ-free mice with MS-prone T cells develop disease with MS-patient microbiome transfer

## Structure

### MS lesion anatomy [^compston-2008-ms-review]

**Acute active plaque:**
- T cells (CD4+, CD8+) and macrophages infiltrate white matter via VCAM-1/ICAM-1 on activated BBB endothelium
- BBB disruption: gadolinium-enhancing on MRI (contrast T1) → first 4-6 weeks of plaque activity
- Macrophages and microglia phagocytose myelin → intracellular lipid droplets (foamy macrophages)
- Oligodendrocyte apoptosis → demyelinated axons
- Axonal transection can occur even in early acute lesions → irreversible damage

**Chronic inactive plaque:**
- Hypocellular center — demyelinated, gliotic; surrounded by sharp lesion edge
- Shadow plaques: partial remyelination by OPCs → thin, irregular myelin → "shadows" on histology; vulnerable to re-attack
- Slowly expanding plaques (SEL): Smoldering microglia activation at plaque edge → ongoing axonal damage in progressive MS

**Grey matter lesions (often underestimated):**
- Cortical lesions (leukocortical, intracortical, subpial) — not detected by conventional MRI; require double inversion recovery (DIR) or 7T MRI; correlate strongly with cognitive impairment
- **Meningeal inflammation:** Follicle-like B-cell aggregates in meninges in some PPMS patients → produce antibodies and cytokines → cortical demyelination (subpial spread)

### MS immunopathology

**Peripheral sensitization (lymph nodes):**
- Molecular mimicry or bystander activation → autoreactive CD4+ Th1/Th17 cells escape thymic deletion (low-affinity TCR for myelin antigens)
- EBV-infected B cells may present myelin antigens (EBNA-1/GlialCAM cross-reactivity) → autoreactive B cells persist

**CNS trafficking:**
- Activated Th1 (CCR5+) and Th17 (CCR6+) cells upregulate VLA-4 (alpha-4 beta-1 integrin) → bind VCAM-1 on inflamed BBB endothelium → transmigrate
- **Natalizumab:** Anti-alpha-4 integrin (VLA-4) antibody → blocks T cell and B cell CNS entry → 68% relapse rate reduction [^kappos-2006-natalizumab]
- Inside CNS: Reactivation of T cells by local APCs (microglia, dendritic cells) presenting myelin peptides (MBP 83-99, MOG 35-55, PLP 139-151) → effector T cell attack

**B cell role in MS:**
- RRMS: CSF oligoclonal bands (OCBs) in >95%; IgG produced by intrathecal B cells and plasma cells
- B cells present antigen to T cells, produce cytokines (IL-6, TNF-alpha, lymphotoxin), and activate complement → ocrelizumab (anti-CD20) highly effective
- Progressive MS: Meningeal B-cell follicles drive cortical demyelination

## Function

### Clinical presentation

**Relapse characteristics:**
- Subacute onset over hours-days → plateau → recovery over weeks-months
- Symptoms determined by lesion location: optic neuritis (pain with eye movement + central visual loss, optic nerve); myelitis (weakness/sensory deficit at/below a spinal level + bladder dysfunction, spinal cord); Lhermitte's sign (electric shock down spine with neck flexion, dorsal column); internuclear ophthalmoplegia (MLF lesion → dysconjugate gaze); cerebellar (Charcot's triad: dysarthria, nystagmus, intention tremor); Uhthoff's phenomenon (transient worsening with heat or exercise)

**Disability measures:**
- **EDSS (Expanded Disability Status Scale):** 0-10; 0 = normal; 4.0 = fully ambulatory without aid, limited by MS symptoms; 6.0 = requires walking aid; 7.0 = essentially restricted to wheelchair; 10.0 = death from MS; half-integer steps; primary endpoint in MS trials

**Cognitive symptoms:**
- Present in 40-65% of MS patients; processing speed and working memory most affected; correlates with grey matter atrophy and thalamic volume loss; no FDA-approved therapy for MS cognitive impairment

**Psychiatric:**
- Depression: ~50% lifetime prevalence; bidirectional (neuroinflammation → depression; MS diagnosis → reactive depression)
- Fatigue: Most common symptom; pathological fatigue (not purely mood or sleep-related); inflammatory mediators (IL-6, TNF-alpha) contribute; amantadine, modafinil modestly helpful

### Diagnosis (McDonald criteria 2017)

**Dissemination in space (DIS):** ≥1 T2 lesion in ≥2 of 4 areas: periventricular (≥3 lesions), juxtacortical/cortical, infratentorial, spinal cord

**Dissemination in time (DIT):** Gadolinium-enhancing lesion (active) AND non-enhancing lesion at same time point, OR new T2/enhancing lesion on follow-up MRI, OR OCBs in CSF

**CSF:** Oligoclonal IgG bands in CSF (not serum) in >95% of MS; elevated IgG index; pleocytosis (<50 cells/μL, predominantly lymphocytes); MOG-IgG and AQP4-IgG testing to exclude MOGAD and NMOSD

## Pathology

### Treatment [^montalban-2017-ocrelizumab-ppms]

**Disease-modifying therapies (DMTs) — platform therapies (moderate efficacy):**
- **Beta-interferons (IFN-beta-1a/1b):** Immunomodulatory; ~30% relapse reduction; SC or IM injection; flu-like symptoms, injection site reactions; first-line, safest in pregnancy after delivery
- **Glatiramer acetate (GA, Copaxone):** Random amino acid polymer; antigen competition or immunomodulation via Th2 shift; ~30% relapse reduction; daily SC; no systemic side effects; safe in pregnancy; antibody formation does not affect efficacy
- **Teriflunomide (Aubagio):** Oral; inhibits DHODH → proliferating lymphocytes; ~36% relapse reduction; teratogenic (accelerated elimination with cholestyramine needed pre-pregnancy)
- **Dimethyl fumarate (Tecfidera, BG-12):** Oral; activates Nrf2 → antioxidant pathway; shifts Th1 → Th2; reduces relapses ~50%; PML risk in lymphopenic patients (monitor lymphocyte count)

**High-efficacy DMTs:**
- **Natalizumab (Tysabri, anti-VLA-4):** IV monthly; 68% relapse reduction vs. placebo (AFFIRM trial); reserved for high-activity RRMS; **PML risk** (JC virus reactivation) in JC antibody+ patients (especially >2 years) — risk stratification by JC antibody index; switch to different therapy if index >0.9-1.5
- **Ocrelizumab (Ocrevus, anti-CD20):** IV every 6 months; 46-47% relapse reduction vs. IFN in RRMS; first approved for PPMS (25% reduction in 12-week confirmed disability progression, ORATORIO trial) [^montalban-2017-ocrelizumab-ppms]; infusion reactions; HBV reactivation screening; PML rare; check IgG levels; approved for RRMS and PPMS
- **Ofatumumab (Kesimpta, anti-CD20):** SC monthly then quarterly; non-inferior to teriflunomide in ASCLEPIOS I/II; self-administered SC injection; lower infection risk than IV ocrelizumab
- **Cladribine (Mavenclad):** Oral; purine analog → lymphocyte depletion → DNA strand breaks in lymphocytes; 2 short courses (4-5 days each, year 1 and year 2) → 5+ years of benefit; 58% relapse reduction vs. placebo; PML risk; lymphocyte monitoring required
- **Ublituximab (Briumvi, anti-CD20):** IV; quarterly after initial doses; ULTIMATE I/II vs. teriflunomide; similar mechanism to ocrelizumab
- **Alemtuzumab (Lemtrada, anti-CD52):** IV; severe B and T cell depletion → immune reconstitution; 49-55% superiority over beta-interferon in relapse reduction; reserved for highly active RRMS due to serious autoimmune AEs (thyroid disease ~30%, ITP, anti-GBM nephritis); risk-management program required

**Symptomatic treatment:**
- **Relapses:** IV methylprednisolone 1 g × 3-5 days → accelerates recovery (no long-term benefit); plasmapheresis for steroid-refractory severe relapses
- **Spasticity:** Baclofen (GABA-B agonist), tizanidine (alpha-2 agonist), oral or intrathecal
- **Bladder dysfunction:** Anticholinergics (oxybutynin, darifenacin) for overactive bladder; self-catheterization for retention; desmopressin for nocturia
- **Fatigue:** Amantadine (modest benefit), modafinil, exercise; treat underlying sleep disorders and depression
- **Pain:** Neuropathic pain — gabapentin, pregabalin, TCAs; trigeminal neuralgia → carbamazepine, oxcarbazepine
- **Walking:** Dalfampridine (4-aminopyridine, extended-release) — potassium channel blocker → improved nerve conduction in demyelinated axons; 10 mg BID; improves walking speed in ~35% of patients

## Connections

- `targets` → **[Brain](../../06-organ/brain/README.md)** — MS demyelinating plaques develop in periventricular white matter and cortical grey matter; brain volume loss (atrophy) correlates with long-term disability; meningeal B-cell follicles drive cortical demyelination in progressive MS via subpial spread.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — oligodendrocytes and their myelin sheaths are the primary MS targets; autoreactive T cells and complement attack myelin, causing demyelination; incomplete OPC remyelination in progressive MS drives permanent axonal loss and disability.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Th1 and Th17 cells are the primary MS pathogenic effectors; Th17 (CCR6+) breach the BBB via CCL20; both subsets attack myelin and activate microglia; natalizumab blocks VLA-4 integrin on T cells, preventing CNS trafficking.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — reactive astrocytes form glial scar in MS lesions, impeding OPC remyelination; astrocytes also sustain BBB integrity and produce neuroprotective factors (CNTF, LIF); astrocyte dysfunction is a primary driver of progressive MS and lesion repair failure.

[^compston-2008-ms-review]: Compston A, Coles A. Multiple sclerosis. *Lancet.* 2008;372(9648):1502-1517. [doi:10.1016/S0140-6736(08)61620-7](https://doi.org/10.1016/S0140-6736(08)61620-7) · [PubMed 18970977](https://pubmed.ncbi.nlm.nih.gov/18970977/)
[^kappos-2006-natalizumab]: Polman CH, O'Connor PW, Havrdova E, et al. A randomized, placebo-controlled trial of natalizumab for relapsing multiple sclerosis. *N Engl J Med.* 2006;354(9):899-910. [doi:10.1056/NEJMoa044397](https://doi.org/10.1056/NEJMoa044397) · [PubMed 16510744](https://pubmed.ncbi.nlm.nih.gov/16510744/)
[^montalban-2017-ocrelizumab-ppms]: Montalban X, Hauser SL, Kappos L, et al. Ocrelizumab versus Placebo in Primary Progressive Multiple Sclerosis. *N Engl J Med.* 2017;376(3):209-220. [doi:10.1056/NEJMoa1606468](https://doi.org/10.1056/NEJMoa1606468) · [PubMed 28002688](https://pubmed.ncbi.nlm.nih.gov/28002688/)

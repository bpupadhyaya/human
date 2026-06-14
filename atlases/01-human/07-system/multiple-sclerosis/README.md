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
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A is elevated in MS lesions and CSF; Th17 cells breach the blood-brain barrier via CXCR6 → demyelination; secukinumab (anti-IL-17A) paradoxically worsened MS relapse rates in phase 2 trials — suggesting complex compensatory roles of IL-17A/Treg balance in CNS disease."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5+ Th1 cells are recruited to CNS white matter lesions in MS; CCR5-Δ32 carriers have modestly reduced MS severity in some cohorts; CCR5 ligands (CCL3/CCL4/CCL5) are elevated in MS CSF; CCR5 antagonism (maraviroc) is being explored in neuroinflammation trials."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "Epstein-Barr virus is now considered a necessary cause of multiple sclerosis: a 10-million-person cohort showed MS risk jumps ~32-fold after EBV seroconversion, and EBV's EBNA-1 protein cross-reacts with the myelin protein GlialCAM — making EBV a leading target for MS prevention."
  - target: 01-human/07-system/myasthenia-gravis
    relation: connects-to
    note: "Multiple sclerosis and myasthenia gravis are both autoimmune neurological diseases: MS is a T-cell-driven demyelination of central myelin, whereas MG is an antibody attack on the neuromuscular junction — CNS versus peripheral, T-cell versus B-cell/complement."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Low vitamin D is a consistent, modifiable multiple-sclerosis risk factor: the latitude gradient of MS tracks sunlight, a vitamin-D-response element sits in the HLA-DRB1*15:01 promoter, and supplementation is being studied for prevention."
  - target: 01-human/07-system/nmo
    relation: connects-to
    note: "MS and NMOSD were long conflated until AQP4-IgG distinguished them: MS is T-cell/myelin-directed with small CNS plaques and a relapsing course, while NMOSD is AQP4-IgG astrocyte attack with severe optic neuritis and extensive myelitis—and MS drugs like interferon-β worsen NMOSD."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "B cells are now central to multiple sclerosis: beyond antibody they present antigen and form meningeal follicles driving cortical damage, and anti-CD20 therapies (ocrelizumab, ofatumumab) that deplete B cells are among the most effective treatments for MS."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "The eye is a frequent first window into multiple sclerosis: optic neuritis—painful monocular vision loss—is a common presenting attack, and internuclear ophthalmoplegia from a brainstem plaque is highly suggestive; OCT retinal thinning now tracks neurodegeneration in MS."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Depression is the commonest psychiatric comorbidity of multiple sclerosis: it stems both from demyelinating lesions in mood circuits and from the burden of chronic disability—often underrecognized, it degrades quality of life and warrants active screening."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Type I interferon was the first disease-modifying therapy for multiple sclerosis: interferon-β shifts immunity away from the pro-inflammatory Th17/Th1 pattern driving demyelination, reducing relapses—paradoxically, since the same cytokine family drives autoimmunity."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Multiple sclerosis is increasingly a neurodegenerative as well as demyelinating disease: beyond myelin loss, axonal and neuronal injury accumulates and underlies progressive disability, so neuroprotection—not just anti-inflammatory therapy—is a key unmet goal."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Microglia are central to MS lesions: they strip myelin and present antigen to drive demyelination, but also clear debris to permit remyelination—the same brain-resident macrophages both damage and repair, making microglial phenotype a target in progressive MS."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Multiple sclerosis and rheumatoid arthritis are both autoimmune diseases driven by Th17 and autoreactive lymphocytes, but target different tissues—CNS myelin vs synovial joints—yet share genetic risk and respond to overlapping immunomodulators."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Cytotoxic T cells contribute to MS damage: though CD4 Th cells initiate the attack, CD8 cytotoxic T cells dominate MS lesions and directly kill oligodendrocytes and neurons, helping explain the axonal loss that drives irreversible progressive disability."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "CD20-targeted therapy transformed MS treatment: depleting CD20+ B cells with ocrelizumab or rituximab sharply cuts relapses, proving B cells—not just T cells—drive the disease, and giving the first effective drug for progressive MS."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Multiple sclerosis is the prototypical demyelinating disease of the central nervous system: immune attack strips myelin from brain, spinal cord and optic nerve in scattered plaques, so its protean symptoms reflect lesions dispersed in space and time."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "MS is fundamentally an autoimmune disease: self-reactive lymphocytes breach the blood-brain barrier to attack myelin, so it overlaps with other autoimmunity and is treated by immunomodulation—shifting MS care from symptom control to immune-directed therapy."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The gut microbiome shapes multiple sclerosis risk and activity: altered gut flora can tip the balance between inflammatory and regulatory T cells that attack myelin, so diet and the microbiome are emerging factors in an autoimmune disease of the brain."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "MS reflects failed immune tolerance: regulatory T cells that should restrain autoreactive cells are deficient or dysfunctional, letting myelin-attacking T and B cells run unchecked—so restoring regulatory balance is a goal of MS therapy."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Plasma cells leave MS's diagnostic signature: B cells mature into plasma cells inside the CNS and secrete antibodies detected as oligoclonal bands in spinal fluid, a hallmark that supports diagnosis and reflects the intrathecal immune response."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "MS's strongest genetic risk is an MHC class II allele: HLA-DRB1*15:01 shapes how myelin peptides are presented to T cells, the genetic basis tying the immune system's antigen presentation to attacks on the central nervous system."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages strip myelin in active MS lesions: drawn into the CNS, they (with microglia) phagocytose myelin and damage oligodendrocytes, so myelin-laden macrophages are the histologic signature of an active demyelinating plaque."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron rims mark MS's smoldering lesions: iron-laden microglia ring chronic active plaques, visible as paramagnetic rim lesions on MRI that flag ongoing, treatment-resistant inflammation driving progression."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Sodium channels betray the demyelinated MS axon: stripped of myelin, the axon scatters sodium channels to keep firing, but this leaky, energy-hungry state lets sodium and calcium flood in, driving the axonal degeneration behind permanent disability."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Nitric oxide is a hidden axon-killer in MS: activated microglia and macrophages pour out NO that blocks nerve conduction and poisons mitochondria in demyelinated axons, contributing to both the symptoms and the slow neurodegeneration."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Glutamate excitotoxicity widens MS damage: inflamed lesions spill excess glutamate that overexcites and kills oligodendrocytes and neurons, so beyond immune attack, this neurotransmitter helps turn inflammation into lasting tissue loss."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "MS damage reaches the synapse: beyond stripping myelin, the disease erodes gray-matter synapses, and this synaptic loss tracks the cognitive decline and disability that demyelination alone does not explain."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium executes the axon loss in MS: demyelinated axons overload with sodium, which reverses the sodium-calcium exchanger and floods them with calcium, the influx that degrades the axon and drives permanent disability."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells help open the brain to MS attack: in lesions they release mediators that breach the blood-brain barrier and amplify demyelination, linking an allergic-type immune cell to the autoimmune assault on myelin."
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
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A is elevated in MS lesions and CSF; Th17 cells breach the blood-brain barrier via CXCR6 → demyelination; secukinumab (anti-IL-17A) paradoxically worsened MS relapse rates in phase 2 trials — suggesting complex compensatory roles of IL-17A/Treg balance in CNS disease.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5⁺ Th1 cells are recruited to CNS white matter MS lesions via CCL3/CCL4/CCL5 chemokines; CCR5-Δ32 heterozygosity is associated with modestly reduced MS severity in some epidemiological cohorts; CCR5 antagonism (maraviroc) is being explored as adjunct anti-inflammatory therapy in neuroinflammation.
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — Epstein-Barr virus is now considered a necessary cause of multiple sclerosis: a 10-million-person cohort showed MS risk jumps ~32-fold after EBV seroconversion, and EBV's EBNA-1 protein cross-reacts with the myelin protein GlialCAM — making EBV a leading target for MS prevention.
- `connects-to` → **[Myasthenia Gravis](../myasthenia-gravis/README.md)** — Multiple sclerosis and myasthenia gravis are both autoimmune neurological diseases: MS is a T-cell-driven demyelination of central myelin, whereas MG is an antibody attack on the neuromuscular junction — CNS versus peripheral, T-cell versus B-cell/complement.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Low vitamin D is a consistent, modifiable multiple-sclerosis risk factor: the latitude gradient of MS tracks sunlight, a vitamin-D-response element sits in the HLA-DRB1*15:01 promoter, and supplementation is being studied for prevention.
- `connects-to` → **[NMOSD](../nmo/README.md)** — MS and NMOSD were long conflated until AQP4-IgG distinguished them: MS is T-cell/myelin-directed with small CNS plaques and a relapsing course, while NMOSD is AQP4-IgG astrocyte attack with severe optic neuritis and extensive myelitis—and MS drugs like interferon-β worsen NMOSD.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — B cells are now central to multiple sclerosis: beyond antibody they present antigen and form meningeal follicles driving cortical damage, and anti-CD20 therapies (ocrelizumab, ofatumumab) that deplete B cells are among the most effective treatments for MS.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — The eye is a frequent first window into multiple sclerosis: optic neuritis—painful monocular vision loss—is a common presenting attack, and internuclear ophthalmoplegia from a brainstem plaque is highly suggestive; OCT retinal thinning now tracks neurodegeneration in MS.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Depression is the commonest psychiatric comorbidity of multiple sclerosis: it stems both from demyelinating lesions in mood circuits and from the burden of chronic disability—often underrecognized, it degrades quality of life and warrants active screening.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Type I interferon was the first disease-modifying therapy for multiple sclerosis: interferon-β shifts immunity away from the pro-inflammatory Th17/Th1 pattern driving demyelination, reducing relapses—paradoxically, since the same cytokine family drives autoimmunity.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Multiple sclerosis is increasingly a neurodegenerative as well as demyelinating disease: beyond myelin loss, axonal and neuronal injury accumulates and underlies progressive disability, so neuroprotection—not just anti-inflammatory therapy—is a key unmet goal.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Microglia are central to MS lesions: they strip myelin and present antigen to drive demyelination, but also clear debris to permit remyelination—the same brain-resident macrophages both damage and repair, making microglial phenotype a target in progressive MS.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Multiple sclerosis and rheumatoid arthritis are both autoimmune diseases driven by Th17 and autoreactive lymphocytes, but target different tissues—CNS myelin vs synovial joints—yet share genetic risk and respond to overlapping immunomodulators.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Cytotoxic T cells contribute to MS damage: though CD4 Th cells initiate the attack, CD8 cytotoxic T cells dominate MS lesions and directly kill oligodendrocytes and neurons, helping explain the axonal loss that drives irreversible progressive disability.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — CD20-targeted therapy transformed MS treatment: depleting CD20+ B cells with ocrelizumab or rituximab sharply cuts relapses, proving B cells—not just T cells—drive the disease, and giving the first effective drug for progressive MS.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Multiple sclerosis is the prototypical demyelinating disease of the central nervous system: immune attack strips myelin from brain, spinal cord and optic nerve in scattered plaques, so its protean symptoms reflect lesions dispersed in space and time.
- `connects-to` → **[Immune System](../immune-system/README.md)** — MS is fundamentally an autoimmune disease: self-reactive lymphocytes breach the blood-brain barrier to attack myelin, so it overlaps with other autoimmunity and is treated by immunomodulation—shifting MS care from symptom control to immune-directed therapy.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The gut microbiome shapes multiple sclerosis risk and activity: altered gut flora can tip the balance between inflammatory and regulatory T cells that attack myelin, so diet and the microbiome are emerging factors in an autoimmune disease of the brain.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — MS reflects failed immune tolerance: regulatory T cells that should restrain autoreactive cells are deficient or dysfunctional, letting myelin-attacking T and B cells run unchecked—so restoring regulatory balance is a goal of MS therapy.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Plasma cells leave MS's diagnostic signature: B cells mature into plasma cells inside the CNS and secrete antibodies detected as oligoclonal bands in spinal fluid, a hallmark that supports diagnosis and reflects the intrathecal immune response.
- `connects-to` → **[MHC Class II](../../03-molecular/mhc-class-ii/README.md)** — MS's strongest genetic risk is an MHC class II allele: HLA-DRB1*15:01 shapes how myelin peptides are presented to T cells, the genetic basis tying the immune system's antigen presentation to attacks on the central nervous system.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages strip myelin in active MS lesions: drawn into the CNS, they (with microglia) phagocytose myelin and damage oligodendrocytes, so myelin-laden macrophages are the histologic signature of an active demyelinating plaque.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron rims mark MS's smoldering lesions: iron-laden microglia ring chronic active plaques, visible as paramagnetic rim lesions on MRI that flag ongoing, treatment-resistant inflammation driving progression.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Sodium channels betray the demyelinated MS axon: stripped of myelin, the axon scatters sodium channels to keep firing, but this leaky, energy-hungry state lets sodium and calcium flood in, driving the axonal degeneration behind permanent disability.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Nitric oxide is a hidden axon-killer in MS: activated microglia and macrophages pour out NO that blocks nerve conduction and poisons mitochondria in demyelinated axons, contributing to both the symptoms and the slow neurodegeneration.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — Glutamate excitotoxicity widens MS damage: inflamed lesions spill excess glutamate that overexcites and kills oligodendrocytes and neurons, so beyond immune attack, this neurotransmitter helps turn inflammation into lasting tissue loss.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — MS damage reaches the synapse: beyond stripping myelin, the disease erodes gray-matter synapses, and this synaptic loss tracks the cognitive decline and disability that demyelination alone does not explain.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium executes the axon loss in MS: demyelinated axons overload with sodium, which reverses the sodium-calcium exchanger and floods them with calcium, the influx that degrades the axon and drives permanent disability.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells help open the brain to MS attack: in lesions they release mediators that breach the blood-brain barrier and amplify demyelination, linking an allergic-type immune cell to the autoimmune assault on myelin.

[^compston-2008-ms-review]: Compston A, Coles A. Multiple sclerosis. *Lancet.* 2008;372(9648):1502-1517. [doi:10.1016/S0140-6736(08)61620-7](https://doi.org/10.1016/S0140-6736(08)61620-7) · [PubMed 18970977](https://pubmed.ncbi.nlm.nih.gov/18970977/)
[^kappos-2006-natalizumab]: Polman CH, O'Connor PW, Havrdova E, et al. A randomized, placebo-controlled trial of natalizumab for relapsing multiple sclerosis. *N Engl J Med.* 2006;354(9):899-910. [doi:10.1056/NEJMoa044397](https://doi.org/10.1056/NEJMoa044397) · [PubMed 16510744](https://pubmed.ncbi.nlm.nih.gov/16510744/)
[^montalban-2017-ocrelizumab-ppms]: Montalban X, Hauser SL, Kappos L, et al. Ocrelizumab versus Placebo in Primary Progressive Multiple Sclerosis. *N Engl J Med.* 2017;376(3):209-220. [doi:10.1056/NEJMoa1606468](https://doi.org/10.1056/NEJMoa1606468) · [PubMed 28002688](https://pubmed.ncbi.nlm.nih.gov/28002688/)

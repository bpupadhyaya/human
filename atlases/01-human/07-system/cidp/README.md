---
schema: human-scale-entry/v1
id: cidp
name: CIDP
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "CIDP (chronic inflammatory demyelinating polyneuropathy) is immune-mediated PNS demyelination lasting >8 weeks; anti-NF155/CNTN1 IgG4 define subtypes; IVIG and corticosteroids first-line; efgartigimod (FcRn inhibitor; FDA Jun 2024) and inebilizumab (anti-CD19) are new options."
aliases: ["CIDP", "chronic inflammatory demyelinating polyneuropathy", "chronic inflammatory demyelinating polyradiculoneuropathy", "anti-NF155 neuropathy"]
sources:
  - id: vanlaar-2010-efns-cidp
    type: peer-reviewed
    cite: "European Federation of Neurological Societies/Peripheral Nerve Society Guideline on management of chronic inflammatory demyelinating polyradiculoneuropathy. J Peripher Nerv Syst. 2010;15(1):1-9."
    doi: "10.1111/j.1529-8027.2010.00238.x"
    pmid: "20433600"
  - id: merkies-2008-ivig-ice
    type: peer-reviewed
    cite: "Hughes RA, Donofrio P, Bril V, et al. Intravenous immune globulin (10% caprylate-chromatography purified) for the treatment of chronic inflammatory demyelinating polyradiculoneuropathy (ICE study). Lancet Neurol. 2008;7(2):136-144."
    doi: "10.1016/S1474-4422(07)70329-0"
    pmid: "18178525"
  - id: vandenberheijde-2023-efgartigimod-cidp
    type: peer-reviewed
    cite: "van den Bergh PYK, van Doorn PA, Hadden RDM, et al. Efgartigimod alfa and hyaluronidase-qvfc in CIDP (ADHERE). N Engl J Med. 2023;390(3):219-232."
    doi: "10.1056/NEJMoa2310819"
    pmid: "38197812"
  - id: van-den-bergh-2023-cidp-guidelines
    type: peer-reviewed
    cite: "Van den Bergh PYK, van Doorn PA, Hadden RDM, et al. European Academy of Neurology/Peripheral Nerve Society guideline on diagnosis and treatment of chronic inflammatory demyelinating polyradiculoneuropathy: 2023 update. Eur J Neurol. 2023;30(10):2976-3020."
    doi: "10.1111/ene.15927"
    pmid: "37382198"
cross_links:
  - target: 01-human/03-molecular/fcrn
    relation: connects-to
    note: "FcRn recycles pathogenic anti-paranodal IgG4 (anti-NF155, anti-CNTN1) and total IgG in CIDP; efgartigimod alfa SC (ADHERE: 67% vs 36% INCAT responders; FDA Jun 2024) accelerates IgG catabolism → reduces pathogenic antibody titers and IVIG dose requirements."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: modulated-by
    note: "IVIG (2 g/kg loading; 1 g/kg q4w maintenance) is first-line CIDP therapy via FcγR blockade and anti-idiotypic antibodies (ICE trial: Lancet Neurol 2008); pathogenic IgG4 anti-NF155 and anti-CNTN1 disrupt paranodal axo-glial junctions; efgartigimod reduces total IgG."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "CIDP demyelinates peripheral nerves via macrophage-mediated paranodal stripping; NCS shows slowed conduction velocity, prolonged DML, F wave prolongation, and conduction blocks; anti-NF155 IgG4 disrupts paranodal axo-glial junctions → nodal instability and conduction failure."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "CD4+ T cells (IL-2-dependent) drive macrophage recruitment and paranodal demyelination in CIDP; Treg dysfunction may predispose; low-dose IL-2 for Treg expansion is under investigation as adjunct therapy in refractory CIDP and other autoimmune neuropathies."
  - target: 01-human/05-tissue/guillain-barre
    relation: connects-to
    note: "CIDP and GBS share peripheral nerve demyelination but differ in course: CIDP is chronic (>8 weeks); GBS is acute monophasic triggered by Campylobacter or EBV; both respond to IVIG and PLEX acutely; CIDP requires chronic immunosuppression; early CIDP may be misdiagnosed as GBS."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages are primary effectors of myelin destruction in CIDP via paranodal myelin stripping and FcR-mediated phagocytosis; IVIG blocks macrophage FcγR; macrophage TNF-α drives oxidative myelin damage; endoneurial macrophage infiltration is the histological hallmark of CIDP."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF-α elevated in CIDP endoneurium and serum; macrophage TNF-α drives oxidative myelin damage and Schwann cell apoptosis; anti-TNF agents (etanercept, infliximab) are CONTRAINDICATED in CIDP — they paradoxically worsen or trigger demyelinating neuropathy (FDA black box warning)."
  - target: 01-human/07-system/als
    relation: connects-to
    note: "CIDP and ALS both weaken muscles but are opposite kinds of disease: CIDP is an immune attack on peripheral-nerve myelin — chronic, demyelinating, and treatable with IVIG or FcRn inhibitors — while ALS is irreversible degeneration of the motor neuron itself."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "B cells drive the IgG4 subtypes of CIDP: clones producing anti-NF155 or anti-CNTN1 paranodal antibodies cause an aggressive, IVIG-resistant disease, which is why depleting them with rituximab (anti-CD20) or inebilizumab (anti-CD19) works where antibody-clearing therapies do less."
  - target: 01-human/07-system/multiple-sclerosis
    relation: connects-to
    note: "CIDP is sometimes called the peripheral counterpart of multiple sclerosis: both are immune-mediated demyelinating diseases, but MS attacks central myelin made by oligodendrocytes while CIDP attacks peripheral myelin made by Schwann cells — different cells and different drugs."
  - target: 01-human/07-system/myasthenia-gravis
    relation: connects-to
    note: "CIDP and myasthenia gravis are both antibody/immune-mediated, treatable autoimmune neuromuscular disorders at different sites: CIDP attacks peripheral-nerve myelin (areflexia, sensory loss), MG the postsynaptic junction (fatigable weakness); both improve with IVIG."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "CIDP and diabetes overlap and complicate each other: CIDP is over-represented in diabetes, and distinguishing demyelinating CIDP (which responds to immunotherapy) from common diabetic peripheral neuropathy is a key challenge, since conduction studies and response differ."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "CIDP often causes neuropathic pain alongside its hallmark weakness: demyelination and secondary axonal damage of sensory fibers produce burning, tingling and sensory ataxia, so beyond immunotherapy (IVIG, steroids) patients frequently need gabapentinoids or SNRIs for the pain."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Plasma cells underlie much of CIDP's autoimmunity: long-lived plasma cells secrete IgG antibodies that, with complement and macrophages, strip myelin from peripheral nerves—so IVIG, plasma exchange, and B-cell-targeting therapies are mainstays."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Regulatory T-cell failure permits CIDP: when Tregs cannot restrain autoreactive T and B cells, the immune system attacks peripheral-nerve myelin, so CIDP is treated by rebalancing immunity (steroids, IVIG)—immune dysregulation drives chronic demyelination."
  - target: 01-human/07-system/nmo
    relation: connects-to
    note: "CIDP and neuromyelitis optica are both antibody-mediated demyelinating diseases at different sites: CIDP attacks peripheral-nerve myelin (areflexia, sensorimotor loss), while NMO attacks CNS astrocytes/myelin via anti-AQP4—both IgG-driven and treated with immunotherapy."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "T helper cells help drive the autoimmune attack in CIDP: activated T cells breach the blood-nerve barrier and, with macrophages and antibodies, strip myelin from peripheral nerves—so immunosuppression, IVIG and plasma exchange restore conduction."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement amplifies nerve damage in CIDP: antibodies against myelin or nodal proteins fix complement on peripheral nerves, recruiting macrophages to demyelinate—so complement and the antibodies behind it are why IVIG and plasma exchange, which remove them, work."
  - target: 01-human/07-system/type-1-diabetes
    relation: connects-to
    note: "CIDP must be distinguished from diabetic neuropathy: diabetes both mimics and predisposes to CIDP, so a diabetic with disproportionate, treatable demyelinating weakness may have CIDP rather than ordinary diabetic polyneuropathy—a crucial, treatable distinction."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "CIDP attacks the insulation of peripheral neurons: immune-mediated stripping of myelin from motor and sensory nerve fibers slows or blocks conduction, causing the progressive weakness and numbness that, unlike Guillain-Barré, persist or relapse over months."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "CIDP is an autoimmune disease of peripheral nerves: antibodies, complement and T cells attack myelin, so it responds to immunotherapy (IVIG, steroids, plasma exchange)—the treatable, chronic counterpart of Guillain-Barré syndrome."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "CIDP is a chronic disorder of the peripheral nervous system: demyelination of nerve roots and trunks impairs the signals between cord and limbs, producing symmetric weakness and sensory loss that can be reversed if immunotherapy starts before axons are lost."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement helps strip myelin in CIDP: antibodies against nerve antigens fix complement (C3 and beyond), and macrophages then peel myelin off axons, so complement activation is part of the demyelinating attack that IVIg and plasma exchange interrupt."
  - target: 01-human/07-system/waldenstrom-macroglobulinemia
    relation: connects-to
    note: "A CIDP-like neuropathy can signal a paraprotein: anti-MAG IgM from Waldenström macroglobulinemia or MGUS attacks myelin, producing a demyelinating neuropathy that mimics CIDP—so an unexplained case warrants checking for a monoclonal protein."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "CIDP is driven partly by T cells: cytotoxic and helper T cells breach the blood-nerve barrier and, with macrophages, attack peripheral myelin, so the disease reflects a cellular as well as antibody-mediated assault on nerves."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "CIDP responds to corticosteroids—unlike its acute cousin: steroids that mimic cortisol calm the autoimmune attack on peripheral myelin and are first-line in CIDP, a key contrast with Guillain-Barré, where steroids fail and only IVIG or plasma exchange help."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "CIDP begins with dendritic cells presenting myelin: these antigen-presenting cells display peripheral-nerve proteins to T cells, breaking tolerance and launching the chronic immune attack that strips myelin from the nerves."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "Refractory CIDP can be treated by deleting B cells via CD20: rituximab targets this B-cell marker to shut down antibody production, especially effective in CIDP variants driven by antibodies against nodal proteins or MAG."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "CIDP cripples nerve conduction at the sodium channels: myelin loss disperses the sodium channels clustered at the nodes of Ranvier, so the saltatory jump of the impulse fails, producing the conduction block behind the weakness."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Demyelination in CIDP exposes potassium channels: stripped of myelin, the juxtaparanodal potassium channels normally hidden under it leak current and dampen the nerve impulse, worsening conduction failure—a target of channel-blocking drugs."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Macrophages strip myelin in CIDP under NF-kB's command: this inflammatory switch drives the cytokines and activation that send macrophages to peel myelin off peripheral nerves, the core attack that immunosuppression aims to halt."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "CIDP can travel with kidney disease: it sometimes co-occurs with membranous nephropathy, the two sharing autoantibodies against nodal proteins like neurofascin and contactin, linking the leaky kidney filter to the demyelinated nerve."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "In POEMS syndrome, VEGF drives a CIDP-like neuropathy: this rare plasma-cell disorder floods the blood with VEGF, producing a demyelinating polyneuropathy that mimics CIDP but needs entirely different, anti-plasma-cell treatment."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Chronic CIDP damage is sealed by calcium: when long demyelination finally lets axons degenerate, calcium pours into the bare fibers and executes their death, the irreversible loss behind lasting disability."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Imaging supports the CIDP diagnosis: MRI photons reveal the thickened, enhancing nerve roots and plexuses, and nerve ultrasound shows the enlarged nerves of this demyelinating disease."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Some CIDP is driven from the marrow: a monoclonal plasma-cell clone (an IgM MGUS, often anti-MAG) makes antibodies that attack peripheral myelin, a paraproteinemic neuropathy needing marrow-directed treatment."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammatory cytokines sustain CIDP: IL-6 and its kin help drive the autoimmune attack on myelin, keeping the demyelination smoldering and offering a target for newer immunomodulatory therapies."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows CIDP's repeated injury: round after round of demyelination and repair leaves Schwann cells wrapped in concentric 'onion-bulb' whorls around the axon, the hallmark of a chronic, relapsing nerve attack."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Severe CIDP can reach the breathing muscles: when the demyelination involves the nerves driving the diaphragm, respiratory weakness develops, the rare but dangerous extension that can require ventilatory support."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Some CIDP variants strike the cranial nerves: involvement of the nerves controlling eye movement causes double vision and drooping, broadening the disease beyond the limbs in its atypical forms."
---

# CIDP

## Overview

Chronic inflammatory demyelinating polyneuropathy (CIDP) is the most common chronic immune-mediated neuropathy, affecting 2–9 per 100,000 adults, with a mean age of onset of 50–55 years [^vanlaar-2010-efns-cidp]. It is characterized by progressive or relapsing-remitting **symmetric proximal and distal limb weakness** and **sensory deficits**, evolving over more than 8 weeks, caused by immune-mediated attack on the peripheral nerve myelin and paranodal structures.

CIDP represents a spectrum of disorders, with the classical phenotype accounting for ~50% of cases and several electrophysiologically and immunologically distinct variants comprising the rest. The identification of **anti-paranodal IgG4 autoantibodies** (anti-NF155, anti-CNTN1, anti-CASPR1, anti-pan-neurofascin) has transformed understanding of CIDP as a molecularly heterogeneous disease — these subsets have distinct clinical features, respond differently to IVIG, and are amenable to targeted B cell depletion therapy.

The approval of **efgartigimod alfa SC** (ADHERE trial, FDA June 2024) marked the first new mechanism of action approved for CIDP in decades, establishing FcRn inhibition as an effective approach to CIDP alongside the long-established IVIG, corticosteroids, and plasma exchange [^vandenberheijde-2023-efgartigimod-cidp].

## Structure

### Clinical Phenotypes

| Phenotype | Approximate frequency | Key features |
|:---------|:---------------------|:-------------|
| Typical/Classical CIDP | ~50% | Symmetric proximal + distal; motor + sensory; responds to IVIG |
| Pure sensory CIDP | ~10% | Sensory ataxia; large-fiber; normal strength |
| Pure motor CIDP | ~10% | Motor predominant; distinguish from MMN |
| Multifocal CIDP (MADSAM) | ~5% | Multifocal asymmetric; Lewis-Sumner syndrome |
| Distal CIDP (DADS) | ~5% | Distal predominant; anti-MAG antibodies in some |
| Anti-NF155 CIDP | ~5–10% | Prominent tremor; sensory ataxia; young onset; poor IVIG response |
| Anti-CNTN1 CIDP | ~3–5% | Aggressive; nephropathy; poor IVIG response; responds to rituximab |

### Diagnostic Criteria (EAN/PNS 2023 Update)

**Clinical criteria** (mandatory):
- Symptom duration >8 weeks (distinguishes from GBS)
- Symmetric proximal + distal weakness in arms and legs (or equivalent for variants)
- Sensory signs (reduced vibration, position sense, pinprick)
- Absent or reduced deep tendon reflexes

**Electrodiagnostic criteria** (nerve conduction studies):
The diagnosis requires ≥1 of (in ≥2 nerves):
- **Prolonged DML** (distal motor latency)
- **Reduced motor conduction velocity**
- **Prolonged F-wave latency** or absent F-waves
- **Conduction block** (≥50% CMAP amplitude reduction across a nerve segment)
- **Temporal dispersion** (>30% CMAP duration increase)

**Supportive criteria**:
- CSF: elevated protein (>45 mg/dL) with normal white cell count (<5/mm³) — albuminocytological dissociation
- MRI: gadolinium enhancement or hypertrophy of nerve roots, plexus, proximal nerve trunks
- Anti-paranodal antibodies: anti-NF155 IgG4, anti-CNTN1 IgG4, anti-CASPR1 IgG4
- Response to IVIG or corticosteroids (therapeutic trial as diagnostic criterion)
- Nerve biopsy: onion bulb formations (repeated demyelination/remyelination), macrophage-mediated demyelination

## Function

CIDP impairs peripheral nerve function through:

1. **Demyelination** — slowed or blocked conduction velocity → weakness and sensory dysfunction; proximal nerve and root involvement explains the unusual combination of proximal + distal deficits (contrasting with length-dependent peripheral neuropathies)

2. **Paranodal disruption** — anti-NF155 and anti-CNTN1 IgG4 disrupt the axo-glial paranodal junction (NF155-CNTN1-CASPR1 complex) → nodal Na⁺ channel instability → conduction failure independent of myelin destruction; explains the poor IVIG response in these subtypes (IVIG primarily targets macrophage FcγR and complement; IgG4 does not fix complement)

3. **Secondary axonal degeneration** — in severe or long-standing CIDP, axonal loss occurs secondary to chronic demyelination → poor recovery even after immunotherapy; explains why early treatment prevents long-term disability

Disease activity is quantified with:
- **INCAT disability scale** (0–10; inflammatory neuropathy cause and treatment)
- **ONLS** (overall neuropathy limitations scale)
- **I-RODS** (Inflammatory-RODS; Rasch-based measure)
- **MRC sum score** (muscle strength)
- **R-ODS** (Rasch-built overall disability scale)

## Pathology

### Immunopathogenesis

CIDP involves both **humoral** and **cellular** immune mechanisms [^van-den-bergh-2023-cidp-guidelines]:

**Humoral arm:**
- Complement-activating IgG1/IgG3 antibodies target compact myelin and Schwann cell surface antigens → classical complement activation → MAC deposition → Schwann cell lysis
- Non-complement-activating IgG4 antibodies target paranodal junctions (NF155, CNTN1, CASPR1) → functional disruption without complement activation; these are resistant to IVIG and plasma exchange but respond to B cell depletion (rituximab)
- Total IgG recycled by FcRn → FcRn inhibitors (efgartigimod) reduce all IgG including pathogenic subtypes

**Cellular arm:**
- CD4+ Th17 cells and CD8+ T cells infiltrate endoneurium → macrophage activation → paranodal myelin stripping
- Aberrant macrophage activation → TNF-α, IL-1β, ROS → oxidative myelin damage
- Defective Treg suppression allows autoreactive T cells to escape peripheral tolerance

### Paranodal Biology — NF155 and Contactin System

The **node of Ranvier** paranodal junction is maintained by a tripartite adhesion complex:
- **Neurofascin-155** (NF155, encoded by *NFASC*): glial side (paranodal loops)
- **Contactin-1** (CNTN1): axonal side
- **Contactin-associated protein 1** (CASPR1): axonal; links CNTN1 to cytoskeleton

IgG4 anti-NF155 or anti-CNTN1 disrupts this complex → paranodal loop detachment → Na⁺/K⁺ channel redistribution → electrical instability. Unlike compact myelin antibodies, these do not activate complement (IgG4 does not fix C1q efficiently) — the reason these patients do not respond to IVIG and respond poorly to plasma exchange. **Rituximab** (anti-CD20) achieves better responses in anti-NF155+ and anti-CNTN1+ CIDP by depleting the B cell clone producing these antibodies.

### Distinction from GBS (Guillain-Barré Syndrome)

| Feature | GBS | CIDP |
|:--------|:----|:-----|
| Course | Acute; monophasic | Chronic (>8 weeks); relapsing or progressive |
| Nadir | <4 weeks | Evolves >8 weeks |
| CSF protein | Elevated | Elevated |
| Electrodiagnostic | Acute demyelination | Chronic demyelination (onion bulbs) |
| Preceding infection | Common (Campylobacter, EBV, CMV) | Less common |
| Treatment | IVIG or PLEX (acute) | IVIG, corticosteroids, FcRn inhibitors (chronic) |

## Treatment

### First-line

**IVIG (Intravenous immunoglobulin):**
- 2 g/kg loading over 2–5 days → sustained therapy 1 g/kg q4w or 2 g/kg q12w
- The **ICE trial** (N=117, randomized, double-blind) demonstrated improvement in INCAT score in 54% vs 21% placebo at 24 weeks [^merkies-2008-ivig-ice]; FDA-approved for CIDP
- Mechanism: FcγR saturation → reduces macrophage phagocytosis of myelin; anti-idiotypic antibodies; complement neutralization; possibly accelerates pathogenic IgG catabolism by saturation of FcRn
- Subcutaneous IVIG (SCIG): equivalent efficacy to IVIG with home administration; Hyqvia (IVIG + recombinant hyaluronidase) and Hizentra approved for CIDP maintenance

**Corticosteroids:**
- Pulsed dexamethasone 40 mg/d × 4 days q4w × 6 cycles: DexDROP trial showed non-inferiority to daily prednisolone in short term
- Oral prednisolone 60 mg/d tapering: long-term immunosuppression; cumulative toxicity (osteoporosis, diabetes, cataract)
- Intravenous methylprednisolone 500–1000 mg/d × 3–5 days: used for relapses

**Plasma Exchange (PLEX):**
- 2–3× weekly × 6 sessions then tapering → removes circulating antibodies
- Benefit is typically short-lived (2–4 weeks); maintenance PLEX 1–2× weekly in some patients
- Less practical than IVIG/corticosteroids; mainly for acute relapses or IVIG-intolerant patients

### Second-line

**Rituximab** (anti-CD20; 375 mg/m² × 4 doses or 1000 mg × 2):
- Preferred for **anti-NF155** and **anti-CNTN1 IgG4-positive** CIDP — depletes the B cell clone producing paranodal antibodies; achieve complete/near-complete responses in ~50-70% of anti-NF155+ patients
- Rituximab does not deplete long-lived plasma cells → antibody titers fall gradually over months

**Azathioprine, mycophenolate mofetil, cyclosporine:**
- Steroid-sparing agents for long-term maintenance; limited controlled trial evidence but widely used

**Cyclophosphamide:** Reserved for severely refractory cases; risk of secondary malignancy

### Newer Approved and Investigational Agents

**FcRn inhibitors:**
- **Efgartigimod alfa and hyaluronidase-qvfc SC** (Vyvgart Hytrulo; argenx): The **ADHERE trial** (N=322, Phase 3, randomized, double-blind) showed **67.0% vs 36.0%** INCAT responders at cycle 3 vs placebo (p<0.0001); FDA approved **June 2024** for CIDP [^vandenberheijde-2023-efgartigimod-cidp]. Weekly SC injection. Reduces all IgG (~50-70%) including anti-paranodal IgG4 → decreases both macrophage-mediated demyelination and paranodal disruption.
- **Rozanolixizumab** (UCB): Phase 3 in CIDP (MOBILITY trial) ongoing; already FDA-approved for MG.
- **Nipocalimab** (Janssen): Anti-FcRn; Phase 3 in CIDP (RALI trial) ongoing.
- **Batoclimab** (Immunovant): Phase 3 in CIDP ongoing.

**Anti-CD19 mAb:**
- **Inebilizumab** (Uplizna; Amgen): FDA-approved for NMO; Phase 3 CIDP-IgG trial ongoing; anti-CD19 depletes a broader B cell compartment than anti-CD20 (includes plasmablasts and some plasma cells)

## Connections

- `connects-to` → **[FcRn](../../03-molecular/fcrn/README.md)** — FcRn recycles anti-paranodal IgG4 (anti-NF155, anti-CNTN1) sustaining pathogenic titers in CIDP; efgartigimod alfa SC (ADHERE: 67% vs 36% INCAT response; FDA Jun 2024) accelerates IgG catabolism and reduces IVIG requirements.
- `modulated-by` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — IVIG (2 g/kg; ICE trial Lancet Neurol 2008) is first-line CIDP therapy; pathogenic IgG4 anti-NF155 and anti-CNTN1 disrupt paranodal junctions; efgartigimod reduces total IgG catabolism.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — CIDP demyelinates peripheral nerves via macrophage-mediated paranodal stripping and anti-paranodal IgG4; NCS shows slowed conduction velocity, conduction blocks, and F-wave prolongation; axonal loss occurs secondary to chronic demyelination.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — CD4+ T cells (IL-2-dependent) drive macrophage recruitment and paranodal demyelination in CIDP; Treg dysfunction may predispose; low-dose IL-2 Treg expansion under investigation as adjunct therapy.
- `connects-to` → **[Guillain-Barré](../../05-tissue/guillain-barre/README.md)** — CIDP and GBS share peripheral nerve demyelination but differ in course: CIDP is chronic (>8 weeks); GBS is acute monophasic triggered by Campylobacter or EBV; both respond to IVIG and PLEX acutely; CIDP requires chronic immunosuppression; early CIDP may be misdiagnosed as GBS.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages are primary effectors of myelin destruction in CIDP via paranodal myelin stripping and FcR-mediated phagocytosis; IVIG blocks macrophage FcγR; macrophage TNF-α drives oxidative myelin damage; endoneurial macrophage infiltration is the histological hallmark of CIDP.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — TNF-α elevated in CIDP endoneurium and serum; macrophage TNF-α drives oxidative myelin damage and Schwann cell apoptosis; anti-TNF agents (etanercept, infliximab) are CONTRAINDICATED in CIDP — they paradoxically worsen or trigger demyelinating neuropathy (FDA black box warning).
- `connects-to` → **[ALS](../als/README.md)** — CIDP and ALS both weaken muscles but are opposite kinds of disease: CIDP is an immune attack on peripheral-nerve myelin — chronic, demyelinating, and treatable with IVIG or FcRn inhibitors — while ALS is irreversible degeneration of the motor neuron itself.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — B cells drive the IgG4 subtypes of CIDP: clones producing anti-NF155 or anti-CNTN1 paranodal antibodies cause an aggressive, IVIG-resistant disease, which is why depleting them with rituximab (anti-CD20) or inebilizumab (anti-CD19) works where antibody-clearing therapies do less.
- `connects-to` → **[Multiple Sclerosis](../multiple-sclerosis/README.md)** — CIDP is sometimes called the peripheral counterpart of multiple sclerosis: both are immune-mediated demyelinating diseases, but MS attacks central myelin made by oligodendrocytes while CIDP attacks peripheral myelin made by Schwann cells — different cells and different drugs.
- `connects-to` → **[Myasthenia Gravis](../myasthenia-gravis/README.md)** — CIDP and myasthenia gravis are both antibody/immune-mediated, treatable autoimmune neuromuscular disorders at different sites: CIDP attacks peripheral-nerve myelin (areflexia, sensory loss), MG the postsynaptic junction (fatigable weakness); both improve with IVIG.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — CIDP and diabetes overlap and complicate each other: CIDP is over-represented in diabetes, and distinguishing demyelinating CIDP (which responds to immunotherapy) from common diabetic peripheral neuropathy is a key challenge, since conduction studies and response differ.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — CIDP often causes neuropathic pain alongside its hallmark weakness: demyelination and secondary axonal damage of sensory fibers produce burning, tingling and sensory ataxia, so beyond immunotherapy (IVIG, steroids) patients frequently need gabapentinoids or SNRIs for the pain.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Plasma cells underlie much of CIDP's autoimmunity: long-lived plasma cells secrete IgG antibodies that, with complement and macrophages, strip myelin from peripheral nerves—so IVIG, plasma exchange, and B-cell-targeting therapies are mainstays.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Regulatory T-cell failure permits CIDP: when Tregs cannot restrain autoreactive T and B cells, the immune system attacks peripheral-nerve myelin, so CIDP is treated by rebalancing immunity (steroids, IVIG)—immune dysregulation drives chronic demyelination.
- `connects-to` → **[NMOSD](../nmo/README.md)** — CIDP and neuromyelitis optica are both antibody-mediated demyelinating diseases at different sites: CIDP attacks peripheral-nerve myelin (areflexia, sensorimotor loss), while NMO attacks CNS astrocytes/myelin via anti-AQP4—both IgG-driven and treated with immunotherapy.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — T helper cells help drive the autoimmune attack in CIDP: activated T cells breach the blood-nerve barrier and, with macrophages and antibodies, strip myelin from peripheral nerves—so immunosuppression, IVIG and plasma exchange restore conduction.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement amplifies nerve damage in CIDP: antibodies against myelin or nodal proteins fix complement on peripheral nerves, recruiting macrophages to demyelinate—so complement and the antibodies behind it are why IVIG and plasma exchange, which remove them, work.
- `connects-to` → **[Type 1 Diabetes](../type-1-diabetes/README.md)** — CIDP must be distinguished from diabetic neuropathy: diabetes both mimics and predisposes to CIDP, so a diabetic with disproportionate, treatable demyelinating weakness may have CIDP rather than ordinary diabetic polyneuropathy—a crucial, treatable distinction.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — CIDP attacks the insulation of peripheral neurons: immune-mediated stripping of myelin from motor and sensory nerve fibers slows or blocks conduction, causing the progressive weakness and numbness that, unlike Guillain-Barré, persist or relapse over months.
- `connects-to` → **[Immune System](../immune-system/README.md)** — CIDP is an autoimmune disease of peripheral nerves: antibodies, complement and T cells attack myelin, so it responds to immunotherapy (IVIG, steroids, plasma exchange)—the treatable, chronic counterpart of Guillain-Barré syndrome.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — CIDP is a chronic disorder of the peripheral nervous system: demyelination of nerve roots and trunks impairs the signals between cord and limbs, producing symmetric weakness and sensory loss that can be reversed if immunotherapy starts before axons are lost.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement helps strip myelin in CIDP: antibodies against nerve antigens fix complement (C3 and beyond), and macrophages then peel myelin off axons, so complement activation is part of the demyelinating attack that IVIg and plasma exchange interrupt.
- `connects-to` → **[Waldenström Macroglobulinemia](../waldenstrom-macroglobulinemia/README.md)** — A CIDP-like neuropathy can signal a paraprotein: anti-MAG IgM from Waldenström macroglobulinemia or MGUS attacks myelin, producing a demyelinating neuropathy that mimics CIDP—so an unexplained case warrants checking for a monoclonal protein.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — CIDP is driven partly by T cells: cytotoxic and helper T cells breach the blood-nerve barrier and, with macrophages, attack peripheral myelin, so the disease reflects a cellular as well as antibody-mediated assault on nerves.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — CIDP responds to corticosteroids—unlike its acute cousin: steroids that mimic cortisol calm the autoimmune attack on peripheral myelin and are first-line in CIDP, a key contrast with Guillain-Barré, where steroids fail and only IVIG or plasma exchange help.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — CIDP begins with dendritic cells presenting myelin: these antigen-presenting cells display peripheral-nerve proteins to T cells, breaking tolerance and launching the chronic immune attack that strips myelin from the nerves.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — Refractory CIDP can be treated by deleting B cells via CD20: rituximab targets this B-cell marker to shut down antibody production, especially effective in CIDP variants driven by antibodies against nodal proteins or MAG.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — CIDP cripples nerve conduction at the sodium channels: myelin loss disperses the sodium channels clustered at the nodes of Ranvier, so the saltatory jump of the impulse fails, producing the conduction block behind the weakness.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Demyelination in CIDP exposes potassium channels: stripped of myelin, the juxtaparanodal potassium channels normally hidden under it leak current and dampen the nerve impulse, worsening conduction failure—a target of channel-blocking drugs.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Macrophages strip myelin in CIDP under NF-kB's command: this inflammatory switch drives the cytokines and activation that send macrophages to peel myelin off peripheral nerves, the core attack that immunosuppression aims to halt.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — CIDP can travel with kidney disease: it sometimes co-occurs with membranous nephropathy, the two sharing autoantibodies against nodal proteins like neurofascin and contactin, linking the leaky kidney filter to the demyelinated nerve.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — In POEMS syndrome, VEGF drives a CIDP-like neuropathy: this rare plasma-cell disorder floods the blood with VEGF, producing a demyelinating polyneuropathy that mimics CIDP but needs entirely different, anti-plasma-cell treatment.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Chronic CIDP damage is sealed by calcium: when long demyelination finally lets axons degenerate, calcium pours into the bare fibers and executes their death, the irreversible loss behind lasting disability.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Imaging supports the CIDP diagnosis: MRI photons reveal the thickened, enhancing nerve roots and plexuses, and nerve ultrasound shows the enlarged nerves of this demyelinating disease.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Some CIDP is driven from the marrow: a monoclonal plasma-cell clone (an IgM MGUS, often anti-MAG) makes antibodies that attack peripheral myelin, a paraproteinemic neuropathy needing marrow-directed treatment.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Inflammatory cytokines sustain CIDP: IL-6 and its kin help drive the autoimmune attack on myelin, keeping the demyelination smoldering and offering a target for newer immunomodulatory therapies.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows CIDP's repeated injury: round after round of demyelination and repair leaves Schwann cells wrapped in concentric 'onion-bulb' whorls around the axon, the hallmark of a chronic, relapsing nerve attack.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Severe CIDP can reach the breathing muscles: when the demyelination involves the nerves driving the diaphragm, respiratory weakness develops, the rare but dangerous extension that can require ventilatory support.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Some CIDP variants strike the cranial nerves: involvement of the nerves controlling eye movement causes double vision and drooping, broadening the disease beyond the limbs in its atypical forms.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^vanlaar-2010-efns-cidp]: European Federation of Neurological Societies/Peripheral Nerve Society. Guideline on management of CIDP. *J Peripher Nerv Syst.* 2010;15(1):1-9. [doi:10.1111/j.1529-8027.2010.00238.x](https://doi.org/10.1111/j.1529-8027.2010.00238.x) · [PubMed 20433600](https://pubmed.ncbi.nlm.nih.gov/20433600/)
[^merkies-2008-ivig-ice]: Hughes RA, et al. Intravenous immune globulin for CIDP (ICE study). *Lancet Neurol.* 2008;7(2):136-144. [doi:10.1016/S1474-4422(07)70329-0](https://doi.org/10.1016/S1474-4422(07)70329-0) · [PubMed 18178525](https://pubmed.ncbi.nlm.nih.gov/18178525/)
[^vandenberheijde-2023-efgartigimod-cidp]: van den Bergh PYK, et al. Efgartigimod alfa and hyaluronidase-qvfc in CIDP (ADHERE). *N Engl J Med.* 2023;390(3):219-232. [doi:10.1056/NEJMoa2310819](https://doi.org/10.1056/NEJMoa2310819) · [PubMed 38197812](https://pubmed.ncbi.nlm.nih.gov/38197812/)
[^van-den-bergh-2023-cidp-guidelines]: Van den Bergh PYK, et al. EAN/PNS guideline on CIDP: 2023 update. *Eur J Neurol.* 2023;30(10):2976-3020. [doi:10.1111/ene.15927](https://doi.org/10.1111/ene.15927) · [PubMed 37382198](https://pubmed.ncbi.nlm.nih.gov/37382198/)

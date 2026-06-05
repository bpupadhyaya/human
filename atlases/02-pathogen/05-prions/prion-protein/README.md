---
schema: pathogen-entry/v1
id: prion-protein
name: Prion Protein
atlas: 02-pathogen
scale: 05-prions
status: draft
last_reviewed: 2026-06-05
summary: "Prion protein: PrPC (normal, α-helical) vs. PrPSc (pathological, β-sheet-rich). PrPSc propagates by templating PrPC misfolding; resists protease, heat, formalin. Causes CJD, kuru, FFI, GSS. 100% fatality. No nucleic acid genome; pure protein pathogen."
aliases: ["PrP", "prion", "PrPSc", "PrPC", "scrapie prion", "misfolded prion"]
sources:
  - id: prusiner-1998-nobel
    type: peer-reviewed
    cite: "Prusiner SB. Nobel lecture: prions. Proc Natl Acad Sci USA. 1998;95(23):13363-83."
    doi: "10.1073/pnas.95.23.13363"
    pmid: "9811807"
    url: "https://doi.org/10.1073/pnas.95.23.13363"
  - id: collinge-2001-prion-disease
    type: peer-reviewed
    cite: "Collinge J. Prion diseases of humans and animals: their causes and molecular basis. Annu Rev Neurosci. 2001;24:519-50."
    doi: "10.1146/annurev.neuro.24.1.519"
    pmid: "11283320"
    url: "https://doi.org/10.1146/annurev.neuro.24.1.519"
  - id: aguzzi-2009-prion-aggregation
    type: peer-reviewed
    cite: "Aguzzi A, Calella AM. Prions: protein aggregation and infectious diseases. Physiol Rev. 2009;89(4):1105-52."
    doi: "10.1152/physrev.00006.2009"
    pmid: "19789378"
    url: "https://doi.org/10.1152/physrev.00006.2009"
cross_links:
  - target: 01-human/04-cellular/neuron
    relation: damages
    note: "PrPSc accumulates as amyloid plaques and vacuoles in grey matter neurons → spongiform encephalopathy → neuronal death. Neurons are the primary site of prion replication and PrPSc deposition. Vacuolar (spongiform) change reflects neuronal swelling and death. The process is universally fatal."
  - target: 01-human/06-organ/brain
    relation: damages
    note: "Progressive spongiform degeneration, reactive astrogliosis, and neuronal loss throughout the brain — particularly cerebral cortex, basal ganglia, thalamus, and cerebellum — lead to universally fatal dementia and motor failure. Distribution of lesions varies by prion strain and disease subtype."
---

# Prion Protein

## Overview

The **prion** (proteinaceous infectious particle) represents the most radical reductionist infectious agent ever identified — a **pathogen composed exclusively of misfolded protein** with no nucleic acid genome. The central principle of prion biology, established by Stanley Prusiner and colleagues and recognised by the 1997 Nobel Prize in Physiology or Medicine, is the **protein-only hypothesis**: a misfolded isoform of a normal host protein (PrP^Sc) can propagate itself by recruiting and converting the normal host protein (PrP^C) to its own aberrant conformation [^prusiner-1998-nobel].

The prion protein gene (*PRNP*, chromosome 20p13) is expressed ubiquitously in all mammalian cells, with highest expression in neurons. The normal cellular prion protein (PrP^C) is a GPI-anchored cell-surface glycoprotein with largely α-helical structure. PrP^Sc — the scrapie or pathological isoform — has an abnormally high β-sheet content, forms insoluble aggregates, resists protease digestion (proteinase K-resistant PrP, PrP^res), and most critically, is **self-propagating**: it acts as a structural template to convert newly synthesised PrP^C molecules to PrP^Sc [^aguzzi-2009-prion-aggregation].

Human prion diseases (**transmissible spongiform encephalopathies, TSEs**) are invariably fatal, typically within weeks to months of symptom onset. They include:
- **Sporadic CJD (sCJD):** Most common (~85% of human prion disease); cause unknown; incidence ~1–2/million/year worldwide
- **Iatrogenic CJD (iCJD):** Transmitted via contaminated surgical instruments, dura mater grafts, human growth hormone (cadaveric)
- **Variant CJD (vCJD):** Acquired by consumption of BSE-contaminated beef; identified in UK epidemic 1995–2004; ~230 total cases globally
- **Genetic CJD, Gerstmann-Sträussler-Scheinker syndrome (GSS), Fatal Familial Insomnia (FFI):** Autosomal dominant *PRNP* mutations
- **Kuru:** Epidemic prion disease of the Fore people of Papua New Guinea; transmitted by ritual mortuary cannibalism; now effectively extinct

## Structure

### PrP^C — Normal Cellular Prion Protein

PrP^C is a **253-amino acid (AA) glycoprotein** (after signal peptide cleavage and GPI addition: mature form 208 AA):

| Domain | Residues | Structure | Function |
|:---|:---|:---|:---|
| **N-terminal flexible tail** | 23–124 | Unstructured; contains octapeptide repeats (PHGGGWGQ × 4–5) | Cu²⁺ binding; endosomal trafficking |
| **Hydrophobic core** | 112–134 | α-helical tendency | Signal for membrane anchoring or transmembrane form |
| **Globular C-terminal domain** | 125–231 | Three α-helices (H1, H2, H3), two short antiparallel β-strands (S1, S2), one disulphide bond (Cys179-Cys214) | Core folded domain; site of pathological refolding |
| **GPI anchor attachment** | 231 | C-terminal signal cleaved; GPI added | Cell surface anchoring (lipid raft association) |

Two N-glycosylation sites at Asn181 and Asn197. PrP^C is found in lipid rafts, is endocytosed and recycled, and has proposed (but debated) functions in copper homeostasis, neuroprotection, and cell signalling.

### PrP^Sc — Pathological Prion Isoform

PrP^Sc is **identical in primary amino acid sequence** to PrP^C — differing only in **three-dimensional conformation**:

| Property | PrP^C | PrP^Sc |
|:---|:---|:---|
| **Secondary structure** | ~42% α-helix, ~3% β-sheet | ~30% α-helix, ~43% β-sheet |
| **Solubility** | Soluble in non-denaturing detergents | Insoluble; forms aggregates |
| **Protease K sensitivity** | Fully degraded | Partially resistant (PrP 27-30 kDa core) |
| **Thermal stability** | Denatured at standard cooking temperatures | Requires >134°C/3h autoclave for inactivation |
| **Chemical stability** | Standard fixatives (formalin) inactivate | **Formalin-resistant; formaldehyde fixation PRESERVES infectivity** |
| **Self-propagating** | No | Yes — templates conversion of PrP^C |

### Prion Strains

Different prion strains are encoded by **distinct PrP^Sc conformations** (not by nucleic acid sequences), accounting for:
- Different incubation periods in the same host
- Different lesion distribution patterns (lesion profile) in the brain
- Different glycoform ratios (ratio of di/mono/non-glycosylated PrP^Sc on Western blot)
- Different cross-species transmission barriers

## Infection Mechanism

### The Protein-Only Conversion Mechanism

The core mechanism of prion propagation is **nucleated polymerisation** or **template-directed refolding** [^prusiner-1998-nobel]:

1. **Seeding:** A PrP^Sc molecule (seed/nucleus) physically contacts PrP^C
2. **Conformational templating:** The PrP^Sc template induces refolding of the contacted PrP^C molecule — shifting α-helices to β-strands through a proposed PrP^Sc:PrP^C heterodimer intermediate
3. **Fibril elongation:** The newly converted PrP^Sc joins the growing aggregate; insoluble PrP^Sc fibrils grow by continued accretion of converted PrP^C monomers
4. **Fragmentation and propagation:** Fibril fragmentation produces new seeding nuclei; exponential amplification of PrP^Sc occurs after a variable lag phase
5. **Cellular dysfunction and death:** PrP^Sc accumulates beyond proteasomal clearance capacity; oligomeric intermediates (pre-fibril aggregates) may be the primary neurotoxic species

The conversion is thermodynamically driven: PrP^Sc is the more thermodynamically stable form under physiological conditions, but the energy barrier to spontaneous PrP^C → PrP^Sc conversion is high, preventing constant spontaneous disease. PrP^Sc seeds dramatically lower this activation barrier.

### Routes of Transmission

| Route | Example Disease | Mechanism |
|:---|:---|:---|
| **Sporadic (de novo)** | sCJD | Spontaneous stochastic PrP^C misfolding (~1/million/year); possibly accelerated by *PRNP* codon 129 polymorphism |
| **Genetic (germline mutation)** | Familial CJD, GSS, FFI | *PRNP* mutations lower the energy barrier to PrP^Sc formation (e.g., D178N + M129 = FFI; D178N + V129 = familial CJD; P102L = GSS) |
| **Iatrogenic** | iCJD | Prion-contaminated neurosurgical instruments; dura mater grafts; cadaveric pituitary-derived growth hormone; corneal transplants |
| **Oral/dietary** | vCJD, kuru | Ingested prions survive gastric digestion; taken up by Peyer's patches → follicular dendritic cells (lymphoid system) → peripheral nerves → CNS |
| **Blood transfusion** | vCJD (4 confirmed UK cases) | PrP^Sc in buffy coat from pre-symptomatic vCJD donors |

### Neuroinvasion

After peripheral exposure (oral or parenteral), prions must reach the CNS. The neuroinvasion pathway is best characterised for vCJD/BSE:

1. **Gut lymphoid tissue:** Prions enter via M cells overlying Peyer's patches → FDCs (follicular dendritic cells) in germinal centres replicate prions (FDCs express PrP^C and seem required for lymphoid amplification)
2. **Peripheral nervous system:** From lymphoid tissue, prions spread to enteric nervous system → vagus nerve → CNS
3. **CNS spread:** Once in the brain, prion propagation spreads by axonal transport along anatomically connected pathways — the distribution of PrP^Sc deposition reflects this synaptic network spread

## Host Interactions

### No Immune Recognition

A defining — and therapeutically devastating — feature of prion disease is the **absence of effective immune recognition**:
- PrP^Sc is a self-protein (same primary sequence as PrP^C); the immune system recognises it as self and does not mount humoral or cellular responses
- No antibody response, no T-cell response, no inflammation in early disease
- The CNS lacks peripheral immune surveillance; PrP^Sc accumulates silently for months to decades before clinical symptoms

### Neuropathological Cascade

The downstream mechanisms of neuronal death in prion disease remain incompletely understood:

| Mechanism | Evidence |
|:---|:---|
| **PrP^Sc toxicity** | PrP^Sc aggregates impair synaptic function; disrupt axonal transport; activate UPR (unfolded protein response) → chronic ER stress → PERK-eIF2α-ATF4 signalling → inhibition of global protein synthesis → neuronal death |
| **Synaptic dysfunction** | PrP^Sc oligomers bind and impair synaptic vesicle cycling; loss of PrP^C from synaptic sites (which normally facilitates glutamate signalling) contributes to dysfunction before cell death |
| **Glial response** | Reactive astrocytosis and microglial activation are prominent (non-specific response to neuronal death); activated microglia may amplify neurodegeneration via TNF-α and ROS production |
| **Vacuolation (spongiform change)** | Intraneuronal vacuoles; origin: abnormal intracellular trafficking; cytoplasmic vacuolation precedes neuronal death by weeks |
| **Loss of PrP^C function** | PrP^C may normally protect neurons from oxidative stress (Cu²⁺ buffering) and regulate NMDA receptor signalling; loss from cell surface as it is converted to PrP^Sc may deprive neurons of protective signalling |

### Prion Strain-Host Interactions

The **species barrier** (or transmission barrier) determines cross-species prion transmission efficiency. It is determined by:
- **Sequence homology** between donor PrP^Sc and recipient PrP^C
- **Prion strain conformation** — some strains adapt more readily to new host PrP sequences
- *PRNP* codon 129 polymorphism (Met/Val) in humans: all vCJD patients in the UK epidemic were MM homozygous at codon 129 (population frequency ~40%); MV and VV homozygotes may have longer incubation periods or relative resistance

## Connections

**Damages** → [Neuron](../../../01-human/04-cellular/neuron/README.md): PrP^Sc accumulates in neuronal cytoplasm and extracellular space as amyloid plaques (in GSS and vCJD with florid plaques) and intraneuronal aggregates. Vacuolation (spongiform change) is the pathological hallmark at the neuronal level — swollen neuronal processes and cell bodies progress to neuronal dropout, leaving sponge-like voids in grey matter. This process is 100% lethal within the affected neuron population.

**Damages** → [Brain](../../../01-human/06-organ/brain/README.md): Progressive spongiform degeneration spreads through anatomically connected brain regions. In sCJD the cortex, basal ganglia, and cerebellum are most affected; in FFI the thalamus is selectively devastated (fatal insomnia); in vCJD the posterior thalamus and pulvinar show florid plaques. Reactive astrogliosis is universal; macroscopic brain atrophy develops in surviving patients with longer disease courses (GSS).

## Pathology

### Human Prion Diseases

| Disease | Cause | Key Features | Survival |
|:---|:---|:---|:---|
| **Sporadic CJD (sCJD)** | Unknown de novo PrP^C misfolding | Rapidly progressive dementia; myoclonus; cerebellar ataxia; cortical ribboning (DWI-MRI); 14-3-3 protein in CSF; MM codon 129 most common | Median 4–6 months; 90% dead by 1 year |
| **Variant CJD (vCJD)** | BSE prion ingestion | Young adults (mean age 26 vs. >60 for sCJD); psychiatric prodrome (6 months); painful dysaesthesiae; pulvinar sign (MRI); florid plaques (neuropathology); MM codon 129 in all confirmed UK cases | Median 13–14 months |
| **Fatal Familial Insomnia (FFI)** | *PRNP* D178N + M129 mutation | Intractable insomnia → autonomic dysfunction → dementia → coma; severe selective thalamic neuronal loss; PET shows thalamic hypometabolism | 12–18 months |
| **Gerstmann-Sträussler-Scheinker (GSS)** | *PRNP* P102L and other mutations | Cerebellar ataxia preceding dementia by years; widespread multicentric plaques; longer course than sCJD | 2–10 years |
| **Kuru** | Ritual cannibalism (Fore people, PNG) | Cerebellar > cerebral presentation; "shivering disease"; kuru plaques; epidemic peaked 1950s–60s | 3–24 months; cases now extremely rare |
| **Familial CJD** | Multiple *PRNP* mutations (E200K most common) | Clinically similar to sCJD; E200K prevalent in Libyan Jews and Slovaks | Months |

### Diagnosis

No validated ante-mortem diagnostic test identifies prion disease definitively — diagnosis remains primarily neuropathological. Best current ante-mortem tools:
- **RT-QuIC (real-time quaking-induced conversion):** Amplifies PrP^Sc in CSF or olfactory mucosa brush biopsy using recombinant PrP substrate; sensitivity ~90–95%, specificity ~98% for sCJD — now the reference test at prion disease centres
- **CSF 14-3-3 protein:** Non-specific marker of rapid neuronal death; sensitivity ~85% for sCJD, low specificity
- **MRI DWI (diffusion-weighted):** Cortical ribboning, basal ganglia and thalamic restricted diffusion — sensitivity/specificity ~90%/90% for sCJD; pulvinar sign in vCJD
- **EEG:** Periodic sharp wave complexes (PSWCs) in sCJD (~66% sensitivity); absent in vCJD
- **Neuropathology:** PrP^Sc immunohistochemistry on fixed brain tissue (formalin — **preserves** prion infectivity; requires special biosafety handling)

### No Treatment Exists

As of 2026, there is **no disease-modifying treatment** for any human prion disease. Prion diseases are uniformly and rapidly fatal after symptom onset. Experimental approaches under investigation include:
- Anti-PrP antibodies (passive immunotherapy): murine anti-PrP monoclonal antibodies; clinical translation hampered by PrP^C expression in peripheral tissues and potential toxicity from PrP^C depletion at the synapse
- ASO (antisense oligonucleotide)-mediated *PRNP* knockdown: Ionis/Prion Alliance programme; has extended survival in mouse models by >2-fold; Phase I trial recently initiated
- Small molecule stabilisers of PrP^C α-helical fold (e.g., IND24 class compounds): active in animal models
- Decontamination: Prion-contaminated instruments require **extended porous load autoclave (134°C, 18–30 min)**, NaOH, or sodium hypochlorite — standard hospital sterilisation is **insufficient**

[^prusiner-1998-nobel]: Prusiner SB. Nobel lecture: prions. *Proc Natl Acad Sci USA.* 1998;95(23):13363-83. [doi:10.1073/pnas.95.23.13363](https://doi.org/10.1073/pnas.95.23.13363) · [PubMed 9811807](https://pubmed.ncbi.nlm.nih.gov/9811807/)
[^collinge-2001-prion-disease]: Collinge J. Prion diseases of humans and animals: their causes and molecular basis. *Annu Rev Neurosci.* 2001;24:519-50. [doi:10.1146/annurev.neuro.24.1.519](https://doi.org/10.1146/annurev.neuro.24.1.519) · [PubMed 11283320](https://pubmed.ncbi.nlm.nih.gov/11283320/)
[^aguzzi-2009-prion-aggregation]: Aguzzi A, Calella AM. Prions: protein aggregation and infectious diseases. *Physiol Rev.* 2009;89(4):1105-52. [doi:10.1152/physrev.00006.2009](https://doi.org/10.1152/physrev.00006.2009) · [PubMed 19789378](https://pubmed.ncbi.nlm.nih.gov/19789378/)

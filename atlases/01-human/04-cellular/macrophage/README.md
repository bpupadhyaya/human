---
schema: human-scale-entry/v1
id: macrophage
name: Macrophage
atlas: 01-human
scale: 04-cellular
status: draft
last_reviewed: 2026-06-05
summary: "Professional phagocyte and innate immune effector. Derived from monocytes; tissue-resident forms include Kupffer cells (liver), microglia (brain), alveolar macrophages (lung). Phagocytoses pathogens and apoptotic cells; secretes IL-6, TNF-α, and ROS upon TLR/NLR activation."
aliases: ["tissue macrophage", "Kupffer cell", "microglia", "alveolar macrophage", "M1 macrophage", "M2 macrophage"]
sources:
  - id: gordon-2016-phagocytosis
    type: peer-reviewed
    cite: "Gordon S. Phagocytosis: an immunobiologic process. Immunity. 2016;44(3):463-75."
    doi: "10.1016/j.immuni.2016.02.026"
    pmid: "27002634"
    url: "https://doi.org/10.1016/j.immuni.2016.02.026"
  - id: ginhoux-2016-macrophage-ontogeny
    type: peer-reviewed
    cite: "Ginhoux F, Guilliams M. Tissue-resident macrophage ontogeny and homeostasis. Immunity. 2016;44(3):439-49."
    doi: "10.1016/j.immuni.2016.02.024"
    pmid: "27002631"
    url: "https://doi.org/10.1016/j.immuni.2016.02.024"
  - id: murray-2017-macrophage-activation
    type: peer-reviewed
    cite: "Murray PJ. Macrophage polarization. Annu Rev Physiol. 2017;79:541-66."
    doi: "10.1146/annurev-physiol-022516-034339"
    pmid: "27813830"
    url: "https://doi.org/10.1146/annurev-physiol-022516-034339"
  - id: mantovani-2013-macrophage-plasticity
    type: peer-reviewed
    cite: "Mantovani A, Biswas SK, Galdiero MR, et al. Macrophage plasticity and polarization in tissue repair and remodelling. J Pathol. 2013;229(2):176-85."
    doi: "10.1002/path.4133"
    pmid: "23096265"
    url: "https://doi.org/10.1002/path.4133"
cross_links:
  - target: 01-human/07-system/immune-system
    relation: part-of
    note: "Macrophages are central cellular effectors of the innate immune system, present in virtually every tissue."
  - target: 01-human/03-molecular/il-6
    relation: expresses
    note: "Macrophages are major IL-6 producers upon TLR4 (LPS) and NLR (NLRP3) activation; IL-6 drives acute-phase response and T-cell differentiation."
  - target: 01-human/03-molecular/tnf-alpha
    relation: expresses
    note: "TNF-α is the canonical macrophage/monocyte cytokine — its name derives from macrophage-mediated tumor necrosis; released via NF-κB signalling downstream of TLR stimulation."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: expresses
    note: "Macrophages are professional antigen-presenting cells (APCs) expressing constitutive MHC-II; present processed peptides to CD4⁺ T-helper cells."
  - target: 01-human/04-cellular/hepatocyte
    relation: damages
    note: "Activated Kupffer cells (liver-resident macrophages) secrete ROS, TNF-α, and IL-6, driving hepatocyte apoptosis and steatohepatitis in NAFLD/NASH progression."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: part-of
    note: "Kupffer cells are the liver-resident macrophage population, lining hepatic sinusoids within each hepatic lobule."
  - target: 01-human/06-organ/liver
    relation: part-of
    note: "Kupffer cells constitute ~15% of total hepatic cells and represent the largest pool of tissue-resident macrophages in the body."
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "Macrophages are ubiquitous; estimated 10¹¹ macrophages populate the adult human body across all major organs."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: modulated-by
    evidence: gordon-2016-phagocytosis
    note: "NK cells stimulate macrophage M1 activation via IFN-γ and suppress M2 polarisation; NK-derived GM-CSF promotes macrophage survival."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: modulated-by
    evidence: murray-2017-macrophage-activation
    note: "Intestinal epithelial cells secrete IL-10 and TGF-β that polarise mucosal macrophages toward tolerogenic M2-like phenotype."
  - target: 01-human/05-tissue/bone-marrow
    relation: part-of
    evidence: ginhoux-2016-macrophage-ontogeny
    note: "Bone marrow monocyte progenitors (cMoPs from GMPs) give rise to circulating monocytes that seed tissues and differentiate into resident macrophages."
  - target: 01-human/03-molecular/stat3
    relation: modulated-by
    evidence: murray-2017-macrophage-activation
    note: "STAT3 downstream of IL-10 and IL-6 drives macrophage M2-like polarisation and suppresses M1 pro-inflammatory gene expression; tumour-associated macrophage STAT3 constitutive activity sustains immunosuppressive TME."
  - target: 01-human/03-molecular/nf-kb
    relation: modulated-by
    evidence: murray-2017-macrophage-activation
    note: "NF-κB p65/p50 is the master transcriptional driver of macrophage M1 polarisation: LPS→TLR4→MyD88/TRIF→IKKβ→NF-κB drives TNF-α, IL-6, IL-12, and iNOS expression in activated macrophages."
  - target: 01-human/06-organ/spleen
    relation: part-of
    evidence: ginhoux-2016-macrophage-ontogeny
    note: "Splenic red pulp macrophages phagocytose senescent erythrocytes and recycle haem iron; marginal zone macrophages clear encapsulated bacteria; both populations derive from blood monocytes seeding the spleen."
  - target: 01-human/03-molecular/complement-c3
    relation: modulated-by
    note: "Modulated by Complement C3."
  - target: 01-human/03-molecular/nitric-oxide
    relation: modulated-by
    note: "Modulated by Nitric Oxide."
  - target: 01-human/03-molecular/histamine
    relation: modulated-by
    note: "Modulated by Histamine."
  - target: 01-human/03-molecular/prostaglandins
    relation: expressed-by
    note: "Expressed by Prostaglandins (Eicosanoids)."
  - target: 01-human/05-tissue/arterial-wall
    relation: modulated-by
    note: "Modulated by Arterial Wall."
  - target: 01-human/04-cellular/neutrophil
    relation: modulated-by
    note: "Modulated by Neutrophil."
  - target: 01-human/04-cellular/osteoclast
    relation: modulated-by
    note: "Modulated by Osteoclast."
  - target: 01-human/04-cellular/endothelial-cell
    relation: modulated-by
    note: "Modulated by Endothelial Cell."
  - target: 01-human/04-cellular/platelet
    relation: modulated-by
    note: "Modulated by Platelet."
  - target: 02-pathogen/01-viruses/ebola-virus
    relation: infected-by
    note: "Infected by Ebola Virus (EBOV)."
  - target: 02-pathogen/01-viruses/rotavirus
    relation: damaged-by
    note: "Damaged by Rotavirus."
  - target: 02-pathogen/06-microbiome/akkermansia-muciniphila
    relation: modulated-by
    note: "Modulated by Akkermansia muciniphila."
  - target: 02-pathogen/03-fungi/cryptococcus-neoformans
    relation: damaged-by
    note: "Damaged by Cryptococcus neoformans."
  - target: 02-pathogen/04-parasites/trypanosoma-brucei
    relation: damaged-by
    note: "Damaged by Trypanosoma brucei."
  - target: 02-pathogen/04-parasites/trypanosoma-cruzi
    relation: damaged-by
    note: "Damaged by Trypanosoma cruzi."
  - target: 02-pathogen/04-parasites/toxoplasma-gondii
    relation: damaged-by
    note: "Damaged by Toxoplasma gondii."
  - target: 02-pathogen/04-parasites/leishmania-donovani
    relation: infected-by
    note: "Infected by Leishmania donovani."
  - target: 02-pathogen/02-bacteria/salmonella-typhi
    relation: damaged-by
    note: "Damaged by Salmonella typhi."
  - target: 02-pathogen/02-bacteria/listeria-monocytogenes
    relation: damaged-by
    note: "Damaged by Listeria monocytogenes."
  - target: 02-pathogen/02-bacteria/helicobacter-pylori
    relation: damaged-by
    note: "Damaged by Helicobacter pylori."
  - target: 03-medicine/03-food/resveratrol
    relation: modulated-by
    note: "Modulated by Resveratrol."
  - target: 03-medicine/03-food/quercetin
    relation: modulated-by
    note: "Modulated by Quercetin."
  - target: 01-human/07-system/familial-hypercholesterolemia
    relation: connects-to
    note: "In FH, chronically elevated LDL-C → macrophage scavenger receptor (SR-A, CD36) uptake of oxidized LDL → foam cell formation; foam cells are the histological hallmark of the atheromatous plaque; FH macrophages exhibit exaggerated ox-LDL uptake vs. normolipidemic controls."
---

# Macrophage

## Overview

Macrophages are long-lived, tissue-resident phagocytes and innate immune effectors that form the first line of defense against pathogens, coordinate inflammation, and maintain tissue homeostasis through continuous surveillance and clearance of apoptotic cells, cellular debris, and foreign material. The name derives from Greek *makros* (large) + *phagein* (to eat), reflecting their defining property of phagocytosis.

In adult humans, macrophages exist in two principal pools: (1) monocyte-derived macrophages that differentiate from circulating Ly6C⁺ classical monocytes following tissue infiltration, and (2) tissue-resident macrophages (TRMs) seeded during embryonic development from yolk-sac progenitors and fetal liver monocytes. TRMs self-renew locally and are remarkably long-lived; Kupffer cells (liver), microglia (CNS), Langerhans cells (skin), and alveolar macrophages (lung) are paradigmatic examples. This ontological duality — embryonic vs. monocyte-derived — profoundly shapes functional identity.

The adult human body harbours an estimated 10¹¹ macrophages. In steady state, macrophages perform constitutive efferocytosis (clearance of ~2×10¹¹ senescent erythrocytes per day), pattern-recognition surveillance via Toll-like receptors (TLRs 1–9), NOD-like receptors (NLRs), scavenger receptors (SR-A, CD36), and complement receptors (CR1, CR3).

## Structure

**Size and morphology.** Macrophages range from 10–30 µm in diameter depending on activation state. Resting tissue macrophages display a rounded or dendriform morphology with abundant cytoplasm and elongated pseudopodia. Activated macrophages spread widely on substrates, with prominent lamellipodia and numerous surface ruffles.

**Nucleus.** A single, often kidney-shaped nucleus with dispersed chromatin; accessible chromatin at inflammatory gene loci (e.g., *Il6*, *Tnf*, *Il1b*) allows rapid transcriptional activation within minutes of pattern-recognition receptor (PRR) engagement.

**Organelles.** Macrophages are rich in lysosomes (pH 4.5–5.0) containing cathepsins, hydrolases, and the NADPH oxidase complex (gp91ᵖʰᵒˣ + p22ᵖʰᵒˣ + p47ᵖʰᵒˣ + p67ᵖʰᵒˣ + p40ᵖʰᵒˣ + Rac2) responsible for the oxidative burst. The rough ER is well developed, supporting high-volume cytokine synthesis. Mitochondria undergo dynamic reprogramming during polarisation: M1-like macrophages shift to aerobic glycolysis (Warburg-like) with fragmented mitochondria and broken TCA cycle (succinate accumulation drives HIF-1α → IL-1β).

**Surface receptors.** Key surface molecules include: CD14 (LPS co-receptor), CD11b/CD18 (Mac-1, complement receptor 3), CD16 (FcγRIII), CD64 (FcγRI), CD163 (haemoglobin scavenger), CD206 (mannose receptor), CD86/CD80 (co-stimulatory, upregulated in M1), MHC-II (constitutive in professional APCs), and CX₃CR1 (fractalkine receptor, tissue patrol).

## Function

**Phagocytosis.** Upon PRR engagement or opsonisation (IgG-FcγR, C3b-CR3), macrophages extend pseudopodia around targets and internalise them into phagosomes (0.5–10 µm). Phagosome–lysosome fusion creates a phagolysosome in which the NADPH oxidase generates superoxide (O₂•⁻), subsequently dismutated to H₂O₂ and hypochlorous acid (HOCl via myeloperoxidase). Nitric oxide synthase 2 (iNOS/NOS2) produces NO in M1 macrophages, forming peroxynitrite (ONOO⁻), a potent microbicide.

**Cytokine secretion.** TLR4 stimulation by lipopolysaccharide (LPS) activates MyD88 → IRAK4 → TRAF6 → NF-κB and MAPK cascades, driving transcription of *TNF*, *IL6*, *IL1B*, *IL12A/B*, *CXCL8* within 30–60 minutes. TNF-α and IL-1β act locally and systemically to amplify inflammation. IL-12 and IL-18 synergise to activate NK cells and drive Th1 polarisation.

**Polarisation (M1/M2 spectrum).** Classical activation (M1): IFN-γ + LPS → STAT1-driven pro-inflammatory phenotype; high iNOS, IL-12, IL-23, TNF-α, low IL-10. Alternative activation (M2): IL-4/IL-13 → STAT6-driven anti-inflammatory/tissue-repair phenotype; high arginase-1 (Arg1), IL-10, TGF-β, CD206; supports wound healing and helminth responses. Real-world macrophages exist on a continuum; the dichotomy is a simplification.

**Antigen presentation.** After phagocytosis, peptides are loaded onto MHC-II molecules and transported to the cell surface. MHC-II–peptide–CD86 complexes are recognised by CD4⁺ T-helper cells, linking innate and adaptive immunity. Cross-presentation of exogenous antigens on MHC-I also occurs, enabling CD8⁺ T-cell priming.

**Tissue homeostasis.** Kupffer cells clear immune complexes and gut-derived LPS from portal blood, preventing systemic endotoxaemia. Alveolar macrophages clear surfactant and inhaled particles. Osteoclasts (monocyte/macrophage lineage) remodel bone matrix. Microglia perform synaptic pruning during development and clearance of amyloid-β in ageing.

## Lifecycle

Macrophages arise from two lineages:

1. **Embryonic lineage (TRMs):** Primitive myeloid progenitors emerge from the yolk sac (~E6.5 in mouse); a second wave from fetal liver monocytes (~E12.5) colonises most organs. These seed tissue-resident populations that persist lifelong through local proliferation (Ki67⁺; driven by CSF1, IL-4).

2. **Monocyte-derived lineage:** In adults, bone-marrow-derived common myeloid progenitors (CMPs) → granulocyte-monocyte progenitors (GMPs) → monocytes. Classical (Ly6C⁺/CD14⁺⁺CD16⁻) monocytes patrol blood for ~1–3 days before transmigrating into tissues during inflammation. Non-classical (Ly6C⁻/CD14⁺CD16⁺⁺) monocytes crawl luminal surfaces of capillaries and are recruited later.

Under homeostatic conditions, TRMs are the dominant population; during infection or injury, monocyte-derived macrophages dominate the inflammatory response and may partially replace depleted TRMs. Resolution is mediated by efferocytosis-triggered anti-inflammatory reprogramming (PGE₂, IL-10, TGF-β) and subsequent apoptosis or local self-renewal of surviving macrophages.

## Connections

- **Upstream activators:** Pathogen-associated molecular patterns (PAMPs: LPS, peptidoglycan, CpG DNA); damage-associated molecular patterns (DAMPs: HMGB1, ATP, urate crystals); cytokines (IFN-γ, GM-CSF, M-CSF/CSF1, IL-4, IL-13).
- **Downstream effectors:** IL-6, TNF-α, IL-1β, IL-12, ROS, NO (pro-inflammatory); IL-10, TGF-β, VEGF, Arg1 (anti-inflammatory/repair).
- **Cellular crosstalk:** Activate T-helper cells via MHC-II + co-stimulation; receive help from Th1 cells (IFN-γ); kill tumour cells via ADCP; cooperate with NK cells (macrophages supply IL-12/IL-18; NK cells supply IFN-γ); interact with mast cells and neutrophils in early inflammation.
- **Pathological roles:** Foam-cell macrophages drive atherosclerotic plaque formation; tumour-associated macrophages (TAMs, M2-like) promote tumour immune evasion and angiogenesis; activated Kupffer cells drive NAFLD → NASH → fibrosis; microglia contribute to neurodegeneration in Alzheimer's and Parkinson's disease.
- `connects-to` → **[Familial Hypercholesterolemia](../../07-system/familial-hypercholesterolemia/README.md)** — in FH, chronically elevated LDL-C → macrophage scavenger receptor (SR-A, CD36) uptake of oxidized LDL → foam cell formation; foam cells are the histological hallmark of the atheromatous plaque; FH macrophages exhibit exaggerated ox-LDL uptake vs. normolipidemic controls.

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

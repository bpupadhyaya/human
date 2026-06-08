---
schema: human-scale-entry/v1
id: tlr4
name: TLR4
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "TLR4 (Toll-like receptor 4; CD284; type I TM PAMP receptor) senses gram-negative LPS via MD-2/CD14 → MyD88/TRIF → NF-κB/IRF3 → TNF-α, IL-12, IFN-β; TLR4 Asp299Gly/Thr399Ile SNPs → hyporesponsiveness and sepsis risk; antagonists (TAK-242) suppress endotoxin-driven inflammation."
aliases: ["Toll-like receptor 4", "CD284", "TLR-4", "LPS receptor", "endotoxin receptor", "ARMD10", "TOLL"]
sources:
  - id: poltorak-1998-tlr4-lps
    type: peer-reviewed
    cite: "Poltorak A, He X, Smirnova I, et al. Defective LPS signaling in C3H/HeJ and C57BL/10ScCr mice: mutations in Tlr4 gene. Science. 1998;282(5396):2085-2088."
    doi: "10.1126/science.282.5396.2085"
    pmid: "9851930"
    url: "https://doi.org/10.1126/science.282.5396.2085"
    accessed: "2026-06-08"
  - id: akira-2006-tlr-signaling
    type: peer-reviewed
    cite: "Akira S, Uematsu S, Takeuchi O. Pathogen recognition and innate immunity. Cell. 2006;124(4):783-801."
    doi: "10.1016/j.cell.2006.02.015"
    pmid: "16497588"
    url: "https://doi.org/10.1016/j.cell.2006.02.015"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/07-system/leishmaniasis
    relation: connects-to
    note: "TLR4 on macrophages senses Leishmania LPG (lipophosphoglycan) and CpG-like motifs → NF-κB → TNF-α + IL-12; however, L. donovani also hijacks TLR2 to suppress IL-12 (ManLAM-like evasion); TLR4-MyD88 signalling is required for optimal anti-Leishmania Th1 priming."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "TLR4/LPS is the primary trigger of gram-negative sepsis: LPS-MD-2-CD14 → TLR4 dimerisation → MyD88 (NF-κB: cytokine storm) + TRIF (IRF3: IFN-β); septic shock = CARS (compensatory anti-inflammatory response) after initial SIRS; TAK-242 (TLR4 antagonist) failed sepsis trials."
  - target: 01-human/03-molecular/nf-kb
    relation: regulates
    note: "TLR4 is the dominant upstream activator of NF-κB in innate immunity: LPS → TLR4/MyD88/IRAK4/TRAF6 → IKK → IκB degradation → p65/p50 nuclear translocation → TNF-α, IL-6, IL-12; TLR4/NF-κB is the central axis in gram-negative sepsis and chronic inflammatory diseases."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "MyD88 is the universal TLR4/TLR2/TLR7/TLR9 adaptor (except TLR3); TLR4-MyD88 → IRAK4-TRAF6 → NF-κB/MAPK → pro-inflammatory cytokines; MyD88 L265P drives constitutive NF-κB in lymphoma (Waldenstrom, DLBCL); MyD88 deficiency → invasive bacterial susceptibility."
  - target: 01-human/03-molecular/tnf-alpha
    relation: regulates
    note: "TLR4/LPS → MyD88 → NF-κB → TNF-α transcription in macrophages; TNF-α is the first cytokine released in gram-negative sepsis within 90 minutes; thalidomide and dexamethasone suppress LPS-induced TNF-α via distinct mechanisms; TNF-α drives the clinical syndrome of endotoxaemia."
  - target: 01-human/07-system/dengue-fever
    relation: connects-to
    note: "Dengue NS1 hexamer activates TLR4 on vascular endothelium → NF-κB → CXCL1, IL-8 → endothelial permeability; NS1 also disrupts glycocalyx via sialidase activation; TLR4-mediated endothelial activation is a key mechanism of plasma leakage in dengue hemorrhagic fever."
---

# TLR4

## Overview

Toll-like receptor 4 (TLR4; CD284) is a type I single-pass transmembrane pattern recognition receptor (PRR) of the innate immune system, expressed primarily on monocytes, macrophages, dendritic cells, and neutrophils. TLR4 is the principal sensor of lipopolysaccharide (LPS), the outer membrane glycolipid of gram-negative bacteria, and is essential for initiating innate defense against gram-negative infections. Its activation triggers a coordinated cytokine response — TNF-α, IL-6, IL-12, IFN-β — that bridges innate and adaptive immunity but, when dysregulated, drives the pathophysiology of septic shock.

TLR4 was identified as the LPS receptor by Poltorak et al. (1998), who found that C3H/HeJ mice — long known to be hyporesponsive to LPS — carried a point mutation in the *Tlr4* gene. This discovery, building on the Toll receptor work in *Drosophila* (Hoffman lab) and the identification of TLR homologs in humans (Medzhitov/Janeway, 1997), defined innate pattern recognition as a receptor-mediated process and launched the modern era of innate immunity research.

## Structure

TLR4 belongs to the TLR family of leucine-rich repeat (LRR)-containing receptors. Key structural features:

- **Ectodomain**: Horseshoe-shaped LRR array (24 repeats) that recognizes LPS in complex with MD-2 (myeloid differentiation factor 2), a small secreted co-receptor that directly binds lipid A
- **Transmembrane domain**: Single alpha-helix anchoring to the plasma membrane
- **Intracellular TIR domain**: Toll/IL-1 receptor homology domain that recruits adaptor proteins (MyD88, TRIF/TICAM-1) upon dimerization
- **Lipid A recognition complex**: LBP (LPS-binding protein) transfers LPS monomers to CD14 → CD14 loads LPS onto MD-2 → MD-2-LPS docks into TLR4 ectodomain → TLR4 dimerization and signal initiation
- **Dimerization**: LPS binding induces TLR4 homodimerization at both the ectodomain (M-shaped dimer) and TIR domain, creating the intracellular signaling platform

Key structural variants:
- **Asp299Gly** (rs4986790): Disrupts LRR9, reduces LPS binding, associated with hyporesponsiveness and increased sepsis risk
- **Thr399Ile** (rs4986791): Co-inherited with Asp299Gly; together reduce inflammatory responses to LPS; associated with increased susceptibility to gram-negative infections in some populations

## Function

TLR4 operates as a sentinel for gram-negative bacterial infection:

1. **Ligand spectrum**: Primarily LPS/lipid A from gram-negative bacteria; also recognizes endogenous DAMPs — HMGB1, heat shock proteins (HSP60/70), oxidized LDL (OxLDL), fibronectin extra domain A, and fibrinogen
2. **Cytokine induction**: Activated macrophages release TNF-α, IL-1β, IL-6, IL-12, and IL-23 within 1–4 hours of LPS stimulation
3. **Antiviral function**: TLR4 can recognize RSV and VSV surface proteins → TRIF/IRF3 → IFN-β production independent of the MyD88 pathway
4. **Dendritic cell maturation**: TLR4 ligation upregulates MHC-II, CD80/CD86, and CCR7 on DCs → migration to lymph nodes and T cell priming
5. **Metabolic inflammation**: OxLDL → TLR4 on macrophages → foam cell formation and atherosclerotic plaque progression; saturated fatty acids activate TLR4 → insulin resistance in obesity

## Mechanism

### MyD88-dependent pathway (early NF-κB activation)

LPS → TLR4 dimerization → MyD88/MAL (TIRAP) recruitment → IRAK4 phosphorylation → IRAK1/IRAK2 activation → TRAF6 ubiquitination (K63-linked) → TAK1 → IKKβ → IκBα phosphorylation and degradation → **NF-κB (p65/p50) nuclear translocation** → TNF-α, IL-6, IL-12, IL-1β transcription (within 30–60 minutes)

### TRIF-dependent pathway (delayed IFN induction)

LPS → TLR4 endocytosis into endosomes → TRAM/TRIF recruitment → TRAF3 → TBK1/IKKε → **IRF3 phosphorylation and dimerization** → nuclear translocation → IFN-β and CXCL10 transcription (2–4 hours); TRIF also activates RIPK1 → NF-κB (secondary wave) and caspase-8-dependent apoptosis

### TAK-242 (Resatorvid) inhibition

TAK-242 covalently binds Cys747 in the TLR4 TIR domain intracellular loop 3 → prevents adaptor protein recruitment → blocks both MyD88 and TRIF pathways; failed in Phase III sepsis trials (RESECT trial) due to administration after cytokine cascade was already underway

### Endotoxin tolerance

Repeated LPS exposure → TLR4 internalization + SHIP-1, A20, and IRAK-M upregulation → sustained hyporesponsiveness to subsequent LPS challenge; underlies the compensatory anti-inflammatory response syndrome (CARS) in sepsis survivors; contributes to post-sepsis immunosuppression and vulnerability to secondary infections

### Atherosclerosis

OxLDL activates TLR4 on macrophages in arterial intima → MyD88/NF-κB → TNF-α + MCP-1 → monocyte recruitment and foam cell formation; statins suppress TLR4 signaling partly independent of cholesterol lowering (anti-inflammatory pleiotropic effect)

## Connections

**→ [Leishmaniasis](../../../07-system/leishmaniasis/)**: TLR4 on macrophages senses Leishmania LPG (lipophosphoglycan) and CpG-like motifs → NF-κB → TNF-α + IL-12; however, L. donovani also hijacks TLR2 to suppress IL-12 (ManLAM-like evasion); TLR4-MyD88 signalling is required for optimal anti-Leishmania Th1 priming.

**→ [Sepsis](../../../07-system/sepsis/)**: TLR4/LPS is the primary trigger of gram-negative sepsis: LPS-MD-2-CD14 → TLR4 dimerisation → MyD88 (NF-κB: cytokine storm) + TRIF (IRF3: IFN-β); septic shock = CARS (compensatory anti-inflammatory response) after initial SIRS; TAK-242 (TLR4 antagonist) failed sepsis trials.

**→ [NF-κB](../nf-kb/)**: TLR4 is the dominant upstream activator of NF-κB in innate immunity: LPS → TLR4/MyD88/IRAK4/TRAF6 → IKK → IκB degradation → p65/p50 nuclear translocation → TNF-α, IL-6, IL-12; TLR4/NF-κB is the central axis in gram-negative sepsis and chronic inflammatory diseases.

**→ [MyD88](../myd88/)**: MyD88 is the universal TLR4/TLR2/TLR7/TLR9 adaptor (except TLR3); TLR4-MyD88 → IRAK4-TRAF6 → NF-κB/MAPK → pro-inflammatory cytokines; MyD88 L265P drives constitutive NF-κB in lymphoma (Waldenstrom, DLBCL); MyD88 deficiency → invasive bacterial susceptibility.

**→ [TNF-α](../tnf-alpha/)**: TLR4/LPS → MyD88 → NF-κB → TNF-α transcription in macrophages; TNF-α is the first cytokine released in gram-negative sepsis within 90 minutes; thalidomide and dexamethasone suppress LPS-induced TNF-α via distinct mechanisms; TNF-α drives the clinical syndrome of endotoxaemia.

**→ [Dengue Fever](../../../07-system/dengue-fever/)**: Dengue NS1 hexamer activates TLR4 on vascular endothelium → NF-κB → CXCL1, IL-8 → endothelial permeability; NS1 also disrupts glycocalyx via sialidase activation; TLR4-mediated endothelial activation is a key mechanism of plasma leakage in dengue hemorrhagic fever.

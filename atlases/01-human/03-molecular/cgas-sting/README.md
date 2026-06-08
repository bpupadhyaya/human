---
schema: human-scale-entry/v1
id: cgas-sting
name: cGAS-STING
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "cGAS (cyclic GMP-AMP synthase; MB21D1) senses cytosolic dsDNA → cGAMP → STING → TBK1 → IRF3 → IFN-β + NF-κB → inflammatory cytokines; activated by mtDNA, viral DNA, NETs; cGAS-STING drives interferonopathies (SLE, AGS); STING agonists (ADU-S100) activate anti-tumor immunity."
aliases: ["cGAS", "STING", "cyclic GMP-AMP synthase", "MB21D1", "TMEM173", "cGAMP", "cyclic dinucleotide", "innate DNA sensor", "interferonopathy", "cytosolic DNA sensing", "SAVI", "ADU-S100", "TBK1-IRF3 axis"]
sources:
  - id: sun-2013-cgas-dna-sensor
    type: peer-reviewed
    cite: "Sun L, Wu J, Du F, Chen X, Chen ZJ. Cyclic GMP-AMP synthase is a cytosolic DNA sensor that activates the type I interferon pathway. Science. 2013;339(6121):786-791."
    doi: "10.1126/science.1232458"
    pmid: "23258413"
    url: "https://doi.org/10.1126/science.1232458"
    accessed: "2026-06-08"
  - id: ishikawa-2008-sting-er-adaptor
    type: peer-reviewed
    cite: "Ishikawa H, Barber GN. STING is an endoplasmic reticulum adaptor that facilitates innate immune signalling. Nature. 2008;455(7213):674-678."
    doi: "10.1038/nature07317"
    pmid: "18724357"
    url: "https://doi.org/10.1038/nature07317"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/07-system/aicardi-goutieres-syndrome
    relation: connects-to
    note: "Aicardi-Goutières syndrome is caused by LOF of nucleases (TREX1, RNASEH2A/B/C, SAMHD1) or editors (ADAR1, IFIH1) → cytosolic nucleic acid accumulation → cGAS-STING → chronic IFN-α/β → brain calcifications, severe encephalopathy, and CSF lymphocytosis in children."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Self-DNA (NETs, late apoptotic cells, oxidized mtDNA) activates cGAS in pDCs and macrophages → cGAMP → STING → IFN-β; TREX1 LOF mutations cause monogenic SLE via cGAS-STING; hydroxychloroquine inhibits TLR7/9 in endosomes but does not directly block cGAS."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "cGAS-STING is the primary cytosolic DNA sensor driving type I IFN production: dsDNA → cGAS → cGAMP → STING → TBK1/IKKε → IRF3 phosphorylation/dimerization → IFN-β transcription; cGAS-STING-IFN-β is central to antiviral innate immunity and sterile inflammation."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "STING activates NF-κB in parallel with IRF3: STING → TRAF6/IKKβ → IκBα degradation → NF-κB → TNF-α, IL-6, and inflammatory genes; NF-κB activation by STING is independent of IRF3 and drives the non-interferon inflammatory response to cytosolic DNA in sepsis."
---

# cGAS-STING

## Overview

The **cGAS-STING axis** (cyclic GMP-AMP synthase → Stimulator of Interferon Genes) is the principal **cytosolic DNA sensing pathway** of the innate immune system. First defined by the Chen laboratory in 2013 [^sun-2013-cgas-dna-sensor], cGAS detects double-stranded DNA (dsDNA) of any sequence in the cytoplasm — whether from invading viruses, bacteria, mitochondria, chromatin fragments, or retrotransposons — and generates the second messenger **2′3′-cGAMP** (cyclic guanosine monophosphate-adenosine monophosphate). cGAMP then binds and activates **STING** (TMEM173), an ER transmembrane adaptor identified by Barber et al. in 2008 [^ishikawa-2008-sting-er-adaptor], triggering TBK1/IRF3-mediated IFN-β production and NF-κB-mediated cytokine release.

cGAS-STING sits at the intersection of antiviral defense, autoimmune disease, aging (senescence-associated secretory phenotype, SASP), and cancer immunotherapy — making it one of the most actively targeted pathways in drug development.

## Structure

### cGAS (MB21D1, ~57 kDa)

cGAS is a nucleotidyltransferase that catalyzes 2′3′-cGAMP synthesis from ATP and GTP:

- **N-terminal domain (1-160)**: Disordered; promotes cGAS oligomerization and chromatin tethering
- **Catalytic core (161-522)**: Nucleotidyltransferase fold with two-lobe structure; Zinc-ribbon domain (Zn²⁺ coordinated by Cys396/Cys397 — essential for DNA binding)
- **DNA binding surface**: Two positively charged surfaces (sites A and B) bind dsDNA with length dependence (≥45 bp optimal); cGAS-DNA forms a 2:2 complex that oligomerizes into a liquid-like phase (phase separation enhances activity)
- **Species specificity**: Human cGAS (hcGAS) has lower basal activity than mouse cGAS (mcGAS); important for therapeutic development — hcGAS agonists require higher concentrations

### STING (TMEM173, ~42 kDa)

STING is a type II ER transmembrane protein with 4 TM helices:

- **N-terminal transmembrane domain**: ER retention and homodimerization
- **Cytoplasmic ligand-binding domain (LBD)**: C2 symmetric homodimer; V-shaped cGAMP-binding pocket; structural rearrangement upon cGAMP binding (closing of "lid" region) → ER export
- **C-terminal tail (CTT)**: TBK1 and IRF3 recruitment site; palmitoylated Cys88/Cys91 anchor STING to Golgi; palmitoylation required for signaling

**STING trafficking:** cGAMP binding → STING-TBK1 complex forms at ER → COPII vesicle export → ER-Golgi intermediate compartment (ERGIC) → Golgi → perinuclear puncta → TBK1 trans-autophosphorylation → IRF3 phosphorylation → nuclear translocation

**Common STING variants:**
- **HAQ (R71H-G230A-R293Q)**: ~20% of Caucasians; reduced cGAMP binding and signaling
- **R232H**: Rare; abolishes cGAMP binding
- **G166E (SAVI-causing GOF)**: STING gain-of-function → constitutive IFN-β → STING-associated vasculopathy with onset in infancy (SAVI)

## Function

1. **Antiviral sensing**: Herpesvirus dsDNA (HSV-1, CMV), HIV reverse-transcribed DNA, Adenovirus → cytoplasmic dsDNA → cGAS → cGAMP → STING → IFN-β → antiviral ISG program
2. **Bacterial sensing**: Bacterial CDNs (c-di-GMP, c-di-AMP) directly activate STING; bacteria-derived dsDNA → cGAS; important for Listeria, Mycobacterium, Shigella recognition
3. **Self-DNA sensing**: Failure of nucleic acid clearance → cGAS activation:
   - Mitochondrial DNA (mtDNA) release during oxidative stress or caspase-inhibited apoptosis
   - Nuclear DNA fragments from genome instability
   - LINE-1 retrotransposon reverse-transcribed cDNA
   - NETs (neutrophil extracellular traps) in SLE and aging
4. **Senescence (SASP)**: Cytoplasmic chromatin bridges and micronuclei from replication stress → cGAS → STING → SASP cytokines (IL-6, IL-1α); drives tumor suppression and aging-associated inflammation
5. **Anti-tumor immunity**: Tumor-derived dsDNA in dendritic cells → cGAS-STING → IFN-β → cross-priming of CD8⁺ T cells; STING agonist injection into tumors activates anti-tumor immune responses

## Mechanism

### Canonical cGAS-STING-TBK1-IRF3 pathway

1. **dsDNA detection**: dsDNA (≥20 bp for activation; ≥45 bp for optimal activity) binds two surfaces on cGAS
2. **Enzyme activation**: DNA binding induces cGAS conformational change → active site geometry optimized → 2′3′-cGAMP synthesis from ATP + GTP (non-canonical 2′-5′/3′-5′ phosphodiester bonds)
3. **STING activation**: 2′3′-cGAMP binds STING homodimer LBD (picomolar affinity) → conformational change → STING palmitoylation (DHHC3/5/11) at Golgi → TBK1 recruitment
4. **IRF3 phosphorylation**: TBK1 trans-autophosphorylation → TBK1 activation → IRF3 Ser396 phosphorylation → IRF3 dimerization → nuclear translocation → **IFN-β promoter activation** (enhanceosome: IRF3 + AP-1 + NF-κB)
5. **STING degradation**: Phosphorylated STING is ubiquitinated by TRIM30α (K48-linked) → proteasomal degradation → signal termination; STING also undergoes lysosomal degradation via autophagy

### Parallel NF-κB activation

STING → TRAF6 (K63-linked ubiquitination) → TAK1 → IKKβ → IκBα phosphorylation/degradation → NF-κB nuclear translocation → TNF-α, IL-6, IL-12, and additional IFN-β (second wave)

### cGAMP transfer

2′3′-cGAMP diffuses through gap junctions (connexins) to neighboring cells → STING activation in cells that lack cGAS or dsDNA → bystander interferon amplification; also packaged into viral capsids (herpesvirus) → delivered to next infected cell

### STING inhibition

- **H-151 (covalent STING inhibitor)**: Binds Cys91 in palmitoylation site → prevents palmitoylation and STING trafficking → blocks signaling; potent in vitro and preclinical disease models
- **SN-011**: Non-covalent STING antagonist; investigational for SLE
- **ENPP1 (ectonucleotidase)**: Degrades extracellular 2′3′-cGAMP → important checkpoint on cGAMP paracrine signaling; ENPP1 inhibitors (RBS2418/uze­brelimab) enhance STING-mediated anti-tumor immunity

## Connections

**→ [Aicardi-Goutières Syndrome](../../../07-system/aicardi-goutieres-syndrome/)**: Aicardi-Goutières syndrome is caused by LOF of nucleases (TREX1, RNASEH2A/B/C, SAMHD1) or editors (ADAR1, IFIH1) → cytosolic nucleic acid accumulation → cGAS-STING → chronic IFN-α/β → brain calcifications, severe encephalopathy, and CSF lymphocytosis in children.

**→ [Systemic Lupus Erythematosus](../../../07-system/systemic-lupus-erythematosus/)**: Self-DNA (NETs, late apoptotic cells, oxidized mtDNA) activates cGAS in pDCs and macrophages → cGAMP → STING → IFN-β; TREX1 LOF mutations cause monogenic SLE via cGAS-STING; hydroxychloroquine inhibits TLR7/9 in endosomes but does not directly block cGAS.

**→ [Type I Interferon](../type-i-interferon/)**: cGAS-STING is the primary cytosolic DNA sensor driving type I IFN production: dsDNA → cGAS → cGAMP → STING → TBK1/IKKε → IRF3 phosphorylation/dimerization → IFN-β transcription; cGAS-STING-IFN-β is central to antiviral innate immunity and sterile inflammation.

**→ [NF-κB](../nf-kb/)**: STING activates NF-κB in parallel with IRF3: STING → TRAF6/IKKβ → IκBα degradation → NF-κB → TNF-α, IL-6, and inflammatory genes; NF-κB activation by STING is independent of IRF3 and drives the non-interferon inflammatory response to cytosolic DNA in sepsis.

---
schema: human-scale-entry/v1
id: aicardi-goutieres-syndrome
name: Aicardi-Goutières Syndrome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Aicardi-Goutières syndrome (AGS) is a genetic interferonopathy caused by LOF mutations in nucleic acid metabolism genes (TREX1, RNASEH2A/B/C, SAMHD1, ADAR1, IFIH1) → cytosolic nucleic acid accumulation → cGAS-STING activation → chronic IFN-α/β → progressive encephalopathy."
aliases: ["AGS", "Aicardi-Goutieres syndrome", "Cree encephalitis", "pseudo-TORCH syndrome", "interferonopathy", "TREX1 deficiency", "RNASEH2 deficiency", "SAMHD1 deficiency", "ADAR1 deficiency", "IFIH1 deficiency", "familial chilblain lupus"]
sources:
  - id: crow-2015-ags-phenotype
    type: peer-reviewed
    cite: "Crow YJ, Chase DS, Lowenstein Schmidt J, et al. Characterization of human disease phenotypes associated with mutations in TREX1, RNASEH2A, RNASEH2B, RNASEH2C, SAMHD1, ADAR, and IFIH1. Am J Med Genet A. 2015;167A(2):296-312."
    doi: "10.1002/ajmg.a.36887"
    pmid: "25604658"
    url: "https://doi.org/10.1002/ajmg.a.36887"
    accessed: "2026-06-08"
  - id: crow-2014-ags-review
    type: peer-reviewed
    cite: "Crow YJ. Aicardi-Goutières syndrome. Handb Clin Neurol. 2013;113:1629-1635."
    doi: "10.1016/B978-0-444-59565-2.00031-9"
    pmid: "23622387"
    url: "https://doi.org/10.1016/B978-0-444-59565-2.00031-9"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "cGAS-STING is the central effector of AGS: undigested nucleic acids (TREX1/RNASEH2 substrates) activate cytosolic cGAS → cGAMP → STING → TBK1 → IRF3 → IFN-β; SAMHD1 dNTPase and ADAR1 A-to-I editing prevent inappropriate cGAS-STING activation by self-nucleic acids."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "TREX1 LOF mutations cause both AGS and familial SLE — demonstrating that the same cGAS-STING pathway underlies both monogenic (AGS) and polygenic (SLE) interferonopathies; ANA and anti-dsDNA occur in TREX1 mutation carriers; type I IFN signature drives both diseases."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "AGS is a chronic interferonopathy: dysfunctional nucleases → nucleic acid accumulation → cGAS-STING → constitutive IFN-α/β; CSF IFN-α >2 IU/mL is diagnostic; ISG score (blood interferon-stimulated gene signature) is elevated; reverse transcriptase inhibitors reduce IFN-α."
  - target: 01-human/06-organ/microcephaly
    relation: connects-to
    note: "AGS causes post-natal progressive microcephaly via chronic IFN-α → microglial activation → cortical neuronal death; distinguishes from primary MCPH (genetic proliferation defects); basal ganglia calcification + acquired microcephaly = pseudo-TORCH presentation on neuroimaging."
  - target: 02-pathogen/01-viruses/hiv-1
    relation: connects-to
    note: "SAMHD1 (AGS gene) is the principal HIV-1 restriction factor: dNTP hydrolase depletes viral dNTP pool → inhibits reverse transcription; HIV-2/SIVsm Vpx degrades SAMHD1; SAMHD1-LOF in AGS links innate antiviral immunity to monogenic neuroinflammation."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "STING → TBK1 activates both IRF3 (IFN-β) and IKKβ/NF-κB; chronic NF-κB in AGS drives TNF-α/IL-6 from microglia independent of IFN; NF-κB upregulation amplifies neuroinflammation; baricitinib (JAK1/2 inhibitor) reduces ISG and NF-κB-driven inflammation in AGS."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "In Aicardi-Goutières syndrome the chronic type I interferon flooding the brain activates microglia, which attack neurons and cerebral vessels — producing the progressive encephalopathy, white-matter disease, and basal-ganglia calcification of AGS."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Aicardi-Goutières syndrome is driven by type I interferon through the IFNAR-JAK-STAT pathway, so JAK1/2 inhibitors like baricitinib are the leading treatment: they lower the interferon signature and can stabilize disease, but rarely reverse established neurological damage."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "AGS is fundamentally a brain disease: constitutive interferon causes an inflammatory encephalopathy with intracranial calcifications and acquired microcephaly that mimics congenital TORCH infection — but with sterile CSF lymphocytosis and high CSF interferon-α."
  - target: 01-human/07-system/dermatomyositis
    relation: connects-to
    note: "AGS and dermatomyositis are both type I interferonopathies: AGS is a monogenic constitutive activation of nucleic-acid sensing (cGAS-STING/RIG-I), DM an acquired interferon signature; both show high interferon scores and chilblain-like lesions, and both respond to JAK inhibition."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "The skin reveals Aicardi-Goutières syndrome: chronic type I interferon drives chilblain lesions—painful red-purple acral swellings on fingers, toes and ears that worsen in cold—mirroring chilblain lupus; these signs reflect the interferon vasculopathy that also injures the brain."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Astrocytes are central to Aicardi-Goutières brain disease: they are a major source of the excess intracerebral type I interferon, and interferon-driven microangiopathy drives the basal-ganglia calcification and white-matter loss that mimic congenital infection."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Aicardi-Goutières syndrome injures neurons through chronic interferon: misprocessed self-nucleic acids drive a type-I-interferon response that damages the developing brain, causing basal-ganglia calcification and an encephalopathy that mimics TORCH infection."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Plasmacytoid dendritic cells amplify Aicardi-Goutières syndrome: defective nucleic-acid sensors let self-DNA/RNA accumulate and trigger pDCs to pour out type I interferon—the same axis overactive in lupus, making AGS a monogenic interferonopathy."
  - target: 01-human/07-system/sjogrens-syndrome
    relation: connects-to
    note: "Aicardi-Goutières syndrome and Sjögren's both run on a type-I-interferon signature: AGS is the monogenic, infantile extreme of interferon-driven disease, while Sjögren's is its acquired adult counterpart—one cytokine pathway across rare genetic and common illness."
---

# Aicardi-Goutières Syndrome

## Overview

**Aicardi-Goutières syndrome (AGS)** is a rare genetic interferonopathy — a progressive inflammatory encephalopathy caused by constitutional activation of the **cGAS-STING innate immune sensing pathway** due to inherited loss-of-function mutations in genes encoding nucleic acid metabolism enzymes. First described by Aicardi and Goutières in 1984 as a "pseudo-TORCH" syndrome (resembling congenital infection but with negative viral cultures), AGS is now recognized as the founding member of the **type I interferonopathies** — a group of genetic disorders characterized by chronic, constitutive type I interferon production.

AGS affects approximately 1 in 100,000 individuals, with equal sex distribution. Most cases present in infancy or early childhood with progressive neurological deterioration, though later-onset presentations are recognized. The molecular mechanism — undigested nucleic acid substrates accumulating in the cytosol → activating cGAS-STING → chronic IFN-α/β production — directly links AGS to acquired autoimmune diseases (particularly SLE), providing fundamental insights into how self-nucleic acids trigger autoimmunity.

## Structure

### Genetic architecture (7 causal genes)

| Gene | Product | Function | % AGS cases |
|------|---------|----------|-------------|
| RNASEH2B | RNase H2 subunit B | Degrades RNA:DNA hybrids; removes ribonucleotides from genomic DNA | ~36% |
| TREX1 | DNase III (3′→5′ exonuclease) | Degrades cytosolic ssDNA and dsDNA from apoptosis, retroelements | ~25% |
| RNASEH2A | RNase H2 subunit A (catalytic) | Ribonucleotide excision repair | ~10% |
| RNASEH2C | RNase H2 subunit C | Structural | ~10% |
| SAMHD1 | dNTP triphosphohydrolase | Depletes dNTP pool; restricts HIV-1 reverse transcription | ~7% |
| ADAR1 | Adenosine deaminase RNA-specific | A-to-I editing of dsRNA → prevents MDA5/cGAS recognition | ~6% |
| IFIH1 (MDA5) | Innate RNA helicase | *Gain-of-function* mutations → hyperactive MDA5 sensing | ~4% |

**Inheritance**: Most genes cause AR (autosomal recessive) AGS; TREX1, ADAR1, and IFIH1 can also cause AD (autosomal dominant) disease via haploinsufficiency or gain-of-function.

### Molecular substrates and cGAS-STING activation

Each gene loss leads to accumulation of specific nucleic acid substrates that activate cGAS-STING or RIG-I/MDA5:
- **TREX1 deficiency**: Accumulation of cytosolic ssDNA/dsDNA from: (1) aberrant processing of DNA replication intermediates; (2) L1 retrotransposon reverse-transcribed cDNA → cGAS activation
- **RNASEH2 deficiency**: Ribonucleotides misincorporated during replication are not removed → RNA:DNA hybrid accumulation → genome instability → cytosolic DNA → cGAS
- **SAMHD1 deficiency**: Elevated dNTP pool → enhanced reverse transcription of LINE-1 elements → L1 cDNA → cGAS; also restricts HIV-1 in non-dividing cells
- **ADAR1 deficiency**: Unedited endogenous dsRNA (Alu/SINE inverted repeats) → MDA5/RIG-I activation → type I IFN (downstream of cGAS-STING-independent pathway)
- **IFIH1 (MDA5) GOF**: Constitutively active MDA5 → MAVS → IRF3 → IFN-β without ligand stimulus

## Function

The AGS genes collectively function as the **nucleic acid surveillance system** that prevents inappropriate innate immune activation by endogenous nucleic acids:

1. **Nuclease degradation**: TREX1 and RNASEH2 complex remove DNA/RNA:DNA hybrids before they reach the cytosol
2. **dNTP regulation**: SAMHD1 depletes the dNTP pool needed for reverse transcription of retrotransposons
3. **Nucleic acid camouflage**: ADAR1 A-to-I editing changes dsRNA structure → prevents MDA5 recognition
4. **Signaling threshold**: Together, these enzymes maintain cytosolic nucleic acid concentrations below the threshold for cGAS/MDA5 activation

When any one of these checkpoints fails (by mutation), the threshold is breached → cGAS-STING/MDA5 activation → chronic type I IFN production → progressive neurovascular inflammation.

## Pathology

### Clinical presentation

**Typical AGS (infantile onset; RNASEH2B, TREX1 mutations)**:
- Normal at birth; developmental regression at 4 months to 1 year
- **Irritability**, poor feeding, fever-like episodes without infection
- **Progressive microcephaly**, spastic quadriplegia, dystonia
- **Intracranial calcifications**: Basal ganglia and deep white matter (bilateral, symmetric; on CT — classic "salt-and-pepper" appearance; present in ~80% of AGS cases)
- **White matter abnormalities**: Periventricular and subcortical (MRI: T2-FLAIR signal abnormality)
- **CSF lymphocytosis**: 10–50 cells/μL (lymphocytes > 5/μL in >80% early AGS); CSF IFN-α elevated >2 IU/mL (diagnostic threshold)
- **Chilblain lesions**: Acral skin lesions (fingers, toes, ears) from vasculopathy; particularly TREX1, SAMHD1 mutations

**Attenuated/late-onset AGS (IFIH1 GOF, ADAR1)**:
- Spastic diplegia, intellectual disability without rapid regression
- Systemic lupus-like features (arthritis, malar rash, ANA) 
- Aicardi-Goutières syndrome / Singleton-Merten overlap syndrome (IFIH1 GOF: dental dysplasia, aortic calcification)

### Laboratory findings

- **ISG score (interferon-stimulated gene signature)**: Elevated in peripheral blood; panel of 6 ISGs (MX1, IFI44L, IFI27, RSAD2, SIGLEC1, IFIT1) scoring > 2.466 in AGS; used for diagnosis and treatment monitoring
- **CSF IFN-α**: >2 IU/mL diagnostic; available in reference labs; elevated in ~70% of cases (higher early)
- **ANA, anti-dsDNA**: Positive in ~25% (particularly TREX1 mutations) — AGS-SLE overlap
- **Low platelets, lymphopenia**: ~20% of cases (systemic immune activation)

### Treatment

**No disease-modifying therapy is FDA-approved** for AGS. Active areas:

| Strategy | Rationale | Status |
|----------|-----------|--------|
| Reverse transcriptase inhibitors (RTIs): abacavir + zidovudine + lamivudine (AZA) | TREX1-deficient cells have excess L1 reverse transcripts → RTIs block L1 cDNA generation → less cGAS substrate | Phase II (PROTECT trial; Crow lab) — ISG score reduced; functional benefit modest |
| JAK inhibitors (ruxolitinib, baricitinib) | Block downstream IFNAR-JAK1/TYK2-STAT1/2 signaling → suppress ISG expression | Case series positive; Phase II ongoing in LIBERATE trial |
| STING inhibitors (H-151, SN-011) | Block STING directly → prevent IFN-β induction | Preclinical only |
| Anti-IFNAR1 (anifrolumab) | Block type I IFN receptor → suppress all IFN-α/β effects | Investigational; compassionate use cases reported |

**Supportive care**: Spasticity management (baclofen, botulinum toxin), anticonvulsants for seizures, enteral nutrition for failure-to-thrive, speech and physiotherapy, chilblain wound care.

### Prognosis

Severe early-onset AGS (TREX1 homozygous, RNASEH2A): death in childhood from respiratory failure or aspiration; most surviving patients have severe disability. Attenuated IFIH1/ADAR1 phenotypes may have near-normal lifespan with moderate disability. RTI trials show stabilization of ISG scores with limited functional recovery — suggesting early intervention (neonatal screening?) may be needed.

## Connections

**→ [cGAS-STING](../../../03-molecular/cgas-sting/)**: cGAS-STING is the central effector of AGS: undigested nucleic acids (TREX1/RNASEH2 substrates) activate cytosolic cGAS → cGAMP → STING → TBK1 → IRF3 → IFN-β; SAMHD1 dNTPase and ADAR1 A-to-I editing prevent inappropriate cGAS-STING activation by self-nucleic acids.

**→ [Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/)**: TREX1 LOF mutations cause both AGS and familial SLE — demonstrating that the same cGAS-STING pathway underlies both monogenic (AGS) and polygenic (SLE) interferonopathies; ANA and anti-dsDNA occur in TREX1 mutation carriers; type I IFN signature drives both diseases.

**→ [Type I Interferon](../../../03-molecular/type-i-interferon/)**: AGS is a chronic interferonopathy: dysfunctional nucleases → nucleic acid accumulation → cGAS-STING → constitutive IFN-α/β; CSF IFN-α >2 IU/mL is diagnostic; ISG score (blood interferon-stimulated gene signature) is elevated; reverse transcriptase inhibitors reduce IFN-α.

**→ [Microcephaly](../../../06-organ/microcephaly/)**: AGS causes post-natal progressive microcephaly via chronic IFN-α → microglial activation → cortical neuronal death; distinguishes from primary MCPH (genetic proliferation defects); basal ganglia calcification + acquired microcephaly = pseudo-TORCH presentation on neuroimaging.

**→ [HIV-1](../../../../02-pathogen/01-viruses/hiv-1/)**: SAMHD1 (AGS gene) is the principal HIV-1 restriction factor: dNTP hydrolase depletes viral dNTP pool → inhibits reverse transcription; HIV-2/SIVsm Vpx degrades SAMHD1; SAMHD1-LOF in AGS links innate antiviral immunity to monogenic neuroinflammation.

**→ [NF-κB](../../../03-molecular/nf-kb/)**: STING → TBK1 activates both IRF3 (IFN-β) and IKKβ/NF-κB; chronic NF-κB in AGS drives TNF-α/IL-6 from microglia independent of IFN; NF-κB upregulation amplifies neuroinflammation; baricitinib (JAK1/2 inhibitor) reduces ISG and NF-κB-driven inflammation in AGS.

- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — In Aicardi-Goutières syndrome the chronic type I interferon flooding the brain activates microglia, which attack neurons and cerebral vessels — producing the progressive encephalopathy, white-matter disease, and basal-ganglia calcification of AGS.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Aicardi-Goutières syndrome is driven by type I interferon through the IFNAR-JAK-STAT pathway, so JAK1/2 inhibitors like baricitinib are the leading treatment: they lower the interferon signature and can stabilize disease, but rarely reverse established neurological damage.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — AGS is fundamentally a brain disease: constitutive interferon causes an inflammatory encephalopathy with intracranial calcifications and acquired microcephaly that mimics congenital TORCH infection — but with sterile CSF lymphocytosis and high CSF interferon-α.
- `connects-to` → **[Dermatomyositis](../dermatomyositis/README.md)** — AGS and dermatomyositis are both type I interferonopathies: AGS is a monogenic constitutive activation of nucleic-acid sensing (cGAS-STING/RIG-I), DM an acquired interferon signature; both show high interferon scores and chilblain-like lesions, and both respond to JAK inhibition.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — The skin reveals Aicardi-Goutières syndrome: chronic type I interferon drives chilblain lesions—painful red-purple acral swellings on fingers, toes and ears that worsen in cold—mirroring chilblain lupus; these signs reflect the interferon vasculopathy that also injures the brain.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Astrocytes are central to Aicardi-Goutières brain disease: they are a major source of the excess intracerebral type I interferon, and interferon-driven microangiopathy drives the basal-ganglia calcification and white-matter loss that mimic congenital infection.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Aicardi-Goutières syndrome injures neurons through chronic interferon: misprocessed self-nucleic acids drive a type-I-interferon response that damages the developing brain, causing basal-ganglia calcification and an encephalopathy that mimics TORCH infection.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Plasmacytoid dendritic cells amplify Aicardi-Goutières syndrome: defective nucleic-acid sensors let self-DNA/RNA accumulate and trigger pDCs to pour out type I interferon—the same axis overactive in lupus, making AGS a monogenic interferonopathy.
- `connects-to` → **[Sjögren's Syndrome](../sjogrens-syndrome/README.md)** — Aicardi-Goutières syndrome and Sjögren's both run on a type-I-interferon signature: AGS is the monogenic, infantile extreme of interferon-driven disease, while Sjögren's is its acquired adult counterpart—one cytokine pathway across rare genetic and common illness.

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

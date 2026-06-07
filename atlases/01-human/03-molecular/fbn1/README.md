---
schema: human-scale-entry/v1
id: fbn1
name: FBN1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "FBN1 encodes fibrillin-1, the principal component of extracellular microfibrils that sequester TGF-β; FBN1 mutations → inadequate TGF-β sequestration → excess TGF-β signaling → aortic root dilation and connective tissue laxity; haploinsufficient FBN1 LOF causes Marfan syndrome."
aliases: ["FBN1", "fibrillin-1", "fibrillin", "FBN1 Marfan", "fibrillin-1 Marfan", "FBN1 aortic aneurysm", "FBN1 ectopia lentis", "fibrillin microfibril", "Marfan FBN1 mutation", "FBN1 connective tissue"]
sources:
  - id: dietz-1991-fbn1-marfan
    type: peer-reviewed
    cite: "Dietz HC, Cutting GR, Pyeritz RE, et al. Marfan syndrome caused by a recurrent de novo missense mutation in the fibrillin gene. Nature. 1991;352(6333):337-339."
    doi: "10.1038/352337a0"
    pmid: "1852208"
    url: "https://doi.org/10.1038/352337a0"
  - id: neptune-2003-tgfb-marfan
    type: peer-reviewed
    cite: "Neptune ER, Frischmeyer PA, Arking DE, et al. Dysregulation of TGF-beta activation contributes to pathogenesis in Marfan syndrome. Nat Genet. 2003;33(3):407-411."
    doi: "10.1038/ng1116"
    pmid: "12598898"
    url: "https://doi.org/10.1038/ng1116"
cross_links:
  - target: 01-human/07-system/marfan-syndrome
    relation: connects-to
    note: "Germline FBN1 haploinsufficiency or dominant-negative mutations → Marfan syndrome; FBN1 LOF reduces microfibril scaffold → less TGF-β sequestration → excess TGF-β signaling → SMAD2/3 activation → aortic smooth muscle cell phenotypic switch → progressive aortic root aneurysm."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "FBN1 microfibrils bind LTBP (latent TGF-β binding protein) → sequester TGF-β in ECM; FBN1 LOF → reduced TGF-β sequestration → excess TGF-β → ERK and SMAD2/3 activation in aortic SMCs → MMP production → elastic lamina fragmentation → aneurysm formation."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "FBN1 LOF → excess TGF-β signaling → SMAD2/3 phosphorylation → nuclear translocation → aortic gene expression changes driving aneurysm; SMAD4 is the common SMAD that co-activates SMAD2/3 transcription; SMAD4 mutations in juvenile polyposis syndrome also cause aortic aneurysm."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "FBN1 fibrillin-1 microfibrils and collagen fibers are the two major structural components of the arterial wall ECM; fibrillin-1 provides elastic recoil; collagen provides tensile strength; Marfan syndrome (FBN1) and OI (COL1A1/2) both affect connective tissue integrity."
---

# FBN1

## Overview

**FBN1** (Fibrillin-1) is a 2,871 amino acid (350 kDa) secreted **extracellular matrix glycoprotein** that polymerizes into **elastic microfibrils** — long rope-like structures (~10-12 nm diameter) that form the scaffold of elastic fibers in virtually all connective tissues. Fibrillin-1 microfibrils serve two major roles: (1) **structural** — providing tensile strength and elasticity to the aortic wall, ocular zonule, and skeletal ligaments; and (2) **regulatory** — sequestering latent TGF-β complexes (via LTBP1/3 binding) and BMPs (via LTBP-like domains) in the ECM, controlling their bioavailability to cell surface receptors. FBN1 was the first Marfan syndrome gene identified; missense mutations were reported by Dietz et al. in 1991 [^dietz-1991-fbn1-marfan]. The critical insight that FBN1 LOF causes disease not only through structural weakening but through excess TGF-β signaling was demonstrated by Neptune et al. in 2003 — fibrillin-1-deficient mice showed elevated TGF-β activity in lungs and aortae, and anti-TGF-β antibody treatment rescued the pulmonary phenotype [^neptune-2003-tgfb-marfan].

**Marfan syndrome pathomechanism — the dual model:**
- **Structural haploinsufficiency**: one defective FBN1 allele → reduced microfibril assembly → weaker, less elastic aortic wall and zonular fibers → aortic dilation, lens subluxation
- **TGF-β excess**: reduced microfibril scaffold → less LTBP-bound TGF-β sequestered → more free, active TGF-β → SMAD2/3 and ERK1/2 activation in aortic smooth muscle cells → MMP overexpression → elastic lamina fragmentation → progressive aneurysm
- Both mechanisms contribute; TGF-β pathway is now the primary therapeutic target (losartan's rationale: AT1R blockade reduces TGF-β production and signaling in aortic SMCs)

**FBN1 genotype spectrum:**

| Mutation type | Proportion | Mechanism | Phenotype severity |
|---|---|---|---|
| Missense in cbEGF domains | ~35% | Dominant negative (misfolded FBN1 poisons microfibril assembly) | Severe (cysteine substitutions most severe) |
| Nonsense/frameshift | ~25% | Haploinsufficiency (truncated allele degraded by NMD) | Moderate-severe |
| Splice site | ~20% | Variable; exon skipping → truncated protein | Variable |
| Large deletions/duplications | ~10-15% | Haploinsufficiency | Moderate |
| Neonatal Marfan zone (exons 24-32) | ~5% | Severe dominant-negative cysteine substitutions in cbEGF domains 14-20 | Neonatal Marfan: worst prognosis |

## Structure

### FBN1 protein domains

**N-terminal unique domain (aa 1-28):**
- Signal peptide; cleaved during ER translocation; FBN1 secreted into ECM as a monomer; N-terminal propeptide removed by PACE/furin in the Golgi

**Calcium-binding EGF-like domains (cbEGF; 47 repeats distributed throughout protein):**
- 6 cysteine residues per cbEGF domain forming 3 disulfide bonds; Ca²⁺ binds in the N-terminal part of each cbEGF domain (DX(D/N)ECX motif) → Ca²⁺ binding rigidifies the domain and protects disulfide bonds from reduction
- **Cysteine substitutions** (e.g., Cys→Arg/Gly/Ser in cbEGF domains): most severe FBN1 mutations; disrupts one of the 3 disulfide bonds → misfolded cbEGF → dominant-negative effect — mutant FBN1 monomer co-polymerizes into microfibrils and disrupts the entire microfibril
- **Calcium coordination residues**: N(D/E)X(D/N)EC motif mutated in many Marfan mutations (N2400S, D1441N, etc.) → impaired Ca²⁺ binding → cbEGF domain unfolds → reduced microfibril stability

**TGF-β-binding protein-like (TB) domains (7 TB domains):**
- Also called 8-cysteine domains; structurally related to LTBP (latent TGF-β binding protein)
- TB domain 4 (also called CBMF4): primary domain that directly contacts LTBP1 and LTBP3 → tethers large latent TGF-β complexes (LLC) to fibrillin-1 microfibrils → TGF-β sequestration
- TB domains also bind BMPs (particularly BMP-7, -10) → modulate BMP bioavailability; relevant to skeletal features (BMP signaling in bone formation)
- TB5 contains RGD (Arg-Gly-Asp) integrin-binding motif → fibrillin-1 engages α5β1 and αvβ3 integrins → cell attachment to ECM; this interaction is important for cell sensing of microfibril scaffold integrity

**EGF-like domains (non-calcium-binding; 13 domains interspersed):**
- Similar disulfide structure to cbEGF but without the Ca²⁺ coordination motif; less rigid; provide flexible linkers between cbEGF clusters; mutations in EGF domains cause milder Marfan phenotypes

**C-terminal propeptide domain:**
- Removed by ADAMTS proteases (ADAMTS10, ADAMTS17) in ECM → initiates fibrillin-1 fibrillar assembly; ADAMTS10 mutations cause Weill-Marchesani syndrome (an FBN1-related microfibrillopathy)

### Fibrillin-1 microfibril assembly

**Assembly steps:**
1. FBN1 monomers secreted → associate via N- and C-terminal interactions → form bead-on-string 10-12 nm microfibrils
2. Microfibrils deposited along cell surfaces → cells retract → microfibrils persist as ECM cables
3. In elastic tissues (aorta, lung): microfibrils serve as scaffolds for tropoelastin deposition → tropoelastin crosslinked by lysyl oxidase (LOX) → amorphous elastin core → fibrillin microfibrils wrap around the elastin → mature elastic fiber
4. In non-elastic tissues (ocular zonule): microfibrils exist without elastin → pure fibrillin scaffold provides tensile strength for lens suspension

**Microfibrils in aortic wall:**
- Aortic media: concentric elastic laminae (alternating smooth muscle cells + elastic fibers) → pressure buffering
- FBN1 microfibrils in the elastic lamina: each elastic lamina is a fibrillin-elastin composite; fibrillin forms the outer 10-12 nm sheath; elastin fills the amorphous core
- FBN1 LOF → reduced microfibril assembly → elastic laminae thinner/disrupted → aortic wall less compliant → TGF-β excess → MMPs degrade elastic laminae → progressive aneurysm

## Function

### FBN1 in TGF-β sequestration

**Latent TGF-β complex and LTBP-fibrillin interaction:**
- TGF-β is secreted as a large latent complex (LLC): TGF-β dimer + LAP (latency-associated peptide) + LTBP1 or LTBP3
- LTBP1/3 bind FBN1 TB domains → LLC anchored to fibrillin-1 microfibrils in ECM → TGF-β stored in inactive (sequestered) form
- TGF-β activation from LLC: proteases (plasmin, MMP9, BMP1) or mechanical force (integrin αvβ6 pulling) releases TGF-β from LAP → free active TGF-β → TGFBR1/TGFBR2 → SMAD2/3 phosphorylation → nuclear transcription
- **FBN1 LOF → reduced LTBP-FBN1 tethering → less TGF-β sequestered in ECM → higher ambient active TGF-β levels in Marfan syndrome tissues**
- Neptune (2003): fibrillin-1-deficient mice (fibrillin-1 hypomorphic) → elevated TGF-β in lung → emphysema + elastic fiber disruption → rescued by TGF-β neutralizing antibody or TGFβRII blockade

**ERK vs. SMAD pathways in Marfan aorta:**
- SMAD pathway (canonical TGF-β): SMAD2/3 → transcription of TGF-β target genes (PAI-1, CTGF, fibronectin) → fibrotic remodeling; SMAD2/3 phosphorylation elevated in Marfan aortic media
- ERK pathway (non-canonical TGF-β via Ang-II): AT1R → ERK1/2 → MMP9 → elastic lamina fragmentation; losartan (AT1R blocker) reduces ERK activation in Marfan aortic SMCs → slows aneurysm progression

### FBN1 in ocular zonule

**Zonular fiber composition:**
- Ciliary body → ocular zonular fibers (suspensory ligaments) → equatorial lens capsule; fiber diameter 8-10 nm; nearly pure fibrillin-1 + fibrillin-2 (with no elastin)
- FBN1 LOF → weakened zonular fibers → lens subluxation (ectopia lentis); typically superior-temporal displacement (contrast with inferior displacement in homocystinuria)
- Zonulysis (complete lens dislocation) can cause pupillary block → acute glaucoma → ocular emergency

### FBN1 in skeletal development

**BMP modulation:**
- FBN1 TB domains (particularly TB2, TB4) bind BMP-7, BMP-10 → sequester in ECM; FBN1 LOF → BMP excess → enhanced osteoprogenitor differentiation → tall, thin body habitus (Marfanoid), arachnodactyly, and scoliosis
- BMP + TGF-β excess in bone: premature periosteal ossification along long bones → bony overgrowth; reduced bone density despite tall stature in Marfan syndrome

## Mechanism

### FBN1 germline mutations in Marfan syndrome

**Mutation characteristics:**
- Over 3,000 distinct FBN1 mutations documented in Universal Marfan Database (UMD-FBN1)
- De novo mutations: ~25% of Marfan cases (new mutations, no family history)
- **Neonatal Marfan zone (exons 24-32, cbEGF domains 14-20)**: mutations here (typically cysteine substitutions) cause the most severe phenotype — neonatal Marfan syndrome with severe mitral valve disease, tricuspid valve disease, heart failure from birth, pulmonary emphysema, arachnodactyly; often fatal within 2 years without intervention; no characteristic aortic root dilation at birth (occurs later)
- **Haploinsufficiency vs. dominant negative**: nonsense/frameshift/large deletion → haploinsufficiency → 50% normal FBN1 → milder phenotype; cysteine substitution missense → full-length mutant protein incorporated into microfibrils → dominant-negative poisoning → more severe phenotype

**Therapeutic strategies:**
- **Losartan (AT1R blocker)**: reduces TGF-β production (AT1R activation stimulates TGF-β secretion from aortic SMCs); reduces ERK1/2 activation; COMPARE trial (losartan vs. atenolol): losartan non-inferior; some data suggest superior; currently first-line or used in combination with beta-blocker
- **Atenolol/propranolol (beta-blocker)**: reduce hemodynamic stress on aortic root (reduced heart rate, reduced pulsatile pressure) → slows aortic root growth rate; standard of care for 30+ years
- **Combination (losartan + atenolol)**: some trials show additive benefit; combination used at major Marfan centers
- **Aortic surgery**: prophylactic aortic root replacement (Bentall procedure or valve-sparing root replacement [David/Yacoub]) at aortic root diameter ≥5.0 cm or ≥4.5 cm with family history of dissection, rapid growth (>0.5 cm/year), or severe AR; valve-sparing repair preferred in younger patients to avoid anticoagulation; perioperative mortality <1% at experienced centers
- **Anti-TGF-β antibody (fresolimumab)**: in trials for Marfan aortopathy; directly neutralizes TGF-β regardless of mechanism
- **Rapamycin (mTOR inhibitor)**: rapamycin rescues some FBN1-null mouse phenotypes; mTOR is downstream of TGF-β; clinical trials pending

**Genotype-phenotype limitations:**
- Wide intrafamilial variability: same FBN1 mutation in a family → different severity of aortic, skeletal, ocular features; modifier genes and environmental factors significant
- FBN1 variant of uncertain significance (VUS): common; functional assay (fibrillin-1 microfibril assembly in dermal fibroblasts) used at specialized centers; co-segregation analysis in families

## Connections

- `connects-to` → **[Marfan Syndrome](../../07-system/marfan-syndrome/README.md)** — Germline FBN1 haploinsufficiency or dominant-negative mutations → Marfan syndrome; FBN1 LOF reduces microfibril scaffold → less TGF-β sequestration → excess TGF-β signaling → SMAD2/3 activation → aortic smooth muscle cell phenotypic switch → progressive aortic root aneurysm.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — FBN1 microfibrils bind LTBP (latent TGF-β binding protein) → sequester TGF-β in ECM; FBN1 LOF → reduced TGF-β sequestration → excess TGF-β → ERK and SMAD2/3 activation in aortic SMCs → MMP production → elastic lamina fragmentation → aneurysm formation.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — FBN1 LOF → excess TGF-β signaling → SMAD2/3 phosphorylation → nuclear translocation → aortic gene expression changes driving aneurysm; SMAD4 is the common SMAD that co-activates SMAD2/3 transcription; SMAD4 mutations in juvenile polyposis syndrome also cause aortic aneurysm.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — FBN1 fibrillin-1 microfibrils and collagen fibers are the two major structural components of the arterial wall ECM; fibrillin-1 provides elastic recoil; collagen provides tensile strength; Marfan syndrome (FBN1) and OI (COL1A1/2) both affect connective tissue integrity.

[^dietz-1991-fbn1-marfan]: Dietz HC, Cutting GR, Pyeritz RE, et al. Marfan syndrome caused by a recurrent de novo missense mutation in the fibrillin gene. *Nature.* 1991;352(6333):337-339. [doi:10.1038/352337a0](https://doi.org/10.1038/352337a0) · [PubMed 1852208](https://pubmed.ncbi.nlm.nih.gov/1852208/)
[^neptune-2003-tgfb-marfan]: Neptune ER, Frischmeyer PA, Arking DE, et al. Dysregulation of TGF-beta activation contributes to pathogenesis in Marfan syndrome. *Nat Genet.* 2003;33(3):407-411. [doi:10.1038/ng1116](https://doi.org/10.1038/ng1116) · [PubMed 12598898](https://pubmed.ncbi.nlm.nih.gov/12598898/)

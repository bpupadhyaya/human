---
schema: pathogen-entry/v1
id: akkermansia-muciniphila
name: Akkermansia muciniphila
atlas: 02-pathogen
scale: 06-microbiome
status: draft
last_reviewed: 2026-06-05
summary: "Gram-negative anaerobe (Verrucomicrobia); mucin-degrading specialist in the inner mucus layer. Amuc_1100 outer membrane protein signals TLR2 → tight junctions + IL-10. Produces propionate/acetate; inversely correlated with obesity, T2DM, and IBD."
aliases: ["A. muciniphila", "Akkermansia", "AKK", "MucT", "ATCC BAA-835"]
sources:
  - id: plovier-2017-akkermansia-pasteurized
    type: peer-reviewed
    cite: "Plovier H, Everard A, Druart C, et al. A purified membrane protein from Akkermansia muciniphila or the pasteurised bacterium improves metabolism in obese and diabetic mice. Nat Med. 2017;23(1):107-13."
    doi: "10.1038/nm.4236"
    pmid: "27892954"
    url: "https://doi.org/10.1038/nm.4236"
    accessed: "2026-06-05"
  - id: depommier-2019-akkermansia-human-trial
    type: peer-reviewed
    cite: "Depommier C, Everard A, Druart C, et al. Supplementation with Akkermansia muciniphila in overweight and obese human volunteers: a proof-of-concept exploratory study. Nat Med. 2019;25(7):1096-103."
    doi: "10.1038/s41591-019-0495-2"
    pmid: "31263284"
    url: "https://doi.org/10.1038/s41591-019-0495-2"
    accessed: "2026-06-05"
  - id: guyton-hall
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
  - id: alberts-mol-cell-biology
    type: textbook
    cite: "Alberts B, Johnson A, Lewis J, et al. Molecular Biology of the Cell. 7th ed. W.W. Norton; 2022."
    url: "https://www.ncbi.nlm.nih.gov/books/NBK26880/"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/07-system/digestive-system
    relation: modulates
    note: "A. muciniphila degrades and renews the colonic mucus layer, maintaining its thickness and glycan composition. Propionate and acetate produced from mucin fermentation lower luminal pH, feed colonocytes, and cross-feed butyrate producers, sustaining overall gut barrier and epithelial metabolic health."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "Amuc_1100 outer membrane protein activates TLR2 on intestinal immune cells, inducing IL-10 secretion and reducing systemic LPS-driven endotoxemia. Pasteurized A. muciniphila retains full TLR2-mediated immune-modulatory activity, suppressing low-grade metabolic inflammation linked to obesity."
  - target: 01-human/04-cellular/macrophage
    relation: modulates
    note: "A. muciniphila-derived Amuc_1100 and outer membrane vesicles (OMVs) shift intestinal macrophage polarisation toward M2-like (anti-inflammatory) phenotype, reducing TNF-α and IL-6 production. Propionate signals via GPR43 on macrophages to further suppress NF-κB-driven pro-inflammatory responses."
  - target: 01-human/06-organ/large-intestine
    relation: modulates
    note: "A. muciniphila colonises the inner mucus layer of the large intestine exclusively, degrading MUC2 O-glycans to release monosaccharides for energy. This mucin turnover stimulates goblet cell MUC2 resynthesis, increases mucus layer thickness, and reduces epithelial exposure to luminal LPS."
---

# Akkermansia muciniphila

## Overview

*Akkermansia muciniphila* is a **Gram-negative, non-motile, strictly anaerobic coccobacillus** and the sole cultivated member of the phylum Verrucomicrobia found in the human gut. First isolated in 2004 by Muriel Derrien and Willem de Vos at Wageningen University, *A. muciniphila* occupies a unique ecological niche: it lives **exclusively in the mucus layer** of the large intestine, degrading host-secreted mucin glycoproteins as its primary carbon and nitrogen source [^plovier-2017-akkermansia-pasteurized].

In healthy adults, *A. muciniphila* constitutes **1–4% of the total gut microbiome** — making it one of the most abundant single bacterial species in the colon — and its abundance is considered a hallmark of a healthy metabolic phenotype. Depletion of *A. muciniphila* is consistently observed in individuals with **obesity, type 2 diabetes (T2DM), metabolic syndrome, inflammatory bowel disease (IBD), multiple sclerosis, and colorectal cancer**, positioning it as perhaps the most metabolically significant commensal bacterium identified to date.

Three interrelated mechanisms underlie its clinical importance:

1. **Mucus layer maintenance:** By degrading and stimulating resynthesis of mucin, *A. muciniphila* maintains the thickness and integrity of the protective mucus barrier, preventing bacterial translocation and endotoxemia
2. **Epithelial tight junction reinforcement:** Amuc_1100 — a unique outer membrane protein — activates TLR2 signalling on intestinal epithelial cells, upregulating tight junction proteins (claudin-3, ZO-1) and suppressing intestinal permeability ("leaky gut")
3. **Metabolic reprogramming:** Short-chain fatty acids (SCFAs) produced from mucin fermentation (propionate, acetate) reduce hepatic lipogenesis, improve insulin sensitivity, and suppress adipose tissue inflammation

The discovery that **pasteurized *A. muciniphila*** retains full biological activity (via heat-stable Amuc_1100) led to the development of the first evidence-based probiotic product specifically targeting metabolic syndrome (Pendulum Akkermansia), approved in 2021 [^depommier-2019-akkermansia-human-trial].

## Structure

### Morphology

*A. muciniphila* cells are **ovoid to coccoid rods** (0.6–1.0 µm × 1.0–2.5 µm), occurring singly or in pairs. They are obligate anaerobes with no tolerance for molecular oxygen — even brief aerobic exposure is lethal, making culture technically demanding. Cells appear **Gram-negative** by staining due to a thin peptidoglycan layer and outer membrane, though their cell wall composition is phylogenetically distinct from classical Gram-negative Proteobacteria (Verrucomicrobia have a unique, heavily cross-linked peptidoglycan).

### Cell Wall and Surface Structures

| Structure | Description | Functional Role |
|:---|:---|:---|
| **Outer membrane** | Asymmetric lipopolysaccharide-containing bilayer; unusual lipid A structure with low TLR4 stimulatory activity | Reduces classical endotoxin signalling; structural barrier |
| **Amuc_1100** | 84 kDa outer membrane protein; heat-stable; forms dimers in the outer membrane | TLR2 agonist → IL-10 induction; tight junction upregulation; retained in pasteurized form |
| **Outer membrane vesicles (OMVs)** | 50–200 nm lipid vesicles shed from the outer membrane; carry Amuc_1100 and other proteins | Deliver immune signals to epithelial and immune cells without direct bacterial contact |
| **Mucin-degrading enzymes** | Multiple secreted sulfatases, sialidases, glycosidases, and a mucinase | Release O-glycan sugars (N-acetylgalactosamine, N-acetylglucosamine, fucose, sialic acid) from MUC2 |
| **Pili / adhesins** | Surface-associated proteins mediating attachment to mucin glycoproteins | Niche establishment in inner mucus layer |

### Genome

- **Genome size:** ~2.66 Mb; GC content ~55.8% (type strain ATCC BAA-835)
- ~2,090 predicted coding sequences
- ~4% of genome dedicated to mucin degradation: sulfatase genes (*arsB* homologues), neuraminidases, glycoside hydrolases (GH families 2, 16, 18, 20, 33)
- Amuc_1100 gene (*Amuc_1100*) is uniquely conserved across all *A. muciniphila* strains; no orthologues in other gut bacteria
- Limited carbohydrate transport (PTS) genes — reflecting sole dependence on mucin-derived sugars; no starch/cellulose utilisation
- No biosynthetic gene clusters for amino acids — relies on mucin-derived amino sugars and cross-feeding from neighbouring bacteria

## Infection Mechanism

### Note on Pathogenic Potential

*A. muciniphila* has **no documented pathogenic capacity** in immunocompetent humans. It is absent from conventional infection/pathogen databases and has never been implicated in bacteraemia, abscess, or invasive disease in healthy individuals. It is included in the Pathogen Atlas at scale 06-microbiome to document its role as a beneficial coloniser at the interface between commensal biology and precision medicine.

### Colonisation Mechanism

*A. muciniphila* establishes its niche through a highly specialised sequence of molecular interactions with the colonic mucus layer:

1. **Mucus sensing and chemotaxis:** Despite being non-flagellate, *A. muciniphila* exhibits directed motility toward mucin glycoproteins via type IV pili-like appendages and mucin-binding surface proteins
2. **Initial adhesion:** Surface adhesins (including proteins in the Amuc family) bind O-glycan side chains of MUC2 — specifically terminal sialic acid and fucose residues — anchoring the bacterium to the inner mucus layer
3. **Mucin degradation cascade:** Sequential enzymatic cleavage removes: (a) sialic acid (neuraminidases), (b) fucose (fucosidases), (c) galactose and N-acetylgalactosamine (β-galactosidases, hexosaminidases), (d) N-acetylglucosamine (N-acetylglucosaminidases) — releasing free monosaccharides for energy
4. **Mucin resynthesis stimulation:** Mucin degradation products (particularly short oligosaccharides) signal goblet cells to upregulate MUC2 transcription and secretion, creating a positive feedback loop that maintains mucus layer thickness
5. **Niche maintenance:** Amuc_1100 OMVs signal to epithelial cells to upregulate tight junction proteins, preventing bacterial translocation across the denuded epithelium exposed during mucin renewal cycles
6. **SCFA production:** Propionate and acetate are released as end-products of mucin sugar fermentation; these cross-feed neighbouring bacteria (e.g., *Faecalibacterium prausnitzii*) and provide energy to colonocytes via portal circulation

### Metabolic Cross-Feeding Interactions

*A. muciniphila* occupies a central position in gut metabolic networks:
- **Releases** monosaccharides (fucose, sialic acid) that feed neighbouring fermenters
- **Provides** acetate and propionate for butyrate-producing bacteria via cross-feeding
- **Receives** H₂ from primary fermenters to maintain its own anaerobic respiratory chain

## Host Interactions

### Barrier Function

The most direct host interaction of *A. muciniphila* is maintenance of the colonic mucus barrier:

- **Mucus layer thickness:** In germ-free mice mono-colonised with *A. muciniphila*, mucus layer thickness increases ~3-fold compared to germ-free controls; in high-fat-diet mice, *A. muciniphila* supplementation normalises mucus layer thickness reduced by diet
- **Tight junction upregulation:** Amuc_1100 → TLR2 → MyD88 → NF-κB (moderate activation) and AP-1 → claudin-3 and ZO-1 mRNA upregulation; translocation assay: FITC-dextran paracellular flux reduced ~40% in Amuc_1100-treated HT-29 monolayers
- **Endotoxemia reduction:** By maintaining barrier integrity, *A. muciniphila* reduces systemic LPS translocation — the primary driver of metabolic endotoxemia-induced insulin resistance and adipose inflammation

### Immune Modulation

| Target Cell | Signalling Axis | Downstream Effect |
|:---|:---|:---|
| **Intestinal epithelial cells** | Amuc_1100 → TLR2 → IL-10 | Tight junctions ↑; epithelial survival ↑ |
| **Macrophages (lamina propria)** | OMV-delivered Amuc_1100 → TLR2 | M2 polarisation; TNF-α ↓, IL-10 ↑; propionate → GPR43 → NF-κB ↓ |
| **Dendritic cells** | TLR2 ligation | Tolerogenic DCs; Treg induction; IL-12 ↓ |
| **Adipose tissue macrophages** | Propionate via portal → systemic | Reduced adipose inflammation; leptin sensitivity restored |

### Metabolic Signalling

*A. muciniphila* produces short-chain fatty acids that act as systemic metabolic signals:

- **Propionate** (primary product): Signals via GPR41 and GPR43 on enteroendocrine L-cells → GLP-1 and PYY secretion → reduced appetite and improved insulin secretion; inhibits hepatic glucose production (gluconeogenesis suppression); reduces adipose lipolysis
- **Acetate:** Converted by colonocytes and hepatocytes to acetyl-CoA; cross-feeds *Faecalibacterium prausnitzii* and *Roseburia* for butyrate production
- **Amuc_1100 (pasteurised):** Heat-stable at 70°C/30 min; retains full TLR2 agonist activity; in the first human proof-of-concept trial (n=40, 3 months), pasteurized *A. muciniphila* at 10¹⁰/day improved insulin sensitivity, reduced total and LDL cholesterol, and reduced circulating lipopolysaccharide-binding protein (LBP) vs. placebo [^depommier-2019-akkermansia-human-trial]

## Connections

**Modulates** → [Digestive system](../../../01-human/07-system/digestive-system/README.md): *A. muciniphila* is the primary microbial architect of the colonic mucus layer. By degrading and stimulating resynthesis of MUC2, producing SCFAs from mucin sugars, and reinforcing epithelial tight junctions via Amuc_1100/TLR2 signalling, it maintains the physical and biochemical barrier that separates the gut microbiome from the systemic circulation.

**Modulates** → [Immune system](../../../01-human/07-system/immune-system/README.md): Amuc_1100-mediated TLR2 activation on intestinal epithelial cells and macrophages drives IL-10 production and M2 macrophage polarisation, suppressing the low-grade endotoxemia-driven inflammation that underlies metabolic disease. OMV-delivered signals extend immune modulation to subepithelial immune compartments without bacterial translocation.

**Modulates** → [Macrophage](../../../01-human/04-cellular/macrophage/README.md): *A. muciniphila* shifts intestinal and adipose macrophage phenotype via two complementary routes — Amuc_1100/TLR2 direct signalling and propionate/GPR43 metabolic signalling — both converging on NF-κB suppression and IL-10/IL-4 upregulation, reducing the chronic inflammatory state that drives insulin resistance.

**Modulates** → [Large intestine](../../../01-human/06-organ/large-intestine/README.md): *A. muciniphila* resides exclusively in the large intestine's inner mucus layer, metabolising colonic MUC2 glycoproteins, cross-feeding the broader microbiome, and providing propionate and acetate to colonocytes and the portal system. Its abundance correlates with colonic barrier integrity and local immune homeostasis.

## Pathology

### Dysbiosis-Associated Conditions

*A. muciniphila* depletion is a consistent finding across a spectrum of metabolic and inflammatory diseases. Its absence removes critical mucus barrier maintenance, epithelial tight junction support, and anti-inflammatory metabolite production:

| Condition | Degree of Depletion | Proposed Mechanism | Evidence Level |
|:---|:---|:---|:---|
| **Obesity / metabolic syndrome** | 10–100× reduction vs. lean controls | Loss of propionate-mediated GLP-1 stimulation; increased endotoxemia; adipose inflammation | High (multiple cohort studies, mouse models) |
| **Type 2 diabetes (T2DM)** | Severely reduced; inversely correlated with HbA1c | Reduced GLP-1/PYY signalling; propionate-mediated gluconeogenesis inhibition lost; insulin sensitivity impaired | High (MetaHIT consortium data) |
| **Inflammatory bowel disease (IBD)** | Reduced in active UC and CD | Loss of mucus layer integrity → bacterial translocation; increased LPS-driven mucosal inflammation | Moderate |
| **Multiple sclerosis** | Reduced in MS patients vs. healthy controls | Gut-brain axis: reduced propionate levels; altered Treg/Th17 balance | Emerging |
| **Colorectal cancer** | Reduced in CRC tumour-adjacent mucosa | Loss of epithelial barrier; increased inflammatory microenvironment; reduced butyrate cross-feeding | Emerging |
| **Non-alcoholic fatty liver disease (NAFLD)** | Reduced; inversely correlated with liver fat | Increased gut permeability → portal LPS delivery → hepatic TLR4 activation → steatohepatitis | Moderate |

### Metformin and A. muciniphila

An important pharmacological interaction: **metformin** (the first-line T2DM drug) markedly increases *A. muciniphila* abundance in both humans and mice. This *A. muciniphila* bloom is hypothesised to contribute to metformin's glycaemic benefits beyond its direct mitochondrial complex I inhibition — a striking example of a drug exerting metabolic effects partly through microbiome remodelling. Germ-free mice given metformin show blunted glycaemic improvement compared to conventionally colonised mice [^plovier-2017-akkermansia-pasteurized].

### Clinical Translation: Pasteurized A. muciniphila

The first-in-human safety and efficacy trial (Depommier et al., 2019) established the feasibility of using **pasteurized *A. muciniphila*** (10¹⁰/day, 3 months) as a metabolic therapeutic [^depommier-2019-akkermansia-human-trial]:
- Improved insulin sensitivity (HOMA-IR reduced)
- Reduced total and LDL cholesterol
- Reduced LBP (surrogate for endotoxemia)
- No safety signals in n=40 overweight/obese volunteers

Live *A. muciniphila* was equally effective; the pasteurized form offers superior stability for commercial formulation. Pendulum (formerly Synlogic spinout) markets a probiotic product based on this evidence, currently available without prescription in the US.

[^plovier-2017-akkermansia-pasteurized]: Plovier H, Everard A, Druart C, et al. A purified membrane protein from *Akkermansia muciniphila* or the pasteurised bacterium improves metabolism in obese and diabetic mice. *Nat Med.* 2017;23(1):107-13. [doi:10.1038/nm.4236](https://doi.org/10.1038/nm.4236) · [PubMed 27892954](https://pubmed.ncbi.nlm.nih.gov/27892954/)
[^depommier-2019-akkermansia-human-trial]: Depommier C, Everard A, Druart C, et al. Supplementation with *Akkermansia muciniphila* in overweight and obese human volunteers: a proof-of-concept exploratory study. *Nat Med.* 2019;25(7):1096-103. [doi:10.1038/s41591-019-0495-2](https://doi.org/10.1038/s41591-019-0495-2) · [PubMed 31263284](https://pubmed.ncbi.nlm.nih.gov/31263284/)

---
*This page is co-maintained with AI assistance. Content is reviewed for accuracy but may not reflect the latest clinical guidelines. See the [project disclaimer](../../../../README.md) for details.*

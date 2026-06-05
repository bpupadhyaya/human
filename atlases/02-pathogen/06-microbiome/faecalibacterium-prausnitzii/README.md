---
schema: pathogen-entry/v1
id: faecalibacterium-prausnitzii
name: Faecalibacterium prausnitzii
atlas: 02-pathogen
scale: 06-microbiome
status: draft
last_reviewed: 2026-06-05
summary: "Gram-positive anaerobe (Firmicutes); 5–15% of healthy colon. Primary butyrate producer (acetyl-CoA pathway) — main colonocyte fuel. Anti-inflammatory MAMs suppress NF-κB/IL-8. Markedly depleted in IBD, IBS, CRC; extremely oxygen-sensitive, limiting commercial formulation."
aliases: ["F. prausnitzii", "Fp", "Fusobacterium prausnitzii (historical)", "ATCC 27766", "A2-165"]
sources:
  - id: sokol-2008-fp-tnbs-colitis
    type: peer-reviewed
    cite: "Sokol H, Pigneur B, Watterlot L, et al. Faecalibacterium prausnitzii is an anti-inflammatory commensal bacterium identified by gut microbiota analysis of Crohn disease patients. Proc Natl Acad Sci USA. 2008;105(43):16731-6."
    doi: "10.1073/pnas.0804812105"
    pmid: "18936492"
    url: "https://doi.org/10.1073/pnas.0809584105"
    accessed: "2026-06-05"
  - id: bui-2019-fp-mam
    type: peer-reviewed
    cite: "Bui TPN, Shetty SA, Lagkouvardos I, et al. Salicylate-derived microbial anti-inflammatory molecules from Faecalibacterium prausnitzii. Sci Rep. 2019;9(1):17629."
    doi: "10.1038/s41598-019-52979-9"
    pmid: "31776385"
    url: "https://doi.org/10.1038/s41598-019-52979-9"
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
  - target: 01-human/06-organ/large-intestine
    relation: modulates
    note: "F. prausnitzii is the dominant butyrate producer in the human large intestine, providing the primary energy substrate for colonocytes via the acetyl-CoA pathway. Butyrate-driven HDAC inhibition in colonocytes upregulates tight junction proteins and suppresses proliferation, directly maintaining colonic barrier function and cancer resistance."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "F. prausnitzii MAMs (microbial anti-inflammatory molecules; salicylate-like compounds) suppress NF-κB signalling and IL-8 production in intestinal epithelial cells. Butyrate drives colonocyte and macrophage HDAC inhibition, reducing NF-κB-dependent pro-inflammatory gene expression and promoting mucosal immune tolerance."
  - target: 01-human/07-system/digestive-system
    relation: modulates
    note: "F. prausnitzii depletion is a consistent predictor of active IBD (Crohn's disease ≥70% reduction vs. remission), IBS, and colorectal cancer. Its butyrate output sustains the entire colonocyte energy budget; its loss triggers colonocyte metabolic failure, mucus thinning, and barrier disruption that precedes or exacerbates inflammatory relapse."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: modulates
    note: "Butyrate produced by F. prausnitzii inhibits HDAC in colonocytes and dendritic cells, promoting FoxP3 gene expression and FoxP3+ Treg differentiation in the colonic lamina propria. F. prausnitzii conditioned medium expands Tregs and IL-10-producing T cells in vitro; butyrate-driven Treg induction is the cellular mechanism linking F. prausnitzii to mucosal tolerance."
---

# Faecalibacterium prausnitzii

## Overview

*Faecalibacterium prausnitzii* is a **Gram-positive, non-motile, strictly anaerobic rod** belonging to the phylum Firmicutes (Bacillota), class Clostridia, family Ruminococcaceae. It is the **sole species in the genus *Faecalibacterium*** and, under optimal gut conditions, constitutes **5–15% of the total colonic microbiome** in healthy adults — making it one of the most abundant single bacterial species in the human large intestine and arguably the most important single commensal bacterium for colonic barrier health.

*F. prausnitzii* was first isolated and formally described in 2002 by Lay and colleagues, though earlier studies identified it as an abundant Clostridium cluster IV member. Originally misclassified as *Fusobacterium prausnitzii* due to morphological similarity, it was renamed in 2002 after 16S rRNA phylogenetic reclassification. Its defining clinical significance was established by the landmark 2008 paper by Sokol and colleagues, which showed that *F. prausnitzii* abundance is **severely and specifically reduced in active Crohn's disease** and that its depletion predicts post-operative disease relapse — positioning it as a living biomarker of gut health [^sokol-2008-fp-tnbs-colitis].

The organism's importance rests on two complementary anti-inflammatory mechanisms:

1. **Butyrate production:** *F. prausnitzii* is the primary butyrate-producing bacterium in the human colon, generating butyrate via the acetyl-CoA pathway from cross-fed acetate. Butyrate is the **preferred energy substrate for colonocytes** (colonocytes derive ~70% of their energy from butyrate oxidation rather than glucose), and simultaneously functions as a **histone deacetylase (HDAC) inhibitor** — suppressing NF-κB-driven inflammatory gene expression in both colonocytes and immune cells
2. **Microbial anti-inflammatory molecules (MAMs):** *F. prausnitzii* secretes salicylate-like small molecules (identified by Bui et al., 2019) that directly block NF-κB nuclear translocation and IL-8 secretion from intestinal epithelial cells — an aspirin-like anti-inflammatory mechanism from a gut commensal [^bui-2019-fp-mam]

## Structure

### Morphology

*F. prausnitzii* cells are **non-motile rods** (0.5–0.8 µm × 2–6 µm), occurring singly or in pairs; some strains form loose chains. The organism is an **obligate anaerobe** with the most extreme oxygen sensitivity of any well-studied gut commensal — it cannot survive more than a few minutes of aerobic exposure, consistent with its exclusive occupancy of the profoundly oxygen-free lumen of the mid-to-distal colon. This extreme oxygen sensitivity (tolerance threshold: <0.1 ppm O₂) has been the primary obstacle to commercial probiotic formulation: freeze-drying, encapsulation, and storage under inert gas all fail to maintain viable *F. prausnitzii* counts comparable to those found in the healthy colon.

### Cell Wall and Surface Structures

| Structure | Description | Functional Role |
|:---|:---|:---|
| **Peptidoglycan** | Thick Gram-positive murein wall; cross-linked via *meso*-diaminopimelic acid (DAP) | Structural integrity; TLR2/NOD2 ligand |
| **Surface-layer (S-layer)** | Paracrystalline protein array (strain-dependent); ~50–100 kDa SLP proteins | Mucin binding; immune modulation; phage defence |
| **Flagella** | Absent; non-motile | — |
| **Exopolysaccharides (EPS)** | Strain-specific; limited capsule | Immune modulation; biofilm formation |
| **Microbial anti-inflammatory molecules (MAMs)** | Secreted low-molecular-weight salicylate derivatives and related polyphenolics | NF-κB suppression; IL-8 inhibition; aspirin-like anti-inflammatory activity [^bui-2019-fp-mam] |
| **Extracellular electron shuttle proteins** | Riboflavin and flavin mononucleotide (FMN) — secreted as electron shuttles | Transfer electrons to oxygen-depleted substrates (iron, sulfur) under strict anaerobiosis; metabolic flexibility |

### Genome

- **Genome size:** ~3.1 Mb (A2-165 reference strain); GC content ~57%
- ~2,700–3,200 predicted coding sequences; considerable inter-strain genomic diversity (pan-genome study by Fitzgerald et al., 2018 identified two distinct phylogroups: clade I and clade II)
- **Butyrate biosynthesis gene cluster:** acetyl-CoA acetyltransferase (*thlA*), 3-hydroxybutyryl-CoA dehydrogenase (*hbd*), crotonase (*crt*), butyryl-CoA dehydrogenase (*bcd*), electron-transfer flavoprotein (*etfA/B*), butyryl-CoA:acetate CoA-transferase (*but*) — the complete acetyl-CoA → butyrate pathway
- **Cross-feeding dependence:** *F. prausnitzii* lacks de novo synthesis pathways for several amino acids and vitamins — it relies on acetate from *Bifidobacterium* and *Lactobacillus* species as a carbon/electron donor for butyrate synthesis
- Notably **lacks** both the lysine-dependent butyrate pathway (Clostridium-type) and the succinate pathway — uses only the acetyl-CoA route via butyryl-CoA:acetate CoA-transferase
- Enriched in genes for polysaccharide degradation (xylan, arabinose) and sugar phosphotransferase systems (PTS) for dietary fibre substrate access

## Infection Mechanism

### Note on Pathogenic Potential

*F. prausnitzii* has **no demonstrated pathogenic capacity** under any clinical circumstance. It has never been isolated from blood cultures, abscesses, or invasive infection sites. Its extreme oxygen sensitivity makes translocation across the gut epithelium (which exposes the bacterium to tissue pO₂ levels lethal to the organism) effectively impossible. It is among the least pathogenic organisms characterised in microbiome research. This section describes its **colonisation mechanism** — how it establishes and maintains its dominant niche in the healthy colon.

### Colonisation Mechanism

*F. prausnitzii* establishes its niche through metabolic dependence and cross-feeding relationships rather than active mucin adhesion or immune manipulation:

1. **Niche location — colonic lumen:** Unlike *A. muciniphila* (mucus layer) or *B. fragilis* (lumen + mucus), *F. prausnitzii* resides primarily in the **colonic lumen and loosely attached to the mucus outer layer** — not the inner, sterile mucus layer. Its extreme oxygen sensitivity makes it dependent on the profound anaerobiosis of the mid-distal colon
2. **Cross-feeding dependency:** *F. prausnitzii* does not efficiently ferment dietary polysaccharides independently — it relies on **acetate produced by *Bifidobacterium* spp., *Bacteroides* spp., and *Lactobacillus* spp.** as its primary substrate for butyrate synthesis via the butyryl-CoA:acetate CoA-transferase reaction
3. **Electron disposal — extracellular electron shuttling:** Under strict anaerobiosis, *F. prausnitzii* disposes of reducing equivalents (NADH, FADH₂) by reducing secreted riboflavin/FMN electron shuttles, which then reduce insoluble iron oxides in the colon — a form of extracellular respiration that enables sustained fermentation in the absence of conventional terminal electron acceptors
4. **Dietary fibre requirements:** *F. prausnitzii* abundance correlates tightly with dietary fermentable fibre intake (inulin, FOS, resistant starch); high-fibre diets sustain the acetate pool that cross-feeds *F. prausnitzii*; low-fibre Western diets reduce *F. prausnitzii* abundance by limiting substrate availability
5. **Butyryl-CoA:acetate CoA-transferase (but) pathway:** The predominant butyrate pathway in *F. prausnitzii* — acetate from cross-feeding is used as both a carbon source and a CoA acceptor, allowing net butyrate production without acetate accumulation

### Metabolic Cross-Feeding Network

*F. prausnitzii* sits at the hub of a colonic cross-feeding network:
- **Receives acetate** from *Bifidobacterium* spp., *Bacteroides* spp., *Ruminococcus bromii*
- **Produces butyrate** consumed by colonocytes (primary energy) and macrophages (HDAC inhibition)
- **Produces CO₂ + H₂** from fermentation — consumed by *Methanobrevibacter smithii* (methanogen) and *Desulfovibrio* spp. (sulfate reducer) to maintain low H₂ partial pressure, thermodynamically driving continued fermentation

## Host Interactions

### Butyrate-Mediated Colonocyte Energetics and Barrier Function

The most direct interaction between *F. prausnitzii* and the host is the provisioning of **butyrate to colonocytes** — the primary energy substrate that colonocytes cannot readily obtain from the portal circulation:

| Effect | Mechanism | Magnitude |
|:---|:---|:---|
| **Colonocyte ATP production** | Butyrate β-oxidation via mitochondrial TCA cycle; ~70% of colonocyte energy from butyrate | Dominant; colonocytes enter metabolic stress without butyrate |
| **HDAC inhibition** | Butyrate competitively inhibits class I/II HDACs → histone H3/H4 hyperacetylation → altered gene expression | IC₅₀ ~1–2 mM; achievable at physiological colonic concentrations (10–20 mM) |
| **Tight junction upregulation** | HDAC inhibition → claudin-1, claudin-3, ZO-1, occludin transcriptional upregulation | Reduced paracellular permeability (TEER increase in vitro) |
| **Colonocyte apoptosis (homeostatic)** | Normal colonocytes: butyrate induces apoptosis → mucosal renewal; cancer cells: Warburg-effect tumour cells fail to oxidise butyrate → butyrate accumulates → tumour cell apoptosis | "Butyrate paradox": butyrate promotes normal epithelial turnover while selectively killing tumour cells |
| **Mucin production** | Butyrate upregulates MUC2 and MUC5AC transcription in goblet cells | Increased mucus layer thickness; barrier reinforcement |

### NF-κB Suppression via MAMs

Beyond butyrate, *F. prausnitzii* exerts direct immune modulation through secreted MAMs:

- **MAM identity (Bui et al., 2019):** Salicylate-derived polyphenolic molecules — structurally similar to aspirin's active metabolite (salicylate) — produced by *F. prausnitzii* during fermentation [^bui-2019-fp-mam]
- **Mechanism:** MAMs block IκB kinase (IKK) complex activation → IκBα is not phosphorylated → NF-κB p65 remains cytoplasmic and inactive → IL-8, TNF-α, IL-6 transcription ↓
- **In vivo relevance:** Sokol et al. (2008) showed that *F. prausnitzii* supernatant (MAM-containing) protects mice from TNBS-induced colitis nearly as effectively as *F. prausnitzii* cells themselves — demonstrating that secreted molecules, not the bacterium per se, mediate anti-inflammatory effects [^sokol-2008-fp-tnbs-colitis]

### Immune Modulation Summary

| Target | Mechanism | Effect |
|:---|:---|:---|
| **Colonocytes** | Butyrate HDAC inhibition; MAM NF-κB suppression | IL-8 ↓; IL-6 ↓; tight junctions ↑; apoptosis homeostasis |
| **Lamina propria macrophages** | Butyrate HDAC inhibition; GPR109a signalling | M2 polarisation; IL-10 ↑; TNF-α ↓; NLRP3 inflammasome suppression |
| **Dendritic cells** | Butyrate conditioning | Tolerogenic DCs; IL-10 ↑; Treg-inducing capacity ↑ |
| **FoxP3+ Tregs (colonic)** | Butyrate → HDAC inhibition → FoxP3 gene accessible chromatin → FoxP3 mRNA ↑ | Treg expansion in colonic lamina propria; mucosal tolerance |
| **Th17 cells** | Butyrate → IL-6 ↓; IL-23 ↓ | Th17 suppression; reduced IL-17A/F; reduced intestinal neutrophil recruitment |

## Connections

**Modulates** → [Large intestine](../../../01-human/06-organ/large-intestine/README.md): *F. prausnitzii* is the dominant butyrate producer in the colonic lumen, providing the primary energy substrate for colonocytes. Butyrate-driven HDAC inhibition reinforces tight junction expression, promotes homeostatic colonocyte apoptosis, and suppresses tumour-promoting Wnt/NF-κB signalling, making *F. prausnitzii* abundance the strongest single microbial predictor of colonic barrier and cancer resistance.

**Modulates** → [Immune system](../../../01-human/07-system/immune-system/README.md): *F. prausnitzii* suppresses mucosal inflammation through two parallel mechanisms — butyrate-mediated HDAC inhibition in immune cells (macrophages, DCs, Tregs) and MAM-mediated NF-κB blockade in epithelial cells. Together, these establish the anti-inflammatory baseline of a healthy colon; their loss in IBD drives the inflammatory relapse cycle.

**Modulates** → [Digestive system](../../../01-human/07-system/digestive-system/README.md): *F. prausnitzii* depletion is the most robust microbiome biomarker of active Crohn's disease and a predictor of post-surgical relapse. Its loss removes the dominant colonocyte fuel supply, triggering energetic failure of the colonic epithelium, mucus thinning, and barrier disruption — a cascade that precipitates or amplifies inflammatory disease across the gastrointestinal tract.

**Modulates** → [Regulatory T cell](../../../01-human/04-cellular/regulatory-t-cell/README.md): Butyrate produced by *F. prausnitzii* inhibits HDAC3 in colonic lamina propria dendritic cells and directly promotes FoxP3 gene expression in naive CD4+ T cells through accessible chromatin remodelling. This butyrate-driven Treg induction is the mechanistic bridge linking dietary fibre → *F. prausnitzii* abundance → colonic immune tolerance — the gut fibre-Treg axis.

## Pathology

### Dysbiosis-Associated Conditions

*F. prausnitzii* is the gut commensal most consistently depleted across a broad spectrum of inflammatory and metabolic diseases, and its abundance has been proposed as a **universal biomarker of gut health**:

| Condition | Degree of Depletion | Proposed Mechanism | Evidence Level |
|:---|:---|:---|:---|
| **Crohn's disease (CD)** | ≥70% reduction in active disease vs. remission or healthy controls; lowest abundance in ileal CD (the biologically most severe subtype) | Loss of butyrate supply → colonocyte metabolic failure; loss of MAM NF-κB suppression → unrestrained mucosal IL-8/TNF-α; loss of Treg support → Th1/Th17 inflammatory cascade | High: founding Sokol 2008 study; replicated across multiple independent cohorts globally; *F. prausnitzii* depletion predicts CD relapse after surgical resection (6-month OR ~8) |
| **Ulcerative colitis (UC)** | Moderately reduced in active disease; less severe than CD | Similar mechanisms; butyrate deficiency particularly relevant for distal colitis where *F. prausnitzii* is normally most abundant | High: multiple cohort studies; meta-analysis confirms |
| **Irritable bowel syndrome (IBS)** | Reduced in IBS-D (diarrhoea-predominant) and post-infectious IBS | Loss of anti-inflammatory tone; visceral hypersensitivity may involve butyrate signalling on enteric neurons via free fatty acid receptors | Moderate |
| **Colorectal cancer (CRC)** | Reduced in CRC tumour-adjacent mucosa vs. healthy colon | Loss of butyrate "butyrate paradox" tumour suppression (butyrate induces Warburg-effect tumour cell apoptosis); loss of NF-κB/Wnt suppression | Moderate–high: case-control studies; meta-analysis; mechanistic data strong |
| **Obesity / metabolic syndrome** | Reduced (inversely correlated with BMI); restored by caloric restriction | Loss of butyrate-driven GPR109a macrophage M2 polarisation in adipose tissue; reduced colonocyte energy → increased gut permeability → endotoxemia | Moderate |
| **Type 2 diabetes (T2DM)** | Reduced; correlates inversely with HOMA-IR | Butyrate-driven GLP-1 and PYY secretion from enteroendocrine cells reduced; increased gut permeability-driven metabolic endotoxemia | Moderate (MetaHIT consortium; Chinese cohort studies) |
| **Autism spectrum disorder (ASD)** | Reduced in ASD children vs. neurotypical; gut-brain axis implications | Butyrate → HDAC inhibition → neuronal gene expression; reduced enteric serotonin; gut permeability changes and neuroinflammation | Emerging; mechanistic data limited |

### The F. prausnitzii Therapeutic Problem

Despite its clear clinical importance, *F. prausnitzii* is **not commercially available as a live probiotic** for a fundamental biological reason: its extreme oxygen sensitivity means viable cell counts in any formulation decline to near-zero within hours of aerobic processing, packaging, or gastric transit. Current approaches in development include:

- **Microencapsulation:** Alginate and chitosan multi-layer microcapsules with oxygen scavenger co-encapsulation; achieves some protection but viable counts still ~10–100× lower than therapeutic target
- **Next-generation probiotics (NGPs):** Several biotech companies (4D Pharma, MicroBiotica, Vedanta Biosciences) are pursuing *F. prausnitzii* NGP development under strict anaerobic manufacturing conditions and nitrogen-purged blister packaging
- **Postbiotic approaches:** Pasteurized *F. prausnitzii* cell-free supernatant (containing MAMs and butyrate metabolites) retains anti-inflammatory activity in animal models — analogous to the *A. muciniphila* pasteurized strategy
- **FMT (fecal microbiota transplantation):** FMT reliably transfers *F. prausnitzii* as part of the donor microbiome; several IBD FMT trials demonstrate partial *F. prausnitzii* restoration and clinical response correlation
- **Dietary prebiotic strategy:** High-inulin, FOS, and resistant starch diets reliably increase *F. prausnitzii* abundance in human intervention studies — the most accessible current approach for microbiome-targeted therapy

[^sokol-2008-fp-tnbs-colitis]: Sokol H, Pigneur B, Watterlot L, et al. *Faecalibacterium prausnitzii* is an anti-inflammatory commensal bacterium identified by gut microbiota analysis of Crohn disease patients. *Proc Natl Acad Sci USA.* 2008;105(43):16731-6. [doi:10.1073/pnas.0804812105](https://doi.org/10.1073/pnas.0804812105) · [PubMed 18936492](https://pubmed.ncbi.nlm.nih.gov/18936492/)
[^bui-2019-fp-mam]: Bui TPN, Shetty SA, Lagkouvardos I, et al. Salicylate-derived microbial anti-inflammatory molecules from *Faecalibacterium prausnitzii*. *Sci Rep.* 2019;9(1):17629. [doi:10.1038/s41598-019-52979-9](https://doi.org/10.1038/s41598-019-52979-9) · [PubMed 31776385](https://pubmed.ncbi.nlm.nih.gov/31776385/)

---
*This page is co-maintained with AI assistance. Content is reviewed for accuracy but may not reflect the latest clinical guidelines. See the [project disclaimer](../../../../README.md) for details.*

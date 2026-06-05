---
schema: pathogen-entry/v1
id: bifidobacterium-longum
name: Bifidobacterium longum
atlas: 02-pathogen
scale: 06-microbiome
status: draft
last_reviewed: 2026-06-05
summary: "Gram-positive anaerobe (Actinobacteria); prominent in infant gut as HMO specialist. Produces acetate/lactate cross-fed to butyrate producers; induces Tregs via TLR2/IL-10. Reduces infant colic and allergen-specific IgE; used in commercial probiotics."
aliases: ["B. longum", "B. infantis", "Bifidobacterium infantis", "B. longum subsp. longum", "B. longum subsp. infantis"]
sources:
  - id: sela-2008-binfantis-hmo
    type: peer-reviewed
    cite: "Sela DA, Chapman J, Adeuya A, et al. The genome sequence of Bifidobacterium longum subsp. infantis reveals adaptations for milk utilization within the infant microbiome. Proc Natl Acad Sci USA. 2008;105(48):18964-9."
    doi: "10.1073/pnas.0809584105"
    pmid: "19033196"
    url: "https://doi.org/10.1073/pnas.0809584105"
    accessed: "2026-06-05"
  - id: fanning-2012-bifidobacterium-mucin
    type: peer-reviewed
    cite: "Fanning S, Hall LJ, Cronin M, et al. Bifidobacterial surface-exopolysaccharide facilitates commensal-host interaction through immune modulation and facilitates gut colonization. Proc Natl Acad Sci USA. 2012;109(6):2108-13."
    doi: "10.1073/pnas.1115621109"
    pmid: "22308390"
    url: "https://doi.org/10.1073/pnas.1115621109"
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
    note: "B. longum subsp. infantis consumes human milk oligosaccharides (HMOs) via dedicated HMO-1 gene cluster transporters, outcompeting pathogens for the breast-milk niche. Acetate and lactate produced lower luminal pH; colonisation reduces infant colic, stool frequency, and pathogen load in the neonatal gut."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "B. longum activates TLR2 on DCs and epithelial cells, inducing IL-10 and TGF-β, promoting FoxP3+ Treg differentiation and mucosal tolerance. Surface EPS shields the bacterium from immune clearance while modulating DC phenotype toward tolerogenic. Reduces allergen-specific IgE in infants."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: modulates
    note: "B. longum-conditioned dendritic cells produce IL-10 and TGF-β that drive FoxP3+ Treg differentiation in Peyer's patches and mesenteric lymph nodes. These Tregs suppress Th2-biased allergic responses and oral tolerance breakdown, reducing IgE sensitisation in early life. Treg induction depends partly on EPS-mediated DC conditioning."
  - target: 01-human/06-organ/large-intestine
    relation: modulates
    note: "B. longum colonises the large intestinal mucosa in adults and the entire colon in infants. Acetate from HMO/polysaccharide fermentation cross-feeds Roseburia intestinalis and Faecalibacterium prausnitzii for butyrate production. Bacteriocin production (bifidin, thermophilin-like peptides) suppresses competing pathogens in the colonic niche."
---

# Bifidobacterium longum

## Overview

*Bifidobacterium longum* is a **Gram-positive, non-motile, strictly anaerobic rod** belonging to the phylum Actinobacteria (Actinomycetota) and the family Bifidobacteriaceae. It is among the **first colonisers of the human gut** after birth and remains one of the dominant genera throughout life, particularly in breast-fed infants. The species is subdivided into two primary subspecies with distinct ecological niches:

- ***B. longum* subsp. *infantis* (B. infantis):** Adapted exclusively to the breast-fed infant gut; possesses a dedicated HMO (human milk oligosaccharide) utilisation gene cluster absent from adult-adapted strains
- ***B. longum* subsp. *longum*:** Adult gut generalist; persists throughout life; consumes plant polysaccharides and host-derived glycans

First described by Henry Tissier in 1900 from the faeces of breast-fed infants — where it comprised the dominant genus (>90% of bacteria in some studies) — *B. longum* has since become one of the most extensively studied probiotic organisms. Its characteristic **bifid (Y-shaped) cell morphology** reflects asymmetric branching during division and gives the entire genus its name (*bifidus* = split/forked in Latin) [^sela-2008-binfantis-hmo].

The clinical significance of *B. longum* spans several domains:

1. **Infant gut colonisation and programming:** *B. infantis* is the keystone consumer of HMOs in the breast-fed infant gut; its depletion (common in Western infants through formula feeding, caesarean delivery, and antibiotic exposure) is associated with increased risk of atopy, inflammatory bowel disease, and immune dysregulation in later life
2. **Immune education:** *B. longum*'s TLR2-mediated IL-10/Treg induction is one of the most well-documented mechanisms by which early gut colonisers "educate" the neonatal immune system toward tolerance
3. **Probiotic applications:** Multiple commercial probiotic preparations contain *B. longum* strains (often in combination with *Lactobacillus* species); specific strains have demonstrated efficacy for reducing infant colic, ↑IgA secretion, and ↓IgE-mediated sensitisation

## Structure

### Morphology

*B. longum* cells exhibit a unique **bifid (Y-shaped) or club-shaped morphology** (0.5–1.3 µm × 1.5–8 µm) — a distinctive branched appearance resulting from polar growth and asymmetric binary fission. Cells occur singly, in pairs, or in irregular clusters; the bifid shape is most pronounced in laboratory culture and may be less apparent in vivo. *B. longum* is a **strict anaerobe** — growth inhibited by atmospheric oxygen concentrations >0.5% — explaining its preferential colonisation of the oxygen-depleted colon and infant caecum.

### Cell Wall and Surface Structures

| Structure | Description | Functional Role |
|:---|:---|:---|
| **Peptidoglycan** | Thick (20–80 nm) cross-linked murein sacculus; Gram-positive architecture | Structural rigidity; TLR2/NOD2 ligand (muramyl dipeptide) |
| **Surface exopolysaccharides (EPS)** | Strain-specific β-glucan and rhamnan polysaccharide capsule; variable chain length | Immune modulation: shields bacterium from phagocytosis; conditions DCs toward tolerogenic phenotype; biofilm formation [^fanning-2012-bifidobacterium-mucin] |
| **Sortase-dependent pili** | Fimbrial appendages anchored by sortase A (SrtA); BopA-family tip adhesins | Mucin binding (MUC2); intestinal epithelial cell attachment; colonisation persistence |
| **Lipoprotein BopA** | Surface-anchored lipoprotein; binds fibronectin and mucin | Adhesion to intestinal epithelium; invasion resistance against pathogens |
| **Bacteriocins** | Bifidin I; thermophilin-like lantibiotic peptides (strain-dependent) | Competitive exclusion: bacteriostatic against *Listeria*, *E. coli*, *Clostridium* |
| **Bile salt hydrolase (BSH)** | Cytoplasmic enzyme; deconjugates primary bile salts to secondary bile acids | Bile tolerance; intestinal survival; bile acid metabolite signalling |

### Genome

- **Genome size:** ~2.26 Mb (*B. longum* NCC2705, adult reference); *B. infantis* ATCC 15697: ~2.83 Mb; GC content ~60% (high GC, characteristic of Actinobacteria)
- ~1,700–2,100 predicted coding sequences
- **HMO-1 gene cluster** (*B. infantis* specific): 43 kb cluster containing HMO transporters (ABC-type), lacto-*N*-biose phosphorylase (LNBP), *N*-acetylhexosamine kinase, and fucosidase — enabling consumption of all major HMO structural types (LNT, LNnT, LNFP-I through -V, 6'-SL, 3'-SL)
- Adult *B. longum*: more extensive plant polysaccharide utilisation loci (xylan, arabinoxylan, pectin); reduced HMO utilisation capacity
- **Low horizontal gene transfer:** *B. longum* genomes are unusually stable; relatively few mobile genetic elements compared to Firmicutes gut colonisers

## Infection Mechanism

### Note on Pathogenic Potential

*B. longum* is **GRAS (Generally Recognized as Safe)** and has no documented pathogenic potential in healthy or immunocompetent individuals. Rare cases of Bifidobacterium bacteraemia are reported in severely immunocompromised patients, but these are opportunistic events, not classical infection. *B. longum* is documented here as a beneficial coloniser; the section below describes its colonisation (not infection) mechanism.

### Colonisation Mechanism

*B. longum* establishes persistent colonisation through a multi-step process tailored to its subspecies-specific niche:

**In breast-fed infants (*B. infantis*):**

1. **Neonatal gut entry:** *B. infantis* is primarily transmitted vertically from the maternal vaginal/perineal microbiome during birth and horizontally via breast milk (HMO delivery); caesarean-born, formula-fed infants show marked *B. infantis* depletion
2. **HMO recognition and import:** The HMO-1 gene cluster encodes ABC-type transporters (SBP-type substrate-binding proteins) with high affinity for intact HMO oligosaccharides (LNT, 2'-FL, 6'-SL); *B. infantis* uniquely imports intact HMO molecules before intracellular hydrolysis, unlike other bacteria that secrete glycosidases extracellularly — minimising cross-feeding of competitors
3. **Intracellular HMO catabolism:** Imported HMOs are sequentially hydrolysed by intracellular β-galactosidase (LacA), lacto-N-biose phosphorylase (LNBP), *N*-acetylhexosamine kinase, and fucosidase into monosaccharides channelled to the bifidus shunt
4. **Metabolic output:** Fermentation via the **bifidus shunt** (fructose-6-phosphate phosphoketolase pathway — unique to Bifidobacteria; not found in Firmicutes or Proteobacteria) produces acetate and lactate (3:2 molar ratio) — higher acetate yield than classical glycolysis
5. **Niche monopolisation:** Competitive HMO consumption, bacteriocin production, and lactic/acetic acid output create a low-pH, *B. infantis*-dominated ecosystem that excludes *Clostridium*, *E. coli*, and other potential pathogens

**In adults (*B. longum* subsp. *longum*):**

1. **Mucin adhesion:** Sortase-dependent pili (SrtA-anchored) mediate binding to MUC2 and MUC3 glycoproteins in the colonic mucus layer; BopA surface lipoprotein provides secondary adhesion to fibronectin on epithelial surfaces
2. **Plant polysaccharide fermentation:** ABC transporters for xylan, arabinogalactan, and pectin oligosaccharides sustain colonisation on dietary fibre substrates
3. **EPS-mediated immune evasion:** Surface EPS suppresses complement-mediated opsonisation and reduces phagocytic clearance by intestinal macrophages [^fanning-2012-bifidobacterium-mucin]
4. **Cross-feeding ecology:** Acetate produced from *B. longum* fermentation is consumed by *Roseburia intestinalis* and *Faecalibacterium prausnitzii* as substrate for butyrate synthesis — establishing mutualistic metabolic cross-feeding

## Host Interactions

### Innate Immune Modulation

*B. longum* engages innate immune receptors through multiple cell wall and surface components:

| Pattern Recognition | Receptor | Signalling | Outcome |
|:---|:---|:---|:---|
| Peptidoglycan / LTA | TLR2/TLR6 heterodimer | MyD88 → NF-κB → IL-10 dominant | Anti-inflammatory; IL-12 ↓ |
| Muramyl dipeptide | NOD2 | RICK/RIP2 → NF-κB | Moderate; context-dependent |
| CpG DNA (unmethylated) | TLR9 | MyD88 → IRF7 → IFN-β ↑; IL-12 ↑ | Th1 skewing; allergen tolerance |
| Surface EPS | DC-SIGN (CD209) | ERK ↑; IL-10 ↑ | Tolerogenic DC conditioning |

The **net immune phenotype** induced by *B. longum* is predominantly **anti-inflammatory and tolerogenic**: IL-10 dominates over IL-12; Treg induction predominates over Th1/Th17 in homeostatic (non-inflammatory) conditions.

### Adaptive Immune Effects

- **Secretory IgA (sIgA) induction:** *B. longum* supplementation consistently increases faecal and breast-milk sIgA in both infants and adults; sIgA coats commensal bacteria to maintain immune exclusion and shapes microbiome composition through a process called "immune selection"
- **Treg expansion:** *B. longum*-conditioned DCs (IL-10+, IL-12low) drive FoxP3+ CD4+ Treg differentiation in Peyer's patches; these Tregs suppress inflammatory responses to both commensal antigens and dietary antigens (oral tolerance)
- **IgE suppression:** In infants colonised by *B. infantis*, allergen-specific IgE responses (skin prick test reactivity, serum IgE) are measurably reduced; proposed mechanism: IL-10-driven B cell class switching away from IgE, and IL-10/TGF-β suppression of IL-4/IL-13-dependent IgE class switch recombination
- **Th2 → Th1 rebalancing:** TLR9-mediated IFN-β and IL-12 production by *B. longum*-stimulated DCs shifts the Th2-biased neonatal immune phenotype toward Th1 — the proposed allergy-protective mechanism in epidemiological studies

### Metabolite Production

| Metabolite | Pathway | Downstream Effect |
|:---|:---|:---|
| **Acetate** | Bifidus shunt (phosphoketolase) | Cross-feeds butyrate producers; colonocyte fuel; GPR43 signalling; reduces NF-κB in colonocytes |
| **Lactate** | Lactate dehydrogenase (LDH) | Acidifies gut lumen; inhibits pathogens; cross-fed by *Veillonella* to propionate |
| **Folate (vitamin B9)** | De novo folate synthesis pathway | Cofactor for host one-carbon metabolism; particularly critical in pregnancy and infancy |
| **Riboflavin (B2)** | Riboflavin biosynthesis gene cluster | Colonocyte mitochondrial function; mucosal immune cell metabolism |

### Infant Colic Modulation

A clinically relevant interaction: *B. longum* supplementation (particularly *B. infantis*-enriched preparations) reduces **crying duration in colicky infants** by ~50 minutes/day in RCTs. The proposed mechanism involves acetate-mediated serotonin (5-HT) precursor modulation in enteroendocrine cells and reduction in *E. coli*-driven gas production through competitive exclusion.

## Connections

**Modulates** → [Digestive system](../../../01-human/07-system/digestive-system/README.md): *B. longum* subsp. *infantis* is the keystone HMO consumer in the breast-fed infant gut, creating a self-reinforcing low-pH ecosystem that excludes pathogens. Its acetate output cross-feeds butyrate producers that maintain colonocyte energy supply and barrier integrity throughout the large intestine.

**Modulates** → [Immune system](../../../01-human/07-system/immune-system/README.md): *B. longum* educates the mucosal immune system through TLR2-mediated IL-10/Treg induction, sIgA stimulation, and surface EPS-mediated DC tolerogenic conditioning. These interactions are most critical in early life, where *B. infantis* colonisation shapes the immune set-point that determines atopy and inflammatory disease risk.

**Modulates** → [Regulatory T cell](../../../01-human/04-cellular/regulatory-t-cell/README.md): *B. longum*-conditioned DCs drive FoxP3+ Treg differentiation in Peyer's patches and mesenteric lymph nodes via IL-10 and TGF-β. These Tregs suppress IgE class switching, Th2 effector responses, and inflammatory reactivity to commensal microbiota, functioning as the cellular intermediary for *B. longum*'s allergy-protective effects.

**Modulates** → [Large intestine](../../../01-human/06-organ/large-intestine/README.md): *B. longum* colonises the colonic mucus layer via sortase-dependent pili, produces acetate and lactate via the bifidus shunt, and cross-feeds *Faecalibacterium prausnitzii* and *Roseburia* for butyrate synthesis. Bacteriocin secretion competitively suppresses pathogen colonisation in the colonic niche.

## Pathology

### Depletion-Associated Conditions

Loss of *B. longum* and especially *B. infantis* from the gut microbiome is increasingly recognised as a contributing factor — and in some cases, a causal driver — of several common inflammatory and metabolic diseases:

| Condition | Nature of Association | Evidence |
|:---|:---|:---|
| **Infant atopic eczema / allergic disease** | *B. infantis* depletion in the first months of life → impaired Treg induction → Th2 skewing → IgE sensitisation; risk factor for asthma, food allergy | Moderate–high: prospective birth cohort studies; RCTs of *B. infantis* supplementation reducing eczema incidence |
| **Infant colic** | *B. infantis* depletion → *E. coli* overgrowth → excess gas production; reduced serotonin axis modulation | Moderate: RCTs showing 50 min/day reduction in crying with *B. longum*/*infantis* supplementation |
| **Neonatal necrotising enterocolitis (NEC)** | Preterm gut *B. infantis* deficiency → pathobiont overgrowth (*E. coli*, *Klebsiella*) → inflammatory cascade → intestinal necrosis; *B. infantis* enrichment reduces NEC risk | High: meta-analyses of Bifidobacterium-enriched probiotic mixtures; individual trial evidence strong |
| **Western microbiome depletion** | Decline of *B. infantis* from Western infant microbiomes (formula feeding, C-section, antibiotics) over past 50–100 years | Epidemiological: comparison of traditional-diet populations (high *B. infantis*) vs. Western (near-absent *B. infantis*); Sonnenburg lab data |
| **Inflammatory bowel disease (IBD)** | Reduced *B. longum* in active UC and CD patients | Moderate: case-control studies; not clearly causal |
| **Type 2 diabetes** | Lower *B. longum* levels in T2DM; acetate output reduction → impaired butyrate cross-feeding → reduced GLP-1 | Emerging: MetaHIT data; intervention studies ongoing |

### Commercial Probiotic Landscape

*B. longum* strains are among the most widely used in commercial probiotics:
- **Similac/Enfamil formulas with *B. infantis* EVC001:** Currently the most evidence-supported infant probiotic for *B. infantis* recolonisation in formula-fed infants; shown to restore HMO-consuming capacity and reduce pathogen load
- **Adult probiotic blends:** *B. longum* BB536 (Morinaga Milk Industry, Japan) — most studied adult *B. longum* strain; evidence for allergy, constipation, influenza prevention
- **Synbiotics:** *B. longum* + galacto-oligosaccharides (GOS)/fructo-oligosaccharides (FOS) — prebiotic combination enhances *B. longum* survival and colonisation; widely sold for IBS and general gut health

[^sela-2008-binfantis-hmo]: Sela DA, Chapman J, Adeuya A, et al. The genome sequence of *Bifidobacterium longum* subsp. *infantis* reveals adaptations for milk utilization within the infant microbiome. *Proc Natl Acad Sci USA.* 2008;105(48):18964-9. [doi:10.1073/pnas.0809584105](https://doi.org/10.1073/pnas.0809584105) · [PubMed 19033196](https://pubmed.ncbi.nlm.nih.gov/19033196/)
[^fanning-2012-bifidobacterium-mucin]: Fanning S, Hall LJ, Cronin M, et al. Bifidobacterial surface-exopolysaccharide facilitates commensal-host interaction through immune modulation and facilitates gut colonization. *Proc Natl Acad Sci USA.* 2012;109(6):2108-13. [doi:10.1073/pnas.1115621109](https://doi.org/10.1073/pnas.1115621109) · [PubMed 22308390](https://pubmed.ncbi.nlm.nih.gov/22308390/)

---
*This page is co-maintained with AI assistance. Content is reviewed for accuracy but may not reflect the latest clinical guidelines. See the [project disclaimer](../../../../README.md) for details.*

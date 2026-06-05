---
schema: pathogen-entry/v1
id: bacteroides-fragilis
name: Bacteroides fragilis
atlas: 02-pathogen
scale: 06-microbiome
status: draft
last_reviewed: 2026-06-05
summary: "Gram-negative anaerobe (Bacteroidota) in ~60% of healthy adults. Polysaccharide A (PSA) signals TLR2 on DCs → IL-10 → Treg induction. Pathogenic ETBF strain secretes Fragilysin metalloprotease promoting colorectal cancer via β-catenin signalling."
aliases: ["B. fragilis", "NTBF", "ETBF", "non-toxigenic B. fragilis", "enterotoxigenic B. fragilis", "BFT", "Fragilysin"]
sources:
  - id: mazmanian-2005-psa-germ-free
    type: peer-reviewed
    cite: "Mazmanian SK, Liu CH, Tzianabos AO, Kasper DL. An immunomodulatory molecule of symbiotic bacteria directs maturation of the host immune system. Cell. 2005;122(1):107-18."
    doi: "10.1016/j.cell.2005.05.007"
    pmid: "16009137"
    url: "https://doi.org/10.1016/j.cell.2005.05.007"
    accessed: "2026-06-05"
  - id: mazmanian-2008-psa-ibd
    type: peer-reviewed
    cite: "Mazmanian SK, Round JL, Kasper DL. A microbial symbiosis factor prevents intestinal inflammatory disease. Nature. 2008;453(7195):620-5."
    doi: "10.1038/nature07008"
    pmid: "18509436"
    url: "https://doi.org/10.1038/nature07008"
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
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "Commensal B. fragilis PSA is the founding example of a microbial molecule that directly matures the vertebrate immune system: PSA → TLR2 on DCs → IL-10 → Treg induction. Corrects Th1/Th2 imbalance in germ-free mice. OMV-delivered PSA signals without bacterial translocation across the epithelium."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: modulates
    note: "PSA-conditioned DCs drive FoxP3+ Treg differentiation in Peyer's patches and mesenteric lymph nodes via IL-10 and TGF-β. These Tregs suppress both Th1 and Th17 inflammatory responses. PSA-mediated Treg induction in germ-free mice (Kasper/Mazmanian 2005) was the first demonstration of a single microbial molecule directing systemic immune maturation."
  - target: 01-human/06-organ/large-intestine
    relation: modulates
    note: "B. fragilis colonises the colon lumen and inner mucus layer; ferments complex polysaccharides to SCFAs (propionate, acetate). ETBF subtype secretes Fragilysin (BFT) metalloprotease that cleaves E-cadherin → β-catenin nuclear translocation → colonocyte proliferation → colonic tumour promotion. OMVs mediate PSA immune signalling at the colonic epithelium."
  - target: 01-human/07-system/digestive-system
    relation: modulates
    note: "B. fragilis degrades host and dietary polysaccharides (heparan sulfate, chondroitin sulfate, pectin) via secreted polysaccharide lyases, contributing to SCFA production and microbiome cross-feeding. If the gut barrier is disrupted, B. fragilis translocation to the peritoneum or bloodstream causes abscess and bacteraemia — a dual commensal/opportunistic pathogen."
---

# Bacteroides fragilis

## Overview

*Bacteroides fragilis* is a **Gram-negative, non-spore-forming, strictly anaerobic rod** belonging to the phylum Bacteroidota (formerly Bacteroidetes) and the family Bacteroidaceae. It is found in approximately **60% of healthy adult humans** as part of the normal colonic microbiome and represents one of the most clinically fascinating organisms in microbiology: it simultaneously exemplifies **mutualistic immune education** (through its PSA capsule) and **conditional pathogenicity** (through the Fragilysin toxin produced by a distinct pathogenic subtype).

*B. fragilis* is divided into two epidemiologically and functionally distinct populations:

- **Non-toxigenic *B. fragilis* (NTBF):** The commensal majority (~60% of carriers); produces polysaccharide A (PSA) and does not secrete Fragilysin; promotes immune homeostasis
- **Enterotoxigenic *B. fragilis* (ETBF):** Minority subtype (~10–15% of healthy adults; 30–40% of individuals with colitis or CRC); carries the *bft* gene encoding **Fragilysin/BFT metalloprotease**; associated with inflammatory diarrhoea and colorectal cancer promotion

The landmark experiments of Sarkis Mazmanian and Dennis Kasper established NTBF as a **paradigm-shifting example of immune symbiosis**: germ-free mice colonised with *B. fragilis* — but not a *B. fragilis* PSA-deletion mutant — showed complete restoration of normal CD4+/CD8+ T cell ratios, spleen architecture, and Th1/Th2 balance [^mazmanian-2005-psa-germ-free]. This was the first demonstration that a single molecule from a single bacterium could direct vertebrate immune system maturation, founding the modern field of host-microbiome immune co-evolution.

## Structure

### Morphology

*B. fragilis* cells are **pleomorphic rods** (0.5–0.9 µm × 1–6 µm) — rod-shaped but exhibiting coccoid forms in old cultures or under nutritional stress. They are **non-motile** (no flagella in wild-type strains), **non-spore-forming**, and **obligate anaerobes** — though unusually among anaerobes, *B. fragilis* possesses modest aerotolerance via catalase and superoxide dismutase (SOD) production, allowing brief survival in oxygen-exposed environments (explaining its capacity for opportunistic infection during abdominal surgery or gut perforation).

### Cell Wall and Surface Structures

| Structure | Description | Functional Role |
|:---|:---|:---|
| **Outer membrane** | LPS-containing bilayer; *B. fragilis* LPS has an unusual lipid A that is hypostimulatory (weak TLR4 agonist) due to modified acylation pattern | Reduced endotoxin activity; colonisation without inflammatory LPS signalling |
| **Polysaccharide A (PSA)** | Zwitterionic capsular polysaccharide (~4 MDa); repeating motif alternates positive (+NH₃) and negative (-PO₄) charges; unique among microbial polysaccharides | TLR2 agonist on DCs and CD4+ T cells; induces IL-10 and IL-12 (balanced); drives Treg differentiation; corrects Th1/Th2 imbalance |
| **Additional capsular polysaccharides (PSB–PSH)** | *B. fragilis* encodes 8 distinct capsular polysaccharide loci (PSA–PSH); phase-variable expression | Antigenic variation; immune evasion; niche persistence |
| **Outer membrane vesicles (OMVs)** | 50–250 nm lipid bilayer vesicles shed from the outer membrane; enriched in PSA, LPS, and outer membrane proteins | Deliver PSA immune signals to subepithelial DCs without bacterial translocation; long-range immune modulation |
| **Fragilysin / BFT (ETBF only)** | 20 kDa zinc-dependent metalloprotease encoded by the *bft* gene; 3 isotypes (BFT-1, -2, -3); secreted via type V secretion | E-cadherin cleavage → E-cadherin ectodomain shedding → β-catenin nuclear translocation → c-Myc/cyclin D1 upregulation → colonocyte hyperproliferation → CRC promotion |
| **Polysaccharide lyases and glycosidases** | Numerous secreted/periplasmic enzymes (heparanase, chondroitin ABC lyase, hyaluronidase) | Complex polysaccharide degradation for energy; tissue invasion during opportunistic infection |

### Genome

- **Genome size:** ~5.2 Mb (ATCC 25285 type strain); GC content ~43%
- ~4,100 predicted coding sequences; among the most gene-rich anaerobes in the human gut
- **Phase variation loci:** 8 polysaccharide biosynthesis loci (PSA–PSH) each with invertible promoter elements — *B. fragilis* can express only one polysaccharide type at a time; stochastic switching allows antigenic diversity in clonal populations
- **Pathogenicity island (ETBF):** ~6 kb chromosomal pathogenicity island containing *bft* gene and flanking regulatory elements; absent from NTBF; horizontally transferred
- Rich complement of sigma factors (22+) enabling transcriptional adaptation to anaerobic microenvironments

## Infection Mechanism

### Colonisation Mechanism (Commensal NTBF)

*B. fragilis* establishes stable luminal colonisation through mechanisms that are immunologically distinctive — leveraging PSA to actively suppress immune clearance rather than passively evading it:

1. **Luminal adhesion:** *B. fragilis* adheres to mucin glycoproteins via outer membrane adhesins (OmpA family proteins, BF3059/BF3331 surface proteins); does not penetrate the inner mucus layer under homeostatic conditions — unlike *A. muciniphila*
2. **Polysaccharide capsule phase variation:** Expression of phase-variable PSA–PSH allows the population to escape B-cell-mediated humoral immunity; any antibody response to one capsular type fails to clear the 1-in-8 fraction expressing a different polysaccharide
3. **PSA-mediated active immune tolerance:** Rather than hiding from the immune system, *B. fragilis* PSA **actively induces the Treg and IL-10 responses** that prevent its own clearance — a remarkable case of a commensal bacteria deliberately programming host immune tolerance to permit its own long-term residence
4. **OMV-based immune signalling at a distance:** OMVs carrying PSA can traverse the mucus layer to reach subepithelial DCs without bacterial translocation, enabling PSA-TLR2 signalling to lamina propria immune cells without triggering barrier alarm responses
5. **Polysaccharide fermentation:** *B. fragilis* ferments host glycosaminoglycans (heparan sulfate, chondroitin sulfate) and dietary complex polysaccharides to propionate and acetate, contributing to the colonic SCFA pool

### Mechanism of ETBF-Mediated Tumour Promotion

The ETBF subtype causes disease through a distinct molecular mechanism:

1. **Fragilysin (BFT) secretion:** BFT is a 20 kDa zinc metalloprotease secreted via the type Vb (two-partner) secretion system into the gut lumen
2. **E-cadherin cleavage:** BFT's sole known substrate is the extracellular domain of E-cadherin (CDH1) — it cleaves E-cadherin between residues 409/410, releasing the 80 kDa ectodomain into the lumen
3. **β-catenin signalling activation:** Loss of E-cadherin disrupts the E-cadherin/β-catenin adhesion complex at colonocyte cell-cell junctions; β-catenin translocates to the nucleus where it activates Wnt target genes (c-Myc, cyclin D1, VEGF)
4. **NF-κB and STAT3 activation:** BFT-driven E-cadherin loss also activates NF-κB (IL-8, TNF-α production) and STAT3 (via JAK2); the resultant inflammatory microenvironment (IL-17, IL-23, Th17 cells) further promotes tumour progression
5. **CRC promotion in animal models:** ETBF-colonised mice develop significantly more colonic tumours than controls; in *Min/+* mice (APC truncation model), ETBF dramatically accelerates polyp-to-adenoma progression

## Host Interactions

### PSA-Mediated Immune Education (NTBF)

The PSA–TLR2 signalling axis is the best-characterised host-microbiome immune interface defined at molecular resolution:

| Cell Type | Receptor | Signal | Outcome |
|:---|:---|:---|:---|
| **Plasmacytoid DCs** | TLR2 (direct PSA contact) | MyD88 → IRF7 → IFN-β; NF-κB → IL-10, IL-12 | Balanced Th1/Th17 promotion with IL-10 counter-regulation |
| **Conventional DCs** | TLR2 + co-receptors (PSA) | NF-κB → IL-10 dominant | Tolerogenic DC conditioning → Treg induction |
| **CD4+ T cells** | Direct TLR2 expression (PSA) | TLR2 → IL-10 → Foxp3 upregulation | Direct Treg conversion without DC intermediary [^mazmanian-2008-psa-ibd] |
| **B cells** | Unknown | PSA → IgM → IgA class switching | Mucosal IgA production; immune exclusion |
| **Epithelial cells** | TLR2/PSA (OMV-delivered) | NF-κB ↓; tight junction maintenance | Barrier preservation; reduced paracellular permeability |

### Th1/Th2 Balance Restoration

The Kasper/Mazmanian germ-free mouse experiment (2005) demonstrated that:
- Germ-free mice have **aberrant Th2 predominance** (excess IL-4, IL-5, IL-13; reduced IFN-γ; reduced CD4+ cells) — recapitulating aspects of allergic disease
- **Colonisation with NTBF wild-type** (PSA-expressing) fully restores normal Th1/Th2 ratios and splenic CD4+/CD8+ ratios within 3 weeks
- **Colonisation with PSA-deletion mutant** *B. fragilis* fails to restore immune balance — proving PSA is the singular required molecule
- **Treatment with purified PSA alone** (without the bacterium) partially recapitulates immune restoration [^mazmanian-2005-psa-germ-free]

### SCFA Production and Metabolic Cross-Feeding

*B. fragilis* is a major colonic polysaccharide degrader:
- Secretes **chondroitin ABC lyase** (degrades chondroitin sulfate, dermatan sulfate, hyaluronan — host extracellular matrix glycosaminoglycans)
- Secretes **heparanase** — unusual; very few gut bacteria possess this activity; provides access to heparan sulfate as carbon source
- Fermentation end-products: **propionate** (primary), **acetate**, trace butyrate; propionate enters portal circulation → hepatic gluconeogenesis suppression; GPR41 signalling on enteroendocrine cells → GLP-1/PYY

## Connections

**Modulates** → [Immune system](../../../01-human/07-system/immune-system/README.md): NTBF PSA is the founding experimental evidence that a single microbial molecule directs vertebrate immune system maturation. PSA-TLR2 signalling on DCs and CD4+ T cells drives Treg induction, corrects Th1/Th2 imbalance, and produces a systemic anti-inflammatory phenotype that underlies the "hygiene hypothesis" molecular mechanism.

**Modulates** → [Regulatory T cell](../../../01-human/04-cellular/regulatory-t-cell/README.md): PSA-conditioned DCs and PSA direct TLR2 signalling on CD4+ T cells converge on FoxP3+ Treg differentiation in Peyer's patches and mesenteric lymph nodes. These Tregs suppress both Th1-mediated intestinal inflammation and Th2-mediated allergic disease, representing the cellular mechanism by which NTBF colonisation prevents IBD in animal models.

**Modulates** → [Large intestine](../../../01-human/06-organ/large-intestine/README.md): NTBF ferments glycosaminoglycans and dietary polysaccharides in the colonic lumen, contributing propionate and acetate to the microbiome metabolic network. ETBF's BFT metalloprotease disrupts colonic epithelial E-cadherin, activating β-catenin/Wnt tumour-promoting signalling in colonocytes, making ETBF a recognised risk factor for colorectal cancer.

**Modulates** → [Digestive system](../../../01-human/07-system/digestive-system/README.md): *B. fragilis* contributes to luminal polysaccharide digestion and SCFA production. Its opportunistic pathogenic capacity manifests when gut barrier integrity is disrupted: translocation to the peritoneum causes abscess and bacteraemia, making it the most common anaerobe recovered from intra-abdominal infections and post-surgical complications.

## Pathology

### Disease Associations: A Dual-Role Organism

*B. fragilis* is unique among gut commensals in having clearly defined **beneficial (NTBF) and harmful (ETBF) disease associations**, with the harmful outcomes concentrated in the ETBF subtype and in barrier-disruption contexts:

#### Commensal NTBF: Loss-of-Function (Depletion) Disease Associations

| Condition | Nature of Association | Evidence Level |
|:---|:---|:---|
| **Inflammatory bowel disease (IBD)** | Depletion of NTBF / PSA-producing strains; loss of IL-10/Treg tone → unrestrained Th1/Th17 intestinal inflammation | Moderate: NTBF depletion in IBD patients; PSA protects against experimental colitis in animal models [^mazmanian-2008-psa-ibd] |
| **Th2-mediated allergic disease** | Loss of PSA-mediated Th1/Th2 rebalancing → Th2 skewing → IgE sensitisation, asthma, eczema | Emerging: germ-free mouse data strong; human epidemiology consistent with hygiene hypothesis |
| **Multiple sclerosis (EAE model)** | NTBF/PSA depletion → reduced Treg tone → CNS autoimmunity; PSA treatment prevents EAE in mice | Emerging animal data; human association studies ongoing |

#### Pathogenic ETBF: Gain-of-Function Disease Associations

| Condition | Mechanism | Evidence Level |
|:---|:---|:---|
| **ETBF diarrhoea** | BFT → E-cadherin cleavage → intestinal epithelial permeability → secretory diarrhoea; NF-κB-driven IL-8/IL-17 recruitment | High: challenge studies, outbreak investigations (ETBF in paediatric traveller's diarrhoea) |
| **Colorectal cancer (CRC) promotion** | BFT → β-catenin nuclear signalling → c-Myc/cyclin D1 → colonocyte hyperproliferation; Th17 inflammatory microenvironment → tumour immune evasion | High: ETBF enriched in CRC tumour-adjacent mucosa vs. healthy controls; mechanistically established in Min mouse model |
| **Bacteraemia / intra-abdominal abscess** | Gut barrier disruption (surgery, diverticulitis, appendicitis, IBD flare) → *B. fragilis* translocation → portal bacteraemia → liver abscess or peritonitis | High: *B. fragilis* is the most commonly isolated anaerobe in clinical blood cultures and abdominal wound infections |
| **Pelvic inflammatory disease (PID)** | *B. fragilis* ascending infection from gut/perineum to pelvic organs; polymicrobial abscess formation | High: clinical bacteriology data |

### Antibiotic Resistance Note

*B. fragilis* is **intrinsically resistant** to many β-lactam antibiotics through chromosomal β-lactamase (*cfiA*) expression. Treatment of *B. fragilis* bacteraemia requires **metronidazole** (drug of choice), **carbapenems**, or **β-lactam/β-lactamase inhibitor combinations** (piperacillin-tazobactam). Resistance to metronidazole is emerging (~5–10% clinical isolates in some regions).

### PSA as a Therapeutic Target

The PSA story has inspired attempts to use purified PSA as a therapeutic immunomodulator:
- Intranasal PSA protects against EAE (MS model) in mice via IL-10/Treg induction
- PSA-loaded nanoparticles are in preclinical development for IBD and MS therapy
- The TLR2-agonist property of PSA is being explored for vaccine adjuvant applications (mucosal delivery)

[^mazmanian-2005-psa-germ-free]: Mazmanian SK, Liu CH, Tzianabos AO, Kasper DL. An immunomodulatory molecule of symbiotic bacteria directs maturation of the host immune system. *Cell.* 2005;122(1):107-18. [doi:10.1016/j.cell.2005.05.007](https://doi.org/10.1016/j.cell.2005.05.007) · [PubMed 16009137](https://pubmed.ncbi.nlm.nih.gov/16009137/)
[^mazmanian-2008-psa-ibd]: Mazmanian SK, Round JL, Kasper DL. A microbial symbiosis factor prevents intestinal inflammatory disease. *Nature.* 2008;453(7195):620-5. [doi:10.1038/nature07008](https://doi.org/10.1038/nature07008) · [PubMed 18509436](https://pubmed.ncbi.nlm.nih.gov/18509436/)

---
*This page is co-maintained with AI assistance. Content is reviewed for accuracy but may not reflect the latest clinical guidelines. See the [project disclaimer](../../../../README.md) for details.*

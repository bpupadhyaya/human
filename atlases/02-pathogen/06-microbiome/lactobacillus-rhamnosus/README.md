---
schema: pathogen-entry/v1
id: lactobacillus-rhamnosus
name: Lactobacillus rhamnosus
atlas: 02-pathogen
scale: 06-microbiome
status: draft
last_reviewed: 2026-06-05
summary: "Gram-positive lactic acid bacterium; GG strain most-studied probiotic. Colonises GI mucosa; reduces antibiotic-associated diarrhoea (NNT ~7), prevents recurrent UTI, and attenuates infantile eczema. Produces lactic acid, SCFA; modulates mucosal IgA and Treg responses."
aliases: ["L. rhamnosus", "LGG", "Lactobacillus GG", "L. rhamnosus GG", "ATCC 53103"]
sources:
  - id: szajewska-2015-lgg-diarrhea
    type: peer-reviewed
    cite: "Szajewska H, Kolodziej M. Systematic review with meta-analysis: Lactobacillus rhamnosus GG in the prevention of antibiotic-associated diarrhoea in children and adults. Aliment Pharmacol Ther. 2015;42(10):1149-57."
    doi: "10.1111/apt.13404"
    pmid: "26365389"
    url: "https://doi.org/10.1111/apt.13404"
  - id: salminen-2021-postbiotics-isapp
    type: peer-reviewed
    cite: "Salminen S, Collado MC, Endo A, et al. The International Scientific Association of Probiotics and Prebiotics (ISAPP) consensus statement on the definition and scope of postbiotics. Nat Rev Gastroenterol Hepatol. 2021;18(9):649-67."
    doi: "10.1038/s41575-021-00440-6"
    pmid: "33948935"
    url: "https://doi.org/10.1038/s41575-021-00440-6"
  - id: rautava-2012-lgg-eczema
    type: peer-reviewed
    cite: "Rautava S, Kainonen E, Salminen S, et al. Maternal probiotic supplementation during pregnancy and breast-feeding reduces the risk of eczema in the infant. J Allergy Clin Immunol. 2012;130(6):1355-60."
    doi: "10.1016/j.jaci.2012.09.003"
    pmid: "23083673"
    url: "https://doi.org/10.1016/j.jaci.2012.09.003"
cross_links:
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "L. rhamnosus GG activates Toll-like receptor 2 (TLR2) and TLR9 on intestinal immune cells, promotes regulatory T-cell (Treg) expansion via IL-10 and TGF-β, suppresses pro-inflammatory NF-κB signalling in intestinal epithelium, and reduces IgE-mediated allergic responses. Its s-layer protein and lipoteichoic acid are key immunomodulatory PAMPs."
  - target: 01-human/07-system/digestive-system
    relation: modulates
    note: "L. rhamnosus GG colonises the intestinal mucosa (transiently in adults, more persistently in infants); produces lactic acid and bacteriocins (including rhamnosin A) that competitively exclude pathogenic bacteria; strengthens intestinal tight junctions (ZO-1, occludin upregulation); and stimulates mucin production from goblet cells."
---

# Lactobacillus rhamnosus

## Overview

*Lactobacillus rhamnosus* is a **Gram-positive, non-spore-forming, homofermentative lactic acid bacterium** belonging to the family Lactobacillaceae. It is found naturally in the human GI tract, oral cavity, urogenital tract, and in fermented dairy products. Its most studied strain — **LGG (*L. rhamnosus* GG; ATCC 53103)** — was isolated in 1983 from the faecal flora of a healthy human by Sherwood Gorbach and Barry Goldin (the "GG" in the name) at Tufts University, and is now the world's **most extensively researched probiotic microorganism**, with >1,000 clinical trials and thousands of in vitro and animal studies documenting its health-promoting properties [^szajewska-2015-lgg-diarrhea].

Unlike the pathogenic members of the Pathogen Atlas, *L. rhamnosus* is included here as a representative **beneficial microbiome member** — a commensal and therapeutic organism whose interactions with the human immune and digestive systems exemplify the positive end of the host-microbiome spectrum. Its classification at the "06-microbiome" scale reflects its role as a defined component of the healthy human microbiota and a widely administered exogenous probiotic agent.

Clinically validated applications of *L. rhamnosus* GG include:
- **Antibiotic-associated diarrhoea (AAD) prevention:** NNT ~7–10 in systematic meta-analyses [^szajewska-2015-lgg-diarrhea]
- **Acute infectious gastroenteritis:** Reduces diarrhoea duration by ~1 day in children (rotavirus most studied)
- **Prevention of infantile eczema:** Maternal supplementation during pregnancy and breastfeeding reduces eczema risk in infants [^rautava-2012-lgg-eczema]
- **Recurrent urinary tract infection prevention** (vaginal *L. rhamnosus* strains)
- **Necrotising enterocolitis prevention** in preterm infants (evidence accumulating; not yet all-cause standard of care)

The ISAPP consensus framework distinguishes *L. rhamnosus* GG (a probiotic — live organism) from **postbiotics** (inanimate products of *L. rhamnosus* metabolism with health benefit) and **prebiotics** (substrates that selectively feed *L. rhamnosus* and other beneficial commensals) [^salminen-2021-postbiotics-isapp].

## Structure

### Morphology

*L. rhamnosus* cells are **non-motile, non-spore-forming rods** (0.8–1.0 µm × 2–4 µm) occurring singly, in pairs, or in short chains. They are **Gram-positive** (thick peptidoglycan wall) and **facultative anaerobes** — tolerant of oxygen but preferring anaerobic or microaerophilic conditions. *L. rhamnosus* is **acid-tolerant** (survives gastric pH 2.0 for several hours; unlike many Lactobacillus species) and **bile-tolerant** (survives 0.3% oxgall — essential for intestinal colonisation after oral ingestion). These properties made it the first *Lactobacillus* strain to survive transit through the human GI tract when administered orally and to stably colonise the intestinal mucosa [^szajewska-2015-lgg-diarrhea].

### Cell Wall and Surface Structures

The *L. rhamnosus* cell wall has several layers critical to its functional properties:

| Structure | Description | Immune / Colonisation Role |
|:---|:---|:---|
| **Peptidoglycan** | Cross-linked N-acetylmuramic acid / N-acetylglucosamine; thick Gram-positive wall (~20–80 nm) | Ligand for TLR2/NOD2; structural rigidity |
| **Teichoic acids (TA)** | Wall TA (WTA) and lipoteichoic acid (LTA); polyol-phosphate chains | LTA engages TLR2; modulates innate signalling |
| **S-layer (surface layer)** | Paracrystalline protein array of SpaA (not all strains) | Mucosal adhesion; immune modulation |
| **Pili (SpaCBA pili)** | Long, non-flagellar fimbriae encoded by *spaCBA* operon | Mucus adhesion (SpaC tip adhesin binds mucin and collagen); essential for gut colonisation |
| **Exopolysaccharides (EPS)** | Strain-specific polysaccharide capsule | Immunomodulation; biofilm formation; bacteriophage resistance |

The **SpaCBA pilus system** is of particular significance: the SpaC tip subunit binds mucin-2 (MUC2) glycoproteins in the intestinal mucus layer and type I collagen, anchoring LGG to the intestinal epithelium. Pilus-deficient mutants of LGG show markedly reduced mucosal persistence and immunomodulatory capacity in vivo.

### Genome

- **Genome size:** ~3.0 Mb; GC content ~46.7% (LGG reference: ATCC 53103)
- ~2,900–3,100 coding sequences
- Notable gene clusters: *spa* (pilus operon), multiple carbohydrate utilisation (PTS systems for sugars), lactic acid fermentation pathway (*ldh*, *pfl*), bile salt hydrolase (*bsh*)
- Contains two plasmids in the original LGG strain (pLGG1, pLGG2); extensive carbohydrate metabolism genes reflect adaptation to gut glycan landscape
- *L. rhamnosus* GG-specific: bacteriocin-like inhibitory substance gene cluster (rhamnosin A precursor)

## Infection Mechanism

### Note on Pathogenic Potential

*L. rhamnosus* is generally considered non-pathogenic and is classified as a **GRAS** (Generally Recognised as Safe) organism by the US FDA. However, in severely immunocompromised patients (particularly those with short bowel syndrome or central venous catheters), rare cases of **LGG bacteraemia** have been reported following probiotic administration — most commonly as a translocation event from the gut rather than classical infection. This underscores the need for caution when using live probiotic organisms in high-risk populations.

### Colonisation and Persistence

*L. rhamnosus* GG colonises the intestinal mucosa through the following sequence:

1. **Gastric survival:** Acid-tolerant proton-pump-mediated cytoplasmic pH homeostasis and cell wall buffering allow survival at gastric pH 2.0–3.0 for up to 2–3 hours
2. **Bile tolerance:** Bile salt hydrolase (BSH) deconjugates bile salts (reducing their detergent activity); ABC transporter efflux pumps remove bile from cytoplasm; adaptation of membrane fatty acid composition (increased cyclopropane fatty acids) under bile stress
3. **Mucus colonisation:** SpaCBA pili (SpaC tip adhesin) bind MUC2 and MUC3 glycoproteins in the mucus layer; collagen-binding S-layer protein (SLP) provides additional adhesion in pilus-independent manner
4. **Epithelial interaction:** LGG interacts directly with intestinal epithelial cell surface proteins; activates anti-apoptotic PI3K/Akt and EGFR signalling pathways in enterocytes — promoting epithelial barrier survival under injury
5. **Colonisation persistence:** Transient in adults (detectable up to 7 days post-supplementation); more prolonged in infants (weeks to months), particularly after neonatal colonisation

### Competitive Exclusion of Pathogens

*L. rhamnosus* competes with and inhibits enteropathogens through multiple mechanisms:
- **Lactic acid production:** Lowers local intestinal pH; bacteriostatic/bactericidal against pH-sensitive pathogens (*Salmonella*, *E. coli*, *C. difficile*)
- **Bacteriocin/rhamnosin A:** Narrow-spectrum antibacterial peptide targeting closely related Gram-positive organisms
- **Steric exclusion:** LGG occupies mucus attachment sites, blocking adhesion of *E. coli*, *Salmonella*, *H. pylori*, and *C. difficile* toxins
- **Biofilm formation:** LGG forms protective mucus-associated biofilm communities, excluding planktonic pathogens

## Host Interactions

### Innate Immune Modulation

*L. rhamnosus* GG exerts pleiotropic effects on intestinal innate immunity:

| Target | Receptor/Pathway | Effect |
|:---|:---|:---|
| **Intestinal epithelial cells** | TLR2 (LTA) → PI3K/Akt; NF-κB | Anti-apoptotic; tight junction (ZO-1, claudin-3) upregulation; mucin synthesis (MUC2, MUC3) stimulation |
| **Macrophages/monocytes** | TLR2 (peptidoglycan, LTA), TLR9 (unmethylated CpG DNA) | Balanced activation: IL-10 up, IL-12 moderated; trained immunity phenotype |
| **Dendritic cells** | CLRs, TLR2, NOD2 | Tolerogenic DC phenotype; IL-10 and TGF-β production → Treg differentiation; reduced IL-12/IL-23 (Th1/Th17 polarisation) in homeostatic context |
| **NK cells** | Indirect (IL-10/IL-12 milieu) | Moderate NK activation; surveillance maintained |
| **Mast cells** | TLR2; indirect | Reduced histamine and IgE-mediated degranulation in ABPA and food allergy models |

### Adaptive Immune Modulation

The most clinically significant adaptive immune effects of *L. rhamnosus* GG are in **mucosal IgA production** and **Treg-mediated immune regulation**:

- **Secretory IgA (sIgA):** LGG stimulates intestinal plasma cell differentiation and polymeric IgA production; sIgA coats bacteria in the gut lumen (immune exclusion) and shapes luminal microbiota composition; increased sIgA after LGG supplementation correlates with protection against gastroenteritis
- **Regulatory T cells (Tregs):** LGG-conditioned DCs (producing IL-10, TGF-β) induce FoxP3⁺ Tregs in mesenteric lymph nodes and Peyer's patches; Tregs suppress excessive inflammatory responses to both commensals and food antigens
- **Th1/Th2 balance in allergy:** In atopic disease models, LGG shifts the Th2-dominant neonatal immune response toward Th1 (IFN-γ), reducing IgE class switching and mast cell sensitisation — the proposed mechanism for eczema prevention [^rautava-2012-lgg-eczema]
- **Th17 modulation:** Context-dependent; LGG can modestly promote or suppress Th17 responses; generally, LGG's anti-inflammatory NF-κB suppression reduces IL-17-driven intestinal inflammation in colitis models

### Short-Chain Fatty Acid and Metabolite Production

*L. rhamnosus* contributes to the gut metabolome through:
- **L-lactic acid** (primary fermentation product): Acidifies colon, inhibits pathogens, signals via GPR81 on colonocytes
- **Short-chain fatty acids (SCFA)** — primarily through cross-feeding: Acetate from LGG fermentation feeds butyrate-producing bacteria (*Faecalibacterium prausnitzii*); butyrate is the primary colonocyte energy source and histone deacetylase inhibitor with broad anti-inflammatory effects
- **D-phenyl lactic acid:** Antimicrobial metabolite inhibiting *C. albicans* and several bacterial pathogens
- **Hydrogen peroxide (H₂O₂):** Produced in trace amounts; contributes to vaginal lactobacillus pathogen exclusion

### Cytokine Profile Elicited

| Context | Dominant cytokine profile |
|:---|:---|
| **Healthy gut homeostasis** | IL-10 ↑, TGF-β ↑ (Treg); sIgA ↑; NF-κB ↓ |
| **AAD prevention** | IL-10 ↑; pro-inflammatory TNF-α and IL-6 ↓ vs. antibiotic-only |
| **Neonatal immune programming** | IFN-γ ↑ (Th1); IL-4, IL-13 ↓ (Th2); IgE ↓ |
| **Colitis/IBD models** | TNF-α ↓; IL-12 ↓; IL-10 ↑; mucosal barrier integrity ↑ |

## Connections

**Modulates** → [Immune system](../../../01-human/07-system/immune-system/README.md): *L. rhamnosus* GG is a model organism for understanding how commensal bacteria educate and balance the mucosal immune system. Its TLR2-mediated NF-κB suppression, Treg-inducing DC conditioning, and sIgA stimulation collectively maintain immune homeostasis — preventing both under-response to pathogens and over-response to commensals and food antigens.

**Modulates** → [Digestive system](../../../01-human/07-system/digestive-system/README.md): *L. rhamnosus* GG colonises the intestinal mucosa, acidifies the gut lumen through lactic acid production, strengthens epithelial tight junctions, stimulates mucin secretion, and competitively excludes enteropathogens. These actions collectively protect intestinal barrier integrity and reduce the incidence and duration of GI infections and antibiotic-associated dysbiosis.

## Pathology

### Beneficial Clinical Applications

| Indication | Evidence Level | Key Findings | NNT / Effect Size |
|:---|:---|:---|:---|
| **Antibiotic-associated diarrhoea (AAD) prevention** | High (multiple RCTs, meta-analyses) | RR reduction ~50% in both adults and children; effective regardless of antibiotic class | NNT ~7 |
| **Acute infectious diarrhoea (children)** | Moderate (Cochrane review) | Reduces diarrhoea duration by ~1 day; reduces stool frequency; most evidence for rotavirus | Moderate effect |
| **Infantile eczema prevention** | Moderate (several RCTs) | Maternal supplementation during late pregnancy + breastfeeding → 50% relative risk reduction in atopic eczema in infants to age 2 | ARR ~10%; NNT ~10 |
| **Recurrent UTI prevention** | Moderate (vaginal/oral LGG strains) | *L. rhamnosus* GR-1 + *L. reuteri* RC-14 combination reduces UTI recurrence; restores Lactobacillus-dominant vaginal flora | NNT ~6 (combination) |
| **Necrotising enterocolitis (NEC) prevention** | Emerging (systematic reviews) | LGG among probiotics associated with NEC risk reduction in preterm infants <1500g; not all trials consistent | ARR ~2–3% |
| **Helicobacter pylori eradication adjunct** | Low-moderate | LGG co-administration may reduce GI side effects of triple therapy; modest improvement in eradication rates | Inconsistent |
| **Paediatric Crohn's disease remission maintenance** | Low | Small RCT evidence only; not currently recommended as standard therapy | Insufficient |

### Safety Considerations

*L. rhamnosus* GG is one of the **safest studied microorganisms** in clinical use:
- **Healthy individuals:** Absolute safety; no serious adverse events in any large RCT
- **Immunocompromised patients:** Caution warranted; ~30 cases of LGG bacteraemia reported in the literature (PubMed), predominantly in patients with central venous catheters, short bowel syndrome, or haematological malignancy; most responded to ampicillin
- **ICU patients:** WHO advisory recommends caution in critically ill ICU patients based on one Scandinavian RCT (PROPATRIA) showing increased mortality in severe acute pancreatitis patients given *Lactobacillus* — causal relationship debated; thought to be related to intestinal ischaemia and translocation in this specific setting

Probiotics containing *L. rhamnosus* are widely available as over-the-counter dietary supplements (e.g., Culturelle) and as pharmaceutical-grade preparations. Dose typically 10⁹–10¹⁰ CFU/day orally [^szajewska-2015-lgg-diarrhea].

[^szajewska-2015-lgg-diarrhea]: Szajewska H, Kolodziej M. Systematic review with meta-analysis: *Lactobacillus rhamnosus* GG in the prevention of antibiotic-associated diarrhoea in children and adults. *Aliment Pharmacol Ther.* 2015;42(10):1149-57. [doi:10.1111/apt.13404](https://doi.org/10.1111/apt.13404) · [PubMed 26365389](https://pubmed.ncbi.nlm.nih.gov/26365389/)
[^salminen-2021-postbiotics-isapp]: Salminen S, Collado MC, Endo A, et al. The ISAPP consensus statement on the definition and scope of postbiotics. *Nat Rev Gastroenterol Hepatol.* 2021;18(9):649-67. [doi:10.1038/s41575-021-00440-6](https://doi.org/10.1038/s41575-021-00440-6) · [PubMed 33948935](https://pubmed.ncbi.nlm.nih.gov/33948935/)
[^rautava-2012-lgg-eczema]: Rautava S, Kainonen E, Salminen S, et al. Maternal probiotic supplementation during pregnancy and breast-feeding reduces the risk of eczema in the infant. *J Allergy Clin Immunol.* 2012;130(6):1355-60. [doi:10.1016/j.jaci.2012.09.003](https://doi.org/10.1016/j.jaci.2012.09.003) · [PubMed 23083673](https://pubmed.ncbi.nlm.nih.gov/23083673/)

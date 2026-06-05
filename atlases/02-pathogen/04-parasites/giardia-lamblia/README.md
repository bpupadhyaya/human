---
schema: pathogen-entry/v1
id: giardia-lamblia
name: Giardia lamblia (G. intestinalis / G. duodenalis)
atlas: 02-pathogen
scale: 04-parasites
status: draft
last_reviewed: 2026-06-05
summary: "Diplomonad protozoan; pear-shaped trophozoite + oval cysts; ventral adhesive disc attaches to duodenal/jejunal epithelium; disrupts tight junctions → secretory diarrhea; no mitochondria; fecal-oral/waterborne. Most common intestinal protozoan worldwide."
aliases: ["Giardia intestinalis", "Giardia duodenalis", "G. lamblia", "giardiasis", "traveler's diarrhea (Giardia)", "beaver fever"]
sources:
  - id: mandell-principles
    type: textbook
    cite: "Bennett JE, Dolin R, Blaser MJ. Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases. 9th ed. Elsevier; 2020."
    url: "https://www.elsevier.com/books/mandell-douglas-and-bennetts-principles-and-practice-of-infectious-diseases/bennett/978-0-323-48255-4"
    accessed: "2026-06-05"
  - id: murray-microbiology
    type: textbook
    cite: "Murray PR, Rosenthal KS, Pfaller MA. Medical Microbiology. 9th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/medical-microbiology/murray/978-0-323-67378-4"
    accessed: "2026-06-05"
  - id: buret-2008-giardia
    type: peer-reviewed
    cite: "Buret AG. Pathophysiology of enteric infections with Giardia duodenalis. Parasite. 2008;15(3):261-5."
    doi: "10.1051/parasite/2008153261"
    pmid: "18814694"
    url: "https://doi.org/10.1051/parasite/2008153261"
  - id: ankarklev-2010-giardia
    type: peer-reviewed
    cite: "Ankarklev J, Jerlström-Hultqvist J, Ringqvist E, Troell K, Svärd SG. Behind the smile: cell biology and disease mechanisms of Giardia species. Nat Rev Microbiol. 2010;8(6):413-22."
    doi: "10.1038/nrmicro2317"
    pmid: "20400969"
    url: "https://doi.org/10.1038/nrmicro2317"
cross_links:
  - target: 01-human/06-organ/small-intestine
    relation: infects
    note: "Trophozoites attach to duodenal and jejunal brush border via ventral disc; VSP antigenic variation evades mucosal IgA; disruption of tight junctions (ZO-1 redistribution) causes villous blunting and malabsorption."
  - target: 01-human/07-system/digestive-system
    relation: damages
    note: "Disruption of duodenal and jejunal epithelium reduces digestive enzyme activity; villous blunting causes fat malabsorption (steatorrhoea); lactase deficiency often persists after clearance."
  - target: 01-human/07-system/immune-system
    relation: damages
    note: "Secretory IgA production against VSPs drives antigenic switching; CD4+ T cell-mediated immunity required for clearance; hypogammaglobulinaemia (e.g. common variable immunodeficiency) leads to chronic giardiasis."
  - target: 01-human/04-cellular/dendritic-cell
    relation: damages
    note: "Giardia-derived proteases activate dendritic cells via TLR4; paradoxical suppression of DC maturation and IL-12 production reduces Th1 responses, facilitating persistent infection."
---

# Giardia lamblia (G. intestinalis / G. duodenalis)

## Overview

***Giardia lamblia*** (also called *G. intestinalis* or *G. duodenalis*) is a binucleate flagellated protozoan and the **most commonly identified intestinal parasitic infection worldwide**, with an estimated 280–300 million clinical cases per year. It is a major cause of waterborne diarrhea outbreaks in developed countries and of chronic childhood malnutrition in low-income settings [^ankarklev-2010-giardia].

*Giardia* occupies a fascinating position in eukaryotic evolution: it is a **diplomonad**, placed in the supergroup Metamonada, and is one of the earliest-diverging eukaryotic lineages. It lacks conventional mitochondria — possessing instead rudimentary **mitosomes** (mitochondria-derived organelles that retain only the iron-sulfur cluster assembly pathway, not ATP generation), peroxisomes, or a conventional Golgi. This anaerobic core metabolism, combined with an extreme conservation of cell biology, makes *Giardia* a model organism for studying early eukaryotic evolution alongside its medical significance [^ankarklev-2010-giardia].

Infection is typically self-limited (2–6 weeks) in immunocompetent individuals but causes significant morbidity: **chronic malabsorption, growth stunting in children, lactase deficiency**, and post-infectious irritable bowel syndrome. Immunocompromised individuals (agammaglobulinaemia, common variable immunodeficiency) develop severe, refractory, sometimes fatal chronic giardiasis. Treatment with **metronidazole or tinidazole** is highly effective; resistance is rare but emerging.

## Structure

**Life cycle stages and morphology:**

| Stage | Location | Size | Features |
|:---|:---|:---|:---|
| **Trophozoite** | Small intestine (duodenum/jejunum) | 9–21 µm × 5–15 µm, pear/tear-drop shaped | 2 nuclei (paired, symmetrical), 4 pairs of flagella (anterior, posterior, caudal, ventral), 1 ventral adhesive disc, 2 axonemes, 2 median bodies |
| **Cyst** | Colon (formed before excretion); feces; water | 8–12 µm × 7–10 µm, oval | 4 nuclei (2-cyst has 2), intracytoplasmic axonemes visible, refractile cyst wall (β-1,3-linked GalNAc polymer) |

**Key structural features:**

- **Ventral adhesive disc:** The defining structure of *Giardia* and its principal virulence factor — a rigid, concave cytoskeletal organelle composed of α/β/γ tubulin microtubules arranged in a spiral coil with **contractile microribbons** (composed of giardins: α, β, δ, ε, ζ-giardin proteins, unique to *Giardia*); the disc functions as a suction cup via a hydrodynamic mechanism (flagellar current creates low-pressure zone beneath the disc), not purely mechanical adhesion
- **Flagella:** 8 flagella in 4 pairs — anterior, posterior-lateral, caudal, and ventral; caudal flagella also contribute to adhesion disc stabilisation; flagellar motility is required for disc repositioning during mitosis
- **Median bodies:** L-shaped or claw hammer-shaped structures of uncertain function; composed of tubulin; possibly precursors to axonemes in daughter cells or structural support
- **VSP (Variant Surface Proteins):** ~190 VSP genes (assemblages A/B); only one VSP expressed at a time on trophozoite surface; highly cysteine-rich, with a conserved C-terminal CRGKA transmembrane anchor; form a dense protease-resistant coat
- **No mitochondria, no peroxisomes, no conventional Golgi:** Fermentation-based energy metabolism (ethanol and acetate as end-products); relies on host for lipid acquisition (Giardia cannot synthesise long-chain fatty acids de novo)

## Infection Mechanism

**Step-by-step molecular pathogenesis:**

**1. Transmission (fecal-oral, waterborne):**
- Infectious dose: remarkably low — as few as **10 cysts** can establish infection
- Sources: contaminated water (chlorine-resistant cysts; filtration required), raw produce, person-to-person (daycare centres, institutions), animal reservoirs (beavers, dogs — zoonotic transmission for assemblage A)
- Cysts remain viable in cold water for months; chlorination at standard doses does not kill cysts (UV and filtration are effective)

**2. Excystation (cyst → trophozoite):**
- Cysts ingested and transit to stomach: gastric acid (pH 2) triggers excystation signal
- Cysts move to duodenum: pancreatic proteases (trypsin) complete excystation → two trophozoites emerge per cyst within minutes of duodenal entry
- Trophozoites express VSPs immediately upon excystation

**3. Attachment to small intestinal epithelium:**
- Trophozoites colonise duodenum and proximal jejunum (location of highest pancreatic enzyme activity and bile, which paradoxically *stimulates* Giardia growth)
- **Ventral disc attachment mechanism:** Flagellar beating creates hydrodynamic suction beneath the disc; α/β-giardin contractile elements adjust disc curvature to maximise contact with epithelial microvilli
- Trophozoites attach to the apical surface of enterocytes without invading — **strictly extracellular** pathogen
- Lectin-mediated adhesion: mannose-binding lectins on *Giardia* interact with mannose residues on enterocyte glycocalyx

**4. Disruption of epithelial barrier:**
- **Tight junction disruption:** *Giardia* secreted proteases (cysteine proteases: CP2, CP14, CP49) cleave ZO-1 (zonula occludens-1); trophozoites signal through PAR-2 (protease-activated receptor 2) → PKC activation → claudin-2 upregulation (creates paracellular cation channels) → increased permeability
- Claudin-1 and occludin are redistributed from tight junctions → "leaky gut" phenotype, paracellular leak of luminal antigens and water
- **Microvillus shortening and villous blunting:** Direct physical stripping of microvilli by disc adhesion; secreted proteins (giardipain, GlcNAcase) contribute; net effect: reduced brush border surface area → malabsorption

**5. Malabsorption mechanisms:**
- **Disaccharidase deficiency:** Brush border lactase, sucrase, maltase activities severely reduced (enzyme proteins displaced from membrane) → carbohydrate malabsorption → osmotic diarrhea component
- **Fat malabsorption:** Reduced bile salt availability (Giardia deconjugates bile salts via its own hydrolases; deconjugated bile salts are less effective detergents for fat emulsification) + reduced lipase access → fat malabsorption → steatorrhoea
- **Chloride secretion:** Cysteine proteases activate PAR-2 on enterocytes → increased Cl⁻ secretion through CFTR → secretory diarrhea component

**6. Encystation (trophozoite → cyst):**
- As trophozoites pass distally into the ileum/colon, changing environment (cholesterol depletion, bile acid reduction, alkaline pH) triggers differentiation
- Encystation-specific vesicles (ESVs) form from ER; synthesise and transport cyst wall components (CWP1/2/3 — cyst wall proteins; β-1,3-GalNAc polymer) to the surface
- Mature cysts are shed in feces; can remain infectious in environment for months

## Host Interactions

**Cells and tissues targeted:**

| Cell/Tissue | Interaction | Mechanism |
|:---|:---|:---|
| Enterocytes (duodenum/jejunum) | Adhesion; barrier disruption; microvillus stripping | Disc attachment; tight junction cleavage; ROS induction |
| Goblet cells | Mucus layer disruption | Giardia reduces mucin secretion; thinner protective mucus layer |
| Innate immune cells (macrophages, neutrophils, mast cells) | Limited activation | Giardia suppresses NF-κB in enterocytes; mast cell degranulation contributes to symptoms |
| Dendritic cells | Partial activation + suppression of maturation | TLR4 activation; simultaneous IL-12 suppression; Th2 skewing |
| IgA-producing B cells | Humoral response drives VSP switching | Anti-VSP IgA in intestinal lumen triggers VSP change → immune escape |

**Immune evasion — VSP antigenic variation:**

*Giardia* expresses ~190 VSP variants encoded in the genome; only **one VSP is expressed per trophozoite** at any time. VSP genes are silenced epigenetically (histone H3K4me3 marks at the active locus; RNA interference (RNAi) pathway suppresses inactive loci). When mucosal IgA directed at the surface VSP accumulates, parasites switch to an alternative VSP — allowing escape from antibody-mediated killing. This mechanism is analogous to antigenic variation in *Trypanosoma* (VSG) but involves a smaller gene family and a different regulatory mechanism.

**Immune status and outcome:**
- **Immunocompetent:** CD4+ T cell and IgA responses eventually clear infection (4–6 weeks); protective immunity is VSP-specific and incomplete
- **Hypogammaglobulinaemia (CVID, agammaglobulinaemia):** Chronic, treatment-refractory giardiasis — IgA is the critical effector for clearance; these patients require long-term or repeated treatment courses
- **HIV/AIDS:** Giardiasis common but usually not severe unless concurrent B cell dysfunction; CD4 count is not the primary determinant (unlike T. gondii)

## Connections

- **Infects** → [Small Intestine](../../../01-human/06-organ/small-intestine/README.md): Trophozoites attach to duodenal and jejunal brush border via ventral disc; VSP antigenic variation evades mucosal IgA; disruption of tight junctions (ZO-1 redistribution) causes villous blunting and malabsorption.

- **Damages** → [Digestive System](../../../01-human/07-system/digestive-system/README.md): Disruption of duodenal and jejunal epithelium reduces digestive enzyme activity; villous blunting causes fat malabsorption (steatorrhoea); lactase deficiency often persists after clearance.

- **Damages** → [Immune System](../../../01-human/07-system/immune-system/README.md): Secretory IgA production against VSPs drives antigenic switching; CD4+ T cell-mediated immunity required for clearance; hypogammaglobulinaemia (e.g. common variable immunodeficiency) leads to chronic giardiasis.

- **Damages** → [Dendritic Cell](../../../01-human/04-cellular/dendritic-cell/README.md): Giardia-derived proteases activate dendritic cells via TLR4; paradoxical suppression of DC maturation and IL-12 production reduces Th1 responses, facilitating persistent infection.

## Pathology

**Clinical giardiasis:**

Incubation period: **1–3 weeks** (average ~14 days). Three clinical patterns:
1. **Asymptomatic carriage** (~50–60% of infected individuals): Cyst excretion without symptoms; common in endemic regions (acquired partial immunity in childhood)
2. **Acute giardiasis:** Abrupt onset of watery, foul-smelling (often greasy/fatty), non-bloody diarrhea; bloating, flatulence (excessive hydrogen/CO₂ from fermentation), abdominal cramps, nausea, anorexia; weight loss common; fever absent or low-grade; self-limited in 2–6 weeks in immunocompetent hosts
3. **Chronic giardiasis:** Intermittent diarrhea, steatorrhoea, malabsorption syndrome; significant weight loss, fatigue; lactose intolerance often develops and may persist; children: growth stunting, cognitive impairment; may persist for months-years without treatment

**Epidemiology:**

| Parameter | Value |
|:---|:---|
| Global burden | ~280–300 million cases/year |
| Prevalence (endemic areas) | Up to 30–40% of children in developing countries |
| Waterborne outbreaks (USA) | Leading protozoan cause; multiple large outbreaks from unfiltered municipal water |
| Infectious dose | ~10 cysts |
| Cyst survival | Months in cold water; killed by boiling; resistant to standard chlorination |

**Diagnosis:**

| Test | Sensitivity | Notes |
|:---|:---|:---|
| Stool microscopy (ova & parasite, ×3 specimens) | 60–90% cumulative | Trophozoites (diarrheal stool) or cysts (formed stool); iodine/trichrome stain; sensitivity increases with serial samples |
| Stool antigen EIA/immunochromatography | ~90–99% | Detects VSP or other antigens; preferred rapid test; single specimen sufficient |
| Stool PCR | ~95–100% | Gold standard sensitivity; used in outbreak investigation; also genotypes assemblage |
| Duodenal aspiration/biopsy | 95% | Reserved for seronegative, treatment-refractory cases; "Giardia string test" (Enterotest) as alternative to endoscopy |

**Treatment:**

| Drug | Dose | Duration | Notes |
|:---|:---|:---|:---|
| Tinidazole | 2 g orally, single dose | 1 day | First-line; single-dose simplicity; 90–95% cure rate |
| Metronidazole | 250 mg TID orally | 5–7 days | Effective; GI side effects (metallic taste, nausea); avoid alcohol |
| Nitazoxanide | 500 mg BID orally | 3 days | Alternative; useful in children (liquid formulation); also active against Cryptosporidium |
| Albendazole | 400 mg daily orally | 5 days | Alternative; less effective but useful when other agents unavailable |
| Paromomycin | 500 mg TID orally | 5–10 days | Preferred in pregnancy (poorly absorbed; minimal systemic exposure) |

[^ankarklev-2010-giardia]: Ankarklev J, et al. Behind the smile: cell biology and disease mechanisms of Giardia species. Nat Rev Microbiol. 2010;8(6):413–22.
[^buret-2008-giardia]: Buret AG. Pathophysiology of enteric infections with Giardia duodenalis. Parasite. 2008;15(3):261–5.
[^mandell-principles]: Bennett JE, Dolin R, Blaser MJ. Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases. 9th ed. Elsevier; 2020.
[^murray-microbiology]: Murray PR, Rosenthal KS, Pfaller MA. Medical Microbiology. 9th ed. Elsevier; 2021.

---
schema: pathogen-entry/v1
id: helicobacter-pylori
name: Helicobacter pylori
atlas: 02-pathogen
scale: 02-bacteria
status: draft
last_reviewed: 2026-06-05
summary: "Gram-negative microaerophilic spiral rod; colonises ~50% of humanity. IARC class I carcinogen. Causes peptic ulcers, gastric adenocarcinoma, and MALT lymphoma via urease, CagA T4SS injection, and VacA cytotoxin."
aliases: ["H. pylori", "Campylobacter pylori", "HP", "CagA+ H. pylori", "pylori"]
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
cross_links:
  - target: 01-human/06-organ/stomach
    relation: infects
    note: "H. pylori colonises gastric antrum and body using urease (NH₃ neutralises acid) and BabA/SabA adhesins; CagA T4SS injection and VacA disrupt epithelial signalling; long-term colonisation causes type B chronic active gastritis."
  - target: 01-human/07-system/digestive-system
    relation: damages
    note: "H. pylori causes 95% of duodenal and 70% of gastric ulcers; disrupts the somatostatin→gastrin→acid balance; CagA+ strains drive intestinal metaplasia→dysplasia→non-cardia gastric adenocarcinoma; MALT lymphoma responds to antibiotic eradication."
  - target: 01-human/04-cellular/macrophage
    relation: damages
    note: "VacA toxin inhibits T cell IL-2 signalling and impairs macrophage phagosome maturation (↓V-ATPase → intracellular survival); CagA disrupts macrophage apoptosis signalling, enabling chronic persistent infection despite immune activation."
  - target: 01-human/06-organ/liver
    relation: damages
    note: "H. pylori LPS reaches the liver via portal blood; eradication improves liver enzymes in NAFLD (meta-analysis); urease-derived NH₃ may exacerbate hepatic encephalopathy in cirrhosis via the gut-liver axis."
  - target: 03-medicine/01-modern/08-gi/omeprazole
    relation: treated-by
    note: "PPI (omeprazole) is essential in H. pylori eradication: raises gastric pH → synergizes with clarithromycin (acid-labile) and amoxicillin; Maastricht VI (2022): standard triple therapy (PPI + clarithromycin + amoxicillin × 14 days); bismuth quadruple for clarithromycin-resistant regions."
  - target: 03-medicine/01-modern/06-antimicrobial/amoxicillin
    relation: treated-by
    note: "Core component of H. pylori triple therapy (PPI + clarithromycin + amoxicillin 1g BD × 14 days); targets H. pylori PBPs; clarithromycin resistance ~20–30% in Europe drives bismuth quadruple therapy preference."
---

# Helicobacter pylori

## Overview

*Helicobacter pylori* (H. pylori) is a **Gram-negative, microaerophilic (5% O₂), spiral-shaped flagellated rod** (~3 µm × 0.5 µm, with 4–6 unipolar flagella) that colonises the gastric mucosa of approximately **50% of the global human population** [^mandell-principles]. Prevalence is markedly higher in lower-income countries (>70%) and lower in high-income settings (<30%). The organism was classified as an **IARC Group 1 (definite) human carcinogen** in 1994, owing to its causal role in non-cardia gastric adenocarcinoma and MALT (mucosa-associated lymphoid tissue) lymphoma.

Despite infecting half of humanity, **~80% of colonised individuals remain asymptomatic**. The remaining 20% develop clinically significant sequelae — peptic ulcer disease (PUD), gastric cancer, or MALT lymphoma — depending on strain virulence factors (particularly CagA status), host genetics, and environmental cofactors.

Transmission occurs via **fecal-oral or gastric-oral routes** (saliva, vomit), predominantly in childhood within households where hygiene is limited. The organism has no environmental reservoir — humans are the only significant host.

## Structure

### Morphology

| Feature | Detail |
|:---|:---|
| **Shape** | Helical/spiral rod with slight curvature |
| **Dimensions** | ~3 µm long × 0.5 µm wide |
| **Flagella** | 4–6 unipolar (single-pole bundle), sheathed; required for motility through mucus viscosity gradient |
| **Gram stain** | Gram-negative (thin peptidoglycan, outer membrane) |
| **Oxygen requirement** | Microaerophilic (5% O₂, 10% CO₂ optimal); cannot survive normal atmospheric O₂ |
| **Culture** | Grows slowly (3–7 days) on blood/chocolate agar with antibiotic supplements (trimethoprim, vancomycin) to suppress competing flora |

### Key Structural Components

- **Outer membrane proteins (OMPs):** BabA (blood group antigen binding adhesin A) — binds Lewis b antigen on gastric epithelium → anchors colonisation; SabA (sialyl-Lewis x binding adhesin) — binds inflamed gastric mucosa expressing sialyl-Lewis x; OipA (outer inflammatory protein A) — proinflammatory signalling
- **Lipopolysaccharide (LPS):** Modified lipid A with low immunostimulatory capacity (↓TLR4 activation compared to *E. coli*); LPS O-antigen contains Lewis x/y antigens (molecular mimicry of human blood group antigens — may reduce immune recognition)
- **Flagellar sheath:** Outer membrane-derived; protects flagellin from gastric acid degradation; also conceals flagellin from TLR5 detection

## Infection Mechanism

### Survival in Gastric Acid — the Urease Strategy

The greatest challenge for *H. pylori* colonisation is the gastric acid barrier (pH 1–2 in the lumen). *H. pylori* overcomes this via **urease** — a hexadimeric nickel-containing enzyme that constitutes ~6% of total bacterial protein [^murray-microbiology]:

```
Urea  →  NH₃ + CO₂   (urease, ~1 µmol urea/min/mg protein)
NH₃ + H⁺  →  NH₄⁺   (local acid neutralisation)
```

Urease creates a micro-environment of pH 6–7 in the periplasm and immediate bacterial vicinity, allowing survival and motility through the mucus layer to reach the near-neutral (pH 6–7) mucus gel overlying epithelial cells.

**Diagnostic use of urease:**
- **CLO test (Campylobacter-like organism test):** Gastric biopsy in urea + pH indicator gel; turns pink/red if urease-positive
- **Urea breath test (UBT):** Patient ingests ¹³C-labelled urea → exhaled ¹³CO₂ detected (sensitivity >95%, specificity >95%); gold-standard non-invasive test
- **Stool antigen test (SAT):** ELISA for *H. pylori* antigen in stool; convenient, validated for eradication confirmation
- **Serology (IgG):** Inexpensive but cannot distinguish active from past infection; not useful for eradication confirmation

### CagA and the Type IV Secretion System (T4SS)

The **cag pathogenicity island (cagPAI)** — a 40-kb genomic island present in ~60% of Western and ~90% of East Asian strains — encodes a **Type IV secretion system (T4SS)** that injects the **CagA oncoprotein** directly into gastric epithelial cells [^mandell-principles]:

1. *H. pylori* attaches to epithelium via integrins (α5β1) contacted by CagL (T4SS pilus tip)
2. T4SS pilus translocates CagA protein into epithelial cytoplasm
3. Host kinases (Src, Abl) phosphorylate CagA on EPIYA motifs (East Asian EPIYA-D > Western EPIYA-C in oncogenic potency)
4. Phosphorylated CagA binds and activates **SHP-2 phosphatase** (proto-oncogenic) → ERK/MAPK activation → ↑cell proliferation, ↓apoptosis, disrupted cell polarity (hummingbird phenotype via PAR1 kinase)
5. Non-phosphorylated CagA also disrupts E-cadherin/β-catenin junctions → nuclear β-catenin → Wnt target gene activation

CagA+ strains carry **significantly higher risk** of PUD, gastric adenocarcinoma, and MALT lymphoma vs. CagA– strains.

### VacA — the Vacuolating Cytotoxin

**VacA (vacuolating cytotoxin A)** is a pore-forming toxin (~140 kDa monomer, assembles into anion-selective channels in target membranes) with multiple immunopathological functions:

| VacA activity | Mechanism | Consequence |
|:---|:---|:---|
| **Vacuolation** | Forms pores in late endosomal membranes → inhibits V-ATPase → swollen, acidified vacuoles | Epithelial cell death; tissue damage |
| **Mitochondrial targeting** | Inserts into inner mitochondrial membrane → cytochrome c release | Intrinsic apoptosis |
| **T cell suppression** | Forms channels in T cell plasma membranes → ↓Ca²⁺ signalling → inhibits NFAT/IL-2 transcription | Impairs adaptive immunity — paradoxical immune evasion |
| **Tight junction disruption** | Targets claudin-4 → paracellular permeability ↑ | Allows bacterial access to deeper mucosa |
| **Macrophage interference** | Impairs phagolysosomal V-ATPase → ↓intracellular killing | Enables intracellular survival |

VacA allelic variation (s1/s2 signal region; m1/m2 middle region) predicts cytotoxicity: **s1/m1 VacA** (most cytotoxic) correlates with highest PUD and cancer risk.

## Host Interactions

### Gastric Acid Dysregulation — the Pathogenic Cascade

*H. pylori* colonisation disrupts the finely regulated gastric acid circuit:

1. **Antrum-predominant colonisation (most strains):**
   - CagA/OipA → IL-8 production → neutrophilic antral gastritis
   - NH₃ from urease damages somatostatin-producing **D cells** in antrum → ↓somatostatin → loss of paracrine inhibition of gastrin (G cells)
   - ↑Gastrin (hypergastrinaemia) → ↑ECL cell histamine → ↑parietal cell HCl secretion
   - Result: **Hyperacidity → duodenal ulcer** (duodenal metaplasia allows colonisation of duodenum; CagA+ strains especially)

2. **Corpus-predominant colonisation (↑atrophy, some CagA+ strains, autoimmune gastritis overlap):**
   - Extensive inflammation → parietal cell loss → ↓acid → **hypochlorhydria**
   - ↓Acid → ↑bacterial overgrowth in stomach → nitrosamines from ingested nitrates
   - Intestinal metaplasia (IM — CDX2+ goblet cells replace gastric mucosa) → dysplasia → **intestinal-type gastric adenocarcinoma** (Lauren classification, Correa cascade: normal mucosa → chronic gastritis → atrophic gastritis → IM → dysplasia → cancer)

### Immune Evasion

| Mechanism | Detail |
|:---|:---|
| **LPS molecular mimicry** | Lewis x/y antigens on LPS mimic host blood group Ags; ↓TLR4 stimulation (modified lipid A) |
| **VacA T cell suppression** | ↓IL-2/NFAT → impairs CD4⁺ effector T cell activation |
| **CagA disrupts apoptosis** | ↓Apoptosis of infected cells via SHP-2/Bcl-2 → chronic bacterial reservoir |
| **Flagellin concealment** | Flagellar sheath hides TLR5-stimulating flagellin from innate sensing |
| **Urease NH₃** | Directly damages neutrophils (peroxynitrite-mediated toxicity) |

## Connections

- **Infects** → [Stomach](../../../01-human/06-organ/stomach/README.md): H. pylori colonises the gastric antrum and body, surviving gastric acid via urease (NH₃)-mediated local neutralisation and motility through mucus. BabA and SabA adhesins anchor the organism to the gastric epithelium. CagA injection and VacA cytotoxin drive chronic type B active gastritis [^mandell-principles].
- **Damages** → [Digestive system](../../../01-human/07-system/digestive-system/README.md): H. pylori is the causative agent of 95% of duodenal and 70% of gastric peptic ulcers. CagA+ strains disrupt somatostatin→gastrin→acid regulation, drive intestinal metaplasia (Correa cascade), and are causal in non-cardia gastric adenocarcinoma (~75% attributable fraction). MALT lymphoma uniquely responds to antibiotic eradication alone in 80% of cases [^mandell-principles].
- **Damages** → [Macrophage](../../../01-human/04-cellular/macrophage/README.md): VacA impairs V-ATPase function in macrophage phagolysosomes, enabling intracellular bacterial survival. VacA also inhibits T cell IL-2 signalling. CagA disrupts macrophage apoptosis via SHP-2, sustaining the chronic bacterial reservoir [^murray-microbiology].
- **Damages** → [Liver](../../../01-human/06-organ/liver/README.md): H. pylori LPS traffics to the liver via portal circulation. Meta-analyses report improved liver enzymes after H. pylori eradication in NAFLD patients. Urease-derived NH₃ may exacerbate hepatic encephalopathy in cirrhotic patients via the gut-liver axis [^murray-microbiology].
- **Treated-by** → [Omeprazole](../../../03-medicine/01-modern/08-gi/omeprazole/README.md): PPI (omeprazole) is essential in H. pylori eradication: raises gastric pH → synergizes with clarithromycin (acid-labile) and amoxicillin; Maastricht VI (2022): standard triple therapy (PPI + clarithromycin + amoxicillin × 14 days); bismuth quadruple for clarithromycin-resistant regions.
- **Treated-by** → [Amoxicillin](../../../03-medicine/01-modern/06-antimicrobial/amoxicillin/README.md): Core component of H. pylori triple therapy (PPI + clarithromycin + amoxicillin 1g BD × 14 days); targets H. pylori PBPs; clarithromycin resistance ~20–30% in Europe drives bismuth quadruple therapy preference.

## Pathology

### Disease Spectrum

| Disease | Epidemiology | Key Mechanism | Notes |
|:---|:---|:---|:---|
| **Asymptomatic gastritis** | ~80% of infected | Chronic mucosal inflammation without symptoms | Most common outcome |
| **Duodenal ulcer (DU)** | 95% are H. pylori+ | Antral gastritis → ↑acid → duodenal injury | M:F ~4:1; anterior duodenum; risk of bleeding/perforation |
| **Gastric ulcer (GU)** | 70% are H. pylori+ | Corpus gastritis → mucosal protection ↓ | Lesser curvature body/antrum; 5% risk of underlying cancer → biopsy mandatory |
| **Gastric adenocarcinoma** | ~75% non-cardia cases attributable | Correa cascade: atrophy→IM→dysplasia→cancer | 5th most common cancer globally; EAC/cardia not related |
| **MALT lymphoma** | H. pylori in >90% of gastric MALT | Chronic T-cell stimulation → B-cell lymphoproliferation | 80% achieve complete remission with eradication alone; API2-MALT1 translocation → eradication-resistant |
| **Iron deficiency anaemia (IDA)** | Emerging association | H. pylori competes for luminal iron; antral gastritis → ↓iron absorption | Consider H. pylori testing in unexplained IDA |

### Treatment

**Test-and-treat strategy:** Indicated for PUD, MALT lymphoma, first-degree relatives of gastric cancer patients, and in regions with high gastric cancer incidence. Eradication should be confirmed with UBT or stool antigen test ≥4 weeks after completing therapy (off PPI ≥2 weeks before testing).

| Regimen | Components | Duration | Notes |
|:---|:---|:---|:---|
| **Clarithromycin triple therapy** | PPI + clarithromycin + amoxicillin | 10–14 days | Declining efficacy (>20% clarithromycin resistance in many regions) — first-line only where resistance <15% |
| **Bismuth quadruple therapy** | Bismuth + PPI + metronidazole + tetracycline | 10–14 days | Preferred where clarithromycin resistance high; also effective for metronidazole-resistant strains |
| **Concomitant therapy** | PPI + clarithromycin + amoxicillin + metronidazole | 10–14 days | Non-bismuth quadruple; useful in areas with dual resistance |
| **Rifabutin-based rescue** | PPI + rifabutin + amoxicillin | 7–14 days | Third-line rescue; risk of myelosuppression |
| **Culture-guided therapy** | Guided by susceptibility testing | Variable | Optimal where resistance testing available |

### Diagnosis Summary

| Test | Sensitivity | Specificity | Notes |
|:---|:---|:---|:---|
| UBT (¹³C) | >95% | >95% | Best non-invasive; requires off PPI ≥2 weeks |
| Stool antigen (monoclonal) | 94% | 97% | Good for eradication confirmation |
| CLO test (biopsy urease) | 90–95% | 95–100% | Requires endoscopy; false-negative if PPI use or bleeding |
| Serology (IgG) | 85% | 79% | Cannot confirm eradication; useful for epidemiology |
| Histology (Giemsa/Warthin-Starry) | 93–99% | 95–99% | Gold standard; allows assessment of gastritis/IM/dysplasia |
| Culture | 70–90% | 100% | Slow (5–7 days); essential for susceptibility testing |

[^mandell-principles]: Bennett JE, Dolin R, Blaser MJ. *Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases.* 9th ed. Elsevier; 2020.
[^murray-microbiology]: Murray PR, Rosenthal KS, Pfaller MA. *Medical Microbiology.* 9th ed. Elsevier; 2021.

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

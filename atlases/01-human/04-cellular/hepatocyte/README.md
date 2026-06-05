---
schema: human-scale-entry/v1
id: hepatocyte
name: Hepatocyte
atlas: 01-human
scale: 04-cellular
status: draft
last_reviewed: 2026-06-04
summary: "Parenchymal cell of the liver comprising ~80% of liver volume. Executes >500 metabolic functions: gluconeogenesis, lipid/cholesterol metabolism, protein synthesis (albumin, clotting factors), urea cycle, phase I/II drug metabolism (CYP450s), and bile acid synthesis."
aliases: ["liver parenchymal cell", "hepatic cell"]
sources:
  - id: taub-2004-hepatocyte-regeneration
    type: peer-reviewed
    cite: "Taub R. Liver regeneration: from myth to mechanism. Nat Rev Mol Cell Biol. 2004;5(10):836-47."
    doi: "10.1038/nrm1489"
    pmid: "15459664"
    url: "https://doi.org/10.1038/nrm1489"
  - id: gebhardt-2014-hepatocyte-heterogeneity
    type: peer-reviewed
    cite: "Gebhardt R, Matz-Soja M. Liver zonation: Novel aspects of its regulation and its impact on homeostasis. World J Gastroenterol. 2014;20(26):8491-504."
    doi: "10.3748/wjg.v20.i26.8491"
    pmid: "25024605"
    url: "https://doi.org/10.3748/wjg.v20.i26.8491"
  - id: hall-guyton-14-liver
    type: textbook
    cite: "Hall JE. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021. Ch. 71."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-04"
  - id: de-la-rosa-2021-hepatocyte-cyp450
    type: peer-reviewed
    cite: "Zanger UM, Schwab M. Cytochrome P450 enzymes in drug metabolism: regulation of gene expression, enzyme activities, and impact of genetic variation. Pharmacol Ther. 2013;138(1):103-41."
    doi: "10.1016/j.pharmthera.2012.12.007"
    pmid: "23333322"
    url: "https://doi.org/10.1016/j.pharmthera.2012.12.007"
cross_links:
  - target: 01-human/05-tissue/hepatic-lobule
    relation: part-of
    note: "Hepatocytes are arranged in cords within the hepatic lobule, radiating from the central vein."
  - target: 01-human/06-organ/liver
    relation: part-of
    note: "Hepatocytes are the dominant parenchymal cell population constituting ~80% of liver volume."
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: damaged-by
    note: "SARS-CoV-2 injures hepatocytes via ACE2-mediated direct infection and immune-mediated hepatitis; COVID-19 liver injury is seen in 14-53% of patients."
  - target: 03-medicine/01-modern/04-cardio/statins
    relation: modulated-by
    note: "Statins inhibit HMG-CoA reductase in hepatocytes, reducing intracellular cholesterol synthesis and upregulating LDL receptor expression to clear circulating LDL-C."
  - target: 02-pathogen/01-viruses/hepatitis-b-virus
    relation: infected-by
    note: "Hepatocytes are the exclusive replication site for HBV; viral entry is mediated by preS1 binding to NTCP (SLC10A1) transporter; cccDNA persists in nucleus as viral minichromosome, conferring lifelong reservoir."
  - target: 02-pathogen/01-viruses/hepatitis-b-virus
    relation: damaged-by
    note: "HBV-mediated hepatocyte injury is primarily immune-mediated (CTL-driven hepatocyte killing) rather than direct cytopathic; hepatocyte loss drives fibrosis, cirrhosis, and HCC risk."
  - target: 01-human/03-molecular/tnf-alpha
    relation: damaged-by
    note: "High-concentration TNF-α causes hepatocyte apoptosis via TNFR1-caspase-8-caspase-3 cascade; a key mechanism of hepatocyte loss in septic shock, alcoholic hepatitis, and drug-induced liver injury."
  - target: 02-pathogen/04-parasites/plasmodium-falciparum
    relation: infected-by
    note: "P. falciparum sporozoites invade hepatocytes via CD81/SR-B1 after Anopheles inoculation; clinically silent hepatic schizogony produces 10,000–30,000 merozoites per infected hepatocyte over 5–7 days before bloodstream release."
taxonomy:
  cell_ontology: "CL:0000182"
  lineage: "endoderm — hepatic endoderm — hepatoblast — hepatocyte"
---

# Hepatocyte

## Overview

The hepatocyte is the principal parenchymal cell of the liver — a large (~20–30 µm diameter), polygonal, binucleate-capable cell that carries out the overwhelming majority of the liver's metabolic activities. Constituting approximately 60–80% of total liver cell number and ~80% of liver volume, hepatocytes execute more than 500 distinct metabolic functions, making them among the most metabolically diverse cells in the human body [^hall-guyton-14-liver].

Key metabolic domains include:
- **Carbohydrate metabolism:** gluconeogenesis, glycogenolysis, glycogen synthesis, glycolysis
- **Lipid metabolism:** fatty acid oxidation (β-oxidation), de novo lipogenesis, triglyceride synthesis, ketogenesis (acetoacetate and β-hydroxybutyrate), lipoprotein synthesis (VLDL)
- **Protein synthesis:** albumin (the dominant plasma protein maintaining oncotic pressure), clotting factors (fibrinogen; factors II, V, VII, VIII, IX, X, XI; protein C and S), complement proteins, acute-phase reactants (CRP, fibrinogen, haptoglobin)
- **Detoxification:** phase I reactions (CYP450s: CYP1A2, CYP2C9, CYP2D6, CYP3A4 — oxidation/reduction/hydrolysis); phase II reactions (glucuronidation, sulfation, glutathione conjugation — increase solubility); phase III (transporters for biliary/renal excretion)
- **Bile acid synthesis:** cholesterol → primary bile acids (cholic and chenodeoxycholic acid) → conjugated with glycine/taurine → secreted into bile for fat emulsification in intestine
- **Nitrogen metabolism:** urea cycle (detoxifies NH₃ from amino acid catabolism → urea for renal excretion)
- **Vitamin/mineral storage:** vitamin A (hepatic stellate cells in Disse space), vitamin D, vitamin B₁₂, iron (as ferritin and hemosiderin)

Hepatocytes can regenerate extensively after injury — a feature exploited in living-donor partial liver transplantation (removal of 60-70% hepatic mass → full regeneration within 4–8 weeks) [^taub-2004-hepatocyte-regeneration].

## Structure

### Morphology

| Feature | Value |
|:---|:---|
| Diameter | 20–30 µm |
| Shape | Polygonal with 6–8 sides |
| Nuclei | 1–2 (25–30% binucleate in adults); large, centrally placed, euchromatic |
| Ploidy | Mix of 2n, 4n, 8n (polyploidy increases with age) |
| Volume | ~6,000 µm³ |
| Lifespan | ~150–500 days (slow turnover in normal liver) |

### Plasma Membrane Domains

Hepatocytes have three functionally distinct plasma membrane surfaces:

1. **Basolateral (sinusoidal) surface** (~70% of membrane area): faces the space of Disse and the liver sinusoidal endothelial cells (LSECs). Contains transporters for uptake from portal blood (NTCP for bile salts, OATPs for bilirubin and drugs, glucose transporters, amino acid transporters). Secretes albumin, clotting factors, VLDL directly into portal blood.

2. **Lateral surface** (~15%): connects adjacent hepatocytes via gap junctions (connexin-32, connexin-26) and desmosomes. Metabolic coupling between hepatocytes via gap junctions is important for coordinating glucagon/insulin signaling responses.

3. **Apical (canalicular) surface** (~15%): faces the bile canaliculus — the thin channel between adjacent hepatocytes that is the first segment of the biliary tree. Bile secretion transporters: BSEP (bile salt export pump, ABCB11), MRP2 (bilirubin-glucuronide secretion, ABCC2), MDR3 (phospholipid secretion, ABCB4).

### Key Organelles

- **Mitochondria** — ~1000–2000 per hepatocyte (~18% cell volume); central to β-oxidation, oxidative phosphorylation, urea cycle, ketogenesis
- **Endoplasmic reticulum (ER)** — extensively developed; rough ER (protein synthesis: albumin, clotting factors); smooth ER (CYP450 drug metabolism, cholesterol synthesis, glycogen metabolism)
- **Golgi complex** — large; protein glycosylation, sorting, secretion of albumin and VLDL
- **Peroxisomes** — abundant; very long-chain fatty acid oxidation (complement mitochondrial β-oxidation); catalase (H₂O₂ detoxification)
- **Lysosomes** — intracellular quality control; autophagy (critical for lipid droplet clearance in NAFLD)
- **Glycogen granules** — visible on electron and light microscopy; hepatocytes store ~150 g glycogen in fed state (major glucose buffer)

### Lipid Droplets

In well-nourished states, small lipid droplets are present. In excess caloric intake (especially fructose + saturated fat), droplets accumulate → hepatic steatosis (NAFLD). Steatosis alone is benign; transition to steatohepatitis (NASH) with ER stress, mitochondrial dysfunction, oxidative stress, and JNK activation → hepatocyte apoptosis/necroptosis → fibrosis → cirrhosis.

## Function

### Glucose Homeostasis

The hepatocyte is the central glucose buffer of the body:

- **Postprandial:** insulin → GLUT2 uptake → glucokinase activation → glycolysis + glycogen synthesis (glycogen synthase activated, glycogen phosphorylase inhibited); de novo lipogenesis from excess glucose → VLDL
- **Fasted/exercise:** glucagon → PKA → glycogen phosphorylase activation → glycogenolysis → glucose output; longer fasting → gluconeogenesis from lactate (Cori cycle), alanine (glucose-alanine cycle), and glycerol
- **Extended fasting/starvation:** fatty acid β-oxidation in hepatocyte mitochondria → excess acetyl-CoA → ketogenesis (acetoacetate, β-hydroxybutyrate) → exported to brain and muscle as fuel

### Lipid and Cholesterol Metabolism

Hepatocytes synthesize ~70% of whole-body cholesterol via the **mevalonate pathway** (acetyl-CoA → HMG-CoA → (HMG-CoA reductase) → mevalonate → cholesterol). **Statins** inhibit HMG-CoA reductase, reducing hepatocyte cholesterol synthesis, upregulating LDL receptors, and clearing circulating LDL-C [^de-la-rosa-2021-hepatocyte-cyp450].

VLDL is assembled in hepatocytes: triglycerides + ApoB-100 + cholesterol ester → VLDL particle → secreted → plasma lipolysis → IDL → LDL.

### Protein Synthesis and Secretion

The hepatocyte is the primary factory for plasma proteins:
- **Albumin** — 10–15 g/day; maintains oncotic pressure (~80% of total plasma oncotic pressure); binds/transports fatty acids, bilirubin, calcium, drugs
- **Clotting factors** — vitamin K-dependent factors (II/VII/IX/X) require hepatic carboxylase activity; PT/INR reflects hepatic synthetic function
- **Complement** — most complement cascade proteins (C1–C9) are hepatocyte-synthesized
- **Acute-phase proteins** — CRP, serum amyloid A, fibrinogen, haptoglobin: upregulated by IL-6 (JAK1-STAT3 pathway) during inflammation; albumin and transferrin suppressed as negative acute-phase reactants

### Drug Metabolism (CYP450 System)

The hepatocyte smooth ER houses the cytochrome P450 enzymes responsible for phase I drug metabolism:

| Enzyme | Substrates |
|:---|:---|
| CYP3A4 | Statins, cyclosporine, midazolam, HIV protease inhibitors (~50% of drugs) |
| CYP2D6 | Codeine→morphine, metoprolol, TCAs, fluoxetine |
| CYP2C9 | Warfarin, ibuprofen, phenytoin |
| CYP1A2 | Theophylline, caffeine, clozapine |
| CYP2C19 | Omeprazole, clopidogrel (prodrug activation), diazepam |

CYP polymorphisms (genetic variation in CYP2D6, CYP2C19) create poor/intermediate/extensive/ultrarapid metabolizer phenotypes — the basis of pharmacogenomics-guided prescribing.

### Urea Cycle (Ammonia Detoxification)

Amino acid catabolism and gut bacterial protein breakdown generate ammonia (NH₃), which is neurotoxic. Hepatocytes convert NH₃ → urea via the urea cycle (primarily in periportal zone 1 hepatocytes):
```
NH₃ + CO₂ → carbamoyl phosphate → citrulline → argininosuccinate → arginine → urea + ornithine
Urea → blood → kidneys → excreted in urine
```
In liver failure, urea cycle capacity falls → hyperammonemia → hepatic encephalopathy.

## Lifecycle

### Origin and Embryonic Development

Hepatocytes derive from the **hepatic endoderm** — a thickening of the foregut endoderm at ~E9.5 (mouse) / ~week 4 (human), induced by FGF signals from adjacent cardiac mesoderm and BMP signals from the septum transversum. Hepatic progenitors (**hepatoblasts**) are bipotential — they can differentiate into hepatocytes or cholangiocytes (biliary epithelial cells). The transcription factor cascade includes Foxa2, GATA4, HNF4α, and C/EBPα.

### Postnatal Growth and Zonal Heterogeneity

The liver grows postnatally through hepatocyte hypertrophy and limited proliferation. Adult hepatocytes are not homogeneous — the liver is **metabolically zonated** [^gebhardt-2014-hepatocyte-heterogeneity]:
- **Zone 1 (periportal):** receives O₂-rich portal blood; specializes in gluconeogenesis, β-oxidation, urea synthesis, bile acid secretion
- **Zone 3 (centrilobular/perivenous):** receives O₂-depleted blood; specializes in glycolysis, de novo lipogenesis, CYP450 drug metabolism (especially CYP2E1, CYP3A4); most susceptible to ischemia and zone-3-specific toxins (acetaminophen)
- Zonation is maintained by Wnt/β-catenin gradients (high in zone 3), decreasing toward zone 1

### Regeneration

The liver has remarkable regenerative capacity:
- After 70% partial hepatectomy (the model used in rodents and clinically in living-donor transplant), remaining hepatocytes — ordinarily quiescent — re-enter the cell cycle within hours
- **Key signals:** Partial hepatectomy → portal blood surge → cytokine priming (TNF-α, IL-6, NF-κB, STAT3) → growth factor activation (HGF/c-Met, EGF/EGFR, Wnt) → hepatocyte proliferation
- Regeneration is complete within 7–14 days in rodents, 4–8 weeks in humans
- In massive injury where hepatocyte regeneration is overwhelmed (e.g., acute liver failure), **hepatic progenitor cells** (Canals of Hering, oval cells) can be recruited as backup

### Cell Turnover in Normal Liver

In undisturbed adult liver, hepatocytes turnover slowly — estimated half-life ~150–450 days. A Wnt-driven "streaming" model from portal to central venous zones has been proposed based on clonal analysis, though this remains debated.

## Connections

- **Part of:** [Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md) — the functional tissue unit.
- **Part of:** [Liver](../../06-organ/liver/README.md) — the organ.
- **Damaged by:** SARS-CoV-2 — direct ACE2-mediated infection of hepatocytes/cholangiocytes; immune-mediated hepatitis; drug-induced liver injury from COVID-19 treatments.
- **Modulated by:** [Statins](../../../03-medicine/01-modern/04-cardio/statins/README.md) — HMG-CoA reductase inhibition reduces cholesterol synthesis; upregulation of LDL receptor clears LDL-C from circulation; rare statin-induced hepatotoxicity (transaminase elevation).

[^taub-2004-hepatocyte-regeneration]: Taub R. Liver regeneration: from myth to mechanism. *Nat Rev Mol Cell Biol.* 2004;5(10):836-47. [doi:10.1038/nrm1489](https://doi.org/10.1038/nrm1489) · [PubMed 15459664](https://pubmed.ncbi.nlm.nih.gov/15459664/)
[^gebhardt-2014-hepatocyte-heterogeneity]: Gebhardt R, Matz-Soja M. Liver zonation: Novel aspects of its regulation and its impact on homeostasis. *World J Gastroenterol.* 2014;20(26):8491-504. [doi:10.3748/wjg.v20.i26.8491](https://doi.org/10.3748/wjg.v20.i26.8491) · [PubMed 25024605](https://pubmed.ncbi.nlm.nih.gov/25024605/)
[^hall-guyton-14-liver]: Hall JE. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021. Ch. 71.
[^de-la-rosa-2021-hepatocyte-cyp450]: Zanger UM, Schwab M. Cytochrome P450 enzymes in drug metabolism. *Pharmacol Ther.* 2013;138(1):103-41. [doi:10.1016/j.pharmthera.2012.12.007](https://doi.org/10.1016/j.pharmthera.2012.12.007) · [PubMed 23333322](https://pubmed.ncbi.nlm.nih.gov/23333322/)

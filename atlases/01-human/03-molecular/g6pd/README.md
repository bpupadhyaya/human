---
schema: human-scale-entry/v1
id: g6pd
name: G6PD
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "G6PD (G6PD; chrXq28) is the pentose phosphate pathway enzyme that generates NADPH for glutathione reduction; X-linked deficiency (400M carriers) → oxidant-induced haemolytic anaemia; G-6-PD A− (Africa) and B− (Mediterranean) are the most common variants; protects vs malaria."
aliases: ["G6PD", "glucose-6-phosphate dehydrogenase", "G-6-PD", "G6PD deficiency", "G6PDd", "favism", "G6PD enzyme", "hexose monophosphate shunt"]
sources:
  - id: cappellini-2008-g6pd-review
    type: peer-reviewed
    cite: "Cappellini MD, Fiorelli G. Glucose-6-phosphate dehydrogenase deficiency. Lancet. 2008;371(9606):64-74."
    doi: "10.1016/S0140-6736(08)60073-2"
    pmid: "18177777"
    url: "https://doi.org/10.1016/S0140-6736(08)60073-2"
  - id: who-g6pd-working-group-1989
    type: clinical-guideline
    cite: "WHO Working Group. Glucose-6-phosphate dehydrogenase deficiency. Bull World Health Organ. 1989;67(6):601-611."
    pmid: "2633878"
    url: "https://pubmed.ncbi.nlm.nih.gov/2633878/"
cross_links:
  - target: 01-human/07-system/malaria
    relation: connects-to
    note: "G6PD heterozygosity confers ~50% protection vs severe P. falciparum malaria; G6PD-deficient patients risk haemolysis with primaquine or tafenoquine (P. vivax radical cure); WHO mandates G6PD testing before 8-aminoquinoline prescription."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "G6PD and haemoglobin variants (HbS, HbC, thalassaemia) are independent malaria-protective adaptations in overlapping endemic regions; G6PD deficiency + SCD → additive oxidant haemolysis risk; avoid dapsone and rasburicase in G6PD-deficient SCD."
  - target: 01-human/07-system/sickle-cell-disease
    relation: connects-to
    note: "G6PD A− deficiency (10-20% of sub-Saharan Africans) co-occurs with HbSS in ~5-10% of SCD patients; G6PD deficiency + SCD → increased haemolysis with oxidant drugs (dapsone for malaria prophylaxis, rasburicase, nitrofurantoin); G6PD screening recommended in SCD patients."
---

# G6PD

## Overview

**Glucose-6-phosphate dehydrogenase (G6PD; gene *G6PD*, chromosome Xq28)** is the rate-limiting enzyme of the **oxidative (non-reversible) branch of the pentose phosphate pathway (PPP)**, catalyzing the first and committed step: oxidation of glucose-6-phosphate to 6-phosphoglucono-δ-lactone, coupled to reduction of NADP⁺ to **NADPH** [^cappellini-2008-g6pd-review].

In red blood cells (RBCs), which lack mitochondria and thus rely entirely on glycolysis and the PPP for energy and reducing power, G6PD is the **sole source of NADPH**. NADPH is essential for:
1. **Glutathione (GSH) regeneration:** Glutathione reductase uses NADPH to reduce GSSG → 2GSH → glutathione peroxidase uses GSH to detoxify H₂O₂ and lipid peroxides
2. **Catalase activity:** Catalase requires NADPH as a cofactor for optimal H₂O₂ decomposition
3. **Methaemoglobin reduction:** Minor pathway to maintain Fe²⁺ haem iron

**G6PD deficiency** is the most common human enzyme defect, affecting approximately **400–500 million people worldwide** — predominantly males (X-linked; females can be heterozygous, affected homozygous, or unaffected) — with highest prevalence in sub-Saharan Africa, the Mediterranean, Middle East, and Southeast Asia. Its geographic distribution closely mirrors historical malaria endemicity, reflecting **balanced polymorphism**: heterozygous females gain partial malaria protection, maintaining the allele at high frequency despite the fitness cost in affected males [^cappellini-2008-g6pd-review].

## Structure

### Protein structure

G6PD is a **105 kDa homodimer** (2 × 514 amino acid subunits) or **tetramers** (2 dimers) at higher concentrations. Each subunit contains:
- **Coenzyme-binding domain (βαβ Rossmann fold):** NADP⁺/NADPH binding; the structural NADP⁺ binding site (not the catalytic site) stabilizes the dimer
- **β+α domain:** Contains Lys386 (catalytic); forms the substrate binding pocket
- **Dimerization interface:** Stabilized by dimer contact residues; mutations in this region destabilize the active enzyme

**Catalytic mechanism:**
1. Glucose-6-phosphate binds the active site → Lys386 (and His263) facilitate hydride transfer from C1 of G6P to NADP⁺
2. Product: 6-phosphoglucono-δ-lactone (spontaneously hydrolyzes to 6-phosphogluconate) + NADPH + H⁺
3. 6-phosphogluconate is further processed by 6-phosphogluconate dehydrogenase → ribulose-5-phosphate + NADPH + CO₂

**Structural NADP⁺:** Each monomer contains a second NADP⁺ binding site (structural, not catalytic) → NADP⁺ at this site stabilizes the G6PD dimer → without it, enzyme dissociates → reduced activity; clinically relevant because G6PD A− has normal enzyme activity at birth but loses structural NADP⁺ binding due to the N126D amino acid change → enzyme degrades prematurely during RBC lifespan

### WHO classification of G6PD variants

| WHO Class | Residual activity | Clinical significance | Examples |
|:---------|:-----------------|:---------------------|:---------|
| Class I | <10% (severe) | Chronic non-spherocytic haemolytic anaemia (CNSHA) | G6PD Mediterranean Hematological; G6PD Canton; rare |
| Class II | <10% (severe) | Episodic haemolysis with triggers | G6PD Mediterranean (B−; Ser188Phe); G6PD Mahidol (Southeast Asia) |
| Class III | 10-60% | Episodic haemolysis with strong triggers | G6PD A− (Africa; Val68Met + Asn126Asp); most common |
| Class IV | 60-150% | Normal | G6PD B (wild type); G6PD A+ (A− relative) |
| Class V | >150% | Normal or enhanced | Very rare; no clinical significance |

**Most clinically important variants:**
- **G6PD A−** (Asn126Asp + Val68Met): 10-15% of West African/African-American males; Class III; episodic haemolysis with infections, drugs; enzyme activity normal at first but falls with RBC aging → older cells most vulnerable; typically self-limited
- **G6PD Mediterranean** (Ser188Phe): <10% activity; Class II; severe haemolysis with broad range of triggers including fava beans; common in Italy, Greece, Sardinia, Middle East; highest risk for severe neonatal jaundice
- **G6PD Mahidol**: Southeast Asia (Thailand, Myanmar); Class II; similar to Mediterranean
- **G6PD Viangchan**: Laos, Cambodia; Class II

## Function

### NADPH in RBC oxidant defense

RBCs are highly vulnerable to oxidative stress because:
- Constant haem iron → risk of autoxidation to Fe³⁺ (methaemoglobin) → O₂ radical generation
- High O₂ concentrations in pulmonary capillaries
- Glucose-only fuel → PPP is the only NADPH source
- No mitochondria, no peroxisome → limited antioxidant redundancy

**G6PD → NADPH pathway in RBCs:**
1. Glucose-6-phosphate → 6-phosphogluconate (G6PD, rate-limiting; produces NADPH)
2. NADPH → glutathione reductase → GSH regenerated from GSSG
3. GSH → glutathione peroxidase → H₂O₂ + lipid peroxides detoxified → GSSG
4. Net: oxidant challenge is quenched by NADPH-fueled recycling of GSH

**In G6PD deficiency:** Oxidant stress overwhelms the reduced GSH pool → H₂O₂ accumulates → haem iron oxidizes (methaemoglobin) → globin chain cross-links and precipitates → **Heinz bodies** (denatured globin inclusions) → RBC membrane damage → splenic sequestration and extravascular haemolysis; additionally intravascular haemolysis occurs with severe oxidant challenge

### Non-erythroid functions

G6PD is expressed in all nucleated cells, where it serves:
- **Phagocyte oxidative burst:** Macrophages and neutrophils use G6PD-derived NADPH as substrate for NADPH oxidase (NOX2) → superoxide → hydrogen peroxide → kill ingested pathogens; severe G6PD deficiency → impaired neutrophil respiratory burst
- **Biosynthesis:** NADPH fuels fatty acid synthesis (acetyl-CoA carboxylase, FAS), cholesterol synthesis (HMG-CoA reductase), and nucleotide synthesis (via ribulose-5-phosphate → DNA/RNA precursors)
- **Anti-apoptosis:** NADPH maintains reduced cytochrome c, prevents caspase activation
- **Tumour metabolism:** High G6PD activity is required for rapidly proliferating cancer cells (high biosynthetic demand for NADPH and ribose-5-phosphate); G6PD is a potential oncology target

## Mechanism

### Clinical presentations of G6PD deficiency

**1. Neonatal jaundice:**
- Most common clinical manifestation globally; occurs in 50-70% of G6PD-deficient neonates in endemic areas
- Mechanism: Immature neonatal liver (limited bilirubin conjugation) + RBC G6PD enzyme activity lowest in neonates + oxidant triggers (cord clamping, hypothermia, infection, vitamin K injection) → acute haemolysis + hepatic bilirubin overload → indirect hyperbilirubinaemia → kernicterus risk if untreated
- Management: Phototherapy; exchange transfusion for severe hyperbilirubinaemia; avoid oxidant drugs

**2. Acute haemolytic anaemia (AHA) — oxidant-triggered:**

| Trigger category | Examples |
|:----------------|:---------|
| Drugs | Primaquine, tafenoquine, rasburicase (recombinant urate oxidase), dapsone, nitrofurantoin, methylene blue (paradoxically!), high-dose ascorbic acid, naphthalene, phenazopyridine |
| Infections | Viral hepatitis, EBV, CMV, pneumonia — any febrile illness can trigger haemolysis even without drug |
| Foods | Fava beans (Vicia faba) contain vicine and convicine → aglycones divicine/isouramil → direct ROS generation → severe haemolysis in Class II variants ("favism") |
| Metabolic | Diabetic ketoacidosis (acidosis + oxidant stress) |

**Haemolysis course (G6PD A−, Class III):**
- Day 1-3: Acute drop in Hb 2-4 g/dL; Heinz bodies on supravital stain; bite cells on smear (splenic macrophages "bite" Heinz-body-containing RBCs)
- Day 4-7: Self-limited — reticulocytes replace older vulnerable RBCs; reticulocytes have higher G6PD activity → resistant to further haemolysis → natural recovery even if drug continued
- Resolution: Hb recovers; drug can usually continue in Class III if critical

**G6PD Mediterranean (Class II) — more severe:**
- Young and old RBCs equally affected (enzyme barely functional)
- Fava bean ingestion → severe intravascular haemolysis → haemoglobinuria (dark urine) → renal failure possible
- May require RBC transfusion

**3. Chronic non-spherocytic haemolytic anaemia (CNSHA):**
- Class I variants → very low G6PD activity even in young RBCs → ongoing haemolysis without triggers
- Rare; splenomegaly; requires folic acid supplementation; severe cases may need transfusion

### G6PD deficiency and primaquine/tafenoquine — the critical clinical interaction

**P. vivax and P. ovale** form liver hypnozoites → relapse even after blood-stage clearance → radical cure requires **primaquine** (8-aminoquinoline, 14 days) or **tafenoquine** (8-aminoquinoline, single dose) to eliminate hypnozoites.

Both primaquine and tafenoquine → oxidant metabolites → acute haemolysis in G6PD-deficient patients:
- **Primaquine:** Haemolysis dose-dependent; G6PD A− (Class III) → moderate haemolysis; G6PD Mediterranean (Class II) → severe haemolysis
- **Tafenoquine (single dose, 300 mg):** Higher oxidant burden than primaquine; G6PD A− → clinically significant haemolysis; **contraindicated in patients with G6PD activity <70% of normal**
- **WHO/PAHO recommendation:** G6PD testing before primaquine or tafenoquine; point-of-care testing (SD BIOSENSOR CareStart G6PD RDT) now available

**G6PD testing methods:**
- **Spectrophotometric (gold standard):** Measures G6PD activity quantitatively; normal 7-10 U/g Hb; false-normal if high reticulocyte count (young cells have more G6PD)
- **Fluorescent spot test (WHO qualitative):** Screening tool; cannot detect heterozygous females reliably; inexpensive
- **Point-of-care RDT (CareStart G6PD):** Semi-quantitative; field-deployable; increasingly used in malaria-endemic settings
- **DNA genotyping:** Identifies specific variants; not needed clinically but useful for epidemiology

## Connections

- `connects-to` → **[Malaria](../../07-system/malaria/README.md)** — G6PD heterozygosity in females confers ~50% protection against severe P. falciparum malaria (mosaic RBC population); G6PD-deficient patients cannot receive primaquine or tafenoquine for P. vivax radical cure (acute haemolysis risk); must test G6PD before prescribing 8-aminoquinolines.
- `connects-to` → **[Hemoglobin](../hemoglobin/README.md)** — G6PD and haemoglobin variants (HbS, HbC, HbF, thalassaemia) represent independent protective adaptations to malaria in overlapping endemic regions; G6PD deficiency co-occurring with SCD → additive oxidant stress risk; avoid oxidant drugs (dapsone, rasburicase) in G6PD-deficient SCD.
- `connects-to` → **[Sickle Cell Disease](../../07-system/sickle-cell-disease/README.md)** — G6PD A− deficiency (10-20% of sub-Saharan Africans) co-occurs with HbSS in ~5-10% of SCD patients; G6PD deficiency + SCD → increased haemolysis with oxidant drugs (dapsone, rasburicase, nitrofurantoin); G6PD screening recommended in SCD patients.

[^cappellini-2008-g6pd-review]: Cappellini MD, Fiorelli G. Glucose-6-phosphate dehydrogenase deficiency. *Lancet.* 2008;371(9606):64-74. [doi:10.1016/S0140-6736(08)60073-2](https://doi.org/10.1016/S0140-6736(08)60073-2) · [PubMed 18177777](https://pubmed.ncbi.nlm.nih.gov/18177777/)
[^who-g6pd-working-group-1989]: WHO Working Group. Glucose-6-phosphate dehydrogenase deficiency. *Bull World Health Organ.* 1989;67(6):601-611. · [PubMed 2633878](https://pubmed.ncbi.nlm.nih.gov/2633878/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

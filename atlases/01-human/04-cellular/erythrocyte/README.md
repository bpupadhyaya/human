---
schema: human-scale-entry/v1
id: erythrocyte
name: Erythrocyte
atlas: 01-human
scale: 04-cellular
status: draft
last_reviewed: 2026-06-05
summary: "Anucleate biconcave disc (~7.5 µm). 250 million haemoglobin molecules carry 4 O₂ each; 25 trillion erythrocytes deliver ~250 mL O₂/min to tissues at rest. 120-day lifespan; removed by splenic macrophages. Erythropoietin (EPO) drives production in bone marrow."
aliases: ["red blood cell", "RBC", "red cell", "erythron"]
sources:
  - id: an-2008-rbc-membrane
    type: peer-reviewed
    cite: "An X, Mohandas N. Disorders of red cell membrane. Br J Haematol. 2008;141(3):367-75."
    doi: "10.1111/j.1365-2141.2008.07091.x"
    pmid: "18341630"
    url: "https://doi.org/10.1111/j.1365-2141.2008.07091.x"
  - id: bunn-2013-erythropoietin
    type: peer-reviewed
    cite: "Bunn HF. Erythropoietin. Cold Spring Harb Perspect Med. 2013;3(3):a011619."
    doi: "10.1101/cshperspect.a011619"
    pmid: "23457295"
    url: "https://doi.org/10.1101/cshperspect.a011619"
  - id: hillman-2019-hematology
    type: textbook
    cite: "Hillman RS, Ault KA, Leporrier M, Rinder HM. Hematology in Clinical Practice. 5th ed. McGraw-Hill; 2019."
    url: "https://www.mhprofessional.com/hematology-in-clinical-practice-fifth-edition-9780071626996-usa"
    accessed: "2026-06-05"
  - id: schechter-2008-hemoglobin
    type: peer-reviewed
    cite: "Schechter AN. Hemoglobin research and the origins of molecular medicine. Blood. 2008;112(10):3927-38."
    doi: "10.1182/blood-2008-04-078188"
    pmid: "18988877"
    url: "https://doi.org/10.1182/blood-2008-04-078188"
cross_links:
  - target: 01-human/07-system/cardiovascular-system
    relation: part-of
    note: "Erythrocytes are the dominant cellular component of blood, suspended in plasma and circulated by the cardiovascular system to deliver O₂ to every tissue."
  - target: 01-human/02-atomic/oxygen
    relation: modulates
    note: "Haemoglobin binds 4 O₂ molecules cooperatively (Hill coefficient ~2.7–3.0); each erythrocyte carries ~10⁹ O₂ molecules. At rest, ~25 trillion circulating erythrocytes collectively deliver ~250 mL O₂/min to tissues."
  - target: 01-human/05-tissue/bone-marrow
    relation: part-of
    note: "Erythrocytes are produced in red bone marrow via erythropoiesis, a process spanning ~7 days from BFU-E progenitor to reticulocyte egress; ~2 million new RBCs enter circulation every second."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: modulates
    note: "Erythrocytes deliver O₂ to cardiomyocytes via coronary circulation; the myocardium extracts ~70% of O₂ at rest — one of the highest extraction ratios in the body."
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "Approximately 25 trillion erythrocytes are present in the adult human body at any time, constituting ~70% of all human cells by number."
  - target: 01-human/03-molecular/hemoglobin
    relation: composed-of
    note: "Composed Of by Hemoglobin."
  - target: 01-human/03-molecular/erythropoietin
    relation: modulated-by
    note: "Modulated by Erythropoietin."
  - target: 01-human/02-atomic/iron
    relation: composed-of
    note: "Composed Of by Iron."
---

# Erythrocyte

## Overview

The erythrocyte (red blood cell, RBC) is the most abundant cell in the human body — approximately 25 trillion circulate in an adult — and the principal vehicle for respiratory gas transport. Despite its near-universal familiarity, the erythrocyte is among the most structurally and biochemically specialised cells in biology: terminally differentiated, devoid of nucleus and most organelles, built almost entirely around haemoglobin, and exquisitely engineered for deformability in capillaries as narrow as 3 µm.

Normal reference ranges: 4.5–5.5 × 10¹² cells/L (males), 4.0–5.0 × 10¹² cells/L (females). Haematocrit (packed cell volume): 40–52% males, 36–46% females. Mean corpuscular volume (MCV): 80–100 fL. The average adult contains ~5 litres of blood, of which ~45% is cellular (overwhelmingly erythrocytes).

Erythrocytes are produced in red bone marrow at a rate of ~2 million per second (~200 billion per day) and survive ~120 days before being cleared by splenic and hepatic macrophages. Production is tightly regulated by erythropoietin (EPO), a glycoprotein hormone synthesised primarily by peritubular interstitial cells of the renal cortex in response to hypoxia (HIF-2α → EPO transcription).

## Structure

**Shape and dimensions.** The mature erythrocyte is a biconcave disc, approximately 7.5–8.0 µm in diameter and 2.0 µm thick at the rim, 1.0 µm at the centre. The biconcave geometry maximises surface-area-to-volume ratio (~90 µm² for ~90 fL) to minimise diffusion distances for O₂ and CO₂ exchange, and confers elastic deformability enabling passage through capillaries 3–4 µm in diameter.

**Membrane.** The erythrocyte membrane consists of a lipid bilayer (outer leaflet: phosphatidylcholine + sphingomyelin; inner leaflet: phosphatidylethanolamine + phosphatidylserine, the latter asymmetry maintained by flippase ATP11C) anchored to a two-dimensional spectrin-actin cytoskeleton via ankyrin-1 and protein 4.1R. This composite structure is the basis of remarkable deformability while maintaining membrane integrity over 10⁵ circulatory passages. Lipid asymmetry collapse (phosphatidylserine externalisation) is the primary eat-me signal during senescence.

**Haemoglobin.** Each erythrocyte contains approximately 250–280 million haemoglobin A (HbA) tetramers (2α + 2β subunits). Each subunit contains one iron-protoporphyrin IX (haem) group coordinated by a proximal histidine (His F8), allowing reversible O₂ binding at the distal face. Cooperative O₂ binding (sigmoid dissociation curve; P₅₀ ≈ 26 mmHg) is driven by T-state (tense, deoxygenated) to R-state (relaxed, oxygenated) quaternary transitions. 2,3-Bisphosphoglycerate (2,3-BPG) binds the T-state cleft, stabilising the deoxygenated form and right-shifting the curve to facilitate O₂ unloading at tissues.

**Metabolism.** Without mitochondria, erythrocytes rely entirely on anaerobic glycolysis (Embden-Meyerhof pathway) for ATP production. ATP drives the Na⁺/K⁺-ATPase maintaining ionic homeostasis, Ca²⁺-ATPase preventing dehydration, and flippase maintaining membrane asymmetry. The pentose phosphate pathway (hexose monophosphate shunt) generates NADPH, which reduces glutathione via glutathione reductase, protecting haemoglobin against oxidative denaturation. G6PD deficiency (most common enzymopathy, >400 million people) compromises this protection.

## Function

**Oxygen transport.** Erythrocytes load O₂ in the pulmonary capillaries (PO₂ ~100 mmHg; haemoglobin ≥97% saturated) and unload it at tissues (PO₂ ~40 mmHg in venous blood; ~75% saturation). The resulting ~22% fractional release × 150 g Hb/L × 1.34 mL O₂/g Hb × 5 L/min cardiac output = ~250 mL O₂/min delivered at rest, rising to 3–4 L/min during maximal exercise. The myocardium extracts ~70% of delivered O₂ even at rest.

**Carbon dioxide transport.** ~70% of CO₂ is transported as bicarbonate (HCO₃⁻): erythrocyte carbonic anhydrase II catalyses CO₂ + H₂O → H₂CO₃ → H⁺ + HCO₃⁻ (>10,000-fold acceleration vs. uncatalysed rate). HCO₃⁻ is exchanged for Cl⁻ via band 3 (AE1/SLC4A1). ~23% binds N-terminal amino groups of globin chains as carbamino compounds. ~7% dissolves in plasma.

**Bohr and Haldane effects.** Rising tissue CO₂ lowers pH (H⁺ stabilises T-state) → right-shifts the O₂ dissociation curve (Bohr effect) → facilitates O₂ unloading. Deoxygenation increases CO₂ capacity of haemoglobin (Haldane effect) → facilitates CO₂ pickup at tissues. These are thermodynamic reciprocals of the same allosteric mechanism.

**Nitric oxide metabolism.** Erythrocytes are central regulators of vascular NO bioavailability. Oxyhaemoglobin scavenges free NO (NO + HbO₂ → metHb + NO₃⁻). S-nitrosylation of Hbβ-Cys93 in the lungs, followed by release at deoxygenation, may contribute to hypoxic vasodilation. SNO-Hb and allosteric control of RBC ATP release (via pannexin-1) provide erythrocyte-mediated vasomotor signalling.

## Lifecycle

**Erythropoiesis (bone marrow, ~7 days).**
1. Haematopoietic stem cell (HSC) → burst-forming unit erythroid (BFU-E) → colony-forming unit erythroid (CFU-E): EPO-dependent commitment.
2. CFU-E → proerythroblast → basophilic → polychromatic → orthochromatic erythroblast: progressive haemoglobin accumulation, nucleus condensation, organelle autophagy.
3. Orthochromatic erythroblast enucleates (~24 hours; actin-myosin contractile ring expels pyknotic nucleus as a pyknosome, engulfed by macrophage nurse cells in erythroblastic islands).
4. Reticulocyte: residual ribosomes, mitochondria; finishes haemoglobin synthesis over 1–2 days in marrow sinusoids, then enters bloodstream.
5. Reticulocyte matures to definitive erythrocyte within ~24 hours of entering circulation (remaining organelles removed by autophagy).

**Circulation (120 days).** Erythrocytes traverse ~300 km of vasculature, withstanding repetitive mechanical deformation, osmotic stress, and oxidative challenge. Senescence markers accumulate: band 3 oxidation → clustering → IgG binding → complement activation → phagocytosis by splenic red-pulp macrophages (~90%) and hepatic Kupffer cells (~10%).

**Clearance.** Macrophages recognise senescent RBCs via phosphatidylserine exposure, band-3 neoantigens, and CD47 (don't-eat-me signal) downregulation. Iron from haem is recycled via haem oxygenase 1 (HMOX1) → biliverdin → bilirubin (conjugated in liver), globin chains are proteolysed, and iron (Fe²⁺) is exported by ferroportin 1 for re-use in new erythropoiesis.

## Connections

- **Upstream regulators:** EPO (renal peritubular cells; HIF-2α-driven under hypoxia); SCF (c-Kit ligand, early progenitor survival); GATA-1/KLF1 (master transcription factors of erythroid differentiation); androgen → enhanced EPO sensitivity (explains sex difference in haematocrit); altitude/hypoxia → chronic EPO elevation → polycythaemia.
- **Downstream physiological effects:** Tissue oxygenation; CO₂ removal; NO and vascular tone modulation; haemostasis (erythrocytes contribute to platelet activation and thrombus formation at high shear); acid-base buffering (HbA as an intracellular buffer, pKa ~6.8).
- **Pathological associations:** Anaemia (iron-deficiency, B12/folate deficiency, haemolytic, aplastic); sickle-cell disease (HbS β-Glu6Val mutation → polymerisation under hypoxia → vaso-occlusion); thalassaemia (α or β globin chain imbalance); hereditary spherocytosis (spectrin/ankyrin mutations); malaria (Plasmodium falciparum obligate intraerythrocytic parasite exploiting host haemoglobin as nutrient source); polycythaemia vera (JAK2 V617F mutation → EPO-independent RBC overproduction).

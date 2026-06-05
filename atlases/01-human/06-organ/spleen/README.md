---
schema: human-scale-entry/v1
id: spleen
name: Spleen
atlas: 01-human
scale: 06-organ
status: draft
last_reviewed: 2026-06-05
summary: "Largest lymphoid organ (~150 g). Red pulp: filters aged/damaged erythrocytes and sequesters platelets. White pulp: PALS (T cell zone) + follicles (B cell zone) — adaptive immune responses to blood-borne antigens. Backup erythropoiesis in chronic anaemia."
aliases: ["splen", "lien"]
sources:
  - id: mebius-2005-spleen-structure
    type: peer-reviewed
    cite: "Mebius RE, Kraal G. Structure and function of the spleen. Nat Rev Immunol. 2005;5(8):606-616."
    doi: "10.1038/nri1669"
    pmid: "16056254"
    url: "https://doi.org/10.1038/nri1669"
  - id: cesta-2006-spleen-anatomy
    type: peer-reviewed
    cite: "Cesta MF. Normal structure, function, and histology of the spleen. Toxicol Pathol. 2006;34(5):455-465."
    doi: "10.1080/01926230600867743"
    pmid: "17067939"
    url: "https://doi.org/10.1080/01926230600867743"
  - id: weiskopf-2019-spleen-trauma
    type: peer-reviewed
    cite: "Weiskopf RB, Viele MK, Feiner J, et al. Human cardiovascular and metabolic response to acute, severe isovolemic anemia. JAMA. 1998;279(3):217-221."
    doi: "10.1001/jama.279.3.217"
    pmid: "9438742"
    url: "https://doi.org/10.1001/jama.279.3.217"
  - id: theml-2004-spleen-textbook
    type: textbook
    cite: "Theml H, Diem H, Haferlach T. Color Atlas of Hematology. Thieme; 2004. Chapter: Spleen."
    url: "https://www.thieme.com/books-main/hematology/product/444-color-atlas-of-hematology"
    accessed: "2026-06-05"
  - id: bronte-2005-spleen-immunity
    type: peer-reviewed
    cite: "Bronte V, Pittet MJ. The spleen in local and systemic regulation of immunity. Immunity. 2013;39(5):806-818."
    doi: "10.1016/j.immuni.2013.10.010"
    pmid: "24238338"
    url: "https://doi.org/10.1016/j.immuni.2013.10.010"
  - id: theilacker-2016-asplenia
    type: peer-reviewed
    cite: "Theilacker C, Ludewig K, Serr A, et al. Overwhelming postsplenectomy infection: a prospective multicenter cohort study. Clin Infect Dis. 2016;62(7):871-878."
    doi: "10.1093/cid/ciw013"
    pmid: "26797211"
    url: "https://doi.org/10.1093/cid/ciw013"
cross_links:
  - target: 01-human/04-cellular/macrophage
    relation: contains
    note: "Splenic red pulp macrophages phagocytose senescent erythrocytes, recycling haemoglobin iron via ferritin; marginal zone macrophages clear encapsulated bacteria and blood-borne debris."
  - target: 01-human/04-cellular/b-cell
    relation: contains
    note: "Splenic follicles contain B cells that mount T-dependent (germinal centre) and T-independent responses to blood-borne antigens; marginal zone B cells provide rapid T-independent IgM responses."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: contains
    note: "The spleen contains a resident NK cell population in red pulp and marginal zone providing innate surveillance against blood-borne pathogens and malignant cells."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "The spleen is the largest secondary lymphoid organ; it orchestrates adaptive immune responses to blood-borne antigens via marginal zone B cells, follicular T/B interactions, and DC-T cell crosstalk."
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "The spleen is a fist-sized lymphoid organ in the left upper quadrant under the 9th–11th ribs; it weighs ~150 g and lies between the stomach and left kidney."
taxonomy:
  uberon: "UBERON:0002106"
  fma: "FMA:7196"
---

# Spleen

## Overview

The spleen is the largest secondary lymphoid organ in the human body, weighing approximately 100–200 g (mean ~150 g) in adults and measuring 11–12 cm in the longest axis. It lies in the left upper quadrant of the abdominal cavity, tucked beneath the 9th–11th ribs, between the fundus of the stomach medially and the left kidney and left adrenal posteromedially. Its distinctive purplish-red colour reflects its high content of blood — at any moment it contains roughly 200–350 mL, or about 4–6% of total blood volume [^mebius-2005-spleen-structure].

The spleen serves three major physiological functions:

1. **Filtration of blood:** Aged, damaged, or parasitised erythrocytes are selectively removed by the red pulp, maintaining RBC quality and recycling iron. The mechanical sieving occurs through inter-endothelial slits in the splenic sinuses (~2–3 μm wide), which RBCs must deform to cross — senescent RBCs with reduced deformability are trapped and phagocytosed.

2. **Adaptive immune responses to blood-borne antigens:** The white pulp contains organised T and B cell zones that respond rapidly to antigens arriving from the bloodstream without requiring lymphatic drainage. The splenic marginal zone is a unique niche for responses to thymus-independent antigens including polysaccharide capsules of encapsulated bacteria — this explains why asplenic individuals are profoundly susceptible to *Streptococcus pneumoniae*, *Haemophilus influenzae*, and *Neisseria meningitidis*.

3. **Haematopoietic reserve:** In foetal life, the spleen is a major haematopoietic organ. In healthy adults this activity is suppressed, but in chronic haemolytic anaemia, thalassaemia, myelofibrosis, and other haematological conditions it can re-emerge as **extramedullary haematopoiesis (EMH)**, causing massive splenomegaly [^theml-2004-spleen-textbook].

## Structure

### Gross Anatomy

The spleen is ovoid, with a convex diaphragmatic surface and a concave visceral surface that carries the **splenic hilum** — the entry point for the splenic artery (a branch of the coeliac trunk) and exit point for the splenic vein (which joins the superior mesenteric vein to form the portal vein). The spleen is entirely covered by visceral peritoneum except at the hilum, and is held in place by the **gastrosplenic ligament** (to the greater curvature of the stomach) and the **splenorenal ligament** (to the left kidney). The latter contains the tail of the pancreas and splenic vessels.

The splenic capsule is thin (1–2 mm), composed of dense connective tissue with smooth muscle fibres and abundant elastic fibres. Contraction of the capsule (splenic autotransfusion) during exercise or haemorrhage can release 200–300 mL of blood into the circulation. In contrast to other species (horse, dog), the human spleen capsule is relatively thin and its contractile contribution to exercise haemoconcentration is modest.

### Microscopic Structure: Red Pulp and White Pulp

The splenic parenchyma is divided into two functionally distinct compartments [^cesta-2006-spleen-anatomy]:

**White pulp** (~20% of volume): lymphoid tissue organised around the central artery (a branch of the trabecular artery). It consists of:
- **Periarteriolar lymphoid sheath (PALS):** T cell zone wrapping the central artery; contains CD4⁺ and CD8⁺ T cells plus dendritic cells. DCs in the PALS capture blood-borne antigens and present them to circulating naïve T cells.
- **Primary follicles:** mantle of IgD⁺/IgM⁺ naive B cells.
- **Secondary follicles (germinal centres):** formed after antigen encounter; site of somatic hypermutation, affinity maturation, and class switching. Produce long-lived plasma cells and memory B cells.
- **Marginal zone:** the interface between white and red pulp; contains marginal zone B cells (IgM^hi, CD21^hi, specialised for T-independent responses to polysaccharides), marginal zone macrophages (express MARCO, SIGNR1, MOMA-2), and metallophilic marginal zone macrophages. This zone is the first to intercept blood-borne antigens and particulates.

**Red pulp** (~80% of volume): functions as a blood filter. Contains:
- **Splenic cords (of Billroth):** loose reticular stroma populated by **red pulp macrophages** (CD68⁺, F4/80⁺, Tim4⁺ in mice; VCAM-1⁺ in humans). These macrophages phagocytose senescent RBCs (~2 × 10¹¹ per day system-wide), extracting haemoglobin for iron recycling via HO-1 and ferritin.
- **Splenic sinuses:** wide-bore (20–40 μm) vascular channels lined by elongated endothelial cells running parallel to the axis, with discontinuous basement membrane and inter-endothelial slits. RBCs traverse these slits, with deformability-dependent retention and phagocytosis of non-compliant cells.

**Circulation pattern:** Blood entering via the splenic artery follows an open (non-sinusoidal) route in humans — it flows from trabecular arteries → central arteries → penicillar arteries → directly into the splenic cords, then "percolates" through the reticular meshwork before re-entering the circulation via the splenic sinuses. This slow passage (transit time ~1 min vs. <1 s in closed circulation) maximises contact with red pulp macrophages [^mebius-2005-spleen-structure].

**Platelet reservoir:** The spleen sequesters approximately 30–40% of the platelet pool at rest. In pathological states (splenomegaly), up to 90% of platelets may be sequestered, causing thrombocytopenia even when platelet production is normal.

## Function

### Erythrocyte Quality Control

Every circulating RBC makes ~1,000 passages through the splenic microcirculation over its 120-day lifespan. As RBCs age, they lose membrane surface area via vesiculation, accumulate oxidatively damaged haemoglobin (haemichromes), and expose phosphatidylserine (PS) on the outer leaflet. These changes reduce deformability and generate "eat-me" signals (PS, band 3 clustering recognised by anti-band-3 IgG, and complement C3b deposition) that trigger phagocytosis by red pulp macrophages.

Iron recycling: Phagocytosed haemoglobin → haem oxygenase-1 (HO-1) degrades haem → Fe²⁺ released → stored as ferritin → exported via ferroportin → bound to transferrin → recycled for erythropoiesis. The spleen processes roughly 0.3 g of iron per day in this manner.

Heinz body removal: Oxidatively denatured, insoluble haemoglobin precipitates (Heinz bodies) adhere to the RBC membrane; the spleen can surgically "pit" them out (removing the inclusion while releasing an intact albeit surface-area-reduced cell) — a process visible as cup cells or bite cells on blood smear.

### Immunity to Blood-Borne Antigens

The spleen is uniquely equipped for immunity to antigens that enter the bloodstream directly (bypassing mucosal or skin barriers). Key mechanisms [^bronte-2005-spleen-immunity]:

**T-independent (TI) responses:** Polysaccharide antigens from encapsulated bacteria cross-link BCRs on marginal zone B cells without T cell help, triggering rapid IgM production (within 3–5 days). This is the critical first-line defence against pneumococcal and meningococcal bacteraemia — the reason asplenic patients require vaccination and antibiotic prophylaxis.

**T-dependent (TD) responses:** Protein antigens are captured by marginal zone macrophages and DCs, transported to the PALS and follicles, where DC–T cell interaction → Tfh cell differentiation → germinal centre formation → affinity maturation → IgG/IgA class switching → long-lived plasma cells migrating to bone marrow.

**NK cell surveillance:** Splenic NK cells (CD56^dim CD16⁺) provide innate cytotoxicity against virally infected and malignant cells entering the bloodstream. The spleen is a major reservoir of "ready-to-kill" NK cells that do not require lymph node homing.

### Extramedullary Haematopoiesis

When bone marrow output is insufficient (myelofibrosis, severe haemolytic anaemia, thalassaemia major, infiltrative diseases), haematopoietic stem cells home to the spleen and resume production of all blood lineages. The result is massive splenomegaly (spleen may reach 4 kg in myelofibrosis). Splenic EMH is detectable by the presence of all blood cell precursors in splenic biopsy or by the characteristic "leukoerythroblastic" blood film (teardrops, nucleated RBCs, immature myeloid cells).

## Connections

- **Contains → [Macrophage](../../04-cellular/macrophage/README.md):** red pulp and marginal zone macrophages are the dominant cell type for filtration and innate immunity.
- **Contains → [B Cell](../../04-cellular/b-cell/README.md):** follicular and marginal zone B cells drive humoral responses to blood-borne antigens.
- **Contains → [NK Cell](../../04-cellular/natural-killer-cell/README.md):** resident NK cells provide innate cytotoxicity in the red pulp.
- **Modulates → [Immune System](../../07-system/immune-system/README.md):** as the largest secondary lymphoid organ, the spleen coordinates blood-borne adaptive immunity.
- **Part of → [Human Body](../../08-whole-body/human-body/README.md):** left-upper-quadrant organ bridging haematopoietic, immune, and circulatory systems.

## Pathology

### Splenomegaly

Enlargement of the spleen (>12 cm, >400 g) is a sign of multiple underlying conditions rather than a diagnosis in itself. Causes classified by mechanism:

| Mechanism | Examples |
|:---|:---|
| **Increased workload (filtration)** | Hereditary spherocytosis, sickle cell disease, thalassaemia, autoimmune haemolytic anaemia |
| **Congestion (portal hypertension)** | Liver cirrhosis, Budd-Chiari syndrome, portal vein thrombosis, right heart failure |
| **Infiltration** | Myelofibrosis, CML, lymphoma, Gaucher disease, amyloidosis |
| **Infection/inflammation** | Malaria (classic cause of "big spleen" in endemic areas), EBV mononucleosis, visceral leishmaniasis, endocarditis, sarcoidosis |
| **Haematopoietic** | Extramedullary haematopoiesis (myeloproliferative neoplasms) |

**Hypersplenism** = splenomegaly + destruction of ≥1 blood cell lines (pancytopenia, anaemia, thrombocytopenia). Treated by addressing the underlying cause; splenectomy if refractory.

### Splenic Rupture

The spleen is the most commonly injured intra-abdominal organ in blunt trauma (motor vehicle accidents). Pathological splenomegaly (especially EBV mononucleosis — risk of spontaneous rupture even with minor trauma) dramatically increases rupture risk. Management: haemodynamically stable → non-operative (splenic artery embolisation if needed); unstable → splenectomy [^weiskopf-2019-spleen-trauma].

### Asplenia and Overwhelming Post-Splenectomy Infection (OPSI)

Loss of splenic function (anatomical after splenectomy, or functional in sickle cell disease after repeated infarctions) creates lifelong risk of OPSI — a fulminant bacteraemia with rapid progression to septic shock. Causative organisms predominantly encapsulated bacteria: *S. pneumoniae* (50–90% of cases), *H. influenzae* type b, *N. meningitidis*. Case fatality rate of OPSI is 50–70% even with treatment [^theilacker-2016-asplenia]. Prevention: vaccination (pneumococcal, Hib, meningococcal) before or immediately after splenectomy; lifelong penicillin prophylaxis in children; antibiotic standby ("rescue") regimen.

### Splenic Infarction

Occlusion of splenic artery branches by emboli (atrial fibrillation, endocarditis), thrombosis, or sickle RBCs causes focal splenic infarcts. Presents with acute left upper quadrant pain and peritoneal signs. CT with contrast is diagnostic. Massive infarction can lead to autosplenectomy (complete fibrosis/atrophy) as seen in sickle cell disease by adolescence.

### Splenic Lymphoma

The spleen is frequently involved in lymphoma, either as primary splenic lymphoma (rare, ~1% of lymphomas) or secondary involvement. Marginal zone lymphoma of the spleen (SMZL) presents as massive splenomegaly, lymphocytosis, and villous lymphocytes on blood smear; involves the marginal zone B cell compartment. Splenic involvement in diffuse large B cell lymphoma (DLBCL), Hodgkin lymphoma, CLL, and hairy cell leukaemia (HCL — pathognomonic dry-tap on marrow aspiration, BRAF V600E mutation) is common.

### Splenic Sequestration Crisis (Sickle Cell Disease)

Acute massive splenic sequestration in young children with sickle cell disease: sudden trapping of large volumes of blood in the spleen → acute severe anaemia (Hb drop >2 g/dL) + splenomegaly + hypovolaemic shock. Life-threatening emergency requiring urgent transfusion. Recurrence rate ~50%; long-term management: splenectomy or chronic transfusion/hydroxyurea.

[^mebius-2005-spleen-structure]: Mebius RE, Kraal G. Structure and function of the spleen. *Nat Rev Immunol.* 2005;5(8):606-616. [doi:10.1038/nri1669](https://doi.org/10.1038/nri1669) · [PubMed 16056254](https://pubmed.ncbi.nlm.nih.gov/16056254/)
[^cesta-2006-spleen-anatomy]: Cesta MF. Normal structure, function, and histology of the spleen. *Toxicol Pathol.* 2006;34(5):455-465. [doi:10.1080/01926230600867743](https://doi.org/10.1080/01926230600867743) · [PubMed 17067939](https://pubmed.ncbi.nlm.nih.gov/17067939/)
[^weiskopf-2019-spleen-trauma]: Weiskopf RB et al. Human cardiovascular and metabolic response to acute, severe isovolemic anemia. *JAMA.* 1998;279(3):217-221. [doi:10.1001/jama.279.3.217](https://doi.org/10.1001/jama.279.3.217) · [PubMed 9438742](https://pubmed.ncbi.nlm.nih.gov/9438742/)
[^theml-2004-spleen-textbook]: Theml H, Diem H, Haferlach T. *Color Atlas of Hematology.* Thieme; 2004.
[^bronte-2005-spleen-immunity]: Bronte V, Pittet MJ. The spleen in local and systemic regulation of immunity. *Immunity.* 2013;39(5):806-818. [doi:10.1016/j.immuni.2013.10.010](https://doi.org/10.1016/j.immuni.2013.10.010) · [PubMed 24238338](https://pubmed.ncbi.nlm.nih.gov/24238338/)
[^theilacker-2016-asplenia]: Theilacker C et al. Overwhelming postsplenectomy infection: a prospective multicenter cohort study. *Clin Infect Dis.* 2016;62(7):871-878. [doi:10.1093/cid/ciw013](https://doi.org/10.1093/cid/ciw013) · [PubMed 26797211](https://pubmed.ncbi.nlm.nih.gov/26797211/)

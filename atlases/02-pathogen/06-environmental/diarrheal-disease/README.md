---
schema: pathogen-entry/v1
id: diarrheal-disease
name: Diarrheal Disease
atlas: 02-pathogen
scale: 06-environmental
status: draft
last_reviewed: 2026-06-06
summary: "Syndrome of ≥3 loose/liquid stools per day; second leading cause of death in children <5 globally. ~1.7 billion cases/year; ~443,000 deaths/year (WHO). Dehydration is the main mortality mechanism; ORS + zinc is cornerstone management."
aliases: ["diarrhoea", "gastroenteritis", "infectious diarrhea", "acute diarrhea", "cholera", "dysentery", "traveler's diarrhea"]
sources:
  - id: liu-2016-child-mortality
    type: peer-reviewed
    cite: "Liu L, Oza S, Hogan D, et al. Global, regional, and national causes of under-5 mortality in 2000-15: an updated systematic analysis with implications for the Sustainable Development Goals. Lancet. 2016;388(10063):3027-3035."
    doi: "10.1016/S0140-6736(16)31593-8"
    pmid: "27839855"
    url: "https://doi.org/10.1016/S0140-6736(16)31593-8"
  - id: guerrant-2012-diarrhea-review
    type: peer-reviewed
    cite: "Guerrant RL, Oriá RB, Moore SR, Oriá MO, Lima AA. Malnutrition as an enteric infectious disease with long-term effects on child development. Nutr Rev. 2008;66(9):487-505."
    doi: "10.1111/j.1753-4887.2008.00082.x"
    pmid: "18752473"
    url: "https://doi.org/10.1111/j.1753-4887.2008.00082.x"
  - id: who-diarrhea-factsheet
    type: regulatory
    cite: "World Health Organization. Diarrhoeal disease. WHO Fact Sheet. 2017."
    url: "https://www.who.int/news-room/fact-sheets/detail/diarrhoeal-disease"
cross_links:
  - target: 02-pathogen/02-bacteria/escherichia-coli
    relation: targets
    note: "Enterotoxigenic E. coli (ETEC) is a leading cause of traveler's diarrhea and diarrhea in children in developing countries; secretes heat-labile (LT) and heat-stable (ST) toxins that activate cAMP/cGMP → chloride secretion → watery diarrhea."
  - target: 02-pathogen/01-viruses/rotavirus
    relation: targets
    note: "Rotavirus is the leading cause of severe dehydrating diarrhea in children <5 worldwide; ~128,000 deaths/year; infects villus tip enterocytes; Rotarix and RotaTeq vaccines are highly effective."
  - target: 02-pathogen/01-viruses/norovirus
    relation: targets
    note: "Norovirus is the leading cause of epidemic non-bacterial gastroenteritis globally (~685 million cases/year); infects jejunal epithelium via HBGA; highly infectious (ID50 ~18 particles); no approved vaccine."
  - target: 01-human/03-molecular/norovirus-vp1
    relation: targets
    note: "Norovirus VP1 P2 subdomain binds HBGA H-type antigens on jejunal enterocytes → attachment and villus blunting; norovirus causes ~685 million diarrhea cases/year; VLP (TAK-214) and mRNA-1403 vaccines in Phase 3 trials target the leading cause of epidemic foodborne diarrhea."
  - target: 01-human/07-system/gut-microbiome
    relation: damages
    note: "Enteric pathogens (Salmonella, C. diff, rotavirus) disrupt gut microbiome via invasion, antimicrobial induction, and diarrhea-driven washout; post-diarrheal dysbiosis delays mucosal recovery; FMT (fecal microbiota transplant) is curative for recurrent C. difficile infection."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: damages
    note: "All major enteric pathogens target intestinal epithelium: rotavirus lyses villus enterocytes; norovirus blunts villi; Shigella/Salmonella invade M cells via T3SS; ETEC/cholera toxins disrupt CFTR/NHE → secretory diarrhea; mucosal barrier integrity is the primary host defense."
---

# Diarrheal Disease

## Overview

**Diarrheal disease** is defined by the World Health Organization as the passage of **three or more loose or liquid stools per day**, or more frequently than normal for the individual. It is a **clinical syndrome** caused by a diverse array of pathogens — bacteria, viruses, and parasites — that share the common endpoint of disrupting intestinal fluid and electrolyte homeostasis.

Diarrheal disease remains one of the leading causes of global morbidity and mortality:
- **~1.7 billion** cases of diarrhea occur globally each year [^who-diarrhea-factsheet]
- **~443,000 deaths/year** (2015 estimate), predominantly in children under 5 years old
- **Second leading cause of death** in children <5 globally after pneumonia; responsible for ~8–9% of under-5 deaths [^liu-2016-child-mortality]
- High burden in sub-Saharan Africa and South Asia; closely linked to inadequate sanitation (WASH — water, sanitation, hygiene)

The principal mechanism of death is **dehydration** — rapid loss of water and electrolytes from watery stool, particularly dangerous in young children whose total body water turnover is high relative to their circulating volume. **Oral rehydration salts (ORS) + zinc** — simple, cheap interventions — can prevent the vast majority of diarrhea deaths if administered promptly.

## Structure

### Classification by Duration

| Type | Duration | Definition |
|:---|:---|:---|
| **Acute** | < 14 days | Most common; self-limiting in immunocompetent |
| **Persistent** | 14–29 days | Often indicates parasitic infection or immune compromise |
| **Chronic** | ≥ 30 days | Usually non-infectious etiology (IBD, IBS, malabsorption) or parasitic (Giardia, cryptosporidium) |

### Classification by Mechanism

| Mechanism | Pathogens | Features |
|:---|:---|:---|
| **Secretory (watery)** | Cholera, ETEC, rotavirus, norovirus | Large volume, non-bloody; due to enterotoxin/viral activation of cAMP/cGMP/Cl⁻ secretion; osmotic gap absent |
| **Inflammatory (dysenteric/bloody)** | Shigella, EHEC O157:H7, *Campylobacter*, *Entamoeba histolytica* | Small volume, bloody mucus; fever; fecal leukocytes; due to mucosal invasion and cytotoxin damage |
| **Osmotic** | Giardia, *Cryptosporidium*, lactase deficiency | Watery; stops with fasting; malabsorption of nutrients; osmotic gap present |
| **Motility-altered** | Diabetic autonomic neuropathy, hyperthyroidism | Non-infectious; altered transit time |

### Major Causative Agents by Syndrome

**Watery diarrhea:**
- *Vibrio cholerae* O1/O139 (cholera): CT toxin → massive rice-water stool (10–20 L/day); CFR <1% with ORS, up to 50% without
- ETEC: heat-labile (LT) + heat-stable (ST) toxins; #1 cause of traveler's diarrhea
- Rotavirus: #1 cause of severe pediatric diarrhea; vaccine-preventable
- Norovirus: #1 cause of foodborne illness globally
- *Cryptosporidium*: prolonged watery diarrhea; particularly severe in HIV/AIDS (CD4 <100 cells/μL)

**Bloody diarrhea (dysentery):**
- *Shigella* spp.: Shiga toxin + invasin; bacillary dysentery; low infectious dose (~10 organisms)
- EHEC O157:H7: Shiga toxin 2 → hemorrhagic colitis → hemolytic uremic syndrome (HUS)
- *Campylobacter jejuni*: most common bacterial foodborne pathogen in high-income countries; bloody diarrhea; Guillain-Barré syndrome (molecular mimicry)
- *Entamoeba histolytica*: liver abscess complication; distinguish from non-pathogenic *E. dispar*

## Infection Mechanism

### Common Pathogenic Mechanisms

#### Toxin-Mediated Secretory Diarrhea

The most dangerous dehydrating diarrheas are mediated by **enterotoxins** that activate secretory pathways in enterocytes without cell death:

- **Cholera toxin (CT)** and **ETEC heat-labile toxin (LT)**: ADP-ribosylation of Gsα → constitutive adenylyl cyclase activation → ↑cAMP → protein kinase A → CFTR Cl⁻ channel opening + NHE (Na⁺/H⁺ exchanger) inhibition → massive Cl⁻ and Na⁺ efflux → osmotic water loss. Net: up to 20 L/day rice-water stool in cholera.
- **ST (heat-stable toxin, ETEC)**: Binds GC-C receptor → ↑cGMP → PKG-II → CFTR activation; same net effect as LT but via cGMP rather than cAMP.
- **Rotavirus NSP4**: Viral enterotoxin; binds enterocyte surface → intracellular Ca²⁺ ↑ → Cl⁻ secretion + brush border enzyme loss → osmotic component.

#### Mucosal Invasion and Cytotoxicity

Dysenteric diarrheas involve pathogen invasion of the colonic mucosa:
- **Shigella**: Type III secretion system (T3SS) injects IpaB/C into M cells → actin polymerization → invasion → intracellular spread via ActA-like IcsA; Shiga toxin inhibits 28S rRNA → protein synthesis stop → cell death.
- **EHEC O157**: Attachment-and-effacement lesion (T3SS LEE island) + Shiga toxin 2 (Stx2) delivered via phage → absorbed into circulation → renal endothelial Gb3 receptor binding → HUS.
- *Campylobacter*: CiaB effector → cytoskeletal disruption; CDT toxin (cytolethal distending toxin) → DNA damage.

#### Viral Enterocyte Destruction

- **Rotavirus**: Infects villus tip enterocytes → cell lysis → loss of absorptive surface → malabsorption; NSP4 also acts as a toxin via Ca²⁺ dysregulation.
- **Norovirus**: Infects differentiated villus enterocytes of the proximal small intestine → villus blunting → malabsorption + secretion; recovers within 2–3 days.

### Fecal-Oral Transmission

Almost all enteric pathogens are transmitted via the **fecal-oral route**:
- Contaminated water supply (cholera, typhoid, *Cryptosporidium*, norovirus)
- Contaminated food (ETEC, Salmonella, *Campylobacter*, EHEC, norovirus)
- Person-to-person contact (norovirus in nursing homes, Shigella in daycare centers)
- Sexual transmission (amoebic dysentery, *Shigella* in MSM)

**WASH (Water, Sanitation, Hygiene)** interventions — safe drinking water, latrines, handwashing with soap — are the most impactful long-term prevention strategy, estimated to reduce diarrheal disease incidence by 25–40%.

## Host Interactions

### Immune Response to Enteric Pathogens

The gut immune system maintains a delicate balance between tolerance (to commensal bacteria) and immunity (against pathogens):

- **Innate**: Mucus layer (MUC2 mucin), tight junctions, Paneth cell defensins, IgA; pattern recognition by toll-like receptors (TLR4-LPS, TLR5-flagellin) in lamina propria macrophages → IL-8, TNF-α → neutrophil recruitment.
- **M cell entry**: Some pathogens (Shigella, *Salmonella*, *E. coli*) exploit M cells (specialized FAE epithelium overlying Peyer's patches) for mucosal invasion.
- **Adaptive**: Secretory IgA (SIgA) from plasma cells in the lamina propria → luminal neutralization; CD4+ Th17 cells produce IL-17 → antimicrobial peptide induction; CD8+ CTLs against virally infected enterocytes.
- **Immunological memory**: Natural rotavirus infection generates protective immunity; basis for Rotarix/RotaTeq live-attenuated oral vaccines (>90% efficacy against severe disease).

### Malnutrition-Diarrhea Cycle

Diarrheal disease and malnutrition are mutually reinforcing [^guerrant-2012-diarrhea-review]:
- Diarrhea → nutrient malabsorption, appetite loss, catabolism → wasting and stunting
- Malnutrition → impaired mucosal immunity (IgA↓, villus atrophy), altered gut microbiome → increased susceptibility to diarrheal pathogens and prolonged illness
- This cycle accounts for much of the long-term neurodevelopmental harm associated with enteric infections in low-income settings (Environmental Enteric Dysfunction, EED)

## Connections

- `targets` → **[Escherichia coli](../../02-bacteria/escherichia-coli/README.md)** — ETEC causes watery traveler's diarrhea via LT/ST toxins; EHEC O157:H7 causes hemorrhagic colitis and hemolytic uremic syndrome via Shiga toxin 2
- `targets` → **[Rotavirus](../../01-viruses/rotavirus/README.md)** — leading cause of severe pediatric dehydrating diarrhea; ~128,000 deaths/year; vaccine-preventable with Rotarix/RotaTeq
- `targets` → **[Norovirus](../../01-viruses/norovirus/README.md)** — leading cause of epidemic foodborne diarrhea globally; ~685 million cases/year; no vaccine or antiviral approved
- `targets` → **[Norovirus VP1](../../../01-human/03-molecular/norovirus-vp1/README.md)** — VP1 P2 HBGA binding mediates intestinal attachment and villus blunting; norovirus VP1 antigenic drift (GII.4 variants) drives successive pandemic waves; VLP (TAK-214) and mRNA-1403 vaccines target VP1 to prevent the leading cause of epidemic foodborne diarrhea.
- `damages` → **[Gut Microbiome](../../../01-human/07-system/gut-microbiome/README.md)** — enteric pathogens disrupt gut microbiome via invasion, antimicrobial peptide induction, and diarrhea-driven washout; post-diarrheal dysbiosis delays mucosal recovery; FMT is curative for recurrent C. difficile colitis.
- `damages` → **[Intestinal Epithelium](../../../01-human/05-tissue/intestinal-epithelium/README.md)** — rotavirus lyses villus enterocytes → malabsorption; norovirus blunts villi; Shigella/Salmonella invade M cells via T3SS; ETEC/cholera toxins disrupt CFTR/NHE → secretory diarrhea; mucosal barrier integrity is the primary host defense.

## Pathology

### Clinical Assessment and Severity

| Assessment | Mild | Moderate | Severe |
|:---|:---|:---|:---|
| **Stool frequency** | < 4/day | 4–6/day | > 6/day |
| **Dehydration** | < 3% body weight loss | 3–9% body weight loss | > 9% body weight loss |
| **Signs** | Thirst | Sunken eyes, decreased skin turgor, dry mouth | Sunken fontanelle, absent tears, no urine, altered consciousness |
| **Management** | ORS at home | ORS under observation | IV fluids (Ringer's lactate) |

### Dehydration Pathophysiology

The critical pathophysiology of severe diarrhea is **isotonic dehydration** — loss of water and electrolytes (Na⁺, K⁺, Cl⁻, HCO₃⁻) in proportional amounts:

- Decreased plasma volume → reduced renal perfusion → pre-renal azotemia → metabolic acidosis (stool HCO₃⁻ loss + lactic acidosis from tissue hypoperfusion)
- Hypokalemia (stool K⁺ losses) → cardiac arrhythmia; particularly dangerous in malnourished children
- Hyponatremia (if water > salt replacement) → cerebral edema; hypernatremia (if water < salt loss) → neurological injury

**ORS composition (WHO standard)**: Na⁺ 75 mmol/L, K⁺ 20 mmol/L, Cl⁻ 65 mmol/L, citrate 10 mmol/L, glucose 75 mmol/L, osmolarity 245 mOsm/L. Glucose co-transport (SGLT1) drives Na⁺ and water absorption even in the presence of active secretion — the physiological basis of ORS.

**Zinc supplementation** (10–20 mg/day × 10–14 days in children <5) reduces duration and severity of diarrhea by ~25% and prevents recurrence for 2–3 months; WHO/UNICEF recommendation since 2004.

### Complications

| Complication | Pathogen | Mechanism |
|:---|:---|:---|
| **Hemolytic Uremic Syndrome (HUS)** | EHEC O157:H7 | Stx2 → renal endothelial injury → microangiopathic hemolytic anemia + thrombocytopenia + renal failure; 5–10% of O157 infections in children |
| **Reactive arthritis** | Salmonella, Shigella, Campylobacter, Yersinia | Post-infectious HLA-B27-associated joint inflammation |
| **Guillain-Barré Syndrome** | *Campylobacter jejuni* | Molecular mimicry: anti-Campylobacter lipooligosaccharide IgG cross-reacts with GM1 ganglioside on peripheral nerves |
| **Extraintestinal amebiasis** | *Entamoeba histolytica* | Hepatic abscess (via portal venous spread); pleuropulmonary, brain (rare) |
| **Toxic megacolon** | EHEC, Clostridioides difficile | Colonic dilation >6 cm; risk of perforation and sepsis; avoid antiperistaltic agents |

### Antimicrobial Treatment Indications

Most acute infectious diarrheas in immunocompetent adults are self-limiting; antibiotics are indicated in:
- **Shigellosis**: Fluoroquinolone (azithromycin if resistance); reduces severity and person-to-person spread
- **Cholera**: Doxycycline or azithromycin; reduces stool output and duration by ~50%
- **Traveler's diarrhea** (severe): Rifaximin, azithromycin, or fluoroquinolone (depending on region/resistance)
- **C. difficile**: Vancomycin (oral) or fidaxomicin; avoid antiperistaltics
- **EHEC O157:H7**: Antibiotics CONTRAINDICATED — may ↑Stx2 release and HUS risk

[^liu-2016-child-mortality]: Liu L et al. Global, regional, and national causes of under-5 mortality in 2000-15. *Lancet.* 2016;388(10063):3027-3035. [doi:10.1016/S0140-6736(16)31593-8](https://doi.org/10.1016/S0140-6736(16)31593-8) · [PubMed 27839855](https://pubmed.ncbi.nlm.nih.gov/27839855/)
[^guerrant-2012-diarrhea-review]: Guerrant RL et al. Malnutrition as an enteric infectious disease with long-term effects on child development. *Nutr Rev.* 2008;66(9):487-505. [doi:10.1111/j.1753-4887.2008.00082.x](https://doi.org/10.1111/j.1753-4887.2008.00082.x) · [PubMed 18752473](https://pubmed.ncbi.nlm.nih.gov/18752473/)
[^who-diarrhea-factsheet]: World Health Organization. Diarrhoeal disease. WHO Fact Sheet. 2017. [who.int](https://www.who.int/news-room/fact-sheets/detail/diarrhoeal-disease)

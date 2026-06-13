---
schema: human-scale-entry/v1
id: hereditary-pancreatitis
name: Hereditary Pancreatitis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Hereditary pancreatitis is caused by autosomal dominant PRSS1 gain-of-function mutations (R122H, N29I); recurrent acute pancreatitis from childhood; chronic pancreatitis with exocrine and endocrine insufficiency; ~40-fold elevated PDAC risk; analgesic-focused management."
aliases: ["hereditary pancreatitis", "hereditary chronic pancreatitis", "PRSS1 pancreatitis", "familial pancreatitis", "trypsinogen R122H pancreatitis", "hereditary pancreatitis PRSS1", "HP pancreatitis", "chronic hereditary pancreatitis", "pancreatitis hereditary syndrome"]
sources:
  - id: whitcomb-1996-prss1
    type: peer-reviewed
    cite: "Whitcomb DC, Gorry MC, Preston RA, et al. Hereditary pancreatitis is caused by a mutation in the cationic trypsinogen gene. Nat Genet. 1996;14(2):141-145."
    doi: "10.1038/ng1096-141"
    pmid: "8841182"
    url: "https://doi.org/10.1038/ng1096-141"
  - id: lowenfels-2001-hp-pdac
    type: peer-reviewed
    cite: "Lowenfels AB, Maisonneuve P, DiMagno EP, et al. Hereditary pancreatitis and the risk of pancreatic cancer. J Natl Cancer Inst. 2001;93(1):26-31."
    doi: "10.1093/jnci/93.1.26"
    pmid: "11136838"
    url: "https://doi.org/10.1093/jnci/93.1.26"
cross_links:
  - target: 01-human/03-molecular/prss1
    relation: connects-to
    note: "PRSS1 R122H and N29I gain-of-function mutations cause hereditary pancreatitis by preventing trypsin inactivation; autosomal dominant; onset childhood/early adulthood; recurrent acute → chronic pancreatitis → exocrine + endocrine insufficiency; ~40-fold elevated PDAC risk."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "PRSS1-hereditary pancreatitis confers ~40-fold PDAC risk; chronic pancreatic inflammation → acinar-ductal metaplasia → PanIN lesions → PDAC (same progression as sporadic); KRAS mutations are the initiating event in PDAC even in PRSS1-hereditary pancreatitis background."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Chronic pancreatitis (hereditary PRSS1 or sporadic) → TGF-β release from acinar cells and inflammatory macrophages → pancreatic stellate cell activation → collagen deposition → fibrosis → acinar cell loss → exocrine insufficiency → endocrine β-cell loss → CFRD-like diabetes."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "KRAS oncogenic mutations (G12D/V/R) drive PanIN and PDAC even in hereditary pancreatitis (PRSS1 mutation background); KRAS mutation is the initiating event; chronic trypsin-mediated inflammation → KRAS-susceptible acinar cells → transformation; KRAS is the primary PDAC oncogene."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Recurrent trypsin-driven autodigestion progressively destroys the pancreas → fibrosis, exocrine insufficiency (steatorrhea, PERT) and Type 3c diabetes; total pancreatectomy with islet autotransplantation (TPIAT) relieves refractory pain and eliminates the ~40-fold PDAC risk."
  - target: 01-human/03-molecular/cftr
    relation: connects-to
    note: "CFTR-driven ductal bicarbonate secretion raises luminal pH and flushes zymogens — one of the pancreas's defenses against premature trypsin activation; CFTR variants act as modifiers that co-contribute to hereditary pancreatitis alongside PRSS1 and SPINK1 mutations."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Progressive fibrotic loss of islet β-cells causes pancreatogenic (Type 3c) diabetes — brittle, with concurrent glucagon deficiency raising hypoglycemia risk; managed with carefully titrated low-dose insulin rather than sulfonylureas, distinguishing it from Type 1 and Type 2."
  - target: 01-human/07-system/cystic-fibrosis
    relation: connects-to
    note: "Hereditary pancreatitis and cystic fibrosis are the two major genetic pancreatic diseases: CFTR's ductal bicarbonate flush normally clears zymogens and blocks premature trypsin activation, so CFTR variants modify hereditary pancreatitis while CF destroys the exocrine pancreas."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Fibrosis is the endpoint of hereditary pancreatitis, and the pancreatic stellate cell is its fibroblast: recurrent trypsin injury and TGF-β turn these cells into collagen-secreting myofibroblasts that scar the gland — the same switch driving pancreatic-cancer desmoplasia."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Hereditary and alcoholic chronic pancreatitis share one fibrotic endpoint: a PRSS1 mutation resisting trypsin inactivation and chronic alcohol both trigger repeated acinar autodigestion, stellate-cell fibrosis, and exocrine/endocrine failure; smoking raises cancer risk."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Hereditary pancreatitis commonly ends in pancreatogenic (type 3c) diabetes: recurrent inflammation destroys the islets along with the exocrine pancreas, producing an insulin-deficient diabetes that is brittle (glucagon is also lost) and distinct from type 1 and type 2."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Hereditary pancreatitis cripples the digestive system: loss of exocrine acinar tissue causes pancreatic enzyme insufficiency with steatorrhea, malabsorption and weight loss needing lifelong enzyme replacement—while the destroyed gland also forfeits its insulin/glucagon function."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Hereditary pancreatitis impairs small-intestinal digestion: without pancreatic lipase, protease and amylase reaching the duodenum, fats, proteins and fat-soluble vitamins go unabsorbed, causing steatorrhea and deficiency—so enzyme replacement is timed to meals to restore uptake."
---

# Hereditary Pancreatitis

## Overview

**Hereditary pancreatitis (HP)** is a rare autosomal dominant condition caused primarily by germline gain-of-function mutations in **PRSS1** (cationic trypsinogen), most commonly **R122H** (~65-70% of HP families) and **N29I** (~20-25%), which prevent the normal autolytic self-inactivation of intrapancreatic trypsin. The result is recurrent episodes of acute pancreatitis beginning in childhood or early adulthood, progressive destruction of pancreatic parenchyma → chronic pancreatitis → exocrine pancreatic insufficiency (malabsorption, steatorrhea) and endocrine pancreatic insufficiency (pancreatogenic diabetes mellitus, Type 3c). The most feared complication is a **~40-fold increased lifetime risk of pancreatic ductal adenocarcinoma (PDAC)**, with cumulative PDAC risk estimated at ~40% by age 70 in Lowenfels et al.'s International HP Study Group cohort. HP was the first pancreatitis syndrome for which a molecular genetic cause was identified, by Whitcomb et al. in 1996. Prevalence is estimated at ~1-3 per 100,000; HP accounts for ~1% of all chronic pancreatitis cases in the Western world [^whitcomb-1996-prss1] [^lowenfels-2001-hp-pdac].

**Genetic causes of hereditary/familial pancreatitis:**

| Gene | Role | Inheritance | HP contribution |
|---|---|---|---|
| PRSS1 (R122H) | Cationic trypsinogen GOF — no autolysis | Autosomal dominant | ~65-70% of HP families |
| PRSS1 (N29I) | Cationic trypsinogen GOF — Ca²⁺ destabilization | Autosomal dominant | ~20-25% of HP families |
| SPINK1 (N34S) | Trypsin inhibitor LOF — modifier | Complex/recessive modifier | Co-contributor; ~1-2% population |
| CTRC (R254W, etc.) | Chymotrypsin C LOF — impaired trypsin clearance | Autosomal recessive modifier | Rare; amplifies other mutations |
| CFTR variants | Ductal fluid/pH dysfunction | Complex modifier | Co-contributor with PRSS1/SPINK1 |

## Structure

### Genetic basis of hereditary pancreatitis

**PRSS1 R122H (Arg122His) — dominant mechanism:**
- Arg122 is the autolysis site: wild-type trypsin cleaves the Arg122-Val123 bond → trypsin fragments → self-inactivation; this prevents persistent trypsin activity in the pancreas
- R122H: Arg→His substitution; trypsin cannot cleave His; autolysis abolished → once activated inside acinar cell, trypsin cannot self-destruct → chain activation of other zymogens → acinar cell autodigestion
- Penetrance of R122H: ~80% lifetime penetrance (vs 100% for most autosomal dominant conditions); modifiers (SPINK1, CFTR, alcohol, smoking, diet) influence phenotypic expression
- Anticipation: some families show earlier onset and more severe disease in successive generations (proposed mechanism: epigenetic modifier accumulation; not fully established)

**PRSS1 N29I (Asn29Ile) — Ca²⁺ destabilization:**
- Asn29 is part of the calcium-binding loop of trypsinogen; Ca²⁺ binding stabilizes trypsinogen in the inactive conformation
- N29I: disrupts Ca²⁺ coordination → lower calcium affinity → trypsinogen less stable → lower threshold for activation (spontaneous premature activation inside acinar cells at normal physiological calcium concentrations)
- Penetrance: somewhat lower than R122H (~65-70%); phenotype is clinically similar but can be milder
- Also associated with higher risk of exocrine insufficiency and diabetes compared to R122H in some cohort studies

**SPINK1 N34S — modifier allele:**
- SPINK1 encodes pancreatic secretory trypsin inhibitor (PSTI); inhibits ~20% of trypsin activity; a first-line buffer against premature trypsin activation
- N34S: found in ~1-2% of the European population; reduces SPINK1 mRNA stability → reduced inhibitor levels; alone not sufficient to cause pancreatitis (~5-10% lifetime risk with N34S alone, requiring additional environmental or genetic co-hits)
- In PRSS1-HP patients: SPINK1 N34S co-inheritance worsens phenotype (earlier onset, more severe chronic pancreatitis, higher PDAC risk)

### Pancreatic physiology and HP pathophysiology

**Normal protection against intrapancreatic trypsin activation:**
1. TAP peptide: blocks active site until enterokinase cleaves in duodenum
2. SPINK1: inhibits nascent premature trypsin in acinar cell and duct
3. CTRC: chymotrypsin C cleaves trypsinogen/trypsin at Leu81 and Arg122 → inactivation
4. Autolysis (Arg122): trypsin destroys itself
5. Alkaline pH: bicarbonate in pancreatic duct (CFTR-mediated) → high pH → trypsin less active

**HP pathophysiology:**
1. PRSS1 GOF → premature/persistent trypsin inside acinar cells
2. Trypsin activates: chymotrypsinogen → chymotrypsin, proelastase → elastase, phospholipase A2, procarboxypeptidase → all digestive enzymes activated inside the cell
3. Acinar cell autodigestion → necrosis → acute pancreatitis episode
4. Repeated acute episodes → persistent inflammation → macrophage infiltration → TGF-β release → pancreatic stellate cell activation → collagen deposition → pancreatic fibrosis
5. Fibrosis → loss of acinar cell mass → exocrine insufficiency; loss of islet β-cells → Type 3c diabetes
6. Chronic inflammation + oxidative stress → genomic instability in ductal epithelium → KRAS mutation acquisition → PanIN lesion formation → PDAC

## Function

### Clinical manifestations

**Recurrent acute pancreatitis (childhood to early adulthood):**
- First episode: typically age 5-15 years; earlier onset than sporadic acute pancreatitis
- Presentation: severe epigastric pain radiating to back, nausea, vomiting; elevated serum amylase and lipase (>3× upper limit of normal); CT: peripancreatic fat stranding, edema, ± necrosis
- Triggers: alcohol, high-fat meals, stress, viral illness — same as sporadic acute pancreatitis but at much lower exposure thresholds
- Recurrence pattern: multiple episodes per year initially; frequency may decrease as parenchyma is depleted; pain character changes from episodic (acute) to constant (chronic)

**Chronic pancreatitis:**
- Develops after ~10-20 years of recurrent acute episodes (earlier in smokers or with SPINK1 co-mutation)
- Pathology: widespread intralobular and perilobular fibrosis, acinar cell loss, ductal epithelial metaplasia, intracanalicular protein plugs, pancreatic stones (calcium carbonate intraductal concretions)
- Pain: often debilitating, constant (neuropathic component); not reliably correlated with disease activity; central sensitization develops in many patients
- Main pancreatic duct dilation: upstream of strictures or stones → obstructive chronic pancreatitis; indication for endoscopic or surgical decompression

**Exocrine pancreatic insufficiency (EPI):**
- Occurs when >90% of functional acinar mass is lost; typically after 10-20 years of disease
- Symptoms: steatorrhea (greasy, foul-smelling stools), weight loss, malabsorption of fat-soluble vitamins (A, D, E, K)
- Diagnosis: fecal elastase-1 (FE-1 <100 μg/g = severe EPI); 72-hour fecal fat collection; secretin-enhanced MRCP for direct measurement of pancreatic secretory capacity
- Treatment: pancreatic enzyme replacement therapy (PERT) — lipase, protease, amylase with all meals; fat-soluble vitamin supplementation

**Pancreatogenic diabetes mellitus (Type 3c diabetes):**
- Results from islet cell destruction by chronic inflammation and fibrosis
- Characteristics: brittle diabetes (loss of glucagon counterregulation → hypoglycemia risk); low insulin requirement initially (preserved β-cells); eventual absolute insulin deficiency
- Type 3c management: low-dose insulin titrated carefully; avoid sulfonylureas (risk of hypoglycemia); metformin for insulin resistance component if tolerated; glucagon monitoring
- Distinct from Type 1 (autoimmune) and Type 2 (insulin resistance): requires different management approach

**Pancreatic ductal adenocarcinoma (PDAC) — the critical late complication:**
- ~40-fold elevated PDAC risk vs general population; cumulative risk ~40% by age 70 in HP
- PDAC develops from pancreatic intraepithelial neoplasia (PanIN) lesions in the chronically inflamed ductal epithelium
- The oncogenic sequence: chronic inflammation → ductal metaplasia → KRAS mutation acquisition → PanIN1 → PanIN2 → PanIN3 → invasive PDAC (same as sporadic PDAC pathway)
- Risk factors that further elevate PDAC risk within HP: smoking (most important — ~2-fold additional multiplier); onset before age 20; PRSS1 R122H (vs N29I); paternal inheritance (vs maternal — possibly imprinting); SPINK1 N34S co-mutation
- Surveillance: recommended from ~40 years of age (or 20 years after first pancreatitis episode, whichever is later); annual EUS (preferred) or MRCP for early detection; serum CA19-9 (limited sensitivity in chronic pancreatitis background)
- TPIAT eliminates PDAC risk by removing the target organ

## Pathology

### Diagnosis and differential

**Diagnosis of hereditary pancreatitis:**
1. Clinical: ≥2 first- or second-degree relatives with recurrent acute pancreatitis or chronic pancreatitis without clear etiology; OR young-onset idiopathic pancreatitis (childhood/adolescence)
2. Genetic testing: PRSS1 sequencing (R122H, N29I, other coding variants); SPINK1 sequencing (N34S); CFTR sequencing (modifier); CTRC sequencing (modifier)
3. Imaging: CT/MRI pancreas (acute episodes); MRCP (chronic disease — duct morphology, stones, strictures); EUS (fine detail of duct and parenchyma; dysplasia surveillance)
4. Functional: fecal elastase (EPI), HbA1c/glucose (Type 3c diabetes), fat-soluble vitamins

**Differential diagnosis of recurrent childhood pancreatitis:**
- Idiopathic recurrent acute pancreatitis (most common; may have subclinical SPINK1 or CFTR variants)
- Pancreas divisum: congenital failure of dorsal/ventral pancreatic ductal fusion → relative obstruction; MRI/MRCP diagnosis; usually less severe
- Structural anomalies: choledochal cyst, anomalous pancreaticobiliary junction
- Hypertriglyceridemia-induced pancreatitis: serum TG >1000 mg/dL; autosomal recessive LPL/APOC2/APOA5 mutations
- Autoimmune pancreatitis (AIP): IgG4-related; responds to steroids; mass-forming; serum IgG4 elevated; PRSS1 test negative
- Trauma, medication-induced (valproic acid, azathioprine), Reye syndrome

### Management

**Acute pancreatitis episodes:**
- IV fluids (aggressive hydration, especially Lactated Ringer's — reduces SIRS vs normal saline); pain management (NSAIDs/opioids); NPO then early enteral feeding (reduces infectious complications vs TPN); antibiotics only for infected necrosis
- Severity scoring: APACHE II, Atlanta 2012 criteria; CT Severity Index for necrosis quantification
- Necrosectomy: for infected necrotizing pancreatitis; endoscopic step-up approach preferred over open necrosectomy (PANTER trial)

**Chronic pancreatitis — pain management:**
- Analgesic ladder: NSAIDs → tramadol → opioids; opioid addiction risk is very high in chronic pancreatitis patients
- Antineuropathic: pregabalin, duloxetine for neuropathic component of chronic pain
- Endoscopic therapy: ERCP with stone extraction, stricture dilation, pancreatic duct stenting → reduces duct hypertension → pain relief in ~50-70% of patients with ductal disease
- Surgical drainage procedures: lateral pancreaticojejunostomy (Puestow/Partington-Rochelle) for main pancreatic duct ≥5-7 mm; pain-free rate ~60-80% at 5 years
- Pancreatic head resection: Beger procedure (duodenum-preserving), Whipple (pancreaticoduodenectomy) for head-dominant fibrotic disease with inflammatory mass

**Total Pancreatectomy with Islet Autotransplantation (TPIAT):**
- Indication: refractory disabling pain not responsive to endoscopic/surgical drainage; diffuse disease; patient willing to accept lifelong enzyme replacement and manage insulin-requiring diabetes
- Procedure: total pancreatectomy (removes entire pancreas) → islet isolation from the resected pancreas → intraportal infusion of islets into the liver → islets engraft → ~30-40% achieve insulin independence; ~60-70% require reduced insulin vs total pancreatectomy without IAT
- Advantage in HP: eliminates lifetime PDAC risk entirely (no pancreas = no PDAC); removes source of recurrent acute pancreatitis; provides pain relief in ~80% of patients at 1 year
- Timing: best outcomes when performed before development of significant islet damage from prior pancreatitis; TPIAT registry data (University of Minnesota, Cincinnati Children's) guide timing decisions

**PDAC surveillance:**
- Start from age 40 (or 20 years after HP onset if HP began before age 20)
- Annual EUS preferred over CT (avoids radiation; better for small lesions); alternative: MRCP
- Serum CA19-9 annually (limited sensitivity in chronic pancreatitis background; useful for trend)
- Smoking cessation: critically important (smoking alone doubles PDAC risk; in HP, synergistic)
- New FNA/EUS-guided biopsy for any new solid lesion, new ductal stricture, or CA19-9 rise

**Genetic counseling:**
- Autosomal dominant; 50% offspring risk for PRSS1 mutations
- Penetrance: ~80% for R122H; ~65-70% for N29I; phenotypic variability within families
- Testing: genetic counseling before testing children; clinical benefit of early identification → lifestyle modifications (smoking avoidance, alcohol avoidance, surveillance)
- SPINK1 N34S: complex inheritance; counsel as modifier allele; alone does not predict reliable HP

## Connections

- `connects-to` → **[PRSS1](../../03-molecular/prss1/README.md)** — PRSS1 R122H and N29I gain-of-function mutations cause hereditary pancreatitis by preventing trypsin inactivation; autosomal dominant; onset childhood/early adulthood; recurrent acute → chronic pancreatitis → exocrine + endocrine insufficiency; ~40-fold elevated PDAC risk.
- `connects-to` → **[Pancreatic Cancer](../../07-system/pancreatic-cancer/README.md)** — PRSS1-hereditary pancreatitis confers ~40-fold PDAC risk; chronic pancreatic inflammation → acinar-ductal metaplasia → PanIN lesions → PDAC (same progression as sporadic); KRAS mutations are the initiating event in PDAC even in PRSS1-hereditary pancreatitis background.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — Chronic pancreatitis (hereditary PRSS1 or sporadic) → TGF-β release from acinar cells and inflammatory macrophages → pancreatic stellate cell activation → collagen deposition → fibrosis → acinar cell loss → exocrine insufficiency → endocrine β-cell loss → CFRD-like diabetes.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — KRAS oncogenic mutations (G12D/V/R) drive PanIN and PDAC even in hereditary pancreatitis (PRSS1 mutation background); KRAS mutation is the initiating event; chronic trypsin-mediated inflammation → KRAS-susceptible acinar cells → transformation; KRAS is the primary PDAC oncogene.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Recurrent trypsin-driven autodigestion progressively destroys the pancreas → fibrosis, exocrine insufficiency (steatorrhea, PERT) and Type 3c diabetes; total pancreatectomy with islet autotransplantation (TPIAT) relieves refractory pain and eliminates the ~40-fold PDAC risk.
- `connects-to` → **[CFTR](../../03-molecular/cftr/README.md)** — CFTR-driven ductal bicarbonate secretion raises luminal pH and flushes zymogens — one of the pancreas's defenses against premature trypsin activation; CFTR variants act as modifiers that co-contribute to hereditary pancreatitis alongside PRSS1 and SPINK1 mutations.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Progressive fibrotic loss of islet β-cells causes pancreatogenic (Type 3c) diabetes — brittle, with concurrent glucagon deficiency raising hypoglycemia risk; managed with carefully titrated low-dose insulin rather than sulfonylureas, distinguishing it from Type 1 and Type 2.
- `connects-to` → **[Cystic Fibrosis](../cystic-fibrosis/README.md)** — Hereditary pancreatitis and cystic fibrosis are the two major genetic pancreatic diseases: CFTR's ductal bicarbonate flush normally clears zymogens and blocks premature trypsin activation, so CFTR variants modify hereditary pancreatitis while CF destroys the exocrine pancreas.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Fibrosis is the endpoint of hereditary pancreatitis, and the pancreatic stellate cell is its fibroblast: recurrent trypsin injury and TGF-β turn these cells into collagen-secreting myofibroblasts that scar the gland — the same switch driving pancreatic-cancer desmoplasia.
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — Hereditary and alcoholic chronic pancreatitis share one fibrotic endpoint: a PRSS1 mutation resisting trypsin inactivation and chronic alcohol both trigger repeated acinar autodigestion, stellate-cell fibrosis, and exocrine/endocrine failure; smoking raises cancer risk.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Hereditary pancreatitis commonly ends in pancreatogenic (type 3c) diabetes: recurrent inflammation destroys the islets along with the exocrine pancreas, producing an insulin-deficient diabetes that is brittle (glucagon is also lost) and distinct from type 1 and type 2.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Hereditary pancreatitis cripples the digestive system: loss of exocrine acinar tissue causes pancreatic enzyme insufficiency with steatorrhea, malabsorption and weight loss needing lifelong enzyme replacement—while the destroyed gland also forfeits its insulin/glucagon function.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — Hereditary pancreatitis impairs small-intestinal digestion: without pancreatic lipase, protease and amylase reaching the duodenum, fats, proteins and fat-soluble vitamins go unabsorbed, causing steatorrhea and deficiency—so enzyme replacement is timed to meals to restore uptake.

[^whitcomb-1996-prss1]: Whitcomb DC, Gorry MC, Preston RA, et al. Hereditary pancreatitis is caused by a mutation in the cationic trypsinogen gene. *Nat Genet.* 1996;14(2):141-145. [doi:10.1038/ng1096-141](https://doi.org/10.1038/ng1096-141) · [PubMed 8841182](https://pubmed.ncbi.nlm.nih.gov/8841182/)
[^lowenfels-2001-hp-pdac]: Lowenfels AB, Maisonneuve P, DiMagno EP, et al. Hereditary pancreatitis and the risk of pancreatic cancer. *J Natl Cancer Inst.* 2001;93(1):26-31. [doi:10.1093/jnci/93.1.26](https://doi.org/10.1093/jnci/93.1.26) · [PubMed 11136838](https://pubmed.ncbi.nlm.nih.gov/11136838/)

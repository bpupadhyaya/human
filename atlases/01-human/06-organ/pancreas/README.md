---
schema: human-scale-entry/v1
id: pancreas
name: Pancreas
atlas: 01-human
scale: 06-organ
status: draft
last_reviewed: 2026-06-05
summary: "Dual-function (exocrine + endocrine) gland behind the stomach. Exocrine: ~1.5 L/day digestive enzyme secretion. Endocrine: islets of Langerhans — β cells secrete insulin, α cells glucagon, δ cells somatostatin. Central regulator of glucose homeostasis."
aliases: ["pancreatic gland", "glandula pancreatica"]
sources:
  - id: hall-guyton-14-pancreas
    type: textbook
    cite: "Hall JE. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021. Ch. 66."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
  - id: rorsman-2013-beta-cell
    type: peer-reviewed
    cite: "Rorsman P, Braun M. Regulation of insulin secretion in human pancreatic islets. Annu Rev Physiol. 2013;75:155-179."
    doi: "10.1146/annurev-physiol-030212-183754"
    pmid: "22974438"
    url: "https://doi.org/10.1146/annurev-physiol-030212-183754"
  - id: rahier-2008-beta-cell-mass
    type: peer-reviewed
    cite: "Rahier J, Guiot Y, Goebbels RM, Sempoux C, Henquin JC. Pancreatic beta-cell mass in European subjects with type 2 diabetes. Diabetes Obes Metab. 2008;10 Suppl 4:32-42."
    doi: "10.1111/j.1463-1326.2008.00969.x"
    pmid: "18834431"
    url: "https://doi.org/10.1111/j.1463-1326.2008.00969.x"
  - id: longnecker-2014-pancreatitis
    type: peer-reviewed
    cite: "Longnecker DS. Anatomy and histology of the pancreas. Pancreapedia: The Exocrine Pancreas Knowledge Base. 2014."
    doi: "10.3998/panc.2014.3"
    url: "https://doi.org/10.3998/panc.2014.3"
  - id: rawla-2019-pancreatic-cancer
    type: peer-reviewed
    cite: "Rawla P, Sunkara T, Gaduputi V. Epidemiology of pancreatic cancer: global trends, etiology and risk factors. World J Oncol. 2019;10(1):10-27."
    doi: "10.14740/wjon1166"
    pmid: "30834048"
    url: "https://doi.org/10.14740/wjon1166"
  - id: atkinson-2014-t1dm
    type: peer-reviewed
    cite: "Atkinson MA, Eisenbarth GS, Michels AW. Type 1 diabetes. Lancet. 2014;383(9911):69-82."
    doi: "10.1016/S0140-6736(13)60591-7"
    pmid: "23890997"
    url: "https://doi.org/10.1016/S0140-6736(13)60591-7"
cross_links:
  - target: 01-human/03-molecular/insulin
    relation: contains
    note: "β cells of the islets of Langerhans synthesise insulin as preproinsulin; C-peptide cleavage produces active insulin stored in secretory granules and released by Ca²⁺-triggered exocytosis at glucose >6 mmol/L."
  - target: 01-human/03-molecular/insulin
    relation: modulates
    note: "Pancreatic β cells synthesise and secrete insulin in response to blood glucose, amino acids, and incretins; glucose-stimulated insulin secretion is the primary mechanism of postprandial blood glucose regulation."
  - target: 01-human/07-system/digestive-system
    relation: modulates
    note: "Exocrine pancreas secretes ~1.5 L/day of enzyme-rich bicarbonate fluid into the duodenum via the pancreatic duct; amylase, lipase, and proteases digest carbohydrates, fats, and proteins."
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "The pancreas is a retroperitoneal gland (~85 g) between the stomach and duodenum; it is a distinct anatomical organ connecting the gastrointestinal and endocrine systems."
taxonomy:
  uberon: "UBERON:0001264"
  fma: "FMA:7198"
---

# Pancreas

## Overview

The pancreas is a soft, elongated retroperitoneal gland lying in the curve of the duodenum, extending transversely across the posterior abdominal wall from the duodenum to the splenic hilum. In adults it weighs approximately 70–120 g and spans 12–20 cm [^longnecker-2014-pancreatitis]. Despite its modest size, the pancreas performs two entirely distinct physiological roles that are anatomically co-located but functionally separate:

1. **Exocrine pancreas** (~98% of gland mass): acinar cells and ductal epithelium synthesise and secrete 1.0–2.5 L/day of alkaline, enzyme-rich fluid into the duodenum via the main pancreatic duct (duct of Wirsung) and minor accessory duct (duct of Santorini). This secretion is indispensable for digestion of macronutrients — its loss (as in chronic pancreatitis or after pancreatic resection) causes malabsorption and steatorrhoea.

2. **Endocrine pancreas** (~2% of gland mass, the islets of Langerhans, ~1 million islets): four secretory cell types regulate fuel metabolism by releasing hormones directly into the portal circulation. The β cell — secreting insulin — and the α cell — secreting glucagon — form a functional yin–yang axis that maintains blood glucose in the narrow euglycaemic range (~4–6 mmol/L fasting) essential for brain function [^hall-guyton-14-pancreas].

The pancreas develops from the dorsal and ventral pancreatic buds of foregut endoderm (week 5 of gestation); impaired islet development or β-cell dysfunction underlies both major forms of diabetes mellitus, making the pancreas the central organ in one of the world's most prevalent non-communicable diseases.

## Structure

### Gross Anatomy

| Region | Description | Blood supply |
|:---|:---|:---|
| **Head** | Nestled in the C-loop of the duodenum; contains the uncinate process | Gastroduodenal artery (superior pancreaticoduodenal), inferior pancreaticoduodenal artery |
| **Neck** | Narrow region overlying the superior mesenteric vein confluence | Branches from superior mesenteric artery |
| **Body** | Main bulk; crosses the vertebral column at L1–L2 | Splenic artery branches |
| **Tail** | Extends to the splenic hilum; lies within the splenorenal ligament | Splenic artery (distal) |

The **main pancreatic duct** (Wirsung) runs the entire length of the gland, collecting secretion from all acinar lobules, and joins the common bile duct to form the **ampulla of Vater** before draining into the duodenum at the major duodenal papilla. The **sphincter of Oddi** controls outflow; CCK-mediated relaxation allows postprandial flow.

Venous drainage enters the portal system (superior mesenteric and splenic veins → portal vein) — pancreatic hormones therefore encounter the liver first, before reaching the systemic circulation.

### Microscopic Structure

**Exocrine compartment:**

- **Acinar cells** — pyramidal serous cells arranged in berry-like clusters (acini). Each cell is polarised: basal RER synthesises zymogens (inactive enzyme precursors) that are packaged in zymogen granules at the apex and released by regulated exocytosis in response to CCK (cholecystokinin) and vagal stimulation. Key zymogens: trypsinogen, chymotrypsinogen, proelastase, prolipase, prophospholipase A2; amylase and ribonuclease are secreted in active form.
- **Centroacinar cells** — small stellate cells at the centre of each acinus, contiguous with ductal epithelium; express carbonic anhydrase and produce HCO₃⁻-rich fluid in response to secretin.
- **Intercalated / intralobular / interlobular ducts** — progressive coalescence into the main duct; duct cells amplify bicarbonate secretion (HCO₃⁻ can reach 120 mmol/L at maximal stimulation, vs. 30 mmol/L at baseline).

**Endocrine compartment (islets of Langerhans):**

| Cell type | Proportion | Hormone | Location within islet |
|:---|:---|:---|:---|
| β (beta) cells | 60–80% | Insulin, C-peptide, amylin | Core |
| α (alpha) cells | 15–20% | Glucagon | Mantle |
| δ (delta) cells | 5–10% | Somatostatin | Scattered |
| PP cells | 1–2% | Pancreatic polypeptide | Peripheral |
| ε (epsilon) cells | <1% | Ghrelin | Scattered |

Islets are highly vascularised (~10% of pancreatic blood flow to 2% of mass) and receive fenestrated capillaries. Intra-islet paracrine signalling: somatostatin from δ cells suppresses both insulin and glucagon release; glucagon from α cells stimulates β cells; amylin from β cells slows gastric emptying. The spatial organisation (β core, α mantle) creates directional blood flow enabling paracrine crosstalk [^rorsman-2013-beta-cell].

**Pancreatic stellate cells:** quiescent periductal/periacinar fibroblast-like cells that, when activated (in pancreatitis, PDAC), become myofibroblasts producing collagen I/III, fibronectin, and TGF-β — driving the desmoplastic stroma characteristic of pancreatic ductal adenocarcinoma.

## Function

### Exocrine Secretion

Pancreatic exocrine secretion is integrated over three phases triggered by food intake:

**Cephalic phase (~20% of response):** sight, smell, thought of food → vagal activation → ACh on M3 receptors of acinar cells → enzyme-rich, low-volume secretion.

**Gastric phase (~5–10%):** gastric distension → vagovagal reflex and gastrin release → modest stimulation.

**Intestinal phase (~70%):** the dominant phase, driven by two enterohormones:
- **Secretin** (from S cells of duodenum/jejunum): released when duodenal pH < 4.5; acts on ductal cells via cAMP/CFTR → high-volume, HCO₃⁻-rich, enzyme-poor "wash" secretion; neutralises gastric acid entering the duodenum.
- **CCK** (from I cells of duodenum/proximal jejunum): released when fat and protein reach the duodenum; acts on acinar CCK-A receptors (via IP₃/DAG/Ca²⁺ pathway) → enzyme-rich secretion; also stimulates gallbladder contraction and Oddi relaxation, synchronising bile and pancreatic enzyme delivery.

Pancreatic enzymes and their activation:

| Enzyme | Zymogen | Activator | Substrate |
|:---|:---|:---|:---|
| Trypsin | Trypsinogen | Enterokinase (duodenal brush border); autocatalytic once trypsin present | Proteins (cleaves Lys/Arg bonds) |
| Chymotrypsin | Chymotrypsinogen | Trypsin | Proteins (Phe/Trp/Tyr bonds) |
| Elastase | Proelastase | Trypsin | Elastin, other proteins |
| Lipase | Active | (Colipase required) | Triglycerides → fatty acids + monoglyceride |
| Phospholipase A2 | Prophospholipase A2 | Trypsin | Phospholipids |
| Amylase | Active | — | Starch → maltose/glucose |

**Premature intrapancreatic activation** of zymogens — the initiating event in acute pancreatitis — typically occurs in secretory blockade (gallstone obstruction, alcohol-induced ductal hypertension) with trypsin activation triggering a cascade of autodigestion.

### Endocrine Secretion

**Glucose-stimulated insulin secretion (GSIS):** Glucose enters β cells via GLUT2 (rodents)/GLUT1+3 (humans) → glucokinase phosphorylates glucose → glycolysis + mitochondrial oxidation → ↑ ATP/ADP ratio → closure of K_ATP channels (SUR1/Kir6.2 subunits) → membrane depolarisation → opening of L-type Ca²⁺ channels → Ca²⁺ influx → fusion of insulin granules with plasma membrane → insulin secretion into portal blood [^rorsman-2013-beta-cell].

First-phase secretion (within 2–5 min, from readily releasable granules) is characteristically absent in type 2 diabetes. Second-phase secretion (sustained, 2–180 min) draws on reserve granule pool.

**Glucagon secretion:** α cells sense hypoglycaemia via paracrine inhibition relief (less insulin, less somatostatin) and direct glucose sensing; glucagon triggers hepatic glycogenolysis and gluconeogenesis — the primary defence against hypoglycaemia.

**Somatostatin (SRIF-14/SRIF-28):** δ cells act as local rheostats, suppressing insulin, glucagon, and exocrine secretion via Gi-coupled SSTR2/5 receptors; used pharmacologically in the form of octreotide/lanreotide for neuroendocrine tumours, carcinoid syndrome, and acromegaly.

**Pancreatic polypeptide (PP):** Released after meals; inhibits pancreatic exocrine secretion; satiety signal. Useful clinical marker for islet-cell tumours.

## Connections

- **Contains → [Insulin](../../03-molecular/insulin/README.md):** β cells are the sole source of insulin in the body.
- **Modulates → [Insulin](../../03-molecular/insulin/README.md):** GSIS is the key glucose-lowering mechanism.
- **Modulates → [Digestive System](../../07-system/digestive-system/README.md):** exocrine secretion enables macronutrient digestion.
- **Part of → [Human Body](../../08-whole-body/human-body/README.md):** retroperitoneal gland linking digestive and endocrine systems.

## Pathology

### Type 1 Diabetes Mellitus (T1DM)

T1DM is an autoimmune disease in which CD8⁺ T cells, CD4⁺ T cells, and macrophages infiltrate the islets (insulitis) and selectively destroy β cells, leading to absolute insulin deficiency [^atkinson-2014-t1dm]. Global incidence is rising at ~3–5% per year, particularly in high-income countries. Key autoantigens include insulin, GAD65 (glutamic acid decarboxylase), IA-2 (tyrosine phosphatase), and ZnT8 (zinc transporter). At clinical presentation, typically 80–90% of β-cell mass has been destroyed. Treatment: subcutaneous insulin (multiple daily injections or continuous infusion) ± closed-loop "artificial pancreas" systems. Islet transplantation and beta-cell regeneration therapies are under active investigation.

### Type 2 Diabetes Mellitus (T2DM)

T2DM involves both peripheral insulin resistance and progressive β-cell dysfunction/loss. Post-mortem studies show ~40–60% reduction in β-cell mass in T2DM vs. controls [^rahier-2008-beta-cell-mass], partly from apoptosis, partly from dedifferentiation to non-insulin-secreting states. Islet amyloid (from misfolded amylin/IAPP) contributes to β-cell toxicity. Pharmacological targets include: KATP channels (sulfonylureas), incretins (GLP-1 receptor agonists, DPP-4 inhibitors), SGLT2 (flozins — affect renal glucose reabsorption, indirectly reduce β-cell demand), insulin itself.

### Acute Pancreatitis

Acute inflammation of the pancreas caused by premature intrapancreatic zymogen activation. The two most common causes are gallstones (~40%) and alcohol (~30%). Severity ranges from mild/interstitial (self-limiting) to severe necrotising pancreatitis with systemic inflammatory response syndrome (SIRS), multi-organ failure, and ~30% mortality. Ranson criteria and BISAP score guide severity assessment. Diagnosis: serum lipase >3× upper limit of normal. CT shows pancreatic oedema, peripancreatic stranding, or necrosis.

### Chronic Pancreatitis

Progressive fibro-inflammatory destruction of the exocrine pancreas, eventually impairing endocrine function. Causes: alcohol, autoimmune (IgG4-related, type 1 AIP), genetic (PRSS1, SPINK1, CFTR mutations), obstructive, idiopathic. Hallmarks: pancreatic ductal calcifications, exocrine insufficiency (steatorrhoea, fat-soluble vitamin deficiencies — A, D, E, K), and eventually endocrine insufficiency (type 3c diabetes — "pancreatogenic diabetes"). Severe, chronic pain is the dominant symptom; mechanism involves perineural invasion and central sensitisation.

### Pancreatic Ductal Adenocarcinoma (PDAC)

One of the most lethal malignancies: 5-year survival ~12% (all stages), ~3% with distant metastasis [^rawla-2019-pancreatic-cancer]. Incidence is rising globally (~500,000 new cases/year). PDAC arises from ductal epithelium via PanIN (pancreatic intraepithelial neoplasia) precursor lesions; driver mutations: *KRAS* (>90%), *TP53* (~70%), *SMAD4* (~55%), *CDKN2A* (~90%). The dense desmoplastic stroma — driven by activated pancreatic stellate cells — creates a hypoperfused, immunosuppressive tumour microenvironment that excludes immune cells and limits chemotherapy penetration. Late presentation (retroperitoneal location, no early symptoms), lack of validated biomarkers (CA 19-9 is not specific), and drug resistance underlie poor outcomes.

### Pancreatic Neuroendocrine Tumours (PNETs)

Arise from islet cells; classified functional (excess hormone secretion) or non-functional. Key functional types: **insulinoma** (insulin excess → hypoglycaemia; Whipple's triad), **gastrinoma** (gastrin excess → Zollinger-Ellison syndrome), **glucagonoma** (glucagon excess → necrolytic migratory erythema, diabetes), **VIPoma** (VIP excess → watery diarrhoea, hypokalaemia, achlorhydria — WDHA syndrome), **somatostatinoma** (somatostatin excess → diabetes, cholelithiasis, steatorrhoea). Most PNETs are sporadic; ~20% are part of MEN1 syndrome. Octreotide/lanreotide controls symptoms; everolimus/sunitinib approved for progressive PNETs.

[^hall-guyton-14-pancreas]: Hall JE. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021. Ch. 66.
[^rorsman-2013-beta-cell]: Rorsman P, Braun M. Regulation of insulin secretion in human pancreatic islets. *Annu Rev Physiol.* 2013;75:155-179. [doi:10.1146/annurev-physiol-030212-183754](https://doi.org/10.1146/annurev-physiol-030212-183754) · [PubMed 22974438](https://pubmed.ncbi.nlm.nih.gov/22974438/)
[^rahier-2008-beta-cell-mass]: Rahier J et al. Pancreatic beta-cell mass in European subjects with type 2 diabetes. *Diabetes Obes Metab.* 2008;10 Suppl 4:32-42. [doi:10.1111/j.1463-1326.2008.00969.x](https://doi.org/10.1111/j.1463-1326.2008.00969.x) · [PubMed 18834431](https://pubmed.ncbi.nlm.nih.gov/18834431/)
[^longnecker-2014-pancreatitis]: Longnecker DS. Anatomy and histology of the pancreas. *Pancreapedia.* 2014. [doi:10.3998/panc.2014.3](https://doi.org/10.3998/panc.2014.3)
[^rawla-2019-pancreatic-cancer]: Rawla P, Sunkara T, Gaduputi V. Epidemiology of pancreatic cancer. *World J Oncol.* 2019;10(1):10-27. [doi:10.14740/wjon1166](https://doi.org/10.14740/wjon1166) · [PubMed 30834048](https://pubmed.ncbi.nlm.nih.gov/30834048/)
[^atkinson-2014-t1dm]: Atkinson MA, Eisenbarth GS, Michels AW. Type 1 diabetes. *Lancet.* 2014;383(9911):69-82. [doi:10.1016/S0140-6736(13)60591-7](https://doi.org/10.1016/S0140-6736(13)60591-7) · [PubMed 23890997](https://pubmed.ncbi.nlm.nih.gov/23890997/)

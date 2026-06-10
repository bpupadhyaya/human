---
schema: human-scale-entry/v1
id: stomach
name: Stomach
atlas: 01-human
scale: 06-organ
status: draft
last_reviewed: 2026-06-05
summary: "J-shaped muscular organ in the epigastrium; length 25–30 cm, capacity 1–4 L. Secretes HCl (parietal cells, H⁺/K⁺-ATPase), pepsinogen (chief cells), intrinsic factor, mucus, and gastrin (G cells). Three-phase acid regulation; gastric mucosal barrier relies on prostaglandins."
aliases: ["ventriculus", "gaster", "gastric", "fundus", "antrum", "pylorus", "cardia"]
sources:
  - id: guyton-hall
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
  - id: stryer-biochemistry
    type: textbook
    cite: "Berg JM, Tymoczko JL, Stryer L. Biochemistry. 9th ed. W.H. Freeman; 2019."
    url: "https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/07-system/digestive-system
    relation: part-of
    note: "Stomach receives food bolus from oesophagus, performs mechanical trituration and chemical digestion (HCl + pepsin), and delivers chyme to duodenum; gastric phase involves all cell types in gastric glands."
  - target: 01-human/06-organ/liver
    relation: modulates
    note: "Stomach-derived gastrin enters portal circulation and reaches hepatocytes; achlorhydria alters bile acid secretion; H. pylori LPS reaches liver via portal blood, activating Kupffer cell TLR4."
  - target: 01-human/06-organ/pancreas
    relation: modulates
    note: "Antral G cells secrete gastrin stimulating pancreatic enzyme secretion; gastric acid entering duodenum triggers secretin release driving pancreatic HCO3 secretion; CCK from I-cells amplifies this."
  - target: 01-human/07-system/nervous-system
    relation: modulates
    note: "Stomach ENS contains ~100 million enteric neurons; vagal afferents signal satiety and nausea; ghrelin from gastric fundus acts on hypothalamic NPY/AgRP neurons to stimulate appetite."
  - target: 02-pathogen/02-bacteria/helicobacter-pylori
    relation: infected-by
    note: "Infected by Helicobacter pylori."
  - target: 03-medicine/02-traditional/licorice-root
    relation: modulated-by
    note: "Modulated by Licorice Root (Glycyrrhiza glabra / G. uralensis)."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Parietal cell H⁺/K⁺-ATPase secretes H⁺ into the gastric lumen against a 10⁶-fold concentration gradient (pH ~1.5); proton pump inhibitors (PPIs: omeprazole, pantoprazole) irreversibly inhibit H⁺/K⁺-ATPase via Cys813/892, reducing basal acid by >90%."
---

# Stomach

## Overview

The stomach is a J-shaped muscular organ located in the left upper quadrant and epigastric region of the abdomen, positioned between the oesophagus and duodenum [^guyton-hall]. It is the most dilatable segment of the gastrointestinal tract, with a resting capacity of 1–1.5 L that can distend to approximately 4 L after a large meal. The stomach performs three essential roles: mechanical trituration of food into fine particles, chemical digestion via hydrochloric acid and pepsin, and regulated delivery of chyme into the duodenum. Its gastric glands contain at least six distinct secretory cell types, each tightly regulated by neural, hormonal, and paracrine signals.

The stomach is central to both nutrition (protein digestion initiation, intrinsic factor secretion for vitamin B12 absorption) and pathology: *Helicobacter pylori* infection of the gastric mucosa is the leading cause of peptic ulcer disease worldwide, and gastric adenocarcinoma is the fifth most common cancer and second most common cause of cancer-related death globally [^guyton-hall].

## Structure

### Gross Anatomy and Regions

The stomach spans approximately 25–30 cm from the gastro-oesophageal junction (GEJ, cardiac orifice) to the pyloric sphincter. Five anatomical regions are functionally distinct:

| Region | Location | Functional specialisation |
|:---|:---|:---|
| Cardia | Immediately distal to GEJ | Transition zone; cardiac glands (mucous cells); anti-reflux zone |
| Fundus | Dome above GEJ, left of cardia | Receptive relaxation reservoir; oxyntic glands (parietal + chief cells); ghrelin-secreting X/A-like cells |
| Body (corpus) | Main central region | Predominant acid (parietal cells) and pepsinogen (chief cells) secretion; ECL cells |
| Antrum | Distal third, inferior | G-cell rich (gastrin); antral peristalsis and pyloric pump |
| Pylorus | Sphincter at gastroduodenal junction | Thick circular smooth muscle; regulates gastric emptying rate (2–4 mm chyme boluses) |

The gastric lumen is lined by rugae — prominent mucosal folds that flatten with distension and increase surface area.

### Wall Layers

The stomach wall has a distinctive four-layer structure [^guyton-hall]:

1. **Mucosa:** Surface epithelium (columnar mucous cells) + gastric pits (foveolae, ~25% of mucosal depth) opening into gastric glands. Renewed every 3–7 days from isthmus progenitor cells.
2. **Submucosa:** Dense connective tissue with blood vessels, lymphatics, Meissner's (submucosal) plexus.
3. **Muscularis externa (three layers — unique to stomach):**
   - Inner oblique layer (fundus and body; enables churning)
   - Middle circular layer (forms pyloric sphincter)
   - Outer longitudinal layer
   Interstitial cells of Cajal (ICC) — the gastric pacemaker — generate 3 slow waves/min originating in the greater curvature pacemaker zone.
4. **Serosa:** Visceral peritoneum.

### Gastric Gland Cell Types

Gastric glands are the functional secretory units embedded in the mucosa. Cell composition varies by region:

| Cell type | Location | Product | Stimulus |
|:---|:---|:---|:---|
| Parietal (oxyntic) | Body/fundus | HCl, intrinsic factor | Histamine (H2R→cAMP), gastrin (CCK-2R→Ca²⁺), ACh (M3R→Ca²⁺) |
| Chief (zymogen) | Body/fundus | Pepsinogen I/II | ACh, secretin, acid |
| G cells | Antrum | Gastrin (G-17) | Dietary protein, stomach distension, vagal ACh |
| ECL cells | Body | Histamine | Gastrin, vagal ACh |
| D cells | Antrum/body | Somatostatin | Low luminal pH (negative feedback) |
| Mucous neck cells | Gland neck | Mucus, HCO₃⁻ | Basal; ↑ by prostaglandins (PGE2, PGI2) |
| Enterochromaffin cells | Mucosa | Serotonin (5-HT) | Mechanical/chemical stimuli |
| X/A-like cells | Fundus | Ghrelin | Fasting, low blood glucose |

The **parietal cell** is the most energetically demanding cell in the GI tract. At rest, H⁺/K⁺-ATPase (proton pump) is sequestered in cytoplasmic tubulovesicles. Stimulation → fusion with apical canalicular membrane → active pumping of H⁺ into the lumen at up to 150 mM HCl (pH 0.8 at the canalicular surface, equilibrating to intragastric pH 1.5–3.5). The resulting alkaline tide in venous blood temporarily raises blood and urine pH postprandially [^guyton-hall].

## Function

### Acid Secretion: Three-Phase Regulation

**Cephalic phase (~30% of acid secretion):**
- Stimulus: sight, smell, taste, thought of food
- Pathway: vagal activation → preganglionic fibres → enteric ganglia → postganglionic ACh → parietal cells (M3R) + G cells → gastrin release + ECL histamine release → integrated stimulation of HCl secretion

**Gastric phase (~60% of acid secretion):**
- Stimuli: gastric distension (mechanoreceptor → vagovagal reflex) + luminal protein/peptides (direct G-cell stimulation)
- Gastrin (G-17) released from antral G cells → bloodstream → parietal cell CCK-2R → intracellular Ca²⁺ → H⁺/K⁺-ATPase activation; gastrin also → ECL histamine release → H2R on parietal cells → additive cAMP → PKA signalling

**Intestinal phase (~10% of acid secretion):**
- Initial stimulatory phase: protein in duodenum → intestinal gastrin (G-34)
- Inhibitory phase: acid/fat/osmolarity in duodenum → secretin (S-cells), CCK (I-cells), GIP (K-cells), somatostatin → enterogastric reflex (vagal and myenteric) → ↓gastric acid and motility

**Negative feedback:** Luminal pH <3 in antrum → D-cell somatostatin release → paracrine inhibition of adjacent G cells and ECL cells → ↓gastrin, ↓histamine → reduced acid output; this protects the mucosa from excessive acidification.

### Peptic Digestion

Chief cells secrete pepsinogen I (body glands) and pepsinogen II (body + antrum) as inactive zymogens [^stryer-biochemistry]. At pH <5, pepsinogen undergoes autocatalytic cleavage (and HCl-catalysed cleavage) → pepsin (aspartyl protease, optimum pH 1.5–2.5). Pepsin cleaves peptide bonds adjacent to aromatic and hydrophobic residues, initiating protein digestion into large peptide fragments. Pepsin activity is irreversibly inactivated at pH >7 on entry to the duodenum (neutralised by pancreatic HCO₃⁻).

### Intrinsic Factor and Vitamin B12

Parietal cells co-secrete **intrinsic factor (IF)**, a 45 kDa glycoprotein, alongside HCl [^guyton-hall]. IF binds dietary vitamin B12 (cobalamin) in the acidified gastric lumen, forming a stable IF-B12 complex. This complex resists proteolysis and travels to the terminal ileum, where cubilin/amnionless (CUBAM) receptor mediates endocytosis → transcytosis → release of B12 into portal circulation bound to transcobalamin II. Parietal cell loss (autoimmune gastritis, gastrectomy) → IF deficiency → pernicious anaemia (megaloblastic, subacute combined degeneration of spinal cord).

### Gastric Mucosal Defence

The gastric mucosa must withstand pH 1.5–3.5, pepsin, bile reflux, and ingested pathogens. Defence is multilayered:

1. **Mucus-bicarbonate layer:** Mucous neck cells and surface epithelial cells secrete 1–1.5 mm thick gel-forming mucus (MUC5AC, MUC6) + HCO₃⁻ → pH gradient from ~2 at luminal surface to ~7 immediately adjacent to epithelium [^guyton-hall]
2. **Prostaglandins (PGE2, PGI2):** Generated by COX-1 (constitutive) in mucosal cells → ↑mucus/HCO₃⁻ secretion, ↑mucosal blood flow, ↓acid secretion. NSAID use → COX-1 inhibition → ↓prostaglandins → mucosal vulnerability
3. **Rapid restitution:** Surface epithelial cells adjacent to erosions migrate within minutes to cover defects (without proliferating) — requires intact basement membrane and growth factors (EGF, TGF-α)
4. **Mucosal blood flow:** Rich submucosal capillary network delivers O₂/nutrients and removes H⁺ that back-diffuses through mucosa; maintained by nitric oxide (NO) and prostaglandins

### Motility and Gastric Emptying

After meal ingestion, two regions behave differently:

- **Fundus:** **Receptive relaxation** (vagally mediated via VIP and NO) → fundal accommodation of food bolus without significant pressure rise; proximal fundal tone then slowly increases, providing the pressure gradient for gastric emptying
- **Antrum/pylorus:** 3 peristaltic slow waves/min from ICC pacemaker → propulsive contractions triturate food against a transiently closed pylorus → retropulsion of larger particles → grinding → eventually 2–4 mm particles permitted through pylorus as chyme

**Emptying regulation:** Duodenal feedback (acid, fat, osmolarity, distension) → CCK, secretin, GIP, neural enterogastric reflex → ↓gastric contractility and ↑pyloric tone → slows emptying. Liquids empty faster (~20 min) than solids (~2–4 h). Fat delays emptying most significantly.

## Connections

- **Part of:** [Digestive System](../../07-system/digestive-system/README.md) — stomach receives the food bolus from the oesophagus, performs mechanical trituration and chemical digestion (HCl + pepsin), and delivers chyme to the duodenum; the gastric phase of digestion involves all cell types of the gastric glands.
- **Modulates:** [Liver](../liver/README.md) — stomach-derived gastrin enters portal circulation and reaches hepatocytes; gastric acid disruption and achlorhydria alter bile acid secretion; *H. pylori* LPS reaches the liver via portal blood, activating Kupffer cell TLR4.
- **Modulates:** [Pancreas](../pancreas/README.md) — antral G cells secrete gastrin stimulating pancreatic enzyme secretion; gastric acid entering the duodenum triggers secretin release driving pancreatic HCO₃⁻ secretion; CCK from I-cells further amplifies this response.
- **Modulates:** [Nervous System](../../07-system/nervous-system/README.md) — stomach has ~100 million enteric neurons (ENS); vagal afferents signal satiety, nausea, and stretch; ghrelin from fundal X/A-like cells acts on hypothalamic NPY/AgRP neurons to stimulate appetite.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Parietal cell H⁺/K⁺-ATPase secretes H⁺ into the gastric lumen against a 10⁶-fold gradient (pH ~1.5); proton pump inhibitors (PPIs: omeprazole, pantoprazole) irreversibly inhibit H⁺/K⁺-ATPase via Cys813/892, reducing basal acid by >90%.

## Pathology

### Peptic Ulcer Disease (PUD)

The two major causes account for >95% of cases:

**H. pylori (CagA/VacA strains):**
- Urease generates NH₃ → neutralises local acid → bacteria colonise antrum → CagA injected via T4SS into epithelial cells → ↑NF-κB, IL-8, gastrin → mucosal inflammation → disruption of mucus barrier → ulceration
- CagA+ strains 2–3× higher ulcer risk; VacA → vacuolating cytotoxin → epithelial cell death
- Duodenal ulcers (antral gastritis pattern → ↑gastrin → ↑acid → duodenal ulceration) are more common than gastric ulcers (pangastritis/body predominant → ↓acid but ↓mucosal defence)
- Triple therapy: PPI + clarithromycin + amoxicillin (7–14 days), or bismuth-quadruple therapy in clarithromycin-resistant areas; test and treat strategy

**NSAIDs:**
- Systemic COX-1 inhibition → ↓PGE2/PGI2 → ↓mucus and HCO₃⁻ → ↓mucosal blood flow → ↑vulnerability to acid/pepsin back-diffusion
- Risk: dose-dependent; selective COX-2 inhibitors (celecoxib) → less GI toxicity but ↑cardiovascular risk
- Co-prescribe PPI for high-risk patients (elderly, prior PUD, anticoagulants)

### Gastric Adenocarcinoma

Two distinct subtypes:

| Type | Subsite | Aetiology | Molecular | Trend |
|:---|:---|:---|:---|:---|
| Non-cardia (intestinal type) | Body/antrum | H. pylori → chronic atrophic gastritis → intestinal metaplasia → dysplasia (Correa cascade) | TP53, ARID1A, CDH1, KRAS | Declining |
| Cardia (diffuse/GEJ) | GEJ | GERD, obesity; H. pylori role less clear | ERBB2 (HER2, ~15%), FGFR2 | Rising |

The Correa cascade: normal mucosa → chronic gastritis → atrophic gastritis → intestinal metaplasia → dysplasia → carcinoma. *H. pylori* drives steps 1–3; eradication at early stages reduces cancer risk by ~40%.

### Autoimmune Gastritis (Type A) and Pernicious Anaemia

Autoimmune attack on parietal cells (anti-H⁺/K⁺-ATPase antibodies, anti-parietal cell antibodies) + loss of intrinsic factor (anti-IF antibodies, blocking type) → achlorhydria + megaloblastic anaemia (B12 deficiency) + subacute combined degeneration of the cord (dorsal column + corticospinal tract demyelination). Associated with other autoimmune diseases (thyroid, T1DM, vitiligo). Treat: parenteral B12 (hydroxocobalamin) lifelong.

### Gastro-Oesophageal Reflux Disease (GORD)

Lower oesophageal sphincter (LOS) incompetence (transient LOS relaxations, ↓resting pressure, hiatus hernia) → acid/bile reflux into oesophagus → heartburn, regurgitation. Chronic → Barrett's oesophagus (columnar intestinal metaplasia of oesophageal squamous epithelium, premalignant) → oesophageal adenocarcinoma (EAC). Treat: lifestyle, PPI (gold standard), surgical fundoplication.

### Zollinger-Ellison Syndrome

Gastrinoma (usually in gastrinoma triangle: duodenum > pancreas > other) → unregulated gastrin secretion → massive gastric acid hypersecretion → multiple, refractory peptic ulcers (often distal duodenum/jejunum), diarrhoea, oesophagitis. Secretin stimulation test (paradoxical gastrin rise). Associated with MEN-1 (20–25%). Treat: high-dose PPI; surgical resection if localised.

### Gastroparesis

Delayed gastric emptying without mechanical obstruction; commonest causes: diabetes mellitus (autonomic neuropathy → ICC dysfunction), post-vagotomy/surgery, idiopathic. Symptoms: nausea, vomiting, early satiety, postprandial fullness, erratic glycaemic control in DM. Diagnose: scintigraphic gastric emptying study. Treat: dietary modification (small, low-fat, low-fibre meals), prokinetics (metoclopramide, domperidone, erythromycin), gastric electrical stimulation in refractory cases.

## See Also

- [Digestive System](../../07-system/digestive-system/README.md) — system-level context
- [Pancreas](../pancreas/README.md) — reciprocal gastro-pancreatic hormonal axis
- [Liver](../liver/README.md) — portal delivery of gastric secretions and microbial products
- [Small Intestine](../small-intestine/README.md) — receives and processes gastric chyme
- [Nervous System](../../07-system/nervous-system/README.md) — enteric nervous system, vagal regulation, appetite

[^guyton-hall]: Hall JE, Hall ME. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021.
[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019.

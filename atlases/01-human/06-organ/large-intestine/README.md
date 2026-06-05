---
schema: human-scale-entry/v1
id: large-intestine
name: Large Intestine
atlas: 01-human
scale: 06-organ
status: draft
last_reviewed: 2026-06-05
summary: "~1.5 m colon + rectum; colonocyte-lined crypts without villi. Absorbs ~1.5 L water/day; harbours ~10¹³ bacteria producing SCFAs (butyrate, propionate, acetate) from fibre; key immunological organ. Dysbiosis linked to IBD, CRC, metabolic disease."
aliases: ["colon", "large bowel", "cecum", "rectum", "sigmoid colon", "ascending colon", "transverse colon"]
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
    note: "Large intestine absorbs water and electrolytes from ileal effluent (~1.5 L → 150 mL formed stool/day), harbours ~10¹³ bacteria that ferment fibre to SCFAs (butyrate, propionate, acetate), and synthesises vitamin K2."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "Large intestine is a major immunological organ; microbiota SCFAs (butyrate via GPR109a) expand colonic FOXP3+ Tregs; IgA secretion; MALT structures sample luminal antigens; dysbiosis → IBD, CRC."
  - target: 01-human/06-organ/liver
    relation: modulates
    note: "Gut-liver axis: portal blood delivers SCFAs (propionate → hepatic gluconeogenesis, butyrate → ketone bodies) and microbial metabolites (bile acids, LPS, urolithins) to liver; dysbiosis → NASH via LPS/TLR4/NF-κB."
  - target: 01-human/07-system/nervous-system
    relation: modulates
    note: "Gut-brain axis: ENS contains ~100 million neurons in colon; microbiome-derived SCFAs and tryptophan metabolites (serotonin, indole) signal via vagus and circulation; gut dysbiosis linked to depression, anxiety, Parkinson's."
  - target: 02-pathogen/06-microbiome/bacteroides-fragilis
    relation: modulated-by
    note: "Modulated by Bacteroides fragilis."
  - target: 02-pathogen/06-microbiome/akkermansia-muciniphila
    relation: modulated-by
    note: "Modulated by Akkermansia muciniphila."
  - target: 02-pathogen/06-microbiome/faecalibacterium-prausnitzii
    relation: modulated-by
    note: "Modulated by Faecalibacterium prausnitzii."
  - target: 02-pathogen/06-microbiome/bifidobacterium-longum
    relation: modulated-by
    note: "Modulated by Bifidobacterium longum."
  - target: 03-medicine/03-food/dietary-fiber
    relation: modulated-by
    note: "Modulated by Dietary Fiber and Butyrate."
---

# Large Intestine

## Overview

The large intestine is the terminal segment of the gastrointestinal tract, spanning approximately 1.5 m from the ileocaecal valve to the anus [^guyton-hall]. Despite its shorter length relative to the small intestine, the large intestine performs functions indispensable to whole-body homeostasis: it recovers ~1.5 L of water and electrolytes from the ~1.5 L of ileal effluent it receives daily (the small intestine already absorbed ~7 of the ~8 L entering the gut each day); it houses ~10¹³ microorganisms — the gut microbiome — whose metabolic activity fundamentally influences host immunity, metabolism, and neurobiology; and it synthesises and absorbs microbial-derived vitamins (K2, B vitamins).

Unlike the small intestine, the large intestinal mucosa lacks villi. Its absorptive surface consists of flat colonocytes lining straight crypts (crypts of Lieberkühn). The colon is the site of microbial fermentation, transforming indigestible dietary fibre into short-chain fatty acids (SCFAs) that serve as the primary fuel for colonocytes and have far-reaching anti-inflammatory and epigenetic effects.

## Structure

### Gross Anatomy

The large intestine is divided into anatomically distinct regions:

| Segment | Length | Key features |
|:---|:---|:---|
| Caecum | 6–8 cm | Blind pouch, receives ileal contents at ileocaecal valve; appendix attaches at its posteromedial wall |
| Appendix | 8–10 cm | Lymphoid organ, remnant; lumen may obstruct → appendicitis |
| Ascending colon | 15 cm | Right side; retroperitoneal; hepatic flexure at right | 
| Transverse colon | 50 cm | Mobile, intraperitoneal; transverse mesocolon; splenic flexure at left |
| Descending colon | 25 cm | Left side; retroperitoneal |
| Sigmoid colon | 35–40 cm | S-shaped; mobile; commonest site of diverticular disease and volvulus |
| Rectum | 12–15 cm | Follows sacral curve; rectal ampulla; no peritoneal covering (partially) |
| Anal canal | 3–4 cm | Dentate line separates squamous from columnar epithelium; internal + external sphincters |

**Distinctive features of the colon wall:**
- **Taeniae coli:** Three narrow bands of longitudinal smooth muscle (shorter than the overall colon length) → create haustral sacculations (haustra), responsible for the characteristic baggy radiographic appearance
- **Haustra:** Saccular pouches between haustral folds; allow segmental mixing and slow passage
- **Appendices epiploicae:** Peritoneal fat appendages along the colon's outer surface; can twist → epiploic appendagitis

### Microscopic Structure

**Mucosa:** No villi. Straight, parallel crypts of Lieberkühn (~0.5 mm deep) lined by:
- **Surface colonocytes:** Absorptive cells (shorter microvilli than small intestinal enterocytes); ENaC, AQP3, AQP8; principal ion-absorbing cells
- **Goblet cells:** More abundant than in small intestine (~30% of crypt cells in distal colon); MUC2 secretion → thick mucus bilayer (inner adherent layer, virtually sterile; outer loose layer, inhabited by bacteria)
- **Enteroendocrine cells (L-cells):** GLP-1, GLP-2, PYY, serotonin
- **LGR5+ stem cells:** At crypt base (also LGR4+); Wnt/Notch/EGF-driven; generate all colonocyte lineages; transit-amplifying zone in middle crypt
- **No Paneth cells** (normally absent in colon; their presence is a marker of intestinal metaplasia in colon disease)

**Muscularis:** Inner circular + outer longitudinal (condensed into 3 taeniae coli) + myenteric plexus (Auerbach's); ICCs of Cajal pacemaking.

**Submucosa:** Meissner's plexus, blood vessels, lymphatics. Prominent lymphoid aggregates (colonic equivalent of Peyer's patches).

## Function

### Water and Electrolyte Absorption

The colon receives ~1.5 L of watery ileal effluent daily and reduces it to ~150 mL of formed stool — a ~90% water absorption efficiency [^guyton-hall].

**Sodium absorption (major driving force):**
- **Proximal colon:** Electroneutral Na⁺/Cl⁻ co-absorption (coupled NHE3/DRA exchange — Na⁺/H⁺ and Cl⁻/HCO₃⁻); also Na⁺-nutrient cotransport for residual amino acids/SCFAs
- **Distal colon/rectum:** Electrogenic Na⁺ absorption via **ENaC** (epithelial sodium channel) — aldosterone-sensitive; mineralocorticoid excess → hypernatraemia/hypokalaemia; amiloride blocks ENaC

**Water follows osmotically** via aquaporin channels (AQP3, AQP8 basolateral; AQP4; paracellular in proximal colon).

**Chloride secretion (secretory diarrhoea mechanism):** CFTR (basolateral Cl⁻ entry via NKCC1; apical exit via CFTR) stimulated by cAMP (cholera toxin → irreversible Gs activation → cAMP → PKA → CFTR → massive Cl⁻ secretion → water follows → secretory diarrhoea).

### Microbial Fermentation and Short-Chain Fatty Acids

The colonic microbiome (~10¹³ organisms, ~1 kg by weight) ferments dietary fibre, resistant starch, and other indigestible substrates to produce SCFAs [^stryer-biochemistry]:

**Key producers:**
- **Butyrate:** Firmicutes (Roseburia, Faecalibacterium prausnitzii, Ruminococcus, Eubacterium hallii) via butyryl-CoA → acetate:CoA transferase pathway
- **Propionate:** Bacteroidetes (Bacteroides, Prevotella) via succinate/acrylate pathways
- **Acetate:** Most bacteria; also principal systemic SCFA, absorbed and used peripherally

**Colonocyte fuel:**
Butyrate is the primary energy source for surface colonocytes (~70% of total colonocyte energy consumption), via β-oxidation → acetyl-CoA → TCA cycle → ATP. Butyrate starvation (fasting, antibiotic perturbation, fibre-free diet) → colonocyte apoptosis → mucosal atrophy.

**Systemic effects:**
- Butyrate: HDAC inhibitor → epigenetic regulation of inflammatory gene expression; GPR109a signalling → induces colonic FOXP3+ regulatory T cells → mucosal and systemic immune tolerance; activates TP53 in cancer cells → pro-apoptotic in CRC
- Propionate: absorbed → portal vein → hepatic gluconeogenesis substrate (propionyl-CoA → succinyl-CoA → OAA → glucose); GPR41/43 signalling
- Acetate: released into systemic circulation; crosses blood-brain barrier → appetite regulation via hypothalamic FFAR3

### Immune Function

The colonic mucosa harbours the densest concentration of immune cells in the body [^guyton-hall]:

- **Lamina propria:** IgA-secreting plasma cells (dimeric IgA → secretory IgA [sIgA] via pIgR transcytosis → luminal protection without inflammation), resident macrophages (tolerogenic, IL-10-producing), dendritic cells (sample luminal antigens via transepithelial dendrites)
- **Isolated lymphoid follicles (ILFs):** Colonic equivalent of small intestinal Peyer's patches; antigen sampling via overlying M-cells
- **Intraepithelial lymphocytes (IELs):** γδ T cells (surveillance)
- **Regulatory T cells (Tregs):** Butyrate-induced FOXP3+ Tregs are critical for mucosal tolerance; depleted in IBD

**Microbiome-immune interaction:** Commensal bacteria (especially Clostridia cluster IV and XIVa, Bacteroides fragilis polysaccharide A, Bifidobacterium) drive Treg induction and IL-10 production → prevents excessive inflammatory responses to luminal antigens. Dysbiosis → ↑Proteobacteria, ↓Firmicutes → ↑LPS → TLR4/NF-κB → pro-inflammatory cytokines → IBD or systemic metabolic inflammation.

### Vitamin Synthesis

Colonic bacteria synthesise:
- **Vitamin K2 (menaquinones):** MK-4 to MK-13 depending on species; absorbed in colon (colon can absorb some lipophilic compounds); quantitatively important for coagulation factor synthesis in the gut and extra-hepatic tissue (bone, vascular)
- **Folate (B9):** synthesised by Bifidobacterium, Lactobacillus; uncertain contribution to host folate status
- **Biotin (B7):** E. coli, Bacteroides; contributes to host biotin requirement
- **Riboflavin (B2):** Lactobacillus; minimal systemic contribution

### Motility and Defaecation

**Haustral contractions:** Rhythmic segmental contractions (3–12 per minute) mix colonic contents without net propulsion; slow transit allows maximal water and SCFA absorption.

**Mass movements (high-amplitude propagating contractions, HAPCs):** Occur 1–3 times daily, typically triggered by the gastrocolic reflex (meal ingestion → colonic motor response); propel content from ascending to sigmoid colon; mediated by 5-HT4 receptor activation.

**Defaecation reflex:** Stool enters rectum → rectal distension → mechanoreceptors → afferent signals → defaecation urge; puborectalis relaxes (anorectal angle straightens from ~90° to ~130°); involuntary internal anal sphincter (IAS, smooth muscle, tonic contraction maintained by myenteric VIP/NO) undergoes rectoanal inhibitory reflex (RAIR) → IAS relaxes; voluntary external anal sphincter (EAS, puborectal/external sphincter complex, pudendal nerve, can be voluntarily contracted to defer defaecation) → coordinated evacuation.

## Connections

- **Part of:** [Digestive System](../../07-system/digestive-system/README.md) — absorbs water and electrolytes from ileal effluent (~1.5 L → 150 mL formed stool/day), harbours ~10¹³ bacteria that ferment dietary fibre to SCFAs (butyrate, propionate, acetate), and synthesises vitamin K2.
- **Modulates:** [Immune System](../../07-system/immune-system/README.md) — major immunological organ; microbiota-derived SCFAs (butyrate via GPR109a) expand colonic FOXP3+ Tregs; sIgA secretion; MALT structures sample luminal antigens; dysbiosis → IBD and CRC.
- **Modulates:** [Liver](../liver/README.md) — gut-liver axis: portal blood delivers SCFAs (propionate → hepatic gluconeogenesis substrate; butyrate → hepatic ketone body production) and microbial metabolites (secondary bile acids, LPS, urolithins) to the liver; dysbiosis → NASH via LPS/TLR4/NF-κB.
- **Modulates:** [Nervous System](../../07-system/nervous-system/README.md) — gut-brain axis: ENS contains ~100 million neurons in the colon; microbiome-derived SCFAs and tryptophan metabolites (serotonin, indole derivatives) signal via the vagus nerve and systemic circulation; gut dysbiosis linked to depression, anxiety, and Parkinson's disease (α-synuclein propagation).

## Pathology

### Colorectal Cancer (CRC)

Third most common cancer, second most common cause of cancer death worldwide. The **Vogelstein adenoma-carcinoma sequence** describes the stepwise accumulation of driver mutations [^guyton-hall]:

**Chromosomal instability (CIN) pathway (~70%):**
APC mutation (Wnt pathway, adenoma initiation) → KRAS mutation (growth advantage) → SMAD4/TGF-β pathway loss (tumour progression) → TP53 mutation (genomic instability, carcinoma) → metastasis.

**Microsatellite instability (MSI) pathway (~15%):**
DNA mismatch repair (MMR) deficiency — somatic (MLH1 promoter methylation, BRAF V600E) or germline (Lynch syndrome: MLH1, MSH2, MSH6, PMS2 mutations, autosomal dominant) → hypermutation → neoantigens → immunogenic → better prognosis, high response to immune checkpoint inhibitors (pembrolizumab).

**Hereditary syndromes:**
- Lynch syndrome: MMR gene germline mutation; lifetime CRC risk 50–80%; also endometrial, ovarian, gastric, urothelial cancers
- FAP (familial adenomatous polyposis): APC germline mutation → 100s-1000s polyps → inevitable CRC by 40s; prophylactic colectomy

**Prevention:** Aspirin reduces CRC risk 30–40% (COX-2 inhibition in tumour cells, apoptosis induction); colonoscopy (removes adenomas) — established screening modality.

### Inflammatory Bowel Disease: Ulcerative Colitis (UC)

Chronic relapsing mucosal inflammatory disease affecting colon exclusively. Extends from rectum (always involved) proximally in a continuous pattern (no skip lesions), up to pan-colitis [^guyton-hall].

**Histology:** Mucosal and submucosal only (unlike Crohn's transmural); crypt abscesses (PMNs in crypts); crypt distortion; goblet cell depletion; pseudopolyps (areas of inflamed mucosa between ulcers). No granulomata (differentiates from Crohn's).

**Complications:** Toxic megacolon (colonic dilation >6 cm with systemic toxicity → perforation risk), primary sclerosing cholangitis (PSC, 4% of UC — stricturing of bile ducts), colorectal cancer (risk ~0.5-1%/year after 8–10 years of pan-colitis; surveillance colonoscopy).

**Treatment:** 5-ASA (mesalazine/sulfasalazine — induces and maintains remission in mild-moderate), corticosteroids (acute severe), azathioprine/6-MP (maintenance), anti-TNF (infliximab, adalimumab — moderate-severe), anti-integrin (vedolizumab), JAK inhibitors (tofacitinib, upadacitinib), IL-12/23 inhibitor (ustekinumab). Surgery (proctocolectomy) is curative.

### Clostridioides difficile Infection (CDI)

Anaerobic spore-forming gram-positive bacterium; after antibiotic disruption of normal microbiome, C. difficile spores germinate → vegetative bacteria → Toxin A (enterotoxin) + Toxin B (cytotoxin) → NF-κB/MAPK activation → mucosal inflammation and cell death → **pseudomembranous colitis** (yellow-white plaques of fibrin, mucus, inflammatory cells on colonoscopy). Risk: antibiotic exposure (especially clindamycin, fluoroquinolones, cephalosporins, ampicillin), hospital acquisition, PPIs, age >65. Treat: stop causative antibiotic; fidaxomicin (non-inferior, lower recurrence than vancomycin); oral vancomycin; faecal microbiota transplantation (FMT, ~90% efficacy for recurrent CDI).

### Diverticular Disease

False diverticula (mucosal/submucosal herniation through points of wall weakness, where blood vessels penetrate muscularis propria) in the sigmoid colon (most common, due to highest intraluminal pressure). Associated with low-fibre, high-animal-fat diet → small, hard stools → prolonged straining → ↑intraluminal pressure → herniation.

**Diverticulitis:** Diverticulum blocks → faecalith → bacterial overgrowth → microperforations → pericolic inflammation. Spectrum: localised pain/fever → perforation → abscess → fistula (colovesical — pneumaturia, faecaluria) → generalised peritonitis. Treat: antibiotics (mild: oral; severe: IV piperacillin-tazobactam); CT-guided drainage; surgery (Hartmann's for perforation/peritonitis).

**Diverticular bleeding:** Most common cause of lower GI haemorrhage; venous, self-limiting in 75%; colonoscopy/embolisation for ongoing bleeding.

### Hirschsprung Disease (Congenital Aganglionic Megacolon)

Congenital failure of neural crest cell migration into the colon → absence of ENS ganglia (both Auerbach's and Meissner's plexus) in a variable length of distal colon (short-segment: rectosigmoid only, most common; long-segment: extends proximal) → failure of peristalsis → functional intestinal obstruction → proximal megacolon. Genetic associations: RET, EDNRB, EDN3 mutations. Presents in neonatal period (failure to pass meconium in 48 h, abdominal distension). Diagnose: suction rectal biopsy (absence of ganglion cells, hypertrophic nerve trunks, ↑AChE staining). Treat: surgical resection of aganglionic segment with pull-through procedure.

## See Also

- [Digestive System](../../07-system/digestive-system/README.md) — system-level context
- [Small Intestine](../small-intestine/README.md) — upstream; delivers ileal effluent to ileocaecal valve
- [Liver](../liver/README.md) — portal delivery of microbial metabolites; gut-liver axis
- [Immune System](../../07-system/immune-system/README.md) — colonic MALT, mucosal IgA, microbiome-Treg axis
- [Nervous System](../../07-system/nervous-system/README.md) — gut-brain axis, ENS, vagal afferents
- [Macrophage](../../04-cellular/macrophage/README.md) — lamina propria tolerogenic macrophages

[^guyton-hall]: Hall JE, Hall ME. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021.
[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019.

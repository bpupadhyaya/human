---
schema: human-scale-entry/v1
id: adipocyte
name: Adipocyte
atlas: 01-human
scale: 04-cellular
status: draft
last_reviewed: 2026-06-05
summary: "Lipid-storing mesenchymal cells in three types: white (WAT — energy storage + endocrine via leptin/adiponectin), brown (BAT — UCP1 thermogenesis), and beige (recruitable thermogenic within WAT). Central to whole-body energy and metabolic homeostasis."
aliases: ["fat cell", "lipocyte", "white adipocyte", "brown adipocyte", "beige adipocyte", "adipose cell"]
sources:
  - id: alberts-mol-cell-biology
    type: textbook
    cite: "Alberts B, Johnson A, Lewis J, et al. Molecular Biology of the Cell. 7th ed. W.W. Norton; 2022."
    url: "https://www.ncbi.nlm.nih.gov/books/NBK26880/"
    accessed: "2026-06-05"
  - id: guyton-hall
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "Adipocytes store 15–25% of body mass as triglyceride in healthy adults (up to 50%+ in obesity); WAT is the largest endocrine organ producing leptin, adiponectin, and resistin that regulate whole-body metabolism."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "Obese WAT accumulates M1 macrophages (via MCP-1/CCL2) forming crown-like structures around dead adipocytes; ↑TNF-α, IL-6, IL-1β → chronic low-grade inflammation → insulin resistance; adiponectin is anti-inflammatory."
  - target: 01-human/04-cellular/hepatocyte
    relation: modulates
    note: "Adipocyte lipolysis releases excess FFA to portal circulation → hepatic lipid accumulation → NAFLD/NASH; adipokine dysregulation (↑leptin, ↓adiponectin) promotes hepatic inflammation and stellate cell activation → fibrosis."
  - target: 01-human/03-molecular/insulin-receptor
    relation: modulates
    note: "In obesity, adipocyte-derived TNF-α and excess FFAs impair IRS-1 (Ser307 phosphorylation by JNK) → uncoupling of insulin receptor signalling → adipocyte insulin resistance → impaired GLUT4 translocation → hyperglycaemia."
  - target: 01-human/03-molecular/leptin
    relation: secretes
    note: "Adipocytes are the primary source of leptin (ob gene product); leptin signals to hypothalamic POMC/AgRP neurons via LepR to suppress appetite; leptin resistance in obesity → hyperphagia; serum leptin correlates with fat mass."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "White adipocyte hypertrophy and hyperplasia define obesity; visceral WAT dysfunction drives metabolic syndrome; adipogenesis via PPARγ/C/EBPα; crown-like structures with M1 macrophages mark obese visceral adipose tissue."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Obese WAT recruits M1 macrophages via MCP-1/CCL2 forming crown-like structures; ATMs secrete TNF-α, IL-6, IL-1β → adipocyte insulin resistance; M2-to-M1 polarisation switch in obesity drives systemic low-grade inflammation."
---

# Adipocyte

## Overview

The adipocyte is the **lipid-storing cell of adipose tissue** — a specialised mesenchymal cell capable of accumulating and mobilising triglycerides to match the body's moment-to-moment energy needs. Adipose tissue was long regarded as a passive energy depot; it is now recognised as a **major endocrine organ** that secretes dozens of bioactive factors (adipokines) that regulate appetite, insulin sensitivity, inflammation, immune function, and cardiovascular risk [^guyton-hall].

Three functionally and developmentally distinct adipocyte types exist in mammals:

| Type | Location | Primary Function | Marker |
|:---|:---|:---|:---|
| **White (WAT)** | Subcutaneous, visceral, bone marrow, ectopic | Energy storage; endocrine | Perilipin-1, Leptin, Adiponectin; unilocular LD |
| **Brown (BAT)** | Interscapular (infants/hibernators), paravertebral, perirenal (adults) | Non-shivering thermogenesis | UCP1, Cidea, Cox8b; multilocular LD |
| **Beige/Brite** | WAT depots, recruited by cold/β3-AR | Inducible thermogenesis | UCP1 (inducible), CD137, Tmem26; multilocular when active |

The balance between these three types — and particularly the browning of WAT — is an emerging target for anti-obesity therapy [^alberts-mol-cell-biology].

## Structure

### White Adipocyte Morphology

White adipocytes are among the **largest cells in the body** (80–120 µm diameter). Their architecture is dominated by a single giant lipid droplet (LD):
- **Lipid droplet**: unilocular; occupies >90% of cell volume; composed of triglycerides (TAG) surrounded by a phospholipid monolayer
- **LD coat**: **Perilipin-1 (PLIN1)** — the master LD-associated protein; controls access of lipases to TAG; phosphorylated by PKA during lipolysis
- **Cytoplasm**: thin rim (~2 µm) surrounding the LD; contains mitochondria (sparse), ER, Golgi
- **Nucleus**: peripherally displaced, often crescent-shaped

**Markers**: PLIN1+, FABP4/aP2+, vimentin+, S100+, adiponectin+, leptin+, CD36+ (fatty acid translocase)

### Brown Adipocyte Morphology

In contrast to WAT:
- **Multilocular** lipid droplets (multiple small LDs — maximise lipase access)
- **Abundant mitochondria** with dense cristae — extremely high oxidative capacity; Cytochrome c oxidase (COX) subunits highly expressed
- Rich **sympathetic (adrenergic) innervation** (β1/β3-adrenergic receptors)
- **UCP1 (thermogenin)** in the inner mitochondrial membrane (IMM) — the defining BAT protein

### Adipose Tissue Architecture

Adipocytes are embedded in a stromal vascular fraction (SVF) containing:
- **Pre-adipocytes** (undifferentiated, PDGFRβ+)
- **Adipose tissue macrophages (ATMs)** — ~10% of SVF; increase 40%+ in obesity (M1 polarisation → crown-like structures, CLSs)
- **Endothelial cells** — extensive capillary network (each adipocyte is within ~2 cell diameters of a capillary)
- **Sympathetic nerve fibres** — innervate BAT extensively; sparse in WAT
- **Mast cells, T cells, ILC2s** — regulate adipose tissue inflammation and browning

## Function

### 1. Lipid Storage and Lipolysis — Energy Buffering

**Lipogenesis / Triglyceride storage (fed state, insulin-dominant):**

1. **Insulin** → IRS-1/PI3K/Akt → **GLUT4 translocation** (glucose uptake) → glycolysis → G-3-P (glycerol backbone)
2. **LPL** (lipoprotein lipase, on capillary endothelium, activated by insulin) → cleaves circulating VLDL and chylomicron TAGs → FFA release → **CD36/FATP4** uptake by adipocyte
3. **De novo lipogenesis** (minor in humans vs. rodents): ChREBP (glucose-sensing) + SREBP1c (insulin-sensing) → FASN (fatty acid synthase), ACC (acetyl-CoA carboxylase) → palmitate → elongation/desaturation
4. **TAG synthesis**: FFA + G-3-P → DAG (DGAT1 or DGAT2 final step) → TAG → incorporated into LD under PLIN1 coat

**Lipolysis (fasted/stressed state, catecholamine-dominant):**

1. β1/β3-AR stimulation (catecholamines, glucagon, natriuretic peptides, growth hormone) → Gs → **cAMP** → **PKA** activation
2. PKA phosphorylates **PLIN1** (Ser492/522) → releases CGI-58/ABHD5 from PLIN1 → CGI-58 co-activates **ATGL** (adipose triglyceride lipase) → TAG → DAG
3. PKA also phosphorylates **HSL** (hormone-sensitive lipase, Ser563/660) → active HSL translocates to LD → DAG → MAG
4. **MGL** (monoacylglycerol lipase, constitutively active) → MAG → glycerol + FFA
5. Products: **3 FFAs + glycerol** per TAG → FFA bound to albumin → transport to liver, muscle, heart for oxidation

**Insulin anti-lipolytic mechanism**: Insulin → IRS-1/PI3K/Akt → **PDE3B** (phosphodiesterase 3B) activation → ↓cAMP → ↓PKA → restores PLIN1 coat → ↓lipolysis [^guyton-hall].

### 2. BAT Thermogenesis — UCP1-Mediated Proton Leak

Cold exposure or β3-AR agonism → cAMP → PKA → lipolysis (to fuel thermogenesis) + **UCP1 activation**:

UCP1 is a **proton transporter** in the IMM: H⁺ re-enters the mitochondrial matrix via UCP1 (bypassing ATP synthase) → dissipates the proton-motive force as **heat** rather than ATP. This is activated by long-chain fatty acids (released by lipolysis) and inhibited by purine nucleotides (GDP, ADP — competitive antagonists).

Net effect: mitochondrial respiration continues at maximal rate, uncoupled from ATP synthesis → heat generation of up to 300 W/kg BAT (most thermogenic tissue in the body) [^alberts-mol-cell-biology].

**Beige adipocyte thermogenesis**: Cold, β3-AR agonists (mirabegron), FGF21, irisin (FNDC5, muscle-secreted) → **browning** (beiging) of WAT — upregulation of UCP1, PGC-1α, Cidea, Cpt1b in existing or newly differentiated beige cells. Less powerful than classical BAT but a realistic therapeutic target.

### 3. Endocrine Functions — Adipokines

The adipocyte secretome (>600 proteins) orchestrates systemic metabolism:

**Leptin (167 aa; LEP gene; ob/ob mouse gene)**:
- Secreted proportional to fat mass (WAT >> BAT); ↑after feeding, ↓fasting
- Binds LepRb (long form) in hypothalamic arcuate nucleus → JAK2/STAT3 → ↓AgRP/NPY (orexigenic) + ↑POMC/CART (anorexigenic) → **satiety + ↑energy expenditure**
- Leptin resistance in obesity: hyperleptinemia with impaired signalling (ER stress, SOCS3, SHIP2 mechanisms)
- Pro-inflammatory at high concentrations; ↑sympathetic tone; angiogenic (VEGF-like effects)

**Adiponectin (collagen-domain protein, acrp30/ADIPOQ)**:
- Most abundant adipokine (~5–10 µg/mL plasma); paradoxically **inversely correlated with fat mass**
- Trimeric/hexameric/HMW forms; signals via AdipoR1 (muscle → AMPK) and AdipoR2 (liver → PPARα)
- Effects: ↑FA oxidation (AMPK → ACC phosphorylation → ↓malonyl-CoA → ↑CPT1 → FAO), ↓gluconeogenesis (liver), ↑insulin sensitivity; **anti-inflammatory** (↓NF-κB, ↑IL-10)
- ↓in obesity, T2DM, MetSyn; ↑with exercise, caloric restriction, TZDs (PPARγ agonists)

**Resistin** (rodents: adipocyte-derived; humans: primarily macrophage-derived in adipose tissue):
- Pro-inflammatory; impairs insulin signalling via TLR4/serine kinase cascades

**Inflammatory adipokines (in obesity)**:
- **CCL2/MCP-1**: monocyte chemoattractant → ATM infiltration
- **CXCL5**: neutrophil chemoattractant
- **TNF-α, IL-6, IL-1β**: secreted by adipocyte-associated macrophages (ATMs) → systemic insulin resistance
- **PAI-1**: plasminogen activator inhibitor-1 → prothrombotic; elevated in visceral obesity

### 4. Metabolic Crosstalk with Other Tissues

| Target | Signal | Consequence |
|:---|:---|:---|
| Liver | ↑portal FFA, ↓adiponectin, ↑leptin | NAFLD, gluconeogenesis, VLDL overproduction |
| Muscle | ↑FFA, ↓adiponectin | Lipotoxicity, ↓GLUT4, mitochondrial dysfunction |
| Pancreas | ↑FFA (lipotoxicity), ↑IL-1β, leptin | β-cell dysfunction → T2DM progression |
| Heart | ↑FFA, epicardial adipose tissue (EAT) paracrine | Lipotoxic cardiomyopathy, atrial fibrillation |
| Brain | Leptin, adiponectin, FFA | Satiety, neuroinflammation, cognitive function |

## Lifecycle

### Adipogenesis — Differentiation Programme

Adipogenesis proceeds from mesenchymal progenitors through a committed pre-adipocyte stage to the mature lipid-laden adipocyte. The transcriptional programme is among the best understood in cell biology [^alberts-mol-cell-biology]:

**Stage 1 — Growth arrest and early induction**: C/EBPβ and C/EBPδ (early response TFs, induced within hours of adipogenic stimulus by insulin/glucocorticoid/IBMX) → activate **PPARγ** and **C/EBPα**

**Stage 2 — Master TF activation**:
- **PPARγ** (PPARG; nuclear receptor) = the **master regulator of adipogenesis**: obligatory for all adipocyte differentiation; activated by natural ligands (PUFAs, 15d-PGJ₂) and pharmacological agonists (thiazolidinediones — rosiglitazone, pioglitazone)
- **C/EBPα** — reinforces PPARγ via positive feedback; drives insulin-sensitive glucose metabolism

**Terminal differentiation targets**: FABP4 (aP2), ADIPOQ, LEP, LPL, PLIN1, SCD1, FASN, GLUT4 — full adipocyte phenotype established within 7–10 days in vitro

**Suppressors of adipogenesis**: Wnt/β-catenin (inhibits C/EBPα/PPARγ), Pref-1/DLK1, GATA2/3, KLF2 — maintain pre-adipocyte state

**BAT specification**: PRDM16 + PPARγ + PGC-1α → brown adipocyte fate; BMP7 (activates PRDM16), β3-AR/cAMP → PGC-1α → mitochondrial biogenesis, UCP1 transcription (via PGC-1α/PPAR response element in UCP1 enhancer)

### Adipocyte Turnover

White adipocytes turn over slowly: **~10% replaced per year** in adult humans (²H-labelled water studies). Visceral adipocytes turn over faster than subcutaneous. In obesity, turnover rate increases but is outpaced by hypertrophy and hyperplasia.

Cell death: **adipocyte death** (mechanical failure of hypertrophied cells, ER stress, lipotoxicity) releases a lipid-rich debris → ATM infiltration → crown-like structures (CLSs) → ATMs attempt to clear lipid → frustrated phagocytosis → pro-inflammatory activation [^guyton-hall].

## Connections

- **Part of** human body [→ human-body](../../08-whole-body/human-body/README.md): Adipocytes store 15–25% of body mass as triglyceride in healthy adults (up to 50%+ in obesity); WAT is the largest endocrine organ producing leptin, adiponectin, and resistin that regulate whole-body metabolism.
- **Modulates** immune system [→ immune-system](../../07-system/immune-system/README.md): Obese WAT accumulates M1 macrophages (via MCP-1/CCL2) forming crown-like structures around dead adipocytes; ↑TNF-α, IL-6, IL-1β → chronic low-grade inflammation → insulin resistance; adiponectin is anti-inflammatory.
- **Modulates** hepatocyte [→ hepatocyte](../../04-cellular/hepatocyte/README.md): Adipocyte lipolysis releases excess FFA to portal circulation → hepatic lipid accumulation → NAFLD/NASH; adipokine dysregulation (↑leptin, ↓adiponectin) promotes hepatic inflammation and stellate cell activation → fibrosis.
- **Modulates** insulin receptor [→ insulin-receptor](../../03-molecular/insulin-receptor/README.md): In obesity, adipocyte-derived TNF-α and excess FFAs impair IRS-1 (Ser307 phosphorylation by JNK) → uncoupling of insulin receptor signalling → adipocyte insulin resistance → impaired GLUT4 translocation → hyperglycaemia.
- **Secretes** leptin [→ leptin](../../03-molecular/leptin/README.md): Adipocytes are the primary source of leptin (ob gene product); leptin signals to hypothalamic POMC/AgRP neurons via LepR to suppress appetite; leptin resistance in obesity drives hyperphagia; serum leptin correlates with body fat mass.
- **Connects to** obesity [→ obesity](../../07-system/obesity/README.md): White adipocyte hypertrophy and hyperplasia define obesity; visceral WAT dysfunction drives metabolic syndrome via adipokine dysregulation; adipogenesis proceeds via PPARγ/C/EBPα; crown-like structures with M1 macrophages mark obese visceral adipose tissue.
- **Connects to** macrophage [→ macrophage](../../04-cellular/macrophage/README.md): Obese WAT recruits M1 macrophages via MCP-1/CCL2 forming crown-like structures; adipose tissue macrophages (ATMs) secrete TNF-α, IL-6, IL-1β → adipocyte insulin resistance; M2-to-M1 polarisation switch in obesity drives systemic low-grade inflammation.

## Pathology

| Condition | Mechanism | Key Features |
|:---|:---|:---|
| **Obesity** | Adipocyte hypertrophy + hyperplasia → hypoxia, death, ATM infiltration → adipokine dysregulation | CVD risk, T2DM, NASH, OSA, cancer risk; visceral > subcutaneous fat for metabolic risk |
| **Metabolic syndrome** | Central adiposity → ↑FFA, ↑TNF-α, ↓adiponectin, ↑PAI-1 | Dyslipidaemia, hypertension, impaired fasting glucose, ↑waist circumference |
| **Lipodystrophy (congenital)** | AGPAT2, BSCL2 (seipin), PPARG mutations → absent adipose tissue | Severe insulin resistance, hypertriglyceridaemia, fatty liver — paradoxically metabolically dangerous despite low BMI |
| **HIV/ART lipodystrophy** | Protease inhibitors, NRTIs → mitochondrial dysfunction, adipogenesis suppression | Peripheral fat loss (lipoatrophy) + central fat accumulation; dyslipidaemia, insulin resistance |
| **Liposarcoma** | Well-differentiated (WDLS) / Dedifferentiated (DDLS): MDM2+CDK4 amplification (chromosome 12q13-15) | Most common soft tissue sarcoma in adults; retroperitoneal and extremity locations |
| **Brown adipose tissue hypofunction** | Ageing, obesity → BAT involution, ↓UCP1, ↓sympathetic innervation | ↑susceptibility to cold; ↓energy expenditure contribution; therapeutic activation target |
| **Adipose inflammation → T2DM** | Obesity → ATM activation → TNF-α/IL-1β/IL-6 → IRS-1 serine phosphorylation → adipocyte and systemic insulin resistance | Progressive β-cell failure → overt T2DM; partially reversible with weight loss |

## See Also

- [Hepatocyte](../../04-cellular/hepatocyte/README.md) — primary recipient of adipocyte-released FFAs via portal circulation; lipotoxic crosstalk drives NAFLD/NASH
- [Insulin Receptor](../../03-molecular/insulin-receptor/README.md) — adipocyte GLUT4 translocation and anti-lipolysis depend on intact insulin receptor/IRS-1/PI3K/Akt signalling
- [Macrophage](../../04-cellular/macrophage/README.md) — adipose tissue macrophages regulate adipocyte homeostasis, fibrosis, and inflammation; M1/M2 balance determines adipose health
- [Human Body](../../08-whole-body/human-body/README.md) — whole-body energy balance is regulated by adipocyte-derived leptin and adiponectin acting on central and peripheral tissues
- [IL-6](../../03-molecular/il-6/README.md) — produced by adipose tissue macrophages in obesity; central mediator of adipose-driven systemic inflammation and hepatic acute-phase response

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

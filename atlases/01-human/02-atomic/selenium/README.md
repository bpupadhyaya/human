---
schema: human-scale-entry/v1
id: selenium
name: Selenium
atlas: 01-human
scale: 02-atomic
status: draft
last_reviewed: 2026-06-05
summary: "Selenium (Se, atomic number 34) — 13–20 mg total; selenocysteine in ~25 selenoproteins: GPx (antioxidant), thioredoxin reductase (redox homeostasis), and deiodinases (T4→T3). Deficiency causes Keshan cardiomyopathy, hypothyroidism, and impaired immune function."
aliases: ["Se", "selenocysteine", "Sec", "selenoprotein", "selenium-78"]
sources:
  - id: stryer-biochemistry
    type: textbook
    cite: "Berg JM, Tymoczko JL, Stryer L. Biochemistry. 9th ed. W.H. Freeman; 2019."
    url: "https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X"
    accessed: "2026-06-05"
  - id: guyton-hall
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
  - id: labunskyy-selenoproteins
    type: peer-reviewed
    cite: "Labunskyy VM, Hatfield DL, Gladyshev VN. Selenoproteins: molecular pathways and physiological roles. Physiol Rev. 2014;94(3):739-77."
    doi: "10.1152/physrev.00039.2013"
    pmid: "24987004"
    url: "https://doi.org/10.1152/physrev.00039.2013"
  - id: papp-gpx4-ferroptosis
    type: peer-reviewed
    cite: "Forcina GC, Dixon SJ. GPX4 at the crossroads of lipid peroxidation and ferroptosis. Proteomics. 2019;19(18):e1800311."
    doi: "10.1002/pmic.201800311"
    pmid: "30924297"
    url: "https://doi.org/10.1002/pmic.201800311"
cross_links:
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "13–20 mg total Se; incorporated as selenocysteine (Sec) in ~25 selenoproteins essential for GPx antioxidant defence, thyroid hormone activation by deiodinases, and sperm mitochondrial function."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "Selenoprotein thioredoxin reductase and GPx protect immune cells from oxidative damage during the respiratory burst; selenium deficiency impairs T-cell proliferation and NK cell cytotoxicity."
  - target: 01-human/04-cellular/hepatocyte
    relation: modulates
    note: "Liver synthesises selenoprotein P (main Se transport protein, 10 Sec residues), TrxR1 (cytosolic antioxidant), and GPx1; hepatocytes are the primary source of circulating selenium in plasma."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "DIO1, DIO2, and DIO3 (all selenocysteine-containing) catalyse reductive deiodination: DIO2 converts T4→T3 in brain, pituitary, and brown fat; DIO3 inactivates T3→T2 in fetal tissue; Se deficiency impairs DIO activity → functional hypothyroidism despite adequate iodine intake."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: connects-to
    note: "DIO1 and DIO2 (selenocysteine active site) provide ~80% of circulating T3 by peripheral T4 5′-deiodination; DIO2 in pituitary suppresses TSH via negative feedback; DIO3 inactivates T3 in fetal tissues; Se deficiency → impaired T3 production → functional hypothyroidism."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "Keshan disease (Se-deficient China) is dilated cardiomyopathy caused by GPx4/TrxR2 deficiency, with Coxsackievirus B as co-factor; GPx4 prevents ferroptosis by reducing lipid hydroperoxides; TrxR2 (selenoprotein, mitochondrial) maintains cardiomyocyte redox homeostasis."
---

# Selenium

## Overview

Selenium (symbol Se, atomic number 34) is a **metalloid** in Group 16 of the periodic table, with atomic mass 78.97 u and electron configuration [Ar] 3d¹⁰ 4s² 4p⁴. Chemically similar to sulfur — with which it shares the same group and comparable electronegativity — selenium replaces sulfur in specific biological contexts with markedly superior catalytic properties. The most important manifestation of this is **selenocysteine (Sec, single-letter code U)**, the 21st canonical amino acid, which replaces cysteine in the active sites of approximately **25 human selenoproteins** [^labunskyy-selenoproteins].

The human body contains approximately **13–20 mg of selenium**, an amount that varies considerably with geography and diet because soil selenium concentration — and therefore plant/animal food content — spans a 1000-fold range globally (selenium-deficient soils in Finland, China [Keshan], and New Zealand vs. selenium-rich Great Plains in the USA). Plasma selenium in selenium-replete individuals is **70–150 µg/L**. The liver, kidney, thyroid, muscle, and testes have the highest tissue concentrations, reflecting the importance of selenoproteins in these organs [^guyton-hall].

Selenium occupies a unique biological niche at the intersection of **antioxidant defence** and **thyroid hormone metabolism** — two seemingly unrelated systems that share the common requirement for redox-active catalysis.

## Structure

### Atomic Properties

| Property | Value |
|:---|:---|
| Atomic number (Z) | 34 |
| Atomic mass | 78.97 u |
| Electron configuration | [Ar] 3d¹⁰ 4s² 4p⁴ |
| Biological forms | Selenocysteine (Sec); selenomethionine (unspecific Se incorporation); selenite/selenate (dietary inorganic) |
| Ionic radius (Se²⁻) | 0.198 nm |
| pKa of selenocysteine | 5.2 (vs. Cys pKa ~8.3) → selenolate anion (Se⁻) predominates at pH 7.4 |
| Electronegativity (Pauling) | 2.55 |

### Selenocysteine: The 21st Amino Acid

Selenocysteine (Sec, U) is structurally identical to cysteine but with selenium replacing sulfur in the side chain:

- **Chemical formula:** HOCH₂CH(NH₂)COOH → HSeCSH₂CH(NH₂)COOH (selenol group –CH₂–SeH vs. thiol –CH₂–SH)
- **Reactivity:** The low pKa of 5.2 means that at physiological pH (7.4), Sec exists almost entirely as the **selenolate anion (–CH₂–Se⁻)** — a far more reactive nucleophile than the Cys thiolate (pKa 8.3, ~1% ionised at pH 7.4). This 1000-fold increase in nucleophilicity at physiological pH explains why selenoproteins are vastly more catalytically efficient than their sulfur (Cys) homologues.
- **Genetic encoding:** Sec is encoded by the **UGA codon** (normally a stop codon) via a specialised recoding mechanism. It requires:
  - A **SECIS (Selenocysteine Insertion Sequence) element** in the 3' UTR of the mRNA (stem-loop structure with critical AUGA and AAAR sequences)
  - **SECIS-BP2** (SBP2): binds SECIS element and recruits the Sec-specific elongation factor EFSec
  - **SepSecS** (O-phosphoseryl-tRNA[Sec] selenium transferase): converts phosphoseryl-tRNA[Sec] → Sec-tRNA[Sec]
  - **Selenophosphate (H₂SePO₃⁻)**: active selenium donor, synthesised from selenide by SPS2 (a selenoprotein itself)

This elaborate recoding machinery is unique to selenoproteins and has no equivalent in any other amino acid insertion system.

## Function

### The Human Selenoproteome: 25 Proteins

| Family | Members | Selenocysteine role | Key function |
|:---|:---|:---|:---|
| **Glutathione peroxidases (GPx)** | GPx1–4, GPx6 | Sec in active site; catalyses 2 GSH + ROOH → GSSG + H₂O + ROH | Reduce H₂O₂ and lipid hydroperoxides |
| **Thioredoxin reductases (TrxR)** | TrxR1, TrxR2, TGR | Sec at C-terminus (penultimate residue); reduces Trx via NADPH | Broad redox homeostasis |
| **Iodothyronine deiodinases (DIO)** | DIO1, DIO2, DIO3 | Sec in active site attacks iodine-carbon bond | Thyroid hormone activation/inactivation |
| **Selenoprotein P (SePP1)** | SELENOP | 10 Sec residues per molecule | Se transport protein; plasma Se reservoir |
| **Selenoprotein W** | SELENOW | Sec + redox motif | Muscle function (exact role unclear) |
| **Sep15/SELENOF** | SELENOF | Sec; ER-resident | Glycoprotein quality control/folding |
| **Methionine sulfoxide reductase B1** | MSRB1 | Sec | Repair of oxidised methionine residues |
| **Selenoprotein M** | SELENOM | Sec; ER-resident | Ca²⁺ homeostasis; neuroprotection |
| **Selenoprotein N** | SELENON | Sec; ER membrane | Muscle development; ryanodine receptor regulation |

#### GPx1 (Ubiquitous Cytosolic GPx)
The most abundant selenoprotein; reduces **H₂O₂** and soluble hydroperoxides using reduced **glutathione (GSH)** as the electron donor:
> 2 GSH + H₂O₂ → GSSG + 2 H₂O

GSSG is regenerated by **glutathione reductase** using NADPH (from the pentose phosphate pathway), completing the antioxidant cycle. GPx1 knockout mice are fertile and viable but more susceptible to oxidative stress (paraquat, viral infection) [^labunskyy-selenoproteins].

#### GPx4 (Phospholipid Hydroperoxide Glutathione Peroxidase)
GPx4 is unique and irreplaceable: it is the **only enzyme capable of reducing phospholipid hydroperoxides directly within the membrane bilayer** — a task inaccessible to GPx1 and catalase because their substrates must be water-soluble. GPx4 prevents the accumulation of oxidised phospholipids that would otherwise cause **ferroptosis** (an iron-dependent, non-apoptotic cell death characterised by overwhelming lipid peroxidation) [^papp-gpx4-ferroptosis].

Ferroptosis is relevant in:
- Cancer: GPx4 inhibitors (RSL3, ML-210) induce ferroptosis selectively in cancer cells with high oxidative stress
- Neurodegeneration: GPx4 protects neurons from lipid peroxidation; reduced GPx4 observed in Alzheimer and Parkinson disease
- Ischaemia-reperfusion injury: restoration of O₂ generates reactive oxygen species that cause lipid peroxidation — GPx4 is a gatekeeper

GPx4 knockout is **embryonic lethal** in mice (unlike GPx1 knockout), underscoring its non-redundant physiological role.

#### Thioredoxin Reductases (TrxR1, TrxR2, TGR)
TrxRs are FAD-containing homodimeric enzymes with Sec at the C-terminus (penultimate position in a –Gly-Cys-Sec-Gly– C-terminal extension). Unlike most selenium-containing enzymes, TrxR can utilise **diverse substrates** beyond thioredoxin, including:
- Dehydroascorbate (vitamin C recycling)
- Lipoic acid (mitochondrial antioxidant)
- H₂O₂ directly (modest rate)
- Ebselen (pharmaceutical seleno-organic compound)

TrxR1 (cytosolic/nuclear) and TrxR2 (mitochondrial) are essential for maintaining the **thioredoxin system** — the major alternative to the glutathione system for cellular redox homeostasis. TrxR2 knockout is embryonic lethal in mice, indicating its indispensability for mitochondrial function.

#### Iodothyronine Deiodinases (DIO1–3)

The deiodinases use Sec to catalyse the **reductive deiodination** of thyroid hormone molecules — the breaking of a strong C–I bond by a selenolate nucleophile. The reaction sequence:
> Sec-SeH + T4-I (outer ring) → Sec-SeI + T3 (or rT3) → Sec-Se⁻ regenerated by thioredoxin/DTT

| Deiodinase | Selenocysteine | Location | Activity | Net effect |
|:---|:---:|:---|:---|:---|
| DIO1 | Yes | Liver, kidney, thyroid | 5' and 5 deiodination | Generates circulating T3; also inactivates T3→T2 |
| DIO2 | Yes | Brain, pituitary, BAT, heart, placenta | 5' only | Local T3 production for tissue use; pituitary TSH feedback |
| DIO3 | Yes | Brain, placenta, fetal liver, skin | 5 only | T4→rT3 (inactivation); T3→T2 (inactivation); fetal protection from excessive T3 |

#### Selenoprotein P (SePP1/SELENOP)
Selenoprotein P is the major plasma **selenium transport protein**, synthesised almost exclusively in the liver. It contains **10 selenocysteine residues** per molecule — the highest Sec content of any mammalian protein — and its expression is the most sensitive molecular indicator of selenium status (its synthesis is prioritised over GPx1 under conditions of Se deficiency). SePP1 delivers Se to the brain via megalin (LRP2)-mediated endocytosis, and to the testes via a distinct receptor (LRP8/ApoER2). Mice lacking SePP1 develop neurological deficits (ataxia, seizures) despite normal plasma selenium, demonstrating that SePP1 is specifically required for brain Se delivery [^labunskyy-selenoproteins].

### Selenium and Thyroid Metabolism

The thyroid has the **highest selenium concentration per gram** of any organ (~0.2–1 µg/g wet weight). Thyroid function requires selenium at two levels:
1. **DIO1 and DIO2** for T4 → T3 conversion (~80% of circulating T3 comes from peripheral deiodination by DIO1)
2. **GPx** and **TrxR** to neutralise the H₂O₂ generated continuously by DUOX2 for iodine oxidation (TPO reaction). Without adequate GPx/TrxR, H₂O₂ accumulates and damages thyrocytes — particularly critical during high iodine intake when DUOX2 is maximally active

This dual dependency explains why combined iodine + selenium deficiency (endemic in parts of Central Africa) produces **myxoedematous cretinism** — more severe than iodine deficiency alone.

### Selenium and Ferroptosis Prevention

GPx4 is the critical gatekeeper against ferroptosis:
- Labile iron (Fe²⁺) reduces lipid hydroperoxides to lipid alkoxy radicals (LOO•) via Fenton-like chemistry → chain reaction of lipid peroxidation → membrane disruption → cell death
- GPx4-Sec reduces phospholipid-OOH → phospholipid-OH, stopping the chain reaction
- Selenium deficiency reduces GPx4 activity → increased ferroptosis susceptibility
- GPx4 inhibitors (RSL3) are explored as cancer therapeutics exploiting ferroptosis

## Connections

- `part-of` → **[Human Body](../../08-whole-body/human-body/README.md)** — 13–20 mg total Se; incorporated as selenocysteine in ~25 selenoproteins essential for GPx antioxidant defence (GPx1–4), thyroid hormone activation (DIO1–3), and sperm mitochondrial integrity (GPx4, TGR).
- `modulates` → **[Immune System](../../07-system/immune-system/README.md)** — selenoprotein TrxR and GPx protect immune cells from ROS during the respiratory burst; Se deficiency impairs T-cell proliferation, NK cell cytotoxicity, and antiviral responses; Se status inversely correlates with HIV progression.
- `modulates` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — liver synthesises selenoprotein P (main circulating Se transporter, 10 Sec residues), cytosolic TrxR1, and GPx1; hepatocytes are the primary source of plasma selenium and the hub for Se distribution to other organs.
- `connects-to` → **[Iodine](../iodine/README.md)** — DIO1/2/3 (selenocysteine-containing) catalyse reductive deiodination: DIO2 converts T4→T3 in brain, pituitary, and BAT; DIO3 inactivates T3 in fetal tissues; Se deficiency → impaired DIO activity → functional hypothyroidism despite adequate iodine intake.
- `connects-to` → **[Thyroid Hormones](../../03-molecular/thyroid-hormones/README.md)** — DIO1/2 (selenocysteine active site) provide ~80% of circulating T3 by peripheral T4 5′-deiodination; DIO2 in pituitary suppresses TSH via negative feedback; DIO3 inactivates T3 in fetal tissues; Se deficiency → impaired T3 production.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — Keshan disease (Se-deficient China) is dilated cardiomyopathy caused by GPx4/TrxR2 deficiency, with Coxsackievirus B as co-factor; GPx4 prevents ferroptosis; TrxR2 (mitochondrial selenoprotein) maintains cardiomyocyte redox homeostasis.

## Pathology

### Keshan Disease (Selenium Deficiency Cardiomyopathy)

**Keshan disease** is an endemic **dilated cardiomyopathy** first described in the Keshan county of Heilongjiang province, China, where soil selenium content is <0.1 mg/kg. Affected individuals develop acute or chronic cardiomyopathy with arrhythmias and sudden cardiac death; children and women of reproductive age are most vulnerable. A **Coxsackievirus B** co-factor has been identified — Se-deficient hosts support more virulent viral strains because antioxidant defences are insufficient to limit viral mutagenesis. Prophylactic oral sodium selenite dramatically reduced incidence in the Keshan county program of the 1970s–80s, providing the definitive proof of Se's essentiality.

### Kashin-Beck Disease

**Kashin-Beck disease** is an osteoarthropathy characterised by articular cartilage necrosis, deformity of multiple joints, and growth retardation in children. Endemic in a broad band from Siberia through North Korea, northern China, and Tibet — all areas of combined Se and iodine deficiency. The exact mechanism is debated but involves impaired antioxidant defence in chondrocytes and possibly contamination of grain by Fusarium mycotoxins.

### Selenium Status and Disease Risk

| Condition | Se–disease relationship | Evidence level |
|:---|:---|:---|
| **Thyroid dysfunction** | Se deficiency impairs DIO activity and increases thyroid H₂O₂ damage; autoimmune thyroiditis associated with low Se | Observational + RCT (Hashimoto TPO-Ab) |
| **Male infertility** | GPx4 is essential for sperm mid-piece integrity (mitochondria sheath); TGR (thioredoxin-glutathione reductase) required for sperm motility | KO mouse studies; observational human |
| **Cancer prevention** | NPC trial (1996): 200 µg/day Se → reduced total cancer mortality; subsequent SELECT trial (2001–2008): Se did NOT prevent prostate cancer; excess Se harmful | Conflicting RCT evidence |
| **Selenosis (toxicity)** | >400 µg/day chronic intake → garlic breath (dimethylselenide), alopecia, nail brittleness, peripheral neuropathy | Observed in Se-rich areas (North Dakota) and high-dose supplement users |
| **Neurodegeneration** | SePP1 knockout: ataxia, seizures — brain most vulnerable to Se deficiency; low SePP1 in Alzheimer disease CSF | Animal models + observational |

### Selenium in Therapeutics

- **Sodium selenite (IV):** used in selenoprotein-depleted ICU patients (Se lost in plasma during critical illness); RCTs show modest benefit in some sepsis outcomes
- **Ebselen:** seleno-organic GPx mimetic; investigated for radioprotection, stroke, COVID-19 (SARS-CoV-2 3CL protease inhibitor in silico), and hearing loss
- **High-dose Se supplementation:** not recommended in Se-replete populations; SELECT trial established no prostate cancer benefit and possible harm at 200 µg/day

## See Also

- [Iodine](../../02-atomic/iodine/README.md) — selenium deiodinases activate thyroid hormones; combined deficiency causes myxoedematous cretinism.
- [Hepatocyte](../../04-cellular/hepatocyte/README.md) — liver synthesises selenoprotein P and distributes selenium systemically.
- [Immune system](../../07-system/immune-system/README.md) — selenium-dependent antioxidant selenoproteins protect immune cells.

[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019. [macmillanlearning.com](https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X)
[^guyton-hall]: Hall JE, Hall ME. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021. [elsevier.com](https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8)
[^labunskyy-selenoproteins]: Labunskyy VM, Hatfield DL, Gladyshev VN. Selenoproteins: molecular pathways and physiological roles. *Physiol Rev.* 2014;94(3):739-77. [doi:10.1152/physrev.00039.2013](https://doi.org/10.1152/physrev.00039.2013) · [PubMed 24987004](https://pubmed.ncbi.nlm.nih.gov/24987004/)
[^papp-gpx4-ferroptosis]: Forcina GC, Dixon SJ. GPX4 at the crossroads of lipid peroxidation and ferroptosis. *Proteomics.* 2019;19(18):e1800311. [doi:10.1002/pmic.201800311](https://doi.org/10.1002/pmic.201800311) · [PubMed 30924297](https://pubmed.ncbi.nlm.nih.gov/30924297/)

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

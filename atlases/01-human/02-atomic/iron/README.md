---
schema: human-scale-entry/v1
id: iron
name: Iron
atlas: 01-human
scale: 02-atomic
status: draft
last_reviewed: 2026-06-05
summary: "Iron (Fe, Z=26, [Ar] 3d⁶ 4s²). ~3.5–4.5g total; 70% in haemoglobin Fe²⁺-haem (O₂ transport), 20% stored as ferritin/haemosiderin, 5% myoglobin/enzymes. Regulated by hepcidin. Most common nutritional deficiency worldwide."
aliases: ["Fe", "Fe2+", "Fe3+", "ferrous iron", "ferric iron", "haem iron"]
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
cross_links:
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "3.5–4.5g total; ~70% in haemoglobin Fe²⁺-haem, ~20% stored as ferritin/haemosiderin in liver/spleen/marrow, ~5% in myoglobin and enzymes (cytochromes, catalase)."
  - target: 01-human/04-cellular/erythrocyte
    relation: part-of
    note: "Each erythrocyte contains ~280 million haemoglobin tetramers each holding 4 haem-Fe²⁺ groups; iron is recycled by macrophages after RBC senescence at the end of the ~120-day erythrocyte lifespan."
  - target: 01-human/06-organ/liver
    relation: modulates
    note: "Liver is primary iron storage organ (ferritin/haemosiderin in hepatocytes) and synthesises hepcidin (iron-regulatory hormone) and transferrin (plasma iron transport protein)."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "Iron is required for lymphocyte proliferation (ribonucleotide reductase for dNTP synthesis); hepcidin-mediated iron sequestration from pathogens constitutes nutritional immunity in chronic infection/inflammation."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Iron loading (BMP6-SMAD) and inflammation (IL-6 → STAT3) upregulate hepcidin → hepcidin binds ferroportin → ferroportin internalisation → reduced Fe export from enterocytes and macrophages → falling serum iron; hepcidin suppression in deficiency/hypoxia restores Fe absorption."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Iron-deficiency anaemia (IDA) is the most common nutritional deficiency (~2 billion globally): inadequate intake, chronic blood loss (GI, menstrual), or malabsorption → depleted ferritin → hypochromic microcytic anaemia; serum Fe low, TIBC high; treated with oral or IV iron."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Haemoglobin Fe²⁺ reversibly binds O₂ (each Hb tetramer carries 4); cooperative binding (Hill n~2.8) enables loading in lungs (PO₂ 100 mmHg) and unloading in tissues (PO₂ 40 mmHg); Fe³⁺ (methaemoglobin) cannot bind O₂ → O₂ transport wholly depends on iron oxidation state."
---

# Iron

## Overview

Iron (symbol Fe, from Latin *ferrum*, atomic number 26, atomic mass 55.85 u) is a transition metal in Group 8 of the periodic table, with ground-state electron configuration [Ar] 3d⁶ 4s². It is the **most abundant transition metal in the human body**, with a total content of approximately **3.5–4.5 g** in a healthy 70 kg adult. Iron's biological importance is rooted in the redox chemistry of its two stable ionic states: **Fe²⁺ (ferrous, reduced)** and **Fe³⁺ (ferric, oxidised)** — a single-electron redox couple that sits at a potential (~+0.77 V for free Fe²⁺/Fe³⁺, but tunable from −0.4 V to +0.35 V by protein coordination) ideally suited to mitochondrial electron transfer, O₂ binding, and oxidative catalysis [^stryer-biochemistry].

The dual identity of iron — indispensable for O₂ delivery and electron transport, yet potentially toxic through the Fenton reaction (Fe²⁺ + H₂O₂ → Fe³⁺ + OH• + OH⁻) — means that virtually every aspect of iron metabolism is tightly regulated: absorption in the duodenum, storage in ferritin, release from macrophages, plasma transport by transferrin, and intracellular use are all controlled by an integrated hormonal and post-transcriptional network centred on **hepcidin** and **iron regulatory proteins (IRPs)** [^guyton-hall].

## Structure

### Atomic Properties

| Property | Value |
|:---|:---|
| Atomic number (Z) | 26 |
| Atomic mass | 55.85 u |
| Electron configuration | [Ar] 3d⁶ 4s² |
| Common ionic forms | Fe²⁺ (ferrous), Fe³⁺ (ferric) |
| Standard redox potential (Fe²⁺/Fe³⁺) | +0.77 V (aqueous; highly protein-tunable) |
| Ionic radius | 78 pm (Fe²⁺ high-spin), 64 pm (Fe³⁺) |

### Haem — the Iron Porphyrin

The dominant biological iron complex is **haem b** (protoporphyrin IX + Fe²⁺): a planar macrocycle of four pyrrole rings linked by methine bridges, with the iron coordinated in the centre by four porphyrin nitrogens (equatorial ligands). The fifth and sixth axial positions are available for:

- **Protein coordination** (His proximal in globins, Cys in P450 cytochromes, His-Met in cytochrome c)
- **Ligand binding** (O₂ in haemoglobin/myoglobin; CO as inhibitor)

The protein environment around the haem dramatically modulates Fe²⁺/Fe³⁺ redox potential and O₂ affinity — the same iron-porphyrin core has P₅₀ ~1 mmHg in myoglobin (high affinity) vs. ~26 mmHg in haemoglobin (tuned for O₂ delivery), and the cytochrome b₅₆₂ redox potential is shifted 800 mV from free haem by protein interactions.

### Body Iron Distribution

| Pool | Fraction | Amount | Form |
|:---|:---|:---|:---|
| Haemoglobin (erythrocytes) | ~70% | ~2.5–3 g | Fe²⁺ in 4 haem groups per Hb tetramer |
| Storage (liver, spleen, marrow) | ~20% | ~0.8–1 g | Ferritin (soluble) and haemosiderin (insoluble) |
| Myoglobin (skeletal/cardiac muscle) | ~5% | ~0.15–0.3 g | Fe²⁺ in single haem |
| Tissue enzymes | ~4% | ~0.1–0.2 g | Cytochromes (a, b, c, P450), catalase, ribonucleotide reductase |
| Plasma (transferrin-bound) | ~0.1% | ~3–4 mg | Fe³⁺ on transferrin (two sites/molecule) |

## Function

### Haemoglobin — O₂ Transport

Each haemoglobin tetramer (α₂β₂) contains four haem-Fe²⁺ groups, each capable of reversibly binding one O₂ molecule:

$$\text{HbFe}^{2+} + \text{O}_2 \rightleftharpoons \text{HbFe}^{2+}\text{-O}_2$$

Crucially, O₂ binds **Fe²⁺** but not Fe³⁺: oxidation of haemoglobin to methaemoglobin (Hb-Fe³⁺) abolishes O₂-carrying capacity. Normal metHb is kept below 1% by NADH-methaemoglobin reductase (cytochrome b₅ reductase) in erythrocytes.

Key functional features [^stryer-biochemistry]:
- **Cooperative binding** (Hill coefficient n ~2.8): sigmoidal O₂-dissociation curve allows efficient loading at PO₂ 100 mmHg (lungs) and unloading at PO₂ 40 mmHg (tissues).
- **Bohr effect**: rising PCO₂/falling pH shifts the ODC rightward (↓ O₂ affinity), enhancing O₂ delivery to metabolically active tissues.
- **2,3-BPG**: synthesised in erythrocytes by bisphosphoglycerate mutase; binds the central cavity of deoxy-Hb (T-state), reducing O₂ affinity — adapted at high altitude.
- **25 trillion circulating RBCs**, each containing ~280 million Hb molecules, deliver ~250 mL O₂/min at rest and up to 4,000 mL/min during maximal exercise.

### Myoglobin — O₂ Storage in Muscle

Myoglobin (Mb) is a single-subunit, single-haem protein with a hyperbolic O₂-binding curve (no cooperativity, P₅₀ ~2–3 mmHg). Its high O₂ affinity means it:

- Acts as an **intracellular O₂ buffer** in working muscle, releasing O₂ only when PO₂ falls very low (during intense exercise).
- Facilitates **O₂ diffusion** from sarcolemma to mitochondria by carrying O₂ against a concentration gradient (myoglobin-facilitated diffusion).
- Contains the diagnostic biomarker released in myocardial infarction and rhabdomyolysis (myoglobin appears in blood within 1–2 hours, earlier than troponins, but less specific).

### Mitochondrial Electron Transport Chain

Iron participates in the ETC in two chemical forms:

1. **Haem proteins**: cytochrome b (Complex III), cytochrome c₁ (Complex III), cytochrome c (mobile carrier between III and IV), cytochrome a and a₃ (Complex IV, cytochrome c oxidase). Each cytochrome undergoes Fe²⁺/Fe³⁺ cycling as electrons flow from NADH/FADH₂ toward O₂.
2. **Iron-sulfur clusters**: [2Fe-2S] and [4Fe-4S] centres in Complexes I, II, and III shuttle single electrons at defined potentials. In aconitase (TCA cycle), a [4Fe-4S] cluster activates the substrate (isocitrate) through Lewis acid catalysis.

Together, haem and Fe-S iron account for **~10–14 mg** of the body's enzyme-bound iron — a small fraction by mass, but catalytically essential: Complex IV alone reduces ~20 L of O₂ per day in a resting adult.

### Non-Haem Iron Functions

Beyond ETC and O₂ transport, iron serves critical roles:

- **Ribonucleotide reductase (RNR)**: the enzyme that reduces ribonucleotides to deoxyribonucleotides (rate-limiting step for DNA synthesis in all dividing cells) contains a Fe-tyrosyl radical pair at its active site. Iron deficiency impairs RNR activity → reduced dNTP pools → impaired DNA replication (relevant in rapidly dividing haematopoietic progenitors and lymphocytes).
- **Prolyl and asparaginyl hydroxylases**: Fe²⁺ and 2-oxoglutarate–dependent dioxygenases that hydroxylate HIF-1α (targeting it for VHL-mediated ubiquitination and proteasomal degradation in normoxia) and hydroxylate proline residues in procollagen (required for triple-helix stability → scurvy if vitamin C, the Fe²⁺ reductant, is deficient).
- **Catalase**: haem-containing tetrameric enzyme in peroxisomes; decomposes H₂O₂ → H₂O + O₂ at rates up to 4 × 10⁷ mol/mol/s — protecting cells from oxidative stress.
- **Myeloperoxidase (MPO)**: haem enzyme in neutrophil azurophilic granules; generates hypochlorous acid (HOCl) from H₂O₂ + Cl⁻ — central to neutrophil bactericidal activity.
- **Cytochrome P450 enzymes**: haem-Fe²⁺/Fe³⁺ cycling drives the monooxygenase reaction in ~57 human CYPs involved in drug metabolism (CYP3A4), steroid biosynthesis (CYP11A1, CYP19A1/aromatase), bile acid synthesis (CYP7A1), and vitamin D activation (CYP27B1).

### Iron Absorption, Transport, and Recycling

**Duodenal absorption (10–15% of dietary non-haem Fe, ~25% of haem Fe):**

1. Fe³⁺ in diet is reduced to Fe²⁺ by **duodenal cytochrome b (DcytB)** and vitamin C at the brush border.
2. Fe²⁺ enters enterocytes via **DMT1** (divalent metal transporter 1; SLC11A2).
3. Haem iron enters via **HCP1** (haem carrier protein 1; SLC46A1) and is processed by haem oxygenase to release Fe²⁺.
4. Intracellular Fe²⁺ may be stored as ferritin or exported basolaterally by **ferroportin** (FPN1; SLC40A1).
5. Basolateral Fe²⁺ is oxidised to Fe³⁺ by **hephaestin** (a multicopper ferroxidase) for loading onto **transferrin** in plasma.

**Transferrin cycle:**
- Plasma transferrin (Tf, ~3 g/L) carries Fe³⁺ (two sites); transferrin saturation normally ~25–30%.
- Cells express transferrin receptor 1 (TfR1; CD71); Tf-Fe³⁺ binds TfR1 → clathrin-mediated endocytosis → endosomal acidification releases Fe³⁺ → DMT1 exports Fe²⁺ to cytoplasm → Tf/TfR1 recycled to surface.

**Macrophage iron recycling:**
- Senescent RBCs (after ~120-day lifespan) are phagocytosed by splenic, hepatic, and marrow macrophages; haem oxygenase 1 (HO-1) catabolises haem, releasing Fe²⁺.
- ~20–25 mg Fe/day is recycled this way — far exceeding the 1–2 mg absorbed daily; this recycling is the dominant source of plasma iron.

### Hepcidin — the Iron Hormone

**Hepcidin** (liver-derived, 25-amino-acid peptide encoded by *HAMP*) is the master regulator of systemic iron homeostasis:

- **Mechanism**: binds ferroportin → induces ferroportin internalisation and degradation → blocks Fe²⁺ export from enterocytes, macrophages, and hepatocytes → reduces plasma iron.
- **Stimuli for hepcidin upregulation**: iron loading (via BMP6-SMAD1/5/8 pathway through HJV and HFE co-receptors), inflammation (IL-6 → STAT3 → *HAMP* transcription), infection.
- **Stimuli for hepcidin suppression**: iron deficiency, hypoxia (↑ ERFE from erythropoietic progenitors), elevated erythropoiesis (ERFE suppresses BMP-SMAD).

**Post-transcriptional regulation by IRPs:**
- **IRP1/IRP2** bind iron-responsive elements (IREs) in the 5′ or 3′ UTRs of target mRNAs.
- Iron deficiency → IRP active → binds 5′ IRE of ferritin mRNA (blocks translation) and 3′ IRE of TfR1 mRNA (stabilises) → cell reduces storage and increases uptake.
- Iron excess → IRP inactive → ferritin synthesised freely; TfR1 mRNA degraded → cell stores iron and reduces uptake.

## Connections

- `part-of` → **[Human Body](../../08-whole-body/human-body/README.md)** — 3.5–4.5 g total; ~70% in haemoglobin Fe²⁺-haem, ~20% stored as ferritin/haemosiderin in liver/spleen/marrow, ~5% in myoglobin and enzymes (cytochromes, catalase) throughout the body.
- `part-of` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — each erythrocyte contains ~280 million haemoglobin tetramers each holding 4 haem-Fe²⁺ groups; iron is recycled by splenic macrophages after RBC senescence at the end of the ~120-day erythrocyte lifespan.
- `modulates` → **[Liver](../../06-organ/liver/README.md)** — liver is the primary iron storage organ (ferritin/haemosiderin in hepatocytes) and synthesises hepcidin (the master iron regulatory hormone) and transferrin (plasma iron transport protein).
- `modulates` → **[Immune System](../../07-system/immune-system/README.md)** — iron is required for lymphocyte proliferation (ribonucleotide reductase for dNTP synthesis); hepcidin-mediated iron sequestration from pathogens constitutes nutritional immunity in chronic infection and inflammation.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — iron loading (BMP6-SMAD) and inflammation (IL-6 → STAT3) upregulate hepcidin → ferroportin internalisation → reduced Fe export from enterocytes and macrophages → falling serum iron; hepcidin suppression in deficiency and hypoxia restores Fe absorption.
- `connects-to` → **[Iron-Deficiency Anemia](../../07-system/iron-deficiency-anemia/README.md)** — IDA is the most common nutritional deficiency (~2 billion globally): inadequate intake, chronic blood loss, or malabsorption → depleted ferritin → hypochromic microcytic anaemia; serum Fe low, TIBC high; treated with oral or IV iron.
- `connects-to` → **[Oxygen](../oxygen/README.md)** — haemoglobin Fe²⁺ reversibly binds O₂ (each Hb tetramer carries 4); cooperative binding (Hill n~2.8) enables loading at PO₂ 100 mmHg and unloading at PO₂ 40 mmHg; Fe³⁺ (methaemoglobin) cannot bind O₂ → O₂ transport wholly depends on iron oxidation state.

## Pathology

| Condition | Mechanism | Key features |
|:---|:---|:---|
| **Iron-deficiency anaemia (IDA)** | Inadequate dietary intake, chronic blood loss (GI, menstrual), malabsorption (coeliac, H. pylori) → depleted stores → hypochromic microcytic anaemia | Most common nutritional deficiency globally (~2 billion people); ferritin ↓, TIBC ↑, serum Fe ↓; treated with oral/IV iron |
| **Hereditary haemochromatosis (HH)** | *HFE* mutations (C282Y homozygosity in &gt;80% of cases) → ↓ hepcidin → ↑ ferroportin activity → excess iron absorption → deposition in liver, pancreas, heart, joints, pituitary | Hepatic cirrhosis/HCC, diabetes mellitus, dilated cardiomyopathy, arthropathy, bronze skin, hypogonadism; treated with regular venesection |
| **Anaemia of chronic disease (ACD)** | Chronic inflammation → ↑ IL-6 → ↑ hepcidin → ↓ ferroportin → iron sequestration in macrophages/hepatocytes → functional iron deficiency despite adequate stores | Normocytic or mildly microcytic; low serum Fe, normal/high ferritin, low TIBC; treat underlying disease; erythropoiesis-stimulating agents in selected patients |
| **Transfusional iron overload** | Chronic transfusions in thalassaemia, sickle cell, MDS → cumulative iron load (~200–250 mg Fe/transfusion) exceeds excretory capacity | Organ damage (liver, heart, endocrine); treated with iron chelation (deferasirox, desferrioxamine) |
| **Iron toxicity / acute poisoning** | Excess free Fe²⁺ → Fenton reaction → hydroxyl radical → lipid peroxidation, mitochondrial damage, GI mucosa necrosis | Common in paediatric iron tablet ingestion; treated with IV desferrioxamine |
| **Sideroblastic anaemia** | Impaired haem synthesis (X-linked: ALAS2 mutation; or acquired: lead, isoniazid, alcohol) → iron accumulates in mitochondria of erythroid precursors (ring sideroblasts) | Microcytic/hypochromic anaemia; bone marrow ring sideroblasts on Prussian blue stain |

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019. [macmillanlearning.com](https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X)
[^guyton-hall]: Hall JE, Hall ME. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021. [elsevier.com](https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8)

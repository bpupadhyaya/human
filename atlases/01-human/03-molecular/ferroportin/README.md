---
schema: human-scale-entry/v1
id: ferroportin
name: Ferroportin
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "Ferroportin (SLC40A1/FPN1) is the sole cellular iron exporter; expressed on enterocytes, macrophages, and hepatocytes; hepcidin binds FPN → internalization → lysosomal degradation → iron sequestration; SLC40A1 mutations cause type 4 haemochromatosis (ferroportin disease)."
aliases: ["ferroportin", "FPN1", "SLC40A1", "IREG1", "MTP1", "ferroportin-1", "iron-regulated transporter", "hepcidin receptor"]
sources:
  - id: donovan-2000-ferroportin-cloning
    type: peer-reviewed
    cite: "Donovan A, Brownlie A, Zhou Y, et al. Positional cloning of zebrafish ferroportin1 identifies a conserved vertebrate iron exporter. Nature. 2000;403(6771):776-781."
    doi: "10.1038/35001596"
    pmid: "10693807"
    url: "https://doi.org/10.1038/35001596"
  - id: nemeth-2004-hepcidin-ferroportin
    type: peer-reviewed
    cite: "Nemeth E, Tuttle MS, Powelson J, et al. Hepcidin regulates cellular iron efflux by binding to ferroportin and inducing its internalization. Science. 2004;306(5704):2090-2093."
    doi: "10.1126/science.1104742"
    pmid: "15514116"
    url: "https://doi.org/10.1126/science.1104742"
  - id: billesbolle-2020-fpn-structure
    type: peer-reviewed
    cite: "Billesbølle CB, Azumaya CM, Kretschmer RC, et al. Structure of hepcidin-bound ferroportin reveals iron homeostasis regulation. Nature. 2020;586(7831):807-811."
    doi: "10.1038/s41586-020-2668-z"
    pmid: "32908311"
    url: "https://doi.org/10.1038/s41586-020-2668-z"
cross_links:
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Hepcidin binds FPN at the extracellular cavity → endocytosis → lysosomal degradation; 2020 cryo-EM structure shows hepcidin locks FPN in inward-facing conformation; high hepcidin → iron sequestration; low hepcidin → FPN stabilized → iron export."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "FPN exports Fe²⁺ from enterocytes and macrophages → hephaestin/ceruloplasmin oxidize Fe²⁺ to Fe³⁺ → binds apo-transferrin → delivery to erythroid TFR1; FPN is the sole gateway from intracellular iron stores into the plasma transferrin pool."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "IDA occurs when FPN-mediated iron export is insufficient for erythropoietic demand; hepcidin falls to near zero in IDA → FPN upregulated → maximal enterocyte iron export; despite this, depleted stores → iron-restricted erythropoiesis → microcytic anemia."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "ACD = hepcidin-driven FPN degradation → functional iron deficiency despite replete stores; elevated IL-6 → hepcidin → FPN lysosomal degradation → iron trapping in macrophages; restoring FPN activity by blocking hepcidin is the therapeutic strategy for ACD."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Ferroportin is the sole cellular Fe²⁺ exporter, mediating dietary iron absorption (enterocytes) and iron recycling (macrophages); exported Fe²⁺ is oxidized by hephaestin/ceruloplasmin to Fe³⁺ → transferrin binding → erythropoiesis; FPN loss traps iron intracellularly."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 drives hepcidin transcription (JAK2/STAT3 → hepcidin promoter) → FPN lysosomal degradation → iron sequestration; IL-6 blocking (tocilizumab in RA) reduces hepcidin and corrects anemia; IL-6/hepcidin/FPN axis is the mechanistic basis of anemia of chronic disease."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Erythropoietic demand stimulates erythroferrone (ERFE) from erythroblasts → ERFE suppresses hepcidin → FPN stabilized → increased iron export; EPO therapy drives ERFE → hepcidin suppression → FPN upregulation; explains mandatory iron supplementation with ESA therapy in CKD."
---

# Ferroportin

## Overview

**Ferroportin (FPN1; gene *SLC40A1*, chromosome 2q32.2; also called IREG1 and MTP1)** is the **only known cellular iron exporter in mammals** — a 571-amino acid, 12-transmembrane-helix protein that mediates the efflux of ferrous iron (Fe²⁺) from cells into the bloodstream [^donovan-2000-ferroportin-cloning]. It was simultaneously identified by three independent groups in 2000 — in zebrafish (*ferroportin1*), mice (*Ireg1*), and humans (*MTP1*) — using positional cloning approaches targeting hypochromic anaemia phenotypes. Its discovery explained the long-standing observation that iron absorption in enterocytes and iron recycling in macrophages must involve a dedicated export mechanism.

Ferroportin is constitutively expressed on four cell types critical for iron homeostasis:
1. **Duodenal enterocytes** (basolateral membrane) — exports absorbed dietary iron into the portal circulation
2. **Macrophages** (Kupffer cells, splenic macrophages, bone marrow macrophages) — releases iron recycled from senescent erythrocyte haemoglobin (~20 mg Fe/day)
3. **Hepatocytes** — releases stored iron from ferritin when systemic demand rises
4. **Placental syncytiotrophoblasts** — transfers maternal iron to the fetal circulation

Without ferroportin, absorbed dietary iron and recycled haemoglobin iron would remain permanently trapped within these cells — a reality that is precisely exploited by hepcidin to restrict iron availability during infection or chronic inflammation.

## Structure

### Protein topology and transport mechanism

Ferroportin is a **major facilitator superfamily (MFS) transporter** consisting of two pseudo-symmetric halves (N-terminal domain: TMDs 1-6; C-terminal domain: TMDs 7-12), characteristic of the MFS alternating-access mechanism:

- **Outward-open conformation:** Iron-binding cavity exposed to cytoplasm → Fe²⁺ from the labile iron pool enters the cavity
- **Occluded → inward-open conformation:** Cavity opens toward extracellular space → Fe²⁺ exits the cell
- Iron transport is electrogenic and coupled to proton antiport (one Fe²⁺ out for one H⁺ in)

The **2020 cryo-EM structure** of hepcidin-bound ferroportin (Billesbølle et al., resolution 2.0 Å) provided the first atomic-level view [^billesbolle-2020-fpn-structure]:
- Hepcidin binds within the **extracellular cavity of FPN** (the same cavity through which Fe²⁺ exits), with its C-terminus reaching into the iron-permeation pathway
- Hepcidin binding **locks FPN in an inward-facing (occluded) conformation** → transport is blocked
- The iron-binding residues in the cavity include **Cys326** (which forms a disulfide with Cys6 of hepcidin) and **His507** — mutations at these sites reduce hepcidin sensitivity
- FPN also has a second, "non-canonical" iron site at the extracellular face that may facilitate iron loading/unloading

### Hepcidin-ferroportin binding and internalization

The hepcidin-FPN interaction is the central molecular event in iron homeostasis [^nemeth-2004-hepcidin-ferroportin]:

1. Hepcidin (25-aa peptide; 4 disulfide bonds) reaches FPN from hepatic blood
2. Hepcidin binds the extracellular cavity of outward-open FPN → conformational lock → FPN cannot cycle
3. Bound FPN-hepcidin complex undergoes **clathrin-mediated endocytosis**
4. **Lysosomal degradation** of both hepcidin and FPN
5. Net effect: cells cannot export iron → iron accumulates intracellularly → available plasma iron falls → TSAT decreases

This process is **dose-dependent**: small increases in hepcidin partially reduce FPN surface expression; high hepcidin (infection, inflammation, iron overload) eliminates cell-surface FPN → near-complete iron export block.

### Hephaestin and ceruloplasmin — iron oxidation for transferrin binding

Exported Fe²⁺ cannot bind transferrin (which only accepts Fe³⁺). Two ferroxidases handle oxidation:
- **Hephaestin** — GPI-anchored multicopper oxidase on the basolateral surface of enterocytes; oxidizes Fe²⁺ → Fe³⁺ immediately after FPN export
- **Ceruloplasmin** — plasma-phase ferroxidase (made in liver); handles Fe²⁺ released by macrophages and hepatocytes

**Acaeruloplasminaemia** (hereditary ceruloplasmin deficiency) → Fe²⁺ cannot be oxidized in the systemic circulation → iron accumulates in macrophages, liver, brain → neurodegeneration + anaemia.

## Function

### Iron absorption — the enterocyte FPN axis

Daily dietary iron absorption (~1–2 mg):
1. Luminal Fe³⁺ reduced to Fe²⁺ by **duodenal cytochrome b (Dcytb)** at the brush border
2. Fe²⁺ imported apically by **DMT1 (SLC11A2; divalent metal transporter 1)**
3. Fe²⁺ stored as ferritin in enterocyte cytoplasm or directed to FPN for export
4. FPN exports Fe²⁺ across basolateral membrane → hephaestin oxidizes → Fe³⁺ binds apo-transferrin
5. Rate-limiting step: FPN activity (determined by surface expression = hepcidin level)

**Haem iron** (~25% of Western dietary iron intake): absorbed through haem carrier protein 1 (HCP1/SLC46A1); intracellular haem oxygenase releases Fe²⁺ → same FPN export pathway.

### Iron recycling — the macrophage FPN axis

The dominant daily iron cycle:
- Senescent RBCs (every 120 days) → phagocytosed by splenic, liver (Kupffer), bone marrow macrophages → haemoglobin digested in phagolysosomes → haem oxygenase → Fe²⁺ + biliverdin + CO
- Fe²⁺ either stored as ferritin (high hepcidin → FPN degraded → iron trapped) or exported via FPN → ceruloplasmin → transferrin → erythropoiesis
- This cycle delivers **~20 mg Fe/day** — dwarfing dietary absorption and representing the dominant iron source for haemoglobin synthesis

### Iron storage release — hepatocyte FPN

Hepatocytes store ~1 g of iron as ferritin (and haemosiderin in overload). FPN on hepatocytes is regulated by the same hepcidin-mediated degradation, controlling the release rate from stores. In iron deficiency, hepcidin suppression maximizes FPN on hepatocytes → liver iron mobilized for erythropoiesis.

## Mechanism

### IRP-independent vs. IRP-regulated iron export

Unlike transferrin receptor 1 (TFR1), whose mRNA is stabilized by iron-responsive proteins (IRPs) under iron deficiency, **FPN mRNA regulation is primarily post-translational** (hepcidin-mediated). However, FPN mRNA does contain a **5'-UTR IRE** — when cytoplasmic iron is very low, IRP1/IRP2 bind the 5'-IRE → **translational repression** of FPN. This prevents enterocytes from exporting iron they cannot afford to lose (protective mechanism in iron deficiency paradox — the IRE ensures enterocytes retain some iron for their own metabolic needs even while maximally absorbing dietary iron).

### Regulation summary

| Signal | Effect on FPN | Mechanism | Outcome |
|:-------|:-------------|:----------|:--------|
| ↑ Hepcidin | ↓ FPN surface expression | Endocytosis + lysosomal degradation | ↓ Iron absorption and recycling |
| ↓ Hepcidin | ↑ FPN | Reduced degradation; ↑ FPN translation | ↑ Iron absorption and recycling |
| Low cytoplasmic iron | ↓ FPN (enterocytes) | 5'-IRE → IRP1/2 → translational repression | Retain iron for cellular use |
| High cytoplasmic iron | ↑ FPN | IRPs released from 5'-IRE; ↑ FPN protein | Export excess iron |
| Inflammation (IL-6) | ↓ FPN (indirect) | IL-6 → STAT3 → hepcidin → FPN degradation | Iron sequestration (nutritional immunity) |

## Pathology

### Ferroportin disease (Hereditary Haemochromatosis Type 4)

**SLC40A1 mutations** cause the only known form of haemochromatosis due to a ferroportin defect — clinically distinct from HFE-related (Type 1), TFR2-related (Type 3), or hepcidin-related (Types 2a/2b) haemochromatosis:

**Type 4A — Loss-of-function (FPN1-A, ~80% of ferroportin disease):**
- FPN cannot export iron (misfolding, impaired trafficking, or reduced expression)
- Iron accumulates in **macrophages and enterocytes** (iron cannot leave cells) → macrophage-predominant tissue loading
- Laboratory: ferritin very high; TSAT **low or normal** (unlike classic haemochromatosis); serum iron often low-normal
- Clinical: relatively mild course; often found incidentally; anaemia if severe; liver fibrosis late
- Treatment: phlebotomy poorly tolerated (accelerates anaemia); low-intensity venesection; management as needed

**Type 4B/C — Gain-of-function (hepcidin resistance; ~20%):**
- FPN expressed normally but **resistant to hepcidin binding** (mutations at hepcidin-binding interface, e.g., Y64N, N144H, C326Y, D473G)
- Iron exported constitutively regardless of hepcidin level → excess iron loading of **parenchymal cells** (hepatocytes, cardiomyocytes, endocrine glands)
- Laboratory: ferritin very high; TSAT **very high** (>60-80%); NTBI present
- Clinical: identical to Type 1 (HFE-related) haemochromatosis; liver cirrhosis, cardiomyopathy, diabetes, hypogonadism
- Treatment: regular phlebotomy (same as HFE haemochromatosis)

### Ferroportin in common iron disorders

| Condition | FPN status | Hepcidin | Consequence |
|:----------|:----------|:---------|:------------|
| Iron deficiency anemia (IDA) | ↑ (hepcidin suppressed) | Very low | Maximal iron absorption; cannot compensate if stores depleted |
| Anemia of chronic disease | ↓ (hepcidin elevated) | Very high | Functional iron deficiency despite replete stores |
| β-Thalassaemia major | ↑ (hepcidin suppressed by ERFE) | Very low | Pathological iron overload; dietary + transfusion iron unrestricted |
| Hereditary haemochromatosis (HFE) | ↑↑ (insufficient hepcidin) | Inappropriately low | Parenchymal iron overload |
| Ferroportin disease Type 4A | ↓↓ (dysfunctional protein) | High (compensatory) | Macrophage iron overload; low TSAT |
| Ferroportin disease Type 4B/C | Normal but hepcidin-resistant | High (compensatory but ineffective) | Parenchymal iron overload |

## Connections

- `connects-to` → **[Hepcidin](../hepcidin/README.md)** — Hepcidin binds FPN at the extracellular cavity → endocytosis → lysosomal degradation; 2020 cryo-EM structure shows hepcidin locks FPN in inward-facing conformation; high hepcidin → iron sequestration; low hepcidin → FPN stabilized → iron export.
- `connects-to` → **[Transferrin](../transferrin/README.md)** — FPN exports Fe²⁺ from enterocytes and macrophages → hephaestin/ceruloplasmin oxidize Fe²⁺ to Fe³⁺ → binds apo-transferrin → delivery to erythroid TFR1; FPN is the sole gateway from intracellular iron stores into the plasma transferrin pool.
- `connects-to` → **[Iron Deficiency Anemia](../../07-system/iron-deficiency-anemia/README.md)** — IDA occurs when FPN-mediated iron export is insufficient for erythropoietic demand; hepcidin falls to near zero in IDA → FPN upregulated → maximal enterocyte iron export; despite this, depleted stores → iron-restricted erythropoiesis → microcytic anemia.
- `connects-to` → **[Anemia of Chronic Disease](../../07-system/anemia-of-chronic-disease/README.md)** — ACD = hepcidin-driven FPN degradation → functional iron deficiency despite replete stores; elevated IL-6 → hepcidin → FPN lysosomal degradation → iron trapping in macrophages; restoring FPN activity by blocking hepcidin is the therapeutic strategy for ACD.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Ferroportin is the sole cellular Fe²⁺ exporter, mediating dietary iron absorption (enterocytes) and iron recycling (macrophages); exported Fe²⁺ is oxidized by hephaestin/ceruloplasmin to Fe³⁺ → transferrin binding → erythropoiesis; FPN loss traps iron intracellularly.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — IL-6 drives hepcidin transcription (JAK2/STAT3 → hepcidin promoter) → FPN lysosomal degradation → iron sequestration; IL-6 blocking (tocilizumab in RA) reduces hepcidin and corrects anemia; IL-6/hepcidin/FPN axis is the mechanistic basis of anemia of chronic disease.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Erythropoietic demand stimulates erythroferrone (ERFE) from erythroblasts → ERFE suppresses hepcidin → FPN stabilized → increased iron export; EPO therapy drives ERFE → hepcidin suppression → FPN upregulation; explains mandatory iron supplementation with ESA therapy in CKD.

[^donovan-2000-ferroportin-cloning]: Donovan A, Brownlie A, Zhou Y, et al. Positional cloning of zebrafish ferroportin1 identifies a conserved vertebrate iron exporter. *Nature.* 2000;403(6771):776-781. [doi:10.1038/35001596](https://doi.org/10.1038/35001596) · [PubMed 10693807](https://pubmed.ncbi.nlm.nih.gov/10693807/)
[^nemeth-2004-hepcidin-ferroportin]: Nemeth E, Tuttle MS, Powelson J, et al. Hepcidin regulates cellular iron efflux by binding to ferroportin and inducing its internalization. *Science.* 2004;306(5704):2090-2093. [doi:10.1126/science.1104742](https://doi.org/10.1126/science.1104742) · [PubMed 15514116](https://pubmed.ncbi.nlm.nih.gov/15514116/)
[^billesbolle-2020-fpn-structure]: Billesbølle CB, Azumaya CM, Kretschmer RC, et al. Structure of hepcidin-bound ferroportin reveals iron homeostasis regulation. *Nature.* 2020;586(7831):807-811. [doi:10.1038/s41586-020-2668-z](https://doi.org/10.1038/s41586-020-2668-z) · [PubMed 32908311](https://pubmed.ncbi.nlm.nih.gov/32908311/)

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

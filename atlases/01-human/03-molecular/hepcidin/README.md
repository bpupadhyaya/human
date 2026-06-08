---
schema: human-scale-entry/v1
id: hepcidin
name: Hepcidin
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "Hepcidin (HAMP; chr19q13.12) is the master iron regulatory hormone produced by hepatocytes; binds ferroportin → internalization → blocks iron efflux from enterocytes, macrophages, and hepatocytes. IL-6→STAT3→hepcidin drives anemia of chronic disease; inhibitors under development."
aliases: ["hepcidin", "HAMP", "hepcidin antimicrobial peptide", "liver antimicrobial peptide", "LEAP-1", "hepcidin-25", "iron hormone", "ferroportin axis"]
sources:
  - id: nemeth-2004-hepcidin-ferroportin
    type: peer-reviewed
    cite: "Nemeth E, Tuttle MS, Powelson J, et al. Hepcidin regulates cellular iron efflux by binding to ferroportin and inducing its internalization. Science. 2004;306(5704):2090-2093."
    doi: "10.1126/science.1104742"
    pmid: "15514116"
    url: "https://doi.org/10.1126/science.1104742"
  - id: ganz-2013-hepcidin-review
    type: peer-reviewed
    cite: "Ganz T. Systemic iron homeostasis. Physiol Rev. 2013;93(4):1721-1741."
    doi: "10.1152/physrev.00008.2013"
    pmid: "24137020"
    url: "https://doi.org/10.1152/physrev.00008.2013"
  - id: camaschella-2015-iron-deficiency
    type: peer-reviewed
    cite: "Camaschella C. Iron-deficiency anemia. N Engl J Med. 2015;372(19):1832-1843."
    doi: "10.1056/NEJMra1401038"
    pmid: "25946282"
    url: "https://doi.org/10.1056/NEJMra1401038"
cross_links:
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "IL-6 → STAT3 → hepcidin upregulation → ferroportin degradation → iron sequestration in macrophages/hepatocytes → hypoferremia → iron-restricted erythropoiesis → normocytic or microcytic anemia; hepcidin is the molecular bridge between inflammation and ACD/AOSD/IBD-related anemia."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 is the primary inducer of hepcidin in inflammation and anemia of chronic disease; IL-6 → JAK1/2 → STAT3 → HAMP promoter → hepcidin synthesis and secretion; tocilizumab (anti-IL-6R) reduces serum hepcidin → iron mobilization → improved hemoglobin in RA and Castleman."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "ERFE (erythroferrone), produced by erythroblasts in response to EPO, suppresses hepcidin via BMP/SMAD inhibition → iron mobilization for erythropoiesis; ERFE excess in β-thalassemia overly suppresses hepcidin → iron overload; HIF-PHIs suppress hepcidin via EPO→ERFE axis."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Hepcidin is elevated in CKD from reduced renal clearance and chronic inflammation; elevated hepcidin → functional iron deficiency → ESA hyporesponsiveness in CKD anemia; HIF-PHIs (roxadustat, daprodustat) suppress hepcidin via EPO→ERFE→BMP-SMAD inhibition."
---

# Hepcidin

## Overview

**Hepcidin** (gene *HAMP*, chromosome 19q13.12; hepcidin antimicrobial peptide; formerly LEAP-1) is a **25-amino acid cysteine-rich hepatic peptide hormone** that functions as the **master regulator of systemic iron homeostasis** [^nemeth-2004-hepcidin-ferroportin]. It is produced predominantly by hepatocytes and acts on its target receptor **ferroportin (SLC40A1; FPN1)** — the only known cellular iron exporter in mammals — inducing ferroportin internalization and lysosomal degradation, thereby blocking iron efflux from:

1. **Duodenal enterocytes** → reduces dietary iron absorption
2. **Macrophages (Kupffer cells, splenic and bone marrow macrophages)** → traps iron from hemoglobin degradation (recycled RBC iron = ~20 mg/day) within macrophages
3. **Hepatocytes** → reduces iron release from hepatic stores

The net effect of elevated hepcidin is **hypoferremia** — reduced circulating iron — which is the physiological defense against iron-overloading pathogens (iron is essential for microbial growth) and the pathological mechanism of **anemia of chronic disease (ACD)**.

**Hepcidin in disease:**
- **Absent/low hepcidin:** Hereditary hemochromatosis (HFE, TFR2, HJV, HAMP mutations) → unrestricted ferroportin → iron overload; β-thalassemia intermedia (ERFE suppresses hepcidin despite iron overload)
- **Elevated hepcidin:** Anemia of chronic disease (infection, autoimmune disease, cancer, CKD) → functional iron deficiency despite adequate iron stores; iron-refractory iron deficiency anemia (IRIDA: TMPRSS6 mutations → constitutive hepcidin elevation)
- **Therapeutic target:** Hepcidin pathway modulators under development — anti-hepcidin antibodies, ERFE mimetics, anti-TMPRSS6 siRNA (for polycythemia vera), anti-HJV antibodies — to treat ACD and hereditary hemochromatosis

## Structure

### Hepcidin peptide

| Feature | Detail |
|:--------|:-------|
| Gene | *HAMP*, chromosome 19q13.12; 3 exons; regulated by HIF-1α (hypoxia → ↓hepcidin), ERFE, BMP/SMAD pathway (iron sensing), IL-6/STAT3 (inflammation) |
| Pre-pro-hepcidin | 84 aa pre-pro-peptide; signal peptide (24 aa) + pro-region (35 aa) + mature hepcidin-25 (25 aa) |
| Mature hepcidin-25 | The bioactive form; 25 aa (≈2.8 kDa); 4 disulfide bonds (8 cysteines) → ladder-like structure with amphipathic β-sheet; the N-terminal DHSLIC hairpin region interacts with ferroportin |
| Circulates | Plasma hepcidin 25-100 ng/mL (normal adults); measured by ELISA or mass spectrometry; sex differences (higher in men, higher in post-menopausal women) |

### The BMP-SMAD pathway — iron sensing by the liver

The liver integrates multiple signals to calibrate hepcidin:

**Iron status (suppresses hepcidin when iron-depleted; induces when iron-replete):**
- Diferric transferrin (Tf-Fe₂) → binds TFR1 (displaces HFE) → HFE interacts with TFR2 → TFR2/HFE complex signals to BMP receptor complex (BMPR1/BMPR2 + HJV co-receptor)
- Iron stores → BMP6 secretion from liver sinusoidal endothelial cells → BMP6/BMPR/HJV → SMAD1/5/8 phosphorylation → SMAD4 nuclear entry → HAMP transcription
- **HJV (hemojuvelin; RGMc):** GPI-anchored co-receptor that amplifies BMP→SMAD signaling; mutations → juvenile hemochromatosis (severe early-onset iron overload); anti-HJV antibodies suppress hepcidin (in development for ACD)

**Erythropoietic activity (suppresses hepcidin):**
- **ERFE (erythroferrone):** Produced by erythroblasts in response to EPO → circulates → inhibits BMP6/SMAD → suppresses hepcidin → iron mobilization for expanded erythropoiesis
- Excessive ERFE (in β-thalassemia, stress erythropoiesis): overly suppresses hepcidin → iron overload despite adequate stores → paradoxical iron overload in ineffective erythropoiesis
- **HIF-2α** (hypoxia-inducible factor): Transcribes EPO, DMT1, DCYTB → indirectly suppresses hepcidin via ERFE

**Inflammation (induces hepcidin):**
- IL-6 → IL-6R/gp130 → JAK1/2 → STAT3 phosphorylation → STAT3 binds HAMP promoter → hepcidin within 2-4 hours
- IL-1β, TNF-α (weaker inducers via NF-κB)
- Activin B (inflammation-induced) → BMPR1/ACVR1 → SMAD1/5 → additive hepcidin induction

### Ferroportin — the sole mammalian iron exporter

**Ferroportin (SLC40A1; FPN1; IREG1):**
- 571 aa 12-transmembrane domain exporter
- Expressed on duodenal enterocytes (basolateral; exports absorbed iron into blood), macrophages (exports recycled RBC iron), hepatocytes (stores), placenta (maternal-fetal iron transfer)
- Hepcidin binds ferroportin extracellular loop → conformational change → JAK2 activation → ferroportin Tyr-phosphorylation → ubiquitination → clathrin-mediated endocytosis → lysosomal degradation within 4 hours
- **Ferroportin disease (gain-of-function FPN1 mutations):** Hepcidin-resistant ferroportin → lifelong iron overload with predominantly macrophage/Kupffer cell iron retention; treated with phlebotomy

## Function

### Physiological iron regulation

Daily iron economy (healthy adult):
- **Loss:** ~1-2 mg/day (gut epithelial shedding, minor hemorrhage); no regulated excretory pathway
- **Absorption:** ~1-2 mg/day dietary iron (duodenal enterocytes; DMT1 imports Fe²⁺; DCYTB reduces Fe³⁺→Fe²⁺; ferroportin exports to blood; hephaestin oxidizes Fe²⁺→Fe³⁺ for transferrin loading)
- **Recycling:** ~20 mg/day from macrophage erythrophagocytosis (the dominant iron source for erythropoiesis)
- **Stores:** Liver ferritin: 0.5-1.5 g total body iron stores (ferritin encapsulates iron as insoluble Fe(III) polymer; serum ferritin ~1 ng/mL ≈ 8 mg iron stores)

**Hepcidin acts as a gain dial:** Low hepcidin (iron deficiency, hypoxia, expanded erythropoiesis) → high ferroportin activity → more iron absorption + macrophage iron release → increase plasma iron. High hepcidin (inflammation, iron overload) → low ferroportin activity → less absorption + iron trapping → reduce plasma iron.

### Antimicrobial function

Hepcidin has weak direct antimicrobial activity against bacteria and fungi at high concentrations (LEAP-1 was originally discovered as an antimicrobial peptide). More importantly, hepcidin-mediated hypoferremia is an **innate immune nutritional immunity** strategy: withholding iron from pathogens by trapping it in macrophages, reducing transferrin saturation, and limiting free ionic iron available for bacterial growth. This is why anemia of infection is the body's deliberate strategy, not a maladaptive consequence.

## Mechanism

### Anemia of chronic disease — hepcidin as the central effector

**ACD pathogenesis (step by step):**
1. Chronic infection, autoimmune disease (RA, SLE, IBD, CKD, malignancy) → sustained **IL-6** (and other cytokines) production
2. IL-6 → hepatocyte STAT3 → **hepcidin** elevated (often 3-10× normal)
3. High hepcidin → ferroportin degradation on:
   - Duodenal enterocytes → ↓iron absorption
   - Reticuloendothelial macrophages → iron trapped from hemoglobin recycling → macrophage iron overload
   - Hepatocytes → stored iron not released
4. **Plasma iron falls (hypoferremia):** Low serum iron + low-normal or normal transferrin saturation + elevated ferritin (iron still present, but trapped)
5. Bone marrow erythroid progenitors (BFU-E, CFU-E) sense iron shortage → **iron-restricted erythropoiesis** → microcytic or normocytic anemia
6. Additionally: cytokines (IL-1β, TNF-α, IFN-γ) inhibit EPO production, blunt EPO receptor signaling on erythroid progenitors, and shorten RBC lifespan → compounding the anemia

**Why treating ACD with iron supplements is limited:**
- Oral iron: low efficacy because ferroportin is degraded in enterocytes → iron cannot be exported from enterocyte into blood → passes through in stool
- IV iron (ferric carboxymaltose, iron sucrose): bypasses gut barrier → delivers iron directly to blood → some benefit, but macrophage trapping still reduces erythroid availability
- **Definitive treatment:** Suppress underlying inflammation → IL-6 falls → hepcidin falls → ferroportin recovers → iron mobilized → anemia corrects

### Clinical measurement and interpretation

| Test | ACD | IDA | ACD + IDA |
|:-----|:----|:----|:---------|
| Serum iron | Low | Low | Low |
| TIBC/transferrin | Low or normal | High | Low or normal |
| Transferrin saturation | Low-normal | Very low | Low |
| Serum ferritin | Normal to high | Low (<30 ng/mL) | Low-normal |
| Soluble TfR (sTfR) | Low-normal | High | High |
| sTfR/log ferritin index | <1 | >2 | >2 |
| Hepcidin | High | Low | Variable |
| Reticulocyte hemoglobin (CHr) | Low | Low | Low |

**Key differentiator:** Ferritin is an acute-phase reactant — it rises in inflammation even when iron stores are low (can mask IDA in the setting of inflammation). sTfR and the sTfR/log ferritin index are less affected by inflammation → useful to detect concurrent IDA in ACD.

## Connections

- `connects-to` → **[Anemia of Chronic Disease](../../07-system/anemia-of-chronic-disease/README.md)** — IL-6 → STAT3 → hepcidin upregulation → ferroportin degradation → iron sequestration in macrophages → hypoferremia → iron-restricted erythropoiesis → normocytic or microcytic anemia; hepcidin is the molecular bridge between inflammation and ACD/IBD/CKD-related anemia.
- `connects-to` → **[IL-6](../il-6/README.md)** — IL-6 is the primary inducer of hepcidin in acute inflammation and anemia of chronic disease; IL-6 → JAK1/2 → STAT3 → HAMP promoter → hepcidin synthesis and secretion; tocilizumab (anti-IL-6R) rapidly reduces serum hepcidin → iron mobilization → improved hemoglobin in RA and Castleman.
- `connects-to` → **[Erythropoietin](../erythropoietin/README.md)** — ERFE (erythroferrone), produced by erythroblasts in response to EPO, suppresses hepcidin via BMP/SMAD inhibition → iron mobilization for erythropoiesis; ERFE excess in β-thalassemia overly suppresses hepcidin → iron overload; HIF-PHIs suppress hepcidin via EPO→ERFE axis.
- `connects-to` → **[CKD](../../07-system/ckd/README.md)** — Hepcidin is elevated in CKD from reduced renal clearance and chronic inflammation; elevated hepcidin → functional iron deficiency → ESA hyporesponsiveness in CKD anemia; HIF-PHIs (roxadustat, daprodustat) suppress hepcidin via EPO→ERFE→BMP-SMAD inhibition.

[^nemeth-2004-hepcidin-ferroportin]: Nemeth E, Tuttle MS, Powelson J, et al. Hepcidin regulates cellular iron efflux by binding to ferroportin and inducing its internalization. *Science.* 2004;306(5704):2090-2093. [doi:10.1126/science.1104742](https://doi.org/10.1126/science.1104742) · [PubMed 15514116](https://pubmed.ncbi.nlm.nih.gov/15514116/)
[^ganz-2013-hepcidin-review]: Ganz T. Systemic iron homeostasis. *Physiol Rev.* 2013;93(4):1721-1741. [doi:10.1152/physrev.00008.2013](https://doi.org/10.1152/physrev.00008.2013) · [PubMed 24137020](https://pubmed.ncbi.nlm.nih.gov/24137020/)
[^camaschella-2015-iron-deficiency]: Camaschella C. Iron-deficiency anemia. *N Engl J Med.* 2015;372(19):1832-1843. [doi:10.1056/NEJMra1401038](https://doi.org/10.1056/NEJMra1401038) · [PubMed 25946282](https://pubmed.ncbi.nlm.nih.gov/25946282/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

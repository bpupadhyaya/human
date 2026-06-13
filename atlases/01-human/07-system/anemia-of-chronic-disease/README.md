---
schema: human-scale-entry/v1
id: anemia-of-chronic-disease
name: Anemia of Chronic Disease
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Anemia of chronic disease (ACD) is anemia from chronic inflammation (infection, autoimmune disease, malignancy, CKD); IL-6 → hepcidin → ferroportin degradation → iron sequestration → iron-restricted erythropoiesis. Treat underlying cause; IV iron and ESAs in CKD."
aliases: ["ACD", "anemia of chronic disease", "anemia of inflammation", "AI", "functional iron deficiency", "AOCD", "inflammatory anemia", "iron sequestration anemia"]
sources:
  - id: weiss-2005-acd-review
    type: peer-reviewed
    cite: "Weiss G, Goodnough LT. Anemia of chronic disease. N Engl J Med. 2005;352(10):1011-1023."
    doi: "10.1056/NEJMra041809"
    pmid: "15758012"
    url: "https://doi.org/10.1056/NEJMra041809"
  - id: nemeth-2004-il6-hepcidin
    type: peer-reviewed
    cite: "Nemeth E, Rivera S, Gabayan V, et al. IL-6 mediates hypoferremia of inflammation by inducing the synthesis of the iron regulatory hormone hepcidin. J Clin Invest. 2004;113(9):1271-1276."
    doi: "10.1172/JCI200420945"
    pmid: "15124018"
    url: "https://doi.org/10.1172/JCI200420945"
  - id: ganz-2019-acd-iron
    type: peer-reviewed
    cite: "Ganz T. Anemia of Inflammation. N Engl J Med. 2019;381(12):1148-1157."
    doi: "10.1056/NEJMra1916038"
    pmid: "31532961"
    url: "https://doi.org/10.1056/NEJMra1916038"
cross_links:
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Hepcidin is the central molecular effector of ACD: IL-6 → STAT3 → hepcidin → ferroportin degradation → iron sequestration in macrophages/hepatocytes → hypoferremia → iron-restricted erythropoiesis; hepcidin pathway inhibitors (anti-HJV, ERFE mimetics) under development for ACD."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 is the primary upstream driver of ACD: IL-6 from macrophages in infection/autoimmune disease/malignancy → STAT3 → hepcidin → ferroportin degradation → iron-restricted erythropoiesis; IL-6 also suppresses EPO production → blunted erythropoietic response."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "EPO production is suppressed in ACD by TNF-α/IL-1β/IFN-γ and EPO-R signaling is blunted by inflammatory cytokines → EPO hyporesponsiveness; ESAs (epoetin, darbepoetin) are used in CKD-ACD with Hgb target 10-11.5 g/dL; HIF-PHIs restore EPO while suppressing hepcidin."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "CKD anemia combines EPO deficiency (from peritubular cell loss) with ACD-driven hepcidin elevation and functional iron deficiency; target Hgb 10-11.5 g/dL with ESA + IV iron; HIF-PHIs (roxadustat) treat CKD anemia by restoring EPO and suppressing hepcidin simultaneously."
  - target: 01-human/03-molecular/ferroportin
    relation: connects-to
    note: "Ferroportin is the cellular target of hepcidin in ACD; IL-6 → hepcidin → FPN internalization → iron trapping in macrophages and enterocytes → hypoferremia → iron-restricted erythropoiesis; FPN is also the therapeutic target — anti-HJV antibodies and ERFE mimetics restore FPN."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "IL-12 links chronic infection to ACD: IL-12 → IFN-γ + TNF-α → macrophage activation → IL-6 → hepcidin; IL-12-driven Th1 inflammation is characteristic of TB, HIV, and leishmaniasis; blocking IL-12 (ustekinumab) partially attenuates ACD but increases infection risk."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "TB is a major cause of ACD: MTB infection → sustained IL-6 + TNF-α + IFN-γ → hepcidin elevation → functional iron deficiency; ACD severity tracks TB activity; successful TB treatment restores haemoglobin; IL-12/IFN-γ activation is the predominant immune driver."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "HIV is a major driver of ACD in sub-Saharan Africa: chronic viral replication + immune activation → IL-6 + IFN-γ → hepcidin elevation → functional iron deficiency; AZT directly suppresses erythropoiesis; ACD severity tracks viral load and CD4 depletion."
  - target: 01-human/07-system/leishmaniasis
    relation: connects-to
    note: "Visceral leishmaniasis causes severe ACD: chronic Leishmania infection drives IL-6 + IFN-γ + TNF-α → hepcidin → hypoferremia; BM infiltration, hypersplenism, and haemolysis compound VL anemia; successful L-AmB treatment eliminates inflammatory stimulus and resolves ACD."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Anemia of chronic disease and IDA are the two commonest anemias and key differentials: both can be microcytic with low serum iron, but ACD has normal/high ferritin with hepcidin-trapped macrophage iron, while IDA has low ferritin from true depletion; combined ACD+IDA is common."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages drive anemia of chronic disease: inflammatory IL-6 raises hepcidin, which degrades macrophage ferroportin so recycled iron from senescent red cells stays locked inside (reticuloendothelial block); serum iron falls while macrophage and ferritin iron stores rise."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Rheumatoid arthritis is a prototypical cause of anemia of chronic disease: sustained IL-6 and inflammation raise hepcidin, sequestering iron and blunting erythropoiesis, so anemia tracks disease activity; effective immunosuppression (IL-6 blockade, DMARDs) often corrects it."
---

# Anemia of Chronic Disease

## Overview

**Anemia of chronic disease (ACD)**, also known as **anemia of inflammation (AI)**, is the **second most common anemia worldwide** after iron deficiency anemia, affecting hundreds of millions of people — predominantly those with chronic infection, autoimmune disease, malignancy, and chronic kidney disease (CKD) [^weiss-2005-acd-review]. Unlike iron deficiency anemia (IDA), ACD occurs despite **adequate or elevated iron stores**: the iron is present but functionally unavailable — sequestered within macrophages and hepatocytes by hepcidin-mediated ferroportin degradation, unable to reach the bone marrow for erythropoiesis.

The central molecular mechanism is the **IL-6 → STAT3 → hepcidin → ferroportin axis** [^nemeth-2004-il6-hepcidin]:
1. Chronic inflammation → sustained IL-6 production from macrophages/monocytes
2. IL-6 → hepatocyte STAT3 → HAMP promoter → elevated hepcidin (3-10× normal)
3. High hepcidin → ferroportin internalization/lysosomal degradation → iron trapping in macrophages and hepatocytes
4. Bone marrow iron shortage → iron-restricted erythropoiesis → normocytic or microcytic anemia

ACD is compounded by additional inflammation-driven mechanisms: **EPO hyporesponsiveness** (IFN-γ, TNF-α blunt EPO signaling on erythroid progenitors), **shortened RBC lifespan** (increased macrophage erythrophagocytosis), and **suppressed EPO production** (TNF-α, IL-1β inhibit renal EPO synthesis). These combined effects make ACD resistant to iron supplementation alone and frequently require treatment of the underlying disease.

**Clinical features:**
- Usually **mild to moderate** anemia (Hgb 8–11 g/dL); rarely severe unless compounded by bleeding, hemolysis, or advanced CKD
- Typically **normocytic, normochromic** (MCV 80–100 fL); can become microcytic if iron stores become truly depleted (ACD+IDA overlap)
- Develops **gradually** over weeks to months of chronic inflammation
- Symptom burden correlates with Hgb level and the underlying condition (fatigue, dyspnea, reduced quality of life)

## Structure

### Pathophysiological framework

**Multi-pathway model of ACD:**

| Mechanism | Driver | Effect on Erythropoiesis |
|:----------|:-------|:------------------------|
| Iron sequestration (hepcidin-mediated) | IL-6 → STAT3 → hepcidin → ferroportin degradation | Functional iron deficiency — stores elevated but unavailable |
| EPO suppression | TNF-α, IL-1β, IFN-γ → ↓renal EPO synthesis; direct CKD effect | Insufficient EPO stimulus for erythroid expansion |
| EPO hyporesponsiveness | IFN-γ, TNF-α → blunted EPO-R signaling; iron shortage limits response | Erythroid progenitors fail to respond to available EPO |
| Shortened RBC lifespan | Macrophage activation → increased erythrophagocytosis; low-grade hemolysis | Reduced RBC survival (120 days → ~80 days in ACD) |
| Inhibited erythroid differentiation | IFN-γ → apoptosis of BFU-E/CFU-E in bone marrow | Reduced erythroid colony formation |

**Iron compartmentalization in ACD (vs. IDA):**

| Iron Parameter | ACD | IDA | ACD+IDA |
|:--------------|:----|:----|:--------|
| Serum iron | Low | Low | Low |
| TIBC/transferrin | Low or normal | High | Low or normal |
| Transferrin saturation | Low-normal | Very low | Low |
| Serum ferritin | Normal to high | <30 ng/mL | Low-normal (acute phase) |
| Soluble TfR (sTfR) | Low-normal | High | High |
| sTfR/log ferritin index | <1 | >2 | >2 |
| Hepcidin | High | Very low | Variable |
| Reticulocyte Hgb (CHr) | Low | Low | Low |
| Bone marrow iron | Normal to high | Absent | Low |

**Key diagnostic pearl:** Ferritin is an acute-phase reactant — it rises during inflammation even when iron stores are genuinely low, masking IDA in the ACD setting. The **sTfR/log ferritin index** (>2 indicates an IDA component) is less affected by inflammation and is the best single test to detect concurrent IDA in an inflamed patient.

## Function

### Nutritional immunity — the adaptive role of ACD

The hepcidin-driven iron sequestration of ACD is not purely pathological. **Nutritional immunity** is the evolutionary strategy of withholding iron from pathogens (bacteria, fungi, intracellular parasites require iron for growth) by reducing circulating transferrin-bound iron. In acute infection, ACD-like hypoferremia is a **deliberate innate immune mechanism**: iron restriction limits pathogen replication, while the bone marrow tolerates temporary anemia better than systemic bacteremia [^ganz-2019-acd-iron].

This adaptive rationale explains why **aggressive iron supplementation during active infection can be harmful** — parenteral iron in bacteremic patients increases free iron → pathogen growth → worsened outcomes (demonstrated in neonatal malaria trials and suggested in critical illness studies).

### Disease associations

**Infections:**
- Chronic bacterial infections (TB, osteomyelitis, endocarditis)
- HIV, hepatitis C, parasitic infections (malaria, visceral leishmaniasis)

**Autoimmune/inflammatory diseases:**
- **Rheumatoid arthritis** — most studied ACD association; Hgb inversely correlates with ESR/CRP; treat underlying disease (DMARDs); tocilizumab (anti-IL-6R) rapidly reverses ACD via hepcidin suppression
- **SLE** — multifactorial anemia (ACD + autoimmune hemolytic anemia + drug effects)
- **IBD (Crohn's/UC)** — ACD + true IDA (mucosal bleeding) coexist; ferritin unreliable; sTfR index + CRP-adjusted ferritin thresholds used; IV iron (ferric carboxymaltose) preferred
- **AOSD (adult-onset Still's disease)** — dramatic ACD with hyperferritinemia; macrophage activation also contributes
- **Vasculitis (GCA, AAV)** — IL-6-driven ACD; resolves with immunosuppression

**CKD/ESRD:**
- CKD-related anemia = ACD + EPO deficiency (uremic suppression of renal EPO synthesis) + shortened RBC lifespan
- Most common indication for ESA therapy (KDIGO target: Hgb 10-11.5 g/dL)

**Malignancy:**
- Cancer-related ACD affects ~40% of cancer patients
- Compounded by: bone marrow invasion, chemotherapy toxicity, gastrointestinal bleeding, hemolysis

## Pathology

### Diagnosis

**Diagnostic approach:**
1. Confirm anemia and assess severity/morphology (CBC, peripheral smear)
2. Establish underlying chronic disease context (clinical + CRP/ESR/ferritin)
3. Iron studies: serum iron + TIBC + transferrin saturation + serum ferritin
4. Distinguish ACD vs. IDA vs. ACD+IDA:
   - ACD: ferritin normal/high + low TSAT + normal sTfR + elevated CRP
   - IDA: ferritin <30 ng/mL + very low TSAT + high sTfR + normal CRP
   - ACD+IDA: "normal" ferritin may mask true IDA; sTfR/log ferritin index >2 indicates IDA
5. Additional: reticulocyte count, reticulocyte hemoglobin (CHr), soluble TfR
6. Bone marrow biopsy with Prussian blue stain: gold standard (stainable iron present in macrophages but absent from erythroid precursors = ACD)

### Treatment [^weiss-2005-acd-review]

**1. Treat the underlying cause — most effective strategy:**
- RA/autoimmune disease: DMARDs, IL-6R blockade (tocilizumab) → IL-6 falls → hepcidin falls → iron mobilizes → Hgb rises within 4-8 weeks
- Infection: Eradicate organism → hepcidin normalization → anemia resolves
- IBD: Induce remission with biologics/5-ASA
- Cancer: Chemotherapy/surgery targeting tumor → inflammation subsides

**2. Iron supplementation:**
- **Oral iron:** Minimally effective in pure ACD (hepcidin degrades intestinal ferroportin → absorbed iron cannot exit enterocyte); useful only if concurrent true IDA
- **IV iron (ferric carboxymaltose, iron sucrose, ferric gluconate):** Bypasses intestinal absorption; effective in CKD-related anemia and IBD-related anemia; less effective in pure ACD without true iron depletion
- KDIGO threshold for IV iron in CKD: ferritin <500 ng/mL + TSAT <30% in ESA-treated patients

**3. Erythropoiesis-stimulating agents (ESAs):**
- **Epoetin alfa, darbepoetin alfa** — stimulate erythroid progenitor proliferation via EPO receptor
- **Indications:** CKD-related anemia (Hgb <10 g/dL); chemotherapy-related anemia when cure is not expected
- **Target Hgb:** 10-11.5 g/dL; avoid >13 g/dL (↑VTE and CV events — FDA black box)
- **ESA hyporesponsiveness:** Functional iron deficiency (persistent high hepcidin) is the most common cause → co-administer IV iron
- **Not indicated:** Non-chemotherapy cancer anemia, surgical anemia, anemia of aging

**4. Transfusion:**
- For severe symptomatic anemia (Hgb <7-8 g/dL) or rapid-onset cardiovascular compromise
- Leukoreduced PRBCs; avoid overtransfusion; restrictive strategy (Hgb <7 g/dL trigger in stable patients)

**5. Emerging therapies:**
- **HIF prolyl hydroxylase inhibitors (HIF-PHIs):** Roxadustat, daprodustat, vadadustat — stabilize HIF-2α → EPO synthesis + hepcidin suppression; FDA-approved for dialysis CKD-anemia (roxadustat REMS program 2023); approved broadly in EU/China
- **Luspatercept (Reblozyl):** Activin receptor ligand trap → promotes late-stage erythroid maturation; FDA-approved for MDS-related anemia (2020) and beta-thalassemia; phase 2 studies in ACD/CKD
- **Hepcidin pathway antagonists (investigational):** Anti-HJV antibodies, ERFE mimetics, anti-TMPRSS6 siRNA; clinical trials ongoing for ACD

## Connections

- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Hepcidin is the central molecular effector of ACD: IL-6 → STAT3 → hepcidin → ferroportin degradation → iron sequestration in macrophages/hepatocytes → hypoferremia → iron-restricted erythropoiesis; hepcidin pathway inhibitors (anti-HJV, ERFE mimetics) under development for ACD.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — IL-6 is the primary upstream driver of ACD: IL-6 from macrophages in infection/autoimmune disease/malignancy → STAT3 → hepcidin → ferroportin degradation → iron-restricted erythropoiesis; IL-6 also suppresses EPO production → blunted erythropoietic response.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — EPO production is suppressed in ACD by TNF-α/IL-1β/IFN-γ and EPO-R signaling is blunted by inflammatory cytokines → EPO hyporesponsiveness; ESAs (epoetin, darbepoetin) are used in CKD-ACD with Hgb target 10-11.5 g/dL; HIF-PHIs restore EPO while suppressing hepcidin.
- `connects-to` → **[CKD](../ckd/README.md)** — CKD anemia combines EPO deficiency (from peritubular cell loss) with ACD-driven hepcidin elevation and functional iron deficiency; target Hgb 10-11.5 g/dL with ESA + IV iron; HIF-PHIs (roxadustat) treat CKD anemia by restoring EPO and suppressing hepcidin simultaneously.
- `connects-to` → **[Ferroportin](../../03-molecular/ferroportin/README.md)** — Ferroportin is the cellular target of hepcidin in ACD; IL-6 → hepcidin → FPN internalization → iron trapping in macrophages and enterocytes → hypoferremia → iron-restricted erythropoiesis; FPN is also the therapeutic target — anti-HJV antibodies and ERFE mimetics restore FPN.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — IL-12-driven Th1 inflammation is the predominant immune mechanism linking chronic intracellular infection to ACD: IL-12 → IFN-γ + TNF-α → IL-6 → hepcidin; chronic IL-12/IFN-γ-driven diseases (TB, HIV, leishmaniasis) are classic ACD causes; IL-12-mediated nutritional immunity withholds iron from both pathogens and erythroid progenitors.
- `connects-to` → **[Tuberculosis](../tuberculosis/README.md)** — TB is a leading global cause of ACD: MTB-driven IL-6 + TNF-α + IFN-γ → hepcidin elevation → functional iron deficiency and normochromic normocytic anemia; ACD severity tracks TB disease activity (smear positivity, cavitary disease); successful TB treatment typically resolves ACD within weeks to months.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — HIV is a major ACD driver in sub-Saharan Africa: chronic viral replication + immune activation → elevated IL-6 + IFN-γ → hepcidin-mediated iron sequestration; AZT (zidovudine) directly suppresses erythropoiesis (bone marrow toxicity); anemia severity correlates with viral load and CD4 depletion and responds to ART.
- `connects-to` → **[Leishmaniasis](../leishmaniasis/README.md)** — Visceral leishmaniasis causes severe ACD: chronic Leishmania infection drives IL-6 + IFN-γ + TNF-α → hepcidin → hypoferremia; BM infiltration, hypersplenism, and haemolysis compound VL anemia; successful L-AmB treatment eliminates inflammatory stimulus and resolves ACD.
- `connects-to` → **[Iron Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Anemia of chronic disease and IDA are the two commonest anemias and key differentials: both can be microcytic with low serum iron, but ACD has normal/high ferritin with hepcidin-trapped macrophage iron, while IDA has low ferritin from true depletion; combined ACD+IDA is common.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages drive anemia of chronic disease: inflammatory IL-6 raises hepcidin, which degrades macrophage ferroportin so recycled iron from senescent red cells stays locked inside (reticuloendothelial block); serum iron falls while macrophage and ferritin iron stores rise.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Rheumatoid arthritis is a prototypical cause of anemia of chronic disease: sustained IL-6 and inflammation raise hepcidin, sequestering iron and blunting erythropoiesis, so anemia tracks disease activity; effective immunosuppression (IL-6 blockade, DMARDs) often corrects it.

[^weiss-2005-acd-review]: Weiss G, Goodnough LT. Anemia of chronic disease. *N Engl J Med.* 2005;352(10):1011-1023. [doi:10.1056/NEJMra041809](https://doi.org/10.1056/NEJMra041809) · [PubMed 15758012](https://pubmed.ncbi.nlm.nih.gov/15758012/)
[^nemeth-2004-il6-hepcidin]: Nemeth E, Rivera S, Gabayan V, et al. IL-6 mediates hypoferremia of inflammation by inducing the synthesis of the iron regulatory hormone hepcidin. *J Clin Invest.* 2004;113(9):1271-1276. [doi:10.1172/JCI200420945](https://doi.org/10.1172/JCI200420945) · [PubMed 15124018](https://pubmed.ncbi.nlm.nih.gov/15124018/)
[^ganz-2019-acd-iron]: Ganz T. Anemia of Inflammation. *N Engl J Med.* 2019;381(12):1148-1157. [doi:10.1056/NEJMra1916038](https://doi.org/10.1056/NEJMra1916038) · [PubMed 31532961](https://pubmed.ncbi.nlm.nih.gov/31532961/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

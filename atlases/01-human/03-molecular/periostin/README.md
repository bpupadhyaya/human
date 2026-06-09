---
schema: human-scale-entry/v1
id: periostin
name: Periostin
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "Periostin (POSTN, chr13q13.3) is an ECM matricellular protein induced by IL-4/IL-13 → STAT6 and TGF-β → SMAD3; serum periostin >25 ng/mL predicts T2-high asthma biologic response; periostin drives cardiac and renal fibrosis via integrin αvβ3/αvβ5 → FAK/PI3K."
aliases: ["periostin", "POSTN", "osteoblast-specific factor 2", "OSF-2", "OSF2", "PDLP"]
cross_links:
  - target: 01-human/07-system/asthma
    relation: connects-to
    note: "Serum periostin >25 ng/mL identifies T2-high eosinophilic asthma regardless of blood eosinophil count; periostin from sub-epithelial fibroblasts (IL-13/IL-4 → STAT6 → POSTN) contributes to airway subepithelial fibrosis; periostin biomarker guided lebrikizumab trial design."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Periostin from cardiac fibroblasts → integrin αvβ3 on cardiomyocytes and fibroblasts → FAK/PI3K → myofibroblast differentiation and collagen I/III deposition; periostin is required for post-MI cardiac fibrosis (periostin-null mice have impaired scar formation)."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β1 is the primary periostin inducer in cardiac fibroblasts and lung fibroblasts via SMAD2/3 → POSTN promoter; periostin → integrin αvβ3 → FAK → PI3K → Akt → further TGF-β1 production (amplification loop); IL-4/IL-13 → STAT6 is the secondary inducer in airway/skin fibroblasts."
  - target: 01-human/07-system/atopic-dermatitis
    relation: connects-to
    note: "Periostin is a type 2 biomarker in AD: IL-4/IL-13 → STAT6 → dermal fibroblast POSTN → serum periostin correlates with AD severity; dermal periostin → integrin αvβ3 on keratinocytes → TSLP production; periostin tracks type 2 skin inflammation and dupilumab response."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "TGF-β1 → periostin in hepatic stellate cells → integrin αvβ3 → FAK/PI3K → collagen I/III deposition → hepatic fibrosis in NASH; periostin correlates with fibrosis stage; periostin-null mice develop less hepatic fibrosis in NASH models; periostin marks activated stellate cells."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Periostin drives fibrotic remodeling in chronic lung disease: TGF-β + IL-13 → POSTN in lung fibroblasts → collagen matrix assembly → subepithelial fibrosis; serum periostin correlates with lung function decline in asthma and IPF; marks remodeling distinct from acute inflammation."
sources:
  - id: takayama-2006-periostin-asthma
    type: peer-reviewed
    cite: "Takayama G, Arima K, Kanaji T, et al. Periostin: a novel component of subepithelial fibrosis of bronchial asthma downstream of IL-4 and IL-13 signals. J Allergy Clin Immunol. 2006;118(1):98-104."
    doi: "10.1016/j.jaci.2006.02.046"
    pmid: "16815146"
    url: "https://doi.org/10.1016/j.jaci.2006.02.046"
  - id: norris-2008-periostin-cardiac
    type: peer-reviewed
    cite: "Oka T, Xu J, Kaiser RA, et al. Genetic manipulation of periostin expression reveals a role in cardiac hypertrophy and ventricular remodeling. Circ Res. 2007;101(3):313-321."
    doi: "10.1161/CIRCRESAHA.107.149047"
    pmid: "17589016"
    url: "https://doi.org/10.1161/CIRCRESAHA.107.149047"
---

# Periostin

## Overview

**Periostin** (osteoblast-specific factor 2; gene *POSTN*, chromosome 13q13.3) is a **secreted matricellular protein** belonging to the fasciclin domain family — non-structural ECM proteins that coordinate cell-matrix communication during tissue remodeling, wound healing, and fibrosis. First identified as an osteoblast-specific factor in the periosteum (hence "periostin"), it is now recognized as a **multifunctional mediator of fibrosis and inflammation** expressed in response to **TGF-β1 (SMAD2/3)** and **IL-4/IL-13 (STAT6)** in fibroblasts, airway epithelium, and cardiac tissue — making it uniquely positioned at the interface of type 2 allergy and structural tissue disease.

Periostin's dual induction by both TGF-β (the master fibrosis cytokine) and the type 2 Th2 cytokines (IL-4/IL-13) means it is elevated in:
1. **Type 2-high asthma** — airway subepithelial fibrosis; serum periostin = validated T2 biomarker; guided the design of IL-13-targeting trials (lebrikizumab)
2. **Atopic dermatitis** — skin fibrosis (lichenification) and barrier reinforcement; periostin promotes keratinocyte differentiation
3. **Cardiac fibrosis** — post-myocardial infarction scar maturation; periostin-null mice have impaired cardiac repair; elevated serum periostin in heart failure patients

## Structure

**Periostin protein architecture (836 aa, ~90 kDa):**
- **Signal peptide (aa 1–21):** Secretory ER entry; cleaved → mature secreted form
- **EMI domain (aa 22–90):** Cysteine-rich N-terminal EMI (emilin) module; mediates periostin-periostin oligomerization and collagen cross-linking; EMI domain of periostin interacts with BMP-1/tolloid to enhance collagen fibril maturation
- **Fasciclin 1 (FAS1) repeat 1 and 2 (aa ~91–350):** First two β-strand-rich fasciclin domains; bind fibronectin and tenascin-C; these interactions assemble the ECM provisional matrix scaffold
- **Fasciclin 1 (FAS1) repeat 3 and 4 (aa ~351–640):** Bind integrins (αvβ3, αvβ5, αvβ1, α4β6); contain RGD-like motifs; primary pro-fibrotic signaling surfaces; αvβ3 binding → FAK Tyr397 autophosphorylation
- **C-terminal domain (aa ~641–836):** Heparin-binding; ECM anchoring; SMAD3-binding interface
- **Splice variants:** At least 8 splice variants identified via alternative exon inclusion in the C-terminal region; variants differentially regulate integrin specificity, matrix binding, and anti-apoptotic activity

**Transcriptional regulation:**
- **IL-4/IL-13 → STAT6:** Airway subepithelial fibroblasts and airway smooth muscle cells → STAT6 → POSTN promoter activation → periostin secretion into airway submucosa; this is the dominant pathway in allergic asthma and AD; both dupilumab and anti-IL-13 therapies reduce serum periostin as pharmacodynamic readout
- **TGF-β1 → SMAD2/3:** Cardiac fibroblasts, lung fibroblasts, renal interstitial fibroblasts → POSTN transcription; dominant in non-allergic fibrosis (post-MI, IPF, CKD)
- **Wnt/β-catenin:** Co-activates POSTN in osteoblasts and cancer-associated fibroblasts
- **BMP-2:** Activates POSTN in osteoblasts and periosteal progenitors → bone remodeling context

**Integrin signaling (pro-fibrotic mechanism):**
Periostin → integrin αvβ3 (or αvβ5) on fibroblasts → FAK (focal adhesion kinase, Tyr397) → SFK (Src) → **PI3K → Akt → mTORC1** → proliferation and survival; FAK → **Rac1/RhoA → ROCK** → cytoskeletal reorganization → myofibroblast α-SMA upregulation → collagen I/III/V secretion; also activates **MAPK/ERK** → MMP-2/9 → ECM degradation/remodeling.

## Function

**Asthma — subepithelial fibrosis and biomarker:**
- Airway subepithelial fibrosis (reticular basement membrane thickening ≥8 μm in severe asthma) is driven by IL-4/IL-13 → STAT6 → periostin from sub-epithelial fibroblasts → integrin αvβ3 → myofibroblast transition → collagen III/V deposition
- Periostin also promotes airway smooth muscle proliferation (integrin αvβ3 → FAK → MAPK) → increased ASM mass → BHR amplification
- **Serum periostin as T2 biomarker:** Liver-derived serum periostin (distinct from local airway periostin — regulated by IL-4/IL-13 via soluble POSTN from fibroblasts circulating after shedding) correlates with IL-13 activity, eosinophilia, and FeNO; serum periostin ≥25 ng/mL identifies T2-high asthma with sensitivity ~70%, specificity ~65%
- **Lebrikizumab trials (IL-13 blockade):** Periostin-high patients (baseline >25 ng/mL) had greater response to lebrikizumab: 60% reduction in exacerbations vs. 5% in periostin-low → periostin prospectively guided enrichment strategy [^takayama-2006-periostin-asthma]

**Atopic dermatitis:**
- IL-4/IL-13 → dermal fibroblast STAT6 → periostin → epidermis → integrin αvβ3 on keratinocytes → FAK/ERK → keratinocyte adhesion and differentiation, including involucrin and cornified envelope protein expression
- Periostin → keratinocyte-derived TSLP → amplification of the allergic cascade (periostin-TSLP loop)
- Lesional AD skin has 3-10× higher periostin than non-lesional AD; periostin-null mice resist IL-4-induced dermatitis in murine models
- Serum periostin correlates with AD severity (EASI score) and decreases with dupilumab therapy

**Cardiac fibrosis and remodeling [^norris-2008-periostin-cardiac]:**
- Normal adult myocardium: periostin is nearly undetectable; dramatically induced in cardiac fibroblasts by TGF-β1 after myocardial infarction, pressure overload (aortic banding), and dilated cardiomyopathy
- Periostin → integrin αvβ3/αvβ5 on cardiac fibroblasts → FAK → MAPK + PI3K/Akt → myofibroblast differentiation → collagen I secretion → infarct scar formation; periostin also maintains cardiac fibroblast survival in the hypoxic peri-infarct zone
- **Periostin-null mice post-MI:** Impaired collagen cross-linking → thinner infarct scar → increased ventricular rupture risk; BUT surviving periostin-null mice had better long-term cardiac function → paradox: periostin is necessary for scar integrity but limits adaptive remodeling
- Cardiac hypertrophy: periostin promotes cardiomyocyte hypertrophy via integrin-FAK-Akt pathway → calcineurin → NFAT → fetal gene program; serum periostin elevated in HFpEF patients and correlates with myocardial fibrosis on cardiac MRI

**Bone and periosteum:**
- Original identification context: periosteum osteoblasts, periodontal ligament cells; periostin → integrin signaling → osteoblast differentiation and mineralization; periostin organizes collagen fibrils in cortical bone; periostin-null mice have reduced bone density and impaired fracture healing

## Mechanism

**Periostin as asthma biomarker in biologic selection:**
Serum periostin (commercial ELISA: Shino-Test periostin assay) is used to identify T2-high asthma patients:
- **Periostin ≥25 ng/mL:** Predicts response to IL-13-targeting (lebrikizumab, tralokinumab) better than eosinophils alone; particularly useful in "T2-discordant" patients with elevated periostin but low blood eosinophils (<300/μL) — who still respond to IL-13 blockade
- Combined biomarker strategy: FeNO (≥25 ppb) + periostin (≥25 ng/mL) + blood eosinophils (≥300/μL) → different T2 axes; combination predicts biologic response more reliably than any single marker
- **Clinical utility limitation:** Serum periostin varies with age (decreases with age), osteoarthritis, renal function, and bone metabolism — reducing specificity in older patients; FeNO has better signal-to-noise in severe asthma

**Periostin in IPF (idiopathic pulmonary fibrosis):**
- IPF: TGF-β1 from alveolar macrophages → lung fibroblast periostin → collagen remodeling in the UIP (usual interstitial pneumonia) pattern → honeycomb lung destruction
- Serum periostin correlates with IPF severity (FVC, DLCO) and predicts mortality; elevated >95th percentile in IPF vs. healthy controls
- Periostin → integrin αvβ3 on IPF fibroblasts → PI3K → elevated FAK activation → reduced sensitivity to nintedanib (TKI) in some studies → potential resistance mechanism

## Connections

- `connects-to` → **[Asthma](../../07-system/asthma/README.md)** — Serum periostin >25 ng/mL identifies T2-high eosinophilic asthma; IL-13/IL-4 → STAT6 → POSTN in sub-epithelial fibroblasts → airway subepithelial fibrosis; periostin biomarker guided lebrikizumab trial enrichment strategy; correlates with eosinophilic exacerbation risk.
- `connects-to` → **[Heart Failure](../../07-system/heart-failure/README.md)** — Periostin from cardiac fibroblasts → integrin αvβ3 on cardiomyocytes and fibroblasts → FAK/PI3K → myofibroblast differentiation and collagen I/III deposition; periostin is required for post-MI cardiac fibrosis (periostin-null mice have impaired scar formation).
- `connects-to` → **[TGF-beta](../tgf-beta/README.md)** — TGF-β1 is the primary periostin inducer in cardiac and lung fibroblasts via SMAD2/3 → POSTN promoter; periostin → integrin αvβ3 → FAK → Akt → further TGF-β1 production (amplification loop); IL-4/IL-13 → STAT6 is the secondary inducer in airway/skin fibroblasts.
- `connects-to` → **[Atopic Dermatitis](../../07-system/atopic-dermatitis/README.md)** — Periostin is a type 2 biomarker in AD: IL-4/IL-13 → STAT6 → dermal fibroblast POSTN → serum periostin correlates with AD severity; dermal periostin → integrin αvβ3 on keratinocytes → TSLP production; periostin tracks type 2 skin inflammation and dupilumab response.
- `connects-to` → **[NASH](../../07-system/nash/README.md)** — TGF-β1 → periostin in hepatic stellate cells → integrin αvβ3 → FAK/PI3K → collagen I/III deposition → hepatic fibrosis in NASH; periostin correlates with fibrosis stage; periostin-null mice develop less hepatic fibrosis in NASH models; periostin marks activated stellate cells.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Periostin drives fibrotic remodeling in chronic lung disease: TGF-β + IL-13 → POSTN in lung fibroblasts → collagen matrix assembly → subepithelial fibrosis; serum periostin correlates with lung function decline in asthma and IPF; marks remodeling distinct from acute inflammation.

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^takayama-2006-periostin-asthma]: Takayama G, Arima K, Kanaji T, et al. Periostin: a novel component of subepithelial fibrosis of bronchial asthma downstream of IL-4 and IL-13 signals. *J Allergy Clin Immunol.* 2006;118(1):98-104. [doi:10.1016/j.jaci.2006.02.046](https://doi.org/10.1016/j.jaci.2006.02.046) · [PubMed 16815146](https://pubmed.ncbi.nlm.nih.gov/16815146/)
[^norris-2008-periostin-cardiac]: Oka T, Xu J, Kaiser RA, et al. Genetic manipulation of periostin expression reveals a role in cardiac hypertrophy and ventricular remodeling. *Circ Res.* 2007;101(3):313-321. [doi:10.1161/CIRCRESAHA.107.149047](https://doi.org/10.1161/CIRCRESAHA.107.149047) · [PubMed 17589016](https://pubmed.ncbi.nlm.nih.gov/17589016/)

---
schema: human-scale-entry/v1
id: ovarian-clear-cell-carcinoma
name: Ovarian Clear Cell Carcinoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Ovarian clear cell carcinoma (OCCC) is an endometriosis-derived subtype; ARID1A (~50%) and PIK3CA (~50%) are hallmark mutations; platinum-resistant; no FDA-approved targeted therapy; higher incidence in Asian women; mTOR inhibitors and EZH2 inhibitors under investigation."
aliases: ["OCCC", "ovarian clear cell carcinoma", "clear cell ovarian cancer", "endometriosis-associated ovarian cancer", "ARID1A ovarian cancer", "PIK3CA ovarian clear cell", "clear cell adenocarcinoma ovary", "endometrioid-related ovarian cancer", "ovarian cancer clear cell", "CCC ovarian"]
sources:
  - id: jones-2010-arid1a-occc
    type: peer-reviewed
    cite: "Jones S, Wang TL, Shih IeM, et al. Frequent mutations of chromatin remodeling gene ARID1A in ovarian clear cell carcinoma. Science. 2010;330(6001):228-231."
    doi: "10.1126/science.1196333"
    pmid: "20826764"
    url: "https://doi.org/10.1126/science.1196333"
  - id: kim-2015-arid1a-ezh2
    type: peer-reviewed
    cite: "Kim KH, Kim W, Howard TP, et al. SWI/SNF-mutant cancers depend on catalytic and non-catalytic activity of EZH2. Nat Med. 2015;21(12):1491-1496."
    doi: "10.1038/nm.3968"
    pmid: "26552009"
    url: "https://doi.org/10.1038/nm.3968"
cross_links:
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A (BAF250A) is mutated in ~50% of OCCC; biallelic ARID1A LOF → cBAF disruption; ARID1A IHC (BAF250A, clone PSG3) protein loss is a surrogate diagnostic marker in OCCC; ARID1A + PIK3CA co-mutation in ~25-30% OCCC defines the highest-risk molecular subgroup."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "ARID1A LOF disrupts cBAF → EZH2/PRC2 accesses ARID1A-target loci → H3K27me3 accumulation; OCCC with ARID1A LOF shows EZH2 dependency in preclinical models; tazemetostat under investigation in ARID1A-mutant OCCC; EZH2 + PARP inhibitor combination explored."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "ARID1A + PIK3CA co-mutation defines ~25-30% of ovarian clear cell carcinomas; PIK3CA → PI3K/AKT/mTOR → OCCC proliferation; ARID1A LOF + PIK3CA creates synthetic vulnerability to dual PI3K/mTOR inhibition; temsirolimus active in PIK3CA-mutant OCCC Phase 2."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "ARID1A LOF in OCCC → PD-L1 upregulation via MLH1 suppression and IFN-γ signaling pathway enhancement; OCCC has higher PD-L1 expression than high-grade serous ovarian cancer; pembrolizumab + bevacizumab shows activity in PD-L1+ OCCC; durvalumab combination trials ongoing."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "PIK3CA mutations (~40-50%) in OCCC → PI3K/AKT → mTOR activation; temsirolimus Phase 2 in OCCC: ORR ~10-15%; alpelisib (PIK3CA inhibitor) explored in PIK3CA-mutant OCCC; PI3K/mTOR dual inhibitors studied; ARID1A LOF + PIK3CA → synthetic vulnerability to PI3K/mTOR inhibition."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "KRAS G12D/V mutations in ~15% of OCCC, enriched in endometriosis-associated OCCC; KRAS + ARID1A co-mutation in ~8-10%; MEK pathway activated in KRAS-mutant OCCC → MEK inhibitors explored; KRAS mutation is more prevalent in OCCC than HGSOC or endometrioid ovarian cancer."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "OCCC is distinct from HGSOC: OCCC (ARID1A/PIK3CA-driven, platinum-resistant, stage I-II at ~35-40%) vs HGSOC (TP53-universal, platinum-sensitive, stage III-IV at ~75%); OCCC lacks HRD enrichment; 5-year OS in advanced OCCC is worse than HGSOC despite identical chemotherapy."
  - target: 01-human/07-system/endometrial-cancer
    relation: connects-to
    note: "Ovarian clear cell carcinoma and endometrioid endometrial cancer are both endometriosis/endometrium-derived tumors driven by ARID1A and PIK3CA; clear-cell and endometrioid histologies recur across ovary and uterus, and both can arise in Lynch syndrome — unlike serous cancers."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "Ovarian clear cell carcinoma and clear-cell renal cell carcinoma are unrelated organs sharing a look and biology: both have glycogen-rich clear cytoplasm, both upregulate HIF/VEGF, and OCCC borrows RCC anti-angiogenics like sunitinib for this platinum-resistant tumor."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Ovarian clear cell carcinoma is more immunogenic than high-grade serous cancer: ARID1A loss raises neoantigens and PD-L1, so it draws cytotoxic CD8+ T cells and responds better to PD-1 blockade — pembrolizumab + bevacizumab is studied in PD-L1+ OCCC."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Ovarian clear cell carcinoma has the highest venous thromboembolism rate of any ovarian cancer—up to a quarter of patients: the tumor is strongly prothrombotic (tissue factor, IL-6), so DVT and pulmonary embolism are watched and often prophylaxed throughout treatment."
  - target: 01-human/07-system/lynch-syndrome
    relation: connects-to
    note: "Clear-cell and endometrioid ovarian cancers are the histologies linked to Lynch syndrome: mismatch-repair deficiency underlies a share of OCCC, so MMR/MSI testing both flags a germline syndrome and identifies tumors that may respond to checkpoint blockade."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Ovarian clear cell carcinoma is the ovarian cancer most tied to endometriosis: ectopic endometrial tissue, under oxidative iron-rich stress, acquires ARID1A and PIK3CA mutations and transforms—making endometriosis a recognized precursor in the reproductive tract."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "Ovarian clear-cell carcinoma and gastric cancer share ARID1A loss: this SWI/SNF chromatin-remodeler tumor suppressor is among the most mutated genes in both, showing how chromatin disruption—not classic oncogenes—drives diverse epithelial cancers."
  - target: 01-human/07-system/cholangiocarcinoma
    relation: connects-to
    note: "Ovarian clear-cell carcinoma and cholangiocarcinoma converge on chromatin-remodeling defects: both frequently lose ARID1A, and both are relatively chemoresistant epithelial cancers—making epigenetic vulnerabilities (EZH2 inhibition) a shared therapeutic avenue."
  - target: 01-human/07-system/hereditary-breast-ovarian-cancer
    relation: connects-to
    note: "Ovarian clear-cell carcinoma differs from the BRCA-driven cancers of HBOC: unlike high-grade serous ovarian cancer, clear-cell is rarely BRCA/HRD-related (it's ARID1A/PIK3CA-driven), so it responds poorly to platinum and PARP inhibitors—a key treatment distinction."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "OCCC is driven by PI3K-pathway and chromatin gene mutations: ARID1A loss with PIK3CA or PTEN alterations activates PI3K/AKT/mTOR growth signaling, distinguishing clear cell carcinoma's biology—and rationale for mTOR/PI3K-targeted trials—from high-grade serous cancer."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "OCCC tends to be immunologically distinct and PD-L1-expressing: among ovarian cancers, clear cell carcinoma more often shows mismatch-repair/ARID1A features and immune infiltration, so NK and T-cell-engaging immunotherapy is of interest in this platinum-resistant subtype."
  - target: 01-human/07-system/vhl-disease
    relation: connects-to
    note: "OCCC shares clear-cell morphology and biology with renal clear cell carcinoma: glycogen-rich clear cytoplasm and HIF/VEGF-driven angiogenesis link it to VHL-associated kidney cancer, so anti-angiogenic agents are explored across these histologically similar tumors."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "Ovarian clear cell carcinoma is characteristically p53-wildtype: unlike high-grade serous ovarian cancer, which is defined by TP53 mutation, OCCC is driven instead by ARID1A and PIK3CA—so p53 status helps distinguish these biologically distinct ovarian cancers."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Ovarian clear cell carcinoma resists platinum chemo but its ARID1A loss links to immunotherapy: ARID1A-mutant or mismatch-repair-deficient tumors can respond to checkpoint blockade, offering an option in this otherwise chemoresistant subtype."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "OCCC's clear cytoplasm reflects HIF-driven metabolism: a stabilized hypoxia program reprograms cells toward glycolysis and glycogen storage (the 'clear' look), and this metabolic state contributes to the platinum chemoresistance that makes OCCC hard to treat."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Clear-cell ovarian cancer is the gynecologic tumor most linked to hypercalcemia: it can drive paraneoplastic high calcium (via PTH-related peptide), so an ovarian mass with unexplained hypercalcemia points toward this histotype."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Clear-cell ovarian cancer often overproduces IL-6: this cytokine drives paraneoplastic fever, thrombocytosis and an inflammatory state, contributing to the thrombosis risk and the relative chemoresistance that set this subtype apart."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Clear-cell ovarian cancer grows from an endometriotic niche rich in fibroblasts: the cyst's reactive stroma and chronic inflammation foster ARID1A-mutant transformation, so the fibroblast-laden microenvironment is part of how this cancer begins."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Ovarian clear cell carcinoma is forged in iron: it arises from endometriosis, where repeated bleeding dumps iron into cysts, and the resulting oxidative stress damages DNA and drives the ARID1A-mutant cancer—linking menstrual iron to a tumor."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Ovarian clear cell carcinoma is intensely angiogenic via VEGF: HIF-driven VEGF feeds its blood supply, so anti-VEGF bevacizumab is among the few systemic options for a tumor notoriously resistant to standard chemotherapy."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Iron-laden macrophages haunt clear cell carcinoma's origin: in the endometriotic cysts it springs from, macrophages gorge on blood-derived iron and pump out inflammatory signals, building the oxidative, pro-tumor niche the cancer exploits."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Clear cell ovarian carcinoma behaves as if starved of oxygen: its glycogen-packed clear cells run a HIF-driven pseudohypoxic program even when oxygen is present, fueling growth and the chemoresistance that makes this subtype so hard to treat."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Clear cell ovarian carcinoma spreads across the peritoneum: like other ovarian cancers it studs the omentum and bowel surface, so abdominal disease and bowel involvement shape its presentation and the surgery aimed at removing all visible tumor."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells matter most in the immunogenic subset of clear cell ovarian carcinoma: some tumors carry mismatch-repair defects and neoantigens, and antigen-presenting dendritic cells help mount the response that checkpoint therapy can amplify."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Clear cell ovarian carcinoma mirrors kidney cancer: it shares the HIF-driven clear-cell biology of renal clear cell carcinoma, and as a pelvic mass it can obstruct the ureters and kidneys."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Clear cell ovarian carcinoma is hypervascular: HIF and VEGF drive endothelial cells to build a rich blood supply, like its renal counterpart, a feature anti-angiogenic therapy targets."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Clear cell ovarian carcinoma is born in endometriosis: it arises within fibrotic, blood-stained endometriotic cysts, whose chronic inflammation and scarring set the stage for malignant transformation."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy explains the 'clear' in clear cell: the cytoplasm is packed with glycogen that dissolves away in processing, leaving the empty, water-clear cells and bulging hobnail nuclei that name the tumor."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Clear cell carcinoma is the great clotter of ovarian cancers: it carries the highest rate of venous thromboembolism, activating platelets and the clotting cascade so strongly that a deep vein thrombosis can be the first sign of the tumor."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "When clear cell carcinoma spreads beyond the pelvis, the liver is a frequent target: hematogenous metastases lodge there, and liver involvement marks the advanced, chemoresistant disease that makes this subtype so hard to treat."
---

# Ovarian Clear Cell Carcinoma

## Overview

**Ovarian clear cell carcinoma (OCCC)** is a distinct histological and molecular subtype of epithelial ovarian cancer characterized by clear cytoplasm (glycogen-rich), hobnail cells, and a unique molecular profile dominated by **ARID1A** and **PIK3CA** mutations. OCCC is strongly associated with endometriosis (~40% of cases arise from endometriotic cysts) and is relatively resistant to standard platinum-based chemotherapy compared to high-grade serous ovarian carcinoma (HGSOC). It has a unique geographic distribution with significantly higher incidence in East Asian women, and remains one of the most therapeutically challenging gynecologic malignancies due to the absence of FDA-approved targeted therapies [^jones-2010-arid1a-occc].

**Epidemiology:**
- Frequency: ~10-12% of all epithelial ovarian cancers in Western populations; ~15-25% in Japan and East Asia
- Geographic/ethnic disparity: Japanese women: ~25% of ovarian cancers are clear cell; Caucasian women: ~5-8%; genetic predisposition and endometriosis prevalence differences explain part of this disparity
- Incidence: ~2,000-2,500 cases/year USA; ~5,000-6,000 in Japan
- Median age: ~50-55 years (younger than HGSOC, median ~60 years)
- Association with endometriosis: ~40% of OCCC arise within or adjacent to endometriotic cysts (endometriomas); endometriosis-associated OCCC: slightly better prognosis; lower CA-125 at presentation
- Germline predisposition: BRCA1/2 pathogenic variants confer HGSOC risk, not OCCC-specific risk; Lynch syndrome (MSH2) predisposes to endometrioid and OCCC subtypes

**Contrast with HGSOC:**

| Feature | OCCC | HGSOC |
|---|---|---|
| BRCA1/2 mutations | ~2-5% | ~15-20% |
| TP53 mutations | ~5-10% | ~95% |
| ARID1A mutations | ~50-55% | <5% |
| PIK3CA mutations | ~40-50% | ~3-5% |
| HER2 amplification | <5% | ~20% |
| Platinum sensitivity | ~20-30% | ~70-80% |
| Taxane sensitivity | Moderate | High |
| CA-125 at diagnosis | Often normal | Usually elevated |
| Stage at diagnosis | Often early (I-II) | Usually late (III-IV) |

## Structure

### Molecular landscape of OCCC

**Hallmark mutations:**

**ARID1A (~50-55%):** [^jones-2010-arid1a-occc]
Truncating mutations in exons 8-18; biallelic LOF in most cases; BAF250A protein lost by IHC; disrupts cBAF complex → EZH2/PRC2 gains access → H3K27me3 accumulation → silencing of differentiation and tumor suppressor genes; ARID1A-mutant tumors are EZH2-dependent; enriched in endometriosis-associated OCCC

**PIK3CA (~40-50%):**
Activating mutations: E542K, E545K (helical domain) and H1047R/L (kinase domain); → PI3K p110α activation → AKT/mTOR → proliferation and survival; co-mutation with ARID1A in ~25-30% of OCCC; PIK3CA mutation is the main kinase driver in OCCC (in contrast to HGSOC which lacks PIK3CA-activating mutations)

**KRAS (~15%):**
G12D/V activating mutations; KRAS + ARID1A co-mutation in ~8-10%; KRAS-mutant OCCC: MEK/ERK pathway driven; MEK inhibitors explored; KRAS mutations more common in endometriosis-associated OCCC

**PPP2R1A (~5-8%):**
Regulatory subunit of PP2A phosphatase; mutations → PP2A inactivation → AKT/mTOR persistence; less common than HGSOC (PPP2R1A ~15% in HG endometrioid)

**TP53 (~5-10%):**
Strikingly lower than HGSOC (~95%); TP53 wildtype is a key molecular feature of OCCC; helps distinguish from HGSOC in ambiguous cases

**TERT promoter mutations (~15%):**
Activating TERT promoter mutations; longer telomere maintenance; associated with more aggressive OCCC behavior

**MYC amplification (~10%):**
Associates with ARID1A-mutant OCCC; predicts worse outcomes; MYC overexpression through CTNNB1-independent mechanisms

### Histology

**Classic OCCC features:**
- **Clear cell pattern**: large polyhedral cells with abundant clear cytoplasm (glycogen by PAS staining); nuclear pleomorphism moderate; "fried egg" nuclei with prominent single nucleolus
- **Hobnail pattern**: cells with bulging nuclei protruding into glandular lumina; nuclei appear above the cytoplasm plane
- **Papillary/tubulocystic pattern**: papillae with hyalinized cores lined by hobnail cells; characteristic of OCCC
- Low mitotic rate; necrosis variable; psammoma bodies absent (unlike serous tumors)

**IHC for OCCC:**
- **Napsin A**: positive in ~80-90% of OCCC; most sensitive single marker; also positive in lung adenocarcinoma (helpful for primary site)
- **HNF1β**: positive in ~80-85% of OCCC; nuclear; also expressed in some endometrioid tumors
- **ARID1A (BAF250A)**: LOST in ~50% (protein loss = ARID1A mutation)
- **WT1**: negative in OCCC (contrast HGSOC: strongly WT1-positive)
- **ER/PR**: negative/focal (contrast endometrioid: often ER/PR-positive)
- **p53**: wild-type pattern (contrast HGSOC: aberrant p53 overexpression or complete null)
- **PAX8**: positive in most OCCC (Müllerian origin marker)

## Function

### Endometriosis → OCCC carcinogenesis

The transition from endometriosis to OCCC follows a defined molecular sequence:
1. **Ectopic endometrium** (endometriotic cyst/endometrioma): cyclic hemorrhage → iron deposition → oxidative stress → mutagenic environment
2. **Atypical endometriosis**: ARID1A mutation + PIK3CA mutation appear first; early clonal expansion without overt malignancy; transition lesion
3. **OCCC in situ** (clear cell glandular neoplasia): increasing nuclear atypia; stromal invasion begins
4. **Invasive OCCC**: full OCCC; additional mutations in TERT, MYC amplification, TP53 (rare late event)

**Iron-mediated mutagenesis:**
Endometrioma fluid contains high concentrations of free iron (from RBC hemoglobin degradation) → Fenton reaction → hydroxyl radical production → oxidative DNA damage → ARID1A and PIK3CA mutations preferentially acquired (mechanism of mutagenic specificity incompletely understood)

**HIF-1α in endometriosis:**
Ectopic endometrium is hypoxic → HIF-1α activation → VEGF, PDGF → angiogenesis and survival; endometriosis-derived OCCC expresses HIF-1α targets constitutively

## Pathology

### Staging and treatment

**Staging:** FIGO staging (same as all epithelial ovarian cancers)
- Stage I (~35-40% of OCCC at diagnosis — higher than HGSOC due to endometrioma detection): best prognosis; 5-year OS ~80-90%
- Stage II (~10-15%): 5-year OS ~60-70%
- Stage III (~35-40%): 5-year OS ~25-40%
- Stage IV (~10-15%): 5-year OS ~15-25%

**Surgery:**
Comprehensive surgical staging (TAH-BSO, omentectomy, pelvic/para-aortic lymphadenectomy, peritoneal biopsy) for apparent early-stage disease; cytoreductive surgery for advanced stage; complete cytoreduction (R0) critical for improved OS; OCCC tends to have fewer peritoneal implants than HGSOC → surgical debulking feasible in more cases

**First-line chemotherapy:**
- **Standard**: carboplatin + paclitaxel × 6 cycles (as per HGSOC)
- **Platinum resistance**: ~40-60% of OCCC are platinum-resistant or -refractory (vs ~20% in HGSOC); especially stage III-IV
- **Irinotecan + cisplatin** (irinotecan-cisplatin, IC): Japanese GCIG trial showed IC equivalent to CP in OCCC; IC preferred in Japan for OCCC; irinotecan may exploit OCCC-specific DNA repair defect
- **Bevacizumab**: benefit in OCCC less established than HGSOC; GOG-218 and ICON7 included OCCC but subgroup benefit unclear; used in some guidelines for stage III-IV

**PARP inhibitors:**
- BRCA1/2 mutation rare in OCCC (~2-5%); HRD (homologous recombination deficiency) low in OCCC (~15-20% vs ~50% in HGSOC)
- ARIEL3 (rucaparib maintenance): OCCC had lowest benefit among epithelial ovarian subtypes
- However, ARID1A LOF → partial HR defect → exploratory role for PARP inhibitors in ARID1A-mutant OCCC

**EZH2 inhibitors:** [^kim-2015-arid1a-ezh2]
- Tazemetostat: Phase 2 trials in ARID1A-mutant solid tumors including OCCC ongoing; ORR data pending (NCT04171700); rationale from ARID1A LOF → EZH2 dependency
- Combination tazemetostat + PARP inhibitor (olaparib): Phase 1/2 being explored

**mTOR inhibitors:**
- Rationale: PIK3CA mutations in ~40-50% → mTOR pathway hyperactivation
- Temsirolimus monotherapy Phase 2 (OCCC-enriched): ORR ~10-15%; DCR ~30-40%
- Combination mTOR + MEK (for KRAS-PIK3CA co-mutation): exploratory
- Alpelisib (PIK3CA inhibitor): breast cancer-approved; being explored in PIK3CA-mutant OCCC

**Immunotherapy:**
- OCCC TMB: moderate (~5-8 mut/Mb); PD-L1: expressed in ~30-40%
- KEYNOTE-100 (pembrolizumab in recurrent OC): OCCC subgroup ORR ~15-17% (higher than HGSOC ~8%)
- ARID1A-mutant OCCC → PD-L1 upregulated → higher ICB response: preclinical rationale supported
- Pembrolizumab + bevacizumab: Phase 2 showing activity in recurrent OCCC; ORR ~25-30% in PD-L1+ cases
- Durvalumab + olaparib combination: GOG 3032 (MEDUSA) includes OCCC cohort

**CDK4/6 inhibitors:**
- OCCC co-expresses CDK4/6 via CCND1 upregulation; palbociclib Phase 2 in OCCC with CDK pathway activation

**Prognosis by stage and molecular subtype:**
- Early-stage (I-II): 5-year OS ~70-85%; early detection via endometrioma surveillance recommended
- Advanced (III-IV): 5-year OS ~20-35%; significantly worse than HGSOC at same stage due to platinum resistance
- ARID1A-mutant vs WT: ARID1A mutation alone not independently prognostic; combined with PIK3CA → worse prognosis
- Endometriosis-associated OCCC: slightly better prognosis than de novo OCCC (detected at earlier stage)
- Recurrent disease: median PFS 2nd line ~4-6 months; few effective options; clinical trial enrollment strongly recommended

## Connections

- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A (BAF250A) is mutated in ~50% of OCCC; biallelic ARID1A LOF → cBAF disruption; ARID1A IHC (BAF250A, clone PSG3) protein loss is a surrogate diagnostic marker in OCCC; ARID1A + PIK3CA co-mutation in ~25-30% OCCC defines the highest-risk molecular subgroup.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — ARID1A LOF disrupts cBAF → EZH2/PRC2 accesses ARID1A-target loci → H3K27me3 accumulation; OCCC with ARID1A LOF shows EZH2 dependency in preclinical models; tazemetostat under investigation in ARID1A-mutant OCCC; EZH2 + PARP inhibitor combination explored.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — ARID1A + PIK3CA co-mutation defines ~25-30% of ovarian clear cell carcinomas; PIK3CA → PI3K/AKT/mTOR → OCCC proliferation; ARID1A LOF + PIK3CA creates synthetic vulnerability to dual PI3K/mTOR inhibition; temsirolimus active in PIK3CA-mutant OCCC Phase 2.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — ARID1A LOF in OCCC → PD-L1 upregulation via MLH1 suppression and IFN-γ signaling pathway enhancement; OCCC has higher PD-L1 expression than high-grade serous ovarian cancer; pembrolizumab + bevacizumab shows activity in PD-L1+ OCCC; durvalumab combination trials ongoing.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — PIK3CA mutations (~40-50%) in OCCC → PI3K/AKT → mTOR activation; temsirolimus Phase 2 in OCCC: ORR ~10-15%; alpelisib (PIK3CA inhibitor) explored in PIK3CA-mutant OCCC; PI3K/mTOR dual inhibitors studied; ARID1A LOF + PIK3CA → synthetic vulnerability to PI3K/mTOR inhibition.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — KRAS G12D/V mutations in ~15% of OCCC, enriched in endometriosis-associated OCCC; KRAS + ARID1A co-mutation in ~8-10%; MEK pathway activated in KRAS-mutant OCCC → MEK inhibitors explored; KRAS mutation is more prevalent in OCCC than HGSOC or endometrioid ovarian cancer.
- `connects-to` → **[Ovarian Cancer](../ovarian-cancer/README.md)** — OCCC is distinct from HGSOC: OCCC (ARID1A/PIK3CA-driven, platinum-resistant, stage I-II at ~35-40%) vs HGSOC (TP53-universal, platinum-sensitive, stage III-IV at ~75%); OCCC lacks HRD enrichment; 5-year OS in advanced OCCC is worse than HGSOC despite identical chemotherapy.
- `connects-to` → **[Endometrial Cancer](../endometrial-cancer/README.md)** — Ovarian clear cell carcinoma and endometrioid endometrial cancer are both endometriosis/endometrium-derived tumors driven by ARID1A and PIK3CA; clear-cell and endometrioid histologies recur across ovary and uterus, and both can arise in Lynch syndrome — unlike serous cancers.
- `connects-to` → **[Renal Cell Carcinoma](../renal-cell-carcinoma/README.md)** — Ovarian clear cell carcinoma and clear-cell renal cell carcinoma are unrelated organs sharing a look and biology: both have glycogen-rich clear cytoplasm, both upregulate HIF/VEGF, and OCCC borrows RCC anti-angiogenics like sunitinib for this platinum-resistant tumor.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Ovarian clear cell carcinoma is more immunogenic than high-grade serous cancer: ARID1A loss raises neoantigens and PD-L1, so it draws cytotoxic CD8+ T cells and responds better to PD-1 blockade — pembrolizumab + bevacizumab is studied in PD-L1+ OCCC.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Ovarian clear cell carcinoma has the highest venous thromboembolism rate of any ovarian cancer—up to a quarter of patients: the tumor is strongly prothrombotic (tissue factor, IL-6), so DVT and pulmonary embolism are watched and often prophylaxed throughout treatment.
- `connects-to` → **[Lynch Syndrome](../lynch-syndrome/README.md)** — Clear-cell and endometrioid ovarian cancers are the histologies linked to Lynch syndrome: mismatch-repair deficiency underlies a share of OCCC, so MMR/MSI testing both flags a germline syndrome and identifies tumors that may respond to checkpoint blockade.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Ovarian clear cell carcinoma is the ovarian cancer most tied to endometriosis: ectopic endometrial tissue, under oxidative iron-rich stress, acquires ARID1A and PIK3CA mutations and transforms—making endometriosis a recognized precursor in the reproductive tract.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — Ovarian clear-cell carcinoma and gastric cancer share ARID1A loss: this SWI/SNF chromatin-remodeler tumor suppressor is among the most mutated genes in both, showing how chromatin disruption—not classic oncogenes—drives diverse epithelial cancers.
- `connects-to` → **[Cholangiocarcinoma](../cholangiocarcinoma/README.md)** — Ovarian clear-cell carcinoma and cholangiocarcinoma converge on chromatin-remodeling defects: both frequently lose ARID1A, and both are relatively chemoresistant epithelial cancers—making epigenetic vulnerabilities (EZH2 inhibition) a shared therapeutic avenue.
- `connects-to` → **[Hereditary Breast and Ovarian Cancer](../hereditary-breast-ovarian-cancer/README.md)** — Ovarian clear-cell carcinoma differs from the BRCA-driven cancers of HBOC: unlike high-grade serous ovarian cancer, clear-cell is rarely BRCA/HRD-related (it's ARID1A/PIK3CA-driven), so it responds poorly to platinum and PARP inhibitors—a key treatment distinction.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — OCCC is driven by PI3K-pathway and chromatin gene mutations: ARID1A loss with PIK3CA or PTEN alterations activates PI3K/AKT/mTOR growth signaling, distinguishing clear cell carcinoma's biology—and rationale for mTOR/PI3K-targeted trials—from high-grade serous cancer.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — OCCC tends to be immunologically distinct and PD-L1-expressing: among ovarian cancers, clear cell carcinoma more often shows mismatch-repair/ARID1A features and immune infiltration, so NK and T-cell-engaging immunotherapy is of interest in this platinum-resistant subtype.
- `connects-to` → **[VHL Disease](../vhl-disease/README.md)** — OCCC shares clear-cell morphology and biology with renal clear cell carcinoma: glycogen-rich clear cytoplasm and HIF/VEGF-driven angiogenesis link it to VHL-associated kidney cancer, so anti-angiogenic agents are explored across these histologically similar tumors.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — Ovarian clear cell carcinoma is characteristically p53-wildtype: unlike high-grade serous ovarian cancer, which is defined by TP53 mutation, OCCC is driven instead by ARID1A and PIK3CA—so p53 status helps distinguish these biologically distinct ovarian cancers.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Ovarian clear cell carcinoma resists platinum chemo but its ARID1A loss links to immunotherapy: ARID1A-mutant or mismatch-repair-deficient tumors can respond to checkpoint blockade, offering an option in this otherwise chemoresistant subtype.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — OCCC's clear cytoplasm reflects HIF-driven metabolism: a stabilized hypoxia program reprograms cells toward glycolysis and glycogen storage (the 'clear' look), and this metabolic state contributes to the platinum chemoresistance that makes OCCC hard to treat.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Clear-cell ovarian cancer is the gynecologic tumor most linked to hypercalcemia: it can drive paraneoplastic high calcium (via PTH-related peptide), so an ovarian mass with unexplained hypercalcemia points toward this histotype.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Clear-cell ovarian cancer often overproduces IL-6: this cytokine drives paraneoplastic fever, thrombocytosis and an inflammatory state, contributing to the thrombosis risk and the relative chemoresistance that set this subtype apart.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Clear-cell ovarian cancer grows from an endometriotic niche rich in fibroblasts: the cyst's reactive stroma and chronic inflammation foster ARID1A-mutant transformation, so the fibroblast-laden microenvironment is part of how this cancer begins.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Ovarian clear cell carcinoma is forged in iron: it arises from endometriosis, where repeated bleeding dumps iron into cysts, and the resulting oxidative stress damages DNA and drives the ARID1A-mutant cancer—linking menstrual iron to a tumor.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Ovarian clear cell carcinoma is intensely angiogenic via VEGF: HIF-driven VEGF feeds its blood supply, so anti-VEGF bevacizumab is among the few systemic options for a tumor notoriously resistant to standard chemotherapy.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Iron-laden macrophages haunt clear cell carcinoma's origin: in the endometriotic cysts it springs from, macrophages gorge on blood-derived iron and pump out inflammatory signals, building the oxidative, pro-tumor niche the cancer exploits.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Clear cell ovarian carcinoma behaves as if starved of oxygen: its glycogen-packed clear cells run a HIF-driven pseudohypoxic program even when oxygen is present, fueling growth and the chemoresistance that makes this subtype so hard to treat.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Clear cell ovarian carcinoma spreads across the peritoneum: like other ovarian cancers it studs the omentum and bowel surface, so abdominal disease and bowel involvement shape its presentation and the surgery aimed at removing all visible tumor.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells matter most in the immunogenic subset of clear cell ovarian carcinoma: some tumors carry mismatch-repair defects and neoantigens, and antigen-presenting dendritic cells help mount the response that checkpoint therapy can amplify.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Clear cell ovarian carcinoma mirrors kidney cancer: it shares the HIF-driven clear-cell biology of renal clear cell carcinoma, and as a pelvic mass it can obstruct the ureters and kidneys.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Clear cell ovarian carcinoma is hypervascular: HIF and VEGF drive endothelial cells to build a rich blood supply, like its renal counterpart, a feature anti-angiogenic therapy targets.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Clear cell ovarian carcinoma is born in endometriosis: it arises within fibrotic, blood-stained endometriotic cysts, whose chronic inflammation and scarring set the stage for malignant transformation.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy explains the 'clear' in clear cell: the cytoplasm is packed with glycogen that dissolves away in processing, leaving the empty, water-clear cells and bulging hobnail nuclei that name the tumor.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Clear cell carcinoma is the great clotter of ovarian cancers: it carries the highest rate of venous thromboembolism, activating platelets and the clotting cascade so strongly that a deep vein thrombosis can be the first sign of the tumor.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — When clear cell carcinoma spreads beyond the pelvis, the liver is a frequent target: hematogenous metastases lodge there, and liver involvement marks the advanced, chemoresistant disease that makes this subtype so hard to treat.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^jones-2010-arid1a-occc]: Jones S, Wang TL, Shih IeM, et al. Frequent mutations of chromatin remodeling gene ARID1A in ovarian clear cell carcinoma. *Science.* 2010;330(6001):228-231. [doi:10.1126/science.1196333](https://doi.org/10.1126/science.1196333) · [PubMed 20826764](https://pubmed.ncbi.nlm.nih.gov/20826764/)
[^kim-2015-arid1a-ezh2]: Kim KH, Kim W, Howard TP, et al. SWI/SNF-mutant cancers depend on catalytic and non-catalytic activity of EZH2. *Nat Med.* 2015;21(12):1491-1496. [doi:10.1038/nm.3968](https://doi.org/10.1038/nm.3968) · [PubMed 26552009](https://pubmed.ncbi.nlm.nih.gov/26552009/)

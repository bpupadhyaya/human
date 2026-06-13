---
schema: human-scale-entry/v1
id: burkitt-lymphoma
name: Burkitt Lymphoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Burkitt lymphoma is a highly aggressive GC B-cell lymphoma defined by MYC translocation and near-100% Ki-67; endemic (EBV+), sporadic, immunodeficiency-associated subtypes; DA-EPOCH-R or R-CODOX-M/IVAC for adults; rituximab+LMB for pediatric; TLS prophylaxis essential."
aliases: ["Burkitt lymphoma", "BL", "Burkitt's lymphoma", "endemic Burkitt", "sporadic Burkitt", "HIV Burkitt lymphoma", "Burkitt leukemia", "L3 ALL"]
sources:
  - id: roschewski-2020-da-epoch-r-bl
    type: peer-reviewed
    cite: "Roschewski M, Dunleavy K, Abramson JS, et al. Multicenter study of risk-adapted therapy with dose-adjusted EPOCH-R in adults with untreated Burkitt lymphoma. J Clin Oncol. 2020;38(22):2519-2529."
    doi: "10.1200/JCO.19.03259"
    pmid: "32530765"
    url: "https://doi.org/10.1200/JCO.19.03259"
  - id: minard-colin-2017-inter-b-nhl-ritux
    type: peer-reviewed
    cite: "Minard-Colin V, Auperin A, Pillon M, et al. Rituximab for children and adolescents with high-risk B-cell non-Hodgkin lymphoma: results of the randomized Inter-B-NHL Ritux 2010 trial. J Clin Oncol. 2022;40(22):2458-2471."
    doi: "10.1200/JCO.21.01940"
    pmid: "35436151"
    url: "https://doi.org/10.1200/JCO.21.01940"
cross_links:
  - target: 01-human/03-molecular/npm1
    relation: connects-to
    note: "NPM1 is a nucleolar ribosome biogenesis factor essential in Ki-67~100% BL cells; NPM1 sequesters ARF → attenuates the MYC → ARF → p53 checkpoint; NPM1 overexpression in high-grade B-cell lymphomas; NPM1 phosphorylation by CDK2 regulates centrosome duplication in BL."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "MYC translocation [t(8;14) ~80%, t(2;8) ~15%, t(8;22) ~5%] is the defining alteration of Burkitt lymphoma; MYC juxtaposed to Ig loci → constitutive transcription; MYC drives near-100% Ki-67; BET bromodomain inhibitors suppress MYC in BL preclinically."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "BL cells silence ARF (CDKN2A deletion ~50%) to evade MYC → ARF → p53 checkpoint; TP53 mutations in ~30% BL at relapse; p53 pathway is intact in most primary BL; MDM2 inhibitors (idasanutlin) + DA-EPOCH-R explored in Phase 1 for relapsed/refractory BL."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "BL tumor microenvironment is immune-poor; PD-L1 expression is variable; EBV+ endemic BL has more immune infiltrate than sporadic BL; PD-1 blockade combined with rituximab-based therapy in early trials for relapsed/refractory high-grade B-cell lymphoma."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "BL arises from germinal center B cells with MYC translocation to Ig loci (IGH/IGK/IGL) during VDJ recombination or class-switch recombination; CD19+/CD20+/CD10+/BCL6+/BCL2- immunophenotype reflects GC B-cell origin; MYC drives near-100% Ki-67 in these rapidly cycling B cells."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "BL originates in germinal center B cells; MYC translocation arises from AID-mediated DSBs at Ig loci during class-switch recombination; CD10+/BCL6+ confirms GC origin; EBV+ endemic BL expresses BCL6 and EBNA-1 in Latency I, exploiting GC biology for viral persistence."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "CD20 (MS4A1) is expressed on all BL cells; rituximab (anti-CD20 mAb) is standard in adult DA-EPOCH-R and pediatric LMB regimens; Inter-B-NHL Ritux 2010: rituximab addition → 3-year EFS 93.9% vs 79.8% (HR 0.33, p<0.001) in high-risk pediatric BL; obinutuzumab explored in R/R BL."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "Epstein-Barr virus is found in nearly all endemic (African) Burkitt lymphoma and a minority of sporadic cases: the virus persists in germinal-center B cells in Latency I, and its EBNA/miRNA program helps the MYC-translocated cell evade apoptosis and immune clearance."
  - target: 02-pathogen/04-parasites/plasmodium-falciparum
    relation: connects-to
    note: "Holoendemic Plasmodium falciparum malaria is the geographic cofactor for endemic Burkitt lymphoma: chronic malaria expands germinal-center B cells and induces AID, raising the chance of the MYC-Ig translocation, while malaria-driven immune dysregulation reactivates EBV."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Burkitt lymphoma must be separated from DLBCL and double-hit large-cell lymphoma: Burkitt has a sole MYC translocation, ~100% Ki-67, and is BCL-2-negative, so FISH for MYC/BCL-2/BCL-6 is essential — a Burkitt diagnosis mandates intensive regimens (DA-EPOCH-R), not R-CHOP."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "Burkitt lymphoma is an AIDS-defining cancer: HIV-driven immunosuppression and chronic B-cell activation raise Burkitt risk even at preserved CD4 counts—so a fast-growing lymphoma in an HIV-positive patient is Burkitt until proven otherwise."
  - target: 01-human/07-system/follicular-lymphoma
    relation: connects-to
    note: "Burkitt and follicular lymphoma are both germinal-center B-cell tumors but opposite in tempo: Burkitt is MYC-driven, near-100% Ki67, doubles in a day and is curable with intensive chemo, while BCL2-driven follicular lymphoma is indolent, incurable, and waxes over years."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "The 'starry sky' appearance pathognomonic of Burkitt lymphoma comes from tingible-body macrophages: scattered pale macrophages engulfing apoptotic debris from the explosively proliferating MYC-driven B cells stand out against the dark sheet of tumor."
  - target: 01-human/07-system/malaria
    relation: connects-to
    note: "Endemic Burkitt lymphoma is malaria-driven: chronic Plasmodium falciparum infection drives intense B-cell proliferation and weakens control of co-infecting Epstein-Barr virus, together promoting the MYC translocation that causes the jaw and abdominal tumors of African children."
  - target: 01-human/07-system/hodgkin-lymphoma
    relation: connects-to
    note: "Burkitt and Hodgkin lymphoma are both EBV-associated but biologically opposite: Burkitt is a fast MYC-driven mature B-cell tumor curable with intensive chemo, while Hodgkin is a CD30+ Reed-Sternberg-cell lymphoma with a rich reactive infiltrate, treated differently with ABVD."
  - target: 01-human/07-system/mantle-cell-lymphoma
    relation: connects-to
    note: "Burkitt and mantle cell lymphoma are aggressive B-cell lymphomas defined by single translocations: Burkitt's t(8;14) drives MYC, mantle cell's t(11;14) drives cyclin D1—but Burkitt is curable while mantle cell is aggressive yet incurable, a key prognostic split."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Burkitt lymphoma is MYC-driven, not BCL2-driven—a key contrast: classic Burkitt carries the MYC translocation and is BCL2-negative, so a tumor with both MYC and BCL2 rearrangements is instead a more aggressive double-hit high-grade lymphoma, not true Burkitt."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Burkitt lymphoma is a germinal-center B cell frozen short of plasma-cell fate: the MYC-driven clone proliferates explosively (near-100% Ki-67) instead of maturing into antibody-secreting plasma cells—so its hallmark is runaway growth, the fastest-doubling human tumor."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Burkitt lymphoma exposes the immune system's role in cancer control: it surges in immunodeficiency (HIV) and where chronic malaria and EBV exhaust immune surveillance—so endemic Burkitt is partly a cancer of weakened immune defense against EBV-driven B cells."
---

# Burkitt Lymphoma

## Overview

**Burkitt lymphoma (BL)** is the most rapidly proliferating human malignancy, defined by a **MYC translocation** juxtaposing MYC (8q24) to an immunoglobulin locus [t(8;14) ~80%, t(2;8) ~15%, t(8;22) ~5%], germinal center (GC) B-cell immunophenotype (CD19+, CD20+, CD10+, BCL6+, TdT–, BCL2–), and near-100% Ki-67 proliferative index. Three distinct subtypes reflect different epidemiological and etiological contexts: **endemic BL** (sub-Saharan Africa, Papua New Guinea; EBV+ in ~95-100%; presents as jaw/facial mass in children aged 4-7); **sporadic BL** (Western countries; EBV+ in ~15-30%; ileocecal/abdominal primary in children and young adults); **immunodeficiency-associated BL** (HIV+ individuals; EBV+ in ~20-40%; often abdominal). The extreme proliferative rate creates the hallmark "**starry sky**" pattern on histology — pale tingible-body macrophages phagocytizing apoptotic tumor cells against a dark background of cycling lymphoma cells. Modern treatment of **adult BL** with **dose-adjusted EPOCH-R** (DA-EPOCH-R) achieves complete remission in ~87-90% of patients with manageable toxicity [^roschewski-2020-da-epoch-r-bl]; pediatric BL is treated with intensive **rituximab + LMB chemotherapy** (Inter-B-NHL Ritux 2010: rituximab addition improved 3-year EFS from 79.8% to 93.9%, HR 0.33, p<0.001 in high-risk) [^minard-colin-2017-inter-b-nhl-ritux].

**Epidemiology:**
- ~1,200-1,500 cases/year USA (all ages); endemic BL ~3-5x more common globally
- Pediatric B-NHL: ~40% of cases are BL; most common pediatric lymphoma in sub-Saharan Africa
- Median age: pediatric for endemic (peak age 4-7); bimodal in sporadic (child + young adult)
- Male predominance 3-4:1 in endemic; 2-3:1 in sporadic
- HIV+ patients: BL is an AIDS-defining malignancy; CD4 count often >100-200 cells/μL at BL diagnosis (unlike primary CNS lymphoma which presents at lower CD4)

## Structure

### Molecular landscape

**MYC translocation — the defining event:**
All BL carry a MYC translocation to an Ig locus:
- **t(8;14)(q24;q32) (~80%):** MYC (8q24) → IGH (14q32) — most common; MYC juxtaposed to IGH E μ/α enhancer → constitutive MYC expression in B cells; in endemic BL, breakpoint is at the MYC promoter/5' region; in sporadic BL, breakpoint is within MYC exon 1 or intron 1
- **t(2;8)(p12;q24) (~15%):** IGK → MYC; less common
- **t(8;22)(q24;q11) (~5%):** MYC ← IGL; least common

**MYC drives Burkitt biology:**
- Near-100% Ki-67 (not just high, virtually all cells are cycling at any timeframe)
- Ribosome biogenesis activation → nucleolar prominence (the histological correlate)
- Aerobic glycolysis (Warburg effect) → rapid lactate production → metabolic stress
- TERT expression → telomere maintenance
- MYC-driven oncogenic stress → p53 activation → but BL escapes via ARF (CDKN2A) deletion or MDM2 overexpression; TP53 wild-type in ~70% primary BL (p53 function partially suppressed by other mechanisms)

**Additional molecular features:**
- **ID3/TCF3 (E2A) mutations:** ~70% BL; ID3 loss-of-function → TCF3 activation → B-cell receptor signaling → pro-survival PI3K; TCF3 mutations less common; ID3 is the canonical BL second hit after MYC translocation
- **CCND3 mutations:** ~38% BL; cyclin D3 T283A → CDK4/6 activation → G1/S bypass → accelerates proliferation
- **TP53 mutations:** ~30-40% at relapse; ~15-25% primary BL; MDM2 amplification ~3%; CDKN2A deletion ~50% (ARF + CDKN2A/p16 co-deleted)
- **RHOA mutations:** ~5%; small GTPase
- **EBV (EBNA-1, EBV-encoded miRNAs):** Endemic BL: EBV-driven BCL6 expression, immune evasion (BHRF1/BART miRNAs); LMP1/LMP2A not expressed in endemic BL (unlike EBV+ DLBCL NOS); EBV establishes Latency I in BL

**Not present in BL:**
- BCL2 translocation (distinguishes BL from DLBCL/follicular lymphoma)
- BCL2 protein overexpression (important diagnostic distinction from double-hit lymphoma)
- BCL6 translocation (BCL6 expressed but not translocated)

### Histology and immunophenotype

**"Starry sky" pattern:** Sheets of monomorphic intermediate-sized lymphoid blasts with scant basophilic cytoplasm, squared-off nuclei, multiple small nucleoli, numerous apoptotic figures; pale tingible-body macrophages (phagocytizing apoptotic debris) scattered → "stars" in a dark "sky" of tumor cells; highly characteristic but not specific to BL (seen in any high-grade lymphoma with rapid turnover).

**Immunophenotype:**
- B-cell markers: CD19+, CD20+, CD22+, CD79a+, CD38+
- GC markers: CD10+, BCL6+
- CD77+ (hallmark of GC centroblasts)
- Ki-67 ~100% (virtually pathognomonic)
- **BCL2 negative** (critical diagnostic distinction from DLBCL)
- TdT negative (distinguishes BL from acute lymphoblastic leukemia, though BL can present as L3-ALL)
- CD5–, CD23–, Cyclin D1–

## Function

### Pathophysiology of extreme proliferation

**MYC → ribosome biogenesis → anabolic metabolism:**
MYC activates all ~350 ribosomal protein genes, RNA Pol I (rDNA transcription), and RNA Pol III (5S rRNA, tRNA) → BL cells produce ribosomes at maximal capacity → enables protein synthesis to support doubling every ~24-48 hours; this extreme anabolic state creates vulnerability:
- **Nucleolar stress (RNA Pol I inhibitors: CX-5461):** Inhibit rDNA transcription → nucleolar disruption → MDM2 trapped in nucleolus → p53 released → apoptosis; promising in BL and other MYC-driven lymphomas
- **NPM1 dependency:** NPM1 is essential for pre-rRNA processing and export; in Ki-67~100% BL cells, NPM1 is a critical rRNA chaperone; BL cannot tolerate NPM1 loss

**MYC → ARF → p53 evasion:**
Normal cells: MYC overactivation → ARF (p14ARF from CDKN2A alt. reading frame) upregulation → MDM2 binding → MDM2 sequestration → p53 stabilization → apoptosis. BL escapes via:
1. CDKN2A deletion (ARF + p16 co-deleted, ~50% BL)
2. MDM2 amplification (~3%)
3. NPM1 overexpression → ARF nucleolar sequestration → MDM2 not inhibited
4. TP53 mutation (~25-30% primary, ~30-40% relapsed)

**Tumor lysis syndrome (TLS):**
BL is the highest TLS-risk malignancy; massive tumor cell death on first contact with chemotherapy → uric acid, potassium, phosphate, LDH release → hyperuricemia → AKI, hypocalcemia, cardiac arrhythmia; TLS prophylaxis is MANDATORY: rasburicase (urate oxidase, preferred if high LDH/bulky disease), aggressive IV hydration (200-250 mL/hour, urine output ≥100 mL/hour), continuous cardiac monitoring, allopurinol for low-risk; delay start of chemotherapy until adequate TLS prophylaxis established.

## Pathology

### Staging (Murphy/St. Jude staging for pediatric)

| Stage | Definition |
|-------|-----------|
| I | Single nodal or extranodal tumor; not mediastinal or abdominal |
| II | Multiple nodal/extranodal sites same side of diaphragm; resectable abdominal |
| III | Extensive abdominal, mediastinal, or ≥2 sites each side of diaphragm; unresectable abdominal |
| IV | CNS or BM involvement |

**Adult BL:** Lugano/Ann Arbor staging (I-IV); CNS involvement defined as CSF cytology +, intracranial disease, or cranial nerve palsies; BM involvement >25% blasts = L3-ALL (BL-leukemia); bulky disease (>10 cm), elevated LDH, and CNS/BM involvement = "high-risk" features.

### Treatment

**Risk-adapted DA-EPOCH-R (adults, low-risk/high-risk):**
EPOCH = etoposide + prednisone + vincristine + cyclophosphamide + doxorubicin (96-hour continuous infusion); DA (dose-adjusted): escalate or reduce doses each cycle based on nadir ANC; + R = rituximab Day 1 of each cycle; CNS prophylaxis: intrathecal MTX+cytarabine during each cycle (7 doses for low-risk, 8 for high-risk) OR high-dose systemic MTX (alternative); NCI multicenter study [^roschewski-2020-da-epoch-r-bl]: low-risk (LDH ≤normal, single extranodal mass, Ann Arbor I/II): DA-EPOCH-R × 3 cycles → 4-year EFS 100%, PFS 100%; high-risk (all other): DA-EPOCH-R × 6 cycles → 4-year EFS 87%, PFS 82%; peripheral neuropathy (vincristine), hematologic toxicity manageable.

**R-CODOX-M/IVAC (Magrath regimen):**
Alternate cycles: CODOX-M (cyclophosphamide/vincristine/doxorubicin/high-dose MTX) and IVAC (ifosfamide/etoposide/high-dose AraC) × 3-4 cycles total (1-2 of each); rituximab added; low-risk BL: R-CODOX-M × 3 cycles; high-risk: R-CODOX-M/IVAC alternating × 4 cycles; reported EFS ~87-92% in low/intermediate-risk; more toxicity (severe mucositis, cytopenias, CNS toxicity from intrathecal chemo) than DA-EPOCH-R; choice between DA-EPOCH-R and R-CODOX-M/IVAC is center-dependent.

**Pediatric LMB chemotherapy (rituximab + LMB):**
FAB/LMB protocols stratified by risk group (A/B/C):
- Group A (Stage I/II, complete resection): COPAM (cyclophosphamide, vincristine, prednisone, doxorubicin, MTX) × 2 cycles; 5-year EFS >98%
- Group B (non-resected Stage II-III, no CNS/BM): COP induction → COPADM × 2 → CYVE consolidation × 2 → maintenance; 5-year EFS ~85-90%
- Group C (CNS+/BM+): High-intensity with HD-MTX and HD-AraC
- Inter-B-NHL Ritux 2010 (rituximab addition to Group B/C): 3-year EFS 93.9% vs 79.8% (HR 0.33, p<0.001 in high-risk group B/C) [^minard-colin-2017-inter-b-nhl-ritux]; rituximab standard of care for pediatric BL >1 year of age.

**HIV-associated BL:**
Treat as non-HIV BL if CD4 >100 and performance status allows; rituximab + DA-EPOCH: similar outcomes to HIV-negative with modern ART; maintain ART throughout therapy; avoid prophylactic dose-reductions; PCP/toxoplasma prophylaxis; G-CSF support.

### Relapsed/refractory Burkitt lymphoma

**Prognosis:** Extremely poor; most relapse within 12 months of initial CR; survival <20% at 2 years.

**Salvage options:**
- R-ICE (rituximab+ifosfamide+carboplatin+etoposide): ORR ~40-50%
- R-DHAP (rituximab+dexamethasone+high-dose AraC+cisplatin): ORR ~30-40%
- DA-EPOCH-R → allo-SCT if CR2 achievable: only potentially curative approach
- Obinutuzumab (Type II anti-CD20): substituted for rituximab; limited additional benefit
- CAR-T cell therapy: tisagenlecleucel/axicabtagene-ciloleucel: Phase 2 data in R/R HGBL (including BL) — ORR ~40-50%; BL included in large cell lymphoma approvals; limited data specifically in BL
- Olaparib: BRCA-pathway downregulation by ARF loss → potential HR defect → PARP inhibitor sensitivity (preclinical data; no clinical approval)
- Obinutuzumab + venetoclax: BCL2-negative BL → venetoclax less rational; BCL2-low BL may not respond; not standard

### BL vs Double-Hit Lymphoma (DHL)

Critical diagnostic distinction:
| Feature | Burkitt Lymphoma | Double-Hit LBCL |
|---------|-----------------|-----------------|
| Ki-67 | ~100% | 40-90% |
| BCL2 IHC | Negative | Positive (usually) |
| BCL2 translocation | Absent | Present (usually) |
| MYC | t(8;IG) | MYC translocation ± any partner |
| Morphology | Classic intermediate/monomorphic | Often DLBCL-like |
| Prognosis | Curable with intensive regimens | Poor; DA-EPOCH-R or R-CHOP+venetoclax |

FISH for MYC, BCL2, and BCL6 is essential; if BCL2 FISH negative and Ki-67 ~100% → BL (treat with BL regimen, NOT CHOP); DHL → DA-EPOCH-R ± venetoclax or clinical trial.

## Connections

- `connects-to` → **[NPM1](../../03-molecular/npm1/README.md)** — NPM1 is a nucleolar ribosome biogenesis factor essential in Ki-67~100% BL cells; NPM1 sequesters ARF → attenuates the MYC → ARF → p53 checkpoint; NPM1 overexpression in high-grade B-cell lymphomas; NPM1 phosphorylation by CDK2 regulates centrosome duplication in BL.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — MYC translocation [t(8;14) ~80%, t(2;8) ~15%, t(8;22) ~5%] is the defining alteration of Burkitt lymphoma; MYC juxtaposed to Ig loci → constitutive transcription; MYC drives near-100% Ki-67; BET bromodomain inhibitors suppress MYC in BL preclinically.
- `connects-to` → **[P53](../../03-molecular/p53/README.md)** — BL cells silence ARF (CDKN2A deletion ~50%) to evade MYC → ARF → p53 checkpoint; TP53 mutations in ~30% BL at relapse; p53 pathway is intact in most primary BL; MDM2 inhibitors (idasanutlin) + DA-EPOCH-R explored in Phase 1 for relapsed/refractory BL.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — BL tumor microenvironment is immune-poor; PD-L1 expression is variable; EBV+ endemic BL has more immune infiltrate than sporadic BL; PD-1 blockade combined with rituximab-based therapy in early trials for relapsed/refractory high-grade B-cell lymphoma.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — BL arises from germinal center B cells with MYC translocation to Ig loci (IGH/IGK/IGL) during VDJ recombination or class-switch recombination; CD19+/CD20+/CD10+/BCL6+/BCL2- immunophenotype reflects GC B-cell origin; MYC drives near-100% Ki-67 in these rapidly cycling B cells.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — BL originates in germinal center B cells; MYC translocation arises from AID-mediated DSBs at Ig loci during class-switch recombination; CD10+/BCL6+ confirms GC origin; EBV+ endemic BL expresses BCL6 and EBNA-1 in Latency I, exploiting GC biology for viral persistence.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — CD20 (MS4A1) is expressed on all BL cells; rituximab (anti-CD20 mAb) is standard in adult DA-EPOCH-R and pediatric LMB regimens; Inter-B-NHL Ritux 2010: rituximab addition → 3-year EFS 93.9% vs 79.8% (HR 0.33, p<0.001) in high-risk pediatric BL; obinutuzumab explored in R/R BL.
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — Epstein-Barr virus is found in nearly all endemic (African) Burkitt lymphoma and a minority of sporadic cases: the virus persists in germinal-center B cells in Latency I, and its EBNA/miRNA program helps the MYC-translocated cell evade apoptosis and immune clearance.
- `connects-to` → **[Plasmodium falciparum](../../../02-pathogen/04-parasites/plasmodium-falciparum/README.md)** — Holoendemic Plasmodium falciparum malaria is the geographic cofactor for endemic Burkitt lymphoma: chronic malaria expands germinal-center B cells and induces AID, raising the chance of the MYC-Ig translocation, while malaria-driven immune dysregulation reactivates EBV.
- `connects-to` → **[Diffuse Large B-Cell Lymphoma](../dlbcl/README.md)** — Burkitt lymphoma must be separated from DLBCL and double-hit large-cell lymphoma: Burkitt has a sole MYC translocation, ~100% Ki-67, and is BCL-2-negative, so FISH for MYC/BCL-2/BCL-6 is essential — a Burkitt diagnosis mandates intensive regimens (DA-EPOCH-R), not R-CHOP.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — Burkitt lymphoma is an AIDS-defining cancer: HIV-driven immunosuppression and chronic B-cell activation raise Burkitt risk even at preserved CD4 counts—so a fast-growing lymphoma in an HIV-positive patient is Burkitt until proven otherwise.
- `connects-to` → **[Follicular Lymphoma](../follicular-lymphoma/README.md)** — Burkitt and follicular lymphoma are both germinal-center B-cell tumors but opposite in tempo: Burkitt is MYC-driven, near-100% Ki67, doubles in a day and is curable with intensive chemo, while BCL2-driven follicular lymphoma is indolent, incurable, and waxes over years.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — The 'starry sky' appearance pathognomonic of Burkitt lymphoma comes from tingible-body macrophages: scattered pale macrophages engulfing apoptotic debris from the explosively proliferating MYC-driven B cells stand out against the dark sheet of tumor.
- `connects-to` → **[Malaria](../malaria/README.md)** — Endemic Burkitt lymphoma is malaria-driven: chronic Plasmodium falciparum infection drives intense B-cell proliferation and weakens control of co-infecting Epstein-Barr virus, together promoting the MYC translocation that causes the jaw and abdominal tumors of African children.
- `connects-to` → **[Hodgkin Lymphoma](../hodgkin-lymphoma/README.md)** — Burkitt and Hodgkin lymphoma are both EBV-associated but biologically opposite: Burkitt is a fast MYC-driven mature B-cell tumor curable with intensive chemo, while Hodgkin is a CD30+ Reed-Sternberg-cell lymphoma with a rich reactive infiltrate, treated differently with ABVD.
- `connects-to` → **[Mantle Cell Lymphoma](../mantle-cell-lymphoma/README.md)** — Burkitt and mantle cell lymphoma are aggressive B-cell lymphomas defined by single translocations: Burkitt's t(8;14) drives MYC, mantle cell's t(11;14) drives cyclin D1—but Burkitt is curable while mantle cell is aggressive yet incurable, a key prognostic split.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Burkitt lymphoma is MYC-driven, not BCL2-driven—a key contrast: classic Burkitt carries the MYC translocation and is BCL2-negative, so a tumor with both MYC and BCL2 rearrangements is instead a more aggressive double-hit high-grade lymphoma, not true Burkitt.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Burkitt lymphoma is a germinal-center B cell frozen short of plasma-cell fate: the MYC-driven clone proliferates explosively (near-100% Ki-67) instead of maturing into antibody-secreting plasma cells—so its hallmark is runaway growth, the fastest-doubling human tumor.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Burkitt lymphoma exposes the immune system's role in cancer control: it surges in immunodeficiency (HIV) and where chronic malaria and EBV exhaust immune surveillance—so endemic Burkitt is partly a cancer of weakened immune defense against EBV-driven B cells.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^roschewski-2020-da-epoch-r-bl]: Roschewski M, Dunleavy K, Abramson JS, et al. Multicenter study of risk-adapted therapy with dose-adjusted EPOCH-R in adults with untreated Burkitt lymphoma. *J Clin Oncol.* 2020;38(22):2519-2529. [doi:10.1200/JCO.19.03259](https://doi.org/10.1200/JCO.19.03259) · [PubMed 32530765](https://pubmed.ncbi.nlm.nih.gov/32530765/)
[^minard-colin-2017-inter-b-nhl-ritux]: Minard-Colin V, Auperin A, Pillon M, et al. Rituximab for children and adolescents with high-risk B-cell non-Hodgkin lymphoma: results of the randomized Inter-B-NHL Ritux 2010 trial. *J Clin Oncol.* 2022;40(22):2458-2471. [doi:10.1200/JCO.21.01940](https://doi.org/10.1200/JCO.21.01940) · [PubMed 35436151](https://pubmed.ncbi.nlm.nih.gov/35436151/)

---
schema: human-scale-entry/v1
id: waldenstrom-macroglobulinemia
name: Waldenström Macroglobulinemia
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Waldenström macroglobulinemia is lymphoplasmacytic lymphoma producing IgM monoclonal protein; MYD88 L265P in ~90% drives NF-κB and JAK-STAT3. Hyperviscosity, neuropathy, and cryoglobulinemia are hallmarks; ibrutinib and zanubrutinib are approved for MYD88 L265P WM."
aliases: ["Waldenström macroglobulinemia", "WM", "lymphoplasmacytic lymphoma", "LPL", "IgM monoclonal protein", "IgM paraprotein", "hyperviscosity syndrome", "MYD88 L265P WM"]
sources:
  - id: treon-2015-ibrutinib-wm
    type: peer-reviewed
    cite: "Treon SP, Tripsas CK, Meid K, et al. Ibrutinib in previously treated Waldenström's macroglobulinemia. N Engl J Med. 2015;373(18):1765-1774."
    doi: "10.1056/NEJMoa1501548"
    pmid: "26352686"
    url: "https://doi.org/10.1056/NEJMoa1501548"
  - id: tam-2020-aspen
    type: peer-reviewed
    cite: "Tam CS, Opat S, D'Sa S, et al. A randomized phase 3 trial of zanubrutinib vs ibrutinib in symptomatic Waldenström macroglobulinemia: the ASPEN study. Blood. 2020;136(18):2038-2050."
    doi: "10.1182/blood.2020006844"
    pmid: "32828187"
    url: "https://doi.org/10.1182/blood.2020006844"
cross_links:
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "MYD88 L265P → constitutive NF-κB via IRAK4-TRAF6-IKK → BCL-2, MYC, CXCR4 transcription; ibrutinib (BTK inhibitor) blocks BTK-dependent NF-κB in MYD88 L265P WM (ORR >90%); CXCR4 mutation (~35%) confers ibrutinib resistance (ORR ~60%)."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "MYD88 L265P drives JAK1-STAT3 → BCL-XL survival in WM independent of cytokine receptor signaling; ruxolitinib (JAK1/2 inhibitor) shows activity in MYD88 L265P WM; combined BTK+JAK inhibition studied in ibrutinib-resistant WM; JAK2 V617F absent in WM (unlike MPN)."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "BCL-2 overexpression is driven by MYD88/NF-κB → IRF4 in WM; venetoclax (BCL-2 inhibitor) shows activity in R/R WM; combined ibrutinib+venetoclax achieves deep responses in R/R WM; BCL-2 is an anti-apoptotic target complementary to BTK inhibition in WM."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "Rituximab ± bendamustine or cyclophosphamide is first-line for WM; rituximab monotherapy causes IgM flare (~40%) before response; ofatumumab and obinutuzumab are alternatives for rituximab-refractory WM; CD20 is uniformly expressed (CD19+/CD20+/sIgM+)."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCR4 gain-of-function mutations (WHIM-type S338X, C1013G) in 30-40% of WM → impaired receptor desensitization → enhanced CXCL12/CXCR4 bone marrow retention and resistance to BTK inhibitor ibrutinib; CXCR4 mutation status predicts ibrutinib response and PFS in WM."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Waldenström macroglobulinemia is a lymphoplasmacytic lymphoma — a clonal B-cell neoplasm frozen midway between a memory B cell and an IgM-secreting plasma cell; this dual identity gives it both surface CD20 and cytoplasmic IgM and shapes its B-cell-directed therapy."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "MYD88 L265P, present in ~90% of WM, is the defining and diagnostic mutation: it assembles a constitutive myddosome that fires NF-κB, JAK-STAT3, and BTK to keep the tumor alive, and its presence predicts response to BTK inhibitors — while MYD88-wildtype WM responds poorly."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "About half of WM patients with neuropathy have IgM anti-MAG antibodies that attack peripheral-nerve myelin, producing a distal, symmetric, sensory-predominant demyelinating neuropathy; lowering IgM with rituximab improves it in some, and titer tracks severity."
  - target: 01-human/07-system/multiple-myeloma
    relation: connects-to
    note: "Waldenström macroglobulinemia and myeloma are B-cell dyscrasias secreting a monoclonal paraprotein but differ: WM is a lymphoplasmacytic lymphoma making IgM (hyperviscosity, neuropathy) with MYD88 L265P, while myeloma is a marrow plasma-cell tumor making IgG/IgA with lytic bone."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "WM's malignant clone is lymphoplasmacytic—a spectrum from small B cells to plasma cells—so it secretes monoclonal IgM like a plasma-cell tumor while keeping B-cell markers (CD20); this dual differentiation explains why both rituximab and plasma-cell-directed agents work."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "WM characteristically infiltrates the bone marrow with lymphoplasmacytic cells, often paratrabecular and with increased mast cells; this marrow involvement causes anemia (the commonest symptom) and underlies the cytopenias, with diagnosis confirmed by marrow biopsy."
  - target: 01-human/07-system/follicular-lymphoma
    relation: connects-to
    note: "Waldenström macroglobulinemia and follicular lymphoma are both indolent B-cell non-Hodgkin lymphomas but molecularly distinct: WM is a lymphoplasmacytic lymphoma defined by MYD88 L265P and an IgM paraprotein, while follicular lymphoma is BCL2-translocated."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Waldenström macroglobulinemia can transform into aggressive diffuse large B-cell lymphoma: like other indolent lymphomas, the low-grade clone can acquire further lesions and evolve into DLBCL, a Richter-like transformation with rapid deterioration and worse prognosis."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Hyperviscosity from WM's IgM paraprotein can mimic or cause stroke: large pentameric IgM thickens blood, causing headache, visual blurring, and neurological deficits, so a stroke-like presentation with a very high protein points to WM, treated by plasmapheresis."
  - target: 01-human/07-system/mantle-cell-lymphoma
    relation: connects-to
    note: "Waldenström macroglobulinemia and mantle cell lymphoma are both B-cell non-Hodgkin lymphomas but distinct: WM is a lymphoplasmacytic lymphoma secreting IgM (MYD88 L265P) causing hyperviscosity, while MCL is a t(11;14) cyclin-D1 nodal tumor."
  - target: 01-human/07-system/cll
    relation: connects-to
    note: "Waldenström macroglobulinemia and CLL are indolent mature B-cell neoplasms: both involve small B cells and respond to BTK inhibitors, but WM's cells secrete monoclonal IgM while CLL circulates as a leukemia—immunophenotype and MYD88 separate them."
  - target: 01-human/07-system/hepatitis-c
    relation: connects-to
    note: "Hepatitis C links to Waldenström macroglobulinemia: chronic HCV-driven B-cell stimulation can progress to lymphoplasmacytic lymphoma, so HCV is screened for in IgM-secreting lymphomas—and antiviral cure can sometimes treat the lymphoproliferation."
  - target: 01-human/03-molecular/btk
    relation: connects-to
    note: "WM is exquisitely BTK-dependent: its hallmark MYD88 mutation signals through Bruton tyrosine kinase to drive malignant B-cell survival, so BTK inhibitors like ibrutinib are highly effective—response even predicted by MYD88 and CXCR4 genotype."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "WM's monoclonal IgM attacks red cells: it can act as a cold agglutinin that clumps and lyses erythrocytes, and marrow infiltration suppresses production, so anemia—often the presenting feature—comes from both hemolysis and crowded-out red-cell formation."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "WM is a classic cause of hyperviscosity retinopathy: the thick, IgM-laden blood engorges and tortuoses retinal veins ('sausage-link' veins) and can cause hemorrhages and blurred vision—an ophthalmoscopic clue that prompts urgent plasmapheresis."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Waldenström's IgM impairs platelets and bleeding: the huge monoclonal IgM coats platelets and clotting factors and thickens blood, so patients bruise and bleed—nosebleeds and mucosal bleeding—even as hyperviscosity paradoxically also risks clots and stroke."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Waldenström's infiltrates the spleen and lymph nodes: the malignant lymphoplasmacytic cells expand beyond the marrow into the spleen and nodes, causing splenomegaly and lymphadenopathy that mark it as a lymphoma, not just a plasma-cell disorder."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Anemia is Waldenström's most common problem: marrow crowding by tumor cells plus chronic-disease and dilutional effects of the expanded plasma volume lower hemoglobin, so fatigue from anemia—not hyperviscosity—is usually what brings patients in."
  - target: 01-human/07-system/pcnsl
    relation: connects-to
    note: "Waldenstrom and primary CNS lymphoma share the MYD88 L265P mutation: when WM invades the brain it is called Bing-Neel syndrome, and the shared mutation makes both B-cell cancers responsive to BTK inhibitors that cross into the CNS."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Waldenstrom's IgM can turn on complement against red cells: as cold agglutinins or cryoglobulins, the paraprotein binds erythrocytes and fixes complement (C3), causing hemolysis—an extra anemia beyond marrow crowding."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Waldenstrom's marrow is studded with mast cells: increased mast cells are a characteristic histologic feature that support the lymphoplasmacytic clone through CD40-ligand and cytokines, part of the tumor's marrow microenvironment."
  - target: 01-human/03-molecular/albumin
    relation: connects-to
    note: "Waldenström's hallmark is hyperviscosity from monoclonal protein: the malignant clone floods blood with IgM that thickens it, inverting the normal albumin-to-globulin ratio and causing the bleeding, visual, and neurologic symptoms relieved by plasmapheresis."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Waldenström's cells survive on autophagy downstream of MYD88: constant MYD88/NF-κB signaling and heavy antibody output make the clone lean on autophagy to manage stress, a vulnerability alongside the BTK pathway that drugs target."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Waldenström evades immunity through regulatory T cells: the marrow accumulates Tregs and exhausted T cells that dampen the antitumor response, helping the slow-growing lymphoplasmacytic clone persist and limiting immunotherapy."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Waldenström can invade the brain: in rare Bing-Neel syndrome the lymphoplasmacytic cells seed the central nervous system, causing headaches, confusion, and neurological deficits that require treatments able to cross into the brain."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Waldenström blunts the body's iron use: marrow packed with the clone and chronic inflammation choke off red-cell production and lock away iron, so anemia—often the presenting complaint—dominates the disease."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Waldenström's thick IgM batters the endothelium: the sludgy, hyperviscous blood engorges and damages the vessel-lining cells, swelling retinal veins and causing the headaches, bleeding, and vision loss of hyperviscosity syndrome."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Waldenström's hyperviscosity shows in the eye: fundoscopy in visible light reveals dilated, sausage-segmented retinal veins, while CT photons map the lymph-node and spleen enlargement of the clone."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Waldenström spreads through the lymphatic organs: hepatomegaly and lymphadenopathy join the splenomegaly as the lymphoplasmacytic clone seeds beyond the bone marrow."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Waldenström's high IgM fools the lab: the excess protein displaces water in the blood sample, producing a spurious low sodium—pseudohyponatremia—that must not be wrongly corrected."
---

# Waldenström Macroglobulinemia

## Overview

**Waldenström macroglobulinemia (WM)** is a rare indolent B-cell malignancy defined by **lymphoplasmacytic lymphoma (LPL)** — a neoplasm of small lymphocytes, plasmacytoid lymphocytes, and plasma cells — with serum **IgM monoclonal protein** (IgM paraprotein). WM accounts for ~2% of hematologic malignancies (~2,000 new cases/year in the US); it follows a characteristically indolent natural history (median OS >10 years) but produces organ dysfunction via IgM-mediated complications: hyperviscosity syndrome, peripheral neuropathy (antimyelin antibodies), cold agglutinin hemolytic anemia, cryoglobulinemia, and systemic amyloidosis (AL). The molecular landscape of WM is dominated by **MYD88 L265P** (~90%), the landmark somatic mutation identifying constitutive NF-κB/JAK-STAT activation as the oncogenic driver, and **CXCR4 WHIM mutations** (~35%) that confer BTK inhibitor resistance. Ibrutinib (FDA approved 2015) and zanubrutinib (ASPEN trial, FDA approved 2021) transformed WM management [^treon-2015-ibrutinib-wm].

**Epidemiology:**
- ~2,000 new cases/year in the US; predominantly older patients (median age ~70); M:F ~2:1
- Mostly Caucasian; familial clustering in ~20% of WM (highest familial risk of any lymphoma)
- Incurable with current therapy; median OS >10 years for treated symptomatic WM
- MGUS-IgM (IgM monoclonal gammopathy of undetermined significance) → WM progression rate ~1.5%/year
- 5-year OS: ~87% (modern BTK inhibitor era); favorable prognosis for most patients

## Structure

### Molecular landscape

**MYD88 L265P (Leu265Pro, TIR domain):**
Present in ~90% of WM/LPL; diagnostic and predictive biomarker; constitutive myddosome assembly → IRAK4-IRAK1 → TRAF6 → NF-κB → BCL-2, CXCR4, IRF4; also activates BTK (non-canonical) and JAK1-STAT3 (via IRAK1). MYD88 WT WM (~10%): inferior outcomes with BTK inhibitors; consider clinical trial or rituximab-based regimen.

**CXCR4 WHIM mutations (exon 2, C-terminal truncations):**
Found in ~35% of WM; gain-of-function truncations that impair CXCR4 internalization → prolonged CXCL12 signaling → PI3K-AKT-ERK → reduced BTK inhibitor efficacy. CXCR4 mutations occur on MYD88 L265P background (virtually never alone); allele burden correlates with depth of ibrutinib response failure.

**Additional co-mutations:**
- ARID1A: ~17%; chromatin remodeling; SWI/SNF subunit
- CD79B: ~5-10% in LPL (more common in ABC-DLBCL); BCR co-receptor; BTK dependency
- TP53: ~5%; rare in WM (unlike aggressive lymphoma); poor prognosis
- 6q deletion: ~40%; most common cytogenetic abnormality; not targetable but prognostic
- Trisomy 4: Less common; prognostic value under study

**Immunophenotype:**
CD19+, CD20+ (often dim), CD22+, CD25+, CD27+ (memory B marker), sIgM+; CD5−, CD10−, CD23−, CD103−; plasma cell component: cytoplasmic IgM+, CD38+, CD138+; PAS-positive intranuclear inclusions (Dutcher bodies) in some cases; mast cells prominent in BM background (CD117+, MYD88 L265P positive — WM microenvironment feature).

### IgM monoclonal protein biology

**IgM structure and overproduction:**
WM plasma cells secrete IgM (pentameric, MW ~900 kDa) as monoclonal paraprotein; elevated serum IgM (often >3 g/dL) → several complications driven by IgM physicochemical properties:

**Hyperviscosity syndrome:**
IgM pentamers are large and do not circulate freely at high concentrations → blood viscosity increases at IgM >4-5 g/dL → retinal hemorrhage (funduscopic "sausage-link" veins), visual disturbance, headache, mental status change, heart failure; treat with urgent plasmapheresis to remove IgM → immediate viscosity reduction before chemotherapy (rituximab can cause transient IgM spike → plasmapheresis before rituximab if symptomatic hyperviscosity).

**Peripheral neuropathy:**
IgM anti-MAG (myelin-associated glycoprotein) antibodies in ~50% of WM neuropathy → predominantly sensory demyelinating neuropathy (distal, symmetric, predominantly sensory, gait disturbance); anti-MAG antibody titer correlates with neuropathy severity; anti-GD1b, anti-GM1 antibodies: motor neuropathy variants; rituximab reduces IgM burden → neuropathy improvement in some.

**Cold agglutinin hemolytic anemia:**
IgM anti-I antibodies bind erythrocytes at cold temperatures → complement activation → hemolysis; common cold agglutinin disease in WM (1°C-10°C: IgM binds/dissociates); sutimlimab (anti-C1s) approved for cold agglutinin disease.

**Cryoglobulinemia:**
IgM (often with IgG) precipitates in cold → mixed cryoglobulinemia (type II) → vasculitis, purpura, arthralgias, membranoproliferative glomerulonephritis; treatment: plasmapheresis + rituximab + immunosuppression for severe manifestations.

## Function

### Normal B-cell to plasma cell differentiation

Mature naive B-cells → antigen stimulation + T-cell help → GC formation → affinity maturation → class switch recombination (in GCB cells) OR terminal differentiation to plasma cells or memory B-cells. IgM-secreting plasma cells are the immediate product of T-independent B-cell activation (without class switching); in WM, this differentiation program is arrested at the lymphoplasmacytic stage — partially differentiated toward plasma cell secreting IgM but retaining B-cell surface markers (CD20).

### BM microenvironment in WM

The WM BM contains characteristic mast cells (CD117+, tryptase+, MYD88 L265P+) that support WM cell survival via CD40L-CD40 interaction → NF-κB; CXCL12/CXCR4 axis retains WM cells in the BM niche; IL-6, BAFF (B-cell activating factor), APRIL from stromal cells → plasma cell differentiation signals. IgM paraprotein in BM interstitium contributes to hyperviscosity and neuropathy independently of blood IgM levels.

## Pathology

### Diagnostic criteria (WHO 2022)

1. IgM monoclonal gammopathy of any concentration
2. BM infiltration by lymphoplasmacytic lymphoma (≥10% of BM cellularity by clonal lymphoplasmacytic cells)
3. Pathological pattern: Small lymphocytes + plasmacytoid lymphocytes + plasma cells; paratrabecular or diffuse BM involvement; PAS+ Dutcher bodies (intranuclear pseudo-inclusions of IgM); mast cells in background; CD20+/CD138+ dual staining shows lymphocytic + plasmacytic spectrum

**Note:** Symptomatic WM = LPL + IgM + any WM-related organ damage (anemia, hyperviscosity, neuropathy, cryoglobulinemia, amyloidosis, hepatosplenomegaly). Asymptomatic (smoldering) WM = LPL + IgM but no organ damage.

**IPSSWM (International Prognostic Scoring System for WM):**
5 adverse factors: Age >65, Hgb ≤11.5 g/dL, platelets ≤100 × 10⁹/L, β2M >3 mg/L, serum IgM >7 g/dL
- Low risk (0-1 factors, not age): Median OS >10 years
- Intermediate (2 factors or age alone): Median OS 8-10 years
- High risk (≥3 factors): Median OS 3-5 years

**Staging workup:**
- CBC, comprehensive metabolic panel, serum protein electrophoresis + IFE (confirm IgM monoclonal), quantitative immunoglobulins, serum free light chains, β2M, LDH, uric acid
- CT chest/abdomen/pelvis: Lymphadenopathy, splenomegaly, extramedullary disease
- BM biopsy + aspirate: Diagnostic; morphology, immunohistochemistry (CD20, CD138, CD56, κ/λ), flow cytometry
- MYD88 L265P mutation testing (AS-PCR or NGS on BM/blood); CXCR4 mutation testing (BM/blood NGS)
- Viscosity measurement: Serum viscosity if IgM >4 g/dL or symptoms
- Anti-MAG antibodies: If neuropathy present; nerve conduction studies
- Echocardiogram/fat pad biopsy: If amyloidosis suspected (AL amyloid deposition in WM)

### Treatment

**Watch and wait (asymptomatic WM):**
~25-30% of newly diagnosed WM is asymptomatic; ECOG 9902 study: No benefit to early treatment in asymptomatic WM; initiate therapy when: symptomatic anemia (Hgb <10 g/dL), symptomatic hyperviscosity, progressive neuropathy, cryoglobulinemia, amyloidosis, bulky lymphadenopathy, thrombocytopenia (<100 × 10⁹/L), or IgM >4 g/dL with symptoms.

**Plasmapheresis (emergent):**
For symptomatic hyperviscosity → removes IgM immediately; does not treat underlying WM; used before rituximab (avoids IgM flare-mediated hyperviscosity exacerbation); requires 2-4 sessions to lower IgM before chemoimmunotherapy.

**First-line systemic therapy:**

**BTK inhibitors (preferred for MYD88 L265P WM):**
- **Ibrutinib 420 mg daily:** [^treon-2015-ibrutinib-wm] Phase 2, R/R WM; ORR 90.5% (VGPR 12%); median PFS 69 months in MYD88 L265P/CXCR4 WT; FDA approved 2015; ECOG-ACRIN 1603 (1st-line): ibrutinib+rituximab superior to PO-rituximab+dexamethasone; toxicities: AFib (~10-15%), bleeding, hypertension, arthralgias
- **Zanubrutinib 160 mg BID (ASPEN trial):** [^tam-2020-aspen] Randomized vs. ibrutinib; VGPR or better: 28% vs. 19% at 19 months; similar OS; AFib rate ~2% vs. ~15%; FDA approved 2021; preferred for cardiac-risk patients or post-ibrutinib intolerance

**Chemoimmunotherapy (BTK inhibitor-ineligible or MYD88 WT WM):**
- **Rituximab + bendamustine (BR):** ORR ~93%; deep responses; peripheral neuropathy risk with bendamustine is lower than bortezomib regimens
- **Rituximab + cyclophosphamide + dexamethasone (RCD) / Rituximab + cyclophosphamide + dexamethasone + bortezomib (BDR):** Less preferred; neuropathy with bortezomib + existing WM neuropathy is problematic

**Relapsed/refractory WM:**
- **Zanubrutinib (after ibrutinib):** Active in ibrutinib-intolerant patients (cardiac/bleeding issues)
- **Pirtobrutinib (non-covalent BTK inhibitor):** Active after covalent BTK inhibitor progression; C481S resistance overcome by non-covalent BTK inhibition; BRUIN trial includes WM; ORR ~70% in BTK-refractory WM
- **Venetoclax:** Active in R/R WM; ibrutinib+venetoclax combination (VCAP trial): deep responses
- **Rituximab + cyclophosphamide (or bendamustine):** Re-challenge if prior response
- **Proteasome inhibitors (bortezomib/carfilzomib + rituximab):** Active in WM; bortezomib toxicity limited by neuropathy
- **Auto-SCT:** Selected high-risk patients in second remission

**WM neuropathy specific:**
- Rituximab-based regimens to reduce IgM burden → neuropathy improvement in ~30-40%; IgM level correlates with neuropathy severity; goal: IgM <1 g/dL for maximal neuropathy benefit
- Intravenous immunoglobulin (IVIg): Symptomatic relief for anti-MAG neuropathy; not disease-modifying
- Sutimlimab (anti-C1s): For cold agglutinin-mediated hemolysis

## Connections

- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — MYD88 L265P → constitutive NF-κB via IRAK4-TRAF6-IKK → BCL-2, MYC, CXCR4 transcription; ibrutinib (BTK inhibitor) blocks BTK-dependent NF-κB in MYD88 L265P WM (ORR >90%); CXCR4 mutation (~35%) confers ibrutinib resistance (ORR ~60%).
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — MYD88 L265P drives JAK1-STAT3 → BCL-XL survival in WM independent of cytokine receptor signaling; ruxolitinib (JAK1/2 inhibitor) shows activity in MYD88 L265P WM; combined BTK+JAK inhibition studied in ibrutinib-resistant WM; JAK2 V617F absent in WM (unlike MPN).
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — BCL-2 overexpression is driven by MYD88/NF-κB → IRF4 in WM; venetoclax (BCL-2 inhibitor) shows activity in R/R WM; combined ibrutinib+venetoclax achieves deep responses in R/R WM; BCL-2 is an anti-apoptotic target complementary to BTK inhibition in WM.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — Rituximab ± bendamustine or cyclophosphamide is first-line for WM; rituximab monotherapy causes IgM flare (~40%) before response; ofatumumab and obinutuzumab are alternatives for rituximab-refractory WM; CD20 is uniformly expressed (CD19+/CD20+/sIgM+).
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — Waldenström macroglobulinemia is a lymphoplasmacytic lymphoma — a clonal B-cell neoplasm frozen midway between a memory B cell and an IgM-secreting plasma cell; this dual identity gives it both surface CD20 and cytoplasmic IgM and shapes its B-cell-directed therapy.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — MYD88 L265P, present in ~90% of WM, is the defining and diagnostic mutation: it assembles a constitutive myddosome that fires NF-κB, JAK-STAT3, and BTK to keep the tumor alive, and its presence predicts response to BTK inhibitors — while MYD88-wildtype WM responds poorly.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — About half of WM patients with neuropathy have IgM anti-MAG antibodies that attack peripheral-nerve myelin, producing a distal, symmetric, sensory-predominant demyelinating neuropathy; lowering IgM with rituximab improves it in some, and titer tracks severity.
- `connects-to` → **[Multiple Myeloma](../multiple-myeloma/README.md)** — Waldenström macroglobulinemia and myeloma are B-cell dyscrasias secreting a monoclonal paraprotein but differ: WM is a lymphoplasmacytic lymphoma making IgM (hyperviscosity, neuropathy) with MYD88 L265P, while myeloma is a marrow plasma-cell tumor making IgG/IgA with lytic bone.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — WM's malignant clone is lymphoplasmacytic—a spectrum from small B cells to plasma cells—so it secretes monoclonal IgM like a plasma-cell tumor while keeping B-cell markers (CD20); this dual differentiation explains why both rituximab and plasma-cell-directed agents work.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — WM characteristically infiltrates the bone marrow with lymphoplasmacytic cells, often paratrabecular and with increased mast cells; this marrow involvement causes anemia (the commonest symptom) and underlies the cytopenias, with diagnosis confirmed by marrow biopsy.
- `connects-to` → **[Follicular Lymphoma](../follicular-lymphoma/README.md)** — Waldenström macroglobulinemia and follicular lymphoma are both indolent B-cell non-Hodgkin lymphomas but molecularly distinct: WM is a lymphoplasmacytic lymphoma defined by MYD88 L265P and an IgM paraprotein, while follicular lymphoma is BCL2-translocated.
- `connects-to` → **[Diffuse Large B-Cell Lymphoma](../dlbcl/README.md)** — Waldenström macroglobulinemia can transform into aggressive diffuse large B-cell lymphoma: like other indolent lymphomas, the low-grade clone can acquire further lesions and evolve into DLBCL, a Richter-like transformation with rapid deterioration and worse prognosis.
- `connects-to` → **[Stroke](../stroke/README.md)** — Hyperviscosity from WM's IgM paraprotein can mimic or cause stroke: large pentameric IgM thickens blood, causing headache, visual blurring, and neurological deficits, so a stroke-like presentation with a very high protein points to WM, treated by plasmapheresis.
- `connects-to` → **[Mantle Cell Lymphoma](../mantle-cell-lymphoma/README.md)** — Waldenström macroglobulinemia and mantle cell lymphoma are both B-cell non-Hodgkin lymphomas but distinct: WM is a lymphoplasmacytic lymphoma secreting IgM (MYD88 L265P) causing hyperviscosity, while MCL is a t(11;14) cyclin-D1 nodal tumor.
- `connects-to` → **[CLL](../cll/README.md)** — Waldenström macroglobulinemia and CLL are indolent mature B-cell neoplasms: both involve small B cells and respond to BTK inhibitors, but WM's cells secrete monoclonal IgM while CLL circulates as a leukemia—immunophenotype and MYD88 separate them.
- `connects-to` → **[Hepatitis C](../hepatitis-c/README.md)** — Hepatitis C links to Waldenström macroglobulinemia: chronic HCV-driven B-cell stimulation can progress to lymphoplasmacytic lymphoma, so HCV is screened for in IgM-secreting lymphomas—and antiviral cure can sometimes treat the lymphoproliferation.
- `connects-to` → **[BTK](../../03-molecular/btk/README.md)** — WM is exquisitely BTK-dependent: its hallmark MYD88 mutation signals through Bruton tyrosine kinase to drive malignant B-cell survival, so BTK inhibitors like ibrutinib are highly effective—response even predicted by MYD88 and CXCR4 genotype.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — WM's monoclonal IgM attacks red cells: it can act as a cold agglutinin that clumps and lyses erythrocytes, and marrow infiltration suppresses production, so anemia—often the presenting feature—comes from both hemolysis and crowded-out red-cell formation.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — WM is a classic cause of hyperviscosity retinopathy: the thick, IgM-laden blood engorges and tortuoses retinal veins ('sausage-link' veins) and can cause hemorrhages and blurred vision—an ophthalmoscopic clue that prompts urgent plasmapheresis.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Waldenström's IgM impairs platelets and bleeding: the huge monoclonal IgM coats platelets and clotting factors and thickens blood, so patients bruise and bleed—nosebleeds and mucosal bleeding—even as hyperviscosity paradoxically also risks clots and stroke.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Waldenström's infiltrates the spleen and lymph nodes: the malignant lymphoplasmacytic cells expand beyond the marrow into the spleen and nodes, causing splenomegaly and lymphadenopathy that mark it as a lymphoma, not just a plasma-cell disorder.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Anemia is Waldenström's most common problem: marrow crowding by tumor cells plus chronic-disease and dilutional effects of the expanded plasma volume lower hemoglobin, so fatigue from anemia—not hyperviscosity—is usually what brings patients in.
- `connects-to` → **[Primary CNS Lymphoma](../pcnsl/README.md)** — Waldenstrom and primary CNS lymphoma share the MYD88 L265P mutation: when WM invades the brain it is called Bing-Neel syndrome, and the shared mutation makes both B-cell cancers responsive to BTK inhibitors that cross into the CNS.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Waldenstrom's IgM can turn on complement against red cells: as cold agglutinins or cryoglobulins, the paraprotein binds erythrocytes and fixes complement (C3), causing hemolysis—an extra anemia beyond marrow crowding.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Waldenstrom's marrow is studded with mast cells: increased mast cells are a characteristic histologic feature that support the lymphoplasmacytic clone through CD40-ligand and cytokines, part of the tumor's marrow microenvironment.
- `connects-to` → **[Albumin](../../03-molecular/albumin/README.md)** — Waldenström's hallmark is hyperviscosity from monoclonal protein: the malignant clone floods blood with IgM that thickens it, inverting the normal albumin-to-globulin ratio and causing the bleeding, visual, and neurologic symptoms relieved by plasmapheresis.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Waldenström's cells survive on autophagy downstream of MYD88: constant MYD88/NF-κB signaling and heavy antibody output make the clone lean on autophagy to manage stress, a vulnerability alongside the BTK pathway that drugs target.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Waldenström evades immunity through regulatory T cells: the marrow accumulates Tregs and exhausted T cells that dampen the antitumor response, helping the slow-growing lymphoplasmacytic clone persist and limiting immunotherapy.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Waldenström can invade the brain: in rare Bing-Neel syndrome the lymphoplasmacytic cells seed the central nervous system, causing headaches, confusion, and neurological deficits that require treatments able to cross into the brain.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Waldenström blunts the body's iron use: marrow packed with the clone and chronic inflammation choke off red-cell production and lock away iron, so anemia—often the presenting complaint—dominates the disease.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Waldenström's thick IgM batters the endothelium: the sludgy, hyperviscous blood engorges and damages the vessel-lining cells, swelling retinal veins and causing the headaches, bleeding, and vision loss of hyperviscosity syndrome.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Waldenström's hyperviscosity shows in the eye: fundoscopy in visible light reveals dilated, sausage-segmented retinal veins, while CT photons map the lymph-node and spleen enlargement of the clone.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Waldenström spreads through the lymphatic organs: hepatomegaly and lymphadenopathy join the splenomegaly as the lymphoplasmacytic clone seeds beyond the bone marrow.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Waldenström's high IgM fools the lab: the excess protein displaces water in the blood sample, producing a spurious low sodium—pseudohyponatremia—that must not be wrongly corrected.

[^treon-2015-ibrutinib-wm]: Treon SP, Tripsas CK, Meid K, et al. Ibrutinib in previously treated Waldenström's macroglobulinemia. *N Engl J Med.* 2015;373(18):1765-1774. [doi:10.1056/NEJMoa1501548](https://doi.org/10.1056/NEJMoa1501548) · [PubMed 26352686](https://pubmed.ncbi.nlm.nih.gov/26352686/)
[^tam-2020-aspen]: Tam CS, Opat S, D'Sa S, et al. A randomized phase 3 trial of zanubrutinib vs ibrutinib in symptomatic Waldenström macroglobulinemia: the ASPEN study. *Blood.* 2020;136(18):2038-2050. [doi:10.1182/blood.2020006844](https://doi.org/10.1182/blood.2020006844) · [PubMed 32828187](https://pubmed.ncbi.nlm.nih.gov/32828187/)

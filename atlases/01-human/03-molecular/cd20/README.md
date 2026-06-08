---
schema: human-scale-entry/v1
id: cd20
name: CD20
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "B-lymphocyte surface antigen (MS4A1); expressed on pre-B through memory B cells; absent on plasma cells. Targeted by anti-CD20 monoclonal antibodies (rituximab, obinutuzumab); R-CHOP is frontline for DLBCL; CD20-negative escape post-rituximab is a resistance mechanism in NHL."
aliases: ["CD20", "MS4A1", "B1 antigen", "Bp35", "membrane-spanning 4-domains A1", "anti-CD20", "rituximab target"]
sources:
  - id: maloney-1997-rituximab
    type: peer-reviewed
    cite: "Maloney DG, Grillo-López AJ, White CA, et al. IDEC-C2B8 (rituximab) anti-CD20 monoclonal antibody therapy in patients with relapsed low-grade non-Hodgkin's lymphoma. Blood. 1997;90(6):2188-2195."
    doi: "10.1182/blood.V90.6.2188"
    pmid: "9310469"
    url: "https://doi.org/10.1182/blood.V90.6.2188"
  - id: coiffier-2002-rchop
    type: peer-reviewed
    cite: "Coiffier B, Lepage E, Brière J, et al. CHOP chemotherapy plus rituximab compared with CHOP alone in elderly patients with diffuse large-B-cell lymphoma. N Engl J Med. 2002;346(4):235-242."
    doi: "10.1056/NEJMoa011795"
    pmid: "11807147"
    url: "https://doi.org/10.1056/NEJMoa011795"
cross_links:
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "CD20 is highly expressed on ABC-DLBCL cells driven by constitutive NF-κB (MYD88 L265P → BTK → NF-κB); rituximab triggers ADCC, CDC, and direct apoptosis in NF-κB-driven B cells; ibrutinib (BTK inhibitor) + rituximab active in MYD88-mutant DLBCL and MCL."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "GCB-DLBCL with t(14;18) → BCL-2 overexpression → apoptosis resistance; rituximab + venetoclax + R-CHOP under study in BCL-2-high DLBCL; double-hit lymphoma (MYC + BCL-2 rearrangement) → venetoclax + dose-adjusted EPOCH-R preferred over R-CHOP."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "MYC rearrangement in ~10% of DLBCL; double-hit (MYC + BCL-2) or triple-hit (+ BCL-6) → high-grade B-cell lymphoma; R-CHOP inferior → EPOCH-R or CAR-T preferred; MYC protein expression >40% is an independent poor-prognosis marker in CD20+ DLBCL."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "B cells co-express CD20 and MHC class II; CD20 downregulation and MHC-II loss are rituximab resistance mechanisms; obinutuzumab reduces CD20 internalization vs. rituximab; CD20×CD3 bispecifics (epcoritamab, glofitamab) bypass MHC-II for T cell-mediated killing."
  - target: 01-human/07-system/nmo
    relation: connects-to
    note: "Rituximab (anti-CD20) depletes B cells → reduces AQP4-IgG and is widely used as off-label first-line NMOSD prevention (~70-80% ARR reduction); inebilizumab (anti-CD19) is approved (N-MOmentum; FDA Jun 2020); ublituximab under investigation in NMOSD trials."
  - target: 01-human/07-system/anca-vasculitis
    relation: connects-to
    note: "Rituximab (anti-CD20) depletes autoreactive B cells in ANCA vasculitis; RAVE trial: rituximab non-inferior to cyclophosphamide for GPA/MPA induction (64% vs 53% CR; FDA Apr 2011); rituximab superior in relapsing disease; MAINRITSAN maintenance reduces relapse."
  - target: 01-human/07-system/sjogrens-syndrome
    relation: connects-to
    note: "Rituximab (anti-CD20) depletes B cells in pSS; TEARS/TRACTISS Phase 3 had mixed results on ESSPRI; used off-label for severe extraglandular pSS (cryoglobulinemia, vasculitis, lymphoma); CD20+ ectopic GC B cells in salivary glands drive anti-Ro/SSA production and lymphomagenesis."
---

# CD20

## Overview

**CD20 (MS4A1, membrane-spanning 4-domains subfamily A member 1)** is a non-glycosylated phosphoprotein exclusively expressed on the surface of **B lymphocytes** from the pre-B cell stage through memory B cells. CD20 is absent on hematopoietic stem cells, pro-B cells, and terminally differentiated plasma cells — a distribution that makes it an ideal therapeutic target: anti-CD20 therapy depletes the entire B cell compartment while sparing hematopoietic stem cells and immunoglobulin-secreting plasma cells [^maloney-1997-rituximab].

**CD20 in B-cell malignancies:**
- **DLBCL:** CD20+ in >95% of cases; R-CHOP (rituximab + CHOP) established as standard of care in 2002 (Coiffier trial) with ~60-70% cure rate
- **Follicular lymphoma (FL):** CD20+ in >99%; rituximab-based therapy is the backbone; obinutuzumab-based therapy improves PFS vs. rituximab
- **Mantle cell lymphoma (MCL):** CD20+; R-hyper-CVAD or R-bendamustine frontline; ibrutinib/venetoclax + rituximab in R/R
- **Chronic lymphocytic leukemia (CLL):** CD20 expression lower than in NHL; obinutuzumab + chlorambucil or venetoclax + obinutuzumab are standard options
- **Multiple sclerosis:** CD20+ B cells (but not plasma cells) contribute to MS pathogenesis; ocrelizumab, ofatumumab, ublituximab approved for MS
- **Primary immunotherapy target:** Rituximab (1997) was one of the first monoclonal antibody therapeutics approved for cancer — a watershed in oncology

**Expression pattern:**
CD20 is the most B-cell-restricted surface marker in clinical use. Expression increases during B cell maturation from pre-B to mature naïve B cells → memory B cells; dramatically downregulated upon plasma cell differentiation (→ explains why Ig levels are partially preserved after rituximab therapy).

## Structure

### CD20 protein architecture

CD20 (MS4A1) is a member of the **membrane-spanning 4-domain (MS4A) superfamily** — a family of tetraspan transmembrane proteins with roles in signal transduction and ion channel-like functions:

**Topology:**
- 297 amino acids; ~33-37 kDa (varies with phosphorylation)
- **N-terminus (intracellular):** Cytoplasmic; interacts with kinases (LYN, Fyn) and PLCγ
- **TM1 (helix 1):** First transmembrane domain
- **TM2 (helix 2):** Second transmembrane domain → short extracellular loop 1 (EL1)
- **Large extracellular loop (EL2, residues 163-206):** The primary antibody-binding domain; contains two disulfide bonds and a structurally critical "EPASE" motif; type I and type II anti-CD20 antibodies bind different epitopes within EL2 with distinct functional consequences
- **TM3 (helix 3):** Third transmembrane domain
- **TM4 (helix 4):** Fourth transmembrane domain → short extracellular loop 2 (EL3)
- **C-terminus (intracellular):** Cytoplasmic; the longer intracellular segment (vs. N-term); contains signaling motifs

**Antibody binding epitopes on EL2:**
- **Type I antibodies (rituximab, ofatumumab):** Bind EL2 proximal domain; induce CD20 redistribution into lipid rafts → CDC (complement-dependent cytotoxicity) and ADCC (antibody-dependent cell-mediated cytotoxicity); promote CD20 internalization (reducing surface expression over time)
- **Type II antibodies (obinutuzumab/GA101, tositumomab):** Bind EL2 distal domain; do not redistribute into lipid rafts; minimal CDC; superior direct B cell apoptosis induction and enhanced ADCC; reduced CD20 internalization → more sustained surface expression → potentially longer immune effector engagement

**CD20 as a calcium channel:**
CD20 has been proposed to function as a store-operated Ca²⁺ channel or Ca²⁺ entry facilitator in B cells. The channel activity is linked to BCR signaling; anti-CD20 binding alters intracellular Ca²⁺ flux. This calcium channel function may contribute to the direct cell death triggered by type II antibodies.

### CD20 in lipid rafts

CD20 resides partially in **detergent-resistant membrane microdomains (lipid rafts)** — cholesterol-enriched platforms that concentrate signaling proteins. Type I anti-CD20 binding → CD20 clustering into lipid rafts → C1q (complement) binding → MAC formation (CDC). CD20's raft association also juxtaposes it with BCR signaling molecules (LYN kinase, CD81) → synergistic signaling disruption.

## Function

### Normal B-cell biology

**CD20 in BCR signaling:**
CD20 associates with CD19-CD21 co-receptor complex and modulates BCR-induced Ca²⁺ mobilization. CD20-deficient mice have subtle B cell signaling defects but are not severely immunocompromised, suggesting CD20 is modulatory rather than essential for B cell development.

**Regulation of CD20 expression:**
- Upregulated by: BCR stimulation, CD40L, cytokines (IL-4), phorbol ester
- Downregulated by: Plasma cell differentiation (Blimp-1 → IRF4 → MS4A1 repression), rituximab (internalization/shaving by FcγRIII+ monocytes)

**CD20 in normal immunity:**
B cells expressing CD20 include: marginal zone B cells, follicular B cells, germinal center B cells, memory B cells — all of which are depleted by anti-CD20 therapy, resulting in humoral immunosuppression lasting 6-12 months post-therapy (until repopulation from CD20-negative pro-B cells).

## Mechanism

### Anti-CD20 mechanisms of action

**Rituximab (IDEC-C2B8, Rituxan):**
- First FDA-approved therapeutic monoclonal antibody for cancer (1997)
- Chimeric human-mouse IgG1; binds type I epitope on EL2
- **ADCC:** FcγRIIIA-mediated; NK cells, macrophages → B cell killing; FcγRIIIA V158F polymorphism → higher affinity → better rituximab response (predictive biomarker)
- **CDC:** C1q binding → classical complement activation → membrane attack complex (MAC) → lysis
- **Direct apoptosis:** Cross-linking of CD20 → mitochondrial pathway apoptosis (less dominant than ADCC/CDC)
- **Phagocytosis (trogocytosis/shaving):** Macrophages strip CD20-antibody complexes from B cell surface → reduces CD20 expression → a resistance mechanism

**Obinutuzumab (GA101, Gazyva):**
- Glycoengineered humanized IgG1; type II binding; bisected, afucosylated Fc → enhanced FcγRIIIA binding → 25-50× greater ADCC vs. rituximab
- Reduced CDC (type II binding, no lipid raft redistribution)
- Greater direct cell death (homotypic adhesion)
- FDA-approved for FL (G-CVP, G-CHOP, G-bendamustine) and CLL (G-chlorambucil, G-venetoclax); some evidence for superiority over rituximab in FL (GALLIUM trial)

**Ofatumumab (Arzerra):**
- Fully human IgG1; binds type I epitope but more proximal on EL2 (includes EL1); high-affinity, slow dissociation → more sustained CDC
- Approved for CLL (now largely superseded by BTK/BCL-2 inhibitors)

**Ocrelizumab (Ocrevus), ofatumumab (Kesimpta), ublituximab (Briumvi):**
- Anti-CD20 mAbs approved for multiple sclerosis; deplete CD20+ B cells → reduce CNS inflammation (B cells as antigen presenters and cytokine producers in MS)

### Rituximab resistance mechanisms

- **CD20 antigen loss:** Downregulation of MS4A1 mRNA (epigenetic silencing, alternative splicing) → CD20-negative clones selected by rituximab pressure; occurs in ~30% of relapsed DLBCL
- **Complement evasion:** Upregulation of complement inhibitory proteins (CD55/DAF, CD59) → MAC protection; seen in CLL
- **FcγRIII downregulation:** Reduced NK cell-mediated ADCC
- **CD20 internalization:** Trogocytosis by FcγRIII+ monocytes → CD20 shaving → reduced surface density for further antibody binding
- **TME immunosuppression:** PD-L1, TGF-beta, IDO → T cell exhaustion → reduced NK/T effector function despite antibody presence

### CD20-targeted bispecific antibodies

**CD20×CD3 bispecific antibodies (approvals, 2022-2023):**
- **Epcoritamab (Epkinly):** Subcutaneous; CD20×CD3; approved for relapsed/refractory DLBCL (3rd-line+); EPITOPHY trial → 39% CR rate; CRS and ICANS management required
- **Glofitamab (Columvi):** IV; fixed-duration (12 cycles); step-up dosing for CRS mitigation; CR 39% in R/R DLBCL; obinutuzumab pre-treatment to reduce CRS
- **Mosunetuzumab (Lunsumio):** Approved for relapsed/refractory FL; fixed duration; CR 60% in FL

CD20×CD3 bispecifics redirect T cells to CD20+ targets — bypassing MHC-I/II restriction and overcoming the CD20-negative escape that limits rituximab; however, CD20 antigen loss is a resistance mechanism for bispecifics as well.

## Connections

- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — CD20 is highly expressed on ABC-DLBCL cells driven by constitutive NF-κB (MYD88 L265P → BTK → NF-κB); rituximab triggers ADCC, CDC, and direct apoptosis in NF-κB-driven B cells; ibrutinib (BTK inhibitor) + rituximab active in MYD88-mutant DLBCL and MCL.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — GCB-DLBCL with t(14;18) → BCL-2 overexpression → apoptosis resistance; rituximab + venetoclax + R-CHOP under study in BCL-2-high DLBCL; double-hit lymphoma (MYC + BCL-2 rearrangement) → venetoclax + dose-adjusted EPOCH-R preferred over R-CHOP.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — MYC rearrangement in ~10% of DLBCL; double-hit (MYC + BCL-2) or triple-hit (+ BCL-6) → high-grade B-cell lymphoma; R-CHOP inferior → EPOCH-R or CAR-T preferred; MYC protein expression >40% is an independent poor-prognosis marker in CD20+ DLBCL.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — B cells co-express CD20 and MHC class II; CD20 downregulation and MHC-II loss are rituximab resistance mechanisms; obinutuzumab reduces CD20 internalization vs. rituximab; CD20×CD3 bispecifics (epcoritamab, glofitamab) bypass MHC-II for T cell-mediated killing.
- `connects-to` → **[NMOSD](../../07-system/nmo/README.md)** — Rituximab (anti-CD20) depletes B cells → reduces AQP4-IgG; widely used off-label as first-line NMOSD prevention (~70-80% ARR reduction); inebilizumab (anti-CD19; N-MOmentum; FDA Jun 2020) is approved for NMOSD; ublituximab under investigation.
- `connects-to` → **[ANCA Vasculitis](../../07-system/anca-vasculitis/README.md)** — Rituximab (anti-CD20) depletes autoreactive B cells in ANCA vasculitis; RAVE trial: rituximab non-inferior to cyclophosphamide for GPA/MPA induction (64% vs 53% CR; FDA Apr 2011); rituximab superior in relapsing disease; MAINRITSAN maintenance reduces relapse.
- `connects-to` → **[Sjögren's Syndrome](../../07-system/sjogrens-syndrome/README.md)** — Rituximab (anti-CD20) depletes B cells in pSS; TEARS/TRACTISS Phase 3 had mixed results on ESSPRI; used off-label for severe extraglandular pSS (cryoglobulinemia, vasculitis, lymphoma); CD20+ ectopic GC B cells in salivary glands drive anti-Ro/SSA production and lymphomagenesis.

[^maloney-1997-rituximab]: Maloney DG, Grillo-López AJ, White CA, et al. IDEC-C2B8 (rituximab) anti-CD20 monoclonal antibody therapy in patients with relapsed low-grade non-Hodgkin's lymphoma. *Blood.* 1997;90(6):2188-2195. [doi:10.1182/blood.V90.6.2188](https://doi.org/10.1182/blood.V90.6.2188) · [PubMed 9310469](https://pubmed.ncbi.nlm.nih.gov/9310469/)
[^coiffier-2002-rchop]: Coiffier B, Lepage E, Brière J, et al. CHOP chemotherapy plus rituximab compared with CHOP alone in elderly patients with diffuse large-B-cell lymphoma. *N Engl J Med.* 2002;346(4):235-242. [doi:10.1056/NEJMoa011795](https://doi.org/10.1056/NEJMoa011795) · [PubMed 11807147](https://pubmed.ncbi.nlm.nih.gov/11807147/)

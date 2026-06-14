---
schema: human-scale-entry/v1
id: cll
name: CLL
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Most common adult leukemia; clonal CD5+/CD19+/CD23+ B-cell malignancy; del(17p)/TP53 mutation is highest-risk. Ibrutinib and venetoclax transformed CLL; obinutuzumab+venetoclax is first-line for unfit patients; pirtobrutinib is active in covalent BTK-inhibitor-resistant CLL."
aliases: ["CLL", "chronic lymphocytic leukemia", "small lymphocytic lymphoma", "SLL", "B-CLL", "CLL/SLL", "del(17p) CLL", "del(11q) CLL"]
sources:
  - id: fischer-2019-clb-cll14
    type: peer-reviewed
    cite: "Fischer K, Al-Sawaf O, Bahlo J, et al. Venetoclax and obinutuzumab in patients with CLL and coexisting conditions. N Engl J Med. 2019;380(23):2225-2236."
    doi: "10.1056/NEJMoa1815281"
    pmid: "31166681"
    url: "https://doi.org/10.1056/NEJMoa1815281"
  - id: shanafelt-2019-ecog-e1912
    type: peer-reviewed
    cite: "Shanafelt TD, Wang XV, Kay NE, et al. Ibrutinib-rituximab or chemoimmunotherapy for chronic lymphocytic leukemia. N Engl J Med. 2019;381(5):432-443."
    doi: "10.1056/NEJMoa1817073"
    pmid: "31365801"
    url: "https://doi.org/10.1056/NEJMoa1815281"
cross_links:
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "BCL-2 overexpression in ~85-90% of CLL via 13q14 deletion (miR-15a/16-1 loss); venetoclax is transformative — CLL14 trial: 57% MRD-undetectable vs. 17% for chlorambucil+obinutuzumab; tumor lysis syndrome risk with initial dosing."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "Del(17p13)/TP53 mutation in ~7% of newly diagnosed CLL and ~30% of relapsed CLL → resistance to chemoimmunotherapy; ibrutinib and venetoclax retain activity in TP53-mutant CLL; del(17p) CLL no longer requires allo-SCT in the targeted therapy era."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "B-cell receptor (BCR) → BTK → PLCγ → PKCβ → NF-κB → BCL-2, MYC, CXCR4 → CLL survival and proliferation; ibrutinib inhibits BTK → blocks BCR-NF-κB → CLL mobilization from lymph nodes (lymphocytosis) and apoptosis; SYK inhibitors (entospletinib) also block BCR upstream of BTK."
  - target: 01-human/03-molecular/atm
    relation: connects-to
    note: "Del(11q22.3)/ATM deletion in ~15-20% of CLL → impaired DDR → bulky adenopathy; del(11q) was high-risk in FCR era; ibrutinib/venetoclax show equal efficacy regardless of del(11q); venetoclax bypasses ATM/TP53 defects by directly engaging mitochondrial apoptosis."
  - target: 01-human/03-molecular/btk
    relation: connects-to
    note: "BTK is the key BCR kinase downstream of LYN/SYK; ibrutinib covalently inhibits BTK at Cys481 → blocks BCR-NF-κB → CLL mobilization and apoptosis; BTK C481S mutation confers covalent BTK inhibitor resistance → switch to non-covalent pirtobrutinib or venetoclax."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "CLL is a clonal CD5+/CD19+/CD23+ B-cell malignancy arising from antigen-experienced B cells; IGHV mutation status (>2% = mutated M-CLL; indolent) is the most important prognostic factor; tonic BCR signaling drives CLL survival; CLL cells home to BM/LN niches via CXCR4/CXCR5."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "CD20 is dimly expressed on CLL cells limiting anti-CD20 antibody efficacy; obinutuzumab (type II, glycoengineered; superior ADCC) + venetoclax (CLL14) achieves 57% MRD-undetectable CR; rituximab + ibrutinib (ECOG E1912) FDA-approved first-line for fit CLL patients."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "CLL accumulates clonal B cells in the bone marrow, where progressive infiltration causes the anemia and thrombocytopenia that mark treatment indication; the marrow and lymph-node niches supply the stromal CD40L and CXCL12 survival signals CLL cells depend on."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Splenomegaly is a common sign and a treatment trigger in CLL: clonal lymphocytes infiltrate the spleen and lymph nodes, and massive or progressive splenomegaly with cytopenias from hypersplenism is one of the Hallek criteria prompting therapy."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Richter transformation is the dreaded complication of CLL — in ~5-10% the indolent clone evolves into aggressive diffuse large B-cell lymphoma, often clonally related, with a poor median survival of about a year; it is even worse when it arises on BTK-inhibitor therapy."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "CLL and its tissue form SLL are a disease of the lymphatic system: clonal mature B cells accumulate in blood, bone marrow and lymph nodes, producing painless generalized lymphadenopathy and splenomegaly; the same cells circulate, so blood counts and nodes reflect one disease."
  - target: 01-human/07-system/mantle-cell-lymphoma
    relation: connects-to
    note: "CLL and mantle cell lymphoma are both CD5-positive mature B-cell neoplasms that can look alike on blood films but differ critically: MCL carries cyclin D1/t(11;14) and is aggressive while CLL is usually indolent—cyclin D1 and SOX11 staining separate them as prognosis diverges."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "CLL is as much an immunodeficiency as a cancer: the malignant B cells suppress normal immunity, causing hypogammaglobulinemia and T-cell dysfunction, so infection is a leading cause of death; CLL also drives autoimmune cytopenias (hemolytic anemia, ITP)."
  - target: 01-human/07-system/cml
    relation: connects-to
    note: "CLL and CML are the two chronic leukemias of opposite lineages: CLL accumulates mature B lymphocytes (smudge cells, often asymptomatic), while CML is a BCR-ABL-driven myeloid proliferation—and where CML is cured by TKIs, CLL uses BTK and BCL-2 inhibitors."
  - target: 01-human/07-system/follicular-lymphoma
    relation: connects-to
    note: "CLL and follicular lymphoma are the commonest indolent B-cell neoplasms but distinct: CLL is a CD5+ small-lymphocyte disease driven by BCL-2 (venetoclax-targeted), while follicular lymphoma is BCL2-translocated and germinal-center-derived—both treatable but incurable."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "CLL famously exhausts cytotoxic T cells, undermining immunity: the leukemic B cells suppress and dysregulate CD8 T cells, causing the immunodeficiency and infection risk that dominate CLL—and this exhaustion is why CAR-T works less well in CLL."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "CLL is a mature B-cell cancer that fails to become a plasma cell: the malignant clone is frozen short of antibody-secreting differentiation, so it accumulates uselessly while normal antibody production falls—causing the hypogammaglobulinemia behind CLL infections."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Hypogammaglobulinemia drives infection risk in CLL: the leukemic B cells crowd out and suppress normal plasma cells, so IgG levels fall and patients suffer recurrent bacterial infections—a leading cause of death, sometimes needing immunoglobulin replacement."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "CLL cripples natural killer and overall immune surveillance: beyond low antibodies, the disease impairs NK and T-cell function, raising infection and second-cancer risk—and this immune dysfunction, not just tumor bulk, shapes the prognosis and treatment of CLL."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "CLL commonly turns the immune system against red cells: autoimmune hemolytic anemia, driven by the dysregulated CLL clone, destroys erythrocytes—so a positive Coombs test and brisk hemolysis are characteristic autoimmune complications of the leukemia."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "PD-1 blockade is studied in CLL, especially Richter transformation: the leukemic microenvironment exhausts T cells via PD-1, so checkpoint inhibition aims to restore anti-tumor immunity where CLL becomes an aggressive large-cell lymphoma."
  - target: 01-human/07-system/immune-thrombocytopenia
    relation: connects-to
    note: "CLL frequently causes immune thrombocytopenia: the disordered clone produces antiplatelet autoantibodies that destroy platelets, so unexplained low platelets in CLL may be autoimmune rather than marrow failure—a distinction that changes treatment."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "CLL's targeted drugs strain the heart: BTK inhibitors like ibrutinib commonly cause atrial fibrillation and hypertension, so cardiac monitoring shapes drug choice—a reminder that even well-tolerated targeted therapy carries organ-specific risk."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "CLL is as much an immune-failure disease as a cancer: the malignant B cells expand regulatory T cells and disarm normal immunity, so infections—not the leukemia itself—are a leading cause of death, and vaccines respond poorly."
  - target: 01-human/07-system/hodgkin-lymphoma
    relation: connects-to
    note: "CLL can transform into aggressive lymphoma (Richter), sometimes of Hodgkin type: a sudden change with rapid nodal growth and B-symptoms signals transformation to Hodgkin or diffuse large B-cell lymphoma, a feared and hard-to-treat turn."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "CLL cells survive inside a protective niche of nurse-like cells: monocyte-derived macrophages in the marrow and lymph nodes shield leukemic B cells from death, so disrupting this microenvironment is a strategy to overcome drug resistance."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "CLL leans on IL-4 for survival: this T-cell cytokine signals leukemic B cells to resist apoptosis and upregulate Bcl-2, part of the external support that keeps these slow-dividing cells alive far longer than they should."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "CLL cells make their own VEGF to stay alive: autocrine VEGF signaling props up anti-apoptotic proteins and feeds the vascular niche in marrow and nodes, adding angiogenesis to the survival tricks behind this indolent leukemia."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "B-cell receptor signaling in CLL runs on calcium: when the receptor fires, BTK and PLC drive a calcium flux that keeps the leukemic cells alive—the very pathway BTK inhibitors interrupt to treat the disease."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "CLL infiltrates the liver as it spreads: leukemic B cells lodge in the liver causing hepatomegaly, part of the organ enlargement that, with big nodes and spleen, marks advancing disease and guides staging."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "CLL cripples dendritic cells and immunity: the leukemia impairs antigen-presenting cell function and broader immune defense, so infections—not the leukemia itself—are a leading cause of death and the reason vaccines respond poorly."
---

# CLL

## Overview

**Chronic lymphocytic leukemia (CLL)** is the most common leukemia in adults in the Western world, characterized by the progressive accumulation of mature, functionally incompetent B lymphocytes (CD5+/CD19+/CD23+/CD20dim) in the blood, bone marrow, and lymphoid organs. CLL and **small lymphocytic lymphoma (SLL)** represent the same biological entity distinguished by the site of predominant involvement (blood/BM vs. lymph node). The disease has a highly variable course: approximately one-third of patients never require treatment, while others progress rapidly and require early intervention. The introduction of **BTK inhibitors (ibrutinib)** and **BCL-2 inhibitors (venetoclax)** has transformed CLL therapy — achieving unprecedented rates of MRD-undetectable remissions and extending survival even in high-risk disease (del17p, TP53-mutant) [^fischer-2019-clb-cll14].

**Epidemiology:**
- ~20,000 new cases/year in the US; median age at diagnosis ~70 years; M:F ~2:1
- Most common adult leukemia in the West; rare in East Asia (genetic/environmental differences)
- 5-year survival: ~83% overall; improving rapidly with targeted therapy
- Familial aggregation: ~10% of CLL patients have a first-degree relative with CLL or related B-cell lymphoproliferative disorder; GWAS identified >40 susceptibility loci

**Indications for treatment (Hallek 2018 criteria):**
- Symptomatic progressive marrow failure (Hgb <10 or plt <100)
- Massive or progressive splenomegaly/lymphadenopathy (>10 cm or rapidly growing)
- Progressive lymphocytosis (>50% increase/2 months or LDT <6 months)
- Autoimmune cytopenia not responsive to corticosteroids
- Constitutional symptoms (>10% weight loss, fatigue, fevers, night sweats)
- NOT: absolute lymphocyte count alone, even if very high

## Structure

### CLL cell biology and immunophenotype

**Immunophenotype (Matutes score ≥3/5 = CLL):**
- CD19+, CD5+, CD23+ (cardinal triad)
- CD20dim (low CD20 expression — key therapeutic implication: anti-CD20 antibodies less effective than in DLBCL)
- FMC7−, CD79b− or dim; sIg dim (kappa or lambda light chain restriction)
- Ki-67 low (<5%): Non-proliferating circulating cells; proliferation occurs in lymph node pseudo-follicles ("proliferation centers")

**CLL cell of origin:** Antigen-experienced B cells (post-germinal center or marginal zone B cells); BCR stereotypy in ~30% of CLL → antigen-driven selection

**IGHV mutation status:**
- **IGHV mutated (M-CLL):** >2% somatic mutations from germline; post-GC B cell; indolent; time to first treatment longer; better OS
- **IGHV unmutated (U-CLL):** <2% somatic mutations; pre-GC B cell; more aggressive; BCR signaling more active; ibrutinib especially effective; U-CLL has higher NF-κB activity

### Prognostic classification

**Binet staging (clinical, Europe):**
- A: <3 lymph node areas; Hgb ≥10, plt ≥100 — favorable
- B: ≥3 lymph node areas; Hgb ≥10, plt ≥100 — intermediate
- C: Hgb <10 or plt <100 — poor (treatment indication)

**Rai staging (clinical, US):**
- 0: Lymphocytosis only → low risk
- I: Lymphocytosis + lymphadenopathy → intermediate
- II: + splenomegaly/hepatomegaly → intermediate
- III: + anemia (Hgb <11) → high risk
- IV: + thrombocytopenia (plt <100) → high risk

**Genomic prognostic factors:**
- **Del(13q14) (~55%):** Most common; miR-15a/miR-16-1 deletion → BCL-2 upregulation; isolated del(13q) = best prognosis
- **Trisomy 12 (~15%):** CD38+, stereotyped BCR; intermediate prognosis; often NOTCH1-mutant
- **Del(11q22.3)/ATM (~15%):** Bulky adenopathy; intermediate-poor in FCR era; equal ibrutinib/venetoclax outcomes
- **Del(17p13.1)/TP53 mutation (~7% newly diagnosed, ~30% relapsed):** Highest risk; no meaningful response to chemoimmunotherapy; requires targeted therapy

**FISH panel standard:** del(13q), trisomy 12, del(11q), del(17p) — performed at diagnosis for staging and treatment planning.

**Recurrent somatic mutations:**
- NOTCH1 (~15%): Trisomy 12-associated; ibrutinib-resistant biology; aggressive
- SF3B1 (~15%): Splicing factor; intermediate risk; del(11q) co-occurrence
- TP53 (see above)
- ATM (~15%)
- BIRC3 (~5%): NF-κB pathway; high-risk in chemotherapy era; ibrutinib active

## Function

### Normal B-cell biology and CLL pathogenesis

**B-cell receptor signaling:**
BCR cross-linking → LYN (SRC kinase) phosphorylates CD79a/b ITAMs → SYK recruitment → PI3Kδ → PDK1 → AKT; BTK (Bruton's tyrosine kinase) → PLCγ2 → IP3/DAG → Ca²⁺ flux/PKC → NF-κB → B-cell activation, proliferation, and survival gene expression (BCL-2, MYC, CXCR4). In CLL, tonic BCR signaling (antigen-independent) sustains this pathway constitutively → ibrutinib exploits this dependency.

**Tumor microenvironment:**
- CLL cells require stromal signals for survival; nurse-like cells (NLCs, CD68+) secrete CXCL12/CXCL13 → CXCR4/CXCR5 on CLL cells → homing to marrow and lymph node niches
- CD4+ T cells provide CD40L → CD40 signaling → CLL proliferation in lymph node pseudo-follicles
- Ibrutinib → reduced CXCR4 expression → CLL mobilization from niches → transient lymphocytosis (not progression)

## Pathology

### Staging and complications

**Complications of CLL:**
- **Autoimmune hemolytic anemia (AIHA, ~10%):** Warm IgG AIHA; treat with corticosteroids (prednisone) → rituximab; ibrutinib may worsen AIHA
- **Immune thrombocytopenia (ITP):** Autoimmune platelet destruction
- **Richter's transformation (~5-10%):** CLL → DLBCL (most common) or Hodgkin lymphoma; DLBCL transformation = poor prognosis (median OS ~1 year); ibrutinib-related Richter's has even worse outcome
- **Hypogammaglobulinemia:** Progressive with disease; IV immunoglobulin (IVIG) if recurrent bacterial infections
- **Infections:** Recurrent bacterial (pneumococcal pneumonia), PCP risk during treatment, CMV reactivation with ibrutinib

### Treatment

**Watch-and-wait:**
- Appropriate for asymptomatic low/intermediate-stage CLL; no survival benefit to early treatment in asymptomatic patients (CLL1, French CLL trial)

**First-line treatment for fit patients (without del17p/TP53mut):**
- **Ibrutinib + rituximab (ECOG-E1912 trial):** [^shanafelt-2019-ecog-e1912] PFS at 3 years 89% vs. 73% vs. FCR; ibrutinib-rituximab superior to FCR in all molecular subgroups; FDA approved 2019
- **Venetoclax + obinutuzumab (CLL14 trial):** [^fischer-2019-clb-cll14] Fixed-duration 12 cycles; MRD-undetectable in 57% of PB; 3-year PFS 81% vs. 49% vs. chlorambucil+obinutuzumab; FDA approved 2019 for unfit patients; increasingly used in fit patients for fixed-duration appeal
- **Acalabrutinib ± obinutuzumab (ELEVATE-TN):** Acalabrutinib (more selective BTK inhibitor) + obinutuzumab PFS 90% at 4 years vs. 47% for chlorambucil+obinutuzumab; fewer cardiac adverse events than ibrutinib (less off-target ITK inhibition → fewer AF events)

**First-line for del(17p)/TP53-mutant:**
- Ibrutinib, acalabrutinib, venetoclax+obinutuzumab — all active; no FCR or BR (alkylating agents/anti-CD20 alone)
- Consider allo-SCT for young fit patients with del(17p) achieving deep remission (decreasing role with targeted therapies)

**Relapsed/refractory:**
- **Venetoclax + rituximab (MURANO trial):** R/R CLL; fixed-duration 2 years; MRD-undetectable 62%; superior to BR; FDA approved 2018
- **BTK C481S mutation (ibrutinib resistance, ~50%):** Cysteine-481 in BTK covalent binding site → ibrutinib cannot covalently bind → resistance; switch to venetoclax; novel non-covalent BTK inhibitors (pirtobrutinib, BRUIN trial → ORR 73% in BTK-inhibitor-resistant CLL) or BTK degraders (ARQ531, BGB-16673) active against C481S
- **Pirtobrutinib (Jaypirca):** Non-covalent BTK inhibitor; FDA approved 2023 for relapsed/refractory CLL after ≥2 lines including BTK inhibitor + BCL-2 inhibitor; ORR 82% in BTK-inhibitor-resistant CLL (BRUIN trial)

**Richter's transformation:**
- R-CHOP ± ibrutinib; CAR-T cells in clinical trials; checkpoint inhibitors (pembrolizumab, nivolumab) for DLBCL transformation; prognosis poor (median OS ~7-12 months)

## Connections

- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — BCL-2 overexpression in ~85-90% of CLL (via 13q14 deletion affecting miR-15a/16-1 which suppress BCL-2); venetoclax (BCL-2 inhibitor) is transformative in CLL — CLL14 trial: 57% MRD-undetectable in PB at end of treatment vs. 17% for chlorambucil+obinutuzumab; tumor lysis syndrome risk in initial dosing.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — Del(17p13)/TP53 mutation in ~7% of treatment-naive CLL, ~30% of relapsed CLL → loss of p53-mediated apoptosis → resistance to alkylating agents and anti-CD20 chemoimmunotherapy; ibrutinib and venetoclax retain activity in TP53-mutant CLL; del(17p) CLL no longer requires allo-SCT with targeted agents.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — B-cell receptor (BCR) → BTK → PLCγ → PKCβ → NF-κB → BCL-2, MYC, CXCR4 → CLL survival and proliferation; ibrutinib inhibits BTK → blocks BCR-NF-κB → CLL mobilization from lymph nodes (lymphocytosis) and apoptosis; SYK inhibitors (entospletinib) also block BCR upstream of BTK.
- `connects-to` → **[ATM](../../03-molecular/atm/README.md)** — ATM deletion at del(11q22.3) in ~15-20% of CLL → impaired DDR → bulky adenopathy; in FCR era, del(11q) was high-risk; ibrutinib/venetoclax show equal efficacy in del(11q) CLL compared to non-del(11q); ATM and TP53 pathway defects are mechanistically distinct — venetoclax bypasses both by directly triggering apoptosis.
- `connects-to` → **[BTK](../../03-molecular/btk/README.md)** — BTK is the key BCR kinase downstream of LYN/SYK; ibrutinib covalently inhibits BTK at Cys481 → blocks BCR-NF-κB → CLL mobilization and apoptosis; BTK C481S mutation confers covalent BTK inhibitor resistance → switch to non-covalent pirtobrutinib or venetoclax.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — CLL is a clonal CD5+/CD19+/CD23+ B-cell malignancy arising from antigen-experienced B cells; IGHV mutation status (>2% = mutated M-CLL; indolent) is the most important prognostic factor; tonic BCR signaling drives CLL survival; CLL cells home to BM/LN niches via CXCR4/CXCR5.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — CD20 is dimly expressed on CLL cells limiting anti-CD20 antibody efficacy; obinutuzumab (type II, glycoengineered; superior ADCC) + venetoclax (CLL14) achieves 57% MRD-undetectable CR; rituximab + ibrutinib (ECOG E1912) FDA-approved first-line for fit CLL patients.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — CLL accumulates clonal B cells in the bone marrow, where progressive infiltration causes the anemia and thrombocytopenia that mark treatment indication; the marrow and lymph-node niches supply the stromal CD40L and CXCL12 survival signals CLL cells depend on.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Splenomegaly is a common sign and a treatment trigger in CLL: clonal lymphocytes infiltrate the spleen and lymph nodes, and massive or progressive splenomegaly with cytopenias from hypersplenism is one of the Hallek criteria prompting therapy.
- `connects-to` → **[Diffuse Large B-Cell Lymphoma](../dlbcl/README.md)** — Richter transformation is the dreaded complication of CLL — in ~5-10% the indolent clone evolves into aggressive diffuse large B-cell lymphoma, often clonally related, with a poor median survival of about a year; it is even worse when it arises on BTK-inhibitor therapy.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — CLL and its tissue form SLL are a disease of the lymphatic system: clonal mature B cells accumulate in blood, bone marrow and lymph nodes, producing painless generalized lymphadenopathy and splenomegaly; the same cells circulate, so blood counts and nodes reflect one disease.
- `connects-to` → **[Mantle Cell Lymphoma](../mantle-cell-lymphoma/README.md)** — CLL and mantle cell lymphoma are both CD5-positive mature B-cell neoplasms that can look alike on blood films but differ critically: MCL carries cyclin D1/t(11;14) and is aggressive while CLL is usually indolent—cyclin D1 and SOX11 staining separate them as prognosis diverges.
- `connects-to` → **[Immune System](../immune-system/README.md)** — CLL is as much an immunodeficiency as a cancer: the malignant B cells suppress normal immunity, causing hypogammaglobulinemia and T-cell dysfunction, so infection is a leading cause of death; CLL also drives autoimmune cytopenias (hemolytic anemia, ITP).
- `connects-to` → **[Chronic Myeloid Leukemia](../cml/README.md)** — CLL and CML are the two chronic leukemias of opposite lineages: CLL accumulates mature B lymphocytes (smudge cells, often asymptomatic), while CML is a BCR-ABL-driven myeloid proliferation—and where CML is cured by TKIs, CLL uses BTK and BCL-2 inhibitors.
- `connects-to` → **[Follicular Lymphoma](../follicular-lymphoma/README.md)** — CLL and follicular lymphoma are the commonest indolent B-cell neoplasms but distinct: CLL is a CD5+ small-lymphocyte disease driven by BCL-2 (venetoclax-targeted), while follicular lymphoma is BCL2-translocated and germinal-center-derived—both treatable but incurable.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — CLL famously exhausts cytotoxic T cells, undermining immunity: the leukemic B cells suppress and dysregulate CD8 T cells, causing the immunodeficiency and infection risk that dominate CLL—and this exhaustion is why CAR-T works less well in CLL.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — CLL is a mature B-cell cancer that fails to become a plasma cell: the malignant clone is frozen short of antibody-secreting differentiation, so it accumulates uselessly while normal antibody production falls—causing the hypogammaglobulinemia behind CLL infections.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Hypogammaglobulinemia drives infection risk in CLL: the leukemic B cells crowd out and suppress normal plasma cells, so IgG levels fall and patients suffer recurrent bacterial infections—a leading cause of death, sometimes needing immunoglobulin replacement.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — CLL cripples natural killer and overall immune surveillance: beyond low antibodies, the disease impairs NK and T-cell function, raising infection and second-cancer risk—and this immune dysfunction, not just tumor bulk, shapes the prognosis and treatment of CLL.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — CLL commonly turns the immune system against red cells: autoimmune hemolytic anemia, driven by the dysregulated CLL clone, destroys erythrocytes—so a positive Coombs test and brisk hemolysis are characteristic autoimmune complications of the leukemia.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — PD-1 blockade is studied in CLL, especially Richter transformation: the leukemic microenvironment exhausts T cells via PD-1, so checkpoint inhibition aims to restore anti-tumor immunity where CLL becomes an aggressive large-cell lymphoma.
- `connects-to` → **[Immune Thrombocytopenia](../immune-thrombocytopenia/README.md)** — CLL frequently causes immune thrombocytopenia: the disordered clone produces antiplatelet autoantibodies that destroy platelets, so unexplained low platelets in CLL may be autoimmune rather than marrow failure—a distinction that changes treatment.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — CLL's targeted drugs strain the heart: BTK inhibitors like ibrutinib commonly cause atrial fibrillation and hypertension, so cardiac monitoring shapes drug choice—a reminder that even well-tolerated targeted therapy carries organ-specific risk.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — CLL is as much an immune-failure disease as a cancer: the malignant B cells expand regulatory T cells and disarm normal immunity, so infections—not the leukemia itself—are a leading cause of death, and vaccines respond poorly.
- `connects-to` → **[Hodgkin Lymphoma](../hodgkin-lymphoma/README.md)** — CLL can transform into aggressive lymphoma (Richter), sometimes of Hodgkin type: a sudden change with rapid nodal growth and B-symptoms signals transformation to Hodgkin or diffuse large B-cell lymphoma, a feared and hard-to-treat turn.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — CLL cells survive inside a protective niche of nurse-like cells: monocyte-derived macrophages in the marrow and lymph nodes shield leukemic B cells from death, so disrupting this microenvironment is a strategy to overcome drug resistance.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — CLL leans on IL-4 for survival: this T-cell cytokine signals leukemic B cells to resist apoptosis and upregulate Bcl-2, part of the external support that keeps these slow-dividing cells alive far longer than they should.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — CLL cells make their own VEGF to stay alive: autocrine VEGF signaling props up anti-apoptotic proteins and feeds the vascular niche in marrow and nodes, adding angiogenesis to the survival tricks behind this indolent leukemia.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — B-cell receptor signaling in CLL runs on calcium: when the receptor fires, BTK and PLC drive a calcium flux that keeps the leukemic cells alive—the very pathway BTK inhibitors interrupt to treat the disease.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — CLL infiltrates the liver as it spreads: leukemic B cells lodge in the liver causing hepatomegaly, part of the organ enlargement that, with big nodes and spleen, marks advancing disease and guides staging.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — CLL cripples dendritic cells and immunity: the leukemia impairs antigen-presenting cell function and broader immune defense, so infections—not the leukemia itself—are a leading cause of death and the reason vaccines respond poorly.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^fischer-2019-clb-cll14]: Fischer K, Al-Sawaf O, Bahlo J, et al. Venetoclax and obinutuzumab in patients with CLL and coexisting conditions. *N Engl J Med.* 2019;380(23):2225-2236. [doi:10.1056/NEJMoa1815281](https://doi.org/10.1056/NEJMoa1815281) · [PubMed 31166681](https://pubmed.ncbi.nlm.nih.gov/31166681/)
[^shanafelt-2019-ecog-e1912]: Shanafelt TD, Wang XV, Kay NE, et al. Ibrutinib-rituximab or chemoimmunotherapy for chronic lymphocytic leukemia. *N Engl J Med.* 2019;381(5):432-443. [doi:10.1056/NEJMoa1817073](https://doi.org/10.1056/NEJMoa1817073) · [PubMed 31365801](https://pubmed.ncbi.nlm.nih.gov/31365801/)

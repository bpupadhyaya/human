---
schema: medicine-entry/v1
id: car-t
name: CAR-T Cell Therapy
atlas: 03-medicine
scale: 01-modern
status: draft
last_reviewed: 2026-06-06
summary: "Patient T cells engineered ex vivo with chimeric antigen receptor (scFv + transmembrane + CD3ζ + costimulatory domain) targeting tumor antigens (CD19, BCMA). FDA-approved 2017. Major AEs: cytokine release syndrome, neurotoxicity (ICANS)."
aliases: ["CAR-T", "chimeric antigen receptor T cell", "adoptive T cell therapy", "anti-CD19 CAR-T", "tisagenlecleucel", "axicabtagene ciloleucel", "Kymriah", "Yescarta"]
drug_class: adoptive cell therapy
modality: cellular immunotherapy
key_agents:
  - tisagenlecleucel (Kymriah) — CD19-directed, CD137/4-1BB costimulatory domain
  - axicabtagene ciloleucel (Yescarta) — CD19-directed, CD28 costimulatory domain
  - ciltacabtagene autoleucel (Carvykti) — BCMA-directed (multiple myeloma)
  - idecabtagene vicleucel (Abecma) — BCMA-directed (multiple myeloma)
sources:
  - id: porter-2011-car-t
    type: peer-reviewed
    cite: "Porter DL, Levine BL, Kalos M, Bagg A, June CH. Chimeric antigen receptor-modified T cells in chronic lymphoid leukemia. N Engl J Med. 2011;365(8):725-33."
    doi: "10.1056/NEJMoa1103849"
    pmid: "21830940"
    url: "https://doi.org/10.1056/NEJMoa1103849"
  - id: maude-2018-cart-all
    type: peer-reviewed
    cite: "Maude SL, Laetsch TW, Buechner J, et al. Tisagenlecleucel in children and young adults with B-cell lymphoblastic leukemia. N Engl J Med. 2018;378(5):439-48."
    doi: "10.1056/NEJMoa1709866"
    pmid: "29385370"
    url: "https://doi.org/10.1056/NEJMoa1709866"
  - id: neelapu-2017-axi-cel
    type: peer-reviewed
    cite: "Neelapu SS, Locke FL, Bartlett NL, et al. Axicabtagene ciloleucel CAR T-cell therapy in refractory large B-cell lymphoma. N Engl J Med. 2017;377(26):2531-44."
    doi: "10.1056/NEJMoa1707447"
    pmid: "29226797"
    url: "https://doi.org/10.1056/NEJMoa1707447"
cross_links:
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: modulates
    evidence: porter-2011-car-t
    note: "CAR-T therapy re-engineers autologous CD8+ (and CD4+) T cells with chimeric antigen receptors; the infused CAR-T cells expand massively, recognize tumor antigen in an MHC-independent manner, and kill via perforin/granzyme and Fas/FasL — the same mechanisms as native CTLs."
  - target: 01-human/04-cellular/b-cell
    relation: targets
    evidence: maude-2018-cart-all
    note: "CD19-directed CAR-T cells target all CD19-expressing cells, including malignant B-ALL blasts and normal B lymphocytes; prolonged B cell aplasia is an expected on-target off-tumour toxicity managed with IVIG supplementation."
  - target: 01-human/03-molecular/il-6
    relation: modulates
    evidence: neelapu-2017-axi-cel
    note: "Cytokine release syndrome (CRS) — the major acute CAR-T toxicity — is driven by massive IL-6 (and IFN-γ, TNF-α) secretion from activated CAR-T cells and bystander immune cells; tocilizumab (anti-IL-6R) is first-line treatment for grade ≥2 CRS."
  - target: 01-human/07-system/immune-system
    relation: modulates
    evidence: maude-2018-cart-all
    note: "Lymphodepleting conditioning chemotherapy (fludarabine + cyclophosphamide) is administered before CAR-T infusion to create cytokine space and reduce immunosuppressive regulatory cell populations, enhancing CAR-T engraftment and expansion."
---

# CAR-T Cell Therapy

## Overview

Chimeric Antigen Receptor T cell therapy (CAR-T) is an **adoptive cellular immunotherapy** in which a patient's own T cells are genetically engineered ex vivo to express a synthetic receptor that redirects cytotoxic killing toward tumor cells expressing a specific surface antigen. CAR-T represents the convergence of gene therapy, immunology, and synthetic biology — and the first therapeutic approach capable of achieving durable complete remissions in heavily pretreated, refractory hematologic malignancies that were uniformly fatal before 2017.

The clinical breakthrough came with the landmark Porter et al. case report (NEJM 2011) [^porter-2011-car-t], describing a complete sustained remission in a patient with relapsed/refractory CLL using anti-CD19 CAR-T cells developed by Carl June's group at the University of Pennsylvania. This proof-of-concept stimulated broad clinical development leading to the **first FDA approvals in August 2017**: tisagenlecleucel (Kymriah; Novartis) for pediatric B-ALL and axicabtagene ciloleucel (Yescarta; Kite/Gilead) for adult relapsed/refractory diffuse large B-cell lymphoma (DLBCL).

As of 2026, six CAR-T products are FDA-approved targeting CD19 (B-ALL, DLBCL, follicular lymphoma, mantle cell lymphoma) or BCMA (multiple myeloma). Clinical development is active across solid tumors (GD2, EGFR, HER2, mesothelin targets) and T cell malignancies.

## Mechanism

### CAR Construct Architecture

The chimeric antigen receptor is a **synthetic transmembrane protein** integrating four functional modules:

| Module | Component | Function |
|:---|:---|:---|
| **Extracellular binding domain** | Single-chain variable fragment (scFv) — VH + VL domains of anti-tumor antibody linked by flexible Gly4Ser linker | Antigen recognition; MHC-independent binding to surface antigen |
| **Hinge/spacer** | IgG4 CH2-CH3 or CD8α hinge | Positions scFv at optimal distance from target cell membrane |
| **Transmembrane domain** | CD28 or CD8α transmembrane helix | Anchors CAR in T cell membrane; can influence signaling |
| **Intracellular signaling** | CD3ζ (zeta) chain ITAMs (3 ITAMs) + costimulatory domain (CD28 or 4-1BB/CD137) | Provides Signal 1 (CD3ζ → ZAP-70) and Signal 2 (co-stimulation → PI3K/Akt/mTOR) within one protein — bypassing MHC-TCR requirement |

**CAR generation evolution:**
- **1st generation:** scFv + CD3ζ only (poor expansion, no memory, early clinical failures)
- **2nd generation (current standard):** scFv + one costimulatory domain (CD28 *or* 4-1BB) + CD3ζ → dramatically improved persistence and efficacy
- **3rd generation:** scFv + two costimulatory domains (CD28 + 4-1BB) + CD3ζ → increased activation, investigated in trials
- **4th generation ("TRUCK" — T cells Redirected for Universal Cytokine Killing):** CAR + inducible cytokine payload (IL-12, IL-15) released in tumour microenvironment → armour-plate for solid tumour immunosuppression

### The CD28 vs. 4-1BB Costimulatory Domain Difference

| Feature | CD28 domain (e.g., Yescarta) | 4-1BB domain (e.g., Kymriah) |
|:---|:---|:---|
| **Expansion kinetics** | Faster, peak earlier | Slower, more sustained |
| **Effector vs. memory bias** | More effector T_eff | More memory T_CM phenotype |
| **Persistence** | Shorter | Longer |
| **CRS severity** | Generally more severe | Generally less severe |
| **Glucose metabolism** | Warburg glycolysis | Mitochondrial oxidative phosphorylation |

### Manufacturing Process

1. **Leukapheresis:** Patient T cells collected by apheresis (typically 3–5 × 10⁹ T cells)
2. **T cell activation:** Anti-CD3/CD28 beads or soluble reagents activate T cells ex vivo
3. **Viral transduction:** Retroviral or lentiviral vector (encoding CAR transgene) transduces activated T cells; transgene integrates stably into host chromatin (semi-random integration — occasionally into proto-oncogene — safety monitoring required)
4. **Expansion:** Transduced T cells expanded in bioreactor to ~10⁸–10⁹ CAR+ T cells over 10–14 days
5. **Formulation, QC, cryopreservation:** Cell viability, transduction efficiency, sterility, and identity testing; frozen in infusion bags shipped to treating centre
6. **Lymphodepleting conditioning:** Patient receives fludarabine + cyclophosphamide 3–5 days before infusion — depletes regulatory T cells and creates cytokine space (↑ IL-7, IL-15) for CAR-T engraftment
7. **Infusion and monitoring:** Single IV infusion; patient monitored in hospital for CRS and ICANS (often 7–14 days)

## Clinical Use

### FDA-Approved Indications (Selected)

| Product | Target | Indication | Key Response Data |
|:---|:---|:---|:---|
| **Tisagenlecleucel (Kymriah)** | CD19 / 4-1BB | Pediatric/young adult B-ALL (≤25 y, R/R) | 81% complete remission at 3 months [^maude-2018-cart-all] |
| **Axicabtagene ciloleucel (Yescarta)** | CD19 / CD28 | R/R large B-cell lymphoma | 54% objective response; 40% complete response [^neelapu-2017-axi-cel] |
| **Lisocabtagene maraleucel (Breyanzi)** | CD19 / 4-1BB | R/R large B-cell lymphoma | 73% ORR; 53% CR |
| **Ciltacabtagene autoleucel (Carvykti)** | BCMA / 4-1BB | R/R multiple myeloma (≥4 prior lines) | 97% ORR; 79% ≥CR (CARTITUDE-1) |
| **Idecabtagene vicleucel (Abecma)** | BCMA / 4-1BB | R/R multiple myeloma (≥4 prior lines) | 73% ORR; 33% CR (KarMMa) |

### Adverse Effects

**Cytokine Release Syndrome (CRS):**
- Occurs in ~50–90% of patients (severity varies by product, indication, and tumour burden)
- Mechanism: Massive CAR-T activation releases IFN-γ, IL-6, TNF-α; bystander macrophage activation amplifies cytokine storm (particularly IL-6)
- Grading: CRS grade 1 (fever only) → grade 4 (life-threatening vasodilatory shock, respiratory failure)
- Management: Antipyretics; **tocilizumab** (IL-6R blockade) for grade ≥2 CRS; corticosteroids for refractory cases
- Severe CRS requires ICU with vasopressor support

**Immune Effector Cell-Associated Neurotoxicity Syndrome (ICANS):**
- Occurs in ~20–60% of patients (typically 4–14 days post-infusion, sometimes overlapping with CRS)
- Mechanism: Breakdown of blood-brain barrier during cytokine storm; CAR-T cell infiltration of CNS; high IL-6, IL-1 in CSF
- Manifestations: aphasia, confusion, tremor, headache; severe: seizures, raised intracranial pressure, cerebral oedema
- Management: Corticosteroids (dexamethasone); levetiracetam prophylaxis; ICU for severe ICANS; tocilizumab is contraindicated in severe ICANS (may worsen neurological outcomes)

**B-cell aplasia:** On-target off-tumour toxicity from CD19-CAR-T; all normal CD19+ B cells are eliminated → prolonged hypogammaglobulinaemia; requires monthly IVIG supplementation; expected and acceptable given the malignant target

**Prolonged cytopenia:** From lymphodepleting conditioning; can be severe and prolonged in some patients

**CAR-T failure modes:** Primary non-response (~20–30%); early relapse due to antigen loss (CD19-negative relapse) or CAR-T exhaustion; antigen-low escape

## Evidence

### Tisagenlecleucel in Pediatric B-ALL (ELIANA Trial)

Maude et al. [^maude-2018-cart-all] — Phase 2, single-arm, global trial in 75 pediatric/young adult patients with R/R B-ALL:

- **Overall remission rate: 81%** (complete remission + complete remission with incomplete count recovery)
- **12-month event-free survival: 50%** (12-month OS: 76%)
- **CRS:** 77% of patients (47% grade 3–4); median time to CRS resolution 8 days
- **Neurotoxicity:** 40% (13% grade 3–4)
- **B cell aplasia:** Maintained in all responders at 3 months — proof of in vivo persistence
- Based on this trial, FDA granted **accelerated approval August 30, 2017** — the first CAR-T product approved

### Axicabtagene Ciloleucel in DLBCL (ZUMA-1 Trial)

Neelapu et al. [^neelapu-2017-axi-cel] — Phase 1/2 in 101 patients with R/R large B-cell lymphoma:

- **Objective response rate: 82%** (54% complete response)
- **2-year OS: 50.5%** — extraordinary in a disease where standard salvage chemotherapy achieves <10% CR
- **Grade ≥3 CRS: 13%;** grade ≥3 neurological events: 28%
- Established CAR-T as standard of care in R/R DLBCL, replacing autologous stem cell transplant in this setting

## Connections

- **Modulates** → [Cytotoxic T Cell](../../../../01-human/04-cellular/t-cytotoxic-cell/README.md): CAR-T therapy re-engineers autologous CD8+ T cells; infused cells expand massively and kill tumour cells via perforin/granzyme in an MHC-independent manner, equivalent to but redirected from native CTL function.
- **Targets** → [B Cell](../../../../01-human/04-cellular/b-cell/README.md): CD19-directed CAR-T eliminates all CD19-expressing B cells — both malignant B-ALL blasts and normal B lymphocytes; B-cell aplasia is an expected on-target toxicity confirming CAR-T activity.
- **Modulates** → [Interleukin-6](../../../../01-human/03-molecular/il-6/README.md): Cytokine release syndrome is IL-6-dominated; massively elevated IL-6 drives fever, hypotension, and end-organ dysfunction; tocilizumab (anti-IL-6R) is first-line CRS treatment.
- **Modulates** → [Immune System](../../../../01-human/07-system/immune-system/README.md): Lymphodepleting conditioning (fludarabine + cyclophosphamide) precedes infusion to eliminate immunosuppressive regulatory cells and create homeostatic space (elevated IL-7/IL-15) for CAR-T expansion.

[^porter-2011-car-t]: Porter DL, Levine BL, Kalos M, Bagg A, June CH. Chimeric antigen receptor-modified T cells in chronic lymphoid leukemia. *N Engl J Med.* 2011;365(8):725-33. [doi:10.1056/NEJMoa1103849](https://doi.org/10.1056/NEJMoa1103849) · [PubMed 21830940](https://pubmed.ncbi.nlm.nih.gov/21830940/)
[^maude-2018-cart-all]: Maude SL, Laetsch TW, Buechner J, et al. Tisagenlecleucel in children and young adults with B-cell lymphoblastic leukemia. *N Engl J Med.* 2018;378(5):439-48. [doi:10.1056/NEJMoa1709866](https://doi.org/10.1056/NEJMoa1709866) · [PubMed 29385370](https://pubmed.ncbi.nlm.nih.gov/29385370/)
[^neelapu-2017-axi-cel]: Neelapu SS, Locke FL, Bartlett NL, et al. Axicabtagene ciloleucel CAR T-cell therapy in refractory large B-cell lymphoma. *N Engl J Med.* 2017;377(26):2531-44. [doi:10.1056/NEJMoa1707447](https://doi.org/10.1056/NEJMoa1707447) · [PubMed 29226797](https://pubmed.ncbi.nlm.nih.gov/29226797/)

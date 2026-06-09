---
schema: human-scale-entry/v1
id: aplastic-anemia
name: Aplastic Anemia
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Aplastic anemia (AA) is a bone marrow failure syndrome; autoreactive CD8+ T cells destroy HSCs via perforin/granzyme → pancytopenia. SAA: ANC <500/µL, plt <20,000/µL, reticulocytes <20,000/µL. Treatment: HSCT (young, matched donor) or ATG + cyclosporine + eltrombopag."
aliases: ["AA", "aplastic anaemia", "severe aplastic anemia", "SAA", "very severe aplastic anemia", "VSAA", "bone marrow failure"]
sources:
  - id: young-2018-aplastic-anemia-review
    type: peer-reviewed
    cite: "Young NS. Aplastic Anemia. N Engl J Med. 2018;379(17):1643-1656."
    doi: "10.1056/NEJMra1413485"
    pmid: "30354959"
    url: "https://doi.org/10.1056/NEJMra1413485"
  - id: townsley-2017-eltrombopag-aa
    type: peer-reviewed
    cite: "Townsley DM, Scheinberg P, Winkler T, et al. Eltrombopag Added to Standard Immunosuppression for Aplastic Anemia. N Engl J Med. 2017;376(16):1540-1550."
    doi: "10.1056/NEJMoa1613878"
    pmid: "28423296"
    url: "https://doi.org/10.1056/NEJMoa1613878"
cross_links:
  - target: 01-human/05-tissue/bone-marrow
    relation: targets
    note: "AA results from T cell-mediated HSC destruction → hypocellular marrow (<25% cellularity) replaced by fat; 25-40% of AA patients have PNH clones (AA-PNH overlap continuum); marrow biopsy showing fat-replaced hypocellular marrow is the diagnostic hallmark."
  - target: 01-human/07-system/pnh
    relation: connects-to
    note: "AA and PNH are closely related: immune destruction of normal HSCs in AA allows PIGA-mutant GPI-deficient clone to expand; 25-40% of AA patients have PNH clones at diagnosis; some AA patients evolve to overt PNH; both conditions are treated at specialized hemato-oncology centers."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "In aplastic anemia, autoreactive CTL target HSCs via perforin/granzyme-mediated cytotoxicity; elevated perforin+ CD8+ T cells in AA bone marrow predict treatment response; cyclosporine + anti-thymocyte globulin (ATG) reduce autoreactive CTL activity and restore hematopoiesis."
  - target: 01-human/03-molecular/thrombopoietin
    relation: connects-to
    note: "In severe AA, HSC destruction → thrombocytopenia; elevated TPO cannot drive production from depleted marrow; eltrombopag added to hATG+CsA (triple IST) improves overall response and may expand HSCs via c-Mpl beyond megakaryopoiesis."
---

# Aplastic Anemia

## Overview

**Aplastic anemia (AA)** is a potentially life-threatening **bone marrow failure syndrome** characterized by **hypocellular bone marrow** and **peripheral blood pancytopenia** (anemia, neutropenia, thrombocytopenia), resulting from destruction or failure of hematopoietic stem cells (HSCs) [^young-2018-aplastic-anemia-review].

In >80% of acquired AA cases, the disease is **immune-mediated**: autoreactive **CD8+ cytotoxic T lymphocytes** (CTL), oligoclonally expanded against unknown HSC antigens, destroy HSCs via **perforin/granzyme-B-mediated cytotoxicity** and Fas-FasL interactions. IFN-γ from activated T cells further suppresses HSC proliferation via STAT1 → ↑FasL expression on HSCs → HSC apoptosis. Tregs are quantitatively and functionally deficient in AA — implicating a breakdown in immune self-tolerance.

**Incidence:** 2-3 cases/100,000/year in Western countries; 5-7/100,000 in East Asia (higher in Asia for unknown reasons — possibly environmental/viral triggers); peak ages: 10-25 years and >60 years (bimodal distribution); equal sex distribution.

**Causes:**
- **Acquired idiopathic (most common, ~80%):** Immune-mediated; preceding viral infection (EBV, parvovirus B19, hepatitis-associated AA after NANB hepatitis), drugs, or no identifiable trigger
- **Drug-induced:** Chloramphenicol (classic), carbamazepine, methimazole, gold, NSAIDs — idiosyncratic reactions; not dose-dependent
- **Inherited bone marrow failure syndromes:** Fanconi anemia (FANC gene family, chromosomal fragility; risk of MDS/AML), dyskeratosis congenita (telomere biology genes: TERT, TERC, DKC1; mucocutaneous triad), Diamond-Blackfan anemia (RPS/RPL ribosomal protein mutations), Shwachman-Diamond syndrome (SBDS)
- **PNH clone expansion:** 25-40% of AA patients have GPI-deficient (PIGA-mutant) clones on FLAER flow; AA and PNH share immune-mediated pathophysiology

## Structure

### Diagnostic criteria and severity classification

**Diagnosis:**
- **Bone marrow biopsy:** Hypocellular marrow (<25-30% cellularity); fat-replaced with few residual hematopoietic cells; empty sinusoids; no evidence of malignant infiltration (rules out hypoplastic MDS, aleukemic leukemia)
- **Peripheral blood:** Pancytopenia — reticulocytopenia (reticulocyte count <20,000/µL or <1%); no or few blasts; target cells from iron deficiency
- **Cytogenetics:** Normal karyotype (vs. hypoplastic MDS which often has cytogenetic abnormalities — monosomy 7 most common)
- **Telomere length:** Short telomeres suggest constitutional telomere disorders (dyskeratosis congenita); tested by flow-FISH or qPCR; actionable as it contraindicates standard ATG (poor response; prefer androgens/danazol + HSCT from matched sibling)

**Severity classification (Camitta criteria, modified):**

| Category | ANC | Platelets | Reticulocytes | Marrow |
|:---|:---|:---|:---|:---|
| **Severe AA (SAA)** | <500/µL | <20,000/µL | <20,000/µL | <25% cellularity |
| **Very Severe AA (VSAA)** | <200/µL | <20,000/µL | <20,000/µL | <25% cellularity |
| **Moderate AA** | 500-2000/µL | 20,000-100,000/µL | — | >25% cellularity |

**VSAA** = SAA criteria + ANC <200/µL; higher risk of early mortality from infections

### Molecular mechanism

**T cell-mediated HSC destruction:**
1. Unknown antigen (possibly cryptic HSC antigen revealed by viral infection or drug metabolite) → Th1-skewed oligoclonal T cell expansion; T cell receptor (TCR) Vβ skewing (increased frequency of specific Vβ chains) documented in AA
2. Autoreactive CD8+ CTL overexpressing IFN-γ, TNF-α, and **perforin** infiltrate the bone marrow
3. **Perforin/granzyme pathway:** CTL form immunological synapse with HSC → perforin pores → granzyme B → Bid cleavage → MOMP → caspase-9/3 → HSC apoptosis
4. **Fas-FasL pathway:** IFN-γ → ↑FasL on T cells → HSC Fas → caspase-8/3 cascade
5. **IFN-γ direct suppression:** STAT1 → ↑p21/WAF1 (CDK inhibitor) → HSC cell cycle arrest; ↑Fas on HSCs → increased susceptibility to FasL-mediated killing
6. **Treg deficiency:** Quantitatively reduced Foxp3+ CD4+CD25+ Tregs in AA; impaired IL-10/TGF-β suppression of autoreactive CTL → unchecked T cell attack

**PNH clone selection mechanism:**
- In AA, immune destruction selectively kills GPI-anchor expressing HSCs (normal HSCs) because GPI-anchored proteins include immune escape signals; PIGA-null (GPI-deficient) HSCs escape immune attack → selective expansion → PNH clone
- Explains the frequent co-occurrence of AA + PNH clones and the progression from AA to PNH in some patients

## Function

### Treatment

**First-line — Allogeneic HSCT (preferred for young patients with matched sibling donor):**
- Age ≤40 years + SAA/VSAA + matched sibling donor (MSD) → HSCT is first-line therapy
- Conditioning: Cyclophosphamide (Cy) + ATG (or fludarabine-based reduced-intensity for older patients); prevents rejection of donor graft
- **5-year OS: >80-85%** with MSD HSCT in young patients (National Registry data)
- Graft failure (primary or secondary): 5-15% with sibling donors; treat with second HSCT or immunosuppression
- MUD (matched unrelated donor) HSCT: Acceptable second-line if ATG fails; 5-year OS ~70-75% in young patients; GvHD risk higher than MSD

**First-line for older patients or no MSD — Immunosuppressive therapy (IST):**

**ATG (anti-thymocyte globulin) + cyclosporine ± eltrombopag:**
- **Horse ATG (hATG; ATGAM; Pfizer):** 40 mg/kg/day × 4 days IV; polyclonal antibody depletes T cells; hATG superior to rabbit ATG (rATG) for AA in a NEJM-published head-to-head trial (response rate 68% vs. 37% at 6 months)
- **Cyclosporine A (CsA):** 10-12 mg/kg/day divided BID; calcineurin inhibitor → ↓IL-2 → blocks T cell activation; maintained for 12-24 months to prevent relapse; monitor trough levels (target 150-250 ng/mL)
- **Eltrombopag (EPAG; thrombopoietin receptor agonist):** Added to hATG + CsA → triple IST [^townsley-2017-eltrombopag-aa]

**EPAG-ATG-CsA triple IST (NIH trial) [^townsley-2017-eltrombopag-aa]:**
- EPAG 150 mg QD (titrated to 300 mg if no response by day 14) started on day 14 of ATG
- **Complete response rate at 6 months: 33% (triple IST) vs. 10% (ATG + CsA alone)**; overall response 80% vs. 51%
- **FDA approval: 2018** for refractory/relapsed SAA; 2022 for first-line SAA in combination with ATG
- Mechanism of EPAG in AA: TPO-R agonism → HSC expansion (c-Mpl on HSCs) + direct stimulation of multilineage hematopoietic progenitor proliferation; also proposed immune modulatory effects
- EPAG adverse effects: LFT elevation (monitor); thrombosis rare in AA (thrombocytopenic patients); cytogenetic abnormalities (chromosome 7 abnormalities): 7-8% at 24 months — monitor karyotype every 3 months

**Relapsed/refractory AA:**
- **Ruxolitinib + eltrombopag:** JAK1/2 inhibition + TPO-R; investigational in refractory AA; ORR ~60%
- **Avacopan (C5aR inhibitor) + eltrombopag:** Phase 2 (complement activation in AA refractory to ATG)
- **HSCT from matched unrelated donor (MUD):** After ≥1 ATG failure; 10/10 MUD or haploidentical + PT-Cy
- **Androgens (danazol):** Second-line; ↑telomerase (TERT) → HSC survival; useful in telomeropathies; hepatotoxic

### Differential diagnosis (critical distinctions)

| Condition | Key differentiator |
|:---|:---|
| **Hypoplastic MDS** | Cytogenetic abnormalities (monosomy 7, del5q); dysplasia on marrow biopsy; older patients |
| **PNH** | FLAER+ GPI-deficient clone >10%; hemolysis (high LDH, low haptoglobin) |
| **Acute leukemia (hypocellular)** | Blasts >5% on marrow biopsy; lymphoblasts in ALL |
| **Fanconi anemia** | Chromosomal fragility (MMC/DEB test); FANC gene panel; congenital anomalies |
| **Dyskeratosis congenita** | Mucocutaneous triad (nail dystrophy, leukoplakia, reticulate pigmentation); short telomeres |

## Pathology

**Clonal evolution:**
- 10-15% of AA patients develop clonal complications: MDS (most common), AML, or PNH evolution
- Risk factors: prior IST (ATG-selected clonal advantage); cytogenetic abnormalities at diagnosis (chromosome 7 monosomy → high MDS/AML risk); very long disease duration
- Monitor: karyotype and FLAER flow every 6-12 months

**Infections:**
- Severe neutropenia → risk of invasive fungal infections (Aspergillus, Candida) and gram-negative bacteremia; prophylaxis: fluconazole/posaconazole; antimicrobials at first fever
- Empiric antifungal coverage during ATG treatment (immunosuppression + neutropenia)
- CMV reactivation in IST: monitor weekly PCR; treat with valganciclovir

**Graft failure after HSCT:**
- Primary graft failure (no engraftment): 5-15% with sibling donor; higher with MUD; treat with second HSCT
- Secondary graft failure (initial engraftment then decline): Rejection by host T cells; reduced-intensity re-conditioning + second graft

**Transfusion iron overload:**
- Chronically transfused AA patients accumulate iron (no physiological iron excretion); ferritin >2,500 ng/mL → iron chelation (deferasirox); oral chelation preferred over deferoxamine

## Connections

- `targets` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — AA results from T cell-mediated HSC destruction → hypocellular marrow (<25% cellularity) replaced by fat; 25-40% of AA patients have PNH clones (AA-PNH overlap continuum); marrow biopsy showing fat-replaced hypocellular marrow is the diagnostic hallmark.
- `connects-to` → **[PNH](../pnh/README.md)** — AA and PNH are closely related: immune destruction of normal HSCs in AA allows PIGA-mutant GPI-deficient clone to expand; 25-40% of AA patients have PNH clones at diagnosis; some AA patients evolve to overt PNH; both conditions are treated at specialized hemato-oncology centers.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — In aplastic anemia, autoreactive CTL target HSCs via perforin/granzyme-mediated cytotoxicity; elevated perforin+ CD8+ T cells in AA bone marrow predict treatment response; cyclosporine + anti-thymocyte globulin (ATG) reduce autoreactive CTL activity and restore hematopoiesis.
- `connects-to` → **[Thrombopoietin](../../03-molecular/thrombopoietin/README.md)** — In severe AA, HSC destruction → thrombocytopenia; elevated TPO cannot drive production from depleted marrow; eltrombopag added to hATG+CsA (triple IST) improves overall response and may expand HSCs via c-Mpl beyond megakaryopoiesis.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^young-2018-aplastic-anemia-review]: Young NS. Aplastic Anemia. *N Engl J Med.* 2018;379(17):1643-1656. [doi:10.1056/NEJMra1413485](https://doi.org/10.1056/NEJMra1413485) · [PubMed 30354959](https://pubmed.ncbi.nlm.nih.gov/30354959/)
[^townsley-2017-eltrombopag-aa]: Townsley DM, Scheinberg P, Winkler T, et al. Eltrombopag Added to Standard Immunosuppression for Aplastic Anemia. *N Engl J Med.* 2017;376(16):1540-1550. [doi:10.1056/NEJMoa1613878](https://doi.org/10.1056/NEJMoa1613878) · [PubMed 28423296](https://pubmed.ncbi.nlm.nih.gov/28423296/)

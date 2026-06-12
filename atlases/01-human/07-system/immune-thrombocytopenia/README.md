---
schema: human-scale-entry/v1
id: immune-thrombocytopenia
name: Immune Thrombocytopenia
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Immune thrombocytopenia (ITP): anti-platelet IgG (anti-GPIIb/IIIa) → FcγR-mediated splenic destruction + CD8+ T-cell lysis; platelet <100×10⁹/L. Corticosteroids/IVIG first-line; romiplostim, eltrombopag (TPO-RAs); efgartigimod (FcRn inhibitor; FDA Jun 2023)."
aliases: ["ITP", "immune thrombocytopenic purpura", "idiopathic thrombocytopenic purpura", "primary ITP", "anti-platelet antibody"]
sources:
  - id: cines-2002-itp-review
    type: peer-reviewed
    cite: "Cines DB, Blanchette VS. Immune thrombocytopenic purpura. N Engl J Med. 2002;346(13):995-1008."
    doi: "10.1056/NEJMra010532"
    pmid: "11919310"
  - id: neunert-2019-ash-itp-guidelines
    type: peer-reviewed
    cite: "Neunert C, Terrell DR, Arnold DM, et al. American Society of Hematology 2019 guidelines for immune thrombocytopenia. Blood Adv. 2019;3(23):3829-3866."
    doi: "10.1182/bloodadvances.2019000966"
    pmid: "31794604"
  - id: bussel-2006-romiplostim-itp
    type: peer-reviewed
    cite: "Bussel JB, Kuter DJ, George JN, et al. AMG 531, a thrombopoiesis-stimulating protein, for chronic ITP. N Engl J Med. 2006;355(16):1672-1681."
    doi: "10.1056/NEJMoa054626"
    pmid: "17050891"
  - id: cheng-2011-eltrombopag-raise
    type: peer-reviewed
    cite: "Cheng G, Saleh MN, Marcher C, et al. Eltrombopag for management of chronic immune thrombocytopenia (RAISE). Lancet. 2011;377(9763):393-402."
    doi: "10.1016/S0140-6736(10)60959-2"
    pmid: "21237459"
cross_links:
  - target: 01-human/03-molecular/thrombopoietin
    relation: modulated-by
    note: "Anti-platelet IgG destroys platelets faster than compensatory TPO can restore them; romiplostim (FDA Aug 2008) and eltrombopag RAISE (FDA Nov 2008) bypass antibody-mediated destruction by stimulating c-Mpl on megakaryocyte progenitors; avatrombopag is also approved."
  - target: 01-human/03-molecular/fcrn
    relation: connects-to
    note: "FcRn recycles anti-GPIIb/IIIa IgG, sustaining pathogenic platelet antibody titers; efgartigimod (ADVANCE-SC: sustained platelet response ~22% vs ~5%; FDA Jun 2023) accelerates IgG catabolism → lower anti-platelet antibody levels; rozanolixizumab under investigation in ITP."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: modulated-by
    note: "Pathogenic anti-GPIIb/IIIa IgG (and anti-GPIb/IX IgG) opsonizes platelets for FcγRIII-mediated splenic macrophage phagocytosis; IVIG (2 g/kg) blocks Fc receptors and provides anti-idiotypic antibodies; rituximab (anti-CD20) depletes anti-platelet IgG-secreting B cells."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Anti-GPIIb/IIIa and anti-GPIb/IX IgG opsonize platelets for FcγR-mediated splenic destruction and CD8+ T-cell lysis; resulting thrombocytopenia causes mucocutaneous bleeding; ITP management targets platelet count >50×10⁹/L (safe for most activities) or >100×10⁹/L (surgery)."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "The spleen is the engine of ITP: red-pulp macrophages phagocytose IgG-opsonized platelets via FcγRIII, and splenic autoreactive B cells are a primary antibody source; splenectomy removes both and gives durable remission in ~60-70%, though now used later given effective TPO-RAs."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Splenic macrophages drive platelet destruction in ITP — FcγRIII (CD16) on red-pulp macrophages binds IgG-opsonized platelets → phagocytosis; IVIG works by Fc-receptor blockade and fostamatinib by inhibiting macrophage SYK signaling downstream of FcγR, both sparing platelets."
  - target: 02-pathogen/02-bacteria/helicobacter-pylori
    relation: connects-to
    note: "H. pylori is a cause of secondary ITP (~40-60% seropositive in endemic regions); eradication normalizes platelets in ~half of seropositive patients, likely by removing molecular-mimicry antigens and polyclonal B-cell stimulation, so ASH advises testing all ITP patients."
  - target: 01-human/07-system/iga-nephropathy
    relation: connects-to
    note: "Immune thrombocytopenia and IgA nephropathy are both antibody-mediated autoimmune diseases: ITP from anti-platelet IgG driving splenic destruction, IgAN from galactose-deficient IgA1 immune complexes in the kidney — distinct antigens, but both respond to B-cell-directed therapy."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Autoreactive B cells are the source of ITP's anti-platelet antibodies, so B-cell depletion with rituximab (anti-CD20) raises platelet counts in ~60% of patients; splenic B cells are a major antibody factory, part of why splenectomy works — both attack the antibody supply."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "ITP is often secondary to systemic lupus erythematosus: thrombocytopenia is a diagnostic criterion for SLE and can be its presenting feature; ITP plus autoimmune hemolytic anemia is termed Evans syndrome, so new-onset ITP warrants screening for connective-tissue disease."
---

# Immune Thrombocytopenia

## Overview

Immune thrombocytopenia (ITP) is an autoimmune disorder characterized by isolated thrombocytopenia (platelet count <100 × 10⁹/L) caused by autoantibody-mediated platelet destruction and impaired platelet production. It is the most common acquired thrombocytopenic disorder, with a prevalence of approximately 5–10 per 100,000 adults and 3–5 per 100,000 children [^cines-2002-itp-review]. ITP is clinically heterogeneous, ranging from an incidental laboratory finding in asymptomatic patients to life-threatening intracranial hemorrhage.

ITP is classified as:
- **Primary ITP**: No identifiable underlying cause (~80%)
- **Secondary ITP**: Associated with systemic lupus erythematosus (SLE), antiphospholipid syndrome, CLL, HIV, HCV, Helicobacter pylori infection, or drug exposure

By chronicity:
- **Newly diagnosed**: <3 months
- **Persistent**: 3–12 months (not spontaneously remitting)
- **Chronic**: >12 months

The discovery that **FcRn inhibition** (efgartigimod alfa, rozanolixizumab) accelerates catabolism of pathogenic anti-platelet IgG has established ITP as a flagship indication for the growing class of FcRn inhibitors, alongside myasthenia gravis, CIDP, and pemphigus [^neunert-2019-ash-itp-guidelines].

## Structure

### Pathogenic Mechanism — Three Pillars

ITP pathogenesis involves three interconnected immune abnormalities [^cines-2002-itp-review]:

**Pillar 1 — Anti-platelet antibodies:**
- **Anti-GPIIb/IIIa** (integrin αIIbβ3): Most common; present in ~60–70% of ITP patients
- **Anti-GPIb/IX**: ~20–40%; particularly important in MuSK-analogous IgG4-mediated functional blockade
- IgG1 and IgG3 (complement-activating subclasses) are the dominant pathogenic antibodies
- These antibodies are produced by autoreactive B cells in the spleen (primary site) and bone marrow
- Anti-GPIIb/IIIa IgG can also directly inhibit platelet aggregation → functional platelet impairment beyond reduced count

**Pillar 2 — FcγR-mediated platelet destruction:**
- IgG-opsonized platelets → **FcγRIII (CD16)** on splenic red pulp macrophages → phagocytosis; splenic FcγRIIa (CD32) also contributes
- **FcRn recycling** of anti-platelet IgG maintains chronic pathogenic antibody levels — the pharmacological basis for FcRn inhibitor therapy
- IVIG (2 g/kg IV over 2 days) acutely raises platelet count by: FcγR blockade on macrophages, anti-idiotypic antibodies, and possibly inhibiting FcRn recycling temporarily

**Pillar 3 — T-cell-mediated platelet destruction:**
- CD8+ cytotoxic T cells directly lyse platelets independent of IgG (important in seronegative ITP ~30%)
- Treg dysfunction: reduced Foxp3+ Treg numbers and suppressive function → failure to restrain autoreactive B and T cells
- CD4+ Th1 skewing: elevated IFN-γ, TNF-α → further macrophage activation

### Why Megakaryopoiesis is Impaired

Despite thrombocytopenia and elevated (or inappropriately normal) TPO, platelet production is suboptimal because:
1. Anti-GPIIb/IIIa antibodies bind megakaryocyte surface GPIIb/IIIa → impair proplatelet formation
2. CD8+ T cells infiltrate bone marrow → direct megakaryocyte destruction
3. Elevated megakaryocyte c-Mpl absorbs circulating TPO → blunts the expected TPO rise

This explains the apparent paradox that TPO-RAs can still further stimulate platelet production despite "normal" or modestly elevated endogenous TPO.

## Function

ITP disrupts normal haemostasis through quantitative (low count) and qualitative (antibody-coated, dysfunctional) platelet defects:

- **Mucocutaneous bleeding** — the hallmark: petechiae, purpura, ecchymoses, gingival bleeding, epistaxis, menorrhagia
- **Visceral bleeding** — GI hemorrhage, hematuria (less common)
- **Intracranial hemorrhage (ICH)** — rare (<1–2% of ITP), life-threatening; risk correlates with platelet count <10×10⁹/L and older age; the primary indication for emergency therapy
- **Fatigue and quality of life** — prevalent even without bleeding; correlates with disease activity and anti-platelet antibody levels, not just platelet count

Platelet count thresholds guide management:
- **>100 × 10⁹/L**: Normal; no ITP by definition
- **50–100 × 10⁹/L**: Low but safe for most activities; no routine treatment needed unless symptomatic
- **20–50 × 10⁹/L**: Increased mucocutaneous bleeding risk; treatment often initiated
- **<20 × 10⁹/L**: High risk; treatment recommended
- **<10 × 10⁹/L**: Emergency treatment threshold; highest ICH risk

## Pathology

### Diagnosis — Exclusion Process

ITP is a **diagnosis of exclusion** — no single definitive test exists:

1. **Complete blood count + peripheral smear**: Isolated thrombocytopenia (no anemia, no leukopenia unless drug-induced); large platelets on smear (young platelets); normal or increased megakaryocytes on bone marrow biopsy
2. **Screening for secondary causes**: ANA (SLE), antiphospholipid antibodies, HIV, HCV, HBV, *H. pylori* antigen/antibody
3. **Bone marrow biopsy**: Not routinely required in young patients with typical ITP; indicated in patients >60 years, atypical findings, or non-response to first-line therapy to exclude MDS or lymphoma
4. **Anti-platelet antibodies**: Low sensitivity (~50–70%); positive result supports diagnosis but negative does not exclude; not routinely used in guidelines
5. **Drug history review**: Quinine, heparin (HIT), valproate, trimethoprim-sulfamethoxazole among many causes of drug-induced thrombocytopenia

### H. pylori and Secondary ITP

*H. pylori* infection is found in ~40–60% of ITP patients (in endemic populations); eradication with triple therapy achieves platelet normalization in ~50% of seropositive patients, presumably by eliminating molecular mimicry antigens and reducing polyclonal B cell stimulation. ASH 2019 guidelines recommend *H. pylori* testing and treatment in all ITP patients.

## Treatment

### First-line (Newly Diagnosed ITP)

**Corticosteroids:**
- **Dexamethasone** 40 mg/day × 4 days: rapid platelet response (>50 × 10⁹/L) in 70–80%; preferred for faster kinetics over prednisone
- **Prednisone** 1 mg/kg/day × 2–4 weeks then taper: traditional standard; higher cumulative steroid exposure
- Complete remission (platelet >100 × 10⁹/L at 6 months off therapy): ~15–25% with either regimen

**IVIG:**
- 1–2 g/kg over 1–2 days for acute severe ITP or steroid contraindications
- Rapid platelet rise (often within 24–72 h) via FcγR blockade; effect transient (2–4 weeks)
- Anti-D (WinRho): 50–75 µg/kg in Rh+ non-splenectomized patients; activates FcγR blockade via IgG-coated RBCs

### Second-line

**Splenectomy:**
- Removes primary site of anti-platelet IgG production and platelet destruction
- Complete response (no therapy, platelet >100 × 10⁹/L) in ~60–70%; durable at 5 years in ~50%
- Delayed with laparoscopic technique; preceded by pneumococcal, meningococcal, Hib vaccination

**Rituximab (anti-CD20):**
- 375 mg/m² weekly × 4 doses (lymphoma schedule) or 1000 mg × 2 doses (RA schedule)
- Initial platelet response ~60%; sustained (>1 year) response ~20–25%
- Depletes CD20+ B cells → reduces anti-platelet IgG-secreting plasma cell precursors

**TPO-receptor agonists:**
- **Romiplostim** (Nplate): SC injection weekly; platelet response 88% vs 14% in pivotal trial [^bussel-2006-romiplostim-itp]; FDA August 2008
- **Eltrombopag** (Promacta): oral daily; RAISE trial (59% vs 16% platelet response at 6 months; FDA November 2008) [^cheng-2011-eltrombopag-raise]; also useful in aplastic anemia (with horse-ATG + cyclosporine)
- **Avatrombopag** (Doptelet): oral daily; non-inferior to eltrombopag; also approved for CLD-associated thrombocytopenia pre-procedure

**Fostamatinib (Tavalisse):**
- Oral SYK (spleen tyrosine kinase) inhibitor → blocks FcγR signaling in macrophages → reduces phagocytosis of IgG-opsonized platelets
- FIT trials: 18% vs 2% complete response; FDA April 2018 for adults with chronic ITP who have failed ≥1 previous treatment

### Third-line / Novel Agents

**FcRn inhibitors:**
- **Efgartigimod alfa SC** (Vyvgart Hytrulo): ADVANCE-SC+ trial: sustained platelet response (≥2 consecutive counts ≥50×10⁹/L) ~22% vs ~5% placebo; FDA June 2023 for adults with primary ITP
- **Rozanolixizumab** (Rystiggo): MYRIAD Phase 3 ongoing for ITP; already FDA-approved for generalized MG
- Mechanism: compete with IgG for FcRn binding → IgG (including anti-platelet IgG) routed to lysosomal degradation → reduced pathogenic antibody titers

**Anti-CD38:**
- **Mezagitamab**: MAYA-2 Phase 2 trial in ITP; anti-CD38 depletes plasma cells that secrete anti-platelet IgG (analogous to daratumumab in myeloma)
- **Daratumumab**: Case reports/series in refractory ITP

### Pregnancy-Associated ITP

ITP in pregnancy carries risk of neonatal thrombocytopenia (maternal IgG crosses placenta via FcRn on syncytiotrophoblasts → anti-platelet IgG opsonizes fetal platelets). Maternal platelet count does not predict neonatal platelet count well. Management:
- Platelet >30 × 10⁹/L in first/second trimester: observe
- Target >50 × 10⁹/L for vaginal delivery; >80 × 10⁹/L for cesarean
- IVIG ± corticosteroids are preferred (avoid TPO-RAs in pregnancy; safety data lacking)
- FcRn inhibitors under investigation for prevention of neonatal ITP

## Connections

- **Modulated by** → **[Thrombopoietin](../../03-molecular/thrombopoietin/README.md)** — Anti-platelet IgG destroys platelets faster than compensatory TPO can restore them; romiplostim and eltrombopag (RAISE) bypass antibody-mediated destruction by stimulating c-Mpl on megakaryocyte progenitors; avatrombopag also approved.
- `connects-to` → **[FcRn](../../03-molecular/fcrn/README.md)** — FcRn recycles anti-GPIIb/IIIa IgG sustaining pathogenic titers; efgartigimod (ADVANCE-SC: ~22% vs ~5% sustained platelet response; FDA Jun 2023) accelerates IgG catabolism → lower anti-platelet antibody levels; rozanolixizumab under investigation.
- **Modulated by** → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Pathogenic anti-GPIIb/IIIa IgG1/IgG3 opsonizes platelets for FcγRIII-mediated splenic phagocytosis; IVIG blocks Fc receptors; rituximab depletes anti-platelet IgG-secreting B cells.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Anti-GPIIb/IIIa and anti-GPIb/IX IgG opsonize platelets for destruction; CD8+ T cells directly lyse platelets; thrombocytopenia causes mucocutaneous bleeding; ITP treatment targets platelet count >50–100×10⁹/L.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — The spleen is the engine of ITP: red-pulp macrophages phagocytose IgG-opsonized platelets via FcγRIII, and splenic autoreactive B cells are a primary antibody source; splenectomy removes both and gives durable remission in ~60-70%, though now used later given effective TPO-RAs.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Splenic macrophages drive platelet destruction in ITP — FcγRIII (CD16) on red-pulp macrophages binds IgG-opsonized platelets → phagocytosis; IVIG works by Fc-receptor blockade and fostamatinib by inhibiting macrophage SYK signaling downstream of FcγR, both sparing platelets.
- `connects-to` → **[Helicobacter pylori](../../../02-pathogen/02-bacteria/helicobacter-pylori/README.md)** — H. pylori is a cause of secondary ITP (~40-60% seropositive in endemic regions); eradication normalizes platelets in ~half of seropositive patients, likely by removing molecular-mimicry antigens and polyclonal B-cell stimulation, so ASH advises testing all ITP patients.
- `connects-to` → **[IgA Nephropathy](../iga-nephropathy/README.md)** — Immune thrombocytopenia and IgA nephropathy are both antibody-mediated autoimmune diseases: ITP from anti-platelet IgG driving splenic destruction, IgAN from galactose-deficient IgA1 immune complexes in the kidney — distinct antigens, but both respond to B-cell-directed therapy.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — Autoreactive B cells are the source of ITP's anti-platelet antibodies, so B-cell depletion with rituximab (anti-CD20) raises platelet counts in ~60% of patients; splenic B cells are a major antibody factory, part of why splenectomy works — both attack the antibody supply.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — ITP is often secondary to systemic lupus erythematosus: thrombocytopenia is a diagnostic criterion for SLE and can be its presenting feature; ITP plus autoimmune hemolytic anemia is termed Evans syndrome, so new-onset ITP warrants screening for connective-tissue disease.

[^cines-2002-itp-review]: Cines DB, Blanchette VS. Immune thrombocytopenic purpura. *N Engl J Med.* 2002;346(13):995-1008. [doi:10.1056/NEJMra010532](https://doi.org/10.1056/NEJMra010532) · [PubMed 11919310](https://pubmed.ncbi.nlm.nih.gov/11919310/)
[^neunert-2019-ash-itp-guidelines]: Neunert C, et al. American Society of Hematology 2019 guidelines for immune thrombocytopenia. *Blood Adv.* 2019;3(23):3829-3866. [doi:10.1182/bloodadvances.2019000966](https://doi.org/10.1182/bloodadvances.2019000966) · [PubMed 31794604](https://pubmed.ncbi.nlm.nih.gov/31794604/)
[^bussel-2006-romiplostim-itp]: Bussel JB, et al. AMG 531, a thrombopoiesis-stimulating protein, for chronic ITP. *N Engl J Med.* 2006;355(16):1672-1681. [doi:10.1056/NEJMoa054626](https://doi.org/10.1056/NEJMoa054626) · [PubMed 17050891](https://pubmed.ncbi.nlm.nih.gov/17050891/)
[^cheng-2011-eltrombopag-raise]: Cheng G, et al. Eltrombopag for management of chronic immune thrombocytopenia (RAISE). *Lancet.* 2011;377(9763):393-402. [doi:10.1016/S0140-6736(10)60959-2](https://doi.org/10.1016/S0140-6736(10)60959-2) · [PubMed 21237459](https://pubmed.ncbi.nlm.nih.gov/21237459/)

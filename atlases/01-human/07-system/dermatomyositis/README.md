---
schema: human-scale-entry/v1
id: dermatomyositis
name: Dermatomyositis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Dermatomyositis is an immune-mediated myopathy with pathognomonic skin findings (heliotrope, Gottron's); type I IFN signature is central; MSAs (anti-MDA5, anti-TIF1γ, anti-NXP2, anti-Jo-1) stratify subtypes; IVIG (FDA Oct 2021), JAK inhibitors (baricitinib) are treatments."
aliases: ["dermatomyositis", "DM", "idiopathic inflammatory myopathy", "IIM", "anti-MDA5 myopathy", "amyopathic dermatomyositis", "antisynthetase syndrome", "juvenile dermatomyositis", "JDM"]
sources:
  - id: lundberg-2021-iim-classification
    type: peer-reviewed
    cite: "Lundberg IE, Tjärnlund A, Bottai M, et al. 2017 European League Against Rheumatism/American College of Rheumatology classification criteria for adult and juvenile idiopathic inflammatory myopathies and their major subgroups. Arthritis Rheumatol. 2017;69(12):2271-2282."
    doi: "10.1002/art.40320"
    pmid: "29106061"
    url: "https://doi.org/10.1002/art.40320"
  - id: aggarwal-2022-ivig-dm-prodera
    type: peer-reviewed
    cite: "Aggarwal R, Charles-Schoeman C, Schessl J, et al. Trial of Intravenous Immune Globulin in Dermatomyositis. N Engl J Med. 2022;387(14):1264-1278."
    doi: "10.1056/NEJMoa2117024"
    pmid: "36198072"
    url: "https://doi.org/10.1056/NEJMoa2117024"
  - id: sato-2021-anti-mda5-ild
    type: peer-reviewed
    cite: "Sato S, Kuwana M. Clinicopathological features of Japanese patients with anti-CADM-140/MDA5 antibody-positive dermatomyositis. Arthritis Rheum. 2009;61(5):611-620."
    doi: "10.1002/art.24341"
    pmid: "19405014"
    url: "https://doi.org/10.1002/art.24341"
  - id: bohan-peter-1975-dm-criteria
    type: peer-reviewed
    cite: "Bohan A, Peter JB. Polymyositis and dermatomyositis. N Engl J Med. 1975;292(7):344-347."
    doi: "10.1056/NEJM197502132920706"
    pmid: "1090839"
    url: "https://doi.org/10.1056/NEJM197502132920706"
cross_links:
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Type I IFN signature (↑MX1, ↑OAS1, ↑RSAD2) is elevated in muscle and blood in >80% of DM; anti-MDA5 (IFIH1) senses dsRNA → RIG-I/MDA5-MAVS-TBK1-IRF3 → IFN-β; pDC infiltration drives DM muscle interferonopathy; anifrolumab under investigation."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: modulated-by
    note: "IVIG (Octagam 10%; 2 g/kg monthly) is the first FDA-approved DM therapy (Oct 2021; ProDERM trial: CDASI-A improvement 58% vs 29%); MSA autoantibodies (anti-MDA5, anti-TIF1γ, anti-NXP2, anti-Mi-2) are IgG that stratify DM subtypes and prognosis."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Baricitinib (JAK1/2) showed efficacy in refractory DM (TRiMM-2: CDASI improvement); tofacitinib (JAK1/3) used for anti-MDA5-associated rapidly progressive ILD; ruxolitinib in refractory MDA5+ DM-ILD; JAK inhibition reduces type I IFN-driven ISG expression."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "DM features pathognomonic skin findings: heliotrope rash (violaceous periorbital edema), Gottron's papules (dorsal MCP/PIP), V-sign (anterior chest/neck), shawl sign, periungual telangiectasias, and mechanic's hands in antisynthetase syndrome."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Tacrolimus (calcineurin inhibitor) is steroid-sparing DM therapy; particularly effective in anti-MDA5+ DM-ILD where rapid IFN-driven fibrosis requires aggressive immunosuppression; calcineurin·NFAT pathway drives CD4+/Th-mediated muscle inflammation."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Interstitial lung disease complicates 20-40% of dermatomyositis: anti-MDA5+ DM can cause rapidly progressive ILD reaching respiratory failure within weeks (high ferritin flags the risk), demanding aggressive immunosuppression — tacrolimus triple therapy or JAK inhibitors."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Dermatomyositis is a microangiopathy: complement MAC on muscle capillaries causes capillary dropout → ischemia at fascicle edges, producing the pathognomonic perifascicular atrophy; this complement mechanism distinguishes DM from the T-cell muscle injury of polymyositis."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Dermatomyositis and lupus are both type I interferonopathies with photosensitive rashes, and their cutaneous signs are contrasted: Gottron's papules sit ON the knuckles whereas lupus spares them; both are now treated with anifrolumab, reflecting the shared interferon axis."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Dermatomyositis is an idiopathic inflammatory myopathy: complement-mediated capillary injury drives perifascicular atrophy and symmetric proximal weakness (trouble rising, lifting, climbing); CK rises, and it burdens the musculoskeletal system with arthralgia and calcinosis."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "Dermatomyositis is paraneoplastic in up to ~20-25% of adults, especially with anti-TIF1γ antibodies: ovarian, lung, breast and GI cancers are over-represented, and ovarian cancer is a classic association—so new adult DM mandates age-appropriate malignancy screening."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Dermatomyositis muscle and skin are infiltrated by macrophages and plasmacytoid dendritic cells pouring out type I interferon, the disease's central cytokine; macrophage inflammation amplifies the complement-driven microangiopathy, and JAK inhibitors blunt this signalling."
---

# Dermatomyositis

## Overview

**Dermatomyositis (DM)** is a systemic autoimmune disease classified among the **idiopathic inflammatory myopathies (IIMs)**, characterized by the combination of **immune-mediated skeletal muscle inflammation** and **distinctive cutaneous manifestations** [^bohan-peter-1975-dm-criteria]. It is distinguished from other IIMs (polymyositis, immune-mediated necrotizing myopathy, inclusion body myositis, antisynthetase syndrome) by its pathognomonic skin features and a strong type I interferon immunopathological signature.

**Epidemiology:**
- Incidence: 2–10 cases per million per year (adults); 2–4 per million (juvenile DM)
- Bimodal age distribution: juvenile DM (JDM) peaks 5–15 years; adult DM peaks 45–65 years
- Sex ratio: F:M ~2:1; juvenile DM ~F:M 2.3:1
- Associated with interstitial lung disease (ILD) in 20–40% of cases, and with malignancy (especially anti-TIF1γ+ DM, ~20–30% cancer risk)

**Myositis-specific autoantibodies (MSAs)** have transformed the diagnostic and prognostic classification of DM, moving beyond the original Bohan & Peter criteria to an MSA-defined taxonomy that predicts clinical phenotype, ILD risk, cancer association, and treatment response [^lundberg-2021-iim-classification]:

| MSA | Prevalence | Clinical features |
|:----|:-----------|:-----------------|
| **Anti-MDA5** (IFIH1) | ~15–30% of DM | Amyopathic or mild myositis; rapidly progressive ILD (RP-ILD); skin ulcers; high mortality if RP-ILD untreated |
| **Anti-TIF1γ** (TRIM33) | ~20–30% of DM | Classic DM skin; cancer-associated DM (lung, ovary, GI, breast); ~25% 3-year cancer risk in adults |
| **Anti-NXP2** (MORC3) | ~10–20% | Severe myositis; dystrophic calcinosis in JDM; cancer-associated in adults |
| **Anti-Mi-2** | ~15–20% | Classic DM skin; moderate myositis; good prognosis; low ILD risk |
| **Anti-SAE** | ~5–10% | Cutaneous-predominant initially; severe dysphagia |
| **Anti-Jo-1** (HARS1) | ~10–15% | Antisynthetase syndrome: ILD + myositis + arthritis + mechanic's hands + Raynaud's |
| **Anti-HMGCR** | Overlaps with IMNM | Statin-associated or de novo necrotizing myopathy |

## Structure

### Disease architecture

DM is a multi-tissue inflammatory disease with variable involvement:

**Muscle:** Proximal limb weakness (shoulder girdle > hip girdle); difficulty rising from floor, climbing stairs, raising arms above head; dysphagia (cricopharyngeal muscle) in severe cases; elevated CK (often 10–50× ULN, but may be normal in amyopathic DM); EMG shows short-duration, low-amplitude polyphasic units (myopathic); MRI shows muscle edema (T2/STIR bright signal) in affected muscles.

**Skin (cutaneous DM features):**
- **Heliotrope rash:** Violaceous (dusky lilac) erythema and edema of bilateral periorbital area, pathognomonic when present
- **Gottron's papules:** Erythematous to violaceous flat-topped papules overlying dorsal MCP, PIP, DIP joints; pathognomonic (vs. SLE which spares knuckles)
- **Gottron's sign:** Erythema over elbows, knees (non-papular variant of Gottron's papules)
- **V-sign:** Erythema in V-distribution over anterior chest/neck (sun-exposed)
- **Shawl sign:** Erythema/poikiloderma over posterior neck, shoulders, upper back
- **Mechanic's hands:** Hyperkeratotic fissured skin along radial aspect of index finger and thumb; associated with antisynthetase syndrome/anti-Jo-1
- **Periungual changes:** Dilated, tortuous nailfold capillaries (nailfold capillaroscopy); cuticular hypertrophy; periungual erythema

**Lung (ILD):** Most common in anti-MDA5 (RP-ILD), anti-PL-12, anti-PL-7, anti-Jo-1 (antisynthetase syndrome); NSIP or UIP pattern on HRCT; RP-ILD in anti-MDA5 can progress to respiratory failure in weeks; ferritin markedly elevated (>1500 μg/L) predicts RP-ILD.

**Joints:** Arthritis/arthralgia in antisynthetase syndrome; not typical of classic DM.

### Diagnostic criteria

The **2017 EULAR/ACR classification criteria** [^lundberg-2021-iim-classification] use a weighted scoring system including:
- Objective muscle weakness (proximal, symmetric)
- Skin manifestations (heliotrope, Gottron's, V-sign/shawl sign)
- Laboratory (elevated CK/aldolase, anti-Jo-1+)
- Muscle biopsy findings (perifascicular atrophy, MAC deposits on capillaries)
- EMG findings
- MSA positivity

## Function

CIDP impairs function through three parallel mechanisms:

1. **Skeletal muscle impairment** — proximal weakness limits activities of daily living (rising from chair, climbing stairs, grooming, swallowing); respiratory muscle involvement can cause hypoventilatory failure; functional status quantified with Manual Muscle Testing 8 (MMT8), HAQ, MYOACT.

2. **Cutaneous impairment** — pruritus (often severe in DM, especially anti-MDA5), skin ulceration (anti-MDA5), calcinosis (NXP2+ JDM); skin disease quantified with CDASI (Cutaneous DM Disease Area and Severity Index).

3. **Extra-muscular systemic burden** — ILD (anti-MDA5, antisynthetase): progressive dyspnea, hypoxemia, risk of respiratory failure; malignancy (anti-TIF1γ, anti-NXP2): cancer surveillance required; cardiac involvement (conduction abnormalities, cardiomyopathy in severe DM): monitoring required.

## Pathology

### Type I interferon-driven immunopathogenesis

Dermatomyositis is fundamentally a **type I interferonopathy** of muscle and skin [^sato-2021-anti-mda5-ild]:

**Sensing and IFN production:**
- **Anti-MDA5-associated DM:** Anti-MDA5 (anti-IFIH1) autoantibodies arise against the RNA helicase MDA5; the trigger is likely viral dsRNA or endogenous dsRNA from damaged cells → MDA5 → MAVS → TBK1 → IRF3 → IFN-β. Paradoxically, anti-MDA5 antibodies may disrupt normal MDA5 viral sensing, impairing viral clearance while IFN production continues via alternative pathways.
- **pDC infiltration:** Plasmacytoid dendritic cells (pDCs) — the major IFN-α factories — infiltrate DM muscle and skin; TLR7/9 sensing of endogenous nucleic acids from damaged muscle → sustained IFN-α production
- **Type I IFN signature:** ↑MX1, ↑OAS1, ↑ISG15, ↑RSAD2 measurable in blood and muscle; present in >80% of DM vs. <30% of inclusion body myositis; IFN score correlates with disease activity

**Complement-mediated muscle capillary injury:**
- **Perifascicular atrophy** (pathognomonic on biopsy): muscle fibers at periphery of fascicles are smaller, atrophic, and necrotic → complement MAC (C5b-9) deposits on capillaries → microangiopathy → perifascicular ischemia → atrophy; this complement-driven mechanism distinguishes DM from PM (which is MHC-I/perforin/CD8+ T cell-mediated)
- Anti-NXP2 and anti-TIF1γ DM have predominantly B cell-driven, complement-activating pathology

**Cellular infiltrates:**
- Perivascular/perimysial CD4+ T cells and B cells (vs. endomysial CD8+ T cells in PM)
- pDC-rich infiltrates in DM skin (type I IFN amplification)
- Th17 CD4+ T cells contribute to anti-MDA5 ILD-associated fibrosis

### Malignancy association

DM carries a ~3–7× elevated cancer risk overall. Anti-TIF1γ (TRIM33) suppresses TGF-β signaling in normal tissue; anti-TIF1γ autoimmunity may represent an immune response to tumor-expressed TIF1γ neoantigens. Screening: CT chest/abdomen/pelvis, CA-125, PSA, colonoscopy, mammography at diagnosis and annually × 3 years.

## Treatment

### First-line

**Corticosteroids (backbone of all IIM therapy):**
- Oral prednisone 1 mg/kg/d (max 60–80 mg/d) → taper over 6–12 months guided by CK, muscle strength, and functional scores
- High-dose IV methylprednisolone 1 g/d × 3 days for severe weakness, dysphagia, or RP-ILD
- Toxicity: osteoporosis (bisphosphonate prophylaxis), diabetes, cataracts, myopathy (steroid myopathy)

**IVIG (first FDA-approved therapy for DM):**
- **ProDERM trial** (N=95, randomized, double-blind): IVIG (Octagam 10%; 2 g/kg monthly × 3 cycles) vs. placebo → primary endpoint: total improvement score at month 3 (58.3% IVIG vs. 28.0% placebo; p<0.0001) [^aggarwal-2022-ivig-dm-prodera]; FDA approved **October 2021**
- Used as steroid-sparing agent or for acute severe DM; mechanism: FcγR saturation, anti-idiotypic, complement neutralization, possible FcRn saturation
- Subcutaneous IVIG: equivalent option for maintenance therapy

### Second-line (steroid-sparing)

**Methotrexate (MTX):** 15–25 mg/week SC or oral; first-line steroid-sparing; avoid in ILD (pulmonary toxicity; use alternative)

**Azathioprine (AZA):** 2–3 mg/kg/d; slow onset (3–6 months); widely used for maintenance; TPMT/NUDT15 testing before start

**Mycophenolate mofetil (MMF):** 2–3 g/d; preferred for ILD-associated DM over MTX

**Tacrolimus:** 1–3 mg/d, targeting trough 5–10 ng/mL; calcineurin inhibitor; particularly effective for **anti-MDA5-associated ILD**; combination tacrolimus + cyclosporine + pulse methylprednisolone ("triple therapy") used in Japan for RP-ILD with reported ~60–70% 12-month survival vs. ~20–30% with steroids alone

**Rituximab:** Anti-CD20; effective for anti-Jo-1 (antisynthetase syndrome) and anti-Mi-2 DM; the **RIM trial** (Rituximab in Myositis; n=200) met primary endpoint in a pre-specified subset; used for refractory DM

### Newer and investigational

**JAK inhibitors:**
- **Baricitinib** (JAK1/2; Olumiant): Phase 3 TRiMM-2 trial showed CDASI improvement in ~60% of DM patients at 36 weeks; FDA approved for a related indication (alopecia areata 2022); off-label use in DM growing
- **Tofacitinib** (JAK1/3): Case series and Phase 2 evidence for anti-MDA5-associated RP-ILD; reduces IFN signature; JAK blockade prevents STAT1 phosphorylation → reduces ISG transcription
- **Ruxolitinib** (JAK1/2): Used for refractory MDA5+ DM-ILD

**Anti-IFNAR (anifrolumab):** Phase 2 trials ongoing in DM given the strong type I IFN signature; already approved for SLE

**Complement inhibitors:** C5 inhibitors (eculizumab) under investigation for HMGCR+ immune-mediated necrotizing myopathy (IMNM) where complement-mediated muscle necrosis is prominent; not established in classic DM

## Connections

- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Type I IFN signature (↑MX1, ↑OAS1, ↑RSAD2) is elevated in muscle and blood in >80% of DM; anti-MDA5 (IFIH1) → RIG-I/MDA5-MAVS-TBK1-IRF3 → IFN-β; pDC infiltration drives DM muscle interferonopathy; anifrolumab under investigation.
- **Modulated by** → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — IVIG (Octagam 10%; 2 g/kg monthly) is the first FDA-approved DM therapy (Oct 2021; ProDERM: CDASI-A improvement 58% vs 29%); MSA autoantibodies (anti-MDA5, anti-TIF1γ, anti-NXP2, anti-Mi-2) are IgG that stratify DM subtypes and prognosis.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Baricitinib (JAK1/2) showed efficacy in refractory DM (TRiMM-2 Phase 3); tofacitinib (JAK1/3) used for anti-MDA5-associated rapidly progressive ILD; ruxolitinib in refractory MDA5+ DM-ILD; JAK inhibition reduces type I IFN-driven ISG expression.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — DM features pathognomonic skin findings: heliotrope rash (periorbital), Gottron's papules (dorsal MCP/PIP), V-sign, shawl sign, periungual telangiectasias, and mechanic's hands in antisynthetase syndrome.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Tacrolimus (calcineurin inhibitor) is steroid-sparing DM therapy; particularly effective in anti-MDA5+ DM-ILD requiring aggressive immunosuppression; calcineurin·NFAT pathway drives CD4+/Th-mediated muscle inflammation.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Interstitial lung disease complicates 20-40% of dermatomyositis: anti-MDA5+ DM can cause rapidly progressive ILD reaching respiratory failure within weeks (high ferritin flags the risk), demanding aggressive immunosuppression — tacrolimus triple therapy or JAK inhibitors.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Dermatomyositis is a microangiopathy: complement MAC on muscle capillaries causes capillary dropout → ischemia at fascicle edges, producing the pathognomonic perifascicular atrophy; this complement mechanism distinguishes DM from the T-cell muscle injury of polymyositis.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — Dermatomyositis and lupus are both type I interferonopathies with photosensitive rashes, and their cutaneous signs are contrasted: Gottron's papules sit ON the knuckles whereas lupus spares them; both are now treated with anifrolumab, reflecting the shared interferon axis.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Dermatomyositis is an idiopathic inflammatory myopathy: complement-mediated capillary injury drives perifascicular atrophy and symmetric proximal weakness (trouble rising, lifting, climbing); CK rises, and it burdens the musculoskeletal system with arthralgia and calcinosis.
- `connects-to` → **[Ovarian Cancer](../ovarian-cancer/README.md)** — Dermatomyositis is paraneoplastic in up to ~20-25% of adults, especially with anti-TIF1γ antibodies: ovarian, lung, breast and GI cancers are over-represented, and ovarian cancer is a classic association—so new adult DM mandates age-appropriate malignancy screening.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Dermatomyositis muscle and skin are infiltrated by macrophages and plasmacytoid dendritic cells pouring out type I interferon, the disease's central cytokine; macrophage inflammation amplifies the complement-driven microangiopathy, and JAK inhibitors blunt this signalling.

[^bohan-peter-1975-dm-criteria]: Bohan A, Peter JB. Polymyositis and dermatomyositis. *N Engl J Med.* 1975;292(7):344-347. [doi:10.1056/NEJM197502132920706](https://doi.org/10.1056/NEJM197502132920706) · [PubMed 1090839](https://pubmed.ncbi.nlm.nih.gov/1090839/)
[^lundberg-2021-iim-classification]: Lundberg IE, et al. 2017 EULAR/ACR classification criteria for adult and juvenile idiopathic inflammatory myopathies. *Arthritis Rheumatol.* 2017;69(12):2271-2282. [doi:10.1002/art.40320](https://doi.org/10.1002/art.40320) · [PubMed 29106061](https://pubmed.ncbi.nlm.nih.gov/29106061/)
[^aggarwal-2022-ivig-dm-prodera]: Aggarwal R, Charles-Schoeman C, Schessl J, et al. Trial of Intravenous Immune Globulin in Dermatomyositis. *N Engl J Med.* 2022;387(14):1264-1278. [doi:10.1056/NEJMoa2117024](https://doi.org/10.1056/NEJMoa2117024) · [PubMed 36198072](https://pubmed.ncbi.nlm.nih.gov/36198072/)
[^sato-2021-anti-mda5-ild]: Sato S, Kuwana M. Clinicopathological features of Japanese patients with anti-CADM-140/MDA5 antibody-positive dermatomyositis. *Arthritis Rheum.* 2009;61(5):611-620. [doi:10.1002/art.24341](https://doi.org/10.1002/art.24341) · [PubMed 19405014](https://pubmed.ncbi.nlm.nih.gov/19405014/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

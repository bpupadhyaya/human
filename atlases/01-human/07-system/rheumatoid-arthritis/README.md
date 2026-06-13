---
schema: human-scale-entry/v1
id: rheumatoid-arthritis
name: Rheumatoid Arthritis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Autoimmune synovitis from Th17/macrophage TNF-alpha and IL-6 activation; ACPA/anti-CCP antibodies are diagnostic. Methotrexate is first-line; TNF inhibitors (adalimumab), IL-6 blockade (tocilizumab), and JAK inhibitors (baricitinib) for refractory disease."
aliases: ["RA", "rheumatoid disease", "adult RA", "seropositive arthritis", "inflammatory arthritis"]
sources:
  - id: smolen-2016-ra-lancet
    type: peer-reviewed
    cite: "Smolen JS, Aletaha D, McInnes IB. Rheumatoid arthritis. Lancet. 2016;388(10055):2023-2038."
    doi: "10.1016/S0140-6736(16)30173-8"
    pmid: "27156434"
    url: "https://doi.org/10.1016/S0140-6736(16)30173-8"
  - id: firestein-2003-ra-pathogenesis
    type: peer-reviewed
    cite: "Firestein GS. Evolving concepts of rheumatoid arthritis. Nature. 2003;423(6937):356-361."
    doi: "10.1038/nature01661"
    pmid: "12748655"
    url: "https://doi.org/10.1038/nature01661"
  - id: genovese-2016-baricitinib
    type: peer-reviewed
    cite: "Genovese MC, Kremer J, Zamani O, et al. Baricitinib in Patients with Refractory Rheumatoid Arthritis. N Engl J Med. 2016;374(13):1243-1252."
    doi: "10.1056/NEJMoa1507247"
    pmid: "27028914"
    url: "https://doi.org/10.1056/NEJMoa1507247"
cross_links:
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF-alpha is the master cytokine in RA synovitis; synovial macrophages and fibroblasts produce TNF → NF-kB → MMP secretion and bone erosion; TNF inhibitors (etanercept, adalimumab, certolizumab) are the backbone of biologic DMARD therapy in RA."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 drives systemic RA inflammation (acute-phase response, anemia, fatigue) and Th17/Tfh polarization → ACPA production; tocilizumab and sarilumab (anti-IL-6R) improve ACR50 vs methotrexate alone; IL-6 is the dominant cytokine driving RA fever and CRP elevation."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Th17 cells produce IL-17A/F → recruit neutrophils and activate synovial fibroblasts; Tfh cells drive ACPA-producing B cells; Th1 drives macrophage activation; abatacept (CTLA-4-Ig) blocks CD28 co-stimulation, suppressing both T cell subsets in RA synovium."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-kB activated in RA synovial fibroblasts by TNF-alpha and IL-1beta → MMP secretion → cartilage degradation; NF-kB also induces RANKL → osteoclast activation → bone erosion; glucocorticoids and DMARDs (methotrexate, bDMARDs) suppress NF-kB as a shared mechanism."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A is present in RA synovium but secondary to TNF-alpha and IL-6; IL-17A promotes osteoclastogenesis via RANKL induction; IL-17A inhibitors (secukinumab) failed pivotal RA trials; bimekizumab (anti-IL-17A/F) showed marginal RA benefit vs established TNF/IL-6 blockade."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5+ macrophages and Th1 cells are abundant in RA synovium; CCR5 ligands (CCL3/CCL4/CCL5) are elevated in RA synovial fluid and correlate with disease activity; maraviroc (CCR5 antagonist) has been explored in RA with modest benefit in small trials."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "CCL2 is the dominant synovial chemokine in RA: synoviocytes and FLS secrete CCL2 → CCR2+ monocyte/macrophage recruitment → pannus formation; synovial fluid CCL2 >5 ng/mL correlates with radiographic damage; macrophage-derived RANKL and MMPs drive joint destruction."
  - target: 03-medicine/01-modern/12-anti-inflammatory/ibuprofen
    relation: treated-by
    note: "NSAIDs including ibuprofen reduce COX-2-driven synovial PGE₂ → less joint pain, swelling, and stiffness; adjuncts to DMARDs; reduce RA symptoms but not radiographic progression; long-term use requires GI prophylaxis (PPI)."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: treated-by
    note: "Corticosteroids (prednisolone 5–10 mg/day) are bridge therapy in RA while DMARDs take effect; reduce radiographic progression in early RA (COBRA, BeSt trials); long-term use requires osteoporosis prophylaxis (bisphosphonate + calcium/vitamin D)."
  - target: 03-medicine/01-modern/11-biologics/adalimumab
    relation: treated-by
    note: "Adalimumab (anti-TNFα) is first-line biologic for MTX-inadequate RA; ARMADA trial: ACR50 59% vs 24% at 24 weeks; inhibits radiographic progression; mTNFα reverse signaling induces IL-10; TB screening mandatory before initiation (3-25× TB reactivation risk)."
  - target: 01-human/07-system/psoriatic-arthritis
    relation: connects-to
    note: "Rheumatoid and psoriatic arthritis are the two major inflammatory arthritides but contrast: RA is a symmetric, RF/anti-CCP-positive synovitis sparing the DIP joints, while PsA is a seronegative spondyloarthropathy with enthesitis, dactylitis, DIP disease, and psoriasis."
  - target: 01-human/07-system/sjogrens-syndrome
    relation: connects-to
    note: "Rheumatoid arthritis is the commonest disease complicated by secondary Sjögren's syndrome: chronic autoimmune inflammation extends to lacrimal and salivary glands, causing dry eyes and mouth (sicca), so RA patients are screened for the overlap."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Synovial fibroblasts are active drivers, not bystanders, of rheumatoid arthritis: activated fibroblast-like synoviocytes form the invasive pannus and secrete proteases and cytokines that erode cartilage and bone, behaving almost tumor-like—a therapeutic target."
---

# Rheumatoid Arthritis

## Overview

**Rheumatoid arthritis (RA)** is a **chronic, systemic autoimmune disease** characterized by persistent synovial inflammation, progressive joint destruction, and extra-articular manifestations. It affects approximately **1% of the global population** (~18 million people), with a female:male ratio of ~3:1, and peak incidence between 40-60 years of age. RA is the most common inflammatory arthritis and a leading cause of disability worldwide [^smolen-2016-ra-lancet].

RA is defined by **synovitis** — inflammation of the synovial membrane lining the joint — driven by an aberrant adaptive immune response against self-antigens, particularly **citrullinated proteins** (resulting from post-translational deimination of arginine to citrulline by PAD enzymes). The resulting **ACPA (anti-citrullinated protein antibodies) / anti-CCP** response is pathognomonic: detected in ~70% of RA patients and present years before clinical disease.

**Classification criteria (ACR/EULAR 2010):** Score ≥6/10 defines RA; includes joint involvement (0-5), serology (RF/ACPA, 0-3), acute-phase reactants (0-1), and duration (0-1).

**Clinical heterogeneity:**
- **Seropositive RA** (~70-80%): RF and/or ACPA positive; more destructive disease; higher risk of erosions and extra-articular manifestations
- **Seronegative RA** (~20-30%): No RF/ACPA; diagnosis by clinical criteria; may represent heterogeneous group including early seronegative psoriatic arthritis, reactive arthritis
- **Very early RA (VERA):** Undifferentiated arthritis evolving to RA; window of opportunity for remission induction before structural damage

## Structure

### Synovial pathology [^firestein-2003-ra-pathogenesis]

Normal synovium: 1-2 cell layers of synoviocytes (type A macrophage-like, type B fibroblast-like) on a thin, vascularized stroma.

**RA pannus formation:**
- **Synovial hyperplasia:** Inflammatory cytokines (TNF-alpha, IL-6, IL-1beta) → synoviocyte proliferation → synovium thickens to 6-10 cell layers
- **Angiogenesis:** VEGF and TNF-alpha → neovascularization → sustains inflammatory infiltrate
- **Cellular infiltrate:** CD4+ T cells (predominantly Th1, Th17) and B cells (follicle-like structures in ~25%) + macrophages + plasma cells (produce RF and ACPA locally)
- **Pannus:** Invasive synovial tissue → invades and destroys cartilage and bone at the cartilage-pannus junction
- **Fibroblast-like synoviocytes (FLS):** Central pathological effector; produce: MMP-1/3/13 → cartilage collagen degradation; RANKL → osteoclast differentiation; IL-6, IL-8, VEGF; also migrate and spread disease to other joints (metastasis-like)

### Pathogenic sequence

**1. Initiating events (years before clinical disease):**
- Genetic susceptibility: **HLA-DRB1 shared epitope** (SE alleles: *0101, *0401, *0404) — SE presents citrullinated peptides to CD4+ T cells; OR 3-5× for seropositive RA
- Environmental triggers: Smoking (most reproducible; promotes citrullination in lungs → anti-CCP production → systemic spread); periodontal disease (P. gingivalis, a citrullinating bacterium); microbiome dysbiosis
- Citrullination: PAD2/4 enzymes citrullinate proteins (vimentin, fibrinogen, alpha-enolase, type II collagen) → neoepitopes presented by SE HLA-DR → ACPA production

**2. Pre-clinical phase:**
- ACPA (IgG, IgM, IgA) and RF in serum; no joint inflammation
- Systemic inflammatory biomarkers: elevated IL-6, TNF-alpha, sRANKL in blood
- First-degree relatives with ACPA: 1-2%/year rate of progression to RA

**3. Clinical synovitis:**
- ACPA-immune complex formation in synovium → activates complement → C3a/C5a → mast cell degranulation and macrophage activation
- **Macrophages:** Master orchestrators; produce TNF-alpha, IL-1beta, IL-6, IL-12/23 → amplify all downstream pathways
- **Th17 cells:** IL-17A/F → IL-17R on FLS and osteoblasts → IL-6, IL-8, CXCL1 (neutrophil recruitment), RANKL (osteoclast activation)
- **B cell involvement:** ACPA and RF production by plasma cells; B cells also present antigens to T cells and produce cytokines; B cell depletion (rituximab) effective

## Function

### Clinical presentation [^smolen-2016-ra-lancet]

**Articular:**
- **Symmetrical polyarthritis:** MCPs, PIPs, wrists, MTPs most commonly; DIP joints typically spared (vs psoriatic arthritis)
- **Morning stiffness:** >1 hour of joint stiffness/pain on waking → correlates with synovitis activity; a key diagnostic criterion
- **Synovitis on exam:** Warm, swollen, tender joints; synovial thickening (boggy texture); reduced grip strength
- **Joint deformities (chronic/untreated RA):**
  - Ulnar deviation of MCPs
  - Swan-neck deformity (MCP flexion, PIP hyperextension, DIP flexion)
  - Boutonnière deformity (PIP flexion, DIP hyperextension)
  - Z-thumb deformity
  - Hammer toes
- **Cervical spine:** C1-C2 atlantoaxial subluxation (cricoarytenoid involvement → hoarseness); screen pre-surgery

**Extra-articular manifestations (~40% of RA):**
- **Rheumatoid nodules:** Fibrinoid necrosis surrounded by palisading macrophages; elbows, fingers, bursae; associated with RF+/seropositive disease and MTX use (accelerated nodulosis)
- **Cardiovascular disease:** Major cause of excess RA mortality; systemic inflammation accelerates atherosclerosis; doubled risk of MI; treat CV risk aggressively; anti-TNF therapy reduces CV events
- **Interstitial lung disease (ILD):** UIP or NSIP pattern; ~10%; anti-CCP+ and male sex are risk factors; smoking cessation critical
- **Felty's syndrome:** RA + splenomegaly + neutropenia → recurrent infections
- **Scleritis, episcleritis**
- **Peripheral neuropathy, mononeuritis multiplex (vasculitis)**

**Disease activity measures:**
- **DAS28:** 28-joint disease activity score; ESR and CRP-based; remission <2.6, low activity 2.6-3.2
- **CDAI/SDAI:** Clinical/simplified disease activity index
- **Treat-to-target (T2T) strategy:** Target DAS28 remission or low disease activity; monthly adjustment until target achieved

### Extra-articular: CV and cancer risk

RA patients have:
- **2× increased cardiovascular mortality** (atherosclerosis acceleration via systemic inflammation; endothelial dysfunction; dyslipidemia from steroids)
- **~2× increased lymphoma risk** (particularly diffuse large B-cell; correlates with disease activity, not treatment)
- **Reduced solid tumor risk** (colorectal) relative to general population

## Pathology

### Diagnosis

**Laboratory:**
- **RF (IgM anti-IgG Fc):** Sensitivity 70%, specificity ~80%; also positive in Sjögren's (>75%), hepatitis C (40-70%), healthy elderly (~5%)
- **ACPA (anti-CCP, Ig class mixture):** Sensitivity 70%, specificity **>95%** — best serological marker for RA diagnosis; detectable 10+ years before symptom onset
- **CRP, ESR:** Correlate with disease activity; CRP more sensitive than ESR for monitoring
- **CBC:** Anemia of chronic disease (normocytic, normochromic); thrombocytosis during active disease
- **Complete metabolic panel:** Monitor for treatment-related hepatotoxicity (MTX) and renal disease

**Imaging:**
- **X-ray:** Periarticular osteopenia (early) → joint space narrowing → marginal erosions (late, irreversible); modified Sharp-van der Heijde score to track progression
- **Ultrasound:** Synovitis (grey-scale) and active vascularity (power Doppler) in real-time; detects subclinical synovitis and guides joint aspiration
- **MRI:** Most sensitive for bone marrow edema (pre-erosive) and synovitis; RAMRIS (RA MRI scoring) in clinical trials

### Treatment [^genovese-2016-baricitinib]

**Treat-to-target strategy:** Aggressive early therapy, monthly monitoring until remission, then taper.

**Conventional synthetic DMARDs (csDMARDs):**
- **Methotrexate (MTX):** First-line; weekly oral/subcutaneous; folate antagonist → adenosine-mediated anti-inflammatory; 15-25 mg/week; folic acid co-administration; monitor LFTs, CBC; teratogenic; combinations with bDMARDs superior to MTX monotherapy
- **Hydroxychloroquine (HCQ):** Mild-moderate RA; antimalarial → inhibits TLR9 and lysosomal acidification → reduces cytokine production; retinal toxicity (annual ophthalmology screening after 5 years)
- **Sulfasalazine:** Combined with MTX+HCQ in "triple therapy"; effective for seronegative RA
- **Leflunomide:** Inhibits DHODH → reduces de novo pyrimidine synthesis → anti-proliferative; alternative to MTX (comparable efficacy)

**Biologic DMARDs (bDMARDs) — for MTX-inadequate responders:**

*Anti-TNF (first-line biologic):*
- Etanercept (TNF receptor-Fc fusion), adalimumab, infliximab (anti-TNF-alpha mAbs), certolizumab (PEGylated anti-TNF Fab, safe in pregnancy), golimumab
- ~30-40% ACR50 at 6 months added to MTX; reduce radiographic progression
- Screen for TB (reactivation risk); do not use with active serious infection; contraindicated in advanced heart failure (Class III-IV)

*Anti-IL-6 receptor:*
- **Tocilizumab (anti-IL-6R, Actemra):** IV or SC; monotherapy effective (unlike TNF inhibitors) for MTX-intolerant patients; MONARCH trial: superior to adalimumab in monotherapy on DAS28 remission; reduces acute-phase reactants → normalizes CRP/ESR (caution: CRP may not reflect infection when on tocilizumab)
- **Sarilumab (anti-IL-6R):** SC injection; SARIL-RA MONARCH: superior to adalimumab monotherapy

*Anti-CD20 (B-cell depletion):*
- **Rituximab:** IV infusion (2× 1000 mg, 2 weeks apart); reserve for RF+/ACPA+ patients (B-cell-driven); effective in TNF-refractory RA; risk of hypogammaglobulinemia with repeated courses; hepatitis B reactivation screening required

*T-cell co-stimulation blockade:*
- **Abatacept (CTLA-4-Ig):** Binds B7 (CD80/86) on APCs → blocks CD28 co-stimulation → prevents T-cell activation; particularly effective in ACPA+ patients (seropositive RA); safer infection profile than anti-TNF; IV or SC

**Targeted synthetic DMARDs (tsDMARDs) — JAK inhibitors:**

*JAK1/2 inhibitors:*
- **Baricitinib (Olumiant):** JAK1/2 inhibitor → blocks IL-6, IFN-gamma, EPO, and growth factor signaling; RA-BEACON: 55% ACR20 vs 27% placebo in TNF-inadequate responders [^genovese-2016-baricitinib]; COVID-19 hospitalized patients benefit (non-RA indication via ACTT-2)
- **Upadacitinib (Rinvoq):** Selective JAK1 inhibitor; SELECT-COMPARE: superior to adalimumab on ACR50 at 12 weeks; also approved for psoriatic arthritis, AS, atopic dermatitis

*JAK1 inhibitors:*
- **Tofacitinib (Xeljanz):** First JAK inhibitor in RA; JAK1/3; FDA approved 2012; boxed warning for thrombosis risk (more prominent in ORAL Surveillance post-marketing study)

**Safety considerations for JAK inhibitors:** Boxed warnings for serious infection, malignancy, thromboembolism, cardiovascular events (MACE); preferred in patients failing TNF inhibitors; not preferred as first-line biologic in high-CV-risk patients per 2022 FDA/EMA guidance

**Glucocorticoids:**
- Prednisone (oral) or methylprednisolone (IV pulse) for bridging during DMARD initiation or flare management
- Intra-articular triamcinolone for monoarthritis flares
- Minimize long-term use: osteoporosis (bisphosphonate prophylaxis if >3 months at ≥7.5 mg/day), adrenal suppression, infection risk

## Connections

- `connects-to` → **[TNF-alpha](../../03-molecular/tnf-alpha/README.md)** — TNF-alpha is the master cytokine in RA synovitis; produced by synovial macrophages and FLS → drives NF-kB, MMP secretion, and RANKL-mediated bone erosion; anti-TNF biologics (adalimumab, etanercept, certolizumab) are the backbone of biologic DMARD therapy.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — IL-6 drives systemic RA inflammation (acute-phase response, anemia of chronic disease, fatigue) and Th17/Tfh polarization promoting ACPA production; tocilizumab and sarilumab (anti-IL-6R) are effective monotherapy or MTX-combination biologics for RA.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Th17 cells produce IL-17A/F driving neutrophil recruitment and FLS activation; Tfh cells sustain ACPA-producing plasma cell differentiation; abatacept (CTLA-4-Ig) blocks CD28 co-stimulation, suppressing pathogenic T-cell activation in RA synovium.
- `connects-to` → **[NF-kB](../../03-molecular/nf-kb/README.md)** — NF-kB activated in RA synovial fibroblasts and macrophages by TNF-alpha and IL-1beta → MMP secretion, RANKL induction, and osteoclast-driven bone erosion; glucocorticoids and multiple bDMARDs converge on NF-kB suppression as a shared downstream mechanism.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A is present in RA synovium but secondary to TNF-alpha and IL-6; IL-17A promotes osteoclastogenesis via RANKL induction; IL-17A inhibitors (secukinumab) failed pivotal RA trials; bimekizumab (anti-IL-17A/F) showed marginal RA benefit vs established TNF/IL-6 blockade.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5⁺ macrophages and Th1 cells are the dominant leukocyte populations in RA pannus; CCL3/CCL4/CCL5 (CCR5 ligands) are elevated in RA synovial fluid and correlate with disease activity; maraviroc (CCR5 antagonist) showed modest benefit in small RA trials, suggesting CCR5-mediated leukocyte recruitment contributes to synovitis.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 is the dominant synovial chemokine in RA: synoviocytes and FLS secrete CCL2 → CCR2+ monocyte/macrophage recruitment → pannus formation; synovial fluid CCL2 >5 ng/mL correlates with radiographic damage; macrophage-derived RANKL and MMPs drive joint destruction.
- `treated-by` → **[Ibuprofen](../../../03-medicine/01-modern/12-anti-inflammatory/ibuprofen/README.md)** — NSAIDs including ibuprofen reduce COX-2-driven synovial PGE₂ → less joint pain, swelling, and stiffness; adjuncts to DMARDs; reduce RA symptoms but not radiographic progression; long-term use requires GI prophylaxis (PPI).
- `treated-by` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — Prednisolone bridge therapy (5–10 mg/day) while DMARDs take effect (8–12 weeks latency); reduces radiographic progression in early RA (COBRA, BeSt trials); long-term use requires osteoporosis prophylaxis (bisphosphonate + calcium/vitamin D).
- `treated-by` → **[Adalimumab](../../../03-medicine/01-modern/11-biologics/adalimumab/README.md)** — fully human anti-TNFα IgG1 biologic; first-line for MTX-inadequate RA; ARMADA trial: ACR50 59% vs 24% at 24 weeks; halts radiographic progression; TB screening mandatory before initiation; concomitant MTX reduces immunogenicity.
- `connects-to` → **[Psoriatic Arthritis](../psoriatic-arthritis/README.md)** — Rheumatoid and psoriatic arthritis are the two major inflammatory arthritides but contrast: RA is a symmetric, RF/anti-CCP-positive synovitis sparing the DIP joints, while PsA is a seronegative spondyloarthropathy with enthesitis, dactylitis, DIP disease, and psoriasis.
- `connects-to` → **[Sjögren's Syndrome](../sjogrens-syndrome/README.md)** — Rheumatoid arthritis is the commonest disease complicated by secondary Sjögren's syndrome: chronic autoimmune inflammation extends to lacrimal and salivary glands, causing dry eyes and mouth (sicca), so RA patients are screened for the overlap.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Synovial fibroblasts are active drivers, not bystanders, of rheumatoid arthritis: activated fibroblast-like synoviocytes form the invasive pannus and secrete proteases and cytokines that erode cartilage and bone, behaving almost tumor-like—a therapeutic target.

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^smolen-2016-ra-lancet]: Smolen JS, Aletaha D, McInnes IB. Rheumatoid arthritis. *Lancet.* 2016;388(10055):2023-2038. [doi:10.1016/S0140-6736(16)30173-8](https://doi.org/10.1016/S0140-6736(16)30173-8) · [PubMed 27156434](https://pubmed.ncbi.nlm.nih.gov/27156434/)
[^firestein-2003-ra-pathogenesis]: Firestein GS. Evolving concepts of rheumatoid arthritis. *Nature.* 2003;423(6937):356-361. [doi:10.1038/nature01661](https://doi.org/10.1038/nature01661) · [PubMed 12748655](https://pubmed.ncbi.nlm.nih.gov/12748655/)
[^genovese-2016-baricitinib]: Genovese MC, Kremer J, Zamani O, et al. Baricitinib in Patients with Refractory Rheumatoid Arthritis. *N Engl J Med.* 2016;374(13):1243-1252. [doi:10.1056/NEJMoa1507247](https://doi.org/10.1056/NEJMoa1507247) · [PubMed 27028914](https://pubmed.ncbi.nlm.nih.gov/27028914/)

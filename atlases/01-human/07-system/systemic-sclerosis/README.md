---
schema: human-scale-entry/v1
id: systemic-sclerosis
name: Systemic Sclerosis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Systemic sclerosis (SSc) is an autoimmune CTD with vasculopathy (Raynaud's), autoantibodies (anti-Scl-70, anti-centromere, anti-RNA pol III), and progressive fibrosis of skin and viscera; limited (lcSSc) vs. diffuse (dcSSc); ILD and PAH are leading causes of death."
aliases: ["SSc", "scleroderma", "systemic scleroderma", "diffuse cutaneous systemic sclerosis", "dcSSc", "limited cutaneous systemic sclerosis", "lcSSc", "CREST syndrome", "anti-Scl-70", "anti-centromere antibody", "SSc-ILD", "SSc-PAH", "scleroderma renal crisis"]
sources:
  - id: denton-2017-ssc-review
    type: peer-reviewed
    cite: "Denton CP, Khanna D. Systemic sclerosis. Lancet. 2017;390(10103):1685-1699."
    doi: "10.1016/S0140-6736(17)30933-9"
    pmid: "28413064"
    url: "https://doi.org/10.1016/S0140-6736(17)30933-9"
  - id: distler-2019-nintedanib-senscis
    type: peer-reviewed
    cite: "Distler O, Highland KB, Gahlemann M, et al. Nintedanib for Systemic Sclerosis-Associated Interstitial Lung Disease. N Engl J Med. 2019;380(26):2518-2528."
    doi: "10.1056/NEJMoa1903076"
    pmid: "31112379"
    url: "https://doi.org/10.1056/NEJMoa1903076"
  - id: khanna-2016-tocilizumab-ssc
    type: peer-reviewed
    cite: "Khanna D, Denton CP, Jahreis A, et al. Safety and efficacy of subcutaneous tocilizumab in adults with systemic sclerosis (faSScinate): a phase 2, randomised, controlled trial. Lancet. 2016;387(10038):2630-2640."
    doi: "10.1016/S0140-6736(16)00932-X"
    pmid: "27156007"
    url: "https://doi.org/10.1016/S0140-6736(16)00932-X"
cross_links:
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β1 is the master profibrotic driver in SSc; dermal fibroblasts in dcSSc show constitutive pSMAD2/3 activation → ↑COL1A1, COL3A1, fibronectin, and CTGF; nintedanib (SENSCIS trial) targets PDGFR/VEGFR/FGFR; TGF-β blockade remains a therapeutic target."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "PAH occurs in 10-15% of SSc (especially lcSSc with anti-centromere antibodies); SSc-PAH is treated identically to IPAH with ERAs + PDE5i; macitentan, ambrisentan, and tadalafil are first-line; SSc-PAH has worse prognosis than IPAH due to concurrent cardiac and pulmonary fibrosis."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 is elevated in SSc serum and drives fibrosis via STAT3 → ↑TGF-β and connective tissue growth factor; tocilizumab (anti-IL-6R) slowed FVC decline in SSc-ILD in the focuSSed trial; IL-6 levels correlate with skin score and ILD activity."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Type I IFN signature elevated in ~50% of SSc, especially anti-RNA pol III+ dcSSc; IFN-α activates plasmacytoid DCs → amplifies anti-nuclear antibodies; type I IFN + TGF-β cooperate to drive SSc fibroblast activation and ILD progression."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Skin fibrosis names systemic sclerosis: TGF-β-activated myofibroblasts deposit collagen, producing taut, hide-bound dermis graded by the modified Rodnan skin score; limited cutaneous SSc spares the trunk while diffuse SSc thickens proximal limbs, predicting organ involvement."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "The effector cell of systemic sclerosis is the myofibroblast (α-SMA+, contractile), driven by TGF-β/SMAD2-3 to oversecrete collagen; in SSc it becomes autonomously fibrogenic through epigenetic FLI1 silencing and persists even without ongoing TGF-β, sustaining fibrosis."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Scleroderma renal crisis strikes ~10-15% of diffuse SSc (especially anti-RNA-pol-III+) as malignant hypertension with onion-skin arterioles and hemolytic anemia; ACE inhibitors are the only proven therapy, and corticosteroids must be avoided as they can precipitate it."
  - target: 01-human/07-system/sjogrens-syndrome
    relation: connects-to
    note: "Systemic sclerosis and Sjögren's are overlapping connective-tissue autoimmune diseases: secondary Sjögren occurs in up to ~20% of SSc, adding sicca to the fibrosis, and both share a type-I-interferon signature — but SSc is defined by vasculopathy and collagen deposition."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lung is the leading cause of death in systemic sclerosis: interstitial lung disease (fibrotic NSIP, worst with anti-Scl-70) scars the lower lobes and pulmonary arterial hypertension narrows vessels; nintedanib and tocilizumab slow the ILD, so CT and PFT surveillance matter."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Endothelial injury is the first event in systemic sclerosis: damaged microvascular endothelium triggers Raynaud's phenomenon, digital ulcers, and capillary dropout (on nailfold capillaroscopy), then activates fibroblasts — making vasculopathy the initiating arm of the SSc triad."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Systemic sclerosis and lupus are both ANA-positive connective tissue diseases that can overlap as mixed connective tissue disease: SSc is dominated by fibrosis (anti-Scl-70), lupus by immune-complex inflammation (anti-dsDNA), but both share Raynaud's and interferon."
  - target: 01-human/07-system/dermatomyositis
    relation: connects-to
    note: "Systemic sclerosis and dermatomyositis overlap in scleromyositis: some patients have both skin fibrosis and inflammatory myopathy, marked by anti-PM/Scl antibodies, so muscle weakness in a scleroderma patient prompts evaluation for a myositis overlap."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "The gut is involved in most systemic sclerosis: fibrosis and smooth-muscle atrophy cause esophageal dysmotility and reflux, gastric antral vascular ectasia, small-bowel bacterial overgrowth, and pseudo-obstruction—a major source of morbidity beyond the skin."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Systemic sclerosis and rheumatoid arthritis are both systemic autoimmune connective-tissue diseases but differ in target: SSc is dominated by fibrosis and vasculopathy (skin, lung, gut), while RA is an inflammatory synovitis—though the two can overlap in some patients."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Systemic sclerosis is fundamentally a disease of excess collagen: TGF-β-activated fibroblasts overproduce and deposit collagen in skin, lung and other organs, hardening tissue and strangling small vessels—a structural protein becoming the agent of organ failure."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Vascular smooth muscle drives the vasculopathy of systemic sclerosis: endothelial injury and smooth-muscle proliferation narrow small arteries, producing Raynaud's, pulmonary hypertension and renal crisis—the vascular, not just fibrotic, face of the disease."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Systemic sclerosis is the prototypical multi-organ fibrosis: the same fibroblast-driven scarring that heals a wound runs unchecked across skin, lung and gut, so SSc anchors the broader family of fibrotic diseases and is a testbed for antifibrotic drugs like nintedanib."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "The heart is a hidden but lethal systemic sclerosis target: myocardial fibrosis and microvascular disease cause arrhythmias, conduction block and heart failure, often silent until advanced—so cardiac involvement is a leading cause of death in scleroderma."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Endothelin-1 drives the vasculopathy of systemic sclerosis: this potent vasoconstrictor, overproduced by injured endothelium, fuels Raynaud's phenomenon and pulmonary hypertension—so endothelin-receptor blockers (bosentan) treat the vascular side of the disease."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Systemic sclerosis is fundamentally autoimmune: specific autoantibodies (anti-Scl-70, anti-centromere) define subsets and predict organ risk, and severe cases are treated by resetting the immune system with autologous stem-cell transplant."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "B cells drive systemic sclerosis beyond autoantibodies: they secrete pro-fibrotic IL-6 and activate fibroblasts, so rituximab (anti-CD20 B-cell depletion) is increasingly used to slow skin and lung fibrosis in progressive disease."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Helper T cells orchestrate the fibrosis of systemic sclerosis: Th2 and Th17 cytokines (IL-4, IL-13, IL-17) push fibroblasts toward collagen overproduction, linking the adaptive immune response directly to the tissue scarring that defines the disease."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Scleroderma renal crisis is an angiotensin-II emergency: sudden malignant hypertension and kidney failure from activated renin-angiotensin once killed many patients, but ACE inhibitors blocking angiotensin II converted it into a treatable complication."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcinosis is the 'C' of CREST in systemic sclerosis: calcium deposits in skin and soft tissue form painful, sometimes ulcerating nodules, one of the hallmark features of limited cutaneous disease alongside Raynaud's and esophageal involvement."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Systemic sclerosis vasculopathy reflects lost nitric oxide: damaged endothelium makes too little NO and too much endothelin, so vessels constrict—driving Raynaud's, digital ulcers and pulmonary hypertension treated with vasodilators that restore NO signaling."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Systemic sclerosis fibrosis is driven by PDGF: the growth factor (and stimulatory anti-PDGFR antibodies) push fibroblasts into collagen-spewing myofibroblasts, so PDGFR-blocking drugs like nintedanib slow the lung scarring."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Systemic sclerosis is fibrosed by M2 macrophages: alternatively-activated macrophages flood the skin and lung and secrete TGF-beta and other signals that drive the relentless collagen deposition central to the disease."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells mark early systemic sclerosis: they accumulate in affected skin and release mediators that activate fibroblasts and inflame vessels, contributing to both the fibrosis and the Raynaud's vasculopathy of the disease."
---

# Systemic Sclerosis

## Overview

**Systemic sclerosis (SSc; scleroderma)** is a systemic autoimmune connective tissue disease characterized by the triad of **vasculopathy**, **autoimmunity** (antinuclear antibodies), and **progressive fibrosis** of the skin and internal organs [^denton-2017-ssc-review]. It is the most severe of the systemic rheumatic diseases, with a standardized mortality ratio 3-5× the general population due to cardiopulmonary complications.

**Epidemiology:**
- Incidence: 2-10 per 100,000 per year; prevalence ~250-300 per 100,000 in the US
- Female predominance (F:M ~4:1); peak onset age 30-50 years
- Higher prevalence in Black women (earlier onset, more severe dcSSc)
- Choctaw Native Americans: highest known prevalence (~469/100,000) due to founder FIBRILLIN-1 variant

**Classification — two major subtypes:**

| Feature | Limited SSc (lcSSc) | Diffuse SSc (dcSSc) |
|---|---|---|
| Skin involvement | Distal to elbows/knees; face | Trunk, proximal limbs; face |
| Time from Raynaud's to fibrosis | Years (Raynaud's may precede by decades) | Months |
| Key autoantibodies | Anti-centromere (anti-CENP-B, 70-80%) | Anti-Scl-70 (anti-topo I, 20-40%); anti-RNA pol III (10-25%) |
| Pulmonary hypertension | PAH more common (~15%) | SSc-ILD more severe |
| Renal crisis | Rare | 10-15% (especially anti-RNA pol III+) |
| Calcinosis | Common (CREST) | Less common |
| Prognosis | Slower progression; better 10-year survival | More rapid organ damage |

**CREST syndrome** (Calcinosis, Raynaud's, Esophageal dysmotility, Sclerodactyly, Telangiectasia) — now considered a subset of lcSSc; anti-centromere antibody characteristic.

## Structure

### Pathogenesis — the triad of vasculopathy, autoimmunity, and fibrosis

SSc pathogenesis proceeds through three interconnected arms:

**1. Vasculopathy — Raynaud's phenomenon and beyond:**
- **Raynaud's phenomenon (RP):** Episodic vasospasm of digital arteries in response to cold or stress → triphasic color change (white/blue/red); >95% of SSc patients; often the presenting symptom, preceding other manifestations by months-decades
- Structural vascular damage: endothelial cell apoptosis → subintimal fibrosis → luminal narrowing → fixed ischemia → digital ulcers, pitting scars, gangrene
- **Nailfold capillaroscopy:** Hallmark diagnostic tool; "SSc pattern" = enlarged/giant capillaries + avascular areas + hemorrhages; distinguishes SSc-RP from primary RP
- Mediators: ET-1 ↑, NO ↓ (impaired eNOS), VEGF paradoxically elevated but ineffective due to receptor downregulation

**2. Autoimmunity — antinuclear antibodies:**
- **Anti-Scl-70 (anti-topoisomerase I; anti-topo I):** Target: DNA topoisomerase I (130 kDa nuclear protein); ~20-40% of SSc; strongly predicts diffuse skin disease and ILD; mutually exclusive with anti-centromere
- **Anti-centromere antibody (ACA; anti-CENP-B):** Target: centromere protein B; ~70-80% of lcSSc; predicts PAH and primary biliary cholangitis overlap
- **Anti-RNA polymerase III (anti-RNAP III):** Target: RNA pol III largest subunit; ~10-25% of SSc; strongly predicts scleroderma renal crisis and rapid dcSSc skin progression; associated with cancer-triggered SSc (coincident cancer ~18%)
- **Anti-fibrillarin (anti-U3-RNP):** Severe dcSSc with musculoskeletal and cardiac involvement
- **Anti-PM/Scl:** SSc-myositis overlap; anti-NOR-90, anti-Th/To: SSc-PAH overlap

**3. Fibrosis — myofibroblast activation:**
- Sequence: Injury/autoimmunity → macrophage M2 polarization → TGF-β1/PDGF secretion → fibroblast → **myofibroblast** (α-SMA+, contractile, high collagen secretion)
- TGF-β1 → SMAD2/3 phosphorylation → SMAD2/3-SMAD4 complex → nucleus → ↑COL1A1, COL1A2, COL3A1, fibronectin (EDA-FN), connective tissue growth factor (CTGF/CCN2)
- **Myofibroblast persistence** in SSc: epigenetic silencing of FLI1 (transcription factor that suppresses collagen) + DNMT3A-mediated hypomethylation of TGF-β-responsive genes → autonomous fibrogenic program even without ongoing TGF-β stimulus
- Type I IFN amplifies this process by activating pDCs → more autoantibody production → more tissue injury → more TGF-β

### Modified Rodnan Skin Score (mRSS)

Standard clinical measure: 17 body areas each scored 0-3 (0 = normal, 3 = hide-bound) → maximum score 51; primary endpoint in dcSSc trials. mRSS correlates with PVR, FVC, and mortality in dcSSc.

## Function

### Organ manifestations and treatment

**Interstitial Lung Disease (SSc-ILD):**
- Most common cause of death in SSc (~35% of SSc deaths); prevalence ~60% of dcSSc, ~35% of lcSSc by HRCT
- Pattern: Non-specific interstitial pneumonia (NSIP) most common (ground-glass + fine reticulation, spares periphery); UIP pattern in ~10-15% (worse prognosis)
- Treatment:
  - **Mycophenolate mofetil (MMF):** SLS-II trial (equivalent to oral cyclophosphamide with better tolerability); current first-line for SSc-ILD
  - **Nintedanib (Ofev):** Tyrosine kinase inhibitor targeting PDGFR-α/β, VEGFR-1/2/3, FGFR-1/2/3; SENSCIS trial (576 patients): −44.9 mL/year FVC decline vs. −87.9 mL/year placebo (p<0.001); FDA approved for SSc-ILD in 2019 [^distler-2019-nintedanib-senscis]
  - **Tocilizumab (Actemra):** Anti-IL-6R; faSScinate Phase 2 (skin score improvement, trend toward FVC benefit); focuSSed Phase 3: slowed FVC decline −4.2 vs. −6.3 mL/year (not statistically significant primary endpoint but numerically meaningful)
  - **Rituximab:** Anti-CD20; observational data suggesting SSc-ILD stabilization; SLS-III Phase 3 ongoing

**Pulmonary Arterial Hypertension (SSc-PAH):**
- 10-15% of SSc patients; SSc is the most common cause of CTD-PAH
- Annual echocardiographic screening for all SSc patients; confirmed by RHC (mPAP >20 mmHg + PVR ≥2 WU + PAWP ≤15 mmHg)
- Treatment: ERAs + PDE5i (same as IPAH); macitentan, ambrisentan + tadalafil (AMBITION regimen)
- SSc-PAH prognosis worse than IPAH: 3-year survival ~55-60% vs. >80% in IPAH

**Scleroderma Renal Crisis (SRC):**
- ~10-15% of dcSSc, especially anti-RNA pol III+ patients; onset typically within 5 years of diagnosis
- Pathophysiology: renal arteriolar intimal proliferation (onion-skin lesion) → ischemia → renin release → accelerated hypertension → microangiopathic hemolytic anemia
- Presentation: acute hypertensive emergency (often sudden severe HTN), AKI, microangiopathy (thrombocytopenia, schistocytes)
- **Treatment: ACE inhibitors** (captopril, enalapril) — the only therapy proven to improve outcomes; 50% still progress to ESRD despite treatment; avoid corticosteroids (precipitate SRC)

**Gastrointestinal:**
- Esophageal dysmotility: most common GI manifestation (>90%); smooth muscle atrophy → impaired LES function → GERD → Barrett's esophagus risk; treat with PPI + prokinetics
- Small bowel: dysmotility → bacterial overgrowth (chronic diarrhea, malabsorption, weight loss); antibiotic rotation (rifaximin, metronidazole, ciprofloxacin)
- Gastric antral vascular ectasia (GAVE; "watermelon stomach"): endoscopic ablation

**Musculoskeletal:**
- Inflammatory arthritis, tendon friction rubs (hallmark of active dcSSc — "leather rubbing" on exam), myopathy, calcinosis cutis (CREST)

**Cardiac:**
- Pericardial effusion; myocardial fibrosis → diastolic dysfunction → arrhythmias; coronary vasospasm

## Pathology

**Skin fibrosis (dcSSc):**
Dermis shows marked collagen accumulation, loss of adnexal structures (sweat glands, hair follicles), and perivascular lymphocytic infiltrate in early stages. Late stage: "hide-bound" dermis — grossly thickened, tethered skin; impairs joint mobility.

**Pulmonary NSIP pattern:**
HRCT: Bilateral basal-predominant ground-glass opacity with fine reticulation; traction bronchiectasis in established fibrosis; subpleural sparing distinguishes NSIP from UIP. Histology: temporally uniform inflammation and fibrosis.

**SSc-PAH vascular pathology:**
Identical to IPAH: medial hypertrophy, intimal fibrosis, concentric laminar intimal fibrosis, plexiform lesions. SSc-PAH additionally shows pericapillary fibrosis.

**Autoantibody-associated disease risk (clinical use):**

| Autoantibody | SSc subtype | Associated manifestation |
|---|---|---|
| Anti-Scl-70 (topo I) | dcSSc | ILD (high risk); FVC monitoring required |
| Anti-centromere (CENP-B) | lcSSc | PAH; primary biliary cholangitis overlap |
| Anti-RNA pol III | dcSSc | Scleroderma renal crisis; cancer association |
| Anti-fibrillarin (U3-RNP) | dcSSc | Severe multiorgan; musculoskeletal |
| Anti-PM/Scl | SSc-myositis overlap | Myositis; ILD |
| Anti-Th/To | lcSSc | PAH; SSc-PBC overlap |

## Connections

- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — TGF-β1 is the master profibrotic driver in SSc; dermal fibroblasts in dcSSc show constitutive pSMAD2/3 activation → ↑COL1A1, COL3A1, fibronectin, and CTGF; nintedanib (SENSCIS trial) targets PDGFR/VEGFR/FGFR; TGF-β blockade remains a therapeutic target.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — PAH occurs in 10-15% of SSc (especially lcSSc with anti-centromere antibodies); SSc-PAH is treated identically to IPAH with ERAs + PDE5i; macitentan, ambrisentan, and tadalafil are first-line; SSc-PAH has worse prognosis than IPAH due to concurrent cardiac and pulmonary fibrosis.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — IL-6 is elevated in SSc serum and drives fibrosis via STAT3 → ↑TGF-β and connective tissue growth factor; tocilizumab (anti-IL-6R) slowed FVC decline in SSc-ILD in the focuSSed trial; IL-6 levels correlate with skin score and ILD activity.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Type I IFN signature elevated in ~50% of SSc, especially anti-RNA pol III+ dcSSc; IFN-α activates plasmacytoid DCs → amplifies anti-nuclear antibodies; type I IFN + TGF-β cooperate to drive SSc fibroblast activation and ILD progression.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Skin fibrosis names systemic sclerosis: TGF-β-activated myofibroblasts deposit collagen, producing taut, hide-bound dermis graded by the modified Rodnan skin score; limited cutaneous SSc spares the trunk while diffuse SSc thickens proximal limbs, predicting organ involvement.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — The effector cell of systemic sclerosis is the myofibroblast (α-SMA+, contractile), driven by TGF-β/SMAD2-3 to oversecrete collagen; in SSc it becomes autonomously fibrogenic through epigenetic FLI1 silencing and persists even without ongoing TGF-β, sustaining fibrosis.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Scleroderma renal crisis strikes ~10-15% of diffuse SSc (especially anti-RNA-pol-III+) as malignant hypertension with onion-skin arterioles and hemolytic anemia; ACE inhibitors are the only proven therapy, and corticosteroids must be avoided as they can precipitate it.
- `connects-to` → **[Sjögren's Syndrome](../sjogrens-syndrome/README.md)** — Systemic sclerosis and Sjögren's are overlapping connective-tissue autoimmune diseases: secondary Sjögren occurs in up to ~20% of SSc, adding sicca to the fibrosis, and both share a type-I-interferon signature — but SSc is defined by vasculopathy and collagen deposition.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lung is the leading cause of death in systemic sclerosis: interstitial lung disease (fibrotic NSIP, worst with anti-Scl-70) scars the lower lobes and pulmonary arterial hypertension narrows vessels; nintedanib and tocilizumab slow the ILD, so CT and PFT surveillance matter.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Endothelial injury is the first event in systemic sclerosis: damaged microvascular endothelium triggers Raynaud's phenomenon, digital ulcers, and capillary dropout (on nailfold capillaroscopy), then activates fibroblasts — making vasculopathy the initiating arm of the SSc triad.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — Systemic sclerosis and lupus are both ANA-positive connective tissue diseases that can overlap as mixed connective tissue disease: SSc is dominated by fibrosis (anti-Scl-70), lupus by immune-complex inflammation (anti-dsDNA), but both share Raynaud's and interferon.
- `connects-to` → **[Dermatomyositis](../dermatomyositis/README.md)** — Systemic sclerosis and dermatomyositis overlap in scleromyositis: some patients have both skin fibrosis and inflammatory myopathy, marked by anti-PM/Scl antibodies, so muscle weakness in a scleroderma patient prompts evaluation for a myositis overlap.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — The gut is involved in most systemic sclerosis: fibrosis and smooth-muscle atrophy cause esophageal dysmotility and reflux, gastric antral vascular ectasia, small-bowel bacterial overgrowth, and pseudo-obstruction—a major source of morbidity beyond the skin.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Systemic sclerosis and rheumatoid arthritis are both systemic autoimmune connective-tissue diseases but differ in target: SSc is dominated by fibrosis and vasculopathy (skin, lung, gut), while RA is an inflammatory synovitis—though the two can overlap in some patients.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Systemic sclerosis is fundamentally a disease of excess collagen: TGF-β-activated fibroblasts overproduce and deposit collagen in skin, lung and other organs, hardening tissue and strangling small vessels—a structural protein becoming the agent of organ failure.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Vascular smooth muscle drives the vasculopathy of systemic sclerosis: endothelial injury and smooth-muscle proliferation narrow small arteries, producing Raynaud's, pulmonary hypertension and renal crisis—the vascular, not just fibrotic, face of the disease.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Systemic sclerosis is the prototypical multi-organ fibrosis: the same fibroblast-driven scarring that heals a wound runs unchecked across skin, lung and gut, so SSc anchors the broader family of fibrotic diseases and is a testbed for antifibrotic drugs like nintedanib.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — The heart is a hidden but lethal systemic sclerosis target: myocardial fibrosis and microvascular disease cause arrhythmias, conduction block and heart failure, often silent until advanced—so cardiac involvement is a leading cause of death in scleroderma.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Endothelin-1 drives the vasculopathy of systemic sclerosis: this potent vasoconstrictor, overproduced by injured endothelium, fuels Raynaud's phenomenon and pulmonary hypertension—so endothelin-receptor blockers (bosentan) treat the vascular side of the disease.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Systemic sclerosis is fundamentally autoimmune: specific autoantibodies (anti-Scl-70, anti-centromere) define subsets and predict organ risk, and severe cases are treated by resetting the immune system with autologous stem-cell transplant.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — B cells drive systemic sclerosis beyond autoantibodies: they secrete pro-fibrotic IL-6 and activate fibroblasts, so rituximab (anti-CD20 B-cell depletion) is increasingly used to slow skin and lung fibrosis in progressive disease.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Helper T cells orchestrate the fibrosis of systemic sclerosis: Th2 and Th17 cytokines (IL-4, IL-13, IL-17) push fibroblasts toward collagen overproduction, linking the adaptive immune response directly to the tissue scarring that defines the disease.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — Scleroderma renal crisis is an angiotensin-II emergency: sudden malignant hypertension and kidney failure from activated renin-angiotensin once killed many patients, but ACE inhibitors blocking angiotensin II converted it into a treatable complication.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcinosis is the 'C' of CREST in systemic sclerosis: calcium deposits in skin and soft tissue form painful, sometimes ulcerating nodules, one of the hallmark features of limited cutaneous disease alongside Raynaud's and esophageal involvement.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Systemic sclerosis vasculopathy reflects lost nitric oxide: damaged endothelium makes too little NO and too much endothelin, so vessels constrict—driving Raynaud's, digital ulcers and pulmonary hypertension treated with vasodilators that restore NO signaling.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Systemic sclerosis fibrosis is driven by PDGF: the growth factor (and stimulatory anti-PDGFR antibodies) push fibroblasts into collagen-spewing myofibroblasts, so PDGFR-blocking drugs like nintedanib slow the lung scarring.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Systemic sclerosis is fibrosed by M2 macrophages: alternatively-activated macrophages flood the skin and lung and secrete TGF-beta and other signals that drive the relentless collagen deposition central to the disease.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells mark early systemic sclerosis: they accumulate in affected skin and release mediators that activate fibroblasts and inflame vessels, contributing to both the fibrosis and the Raynaud's vasculopathy of the disease.

[^denton-2017-ssc-review]: Denton CP, Khanna D. Systemic sclerosis. *Lancet.* 2017;390(10103):1685-1699. [doi:10.1016/S0140-6736(17)30933-9](https://doi.org/10.1016/S0140-6736(17)30933-9) · [PubMed 28413064](https://pubmed.ncbi.nlm.nih.gov/28413064/)
[^distler-2019-nintedanib-senscis]: Distler O, Highland KB, Gahlemann M, et al. Nintedanib for Systemic Sclerosis-Associated Interstitial Lung Disease. *N Engl J Med.* 2019;380(26):2518-2528. [doi:10.1056/NEJMoa1903076](https://doi.org/10.1056/NEJMoa1903076) · [PubMed 31112379](https://pubmed.ncbi.nlm.nih.gov/31112379/)
[^khanna-2016-tocilizumab-ssc]: Khanna D, Denton CP, Jahreis A, et al. Safety and efficacy of subcutaneous tocilizumab in adults with systemic sclerosis (faSScinate): a phase 2, randomised, controlled trial. *Lancet.* 2016;387(10038):2630-2640. [doi:10.1016/S0140-6736(16)00932-X](https://doi.org/10.1016/S0140-6736(16)00932-X) · [PubMed 27156007](https://pubmed.ncbi.nlm.nih.gov/27156007/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

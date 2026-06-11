---
schema: human-scale-entry/v1
id: gvhd
name: Graft-Versus-Host Disease
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "GvHD occurs when donor T cells recognize host alloantigens after allogeneic HSCT; acute (skin, gut, liver, <100 days) vs. chronic (fibrotic, >100 days). IL-10/Treg axis is protective; ruxolitinib (JAK1/2) is the approved steroid-refractory treatment."
aliases: ["GvHD", "graft versus host disease", "GVHD", "acute GvHD", "chronic GvHD", "aGvHD", "cGvHD"]
sources:
  - id: ferrara-2009-gvhd-review
    type: peer-reviewed
    cite: "Ferrara JL, Levine JE, Reddy P, Holler E. Graft-versus-host disease. Lancet. 2009;373(9674):1550-1561."
    doi: "10.1016/S0140-6736(09)60237-3"
    pmid: "19380114"
    url: "https://doi.org/10.1016/S0140-6736(09)60237-3"
  - id: zeiser-2020-ruxolitinib-gvhd-reach
    type: peer-reviewed
    cite: "Zeiser R, von Bubnoff N, Butler J, et al. Ruxolitinib for Glucocorticoid-Refractory Acute Graft-versus-Host Disease. N Engl J Med. 2020;382(19):1800-1810."
    doi: "10.1056/NEJMoa1917635"
    pmid: "32374962"
    url: "https://doi.org/10.1056/NEJMoa1917635"
  - id: przepiorka-2020-ruxolitinib-cgvhd-reach3
    type: peer-reviewed
    cite: "Przepiorka D, Luo L, Subramaniam S, et al. FDA Approval Summary: Ruxolitinib for Treatment of Chronic Graft-versus-Host Disease. Oncologist. 2022;27(2):98-104."
    doi: "10.1093/oncolo/oyab055"
    pmid: "35641197"
    url: "https://doi.org/10.1093/oncolo/oyab055"
cross_links:
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Treg-derived IL-10 is the dominant immunosuppressive brake on alloreactive donor T cells post-HSCT; low circulating IL-10 and IL-10R polymorphisms predict GvHD severity; IL-10 gene transfer and IL-10-secreting Treg infusions are investigational GvHD prevention strategies."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "GvHD originates from allogeneic bone marrow or peripheral blood stem cell transplantation; donor hematopoietic stem cell engraftment is required for GvHD to occur; the bone marrow niche is reshaped by donor-derived immune reconstitution, influencing GvHD vs. GvL balance."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 is a central amplifier of acute GvHD: conditioning regimen tissue damage releases DAMPs → IL-6 from host APCs → JAK1/STAT3 in donor T cells → Th17 polarization + survival signals; tocilizumab (anti-IL-6R) is studied as GvHD prophylaxis in clinical trials."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Alloreactive donor CD4+ Th1 cells are the central drivers of acute GvHD: IL-12+IFN-γ drives Th1 polarization; IL-6+TGF-β drives Th17; donor T helper cells recognize host alloantigens via direct (host MHC mismatch) and indirect (host peptides on donor APCs) pathways."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Donor CD8+ CTLs are the primary effectors of target organ damage in acute GvHD: recognize host MHC-I mismatch → perforin/granzyme-mediated killing of skin basal keratinocytes, GI crypt ISCs, and biliary epithelium → grade III/IV GvHD is the leading cause of non-relapse mortality."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "Gut microbiome diversity at transplant predicts GvHD severity; Akkermansia muciniphila and Blautia spp. are protective — loss of butyrate-producing bacteria reduces Treg support; antibiotic dysbiosis → loss of SCFAs → increased GvHD risk; FMT is investigational for GvHD rescue."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Skin is the first and most common target of acute graft-versus-host disease: donor CD8 T cells kill basal keratinocytes, producing a maculopapular rash that can progress to bullae, while chronic GvHD turns the skin lichenoid and sclerodermatous."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Ruxolitinib, a JAK1/JAK2 inhibitor, is the approved treatment for steroid-refractory graft-versus-host disease, both acute and chronic: by blocking JAK-STAT signaling downstream of IL-6, IFN-γ, and IL-12 it suppresses Th1/Th17 effectors while sparing regulatory T cells."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Donor regulatory T cells are the protective counterweight in GvHD: through IL-10 and TGF-β they restrain alloreactive effector T cells, and the graft's Treg-to-conventional-T ratio predicts tolerance versus disease — the rationale behind post-transplant cyclophosphamide."
---

# Graft-Versus-Host Disease

## Overview

**Graft-versus-host disease (GvHD)** is the leading cause of non-relapse morbidity and mortality after **allogeneic hematopoietic stem cell transplantation (allo-HSCT)**, occurring when immunologically competent donor T cells recognize and attack the tissues of an immunologically distinct host [^ferrara-2009-gvhd-review].

GvHD occurs in two biologically distinct forms:
- **Acute GvHD (aGvHD):** Classically defined as occurring within **100 days** post-transplant (though now recognized by clinical syndrome rather than timing); targets skin, gastrointestinal tract, and liver; characterized by donor T cell cytotoxicity and pro-inflammatory cytokine storm
- **Chronic GvHD (cGvHD):** Occurring after day 100 (or earlier with overlap syndrome); resembles fibrotic autoimmune disorders (scleroderma, Sjögren's syndrome, primary biliary cirrhosis analogues); targets skin/fascia, mouth, eyes, lungs, joints, and liver; involves dysregulated B cell and Th2/Th17 responses

**Incidence and impact:**
- Allo-HSCT performed in ~30,000 patients/year in the US; GvHD incidence: ~30-50% acute (grade II-IV), ~40-70% chronic
- Grade III-IV acute GvHD: ~15-20%; associated with 80-90% 2-year mortality without effective treatment
- 5-year non-relapse mortality from chronic GvHD: ~20-30% in high-risk patients
- Annual US cost of GvHD management: >$500 million

**The GvL trade-off:** Donor T cells cause GvHD, but also mediate the **graft-versus-leukemia (GvL)** effect — direct allograft T cell cytotoxicity against residual leukemic/lymphoma cells. Strategies to prevent GvHD (T cell depletion, immunosuppression) inevitably reduce GvL, increasing relapse risk. This fundamental biological tension defines the central challenge of allogeneic transplantation.

## Structure

### Three-phase pathogenesis model (Ferrara model)

**Phase 1 — Tissue damage and APC activation (afferent phase):**
- Pre-transplant conditioning regimen (total body irradiation, high-dose chemotherapy) → GI mucosal damage → bacterial product translocation (LPS, flagellin, peptidoglycan) + host DAMP release (HMGB1, heat shock proteins, ATP)
- Host antigen-presenting cells (APCs: macrophages, DCs) activated via TLR4/TLR5/TLR2 → ↑IL-6, IL-1β, TNF-α, IL-12; ↑MHC class I/II expression; ↑CD80/86 costimulation
- **Host APC priming of donor T cells** is the critical initial event

**Phase 2 — T cell activation and expansion (central phase):**
- Donor naïve CD4+ and CD8+ T cells recognize **host alloantigens** (direct pathway: foreign donor MHC complexes; indirect pathway: host-derived peptides on donor APCs)
- IL-12 + IFN-γ → **Th1 differentiation**; IL-6 + TGF-β → **Th17 differentiation**
- CD8+ CTL → recognize host MHC class I mismatch → kill host epithelium via perforin/granzyme and Fas-FasL
- Cytokine amplification: **TNF-α** (from donor Th1 + host macrophages) → NF-κB → IL-6, IL-8, IL-1β; **IFN-γ** → CXCL9/CXCL10 → further CTL recruitment
- Protective countercurrent: donor-derived **Foxp3+ Tregs** secrete **IL-10** and **TGF-β** → suppress alloreactive T cells; Treg:Tconv ratio in graft is the key determinant of GvHD vs. tolerance

**Phase 3 — Target organ damage (efferent phase):**
- **Skin:** CD8+ T cell-mediated basal keratinocyte apoptosis → grade I (maculopapular rash) → grade IV (bullous dermatitis); satellitosis (single-cell lymphocytic apoptosis) on biopsy
- **GI tract:** Crypt apoptosis → loss of intestinal stem cells → diarrhea (secretary + bloody) → grade III/IV GvHD carries >80% mortality without salvage; gut is the primary determinant of aGvHD lethality
- **Liver:** Donor T cell injury to biliary epithelium → cholestatic hepatitis (↑bilirubin, alkaline phosphatase) → grade IV → hepatic failure

### Grading systems

**Acute GvHD — Overall grade (Glucksberg/Harris):**
- Grade I: Skin only (stage 1-2); no functional impairment
- Grade II: Skin stage 3, or liver bilirubin 2-3 mg/dL, or GI diarrhea 500-1000 mL/day; mild functional impairment
- Grade III: Skin/liver/GI involvement; marked functional impairment
- Grade IV: Generalized erythroderma ± bullae; bilirubin >15 mg/dL; diarrhea >1500 mL/day; severe functional impairment

**Chronic GvHD — NIH scoring:**
- NIH Consensus Criteria (2005, revised 2014): Organ-specific scoring (skin, mouth, eyes, GI, liver, lungs, joints/fascia, genitalia) → overall: mild/moderate/severe
- Key differentiating features from aGvHD: lichen planus-like changes, scleroderma, bronchiolitis obliterans (BO), dry eyes (keratoconjunctivitis sicca)

### Risk factors

- **HLA mismatch:** Fully matched 10/10 (HLA-A, B, C, DRB1, DQB1) vs. 9/10 or lower → progressively higher GvHD risk
- **Unrelated donor** vs. matched sibling: ×2-3 higher GvHD risk
- **Graft source:** Peripheral blood stem cells (PBSC) > bone marrow > cord blood for chronic GvHD risk
- **Conditioning intensity:** Myeloablative conditioning > reduced-intensity conditioning → more tissue damage → more phase 1 danger signals
- **CMV serostatus mismatch** and **older recipient age** → higher GvHD risk
- **Microbiome diversity:** High gut microbiome diversity at transplant → lower GvHD risk (clinical trial data; Akkermansia muciniphila, Blautia spp. protective)

## Function

### Prevention strategies

**Calcineurin inhibitor–based prophylaxis (standard of care):**
- **Tacrolimus** (FK506) + **methotrexate** (MTX): most widely used backbone; tacrolimus inhibits calcineurin → ↓NFAT → ↓IL-2 transcription → T cell activation blockade; MTX kills rapidly proliferating T cells
- **Cyclosporine + MTX:** Alternative; similar efficacy to tacrolimus + MTX in matched sibling transplants
- Post-transplant cyclophosphamide (**PT-Cy; BuCyPT**): High-dose Cy on days +3/+4 → kills proliferating alloreactive T cells while sparing slowly dividing Tregs → profoundly reduces GvHD; now standard for haploidentical (half-matched) transplants and increasingly used in MUD transplants

**PTCy mechanism:** Donor alloreactive T cells proliferate rapidly (day 3-4 after infusion) → high cyclophosphamide sensitivity via aldehyde dehydrogenase (ALDH) low expression; Tregs express high ALDH → PTCy preferentially kills alloreactive Teffs, spares Tregs → immune reconstitution weighted toward tolerance

### Treatment — Acute GvHD

**First-line: Corticosteroids:**
- Methylprednisolone 1-2 mg/kg/day; ~50% complete response rate; steroid-refractory (SR) in ~50% of patients (response day 5-7 defines SR)
- Mechanism: glucocorticoid receptor → ↓NF-κB + AP-1 → broad anti-inflammatory; apoptosis of activated T cells

**Second-line steroid-refractory aGvHD:**

**Ruxolitinib (Jakafi; JAK1/2 inhibitor; Incyte)** [^zeiser-2020-ruxolitinib-gvhd-reach]:
- **REACH2 trial** (Phase 3): Ruxolitinib 10 mg BID vs. investigator's choice (BAT; 7 options including MMF, infliximab, etanercept, tacrolimus) in SR aGvHD grade II-IV
- **Day 28 ORR: 62% vs. 39%** (OR 2.64, p<0.001); CR 34% vs. 19%; durable ORR at day 56: 40% vs. 22%
- Mechanism: JAK1/JAK2 inhibition → ↓STAT3/STAT5 → ↓IL-2, IL-6, IL-12, IFN-γ signaling → suppression of Th1/Th17 effector programs; also increases Treg proportion
- **FDA approval: May 2019** for SR acute GvHD ≥12 years old (first approved second-line agent)
- Adverse effects: anemia (Hgb ↓), thrombocytopenia, CMV reactivation (monitor PCR); secondary viral infections

**Ruxolitinib for chronic GvHD (REACH3):**
- SR chronic GvHD: Ruxolitinib 10 mg BID vs. BAT; ORR at week 24: **49.7% vs. 25.6%** (OR 2.99); failure-free survival superior
- **FDA approval: September 2021** for SR/RI chronic GvHD ≥12 years old [^przepiorka-2020-ruxolitinib-cgvhd-reach3]

**Ibrutinib (Imbruvica; BTK inhibitor; AbbVie/J&J) for chronic GvHD:**
- Ibrutinib inhibits BTK → ↓B cell activation → ↓donor B cell-mediated fibrogenesis + ↓Th2 cytokines (IL-4, IL-13) via ITK inhibition
- **FDA accelerated approval August 2017** for SR/RI cGvHD after ≥1 prior therapy; iNNOVATE trial (open-label): 67% ORR; 21% CR; 46% sustained response ≥20 weeks
- GI cGvHD and IBRUTINIB: less effective for GI manifestations vs. skin/mouth; replaced in many centers by ruxolitinib post-REACH3

**Belumosudil (Rezurock; ROCK2 inhibitor; Kadmon/Sanofi) for chronic GvHD:**
- ROCK2 (Rho-associated kinase 2): Belumosudil → ↓STAT3 phosphorylation (independently of JAK) → ↓Th17 polarization + ↑Treg differentiation; also inhibits fibroblast activation → anti-fibrotic in skin/lung cGvHD
- **KD025-213 Phase 2:** 200 mg QD: 74% ORR; 200 mg BID: 77% ORR; lung ORR 29% (rare responders in this manifestation)
- **FDA approval: August 2021** for SR/RI cGvHD ≥12 years after ≥2 prior therapies
- Distinct mechanism from ruxolitinib/ibrutinib; can be combined or used sequentially

**Axatilimab (anti-CSF-1R; Syndax) for cGvHD:**
- Targets colony-stimulating factor-1 receptor (CSF-1R) on macrophages → depletes fibrosis-driving macrophages (particularly in skin/fascia/GI fibrosis)
- **AGAVE-201 Phase 2:** 200 µg/kg Q2W: 74% ORR (best cohort); 100 µg/kg Q2W: 67% ORR; anti-fibrotic signal in skin and GI
- **FDA approval: August 2024** for SR/RI cGvHD after ≥2 prior therapies; newest approved mechanism

### IL-10 and Treg biology in GvHD

The protective Treg/IL-10 axis is the key biological counterbalance to alloreactive T cell pathogenicity:
- **Graft Treg content:** Peripheral blood grafts have ~5-10× fewer Tregs than bone marrow; Treg:Tconv ratio <1:20 in PBSC grafts predicts GvHD risk
- **Ex vivo Treg expansion:** ORCA-T (Orca Bio): selective Treg expansion from donor → 1-year GvHD-free survival 79% vs. 29% (matched external control); Phase 3 (PRECISION-T) ongoing
- **IL-10 serum kinetics:** Post-HSCT IL-10 peaks day +7 in non-GvHD patients; patients developing GvHD show paradoxically low IL-10 at day +7 (despite apparent inflammation) — reflecting insufficient Treg engagement
- **IL-10R mutations and VEO-IBD:** Biallelic loss-of-function mutations in *IL10RA* or *IL10RB* → infantile pancolitis; allo-HSCT from IL-10R-functional donor → curative, reinforcing the direct mechanistic role of the IL-10 axis in gut immune tolerance

## Pathology

**Refractory GvHD:**
- Grade III-IV SR aGvHD: 2-year OS <20%; multiple sequential salvage therapies further impair immune reconstitution; opportunistic infections (CMV, fungal, PJP) are major causes of death
- **Steroid refractory definition:** Progression after 3 days of methylprednisolone ≥2 mg/kg/day, or no improvement after 7 days, or inability to taper steroids

**Chronic GvHD — Bronchiolitis obliterans syndrome (BOS):**
- Lung manifestation of cGvHD; irreversible obstructive lung disease (FEV1/FVC <0.7); NIH lung score 2-3
- Pathology: concentric fibrotic obliteration of bronchioles; analogous to BOS in solid organ lung transplant
- Treatment: inhaled fluticasone + azithromycin + montelukast (FAM regimen); systemic immunosuppression; lung transplant in extreme cases
- Poor prognosis: FEV1 decline >10% in 2 years before diagnosis → 50% mortality within 2 years

**Infection and immune reconstitution:**
- GvHD and its treatment (immunosuppression) → profound secondary immunodeficiency
- CMV reactivation: monitored weekly by PCR; treated with valganciclovir (preemptive strategy)
- Invasive fungal infections (Aspergillus, Candida): prophylaxis with voriconazole or posaconazole for high-risk patients
- PJP prophylaxis: trimethoprim-sulfamethoxazole until CD4+ >200 cells/µL
- Hypogammaglobulinemia: monthly IVIG for IgG <400 mg/dL until immune reconstitution

**GvHD vs. relapse — the central tension:**
- Aggressive GvHD prophylaxis → reduced GvL → higher leukemia relapse rates (paradox: patients who develop mild cGvHD have lower relapse risk — GvL signal)
- **Donor lymphocyte infusion (DLI):** Infusion of additional donor T cells post-transplant to enhance GvL in patients with molecular relapse; deliberately induces mild GvHD to eliminate residual disease; used primarily in CML (90% CMR rates), AML, MDS

## Connections

- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — Treg-derived IL-10 is the dominant immunosuppressive brake on alloreactive donor T cells post-HSCT; low circulating IL-10 and IL-10R polymorphisms predict GvHD severity; IL-10 gene transfer and IL-10-secreting Treg infusions are investigational GvHD prevention strategies.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — GvHD originates from allogeneic bone marrow or peripheral blood stem cell transplantation; donor hematopoietic stem cell engraftment is required for GvHD to occur; the bone marrow niche is reshaped by donor-derived immune reconstitution, influencing GvHD vs. GvL balance.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — IL-6 is a central amplifier of acute GvHD: conditioning regimen tissue damage releases DAMPs → IL-6 from host APCs → JAK1/STAT3 in donor T cells → Th17 polarization + survival signals; tocilizumab (anti-IL-6R) is studied as GvHD prophylaxis in clinical trials.
- `connects-to` → **[T-Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Alloreactive donor CD4+ Th1 cells are the central drivers of acute GvHD: IL-12+IFN-γ drives Th1 polarization; IL-6+TGF-β drives Th17; recognize host alloantigens via direct (host MHC mismatch) and indirect (host peptides on donor APCs) pathways.
- `connects-to` → **[T-Cytotoxic Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Donor CD8+ CTLs are the primary effectors of target organ damage: recognize host MHC-I mismatch → perforin/granzyme-mediated killing of skin keratinocytes, GI crypt ISCs, and biliary epithelium → grade III/IV GvHD is the leading cause of non-relapse mortality.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — Gut microbiome diversity at transplant predicts GvHD severity; Akkermansia muciniphila and Blautia spp. are protective — loss of butyrate-producing bacteria reduces Treg support; antibiotic dysbiosis → loss of SCFAs → increased GvHD risk; FMT is investigational for GvHD rescue.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Skin is the first and most common target of acute graft-versus-host disease: donor CD8 T cells kill basal keratinocytes, producing a maculopapular rash that can progress to bullae, while chronic GvHD turns the skin lichenoid and sclerodermatous.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Ruxolitinib, a JAK1/JAK2 inhibitor, is the approved treatment for steroid-refractory graft-versus-host disease, both acute and chronic: by blocking JAK-STAT signaling downstream of IL-6, IFN-γ, and IL-12 it suppresses Th1/Th17 effectors while sparing regulatory T cells.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Donor regulatory T cells are the protective counterweight in GvHD: through IL-10 and TGF-β they restrain alloreactive effector T cells, and the graft's Treg-to-conventional-T ratio predicts tolerance versus disease — the rationale behind post-transplant cyclophosphamide.

[^ferrara-2009-gvhd-review]: Ferrara JL, Levine JE, Reddy P, Holler E. Graft-versus-host disease. *Lancet.* 2009;373(9674):1550-1561. [doi:10.1016/S0140-6736(09)60237-3](https://doi.org/10.1016/S0140-6736(09)60237-3) · [PubMed 19380114](https://pubmed.ncbi.nlm.nih.gov/19380114/)
[^zeiser-2020-ruxolitinib-gvhd-reach]: Zeiser R, von Bubnoff N, Butler J, et al. Ruxolitinib for Glucocorticoid-Refractory Acute Graft-versus-Host Disease. *N Engl J Med.* 2020;382(19):1800-1810. [doi:10.1056/NEJMoa1917635](https://doi.org/10.1056/NEJMoa1917635) · [PubMed 32374962](https://pubmed.ncbi.nlm.nih.gov/32374962/)
[^przepiorka-2020-ruxolitinib-cgvhd-reach3]: Przepiorka D, Luo L, Subramaniam S, et al. FDA Approval Summary: Ruxolitinib for Treatment of Chronic Graft-versus-Host Disease. *Oncologist.* 2022;27(2):98-104. [doi:10.1093/oncolo/oyab055](https://doi.org/10.1093/oncolo/oyab055) · [PubMed 35641197](https://pubmed.ncbi.nlm.nih.gov/35641197/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

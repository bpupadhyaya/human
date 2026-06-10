---
schema: medicine-entry/v1
id: adalimumab
name: Adalimumab
atlas: 03-medicine
scale: 01-modern
status: draft
last_reviewed: 2026-06-06
summary: "Fully human anti-TNFα monoclonal antibody (IgG1); neutralizes soluble and membrane-bound TNFα → ↓ NF-κB/MAPK inflammation. FDA-approved for RA, psoriasis, IBD, AS, JIA and 10 other indications. Humira was the world's best-selling drug 2012–2022."
aliases: ["adalimumab", "Humira", "D2E7", "adalimumab-atto", "adalimumab-adbm", "Hyrimoz", "Hadlima", "Amjevita"]
sources:
  - id: weinblatt-2003-adalimumab-ra
    type: peer-reviewed
    cite: "Weinblatt ME, Keystone EC, Furst DE, et al. Adalimumab, a fully human anti-tumor necrosis factor alpha monoclonal antibody, for the treatment of rheumatoid arthritis in patients taking concomitant methotrexate. Arthritis Rheum. 2003;48(1):35-45."
    doi: "10.1002/art.10697"
    pmid: "12528101"
    url: "https://doi.org/10.1002/art.10697"
  - id: colombel-2007-charm
    type: peer-reviewed
    cite: "Colombel JF, Sandborn WJ, Rutgeerts P, et al. Adalimumab for maintenance of clinical response and remission in patients with Crohn's disease: the CHARM trial. Gastroenterology. 2007;132(1):52-65."
    doi: "10.1053/j.gastro.2006.09.018"
    pmid: "17241859"
    url: "https://doi.org/10.1053/j.gastro.2006.09.018"
  - id: keystone-2004-armada
    type: peer-reviewed
    cite: "Keystone EC, Kavanaugh AF, Sharp JT, et al. Radiographic, clinical, and functional outcomes of treatment with adalimumab (a human anti-tumor necrosis factor monoclonal antibody) in patients with active rheumatoid arthritis receiving concomitant methotrexate therapy. Arthritis Rheum. 2004;50(5):1400-11."
    doi: "10.1002/art.20217"
    pmid: "15146409"
    url: "https://doi.org/10.1002/art.20217"
  - id: chan-2010-tnf-biology
    type: peer-reviewed
    cite: "Tracey D, Klareskog L, Sasso EH, Salfeld JG, Tak PP. Tumor necrosis factor antagonist mechanisms of action: a comprehensive review. Pharmacol Ther. 2008;117(2):244-79."
    doi: "10.1016/j.pharmthera.2007.10.001"
    pmid: "18155297"
    url: "https://doi.org/10.1016/j.pharmthera.2007.10.001"
cross_links:
  - target: 01-human/03-molecular/tnf-alpha
    relation: targets
    evidence: chan-2010-tnf-biology
    note: "Adalimumab is a fully human IgG1 monoclonal antibody that binds both soluble and membrane-bound TNFα with high affinity (Kd ~100 pM), neutralizing its interaction with p55 (TNFR1) and p75 (TNFR2) receptors — blocking NF-κB activation, MAPK/JNK signaling, and downstream inflammatory cytokine cascades."
  - target: 01-human/04-cellular/macrophage
    relation: modulates
    note: "TNFα is primarily produced by macrophages; adalimumab-mediated TNF neutralization reduces macrophage-driven IL-1β, IL-6, IL-8, MMP production and endothelial activation — the dominant mechanism in RA synovitis."
  - target: 01-human/03-molecular/nf-kb
    relation: modulates
    note: "TNFα-TNFR1 signaling is a major activator of NF-κB via TRADD-TRAF2-RIP1 → IKK complex → IκB phosphorylation/degradation; adalimumab blocks this upstream, preventing NF-κB nuclear translocation and pro-inflammatory gene transcription."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: treats
    note: "Adalimumab is first-line biologic for MTX-inadequate RA; ARMADA trial: ACR50 59% (adalimumab+MTX) vs 24% (MTX alone) at 24 weeks; halts radiographic progression; concomitant MTX reduces anti-drug antibody formation; approved per ACR and EULAR guidelines."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: treats
    note: "Adalimumab is approved for Crohn's disease (CHARM trial: 36% vs 12% 52-week remission) and ulcerative colitis (ULTRA-2: 16.5% vs 9.3% remission at 9 weeks); reduces fistula closure in perianal CD; both induction and maintenance approved."
---

# Adalimumab

## Overview

**Adalimumab** (Humira, D2E7) is a **fully human IgG1 monoclonal antibody** that targets **tumor necrosis factor alpha (TNFα)**, one of the central cytokines driving chronic inflammatory diseases. Developed by BASF Bioresearch (later AbbVie) using phage display technology to generate fully human sequences, adalimumab was first approved by the FDA in December 2002 for rheumatoid arthritis. It subsequently became the **world's best-selling drug by revenue** from 2012 to 2022 — a remarkable 10-year run — reflecting both its broad clinical utility across 13+ indications and the extraordinary commercial success of the Humira franchise.

Adalimumab is approved for: **rheumatoid arthritis (RA)**, **psoriatic arthritis**, **ankylosing spondylitis (AS)**, **Crohn's disease**, **ulcerative colitis**, **plaque psoriasis**, **juvenile idiopathic arthritis (JIA)**, **uveitis**, **hidradenitis suppurativa**, and others. Biosimilars began entering the US market in 2023 (following patent expiry), dramatically reducing costs.

## Mechanism

**TNFα biology:**
- TNFα is a 17 kDa homotrimeric cytokine produced primarily by **macrophages**, monocytes, T cells, and NK cells in response to infection or sterile inflammation
- Exists in two forms: **soluble TNFα (sTNFα)** (proteolytically cleaved from the membrane by ADAM17/TACE) and **membrane-bound TNFα (mTNFα)**
- Signals via two receptors: **TNFR1 (p55)** — constitutively expressed, primarily pro-inflammatory; **TNFR2 (p75)** — inducible, expressed mainly on immune cells
- TNFR1 signaling: TRADD → TRAF2 → RIP1 → IKK complex → **NF-κB activation** → transcription of IL-1, IL-6, IL-8, ICAM-1, VCAM-1, MMPs, COX-2; also activates **MAPK/JNK** → AP-1 → additional inflammatory gene transcription; can also trigger **caspase-8 → apoptosis** under certain conditions

**Adalimumab mechanism of action:**
1. **TNFα neutralization:** Adalimumab binds soluble and membrane-bound TNFα with high affinity (Kd ~100–200 pM); prevents binding to both TNFR1 and TNFR2 [^chan-2010-tnf-biology]
2. **Downstream effects:** ↓ NF-κB activation → ↓ IL-6, IL-8, MMP-1/3/13 production; ↓ endothelial cell activation (reduced ICAM-1, VCAM-1 → less leukocyte trafficking to synovium/gut/skin)
3. **mTNFα reverse signaling:** Adalimumab binding to mTNFα-expressing cells can induce reverse signaling → anti-inflammatory IL-10 production, T cell apoptosis — an additional mechanism of immune modulation
4. **ADCC and complement (secondary mechanisms):** As an IgG1, adalimumab can mediate antibody-dependent cellular cytotoxicity (ADCC) and complement-dependent cytotoxicity (CDC) against mTNFα-expressing cells (e.g., activated macrophages in synovium)

**Pharmacokinetics:**
- Route: Subcutaneous (SC) injection; bioavailability ~64%
- Peak concentration: 5 days post-SC injection
- Half-life: ~2 weeks (14 days)
- Eliminated predominantly by proteolysis
- Standard dosing: 40 mg SC every other week (RA, PsA); 160/80/40 mg (induction for Crohn's); 80/40 mg (PS induction)

## Clinical Use

**Rheumatoid Arthritis:**
- ARMADA trial [^keystone-2004-armada]: Adalimumab + methotrexate vs MTX alone: ACR50 response 59% vs 24% at 24 weeks; significant inhibition of radiographic progression
- First-line biologic in MTX-inadequate responders per ACR and EULAR guidelines
- Concomitant MTX reduces anti-drug antibody (ADA) formation and enhances response

**Crohn's Disease — CHARM trial:**
- 52-week remission rate: adalimumab 36% vs placebo 12% [^colombel-2007-charm]
- Significant fistula closure in perianal CD
- Both induction and maintenance therapy approved

**Safety — critical concerns:**
- **Tuberculosis reactivation:** TNFα is essential for granuloma formation and containment of *Mycobacterium tuberculosis*. All patients **must be screened with TST or IGRA** before starting; treat latent TB before adalimumab. Risk of TB reactivation ~3–25× increased (systematic review)
- **Other serious infections:** Increased risk of bacterial, fungal (histoplasmosis, coccidioidomycosis), viral infections; contraindicated with active serious infections
- **Hepatitis B reactivation:** Screen for HBsAg and HBcAb; antiviral prophylaxis if HBsAg+
- **Malignancy:** Modest increased risk of lymphoma (2–3×); no significant increase in solid tumors except non-melanoma skin cancer; benefit-risk favourable given severity of underlying disease
- **Demyelinating disease:** Contraindicated in pre-existing or new demyelinating disease (MS, optic neuritis)
- **Heart failure:** Contraindicated in NYHA class III/IV HF; worsens outcomes
- **Anti-drug antibodies (immunogenicity):** ~10–15% of patients develop neutralizing antibodies → loss of efficacy; concomitant immunosuppressants (MTX) reduce ADA formation

## Evidence

| Trial | Population | Key Finding |
|:---|:---|:---|
| ARMADA (Keystone 2004) [^keystone-2004-armada] | Active RA on MTX | ACR50: 59% (adalimumab+MTX) vs 24% (MTX alone); radiographic progression halted |
| CHARM (Colombel 2007) [^colombel-2007-charm] | Active Crohn's disease | 52-week remission: 36% vs 12%; fistula closure benefit confirmed |
| ULTRA-2 | Ulcerative colitis | 9-week remission rate: 16.5% vs 9.3% placebo; significant reduction in colectomy |
| REVEAL (plaque psoriasis) | Moderate-severe psoriasis | PASI 75 response at 16 weeks: 71% vs 7% placebo; durable at 60 weeks |
| Weinblatt 2003 [^weinblatt-2003-adalimumab-ra] | Early pivotal RA trial | ACR20/50/70 significantly superior to placebo; well-tolerated; established safety profile |

## Connections

- `targets` → **[TNFα](../../../../../01-human/03-molecular/tnf-alpha/README.md)** — high-affinity (Kd ~100 pM) neutralization of both soluble and membrane-bound TNFα, blocking TNFR1/TNFR2 signaling — the master inflammatory cytokine in RA, Crohn's disease, and psoriasis.
- `modulates` → **[Macrophage](../../../../../01-human/04-cellular/macrophage/README.md)** — reduces macrophage-driven synovial and mucosal inflammation via TNFα blockade; mTNFα reverse signaling on macrophages induces IL-10 production and T-cell apoptosis.
- `modulates` → **[NF-κB](../../../../../01-human/03-molecular/nf-kb/README.md)** — blocks TNFα-TNFR1-TRADD-TRAF2 signaling axis → prevents IKK-mediated IκB degradation → ↓ NF-κB nuclear translocation and pro-inflammatory gene transcription.
- `treats` → **[Rheumatoid Arthritis](../../../../../01-human/07-system/rheumatoid-arthritis/README.md)** — first-line biologic for MTX-inadequate RA; ARMADA trial: ACR50 59% vs 24% at 24 weeks; halts radiographic progression; concomitant MTX reduces anti-drug antibody formation.
- `treats` → **[Inflammatory Bowel Disease](../../../../../01-human/07-system/inflammatory-bowel-disease/README.md)** — approved for Crohn's disease (CHARM: 36% vs 12% 52-week remission) and ulcerative colitis (ULTRA-2: 16.5% vs 9.3%); fistula closure in perianal CD; induction and maintenance approved.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

---
schema: human-scale-entry/v1
id: c1-esterase-inhibitor
name: C1-Esterase Inhibitor
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "C1-esterase inhibitor (SERPING1; chr11q12.1) is a serpin blocking complement C1r/C1s and contact activation (FXII, kallikrein, FXIa); deficiency → bradykinin excess → vascular permeability → hereditary angioedema; icatibant (B2R antagonist) and berotralstat are approved."
aliases: ["C1-INH", "SERPING1", "C1 inhibitor", "C1 esterase inhibitor", "HAE protein", "C1 inactivator", "serine protease inhibitor G1"]
sources:
  - id: cicardi-2010-icatibant-nejm
    type: peer-reviewed
    cite: "Cicardi M, Banerji A, Bracho F, et al. Icatibant, a new bradykinin-receptor antagonist, in hereditary angioedema. N Engl J Med. 2010;363(6):532-541."
    doi: "10.1056/NEJMoa0906393"
    pmid: "20818873"
    url: "https://doi.org/10.1056/NEJMoa0906393"
  - id: maurer-2018-lanadelumab-help
    type: peer-reviewed
    cite: "Banerji A, Riedl MA, Bernstein JA, et al. Effect of lanadelumab compared with placebo on prevention of hereditary angioedema attacks: a randomized clinical trial. JAMA. 2018;320(20):2108-2121."
    doi: "10.1001/jama.2018.16773"
    pmid: "30480729"
    url: "https://doi.org/10.1001/jama.2018.16773"
  - id: zuraw-2020-berotralstat-apex2
    type: peer-reviewed
    cite: "Zuraw BL, Busse PJ, White M, et al. Berotralstat (BCX7353) for the prevention of hereditary angioedema. N Engl J Med. 2021;384(23):2186-2195."
    doi: "10.1056/NEJMoa2103679"
    pmid: "34077648"
    url: "https://doi.org/10.1056/NEJMoa2103679"
cross_links:
  - target: 01-human/07-system/hereditary-angioedema
    relation: connects-to
    note: "C1-INH deficiency (type I: low antigen + activity; type II: low activity, normal antigen) → uncontrolled FXII/kallikrein → bradykinin excess → B2R-mediated vascular permeability → HAE attacks; icatibant, C1-INH concentrate, berotralstat, and lanadelumab are therapeutic targets."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "C1-INH inhibits C1r and C1s (classical pathway C1 complex) → prevents C4/C2 cleavage → prevents classical C3 convertase formation; C1-INH deficiency → chronic low-level C4 consumption → low C4 (even between attacks) is the hallmark screening test for HAE type I and II."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "C1-INH inhibits contact activation: FXII (Hageman factor) and FXIa → limiting intrinsic coagulation; C1-INH also inhibits plasma kallikrein (shared FXII/kallikrein pathway); deficiency → FXII activation → kallikrein → bradykinin (not thrombin) is the primary effector."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "In sepsis, contact activation (FXII → kallikrein → bradykinin) contributes to vascular leak; C1-INH levels fall during severe sepsis from consumption; C1-INH concentrate investigated for sepsis capillary leak; C1-INH inhibits complement and contact activation in septic shock."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "C1-INH is a central innate immunity regulator: inhibits classical C1r/C1s (preventing C3 convertase formation) and contact FXII/kallikrein (preventing bradykinin-driven inflammation); C1-INH maintains homeostasis between complement activation and vascular integrity."
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: connects-to
    note: "SARS-CoV-2 activates contact activation; bradykinin hypothesis proposes FXII/kallikrein → bradykinin excess in COVID-19 vascular disease; low ACE2 → reduced bradykinin degradation → vascular permeability; C1-INH concentrate explored for COVID-19 vascular complications and ARDS."
---

# C1-Esterase Inhibitor

## Overview

**C1-esterase inhibitor (C1-INH)** (gene *SERPING1*, chromosome 11q12.1; also C1 inhibitor, C1 inactivator) is a **serpin (serine protease inhibitor)** — specifically a member of the serpin superfamily clade G — that functions as the **primary regulator of the contact activation (kallikrein-kinin) pathway and the classical complement pathway** [^cicardi-2010-icatibant-nejm]. Synthesized predominantly by hepatocytes and released into plasma at 0.15–0.35 g/L, C1-INH is unique among serpins in its **dual regulatory role** spanning two fundamentally distinct proteolytic cascades: the complement system (C1r, C1s inhibition) and the contact activation system (FXII, FXIa, plasma kallikrein inhibition).

**Clinical significance:** C1-INH deficiency is the molecular cause of **hereditary angioedema (HAE)** — recurrent, self-limited, potentially life-threatening subcutaneous and submucosal edema driven by bradykinin excess. The discovery that HAE attacks are bradykinin-mediated (not histamine-mediated) revolutionized treatment: antihistamines and corticosteroids are ineffective, but **icatibant** (bradykinin B2 receptor antagonist), **C1-INH concentrate**, and **kallikrein inhibitors** (berotralstat, lanadelumab) are highly effective [^maurer-2018-lanadelumab-help].

**Therapeutic targets built around the C1-INH/bradykinin axis:**

| Drug | Class | Target | Indication |
|:-----|:------|:-------|:-----------|
| Icatibant (Firazyr) | Bradykinin B2R antagonist (peptide) | B2R on endothelium | Acute HAE attack (SC, self-administered) |
| Berinert, Ruconest | C1-INH concentrate (plasma/recombinant) | Replaces C1-INH | Acute HAE attack or prophylaxis |
| Haegarda | C1-INH concentrate SC | Replaces C1-INH | Long-term prophylaxis |
| Lanadelumab (Takhzyro) | Anti-kallikrein mAb | Plasma kallikrein | Long-term prophylaxis (SC q2-4 weeks) |
| Berotralstat (Orladeyo) | Oral kallikrein inhibitor | Plasma kallikrein | Daily oral prophylaxis |
| Ecallantide (Kalbitor) | Kallikrein inhibitor (DX-88) | Plasma kallikrein | Acute HAE (SC; healthcare provider administered) |

## Structure

### Protein architecture

C1-INH is a **105 kDa single-chain glycoprotein** (478 amino acids after signal peptide cleavage) — the largest and most heavily glycosylated member of the serpin superfamily:

| Feature | Detail |
|:--------|:-------|
| Total molecular weight | ~105 kDa (protein ~57 kDa + N-linked + O-linked carbohydrate ~50 kDa) |
| Glycosylation | 7 N-linked oligosaccharide chains + numerous O-linked GalNAc-Ser/Thr at the N-terminal proline-rich domain; carbohydrates are essential for stability and half-life (~64 hours) |
| N-terminal domain | ~100 aa proline-rich, sialylated domain (not present in other serpins); O-glycosylated; not essential for protease inhibition but important for plasma stability |
| Serpin body | Classic β-sheets A, B, C + α-helices including the central helix F and hD |
| Reactive center loop (RCL) | Exposed loop with P1-P1' = Met434-Thr435; functions as the "bait" peptide for target serine proteases |

### Serpin mechanism of action — the suicide substrate trap

C1-INH inhibits its target serine proteases via the **serpin mechanism** — an irreversible "suicide substrate" strategy [^cicardi-2010-icatibant-nejm]:

1. Target protease (C1r, C1s, FXIIa, kallikrein, FXIa) binds C1-INH reactive center loop (RCL) → forms a Michaelis complex
2. Protease cleaves the P1-P1' bond (Met434-Thr435) → forms a covalent acyl-enzyme intermediate
3. Before the ester bond is hydrolyzed, C1-INH undergoes a **massive conformational change**: the RCL inserts into β-sheet A as an additional strand → the covalently attached protease is translocated ~70Å and deformed → the protease active site is physically distorted and inactivated
4. Result: a **stable 1:1 covalent complex** (C1-INH–protease) — functionally dead for both partners, rapidly cleared by the liver

This mechanism is fundamentally different from competitive inhibition: once the covalent complex forms, it is irreversible. The conformational change is also why serpins can only inhibit serine proteases (which form the acyl-enzyme intermediate) and not metalloproteases.

## Function

### Target proteases and their roles

**Classical complement pathway:**
- **C1r:** Autocatalytically activated C1r cleaves C1s; C1-INH inhibits activated C1r rapidly
- **C1s:** Cleaves C4 → C4b + C4a; cleaves C2 → C2b + C2a; C4b + C2a = classical C3 convertase; C1-INH terminates C1s activity → blocks C3 convertase formation via classical pathway

**Contact activation (kallikrein-kinin) pathway:**
- **Factor XII (FXII; Hageman factor):** Contact activator; activated by exposure to negatively charged surfaces (glass, collagen, polyphosphates, misfolded proteins); FXIIa activates prekallikrein → plasma kallikrein; C1-INH is the primary plasma inhibitor of FXIIa and FXIIf (FXIIa fragment)
- **Plasma kallikrein:** Cleaves high-molecular-weight kininogen (HMWK) → releases **bradykinin** (9 amino acids: Arg-Pro-Pro-Gly-Phe-Ser-Pro-Phe-Arg); C1-INH is the major plasma kallikrein inhibitor (~50% of plasma kallikrein inhibition capacity)
- **Factor XIa (FXIa):** Intrinsic coagulation pathway; C1-INH inhibits FXIa, bridging complement and coagulation regulation

### Bradykinin and vascular permeability

**Bradykinin** (BK) is the effector molecule of C1-INH deficiency:
- Bradykinin binds **B2 receptor (BDKRB2)** on endothelial cells → Gαq → IP₃/DAG → ↑intracellular Ca²⁺ → eNOS activation → nitric oxide (NO) + prostacyclin (PGI₂) → postcapillary venule vasodilation + ↑endothelial permeability + fluid extravasation
- Bradykinin also activates B1 receptor (BDKRB1) on activated/inflamed endothelium (upregulated by cytokines); B1R mediates sustained inflammation
- **Half-life of bradykinin:** ~30 seconds in plasma (rapidly degraded by ACE [kininase II = ACE], kininase I [carboxypeptidase N], and neutral endopeptidase)
- **ACE inhibitors block bradykinin degradation** → accumulation → angioedema (ACE inhibitor-induced angioedema = bradykinin-mediated, not IgE; treated with icatibant, not epinephrine; C1-INH typically normal)

### Role in complement regulation

C1-INH prevents inappropriate classical pathway activation by regulating the activity of the C1 complex. In HAE, chronic low-level C1 activation (in the absence of C1-INH) leads to:
- Gradual C4 consumption → **low C4 is a persistent finding in HAE type I and II** (even between attacks, when C3 may be normal)
- C4 level is the single best screening test for HAE — if low C4 + low C1-INH activity, diagnosis is established
- C1q is normal in HAE (differentiates from acquired angioedema with anti-C1q antibodies, where C1q is consumed)

## Mechanism

### HAE attack pathogenesis — bradykinin storm

**Sequence of events in an HAE attack:**

1. **Trigger** (trauma, surgery, dental procedure, stress, infection, estrogen, ACE inhibitor) → **FXII contact activation** on damaged endothelium or locally active surfaces
2. FXIIa + kallikrein → positive feedback amplification (kallikrein cleaves FXII → more FXIIa → more kallikrein)
3. **Plasma kallikrein cleaves HMWK** → releases **bradykinin**
4. Bradykinin binds **B2R on endothelial cells** → IP₃/Ca²⁺/eNOS → ↑vascular permeability in postcapillary venules → fluid and plasma proteins extravasate into interstitial space
5. **Swelling** develops over 2-24h; peaks at 24-72h; spontaneously resolves in 48-96h (bradykinin half-life short but production sustained during attack)
6. **C1-INH** is the key brake: it inhibits both FXII/kallikrein (stopping bradykinin generation) and C1r/C1s (complement arm); in HAE, this brake is absent or insufficient → runaway bradykinin production

**Why C4 is always low in HAE but C1q is normal:**
- C1-INH deficiency → C1r/C1s not fully inhibited → slow constitutive C4 cleavage → C4 is chronically consumed (C4 half-life ~2.5 days; synthesis can't keep up)
- C1q is upstream of C1r/C1s and is not consumed by the C1-INH-deficient state
- C3 is usually normal (C3 convertase still requires C4b2a, which is limited; complement amplification usually doesn't proceed to significant C3 cleavage in HAE)

### Treatment mechanism

| Drug | Mechanism | Speed of action |
|:-----|:----------|:----------------|
| C1-INH concentrate (IV/SC) | Direct replacement of missing C1-INH → restores inhibition of kallikrein and FXII | 30-120 min (IV faster) |
| Icatibant | Competitive antagonist of bradykinin B2R → blocks B2R-mediated vascular permeability; does not stop bradykinin generation | 30-60 min |
| Ecallantide | Recombinant Kunitz-domain inhibitor; inhibits plasma kallikrein catalytic site → stops bradykinin generation | 60-90 min |
| Berotralstat | Small molecule; non-covalent competitive inhibitor of plasma kallikrein (KKB1); oral; 110 mg/day → 44% reduction in attacks (APeX-2) [^zuraw-2020-berotralstat-apex2] | Prophylaxis only |
| Lanadelumab | Fully human anti-kallikrein IgG4 mAb (clone DX-2930); binds plasma kallikrein with picomolar affinity → prevents HMWK cleavage → no bradykinin; SC q2-4 weeks; HELP OLE: 87% reduction in attacks [^maurer-2018-lanadelumab-help] | Prophylaxis only; weeks to max effect |

## Connections

- `connects-to` → **[Hereditary Angioedema](../../07-system/hereditary-angioedema/README.md)** — C1-INH deficiency (type I: low antigen + activity; type II: low activity, normal antigen) → uncontrolled FXII/kallikrein → bradykinin excess → B2R-mediated vascular permeability → HAE attacks; icatibant, C1-INH concentrate, berotralstat, and lanadelumab are therapeutic targets.
- `connects-to` → **[Complement C3](../complement-c3/README.md)** — C1-INH inhibits C1r and C1s (classical pathway C1 complex) → prevents C4/C2 cleavage → prevents classical C3 convertase formation; C1-INH deficiency → chronic low-level C4 consumption → low C4 (even between attacks) is the hallmark screening test for HAE type I and II.
- `connects-to` → **[Thrombin](../thrombin/README.md)** — C1-INH inhibits contact activation: FXII (Hageman factor) and FXIa → limiting intrinsic coagulation; C1-INH also inhibits plasma kallikrein (shared FXII/kallikrein pathway); deficiency → FXII activation → kallikrein → bradykinin (not thrombin) is the primary effector.
- `connects-to` → **[Sepsis](../../07-system/sepsis/README.md)** — In sepsis, contact activation (FXII → kallikrein → bradykinin) contributes to vascular leak; C1-INH levels fall during severe sepsis from consumption; C1-INH concentrate investigated for sepsis capillary leak; C1-INH inhibits complement and contact activation in septic shock.
- `connects-to` → **[Immune System](../../07-system/immune-system/README.md)** — C1-INH is a central innate immunity regulator: inhibits classical C1r/C1s (preventing C3 convertase formation) and contact FXII/kallikrein (preventing bradykinin-driven inflammation); C1-INH maintains homeostasis between complement activation and vascular integrity.
- `connects-to` → **[SARS-CoV-2](../../../02-pathogen/01-viruses/sars-cov-2/README.md)** — SARS-CoV-2 activates contact activation; bradykinin hypothesis proposes FXII/kallikrein → bradykinin excess in COVID-19 vascular disease; low ACE2 → reduced bradykinin degradation → vascular permeability; C1-INH concentrate explored for COVID-19 vascular complications and ARDS.

[^cicardi-2010-icatibant-nejm]: Cicardi M, Banerji A, Bracho F, et al. Icatibant, a new bradykinin-receptor antagonist, in hereditary angioedema. *N Engl J Med.* 2010;363(6):532-541. [doi:10.1056/NEJMoa0906393](https://doi.org/10.1056/NEJMoa0906393) · [PubMed 20818873](https://pubmed.ncbi.nlm.nih.gov/20818873/)
[^maurer-2018-lanadelumab-help]: Banerji A, Riedl MA, Bernstein JA, et al. Effect of lanadelumab compared with placebo on prevention of hereditary angioedema attacks. *JAMA.* 2018;320(20):2108-2121. [doi:10.1001/jama.2018.16773](https://doi.org/10.1001/jama.2018.16773) · [PubMed 30480729](https://pubmed.ncbi.nlm.nih.gov/30480729/)
[^zuraw-2020-berotralstat-apex2]: Zuraw BL, Busse PJ, White M, et al. Berotralstat (BCX7353) for the prevention of hereditary angioedema. *N Engl J Med.* 2021;384(23):2186-2195. [doi:10.1056/NEJMoa2103679](https://doi.org/10.1056/NEJMoa2103679) · [PubMed 34077648](https://pubmed.ncbi.nlm.nih.gov/34077648/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

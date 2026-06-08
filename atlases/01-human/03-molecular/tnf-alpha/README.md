---
schema: human-scale-entry/v1
id: tnf-alpha
name: "TNF-α (Tumor Necrosis Factor-alpha)"
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-04
summary: "17 kDa TNF-superfamily homotrimer. Produced by macrophages/monocytes; signals via TNFR1/TNFR2 → NF-κB, MAPK, apoptosis. Master proximal alarm cytokine; drives septic shock, cytokine storm, RA, Crohn's. Targeted by adalimumab, infliximab, etanercept — best-selling biologic class."
aliases: ["TNF-alpha", "TNF-α", "tumor necrosis factor", "TNF", "cachectin", "DIF", "TNFSF2"]
taxonomy:
  gene_symbol: "TNF"
  chromosome: "6p21.33"
  uniprot: "P01375"
sources:
  - id: pennica-1984-tnf-cloning
    type: peer-reviewed
    cite: "Pennica D, Nedwin GE, Hayflick JS, et al. Human tumour necrosis factor: precursor structure, expression and homology to lymphotoxin. Nature. 1984;312(5996):724-9."
    doi: "10.1038/312724a0"
    pmid: "6392892"
    url: "https://doi.org/10.1038/312724a0"
  - id: aggarwal-2003-tnf-biology
    type: peer-reviewed
    cite: "Aggarwal BB. Signalling pathways of the TNF superfamily: a double-edged sword. Nat Rev Immunol. 2003;3(9):745-56."
    doi: "10.1038/nri1184"
    pmid: "12949498"
    url: "https://doi.org/10.1038/nri1184"
  - id: tracey-1987-tnf-cachectin
    type: peer-reviewed
    cite: "Tracey KJ, Fong Y, Hesse DG, et al. Anti-cachectin/TNF monoclonal antibodies prevent septic shock during lethal bacteraemia. Nature. 1987;330(6149):662-4."
    doi: "10.1038/330662a0"
    pmid: "3317066"
    url: "https://doi.org/10.1038/330662a0"
  - id: feldmann-1994-tnf-ra
    type: peer-reviewed
    cite: "Feldmann M, Brennan FM, Maini RN. Rheumatoid arthritis. Cell. 1996;85(3):307-10."
    doi: "10.1016/S0092-8674(00)81109-5"
    pmid: "8616886"
    url: "https://doi.org/10.1016/S0092-8674(00)81109-5"
cross_links:
  - target: 01-human/07-system/immune-system
    relation: expressed-by
    evidence: aggarwal-2003-tnf-biology
    note: "TNF-α is the canonical product of activated macrophages and monocytes within the immune system; it is released within minutes of pattern-recognition receptor activation (TLRs, NLRs) and serves as the proximal alarm signal of systemic inflammation."
  - target: 01-human/03-molecular/il-6
    relation: modulates
    evidence: aggarwal-2003-tnf-biology
    note: "TNF-α is a potent inducer of IL-6 transcription via NF-κB binding to the IL-6 promoter; TNF and IL-6 act synergistically in driving the acute-phase response and cytokine storm in sepsis and severe viral infections."
  - target: 01-human/04-cellular/hepatocyte
    relation: damages
    evidence: tracey-1987-tnf-cachectin
    note: "High-concentration TNF-α causes hepatocyte apoptosis via TNFR1-caspase-8-caspase-3 cascade; contributes to hepatic dysfunction in septic shock, DILI (drug-induced liver injury), and alcoholic hepatitis."
  - target: 01-human/06-organ/liver
    relation: damages
    evidence: tracey-1987-tnf-cachectin
    note: "TNF-α-mediated hepatocyte apoptosis and inflammatory signaling cause liver injury in septic shock, alcoholic hepatitis, and autoimmune hepatitis; the liver is a primary organ target of systemic TNF-α excess."
  - target: 01-human/04-cellular/macrophage
    relation: expressed-by
    evidence: aggarwal-2003-tnf-biology
    note: "M1-polarised macrophages are the dominant cellular source of TNF-α: TLR4/LPS activates NF-κB → TNF gene transcription within 15–30 min; macrophage-released TNF-α amplifies systemic inflammation and drives the acute-phase response."
  - target: 03-medicine/03-food/curcumin
    relation: modulated-by
    evidence: aggarwal-2003-tnf-biology
    note: "Curcumin covalently inhibits IKKβ (Michael addition to Cys-179), trapping NF-κB in the cytoplasm and suppressing TNF-α transcription; AP-1 suppression (via JNK inhibition) and STAT3 inhibition provide additional multi-level anti-inflammatory suppression."
  - target: 01-human/03-molecular/nf-kb
    relation: modulated-by
    evidence: aggarwal-2003-tnf-biology
    note: "NF-κB p65/p50 binds two κB sites in the TNF promoter, driving TNF-α transcription in macrophages; TNF-α in turn activates NF-κB via TNFR1→TRADD→RIP1→IKK, creating a positive inflammatory feedback loop."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: modulated-by
    evidence: aggarwal-2003-tnf-biology
    note: "GR activation transrepresses TNF-α transcription via direct binding to NF-κB p65, displacing coactivators CBP/p300 and recruiting HDAC2; this is the mechanistic basis of glucocorticoid anti-inflammatory action."
  - target: 01-human/07-system/ankylosing-spondylitis
    relation: connects-to
    note: "TNF-α drives entheseal and synovial inflammation in AS; anti-TNF biologics (adalimumab, etanercept, infliximab, certolizumab, golimumab) are first-line biologic therapy; TNF blockade reduces MRI sacroiliitis (ASAS40 ~50-60%) but does not halt new bone formation (syndesmophytes)."
  - target: 01-human/07-system/psoriatic-arthritis
    relation: connects-to
    note: "TNF-α drives PsA synovitis, enthesitis, and structural damage; adalimumab, certolizumab (RAPID-PsA: ACR20 58% vs 24%; FDA 2013), etanercept, golimumab, and infliximab are approved; TNF and IL-36 co-activation amplifies synovial inflammation in PsA."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "TNF-α is essential for granuloma formation and maintenance in TB; anti-TNF therapy (infliximab, adalimumab) → 4-25× increased TB reactivation risk; anti-TNF antibodies carry higher TB risk than etanercept; IGRA/TST screening mandatory before anti-TNF initiation."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "TLR4/LPS → MyD88 → NF-κB → rapid TNF-α transcription in macrophages within 15–30 min; TNF-α is the first cytokine released in gram-negative sepsis; TLR4/TNF-α form a positive amplification loop (TNF-α → TNFR1 → NF-κB → more TNF-α); thalidomide suppresses LPS-induced TNF-α."
---

# TNF-α (Tumor Necrosis Factor-alpha)

## Overview

**Tumor necrosis factor-alpha (TNF-α)** is a 17 kDa pleiotropic cytokine and the founding member of the **TNF superfamily** (27 members in humans). First described as "cachectin" and as a factor causing tumor necrosis in LPS-treated animals in the 1970s, it was cloned and sequenced in 1984 by Pennica and colleagues at Genentech [^pennica-1984-tnf-cloning]. It is now understood as one of the master proximal regulators of systemic inflammation.

TNF-α is synthesized as a **26 kDa transmembrane precursor** (tmTNF) that is cleaved by ADAM17 (TACE, TNF-converting enzyme) to release the soluble **17 kDa monomeric form**, which spontaneously assembles into non-covalent **homotrimers** — the bioactive species. Both tmTNF and soluble TNF are biologically active; tmTNF provides juxtacrine signaling, while soluble TNF acts at a distance.

The central physiological role of TNF-α is as an **early-response cytokine**: within minutes of innate receptor activation (TLRs, NOD2, STING), macrophages and monocytes release pre-formed tmTNF and rapidly transcribe new TNF, amplifying the alarm signal to the rest of the immune system. Appropriate TNF responses are essential for pathogen containment; uncontrolled TNF drives the pathological inflammation of septic shock, rheumatoid arthritis, Crohn's disease, and cytokine storm [^aggarwal-2003-tnf-biology].

TNF-α is the molecular target of the best-selling class of biologic drugs in history — **anti-TNF monoclonal antibodies** (adalimumab, infliximab, certolizumab, golimumab) and the receptor fusion protein **etanercept** — used across rheumatoid arthritis, ankylosing spondylitis, psoriatic arthritis, and inflammatory bowel disease [^feldmann-1994-tnf-ra].

## Structure

TNF-α is encoded by the *TNF* gene at **6p21.33** within the MHC class III region, expressed as a type II transmembrane protein:

- **Precursor (tmTNF):** 233 amino acids; signal anchor in N-terminal cytoplasmic domain, transmembrane helix, 157-aa ectodomain
- **Soluble form:** 157 amino acids (released after ADAM17 cleavage at Ala-76/Val-77)
- **Bioactive unit:** homotrimer; each protomer adopts a **β-jelly-roll fold** (10-stranded antiparallel β-sandwich); three protomers associate non-covalently around a 3-fold symmetry axis, creating a cone-shaped trimer with three receptor-binding grooves at the base
- **Disulfide bond:** Cys-69/Cys-101 in each protomer (stabilizes the β-sandwich)

### Receptor interactions
- **TNFR1** (p55, CD120a, TNFRSF1A): ubiquitously expressed; contains a **death domain (DD)** in its cytoplasmic tail; primary mediator of inflammatory and apoptotic signaling; binds both soluble and tmTNF
- **TNFR2** (p75, CD120b, TNFRSF1B): predominantly on immune cells and endothelial cells; no death domain; primarily pro-survival/proliferative; preferentially activated by tmTNF

## Function

### Signaling pathways

**TNFR1 signaling:**
1. **NF-κB pathway** — Ligand-induced TNFR1 trimerization recruits TRADD, then TRAF2/5 and RIP1; RIP1-mediated IKK complex activation → IκB phosphorylation and degradation → NF-κB nuclear translocation → transcription of pro-inflammatory genes (IL-1β, IL-6, IL-8, COX-2, iNOS, adhesion molecules, anti-apoptotic BCL-2 family members)
2. **MAPK cascade** — TRAF2 → ASK1 → JNK/p38 → AP-1 transcription → IL-6, IL-1 production
3. **Apoptosis (Complex II / Ripoptosome)** — When NF-κB is insufficient (e.g., in sustained high TNF), TRADD → FADD → caspase-8 → caspase-3 cascade → apoptosis
4. **Necroptosis (Complex III)** — When caspase-8 is blocked (e.g., certain viral infections), RIP1 + RIP3 → MLKL phosphorylation → plasma membrane rupture → programmed necrosis

**TNFR2 signaling:**
- TRAF1/2 → TRAF2 depletion from TNFR1 complex (modulates TNFR1 response)
- PI3K/Akt → survival, proliferation (T-reg expansion, NK cell activation)
- NF-κB2 (non-canonical NF-κB pathway)

## Mechanism

**Acute-phase amplification:** TNF-α transcription is initiated within 15–30 minutes of TLR4 (LPS) activation in macrophages, mediated by NF-κB and AP-1 binding the *TNF* promoter. TNF-α then acts on hepatocytes to upregulate CRP, SAA, fibrinogen (acute-phase proteins) via IL-6 [^aggarwal-2003-tnf-biology]. It also acts on the hypothalamus (prostaglandin-mediated fever) and drives endothelial activation (VCAM-1, ICAM-1 upregulation → leukocyte recruitment).

**Granuloma formation:** TNF-α is essential for macrophage activation and granuloma maintenance in mycobacterial infection (TB) and other intracellular pathogens. Anti-TNF therapy dramatically increases TB reactivation risk — ~25-fold increase in active TB in anti-TNF recipients, particularly infliximab [^feldmann-1994-tnf-ra].

**Cancer cachexia (historical):** TNF-α was initially named "cachectin" for its ability to induce wasting syndrome (cachexia) — lipolysis via hormone-sensitive lipase activation, skeletal muscle proteolysis, suppression of lipoprotein lipase. Chronic low-level TNF in malignancy drives the cachectic state.

## Connections

- **Expressed-by** → [Immune System](../../../01-human/07-system/immune-system/README.md): Macrophages and monocytes of the immune system are the primary source of TNF-α in response to innate receptor activation; dendritic cells, T cells, and NK cells also produce TNF-α.
- **Modulates** → [Interleukin-6](../../../01-human/03-molecular/il-6/README.md): TNF-α drives IL-6 transcription via NF-κB; the two cytokines act synergistically in driving systemic inflammation, cytokine storm, and the hepatic acute-phase response.
- **Damages** → [Hepatocyte](../../../01-human/04-cellular/hepatocyte/README.md): At high concentrations (as in septic shock or immune-mediated hepatitis), TNFR1-mediated caspase activation causes hepatocyte apoptosis and contributes to acute liver failure.
- `connects-to` → **[Ankylosing Spondylitis](../../07-system/ankylosing-spondylitis/README.md)** — TNF-α drives entheseal and synovial inflammation in AS; anti-TNF biologics (adalimumab, etanercept, infliximab, certolizumab, golimumab) are first-line biologic therapy; TNF blockade reduces MRI sacroiliitis (ASAS40 ~50-60%) but does not halt new bone formation (syndesmophytes).
- `connects-to` → **[Psoriatic Arthritis](../../07-system/psoriatic-arthritis/README.md)** — TNF-α drives PsA synovitis, enthesitis, and structural damage; adalimumab, certolizumab (RAPID-PsA: ACR20 58% vs 24%; FDA 2013), etanercept, golimumab, and infliximab are approved; TNF and IL-36 co-activation amplifies synovial inflammation in PsA.
- `connects-to` → **[Tuberculosis](../../07-system/tuberculosis/README.md)** — TNF-α is essential for granuloma formation, macrophage activation, and MTB containment; anti-TNF therapy (infliximab, adalimumab) → 4–25× increased TB reactivation risk; antibody-based anti-TNF agents carry higher TB risk than etanercept (receptor fusion protein); mandatory IGRA/TST screening + LTBI prophylaxis before initiating anti-TNF biologic therapy.
- `connects-to` → **[TLR4](../tlr4/README.md)** — TLR4/LPS → MyD88 → NF-κB → rapid TNF-α transcription in macrophages within 15–30 min; TNF-α is the first cytokine released in gram-negative sepsis; TLR4/TNF-α form a positive amplification loop (TNF-α → TNFR1 → NF-κB → more TNF-α); thalidomide suppresses LPS-induced TNF-α.

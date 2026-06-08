---
schema: human-scale-entry/v1
id: il-2
name: IL-2
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "IL-2 (IL2, chr4q26) is the canonical T cell growth factor; signals via IL-2Rα/β/γc → JAK1/JAK3/STAT5 → proliferation. Low-dose expands Tregs (clinical trials in SLE, GVHD); high-dose aldesleukin approved for metastatic RCC and melanoma (FDA 1992/1998)."
aliases: ["IL-2", "interleukin-2", "T cell growth factor", "aldesleukin", "Proleukin", "TCGF"]
sources:
  - id: morgan-1976-il2-discovery
    type: peer-reviewed
    cite: "Morgan DA, Ruscetti FW, Gallo R. Selective in vitro growth of T lymphocytes from normal human bone marrows. Science. 1976;193(4257):1007-1008."
    doi: "10.1126/science.181845"
    pmid: "181845"
  - id: lotze-1985-aldesleukin-rcc
    type: peer-reviewed
    cite: "Rosenberg SA, Lotze MT, Muul LM, et al. Observations on the systemic administration of autologous lymphokine-activated killer cells and recombinant interleukin-2 to patients with metastatic cancer. N Engl J Med. 1985;313(23):1485-1492."
    doi: "10.1056/NEJM198512053132327"
    pmid: "3903516"
  - id: klatzmann-2015-lowdose-il2-review
    type: peer-reviewed
    cite: "Klatzmann D, Abbas AK. The promise of low-dose interleukin-2 therapy for autoimmune and inflammatory diseases. Nat Rev Immunol. 2015;15(5):283-294."
    doi: "10.1038/nri3823"
    pmid: "25882245"
  - id: abbas-immunology-9e
    type: textbook
    cite: "Abbas AK, Lichtman AH, Pillai S. Cellular and Molecular Immunology. 9th ed. Elsevier; 2018."
    url: "https://www.elsevier.com/books/cellular-and-molecular-immunology/abbas/978-0-323-52323-3"
    accessed: "2026-06-07"
cross_links:
  - target: 01-human/04-cellular/t-helper-cell
    relation: modulates
    note: "IL-2 is the primary autocrine/paracrine Th cell growth factor after TCR + CD28 co-stimulation; NFAT drives IL-2 transcription (blocked by calcineurin inhibitors); IL-2 → JAK1/JAK3/STAT5 → cyclin D/BCL-2/BCL-XL → T cell proliferation and survival in immune responses."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: modulates
    note: "IL-2 is essential for Treg development, survival, and FOXP3 maintenance via IL-2Rα (CD25, highly expressed on Tregs) → STAT5 phosphorylation; low-dose IL-2 (0.5–2 MIU/d SC) selectively expands Tregs in SLE, ALS, GVHD, and T1D clinical trials."
  - target: 01-human/07-system/cidp
    relation: connects-to
    note: "CD4+ T cells (IL-2-dependent) drive macrophage-mediated paranodal demyelination in CIDP; Treg dysfunction (defective IL-2 signaling) may predispose; low-dose IL-2 for Treg expansion is under investigation as adjunct therapy in refractory CIDP and other autoimmune neuropathies."
  - target: 01-human/07-system/immune-thrombocytopenia
    relation: connects-to
    note: "Low-dose IL-2 (0.5–2 MIU/d SC) selectively expands Tregs in ITP; pilot trials show platelet increases and anti-platelet IgG reduction; calcineurin inhibitors block IL-2/NFAT → impair Treg expansion and immune tolerance in ITP."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin dephosphorylates NFAT to drive IL-2 transcription; cyclosporine/tacrolimus block calcineurin → NFAT cytoplasmic → IL-2 abolished → T cell expansion prevented; NFAT+AP-1+NF-κB combinatorially govern the IL-2 promoter as an AND-gate."
---

# IL-2

## Overview

Interleukin-2 (IL-2), encoded by *IL2* on chromosome 4q26, is the founding member of the γc-chain cytokine family and the **canonical T lymphocyte growth factor**. Discovered in 1976 by Morgan, Ruscetti, and Gallo as a factor enabling the long-term culture of T cells in vitro [^morgan-1976-il2-discovery], it was initially called "T cell growth factor" (TCGF). IL-2 is produced primarily by activated CD4⁺ Th1 cells and CD8⁺ T cells after T cell receptor (TCR) engagement plus CD28 co-stimulation, and acts as a potent autocrine and paracrine growth signal.

IL-2 occupies a dual role in immunity: it drives **effector T cell expansion** (essential for mounting immune responses) while also being the critical survival and proliferation signal for **regulatory T cells (Tregs)** — the very cells that suppress those responses [^klatzmann-2015-lowdose-il2-review]. This duality has profound therapeutic implications: high-dose IL-2 (aldesleukin/Proleukin) stimulates anti-tumor immunity, while low-dose IL-2 selectively expands Tregs to suppress autoimmunity.

## Structure

### Protein

Mature IL-2 is a **133-amino acid**, ~15 kDa (glycosylated: ~18 kDa) monoglycosylated cytokine adopting a **4-helix bundle fold** (helices A–D). It belongs to the short-chain cytokine family with an up-up-down-down antiparallel helix topology. Key structural features:
- Cys58–Cys105 intra-chain disulfide (essential for receptor binding)
- Helix A and D form the IL-2Rα (CD25) binding interface
- Helix A, C, and the loop between B and C contact IL-2Rβ (CD122)
- IL-2Rγ (γc chain) contacted by the helical bundle exterior

### Receptor Complex — Three Affinities

| Complex | Components | Kd | Expression | Function |
|:--------|:-----------|:---|:-----------|:---------|
| High-affinity trimeric | IL-2Rα (CD25) + IL-2Rβ (CD122) + IL-2Rγ (γc, CD132) | ~10 pM | Tregs (constitutive), activated T cells | Full signaling; Treg survival |
| Intermediate-affinity dimeric | IL-2Rβ + IL-2Rγ | ~1 nM | NK cells, resting memory T cells, CD8+ | NK activation; memory T cell maintenance |
| Low-affinity monomeric | IL-2Rα (CD25) alone | ~10 nM | Activated T cells, some B cells | Ligand capture; no signaling |

The **CD25 (IL-2Rα) chain** is the key differentiator: Tregs constitutively express high CD25, giving them a selective advantage in capturing IL-2 at low concentrations — the mechanistic basis of low-dose IL-2 Treg therapy.

### Signaling Cascade

IL-2 → trimeric receptor complex → **JAK1** (pre-associated with IL-2Rβ) and **JAK3** (pre-associated with IL-2Rγ) trans-phosphorylate → three primary downstream cascades:

1. **STAT5a/STAT5b**: Principal signaling arm → STAT5 Tyr694/699 phosphorylation → homodimerization → nuclear translocation → target gene transcription:
   - *BCL2* (anti-apoptosis)
   - *MCL1*, *BCL2L1* (BCL-XL) (anti-apoptosis)
   - *CCND1/D2* (cyclin D; G1/S progression)
   - *FOXP3* (Treg master transcription factor; maintained by IL-2/STAT5)
   - *IL2RA* (CD25; autocrine upregulation)

2. **PI3K/Akt/mTOR**: Activated via IRS-1/2 → mTORC1 → S6K/4E-BP1 → protein synthesis, metabolic reprogramming (aerobic glycolysis in effector T cells; oxidative phosphorylation in Tregs)

3. **MAPK/ERK**: via Ras → Raf → MEK → ERK1/2 → AP-1 (Fos/Jun) → transcriptional proliferative program

### Transcriptional Regulation of *IL2* Gene

The *IL2* promoter integrates three signal-dependent transcription factors:
- **NFAT** (nuclear factor of activated T cells): Ca²⁺/calcineurin-dependent; dephosphorylated NFAT enters nucleus; site of action of cyclosporine A (CsA) and tacrolimus (FK506), which inhibit calcineurin → block NFAT dephosphorylation → no IL-2 transcription
- **AP-1** (Fos/Jun): MAPK-dependent; co-operative with NFAT
- **NF-κB**: CD28 co-stimulation → PI3K/Akt → IKK → NF-κB nuclear entry → cooperates with NFAT/AP-1

This combinatorial requirement for three signals explains T cell tolerance induction: TCR signal without CD28 → no NF-κB → incomplete NFAT/AP-1 activation → anergy (no IL-2 production).

## Function

### Effector T Cell Expansion

After TCR activation, IL-2 (autocrine and from neighboring Th1 cells) drives:
1. **G1 → S phase transition** via cyclin D1/CDK4 and CDK6 activation
2. **Anti-apoptotic protection** via BCL-2/BCL-XL upregulation
3. **Metabolic shift** to aerobic glycolysis (Warburg effect) via mTORC1

IL-2 is also the survival signal for **effector memory CD8+ T cells** (via intermediate-affinity IL-2Rβγ) and **NK cells** — explaining its anti-tumor activity at high doses.

### Treg Homeostasis

Tregs express high constitutive CD25 and depend on IL-2 from neighboring activated T cells (Tregs do not produce IL-2 themselves — FOXP3 represses the *IL2* gene in Tregs). IL-2 → IL-2Rαβγ → STAT5 → FOXP3 transcription → Treg suppressive program (IL-10, TGF-β, CTLA-4, LAG-3). This creates a homeostatic circuit: effector T cell activation → more IL-2 → simultaneously drives effector expansion AND fuels the Treg brake.

## Mechanism

### High-Dose IL-2 — Tumor Immunotherapy

**Aldesleukin** (recombinant human IL-2; Proleukin; Clinigen) was FDA-approved for **metastatic renal cell carcinoma** in 1992 and **metastatic melanoma** in 1998. Doses of 600,000–720,000 IU/kg IV q8h ("high-dose bolus") achieve complete responses in ~7–8% of patients with durable remission in ~3–5% (effectively curative) [^lotze-1985-aldesleukin-rcc].

Major toxicity: **vascular leak syndrome (VLS)** — IL-2 activates endothelial cells and NK cells → systemic capillary leak → hypotension, edema, renal failure; requires ICU management. Less used since checkpoint inhibitors (anti-PD-1/CTLA-4) achieve higher response rates with better tolerability.

### Low-Dose IL-2 — Treg Expansion Therapy

Doses of **0.5–3 × 10⁶ IU/day** SC (5-10× lower than immunostimulatory doses) preferentially expand Tregs (high CD25) without significantly expanding Tconv or NK cells. Clinical trials across multiple autoimmune diseases:
- **SLE** (lupus nephritis): Phase 3 trials ongoing; IL-2 reduces disease activity scores and increases Treg/Teff ratios
- **GVHD**: Low-dose IL-2 expands Tregs → chronic GVHD improvement in Phase 1/2 studies
- **T1D**: Preservation of residual β-cell function in early-onset T1D under investigation
- **ALS**: Neuroinflammatory contribution
- **Hepatitis C cirrhosis**: Restores Treg homeostasis in liver

[^klatzmann-2015-lowdose-il2-review]

### Anti-IL-2Rα (Anti-CD25) Therapeutics

**Basiliximab** (Simulect; Novartis): chimeric anti-CD25 mAb; FDA 1998 for prophylaxis of acute organ rejection in renal transplantation; blocks IL-2Rα → prevents allograft-reactive T cell proliferation.

**Daclizumab** (Zinbryta; Biogen): humanized anti-CD25; FDA May 2016 for RRMS — by blocking CD25, it paradoxically increases NK cell activity (no Treg expansion → increased NK surveillance of CNS Th17) and reduces B cell plasmablasts. Voluntarily withdrawn March 2018 following cases of fulminant liver failure and immune-mediated encephalitis.

### Next-Generation IL-2 Variants

**CD122-preferential ("orthogonal") IL-2 analogs:**
- **Bempegaldesleukin** (BEMPEG; NKTR-358): PEGylated IL-2 preferentially activating CD122/CD132 → CD8+ T cell and NK expansion without Treg expansion → Phase 3 trials in melanoma (PIVOT IO-001; combined with nivolumab); mixed trial results in 2023.
- **THOR-707** (SAR444245): non-alpha IL-2; avoids CD25 → no Treg expansion; tumor immunity focus.
- **Rezpegaldesleukin** (LY3471851): CD122 agonist; Phase 2.

These agents aim to preserve anti-tumor IL-2 activity while avoiding VLS (Treg-independent) and without the oncologic concern of Treg expansion.

## Connections

- **Modulates** → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — IL-2 is the primary autocrine/paracrine T cell growth factor; produced by Th1/Th2/Th17 cells after TCR + CD28 co-stimulation → JAK1/JAK3/STAT5 → cyclin D, BCL-2, BCL-XL → proliferation; NFAT drives IL-2 gene transcription blocked by cyclosporine/tacrolimus.
- **Modulates** → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — IL-2 is essential for Treg development, survival, and FOXP3 maintenance via CD25 (high on Tregs) → STAT5; low-dose IL-2 selectively expands Tregs in SLE, GVHD, and T1D clinical trials; Treg depletion (anti-CD25) releases anti-tumor immunity.
- `connects-to` → **[CIDP](../../07-system/cidp/README.md)** — CD4+ T cells (IL-2-dependent) drive macrophage-mediated paranodal demyelination in CIDP; Treg dysfunction may predispose; low-dose IL-2 Treg expansion is under investigation as adjunct therapy in refractory CIDP.
- `connects-to` → **[Immune Thrombocytopenia](../../07-system/immune-thrombocytopenia/README.md)** — Low-dose IL-2 selectively expands Tregs in ITP → restores immune tolerance and reduces anti-platelet IgG in pilot trials; calcineurin inhibitor-mediated NFAT blockade prevents IL-2 production → broad T cell immunosuppression.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin dephosphorylates NFAT to drive IL-2 transcription; cyclosporine/tacrolimus block calcineurin → NFAT cytoplasmic → IL-2 abolished → T cell expansion prevented; NFAT+AP-1+NF-κB combinatorially govern the IL-2 promoter as an AND-gate.

[^morgan-1976-il2-discovery]: Morgan DA, Ruscetti FW, Gallo R. Selective in vitro growth of T lymphocytes from normal human bone marrows. *Science.* 1976;193(4257):1007-1008. [doi:10.1126/science.181845](https://doi.org/10.1126/science.181845) · [PubMed 181845](https://pubmed.ncbi.nlm.nih.gov/181845/)
[^lotze-1985-aldesleukin-rcc]: Rosenberg SA, Lotze MT, Muul LM, et al. Observations on the systemic administration of autologous lymphokine-activated killer cells and recombinant interleukin-2 to patients with metastatic cancer. *N Engl J Med.* 1985;313(23):1485-1492. [doi:10.1056/NEJM198512053132327](https://doi.org/10.1056/NEJM198512053132327) · [PubMed 3903516](https://pubmed.ncbi.nlm.nih.gov/3903516/)
[^klatzmann-2015-lowdose-il2-review]: Klatzmann D, Abbas AK. The promise of low-dose interleukin-2 therapy for autoimmune and inflammatory diseases. *Nat Rev Immunol.* 2015;15(5):283-294. [doi:10.1038/nri3823](https://doi.org/10.1038/nri3823) · [PubMed 25882245](https://pubmed.ncbi.nlm.nih.gov/25882245/)
[^abbas-immunology-9e]: Abbas AK, Lichtman AH, Pillai S. *Cellular and Molecular Immunology.* 9th ed. Elsevier; 2018.

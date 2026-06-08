---
schema: human-scale-entry/v1
id: aquaporin-4
name: Aquaporin-4
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "Aquaporin-4 (AQP4; chr18q11.2) is the principal water channel of CNS astrocyte endfeet; AQP4-IgG (anti-AQP4) is pathognomonic for NMOSD and drives complement-mediated astrocyte destruction → optic neuritis and transverse myelitis. Eculizumab (FDA 2019) prevents CNS attacks."
aliases: ["aquaporin-4", "AQP4", "NMO-IgG", "anti-AQP4 antibody", "M1-AQP4", "M23-AQP4", "water channel", "AQP4-IgG"]
sources:
  - id: lennon-2004-aqp4-antibody-nmo
    type: peer-reviewed
    cite: "Lennon VA, Wingerchuk DM, Kryzer TJ, et al. A serum autoantibody marker of neuromyelitis optica: distinction from multiple sclerosis. Lancet. 2004;364(9451):2106-2112."
    doi: "10.1016/S0140-6736(04)17551-X"
    pmid: "15589308"
    url: "https://doi.org/10.1016/S0140-6736(04)17551-X"
  - id: wingerchuk-2015-nmosd-criteria
    type: peer-reviewed
    cite: "Wingerchuk DM, Banwell B, Bennett JL, et al. International consensus diagnostic criteria for neuromyelitis optica spectrum disorders. Neurology. 2015;85(2):177-189."
    doi: "10.1212/WNL.0000000000001729"
    pmid: "26092914"
    url: "https://doi.org/10.1212/WNL.0000000000001729"
  - id: bhatt-2019-eculizumab-prevent
    type: peer-reviewed
    cite: "Pittock SJ, Berthele A, Fujihara K, et al. Eculizumab in Aquaporin-4-Positive Neuromyelitis Optica Spectrum Disorder. N Engl J Med. 2019;381(7):614-625."
    doi: "10.1056/NEJMoa1900866"
    pmid: "31050279"
    url: "https://doi.org/10.1056/NEJMoa1900866"
  - id: verkman-2013-aqp4-review
    type: peer-reviewed
    cite: "Verkman AS, Phuan PW, Asavapanumas N, Tradtrantip L. Biology of AQP4 and anti-AQP4 antibody: therapeutic implications for NMO. Brain Pathol. 2013;23(6):684-695."
    doi: "10.1111/bpa.12085"
    pmid: "24118858"
    url: "https://doi.org/10.1111/bpa.12085"
cross_links:
  - target: 01-human/07-system/nmo
    relation: connects-to
    note: "AQP4-IgG (anti-aquaporin-4) binds AQP4 on astrocyte endfeet → complement activation → MAC deposition → astrocyte lysis → secondary demyelination; pathognomonic for AQP4-IgG+ NMOSD in ~85% of cases; ELISA and cell-based assay are diagnostic tests."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "AQP4-IgG activates classical complement → C5 → C5a (eosinophil/neutrophil chemoattractant) + C5b → MAC → astrocyte lysis; eculizumab (PREVENT: ARR 0.02 vs 0.35; FDA Jun 2019) and ravulizumab (CHAMPION-NMOSD; FDA Jun 2023) block C5 to halt attacks."
  - target: 01-human/06-organ/brain
    relation: part-of
    note: "AQP4 is the dominant water channel in CNS astrocyte endfeet at blood-brain barrier; regulates brain water homeostasis and interstitial fluid pressure; high-density expression at perivascular endfeet explains the perivascular location of NMOSD lesions."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 promotes plasmablast differentiation → AQP4-IgG production in NMOSD; satralizumab (anti-IL-6R; FDA Aug 2020) reduces AQP4-IgG titers and prevents CNS attacks; IL-6 also drives Th17 differentiation, amplifying neuroinflammation."
---

# Aquaporin-4

## Overview

**Aquaporin-4 (AQP4)** is a member of the aquaporin family of water-selective transmembrane channels and is the **most abundantly expressed aquaporin in the central nervous system**. It is critical for water homeostasis in the brain and spinal cord — controlling the movement of water across the blood-brain barrier (BBB) astrocyte endfeet, the ependymal layer lining the ventricles, and the glia limitans at the brain surface [^verkman-2013-aqp4-review].

AQP4 holds extraordinary clinical significance because it is the **target autoantigen in neuromyelitis optica spectrum disorder (NMOSD)**: anti-AQP4 IgG autoantibodies (AQP4-IgG, also called NMO-IgG) were identified in 2004 [^lennon-2004-aqp4-antibody-nmo] and revolutionized understanding of NMOSD as a distinct disease from multiple sclerosis. AQP4-IgG binds AQP4 on astrocyte endfeet → activates complement → astrocyte destruction → secondary oligodendrocyte death and demyelination → severe and often irreversible neurological attacks.

**Discovery:** Vanda Lennon and colleagues at Mayo Clinic identified a serum IgG autoantibody ("NMO-IgG") in NMOSD patients in 2004; the target antigen was identified as AQP4 in 2005, establishing NMOSD as an astrocytopathy rather than a primary demyelinating disease like MS.

## Structure

### Protein architecture

| Feature | Detail |
|:--------|:-------|
| Gene | *AQP4*, chromosome 18q11.2 |
| Protein size | 301 amino acids (~32 kDa) |
| Topology | 6 transmembrane domains (TM1-TM6) + 2 NPA (Asn-Pro-Ala) loops (B and E) forming the water-selective pore |
| Quaternary structure | Forms homotetramers; tetramers aggregate into higher-order **orthogonal arrays of particles (OAPs)** |
| Key isoforms | **M23-AQP4:** OAP-forming long isoform (predominant in astrocyte endfeet); **M1-AQP4:** shorter isoform that limits OAP size |

### Orthogonal arrays of particles (OAPs)

AQP4 tetramers self-assemble into large, regular arrays visible by freeze-fracture electron microscopy. M23-AQP4 drives OAP formation; M1 disrupts it. OAPs are concentrated at perivascular astrocyte endfeet — the interface with the blood-brain barrier — and at the glia limitans.

**Clinical relevance:** AQP4-IgG binds M23-AQP4 within OAPs with higher affinity than monomeric AQP4; OAP clustering enhances complement fixation efficiency → more potent astrocyte destruction in NMOSD.

### Blood-brain barrier localization

AQP4 is enriched at the **astrocyte endfeet** (perivascular processes that wrap around CNS capillaries) — the primary site of NMOSD attack. AQP4 is also expressed at:
- Ependymal cells (lining the ventricular system)
- Müller cells of the retina
- Renal collecting duct (lesser expression)
- Skeletal muscle (sarcolemma)

## Function

### Water transport

AQP4 facilitates **bidirectional osmotic water movement** across the astrocyte membrane at rates ~10× the rate of lipid bilayer diffusion. It is the dominant pathway for:

1. **Edema formation after brain injury** — vasogenic edema (from BBB disruption) and cytotoxic edema (cellular swelling); AQP4 accelerates cytotoxic edema formation, explaining why AQP4-knockout mice have improved outcomes in focal ischemia and hypo-osmotic challenge
2. **Edema resolution** — AQP4 mediates resorption of vasogenic edema from the interstitium
3. **Neural signal transduction** — rapid K⁺ clearance from synapses is partially AQP4-dependent (K⁺ spatial buffering)
4. **Astroglial migration and gliosis** — AQP4 facilitates astrocyte volume changes needed for cell migration; important in wound healing and gliosis after CNS injury

### Blood-brain barrier regulation

AQP4 modulates interstitial fluid dynamics and glymphatic system function — the recently described peri-arterial CSF influx pathway that clears metabolic waste (including amyloid-β). AQP4 downregulation is associated with impaired glymphatic clearance and increased amyloid deposition in Alzheimer's models.

## Mechanism

### AQP4-IgG pathogenesis

AQP4-IgG (predominantly IgG1 in AQP4+ NMOSD) targets extracellular domains of AQP4 on astrocyte endfeet [^lennon-2004-aqp4-antibody-nmo]:

**Step 1 — Antibody binding:** AQP4-IgG crosses the BBB (particularly at regions of mild barrier dysfunction), binds AQP4 on astrocyte endfeet. Both IgG1 (complement-activating) and IgG4 (non-complement-activating) AQP4 autoantibodies are detected, but IgG1 predominates.

**Step 2 — Complement activation:** AQP4-IgG–AQP4 complexes activate the classical complement pathway:
- C1q binds IgG Fc → C4b2a (C3 convertase) → C3b → C4b2a3b (C5 convertase) → **C5** → C5a + C5b
- C5b → C5b-9 (membrane attack complex; MAC) deposits on astrocyte membrane → astrocyte lysis

**Step 3 — Cellular immune amplification:** C5a attracts **eosinophils** (prominent in early NMOSD lesions, more than in MS), macrophages, and neutrophils → release of secondary mediators → oligodendrocyte killing and demyelination

**Step 4 — Astrocyte loss:** Granulocyte-mediated astrocyte loss → loss of astrocytic support for oligodendrocytes → secondary demyelination → leukoencephalopathy. Surviving astrocytes show reduced AQP4 and GFAP expression in chronic lesions.

**Complement dependence:** This complement-dependent mechanism explains why:
- C5 inhibitors (eculizumab, ravulizumab) are highly effective in AQP4-IgG+ NMOSD
- Plasma exchange (removing IgG and complement components) is acutely effective
- IFN-β, which increases complement activation in some contexts, may worsen NMOSD

### MOG-IgG (non-AQP4 NMOSD)

~10–15% of NMOSD have **MOG-IgG** (anti-myelin oligodendrocyte glycoprotein, predominantly IgG1); the disease mechanism differs:
- MOG is expressed on oligodendrocyte and myelin sheaths (not astrocytes) → primary demyelination without astrocyte loss
- Lesions tend to be cortical (leukocortical pattern) vs. periventricular/perivascular in AQP4-IgG+ NMOSD
- MOG-IgG+ disease is often monophasic and milder; prognosis differs
- Eculizumab is NOT approved for MOG-IgG+ NMOSD

## Connections

- `connects-to` → **[NMOSD](../../07-system/nmo/README.md)** — AQP4-IgG (anti-aquaporin-4) binds AQP4 on astrocyte endfeet → complement activation → MAC deposition → astrocyte lysis → secondary demyelination; pathognomonic for AQP4-IgG+ NMOSD in ~85% of cases; ELISA and cell-based assay are diagnostic tests.
- `connects-to` → **[Complement C5](../complement-c5/README.md)** — AQP4-IgG activates classical complement → C5 → C5a (chemoattractant) + C5b → MAC → astrocyte lysis; eculizumab (PREVENT: ARR 0.02 vs 0.35; FDA Jun 2019) and ravulizumab (CHAMPION-NMOSD; FDA Jun 2023) block C5 to halt attacks.
- `part-of` → **[Brain](../../06-organ/brain/README.md)** — AQP4 is the dominant water channel in CNS astrocyte endfeet at the blood-brain barrier; regulates brain water homeostasis and interstitial fluid pressure; high-density OAP expression at perivascular endfeet explains the perivascular location of NMOSD lesions.
- `connects-to` → **[IL-6](../il-6/README.md)** — IL-6 promotes plasmablast differentiation → AQP4-IgG production in NMOSD; satralizumab (anti-IL-6R; FDA Aug 2020) reduces AQP4-IgG titers and prevents CNS attacks; IL-6 also drives Th17 differentiation, amplifying neuroinflammation.

[^lennon-2004-aqp4-antibody-nmo]: Lennon VA, Wingerchuk DM, Kryzer TJ, et al. A serum autoantibody marker of neuromyelitis optica: distinction from multiple sclerosis. *Lancet.* 2004;364(9451):2106-2112. [doi:10.1016/S0140-6736(04)17551-X](https://doi.org/10.1016/S0140-6736(04)17551-X) · [PubMed 15589308](https://pubmed.ncbi.nlm.nih.gov/15589308/)
[^wingerchuk-2015-nmosd-criteria]: Wingerchuk DM, Banwell B, Bennett JL, et al. International consensus diagnostic criteria for neuromyelitis optica spectrum disorders. *Neurology.* 2015;85(2):177-189. [doi:10.1212/WNL.0000000000001729](https://doi.org/10.1212/WNL.0000000000001729) · [PubMed 26092914](https://pubmed.ncbi.nlm.nih.gov/26092914/)
[^bhatt-2019-eculizumab-prevent]: Pittock SJ, Berthele A, Fujihara K, et al. Eculizumab in Aquaporin-4-Positive Neuromyelitis Optica Spectrum Disorder. *N Engl J Med.* 2019;381(7):614-625. [doi:10.1056/NEJMoa1900866](https://doi.org/10.1056/NEJMoa1900866) · [PubMed 31050279](https://pubmed.ncbi.nlm.nih.gov/31050279/)
[^verkman-2013-aqp4-review]: Verkman AS, Phuan PW, Asavapanumas N, Tradtrantip L. Biology of AQP4 and anti-AQP4 antibody: therapeutic implications for NMO. *Brain Pathol.* 2013;23(6):684-695. [doi:10.1111/bpa.12085](https://doi.org/10.1111/bpa.12085) · [PubMed 24118858](https://pubmed.ncbi.nlm.nih.gov/24118858/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

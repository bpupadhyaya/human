---
schema: human-scale-entry/v1
id: photon
name: Photon
atlas: 01-human
scale: 01-subatomic
status: draft
last_reviewed: 2026-06-05
summary: "Quantum of electromagnetic radiation. UV photons (200–400 nm) cause pyrimidine dimers in DNA; ionizing γ/X-ray photons generate double-strand breaks via free radicals. Visible photons (400–700 nm) drive retinal photoisomerization, circadian signalling."
aliases: ["γ-ray", "X-ray", "UV photon", "visible light", "electromagnetic quantum", "hν"]
sources:
  - id: sancar-2004-dna-repair
    type: peer-reviewed
    cite: "Sancar A, Lindsey-Boltz LA, Ünsal-Kaçmaz K, Linn S. Molecular mechanisms of mammalian DNA repair and the DNA damage checkpoints. Annu Rev Biochem. 2004;73:39-85."
    doi: "10.1146/annurev.biochem.73.011303.073723"
    pmid: "15189136"
    url: "https://doi.org/10.1146/annurev.biochem.73.011303.073723"
  - id: lobrich-2007-g2m-checkpoint
    type: peer-reviewed
    cite: "Löbrich M, Jeggo PA. The impact of a negligent G2/M checkpoint on genomic instability and cancer induction. Nat Rev Cancer. 2007;7(11):861-9."
    doi: "10.1038/nrc2248"
    pmid: "17943134"
    url: "https://doi.org/10.1038/nrc2248"
cross_links:
  - target: 01-human/01-subatomic/electron
    relation: modulates
    note: "Photon absorption raises electrons to higher energy states (excitation) or ejects them from orbitals (ionization). UV photons promote DNA base electrons to reactive singlet states, enabling covalent bond formation between adjacent pyrimidines."
  - target: 01-human/04-cellular/hepatocyte
    relation: damages
    note: "Ionizing photons (γ-rays, X-rays) generate hydroxyl radicals via radiolysis that produce double-strand breaks in hepatocyte DNA, triggering apoptosis or — if misrepaired — neoplastic transformation. Liver parenchyma is radiosensitive, constraining radiotherapy doses."
  - target: 01-human/07-system/psoriasis
    relation: connects-to
    note: "Narrow-band UVB (311–313 nm) phototherapy induces apoptosis of T cells in psoriatic plaques, suppresses Th17/IL-17A axis, and upregulates regulatory T cells; NBUVB achieves PASI 75 in 50–70% of patients; first-line for extensive plaque psoriasis and safe in pregnancy."
  - target: 01-human/07-system/melanoma
    relation: damages
    note: "UV-B photons cause cyclobutane pyrimidine dimers and C→T UV signature mutations in BRAF, NRAS, and TP53 in melanocytes; UV-A generates ROS → 8-oxoguanine; melanoma carries the highest UV mutational burden (~10 mutations/Mb) of all human cancers."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Photons drive rod and cone phototransduction; UV-A cumulatively crosslinks crystallin proteins → nuclear cataract; photodynamic therapy (PDT: verteporfin + 689 nm laser) treats subfoveal choroidal neovascularization in neovascular AMD."
---

# Photon

## Overview

The photon is the fundamental quantum — the indivisible particle — of electromagnetic radiation. Unlike all other particles in biology, the photon has zero rest mass, travels at the speed of light in vacuum (c = 2.998 × 10⁸ m/s), and carries energy exclusively as a function of its frequency: **E = hν**, where h is Planck's constant (6.626 × 10⁻³⁴ J·s) and ν is frequency [^sancar-2004-dna-repair]. Equivalently, E = hc/λ, where λ is wavelength.

The photon occupies a unique position in the biology atlas: it is not a component of matter, yet it is one of the primary **exogenous physical agents** that interacts with biological molecules, cells, and tissues. Its biological effects span from the life-sustaining (visible photons driving retinal photoisomerization and circadian pacemaking) to the life-threatening (ionizing photons causing DNA double-strand breaks and oncogenesis).

Historically, the biological importance of photons was recognized incrementally. Wilhelm Röntgen's discovery of X-rays in 1895 was immediately applied medically, and within years both therapeutic uses (radiology) and harmful effects (radiation burns, malignancy in early radiology workers) were documented. The UV–DNA damage connection was established through action spectroscopy in the 1930s and 1940s, culminating in the molecular identification of cyclobutane pyrimidine dimers. The photoreactivation and nucleotide excision repair pathways were worked out biochemically through the second half of the twentieth century, with Sancar's Nobel Prize–recognized mechanistic work completing the picture [^sancar-2004-dna-repair].

## Structure

### Physical Properties

| Property | Value |
|:---|:---|
| Rest mass | 0 (massless boson) |
| Charge | 0 |
| Spin | 1 (boson) |
| Energy formula | E = hν = hc/λ |
| Speed in vacuum | 2.998 × 10⁸ m/s |
| Wave–particle duality | Both wave (diffraction, interference) and particle (photoelectric effect, Compton scattering) |

### The Electromagnetic Spectrum — Biological Subdivisions

| Region | Wavelength | Photon energy | Primary biological target / effect |
|:---|:---|:---|:---|
| **Gamma (γ) rays** | <0.01 nm | >100 keV | Ionization, DSBs, radiolysis; cancer therapy, PET |
| **X-rays** | 0.01–10 nm | 100 eV – 100 keV | Ionization, DSBs; diagnostic imaging, radiation therapy |
| **Far UV / germicidal UV-C** | 100–280 nm | 4.4–12.4 eV | Cyclobutane pyrimidine dimers (CPDs) in DNA; 254 nm peak |
| **UV-B** | 280–315 nm | 3.9–4.4 eV | CPDs and 6-4 photoproducts; sunburn, skin carcinogenesis |
| **UV-A** | 315–400 nm | 3.1–3.9 eV | Indirect DNA damage via reactive oxygen species; melanin photodegradation |
| **Visible** | 400–700 nm | 1.8–3.1 eV | Retinal 11-cis → all-trans isomerization (rhodopsin); melanopsin/circadian |
| **Near infrared** | 700–2500 nm | 0.5–1.8 eV | Thermal; photobiomodulation |
| **Microwave / radio** | >1 mm | <1.2 meV | Non-ionizing; NMR/MRI signal |

### Ionizing vs. Non-Ionizing Threshold

The ionization threshold for carbon (the most common element in organic molecules) is approximately 11.3 eV, corresponding to ~110 nm (deep UV-C). In practice, photons with E ≥ ~10 eV (i.e., UV-C and shorter wavelengths) are considered ionizing for biological purposes. **Gamma rays and X-rays** have photon energies three to six orders of magnitude higher than this threshold.

## Function

### UV Photons and DNA Damage

UV-B and UV-C photons are directly absorbed by the conjugated ring systems of the DNA bases thymine and cytosine. The excited electronic state produced by UV absorption (singlet ¹(Py)* or triplet ³(Py)*) drives covalent bond formation between adjacent pyrimidines on the same strand, producing two major photoproducts [^sancar-2004-dna-repair]:

1. **Cyclobutane pyrimidine dimers (CPDs):** A cyclobutane ring bridges C5 and C6 of two adjacent pyrimidines. The most common lesion (~75% of UV damage). CPDs distort the DNA helix, blocking replicative polymerases.

2. **6-4 photoproducts (6-4 PPs):** A covalent bond between C6 of one pyrimidine and C4 of the next. Less frequent (~25%) but more helix-distorting and mutagenic.

Both lesions block RNA polymerase II transcription and stall replication forks, triggering the DNA damage response (ATR kinase pathway). If unrepaired before S-phase entry, CPDs produce C→T and CC→TT transition mutations — the **UV signature mutations** diagnostic of solar skin cancers (BCC, SCC, melanoma).

**Repair: Nucleotide Excision Repair (NER):** The dominant repair pathway for bulky UV lesions. A 12-subunit damage recognition complex (XPC–RAD23B in global genome NER, or stalled RNA Pol II in transcription-coupled NER) recruits TFIIH helicases (XPB, XPD) to unwind ~30 bp around the lesion. XPA verifies the damage. XPG and XPF–ERCC1 endonucleases make dual incisions, excising a 25–30 nt oligonucleotide containing the lesion. Gap-fill synthesis and ligation complete the repair [^sancar-2004-dna-repair].

### Ionizing Photons (X-rays, γ-rays) and Double-Strand Breaks

Ionizing photons interact with biological tissue primarily through:

1. **Photoelectric effect** (dominant at <0.1 MeV): The photon ejects an inner-shell electron; the released photoelectron ionizes surrounding molecules.
2. **Compton scattering** (dominant at 0.1–10 MeV): The photon deflects and ejects a recoil electron, which produces a track of ionizations.
3. **Pair production** (>1.022 MeV): The photon is annihilated and an electron–positron pair is created.

In all cases, the **primary biological damage** is produced by secondary electrons (and OH• radicals from water radiolysis). The hydroxyl radical (OH•) is the most damaging species: it abstracts hydrogen from the deoxyribose backbone, producing strand breaks. **Double-strand breaks (DSBs)** — where both strands are cleaved within ~10 bp — are the most cytotoxic and mutagenic lesion [^lobrich-2007-g2m-checkpoint].

**DSB Quantification:** 1 Gy of ionizing radiation produces approximately 25–40 DSBs per diploid mammalian cell. A single unrepaired DSB is sufficient to trigger apoptosis in a differentiated cell or — in a cycling cell with a faulty G2/M checkpoint — to drive chromosomal rearrangement and oncogenic transformation.

**Repair Pathways for DSBs:**
- **Non-homologous end joining (NHEJ):** Rapid, dominant in G1 and early S phase. Error-prone (can produce insertions/deletions at junctions). Relies on Ku70/Ku80, DNA-PKcs, XRCC4-LigaseIV.
- **Homologous recombination (HR):** High-fidelity, requires sister chromatid (late S/G2). BRCA1, BRCA2, RAD51, RPA. The basis of cancer-associated BRCA1/2 mutation predisposition.

The G2/M DNA damage checkpoint — mediated by ATM→CHK2→CDC25C and ATR→CHK1→CDC25A signalling — arrests cells with unrepaired DSBs before mitosis. Failure of this checkpoint allows cells to enter mitosis with broken chromosomes, generating micronuclei, lagging chromosomes, and aneuploidy — an early step in carcinogenesis [^lobrich-2007-g2m-checkpoint].

### Visible Photons and Phototransduction

At the long-wavelength end of the spectrum, visible photons (400–700 nm, E ≈ 1.8–3.1 eV) are harnessed rather than tolerated:

- **Rhodopsin / rod phototransduction:** A 500 nm photon is absorbed by the 11-cis retinal chromophore of rhodopsin. The photon isomerizes 11-cis to all-trans retinal within 200 femtoseconds — one of the fastest chemical reactions in biology. This conformational change activates transducin (a G protein), triggering a cGMP phosphodiesterase cascade that hyperpolarizes the rod photoreceptor.

- **Melanopsin and circadian entrainment:** Intrinsically photosensitive retinal ganglion cells (ipRGCs) express melanopsin (peak absorption ~480 nm). Photon-driven melanopsin activation projects via the retinohypothalamic tract to the suprachiasmatic nucleus (SCN), synchronizing the ~24-hour circadian oscillator to the light–dark cycle.

- **Vitamin D synthesis:** UV-B photons (290–315 nm) penetrate the epidermis and photolyze 7-dehydrocholesterol to pre-vitamin D₃, which thermally isomerizes to vitamin D₃. Inadequate UV-B exposure is the commonest cause of vitamin D deficiency worldwide.

### Photon Interactions by Tissue Type

| Tissue | Radiation sensitivity | Reason |
|:---|:---|:---|
| Bone marrow (haematopoietic cells) | Very high | Rapidly dividing; critical for immune and red cell production |
| Gut epithelium | High | High cell turnover; stem cells at crypt base |
| Gonads | High | Germ cells; reproductive consequences of mutation |
| Hepatocytes | Moderate | Post-mitotic in adults; DNA damage triggers apoptosis more than proliferation |
| Muscle, nerve | Low | Post-mitotic; do not pass mutant DNA to daughters; mitotic death uncommon |

## Connections

- `modulates` → **[Electron](../../01-subatomic/electron/README.md)** — Photon absorption promotes electrons to higher energy states (excitation) or ejects them entirely (ionization). UV photons cause electronic excitation of DNA base π-systems, leading to pyrimidine dimer formation; ionizing photons eject electrons from water, generating OH• radicals.
- `damages` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — Ionizing photons (γ-rays, X-rays) produce DSBs in hepatocyte DNA via water radiolysis; acute high-dose irradiation causes radiation hepatitis; mean liver dose is strictly constrained in radiotherapy treatment planning to preserve parenchymal regenerative capacity.
- `connects-to` → **[Psoriasis](../../07-system/psoriasis/README.md)** — Narrow-band UVB (311–313 nm) phototherapy induces T-cell apoptosis in psoriatic plaques, suppresses the Th17/IL-17A axis, and upregulates regulatory T cells; NBUVB achieves PASI 75 in 50–70% of patients and is safe in pregnancy.
- `damages` → **[Melanoma](../../07-system/melanoma/README.md)** — UV-B photons cause cyclobutane pyrimidine dimers and C→T UV signature mutations in BRAF, NRAS, and TP53 in melanocytes; UV-A generates ROS → 8-oxoguanine; melanoma carries the highest UV mutational burden (~10 mutations/Mb) of all human cancers.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Photons drive rod and cone phototransduction; UV-A cumulatively crosslinks lens crystallin proteins → nuclear cataract; photodynamic therapy (PDT: verteporfin + 689 nm laser) treats subfoveal choroidal neovascularization in neovascular AMD.

## Pathology

| Condition | Photon type | Mechanism |
|:---|:---|:---|
| Sunburn (erythema) | UV-B (290–315 nm) | CPD/6-4PP formation → apoptosis of keratinocytes → inflammatory response |
| Skin cancer (BCC/SCC) | Cumulative UV-B | Unrepaired CPDs in p53 and PTCH/RAS → CC→TT mutations |
| Melanoma | UV-A + UV-B | Indirect ROS (UV-A) + direct CPDs (UV-B) in melanocytes |
| Cataract | UV-A cumulative | Oxidative crosslinking of crystallin proteins in lens |
| Radiation sickness | Ionizing (γ/X) | Bone marrow failure (aplastic anaemia) from HSC killing |
| Radiation-induced malignancy | Ionizing (γ/X) | Misrepaired DSBs → chromosomal translocations, oncogene activation |

## Open Questions

- **Bystander effect:** Cells not directly irradiated exhibit DNA damage and apoptosis after exposure of neighbouring cells. The mediators (gap-junction signals, secreted ROS, exosomes) are incompletely characterised.
- **Low-dose linearity:** Whether the linear no-threshold (LNT) model accurately describes cancer risk at doses <100 mSv remains contested; adaptive responses (upregulation of repair and antioxidant pathways) may provide a hormetic benefit at very low doses.
- **Photobiomodulation:** Near-infrared photons (630–850 nm) applied to tissue (laser or LED therapy) appear to modulate mitochondrial cytochrome c oxidase activity. The molecular mechanism — putatively photon-driven changes in the redox state of the binuclear centre — and clinical utility are active research areas.

## See Also

- [Electron](../../01-subatomic/electron/README.md) — particle excited or ejected by photon absorption.
- [Hepatocyte](../../04-cellular/hepatocyte/README.md) — cell damaged by ionizing photons via DSB induction.

[^sancar-2004-dna-repair]: Sancar A, Lindsey-Boltz LA, Ünsal-Kaçmaz K, Linn S. Molecular mechanisms of mammalian DNA repair and the DNA damage checkpoints. *Annu Rev Biochem.* 2004;73:39-85. [doi:10.1146/annurev.biochem.73.011303.073723](https://doi.org/10.1146/annurev.biochem.73.011303.073723) · [PubMed 15189136](https://pubmed.ncbi.nlm.nih.gov/15189136/)
[^lobrich-2007-g2m-checkpoint]: Löbrich M, Jeggo PA. The impact of a negligent G2/M checkpoint on genomic instability and cancer induction. *Nat Rev Cancer.* 2007;7(11):861-9. [doi:10.1038/nrc2248](https://doi.org/10.1038/nrc2248) · [PubMed 17943134](https://pubmed.ncbi.nlm.nih.gov/17943134/)

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

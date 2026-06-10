---
schema: human-scale-entry/v1
id: abl1
name: ABL1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Non-receptor tyrosine kinase; fused with BCR in CML (t(9;22)) → constitutive BCR-ABL → RAS-MAPK, STAT5, and PI3K → leukemic proliferation. Imatinib, dasatinib, nilotinib are ABL inhibitors; asciminib (STAMP) and ponatinib overcome T315I gatekeeper resistance."
aliases: ["ABL", "ABL1", "BCR-ABL", "BCR-ABL1", "c-ABL", "Philadelphia chromosome kinase", "p210 BCR-ABL", "CML kinase", "Abelson kinase"]
sources:
  - id: druker-2001-imatinib-iris
    type: peer-reviewed
    cite: "Druker BJ, Talpaz M, Resta DJ, et al. Efficacy and safety of a specific inhibitor of the BCR-ABL tyrosine kinase in chronic myeloid leukemia. N Engl J Med. 2001;344(14):1031-1037."
    doi: "10.1056/NEJM200104053441401"
    pmid: "11287973"
    url: "https://doi.org/10.1056/NEJM200104053441401"
  - id: hochhaus-2017-asciminib
    type: peer-reviewed
    cite: "Hochhaus A, Boquimpani C, Rea D, et al. Efficacy and safety results from ASCEMBL, a multicenter, open-label, phase 3 study of asciminib vs bosutinib in chronic-phase CML. Blood. 2021;138(Suppl 1):2160."
    doi: "10.1182/blood-2021-147441"
    pmid: "34739052"
    url: "https://doi.org/10.1182/blood-2021-147441"
cross_links:
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "BCR-ABL activates SRC family kinases (LYN, HCK, FGR) → downstream CrkL, STAT5, and PI3K signaling; dasatinib inhibits both BCR-ABL and SRC kinases — dual mechanism vs. imatinib (ABL-only); SRC-mediated BCR-ABL-independent survival contributes to imatinib resistance in CML."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "BCR-ABL activates STAT5 (dominant) and STAT3 → BCL-XL, MYC, and cyclin D1 → CML blast proliferation; STAT5 is essential for CML LSC maintenance; FLT3+JAK2 inhibitors combined with TKI target STAT5 in TKI-persistent CML stem cells in preclinical models."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "BCR-ABL → PI3K-AKT → mTORC1 → protein synthesis and CML stem cell (LSC) maintenance; mTOR is active in quiescent CML LSCs; TKI + mTOR inhibitor combinations eliminate CML LSC reservoir in mouse models and may improve treatment-free remission rates in deep molecular responders."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "BCR-ABL activates RAS via GRB2-SOS → RAF-MEK-ERK → proliferation; KRAS mutations are rare in chronic-phase CML but selected in blast crisis; RAS/MAPK activation is a BCR-ABL-independent bypass mechanism contributing to TKI resistance in accelerated-phase and blast-phase CML."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "c-Abl is activated by ATM at DSBs → phosphorylates MDM2 Tyr394 → blocks MDM2-p53 ubiquitination → p53 stabilization → apoptosis; BCR-ABL disrupts ATM-c-Abl-p53 axis → CML cell survival; TP53 mutations accumulate in blast crisis as escape from p53-dependent apoptosis."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "NK cells mediate CML immune surveillance during TFR; imatinib-treated patients show NK cell expansion and activation; high NK cell count predicts TFR success; TKI therapy normalises NK cell education via KIR licensing, enabling MRD immune control after TKI discontinuation."
  - target: 01-human/03-molecular/rad51
    relation: connects-to
    note: "c-Abl phosphorylates RAD51 Tyr315 → promotes RAD51 nuclear foci at DSBs → HR repair; BCR-ABL-driven RAD51 overactivation elevates HR → accelerates acquisition of BCR-ABL kinase domain resistance mutations; RAD51 inhibition sensitises CML cells to imatinib in preclinical models."
---

# ABL1

## Overview

**ABL1 (Abelson murine leukemia viral oncogene homolog 1, c-Abl)** is a ubiquitously expressed non-receptor tyrosine kinase involved in cell growth, differentiation, DNA damage response, and actin cytoskeletal dynamics. In chronic myeloid leukemia (CML), the translocation t(9;22)(q34;q11) — the **Philadelphia chromosome** — fuses *BCR* (breakpoint cluster region, chromosome 22) to *ABL1* (chromosome 9) → **BCR-ABL fusion protein** → constitutive, ligand-independent ABL kinase activity → unrestrained myeloid proliferation [^druker-2001-imatinib-iris].

The discovery that imatinib (STI571, Gleevec) could specifically inhibit BCR-ABL and achieve complete cytogenetic remission in CML patients (Druker et al., 2001) was a landmark moment in oncology — the first demonstration that targeted kinase inhibition could transform a previously fatal cancer into a chronic, manageable disease. CML has since become the paradigm for targeted cancer therapy and precision oncology.

**ABL1 in normal biology:**
- **Cell cycle control:** c-Abl is activated by DNA double-strand breaks (DSBs) via ATM → c-Abl phosphorylates RAD51, BRCA1, and MDM2 → DNA repair coordination and p53 activation; in response to severe DNA damage, c-Abl promotes apoptosis (phosphorylates FADD, caspase-8)
- **Cytoskeletal remodeling:** c-Abl phosphorylates cortactin, WAVE2, and N-WASP → F-actin dynamics → cell migration and adhesion; BCR-ABL hijacks this function → enhanced migratory and invasive potential
- **Synaptic development:** ABL2 (Arg, Abelson-related gene) is critical for dendritic spine morphogenesis and synapse formation; Abl kinase inhibitors (imatinib) show some neuroprotective effects via Abl2 inhibition in models of Parkinson's disease
- **Normal ABL1 regulation:** c-Abl is autoinhibited by an N-terminal myristoyl group that occupies the C-lobe myristoyl pocket → holds SH3-SH2 "clamp" over the kinase domain; BCR fusion disrupts this myristoyl-mediated autoinhibition → constitutive kinase activity

**BCR-ABL fusion proteins:**
- **p210 BCR-ABL** (major breakpoint region, M-BCR, b2a2 or b3a2 fusion): Present in >95% of CML; the canonical CML kinase; ABL kinase activity ~100-fold above c-Abl
- **p190 BCR-ABL** (minor breakpoint region, m-BCR, e1a2 fusion): Present in ~50% of Ph+ ALL in adults; rare in CML; smaller fusion; typically has worse prognosis in ALL
- **p230 BCR-ABL** (μ-BCR): Very rare; associated with chronic neutrophilic leukemia; indolent CML variant

## Structure

### ABL1 kinase domain structure

ABL1 (1,130 amino acids, ~123 kDa) has a complex domain structure:

**N-terminal region:**
- **Myristoylated Cap:** The first 14 aa of c-Abl are myristoylated → the myristoyl group folds back and occupies a hydrophobic pocket in the C-lobe of the kinase domain → "autoinhibitory cap"; the BCR fusion displaces this cap → constitutive activation; **asciminib** (STAMP inhibitor) binds exactly this myristoyl pocket → restores autoinhibition → allosteric inhibition mechanism [^hochhaus-2017-asciminib]
- **SH3 domain:** Binds PXXP motifs; in autoinhibited c-Abl, SH3 binds the SH2-kinase linker → locks kinase in inactive state (same as SRC kinase)
- **SH2 domain:** Binds pTyr peptides; in autoinhibited state, SH2 contacts the kinase N-lobe → stabilizes inactive conformation; disrupted by BCR fusion

**Kinase domain (SH1):**
- Classic bilobal RTK fold; ATP-binding pocket in N-lobe cleft
- **DFG motif:** DFG-out conformation = inactive; DFG-in = active
- **T315 "gatekeeper" residue:** The threonine gatekeeper makes a critical hydrogen bond with imatinib (and most first/second-generation TKIs); **T315I mutation** → isoleucine is bulkier → steric clash → imatinib, dasatinib, nilotinib all lose binding; T315I is the most common resistance mutation (~15-30% of TKI-resistant CML); only **ponatinib** (contains a carbon-carbon triple bond that accommodates T315I) and **asciminib** (binds myristoyl pocket, not ATP site) overcome T315I

**C-terminal domain:**
- Nuclear localization signals (NLS) × 3: c-Abl shuttles between nucleus (DNA damage response) and cytoplasm (cytoskeletal functions); BCR-ABL is predominantly cytoplasmic (BCR provides cytoplasmic localization → cytoplasmic STAT5/RAS/PI3K activation is the dominant oncogenic signal)
- **F-actin binding domain:** The last 150 aa bind F-actin directly — unique feature of ABL kinases not shared by other RTKs; this actin-binding domain is present in BCR-ABL → BCR-ABL co-localizes with F-actin → activation of actin-dependent signaling
- **DNA-binding domain:** Binds dsDNA (sequence non-specifically) → may facilitate DNA damage response

### BCR contribution to BCR-ABL oncogenesis

The BCR portion of the fusion provides several critical functions:
- **Dimerization:** BCR coiled-coil domain (exons 1-2) → constitutive BCR-ABL dimerization/oligomerization → trans-autophosphorylation → sustained kinase activation; dimerization is required for full oncogenic transformation
- **GRB2 binding site:** BCR pY177 → GRB2 SH2 binding → GRB2-SOS → RAS-GTP → RAF-MEK-ERK; the BCR Y177 → GRB2-RAS axis is independent of ABL kinase activity and contributes to CML transformation
- **Phosphatase activity:** BCR has a Rho-GEF domain and a GTPase-activating protein (GAP) activity for RAC; these domains are disrupted in BCR-ABL → altered cytoskeletal signaling contributes to BCR-ABL-mediated morphological transformation

## Function

### BCR-ABL signaling networks

**RAS-MAPK pathway:**
- BCR pY177 → GRB2-SOS → RAS-GTP → RAF-MEK-ERK → cyclin D1, c-FOS, c-MYC → proliferation
- Alternatively: BCR-ABL (kinase domain) → SHC pTyr → GRB2-SOS → RAS → ERK
- RAS-MAPK is required for BCR-ABL-mediated transformation (dominant-negative RAS abrogates CML cell colony formation)

**STAT5 pathway (dominant survival axis):**
- BCR-ABL directly phosphorylates STAT5 at Y694 (or via JAK2 indirect phosphorylation) → STAT5 dimers → nuclear → BCL-XL, MCL-1, MYC, cyclin D1, PIM kinases → CML cell survival and proliferation
- STAT5 is required for CML stem cell maintenance; STAT5 inhibition alone induces apoptosis in CML LSCs even when BCR-ABL kinase is active; next-generation CML therapy may require STAT5 targeting to eliminate residual LSCs

**PI3K-AKT-mTOR pathway:**
- BCR-ABL → PI3K p85 → PIP3 → AKT → mTORC1 → protein synthesis, cell growth; BCR-ABL also activates PI3K via RAS and via SRC kinases
- mTORC1 is active in CML LSCs; mTOR inhibitors (rapamycin, everolimus) sensitize CML LSCs to imatinib in mouse transplantation models → potential strategy to eliminate MRD and achieve TFR

**SRC family kinase (SFK) activation:**
- BCR-ABL phosphorylates and activates LYN (the dominant SFK in CML), HCK, and FGR → downstream CrkL, STAT5, and PI3K signaling
- Activated LYN phosphorylates BCR-ABL → positive feedback; LYN/HCK → BCR-ABL-independent survival in some TKI-resistant CML lines
- Dasatinib's advantage vs. imatinib: Dual BCR-ABL + SFK inhibition disrupts this feedback and may eliminate residual disease more completely

## Mechanism

### ABL1/BCR-ABL inhibitors

**Imatinib (Gleevec, STI571) — first-generation [^druker-2001-imatinib-iris]:**
- Type II inhibitor binding BCR-ABL in DFG-out (inactive) conformation; competitive with ATP; also inhibits KIT and PDGFR
- IRIS trial (2001): Imatinib vs. IFN-alpha in newly diagnosed CML → 5-year CCyR 69%, 5-year OS 89%; landmark that defined TKI-based CML therapy
- **Resistance:** ~30% of patients need TKI switch; mechanisms: T315I (15-30%), E255K/V, F359C/V (domain mutations changing ATP-binding pocket shape); BCR-ABL amplification; T315I is imatinib-cross-resistant to all 2nd-gen TKIs

**Nilotinib (Tasigna) — second-generation:**
- Type II, more potent vs. BCR-ABL than imatinib (~30×); also inhibits KIT, PDGFR; does NOT inhibit SRC kinases
- ENESTnd trial: Nilotinib vs. imatinib frontline → deeper molecular responses (MR4.5) earlier → more patients eligible for TFR; preferred for high-risk Sokal score; side effects: QTc prolongation, pancreatitis, vascular events (atherosclerosis → PAOD, coronary artery disease); monitoring required

**Dasatinib (Sprycel) — second-generation, dual BCR-ABL+SRC:**
- Type I (DFG-in binding); more potent than imatinib (~300×); inhibits both BCR-ABL and SRC family kinases; active vs. many (not T315I) imatinib-resistant mutations
- DASISION trial: Frontline in CML; faster/deeper molecular response vs. imatinib; side effects: pleural effusion (~25-35%), pulmonary arterial hypertension (rare, <1%); inferior to nilotinib/imatinib for vascular safety

**Bosutinib (Bosulif) — second-generation, dual BCR-ABL+SRC:**
- Type I; minimal KIT/PDGFR inhibition → less off-target effects vs. imatinib; BELA/BFORE trials: Frontline superiority in molecular response vs. imatinib; approved for newly diagnosed and resistant/intolerant CML; diarrhea and hepatotoxicity are dominant side effects

**Ponatinib (Iclusig) — third-generation, pan-BCR-ABL including T315I:**
- Carbon-carbon triple bond → accommodates T315I bulky isoleucine; Type II inhibitor; inhibits T315I, F317L, E255K, and compound mutations; also inhibits SRC, KIT, PDGFR, FGFR, VEGFR
- PACE trial: Active in highly TKI-resistant CML (CCyR ~16% in T315I); approved for T315I and TKI-failure; arterial occlusion (PAOD, coronary, cerebrovascular) — class effect; low-dose ponatinib (15 mg) may reduce vascular risk; OPTIC trial: dose-optimization approach

**Asciminib (Scemblix) — STAMP inhibitor (Specifically Targeting the ABL Myristoyl Pocket) [^hochhaus-2017-asciminib]:**
- Allosteric inhibitor binding the myristoyl pocket (not the ATP site); restores myristoyl cap autoinhibition; active vs. T315I when combined with dose escalation (200 mg BID); minimal off-target (no SRC, KIT, PDGFR inhibition)
- ASCEMBL trial: Asciminib vs. bosutinib in ≥2 prior TKI CML → MMR 25.5% vs. 13.2%; FDA-approved 2021 for ≥2 prior TKIs; also approved for T315I (200 mg BID dose); compound mutations (T315I+E255V, T315I+F317L) may cause asciminib resistance

**Treatment-free remission (TFR):**
- The paradigm-shifting concept in CML: patients achieving sustained deep molecular response (MR4 = BCR-ABL ≤0.01% on IS = 4-log reduction) for ≥2-3 years can attempt TKI discontinuation → TFR in ~50%
- TFR is dependent on immune surveillance (NK cells, T cells) maintaining residual CML cells below threshold; immune function during TKI therapy and NK cell education are critical determinants
- Re-challenge with TKI after molecular relapse → re-induction in virtually all patients

## Connections

- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — BCR-ABL activates SRC family kinases (LYN, HCK, FGR) → downstream CrkL, STAT5, and PI3K signaling; dasatinib inhibits both BCR-ABL and SRC kinases — dual mechanism vs. imatinib (ABL-only); SRC-mediated BCR-ABL-independent survival contributes to imatinib resistance in CML.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — BCR-ABL activates STAT5 (dominant) and STAT3 → BCL-XL, MYC, and cyclin D1 → CML blast proliferation; STAT5 is essential for CML LSC maintenance; FLT3+JAK2 inhibitors combined with TKI target STAT5 in TKI-persistent CML stem cells in preclinical models.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — BCR-ABL → PI3K-AKT → mTORC1 → protein synthesis and CML stem cell (LSC) maintenance; mTOR is active in quiescent CML LSCs; TKI + mTOR inhibitor combinations eliminate CML LSC reservoir in mouse models and may improve treatment-free remission rates in deep molecular responders.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — BCR-ABL activates RAS via GRB2-SOS → RAF-MEK-ERK → proliferation; KRAS mutations are rare in chronic-phase CML but selected in blast crisis; RAS/MAPK activation is a BCR-ABL-independent bypass mechanism contributing to TKI resistance in accelerated-phase and blast-phase CML.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — c-Abl activated by ATM at DSBs phosphorylates MDM2 Tyr394 → blocks MDM2-p53 ubiquitination → p53 stabilization → apoptosis; BCR-ABL disrupts this ATM-c-Abl-p53 axis → CML cell survival; TP53 mutations accumulate in blast crisis as cells escape p53-dependent apoptosis.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — NK cells mediate CML immune surveillance during treatment-free remission (TFR); imatinib-treated patients show NK cell expansion and activation; high NK cell count predicts TFR success; TKI normalises NK cell education via KIR licensing, enabling MRD immune control.
- `connects-to` → **[RAD51](../../03-molecular/rad51/README.md)** — c-Abl phosphorylates RAD51 Tyr315 → promotes RAD51 nuclear foci at DSBs → HR repair; BCR-ABL-driven RAD51 overactivation elevates HR → accelerates acquisition of BCR-ABL kinase domain resistance mutations; RAD51 inhibition sensitises CML cells to imatinib in preclinical models.

[^druker-2001-imatinib-iris]: Druker BJ, Talpaz M, Resta DJ, et al. Efficacy and safety of a specific inhibitor of the BCR-ABL tyrosine kinase in chronic myeloid leukemia. *N Engl J Med.* 2001;344(14):1031-1037. [doi:10.1056/NEJM200104053441401](https://doi.org/10.1056/NEJM200104053441401) · [PubMed 11287973](https://pubmed.ncbi.nlm.nih.gov/11287973/)
[^hochhaus-2017-asciminib]: Hochhaus A, Boquimpani C, Rea D, et al. Efficacy and safety results from ASCEMBL, a multicenter, open-label, phase 3 study of asciminib vs bosutinib in chronic-phase CML. *Blood.* 2021;138(Suppl 1):2160. [doi:10.1182/blood-2021-147441](https://doi.org/10.1182/blood-2021-147441) · [PubMed 34739052](https://pubmed.ncbi.nlm.nih.gov/34739052/)

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

---
schema: human-scale-entry/v1
id: pd-1
name: PD-1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Programmed death receptor 1 (CD279); inhibitory checkpoint on activated T cells. PD-L1 binding recruits SHP-2, dephosphorylating TCR intermediates and suppressing CTL cytotoxicity. Blocked by pembrolizumab/nivolumab — approved immunotherapy in NSCLC, melanoma, and 40+ cancers."
aliases: ["PDCD1", "CD279", "programmed death-1", "PD1", "immune checkpoint receptor"]
sources:
  - id: ishida-1992-pd1
    type: peer-reviewed
    cite: "Ishida Y, Agata Y, Shibahara K, Honjo T. Induced expression of PD-1, a novel member of the immunoglobulin gene superfamily, upon programmed cell death. EMBO J. 1992;11(11):3887-3895."
    doi: "10.1002/j.1460-2075.1992.tb05481.x"
    pmid: "1396582"
    url: "https://doi.org/10.1002/j.1460-2075.1992.tb05481.x"
  - id: dong-2002-pdl1-tumor
    type: peer-reviewed
    cite: "Dong H, Strome SE, Salomao DR, et al. Tumor-associated B7-H1 promotes T-cell apoptosis: a potential mechanism of immune evasion. Nat Med. 2002;8(8):793-800."
    doi: "10.1038/nm730"
    pmid: "12091876"
    url: "https://doi.org/10.1038/nm730"
  - id: topalian-2012-antipd1
    type: peer-reviewed
    cite: "Topalian SL, Hodi FS, Brahmer JR, et al. Safety, activity, and immune correlates of anti-PD-1 antibody in cancer. N Engl J Med. 2012;366(26):2443-2454."
    doi: "10.1056/NEJMoa1200690"
    pmid: "22658127"
    url: "https://doi.org/10.1056/NEJMoa1200690"
cross_links:
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: modulated-by
    note: "PD-1 is highly expressed on CTLs during chronic antigen exposure; PD-L1 on tumor cells recruits SHP-2 → dephosphorylates CD28 and ZAP-70 → suppresses IL-2, IFN-γ production and cytotoxic killing → T cell exhaustion; anti-PD-1 reverses this exhaustion program."
  - target: 01-human/04-cellular/t-helper-cell
    relation: modulated-by
    note: "PD-1 is upregulated on follicular helper T cells (Tfh) and effector CD4+ cells; PD-L1/2 ligation suppresses Tfh–B cell germinal center interactions; PD-1 blockade also restores helper T cell function, enhancing tumor-specific B cell and CTL responses."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "KRAS oncogenic signaling via MEK→ERK and NF-κB transcriptionally upregulates PD-L1 on tumor cells → immune evasion; KRAS inhibition (sotorasib) reduces PD-L1 — basis for combining KRAS and PD-1 pathway inhibitors in NSCLC and CRC clinical trials."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB directly drives PD-L1 (CD274) transcription in tumors and inflammatory contexts; KRAS, EGFR, and PI3K pathways converge on NF-κB to upregulate PD-L1 — adaptive immune resistance mechanism that allows tumors to suppress tumor-infiltrating CTL attack."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "CTLA-4 and PD-1 are complementary checkpoints: CTLA-4 acts at the priming phase (lymph node; competes with CD28 for B7-1/B7-2); PD-1 acts at the effector phase (tumor); ipilimumab+nivolumab dual blockade: 5-year OS 52% in melanoma; sequential resistance mechanisms exist."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "IFN-γ from tumor-infiltrating CTLs → JAK1/2 → STAT1 → IRF1 → CD274 promoter → PD-L1 — termed adaptive immune resistance; IFN-γ is both anti-tumor (killing, macrophage activation) and pro-evasion (PD-L1 induction); JAK1/2 LOF → resistance to IFN-γ → anti-PD-1 resistance."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "MYC directly drives CD274 (PD-L1) transcription via E-box elements; MYC amplification correlates with high PD-L1 in TNBC, lymphoma, and NSCLC; BET inhibitors (JQ1) target MYC → reduce PD-L1; MYC-PD-L1 axis links oncogene amplification to adaptive immune checkpoint upregulation."
---

# PD-1

## Overview

**PD-1 (programmed death 1, CD279, encoded by PDCD1)** is an inhibitory immune checkpoint receptor expressed on activated **T cells, B cells, NK cells, and monocytes**. First described by Honjo and colleagues in 1992 while screening for genes upregulated during T cell apoptosis [^ishida-1992-pd1], PD-1 was subsequently found to be a key **negative regulator of adaptive immunity** — dampening T cell activation to prevent autoimmunity and limit collateral tissue damage during infection resolution.

PD-1 binds two ligands:
- **PD-L1 (CD274, B7-H1):** Broadly expressed; strongly upregulated in tumors, infected cells, and inflamed tissues in response to IFN-γ; also expressed constitutively on resting lymphocytes, macrophages, and placenta
- **PD-L2 (CD273, B7-DC):** More restricted expression; dendritic cells, macrophages, and resting B cells; induced by IL-4, IL-13, GM-CSF

Under physiological conditions, the PD-1/PD-L1 axis maintains **peripheral tolerance** — preventing autoreactive T cells from causing autoimmunity and silencing effector T cells once infection is cleared. In cancer, **tumors exploit PD-L1 overexpression** (via IFN-γ from tumor-infiltrating T cells → STAT1 → IRF1 → PD-L1 — termed "adaptive immune resistance") to suppress CTL cytotoxicity and escape immune elimination [^dong-2002-pdl1-tumor].

**Anti-PD-1/PD-L1 therapy** — arguably the most transformative cancer treatment of the 21st century — blocks this suppressive interaction:
- **Pembrolizumab (Keytruda, anti-PD-1):** FDA-approved in 40+ indications including NSCLC, melanoma, HNSCC, gastric, endometrial, cervical, bladder, HCC, and TMB-high/MSI-H tumors (tissue-agnostic)
- **Nivolumab (Opdivo, anti-PD-1):** Approved for melanoma, NSCLC, RCC, HNSCC, hepatocellular carcinoma, gastric, and others
- **Atezolizumab, durvalumab, avelumab (anti-PD-L1):** Approved for NSCLC, urothelial carcinoma, Merkel cell carcinoma
- **Ipilimumab + nivolumab (anti-CTLA-4 + anti-PD-1):** Synergistic in melanoma and RCC; CTLA-4 blockade acts at priming stage, PD-1 at effector stage

## Structure

### PD-1 protein

PD-1 is a **288 amino acid type I transmembrane protein** of the CD28/CTLA-4 family (immunoglobulin superfamily):
- **Extracellular IgV-like domain (aa 1-149):** The ligand-binding domain; contacts both PD-L1 and PD-L2 through an IgV fold; binding affinity PD-L1: Kd ~0.77 μM, PD-L2: ~3× higher affinity
- **Transmembrane domain (aa 150-170):** Single pass
- **Cytoplasmic tail (aa 171-288):** 95 aa; contains two tyrosines:
  - **ITIM (immunoreceptor tyrosine-based inhibitory motif, Tyr223):** Binds SHP-1 when phosphorylated
  - **ITSM (immunoreceptor tyrosine-based switch motif, Tyr248):** Primary docking site for **SHP-2 (PTPN11)** — the phosphatase mediating PD-1 inhibitory signaling; also binds SHP-1 at reduced affinity

**Structure of inhibition:** TCR activation → Lck phosphorylates ITAM motifs in CD3ζ → ZAP-70 recruited → CD28 (co-stimulatory receptor) phosphorylated by Lck → PI3K recruited → Akt → survival/proliferation. PD-1 ligation → Lck phosphorylates ITSM → SHP-2 binds → SHP-2 dephosphorylates CD28 (Tyr191) → PI3K uncoupled → Akt signaling lost → attenuated T cell activation.

### PD-L1 regulation in tumors [^dong-2002-pdl1-tumor]

PD-L1 expression is induced by multiple overlapping oncogenic pathways:
- **IFN-γ → JAK1/2 → STAT1 → IRF1 → CD274 promoter:** Dominant mechanism; tumor-infiltrating T cells produce IFN-γ → tumor cells upregulate PD-L1 → suppress those same T cells (adaptive immune resistance)
- **KRAS/MAPK → MEK → ERK → transcriptional and epigenetic PD-L1 upregulation**
- **PI3K/Akt/mTOR → NF-κB → PD-L1**
- **MYC → CD274 transcription (direct):** MYC amplification strongly correlates with PD-L1 expression
- **Oncogenic EGFRmut → EGFR→STAT3 → PD-L1:** EGFR-mutant NSCLC upregulates PD-L1 independently of IFN-γ

## Function

### Peripheral tolerance and autoimmunity

PD-1–deficient mice develop:
- Lupus-like glomerulonephritis and dilated cardiomyopathy (on BALB/c background; anti-cardiac troponin I autoantibodies)
- Arthritis and myocarditis (on C57BL/6 background)

Clinical correlate: Anti-PD-1/PD-L1 therapy causes **immune-related adverse events (irAEs)** that phenocopy organ-specific autoimmunity:
- **Colitis (10-20%):** Most common; mimics IBD
- **Pneumonitis (3-5%):** Potentially life-threatening
- **Endocrinopathies:** Hypothyroidism (10-20%), hypophysitis, adrenal insufficiency, type 1 diabetes (rare but permanent)
- **Hepatitis, nephritis, neurotoxicity, myocarditis (rare; <1% but high mortality)**

### T cell exhaustion in cancer

Chronic antigen stimulation in tumors → progressive T cell exhaustion phenotype:
- **Exhaustion markers:** PD-1^high, LAG-3+, TIM-3+, TIGIT+
- **Functional deficits:** Reduced IL-2, IFN-γ, TNF-α production; impaired proliferative capacity; reduced cytotoxicity
- **Transcription factor:** TOX (thymocyte selection-associated HMG box factor) — master regulator of T cell exhaustion; induced by chronic NFAT activation; TOX maintains PD-1, LAG-3, and other inhibitory receptors

Anti-PD-1 therapy can rescue **progenitor exhausted T cells** (PD-1+TCF1+; stem-like) but has limited effect on **terminally exhausted T cells** (PD-1^high, TOX^high, TCF1-).

### Predictive biomarkers [^topalian-2012-antipd1]

| Biomarker | Threshold | Application | Limitation |
|:---|:---|:---|:---|
| PD-L1 TPS | ≥50% | Pembrolizumab monotherapy, 1st-line NSCLC | Imperfect; heterogeneous expression, biopsy timing |
| MSI-H/dMMR | Presence | Pembrolizumab (tissue-agnostic); ORR ~40% | Rare (~4% of all cancers) |
| TMB | ≥10 mut/Mb | Pembrolizumab (tissue-agnostic) | Threshold variable by tumor type |
| EBV/viral | Presence | Pembrolizumab in EBV+ gastric cancer, PD-L1 amplicon | Specific to viral malignancies |

## Mechanism

### Molecular mechanism of PD-1-mediated inhibition

1. TCR antigen recognition → Lck (Src kinase) phosphorylates CD3ζ ITAM motifs → ZAP-70 recruits → phosphorylates LAT, SLP-76, PLC-γ → Ca²⁺ flux → NFAT dephosphorylation → IL-2 transcription; also → Ras→ERK→AP-1; and → PI3K→Akt→NF-κB
2. Simultaneous CD28 co-stimulation → CD28 Tyr191 phosphorylation → PI3K p85 recruitment → PIP3 → PDK1+mTORC2 → Akt (full activation) → CD28-dependent survival, proliferation, IL-2 amplification
3. PD-1 ligation by PD-L1: ITSM (Tyr248) phosphorylated by Lck → SHP-2 ITIM domain binds ITSM → SHP-2 activated → **dephosphorylates CD28 Tyr191** → PI3K uncoupled → Akt signaling collapses → IL-2 lost, survival signals attenuated
4. SHP-2 also dephosphorylates ZAP-70, LAT, PLC-γ → attenuates upstream TCR signaling directly

**Net effect:** PD-1 hijacks the same Lck kinase that activates TCR signaling to phosphorylate its own ITSM → recruit SHP-2 → dismantle the CD28-PI3K-Akt axis that amplifies TCR-induced T cell activation.

### Anti-PD-1 clinical milestones

- **2014:** FDA approves pembrolizumab for ipilimumab-refractory melanoma (first anti-PD-1)
- **2015:** Nivolumab + pembrolizumab approved for NSCLC; ORR 20% vs 1% for docetaxel in chemorefractory NSCLC (Brahmer 2015, NEJM)
- **2017:** Pembrolizumab approved for any MSI-H/dMMR solid tumor — first **tumor-agnostic** approval in FDA history
- **2018:** Pembrolizumab first-line for PD-L1 ≥50% NSCLC (KEYNOTE-024: 45% vs 28% ORR, significantly improved PFS and OS vs platinum doublet)
- **2022:** Pembrolizumab + chemotherapy first-line for triple-negative breast cancer (KEYNOTE-522: 64.8% vs 51.2% pCR)

**Resistance mechanisms:**
- Loss of MHC-I expression (β2-microglobulin mutations) → T cells cannot recognize tumor antigens
- JAK1/2 loss-of-function → insensitivity to IFN-γ → no PD-L1 upregulation paradoxically, but also no antitumor IFN-γ effects
- PTEN loss → PI3K/Akt → exclusion of T cells from tumor microenvironment
- Alternative checkpoint upregulation (TIM-3, LAG-3, TIGIT) → T cell re-exhaustion after PD-1 blockade

## Connections

- `modulated-by` → **[T Cytotoxic Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — PD-1 is expressed on CTLs and drives T cell exhaustion in tumors; tumor PD-L1 binding suppresses CTL cytotoxicity via SHP-2 dephosphorylation of CD28; anti-PD-1 reverses exhaustion and restores CTL killing.
- `modulated-by` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — PD-1 on follicular Th (Tfh) and effector CD4+ cells suppresses GC reactions and Th-dependent immunity; anti-PD-1 also restores helper T cell function, augmenting tumor-specific B cell and CTL responses.
- `connects-to` → **[KRAS](../kras/README.md)** — oncogenic KRAS upregulates PD-L1 via MEK→ERK and NF-κB; KRAS inhibition reduces PD-L1 — rationale for combining KRAS and PD-1 pathway inhibitors in NSCLC and CRC trials.
- `connects-to` → **[NF-κB](../nf-kb/README.md)** — NF-κB directly transcribes PD-L1 in tumors; KRAS, PI3K, and EGFR pathways converge on NF-κB to drive adaptive immune resistance through PD-L1 upregulation.
- `connects-to` → **[CTLA-4](../ctla-4/README.md)** — CTLA-4 and PD-1 are complementary checkpoints: CTLA-4 acts at the priming phase (lymph node; competes with CD28 for B7-1/B7-2); PD-1 acts at the effector phase (tumor); ipilimumab+nivolumab dual blockade: 5-year OS 52% in melanoma; sequential resistance mechanisms exist.
- `connects-to` → **[IFN-γ](../ifn-gamma/README.md)** — IFN-γ from tumor-infiltrating CTLs → JAK1/2 → STAT1 → IRF1 → CD274 promoter → PD-L1 — termed adaptive immune resistance; IFN-γ is both anti-tumor (killing, macrophage activation) and pro-evasion (PD-L1 induction); JAK1/2 LOF → resistance to IFN-γ → anti-PD-1 resistance.
- `connects-to` → **[MYC](../myc/README.md)** — MYC directly drives CD274 (PD-L1) transcription via E-box elements; MYC amplification correlates with high PD-L1 in TNBC, lymphoma, and NSCLC; BET inhibitors (JQ1) target MYC → reduce PD-L1; MYC-PD-L1 axis links oncogene amplification to adaptive immune checkpoint upregulation.

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^ishida-1992-pd1]: Ishida Y, Agata Y, Shibahara K, Honjo T. Induced expression of PD-1, a novel member of the immunoglobulin gene superfamily, upon programmed cell death. *EMBO J.* 1992;11(11):3887-3895. [doi:10.1002/j.1460-2075.1992.tb05481.x](https://doi.org/10.1002/j.1460-2075.1992.tb05481.x) · [PubMed 1396582](https://pubmed.ncbi.nlm.nih.gov/1396582/)
[^dong-2002-pdl1-tumor]: Dong H, Strome SE, Salomao DR, et al. Tumor-associated B7-H1 promotes T-cell apoptosis: a potential mechanism of immune evasion. *Nat Med.* 2002;8(8):793-800. [doi:10.1038/nm730](https://doi.org/10.1038/nm730) · [PubMed 12091876](https://pubmed.ncbi.nlm.nih.gov/12091876/)
[^topalian-2012-antipd1]: Topalian SL, Hodi FS, Brahmer JR, et al. Safety, activity, and immune correlates of anti-PD-1 antibody in cancer. *N Engl J Med.* 2012;366(26):2443-2454. [doi:10.1056/NEJMoa1200690](https://doi.org/10.1056/NEJMoa1200690) · [PubMed 22658127](https://pubmed.ncbi.nlm.nih.gov/22658127/)

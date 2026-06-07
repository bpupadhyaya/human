---
schema: human-scale-entry/v1
id: men1
name: MEN1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "MEN1 (menin) is a scaffold in the MLL1/MLL2-menin complex that writes H3K4me3 at CDKN1B and Hox loci; LOF → CDK4/6 derepression → neuroendocrine proliferation; germline MEN1 = MEN1 syndrome; somatic MEN1 loss in 70-90% pancreatic NETs; no catalytic activity."
aliases: ["MEN1", "menin", "multiple endocrine neoplasia type 1 gene", "MEN1 tumor suppressor", "menin-MLL complex", "menin scaffold", "MEN1 LOF", "MEN1 mutation", "MEN1 pNET", "KMT2A-menin"]
sources:
  - id: chandrasekharappa-1997-men1
    type: peer-reviewed
    cite: "Chandrasekharappa SC, Guru SC, Manickam P, et al. Positional cloning of the gene for multiple endocrine neoplasia-type 1. Science. 1997;276(5311):404-407."
    doi: "10.1126/science.276.5311.404"
    pmid: "9103196"
    url: "https://doi.org/10.1126/science.276.5311.404"
  - id: huang-2012-menin-mll
    type: peer-reviewed
    cite: "Huang J, Gurung B, Wan B, et al. The same pocket in menin binds both MLL and JUND but has opposite effects on transcription. Nature. 2012;482(7386):542-546."
    doi: "10.1038/nature10806"
    pmid: "22327296"
    url: "https://doi.org/10.1038/nature10806"
cross_links:
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Menin maintains H3K4me3 at CDKN1B (p27) and CDKN2C (p18) loci to suppress CDK4/CDK6 activity; MEN1 LOF depletes H3K4me3 → p27/p18 loss → CDK4/6 activation → G1 escape in neuroendocrine cells; CDKN2A (p16) independently suppresses CDK4/6."
  - target: 01-human/03-molecular/sstr2
    relation: connects-to
    note: "Somatostatin receptor 2 (SSTR2) is the primary target of octreotide/lanreotide in MEN1-associated NETs; Ga-68 DOTATATE PET exploits SSTR2 overexpression for functional imaging; SSA therapy suppresses hormonal hypersecretion and has anti-proliferative effects."
  - target: 01-human/07-system/neuroendocrine-tumors
    relation: connects-to
    note: "MEN1 LOF is the most common somatic driver of sporadic pancreatic NETs (70-90%); MEN1-associated NETs often arise at younger age, are multifocal, and may be G1/G2 grade; menin loss disrupts H3K4me3 and cell cycle control in neuroendocrine lineage cells."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "Pancreatic NETs differ from pancreatic ductal adenocarcinoma (PDAC) in driver genes (MEN1/DAXX/ATRX vs KRAS/CDKN2A/SMAD4/TP53), prognosis, and treatment; MEN1-loss NETs are better differentiated with slower progression than PDAC."
---

# MEN1

## Overview

**MEN1** encodes menin, a 610 amino acid (68 kDa) nuclear scaffold protein with no intrinsic enzymatic activity. Menin is the product of the MEN1 tumor suppressor gene at chromosome **11q13** and functions as a molecular bridge within the **MLL1 (KMT2A)/MLL2 (KMT2B) histone H3K4 methyltransferase complex**, positioning the SET domain over target gene promoters to deposit the active H3K4me3 mark. Germline MEN1 pathogenic variants cause **Multiple Endocrine Neoplasia type 1 (MEN1 syndrome)**, an autosomal dominant hereditary cancer syndrome featuring parathyroid adenomas, pituitary adenomas, and pancreatic neuroendocrine tumors (pNETs). Somatic biallelic MEN1 inactivation is the most frequent driver event in sporadic pNETs (~70-90%) [^chandrasekharappa-1997-men1] [^huang-2012-menin-mll].

**MEN1 somatic alteration frequency across tumor types:**

| Tumor type | MEN1 mutation frequency | Notes |
|---|---|---|
| Pancreatic NET (pNET) | ~70-90% | Most common pNET driver; with DAXX/ATRX |
| Lung carcinoid/NET | ~25-35% | Typical carcinoid; co-occurs with DAXX |
| Parathyroid adenoma (sporadic) | ~20-35% | LOH at 11q13 in sporadic HPT |
| MEN1 syndrome tumors | ~100% (germline + somatic) | Two-hit model; LOH on second allele |
| Uterine leiomyoma | <5% somatic | Occasional MEN1 LOF |

## Structure

Menin is a 610 aa protein with three **winged-helix-turn-helix (wHTH)** domains at the N-terminus and two **nuclear localization signals (NLS)** at the C-terminus. The protein functions as a scaffold with multiple interacting surfaces and no catalytic domain.

**Key structural domains:**

- **N-terminal MLL-binding pocket (aa 1-40, 40-120)**: engages the FXPP motif of MLL1 (KMT2A) and MLL2 (KMT2B); the same pocket binds JunD with competing affinity; crystal structure solved at 2.7 Å (Huang 2012, Nature) reveals deep hydrophobic groove
- **wHTH domains (aa 200-480)**: three winged-helix-turn-helix repeats form the central body; interface for RBBP5 and ASH2L sub-complex of the MLL complex
- **LEDGF-binding domain (~aa 166-200)**: interacts with LEDGF/p75 (PC4-and-SFRS1-interacting protein); links menin to chromatin via LEDGF H3K36me2 reader domain
- **NLS-1 (aa 479-497) and NLS-2 (aa 588-608)**: bipartite nuclear localization; pathogenic missense variants disrupting NLS → cytoplasmic menin → functional loss
- **No enzymatic domain**: menin has no SET domain, no HAT, no kinase, no phosphatase activity — pure scaffold

**Menin-MLL1/MLL2 complex:**
The full active complex includes menin + MLL1/MLL2 SET domain + WRAD sub-complex (WDR5, RBBP5, ASH2L, DPY30):

```
Chromatin H3K4me0/me1
    ↓ (WDR5+CFP1 recognition)
Menin bridges MLL1 to chromatin
    ↓
MLL1 SET domain transfers CH3 from SAM → H3K4me3
    ↓
H3K4me3 recruits TAF3, TFIID → transcription initiation
```

## Function

Menin maintains H3K4me3 at a defined set of gene promoters that control cell cycle entry and differentiation in neuroendocrine lineages:

**Cell cycle targets:**
- **CDKN1B (p27/KIP1)**: menin positions H3K4me3 at CDKN1B promoter → p27 expression → CDK2 inhibition → G1 arrest; MEN1 LOF → p27 loss → CDK2 activation → S-phase entry
- **CDKN2C (p18/INK4C)**: menin maintains H3K4me3 at CDKN2C → p18 → CDK4/CDK6 inhibition; MEN1 LOF → p18 loss → cyclin D1-CDK4/6 activity → Rb phosphorylation → E2F release → proliferation
- **Insulin gene**: menin represses insulin expression in islet β-cells via recruitment of MLL complex to a non-H3K4me3 repressive context (context-dependent role distinct from activation function)

**Developmental targets:**
- **HOXA9/HOXA10 (Hox cluster)**: menin-MLL1 maintains Hox gene expression in hematopoietic progenitors; this function is hijacked in KMT2A-rearranged AML (see Mechanism)
- **GAS2**: menin activates GAS2 which blocks calpain-mediated cyclin D1 degradation

**JunD suppression:**
Menin binds JunD (AP-1 transcription factor) via the same N-terminal pocket used by MLL — but has the opposite effect: menin-JunD interaction suppresses JunD-mediated transcription of oncogenes (cyclin D1, c-Myc). MEN1 LOF releases JunD → AP-1 target gene upregulation → proliferation. This dual-pocket property (MLL activation / JunD repression using the same binding site) is the structural basis for menin's tumor suppressor function [^huang-2012-menin-mll].

## Mechanism

### Two-hit tumor suppressor model

MEN1 follows Knudson's two-hit model:
1. **Germline first hit**: heterozygous pathogenic MEN1 variant (missense, frameshift, splice, deletion) inherited from carrier parent or de novo
2. **Somatic second hit**: LOH at 11q13 in tumor cells (most common: large deletion encompassing MEN1 locus); verified by allele-specific PCR or SNP array; confirms biallelic inactivation
3. **Net effect**: complete menin loss → H3K4me3 depletion at CDKN1B/CDKN2C → CDK4/6-driven proliferation → neuroendocrine tumorigenesis

### Menin inhibitors in KMT2A-rearranged AML

In KMT2A (MLL1)-rearranged AML, the fusion protein (KMT2A-MLLT3/AF9, KMT2A-MLLT1/ENL) retains the FXPP menin-binding motif → permanently tethers menin-MLL1 to HOXA9/HOXA10 and MEIS1 → Hox gene overexpression → leukemia stem cell maintenance.

**Menin inhibitors**: revumenib (SNDX-5613), ziftomenib (KO-539) — small molecules that occupy the N-terminal menin pocket → displace MLL1 fusion → Hox gene downregulation → differentiation of leukemic blasts. These are NOT applicable to MEN1-deficient NETs (protein already absent). Revumenib FDA approval expected/received for KMT2A-r AML.

### Somatic MEN1 in pancreatic NETs

Sporadic pNETs have two major epigenetic subtypes defined by somatic mutation pattern:
- **MEN1 + DAXX/ATRX mutant (70-90%)**: menin loss + DAXX (death domain-associated protein) or ATRX loss → ALT (alternative lengthening of telomeres); better prognosis; oligometastatic
- **MEN1 + DAXX/ATRX wildtype**: rare; different epigenome
- **Ki-67 < 3%, G1**: majority of MEN1-LOF pNETs; G2 (Ki-67 3-20%) in minority; G3 (>20%) rare

### Therapeutic implications for MEN1-deficient NETs

- **CDK4/6 inhibitors**: rational given p18/p27 loss → CDK4/6 activation; palbociclib + everolimus under investigation in pNETs; no Phase 3 data yet
- **mTOR inhibitors**: everolimus (RADIANT-3 Phase 3): pNET PFS HR 0.35 (11.0 vs 4.6 months); FDA-approved for progressive, well-differentiated pNETs regardless of MEN1 status; mTOR pathway activated downstream of CDK4/6 and AKT in pNETs
- **Somatostatin analogs**: octreotide LAR/lanreotide autogel; CLARINET trial: lanreotide PFS HR 0.47 vs placebo in G1/G2 gastroenteropancreatic NETs
- **PRRT (¹⁷⁷Lu-DOTATATE)**: NETTER-1 Phase 3: PFS HR 0.18 in midgut NETs; SSTR2 positivity required; applicable to MEN1-associated NETs with SSTR2 expression

## Connections

- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — Menin maintains H3K4me3 at CDKN1B (p27) and CDKN2C (p18) loci to suppress CDK4/CDK6 activity; MEN1 LOF depletes H3K4me3 → p27/p18 loss → CDK4/6 activation → G1 escape in neuroendocrine cells; CDKN2A (p16) independently suppresses CDK4/6.
- `connects-to` → **[SSTR2](../../03-molecular/sstr2/README.md)** — Somatostatin receptor 2 (SSTR2) is the primary target of octreotide/lanreotide in MEN1-associated NETs; Ga-68 DOTATATE PET exploits SSTR2 overexpression for functional imaging; SSA therapy suppresses hormonal hypersecretion and has anti-proliferative effects.
- `connects-to` → **[Neuroendocrine Tumors](../../07-system/neuroendocrine-tumors/README.md)** — MEN1 LOF is the most common somatic driver of sporadic pancreatic NETs (70-90%); MEN1-associated NETs often arise at younger age, are multifocal, and may be G1/G2 grade; menin loss disrupts H3K4me3 and cell cycle control in neuroendocrine lineage cells.
- `connects-to` → **[Pancreatic Cancer](../../07-system/pancreatic-cancer/README.md)** — Pancreatic NETs differ from pancreatic ductal adenocarcinoma (PDAC) in driver genes (MEN1/DAXX/ATRX vs KRAS/CDKN2A/SMAD4/TP53), prognosis, and treatment; MEN1-loss NETs are better differentiated with slower progression than PDAC.

[^chandrasekharappa-1997-men1]: Chandrasekharappa SC, Guru SC, Manickam P, et al. Positional cloning of the gene for multiple endocrine neoplasia-type 1. *Science.* 1997;276(5311):404-407. [doi:10.1126/science.276.5311.404](https://doi.org/10.1126/science.276.5311.404) · [PubMed 9103196](https://pubmed.ncbi.nlm.nih.gov/9103196/)
[^huang-2012-menin-mll]: Huang J, Gurung B, Wan B, et al. The same pocket in menin binds both MLL and JUND but has opposite effects on transcription. *Nature.* 2012;482(7386):542-546. [doi:10.1038/nature10806](https://doi.org/10.1038/nature10806) · [PubMed 22327296](https://pubmed.ncbi.nlm.nih.gov/22327296/)

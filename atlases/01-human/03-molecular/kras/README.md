---
schema: human-scale-entry/v1
id: kras
name: KRAS
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Small GTPase and proto-oncogene; mutated in ~25% of all human cancers (PDAC ~90%, CRC ~45%, NSCLC ~30%). Oncogenic mutations (G12D, G12V, G12C) lock KRAS in GTP-bound active state, constitutively activating RAF-MEK-ERK and PI3K-Akt-mTOR. KRAS G12C now targetable by sotorasib."
aliases: ["KRAS4A", "KRAS4B", "Kirsten RAS", "RAS GTPase", "v-Ki-ras2"]
sources:
  - id: prior-2012-ras
    type: peer-reviewed
    cite: "Prior IA, Lewis PD, Mattos C. A comprehensive survey of Ras mutations in cancer. Cancer Res. 2012;72(10):2457-2467."
    doi: "10.1158/0008-5472.CAN-11-2612"
    pmid: "22589270"
    url: "https://doi.org/10.1158/0008-5472.CAN-11-2612"
  - id: hallin-2020-sotorasib
    type: peer-reviewed
    cite: "Hallin J, Engstrom LD, Hargis L, et al. The KRASG12C Inhibitor MRTX849 Provides Insight toward Therapeutic Susceptibility of KRAS-Mutant Cancers in Mouse Models and Patients. Cancer Discov. 2020;10(1):54-71."
    doi: "10.1158/2159-8290.CD-19-1167"
    pmid: "31658955"
    url: "https://doi.org/10.1158/2159-8290.CD-19-1167"
  - id: hong-2020-codebreak100
    type: peer-reviewed
    cite: "Hong DS, Fakih MG, Strickler JH, et al. KRASG12C Inhibition with Sotorasib in Advanced Solid Tumors. N Engl J Med. 2020;383(13):1207-1217."
    doi: "10.1056/NEJMoa1917239"
    pmid: "32955176"
    url: "https://doi.org/10.1056/NEJMoa1917239"
cross_links:
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Oncogenic KRAS activates NF-κB through RAF→MEK→ERK and RalGDS→Ral→NF-κB pathways; NF-κB-driven inflammation creates an immunosuppressive tumor microenvironment that sustains KRAS-mutant PDAC and CRC growth."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "KRAS activates PI3K (via p110α direct interaction with Ras-GTP) → Akt → mTORC1 → anabolism and autophagy suppression; this KRAS→PI3K→mTOR axis drives tumor cell growth and contributes to resistance to single-agent KRAS inhibition."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β and KRAS signaling cooperate in PDAC: TGF-β initially suppresses early-stage cells (anti-proliferative) but in KRAS-mutant context TGF-β drives EMT, stromal desmoplasia, and immune exclusion — making KRAS-mutant tumors highly resistant to checkpoint immunotherapy."
---

# KRAS

## Overview

**KRAS** (Kirsten rat sarcoma viral proto-oncogene) is the most frequently mutated oncogene in human cancer — mutated in approximately **25% of all tumors** and dominant in several of the deadliest cancers: **pancreatic ductal adenocarcinoma (PDAC, ~90%)**, colorectal carcinoma (CRC, ~45%), and non-small cell lung carcinoma (NSCLC, ~30%) [^prior-2012-ras].

KRAS belongs to the **RAS superfamily** of small GTPases — molecular switches that cycle between an **inactive GDP-bound state** and an **active GTP-bound state**. Under physiological conditions, growth factor receptor stimulation → guanine nucleotide exchange factors (GEFs, e.g., SOS1) → GDP→GTP exchange → KRAS activation → downstream effector signaling → intrinsic GTPase activity (accelerated by GAPs: RasGAP, NF1/neurofibromin) → GTP hydrolysis → inactivation. This cycle takes seconds to minutes.

**Oncogenic mutations** at codons **G12, G13, and Q61** impair GTPase activity (both intrinsic and GAP-stimulated) → KRAS locked in GTP-bound active state → constitutive signaling → uncontrolled cell proliferation. For 40+ years, KRAS was considered "undruggable" due to the lack of a suitable small molecule binding pocket. The discovery of a cysteine-accessible switch-II pocket (S-IIP) in KRAS G12C (cysteine substitution) enabled **covalent inhibitor development**, culminating in FDA approval of **sotorasib** (AMG 510) in 2021 and **adagrasib** in 2022 — the first direct KRAS inhibitors [^hong-2020-codebreak100].

## Structure

### KRAS protein

KRAS is a 189-amino acid (21 kDa) GTPase. Two alternatively spliced isoforms exist: **KRAS4A** (relatively rare) and **KRAS4B** (dominant; almost all cancer studies reference 4B).

**Key structural features:**
- **P-loop (G1 box, aa 10-17):** Phosphate binding; GxxxxGKS/T motif; contact point for GDP/GTP phosphates
- **Switch I (aa 30-38):** Changes conformation upon GTP binding; Thr35 coordinates Mg²⁺ and γ-phosphate; GEF/GAP interaction site; effector binding surface
- **Switch II (aa 57-75):** Includes Gly60, Gly12, Gln61; undergoes dramatic conformational change; Gln61 is the catalytic residue for GTP hydrolysis (assisted by GAP-Arg-finger)
- **α3-helix and α5-helix:** Membrane association; KRAS4B contains a polybasic stretch (KEKMSK) and C-terminal CAAX motif (Cys185) → farnesylation → membrane targeting

**The G12C pocket (S-IIP):** In KRAS G12C, the cysteine at position 12 is near a cryptic pocket (switch-II pocket, S-IIP) accessible in the GDP-bound (inactive) conformation. **Covalent inhibitors** (sotorasib, adagrasib) form a Michael addition with Cys12 → lock KRAS G12C in GDP-bound state → permanent inactivation (cannot exchange GDP for GTP).

### Cancer mutation landscape [^prior-2012-ras]

| Mutation | Prevalence | Predominant tumor type |
|:---|:---|:---|
| G12D | ~36% of KRAS mut | PDAC (most common), CRC |
| G12V | ~22% of KRAS mut | PDAC, CRC, NSCLC |
| G12C | ~14% of KRAS mut | NSCLC (most common single KRAS mutation in lung), CRC |
| G13D | ~8% of KRAS mut | CRC (particularly enriched) |
| G12R | ~6% of KRAS mut | PDAC |
| Q61H/L/K | ~5% | Various |

KRAS G12D and G12V are the most biochemically recalcitrant to direct inhibition (no accessible cysteine); G12C is uniquely drugable due to the cysteine electrophile.

## Function

### Downstream effector pathways

KRAS-GTP activates three major effector branches simultaneously:

**1. RAF-MEK-ERK (MAPK) pathway:**
KRAS-GTP → RAF1/BRAF dimerization → MEK1/2 (MAP2K1/2) phosphorylation → ERK1/2 (MAPK3/1) activation → nuclear translocation → transcription factors (ELK1, MYC, FOS/JUN) → cell proliferation, survival, migration

**2. PI3K-Akt-mTOR pathway:**
KRAS-GTP → p110α (PIK3CA) direct binding → PI3K lipid kinase activation → PIP3 → Akt (PKB) phosphorylation → mTORC1 → protein synthesis, metabolic reprogramming, anti-apoptosis

**3. RAL-RALGEF pathway:**
KRAS-GTP → RalGDS/RGL/RGL2 → RalA/B (GTPases) → RalBP1 → exocyst complex regulation → vesicle trafficking, cell migration; also activates NF-κB → inflammatory gene expression in tumor stroma

**Effector bias by mutation:** G12D preferentially activates PI3K over RAF; G12V shows relatively balanced RAF/PI3K activation; Q61 mutations impair intrinsic GTPase more severely than G12/G13 mutations — differences with therapeutic implications.

### Role in tumor biology

**Metabolic reprogramming:** Oncogenic KRAS drives macropinocytosis (non-selective uptake of extracellular fluid → amino acid supply), autophagy (recycling for amino acids), and Warburg-type glycolysis via LDHA induction. KRAS-mutant PDAC cells rely heavily on macropinocytosis and autophagy for survival in nutrient-poor tumor microenvironments.

**Immune evasion:** KRAS promotes an immunosuppressive tumor microenvironment via:
- IL-8 (CXCL8), GM-CSF secretion → MDSC recruitment
- Reduced MHC-I expression (via MEK-ERK → NLRC5 suppression) → reduced T cell recognition
- PD-L1 upregulation via MEK-ERK
Result: KRAS-mutant cancers are notoriously resistant to checkpoint immunotherapy (especially PDAC).

**Synthetic lethality screens:** KRAS-mutant cells show dependencies on SHP2, SOS1, EGFR (co-receptor for SOS1-mediated feedback), and autophagy pathways — basis for combination therapy strategies.

## Mechanism

### The KRAS G12C inhibitor story [^hallin-2020-sotorasib]

The "undruggable" era ended when Wellspring Biosciences/Araxes Pharma/Amgen teams discovered that:
1. KRAS G12C uniquely has a nucleophilic Cys12 (only ~1% of KRAS mutations are G12C in PDAC, but ~13% in NSCLC — larger patient population)
2. A cryptic hydrophobic pocket (S-IIP) forms transiently in KRAS GDP-bound conformation
3. **Covalent irreversible inhibitors** can reach Cys12 and form a permanent adduct

**Sotorasib (AMG 510, Lumakras):** First FDA-approved KRAS G12C inhibitor (May 2021, NSCLC); CodeBreaK 100 Phase I/II trial: ORR 37.1% in NSCLC; PFS 6.8 months; approved second-line for KRAS G12C NSCLC. CodeBreaK 200 (Phase III vs docetaxel): superior PFS.

**Adagrasib (MRTX849, Krazati):** Second FDA-approved KRAS G12C inhibitor (December 2022); KRYSTAL-1 trial: ORR 42.9% (NSCLC), 45.3% (CRC as combination with cetuximab); also shows CNS activity (crosses BBB better than sotorasib); approved for NSCLC and CRC.

**Resistance mechanisms to G12C inhibitors:**
- Secondary KRAS mutations (Y96D, H95R) that impair inhibitor binding
- Amplification of KRAS G12C
- Bypass pathway activation: MET amplification, NRAS/BRAF mutations
- RAC1 mutations
- Adaptive feedback: RTK upregulation → SOS1 → reloading of KRAS with GTP

**Combination strategies:**
- KRAS G12C inhibitor + SHP2 inhibitor (blocks feedback activation): SHP2 (PTPN11) is a phosphatase promoting SOS1-mediated nucleotide exchange; blockade prevents adaptive resistance
- KRAS G12C inhibitor + MEK inhibitor: addresses ERK rebound
- KRAS G12C inhibitor + cetuximab (anti-EGFR): EGFR drives feedback in CRC; KRYSTAL-1 CRC combination arm shows ORR 45.3%

**KRAS G12D/G12V inhibitors (next generation):**
- MRTX1133 (adagrasib analog): high selectivity for KRAS G12D; Phase I in progress (2024)
- RAS(ON) inhibitors: covalent inhibitors targeting the active (GTP-bound) state
- RAS multi-selectivenon-covalent inhibitors (BI 1701963): bind GDP state, suitable for all G12 mutations

## Connections

- `connects-to` → **[NF-κB](../nf-kb/README.md)** — oncogenic KRAS activates NF-κB through RAF→MEK→ERK and RalGDS effector branches; NF-κB drives inflammatory cytokines (IL-6, IL-8) that sustain the immunosuppressive KRAS-mutant tumor microenvironment.
- `connects-to` → **[mTOR](../mtor/README.md)** — KRAS activates PI3K via direct p110α interaction, leading to Akt→mTOR activation; mTOR-driven anabolism is essential for KRAS-mutant tumor growth; combined KRAS+PI3K inhibition is a key resistance strategy.
- `connects-to` → **[TGF-β](../tgf-beta/README.md)** — TGF-β and KRAS signaling cooperate in PDAC to drive stromal desmoplasia, EMT, and immune exclusion; combined KRAS activation + SMAD4 loss (co-occurring in ~55% of PDAC) creates aggressive disease biology.

[^prior-2012-ras]: Prior IA, Lewis PD, Mattos C. A comprehensive survey of Ras mutations in cancer. *Cancer Res.* 2012;72(10):2457-2467. [doi:10.1158/0008-5472.CAN-11-2612](https://doi.org/10.1158/0008-5472.CAN-11-2612) · [PubMed 22589270](https://pubmed.ncbi.nlm.nih.gov/22589270/)
[^hallin-2020-sotorasib]: Hallin J, Engstrom LD, Hargis L, et al. The KRASG12C Inhibitor MRTX849 Provides Insight toward Therapeutic Susceptibility. *Cancer Discov.* 2020;10(1):54-71. [doi:10.1158/2159-8290.CD-19-1167](https://doi.org/10.1158/2159-8290.CD-19-1167) · [PubMed 31658955](https://pubmed.ncbi.nlm.nih.gov/31658955/)
[^hong-2020-codebreak100]: Hong DS, Fakih MG, Strickler JH, et al. KRASG12C Inhibition with Sotorasib in Advanced Solid Tumors. *N Engl J Med.* 2020;383(13):1207-1217. [doi:10.1056/NEJMoa1917239](https://doi.org/10.1056/NEJMoa1917239) · [PubMed 32955176](https://pubmed.ncbi.nlm.nih.gov/32955176/)

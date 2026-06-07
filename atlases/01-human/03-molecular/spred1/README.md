---
schema: human-scale-entry/v1
id: spred1
name: SPRED1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "SPRED1 (Sprouty-related EVH1 domain) recruits NF1/neurofibromin to the plasma membrane and inhibits BRAF/CRAF to suppress RAS-MAPK; LOF → RAS-MAPK dysregulation; germline SPRED1 = Legius syndrome (café-au-lait macules without neurofibromas or cancer predisposition)."
aliases: ["SPRED1", "Sprouty-related EVH1", "SPRED1 Legius syndrome", "SPRED1 RAS MAPK", "SPRED1 NF1 pathway", "SPRED1 RAF inhibitor", "Legius SPRED1", "sprouty SPRED1 BRAF"]
sources:
  - id: brems-2007-spred1
    type: peer-reviewed
    cite: "Brems H, Chmara M, Sahbatou M, et al. Germline loss-of-function mutations in SPRED1 cause a neurofibromatosis 1-like phenotype. Nat Genet. 2007;39(9):1120-1126."
    doi: "10.1038/ng2111"
    pmid: "17704774"
    url: "https://doi.org/10.1038/ng2111"
  - id: tidyman-2009-rasopathy
    type: peer-reviewed
    cite: "Tidyman WE, Rauen KA. The RASopathies: developmental syndromes of Ras/MAPK pathway dysregulation. Curr Opin Genet Dev. 2009;19(3):230-236."
    doi: "10.1016/j.gde.2009.04.001"
    pmid: "19467855"
    url: "https://doi.org/10.1016/j.gde.2009.04.001"
cross_links:
  - target: 01-human/03-molecular/nf1
    relation: connects-to
    note: "SPRED1 recruits NF1/neurofibromin to the plasma membrane as a ternary RAS-SPRED1-NF1 complex to accelerate RAS-GTP→GDP hydrolysis; SPRED1 LOF → impaired NF1 membrane targeting → RAS-MAPK activation; germline SPRED1 = Legius syndrome (NF1-like, no tumors)."
  - target: 01-human/03-molecular/braf
    relation: connects-to
    note: "SPRED1 EVH1 domain also directly inhibits BRAF and CRAF kinase activity independently of NF1 recruitment; SPRED1-mediated BRAF inhibition is additive with NF1-mediated RAS inactivation; BRAF V600E melanoma and other BRAF-mutant tumors may have reduced SPRED1 expression."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "SPRED1 suppresses RAS-MAPK signaling downstream of KRAS/HRAS/NRAS via EVH1-BRAF inhibition and NF1-dependent RAS-GTP hydrolysis; KRAS G12C/G12D tumors evade SPRED1/NF1 suppression because oncogenic KRAS resists GAP-mediated hydrolysis."
  - target: 01-human/07-system/neurofibromatosis-type-1
    relation: connects-to
    note: "Germline SPRED1 causes Legius syndrome (café-au-lait macules + axillary freckling) without neurofibromas or cancer predisposition; clinically mimics mild NF1; molecular testing distinguishes both; SPRED1 and NF1 both restrain RAS-MAPK at the plasma membrane."
---

# SPRED1

## Overview

**SPRED1** (Sprouty-Related EVH1 Domain Protein 1) is a member of the **Sprouty-related (SPRED)** protein family (SPRED1, SPRED2, SPRED3) that functions as a negative regulator of the **RAS-MAPK signaling pathway**. SPRED1 was identified as the gene responsible for **Legius syndrome** (NF1-like syndrome) by Brems et al. in 2007, establishing SPRED1 as a human disease gene in the **RASopathy** spectrum of germline RAS pathway dysregulation disorders. SPRED1 operates through two complementary mechanisms: (1) recruiting **NF1/neurofibromin** to the plasma membrane to accelerate RAS-GTP hydrolysis, and (2) directly inhibiting **BRAF and CRAF** kinase activity via its EVH1 domain. Loss of SPRED1 impairs both mechanisms, dysregulating MAPK signaling in cells expressing active RAS [^brems-2007-spred1] [^tidyman-2009-rasopathy].

**RASopathy spectrum (germline RAS-MAPK pathway disorders):**

| Syndrome | Gene(s) | Pathway node | Key features |
|---|---|---|---|
| NF1 | NF1 | RAS-GAP | Neurofibromas, café-au-lait, MPNST, optic glioma |
| Legius | SPRED1 | RAS-MAPK inhibitor | Café-au-lait, freckling; no neurofibromas or cancer |
| Noonan | SOS1, RAF1, PTPN11, others | RAS-MAPK activators | Pulmonary stenosis, short stature, cardiac defects |
| CFC | BRAF, MEK1/2 | MAPK cascade | Cardio-facio-cutaneous features, severe ID |
| Costello | HRAS | HRAS GOF | Papillomata, cardiomyopathy, HRAS G12S most common |
| LEOPARD | PTPN11 (GOF), RAF1, BRAF | Multiple nodes | Lentigines, cardiac defects, deafness |

## Structure

### SPRED1 protein domains

**EVH1 domain (Enabled/VASP Homology 1; aa 1-110):**
- N-terminal; structurally homologous to the Enabled/VASP actin-regulatory protein EVH1 domain
- Does not bind canonical EVH1 ligands (PPxxF proline-rich peptides); instead has two specialized functions:
  1. **NF1 recruitment**: EVH1 binds neurofibromin (NF1) GRD domain-flanking region → brings NF1 to the plasma membrane where it has access to RAS-GTP → RAS-GAP acceleration
  2. **BRAF/CRAF inhibition**: EVH1 binds BRAF kinase domain directly → allosteric inhibition of BRAF/CRAF kinase activity; this inhibition is independent of NF1 or RAS
- EVH1 pathogenic variants in Legius syndrome: truncating variants (frameshift/nonsense) most common; rare missense variants at conserved positions (Asn52, Asp72) are functional null

**SPR domain (Sprouty-related; aa 111-180):**
- Central domain; mediates SPRED1 homo- and heterodimerization with SPRED2/SPRED3
- SPRED1-SPRED2 heterodimers have distinct functional properties vs homodimers; SPRED2 has overlapping but distinct expression pattern

**c-Kit binding domain (KBD) / C-terminal domain (aa 181-444):**
- Binds the cytoplasmic tail of activated receptor tyrosine kinases (c-Kit, PDGFR, VEGFR2) and adaptor proteins → SPRED1 membrane localization after RTK activation
- Also contains a PHOX homology domain-like (PX) region for membrane phosphoinositide binding
- SPRED1 membrane localization (via KBD + RTK binding + RAS interaction) is required for its function: SPRED1 must be at the plasma membrane where active RAS resides

**RAS-interaction mechanism:**
SPRED1 contains a putative RAS-interacting element that may directly contact RAS-GTP, though the primary mechanism is indirect: SPRED1 EVH1 → NF1 GRD → NF1 GAP accelerates RAS-GTP hydrolysis by 1000-fold → RAS becomes GDP-bound (inactive). This model (SPRED1 as a NF1 membrane-targeting scaffold) was validated by Stowe et al. 2012 (Nature Struct Mol Biol).

## Function

### SPRED1 as a RAS-MAPK pathway brake

**In receptor-activated cells (normal):**
1. Growth factor → RTK (EGFR, VEGFR2, c-Kit) → RAS exchange factors (GRBs2-SOS1) → RAS-GTP
2. RAS-GTP → RAF (BRAF/CRAF) → MEK1/2 → ERK1/2 → gene expression
3. **SPRED1 feedback inhibition**: SPRED1 recruited to plasma membrane (via KBD + RTK) → EVH1 recruits NF1 to active RAS → NF1 GAP → RAS-GDP; AND EVH1 directly inhibits BRAF → MEK not activated → ERK dampened
4. Net result: MAPK signal is transient and self-limited

**With SPRED1 LOF:**
- NF1 cannot be efficiently membrane-targeted → RAS-GTP persists longer
- BRAF/CRAF not inhibited by EVH1 → MEK/ERK more active
- Net: sustained low-level MAPK hyperactivation; not as severe as oncogenic KRAS mutation, but enough to cause developmental and cancer predisposition phenotypes when NF1 is also haploinsufficient

### SPRED1 in development

SPRED1 is broadly expressed during embryogenesis. In Spred1 knockout mice:
- Skeletal defects (face, limb)
- Abnormal cardiac development
- Hematopoietic abnormalities (myeloid bias)
- Enhanced ERK activation in multiple tissues after growth factor stimulation

Human Legius syndrome phenotype (germline SPRED1 LOF) is milder than NF1 syndrome, reflecting the incomplete redundancy between SPRED1-NF1 (Legius) and NF1 alone mechanisms.

### SPRED1 in cancer

SPRED1 is not a classical tumor suppressor (biallelic somatic inactivation is rare), but:
- **Somatic SPRED1 LOF** identified in ~3-5% of melanoma, NSCLC, and CRC (enriched in RAS-MAPK pathway-altered tumors)
- **NF1/SPRED1 co-deletion**: in some melanomas and gliomas with NF1 deletion, co-deletion of adjacent SPRED1 (13q) amplifies RAS-MAPK hyperactivation
- **Legius syndrome and cancer**: unlike NF1 syndrome, Legius syndrome (germline SPRED1) does NOT carry elevated cancer risk; animal models and human data suggest SPRED1 haploinsufficiency alone is insufficient for tumor initiation without a second event (complete LOH not observed in Legius patients)
- **MAPK inhibitor resistance**: somatic SPRED1 deletion as a mechanism of acquired BRAF/MEK inhibitor resistance in BRAF-mutant melanoma (loss of feedback inhibition → paradoxical ERK reactivation)

## Mechanism

### Legius syndrome clinical features

Legius syndrome (germline SPRED1 LOF) presents with NF1-like skin findings but lacks the tumor-forming and other systemic features:

**Present (shared with NF1):**
- ≥6 café-au-lait macules (≥5 mm pre-pubertal, ≥15 mm post-pubertal)
- Axillary and/or inguinal freckling (Crowe's sign — also present in NF1)
- Macrocephaly in some patients

**Absent (distinguishes from NF1):**
- Cutaneous neurofibromas (absent — most important distinguishing feature)
- Lisch nodules (absent)
- Plexiform neurofibromas (absent)
- Optic pathway glioma (absent)
- MPNST risk (not elevated above population)
- Bone abnormalities (absent: no sphenoid wing dysplasia, no pseudarthrosis)
- Learning disabilities: mild in some Legius patients (not as prevalent as NF1)

**Diagnostic approach:**
In a child with café-au-lait macules but no neurofibromas:
1. Clinical evaluation for NF1 diagnostic criteria (NIH 1988 or 2021 revised): may not yet meet criteria in young children (≥2 criteria required)
2. Slit-lamp exam (Lisch nodules absent in Legius)
3. Molecular testing: multigene panel including NF1 + SPRED1; distinguishes NF1 from Legius
4. Genetic counseling: Legius has 50% inheritance risk but excellent prognosis; NF1 has significant morbidity

## Connections

- `connects-to` → **[NF1](../../03-molecular/nf1/README.md)** — SPRED1 recruits NF1/neurofibromin to the plasma membrane as a ternary RAS-SPRED1-NF1 complex to accelerate RAS-GTP→GDP hydrolysis; SPRED1 LOF → impaired NF1 membrane targeting → RAS-MAPK activation; germline SPRED1 = Legius syndrome (NF1-like, no tumors).
- `connects-to` → **[BRAF](../../03-molecular/braf/README.md)** — SPRED1 EVH1 domain also directly inhibits BRAF and CRAF kinase activity independently of NF1 recruitment; SPRED1-mediated BRAF inhibition is additive with NF1-mediated RAS inactivation; BRAF V600E melanoma and other BRAF-mutant tumors may have reduced SPRED1 expression.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — SPRED1 suppresses RAS-MAPK signaling downstream of KRAS/HRAS/NRAS via EVH1-BRAF inhibition and NF1-dependent RAS-GTP hydrolysis; KRAS G12C/G12D tumors evade SPRED1/NF1 suppression because oncogenic KRAS resists GAP-mediated hydrolysis.
- `connects-to` → **[Neurofibromatosis Type 1](../../07-system/neurofibromatosis-type-1/README.md)** — Germline SPRED1 causes Legius syndrome (café-au-lait macules + axillary freckling) without neurofibromas or cancer predisposition; clinically mimics mild NF1; molecular testing distinguishes both; SPRED1 and NF1 both restrain RAS-MAPK at the plasma membrane.

[^brems-2007-spred1]: Brems H, Chmara M, Sahbatou M, et al. Germline loss-of-function mutations in SPRED1 cause a neurofibromatosis 1-like phenotype. *Nat Genet.* 2007;39(9):1120-1126. [doi:10.1038/ng2111](https://doi.org/10.1038/ng2111) · [PubMed 17704774](https://pubmed.ncbi.nlm.nih.gov/17704774/)
[^tidyman-2009-rasopathy]: Tidyman WE, Rauen KA. The RASopathies: developmental syndromes of Ras/MAPK pathway dysregulation. *Curr Opin Genet Dev.* 2009;19(3):230-236. [doi:10.1016/j.gde.2009.04.001](https://doi.org/10.1016/j.gde.2009.04.001) · [PubMed 19467855](https://pubmed.ncbi.nlm.nih.gov/19467855/)

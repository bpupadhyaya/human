---
schema: human-scale-entry/v1
id: apc
name: APC
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "APC (adenomatous polyposis coli) scaffolds the β-catenin destruction complex (APC-AXIN-GSK-3β-CK1α); LOF → nuclear β-catenin → Wnt pathway activation; mutated in ~80% of sporadic CRC; germline APC = familial adenomatous polyposis; MCR hotspots at codons 1309 and 1450."
aliases: ["APC", "APC mutation", "APC colorectal", "APC FAP", "adenomatous polyposis coli", "APC truncation", "APC MCR", "APC beta-catenin", "APC Wnt", "APC colon cancer"]
sources:
  - id: kinzler-1991-apc
    type: peer-reviewed
    cite: "Kinzler KW, Nilbert MC, Su LK, et al. Identification of FAP locus genes from chromosome 5q21. Science. 1991;253(5020):661-665."
    doi: "10.1126/science.1651562"
    pmid: "1651562"
    url: "https://doi.org/10.1126/science.1651562"
  - id: fearon-1990-vogelstein
    type: peer-reviewed
    cite: "Fearon ER, Vogelstein B. A genetic model for colorectal tumorigenesis. Cell. 1990;61(5):759-767."
    doi: "10.1016/0092-8674(90)90186-i"
    pmid: "2188735"
    url: "https://doi.org/10.1016/0092-8674(90)90186-i"
cross_links:
  - target: 01-human/03-molecular/ctnnb1
    relation: connects-to
    note: "APC LOF → insufficient destruction complex → β-catenin nuclear accumulation → TCF/LEF → Wnt targets; equivalent to CTNNB1 activating mutation; APC MCR truncations (codons 1250-1450) leave incomplete SAMP repeats → AXIN binding lost → β-catenin not degraded"
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "APC is the gatekeeper of Wnt/β-catenin signaling in intestinal epithelium; APC LOF → constitutive Wnt-ON state → crypt stem cell expansion → adenoma; APC biallelic LOF is the earliest initiating event in sporadic CRC and FAP; complete APC LOF required in each adenoma"
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "APC is mutated in ~80% of sporadic CRC; Fearon-Vogelstein adenoma-carcinoma model: APC LOF → KRAS → SMAD4 → TP53 sequence; APC mutation cluster region (codons 1250-1450) in CRC; FAP: 100% CRC penetrance by 40 without colectomy; cetuximab/bevacizumab active in APC-mutant mCRC"
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Notch and Wnt/APC co-regulate intestinal crypt homeostasis; Notch NICD1 + APC LOF nuclear β-catenin → synergistic stem cell expansion in early CRC; dual Notch+Wnt hyperactivation in APC-mutant adenomas; γ-secretase inhibitors explored in APC-mutant colorectal cancer"
---

# APC

## Overview

**APC** (Adenomatous Polyposis Coli) encodes a 2,843-amino-acid (310 kDa) scaffold protein that serves as the central organizer of the **β-catenin destruction complex** — the critical molecular brake on Wnt/β-catenin signaling in adult epithelial tissues. APC tethers the destruction complex by providing docking sites for both AXIN (via SAMP repeats) and β-catenin (via armadillo-binding 20 aa repeats), enabling CK1α and GSK-3β to sequentially phosphorylate β-catenin at its degron, triggering β-TrCP-mediated proteasomal degradation. Loss of APC function phenocopies constitutive Wnt-ON signaling regardless of ligand — driving crypt stem cell expansion and adenoma formation. APC is the **gatekeeper tumor suppressor of the colorectal epithelium**: mutated in ~80% of sporadic colorectal carcinomas, all colorectal adenomas in FAP patients, and ~50% of colorectal adenomas in the general population. Germline APC pathogenic variants cause **familial adenomatous polyposis (FAP)**, the most penetrant inherited colorectal cancer syndrome [^kinzler-1991-apc] [^fearon-1990-vogelstein].

**APC alterations across tumor types:**

| Tumor type | Frequency | Notes |
|---|---|---|
| Colorectal carcinoma | ~75-80% | Most commonly mutated gene in CRC; gatekeeper |
| Colorectal adenoma | ~50-60% | Present in early adenomas; biallelic LOF precedes KRAS |
| Medulloblastoma (WNT subgroup) | ~50% | APC or CTNNB1 mutations; excellent prognosis |
| Desmoid fibromatosis (FAP-associated) | FAP (20%) | APC codons 1310-2011; mesenteric desmoid |
| Duodenal/ampullary adenoma (FAP) | ~100% | FAP extracolonic; malignancy risk ~5-10% |
| Gastric cancer | ~5-10% | Typically microsatellite stable |
| Hepatoblastoma | ~30% | Pediatric liver tumor; APC or CTNNB1 |

**APC mutation cluster region (MCR) and genotype-phenotype:**

| APC codon region | FAP phenotype | Notes |
|---|---|---|
| <168 (5' end) | Attenuated FAP (AFAP) | <100 polyps, later onset, distal predominance |
| 168-1250 | Classic FAP | 100-1000 polyps; intermediate |
| 1250-1464 (MCR) | Profuse classic FAP | >1000 polyps; earliest CRC |
| 1310-2011 | Desmoid risk | Mesenteric desmoid; especially 1310-1450 |
| >1580 | Attenuated FAP (AFAP) | 3' attenuated; also CHRPE absent |
| Codon 1309 | Most severe | Thousands of polyps; CRC by age 20s without surveillance |

## Structure

### APC protein architecture

**Oligomerization domain (aa 1-60):**
N-terminal coiled-coil; APC forms obligate homodimers (two APC molecules); dimerization required for full APC function as destruction complex scaffold; tumor-derived truncations that eliminate this domain cannot dimerize effectively

**ASPM-SPD-2-Hydin (ASH) domain (aa 1-200):**
Required for centrosome and spindle localization of APC; APC at kinetochores ensures chromosome stability; APC LOF → chromosomal instability (CIN) → aneuploidy; APC is one of the most important CIN-driving mutations in CRC; disruption of the ASH domain contributes to mitotic dysregulation

**Armadillo repeat domain (aa 334-767; Arm repeats 1-7):**
Seven imperfect armadillo repeats; binds B56 subunit of PP2A (protein phosphatase 2A) → regulation of APC phosphorylation and stability; also binds IQGAP1 (involved in cell migration); Arm repeats of APC are distinct from those of β-catenin — they do not directly bind β-catenin

**β-catenin binding repeats (15 aa repeats, aa 1020-1169; 20 aa repeats, aa 1262-2035):**
Multiple copies of 15 aa and 20 aa repeats that directly bind the ARM repeat domain of β-catenin; the 20 aa repeats are the most important — they bind β-catenin and present it to GSK-3β for phosphorylation; repeats 1, 2, 3 (20 aa) in the MCR are essential for β-catenin binding; truncations in the MCR eliminate the critical 20 aa repeats → β-catenin not presented → not phosphorylated → not degraded

**SAMP repeats (aa 1504-2075):**
SAMP (Ser-Ala-Met-Pro) motifs; bind AXIN (scaffolding partner); three SAMP repeats in APC; AXIN bridges APC to GSK-3β and CK1α; truncations eliminating all SAMP repeats → AXIN cannot bind → destruction complex cannot assemble; truncations eliminating only some SAMP repeats → partial destruction complex → hypomorphic β-catenin degradation

**EB1/microtubule-binding domain (aa 2130-2843):**
C-terminal domain; binds EB1 (end-binding protein 1, microtubule plus-end tracking protein); APC-EB1 complex localizes to microtubule plus ends and kinetochores; required for chromosome segregation; mutations in C-terminal domain (AFAP region >1580) affect microtubule function but preserve sufficient 20 aa repeats for partial β-catenin destruction → less severe phenotype; nuclear export signal (NES) at C-terminus: APC shuttles β-catenin from nucleus to cytoplasm for degradation — "β-catenin chaperone" function

### APC mutation patterns

**Mutation types:**
- Truncating mutations (frameshift, nonsense): >95% of APC cancer mutations; almost always produce truncated protein lacking critical β-catenin binding and SAMP repeats; protein detected by IHC in sporadic CRC (absent in FAP germline mutants due to haploinsufficiency)
- In-frame deletions: rare; preserve reading frame but delete functional domains
- Missense: <5%; functional consequences variable; some at ARM repeats affect AXIN binding
- Large deletions: germline only; ~20% of germline FAP mutations are large rearrangements; detected by MLPA

**Biallelic requirement:**
APC is a classic tumor suppressor requiring biallelic LOF:
- FAP (germline first hit): second hit acquired somatically in each adenoma; LOH at 5q21 is the most common second hit (~60%); somatic truncating mutation is the second hit in ~30%
- Sporadic CRC: two somatic hits in the same stem cell; first hit → aberrant crypt focus; second hit → adenoma; KRAS, TP53, SMAD4 are subsequent hits in the sequence

**IHC:**
APC IHC is technically challenging (large protein, variable antibody quality); not routinely used in clinical diagnostics; in research: APC protein loss in FAP adenomas; nuclear β-catenin IHC (anti-β-catenin) is the practical surrogate for APC/Wnt pathway activation in colorectal tumor pathology

## Function

### APC in the β-catenin destruction complex

**Destruction complex assembly:** [^fearon-1990-vogelstein]
In Wnt-OFF state:
- APC dimers recruit AXIN via SAMP repeats → AXIN scaffolds GSK-3β + CK1α
- APC 20 aa repeats bind β-catenin and position it for phosphorylation
- CK1α phosphorylates β-catenin at S45 → GSK-3β sequentially phosphorylates T41 → S37 → S33
- Phosphorylated β-catenin (S33/S37/T41/S45) recognized by β-TrCP E3 ubiquitin ligase → K48-polyubiquitination → 26S proteasome degradation
- Result: cytoplasmic β-catenin levels maintained low; TCF/LEF bound by GROUCHO repressor; target genes off

**APC as β-catenin chaperone:**
APC does not merely scaffold the destruction complex — it also actively removes β-catenin from the nucleus by acting as a nuclear export factor; phosphorylated β-catenin in the nucleus is bound by APC → APC NES exports β-catenin to cytoplasm → cytoplasmic phosphorylation and degradation; APC LOF → β-catenin accumulates in nucleus AND cytoplasm → constitutive Wnt-ON signaling

**Tumor suppressor functions beyond Wnt:**
1. **Chromosomal stability**: APC-EB1 at kinetochores → proper spindle assembly checkpoint; APC LOF → CIN (chromosomal instability) → aneuploidy; CIN in APC-mutant CRC drives clonal evolution
2. **Cell migration and polarity**: APC regulates actin dynamics via IQGAP1 and formin mDia; APC LOF → aberrant cell migration
3. **DNA repair**: APC interacts with MLH1 and MSH3 at the replication fork; APC LOF → minor MMR reduction (not sufficient to cause MSI-H, contrast MLH1/MSH2 LOF)
4. **Microtubule dynamics**: APC-EB1 stabilizes growing microtubule plus ends → epithelial polarity maintenance

### The Fearon-Vogelstein adenoma-carcinoma sequence [^fearon-1990-vogelstein]

**Classic molecular sequence in CRC:**
1. Normal colon epithelium
2. Biallelic APC LOF → aberrant crypt focus (ACF) → early adenoma (Wnt-ON, crypt stem cell expansion)
3. KRAS activating mutation (G12D/V) → late adenoma, increased proliferation
4. SMAD4 and/or TGF-β pathway LOF → adenoma with villous features
5. TP53 mutation (p53 LOF) → carcinoma in situ
6. Additional mutations (PIK3CA, BRAF, etc.) → invasive carcinoma

**Timing and rate-limiting steps:**
ACF to adenoma: ~5-10 years; adenoma to carcinoma: ~10 years average; total transit time: ~15-20 years; this long timeline is the basis for colonoscopic surveillance effectiveness — detecting adenomas allows curative resection before CRC develops; APC LOF is the rate-limiting first step; in FAP, this first step is pre-existing in all cells → thousands of adenomas form simultaneously → CRC by 30-40 years

## Mechanism

### Therapeutic implications of APC mutation

**Direct APC targeting:**
No approved therapy restores APC function; APC is a scaffold protein — not an enzyme — making drug development difficult; read-through drugs for APC nonsense mutations: aminoglycosides (G418, gentamicin) → partial read-through at APC stop codon → truncated APC with partial function; ataluren (PTC124): oral read-through compound; tested in FAP (NCT01735487): modest polyp reduction; not FDA-approved for FAP

**β-catenin pathway targeting in APC-mutant CRC:**
- Tankyrase inhibitors (XAV939, G007-LK): stabilize AXIN by blocking TNKS-mediated AXIN polyubiquitination → AXIN accumulates → destruction complex partially reconstituted even in APC-null cells → β-catenin degraded; preclinical activity in APC-mutant CRC; clinical development ongoing
- CBP/β-catenin inhibitors (ICG-001, PRI-724): block β-catenin-CBP interaction → reduce β-catenin transcriptional activity; Phase 1 trials in APC-mutant CRC
- WNT974 (Porcupine inhibitor): blocks Wnt ligand secretion; rationale limited in APC-mutant CRC (constitutive activation regardless of Wnt ligand) — not active; more useful in RSPO-amplified CRC where ligand is required

**NSAID chemoprevention:**
- **Sulindac**: COX-1/COX-2 inhibitor; reduces polyp number ~40-60% in FAP; does NOT prevent CRC (polyp regression not complete); not sufficient alone; used as adjunct to surveillance
- **Celecoxib (COX-2 selective)**: FDA-approved for FAP polyp reduction (as adjunct to surveillance and surgery, NOT as substitute for colectomy); Phase 3 FAP study: reduces polyp number by ~28-45% vs placebo; GI safety better than nonselective NSAIDs but cardiovascular toxicity concern
- Mechanism: COX-2 inhibition → prostaglandin E2 reduction → decreased Wnt pathway activity and reduced proliferation

**Surgical management:**
- Classic FAP: total proctocolectomy with IPAA (ileal pouch-anal anastomosis) → standard; preserves continence
- Alternatively: colectomy + ileorectal anastomosis (IRA) if rectum has few polyps; requires annual rectal surveillance thereafter
- AFAP: less urgent; surveillance until polypectomy inadequate → surgery then

## Connections

- `connects-to` → **[CTNNB1](../../03-molecular/ctnnb1/README.md)** — APC LOF → insufficient destruction complex → β-catenin nuclear accumulation → TCF/LEF → Wnt targets; equivalent to CTNNB1 activating mutation; APC MCR truncations (codons 1250-1450) leave incomplete SAMP repeats → AXIN binding lost → β-catenin not degraded
- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — APC is the gatekeeper of Wnt/β-catenin signaling in intestinal epithelium; APC LOF → constitutive Wnt-ON state → crypt stem cell expansion → adenoma; APC biallelic LOF is the earliest initiating event in sporadic CRC and FAP; complete APC LOF required in each adenoma
- `connects-to` → **[Colorectal Cancer](../../07-system/colorectal-cancer/README.md)** — APC is mutated in ~80% of sporadic CRC; Fearon-Vogelstein adenoma-carcinoma model: APC LOF → KRAS → SMAD4 → TP53 sequence; APC mutation cluster region (codons 1250-1450) in CRC; FAP: 100% CRC penetrance by 40 without colectomy; cetuximab/bevacizumab active in APC-mutant mCRC
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — Notch and Wnt/APC co-regulate intestinal crypt homeostasis; Notch NICD1 + APC LOF nuclear β-catenin → synergistic stem cell expansion in early CRC; dual Notch+Wnt hyperactivation in APC-mutant adenomas; γ-secretase inhibitors explored in APC-mutant colorectal cancer

[^kinzler-1991-apc]: Kinzler KW, Nilbert MC, Su LK, et al. Identification of FAP locus genes from chromosome 5q21. *Science.* 1991;253(5020):661-665. [doi:10.1126/science.1651562](https://doi.org/10.1126/science.1651562) · [PubMed 1651562](https://pubmed.ncbi.nlm.nih.gov/1651562/)
[^fearon-1990-vogelstein]: Fearon ER, Vogelstein B. A genetic model for colorectal tumorigenesis. *Cell.* 1990;61(5):759-767. [doi:10.1016/0092-8674(90)90186-i](https://doi.org/10.1016/0092-8674(90)90186-i) · [PubMed 2188735](https://pubmed.ncbi.nlm.nih.gov/2188735/)

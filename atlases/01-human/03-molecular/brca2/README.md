---
schema: human-scale-entry/v1
id: brca2
name: BRCA2
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Tumor suppressor; BRCA2-PALB2 complex loads RAD51 onto RPA-coated ssDNA → homologous recombination repair; BRCA2 loss → HRD → PARP inhibitor synthetic lethality. Germline BRCA2 mutations → breast (~50-70% LT risk), ovarian (~10-30%), prostate, and pancreatic cancer risk."
aliases: ["BRCA2", "FANCD1", "breast cancer 2", "BRCA2 tumor suppressor", "RAD51 loader", "HRD", "FANCD1 Fanconi anemia"]
sources:
  - id: wooster-1995-brca2
    type: peer-reviewed
    cite: "Wooster R, Bignell G, Lancaster J, et al. Identification of the breast cancer susceptibility gene BRCA2. Nature. 1995;378(6559):789-792."
    doi: "10.1038/378789a0"
    pmid: "8524414"
    url: "https://doi.org/10.1038/378789a0"
  - id: moore-2018-olaparib-solo1
    type: peer-reviewed
    cite: "Moore K, Colombo N, Scambia G, et al. Maintenance olaparib in patients with newly diagnosed advanced ovarian cancer. N Engl J Med. 2018;379(26):2495-2505."
    doi: "10.1056/NEJMoa1810858"
    pmid: "30345884"
    url: "https://doi.org/10.1056/NEJMoa1810858"
cross_links:
  - target: 01-human/03-molecular/rad51
    relation: connects-to
    note: "BRCA2 binds single-stranded DNA at sites of DSBs → loads RAD51 recombinase onto RPA-coated ssDNA → RAD51 nucleofilament formation → homology search and strand invasion → HR completion; BRCA2 loss → RAD51 cannot bind ssDNA → no HRR → PARP inhibitor synthetic lethality."
  - target: 01-human/03-molecular/brca1
    relation: connects-to
    note: "BRCA1 and BRCA2 act sequentially in HRR: BRCA1 (with BARD1) processes DSBs at 5' ends → recruits PALB2, which bridges to BRCA2 → RAD51 loading; germline BRCA1 predominantly causes HGSOC and basal-like breast cancer; BRCA2 predominantly causes HR+ breast and ovarian cancers."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN loss → PI3K-AKT-mTOR activation in clear cell and endometrioid ovarian cancer; PARP inhibitor activity in BRCA2-mutant ovarian cancer is potentiated by PTEN loss → AKT-mTOR promotes reliance on PARP for DSB repair; dual PARP+PI3K inhibition under study in HRD+ tumors."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 mutations in ~96% of HGSOC frequently co-occur with BRCA2 deficiency → dual checkpoint loss → replication stress and genomic instability; BRCA2-mutant tumors with TP53 loss are more genomically complex; MDM2 amplification in a minority of BRCA2-mutant ovarian cancers."
---

# BRCA2

## Overview

**BRCA2 (breast cancer susceptibility gene 2)** is a 3,418-amino-acid tumor suppressor protein encoded at chromosome 13q12.3. BRCA2 is the central mediator of **homologous recombination repair (HRR)** at DNA double-strand breaks (DSBs): it recruits the RAD51 recombinase to resected single-stranded DNA at DSB sites, enabling template-directed error-free repair. BRCA2 loss-of-function creates a state of **homologous recombination deficiency (HRD)**, which generates therapeutic vulnerability to **PARP inhibitors** through synthetic lethality — the conceptual and clinical cornerstone of BRCA-targeted therapy [^wooster-1995-brca2].

**BRCA2 vs. BRCA1:**
- Both are tumor suppressors in the HRR pathway but with distinct molecular roles: BRCA1 functions upstream (DSB recognition, end-resection, checkpoint signaling) while BRCA2 functions at the core step of RAD51 loading
- Germline BRCA2 mutations: lifetime breast cancer risk ~50-70% (slightly lower than BRCA1), ovarian cancer risk ~10-30% (lower than BRCA1's ~40-60%), prostate cancer (3-5× elevated, particularly aggressive early-onset), pancreatic cancer (3-5× elevated), melanoma (elevated)
- BRCA2 is also known as **FANCD1**: biallelic BRCA2 mutation → Fanconi anemia subtype D1, a severe childhood cancer predisposition syndrome

**BRCA2 in cancer genetics:**
- **Ashkenazi Jewish founder mutations:** BRCA2 6174delT (in addition to BRCA1 185delAG and BRCA1 5382insC)
- **Population frequency:** ~1:300-500 for BRCA2 heterozygous carriers in the general population; higher in Ashkenazi Jews (~1:40)
- **Penetrance:** Context-dependent; modifiers (RAD51 paralogue variants, other HRR genes, polygenic risk scores) influence cancer risk substantially

## Structure

### BRCA2 protein architecture

BRCA2 is a very large (384 kDa) largely unstructured protein with several discrete functional domains:

**N-terminal domain (NTD, 1-39):**
- Binds PALB2 (partner and localizer of BRCA2) → PALB2 bridges BRCA1 and BRCA2; PALB2 mutations cause an intermediate-penetrance BRCA2-like cancer syndrome; PALB2 loss → impairs BRCA2 nuclear localization and HR function

**BRCA2 repeats / BRC repeats (1002-2667):**
- Eight BRC repeats (~35 amino acids each); each BRC repeat binds one RAD51 monomer via an FxxA motif (phenylalanine-X-X-alanine) that mimics RAD51 self-oligomerization interface
- BRC repeat 1-4: Higher affinity for free RAD51 monomers → sequestration
- BRC repeat 5-8: Lower affinity; may modulate RAD51 nucleofilament dynamics
- BRCA2 delivers multiple RAD51 molecules simultaneously to ssDNA via cooperative BRC interactions → efficient nucleofilament assembly

**DNA binding domain (DBD, 2481-3186):**
- Contains **OB-fold domains (OB1, OB2, OB3)** — oligonucleotide/oligosaccharide binding folds that directly contact ssDNA and RPA (replication protein A)
- **Tower domain (between OB2-OB3):** Contains the BRCA2-DSSB binding domain for dsDNA at DSB junctions
- OB-fold domains mediate BRCA2 binding to RPA-coated ssDNA at resected DSBs → enables RAD51 delivery to the correct DNA substrate (ssDNA, not dsDNA)

**C-terminal domain (CTD, 3187-3418):**
- Contains **nuclear localization signals (NLS):** BRCA2 is strictly nuclear
- Binds **BRCA2 interacting domain (BRCA2-CTIP):** Promotes DNA end resection
- **RAD51 binding at CTD (Y3263):** A phosphorylation-dependent RAD51 binding site distinct from BRC repeats; important for efficient nucleofilament stabilization during late HR steps

### BRCA2 in the Fanconi anemia pathway

BRCA2 (FANCD1) participates in the **Fanconi anemia (FA) pathway** for interstrand crosslink (ICL) repair:
- ICL → FA core complex → monoubiquitinates FANCD2/FANCI → FANCD2-FANCI complex recruits nucleases (SLX4, XPF-ERCC1) to unhook the crosslink → gap created → TLS polymerase fills gap → BLM/BRCA1/BRCA2-dependent HR completes repair
- Biallelic BRCA2 (FANCD1) mutation → FA-D1: severe childhood cancer predisposition (Wilms tumor, medulloblastoma, ALL, AML) rather than breast/ovarian cancer (consistent with two-hit kinetics: loss of second allele early in development)

## Function

### BRCA2 in homologous recombination repair

**HR pathway (BRCA2-mediated steps):**

1. **DSB recognition:** MRN complex (MRE11-RAD50-NBS1) → ATM → CHK2/H2AX → checkpoint activation; BRCA1-BARD1 recruited to DSB via RING domain-MRN interaction
2. **End resection:** CtIP (RBBP8) + BRCA1 → 5'→3' resection at DSB ends → RPA (RPA70/32/14 heterotrimer) coats exposed 3' ssDNA → ssDNA-RPA structure
3. **BRCA2 delivery of RAD51:** PALB2 recruits BRCA2 to RPA-ssDNA; BRCA2 BRC repeats capture free RAD51 → deliver to RPA-ssDNA; OB-fold DBD contacts RPA-ssDNA → nucleates RAD51 filament; BRCA2 displaces RPA from ssDNA to allow RAD51 binding
4. **Homology search:** RAD51 filament (nucleoprotein filament) searches sister chromatid for complementary sequence → strand invasion → D-loop formation
5. **DNA synthesis:** Pol δ/ε extends from invaded strand using sister chromatid template → accurate repair using homologous sequence

**BRCA2 also functions in:**
- **Replication fork protection:** BRCA2 stabilizes stalled replication forks by protecting nascent DNA from MRE11 degradation; fork protection deficiency is a distinct consequence of BRCA2 loss that contributes to genomic instability independent of HRR
- **Cytokinesis:** BRCA2 localizes to the central spindle and midbody during cell division; facilitates abscission; BRCA2 loss → cytokinesis failure → aneuploidy
- **Centrosome duplication:** BRCA2 at centrosomes prevents centrosome amplification during S phase

### PARP inhibitor synthetic lethality

**PARP1/2 function:**
PARP1 detects single-strand breaks (SSBs) → poly-ADP-ribosylation (PAR) → recruits XRCC1, LIG3 → base excision repair (BER); PARP1 also functions at stalled replication forks and in regulating chromatin structure.

**PARP inhibitor mechanism in BRCA2-mutant cells:**
1. PARP inhibitor → traps PARP1/2 on DNA (catalytic inhibition + trapping of PARylated PARP on DNA)
2. Trapped PARP-DNA adducts → block replication forks → fork collapse → replication-associated DSBs
3. In BRCA2-intact cells: HRR repairs DSBs → cell survives
4. In BRCA2-mutant cells: HRR deficient → DSBs repaired by error-prone NHEJ → chromosome aberrations → mitotic catastrophe → cell death
5. **Synthetic lethality:** Loss of BRCA2 (one DNA repair pathway) + PARP inhibition (blocks another backup pathway) = lethal combination; neither alone is sufficient to kill the cell

**Approved PARP inhibitors and indications:**
- **Olaparib (Lynparza, AstraZeneca):** First PARP inhibitor approved; SOLO-1 → maintenance in BRCA1/2-mutant HGSOC → PFS 56% at 3 years vs. 12% placebo [^moore-2018-olaparib-solo1]; also approved in metastatic prostate cancer (PROfound, BRCA1/2/ATM), BRCA-mutant pancreatic cancer (POLO trial), and HER2-negative BRCA-mutant breast cancer (OlympiA adjuvant, OlympiAD metastatic)
- **Niraparib (Zejula, GSK):** NOVA trial → maintenance in ovarian cancer regardless of BRCA status (HRD+ enrichment); approved for frontline maintenance in all advanced ovarian cancer (PRIMA trial — niraparib vs. placebo regardless of BRCA)
- **Rucaparib (Rubraca, Pfizer):** Approved in BRCA1/2-mutant ovarian cancer; withdrawn from US market 2022 due to commercial/competitive reasons
- **Talazoparib (Talzenna, Pfizer):** Most potent PARP trapper; approved in germline BRCA1/2-mutant HER2-negative locally advanced/metastatic breast cancer

**PARP inhibitor resistance mechanisms:**
- **Reversion mutations:** Somatic "back-mutations" in BRCA2 that restore the open reading frame → HRR partially restored → PARPi resistance; most common resistance mechanism (~30-40% of resistant cases)
- **53BP1/RIF1 pathway loss:** Loss of NHEJ error-prone repair → even without HRR, cells survive (NHEJ loss → protection)
- **PARP1 expression loss:** Loss of drug target
- **Upregulation of drug efflux pumps (ABCB1)**

## Mechanism

### Germline BRCA2 testing and genetic counseling

**Variants of uncertain significance (VUS):**
BRCA2 is 3,418 aa → large gene → many VUS; interpretation uses: co-segregation with disease in families, evolutionary conservation (BRCA2 is highly conserved), functional assays (HR activity), ClinVar/LOVD databases; ~30% of BRCA2 variants detected are VUS — a major clinical challenge

**Cascade testing:**
If pathogenic BRCA2 mutation identified → offer testing to first/second-degree relatives; 50% chance per first-degree relative of inheriting; positive relatives → enhanced surveillance and risk-reduction options

**Risk-reduction strategies for BRCA2 carriers:**
- **Breast:** Annual MRI + mammography starting age 25 (semiannual alternating); bilateral risk-reducing mastectomy (reduces risk by ~90-95%)
- **Ovarian:** Risk-reducing salpingo-oophorectomy (RRSO) at age 40-45 (after childbearing); reduces ovarian cancer risk by ~80%; also reduces breast cancer risk by ~50%
- **Prostate:** PSA screening starting at 40 in BRCA2 carriers (IMPACT study → biennial PSA recommended); high-risk prostate screening protocol
- **Pancreatic:** No established screening; CAPS trials suggest MRI/EUS surveillance in BRCA2 carriers with FH of pancreatic cancer

### BRCA2 in prostate cancer

BRCA2 mutations in ~4-5% of all prostate cancer patients (vs. ~0.3% population prevalence) — especially in high-risk/metastatic disease (~10-15%). BRCA2-mutant prostate cancer:
- More aggressive: higher Gleason grade, more metastatic
- **Olaparib (PROfound trial):** PFS 7.4 vs. 3.6 months in BRCA1/2-mutant mCRPC after ENZA/ABI; FDA approved 2020
- **Rucaparib:** Also approved for BRCA1/2-mutant mCRPC
- **Niraparib + abiraterone (MAGNITUDE trial):** PFS benefit in BRCA+ mCRPC

## Connections

- `connects-to` → **[RAD51](../../03-molecular/rad51/README.md)** — BRCA2 binds single-stranded DNA at sites of DSBs → loads RAD51 recombinase onto RPA-coated ssDNA → RAD51 nucleofilament formation → homology search and strand invasion → HR completion; BRCA2 loss → RAD51 cannot bind ssDNA → no HRR → PARP inhibitor synthetic lethality.
- `connects-to` → **[BRCA1](../../03-molecular/brca1/README.md)** — BRCA1 and BRCA2 act sequentially in HRR: BRCA1 (with BARD1) processes DSBs at 5' ends → recruits PALB2, which bridges to BRCA2 → RAD51 loading; germline BRCA1 mutations predominantly cause HGSOC and basal-like breast cancer; BRCA2 predominantly causes HR+ breast and ovarian cancers.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss → PI3K-AKT-mTOR activation in clear cell and endometrioid ovarian cancer; PARP inhibitor activity in BRCA2-mutant ovarian cancer is potentiated by PTEN loss → AKT-mTOR promotes reliance on PARP for DSB repair; dual PARP+PI3K inhibition under study in HRD+ tumors.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 mutations in ~96% of HGSOC frequently co-occur with BRCA2 deficiency → dual checkpoint loss → replication stress and genomic instability; BRCA2-mutant tumors with TP53 loss are more genomically complex; MDM2 amplification in a minority of BRCA2-mutant ovarian cancers.

[^wooster-1995-brca2]: Wooster R, Bignell G, Lancaster J, et al. Identification of the breast cancer susceptibility gene BRCA2. *Nature.* 1995;378(6559):789-792. [doi:10.1038/378789a0](https://doi.org/10.1038/378789a0) · [PubMed 8524414](https://pubmed.ncbi.nlm.nih.gov/8524414/)
[^moore-2018-olaparib-solo1]: Moore K, Colombo N, Scambia G, et al. Maintenance olaparib in patients with newly diagnosed advanced ovarian cancer. *N Engl J Med.* 2018;379(26):2495-2505. [doi:10.1056/NEJMoa1810858](https://doi.org/10.1056/NEJMoa1810858) · [PubMed 30345884](https://pubmed.ncbi.nlm.nih.gov/30345884/)

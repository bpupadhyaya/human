---
schema: human-scale-entry/v1
id: pik3ca
name: PIK3CA
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Catalytic subunit of PI3K; phosphorylates PIP2 to PIP3, activating AKT-mTOR. Gain-of-function mutations (H1047R, E545K) in 25-40% of breast and 15% of colorectal cancers. Alpelisib (PI3K-alpha inhibitor) approved for PIK3CA-mutant HR+/HER2- breast cancer."
aliases: ["PI3K", "PI3Kalpha", "PI3K p110alpha", "phosphoinositide 3-kinase catalytic alpha", "p110alpha"]
sources:
  - id: samuels-2004-pik3ca-mutation
    type: peer-reviewed
    cite: "Samuels Y, Wang Z, Bardelli A, et al. High frequency of mutations of the PIK3CA gene in human cancers. Science. 2004;304(5670):554."
    doi: "10.1126/science.1096502"
    pmid: "15016963"
    url: "https://doi.org/10.1126/science.1096502"
  - id: andre-2019-solar-1
    type: peer-reviewed
    cite: "André F, Ciruelos E, Rubovszky G, et al. Alpelisib for PIK3CA-Mutated, Hormone Receptor-Positive Advanced Breast Cancer. N Engl J Med. 2019;380(20):1929-1940."
    doi: "10.1056/NEJMoa1813904"
    pmid: "31091374"
    url: "https://doi.org/10.1056/NEJMoa1813904"
  - id: engelman-2006-pi3k-review
    type: peer-reviewed
    cite: "Engelman JA, Luo J, Cantley LC. The evolution of phosphatidylinositol 3-kinases as regulators of growth and metabolism. Nat Rev Genet. 2006;7(8):606-619."
    doi: "10.1038/nrg1879"
    pmid: "16847462"
    url: "https://doi.org/10.1038/nrg1879"
cross_links:
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "PI3K→AKT→mTORC1 is the central growth and survival axis; PIK3CA mutation constitutively activates AKT → mTORC1 → S6K and 4EBP1 → protein synthesis and cell growth; mTOR inhibitors (everolimus) partially overcome PI3K pathway activation but lack durable responses due to feedback."
  - target: 01-human/03-molecular/her2
    relation: connects-to
    note: "HER2 activates PI3K via p85 binding and via RAS; PIK3CA mutation confers partial resistance to trastuzumab in HER2+ breast cancer; combining alpelisib with anti-HER2 therapy overcomes this resistance in PIK3CA-mutant HER2+ tumors."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "KRAS activates both PI3K-AKT and RAF-MEK-ERK; in CRC, concurrent KRAS and PIK3CA mutations are common; PIK3CA H1047R mutation is mutually exclusive with PTEN loss in some cancers; combined KRAS+PIK3CA inhibition shows synergistic anti-tumor activity in preclinical models."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "PTEN (PI3K phosphatase) is a p53 transcriptional target; p53 loss → reduced PTEN → enhanced PI3K-AKT signaling; AKT phosphorylates MDM2 → nuclear MDM2 → p53 degradation, creating a reciprocal negative loop; PIK3CA mutation and TP53 mutation co-occur in many solid tumors."
---

# PIK3CA

## Overview

**PIK3CA** encodes the **p110-alpha** catalytic subunit of class I **PI3K (phosphatidylinositol 3-kinase)**, the lipid kinase that phosphorylates **PIP2 (phosphatidylinositol-4,5-bisphosphate) to PIP3 (phosphatidylinositol-3,4,5-trisphosphate)** at the inner leaflet of the plasma membrane. PIP3 recruits and activates **AKT (protein kinase B)** → activates **mTORC1** and dozens of downstream survival, proliferation, and metabolic targets — the **PI3K-AKT-mTOR pathway**, one of the most frequently activated oncogenic signaling cascades in human cancer [^engelman-2006-pi3k-review].

PIK3CA gain-of-function **somatic mutations** were first reported at high frequency in human cancers in 2004 [^samuels-2004-pik3ca-mutation], with two mutational hotspots (H1047R and E545K/E542K) collectively accounting for ~80% of PIK3CA cancer mutations. These mutations increase PIP3 production constitutively, bypassing the requirement for upstream RTK activation.

**PIK3CA mutation prevalence:**
- **Breast cancer (HR+/HER2-):** 35-40% — the highest frequency of any major cancer; concentrated in luminal B subtype; H1047R (exon 20, kinase domain) most common
- **Breast cancer (HER2+):** 20-25% — co-driver with HER2; contributes to trastuzumab resistance
- **Colorectal cancer:** 15-20%; enriched in right-sided/MSI tumors; E545K/H1047R
- **Endometrial cancer:** 25-36%; often with PTEN loss
- **Cervical cancer:** ~30%; SCC subtype
- **Bladder cancer:** 20%
- **Head and neck (HNSCC):** 10-15%
- **Ovarian cancer:** ~12% (clear cell subtype ~40%)

**PIK3CA germline mutations (Cowden syndrome):** PTEN loss-of-function germline mutations cause Cowden syndrome (PTEN hamartoma tumor syndrome, PHTS) with similar pathway effect; PIK3CA gain-of-function germline mutations cause PROS (PIK3CA-Related Overgrowth Spectrum) — segmental overgrowth syndromes (CLOVES, Klippel-Trenaunay); treated with alpelisib (off-label/compassionate use).

## Structure

### PI3K class I complex

Class I PI3Ks are **heterodimers** of a catalytic subunit (p110) and a regulatory subunit (p85/p55/p50):

**PIK3CA (p110-alpha) domain structure:**
- **ABD (adaptor-binding domain, aa 1-108):** Constitutively binds the SH2 domains of the regulatory p85 subunit (PIK3R1) → maintains p110 in autoinhibited state; oncogenic mutations in E domain (H1047R) relieve p85-mediated inhibition
- **RBD (Ras-binding domain, aa 190-291):** Binds GTP-loaded RAS (KRAS, HRAS, NRAS) → allosteric activation; RBD mutations that disrupt RAS binding reduce PI3K oncogenicity
- **C2 domain (aa 358-481):** Membrane interaction
- **Helical domain (aa 542-726):** Contains hotspot mutations E542K and E545K (disrupt inhibitory interaction with p85 N-SH2 domain → constitutive activation)
- **Kinase domain (aa 727-1068):** Catalytic lipid kinase; H1047R is in the activation loop → increased membrane affinity and PIP3 production

**Regulatory subunit (PIK3R1, p85-alpha):**
- Two SH2 domains (N-SH2 and C-SH2): bind phosphorylated YXXM motifs on activated RTKs (EGFR, HER2, IGFR1, insulin receptor) → relief of p110 autoinhibition → membrane recruitment
- SH3 and rho-GAP domains: additional scaffolding functions

### PI3K family context

| Isoform | Regulatory | Primary activator | Key function |
|:---|:---|:---|:---|
| p110-alpha (PIK3CA) | p85 | RTKs, RAS | Growth, survival, metabolism |
| p110-beta (PIK3CB) | p85 | GPCRs, RAS | Growth; activated by PTEN loss |
| p110-delta (PIK3CD) | p85 | BCR, TCR, cytokine receptors | B/T cell signaling |
| p110-gamma (PIK3CG) | p101/p84 | GPCRs | Neutrophil/macrophage function |

## Function

### PI3K-AKT-mTOR pathway

The PI3K-AKT-mTOR cascade is the master regulator of cell growth and survival [^engelman-2006-pi3k-review]:

1. **RTK activation** → autophosphorylation → p85 SH2 binding → p110-alpha recruited to membrane → PIP2 → PIP3
2. **PIP3** recruits **PDK1** and **AKT** (all 3 isoforms: AKT1, AKT2, AKT3) via PH domains → PDK1 phosphorylates AKT Thr308 → mTORC2 phosphorylates AKT Ser473 → full AKT activation
3. **AKT** phosphorylates:
   - **TSC2** → relieves mTORC1 inhibition → **mTORC1** → S6K1/4EBP1 → protein synthesis, ribosome biogenesis
   - **FOXO** transcription factors → cytoplasmic sequestration → suppresses apoptotic/cell cycle arrest genes (p21, BIM, PUMA)
   - **MDM2** → nuclear translocation → p53 ubiquitination and degradation
   - **GSK-3beta** → inhibition → stabilizes cyclin D1, beta-catenin → G1 progression and Wnt pathway amplification
   - **BAD** → dissociates from BCL-2/BCL-XL → anti-apoptotic signal
4. **PTEN (phosphatase and tensin homolog):** PIP3 → PIP2 phosphatase; PTEN is the key negative regulator of PI3K signaling; PTEN loss → constitutive AKT activation even without PIK3CA mutation

**PIK3CA H1047R mechanism:**
- H1047R in the activation loop → increased membrane affinity of p110 → enhanced PIP3 production constitutively; acts independently of RTK input but synergizes with RTK activation
- **E545K/E542K:** In the helical domain → disrupts inhibitory interaction of N-SH2 domain of p85 → releases p110 autoinhibition → constitutive activity without RTK binding

### PIK3CA in breast cancer

**Hormone receptor-positive (HR+)/HER2- breast cancer:**
- PIK3CA mutations are the most common genetic alteration in luminal breast cancer
- PIK3CA mutation → increased PI3K-AKT signaling → promotes estrogen receptor (ER)-independent growth → **endocrine therapy resistance** (tamoxifen, aromatase inhibitors)
- **Mechanism of endocrine resistance:** AKT phosphorylates ER directly (Ser167) → ligand-independent ER transcriptional activation; also: AKT → mTORC1 → S6K → ER phosphorylation → tamoxifen resistance
- **Predictive biomarker:** PIK3CA mutation predicts alpelisib benefit in SOLAR-1 trial

## Mechanism

### Alpelisib and PI3K inhibition [^andre-2019-solar-1]

**Alpelisib (BYL719, Piqray, Novartis):** PI3K-alpha selective inhibitor (>50× selectivity for p110-alpha vs. p110-beta); FDA approved May 2019 for **PIK3CA-mutated, HR+/HER2- advanced breast cancer** (with fulvestrant) after progression on endocrine therapy.

**SOLAR-1 trial:**
- Population: HR+/HER2- advanced breast cancer with PIK3CA mutation (ctDNA) after prior endocrine therapy
- Alpelisib + fulvestrant vs. placebo + fulvestrant
- **PFS in PIK3CA-mutant cohort: 11.0 vs 5.7 months** (HR 0.65); ORR 26.6% vs 12.8%
- No benefit in PIK3CA-wildtype cohort (PFS 7.4 vs 5.6 months) — confirms predictive biomarker utility
- **Toxicity:** Hyperglycemia (63.7%; mechanism: insulin secretion requires PI3K-alpha in beta cells; treat with metformin); rash (52.5%; manage with antihistamines); diarrhea; dose reductions in ~25%
- **ctDNA selection test:** Therascreen PIK3CA RGQ PCR kit (plasma ctDNA) — FDA-approved companion diagnostic; tissue NGS also acceptable

**Other PI3K inhibitors:**
- **Copanlisib (pan-PI3K):** IV; approved for relapsed follicular lymphoma (B-cell: PI3K-delta + PI3K-alpha); hyperglycemia is transient (on-target, IV dosing)
- **Idelalisib (PI3K-delta):** Oral; approved for follicular lymphoma, CLL (with rituximab); immune-related colitis, hepatotoxicity (grade 3 in ~15%) limit use
- **Duvelisib (PI3K-delta/gamma):** CLL, follicular lymphoma; targets immune cell PI3K isoforms
- **Capivasertib (AKT inhibitor):** Combined with fulvestrant in CAPItello-291 (PIK3CA/AKT/PTEN-altered HR+/HER2- breast cancer): PFS 7.3 vs 3.1 months — FDA approved 2023; targets pathway downstream of PIK3CA and PTEN alterations

**Resistance to PI3K-alpha inhibition:**
- PTEN loss → PI3K-beta (not alpha) drives AKT → alpelisib ineffective
- Feedback: PI3K inhibition → reduces S6K → relieves S6K-mediated IRS1 degradation → increased IRS1 → RTK (HER3/IGFR1) reactivates PI3K → adaptive resistance
- ESR1 mutations (Y537S, D538G): Co-occurring with PIK3CA in endocrine-resistant breast cancer → use fulvestrant (pan-ESR1) or elacestrant (selective ER degrader) combinations
- Concurrent KRAS/BRAF mutations → bypass PI3K dependence via MEK-ERK

## Connections

- `connects-to` → **[mTOR](../mtor/README.md)** — PI3K→AKT→mTORC1 is the central growth signaling axis; PIK3CA mutation constitutively activates AKT → mTORC1 → protein synthesis and survival; mTOR inhibitors (everolimus) partially block but trigger compensatory feedback loop reactivation of PI3K via IRS1.
- `connects-to` → **[HER2](../her2/README.md)** — HER2 directly activates PI3K via p85 binding; PIK3CA mutation causes partial resistance to anti-HER2 therapy (trastuzumab); combining alpelisib with anti-HER2 therapy overcomes resistance in PIK3CA-mutant HER2+ breast and gastric tumors.
- `connects-to` → **[KRAS](../kras/README.md)** — KRAS activates both PI3K-AKT and MEK-ERK; concurrent PIK3CA and KRAS mutations occur in CRC and lung cancer; combined KRAS+PI3K inhibition shows synergistic anti-tumor activity and may be needed for durable response in co-mutant tumors.
- `connects-to` → **[p53](../p53/README.md)** — PTEN is a p53 transcriptional target; p53 loss reduces PTEN → PI3K-AKT hyperactivation; AKT phosphorylates MDM2 → p53 degradation, creating a negative regulatory loop; PIK3CA mutation and TP53 mutation co-occur in aggressive breast, ovarian, and uterine cancers.

[^samuels-2004-pik3ca-mutation]: Samuels Y, Wang Z, Bardelli A, et al. High frequency of mutations of the PIK3CA gene in human cancers. *Science.* 2004;304(5670):554. [doi:10.1126/science.1096502](https://doi.org/10.1126/science.1096502) · [PubMed 15016963](https://pubmed.ncbi.nlm.nih.gov/15016963/)
[^andre-2019-solar-1]: André F, Ciruelos E, Rubovszky G, et al. Alpelisib for PIK3CA-Mutated, Hormone Receptor-Positive Advanced Breast Cancer. *N Engl J Med.* 2019;380(20):1929-1940. [doi:10.1056/NEJMoa1813904](https://doi.org/10.1056/NEJMoa1813904) · [PubMed 31091374](https://pubmed.ncbi.nlm.nih.gov/31091374/)
[^engelman-2006-pi3k-review]: Engelman JA, Luo J, Cantley LC. The evolution of phosphatidylinositol 3-kinases as regulators of growth and metabolism. *Nat Rev Genet.* 2006;7(8):606-619. [doi:10.1038/nrg1879](https://doi.org/10.1038/nrg1879) · [PubMed 16847462](https://pubmed.ncbi.nlm.nih.gov/16847462/)

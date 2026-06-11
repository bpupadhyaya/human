---
schema: human-scale-entry/v1
id: her2
name: HER2
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "ErbB2/HER2 receptor tyrosine kinase; ligandless but preferred ErbB dimerization partner amplifying EGFR/HER3/HER4 signaling. Amplified in 15–20% of breast cancer and 15% of gastric cancer. Targeted by trastuzumab, pertuzumab, T-DM1, and T-DXd (trastuzumab deruxtecan)."
aliases: ["ErbB2", "HER-2", "HER2/neu", "c-erbB-2", "CD340", "proto-oncogene HER2"]
sources:
  - id: slamon-1987-her2
    type: peer-reviewed
    cite: "Slamon DJ, Clark GM, Wong SG, Levin WJ, Ullrich A, McGuire WL. Human breast cancer: correlation of relapse and survival with amplification of the HER-2/neu oncogene. Science. 1987;235(4785):177-182."
    doi: "10.1126/science.3798106"
    pmid: "3798106"
    url: "https://doi.org/10.1126/science.3798106"
  - id: slamon-2001-trastuzumab
    type: peer-reviewed
    cite: "Slamon DJ, Leyland-Jones B, Shak S, et al. Use of chemotherapy plus a monoclonal antibody against HER2 for metastatic breast cancer that overexpresses HER2. N Engl J Med. 2001;344(11):783-792."
    doi: "10.1056/NEJM200103153441101"
    pmid: "11248153"
    url: "https://doi.org/10.1056/NEJM200103153441101"
  - id: modi-2022-tdxd
    type: peer-reviewed
    cite: "Modi S, Jacot W, Yamashita T, et al. Trastuzumab Deruxtecan in Previously Treated HER2-Positive Metastatic Breast Cancer. N Engl J Med. 2022;387(1):9-20."
    doi: "10.1056/NEJMoa2203690"
    pmid: "35665782"
    url: "https://doi.org/10.1056/NEJMoa2203690"
cross_links:
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "HER2 lacks a high-affinity ligand but adopts an open, dimerization-ready conformation → preferred heterodimerization partner for EGFR, HER3, HER4, amplifying ErbB signaling 10-100×; EGFR-HER2 is the most potent signaling heterodimer and a resistance mechanism to EGFR TKIs."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "HER2 amplification strongly activates PI3K-Akt-mTOR via HER3 (which has multiple PI3K docking sites); mTOR-driven protein synthesis and survival are critical in HER2-positive tumors; everolimus + exemestane is active in trastuzumab-resistant HER2+ breast cancer (BOLERO-3 trial)."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "HER2 drives RAS-MEK-ERK via Grb2-SOS1 downstream of EGFR-HER2 heterodimers; RAS mutations co-occurring with HER2 amplification in gastric cancer cause trastuzumab resistance (active RAS bypasses HER2); RAS-WT is a selection criterion for anti-HER2 therapy in GEJ cancer."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "HER2-amplified tumors upregulate PD-L1 via PI3K-Akt-NF-κB and IFN-γ → adaptive immune resistance; trastuzumab + anti-PD-1 (pembrolizumab) in HER2+ gastric cancer (KEYNOTE-811): improved ORR and PFS; HER2 amplification and PD-L1 expression are complementary therapeutic targets."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PIK3CA mutations co-occur with HER2 amplification in ~30% of HER2+ breast cancer → PI3K reactivated downstream of HER2 blockade → trastuzumab resistance; alpelisib (PI3Kα inhibitor) + trastuzumab in PIK3CA-mutant HER2+ BC; PIK3CA is the dominant anti-HER2 resistance co-mutation."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "HER2 activates STAT3 via JAK2 and Src → STAT3 nuclear → MYC, cyclin D1, BCL-XL, VEGF transcription; STAT3 activation correlates with trastuzumab resistance in HER2+ breast cancer; tumor-associated macrophage IL-6 → STAT3 → HER2+ TME immunosuppression and treatment resistance."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN loss → constitutive PI3K-Akt → bypasses HER2 blockade → trastuzumab resistance; PTEN loss (~30% HER2+ tumors) predicts reduced trastuzumab benefit; HER2 amplification + PTEN loss cooperate — dual PI3Kα (alpelisib) + HER2 (trastuzumab) blockade improves PTEN-null resistance."
---

# HER2

## Overview

**HER2 (human epidermal growth factor receptor 2, also ErbB2/HER-2/neu)** is a **receptor tyrosine kinase** of the ErbB family and the most potent oncogenic driver in the ErbB receptor network. Unlike its three family members (EGFR/HER1, HER3, HER4), HER2 has **no known high-affinity ligand** — it instead exists in an open, dimerization-ready conformation that makes it the **preferred heterodimerization partner** for all other ErbB receptors. As a result, HER2 amplifies the signaling output of EGFR, HER3, and HER4 by 10-100-fold when they form heterodimers.

First identified as the viral oncogene v-erbB2 (chicken) and its cellular homolog c-erbB2 (rat neu, 1984-1985), HER2 was linked to human breast cancer prognosis by Slamon and colleagues in 1987 — demonstrating that HER2 amplification (by FISH) correlated with shorter disease-free and overall survival [^slamon-1987-her2]. This discovery, combined with the development of **trastuzumab (Herceptin)** by Genentech, defined the paradigm of molecularly targeted oncology.

**HER2 amplification/overexpression:**
- **Breast cancer:** 15-20% of breast cancers; historically associated with poor prognosis; now among the most treatable subtypes with targeted therapy
- **Gastric/gastroesophageal junction (GEJ) cancer:** ~15-20%; trastuzumab-based first-line therapy (ToGA trial)
- **Endometrial cancer:** ~20-30% (HER2-amplified serous histology)
- **Colorectal cancer:** ~5% (primarily in RAS/RAF-WT tumors — actionable in 3rd+ line with trastuzumab + tucatinib)
- **Lung adenocarcinoma:** HER2 mutations (exon 20 insertions) ~3%, HER2 amplification ~6%
- **Salivary gland cancer:** HER2 amplification ~30%

**HER2-targeted therapeutic arsenal:**
- **Trastuzumab (Herceptin):** Anti-HER2 IgG1 antibody; binds HER2 extracellular domain IV → blocks dimerization, activates ADCC
- **Pertuzumab (Perjeta):** Anti-HER2 antibody; binds domain II (dimerization arm) → blocks HER2-HER3 heterodimerization specifically; synergistic with trastuzumab (double HER2 blockade)
- **T-DM1 (trastuzumab emtansine, Kadcyla):** Antibody-drug conjugate (ADC); trastuzumab + DM1 (microtubule poison) via thioether linker
- **T-DXd (trastuzumab deruxtecan, Enhertu):** ADC; trastuzumab + deruxtecan (topoisomerase I inhibitor payload) via cleavable tetrapeptide linker; high drug-to-antibody ratio (8:1); bystander effect (membrane-permeable payload kills neighboring cells) [^modi-2022-tdxd]
- **Lapatinib, tucatinib, neratinib:** Small molecule HER2/EGFR TKIs; cross BBB (CNS activity)

## Structure

### HER2 protein and extracellular architecture

HER2 is a **1255 amino acid type I transmembrane glycoprotein** (~185 kDa):

**Extracellular domain (ECD, aa 1-630): four subdomains:**
- **Domain I (L1):** Leucine-rich repeats; ligand-binding domain in EGFR/HER4; in HER2, no ligand binds here
- **Domain II (S1/CR1):** Cysteine-rich; contains the **dimerization arm (loop II-2)** — critical for heterodimerization; **pertuzumab binds here** → blocks HER2-HER3 dimerization
- **Domain III (L2):** Leucine-rich repeats; second leucine-rich domain
- **Domain IV (S2/CR2):** Cysteine-rich; contains the **trastuzumab binding epitope (close to transmembrane anchor)** → **trastuzumab binds here** → blocks HER2 shedding and activates ADCC; also contains the ADAM10/17 metalloprotease cleavage site → generates p95-HER2 fragment (truncated, constitutively active, trastuzumab-resistant)

**Why HER2 has no ligand:** Comparison with EGFR: the HER2 domain II dimerization arm is constitutively exposed (no autoinhibitory tether) and domain I is in a "preformed open state" → HER2 is always dimerization-competent; pseudo-liganded by the domain I-III interaction that is absent in HER2 structure

**Transmembrane and intracellular:**
- Single TM helix (aa 632-659)
- Juxtamembrane (660-720): regulates kinase activation
- Kinase domain (720-987): active; asymmetric dimerization to activate partner kinase (HER2 acts as activator kinase); Thr877 equivalent to EGFR T790M as gatekeeper; neratinib and afatinib covalently modify Cys805
- C-terminal tail (987-1255): 6 phosphorylation sites; docking sites for PI3K (via HER3 bridge), GRB7 (Tyr1248), SHC/GRB2 (Tyr877), PLCG1

**HER2-HER3 heterodimer: the dominant oncogenic unit:**
- HER3 has impaired kinase activity (~1000× reduced vs HER2) but has 6 PI3K-binding p-Tyr sites in its C-tail; when HER2 phosphorylates HER3 → HER3 recruits PI3K → maximal PI3K-Akt-mTOR activation; this HER2-HER3 pair is the most potent PI3K activator in the ErbB family

## Function

### Signal transduction from HER2

**Upon EGFR-HER2 heterodimerization (most potent mitogenic pair):**
- EGFR kinase domain phosphorylates EGFR C-tail → GRB2-SOS1 → RAS → RAF → MEK → ERK → proliferation
- HER2 kinase phosphorylates HER2 C-tail → GRB7 (involved in cell migration) + SHC/GRB2 → RAS
- Tumor: sustained and amplified RAS-ERK signaling

**Upon HER2-HER3 heterodimerization (dominant PI3K activator):**
- HER2 kinase phosphorylates HER3 C-tail at 6 YXXM motifs → direct PI3K p85 binding → PIP3 → Akt → mTOR → survival, protein synthesis
- Combined PI3K + RAS-ERK activation → maximal proliferative/survival output

### HER2 in breast cancer biology

In HER2-positive breast cancer:
- Chromosomal amplification of 17q12 → HER2 gene copies 10-100× → protein overexpression (3+ IHC or FISH ratio ≥2.0)
- HER2 overexpression → constitutive heterodimerization without ligand → continuous PI3K-Akt-mTOR and RAS-ERK signaling → cell cycle progression (cyclin D1), survival (BCL-XL, MCL-1), invasion (MMP expression)
- HER2+ breast cancers have high grade, rapid proliferation, frequent brain metastasis (HER2 and lapatinib/tucatinib data)
- Historical prognosis: poor; with targeted therapy: dramatically improved (5-year pCR ~40-70% in early-stage)

### HER2 low and ultratlow (emerging paradigm)

Traditional HER2 testing: IHC 3+ or IHC 2+/FISH+ = HER2+; IHC 0 = HER2-negative.
**HER2-low** (IHC 1+ or IHC 2+/FISH-): ~50% of all breast cancers; previously considered HER2-negative.
- T-DXd (trastuzumab deruxtecan) shows activity in HER2-low metastatic breast cancer (DESTINY-Breast04: 9.9 vs 5.1 months PFS vs chemotherapy — approval 2022)
- Mechanism: high DAR (drug:antibody ratio = 8) + bystander effect → effective even at low HER2 surface expression
- Extends HER2-targeted therapy to a much larger patient population

## Mechanism

### Trastuzumab mechanism of action [^slamon-2001-trastuzumab]

Trastuzumab is a humanized IgG1 anti-HER2 monoclonal antibody binding HER2 domain IV:
1. **HER2 shedding inhibition:** ADAM10/17 cleaves HER2 ECD → p95-HER2 (lacks trastuzumab binding site, constitutively active); trastuzumab blocks shedding → maintains full-length HER2 + reduces trastuzumab-resistant p95 generation
2. **HER2 dimerization inhibition:** Partial; pertuzumab (domain II) more directly blocks dimerization
3. **ADCC (antibody-dependent cellular cytotoxicity):** Trastuzumab IgG1 Fc → NK cell FcγRIII (CD16) → perforin/granzyme B → tumor cell lysis; a major mechanism of action (ADCC activity correlates with FcγRIII polymorphisms)
4. **PI3K/Akt attenuation:** Trastuzumab → reduced HER2-HER3 signaling → reduced PI3K activation

**CLEOPATRA trial (pertuzumab + trastuzumab + docetaxel, 1st-line HER2+ mBC):** Median OS 57.1 vs 40.8 months (placebo + trastuzumab + docetaxel) — the longest OS ever reported in HER2+ mBC at time of publication; double HER2 blockade is standard of care.

**T-DXd (trastuzumab deruxtecan) — 3rd generation ADC [^modi-2022-tdxd]:**
- DESTINY-Breast03 (HER2+ mBC, 2nd line): T-DXd vs T-DM1 → PFS not reached vs 6.8 months (HR 0.28); ORR 79.7% vs 34.2%; T-DXd is now 2nd-line standard
- DESTINY-Breast04 (HER2-low mBC): HER2-low patients: 9.9 vs 5.1 months PFS; approved 2022 — opens HER2-low as actionable category
- Key toxicity: **interstitial lung disease (ILD, ~15%)** — can be fatal; careful monitoring required; grade 3-4 ILD in ~3%

**Trastuzumab resistance mechanisms:**
- **HER2 ECD shedding** → p95-HER2 (trastuzumab cannot bind); treated with TKIs (lapatinib, tucatinib)
- **PI3K/PTEN mutations:** PIK3CA mutations in ~30% of HER2+ tumors → PI3K reactivation downstream of HER2 blockade; alpelisib + trastuzumab being studied
- **Alternative receptor activation:** IGFR1, FGFR, MET
- **Autophagy-mediated trastuzumab resistance:** Trastuzumab induces autophagy → sequestration of HER2 in autophagosomes → reduced surface HER2; chloroquine + trastuzumab synergistic in preclinical models

## Connections

- `connects-to` → **[EGFR](../egfr/README.md)** — HER2 is the preferred dimerization partner for EGFR; EGFR-HER2 heterodimer is the most potent ErbB signaling pair; HER2 amplification is a resistance mechanism to EGFR TKIs by providing an amplified bypass.
- `connects-to` → **[mTOR](../mtor/README.md)** — HER2-HER3 heterodimer strongly activates PI3K→Akt→mTOR via HER3's 6 PI3K docking sites; mTOR is a major survival pathway in HER2+ tumors; everolimus + trastuzumab overcomes some trastuzumab resistance.
- `connects-to` → **[KRAS](../kras/README.md)** — HER2 drives RAS-ERK via Grb2-SOS1; RAS mutations co-occurring with HER2 amplification in gastric cancer confer trastuzumab resistance; RAS pathway status influences HER2-targeted therapy response.
- `connects-to` → **[PD-1](../pd-1/README.md)** — HER2-amplified tumors upregulate PD-L1 via PI3K-Akt-NF-κB; anti-HER2 + anti-PD-1 (trastuzumab + pembrolizumab, KEYNOTE-811) improve outcomes in HER2+ gastric cancer; combined blockade addresses both oncogenic and immune evasion mechanisms.
- `connects-to` → **[PIK3CA](../pik3ca/README.md)** — PIK3CA mutations co-occur with HER2 amplification in ~30% of HER2+ breast cancer → PI3K reactivated downstream of HER2 blockade → trastuzumab resistance; alpelisib (PI3Kα inhibitor) + trastuzumab in PIK3CA-mutant HER2+ BC; PIK3CA is the dominant anti-HER2 resistance co-mutation.
- `connects-to` → **[STAT3](../stat3/README.md)** — HER2 activates STAT3 via JAK2 and Src → STAT3 nuclear → MYC, cyclin D1, BCL-XL, VEGF transcription; STAT3 activation correlates with trastuzumab resistance in HER2+ breast cancer; tumor-associated macrophage IL-6 → STAT3 → HER2+ TME immunosuppression and treatment resistance.
- `connects-to` → **[PTEN](../pten/README.md)** — PTEN loss → constitutive PI3K-Akt → bypasses HER2 blockade → trastuzumab resistance; PTEN loss (~30% HER2+ tumors) predicts reduced trastuzumab benefit; HER2 amplification + PTEN loss cooperate — dual PI3Kα (alpelisib) + HER2 (trastuzumab) blockade improves PTEN-null resistance.

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^slamon-1987-her2]: Slamon DJ, Clark GM, Wong SG, Levin WJ, Ullrich A, McGuire WL. Human breast cancer: correlation of relapse and survival with amplification of the HER-2/neu oncogene. *Science.* 1987;235(4785):177-182. [doi:10.1126/science.3798106](https://doi.org/10.1126/science.3798106) · [PubMed 3798106](https://pubmed.ncbi.nlm.nih.gov/3798106/)
[^slamon-2001-trastuzumab]: Slamon DJ, Leyland-Jones B, Shak S, et al. Use of chemotherapy plus a monoclonal antibody against HER2 for metastatic breast cancer that overexpresses HER2. *N Engl J Med.* 2001;344(11):783-792. [doi:10.1056/NEJM200103153441101](https://doi.org/10.1056/NEJM200103153441101) · [PubMed 11248153](https://pubmed.ncbi.nlm.nih.gov/11248153/)
[^modi-2022-tdxd]: Modi S, Jacot W, Yamashita T, et al. Trastuzumab Deruxtecan in Previously Treated HER2-Positive Metastatic Breast Cancer. *N Engl J Med.* 2022;387(1):9-20. [doi:10.1056/NEJMoa2203690](https://doi.org/10.1056/NEJMoa2203690) · [PubMed 35665782](https://pubmed.ncbi.nlm.nih.gov/35665782/)

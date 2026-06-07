---
schema: human-scale-entry/v1
id: mlh1
name: MLH1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "MutL homolog 1; forms MutLα heterodimer with PMS2 → mismatch repair (MMR) of replication errors. MLH1 loss → MSI-H phenotype and TMB-high tumors responsive to PD-1 blockade. Germline MLH1 mutations cause Lynch syndrome (colorectal, endometrial, ovarian, gastric cancers)."
aliases: ["MLH1", "MutL homolog 1", "MutLα", "mismatch repair", "MMR", "Lynch syndrome", "MSI-H", "dMMR", "HNPCC", "microsatellite instability"]
sources:
  - id: le-2015-msi-pembrolizumab
    type: peer-reviewed
    cite: "Le DT, Uram JN, Wang H, et al. PD-1 blockade in tumors with mismatch-repair deficiency. N Engl J Med. 2015;372(26):2509-2520."
    doi: "10.1056/NEJMoa1500596"
    pmid: "26028255"
    url: "https://doi.org/10.1056/NEJMoa1500596"
  - id: lynch-2015-lynch-syndrome
    type: peer-reviewed
    cite: "Lynch HT, Snyder CL, Shaw TG, Heinen CD, Hitchins MP. Milestones of Lynch syndrome: 1895-2015. Nat Rev Cancer. 2015;15(3):181-194."
    doi: "10.1038/nrc3878"
    pmid: "25673086"
    url: "https://doi.org/10.1038/nrc3878"
cross_links:
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "MMR-deficient tumors rarely carry TP53 mutations; MSI-H tumors accumulate frameshifts at microsatellites rather than TP53 hotspot mutations; MSI-H and TP53-mutant pathways are divergent CRC carcinogenesis routes; MMR loss cooperates with KRAS in serrated adenoma progression."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "MSI-H/dMMR tumors have high neoantigen load from frameshift mutations → PD-L1 upregulation → T-cell exhaustion; pembrolizumab pan-tumor MSI-H approval (FDA 2017, first tumor-agnostic); nivolumab + ipilimumab active in dMMR CRC; MSI-H is the strongest predictor of ICI response."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Lynch syndrome CRC development follows the microsatellite instability pathway: APC/Wnt activation → KRAS → MLH1/MSH2 loss → frameshift mutations in TGFBR2, BAX, ACVR2A → tumor progression; Wnt pathway mutations are early events in Lynch-associated CRC."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGFBR2 frameshift mutations at poly-A tracts are the prototypical MSI-H target; ~80% of MSI-H CRC carry TGFBR2 frameshift → loss of TGF-β growth suppression → tumor progression despite high TMB; biallelic TGFBR2 frameshift is a hallmark of dMMR CRC."
---

# MLH1

## Overview

**MLH1 (MutL Homolog 1)** is a central component of the **mismatch repair (MMR)** system — the post-replicative proofreading pathway that corrects mismatched base pairs and small insertion-deletion loops (IDLs) that escape DNA polymerase proofreading. MLH1 heterodimerizes with PMS2 to form the **MutLα** complex, which coordinates repair by recruiting downstream endonuclease and exonuclease activities after MutSα (MSH2-MSH6) or MutSβ (MSH2-MSH3) recognizes a mismatch. Loss of MLH1 function — through somatic promoter hypermethylation (sporadic CRC) or germline mutation (Lynch syndrome) — abrogates MMR, leading to **microsatellite instability-high (MSI-H)** tumors with thousands of frameshift mutations at repetitive sequences [^le-2015-msi-pembrolizumab].

**MLH1 in cancer:**
- **Sporadic MSI-H CRC (~15% of CRC):** MLH1 promoter hypermethylation + BRAF V600E → sporadic MSI-H CRC (serrated pathway); not hereditary; poor prognosis compared to Lynch-associated CRC if metastatic
- **Lynch syndrome (germline MLH1 mutation, ~40% of Lynch):** Hereditary colorectal cancer syndrome; also causes endometrial, ovarian, gastric, urothelial, and brain cancers; lifetime CRC risk 40-80% in MLH1 carriers; endometrial cancer risk 40-60% (highest non-colorectal cancer risk in female Lynch carriers)
- **MSI-H tumor-agnostic immunotherapy:** Pembrolizumab FDA approved 2017 for all MSI-H/dMMR solid tumors regardless of histology — first tumor-agnostic cancer drug approval; ORR ~40-50% in dMMR solid tumors [^le-2015-msi-pembrolizumab]

**MMR gene prevalence in Lynch syndrome:**
- MLH1: ~40% of Lynch syndrome families
- MSH2: ~30-40%
- MSH6: ~10-15%
- PMS2: ~5-10%
- EPCAM deletions (MSH2 epigenetic silencing): ~3%

## Structure

### MLH1 protein architecture

MLH1 is a 756-amino-acid, ~85 kDa protein with two functional domains:

**N-terminal ATPase domain (1-336):**
- GHKL ATPase superfamily fold (shared with Hsp90, DNA gyrase B, histidine kinase)
- ATP binding and hydrolysis → conformational change required for MMR activation
- Interacts with MutSα-mismatch complex; ATP hydrolysis drives sliding clamp translocation along DNA
- **Key residue Lys618 (ATPase):** Walker A motif; mutations here abolish ATPase activity and MMR function

**C-terminal dimerization domain (337-756):**
- Forms obligate heterodimer with PMS2 (MutLα) via C-terminal interaction
- Also interacts with MLH3 (MutLγ, for meiotic recombination)
- Contains multiple PCNA-interacting protein (PIP) boxes → recruits PMS2 endonuclease to replication foci
- Nuclear localization signal (NLS) within C-terminal domain

### MMR complex assembly

1. **Mismatch recognition:** MutSα (MSH2-MSH6) recognizes single base mismatches and 1-2 nt IDLs; MutSβ (MSH2-MSH3) recognizes larger IDLs (2-10 nt)
2. **MutLα recruitment:** MutSα·mismatch → recruits MLH1-PMS2 (MutLα) → ternary complex
3. **Endonuclease activation:** PMS2 contains the latent endonuclease (DQHA motif); MutLα activated by RFC-PCNA at hemi-methylated DNA → PMS2 nicks new strand
4. **Excision and resynthesis:** EXO1 degrades nicked strand past mismatch → RPA, PCNA, Polδ → resynthesis

**MLH1 stability:**
- MLH1 requires PMS2 for nuclear stability (and vice versa) — when one MMR protein is lost, its heterodimer partner is often degraded → both appear absent by IHC
- MLH1 loss by methylation or mutation → both MLH1 and PMS2 absent by IHC → interpreted as MLH1 deficiency

## Function

### Normal MMR roles

**Replication fidelity:**
- MMR reduces replication error rate 100-1000-fold; without MMR, mutation rate at microsatellites increases dramatically → MSI
- Microsatellites (short tandem repeats, e.g., (CA)n, poly-A tracts) are especially prone to polymerase slippage → IDLs → require MMR for correction
- MMR-proficient cells maintain microsatellite length; MMR-deficient cells accumulate length heterogeneity → MSI-H phenotype (>30% of tested loci unstable = MSI-H)

**DNA damage response:**
- MLH1-PMS2 also participates in response to alkylating agents (temozolomide, CCNU), 6-thioguanine, cisplatin — recognizes O6-methylguanine:T mismatches → triggers apoptosis rather than repair → MLH1-deficient tumors are resistant to alkylating agents (paradoxical MMR-mediated cytotoxicity)
- MLH1-deficient GBM → temozolomide resistance; mechanism: lack of MLH1-mediated recognition of O6-MG:T → no futile repair cycles → no apoptosis

**Meiotic recombination:**
- MutLγ (MLH1-MLH3) resolves Holliday junctions during meiosis → crossover formation; MLH1 germline loss → meiotic defects (rare human phenotype, mostly studied in mouse)

### Lynch syndrome pathogenesis

**Two-hit model:**
1. Germline MLH1 mutation (inherited one defective allele)
2. Somatic LOH, second MMR mutation, or promoter methylation of wild-type allele → complete MMR loss
3. Rapid accumulation of frameshift mutations at microsatellite targets (TGFBR2, BAX, APC, PTEN, IGF2R, β2-microglobulin) → tumor progression

**Constitutional MLH1 methylation:**
- Rare: germline epigenetic silencing of MLH1 promoter (not mutation) → Lynch-like phenotype; heritable but not Mendelian; treated like Lynch syndrome clinically

## Mechanism

### MSI-H tumor biology

**Neoantigen landscape:**
MSI-H tumors accumulate thousands of frameshift mutations at coding microsatellites → novel neopeptides presented on MHC-I → high neoantigen density → strong TIL infiltration → PD-L1 upregulation as adaptive immune evasion. This explains the exceptional response to PD-1 blockade (pembrolizumab, nivolumab) in dMMR tumors.

**MSI detection methods:**
- **PCR-based MSI testing:** Bethesda panel (5 loci: BAT25, BAT26, D2S123, D5S346, D17S250); MSI-H = ≥2 loci unstable; gold standard
- **IHC for MMR proteins (MLH1, PMS2, MSH2, MSH6):** Loss of nuclear staining = protein absent; MLH1+PMS2 loss → MLH1 deficiency; MSH2+MSH6 loss → MSH2 deficiency; concordance with PCR-MSI ~95%
- **Next-generation sequencing (NGS):** MSI score from tumor sequencing (many platforms); TMB-high (≥10 mut/Mb) partially overlaps MSI-H but not equivalent

**Sporadic MLH1 methylation and BRAF V600E:**
- Sporadic MSI-H CRC: MLH1 promoter methylation + BRAF V600E → right-sided, mucin-rich, poorly differentiated → not Lynch syndrome; BRAF V600E testing + methylation analysis differentiates sporadic vs. Lynch-associated MSI-H CRC

### MMR testing and Lynch syndrome diagnosis

**Universal tumor screening:**
- NCCN/ASCO recommend universal MMR/MSI testing in all newly diagnosed CRC and endometrial cancer
- MLH1-deficient tumors → reflex BRAF V600E + MLH1 methylation → if methylation+BRAF V600E → sporadic; if no methylation → suspect Lynch → germline testing

**Lynch syndrome surveillance:**
- Colonoscopy every 1-2 years (starting age 20-25)
- Risk-reducing hysterectomy + bilateral salpingo-oophorectomy for female Lynch carriers (after childbearing)
- Annual endometrial sampling for Lynch women not pursuing risk-reducing surgery
- Gastric + urothelial cancer surveillance in high-risk families (especially MSH2 carriers)

### Immunotherapy in dMMR tumors

**Pembrolizumab (KEYNOTE-158, -016):** [^le-2015-msi-pembrolizumab]
- FDA approved 2017 for MSI-H/dMMR solid tumors (all histologies, 2nd+ line) — first tumor-agnostic approval
- FDA approved 2020 for 1st-line dMMR CRC (KEYNOTE-177): PFS 16.5 vs. 8.2 months vs. mFOLFOX6/FOLFIRI + bevacizumab/cetuximab
- ORR ~36-45% in unselected dMMR solid tumors; durable CR possible (median DOR not reached)

**Nivolumab + ipilimumab (CheckMate 142):**
- dMMR/MSI-H CRC: ORR 46% (1st-line), 49% (nivolumab+ipi combined); FDA approved 2nd+ line in dMMR CRC

## Connections

- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — MMR-deficient tumors rarely carry TP53 mutations — POLE-ultramutated and MSI-H tumors accumulate frameshifts at microsatellites rather than TP53 hotspot missense mutations; MSI-H and TP53-mutant pathways represent divergent routes of CRC carcinogenesis; MMR loss cooperates with KRAS mutation in serrated adenoma progression.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — MSI-H/dMMR tumors have high neoantigen load from frameshift mutations → PD-L1 upregulation → T-cell exhaustion; pembrolizumab pan-tumor MSI-H approval (FDA 2017, first tumor-agnostic indication); nivolumab + ipilimumab active in dMMR CRC; MSI-H is the strongest predictor of ICI response.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Lynch syndrome CRC development follows the microsatellite instability pathway: APC/Wnt activation → KRAS → MLH1/MSH2 loss (rather than chromosomal instability) → frameshift mutations in TGFBR2, BAX, ACVR2A → tumor progression; Wnt pathway mutations are early events in Lynch-associated CRC.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — TGFBR2 frameshift mutations at poly-A tracts are the prototypical MSI-H target; ~80% of MSI-H CRC have TGFBR2 frameshift → loss of TGF-β growth suppression → tumor progression despite high TMB; TGFBR2 biallelic inactivation by frameshift is a hallmark of mismatch repair deficiency in CRC.

[^le-2015-msi-pembrolizumab]: Le DT, Uram JN, Wang H, et al. PD-1 blockade in tumors with mismatch-repair deficiency. *N Engl J Med.* 2015;372(26):2509-2520. [doi:10.1056/NEJMoa1500596](https://doi.org/10.1056/NEJMoa1500596) · [PubMed 26028255](https://pubmed.ncbi.nlm.nih.gov/26028255/)
[^lynch-2015-lynch-syndrome]: Lynch HT, Snyder CL, Shaw TG, Heinen CD, Hitchins MP. Milestones of Lynch syndrome: 1895-2015. *Nat Rev Cancer.* 2015;15(3):181-194. [doi:10.1038/nrc3878](https://doi.org/10.1038/nrc3878) · [PubMed 25673086](https://pubmed.ncbi.nlm.nih.gov/25673086/)

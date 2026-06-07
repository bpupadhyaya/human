---
schema: human-scale-entry/v1
id: msh2
name: MSH2
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "MSH2 (MutS Homolog 2) forms MutSα (MSH2-MSH6) and MutSβ (MSH2-MSH3) heterodimers for mismatch repair; germline MSH2 mutations cause Lynch syndrome (~31%); MMR LOF → MSI-H → elevated TMB → immunotherapy sensitivity; EPCAM deletions silence MSH2 epigenetically."
aliases: ["MSH2", "MSH2 mutation", "MSH2 Lynch syndrome", "MutSα", "MSH2-MSH6", "dMMR MSH2", "MSH2 IHC", "MMR MSH2", "MSH2 mismatch repair", "MSH2 Lynch cancer"]
sources:
  - id: bonadona-2011-lynch-risks
    type: peer-reviewed
    cite: "Bonadona V, Bonaïti B, Olschwang S, et al. Cancer risks associated with germline mutations in MLH1, MSH2, and MSH6 genes in Lynch syndrome. JAMA. 2011;305(22):2304-2310."
    doi: "10.1001/jama.2011.743"
    pmid: "21642683"
    url: "https://doi.org/10.1001/jama.2011.743"
  - id: lynch-2015-lynch-review
    type: peer-reviewed
    cite: "Lynch HT, Snyder CL, Shaw TG, et al. Milestones of Lynch syndrome: 1895-2015. Nat Rev Cancer. 2015;15(3):181-194."
    doi: "10.1038/nrc3878"
    pmid: "25673086"
    url: "https://doi.org/10.1038/nrc3878"
cross_links:
  - target: 01-human/03-molecular/mlh1
    relation: connects-to
    note: "MSH2 and MLH1 form the core MMR complex; MSH2-MSH6 (MutSα) detects mismatches → recruits MLH1-PMS2 (MutLα) → strand excision; MLH1 LOF and MSH2 LOF both cause Lynch syndrome; dMMR IHC panel includes MLH1, PMS2, MSH2, MSH6 loss patterns"
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "MMR LOF → MSI-H → elevated TMB → PD-L1 upregulation → immunotherapy sensitive tumors; pembrolizumab FDA-approved for dMMR/MSI-H tumors (any histology, tissue-agnostic); dostarlimab for dMMR endometrial cancer; MSH2-deficient Lynch tumors are paradigmatic ICB responders"
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Lynch syndrome is the most common inherited CRC predisposition; lifetime CRC risk with MSH2 germline: ~40-50%; Lynch CRC: proximal colon, mucinous, lymphocytic infiltrate; universal MMR testing of all CRC; MSH2 IHC loss → germline testing"
  - target: 01-human/07-system/endometrial-cancer
    relation: connects-to
    note: "MSH2 germline → Lynch syndrome; endometrial cancer lifetime risk ~40-60%; Lynch endometrial: often MSI-H; dostarlimab FDA-approved for dMMR recurrent endometrial cancer; universal MMR IHC testing of endometrial cancer recommended"
---

# MSH2

## Overview

**MSH2** (MutS Homolog 2) encodes a 934-amino-acid (~104 kDa) DNA mismatch repair (MMR) protein that is the obligate scaffolding partner in two distinct heterodimeric MutS complexes: **MutSα** (MSH2-MSH6), which recognizes single base-base mismatches and small insertion/deletion loops (+1 IDLs), and **MutSβ** (MSH2-MSH3), which recognizes larger insertion/deletion loops (+2 to +8 IDLs). MSH2 is unique in that it is the shared subunit of both complexes; unlike MSH6 or MSH3, MSH2 LOF abrogates both mismatch recognition pathways simultaneously. Germline pathogenic variants in MSH2 account for approximately 31% of Lynch syndrome — the most common hereditary cancer predisposition syndrome in adults — and confer markedly elevated lifetime risks for colorectal, endometrial, ovarian, gastric, and urothelial cancers. Loss of MSH2 function results in deficient MMR (dMMR), microsatellite instability-high (MSI-H) tumors, elevated tumor mutational burden (TMB), and constitutive PD-L1 upregulation — making MSH2-deficient Lynch tumors among the best immunotherapy responders [^bonadona-2011-lynch-risks] [^lynch-2015-lynch-review].

**MSH2-dependent MMR coverage:**

| MutS complex | Subunits | Mismatch substrates recognized |
|---|---|---|
| MutSα | MSH2 + MSH6 | G/T, G/G, A/C, T/C mismatches; +1 IDLs |
| MutSβ | MSH2 + MSH3 | +1 to +8 insertion/deletion loops (IDLs) |
| MutSα specificity | — | Replication errors at coding microsatellites; single base substitutions |
| MutSβ specificity | — | Large IDLs; trinucleotide repeat instability |

**MSH2 in Lynch syndrome vs other MMR genes:**

| Gene | Lynch frequency | Lifetime CRC risk | Lifetime EC risk | Urothelial |
|---|---|---|---|---|
| MLH1 | ~50% | 40-80% | 40-60% | Low |
| MSH2 | ~31% | 40-50% | 40-60% | High (~12%) |
| MSH6 | ~13% | 10-22% | 16-26% | Low |
| PMS2 | ~6% | <15% | <15% | Very low |
| EPCAM (→MSH2 silencing) | ~2% | MSH2-equivalent | MSH2-equivalent | Moderate |

## Structure

### MSH2 protein architecture

**Domain I — mismatch-binding domain (aa 1~1-98):**
Not directly involved in mismatch recognition (this role is primarily MSH6's domain Ia phenylalanine-loop: F432); MSH2 domain I mediates interaction with PCNA; MSH2-MSH6 is recruited to the replication fork via MSH6's N-terminal PCNA-interacting protein box (PIP box: Qxx[I/L/M]xx[F/Y][F/Y])

**Connector domain (domain II) and lever domain (domain III; aa ~300-500):**
Conformational coupling between mismatch binding and ATPase domains; lever domain rotates upon mismatch binding → long-range conformational change → ATP loading at ATPase domain → MSH2-MSH6 adopts sliding clamp conformation; these domains are critical for signal transduction between mismatch recognition and downstream recruitment

**Clamp domain (domain IV; aa ~500-620):**
DNA-encircling clamp domain; MSH2-MSH6 encircles the DNA duplex after mismatch recognition → sliding along DNA → recruits MutLα (MLH1-PMS2); MSH2 clamp domain mediates protein-protein interactions with MLH1 (MutLα recruitment); mutations at the MSH2-MLH1 interface → MMR failure without loss of mismatch binding

**ATPase/NBD domain (domain V; Walker A/B; aa ~620-934):**
Nucleotide-binding domain; Walker A motif (GxxxxGKS/T) + Walker B motif (hhhhD, h = hydrophobic) → ATP hydrolysis; mismatch binding at domain Ia → remote conformational change → ATP binding at MSH2 NBD → MSH2-MSH6 releases mismatch → slides on DNA → recruits MutLα; ATPase activity is required for productive MMR (ATPase-deficient mutants trap MutSα at mismatch, block repair)

### MSH2 mutation patterns

**Germline pathogenic variants in Lynch syndrome:**
- Truncating mutations (frameshift, nonsense): ~55-60% of MSH2 Lynch pathogenic variants; protein absent by IHC
- Missense: ~20-25%; pathogenicity depends on functional domain; G322D, R524P, D603G are well-characterized pathogenic missense variants
- Splice site: ~10-15%; exon skipping or aberrant splicing → truncated protein
- Large genomic rearrangements: ~20% of MSH2 Lynch families; whole-exon deletions/duplications; detected by MLPA or aCGH, not by gene sequencing alone

**EPCAM deletion mechanism:**
3' end deletions in EPCAM (epithelial cell adhesion molecule gene, immediately upstream of MSH2 on chromosome 2p21) → transcriptional read-through from EPCAM into MSH2 → EPCAM-MSH2 fusion transcript → DNA methylation-mediated silencing of MSH2 promoter → MSH2 protein absent; EPCAM deletions account for ~2% of Lynch syndrome families; detected by MLPA; sequencing-based panels miss this mechanism; phenotype identical to MSH2 pathogenic variant; MSH2 IHC shows protein loss

**IHC patterns:**
MSH2 nuclear loss by IHC:
- MSH2 loss + MSH6 loss (concurrent): MSH2 or EPCAM pathogenic variant; MSH6 protein is unstable without its MSH2 partner → both lost together
- MSH2 intact + MSH6 loss alone: MSH6 pathogenic variant or somatic MSH6 mutation
- MLH1 loss + PMS2 loss (concurrent): MLH1 pathogenic variant or MLH1 promoter methylation (sporadic)
- PMS2 loss alone: PMS2 pathogenic variant

## Function

### MSH2-MSH6 (MutSα) mismatch recognition and MMR

**Mismatch recognition:**
MSH6 subunit provides direct mismatch contact via the F432 phenylalanine residue (Phe-loop) that stacks with the mispaired base → bends DNA by ~60° at mismatch; MSH2 contributes scaffold and ATPase function but does not directly contact mismatch; MSH2-MSH6 binds mismatch with KD ~10-100 nM; specificity: MutSα preferentially binds G/T > G/G > A/C base-base mismatches + +1 IDLs at microsatellite sequences

**Sliding clamp and MLH1 recruitment:**
Upon mismatch binding: ATP loading at MSH2 NBD → MutSα conformational change → closed ring (sliding clamp) → releases mismatch → translocates along DNA in ATP-hydrolysis-independent manner; sliding MutSα recruits MutLα (MLH1-PMS2) via MSH2-MLH1 protein-protein interaction → ternary complex (MutSα-MutLα-DNA); PMS2 endonuclease (within MutLα) nicks the newly synthesized strand → ExoI degrades from nick toward mismatch → RPA + PCNA + polδ resynthesize strand → ligation

**Microsatellite instability:**
When MMR is deficient: replication slippage at microsatellite loci (poly-A, dinucleotide, trinucleotide repeats) → insertion/deletion errors not corrected → accumulation of frameshift mutations at microsatellite loci → detectable as MSI by PCR or NGS; Bethesda panel microsatellites: BAT25, BAT26 (mononucleotide repeats), D5S346, D2S123, D17S250 (dinucleotide repeats); MSI-H: ≥2 of 5 markers unstable (classic) or NGS-based classifier

**Mutational consequences of dMMR:**
MSI-H tumors accumulate frameshift mutations in coding microsatellites → neoantigen generation → immunogenic tumors; TMB in MSI-H CRC: ~50-100 mut/Mb (vs ~3-5 in microsatellite stable CRC); PD-L1 upregulated by IFN-γ signaling from tumor-infiltrating lymphocytes → sensitivity to PD-1/PD-L1 blockade [^bonadona-2011-lynch-risks]

## Mechanism

### Therapeutic implications of MSH2 LOF

**Immunotherapy in dMMR/MSI-H tumors:**
- **Pembrolizumab (KEYNOTE-158)**: ORR 36% in dMMR solid tumors across 10 tumor types; FDA-approved June 2020 (tumor-agnostic, first ever tissue-agnostic FDA approval based on molecular biomarker)
- **Nivolumab + ipilimumab (CheckMate 142)**: dMMR metastatic CRC; ORR 55%; mPFS 12.4 months; FDA-approved dMMR/MSI-H CRC first-line
- **Dostarlimab (GARNET trial)**: dMMR recurrent/advanced endometrial cancer; ORR 42.3%; FDA-approved April 2021; RUBY Phase 3: dostarlimab + carboplatin/paclitaxel → PFS HR 0.28 in dMMR endometrial → FDA-approved November 2023 for first-line dMMR endometrial
- **First-line CRC**: KEYNOTE-177 (pembrolizumab vs chemotherapy in dMMR/MSI-H mCRC): mPFS 16.5 vs 8.2 months (HR 0.60); pembrolizumab standard first-line for dMMR mCRC

**Lynch syndrome surveillance and risk reduction:**
- CRC: colonoscopy every 1-2 years from age 25 (MLH1/MSH2/MSH6 carriers); annual from age 20-25 (PMS2: every 2-3 yrs from 30-35)
- Endometrial: annual endometrial biopsy + TVUS from age 30-35; prophylactic hysterectomy + BSO after childbearing complete
- Urothelial (MSH2-specific, highest risk among MMR genes): annual urinalysis + urine cytology from age 25-30

**Aspirin chemoprevention (CAPP2 trial):**
Colorectal Adenoma/Carcinoma Prevention Programme 2: Lynch syndrome patients; aspirin 600 mg/day × 2 years; 10-year follow-up: hazard ratio for CRC 0.63 (non-significant at primary endpoint, then significant at follow-up); aspirin now recommended for Lynch syndrome CRC prevention (mechanism: prostaglandin-mediated MMR modulation and anti-inflammatory effects)

**5-FU resistance in MSI-H tumors:**
MSI-H stage II CRC: 5-FU/leucovorin adjuvant does NOT improve and may harm OS (vs no adjuvant); mechanism: 5-FU requires intact MMR for mismatch-mediated apoptotic signaling; dMMR → 5-FU resistance; for MSI-H stage III CRC: FOLFOX (oxaliplatin + 5-FU) is used (oxaliplatin not MMR-dependent); important clinical decision point for Lynch CRC adjuvant therapy

## Connections

- `connects-to` → **[MLH1](../../03-molecular/mlh1/README.md)** — MSH2 and MLH1 form the core MMR complex; MSH2-MSH6 (MutSα) detects mismatches → recruits MLH1-PMS2 (MutLα) → strand excision; MLH1 LOF and MSH2 LOF both cause Lynch syndrome; dMMR IHC panel includes MLH1, PMS2, MSH2, MSH6 loss patterns
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — MMR LOF → MSI-H → elevated TMB → PD-L1 upregulation → immunotherapy sensitive tumors; pembrolizumab FDA-approved for dMMR/MSI-H tumors (any histology, tissue-agnostic); dostarlimab for dMMR endometrial cancer; MSH2-deficient Lynch tumors are paradigmatic ICB responders
- `connects-to` → **[Colorectal Cancer](../../07-system/colorectal-cancer/README.md)** — Lynch syndrome is the most common inherited CRC predisposition; lifetime CRC risk with MSH2 germline: ~40-50%; Lynch CRC: proximal colon, mucinous, lymphocytic infiltrate; universal MMR testing of all CRC; MSH2 IHC loss → germline testing
- `connects-to` → **[Endometrial Cancer](../../07-system/endometrial-cancer/README.md)** — MSH2 germline → Lynch syndrome; endometrial cancer lifetime risk ~40-60%; Lynch endometrial: often MSI-H; dostarlimab FDA-approved for dMMR recurrent endometrial cancer; universal MMR IHC testing of endometrial cancer recommended

[^bonadona-2011-lynch-risks]: Bonadona V, Bonaïti B, Olschwang S, et al. Cancer risks associated with germline mutations in MLH1, MSH2, and MSH6 genes in Lynch syndrome. *JAMA.* 2011;305(22):2304-2310. [doi:10.1001/jama.2011.743](https://doi.org/10.1001/jama.2011.743) · [PubMed 21642683](https://pubmed.ncbi.nlm.nih.gov/21642683/)
[^lynch-2015-lynch-review]: Lynch HT, Snyder CL, Shaw TG, et al. Milestones of Lynch syndrome: 1895-2015. *Nat Rev Cancer.* 2015;15(3):181-194. [doi:10.1038/nrc3878](https://doi.org/10.1038/nrc3878) · [PubMed 25673086](https://pubmed.ncbi.nlm.nih.gov/25673086/)

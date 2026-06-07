---
schema: human-scale-entry/v1
id: smad4
name: SMAD4
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "SMAD4 is the common-mediator SMAD that bridges TGF-β/BMP-activated R-SMADs (SMAD2/3, SMAD1/5/8) to nuclear transcriptional complexes; LOF → TGF-β cytostatic program lost → tumor progression; germline SMAD4 = juvenile polyposis syndrome; somatic loss in ~55% PDAC and ~15% CRC."
aliases: ["SMAD4", "DPC4", "deleted in pancreatic cancer 4", "SMAD4 tumor suppressor", "SMAD4 co-SMAD", "SMAD4 JPS", "SMAD4 PDAC", "SMAD4 CRC", "18q loss", "common mediator SMAD"]
sources:
  - id: hahn-1996-smad4-dpc4
    type: peer-reviewed
    cite: "Hahn SA, Schutte M, Hoque AT, et al. DPC4, a candidate tumor suppressor gene at human chromosome 18q21.1. Science. 1996;271(5247):350-353."
    doi: "10.1126/science.271.5247.350"
    pmid: "8553070"
    url: "https://doi.org/10.1126/science.271.5247.350"
  - id: howe-1998-smad4-jps
    type: peer-reviewed
    cite: "Howe JR, Roth S, Ringold JC, et al. Mutations in the SMAD4/DPC4 gene in juvenile polyposis. Science. 1998;280(5366):1086-1088."
    doi: "10.1126/science.280.5366.1086"
    pmid: "9582123"
    url: "https://doi.org/10.1126/science.280.5366.1086"
cross_links:
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "SMAD4 is the obligate co-SMAD that forms heterotrimeric complexes with TGF-β-activated SMAD2/3 and BMP-activated SMAD1/5/8; SMAD4 LOF uncouples TGF-β signaling from nuclear transcriptional programs; TGF-β switches from tumor suppressor to tumor promoter when SMAD4 is lost."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "SMAD4 LOF is present in ~15-20% of sporadic CRC; in the Fearon-Vogelstein adenoma-carcinoma sequence, SMAD4/18q LOH occurs late (after KRAS); SMAD4 loss enables TGF-β-driven invasion/EMT; staining loss by IHC predicts poor prognosis in CRC."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "SMAD4 is lost in ~55% of PDAC; SMAD4 IHC loss correlates with systemic metastases rather than local spread; whole-mount pathology studies showed SMAD4-intact PDAC spreads locally, SMAD4-lost PDAC spreads systemically; SMAD4 IHC helps treatment planning."
  - target: 01-human/07-system/juvenile-polyposis-syndrome
    relation: connects-to
    note: "Germline SMAD4 pathogenic variants cause ~20% of JPS cases and a distinct SMAD4-JPS subtype with overlap of hamartomatous polyposis and HHT (telangiectasias, AVMs); BMPR1A germline variants cause another ~25% of JPS; both impair TGF-β/BMP signaling."
---

# SMAD4

## Overview

**SMAD4** (Mothers Against Decapentaplegic Homolog 4; also DPC4 — Deleted in Pancreatic Cancer locus 4) encodes a 552 amino acid (60 kDa) transcription factor that serves as the **common mediator SMAD (co-SMAD)** in the TGF-β superfamily signaling pathway. Unlike receptor-activated SMADs (R-SMADs), SMAD4 is not directly phosphorylated by type I receptors; instead, it forms heterotrimeric complexes with phosphorylated R-SMADs and translocates to the nucleus to activate or repress target gene transcription. SMAD4 is the central bottleneck of TGF-β and BMP signaling — a required partner for both the TGF-β/activin branch (SMAD2/3) and the BMP branch (SMAD1/5/8). SMAD4 was originally cloned as **DPC4**, a tumor suppressor deleted in ~55% of pancreatic ductal adenocarcinomas (PDAC) at chromosome **18q21.1** [^hahn-1996-smad4-dpc4]. Germline SMAD4 pathogenic variants cause **juvenile polyposis syndrome (JPS)**, an autosomal dominant hamartomatous polyposis syndrome [^howe-1998-smad4-jps].

**SMAD4 loss across cancer types:**

| Cancer type | SMAD4 loss frequency | Mechanism/Notes |
|---|---|---|
| Pancreatic ductal adenocarcinoma (PDAC) | ~55% | 18q LOH + somatic point mutation; early event |
| Colorectal cancer (CRC) | ~15-20% | 18q LOH common (~70%); SMAD4 loss in subset |
| Esophageal adenocarcinoma | ~30% | 18q arm loss |
| Cholangiocarcinoma | ~20% | Intrahepatic; co-occurs with IDH1/FGFR2 |
| Small intestinal adenocarcinoma | ~15% | Duodenal/jejunal |
| JPS-associated CRC | ~100% (germline+LOH) | Two-hit model in polyp epithelium |

## Structure

### SMAD4 protein domains

**MH1 domain (aa 1-146):**
- DNA-binding domain; β-hairpin inserts into major groove at **SMAD-binding element (SBE)**: 5'-GTCT-3' / 5'-AGAC-3' palindrome
- Pathway-specific SBE: cooperative binding with SMAD2/3 to SMAD-responsive GC-rich elements and FOXH1
- Intramolecular autoinhibition: MH1 contacts MH2 → keeps SMAD4 inactive in basal state until R-SMAD binding
- Nuclear localization signal (β4α3 region): constitutive nuclear import; SMAD4 shuttles continuously but accumulates in nucleus only after R-SMAD complex formation

**Linker region (aa 147-270):**
- Flexible; contains multiple phosphorylation sites (CDK8/9 at Thr277; ERK at Ser246)
- Ubiquitin ligase binding: WWP1/ITCH E3 ligase binds linker PY motif (Pro-Pro-X-Tyr) → SMAD4 ubiquitination → proteasomal degradation; tumor suppressor-opposing pathway
- SAD (SMAD activation domain): within linker; required for transactivation of some targets

**MH2 domain (aa 271-552):**
- Protein-protein interaction domain; L3 loop binds phosphorylated SSXS motif of R-SMADs (Thr324 and Ser325 in R-SMAD)
- Trimerization: MH2 domain forms symmetric β-barrel; two R-SMAD MH2 + one SMAD4 MH2 = functional heterotrimer in crystal structures
- Co-activator recruitment: MH2 binds CBP/p300 histone acetyltransferases → H3K27ac at target promoters
- Exon 8/9 tumor mutations: R361C/H/S, G386D, R409H — hotspot missense variants in MH2 that disrupt heterotrimer formation without abolishing protein expression (dominant negative in some contexts)

**Tumor-associated SMAD4 variants:**
- **Truncating** (frame-shift, nonsense): ~40% of somatic mutations; protein absent → pure LOF
- **Missense in MH2** (R361, G386, R409): ~30% of somatic mutations; disrupt R-SMAD binding or nuclear complex stability
- **Splice site**: ~15%; exon skipping → truncated/unstable protein
- **Large genomic deletions (18q)**: LOH (~55% PDAC); detected by SNP array or CGH

## Function

### TGF-β/SMAD4 canonical pathway

**Signaling sequence:**
1. TGF-β ligand binds TGFBR2 (type II receptor serine/threonine kinase) → recruits and phosphorylates TGFBR1 (ALK5) Gly-Ser box
2. Activated TGFBR1 phosphorylates **SMAD2** or **SMAD3** at C-terminal SSXS motif (Ser465/Ser467 on SMAD2; Ser423/Ser425 on SMAD3)
3. pSMAD2/3 release from SARA (SMAD anchor for receptor activation) → bind SMAD4 MH2 → form heterotrimers (2× R-SMAD + 1× SMAD4)
4. Nuclear import → bind SBE and cooperate with FOXH1, SP1, AP-1 → transcription of **TGF-β target genes**

**Tumor suppressor outputs (TGF-β cytostatic program):**
- **CDKN1A (p21/CIP1)** and **CDKN2B (p15/INK4B)**: SMAD3-SMAD4 complex → SP1 → p21/p15 transcription → CDK2/CDK4-6 inhibition → G1 arrest
- **c-Myc repression**: SMAD3-SMAD4 recruit E2F4/5-p107-DP1 co-repressor → c-Myc promoter → transcriptional repression → cell cycle exit
- **ID proteins**: BMP-SMAD1/5/8-SMAD4 repress ID1/ID3 in epithelial differentiation contexts

**Tumor promoting outputs when R-SMAD signaling continues without SMAD4:**
When SMAD4 is lost, TGF-β/activin signals can still activate non-canonical pathways (PI3K, MAPK, TRAF4-TAK1) without transcriptional restriction. Additionally, SMAD2/3 without SMAD4 can activate partial programs promoting EMT and invasion via SNAI1/TWIST1 but cannot activate p15/p21 programs → "TGF-β paradox": cytostatic program lost, pro-metastatic program retained.

### BMP/SMAD4 signaling in intestinal homeostasis

BMPs are secreted by the intestinal mesenchyme to suppress proliferation of crypt stem cells via SMAD1/5/8-SMAD4 → p21 → stem cell quiescence. SMAD4 LOF in intestinal epithelium → loss of BMP-mediated crypt suppression → hamartomatous polyp formation (JPS); stroma-derived BMP signals cannot reach epithelial SMAD4 → epithelial proliferation unchecked → juvenile polyps. This explains why JPS polyps are hamartomas (stromal overgrowth + epithelial proliferation) rather than purely adenomatous (epithelial dysplasia only).

## Mechanism

### SMAD4 as tumor suppressor gatekeeper in PDAC

In PDAC development, SMAD4 loss is a key progression event. The PDAC driver sequence (Kras → CDKN2A → TP53 → SMAD4) has SMAD4 as the last major hit, associated with transition from in-situ PanIN-3 to invasive PDAC in some genetic studies. SMAD4 IHC loss by immunohistochemistry identifies ~55% of PDAC and has clinical implications:

**SMAD4 IHC in clinical PDAC practice:**
- Performed on core biopsy or resection specimen
- SMAD4 loss (negative IHC) → correlates with **systemic metastatic spread pattern** at autopsy (Iacobuzio-Donahue 2009): SMAD4-null PDAC → widespread peritoneal + distant organ metastases; SMAD4-intact PDAC → locally destructive, locoregional spread
- Implication: SMAD4-null PDAC → systemic chemotherapy may benefit more than upfront surgery; SMAD4-intact → chemo-radiation + surgery may be preferable
- No approved targeted therapy for SMAD4-lost PDAC as of 2026; TGF-β pathway inhibition (galunisertib) + gemcitabine showed modest benefit in SMAD4-intact PDAC (SMAD4 needed for TGF-β response)

### SMAD4 germline and JPS

Germline SMAD4 pathogenic variants follow a two-hit model in JPS polyps, with LOH at 18q21 as somatic second hit. De novo SMAD4 mutations occur in ~25% of JPS cases. Germline testing distinguishes SMAD4-JPS (broader phenotype including HHT features) from BMPR1A-JPS (pure polyposis phenotype):
- **SMAD4 germline**: ~20% of JPS; associated with concurrent **SMAD4-HHT overlap**: telangiectasias (mucocutaneous), pulmonary AVMs, hepatic AVMs, cerebral AVMs — identical to HHT1/2 features; requires cardiopulmonary vascular surveillance
- **BMPR1A germline**: ~25% of JPS; BMP type I receptor LOF; no HHT features; Cowden-like features in some families
- **No known germline mutation**: ~55% of clinical JPS; may have BMPR1A large deletions, PTEN variants, or yet-unidentified genes

## Connections

- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — SMAD4 is the obligate co-SMAD that forms heterotrimeric complexes with TGF-β-activated SMAD2/3 and BMP-activated SMAD1/5/8; SMAD4 LOF uncouples TGF-β signaling from nuclear transcriptional programs; TGF-β switches from tumor suppressor to tumor promoter when SMAD4 is lost.
- `connects-to` → **[Colorectal Cancer](../../07-system/colorectal-cancer/README.md)** — SMAD4 LOF is present in ~15-20% of sporadic CRC; in the Fearon-Vogelstein adenoma-carcinoma sequence, SMAD4/18q LOH occurs late (after KRAS); SMAD4 loss enables TGF-β-driven invasion/EMT; staining loss by IHC predicts poor prognosis in CRC.
- `connects-to` → **[Pancreatic Cancer](../../07-system/pancreatic-cancer/README.md)** — SMAD4 is lost in ~55% of PDAC; SMAD4 IHC loss correlates with systemic metastases rather than local spread; whole-mount pathology studies showed SMAD4-intact PDAC spreads locally, SMAD4-lost PDAC spreads systemically; SMAD4 IHC helps treatment planning.
- `connects-to` → **[Juvenile Polyposis Syndrome](../../07-system/juvenile-polyposis-syndrome/README.md)** — Germline SMAD4 pathogenic variants cause ~20% of JPS cases and a distinct SMAD4-JPS subtype with overlap of hamartomatous polyposis and HHT (telangiectasias, AVMs); BMPR1A germline variants cause another ~25% of JPS; both impair TGF-β/BMP signaling.

[^hahn-1996-smad4-dpc4]: Hahn SA, Schutte M, Hoque AT, et al. DPC4, a candidate tumor suppressor gene at human chromosome 18q21.1. *Science.* 1996;271(5247):350-353. [doi:10.1126/science.271.5247.350](https://doi.org/10.1126/science.271.5247.350) · [PubMed 8553070](https://pubmed.ncbi.nlm.nih.gov/8553070/)
[^howe-1998-smad4-jps]: Howe JR, Roth S, Ringold JC, et al. Mutations in the SMAD4/DPC4 gene in juvenile polyposis. *Science.* 1998;280(5366):1086-1088. [doi:10.1126/science.280.5366.1086](https://doi.org/10.1126/science.280.5366.1086) · [PubMed 9582123](https://pubmed.ncbi.nlm.nih.gov/9582123/)

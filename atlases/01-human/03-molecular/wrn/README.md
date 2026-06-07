---
schema: human-scale-entry/v1
id: wrn
name: WRN
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "WRN is a RecQ family 3'→5' helicase/exonuclease that resolves G-quadruplex DNA and stalled replication forks; WRN maintains telomere stability; biallelic WRN LOF = Werner syndrome — premature aging with early cataracts, sarcomas, diabetes, and accelerated atherosclerosis."
aliases: ["WRN", "Werner syndrome helicase", "WRN helicase", "WRN RecQ helicase", "WRN exonuclease", "RECQL2", "Werner syndrome gene", "WRN DNA repair", "WRN telomere"]
sources:
  - id: yu-1996-wrn
    type: peer-reviewed
    cite: "Yu CE, Oshima J, Fu YH, et al. Positional cloning of the Werner's syndrome gene. Science. 1996;272(5259):258-262."
    doi: "10.1126/science.272.5259.258"
    pmid: "8602509"
    url: "https://doi.org/10.1126/science.272.5259.258"
  - id: lauper-2013-wrn-neoplasia
    type: peer-reviewed
    cite: "Lauper JM, Krause A, Vaughan TL, Monnat RJ Jr. Spectrum and risk of neoplasia in Werner syndrome: a systematic review. PLoS One. 2013;8(4):e59709."
    doi: "10.1371/journal.pone.0059709"
    pmid: "23579047"
    url: "https://doi.org/10.1371/journal.pone.0059709"
cross_links:
  - target: 01-human/07-system/werner-syndrome
    relation: connects-to
    note: "Biallelic WRN LOF causes Werner syndrome via unchecked G-quadruplex accumulation, replication fork collapse, and telomere attrition; premature aging features appear in the 3rd decade; cancer risk predominantly mesenchymal (sarcomas); median survival ~47 years."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "WRN co-localizes with TERT at telomeres in S-phase; WRN resolves G-quadruplex structures in the G-rich telomeric repeat (TTAGGG) that would impede TERT-mediated elongation; WRN LOF → telomere shortening → replicative senescence → accelerated aging phenotype in Werner syndrome."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "WRN LOF → persistent replication stress → ATM/ATR activation → CHK1/CHK2 → p53 phosphorylation → p21 induction → premature senescence in Werner syndrome fibroblasts; p53-dependent senescence drives the aging phenotype; Werner cells have elevated p53 activity at baseline."
  - target: 01-human/03-molecular/brca2
    relation: connects-to
    note: "WRN and BRCA2 cooperate at stalled replication forks to protect nascent strand DNA from MRE11-mediated degradation; both are required for fork protection and template switching; Werner cells and BRCA2-deficient cells share fork protection defects and genome instability."
---

# WRN

## Overview

**WRN** (Werner Syndrome, RecQ Helicase-like; also RECQL2) is a 1,432 amino acid (162 kDa) member of the **RecQ family of 3'→5' DNA helicases** — a conserved group of ATP-dependent DNA unwinding enzymes that maintain genome stability by resolving unusual DNA secondary structures (G-quadruplexes, holiday junctions, D-loops, replication fork structures) during DNA replication, recombination, and repair. WRN is unique among human RecQ helicases in possessing both **3'→5' helicase activity** and an **intrinsic 3'→5' exonuclease activity** (in the N-terminal domain), making it capable of both unwinding and nucleolytic processing of DNA substrates. WRN localizes primarily to the nucleolus (during S-phase) and to replication forks and telomeres, where it collaborates with RPA, FEN1, DNA polymerase δ, PCNA, BLM, and TERT. Biallelic loss-of-function mutations in WRN cause **Werner syndrome (WS)** — an autosomal recessive progeroid (premature aging) syndrome characterized by early-onset bilateral cataracts, scleroderma-like skin, gray hair and hair loss, type 2 diabetes, dyslipidemia, atherosclerosis, and a distinctive spectrum of mesenchymal cancers (sarcomas, meningiomas, melanoma) with reduced carcinoma risk. WRN was positionally cloned by Yu et al. in 1996 [^yu-1996-wrn] [^lauper-2013-wrn-neoplasia].

**RecQ helicase family — human members:**

| Gene | Protein | Size | Primary function | LOF Syndrome |
|---|---|---|---|---|
| RECQL | RecQL | 649 aa | Fork regression | No Mendelian syndrome identified |
| BLM | Bloom helicase | 1417 aa | HR regulation, fork restart | Bloom syndrome (autosomal recessive) |
| WRN | Werner helicase | 1432 aa | Fork protection, telomere, G4 | Werner syndrome (autosomal recessive) |
| RECQL4 | RecQL4 | 1208 aa | Replication origin firing | Rothmund-Thomson syndrome |
| RECQL5 | RecQL5 | 991 aa | Transcription-replication conflict | No clinical syndrome |

## Structure

### WRN protein domains

**N-terminal 3'→5' exonuclease domain (aa 1-333):**
- RNase H superfamily fold; DExDc/HELICc-proximal exonuclease; contains catalytic Asp/Glu residues coordinating Mg²⁺ ions; degrades single-stranded DNA (ssDNA) and the non-template strand of partial duplexes
- Also possesses limited RNA:DNA degradation activity; important for Okazaki fragment processing (in concert with FEN1 and DNA pol δ) and for degrading aberrant RNA:DNA hybrids (R-loops) at telomeres and rDNA
- Exonuclease domain mutations: frameshifts/nonsense in Werner syndrome most commonly affect helicase or C-terminal regions; but exonuclease-specific point mutations can uncouple the two activities and demonstrate their distinct roles

**Helicase core (aa 548-859; ATPase and translocation):**
- Seven RecA-like motifs (I, Ia, II, III, IV, V, VI) — conserved across all DNA/RNA helicases; Motif I and II (Walker A and B boxes) coordinate ATP hydrolysis
- WRN is a 3'→5' helicase (translocates along the 3' overhang strand, displacing the complementary strand); can unwind standard B-form DNA duplexes and specialized structures:
  - G-quadruplex DNA (G4): key WRN substrate; G-rich sequences (TTAGGG telomere repeats, G-rich promoters, rDNA G-runs) form stable G4 structures; WRN unwinds G4 → allows replication/transcription through these regions
  - Holliday junctions: branch migration (with BLM, RuvBL1/2)
  - D-loops: resolution of displacement loops (critical for homologous recombination control)
  - Forked duplexes, three-way forks: replication fork regression intermediates

**Winged-helix domain (WHD; aa 860-940):**
- DNA binding; mediates interaction with the WRN nuclear localization signal (NLS) and with other protein partners including p53 (N-terminal of p53 interacts with WRN WHD); WRN-p53 interaction inhibits WRN exonuclease → may prevent excessive degradation of DNA under p53 checkpoint activation

**HRDC domain (Helicase-and-RNase-D C-terminal; aa 940-1060):**
- Auxiliary DNA-binding domain; structural similarity to RNase D's C-terminal; in WRN, HRDC mediates specific binding to bubbled DNA and fork structures; also important for inter-domain communication and helicase processivity; HRDC mutations can abrogate helicase function even when ATPase is intact

**Nuclear localization signal (NLS; aa 1370-1432):**
- Bipartite NLS at the extreme C-terminus; recognized by importin-α; mutations in this NLS → cytoplasmic WRN → loss of nuclear function → Werner syndrome; NLS-defective WRN behaves as null in functional assays
- Nucleolar localization signal overlaps with NLS; WRN accumulates in nucleoli (rDNA-containing compartment) during G1 and S-phase for rDNA replication support; redistributes to replication forks (via PCNA interaction) under replication stress

### WRN protein interactions

**Key interaction partners:**
- **RPA (Replication Protein A)**: stabilizes WRN at ssDNA; essential for WRN helicase processivity; WRN-RPA co-unwinds G4 substrates
- **FEN1 (Flap Endonuclease 1)**: cleaves Okazaki fragment 5' flaps; WRN and FEN1 functionally interact on lagging strand during normal replication; WRN stimulates FEN1 flap cleavage
- **DNA polymerase δ (pol δ)**: WRN-pol δ interact at replication forks; WRN re-primes stalled forks; WRN helps maintain template for pol δ re-extension after fork regression
- **PCNA**: WRN interacts with PCNA via PIP box; recruited to replication forks and repair sites
- **TERT/telomerase holoenzyme**: co-localizes at telomeres during S-phase; WRN resolves G4 structures in telomeric repeat sequences that would block TERT access; required for complete telomere replication by TERT
- **BLM**: WRN and BLM functionally cooperate on Holliday junction dissolution (with topoisomerase IIIα and RMI1/2); compensatory; WRN and BLM have partially overlapping G4 helicase substrates
- **p53 (TP53)**: WRN-p53 physical interaction; p53 Ser15-phosphorylated form has altered affinity for WRN; p53 inhibits WRN exonuclease after DNA damage (checkpoint); WRN promotes p53 transcriptional activity at certain promoters (WRN-p53 co-regulation of gene expression)
- **BRCA2/RAD51**: WRN participates in fork protection at stalled forks; BRCA2 protects nascent strands from MRE11; WRN provides separate protection of the fork (exonuclease activity and structural stabilization)

## Function

### WRN at replication forks

**Normal S-phase role:**
1. WRN is recruited to stalled replication forks (by RPA, PCNA, Rad6 signaling)
2. At stalled forks: WRN helicase unwinds G4 structures and recessed fork structures that impede replicative polymerases
3. WRN facilitates fork regression (conversion of stalled fork to 4-way junction) — protective pathway that allows repair before restart
4. WRN exonuclease degrades aberrant ssDNA flaps at the fork — prevents nucleolytic collapse
5. WRN promotes template switching (recombination-mediated fork rescue via BLM, POLD3)

**Fork protection (critical function):**
- WRN protects nascent DNA at stalled forks from MRE11/DNA2 nucleolytic degradation; this "fork protection" function is shared with BRCA1/BRCA2, FANCD2, RADX
- WRN LOF → unprotected stalled forks → excessive degradation → chromosomal instability → abnormal chromosomal structures (large deletions, translocations)
- In Werner syndrome fibroblasts: elevated sister chromatid exchanges (SCE — like Bloom syndrome, but fewer), chromosomal rearrangements, large deletions; hallmark of WRN deficiency in somatic cells

### WRN at telomeres

**Telomere maintenance:**
- Telomeres = TTAGGG repeats (5-15 kb in humans) ending in a 3' G-overhang → forms T-loop (protective structure) and G-quadruplex (G4) at the 3' overhang
- During S-phase: the telomere G-overhang is replicated by lagging strand synthesis → requires G4 unwinding before replication fork can proceed; WRN is the primary helicase that resolves G4 at telomeres in S-phase
- WRN co-localizes with TERT (telomerase), TRF1, TRF2 (shelterin components) at telomeres; WRN-TRF2 interaction is required for WRN recruitment
- WRN LOF → G4 persists at telomeres → replication fork stalls → telomere truncation or loss → critically short or absent telomeres → replicative senescence in Werner syndrome cells

**Telomere phenotype in Werner syndrome:**
- Werner syndrome cells exhibit ~3-fold accelerated telomere shortening per population doubling vs normal fibroblasts
- Critically short telomeres → ATM/ATR activation → p53 → p21 → irreversible growth arrest (replicative senescence)
- Werner syndrome fibroblasts senesce after ~20 population doublings vs ~60 for normal fibroblasts — quantitative measure of accelerated aging
- Proposed therapy: TERT overexpression in Werner fibroblasts rescues proliferation defect in vitro; clinical relevance limited (cancer risk concern from TERT activation)

### WRN and G-quadruplex biology

**G-quadruplex (G4) structures:**
- G4 = four G-rich strands folded into a planar tetrad stabilized by Hoogsteen base pairing and a central monovalent cation (K⁺ or Na⁺); multiple tetrads stack → highly stable G4 structure
- G4-forming sequences are enriched at: telomeres (TTAGGG), oncogene promoters (MYC, VEGF, KRAS), rDNA, immunoglobulin switch regions, common fragile sites
- WRN is one of the most effective G4 helicases among human RecQ proteins; WRN ATPase-driven strand separation of G4 requires Mg²⁺ and ssDNA flanking the G4

**WRN LOF → G4 accumulation:**
- G4 structures accumulate in Werner syndrome cells (shown by G4-binding antibody BG4 in fluorescence microscopy)
- G4 at replication forks: stalls fork → MRE11 degradation or fork collapse → double-strand breaks → chromosomal instability
- G4 at telomeres: prevents telomere replication as described above
- G4 at rDNA: WRN is required for efficient rDNA replication (nucleolus has highest WRN concentration); rDNA replication defects → reduced ribosome biogenesis → reduced protein synthesis → metabolic aging phenotype

## Mechanism

### WRN loss and Werner syndrome pathogenesis

**Werner syndrome mutation spectrum:**
- All known disease-causing WRN mutations result in loss of the nuclear localization signal (NLS) or produce truncated proteins lacking the C-terminal NLS → cytoplasmic WRN → no nuclear function
- This is a unifying feature: even missense mutations within functional domains are rare causes; NLS-disabling truncations predominate
- Most WRN variants found in Japanese Werner syndrome patients (~5,500 WS patients worldwide, ~1,400 confirmed Japanese patients): 8-bp deletion at intron 25/exon 26 boundary is the most common Japanese founder mutation
- Autosomal recessive: both alleles must be affected; heterozygous carriers: no Werner syndrome phenotype; population carrier frequency ~1/150-200 in Japan; ~1/1000 globally

**Molecular basis of accelerated aging:**
1. WRN LOF → G4 accumulation at rDNA, telomeres, common fragile sites, oncogene promoters
2. G4-induced replication fork stalling → chromosomal instability → large-scale genomic changes (deletions, translocations)
3. Telomere attrition → ATM/ATR → CHK2/CHK1 → p53/p21 → irreversible G1/S senescence in normal Werner cells
4. Senescent Werner cells accumulate inflammatory cytokines (SASP — senescence-associated secretory phenotype): IL-1β, IL-6, TNF-α, MMP3 → chronic low-grade inflammation → accelerated tissue aging
5. WRN LOF in stem cell populations (mesenchymal stem cells, adipose precursors) → premature senescence of stem cells → impaired tissue renewal → progeroid phenotype

**Cancer spectrum in Werner syndrome (distinctive):**
- Elevated mesenchymal tumor risk: osteosarcoma, fibrosarcoma, malignant fibrous histiocytoma, soft tissue sarcomas (~25% of all WS cancers)
- Thyroid carcinoma (~13% of WS cancers)
- Melanoma, meningioma, leukemia
- Notably REDUCED carcinoma (epithelial cancer) risk vs general population — opposite of most cancer predisposition syndromes
- Explanation: Werner syndrome cells accumulate chromosomal rearrangements (mesenchymal transformation pathway) rather than point mutations (carcinoma pathway); the type of genomic instability determines cancer type

**Metabolic features — premature aging phenotype:**
- Type 2 diabetes (~72-90% of Werner syndrome patients by 40 years): central lipodystrophy (redistribution of fat from extremities to central depots) → insulin resistance → T2DM; not due to pancreatic β-cell loss (islets are preserved early); managed as T2DM
- Dyslipidemia: hypertriglyceridemia, low HDL; accelerated atherosclerosis
- Atherosclerosis: mean age of first MI or stroke ~39 years; leading cause of death in WS (cardiovascular disease causes ~50% of deaths, cancer ~30%)
- Osteoporosis: bone loss prominent; vertebral fractures from osteoporosis; WRN-deficient osteoblasts senesce prematurely → reduced bone formation

**Therapeutic approaches:**
- No disease-modifying therapy approved for Werner syndrome
- NAD⁺ precursors (NMN, NR): replenish NAD⁺ → restore PARP1/SIRT1/SIRT6 activity → reduce SASP; Werner cells and WRN-knockout mice show NAD⁺ depletion; NMN improves Werner mouse phenotype (preclinical)
- Rapamycin (mTORC1 inhibitor): suppresses SASP; extends lifespan in other progeroid models; clinical trials under consideration for Werner syndrome
- Metformin: activates AMPK → reduces mTOR → reduces SASP; rational in WS (also treats T2DM which is nearly universal)
- Statin + antiplatelet: for cardiovascular risk reduction
- Annual cancer surveillance: dermatology (melanoma), musculoskeletal imaging (sarcoma surveillance), thyroid ultrasound

## Connections

- `connects-to` → **[Werner Syndrome](../../07-system/werner-syndrome/README.md)** — Biallelic WRN LOF causes Werner syndrome via unchecked G-quadruplex accumulation, replication fork collapse, and telomere attrition; premature aging features appear in the 3rd decade; cancer risk predominantly mesenchymal (sarcomas); median survival ~47 years.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — WRN co-localizes with TERT at telomeres in S-phase; WRN resolves G-quadruplex structures in the G-rich telomeric repeat (TTAGGG) that would impede TERT-mediated elongation; WRN LOF → telomere shortening → replicative senescence → accelerated aging phenotype in Werner syndrome.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — WRN LOF → persistent replication stress → ATM/ATR activation → CHK1/CHK2 → p53 phosphorylation → p21 induction → premature senescence in Werner syndrome fibroblasts; p53-dependent senescence drives the aging phenotype; Werner cells have elevated p53 activity at baseline.
- `connects-to` → **[BRCA2](../../03-molecular/brca2/README.md)** — WRN and BRCA2 cooperate at stalled replication forks to protect nascent strand DNA from MRE11-mediated degradation; both are required for fork protection and template switching; Werner cells and BRCA2-deficient cells share fork protection defects and genome instability.

[^yu-1996-wrn]: Yu CE, Oshima J, Fu YH, et al. Positional cloning of the Werner's syndrome gene. *Science.* 1996;272(5259):258-262. [doi:10.1126/science.272.5259.258](https://doi.org/10.1126/science.272.5259.258) · [PubMed 8602509](https://pubmed.ncbi.nlm.nih.gov/8602509/)
[^lauper-2013-wrn-neoplasia]: Lauper JM, Krause A, Vaughan TL, Monnat RJ Jr. Spectrum and risk of neoplasia in Werner syndrome: a systematic review. *PLoS One.* 2013;8(4):e59709. [doi:10.1371/journal.pone.0059709](https://doi.org/10.1371/journal.pone.0059709) · [PubMed 23579047](https://pubmed.ncbi.nlm.nih.gov/23579047/)

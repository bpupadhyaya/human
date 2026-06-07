---
schema: human-scale-entry/v1
id: recql4
name: RECQL4
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "RECQL4 is a RecQ helicase that initiates DNA replication by recruiting the CMG complex and maintains mitochondrial DNA integrity; biallelic RECQL4 LOF → Rothmund-Thomson syndrome — poikiloderma, skeletal defects, and ~30% osteosarcoma risk; SCE is NOT elevated."
aliases: ["RECQL4", "RecQL4 helicase", "RECQL4 helicase", "Rothmund-Thomson RECQL4", "RECQL4 osteosarcoma", "RECQL4 Rapadilino", "RECQL4 Baller-Gerold", "RECQL4 replication", "RecQ4"]
sources:
  - id: kitao-1999-recql4-rts
    type: peer-reviewed
    cite: "Kitao S, Shimamoto A, Goto M, et al. Mutations in RECQL4 cause a subset of cases of Rothmund-Thomson syndrome. Nat Genet. 1999;22(1):82-84."
    doi: "10.1038/8788"
    pmid: "10319867"
    url: "https://doi.org/10.1038/8788"
  - id: sangrithi-2005-recql4-replication
    type: peer-reviewed
    cite: "Sangrithi MN, Bernal JA, Madine M, et al. Initiation of DNA replication requires the RECQL4 protein mutated in Rothmund-Thomson syndrome. Cell. 2005;121(6):887-898."
    doi: "10.1016/j.cell.2005.05.015"
    pmid: "15960976"
    url: "https://doi.org/10.1016/j.cell.2005.05.015"
cross_links:
  - target: 01-human/07-system/rothmund-thomson
    relation: connects-to
    note: "Biallelic RECQL4 LOF → Rothmund-Thomson syndrome; RECQL4 loss impairs replication initiation (CMG loading) and mitochondrial DNA repair; poikiloderma, skeletal defects (radial ray), juvenile cataracts, and ~30% lifetime osteosarcoma risk; SCE is not elevated."
  - target: 01-human/03-molecular/wrn
    relation: connects-to
    note: "RECQL4 and WRN are both RecQ helicases with distinct mechanisms: WRN has exonuclease activity and resolves G-quadruplex structures; RECQL4 initiates DNA replication via CMG complex; WRN LOF → Werner syndrome (progeroid, sarcomas); RECQL4 LOF → Rothmund-Thomson (osteosarcoma)."
  - target: 01-human/03-molecular/blm
    relation: connects-to
    note: "RECQL4 and BLM are both RecQ helicases: BLM dissolves Holliday junctions and suppresses crossover (SCE ~10x elevated in BLM LOF); RECQL4 initiates replication; both cause cancer predisposition — BLM LOF pan-cancer, RECQL4 LOF predominantly osteosarcoma."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "RECQL4 and p53 interact at replication origins during S-phase; p53-mediated transcription of p21 and RECQL4 both suppress aberrant replication; osteosarcoma (the hallmark cancer of Rothmund-Thomson syndrome) also occurs in Li-Fraumeni syndrome (TP53 germline LOF)."
---

# RECQL4

## Overview

**RECQL4** (RecQ-like helicase 4; also RECQ4) is a 1,208 amino acid (133 kDa) member of the **RecQ family of 3'→5' DNA helicases** with a unique dual role: unlike BLM (which dissolves Holliday junctions) or WRN (which resolves G-quadruplexes at stalled forks), RECQL4 functions primarily in **DNA replication initiation** — its N-terminal domain is structurally homologous to yeast Sld2 and Drosophila Recql4, which are essential for loading the CMG (CDC45-MCM2-7-GINS) helicase complex onto DNA origins, licensing replication initiation. This replication function is distinct from any other RecQ helicase in humans. RECQL4 also participates in **base excision repair (BER)** and maintains **mitochondrial DNA (mtDNA) integrity** via a fraction of RECQL4 that localizes to mitochondria. Unlike BLM and WRN, **RECQL4 LOF does NOT cause elevated sister chromatid exchanges (SCE)** — a key distinguishing feature in clinical cytogenetic diagnosis.

Biallelic germline RECQL4 mutations cause three overlapping autosomal recessive syndromes: **Rothmund-Thomson syndrome (RTS)**, **RAPADILINO syndrome**, and **Baller-Gerold syndrome** — collectively distinguished by skin, skeletal, and cancer features. RECQL4 mutations in RTS type II (the classic form with osteosarcoma risk) are LOF mutations in the helicase core; ~30% of RTS type II patients develop osteosarcoma, making RECQL4 one of the most specific cancer-predisposition genes for osteosarcoma. The gene was cloned as a RecQ helicase in 1998 and first connected to RTS by Kitao et al. in 1999 [^kitao-1999-recql4-rts]; its replication initiation function was established by Sangrithi et al. in 2005 [^sangrithi-2005-recql4-replication].

**RECQL4 vs. other RecQ helicases:**

| Gene | Clinical Syndrome | Primary function | SCE | Cancer risk |
|---|---|---|---|---|
| RECQL4 | Rothmund-Thomson, Rapadilino, Baller-Gerold | Replication initiation (CMG loading) | Not elevated | Osteosarcoma (~30%) |
| BLM | Bloom syndrome | dHJ dissolution, crossover suppression | ~10x elevated | Pan-cancer |
| WRN | Werner syndrome | G4 unwinding, fork protection, exonuclease | ~2-3x elevated | Sarcomas, melanoma, thyroid |

## Structure

### RECQL4 protein domains

**N-terminal Sld2-homology domain (aa 1-~400):**
- Structural homolog of yeast Sld2 (essential replication initiation factor) and Drosophila Recql4; no helicase activity in this domain
- **Replication initiation function**: interacts with Sld3 (human analog: TopBP1/TOPBP1-interacting scaffold proteins) and with GINS subunits → required for CMG helicase complex assembly on pre-replication complexes (pre-RCs) at origins
- Sangrithi et al. (2005) demonstrated in Xenopus egg extracts that immunodepletion of RECQL4 (but not of other RecQ helicases) abolishes DNA replication initiation; add-back rescues replication
- **p53 interaction site**: RECQL4 N-terminal domain interacts with p53 at replication origins; p53 modulates origin firing via this interaction; RECQL4 overexpression promotes p53 ubiquitination in some contexts
- Contains multiple CDK phosphorylation sites (S89, S251); CDK2-mediated phosphorylation in late G1 → triggers CMG loading and origin firing

**Intrinsically disordered linker (aa ~400-455):**
- Connects Sld2-homology domain to helicase core; contains protein interaction sites (RPA70, Rad51); flexible; not structurally resolved
- Contains nuclear export signal and mitochondrial targeting sequence — competing localization signals; RECQL4 distribution is cell cycle-regulated

**Helicase core (aa 455-1,048):**
- Seven RecA-like motifs (Walker A/B + RecQ-specific motifs); 3'→5' directional translocation on ssDNA; unwinds duplex DNA, G-quadruplexes, D-loops, flaps
- **No HRDC domain** (distinguishes RECQL4 from BLM and WRN, which both have C-terminal HRDC domains); absence of HRDC reduces substrate specificity for Holliday junctions specifically — consistent with RECQL4 not functioning in dHJ dissolution
- RECQL4 helicase is less processive than BLM; unwinding activity requires forked substrates or G-overhangs; cannot efficiently unwind long duplexes without accessory factors

**C-terminal domain (aa 1,048-1,208):**
- Interacts with PARP1 (poly(ADP-ribose) polymerase 1): RECQL4-PARP1 interaction promotes BER at SSBs (single-strand breaks); RECQL4 stimulates PARP1 activity in vitro
- Ku70/Ku80 interaction: participates in DSB repair pathway choice (RECQL4 promotes NHEJ access at some DSBs)
- Mitochondrial localization signal: ~10-15% of cellular RECQL4 localizes to mitochondria; interacts with mitochondrial PARP1; maintains mtDNA copy number and integrity; RECQL4 LOF → mtDNA deletions in RTS fibroblasts

### Germline mutations in RECQL4-associated syndromes

**Rothmund-Thomson syndrome type II (RTS type II; OMIM #268400):**
- LOF mutations (nonsense, frameshift, missense in helicase core) distributed throughout the gene
- Most common mutations: helicase core missense (disrupt ATPase activity), truncating mutations in C-terminal domain; compound heterozygotes most common
- Genotype-phenotype correlation: mutations with residual helicase activity → less severe phenotype; complete LOF → classic severe RTS; no strong predictor of osteosarcoma risk from genotype alone
- ~60-65% of clinically defined RTS type II patients have biallelic RECQL4 mutations; remainder may have other unidentified genes

**RAPADILINO syndrome (OMIM #266280):**
- AR; biallelic RECQL4 mutations (different mutation spectrum than RTS — splice site c.1390+2T>C Finnish founder mutation, ~85% of Finnish Rapadilino patients)
- Finnish founder mutation: c.1390+2T>C → exon 7 skipping → in-frame deletion of helicase motif → partial LOF
- Features: RA (radius hypoplasia/aplasia), PA (patella hypoplasia/aplasia), DILI (diarrhea, dislocated joints), LI (little size), NO (normal intelligence) — mnemonic RAPADILINO
- Osteosarcoma risk: ~8% in Rapadilino (less than RTS type II ~30%)
- No poikiloderma (distinguishes from RTS)

**Baller-Gerold syndrome (OMIM #218600):**
- AR; biallelic RECQL4 mutations (subset); also caused by TWIST mutations (no RECQL4 involvement)
- Features: craniosynostosis, radial aplasia, growth retardation; overlaps with RTS skeletal features
- Osteosarcoma: rare reports; less than RTS type II

## Function

### RECQL4 in DNA replication initiation

**CMG helicase loading — molecular mechanism:**
1. G1 phase: MCM2-7 hexameric ring loaded onto DNA origins (forming pre-replication complex, pre-RC) by ORC/CDC6/CDT1
2. Late G1/S boundary: CDK2 phosphorylates RECQL4 (and other factors); RECQL4 N-terminal Sld2-homology domain assembles with TopBP1, Treslin (Sld3 homolog), Cdc45 → firing complex
3. Firing complex displaces MCM2-7-bound proteins → recruits GINS to form CMG (Cdc45-MCM2-7-GINS) holo-helicase → CMG unwinds duplex at origin → bidirectional replication fork establishment
4. RECQL4 travels with the elongating fork as part of the CMG, though its role post-initiation is less clear
5. Depletion of RECQL4 (by siRNA or immunodepletion in Xenopus extracts) → no origin firing even though pre-RCs are intact → global replication failure → S-phase arrest

**Distinction from other replication factors:**
- RECQL4 is required for EVERY replication origin firing — not just a subset; this is unusual among RecQ helicases (BLM and WRN are not replication initiation factors)
- Partial RECQL4 LOF → hyporeplication → fewer origins fire → fork stalling compensates → but under replication stress (HU, aphidicolin), LOF cells show catastrophic stalling → DSBs → genomic instability
- RECQL4 helicase activity is dispensable for replication initiation in some assays (the Sld2-homology domain scaffolding is sufficient for CMG loading); helicase activity is required for stress responses

### RECQL4 at mitochondria

**Mitochondrial function:**
- RECQL4 localizes to mitochondria via a cryptic N-terminal MTS (mitochondrial targeting sequence); ~10-15% of total RECQL4 is mitochondrial
- Interacts with mitochondrial PARP1 and p32 (mitochondrial matrix protein) → promotes mtDNA repair
- RTS fibroblasts: reduced mtDNA copy number, increased mtDNA deletions, elevated mitochondrial ROS → mitochondrial dysfunction → may contribute to premature aging phenotype of RTS
- RECQL4 is the only RecQ helicase with established mitochondrial localization and function

### RECQL4 in BER and NHEJ

**Base excision repair (BER):**
- RECQL4 interacts with PARP1 (promotes poly-ADP-ribosylation at SSBs), XRCC1 (SSB repair scaffold), APE1 (AP endonuclease) → RECQL4 is a BER accessory factor at oxidative DNA damage lesions
- RECQL4 stimulates PARP1 ADP-ribosylation at SSBs in vitro; RECQL4 LOF → increased unrepaired 8-oxoguanine in nuclear and mitochondrial DNA

**Non-homologous end joining (NHEJ):**
- RECQL4 interacts with Ku70/Ku80 at DSBs; promotes NHEJ at DSBs in S-phase when NHEJ may compete with HR; RECQL4 acts as HR suppressor in non-replicating regions

## Mechanism

### RECQL4 helicase mechanism

**Substrate specificity:**
- Unwinds: forked duplexes (most efficient), D-loops, R-loops, G-quadruplexes (with lower efficiency than WRN or BLM), bubble substrates, flap structures
- Requires ssDNA 3'-overhang for loading (3'→5' translocation direction)
- Inefficient at long duplex regions without fork structure; no HRDC-mediated HJ recognition (unlike BLM); cannot dissolve dHJs
- ATPase-dependent translocation: Km for ATP ~30-50 μM; Walker B mutation (D605A) abolishes helicase but not scaffold function in replication

**Comparison of substrate selectivity among RecQ helicases:**
- BLM: best at dHJ dissolution (HRDC domain targets HJs), D-loops, G4; requires BTR complex for dissolution
- WRN: best at G4 structures, long forked duplexes, Holliday junctions; exonuclease acts on 3'-recessed ends
- RECQL4: best at initiating replication (via Sld2-homology); G4 less efficiently than WRN/BLM; no dHJ dissolution

### Cancer biology — RECQL4 and osteosarcoma

**Why osteosarcoma?**
- Osteosarcoma arises predominantly from osteoblast precursors during rapid bone growth; peak incidence at the adolescent growth spurt (ages 10-14)
- Osteoblasts are highly proliferative during bone growth → most dependent on RECQL4 for replication initiation → most vulnerable to RECQL4 LOF-induced replication stress
- RECQL4 LOF → replication-dependent DSBs → chromosomal instability → LOH at RB1, TP53 (the two primary osteosarcoma tumor suppressor loci) → osteosarcoma initiation
- ~30% lifetime osteosarcoma risk in RTS type II (RECQL4 biallelic LOF)
- RTS osteosarcoma: same histology as sporadic (high-grade osteoblastic, chondroblastic, fibroblastic subtypes); often multifocal; treated with standard neoadjuvant chemotherapy (MAP: methotrexate, adriamycin, cisplatin) + surgical resection
- Chemotherapy sensitivity: RTS osteosarcoma may respond differently from sporadic due to underlying replication defect; clinical trials exclude RTS patients typically; dose modification empirical

**RECQL4 somatic mutations in sporadic cancers:**
- RECQL4 somatic LOF in sporadic osteosarcoma (~5-10%): amplified osteosarcoma samples also show RECQL4 copy gain (possibly as a passenger gain in 8q amplicons)
- RECQL4 somatic mutations reported in colorectal cancer, gastric cancer, and AML (~2-5%)

**Therapeutic opportunities:**
- RECQL4 LOF → reduced replication capacity → osteosarcoma cells may be sensitized to replication stress agents (gemcitabine, hydroxyurea) — not yet clinically validated in RTS
- MAP chemotherapy (standard osteosarcoma protocol): used in RTS osteosarcoma; standard response rates observed; consult sarcoma center
- PARP inhibitors: rationale for RECQL4 LOF (impaired BER/PARP interaction) — not yet tested in RTS

## Connections

- `connects-to` → **[Rothmund-Thomson Syndrome](../../07-system/rothmund-thomson/README.md)** — Biallelic RECQL4 LOF → Rothmund-Thomson syndrome; RECQL4 loss impairs replication initiation (CMG loading) and mitochondrial DNA repair; poikiloderma, skeletal defects (radial ray), juvenile cataracts, and ~30% lifetime osteosarcoma risk; SCE is not elevated.
- `connects-to` → **[WRN](../../03-molecular/wrn/README.md)** — RECQL4 and WRN are both RecQ helicases with distinct mechanisms: WRN has exonuclease activity and resolves G-quadruplex structures; RECQL4 initiates DNA replication via CMG complex; WRN LOF → Werner syndrome (progeroid, sarcomas); RECQL4 LOF → Rothmund-Thomson (osteosarcoma).
- `connects-to` → **[BLM](../../03-molecular/blm/README.md)** — RECQL4 and BLM are both RecQ helicases: BLM dissolves Holliday junctions and suppresses crossover (SCE ~10x elevated in BLM LOF); RECQL4 initiates replication; both cause cancer predisposition — BLM LOF pan-cancer, RECQL4 LOF predominantly osteosarcoma.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — RECQL4 and p53 interact at replication origins during S-phase; p53-mediated transcription of p21 and RECQL4 both suppress aberrant replication; osteosarcoma (the hallmark cancer of Rothmund-Thomson syndrome) also occurs in Li-Fraumeni syndrome (TP53 germline LOF).

[^kitao-1999-recql4-rts]: Kitao S, Shimamoto A, Goto M, et al. Mutations in RECQL4 cause a subset of cases of Rothmund-Thomson syndrome. *Nat Genet.* 1999;22(1):82-84. [doi:10.1038/8788](https://doi.org/10.1038/8788) · [PubMed 10319867](https://pubmed.ncbi.nlm.nih.gov/10319867/)
[^sangrithi-2005-recql4-replication]: Sangrithi MN, Bernal JA, Madine M, et al. Initiation of DNA replication requires the RECQL4 protein mutated in Rothmund-Thomson syndrome. *Cell.* 2005;121(6):887-898. [doi:10.1016/j.cell.2005.05.015](https://doi.org/10.1016/j.cell.2005.05.015) · [PubMed 15960976](https://pubmed.ncbi.nlm.nih.gov/15960976/)

---
schema: human-scale-entry/v1
id: type-i-interferon
name: Type I Interferon
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "IFN-α/β (type I IFNs) are antiviral cytokines; cGAS-STING or RIG-I/MDA5 → TBK1 → IRF3/7 → IFN-α/β → IFNAR1/2 → JAK1/TYK2 → STAT1/STAT2 → ISGs. Type I IFN signature drives SLE, SSc, dermatomyositis; anifrolumab (anti-IFNAR1) approved for SLE."
aliases: ["type I interferon", "IFN-alpha", "IFN-beta", "IFN-α", "IFN-β", "IFNA", "IFNB", "type I IFN", "interferon alpha", "interferon beta", "innate antiviral", "cGAS-STING", "RIG-I", "MDA5", "MAVS", "ISG", "interferon-stimulated gene", "anifrolumab", "IFNAR1", "IFNAR2", "IFN signature"]
sources:
  - id: ivashkiv-2018-type-i-ifn-review
    type: peer-reviewed
    cite: "Ivashkiv LB, Donlin LT. Regulation of type I interferon responses. Nat Rev Immunol. 2014;14(1):36-49."
    doi: "10.1038/nri3581"
    pmid: "24362405"
    url: "https://doi.org/10.1038/nri3581"
  - id: morand-2020-anifrolumab-tulip2
    type: peer-reviewed
    cite: "Morand EF, Furie R, Tanaka Y, et al. Trial of Anifrolumab in Active Systemic Lupus Erythematosus. N Engl J Med. 2020;382(3):211-221."
    doi: "10.1056/NEJMoa1912196"
    pmid: "31851795"
    url: "https://doi.org/10.1056/NEJMoa1912196"
  - id: barrat-2019-type-i-ifn-autoimmunity
    type: peer-reviewed
    cite: "Barrat FJ, Crow MK, Ivashkiv LB. Interferon target-gene expression and epigenomic signatures in health and disease. Nat Immunol. 2019;20(12):1574-1583."
    doi: "10.1038/s41590-019-0466-2"
    pmid: "31745299"
    url: "https://doi.org/10.1038/s41590-019-0466-2"
cross_links:
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Type I IFN signature (↑MX1, ↑OAS1, ↑ISG15) is present in ~75% of SLE patients; IFN-α amplifies plasmacytoid DC activation, anti-dsDNA production, and NET formation; anifrolumab (anti-IFNAR1) reduced disease activity in TULIP-2 (SRI-4 response 47.8% vs. 31.5%)."
  - target: 01-human/07-system/systemic-sclerosis
    relation: connects-to
    note: "Type I IFN signature is elevated in ~50% of SSc patients, particularly anti-RNA pol III+ dcSSc; IFN-α promotes plasmacytoid DC activation and anti-nuclear antibody amplification; type I IFN and TGF-β cooperate to drive SSc fibroblast activation and ILD progression."
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: connects-to
    note: "SARS-CoV-2 encodes multiple IFN evasion proteins (NSP1 blocks translation, NSP3 papain-like protease deISGylates, ORF6 blocks STAT1 nuclear import); impaired early IFN-β response predicts severe COVID-19; type I IFN treatment window closes after peak viral replication."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "TLR7/9 → MyD88 → IRF7 and TBK1 → IRF3 pathways activate type I IFN in parallel with NF-κB; NF-κB drives IFN-β enhanceosome formation (NF-κB + IRF3 + AP-1 at IFN-β promoter); type I IFN-induced ISGs suppress NF-κB through STAT1 and SOCS1."
  - target: 01-human/07-system/dermatomyositis
    relation: connects-to
    note: "Type I IFN signature (↑MX1, ↑OAS1, ↑RSAD2) is elevated in muscle and blood in >80% of DM; anti-MDA5 (IFIH1) senses dsRNA → MAVS-TBK1-IRF3 → IFN-β; pDC infiltration drives DM interferonopathy; anifrolumab (anti-IFNAR1) under investigation for DM."
  - target: 01-human/07-system/nmo
    relation: connects-to
    note: "IFN-β is CONTRAINDICATED in AQP4-IgG+ NMOSD — clinical trials showed IFN-β increases attack frequency; IFN-β may promote plasmablast differentiation → higher AQP4-IgG titers; differentiates NMOSD from MS (IFN-β first-line in MS but harmful in NMOSD)."
  - target: 01-human/07-system/sjogrens-syndrome
    relation: connects-to
    note: "Type I IFN signature is present in ~75% of pSS (highest in anti-Ro/SSA+ patients); pDCs sense anti-Ro/RNA complexes via TLR7 → IFN-α; IFN-α → BAFF upregulation → B-cell hyperactivation; IFN signature correlates with ESSDAI and systemic Sjögren's manifestations."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "cGAS-STING is the primary upstream inducer of type I IFN in response to cytosolic dsDNA: dsDNA → cGAS → cGAMP → STING → TBK1/IKKε → IRF3 → IFN-β transcription; cGAS-STING-driven type I IFN underlies SLE interferonopathy, AGS, anti-tumor immunity, and antiviral defense."
  - target: 01-human/07-system/aicardi-goutieres-syndrome
    relation: connects-to
    note: "AGS is the prototype genetic interferonopathy: TREX1/RNASEH2/SAMHD1/ADAR1 mutations → nucleic acid accumulation → cGAS-STING → constitutive IFN-α/β; CSF IFN-α >2 IU/mL is diagnostic; JAK inhibitors and reverse transcriptase inhibitors reduce IFN-α in clinical trials."
  - target: 01-human/03-molecular/mavs
    relation: connects-to
    note: "MAVS is the mitochondrial adaptor for RIG-I/MDA5 RNA sensing → type I IFN: 5′ppp-dsRNA → RIG-I → MAVS prion-like filament → TRAF3/TBK1 → IRF3/IRF7 → IFN-α/β; MAVS and cGAS-STING are the two major parallel upstream inducers of type I IFN in antiviral innate immunity."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFNAR1/2 → JAK1/TYK2 → STAT1 Tyr701 + STAT2 Tyr689 phosphorylation → ISGF3 (STAT1/STAT2/IRF9) → ISRE → ISGs (MX1, OAS1, IFIT1, PKR); STAT1 is the transcription factor transducing type I IFN signaling; STAT1 GOF → CMC; STAT1 LOF → viral susceptibility and MSMD."
  - target: 01-human/07-system/influenza
    relation: connects-to
    note: "Influenza RIG-I/MAVS → IRF3 → IFN-β in epithelial cells; pDC TLR7 → IFN-α; NS1 blocks IRF3 and dsRNA sensing; H5N1 paradoxically induces high IFN-β contributing to cytokine storm; NS1 IFN antagonism strength is the key difference between pandemic and seasonal influenza strains."
  - target: 01-human/03-molecular/irf3
    relation: connects-to
    note: "IRF3 is the master transcription factor for IFN-β: phospho-IRF3 dimers bind PRDI/III on the IFN-β promoter; IRF3 + NF-κB + AP-1 form the enhanceosome; TBK1 phosphorylates IRF3 Ser396 downstream of MAVS and STING; IRF7 amplifies IFN-α in the second wave response."
  - target: 01-human/07-system/hepatitis-c
    relation: connects-to
    note: "HCV evades type I IFN: NS3/4A cleaves MAVS → no IFN-β; NS5A blocks PKR; high baseline ISG expression from low-grade IFN predicts pegIFN-α failure; IL28B TT genotype (high ISGs) = pegIFN non-response; DAAs bypass IFN-dependent mechanisms and achieve >95% cure."
  - target: 01-human/07-system/rsv
    relation: connects-to
    note: "RSV NS1/NS2 cooperatively block type I IFN: NS1 targets TRIM25/IRF3, NS2 blocks STAT2 nuclear translocation → ISGs suppressed; immature IFN signaling in premature infants → more severe RSV bronchiolitis; IFN-λ (type III) at mucosal surfaces is dominant innate RSV defense."
  - target: 01-human/03-molecular/rsv-f-protein
    relation: connects-to
    note: "RSV F protein (prefusion, proline-stabilized) exposes site Ø → high-titer neutralizing antibodies; all approved RSV vaccines (Abrysvo, Arexvy, mResvia) and nirsevimab target site Ø; RSV NS1/NS2 block type I IFN but not IFN-λ; F TLR4 signaling amplifies innate inflammation."
---

# Type I Interferon

## Overview

**Type I interferons (IFN-α/β)** are a family of secreted cytokines that constitute the **first line of antiviral defense** in virtually all nucleated cells and are central orchestrators of innate immunity [^ivashkiv-2018-type-i-ifn-review]. The family includes:

- **IFN-α:** 13 functional subtypes (IFNA1, IFNA2, IFNA4, IFNA5, IFNA6, IFNA7, IFNA8, IFNA10, IFNA13, IFNA14, IFNA16, IFNA17, IFNA21); clustered on chromosome 9p21; primarily produced by **plasmacytoid dendritic cells (pDCs)** — the principal "IFN factories" of the immune system (up to 1,000× more IFN per cell than other leukocytes)
- **IFN-β:** Single gene (*IFNB1*, chr9p21.3); produced by nearly all nucleated cells (fibroblasts, epithelial cells, macrophages) in response to intracellular nucleic acid sensing
- **IFN-ε, IFN-κ, IFN-ω:** Minor type I IFNs with tissue-restricted expression (mucosal, keratinocyte)

All type I IFNs signal through the same receptor complex — **IFNAR1/IFNAR2** — distinguishing them from type II IFN (IFN-γ, signals via IFNGR1/IFNGR2) and type III IFNs (IFN-λ1-4, IL28RA/IL10RB, primarily epithelial antiviral defense). Type I IFN signaling drives expression of **hundreds of interferon-stimulated genes (ISGs)** that establish the antiviral state and modulate adaptive immunity.

**Clinical significance:** Dysregulated type I IFN is central to **systemic autoimmune diseases** — particularly SLE, systemic sclerosis, dermatomyositis, Sjögren's syndrome, and primary antiphospholipid syndrome — where chronic activation of IFN-α/β drives inflammation, autoantibody production, and organ damage [^barrat-2019-type-i-ifn-autoimmunity]. The "type I IFN signature" — elevated expression of ISGs (MX1, OAS1-3, ISG15, IFIT1-3) measurable in blood — is the most robust biomarker of disease activity in SLE. **Anifrolumab** (anti-IFNAR1 mAb; AstraZeneca), approved by the FDA in August 2021, is the first approved therapy directly targeting IFN signaling for SLE [^morand-2020-anifrolumab-tulip2].

## Structure

### The IFNB1 enhanceosome

IFN-β transcription is among the best-characterized mammalian gene regulatory events:

**IFN-β enhanceosome:** A precisely assembled multiprotein complex on the 70 bp IFN-β enhancer region (~−100 to −35 upstream of TSS), requiring simultaneous binding of:
- **NF-κB** (p65/p50 heterodimer): virus-induced IKK activation → IκBα degradation → NF-κB nuclear entry
- **IRF3/IRF7** (dimer): TBK1 phosphorylation of IRF3 Ser386/396 → nuclear translocation
- **AP-1** (c-Jun/ATF-2): MAPK signaling

Cooperative binding of all three factors, plus HMG-I/Y architectural protein, is required for full enhanceosome assembly → RNA Pol II recruitment → IFN-β transcription. This "AND-gate" logic ensures IFN-β production only when multiple danger signals co-occur.

**IFN-α promoters** lack the full enhanceosome architecture; they are primarily regulated by **IRF7** (not IRF3), explaining why pDCs (which constitutively express high IRF7) are superior IFN-α producers.

### Type I IFN receptor complex (IFNAR)

| Subunit | Gene | Associated kinase | Signal transduction |
|---|---|---|---|
| IFNAR1 | *IFNAR1* (chr21q22.11) | TYK2 (pre-associated) | Ligand binding: IFN-β > IFN-α; signal initiation |
| IFNAR2 | *IFNAR2* (chr21q22.11) | JAK1 (pre-associated) | Ligand binding: IFN-α > IFN-β |

IFN binding → IFNAR1/IFNAR2 dimerization → TYK2/JAK1 cross-phosphorylation → STAT1 Tyr701 and STAT2 Tyr690 phosphorylation → STAT1/STAT2 dimerization → recruitment of **IRF9** → **ISGF3** (Interferon-Stimulated Gene Factor 3) complex → nuclear translocation → binds **ISRE** (Interferon-Stimulated Response Element; consensus: GAAA-N₂₋₃-GAAACT) → ISG transcription.

## Function

### Antiviral effector ISGs

The type I IFN-induced ISG repertoire (~300-500 genes) establishes the **antiviral state**:

| ISG | Gene | Mechanism |
|---|---|---|
| MX1/MX2 | *MX1*, *MX2* | Dynamin-like GTPases; block viral RNA synthesis; MX1 restricts influenza A, bunyavirus |
| OAS1-3/RNASEL | *OAS1-3*, *RNASEL* | dsRNA → OAS → 2',5'-oligoadenylate → RNase L activation → viral/cellular RNA degradation |
| PKR | *EIF2AK2* | dsRNA-activated kinase → eIF2α Ser51 phosphorylation → global translation inhibition → viral protein synthesis arrested |
| ISG15 | *ISG15* | Ubiquitin-like modifier; ISGylation of host and viral proteins; innate immune amplification |
| APOBEC3G/H | *APOBEC3G/H* | Cytidine deaminase; mutates retroviral cDNA during reverse transcription; restricts HIV |
| SAMHD1 | *SAMHD1* | dNTP hydrolase; depletes dNTP pool → restricts HIV/HTLV reverse transcription |
| IFITM1-3 | *IFITM1-3* | Block viral membrane fusion at endosomes; restrict influenza, dengue, Ebola |
| TRIM5α | *TRIM5* | Restricts retroviral capsid uncoating (species-specific) |

### Innate immune sensing — upstream pathways

**cGAS-STING pathway (cytosolic DNA sensing):**
1. dsDNA (viral, mitochondrial, nuclear) → **cGAS** (cGMP-AMP synthase; *MB21D1*, chr15q25) → catalyzes GTP + ATP → **2',3'-cGAMP** (cyclic GMP-AMP)
2. cGAMP → **STING** (stimulator of interferon genes; *STING1*/TMEM173, chr5q31) → STING dimerization + palmitoylation → ER-to-Golgi trafficking
3. STING → recruits **TBK1** (TANK-binding kinase 1) → TBK1 phosphorylates STING Ser366 + IRF3 Ser386/396
4. IRF3 dimer → nucleus → IFN-β enhanceosome → IFN-β transcription
5. Simultaneously: STING → IKK → NF-κB → inflammatory cytokines

**RIG-I/MDA5 pathway (cytosolic RNA sensing):**
1. **RIG-I** (*DDX58*): short dsRNA, 5'-ppp RNA (influenza, paramyxovirus)
2. **MDA5** (*IFIH1*): long dsRNA (picornavirus, COVID-19 dsRNA replication intermediates)
3. Both → interact with **MAVS** (mitochondrial antiviral-signaling protein; *MAVS*) via CARD-CARD domain → MAVS prion-like aggregation on mitochondrial outer membrane → scaffold for TBK1 + TRAF3/6 → IRF3/7 + NF-κB

**TLR-mediated sensing (endosomal):**
- **TLR7/8** (ssRNA; pDC endosome) → **MyD88** → IRAK4 → TRAF6 → IRF7 → IFN-α
- **TLR9** (CpG DNA; pDC endosome) → MyD88 → IRAK4 → TRAF6 → IRF7 → IFN-α (massive pDC output)
- **TLR3** (dsRNA; conventional DC) → **TRIF** → TBK1 → IRF3 → IFN-β

## Mechanism

### IFNAR signaling and negative regulation

**Canonical JAK-STAT signaling → ISGF3:**
- IFNAR → JAK1/TYK2 → pSTAT1 (Y701) + pSTAT2 (Y690) → STAT1/STAT2 heterodimer + IRF9 → **ISGF3** → ISRE elements → ISG expression
- **STAT1 homodimer** (pSTAT1-pSTAT1) also forms → binds **GAS** elements → IFN-γ-like gene signature (partial overlap with STAT1 homodimer-driven genes)
- **Non-canonical signaling:** PI3K/Akt (protein synthesis); MAPK/ERK; mTOR (translation efficiency of ISG mRNAs)

**Negative regulators (critical for preventing IFN toxicity):**
- **SOCS1/3 (STAT3):** Rapidly induced ISGs; bind phospho-JAKs → proteasomal degradation; SOCS1 is the primary negative feedback for IFN-α/β signaling
- **USP18:** ISG15 deubiquitinase that also acts as a decoy receptor — USP18 binds IFNAR2, blocking its interaction with JAK1 → prevents sustained IFN signaling. USP18 deficiency (Mendelian disease) → life-threatening neonatal type I interferonopathy
- **IRF2:** Transcriptional repressor of ISRE elements; competes with IRF3/7/9

**Viral IFN evasion strategies (selected):**
- **SARS-CoV-2:** NSP1 blocks ribosomal mRNA translation; NSP3 papain-like protease removes ISG15 and ubiquitin from innate signaling proteins; NSP16 caps viral RNA to hide from MDA5; ORF6 blocks KPNA2 (importin) → blocks STAT1 nuclear import
- **Influenza A:** NS1 protein sequesters dsRNA → hides from MDA5/RIG-I; also inhibits TRIM25 (RIG-I ubiquitination required for activation)
- **HIV:** Vpr/Vpx degrade SAMHD1; Vif degrades APOBEC3G; neither HIV-1 nor HIV-2 encodes a direct anti-cGAS-STING evasion factor

### Interferonopathies

Monogenic diseases of uncontrolled type I IFN production:

| Disease | Gene | Mechanism |
|---|---|---|
| Aicardi-Goutières syndrome (AGS) | *TREX1*, *RNASEH2A/B/C*, *SAMHD1*, *ADAR*, *IFIH1* | Failure to degrade endogenous nucleic acids → chronic cGAS or MDA5 activation |
| SAVI (STING-associated vasculopathy with onset in infancy) | *STING1* GOF | Constitutively active STING → TBK1 → IRF3 → chronic IFN-β → pulmonary fibrosis + vasculopathy |
| PRAAS (proteasome-associated autoinflammatory syndrome) | *PSMB8*, *PSMB9*, *PSMA3* | Impaired proteasome → ↑ubiquitinated proteins → cGAS/STING activation → type I IFN |
| DNase II deficiency | *DNASE2* | Failure to degrade nuclear DNA in macrophage lysosomes → TLR9/cGAS chronic activation |

## Connections

- `connects-to` → **[Systemic Lupus Erythematosus](../../07-system/systemic-lupus-erythematosus/README.md)** — Type I IFN signature (↑MX1, ↑OAS1, ↑ISG15) is present in ~75% of SLE patients; IFN-α amplifies plasmacytoid DC activation, anti-dsDNA production, and NET formation; anifrolumab (anti-IFNAR1) reduced disease activity in TULIP-2 (SRI-4 response 47.8% vs. 31.5%).
- `connects-to` → **[Systemic Sclerosis](../../07-system/systemic-sclerosis/README.md)** — Type I IFN signature is elevated in ~50% of SSc patients, particularly anti-RNA pol III+ dcSSc; IFN-α promotes plasmacytoid DC activation and anti-nuclear antibody amplification; type I IFN and TGF-β cooperate to drive SSc fibroblast activation and ILD progression.
- `connects-to` → **[SARS-CoV-2](../../../02-pathogen/01-viruses/sars-cov-2/README.md)** — SARS-CoV-2 encodes multiple IFN evasion proteins (NSP1 blocks translation, NSP3 papain-like protease deISGylates, ORF6 blocks STAT1 nuclear import); impaired early IFN-β response predicts severe COVID-19; type I IFN treatment window closes after peak viral replication.
- `connects-to` → **[NF-κB](../nf-kb/README.md)** — TLR7/9 → MyD88 → IRF7 and TBK1 → IRF3 pathways activate type I IFN in parallel with NF-κB; NF-κB drives IFN-β enhanceosome formation (NF-κB + IRF3 + AP-1 at IFN-β promoter); type I IFN-induced ISGs suppress NF-κB through STAT1 and SOCS1.
- `connects-to` → **[Dermatomyositis](../../07-system/dermatomyositis/README.md)** — Type I IFN signature (↑MX1, ↑OAS1, ↑RSAD2) is elevated in muscle and blood in >80% of DM; anti-MDA5 (IFIH1) senses dsRNA → MAVS-TBK1-IRF3 → IFN-β; pDC infiltration drives DM interferonopathy; anifrolumab (anti-IFNAR1) under investigation for DM.
- `connects-to` → **[NMOSD](../../07-system/nmo/README.md)** — IFN-β is CONTRAINDICATED in AQP4-IgG+ NMOSD — clinical trials showed IFN-β increases attack frequency; IFN-β may promote plasmablast differentiation → higher AQP4-IgG titers; distinguishes NMOSD from MS (where IFN-β is first-line).
- `connects-to` → **[Sjögren's Syndrome](../../07-system/sjogrens-syndrome/README.md)** — Type I IFN signature is present in ~75% of pSS (highest in anti-Ro/SSA+ patients); pDCs sense anti-Ro/RNA complexes via TLR7 → IFN-α; IFN-α → BAFF upregulation → B-cell hyperactivation; IFN signature correlates with ESSDAI and systemic Sjögren's manifestations.
- `connects-to` → **[cGAS-STING](../cgas-sting/README.md)** — cGAS-STING is the primary upstream inducer of type I IFN in response to cytosolic dsDNA: dsDNA → cGAS → cGAMP → STING → TBK1/IKKε → IRF3 → IFN-β transcription; cGAS-STING-driven type I IFN underlies SLE interferonopathy, AGS, anti-tumor immunity, and antiviral defense.
- `connects-to` → **[Aicardi-Goutières Syndrome](../../07-system/aicardi-goutieres-syndrome/README.md)** — AGS is the prototype genetic interferonopathy: TREX1/RNASEH2/SAMHD1/ADAR1 mutations → nucleic acid accumulation → cGAS-STING → constitutive IFN-α/β; CSF IFN-α >2 IU/mL is diagnostic; JAK inhibitors and reverse transcriptase inhibitors reduce IFN-α in clinical trials.
- `connects-to` → **[MAVS](../mavs/README.md)** — MAVS is the central adaptor linking cytosolic RNA sensing (RIG-I/MDA5) to type I IFN production; 5′ppp-dsRNA → RIG-I → MAVS prion-like filament → TRAF3/TBK1 → IRF3/IRF7 → IFN-α/β; MAVS and cGAS-STING are the two major parallel upstream inducers of type I IFN in antiviral innate immunity.
- `connects-to` → **[STAT1](../stat1/README.md)** — IFNAR1/2 → JAK1/TYK2 → STAT1/STAT2 phosphorylation → ISGF3 (STAT1/STAT2/IRF9) → ISRE → ISGs (MX1, OAS1, IFIT1, PKR); STAT1 is the transcription factor transducing type I IFN signaling; STAT1 GOF → CMC; STAT1 LOF → viral susceptibility and MSMD.
- `connects-to` → **[Influenza](../../07-system/influenza/README.md)** — Influenza RIG-I/MAVS → IRF3 → IFN-β in epithelial cells; pDC TLR7 → IFN-α; NS1 blocks IRF3 and dsRNA sensing; H5N1 paradoxically induces high IFN-β contributing to cytokine storm; NS1 IFN antagonism distinguishes pandemic from seasonal influenza strains.
- `connects-to` → **[IRF3](../irf3/README.md)** — IRF3 is the master transcription factor for IFN-β: phospho-IRF3 dimers bind PRDI/III on the IFN-β promoter; IRF3 + NF-κB + AP-1 form the enhanceosome; TBK1 phosphorylates IRF3 Ser396 downstream of MAVS and STING; IRF7 amplifies IFN-α in the second wave response.
- `connects-to` → **[Hepatitis C](../../07-system/hepatitis-c/README.md)** — HCV evades type I IFN: NS3/4A cleaves MAVS → no IFN-β; NS5A blocks PKR; high baseline ISG expression from low-grade IFN predicts pegIFN-α failure; IL28B TT genotype (high ISGs) = pegIFN non-response; DAAs bypass IFN-dependent mechanisms and achieve >95% cure.
- `connects-to` → **[RSV](../../07-system/rsv/README.md)** — RSV NS1/NS2 cooperatively block type I IFN: NS1 targets TRIM25/IRF3, NS2 blocks STAT2 nuclear translocation → ISGs suppressed; immature IFN signaling in premature infants → more severe RSV bronchiolitis; IFN-λ (type III) at mucosal surfaces is the dominant innate RSV defense.
- `connects-to` → **[RSV F Protein](../rsv-f-protein/README.md)** — RSV F protein (prefusion, proline-stabilized) exposes site Ø → high-titer neutralizing antibodies; all approved RSV vaccines (Abrysvo, Arexvy, mResvia) and nirsevimab target site Ø; RSV NS1/NS2 block type I IFN but not IFN-λ; F TLR4 signaling amplifies innate inflammation.

[^ivashkiv-2018-type-i-ifn-review]: Ivashkiv LB, Donlin LT. Regulation of type I interferon responses. *Nat Rev Immunol.* 2014;14(1):36-49. [doi:10.1038/nri3581](https://doi.org/10.1038/nri3581) · [PubMed 24362405](https://pubmed.ncbi.nlm.nih.gov/24362405/)
[^morand-2020-anifrolumab-tulip2]: Morand EF, Furie R, Tanaka Y, et al. Trial of Anifrolumab in Active Systemic Lupus Erythematosus. *N Engl J Med.* 2020;382(3):211-221. [doi:10.1056/NEJMoa1912196](https://doi.org/10.1056/NEJMoa1912196) · [PubMed 31851795](https://pubmed.ncbi.nlm.nih.gov/31851795/)
[^barrat-2019-type-i-ifn-autoimmunity]: Barrat FJ, Crow MK, Ivashkiv LB. Interferon target-gene expression and epigenomic signatures in health and disease. *Nat Immunol.* 2019;20(12):1574-1583. [doi:10.1038/s41590-019-0466-2](https://doi.org/10.1038/s41590-019-0466-2) · [PubMed 31745299](https://pubmed.ncbi.nlm.nih.gov/31745299/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

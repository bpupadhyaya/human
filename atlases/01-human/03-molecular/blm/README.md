---
schema: human-scale-entry/v1
id: blm
name: BLM
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "BLM is a RecQ helicase that dissolves double Holliday junctions via the BTR complex to suppress crossover during homologous recombination; biallelic BLM LOF → Bloom syndrome — elevated SCE (~10x), growth retardation, immunodeficiency, and pan-cancer predisposition."
aliases: ["BLM", "Bloom syndrome helicase", "BLM helicase", "RECQL3", "BLM RecQ helicase", "Bloom syndrome BLM", "BLM DNA repair", "BLM sister chromatid exchange", "BTR complex BLM"]
sources:
  - id: ellis-1995-blm-cloning
    type: peer-reviewed
    cite: "Ellis NA, Groden J, Ye TZ, et al. The Bloom's syndrome gene product is homologous to RecQ helicases. Cell. 1995;83(4):655-666."
    doi: "10.1016/0092-8674(95)90105-1"
    pmid: "7585968"
    url: "https://doi.org/10.1016/0092-8674(95)90105-1"
  - id: german-1997-bloom-cancer
    type: peer-reviewed
    cite: "German J. Bloom's syndrome. XX. The first 100 cancers. Cancer. 1997;71(12):4016-4023."
    doi: "10.1002/1097-0142(19930615)71:12<4016::AID-CNCR18>3.0.CO;2-E"
    pmid: "9216035"
    url: "https://doi.org/10.1002/1097-0142(19930615)71:12<4016::AID-CNCR18>3.0.CO;2-E"
cross_links:
  - target: 01-human/07-system/bloom-syndrome
    relation: connects-to
    note: "Biallelic BLM LOF → Bloom syndrome via crossover accumulation and SCE elevation (~10x); chromosomal instability → LOH at tumor suppressor loci → pan-cancer predisposition (ALL, lymphoma, GI carcinoma, skin); Bloom Syndrome Registry has tracked >300 patients for >60 years."
  - target: 01-human/03-molecular/brca1
    relation: connects-to
    note: "BLM and BRCA1 form a complex at stalled replication forks to suppress aberrant homologous recombination and resolve Holliday junctions; both BLM LOF and BRCA1 LOF result in chromosomal instability and pan-cancer predisposition via distinct but overlapping HR defects."
  - target: 01-human/03-molecular/wrn
    relation: connects-to
    note: "BLM and WRN are both RecQ helicases: BLM resolves double Holliday junctions to suppress crossover (SCE elevated ~10x in BLM LOF); WRN has exonuclease activity and maintains telomeres; BLM LOF → childhood-onset pan-cancer; WRN LOF → adult progeroid syndrome."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "BLM LOF in Bloom syndrome confers elevated colorectal cancer risk due to crossover-mediated LOH at APC and other CRC tumor suppressor loci; GI carcinomas are among the most common malignancies in adult Bloom syndrome patients; colonoscopy surveillance from early adulthood."
  - target: 01-human/03-molecular/rad51
    relation: connects-to
    note: "BLM acts as both pro- and anti-recombinase for RAD51; BLM-DNA2 promotes DSB end resection → RPA → RAD51 loading (pro); BLM also displaces RAD51 from ssDNA to inhibit crossover (anti); the BLM-RAD51 balance determines HR fidelity and crossover frequency in S/G2."
  - target: 01-human/03-molecular/atm
    relation: connects-to
    note: "ATM phosphorylates BLM at Ser646 after DSBs → recruits BLM to γH2AX foci; BLM promotes long-range end resection with DNA2; ATM-BLM axis enables HR in G2; BLM LOF + ionizing radiation → catastrophic chromosomal breakage; BS patients are highly radiosensitive."
  - target: 01-human/03-molecular/mlh1
    relation: connects-to
    note: "BLM interacts with MLH1 (MMR) via its N-terminal region; BLM-MLH1 cooperation suppresses microsatellite instability; BLM unwinds heteroduplex DNA during MMR; some BS GI cancers show MSI-H — dual HR + MMR defect may contribute to extreme GI carcinoma risk."
---

# BLM

## Overview

**BLM** (Bloom Syndrome, RecQ helicase-like; also RECQL3) is a 1,417 amino acid (159 kDa) member of the **RecQ family of 3'→5' DNA helicases** that functions primarily to **dissolve double Holliday junctions (dHJs)** — the central intermediate of homologous recombination (HR). BLM acts as the catalytic core of the **BTR complex** (BLM–Topoisomerase IIIα–RMI1–RMI2): BLM helicase unwinds the two Holliday junctions simultaneously in a convergent manner, feeding the underwound ssDNA through Top3α (which performs strand passage), generating non-crossover products — a process called **dissolution**. This distinguishes the BTR mechanism from **resolution** (by GEN1/SLX1/SLX4/MUS81 nucleases), which can generate either crossover or non-crossover products. By strongly favoring the non-crossover pathway, BLM suppresses loss of heterozygosity (LOH) that would otherwise arise from crossing over, thereby preventing tumor suppressor silencing. The consequences of BLM LOF are spectacularly visible at the chromosome level: **sister chromatid exchanges (SCE) are elevated ~10-fold** in Bloom syndrome cells — the diagnostic gold standard — reflecting unconstrained crossover between sister chromatids. Biallelic BLM mutations cause **Bloom syndrome (BS)**, an autosomal recessive condition featuring small body size (the most uniform feature), sun-sensitive facial telangiectasia, immunodeficiency, and a dramatically elevated pan-cancer risk affecting virtually every organ system. BLM was positionally cloned by Ellis et al. in 1995; the Bloom Syndrome Registry (BSR) established by James German has followed over 300 patients for >60 years and provides the most complete cancer dataset for any RecQ helicase disorder [^ellis-1995-blm-cloning] [^german-1997-bloom-cancer].

**BLM vs. other RecQ helicases — distinct clinical phenotypes:**

| Gene | Clinical Syndrome | Age of onset | SCE | Primary cancer risk |
|---|---|---|---|---|
| BLM | Bloom syndrome | Birth | ~10x elevated | Pan-cancer (ALL, lymphoma, GI, skin) |
| WRN | Werner syndrome | 3rd decade | ~2-3x elevated | Sarcomas, melanoma, thyroid |
| RECQL4 | Rothmund-Thomson | Childhood | Not elevated | Osteosarcoma |

## Structure

### BLM protein domains

**N-terminal disordered region (aa 1-647):**
- No crystal structure available for full-length BLM; N-terminal region (~647 aa) is largely intrinsically disordered; contains nuclear localization signals and multiple regulatory phosphorylation sites
- **Key phosphosites**:
  - Thr99, Thr122: phosphorylated by ATM/ATR after DNA damage → activates BLM at damage sites; dephosphorylated by PP2A to terminate the response
  - Ser144: Aurora B kinase phosphorylation during mitosis → regulates BLM nuclear exclusion in mitosis (BLM is excluded from condensed chromosomes)
  - Thr99 (CDK1): cell cycle-dependent regulation — BLM is most active in S/G2

**N-terminal OB-fold protein interaction region:**
- Contains interaction sites for RAD51 (BLM anti-recombinase function — displaces RAD51 from ssDNA; promotes anti-crossover HR), RPA (functional partner at ssDNA), MLH1 (mismatch repair interface)
- BLM-RAD51 interaction: BLM can translocate on ssDNA (bound by RAD51 filament) and displace RAD51 → regulates strand invasion during HR; not all RecQ helicases have this anti-recombinase activity; BLM uses it to limit aberrant recombination

**Helicase core (aa 648-1,012):**
- Seven RecA-like motifs (Walker A/B, I/Ia/II/III/IV/V/VI); 3'→5' translocation on ssDNA (3' overhang strand displaced); unwinds partial duplexes, G-quadruplex structures, forked duplexes, flap structures, holiday junction-like structures
- BLM G4 unwinding: can unwind G-quadruplex DNA, though less efficiently than WRN; functional at telomeres during lagging strand synthesis; important for rDNA replication (where G-rich repeats form G4)
- **HRDC domain (aa 1,077-1,220)**: aids DNA binding; required for dHJ recognition; BLM HRDC domain interacts specifically with Holliday junctions (selectivity for the branched DNA form)
- **C-terminal Top3α interaction domain (aa 1,220-1,417)**: mediates direct binding to Topoisomerase IIIα (essential for BTR complex assembly and dHJ dissolution)

### BTR complex — double Holliday junction dissolution

**Complex composition:**
- **BLM** (helicase, catalytic): translocates inward on the dHJ; unwinds both junctions simultaneously toward each other
- **Topoisomerase IIIα** (Type I topoisomerase): performs strand passage to resolve the hemicatenane intermediate generated by BLM's convergent branch migration; Top3α covalent reaction mechanism: transient 5'-phosphotyrosine intermediate
- **RMI1** (RecQ-mediated genome instability protein 1): scaffold; bridges BLM and Top3α; required for dHJ dissolution in vitro and in vivo; contains OB-fold domains for ssDNA binding
- **RMI2**: auxiliary scaffold that stabilizes the RMI1-Top3α interaction; required for full BTR activity; RMI2 LOF (partial loss) causes elevated SCE similar to BLM LOF

**dHJ dissolution mechanism:**
1. HR strand invasion → D-loop extends → second-end capture → double Holliday junction (dHJ; two connected Holliday junctions flanking the heteroduplex region)
2. BTR is recruited to dHJ; BLM binds at both HJ branch points and migrates them convergently inward (both junctions approach each other)
3. Convergent branch migration generates a hemicatenane (two ssDNA circles linked by a covalent strand)
4. Top3α performs strand passage through the hemicatenane → complete decatenation → two separate dsDNA molecules with the repair information incorporated → non-crossover product
5. The non-crossover outcome prevents LOH (which would occur if the same junction were resolved by nucleases that cut crosswise)

## Function

### BLM as a crossover suppressor

**Why crossover suppression matters:**
- In S/G2, HR between homologous chromosomes (not sister chromatids) can generate crossovers → LOH at all loci distal to the crossover point on that chromosome arm
- If a tumor suppressor gene is heterozygous LOF (one mutant allele) and an HR crossover event places the mutant allele on both chromosomes → biallelic LOF without a second mutation → tumor initiation
- BLM suppresses crossover by channeling HR through dissolution (non-crossover) vs resolution (crossover-prone)
- SCE (sister chromatid exchanges) measure crossovers between identical sister chromatids (same sequence, no LOH generated) — SCE is the visible indicator of crossover frequency; elevated in BLM LOF because the same dissolution-vs-resolution imbalance affects sister chromatid junctions

**Diagnostic significance of elevated SCE:**
- Normal human cells: ~5-10 SCEs per metaphase cell
- Bloom syndrome cells: ~50-100 SCEs per metaphase cell (~10x elevated; highly reproducible)
- SCE assay: BrdU (bromodeoxyuridine) incorporation for two cycles → sister chromatids differentially labeled → metaphase spread staining → count exchanges under fluorescence; SCE ≥50 per metaphase is diagnostic for Bloom syndrome
- SCE ~10-fold elevated is specific for BLM LOF; WRN LOF, BRCA1/2 LOF, other HR deficiencies do NOT elevate SCE to this degree

**BLM and fork restart:**
- BLM also functions at stalled replication forks: regulates fork regression (fork reversal → fork protection) and restart; BLM promotes restart of stalled forks by template switching
- In the absence of BLM, stalled forks collapse to double-strand breaks → aberrant recombination → chromosomal rearrangements and crossovers
- BLM interaction with FANCM (Fanconi anemia complementation group M): both promote fork reversal; BLM may be a downstream effector of the FA pathway at stalled forks

### BLM in DNA damage response

**G2/M checkpoint and BLM:**
- BLM is phosphorylated by ATM at Ser646 in response to DSBs → recruited to γH2AX foci → participates in end-resection (5'→3' nucleolytic degradation of DSB ends to generate 3' ssDNA overhangs for RAD51 loading)
- BLM-DNA2 complex: BLM unwinds DNA at DSB ends, allowing DNA2 (an exonuclease) to process the 5' strand → long-range resection → RPA-coated 3' ssDNA → RAD51 loading → HR
- BLM anti-recombinase: BLM also restrains premature RAD51 filament formation (by competing with RAD51 for ssDNA binding and by stimulating FBLX1-mediated RAD51 disassembly) — a regulatory balance between pro- and anti-recombinase activities

**Nucleolar BLM:**
- Like WRN, BLM accumulates in nucleoli; BLM is required for efficient rDNA replication; rDNA repeat arrays (13.5 kb repeats, ~400 copies in humans) are prone to recombination (rDNA amplification and deletion are suppressed by BLM); BLM LOF → rDNA rearrangements → reduced ribosome biogenesis in Bloom syndrome

## Mechanism

### BLM germline mutations and Bloom syndrome genetics

**Mutation spectrum:**
- Over 70 distinct BLM mutations causing Bloom syndrome; all result in loss of helicase activity, complex assembly, or nuclear localization
- **blmAsh founder mutation (Ashkenazi Jewish)**: c.2207_2212delATCTGAinsTAGATTC (6 bp deletion + 7 bp insertion in exon 10; net +1 frameshift → premature stop codon at aa 740); ~1 in 48,000 Ashkenazi Jews are carriers; responsible for ~80% of Bloom syndrome in Ashkenazi families
- Non-Ashkenazi mutations: diverse spectrum; missense within helicase core (DSBH fold), nonsense, frameshifts, splice site; compound heterozygotes common outside Ashkenazi populations

**Ashkenazi Jewish carrier screening:**
- blmAsh is detected by standard allele-specific PCR or sequencing; included in standard Ashkenazi Jewish carrier panels (along with HEXA, CFTR, FANCC, etc.)
- Carrier frequency ~1/48,000 → sibling risk 1/4 for homozygotes when two carriers; ~0.005% chance of affected offspring from two Ashkenazi carriers

**Somatic BLM reversion:**
- Intragenic recombination: in BS cells (which have elevated SCE), a second somatic event can revert one BLM allele to wildtype within a clone → somatic rescue → rare clones with normal BLM function emerge; these wild-type revertants have a growth advantage → can overgrow the BS cells in culture
- BLM somatic reversion can confound genetic diagnosis if blood samples are taken from revertant clones — requires testing of other tissues (fibroblasts, hair roots) for confirmation

**BLM somatic mutations in cancer:**
- BLM somatic LOF in sporadic AML, colorectal cancer, and other tumors (~2-5% of cases); somatic BLM LOF → elevated LOH → accelerated tumor suppressor silencing → clonal evolution; BLM is classified as a moderate-penetrance tumor suppressor in sporadic cancer

**Therapeutic considerations in Bloom syndrome:**
- No disease-modifying therapy; management is cancer surveillance and early treatment
- Standard chemotherapy: Bloom syndrome cells are hypersensitive to DNA cross-linking agents (cisplatin, mitomycin C) because BLM is required for ICL repair; BLM LOF cells may experience greater toxicity → dose modification considerations
- Cancer treatment in BS: pediatric oncology protocols with vigilance for excessive toxicity; reduced intensity regimens may be appropriate for hematologic malignancies
- Surveillance: BS Registry follows cancer incidence; annual CBC (leukemia), annual GI endoscopy from ~15y, annual dermatological exam, regular imaging for lymphoma surveillance

## Connections

- `connects-to` → **[Bloom Syndrome](../../07-system/bloom-syndrome/README.md)** — Biallelic BLM LOF → Bloom syndrome via crossover accumulation and SCE elevation (~10x); chromosomal instability → LOH at tumor suppressor loci → pan-cancer predisposition (ALL, lymphoma, GI carcinoma, skin); Bloom Syndrome Registry has tracked >300 patients for >60 years.
- `connects-to` → **[BRCA1](../../03-molecular/brca1/README.md)** — BLM and BRCA1 form a complex at stalled replication forks to suppress aberrant homologous recombination and resolve Holliday junctions; both BLM LOF and BRCA1 LOF result in chromosomal instability and pan-cancer predisposition via distinct but overlapping HR defects.
- `connects-to` → **[WRN](../../03-molecular/wrn/README.md)** — BLM and WRN are both RecQ helicases: BLM resolves double Holliday junctions to suppress crossover (SCE elevated ~10x in BLM LOF); WRN has exonuclease activity and maintains telomeres; BLM LOF → childhood-onset pan-cancer; WRN LOF → adult progeroid syndrome.
- `connects-to` → **[Colorectal Cancer](../../07-system/colorectal-cancer/README.md)** — BLM LOF in Bloom syndrome confers elevated colorectal cancer risk due to crossover-mediated LOH at APC and other CRC tumor suppressor loci; GI carcinomas are among the most common malignancies in adult Bloom syndrome patients; colonoscopy surveillance from early adulthood.
- `connects-to` → **[RAD51](../rad51/README.md)** — BLM acts as both pro- and anti-recombinase for RAD51; BLM-DNA2 promotes DSB end resection → RPA → RAD51 loading; BLM also displaces RAD51 from ssDNA to inhibit crossover; the BLM-RAD51 balance determines HR fidelity and crossover frequency in S/G2.
- `connects-to` → **[ATM](../atm/README.md)** — ATM phosphorylates BLM at Ser646 after DSBs → recruits BLM to γH2AX foci; BLM promotes long-range end resection with DNA2; ATM-BLM axis enables HR in G2; BLM LOF + ionizing radiation → catastrophic chromosomal breakage; BS patients are highly radiosensitive.
- `connects-to` → **[MLH1](../mlh1/README.md)** — BLM interacts with MLH1 (MMR) via its N-terminal region; BLM-MLH1 cooperation suppresses microsatellite instability; BLM unwinds heteroduplex DNA during MMR; some BS GI cancers show MSI-H — dual HR + MMR defect may contribute to extreme GI carcinoma risk.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^ellis-1995-blm-cloning]: Ellis NA, Groden J, Ye TZ, et al. The Bloom's syndrome gene product is homologous to RecQ helicases. *Cell.* 1995;83(4):655-666. [doi:10.1016/0092-8674(95)90105-1](https://doi.org/10.1016/0092-8674(95)90105-1) · [PubMed 7585968](https://pubmed.ncbi.nlm.nih.gov/7585968/)
[^german-1997-bloom-cancer]: German J. Bloom's syndrome. XX. The first 100 cancers. *Cancer.* 1997;71(12):4016-4023. [doi:10.1002/1097-0142(19930615)71:12<4016::AID-CNCR18>3.0.CO;2-E](https://doi.org/10.1002/1097-0142(19930615)71:12<4016::AID-CNCR18>3.0.CO;2-E) · [PubMed 9216035](https://pubmed.ncbi.nlm.nih.gov/9216035/)

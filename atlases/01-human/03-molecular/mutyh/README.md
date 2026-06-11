---
schema: human-scale-entry/v1
id: mutyh
name: MUTYH
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "MUTYH (MutY homolog) is a BER glycosylase that removes adenine mispaired with 8-oxoguanine; LOF → G:C→T:A transversions (SBS18) → somatic APC and KRAS mutations; biallelic germline MUTYH = MUTYH-associated polyposis (MAP); monoallelic variants modestly elevate CRC risk."
aliases: ["MUTYH", "MYH", "MutY homolog", "MUTYH glycosylase", "MUTYH MAP", "MUTYH BER", "MUTYH 8-oxoguanine", "MUTYH colorectal cancer", "MUTYH-associated polyposis gene"]
sources:
  - id: al-tassan-2002-mutyh
    type: peer-reviewed
    cite: "Al-Tassan N, Chmiel NH, Maynard J, et al. Inherited variants of MYH associated with somatic G:C→T:A mutations in colorectal tumors. Nat Genet. 2002;30(2):227-232."
    doi: "10.1038/ng828"
    pmid: "11818965"
    url: "https://doi.org/10.1038/ng828"
  - id: sieber-2003-mutyh-map
    type: peer-reviewed
    cite: "Sieber OM, Lipton L, Crabtree M, et al. Multiple colorectal adenomas, classic adenomatous polyposis, and germ-line mutations in MYH. N Engl J Med. 2003;348(9):791-799."
    doi: "10.1056/NEJMoa025283"
    pmid: "12606733"
    url: "https://doi.org/10.1056/NEJMoa025283"
cross_links:
  - target: 01-human/03-molecular/apc
    relation: connects-to
    note: "MUTYH LOF → G:C→T:A transversions at GCA codons → somatic APC mutations (K→N) driving MAP adenomas; MAP adenomas carry somatic APC mutations similar to FAP but induced by MUTYH-mediated oxidative damage; SBS18 mutational signature in MUTYH-deficient tumors."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Biallelic MUTYH germline variants cause ~1% of all CRC and ~5-15% of adenomatous polyposis not explained by APC; MUTYH-deficient CRC has a distinct SBS18 mutational signature (G:C→T:A transversions, often in an oxoG context); right-sided CRC predominates."
  - target: 01-human/07-system/fap
    relation: connects-to
    note: "MAP (biallelic MUTYH) mimics attenuated FAP (APC germline) but has autosomal recessive inheritance, fewer adenomas (10-100 vs >100 in FAP), later CRC onset (40-60s), and includes serrated polyps; genetic testing distinguishes both syndromes in apparent de novo polyposis."
  - target: 01-human/07-system/mutyh-associated-polyposis
    relation: connects-to
    note: "Germline biallelic MUTYH pathogenic variants cause MAP; two founder variants (Y179C and G396D) account for ~80% of Western MAP; monoallelic MUTYH carriers have modestly elevated CRC risk (~1.5-2x); MAP surveillance mimics FAP but with 1-2 year colonoscopy intervals."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "MUTYH LOF → SBS18 G:C→T:A transversions → KRAS G12C at codon 12 (~70% of MAP-CRC); KRAS G12C is rare in sporadic CRC (~5%) but predominates in MAP-CRC; KRAS G12C in CRC should prompt MUTYH germline testing; sotorasib/adagrasib target KRAS G12C in advanced MAP-associated CRC."
  - target: 01-human/03-molecular/msh2
    relation: connects-to
    note: "MUTYH (BER, oxidative G:C→T:A) and MSH2 (MMR, replication errors) are distinct CRC prevention pathways; MAP shows SBS18, not MSI-H (SBS6/15); MAP-CRC is microsatellite-stable → does not qualify for PD-1 blockade based on MMR deficiency — key distinction for immunotherapy."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "SBS18 G:C→T:A transversions from MUTYH LOF can target TP53 codon hotspots (R248: CGC→TGC = Arg248Cys missense) → p53 LOF in MAP adenoma-carcinoma progression; MUTYH-driven APC, KRAS, and TP53 somatic mutations cooperate in MAP-CRC tumorigenesis."
---

# MUTYH

## Overview

**MUTYH** (MutY DNA Glycosylase; formerly MYH) encodes a 535 amino acid (60 kDa) base excision repair (BER) DNA glycosylase that removes **adenine** mispaired with **8-oxoguanine (8-oxoG)**, the most abundant oxidative DNA lesion in mammalian cells. 8-oxoG is produced by reactive oxygen species (ROS) attack on guanine in DNA or dNTP pools; it is a potent pre-mutagenic lesion because replicative DNA polymerases preferentially insert **A** opposite 8-oxoG instead of the correct C, generating A:8-oxoG mispairs that, if left unrepaired, produce permanent **G:C→T:A transversions** after the next replication. MUTYH was discovered through the MutY system of *E. coli* (Michaels 1992) and the human homolog linked to colorectal polyposis by Al-Tassan in 2002. Biallelic germline MUTYH pathogenic variants cause **MUTYH-associated polyposis (MAP)**, the principal autosomal recessive hereditary colorectal cancer syndrome [^al-tassan-2002-mutyh] [^sieber-2003-mutyh-map].

**BER pathway for 8-oxoG:A mispairs — three-enzyme system:**

| Enzyme | Substrate | Product | Gene |
|---|---|---|---|
| OGG1 (Ogg1) | 8-oxoG:C (correct base pair) | Removes 8-oxoG → AP site | OGG1 |
| MUTYH | A:8-oxoG mispair | Removes A from A:8-oxoG → dR:8-oxoG | MUTYH |
| MTH1 (NUDT1) | 8-oxo-dGTP in nucleotide pool | Hydrolyzes 8-oxo-dGTP → monophosphate | NUDT1 |

MUTYH acts in the second line of defense: after OGG1 removes 8-oxoG incorporated by DNA polymerase during synthesis, and after MTH1 sanitizes the dNTP pool, MUTYH corrects the A:8-oxoG mispair that escapes these defenses.

## Structure

### MUTYH protein domains

**N-terminal MutT homolog (MTH) domain (aa 1-65):**
- 8-oxoG recognition element; binds 8-oxoG in the complementary strand using a NUDIX fold
- Provides specificity: MUTYH is only recruited to A:8-oxoG mispairs, not to A:G, A:T, or other mispairs
- Contacts the 8-oxoG nucleotide in the complementary strand via Gln48 (Q48) and Tyr82 (Y82)

**Helix-hairpin-helix (HhH) domain (aa 66-225):**
- Structural scaffold; mediates non-sequence-specific DNA-backbone contacts
- Iron-sulfur cluster (4Fe-4S): coordinated by Cys266, Cys269, Cys272, Cys288; required for DNA binding and structural integrity; functional as electron conduit (charge transport along DNA may help MUTYH locate 8-oxoG lesions)
- Adenine extrusion: HhH inserts into the DNA duplex → flips the mismatched A nucleotide out of the helix into the active site pocket → MUTYH catalytic residue Asp222 (D222) acts as general base → cleaves N-glycosidic bond → AP site

**C-terminal domain (aa 226-535):**
- PCNA-interacting domain (PIP box, aa 497-505): MUTYH-PCNA interaction couples BER to the replication fork; MUTYH acts immediately behind the replication fork to correct newly created A:8-oxoG mispairs
- RPA-binding domain: MUTYH interacts with RPA70 → coordinates BER with single-stranded DNA processing
- 9-1-1 clamp interaction (aa 490-497): the 9-1-1 checkpoint clamp (RAD9-HUS1-RAD1) recruits MUTYH at stalled replication forks

**Pathogenic germline variants:**
- **Y179C** (formerly Y165C, European nomenclature): exon 7; Tyr179Cys; most common Western MAP variant; disrupts 8-oxoG recognition specificity; ~25-35% of MAP alleles in UK/Nordic
- **G396D** (formerly G382D): exon 13; Gly396Asp; second most common; disrupts 4Fe-4S cluster integrity; ~20-25% of MAP alleles in Western Europe
- Together Y179C + G396D account for ~80% of MAP alleles in European-ancestry populations; other pathogenic variants more prevalent in specific ethnic groups (e.g., Japanese, Turkish, Indian populations have different hotspots)
- **Monoallelic (heterozygous) carriers**: not MAP; modestly elevated CRC risk (~1.5-2x population risk, OR ~1.4-1.6); do not require MAP surveillance but may be included in moderate-risk colonoscopy programs

## Function

### MUTYH BER mechanism at A:8-oxoG mispairs

After replication of an 8-oxoG-containing template strand:
1. DNA polymerase δ or ε inserts **A** opposite template 8-oxoG → A:8-oxoG mispair in daughter strand
2. **MUTYH recruited** to replication fork via PCNA PIP box + 9-1-1 clamp; MutSα (MSH2-MSH6) may also recognize the mispair and recruit MUTYH
3. MUTYH flips the **A** nucleotide into the active site cavity (base flipping); D222 catalyzes cleavage of A N-glycosidic bond → AP site (apurinic site) in daughter strand
4. **APE1** (AP endonuclease 1) incises the DNA backbone 5' to the AP site → 5' deoxyribose phosphate flap
5. **DNA polymerase δ or β** fills in the gap with the correct **C** nucleotide (using 8-oxoG-containing template before OGG1 repair)
6. **Flap endonuclease FEN1** removes the 5' flap; **DNA ligase I or III** seals the nick → restored G:C base pair (8-oxoG still in template, removed by OGG1 subsequently)

### MUTYH LOF → SBS18 mutational signature

When MUTYH is absent (biallelic LOF):
- A:8-oxoG mispairs persist → next replication → A becomes template → T:A inserted → permanent **G:C→T:A transversion** in the strand that originally had G
- Transcribed strand: original G → T:A transversion appears as C:A→A:T on sequencing (same event, different strand notation)
- **COSMIC SBS18** (signature SBS18): dominant in MAP tumors; characterized by G[C>A]N context with enrichment in CpCpA, TpCpT trinucleotide context; formally called "MUTYH deficiency signature" or "oxidative damage signature"
- Also: **SBS36** (alternative oxidative signature) seen in some MAP tumors
- SBS18 is biologically distinct from MSI/SBS6/SBS15 (Lynch syndrome) and APOBEC/SBS2/SBS13; genomic profiling can distinguish MAP-associated CRC from MMR-deficient CRC

### Downstream driver mutations caused by MUTYH LOF

With SBS18 active:
- **APC codon mutations**: G:C→T:A at codon AGA→ATA (Arg→Ile), GCA→GTA (Ala→Val), GAA→TAA (Glu→Stop, or K→N depending on codon); APC mutations in MAP tumors are predominantly G:T transversions, distinct from the frameshifts/truncating variants seen in FAP
- **KRAS codon 12**: GGT→TGT (Gly12Cys, G12C); same KRAS G12C transversion seen in MAP-CRC; G12C is unusual in sporadic CRC (more common in NSCLC); presence of G12C in CRC raises suspicion of MUTYH deficiency
- **KRAS codon 12 transversion pattern in MAP**: ~70% of MAP-CRC have KRAS G12C (vs ~5% of sporadic CRC)

## Mechanism

### Clinical approach to MUTYH testing

**When to test:**
- Attenuated polyposis: 10-100 colorectal adenomas, no known APC/POLE/POLD1 pathogenic variant → sequence MUTYH (both alleles)
- CRC in setting of polyp family history but no dominant inheritance pattern (autosomal recessive pattern: affected siblings with unaffected parents, consanguinity)
- CRC with SBS18 dominant mutational signature on somatic tumor profiling → prompt germline testing
- Duodenal polyposis without APC germline pathogenic variant

**Testing strategy:**
- Sequence both MUTYH alleles (bi-directional Sanger or NGS panel)
- If Y179C or G396D on one allele: search for a second pathogenic variant (may miss compound heterozygotes)
- MLPA if large deletion suspected
- Monoallelic finding: moderate risk; recommend to first-degree relatives

**Functional interpretation:**
- Biallelic pathogenic variants (compound heterozygous or homozygous): MAP → intensive surveillance
- Monoallelic pathogenic variant: no MAP; modest risk; colonoscopy from age 40 every 3-5 years
- VUS in MUTYH: functional BER assays (A:8-oxoG repair) or computational protein modeling used for classification

## Connections

- `connects-to` → **[APC](../../03-molecular/apc/README.md)** — MUTYH LOF → G:C→T:A transversions at GCA codons → somatic APC mutations (K→N) driving MAP adenomas; MAP adenomas carry somatic APC mutations similar to FAP but induced by MUTYH-mediated oxidative damage; SBS18 mutational signature in MUTYH-deficient tumors.
- `connects-to` → **[Colorectal Cancer](../../07-system/colorectal-cancer/README.md)** — Biallelic MUTYH germline variants cause ~1% of all CRC and ~5-15% of adenomatous polyposis not explained by APC; MUTYH-deficient CRC has a distinct SBS18 mutational signature (G:C→T:A transversions, often in an oxoG context); right-sided CRC predominates.
- `connects-to` → **[FAP](../../07-system/fap/README.md)** — MAP (biallelic MUTYH) mimics attenuated FAP (APC germline) but has autosomal recessive inheritance, fewer adenomas (10-100 vs >100 in FAP), later CRC onset (40-60s), and includes serrated polyps; genetic testing distinguishes both syndromes in apparent de novo polyposis.
- `connects-to` → **[MUTYH-Associated Polyposis](../../07-system/mutyh-associated-polyposis/README.md)** — Germline biallelic MUTYH pathogenic variants cause MAP; two founder variants (Y179C and G396D) account for ~80% of Western MAP; monoallelic MUTYH carriers have modestly elevated CRC risk (~1.5-2x); MAP surveillance mimics FAP but with 1-2 year colonoscopy intervals.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — MUTYH LOF → SBS18 G:C→T:A transversions → KRAS G12C at codon 12 (~70% of MAP-CRC); KRAS G12C is rare in sporadic CRC (~5%) but predominates in MAP-CRC; KRAS G12C in CRC should prompt MUTYH germline testing; sotorasib/adagrasib target KRAS G12C in advanced MAP-associated CRC.
- `connects-to` → **[MSH2](../../03-molecular/msh2/README.md)** — MUTYH (BER, oxidative G:C→T:A) and MSH2 (MMR, replication errors) are distinct CRC prevention pathways; MAP shows SBS18, not MSI-H (SBS6/15); MAP-CRC is microsatellite-stable → does not qualify for PD-1 blockade based on MMR deficiency — key distinction for immunotherapy.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — SBS18 G:C→T:A transversions from MUTYH LOF can target TP53 codon hotspots (R248: CGC→TGC = Arg248Cys missense) → p53 LOF in MAP adenoma-carcinoma progression; MUTYH-driven APC, KRAS, and TP53 somatic mutations cooperate in MAP-CRC tumorigenesis.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^al-tassan-2002-mutyh]: Al-Tassan N, Chmiel NH, Maynard J, et al. Inherited variants of MYH associated with somatic G:C→T:A mutations in colorectal tumors. *Nat Genet.* 2002;30(2):227-232. [doi:10.1038/ng828](https://doi.org/10.1038/ng828) · [PubMed 11818965](https://pubmed.ncbi.nlm.nih.gov/11818965/)
[^sieber-2003-mutyh-map]: Sieber OM, Lipton L, Crabtree M, et al. Multiple colorectal adenomas, classic adenomatous polyposis, and germ-line mutations in MYH. *N Engl J Med.* 2003;348(9):791-799. [doi:10.1056/NEJMoa025283](https://doi.org/10.1056/NEJMoa025283) · [PubMed 12606733](https://pubmed.ncbi.nlm.nih.gov/12606733/)

---
schema: human-scale-entry/v1
id: caspase-3
name: Caspase-3
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Executioner caspase of apoptosis; cleaves PARP, lamins, and hundreds of substrates → orderly cell dismantling. Activated by intrinsic (cytochrome c → caspase-9) and extrinsic (FasL → caspase-8) pathways; BCL-2 and IAPs suppress caspase-3 to evade apoptosis in cancer."
aliases: ["CASP3", "CPP32", "apopain", "executioner caspase", "SCA-1", "Yama"]
sources:
  - id: nicholson-1997-caspase-review
    type: peer-reviewed
    cite: "Nicholson DW, Thornberry NA. Caspases: killer proteases. Trends Biochem Sci. 1997;22(8):299-306."
    doi: "10.1016/S0968-0004(97)01085-2"
    pmid: "9270303"
    url: "https://doi.org/10.1016/S0968-0004(97)01085-2"
  - id: taylor-2008-apoptosis-review
    type: peer-reviewed
    cite: "Taylor RC, Cullen SP, Martin SJ. Apoptosis: controlled demolition at the cellular level. Nat Rev Mol Cell Biol. 2008;9(3):231-241."
    doi: "10.1038/nrm2312"
    pmid: "18073771"
    url: "https://doi.org/10.1038/nrm2312"
  - id: porter-1999-caspase-mechanisms
    type: peer-reviewed
    cite: "Porter AG, Jänicke RU. Emerging roles of caspase-3 in apoptosis. Cell Death Differ. 1999;6(2):99-104."
    doi: "10.1038/sj.cdd.4400476"
    pmid: "10200555"
    url: "https://doi.org/10.1038/sj.cdd.4400476"
cross_links:
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "BCL-2 inhibits caspase-3 activation by sequestering BAX/BAK → preventing cytochrome c release and apoptosome formation; BCL-2 overexpression is the primary mechanism of caspase-3 suppression in lymphoma and CLL; venetoclax (BCL-2 inhibitor) restores caspase-3 activation."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "p53 activates caspase-3-dependent apoptosis via transcriptional induction of PUMA, NOXA, and BAX → BAX/BAK → cytochrome c → apoptosome → caspase-9 → caspase-3; p53 also directly activates BAX by binding mitochondria; p53 loss → caspase-3 suppression → therapy resistance."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "NLRP3 activates caspase-1 (pyroptotic caspase) rather than caspase-3; however, pyroptosis and caspase-3 apoptosis are interconnected — gasdermin D (caspase-1 substrate) can activate caspase-3 in certain contexts; caspase-3 also cleaves gasdermin E (DFNA5) → secondary pyroptosis."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "AKT phosphorylates caspase-9 Ser196 → inhibits caspase-9 → reduces caspase-3 activation; AKT also phosphorylates and inhibits BAD → anti-apoptotic; AKT-driven caspase-3 suppression is a key survival mechanism in PI3K-mutant and PTEN-null tumors."
  - target: 01-human/07-system/cll
    relation: connects-to
    note: "BCL-2 overexpression in CLL sequesters BAX/BAK → suppresses caspase-3; venetoclax (BCL-2 inhibitor) releases BAX → MOMP → caspase-9 → caspase-3 → rapid tumor lysis; venetoclax+obinutuzumab is preferred frontline CLL therapy achieving 57% uMRD (CLL14 trial)."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Venetoclax + azacitidine restores caspase-3 in AML blasts; MCL-1 overexpression is the primary resistance mechanism; p53 loss blunts caspase-3 activation; VIALE-A: venetoclax+aza 65% CR/CRi vs 19% with azacitidine alone in elderly/unfit AML."
  - target: 01-human/07-system/multiple-myeloma
    relation: connects-to
    note: "BCL-2, BCL-XL, and MCL-1 suppress caspase-3 in multiple myeloma; venetoclax is active in t(11;14) MM (high BCL-2); navitoclax adds BCL-XL inhibition; MCL-1 inhibitors address MM-specific resistance; IMid and proteasome inhibitor efficacy converges on caspase-3 activation."
---

# Caspase-3

## Overview

**Caspase-3 (CASP3)** is the **central executioner caspase** in mammalian apoptosis — the serine/cysteine aspartate-specific protease responsible for cleaving the vast majority of apoptotic substrates that dismantle the dying cell in an orderly, immunologically silent manner [^nicholson-1997-caspase-review]. Unlike the **initiator caspases** (caspase-8, caspase-9, caspase-10) that are activated by upstream death signals, caspase-3 is a **downstream amplifier and effector** that once activated, irreversibly commits the cell to death.

**The caspase family (human, 12 members):**
- **Initiator caspases:** Caspase-8, -10 (extrinsic/death receptor pathway); caspase-9 (intrinsic/mitochondrial pathway); caspase-2 (DNA damage-induced, upstream of mitochondria)
- **Executioner caspases:** **Caspase-3 (dominant effector)**, caspase-6, caspase-7 (PARP and lamin substrates; minor roles)
- **Inflammatory caspases:** Caspase-1, -4, -5, -11 (human/mouse) → IL-1beta, IL-18, gasdermin D (pyroptosis)

**Why caspase-3 is the central executioner:**
- Caspase-3 cleaves >300 identified substrates including PARP-1 (DNA repair inhibition, nuclear fragmentation hallmark), lamin A/B/C (nuclear lamina breakdown), ICAD/DFF45 (releases CAD DNase → internucleosomal DNA fragmentation → "DNA ladder"), gelsolin → actin cytoskeleton cleavage → membrane blebbing; collectively: the morphological hallmarks of apoptosis
- Cross-amplification: caspase-3 activates upstream caspase-8 and -9 (feedback loop) → signal amplification; also cleaves and activates caspase-6 → nuclear lamina disruption

**Apoptosis as a cancer therapeutic target:**
- Evasion of apoptosis is a hallmark of cancer; most chemotherapy and targeted therapy drugs kill cancer cells ultimately through caspase-3 activation; BCL-2/BCL-XL overexpression, IAP overexpression, and p53 mutation are the three major mechanisms cancers use to suppress caspase-3 — and all three are now druggable targets

## Structure

### Caspase-3 protein structure and activation [^taylor-2008-apoptosis-review]

Caspase-3 is a **cysteine protease** that cleaves after aspartate residues (DEVD specificity; DEVD-AMC is the fluorescent substrate used in caspase-3 activity assays).

**Domain architecture:**
- **Prodomain:** Short (29 aa); unlike initiator caspases which have long CARD or DED prodomains for adaptor recruitment, caspase-3 prodomain is minimal and does not mediate direct upstream recruitment
- **Large subunit (p17):** Contains active site Cys163 (nucleophile), His121 (general acid/base); adjacent L3 loop → substrate specificity (DEVD preference)
- **Small subunit (p12):** Allosteric regulation; forms the interdomain linker-cleaved product after caspase-9/8 processing

**Processing and activation:**
- Pro-caspase-3 is a 32 kDa zymogen → inactive (low basal activity)
- Initiator caspase-9 (intrinsic) or caspase-8 (extrinsic) cleaves the interdomain linker (Asp175 cleavage → p17+p12) → releases active caspase-3 heterotetramer (2×p17 + 2×p12)
- Caspase-3 is fully active as a dimer: allosteric dimerization is required for full catalytic activity; XIAP and survivin block active caspase-3 by obstructing the active site

**Inhibition of caspase-3 in normal and cancer cells:**
- **XIAP (X-linked inhibitor of apoptosis):** BIR2 domain directly inserts into caspase-3 active site → competitive inhibition; XIAP is the only IAP that directly inhibits caspase-3 and -7 (other IAPs inhibit upstream caspase-9 or activate NF-kB); XIAP overexpressed in many cancer types → caspase-3 blockade → chemoresistance
- **Survivin (BIRC5):** IAP family member; overexpressed in virtually all cancers, absent in most normal adult tissues; associates with activated caspase-3 and -9 → inhibition; simultaneously regulates mitotic spindle assembly (chromosomal passenger complex); dual function makes it an attractive therapeutic target
- **FLIP (c-FLIP, CASP8 and FADD-like apoptosis regulator):** DED-domain protein competing with caspase-8 for DISC (death-inducing signaling complex) → blocks extrinsic pathway → prevents caspase-3 activation via extrinsic route; overexpressed in many cancer types

### Intrinsic (mitochondrial) pathway to caspase-3

1. Apoptotic stimuli (DNA damage, ER stress, growth factor withdrawal, oncogene activation, cytotoxic drugs) → p53 → PUMA/NOXA/BAX transcription → BAX conformational change → BAX/BAK oligomerization → MOMP (mitochondrial outer membrane permeabilization)
2. Cytochrome c release → binds Apaf-1 WD40 domain → conformational change → dATP-driven apoptosome assembly (7×Apaf-1 + 7×cytochrome c wheel) → recruits caspase-9 via CARD domains → caspase-9 activation
3. Activated caspase-9 → cleaves and activates caspase-3 → irreversible apoptosis execution

**BCL-2 family controls MOMP (caspase-3 checkpoint):**
- **Pro-apoptotic effectors (BAX, BAK):** Pore-forming; required for MOMP
- **Pro-apoptotic BH3-only (PUMA, NOXA, BID, BAD, BIM, HRK):** Activate BAX/BAK or neutralize anti-apoptotic BCL-2 proteins
- **Anti-apoptotic (BCL-2, BCL-XL, MCL-1):** Sequester BAX/BAK and BH3-only proteins → prevent MOMP → suppress caspase-3; target of venetoclax (BCL-2), navitoclax (BCL-2/XL), and MCL-1 inhibitors (AZD5991)

### Extrinsic (death receptor) pathway to caspase-3

1. Death ligands (FasL/CD95L, TRAIL, TNF) bind death receptors (FAS, TRAIL-R1/R2, TNFR1) → DISC formation → caspase-8 dimerization and activation
2. **Type I cells (lymphocytes, hepatocytes in some contexts):** Caspase-8 directly cleaves caspase-3 → sufficient for apoptosis without mitochondrial amplification
3. **Type II cells (most solid tumor cells):** Caspase-8 → truncated BID (tBID) → BAX/BAK → cytochrome c → apoptosome → caspase-9 → caspase-3 (mitochondrial amplification loop required); BCL-2 overexpression in Type II cells → TRAIL and FasL resistance

## Function

### Caspase-3 substrates and apoptosis morphology [^porter-1999-caspase-mechanisms]

**Nuclear substrates:**
- **PARP-1 (poly ADP-ribose polymerase 1):** Cleaved at DEVD↓G → 85 kDa + 24 kDa fragments; diagnostic hallmark of caspase-3 activation (cleaved PARP on Western blot); inactivation prevents energy depletion from ADP-ribosylation → orderly versus necrotic death
- **ICAD/DFF45:** Caspase-3 cleavage releases CAD (caspase-activated DNase) from ICAD repression → CAD translocates to nucleus → internucleosomal DNA cleavage → ~180 bp DNA ladder on gel → apoptotic DNA fragmentation
- **Lamins A, B, C:** Nuclear lamina disassembly → nuclear condensation and blebbing; lamin cleavage is a diagnostic marker of advanced apoptosis

**Cytoplasmic/cytoskeletal substrates:**
- **Gelsolin:** Activated caspase-3 fragment constitutively cleaves actin → membrane blebbing independent of upstream signaling; positive feedback amplifier
- **Focal adhesion kinase (FAK):** Cleavage → detachment from extracellular matrix → anoikis-like signaling
- **MDM2:** Caspase-3 cleaves MDM2 → generates fragment that no longer suppresses p53 → p53 activation → transcriptional amplification of apoptotic signals (p53-caspase-3 positive feedback)
- **RB (retinoblastoma protein):** Caspase-3 cleavage → removes E2F repression → pro-apoptotic E2F target gene activation

**Kinase/phosphatase substrates (caspase-3 disables survival signaling):**
- **AKT:** Cleaved by caspase-3 during late apoptosis → complete shut-off of PI3K-AKT survival signaling
- **RAF1, RAS-GEF (SOS):** Caspase-3 cleavage → disables RAS-ERK survival cascade
- **PKB, PKC isoforms:** Multiple pro-survival kinases are caspase-3 substrates → ensuring commitment to death

### Non-apoptotic roles of caspase-3 (sublethal activation)

Transient, sublethal caspase-3 activation (without full MOMP or XIAP saturation) has emerging roles:
- **Inflammation:** Caspase-3 → gasdermin E (DFNA5) cleavage → pyroptosis pore → IL-1alpha release (distinct from caspase-1/gasdermin D pyroptosis)
- **Stem cell differentiation:** Transient caspase-3 activation in stem cells → activates iPLA2 → prostaglandin E2 → Wnt/beta-catenin → stemness maintenance (apoptosis-induced proliferation / "phoenix rising")
- **Bone remodeling:** Osteoclast and osteoblast regulation via sublethal caspase-3 activity

## Mechanism

### Therapeutic exploitation of caspase-3

**BH3 mimetics → restore caspase-3 activation:**
- **Venetoclax (ABT-199, BCL-2 selective):** Releases BAX from BCL-2 → MOMP → caspase-9 → caspase-3; approved for CLL, AML, multiple myeloma (in combination); the paradigm for "priming" tumor cells for caspase-3-dependent death
- **Navitoclax (ABT-263, BCL-2/BCL-XL):** Adds BCL-XL inhibition → broader apoptosis activation; thrombocytopenia limits dosing (platelets require BCL-XL)
- **MCL-1 inhibitors (AZD5991, AMG-176):** Target MCL-1 (which venetoclax doesn't inhibit) → overcome MCL-1-dependent resistance; in clinical trials for AML, myeloma

**SMAC mimetics → restore caspase-3 by neutralizing IAPs:**
- SMAC (second mitochondrial activator of caspases) is released alongside cytochrome c → binds XIAP → relieves XIAP-mediated caspase-3 inhibition; SMAC mimetics (birinapant, LCL-161, xevinapant) mimic SMAC → neutralize cIAP1/2 and XIAP → caspase-3 restoration; Phase 2 in solid tumors

**TRAIL-receptor agonists → extrinsic caspase-3:**
- Recombinant TRAIL (dulanermin) and anti-TRAIL-R1/R2 agonist antibodies (mapatumumab, lexatumumab, tigatuzumab) → activate caspase-8 → caspase-3 in TRAIL-sensitive tumor cells; challenge: Type II tumor cells require mitochondrial amplification for TRAIL killing → combine with BH3 mimetics

**Caspase-3 as a biomarker:**
- Cleaved PARP, cleaved caspase-3 IHC: standard pathology assays for apoptosis in tumor biopsies; used as pharmacodynamic endpoint in oncology trials to verify on-target drug activity

## Connections

- `connects-to` → **[BCL-2](../bcl-2/README.md)** — BCL-2 inhibits caspase-3 activation by sequestering BAX/BAK → preventing cytochrome c release and apoptosome formation; BCL-2 overexpression is the primary mechanism of caspase-3 suppression in lymphoma and CLL; venetoclax (BCL-2 inhibitor) restores caspase-3 activation.
- `connects-to` → **[p53](../p53/README.md)** — p53 activates caspase-3-dependent apoptosis via PUMA, NOXA, and BAX → BAX/BAK → cytochrome c → apoptosome → caspase-9 → caspase-3; p53 also directly activates BAX at the mitochondria; p53 loss → caspase-3 suppression → therapy resistance.
- `connects-to` → **[NLRP3 Inflammasome](../nlrp3-inflammasome/README.md)** — NLRP3 activates caspase-1 (pyroptotic); caspase-3 and caspase-1 pathways intersect: gasdermin D (caspase-1 substrate) can amplify caspase-3 activity; caspase-3 cleaves gasdermin E → secondary pyroptosis and IL-1alpha release.
- `connects-to` → **[AKT](../akt/README.md)** — AKT phosphorylates caspase-9 Ser196 → inhibits caspase-9 → reduces caspase-3 activation; AKT also phosphorylates BAD → anti-apoptotic sequestration; AKT-driven caspase-3 suppression is a key survival mechanism in PI3K-mutant and PTEN-null tumors.
- `connects-to` → **[CLL](../../07-system/cll/README.md)** — BCL-2 overexpression in CLL sequesters BAX/BAK → suppresses caspase-3; venetoclax (BCL-2 inhibitor) releases BAX → MOMP → caspase-9 → caspase-3 → rapid tumor lysis; venetoclax+obinutuzumab is preferred frontline CLL therapy achieving 57% uMRD (CLL14 trial).
- `connects-to` → **[AML](../../07-system/aml/README.md)** — venetoclax + azacitidine restores caspase-3 in AML blasts; MCL-1 overexpression is the primary resistance mechanism; p53 loss blunts caspase-3 activation; VIALE-A: venetoclax+aza 65% CR/CRi vs 19% with azacitidine alone in elderly/unfit AML.
- `connects-to` → **[Multiple Myeloma](../../07-system/multiple-myeloma/README.md)** — BCL-2, BCL-XL, and MCL-1 suppress caspase-3 in multiple myeloma; venetoclax is active in t(11;14) MM (high BCL-2); navitoclax adds BCL-XL inhibition; MCL-1 inhibitors address MM-specific resistance; IMid and proteasome inhibitor efficacy converges on caspase-3 activation.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^nicholson-1997-caspase-review]: Nicholson DW, Thornberry NA. Caspases: killer proteases. *Trends Biochem Sci.* 1997;22(8):299-306. [doi:10.1016/S0968-0004(97)01085-2](https://doi.org/10.1016/S0968-0004(97)01085-2) · [PubMed 9270303](https://pubmed.ncbi.nlm.nih.gov/9270303/)
[^taylor-2008-apoptosis-review]: Taylor RC, Cullen SP, Martin SJ. Apoptosis: controlled demolition at the cellular level. *Nat Rev Mol Cell Biol.* 2008;9(3):231-241. [doi:10.1038/nrm2312](https://doi.org/10.1038/nrm2312) · [PubMed 18073771](https://pubmed.ncbi.nlm.nih.gov/18073771/)
[^porter-1999-caspase-mechanisms]: Porter AG, Jänicke RU. Emerging roles of caspase-3 in apoptosis. *Cell Death Differ.* 1999;6(2):99-104. [doi:10.1038/sj.cdd.4400476](https://doi.org/10.1038/sj.cdd.4400476) · [PubMed 10200555](https://pubmed.ncbi.nlm.nih.gov/10200555/)

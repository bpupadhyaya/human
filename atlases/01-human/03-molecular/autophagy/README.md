---
schema: human-scale-entry/v1
id: autophagy
name: Autophagy
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Lysosomal self-digestion pathway; ULK1 initiates phagophore formation, LC3 lipidation seals it, SQSTM1/p62 links ubiquitinated cargo. mTORC1 suppresses; AMPK activates. Roles in cancer survival, neurodegeneration, immunity, and antibiotic resistance via xenophagy."
aliases: ["macroautophagy", "autophagy pathway", "ULK1 pathway", "LC3-mediated autophagy", "mitophagy"]
sources:
  - id: mizushima-2011-autophagy
    type: peer-reviewed
    cite: "Mizushima N, Yoshimori T, Ohsumi Y. The role of Atg proteins in autophagosome formation. Annu Rev Cell Dev Biol. 2011;27:107-132."
    doi: "10.1146/annurev-cellbio-092910-154005"
    pmid: "21801009"
    url: "https://doi.org/10.1146/annurev-cellbio-092910-154005"
  - id: levine-2019-autophagy-immunity
    type: peer-reviewed
    cite: "Levine B, Mizushima N, Virgin HW. Autophagy in immunity and inflammation. Nature. 2011;469(7330):323-335."
    doi: "10.1038/nature09782"
    pmid: "21248839"
    url: "https://doi.org/10.1038/nature09782"
  - id: galluzzi-2015-autophagy-cancer
    type: peer-reviewed
    cite: "Galluzzi L, Pietrocola F, Bravo-San Pedro JM, et al. Autophagy in malignant transformation and cancer progression. EMBO J. 2015;34(7):856-880."
    doi: "10.15252/embj.201490784"
    pmid: "25712477"
    url: "https://doi.org/10.15252/embj.201490784"
cross_links:
  - target: 01-human/03-molecular/mtor
    relation: modulated-by
    note: "mTORC1 is the master negative regulator of autophagy; nutrient-rich: mTORC1 phosphorylates ULK1 (Ser757) → ULK1 inactivated; starvation: mTORC1 off → ULK1 activated → autophagy initiation; rapamycin/everolimus induce autophagy by relieving mTORC1 suppression of ULK1."
  - target: 01-human/03-molecular/ampk
    relation: modulated-by
    note: "AMPK directly phosphorylates ULK1 (Ser317, Ser777) → activates autophagy initiation; AMPK also inhibits mTORC1 (via TSC2 and Raptor) → further relieves ULK1 repression; the AMPK→ULK1 and AMPK-mTORC1-ULK1 axes both converge to couple energy stress to autophagy induction."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "BCL-2 and BCL-XL sequester Beclin-1 (autophagy initiation factor) through BH3-domain interaction → inhibit autophagosome nucleation; BH3-only proteins (PUMA, BAD) displace Beclin-1 from BCL-2 → activate autophagy; venetoclax releases Beclin-1 → autophagy induction in tumor cells."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "p53 regulates autophagy in a compartment-specific and context-dependent manner: nuclear p53 transcriptionally activates DRAM1 and sestrin2 → promote autophagy; cytoplasmic p53 inhibits autophagy by sequestering FIP200; p53 loss can promote basal autophagy in KRAS-mutant tumors."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "PINK1/Parkin mitophagy is central to Parkinson disease; PINK1 accumulates on depolarized mitochondria, activates Parkin E3 ligase, ubiquitinates OMM proteins, and recruits p62/optineurin for mitophagy; PINK1 or Parkin LOF → impaired mitophagy → ROS → dopaminergic neuron death."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "KRAS-mutant tumors (especially PDAC) are highly autophagy-dependent; KRAS sustains autophagic flux for amino acid recycling in nutrient-poor microenvironments; HCQ + KRAS G12C inhibitors show preclinical synergy; ATG7 deletion in KRAS-driven mouse tumors causes regression."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophage xenophagy captures intracellular pathogens (Mycobacterium tuberculosis, Salmonella) in LC3+ vacuoles for lysosomal killing; autophagy degrades NLRP3 and mtDNA-releasing mitochondria → limits inflammasome hyperactivation; beclin-1 directly binds and suppresses cGAS."
---

# Autophagy

## Overview

**Autophagy** (from Greek: "self-eating") is a conserved lysosomal degradation pathway through which cells recycle damaged organelles, misfolded proteins, and surplus cytoplasmic material — balancing cellular homeostasis, adaptation to nutrient stress, and quality control. Discovered through seminal work by **Yoshinori Ohsumi** (2016 Nobel Prize in Physiology or Medicine), who identified the essential autophagy (Atg) genes in yeast by screening for autophagy-defective mutants under starvation conditions.

Three forms of autophagy exist in mammalian cells:
- **Macroautophagy (commonly "autophagy"):** Formation of a double-membrane **phagophore** that expands to engulf cytoplasmic cargo → **autophagosome** → fusion with lysosome → **autolysosome** → cargo degradation by lysosomal hydrolases → amino acids, fatty acids, nucleotides released back to cytoplasm
- **Microautophagy:** Direct invagination of lysosomal membrane around cytoplasmic material; less characterized in mammals
- **Chaperone-mediated autophagy (CMA):** Selective degradation of proteins bearing a KFERQ motif via HSC70 and LAMP-2A (lysosomal receptor); upregulated in prolonged starvation and neurodegeneration

**Selective autophagy** degrades specific cargo through adaptor proteins (receptors) that simultaneously bind ubiquitinated cargo and LC3/GABARAP on the phagophore:
- **Mitophagy:** Damaged mitochondria (PINK1/Parkin pathway; NIX/BNIP3L in developmental mitophagy)
- **Lysophagy:** Damaged lysosomes (galectins, ubiquitin)
- **ER-phagy:** ER fragments (FAM134B, RTN3)
- **Xenophagy:** Intracellular pathogens (bacteria, viruses)
- **Aggrephagy:** Protein aggregates (SQSTM1/p62, NBR1, HDAC6)

## Structure

### The autophagy initiation complex (ULK1 complex) [^mizushima-2011-autophagy]

Autophagy is initiated by the **ULK1/2 (unc-51-like kinase 1/2) complex**:
- **ULK1/2 (Atg1 homolog):** The initiating serine/threonine kinase; phosphorylated and activated by AMPK (Ser317, Ser777) and inhibited by mTORC1 (Ser757); when active → phosphorylates Beclin-1, ATG14, ATG13, FIP200
- **ATG13:** ULK1-binding partner; phosphorylated by mTORC1 → dissociates from ULK1 (OFF); when mTORC1 inactive → ATG13 in complex → ULK1 stabilized and active
- **FIP200 (RB1CC1):** ULK1-binding partner; essential for autophagosome formation
- **ATG101:** Stabilizes ATG13 in the complex

**The PI3K complex (Beclin-1 complex):**
After ULK1 activation, the **class III PI3K (VPS34) complex** is recruited to the phagophore initiation site:
- **VPS34 (PIK3C3):** Lipid kinase; produces PI3P (phosphatidylinositol 3-phosphate) → recruits WIPI2 → recruits the ATG12–ATG5–ATG16L1 conjugation system
- **Beclin-1 (BECN1):** Scaffold and autophagic regulator; contains BH3-like domain (binding site for BCL-2/BCL-XL inhibition); also binds UVRAG, Rubicon (inhibitory), and AMBRA1 (activating)
- **ATG14/Barkor:** Directs VPS34 complex to phagophore membranes (ER-associated)

### LC3 lipidation: the autophagosome marker [^mizushima-2011-autophagy]

LC3 (microtubule-associated protein 1A/1B light chain 3, Atg8 homolog) lipidation is the hallmark event of autophagosome formation:

1. **ATG12-ATG5-ATG16L1 conjugation system:**
   - ATG12 conjugated to ATG5 (by ATG7 [E1-like] and ATG10 [E2-like]) → ATG12–ATG5 complex → forms oligomeric complex with ATG16L1
   - ATG16L1 complex localizes to phagophore outer membrane → acts as E3-like enzyme for LC3 lipidation

2. **LC3 lipidation cascade:**
   - Pro-LC3 → cleaved by ATG4 cysteine protease → cytosolic LC3-I (with free C-terminal glycine)
   - ATG7 (E1) → ATG3 (E2) → LC3-I coupled to phosphatidylethanolamine (PE) on the phagophore membrane → **LC3-II** (lipidated, membrane-associated)
   - LC3-II remains on autophagosome membrane → hallmark of autophagosomes in immunofluorescence and Western blot (shifts from 16 to 14 kDa)
   - LC3-II on outer membrane is removed by ATG4 after fusion with lysosome; inner membrane LC3-II is degraded with cargo

3. **Cargo receptors:** SQSTM1/p62, NBR1, OPTN, NDP52, TAX1BP1 — bind polyubiquitinated cargo AND LC3-II simultaneously → bridge cargo to autophagosome → selective degradation

## Function

### Autophagy in cellular homeostasis

**Nutrient recycling (starvation response):**
- Glucose/amino acid deprivation → AMPK activation + mTORC1 inactivation → ULK1 active → autophagy → cytoplasmic material degraded → amino acids (via lysosomes → lysosomal amino acid transporter) → mTORC1 reactivated (amino acid sensing at lysosome via Ragulator/GATOR) → autophagy terminates (negative feedback loop)
- This "self-eating" provides essential amino acids and energy for survival during starvation

**Organelle quality control:**
- **Mitophagy:** PINK1 accumulates on depolarized (damaged) mitochondria (normally translocated into mitochondria and degraded by matrix proteases; in damaged mito → no import → accumulates on outer membrane) → PINK1 phosphorylates Parkin (E3 ubiquitin ligase) → Parkin ubiquitinates OMM proteins → p62/optineurin/NDP52 bind Ub chains → phagophore engulfs → mitophagy
  - **Parkinson's disease:** PINK1 and Parkin mutations → impaired mitophagy → damaged mitochondria accumulate in dopaminergic neurons → ROS → neurodegeneration

**Proteostasis:**
- Misfolded proteins (e.g., polyglutamine expansions in Huntington's disease, mutant SOD1 in ALS, tau in Alzheimer's) aggregated in cytoplasm → SQSTM1/p62-mediated aggrephagy; rapamycin-induced autophagy reduces polyQ aggregates in HD cell and mouse models → neuroprotective

### Autophagy in cancer: dual roles [^galluzzi-2015-autophagy-cancer]

Autophagy plays paradoxical roles in cancer — both tumor suppressive and tumor promoting:

**Tumor suppression (pre-malignant stage):**
- Autophagy eliminates damaged organelles (mitochondria) that produce ROS → ROS-driven genome instability; also eliminates oncogenic proteins
- Beclin-1 (BECN1) is monoallelically deleted in ~50-70% of breast, ovarian, and prostate cancers → haploinsufficiency → reduced autophagy → accumulation of p62 aggregates → NRF2 activation → cancer promotion
- BECN1-heterozygous mice spontaneously develop hepatocellular carcinoma and lymphoma

**Tumor promotion (established tumors):**
- Established tumors (KRAS-mutant PDAC especially) depend on autophagy for survival under metabolic stress: macropinocytosis + autophagy = dominant amino acid supply mechanisms in nutrient-poor PDAC microenvironment
- Autophagy promotes survival under anoikis (anchorage-independent), chemotherapy-induced ER stress, and anti-cancer drug treatment → resistance
- Selective autophagy degrades anti-tumor proteins: AMBRA1-mediated degradation of cyclin D → promotes S-phase entry; p62-mediated KEAP1 sequestration → NRF2 → antioxidant → drug resistance

**KRAS-mutant tumor autophagy dependency:**
- Oncogenic KRAS drives both mTORC1 activation (anti-autophagy) and LC3-II flux (pro-autophagy) — balanced toward sustained basal autophagy
- Chloroquine/hydroxychloroquine (lysosome acidification inhibitors → block autolysosome maturation) + KRAS inhibitors (sotorasib) show synergistic activity in NSCLC
- ATG7 deletion in KRAS-driven mouse lung tumors → tumor regression (synthetic lethal in established cancer) but → benign oncocytomas (mitophagy-defective mitochondria accumulation) — confirms context-dependence

### Autophagy in immunity [^levine-2019-autophagy-immunity]

- **Xenophagy:** LC3-associated phagocytosis (LAP) captures phagocytosed bacteria in LC3+ single-membrane vacuoles → lysosomal degradation; targets: Mycobacterium tuberculosis, Salmonella, Group A Streptococcus
- **Antigen presentation:** Autophagy degrades cytoplasmic proteins into peptides → presented on MHC class II → CD4+ T cell activation; critical for steady-state MHC-II loading in thymic dendritic cells → central tolerance
- **Inflammasome regulation:** Autophagy degrades NLRP3 and mitochondria that release mtDNA (activates NLRP3) → limits inflammasome hyperactivation → anti-inflammatory autophagy function
- **cGAS-STING clearance:** Cytoplasmic DNA sensed by cGAS → STING → IFN-β; autophagy degrades cytoplasmic DNA and damaged mitochondria → limits cGAS-STING over-activation; beclin-1 directly binds cGAS → suppresses cGAS activity

## Mechanism

### Autophagy regulation: nutrient and energy sensing

**Amino acid sensing (lysosomal):**
- Amino acids (especially leucine, arginine) → sensed in the lysosomal lumen by SLC38A9, CASTOR1 (arginine sensor), Sestrin2 (leucine sensor) → GATOR1/2 complexes → Ragulator → RagA/B-GTP loaded → mTORC1 recruited to lysosome surface → mTORC1 active → ULK1 phospho-inhibited → autophagy suppressed
- Starvation → amino acids fall → GATOR1 activates → RagA/B-GDP → mTORC1 leaves lysosome → mTORC1 inactive → ULK1 active → autophagy induced
- This lysosomal amino acid sensing directly couples the end product of autophagy (amino acids from degradation) to its own suppression — elegant negative feedback

**Lipid sensing via PI3P:**
- PI3P (generated by VPS34 at phagophore initiation site) recruits WIPI2 (WD repeat protein interacting with phosphoinositides) → WIPI2 recruits ATG12-ATG5-ATG16L1 complex → LC3 lipidation at nascent phagophore → expansion

### Pharmacological autophagy modulation

**Autophagy inducers:**
- **Rapamycin/everolimus:** mTORC1 inhibition → ULK1 dephosphorylation → autophagy; used to induce autophagy in HD, Parkinson's (preclinical); anti-aging via autophagy enhancement
- **AMPK activators (metformin, AICAR):** AMPK → ULK1 Ser317/777 phosphorylation → autophagy initiation independent of mTOR
- **Starvation/caloric restriction:** Robust autophagy inducer; responsible for much of caloric restriction's lifespan extension

**Autophagy inhibitors (therapeutic relevance):**
- **Chloroquine (CQ)/Hydroxychloroquine (HCQ):** Accumulate in lysosomes → alkalinize lumen (normally pH 4.5-5.0) → impair lysosomal hydrolase activity → autophagosome accumulation → autophagic flux blocked; FDA-approved for malaria/rheumatology; in clinical trials for autophagy-dependent cancers (KRAS-mutant PDAC, melanoma)
- **Bafilomycin A1:** V-ATPase inhibitor → blocks lysosomal acidification; research tool, not clinical

**Clinical trials — autophagy inhibition in cancer:**
- HCQ + gemcitabine/abraxane in metastatic PDAC: Phase II (SWOG 1521) — modest activity
- HCQ + mTOR inhibitor in RCC: Phase II — superior to single-agent mTOR
- HCQ + BRAF/MEK inhibitor in melanoma: Phase II — ongoing
- HCQ + chloroquine + sorafenib: Phase II in HCC

## Connections

- `modulated-by` → **[mTOR](../mtor/README.md)** — mTORC1 phosphorylates ULK1 (Ser757) → autophagy suppressed under nutrient-rich conditions; mTORC1 inactivation (starvation, rapamycin) → ULK1 active → autophagy initiation; mTOR is the master autophagy repressor.
- `modulated-by` → **[AMPK](../ampk/README.md)** — AMPK directly activates ULK1 (Ser317/777) under energy stress; AMPK also inhibits mTORC1 → further promotes autophagy; the AMPK-mTOR-ULK1 axis couples cellular energy state to autophagic flux.
- `connects-to` → **[BCL-2](../bcl-2/README.md)** — BCL-2 and BCL-XL sequester Beclin-1 at the BH3 domain → inhibit autophagosome nucleation; BH3-only proteins and venetoclax displace Beclin-1 → activate autophagy; BCL-2 family members regulate both apoptosis and autophagy via the same BH3-binding groove.
- `connects-to` → **[p53](../p53/README.md)** — nuclear p53 activates autophagy genes (DRAM1, sestrin2) after DNA damage; cytoplasmic p53 inhibits autophagy; p53 loss alters basal autophagy; KRAS-mutant/p53-null tumors (PDAC) show extreme autophagy dependence for nutrient recycling.
- `connects-to` → **[Parkinson's Disease](../../07-system/parkinsons-disease/README.md)** — PINK1/Parkin mitophagy is central to Parkinson disease; PINK1 accumulates on depolarized mitochondria, activates Parkin E3 ligase, ubiquitinates OMM proteins, and recruits p62/optineurin for mitophagy; PINK1 or Parkin LOF → impaired mitophagy → ROS → dopaminergic neuron death.
- `connects-to` → **[KRAS](../kras/README.md)** — KRAS-mutant tumors (especially PDAC) are highly autophagy-dependent; KRAS sustains autophagic flux for amino acid recycling in nutrient-poor microenvironments; HCQ + KRAS G12C inhibitors show preclinical synergy; ATG7 deletion in KRAS-driven mouse tumors causes regression.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — macrophage xenophagy captures intracellular pathogens (Mycobacterium tuberculosis, Salmonella) in LC3+ vacuoles for lysosomal killing; autophagy degrades NLRP3 and mtDNA-releasing mitochondria → limits inflammasome hyperactivation; beclin-1 directly binds and suppresses cGAS.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^mizushima-2011-autophagy]: Mizushima N, Yoshimori T, Ohsumi Y. The role of Atg proteins in autophagosome formation. *Annu Rev Cell Dev Biol.* 2011;27:107-132. [doi:10.1146/annurev-cellbio-092910-154005](https://doi.org/10.1146/annurev-cellbio-092910-154005) · [PubMed 21801009](https://pubmed.ncbi.nlm.nih.gov/21801009/)
[^levine-2019-autophagy-immunity]: Levine B, Mizushima N, Virgin HW. Autophagy in immunity and inflammation. *Nature.* 2011;469(7330):323-335. [doi:10.1038/nature09782](https://doi.org/10.1038/nature09782) · [PubMed 21248839](https://pubmed.ncbi.nlm.nih.gov/21248839/)
[^galluzzi-2015-autophagy-cancer]: Galluzzi L, Pietrocola F, Bravo-San Pedro JM, et al. Autophagy in malignant transformation and cancer progression. *EMBO J.* 2015;34(7):856-880. [doi:10.15252/embj.201490784](https://doi.org/10.15252/embj.201490784) · [PubMed 25712477](https://pubmed.ncbi.nlm.nih.gov/25712477/)

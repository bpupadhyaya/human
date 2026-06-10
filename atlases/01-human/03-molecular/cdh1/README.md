---
schema: human-scale-entry/v1
id: cdh1
name: CDH1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "E-cadherin (CDH1) is the epithelial adhesion molecule and Wnt/β-catenin co-regulator. CDH1 loss → EMT and invasive growth; germline CDH1 mutations cause hereditary diffuse gastric cancer (HDGC) with 70-80% lifetime risk; CDH1 promoter methylation is common in sporadic tumors."
aliases: ["CDH1", "E-cadherin", "E-cad", "cadherin-1", "hereditary diffuse gastric cancer", "HDGC", "E-cadherin loss", "CDH1 mutation", "uvomorulin"]
sources:
  - id: van-der-post-2015-hdgc
    type: peer-reviewed
    cite: "van der Post RS, Vogelaar IP, Carneiro F, et al. Hereditary diffuse gastric cancer: updated clinical guidelines with an emphasis on germline CDH1 mutation carriers. J Med Genet. 2015;52(6):361-374."
    doi: "10.1136/jmedgenet-2015-103094"
    pmid: "25979631"
    url: "https://doi.org/10.1136/jmedgenet-2015-103094"
  - id: christofori-1999-cadherin-switch
    type: peer-reviewed
    cite: "Christofori G, Semb H. The role of the cell-adhesion molecule E-cadherin as a tumour-suppressor gene. Trends Biochem Sci. 1999;24(2):73-76."
    doi: "10.1016/S0968-0004(98)01343-7"
    pmid: "10098403"
    url: "https://doi.org/10.1016/S0968-0004(98)01343-7"
cross_links:
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "CDH1 sequesters β-catenin at the cell membrane; CDH1 loss → cytoplasmic β-catenin release → nuclear translocation → Wnt target gene activation (MYC, cyclin D1, SNAIL); CDH1 loss is a structural adhesion defect and Wnt pathway activating event in cancer."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β drives EMT via SMAD2/3 → SNAIL/SLUG/ZEB1 transcription → CDH1 promoter repression → E-cadherin loss; CDH1 loss is a hallmark readout of TGF-β-driven EMT; CDH1 promoter methylation cooperates with TGF-β pathway in diffuse gastric cancer and lobular breast cancer."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 mutations co-occur with CDH1 loss in diffuse gastric cancer and lobular breast cancer; p53 inactivation allows CDH1-deficient cells to survive anoikis; germline CDH1 carriers show focal TP53 staining in signet ring cell foci during HDGC progression."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC kinase phosphorylates E-cadherin at Tyr754/755 → β-catenin dissociation → endocytosis → CDH1 loss without mutation; SRC-mediated CDH1 loss is reversible, a non-genetic inactivation mechanism; SRC inhibitors restore E-cadherin surface localization."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "Germline CDH1 truncating mutations cause HDGC with 70-80% lifetime risk (men); prophylactic total gastrectomy is recommended; all resected specimens show signet ring cell foci; CDH1 promoter methylation occurs in ~50% of sporadic diffuse gastric cancer."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "CDH1 loss occurs in ~90% of invasive lobular breast cancer (ILC), causing the discohesive Indian file pattern; CDH1 loss → PI3K-AKT activation; ILC is ER+ in >90%; CDK4/6 inhibitors, fulvestrant, and alpelisib (PIK3CA-mutant) are key; ILC is less chemo-sensitive than IDC."
  - target: 01-human/03-molecular/met
    relation: connects-to
    note: "MET receptor binds the CDH1 cytoplasmic domain; HGF/MET activation phosphorylates CDH1 → β-catenin dissociation → CDH1 loss and EMT; MET amplification co-occurs with CDH1 loss in gastric cancer; MET inhibitors (savolitinib) restore epithelial phenotype in MET-driven tumors."
---

# CDH1

## Overview

**CDH1 (E-cadherin)** is a classical calcium-dependent cell-cell adhesion glycoprotein essential for epithelial tissue integrity, polarity, and the suppression of cell migration and invasion. E-cadherin forms homotypic trans-dimers between adjacent epithelial cells, and its intracellular domain anchors the actin cytoskeleton through interactions with α-, β-, and γ-catenins. As a tumor suppressor, CDH1 loss — whether through somatic mutation, promoter hypermethylation, or post-translational inactivation by proteases or SRC kinase — promotes **epithelial-to-mesenchymal transition (EMT)**: loss of apical-basal polarity, dissolution of cell-cell junctions, acquisition of mesenchymal morphology, and invasive growth. In hereditary settings, **germline CDH1 mutations** cause **hereditary diffuse gastric cancer (HDGC)**, conferring up to 70-80% lifetime gastric cancer risk and 40-60% lifetime lobular breast cancer risk in women [^van-der-post-2015-hdgc].

**CDH1 in cancer:**
- **Hereditary Diffuse Gastric Cancer (HDGC):** Autosomal dominant; germline CDH1 truncating or splice-site mutations in 25-50% of HDGC families; gastric cancer lifetime risk 70-80% in men, 60-70% in women; lobular breast cancer risk 40-60% in women; prophylactic total gastrectomy recommended for CDH1 carriers; pathology: signet ring cell carcinoma (discohesive cells with mucin vacuole)
- **Sporadic diffuse gastric cancer:** CDH1 promoter methylation in ~50%; somatic CDH1 mutation + LOH
- **Invasive lobular breast cancer (ILC, ~15% of breast cancer):** CDH1 loss in ~90% (promoter methylation + LOH or mutation); ILC characteristic discohesive "Indian file" pattern; CDH1 loss releases β-catenin → PI3K-AKT activation; lobular carcinoma in situ (LCIS) = non-invasive CDH1-deficient precursor
- **Colorectal, ovarian, endometrial cancers:** CDH1 promoter methylation in sporadic tumors → EMT and invasion

**The cadherin switch:**
Cancer cells downregulate E-cadherin (CDH1) and upregulate N-cadherin (CDH2), a mesenchymal cadherin that promotes migration and invasion — the "cadherin switch." N-cadherin homotypic interactions are weaker and more dynamic than E-cadherin → increased motility; N-cadherin also binds FGFR → enhanced RTK signaling.

## Structure

### CDH1 protein architecture

CDH1 is a 135 kDa single-pass transmembrane glycoprotein, 882 amino acids:

**N-terminal signal peptide (1-22) → Pro-peptide (23-154):**
- Pro-peptide removed by furin-like proprotein convertases in the Golgi → mature E-cadherin trafficking to cell surface
- Pro-peptide removal is required for adhesive activity

**Extracellular domain (ECD, 155-699):**
- 5 cadherin repeats (EC1-EC5): Each ~110 aa β-sandwich fold; calcium coordination at each linker (3 Ca²⁺ per linker)
- EC1-EC1 trans-dimerization: X-dimers → strand swap dimers → zipper assembly at adherens junctions
- Ca²⁺ coordination rigidifies ECD → loss of Ca²⁺ (EGTA treatment) → CDH1 becomes flexible → no adhesion → endocytosis

**Transmembrane domain (TM, 700-723):** Single pass

**Cytoplasmic tail (724-882):**
- Juxtamembrane domain (JMD): p120-catenin binding → stabilizes CDH1 at cell surface; loss of p120 → CDH1 endocytosis
- β-catenin binding domain (CBD): β-catenin Arm repeats bind CDH1 tail → α-catenin → actin cytoskeleton
- Tyr754/755: SRC phosphorylation sites → β-catenin dissociation → CDH1 endocytosis → EMT

### CDH1 loss mechanisms

1. **Genetic:** Truncating mutation (frameshift, nonsense) → haploinsufficiency; LOH of second allele in HDGC
2. **Epigenetic:** CDH1 promoter CpG island hypermethylation (most common in sporadic diffuse gastric cancer); reversible with DNMT inhibitors in vitro
3. **Transcriptional repression:** SNAIL (SNAI1) → direct binding to CDH1 E-box → transcriptional silencing; ZEB1/2, TWIST, SLUG (SNAI2) also repress CDH1; all induced by TGF-β/EMT pathway
4. **Post-translational:** SRC phosphorylation at Tyr754/755 → β-catenin dissociation; MMP-mediated ectodomain shedding (E-cad fragment = soluble E-cad in serum)
5. **Co-receptor:** EGFR, MET direct binding to CDH1 cytoplasmic domain → signaling in cis; EGF/HGF → receptor activation → CDH1 phosphorylation → EMT signaling

## Function

### Normal CDH1 roles

**Epithelial tissue integrity and polarity:**
E-cadherin is the principal adhesion molecule of adherens junctions at the apical lateral membrane. CDH1 trans-dimers → homotypic adhesion → cell clustering → epithelial sheet formation. CDH1 recruits α-, β-, and p120-catenins → connects to actin cortex → mechanical stiffness. Without CDH1, epithelial cells lose polarity, adopt mesenchymal morphology, and migrate individually.

**β-catenin sequestration:**
CDH1 sequesters β-catenin at the cell membrane, keeping it away from the Wnt signaling pool (which is regulated by the APC destruction complex). CDH1 loss → excess β-catenin available for nuclear translocation → TCF/LEF-mediated transcription (MYC, cyclin D1, axin2) — overlap with Wnt pathway activation.

**Organ morphogenesis:**
E-cadherin is essential for compaction at the 8-cell stage of embryogenesis (CDH1 forms the first adhesion bonds that convert the morula into the blastocyst) and for epithelial tubulogenesis in kidney, lung, and mammary gland development.

### CDH1 in EMT

**EMT transcription factor cascade:**
TGF-β → SMAD2/3 → SNAI1/2/ZEB1/2/TWIST → E-box binding at CDH1 promoter → CDH1 silencing → E-cadherin loss → β-catenin release → nuclear Wnt signaling → MYC/cyclin D1 → proliferation + SNAIL → CDH1 repression (positive feedback loop).

**Metastatic cascade role:**
CDH1 loss is an early step in the local invasion of carcinoma. At the invasive front of tumors: CDH1 low; N-cadherin high; vimentin high → mesenchymal phenotype → basement membrane penetration → lymphovascular invasion. At metastatic sites: mesenchymal-to-epithelial reversal (MET) → CDH1 re-expression → epithelial colonization.

## Mechanism

### HDGC management

**Germline CDH1 testing indications (IGCLC 2020 guidelines):**
- Personal or family history of diffuse gastric cancer + lobular breast cancer
- Family with ≥2 diffuse gastric cancers (any age) with at least 1 confirmed before 50
- Individual with diffuse gastric cancer before 40
- Bilateral or multifocal lobular breast cancer before 70
- Bilateral lobular breast cancer before 50

**Risk management for CDH1 germline carriers:**
- **Prophylactic total gastrectomy (PTG):** Recommended for CDH1 carriers at risk; all PTG specimens from confirmed CDH1 carriers show microscopic signet ring cell foci in ~90%; these foci are T1a (intramucosal) → curable with surgery → surgery before cancer development
- **Endoscopic surveillance:** For carriers who decline or defer PTG; Cambridge protocol — random biopsies + systematic surveillance; low sensitivity (~30-70%) for flat lesions
- **Breast screening:** Annual MRI (CDH1 carriers); consider prophylactic mastectomy for carriers with LCIS found on biopsy

**Systemic therapy for CDH1-mutant tumors:**
- HDGC signet ring cell gastric cancer: Platinum + fluoropyrimidine chemotherapy (FLOT perioperative if resectable); trastuzumab if HER2+ (uncommon in diffuse type); pembrolizumab in MSI-H or PD-L1+ recurrent disease
- Lobular breast cancer: Hormonal therapy (ER+ in >90%); CDK4/6 inhibitor + fulvestrant/letrozole; ILC responds less well to anthracycline-based chemotherapy than IDC; PI3K-AKT inhibitors (alpelisib in PIK3CA-mutant) applicable to ILC
- SRC inhibitors (dasatinib) under investigation to restore CDH1 surface expression

## Connections

- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — E-cadherin sequesters β-catenin at the cell membrane in adherens junctions; CDH1 loss → cytoplasmic β-catenin release → nuclear translocation → Wnt target gene activation (MYC, cyclin D1, SNAIL); E-cadherin loss is both a structural adhesion defect and a Wnt pathway activating event in cancer.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — TGF-β drives EMT via SMAD2/3 → SNAIL/SLUG/ZEB1 transcription → CDH1 promoter repression → E-cadherin loss; CDH1 loss is a hallmark and functional readout of TGF-β-driven EMT; CDH1 promoter methylation cooperates with TGF-β pathway in diffuse-type gastric cancer and lobular breast cancer.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 mutations co-occur with CDH1 loss in advanced diffuse gastric cancer and invasive lobular breast cancer; p53-pathway inactivation allows cells with CDH1 loss to survive anoikis; germline CDH1 carriers show focal TP53 staining in signet ring cell foci indicating somatic TP53 mutations acquired during HDGC progression.
- `connects-to` → **[SRC kinase](../../03-molecular/src-kinase/README.md)** — SRC kinase phosphorylates E-cadherin at Tyr754/Tyr755 → β-catenin dissociation → cadherin endocytosis → functional CDH1 loss without mutation; SRC-mediated CDH1 phosphorylation is reversible and represents a non-genetic mechanism of E-cadherin inactivation in tumor invasion; Src inhibitors restore E-cadherin surface localization.
- `connects-to` → **[Gastric Cancer](../../07-system/gastric-cancer/README.md)** — germline CDH1 truncating mutations cause HDGC with 70-80% lifetime risk (men); prophylactic total gastrectomy is recommended; all resected specimens show signet ring cell foci; CDH1 promoter methylation occurs in ~50% of sporadic diffuse gastric cancer.
- `connects-to` → **[Breast Cancer](../../07-system/breast-cancer/README.md)** — CDH1 loss occurs in ~90% of invasive lobular breast cancer (ILC), causing the discohesive Indian file pattern; CDH1 loss → PI3K-AKT activation; ILC is ER+ in >90%; CDK4/6 inhibitors, fulvestrant, and alpelisib (PIK3CA-mutant) are key; ILC is less chemo-sensitive than IDC.
- `connects-to` → **[MET](../met/README.md)** — MET receptor binds the CDH1 cytoplasmic domain; HGF/MET activation phosphorylates CDH1 → β-catenin dissociation → CDH1 loss and EMT; MET amplification co-occurs with CDH1 loss in gastric cancer; MET inhibitors (savolitinib) restore epithelial phenotype in MET-driven tumors.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^van-der-post-2015-hdgc]: van der Post RS, Vogelaar IP, Carneiro F, et al. Hereditary diffuse gastric cancer: updated clinical guidelines with an emphasis on germline CDH1 mutation carriers. *J Med Genet.* 2015;52(6):361-374. [doi:10.1136/jmedgenet-2015-103094](https://doi.org/10.1136/jmedgenet-2015-103094) · [PubMed 25979631](https://pubmed.ncbi.nlm.nih.gov/25979631/)
[^christofori-1999-cadherin-switch]: Christofori G, Semb H. The role of the cell-adhesion molecule E-cadherin as a tumour-suppressor gene. *Trends Biochem Sci.* 1999;24(2):73-76. [doi:10.1016/S0968-0004(98)01343-7](https://doi.org/10.1016/S0968-0004(98)01343-7) · [PubMed 10098403](https://pubmed.ncbi.nlm.nih.gov/10098403/)

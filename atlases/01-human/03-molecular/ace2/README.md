---
schema: human-scale-entry/v1
id: ace2
name: Angiotensin-Converting Enzyme 2
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Type I transmembrane carboxypeptidase that cleaves angiotensin II to angiotensin 1-7, counter-regulating RAAS. Primary entry receptor for SARS-CoV-2; expressed on type II pneumocytes, cardiomyocytes, intestinal enterocytes, and renal tubular cells."
aliases: ["ACE2", "angiotensin-converting enzyme 2", "SARS-CoV-2 receptor"]
sources:
  - id: hoffmann-2020-ace2-entry
    type: peer-reviewed
    cite: "Hoffmann M, Kleine-Weber H, Schroeder S, et al. SARS-CoV-2 Cell Entry Depends on ACE2 and TMPRSS2 and Is Blocked by a Clinically Proven Protease Inhibitor. Cell. 2020;181(2):271-280."
    doi: "10.1016/j.cell.2020.02.052"
    pmid: "32142651"
  - id: hamming-2004-ace2-distribution
    type: peer-reviewed
    cite: "Hamming I, Timens W, Bulthuis MLC, Lely AT, Navis GJ, van Goor H. Tissue distribution of ACE2 protein, the functional receptor for SARS coronavirus. A first step in understanding SARS pathogenesis. J Pathol. 2004;203(2):631-637."
    doi: "10.1002/path.1570"
    pmid: "15141377"
  - id: santos-2018-ras-ace2
    type: peer-reviewed
    cite: "Santos RAS, Sampaio WO, Alzamora AC, et al. The ACE2/angiotensin-(1-7)/MAS axis of the renin-angiotensin system: focus on angiotensin-(1-7). Physiol Rev. 2018;98(1):505-553."
    doi: "10.1152/physrev.00023.2016"
    pmid: "29351514"
  - id: wrapp-2020-spike-structure
    type: peer-reviewed
    cite: "Wrapp D, Wang N, Corbett KS, et al. Cryo-EM structure of the 2019-nCoV spike in the prefusion conformation. Science. 2020;367(6483):1260-1263."
    doi: "10.1126/science.abb2507"
    pmid: "32075877"
cross_links:
  - target: 01-human/04-cellular/type-ii-pneumocyte
    relation: expressed-by
    note: "ACE2 is abundantly expressed on the apical surface of type II pneumocytes, making them the primary site of SARS-CoV-2 pulmonary entry."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: expressed-by
    note: "ACE2 expression on cardiomyocytes provides a direct cardiac entry route for SARS-CoV-2 and participates in myocardial RAAS homeostasis."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: modulates
    note: "ACE2 cleaves angiotensin II (pro-inflammatory, vasoconstrictive) to angiotensin 1-7 (cardioprotective, vasodilatory), counter-regulating the classical RAAS axis."
  - target: 01-human/06-organ/lung
    relation: expressed-by
    note: "Lung is the primary site of ACE2 expression and SARS-CoV-2 replication; alveolar ACE2 downregulation during infection worsens ARDS."
  - target: 01-human/06-organ/heart
    relation: expressed-by
    note: "Cardiac ACE2 participates in local RAAS balance; SARS-CoV-2-mediated ACE2 internalization shifts cardiac milieu toward excess angiotensin II and pro-fibrotic signaling."
  - target: 01-human/06-organ/kidney
    relation: expressed-by
    note: "ACE2 is highly expressed in renal proximal tubules and glomerular podocytes; mediates COVID-19-associated nephropathy and FSGS."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "ACE2 is a master regulator of cardiovascular homeostasis via the angiotensin 1-7/MAS receptor axis; its downregulation in COVID-19 amplifies cardiac injury."
  - target: 01-human/07-system/renal-system
    relation: modulates
    note: "Renal ACE2 regulates tubular amino acid transport (collectrin-like domain) and counter-balances RAAS-driven renal inflammation and fibrosis."
---

# Angiotensin-Converting Enzyme 2 (ACE2)

## Overview

Angiotensin-Converting Enzyme 2 (ACE2) is a **type I transmembrane zinc metallocarboxypeptidase** that serves two intertwined roles in human physiology: it is a pivotal negative regulator of the renin-angiotensin-aldosterone system (RAAS), and it is the obligate host-cell receptor for SARS-CoV-2 (and previously for SARS-CoV-1). Understanding ACE2 is therefore essential both for cardiovascular, renal, and pulmonary physiology and for the molecular pathogenesis of COVID-19.

ACE2 was discovered in 2000 as a homolog of ACE (angiotensin-converting enzyme), but with distinct catalytic activity: whereas ACE generates angiotensin II (Ang II) from angiotensin I, ACE2 **degrades Ang II** to angiotensin 1-7 (Ang 1-7) — a heptapeptide with vasodilatory, anti-inflammatory, and antifibrotic properties [^santos-2018-ras-ace2]. The ACE2/Ang 1-7/MAS axis thus constitutes a counter-regulatory arm of the RAAS that restrains the pro-hypertensive, pro-inflammatory classical axis.

The discovery that SARS-CoV spike protein uses ACE2 as its entry receptor [^hamming-2004-ace2-distribution], confirmed and extended to SARS-CoV-2 by Hoffmann et al. in 2020 [^hoffmann-2020-ace2-entry], transformed ACE2 from a relatively obscure RAAS enzyme into a central actor in one of the most consequential global pandemics of the 21st century.

## Structure

### Protein architecture

ACE2 is encoded by the *ACE2* gene on chromosome Xp22.2 and is a **805 amino acid, ~92 kDa** single-pass type I transmembrane glycoprotein (apparent MW ~120 kDa due to N-glycosylation at 7 sites). It consists of:

| Domain | Residues | Function |
|:---|:---|:---|
| **Signal peptide** | 1–17 | Directs to ER/Golgi secretory pathway |
| **Extracellular catalytic domain** | 18–615 | Zinc metallocarboxypeptidase; substrate and SARS-CoV-2 spike binding |
| **Collectrin-like domain** | 616–740 | Dimerization; interacts with amino acid transporter B0AT1 (SLC6A19) |
| **Transmembrane domain** | 741–763 | Membrane anchoring |
| **Cytoplasmic tail** | 764–805 | Signaling, internalization |

The catalytic domain contains a **HEXXH zinc-binding motif** (HExxH = HEMGH, residues 374–378) with a single catalytic zinc ion. X-ray and cryo-EM structures reveal a clamshell-like conformation that opens to bind substrate or close around the viral receptor-binding domain (RBD) — with the ACE2:RBD interface burying ~1,700 Å² of solvent-accessible surface [^wrapp-2020-spike-structure].

ACE2 forms a **homodimer** in the membrane (via the collectrin domain) and also associates with the amino acid transporter **B0AT1** on intestinal brush border. The shedding of the ACE2 ectodomain by the metalloprotease **ADAM17** (TACE) releases soluble ACE2 (sACE2) into plasma, providing a soluble "decoy receptor" for viral particles.

### Biochemical activity

ACE2 is a **monocarboxypeptidase**: it removes a single C-terminal amino acid from peptide substrates. Key reactions:

- **Angiotensin II** (Arg-Val-Tyr-Ile-His-Pro-Phe) → **Angiotensin 1-7** (Arg-Val-Tyr-Ile-His-Pro) + Phe
- **Angiotensin I** (Ang I, decapeptide) → **Angiotensin 1-9** (less efficiently)
- **Apelin-13**, **des-Arg9-bradykinin** — additional substrates

Compared with ACE (which cleaves two C-terminal residues — a dipeptidyl carboxypeptidase), ACE2 removes only a single residue and is **not inhibited by classical ACE inhibitors** (captopril, enalaprilat). It is inhibited by the experimental compound MLN-4760.

## Function

### RAAS counter-regulation

The classical RAAS axis (renin → Ang I → ACE → Ang II → AT1R) is pro-hypertensive, pro-inflammatory, and pro-fibrotic. ACE2 opposes this by:

1. Cleaving Ang II → Ang 1-7, reducing AT1R stimulation
2. Ang 1-7 signals through the **MAS receptor** (MASR/MAS1 oncogene), activating eNOS, reducing oxidative stress, opposing TGF-β-driven fibrosis, and promoting natriuresis
3. Net effect: **vasodilation, anti-inflammation, anti-fibrosis, reduced cardiac remodeling**

ACE2 deficiency in mice worsens hypertension, acute lung injury, and cardiac dysfunction — phenotypes rescued by Ang 1-7 infusion or MAS receptor agonists [^santos-2018-ras-ace2].

### Intestinal amino acid transport

In the small intestine, ACE2 co-localizes with and stabilizes the **neutral amino acid transporter B0AT1** (SLC6A19) on the brush border. This complex mediates uptake of tryptophan (and other neutral amino acids), which is required for intestinal serotonin synthesis and antimicrobial peptide production. COVID-19-related ACE2 downregulation in the gut disrupts tryptophan absorption, contributing to GI manifestations and altered microbiome composition.

### Lung protection

Acute lung injury (ALI) and ARDS are associated with Ang II excess; ACE2 is protective against both. ACE2 knockout mice develop worse ALI in response to acid or LPS. This lung-protective function of ACE2 is precisely why SARS-CoV-2-mediated ACE2 downregulation worsens ARDS pathophysiology.

## Mechanism

### SARS-CoV-2 entry via ACE2

The molecular mechanism of SARS-CoV-2 entry has been precisely defined [^hoffmann-2020-ace2-entry]:

1. **Spike S1 RBD binding**: The receptor-binding domain (RBD) of the SARS-CoV-2 spike (S1 subunit) binds ACE2 with high affinity (K_d ~15 nM) via a complementary interface involving 17 ACE2 residues and 18 spike RBD residues. Key ACE2 contact residues: Lys31, Tyr41, Gln42, Lys353, Arg357.
2. **TMPRSS2 priming**: The surface serine protease **TMPRSS2** cleaves the spike S2' site, activating the fusion peptide and enabling membrane fusion (preferred route in lung). Alternatively, endosomal cathepsins (CatB/L) can prime spike in TMPRSS2-low cells.
3. **Membrane fusion and viral entry**: The S2 fusion peptide inserts into the host membrane; heptad repeats HR1/HR2 form a 6-helix bundle driving membrane merger and genome release into the cytoplasm.
4. **ACE2 downregulation**: Spike:ACE2 binding triggers ACE2 internalization and ADAM17-mediated shedding, reducing surface ACE2 — impairing RAAS counter-regulation locally.

### RAAS signaling cascade

ACE2 → Ang 1-7 → MAS receptor → Gαi coupling → PI3K/Akt activation → eNOS phosphorylation (Ser1177) → NO production → vasodilation and anti-inflammatory signaling. Simultaneously, MAS signaling opposes PKC and ERK1/2 pathways activated by Ang II/AT1R, reducing NADPH oxidase activity and ROS generation.

## Connections

- `expressed-by` → **[Type II Pneumocyte](../../04-cellular/type-ii-pneumocyte/README.md)** — highest pulmonary ACE2 expression; primary SARS-CoV-2 entry site
- `expressed-by` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — cardiac ACE2 regulates local RAAS; SARS-CoV-2 entry route for myocarditis
- `modulates` → **[Angiotensin II](../angiotensin-ii/README.md)** — ACE2 cleaves and inactivates Ang II, counter-regulating the classical RAAS
- `modulates` → **[Cardiovascular System](../../07-system/cardiovascular-system/README.md)** — central RAAS regulator; ACE2 loss worsens hypertension, cardiac remodeling, and HF
- `expressed-by` → **[Lung](../../06-organ/lung/README.md)** — alveolar ACE2 mediates SARS-CoV-2 pulmonary infection and ARDS amplification
- `expressed-by` → **[Kidney](../../06-organ/kidney/README.md)** — tubular/podocyte ACE2 mediates COVID-19 nephropathy

## Pathology

| Disease/Condition | ACE2 Role | Consequence |
|:---|:---|:---|
| **COVID-19 / SARS-CoV-2** | Obligate entry receptor; internalization causes ACE2 downregulation | ARDS, myocarditis, AKI, GI disease, multi-organ failure |
| **Hypertension** | Reduced ACE2 activity → excess Ang II → vasoconstriction, aldosterone release | Target organ damage: cardiac hypertrophy, renal fibrosis |
| **Heart failure** | ACE2/Ang 1-7/MAS protective axis impaired → unchecked Ang II → cardiac fibrosis | Progressive systolic/diastolic dysfunction |
| **Diabetic nephropathy** | ACE2 reduced in diabetic kidney → Ang II excess → TGF-β activation → glomerulosclerosis | Accelerated CKD progression |
| **ARDS (non-COVID)** | ACE2 downregulation by injurious stimuli (acid, ventilator injury) → Ang II excess → vascular leak | Worsened alveolar flooding and hypoxemia |

ACE2 activators and Ang 1-7 mimetics (e.g., **TXA127**, **AV0991**) are under clinical investigation for heart failure, COVID-19, and pulmonary hypertension. Paradoxically, ACE inhibitors and ARBs — by reducing Ang II feedback — may upregulate ACE2 expression, a phenomenon with complex implications for COVID-19 susceptibility and severity.

[^hoffmann-2020-ace2-entry]: Hoffmann M, Kleine-Weber H, Schroeder S, et al. SARS-CoV-2 Cell Entry Depends on ACE2 and TMPRSS2 and Is Blocked by a Clinically Proven Protease Inhibitor. *Cell.* 2020;181(2):271-280. [doi:10.1016/j.cell.2020.02.052](https://doi.org/10.1016/j.cell.2020.02.052) · [PubMed 32142651](https://pubmed.ncbi.nlm.nih.gov/32142651/)
[^hamming-2004-ace2-distribution]: Hamming I, Timens W, Bulthuis MLC, Lely AT, Navis GJ, van Goor H. Tissue distribution of ACE2 protein, the functional receptor for SARS coronavirus. *J Pathol.* 2004;203(2):631-637. [doi:10.1002/path.1570](https://doi.org/10.1002/path.1570) · [PubMed 15141377](https://pubmed.ncbi.nlm.nih.gov/15141377/)
[^santos-2018-ras-ace2]: Santos RAS, Sampaio WO, Alzamora AC, et al. The ACE2/angiotensin-(1-7)/MAS axis of the renin-angiotensin system: focus on angiotensin-(1-7). *Physiol Rev.* 2018;98(1):505-553. [doi:10.1152/physrev.00023.2016](https://doi.org/10.1152/physrev.00023.2016) · [PubMed 29351514](https://pubmed.ncbi.nlm.nih.gov/29351514/)
[^wrapp-2020-spike-structure]: Wrapp D, Wang N, Corbett KS, et al. Cryo-EM structure of the 2019-nCoV spike in the prefusion conformation. *Science.* 2020;367(6483):1260-1263. [doi:10.1126/science.abb2507](https://doi.org/10.1126/science.abb2507) · [PubMed 32075877](https://pubmed.ncbi.nlm.nih.gov/32075877/)

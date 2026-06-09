---
schema: human-scale-entry/v1
id: mu-opioid-receptor
name: Mu-Opioid Receptor
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "μ-opioid receptor (MOR/OPRM1), Gi-coupled GPCR activated by β-endorphin and opioid drugs; mediates analgesia via PAG descending pathway, euphoria via VTA disinhibition → NAcc dopamine, and respiratory depression via pre-Bötzinger complex; therapeutic target for pain and OUD."
aliases: ["mu-opioid receptor", "MOR", "OPRM1", "μ-opioid receptor", "mu opioid", "beta-endorphin receptor", "morphine receptor", "opioid receptor mu", "A118G", "Asn40Asp"]
sources:
  - id: matthes-1996-mor-knockout
    type: peer-reviewed
    cite: "Matthes HW, Maldonado R, Simonin F, et al. Loss of morphine-induced analgesia, reward effect and withdrawal symptoms in mice lacking the mu-opioid receptor gene. Nature. 1996;383(6603):819-823."
    doi: "10.1038/383819a0"
    pmid: "8893006"
    url: "https://doi.org/10.1038/383819a0"
    accessed: "2026-06-08"
  - id: pasternak-2014-mor-review
    type: peer-reviewed
    cite: "Pasternak GW, Pan YX. Mu opioids and their receptors: evolution of a concept. Pharmacol Rev. 2013;65(4):1257-1317."
    doi: "10.1124/pr.112.007138"
    pmid: "24076545"
    url: "https://doi.org/10.1124/pr.112.007138"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "MOR activation on VTA GABAergic interneurons → disinhibition → increased DA firing → NAcc dopamine surge → euphoria; this opioid-DA coupling is the primary reward mechanism in OUD and underlies naltrexone's efficacy in reducing opioid and alcohol reward."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "MOR is expressed on GABAergic interneurons throughout CNS; Gi → hyperpolarize GABA interneurons → reduced GABA release → disinhibition of DA neurons (VTA) and PAG neurons (analgesia); buprenorphine as partial MOR agonist preserves stable GABAergic tone without euphoric surge."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "MOR on LC neurons → Gi → suppresses cAMP → reduces LC firing → decreased NE during opioid use; opioid withdrawal → LC rebound hyperactivation → NE storm → sympathetic withdrawal; clonidine/lofexidine suppress LC rebound via α2A autoreceptor agonism."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Chronic MOR activation in NAcc → ΔFosB accumulation → altered BDNF signaling and reward plasticity; BDNF in VTA potentiates opioid reinforcement via TrkB signaling; withdrawal → acute BDNF surge in NAcc contributing to withdrawal aversion and craving intensity."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "MOR expressed in PAG (descending analgesia), VTA (euphoria via DA disinhibition), LC (arousal/withdrawal), NAcc (reinforcement), amygdala (aversion), and pre-Bötzinger complex (respiratory rhythm); distribution explains opioids' broad and opposing CNS effects."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Alcohol triggers β-endorphin → MOR on VTA GABAergic interneurons → disinhibition → dopamine surge in NAcc; naltrexone (MOR/KOR antagonist) blocks this reward mechanism → reduces alcohol craving; OPRM1 A118G (Asn40Asp) predicts superior naltrexone response in AUD."
  - target: 01-human/07-system/opioid-use-disorder
    relation: connects-to
    note: "Compulsive MOR activation in OUD drives tolerance (GRK/β-arrestin desensitization + cAMP superactivation), physical dependence, and withdrawal; buprenorphine (partial MOR agonist), methadone (full agonist), and naltrexone (MOR antagonist) all target MOR for treatment."
---

# Mu-Opioid Receptor

## Overview

The **μ-opioid receptor (MOR; gene OPRM1)** is the primary molecular target for endogenous opioid peptides and opioid drugs — including morphine, heroin, fentanyl, oxycodone, and buprenorphine. It belongs to the Gi/Go-coupled GPCR superfamily (rhodopsin class A) and mediates the primary therapeutic effects of opioid analgesics as well as the reinforcing properties underlying opioid use disorder.

**Endogenous MOR ligands:**
- **β-Endorphin (POMC-derived):** High-affinity, high-efficacy MOR agonist; released from pituitary and arcuate nucleus neurons during stress, exercise (runner's high), and social reward
- **Endomorphin-1 and -2:** Tetrapeptides with highest MOR selectivity of any endogenous opioid; distribution primarily in brainstem pain circuits
- **Enkephalins (Met- and Leu-enkephalin; PENK-derived):** Moderate affinity at MOR; also active at δ-opioid receptors; widespread CNS distribution; short half-life (rapidly cleaved by peptidases)
- **Dynorphins (PDYN-derived):** Primarily κ-opioid receptor selective; high concentrations can activate MOR; dysphorigenic

**OPRM1 genetic variation:**
- **A118G (rs1799971; Asn40Asp):** Most studied functional variant; ~15-20% minor allele frequency; Asn40Asp → slightly increased β-endorphin potency and binding; clinical relevance: predicts response to naltrexone (Asp40 carriers respond better, ~5-8% of alcohol use disorder patients); associated with reduced opioid reward in some studies but also increased blunted stress response
- **OPRM1** copy number variants and intronic variants in promoter methylation affect MOR expression levels and pain sensitivity

## Structure

### Protein structure

- 400 amino acid GPCR; 7 transmembrane (TM) helices; N-terminal extracellular, C-terminal intracellular
- **Orthosteric binding site:** Asp147 (TM3) — critical for ionic interaction with opioid nitrogen; deep hydrophobic pocket formed by TM3/5/6/7
- **Allosteric sites:** Sodium allosteric site (Asp2.50 Na+ coordinated) modulates agonist efficacy; targeted by experimental positive/negative allosteric modulators
- **C-terminal tail:** Multiple serine/threonine phosphorylation sites for GRK2/3/5/6 → β-arrestin1/2 recruitment → desensitization and internalization

**Crystal structure (2012, 2015, 2023 cryo-EM):** Inactive (antagonist-bound) and active (agonist-bound + G-protein) structures resolved; revealed outward TM6 movement upon activation; basis for structure-based drug design.

### Splice variants

OPRM1 undergoes extensive alternative splicing (>20 variants in rodents; fewer confirmed in humans):
- Full-length MOR-1 (400 aa): dominant functional receptor; 7TM; couples efficiently to Gi
- MOR-1A, MOR-1B, etc.: truncated C-terminal variants; altered trafficking and Gi/arrestin coupling ratios
- 6TM variants: 6-transmembrane isoforms; couple to Gs rather than Gi → excitatory effects; expressed in peripheral pain neurons; may explain opioid-induced hyperalgesia (OIH)

## Function

### G-protein signaling cascade

**Canonical Gi/Go pathway:**
1. **Agonist binding** → MOR conformational change (TM5/6 displacement) → Gαi/o activation (GDP→GTP exchange)
2. **Gαi:** Inhibits adenylyl cyclase → ↓cAMP → ↓PKA → reduced CREB phosphorylation
3. **Gβγ:** Activates GIRK K⁺ channels → hyperpolarization → reduced neuronal firing; inhibits N/P/Q-type VGCCs → reduced Ca²⁺ entry → reduced neurotransmitter release
4. Net effect: **neuronal inhibition** — reduced spontaneous firing, reduced evoked transmitter release

**PAG descending analgesia pathway:**
- β-Endorphin → MOR on PAG GABAergic interneurons → suppress GABA → disinhibit PAG output neurons → RVM (rostral ventromedial medulla) → spinal dorsal horn → inhibit pain transmission
- This disinhibition cascade (GABA interneuron → PAG output) mirrors the VTA disinhibition mechanism for reward

**VTA reward disinhibition:**
- Opioid → MOR on VTA GABAergic interneurons → Gi → hyperpolarize GABA interneurons → reduced GABA on DA neurons → DA disinhibition → increased firing → NAcc DA release → reinforcement

### Arrestin pathway and biased agonism

**β-Arrestin recruitment:**
1. GRK (2,3,5,6) phosphorylates MOR C-tail → β-arrestin1/2 recruitment
2. β-Arrestin: (a) physically uncouples receptor from G-protein → desensitization; (b) recruits clathrin/AP2 → endocytosis → receptor downregulation → tolerance
3. Endosomal MOR can continue signaling (sustained Gi from endosome)

**Biased agonism hypothesis:**
- Different opioid ligands stabilize different MOR conformations → differentially recruit G-protein vs. arrestin pathways
- **G-protein-biased agonists** (experimental): TRV130 (oliceridine, FDA-approved 2020 — IV analgesic) → less arrestin recruitment → less respiratory depression, constipation, tolerance (in theory)
- **Clinical reality:** Respiratory depression appears partially G-protein-mediated (not arrestin-only), so biased agonism advantage is more modest than initially predicted (2020-2022 rethinking)

## Mechanism

### Tolerance mechanisms

1. **Acute desensitization:** Phosphorylation (GRK) → β-arrestin → uncoupling from Gi → loss of receptor function within minutes-hours
2. **Receptor downregulation:** Endocytosis → lysosomal degradation → reduced surface receptor density → tolerance over days-weeks
3. **Adenylyl cyclase superactivation:** Chronic Gi-mediated inhibition of AC → compensatory AC upregulation → when opioid removed, elevated cAMP → LC hyperactivation → withdrawal syndrome
4. **Post-receptor changes:** Chronic use → altered gene expression (CREB, ΔFosB) → neuroplasticity changes in NAcc, VTA, PFC → long-term loss of natural reward sensitivity

### MOR pharmacology

| Drug | Class | Efficacy (MOR) | Notes |
|:---|:---|:---|:---|
| Morphine | Full agonist | High | Prototype; moderate arrestin recruitment |
| Fentanyl | Full agonist | Very high | 50-100× more potent; rapid onset; high arrestin recruitment |
| Oxycodone | Full agonist | High | Oral bioavailability >60%; DAT interaction may contribute to abuse |
| Buprenorphine | Partial agonist + κ-antagonist | Partial (ceiling) | Tight MOR binding → "blocks" full agonist; ceiling on respiratory depression |
| Methadone | Full agonist + NMDA antagonist | High | Long t½; NMDA antagonism may reduce OIH; QTc prolongation |
| Naltrexone | Pure antagonist | None | Competitive; 72h MOR occupancy; long-acting injectable (monthly) |
| Naloxone | Antagonist | None | Short t½ (30-90 min); IV/IN overdose reversal; SC depot form |
| Oliceridine | G-protein biased agonist | Moderate (biased) | IV; reduced GI and respiratory effects vs morphine; FDA 2020 |

## Connections

- `connects-to` → **[Dopamine](../dopamine/README.md)** — MOR activation on VTA GABAergic interneurons → disinhibition → increased VTA DA firing → NAcc dopamine surge → euphoria; this opioid-DA coupling is the primary reward mechanism in OUD; naltrexone blocks MOR-mediated VTA disinhibition → reduces opioid and alcohol reward.

- `connects-to` → **[GABA](../gaba/README.md)** — MOR expressed on GABAergic interneurons in VTA and PAG; Gi activation → hyperpolarizes GABA interneurons → disinhibition of DA neurons (VTA reward) and PAG output neurons (descending analgesia); buprenorphine as partial MOR agonist maintains stable GABAergic tone.

- `connects-to` → **[Norepinephrine](../norepinephrine/README.md)** — MOR on LC neurons → Gi → suppresses LC firing → decreased NE during opioid use; abrupt cessation → LC rebound hyperactivation → NE storm → sympathetic withdrawal syndrome; clonidine/lofexidine suppress LC rebound via α2A autoreceptor agonism.

- `connects-to` → **[BDNF](../bdnf/README.md)** — chronic MOR activation in NAcc drives ΔFosB accumulation → altered BDNF expression and reward plasticity; BDNF in VTA potentiates opioid reinforcement via TrkB; withdrawal-phase BDNF surge in NAcc contributes to withdrawal aversion and drug craving.

- `expressed-in` → **[Brain](../../06-organ/brain/README.md)** — MOR expressed in PAG (descending analgesia), VTA (euphoria via DA disinhibition), LC (arousal/withdrawal), NAcc (reinforcement), amygdala (aversion), and pre-Bötzinger complex (respiratory rhythm depression); distribution explains opioids' broad opposing CNS effects.

- `connects-to` → **[Opioid Use Disorder](../../07-system/opioid-use-disorder/README.md)** — compulsive MOR activation drives tolerance (GRK/β-arrestin desensitization + cAMP superactivation), physical dependence, and withdrawal; buprenorphine (partial agonist), methadone (full agonist), and naltrexone (antagonist) all target MOR for MOUD.

- `connects-to` → **[Alcohol Use Disorder](../../07-system/alcohol-use-disorder/README.md)** — alcohol triggers β-endorphin → MOR on VTA GABAergic interneurons → disinhibition → dopamine surge in NAcc; naltrexone (MOR/KOR antagonist) blocks this reward mechanism → reduces alcohol craving; OPRM1 A118G (Asn40Asp) predicts superior naltrexone response in AUD.

[^matthes-1996-mor-knockout]: Matthes HW, Maldonado R, Simonin F, et al. Loss of morphine-induced analgesia, reward effect and withdrawal symptoms in mice lacking the mu-opioid receptor gene. *Nature.* 1996;383(6603):819-823. [doi:10.1038/383819a0](https://doi.org/10.1038/383819a0) · [PubMed 8893006](https://pubmed.ncbi.nlm.nih.gov/8893006/)
[^pasternak-2014-mor-review]: Pasternak GW, Pan YX. Mu opioids and their receptors: evolution of a concept. *Pharmacol Rev.* 2013;65(4):1257-1317. [doi:10.1124/pr.112.007138](https://doi.org/10.1124/pr.112.007138) · [PubMed 24076545](https://pubmed.ncbi.nlm.nih.gov/24076545/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

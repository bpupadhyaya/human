---
schema: human-scale-entry/v1
id: substance-p
name: Substance P
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "Substance P (11-aa tachykinin; NK1R/Gαq) is the primary neuropeptide mediator of slow pain, neurogenic inflammation, and emotional stress. Elevated CSF SP is a reproducible fibromyalgia biomarker. NK1R antagonists (aprepitant) are antiemetics; failed for depression."
aliases: ["substance P", "SP", "neurokinin 1", "NK1R", "tachykinin", "TAC1", "undecapeptide", "slow pain mediator", "neurogenic inflammation"]
sources:
  - id: otsuka-1993-substance-p-review
    type: peer-reviewed
    cite: "Otsuka M, Yoshioka K. Neurotransmitter functions of mammalian tachykinins. Physiol Rev. 1993;73(2):229-308."
    doi: "10.1152/physrev.1993.73.2.229"
    pmid: "8385466"
    url: "https://doi.org/10.1152/physrev.1993.73.2.229"
    accessed: "2026-06-08"
  - id: russell-1994-fibromyalgia-substance-p
    type: peer-reviewed
    cite: "Russell IJ, Orr MD, Littman B, et al. Elevated cerebrospinal fluid levels of substance P in patients with the fibromyalgia syndrome. Arthritis Rheum. 1994;37(11):1593-1601."
    doi: "10.1002/art.1780371106"
    pmid: "7526868"
    url: "https://doi.org/10.1002/art.1780371106"
    accessed: "2026-06-08"
  - id: kramer-1998-nk1-antagonist-depression
    type: peer-reviewed
    cite: "Kramer MS, Cutler N, Feighner J, et al. Distinct mechanism for antidepressant activity by blockade of central substance P receptors. Science. 1998;281(5383):1640-1645."
    doi: "10.1126/science.281.5383.1640"
    pmid: "9733503"
    url: "https://doi.org/10.1126/science.281.5383.1640"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "SP and glutamate act synergistically at spinal dorsal horn: SP activates NK1R → depolarizes neurons → removes NMDA Mg²⁺ block → LTP-like wind-up facilitation; NK1R-NMDA synergy underlies central sensitization in fibromyalgia and chronic neuropathic pain."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Serotonin and substance P are co-expressed in raphe nuclei; descending 5-HT pathways gate spinal SP release (5-HT3 → SP excitation; 5-HT1A → SP inhibition); duloxetine's serotonergic component suppresses SP-driven central sensitization in chronic pain states."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Descending NE pathways from LC suppress spinal SP release via α2 adrenergic receptors on dorsal horn neurons; duloxetine's NE reuptake inhibition suppresses SP signaling; NE depletion in descending pathways amplifies SP-driven pain and allodynia."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "SP is expressed in primary afferent C-fibers (dorsal horn pain transmission), amygdala (fear and stress), raphe nuclei (co-released with 5-HT), and striatum; NK1R is broadly distributed in pain, emotion, and vomiting circuits; NK1R antagonists are clinical antiemetics."
  - target: 01-human/07-system/fibromyalgia
    relation: connects-to
    note: "CSF substance P is elevated ~3-fold in fibromyalgia — one of the most reproducible biomarkers in FM; elevated SP → NK1R sensitization → dorsal horn wind-up → diffuse hyperalgesia; NK1R antagonists reduce central sensitization markers in preclinical FM models."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "SP and CGRP are co-stored and co-released from trigeminal C-fibers; together they mediate neurogenic inflammation (SP → plasma extravasation + mast cell degranulation; CGRP → vasodilation); both are elevated in CSF during migraine attacks and in FM patients."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "SP released from injured C-fibers drives NK1R dorsal horn sensitization; peripheral nerve injury → ↑ SP in DRG → amplified spinal wind-up; NK1R-NMDA synergy underlies central sensitization; SP-driven allodynia and hyperalgesia are NK1R-mediated."
---

# Substance P

## Overview

**Substance P (SP)** is an 11-amino acid neuropeptide of the **tachykinin family** (gene: *TAC1*, chromosome 7q21–22), first isolated from equine gut by von Euler and Gaddum in 1931 and named for its ability to cause intestinal smooth muscle contraction. The structure and amino acid sequence were elucidated by Chang, Leeman, and Niall in 1971.

SP is the **prototypical slow-pain transmitter** — released from unmyelinated C-fiber nociceptors at the spinal dorsal horn, where it amplifies pain signals over seconds to minutes via NK1R activation. Unlike fast glutamate-mediated pain (AMPA/kainate; milliseconds), SP-mediated pain transmission is slow, sustained, and facilitates central sensitization — the neuroplastic amplification of pain that underlies conditions such as fibromyalgia, irritable bowel syndrome, and migraine chronification.

Beyond pain, SP is a neuromodulator in emotional processing circuits: it is abundant in the amygdala, raphe nuclei, striatum, and brainstem, where it modulates stress responses, anxiety, nausea, and mood. The initial excitement over NK1R antagonists as antidepressants (Kramer et al., Science, 1998 [^kramer-1998-nk1-antagonist-depression]) was not confirmed in larger Phase 3 trials, but NK1R antagonists became established antiemetics (aprepitant, fosaprepitant — for chemotherapy-induced nausea/vomiting and postoperative nausea).

**Why SP matters:**
- Elevated CSF SP is the **most consistently replicated biological finding** in fibromyalgia [^russell-1994-fibromyalgia-substance-p]
- SP contributes to neurogenic inflammation (vasodilatation, mast cell degranulation, plasma protein extravasation)
- SP-NMDA synergy at the dorsal horn is the molecular mechanism of **spinal wind-up** — the temporal summation of pain signals that drives central sensitization
- SP is a druggable target: NK1R antagonists are established antiemetics and under investigation for itch, PTSD, and pain

## Structure

### Peptide chemistry

Substance P: **Arg¹-Pro²-Lys³-Pro⁴-Gln⁵-Gln⁶-Phe⁷-Phe⁸-Gly⁹-Leu¹⁰-Met¹¹-NH₂**

Key features:
- MW: 1347 Da; C-terminal amide essential for NK1R binding
- **Proline residues** at positions 2 and 4 confer rigidity and receptor selectivity
- Half-life in vivo: ~1 minute (NEP/endopeptidase-24.11, ACE-like peptidases)
- Part of the tachykinin family that includes **Neurokinin A (NKA)** and **Neurokinin B (NKB)** (also from *TAC1* and *TAC3* respectively)

### Neurokinin receptor family

| Receptor | Gene | Preferred ligand | Coupling | Expression |
|:---|:---|:---|:---|:---|
| **NK1R (NK₁)** | *TACR1* | SP >> NKA, NKB | Gαq → PLC → IP₃/DAG → PKC | Dorsal horn (laminae I/V), amygdala, striatum, raphe, CTZ |
| **NK2R (NK₂)** | *TACR2* | NKA >> SP, NKB | Gαq | Peripheral (gut, airways, bladder smooth muscle) |
| **NK3R (NK₃)** | *TACR3* | NKB >> NKA, SP | Gαq | Hypothalamus, forebrain |

**NK1R cellular signaling:**
1. SP → NK1R → Gαq → PLC-β → IP₃ → ER Ca²⁺ release + DAG → PKC
2. PKC → phosphorylation of ion channels and transcription factors → sustained neuronal excitability
3. β-arrestin recruitment → receptor internalization → desensitization over minutes
4. NK1R internalization is used as a histological marker of nociceptive C-fiber activation in rodent pain models

### Source and distribution

| Location | Cell type | Function |
|:---|:---|:---|
| **Primary afferent C-fibers** | Small-diameter DRG neurons (IB4-negative, peptidergic) | Slow pain transmission to dorsal horn |
| **Spinal dorsal horn** | Projection neurons (lamina I) | Second-order pain relay; receives SP from C-fibers |
| **Trigeminal nucleus** | Trigeminal ganglion C-fibers | Craniofacial pain; migraine |
| **Amygdala (CeA, BLA)** | GABAergic interneurons and projection neurons | Stress responses, fear, aversion |
| **Raphe nuclei** | Serotonergic neurons (co-release) | Pain modulation, mood, vomiting |
| **Striatum / NAcc** | Medium spiny neurons | Reward, mood regulation |
| **Nodose ganglion / vagus** | Vagal afferents | Gut-brain axis, nausea, vomiting |

## Function

### Slow pain transmission and wind-up

**Peripheral nociception:**
1. Tissue damage/inflammation → bradykinin, PGE2, NGF, ATP → sensitize C-fiber nociceptors (peripheral sensitization → hyperalgesia)
2. C-fibers release **SP + CGRP + glutamate** at the dorsal horn (lamina I/V) in response to nociceptive stimuli

**Spinal wind-up (temporal summation):**
- Repetitive C-fiber activation → sustained SP release → NK1R activation → maintained Na⁺/Ca²⁺ influx → membrane depolarization
- This depolarization removes the Mg²⁺ block from **NMDA receptors** (normally voltage-dependent at resting potential)
- SP (NK1R) + glutamate (NMDA) + AMPA → synergistic Ca²⁺ influx → PKC-ε/PKA activation → PKC phosphorylates NR2B → lower NMDA threshold
- Result: **central sensitization** — the spinal cord becomes hyperexcitable, amplifying and expanding pain signals

**Neurogenic inflammation (peripheral):**
- SP released antidromically from C-fiber terminals → local vasodilation, mast cell degranulation (histamine, 5-HT), plasma protein extravasation → "flare" response
- Underlies the neurogenic component of migraine (along with CGRP)
- In RA and asthma: SP from sensory nerves amplifies local inflammation via NK1R on immune cells

### Emotional and stress regulation

**Amygdala SP circuits:**
- CeA SP neurons project to BNST, LC, PAG — coordinates fear responses
- CeA NK1R activation → increased fear expression, reduced extinction; NK1R antagonism → anxiolytic effects in rodent models
- Stress → hypothalamic-pituitary axis → CRH → SP co-release → amplified HPA activation

**Vomiting (CTZ and NTS):**
- SP activates NK1R in the chemoreceptor trigger zone (CTZ) and nucleus tractus solitarius (NTS) → vomiting reflex
- **NK1R antagonists (aprepitant, netupitant, rolapitant):** FDA-approved antiemetics for chemotherapy-induced nausea/vomiting (CINV) and postoperative nausea/vomiting (PONV) — most effective for delayed-phase CINV (>24 hours)

## Mechanism

### NK1R antagonists: from antidepressant hope to antiemetic reality

The 1998 Science paper by Kramer et al. reported that an NK1R antagonist (MK-869/aprepitant) was effective as an antidepressant in Phase 2 trials [^kramer-1998-nk1-antagonist-depression]. The mechanism hypothesized: SP in CeA/raphe → chronic stress → HPA dysregulation → depression; blocking NK1R would normalize this. However:
- Four Phase 3 trials with aprepitant and lanepitant failed to show significant antidepressant efficacy vs. placebo
- The larger Phase 2 result likely reflected placebo response and small sample size
- NK1R antagonists are nevertheless established antiemetics (aprepitant → Emend, FDA 2003)

**NK1R antagonists in clinical use:**

| Drug | Indication | Route |
|:---|:---|:---|
| Aprepitant (Emend) | CINV prophylaxis (acute + delayed) | Oral |
| Fosaprepitant | CINV prophylaxis | IV prodrug of aprepitant |
| Netupitant | CINV (combination with palonosetron) | Oral |
| Rolapitant | CINV delayed phase | Oral |
| Tradipitant | Gastroparesis, motion sickness | Phase 3 |

### SP in central sensitization

Repeated or sustained nociceptive input → progressive SP-NMDA sensitization → three-tier amplification:
1. **Synaptic level:** ↑ AMPA/NMDA ratio; NR2B phosphorylation; reduced GABAergic inhibition of dorsal horn
2. **Transcriptional level:** PKC-ε → CREB → c-Fos → ↑ SP synthesis in DRG; ↑ NK1R expression in dorsal horn
3. **Descending facilitation:** sustained SP signals activate ON-cells in RVM → descending facilitation of pain → self-perpetuating sensitization

This three-tier cascade is the molecular basis of **allodynia** (pain from normally non-painful stimuli) and **hyperalgesia** (enhanced pain from noxious stimuli) in fibromyalgia, post-surgical pain, and neuropathic pain.

## Connections

- `connects-to` → **[Glutamate](../glutamate/README.md)** — SP and glutamate synergize at spinal dorsal horn: NK1R activation depolarizes neurons → removes NMDA Mg²⁺ block → enables NMDA Ca²⁺ influx and wind-up (central sensitization); NMDA antagonists (ketamine, memantine) block SP-driven wind-up; this mechanism underlies chronic pain in fibromyalgia, neuropathic pain, and migraine chronification.

- `connects-to` → **[Serotonin](../serotonin/README.md)** — SP and serotonin are co-expressed in raphe nuclei and co-released at descending pain modulation synapses; 5-HT3 receptors on dorsal horn neurons facilitate SP release (pronociceptive), while 5-HT1A/1B receptors inhibit SP release; duloxetine exploits serotonergic suppression of SP-driven pain.

- `connects-to` → **[Norepinephrine](../norepinephrine/README.md)** — descending NE from LC suppresses spinal SP release via α2 adrenergic receptors on primary afferents and dorsal horn interneurons; NE deficiency in descending spinal pathways amplifies SP-driven central sensitization; duloxetine and tricyclic antidepressants achieve analgesia partly through this NE-SP mechanism.

- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — SP is expressed in primary afferent C-fibers (slow pain), amygdala (fear/stress), raphe (co-release with 5-HT), striatum, and brainstem vagal circuits (nausea); NK1R is widely expressed in pain-emotion circuits; NK1R internalization in dorsal horn is a validated histological marker of C-fiber nociceptive activation.

- `connects-to` → **[Fibromyalgia](../../07-system/fibromyalgia/README.md)** — CSF substance P is elevated ~3-fold in fibromyalgia patients vs healthy controls — the most consistently replicated biological finding in FM; elevated SP drives NK1R sensitization → dorsal horn wind-up → diffuse hyperalgesia and allodynia; SP-NMDA central sensitization is the mechanistic basis of FM's central pain amplification.

- `connects-to` → **[CGRP](../cgrp/README.md)** — SP and CGRP are co-stored and co-released from trigeminal C-fiber terminals; SP causes plasma protein extravasation and mast cell degranulation while CGRP mediates vasodilation — together orchestrating neurogenic inflammation; both neuropeptides are elevated in CSF during migraine attacks and contribute to peripheral sensitization in fibromyalgia.
- `connects-to` → **[Neuropathic Pain](../../07-system/neuropathic-pain/README.md)** — SP released from injured primary afferent C-fibers drives NK1R sensitization at the spinal dorsal horn; peripheral nerve injury increases SP synthesis in DRG neurons, amplifying spinal wind-up; NK1R-NMDA receptor synergy is the molecular basis of central sensitization in neuropathic pain states; SP-driven allodynia and hyperalgesia are NK1R-mediated phenomena.

[^otsuka-1993-substance-p-review]: Otsuka M, Yoshioka K. Neurotransmitter functions of mammalian tachykinins. *Physiol Rev.* 1993;73(2):229-308. [doi:10.1152/physrev.1993.73.2.229](https://doi.org/10.1152/physrev.1993.73.2.229) · [PubMed 8385466](https://pubmed.ncbi.nlm.nih.gov/8385466/)
[^russell-1994-fibromyalgia-substance-p]: Russell IJ, Orr MD, Littman B, et al. Elevated cerebrospinal fluid levels of substance P in patients with the fibromyalgia syndrome. *Arthritis Rheum.* 1994;37(11):1593-1601. [doi:10.1002/art.1780371106](https://doi.org/10.1002/art.1780371106) · [PubMed 7526868](https://pubmed.ncbi.nlm.nih.gov/7526868/)
[^kramer-1998-nk1-antagonist-depression]: Kramer MS, Cutler N, Feighner J, et al. Distinct mechanism for antidepressant activity by blockade of central substance P receptors. *Science.* 1998;281(5383):1640-1645. [doi:10.1126/science.281.5383.1640](https://doi.org/10.1126/science.281.5383.1640) · [PubMed 9733503](https://pubmed.ncbi.nlm.nih.gov/9733503/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

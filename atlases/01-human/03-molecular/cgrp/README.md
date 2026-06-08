---
schema: human-scale-entry/v1
id: cgrp
name: CGRP
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "CGRP (37-aa neuropeptide encoded by CALCA via neuronal alternative splicing) mediates trigeminovascular pain and dural vasodilation in migraine; anti-CGRP mAbs (erenumab, fremanezumab) prevent migraine; gepants (rimegepant, ubrogepant) treat acute attacks."
aliases: ["calcitonin gene-related peptide", "αCGRP", "CALCA peptide", "trigeminal CGRP", "CGRP receptor", "CLR RAMP1", "anti-CGRP monoclonal antibody", "gepant", "erenumab", "rimegepant"]
sources:
  - id: amara-1982-cgrp-discovery
    type: peer-reviewed
    cite: "Amara SG, Jonas V, Rosenfeld MG, Ong ES, Evans RM. Alternative RNA processing in calcitonin gene expression generates mRNAs encoding different polypeptide products. Nature. 1982;298(5871):240-244."
    doi: "10.1038/298240a0"
    pmid: "6285202"
    url: "https://doi.org/10.1038/298240a0"
    accessed: "2026-06-08"
  - id: olesen-2004-cgrp-migraine
    type: peer-reviewed
    cite: "Olesen J, Diener HC, Husstedt IW, et al. Calcitonin gene-related peptide receptor antagonist BIBN 4096 BS for the acute treatment of migraine. N Engl J Med. 2004;350(11):1104-1110."
    doi: "10.1056/NEJMoa030505"
    pmid: "15014183"
    url: "https://doi.org/10.1056/NEJMoa030505"
    accessed: "2026-06-08"
  - id: dodick-2018-erenumab-arise
    type: peer-reviewed
    cite: "Dodick DW, Ashina M, Brandes JL, et al. ARISE: A Phase 3 randomized trial of erenumab for episodic migraine. Cephalalgia. 2018;38(6):1026-1037."
    doi: "10.1177/0333102418759786"
    pmid: "29471679"
    url: "https://doi.org/10.1177/0333102418759786"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/07-system/migraine
    relation: connects-to
    note: "CGRP released from trigeminal C-fibers mediates dural vasodilation and neurogenic inflammation in migraine; plasma CGRP rises during attacks and normalizes post-triptan; anti-CGRP mAbs (erenumab) reduce frequency ~50%; gepants (rimegepant) treat acute attacks."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Triptans (5-HT1B/D agonists) abort migraine by constricting dural vessels and inhibiting trigeminal CGRP release; serotonin regulates CGRP release from TNC neurons; serotonin syndrome risk is low when combining triptans with SSRIs or SNRIs."
---

# CGRP

## Overview

**Calcitonin gene-related peptide (CGRP)** is a 37-amino acid neuropeptide and the most potent endogenous vasodilator identified in humans. It was discovered in 1982 by Amara et al. [^amara-1982-cgrp-discovery] through an unexpected finding: the **CALCA gene** (chromosome 11p15.2), previously known only for encoding calcitonin, produces two entirely different peptides via **tissue-specific alternative RNA splicing**:

- In **thyroid C-cells**: exon 4 is included → **calcitonin** (32-aa peptide regulating calcium homeostasis)
- In **sensory and autonomic neurons**: exon 4 is skipped; exons 5 and 6 are spliced → **αCGRP** (37-aa neuropeptide mediating pain and vascular tone)

A second isoform, **βCGRP**, is encoded by the closely related **CALCB gene** and differs from αCGRP by 3 amino acids. βCGRP is expressed primarily in the enteric nervous system and spinal motor neurons; αCGRP is the predominant peripheral/CNS form and the pharmacologically relevant target in migraine.

CGRP's clinical importance escalated dramatically in the 2010s–2020s when anti-CGRP monoclonal antibodies demonstrated **prophylactic migraine prevention** with a safety profile superior to prior preventive agents — validating CGRP as the primary mediator of migraine pain decades after its first link to headache was identified by Edvinsson and colleagues.

## Structure

### Peptide structure

αCGRP is a 37-amino acid peptide with:
- An N-terminal disulfide bridge between Cys² and Cys⁷ forming a ring essential for receptor binding
- A C-terminal amidated phenylalanine (Phe³⁷-NH₂) — required for full receptor activation
- MW: ~3.8 kDa after post-translational processing
- Predominantly α-helical mid-region; flexible N- and C-termini

### CGRP receptor complex

The **CGRP receptor** is a Class B GPCR assembled from three components:

| Component | Gene | Role |
|:---|:---|:---|
| **CLR** (calcitonin receptor-like receptor) | CALCRL | 7-TM GPCR — ligand-binding scaffold; alone has no CGRP affinity |
| **RAMP1** (receptor activity-modifying protein 1) | RAMP1 | Single-pass TM protein — confers CGRP selectivity; required for CLR cell surface trafficking and CGRP recognition |
| **RCP** (receptor component protein) | CRCP | Intracellular adaptor; couples complex to Gs and downstream cAMP signaling |

Without RAMP1, CLR binds adrenomedullin (via RAMP2/3) rather than CGRP. RAMP1 is therefore the **molecular determinant of CGRP selectivity** — the target of erenumab, which blocks the CLR/RAMP1 extracellular interface.

**Signaling cascades:**
- CGRP → CLR/RAMP1 → Gαs → adenylyl cyclase → ↑cAMP → **PKA activation** → vasodilation (KATP channel opening in smooth muscle), modulation of CGRP release, and neuronal sensitization
- β-arrestin recruitment → receptor internalization and ERK1/2 MAPK activation (independent signaling arm)
- Gαi signaling in some sensory neuron subtypes (inhibitory modulation)

**Receptor distribution relevant to migraine:**
- Trigeminal ganglion (TG) neurons — source of CGRP release
- Dural mast cells — CGRP drives histamine release, potentiating neurogenic inflammation
- Cerebral and dural blood vessel smooth muscle — vasodilation
- Trigeminal nucleus caudalis (TNC, C1–C2) — central sensitization
- Sphenopalatine ganglion — parasympathetic autonomic activation contributing to migraine autonomic features

## Function

### Vasodilation

CGRP is effective at picomolar concentrations, orders of magnitude more potent than acetylcholine or bradykinin. Mechanism:
- CGRP → smooth muscle CLR/RAMP1 → cAMP → PKA → phosphorylation of KATP channels → K⁺ efflux → membrane hyperpolarization → Ca²⁺ channel closure → smooth muscle relaxation and vasodilation
- Endothelium: CGRP → eNOS → nitric oxide → cGMP (secondary vasodilatory pathway)
- Vascular half-life ~7 minutes (cleared by neprilysin and carboxypeptidase N)

In the **dural vasculature**, CGRP-mediated vasodilation is a key step in migraine headache generation.

### Nociception and pain modulation

CGRP is expressed in 30–40% of small-diameter DRG and trigeminal ganglion neurons — the C-fibers and Aδ-fibers that transmit nociceptive signals:

- **Peripheral sensitization:** CGRP released at peripheral terminals sensitizes TRPV1 and TRPA1 channels on nociceptors, lowering pain threshold
- **Neurogenic inflammation:** CGRP (vasodilation) and co-released substance P (plasma extravasation) produce the cardinal features of neurogenic inflammation at dural terminals
- **Central sensitization:** CGRP released at TNC synapses potentiates NMDA receptor-mediated transmission → wind-up → allodynia (late migraine phase)
- **Dorsal horn modulation:** CGRP interneurons in spinal cord contribute to pain/itch gating circuits

### Cardiovascular and systemic roles

- **Cardiac protection:** CGRP in cardiac sensory neurons protects against ischemia-reperfusion injury; CGRP knockout mice show exaggerated infarct damage
- **Blood pressure:** CGRP contributes to vasodilatory tone; elevated in pulmonary arterial hypertension as a compensatory response
- **Gut motility:** βCGRP in enteric neurons modulates intestinal smooth muscle contractility

## Mechanism

### Trigeminovascular activation cascade in migraine

The **trigeminovascular hypothesis** (Moskowitz, 1984; validated by Edvinsson 1990s) positions CGRP as the central pain mediator:

**Step 1 — Cortical spreading depression (CSD):**
- In migraine with aura: a self-propagating wave of neuronal/glial depolarization travels at 3–5 mm/min across occipital cortex, generating aura symptoms (visual scotoma, spreading tingling)
- CSD activates trigeminal afferents innervating the overlying meninges via potassium and glutamate spillover → triggers the headache phase

**Step 2 — Trigeminal ganglion activation:**
- C-fibers and Aδ-fibers of the **trigeminal nerve (V1/ophthalmic division)** densely innervate dural blood vessels and pia mater
- TG neuron activation → antidromic CGRP release at dural terminals + orthodromic pain signal transmission centrally

**Step 3 — Neurogenic inflammation:**
- CGRP at dural terminals → CLR/RAMP1 on smooth muscle → vasodilation (dural arteries dilate 20–30%)
- Co-released substance P → NK1 receptors on endothelium → plasma protein extravasation (neurogenic edema)
- CGRP on dural mast cells → histamine release → further sensitization

**Step 4 — Central sensitization at TNC:**
- TG C-fibers synapse on neurons in the **trigeminal nucleus caudalis (TNC)** at cervical spinal cord C1–C2
- Sustained TNC activation + central CGRP release → NMDA receptor sensitization → **central sensitization** (allodynia, generalized hypersensitivity)
- TNC neurons → thalamus → somatosensory cortex (pain) + limbic system (affective dimension)

**Step 5 — Resolution:**
- Plasma CGRP normalizes within hours of migraine resolution or successful triptan/gepant treatment
- Descending PAG-raphe pathways provide endogenous pain suppression via serotonin and opioids

### Anti-CGRP pharmacology

| Drug class | Mechanism | Examples | Indication |
|:---|:---|:---|:---|
| **Anti-CGRP ligand mAbs** | Block free CGRP peptide | Fremanezumab, Galcanezumab, Eptinezumab (IV) | Prevention — monthly or quarterly dosing |
| **Anti-CGRP receptor mAb** | Block CLR/RAMP1 complex | Erenumab | Prevention — monthly SC injection |
| **Gepants** | Small-molecule CLR/RAMP1 antagonists | Rimegepant, Ubrogepant (acute); Atogepant, Rimegepant (prevention) | Acute treatment and/or prevention |
| **Ditans** | 5-HT1F agonist → TNC inhibition | Lasmiditan | Acute — no cardiovascular vasoconstriction |
| **Triptans** | 5-HT1B/D → vasoconstriction + ↓CGRP release | Sumatriptan, rizatriptan, eletriptan | Acute — contraindicated in cardiovascular disease |

**Anti-CGRP mAb efficacy:** Erenumab (ARISE trial) [^dodick-2018-erenumab-arise]: ~40% of patients achieved ≥50% reduction in monthly migraine days vs. 30% placebo; FDA-approved 2018. Fremanezumab, galcanezumab, and eptinezumab achieve similar ~40–50% responder rates with monthly or quarterly dosing. No cardiovascular safety signal has emerged despite theoretical concern given CGRP's vasodilatory role.

**Gepants:** Rimegepant (Nurtec ODT) is the first drug approved for both acute migraine treatment AND prevention. Unlike triptans, gepants carry no contraindication in cardiovascular disease. The proof-of-concept for oral CGRP receptor antagonism was established by Olesen et al. [^olesen-2004-cgrp-migraine] using IV olcegepant (BIBN 4096 BS) in 2004.

## Connections

**→ [Migraine](../../07-system/migraine/)**: CGRP released from trigeminal C-fibers mediates dural vasodilation and neurogenic inflammation in migraine; plasma CGRP rises during attacks and normalizes after successful triptan treatment; anti-CGRP mAbs (erenumab) reduce frequency ~50%; gepants (rimegepant) treat acute attacks.

**→ [Serotonin](../serotonin/)**: Triptans (5-HT1B/D agonists) abort migraine by constricting dural vessels and inhibiting trigeminal CGRP release; serotonin regulates CGRP release from TNC neurons; serotonin syndrome risk is low when combining triptans with SSRIs or SNRIs.

[^amara-1982-cgrp-discovery]: Amara SG, Jonas V, Rosenfeld MG, Ong ES, Evans RM. Alternative RNA processing in calcitonin gene expression generates mRNAs encoding different polypeptide products. *Nature.* 1982;298(5871):240-244. [doi:10.1038/298240a0](https://doi.org/10.1038/298240a0) · [PubMed 6285202](https://pubmed.ncbi.nlm.nih.gov/6285202/)
[^olesen-2004-cgrp-migraine]: Olesen J, Diener HC, Husstedt IW, et al. Calcitonin gene-related peptide receptor antagonist BIBN 4096 BS for the acute treatment of migraine. *N Engl J Med.* 2004;350(11):1104-1110. [doi:10.1056/NEJMoa030505](https://doi.org/10.1056/NEJMoa030505) · [PubMed 15014183](https://pubmed.ncbi.nlm.nih.gov/15014183/)
[^dodick-2018-erenumab-arise]: Dodick DW, Ashina M, Brandes JL, et al. ARISE: A Phase 3 randomized trial of erenumab for episodic migraine. *Cephalalgia.* 2018;38(6):1026-1037. [doi:10.1177/0333102418759786](https://doi.org/10.1177/0333102418759786) · [PubMed 29471679](https://pubmed.ncbi.nlm.nih.gov/29471679/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

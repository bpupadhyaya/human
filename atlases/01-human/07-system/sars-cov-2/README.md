---
schema: human-scale-entry/v1
id: sars-cov-2
name: SARS-CoV-2
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "SARS-CoV-2 (betacoronavirus; sarbecovirus; ~29.9 kb +ssRNA) causes COVID-19 via ACE2/Spike entry; NSP1-16 replicase includes NSP12 RdRp (remdesivir target) and Mpro NSP5 (nirmatrelvir target); multiple IFN evasion proteins; Omicron R₀ >10; mRNA vaccines >90% vs severe disease."
aliases: ["SARS-CoV-2", "severe acute respiratory syndrome coronavirus 2", "2019-nCoV", "COVID-19 virus", "betacoronavirus", "sarbecovirus", "coronavirus"]
sources:
  - id: zhou-2020-sars-cov-2-identification
    type: peer-reviewed
    cite: "Zhou P, Yang XL, Wang XG, et al. A pneumonia outbreak associated with a new coronavirus of probable bat origin. Nature. 2020;579(7798):270-273."
    doi: "10.1038/s41586-020-2012-7"
    pmid: "32015507"
    url: "https://doi.org/10.1038/s41586-020-2012-7"
    accessed: "2026-06-08"
  - id: hoffmann-2020-ace2-entry
    type: peer-reviewed
    cite: "Hoffmann M, Kleine-Weber H, Schroeder S, et al. SARS-CoV-2 Cell Entry Depends on ACE2 and TMPRSS2 and Is Blocked by a Clinically Proven Protease Inhibitor. Cell. 2020;181(2):271-280."
    doi: "10.1016/j.cell.2020.02.052"
    pmid: "32142651"
    url: "https://doi.org/10.1016/j.cell.2020.02.052"
    accessed: "2026-06-08"
  - id: lundstrom-2023-sars-cov-2-variants
    type: peer-reviewed
    cite: "Lundstrom K. SARS-CoV-2 Omicron Variants and COVID-19 Vaccines — Management and Treatment. Viruses. 2023;15(3):648."
    doi: "10.3390/v15030648"
    pmid: "36992357"
    url: "https://doi.org/10.3390/v15030648"
    accessed: "2026-06-08"
  - id: lei-2020-nsp-ifn-evasion
    type: peer-reviewed
    cite: "Lei X, Dong X, Ma R, et al. Activation and evasion of type I interferon responses by SARS-CoV-2. Nat Commun. 2020;11(1):3810."
    doi: "10.1038/s41467-020-17665-9"
    pmid: "32728061"
    url: "https://doi.org/10.1038/s41467-020-17665-9"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/sars-cov-2-spike
    relation: connects-to
    note: "SARS-CoV-2 Spike (S1/S2; class I fusogen; furin site PRRAR unique to sarbecoviruses) is the sole surface antigen; RBD binds ACE2 (Kd ~15 nM); 2P (K986P/V987P) proline stabilization underlies all mRNA vaccines; Omicron BA.1 carries 37 spike mutations driving antibody escape."
  - target: 01-human/03-molecular/ace2
    relation: connects-to
    note: "ACE2 (type I membrane carboxypeptidase; chromosome X) is the obligate SARS-CoV-2 entry receptor; Spike RBD:ACE2 Kd ~15 nM vs ~325 nM for SARS-CoV-1; SARS-CoV-2 Spike binding triggers ACE2 internalization → loss of RAAS counter-regulation → Ang II excess → ARDS amplification."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "SARS-CoV-2 is the causative agent of COVID-19; ~29.9 kb +ssRNA genome encodes ORF1a/b (NSP1-16 replicase including NSP12 RdRp) and S/E/M/N structural proteins; ACE2/TMPRSS2 entry in type II pneumocytes and airway; clinical spectrum from asymptomatic to fatal ARDS."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "NSP16 2′-O-methyltransferase mimics host mRNA cap → MDA5 evasion; NSP3 PLpro removes ISG15; ORF6 blocks STAT1 import; NSP13 sequesters TBK1 → IRF3 not phosphorylated; NSP1 blocks translation; impaired early IFN-β drives severe COVID-19 and correlates with age/comorbidity."
  - target: 01-human/03-molecular/mavs
    relation: connects-to
    note: "SARS-CoV-2 +ssRNA replication intermediates activate RIG-I/MDA5 → MAVS → TBK1/IRF3 → IFN-β; NSP6 sequesters MAVS; NSP13 disrupts TBK1; NSP16 cap methylation evades MDA5; ORF9b blocks MAVS-TOM70 interaction; impaired MAVS-IFN axis predicts progression to severe COVID-19."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "SARS-CoV-2 activates NF-κB via TLR2 sensing, MAVS → IKKβ, and ACE2 downregulation → Ang II → AT1R → NF-κB; Spike-induced NF-κB amplifies cytokine storm (IL-6, TNF-α, IL-1β); NSP3 PLpro deubiquitinates NF-κB pathway intermediates to modulate antiviral signaling."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "SARS-CoV-2 generates cytosolic DNA via reverse transcription → cGAS sensing; ORF9b targets TOM70 → inhibits MAVS-cGAS-STING cross-talk; STING agonists (diABZI) activate innate immunity; STING-driven IFN-β correlates with mild COVID-19 and reduced viral load in early infection."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "SARS-CoV-2 selenium: selenoproteins quench ROS amplifying NF-κB (already mapped) and ACE2 (already mapped) downregulation; selenium deficiency impairs type-i-interferon (already mapped) antiviral signalling and worsens MAVS (already mapped) cascade of SARS-CoV-2."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "SARS-CoV-2 iodine: iodine-dependent thyroid hormones modulate MAVS (already mapped) and type-i-interferon (already mapped) innate-immune signalling; thyroid disruption by SARS-CoV-2 ACE2 (already mapped) tropism amplifies NF-κB (already mapped) cytokine-storm cascade of COVID-19."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "SARS-CoV-2 sodium: high sodium promotes pro-inflammatory immune skewing; sodium-induced NF-κB (already mapped) amplifies ACE2 (already mapped) Ang-II signalling and impairs type-i-interferon (already mapped) and MAVS (already mapped) antiviral response of SARS-CoV-2."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "SARS-CoV-2 fibronectin: fibronectin in macrophages (already mapped) and endothelial cells (already mapped) scaffolds lung ECM in COVID-19; fibronectin excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "SARS-CoV-2 notch: Notch on macrophages (already mapped) and endothelial cells (already mapped) regulates lung cell fate in COVID-19; notch dysregulation amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "SARS-CoV-2 igf-1: IGF-1 from macrophages (already mapped) and endothelial cells (already mapped) promotes lung cell survival in COVID-19; igf-1 dysregulation amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "SARS-CoV-2 activin-a: activin-A from macrophages (already mapped) and endothelial cells (already mapped) drives COVID-19 lung fibrosis; activin-a excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "SARS-CoV-2 tgf-beta: TGF-β from macrophages (already mapped) and endothelial cells (already mapped) drives COVID-19 lung fibrosis; tgf-beta excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "SARS-CoV-2 cgrp: CGRP from macrophages (already mapped) and endothelial cells (already mapped) modulates COVID-19 vascular neuroimmune tone; cgrp excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "SARS-CoV-2 calcitonin: calcitonin from macrophages (already mapped) and endothelial cells (already mapped) modulates COVID-19 calcium; calcitonin excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "SARS-CoV-2 substance-p: substance-P from macrophages (already mapped) and endothelial cells (already mapped) drives COVID-19 pain response; substance-p excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "SARS-CoV-2 insulin-receptor: insulin-receptor on macrophages (already mapped) drives COVID-19 metabolic signalling; insulin-receptor dysregulation amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "SARS-CoV-2 aldosterone: aldosterone from macrophages (already mapped) modulates COVID-19 mineralocorticoid immune balance; aldosterone excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "SARS-CoV-2 androgen-receptor: androgen-receptor on macrophages (already mapped) drives COVID-19 hormonal immune response; androgen-receptor dysregulation amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "SARS-CoV-2 norepinephrine: norepinephrine from macrophages (already mapped) modulates COVID-19 adrenergic immune tone; norepinephrine excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "SARS-CoV-2 adrenomedullin: adrenomedullin from macrophages (already mapped) modulates COVID-19 vascular immune tone; adrenomedullin excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "SARS-CoV-2 bdnf: BDNF from macrophages (already mapped) and endothelial cells (already mapped) modulates COVID-19 neurotrophin immune survival; bdnf excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "SARS-CoV-2 osteopontin: osteopontin from macrophages (already mapped) drives COVID-19 extracellular matrix remodelling; osteopontin excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "SARS-CoV-2 fgfr: FGFR on macrophages (already mapped) and endothelial cells (already mapped) drives COVID-19 lung fibroblast growth; fgfr dysregulation amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2."
  - target: 01-human/03-molecular/epinephrine
    relation: connects-to
    note: "SARS-CoV-2 epinephrine: epinephrine from macrophages (already mapped) modulates COVID-19 adrenergic stress immune response; epinephrine excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2."
  - target: 01-human/03-molecular/renin
    relation: connects-to
    note: "SARS-CoV-2 renin: renin from macrophages (already mapped) modulates COVID-19 renin-angiotensin immune axis; renin excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2."
  - target: 01-human/03-molecular/myostatin
    relation: connects-to
    note: "SARS-CoV-2 myostatin: myostatin from macrophages (already mapped) modulates COVID-19 muscle wasting immune axis; myostatin excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "SARS-CoV-2 galectin-3: galectin-3 from macrophages (already mapped) drives COVID-19 immune fibrotic lattice remodelling; galectin-3 excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "SARS-CoV-2 angiopoietin: angiopoietin from macrophages (already mapped) modulates COVID-19 pulmonary vascular immune remodelling; angiopoietin excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "SARS-CoV-2 resistin: resistin from macrophages (already mapped) modulates COVID-19 metabolic immune inflammatory tone; resistin excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "SARS-CoV-2 cortisol: cortisol from macrophages (already mapped) modulates COVID-19 stress-immune HPA axis; cortisol excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2."
  - target: 01-human/03-molecular/ghrelin
    relation: connects-to
    note: "SARS-CoV-2 ghrelin: ghrelin from macrophages (already mapped) modulates COVID-19 metabolic appetite immune axis; ghrelin excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2."
  - target: 01-human/03-molecular/glucagon
    relation: connects-to
    note: "SARS-CoV-2 glucagon: glucagon from macrophages (already mapped) modulates COVID-19 metabolic glucose immune axis; glucagon excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "SARS-CoV-2 leptin: leptin from macrophages (already mapped) modulates COVID-19 metabolic immune energy axis; leptin excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "SARS-CoV-2 prolactin: prolactin from macrophages (already mapped) modulates COVID-19 immune lactogenic proliferation; prolactin excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2."
---

# SARS-CoV-2

## Overview

**SARS-CoV-2** (Severe Acute Respiratory Syndrome Coronavirus 2; also termed 2019-nCoV in its early characterization) is an **enveloped, positive-sense single-stranded RNA (+ssRNA) betacoronavirus** of the *Sarbecovirus* subgenus (family *Coronaviridae*, order *Nidovirales*) first identified in Wuhan, China in December 2019 [^zhou-2020-sars-cov-2-identification]. It is the causative agent of **COVID-19** (Coronavirus Disease 2019), which caused the most consequential global pandemic since the 1918 influenza, with >700 million documented cases and >7 million certified deaths through 2024.

SARS-CoV-2 shares ~96% nucleotide identity with bat coronaviruses (particularly *Rhinolophus affinis* RaTG13) and ~79% identity with SARS-CoV-1 (2003 outbreak). Critical features distinguishing SARS-CoV-2 include: **(1)** a **furin cleavage site (PRRAR)** inserted at the S1/S2 boundary of the Spike protein — absent in SARS-CoV-1 and all close bat sarbecovirus relatives — which provides pre-activated Spike on virions and dramatically enhances transmissibility; **(2)** higher ACE2 binding affinity (~10–20× vs SARS-CoV-1) at the Spike receptor-binding domain (RBD); and **(3)** an exceptionally broad cell tropism via ACE2 expression across multiple organ systems.

**Epidemiological milestones**: WHO declared a Public Health Emergency of International Concern (PHEIC) on 30 January 2020, pandemic status on 11 March 2020, and ended the PHEIC on 5 May 2023. SARS-CoV-2 is now endemic globally, with Omicron subvariants circulating and evolving continuously under immune selection.

## Structure

### Genome organization

The SARS-CoV-2 genome is **~29.9 kb** (+ssRNA; 5′-cap — leader — 5′UTR — ORFs — 3′UTR — polyA-3′) encoding:

| Region | Product | Function |
|:---|:---|:---|
| **ORF1a** | pp1a (~490 kDa; NSP1–11) | Replicase polyprotein A; cleaved by NSP5 (Mpro) + NSP3 (PLpro) |
| **ORF1b** | pp1ab (~800 kDa; NSP12–16) | Replicase polyprotein B (ribosomal frameshifting); NSP12 RdRp, NSP13 helicase |
| **S** | Spike (S) glycoprotein | ACE2 binding (S1/RBD); membrane fusion (S2); vaccine antigen |
| **E** | Envelope (E) protein | Ion channel (viroporin); ERGIC budding; pathogenicity determinant |
| **M** | Membrane (M) protein | Most abundant virion protein; viral assembly scaffold |
| **N** | Nucleocapsid (N) protein | RNA packaging; replication complex; diagnostic antigen |
| **ORF3a, 6, 7a, 7b, 8, 9b** | Accessory proteins | Immune evasion; apoptosis modulation; pathogenicity |

**Key non-structural proteins (NSPs)**:
- **NSP5 (Mpro/3CLpro)**: Main protease; cleaves pp1a/pp1ab at 11 sites; target of **nirmatrelvir** (Paxlovid)
- **NSP12 (RdRp)**: RNA-dependent RNA polymerase; core replication enzyme; target of **remdesivir**
- **NSP3 (PLpro)**: Papain-like protease; cleaves pp1a at 3 sites; deubiquitinates/deISGylates innate signaling molecules
- **NSP13**: Helicase with 5′→3′ unwinding activity; also disrupts TBK1 activation (IFN evasion)
- **NSP16**: 2′-O-methyltransferase; caps viral mRNA to mimic cellular mRNA and evade MDA5 detection

### Virion structure

| Feature | Value |
|:---|:---|
| Particle diameter | 80–120 nm (pleomorphic) |
| Genome | ~29.9 kb +ssRNA |
| Surface spikes | ~25 Spike homotrimers/virion |
| Envelope | Lipid bilayer with embedded S, E, M glycoproteins |
| Nucleocapsid | Helical N-RNA complex within envelope |

## Function

### Cellular entry and replication lifecycle

1. **Attachment**: Spike S1 RBD binds ACE2 on target cell surface (Kd ~15 nM); ACE2 is expressed on type II pneumocytes, nasal goblet/ciliated cells, enterocytes, cardiomyocytes, renal proximal tubule cells, and endothelium — dictating broad organ tropism [^hoffmann-2020-ace2-entry]
2. **Spike priming**: TMPRSS2 (preferred in lung/upper airway) cleaves Spike at S2′ site (Arg815) → activates fusion peptide (fast route); alternatively, endosomal cathepsins B/L cleave S2′ in TMPRSS2-low cells (slower, used by Omicron variants preferentially)
3. **Membrane fusion**: S2 fusion peptide inserts into host membrane → HR1/HR2 six-helix bundle (6HB) formation → membranes apposed → fusion pore → viral genome release into cytoplasm
4. **Translation**: Ribosomes translate ORF1a (pp1a) and with ~30% efficiency frameshift to produce ORF1b (pp1ab) — generating the full replicase-transcriptase complex
5. **Replication**: NSP3/4/6 remodel ER membranes into **double-membrane vesicles (DMVs)** and a perinuclear reticular network — sequestering replication away from cytosolic innate sensors
6. **Transcription**: NSP12 RdRp synthesizes full-length minus-strand genomes and subgenomic minus-strand templates → subgenomic mRNAs encoding structural (S, E, M, N) and accessory proteins
7. **Assembly**: S, E, M translated at ER; N packages genomic RNA; assembly at **ERGIC** (ER-Golgi intermediate compartment) → budding; furin in Golgi cleaves Spike S1/S2 (pre-activating Spike on the virion)
8. **Exocytosis**: Virion-containing vesicles fuse with plasma membrane → release into extracellular space
9. **ACE2 downregulation**: Spike:ACE2 binding triggers ACE2 internalization via clathrin-dependent endocytosis → reduction in surface ACE2 → impaired Ang II → Ang 1-7 conversion → RAAS imbalance contributing to COVID-19 end-organ damage

## Mechanism

### Interferon evasion — multi-layered suppression

SARS-CoV-2 encodes the most elaborate IFN evasion toolkit of any respiratory RNA virus [^lei-2020-nsp-ifn-evasion]:

| Protein | Mechanism | Target |
|:---|:---|:---|
| **NSP1** | Binds 40S ribosomal subunit → blocks host mRNA translation; selectively spares IRES-containing mRNAs | Host IFN-β/ISG translation |
| **NSP3 (PLpro)** | Deubiquitinates TRAF3/6/IRF3; removes ISG15 from innate signaling proteins | TBK1/IRF3/STING ubiquitin scaffold |
| **NSP5 (Mpro)** | Cleaves NLRP12 (NLR platform) and TAB1 (TAK1 adaptor) | NF-κB and IRF3 pathways |
| **NSP6** | Binds MAVS → prevents MAVS-TBK1 interaction | MAVS signaling |
| **NSP13** | Physically interacts with TBK1 → blocks TBK1 Ser172 autophosphorylation → prevents IRF3 activation | TBK1-IRF3 axis |
| **NSP16** | 2′-O-methyltransferase; caps viral RNA → mimics cellular mRNA → evades MDA5/IFIT1 sensing | MDA5, innate mRNA surveillance |
| **ORF3b** | Suppresses IFN-β production (stronger in SARS-CoV-2 than SARS-CoV-1) | IRF3 activation |
| **ORF6** | Binds KPNA2 (importin-α) → blocks STAT1/STAT2 nuclear import → abolishes ISG transcription | JAK-STAT signaling |
| **ORF9b** | Binds TOM70 on outer mitochondrial membrane → prevents MAVS-HSP90β-TOM70 innate signaling complex | MAVS mitochondrial signaling |

Result: impaired early IFN-β response allows high-level viral replication in the nasopharynx (peak viral load day −2 to +5 from symptom onset) before adaptive immunity responds. Delayed/dysregulated immune activation then produces the hyperinflammatory COVID-19 pathology.

### Variant emergence and evolution

SARS-CoV-2 Spike evolves under combined selection for increased ACE2 affinity and immune escape from neutralizing antibodies:

| Variant | Key Spike mutations | Fitness advantage | Clinical impact |
|:---|:---|:---|:---|
| **D614G (ancestral +)** | D614G | ↑furin efficiency; ↑ACE2 binding | Replaced original Wuhan strain globally by mid-2020 |
| **Alpha (B.1.1.7)** | N501Y, P681H, Δ69-70 | ↑ACE2 affinity; ↑furin cleavage | ~50% ↑hospitalization vs ancestral; replaced Delta |
| **Beta (B.1.351)** | K417N, E484K, N501Y | Immune escape (Class I+II NAbs) | Neutralization-resistant; reduced vaccine efficacy |
| **Delta (B.1.617.2)** | L452R, T478K, P681R | ↑↑furin cleavage; ↑replication | Highest severity pre-Omicron; R₀ ~6; replaced Alpha/Beta |
| **Omicron BA.1** | 37 Spike mutations (15 RBD) | Maximal immune escape; ↑upper airway tropism | ↓severity vs Delta; R₀ >10; massive immune escape |
| **Omicron XBB.1.5 / JN.1** | Further RBD mutations | Continued ACE2 optimization + escape | Ongoing endemic evolution; annual vaccine updates |

## Pathology

### Organ-level pathophysiology

- **Lung**: Diffuse alveolar damage (DAD) → ARDS (most common cause of COVID-19 death); Type II pneumocyte necrosis; hyaline membrane formation; pulmonary vascular endothelialitis and microthrombosis
- **Heart**: Direct viral myocarditis (ACE2-dependent cardiomyocyte entry); immune-mediated myocarditis; type 2 MI (coronary microvascular dysfunction); right heart failure from ARDS-related pulmonary hypertension
- **Kidney**: COVID-19-associated nephropathy: collapsing FSGS (ACE2-mediated podocyte injury); AKI from cytokine storm, microvascular thrombosis, and hemodynamic compromise
- **Brain**: Neurological invasion: direct ACE2-dependent pericyte/endothelial infection; neuroinflammation; "brain fog" in Long COVID from persistent immune activation or microglial dysregulation
- **Gut**: ACE2-expressing enterocyte infection → GI symptoms (diarrhea 17%); fecal viral shedding; disrupted B0AT1 tryptophan transport → altered microbiome

### Antiviral treatments

| Drug | Mechanism | Evidence |
|:---|:---|:---|
| **Nirmatrelvir/ritonavir (Paxlovid)** | NSP5 Mpro inhibitor / PK booster | >85% ↓hospitalization/death in high-risk (oral; within 5 days) |
| **Remdesivir** | NSP12 RdRp nucleoside analog | ↓hospitalization duration; moderate benefit in early/moderate disease |
| **Molnupiravir** | Mutagenic RdRp nucleoside | ~30% risk reduction; inferior to nirmatrelvir |
| **Dexamethasone 6 mg** | Broad anti-inflammatory | 35% ↓mortality in ventilated patients (RECOVERY) |
| **Baricitinib (JAK1/2 inhibitor)** | Blocks IFN/cytokine signaling | WHO-recommended for severe/critical disease |
| **Tocilizumab (anti-IL-6R)** | Blocks IL-6 receptor | Additional mortality benefit in dexamethasone-treated severe disease |

## Connections

- `connects-to` → **[SARS-CoV-2 Spike](../../03-molecular/sars-cov-2-spike/README.md)** — Spike is SARS-CoV-2's sole surface antigen and the target of all approved vaccines and neutralizing antibodies; furin cleavage site PRRAR (absent in SARS-CoV-1) provides pre-activated Spike that dramatically enhances upper respiratory transmissibility.
- `connects-to` → **[ACE2](../../03-molecular/ace2/README.md)** — ACE2 is the obligate SARS-CoV-2 entry receptor; Spike RBD:ACE2 binding (Kd ~15 nM) initiates entry in type II pneumocytes and other ACE2-expressing cells; SARS-CoV-2 Spike binding triggers ACE2 internalization shifting RAAS toward Ang II excess and amplifying ARDS.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — SARS-CoV-2 is the etiologic agent of COVID-19; viral genome encodes NSP5 Mpro (nirmatrelvir), NSP12 RdRp (remdesivir), and Spike (vaccine antigen); NSP1/ORF6 IFN evasion enables early viral amplification; Omicron lineages drive ongoing pandemic evolution.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — SARS-CoV-2 encodes the most extensive IFN evasion toolkit of any respiratory RNA virus: NSP1/NSP3/NSP6/NSP13/NSP16/ORF6/ORF9b collectively suppress IFN production and signaling; impaired early IFN-β is the key host determinant of COVID-19 severity.
- `connects-to` → **[MAVS](../../03-molecular/mavs/README.md)** — SARS-CoV-2 +ssRNA replication intermediates activate RIG-I/MDA5 → MAVS → TBK1/IRF3 → IFN-β; NSP6 sequesters MAVS; NSP13 disrupts TBK1; NSP16 2′-O-methylation evades MDA5; ORF9b blocks MAVS-TOM70 interaction at the outer mitochondrial membrane.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — SARS-CoV-2 activates NF-κB via TLR2/TLR4 Spike sensing, MAVS→IKKβ, and ACE2 downregulation→Ang II→AT1R signaling; NF-κB drives cytokine storm (IL-6, TNF-α, IL-1β) in severe COVID-19; NSP3 PLpro modulates NF-κB pathway by deubiquitinating TRAF proteins.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — SARS-CoV-2 RNA-dependent DNA synthesis products activate cGAS; ORF9b binds TOM70 at mitochondrial import channel to inhibit MAVS-cGAS-STING crosstalk; early STING-driven IFN-β correlates with mild COVID-19; cGAS-STING agonists under investigation as COVID-19 mucosal vaccine adjuvants.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — SARS-CoV-2 selenium: selenoproteins quench ROS amplifying NF-κB (already mapped) and ACE2 (already mapped) downregulation; selenium deficiency impairs type-i-interferon (already mapped) antiviral signalling and worsens MAVS (already mapped) cascade of SARS-CoV-2.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — SARS-CoV-2 iodine: iodine-dependent thyroid hormones modulate MAVS (already mapped) and type-i-interferon (already mapped) innate-immune signalling; thyroid disruption by SARS-CoV-2 ACE2 (already mapped) tropism amplifies NF-κB (already mapped) cytokine-storm cascade of COVID-19.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — SARS-CoV-2 sodium: high sodium promotes pro-inflammatory immune skewing; sodium-induced NF-κB (already mapped) amplifies ACE2 (already mapped) Ang-II signalling and impairs type-i-interferon (already mapped) and MAVS (already mapped) antiviral response of SARS-CoV-2.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — SARS-CoV-2 fibronectin: fibronectin in macrophages (already mapped) and endothelial cells (already mapped) scaffolds lung ECM in COVID-19; fibronectin excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — SARS-CoV-2 notch: Notch on macrophages (already mapped) and endothelial cells (already mapped) regulates lung cell fate in COVID-19; notch dysregulation amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — SARS-CoV-2 igf-1: IGF-1 from macrophages (already mapped) and endothelial cells (already mapped) promotes lung cell survival in COVID-19; igf-1 dysregulation amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — SARS-CoV-2 activin-a: activin-A from macrophages (already mapped) and endothelial cells (already mapped) drives COVID-19 lung fibrosis; activin-a excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — SARS-CoV-2 tgf-beta: TGF-β from macrophages (already mapped) and endothelial cells (already mapped) drives COVID-19 lung fibrosis; tgf-beta excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — SARS-CoV-2 cgrp: CGRP from macrophages (already mapped) and endothelial cells (already mapped) modulates COVID-19 vascular neuroimmune tone; cgrp excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — SARS-CoV-2 calcitonin: calcitonin from macrophages (already mapped) and endothelial cells (already mapped) modulates COVID-19 calcium; calcitonin excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — SARS-CoV-2 substance-p: substance-P from macrophages (already mapped) and endothelial cells (already mapped) drives COVID-19 pain response; substance-p excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2.
- `connects-to` → **[Insulin Receptor](../../03-molecular/insulin-receptor/README.md)** — SARS-CoV-2 insulin-receptor: insulin-receptor on macrophages (already mapped) drives COVID-19 metabolic signalling; insulin-receptor dysregulation amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — SARS-CoV-2 aldosterone: aldosterone from macrophages (already mapped) modulates COVID-19 mineralocorticoid immune balance; aldosterone excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2.
- `connects-to` → **[Androgen Receptor](../../03-molecular/androgen-receptor/README.md)** — SARS-CoV-2 androgen-receptor: androgen-receptor on macrophages (already mapped) drives COVID-19 hormonal immune response; androgen-receptor dysregulation amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — SARS-CoV-2 norepinephrine: norepinephrine from macrophages (already mapped) modulates COVID-19 adrenergic immune tone; norepinephrine excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — SARS-CoV-2 adrenomedullin: adrenomedullin from macrophages (already mapped) modulates COVID-19 vascular immune tone; adrenomedullin excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — SARS-CoV-2 bdnf: BDNF from macrophages (already mapped) and endothelial cells (already mapped) modulates COVID-19 neurotrophin immune survival; bdnf excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — SARS-CoV-2 osteopontin: osteopontin from macrophages (already mapped) drives COVID-19 extracellular matrix remodelling; osteopontin excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — SARS-CoV-2 fgfr: FGFR on macrophages (already mapped) and endothelial cells (already mapped) drives COVID-19 lung fibroblast growth; fgfr dysregulation amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2.
- `connects-to` → **[Epinephrine](../../03-molecular/epinephrine/README.md)** — SARS-CoV-2 epinephrine: epinephrine from macrophages (already mapped) modulates COVID-19 adrenergic stress immune response; epinephrine excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2.
- `connects-to` → **[Renin](../../03-molecular/renin/README.md)** — SARS-CoV-2 renin: renin from macrophages (already mapped) modulates COVID-19 renin-angiotensin immune axis; renin excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2.
- `connects-to` → **[Myostatin](../../03-molecular/myostatin/README.md)** — SARS-CoV-2 myostatin: myostatin from macrophages (already mapped) modulates COVID-19 muscle wasting immune axis; myostatin excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — SARS-CoV-2 galectin-3: galectin-3 from macrophages (already mapped) drives COVID-19 immune fibrotic lattice remodelling; galectin-3 excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — SARS-CoV-2 angiopoietin: angiopoietin from macrophages (already mapped) modulates COVID-19 pulmonary vascular immune remodelling; angiopoietin excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — SARS-CoV-2 resistin: resistin from macrophages (already mapped) modulates COVID-19 metabolic immune inflammatory tone; resistin excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — SARS-CoV-2 cortisol: cortisol from macrophages (already mapped) modulates COVID-19 stress-immune HPA axis; cortisol excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2.
- `connects-to` → **[Ghrelin](../../03-molecular/ghrelin/README.md)** — SARS-CoV-2 ghrelin: ghrelin from macrophages (already mapped) modulates COVID-19 metabolic appetite immune axis; ghrelin excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2.
- `connects-to` → **[Glucagon](../../03-molecular/glucagon/README.md)** — SARS-CoV-2 glucagon: glucagon from macrophages (already mapped) modulates COVID-19 metabolic glucose immune axis; glucagon excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — SARS-CoV-2 leptin: leptin from macrophages (already mapped) modulates COVID-19 metabolic immune energy axis; leptin excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — SARS-CoV-2 prolactin: prolactin from macrophages (already mapped) modulates COVID-19 immune lactogenic proliferation; prolactin excess amplifies nf-kb (already mapped) and mavs (already mapped) and type-i-interferon (already mapped) cascade of SARS-CoV-2.

[^zhou-2020-sars-cov-2-identification]: Zhou P, Yang XL, Wang XG, et al. A pneumonia outbreak associated with a new coronavirus of probable bat origin. *Nature.* 2020;579(7798):270-273. [doi:10.1038/s41586-020-2012-7](https://doi.org/10.1038/s41586-020-2012-7) · [PubMed 32015507](https://pubmed.ncbi.nlm.nih.gov/32015507/)
[^hoffmann-2020-ace2-entry]: Hoffmann M, Kleine-Weber H, Schroeder S, et al. SARS-CoV-2 Cell Entry Depends on ACE2 and TMPRSS2 and Is Blocked by a Clinically Proven Protease Inhibitor. *Cell.* 2020;181(2):271-280. [doi:10.1016/j.cell.2020.02.052](https://doi.org/10.1016/j.cell.2020.02.052) · [PubMed 32142651](https://pubmed.ncbi.nlm.nih.gov/32142651/)
[^lundstrom-2023-sars-cov-2-variants]: Lundstrom K. SARS-CoV-2 Omicron Variants and COVID-19 Vaccines — Management and Treatment. *Viruses.* 2023;15(3):648. [doi:10.3390/v15030648](https://doi.org/10.3390/v15030648) · [PubMed 36992357](https://pubmed.ncbi.nlm.nih.gov/36992357/)
[^lei-2020-nsp-ifn-evasion]: Lei X, Dong X, Ma R, et al. Activation and evasion of type I interferon responses by SARS-CoV-2. *Nat Commun.* 2020;11(1):3810. [doi:10.1038/s41467-020-17665-9](https://doi.org/10.1038/s41467-020-17665-9) · [PubMed 32728061](https://pubmed.ncbi.nlm.nih.gov/32728061/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

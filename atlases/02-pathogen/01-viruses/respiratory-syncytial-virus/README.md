---
schema: pathogen-entry/v1
id: respiratory-syncytial-virus
name: Respiratory Syncytial Virus
atlas: 02-pathogen
scale: 01-viruses
status: draft
last_reviewed: 2026-06-05
summary: "Pneumoviridae; (−)ssRNA ~15.2 kb; enveloped. Two subgroups (A/B). Leading cause of severe LRTI (bronchiolitis, pneumonia) in infants globally. NS1/NS2 suppress IFN; prefusion F protein is the key neutralisation target for vaccines/mAbs."
aliases: ["RSV", "RSV-A", "RSV-B", "hRSV", "RSV type A", "RSV type B", "Orthopneumovirus"]
sources:
  - id: mandell-principles
    type: textbook
    cite: "Bennett JE, Dolin R, Blaser MJ. Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases. 9th ed. Elsevier; 2020."
    url: "https://www.elsevier.com/books/mandell-douglas-and-bennetts-principles-and-practice-of-infectious-diseases/bennett/978-0-323-48255-4"
    accessed: "2026-06-05"
  - id: fields-virology
    type: textbook
    cite: "Knipe DM, Howley PM, eds. Fields Virology. 7th ed. Wolters Kluwer; 2021."
    url: "https://www.lww.com/product/9781975112547"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/04-cellular/type-ii-pneumocyte
    relation: infects
    note: "RSV infects bronchial and alveolar epithelium including type II pneumocytes; F protein mediates membrane fusion; infected cells form syncytia (multinucleate giant cells); epithelial necrosis and mucus plugging cause airway obstruction in infant bronchiolitis."
  - target: 01-human/06-organ/lung
    relation: damages
    note: "RSV bronchiolitis in infants: diffuse bronchiolar inflammation → epithelial necrosis → mucus and cellular debris plugging → air trapping, atelectasis, V/Q mismatch, hypoxia; adults/elderly: RSV pneumonia with exacerbation of underlying COPD or heart failure."
  - target: 01-human/07-system/respiratory-system
    relation: damages
    note: "RSV is the most common cause of severe LRTI (bronchiolitis, pneumonia) in infants; 3.6 million annual hospitalisations globally; NS1/2 proteins suppress IFN response; RSV reinfection occurs throughout life due to poor immunological memory."
  - target: 01-human/07-system/immune-system
    relation: damages
    note: "RSV NS1 (STAT2 degradation) and NS2 (IRF3 degradation) suppress IFN-α/β response for 24–48h post-infection; G protein CX3C motif depletes CX3CR1+ memory CD8+ T cells; RSV-induced immune evasion enables reinfection across the lifespan."
---

# Respiratory Syncytial Virus

## Overview

Respiratory syncytial virus (RSV) is the **most important cause of severe lower respiratory tract infection (LRTI) in infants and young children** worldwide — responsible for approximately **3.6 million hospitalisations and 100,000 deaths annually in children under 5 years**, with the greatest burden in low- and middle-income countries. It is also an underappreciated cause of pneumonia and mortality in the elderly (≥65 years) and immunocompromised patients, where it causes morbidity and mortality rivalling seasonal influenza [^mandell-principles].

RSV belongs to the family **Pneumoviridae** (reclassified from Paramyxoviridae in 2016), genus **Orthopneumovirus**. Its genome is a non-segmented, negative-sense single-stranded RNA (~15.2 kb). Two subgroups, **RSV-A** and **RSV-B**, co-circulate annually worldwide, distinguished primarily by approximately **50% amino acid divergence** in the heavily glycosylated attachment protein G [^fields-virology].

RSV is notable for causing **reinfection throughout life** without conferring durable protective immunity — a consequence of its potent innate immune evasion (NS1/NS2 proteins), the high antigenic variability of G protein, and T cell memory dysfunction mediated by the G protein CX3C motif.

A major breakthrough in the 2020s has been the **stabilised prefusion F protein (prefF)** as the dominant vaccine and monoclonal antibody target: the prefusion conformation exposes neutralising epitopes (particularly site Ø) that are hidden in the post-fusion form, and prefF-based immunogens elicit far superior neutralising antibody responses.

## Structure

### Virion Architecture

| Component | Description |
|:---|:---|
| **Envelope** | Host-derived lipid bilayer; ~150–300 nm diameter; pleomorphic (spherical to filamentous) |
| **F protein (Fusion)** | Class I fusion protein; homotrimer of F1/F2 disulfide-linked heterodimers; undergoes irreversible prefusion → postfusion conformational change; primary neutralisation target |
| **G protein (Attachment)** | Heavily O-glycosylated; mucin-like; binds heparan sulfate proteoglycans and CX3CR1 (fractalkine receptor); contains conserved CX3C motif (fractalkine mimic); ~50% amino acid divergence between RSV-A and RSV-B |
| **SH protein (Small hydrophobic)** | Viroporin; inhibits TNF-α-induced NF-κB signalling → ↓inflammatory amplification |
| **M protein (Matrix)** | Lines inner envelope; coordinates assembly and budding |
| **M2-1** | Transcriptional processivity factor; part of cytoplasmic inclusion bodies |
| **M2-2** | Regulates balance between transcription and replication |
| **N protein** | Encapsidates genomic RNA; N-RNA forms helical nucleocapsid |
| **L protein (Large/RdRp)** | RNA-dependent RNA polymerase; methyltransferase activity; target of nucleoside analogues |

### Genome Organisation

RSV genome: **3′-NS1-NS2-N-P-M-SH-G-F-M2-L-5′** (10 genes encoding 11 proteins, with M2 encoding M2-1 and M2-2 from the same gene by overlapping ORFs).

| Gene | Protein(s) | Key function |
|:---:|:---|:---|
| NS1 | Non-structural 1 | IFN antagonist: binds TRIM25, HERC2 (disrupts RIG-I ubiquitination); targets STAT2 for proteasomal degradation |
| NS2 | Non-structural 2 | IFN antagonist: degrades IRF3; impairs IFN-β transcription |
| N | Nucleoprotein | RNA encapsidation; forms helical RNP with genomic RNA |
| P | Phosphoprotein | Polymerase cofactor; recruits L to template |
| M | Matrix protein | Assembly; virion shape; interacts with RNP and envelope |
| SH | Small hydrophobic | Viroporin; blocks TNF-α NF-κB signalling |
| G | Attachment glycoprotein | Cell attachment; CX3CR1/fractalkine receptor binding; immune modulation |
| F | Fusion glycoprotein | Membrane fusion; cell-cell fusion → syncytia; primary vaccine/mAb target |
| M2 | M2-1 + M2-2 | Transcriptional processivity (M2-1); transcription/replication balance (M2-2) |
| L | Large protein (RdRp) | Polymerase + capping + methyltransferase |

### Prefusion vs Postfusion F Protein

The F protein conformational state is central to RSV immunobiology:

| Feature | Prefusion F (prefF) | Postfusion F |
|:---|:---|:---|
| **Structure** | Metastable trimer; "lollipop" head | Stable 6-helix bundle; elongated rod |
| **Key neutralising epitope** | **Site Ø** (apex of prefF trimer); highest-potency neutralisation; absent in postfusion | Sites II and IV (shared); site Ø absent |
| **Spontaneous stability** | Unstable — converts irreversibly to postfusion | Stable end state |
| **Stabilisation strategies** | "DS-Cav1" mutations (S155C/S290C + S190F/V207L); "SC-TM" and other engineered variants | Not needed |
| **Vaccine basis** | Abrysvo (Pfizer) prefF subunit; mRESVIA (Moderna) mRNA encoding prefF | Older candidates (lower efficacy) |
| **mAb target** | Nirsevimab (sites II + Ø); palivizumab (site II) | Palivizumab (site II only) |

## Infection Mechanism

### Cell Tropism and Entry

**Primary target cells:** Ciliated airway epithelial cells (nasal, tracheal, bronchial), type II alveolar pneumocytes; secondary: airway smooth muscle cells, macrophages, dendritic cells.

1. **Attachment:** G protein binds **heparan sulfate proteoglycans** (ubiquitous on cell surfaces) and **CX3CR1** (fractalkine receptor, expressed on DCs, NK cells, CX3CR1+ T cells). This dual-receptor engagement broadens tropism and enables immune cell targeting.
2. **Fusion:** F protein undergoes refolding → insertion of hydrophobic fusion peptide into the target membrane → 6-helix bundle formation (heptad repeat collapse) → membrane merger → viral RNP delivered into cytoplasm.
3. **Replication compartments:** RSV replicates in cytoplasmic **inclusion bodies (IBs)** — liquid-liquid phase-separated condensates of N-RNA + P + M2-1 + L. IBs are the sites of transcription and genome replication.
4. **Budding:** New virions bud from the apical surface of polarised epithelial cells.
5. **Syncytium formation:** F protein expressed on the infected cell surface drives fusion with neighbouring cells → **multinucleated syncytia** (the defining cytopathic effect giving RSV its name).

### Immune Evasion

RSV deploys multiple overlapping strategies to delay and suppress innate immune responses:

| Protein | Mechanism |
|:---|:---|
| **NS1** | Binds TRIM25 and HERC2 ubiquitin ligases → impairs RIG-I K63-ubiquitination → ↓RIG-I activation; targets STAT2 for proteasomal degradation → blunts IFN-α/β signalling |
| **NS2** | Directly degrades IRF3 via Elongin C-Cullin ubiquitin E3 ligase → prevents IFN-β promoter activation |
| **NS1 + NS2 together** | Delay the host IFN response by 24–48 h post-infection → establishes the replication window enabling high viral burdens |
| **G protein CX3C motif** | Fractalkine mimic; binds CX3CR1 on CX3CR1+ memory CD8+ T cells → impairs T cell migration and function → reduced T cell memory formation → reinfection throughout life |
| **SH protein** | Blocks TNF-α-induced NF-κB signalling → ↓proinflammatory cytokine amplification loop |

## Host Interactions

### Age-Dependent Clinical Impact

RSV causes strikingly different disease severity across age groups, determined by airway calibre, immunological status, and pre-existing medical conditions:

**Infants (<12 months):**
- Anatomically small airways are easily obstructed by inflammatory oedema and mucus → bronchiolitis is the dominant syndrome.
- RSV accounts for 60–75% of all bronchiolitis and ~25% of all pneumonia hospitalisations in infants.
- RSV is the **single leading cause of infant hospitalisation** in the USA (~58,000/year) and globally.
- Premature infants, those with congenital heart disease (CHD), chronic lung disease (CLD/BPD), or Down syndrome are at highest risk for severe disease.

**Adults and elderly (≥65 years):**
- RSV causes 177,000+ adult hospitalisations per year in the USA alone.
- Mortality in elderly RSV pneumonia is comparable to influenza; exacerbates underlying COPD, CHF, and asthma.
- RSV-A and RSV-B alternate in predominance across seasons; subgroup A generally associated with slightly more severe disease.

**Immunocompromised:**
- HSCT recipients: RSV upper RTI progresses to LRTI in 25–40%; LRTI mortality 30–90% in early post-engraftment period.
- Ribavirin ± IVIG used in high-risk settings with limited evidence.

### Pathogenesis of Bronchiolitis

Infant bronchiolitis represents a unique immunopathological syndrome:

1. RSV infects ciliated bronchiolar epithelial cells → necrosis → sloughed epithelial cells + mucus + inflammatory cells form **intraluminal plugs**.
2. Peribronchiolar lymphocytic infiltration → submucosal oedema → airway wall thickening.
3. Plug formation → **air trapping** (check-valve obstruction) → hyperinflation + atelectasis downstream of completely obstructed airways.
4. **Ventilation-perfusion (V/Q) mismatch** → hypoxaemia → the clinical hallmark.
5. Unlike adults, infants cannot generate sufficient expiratory force to clear plugs; small airway radius amplifies resistance (resistance ∝ 1/r⁴ by Poiseuille's law).

## Connections

- **Infects** → [Type II pneumocyte](../../../01-human/04-cellular/type-ii-pneumocyte/README.md): RSV infects bronchial and alveolar epithelium including type II pneumocytes; F protein mediates membrane fusion and syncytium formation; epithelial necrosis and mucus plugging of small airways cause airway obstruction in infant bronchiolitis.
- **Damages** → [Lung](../../../01-human/06-organ/lung/README.md): RSV bronchiolitis in infants causes diffuse bronchiolar inflammation, epithelial necrosis, mucus/cellular debris plugging, air trapping, atelectasis, and V/Q mismatch with hypoxia; in adults and elderly, RSV pneumonia exacerbates underlying COPD and cardiac failure.
- **Damages** → [Respiratory system](../../../01-human/07-system/respiratory-system/README.md): RSV is the most common cause of severe LRTI (bronchiolitis, pneumonia) in infants; responsible for 3.6 million annual hospitalisations globally; NS1/2 proteins suppress the IFN response; reinfection occurs throughout life due to incomplete immunological memory.
- **Damages** → [Immune system](../../../01-human/07-system/immune-system/README.md): RSV NS1 (STAT2 degradation) and NS2 (IRF3 degradation) suppress IFN-α/β signalling for 24–48 h post-infection; G protein CX3C motif depletes CX3CR1+ memory CD8+ T cells; together these mechanisms enable reinfection across the entire lifespan.

## Pathology

### Clinical Syndromes by Age

| Syndrome | Age group | Key features |
|:---|:---|:---|
| **Bronchiolitis** | Infants <12 months | Wheeze, tachypnoea, intercostal/subcostal recession, hypoxia, feeding difficulty; most common cause of infant hospitalisation |
| **Croup** | 1–5 years | Barking cough, stridor, hoarseness; RSV is second most common cause after parainfluenza |
| **Pneumonia** | All ages | Bilateral infiltrates, more severe in infants and elderly |
| **Common cold** | Older children and adults | Rhinorrhoea, mild cough; generally self-limiting |
| **Exacerbation of COPD/asthma** | Adults | RSV triggers exacerbations; often underdiagnosed |
| **Severe LRTI** | Elderly ≥65 years | 177,000+ US hospitalisations/year; mortality comparable to influenza |
| **Disseminated/fatal RSV** | Immunocompromised (HSCT, haematological malignancy) | 30–90% mortality post-LRTI in early post-HSCT period |

### Prevention

| Product | Type | Target population | Efficacy |
|:---|:---|:---|:---|
| **Nirsevimab (Beyfortus)** | Anti-prefF bispecific mAb (sites II + Ø); YTE Fc modification → t½ ~71 days | All infants ≤8 months; second season for high-risk children | >75% against RSV-LRTI hospitalisation in healthy term infants (MELODY RCT) |
| **Palivizumab (Synagis)** | Anti-F site II mAb (postfusion epitope); monthly IM | High-risk: premature infants <29 weeks, CHD, CLD | ~55% reduction in RSV hospitalisation; now largely superseded by nirsevimab |
| **Abrysvo (Pfizer)** | Bivalent prefF subunit (RSV-A + RSV-B); AS01B adjuvant-free | Maternal immunisation (32–36 weeks gestation); adults ≥60 years | >80% efficacy for infant RSV-LRTI within 6 months post-partum (MATISSE trial); >66% in adults ≥60 |
| **mRESVIA (Moderna)** | mRNA encoding prefF | Adults ≥60 years | First licensed mRNA vaccine outside COVID-19; >83% efficacy in trials |

### Treatment

| Approach | Details |
|:---|:---|
| **Supportive care** | Mainstay for all ages: supplemental oxygen, nasogastric feeding in infants, CPAP/high-flow nasal cannula (HFNC) |
| **Ribavirin (aerosolised or IV)** | RSV RNA polymerase inhibitor; limited RCT evidence; reserved for severe RSV in HSCT/immunocompromised patients ± IVIG |
| **Bronchodilators** | Salbutamol/albuterol: minimal benefit in bronchiolitis (Cochrane review negative); not routinely recommended |
| **Corticosteroids** | No proven benefit in infant bronchiolitis; may worsen outcomes |
| **IVIG/palivizumab** | Used post-exposure prophylaxis in HSCT recipients; no proven treatment benefit in established RSV LRTI |

[^mandell-principles]: Bennett JE, Dolin R, Blaser MJ. *Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases.* 9th ed. Elsevier; 2020.
[^fields-virology]: Knipe DM, Howley PM, eds. *Fields Virology.* 7th ed. Wolters Kluwer; 2021.

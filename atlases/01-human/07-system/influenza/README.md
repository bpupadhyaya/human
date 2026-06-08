---
schema: human-scale-entry/v1
id: influenza
name: Influenza
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Influenza A/B (orthomyxovirus; segmented negative-sense RNA) causes seasonal epidemics (H1N1, H3N2) and pandemics (1918 H1N1 killed ~50M; H5N1 mortality 60%); NS1 evades RIG-I/MAVS/STAT1; oseltamivir inhibits neuraminidase; baloxavir targets PA; annual vaccines 40-60% effective."
aliases: ["influenza", "flu", "influenza A", "influenza B", "H1N1", "H3N2", "H5N1", "avian influenza", "seasonal flu", "pandemic influenza", "orthomyxovirus", "hemagglutinin", "neuraminidase", "oseltamivir", "Tamiflu", "baloxavir"]
sources:
  - id: taubenberger-2006-influenza-pandemics
    type: peer-reviewed
    cite: "Taubenberger JK, Morens DM. 1918 Influenza: the mother of all pandemics. Emerg Infect Dis. 2006;12(1):15-22."
    doi: "10.3201/eid1201.050979"
    pmid: "16494711"
    url: "https://doi.org/10.3201/eid1201.050979"
    accessed: "2026-06-08"
  - id: who-influenza-seasonal
    type: clinical-guideline
    cite: "World Health Organization. Influenza (Seasonal) Fact Sheet. Geneva: WHO; 2023."
    url: "https://www.who.int/news-room/fact-sheets/detail/influenza-(seasonal)"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/mavs
    relation: connects-to
    note: "Influenza 5′ppp ssRNA activates RIG-I → TRIM25 → MAVS → TBK1/IRF3 → IFN-β; NS1 blocks TRIM25-mediated RIG-I ubiquitination and sequesters dsRNA → impairs MAVS activation; RIG-I/MAVS is the primary innate sensor for influenza A in respiratory epithelium."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Influenza RIG-I/MAVS → IRF3 → IFN-β in epithelial cells; pDC TLR7 → IFN-α; NS1 blocks IRF3 and dsRNA sensing; H5N1 paradoxically induces high IFN-β → cytokine storm; pandemic strains differ from seasonal strains primarily in NS1 IFN antagonism potency."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "Influenza NS1 blocks ISGF3 (STAT1/STAT2/IRF9) by dsRNA sequestration and TRIM25 inhibition; PA-X degrades host mRNAs; H5N1 overcomes STAT1/SOCS1 feedback → hyperinflammation; NS1 IFN antagonism is the primary virulence difference between pandemic and seasonal influenza strains."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Influenza M2 proton channel and PB1-F2 (mitochondrial targeting) activate NLRP3 → IL-1β + IL-18; NLRP3-mediated IL-1β amplifies cytokine storm in H5N1 and 1918 H1N1 pneumonia; NLRP3 genetic variants are associated with influenza severity and ASC speck formation in macrophages."
  - target: 01-human/03-molecular/rig-i
    relation: connects-to
    note: "Influenza A 5′ppp genomic ssRNA and dsRNA replication intermediates are the canonical RIG-I ligands; NS1 blocks RIG-I by sequestering dsRNA and inhibiting TRIM25-mediated K63-ubiquitination of RIG-I CARDs; NS1 IFN antagonism strength correlates with pandemic potential."
  - target: 01-human/03-molecular/influenza-ha
    relation: connects-to
    note: "HA is the primary influenza vaccine antigen; HA1 head antigenic sites A-E undergo annual drift requiring reformulation; HA2 stalk BNAbs are the basis of universal influenza vaccine strategies; α2,6-SA vs α2,3-SA receptor binding specificity determines human transmissibility."
---

# Influenza

## Overview

**Influenza** is an acute respiratory infection caused by **influenza viruses** (family *Orthomyxoviridae*), with four types recognized in humans: influenza A, B, C, and D. Influenza A and B cause clinically significant human disease: **influenza A** (with subtypes defined by hemagglutinin H1-H18 and neuraminidase N1-N11) is responsible for all documented pandemics and the most severe seasonal epidemics; **influenza B** (lineages Yamagata and Victoria) causes significant seasonal morbidity, especially in children.

Globally, seasonal influenza causes an estimated **3–5 million severe cases** and **290,000–650,000 respiratory deaths** annually (WHO). The 1918 Spanish influenza pandemic (H1N1) — the most catastrophic acute infectious disease event in recorded history — killed an estimated 50–100 million people worldwide [^taubenberger-2006-influenza-pandemics]. The ongoing threat of **highly pathogenic avian influenza H5N1** (case fatality rate ~60% in confirmed human cases) represents one of the highest-priority pandemic preparedness concerns.

**Clinical spectrum:**
- **Uncomplicated influenza**: Abrupt-onset fever (38–40°C), myalgia ("flu"), headache, malaise, dry cough, sore throat; self-limiting 5–7 days
- **Complicated influenza**: Primary viral pneumonia, secondary bacterial pneumonia (*S. aureus*, *S. pneumoniae*, *H. influenzae*), myocarditis, encephalitis
- **Severe/fatal influenza**: ARDS, multi-organ failure; cytokine storm (particularly H5N1 and 1918 H1N1); Reye syndrome (children: aspirin + influenza → mitochondrial dysfunction)

High-risk groups: elderly (≥65), children <2 years, pregnancy, immunocompromised, obesity, chronic cardiopulmonary/metabolic disease.

## Structure

### Influenza virus biology

Influenza A is an enveloped virus (~120 nm diameter) with an **8-segment negative-sense ssRNA genome**:

| Segment | Protein(s) | Function |
|---------|-----------|----------|
| 1 | PB2 | Cap-binding subunit of RdRp; binds 5′ m7GTP cap of host mRNAs for cap-snatching |
| 2 | PB1, PB1-F2 | PB1: RNA polymerase catalytic subunit; PB1-F2: mitochondria-targeting pro-apoptotic peptide; activates NLRP3 |
| 3 | PA | Endonuclease subunit of RdRp; cleaves snatched host cap primers; target of baloxavir |
| 4 | HA (hemagglutinin) | Sialic acid receptor binding (α2,6 SA — human upper airway; α2,3 SA — avian/lower airway); membrane fusion; neutralizing antibody target; 18 subtypes |
| 5 | NP (nucleoprotein) | Encapsidates genomic RNA; vRNP nuclear import/export |
| 6 | NA (neuraminidase) | Sialidase: cleaves sialic acid → virion release from cells and mucus barrier penetration; target of oseltamivir, zanamivir, peramivir; 11 subtypes |
| 7 | M1, M2 | M1: matrix protein, virion structure; M2: proton channel, endosomal uncoating; amantadine target (now largely resistant) |
| 8 | NS1, NEP/NS2 | NS1: multifunctional IFN antagonist; NEP: nuclear export of vRNPs |

### Key surface glycoproteins

**Hemagglutinin (HA):**
- HA0 precursor cleaved to HA1+HA2 (disulfide-linked) by host serine proteases (TMPRSS2, plasmin, furin for highly pathogenic strains)
- HA1 globular head: receptor binding domain; hypervariable; target of strain-specific neutralizing antibodies
- HA2 stalk: membrane fusion domain; conserved; target of broadly neutralizing antibodies (research/universal vaccine focus)
- HA binding specificity: α2,6-linked sialic acid (human upper respiratory epithelium) vs α2,3-linked (avian intestinal epithelium; human lower respiratory) — key determinant of human transmissibility

**Neuraminidase (NA):**
- Box-shaped tetramer on virion surface
- Sialidase activity cleaves sialic acid from HA-receptor complexes → releases new virions; also cleaves mucus glycoproteins allowing viral spread through mucus layer
- Active site is highly conserved across subtypes → druggable target with oseltamivir, zanamivir, peramivir, laninamivir

### Antigenic variation

- **Antigenic drift**: Accumulation of point mutations in HA/NA surface epitopes → immune evasion; basis for annual vaccine reformulation
- **Antigenic shift**: Reassortment of genome segments between human and animal (avian, swine) influenza A strains → novel HA/NA subtypes → pandemic potential (no pre-existing population immunity)

## Function

### Viral entry and replication cycle

1. **Attachment**: HA1 binds sialic acid on respiratory epithelium → endocytosis via clathrin-mediated pathway
2. **Fusion**: Endosomal acidification (pH 5–6) → HA conformational change (HA2 spring-loaded) → membrane fusion → vRNP release into cytoplasm; M2 proton channel acidifies virion interior simultaneously
3. **Nuclear import**: vRNPs transported to nucleus via importin-α/β
4. **Transcription/Replication**: Cap-snatching by PB2/PA → capped viral mRNA synthesis by PB1; cRNA synthesis (antigenomic positive-sense) → vRNA amplification
5. **Assembly**: vRNPs exported via NEP/M1 to cytoplasm → transported to apical plasma membrane; HA and NA traffic via Golgi
6. **Budding/Release**: Virion buds from plasma membrane; NA cleaves sialic acid → virion released (without NA: virion clusters on cell surface)

### Innate immune response

| Time | Host response | Viral countermeasure |
|------|---------------|---------------------|
| 0–6 h | RIG-I detects 5′ppp ssRNA → MAVS → IRF3 → IFN-β | NS1 sequesters dsRNA, blocks TRIM25-mediated RIG-I ubiquitination |
| 6–24 h | IFN-β → IFNAR → STAT1/STAT2 → ISGs (MX1, OAS1, PKR) | NS1 blocks ISGF3; PA-X degrades host mRNAs |
| 24–48 h | NK cells, pDC IFN-α; macrophage/DC activation | NS1 binds CPSF30 → blocks host mRNA polyadenylation |
| Day 2–5 | Virus-specific CD8+ T cells (M1 peptide dominant); CD4+ Tfh | — |
| Day 5–7 | Neutralizing IgM (anti-HA); IgA (mucosal) | Antigenic drift in subsequent infections |

### NS1 multi-function IFN antagonism

NS1 is the dominant virulence factor for IFN evasion:
- **dsRNA sequestration**: NS1 RNA-binding domain sequesters dsRNA replication intermediates → RIG-I and PKR not activated
- **TRIM25 inhibition**: NS1 binds TRIM25 → prevents K63-ubiquitination of RIG-I CARDs → MAVS not activated
- **IRF3 blockade**: NS1 inhibits TBK1/IKKε → impairs IRF3 phosphorylation
- **Host mRNA processing block**: NS1 C-terminal ESAV/EPEV motif binds CPSF30 → blocks polyadenylation of host mRNAs (including IFN-β) → selectively reduces host mRNA stability
- **STAT2 evasion** (some strains): NS1 reported to block STAT1/STAT2 signaling

Highly pathogenic H5N1 NS1 has stronger multi-functional IFN antagonism than seasonal H1N1/H3N2, contributing to the paradoxically high cytokine response.

## Pathology

### Primary viral pneumonia

Influenza A infects alveolar epithelial cells (type I and II pneumocytes) → massive cell death → impaired surfactant production → reduced lung compliance → ARDS. Highly pathogenic H5N1 causes diffuse alveolar damage (DAD) with hyaline membrane formation, similar to ARDS from other causes.

### Cytokine storm

H5N1 and the 1918 pandemic strain drive disproportionate innate immune activation in the lower respiratory tract:
- NLRP3 inflammasome activation (M2 ion channel, PB1-F2 mitochondrial damage) → IL-1β + IL-18
- Macrophage activation → TNF-α, IL-6, CXCL10, IL-8 → neutrophil infiltration
- Paradoxically high IFN-β → may amplify rather than resolve inflammation in severe disease
- STAT1-mediated transcription overwhelmed → tissue destruction rather than pathogen clearance

### Secondary bacterial pneumonia

Influenza damages mucociliary clearance and exposes basal lamina glycoproteins → bacterial colonization by *S. aureus* (including MRSA), *S. pneumoniae*, *H. influenzae* → secondary pneumonia peaks at Day 5–10; responsible for majority of 1918 influenza deaths

### Diagnosis

- **Rapid antigen detection tests (RADTs)**: Sensitivity 50-70% for influenza A; faster and cheaper but miss many cases
- **RT-PCR (multiplex respiratory panel)**: Gold standard; highly sensitive; distinguishes A/B and subtypes (H1, H3, H5)
- **DFA/IFA**: Direct fluorescent antibody; moderate sensitivity
- Point-of-care molecular tests (ID NOW, Cepheid): Near RT-PCR sensitivity with 15-min turnaround

### Treatment

**Antivirals:**
- **Oseltamivir (Tamiflu)**: Oral NA inhibitor; reduces symptom duration by ~1 day and hospitalizations; most effective ≤48 h from symptom onset; prophylactic use post-exposure; oseltamivir resistance (H275Y in NA) in some H1N1 strains
- **Zanamivir (Relenza)**: Inhaled NA inhibitor; alternative to oseltamivir; contraindicated in asthma/COPD
- **Peramivir (Rapivab)**: IV NA inhibitor for hospitalized patients
- **Baloxavir marboxil (Xofluza)**: PA cap-dependent endonuclease inhibitor; single oral dose; active against oseltamivir-resistant strains; I38T resistance emerging with H3N2
- Amantadine/rimantadine: M2 channel blockers; virtually all circulating influenza A strains are resistant (S31N in M2)

**Severe disease:** ICU support, mechanical ventilation for ARDS; IV NAI (peramivir or inhaled zanamivir via ventilator); no proven benefit of corticosteroids

### Vaccines

- **IIV4 (inactivated influenza vaccine, quadrivalent)**: Standard-dose IM; annual; includes two influenza A strains (H1N1, H3N2) + two B strains (Yamagata, Victoria lineages); efficacy 40-60% depending on antigenic match
- **LAIV (live attenuated, FluMist)**: Intranasal; cold-adapted (25°C restricted replication); superior mucosal IgA induction; approved for ages 2-49
- **Adjuvanted (Fluad MF59)**: For adults ≥65; MF59 oil-in-water emulsion activates NLRP3 → depot effect + improved immunogenicity in elderly
- **High-dose (Fluzone HD)**: 4× antigen dose for adults ≥65; superior seroconversion
- **Recombinant HA (Flublok)**: Cell-culture independent; broader HA representation; approved for immunogenicity in elderly
- **mRNA influenza vaccines (investigational)**: Moderna/Pfizer in Phase II; potential for rapid pandemic strain updates and universal HA stalk targeting

## Connections

**→ [MAVS](../../../03-molecular/mavs/)**: Influenza 5′ppp negative-sense genomic ssRNA activates RIG-I → TRIM25 K63-ubiquitination → MAVS filament formation → TBK1 → IRF3 → IFN-β; NS1 suppresses MAVS by blocking TRIM25 and sequestering dsRNA replication intermediates; RIG-I/MAVS is the primary innate sensor for influenza in respiratory epithelium.

**→ [Type I Interferon](../../../03-molecular/type-i-interferon/)**: Influenza RIG-I/MAVS → IRF3/IRF7 → IFN-β in epithelial cells; pDC TLR7 → IFN-α (systemic); NS1 suppresses IFN by blocking IRF3 and dsRNA sensing; highly pathogenic H5N1 induces paradoxically high IFN-β contributing to cytokine storm; pandemic strains differ from seasonal in NS1 IFN antagonism potency.

**→ [STAT1](../../../03-molecular/stat1/)**: Influenza NS1 blocks ISGF3 formation (STAT1/STAT2/IRF9) by dsRNA sequestration and TRIM25 inhibition; PA-X endonuclease degrades host mRNAs including STAT1; H5N1 overcomes STAT1/SOCS1 negative feedback → hyperinflammation; NS1 IFN antagonism distinguishes highly pathogenic from seasonal strains.

**→ [NLRP3 Inflammasome](../../../03-molecular/nlrp3-inflammasome/)**: Influenza M2 proton channel and PB1-F2 (mitochondrial targeting) activate NLRP3 → caspase-1 → IL-1β + IL-18; NLRP3-mediated IL-1β amplifies cytokine storm in severe H5N1 and 1918 H1N1 pneumonia; NLRP3 genetic variants associated with influenza severity; ASC speck formation observed in infected macrophages.

**→ [RIG-I](../../../03-molecular/rig-i/)**: Influenza A 5′ppp genomic ssRNA and dsRNA replication intermediates are the canonical RIG-I ligands; NS1 blocks RIG-I by sequestering dsRNA and inhibiting TRIM25-mediated K63-ubiquitination of RIG-I CARDs; NS1 IFN antagonism strength correlates with pandemic potential.

**→ [Influenza Hemagglutinin](../../../03-molecular/influenza-ha/)**: HA1 head antigenic sites A-E undergo annual drift requiring vaccine reformulation; HA2 stalk BNAbs (CR6261, MEDI8852, FI6v3) are the basis of universal influenza vaccine strategies; α2,6-SA vs α2,3-SA receptor binding specificity determines human transmissibility and pandemic potential.

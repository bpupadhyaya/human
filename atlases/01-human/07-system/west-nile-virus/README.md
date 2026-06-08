---
schema: human-scale-entry/v1
id: west-nile-virus
name: West Nile Virus
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Flavivirus (Culex mosquito vector); 1937 Uganda origin, 1999 North American invasion; 80% asymptomatic infection; neuroinvasive disease (meningitis, encephalitis, paralysis) in elderly/immunocompromised; NS3/NS5 proteins block IFN signaling; no approved antiviral/vaccine."
aliases: ["WNV", "West Nile virus", "West Nile fever", "West Nile encephalitis", "West Nile neuroinvasive disease", "WNND", "West Nile meningitis", "West Nile paralysis", "Culex WNV", "flavivirus encephalitis"]
sources:
  - id: petersen-2013-wnv-review
    type: peer-reviewed
    cite: "Petersen LR, Brault AC, Nasci RS. West Nile virus: review of the literature. JAMA. 2013;310(3):308-315."
    doi: "10.1001/jama.2013.8042"
    pmid: "23860989"
    url: "https://doi.org/10.1001/jama.2013.8042"
    accessed: "2026-06-08"
  - id: colpitts-2012-wnv-biology
    type: peer-reviewed
    cite: "Colpitts TM, Conway MJ, Montgomery RR, Fikrig E. West Nile Virus: Biology, Transmission, and Human Infection. Clin Microbiol Rev. 2012;25(4):635-648."
    doi: "10.1128/CMR.00045-12"
    pmid: "23034323"
    url: "https://doi.org/10.1128/CMR.00045-12"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/mavs
    relation: connects-to
    note: "WNV NS3-NS4A complex inhibits RIG-I signaling and disrupts MAVS; NS5-mediated RNA capping (7-methylguanosine) prevents 5′ppp recognition by RIG-I → MAVS not engaged; combined NS3/NS5 strategy suppresses MAVS-TBK1-IRF3 axis enabling WNV establishment."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "WNV NS5 blocks STAT1 by: (1) preventing Tyr701 phosphorylation → ISGF3 cannot form; (2) K48-ubiquitination of STAT1 → proteasomal degradation; NS5-mediated STAT1 antagonism enables WNV to evade ISG-based antiviral defense after IFN-β induction."
  - target: 01-human/03-molecular/rig-i
    relation: connects-to
    note: "WNV NS5 methyltransferase caps viral RNA with 7-methylguanosine → RIG-I CTD cannot recognize 5′ppp → MAVS not activated; NS3-NS4A helicase also directly inhibits RIG-I signaling; RNA capping mimics host mRNA modification to evade cytosolic innate immunity."
  - target: 01-human/07-system/dengue-fever
    relation: connects-to
    note: "WNV and DENV share Aedes aegypti + Culex vectors, flavivirus structure, and flaviviral biology; anti-DENV antibodies cross-react with WNV but provide variable protection; WNV neuroinvasive disease has no DENV equivalent; both evade STAT1 via NS5."
  - target: 01-human/07-system/zika-virus
    relation: connects-to
    note: "WNV and ZIKV are neurotropic flaviviruses with serological cross-reactivity; prior WNV immunity may partially protect against ZIKV and vice versa; unlike ZIKV, WNV lacks sexual transmission and does not cause congenital brain malformations; both NS5 proteins evade STAT1."
---

# West Nile Virus

## Overview

**West Nile virus (WNV)** is a positive-sense single-stranded RNA virus of the family *Flaviviridae* (genus *Flavivirus*), transmitted in an enzootic bird–mosquito cycle and incidentally infecting humans via the bite of infected *Culex* mosquitoes, primarily *Culex pipiens* and *Culex quinquefasciatus*. First isolated from a febrile patient in the West Nile Province of Uganda in 1947, WNV circulated primarily in Africa, the Middle East, and South Asia for decades before causing explosive outbreaks in Romania (1996) and then **invading North America in 1999** — appearing suddenly in New York City and spreading to all contiguous US states within 4 years, becoming the leading cause of domestically acquired viral encephalitis in North America [^petersen-2013-wnv-review].

WNV infection follows a stark **80/20 rule**: ~80% of infections are completely asymptomatic, ~20% cause **West Nile fever** (a self-limited febrile illness), and ~1 in 150 symptomatic infections progresses to **West Nile neuroinvasive disease (WNND)** — encompassing meningitis, encephalitis, and an acute flaccid paralysis (AFP) syndrome resembling poliomyelitis. The elderly and immunocompromised are disproportionately affected by WNND, with case-fatality rates of 3–15% in hospitalized patients [^colpitts-2012-wnv-biology].

**Clinical significance:** WNV has caused over 25,000 neuroinvasive disease cases and ~2,500 deaths in the United States since 1999. There is no approved antiviral therapy or human vaccine. WNV serves as a model for understanding neurotropic flavivirus pathogenesis, BBB breach mechanisms, and innate immune evasion via RNA capping.

## Structure

### WNV biology

WNV is an enveloped icosahedral virus (~50 nm) with an **~11 kb positive-sense ssRNA genome** encoding a single polyprotein processed into three structural and seven non-structural proteins:

| Protein | Function |
|---------|----------|
| C (capsid) | Nucleocapsid assembly; interacts with genomic RNA |
| prM/M | Precursor membrane protein; furin-cleaved during maturation; protects E during assembly |
| E (envelope) | Receptor binding (TIM-1/HAVCR1, integrins, heparan sulfate); membrane fusion at endosomal pH 5–6; target of neutralizing antibodies |
| NS1 | Secreted hexamer; evades complement via C4b-binding protein; used as serologic diagnostic marker; endothelial activation |
| NS2A/2B | NS2A: replication complex; NS2B: NS3 serine protease cofactor |
| NS3 | Serine protease (with NS2B) + RNA helicase; cleaves viral polyprotein; inhibits RIG-I/MAVS signaling |
| NS4A/4B | Membrane rearrangement; replication organelles; NS4A blocks JAK-STAT signaling |
| NS5 | RNA-dependent RNA polymerase + **methyltransferase** (caps viral RNA → evades RIG-I); **blocks STAT1** → IFN evasion |

### WNV lineages

WNV is classified into at least 8 lineages:
- **Lineage 1 clade 1a**: Responsible for most human disease globally including North America (NY99 strain) and European outbreaks; highest neurovirulence
- **Lineage 2**: Historically sub-Saharan Africa; caused 2010–2012 European outbreaks (Hungary, Greece)
- **Lineage 1 clade 1b (Kunjin)**: Australia; lower neurovirulence than lineage 1a

The **NY99 strain** that entered North America in 1999 is closely related to a 1998 Israeli isolate, suggesting a Middle Eastern origin.

## Function

### Viral life cycle

1. **Mosquito-to-host transmission**: *Culex* mosquito takes a blood meal from infected amplifying host (corvids — crows, blue jays — are highly susceptible) → injects WNV in saliva → skin DCs and Langerhans cells infected at inoculation site
2. **Initial replication**: Local replication in skin, draining lymph nodes → primary viremia (Days 1–4)
3. **Systemic dissemination**: Viremia seeds spleen, liver, kidney; amplified in monocytes/macrophages; peak viremia Day 3–7
4. **Neuroinvasion** (minority of cases): WNV crosses BBB via: (a) direct transcytosis through endothelial cells; (b) Trojan horse — infected monocytes traverse BBB; (c) axonal retrograde transport from peripheral nerve terminals; (d) MMP-mediated BBB disruption
5. **CNS infection**: Replication in neurons (especially anterior horn motor neurons, Purkinje cells, hippocampal neurons), astrocytes, and microglia

### Immune evasion

WNV has evolved a multilayered strategy to evade innate immunity:

| Mechanism | Molecular detail |
|-----------|-----------------|
| RNA capping | NS5 methyltransferase adds 7-methylguanosine 5′-cap → viral RNA resembles host mRNA → RIG-I CTD cannot detect 5′ppp → MAVS not activated |
| RIG-I/MDA5 inhibition | NS3-NS4A complex directly disrupts RIG-I signaling |
| STAT1 blockade | NS5 prevents STAT1 Tyr701 phosphorylation and targets STAT1 for K48-ubiquitination → proteasomal degradation → ISGF3 cannot form → ISGs not induced |
| Complement evasion | NS1 binds C4b-binding protein → prevents C3 amplification; inhibits classical complement cascade |
| IFN-β blockade | NS4A/NS4B block TBK1 → IRF3 not fully activated; additive with NS3-NS4A upstream block |

### Innate and adaptive immune response

| Phase | Response |
|-------|---------|
| Hours 0–12 | Skin DC sensing; low-level IFN-β despite NS5 evasion |
| Days 1–3 | NK cell activation; complement-mediated lysis of WNV-infected cells |
| Days 3–7 | WNV-specific CD8+ T cells (E protein peptides dominant); CD4+ Tfh |
| Days 7–14 | Neutralizing IgM (anti-E protein); most infections cleared |
| >14 days | IgG seroconversion; long-lived B cell memory; durable protection from reinfection |

## Pathology

### West Nile fever

**Epidemiology:** ~20% of WNV-infected individuals; incubation 3–14 days.

**Clinical:** Abrupt fever (38–40°C), headache, myalgias, arthralgias, fatigue; **maculopapular rash** (truncal, non-pruritic) in ~50%; lymphadenopathy; gastrointestinal symptoms (nausea, diarrhea) in ~30%. Duration 3–7 days; full recovery typically within weeks but fatigue and cognitive symptoms can persist months.

**Laboratory:** Lymphocytopenia, mild thrombocytopenia, elevated transaminases; WNV IgM in serum/CSF from Day 4–8.

### West Nile neuroinvasive disease (WNND)

**Risk factors:** Age ≥60 years (30-fold higher WNND risk vs. age <20), immunosuppression (transplant, HIV, chemotherapy), diabetes, hypertension, CCR5Δ32 homozygosity (impaired CNS immune control).

**Three WNND syndromes:**

1. **West Nile meningitis** (~45% of WNND): Fever, severe headache, stiff neck, photophobia; CSF shows lymphocytic pleocytosis (10–100 cells/mm³), elevated protein, normal glucose; generally good prognosis

2. **West Nile encephalitis** (~40% of WNND): Altered consciousness, confusion, disorientation, seizures, extrapyramidal signs (tremor, bradykinesia — basal ganglia involvement), Parkinsonism; MRI shows T2/FLAIR signal in basal ganglia, thalamus, brainstem, periventricular white matter; mortality 3–15% in hospitalized patients; cognitive and neurological deficits common in survivors

3. **West Nile acute flaccid paralysis/poliomyelitis** (~10% of WNND): Asymmetric proximal limb weakness (anterior horn cell injury); respiratory failure if diaphragm involved; CSF pleocytosis; EMG shows anterior horn cell pattern; NCS normal → distinguishes from GBS; 50% have permanent residual weakness

### Diagnosis

- **Serology (IgM ELISA)**: Preferred; IgM appears in serum and CSF Days 4–8; highly specific; *note:* cross-reactivity with DENV, ZIKV, SLEV (St. Louis encephalitis) may require PRNT confirmation
- **RT-PCR**: Detects viremia (Days 1–6); low sensitivity after Day 7 (immune clearance); most useful for immunocompromised patients with prolonged viremia
- **Blood supply screening**: US blood supply screened by NAT (nucleic acid testing) — reduces transfusion-associated risk to <1 per million units

### Treatment and prevention

**No approved antiviral therapy.** Management is supportive:
- Uncomplicated fever: Antipyretics, rest, hydration
- Encephalitis/meningitis: Hospitalization; ICP management if severe; seizure control
- AFP: ICU admission, mechanical ventilation for respiratory compromise; physical therapy
- Experimental: IV immunoglobulin (convalescent plasma with high anti-WNV titers) — anecdotal benefit in severe cases; no RCT evidence for IFN-α, ribavirin, or steroids

**Vaccines:**
- **Human vaccines:** No approved vaccine as of 2026; multiple candidates failed in efficacy trials or development was deprioritized due to commercial considerations; candidates include ChimeriVax-WN (Sanofi), DNA vaccine (NIAID Phase II), and recombinant subunit approaches
- **Equine vaccine:** Licensed (West Nile-Innovator, Vetera WNV); ~90% efficacy; 3-dose series; widely used in the US equine industry

**Vector control and prevention:**
- Public health: Insecticide applications (pyrethroid aerial/ground spraying), larval source reduction (standing water elimination), Culex breeding habitat management
- Personal: DEET-containing repellent (≥20%), permethrin-treated clothing, mosquito netting, indoor air conditioning (reduces mosquito exposure)
- Blood donation: NAT screening; donors deferred if recent WNV exposure suspected

## Connections

**→ [MAVS](../../../03-molecular/mavs/)**: WNV NS3-NS4A complex inhibits RIG-I signaling and disrupts MAVS; NS5-mediated RNA capping (7-methylguanosine) prevents 5′ppp recognition by RIG-I → MAVS not engaged; combined NS3/NS5 strategy suppresses MAVS-TBK1-IRF3 axis enabling WNV establishment.

**→ [STAT1](../../../03-molecular/stat1/)**: WNV NS5 blocks STAT1 by: (1) preventing Tyr701 phosphorylation → ISGF3 cannot form; (2) K48-ubiquitination of STAT1 → proteasomal degradation; NS5-mediated STAT1 antagonism enables WNV to evade ISG-based antiviral defense after IFN-β induction.

**→ [RIG-I](../../../03-molecular/rig-i/)**: WNV NS5 methyltransferase caps viral RNA with 7-methylguanosine → RIG-I CTD cannot recognize 5′ppp → MAVS not activated; NS3-NS4A helicase also directly inhibits RIG-I signaling; RNA capping mimics host mRNA modification to evade cytosolic innate immunity.

**→ [Dengue Fever](../dengue-fever/)**: WNV and DENV share Aedes aegypti + Culex vectors, flavivirus structure, and flaviviral biology; anti-DENV antibodies cross-react with WNV but provide variable protection; WNV neuroinvasive disease has no DENV equivalent; both evade STAT1 via NS5.

**→ [Zika Virus](../zika-virus/)**: WNV and ZIKV are neurotropic flaviviruses with serological cross-reactivity; prior WNV immunity may partially protect against ZIKV and vice versa; unlike ZIKV, WNV lacks sexual transmission and does not cause congenital brain malformations; both NS5 proteins evade STAT1.

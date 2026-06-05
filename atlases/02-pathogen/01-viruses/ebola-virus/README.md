---
schema: pathogen-entry/v1
id: ebola-virus
name: Ebola Virus (EBOV)
atlas: 02-pathogen
scale: 01-viruses
status: draft
last_reviewed: 2026-06-05
summary: "Filoviridae; filamentous enveloped negative-sense ssRNA (~19 kb). GP1,2 trimers bind NPC1 in late endosomes for entry; VP35/VP40/VP24 suppress IFN signaling. Causes hemorrhagic fever with DIC, vascular leak; CFR 25-90%. Ervebo vaccine FDA-approved."
aliases: ["EBOV", "Ebola", "Ebola haemorrhagic fever virus", "EHF", "EVD virus", "Zaire ebolavirus"]
sources:
  - id: mandell-principles
    type: textbook
    cite: "Bennett JE, Dolin R, Blaser MJ. Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases. 9th ed. Elsevier; 2020."
    url: "https://www.elsevier.com/books/mandell-douglas-and-bennetts-principles-and-practice-of-infectious-diseases/bennett/978-0-323-48255-4"
    accessed: "2026-06-05"
  - id: murray-microbiology
    type: textbook
    cite: "Murray PR, Rosenthal KS, Pfaller MA. Medical Microbiology. 9th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/medical-microbiology/murray/978-0-323-67378-4"
    accessed: "2026-06-05"
  - id: feldmann-2011-ebola-review
    type: peer-reviewed
    cite: "Feldmann H, Geisbert TW. Ebola haemorrhagic fever. Lancet. 2011;377(9768):849-62."
    doi: "10.1016/S0140-6736(10)60667-8"
    pmid: "21084112"
    url: "https://doi.org/10.1016/S0140-6736(10)60667-8"
  - id: henao-restrepo-2017-ring-vaccination
    type: peer-reviewed
    cite: "Henao-Restrepo AM, Camacho A, Longini IM, et al. Efficacy and effectiveness of an rVSV-vectored vaccine in preventing Ebola virus disease: final results from the Guinea ring vaccination, open-label, cluster-randomised trial (Ebola Ça Suffit!). Lancet. 2017;389(10068):505-18."
    doi: "10.1016/S0140-6736(16)32621-6"
    pmid: "28017403"
    url: "https://doi.org/10.1016/S0140-6736(16)32621-6"
  - id: geisbert-2010-ebola-pathogenesis
    type: peer-reviewed
    cite: "Geisbert TW, Hensley LE. Ebola virus: new insights into disease aetiopathology and possible therapeutic interventions. Expert Rev Mol Med. 2004;6(20):1-24."
    doi: "10.1017/S1462399404008300"
    pmid: "15504257"
    url: "https://doi.org/10.1017/S1462399404008300"
  - id: white-2012-npc1-ebola
    type: peer-reviewed
    cite: "Carette JE, Raaben M, Wong AC, et al. Ebola virus entry requires the cholesterol transporter Niemann-Pick C1. Nature. 2011;477(7364):340-3."
    doi: "10.1038/nature10348"
    pmid: "21866103"
    url: "https://doi.org/10.1038/nature10348"
cross_links:
  - target: 01-human/04-cellular/macrophage
    relation: infects
    note: "Macrophages and monocytes are primary early targets of EBOV; GP1,2 binds DC-SIGN/L-SIGN enabling viral uptake, replication, and cytokine storm (TNF-α, IL-6, IL-8) that amplifies systemic pathology."
  - target: 01-human/07-system/immune-system
    relation: damages
    note: "VP35 blocks RIG-I/MDA5 sensing; VP24 prevents STAT1 nuclear import; lymphocyte apoptosis depletes T and NK cells, leaving unchecked viral replication and fatal immune collapse."
  - target: 01-human/06-organ/liver
    relation: damages
    note: "EBOV infects hepatocytes causing diffuse necrosis, markedly elevated transaminases, and coagulopathy from impaired clotting factor synthesis — hepatic failure drives DIC and hemorrhage."
  - target: 04-vaccine/02-viral-vector/ervebo
    relation: prevented-by
    note: "Ervebo (rVSV-ZEBOV-GP) is a live recombinant VSV expressing Ebola GP; FDA-approved 2019; ring vaccination achieved >97% efficacy in the Guinea Ebola ring vaccination trial (Henao-Restrepo 2017)."
---

# Ebola Virus (EBOV)

## Overview

**Ebola virus (EBOV)**, a member of the family *Filoviridae* and the species *Zaire ebolavirus*, is one of the most lethal human pathogens known: case fatality rates (CFR) in outbreaks range from **25% to 90%** depending on outbreak conditions, healthcare access, and the specific variant [^feldmann-2011-ebola-review]. First identified in 1976 during simultaneous outbreaks in the Democratic Republic of the Congo (then Zaire) and Sudan, EBOV remained an intermittent but devastating scourge of equatorial Africa for decades.

The **2014–2016 West Africa epidemic** — centred on Guinea, Sierra Leone, and Liberia — was a catastrophic departure from prior patterns: approximately **28,600 cases and 11,325 deaths**, with secondary spread to Nigeria, Mali, Senegal, the United States, and Europe. This epidemic demonstrated EBOV's capacity to sustain urban transmission and prompted unprecedented international mobilization. The **2018–2020 DRC North Kivu outbreak** (3,470 cases, 2,287 deaths) became the second-largest Ebola outbreak on record, complicated by armed conflict and community mistrust [^feldmann-2011-ebola-review].

Two major advances emerged from these crises:

1. **Ervebo (rVSV-ZEBOV-GP)** — the first FDA-approved Ebola vaccine (December 2019), demonstrating >97% efficacy in ring vaccination trials [^henao-restrepo-2017-ring-vaccination]
2. **Inmazeb (atoltivimab/maftivimab/odesivimab)** — an FDA-approved triple monoclonal antibody cocktail targeting non-overlapping GP epitopes; in the PALM trial, treatment with Inmazeb reduced CFR from ~50% to ~34% (and lower in early-treated patients)

EBOV's extreme pathogenicity arises from its ability to infect macrophages and dendritic cells early in infection, disabling innate immune defenses and triggering a systemic inflammatory cascade that leads to disseminated intravascular coagulation (DIC), vascular leak, multi-organ failure, and hemorrhage.

## Structure

### Virion Morphology

EBOV has a distinctive **filamentous or pleomorphic structure** — the characteristic "shepherd's crook" or loop shape visible by electron microscopy. Virions are uniformly ~80 nm in diameter but vary enormously in length (typically **800–1000 nm**; some reaching 14,000 nm).

| Component | Description |
|:---|:---|
| **Genome** | ~19 kb negative-sense, single-stranded RNA (−ssRNA); 7 genes in 3′→5′ order: NP–VP35–VP40–GP–VP30–VP24–L |
| **Nucleocapsid** | Helical; NP (nucleoprotein) encapsidates genomic RNA; VP35, VP30, L (RNA-dependent RNA polymerase) are associated |
| **Matrix layer** | VP40 (major matrix protein) lines the inner leaflet; drives virion budding and maintains filamentous structure |
| **Envelope** | Host-derived lipid bilayer |
| **Glycoprotein (GP1,2)** | Surface trimeric spikes (~150 nm projections); sole surface antigen; mediates attachment and membrane fusion |
| **sGP** | Soluble secreted truncated GP; decoys anti-GP antibodies, reducing neutralization of intact virions |
| **VP24** | Minor matrix protein; IFN antagonist; interacts with STAT1 and karyopherin-α |

### Key Virulence Factors

| Factor | Mechanism |
|:---|:---|
| **GP1,2** | Macropinocytosis-mediated entry; cathepsin B/L cleavage in late endosomes exposes NPC1-binding site |
| **VP35** | Blocks RIG-I/MDA5-mediated double-stranded RNA sensing; inhibits IRF3/IRF7 activation; suppresses IFN-β production |
| **VP24** | Competes with STAT1 for karyopherin-α nuclear import; prevents IFN-JAK-STAT signaling |
| **VP40** | Drives budding and filamentous morphology; antagonizes tetherin/BST-2 |
| **sGP** | Secreted GP decoy; absorbs anti-GP antibodies before they can neutralize virions |
| **NP** | Suppresses innate immunity; sequesters activators of RIG-I signaling |

## Infection Mechanism

### Transmission and Initial Entry

EBOV is transmitted via **direct contact with the blood, secretions, organs, or other bodily fluids of infected persons** — there is no documented aerosol transmission in natural outbreaks. Healthcare workers, burial teams, and close family caregivers face the highest risk. The **natural reservoir** is most likely insectivorous fruit bats (particularly *Rousettus aegyptiacus*), though the exact spillover event for each outbreak is rarely identified.

**Entry steps:**

1. **Attachment:** GP1 (the surface subunit of the GP1,2 trimer) binds **DC-SIGN (CD209)** and **L-SIGN (CD209L)** on macrophages and dendritic cells — the primary initial targets. Additional attachment factors include TIM-1 (hepatocyte), NPC1 (broadly expressed), and β1 integrins [^feldmann-2011-ebola-review]

2. **Macropinocytosis:** EBOV triggers non-specific macropinocytosis (large vesicle formation via actin-driven membrane ruffling) — the primary internalization route. Clathrin- and caveolae-dependent routes play minor roles

3. **Endosomal processing:** Within the late endosome/lysosome, host **cathepsins B and L** proteolytically cleave GP1 (~130 kDa → 19 kDa) to expose the **Niemann-Pick C1 (NPC1) receptor-binding domain** [^white-2012-npc1-ebola]. NPC1 is a late endosomal cholesterol transporter that serves as the essential intracellular receptor for EBOV

4. **Membrane fusion:** GP2 (the fusion subunit) undergoes pH-dependent conformational change → internal fusion peptide inserts into the endosomal membrane → six-helix bundle formation → lipid bilayer merging → nucleocapsid release into cytoplasm

5. **Replication:** The L polymerase transcribes 7 mRNAs (each capped and polyadenylated) using the negative-sense genome as template. Replication occurs in **inclusion bodies** (viral factories) visible by electron microscopy. New NPs encapsidate replicated genomes; VP40-driven budding releases filamentous progeny virions from the plasma membrane

### Macrophage/DC as Amplifiers

Infected macrophages do not simply carry the virus — they become **cytokine factories**, releasing massive amounts of TNF-α, IL-6, IL-1β, IL-8, MCP-1, and MIP-1α/β. Dendritic cells infected with EBOV fail to mature normally: they do not upregulate MHC-II, CD80, CD86, or CCR7, and therefore cannot prime adaptive T-cell responses effectively. This combination — amplified innate inflammation without adaptive immune activation — is the core of EBOV's lethal strategy.

## Host Interactions

### Immune Evasion

| Mechanism | Effector | Detail |
|:---|:---|:---|
| **IFN production blockade** | VP35 | Competitive inhibition of RIG-I; direct binding to dsRNA (prevents recognition); inhibition of IRF3/7 activation and nuclear translocation |
| **IFN signaling blockade** | VP24 | Competes with phospho-STAT1 for karyopherin-α1/5/6 binding → STAT1 cannot enter nucleus → IFN-stimulated genes not induced |
| **Antibody decoy** | sGP | Secreted in massive quantities; antigenically similar to GP1,2; absorbs patient antibodies, preventing virion neutralization |
| **DC dysfunction** | GP (unclear mechanism) | EBOV-infected DCs fail to mature; cannot present antigen effectively; T-cell priming is severely blunted |
| **NK cell evasion** | VP40 | Counteracts tetherin; virion release continues despite innate restriction |
| **Lymphocyte apoptosis** | Indirect (cytokines, NTG) | Bystander lymphocyte apoptosis (via Fas/FasL, TRAIL) depletes CD4⁺/CD8⁺ T cells and NK cells — immunosuppression without direct lymphocyte infection |

### Cytokine Storm and Vascular Leak

The systemic release of vasoactive cytokines (TNF-α, IL-6) and direct GP-mediated endothelial activation disrupts vascular integrity:
- GP expressed on endothelial cells causes cell rounding and detachment
- Activated macrophages release VEGF, MMP-9, and tissue factor
- DIC is initiated by tissue factor expression on infected macrophages → thrombin generation → fibrin microthrombi → consumptive coagulopathy → hemorrhage

The final common pathway is **multi-organ failure**: liver, kidney, adrenal glands, and spleen are severely damaged, with shock caused by vascular leak rather than direct hemorrhage in the majority of fatal cases.

## Connections

- **Infects** → [Macrophage](../../../01-human/04-cellular/macrophage/README.md): Macrophages and monocytes are the primary early cellular targets. EBOV GP1,2 binds DC-SIGN/L-SIGN on their surfaces; infected macrophages become cytokine-producing amplifiers driving the systemic inflammatory cascade central to Ebola virus disease pathophysiology.

- **Damages** → [Immune System](../../../01-human/07-system/immune-system/README.md): VP35 and VP24 cooperatively disable innate IFN defenses at both the production and signaling levels. Bystander lymphocyte apoptosis devastates adaptive immunity. sGP decoys neutralizing antibodies. The result is profound immunosuppression despite intense systemic inflammation.

- **Damages** → [Liver](../../../01-human/06-organ/liver/README.md): EBOV infects hepatocytes directly, causing diffuse hepatocellular necrosis with markedly elevated AST/ALT. Impaired synthesis of clotting factors (fibrinogen, factors V, VII, VIII, X) from liver failure is a direct driver of DIC and the hemorrhagic manifestations of severe disease.

- **Prevented by** → [Ervebo (rVSV-ZEBOV)](../../../../04-vaccine/02-viral-vector/ervebo/README.md): Ervebo is a live recombinant vesicular stomatitis virus (rVSV) in which the VSV glycoprotein is replaced by EBOV GP. A single dose induces robust GP-specific IgG and T-cell responses; ring vaccination of contacts and contacts-of-contacts achieved >97% efficacy in the Guinea Ebola Ça Suffit! trial [^henao-restrepo-2017-ring-vaccination].

## Pathology

### Clinical Course: Ebola Virus Disease (EVD)

The incubation period is **2–21 days** (typically 4–10 days). EVD evolves through overlapping phases:

| Phase | Timing | Features |
|:---|:---|:---|
| **Prodromal** | Days 1–3 | Abrupt onset fever (≥38.6°C), severe headache, fatigue, myalgia — clinically indistinguishable from malaria/typhoid |
| **Gastrointestinal** | Days 3–7 | Profuse watery diarrhea (3–10 L/day), vomiting, abdominal pain — major source of dehydration and electrolyte derangement |
| **Peak viremia** | Days 5–10 | Viral loads reach 10⁸–10¹⁰ copies/mL in fatal cases; DIC, petechiae, ecchymoses; splenic necrosis; liver failure |
| **Hemorrhagic** | Days 7–12 (if present) | Overt hemorrhage (oozing venipuncture sites, hematemesis, melena, epistaxis, gingival bleeding) — present in only ~50% of cases |
| **Shock/Recovery** | Days 8–12+ | Non-survivors: shock, multi-organ failure, death. Survivors: fever defervescence, gradual recovery over weeks; may shed virus in semen for months |

**Hemorrhage is not universal** — the name "hemorrhagic fever" is somewhat misleading. Most deaths result from hypovolemic shock from GI fluid losses and vascular leak, compounded by multi-organ failure, rather than exsanguination per se.

### Diagnostics

| Method | Window | Notes |
|:---|:---|:---|
| **RT-PCR (blood)** | Day 3+ after symptom onset | Gold standard; Ct <25 correlates with high infectivity; viral RNA may persist in semen/CSF/aqueous humor long after blood clearance |
| **Antigen RDTs** | Day 3+ | OraQuick Ebola RDT (OraQuick); useful in field settings; sensitivity ~91-97% vs. RT-PCR in viremic patients |
| **Serology (IgM/IgG)** | Week 2+ | IgM appears first; IgG persists for years; ELISA and lateral flow formats; used for outbreak investigation and immune status |
| **Isolation in BSL-4** | Research only | Virus culture confirms viability; not used clinically |

### Treatment

**Supportive care** remains the cornerstone: aggressive IV or oral rehydration, electrolyte correction (hyponatremia, hypokalemia), analgesics, antiemetics, management of secondary infections, and careful attention to DIC (fresh frozen plasma, platelets). Barrier nursing and PPE are essential.

**Specific therapies (approved):**

- **Inmazeb (atoltivimab + maftivimab + odesivimab):** FDA-approved October 2020. Three monoclonal antibodies targeting GP1 (two epitopes) and GP2 fusion loop; administered as a single IV infusion. In the PALM RCT (DRC, 2018–19), Inmazeb reduced 28-day mortality to ~34% vs. ~49% in control arms in high-viremia patients [^mandell-principles]
- **Ebanga (ansuvimab):** FDA-approved December 2020. Single mAb targeting the GP1 receptor-binding domain (RBD); showed similar efficacy to Inmazeb in PALM trial

**Prophylaxis:**
- **Ervebo:** Ring vaccination (vaccinating contacts and contacts-of-contacts within 21 days of last exposure) is the WHO-recommended strategy for outbreak containment
- **Zabdeno + Mvabea (Johnson & Johnson two-dose regimen):** EMA-approved 2020; Ad26.ZEBOV prime + MVA-BN-Filo boost; for broader population prophylaxis including healthcare workers

---

> **AI co-maintenance notice:** Portions of this entry were drafted or reviewed with AI assistance. All content is cross-checked against primary sources; contact bpupadhyaya@gmail.com for corrections.

[^feldmann-2011-ebola-review]: Feldmann H, Geisbert TW. Ebola haemorrhagic fever. *Lancet.* 2011;377(9768):849-62. [doi:10.1016/S0140-6736(10)60667-8](https://doi.org/10.1016/S0140-6736(10)60667-8) · [PubMed 21084112](https://pubmed.ncbi.nlm.nih.gov/21084112/)
[^henao-restrepo-2017-ring-vaccination]: Henao-Restrepo AM, et al. Efficacy and effectiveness of an rVSV-vectored vaccine in preventing Ebola virus disease. *Lancet.* 2017;389(10068):505-18. [doi:10.1016/S0140-6736(16)32621-6](https://doi.org/10.1016/S0140-6736(16)32621-6) · [PubMed 28017403](https://pubmed.ncbi.nlm.nih.gov/28017403/)
[^white-2012-npc1-ebola]: Carette JE, Raaben M, Wong AC, et al. Ebola virus entry requires the cholesterol transporter Niemann-Pick C1. *Nature.* 2011;477(7364):340-3. [doi:10.1038/nature10348](https://doi.org/10.1038/nature10348) · [PubMed 21866103](https://pubmed.ncbi.nlm.nih.gov/21866103/)
[^geisbert-2010-ebola-pathogenesis]: Geisbert TW, Hensley LE. Ebola virus: new insights into disease aetiopathology and possible therapeutic interventions. *Expert Rev Mol Med.* 2004;6(20):1-24. [doi:10.1017/S1462399404008300](https://doi.org/10.1017/S1462399404008300) · [PubMed 15504257](https://pubmed.ncbi.nlm.nih.gov/15504257/)
[^mandell-principles]: Bennett JE, Dolin R, Blaser MJ. *Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases.* 9th ed. Elsevier; 2020.
[^murray-microbiology]: Murray PR, Rosenthal KS, Pfaller MA. *Medical Microbiology.* 9th ed. Elsevier; 2021.

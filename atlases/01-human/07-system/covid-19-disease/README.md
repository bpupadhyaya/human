---
schema: human-scale-entry/v1
id: covid-19-disease
name: COVID-19 Disease
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Multisystem infectious disease caused by SARS-CoV-2; clinical spectrum from asymptomatic to severe ARDS and cytokine storm. Spike protein binds ACE2 for cell entry; hyperinflammation drives severe disease; mRNA vaccines (mRNA-1273, BNT162b2) provide high efficacy."
aliases: ["COVID-19", "coronavirus disease 2019", "SARS-CoV-2 infection", "COVID"]
sources:
  - id: guan-2020-china-cohort
    type: peer-reviewed
    cite: "Guan WJ, Ni ZY, Hu Y, et al. Clinical Characteristics of Coronavirus Disease 2019 in China. N Engl J Med. 2020;382(18):1708-1720."
    doi: "10.1056/NEJMoa2002032"
    pmid: "32109013"
    url: "https://doi.org/10.1056/NEJMoa2002032"
  - id: hoffmann-2020-ace2-entry
    type: peer-reviewed
    cite: "Hoffmann M, Kleine-Weber H, Schroeder S, et al. SARS-CoV-2 Cell Entry Depends on ACE2 and TMPRSS2 and Is Blocked by a Clinically Proven Protease Inhibitor. Cell. 2020;181(2):271-280."
    doi: "10.1016/j.cell.2020.02.052"
    pmid: "32142651"
    url: "https://doi.org/10.1016/j.cell.2020.02.052"
  - id: polack-2020-bnt162b2
    type: peer-reviewed
    cite: "Polack FP, Thomas SJ, Kitchin N, et al. Safety and Efficacy of the BNT162b2 mRNA Covid-19 Vaccine. N Engl J Med. 2020;383(27):2603-2615."
    doi: "10.1056/NEJMoa2034577"
    pmid: "33301246"
    url: "https://doi.org/10.1056/NEJMoa2034577"
cross_links:
  - target: 01-human/03-molecular/ace2
    relation: modulates
    note: "SARS-CoV-2 spike protein binds ACE2 for cell entry; viral binding downregulates surface ACE2, shifting angiotensin II/Ang-(1-7) balance toward pro-inflammatory Ang II signaling — amplifying vascular injury and cytokine release in severe COVID-19."
  - target: 01-human/07-system/cytokine-storm
    relation: connects-to
    note: "Severe COVID-19 is pathologically defined by a hyperinflammatory cytokine release syndrome (elevated IL-6, IL-1β, TNF-α, ferritin); cytokine storm drives the vascular leak, ARDS, multiorgan failure, and high mortality of critical COVID-19."
  - target: 01-human/06-organ/lung
    relation: targets
    note: "The lung is the primary target organ in COVID-19 pneumonitis: diffuse alveolar damage, type II pneumocyte injury, pulmonary vascular thrombosis, and hyaline membrane formation produce the bilateral infiltrates and hypoxemia characteristic of COVID-19 ARDS."
  - target: 01-human/07-system/respiratory-system
    relation: targets
    note: "SARS-CoV-2 infects upper and lower respiratory epithelium via ACE2; initial upper respiratory replication (nasal turbinates, oropharynx) is followed by lower respiratory spread in severe cases, causing COVID-19 pneumonia and respiratory failure."
  - target: 01-human/07-system/sars-cov-2
    relation: connects-to
    note: "SARS-CoV-2 betacoronavirus causes COVID-19; NSP5 Mpro (nirmatrelvir), NSP12 RdRp (remdesivir), and Spike (vaccine antigen) are the key drug/vaccine targets; NSP1/ORF6 IFN evasion enables early viral amplification; Omicron immune escape lineages drive ongoing pandemic waves."
  - target: 01-human/03-molecular/sars-cov-2-spike
    relation: connects-to
    note: "SARS-CoV-2 Spike is the COVID-19 vaccine antigen; RBD:ACE2 binding (Kd ~15 nM) initiates infection of airway epithelium and type II pneumocytes; Spike-mediated ACE2 internalization amplifies ARDS; 2P-stabilized prefusion Spike is the basis of all approved mRNA vaccines."
  - target: 01-human/07-system/rsv
    relation: connects-to
    note: "COVID-19 and RSV are enveloped respiratory RNA viruses driving the seasonal lower-respiratory burden alongside influenza; both cause bronchiolitis/pneumonia at the extremes of age, both are now vaccine-preventable in older adults, and multiplex panels distinguish them."
  - target: 01-human/07-system/influenza
    relation: connects-to
    note: "COVID-19 and influenza are the dominant pandemic-capable respiratory viruses—overlapping fever, cough and pneumonia but distinct treatments (nirmatrelvir/remdesivir vs oseltamivir/baloxavir); co-circulation strains health systems and both have annually updated vaccines."
  - target: 01-human/04-cellular/type-ii-pneumocyte
    relation: connects-to
    note: "SARS-CoV-2 targets ACE2-expressing alveolar type II pneumocytes: infection destroys these surfactant-producing progenitor cells → alveolar collapse, hyaline membranes and diffuse alveolar damage → ARDS; their loss impairs lung repair and underlies severe COVID-19 hypoxemia."
  - target: 03-medicine/01-modern/12-anti-inflammatory/dexamethasone
    relation: treated-by
    note: "RECOVERY trial (Horby 2021): 6 mg OD × 10 days reduced 28-day mortality by 17% (RR 0.83) in patients requiring oxygen; 29% reduction in mechanically ventilated patients; no benefit in those not requiring supplemental oxygen."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: treated-by
    note: "RECOVERY trial (2021): dexamethasone 6 mg/d × 10 days; 36% 28-day mortality reduction in mechanically ventilated patients (RR 0.64); 18% reduction in those requiring supplemental oxygen; class mechanism: GR:NF-κB transrepression of cytokine genes."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "COVID-19 is strongly prothrombotic: SARS-CoV-2 endothelial injury and intense inflammation drive immunothrombosis, raising deep vein thrombosis, pulmonary embolism, and microvascular clots—so inpatients get thromboprophylaxis and D-dimer marks severity."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "COVID-19 is in part an endothelial disease: SARS-CoV-2 and inflammation injure ACE2-bearing endothelial cells, causing endotheliitis, microthrombi, and the capillary leak that drives severe lung and multi-organ failure—the virus's vascular face."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages drive severe COVID-19's cytokine storm: dysregulated alveolar macrophages pour out IL-6 and TNF in a macrophage-activation-like syndrome, fueling the hyperinflammation that dexamethasone and IL-6 blockade (tocilizumab) target in critically ill patients."
  - target: 01-human/06-organ/ards
    relation: connects-to
    note: "ARDS is the lethal pulmonary endpoint of severe COVID-19: SARS-CoV-2 injury to alveolar epithelium and endothelium floods the lungs with protein-rich edema, collapsing gas exchange and requiring ventilation or ECMO—the final common pathway of fatal COVID pneumonia."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Type 2 diabetes markedly worsens COVID-19: hyperglycemia and the inflammatory, prothrombotic milieu of diabetes raise the risk of severe disease and death, while COVID can itself precipitate hyperglycemia and new diabetes—a bidirectional, dangerous interaction."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "COVID-19 raises stroke risk through its prothrombotic state: SARS-CoV-2-driven endothelial injury and hypercoagulability cause arterial thromboses, so ischemic stroke is a recognized complication alongside the venous thromboembolism the infection provokes."
  - target: 01-human/05-tissue/alveolus
    relation: targets
    note: "COVID-19 pneumonia injures the alveolus directly: SARS-CoV-2 infects ACE2-bearing type II pneumocytes lining the air sacs, triggering diffuse alveolar damage, hyaline membranes and flooding that impair gas exchange and underlie hypoxemic respiratory failure."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Type I interferon is the fault line of severe COVID-19: inborn errors or autoantibodies blunting interferon predispose to critical disease, while SARS-CoV-2 also actively suppresses it—explaining why a weak early interferon response lets the virus run unchecked."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils worsen severe COVID-19: they flood inflamed lungs and release neutrophil extracellular traps (NETs) that drive immunothrombosis, clogging pulmonary microvessels and linking the hyperinflammatory and clotting features of the disease."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "COVID-19 reaches beyond the lungs to the brain: loss of smell and taste, strokes, and the lingering brain fog of long COVID reflect both direct effects and inflammation, so neurological symptoms are now recognized as core features, not rare complications."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "COVID-19 injures the heart: the infection and its inflammation cause myocarditis, arrhythmias, and raised troponin, and survivors carry elevated cardiovascular risk for months—so cardiac monitoring matters even after the respiratory illness resolves."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "B cells are central to COVID immunity: they generate the neutralizing antibodies that vaccines and prior infection rely on, but spike mutations in new variants erode that antibody protection—driving the need for updated boosters and explaining reinfections."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Cytotoxic T cells clear SARS-CoV-2-infected cells: CD8 T-cell responses help end the infection and, as durable memory, underpin protection from severe disease after infection or vaccination even when antibodies wane."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 drives COVID-19's cytokine storm: severe disease floods the blood with IL-6, fueling the hyperinflammation that injures the lungs—so the IL-6-blocker tocilizumab improves survival in critically ill patients alongside steroids."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "COVID-19 frequently injures the kidney: acute kidney injury is common in severe disease from direct infection, cytokines and microthrombi, and needing dialysis sharply worsens outcomes—evidence the virus is multisystem, not just respiratory."
---

# COVID-19 Disease

## Overview

**COVID-19 (Coronavirus Disease 2019)** is an infectious, multisystem disease caused by **SARS-CoV-2** (Severe Acute Respiratory Syndrome Coronavirus 2), a betacoronavirus identified in Wuhan, China in December 2019. It caused the first pandemic of the 21st century, responsible for >7 million documented deaths globally as of 2024 (with substantial excess-mortality estimates suggesting 14–24 million total).

The clinical spectrum is remarkably broad — ranging from **completely asymptomatic** (~35–45% of infections) to **mild-moderate respiratory illness** to **severe pneumonia, ARDS, and multiorgan failure**. Risk stratification is critically determined by age (strong exponential increase in severity/mortality above 50 years), immunosuppression, diabetes, obesity, cardiovascular disease, and CKD. The case-fatality rate (CFR) of the original Wuhan strain was ~1–3%; Omicron subvariants have substantially lower CFR (~0.1–0.3%) due to immune escape mutations reducing lower respiratory tropism and widespread population immunity from vaccination and prior infection.

SARS-CoV-2 belongs to the same betacoronavirus clade as SARS-CoV-1 (2003 outbreak) and shares the ACE2 receptor; its spike protein RBD has ~10–20× higher ACE2 affinity than SARS-CoV-1, contributing to efficient upper respiratory transmission.

## Structure

### Viral cell entry and early replication

SARS-CoV-2 infects cells via the **spike (S) protein** trimer on the viral surface [^hoffmann-2020-ace2-entry]:
1. **Receptor binding:** The spike receptor-binding domain (RBD) binds **ACE2** (angiotensin-converting enzyme 2) on host cell surfaces; ACE2 is highly expressed on type II pneumocytes, nasal goblet/ciliated cells, enterocytes, cardiomyocytes, and renal proximal tubule cells — explaining the multiorgan tropism
2. **Spike priming:** Host serine protease **TMPRSS2** (or cathepsin L in endosomes) cleaves the spike at S1/S2 and S2' sites → conformational change → fusion peptide insertion into host membrane → membrane fusion and viral entry
3. **Replication:** Positive-sense ssRNA genome (29.9 kb) → translation of replicase (ORF1a/1b, pp1a/pp1ab, cleaved to nsp1-16) → RNA-dependent RNA polymerase (nsp12) → genome replication and subgenomic mRNA synthesis → structural proteins (S, E, M, N) → assembly and budding from ER-Golgi intermediate compartment (ERGIC)

### Innate immune evasion and early pathogenesis

A key feature distinguishing SARS-CoV-2 from influenza is its ability to **suppress early innate immune responses**:
- ORF6 and ORF9b block type I interferon (IFN-α/β) signaling by sequestering KPNA2 and blocking STAT1/2 import
- nsp3 (papain-like protease) deubiquitinates innate signaling intermediates; nsp16 methylates viral RNA cap to avoid MDA5 recognition
- Result: initial viral replication can proceed with minimal IFN response → high viral loads in the nasopharynx → efficient spread; then delayed, dysregulated immune activation produces hyperinflammation

## Function

### Clinical course and staging [^guan-2020-china-cohort]

**Stage I — Asymptomatic/presymptomatic (days 1–5):**
Active viral replication in upper respiratory tract (nasopharynx, oropharynx); peak infectivity occurs 1–2 days before and within ~5 days of symptom onset; most transmission occurs in this window.

**Stage II — Mild-moderate disease (days 1–10):**
Fever, cough, myalgia, fatigue, headache, anosmia/ageusia (loss of smell/taste — characteristic of original strain and Delta but less prominent in Omicron); most patients recover without hospitalization; oxygen saturation normal at rest.

**Stage III — Severe disease (days 7–14, ~15% of symptomatic):**
COVID-19 pneumonia: bilateral infiltrates, progressive hypoxemia (SpO₂ <94%), dyspnea; CT: "ground-glass opacities," consolidation, vascular congestion; driven by viral cytopathology in type II pneumocytes and alveolar macrophage hyperactivation.

**Stage IV — Critical disease (~5% of symptomatic):**
ARDS (PaO₂/FiO₂ <300), requiring mechanical ventilation; associated:
- **Cytokine storm:** Hyperactivated innate immunity (macrophage activation, complement activation, NF-κB) → massive release of IL-6, IL-1β, TNF-α, GM-CSF → diffuse vascular leak, coagulation activation, multiorgan dysfunction
- **COVID-19-associated coagulopathy:** Microvascular thrombosis (fibrin, platelet-rich thrombi) in pulmonary vasculature and systemic organs → thrombocytopenia, elevated D-dimer, arterial/venous thromboembolism

**Long COVID (post-acute sequelae of SARS-CoV-2 / PASC):**
Symptoms persisting >4 weeks: fatigue (most common), cognitive impairment ("brain fog"), dyspnea, autonomic dysfunction (POTS), musculoskeletal pain. Affects 10–20% of hospitalized and 5–10% of non-hospitalized patients. Mechanisms: viral persistence, autoantibodies, immune dysregulation, mitochondrial dysfunction, gut microbiome disruption.

### Treatment

**Antivirals:**
- **Nirmatrelvir/ritonavir (Paxlovid):** Protease inhibitor combination; >85% reduction in hospitalization/death if given within 5 days of symptom onset to high-risk patients; broad effectiveness across variants (targets conserved Mpro)
- **Remdesivir:** Nucleoside analog inhibiting RdRp (nsp12); IV formulation; reduces hospitalization duration and progression to ARDS in moderately ill patients
- **Molnupiravir:** Oral mutagenic nucleoside; 30% risk reduction; inferior to nirmatrelvir

**Immunomodulation (severe/critical disease):**
- **Dexamethasone 6 mg daily × 10 days:** Reduces 28-day mortality by 35% in ventilated patients (RECOVERY trial); no benefit in non-oxygen-requiring patients
- **Anti-IL-6 (tocilizumab, sarilumab):** Additional mortality benefit in patients already on dexamethasone with severe disease (CRP-guided)
- **Baricitinib (JAK1/2 inhibitor):** WHO-recommended for severe/critical disease; reduces mortality

**mRNA vaccines [^polack-2020-bnt162b2]:**
- BNT162b2 (Pfizer-BioNTech): 95% efficacy against original-strain symptomatic infection (Phase 3); encodes pre-fusion stabilized spike (2P mutations)
- mRNA-1273 (Moderna): 94% efficacy; higher dose (100 μg), more reactogenic; similar durability
- Both vaccines drive robust germinal center reactions in draining lymph nodes (months-long GC persistence), generating high-affinity memory B cells and long-lived plasma cells

## Connections

- `modulates` → **[ACE2](../../03-molecular/ace2/README.md)** — SARS-CoV-2 binds and downregulates ACE2, shifting Ang II/Ang-(1-7) balance toward pro-inflammatory Ang II signaling; ACE2 downregulation contributes to vascular dysfunction, hypertension, and ARDS in severe COVID-19.
- `connects-to` → **[Cytokine Storm](../cytokine-storm/README.md)** — severe COVID-19 is characterized by pathological cytokine release (IL-6, IL-1β, TNF-α, ferritin elevation); cytokine storm is the proximate driver of ARDS, vascular injury, and multiorgan failure in critical COVID-19.
- `targets` → **[Lung](../../06-organ/lung/README.md)** — the lung is the primary COVID-19 target organ; diffuse alveolar damage, type II pneumocyte necrosis, and pulmonary vascular thrombosis produce the bilateral ground-glass infiltrates and hypoxemia of COVID-19 pneumonia.
- `targets` → **[Respiratory System](../respiratory-system/README.md)** — SARS-CoV-2 initiates infection in the upper respiratory epithelium (ACE2-TMPRSS2 expression) and progresses to lower respiratory tract pneumonitis in severe disease; respiratory failure is the leading cause of COVID-19 mortality.
- `connects-to` → **[SARS-CoV-2](../sars-cov-2/README.md)** — SARS-CoV-2 is the causative betacoronavirus; NSP5 Mpro (nirmatrelvir), NSP12 RdRp (remdesivir), and Spike (vaccine antigen) are the key targets; NSP1/ORF6 IFN evasion enables early viral amplification before adaptive immunity responds.
- `connects-to` → **[SARS-CoV-2 Spike](../../03-molecular/sars-cov-2-spike/README.md)** — Spike is the primary COVID-19 vaccine antigen; RBD:ACE2 binding initiates infection; Spike-mediated ACE2 internalization amplifies ARDS; 2P prefusion-stabilized Spike is the basis of all approved mRNA vaccines; Omicron BA.1's 37 Spike mutations drive extensive immune escape.
- `treated-by` → **[Dexamethasone](../../03-medicine/01-modern/12-anti-inflammatory/dexamethasone/README.md)** — RECOVERY trial (Horby 2021): 6 mg OD × 10 days reduced 28-day mortality by 17% (RR 0.83) in patients requiring oxygen; 29% mortality reduction in mechanically ventilated patients; no benefit in those not requiring supplemental oxygen.
- `treated-by` → **[Corticosteroids](../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — RECOVERY trial (2021): dexamethasone 6 mg/d × 10 days; 36% mortality reduction in mechanically ventilated patients (RR 0.64); 18% reduction in those requiring supplemental oxygen; mechanism: GR:NF-κB transrepression of pro-inflammatory cytokine genes.
- `connects-to` → **[RSV](../rsv/README.md)** — COVID-19 and RSV are enveloped respiratory RNA viruses driving the seasonal lower-respiratory burden alongside influenza; both cause bronchiolitis/pneumonia at the extremes of age, both are now vaccine-preventable in older adults, and multiplex panels distinguish them.
- `connects-to` → **[Influenza](../influenza/README.md)** — COVID-19 and influenza are the dominant pandemic-capable respiratory viruses—overlapping fever, cough and pneumonia but distinct treatments (nirmatrelvir/remdesivir vs oseltamivir/baloxavir); co-circulation strains health systems and both have annually updated vaccines.
- `connects-to` → **[Type II pneumocyte](../../04-cellular/type-ii-pneumocyte/README.md)** — SARS-CoV-2 targets ACE2-expressing alveolar type II pneumocytes: infection destroys these surfactant-producing progenitor cells → alveolar collapse, hyaline membranes and diffuse alveolar damage → ARDS; their loss impairs lung repair and underlies severe COVID-19 hypoxemia.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — COVID-19 is strongly prothrombotic: SARS-CoV-2 endothelial injury and intense inflammation drive immunothrombosis, raising deep vein thrombosis, pulmonary embolism, and microvascular clots—so inpatients get thromboprophylaxis and D-dimer marks severity.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — COVID-19 is in part an endothelial disease: SARS-CoV-2 and inflammation injure ACE2-bearing endothelial cells, causing endotheliitis, microthrombi, and the capillary leak that drives severe lung and multi-organ failure—the virus's vascular face.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages drive severe COVID-19's cytokine storm: dysregulated alveolar macrophages pour out IL-6 and TNF in a macrophage-activation-like syndrome, fueling the hyperinflammation that dexamethasone and IL-6 blockade (tocilizumab) target in critically ill patients.
- `connects-to` → **[Acute Respiratory Distress Syndrome](../../06-organ/ards/README.md)** — ARDS is the lethal pulmonary endpoint of severe COVID-19: SARS-CoV-2 injury to alveolar epithelium and endothelium floods the lungs with protein-rich edema, collapsing gas exchange and requiring ventilation or ECMO—the final common pathway of fatal COVID pneumonia.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Type 2 diabetes markedly worsens COVID-19: hyperglycemia and the inflammatory, prothrombotic milieu of diabetes raise the risk of severe disease and death, while COVID can itself precipitate hyperglycemia and new diabetes—a bidirectional, dangerous interaction.
- `connects-to` → **[Stroke](../stroke/README.md)** — COVID-19 raises stroke risk through its prothrombotic state: SARS-CoV-2-driven endothelial injury and hypercoagulability cause arterial thromboses, so ischemic stroke is a recognized complication alongside the venous thromboembolism the infection provokes.
- `targets` → **[Alveolus](../../05-tissue/alveolus/README.md)** — COVID-19 pneumonia injures the alveolus directly: SARS-CoV-2 infects ACE2-bearing type II pneumocytes lining the air sacs, triggering diffuse alveolar damage, hyaline membranes and flooding that impair gas exchange and underlie hypoxemic respiratory failure.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Type I interferon is the fault line of severe COVID-19: inborn errors or autoantibodies blunting interferon predispose to critical disease, while SARS-CoV-2 also actively suppresses it—explaining why a weak early interferon response lets the virus run unchecked.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils worsen severe COVID-19: they flood inflamed lungs and release neutrophil extracellular traps (NETs) that drive immunothrombosis, clogging pulmonary microvessels and linking the hyperinflammatory and clotting features of the disease.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — COVID-19 reaches beyond the lungs to the brain: loss of smell and taste, strokes, and the lingering brain fog of long COVID reflect both direct effects and inflammation, so neurological symptoms are now recognized as core features, not rare complications.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — COVID-19 injures the heart: the infection and its inflammation cause myocarditis, arrhythmias, and raised troponin, and survivors carry elevated cardiovascular risk for months—so cardiac monitoring matters even after the respiratory illness resolves.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — B cells are central to COVID immunity: they generate the neutralizing antibodies that vaccines and prior infection rely on, but spike mutations in new variants erode that antibody protection—driving the need for updated boosters and explaining reinfections.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Cytotoxic T cells clear SARS-CoV-2-infected cells: CD8 T-cell responses help end the infection and, as durable memory, underpin protection from severe disease after infection or vaccination even when antibodies wane.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 drives COVID-19's cytokine storm: severe disease floods the blood with IL-6, fueling the hyperinflammation that injures the lungs—so the IL-6-blocker tocilizumab improves survival in critically ill patients alongside steroids.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — COVID-19 frequently injures the kidney: acute kidney injury is common in severe disease from direct infection, cytokines and microthrombi, and needing dialysis sharply worsens outcomes—evidence the virus is multisystem, not just respiratory.

## Pathology

**Diffuse alveolar damage (DAD):** Autopsy studies of COVID-19 ARDS show exudative phase DAD: protein-rich edema, hyaline membranes, type I pneumocyte necrosis, fibrin deposition, and reactive type II pneumocyte hyperplasia. Organizing phase: fibroblast proliferation, myofibroblast invasion, progressive fibrosis in some survivors.

**COVID-19-associated coagulopathy:** Elevated D-dimer, fibrinogen, and PT; microvascular fibrin thrombi throughout pulmonary and systemic capillaries (distinctive from DIC); likely driven by endothelialitis, platelet-endothelium interactions, and complement activation. Anticoagulation (prophylactic heparin) is standard for hospitalized COVID-19.

**Myocarditis/pericarditis:** Cardiac complications from direct myocardial ACE2-mediated infection or immune-mediated injury; also seen as rare (1 in 50,000–100,000) complication of mRNA vaccination, predominantly in young males, mostly mild and self-limited.

**COVID-19 and special populations:**
- Pregnancy: Higher risk of preterm birth, ICU admission, preeclampsia; vaccine strongly recommended
- Immunocompromised: Prolonged infection, viral evolution to immune-escape variants; chronic infection documented in hematology/oncology patients

[^guan-2020-china-cohort]: Guan WJ, Ni ZY, Hu Y, et al. Clinical Characteristics of Coronavirus Disease 2019 in China. *N Engl J Med.* 2020;382(18):1708-1720. [doi:10.1056/NEJMoa2002032](https://doi.org/10.1056/NEJMoa2002032) · [PubMed 32109013](https://pubmed.ncbi.nlm.nih.gov/32109013/)
[^hoffmann-2020-ace2-entry]: Hoffmann M, Kleine-Weber H, Schroeder S, et al. SARS-CoV-2 Cell Entry Depends on ACE2 and TMPRSS2. *Cell.* 2020;181(2):271-280. [doi:10.1016/j.cell.2020.02.052](https://doi.org/10.1016/j.cell.2020.02.052) · [PubMed 32142651](https://pubmed.ncbi.nlm.nih.gov/32142651/)
[^polack-2020-bnt162b2]: Polack FP, Thomas SJ, Kitchin N, et al. Safety and Efficacy of the BNT162b2 mRNA Covid-19 Vaccine. *N Engl J Med.* 2020;383(27):2603-2615. [doi:10.1056/NEJMoa2034577](https://doi.org/10.1056/NEJMoa2034577) · [PubMed 33301246](https://pubmed.ncbi.nlm.nih.gov/33301246/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

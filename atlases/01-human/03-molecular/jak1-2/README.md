---
schema: human-scale-entry/v1
id: jak1-2
name: JAK1/2
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Janus kinase 1 and 2; non-receptor tyrosine kinases that phosphorylate STAT proteins downstream of cytokine receptors (IL-6, IFN-gamma, EPO, GM-CSF). JAK2 V617F drives myeloproliferative neoplasms. Inhibited by ruxolitinib (MF/PV), baricitinib (RA), and upadacitinib."
aliases: ["JAK1", "JAK2", "JAK kinase", "Janus kinase 1", "Janus kinase 2", "JAK-STAT"]
sources:
  - id: vainchenker-2008-jak2-mpn
    type: peer-reviewed
    cite: "Vainchenker W, Constantinescu SN. A unique activating mutation in JAK2 (V617F) is at the origin of polycythemia vera and allows a new classification of myeloproliferative diseases. Hematology Am Soc Hematol Educ Program. 2005;2005:195-200."
    doi: "10.1182/asheducation-2005.1.195"
    pmid: "16304378"
    url: "https://doi.org/10.1182/asheducation-2005.1.195"
  - id: verstovsek-2012-ruxolitinib-mf
    type: peer-reviewed
    cite: "Verstovsek S, Mesa RA, Gotlib J, et al. A double-blind, placebo-controlled trial of ruxolitinib for myelofibrosis. N Engl J Med. 2012;366(9):799-807."
    doi: "10.1056/NEJMoa1110557"
    pmid: "22375971"
    url: "https://doi.org/10.1056/NEJMoa1110557"
  - id: fleischmann-2017-upadacitinib-ra
    type: peer-reviewed
    cite: "Fleischmann R, Mysler E, Hall S, et al. Efficacy and safety of tofacitinib monotherapy, tofacitinib with methotrexate, and adalimumab with methotrexate in patients with rheumatoid arthritis. Lancet. 2017;390(10093):457-468."
    doi: "10.1016/S0140-6736(17)31619-7"
    pmid: "28629651"
    url: "https://doi.org/10.1016/S0140-6736(17)31619-7"
cross_links:
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "JAK1 (activated by IL-6 receptor) phosphorylates STAT3 Tyr705 → STAT3 dimerization → nuclear translocation → pro-survival transcription; JAK1/2 inhibition (ruxolitinib, baricitinib) blocks STAT3 activation in inflammatory and malignant contexts."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 binds IL-6R/gp130 → JAK1/TYK2 activation → STAT3/1/2 phosphorylation → acute-phase and pro-inflammatory transcription; JAK inhibitors (baricitinib, upadacitinib) block IL-6 and other cytokine receptor signaling simultaneously, unlike tocilizumab which blocks only IL-6R."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF-alpha primarily activates NF-kB; JAK inhibitors (baricitinib, tofacitinib) reduce TNF-alpha by blocking IL-6 and IFN-gamma JAK-STAT loops; ruxolitinib reduces cytokine storm in MPN and GvHD by suppressing TNF-alpha and other JAK-dependent cytokines."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "JAK1/2/3 inhibitors are approved tsDMARDs for RA; baricitinib (JAK1/2) and upadacitinib (JAK1) are superior to adalimumab in clinical trials; selectivity for JAK1 vs JAK2/3 reduces erythropoiesis and platelet effects; safety: infection, VTE, MACE risk inform patient selection."
  - target: 01-human/07-system/dermatomyositis
    relation: connects-to
    note: "Baricitinib (JAK1/2) showed efficacy in refractory DM (TRiMM-2 Phase 3); tofacitinib (JAK1/3) used for anti-MDA5-associated rapidly progressive ILD; ruxolitinib in refractory MDA5+ DM-ILD; JAK inhibition reduces type I IFN-driven ISG expression in DM muscle."
---

# JAK1/2

## Overview

**JAK1 and JAK2 (Janus kinase 1 and 2)** are **non-receptor tyrosine kinases** of the JAK family (JAK1, JAK2, JAK3, TYK2) that mediate intracellular signaling downstream of **type I and type II cytokine receptors** — receptors lacking intrinsic kinase activity that rely on constitutively associated JAKs. JAK-STAT signaling transmits signals from dozens of cytokines (interferons, interleukins, colony-stimulating factors, hormones like EPO, TPO, GH) to the nucleus via **STAT (signal transducers and activators of transcription) proteins**.

JAK1/2 represent two of the most clinically significant kinases in medicine:
- **JAK2 V617F:** Acquired gain-of-function mutation in **~95% of polycythemia vera (PV)** and **50-60% of essential thrombocythemia (ET) and primary myelofibrosis (MF)** — the founding discovery of the myeloproliferative neoplasm (MPN) field [^vainchenker-2008-jak2-mpn]
- **JAK1/2 inhibition:** Ruxolitinib (JAK1/2) is FDA-approved for MF, PV, and graft-versus-host disease (GvHD); baricitinib (JAK1/2) and upadacitinib (JAK1-selective) approved for rheumatoid arthritis; tofacitinib (JAK1/3) approved for RA, PsA, and UC; filgotinib (JAK1) for UC and Crohn's

**JAK family overview:**
- **JAK1:** Pairs with JAK2, JAK3, or TYK2 → type I IFN (IFN-alpha/beta), IL-6 family (gp130), IL-2 family (common gamma chain), IL-4/13 family signaling; ubiquitous expression
- **JAK2:** Pairs with JAK2 (homodimer) → EPO, TPO, GH, G-CSF, IFN-gamma signaling; also pairs with JAK1 (IL-6 family); expressed in hematopoietic and endothelial cells
- **JAK3:** Pairs exclusively with JAK1 → IL-2, IL-4, IL-7, IL-9, IL-15, IL-21 (common gamma chain cytokines) → T and NK cell development; expressed in hematopoietic/lymphoid cells; JAK3-selective inhibition limits immune suppression to lymphocyte pathways
- **TYK2:** Pairs with JAK1/JAK2 → type I IFN (IFN-alpha/beta), IL-12, IL-23 signaling; expressed broadly; TYK2 inhibitor (deucravacitinib) approved for psoriasis (2022)

## Structure

### JAK kinase domain architecture

Each JAK protein contains **seven JAK-homology (JH) domains (JH1-7)**:
- **JH1 (C-terminal kinase domain):** Tyrosine kinase catalytic domain; contains activation loop with key autophosphorylation sites (JAK2 Tyr1007/1008); active in full-length receptor-associated JAK
- **JH2 (pseudokinase domain):** Structurally similar to kinase domain but lacks catalytic activity; functions as an **autoinhibitory regulator** of JH1; allosteric communication between JH1 and JH2; **JAK2 V617F** is in the JH2 domain → relieves JH2-mediated autoinhibition → constitutive JH1 activation
- **JH3-7 (N-terminal FERM + SH2-like domains):** Required for receptor binding; FERM domain (band 4.1, ezrin, radixin, moesin) directly contacts cytokine receptor Box 1/Box 2 motifs → constitutive receptor association; SH2-like domain (JH3-4) contacts phosphorylated receptor tyrosines after cytokine binding

**JAK2 V617F mechanism:**
- Val→Phe at position 617 in JH2 → structural clash → destabilizes JH2 autoinhibitory conformation → JH1 becomes constitutively active → cytokine-independent JAK2 signaling → myeloproliferative disease (constitutive EPO, TPO, G-CSF signaling → erythrocytosis, thrombocytosis, myelofibrosis)

### JAK inhibitor structure

JAK inhibitors are **ATP-competitive small molecules** targeting the JH1 kinase domain ATP binding pocket. Selectivity is determined by differences in the ATP binding site across JAK isoforms:
- **Type I (DFG-in, active conformation):** Ruxolitinib, baricitinib, tofacitinib, upadacitinib
- **Type II (DFG-out, inactive conformation):** Pacritinib (JAK2/IRAK1) — avoids JAK1/3 → less anemia
- **Covalent:** Itacitinib (selective JAK1)

**Selectivity profile:**
- **Ruxolitinib:** JAK1~JAK2 >> JAK3 >> TYK2; approved MF, PV, GvHD, GVHD (cGVHD)
- **Baricitinib:** JAK1~JAK2 >> JAK3 = TYK2; approved RA, atopic dermatitis, COVID-19 hospitalized
- **Upadacitinib:** JAK1 >> JAK2/3; approved RA, PsA, AS, atopic dermatitis, Crohn's, UC
- **Tofacitinib:** JAK1~JAK3 > JAK2; approved RA, PsA, UC, polyarticular JIA
- **Filgotinib:** JAK1 >> JAK2 (~30× selectivity); approved UC in EU; Crohn's FDA filed

## Function

### JAK-STAT signaling cascade

The canonical JAK-STAT pathway:

1. **Cytokine binding** → receptor dimerization/oligomerization → conformational change bringing receptor-bound JAKs into proximity
2. **JAK transphosphorylation:** JAK1-JAK2 (or JAK2-JAK2 homodimer) transphosphorylate activation loop tyrosines → kinase activation
3. **Receptor tyrosine phosphorylation:** Active JAKs phosphorylate receptor cytoplasmic tail tyrosines → create docking sites for STAT SH2 domains
4. **STAT recruitment and phosphorylation:** STATs bind via SH2 domain → JAK phosphorylates STAT tyrosine (e.g., STAT3 Tyr705, STAT1 Tyr701) → STAT dissociates from receptor
5. **STAT dimerization:** Phospho-STATs dimerize via reciprocal SH2-pTyr interactions → translocate to nucleus → bind GAS or ISRE elements → gene transcription
6. **Termination:** SOCS proteins (suppressors of cytokine signaling, SOCS1-7) → bind JAK or receptor → negative feedback; PIAS (protein inhibitors of activated STATs) → SUMO-mediated STAT inhibition; phosphatases (SHP-1, SHP-2, CD45) → dephosphorylate JAKs and STATs

**Key JAK-STAT pathways:**

| Cytokine | Receptor | JAK pair | Primary STAT | Function |
|:---|:---|:---|:---|:---|
| IFN-alpha/beta | IFNAR1/2 | JAK1/TYK2 | STAT1/STAT2 | Antiviral, ISG induction |
| IFN-gamma | IFNGR1/2 | JAK1/JAK2 | STAT1 | Macrophage activation |
| IL-6 | IL-6R/gp130 | JAK1/JAK2 | STAT3 | Acute phase, Th17 |
| EPO | EPOR | JAK2/JAK2 | STAT5 | Erythropoiesis |
| TPO | MPL | JAK2/TYK2 | STAT5 | Thrombopoiesis |
| IL-2 | IL-2Rβγ | JAK1/JAK3 | STAT5 | T cell proliferation |
| IL-4/IL-13 | IL-4Rα | JAK1/JAK3 | STAT6 | Th2, IgE, fibrosis |
| IL-12 | IL-12Rβ1/2 | JAK2/TYK2 | STAT4 | Th1 differentiation |
| IL-23 | IL-23R | JAK2/TYK2 | STAT3/STAT4 | Th17 differentiation |

### JAK2 V617F in myeloproliferative neoplasms [^vainchenker-2008-jak2-mpn]

**Discovery:** JAK2 V617F was identified simultaneously by four groups in 2005 (Levine, James, Kralovics, Baxter) — the first unified molecular mechanism for the BCR-ABL-negative MPNs.

**Pathogenesis:**
- JAK2 V617F → constitutive JAK2 activation → cytokine-independent proliferation and differentiation of myeloid progenitors
- Clonal expansion from a single HSC (hematopoietic stem cell) → increased erythroid, megakaryocyte, and myeloid output
- **Polycythemia vera (PV):** JAK2 V617F homozygosity (loss of heterozygosity) → extreme erythrocytosis; hyperviscosity → stroke, PE, DVT (major cause of morbidity/mortality); venesection + ruxolitinib
- **Essential thrombocythemia (ET):** JAK2 V617F heterozygous; platelet count >450 k/μL; thrombosis risk; hydroxyurea, aspirin, anagrelide, or ruxolitinib
- **Primary myelofibrosis (MF):** Fibrosis of bone marrow (reticulin → collagen) → progressive pancytopenia, extramedullary hematopoiesis (splenomegaly), constitutional symptoms (fatigue, night sweats, weight loss); median OS 5-7 years (IPSS high-risk); stem cell transplant is only curative option; ruxolitinib reduces spleen size and constitutional symptoms [^verstovsek-2012-ruxolitinib-mf]

**Other MPN mutations:**
- **CALR (calreticulin) mutations:** Exon 9 insertions/deletions in JAK2 V617F-negative ET/MF (~25% of ET, ~35% of MF); activate MPL (TPO receptor) via unconventional mechanism → JAK2 activation without direct JAK2 mutation; better prognosis than JAK2 V617F in ET
- **MPL W515L/K:** Activating mutations in TPO receptor → JAK2 activation; 5-10% of JAK2/CALR-negative MF

## Mechanism

### Ruxolitinib (JAK1/2 inhibitor) [^verstovsek-2012-ruxolitinib-mf]

**Ruxolitinib (Jakafi/Jakavi, Incyte):** First JAK inhibitor approved (FDA 2011 for MF, 2014 for PV); competitive JAK1~JAK2 inhibitor (IC50 JAK1 3.3 nM, JAK2 2.8 nM).

**COMFORT-I trial (ruxolitinib vs. placebo in MF):**
- Primary endpoint: 35% reduction in spleen volume from baseline at week 24
- Ruxolitinib: 41.9% achieved primary endpoint vs. 0.7% placebo
- Improved symptom score (TSS), OS advantage at 5 years (hazard ratio 0.69)
- **Side effects:** Dose-dependent anemia and thrombocytopenia (platelet count-guided dosing); increased herpes zoster reactivation; lymphoma risk with long-term use; second malignancy (MYELOFIBROSIS duration concern)

**Baricitinib (JAK1/2) in COVID-19 (ACTT-2):**
- Hospitalized COVID-19 patients: baricitinib + remdesivir → median 7 days to clinical improvement vs. 9 days with remdesivir alone; WHO Solidarity baricitinib arm similarly positive; baricitinib now preferred anti-inflammatory in COVID-19 over IL-6 inhibitors for hospitalized patients (less immunosuppression at low doses)

**Ruxolitinib in steroid-refractory GvHD:**
- Acute GvHD (aGvHD): REACH1/REACH2 — ruxolitinib vs. best available therapy → 62% ORR (ruxolitinib) vs. 39% (BAT) at day 28; FDA approved 2019
- Chronic GvHD (cGvHD): REACH3 → 70% ORR vs 57% BAT

### Selectivity and safety considerations

**Hematological toxicity from JAK2 inhibition:**
- EPO → JAK2 → STAT5 → erythropoiesis; JAK2 inhibition → dose-dependent anemia
- TPO → JAK2 → STAT5 → thrombopoiesis; JAK2 inhibition → thrombocytopenia
- JAK1-selective agents (upadacitinib, filgotinib) spare these pathways → fewer hematological AEs

**Class-effect safety concerns for JAK inhibitors:**
- **Serious infection:** Reactivation of herpes zoster (VZV prophylaxis with valacyclovir recommended), TB (screen before initiation), CMV; pneumonia in RA; risk higher than anti-TNF
- **Venous thromboembolism (VTE):** DVT, PE; more prominent with tofacitinib at 10 mg BID in older patients with ASCVD risk (ORAL Surveillance); FDA 2021 boxed warning; prefer baricitinib/upadacitinib in low-VTE-risk patients
- **Major adverse cardiovascular events (MACE):** Tofacitinib increased MACE in post-MI/high-CV-risk RA; FDA safety labeling; caution in older patients with CV risk factors
- **Malignancy:** Non-melanoma skin cancer; lymphoma risk (especially in RA with immunosuppression)

## Connections

- `connects-to` → **[STAT3](../stat3/README.md)** — JAK1 (activated by IL-6R, IFN-gamma receptor) phosphorylates STAT3 Tyr705 → STAT3 dimerization → nuclear translocation → anti-apoptotic and inflammatory transcription; JAK1/2 inhibition (baricitinib, ruxolitinib) blocks STAT3 activation in RA, MF, and cytokine storm.
- `connects-to` → **[IL-6](../il-6/README.md)** — IL-6 binds IL-6R/gp130 → JAK1/TYK2 activation → STAT3/STAT1 phosphorylation; JAK inhibitors block IL-6 and all other JAK-dependent cytokines simultaneously, unlike single-cytokine biologics; useful in diseases with polycytokine pathogenesis.
- `connects-to` → **[TNF-alpha](../tnf-alpha/README.md)** — TNF-alpha drives inflammation primarily via NF-kB but also activates JAK1 in some pathways; JAK inhibitors reduce TNF-alpha production indirectly by blocking JAK-STAT loops that amplify TNF-alpha secretion; ruxolitinib attenuates cytokine storm in MF and GvHD.
- `connects-to` → **[Rheumatoid Arthritis](../../07-system/rheumatoid-arthritis/README.md)** — baricitinib (JAK1/2) and upadacitinib (JAK1) are approved tsDMARDs for RA; superior to adalimumab in clinical trials; selectivity for JAK1 vs JAK2/3 reduces hematological side effects; safety warnings for VTE, MACE, and serious infection guide patient selection.
- `connects-to` → **[Dermatomyositis](../../07-system/dermatomyositis/README.md)** — Baricitinib (JAK1/2) showed efficacy in refractory DM (TRiMM-2 Phase 3); tofacitinib (JAK1/3) used for anti-MDA5-associated rapidly progressive ILD; ruxolitinib in refractory MDA5+ DM-ILD; JAK inhibition reduces type I IFN-driven ISG expression in DM muscle.

[^vainchenker-2008-jak2-mpn]: Vainchenker W, Constantinescu SN. A unique activating mutation in JAK2 (V617F) is at the origin of polycythemia vera and allows a new classification of myeloproliferative diseases. *Hematology Am Soc Hematol Educ Program.* 2005;2005:195-200. [doi:10.1182/asheducation-2005.1.195](https://doi.org/10.1182/asheducation-2005.1.195) · [PubMed 16304378](https://pubmed.ncbi.nlm.nih.gov/16304378/)
[^verstovsek-2012-ruxolitinib-mf]: Verstovsek S, Mesa RA, Gotlib J, et al. A double-blind, placebo-controlled trial of ruxolitinib for myelofibrosis. *N Engl J Med.* 2012;366(9):799-807. [doi:10.1056/NEJMoa1110557](https://doi.org/10.1056/NEJMoa1110557) · [PubMed 22375971](https://pubmed.ncbi.nlm.nih.gov/22375971/)
[^fleischmann-2017-upadacitinib-ra]: Fleischmann R, Mysler E, Hall S, et al. Efficacy and safety of tofacitinib monotherapy, tofacitinib with methotrexate, and adalimumab with methotrexate in patients with rheumatoid arthritis. *Lancet.* 2017;390(10093):457-468. [doi:10.1016/S0140-6736(17)31619-7](https://doi.org/10.1016/S0140-6736(17)31619-7) · [PubMed 28629651](https://pubmed.ncbi.nlm.nih.gov/28629651/)

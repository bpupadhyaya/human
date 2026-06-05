---
schema: pathogen-entry/v1
id: leishmania-donovani
name: Leishmania donovani
atlas: 02-pathogen
scale: 04-parasites
status: draft
last_reviewed: 2026-06-05
summary: "Kinetoplastid; amastigote survives in macrophage phagolysosomes; sandfly vector. gp63 + LPG virulence factors; inhibits phagolysosome acidification. Visceral leishmaniasis: hepatosplenomegaly, pancytopenia. ~50,000-90,000 new cases/year; ~30,000 deaths if untreated."
aliases: ["L. donovani", "visceral leishmaniasis", "kala-azar", "black fever", "Leishmania donovani", "VL", "PKDL"]
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
  - id: kaye-2011-leishmania
    type: peer-reviewed
    cite: "Kaye P, Scott P. Leishmaniasis: complexity at the host-pathogen interface. Nat Rev Microbiol. 2011;9(8):604-15."
    doi: "10.1038/nrmicro2608"
    pmid: "21747391"
    url: "https://doi.org/10.1038/nrmicro2608"
  - id: chappuis-2007-vl-review
    type: peer-reviewed
    cite: "Chappuis F, Sundar S, Hailu A, et al. Visceral leishmaniasis: what are the needs for diagnosis, treatment and control? Nat Rev Microbiol. 2007;5(11):873-82."
    doi: "10.1038/nrmicro1748"
    pmid: "17938629"
    url: "https://doi.org/10.1038/nrmicro1748"
cross_links:
  - target: 01-human/04-cellular/macrophage
    relation: infects
    note: "gp63 cleaves complement C3b to C3bi, promoting CR3-mediated uptake; LPG coats amastigotes and inhibits PKC activation; peroxynitrite scavenged by iron-superoxide dismutase; amastigotes replicate in phagolysosome."
  - target: 01-human/07-system/immune-system
    relation: damages
    note: "Visceral leishmaniasis causes profound immunosuppression; parasite-driven IL-10 production suppresses IL-12/IFN-gamma axis; parasite-specific T cell anergy; secondary infections common; post-kala-azar dermal leishmaniasis (PKDL) follows treatment."
  - target: 01-human/06-organ/liver
    relation: damages
    note: "Kupffer cells and hepatic macrophages infected; hepatomegaly from parasite-laden Kupffer cells and portal inflammation; hypoalbuminaemia from hepatic dysfunction; liver pathology partially reversible with treatment."
  - target: 01-human/07-system/digestive-system
    relation: damages
    note: "Hepatosplenomegaly leads to hypersplenism and pancytopenia; gut-associated lymphoid tissue (GALT) macrophages act as reservoir; weight loss and malabsorption in severe VL; enteric involvement less prominent than splenic."
---

# Leishmania donovani

## Overview

***Leishmania donovani*** is the primary causative agent of **visceral leishmaniasis (VL)**, also known as **kala-azar** (Hindi/Urdu: "black fever," referring to the skin darkening — hyperpigmentation — that characterises advanced disease). It is the most dangerous form of leishmaniasis and is uniformly fatal if untreated. The leishmaniases collectively represent a major neglected tropical disease (NTD) complex — caused by >20 species of *Leishmania* — but visceral leishmaniasis, caused by *L. donovani* (Indian subcontinent, East Africa) and *L. infantum/L. chagasi* (Mediterranean Europe, Latin America), carries the highest mortality burden [^chappuis-2007-vl-review].

The WHO estimates **50,000–90,000 new VL cases** per year globally, with approximately **30,000 deaths** annually if untreated — and this is considered a substantial undercount given limited diagnostic capacity in endemic regions. More than 90% of cases occur in just six countries: India, Bangladesh, Sudan, South Sudan, Ethiopia, and Brazil.

*Leishmania* occupies a fascinating niche in parasitology: it is an **obligate intracellular parasite that has evolved to survive and replicate inside the most hostile environment macrophages can create — the phagolysosome** (pH 5.5, loaded with reactive oxygen species, hydrolytic enzymes, and nitrogen radicals). The parasite's molecular toolkit for surviving inside macrophage phagolysosomes involves lipid-based surface molecules (LPG, lipophosphoglycan), metalloprotease-based complement manipulation (gp63), and metabolic adaptations to acidic, nutrient-poor conditions [^kaye-2011-leishmania].

## Structure

**Life cycle stages and morphology:**

| Stage | Location | Size | Features |
|:---|:---|:---|:---|
| **Promastigote** | Sandfly (Phlebotomus/Lutzomyia) midgut and hindgut | 10–20 µm elongated; anterior flagellum | Non-infective procyclic → infective metacyclic promastigote (shorter, stouter, 7–10 µm); dense LPG coat on metacyclic form |
| **Amastigote** | Mammalian macrophage phagolysosome | 2–4 µm, round/oval; rudimentary flagellum (kinetoplast visible) | Non-motile; replicates by binary fission; adapted for phagolysosomal survival |

**Key molecular virulence factors:**

- **gp63 (Leishmanolysin, Major Surface Protease):** 63-kDa zinc metalloprotease; GPI-anchored; most abundant surface protein on metacyclic promastigotes (~500,000 copies/cell); multifunctional:
  - Cleaves complement component C3b → iC3b (inactivated C3b) → iC3b-opsonised promastigotes are taken up via CR3 (Mac-1, CD11b/CD18) — a non-inflammatory receptor that does not trigger oxidative burst
  - Cleaves and inactivates complement C5 → prevents MAC (membrane attack complex) formation
  - Inside macrophage: cleaves and inactivates PKC-α and PKC-β (preventing oxidative burst activation); cleaves STAT1 and NF-κB p65 to suppress macrophage activation
  - Degrades antibody Fc regions on the parasite surface

- **LPG (Lipophosphoglycan):** Major surface glycolipid of promastigotes; GPI-anchored polymer of phosphorylated galactosyl-mannose repeating units with a lipid A core; undergoes major structural change between procyclic and metacyclic forms (stage-specific); functions:
  - Inhibits phagosome-lysosome fusion immediately after parasite uptake (transiently delays acidification by ~30 min, allowing parasite to adapt)
  - Scavenges reactive oxygen species (ROS) — antioxidant buffer
  - Inhibits PKC-α activation (suppresses respiratory burst signal transduction)
  - Complement resistance: its repeating units bind complement C3 but resist MAC assembly

- **A2 protein:** Amastigote-specific stress protein; viscerotropism-associated; *L. donovani* and *L. infantum* express A2 (viscerotropic species); cutaneous *Leishmania* (e.g., *L. major*) do not; A2 expression required for intrasplenic growth and persistence

- **Iron-Superoxide Dismutase (FeSOD):** Cytoplasmic enzyme uniquely using Fe³⁺ as cofactor (mammals use Mn-SOD or Cu/Zn-SOD); FeSOD scavenges superoxide radicals (O₂⁻) generated by host NADPH oxidase; critical survival factor inside macrophage phagolysosome

- **Amastin surface proteins:** Stage-specific (amastigote); GPI-anchored; structural role in surface coat maintenance in the phagolysosomal environment

- **Kinetoplast (kDNA):** Large concatenated mitochondrial DNA network (minicircles + maxicircles); minicircles encode guide RNAs for RNA editing of maxicircle transcripts; target for diagnostic PCR (kDNA PCR highly sensitive)

## Infection Mechanism

**Step-by-step molecular pathogenesis:**

**1. Sandfly inoculation:**
- Female *Phlebotomus* (Old World: India, East Africa, Mediterranean) or *Lutzomyia* (New World: Brazil) sandfly takes a blood meal; metacyclic promastigotes regurgitated with saliva into skin (forceful inoculation during sandfly feeding)
- **Sandfly saliva** (maxadilan in New World; adenosine, prostaglandin E2 in Old World) suppresses local innate immunity: inhibits NK cell activation, promotes Th2 response, enhances Leishmania survival at inoculation site

**2. Complement evasion and phagocyte recruitment:**
- Metacyclic promastigotes in dermis activate complement (alternative pathway via LPG)
- gp63 cleaves C3b → iC3b; iC3b-opsonised promastigotes signal CR3 on neutrophils and macrophages
- **Neutrophil "Trojan horse":** Promastigotes are first phagocytosed by neutrophils (abundant at bite site); neutrophils die by apoptosis within hours (carrying intact amastigotes); apoptotic neutrophils are phagocytosed by macrophages ("efferocytosis") — non-inflammatory uptake that suppresses macrophage activation signals; this delays effective macrophage killing response

**3. Macrophage phagocytosis — multiple receptors engaged:**
- Receptors for uptake: CR1 (CD35, via C3b), CR3 (CD11b/CD18, via iC3b), FcγR (via antibody, in immune hosts), mannose receptor (CD206, via mannose-rich LPG/gp63 glycans), scavenger receptor SR-A
- CR3-mediated uptake is preferred: does not activate the respiratory burst; does not trigger NF-κB-dependent pro-inflammatory signalling; provides an immunologically "quiet" portal of entry

**4. Phagosome maturation arrest and pH adaptation:**
- Normal phagosome: Rab5 (early endosome) → Rab7 (late endosome) → LAMP-1/2 acquisition → acidification (pH 6.0) → lysosomal enzyme delivery → digestion
- *L. donovani* LPG transiently inhibits PKC-α → delays PI3-kinase recruitment → slows Rab5→Rab7 transition → delays full phagolysosome maturation by ~20–30 minutes
- During this window, promastigotes differentiate into amastigotes (shorter flagellum, rounder shape, acid-stable HSP70/HSP83 upregulated, metabolic shifts)
- **Amastigotes are paradoxically ADAPTED to the phagolysosome:** Optimal growth at pH 5.0–5.5; acid-stable metabolic enzymes; FeSOD for ROS neutralisation; cysteine proteases (CPA, CPB) for nutrient acquisition at low pH

**5. Inhibition of macrophage killing mechanisms:**
- **NADPH oxidase inhibition:** LPG prevents PKC-mediated phosphorylation of p47phox (cytosolic component) → reduced assembly of NADPH oxidase complex → diminished superoxide production; gp63 also cleaves and inactivates NADPH oxidase subunits
- **iNOS suppression:** IL-12 and IFN-γ required for iNOS (inducible nitric oxide synthase) induction in macrophages; *L. donovani* suppresses IL-12 production from infected macrophages (via ERK1/2 activation → Th2 cytokine cascade); reduces IFN-γ responsiveness of macrophages (JAK/STAT1 signalling blunted by gp63-mediated STAT1 cleavage)
- **IL-10 induction:** Infected macrophages upregulate IL-10 (via Erk → CREB activation → IL-10 promoter); IL-10 acts in autocrine/paracrine loop to suppress TNF-α and IL-12; maintains anti-inflammatory macrophage phenotype (M2-like)

**6. Systemic dissemination (viscerotropism):**
- Amastigote-laden macrophages migrate through lymphatics → spleen, liver (Kupffer cells), bone marrow
- Spleen: massive expansion of infected and bystander macrophages → splenomegaly; splenic architecture disrupts (germinal centres lost → impaired B cell responses)
- Liver: Kupffer cell infection → hepatomegaly; portal infiltration; inflammatory hepatitis; A2 protein expression required for hepatic/splenic persistence (viscerotropism vs. cutaneotropism determinant)
- Bone marrow: infiltration of infected macrophages → hematopoietic suppression → pancytopenia (anaemia, thrombocytopenia, neutropenia)

## Host Interactions

**Cells and tissues targeted:**

| Cell/Tissue | Mechanism | Consequence |
|:---|:---|:---|
| Dermal macrophages/dendritic cells | First line of infection; CR3/mannose-mediated uptake | Dissemination if not controlled |
| Neutrophils | "Trojan horse" efferocytosis pathway | Delivery of intact parasites to macrophages in non-inflammatory context |
| Kupffer cells (hepatic macrophages) | Hematogenous arrival; infected Kupffer cells proliferate | Hepatomegaly; hepatic amastigote reservoir |
| Splenic macrophages | Hematogenous seeding; massive expansion | Splenomegaly; B cell follicle collapse; hypersplenism → pancytopenia |
| Bone marrow macrophages | Hematogenous seeding | Haemopoietic suppression; anaemia, thrombocytopenia, neutropenia |
| B cells (indirect) | Polyclonal activation by parasite mitogens | Hypergammaglobulinaemia (↑IgG, IgM); anti-Leishmania antibodies not protective for VL |

**Immune evasion (comprehensive):**

| Mechanism | Molecular basis | Effect |
|:---|:---|:---|
| Complement evasion | gp63 cleaves C3b→iC3b; LPG resists MAC | Serum-resistant; CR3-mediated uptake |
| Oxidative burst suppression | LPG inhibits PKC-α; FeSOD scavenges O₂⁻; gp63 inactivates NADPH oxidase | Reduced respiratory burst in infected macrophage |
| Phagolysosome survival | Acid-stable amastigote enzymes; LPG ROS scavenging; FeSOD; cysteine proteases | Replication at pH 5.0–5.5 |
| IL-12 suppression | ERK1/2→CREB activation → IL-10 induction; MAPK-mediated IL-12 blockade | Impaired Th1 induction; T cell anergy |
| STAT1 cleavage (gp63) | gp63 inactivates STAT1 inside macrophage | IFN-γ signal transduction blunted |
| PKC cleavage (gp63) | gp63 cleaves PKC-α and -β | Reduces phosphorylation of downstream inflammatory targets |
| Neutrophil Trojan horse | Anti-apoptotic effect in neutrophils → delayed death → efferocytosis | Silent delivery to macrophages |

**Protective immunity (for recovery/resolution):**

VL can be fatal without treatment, but a minority of infected individuals naturally clear infection. Protective immunity requires:
- **Th1 polarisation:** IL-12 from non-infected DCs → IFN-γ from NK cells and CD4+ T cells → macrophage classical activation (M1) → iNOS → NO → kills amastigotes
- **CD8+ T cells:** Cytolysis of infected macrophages; IFN-γ production
- **Absence of IL-10:** IL-10 knockout mice and IL-10 blockade in humans dramatically improves parasite clearance (IL-10 is the central immune evasion cytokine)
- **Post-treatment:** Acquiring long-term immunity after treatment requires CD4+ memory T cells expressing IFN-γ/TNF-α; NK cells; memory cells persist years in treated patients (basis for human vaccination attempts)

## Connections

- **Infects** → [Macrophage](../../../01-human/04-cellular/macrophage/README.md): gp63 cleaves complement C3b to C3bi, promoting CR3-mediated uptake; LPG coats amastigotes and inhibits PKC activation; peroxynitrite scavenged by iron-superoxide dismutase; amastigotes replicate in phagolysosome.

- **Damages** → [Immune System](../../../01-human/07-system/immune-system/README.md): Visceral leishmaniasis causes profound immunosuppression; parasite-driven IL-10 production suppresses IL-12/IFN-gamma axis; parasite-specific T cell anergy; secondary infections common; post-kala-azar dermal leishmaniasis (PKDL) follows treatment.

- **Damages** → [Liver](../../../01-human/06-organ/liver/README.md): Kupffer cells and hepatic macrophages infected; hepatomegaly from parasite-laden Kupffer cells and portal inflammation; hypoalbuminaemia from hepatic dysfunction; liver pathology partially reversible with treatment.

- **Damages** → [Digestive System](../../../01-human/07-system/digestive-system/README.md): Hepatosplenomegaly leads to hypersplenism and pancytopenia; gut-associated lymphoid tissue (GALT) macrophages act as reservoir; weight loss and malabsorption in severe VL; enteric involvement less prominent than splenic.

## Pathology

**Clinical visceral leishmaniasis (kala-azar):**

Incubation: **2–6 months** (range: weeks to >2 years). Classic VL presentation:
- **Fever:** Prolonged, undulant (double daily fever spikes — "double quotidian"), often months duration; fever with relative bradycardia
- **Splenomegaly:** Massive; may extend below umbilicus; spleen can become the largest organ by weight in the body
- **Hepatomegaly:** Less marked than splenomegaly; hepatic macrophage infiltration
- **Weight loss and cachexia:** Profound; patients with VL in the Indian subcontinent (kala-azar) classically appear wasted with massive splenomegaly
- **Skin darkening (hyperpigmentation):** "Kala-azar" = Hindi for "black fever"; hyperpigmentation of face, hands, feet (cause: ACTH-like parasite products stimulating melanocytes, or cortisol metabolism changes)
- **Pancytopenia:** Anaemia (normocytic; haemolytic + hypersplenism + bone marrow suppression), thrombocytopenia (bleeding), neutropenia (secondary infections)
- **Hypoalbuminaemia + hypergammaglobulinaemia:** Protein malnutrition, hepatic dysfunction, massive IgG/IgM production; low albumin → oedema, ascites
- **Secondary infections:** Pneumonia, TB (co-infection common, especially in East Africa), other opportunistic infections; major cause of death

**Post-Kala-azar Dermal Leishmaniasis (PKDL):**

Occurs in ~5–10% (India) to ~50% (Sudan) of successfully treated VL patients; appears weeks to years after VL treatment; characteristic macular, maculopapular, or nodular skin rash (hypopigmented macules on face → progressive skin involvement); caused by residual amastigotes in dermis; important **transmission reservoir** (parasite reachable by sandflies on skin); treatment required (longer, more difficult); pathogenesis involves partial immune reconstitution driving dermal inflammation.

**Epidemiology:**

| Parameter | Value |
|:---|:---|
| Annual new VL cases | 50,000–90,000 (WHO 2022 estimate; underreported) |
| Mortality (untreated) | Near 100% within 2 years |
| Deaths/year (treated/untreated combined) | ~20,000–30,000 |
| Major endemic countries | India, Bangladesh, Nepal, Sudan, South Sudan, Ethiopia, Brazil |
| HIV-VL co-infection | Up to 35% of VL in Ethiopia; dramatically worsens prognosis; higher relapse rate |
| Zoonotic reservoirs | *L. infantum/chagasi*: dogs (domestic reservoir); *L. donovani*: anthroponotic (humans only) |
| Vector | *Phlebotomus argentipes* (India/Bangladesh); *P. orientalis* (Sudan/Ethiopia); *Lutzomyia longipalpis* (Brazil) |

**Diagnosis:**

| Test | Sensitivity | Specificity | Notes |
|:---|:---|:---|:---|
| rK39 RDT (immunochromatographic strip) | 92–100% (India); 67–85% (East Africa/Brazil) | 96–100% | Recombinant antigen K39 (kinesin-related); rapid, field-applicable; lower sensitivity in Africa where non-Ld species occur |
| Direct agglutination test (DAT) | ~90% | ~95% | Long shelf-life; good for remote settings; labour-intensive |
| Bone marrow/spleen/lymph node aspiration and microscopy | 53–86% (marrow); 93–99% (spleen) | ~100% | Gold standard parasitological; spleen aspiration carries haemorrhage risk (requires platelet count >40,000); lymph node aspiration safer |
| Splenic/bone marrow/blood PCR | 70–100% (spleen); 70–93% (blood) | >95% | Most sensitive; kDNA PCR; used for treatment monitoring and HIV-VL |
| CBC/chemistry | — | — | Pancytopenia + ↑IgG + ↓albumin + ↑ESR supports diagnosis; not diagnostic alone |

**Treatment:**

| Drug | Dose/Route | Setting | Notes |
|:---|:---|:---|:---|
| Liposomal amphotericin B (L-AmB, AmBisome) | Single 10 mg/kg IV; or 3–5 mg/kg × 3–5 doses | WHO drug of choice globally | Extremely high cure rate (>95% in India); favourable safety profile; lipid formulation targets macrophage-rich tissues; expensive; refrigeration required |
| Miltefosine (hexadecylphosphocholine) | 2.5 mg/kg/day orally × 28 days | India, East Africa, Brazil | First effective oral treatment; teratogenic (mandatory contraception); emerging resistance in India (PKDL reservoir); 94% cure rate (naïve patients) |
| Conventional amphotericin B (deoxycholate) | 1 mg/kg IV every other day × 30 days | India, resource-limited | Effective but nephrotoxic, hypokalaemia, infusion reactions; displaced by L-AmB |
| Antimonials (SSG, meglumine antimoniate) | 20 mg/kg/day IM × 28–30 days | East Africa (SSG); Latin America (Glucantime) | High clinical resistance in Bihar, India (>60%); still effective in East Africa; pain at injection site; cardiac toxicity (QT prolongation); pancreatitis |
| Paromomycin | 11 mg/kg/day IM × 21 days | India (combination) | Used in combination with SSG in East Africa (SSG+PM); nephrotoxicity, ototoxicity; oral form not effective for VL |
| Combination therapy (e.g., L-AmB + miltefosine) | Varied | India — visceral elimination programme | Reduces treatment duration and resistance pressure; used in elimination campaigns |
| HIV-VL | L-AmB preferred for treatment; secondary prophylaxis required | Complex; high relapse rate | Anti-retroviral therapy + anti-leishmanial; CD4 determines relapse risk |

[^kaye-2011-leishmania]: Kaye P, Scott P. Leishmaniasis: complexity at the host-pathogen interface. Nat Rev Microbiol. 2011;9(8):604–15.
[^chappuis-2007-vl-review]: Chappuis F, et al. Visceral leishmaniasis: what are the needs for diagnosis, treatment and control? Nat Rev Microbiol. 2007;5(11):873–82.
[^mandell-principles]: Bennett JE, Dolin R, Blaser MJ. Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases. 9th ed. Elsevier; 2020.
[^murray-microbiology]: Murray PR, Rosenthal KS, Pfaller MA. Medical Microbiology. 9th ed. Elsevier; 2021.

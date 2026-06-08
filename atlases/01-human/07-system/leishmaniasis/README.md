---
schema: human-scale-entry/v1
id: leishmaniasis
name: Leishmaniasis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Leishmaniasis (Leishmania spp.; sand fly vector) causes cutaneous (CL), mucocutaneous (MCL), and visceral (VL/kala-azar) disease; IL-12/IFN-γ/iNOS axis controls Leishmania in macrophages; liposomal amphotericin B (L-AmB) is first-line for VL; miltefosine is the only oral agent."
aliases: ["kala-azar", "visceral leishmaniasis", "cutaneous leishmaniasis", "mucocutaneous leishmaniasis", "VL", "CL", "MCL", "PKDL", "Leishmania", "black fever", "dumdum fever"]
sources:
  - id: scott-2016-leishmaniasis-immunity
    type: peer-reviewed
    cite: "Scott P, Novais FO. Cutaneous leishmaniasis: immune responses in protection and pathogenesis. Nat Rev Immunol. 2016;16(9):581-592."
    doi: "10.1038/nri.2016.72"
    pmid: "27424773"
    url: "https://doi.org/10.1038/nri.2016.72"
    accessed: "2026-06-08"
  - id: who-2022-leishmaniasis-guideline
    type: clinical-guideline
    cite: "World Health Organization. Leishmaniasis. WHO Fact Sheet. Geneva: WHO; 2023."
    url: "https://www.who.int/news-room/fact-sheets/detail/leishmaniasis"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "TLR4-MyD88 signalling on macrophages initiates anti-Leishmania innate response: LPG → TLR4 → NF-κB → TNF-α + IL-12; however, L. donovani subverts TLR2 to suppress IL-12 production and promote parasite survival; TLR4-deficient mice are more susceptible to visceral leishmaniasis."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "IL-12 is the pivotal cytokine determining resistance vs. susceptibility to Leishmania: Th1 response (IL-12 → IFN-γ → iNOS → NO) eliminates intracellular parasites; IL-12 deficiency (MSMD) → disseminated cutaneous Leishmania; IL-12 genetic polymorphisms influence disease severity."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "HIV-AIDS reactivates visceral leishmaniasis in co-endemic regions: CD4+ depletion → Leishmania escapes macrophage control → disseminated VL; HIV-VL co-infection is a leading opportunistic parasitosis in Mediterranean Europe, East Africa, and the Indian subcontinent."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: damages
    note: "Visceral leishmaniasis causes severe ACD: chronic Leishmania infection → IL-6 + IFN-γ + TNF-α → hepcidin elevation → profound hypoferraemia; VL anemia is compounded by direct parasite infiltration of bone marrow, hypersplenism, and haemolysis; L-AmB treatment resolves ACD."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "IFN-γ from Th1 T cells and NK cells is the key anti-Leishmania effector: IFN-γ → iNOS → nitric oxide → kills intracellular Leishmania in macrophages; IFNGR deficiency (MSMD) → VL; IFN-γ also upregulates MHC-II on macrophages for better T cell priming."
---

# Leishmaniasis

## Overview

Leishmaniasis is a vector-borne protozoan disease caused by over 20 species of *Leishmania*, transmitted by the bite of female phlebotomine sand flies (*Phlebotomus* in Old World; *Lutzomyia* in New World). With 700,000–1,000,000 new cases annually and 26,000–65,000 deaths, leishmaniasis ranks second among fatal parasitic diseases after malaria. Disease manifests across a clinical spectrum — cutaneous (CL), mucocutaneous (MCL), and visceral (VL/kala-azar) — determined by *Leishmania* species, host immune genetics, and geographic setting. The IL-12/IFN-γ/iNOS Th1 axis is the critical host determinant of resistance versus progressive disease.

Leishmaniasis is a neglected tropical disease (NTD) affecting primarily impoverished populations in 88 countries. It is intimately linked to poverty, malnutrition, deforestation, and HIV co-infection. The WHO 2030 NTD Roadmap targets elimination of VL as a public health problem in South Asia and East Africa.

## Structure

### Parasite biology

*Leishmania* is a kinetoplastid protozoan with a two-stage lifecycle:

- **Promastigote** (extracellular, in sand fly): Motile, flagellated form; resides in sand fly midgut; inoculated into skin during blood meal
- **Amastigote** (intracellular, in mammalian host): Non-flagellated, oval; survives within acidic phagolysosomes (pH 4.5–5.5) of macrophages, dendritic cells, and neutrophils

Key surface virulence factors:
- **Lipophosphoglycan (LPG)**: Abundant promastigote surface glycolipid; inhibits phagosome maturation via PI3K blockade; TLR4 and TLR2 ligand
- **gp63 (leishmanolysin)**: Zinc metalloprotease; cleaves complement C3b → C3bi → CR3-mediated phagocytosis without oxidative burst activation; cleaves host proteins that trigger innate alarms
- **A2 protein**: Visceral-tropic survival factor; promotes amastigote tolerance of acidic lysosomes; absent in dermatotropic species

### Clinical forms

| Form | Species | Vector | Distribution |
|------|---------|--------|--------------|
| Cutaneous (CL) | *L. major*, *L. tropica*, *L. aethiopica* | *Phlebotomus* | Middle East, Central Asia, Africa |
| New World CL | *L. mexicana*, *L. braziliensis* | *Lutzomyia* | Latin America |
| Mucocutaneous (MCL) | *L. braziliensis* | *Lutzomyia* | South America |
| Visceral (VL/kala-azar) | *L. donovani*, *L. infantum* | *Phlebotomus* | South Asia, East Africa, Mediterranean |

## Function

### Macrophage subversion

*Leishmania* exploits macrophages as its primary intracellular niche:

1. **Entry**: Promastigotes bind CR3, FcγR, and mannose receptor → phagocytosis without activation of the oxidative burst (gp63 suppresses PKC signaling)
2. **Phagosome arrest**: LPG inserts into phagosome membrane → inhibits PI3K and Ca²⁺ signaling → delays phagolysosome fusion; amastigotes later adapt to and require the acidic environment for survival
3. **IL-12 suppression**: *L. donovani* triggers TLR2 ligation → MAPK/ERK activation → IL-12 p70 suppression; simultaneously activates STAT3 → IL-10 upregulation → regulatory/Th2 skew
4. **Antigen presentation sabotage**: Downregulation of MHC-II and CD80/CD86 on macrophages → impaired CD4+ T cell priming

### Th1 vs. Th2 immunity paradigm

The murine model (*L. major* in BALB/c vs. C57BL/6 mice) established the Th1/Th2 paradigm for infection immunity:

- **Th1 (resistance)**: IL-12 from DCs/macrophages → IFN-γ from NK cells and CD4+ T cells → iNOS induction → nitric oxide (NO) → kills intracellular amastigotes; IFN-γ also activates macrophage oxidative burst
- **Th2 (susceptibility)**: IL-4/IL-13 → alternative macrophage activation (arginase-1 upregulation vs. iNOS) → permissive intracellular environment; IL-10 suppresses IL-12 and IFN-γ (key driver of VL chronicity)
- **Regulatory axis**: Foxp3+ Tregs and IL-10-producing CD4+ T cells maintain parasite tolerance and PKDL

## Pathology

### Visceral leishmaniasis (kala-azar)

*L. donovani* and *L. infantum* disseminate from skin to liver, spleen, and bone marrow:

- **Hepatosplenomegaly**: Massive splenomegaly from reticuloendothelial hyperplasia and immune cell infiltration; spleen may reach the pelvis; Dunbar's sign (spleen extending to right iliac fossa) in severe cases
- **Pancytopenia**: Bone marrow infiltration by parasitized macrophages + hypersplenism → normocytic normochromic anemia, leukopenia, thrombocytopenia
- **Anemia of chronic disease**: IL-6 + TNF-α + IFN-γ → hepcidin induction → iron sequestration from erythroid precursors; compounded by haemolysis, BM suppression, and hypersplenism
- **Hypoalbuminaemia and edema**: Hepatic synthetic failure + severe protein-energy malnutrition → anasarca in terminal cases
- **Hypergammaglobulinaemia**: Polyclonal B cell activation → high IgG (may reach 50–60 g/L); non-protective antibodies (parasite survives despite high antibody titres); total protein elevated, albumin:globulin ratio inverted
- **PKDL**: Post-kala-azar dermal leishmaniasis — macular or nodular rash appearing 6 months to 3 years after VL treatment; dermal parasites serve as an anthroponotic reservoir; 5–50% of treated VL in South Asia; treated with miltefosine 12 weeks

### Mucocutaneous leishmaniasis

*L. braziliensis*: Metastatic spread from primary CL to nasopharyngeal mucosa (months to years later) → destructive granulomatous inflammation driven by paradoxically hyperactive Th1 response (high IFN-γ + TNF-α); disfiguring destruction of nose (tapir nose), lips, and palate; treated with pentavalent antimonials + liposomal AmB; miltefosine

### Diagnosis

- **rK39 rapid immunochromatographic test (ICT)**: Field-deployable serological test for VL; sensitivity ~97%, specificity ~97% in South Asia; less reliable in East Africa and HIV co-infection
- **Splenic aspirate culture**: Gold standard for VL diagnosis (sensitivity ~98%) but carries bleeding risk; bone marrow aspirate safer alternative (sensitivity ~70%)
- **PCR**: High sensitivity on peripheral blood (VL) and tissue biopsies (CL); useful in HIV co-infection where serology is unreliable
- **Skin slit smear or punch biopsy**: CL/PKDL diagnosis; Giemsa stain reveals amastigotes within macrophages; Leishman-Donovan bodies

### Treatment

| Disease | First-line | Alternative |
|---------|-----------|-------------|
| Visceral (South Asia) | Liposomal amphotericin B (L-AmB) single 10 mg/kg dose | Miltefosine 28 days (oral) |
| Visceral (East Africa) | L-AmB + miltefosine combination | SSG + paromomycin IM |
| Cutaneous | Meglumine antimoniate or SSG (intralesional/IM) | Miltefosine, fluconazole |
| Mucocutaneous | Pentavalent antimonials IM ± L-AmB | Miltefosine |
| PKDL | Miltefosine 12 weeks | SSG prolonged |

**Liposomal amphotericin B (L-AmB)**: Acts by binding ergosterol in *Leishmania* cell membrane → ion channel formation → osmotic lysis; single-dose 10 mg/kg IV achieves >95% cure in India; dramatically reduces treatment burden vs. 28-day regimens

**Miltefosine** (hexadecylphosphocholine): The only approved oral antileishmanial agent; mechanism involves disruption of *Leishmania* phospholipid metabolism and mitochondrial function; 28-day oral course; teratogenic (contraindicated in pregnancy, requires contraception); resistance emerging in South Asia due to uptake transporter mutations

**Pentavalent antimonials** (sodium stibogluconate/SSG, meglumine antimoniate): Prodrug activated to Sb(III) by *Leishmania* → inhibits trypanothione reductase; widespread SSG resistance in Bihar, India (>60% primary failure) has shifted first-line therapy to L-AmB in that region

### HIV co-infection

HIV-VL co-infection: CD4+ depletion → loss of IFN-γ production → *Leishmania* escapes macrophage control → disseminated VL with atypical organ involvement (GI tract, pleura, lungs). High relapse rates (>50%) post-treatment. ART partially restores Th1 immunity but rarely cures. Secondary prophylaxis with L-AmB monthly recommended while CD4 count <200 cells/μL.

## Connections

**→ [TLR4](../../../03-molecular/tlr4/)**: TLR4-MyD88 signalling on macrophages initiates anti-Leishmania innate response: LPG → TLR4 → NF-κB → TNF-α + IL-12; however, L. donovani subverts TLR2 to suppress IL-12 production and promote parasite survival; TLR4-deficient mice are more susceptible to visceral leishmaniasis.

**→ [IL-12](../../../03-molecular/il-12/)**: IL-12 is the pivotal cytokine determining resistance vs. susceptibility to Leishmania: Th1 response (IL-12 → IFN-γ → iNOS → NO) eliminates intracellular parasites; IL-12 deficiency (MSMD) → disseminated cutaneous Leishmania; IL-12 genetic polymorphisms influence disease severity.

**→ [HIV/AIDS](../hiv-aids/)**: HIV-AIDS reactivates visceral leishmaniasis in co-endemic regions: CD4+ depletion → Leishmania escapes macrophage control → disseminated VL; HIV-VL co-infection is a leading opportunistic parasitosis in Mediterranean Europe, East Africa, and the Indian subcontinent.

**→ [Anemia of Chronic Disease](../anemia-of-chronic-disease/)**: Visceral leishmaniasis causes severe ACD: chronic Leishmania infection → IL-6 + IFN-γ + TNF-α → hepcidin elevation → profound hypoferraemia; VL anemia is compounded by direct parasite infiltration of bone marrow, hypersplenism, and haemolysis; L-AmB treatment resolves ACD.

**→ [IFN-γ](../../../03-molecular/ifn-gamma/)**: IFN-γ from Th1 T cells and NK cells is the key anti-Leishmania effector: IFN-γ → iNOS → nitric oxide → kills intracellular Leishmania in macrophages; IFNGR deficiency (MSMD) → VL; IFN-γ also upregulates MHC-II on macrophages for better T cell priming.

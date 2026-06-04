---
schema: pathogen-entry/v1
id: coxsackievirus-b
name: Coxsackievirus B
atlas: 02-pathogen
scale: 01-viruses
status: draft
last_reviewed: 2026-06-03
summary: "Non-enveloped +ssRNA enterovirus (Picornaviridae) with six serotypes (B1–B6). The leading infectious cause of acute myocarditis and a major antecedent of dilated cardiomyopathy. Replicates cytolytically in cardiomyocytes via the coxsackievirus and adenovirus receptor (CAR); protease 2A cleaves dystrophin, initiating sarcolemmal disruption."
aliases: ["CVB", "Coxsackie B virus", "enterovirus B"]
sources:
  - id: cooper-2009-myocarditis-nejm
    type: peer-reviewed
    cite: "Cooper LT Jr. Myocarditis. N Engl J Med. 2009;360(15):1526-38."
    doi: "10.1056/NEJMra0800028"
    pmid: "19357408"
    url: "https://doi.org/10.1056/NEJMra0800028"
  - id: kindermann-2012-myocarditis-circulation
    type: peer-reviewed
    cite: "Kindermann I, Barth C, Mahfoud F, et al. Update on myocarditis. J Am Coll Cardiol. 2012;59(9):779-92."
    doi: "10.1016/j.jacc.2011.09.074"
    pmid: "22361396"
    url: "https://doi.org/10.1016/j.jacc.2011.09.074"
  - id: rose-2016-inflammatory-cardiomyopathy-nejm
    type: peer-reviewed
    cite: "Rose NR. Viral myocarditis. Curr Opin Rheumatol. 2016;28(4):383-9."
    doi: "10.1097/BOR.0000000000000303"
    pmid: "27166925"
    url: "https://doi.org/10.1097/BOR.0000000000000303"
  - id: ncbi-taxon-cvb
    type: database
    cite: "NCBI Taxonomy — Enterovirus B, species; Coxsackievirus B1-B6, serotypes."
    url: "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=138948"
    accessed: "2026-06-03"
  - id: yang-2009-dystrophin-cleavage
    type: peer-reviewed
    cite: "Yang D, Itagaki M, Buja LM, Garg NJ. Coxsackievirus B3 replication, apoptosis, and persistence in the heart. Cell Microbiol. 2009;11(11):1658-71."
    doi: "10.1111/j.1462-5822.2009.01359.x"
    pmid: "19575749"
    url: "https://doi.org/10.1111/j.1462-5822.2009.01359.x"
cross_links:
  - target: 01-human/04-cellular/cardiomyocyte
    relation: infects
    note: "CVB3/B5 enter cardiomyocytes via CAR (coxsackievirus-adenovirus receptor) and CD55; cytolytic replication destroys the cell."
  - target: 01-human/05-tissue/myocardium
    relation: damages
    note: "Cardiomyocyte lysis, inflammatory infiltrate, and immune-mediated injury produce myocarditis and subsequent fibrosis."
---

# Coxsackievirus B

## Overview

Coxsackievirus B (CVB) is a member of the genus *Enterovirus*, family *Picornaviridae*. It is a **non-enveloped, positive-sense single-stranded RNA (+ssRNA) virus** approximately 30 nm in diameter, comprising six serotypes (B1 through B6). CVB is transmitted via the fecal-oral and respiratory routes, replicates in the gastrointestinal tract, and in a subset of infections spreads hematogenously to the heart, pancreas, and central nervous system [^cooper-2009-myocarditis-nejm].

Cardiac disease is the most clinically significant consequence of CVB infection. It is the **leading infectious cause of acute myocarditis** in the developed world, responsible for an estimated 20–40% of cases of lymphocytic myocarditis in biopsy series [^kindermann-2012-myocarditis-circulation]. Approximately 30% of patients with severe CVB myocarditis progress to dilated cardiomyopathy (DCM), making CVB a quantitatively important antecedent of heart failure.

## Structure

CVB shares the canonical picornavirus icosahedral capsid architecture:

| Feature | Detail |
|:---|:---|
| **Capsid symmetry** | T=1 icosahedral, 60 protomers |
| **Capsid proteins** | VP1, VP2, VP3 (external), VP4 (internal, stabilizing) |
| **Genome** | ~7.4 kb +ssRNA; single open reading frame flanked by 5' and 3' UTRs; VPg protein covalently attached to 5' end |
| **Receptor** | CAR (Coxsackievirus and Adenovirus Receptor; F11R / JAM-A co-receptor facilitates entry); CD55 (decay-accelerating factor) acts as attachment receptor |
| **Diameter** | ~28–30 nm |
| **Stability** | Stable at low pH (important for gut transit); thermolabile above 50°C |

The canyon on the surface of VP1 accommodates receptor binding. Antivirals targeting this canyon (e.g., pleconaril, which obstructs receptor binding) have been studied but not yet approved for routine use.

## Mechanism of Harm

### Cytolytic Replication in Cardiomyocytes

CVB enters cardiomyocytes via **CAR**, which is concentrated at the intercalated discs — the same junction structures that mediate electrical coupling between cells [^cooper-2009-myocarditis-nejm]. This tropism for intercalated discs facilitates spread of infection across the myocardial syncytium.

Intracellular replication follows the picornavirus program:

1. **Uncoating** — the positive-sense genome is released directly into the cytoplasm.
2. **Translation** — the 5' IRES drives cap-independent translation of a single polyprotein that is auto-cleaved by the viral proteases 2A^pro^ and 3C^pro^ into structural (VP1–4) and non-structural (2A, 2B, 2C, 3A, 3B/VPg, 3C, 3D/RdRp) proteins.
3. **Replication** — RNA-dependent RNA polymerase (3D^pol^) synthesizes a negative-sense intermediate, then multiple positive-sense copies, in membrane-associated replication complexes.
4. **Cytolysis** — progeny virions accumulate until lytic release destroys the cell.

### Protease 2A Cleavage of Dystrophin

A cardinal mechanism of CVB cardiac pathology beyond simple cytolysis: the viral protease **2A^pro^ cleaves human dystrophin** at the hinge-3 domain [^yang-2009-dystrophin-cleavage]. Dystrophin is the mechanical linker between the intracellular cytoskeleton (F-actin) and the sarcolemmal dystrophin-associated glycoprotein complex (DGC), which is essential for sarcolemmal integrity during contraction. Proteolytic cleavage of dystrophin:

- Disrupts the cytoskeleton-membrane link
- Increases sarcolemmal permeability to Ca²⁺ and other ions
- Initiates a necrotic cascade independent of direct viral cytolysis
- Creates a phenotype mechanistically similar to **Duchenne muscular dystrophy** at the cell scale — explaining why DCM following CVB myocarditis can persist long after viral clearance

### Immune-Mediated Injury

Acute lytic infection triggers innate immune responses (interferon, NK cells, macrophages). In the subsequent adaptive phase, **CD8⁺ cytotoxic T lymphocytes** target virus-infected cardiomyocytes. However, molecular mimicry between CVB capsid proteins (particularly VP1) and cardiac myosin heavy chain (MHC-α, MHC-β) can generate **autoreactive T cells and antibodies** that continue to damage the myocardium after viral clearance [^rose-2016-inflammatory-cardiomyopathy-nejm]. This immune-mediated component explains why myocarditis can persist and worsen in the convalescent phase.

## Cardiac Pathology

| Phase | Mechanism | Tissue signature |
|:---|:---|:---|
| **Acute (days 1–14)** | Direct cytolysis, innate inflammation | Cardiomyocyte necrosis, neutrophil/macrophage infiltrate, edema |
| **Subacute (weeks 2–8)** | Adaptive immune cytotoxicity, immune complex deposition | Lymphocytic infiltrate (Dallas criteria: myocarditis), ongoing myocyte death |
| **Chronic / healed** | Scar formation, or ongoing autoimmune activation | Interstitial fibrosis, ventricular remodeling, chamber dilation |

Approximately 30% of patients with symptomatic CVB myocarditis develop **dilated cardiomyopathy** with reduced ejection fraction, meeting criteria for HFrEF and often requiring long-term guideline-directed medical therapy (beta-blockers, ACE inhibitors/ARBs, MRAs, SGLT2 inhibitors) [^kindermann-2012-myocarditis-circulation].

## Immune Signature

- **Innate:** IFN-α/β (type I interferons) restrict early replication; RIG-I/MDA5 are the primary RNA sensors.
- **Adaptive:** CD4⁺ Th1 cells support cytotoxic CD8⁺ responses; CD8⁺ T cells are the primary effectors against infected cardiomyocytes.
- **Autoimmune:** Anti-cardiac myosin antibodies (detectable in 30–50% of DCM patients post-myocarditis); autoreactive T cells; these can be pathogenic in the post-viral phase.
- **Regulatory failure:** TGF-β, IL-10 regulatory responses that normally limit myocardial inflammation are often insufficient in patients who progress to DCM.

## Connections

- **Infects** → [Cardiomyocyte](../../../01-human/04-cellular/cardiomyocyte/README.md): CVB enters cardiomyocytes via CAR at intercalated discs; cytolytic replication and 2A^pro^-mediated dystrophin cleavage destroy the cell.
- **Damages** → [Myocardium](../../../01-human/05-tissue/myocardium/README.md): Acute myocarditis (lymphocytic infiltration, necrosis) followed by fibrotic remodeling and, in ~30% of severe cases, dilated cardiomyopathy.
- **Indirectly affects** → [Heart](../../../01-human/06-organ/heart/README.md): Reduced contractility, chamber dilation, arrhythmia risk, and heart failure phenotype at the organ scale.
- **Medicine Atlas (planned):** Immunosuppression (corticosteroids, azathioprine) in biopsy-proven myocarditis; antiviral research (pleconaril, interferon-β); guideline-directed medical therapy for post-myocarditis DCM.

## Open Questions

- Why do some CVB-infected patients clear the virus without lasting damage while others progress to DCM? Host genetic factors (HLA type, innate immune gene variants), viral strain, and initial viral load all likely contribute, but the predictive model is incomplete.
- Can immune-tolerizing strategies (checkpoint inhibitors, regulatory T-cell augmentation) interrupt the autoimmune phase and prevent DCM progression?
- Does persistent viral RNA (rather than replicating virus) drive chronic myocarditis in some patients?

## See Also

- [Cardiomyocyte entry](../../../01-human/04-cellular/cardiomyocyte/README.md)
- [Myocardium entry](../../../01-human/05-tissue/myocardium/README.md)
- [Heart entry](../../../01-human/06-organ/heart/README.md)

[^cooper-2009-myocarditis-nejm]: Cooper LT Jr. Myocarditis. *N Engl J Med.* 2009;360(15):1526-38. [doi:10.1056/NEJMra0800028](https://doi.org/10.1056/NEJMra0800028) · [PubMed 19357408](https://pubmed.ncbi.nlm.nih.gov/19357408/)
[^kindermann-2012-myocarditis-circulation]: Kindermann I, Barth C, Mahfoud F, et al. Update on myocarditis. *J Am Coll Cardiol.* 2012;59(9):779-92. [doi:10.1016/j.jacc.2011.09.074](https://doi.org/10.1016/j.jacc.2011.09.074) · [PubMed 22361396](https://pubmed.ncbi.nlm.nih.gov/22361396/)
[^rose-2016-inflammatory-cardiomyopathy-nejm]: Rose NR. Viral myocarditis. *Curr Opin Rheumatol.* 2016;28(4):383-9. [doi:10.1097/BOR.0000000000000303](https://doi.org/10.1097/BOR.0000000000000303) · [PubMed 27166925](https://pubmed.ncbi.nlm.nih.gov/27166925/)
[^yang-2009-dystrophin-cleavage]: Yang D, Itagaki M, Buja LM, Garg NJ. Coxsackievirus B3 replication, apoptosis, and persistence in the heart. *Cell Microbiol.* 2009;11(11):1658-71. [doi:10.1111/j.1462-5822.2009.01359.x](https://doi.org/10.1111/j.1462-5822.2009.01359.x) · [PubMed 19575749](https://pubmed.ncbi.nlm.nih.gov/19575749/)

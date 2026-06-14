---
schema: human-scale-entry/v1
id: pcnsl
name: Primary CNS Lymphoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "PCNSL is ABC-DLBCL confined to CNS; MYD88 L265P ~90%, CD79B ~70%; high-dose methotrexate is the treatment backbone; ibrutinib shows ~50-60% ORR in R/R disease; 5-year OS ~30-40% with HDMTX-based therapy; vitreous IL-10 >10 pg/mL is pathognomonic."
aliases: ["PCNSL", "primary CNS lymphoma", "primary central nervous system lymphoma", "CNS lymphoma", "cerebral lymphoma", "vitreoretinal lymphoma", "primary intraocular lymphoma"]
sources:
  - id: bromberg-2019-hovon105
    type: peer-reviewed
    cite: "Bromberg JE, Issa S, Bakunina K, et al. Rituximab in patients with primary CNS lymphoma (HOVON 105/ALLG NHL 24): a randomised, open-label, phase 3 intergroup study. Lancet Oncol. 2019;20(2):216-228."
    doi: "10.1016/S1470-2045(18)30747-2"
    pmid: "30528440"
    url: "https://doi.org/10.1016/S1470-2045(18)30747-2"
  - id: grommes-2017-ibrutinib-pcnsl
    type: peer-reviewed
    cite: "Grommes C, Pastore A, Palaskas N, et al. Ibrutinib unmasks critical role of Bruton tyrosine kinase in primary CNS lymphoma. Cancer Cell. 2017;31(6):833-843."
    doi: "10.1016/j.ccell.2017.04.012"
    pmid: "28552327"
    url: "https://doi.org/10.1016/j.ccell.2017.04.012"
cross_links:
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "MYD88 L265P is present in ~90% of PCNSL — the highest prevalence in any cancer outside WM; constitutive IRAK4-NF-κB signaling drives RS cell survival; ibrutinib (BTK inhibitor) crosses the blood-brain barrier and shows ORR ~50-60% in R/R PCNSL via MYD88-BTK pathway suppression."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "PCNSL tumor cells express PD-L1 driven by MYD88-NF-κB and JAK-STAT3 signaling; CNS immune privilege maintains low T-cell surveillance; nivolumab and pembrolizumab show modest activity in R/R PCNSL (ORR ~35%); PD-L1 blockade combined with HDMTX is under investigation."
  - target: 01-human/03-molecular/btk
    relation: connects-to
    note: "BTK is the downstream effector of BCR and MYD88 signaling in PCNSL; ibrutinib (BTK covalent inhibitor) achieves ~50-75% of plasma levels in CSF and shows ORR ~50-60% in R/R PCNSL; ibrutinib+MTX+rituximab (TEDDi-R) studied as frontline; zanubrutinib also CNS-penetrant."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "MYD88 L265P drives IL-6 and IL-10 autocrine in PCNSL; vitreous IL-10 >10 pg/mL and IL-10:IL-6 ratio >1 are pathognomonic for PCNSL/vitreoretinal lymphoma; IL-10 drives JAK1-STAT3 survival in tumor cells; CSF IL-10 elevation correlates with PCNSL disease burden and response."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "PCNSL is non-Hodgkin lymphoma confined to the CNS (periventricular, basal ganglia, corpus callosum) as homogeneously enhancing masses with restricted diffusion; the blood-brain barrier blocks most lymphoma drugs, making BBB-penetrant high-dose methotrexate the backbone."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "PCNSL is an aggressive B-cell lymphoma (ABC-DLBCL): CD20+ neoplastic B cells with MYD88 L265P and CD79B mutations driving NF-κB; they home to the CNS via CXCR4/CXCR5 and evade immunity by downregulating MHC — rituximab penetrates the BBB poorly, limiting anti-CD20 benefit."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "In immunosuppressed patients (HIV with CD4 <50, transplant), PCNSL is typically EBV-driven and EBER-positive — a distinct entity from the EBV-negative, MYD88-mutant immunocompetent form; restoring immunity with HAART can induce regression of EBV-associated CNS lymphoma."
  - target: 01-human/07-system/ptcl
    relation: connects-to
    note: "Primary CNS lymphoma and peripheral T-cell lymphoma are aggressive non-Hodgkin lymphomas of opposite lineage: PCNSL is a B-cell (ABC-DLBCL) tumor driven by MYD88/CD79B-NF-κB, PTCL a heterogeneous T-cell group driven by TET2/RHOA/STAT3 — different cells, different therapies."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Primary CNS lymphoma is essentially a diffuse large B-cell lymphoma (ABC type) trapped in the CNS: it shares DLBCL's CD20+ biology and MYD88/CD79B-NF-κB drivers, but immune privilege and the blood-brain barrier make it behave differently — high-dose methotrexate, not R-CHOP."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Primary CNS lymphoma has an ocular form — vitreoretinal lymphoma — that seeds the eye as painless floaters or steroid-refractory uveitis; a vitreous IL-10:IL-6 ratio >1 and MYD88 L265P clinch the diagnosis, and ~15-25% of PCNSL involves the eye, often bilaterally."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "Primary CNS lymphoma is an AIDS-defining cancer: in advanced HIV with low CD4 counts, EBV-driven B-cell lymphoma arises in the brain, so a periventricular mass in AIDS raises PCNSL versus toxoplasmosis—distinguished by EBV PCR of CSF and thallium imaging."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Whole-brain photon radiotherapy once anchored PCNSL treatment but is now used cautiously: the tumor is exquisitely radiosensitive, yet WBRT causes severe delayed neurocognitive decline, so high-dose methotrexate is preferred and radiation reserved or dose-reduced."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "PCNSL grows in the unique immune environment policed by microglia: this EBV-driven B-cell lymphoma proliferates around vessels in brain parenchyma, and reactive microglia form the perivascular cuffs and inflammatory backdrop characteristic of its histology."
  - target: 01-human/07-system/glioblastoma
    relation: connects-to
    note: "PCNSL and glioblastoma are the two great intra-axial brain masses that imaging can confuse: both enhance and infiltrate, but PCNSL is a B-cell lymphoma exquisitely steroid- and methotrexate-sensitive, while GBM needs surgery and chemoradiation—biopsy is decisive."
  - target: 01-human/07-system/meningioma
    relation: connects-to
    note: "PCNSL and meningioma are both intracranial tumors but opposite: PCNSL is an intra-axial B-cell lymphoma treated with methotrexate, while meningioma is an extra-axial dural tumor cured by resection—MRI location usually separates the medical from the surgical disease."
  - target: 01-human/07-system/mantle-cell-lymphoma
    relation: connects-to
    note: "PCNSL and mantle cell lymphoma can both involve the CNS: primary CNS lymphoma is a brain-confined DLBCL, while aggressive systemic lymphomas like MCL can spread secondarily to the leptomeninges—so CNS lymphoma may be primary or secondary."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "PCNSL is largely a disease of immune failure: it is far commoner in HIV/AIDS and transplant immunosuppression, where unchecked EBV transforms B cells in the brain—so immune status drives both its incidence and (with immune restoration) sometimes its regression."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "PCNSL arises from a late germinal-center B cell trapped in the CNS: it is a post-germinal-center DLBCL expressing BCL6/IRF4 that, oddly, homes to and grows within the immune-privileged brain—so it shares lymphoma-node biology yet behaves as a CNS tumor."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "MYC and BCL2 co-expression marks aggressive PCNSL: like systemic DLBCL, double-expressor PCNSL carries a worse prognosis, but the blood-brain barrier limits which drugs reach it—so high-dose methotrexate, not standard R-CHOP, anchors treatment."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "PCNSL is a CD20-positive B-cell lymphoma treated through that target: high-dose methotrexate crosses the blood-brain barrier and is combined with the anti-CD20 antibody rituximab, exploiting the same B-cell marker used against systemic lymphomas."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Primary CNS lymphoma is a lymphoma confined to the nervous system: it grows in the brain, spinal cord, eyes and meninges without nodal disease, so it presents with focal deficits and cognitive change—and its CNS sanctuary demands brain-penetrant therapy."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "PCNSL is a striking exception within the lymphatic system: though a B-cell lymphoma, it arises and stays in the immune-privileged CNS rather than lymph nodes, so staging is typically negative outside the brain and eye—unlike systemic DLBCL."
---

# Primary CNS Lymphoma

## Overview

**Primary CNS lymphoma (PCNSL)** is a rare extranodal non-Hodgkin lymphoma confined at diagnosis to the **central nervous system** (brain parenchyma, spinal cord, leptomeninges, cranial nerves, eyes) without systemic involvement. PCNSL is almost universally of **ABC-DLBCL (activated B-cell-like diffuse large B-cell lymphoma) histology**, with near-universal expression of **MYD88 L265P** (~90%) and frequent **CD79B mutations** (~70%) — creating a distinct genomic profile that explains CNS tropism and BTK inhibitor sensitivity [^grommes-2017-ibrutinib-pcnsl]. The **blood-brain barrier (BBB)** presents a fundamental challenge to drug delivery: most effective systemic lymphoma therapies (rituximab, cyclophosphamide, doxorubicin) achieve inadequate CNS penetration, making **high-dose methotrexate (HDMTX)** — which crosses the BBB via organic anion transporters — the irreplaceable backbone of PCNSL treatment. Despite high initial response rates to HDMTX-based therapy (~75-80% CR), PCNSL has a high relapse rate and poor long-term outcomes (5-year OS ~30-40%), underscoring the need for effective consolidation strategies and novel agents [^bromberg-2019-hovon105].

**Epidemiology:**
- Incidence: ~1,500 cases/year USA; ~7,000 globally; 1-5% of all primary brain tumors
- Median age at diagnosis: ~65 years (immunocompetent); younger in HIV-associated (median ~35 years)
- Risk factors: Immunosuppression (HIV, solid organ transplant, autoimmune therapy); age >60; male predominance (M:F ~1.3:1)
- HIV-associated PCNSL: EBV-driven; CD4 count usually <50/μL; dramatically reduced in HAART era
- Immunocompetent PCNSL: EBV-negative; MYD88 L265P ~90%; genetically distinct

## Structure

### Molecular and genomic architecture

**Core driver mutations:**
- **MYD88 L265P (~90%):** Constitutive IRAK4-NF-κB + JAK1-STAT3 → lymphocyte survival; highest MYD88 L265P prevalence of any cancer type
- **CD79B Y196H/N/S/D (~70%):** BCR co-receptor mutations → chronic active BCR signaling → BTK activation → NF-κB; CD79B Y196 is the primary phosphorylation site for SYK → Y196 mutation prevents ITAM-dependent SYK downregulation → persistent BCR signal
- **MYD88+CD79B co-mutation (~65% PCNSL):** Near-universal co-occurrence drives synergistic NF-κB from two converging pathways; predicts BTK inhibitor sensitivity; together called the "double-mutant" PCNSL
- **CARD11 mutations (~15%):** Constitutive NF-κB via CBM complex
- **CDKN2A deletion (~50%):** p16/p14 loss; p53 pathway impairment
- **HLA class I and II loss (~40%):** Immune evasion in CNS immune-privileged site
- **MYC rearrangement/amplification (~15%):** Aggressive subset; double-hit PCNSL (MYD88+MYC) has very poor prognosis

**Immune privilege mechanism:**
PCNSL exploits CNS immune privilege: (1) BBB restricts lymphocyte trafficking — fewer patrolling cytotoxic T cells; (2) Microglia (CNS-resident macrophages) are anti-inflammatory; (3) PCNSL cells downregulate MHC class I/II → evade CTL killing; (4) PD-L1 overexpression (MYD88-NF-κB → PD-L1 transcription) further suppresses T-cell function; the CNS thus provides a sanctuary from immune surveillance analogous to the testicular "immune privilege" that explains primary testicular DLBCL sharing the same MYD88+CD79B profile.

**Vitreoretinal lymphoma (VRL):**
~15-25% of PCNSL involves the vitreous/retina simultaneously (primary intraocular lymphoma); VRL is usually the ocular manifestation of the same PCNSL clone; shares MYD88 L265P (~90%), CD79B mutations (~60%); vitreous biopsy with cytology + IL-10 measurement is diagnostic; often presents as "uveitis" and is misdiagnosed; PCNSL can follow isolated VRL by months to years.

### Histopathology

**Morphology:** Large B cells with prominent nucleoli; perivascular (angiocentric) growth pattern (tumor cells cuffing blood vessels); necrosis variable; reactive T cells sparse (immune-depleted microenvironment); prominent gliosis.

**Immunophenotype:** CD20+, CD19+, CD10−, BCL6±, IRF4/MUM1+, PAX5+, BOB1+, OCT2+ (ABC-DLBCL pattern); Ki-67 >90% common; EBV EBER negative (immunocompetent); EBER+ only in HIV-associated.

**Radiologic features (MRI):**
- Solitary or multiple lesions (75% in brain parenchyma); hemispheres most common; periventricular white matter; basal ganglia; corpus callosum
- Isointense T1, homogeneous gadolinium enhancement (vivid enhancement due to BBB disruption); no ring enhancement (unlike glioblastoma/abscess)
- Restricted diffusion on DWI (hypercellular tumor)
- Spontaneous regression on steroids (lympholytic effect) → "ghost tumor" phenomenon; biopsy before steroids if possible

## Function

### Normal BBB and CNS lymphocyte trafficking

Lymphocytes normally cross the BBB via VCAM-1/ICAM-1 and VLA-4/LFA-1 interactions at postcapillary venules → patrolling within the CNS parenchyma; in PCNSL, neoplastic B cells with high CXCR4 and CXCR5 expression home to CXCL12-rich (CNS endothelium) and CXCL13-rich (follicular microenvironment-like niches) zones within the CNS, explaining CNS tropism; intact BBB explains why rituximab (168 kDa, poor BBB penetration) adds little benefit over HDMTX alone in the CNS.

## Pathology

### Diagnosis

**Clinical presentation:**
Cognitive decline (~70%), focal neurologic deficits (hemiparesis, aphasia, ~50%), personality change, headache, seizures (~10%); visual symptoms (floaters, blurred vision if VRL); B symptoms uncommon (not systemic lymphoma); rapid progression over weeks without treatment → herniation.

**Diagnostic workup:**
- Brain MRI with gadolinium (mandatory); whole-spine MRI if cord symptoms
- CSF analysis: cytology (lymphoma cells in ~50%), flow cytometry (CD19+CD10-), protein (elevated), glucose, VDRL; CSF cell-free DNA (cfDNA) for MYD88 L265P (sensitivity ~60-70%); IgH rearrangement by PCR
- **Vitreous/aqueous humor IL-10:** IL-10 >10 pg/mL + IL-10:IL-6 ratio >1 in VRL is highly specific (>90%); send both IL-6 and IL-10
- **Slit-lamp examination:** VRL in vitreous; subretinal infiltrates
- Brain biopsy (stereotactic): gold standard; defer until after CSF/vitreous attempts; avoid corticosteroids before biopsy (steroid-induced CR can prevent diagnosis)
- Systemic staging: PET-CT (exclude systemic involvement); testicular ultrasound in males (testis is immune-privileged site; occult testicular lymphoma can present as PCNSL); BM biopsy
- HIV testing, immunosuppression history
- Ophthalmologic evaluation (slit-lamp + fundus)

### Treatment

**Induction (fit patients):**
- **HDMTX-based regimens:** Methotrexate 3-8 g/m²  over 3-4 hours IV with leucovorin rescue + alkaline hydration; penetrates BBB via reduced folate carrier; CSF levels reach therapeutic concentrations; ORR ~75-80%
- **R-MPV (rituximab, methotrexate, procarbazine, vincristine):** Widely used; MTX 3.5 g/m² days 2, 15; rituximab IV (poor BBB penetration but may reach leptomeninges); ORR ~78% CR; HOVON 105 trial (rituximab + HDMTX vs HDMTX alone): CR 49% vs 38% (p=0.071, not significant); rituximab benefit trend but not proven [^bromberg-2019-hovon105]
- **MATRix (methotrexate, cytarabine, thiotepa, rituximab):** IELSG32 trial: CR 49% vs 23% (HDMTX alone); PFS superior; used widely in Europe
- Intrathecal MTX or cytarabine: for leptomeningeal disease; not routinely added to systemic HDMTX

**Consolidation:**
- **Autologous SCT (BEAM or thiotepa-based conditioning):** IELSG43 trial (auto-SCT vs WBRT): equivalent PFS ~2 years; auto-SCT preferred (avoids neurotoxicity of WBRT); BEAM-R: carmustine, etoposide, cytarabine, melphalan + rituximab conditioning
- **WBRT (whole-brain radiotherapy, 23.4-45 Gy):** Highly effective (ORR ~90% in recurrent) but severe neurotoxicity (white matter changes, cognitive decline, leukoencephalopathy) in >60% of patients >60 years; now reserved for young/fit patients or relapse setting
- **High-dose cytarabine consolidation:** Alternative to auto-SCT in older/frail patients
- **Maintenance rituximab:** Under investigation; limited CNS penetration argues against utility

**Relapsed/Refractory PCNSL:**
- **Ibrutinib (BTK inhibitor):** ORR ~50-60% (Phase 1/2: 15/20 patients responded, CR in 10/20); CSF penetration ~50-75% of plasma; CNS response correlates with MYD88 L265P; combinations with MTX, rituximab being studied; atrial fibrillation, bleeding risk [^grommes-2017-ibrutinib-pcnsl]
- **Zanubrutinib:** More selective BTK inhibitor; better CNS penetration; Phase 2 in R/R PCNSL ongoing
- **Pirtobrutinib (non-covalent BTK inhibitor):** Active after covalent BTK inhibitor failure; PCNSL cohort in Phase 2
- **TEDDi-R (thiotepa, etoposide, dexamethasone, dexamethasone, ibrutinib, rituximab):** Feasibility shown; high ORR (~90%) but high toxicity
- **Lenalidomide + rituximab (R²):** ORR ~35% in R/R PCNSL; immunomodulatory
- **Nivolumab/pembrolizumab:** ORR ~35% in R/R PCNSL (MYD88-driven PD-L1 upregulation); durable responses in subset
- Re-HDMTX: Active in patients relapsing >12 months after initial HDMTX

**Elderly/frail patients (age >70):**
- Reduced-dose MTX (1.5-2 g/m²) ± procarbazine/vincristine
- Ibrutinib as primary therapy or maintenance
- WBRT at reduced dose (23.4 Gy) as monotherapy in very frail patients

**HIV-associated PCNSL:**
- HAART + HDMTX-based therapy if CD4 >50 and performance status allows
- EBV-driven: HAART alone may induce regression in some (immune reconstitution)
- Prognosis significantly improved with HAART era vs pre-HAART (OS weeks → months/years)

### Prognostic scoring (IELSG score)

International Extranodal Lymphoma Study Group (IELSG) score — 5 adverse factors:
1. Age >60 years
2. ECOG PS >1
3. Elevated LDH
4. High CSF protein
5. Deep brain involvement (corpus callosum, basal ganglia, brainstem, cerebellum)

Score 0-1: 2-year OS ~80%; Score 2-3: ~48%; Score 4-5: ~15%

## Connections

- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — MYD88 L265P is present in ~90% of PCNSL — the highest prevalence in any cancer outside WM; constitutive IRAK4-NF-κB signaling drives RS cell survival; ibrutinib (BTK inhibitor) crosses the blood-brain barrier and shows ORR ~50-60% in R/R PCNSL via MYD88-BTK pathway suppression.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — PCNSL tumor cells express PD-L1 driven by MYD88-NF-κB and JAK-STAT3 signaling; CNS immune privilege maintains low T-cell surveillance; nivolumab and pembrolizumab show modest activity in R/R PCNSL (ORR ~35%); PD-L1 blockade combined with HDMTX is under investigation.
- `connects-to` → **[BTK](../../03-molecular/btk/README.md)** — BTK is the downstream effector of BCR and MYD88 signaling in PCNSL; ibrutinib (BTK covalent inhibitor) achieves ~50-75% of plasma levels in CSF and shows ORR ~50-60% in R/R PCNSL; ibrutinib+MTX+rituximab (TEDDi-R) studied as frontline; zanubrutinib also CNS-penetrant.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — MYD88 L265P drives IL-6 and IL-10 autocrine in PCNSL; vitreous IL-10 >10 pg/mL and IL-10:IL-6 ratio >1 are pathognomonic for PCNSL/vitreoretinal lymphoma; IL-10 drives JAK1-STAT3 survival in tumor cells; CSF IL-10 elevation correlates with PCNSL disease burden and response.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — PCNSL is non-Hodgkin lymphoma confined to the CNS (periventricular, basal ganglia, corpus callosum) as homogeneously enhancing masses with restricted diffusion; the blood-brain barrier blocks most lymphoma drugs, making BBB-penetrant high-dose methotrexate the backbone.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — PCNSL is an aggressive B-cell lymphoma (ABC-DLBCL): CD20+ neoplastic B cells with MYD88 L265P and CD79B mutations driving NF-κB; they home to the CNS via CXCR4/CXCR5 and evade immunity by downregulating MHC — rituximab penetrates the BBB poorly, limiting anti-CD20 benefit.
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — In immunosuppressed patients (HIV with CD4 <50, transplant), PCNSL is typically EBV-driven and EBER-positive — a distinct entity from the EBV-negative, MYD88-mutant immunocompetent form; restoring immunity with HAART can induce regression of EBV-associated CNS lymphoma.
- `connects-to` → **[Peripheral T-cell Lymphoma](../ptcl/README.md)** — Primary CNS lymphoma and peripheral T-cell lymphoma are aggressive non-Hodgkin lymphomas of opposite lineage: PCNSL is a B-cell (ABC-DLBCL) tumor driven by MYD88/CD79B-NF-κB, PTCL a heterogeneous T-cell group driven by TET2/RHOA/STAT3 — different cells, different therapies.
- `connects-to` → **[Diffuse Large B-Cell Lymphoma](../dlbcl/README.md)** — Primary CNS lymphoma is essentially a diffuse large B-cell lymphoma (ABC type) trapped in the CNS: it shares DLBCL's CD20+ biology and MYD88/CD79B-NF-κB drivers, but immune privilege and the blood-brain barrier make it behave differently — high-dose methotrexate, not R-CHOP.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Primary CNS lymphoma has an ocular form — vitreoretinal lymphoma — that seeds the eye as painless floaters or steroid-refractory uveitis; a vitreous IL-10:IL-6 ratio >1 and MYD88 L265P clinch the diagnosis, and ~15-25% of PCNSL involves the eye, often bilaterally.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — Primary CNS lymphoma is an AIDS-defining cancer: in advanced HIV with low CD4 counts, EBV-driven B-cell lymphoma arises in the brain, so a periventricular mass in AIDS raises PCNSL versus toxoplasmosis—distinguished by EBV PCR of CSF and thallium imaging.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Whole-brain photon radiotherapy once anchored PCNSL treatment but is now used cautiously: the tumor is exquisitely radiosensitive, yet WBRT causes severe delayed neurocognitive decline, so high-dose methotrexate is preferred and radiation reserved or dose-reduced.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — PCNSL grows in the unique immune environment policed by microglia: this EBV-driven B-cell lymphoma proliferates around vessels in brain parenchyma, and reactive microglia form the perivascular cuffs and inflammatory backdrop characteristic of its histology.
- `connects-to` → **[Glioblastoma](../glioblastoma/README.md)** — PCNSL and glioblastoma are the two great intra-axial brain masses that imaging can confuse: both enhance and infiltrate, but PCNSL is a B-cell lymphoma exquisitely steroid- and methotrexate-sensitive, while GBM needs surgery and chemoradiation—biopsy is decisive.
- `connects-to` → **[Meningioma](../meningioma/README.md)** — PCNSL and meningioma are both intracranial tumors but opposite: PCNSL is an intra-axial B-cell lymphoma treated with methotrexate, while meningioma is an extra-axial dural tumor cured by resection—MRI location usually separates the medical from the surgical disease.
- `connects-to` → **[Mantle Cell Lymphoma](../mantle-cell-lymphoma/README.md)** — PCNSL and mantle cell lymphoma can both involve the CNS: primary CNS lymphoma is a brain-confined DLBCL, while aggressive systemic lymphomas like MCL can spread secondarily to the leptomeninges—so CNS lymphoma may be primary or secondary.
- `connects-to` → **[Immune System](../immune-system/README.md)** — PCNSL is largely a disease of immune failure: it is far commoner in HIV/AIDS and transplant immunosuppression, where unchecked EBV transforms B cells in the brain—so immune status drives both its incidence and (with immune restoration) sometimes its regression.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — PCNSL arises from a late germinal-center B cell trapped in the CNS: it is a post-germinal-center DLBCL expressing BCL6/IRF4 that, oddly, homes to and grows within the immune-privileged brain—so it shares lymphoma-node biology yet behaves as a CNS tumor.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — MYC and BCL2 co-expression marks aggressive PCNSL: like systemic DLBCL, double-expressor PCNSL carries a worse prognosis, but the blood-brain barrier limits which drugs reach it—so high-dose methotrexate, not standard R-CHOP, anchors treatment.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — PCNSL is a CD20-positive B-cell lymphoma treated through that target: high-dose methotrexate crosses the blood-brain barrier and is combined with the anti-CD20 antibody rituximab, exploiting the same B-cell marker used against systemic lymphomas.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Primary CNS lymphoma is a lymphoma confined to the nervous system: it grows in the brain, spinal cord, eyes and meninges without nodal disease, so it presents with focal deficits and cognitive change—and its CNS sanctuary demands brain-penetrant therapy.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — PCNSL is a striking exception within the lymphatic system: though a B-cell lymphoma, it arises and stays in the immune-privileged CNS rather than lymph nodes, so staging is typically negative outside the brain and eye—unlike systemic DLBCL.

[^bromberg-2019-hovon105]: Bromberg JE, Issa S, Bakunina K, et al. Rituximab in patients with primary CNS lymphoma (HOVON 105/ALLG NHL 24): a randomised, open-label, phase 3 intergroup study. *Lancet Oncol.* 2019;20(2):216-228. [doi:10.1016/S1470-2045(18)30747-2](https://doi.org/10.1016/S1470-2045(18)30747-2) · [PubMed 30528440](https://pubmed.ncbi.nlm.nih.gov/30528440/)
[^grommes-2017-ibrutinib-pcnsl]: Grommes C, Pastore A, Palaskas N, et al. Ibrutinib unmasks critical role of Bruton tyrosine kinase in primary CNS lymphoma. *Cancer Cell.* 2017;31(6):833-843. [doi:10.1016/j.ccell.2017.04.012](https://doi.org/10.1016/j.ccell.2017.04.012) · [PubMed 28552327](https://pubmed.ncbi.nlm.nih.gov/28552327/)

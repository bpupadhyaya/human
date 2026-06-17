---
schema: human-scale-entry/v1
id: synovial-sarcoma
name: Synovial Sarcoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Synovial sarcoma is defined by SS18-SSX1/SSX2 fusion (t(X;18)) → SMARCB1 displacement from BAF → EZH2 dependency; ~800/year USA; biphasic/monophasic histology; TLE1 IHC positive; ifosfamide-based chemotherapy; tazemetostat (SARC057 ORR ~22%) and trabectedin active."
aliases: ["synovial sarcoma", "SS18-SSX sarcoma", "biphasic synovial sarcoma", "monophasic synovial sarcoma", "t(X;18) sarcoma", "TLE1-positive sarcoma", "translocation sarcoma SYT-SSX", "synovial cell sarcoma"]
sources:
  - id: kadoch-2013-ss18-ssx-baf
    type: peer-reviewed
    cite: "Kadoch C, Crabtree GR. Reversible disruption of mSWI/SNF (BAF) complexes by the SS18-SSX oncogenic fusion in synovial sarcoma. Cell. 2013;153(1):71-85."
    doi: "10.1016/j.cell.2013.02.036"
    pmid: "23540691"
    url: "https://doi.org/10.1016/j.cell.2013.02.036"
  - id: kawai-2015-trabectedin-synovial
    type: peer-reviewed
    cite: "Kawai A, Araki N, Sugiura H, et al. Trabectedin monotherapy after standard chemotherapy versus best supportive care in patients with advanced, translocation-related sarcoma: a randomised, open-label, phase 2 study. Lancet Oncol. 2015;16(4):406-416."
    doi: "10.1016/S1470-2045(15)70098-7"
    pmid: "25795407"
    url: "https://doi.org/10.1016/S1470-2045(15)70098-7"
cross_links:
  - target: 01-human/03-molecular/ss18
    relation: connects-to
    note: "SS18-SSX1/SSX2 fusion (t(X;18)(p11;q11)) is the pathognomonic alteration of synovial sarcoma (100% of cases); FISH for SS18 rearrangement or RT-PCR for SS18-SSX transcript is the diagnostic standard; SSX2 predominates in monophasic SS; SSX1 in biphasic SS."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "SS18-SSX displaces SMARCB1 from BAF → PRC2/EZH2 unrestricted → H3K27me3 at CDKN2A, KLF4, and differentiation loci; synovial sarcoma is EZH2-dependent; tazemetostat (EZH2 inhibitor, SARC057): ORR 22% in pretreated SS; FDA breakthrough therapy designation granted for SS."
  - target: 01-human/03-molecular/smarcb1
    relation: connects-to
    note: "SS18-SSX displaces SMARCB1 from canonical BAF without SMARCB1 mutation → SMARCB1 degraded → BAF destabilized → PRC2 access; SMARCB1 IHC remains intact in SS (contrast AT/RT where SMARCB1 is lost); SS18-SSX knockdown → SMARCB1 re-occupies BAF → G1 arrest; shared EZH2 dependency."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Homozygous CDKN2A deletion in ~10-15% synovial sarcoma predicts poor prognosis; EZH2/H3K27me3 epigenetically silences CDKN2A even without deletion → absent p16 → CDK4/6 hyperactivation → E2F-driven S-phase; CDK4/6 inhibitors (palbociclib) under evaluation in CDKN2A-deleted SS."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "SS18-SSX QPGY activation domain drives VEGF transcription → angiogenesis; pazopanib (VEGFR2 inhibitor, PALETTE trial: PFS HR 0.35) FDA-approved for advanced STS post-chemo including SS; VEGF overexpression correlates with tumor grade and metastatic potential in synovial sarcoma."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "SS has low TMB (~1-2 mut/Mb) and variable PD-L1 → limited single-agent ICB ORR (~10-15%); tazemetostat + pembrolizumab (Phase 1/2) under investigation; EZH2 inhibition may restore IFN-γ response; TMB-high/MSI-H SS (<5%) most likely ICB responders."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "TLE1 (most specific SS IHC marker) is a Groucho-family WNT/β-catenin co-repressor (binds TCF/LEF); SS18-SSX recruits TLE1 into the oncogenic complex; ~30% of SS show nuclear β-catenin; CTNNB1 mutations in <5%; WNT pathway modulation is part of SS epigenetic de-regulation."
  - target: 01-human/07-system/atypical-teratoid-rhabdoid-tumor
    relation: connects-to
    note: "Synovial sarcoma and AT/RT both derange the SWI/SNF (BAF) complex and depend on EZH2: SS18-SSX fusion ejects SMARCB1 from BAF (SMARCB1 stays detectable), while AT/RT deletes SMARCB1 entirely (INI1 lost on IHC) — yet both respond to the EZH2 inhibitor tazemetostat."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Synovial sarcoma is a soft-tissue sarcoma of adolescents and young adults arising near — not from — joints, typically in deep extremity soft tissue (around the knee); despite the name it is not of synovial origin, and wide resection plus radiation is standard."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lung is the dominant metastatic site in synovial sarcoma: it spreads hematogenously to the lungs even years after the primary is controlled, so long-term chest CT surveillance is essential and pulmonary metastasectomy is offered for limited disease."
  - target: 01-human/07-system/schwannomatosis
    relation: connects-to
    note: "Synovial sarcoma and schwannomatosis both subvert the SWI/SNF (BAF) chromatin-remodeling complex: synovial sarcoma's SS18-SSX fusion reprograms BAF to silence tumor-suppressors, while loss of the BAF subunit SMARCB1 drives schwannomatosis and rhabdoid tumors."
  - target: 01-human/07-system/ewing-sarcoma
    relation: connects-to
    note: "Synovial and Ewing sarcoma are fusion-driven sarcomas of young adults defined by a single translocation: SS18-SSX for synovial sarcoma, EWSR1-FLI1 for Ewing—both aberrant transcription factors that remodel the epigenome, models of fusion-oncoprotein cancer."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Synovial sarcoma is a mesenchymal tumor of fibroblast-like spindle cells despite its misleading name: it arises not from synovium but from a primitive mesenchymal cell, its monophasic form being sheets of spindle cells expressing TLE1 and SS18-SSX."
  - target: 01-human/07-system/rhabdomyosarcoma
    relation: connects-to
    note: "Synovial sarcoma and rhabdomyosarcoma are both fusion-driven soft-tissue sarcomas: synovial sarcoma's SS18-SSX fusion hijacks the SWI/SNF complex, while alveolar RMS's PAX-FOXO1 drives myogenic transcription—translocations defining distinct, aggressive sarcomas."
  - target: 01-human/07-system/mpnst
    relation: connects-to
    note: "Synovial sarcoma and MPNST are spindle-cell sarcomas that can look alike: synovial sarcoma is defined by SS18-SSX, MPNST by NF1-driven nerve-sheath origin—so SS18-SSX testing and S100/SOX10 staining separate these spindle tumors."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Synovial sarcoma is managed like other high-grade soft-tissue sarcomas with surgery plus radiotherapy: wide resection combined with photon radiation improves local control, while the SS18-SSX fusion is now also targeted by EZH2 inhibitors and cellular therapy."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 mutation can mark progression in synovial sarcoma: while the SS18-SSX fusion is the defining initiating event, secondary p53 loss appears in high-grade, dedifferentiated tumors—so the genome guardian's failure layers onto the fusion oncogene to worsen behavior."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "TERT activation helps immortalize synovial sarcoma cells: telomerase reactivation, alongside the SS18-SSX fusion that reprograms the epigenome, lets these translocation-driven sarcomas divide indefinitely—a step common to many cancers despite their distinct drivers."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Synovial sarcoma joins the broad sarcoma spectrum of Li-Fraumeni syndrome: although defined by the somatic SS18-SSX fusion rather than germline p53 loss, sarcomas like it occur excessively in p53-deficient patients—linking fusion-driven and hereditary sarcomas."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Synovial sarcoma is a leading target for engineered T-cell therapy: it expresses cancer-testis antigens (NY-ESO-1, MAGE-A4), so afami-cel/tecelra—TCR T cells the immune system is reprogrammed to deploy—became the first such therapy approved for a solid tumor."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Synovial sarcoma's cancer-testis antigens depend on antigen presentation: dendritic cells process NY-ESO-1 and MAGE-A4 onto HLA, the step that primes the T cells engineered immunotherapies exploit—and the tumor evades this by downregulating MHC."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Synovial sarcoma is a rare primary cardiac sarcoma: though usually arising in limb soft tissue, it can originate in the heart or pericardium, presenting with obstruction or effusion and a grim prognosis given difficult surgical clearance."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Synovial sarcoma is a flagship for engineered T cells: it expresses NY-ESO-1, and afamitresgene autoleucel—TCR-engineered cytotoxic T cells targeting that antigen—won FDA approval in 2024 for this sarcoma, a first for solid-tumor TCR therapy."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Synovial sarcoma is an immunologically 'cold' tumor rich in macrophages: tumor-associated macrophages dominate its sparse immune infiltrate and suppress T-cell responses, helping explain why checkpoint inhibitors disappoint while TCR-engineered T cells work."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Synovial sarcoma runs an IGF-1 autocrine loop: the tumor overexpresses IGF1R and its ligands to drive growth and survival, so IGF1R inhibition has been explored as targeted therapy in this fusion-driven sarcoma."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "Synovial sarcoma is a chromatin disease: its SS18-SSX fusion hijacks the SWI/SNF (BAF) complex—which includes ARID1A—wrenching it onto the wrong genes, so the tumor is driven by epigenetic miswiring rather than classic mutations."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Synovial sarcoma's immunotherapy is limited by regulatory T cells: it expresses the NY-ESO-1 antigen targeted by TCR-engineered T cells, but a Treg-rich, suppressive microenvironment blunts the attack and curbs durable responses."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Synovial sarcoma grows on IGF-driven mTOR signaling: autocrine IGF-1 feeds the PI3K-AKT-mTOR axis to fuel proliferation, making mTOR a studied target in a sarcoma otherwise reliant on chemotherapy and surgery."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Hypoxia stokes synovial sarcoma's aggressiveness: as the tumor outgrows its blood supply, low oxygen drives invasion and metastasis, contributing to the lung spread that threatens patients with this translocation-driven sarcoma."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Synovial sarcoma can spread to the brain: though lung is the dominant metastatic site, hematogenous spread occasionally seeds brain metastases in advanced disease, prompting imaging when neurologic symptoms appear."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Synovial sarcoma leans on AKT downstream of IGF: autocrine IGF-1 activates the PI3K-AKT-mTOR axis to drive proliferation and survival, so AKT-mTOR inhibitors are studied alongside the IGF and immune approaches in this sarcoma."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Synovial sarcoma sometimes calcifies: foci of calcium deposit within the tumor, and heavily calcified synovial sarcomas tend to carry a notably better prognosis than non-calcified ones."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Synovial sarcoma can spread to the liver: though it favors the lungs, hematogenous metastasis seeds the liver and other organs in advanced disease, marking the shift to systemic treatment."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Synovial sarcoma weaves a fibrous stroma: its spindle-cell component lays down dense collagen in the biphasic tumor, the firm fibrous tissue that, with epithelial nests, defines its histology."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy exposes synovial sarcoma's split personality: alongside the spindle cells sit true epithelial cells joined by desmosomes, sprouting microvilli into gland-like lumina over a basal lamina — the ultrastructure of its biphasic histology."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Synovial sarcoma can invade the skeleton: though it favors the lungs, late disease seeds bone and the marrow within, and tumors abutting a joint erode the neighboring bone as they grow."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Rarely synovial sarcoma is born in the kidney itself: primary renal synovial sarcoma, carrying the same SS18 fusion, is a recognized aggressive entity that masquerades as a more common kidney tumor until molecular testing reveals it."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Despite its name, synovial sarcoma weaves a fibrous tumor: its spindle cells sit in a collagen-rich stroma, often with stippled calcification, and the biphasic form adds glandular epithelium — a texture that, with the SS18 fusion, makes the diagnosis."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "The ifosfamide in its chemotherapy can fog the brain: a metabolite of this alkylator crosses into the CNS and poisons neurons, causing a reversible encephalopathy with confusion and seizures that methylene blue is used to treat."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Ifosfamide also injures the kidney's tubules: the resulting Fanconi-like syndrome wastes magnesium, phosphate, and bicarbonate into the urine, so electrolytes are monitored and replaced through synovial sarcoma treatment."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "An antibody now clinches the diagnosis: a stain against the SS18-SSX fusion protein is highly specific for synovial sarcoma, and with TLE1 it confirms the t(X;18)-driven tumor that can otherwise mimic many spindle-cell cancers."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The doxorubicin-ifosfamide regimen empties the marrow: both drugs are heavily myelosuppressive, dropping neutrophil counts so that febrile neutropenia is a recurring hazard through synovial sarcoma chemotherapy."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Treatment and tumor both thin the red cells: the anthracycline-and-alkylator chemotherapy suppresses marrow erythrocyte production, leaving an anemia and fatigue that may need transfusion across the long course of care."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "The doxorubicin-ifosfamide chemotherapy strains the heart: the anthracycline backbone for synovial sarcoma is cumulatively cardiotoxic to cardiomyocytes, so cardiac function is checked across treatment in these often-young patients."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Cure can cost fertility: synovial sarcoma strikes adolescents and young adults, and its alkylating ifosfamide and any pelvic radiation damage the gonads, so fertility preservation is discussed before treatment begins."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "It is a hypoxic, vessel-hungry tumor: synovial sarcoma stabilizes HIF and pours out VEGF to feed its growth, the angiogenic drive behind the activity of anti-VEGF tyrosine-kinase inhibitors like pazopanib against it."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "It survives by blocking its own death: synovial sarcoma strongly and characteristically expresses the anti-apoptotic protein BCL-2 — useful as a diagnostic marker and a hint that drugs disabling this survival signal might work against it."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "A receptor it leans on: synovial sarcoma frequently overexpresses EGFR, feeding growth signals into its proliferation, which has made the receptor a studied (if so far disappointing) target in this fusion-driven sarcoma."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "It is a flagship for cell therapy: synovial sarcoma expresses the cancer-testis antigen NY-ESO-1, the target of engineered T-cell therapy, and natural killer and other cell-based approaches are pursued against a tumor that resists checkpoint drugs."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 backs its survival signaling: synovial sarcoma cells show STAT3 activation that supports proliferation and immune evasion, one of the cooperating pathways downstream of the SS18-SSX fusion that drives the tumor."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "A solid cancer that clots: like other sarcomas, synovial sarcoma raises thrombosis risk through tumor-driven hypercoagulability, with deep-vein thrombosis and pulmonary embolism worsened by major limb surgery and chemotherapy."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Chemo neutropenia opens the door to infection: the ifosfamide-doxorubicin regimens used against synovial sarcoma cause deep neutropenia, so neutropenic fever and sepsis are recurrent treatment hazards."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Ifosfamide is hard on the kidney: the alkylator central to synovial-sarcoma chemotherapy is tubulotoxic, causing a Fanconi-type tubulopathy and lasting chronic kidney impairment, especially with cumulative dosing."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Its cure can sow a later leukemia: the alkylators and anthracyclines used against synovial sarcoma carry a small long-term risk of therapy-related myelodysplasia and acute myeloid leukemia in survivors."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Tumor inflammation and chemo blunt the marrow: advanced synovial sarcoma's inflammatory burden raises hepcidin while cytotoxic therapy suppresses erythropoiesis, adding an anemia-of-chronic-disease component to treatment cytopenias."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its anthracycline-based chemo strains the heart: doxorubicin, paired with ifosfamide as the mainstay for synovial sarcoma, is dose-dependently cardiotoxic and can leave a cardiomyopathy and heart failure in young survivors."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Its intensive chemotherapy opens the lung to mold: the deep neutropenia of doxorubicin-ifosfamide therapy for synovial sarcoma lets inhaled Aspergillus invade as pulmonary aspergillosis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A cancer of the young with hard therapy weighs on mood: synovial sarcoma's diagnosis in adolescents and young adults, disfiguring surgery and grueling chemotherapy contribute to depression and distress."
---

# Synovial Sarcoma

## Overview

**Synovial sarcoma (SS)** is a malignant soft tissue sarcoma universally defined by the chromosomal translocation **t(X;18)(p11;q11)** generating a **SS18-SSX1, SS18-SSX2, or SS18-SSX4 fusion protein**. Despite its name, synovial sarcoma does not arise from synovial tissue — it originates from undifferentiated mesenchymal/neural crest precursors. SS is the **second most common soft tissue sarcoma in adolescents and young adults** (after rhabdomyosarcoma) and one of the few sarcomas with a pathognomonic chromosomal translocation [^ladanyi note via kadoch-2013-ss18-ssx-baf].

**Epidemiology:**
- Incidence: ~800 cases/year USA; ~7-10% of all soft tissue sarcomas
- Peak age: 15-40 years (median ~26-30 years); rare in children <5 and adults >60
- Slight male predominance (~1.2:1 M:F)
- No established environmental risk factors; not associated with radiation or NF2 syndrome

**Anatomic locations:**
- Lower extremity (knee/thigh/popliteal fossa): ~50-60% — most common
- Upper extremity (shoulder, elbow, wrist, hand): ~15-20%
- Head and neck (pharynx, tongue, larynx): ~5-10%
- Trunk wall, mediastinum, pleura, lung (primary): ~5-10%
- Intra-abdominal, retroperitoneal: rare; worse prognosis
- Joint space involvement is uncommon despite the name

**Key clinical features:**
- Most present as a painless or mildly painful soft tissue mass, often near (but not within) a joint
- Many are initially misdiagnosed as a benign cyst or ganglion; delay in diagnosis 2-4 years is common
- ~20-25% present with calcifications on plain radiograph (stippled, "egg-shell" calcification characteristic)
- MRI: heterogeneous mass with "triple signal" appearance (hemorrhage, necrosis, calcification); T2 bright heterogeneous; invades fascial planes but rarely bone (unlike osteosarcoma)

## Structure

### Histological subtypes

**Biphasic synovial sarcoma (~30%):**
Two morphologically distinct components:
- **Epithelial component**: glandular/tubular structures lined by cuboidal-to-columnar cells with round nuclei, prominent nucleoli; positive for cytokeratin, EMA, CD34 (focal)
- **Spindle cell component**: fascicular spindle cells with scant cytoplasm, overlapping nuclei, minimal pleomorphism; characteristic hemangiopericytoma-like vessels
- SS18-SSX1 predominates in biphasic type
- Higher rate of epithelial marker positivity; diagnosis is more straightforward

**Monophasic synovial sarcoma (~65%):**
Exclusively spindle cell morphology; can mimic solitary fibrous tumor, malignant peripheral nerve sheath tumor (MPNST), or poorly differentiated carcinoma; TLE1 IHC + and SS18 FISH are critical for diagnosis in monophasic type; SS18-SSX2 predominates

**Poorly differentiated/high-grade synovial sarcoma (~5%):**
Round to large pleomorphic cells; loss of spindle cell morphology; >10 mitoses/10 HPF; rapid growth; worst prognosis; CDKN2A deletion common; all subtypes can have focal poorly differentiated areas

### IHC panel and diagnostic workup

**TLE1 (transducin-like enhancer protein 1):** nuclear positivity in ~85-90% of SS; most sensitive and specific single marker for SS among soft tissue tumors; however, focal TLE1 positivity also in MPNST, solitary fibrous tumor, desmoplastic small round cell tumor — context required

**Keratin (AE1/AE3, MNF116, CAM5.2):** positive in epithelial component of biphasic SS (~70%); focal (25-50%) in monophasic; variable

**EMA (epithelial membrane antigen):** positive in 85% of biphasic; 50% monophasic

**CD34:** focal in some SS; helps distinguish from SFT (CD34 diffuse in SFT)

**SOX2:** strongly positive in most SS (EZH2-driven SOX2 re-expression in SS); synergizes with TLE1 positivity

**SS18 FISH**: confirmatory; SS18 break-apart probe; sensitivity ~95%

## Function

### SS18-SSX oncogenic mechanism

The SS18-SSX fusion protein drives synovial sarcoma through BAF complex subversion [^kadoch-2013-ss18-ssx-baf]:
- SS18-SSX incorporates into cBAF complex, displacing wild-type SS18 → SMARCB1 evicted → BAF destabilized
- EZH2/PRC2 gains chromatin access → H3K27me3 spreads over differentiation loci → CDKN2A, KLF4, neural differentiation genes silenced
- QPGY activation domain (from SS18) drives ETV4, VEGF, and MYC target gene transcription
- Net result: tumor cells are locked in a proliferative, undifferentiated, vascular state with features of both epithelial and mesenchymal lineages

Normal cell (with wild-type BAF-SS18): BAF → SMARCB1 intact → PRC2 excluded from BAF target loci → CDKN2A transcribed → G1 arrest maintained; differentiation programs active

SS cell (with SS18-SSX): cBAF disrupted → SMARCB1 evicted → PRC2 silences CDKN2A + differentiation → proliferative state; paradoxically retains some epithelial features via ETV4/SOX2 de-repression

## Pathology

### Staging and risk stratification

**FNCLCC grading:**
- SS is uniformly high grade (FNCLCC grade 2-3); grading matters less for SS than for other STS
- Poor differentiation, CDKN2A deletion, high mitotic rate → grade 3

**Prognostic factors:**
- **Tumor size**: most important prognostic variable; ≤5 cm → 5-year OS ~85%; >5 cm → ~50%
- **CDKN2A deletion** (~10-15%): associated with >50% reduction in 5-year OS; worst prognostic marker in SS
- **Location**: extremity better than axial/pleural/intra-abdominal; head-neck intermediate
- **Extent of resection**: R0 (negative margin) resection → curative intent; R2 → high recurrence
- **Histological subtype**: poorly differentiated confers worst prognosis within SS
- **Metastases at diagnosis**: ~20-25% have metastases; lung (80%), lymph node (5-10%), bone

### Treatment

**Surgery:**
Wide local excision with ≥1 cm margins is the cornerstone; amputation rarely necessary with modern limb-salvage; compartmental resection when feasible; en-bloc resection of adjacent structures (nerve, vessel) when invaded; regional lymph node dissection for pathologically positive nodes (rare)

**Radiation therapy:**
- Adjuvant RT for high-risk features: tumor >5 cm, positive/close margins (<1 mm), deep location, recurrence
- Standard dose: 50-54 Gy preoperative or 60-66 Gy postoperative (IMRT preferred); equivalent local control in randomized VORTEX trial
- Preoperative RT preferred by most centers (smaller volume, better wound healing in selected cases)

**Chemotherapy — ifosfamide-based regimens:**
SS is one of the most chemotherapy-sensitive sarcomas:
- **First-line**: AI (doxorubicin 75 mg/m² + ifosfamide 10 g/m²) or AIM (AI + mesna) — ORR ~40-60%; PFS ~6-8 months in metastatic SS
- **Ifosfamide monotherapy**: ORR ~25-30% in SS; higher single-agent activity than in other STS subtypes
- **High-dose ifosfamide** (14-21 g/m²): ORR ~30-35% in ifosfamide-pretreated SS (unique ifosfamide sensitivity in SS vs other STS)

**Trabectedin:**
KAWAI 2015 (Phase 2 vs BSC) [^kawai-2015-trabectedin-synovial]: N=73 translocation-positive sarcomas (SS + myxoid liposarcoma); trabectedin 1.5 mg/m² q21d vs BSC; primary endpoint PFS; HR 0.07 (p<0.0001); 12-week PFS 60% vs 21%; OS benefit trending; ORR 17%; approved in Japan for translocation-related sarcoma; used off-label in USA; proposed mechanism: trabectedin directly disrupts SS18-SSX from chromatin

**Pazopanib:**
PALETTE Phase 3: PFS benefit in non-adipocytic STS including SS; HR 0.35; FDA-approved for advanced STS after prior chemotherapy; ORR ~5-10% in SS; PFS benefit more reliable than objective response

**Tazemetostat (EZH2 inhibitor):**
SARC057 (Phase 2): ORR ~22%, DCR ~67% in relapsed/refractory SS; FDA breakthrough therapy designation; ongoing Phase 1/2 combination studies (tazemetostat + ifosfamide; tazemetostat + pembrolizumab); represents first molecularly targeted therapy in SS

**Pembrolizumab/nivolumab:**
SS has low TMB (~1-2 mut/Mb) and variable PD-L1 expression; ICB response rates ~10-15% (lower than expected); MSS phenotype (no mismatch repair deficiency); combination with tazemetostat under investigation (EZH2 inhibition may restore IFN-γ response via epigenetic de-repression)

**Prognosis:**
- Localized SS (≤5 cm, R0 resection, no poor-differentiation): 5-year OS ~80-85%
- Localized SS (>5 cm, positive margin, or grade 3): 5-year OS ~50-60%
- Metastatic SS at diagnosis: 5-year OS ~20-25%; median OS ~18-24 months
- CDKN2A-deleted SS: 5-year OS ~30-40% regardless of stage
- Local recurrence: ~20-30% at 5 years; re-resection feasible if technically possible
- Lung metastases: surgical resection if oligometastatic; 5-year OS after resection ~30%

## Connections

- `connects-to` → **[SS18](../../03-molecular/ss18/README.md)** — SS18-SSX1/SSX2 fusion (t(X;18)(p11;q11)) is the pathognomonic alteration of synovial sarcoma (100% of cases); FISH for SS18 rearrangement or RT-PCR for SS18-SSX transcript is the diagnostic standard; SSX2 predominates in monophasic SS; SSX1 in biphasic SS.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — SS18-SSX displaces SMARCB1 from BAF → PRC2/EZH2 unrestricted → H3K27me3 at CDKN2A, KLF4, and differentiation loci; synovial sarcoma is EZH2-dependent; tazemetostat (EZH2 inhibitor, SARC057): ORR 22% in pretreated SS; FDA breakthrough therapy designation granted for SS.
- `connects-to` → **[SMARCB1](../../03-molecular/smarcb1/README.md)** — SS18-SSX displaces SMARCB1 from canonical BAF without SMARCB1 mutation → SMARCB1 degraded → BAF destabilized → PRC2 access; SMARCB1 IHC remains intact in SS (contrast AT/RT where SMARCB1 is lost); SS18-SSX knockdown → SMARCB1 re-occupies BAF → G1 arrest; shared EZH2 dependency.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — Homozygous CDKN2A deletion in ~10-15% synovial sarcoma predicts poor prognosis; EZH2/H3K27me3 epigenetically silences CDKN2A even without deletion → absent p16 → CDK4/6 hyperactivation → E2F-driven S-phase; CDK4/6 inhibitors (palbociclib) under evaluation in CDKN2A-deleted SS.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — SS18-SSX QPGY activation domain drives VEGF transcription → angiogenesis; pazopanib (VEGFR2 inhibitor, PALETTE trial: PFS HR 0.35) FDA-approved for advanced STS post-chemo including SS; VEGF overexpression correlates with tumor grade and metastatic potential in synovial sarcoma.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — SS has low TMB (~1-2 mut/Mb) and variable PD-L1 → limited single-agent ICB ORR (~10-15%); tazemetostat + pembrolizumab (Phase 1/2) under investigation; EZH2 inhibition may restore IFN-γ response; TMB-high/MSI-H SS (<5%) most likely ICB responders.
- `connects-to` → **[WNT/β-Catenin](../../03-molecular/wnt-beta-catenin/README.md)** — TLE1 (most specific SS IHC marker) is a Groucho-family WNT/β-catenin co-repressor (binds TCF/LEF); SS18-SSX recruits TLE1 into the oncogenic complex; ~30% of SS show nuclear β-catenin; CTNNB1 mutations in <5%; WNT pathway modulation is part of SS epigenetic de-regulation.
- `connects-to` → **[Atypical Teratoid/Rhabdoid Tumor](../atypical-teratoid-rhabdoid-tumor/README.md)** — Synovial sarcoma and AT/RT both derange the SWI/SNF (BAF) complex and depend on EZH2: SS18-SSX fusion ejects SMARCB1 from BAF (SMARCB1 stays detectable), while AT/RT deletes SMARCB1 entirely (INI1 lost on IHC) — yet both respond to the EZH2 inhibitor tazemetostat.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Synovial sarcoma is a soft-tissue sarcoma of adolescents and young adults arising near — not from — joints, typically in deep extremity soft tissue (around the knee); despite the name it is not of synovial origin, and wide resection plus radiation is standard.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lung is the dominant metastatic site in synovial sarcoma: it spreads hematogenously to the lungs even years after the primary is controlled, so long-term chest CT surveillance is essential and pulmonary metastasectomy is offered for limited disease.
- `connects-to` → **[Schwannomatosis](../schwannomatosis/README.md)** — Synovial sarcoma and schwannomatosis both subvert the SWI/SNF (BAF) chromatin-remodeling complex: synovial sarcoma's SS18-SSX fusion reprograms BAF to silence tumor-suppressors, while loss of the BAF subunit SMARCB1 drives schwannomatosis and rhabdoid tumors.
- `connects-to` → **[Ewing Sarcoma](../ewing-sarcoma/README.md)** — Synovial and Ewing sarcoma are fusion-driven sarcomas of young adults defined by a single translocation: SS18-SSX for synovial sarcoma, EWSR1-FLI1 for Ewing—both aberrant transcription factors that remodel the epigenome, models of fusion-oncoprotein cancer.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Synovial sarcoma is a mesenchymal tumor of fibroblast-like spindle cells despite its misleading name: it arises not from synovium but from a primitive mesenchymal cell, its monophasic form being sheets of spindle cells expressing TLE1 and SS18-SSX.
- `connects-to` → **[Rhabdomyosarcoma](../rhabdomyosarcoma/README.md)** — Synovial sarcoma and rhabdomyosarcoma are both fusion-driven soft-tissue sarcomas: synovial sarcoma's SS18-SSX fusion hijacks the SWI/SNF complex, while alveolar RMS's PAX-FOXO1 drives myogenic transcription—translocations defining distinct, aggressive sarcomas.
- `connects-to` → **[MPNST](../mpnst/README.md)** — Synovial sarcoma and MPNST are spindle-cell sarcomas that can look alike: synovial sarcoma is defined by SS18-SSX, MPNST by NF1-driven nerve-sheath origin—so SS18-SSX testing and S100/SOX10 staining separate these spindle tumors.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Synovial sarcoma is managed like other high-grade soft-tissue sarcomas with surgery plus radiotherapy: wide resection combined with photon radiation improves local control, while the SS18-SSX fusion is now also targeted by EZH2 inhibitors and cellular therapy.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 mutation can mark progression in synovial sarcoma: while the SS18-SSX fusion is the defining initiating event, secondary p53 loss appears in high-grade, dedifferentiated tumors—so the genome guardian's failure layers onto the fusion oncogene to worsen behavior.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — TERT activation helps immortalize synovial sarcoma cells: telomerase reactivation, alongside the SS18-SSX fusion that reprograms the epigenome, lets these translocation-driven sarcomas divide indefinitely—a step common to many cancers despite their distinct drivers.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Synovial sarcoma joins the broad sarcoma spectrum of Li-Fraumeni syndrome: although defined by the somatic SS18-SSX fusion rather than germline p53 loss, sarcomas like it occur excessively in p53-deficient patients—linking fusion-driven and hereditary sarcomas.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Synovial sarcoma is a leading target for engineered T-cell therapy: it expresses cancer-testis antigens (NY-ESO-1, MAGE-A4), so afami-cel/tecelra—TCR T cells the immune system is reprogrammed to deploy—became the first such therapy approved for a solid tumor.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Synovial sarcoma's cancer-testis antigens depend on antigen presentation: dendritic cells process NY-ESO-1 and MAGE-A4 onto HLA, the step that primes the T cells engineered immunotherapies exploit—and the tumor evades this by downregulating MHC.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Synovial sarcoma is a rare primary cardiac sarcoma: though usually arising in limb soft tissue, it can originate in the heart or pericardium, presenting with obstruction or effusion and a grim prognosis given difficult surgical clearance.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Synovial sarcoma is a flagship for engineered T cells: it expresses NY-ESO-1, and afamitresgene autoleucel—TCR-engineered cytotoxic T cells targeting that antigen—won FDA approval in 2024 for this sarcoma, a first for solid-tumor TCR therapy.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Synovial sarcoma is an immunologically 'cold' tumor rich in macrophages: tumor-associated macrophages dominate its sparse immune infiltrate and suppress T-cell responses, helping explain why checkpoint inhibitors disappoint while TCR-engineered T cells work.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Synovial sarcoma runs an IGF-1 autocrine loop: the tumor overexpresses IGF1R and its ligands to drive growth and survival, so IGF1R inhibition has been explored as targeted therapy in this fusion-driven sarcoma.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — Synovial sarcoma is a chromatin disease: its SS18-SSX fusion hijacks the SWI/SNF (BAF) complex—which includes ARID1A—wrenching it onto the wrong genes, so the tumor is driven by epigenetic miswiring rather than classic mutations.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Synovial sarcoma's immunotherapy is limited by regulatory T cells: it expresses the NY-ESO-1 antigen targeted by TCR-engineered T cells, but a Treg-rich, suppressive microenvironment blunts the attack and curbs durable responses.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Synovial sarcoma grows on IGF-driven mTOR signaling: autocrine IGF-1 feeds the PI3K-AKT-mTOR axis to fuel proliferation, making mTOR a studied target in a sarcoma otherwise reliant on chemotherapy and surgery.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Hypoxia stokes synovial sarcoma's aggressiveness: as the tumor outgrows its blood supply, low oxygen drives invasion and metastasis, contributing to the lung spread that threatens patients with this translocation-driven sarcoma.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Synovial sarcoma can spread to the brain: though lung is the dominant metastatic site, hematogenous spread occasionally seeds brain metastases in advanced disease, prompting imaging when neurologic symptoms appear.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Synovial sarcoma leans on AKT downstream of IGF: autocrine IGF-1 activates the PI3K-AKT-mTOR axis to drive proliferation and survival, so AKT-mTOR inhibitors are studied alongside the IGF and immune approaches in this sarcoma.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Synovial sarcoma sometimes calcifies: foci of calcium deposit within the tumor, and heavily calcified synovial sarcomas tend to carry a notably better prognosis than non-calcified ones.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Synovial sarcoma can spread to the liver: though it favors the lungs, hematogenous metastasis seeds the liver and other organs in advanced disease, marking the shift to systemic treatment.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Synovial sarcoma weaves a fibrous stroma: its spindle-cell component lays down dense collagen in the biphasic tumor, the firm fibrous tissue that, with epithelial nests, defines its histology.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy exposes synovial sarcoma's split personality: alongside the spindle cells sit true epithelial cells joined by desmosomes, sprouting microvilli into gland-like lumina over a basal lamina — the ultrastructure of its biphasic histology.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Synovial sarcoma can invade the skeleton: though it favors the lungs, late disease seeds bone and the marrow within, and tumors abutting a joint erode the neighboring bone as they grow.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Rarely synovial sarcoma is born in the kidney itself: primary renal synovial sarcoma, carrying the same SS18 fusion, is a recognized aggressive entity that masquerades as a more common kidney tumor until molecular testing reveals it.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Despite its name, synovial sarcoma weaves a fibrous tumor: its spindle cells sit in a collagen-rich stroma, often with stippled calcification, and the biphasic form adds glandular epithelium — a texture that, with the SS18 fusion, makes the diagnosis.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — The ifosfamide in its chemotherapy can fog the brain: a metabolite of this alkylator crosses into the CNS and poisons neurons, causing a reversible encephalopathy with confusion and seizures that methylene blue is used to treat.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Ifosfamide also injures the kidney's tubules: the resulting Fanconi-like syndrome wastes magnesium, phosphate, and bicarbonate into the urine, so electrolytes are monitored and replaced through synovial sarcoma treatment.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — An antibody now clinches the diagnosis: a stain against the SS18-SSX fusion protein is highly specific for synovial sarcoma, and with TLE1 it confirms the t(X;18)-driven tumor that can otherwise mimic many spindle-cell cancers.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The doxorubicin-ifosfamide regimen empties the marrow: both drugs are heavily myelosuppressive, dropping neutrophil counts so that febrile neutropenia is a recurring hazard through synovial sarcoma chemotherapy.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Treatment and tumor both thin the red cells: the anthracycline-and-alkylator chemotherapy suppresses marrow erythrocyte production, leaving an anemia and fatigue that may need transfusion across the long course of care.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — The doxorubicin-ifosfamide chemotherapy strains the heart: the anthracycline backbone for synovial sarcoma is cumulatively cardiotoxic to cardiomyocytes, so cardiac function is checked across treatment in these often-young patients.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Cure can cost fertility: synovial sarcoma strikes adolescents and young adults, and its alkylating ifosfamide and any pelvic radiation damage the gonads, so fertility preservation is discussed before treatment begins.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — It is a hypoxic, vessel-hungry tumor: synovial sarcoma stabilizes HIF and pours out VEGF to feed its growth, the angiogenic drive behind the activity of anti-VEGF tyrosine-kinase inhibitors like pazopanib against it.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — It survives by blocking its own death: synovial sarcoma strongly and characteristically expresses the anti-apoptotic protein BCL-2 — useful as a diagnostic marker and a hint that drugs disabling this survival signal might work against it.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — A receptor it leans on: synovial sarcoma frequently overexpresses EGFR, feeding growth signals into its proliferation, which has made the receptor a studied (if so far disappointing) target in this fusion-driven sarcoma.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — It is a flagship for cell therapy: synovial sarcoma expresses the cancer-testis antigen NY-ESO-1, the target of engineered T-cell therapy, and natural killer and other cell-based approaches are pursued against a tumor that resists checkpoint drugs.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 backs its survival signaling: synovial sarcoma cells show STAT3 activation that supports proliferation and immune evasion, one of the cooperating pathways downstream of the SS18-SSX fusion that drives the tumor.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — A solid cancer that clots: like other sarcomas, synovial sarcoma raises thrombosis risk through tumor-driven hypercoagulability, with deep-vein thrombosis and pulmonary embolism worsened by major limb surgery and chemotherapy.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Chemo neutropenia opens the door to infection: the ifosfamide-doxorubicin regimens used against synovial sarcoma cause deep neutropenia, so neutropenic fever and sepsis are recurrent treatment hazards.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Ifosfamide is hard on the kidney: the alkylator central to synovial-sarcoma chemotherapy is tubulotoxic, causing a Fanconi-type tubulopathy and lasting chronic kidney impairment, especially with cumulative dosing.
- `connects-to` → **[AML](../aml/README.md)** — Its cure can sow a later leukemia: the alkylators and anthracyclines used against synovial sarcoma carry a small long-term risk of therapy-related myelodysplasia and acute myeloid leukemia in survivors.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Tumor inflammation and chemo blunt the marrow: advanced synovial sarcoma's inflammatory burden raises hepcidin while cytotoxic therapy suppresses erythropoiesis, adding an anemia-of-chronic-disease component to treatment cytopenias.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its anthracycline-based chemo strains the heart: doxorubicin, paired with ifosfamide as the mainstay for synovial sarcoma, is dose-dependently cardiotoxic and can leave a cardiomyopathy and heart failure in young survivors.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Its intensive chemotherapy opens the lung to mold: the deep neutropenia of doxorubicin-ifosfamide therapy for synovial sarcoma lets inhaled Aspergillus invade as pulmonary aspergillosis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A cancer of the young with hard therapy weighs on mood: synovial sarcoma's diagnosis in adolescents and young adults, disfiguring surgery and grueling chemotherapy contribute to depression and distress.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^kadoch-2013-ss18-ssx-baf]: Kadoch C, Crabtree GR. Reversible disruption of mSWI/SNF (BAF) complexes by the SS18-SSX oncogenic fusion in synovial sarcoma. *Cell.* 2013;153(1):71-85. [doi:10.1016/j.cell.2013.02.036](https://doi.org/10.1016/j.cell.2013.02.036) · [PubMed 23540691](https://pubmed.ncbi.nlm.nih.gov/23540691/)
[^kawai-2015-trabectedin-synovial]: Kawai A, Araki N, Sugiura H, et al. Trabectedin monotherapy after standard chemotherapy versus best supportive care in patients with advanced, translocation-related sarcoma: a randomised, open-label, phase 2 study. *Lancet Oncol.* 2015;16(4):406-416. [doi:10.1016/S1470-2045(15)70098-7](https://doi.org/10.1016/S1470-2045(15)70098-7) · [PubMed 25795407](https://pubmed.ncbi.nlm.nih.gov/25795407/)

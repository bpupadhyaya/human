---
schema: human-scale-entry/v1
id: burkitt-lymphoma
name: Burkitt Lymphoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Burkitt lymphoma is a highly aggressive GC B-cell lymphoma defined by MYC translocation and near-100% Ki-67; endemic (EBV+), sporadic, immunodeficiency-associated subtypes; DA-EPOCH-R or R-CODOX-M/IVAC for adults; rituximab+LMB for pediatric; TLS prophylaxis essential."
aliases: ["Burkitt lymphoma", "BL", "Burkitt's lymphoma", "endemic Burkitt", "sporadic Burkitt", "HIV Burkitt lymphoma", "Burkitt leukemia", "L3 ALL"]
sources:
  - id: roschewski-2020-da-epoch-r-bl
    type: peer-reviewed
    cite: "Roschewski M, Dunleavy K, Abramson JS, et al. Multicenter study of risk-adapted therapy with dose-adjusted EPOCH-R in adults with untreated Burkitt lymphoma. J Clin Oncol. 2020;38(22):2519-2529."
    doi: "10.1200/JCO.19.03259"
    pmid: "32530765"
    url: "https://doi.org/10.1200/JCO.19.03259"
  - id: minard-colin-2017-inter-b-nhl-ritux
    type: peer-reviewed
    cite: "Minard-Colin V, Auperin A, Pillon M, et al. Rituximab for children and adolescents with high-risk B-cell non-Hodgkin lymphoma: results of the randomized Inter-B-NHL Ritux 2010 trial. J Clin Oncol. 2022;40(22):2458-2471."
    doi: "10.1200/JCO.21.01940"
    pmid: "35436151"
    url: "https://doi.org/10.1200/JCO.21.01940"
cross_links:
  - target: 01-human/03-molecular/npm1
    relation: connects-to
    note: "NPM1 is a nucleolar ribosome biogenesis factor essential in Ki-67~100% BL cells; NPM1 sequesters ARF → attenuates the MYC → ARF → p53 checkpoint; NPM1 overexpression in high-grade B-cell lymphomas; NPM1 phosphorylation by CDK2 regulates centrosome duplication in BL."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "MYC translocation [t(8;14) ~80%, t(2;8) ~15%, t(8;22) ~5%] is the defining alteration of Burkitt lymphoma; MYC juxtaposed to Ig loci → constitutive transcription; MYC drives near-100% Ki-67; BET bromodomain inhibitors suppress MYC in BL preclinically."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "BL cells silence ARF (CDKN2A deletion ~50%) to evade MYC → ARF → p53 checkpoint; TP53 mutations in ~30% BL at relapse; p53 pathway is intact in most primary BL; MDM2 inhibitors (idasanutlin) + DA-EPOCH-R explored in Phase 1 for relapsed/refractory BL."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "BL tumor microenvironment is immune-poor; PD-L1 expression is variable; EBV+ endemic BL has more immune infiltrate than sporadic BL; PD-1 blockade combined with rituximab-based therapy in early trials for relapsed/refractory high-grade B-cell lymphoma."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "BL arises from germinal center B cells with MYC translocation to Ig loci (IGH/IGK/IGL) during VDJ recombination or class-switch recombination; CD19+/CD20+/CD10+/BCL6+/BCL2- immunophenotype reflects GC B-cell origin; MYC drives near-100% Ki-67 in these rapidly cycling B cells."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "BL originates in germinal center B cells; MYC translocation arises from AID-mediated DSBs at Ig loci during class-switch recombination; CD10+/BCL6+ confirms GC origin; EBV+ endemic BL expresses BCL6 and EBNA-1 in Latency I, exploiting GC biology for viral persistence."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "CD20 (MS4A1) is expressed on all BL cells; rituximab (anti-CD20 mAb) is standard in adult DA-EPOCH-R and pediatric LMB regimens; Inter-B-NHL Ritux 2010: rituximab addition → 3-year EFS 93.9% vs 79.8% (HR 0.33, p<0.001) in high-risk pediatric BL; obinutuzumab explored in R/R BL."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "Epstein-Barr virus is found in nearly all endemic (African) Burkitt lymphoma and a minority of sporadic cases: the virus persists in germinal-center B cells in Latency I, and its EBNA/miRNA program helps the MYC-translocated cell evade apoptosis and immune clearance."
  - target: 02-pathogen/04-parasites/plasmodium-falciparum
    relation: connects-to
    note: "Holoendemic Plasmodium falciparum malaria is the geographic cofactor for endemic Burkitt lymphoma: chronic malaria expands germinal-center B cells and induces AID, raising the chance of the MYC-Ig translocation, while malaria-driven immune dysregulation reactivates EBV."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Burkitt lymphoma must be separated from DLBCL and double-hit large-cell lymphoma: Burkitt has a sole MYC translocation, ~100% Ki-67, and is BCL-2-negative, so FISH for MYC/BCL-2/BCL-6 is essential — a Burkitt diagnosis mandates intensive regimens (DA-EPOCH-R), not R-CHOP."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "Burkitt lymphoma is an AIDS-defining cancer: HIV-driven immunosuppression and chronic B-cell activation raise Burkitt risk even at preserved CD4 counts—so a fast-growing lymphoma in an HIV-positive patient is Burkitt until proven otherwise."
  - target: 01-human/07-system/follicular-lymphoma
    relation: connects-to
    note: "Burkitt and follicular lymphoma are both germinal-center B-cell tumors but opposite in tempo: Burkitt is MYC-driven, near-100% Ki67, doubles in a day and is curable with intensive chemo, while BCL2-driven follicular lymphoma is indolent, incurable, and waxes over years."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "The 'starry sky' appearance pathognomonic of Burkitt lymphoma comes from tingible-body macrophages: scattered pale macrophages engulfing apoptotic debris from the explosively proliferating MYC-driven B cells stand out against the dark sheet of tumor."
  - target: 01-human/07-system/malaria
    relation: connects-to
    note: "Endemic Burkitt lymphoma is malaria-driven: chronic Plasmodium falciparum infection drives intense B-cell proliferation and weakens control of co-infecting Epstein-Barr virus, together promoting the MYC translocation that causes the jaw and abdominal tumors of African children."
  - target: 01-human/07-system/hodgkin-lymphoma
    relation: connects-to
    note: "Burkitt and Hodgkin lymphoma are both EBV-associated but biologically opposite: Burkitt is a fast MYC-driven mature B-cell tumor curable with intensive chemo, while Hodgkin is a CD30+ Reed-Sternberg-cell lymphoma with a rich reactive infiltrate, treated differently with ABVD."
  - target: 01-human/07-system/mantle-cell-lymphoma
    relation: connects-to
    note: "Burkitt and mantle cell lymphoma are aggressive B-cell lymphomas defined by single translocations: Burkitt's t(8;14) drives MYC, mantle cell's t(11;14) drives cyclin D1—but Burkitt is curable while mantle cell is aggressive yet incurable, a key prognostic split."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Burkitt lymphoma is MYC-driven, not BCL2-driven—a key contrast: classic Burkitt carries the MYC translocation and is BCL2-negative, so a tumor with both MYC and BCL2 rearrangements is instead a more aggressive double-hit high-grade lymphoma, not true Burkitt."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Burkitt lymphoma is a germinal-center B cell frozen short of plasma-cell fate: the MYC-driven clone proliferates explosively (near-100% Ki-67) instead of maturing into antibody-secreting plasma cells—so its hallmark is runaway growth, the fastest-doubling human tumor."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Burkitt lymphoma exposes the immune system's role in cancer control: it surges in immunodeficiency (HIV) and where chronic malaria and EBV exhaust immune surveillance—so endemic Burkitt is partly a cancer of weakened immune defense against EBV-driven B cells."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Burkitt lymphoma is an aggressive cancer of the lymphatic system: the endemic form classically erupts as a jaw or facial mass while sporadic disease hits abdominal lymph nodes and bowel, reflecting its origin in germinal-center B cells of lymphoid tissue."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Burkitt lymphoma can flood the bone marrow and blood: with the fastest doubling time of any human tumor, it readily spills into marrow as a leukemic phase, so it overlaps clinically with acute leukemia and demands immediate intensive chemotherapy."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Burkitt lymphoma is the textbook cause of tumor lysis syndrome threatening the kidney: its explosive growth and rapid chemo-induced cell death dump uric acid, potassium and phosphate that can crystallize and cause acute kidney injury without aggressive prophylaxis."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Sporadic Burkitt lymphoma favors the abdomen: it typically presents as a fast-growing ileocecal or bowel mass causing obstruction or intussusception, so a rapidly enlarging abdominal tumor in a child is a classic Burkitt presentation."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Burkitt lymphoma is held in check by cytotoxic T cells: EBV-specific T-cell surveillance normally controls infected B cells, so when HIV or immunosuppression weakens it, EBV-driven Burkitt emerges—underpinning T-cell-based immunotherapies."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Burkitt lymphoma's abdominal disease often centers on the spleen and viscera: this fast-growing lymphoma seeds the spleen, liver, and mesentery, so bulky intra-abdominal and splenic involvement is typical of the sporadic form."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Burkitt lymphoma is the textbook cause of tumor lysis syndrome: its explosively dividing cells burst and dump phosphate into the blood, and the resulting hyperphosphatemia binds calcium and crashes the kidneys—why hydration and rasburicase precede therapy."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "NK cells help police the EBV behind Burkitt lymphoma: natural killer cells kill virus-infected B cells before they transform, so when immune surveillance fails—in HIV or malaria-driven immune exhaustion—EBV-driven Burkitt is far more likely."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Malaria-driven Treg expansion fuels endemic Burkitt: chronic falciparum infection ramps up regulatory T cells that suppress immunity, loosening control of EBV-infected B cells and helping the MYC-translocated tumor emerge in African children."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Burkitt is the textbook tumor-lysis cancer: its blistering growth means chemotherapy bursts huge numbers of cells at once, dumping potassium into the blood, so dangerous hyperkalemia and arrhythmia must be anticipated and prevented from the first dose."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Burkitt lymphoma readily seeds the brain: it has a strong tendency to spread to the central nervous system and meninges, so treatment includes CNS-directed chemotherapy and prophylaxis to reach this sanctuary the bloodstream drugs miss."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "MYC rewires Burkitt's metabolism through the PI3K-mTOR axis: the driving oncogene partners with mTOR signaling to fuel the relentless growth and protein synthesis, making this pathway an attractive target alongside chemotherapy."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Burkitt's furious metabolism can acidify the blood: its MYC-driven glycolysis pours out lactic acid, so a rare type B lactic acidosis can appear from the tumor burden alone, even before chemotherapy begins."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Sporadic Burkitt lymphoma fills the abdomen: it forms bulky masses that involve the bowel, liver, and ovaries, so abdominal pain and a rapidly growing belly mass are common presentations in children."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Burkitt lymphoma blazes on a PET scan: its near-100% proliferation rate makes it intensely avid for the radiotracer's photons, so PET imaging vividly stages this fastest-growing human tumor."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Burkitt's massive tumor lysis crashes calcium: the flood of phosphate from dying cells binds calcium and drops it, risking tetany and arrhythmia alongside the high potassium of the emergency."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Endemic Burkitt classically swells the jaw and orbit: rapidly growing facial and eye-socket masses are the hallmark presentation in the African malaria belt where the EBV-driven form arises."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "MYC floors the cell cycle in Burkitt: it drives cyclin D and CDK4/6 to push cells relentlessly from rest into division, powering the roughly one-day doubling time of this fastest-growing tumor."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows Burkitt's 'starry sky': sheets of blasts with lipid-vacuoled cytoplasm are dotted with tingible-body macrophages clearing the debris of cells dying as fast as the tumor divides."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Sporadic Burkitt erupts in the abdomen: it forms bulky masses in the stomach, ileocecum, and surrounding organs, the GI presentation that distinguishes it from the jaw tumors of the endemic African form."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "Abdominal Burkitt seeds the retroperitoneum: its explosive growth fills the abdomen and can involve the adrenals, kidneys, and ovaries, masses that swell almost visibly day by day."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "An antibody is part of the cure: rituximab against CD20 added to intensive chemotherapy markedly improves outcomes in Burkitt lymphoma, harnessing the immune system against the malignant B cells."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Burkitt readily invades the nervous system: its high rate of CNS spread demands intrathecal chemotherapy as prophylaxis, while the vincristine in its regimens poisons peripheral neurons into a dose-limiting neuropathy."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Burkitt carries the highest risk of tumor lysis syndrome: as its fast-dividing cells burst under chemotherapy, potassium, phosphate, and uric acid surge while calcium and magnesium swing — a metabolic storm that can stop the heart and shut the kidneys."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "MYC needs a partner in Burkitt: recurrent TCF3 and ID3 mutations switch on tonic B-cell-receptor signaling through PI3K-AKT, which cooperates with the translocated MYC to drive the tumor — a survival pathway being targeted by PI3K inhibitors."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Sporadic Burkitt favors the abdomen and gonads: bulky ileocecal masses and ovarian or testicular deposits are common presentations, and the intensive multi-agent chemotherapy that cures it can leave survivors infertile."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Marrow takeover drops the red cells: when Burkitt floods the bone marrow it crowds out normal blood production, and the resulting anemia — deepened by chemotherapy — leaves patients pale and fatigued during treatment."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Sporadic Burkitt strikes the gut: it classically presents as a bulky ileocecal mass in the small bowel, the fastest-growing human tumor erupting as an abdominal emergency that can obstruct or perforate."
  - target: 01-human/07-system/all
    relation: connects-to
    note: "Burkitt has a leukemic twin: when it floods the blood and marrow it becomes mature B-cell acute lymphoblastic leukemia (the old L3 ALL), treated on the same intensive Burkitt protocols."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Its birthplace is the germinal center's scaffold: follicular dendritic cells present antigen to the rapidly dividing B cells there, the microenvironment from which the MYC-driven Burkitt clone arises."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Cure comes at the cost of deep immunosuppression: the intensive multi-agent chemotherapy for Burkitt produces severe neutropenia, so febrile neutropenia and sepsis are among the leading treatment-related dangers."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Burkitt is the NF-κB-independent lymphoma: unlike activated B-cell DLBCL it survives on tonic BCR/PI3K and MYC rather than chronic NF-κB signaling, a distinction that shapes which targeted therapies can work."
  - target: 01-human/07-system/multiple-myeloma
    relation: connects-to
    note: "Two ends of the B-cell lineage: Burkitt is an aggressive germinal-center B-cell tumor while myeloma is a malignancy of terminal plasma cells, contrasting points on the maturation path that both rely on MYC dysregulation."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "The fastest tumor floods the kidneys when it dies: Burkitt's explosive proliferation gives it the highest tumor-lysis-syndrome risk of any cancer, releasing urate and phosphate that injure the kidneys into acute and sometimes chronic kidney disease."
  - target: 01-human/07-system/disseminated-intravascular-coagulation
    relation: connects-to
    note: "Massive tumor turnover can ignite clotting: the high cell burden and rapid lysis of Burkitt lymphoma can release procoagulant material that triggers disseminated intravascular coagulation, especially around the start of chemotherapy."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "An aggressive lymphoma that clots: like other high-grade cancers, Burkitt raises venous thromboembolism risk through tumor-driven hypercoagulability, compounded by central venous catheters and immobility during intensive treatment."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Intensive chemo strips the lung's defenses: the dose-dense regimens curing Burkitt cause profound neutropenia, letting inhaled Aspergillus invade as pulmonary aspergillosis, a feared infectious complication."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "Immunosuppression opens the lung to it: the intensive chemotherapy — and in HIV-associated cases the underlying immunodeficiency — deplete T-cell defenses, so Pneumocystis prophylaxis accompanies Burkitt treatment."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Marrow takeover and chemo blunt the count: Burkitt frequently infiltrates the bone marrow, and with its inflammatory cytokines and myelosuppressive therapy this produces anemia carrying a chronic-disease component."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its anthracyclines strain the heart: the doxorubicin in the intensive CODOX-M/IVAC and DA-EPOCH regimens for Burkitt is dose-dependently cardiotoxic, risking cardiomyopathy and heart failure."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Vincristine leaves the nerves raw: the vinca alkaloid central to Burkitt chemotherapy causes a dose-limiting peripheral neuropathy with numbness and neuropathic pain."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A sudden, explosive cancer weighs on mood: Burkitt's rapid onset, urgent intensive chemotherapy and life-threatening course impose a heavy psychological burden contributing to depression."
---

# Burkitt Lymphoma

## Overview

**Burkitt lymphoma (BL)** is the most rapidly proliferating human malignancy, defined by a **MYC translocation** juxtaposing MYC (8q24) to an immunoglobulin locus [t(8;14) ~80%, t(2;8) ~15%, t(8;22) ~5%], germinal center (GC) B-cell immunophenotype (CD19+, CD20+, CD10+, BCL6+, TdT–, BCL2–), and near-100% Ki-67 proliferative index. Three distinct subtypes reflect different epidemiological and etiological contexts: **endemic BL** (sub-Saharan Africa, Papua New Guinea; EBV+ in ~95-100%; presents as jaw/facial mass in children aged 4-7); **sporadic BL** (Western countries; EBV+ in ~15-30%; ileocecal/abdominal primary in children and young adults); **immunodeficiency-associated BL** (HIV+ individuals; EBV+ in ~20-40%; often abdominal). The extreme proliferative rate creates the hallmark "**starry sky**" pattern on histology — pale tingible-body macrophages phagocytizing apoptotic tumor cells against a dark background of cycling lymphoma cells. Modern treatment of **adult BL** with **dose-adjusted EPOCH-R** (DA-EPOCH-R) achieves complete remission in ~87-90% of patients with manageable toxicity [^roschewski-2020-da-epoch-r-bl]; pediatric BL is treated with intensive **rituximab + LMB chemotherapy** (Inter-B-NHL Ritux 2010: rituximab addition improved 3-year EFS from 79.8% to 93.9%, HR 0.33, p<0.001 in high-risk) [^minard-colin-2017-inter-b-nhl-ritux].

**Epidemiology:**
- ~1,200-1,500 cases/year USA (all ages); endemic BL ~3-5x more common globally
- Pediatric B-NHL: ~40% of cases are BL; most common pediatric lymphoma in sub-Saharan Africa
- Median age: pediatric for endemic (peak age 4-7); bimodal in sporadic (child + young adult)
- Male predominance 3-4:1 in endemic; 2-3:1 in sporadic
- HIV+ patients: BL is an AIDS-defining malignancy; CD4 count often >100-200 cells/μL at BL diagnosis (unlike primary CNS lymphoma which presents at lower CD4)

## Structure

### Molecular landscape

**MYC translocation — the defining event:**
All BL carry a MYC translocation to an Ig locus:
- **t(8;14)(q24;q32) (~80%):** MYC (8q24) → IGH (14q32) — most common; MYC juxtaposed to IGH E μ/α enhancer → constitutive MYC expression in B cells; in endemic BL, breakpoint is at the MYC promoter/5' region; in sporadic BL, breakpoint is within MYC exon 1 or intron 1
- **t(2;8)(p12;q24) (~15%):** IGK → MYC; less common
- **t(8;22)(q24;q11) (~5%):** MYC ← IGL; least common

**MYC drives Burkitt biology:**
- Near-100% Ki-67 (not just high, virtually all cells are cycling at any timeframe)
- Ribosome biogenesis activation → nucleolar prominence (the histological correlate)
- Aerobic glycolysis (Warburg effect) → rapid lactate production → metabolic stress
- TERT expression → telomere maintenance
- MYC-driven oncogenic stress → p53 activation → but BL escapes via ARF (CDKN2A) deletion or MDM2 overexpression; TP53 wild-type in ~70% primary BL (p53 function partially suppressed by other mechanisms)

**Additional molecular features:**
- **ID3/TCF3 (E2A) mutations:** ~70% BL; ID3 loss-of-function → TCF3 activation → B-cell receptor signaling → pro-survival PI3K; TCF3 mutations less common; ID3 is the canonical BL second hit after MYC translocation
- **CCND3 mutations:** ~38% BL; cyclin D3 T283A → CDK4/6 activation → G1/S bypass → accelerates proliferation
- **TP53 mutations:** ~30-40% at relapse; ~15-25% primary BL; MDM2 amplification ~3%; CDKN2A deletion ~50% (ARF + CDKN2A/p16 co-deleted)
- **RHOA mutations:** ~5%; small GTPase
- **EBV (EBNA-1, EBV-encoded miRNAs):** Endemic BL: EBV-driven BCL6 expression, immune evasion (BHRF1/BART miRNAs); LMP1/LMP2A not expressed in endemic BL (unlike EBV+ DLBCL NOS); EBV establishes Latency I in BL

**Not present in BL:**
- BCL2 translocation (distinguishes BL from DLBCL/follicular lymphoma)
- BCL2 protein overexpression (important diagnostic distinction from double-hit lymphoma)
- BCL6 translocation (BCL6 expressed but not translocated)

### Histology and immunophenotype

**"Starry sky" pattern:** Sheets of monomorphic intermediate-sized lymphoid blasts with scant basophilic cytoplasm, squared-off nuclei, multiple small nucleoli, numerous apoptotic figures; pale tingible-body macrophages (phagocytizing apoptotic debris) scattered → "stars" in a dark "sky" of tumor cells; highly characteristic but not specific to BL (seen in any high-grade lymphoma with rapid turnover).

**Immunophenotype:**
- B-cell markers: CD19+, CD20+, CD22+, CD79a+, CD38+
- GC markers: CD10+, BCL6+
- CD77+ (hallmark of GC centroblasts)
- Ki-67 ~100% (virtually pathognomonic)
- **BCL2 negative** (critical diagnostic distinction from DLBCL)
- TdT negative (distinguishes BL from acute lymphoblastic leukemia, though BL can present as L3-ALL)
- CD5–, CD23–, Cyclin D1–

## Function

### Pathophysiology of extreme proliferation

**MYC → ribosome biogenesis → anabolic metabolism:**
MYC activates all ~350 ribosomal protein genes, RNA Pol I (rDNA transcription), and RNA Pol III (5S rRNA, tRNA) → BL cells produce ribosomes at maximal capacity → enables protein synthesis to support doubling every ~24-48 hours; this extreme anabolic state creates vulnerability:
- **Nucleolar stress (RNA Pol I inhibitors: CX-5461):** Inhibit rDNA transcription → nucleolar disruption → MDM2 trapped in nucleolus → p53 released → apoptosis; promising in BL and other MYC-driven lymphomas
- **NPM1 dependency:** NPM1 is essential for pre-rRNA processing and export; in Ki-67~100% BL cells, NPM1 is a critical rRNA chaperone; BL cannot tolerate NPM1 loss

**MYC → ARF → p53 evasion:**
Normal cells: MYC overactivation → ARF (p14ARF from CDKN2A alt. reading frame) upregulation → MDM2 binding → MDM2 sequestration → p53 stabilization → apoptosis. BL escapes via:
1. CDKN2A deletion (ARF + p16 co-deleted, ~50% BL)
2. MDM2 amplification (~3%)
3. NPM1 overexpression → ARF nucleolar sequestration → MDM2 not inhibited
4. TP53 mutation (~25-30% primary, ~30-40% relapsed)

**Tumor lysis syndrome (TLS):**
BL is the highest TLS-risk malignancy; massive tumor cell death on first contact with chemotherapy → uric acid, potassium, phosphate, LDH release → hyperuricemia → AKI, hypocalcemia, cardiac arrhythmia; TLS prophylaxis is MANDATORY: rasburicase (urate oxidase, preferred if high LDH/bulky disease), aggressive IV hydration (200-250 mL/hour, urine output ≥100 mL/hour), continuous cardiac monitoring, allopurinol for low-risk; delay start of chemotherapy until adequate TLS prophylaxis established.

## Pathology

### Staging (Murphy/St. Jude staging for pediatric)

| Stage | Definition |
|-------|-----------|
| I | Single nodal or extranodal tumor; not mediastinal or abdominal |
| II | Multiple nodal/extranodal sites same side of diaphragm; resectable abdominal |
| III | Extensive abdominal, mediastinal, or ≥2 sites each side of diaphragm; unresectable abdominal |
| IV | CNS or BM involvement |

**Adult BL:** Lugano/Ann Arbor staging (I-IV); CNS involvement defined as CSF cytology +, intracranial disease, or cranial nerve palsies; BM involvement >25% blasts = L3-ALL (BL-leukemia); bulky disease (>10 cm), elevated LDH, and CNS/BM involvement = "high-risk" features.

### Treatment

**Risk-adapted DA-EPOCH-R (adults, low-risk/high-risk):**
EPOCH = etoposide + prednisone + vincristine + cyclophosphamide + doxorubicin (96-hour continuous infusion); DA (dose-adjusted): escalate or reduce doses each cycle based on nadir ANC; + R = rituximab Day 1 of each cycle; CNS prophylaxis: intrathecal MTX+cytarabine during each cycle (7 doses for low-risk, 8 for high-risk) OR high-dose systemic MTX (alternative); NCI multicenter study [^roschewski-2020-da-epoch-r-bl]: low-risk (LDH ≤normal, single extranodal mass, Ann Arbor I/II): DA-EPOCH-R × 3 cycles → 4-year EFS 100%, PFS 100%; high-risk (all other): DA-EPOCH-R × 6 cycles → 4-year EFS 87%, PFS 82%; peripheral neuropathy (vincristine), hematologic toxicity manageable.

**R-CODOX-M/IVAC (Magrath regimen):**
Alternate cycles: CODOX-M (cyclophosphamide/vincristine/doxorubicin/high-dose MTX) and IVAC (ifosfamide/etoposide/high-dose AraC) × 3-4 cycles total (1-2 of each); rituximab added; low-risk BL: R-CODOX-M × 3 cycles; high-risk: R-CODOX-M/IVAC alternating × 4 cycles; reported EFS ~87-92% in low/intermediate-risk; more toxicity (severe mucositis, cytopenias, CNS toxicity from intrathecal chemo) than DA-EPOCH-R; choice between DA-EPOCH-R and R-CODOX-M/IVAC is center-dependent.

**Pediatric LMB chemotherapy (rituximab + LMB):**
FAB/LMB protocols stratified by risk group (A/B/C):
- Group A (Stage I/II, complete resection): COPAM (cyclophosphamide, vincristine, prednisone, doxorubicin, MTX) × 2 cycles; 5-year EFS >98%
- Group B (non-resected Stage II-III, no CNS/BM): COP induction → COPADM × 2 → CYVE consolidation × 2 → maintenance; 5-year EFS ~85-90%
- Group C (CNS+/BM+): High-intensity with HD-MTX and HD-AraC
- Inter-B-NHL Ritux 2010 (rituximab addition to Group B/C): 3-year EFS 93.9% vs 79.8% (HR 0.33, p<0.001 in high-risk group B/C) [^minard-colin-2017-inter-b-nhl-ritux]; rituximab standard of care for pediatric BL >1 year of age.

**HIV-associated BL:**
Treat as non-HIV BL if CD4 >100 and performance status allows; rituximab + DA-EPOCH: similar outcomes to HIV-negative with modern ART; maintain ART throughout therapy; avoid prophylactic dose-reductions; PCP/toxoplasma prophylaxis; G-CSF support.

### Relapsed/refractory Burkitt lymphoma

**Prognosis:** Extremely poor; most relapse within 12 months of initial CR; survival <20% at 2 years.

**Salvage options:**
- R-ICE (rituximab+ifosfamide+carboplatin+etoposide): ORR ~40-50%
- R-DHAP (rituximab+dexamethasone+high-dose AraC+cisplatin): ORR ~30-40%
- DA-EPOCH-R → allo-SCT if CR2 achievable: only potentially curative approach
- Obinutuzumab (Type II anti-CD20): substituted for rituximab; limited additional benefit
- CAR-T cell therapy: tisagenlecleucel/axicabtagene-ciloleucel: Phase 2 data in R/R HGBL (including BL) — ORR ~40-50%; BL included in large cell lymphoma approvals; limited data specifically in BL
- Olaparib: BRCA-pathway downregulation by ARF loss → potential HR defect → PARP inhibitor sensitivity (preclinical data; no clinical approval)
- Obinutuzumab + venetoclax: BCL2-negative BL → venetoclax less rational; BCL2-low BL may not respond; not standard

### BL vs Double-Hit Lymphoma (DHL)

Critical diagnostic distinction:
| Feature | Burkitt Lymphoma | Double-Hit LBCL |
|---------|-----------------|-----------------|
| Ki-67 | ~100% | 40-90% |
| BCL2 IHC | Negative | Positive (usually) |
| BCL2 translocation | Absent | Present (usually) |
| MYC | t(8;IG) | MYC translocation ± any partner |
| Morphology | Classic intermediate/monomorphic | Often DLBCL-like |
| Prognosis | Curable with intensive regimens | Poor; DA-EPOCH-R or R-CHOP+venetoclax |

FISH for MYC, BCL2, and BCL6 is essential; if BCL2 FISH negative and Ki-67 ~100% → BL (treat with BL regimen, NOT CHOP); DHL → DA-EPOCH-R ± venetoclax or clinical trial.

## Connections

- `connects-to` → **[NPM1](../../03-molecular/npm1/README.md)** — NPM1 is a nucleolar ribosome biogenesis factor essential in Ki-67~100% BL cells; NPM1 sequesters ARF → attenuates the MYC → ARF → p53 checkpoint; NPM1 overexpression in high-grade B-cell lymphomas; NPM1 phosphorylation by CDK2 regulates centrosome duplication in BL.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — MYC translocation [t(8;14) ~80%, t(2;8) ~15%, t(8;22) ~5%] is the defining alteration of Burkitt lymphoma; MYC juxtaposed to Ig loci → constitutive transcription; MYC drives near-100% Ki-67; BET bromodomain inhibitors suppress MYC in BL preclinically.
- `connects-to` → **[P53](../../03-molecular/p53/README.md)** — BL cells silence ARF (CDKN2A deletion ~50%) to evade MYC → ARF → p53 checkpoint; TP53 mutations in ~30% BL at relapse; p53 pathway is intact in most primary BL; MDM2 inhibitors (idasanutlin) + DA-EPOCH-R explored in Phase 1 for relapsed/refractory BL.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — BL tumor microenvironment is immune-poor; PD-L1 expression is variable; EBV+ endemic BL has more immune infiltrate than sporadic BL; PD-1 blockade combined with rituximab-based therapy in early trials for relapsed/refractory high-grade B-cell lymphoma.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — BL arises from germinal center B cells with MYC translocation to Ig loci (IGH/IGK/IGL) during VDJ recombination or class-switch recombination; CD19+/CD20+/CD10+/BCL6+/BCL2- immunophenotype reflects GC B-cell origin; MYC drives near-100% Ki-67 in these rapidly cycling B cells.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — BL originates in germinal center B cells; MYC translocation arises from AID-mediated DSBs at Ig loci during class-switch recombination; CD10+/BCL6+ confirms GC origin; EBV+ endemic BL expresses BCL6 and EBNA-1 in Latency I, exploiting GC biology for viral persistence.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — CD20 (MS4A1) is expressed on all BL cells; rituximab (anti-CD20 mAb) is standard in adult DA-EPOCH-R and pediatric LMB regimens; Inter-B-NHL Ritux 2010: rituximab addition → 3-year EFS 93.9% vs 79.8% (HR 0.33, p<0.001) in high-risk pediatric BL; obinutuzumab explored in R/R BL.
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — Epstein-Barr virus is found in nearly all endemic (African) Burkitt lymphoma and a minority of sporadic cases: the virus persists in germinal-center B cells in Latency I, and its EBNA/miRNA program helps the MYC-translocated cell evade apoptosis and immune clearance.
- `connects-to` → **[Plasmodium falciparum](../../../02-pathogen/04-parasites/plasmodium-falciparum/README.md)** — Holoendemic Plasmodium falciparum malaria is the geographic cofactor for endemic Burkitt lymphoma: chronic malaria expands germinal-center B cells and induces AID, raising the chance of the MYC-Ig translocation, while malaria-driven immune dysregulation reactivates EBV.
- `connects-to` → **[Diffuse Large B-Cell Lymphoma](../dlbcl/README.md)** — Burkitt lymphoma must be separated from DLBCL and double-hit large-cell lymphoma: Burkitt has a sole MYC translocation, ~100% Ki-67, and is BCL-2-negative, so FISH for MYC/BCL-2/BCL-6 is essential — a Burkitt diagnosis mandates intensive regimens (DA-EPOCH-R), not R-CHOP.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — Burkitt lymphoma is an AIDS-defining cancer: HIV-driven immunosuppression and chronic B-cell activation raise Burkitt risk even at preserved CD4 counts—so a fast-growing lymphoma in an HIV-positive patient is Burkitt until proven otherwise.
- `connects-to` → **[Follicular Lymphoma](../follicular-lymphoma/README.md)** — Burkitt and follicular lymphoma are both germinal-center B-cell tumors but opposite in tempo: Burkitt is MYC-driven, near-100% Ki67, doubles in a day and is curable with intensive chemo, while BCL2-driven follicular lymphoma is indolent, incurable, and waxes over years.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — The 'starry sky' appearance pathognomonic of Burkitt lymphoma comes from tingible-body macrophages: scattered pale macrophages engulfing apoptotic debris from the explosively proliferating MYC-driven B cells stand out against the dark sheet of tumor.
- `connects-to` → **[Malaria](../malaria/README.md)** — Endemic Burkitt lymphoma is malaria-driven: chronic Plasmodium falciparum infection drives intense B-cell proliferation and weakens control of co-infecting Epstein-Barr virus, together promoting the MYC translocation that causes the jaw and abdominal tumors of African children.
- `connects-to` → **[Hodgkin Lymphoma](../hodgkin-lymphoma/README.md)** — Burkitt and Hodgkin lymphoma are both EBV-associated but biologically opposite: Burkitt is a fast MYC-driven mature B-cell tumor curable with intensive chemo, while Hodgkin is a CD30+ Reed-Sternberg-cell lymphoma with a rich reactive infiltrate, treated differently with ABVD.
- `connects-to` → **[Mantle Cell Lymphoma](../mantle-cell-lymphoma/README.md)** — Burkitt and mantle cell lymphoma are aggressive B-cell lymphomas defined by single translocations: Burkitt's t(8;14) drives MYC, mantle cell's t(11;14) drives cyclin D1—but Burkitt is curable while mantle cell is aggressive yet incurable, a key prognostic split.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Burkitt lymphoma is MYC-driven, not BCL2-driven—a key contrast: classic Burkitt carries the MYC translocation and is BCL2-negative, so a tumor with both MYC and BCL2 rearrangements is instead a more aggressive double-hit high-grade lymphoma, not true Burkitt.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Burkitt lymphoma is a germinal-center B cell frozen short of plasma-cell fate: the MYC-driven clone proliferates explosively (near-100% Ki-67) instead of maturing into antibody-secreting plasma cells—so its hallmark is runaway growth, the fastest-doubling human tumor.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Burkitt lymphoma exposes the immune system's role in cancer control: it surges in immunodeficiency (HIV) and where chronic malaria and EBV exhaust immune surveillance—so endemic Burkitt is partly a cancer of weakened immune defense against EBV-driven B cells.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Burkitt lymphoma is an aggressive cancer of the lymphatic system: the endemic form classically erupts as a jaw or facial mass while sporadic disease hits abdominal lymph nodes and bowel, reflecting its origin in germinal-center B cells of lymphoid tissue.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Burkitt lymphoma can flood the bone marrow and blood: with the fastest doubling time of any human tumor, it readily spills into marrow as a leukemic phase, so it overlaps clinically with acute leukemia and demands immediate intensive chemotherapy.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Burkitt lymphoma is the textbook cause of tumor lysis syndrome threatening the kidney: its explosive growth and rapid chemo-induced cell death dump uric acid, potassium and phosphate that can crystallize and cause acute kidney injury without aggressive prophylaxis.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Sporadic Burkitt lymphoma favors the abdomen: it typically presents as a fast-growing ileocecal or bowel mass causing obstruction or intussusception, so a rapidly enlarging abdominal tumor in a child is a classic Burkitt presentation.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Burkitt lymphoma is held in check by cytotoxic T cells: EBV-specific T-cell surveillance normally controls infected B cells, so when HIV or immunosuppression weakens it, EBV-driven Burkitt emerges—underpinning T-cell-based immunotherapies.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Burkitt lymphoma's abdominal disease often centers on the spleen and viscera: this fast-growing lymphoma seeds the spleen, liver, and mesentery, so bulky intra-abdominal and splenic involvement is typical of the sporadic form.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Burkitt lymphoma is the textbook cause of tumor lysis syndrome: its explosively dividing cells burst and dump phosphate into the blood, and the resulting hyperphosphatemia binds calcium and crashes the kidneys—why hydration and rasburicase precede therapy.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — NK cells help police the EBV behind Burkitt lymphoma: natural killer cells kill virus-infected B cells before they transform, so when immune surveillance fails—in HIV or malaria-driven immune exhaustion—EBV-driven Burkitt is far more likely.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Malaria-driven Treg expansion fuels endemic Burkitt: chronic falciparum infection ramps up regulatory T cells that suppress immunity, loosening control of EBV-infected B cells and helping the MYC-translocated tumor emerge in African children.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Burkitt is the textbook tumor-lysis cancer: its blistering growth means chemotherapy bursts huge numbers of cells at once, dumping potassium into the blood, so dangerous hyperkalemia and arrhythmia must be anticipated and prevented from the first dose.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Burkitt lymphoma readily seeds the brain: it has a strong tendency to spread to the central nervous system and meninges, so treatment includes CNS-directed chemotherapy and prophylaxis to reach this sanctuary the bloodstream drugs miss.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — MYC rewires Burkitt's metabolism through the PI3K-mTOR axis: the driving oncogene partners with mTOR signaling to fuel the relentless growth and protein synthesis, making this pathway an attractive target alongside chemotherapy.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Burkitt's furious metabolism can acidify the blood: its MYC-driven glycolysis pours out lactic acid, so a rare type B lactic acidosis can appear from the tumor burden alone, even before chemotherapy begins.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Sporadic Burkitt lymphoma fills the abdomen: it forms bulky masses that involve the bowel, liver, and ovaries, so abdominal pain and a rapidly growing belly mass are common presentations in children.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Burkitt lymphoma blazes on a PET scan: its near-100% proliferation rate makes it intensely avid for the radiotracer's photons, so PET imaging vividly stages this fastest-growing human tumor.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Burkitt's massive tumor lysis crashes calcium: the flood of phosphate from dying cells binds calcium and drops it, risking tetany and arrhythmia alongside the high potassium of the emergency.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Endemic Burkitt classically swells the jaw and orbit: rapidly growing facial and eye-socket masses are the hallmark presentation in the African malaria belt where the EBV-driven form arises.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — MYC floors the cell cycle in Burkitt: it drives cyclin D and CDK4/6 to push cells relentlessly from rest into division, powering the roughly one-day doubling time of this fastest-growing tumor.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows Burkitt's 'starry sky': sheets of blasts with lipid-vacuoled cytoplasm are dotted with tingible-body macrophages clearing the debris of cells dying as fast as the tumor divides.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Sporadic Burkitt erupts in the abdomen: it forms bulky masses in the stomach, ileocecum, and surrounding organs, the GI presentation that distinguishes it from the jaw tumors of the endemic African form.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — Abdominal Burkitt seeds the retroperitoneum: its explosive growth fills the abdomen and can involve the adrenals, kidneys, and ovaries, masses that swell almost visibly day by day.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — An antibody is part of the cure: rituximab against CD20 added to intensive chemotherapy markedly improves outcomes in Burkitt lymphoma, harnessing the immune system against the malignant B cells.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Burkitt readily invades the nervous system: its high rate of CNS spread demands intrathecal chemotherapy as prophylaxis, while the vincristine in its regimens poisons peripheral neurons into a dose-limiting neuropathy.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Burkitt carries the highest risk of tumor lysis syndrome: as its fast-dividing cells burst under chemotherapy, potassium, phosphate, and uric acid surge while calcium and magnesium swing — a metabolic storm that can stop the heart and shut the kidneys.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — MYC needs a partner in Burkitt: recurrent TCF3 and ID3 mutations switch on tonic B-cell-receptor signaling through PI3K-AKT, which cooperates with the translocated MYC to drive the tumor — a survival pathway being targeted by PI3K inhibitors.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Sporadic Burkitt favors the abdomen and gonads: bulky ileocecal masses and ovarian or testicular deposits are common presentations, and the intensive multi-agent chemotherapy that cures it can leave survivors infertile.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Marrow takeover drops the red cells: when Burkitt floods the bone marrow it crowds out normal blood production, and the resulting anemia — deepened by chemotherapy — leaves patients pale and fatigued during treatment.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — Sporadic Burkitt strikes the gut: it classically presents as a bulky ileocecal mass in the small bowel, the fastest-growing human tumor erupting as an abdominal emergency that can obstruct or perforate.
- `connects-to` → **[Acute Lymphoblastic Leukemia](../all/README.md)** — Burkitt has a leukemic twin: when it floods the blood and marrow it becomes mature B-cell acute lymphoblastic leukemia (the old L3 ALL), treated on the same intensive Burkitt protocols.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Its birthplace is the germinal center's scaffold: follicular dendritic cells present antigen to the rapidly dividing B cells there, the microenvironment from which the MYC-driven Burkitt clone arises.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Cure comes at the cost of deep immunosuppression: the intensive multi-agent chemotherapy for Burkitt produces severe neutropenia, so febrile neutropenia and sepsis are among the leading treatment-related dangers.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Burkitt is the NF-κB-independent lymphoma: unlike activated B-cell DLBCL it survives on tonic BCR/PI3K and MYC rather than chronic NF-κB signaling, a distinction that shapes which targeted therapies can work.
- `connects-to` → **[Multiple Myeloma](../multiple-myeloma/README.md)** — Two ends of the B-cell lineage: Burkitt is an aggressive germinal-center B-cell tumor while myeloma is a malignancy of terminal plasma cells, contrasting points on the maturation path that both rely on MYC dysregulation.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — The fastest tumor floods the kidneys when it dies: Burkitt's explosive proliferation gives it the highest tumor-lysis-syndrome risk of any cancer, releasing urate and phosphate that injure the kidneys into acute and sometimes chronic kidney disease.
- `connects-to` → **[Disseminated Intravascular Coagulation](../disseminated-intravascular-coagulation/README.md)** — Massive tumor turnover can ignite clotting: the high cell burden and rapid lysis of Burkitt lymphoma can release procoagulant material that triggers disseminated intravascular coagulation, especially around the start of chemotherapy.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — An aggressive lymphoma that clots: like other high-grade cancers, Burkitt raises venous thromboembolism risk through tumor-driven hypercoagulability, compounded by central venous catheters and immobility during intensive treatment.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Intensive chemo strips the lung's defenses: the dose-dense regimens curing Burkitt cause profound neutropenia, letting inhaled Aspergillus invade as pulmonary aspergillosis, a feared infectious complication.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — Immunosuppression opens the lung to it: the intensive chemotherapy — and in HIV-associated cases the underlying immunodeficiency — deplete T-cell defenses, so Pneumocystis prophylaxis accompanies Burkitt treatment.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Marrow takeover and chemo blunt the count: Burkitt frequently infiltrates the bone marrow, and with its inflammatory cytokines and myelosuppressive therapy this produces anemia carrying a chronic-disease component.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its anthracyclines strain the heart: the doxorubicin in the intensive CODOX-M/IVAC and DA-EPOCH regimens for Burkitt is dose-dependently cardiotoxic, risking cardiomyopathy and heart failure.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Vincristine leaves the nerves raw: the vinca alkaloid central to Burkitt chemotherapy causes a dose-limiting peripheral neuropathy with numbness and neuropathic pain.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A sudden, explosive cancer weighs on mood: Burkitt's rapid onset, urgent intensive chemotherapy and life-threatening course impose a heavy psychological burden contributing to depression.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^roschewski-2020-da-epoch-r-bl]: Roschewski M, Dunleavy K, Abramson JS, et al. Multicenter study of risk-adapted therapy with dose-adjusted EPOCH-R in adults with untreated Burkitt lymphoma. *J Clin Oncol.* 2020;38(22):2519-2529. [doi:10.1200/JCO.19.03259](https://doi.org/10.1200/JCO.19.03259) · [PubMed 32530765](https://pubmed.ncbi.nlm.nih.gov/32530765/)
[^minard-colin-2017-inter-b-nhl-ritux]: Minard-Colin V, Auperin A, Pillon M, et al. Rituximab for children and adolescents with high-risk B-cell non-Hodgkin lymphoma: results of the randomized Inter-B-NHL Ritux 2010 trial. *J Clin Oncol.* 2022;40(22):2458-2471. [doi:10.1200/JCO.21.01940](https://doi.org/10.1200/JCO.21.01940) · [PubMed 35436151](https://pubmed.ncbi.nlm.nih.gov/35436151/)

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
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Sporadic Burkitt erupts in the abdomen: it commonly presents as a bulky ileocecal or abdominal mass causing pain, obstruction or intussusception, and its chemotherapy adds mucositis and typhlitis."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "The endemic form attacks the jaw: African endemic Burkitt lymphoma classically presents as a rapidly growing tumour of the jaw and facial bones, distorting the maxilla and mandible."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Intensive chemo reawakens shingles: the dose-dense multi-agent chemotherapy for Burkitt lymphoma deeply suppresses T-cell immunity, allowing latent varicella-zoster to reactivate."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It is the classic cause of tumour lysis: Burkitt's huge tumour burden and rapid turnover release urate and potassium, causing acute kidney injury, while bulky abdominal disease can obstruct the ureters."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It readily seeds the brain's linings: Burkitt lymphoma has a high risk of central nervous system spread with leptomeningeal disease and cranial nerve palsies, so intrathecal prophylaxis is standard."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Its abdominal predilection reaches endocrine glands: Burkitt lymphoma can infiltrate the adrenals, thyroid and pancreas, occasionally causing endocrine dysfunction such as adrenal insufficiency."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Treatment and tumour bulk burden the heart: intensive anthracycline chemotherapy risks cardiomyopathy, while tumour lysis syndrome's hyperkalaemia can cause fatal arrhythmia in this fastest-growing human tumour."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Bulky disease fills the chest: abdominal and mediastinal Burkitt masses can compress the airway and cause pleural effusions, while the deep immunosuppression of treatment invites pneumonia."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Therapy marks the skin: the dose-intensive regimens for Burkitt lymphoma cause alopecia and mucositis, and rare cutaneous infiltration can occur."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Intensive chemo cures it: Burkitt lymphoma, the fastest-growing human tumour, is treated with short intensive multi-agent chemotherapy plus CNS prophylaxis, curing most patients."
  - target: 02-pathogen/01-viruses/hiv-1
    relation: connects-to
    note: "Immunodeficiency unleashes the clone: HIV is a major cause of Burkitt lymphoma, an AIDS-defining cancer arising as falling immunity permits EBV-driven B-cell proliferation."
  - target: 03-medicine/01-modern/13-cancer/car-t
    relation: connects-to
    note: "Engineered cells for relapse: CD19-directed CAR-T therapy is an option for relapsed or refractory Burkitt and other aggressive B-cell lymphomas after chemotherapy fails."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Rituximab cemented the cure: adding the anti-CD20 antibody rituximab to intensive chemotherapy markedly improved survival in Burkitt lymphoma, and its MYC-driven biology is a target of ongoing precision approaches."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Endemic Burkitt deforms the jaw: in equatorial Africa, EBV- and malaria-associated Burkitt lymphoma classically presents as a rapidly growing jaw or facial-bone mass in children, distorting the cortical bone."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Sporadic Burkitt fills the abdomen: outside the endemic belt, Burkitt lymphoma typically presents as a bulky ileocaecal mass in the bowel wall, causing obstruction or intussusception from the intestinal lining."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Tumour lysis nephropathy: Burkitt's explosive growth causes tumour lysis syndrome, whose urate and phosphate crystals obstruct the glomerulus and tubules, triggering acute kidney injury at presentation."
  - target: 01-human/07-system/cll
    relation: connects-to
    note: "Opposite tempos of B-cell cancer: Burkitt is the fastest-growing human tumour, MYC-driven and doubling within a day, whereas chronic lymphocytic leukaemia is the most indolent—the extremes of mature B-cell malignancy."
  - target: 01-human/07-system/pcnsl
    relation: connects-to
    note: "Aggressive B-cell lymphomas that seek sanctuary sites: Burkitt readily seeds the CNS and meninges, requiring intrathecal prophylaxis, a behaviour it shares with primary CNS lymphoma."
  - target: 01-human/07-system/cytokine-storm
    relation: connects-to
    note: "Acute treatment storms: Burkitt's explosive growth causes severe tumour-lysis syndrome at induction, and CD19 immunotherapies add cytokine release syndrome—two systemic emergencies of its therapy."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Abdominal and visceral bulk: sporadic Burkitt lymphoma forms large abdominal masses that involve the liver, infiltrating the hepatic lobules alongside the bowel and mesentery."
  - target: 01-human/07-system/gvhd
    relation: connects-to
    note: "EBV-driven B-cell proliferation: like the post-transplant lymphoproliferative disease that complicates GVHD-prone transplants, Burkitt lymphoma exploits EBV and impaired immunity to drive B-cell growth."
  - target: 01-human/03-molecular/foxo1
    relation: connects-to
    note: "Recurrent driver mutation: activating FOXO1 mutations are among the most frequent secondary lesions in Burkitt lymphoma, cooperating with MYC to sustain the malignant germinal-centre B cell."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Germinal-centre epigenetics: EZH2 enforces the proliferative, anti-differentiation programme of germinal-centre B cells from which Burkitt lymphoma arises, a shared lever across GC-derived lymphomas."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Germinal-centre help: follicular helper T cells deliver the CD40 and cytokine signals that drive germinal-centre B-cell proliferation, the very reaction hijacked in Burkitt lymphomagenesis."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cell-cycle acceleration: MYC translocation in Burkitt lymphoma drives cyclin D and the cell-cycle machinery, producing the near-100% proliferative fraction that defines the disease."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Replicative immortality: TERT activation maintains telomeres in the explosively dividing Burkitt cells, sustaining the limitless proliferation MYC unleashes."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Glycolytic metabolism: MYC and HIF-1α together drive the aerobic glycolysis (Warburg effect) that fuels the extreme proliferative rate of Burkitt lymphoma."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Tonic BCR-PI3K: chronic tonic B-cell-receptor signalling through PI3K cooperates with MYC in Burkitt lymphoma, a recurrently mutated pathway essential for the malignant B cells' survival."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Tumour lysis syndrome: the explosive cell turnover of Burkitt lymphoma floods the blood with purines that xanthine oxidase converts to uric acid, causing the tumour lysis syndrome that rasburicase and allopurinol prevent."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Apoptotic priming: high MYC primes Burkitt cells for apoptosis, so chemotherapy readily triggers caspase-3-mediated cell death — the basis of the tumour's striking chemosensitivity and curability."
  - target: 01-human/03-molecular/btk
    relation: connects-to
    note: "Tonic BCR signalling: BTK transduces the tonic B-cell-receptor signal that, with PI3K, sustains Burkitt lymphoma — a tonic (rather than chronic-active) BCR dependency distinct from that of other aggressive lymphomas."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Marrow and CNS spread: CXCR4 on Burkitt cells follows CXCL12 gradients into the bone marrow and central nervous system, the dissemination pattern that mandates intensive CNS-directed prophylaxis in treatment."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "p53 restraint: MDM2 restrains the strong pro-apoptotic p53 response that MYC overexpression provokes, so the MDM2-p53 balance shapes how readily Burkitt cells die — relevant when TP53 is intact."
  - target: 01-human/03-molecular/lmp1
    relation: connects-to
    note: "EBV cofactor: endemic Burkitt lymphoma is driven by Epstein-Barr virus together with chronic malaria, and the EBV-infected germinal-centre B cell is the cell of origin in which the MYC translocation arises in the African childhood form."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Translocation and BCR: the defining t(8;14) places MYC under the control of the immunoglobulin heavy-chain enhancer, driving its overexpression, and tonic B-cell-receptor signalling further sustains the Burkitt cell — the basis for BTK and PI3K targeting."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Immunotherapy: CD19-directed CAR-T cells and the CD19-CD3 bispecific blinatumomab redirect cytotoxic T cells to kill Burkitt cells through perforin and granzyme, an emerging option in relapsed or refractory disease."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Forced S-phase: MYC transactivates E2F1, and the two cooperate to drive cell-cycle entry alongside the cyclin-D1/CDK4-6 axis already mapped, underpinning Burkitt lymphoma's extreme proliferative rate."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "Cooperating PI3K hit: PTEN loss activates the PI3K-AKT-mTOR pathway (PIK3CA, AKT and mTOR already mapped), a tonic-BCR-driven second hit that cooperates with the MYC translocation in Burkitt lymphomagenesis."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "ARF-p53 backup: the CDKN2A locus encodes p14ARF, which normally stabilises p53 against MDM2 (both mapped); its loss removes the apoptotic brake on MYC-driven proliferation in Burkitt lymphoma."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "BCR-MAPK proliferation: tonic B-cell-receptor and RAS signalling converge on ERK1/2 MAPK to drive the proliferation that cooperates with the MYC translocation in Burkitt lymphoma."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "RAS cooperation: activating RAS-pathway mutations recurrently accompany the MYC translocation in Burkitt lymphoma, reinforcing the proliferative and survival signalling of the tumour."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Cell-cycle brake: the RB1-E2F checkpoint (E2F1, CDK4/6 and cyclin-D already mapped) restrains S-phase entry, and its inactivation removes a brake on the MYC-driven proliferation of Burkitt lymphoma."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK-STAT signalling contributes to the cytokine-responsive proliferation of Burkitt lymphoma cells."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING participates in the response to EBV (LMP1 mapped) in EBV-associated Burkitt lymphoma."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 modulates apoptosis resistance and the microenvironment interactions of Burkitt lymphoma cells."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6/IL-10-STAT3 signalling supports the survival of Burkitt lymphoma cells, exploited by the Epstein-Barr-virus-associated subtype."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antiviral and antitumour immune response to the Epstein-Barr-virus-driven Burkitt lymphoma."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling normally restrains B-cell proliferation, a brake overridden by the MYC translocation of Burkitt lymphoma."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β regulates MYC phosphorylation and turnover (MYC already mapped) and the survival signaling of Burkitt lymphoma cells."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins from infiltrating myeloid cells shape the inflammatory microenvironment of Burkitt lymphoma."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "NOTCH signaling, recurrently mutated in a subset of Burkitt lymphoma, contributes to its pathogenesis."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family (LYN) kinase signaling downstream of the tonic B-cell receptor supports the survival of the MYC-driven cells of Burkitt lymphoma."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of Burkitt lymphoma."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and metabolic-stress management of the highly proliferative MYC-driven cells of Burkitt lymphoma."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of the highly proliferative cells of Burkitt lymphoma."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-family chemokine signaling (CXCL12/CXCR4 already mapped) participates in the trafficking of Burkitt lymphoma cells."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic dysregulation of Burkitt lymphoma."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of Burkitt lymphoma."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of Burkitt lymphoma."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of Burkitt lymphoma."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of Burkitt lymphoma."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of Burkitt lymphoma."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling downstream of the B-cell receptor participates in the survival signaling of Burkitt lymphoma."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "EBV immune escape: MHC class II presentation of Epstein-Barr-virus antigens (LMP1 already mapped) shapes the immune control of EBV-driven Burkitt lymphoma, and downregulation of antigen presentation is one route by which the tumour evades T cells."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Cellular immunotherapy: IL-2-driven T-cell expansion supports the CD19-directed CAR-T and EBV-specific T-cell therapies (perforin already mapped) explored for relapsed and immunodeficiency-associated Burkitt lymphoma."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "Checkpoint context: CTLA-4 restrains the anti-tumour T-cell response, and its role in immune tolerance is relevant to the impaired EBV surveillance underlying the endemic and immunodeficiency-associated forms of Burkitt lymphoma."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Marrow involvement: bone-marrow infiltration by Burkitt lymphoma and its intensive chemotherapy lower haemoglobin, and the resulting anaemia, with the other cytopenias, adds to the acute morbidity of this rapidly growing tumour."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Tumour-lysis acidosis: the extreme proliferation of Burkitt lymphoma, lysed by chemotherapy, releases acids that, with lactate from the metabolic stress, produce the metabolic acidosis of tumour-lysis syndrome (potassium and urate already mapped)."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Anthracycline cardiotoxicity: the intensive anthracycline-containing chemotherapy that cures most Burkitt lymphoma is cardiotoxic, and troponin elevation helps detect the myocardial injury threatening long-term survivors."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10, whose viral homologue is encoded by the Epstein-Barr virus (LMP1 already mapped) of endemic Burkitt lymphoma, dampens the anti-tumour T-cell response (PD-1 already mapped), part of the immune evasion of the tumour."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Tumour angiogenesis: VEGF-driven angiogenesis supplies the extraordinarily proliferative Burkitt lymphoma (HIF-1-alpha already mapped), part of the microenvironment sustaining the fastest-growing human tumour."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Transfusion and anaemia: the anaemia of marrow involvement and intensive chemotherapy (haemoglobin already mapped) requires red-cell transfusion in Burkitt lymphoma, whose repeated support can load the body with iron."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "CNS involvement: Burkitt lymphoma has a high risk of central nervous system involvement and relapse, requiring intrathecal chemotherapy prophylaxis to the brain and meninges as part of curative therapy."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Tumour-lysis hyperkalaemia: the massive, rapid cell turnover of Burkitt lymphoma (xanthine oxidase and urate already mapped) releases potassium, the hyperkalaemia of tumour-lysis syndrome being a life-threatening metabolic emergency."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Starry-sky macrophages: IL-4 polarises the tingible-body macrophages that engulf the abundant apoptotic cells, producing the classic 'starry-sky' appearance (IL-10 already mapped) of the M2 macrophages in Burkitt lymphoma."
  - target: 01-human/07-system/hiv
    relation: connects-to
    note: "AIDS-associated lymphoma: Burkitt lymphoma is an AIDS-defining lymphoma, HIV predisposing to it via the immune dysregulation, a form distinct from the endemic EBV/malaria (LMP1 already mapped) variant."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 starry-sky arm: IL-13, with IL-4 (already mapped), supports the M2 tingible-body macrophage (already mapped) 'starry-sky' phenotype of Burkitt lymphoma."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Adipokine microenvironment: leptin signals from the adipose and marrow microenvironment to the aggressive lymphoma cells, part of the metabolic context (xanthine oxidase already mapped) of Burkitt lymphoma."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine microenvironment: adiponectin, with leptin (already mapped), is part of the adipose/marrow-microenvironment adipokine signalling to the aggressive Burkitt lymphoma cells."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine microenvironment: resistin, with leptin and adiponectin (already mapped), completes the adipokine dimension of the microenvironment of Burkitt lymphoma."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "EBV antiviral interferon: the type-I interferon antiviral response to the EBV (LMP1 already mapped) is part of the host-virus biology of the endemic EBV-driven Burkitt lymphoma."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour/antiviral arm: the IFN-γ of the T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour and anti-EBV (LMP1 already mapped) immunity of Burkitt lymphoma."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of Burkitt lymphoma."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of Burkitt lymphoma."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the Burkitt-lymphoma microenvironment."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the Burkitt-lymphoma microenvironment."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of Burkitt lymphoma."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Rituximab CDC: the complement C5 (with C3 already mapped) is the effector of the complement-dependent cytotoxicity by which the anti-CD20 (already mapped) rituximab kills the Burkitt-lymphoma B cells (already mapped)."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling links the complement (C3 and C5 already mapped) to the myeloid inflammation of the Burkitt-lymphoma microenvironment."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the Burkitt-lymphoma cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), a resistance mechanism to the rituximab complement-dependent killing."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway of the anti-CD20 (already mapped) rituximab complement-dependent cytotoxicity against the Burkitt-lymphoma cells."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Microenvironment matricellular: osteopontin, a matricellular cytokine, is part of the inflammatory microenvironment of the highly proliferative Burkitt lymphoma."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "MYC-driven iron: transferrin, the iron carrier, supplies the high iron demand of the MYC-driven (already mapped) rapid proliferation of Burkitt lymphoma."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-TME axis: TSLP, from stromal cells and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2 immunosuppression of the Burkitt-lymphoma microenvironment."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-lymphoma axis: bradykinin, via B1/B2 receptors on tumour endothelium (already mapped) and mast cells (already mapped), amplifies the vascular permeability and the cytokine milieu of the Burkitt-lymphoma microenvironment."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Erythropoietic support: erythropoietin supports the management of the myelosuppressive-chemotherapy-induced anaemia of the intensive treatment of Burkitt lymphoma."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell lymphoma axis: histamine, from mast cells (already mapped) in the Burkitt-lymphoma microenvironment, amplifies the MYC-driven (already mapped) angiogenesis (already mapped) and the immunosuppressive cytokine milieu of the tumour stroma."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian-lymphoma axis: melatonin, via MT1/MT2 receptors and its radical-scavenging activity, modulates the oxidative stress of the MYC-driven (already mapped) rapid proliferation and the genomic instability of Burkitt lymphoma."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen-lymphoma axis: testosterone, via androgen receptors on tumour B-cells (already mapped) and stromal cells, modulates the sex-differential incidence and the immunosuppressive microenvironment of Burkitt lymphoma."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Burkitt serotonin: serotonin, via 5-HT receptors on macrophages (already mapped) and mast cells (already mapped), modulates the lymphoma TME; serotonin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) proliferative cascade of Burkitt lymphoma."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Burkitt prolactin: prolactin, via PRLR on macrophages (already mapped) and mast cells (already mapped), promotes lymphoma immune escape; hyperprolactinaemia amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of Burkitt lymphoma."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Burkitt oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates lymphoma TME inflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of Burkitt lymphoma."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Burkitt vasopressin: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates lymphoma TME immune tone; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of Burkitt lymphoma."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Burkitt selenium: selenium, as GPx in macrophages (already mapped) and mast cells (already mapped), scavenges ROS driving the lymphoma TME; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour-promoting cascade of Burkitt lymphoma."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Burkitt iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) and mast-cell (already mapped) immune function; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour-promoting cascade of Burkitt lymphoma."
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
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Sporadic Burkitt erupts in the abdomen: it commonly presents as a bulky ileocecal or abdominal mass causing pain, obstruction or intussusception, and its chemotherapy adds mucositis and typhlitis.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — The endemic form attacks the jaw: African endemic Burkitt lymphoma classically presents as a rapidly growing tumour of the jaw and facial bones, distorting the maxilla and mandible.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Intensive chemo reawakens shingles: the dose-dense multi-agent chemotherapy for Burkitt lymphoma deeply suppresses T-cell immunity, allowing latent varicella-zoster to reactivate.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It is the classic cause of tumour lysis: Burkitt's huge tumour burden and rapid turnover release urate and potassium, causing acute kidney injury, while bulky abdominal disease can obstruct the ureters.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It readily seeds the brain's linings: Burkitt lymphoma has a high risk of central nervous system spread with leptomeningeal disease and cranial nerve palsies, so intrathecal prophylaxis is standard.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Its abdominal predilection reaches endocrine glands: Burkitt lymphoma can infiltrate the adrenals, thyroid and pancreas, occasionally causing endocrine dysfunction such as adrenal insufficiency.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Treatment and tumour bulk burden the heart: intensive anthracycline chemotherapy risks cardiomyopathy, while tumour lysis syndrome's hyperkalaemia can cause fatal arrhythmia in this fastest-growing human tumour.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Bulky disease fills the chest: abdominal and mediastinal Burkitt masses can compress the airway and cause pleural effusions, while the deep immunosuppression of treatment invites pneumonia.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Therapy marks the skin: the dose-intensive regimens for Burkitt lymphoma cause alopecia and mucositis, and rare cutaneous infiltration can occur.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Intensive chemo cures it: Burkitt lymphoma, the fastest-growing human tumour, is treated with short intensive multi-agent chemotherapy plus CNS prophylaxis, curing most patients.
- `connects-to` → **[HIV-1](../../../02-pathogen/01-viruses/hiv-1/README.md)** — Immunodeficiency unleashes the clone: HIV is a major cause of Burkitt lymphoma, an AIDS-defining cancer arising as falling immunity permits EBV-driven B-cell proliferation.
- `connects-to` → **[CAR-T](../../../03-medicine/01-modern/13-cancer/car-t/README.md)** — Engineered cells for relapse: CD19-directed CAR-T therapy is an option for relapsed or refractory Burkitt and other aggressive B-cell lymphomas after chemotherapy fails.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Rituximab cemented the cure: adding the anti-CD20 antibody rituximab to intensive chemotherapy markedly improved survival in Burkitt lymphoma, and its MYC-driven biology is a target of ongoing precision approaches.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Endemic Burkitt deforms the jaw: in equatorial Africa, EBV- and malaria-associated Burkitt lymphoma classically presents as a rapidly growing jaw or facial-bone mass in children, distorting the cortical bone.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Sporadic Burkitt fills the abdomen: outside the endemic belt, Burkitt lymphoma typically presents as a bulky ileocaecal mass in the bowel wall, causing obstruction or intussusception from the intestinal lining.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Tumour lysis nephropathy: Burkitt's explosive growth causes tumour lysis syndrome, whose urate and phosphate crystals obstruct the glomerulus and tubules, triggering acute kidney injury at presentation.
- `connects-to` → **[CLL](../cll/README.md)** — Opposite tempos of B-cell cancer: Burkitt is the fastest-growing human tumour, MYC-driven and doubling within a day, whereas chronic lymphocytic leukaemia is the most indolent—the extremes of mature B-cell malignancy.
- `connects-to` → **[PCNSL](../pcnsl/README.md)** — Aggressive B-cell lymphomas that seek sanctuary sites: Burkitt readily seeds the CNS and meninges, requiring intrathecal prophylaxis, a behaviour it shares with primary CNS lymphoma.
- `connects-to` → **[Cytokine Storm](../cytokine-storm/README.md)** — Acute treatment storms: Burkitt's explosive growth causes severe tumour-lysis syndrome at induction, and CD19 immunotherapies add cytokine release syndrome—two systemic emergencies of its therapy.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Abdominal and visceral bulk: sporadic Burkitt lymphoma forms large abdominal masses that involve the liver, infiltrating the hepatic lobules alongside the bowel and mesentery.
- `connects-to` → **[GVHD](../gvhd/README.md)** — EBV-driven B-cell proliferation: like the post-transplant lymphoproliferative disease that complicates GVHD-prone transplants, Burkitt lymphoma exploits EBV and impaired immunity to drive B-cell growth.
- `connects-to` → **[FOXO1](../../03-molecular/foxo1/README.md)** — Recurrent driver mutation: activating FOXO1 mutations are among the most frequent secondary lesions in Burkitt lymphoma, cooperating with MYC to sustain the malignant germinal-centre B cell.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Germinal-centre epigenetics: EZH2 enforces the proliferative, anti-differentiation programme of germinal-centre B cells from which Burkitt lymphoma arises, a shared lever across GC-derived lymphomas.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Germinal-centre help: follicular helper T cells deliver the CD40 and cytokine signals that drive germinal-centre B-cell proliferation, the very reaction hijacked in Burkitt lymphomagenesis.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cell-cycle acceleration: MYC translocation in Burkitt lymphoma drives cyclin D and the cell-cycle machinery, producing the near-100% proliferative fraction that defines the disease.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Replicative immortality: TERT activation maintains telomeres in the explosively dividing Burkitt cells, sustaining the limitless proliferation MYC unleashes.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Glycolytic metabolism: MYC and HIF-1α together drive the aerobic glycolysis (Warburg effect) that fuels the extreme proliferative rate of Burkitt lymphoma.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — Tonic BCR-PI3K: chronic tonic B-cell-receptor signalling through PI3K cooperates with MYC in Burkitt lymphoma, a recurrently mutated pathway essential for the malignant B cells' survival.
- `connects-to` → **[Xanthine Oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Tumour lysis syndrome: the explosive cell turnover of Burkitt lymphoma floods the blood with purines that xanthine oxidase converts to uric acid, causing the tumour lysis syndrome that rasburicase and allopurinol prevent.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Apoptotic priming: high MYC primes Burkitt cells for apoptosis, so chemotherapy readily triggers caspase-3-mediated cell death — the basis of the tumour's striking chemosensitivity and curability.
- `connects-to` → **[BTK](../../03-molecular/btk/README.md)** — BTK transduces the tonic B-cell-receptor signal that, with PI3K, sustains Burkitt lymphoma—a tonic rather than chronic-active BCR dependency that distinguishes its signaling from other aggressive B-cell lymphomas.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCR4 on Burkitt cells follows CXCL12 gradients into the bone marrow and central nervous system, the dissemination pattern that makes intensive CNS-directed prophylaxis essential in Burkitt-lymphoma therapy.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2 restrains the strong pro-apoptotic p53 response that MYC overexpression provokes, so the MDM2-p53 balance shapes how readily Burkitt cells undergo apoptosis when their TP53 is still intact.
- `connects-to` → **[LMP1](../../03-molecular/lmp1/README.md)** — Endemic Burkitt lymphoma is driven by Epstein-Barr virus together with chronic malaria, and the EBV-infected germinal-center B cell is the cell of origin in which the MYC translocation arises in the African childhood form.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — The defining t(8;14) places MYC under the control of the immunoglobulin heavy-chain enhancer, driving its overexpression, and tonic B-cell-receptor signaling further sustains the Burkitt cell—the basis for BTK and PI3K targeting.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — CD19-directed CAR-T cells and the CD19-CD3 bispecific blinatumomab redirect cytotoxic T cells to kill Burkitt cells through perforin and granzyme, an emerging option in relapsed or refractory disease.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — MYC transactivates E2F1, and the two cooperate to drive cell-cycle entry alongside the cyclin-D1/CDK4-6 axis already mapped, underpinning Burkitt lymphoma's extreme proliferative rate.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss activates the PI3K-AKT-mTOR pathway (PIK3CA, AKT and mTOR already mapped), a tonic-BCR-driven second hit that cooperates with the MYC translocation in Burkitt lymphomagenesis.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — The CDKN2A locus encodes p14ARF, which normally stabilizes p53 against MDM2 (both mapped); its loss removes the apoptotic brake on MYC-driven proliferation in Burkitt lymphoma.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Tonic B-cell-receptor and RAS signaling converge on ERK1/2 MAPK to drive the proliferation that cooperates with the MYC translocation in Burkitt lymphoma.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — Activating RAS-pathway mutations recurrently accompany the MYC translocation in Burkitt lymphoma, reinforcing the proliferative and survival signaling of the tumor.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — The RB1-E2F checkpoint (E2F1, CDK4/6 and cyclin-D already mapped) restrains S-phase entry, and its inactivation removes a brake on the MYC-driven proliferation of Burkitt lymphoma.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK-STAT signaling contributes to the cytokine-responsive proliferation of Burkitt lymphoma cells.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING participates in the response to EBV (LMP1 mapped) in EBV-associated Burkitt lymphoma.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 modulates apoptosis resistance and the microenvironment interactions of Burkitt lymphoma cells.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6/IL-10-STAT3 signaling supports the survival of Burkitt lymphoma cells, exploited by the Epstein-Barr-virus-associated subtype.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antiviral and antitumor immune response to the Epstein-Barr-virus-driven Burkitt lymphoma.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling normally restrains B-cell proliferation, a brake overridden by the MYC translocation of Burkitt lymphoma.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β regulates MYC phosphorylation and turnover (MYC already mapped) and the survival signaling of Burkitt lymphoma cells.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins from infiltrating myeloid cells shape the inflammatory microenvironment of Burkitt lymphoma.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH signaling, recurrently mutated in a subset of Burkitt lymphoma, contributes to its pathogenesis.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family (LYN) kinase signaling downstream of the tonic B-cell receptor supports the survival of the MYC-driven cells of Burkitt lymphoma.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of Burkitt lymphoma.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and metabolic-stress management of the highly proliferative MYC-driven cells of Burkitt lymphoma.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of the highly proliferative cells of Burkitt lymphoma.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-family chemokine signaling (CXCL12/CXCR4 already mapped) participates in the trafficking of Burkitt lymphoma cells.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic dysregulation of Burkitt lymphoma.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of Burkitt lymphoma.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of Burkitt lymphoma.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of Burkitt lymphoma.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of Burkitt lymphoma.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of Burkitt lymphoma.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling downstream of the B-cell receptor participates in the survival signaling of Burkitt lymphoma.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — EBV immune escape: MHC class II presentation of Epstein-Barr-virus antigens (LMP1 already mapped) shapes the immune control of EBV-driven Burkitt lymphoma, and downregulation of antigen presentation is one route by which the tumour evades T cells.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Cellular immunotherapy: IL-2-driven T-cell expansion supports the CD19-directed CAR-T and EBV-specific T-cell therapies (perforin already mapped) explored for relapsed and immunodeficiency-associated Burkitt lymphoma.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — Checkpoint context: CTLA-4 restrains the anti-tumour T-cell response, and its role in immune tolerance is relevant to the impaired EBV surveillance underlying the endemic and immunodeficiency-associated forms of Burkitt lymphoma.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Marrow involvement: bone-marrow infiltration by Burkitt lymphoma and its intensive chemotherapy lower haemoglobin, and the resulting anaemia, with the other cytopenias, adds to the acute morbidity of this rapidly growing tumour.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Tumour-lysis acidosis: the extreme proliferation of Burkitt lymphoma, lysed by chemotherapy, releases acids that, with lactate from the metabolic stress, produce the metabolic acidosis of tumour-lysis syndrome (potassium and urate already mapped).
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Anthracycline cardiotoxicity: the intensive anthracycline-containing chemotherapy that cures most Burkitt lymphoma is cardiotoxic, and troponin elevation helps detect the myocardial injury threatening long-term survivors.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10, whose viral homologue is encoded by the Epstein-Barr virus (LMP1 already mapped) of endemic Burkitt lymphoma, dampens the anti-tumour T-cell response (PD-1 already mapped), part of the immune evasion of the tumour.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Tumour angiogenesis: VEGF-driven angiogenesis supplies the extraordinarily proliferative Burkitt lymphoma (HIF-1-alpha already mapped), part of the microenvironment sustaining the fastest-growing human tumour.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Transfusion and anaemia: the anaemia of marrow involvement and intensive chemotherapy (haemoglobin already mapped) requires red-cell transfusion in Burkitt lymphoma, whose repeated support can load the body with iron.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — CNS involvement: Burkitt lymphoma has a high risk of central nervous system involvement and relapse, requiring intrathecal chemotherapy prophylaxis to the brain and meninges as part of curative therapy.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Tumour-lysis hyperkalaemia: the massive, rapid cell turnover of Burkitt lymphoma (xanthine oxidase and urate already mapped) releases potassium, the hyperkalaemia of tumour-lysis syndrome being a life-threatening metabolic emergency.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Starry-sky macrophages: IL-4 polarises the tingible-body macrophages that engulf the abundant apoptotic cells, producing the classic 'starry-sky' appearance (IL-10 already mapped) of the M2 macrophages in Burkitt lymphoma.
- `connects-to` → **[HIV](../hiv/README.md)** — AIDS-associated lymphoma: Burkitt lymphoma is an AIDS-defining lymphoma, HIV predisposing to it via the immune dysregulation, a form distinct from the endemic EBV/malaria (LMP1 already mapped) variant.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 starry-sky arm: IL-13, with IL-4 (already mapped), supports the M2 tingible-body macrophage (already mapped) 'starry-sky' phenotype of Burkitt lymphoma.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Adipokine microenvironment: leptin signals from the adipose and marrow microenvironment to the aggressive lymphoma cells, part of the metabolic context (xanthine oxidase already mapped) of Burkitt lymphoma.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine microenvironment: adiponectin, with leptin (already mapped), is part of the adipose/marrow-microenvironment adipokine signalling to the aggressive Burkitt lymphoma cells.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine microenvironment: resistin, with leptin and adiponectin (already mapped), completes the adipokine dimension of the microenvironment of Burkitt lymphoma.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — EBV antiviral interferon: the type-I interferon antiviral response to the EBV (LMP1 already mapped) is part of the host-virus biology of the endemic EBV-driven Burkitt lymphoma.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour/antiviral arm: the IFN-γ of the T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour and anti-EBV (LMP1 already mapped) immunity of Burkitt lymphoma.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of Burkitt lymphoma.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of Burkitt lymphoma.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the Burkitt-lymphoma microenvironment.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the Burkitt-lymphoma microenvironment.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of Burkitt lymphoma.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Rituximab CDC: the complement C5 (with C3 already mapped) is the effector of the complement-dependent cytotoxicity by which the anti-CD20 (already mapped) rituximab kills the Burkitt-lymphoma B cells (already mapped).
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling links the complement (C3 and C5 already mapped) to the myeloid inflammation of the Burkitt-lymphoma microenvironment.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the Burkitt-lymphoma cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), a resistance mechanism to the rituximab complement-dependent killing.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway of the anti-CD20 (already mapped) rituximab complement-dependent cytotoxicity against the Burkitt-lymphoma cells.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Microenvironment matricellular: osteopontin, a matricellular cytokine, is part of the inflammatory microenvironment of the highly proliferative Burkitt lymphoma.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — MYC-driven iron: transferrin, the iron carrier, supplies the high iron demand of the MYC-driven (already mapped) rapid proliferation of Burkitt lymphoma.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-TME axis: TSLP, from stromal cells and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2 immunosuppression of the Burkitt-lymphoma microenvironment.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-lymphoma axis: bradykinin, via B1/B2 receptors on tumour endothelium (already mapped) and mast cells (already mapped), amplifies the vascular permeability and the cytokine milieu of the Burkitt-lymphoma microenvironment.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Erythropoietic support: erythropoietin supports the management of the myelosuppressive-chemotherapy-induced anaemia of the intensive treatment of Burkitt lymphoma.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell lymphoma axis: histamine, from mast cells (already mapped) in the Burkitt-lymphoma microenvironment, amplifies the MYC-driven (already mapped) angiogenesis (already mapped) and the immunosuppressive cytokine milieu of the tumour stroma.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian-lymphoma axis: melatonin, via MT1/MT2 receptors and its radical-scavenging activity, modulates the oxidative stress of the MYC-driven (already mapped) rapid proliferation and the genomic instability of Burkitt lymphoma.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen-lymphoma axis: testosterone, via androgen receptors on tumour B-cells (already mapped) and stromal cells, modulates the sex-differential incidence and the immunosuppressive microenvironment of Burkitt lymphoma.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Burkitt serotonin: serotonin, via 5-HT receptors on macrophages (already mapped) and mast cells (already mapped), modulates the lymphoma TME; serotonin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) proliferative cascade of Burkitt lymphoma.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Burkitt prolactin: prolactin, via PRLR on macrophages (already mapped) and mast cells (already mapped), promotes lymphoma immune escape; hyperprolactinaemia amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of Burkitt lymphoma.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Burkitt oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates lymphoma TME inflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of Burkitt lymphoma.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Burkitt vasopressin: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates lymphoma TME immune tone; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of Burkitt lymphoma.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Burkitt selenium: selenium, as GPx in macrophages (already mapped) and mast cells (already mapped), scavenges ROS driving the lymphoma TME; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour-promoting cascade of Burkitt lymphoma.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Burkitt iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) and mast-cell (already mapped) immune function; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour-promoting cascade of Burkitt lymphoma.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^roschewski-2020-da-epoch-r-bl]: Roschewski M, Dunleavy K, Abramson JS, et al. Multicenter study of risk-adapted therapy with dose-adjusted EPOCH-R in adults with untreated Burkitt lymphoma. *J Clin Oncol.* 2020;38(22):2519-2529. [doi:10.1200/JCO.19.03259](https://doi.org/10.1200/JCO.19.03259) · [PubMed 32530765](https://pubmed.ncbi.nlm.nih.gov/32530765/)
[^minard-colin-2017-inter-b-nhl-ritux]: Minard-Colin V, Auperin A, Pillon M, et al. Rituximab for children and adolescents with high-risk B-cell non-Hodgkin lymphoma: results of the randomized Inter-B-NHL Ritux 2010 trial. *J Clin Oncol.* 2022;40(22):2458-2471. [doi:10.1200/JCO.21.01940](https://doi.org/10.1200/JCO.21.01940) · [PubMed 35436151](https://pubmed.ncbi.nlm.nih.gov/35436151/)

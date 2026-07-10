---
schema: human-scale-entry/v1
id: neuroblastoma
name: Neuroblastoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Neuroblastoma is the most common extracranial pediatric solid tumor; neural crest-derived; MYCN amplification in ~40% high-risk; tandem auto-SCT + dinutuximab (anti-GD2) + 13-cis-retinoic acid maintenance for high-risk; ALK inhibitors in Phase 3 trials."
aliases: ["neuroblastoma", "NB", "high-risk neuroblastoma", "neuroblastoma MYCN", "Stage 4 neuroblastoma", "N-myc neuroblastoma", "INRG neuroblastoma"]
sources:
  - id: yu-2010-dinutuximab-nb
    type: peer-reviewed
    cite: "Yu AL, Gilman AL, Ozkaynak MF, et al. Anti-GD2 antibody with GM-CSF, interleukin-2, and isotretinoin for neuroblastoma. N Engl J Med. 2010;363(14):1324-1334."
    doi: "10.1056/NEJMoa0911123"
    pmid: "20879881"
    url: "https://doi.org/10.1056/NEJMoa0911123"
  - id: park-2019-tandem-sct-nb
    type: peer-reviewed
    cite: "Park JR, Kreissman SG, London WB, et al. Effect of tandem autologous stem cell transplant vs single transplant on event-free survival in patients with high-risk neuroblastoma: a randomized clinical trial. JAMA. 2019;322(8):746-755."
    doi: "10.1001/jama.2019.11642"
    pmid: "31454023"
    url: "https://doi.org/10.1001/jama.2019.11642"
cross_links:
  - target: 01-human/03-molecular/mycn
    relation: connects-to
    note: "MYCN amplification (~20% overall, ~40% high-risk NB) is the primary risk-stratification biomarker; AURKA stabilizes MYCN protein; MYCN drives proliferation and blocks differentiation; MYCN amplification confers high-risk designation regardless of age or stage."
  - target: 01-human/03-molecular/alk
    relation: connects-to
    note: "ALK GOF mutations (F1174L, R1275Q) in ~10-14% NB; ALK amplification in ~4%; ALK and MYCN co-amplification → double-hit worst prognosis; lorlatinib in Phase 3 ANBL2232; PHOX2B and ALK co-mutated in familial NB predisposition."
  - target: 01-human/03-molecular/ret
    relation: connects-to
    note: "Neural crest-derived NB cells co-express RET during sympathoadrenal development; GDNF-RET signaling is required for sympathetic ganglion formation; retinoic acid-induced differentiation upregulates RET; RET mutations are not primary NB drivers."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 mutations are rare at NB diagnosis (~1-2%) but acquired in ~80% of relapsed NB; MDM2 amplification (~4%) functionally inactivates p53; MYCN drives MDM2-dependent p53 suppression; MDM2 inhibitors (idasanutlin) explored in relapsed MYCN-amplified NB."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "TRKA (NTRK1) drives NGF-induced differentiation/apoptosis in Stage MS NB, enabling spontaneous regression; MYCN-amplified NB loses TRKA so NGF cannot trigger regression, yielding aggressive disease; rare ETV6-NTRK3 and other NTRK fusions respond to larotrectinib/entrectinib."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "The adrenal medulla is the single most common NB primary site (~40%); NB arises from arrested sympathoadrenal chromaffin/neuroblast precursors of neural-crest origin; it presents as an MIBG-avid adrenal mass secreting catecholamine metabolites (urine VMA/HVA)."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Dinutuximab (anti-GD2) kills NB via NK-cell ADCC and complement-dependent cytotoxicity; GM-CSF enhances NK/monocyte effector function; IL-2 expands NK cells in COG ANBL0032 maintenance; NK-mediated immunotherapy improved high-risk NB event-free survival."
  - target: 01-human/07-system/neuroendocrine-tumors
    relation: connects-to
    note: "Neuroblastoma and adult neuroendocrine tumors are both neural-crest/neuroendocrine cancers that secrete amines and take up amine tracers, but differ sharply: neuroblastoma is an aggressive embryonal tumor of young children (MYCN-driven), NETs mostly indolent tumors of adults."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Bone marrow is the most common metastatic site in high-risk neuroblastoma: small-round-blue-cell nests infiltrate the marrow (stage M), detected by bilateral biopsies and MIBG scan, and clearing marrow disease is a key goal of induction chemotherapy and anti-GD2 immunotherapy."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Neuroblastoma is a tumor of arrested sympathetic neuroblasts: its cells span a spectrum from neuroblastoma through ganglioneuroblastoma to benign ganglioneuroma, and retinoic acid pushes residual cells toward mature neurons — the basis of isotretinoin maintenance after therapy."
  - target: 01-human/07-system/pheochromocytoma-paraganglioma
    relation: connects-to
    note: "Neuroblastoma and pheochromocytoma both arise from sympathoadrenal neural-crest cells: neuroblastoma is the malignant childhood tumor of immature sympathetic precursors, while pheochromocytoma is its catecholamine-secreting adult counterpart—both seen on MIBG."
  - target: 01-human/07-system/wilms-tumor
    relation: connects-to
    note: "Neuroblastoma and Wilms tumor are the two commonest extracranial solid tumors of early childhood and key differentials for an abdominal mass: neuroblastoma is an adrenal/sympathetic-chain tumor crossing the midline, while Wilms (nephroblastoma) is a renal tumor that respects it."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy treats high-risk neuroblastoma two ways: external-beam photon irradiation consolidates the primary site after surgery and chemo, while 131-I-MIBG delivers targeted internal radiation to MIBG-avid metastases—exploiting the tumor's radiosensitivity."
  - target: 01-human/07-system/ewing-sarcoma
    relation: connects-to
    note: "Neuroblastoma and Ewing sarcoma are both 'small round blue cell' childhood tumors that overlap on biopsy but are distinct: neuroblastoma arises from sympathetic neuroblasts, while Ewing arises in bone with EWSR1-FLI1 and CD99—immunostains separate them."
  - target: 01-human/07-system/medulloblastoma
    relation: connects-to
    note: "Neuroblastoma and medulloblastoma are both embryonal childhood tumors at different sites: neuroblastoma arises from peripheral sympathetic neuroblasts, medulloblastoma from cerebellar progenitors—peripheral versus central nervous-system embryonal cancers."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Neuroblastoma sits in the expanded Li-Fraumeni spectrum: germline TP53 loss modestly raises childhood neuroblastoma risk, and although most are sporadic, TP53-pathway inactivation contributes to aggressive, treatment-resistant relapses—linking it to the p53 guardian."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Neuroblastoma arises from catecholamine-making cells: its sympathetic-lineage cells secrete norepinephrine precursors, so the urinary breakdown products VMA and HVA serve as diagnostic and monitoring markers—and catecholamine excess can cause hypertension."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Neuroblastoma is a cancer of the developing sympathetic nervous system: it arises from neural-crest-derived sympathetic precursors anywhere along the chain or in the adrenal medulla, so tumors appear in the abdomen, chest or neck wherever sympathetic tissue lies."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Neuroblastoma's stage 4S shows uncanny liver behavior: in infants, tumor can massively infiltrate the liver yet spontaneously regress without treatment—a striking exception to cancer's usual course that makes neuroblastoma's biology age-dependent."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Neuroblastoma is treated by harnessing the immune system: anti-GD2 antibodies (dinutuximab) target a glycolipid richly expressed on neuroblasts, and adding immunotherapy to high-risk regimens markedly improved survival—a landmark for solid-tumor immunotherapy in children."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Proton therapy is favored for neuroblastoma in young children: the tumor often sits near the spine, kidneys and liver, so protons' lack of exit dose limits damage to developing organs and lowers the risk of radiation-induced second cancers."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "GD2-directed cell therapy targets neuroblastoma via cytotoxic T cells: CAR-T cells engineered against the GD2 antigen are in trials to kill neuroblasts, extending the anti-GD2 strategy from antibodies to engineered T-cell immunity."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Neuroblastoma is targeted with radioactive iodine via MIBG: the tumor takes up metaiodobenzylguanidine like norepinephrine, so I-123 MIBG scans light up disease and I-131 MIBG delivers radiation directly to neuroblastoma cells in high-risk patients."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "High-risk neuroblastoma keeps its telomeres long: TERT activation (or ATRX-driven alternative lengthening) lets cells divide endlessly, and this telomere-maintenance switch—alongside MYCN—marks the aggressive tumors that need intensive therapy."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Anti-GD2 immunotherapy enlists macrophages: the antibody dinutuximab coats neuroblastoma's GD2 antigen so macrophages and complement (with NK cells) destroy it, a now-standard treatment that improved survival in high-risk disease."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Neuroblastoma betrays its neural-crest origin by making dopamine: arising from sympathetic precursors, it synthesizes catecholamines whose breakdown products (HVA from dopamine, VMA from noradrenaline) spill into urine as diagnostic tumor markers."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Neuroblastoma defends itself with regulatory T cells: a suppressive microenvironment rich in Tregs blunts the immune attack, a barrier that anti-GD2 antibody immunotherapy (dinutuximab) must overcome to clear high-risk disease."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "High-risk neuroblastoma is intensely angiogenic via VEGF: the tumor drives new blood vessels to fuel rapid growth and spread, and high vascularity marks aggressive disease—making anti-angiogenic strategies a research target."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Infant neuroblastoma can stud the skin: in the special 4S stage, blue-tinged skin nodules ('blueberry muffin') appear alongside liver and marrow spread, yet this pattern often regresses on its own—a striking exception to the cancer's usual aggressiveness."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells anchor neuroblastoma immunotherapy: presenting tumor antigens, they help prime the T-cell and anti-GD2 responses that have improved survival, and dendritic-cell vaccines are explored to boost immunity against residual disease."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Neuroblastoma's ALK mutations signal through AKT: activated ALK drives the PI3K-AKT-mTOR pathway to fuel growth and survival, so AKT-pathway inhibitors are studied alongside ALK inhibitors in the high-risk, MYCN-amplified disease."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Neuroblastoma announces itself in the eyes: spread to the bones around the orbit causes the 'raccoon eye' bruising, and the paraneoplastic opsoclonus-myoclonus brings the 'dancing eyes' that can be the first clue."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Neuroblastoma eats away calcium-rich bone: it metastasizes widely to the cortical skeleton, eroding the bone and causing the pain and fractures that mark high-risk, disseminated disease."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Neuroblastoma recruits endothelial cells to grow: VEGF from the tumor drives them to build a dense blood supply, and the degree of this angiogenesis tracks with the aggressive, high-risk forms."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy proves a tumor is neuroblastic: the beam reveals dense-core neurosecretory granules and slender neuritic processes packed with microtubules — ultrastructure that confirms neural origin when an undifferentiated small-round-blue-cell tumor defies routine stains."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Neuroblastoma is the great mimic of a kidney tumor: arising in the adrenal gland atop the kidney, it pushes the organ down and outward rather than springing from it — the displacement that distinguishes it on imaging from Wilms tumor."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Many neuroblastomas grow beside the lung: the posterior mediastinum, along the paraspinal sympathetic chain, is the second commonest primary site, where a chest mass can press on the airway or erode through the spinal foramina."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Neuroblastoma reaches the brain in two ways: it spreads to the dura and skull (the 'raccoon-eye' orbital deposits), and as a paraneoplastic syndrome it provokes opsoclonus-myoclonus, the 'dancing eyes' from an immune attack on the brain."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Some neuroblastomas flood the gut with hormone: a VIP-secreting tumor causes Kerner-Morrison syndrome, intractable watery diarrhea that drains the bowel and the body's potassium."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "The VIP-secreting neuroblastoma crashes the potassium: its relentless secretory diarrhea flushes potassium out of the body, a hypokalemia severe enough to threaten the heart until the tumor is removed."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "An antibody is now front-line therapy: dinutuximab targets the GD2 disialoganglioside coating neuroblastoma cells, marking them for immune killing, and the tumor can also trigger the autoantibodies of opsoclonus-myoclonus, the paraneoplastic 'dancing eyes' syndrome."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Cure means battering the marrow: high-dose chemotherapy and stem-cell transplant drop the neutrophil count to near zero, and the anti-GD2 antibody is paired with GM-CSF to coax neutrophils into helping kill the tumor."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Neuroblastoma packs the marrow at diagnosis: as the small round blue cells flood the bone marrow they crowd out red-cell production, and the resulting anemia, pale erythrocytes, and fatigue are often what bring a child to care."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "The same marrow takeover starves the platelets: tumor flooding the bone marrow suppresses platelet production into thrombocytopenia, so bruising and bleeding join the anemia among the presenting signs of widespread neuroblastoma."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Cisplatin in high-risk regimens wastes magnesium: the platinum chemotherapy injures the kidney tubule that reclaims the mineral, so blood magnesium falls and needs replacing, alongside watching for the drug's hearing loss and kidney damage."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Cure can cost future fertility: the intensive chemotherapy, total-body irradiation, and stem-cell transplant used for high-risk neuroblastoma damage the gonads, so the late effects on growth and fertility are part of survivor care for these children."
  - target: 01-human/03-molecular/atrx
    relation: connects-to
    note: "An alternate route to the same cancer: ATRX mutations mark a distinct, often older-child neuroblastoma that keeps its telomeres long by recombination rather than telomerase, mutually exclusive with MYCN amplification and tied to a chronic, treatment-resistant course."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "It springs from the body's autonomic wiring: neuroblastoma arises from immature sympathetic neuroblasts of the peripheral nervous system, which is why it appears along the sympathetic chain and adrenal medulla and why favorable tumors can mature into benign nerve tissue."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "The tumor can drive up blood pressure: like its catecholamine-secreting cousins, some neuroblastomas pour out norepinephrine and dopamine, producing hypertension, sweating and flushing that can be the clue that leads to diagnosis."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Cell-cycle escape marks the aggressive tumor: CDKN2A loss and other cell-cycle lesions cooperate with MYCN amplification in high-risk neuroblastoma, driving the rapid proliferation that defines the lethal subtype."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "The tumor and its cure both hurt the nerves: paraspinal neuroblastoma compresses nerve roots and the spinal cord, and platinum/vincristine chemotherapy adds a peripheral neuropathy — together a major pain burden in these children."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Intensive therapy strips the defenses: the high-dose chemotherapy and autologous transplant used for high-risk neuroblastoma cause prolonged neutropenia, making febrile neutropenia and sepsis a central treatment hazard."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 backs the high-risk tumor: MYCN-amplified neuroblastoma shows STAT3 activation that supports proliferation and immune evasion, a pathway explored where this childhood cancer resists intensive therapy."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Tumor and central lines clot the veins: neuroblastoma's hypercoagulable state, the long-term central venous catheters and the immobility of intensive treatment together raise venous thromboembolism risk in these children."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Marrow metastasis and inflammation drain the blood: high-risk neuroblastoma commonly infiltrates the bone marrow and raises inflammatory cytokines, producing anemia from both crowding and chronic disease."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its anthracyclines scar the developing heart: the doxorubicin in high-risk neuroblastoma regimens is dose-dependently cardiotoxic, risking a cardiomyopathy and heart failure that can emerge years into survivorship."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "High-dose therapy strips the lung's defenses: the intensive chemotherapy and autologous stem-cell transplant for high-risk neuroblastoma cause profound neutropenia, letting inhaled Aspergillus invade as pulmonary aspergillosis."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Its platinum chemo scars young kidneys: the cisplatin and carboplatin central to neuroblastoma regimens are nephrotoxic, and in a child the tubular and electrolyte injury can leave lasting chronic kidney impairment."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Transplant immunosuppression reawakens shingles: the autologous stem-cell transplant and immunotherapy for high-risk neuroblastoma deplete T-cell immunity, allowing latent varicella-zoster to reactivate."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Resecting an abdominal mass heals slowly: the wide surgical removal of a neuroblastoma, often after chemotherapy in a malnourished child, leaves large wounds prone to dehiscence and delayed closure."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Childhood cancer breeds enduring worry: the intensive treatment, relapse risk and long survivorship surveillance of high-risk neuroblastoma foster chronic anxiety in survivors and their families."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It spreads to bone and marrow: high-risk neuroblastoma metastasises avidly to the bones and bone marrow, causing bone pain, limping and the periorbital 'raccoon eyes' of orbital deposits."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Its mass and hormones disturb the gut: an abdominal or adrenal neuroblastoma compresses the bowel, and VIP-secreting tumours cause a profuse, intractable secretory diarrhoea."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It is a hormone-secreting neural-crest tumour: arising from the sympathoadrenal lineage, neuroblastoma secretes catecholamines and sometimes VIP, and MIBG therapy requires thyroid protection."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It shows on the skin and around the eyes: infants with stage MS disease develop blue 'blueberry muffin' skin nodules, and orbital metastases cause periorbital 'raccoon eye' ecchymoses."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Thoracic tumours crowd the chest: a posterior mediastinal neuroblastoma can compress the airway and spinal cord, and the disease can rarely metastasise to the lungs."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It spreads through the nodes: neuroblastoma disseminates to regional and distant lymph nodes, part of the staging that guides its risk-stratified treatment."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It floods the body with catecholamines: neuroblastoma can secrete catecholamines causing hypertension, and its anthracycline chemotherapy adds long-term cardiotoxicity."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It crowds and is treated near the kidney: adrenal and paraspinal neuroblastomas compress the kidney and ureter, and cisplatin chemotherapy is nephrotoxic."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "It is treated by precision agents: anti-GD2 immunotherapy (dinutuximab) and MIBG-targeted radiotherapy exploit neuroblastoma's neural markers in high-risk disease."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Intensive chemo for high-risk disease: high-risk neuroblastoma is treated with multi-agent induction chemotherapy and high-dose therapy with autologous stem-cell rescue."
  - target: 03-medicine/01-modern/13-cancer/car-t
    relation: connects-to
    note: "GD2 cell therapy shows promise: GD2-directed CAR-T cells, building on the success of anti-GD2 antibodies, have produced responses in relapsed neuroblastoma, a leading solid-tumour CAR-T target."
  - target: 01-human/07-system/mpnst
    relation: connects-to
    note: "A fellow neural-crest tumour: like malignant peripheral nerve sheath tumour, neuroblastoma derives from neural-crest lineage, the two among the nerve-associated malignancies of childhood and young adults."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Its metastases love bone: neuroblastoma spreads to cortical bone and marrow—skull and orbits producing periorbital bruising ('raccoon eyes')—and these deposits, rich in catecholamine metabolism, are imaged with MIBG scintigraphy."
  - target: 01-human/07-system/diffuse-midline-glioma
    relation: connects-to
    note: "A shared GD2 immunotherapy target: the disialoganglioside GD2 that anti-GD2 antibodies and CAR-T target in neuroblastoma is also highly expressed on diffuse midline glioma, where GD2 CAR-T has produced striking early responses."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "An immunologically cold childhood tumour: neuroblastoma has a low mutational burden and responds poorly to PD-1 checkpoint inhibitors, so its immunotherapy relies on anti-GD2 antibodies and CAR-T rather than checkpoint blockade."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Stage 4S liver disease: in infant 4S neuroblastoma, tumour floods the hepatic lobule causing massive hepatomegaly that can spontaneously regress—a behaviour unique among cancers."
  - target: 01-human/07-system/retinoblastoma
    relation: connects-to
    note: "Two infant cancers, opposite genetics: neuroblastoma (MYCN amplification, an oncogene) and retinoblastoma (RB1 loss, a tumour suppressor) are both classic tumours of infancy from contrasting molecular routes."
  - target: 01-human/07-system/rhabdomyosarcoma
    relation: connects-to
    note: "A small-round-blue-cell mimic: neuroblastoma joins rhabdomyosarcoma, Ewing sarcoma and lymphoma in the childhood small-round-blue-cell differential, distinguished by neuroendocrine markers and urinary catecholamines."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "A shared druggable driver: ALK rearrangements in lung cancer and activating ALK mutations in neuroblastoma make the same kinase targetable in both, so ALK inhibitors like lorlatinib cross from adult NSCLC into paediatric neuroblastoma."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Therapy-related leukaemia: the high-dose alkylator chemotherapy and stem-cell transplant used for high-risk neuroblastoma damage the marrow, occasionally causing secondary myelodysplasia and acute myeloid leukaemia in survivors."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Cardiotoxic survivorship: anthracyclines in high-risk neuroblastoma regimens injure the myocardium, leaving childhood survivors at lifelong risk of cardiomyopathy and heart failure decades later."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Apoptosis evasion: neuroblastoma depends on anti-apoptotic BCL-2 family proteins for survival, a vulnerability targeted by BH3-mimetic drugs."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Cell-cycle drive: CDK4/6-cyclin D activity, amplified by MYCN, propels neuroblastoma proliferation, making CDK4/6 inhibition an investigational strategy."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "MYCN's epigenetic effector: MYCN upregulates EZH2 to enforce the repressive, anti-differentiation chromatin programme of high-risk neuroblastoma."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "MYC-family alternative: in MYCN-non-amplified neuroblastoma, c-MYC drives a similar high-risk transcriptional programme, the two MYC-family oncogenes converging on aggressive disease."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Growth-signal hub: PI3K/AKT/mTOR signalling stabilises MYCN and drives the protein synthesis that fuels neuroblastoma growth, a rationale for mTOR-pathway inhibition."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Tumour hypoxia: HIF-1α stabilised in the hypoxic neuroblastoma drives angiogenesis and an undifferentiated, aggressive phenotype linked to poor outcome."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ALK-RAS-MAPK: activating ALK mutations signal through RAS-RAF-ERK to drive neuroblastoma proliferation, the rationale for ALK inhibitors in the ALK-mutant subset."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Differentiation and apoptosis: retinoic acid and chemotherapy drive neuroblastoma cells toward caspase-3-mediated apoptosis and differentiation, the basis of maintenance therapy in high-risk disease."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Macrophage microenvironment: CCL2 recruits tumour-associated macrophages into neuroblastoma, contributing to the immunosuppressive niche of this often immunologically cold childhood tumour."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Marrow and bone metastasis: CXCR4 on neuroblastoma cells follows CXCL12 gradients to the bone marrow and bone, the hallmark metastatic sites whose involvement defines high-risk, metastatic (stage M) disease."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Antibody-directed killing: anti-GD2 antibody (dinutuximab) directs NK cells and macrophages to kill neuroblastoma, with NK perforin-mediated cytotoxicity a key effector of this immunotherapy that improved high-risk survival."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cold-tumour innate immunity: MYCN-amplified neuroblastoma is immunologically cold with suppressed cGAS-STING signalling, and restoring this innate pathway is explored to inflame the tumour for immunotherapy."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Neurotrophic survival: high-risk neuroblastomas express TrkB and respond to its ligand BDNF with an autocrine survival, angiogenic and chemoresistance loop, the neurotrophin axis that distinguishes aggressive disease from the TrkA-expressing tumours prone to regress."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Neural-crest development: neuroblastoma arises from sympathoadrenal neural-crest progenitors, and Wnt/β-catenin signalling that patterns neural-crest development is co-opted to sustain the proliferative, undifferentiated state of the tumour."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "Epigenetic dependence: with few recurrent mutations, neuroblastoma is driven heavily by epigenetic dysregulation — MYCN-bound super-enhancers and DNA-methylation programmes — making the epigenome a key therapeutic target in this developmental cancer."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K-MYCN axis: ALK and growth-factor signalling drive PI3K-AKT-mTOR (AKT and mTOR already mapped), which stabilises MYCN protein (mapped), coupling PI3K activity to the central oncogenic driver of high-risk neuroblastoma."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Proliferative output: the CDK4/6 axis (CDK4/6 and CDKN2A already mapped) releases E2F1, and MYCN transactivates E2F target genes to drive the cell-cycle progression of neuroblastoma."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "Relapse RAS pathway: ALK signals through RAS-MAPK (ERK1/2 mapped), and activating RAS-pathway mutations are enriched at neuroblastoma relapse as a mechanism of treatment resistance."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Cell-cycle target: the RB1-E2F checkpoint (CDK4/6, CDKN2A and E2F1 already mapped) restrains proliferation, and its dysregulation in high-risk neuroblastoma is a target of CDK4/6 inhibition."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "p53 inactivation: TP53 is rarely mutated in neuroblastoma; instead MDM2 amplification (transactivated by MYCN) inactivates wild-type p53 (already mapped), an actively pursued MDM2-p53 therapeutic axis."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "STAT3 microenvironment: JAK-STAT3 signalling (STAT3 already mapped) supports the survival and immunosuppressive microenvironment of neuroblastoma."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 modulates neuroblastoma differentiation, survival and the immune microenvironment."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β signalling shapes neuroblastoma differentiation and the immunosuppressive tumour microenvironment."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "Loss of PTEN restraint on PI3K-AKT-mTOR signalling (AKT, PIK3CA and mTOR mapped) cooperates with MYCN amplification in high-risk neuroblastoma."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the immunologically cold microenvironment of high-risk neuroblastoma, relevant to its anti-GD2 and emerging immunotherapy."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling shapes the differentiation block and immunosuppressive microenvironment of neuroblastoma."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors, restrained by the PTEN-PI3K-AKT axis, regulate the survival and differentiation of the neural-crest-derived cells of neuroblastoma."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the MYCN stability and survival signaling of neuroblastoma."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the immunosuppressive microenvironment of the immune-cold high-risk neuroblastoma."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-kinase signaling downstream of ALK and TrkB (ALK and NTRK already mapped) drives the survival and invasion of neuroblastoma."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and therapy resistance of the MYCN-amplified cells of neuroblastoma."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling contributes to the epigenetic dysregulation of neuroblastoma."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of the MYCN-driven cells of neuroblastoma."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of neuroblastoma."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of neuroblastoma."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "NOTCH signaling participates in the differentiation and stemness biology of neuroblastoma."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of neuroblastoma."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of neuroblastoma."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of neuroblastoma."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the tumor microenvironment of neuroblastoma."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of neuroblastoma."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin (SPP1) participates in the tumor microenvironment, metastasis, and bone-marrow involvement of neuroblastoma."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Anti-GD2 immunotherapy: high-risk neuroblastoma is treated with the anti-GD2 antibody dinutuximab combined with IL-2 and GM-CSF, and IL-2-driven immune-cell activation (perforin already mapped) enhances antibody-dependent killing of the tumour."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immune escape: neuroblastoma frequently downregulates MHC antigen presentation to evade T cells, one reason antibody-based (GD2) rather than T-cell approaches have led its immunotherapy, though restoring presentation is an active strategy."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Checkpoint context: neuroblastoma is an immunologically cold tumour with low mutational burden, and PD-1 checkpoint blockade is being tested in combination with anti-GD2 and other therapies to boost the anti-tumour response."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Marrow infiltration: bone-marrow metastasis (already mapped) by neuroblastoma and the intensive multidrug chemotherapy suppress erythropoiesis, lowering haemoglobin and requiring transfusion in high-risk disease."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Anthracycline cardiotoxicity: the doxorubicin in high-risk neuroblastoma regimens is cardiotoxic, and troponin elevation helps detect the cumulative myocardial injury that threatens these very young long-term survivors."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 helps make neuroblastoma an immunologically cold tumour (PD-1 already mapped), dampening the T-cell response, one reason antibody-based anti-GD2 rather than checkpoint approaches have led its immunotherapy."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the cold, immune-evasive microenvironment of neuroblastoma."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative stress: the proliferative neuroblastoma and its intensive chemotherapy generate oxidative stress, to which xanthine oxidase contributes, adding reactive oxygen species to the tumour microenvironment and treatment toxicity."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Transfusion and anaemia: the marrow involvement and intensive multimodal therapy of high-risk neuroblastoma (haemoglobin already mapped) cause anaemia needing transfusion, whose repeated support can load the young survivor with iron."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 tumour-associated macrophage niche of the immunosuppressive microenvironment of neuroblastoma."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper and catecholamines: copper is the cofactor of dopamine-β-hydroxylase, which makes noradrenaline from dopamine (both already mapped), the catecholamine biosynthesis of the neuroblastoma cells that secrete the VMA and HVA used to diagnose and monitor the tumour."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the angiogenesis and vascular tone of the highly vascular neuroblastoma, part of the stromal biology of the tumour."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Marrow-adipose adipokine: leptin from the marrow adipose tissue signals to the metastatic neuroblastoma cells in the bone marrow (already mapped), part of its metabolic microenvironment."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the marrow-adipose adipokine milieu of the metabolic microenvironment of metastatic neuroblastoma."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), completes the marrow-adipose adipokine signalling of the metabolic microenvironment of neuroblastoma."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the immunotherapy of neuroblastoma."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-neuroblastoma immunity augmented by the anti-GD2 plus IL-2 (already mapped) therapy."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the neuroblastoma immune microenvironment."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of neuroblastoma."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the neuroblastoma microenvironment."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2/AllergoOncology arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), is the antibody arm complementing the anti-GD2 (immunoglobulin already mapped) immunotherapy of neuroblastoma."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Humoral/GD2 arm: the B cells and the tertiary lymphoid structures underpin the antibody (anti-GD2 immunoglobulin already mapped) response harnessed by the dinutuximab immunotherapy of neuroblastoma."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of neuroblastoma."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of neuroblastoma."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Dinutuximab CDC: the complement C5 (with C3 already mapped) is an effector of the complement-dependent cytotoxicity of the anti-GD2 dinutuximab, alongside the NK-cell (already mapped) ADCC, against neuroblastoma."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the myeloid recruitment into the neuroblastoma stroma."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the neuroblastoma cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), a resistance mechanism to the anti-GD2 complement-dependent killing."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Bone marrow and treatment anaemia: EPO receptors on sympathetic neuroblasts (already mapped) confer neuroprotection; EPO-stimulating agents counter the severe myelosuppression from the high-dose chemotherapy and autologous stem-cell transplant used in high-risk neuroblastoma."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell catecholamine stroma: histamine from the mast cells infiltrating neuroblastoma stroma promotes angiogenesis (VEGF already mapped); neuroblastoma-released catecholamines amplify mast-cell degranulation and H2 receptor signalling on the NB cells promotes proliferation."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Bone pain mediator: bradykinin activates B2 receptors at the bone and bone-marrow (already mapped) metastasis sites of high-risk neuroblastoma, contributing to the severe neuropathic bone pain and amplifying the NF-kB (already mapped) pro-tumour inflammatory signalling."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Tumour-immune alarmin: TSLP released by the neuroblastoma stroma activates dendritic cells (already mapped) toward a Th2 (IL-4 already mapped) immune microenvironment, amplifying TGF-β (already mapped) immunosuppression and attenuating NK-cell (already mapped) cytotoxicity."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement immunotherapy modulation: C1-INH controls the classical-pathway arm (complement C3, C5 and C5aR1 already mapped) in neuroblastoma, modulating the complement-dependent cytotoxicity triggered by dinutuximab (antibody already mapped) anti-GD2 immunotherapy."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Bone marrow niche periostin: periostin secreted by the bone-marrow (already mapped) stromal fibroblasts in neuroblastoma metastases activates integrin-AKT (already mapped) pro-survival signalling and promotes VEGF-driven (already mapped) angiogenesis in high-risk neuroblastoma."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Tumour-suppressive pineal hormone: melatonin inhibits neuroblastoma proliferation through MT1/MT2 receptor-mediated cAMP-PKA suppression and p53 (already mapped)-dependent apoptosis, counteracting MYCN (already mapped) oncogenic drive."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Catecholamine cross-talk: neuroblastoma arises from sympathoadrenal precursors sharing the catecholamine pathway with adrenal androgen production; testosterone converges on AR signalling to modulate NB differentiation and MYCN (already mapped) expression."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Catecholamine pathway co-regulator: neuroblastoma tumour cells express the serotonin transporter (SERT; already mapped) and metabolise 5-HIAA alongside catecholamines; serotonin receptor activation modulates cAMP-PKA signalling (MYCN already mapped) and NB cell proliferation."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "NB prolactin neuro-immune: prolactin, via PRLR on neuroblastoma macrophages (already mapped) and mast cells (already mapped), upregulates IL-6 (already mapped) and VEGF-driven (already mapped) pro-tumour signalling, promoting the immunosuppressive TME of neuroblastoma."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "NB oxytocin anti-tumour: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped) in the neuroblastoma stroma, attenuates IL-6 (already mapped) and VEGF-driven (already mapped) pro-tumour signalling in the neuroblastoma microenvironment."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "NB vasopressin vascular: vasopressin, via V1aR on neuroblastoma macrophages (already mapped) and mast cells (already mapped), modulates the tumour vascular niche; dysregulation amplifies IL-6 (already mapped) and VEGF (already mapped) pro-tumour signalling in neuroblastoma."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "NB selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS in the neuroblastoma TME; selenium deficiency amplifies the IL-6 (already mapped) and mTOR (already mapped) oxidative tumour cascade of neuroblastoma."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "NB sodium: high dietary sodium promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory activation; sodium-induced IL-6 (already mapped) and mTOR (already mapped) signalling amplifies the T-cytotoxic (already mapped) tumour cascade of neuroblastoma."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "NB zinc: zinc, as cofactor of antioxidant enzymes in macrophages (already mapped) and neutrophils (already mapped), attenuates oxidative stress; zinc deficiency amplifies the IL-6 (already mapped) and mTOR (already mapped) pro-tumour cascade of neuroblastoma."
---

# Neuroblastoma

## Overview

**Neuroblastoma** is the most common **extracranial solid tumor of childhood**, derived from neural crest progenitor cells committed to the sympathoadrenal lineage (adrenal medulla, sympathetic ganglia). It accounts for ~8-10% of all pediatric cancers but ~15% of pediatric cancer deaths, reflecting the extreme lethality of high-risk disease (median 5-year OS ~50%). Neuroblastoma spans a striking biological spectrum from **spontaneous regression** (Stage MS in infants) to **rapidly fatal dissemination** (Stage M with MYCN amplification), and this spectrum is captured by the **International Neuroblastoma Risk Group Staging System (INRGSS)** and risk classification incorporating MYCN status, histology, ploidy, ALK status, and segmental chromosomal aberrations. The most powerful adverse biomarker is **MYCN amplification** (~40% of high-risk cases): it is present in nearly all fatal neuroblastomas yet is absent in most spontaneously regressing tumors. Treatment of **high-risk neuroblastoma** has improved dramatically through cooperative group studies: modern regimens combine multi-agent induction chemotherapy → surgery + radiotherapy → **tandem autologous stem cell transplantation** (ANBL12P1: 3-year EFS 61.9% vs 48.4% single-SCT, p=0.007) [^park-2019-tandem-sct-nb] → maintenance with **dinutuximab** (anti-GD2 antibody) + GM-CSF + IL-2 + **13-cis-retinoic acid** (COG ANBL0032: improved 2-year EFS from 46% to 66%) [^yu-2010-dinutuximab-nb].

**Epidemiology:**
- ~700-750 cases/year in the USA; ~3,000-3,500/year globally
- Median age at diagnosis: 19 months; ~50% diagnosed <2 years; rare after age 10
- ~1-2% of all childhood cancers in USA; ~7-10% of pediatric cancer deaths
- ~1-2% are familial (ALK germline GOF or PHOX2B mutations); most are sporadic
- Slight male predominance (~1.2:1)

## Structure

### Molecular and genetic landscape

**MYCN amplification (~20% overall, ~40% high-risk):**
MYCN amplification (>4 haploid copies, typically 50-300 copies in double minutes or homogeneous staining regions) is the single most important adverse biomarker: present → always high-risk regardless of stage or age. MYCN drives proliferative arrest of sympathoadrenal differentiation, TERT activation, ribosome biogenesis, and ALK transcription.

**ALK alterations (~14-18% overall):**
- Somatic GOF mutations: F1174L (~8%, worst prognosis — activating at multiple levels), R1275Q (~4%, less activating), F1245C/V (~2%); all in ALK kinase domain
- ALK amplification: ~4%; often co-amplified with MYCN (double-hit)
- Germline ALK mutations: ~1% of cases; familial neuroblastoma predisposition; F1174L and R1275Q also seen germline; allo-SCT not standard but monitoring
- ALK inhibition: crizotinib (1st gen, minimal NB activity due to F1174L resistance), alectinib (2nd gen), **lorlatinib** (3rd gen, highly active vs F1174L and R1275Q; Phase 3 ANBL2232 currently enrolling)

**Segmental chromosomal aberrations (SCAs):**
- **1p36 deletion (~35%):** Tumor suppressor (CHD5, miR-34a) loss → adverse
- **11q aberration (~35%, predominantly deletion):** Poorly characterized TSG; correlates with poor prognosis in MYCN-wild-type tumors
- **17q gain (~60%):** Most common cytogenetic change; gene dosage effects (BIRC5/survivin, NME1); adverse prognostic factor
- **1p and 11q are mutually exclusive** with MYCN amplification in most cases → different genomic evolution pathways

**TERT and ATRX (telomere maintenance alterations):**
- TERT structural variants (SVs): ~20-25% high-risk NB; chromosomal rearrangements juxtapose strong enhancers to TERT → TERT overexpression → telomere maintenance → immortality; adverse prognostic impact
- ATRX mutations: ~5-10% older children (>6 years); ATRX loss → ALT (alternative lengthening of telomeres) pathway; co-occurs with 11q aberration; not MYCN-amplified; older age at diagnosis NB with ALT has poor prognosis
- MYCN amp, TERT-SV, and ATRX-LOF are mutually exclusive telomere maintenance mechanisms

**Ploidy:**
- Hyperdiploidy (3N, triploid) in ~50% of infants: correlates with whole-chromosome gains, favorable histology, low-risk disease, excellent response to moderate chemotherapy
- Near-diploid/near-tetraploid (>4N) in high-risk: correlates with segmental chromosomal aberrations, MYCN amplification, poor prognosis

**RAS/MAPK at relapse:**
Acquired at relapse in ~80% of NB: ALK mutations (predominantly F1174L/R1275Q), NRAS, KRAS, NF1, BRAF → constitutive MAPK → chemotherapy resistance; MEK inhibitors (trametinib), lorlatinib being evaluated in relapsed setting.

### Histological classification — Shimada

Histologic classification by **International Neuroblastoma Pathology Classification (INPC, Shimada)**:
- **Favorable histology:** Well-differentiated neuroblastoma (ganglion cells), ganglioneuroblastoma (intermixed), low mitosis-karyorrhexis index (MKI)
- **Unfavorable histology:** Undifferentiated NB, poorly differentiated NB with high MKI, stroma-poor pattern
- Histology assigned favorable or unfavorable based on Schwann cell stroma richness, degree of differentiation, MKI, and patient age

## Function

### Neural crest origin and sympathoadrenal development

**Normal sympathoadrenal development:**
Neural crest cells (NCCs) delaminate from dorsal neural tube → migrate along ventrolateral pathway → dorsal aorta → sympathetic ganglia (sympathoblasts) or adrenal medulla (chromaffin cells). Key transcription factors: HAND2, PHOX2B, DBH (dopamine β-hydroxylase), TH (tyrosine hydroxylase), GATA2/3. **PHOX2B** is the master regulator of sympathoadrenal fate — germline PHOX2B polyalanine expansions cause congenital central hypoventilation syndrome (Ondine's curse) + NB predisposition.

Neuroblastoma represents arrest at various stages of sympathoadrenal differentiation:
- Undifferentiated NB: arrested at sympathoblast stage (MYCN-amplified, high MKI)
- Ganglioneuroblastoma: partial differentiation toward ganglion cells
- Ganglioneuroma: complete differentiation, benign → no treatment needed after resection

### Tumor biology

**Catecholamine secretion:**
~90% of NB produce catecholamines (dopamine, norepinephrine, epinephrine) and their metabolites (VMA — vanillylmandelic acid, HVA — homovanillic acid); elevated urine VMA/HVA is a diagnostic biomarker and response marker during treatment; some tumors are non-secretory (HVA/VMA normal); VIP-secreting tumors → secretory diarrhea (Verner-Morrison-like).

**MIBG (metaiodobenzylguanidine) avidity:**
~90% of NB tumors are MIBG-avid (take up norepinephrine transporter substrate MIBG → ¹²³I-MIBG for diagnosis/staging; ¹³¹I-MIBG for therapy); non-MIBG-avid NB → ¹⁸F-FDG PET-CT for staging; MIBG avidity is predictive of ¹³¹I-MIBG therapeutic response.

**Paraneoplastic — opsoclonus-myoclonus-ataxia (OMA):**
~2-3% of NB; autoimmune attack on cerebellar neurons by anti-NB antibodies (anti-Hu, anti-ANNA-1); OMA NB is typically localized (lower-risk, often favorable histology); paradoxically good tumor prognosis but poor neurological prognosis (chronic OMA with cognitive/behavioral sequelae); treatment: ACTH + IVIG + rituximab for OMA; surgical resection of NB does not consistently improve OMA.

## Pathology

### Staging — INRGSS

| Stage | Definition |
|-------|-----------|
| L1 | Localized tumor confined to one body compartment; no image-defined risk factors (IDRFs) |
| L2 | Localized tumor with one or more IDRFs |
| M | Distant metastatic disease (except Stage MS) |
| MS | Metastatic disease in patients <18 months; metastases limited to skin, liver, and/or bone marrow (<10% marrow involvement); not bone cortex |

**Image-defined risk factors (IDRFs):** Anatomical structures that predict incomplete resection (encasement of vessels, organ invasion, intraspinal extension); defined on CT/MRI pre-operatively.

### Risk classification (INRG)

Risk is determined by INRG stage, MYCN status, histology (Shimada), ploidy, SCAs (1p, 11q), and age:
- **Low risk:** L1 any age; MS with no MYCN amp; ~1% of cases are truly low-risk with MYCN amp (rare exception)
- **Intermediate risk:** L2 (certain histology/age combinations), MS with SCAs or unfavorable histology, M <18 months favorable biology
- **High risk:** MYCN amplification (any stage, any age); M disease ≥18 months; L2 with unfavorable histology; most M-stage disease; 4-year EFS ~40-50% historically, improving to ~60-70% with modern regimens

### Treatment

**Low-risk:**
Surgery alone for L1 stage (IDRF-absent, favorable histology); observation for Stage MS with favorable biology (spontaneous regression expected); 5-year EFS >95%; chemotherapy reserved for symptomatic low-risk (hepatomegaly, respiratory compromise in MS).

**Intermediate-risk:**
Surgical resection + moderate chemotherapy (carboplatin/etoposide alternating with cyclophosphamide/doxorubicin/vincristine × 4-8 cycles); no radiation; 3-year EFS ~90-95%; no tandem SCT or dinutuximab required.

**High-risk (current COG backbone ANBL1232/ANBL2032):**
1. **Induction (5-6 cycles):** Alternating cycles of high-dose cisplatin/etoposide/doxorubicin/cyclophosphamide (CEDE) and vincristine/topotecan/cyclophosphamide (VTC) → tumor shrinkage, metastatic disease control; CR/PR >90%
2. **Local control:** Surgical resection of primary tumor (nephron-sparing if adjacent to kidney) + local RT (21.6 Gy) to primary tumor bed ± residual metastatic sites
3. **Consolidation — tandem autologous SCT:** ANBL12P1 (Phase 3 RCT, N=652): tandem SCT (Arm A: carboplatin/etoposide/melphalan + thiotepa/cyclophosphamide) vs single SCT (Arm B: carboplatin/etoposide/melphalan); 3-year EFS 61.9% vs 48.4% (p=0.007); tandem SCT now standard of care [^park-2019-tandem-sct-nb]
4. **Maintenance (6 cycles dinutuximab, 6 cycles 13-cis-RA):** ANBL0032 (Phase 3 RCT, N=226): dinutuximab (anti-GD2) + GM-CSF + IL-2 + isotretinoin vs isotretinoin alone post-consolidation; 2-year EFS 66% vs 46% (HR 0.57, p=0.01); 2-year OS 86% vs 75% (p=0.02); FDA approved 2015 [^yu-2010-dinutuximab-nb]; adverse effects: neuropathic pain (Grade 3-4 ~50%), capillary leak, hypotension
5. **ALK-aberrant high-risk (Phase 3 ANBL2232):** Lorlatinib added to induction chemotherapy backbone for patients with ALK GOF mutation or amplification; results pending

**¹³¹I-MIBG therapy:**
¹³¹I-MIBG (iobenguane I-131): delivers high-dose β-radiation to MIBG-avid NB cells; FDA approved (Azedra) for MIBG-avid pheochromocytoma/paraganglioma; used off-label/protocol for R/R MIBG-avid NB (ORR ~25-36%); ANBL09P1: ¹³¹I-MIBG + high-dose chemotherapy before tandem SCT in Phase 2.

**Relapsed/refractory NB:**
Near-universal lethality; no standard salvage with curative intent:
- Irinotecan + temozolomide (IRET): ORR ~15-20%; most common backbone
- Dinutuximab beta (tanezumab-MIBG): anti-GD2 combinations
- DFMO (eflornithine/ODC inhibitor) + IRET: Phase 2 improved PFS
- ALK inhibitors: lorlatinib (Phase 1/2 for R/R): ORR ~20-40% in ALK-mutant
- NKTR-358/LY3434172 and other immune approaches: Phase 1
- Allo-SCT: occasionally attempted but not standard

**Long-term effects:**
High-risk NB survivors face significant treatment-related late effects:
- Hearing loss: cisplatin-induced sensorineural hearing loss (~30-50% requiring hearing aids)
- Growth: spinal RT → scoliosis, short stature
- Cardiac: doxorubicin → cardiomyopathy
- Secondary malignancy: alkylator/etoposide exposure → secondary AML/MDS
- Hypothyroidism: neck/mediastinal RT
- Renal: cisplatin nephrotoxicity

### Spontaneous regression — Stage MS

Stage MS (metastatic, <18 months, skin/liver/bone marrow only, MYCN wild-type): ~50-75% undergo spontaneous tumor regression or maturation; mechanism: TRKA (NTRK1) expression → nerve growth factor (NGF)-induced differentiation/apoptosis; Stage MS cells respond to NGF by undergoing apoptosis (pro-differentiation paradox); MYCN-amplified tumors have lost TRKA → no NGF response → aggressive disease; observation ± supportive care (corticosteroids for massive hepatomegaly compressing respiratory system) → excellent outcomes (~95% 3-year EFS).

## Connections

- `connects-to` → **[MYCN](../../03-molecular/mycn/README.md)** — MYCN amplification (~20% overall, ~40% high-risk NB) is the primary risk-stratification biomarker; AURKA stabilizes MYCN protein; MYCN drives proliferation and blocks differentiation; MYCN amplification confers high-risk designation regardless of age or stage.
- `connects-to` → **[ALK](../../03-molecular/alk/README.md)** — ALK GOF mutations (F1174L, R1275Q) in ~10-14% NB; ALK amplification in ~4%; ALK and MYCN co-amplification → double-hit worst prognosis; lorlatinib in Phase 3 ANBL2232; PHOX2B and ALK co-mutated in familial NB predisposition.
- `connects-to` → **[RET](../../03-molecular/ret/README.md)** — Neural crest-derived NB cells co-express RET during sympathoadrenal development; GDNF-RET signaling is required for sympathetic ganglion formation; retinoic acid-induced differentiation upregulates RET; RET mutations are not primary NB drivers.
- `connects-to` → **[P53](../../03-molecular/p53/README.md)** — TP53 mutations are rare at NB diagnosis (~1-2%) but acquired in ~80% of relapsed NB; MDM2 amplification (~4%) functionally inactivates p53; MYCN drives MDM2-dependent p53 suppression; MDM2 inhibitors (idasanutlin) explored in relapsed MYCN-amplified NB.
- `connects-to` → **[NTRK](../../03-molecular/ntrk/README.md)** — TRKA (NTRK1) drives NGF-induced differentiation/apoptosis in Stage MS NB, enabling spontaneous regression; MYCN-amplified NB loses TRKA so NGF cannot trigger regression, yielding aggressive disease; rare ETV6-NTRK3 and other NTRK fusions respond to larotrectinib/entrectinib.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — The adrenal medulla is the single most common NB primary site (~40%); NB arises from arrested sympathoadrenal chromaffin/neuroblast precursors of neural-crest origin; it presents as an MIBG-avid adrenal mass secreting catecholamine metabolites (urine VMA/HVA).
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Dinutuximab (anti-GD2) kills NB via NK-cell ADCC and complement-dependent cytotoxicity; GM-CSF enhances NK/monocyte effector function; IL-2 expands NK cells in COG ANBL0032 maintenance; NK-mediated immunotherapy improved high-risk NB event-free survival.
- `connects-to` → **[Neuroendocrine Tumors](../neuroendocrine-tumors/README.md)** — Neuroblastoma and adult neuroendocrine tumors are both neural-crest/neuroendocrine cancers that secrete amines and take up amine tracers, but differ sharply: neuroblastoma is an aggressive embryonal tumor of young children (MYCN-driven), NETs mostly indolent tumors of adults.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Bone marrow is the most common metastatic site in high-risk neuroblastoma: small-round-blue-cell nests infiltrate the marrow (stage M), detected by bilateral biopsies and MIBG scan, and clearing marrow disease is a key goal of induction chemotherapy and anti-GD2 immunotherapy.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Neuroblastoma is a tumor of arrested sympathetic neuroblasts: its cells span a spectrum from neuroblastoma through ganglioneuroblastoma to benign ganglioneuroma, and retinoic acid pushes residual cells toward mature neurons — the basis of isotretinoin maintenance after therapy.
- `connects-to` → **[Pheochromocytoma/Paraganglioma](../pheochromocytoma-paraganglioma/README.md)** — Neuroblastoma and pheochromocytoma both arise from sympathoadrenal neural-crest cells: neuroblastoma is the malignant childhood tumor of immature sympathetic precursors, while pheochromocytoma is its catecholamine-secreting adult counterpart—both seen on MIBG.
- `connects-to` → **[Wilms Tumor](../wilms-tumor/README.md)** — Neuroblastoma and Wilms tumor are the two commonest extracranial solid tumors of early childhood and key differentials for an abdominal mass: neuroblastoma is an adrenal/sympathetic-chain tumor crossing the midline, while Wilms (nephroblastoma) is a renal tumor that respects it.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy treats high-risk neuroblastoma two ways: external-beam photon irradiation consolidates the primary site after surgery and chemo, while 131-I-MIBG delivers targeted internal radiation to MIBG-avid metastases—exploiting the tumor's radiosensitivity.
- `connects-to` → **[Ewing Sarcoma](../ewing-sarcoma/README.md)** — Neuroblastoma and Ewing sarcoma are both 'small round blue cell' childhood tumors that overlap on biopsy but are distinct: neuroblastoma arises from sympathetic neuroblasts, while Ewing arises in bone with EWSR1-FLI1 and CD99—immunostains separate them.
- `connects-to` → **[Medulloblastoma](../medulloblastoma/README.md)** — Neuroblastoma and medulloblastoma are both embryonal childhood tumors at different sites: neuroblastoma arises from peripheral sympathetic neuroblasts, medulloblastoma from cerebellar progenitors—peripheral versus central nervous-system embryonal cancers.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Neuroblastoma sits in the expanded Li-Fraumeni spectrum: germline TP53 loss modestly raises childhood neuroblastoma risk, and although most are sporadic, TP53-pathway inactivation contributes to aggressive, treatment-resistant relapses—linking it to the p53 guardian.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — Neuroblastoma arises from catecholamine-making cells: its sympathetic-lineage cells secrete norepinephrine precursors, so the urinary breakdown products VMA and HVA serve as diagnostic and monitoring markers—and catecholamine excess can cause hypertension.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Neuroblastoma is a cancer of the developing sympathetic nervous system: it arises from neural-crest-derived sympathetic precursors anywhere along the chain or in the adrenal medulla, so tumors appear in the abdomen, chest or neck wherever sympathetic tissue lies.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Neuroblastoma's stage 4S shows uncanny liver behavior: in infants, tumor can massively infiltrate the liver yet spontaneously regress without treatment—a striking exception to cancer's usual course that makes neuroblastoma's biology age-dependent.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Neuroblastoma is treated by harnessing the immune system: anti-GD2 antibodies (dinutuximab) target a glycolipid richly expressed on neuroblasts, and adding immunotherapy to high-risk regimens markedly improved survival—a landmark for solid-tumor immunotherapy in children.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Proton therapy is favored for neuroblastoma in young children: the tumor often sits near the spine, kidneys and liver, so protons' lack of exit dose limits damage to developing organs and lowers the risk of radiation-induced second cancers.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — GD2-directed cell therapy targets neuroblastoma via cytotoxic T cells: CAR-T cells engineered against the GD2 antigen are in trials to kill neuroblasts, extending the anti-GD2 strategy from antibodies to engineered T-cell immunity.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Neuroblastoma is targeted with radioactive iodine via MIBG: the tumor takes up metaiodobenzylguanidine like norepinephrine, so I-123 MIBG scans light up disease and I-131 MIBG delivers radiation directly to neuroblastoma cells in high-risk patients.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — High-risk neuroblastoma keeps its telomeres long: TERT activation (or ATRX-driven alternative lengthening) lets cells divide endlessly, and this telomere-maintenance switch—alongside MYCN—marks the aggressive tumors that need intensive therapy.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Anti-GD2 immunotherapy enlists macrophages: the antibody dinutuximab coats neuroblastoma's GD2 antigen so macrophages and complement (with NK cells) destroy it, a now-standard treatment that improved survival in high-risk disease.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Neuroblastoma betrays its neural-crest origin by making dopamine: arising from sympathetic precursors, it synthesizes catecholamines whose breakdown products (HVA from dopamine, VMA from noradrenaline) spill into urine as diagnostic tumor markers.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Neuroblastoma defends itself with regulatory T cells: a suppressive microenvironment rich in Tregs blunts the immune attack, a barrier that anti-GD2 antibody immunotherapy (dinutuximab) must overcome to clear high-risk disease.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — High-risk neuroblastoma is intensely angiogenic via VEGF: the tumor drives new blood vessels to fuel rapid growth and spread, and high vascularity marks aggressive disease—making anti-angiogenic strategies a research target.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Infant neuroblastoma can stud the skin: in the special 4S stage, blue-tinged skin nodules ('blueberry muffin') appear alongside liver and marrow spread, yet this pattern often regresses on its own—a striking exception to the cancer's usual aggressiveness.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells anchor neuroblastoma immunotherapy: presenting tumor antigens, they help prime the T-cell and anti-GD2 responses that have improved survival, and dendritic-cell vaccines are explored to boost immunity against residual disease.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Neuroblastoma's ALK mutations signal through AKT: activated ALK drives the PI3K-AKT-mTOR pathway to fuel growth and survival, so AKT-pathway inhibitors are studied alongside ALK inhibitors in the high-risk, MYCN-amplified disease.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Neuroblastoma announces itself in the eyes: spread to the bones around the orbit causes the 'raccoon eye' bruising, and the paraneoplastic opsoclonus-myoclonus brings the 'dancing eyes' that can be the first clue.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Neuroblastoma eats away calcium-rich bone: it metastasizes widely to the cortical skeleton, eroding the bone and causing the pain and fractures that mark high-risk, disseminated disease.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Neuroblastoma recruits endothelial cells to grow: VEGF from the tumor drives them to build a dense blood supply, and the degree of this angiogenesis tracks with the aggressive, high-risk forms.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy proves a tumor is neuroblastic: the beam reveals dense-core neurosecretory granules and slender neuritic processes packed with microtubules — ultrastructure that confirms neural origin when an undifferentiated small-round-blue-cell tumor defies routine stains.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Neuroblastoma is the great mimic of a kidney tumor: arising in the adrenal gland atop the kidney, it pushes the organ down and outward rather than springing from it — the displacement that distinguishes it on imaging from Wilms tumor.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Many neuroblastomas grow beside the lung: the posterior mediastinum, along the paraspinal sympathetic chain, is the second commonest primary site, where a chest mass can press on the airway or erode through the spinal foramina.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Neuroblastoma reaches the brain in two ways: it spreads to the dura and skull (the 'raccoon-eye' orbital deposits), and as a paraneoplastic syndrome it provokes opsoclonus-myoclonus, the 'dancing eyes' from an immune attack on the brain.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Some neuroblastomas flood the gut with hormone: a VIP-secreting tumor causes Kerner-Morrison syndrome, intractable watery diarrhea that drains the bowel and the body's potassium.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — The VIP-secreting neuroblastoma crashes the potassium: its relentless secretory diarrhea flushes potassium out of the body, a hypokalemia severe enough to threaten the heart until the tumor is removed.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — An antibody is now front-line therapy: dinutuximab targets the GD2 disialoganglioside coating neuroblastoma cells, marking them for immune killing, and the tumor can also trigger the autoantibodies of opsoclonus-myoclonus, the paraneoplastic 'dancing eyes' syndrome.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Cure means battering the marrow: high-dose chemotherapy and stem-cell transplant drop the neutrophil count to near zero, and the anti-GD2 antibody is paired with GM-CSF to coax neutrophils into helping kill the tumor.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Neuroblastoma packs the marrow at diagnosis: as the small round blue cells flood the bone marrow they crowd out red-cell production, and the resulting anemia, pale erythrocytes, and fatigue are often what bring a child to care.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — The same marrow takeover starves the platelets: tumor flooding the bone marrow suppresses platelet production into thrombocytopenia, so bruising and bleeding join the anemia among the presenting signs of widespread neuroblastoma.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Cisplatin in high-risk regimens wastes magnesium: the platinum chemotherapy injures the kidney tubule that reclaims the mineral, so blood magnesium falls and needs replacing, alongside watching for the drug's hearing loss and kidney damage.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Cure can cost future fertility: the intensive chemotherapy, total-body irradiation, and stem-cell transplant used for high-risk neuroblastoma damage the gonads, so the late effects on growth and fertility are part of survivor care for these children.
- `connects-to` → **[ATRX](../../03-molecular/atrx/README.md)** — An alternate route to the same cancer: ATRX mutations mark a distinct, often older-child neuroblastoma that keeps its telomeres long by recombination rather than telomerase, mutually exclusive with MYCN amplification and tied to a chronic, treatment-resistant course.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — It springs from the body's autonomic wiring: neuroblastoma arises from immature sympathetic neuroblasts of the peripheral nervous system, which is why it appears along the sympathetic chain and adrenal medulla and why favorable tumors can mature into benign nerve tissue.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — The tumor can drive up blood pressure: like its catecholamine-secreting cousins, some neuroblastomas pour out norepinephrine and dopamine, producing hypertension, sweating and flushing that can be the clue that leads to diagnosis.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — Cell-cycle escape marks the aggressive tumor: CDKN2A loss and other cell-cycle lesions cooperate with MYCN amplification in high-risk neuroblastoma, driving the rapid proliferation that defines the lethal subtype.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — The tumor and its cure both hurt the nerves: paraspinal neuroblastoma compresses nerve roots and the spinal cord, and platinum/vincristine chemotherapy adds a peripheral neuropathy — together a major pain burden in these children.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Intensive therapy strips the defenses: the high-dose chemotherapy and autologous transplant used for high-risk neuroblastoma cause prolonged neutropenia, making febrile neutropenia and sepsis a central treatment hazard.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 backs the high-risk tumor: MYCN-amplified neuroblastoma shows STAT3 activation that supports proliferation and immune evasion, a pathway explored where this childhood cancer resists intensive therapy.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Tumor and central lines clot the veins: neuroblastoma's hypercoagulable state, the long-term central venous catheters and the immobility of intensive treatment together raise venous thromboembolism risk in these children.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Marrow metastasis and inflammation drain the blood: high-risk neuroblastoma commonly infiltrates the bone marrow and raises inflammatory cytokines, producing anemia from both crowding and chronic disease.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its anthracyclines scar the developing heart: the doxorubicin in high-risk neuroblastoma regimens is dose-dependently cardiotoxic, risking a cardiomyopathy and heart failure that can emerge years into survivorship.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — High-dose therapy strips the lung's defenses: the intensive chemotherapy and autologous stem-cell transplant for high-risk neuroblastoma cause profound neutropenia, letting inhaled Aspergillus invade as pulmonary aspergillosis.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Its platinum chemo scars young kidneys: the cisplatin and carboplatin central to neuroblastoma regimens are nephrotoxic, and in a child the tubular and electrolyte injury can leave lasting chronic kidney impairment.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Transplant immunosuppression reawakens shingles: the autologous stem-cell transplant and immunotherapy for high-risk neuroblastoma deplete T-cell immunity, allowing latent varicella-zoster to reactivate.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Resecting an abdominal mass heals slowly: the wide surgical removal of a neuroblastoma, often after chemotherapy in a malnourished child, leaves large wounds prone to dehiscence and delayed closure.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Childhood cancer breeds enduring worry: the intensive treatment, relapse risk and long survivorship surveillance of high-risk neuroblastoma foster chronic anxiety in survivors and their families.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It spreads to bone and marrow: high-risk neuroblastoma metastasises avidly to the bones and bone marrow, causing bone pain, limping and the periorbital 'raccoon eyes' of orbital deposits.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Its mass and hormones disturb the gut: an abdominal or adrenal neuroblastoma compresses the bowel, and VIP-secreting tumours cause a profuse, intractable secretory diarrhoea.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It is a hormone-secreting neural-crest tumour: arising from the sympathoadrenal lineage, neuroblastoma secretes catecholamines and sometimes VIP, and MIBG therapy requires thyroid protection.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It shows on the skin and around the eyes: infants with stage MS disease develop blue 'blueberry muffin' skin nodules, and orbital metastases cause periorbital 'raccoon eye' ecchymoses.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Thoracic tumours crowd the chest: a posterior mediastinal neuroblastoma can compress the airway and spinal cord, and the disease can rarely metastasise to the lungs.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It spreads through the nodes: neuroblastoma disseminates to regional and distant lymph nodes, part of the staging that guides its risk-stratified treatment.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It floods the body with catecholamines: neuroblastoma can secrete catecholamines causing hypertension, and its anthracycline chemotherapy adds long-term cardiotoxicity.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It crowds and is treated near the kidney: adrenal and paraspinal neuroblastomas compress the kidney and ureter, and cisplatin chemotherapy is nephrotoxic.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — It is treated by precision agents: anti-GD2 immunotherapy (dinutuximab) and MIBG-targeted radiotherapy exploit neuroblastoma's neural markers in high-risk disease.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Intensive chemo for high-risk disease: high-risk neuroblastoma is treated with multi-agent induction chemotherapy and high-dose therapy with autologous stem-cell rescue.
- `connects-to` → **[CAR-T](../../../03-medicine/01-modern/13-cancer/car-t/README.md)** — GD2 cell therapy shows promise: GD2-directed CAR-T cells, building on the success of anti-GD2 antibodies, have produced responses in relapsed neuroblastoma, a leading solid-tumour CAR-T target.
- `connects-to` → **[MPNST](../mpnst/README.md)** — A fellow neural-crest tumour: like malignant peripheral nerve sheath tumour, neuroblastoma derives from neural-crest lineage, the two among the nerve-associated malignancies of childhood and young adults.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Its metastases love bone: neuroblastoma spreads to cortical bone and marrow—skull and orbits producing periorbital bruising ('raccoon eyes')—and these deposits, rich in catecholamine metabolism, are imaged with MIBG scintigraphy.
- `connects-to` → **[Diffuse Midline Glioma](../diffuse-midline-glioma/README.md)** — A shared GD2 immunotherapy target: the disialoganglioside GD2 that anti-GD2 antibodies and CAR-T target in neuroblastoma is also highly expressed on diffuse midline glioma, where GD2 CAR-T has produced striking early responses.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — An immunologically cold childhood tumour: neuroblastoma has a low mutational burden and responds poorly to PD-1 checkpoint inhibitors, so its immunotherapy relies on anti-GD2 antibodies and CAR-T rather than checkpoint blockade.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Stage 4S liver disease: in infant 4S neuroblastoma, tumour floods the hepatic lobule causing massive hepatomegaly that can spontaneously regress—a behaviour unique among cancers.
- `connects-to` → **[Retinoblastoma](../retinoblastoma/README.md)** — Two infant cancers, opposite genetics: neuroblastoma (MYCN amplification, an oncogene) and retinoblastoma (RB1 loss, a tumour suppressor) are both classic tumours of infancy from contrasting molecular routes.
- `connects-to` → **[Rhabdomyosarcoma](../rhabdomyosarcoma/README.md)** — A small-round-blue-cell mimic: neuroblastoma joins rhabdomyosarcoma, Ewing sarcoma and lymphoma in the childhood small-round-blue-cell differential, distinguished by neuroendocrine markers and urinary catecholamines.
- `connects-to` → **[NSCLC](../nsclc/README.md)** — A shared druggable driver: ALK rearrangements in lung cancer and activating ALK mutations in neuroblastoma make the same kinase targetable in both, so ALK inhibitors like lorlatinib cross from adult NSCLC into paediatric neuroblastoma.
- `connects-to` → **[AML](../aml/README.md)** — Therapy-related leukaemia: the high-dose alkylator chemotherapy and stem-cell transplant used for high-risk neuroblastoma damage the marrow, occasionally causing secondary myelodysplasia and acute myeloid leukaemia in survivors.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Cardiotoxic survivorship: anthracyclines in high-risk neuroblastoma regimens injure the myocardium, leaving childhood survivors at lifelong risk of cardiomyopathy and heart failure decades later.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Apoptosis evasion: neuroblastoma depends on anti-apoptotic BCL-2 family proteins for survival, a vulnerability targeted by BH3-mimetic drugs.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Cell-cycle drive: CDK4/6-cyclin D activity, amplified by MYCN, propels neuroblastoma proliferation, making CDK4/6 inhibition an investigational strategy.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — MYCN's epigenetic effector: MYCN upregulates EZH2 to enforce the repressive, anti-differentiation chromatin programme of high-risk neuroblastoma.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — MYC-family alternative: in MYCN-non-amplified neuroblastoma, c-MYC drives a similar high-risk transcriptional programme, the two MYC-family oncogenes converging on aggressive disease.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Growth-signal hub: PI3K/AKT/mTOR signalling stabilises MYCN and drives the protein synthesis that fuels neuroblastoma growth, a rationale for mTOR-pathway inhibition.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Tumour hypoxia: HIF-1α stabilised in the hypoxic neuroblastoma drives angiogenesis and an undifferentiated, aggressive phenotype linked to poor outcome.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ALK-RAS-MAPK: activating ALK mutations signal through RAS-RAF-ERK to drive neuroblastoma proliferation, the rationale for ALK inhibitors in the ALK-mutant subset.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Differentiation and apoptosis: retinoic acid and chemotherapy drive neuroblastoma cells toward caspase-3-mediated apoptosis and differentiation, the basis of maintenance therapy in high-risk disease.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Macrophage microenvironment: CCL2 recruits tumour-associated macrophages into neuroblastoma, contributing to the immunosuppressive niche of this often immunologically cold childhood tumour.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCR4 on neuroblastoma cells follows CXCL12 gradients to the bone marrow and bone, the hallmark metastatic sites whose involvement defines the high-risk metastatic (stage M) disease that drives most neuroblastoma mortality.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Anti-GD2 antibody (dinutuximab) directs NK cells and macrophages to kill neuroblastoma, with NK perforin-mediated cytotoxicity a key effector of the immunotherapy that meaningfully improved survival in high-risk disease.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — MYCN-amplified neuroblastoma is immunologically cold with suppressed cGAS-STING signaling, and restoring this innate DNA-sensing pathway is being explored to inflame the tumor and make it responsive to immunotherapy.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — High-risk neuroblastomas express TrkB and respond to its ligand BDNF with an autocrine survival, angiogenic and chemoresistance loop, the neurotrophin axis that distinguishes aggressive disease from the TrkA-expressing tumors prone to regress.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Neuroblastoma arises from sympathoadrenal neural-crest progenitors, and Wnt/β-catenin signaling that patterns neural-crest development is co-opted to sustain the proliferative, undifferentiated state of the tumor.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — With few recurrent mutations, neuroblastoma is driven heavily by epigenetic dysregulation—MYCN-bound super-enhancers and DNA-methylation programs—making the epigenome a key therapeutic target in this developmental cancer.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — ALK and growth-factor signaling drive PI3K-AKT-mTOR (AKT and mTOR already mapped), which stabilizes MYCN protein (mapped), coupling PI3K activity to the central oncogenic driver of high-risk neuroblastoma.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — The CDK4/6 axis (CDK4/6 and CDKN2A already mapped) releases E2F1, and MYCN transactivates E2F target genes to drive the cell-cycle progression of neuroblastoma.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — ALK signals through RAS-MAPK (ERK1/2 mapped), and activating RAS-pathway mutations are enriched at neuroblastoma relapse as a mechanism of treatment resistance.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — The RB1-E2F checkpoint (CDK4/6, CDKN2A and E2F1 already mapped) restrains proliferation, and its dysregulation in high-risk neuroblastoma is a target of CDK4/6 inhibition.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — TP53 is rarely mutated in neuroblastoma; instead MDM2 amplification (transactivated by MYCN) inactivates wild-type p53 (already mapped), an actively pursued MDM2-p53 therapeutic axis.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK-STAT3 signaling (STAT3 already mapped) supports the survival and immunosuppressive microenvironment of neuroblastoma.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 modulates neuroblastoma differentiation, survival and the immune microenvironment.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β signaling shapes neuroblastoma differentiation and the immunosuppressive tumor microenvironment.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — Loss of PTEN restraint on PI3K-AKT-mTOR signaling (AKT, PIK3CA and mTOR mapped) cooperates with MYCN amplification in high-risk neuroblastoma.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the immunologically cold microenvironment of high-risk neuroblastoma, relevant to its anti-GD2 and emerging immunotherapy.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling shapes the differentiation block and immunosuppressive microenvironment of neuroblastoma.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors, restrained by the PTEN-PI3K-AKT axis, regulate the survival and differentiation of the neural-crest-derived cells of neuroblastoma.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the MYCN stability and survival signaling of neuroblastoma.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the immunosuppressive microenvironment of the immune-cold high-risk neuroblastoma.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-kinase signaling downstream of ALK and TrkB (ALK and NTRK already mapped) drives the survival and invasion of neuroblastoma.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and therapy resistance of the MYCN-amplified cells of neuroblastoma.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling contributes to the epigenetic dysregulation of neuroblastoma.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of the MYCN-driven cells of neuroblastoma.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of neuroblastoma.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of neuroblastoma.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH signaling participates in the differentiation and stemness biology of neuroblastoma.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of neuroblastoma.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of neuroblastoma.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of neuroblastoma.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the tumor microenvironment of neuroblastoma.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of neuroblastoma.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin (SPP1) participates in the tumor microenvironment, metastasis, and bone-marrow involvement of neuroblastoma.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Anti-GD2 immunotherapy: high-risk neuroblastoma is treated with the anti-GD2 antibody dinutuximab combined with IL-2 and GM-CSF, and IL-2-driven immune-cell activation (perforin already mapped) enhances antibody-dependent killing of the tumour.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immune escape: neuroblastoma frequently downregulates MHC antigen presentation to evade T cells, one reason antibody-based (GD2) rather than T-cell approaches have led its immunotherapy, though restoring presentation is an active strategy.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Checkpoint context: neuroblastoma is an immunologically cold tumour with low mutational burden, and PD-1 checkpoint blockade is being tested in combination with anti-GD2 and other therapies to boost the anti-tumour response.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Marrow infiltration: bone-marrow metastasis (already mapped) by neuroblastoma and the intensive multidrug chemotherapy suppress erythropoiesis, lowering haemoglobin and requiring transfusion in high-risk disease.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Anthracycline cardiotoxicity: the doxorubicin in high-risk neuroblastoma regimens is cardiotoxic, and troponin elevation helps detect the cumulative myocardial injury that threatens these very young long-term survivors.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 helps make neuroblastoma an immunologically cold tumour (PD-1 already mapped), dampening the T-cell response, one reason antibody-based anti-GD2 rather than checkpoint approaches have led its immunotherapy.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the cold, immune-evasive microenvironment of neuroblastoma.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative stress: the proliferative neuroblastoma and its intensive chemotherapy generate oxidative stress, to which xanthine oxidase contributes, adding reactive oxygen species to the tumour microenvironment and treatment toxicity.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Transfusion and anaemia: the marrow involvement and intensive multimodal therapy of high-risk neuroblastoma (haemoglobin already mapped) cause anaemia needing transfusion, whose repeated support can load the young survivor with iron.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 tumour-associated macrophage niche of the immunosuppressive microenvironment of neuroblastoma.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper and catecholamines: copper is the cofactor of dopamine-β-hydroxylase, which makes noradrenaline from dopamine (both already mapped), the catecholamine biosynthesis of the neuroblastoma cells that secrete the VMA and HVA used to diagnose and monitor the tumour.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the angiogenesis and vascular tone of the highly vascular neuroblastoma, part of the stromal biology of the tumour.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Marrow-adipose adipokine: leptin from the marrow adipose tissue signals to the metastatic neuroblastoma cells in the bone marrow (already mapped), part of its metabolic microenvironment.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the marrow-adipose adipokine milieu of the metabolic microenvironment of metastatic neuroblastoma.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), completes the marrow-adipose adipokine signalling of the metabolic microenvironment of neuroblastoma.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the immunotherapy of neuroblastoma.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-neuroblastoma immunity augmented by the anti-GD2 plus IL-2 (already mapped) therapy.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the neuroblastoma immune microenvironment.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of neuroblastoma.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the neuroblastoma microenvironment.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2/AllergoOncology arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), is the antibody arm complementing the anti-GD2 (immunoglobulin already mapped) immunotherapy of neuroblastoma.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Humoral/GD2 arm: the B cells and the tertiary lymphoid structures underpin the antibody (anti-GD2 immunoglobulin already mapped) response harnessed by the dinutuximab immunotherapy of neuroblastoma.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of neuroblastoma.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of neuroblastoma.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Dinutuximab CDC: the complement C5 (with C3 already mapped) is an effector of the complement-dependent cytotoxicity of the anti-GD2 dinutuximab, alongside the NK-cell (already mapped) ADCC, against neuroblastoma.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the myeloid recruitment into the neuroblastoma stroma.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the neuroblastoma cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), a resistance mechanism to the anti-GD2 complement-dependent killing.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Bone marrow and treatment anaemia: EPO receptors on sympathetic neuroblasts (already mapped) confer neuroprotection; EPO-stimulating agents counter the severe myelosuppression from the high-dose chemotherapy and autologous stem-cell transplant used in high-risk neuroblastoma.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell catecholamine stroma: histamine from the mast cells infiltrating neuroblastoma stroma promotes angiogenesis (VEGF already mapped); neuroblastoma-released catecholamines amplify mast-cell degranulation and H2 receptor signalling on the NB cells promotes proliferation.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Bone pain mediator: bradykinin activates B2 receptors at the bone and bone-marrow (already mapped) metastasis sites of high-risk neuroblastoma, contributing to the severe neuropathic bone pain and amplifying the NF-kB (already mapped) pro-tumour inflammatory signalling.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Tumour-immune alarmin: TSLP released by the neuroblastoma stroma activates dendritic cells (already mapped) toward a Th2 (IL-4 already mapped) immune microenvironment, amplifying TGF-β (already mapped) immunosuppression and attenuating NK-cell (already mapped) cytotoxicity.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement immunotherapy modulation: C1-INH controls the classical-pathway arm (complement C3, C5 and C5aR1 already mapped) in neuroblastoma, modulating the complement-dependent cytotoxicity triggered by dinutuximab (antibody already mapped) anti-GD2 immunotherapy.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Bone marrow niche periostin: periostin secreted by the bone-marrow (already mapped) stromal fibroblasts in neuroblastoma metastases activates integrin-AKT (already mapped) pro-survival signalling and promotes VEGF-driven (already mapped) angiogenesis in high-risk neuroblastoma.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Tumour-suppressive pineal hormone: melatonin inhibits neuroblastoma proliferation through MT1/MT2 receptor-mediated cAMP-PKA suppression and p53 (already mapped)-dependent apoptosis, counteracting MYCN (already mapped) oncogenic drive.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Catecholamine cross-talk: neuroblastoma arises from sympathoadrenal precursors sharing the catecholamine pathway with adrenal androgen production; testosterone converges on AR signalling to modulate NB differentiation and MYCN (already mapped) expression.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Catecholamine pathway co-regulator: neuroblastoma tumour cells express the serotonin transporter (SERT; already mapped) and metabolise 5-HIAA alongside catecholamines; serotonin receptor activation modulates cAMP-PKA signalling (MYCN already mapped) and NB cell proliferation.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — NB prolactin neuro-immune: prolactin, via PRLR on neuroblastoma macrophages (already mapped) and mast cells (already mapped), upregulates IL-6 (already mapped) and VEGF-driven (already mapped) pro-tumour signalling, promoting the immunosuppressive TME of neuroblastoma.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — NB oxytocin anti-tumour: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped) in the neuroblastoma stroma, attenuates IL-6 (already mapped) and VEGF-driven (already mapped) pro-tumour signalling in the neuroblastoma microenvironment.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — NB vasopressin vascular: vasopressin, via V1aR on neuroblastoma macrophages (already mapped) and mast cells (already mapped), modulates the tumour vascular niche; dysregulation amplifies IL-6 (already mapped) and VEGF (already mapped) pro-tumour signalling in neuroblastoma.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — NB selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS in the neuroblastoma TME; selenium deficiency amplifies the IL-6 (already mapped) and mTOR (already mapped) oxidative tumour cascade of neuroblastoma.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — NB sodium: high dietary sodium promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory activation; sodium-induced IL-6 (already mapped) and mTOR (already mapped) signalling amplifies the T-cytotoxic (already mapped) tumour cascade of neuroblastoma.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — NB zinc: zinc, as cofactor of antioxidant enzymes in macrophages (already mapped) and neutrophils (already mapped), attenuates oxidative stress; zinc deficiency amplifies the IL-6 (already mapped) and mTOR (already mapped) pro-tumour cascade of neuroblastoma.

[^yu-2010-dinutuximab-nb]: Yu AL, Gilman AL, Ozkaynak MF, et al. Anti-GD2 antibody with GM-CSF, interleukin-2, and isotretinoin for neuroblastoma. *N Engl J Med.* 2010;363(14):1324-1334. [doi:10.1056/NEJMoa0911123](https://doi.org/10.1056/NEJMoa0911123) · [PubMed 20879881](https://pubmed.ncbi.nlm.nih.gov/20879881/)
[^park-2019-tandem-sct-nb]: Park JR, Kreissman SG, London WB, et al. Effect of tandem autologous stem cell transplant vs single transplant on event-free survival in patients with high-risk neuroblastoma: a randomized clinical trial. *JAMA.* 2019;322(8):746-755. [doi:10.1001/jama.2019.11642](https://doi.org/10.1001/jama.2019.11642) · [PubMed 31454023](https://pubmed.ncbi.nlm.nih.gov/31454023/)

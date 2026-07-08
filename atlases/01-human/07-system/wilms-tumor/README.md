---
schema: human-scale-entry/v1
id: wilms-tumor
name: Wilms Tumor
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Wilms tumor (nephroblastoma) is the most common pediatric renal malignancy; peak age 3-4 years; favorable histology ~90% with 4-year OS >95%; anaplastic ~10% with TP53 mutations; WT1/CTNNB1/WTX/DROSHA drivers; actinomycin D+vincristine±doxorubicin backbone."
aliases: ["Wilms tumor", "nephroblastoma", "Wilms' tumor", "pediatric kidney cancer", "childhood renal tumor", "nephroblastoma WAGR", "Wilms anaplastic"]
sources:
  - id: dome-2015-wilms
    type: peer-reviewed
    cite: "Dome JS, Graf N, Geller JI, et al. Advances in Wilms tumor treatment and biology: progress through international collaboration. J Clin Oncol. 2015;33(27):2999-3007."
    doi: "10.1200/JCO.2015.62.1888"
    pmid: "26261251"
    url: "https://doi.org/10.1200/JCO.2015.62.1888"
  - id: dix-2006-arenl0002
    type: peer-reviewed
    cite: "Dix DB, Bhatt SM, Geller JI, et al. Treatment of Stage IV favorable histology Wilms tumor with incomplete lung metastasis response after chemotherapy: a report from Children's Oncology Group Study AREN0533. J Clin Oncol. 2018;36(16):1564-1570."
    doi: "10.1200/JCO.2017.77.1877"
    pmid: "29584550"
    url: "https://doi.org/10.1200/JCO.2017.77.1877"
cross_links:
  - target: 01-human/03-molecular/wt1
    relation: connects-to
    note: "WT1 mutations occur in ~10-15% sporadic Wilms tumor and are near-universal in WAGR and Denys-Drash syndromes; WT1+CTNNB1 co-mutation → blastemal-predominant Wilms from intralobar nephrogenic rests; WT1 is required for nephron formation from metanephric blastema."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "CTNNB1 activating mutations occur in ~15-20% Wilms tumor, co-occurring with WT1 mutations; nuclear β-catenin marks the blastemal component; WNT activation promotes blastema self-renewal and prevents epithelial differentiation; WNT inhibitors studied preclinically."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 mutations occur in ~70% of diffuse anaplastic Wilms (unfavorable histology); anaplasia is the strongest adverse prognostic factor; TP53 drives resistance to standard chemotherapy; anaplastic WT requires alkylator-based intensification (cyclophosphamide/etoposide)."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "IGF2 overexpression (~75% Wilms tumor via 11p15 imprinting loss) → IGF1R → PI3K-AKT-mTOR → proliferation; everolimus explored in relapsed Wilms; DROSHA/DGCR8 mutations impair miRNA biogenesis → mTOR derepression."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Wilms tumor (nephroblastoma) is the most common childhood kidney cancer, arising at age 3-4 from persistent, undifferentiated metanephric blastema; radical nephrectomy is the backbone, with nephron-sparing surgery reserved for bilateral disease to preserve renal function."
  - target: 01-human/04-cellular/podocyte
    relation: connects-to
    note: "WT1 is essential for podocyte function, so the WT1 mutations that cause Wilms tumor also cause glomerular disease: Denys-Drash (missense) brings diffuse mesangial sclerosis and infantile nephrotic syndrome, while Frasier (KTS splice) causes focal segmental glomerulosclerosis."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "The commonest molecular change in Wilms tumor (~75%) is loss of imprinting at 11p15 that doubles IGF2 dosage; excess IGF2 signals through IGF1R to PI3K-AKT-mTOR, driving nephroblast proliferation — the same locus whose disruption underlies Beckwith-Wiedemann overgrowth."
  - target: 01-human/07-system/rhabdomyosarcoma
    relation: connects-to
    note: "Wilms tumor and rhabdomyosarcoma are both embryonal childhood cancers of arrested development — Wilms from kidney blastema, RMS from myogenic precursors — sharing a key driver: 11p15.5 loss of imprinting doubles IGF2, feeding an IGF1R-PI3K-AKT-mTOR loop in both."
  - target: 01-human/07-system/neuroblastoma
    relation: connects-to
    note: "Wilms tumor and neuroblastoma are the two classic malignant abdominal masses of young children (ages 1-4): Wilms is an intrarenal nephroblastoma rarely crossing midline; neuroblastoma is an adrenal/sympathetic tumor that secretes catecholamines and often crosses."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Anaplastic (unfavorable-histology) Wilms tumor is defined by TP53 mutation, driving chemoresistance and worse prognosis; germline TP53 (Li-Fraumeni) is occasionally found with anaplasia or family history — linking Wilms to the p53-driven childhood cancer-predisposition spectrum."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "Wilms tumor and renal cell carcinoma are the kidney cancers of childhood versus adulthood: Wilms (nephroblastoma) is an embryonal tumor of nephron precursors curable with surgery and chemo, while RCC arises from mature tubular epithelium in adults, driven by VHL/HIF."
  - target: 01-human/07-system/ewing-sarcoma
    relation: connects-to
    note: "Wilms tumor's blastemal component enters the small-round-blue-cell differential with Ewing sarcoma: both are pediatric tumors of primitive cells, but Wilms is triphasic (blastema/epithelium/stroma) with WT1 changes while Ewing is EWSR1-FLI1-driven."
  - target: 01-human/07-system/retinoblastoma
    relation: connects-to
    note: "Wilms tumor and retinoblastoma are paradigm embryonal childhood cancers fitting Knudson's two-hit model: bilateral Wilms (often WT1-linked) parallels heritable bilateral retinoblastoma—germline loss of one suppressor allele plus a somatic second hit drives early tumors."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy is part of risk-adapted Wilms tumor cure: flank or whole-abdomen photon radiation is added for higher-stage or unfavorable-histology disease after nephrectomy and chemotherapy, contributing to Wilms' high cure rate."
  - target: 01-human/07-system/atypical-teratoid-rhabdoid-tumor
    relation: connects-to
    note: "Wilms tumor and rhabdoid tumors are distinct pediatric renal/CNS cancers: classic Wilms is a WT1-related nephroblastoma with good prognosis, while malignant rhabdoid tumor of the kidney (and CNS ATRT) is a SMARCB1-deficient, far more aggressive tumor."
  - target: 01-human/07-system/medulloblastoma
    relation: connects-to
    note: "Wilms tumor and medulloblastoma are both embryonal childhood tumors arising from developmental precursors: Wilms from metanephric blastema (WT1/Wnt), medulloblastoma from cerebellar progenitors—different organs, but both recapitulate arrested embryonic development."
  - target: 01-human/03-molecular/ctnnb1
    relation: connects-to
    note: "Wilms tumor is partly a Wnt-driven cancer: beta-catenin (CTNNB1) activating mutations, often with WT1 loss, derail the kidney's developmental Wnt signaling so nephron precursors keep proliferating—turning arrested fetal kidney tissue into the embryonal tumor."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Wilms tumor metastasizes characteristically to the lung: it spreads hematogenously to produce pulmonary nodules, so chest imaging is part of staging—yet even metastatic Wilms is often cured, an unusually favorable pediatric cancer."
  - target: 01-human/07-system/dicer1-syndrome
    relation: connects-to
    note: "Wilms tumor links to several developmental cancer syndromes including DICER1: beyond WT1, predispositions like DICER1 and Beckwith-Wiedemann raise risk, so bilateral or syndromic Wilms prompts genetic evaluation and tailored surveillance."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Wilms tumor ties to the reproductive system through WT1: this gene guides both kidney and gonadal development, so its mutation links Wilms to genitourinary malformations—cryptorchidism, hypospadias, and the ambiguous genitalia of Denys-Drash and WAGR syndromes."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Wilms tumor links to the eye via WAGR syndrome: a chromosome 11p13 deletion removing the adjacent PAX6 gene causes aniridia, so a child born without irises is screened for Wilms—a developmental neighbor on the genome flagging tumor risk."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Beyond the lungs, Wilms tumor spreads to the liver: hematogenous metastasis there marks higher-stage disease, yet even metastatic Wilms is highly curable with chemotherapy, surgery, and radiation—so liver lesions are treated aggressively, not as terminal."
  - target: 01-human/03-molecular/dicer1
    relation: connects-to
    note: "DICER1 mutations cause a Wilms-like spectrum: the DICER1 syndrome predisposes to cystic nephroma and Wilms-type kidney tumors (plus pleuropulmonary blastoma), so a child's nephroblastoma can be a clue to test for this microRNA-processing defect."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Wilms tumor recapitulates kidney development, forming abortive glomeruli: its epithelial component makes primitive glomeruloid structures, and WT1—mutated in Wilms—is essential for normal podocytes, so the same gene builds and, when lost, deranges the glomerulus."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Wilms tumor is classically triphasic, including a fibroblast-like stroma: alongside blastema and epithelium, a spindled stromal component can differentiate toward muscle, cartilage or fibroblasts—reflecting the tumor's origin in pluripotent nephrogenic cells."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Wilms tumor is well-vascularized through VEGF: the tumor and its blastemal cells drive angiogenesis to fuel rapid growth, and anti-VEGF agents have been explored for relapsed or anaplastic disease that resists standard chemotherapy."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Wilms tumor recruits tumor-associated macrophages: these immune cells populate its microenvironment and can support growth and immune escape, making the TME a focus for new approaches in high-risk or relapsed nephroblastoma."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Wilms tumor is studied as a target for NK and immune therapy: as a childhood embryonal tumor it draws interest in harnessing natural killer cells to attack relapsed disease where chemotherapy and radiation reach their limits."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Wilms tumor grows on the IGF-PI3K-AKT axis: high IGF signaling (often from 11p15 imprinting defects) feeds AKT and mTOR to drive the embryonal kidney cancer, so this growth pathway is a target alongside its Wnt and WT1 lesions."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Hypoxia shapes Wilms tumor's behavior: the fast-growing embryonal tumor outpaces its blood supply, and low oxygen drives HIF and angiogenesis that fuel growth and the lung spread that is its main metastatic threat."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells anchor immunotherapy efforts in Wilms tumor: as antigen-presenters they help prime the T-cell and NK response, and dendritic-cell and WT1-vaccine strategies are explored for relapsed embryonal kidney cancer."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Wilms tumor can grow inside the bloodstream: it famously sends a tumor thrombus up the renal vein and inferior vena cava, sometimes reaching the right atrium of the heart, a finding that reshapes the surgical plan."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "The fast-growing Wilms tumor must build its own blood supply: VEGF recruits endothelial cells to sprout new vessels, feeding the embryonal mass and opening the route for its spread to the lungs."
  - target: 01-human/03-molecular/mycn
    relation: connects-to
    note: "MYCN gain marks the dangerous end of Wilms tumor: amplification or extra copies of this oncogene cluster with anaplastic histology and worse outcomes, helping flag the high-risk tumors that need intensified treatment."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows Wilms tumor rebuilding a kidney gone wrong: its triphasic mix of primitive blastema, gland-like epithelial tubules, and stromal cells recapitulates fetal nephron development frozen in malignant form."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "A Wilms mimic heads for the bone: clear cell sarcoma of the kidney, long called the 'bone-metastasizing renal tumor of childhood,' seeds the skeleton and its marrow — spread that classic Wilms tumor, favoring lung and liver, rarely shows."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Some childhood kidney tumors reach the brain: the rhabdoid and clear cell sarcoma variants in the Wilms differential can metastasize to the central nervous system, a site that demands brain imaging when these aggressive types are found."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Wilms tumor often raises the blood pressure: the tumor secretes renin or compresses the renal vessels, and the resulting hypertension is a common presenting sign that settles once the kidney and tumor are removed."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Wilms chemotherapy frays the nerves: vincristine, paired with dactinomycin in the standard regimen, poisons the microtubule transport of peripheral neurons, causing the foot drop, constipation, and tingling that limit its dose."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Wilms tumor can swing the red-cell count either way: bleeding into the tumor drops it toward anemia, while a minority secrete erythropoietin to drive a paraneoplastic polycythemia of excess red cells."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "An antibody confirms the blastema: nuclear WT1 staining on biopsy marks the embryonic kidney cells of a Wilms tumor, helping separate this triphasic nephroblastoma from the other small round blue cell tumors of childhood."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The chemotherapy empties the marrow: adding doxorubicin and, for higher-risk disease, agents like cyclophosphamide and etoposide is myelosuppressive, dropping neutrophil counts so that febrile neutropenia is watched through treatment."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Relapse regimens leak magnesium: the ifosfamide and carboplatin used for high-risk or recurrent Wilms injure the kidney tubule, wasting magnesium and potassium that must be replaced — a special concern when one kidney has already been removed."
  - target: 01-human/03-molecular/renin
    relation: connects-to
    note: "Wilms tumor can hijack blood-pressure control: some secrete renin or compress the renal vasculature, driving a paraneoplastic hypertension that often resolves once the tumor is removed."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "Its chemotherapy can scar the heart: doxorubicin, used for higher-risk Wilms tumor, is cumulatively cardiotoxic to cardiomyocytes, so survivors are followed for a late cardiomyopathy across decades."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "The multi-drug chemotherapy lowers the platelets: the vincristine-actinomycin-doxorubicin regimens suppress platelet production into thrombocytopenia, raising bleeding risk through the months of treatment."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It is the kidney's embryonic gone awry: Wilms tumor (nephroblastoma) arises from persistent metanephric blastema that should have matured into nephrons, a recapitulation of failed kidney development within the renal system."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "The tumor can spike the red count: some Wilms tumors secrete erythropoietin, causing a paraneoplastic polycythemia, while others drive renin and hypertension — the embryonic kidney's hormones turned loose by the cancer."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Curable but watched for immune escape: Wilms tumor is largely chemo-curable, yet its immune microenvironment and cytotoxic T-cell infiltrate are studied for the relapsed, anaplastic cases that resist standard therapy."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "It grows a clot up the great veins: Wilms tumor characteristically extends as a tumor thrombus into the renal vein and inferior vena cava, sometimes reaching the heart — a vascular invasion that must be mapped before surgery."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 supports the blastemal cells: the chemoresistant blastemal component of Wilms tumor shows STAT3 activation that backs its proliferation, a pathway studied in the anaplastic cases that escape standard therapy."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Intensive chemo opens the door to infection: the multidrug regimens that cure most Wilms tumors cause neutropenia, so febrile neutropenia and sepsis are recurrent treatment hazards in these young children."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Losing a kidney leaves the other to compensate: nephrectomy for Wilms tumor, and bilateral or syndromic disease especially, reduces nephron mass, so hyperfiltration injury and chronic kidney disease are long-term survivor concerns."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its anthracycline scars the heart: doxorubicin used in higher-stage Wilms tumor is cardiotoxic, and the cumulative dose can cause a dose-dependent cardiomyopathy and heart failure that may surface years into survivorship."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Tumor and chemo blunt the marrow: an advanced Wilms tumor's inflammatory burden plus myelosuppressive chemotherapy depress erythropoiesis, adding an anemia-of-chronic-disease component to treatment-related cytopenias."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Its chemotherapy opens the lung to mold: the neutropenia from the vincristine-actinomycin-doxorubicin regimens for Wilms tumor lets inhaled Aspergillus invade as pulmonary aspergillosis in these young children."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Childhood radiation and chemo stunt bone accrual: abdominal radiotherapy and cytotoxic treatment for Wilms tumor impair the bone mineral that should build during childhood, leaving reduced bone density in survivors."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A cancer in early childhood weighs on families: the diagnosis in toddlers, major kidney surgery and prolonged treatment impose lasting psychological strain on survivors and their parents."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Nephrectomy is major abdominal surgery in a small child: removing the kidney bearing a Wilms tumour, often after chemotherapy, leaves a large wound prone to slow healing in a young patient."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Vincristine numbs the nerves: the vincristine central to Wilms-tumour chemotherapy is reliably neurotoxic, causing a peripheral neuropathy with weakness, constipation and painful paraesthesiae."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A childhood cancer with long survivorship breeds worry: the major surgery, relapse risk and lifelong late-effect surveillance after Wilms tumour foster chronic anxiety in survivors and their families."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "The lungs are its commonest distant target: Wilms tumour metastasises preferentially to the lungs, so chest imaging stages disease and pulmonary metastases guide intensified chemotherapy and sometimes whole-lung radiation."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It can grow into the great veins and strain the heart: Wilms tumour forms intravascular thrombus extending up the renal vein and IVC to the right atrium, while anthracycline chemotherapy adds long-term cardiotoxicity."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Its overgrowth predisposition shows in the abdomen: Beckwith-Wiedemann syndrome, a leading Wilms risk factor, causes omphalocele, macroglossia and visceromegaly alongside hemihypertrophy."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Nodes guide its staging: regional lymph-node involvement is assessed at nephrectomy and raises the stage, intensifying chemotherapy and radiation."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Its overgrowth syndrome skews the skeleton: the hemihypertrophy of Beckwith-Wiedemann causes limb-length asymmetry, and Wilms tumour can rarely metastasise to bone."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Its gene shapes the gonads: WT1 mutations disrupt gonadal development in Denys-Drash and Frasier syndromes, combining Wilms tumour with genital anomalies and progressive nephropathy."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Therapy suppresses immunity: the chemotherapy for Wilms tumour leaves children immunocompromised, raising opportunistic-infection risk during treatment."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Treatment and syndromes reach the nervous system: vincristine causes peripheral neuropathy, and WAGR syndrome (with Wilms) includes intellectual disability and aniridia."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Treatment marks the skin: chemotherapy causes alopecia and mucositis, and flank radiotherapy produces dermatitis over the treated kidney bed."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "A triumph of chemotherapy: vincristine and actinomycin-D, with doxorubicin for higher stages, combine with surgery and sometimes radiation to cure the great majority of Wilms tumours — a model of how multimodal chemotherapy transformed a paediatric cancer."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "A cold paediatric tumour: unlike the adult clear-cell kidney cancer it neighbours, Wilms tumour has a low mutational burden and responds poorly to PD-1 checkpoint blockade, so immunotherapy has little role in its largely chemo-curable course."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Its bone-seeking mimic: clear cell sarcoma of the kidney, the bone-metastasising renal tumour of childhood and a key differential of Wilms, characteristically spreads to the skeleton — unlike favourable-histology Wilms, which favours lung and liver."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "It spreads to the lungs: Wilms tumour metastasises preferentially to the lungs, so chest imaging stages disease and pulmonary metastases guide intensified chemotherapy and sometimes whole-lung radiation."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "One gene, opposite roles: WT1 is the tumour-suppressor driver of Wilms tumour, yet it is overexpressed in acute myeloid leukaemia, where it serves as a minimal-residual-disease marker and an immunotherapy and vaccine target."
  - target: 01-human/07-system/mesothelioma
    relation: connects-to
    note: "The gene named for a kidney tumour marks a pleural one: WT1, mutated in Wilms tumour, is a defining immunohistochemical marker of mesothelioma (and serous ovarian cancer), distinguishing it from its mimics."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Beyond lung metastasis: Wilms tumour also spreads to the liver, seeding the hepatic lobules; like hepatoblastoma it is an embryonal childhood tumour, both over-represented in Beckwith-Wiedemann overgrowth."
  - target: 01-human/07-system/polycythemia-vera
    relation: connects-to
    note: "A paraneoplastic polycythaemia: some Wilms tumours secrete erythropoietin, raising the red-cell mass and resolving on resection—an acquired, tumour-driven echo of the JAK2-driven erythrocytosis of polycythaemia vera."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Tumour reaches the heart, treatment harms it: Wilms tumour thrombus can extend up the IVC into the right atrium, while the anthracycline chemotherapy that cures it can leave survivors with a late cardiomyopathy of the myocardium."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "A shared diagnostic marker: WT1, the gene behind Wilms tumour, is a key immunohistochemical marker also expressed by serous ovarian carcinoma and mesothelioma, tying an embryonal kidney cancer to adult tumours."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "WT1 in the marrow: WT1 is overexpressed in acute myeloid leukaemia and myelodysplasia, where it serves as a minimal-residual-disease marker—the same gene whose loss drives Wilms tumour acting as an oncogene in myeloid cells."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Wnt/beta-catenin in common: CTNNB1-activating mutations drive a subset of Wilms tumours just as constitutive Wnt/beta-catenin signalling drives colorectal cancer, the same pathway hijacked in very different tissues."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Amplified oncogene: MYC, alongside MYCN, drives the proliferation of Wilms tumour, particularly its undifferentiated blastemal component."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Blastemal epigenetics: EZH2/polycomb activity helps maintain the undifferentiated blastemal cells of Wilms tumour, a candidate epigenetic vulnerability."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Telomere maintenance: TERT activation supports replicative immortality and marks higher-risk, relapse-prone Wilms tumour."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cell-cycle drive: cyclin D1, upregulated downstream of Wnt/β-catenin and IGF signalling, propels Wilms tumour blastemal cells through the G1 checkpoint."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Checkpoint bypass: CDK4/6 activity partnering cyclin D drives the proliferation of Wilms tumour, a candidate cell-cycle therapeutic target."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Tumour hypoxia: HIF-1α stabilised in the hypoxic Wilms tumour drives the VEGF angiogenesis and erythropoietin production that can cause its polycythaemia."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Pulmonary metastasis: CXCR4 on Wilms tumour cells follows CXCL12 gradients toward the lung, the dominant site of metastatic relapse that drives the staging and intensity of Wilms-tumour chemotherapy."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Blastemal stroma: TGF-β drives the mesenchymal-epithelial transitions and stromal differentiation of the triphasic Wilms tumour, shaping the blastemal, stromal and epithelial components that define its histology."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Reactivated nephrogenesis: Notch signalling, essential in normal kidney development, is reactivated in the blastemal cells of Wilms tumour, reflecting its origin as arrested, persistent embryonic nephrogenic tissue."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Chemosensitivity: Wilms tumour is among the most chemocurable solid cancers, and vincristine, actinomycin-D and doxorubicin kill its cells through caspase-3-mediated apoptosis — the basis for the high cure rates achieved with relatively modest therapy."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Tumour-associated macrophages: CCL2 recruits monocytes into the Wilms-tumour microenvironment, where the resulting macrophages support angiogenesis and an immunosuppressive niche around the triphasic blastemal, epithelial and stromal components."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "Nephron-progenitor signalling: FGF signalling that normally sustains self-renewal of the cap-mesenchyme nephron progenitors is co-opted in Wilms-tumour blastema, part of the developmental programme reactivated in this embryonal kidney cancer."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K survival axis: PI3K-AKT-mTOR signalling (AKT and mTOR already mapped) is activated in Wilms tumour and supports the proliferation of its blastemal component, a candidate therapeutic node."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Stromal component: PDGF signalling supports the stromal/mesenchymal element of triphasic Wilms tumour and its angiogenesis, part of the developmental signalling reactivated in this embryonal kidney cancer."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Cell-cycle drive: deregulated RB-E2F1 transcription powers Wilms-tumour proliferation, cooperating with the CDK4/6-cyclin-D machinery already mapped."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Growth-factor MAPK: FGFR and PDGFR signalling (both mapped) drives the MAPK-ERK cascade promoting proliferation of the blastemal component of Wilms tumour."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "IGF-PI3K axis: IGF2-driven (IGF-1 mapped) PI3K-AKT-mTOR signalling (PIK3CA, AKT and mTOR mapped), restrained by PTEN, supports the growth of Wilms tumour."
  - target: 01-human/03-molecular/cdh1
    relation: connects-to
    note: "Developmental MET: Wilms tumour recapitulates nephrogenesis, and E-cadherin marks the mesenchymal-to-epithelial transition that forms its epithelial (tubular) component within the triphasic histology."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Cell-cycle drive: dysregulation of the RB1-E2F checkpoint (CDK4/6, cyclin-D1 and E2F1 already mapped) contributes to the proliferation of the blastemal cells of Wilms tumour."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "RAS proliferation: RAS-ERK signalling (ERK1/2 already mapped) downstream of receptor tyrosine kinases provides a proliferative input in Wilms tumour."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "Anaplastic p53 loss: MDM2-mediated p53 inactivation (p53 already mapped) contributes to the apoptosis evasion of the aggressive anaplastic subtype of Wilms tumour."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING shapes the immune microenvironment of Wilms tumour, relevant to emerging immunotherapy in relapsed paediatric renal cancer."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling governs the antitumour immune response and immune-evasion balance of Wilms tumour."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 supports proliferation and immune evasion in the embryonal blastemal cells of Wilms tumour."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signaling (TGF-β already mapped) shapes the mesenchymal/stromal differentiation and EMT of the triphasic Wilms tumor."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "PI3K-AKT-mediated FOXO inactivation removes a pro-apoptotic brake, favoring survival of Wilms tumor blastemal cells (PI3K-AKT already mapped)."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-delivered cytotoxic killing by CD8 T and NK cells mediates the immune clearance that Wilms tumor must evade."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β regulates β-catenin stability (CTNNB1/Wnt already mapped), a pathway aberrantly activated in Wilms tumor."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory microenvironment of Wilms tumor."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling contributes to the proliferative and invasive signaling of the nephroblastoma blastema of Wilms tumor."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation and imprinting alterations (IGF2/H19) contribute to the epigenetic dysregulation of Wilms tumor."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival of the nephroblast-derived cells of Wilms tumor."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling contributes to the epigenetic dysregulation of Wilms tumor."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of Wilms tumor."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the tumor microenvironment of Wilms tumor."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of Wilms tumor."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of Wilms tumor."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of Wilms tumor."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of Wilms tumor."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Gonadal development: WT1 is essential for forming both kidney and gonad, so WT1 mutations cause Denys-Drash and Frasier syndromes with gonadal dysgenesis and disorders of sex development, disrupting the testosterone-dependent programme alongside the renal tumour."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "WT1 tumour antigen: WT1 is itself a shared tumour antigen targeted by WT1 peptide vaccines and T-cell therapies, so MHC-restricted antigen presentation is central to the immunotherapy directed at Wilms tumour and other WT1-expressing cancers."
  - target: 01-human/03-molecular/growth-hormone
    relation: connects-to
    note: "Overgrowth predisposition: Wilms tumour arises excessively in overgrowth syndromes such as Beckwith-Wiedemann and hemihypertrophy, where the GH-IGF2 axis (IGF already mapped) drives the somatic overgrowth that mandates renal-tumour surveillance."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "WT1 immunotherapy: IL-2-driven T-cell expansion supports the WT1-directed vaccine and adoptive T-cell therapies (MHC class II already mapped) explored for Wilms tumour and other WT1-expressing cancers."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Anthracycline cardiotoxicity: the doxorubicin used for higher-risk Wilms tumour is cardiotoxic, and troponin elevation helps detect the cumulative myocardial injury that threatens these otherwise highly curable children long-term."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Blood-count changes: Wilms tumour can raise haemoglobin through ectopic erythropoietin (already mapped), while its chemotherapy is myelosuppressive and lowers it, giving the disease a variable effect on the blood count."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Renin-driven hypertension: Wilms tumour commonly secretes renin (already mapped), and the resulting angiotensin II raises blood pressure, the paraneoplastic hypertension that is a frequent presenting sign and resolves after nephrectomy."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Tumour lysis: treating a large Wilms tumour lyses the tumour, releasing purines that xanthine oxidase converts to uric acid, a tumour-lysis risk managed with allopurinol and hydration in this chemosensitive childhood cancer."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response (CD8 already mapped), part of the immune evasion of Wilms tumour relevant to the cellular immunotherapy being explored."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune microenvironment of Wilms tumour, this childhood cancer of the kidney."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Chemotherapy anaemia: the vincristine-actinomycin-doxorubicin chemotherapy of Wilms tumour is myelosuppressive, causing anaemia (haemoglobin already mapped) that needs transfusion whose repeated support can load the young child with iron."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Proton radiotherapy: proton-beam radiotherapy can treat higher-stage Wilms tumour while sparing the developing abdominal organs and spine, an option valued in these very young patients."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immune microenvironment of the Wilms tumour."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Intravascular extension: Wilms tumour can grow up the renal vein and inferior vena cava into the right atrium of the heart, a tumour thrombus that complicates surgery and can embolise."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Immune microenvironment: the cytotoxic T cells (perforin already mapped) of the tumour microenvironment are the focus of the immunotherapy explored for the relapsed and anaplastic Wilms tumour that resists chemotherapy."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Metabolic microenvironment: leptin from the marrow and stromal adipose tissue signals within the metabolic microenvironment of the metastatic Wilms tumour."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Marrow-adipose adipokine: adiponectin, with leptin (already mapped), is the marrow-adipose adipokine of the Wilms-tumour microenvironment."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the Wilms-tumour microenvironment."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the immunotherapy of Wilms tumour."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the immune microenvironment of Wilms tumour."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of Wilms tumour."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of Wilms tumour."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the Wilms-tumour microenvironment."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the Wilms-tumour microenvironment."
---

# Wilms Tumor

## Overview

**Wilms tumor (nephroblastoma)** is the most common renal malignancy of childhood and the fourth most common pediatric cancer overall, arising from persistent embryonic metanephric blastema that fails to undergo normal differentiation. Wilms tumor is one of pediatric oncology's greatest success stories — with overall survival exceeding **90%** through decades of cooperative group trials (NWTS/COG in North America; SIOP in Europe) that established risk-adapted chemotherapy regimens [^dome-2015-wilms]. The tri-phasic histology (blastemal, epithelial, stromal components) reflects arrested renal embryogenesis; the genetic landscape is defined by **WT1 mutations** in 10-15%, **CTNNB1 (β-catenin)** in 15-20%, **WTX (AMER1)** in 15-20%, **IGF2 overexpression** in 75% (via 11p15 imprinting loss), and **miRNA processing gene mutations (DROSHA, DGCR8)** in 5-10%. Histological risk stratification — into **favorable histology (FH, ~90%)** and **unfavorable/anaplastic histology (UH, ~10%)** — remains the most powerful prognostic determinant, with TP53 mutations driving anaplastic change and resistance to standard chemotherapy [^dix-2006-arenl0002].

**Epidemiology:**
- Incidence: ~650 cases/year USA; ~9,000 globally/year
- Peak age: 3-4 years; rare after age 8; rare in adults
- ~10% bilateral (synchronous or metachronous); bilateral → higher likelihood of germline predisposition (WAGR, Beckwith-Wiedemann syndrome)
- Sex: slight female predominance; sporadic left-to-right equal; syndrome-associated may differ
- Race: slight higher incidence in African American children; similar outcomes with modern treatment

## Structure

### Molecular and genetic landscape

**Driver pathways:**

**11p15 imprinting (IGF2/H19 locus, ~75%):**
Normal 11p15: Maternal allele (H19 expressed, IGF2 silenced); Paternal allele (H19 silenced, IGF2 expressed). Loss of imprinting (LOI) on maternal allele → biallelic IGF2 expression → IGF2 overproduction → IGF1R-PI3K-AKT-mTOR → proliferation. This is the most common molecular change; associated with Beckwith-Wiedemann syndrome (organomegaly, macroglossia, omphalocele, ~5-10% Wilms risk).

**WT1 pathway (intralobar nephrogenic rests, ~10-15%):**
WT1 loss-of-function → impaired kidney differentiation → persistent intralobar nephrogenic rests (ILNR) → secondary CTNNB1 (WNT pathway) mutations → blastemal-predominant Wilms tumor. WT1+CTNNB1 co-mutation is the canonical "two-hit" model for a subset of Wilms tumor.

**miRNA processing (DROSHA/DGCR8, ~5-10%):**
DROSHA (microprocessor complex subunit) hotspot mutation E1147K; DGCR8 mutations → impaired primary miRNA processing → global mature miRNA reduction → derepression of many oncogenic targets including LIN28 (miRNA suppressor → promotes stem cell state → IGF2/mTOR activation → nephroblastic proliferation). DROSHA E1147K is acquired somatically; associated with blastemal-predominant histology and relapse risk.

**Other recurrent alterations:**
- WTX/AMER1 (X-linked APC-like gene, WNT negative regulator): ~15-20%; truncating mutations → WNT activation; predominantly in boys (hemizygous); independently causes osteopathia striata with cranial sclerosis when germline
- SIX1/SIX2 (homeobox TF, metanephric progenitors): ~5-10%; frameshift hotspot Q177R; associated with epithelial-predominant Wilms tumor; good prognosis
- TP53 mutations: ~70% of anaplastic (unfavorable histology) Wilms tumor; extremely rare in FH Wilms; acquired → signal for impending anaplasia

**Chromosomal changes:**
- 1q gain: most common cytogenetic abnormality (~30%); adverse prognostic factor in FH Wilms tumor
- 16q loss: ~15%; independent adverse factor (NWTS-5)
- 1p loss: ~10%; adverse factor
- 11p15 LOH (paternal UPD/maternal deletion): ~40%; correlates with IGF2 overexpression

### Histological classification

**Favorable histology (FH, ~90%):** Tri-phasic nephroblastoma (blastemal + epithelial + stromal); or predominantly one component without anaplasia; nuclear uniformity; good prognosis with standard treatment.

**Unfavorable histology (UH) / Anaplastic Wilms (~10%):**
- **Diffuse anaplasia (DAWT):** Any anaplastic focus beyond a single foci, or any anaplasia in unfavorable location (extrarenal, invasive); characterized by extreme nuclear enlargement (≥3× adjacent nuclei), hyperchromatic, multipolar mitoses; TP53 mutations ~70%; prognosis poor (Stage IV DAWT 4-year OS ~33%)
- **Focal anaplasia (FAWT):** Single circumscribed anaplastic focus, sharply demarcated; TP53 mutations lower rate; prognosis intermediate between FH and DAWT

**Blastemal-predominant post-chemotherapy (SIOP classification):**
After SIOP neoadjuvant chemotherapy, blastemal cells are treatment-resistant cells; >65% blastemal component post-chemotherapy = "blastemal-type" → high-risk regimen even without anaplasia; analogous to adverse outcome DROSHA-mutant tumors.

## Function

### Normal nephrogenesis and WT1

Kidney development proceeds through three waves of induction: pronephros → mesonephros → metanephros (permanent kidney). Metanephric mesenchyme (MM) expresses WT1, PAX2, SIX2 → receives ureteric bud signals (WNT9B, WNT4) → MM undergoes mesenchymal-to-epithelial transition (MET) → forms nephrons (glomeruli + tubules). WT1 maintains the MM pool while allowing controlled differentiation; WT1 loss → MM fails to differentiate → forms nephrogenic rests → risk of Wilms tumor.

## Pathology

### Predisposition syndromes

**WAGR syndrome (11p13 deletion):**
WT1 + PAX6 deletion; ~30% lifetime Wilms tumor risk; aniridia (PAX6 deletion); genitourinary malformalities; intellectual disability; annual abdominal ultrasound surveillance until age 8-10.

**Denys-Drash syndrome (WT1 ZF3/4 missense, R394W/Q):**
~90% Wilms tumor risk; diffuse mesangial sclerosis → nephrotic syndrome in infancy; male pseudohermaphroditism (46,XY with ambiguous genitalia); diagnosis → bilateral prophylactic nephrectomy recommended by age 2 after gonadal histology clarification.

**Frasier syndrome (WT1 KTS splice mutations):**
+KTS/-KTS ratio disruption → focal segmental glomerulosclerosis → nephrotic syndrome; gonadoblastoma in 46,XY; low Wilms tumor risk (unlike Denys-Drash); managed conservatively.

**Beckwith-Wiedemann syndrome (11p15 imprinting):**
Macroglossia, omphalocele, organomegaly, hemihypertrophy; ~5-10% Wilms tumor (bilateral more common); abdominal ultrasound every 3 months until age 8.

**Isolated hemihypertrophy:** Wilms tumor risk ~5%; screening recommended.

### Staging (COG/NWTS, upfront nephrectomy)

| Stage | Definition | 4-year OS (FH) |
|-------|-----------|----------------|
| I | Confined to kidney, completely resected | ~99% |
| II | Extends beyond kidney, completely resected | ~98% |
| III | Residual tumor (local spillage, positive margins, abdominal nodes, biopsy) | ~95% |
| IV | Hematogenous metastases (lung, liver, bone) | ~85% |
| V | Bilateral | ~80% (depends on salvage) |

**SIOP staging (post-chemotherapy):** Uses similar criteria but applied after neoadjuvant chemotherapy; necrosis/blastemal classification differs from COG upfront system.

### Treatment (COG approach — upfront nephrectomy)

**Standard-risk FH (Stage I-II, no 1q gain or 16q LOH):**
- Radical nephrectomy → actinomycin D + vincristine × 18 weeks (Regimen EE-4A or DD-4A)
- No radiation; 4-year EFS ~95%

**Higher-risk FH (Stage III, bilateral, 1q gain, or Stage IV):**
- Radical nephrectomy (for Stage I-III) → actinomycin D + vincristine + doxorubicin × 24 weeks (Regimen DD-4A/M)
- ± Flank radiation (Stage III local, Stage IV incomplete pulmonary response)
- Stage IV pulmonary metastases: 2 chemotherapy cycles → assess lung response: if complete → omit lung RT; if incomplete → whole-lung RT 12 Gy [^dix-2006-arenl0002]
- 4-year EFS ~87-90%

**Unfavorable histology / Anaplastic Wilms:**
- Focal anaplasia: DD-4A + flank RT (Stage II+)
- Diffuse anaplasia: Regimen UH-1/I (vincristine, actinomycin D, doxorubicin, cyclophosphamide, etoposide, carboplatin) + RT; 4-year EFS ~33% (Stage IV DAWT)
- TP53-mutant DAWT: Very high risk; allo-SCT considered after relapse

**Bilateral Wilms tumor (Stage V):**
- Biopsy first → neoadjuvant chemotherapy × 6 weeks (actinomycin D + vincristine) → reassess bilaterally → nephron-sparing surgery (bilateral partial nephrectomy to preserve renal function) → final staging → further chemotherapy ± RT
- Goal: preserve maximum renal parenchyma; avoid dialysis-dependent chronic kidney disease
- Genetic testing strongly recommended for bilateral cases

**Relapsed Wilms tumor:**
- Prior chemotherapy determines salvage: if previously treated with 2-drug → ICE (ifosfamide, carboplatin, etoposide) or VDC/IE (vincristine+doxorubicin+cyclophosphamide/ifosfamide+etoposide)
- High-dose chemotherapy + autologous SCT for multiply relapsed FH
- Irinotecan+vincristine: active in salvage; ORR ~40-60%
- Everolimus (mTOR), bevacizumab (VEGF): Studied in refractory disease; limited single-agent activity

**SIOP approach (European — neoadjuvant chemotherapy):**
Neoadjuvant actinomycin D + vincristine × 4 weeks (Stage I-III) or + doxorubicin × 6 weeks (Stage IV) → nephrectomy → pathology-based staging + blastemal typing → risk-adapted consolidation; advantage: tumor downstaging (easier surgery, less spillage); disadvantage: loss of upfront pathology staging.

### Long-term effects

Wilms tumor survivors face late effects proportional to treatment intensity:
- **Renal insufficiency:** Single kidney (after radical nephrectomy) → lifetime GFR monitoring; 30-year CKD risk ~15%; bilateral Wilms → higher risk; avoid nephrotoxic drugs
- **Cardiac toxicity:** Doxorubicin → cardiomyopathy; flank RT → cardiac RT if large field; cardiac surveillance echocardiography at 5-year intervals
- **Secondary malignancies:** Abdominal RT → risk of sarcoma, breast cancer (if chest field); doxorubicin → secondary AML (rare)
- **Musculoskeletal:** Flank RT → scoliosis (if field encompasses spine growth plates); asymmetric muscle atrophy
- **Reproductive:** Gonadal irradiation → infertility; oophoropexy before pelvic RT in girls

## Connections

- `connects-to` → **[WT1](../../03-molecular/wt1/README.md)** — WT1 mutations occur in ~10-15% sporadic Wilms tumor and are near-universal in WAGR and Denys-Drash syndromes; WT1+CTNNB1 co-mutation → blastemal-predominant Wilms from intralobar nephrogenic rests; WT1 is required for nephron formation from metanephric blastema.
- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — CTNNB1 activating mutations occur in ~15-20% Wilms tumor, co-occurring with WT1 mutations; nuclear β-catenin marks the blastemal component; WNT activation promotes blastema self-renewal and prevents epithelial differentiation; WNT inhibitors studied preclinically.
- `connects-to` → **[P53](../../03-molecular/p53/README.md)** — TP53 mutations occur in ~70% of diffuse anaplastic Wilms (unfavorable histology); anaplasia is the strongest adverse prognostic factor; TP53 drives resistance to standard chemotherapy; anaplastic WT requires alkylator-based intensification (cyclophosphamide/etoposide).
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — IGF2 overexpression (~75% Wilms tumor via 11p15 imprinting loss) → IGF1R → PI3K-AKT-mTOR → proliferation; everolimus explored in relapsed Wilms; DROSHA/DGCR8 mutations impair miRNA biogenesis → mTOR derepression.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Wilms tumor (nephroblastoma) is the most common childhood kidney cancer, arising at age 3-4 from persistent, undifferentiated metanephric blastema; radical nephrectomy is the backbone, with nephron-sparing surgery reserved for bilateral disease to preserve renal function.
- `connects-to` → **[Podocyte](../../04-cellular/podocyte/README.md)** — WT1 is essential for podocyte function, so the WT1 mutations that cause Wilms tumor also cause glomerular disease: Denys-Drash (missense) brings diffuse mesangial sclerosis and infantile nephrotic syndrome, while Frasier (KTS splice) causes focal segmental glomerulosclerosis.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — The commonest molecular change in Wilms tumor (~75%) is loss of imprinting at 11p15 that doubles IGF2 dosage; excess IGF2 signals through IGF1R to PI3K-AKT-mTOR, driving nephroblast proliferation — the same locus whose disruption underlies Beckwith-Wiedemann overgrowth.
- `connects-to` → **[Rhabdomyosarcoma](../rhabdomyosarcoma/README.md)** — Wilms tumor and rhabdomyosarcoma are both embryonal childhood cancers of arrested development — Wilms from kidney blastema, RMS from myogenic precursors — sharing a key driver: 11p15.5 loss of imprinting doubles IGF2, feeding an IGF1R-PI3K-AKT-mTOR loop in both.
- `connects-to` → **[Neuroblastoma](../neuroblastoma/README.md)** — Wilms tumor and neuroblastoma are the two classic malignant abdominal masses of young children (ages 1-4): Wilms is an intrarenal nephroblastoma rarely crossing midline; neuroblastoma is an adrenal/sympathetic tumor that secretes catecholamines and often crosses.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Anaplastic (unfavorable-histology) Wilms tumor is defined by TP53 mutation, driving chemoresistance and worse prognosis; germline TP53 (Li-Fraumeni) is occasionally found with anaplasia or family history — linking Wilms to the p53-driven childhood cancer-predisposition spectrum.
- `connects-to` → **[Renal Cell Carcinoma](../renal-cell-carcinoma/README.md)** — Wilms tumor and renal cell carcinoma are the kidney cancers of childhood versus adulthood: Wilms (nephroblastoma) is an embryonal tumor of nephron precursors curable with surgery and chemo, while RCC arises from mature tubular epithelium in adults, driven by VHL/HIF.
- `connects-to` → **[Ewing Sarcoma](../ewing-sarcoma/README.md)** — Wilms tumor's blastemal component enters the small-round-blue-cell differential with Ewing sarcoma: both are pediatric tumors of primitive cells, but Wilms is triphasic (blastema/epithelium/stroma) with WT1 changes while Ewing is EWSR1-FLI1-driven.
- `connects-to` → **[Retinoblastoma](../retinoblastoma/README.md)** — Wilms tumor and retinoblastoma are paradigm embryonal childhood cancers fitting Knudson's two-hit model: bilateral Wilms (often WT1-linked) parallels heritable bilateral retinoblastoma—germline loss of one suppressor allele plus a somatic second hit drives early tumors.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy is part of risk-adapted Wilms tumor cure: flank or whole-abdomen photon radiation is added for higher-stage or unfavorable-histology disease after nephrectomy and chemotherapy, contributing to Wilms' high cure rate.
- `connects-to` → **[Atypical Teratoid/Rhabdoid Tumor](../atypical-teratoid-rhabdoid-tumor/README.md)** — Wilms tumor and rhabdoid tumors are distinct pediatric renal/CNS cancers: classic Wilms is a WT1-related nephroblastoma with good prognosis, while malignant rhabdoid tumor of the kidney (and CNS ATRT) is a SMARCB1-deficient, far more aggressive tumor.
- `connects-to` → **[Medulloblastoma](../medulloblastoma/README.md)** — Wilms tumor and medulloblastoma are both embryonal childhood tumors arising from developmental precursors: Wilms from metanephric blastema (WT1/Wnt), medulloblastoma from cerebellar progenitors—different organs, but both recapitulate arrested embryonic development.
- `connects-to` → **[CTNNB1](../../03-molecular/ctnnb1/README.md)** — Wilms tumor is partly a Wnt-driven cancer: beta-catenin (CTNNB1) activating mutations, often with WT1 loss, derail the kidney's developmental Wnt signaling so nephron precursors keep proliferating—turning arrested fetal kidney tissue into the embryonal tumor.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Wilms tumor metastasizes characteristically to the lung: it spreads hematogenously to produce pulmonary nodules, so chest imaging is part of staging—yet even metastatic Wilms is often cured, an unusually favorable pediatric cancer.
- `connects-to` → **[DICER1 Syndrome](../dicer1-syndrome/README.md)** — Wilms tumor links to several developmental cancer syndromes including DICER1: beyond WT1, predispositions like DICER1 and Beckwith-Wiedemann raise risk, so bilateral or syndromic Wilms prompts genetic evaluation and tailored surveillance.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Wilms tumor ties to the reproductive system through WT1: this gene guides both kidney and gonadal development, so its mutation links Wilms to genitourinary malformations—cryptorchidism, hypospadias, and the ambiguous genitalia of Denys-Drash and WAGR syndromes.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Wilms tumor links to the eye via WAGR syndrome: a chromosome 11p13 deletion removing the adjacent PAX6 gene causes aniridia, so a child born without irises is screened for Wilms—a developmental neighbor on the genome flagging tumor risk.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Beyond the lungs, Wilms tumor spreads to the liver: hematogenous metastasis there marks higher-stage disease, yet even metastatic Wilms is highly curable with chemotherapy, surgery, and radiation—so liver lesions are treated aggressively, not as terminal.
- `connects-to` → **[DICER1](../../03-molecular/dicer1/README.md)** — DICER1 mutations cause a Wilms-like spectrum: the DICER1 syndrome predisposes to cystic nephroma and Wilms-type kidney tumors (plus pleuropulmonary blastoma), so a child's nephroblastoma can be a clue to test for this microRNA-processing defect.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Wilms tumor recapitulates kidney development, forming abortive glomeruli: its epithelial component makes primitive glomeruloid structures, and WT1—mutated in Wilms—is essential for normal podocytes, so the same gene builds and, when lost, deranges the glomerulus.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Wilms tumor is classically triphasic, including a fibroblast-like stroma: alongside blastema and epithelium, a spindled stromal component can differentiate toward muscle, cartilage or fibroblasts—reflecting the tumor's origin in pluripotent nephrogenic cells.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Wilms tumor is well-vascularized through VEGF: the tumor and its blastemal cells drive angiogenesis to fuel rapid growth, and anti-VEGF agents have been explored for relapsed or anaplastic disease that resists standard chemotherapy.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Wilms tumor recruits tumor-associated macrophages: these immune cells populate its microenvironment and can support growth and immune escape, making the TME a focus for new approaches in high-risk or relapsed nephroblastoma.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Wilms tumor is studied as a target for NK and immune therapy: as a childhood embryonal tumor it draws interest in harnessing natural killer cells to attack relapsed disease where chemotherapy and radiation reach their limits.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Wilms tumor grows on the IGF-PI3K-AKT axis: high IGF signaling (often from 11p15 imprinting defects) feeds AKT and mTOR to drive the embryonal kidney cancer, so this growth pathway is a target alongside its Wnt and WT1 lesions.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Hypoxia shapes Wilms tumor's behavior: the fast-growing embryonal tumor outpaces its blood supply, and low oxygen drives HIF and angiogenesis that fuel growth and the lung spread that is its main metastatic threat.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells anchor immunotherapy efforts in Wilms tumor: as antigen-presenters they help prime the T-cell and NK response, and dendritic-cell and WT1-vaccine strategies are explored for relapsed embryonal kidney cancer.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Wilms tumor can grow inside the bloodstream: it famously sends a tumor thrombus up the renal vein and inferior vena cava, sometimes reaching the right atrium of the heart, a finding that reshapes the surgical plan.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — The fast-growing Wilms tumor must build its own blood supply: VEGF recruits endothelial cells to sprout new vessels, feeding the embryonal mass and opening the route for its spread to the lungs.
- `connects-to` → **[MYCN](../../03-molecular/mycn/README.md)** — MYCN gain marks the dangerous end of Wilms tumor: amplification or extra copies of this oncogene cluster with anaplastic histology and worse outcomes, helping flag the high-risk tumors that need intensified treatment.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows Wilms tumor rebuilding a kidney gone wrong: its triphasic mix of primitive blastema, gland-like epithelial tubules, and stromal cells recapitulates fetal nephron development frozen in malignant form.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — A Wilms mimic heads for the bone: clear cell sarcoma of the kidney, long called the 'bone-metastasizing renal tumor of childhood,' seeds the skeleton and its marrow — spread that classic Wilms tumor, favoring lung and liver, rarely shows.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Some childhood kidney tumors reach the brain: the rhabdoid and clear cell sarcoma variants in the Wilms differential can metastasize to the central nervous system, a site that demands brain imaging when these aggressive types are found.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Wilms tumor often raises the blood pressure: the tumor secretes renin or compresses the renal vessels, and the resulting hypertension is a common presenting sign that settles once the kidney and tumor are removed.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Wilms chemotherapy frays the nerves: vincristine, paired with dactinomycin in the standard regimen, poisons the microtubule transport of peripheral neurons, causing the foot drop, constipation, and tingling that limit its dose.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Wilms tumor can swing the red-cell count either way: bleeding into the tumor drops it toward anemia, while a minority secrete erythropoietin to drive a paraneoplastic polycythemia of excess red cells.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — An antibody confirms the blastema: nuclear WT1 staining on biopsy marks the embryonic kidney cells of a Wilms tumor, helping separate this triphasic nephroblastoma from the other small round blue cell tumors of childhood.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The chemotherapy empties the marrow: adding doxorubicin and, for higher-risk disease, agents like cyclophosphamide and etoposide is myelosuppressive, dropping neutrophil counts so that febrile neutropenia is watched through treatment.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Relapse regimens leak magnesium: the ifosfamide and carboplatin used for high-risk or recurrent Wilms injure the kidney tubule, wasting magnesium and potassium that must be replaced — a special concern when one kidney has already been removed.
- `connects-to` → **[Renin](../../03-molecular/renin/README.md)** — Wilms tumor can hijack blood-pressure control: some secrete renin or compress the renal vasculature, driving a paraneoplastic hypertension that often resolves once the tumor is removed.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — Its chemotherapy can scar the heart: doxorubicin, used for higher-risk Wilms tumor, is cumulatively cardiotoxic to cardiomyocytes, so survivors are followed for a late cardiomyopathy across decades.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — The multi-drug chemotherapy lowers the platelets: the vincristine-actinomycin-doxorubicin regimens suppress platelet production into thrombocytopenia, raising bleeding risk through the months of treatment.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It is the kidney's embryonic gone awry: Wilms tumor (nephroblastoma) arises from persistent metanephric blastema that should have matured into nephrons, a recapitulation of failed kidney development within the renal system.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — The tumor can spike the red count: some Wilms tumors secrete erythropoietin, causing a paraneoplastic polycythemia, while others drive renin and hypertension — the embryonic kidney's hormones turned loose by the cancer.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Curable but watched for immune escape: Wilms tumor is largely chemo-curable, yet its immune microenvironment and cytotoxic T-cell infiltrate are studied for the relapsed, anaplastic cases that resist standard therapy.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — It grows a clot up the great veins: Wilms tumor characteristically extends as a tumor thrombus into the renal vein and inferior vena cava, sometimes reaching the heart — a vascular invasion that must be mapped before surgery.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 supports the blastemal cells: the chemoresistant blastemal component of Wilms tumor shows STAT3 activation that backs its proliferation, a pathway studied in the anaplastic cases that escape standard therapy.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Intensive chemo opens the door to infection: the multidrug regimens that cure most Wilms tumors cause neutropenia, so febrile neutropenia and sepsis are recurrent treatment hazards in these young children.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Losing a kidney leaves the other to compensate: nephrectomy for Wilms tumor, and bilateral or syndromic disease especially, reduces nephron mass, so hyperfiltration injury and chronic kidney disease are long-term survivor concerns.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its anthracycline scars the heart: doxorubicin used in higher-stage Wilms tumor is cardiotoxic, and the cumulative dose can cause a dose-dependent cardiomyopathy and heart failure that may surface years into survivorship.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Tumor and chemo blunt the marrow: an advanced Wilms tumor's inflammatory burden plus myelosuppressive chemotherapy depress erythropoiesis, adding an anemia-of-chronic-disease component to treatment-related cytopenias.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Its chemotherapy opens the lung to mold: the neutropenia from the vincristine-actinomycin-doxorubicin regimens for Wilms tumor lets inhaled Aspergillus invade as pulmonary aspergillosis in these young children.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Childhood radiation and chemo stunt bone accrual: abdominal radiotherapy and cytotoxic treatment for Wilms tumor impair the bone mineral that should build during childhood, leaving reduced bone density in survivors.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A cancer in early childhood weighs on families: the diagnosis in toddlers, major kidney surgery and prolonged treatment impose lasting psychological strain on survivors and their parents.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Nephrectomy is major abdominal surgery in a small child: removing the kidney bearing a Wilms tumour, often after chemotherapy, leaves a large wound prone to slow healing in a young patient.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Vincristine numbs the nerves: the vincristine central to Wilms-tumour chemotherapy is reliably neurotoxic, causing a peripheral neuropathy with weakness, constipation and painful paraesthesiae.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A childhood cancer with long survivorship breeds worry: the major surgery, relapse risk and lifelong late-effect surveillance after Wilms tumour foster chronic anxiety in survivors and their families.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — The lungs are its commonest distant target: Wilms tumour metastasises preferentially to the lungs, so chest imaging stages disease and pulmonary metastases guide intensified chemotherapy and sometimes whole-lung radiation.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It can grow into the great veins and strain the heart: Wilms tumour forms intravascular thrombus extending up the renal vein and IVC to the right atrium, while anthracycline chemotherapy adds long-term cardiotoxicity.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Its overgrowth predisposition shows in the abdomen: Beckwith-Wiedemann syndrome, a leading Wilms risk factor, causes omphalocele, macroglossia and visceromegaly alongside hemihypertrophy.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Nodes guide its staging: regional lymph-node involvement is assessed at nephrectomy and raises the stage, intensifying chemotherapy and radiation.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Its overgrowth syndrome skews the skeleton: the hemihypertrophy of Beckwith-Wiedemann causes limb-length asymmetry, and Wilms tumour can rarely metastasise to bone.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Its gene shapes the gonads: WT1 mutations disrupt gonadal development in Denys-Drash and Frasier syndromes, combining Wilms tumour with genital anomalies and progressive nephropathy.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Therapy suppresses immunity: the chemotherapy for Wilms tumour leaves children immunocompromised, raising opportunistic-infection risk during treatment.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Treatment and syndromes reach the nervous system: vincristine causes peripheral neuropathy, and WAGR syndrome (with Wilms) includes intellectual disability and aniridia.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Treatment marks the skin: chemotherapy causes alopecia and mucositis, and flank radiotherapy produces dermatitis over the treated kidney bed.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — A triumph of chemotherapy: vincristine and actinomycin-D, with doxorubicin for higher stages, combine with surgery and sometimes radiation to cure the great majority of Wilms tumours — a model of how multimodal chemotherapy transformed a paediatric cancer.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — A cold paediatric tumour: unlike the adult clear-cell kidney cancer it neighbours, Wilms tumour has a low mutational burden and responds poorly to PD-1 checkpoint blockade, so immunotherapy has little role in its largely chemo-curable course.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Its bone-seeking mimic: clear cell sarcoma of the kidney, the bone-metastasising renal tumour of childhood and a key differential of Wilms, characteristically spreads to the skeleton — unlike favourable-histology Wilms, which favours lung and liver.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — It spreads to the lungs: Wilms tumour metastasises preferentially to the lungs, so chest imaging stages disease and pulmonary metastases guide intensified chemotherapy and sometimes whole-lung radiation.
- `connects-to` → **[AML](../aml/README.md)** — One gene, opposite roles: WT1 is the tumour-suppressor driver of Wilms tumour, yet it is overexpressed in acute myeloid leukaemia, where it serves as a minimal-residual-disease marker and an immunotherapy and vaccine target.
- `connects-to` → **[Mesothelioma](../mesothelioma/README.md)** — The gene named for a kidney tumour marks a pleural one: WT1, mutated in Wilms tumour, is a defining immunohistochemical marker of mesothelioma (and serous ovarian cancer), distinguishing it from its mimics.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Beyond lung metastasis: Wilms tumour also spreads to the liver, seeding the hepatic lobules; like hepatoblastoma it is an embryonal childhood tumour, both over-represented in Beckwith-Wiedemann overgrowth.
- `connects-to` → **[Polycythemia Vera](../polycythemia-vera/README.md)** — A paraneoplastic polycythaemia: some Wilms tumours secrete erythropoietin, raising the red-cell mass and resolving on resection—an acquired, tumour-driven echo of the JAK2-driven erythrocytosis of polycythaemia vera.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Tumour reaches the heart, treatment harms it: Wilms tumour thrombus can extend up the IVC into the right atrium, while the anthracycline chemotherapy that cures it can leave survivors with a late cardiomyopathy of the myocardium.
- `connects-to` → **[Ovarian Cancer](../ovarian-cancer/README.md)** — A shared diagnostic marker: WT1, the gene behind Wilms tumour, is a key immunohistochemical marker also expressed by serous ovarian carcinoma and mesothelioma, tying an embryonal kidney cancer to adult tumours.
- `connects-to` → **[MDS](../mds/README.md)** — WT1 in the marrow: WT1 is overexpressed in acute myeloid leukaemia and myelodysplasia, where it serves as a minimal-residual-disease marker—the same gene whose loss drives Wilms tumour acting as an oncogene in myeloid cells.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — Wnt/beta-catenin in common: CTNNB1-activating mutations drive a subset of Wilms tumours just as constitutive Wnt/beta-catenin signalling drives colorectal cancer, the same pathway hijacked in very different tissues.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Amplified oncogene: MYC, alongside MYCN, drives the proliferation of Wilms tumour, particularly its undifferentiated blastemal component.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Blastemal epigenetics: EZH2/polycomb activity helps maintain the undifferentiated blastemal cells of Wilms tumour, a candidate epigenetic vulnerability.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Telomere maintenance: TERT activation supports replicative immortality and marks higher-risk, relapse-prone Wilms tumour.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cell-cycle drive: cyclin D1, upregulated downstream of Wnt/β-catenin and IGF signalling, propels Wilms tumour blastemal cells through the G1 checkpoint.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Checkpoint bypass: CDK4/6 activity partnering cyclin D drives the proliferation of Wilms tumour, a candidate cell-cycle therapeutic target.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Tumour hypoxia: HIF-1α stabilised in the hypoxic Wilms tumour drives the VEGF angiogenesis and erythropoietin production that can cause its polycythaemia.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCR4 on Wilms tumor cells follows CXCL12 gradients toward the lung, the dominant site of metastatic relapse that drives the staging and the intensity of the chemotherapy used in this otherwise highly curable childhood cancer.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — TGF-β drives the mesenchymal-epithelial transitions and stromal differentiation of the triphasic Wilms tumor, shaping the blastemal, stromal, and epithelial components whose proportions define its histology and prognosis.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — Notch signaling, essential in normal kidney development, is reactivated in the blastemal cells of Wilms tumor—reflecting its origin as arrested, persistent embryonic nephrogenic tissue (nephrogenic rests) that failed to mature.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Wilms tumor is among the most chemocurable solid cancers, and vincristine, actinomycin-D and doxorubicin kill its cells through caspase-3-mediated apoptosis—the basis for the high cure rates achieved with relatively modest therapy.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 recruits monocytes into the Wilms-tumor microenvironment, where the resulting macrophages support angiogenesis and an immunosuppressive niche around the triphasic blastemal, epithelial and stromal components.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — FGF signaling that normally sustains self-renewal of the cap-mesenchyme nephron progenitors is co-opted in Wilms-tumor blastema, part of the developmental program reactivated in this embryonal kidney cancer.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K-AKT-mTOR signaling (AKT and mTOR already mapped) is activated in Wilms tumor and supports the proliferation of its blastemal component, a candidate therapeutic node.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — PDGF signaling supports the stromal/mesenchymal element of triphasic Wilms tumor and its angiogenesis, part of the developmental signaling reactivated in this embryonal kidney cancer.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — Deregulated RB-E2F1 transcription powers Wilms-tumor proliferation, cooperating with the CDK4/6-cyclin-D machinery already mapped.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — FGFR and PDGFR signaling (both mapped) drives the MAPK-ERK cascade promoting proliferation of the blastemal component of Wilms tumor.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — IGF2-driven (IGF-1 mapped) PI3K-AKT-mTOR signaling (PIK3CA, AKT and mTOR mapped), restrained by PTEN, supports the growth of Wilms tumor.
- `connects-to` → **[CDH1](../../03-molecular/cdh1/README.md)** — Wilms tumor recapitulates nephrogenesis, and E-cadherin marks the mesenchymal-to-epithelial transition that forms its epithelial (tubular) component within the triphasic histology.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — Dysregulation of the RB1-E2F checkpoint (CDK4/6, cyclin-D1 and E2F1 already mapped) contributes to the proliferation of the blastemal cells of Wilms tumor.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — RAS-ERK signaling (ERK1/2 already mapped) downstream of receptor tyrosine kinases provides a proliferative input in Wilms tumor.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 inactivation (p53 already mapped) contributes to the apoptosis evasion of the aggressive anaplastic subtype of Wilms tumor.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING shapes the immune microenvironment of Wilms tumor, relevant to emerging immunotherapy in relapsed pediatric renal cancer.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling governs the antitumor immune response and immune-evasion balance of Wilms tumor.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 supports proliferation and immune evasion in the embryonal blastemal cells of Wilms tumor.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β already mapped) shapes the mesenchymal/stromal differentiation and EMT of the triphasic Wilms tumor.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — PI3K-AKT-mediated FOXO inactivation removes a pro-apoptotic brake, favoring survival of Wilms tumor blastemal cells (PI3K-AKT already mapped).
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-delivered cytotoxic killing by CD8 T and NK cells mediates the immune clearance that Wilms tumor must evade.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β regulates β-catenin stability (CTNNB1/Wnt already mapped), a pathway aberrantly activated in Wilms tumor.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory microenvironment of Wilms tumor.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling contributes to the proliferative and invasive signaling of the nephroblastoma blastema of Wilms tumor.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation and imprinting alterations (IGF2/H19) contribute to the epigenetic dysregulation of Wilms tumor.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival of the nephroblast-derived cells of Wilms tumor.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling contributes to the epigenetic dysregulation of Wilms tumor.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of Wilms tumor.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the tumor microenvironment of Wilms tumor.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of Wilms tumor.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of Wilms tumor.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of Wilms tumor.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of Wilms tumor.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Gonadal development: WT1 is essential for forming both kidney and gonad, so WT1 mutations cause Denys-Drash and Frasier syndromes with gonadal dysgenesis and disorders of sex development, disrupting the testosterone-dependent programme alongside the renal tumour.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — WT1 tumour antigen: WT1 is itself a shared tumour antigen targeted by WT1 peptide vaccines and T-cell therapies, so MHC-restricted antigen presentation is central to the immunotherapy directed at Wilms tumour and other WT1-expressing cancers.
- `connects-to` → **[Growth hormone](../../03-molecular/growth-hormone/README.md)** — Overgrowth predisposition: Wilms tumour arises excessively in overgrowth syndromes such as Beckwith-Wiedemann and hemihypertrophy, where the GH-IGF2 axis (IGF already mapped) drives the somatic overgrowth that mandates renal-tumour surveillance.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — WT1 immunotherapy: IL-2-driven T-cell expansion supports the WT1-directed vaccine and adoptive T-cell therapies (MHC class II already mapped) explored for Wilms tumour and other WT1-expressing cancers.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Anthracycline cardiotoxicity: the doxorubicin used for higher-risk Wilms tumour is cardiotoxic, and troponin elevation helps detect the cumulative myocardial injury that threatens these otherwise highly curable children long-term.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Blood-count changes: Wilms tumour can raise haemoglobin through ectopic erythropoietin (already mapped), while its chemotherapy is myelosuppressive and lowers it, giving the disease a variable effect on the blood count.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — Renin-driven hypertension: Wilms tumour commonly secretes renin (already mapped), and the resulting angiotensin II raises blood pressure, the paraneoplastic hypertension that is a frequent presenting sign and resolves after nephrectomy.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Tumour lysis: treating a large Wilms tumour lyses the tumour, releasing purines that xanthine oxidase converts to uric acid, a tumour-lysis risk managed with allopurinol and hydration in this chemosensitive childhood cancer.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response (CD8 already mapped), part of the immune evasion of Wilms tumour relevant to the cellular immunotherapy being explored.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune microenvironment of Wilms tumour, this childhood cancer of the kidney.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Chemotherapy anaemia: the vincristine-actinomycin-doxorubicin chemotherapy of Wilms tumour is myelosuppressive, causing anaemia (haemoglobin already mapped) that needs transfusion whose repeated support can load the young child with iron.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Proton radiotherapy: proton-beam radiotherapy can treat higher-stage Wilms tumour while sparing the developing abdominal organs and spine, an option valued in these very young patients.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immune microenvironment of the Wilms tumour.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Intravascular extension: Wilms tumour can grow up the renal vein and inferior vena cava into the right atrium of the heart, a tumour thrombus that complicates surgery and can embolise.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Immune microenvironment: the cytotoxic T cells (perforin already mapped) of the tumour microenvironment are the focus of the immunotherapy explored for the relapsed and anaplastic Wilms tumour that resists chemotherapy.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Metabolic microenvironment: leptin from the marrow and stromal adipose tissue signals within the metabolic microenvironment of the metastatic Wilms tumour.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Marrow-adipose adipokine: adiponectin, with leptin (already mapped), is the marrow-adipose adipokine of the Wilms-tumour microenvironment.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the Wilms-tumour microenvironment.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the immunotherapy of Wilms tumour.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the immune microenvironment of Wilms tumour.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of Wilms tumour.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of Wilms tumour.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the Wilms-tumour microenvironment.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the Wilms-tumour microenvironment.

[^dome-2015-wilms]: Dome JS, Graf N, Geller JI, et al. Advances in Wilms tumor treatment and biology: progress through international collaboration. *J Clin Oncol.* 2015;33(27):2999-3007. [doi:10.1200/JCO.2015.62.1888](https://doi.org/10.1200/JCO.2015.62.1888) · [PubMed 26261251](https://pubmed.ncbi.nlm.nih.gov/26261251/)
[^dix-2006-arenl0002]: Dix DB, Bhatt SM, Geller JI, et al. Treatment of Stage IV favorable histology Wilms tumor with incomplete lung metastasis response after chemotherapy: a report from Children's Oncology Group Study AREN0533. *J Clin Oncol.* 2018;36(16):1564-1570. [doi:10.1200/JCO.2017.77.1877](https://doi.org/10.1200/JCO.2017.77.1877) · [PubMed 29584550](https://pubmed.ncbi.nlm.nih.gov/29584550/)

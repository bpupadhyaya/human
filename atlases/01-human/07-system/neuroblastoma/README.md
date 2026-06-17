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

[^yu-2010-dinutuximab-nb]: Yu AL, Gilman AL, Ozkaynak MF, et al. Anti-GD2 antibody with GM-CSF, interleukin-2, and isotretinoin for neuroblastoma. *N Engl J Med.* 2010;363(14):1324-1334. [doi:10.1056/NEJMoa0911123](https://doi.org/10.1056/NEJMoa0911123) · [PubMed 20879881](https://pubmed.ncbi.nlm.nih.gov/20879881/)
[^park-2019-tandem-sct-nb]: Park JR, Kreissman SG, London WB, et al. Effect of tandem autologous stem cell transplant vs single transplant on event-free survival in patients with high-risk neuroblastoma: a randomized clinical trial. *JAMA.* 2019;322(8):746-755. [doi:10.1001/jama.2019.11642](https://doi.org/10.1001/jama.2019.11642) · [PubMed 31454023](https://pubmed.ncbi.nlm.nih.gov/31454023/)

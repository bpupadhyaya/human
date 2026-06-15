---
schema: human-scale-entry/v1
id: peutz-jeghers-syndrome
name: Peutz-Jeghers Syndrome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Peutz-Jeghers syndrome (PJS) is caused by germline STK11/LKB1 mutations; hamartomatous GI polyps + mucocutaneous melanotic spots; cumulative cancer risk by age 70: breast 45%, CRC 39%, pancreatic 36%; intussusception risk; surveillance from age 8."
aliases: ["Peutz-Jeghers syndrome", "PJS", "STK11 hamartoma", "LKB1 polyp syndrome", "Peutz-Jeghers", "hereditary hamartomatous polyposis", "PJ polyp", "STK11 cancer syndrome", "hamartomatous polyposis", "Peutz-Jeghers cancer risk"]
sources:
  - id: hearle-2006-pjs-cancer
    type: peer-reviewed
    cite: "Hearle N, Schumacher V, Menko FH, et al. Frequency and spectrum of cancers in the Peutz-Jeghers syndrome. Clin Cancer Res. 2006;12(10):3209-3215."
    doi: "10.1158/1078-0432.CCR-06-0083"
    pmid: "16707622"
    url: "https://doi.org/10.1158/1078-0432.CCR-06-0083"
  - id: skoulidis-2018-stk11-nsclc
    type: peer-reviewed
    cite: "Skoulidis F, Goldberg ME, Greenawalt DM, et al. STK11/LKB1 mutations and PD-1 inhibitor resistance in KRAS-mutant lung adenocarcinoma. Cancer Cell. 2018;34(3):412-424."
    doi: "10.1016/j.ccell.2018.08.013"
    pmid: "30174241"
    url: "https://doi.org/10.1016/j.ccell.2018.08.013"
cross_links:
  - target: 01-human/03-molecular/stk11
    relation: connects-to
    note: "Germline STK11 mutations cause ~94% of PJS; STK11 encodes LKB1 (AMPK activator); haploinsufficiency → polyp formation (second hit in polyp epithelium); truncating STK11 mutations associate with higher cancer risk than missense; STK11 germline panel + deletion analysis required"
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "STK11 LOF → AMPK inactivation → mTOR unrestrained → hamartoma growth in PJS; rapamycin reduces polyp burden in STK11+/− mouse models; mTORC1 is the primary growth driver in PJS hamartomas; AMPK activators (metformin) explored as chemoprevention in PJS pilot studies"
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "PJS lifetime CRC risk ~39% by age 70 (Hearle 2006); PJS CRC arises through hamartoma-adenoma-carcinoma sequence; proximal colon predominance; colonoscopy with polypectomy every 1-3 years from age 15-20; CRC is the third most common PJS cancer after breast and pancreatic"
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "PJS lifetime pancreatic cancer risk ~36% by age 70; EUS + MRI surveillance from age 30-35; STK11 LOF co-mutation with KRAS in pancreatic cancer → mTOR + MAPK dual activation; PJS pancreatic cancer prognosis poor; resectability rate ~40% at detection"
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "STK11 LOF → AMPK loss → mTORC1 unrestrained → S6K1/4EBP1 → epithelial and smooth muscle proliferation → PJ hamartoma formation; rapamycin reduces polyp burden ~50-80% in STK11+/− mice; sirolimus + metformin pilot trial ongoing in PJS patients (NCT03943992)."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "PJS breast cancer lifetime risk ~45-54% by age 70 (BRCA1/2-equivalent); breast MRI + mammogram from age 25; STK11 LOF → mTOR hyperactivation in breast epithelium; HR+ predominant; no PJS-specific breast cancer histology; risk-reducing bilateral mastectomy discussed."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "STK11/LKB1 somatic mutations in ~15-20% of KRAS-mutant lung adenocarcinoma; STK11 loss → PD-L1 downregulation + CXCL7 secretion → neutrophilic immunosuppressive TME → primary ICB resistance; STK11-mutant KRAS+ NSCLC is the poorest immunotherapy responder subgroup."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "The small intestine is the danger zone of Peutz-Jeghers syndrome: large hamartomatous polyps in the jejunum and ileum become lead points for intussusception — the most common complication, often needing emergency surgery in childhood; surveillance and polypectomy prevent it."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "The diagnostic clue to Peutz-Jeghers syndrome is on the skin and lips: mucocutaneous melanotic macules — dark freckle-like spots on the lips, buccal mucosa, and fingertips — appear in infancy and often fade with age, but with hamartomatous polyps they establish the diagnosis."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Peutz-Jeghers hamartomas have a unique histology: an arborizing (tree-like) core of bundled smooth muscle extending into the polyp, covered by normal epithelium — distinguishing them from the edematous juvenile polyps of JPS or the dysplastic adenomas of FAP."
  - target: 01-human/07-system/juvenile-polyposis-syndrome
    relation: connects-to
    note: "Peutz-Jeghers and juvenile polyposis are the two main hamartomatous polyposis syndromes: PJS (STK11) produces arborizing smooth-muscle polyps and mucocutaneous pigmentation, while JPS (SMAD4/BMPR1A) produces juvenile polyps—both raise GI cancer risk."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "Peutz-Jeghers syndrome predisposes to distinctive ovarian tumors: sex cord tumors with annular tubules (SCTAT) and mucinous tumors arise from STK11 loss, often causing precocious puberty or estrogen effects—part of the syndrome's broad, organ-spanning cancer risk."
  - target: 01-human/07-system/cervical-cancer
    relation: connects-to
    note: "Peutz-Jeghers syndrome carries a rare cervical cancer—adenoma malignum (minimal-deviation adenocarcinoma): this deceptively bland, HPV-independent tumor is strongly associated with STK11 loss, so PJS patients warrant gynecologic surveillance for it."
  - target: 01-human/07-system/cowden-syndrome
    relation: connects-to
    note: "Peutz-Jeghers and Cowden are both hamartomatous polyposis syndromes with different genes: PJS from STK11 loss giving GI hamartomas and mucocutaneous pigmentation, Cowden from PTEN (PI3K-AKT) loss—both fill the gut with hamartomas and raise multi-organ cancer risk."
  - target: 01-human/07-system/fap
    relation: connects-to
    note: "Peutz-Jeghers and FAP are inherited polyposis syndromes with opposite polyp types: PJS produces hamartomatous polyps from STK11 loss, while FAP produces hundreds of adenomatous polyps from APC loss with near-certain colorectal cancer—hamartoma versus adenoma."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "Peutz-Jeghers raises gastric as well as colorectal cancer risk: STK11 loss seeds hamartomatous polyps throughout the stomach and small bowel that can bleed, obstruct or harbor dysplasia, so upper-GI surveillance accompanies colonoscopy in PJS patients from childhood."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Peutz-Jeghers polyps stud the large intestine and beyond: STK11 loss produces hamartomatous polyps throughout the GI tract—small bowel most, but also colon—that bleed, cause intussusception, and modestly raise colorectal cancer risk."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "PJS hamartomas arise in disordered intestinal epithelium: loss of the STK11/LKB1 kinase deranges epithelial polarity and growth, so the crypts overgrow into the branching, smooth-muscle-cored hamartomatous polyps that distinguish PJS from adenomatous polyposis."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "PJS shows a non-Wnt route to GI tumors: unlike FAP's APC/Wnt adenomas, Peutz-Jeghers polyps arise from STK11/LKB1-AMPK-mTOR dysregulation, so its hamartomas form by a different pathway—though malignant transformation can still recruit Wnt-driven changes."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Peutz-Jeghers fills the digestive tract with hamartomatous polyps: STK11/LKB1 loss seeds large hamartomas, especially in the small bowel, that bleed and cause intussusception in childhood—so GI polyps and obstruction often bring the diagnosis."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Pigmented spots make Peutz-Jeghers visible on the skin: mucocutaneous melanin macules on the lips, mouth and fingers appear in childhood, so these freckle-like spots are often the first clue to this STK11 polyposis-and-cancer syndrome."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Peutz-Jeghers affects the reproductive system with distinctive tumors: women develop sex-cord tumors with annular tubules (SCTAT) and raised cervical/ovarian cancer risk, and men can get calcifying Sertoli cell testicular tumors—warranting gonadal surveillance."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Peutz-Jeghers hamartomas stud the whole gut, including the stomach: gastric polyps add to the small-bowel ones, contributing bleeding and a raised gastric-cancer risk, so upper endoscopy joins small-bowel surveillance in management."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Peutz-Jeghers often presents with iron-deficiency anemia: chronic slow bleeding from gastrointestinal hamartomas depletes iron, so unexplained anemia in a young patient with lip pigmentation can be the clue that prompts diagnosis."
  - target: 01-human/07-system/mutyh-associated-polyposis
    relation: connects-to
    note: "Peutz-Jeghers and MUTYH-associated polyposis are distinct inherited polyposes: PJS makes STK11-driven hamartomas with smooth-muscle cores, while MAP makes adenomas from oxidative DNA-repair failure—so polyp histology and gene testing separate them."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Peutz-Jeghers grows hormone-secreting gonadal tumors: ovarian sex cord tumors (SCTAT) and testicular Sertoli cell tumors pour out estrogen, causing precocious puberty, gynecomastia, and irregular bleeding—distinctive endocrine clues to the syndrome."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Peutz-Jeghers unleashes AKT-mTOR growth: LKB1 loss disables the AMPK brake, so the AKT-mTOR pathway runs unchecked in the hamartomatous polyps—rationale for trialing mTOR inhibitors to slow polyp growth and cancer risk."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Peutz-Jeghers polyps grow large on a fibroblast-rich hamartomatous stroma: their bulky, arborizing structure can drag a loop of bowel into itself (intussusception), the acute complication that often brings these polyps to medical attention."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Peutz-Jeghers polyps bleed and drain iron: the large hamartomas erode and ooze blood into the gut, and with the obstruction they cause, chronic blood loss makes iron-deficiency anemia a frequent sign in these patients."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages help build the Peutz-Jeghers polyp: tumor-associated macrophages populate the fibroblast-rich hamartomatous stroma and secrete growth and angiogenic factors, supporting the bulky polyps that arise from LKB1 loss."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Peutz-Jeghers polyps recruit blood vessels via VEGF: LKB1/AMPK loss disinhibits mTOR, which drives VEGF and angiogenesis to feed the growing hamartomas, part of the rationale for mTOR-pathway drugs studied in the syndrome."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Peutz-Jeghers' freckles are made with copper: the dark spots on the lips and mouth are melanin, built by the copper-dependent enzyme tyrosinase, the mucocutaneous sign that flags the syndrome."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Peutz-Jeghers carries a steep pancreatic cancer risk: STK11 loss makes the pancreas one of the syndrome's most dangerous cancer sites, so it joins the gut and breast in lifelong surveillance."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Peutz-Jeghers polyps are fragile and vascular: their endothelial-lined vessels tear easily as the bulky polyps tumble and intussuscept, causing the recurrent bleeding that drains the body's iron."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photons keep watch over the small bowel: video capsule endoscopy and MR enterography survey the long stretches of intestine that ordinary scopes miss, finding the hamartomatous polyps before they grow big enough to bleed or obstruct."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Losing STK11 raises the lung's cancer risk: Peutz-Jeghers carries one of the highest lifetime risks of lung cancer among inherited syndromes, so the same gene that studs the gut with polyps also primes the airway lining for malignancy."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver becomes a target as Peutz-Jeghers cancers spread: the syndrome's many adenocarcinomas — pancreatic, gastrointestinal, breast — metastasize there, so liver imaging joins the broad cancer surveillance these patients need."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Peutz-Jeghers often shows up as anemia: the hamartomatous polyps bleed slowly into the gut, draining red cells and iron until a child turns up pale and microcytic — sometimes the first clue that leads to the diagnosis."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "The telltale freckling is melanin under the microscope: the dark macules on lips and buccal mucosa come from melanin packed into basal keratinocytes, pigment granules that electron microscopy resolves within the epidermis."
  - target: 01-human/07-system/endometrial-cancer
    relation: connects-to
    note: "Peutz-Jeghers reaches into the gynecologic tract: beyond its signature cervical and ovarian sex-cord tumors, the syndrome raises the lifetime risk of endometrial cancer, adding the uterus to its wide field of cancer surveillance."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibody stains confirm the hallmark polyp: desmin and smooth-muscle-actin staining reveal the arborizing tree of smooth muscle that defines a Peutz-Jeghers hamartoma, separating it from the adenomas of other polyposis syndromes."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "The thyroid joins the long cancer list: differentiated (papillary) thyroid carcinoma appears within the Peutz-Jeghers tumor spectrum, one more organ folded into the lifelong, head-to-pelvis surveillance the syndrome demands."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Chronic ooze from the polyps shows in the blood: the slow intestinal bleeding that drains iron also drives a reactive thrombocytosis, the platelet count climbing as the marrow responds to ongoing loss."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "STK11 is the master switch above AMPK: losing it deranges the LKB1-AMPK energy sensor that ties metabolism to growth, which is why metformin — an AMPK activator that improves insulin signaling — is studied as chemoprevention in Peutz-Jeghers."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Losing LKB1 turns tumors cold: STK11/LKB1 loss reshapes the microenvironment to exclude and disarm cytotoxic T cells, a recognized driver of resistance to checkpoint immunotherapy in the lung and other cancers it predisposes to."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "The faulty gene sits at the body's energy controls: LKB1-AMPK signaling governs how adipocytes and other tissues sense and store energy, so the syndrome's defect reaches a metabolic network far beyond the gut polyps it is known for."
---

# Peutz-Jeghers Syndrome

## Overview

**Peutz-Jeghers syndrome (PJS)** is an autosomal dominant hamartomatous polyposis syndrome caused by germline pathogenic variants in **STK11** (LKB1), a master serine/threonine kinase that activates AMPK and controls mTOR signaling and cell polarity. PJS affects approximately 1 in 50,000 to 200,000 individuals and is characterized by: (1) **hamartomatous gastrointestinal polyps** (predominantly small intestine) lined by branching smooth muscle with overlying normal mucosa — the so-called "Christmas tree" arborizing pattern; (2) **mucocutaneous melanotic macules** (lips, perioral skin, buccal mucosa, fingertips, genitalia) from melanin deposits in dermal macrophages; and (3) markedly elevated lifetime risks for multiple cancers — most prominently breast (~45%), CRC (~39%), and pancreatic (~36%) by age 70. The most acute complication is **small bowel intussusception** from large polyps, presenting as episodic abdominal pain, vomiting, and obstruction. There is no cure; management focuses on endoscopic surveillance and polypectomy to prevent obstruction and cancer [^hearle-2006-pjs-cancer].

**Epidemiology:**
- Prevalence: 1/50,000-200,000; estimated ~5,000-15,000 cases in the USA
- Inheritance: autosomal dominant; 50% transmission per pregnancy; ~45% de novo (no family history)
- STK11 germline pathogenic variant: ~94% of PJS families; ~6% STK11-negative (possible other loci or missed variants)
- Penetrance: nearly complete for polyps (>95%); cancer risk penetrance variable and age-dependent
- Median age of PJS diagnosis: typically childhood (polyp detection or intussusception) or young adulthood; mucocutaneous pigmentation may be the first clue in infancy

**Cumulative cancer risks by age 70 (Hearle 2006):** [^hearle-2006-pjs-cancer]

| Cancer | Cumulative risk by age 70 | Notes |
|---|---|---|
| Breast | ~45-54% | High; BRCA1/2-equivalent risk in some series |
| Colorectal | ~39% | Hamartoma-adenoma-carcinoma sequence |
| Pancreatic | ~36% | Very high; aggressive; EUS surveillance critical |
| Small intestinal | ~13% | Arising from PJ polyps; rare pre-PJS surveillance era |
| Gastric | ~29% | Type depends on PJS genetics and geography |
| Ovarian (SCTAT) | ~21% | Sex cord tumor with annular tubules — unique PJS tumor |
| Cervical (adenoma malignum) | ~10% | Minimal deviation adenocarcinoma; unusual PJS tumor |
| Uterine | ~9% | Less studied; cervical + uterine combined risk ~10-15% |

## Structure

### STK11 and PJS polyp biology

**STK11/LKB1 molecular basis:**
STK11 is the master upstream kinase of AMPK and 12 AMPK-related kinases (MARK1-4, SIK1-3, BRSK1/2, NUAK1/2); germline STK11 LOF → haploinsufficiency of STK11 in intestinal epithelium → somatic second hit in polyp epithelium → biallelic STK11 LOF → AMPK inactivation → mTOR hyperactivation → epithelial overgrowth + smooth muscle proliferation → hamartoma formation; unlike FAP (adenomatous) or juvenile polyposis (JPS), PJS polyps are hamartomas — they contain normal cellular elements in disorganized architecture

**PJ polyp pathology:**
- Macroscopic: lobulated, pedunculated; largest in small intestine (jejunum > ileum); smaller in colon and stomach; multiple (dozens to hundreds over a lifetime)
- Microscopic: arborizing smooth muscle core (from muscularis mucosae) covered by normal colonic/small intestinal epithelium; the "Christmas tree" pattern of smooth muscle branching into polyp lobules is pathognomonic; no dysplasia in the polyp itself
- Intussusception mechanism: large polyp acts as intussusceptum (lead point) → peristalsis → telescoping of bowel around polyp → obstruction; can be acute surgical emergency; PJS presents with recurrent episodic intussusception in childhood/adolescence

**Mucocutaneous pigmentation:**
- Mechanism: dermal melanin deposition in histiocytes/macrophages; NOT melanocyte proliferation (non-neoplastic)
- Distribution: lips (lower and upper; most specific for PJS), perioral skin, buccal mucosa, fingertips, palms, genitalia; may be present at birth or appear in early childhood
- Fate: perioral and skin pigmentation may fade with age (especially after puberty); buccal mucosal pigmentation tends to persist; the fading of lip pigmentation does not mean LOF — PJS diagnosis is still valid
- Distinction: Laugier-Hunziker syndrome (acquired; no polyps; no cancer risk); Addison disease (diffuse hyperpigmentation, not discrete macules); normal ethnic variation

### Unique PJS tumor types

**Sex cord tumor with annular tubules (SCTAT):**
Unique ovarian tumor type in PJS: arises from granulosa-theca cells; bilateral (multifocal) in PJS (contrast: unilateral in sporadic SCTAT); usually benign in PJS; small, calcified; estrogen and inhibin-producing → menstrual irregularities, precocious puberty; IHC: inhibin-positive, calretinin-positive; malignancy rare but possible in large PJS SCTAT; annual TVUS for female PJS patients

**Adenoma malignum (minimal deviation adenocarcinoma of cervix):**
Rare cervical glandular tumor seen disproportionately in PJS (~10% lifetime risk, vs <0.1% general population); well-differentiated mucin-producing glands → easily mistaken for normal endocervical glands; extremely difficult to diagnose by cytology alone; diagnosis: deep biopsy + CEA staining; pap smear + annual cervical examination for PJS females; radical hysterectomy if diagnosed

## Function

### PJS carcinogenesis: hamartoma-adenoma-carcinoma sequence

**Mechanism of cancer development:**
PJS polyps themselves are hamartomas — they have very low intrinsic malignant potential; however, PJS patients develop adenomas (not from PJ hamartomas directly, but as separate lesions) at higher rates than the general population; adenomas arise in the context of STK11 LOF + mTOR hyperactivation + dysregulated epithelial proliferation; adenoma → carcinoma sequence is the main pathway for CRC in PJS; small intestinal cancer may arise directly from PJ hamartoma-adenoma transition (uncommon)

**mTOR pathway in PJS tumorigenesis:**
STK11 LOF → AMPK loss → mTORC1 unrestrained → S6K1 activation → ribosome biogenesis → epithelial and smooth muscle growth → PJ polyp formation; in mouse models: STK11+/- mice develop GI polyps similar to human PJS; rapamycin (mTOR inhibitor) given to STK11+/- mice reduces polyp number and size by ~50-80% (several independent studies); this validates mTOR as the mechanistic driver; in STK11+/- cells: rapamycin induces autophagy and corrects the proliferative excess

**STK11 and breast cancer risk:**
PJS breast cancer risk (~45%) approaches BRCA1/2-associated risk; mechanism: STK11 LOF → AMPK loss → mTOR hyperactivation in breast epithelium → accelerated proliferation; STK11-mutant breast cancer: no specific histology; HR+ predominance; no clear HER2 enrichment; breast MRI surveillance (same as BRCA1/2 guidelines) recommended from age 25; risk-reducing mastectomy: discussed but evidence limited compared to BRCA1/2 context

## Pathology

### Diagnosis

**Clinical diagnostic criteria:**
Any ONE of the following confirms PJS diagnosis:
1. Three or more histologically confirmed PJ polyps (small intestinal hamartomas with arborizing smooth muscle)
2. Any number of PJ polyps + family history of PJS in a first-degree relative
3. Characteristic mucocutaneous pigmentation + family history of PJS
4. Any number of PJ polyps + characteristic mucocutaneous pigmentation

**Genetic testing:**
- STK11 germline sequencing (full coding + splice sites) + MLPA for large rearrangements: ~94% detection rate in clinical PJS
- ~6% STK11-negative PJS: likely technical false-negative (deep intronic, somatic mosaicism) or extremely rare alternative loci
- Pathogenicity classification: truncating = pathogenic; missense: variant interpretation using functional assays and co-segregation data
- Cascade testing: all first-degree relatives of STK11 carrier should be offered testing

### Surveillance and management (NCCN/ESMO 2024)

**Gastrointestinal surveillance:**

Small bowel (highest priority):
- Video capsule endoscopy (VCE): gold standard for small bowel visualization; every 1-3 years from age 8-10; polypectomy of polyps >1-1.5 cm by device-assisted enteroscopy (double-balloon enteroscopy, DBE) to prevent intussusception
- DBE polypectomy: preferred over surgical resection to preserve small bowel length; all PJ polyps >1.5 cm should be removed

Upper GI (gastric/duodenal):
- Upper endoscopy: every 1-3 years from age 8-10; gastric PJ polyps usually small; duodenal surveillance important (ampullary region)

Colorectal:
- Colonoscopy: every 1-3 years from age 15-20 (some guidelines: 18 years or first bowel symptoms, whichever is first)
- Adenomatous polyps removed at colonoscopy (same as non-PJS adenoma management)

**Gynecologic surveillance (female PJS):**
- Pelvic exam + pap smear annually from age 18-20 (cervical adenoma malignum)
- Pelvic TVUS: annually from age 20-25 (SCTAT detection)
- Endometrial biopsy: not routinely recommended (uterine cancer risk ~9% is lower); evaluate abnormal uterine bleeding

**Breast surveillance:**
- Annual breast MRI + annual mammogram from age 25-30 (same intensity as BRCA1/2)
- Clinical breast exam every 6 months from age 25
- Risk-reducing bilateral mastectomy: considered in high-risk individuals after discussion of risk-benefit; less evidence than BRCA1/2 context

**Pancreatic surveillance:**
- Endoscopic ultrasound (EUS) + MRI/MRCP: every 1-2 years from age 30-35
- CA19-9: annual from age 30-35 (modest sensitivity/specificity; trend more useful than single value)
- Urgency: PJS pancreatic cancer is often detected at advanced/unresectable stage; early detection critical

**Treatment:**
- Small bowel intussusception: urgent endoscopic or surgical reduction; DBE or laparotomy + intraoperative enteroscopy to clear accessible polyps at time of surgery
- Cancer treatment: same as sporadic cancer of that type; no PJS-specific chemotherapy regimen
- mTOR inhibition: rapamycin (sirolimus) + metformin combination pilot trial in PJS patients (NCT03943992): reduces polyp burden modestly; ongoing; not yet standard of care
- Metformin: single-agent pilot data showing reduction in small bowel polyp number in PJS; Phase 2 trials ongoing; mechanism: indirect AMPK activation bypasses STK11 LOF

**Prognosis:**
Without surveillance: cumulative cancer risk reaches ~85-93% by age 70 (all cancer types combined); with active surveillance: cancer incidence and mortality markedly reduced but not eliminated; intussusception risk remains the dominant pediatric morbidity; cancer accounts for the major adult morbidity and mortality

## Connections

- `connects-to` → **[STK11](../../03-molecular/stk11/README.md)** — Germline STK11 mutations cause ~94% of PJS; STK11 encodes LKB1 (AMPK activator); haploinsufficiency → polyp formation (second hit in polyp epithelium); truncating STK11 mutations associate with higher cancer risk than missense; STK11 germline panel + deletion analysis required
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — STK11 LOF → AMPK inactivation → mTOR unrestrained → hamartoma growth in PJS; rapamycin reduces polyp burden in STK11+/− mouse models; mTORC1 is the primary growth driver in PJS hamartomas; AMPK activators (metformin) explored as chemoprevention in PJS pilot studies
- `connects-to` → **[Colorectal Cancer](../../07-system/colorectal-cancer/README.md)** — PJS lifetime CRC risk ~39% by age 70 (Hearle 2006); PJS CRC arises through hamartoma-adenoma-carcinoma sequence; proximal colon predominance; colonoscopy with polypectomy every 1-3 years from age 15-20; CRC is the third most common PJS cancer after breast and pancreatic
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — PJS lifetime pancreatic cancer risk ~36% by age 70; EUS + MRI surveillance from age 30-35; STK11 LOF co-mutation with KRAS in pancreatic cancer → mTOR + MAPK dual activation; PJS pancreatic cancer prognosis poor; resectability rate ~40% at detection
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — STK11 LOF → AMPK loss → mTORC1 unrestrained → S6K1/4EBP1 → epithelial and smooth muscle proliferation → PJ hamartoma formation; rapamycin reduces polyp burden ~50-80% in STK11+/− mice; sirolimus + metformin pilot trial ongoing in PJS patients (NCT03943992).
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — PJS breast cancer lifetime risk ~45-54% by age 70 (BRCA1/2-equivalent); breast MRI + mammogram from age 25; STK11 LOF → mTOR hyperactivation in breast epithelium; HR+ predominant; no PJS-specific breast cancer histology; risk-reducing bilateral mastectomy discussed.
- `connects-to` → **[NSCLC](../nsclc/README.md)** — STK11/LKB1 somatic mutations in ~15-20% of KRAS-mutant lung adenocarcinoma; STK11 loss → PD-L1 downregulation + CXCL7 secretion → neutrophilic immunosuppressive TME → primary ICB resistance; STK11-mutant KRAS+ NSCLC is the poorest immunotherapy responder subgroup.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — The small intestine is the danger zone of Peutz-Jeghers syndrome: large hamartomatous polyps in the jejunum and ileum become lead points for intussusception — the most common complication, often needing emergency surgery in childhood; surveillance and polypectomy prevent it.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — The diagnostic clue to Peutz-Jeghers syndrome is on the skin and lips: mucocutaneous melanotic macules — dark freckle-like spots on the lips, buccal mucosa, and fingertips — appear in infancy and often fade with age, but with hamartomatous polyps they establish the diagnosis.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Peutz-Jeghers hamartomas have a unique histology: an arborizing (tree-like) core of bundled smooth muscle extending into the polyp, covered by normal epithelium — distinguishing them from the edematous juvenile polyps of JPS or the dysplastic adenomas of FAP.
- `connects-to` → **[Juvenile Polyposis Syndrome](../juvenile-polyposis-syndrome/README.md)** — Peutz-Jeghers and juvenile polyposis are the two main hamartomatous polyposis syndromes: PJS (STK11) produces arborizing smooth-muscle polyps and mucocutaneous pigmentation, while JPS (SMAD4/BMPR1A) produces juvenile polyps—both raise GI cancer risk.
- `connects-to` → **[Ovarian Cancer](../ovarian-cancer/README.md)** — Peutz-Jeghers syndrome predisposes to distinctive ovarian tumors: sex cord tumors with annular tubules (SCTAT) and mucinous tumors arise from STK11 loss, often causing precocious puberty or estrogen effects—part of the syndrome's broad, organ-spanning cancer risk.
- `connects-to` → **[Cervical Cancer](../cervical-cancer/README.md)** — Peutz-Jeghers syndrome carries a rare cervical cancer—adenoma malignum (minimal-deviation adenocarcinoma): this deceptively bland, HPV-independent tumor is strongly associated with STK11 loss, so PJS patients warrant gynecologic surveillance for it.
- `connects-to` → **[Cowden Syndrome](../cowden-syndrome/README.md)** — Peutz-Jeghers and Cowden are both hamartomatous polyposis syndromes with different genes: PJS from STK11 loss giving GI hamartomas and mucocutaneous pigmentation, Cowden from PTEN (PI3K-AKT) loss—both fill the gut with hamartomas and raise multi-organ cancer risk.
- `connects-to` → **[Familial Adenomatous Polyposis](../fap/README.md)** — Peutz-Jeghers and FAP are inherited polyposis syndromes with opposite polyp types: PJS produces hamartomatous polyps from STK11 loss, while FAP produces hundreds of adenomatous polyps from APC loss with near-certain colorectal cancer—hamartoma versus adenoma.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — Peutz-Jeghers raises gastric as well as colorectal cancer risk: STK11 loss seeds hamartomatous polyps throughout the stomach and small bowel that can bleed, obstruct or harbor dysplasia, so upper-GI surveillance accompanies colonoscopy in PJS patients from childhood.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Peutz-Jeghers polyps stud the large intestine and beyond: STK11 loss produces hamartomatous polyps throughout the GI tract—small bowel most, but also colon—that bleed, cause intussusception, and modestly raise colorectal cancer risk.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — PJS hamartomas arise in disordered intestinal epithelium: loss of the STK11/LKB1 kinase deranges epithelial polarity and growth, so the crypts overgrow into the branching, smooth-muscle-cored hamartomatous polyps that distinguish PJS from adenomatous polyposis.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — PJS shows a non-Wnt route to GI tumors: unlike FAP's APC/Wnt adenomas, Peutz-Jeghers polyps arise from STK11/LKB1-AMPK-mTOR dysregulation, so its hamartomas form by a different pathway—though malignant transformation can still recruit Wnt-driven changes.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Peutz-Jeghers fills the digestive tract with hamartomatous polyps: STK11/LKB1 loss seeds large hamartomas, especially in the small bowel, that bleed and cause intussusception in childhood—so GI polyps and obstruction often bring the diagnosis.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Pigmented spots make Peutz-Jeghers visible on the skin: mucocutaneous melanin macules on the lips, mouth and fingers appear in childhood, so these freckle-like spots are often the first clue to this STK11 polyposis-and-cancer syndrome.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Peutz-Jeghers affects the reproductive system with distinctive tumors: women develop sex-cord tumors with annular tubules (SCTAT) and raised cervical/ovarian cancer risk, and men can get calcifying Sertoli cell testicular tumors—warranting gonadal surveillance.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Peutz-Jeghers hamartomas stud the whole gut, including the stomach: gastric polyps add to the small-bowel ones, contributing bleeding and a raised gastric-cancer risk, so upper endoscopy joins small-bowel surveillance in management.
- `connects-to` → **[Iron Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Peutz-Jeghers often presents with iron-deficiency anemia: chronic slow bleeding from gastrointestinal hamartomas depletes iron, so unexplained anemia in a young patient with lip pigmentation can be the clue that prompts diagnosis.
- `connects-to` → **[MUTYH-Associated Polyposis](../mutyh-associated-polyposis/README.md)** — Peutz-Jeghers and MUTYH-associated polyposis are distinct inherited polyposes: PJS makes STK11-driven hamartomas with smooth-muscle cores, while MAP makes adenomas from oxidative DNA-repair failure—so polyp histology and gene testing separate them.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Peutz-Jeghers grows hormone-secreting gonadal tumors: ovarian sex cord tumors (SCTAT) and testicular Sertoli cell tumors pour out estrogen, causing precocious puberty, gynecomastia, and irregular bleeding—distinctive endocrine clues to the syndrome.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Peutz-Jeghers unleashes AKT-mTOR growth: LKB1 loss disables the AMPK brake, so the AKT-mTOR pathway runs unchecked in the hamartomatous polyps—rationale for trialing mTOR inhibitors to slow polyp growth and cancer risk.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Peutz-Jeghers polyps grow large on a fibroblast-rich hamartomatous stroma: their bulky, arborizing structure can drag a loop of bowel into itself (intussusception), the acute complication that often brings these polyps to medical attention.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Peutz-Jeghers polyps bleed and drain iron: the large hamartomas erode and ooze blood into the gut, and with the obstruction they cause, chronic blood loss makes iron-deficiency anemia a frequent sign in these patients.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages help build the Peutz-Jeghers polyp: tumor-associated macrophages populate the fibroblast-rich hamartomatous stroma and secrete growth and angiogenic factors, supporting the bulky polyps that arise from LKB1 loss.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Peutz-Jeghers polyps recruit blood vessels via VEGF: LKB1/AMPK loss disinhibits mTOR, which drives VEGF and angiogenesis to feed the growing hamartomas, part of the rationale for mTOR-pathway drugs studied in the syndrome.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Peutz-Jeghers' freckles are made with copper: the dark spots on the lips and mouth are melanin, built by the copper-dependent enzyme tyrosinase, the mucocutaneous sign that flags the syndrome.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Peutz-Jeghers carries a steep pancreatic cancer risk: STK11 loss makes the pancreas one of the syndrome's most dangerous cancer sites, so it joins the gut and breast in lifelong surveillance.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Peutz-Jeghers polyps are fragile and vascular: their endothelial-lined vessels tear easily as the bulky polyps tumble and intussuscept, causing the recurrent bleeding that drains the body's iron.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photons keep watch over the small bowel: video capsule endoscopy and MR enterography survey the long stretches of intestine that ordinary scopes miss, finding the hamartomatous polyps before they grow big enough to bleed or obstruct.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Losing STK11 raises the lung's cancer risk: Peutz-Jeghers carries one of the highest lifetime risks of lung cancer among inherited syndromes, so the same gene that studs the gut with polyps also primes the airway lining for malignancy.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver becomes a target as Peutz-Jeghers cancers spread: the syndrome's many adenocarcinomas — pancreatic, gastrointestinal, breast — metastasize there, so liver imaging joins the broad cancer surveillance these patients need.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Peutz-Jeghers often shows up as anemia: the hamartomatous polyps bleed slowly into the gut, draining red cells and iron until a child turns up pale and microcytic — sometimes the first clue that leads to the diagnosis.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — The telltale freckling is melanin under the microscope: the dark macules on lips and buccal mucosa come from melanin packed into basal keratinocytes, pigment granules that electron microscopy resolves within the epidermis.
- `connects-to` → **[Endometrial Cancer](../endometrial-cancer/README.md)** — Peutz-Jeghers reaches into the gynecologic tract: beyond its signature cervical and ovarian sex-cord tumors, the syndrome raises the lifetime risk of endometrial cancer, adding the uterus to its wide field of cancer surveillance.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibody stains confirm the hallmark polyp: desmin and smooth-muscle-actin staining reveal the arborizing tree of smooth muscle that defines a Peutz-Jeghers hamartoma, separating it from the adenomas of other polyposis syndromes.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — The thyroid joins the long cancer list: differentiated (papillary) thyroid carcinoma appears within the Peutz-Jeghers tumor spectrum, one more organ folded into the lifelong, head-to-pelvis surveillance the syndrome demands.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Chronic ooze from the polyps shows in the blood: the slow intestinal bleeding that drains iron also drives a reactive thrombocytosis, the platelet count climbing as the marrow responds to ongoing loss.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — STK11 is the master switch above AMPK: losing it deranges the LKB1-AMPK energy sensor that ties metabolism to growth, which is why metformin — an AMPK activator that improves insulin signaling — is studied as chemoprevention in Peutz-Jeghers.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Losing LKB1 turns tumors cold: STK11/LKB1 loss reshapes the microenvironment to exclude and disarm cytotoxic T cells, a recognized driver of resistance to checkpoint immunotherapy in the lung and other cancers it predisposes to.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — The faulty gene sits at the body's energy controls: LKB1-AMPK signaling governs how adipocytes and other tissues sense and store energy, so the syndrome's defect reaches a metabolic network far beyond the gut polyps it is known for.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^hearle-2006-pjs-cancer]: Hearle N, Schumacher V, Menko FH, et al. Frequency and spectrum of cancers in the Peutz-Jeghers syndrome. *Clin Cancer Res.* 2006;12(10):3209-3215. [doi:10.1158/1078-0432.CCR-06-0083](https://doi.org/10.1158/1078-0432.CCR-06-0083) · [PubMed 16707622](https://pubmed.ncbi.nlm.nih.gov/16707622/)
[^skoulidis-2018-stk11-nsclc]: Skoulidis F, Goldberg ME, Greenawalt DM, et al. STK11/LKB1 mutations and PD-1 inhibitor resistance in KRAS-mutant lung adenocarcinoma. *Cancer Cell.* 2018;34(3):412-424. [doi:10.1016/j.ccell.2018.08.013](https://doi.org/10.1016/j.ccell.2018.08.013) · [PubMed 30174241](https://pubmed.ncbi.nlm.nih.gov/30174241/)

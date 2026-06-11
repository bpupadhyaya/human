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

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^hearle-2006-pjs-cancer]: Hearle N, Schumacher V, Menko FH, et al. Frequency and spectrum of cancers in the Peutz-Jeghers syndrome. *Clin Cancer Res.* 2006;12(10):3209-3215. [doi:10.1158/1078-0432.CCR-06-0083](https://doi.org/10.1158/1078-0432.CCR-06-0083) · [PubMed 16707622](https://pubmed.ncbi.nlm.nih.gov/16707622/)
[^skoulidis-2018-stk11-nsclc]: Skoulidis F, Goldberg ME, Greenawalt DM, et al. STK11/LKB1 mutations and PD-1 inhibitor resistance in KRAS-mutant lung adenocarcinoma. *Cancer Cell.* 2018;34(3):412-424. [doi:10.1016/j.ccell.2018.08.013](https://doi.org/10.1016/j.ccell.2018.08.013) · [PubMed 30174241](https://pubmed.ncbi.nlm.nih.gov/30174241/)

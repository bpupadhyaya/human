---
schema: human-scale-entry/v1
id: neuroendocrine-tumors
name: Neuroendocrine Tumors
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Neuroendocrine tumors arise from diffuse neuroendocrine cells; well-differentiated G1/G2 NETs are treated with SSA (octreotide/lanreotide) and lutetium-177 DOTATATE (NETTER-1); everolimus (RADIANT) and sunitinib approved for pNET; poorly differentiated NEC treated as SCLC."
aliases: ["neuroendocrine tumors", "NET", "NEN", "carcinoid tumor", "pNET", "pancreatic NET", "GEP-NET", "neuroendocrine carcinoma", "NEC", "PRRT", "Lutathera", "DOTATATE"]
sources:
  - id: yao-2011-radiant3
    type: peer-reviewed
    cite: "Yao JC, Shah MH, Ito T, et al. Everolimus for advanced pancreatic neuroendocrine tumors. N Engl J Med. 2011;364(6):514-523."
    doi: "10.1056/NEJMoa1009290"
    pmid: "21306237"
    url: "https://doi.org/10.1056/NEJMoa1009290"
  - id: raymond-2011-sunitinib-pnet
    type: peer-reviewed
    cite: "Raymond E, Dahan L, Raoul JL, et al. Sunitinib malate for the treatment of pancreatic neuroendocrine tumors. N Engl J Med. 2011;364(6):501-513."
    doi: "10.1056/NEJMoa1003825"
    pmid: "21306236"
    url: "https://doi.org/10.1056/NEJMoa1003825"
cross_links:
  - target: 01-human/03-molecular/sstr2
    relation: connects-to
    note: "SSTR2 overexpression in well-differentiated NETs enables SSA therapy (octreotide/lanreotide; PROMID/CLARINET antiproliferative trials) and 177Lu-DOTATATE PRRT (NETTER-1: 14-month PFS benefit); DOTATATE PET/CT confirms SSTR2 expression for PRRT eligibility."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Everolimus (RADIANT-3: PFS 11.0 vs 4.6 months in pNET; RADIANT-4: PFS 11.0 vs 3.9 months in non-functional NET) is approved for progressive/metastatic NET; mTOR inhibition reduces HIF-1α, VEGF, and cell cycle progression; resistance via AKT rebound."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Sunitinib (VEGFR1/2/3/PDGFRA/B; A6181111 trial: PFS 11.4 vs 5.5 months) is approved for pancreatic NET; NETs are hypervascular tumors with high VEGF expression; bevacizumab studied in midgut NET; cabozantinib (VEGFR2+MET) under investigation."
  - target: 01-human/03-molecular/glucagon
    relation: connects-to
    note: "Functioning pNETs include glucagonoma (necrolytic migratory erythema, diabetes), insulinoma (most common pNET), gastrinoma (Zollinger-Ellison), and VIPoma; SSTR2 agonists (octreotide) control glucagonoma and other secretory syndromes via α-cell glucagon inhibition."
  - target: 01-human/07-system/men1-syndrome
    relation: connects-to
    note: "Germline MEN1 mutations underlie ~10% of pancreatic NETs, which in MEN1 are typically multifocal and non-functioning alongside parathyroid and pituitary tumors; menin loss (H3K4me3 at target promoters) is also the most common somatic event (~44%) in sporadic pNET."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Midgut carcinoids secrete serotonin that, once liver metastases bypass portal clearance, causes carcinoid syndrome — flushing, secretory diarrhea, and carcinoid heart disease; urinary 5-HIAA tracks it and telotristat (a tryptophan hydroxylase inhibitor) curbs refractory diarrhea."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "The pancreas is a leading NET site: functioning pNETs (insulinoma, gastrinoma, glucagonoma, VIPoma) cause hormone syndromes while non-functioning pNETs grow silently; everolimus and sunitinib are pNET-specific approvals, and DAXX/ATRX-mutant pNETs use the ALT telomere pathway."
  - target: 01-human/07-system/neuroblastoma
    relation: connects-to
    note: "Neuroendocrine tumors and neuroblastoma are both neural-crest-derived, amine-handling cancers at opposite ends of age and behavior: NETs are well-differentiated, slow-growing adult tumors, while neuroblastoma is an aggressive MYCN-driven embryonal cancer of children."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "The small intestine (midgut) is a classic NET site: serotonin-secreting enterochromaffin-cell tumors of the ileum grow slowly but metastasize to the liver, producing carcinoid syndrome (flushing, diarrhea, carcinoid heart disease) and are SSTR2-positive."
  - target: 01-human/07-system/men4-syndrome
    relation: connects-to
    note: "MEN4, like MEN1, is a hereditary cause of neuroendocrine tumors: germline CDKN1B/p27 loss predisposes to pancreatic NETs alongside parathyroid and pituitary tumors, so a young or multifocal NET prompts germline MEN1 and CDKN1B testing for syndromic disease."
  - target: 01-human/07-system/pheochromocytoma-paraganglioma
    relation: connects-to
    note: "Pheochromocytoma/paraganglioma are neuroendocrine tumors of the adrenal medulla and sympathetic ganglia: like other NETs they express somatostatin receptors (enabling DOTATATE imaging and PRRT) but uniquely secrete catecholamines, causing paroxysmal hypertension."
  - target: 01-human/07-system/vhl-disease
    relation: connects-to
    note: "VHL disease is a major hereditary cause of neuroendocrine tumors: germline VHL loss predisposes to pancreatic neuroendocrine tumors and pheochromocytomas alongside its hemangioblastomas and clear-cell RCC, so a young patient with a panNET warrants VHL and MEN1 testing."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver dictates carcinoid syndrome in neuroendocrine tumors: a midgut NET's serotonin is normally cleared by hepatic first-pass, so flushing and diarrhea appear only once liver metastases dump vasoactive amines directly into the systemic circulation."
  - target: 01-human/07-system/sclc
    relation: connects-to
    note: "Neuroendocrine tumors and small-cell lung cancer are the two ends of the neuroendocrine spectrum: well-differentiated NETs are indolent, while SCLC is a poorly differentiated, high-grade neuroendocrine carcinoma that grows explosively—same lineage, opposite tempo."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Insulinoma is the prototypical functional neuroendocrine tumor: a pancreatic-islet NET that autonomously secretes insulin, causing fasting hypoglycemia (Whipple's triad)—it shows how NETs are classified and treated by the hormone they produce."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lung is a major site of neuroendocrine tumors: from indolent typical bronchial carcinoids through atypical carcinoids to high-grade small-cell neuroendocrine carcinoma, all arising from pulmonary neuroendocrine cells—'lung NET' spans benign to lethal."
---

# Neuroendocrine Tumors

## Overview

**Neuroendocrine tumors (NETs)** are a heterogeneous group of neoplasms arising from the diffuse neuroendocrine system — secretory cells distributed throughout the body that share features of neurons and endocrine glands (dense-core secretory granules, specific hormone production, chromogranin A/synaptophysin expression). NETs range from indolent well-differentiated tumors (G1 carcinoids) with decades-long survival to aggressive poorly differentiated neuroendocrine carcinomas (NECs) biologically similar to small cell lung cancer (SCLC) with median OS <12 months. Gastroenteropancreatic NETs (GEP-NETs) account for the majority of NETs, with the small bowel (midgut carcinoids), pancreas, and rectum being the most common primary sites. The therapeutic revolution in GEP-NET includes: somatostatin analogs (SSA) for symptom control and antiproliferative effect; peptide receptor radionuclide therapy (PRRT) with lutetium-177 DOTATATE (NETTER-1); mTOR inhibition with everolimus (RADIANT trials); and sunitinib for pancreatic NET [^yao-2011-radiant3] [^raymond-2011-sunitinib-pnet].

**Incidence and epidemiology:**
- Overall incidence: ~7/100,000/year in the USA; prevalence ~170,000 (rising due to better detection)
- Most common primary sites: Rectum (~25%), small intestine (~22%), pancreas (~15%), lung (~13%), appendix (~8%), stomach (~7%), colon (~7%)
- Small intestinal NETs (midgut carcinoids): Well-differentiated G1/G2; SSTR2+; often present with liver metastases + carcinoid syndrome; 5-year OS ~83% localized, ~32% metastatic
- Pancreatic NETs (pNET): Functioning (insulinoma, gastrinoma, glucagonoma) or non-functioning; VHL syndrome, MEN1 (MEN1 germline mutations in ~10% of pNET → multiple tumors); 5-year OS ~55-65% all stages
- Appendix NETs: Incidentally found at appendectomy; most <2 cm → appendectomy curative; >2 cm → right hemicolectomy

**WHO 2022 classification:**
- **NET G1 (Ki-67 <3%):** Well-differentiated; low mitotic rate; slowly progressive; SSA antiproliferative
- **NET G2 (Ki-67 3-20%):** Well-differentiated; intermediate; SSA + targeted therapy; PRRT
- **NET G3 (Ki-67 >20%):** Well-differentiated but high Ki-67; SSTR2 often retained; PRRT may work; distinct from NEC
- **NEC (poorly differentiated, Ki-67 >20%):** SCLC-type (small cell NEC) or large cell NEC; SSTR2 low/absent; platinum/etoposide
- **MiNEN (mixed neuroendocrine-non-neuroendocrine neoplasm):** ≥30% of each component; treat aggressive component

## Structure

### Tumor biology and neuroendocrine differentiation markers

**IHC markers of neuroendocrine differentiation:**
- **Chromogranin A (CgA):** Secreted from dense-core granules; elevated serum CgA in ~70-90% of functioning NETs; serum marker for monitoring; false positive with PPIs (chromogranin production is pH-sensitive); IHC positivity in >90% of well-differentiated NETs
- **Synaptophysin:** Presynaptic vesicle membrane protein; IHC positive in >95% of well-differentiated NETs; more sensitive than CgA for poorly differentiated NEC
- **Insulinoma-associated protein 1 (INSM1):** Nuclear transcription factor; highly specific neuroendocrine marker; positive in NET, NEC, SCLC, Merkel cell carcinoma; negative in adenocarcinoma
- **SSTR2A (IHC):** Semi-quantitative SSTR2 expression; Volante/Papotti scoring (0-3+); correlates with DOTATATE PET avidity; used for PRRT patient selection when PET not available
- **Ki-67 (MIB-1 antibody):** Proliferative index; defines WHO grade; counted in 500 cells in hotspot; critical for G1/G2/G3 classification

**Site-specific markers:**
- Midgut carcinoid: Serotonin-positive; CDX2+ (intestinal origin); SSTR2+ high
- pNET: Islet-specific markers — insulin (insulinoma), gastrin (gastrinoma), glucagon (glucagonoma), pancreatic polypeptide (PP-oma), VIP (VIPoma), somatostatin (somatostatinoma); non-functioning pNET: may be chromogranin+/synaptophysin+ without hormonal syndrome
- Lung carcinoid: TTF-1+/- (atypical carcinoid more often TTF-1+); CK7+; SSTR2/5+ (typical > atypical); DLL3 (Delta-like ligand 3) overexpression in both carcinoid and SCLC

**Molecular alterations:**
- pNET-specific: MEN1 mutations (~44%; menin → H3K4me3 loss → growth suppression); DAXX/ATRX mutations (~25% each; alternative lengthening of telomeres, ALT phenotype; poorer prognosis in pNET); VHL mutations; SETD2; mTOR pathway (TSC2, PIK3CA, PTEN) in ~15%
- Midgut carcinoid: CDKN1B (p27) mutations ~8%; MEN1/DAXX/ATRX less common; SSTR2 high; very stable genome; YY1 and EGLN1 mutations
- MEN1 syndrome (germline MEN1 mutation): Parathyroid adenoma, pituitary adenoma, pNET; pNETs in MEN1 are often multifocal, non-functioning; surveillance + surgery for functional tumors or >2 cm non-functional
- VHL syndrome: Somatostatinoma in duodenum (periampullary); pNET (non-functional, often); clear cell RCC

### Functioning syndrome pathophysiology

**Carcinoid syndrome:**
From serotonin, substance P, bradykinin, histamine secreted by midgut NETs with liver metastases (liver fails to inactivate serotonin that bypasses portal filtration in liver mets): Flushing (episodic, triggered by food/alcohol/stress), secretory diarrhea (watery, frequent), bronchospasm, carcinoid heart disease (right-sided valvular lesions from serotonin exposure to right heart = tricuspid regurgitation + pulmonary stenosis; Hedinger syndrome). Urinary 5-HIAA (24-hour urine): Elevated in ~70-85% of carcinoid syndrome patients. Treatment: SSA (octreotide/lanreotide) as backbone; telotristat ethyl (tryptophan hydroxylase-1 inhibitor, reduces serotonin synthesis, FDA 2017) for carcinoid diarrhea refractory to SSA.

**Insulinoma:**
Most common functioning pNET; unregulated insulin secretion → hypoglycemia; Whipple's triad: symptoms of hypoglycemia, glucose <45 mg/dL, relief with glucose; 90-95% benign single adenoma (<2 cm); 72-hour fast → insulin, C-peptide, proinsulin, glucose; CT/MRI/EUS for localization (small, vascular); surgical enucleation curative; diazoxide (Kfᴷ opener → reduces insulin secretion) for unresectable.

**Gastrinoma (Zollinger-Ellison Syndrome):**
Gastrin-secreting tumor → hypergastrinemia → excessive HCl → multiple peptic ulcers, refractory GERD, diarrhea; ~25% in MEN1; ~60% in pancreas (duodenal more common in sporadic); secretin stimulation test → gastrin spike (paradoxical); PPI therapy controls acid secretion; surgery for sporadic gastrinoma; somatostatin analogs reduce gastrin in ~50%.

## Function

### GEP-NET natural history and staging

**ENETS/AJCC staging (TNM, site-specific):**
Midgut and other NET: T1-T4 by tumor size and invasion; N0/N1 by regional nodal status; M0/M1a (liver only) / M1b (extrahepatic) / M1c (diffuse metastatic). Functional staging by Ki-67 grade. Prognosis: G1 midgut NET with liver mets → 10-year OS ~30-50% (slow-growing); G3 NET or NEC → 1-year OS <50%.

**Chromogranin A monitoring:**
Serum CgA correlates with tumor burden in most GEP-NETs; useful for monitoring response to therapy or progression; CgA doubling time predicts outcomes. PPI-induced hypergastrinemia → ECL cell hyperplasia → CgA elevation (false positive); hold PPI ≥2 weeks before CgA measurement.

## Pathology

### Diagnosis and imaging

**Biochemical diagnosis:**
- Carcinoid syndrome: 24-hour urine 5-HIAA (serotonin metabolite) + serum serotonin
- Insulinoma: 72-hour fast (glucose, insulin, C-peptide, proinsulin, β-hydroxybutyrate)
- Gastrinoma: Fasting serum gastrin; secretin stimulation test (>200 pg/mL increase = positive)
- Glucagonoma: Elevated fasting glucagon (>500 pg/mL); characteristic rash
- VIPoma: Watery diarrhea + hypokalemia + achlorhydria (WDHA/Verner-Morrison); elevated VIP

**Functional imaging:**
- **68Ga-DOTATATE PET/CT (preferred):** Sensitivity ~94-96% for SSTR2+ lesions; superior to conventional CT/MRI for lymph node and peritoneal deposits; replaces OctreoScan (99mTc-HYNIC-TOC) in most centers
- **FDG PET:** Useful for G3/NEC (high Ki-67, high glycolytic activity) where DOTATATE uptake is low; "flip-flop" pattern: high DOTATATE/low FDG = G1-G2; high FDG/low DOTATATE = G3/NEC
- **68Ga-DOTANOC:** Binds SSTR2, SSTR3, SSTR5; broader coverage than DOTATATE; preferred in some European centers

### Treatment algorithms

**Localized resectable disease:**
Curative-intent surgery for all localized NETs; appendix NETs <2 cm → appendectomy sufficient; pNET <2 cm, non-functioning: watchful waiting vs. surveillance (indolent biology); cytoreductive surgery ("debulking") in selected patients with liver-dominant metastatic NET for symptom control and potential survival benefit.

**Metastatic GEP-NET — systemic treatment sequence:**
1. **SSA antiproliferative (first-line, SSTR2+ G1/G2):** Octreotide LAR 30 mg q28d or lanreotide 120 mg q28d; PROMID (midgut) and CLARINET (GEP-NET) trials; telotristat for carcinoid diarrhea add-on
2. **177Lu-DOTATATE PRRT (progressive SSTR2+ NET):** NETTER-1 (midgut); also used off-label in pNET and other SSTR2+ sites; 4 cycles q8-12 weeks; requires adequate kidney function (GFR >40); after PRRT, SSA maintenance
3. **Everolimus (mTOR inhibitor):** RADIANT-3 (pNET) [^yao-2011-radiant3], RADIANT-4 (non-functional GEP/lung NET); well-tolerated orally; stomatitis, fatigue, hyperglycemia, pneumonitis toxicities
4. **Sunitinib (pNET only):** [^raymond-2011-sunitinib-pnet] 37.5 mg/day continuous; approved specifically for pNET; VEGFR/PDGFR inhibitor; hypertension, fatigue, hand-foot syndrome
5. **Chemotherapy (pNET, G3, NEC):** Streptozocin + doxorubicin (classic pNET); temozolomide + capecitabine (TEMCAP: ORR ~70% in MGMT-methylated pNET); cisplatin + etoposide (platinum-etoposide for NEC); FOLFOX/FOLFIRI for intermediate G3
6. **Hepatic-directed therapy (liver-dominant mets):** Bland embolization, TACE, SIRT (Y-90 radioembolization, SIRFLOX/TELESTAR data); ablation (RFA, MWA) for oligometastatic disease

**Poorly differentiated NEC:**
Treatment identical to SCLC: cisplatin (or carboplatin) + etoposide (4-6 cycles); ORR ~40-60% but brief duration (~6-8 months); atezolizumab + carboplatin/etoposide (IMpower133 extrapolation) used in some centers; no established immunotherapy approval specifically for extrapulmonary NEC; NTRK fusion (rare) → larotrectinib.

**Peptide receptor radionuclide therapy (PRRT) eligibility:**
- SSTR2+ (68Ga-DOTATATE PET: Krenning score ≥3, i.e., uptake ≥ liver uptake intensity)
- Well-differentiated G1/G2 (or selected G3 NET with SSTR2 retention)
- Adequate renal function (GFR >40 mL/min); adequate bone marrow (no extensive bone metastases)
- Progressive disease (typically after/concurrent with SSA)
- Dosimetry individualized; amino acid renal protection protocol

## Connections

- `connects-to` → **[SSTR2](../../03-molecular/sstr2/README.md)** — SSTR2 overexpression in well-differentiated NETs enables SSA therapy (octreotide/lanreotide; PROMID/CLARINET antiproliferative trials) and 177Lu-DOTATATE PRRT (NETTER-1: 14-month PFS benefit); DOTATATE PET/CT confirms SSTR2 expression for PRRT eligibility.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Everolimus (RADIANT-3: PFS 11.0 vs 4.6 months in pNET; RADIANT-4: PFS 11.0 vs 3.9 months in non-functional NET) is approved for progressive/metastatic NET; mTOR inhibition reduces HIF-1α, VEGF, and cell cycle progression; resistance via AKT rebound.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Sunitinib (VEGFR1/2/3/PDGFRA/B; A6181111 trial: PFS 11.4 vs 5.5 months) is approved for pancreatic NET; NETs are hypervascular tumors with high VEGF expression; bevacizumab studied in midgut NET; cabozantinib (VEGFR2+MET) under investigation.
- `connects-to` → **[Glucagon](../../03-molecular/glucagon/README.md)** — Functioning pNETs include glucagonoma (necrolytic migratory erythema, diabetes), insulinoma (most common pNET), gastrinoma (Zollinger-Ellison), and VIPoma; SSTR2 agonists (octreotide) control glucagonoma and other secretory syndromes via α-cell glucagon inhibition.
- `connects-to` → **[MEN1 Syndrome](../men1-syndrome/README.md)** — Germline MEN1 mutations underlie ~10% of pancreatic NETs, which in MEN1 are typically multifocal and non-functioning alongside parathyroid and pituitary tumors; menin loss (H3K4me3 at target promoters) is also the most common somatic event (~44%) in sporadic pNET.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Midgut carcinoids secrete serotonin that, once liver metastases bypass portal clearance, causes carcinoid syndrome — flushing, secretory diarrhea, and carcinoid heart disease; urinary 5-HIAA tracks it and telotristat (a tryptophan hydroxylase inhibitor) curbs refractory diarrhea.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — The pancreas is a leading NET site: functioning pNETs (insulinoma, gastrinoma, glucagonoma, VIPoma) cause hormone syndromes while non-functioning pNETs grow silently; everolimus and sunitinib are pNET-specific approvals, and DAXX/ATRX-mutant pNETs use the ALT telomere pathway.
- `connects-to` → **[Neuroblastoma](../neuroblastoma/README.md)** — Neuroendocrine tumors and neuroblastoma are both neural-crest-derived, amine-handling cancers at opposite ends of age and behavior: NETs are well-differentiated, slow-growing adult tumors, while neuroblastoma is an aggressive MYCN-driven embryonal cancer of children.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — The small intestine (midgut) is a classic NET site: serotonin-secreting enterochromaffin-cell tumors of the ileum grow slowly but metastasize to the liver, producing carcinoid syndrome (flushing, diarrhea, carcinoid heart disease) and are SSTR2-positive.
- `connects-to` → **[MEN4 Syndrome](../men4-syndrome/README.md)** — MEN4, like MEN1, is a hereditary cause of neuroendocrine tumors: germline CDKN1B/p27 loss predisposes to pancreatic NETs alongside parathyroid and pituitary tumors, so a young or multifocal NET prompts germline MEN1 and CDKN1B testing for syndromic disease.
- `connects-to` → **[Pheochromocytoma/Paraganglioma](../pheochromocytoma-paraganglioma/README.md)** — Pheochromocytoma/paraganglioma are neuroendocrine tumors of the adrenal medulla and sympathetic ganglia: like other NETs they express somatostatin receptors (enabling DOTATATE imaging and PRRT) but uniquely secrete catecholamines, causing paroxysmal hypertension.
- `connects-to` → **[VHL Disease](../vhl-disease/README.md)** — VHL disease is a major hereditary cause of neuroendocrine tumors: germline VHL loss predisposes to pancreatic neuroendocrine tumors and pheochromocytomas alongside its hemangioblastomas and clear-cell RCC, so a young patient with a panNET warrants VHL and MEN1 testing.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver dictates carcinoid syndrome in neuroendocrine tumors: a midgut NET's serotonin is normally cleared by hepatic first-pass, so flushing and diarrhea appear only once liver metastases dump vasoactive amines directly into the systemic circulation.
- `connects-to` → **[Small Cell Lung Cancer](../sclc/README.md)** — Neuroendocrine tumors and small-cell lung cancer are the two ends of the neuroendocrine spectrum: well-differentiated NETs are indolent, while SCLC is a poorly differentiated, high-grade neuroendocrine carcinoma that grows explosively—same lineage, opposite tempo.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Insulinoma is the prototypical functional neuroendocrine tumor: a pancreatic-islet NET that autonomously secretes insulin, causing fasting hypoglycemia (Whipple's triad)—it shows how NETs are classified and treated by the hormone they produce.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lung is a major site of neuroendocrine tumors: from indolent typical bronchial carcinoids through atypical carcinoids to high-grade small-cell neuroendocrine carcinoma, all arising from pulmonary neuroendocrine cells—'lung NET' spans benign to lethal.

[^yao-2011-radiant3]: Yao JC, Shah MH, Ito T, et al. Everolimus for advanced pancreatic neuroendocrine tumors. *N Engl J Med.* 2011;364(6):514-523. [doi:10.1056/NEJMoa1009290](https://doi.org/10.1056/NEJMoa1009290) · [PubMed 21306237](https://pubmed.ncbi.nlm.nih.gov/21306237/)
[^raymond-2011-sunitinib-pnet]: Raymond E, Dahan L, Raoul JL, et al. Sunitinib malate for the treatment of pancreatic neuroendocrine tumors. *N Engl J Med.* 2011;364(6):501-513. [doi:10.1056/NEJMoa1003825](https://doi.org/10.1056/NEJMoa1003825) · [PubMed 21306236](https://pubmed.ncbi.nlm.nih.gov/21306236/)

---
schema: human-scale-entry/v1
id: hereditary-breast-ovarian-cancer
name: Hereditary Breast and Ovarian Cancer
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Hereditary breast and ovarian cancer syndrome (HBOC) is caused by germline BRCA1/2, PALB2, ATM, or CHEK2 variants; BRCA1 lifetime breast risk ~70%, ovarian ~44%; PARP inhibitors approved across cancer types; risk-reducing surgery (mastectomy/BSO) is standard."
aliases: ["HBOC", "hereditary breast and ovarian cancer", "BRCA syndrome", "BRCA1 BRCA2 syndrome", "hereditary breast cancer", "germline BRCA", "HBOC syndrome", "BRCA1 germline", "familial breast cancer"]
sources:
  - id: kuchenbaecker-2017-brca-risks
    type: peer-reviewed
    cite: "Kuchenbaecker KB, Hopper JL, Barnes DR, et al. Risks of Breast, Ovarian, and Contralateral Breast Cancer for BRCA1 and BRCA2 Mutation Carriers. JAMA. 2017;317(23):2402-2416."
    doi: "10.1001/jama.2017.7112"
    pmid: "28632853"
    url: "https://doi.org/10.1001/jama.2017.7112"
  - id: antoniou-2014-palb2-risk
    type: peer-reviewed
    cite: "Antoniou AC, Casadei S, Heikkinen T, et al. Breast-cancer risk in families with mutations in PALB2. N Engl J Med. 2014;371(6):497-506."
    doi: "10.1056/NEJMoa1400382"
    pmid: "25099575"
    url: "https://doi.org/10.1056/NEJMoa1400382"
cross_links:
  - target: 01-human/03-molecular/palb2
    relation: connects-to
    note: "Germline PALB2 pathogenic variants confer ~35-65% lifetime breast cancer risk (second after BRCA1/2); ~5-10% ovarian cancer risk (primarily HGSOC); biallelic PALB2 = Fanconi anemia FA-N; PARP inhibitors are active in PALB2-germline breast and pancreatic cancer."
  - target: 01-human/03-molecular/brca1
    relation: connects-to
    note: "BRCA1 germline variants confer the highest hereditary breast cancer risk (~55-72% lifetime) and ovarian cancer risk (~44%); BRCA1-mutant tumors are often triple-negative (ER-/PR-/HER2-) and high-grade; risk-reducing BSO at age 35 and bilateral mastectomy are standard options."
  - target: 01-human/03-molecular/brca2
    relation: connects-to
    note: "BRCA2 germline variants confer ~45-69% lifetime breast cancer risk and ~17% ovarian cancer risk (lower than BRCA1); BRCA2-mutant breast cancer is often ER+/HER2-; olaparib and niraparib FDA-approved for BRCA-mutant metastatic breast cancer; risk-reducing BSO at age 40-45."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "HBOC-associated ovarian cancer is predominantly high-grade serous carcinoma (HGSOC); BRCA1 germline: 44% lifetime risk; BRCA2: 17%; PALB2/RAD51C/D: 5-10%; bilateral salpingo-oophorectomy (BSO) at age 35-40 reduces ovarian cancer mortality; PARP inhibitors in maintenance."
  - target: 01-human/03-molecular/atm
    relation: connects-to
    note: "Germline ATM pathogenic variants confer ~20-30% lifetime breast cancer risk; elevated prostate (~6%) and pancreatic risk; biallelic ATM = ataxia-telangiectasia; ATM-germline BC is often ER+/luminal; NCCN recommends breast MRI from age 40 for ATM heterozygotes with family history."
  - target: 01-human/03-molecular/rad51
    relation: connects-to
    note: "BRCA2 loads RAD51 monomers onto ssDNA at DSBs via eight BRC repeats → RAD51 filament → strand invasion (HR repair); BRCA2 LOF → RAD51 loading failure → error-prone NHEJ/MMEJ → tumorigenesis; RAD51 paralogs (RAD51C, RAD51D) each confer ~10-15% lifetime ovarian cancer risk in HBOC."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "HBOC causes ~5-10% of breast cancer; BRCA1-associated BC is predominantly TNBC (~60-80%) with peak onset at 30-40 years; BRCA2-associated BC is predominantly ER+ (~60-70%); olaparib (OlympiAD) and talazoparib (EMBRACA) are FDA-approved for germline BRCA1/2 HER2-neg metastatic BC."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "HBOC and Li-Fraumeni are the major hereditary breast cancer syndromes but differ in scope: HBOC (BRCA1/2) focuses on breast and ovarian cancer with PARP sensitivity, while LFS (germline TP53) spans sarcomas, brain tumors, and adrenocortical carcinoma — focused vs multi-cancer."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "BRCA2 (and to a lesser degree BRCA1, PALB2, ATM) raises pancreatic cancer risk ~3-7×, extending HBOC beyond breast and ovary; these HR-deficient pancreatic cancers respond to platinum and PARP-inhibitor maintenance (olaparib, POLO), so germline testing now guides therapy."
  - target: 01-human/07-system/prostate-cancer
    relation: connects-to
    note: "BRCA2 carriers face ~2-6× prostate cancer risk with more aggressive, earlier-onset disease; HBOC thus affects men too, and BRCA/HR-deficient metastatic prostate cancer responds to PARP inhibitors (olaparib, PROfound) — making germline and tumor testing standard in advanced cases."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "BRCA2 widens the hereditary breast-ovarian cancer spectrum to melanoma: germline BRCA2 modestly raises risk of cutaneous and especially uveal melanoma alongside breast, ovarian, pancreatic and prostate cancer, so a melanoma history can inform BRCA testing."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Hereditary breast-ovarian cancer strikes the reproductive system hardest: BRCA1/2 carriers face high lifetime risks of breast, ovarian and fallopian-tube cancer, so risk-reducing salpingo-oophorectomy and enhanced breast surveillance are cornerstones of management."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: treated-by
    note: "Hereditary breast-ovarian cancer is the paradigm for synthetic-lethal targeted therapy: BRCA1/2-mutant tumors cannot repair DNA by homologous recombination, so PARP inhibitors (olaparib) blocking backup repair selectively kill them—turning the germline defect into a drug target."
  - target: 01-human/07-system/lynch-syndrome
    relation: connects-to
    note: "HBOC and Lynch syndrome are major hereditary cancers raising women's ovarian/endometrial risk via different repair defects: HBOC from BRCA1/2 homologous-recombination loss, Lynch from mismatch-repair loss—each guides distinct screening and surgery."
  - target: 01-human/07-system/cowden-syndrome
    relation: connects-to
    note: "HBOC and Cowden syndrome both sharply raise hereditary breast cancer risk through different genes: HBOC via BRCA1/2 (homologous-recombination repair), Cowden via PTEN (PI3K-AKT pathway)—PTEN also brings thyroid and endometrial cancer plus hamartomas."
  - target: 01-human/07-system/peutz-jeghers-syndrome
    relation: connects-to
    note: "HBOC and Peutz-Jeghers both elevate breast cancer risk through different mechanisms: HBOC from BRCA1/2 DNA-repair loss, PJS from STK11 loss—PJS also raises ovarian (sex-cord) and GI cancer risk, so both warrant intensified breast surveillance from a young age."
---

# Hereditary Breast and Ovarian Cancer

## Overview

**Hereditary breast and ovarian cancer syndrome (HBOC)** is the most common hereditary cancer predisposition syndrome, caused by germline pathogenic variants in **BRCA1** or **BRCA2** (primarily) and in moderate-to-high risk genes including **PALB2**, **ATM**, **CHEK2**, **RAD51C**, and **RAD51D**. HBOC accounts for approximately **5-10% of all breast cancers** and **10-15% of all ovarian cancers**. The BRCA1 and BRCA2 proteins are core components of the homologous recombination (HR) DNA repair pathway; their loss creates HR deficiency (HRD), rendering cells reliant on error-prone repair — accumulating mutations and facilitating cancer initiation [^kuchenbaecker-2017-brca-risks] [^antoniou-2014-palb2-risk].

**HBOC gene risk stratification (2026 NCCN/ACMG framework):**

| Gene | Breast Ca lifetime risk | Ovarian Ca lifetime risk | Other elevated risks |
|---|---|---|---|
| BRCA1 | ~55-72% | ~44% | TNBC, premenopausal |
| BRCA2 | ~45-69% | ~17% | Pancreatic (~4%), prostate (~19% in males), male breast (~7%) |
| PALB2 | ~35-65% | ~5-10% | Pancreatic (~2-3%) |
| ATM (germline, biallelic = AT) | ~20-30% | Low | Prostate (~6%), pancreatic elevated |
| CHEK2 | ~15-25% | Low | CRC (~3%), prostate moderate |
| RAD51C | ~15-20% | ~10-15% | HGSOC subtype |
| RAD51D | ~15-20% | ~10-15% | HGSOC subtype |
| CDH1 (E-cadherin) | ~42% (lobular BC) | Low | Diffuse gastric cancer ~70% |
| PTEN (Cowden) | ~50% | Low | Thyroid, endometrial |

*Population breast cancer risk ~13% lifetime; ovarian risk ~2% lifetime.*

## Structure

### Genetic architecture

**BRCA1 (17q21.31):**
- 1863 aa, 220 kDa; RING domain (N-terminus; E3 ubiquitin ligase with BARD1), BRCT repeats (C-terminus; phosphoprotein binding after DNA damage: pSer1524-CtIP, pSer1387-BACH1, pSer178-ABRAXAS)
- Germline spectrum: ~1,650 pathogenic/likely pathogenic variants in ClinVar; frameshift (~40%), nonsense (~20%), large deletions (MLPA required, ~10%), missense (rare pathogenic); founder variants: 185delAG (Ashkenazi Jewish); 5382insC (Ashkenazi Jewish, Eastern European)
- De novo rate: ~1% of BRCA1 PV
- Penetrance modifiers: polygenic risk score (PRS), reproductive history, BMI, oral contraceptive use

**BRCA2 (13q12.3):**
- 3418 aa, 384 kDa; eight BRC repeats (bind RAD51 monomers); nuclear export signal (C-terminal); DNA-binding domain (OB-fold, tower domain)
- Germline spectrum: ~1,250 pathogenic variants; similar to BRCA1 (frameshift, nonsense, large deletions); founder variants: 6174delT (Ashkenazi Jewish); 999del5 (Icelandic/Celtic)
- BRCA2 germline also elevated in prostate cancer (HIGH risk: up to ~19-23% lifetime in BRCA2 vs ~12% population), pancreatic adenocarcinoma (~4% vs ~1.5%), cholangiocarcinoma
- Male BRCA2 carriers: elevated male breast cancer (~7% lifetime vs <0.1% population)

**Genetic testing landscape (2026):**
Multigene panel testing has largely replaced sequential BRCA1/2 testing; panels include BRCA1, BRCA2, PALB2, ATM, CHEK2, RAD51C, RAD51D, CDH1, PTEN, TP53, STK11, and up to 75+ genes depending on platform. Cascade testing (family members of identified carriers) is cost-effective and recommended.

### BRCA gene discovery

- BRCA1: Hall 1990 (linkage) → Miki 1994 (cloning, Science); BRCA2: Wooster 1995 (linkage) → Tavtigian 1996 (cloning, Nature Genetics)
- BRCA1/2 population prevalence: ~1 in 400 carry a BRCA1/2 pathogenic variant in general population; 1 in 40 in Ashkenazi Jewish population (due to three founder variants)

## Function

### HR pathway and BRCA proteins

Both BRCA1 and BRCA2 are required for the S/G2 phase homologous recombination repair of DSBs — the error-free, template-directed mechanism using a sister chromatid as repair template. Loss of HR → cells use error-prone non-homologous end joining (NHEJ) or microhomology-mediated end joining (MMEJ) → accumulation of structural variants, inversions, translocations → genomic instability → tumorigenesis.

**BRCA1 roles:**
- **DSB recognition and signaling**: BRCA1 localizes to DSBs via 53BP1 competition (ATM phosphorylates histone H2AX → MDC1 → BRCA1 recruited); BRCA1 promotes end resection (long-range resection) by antagonizing 53BP1-RIF1-Shieldin
- **Ubiquitin E3 ligase (RING-BARD1)**: ubiquitinates H2A at Lys127/129 → local chromatin remodeling at DSBs; also ubiquitinates RPB8 → stalled RNA Pol II degradation at DSBs (transcription-coupled repair)
- **Cell cycle checkpoint**: BRCA1 BRCT phosphopeptide-binding → BACH1/FANCJ helicase interaction → replication fork stability; ABRAXAS-RAP80 complex → BRCA1 retained at DSBs
- **Centrosome number**: BRCA1 localizes to centrosomes; BRCA1 LOF → supernumerary centrosomes → multipolar spindles → aneuploidy

**BRCA2 roles:**
- **RAD51 loader**: BRC repeats 1-8 each bind one RAD51 monomer → BRCA2 can load up to 8 RAD51 units at once; BRCA2 OB-fold also contacts ssDNA directly → positions RAD51 filament for optimal strand invasion
- **Replication fork protection**: BRCA2 stabilizes RAD51 on ssDNA at stalled forks → prevents MRE11 nuclease degradation of nascent DNA; fork protection is independent of DSB repair and requires distinct BRCA2 domains (Leu2647-Asp2803)
- **Meiosis**: BRCA2 regulates DMC1 (meiosis-specific RAD51 homolog) loading during meiotic HR; BRCA2 loss in mouse germline → meiotic failure → infertility

**Synthetic lethality basis for PARP inhibition:**

Normal cells: single-strand breaks → PARP1 binds SSB → poly-ADP ribose (PAR) chain → recruits XRCC1-DNA Pol β-LIG3 → base excision repair → SSB fixed (PARP released/recycled)

BRCA-mutant cells (HRD):
1. PARP inhibitor occupies PARP1 catalytic domain → prevents PAR synthesis AND traps PARP1 on DNA (PARP trapping; potency: talazoparib > niraparib > olaparib > rucaparib)
2. Trapped PARP1 on DNA → replication forks collide with trapped PARP1 → fork collapse → DSB
3. DSB repair requires HR (BRCA1/2-RAD51) — absent in BRCA-mutant cells → cell dies
4. Normal cells (HR-proficient): DSB repaired by HR → survival; selective toxicity to HRD cells

## Pathology

### Cancer subtypes in HBOC

**BRCA1-associated breast cancer:**
- Predominantly **triple-negative breast cancer (TNBC)** (~60-80% of BRCA1-associated invasive breast cancer)
- High grade (grade 3); high Ki-67; often medullary/pushing border histology
- Young age at onset (peak 30-40 years); bilateral risk ~40% at 10 years
- Chemotherapy: platinum agents (carboplatin) + taxane + immunotherapy (pembrolizumab, KEYNOTE-522 in TNBC regardless of germline status)
- PARP inhibitor: olaparib adjuvant (OlympiA trial: germline BRCA1/2, HER2-negative, residual disease after neoadjuvant; 4-year OS benefit 3.4%)

**BRCA2-associated breast cancer:**
- Predominantly **luminal (ER+/HER2-)**: ~60-70% ER-positive; less TNBC than BRCA1
- Higher grade than average ER+ BC; may behave like ER+ but with HRD features
- CDK4/6 inhibitors (palbociclib, ribociclib, abemaciclib) for ER+/HER2- metastatic disease (BRCA2 does not affect CDK4/6i sensitivity)
- PARP inhibitor: olaparib/talazoparib for germline BRCA1/2 HER2-negative metastatic breast cancer

**HBOC-associated ovarian cancer:**
- **High-grade serous carcinoma (HGSOC)**: the predominant histology in BRCA1/2/PALB2/RAD51C/D-associated OC; TP53 mutation is universal in HGSOC
- Clear cell carcinoma: NOT elevated in BRCA1/2 carriers (associated with ARID1A, PIK3CA, loss of MLH1)
- Mucinous: NOT elevated in BRCA1/2 carriers
- **BRCA1-associated OC**: onset age 40-50 (earlier than sporadic OC age 60-70)
- **BRCA2-associated OC**: onset age 50-60
- PARP inhibitor maintenance: olaparib (SOLO-1: germline BRCA1/2, first-line OC; OS benefit at 5 years, HR 0.55); niraparib (PRIMA: germline BRCA + HRD-positive sporadic); rucaparib (ARIEL3)
- Bevacizumab + chemotherapy → maintenance: GOG-0218, ICON7 (regardless of BRCA status)

### Risk management (NCCN 2024)

**Breast cancer surveillance:**
- Annual **breast MRI** (preferred) + **mammogram**: from age 25 (BRCA1/2); from age 30 (PALB2, ATM with fam history, CHEK2)
- Semi-annual clinical breast exam: every 6 months from age 25
- Risk-reducing bilateral mastectomy (BRM): reduces breast cancer risk by ~90-95%; does not eliminate completely (residual axillary tail/skin tissue); timing at patient's discretion after genetic counseling
- No role for tamoxifen chemoprevention in BRCA1 carriers (TNBC is ER-negative, tamoxifen not protective); tamoxifen reduces contralateral BC in BRCA2 carriers

**Ovarian cancer risk reduction:**
- **Bilateral salpingo-oophorectomy (BSO)**: most effective risk reduction
  - BRCA1 carriers: age 35-40 (after childbearing)
  - BRCA2 carriers: age 40-45 (later onset, more time; natural menopause may be acceptable in some)
  - PALB2, RAD51C/D: age 45-50 (lower risk)
- BSO also reduces breast cancer risk in premenopausal carriers (estrogen deprivation): ~50% reduction in BRCA1/2 (if done before age 40)
- Annual CA-125 + transvaginal ultrasound (TVU): low sensitivity for early OC detection (not recommended as primary surveillance); used in women who decline BSO

**Male BRCA2 carriers:**
- Breast self-exam monthly + annual clinical breast exam from age 35; mammogram annually from 40
- PSA + DRE from age 40 for prostate cancer surveillance
- Pancreatic cancer: MRI/MRCP + EUS every 1-2 years from age 50 (CAPS consortium guidelines) for BRCA2 + one affected relative

**Chemoprevention:**
- Oral contraceptive pills (OCP): reduce ovarian cancer risk by ~50% in BRCA1/2 carriers (any duration); possible slight increase in breast cancer risk with long-term use; net benefit for ovarian cancer prevention is generally accepted, especially in BRCA2
- Risk-benefit counseling: individualized; BSO is more protective than OCP alone

### PARP inhibitor clinical approvals (as of 2026)

| PARP inhibitor | Indication | Key trial |
|---|---|---|
| Olaparib (Lynparza) | gBRCA1/2 HER2-neg metastatic BC; gBRCA1/2 HGSOC 1L + maintenance + relapse; gBRCA1/2 mCRPC; gBRCA1/2 mPDAC maintenance | OlympiAD, OlympiA, SOLO-1/2, PROfound, POLO |
| Niraparib (Zejula) | HGSOC maintenance (HRD+/BRCA+); HER2-neg gBRCA1/2 metastatic BC | PRIMA, BRAVO |
| Rucaparib (Rubraca) | gBRCA1/2 HGSOC maintenance + relapse | ARIEL3 |
| Talazoparib (Talzenna) | gBRCA1/2 HER2-neg metastatic BC | EMBRACA |

## Connections

- `connects-to` → **[PALB2](../../03-molecular/palb2/README.md)** — Germline PALB2 pathogenic variants confer ~35-65% lifetime breast cancer risk (second after BRCA1/2); ~5-10% ovarian cancer risk (primarily HGSOC); biallelic PALB2 = Fanconi anemia FA-N; PARP inhibitors are active in PALB2-germline breast and pancreatic cancer.
- `connects-to` → **[BRCA1](../../03-molecular/brca1/README.md)** — BRCA1 germline variants confer the highest hereditary breast cancer risk (~55-72% lifetime) and ovarian cancer risk (~44%); BRCA1-mutant tumors are often triple-negative (ER-/PR-/HER2-) and high-grade; risk-reducing BSO at age 35 and bilateral mastectomy are standard options.
- `connects-to` → **[BRCA2](../../03-molecular/brca2/README.md)** — BRCA2 germline variants confer ~45-69% lifetime breast cancer risk and ~17% ovarian cancer risk (lower than BRCA1); BRCA2-mutant breast cancer is often ER+/HER2-; olaparib and niraparib FDA-approved for BRCA-mutant metastatic breast cancer; risk-reducing BSO at age 40-45.
- `connects-to` → **[Ovarian Cancer](../ovarian-cancer/README.md)** — HBOC-associated ovarian cancer is predominantly high-grade serous carcinoma (HGSOC); BRCA1 germline: 44% lifetime risk; BRCA2: 17%; PALB2/RAD51C/D: 5-10%; bilateral salpingo-oophorectomy (BSO) at age 35-40 reduces ovarian cancer mortality; PARP inhibitors in maintenance.
- `connects-to` → **[ATM](../../03-molecular/atm/README.md)** — Germline ATM pathogenic variants confer ~20-30% lifetime breast cancer risk; elevated prostate (~6%) and pancreatic risk; biallelic ATM = ataxia-telangiectasia; ATM-germline BC is often ER+/luminal; NCCN recommends breast MRI from age 40 for ATM heterozygotes with family history.
- `connects-to` → **[RAD51](../../03-molecular/rad51/README.md)** — BRCA2 loads RAD51 monomers onto ssDNA at DSBs via eight BRC repeats → RAD51 filament → strand invasion (HR repair); BRCA2 LOF → RAD51 loading failure → error-prone NHEJ/MMEJ → tumorigenesis; RAD51 paralogs (RAD51C, RAD51D) each confer ~10-15% lifetime ovarian cancer risk in HBOC.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — HBOC causes ~5-10% of breast cancer; BRCA1-associated BC is predominantly TNBC (~60-80%) with peak onset at 30-40 years; BRCA2-associated BC is predominantly ER+ (~60-70%); olaparib (OlympiAD) and talazoparib (EMBRACA) are FDA-approved for germline BRCA1/2 HER2-neg metastatic BC.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — HBOC and Li-Fraumeni are the major hereditary breast cancer syndromes but differ in scope: HBOC (BRCA1/2) focuses on breast and ovarian cancer with PARP sensitivity, while LFS (germline TP53) spans sarcomas, brain tumors, and adrenocortical carcinoma — focused vs multi-cancer.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — BRCA2 (and to a lesser degree BRCA1, PALB2, ATM) raises pancreatic cancer risk ~3-7×, extending HBOC beyond breast and ovary; these HR-deficient pancreatic cancers respond to platinum and PARP-inhibitor maintenance (olaparib, POLO), so germline testing now guides therapy.
- `connects-to` → **[Prostate Cancer](../prostate-cancer/README.md)** — BRCA2 carriers face ~2-6× prostate cancer risk with more aggressive, earlier-onset disease; HBOC thus affects men too, and BRCA/HR-deficient metastatic prostate cancer responds to PARP inhibitors (olaparib, PROfound) — making germline and tumor testing standard in advanced cases.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — BRCA2 widens the hereditary breast-ovarian cancer spectrum to melanoma: germline BRCA2 modestly raises risk of cutaneous and especially uveal melanoma alongside breast, ovarian, pancreatic and prostate cancer, so a melanoma history can inform BRCA testing.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Hereditary breast-ovarian cancer strikes the reproductive system hardest: BRCA1/2 carriers face high lifetime risks of breast, ovarian and fallopian-tube cancer, so risk-reducing salpingo-oophorectomy and enhanced breast surveillance are cornerstones of management.
- `treated-by` → **[Targeted Therapy](../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Hereditary breast-ovarian cancer is the paradigm for synthetic-lethal targeted therapy: BRCA1/2-mutant tumors cannot repair DNA by homologous recombination, so PARP inhibitors (olaparib) blocking backup repair selectively kill them—turning the germline defect into a drug target.
- `connects-to` → **[Lynch Syndrome](../lynch-syndrome/README.md)** — HBOC and Lynch syndrome are major hereditary cancers raising women's ovarian/endometrial risk via different repair defects: HBOC from BRCA1/2 homologous-recombination loss, Lynch from mismatch-repair loss—each guides distinct screening and surgery.
- `connects-to` → **[Cowden Syndrome](../cowden-syndrome/README.md)** — HBOC and Cowden syndrome both sharply raise hereditary breast cancer risk through different genes: HBOC via BRCA1/2 (homologous-recombination repair), Cowden via PTEN (PI3K-AKT pathway)—PTEN also brings thyroid and endometrial cancer plus hamartomas.
- `connects-to` → **[Peutz-Jeghers Syndrome](../peutz-jeghers-syndrome/README.md)** — HBOC and Peutz-Jeghers both elevate breast cancer risk through different mechanisms: HBOC from BRCA1/2 DNA-repair loss, PJS from STK11 loss—PJS also raises ovarian (sex-cord) and GI cancer risk, so both warrant intensified breast surveillance from a young age.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^kuchenbaecker-2017-brca-risks]: Kuchenbaecker KB, Hopper JL, Barnes DR, et al. Risks of Breast, Ovarian, and Contralateral Breast Cancer for BRCA1 and BRCA2 Mutation Carriers. *JAMA.* 2017;317(23):2402-2416. [doi:10.1001/jama.2017.7112](https://doi.org/10.1001/jama.2017.7112) · [PubMed 28632853](https://pubmed.ncbi.nlm.nih.gov/28632853/)
[^antoniou-2014-palb2-risk]: Antoniou AC, Casadei S, Heikkinen T, et al. Breast-cancer risk in families with mutations in PALB2. *N Engl J Med.* 2014;371(6):497-506. [doi:10.1056/NEJMoa1400382](https://doi.org/10.1056/NEJMoa1400382) · [PubMed 25099575](https://pubmed.ncbi.nlm.nih.gov/25099575/)

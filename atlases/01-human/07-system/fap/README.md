---
schema: human-scale-entry/v1
id: fap
name: Familial Adenomatous Polyposis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Familial adenomatous polyposis (FAP) is caused by germline APC mutations; >100 colorectal adenomas from age 10-20; CRC by 30-40 without treatment; prophylactic proctocolectomy is curative; desmoid tumor, duodenal adenomas, and Gardner syndrome are extracolonic features."
aliases: ["FAP", "familial adenomatous polyposis", "APC polyposis", "Gardner syndrome", "attenuated FAP", "AFAP", "FAP colon", "hereditary CRC APC", "APC syndrome", "FAP desmoid"]
sources:
  - id: kinzler-1991-apc
    type: peer-reviewed
    cite: "Kinzler KW, Nilbert MC, Su LK, et al. Identification of FAP locus genes from chromosome 5q21. Science. 1991;253(5020):661-665."
    doi: "10.1126/science.1651562"
    pmid: "1651562"
    url: "https://doi.org/10.1126/science.1651562"
  - id: fearon-1990-vogelstein
    type: peer-reviewed
    cite: "Fearon ER, Vogelstein B. A genetic model for colorectal tumorigenesis. Cell. 1990;61(5):759-767."
    doi: "10.1016/0092-8674(90)90186-i"
    pmid: "2188735"
    url: "https://doi.org/10.1016/0092-8674(90)90186-i"
cross_links:
  - target: 01-human/03-molecular/apc
    relation: connects-to
    note: "Germline APC truncating mutations cause FAP; codon position determines phenotype: codons 1250-1464 = classic profuse FAP; codons 1310-2011 = mesenteric desmoid risk; codons <168 or >1580 = attenuated FAP; codon 1309 hotspot = most severe; nuclear β-catenin in FAP adenomas"
  - target: 01-human/03-molecular/ctnnb1
    relation: connects-to
    note: "APC LOF → insufficient β-catenin destruction complex → nuclear β-catenin → TCF/LEF → Wnt-ON; FAP tumors show nuclear β-catenin by IHC; FAP desmoid (APC codons 1310-2011) driven by APC LOF, not CTNNB1 mutation; functionally equivalent outcome via distinct mechanisms"
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "FAP: 100% CRC penetrance by age 40 without colectomy; proctocolectomy (IPAA or ileostomy) is definitive prevention; annual colonoscopy from age 10-12; celecoxib FDA-approved for FAP adenoma reduction; sulindac reduces polyp burden; duodenal surveillance required"
  - target: 01-human/07-system/desmoid-tumor
    relation: connects-to
    note: "APC germline mutations (codons 1310-2011) → FAP-associated mesenteric desmoid; more aggressive than sporadic CTNNB1-mutant desmoid; post-colectomy FAP mesenteric desmoid is a leading mortality cause in FAP; nirogacestat FDA-approved for all desmoid including FAP-associated"
  - target: 01-human/07-system/mutyh-associated-polyposis
    relation: connects-to
    note: "Biallelic MUTYH mutations cause an autosomal-recessive phenocopy of attenuated FAP (10-100 adenomas) with no germline APC mutation; defective 8-oxoG base-excision repair drives G:C→T:A transversions in APC and KRAS; ~30% of APC-negative AFAP is actually MAP."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "KRAS activating mutations (G12D/V, ~50% of large FAP adenomas) are a key step in the Fearon-Vogelstein adenoma-carcinoma sequence after biallelic APC loss; the same APC→KRAS→SMAD4→TP53 progression as sporadic CRC, but compressed and universal because APC LOF is pre-present."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "FAP carpets the colorectal mucosa with hundreds-to-thousands of adenomas; every colonocyte carries the germline APC first hit, so independent somatic second hits seed many foci; prophylactic proctocolectomy removes the at-risk mucosa and is curative for colorectal risk."
  - target: 01-human/07-system/hereditary-diffuse-gastric-cancer
    relation: connects-to
    note: "FAP and hereditary diffuse gastric cancer are both dominant GI cancer syndromes but opposite in lesion: FAP carpets the colon with thousands of APC-driven adenomas, while HDGC seeds the stomach with CDH1-driven signet-ring foci that never form polyps — adenomatous versus diffuse."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "After colectomy the duodenum becomes FAP's most dangerous site: duodenal and ampullary adenomas (Spigelman-staged) progress to cancer in 3-5% and are the leading cause of cancer death in FAP, mandating lifelong upper-GI surveillance and sometimes pancreas-sparing duodenectomy."
  - target: 01-human/07-system/thyroid-cancer
    relation: connects-to
    note: "FAP confers a distinctive thyroid risk: cribriform-morular thyroid carcinoma, a rare papillary variant occurring almost exclusively in young women with FAP, can be the presenting sign of an undiagnosed APC mutation — prompting colonoscopy and germline testing when it appears."
  - target: 01-human/07-system/juvenile-polyposis-syndrome
    relation: connects-to
    note: "FAP and juvenile polyposis are both autosomal-dominant polyposis syndromes with high colorectal-cancer risk but differ in polyp biology: FAP carpets the colon with adenomas (APC/Wnt), while JPS makes fewer hamartomatous polyps (SMAD4/BMPR1A)—both need surveillance, often surgery."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "FAP affects the upper GI tract, not just the colon: nearly all patients develop fundic gland polyps and duodenal/ampullary adenomas, and gastric-cancer risk is raised, so after colectomy upper endoscopic surveillance of the stomach and duodenum becomes the priority."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "FAP is a disease of the intestinal epithelium's stem cells: germline APC loss removes the brake on Wnt/β-catenin in colonic crypt stem cells, so the entire epithelium is primed to form adenomas—hundreds to thousands—making the field, not a single clone, the cancer-prone tissue."
  - target: 01-human/07-system/lynch-syndrome
    relation: connects-to
    note: "FAP and Lynch syndrome are the major hereditary colorectal cancer syndromes but opposite: FAP floods the colon with hundreds of adenomatous polyps via APC loss, while Lynch causes few polyps but mismatch-repair failure—polyposis versus microsatellite instability."
  - target: 01-human/07-system/peutz-jeghers-syndrome
    relation: connects-to
    note: "FAP and Peutz-Jeghers are both inherited GI polyposis conditions but differ in polyp type and gene: FAP's APC loss yields hundreds of adenomas, while PJS's STK11 loss gives hamartomatous polyps and mucocutaneous pigmentation—different polyps, different cancer risks."
  - target: 01-human/07-system/medulloblastoma
    relation: connects-to
    note: "FAP can include brain tumors as Turcot syndrome: the same germline APC mutation that drives colonic polyposis also raises risk of medulloblastoma, linking Wnt-pathway dysregulation in gut and cerebellum—one mutated gene producing tumors in two very different organs."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "FAP is the textbook Wnt-pathway cancer syndrome: germline APC loss removes the brake on beta-catenin, so constitutive Wnt signaling drives the hundreds of colonic adenomas—mechanistically the same pathway activated somatically in most sporadic colorectal cancers."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "The stomach is an extracolonic FAP target: patients develop numerous fundic gland polyps and have raised gastric and duodenal cancer risk, so surveillance endoscopy of the upper GI tract complements colectomy in managing the syndrome."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "FAP raises the risk of pancreatic and other extracolonic cancers: APC loss predisposes beyond the colon to duodenal, pancreatic, thyroid and hepatoblastoma tumors—so even after prophylactic colectomy, FAP patients need broader cancer surveillance."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "FAP carpets the digestive tract with polyps: APC loss seeds hundreds to thousands of colonic adenomas that inevitably progress to colorectal cancer without colectomy, plus duodenal and gastric polyps—so FAP is a whole-gut polyposis, not just a colon disease."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "A retinal sign helps flag FAP: congenital hypertrophy of the retinal pigment epithelium (CHRPE) appears as pigmented fundus patches in many families, so an eye exam can provide an early, noninvasive clue to the APC mutation before polyps are found."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "FAP's Gardner variant shows in skin and bone: APC loss produces epidermoid cysts, fibromas and osteomas (especially of the jaw and skull), so these extraintestinal lumps of the integumentary and skeletal system can be the first visible sign of the syndrome."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "FAP raises childhood hepatoblastoma risk: young children with an APC mutation have a markedly increased chance of this liver cancer, so some families screen infants with abdominal ultrasound and AFP before the colonic polyps even appear."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "FAP overlaps brain tumors in Turcot syndrome: an APC mutation predisposes to medulloblastoma and other CNS tumors, so the colon and brain share a Wnt-pathway driver—linking a bowel polyposis syndrome to childhood brain cancer."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "FAP's Gardner variant is a fibroblast disease too: APC loss drives fibroblasts to form desmoid tumors, Gardner fibromas, and excess scar, so the same Wnt activation that carpets the colon also makes connective tissue overgrow."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "FAP grows bony osteomas as a Gardner feature: APC loss spurs osteoblasts to build benign bone tumors in the jaw and skull, an extracolonic clue that—with skin cysts and dental anomalies—can flag the syndrome before colon polyps declare themselves."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "FAP's polyps grow because APC loss unleashes MYC: with APC gone, β-catenin piles up and switches on MYC, the master proliferation gene, so every adenoma is driven by the Wnt-to-MYC signal that turns normal colon lining into a carpet of polyps."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "FAP tumors are immunologically cold: unlike the mismatch-repair-deficient cancers of Lynch syndrome, APC-driven colorectal cancers are microsatellite-stable with few neoantigens, so they respond poorly to the checkpoint immunotherapy that helps Lynch tumors."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "FAP reaches the skin in its Gardner variant: beyond the colon, APC loss spawns epidermoid cysts, lipomas, fibromas and bony osteomas, so skin and jaw lumps can be the first visible clue to the syndrome."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "FAP polyps recruit blood vessels via VEGF: as adenomas grow they drive VEGF-fueled angiogenesis, part of why COX-2 inhibitors—which lower this signaling—reduce polyp burden as chemoprevention in the syndrome."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages populate the stroma of FAP's polyps: drawn into the adenomas, tumor-associated macrophages secrete growth and inflammatory factors that help the APC-driven lesions progress toward colorectal cancer."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "FAP's polyps bleed away iron: hundreds of colonic adenomas ooze blood, so chronic loss drains the body's iron into a deficiency anemia that can be an early clue before cancer develops."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "FAP extends cancer risk to the pancreas: beyond the colon, the APC defect raises the chance of duodenal, periampullary, and pancreatic tumors, so surveillance reaches the upper GI tract too."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "FAP's adenomas summon endothelial cells: VEGF from the growing polyps drives these vessel-lining cells to build blood supply, which is why COX-2 inhibitors that curb this angiogenesis shrink polyp burden."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "FAP is policed by light: lifelong colonoscopy hunts the polyps, and a dilated eye exam spots CHRPE—the dark retinal patches that mark the syndrome—both relying on visible-light viewing."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "FAP's desmoid tumors are fibrosis run amok: APC loss lets fibroblasts build invasive fibrous masses, the desmoids that become a leading cause of death once the colon is removed."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "FAP raises thyroid cancer risk: a distinctive cribriform-morular papillary thyroid carcinoma occurs especially in young women with the syndrome, so thyroid screening is advised."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reads FAP's two telltale lesions: the dysplastic glands of its countless colonic adenomas, and the pigment-stuffed cells of CHRPE, the dark retinal patches that flag the syndrome at an eye exam."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "In the Gardner variant, FAP grows bone: benign osteomas sprout from the jaw and skull, bony overgrowths of the marrow-bearing facial bones that, with skin cysts, can betray the syndrome before the gut polyps do."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "FAP's osteomas are built of calcium: the Gardner-syndrome bony tumors lay down dense calcium-phosphate mineral, hard masses on the skull and jaw visible as bright opacities on imaging."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Gardner syndrome marks the skeleton and teeth: FAP's variant grows osteomas on the jaw and skull and brings dental anomalies — supernumerary teeth and odontomas — extracolonic clues that can predate the bowel polyps."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "The Turcot variant ties FAP to the brain: alongside its colonic polyps it predisposes to CNS tumors, classically medulloblastoma, so neurological symptoms can be part of the syndrome's reach."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "FAP quietly enlarges the adrenals: benign adrenal adenomas are more common than in the general population, usually silent incidentalomas found on the imaging done to track the syndrome's other tumors."
---

# Familial Adenomatous Polyposis

## Overview

**Familial adenomatous polyposis (FAP)** is an autosomal dominant colorectal cancer predisposition syndrome caused by germline pathogenic variants in **APC** (adenomatous polyposis coli), a scaffold for the β-catenin destruction complex. FAP is characterized by the development of hundreds to thousands of colorectal adenomas beginning in adolescence, with a 100% lifetime risk of colorectal carcinoma (CRC) by the 4th-5th decade of life if the colon is not removed. In addition to colorectal polyps, FAP patients develop characteristic extracolonic manifestations: **desmoid tumors** (especially mesenteric, post-colectomy), **duodenal and periampullary adenomas** (lifetime cancer risk ~5-10%), **fundic gland polyps**, **congenital hypertrophy of the retinal pigment epithelium (CHRPE)**, and the classic **Gardner syndrome** triad (colorectal polyps + osteomas + soft tissue tumors). FAP accounts for ~1% of all CRC in Western countries. Prophylactic proctocolectomy is the definitive intervention, and endoscopic surveillance + celecoxib chemoprevention are used to manage residual rectal or duodenal adenoma burden [^kinzler-1991-apc] [^fearon-1990-vogelstein].

**Epidemiology:**
- Prevalence: 1/10,000-30,000 in Western populations; ~15,000-20,000 patients in the USA
- Inheritance: autosomal dominant; 50% transmission; ~25-30% de novo (no family history)
- APC germline variant: ~100% of classic FAP; ~70% of attenuated FAP (AFAP); ~30% of AFAP are MUTYH-associated polyposis (MAP), biallelic MUTYH mutations — autosomal recessive
- Classic FAP: typically >100 adenomas, carpeting colorectum
- Attenuated FAP (AFAP): 10-99 adenomas; later onset (age 30-40); more distal colon; APC mutations at 5' end (<168), 3' end (>1580), or exon 9

**APC mutation-phenotype correlations:**

| APC codon region | Phenotype | CRC onset | Desmoid |
|---|---|---|---|
| <168 | AFAP (few polyps, late onset) | 50-60 yrs | Rare |
| 168-1250 | Classic FAP | 30-40 yrs | Uncommon |
| 1250-1464 (MCR) | Profuse classic FAP | 20-30 yrs | Uncommon |
| 1310-2011 | Classic + desmoid risk | 30-40 yrs | High (~50%) |
| 1309 (hotspot) | Most severe FAP | 20s | Uncommon |
| >1580 | AFAP (3' attenuated) | 50-60 yrs | Rare |

## Structure

### APC and the β-catenin destruction complex in FAP

**Molecular basis:**
APC protein scaffolds the β-catenin destruction complex (APC + AXIN + GSK-3β + CK1α): sequential phosphorylation of β-catenin at S45 (CK1α) → T41/S37/S33 (GSK-3β) → β-TrCP E3 ligase → proteasomal degradation → Wnt-OFF; germline APC pathogenic variant (truncating) → one allele non-functional at birth → somatic second hit (LOH at 5q21 or somatic truncating mutation) in a single colonocyte → biallelic APC LOF → β-catenin accumulates → nuclear → TCF/LEF → MYC, CCND1, VEGFA → stem cell expansion → adenoma

**From one cell to thousands of polyps:**
In FAP, every colonocyte carries the germline APC first hit; over time, independent somatic second-hit events in separate stem cells → multiple simultaneous adenoma foci; because millions of colonocytes are at risk, FAP patients develop hundreds to thousands of adenomas rather than the 1-5 sporadic adenomas a normal individual accumulates over a lifetime; polyp density is proportional to the residual APC protein function (truncation site determines how many β-catenin binding 20 aa repeats are retained)

**Adenoma-to-carcinoma sequence in FAP:**
Within FAP adenomas, additional mutations accumulate: KRAS (G12D/V, ~50% of large adenomas) → SMAD4 LOF → TP53 LOF → CRC; the sequence is the same as sporadic CRC (Fearon-Vogelstein model) but the timeline is compressed and universal because the initiating APC LOF is pre-present; FAP CRC typically arises from one of the most dysplastic adenomas (often >1 cm, villous features, high-grade dysplasia)

### MUTYH-associated polyposis (MAP)

**MAP genetics and phenotype:**
- Biallelic pathogenic variants in MUTYH (MutY DNA glycosylase; base excision repair): autosomal recessive
- MUTYH removes adenine mispaired with 8-oxoguanine (oxidative DNA damage) → prevents G:C → T:A transversions
- Biallelic MUTYH LOF → accumulation of G:C → T:A mutations → accumulates KRAS G12C/D and APC codon 1309 mutations → adenoma formation without germline APC mutation
- Phenotype: 10-100 adenomas (AFAP-like); CRC lifetime risk ~80%; onset slightly later than classic FAP
- Molecular signature: characteristic APC somatic mutations (APC codon 1369, 1450 missense/nonsense from G:C→T:A transversions) + KRAS G12C (G:C→T:A)
- IHC/testing: MUTYH germline sequencing for biallelic testing; both copies must be mutated (compound heterozygous or homozygous); heterozygous MUTYH carriers: minor CRC risk increase (~1.5-2×)

## Function

### Carcinogenesis in FAP

**Polyp development timeline:**
- Age 10-15: microscopic adenomas detectable by high-resolution colonoscopy; CHRPE (CHRPE associated with mutations at codons 311-1444) already present from birth
- Age 15-25: macroscopic adenomas apparent; annual colonoscopy positive; polypectomy insufficient due to polyp burden
- Age 25-35: hundreds to thousands of polyps; progressive high-grade dysplasia in largest polyps
- Age 30-40: CRC inevitable without colectomy; 90% of untreated classic FAP patients develop CRC by age 40

**Extracolonic manifestations:**

*Gardner syndrome* (the full extracolonic FAP triad):
- **Osteomas**: mandible (most common), skull, long bones; benign; may precede colon polyps by years; detected by panoramic dental X-ray; marker of FAP in young patients
- **Desmoid tumors**: mesenteric (post-colectomy trigger) or abdominal wall; ~15-20% of FAP patients; especially APC codons 1310-2011; mesenteric desmoid can be life-threatening; see desmoid-tumor entry
- **Epidermoid/sebaceous cysts**: back, face, extremities; benign; FAP stigmata
- **Supernumerary teeth** (hyperdontia): rare; associated with FAP

*Duodenal/periampullary disease:*
- Duodenal adenomas: ~90% of FAP patients develop them by age 50; periampullary carcinoma lifetime risk ~5-10% (4th most common FAP cancer after CRC, desmoid, thyroid)
- **Spigelman staging** (0-IV based on number, size, histology, dysplasia of duodenal polyps): Stage IV → prophylactic pancreaticoduodenectomy (Whipple) consideration
- Surveillance: EGD every 1-5 years depending on Spigelman stage; ampullary/periampullary polyps get endoscopic ampullectomy

*Fundic gland polyps (FGPs):*
- ~90% of FAP patients; stomach body and fundus; NOT adenomas (non-dysplastic, hyperplastic-like glands); rarely progress to cancer; biopsied to confirm FGP vs adenoma

*CHRPE (congenital hypertrophy of retinal pigment epithelium):*
- Bilateral, multifocal CHRPE: highly specific for FAP with APC mutations at codons 311-1444; absent in AFAP (mutations <168 or >1580); detected by fundoscopy; useful for surveillance of at-risk relatives pre-genotyping
- Non-FAP CHRPE: unilateral, unifocal; much more common; not associated with APC mutation

*Thyroid cancer (papillary, cribriform-morular variant):*
- ~1-2% of FAP patients; young women predominance; cribriform-morular thyroid carcinoma is pathognomonic for FAP (nuclear β-catenin by IHC); annual thyroid US recommended by some guidelines

## Pathology

### Diagnosis and genetic evaluation

**Clinical diagnosis:**
- Classic FAP: ≥100 colorectal adenomas (any age) OR personal/family history of FAP + any adenomas
- AFAP: 10-99 colorectal adenomas + APC pathogenic variant OR biallelic MUTYH pathogenic variant
- Pathological: carpeting carpet adenomas; tubulovillous histology predominates large polyps; high-grade dysplasia precedes CRC

**Genetic testing:**
- APC germline sequencing (full coding + splice sites) + MLPA (multiplex ligation-dependent probe amplification) for large rearrangements: ~95% sensitivity for APC pathogenic variant in classic FAP
- Negative APC → MUTYH biallelic testing (rule out MAP)
- Negative APC+MUTYH → POLE/POLD1 germline testing (polymerase proofreading-associated polyposis, PPAP): rare; 10-100 adenomas + extracolonic features
- Cascade testing: all first-degree relatives of APC carrier should be offered testing; start surveillance colonoscopy at age 10-12 in APC+ relatives

### Surveillance protocols (NCCN/ESMO 2024)

**Colorectal:**
- APC-positive individuals (or at-risk relatives pending testing): annual sigmoidoscopy or colonoscopy from age 10-12
- Once polyps detected: annual colonoscopy + polypectomy until polyp burden mandates colectomy (typically age 15-25 for classic FAP)
- Post-colectomy (if IRA): annual or biannual flexible sigmoidoscopy of rectal remnant (pouch or stump); rectal polyp burden dictates completion proctectomy timing

**Duodenal/upper GI:**
- EGD starting age 25-30; frequency based on Spigelman stage:
  - Stage 0-I: every 5 years
  - Stage II: every 3 years
  - Stage III: every 1-2 years
  - Stage IV: surgical consultation (Whipple vs ampullectomy)

**Desmoid:**
- Baseline abdominal MRI at time of diagnosis (FAP with codons 1310-2011 or family history of desmoid); repeat MRI if symptomatic or annually in high-risk
- Desmoid screening intensified 1-2 years post-colectomy (surgery triggers desmoid development)

### Surgical management and chemoprevention

**Prophylactic colectomy options:**

1. **Total proctocolectomy with IPAA (ileal pouch-anal anastomosis)**: most definitive; removes all colorectal mucosa; ileostomy reversed; continence preserved (pouch acts as neorectum); risk of pouchitis, nighttime incontinence
2. **Colectomy with ileorectal anastomosis (IRA)**: preserves rectum; fewer complications; requires annual rectal surveillance; pouch formation later if rectal polyps progress
3. **Total proctocolectomy with end ileostomy**: for patients with low sphincter function or inability to undergo IRA/IPAA; permanent ileostomy
4. **Timing**: colectomy typically performed in teens to early 20s, before polyp burden is unmanageable; urgency based on polyp density and dysplasia

**Medical/chemopreventive therapy:**
- **Celecoxib (400 mg BID)**: FDA-approved for reduction of colorectal polyps in FAP patients; Phase 3 data: reduces duodenal + colorectal polyp number by ~28-45%; NOT a substitute for surveillance or surgery; concurrent use with post-colectomy surveillance
- **Sulindac (150 mg BID)**: non-selective COX-1/COX-2 NSAID; reduces adenoma number ~50-60% in some FAP patients; polyp regression but rarely elimination; rebound after stopping; GI toxicity limits use; used in AFAP patients with low adenoma burden
- **Eflornithine**: ornithine decarboxylase (ODC) inhibitor; explored in FAP (NCI clinical trials); less data than celecoxib

**Desmoid management in FAP:**
- Watch-and-wait (many FAP desmoids are stable): first-line for asymptomatic or slowly growing mesenteric desmoid
- Nirogacestat (FDA 2023): indicated for all progressing desmoid tumors regardless of etiology (FAP or sporadic); ovarian toxicity in women
- Sorafenib (VEGFR/PDGFR inhibitor): off-label; used in FAP desmoid with ORR ~15-20%
- Imatinib + sulindac combination: Phase 2 data in FAP desmoid; partial responses
- Surgery: reserved for localized desmoid with complete resection achievable; mesenteric desmoid often unresectable due to adherence to mesenteric vessels

**Prognosis:**
With modern surveillance and prophylactic colectomy: FAP is no longer an inevitable death sentence; colectomy by age 25 eliminates CRC risk from the colorectum; remaining risks are duodenal cancer (~5-10%), desmoid (~10-20% cause significant morbidity/mortality), papillary thyroid (~1-2%), and gastric cancer in high-risk populations; overall life expectancy now approaches near-normal if colectomy performed and extracolonic surveillance maintained

## Connections

- `connects-to` → **[APC](../../03-molecular/apc/README.md)** — Germline APC truncating mutations cause FAP; codon position determines phenotype: codons 1250-1464 = classic profuse FAP; codons 1310-2011 = mesenteric desmoid risk; codons <168 or >1580 = attenuated FAP; codon 1309 hotspot = most severe; nuclear β-catenin in FAP adenomas
- `connects-to` → **[CTNNB1](../../03-molecular/ctnnb1/README.md)** — APC LOF → insufficient β-catenin destruction complex → nuclear β-catenin → TCF/LEF → Wnt-ON; FAP tumors show nuclear β-catenin by IHC; FAP desmoid (APC codons 1310-2011) driven by APC LOF, not CTNNB1 mutation; functionally equivalent outcome via distinct mechanisms
- `connects-to` → **[Colorectal Cancer](../../07-system/colorectal-cancer/README.md)** — FAP: 100% CRC penetrance by age 40 without colectomy; proctocolectomy (IPAA or ileostomy) is definitive prevention; annual colonoscopy from age 10-12; celecoxib FDA-approved for FAP adenoma reduction; sulindac reduces polyp burden; duodenal surveillance required
- `connects-to` → **[Desmoid Tumor](../../07-system/desmoid-tumor/README.md)** — APC germline mutations (codons 1310-2011) → FAP-associated mesenteric desmoid; more aggressive than sporadic CTNNB1-mutant desmoid; post-colectomy FAP mesenteric desmoid is a leading mortality cause in FAP; nirogacestat FDA-approved for all desmoid including FAP-associated
- `connects-to` → **[MUTYH-Associated Polyposis](../mutyh-associated-polyposis/README.md)** — Biallelic MUTYH mutations cause an autosomal-recessive phenocopy of attenuated FAP (10-100 adenomas) with no germline APC mutation; defective 8-oxoG base-excision repair drives G:C→T:A transversions in APC and KRAS; ~30% of APC-negative AFAP is actually MAP.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — KRAS activating mutations (G12D/V, ~50% of large FAP adenomas) are a key step in the Fearon-Vogelstein adenoma-carcinoma sequence after biallelic APC loss; the same APC→KRAS→SMAD4→TP53 progression as sporadic CRC, but compressed and universal because APC LOF is pre-present.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — FAP carpets the colorectal mucosa with hundreds-to-thousands of adenomas; every colonocyte carries the germline APC first hit, so independent somatic second hits seed many foci; prophylactic proctocolectomy removes the at-risk mucosa and is curative for colorectal risk.
- `connects-to` → **[Hereditary Diffuse Gastric Cancer](../hereditary-diffuse-gastric-cancer/README.md)** — FAP and hereditary diffuse gastric cancer are both dominant GI cancer syndromes but opposite in lesion: FAP carpets the colon with thousands of APC-driven adenomas, while HDGC seeds the stomach with CDH1-driven signet-ring foci that never form polyps — adenomatous versus diffuse.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — After colectomy the duodenum becomes FAP's most dangerous site: duodenal and ampullary adenomas (Spigelman-staged) progress to cancer in 3-5% and are the leading cause of cancer death in FAP, mandating lifelong upper-GI surveillance and sometimes pancreas-sparing duodenectomy.
- `connects-to` → **[Thyroid Cancer](../thyroid-cancer/README.md)** — FAP confers a distinctive thyroid risk: cribriform-morular thyroid carcinoma, a rare papillary variant occurring almost exclusively in young women with FAP, can be the presenting sign of an undiagnosed APC mutation — prompting colonoscopy and germline testing when it appears.
- `connects-to` → **[Juvenile Polyposis Syndrome](../juvenile-polyposis-syndrome/README.md)** — FAP and juvenile polyposis are both autosomal-dominant polyposis syndromes with high colorectal-cancer risk but differ in polyp biology: FAP carpets the colon with adenomas (APC/Wnt), while JPS makes fewer hamartomatous polyps (SMAD4/BMPR1A)—both need surveillance, often surgery.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — FAP affects the upper GI tract, not just the colon: nearly all patients develop fundic gland polyps and duodenal/ampullary adenomas, and gastric-cancer risk is raised, so after colectomy upper endoscopic surveillance of the stomach and duodenum becomes the priority.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — FAP is a disease of the intestinal epithelium's stem cells: germline APC loss removes the brake on Wnt/β-catenin in colonic crypt stem cells, so the entire epithelium is primed to form adenomas—hundreds to thousands—making the field, not a single clone, the cancer-prone tissue.
- `connects-to` → **[Lynch Syndrome](../lynch-syndrome/README.md)** — FAP and Lynch syndrome are the major hereditary colorectal cancer syndromes but opposite: FAP floods the colon with hundreds of adenomatous polyps via APC loss, while Lynch causes few polyps but mismatch-repair failure—polyposis versus microsatellite instability.
- `connects-to` → **[Peutz-Jeghers Syndrome](../peutz-jeghers-syndrome/README.md)** — FAP and Peutz-Jeghers are both inherited GI polyposis conditions but differ in polyp type and gene: FAP's APC loss yields hundreds of adenomas, while PJS's STK11 loss gives hamartomatous polyps and mucocutaneous pigmentation—different polyps, different cancer risks.
- `connects-to` → **[Medulloblastoma](../medulloblastoma/README.md)** — FAP can include brain tumors as Turcot syndrome: the same germline APC mutation that drives colonic polyposis also raises risk of medulloblastoma, linking Wnt-pathway dysregulation in gut and cerebellum—one mutated gene producing tumors in two very different organs.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — FAP is the textbook Wnt-pathway cancer syndrome: germline APC loss removes the brake on beta-catenin, so constitutive Wnt signaling drives the hundreds of colonic adenomas—mechanistically the same pathway activated somatically in most sporadic colorectal cancers.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — The stomach is an extracolonic FAP target: patients develop numerous fundic gland polyps and have raised gastric and duodenal cancer risk, so surveillance endoscopy of the upper GI tract complements colectomy in managing the syndrome.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — FAP raises the risk of pancreatic and other extracolonic cancers: APC loss predisposes beyond the colon to duodenal, pancreatic, thyroid and hepatoblastoma tumors—so even after prophylactic colectomy, FAP patients need broader cancer surveillance.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — FAP carpets the digestive tract with polyps: APC loss seeds hundreds to thousands of colonic adenomas that inevitably progress to colorectal cancer without colectomy, plus duodenal and gastric polyps—so FAP is a whole-gut polyposis, not just a colon disease.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — A retinal sign helps flag FAP: congenital hypertrophy of the retinal pigment epithelium (CHRPE) appears as pigmented fundus patches in many families, so an eye exam can provide an early, noninvasive clue to the APC mutation before polyps are found.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — FAP's Gardner variant shows in skin and bone: APC loss produces epidermoid cysts, fibromas and osteomas (especially of the jaw and skull), so these extraintestinal lumps of the integumentary and skeletal system can be the first visible sign of the syndrome.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — FAP raises childhood hepatoblastoma risk: young children with an APC mutation have a markedly increased chance of this liver cancer, so some families screen infants with abdominal ultrasound and AFP before the colonic polyps even appear.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — FAP overlaps brain tumors in Turcot syndrome: an APC mutation predisposes to medulloblastoma and other CNS tumors, so the colon and brain share a Wnt-pathway driver—linking a bowel polyposis syndrome to childhood brain cancer.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — FAP's Gardner variant is a fibroblast disease too: APC loss drives fibroblasts to form desmoid tumors, Gardner fibromas, and excess scar, so the same Wnt activation that carpets the colon also makes connective tissue overgrow.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — FAP grows bony osteomas as a Gardner feature: APC loss spurs osteoblasts to build benign bone tumors in the jaw and skull, an extracolonic clue that—with skin cysts and dental anomalies—can flag the syndrome before colon polyps declare themselves.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — FAP's polyps grow because APC loss unleashes MYC: with APC gone, β-catenin piles up and switches on MYC, the master proliferation gene, so every adenoma is driven by the Wnt-to-MYC signal that turns normal colon lining into a carpet of polyps.
- `connects-to` → **[Immune System](../immune-system/README.md)** — FAP tumors are immunologically cold: unlike the mismatch-repair-deficient cancers of Lynch syndrome, APC-driven colorectal cancers are microsatellite-stable with few neoantigens, so they respond poorly to the checkpoint immunotherapy that helps Lynch tumors.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — FAP reaches the skin in its Gardner variant: beyond the colon, APC loss spawns epidermoid cysts, lipomas, fibromas and bony osteomas, so skin and jaw lumps can be the first visible clue to the syndrome.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — FAP polyps recruit blood vessels via VEGF: as adenomas grow they drive VEGF-fueled angiogenesis, part of why COX-2 inhibitors—which lower this signaling—reduce polyp burden as chemoprevention in the syndrome.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages populate the stroma of FAP's polyps: drawn into the adenomas, tumor-associated macrophages secrete growth and inflammatory factors that help the APC-driven lesions progress toward colorectal cancer.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — FAP's polyps bleed away iron: hundreds of colonic adenomas ooze blood, so chronic loss drains the body's iron into a deficiency anemia that can be an early clue before cancer develops.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — FAP extends cancer risk to the pancreas: beyond the colon, the APC defect raises the chance of duodenal, periampullary, and pancreatic tumors, so surveillance reaches the upper GI tract too.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — FAP's adenomas summon endothelial cells: VEGF from the growing polyps drives these vessel-lining cells to build blood supply, which is why COX-2 inhibitors that curb this angiogenesis shrink polyp burden.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — FAP is policed by light: lifelong colonoscopy hunts the polyps, and a dilated eye exam spots CHRPE—the dark retinal patches that mark the syndrome—both relying on visible-light viewing.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — FAP's desmoid tumors are fibrosis run amok: APC loss lets fibroblasts build invasive fibrous masses, the desmoids that become a leading cause of death once the colon is removed.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — FAP raises thyroid cancer risk: a distinctive cribriform-morular papillary thyroid carcinoma occurs especially in young women with the syndrome, so thyroid screening is advised.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reads FAP's two telltale lesions: the dysplastic glands of its countless colonic adenomas, and the pigment-stuffed cells of CHRPE, the dark retinal patches that flag the syndrome at an eye exam.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — In the Gardner variant, FAP grows bone: benign osteomas sprout from the jaw and skull, bony overgrowths of the marrow-bearing facial bones that, with skin cysts, can betray the syndrome before the gut polyps do.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — FAP's osteomas are built of calcium: the Gardner-syndrome bony tumors lay down dense calcium-phosphate mineral, hard masses on the skull and jaw visible as bright opacities on imaging.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Gardner syndrome marks the skeleton and teeth: FAP's variant grows osteomas on the jaw and skull and brings dental anomalies — supernumerary teeth and odontomas — extracolonic clues that can predate the bowel polyps.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — The Turcot variant ties FAP to the brain: alongside its colonic polyps it predisposes to CNS tumors, classically medulloblastoma, so neurological symptoms can be part of the syndrome's reach.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — FAP quietly enlarges the adrenals: benign adrenal adenomas are more common than in the general population, usually silent incidentalomas found on the imaging done to track the syndrome's other tumors.

[^kinzler-1991-apc]: Kinzler KW, Nilbert MC, Su LK, et al. Identification of FAP locus genes from chromosome 5q21. *Science.* 1991;253(5020):661-665. [doi:10.1126/science.1651562](https://doi.org/10.1126/science.1651562) · [PubMed 1651562](https://pubmed.ncbi.nlm.nih.gov/1651562/)
[^fearon-1990-vogelstein]: Fearon ER, Vogelstein B. A genetic model for colorectal tumorigenesis. *Cell.* 1990;61(5):759-767. [doi:10.1016/0092-8674(90)90186-i](https://doi.org/10.1016/0092-8674(90)90186-i) · [PubMed 2188735](https://pubmed.ncbi.nlm.nih.gov/2188735/)

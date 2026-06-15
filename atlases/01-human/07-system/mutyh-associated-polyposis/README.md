---
schema: human-scale-entry/v1
id: mutyh-associated-polyposis
name: MUTYH-Associated Polyposis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "MUTYH-associated polyposis (MAP) is an autosomal recessive CRC predisposition syndrome caused by biallelic MUTYH mutations; 10-100 colorectal adenomas; CRC risk ~40-75% lifetime; two founder variants (Y179C, G396D) in most Western patients; annual colonoscopy from age 25."
aliases: ["MAP", "MUTYH-associated polyposis", "MYH-associated polyposis", "biallelic MUTYH", "MUTYH polyposis", "MAP CRC", "MYH polyposis", "autosomal recessive polyposis", "MAP colorectal"]
sources:
  - id: sieber-2003-mutyh-map
    type: peer-reviewed
    cite: "Sieber OM, Lipton L, Crabtree M, et al. Multiple colorectal adenomas, classic adenomatous polyposis, and germ-line mutations in MYH. N Engl J Med. 2003;348(9):791-799."
    doi: "10.1056/NEJMoa025283"
    pmid: "12606733"
    url: "https://doi.org/10.1056/NEJMoa025283"
  - id: al-tassan-2002-mutyh
    type: peer-reviewed
    cite: "Al-Tassan N, Chmiel NH, Maynard J, et al. Inherited variants of MYH associated with somatic G:C→T:A mutations in colorectal tumors. Nat Genet. 2002;30(2):227-232."
    doi: "10.1038/ng828"
    pmid: "11818965"
    url: "https://doi.org/10.1038/ng828"
cross_links:
  - target: 01-human/03-molecular/mutyh
    relation: connects-to
    note: "Germline biallelic MUTYH pathogenic variants cause MAP; two founder variants (Y179C and G396D) account for ~80% of Western MAP; monoallelic MUTYH carriers have modestly elevated CRC risk (~1.5-2x); MAP surveillance mimics FAP but with 1-2 year colonoscopy intervals."
  - target: 01-human/03-molecular/apc
    relation: connects-to
    note: "MAP adenomas harbor somatic APC mutations driven by MUTYH-induced G:C→T:A transversions (SBS18); APC germline (FAP) and MUTYH biallelic (MAP) cause polyposis via distinct mechanisms (Wnt dysregulation vs oxidative mutational load); germline testing distinguishes both."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "MAP-associated CRC is predominantly right-sided; MUTYH SBS18 signature drives KRAS G12C transversions in MAP-CRC; overall CRC risk ~40-75% lifetime by age 60; annual colonoscopy with polypectomy from age 25 is the primary prevention strategy."
  - target: 01-human/07-system/fap
    relation: connects-to
    note: "MAP (biallelic MUTYH) mimics attenuated FAP (APC germline) but has autosomal recessive inheritance, fewer adenomas (10-100 vs >100 in FAP), later CRC onset (40-60s), and includes serrated polyps; genetic testing distinguishes both syndromes in apparent de novo polyposis."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "MUTYH-induced SBS18 (G:C→T:A transversions) drives KRAS G12C in ~70% of MAP-CRC; KRAS G12C is rare in sporadic CRC (~2-5%) but prevalent in NSCLC; G12C in CRC should prompt MUTYH germline testing; sotorasib and adagrasib (KRAS G12C inhibitors) show modest activity in CRC G12C."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "MAP adenomas harbor somatic APC G→T transversions (SBS18) → APC loss → Wnt/β-catenin activation → adenoma initiation; MAP APC transversions create the same Wnt dysregulation as FAP germline truncations via MUTYH oxidative load; CTNNB1 G→T transversions also occur in MAP adenomas."
  - target: 01-human/07-system/lynch-syndrome
    relation: connects-to
    note: "MAP and Lynch are key non-FAP hereditary CRC syndromes: MAP (biallelic MUTYH, recessive, MSS, KRAS G12C) vs Lynch (MMR, dominant, MSI-H, extracolonic cancers); MAP is MSS → anti-PD-1 ICB inactive; Lynch MSI-H → pembrolizumab-responsive; germline testing distinguishes both."
  - target: 01-human/07-system/hlrcc
    relation: connects-to
    note: "MUTYH-associated polyposis and HLRCC are hereditary cancer syndromes but utterly different: MAP is recessive MUTYH repair failure causing oxidative mutations and colonic polyposis; HLRCC is dominant FH (Krebs-cycle) loss causing fumarate-driven leiomyomas and kidney cancer."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "The large intestine is MAP's main target: biallelic MUTYH failure to repair oxidative 8-oxoguanine lesions lets G:C→T:A transversions accumulate in colonic epithelium, seeding 10-100 adenomas with a ~40-75% lifetime CRC risk — managed by colonoscopy from the mid-20s."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Beyond the colon, MAP affects the upper GI tract: duodenal adenomas develop in ~17-25% of patients (with a smaller duodenal cancer risk than FAP), so periodic upper endoscopy with attention to the ampulla is added to colonoscopic surveillance in MUTYH biallelic carriers."
  - target: 01-human/07-system/juvenile-polyposis-syndrome
    relation: connects-to
    note: "MAP and juvenile polyposis are inherited polyposis syndromes distinguished by polyp histology: MAP (biallelic MUTYH) produces adenomatous polyps from defective oxidative DNA repair, while juvenile polyposis (SMAD4/BMPR1A) produces hamartomatous polyps."
  - target: 01-human/07-system/peutz-jeghers-syndrome
    relation: connects-to
    note: "MAP and Peutz-Jeghers are polyposis syndromes at different poles: MAP's MUTYH-driven adenomas carry high colorectal cancer risk through the classic adenoma-carcinoma sequence, while Peutz-Jeghers' STK11 hamartomas plus mucocutaneous pigmentation raise risk across many organs."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "MAP raises upper-GI as well as colorectal risk: many patients develop duodenal and gastric polyps, and gastric/duodenal cancer risk is elevated, so MUTYH biallelic carriers need upper-endoscopic surveillance alongside their colonoscopy."
  - target: 01-human/07-system/hereditary-diffuse-gastric-cancer
    relation: connects-to
    note: "MAP and HDGC are inherited GI cancer syndromes with different mechanisms: MAP from biallelic MUTYH loss causing colorectal polyposis, HDGC from CDH1 loss causing diffuse gastric and lobular breast cancer—both warrant upper- and lower-GI surveillance."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "MAP carries extracolonic cancer risk including the pancreas: biallelic MUTYH loss raises risk of duodenal and modestly pancreatic cancers, since unrepaired oxidative DNA damage can transform other epithelia too—so surveillance extends to the upper GI tract."
  - target: 01-human/07-system/endometrial-cancer
    relation: connects-to
    note: "MAP raises gynecologic as well as colorectal cancer risk: biallelic MUTYH carriers have increased endometrial (and ovarian) cancer rates, as unrepaired oxidative mutations accumulate in tissues beyond the colon—broadening surveillance for affected women."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "MAP carpets the intestinal epithelium with adenomas: defective MUTYH base-excision repair lets oxidative G-to-T mutations accumulate in colonic crypt cells, driving the tens-to-hundreds of polyps—fewer than FAP but on the same adenoma-carcinoma path."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "MAP extends beyond the colon to the upper GI tract: like FAP, it raises the risk of duodenal and gastric polyps and cancer, so surveillance includes upper endoscopy—the same MUTYH repair defect mutating epithelium throughout the gut."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "MAP tumors progress through the usual colorectal genes: MUTYH loss seeds characteristic G-to-T transversions in APC and KRAS, and TP53 loss later drives invasion—so a base-excision-repair defect feeds the standard adenoma-carcinoma mutation sequence."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "MUTYH-associated polyposis predisposes across the digestive tract: biallelic MUTYH loss seeds adenomatous polyps and cancer in the colon plus duodenal and gastric tumors, so it is managed like a milder, recessive cousin of FAP with GI surveillance."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "MAP is fundamentally a failure to repair oxidative DNA damage: MUTYH normally excises adenine mispaired with 8-oxoguanine, the lesion left when reactive oxygen attacks DNA, so its loss lets oxygen-driven G:C-to-T:A mutations accumulate and seed polyps."
  - target: 01-human/07-system/bladder-cancer
    relation: connects-to
    note: "MAP raises risk beyond the gut, including bladder cancer: the same defective oxidative-damage repair predisposes the urothelium, so MUTYH carriers face a modestly increased risk of bladder and other extraintestinal cancers warranting awareness."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "MUTYH-driven tumors are hypermutated and immunogenic: unrepaired oxidative damage produces a heavy load of G-to-T mutations and neoantigens that cytotoxic T cells can recognize, so checkpoint immunotherapy is of interest in these cancers."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "MUTYH-associated polyposis raises risk beyond the bowel: biallelic carriers face a modestly increased rate of ovarian and other extracolonic cancers, so management considers gynecologic risk alongside the dominant colorectal surveillance."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Breast cancer is a debated MUTYH extracolonic risk: some studies link biallelic MUTYH loss to a modest rise in breast cancer, adding it to the extracolonic tumors weighed when counseling families with the syndrome."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "MUTYH-associated polyposis writes its mutations as G→T transversions: failed repair of oxidized guanine misspells DNA, hitting APC, KRAS, and tumor suppressors like CDKN2A—a distinctive oxidative signature that turns colon polyps cancerous."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "MAP tumors carry a heavy mutation load that can alert NK cells: the oxidative damage spawns many altered proteins, marking cells for natural killer (and T-cell) attack and making these cancers candidates for immunotherapy."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "MAP's mutation-rich tumors give dendritic cells plenty to present: the neoantigens from oxidative DNA errors can be displayed to prime T cells, an immune opening that checkpoint therapy may exploit in mismatch-proficient but heavily mutated cancers."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "MAP's colorectal cancers spread to the liver: like other bowel cancers, the tumors that arise from MUTYH-driven polyps metastasize first to the liver through the portal vein, making liver imaging key to staging and follow-up."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Chronic inflammation via NF-kB helps MAP polyps progress: in the colon, this inflammatory switch supports survival and proliferation of the mutation-laden cells, adding an inflammatory push to the oxidative DNA damage that defines the syndrome."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Regulatory T cells temper the immune response to MAP's mutated tumors: though the oxidative-damage cancers carry many neoantigens, Tregs in the infiltrate restrain the attack, a brake that checkpoint therapy could lift in heavily mutated cases."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "MUTYH-associated polyposis bleeds iron from the colon: its adenomas ooze blood, so iron-deficiency anemia can be the quiet first clue that prompts the colonoscopy revealing the polyps."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "MAP's hypermutated tumors draw macrophages: oxidative-damage mutations spawn neoantigens that pull a dense immune infiltrate including macrophages into the colorectal cancers."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "MAP's colorectal cancers grow in fibrosis: as the adenomas turn malignant they provoke a desmoplastic fibrous stroma that supports invasion, the scar-like tissue typical of colon cancer."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photons keep MAP patients alive: lifelong colonoscopy is the surveillance backbone, finding and clearing polyps before they turn cancerous, while upper endoscopy and imaging watch the duodenum where MAP's extracolonic tumors also arise."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "MAP reaches beyond the colon to the thyroid: like FAP, it carries an increased risk of papillary thyroid cancer, so thyroid examination and ultrasound are folded into the surveillance these patients receive for life."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "MAP can announce itself on the skin: like other polyposis syndromes it is associated with sebaceous tumors and epidermoid cysts, cutaneous clues that can prompt the genetic testing which uncovers the underlying colon-cancer risk."
---

# MUTYH-Associated Polyposis

## Overview

**MUTYH-associated polyposis (MAP)** is an **autosomal recessive** hereditary colorectal polyposis syndrome caused by biallelic pathogenic variants in the **MUTYH** (MutY DNA Glycosylase) gene on chromosome **1p34**. MAP is unique among major hereditary colorectal cancer syndromes in its recessive inheritance — all other well-characterized syndromes (FAP/APC, Lynch/MMR, PJS/STK11, JPS/SMAD4) are autosomal dominant. MAP affects approximately **1 in 15,000-20,000** individuals in European-ancestry populations. The phenotype is characterized by **10-100 colorectal adenomas** (occasionally more), elevated colorectal cancer (CRC) risk of ~40-75% lifetime, and an attenuated or FAP-like endoscopic appearance. Two founder pathogenic variants — **Y179C** and **G396D** — account for ~80% of MAP alleles in Western European and UK populations [^sieber-2003-mutyh-map] [^al-tassan-2002-mutyh].

**MAP phenotype compared to other colorectal polyposis syndromes:**

| Feature | MAP (MUTYH biallelic) | FAP (APC germline) | AFAP (APC, C/N-terminal) | Lynch (MMR germline) |
|---|---|---|---|---|
| Inheritance | Autosomal recessive | Autosomal dominant | Autosomal dominant | Autosomal dominant |
| Gene | MUTYH | APC | APC | MLH1/MSH2/MSH6/PMS2 |
| Polyp count | 10-100 (variable) | >100 (usually 1000s) | 10-100 | 0-5 (no polyp syndrome) |
| Polyp type | Adenomas + serrated | Adenomas | Adenomas | Few adenomas (MSI-H) |
| CRC lifetime risk | ~40-75% | ~100% (without surgery) | ~70% | ~40-80% (gene-specific) |
| Age of CRC | 40s-60s | 30-40s (untreated) | 40s-50s | 40-70s |
| De novo pattern | Siblings affected, parents unaffected | One parent usually affected | Variable | Variable |
| MSI | Microsatellite stable | Microsatellite stable | Microsatellite stable | MSI-High |

## Structure

### Genetic basis of MAP

**Biallelic MUTYH requirement:**
Both copies of MUTYH must be inactivated for MAP phenotype. Compound heterozygosity (two different pathogenic variants on separate alleles) is more common than homozygosity in outbred populations. The most frequent genotypes in European populations:

- **Y179C/G396D** (compound heterozygous): ~30-40% of MAP patients in UK/NL series
- **Y179C/Y179C** (homozygous): ~15-20%; associated with higher polyp burden
- **G396D/G396D** (homozygous): ~5-10%
- Other biallelic combinations: ~30-40%

**Founder variants:**
- **Y179C** (c.536A>G, p.Tyr179Cys): exon 7; disrupts 8-oxoG recognition by MUTYH; globally prevalent in European-ancestry populations; also present in Indian, Asian, and Hispanic populations at lower frequency
- **G396D** (c.1187G>A, p.Gly396Asp): exon 13; disrupts MUTYH 4Fe-4S cluster; common in UK, Dutch, Northern European
- **Other ethnic-specific variants**: South Asian MAP patients: E466del, Y104Cys; Japanese: G265del; Ashkenazi Jewish: rare (MUTYH MAP less prevalent in Ashkenazi population)

**Monoallelic (heterozygous) MUTYH carriers:**
- ~1-2% of European-ancestry general population
- ~1.5-2x elevated CRC risk (odds ratio ~1.4-1.6 in meta-analyses)
- Not MAP; do not need MAP surveillance protocol
- Recommend: colonoscopy every 3-5 years from age 40; intensity varies by family history and polyp findings

### Somatic mutation landscape in MAP tumors

MUTYH deficiency creates a characteristic **SBS18 mutational signature** (G:C→T:A transversions; COSMIC Mutational Signatures):
- APC somatic mutations: predominantly nonsense or missense G→T transversions (e.g., K1462N, E1309Stop converted to T); different from the frameshift/truncating APC variants in FAP; MAP APC mutations still activate Wnt/β-catenin
- KRAS somatic mutations: **G12C** (GGT→TGT) transversion in ~70% of MAP-associated CRC; KRAS G12C is rare in sporadic CRC (~2-5%) and prevalent in NSCLC (~14%); KRAS G12C in CRC should prompt MUTYH germline testing
- CTNNB1 (β-catenin) mutations: some MAP adenomas have CTNNB1 G→T transversions activating β-catenin
- Microsatellite stability: MAP tumors are **MSS** (microsatellite stable), unlike Lynch syndrome CRC (MSI-H); this is critical for correct prognostication and immunotherapy selection

## Function

### Disease mechanism

MUTYH deficiency prevents removal of adenine mispaired with 8-oxoguanine (8-oxoG) in the genome. Reactive oxygen species (dietary, inflammatory, metabolic) oxidize guanine to 8-oxoG at thousands of sites per cell per day. DNA polymerase inserts A opposite 8-oxoG → A:8-oxoG mispair. Without MUTYH:
1. A:8-oxoG → next replication → T:A permanently replaces G:C → **G:C→T:A transversion**
2. Transversions accumulate preferentially at GC-rich sequences (proto-oncogene codons and tumor suppressor codon hotspots)
3. Somatic APC G→T transversions → Wnt pathway activation → adenoma initiation
4. Additional transversions (KRAS G12C, CTNNB1) → adenoma-to-carcinoma progression

The key distinction from MMR-deficient (Lynch syndrome) carcinogenesis: MAP generates a different mutational signature (SBS18, large-scale transversions) and produces MSS tumors, while Lynch generates SBS6/SBS15 (small indel hypermutation) and MSI-H tumors.

### Colorectal adenoma progression in MAP

MAP adenomas are morphologically similar to sporadic conventional adenomas (tubular, tubulovillous, villous). However, MAP patients also develop **serrated polyps** (sessile serrated lesions, traditional serrated adenomas) at higher frequency than the general population — consistent with oxidative damage driving the serrated pathway through KRAS G12C activation. The serrated pathway adds to CRC risk beyond classical adenoma-carcinoma progression.

**Upper GI involvement:**
- ~50% of MAP patients develop **duodenal adenomas** (D1-D4); often periampullary; histologically similar to colorectal adenomas; lifetime risk of duodenal/small bowel cancer is elevated (~4-10%); Spigelman staging applied to duodenal polyposis in MAP
- Gastric fundic gland polyps: less common than in FAP but reported in MAP

**Extracolonic malignancies in MAP:**
- **Duodenal/small bowel cancer**: ~4-10% lifetime risk; surveillance recommended
- **Ovarian cancer**: possible modest elevation in some series (biologically plausible: oxidative BER role in ovarian epithelium)
- **Sebaceous gland tumors** (sebaceoma, sebaceous carcinoma): Muir-Torre-like phenotype in a subset of MAP patients; distinct from Lynch-associated Muir-Torre (MMR-deficient tumors); MAP sebaceous tumors are MSS
- **Bladder cancer**: slight elevation in some population-based studies

## Pathology

### Surveillance and management protocol

**Diagnosis criteria:**
- ≥10 colorectal adenomas + biallelic MUTYH pathogenic variants confirmed
- Or CRC with biallelic MUTYH + limited/absent family history (recessive pattern)
- Or CRC with SBS18 signature on tumor profiling → germline confirmation

**Colonoscopy surveillance:**
- From age **25-30** (or 5 years before earliest CRC in family)
- Every **1-2 years** if adenomas present (annual if multiple or large)
- Every **2-3 years** if polyp-free
- Polypectomy at each session; annual if polyp count difficult to control endoscopically
- Chromoendoscopy or image-enhanced endoscopy (NBI, FICE) to detect flat adenomas

**Upper GI surveillance:**
- EGD from age **30-35**
- Every 1-4 years depending on Spigelman stage for duodenal adenomas (Stage 0-II: 5 years; Stage III: 3 years; Stage IV: consider surgery)

**Colectomy indications:**
- Unmanageable polyp burden (>20-30 adenomas per annual colonoscopy with inadequate polypectomy)
- High-grade dysplasia in multiple adenomas
- CRC detected at surveillance
- Options: **segmental colectomy + continued surveillance** (acceptable if polyp burden is low/regional), **subtotal colectomy + ileorectal anastomosis (IRA)** (if diffuse colonic disease), **ileal pouch-anal anastomosis (IPAA)** (if rectum heavily involved)
- Timing: generally around age 40-50, guided by polyp burden and patient preference; much later than FAP (which requires surgery in teens-20s)

**Chemoprevention:**
- **Sulindac** and **celecoxib**: reduce adenoma count in MAP patients in small case series; rationale from FAP (APC-mutant) data; no randomized MAP-specific trial; used as adjunct to endoscopic surveillance
- Antioxidants (vitamin C, E, N-acetylcysteine): theoretical rationale (reduce ROS → reduce 8-oxoG); no clinical evidence for chemoprevention in MAP

### Family cascade testing

Because MAP is autosomal recessive: siblings of MAP patients are at **25%** risk (both parents are obligate carriers); parents are carriers (heterozygous) unless de novo. Cascade testing:
1. Test both parents → confirm each is monoallelic MUTYH carrier
2. Test all siblings: each has 25% chance of biallelic MUTYH; 50% chance of monoallelic (elevated risk)
3. Children of MAP patients: all children of a MAP patient are obligate monoallelic carriers; children are at MAP risk only if the other parent is also a MUTYH carrier (population carrier frequency ~1-2% → MAP child risk ~1-2% for each child of a MAP patient in an outbred population)

## Connections

- `connects-to` → **[MUTYH](../../03-molecular/mutyh/README.md)** — Germline biallelic MUTYH pathogenic variants cause MAP; two founder variants (Y179C and G396D) account for ~80% of Western MAP; monoallelic MUTYH carriers have modestly elevated CRC risk (~1.5-2x); MAP surveillance mimics FAP but with 1-2 year colonoscopy intervals.
- `connects-to` → **[APC](../../03-molecular/apc/README.md)** — MAP adenomas harbor somatic APC mutations driven by MUTYH-induced G:C→T:A transversions (SBS18); APC germline (FAP) and MUTYH biallelic (MAP) cause polyposis via distinct mechanisms (Wnt dysregulation vs oxidative mutational load); germline testing distinguishes both.
- `connects-to` → **[Colorectal Cancer](../../07-system/colorectal-cancer/README.md)** — MAP-associated CRC is predominantly right-sided; MUTYH SBS18 signature drives KRAS G12C transversions in MAP-CRC; overall CRC risk ~40-75% lifetime by age 60; annual colonoscopy with polypectomy from age 25 is the primary prevention strategy.
- `connects-to` → **[FAP](../fap/README.md)** — MAP (biallelic MUTYH) mimics attenuated FAP (APC germline) but has autosomal recessive inheritance, fewer adenomas (10-100 vs >100 in FAP), later CRC onset (40-60s), and includes serrated polyps; genetic testing distinguishes both syndromes in apparent de novo polyposis.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — MUTYH-induced SBS18 (G:C→T:A transversions) drives KRAS G12C in ~70% of MAP-CRC; KRAS G12C is rare in sporadic CRC (~2-5%) but prevalent in NSCLC; G12C in CRC should prompt MUTYH germline testing; sotorasib and adagrasib (KRAS G12C inhibitors) show modest activity in CRC G12C.
- `connects-to` → **[Wnt/β-Catenin](../../03-molecular/wnt-beta-catenin/README.md)** — MAP adenomas harbor somatic APC G→T transversions (SBS18) → APC loss → Wnt/β-catenin activation → adenoma initiation; MAP APC transversions create the same Wnt dysregulation as FAP germline truncations via MUTYH oxidative load; CTNNB1 G→T transversions also occur in MAP adenomas.
- `connects-to` → **[Lynch Syndrome](../lynch-syndrome/README.md)** — MAP and Lynch are key non-FAP hereditary CRC syndromes: MAP (biallelic MUTYH, recessive, MSS, KRAS G12C) vs Lynch (MMR, dominant, MSI-H, extracolonic cancers); MAP is MSS → anti-PD-1 ICB inactive; Lynch MSI-H → pembrolizumab-responsive; germline testing distinguishes both.
- `connects-to` → **[Hereditary Leiomyomatosis and Renal Cell Carcinoma](../hlrcc/README.md)** — MUTYH-associated polyposis and HLRCC are hereditary cancer syndromes but utterly different: MAP is recessive MUTYH repair failure causing oxidative mutations and colonic polyposis; HLRCC is dominant FH (Krebs-cycle) loss causing fumarate-driven leiomyomas and kidney cancer.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — The large intestine is MAP's main target: biallelic MUTYH failure to repair oxidative 8-oxoguanine lesions lets G:C→T:A transversions accumulate in colonic epithelium, seeding 10-100 adenomas with a ~40-75% lifetime CRC risk — managed by colonoscopy from the mid-20s.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — Beyond the colon, MAP affects the upper GI tract: duodenal adenomas develop in ~17-25% of patients (with a smaller duodenal cancer risk than FAP), so periodic upper endoscopy with attention to the ampulla is added to colonoscopic surveillance in MUTYH biallelic carriers.
- `connects-to` → **[Juvenile Polyposis Syndrome](../juvenile-polyposis-syndrome/README.md)** — MAP and juvenile polyposis are inherited polyposis syndromes distinguished by polyp histology: MAP (biallelic MUTYH) produces adenomatous polyps from defective oxidative DNA repair, while juvenile polyposis (SMAD4/BMPR1A) produces hamartomatous polyps.
- `connects-to` → **[Peutz-Jeghers Syndrome](../peutz-jeghers-syndrome/README.md)** — MAP and Peutz-Jeghers are polyposis syndromes at different poles: MAP's MUTYH-driven adenomas carry high colorectal cancer risk through the classic adenoma-carcinoma sequence, while Peutz-Jeghers' STK11 hamartomas plus mucocutaneous pigmentation raise risk across many organs.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — MAP raises upper-GI as well as colorectal risk: many patients develop duodenal and gastric polyps, and gastric/duodenal cancer risk is elevated, so MUTYH biallelic carriers need upper-endoscopic surveillance alongside their colonoscopy.
- `connects-to` → **[Hereditary Diffuse Gastric Cancer](../hereditary-diffuse-gastric-cancer/README.md)** — MAP and HDGC are inherited GI cancer syndromes with different mechanisms: MAP from biallelic MUTYH loss causing colorectal polyposis, HDGC from CDH1 loss causing diffuse gastric and lobular breast cancer—both warrant upper- and lower-GI surveillance.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — MAP carries extracolonic cancer risk including the pancreas: biallelic MUTYH loss raises risk of duodenal and modestly pancreatic cancers, since unrepaired oxidative DNA damage can transform other epithelia too—so surveillance extends to the upper GI tract.
- `connects-to` → **[Endometrial Cancer](../endometrial-cancer/README.md)** — MAP raises gynecologic as well as colorectal cancer risk: biallelic MUTYH carriers have increased endometrial (and ovarian) cancer rates, as unrepaired oxidative mutations accumulate in tissues beyond the colon—broadening surveillance for affected women.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — MAP carpets the intestinal epithelium with adenomas: defective MUTYH base-excision repair lets oxidative G-to-T mutations accumulate in colonic crypt cells, driving the tens-to-hundreds of polyps—fewer than FAP but on the same adenoma-carcinoma path.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — MAP extends beyond the colon to the upper GI tract: like FAP, it raises the risk of duodenal and gastric polyps and cancer, so surveillance includes upper endoscopy—the same MUTYH repair defect mutating epithelium throughout the gut.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — MAP tumors progress through the usual colorectal genes: MUTYH loss seeds characteristic G-to-T transversions in APC and KRAS, and TP53 loss later drives invasion—so a base-excision-repair defect feeds the standard adenoma-carcinoma mutation sequence.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — MUTYH-associated polyposis predisposes across the digestive tract: biallelic MUTYH loss seeds adenomatous polyps and cancer in the colon plus duodenal and gastric tumors, so it is managed like a milder, recessive cousin of FAP with GI surveillance.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — MAP is fundamentally a failure to repair oxidative DNA damage: MUTYH normally excises adenine mispaired with 8-oxoguanine, the lesion left when reactive oxygen attacks DNA, so its loss lets oxygen-driven G:C-to-T:A mutations accumulate and seed polyps.
- `connects-to` → **[Bladder Cancer](../bladder-cancer/README.md)** — MAP raises risk beyond the gut, including bladder cancer: the same defective oxidative-damage repair predisposes the urothelium, so MUTYH carriers face a modestly increased risk of bladder and other extraintestinal cancers warranting awareness.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — MUTYH-driven tumors are hypermutated and immunogenic: unrepaired oxidative damage produces a heavy load of G-to-T mutations and neoantigens that cytotoxic T cells can recognize, so checkpoint immunotherapy is of interest in these cancers.
- `connects-to` → **[Ovarian Cancer](../ovarian-cancer/README.md)** — MUTYH-associated polyposis raises risk beyond the bowel: biallelic carriers face a modestly increased rate of ovarian and other extracolonic cancers, so management considers gynecologic risk alongside the dominant colorectal surveillance.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — Breast cancer is a debated MUTYH extracolonic risk: some studies link biallelic MUTYH loss to a modest rise in breast cancer, adding it to the extracolonic tumors weighed when counseling families with the syndrome.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — MUTYH-associated polyposis writes its mutations as G→T transversions: failed repair of oxidized guanine misspells DNA, hitting APC, KRAS, and tumor suppressors like CDKN2A—a distinctive oxidative signature that turns colon polyps cancerous.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — MAP tumors carry a heavy mutation load that can alert NK cells: the oxidative damage spawns many altered proteins, marking cells for natural killer (and T-cell) attack and making these cancers candidates for immunotherapy.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — MAP's mutation-rich tumors give dendritic cells plenty to present: the neoantigens from oxidative DNA errors can be displayed to prime T cells, an immune opening that checkpoint therapy may exploit in mismatch-proficient but heavily mutated cancers.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — MAP's colorectal cancers spread to the liver: like other bowel cancers, the tumors that arise from MUTYH-driven polyps metastasize first to the liver through the portal vein, making liver imaging key to staging and follow-up.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Chronic inflammation via NF-kB helps MAP polyps progress: in the colon, this inflammatory switch supports survival and proliferation of the mutation-laden cells, adding an inflammatory push to the oxidative DNA damage that defines the syndrome.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Regulatory T cells temper the immune response to MAP's mutated tumors: though the oxidative-damage cancers carry many neoantigens, Tregs in the infiltrate restrain the attack, a brake that checkpoint therapy could lift in heavily mutated cases.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — MUTYH-associated polyposis bleeds iron from the colon: its adenomas ooze blood, so iron-deficiency anemia can be the quiet first clue that prompts the colonoscopy revealing the polyps.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — MAP's hypermutated tumors draw macrophages: oxidative-damage mutations spawn neoantigens that pull a dense immune infiltrate including macrophages into the colorectal cancers.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — MAP's colorectal cancers grow in fibrosis: as the adenomas turn malignant they provoke a desmoplastic fibrous stroma that supports invasion, the scar-like tissue typical of colon cancer.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photons keep MAP patients alive: lifelong colonoscopy is the surveillance backbone, finding and clearing polyps before they turn cancerous, while upper endoscopy and imaging watch the duodenum where MAP's extracolonic tumors also arise.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — MAP reaches beyond the colon to the thyroid: like FAP, it carries an increased risk of papillary thyroid cancer, so thyroid examination and ultrasound are folded into the surveillance these patients receive for life.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — MAP can announce itself on the skin: like other polyposis syndromes it is associated with sebaceous tumors and epidermoid cysts, cutaneous clues that can prompt the genetic testing which uncovers the underlying colon-cancer risk.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^sieber-2003-mutyh-map]: Sieber OM, Lipton L, Crabtree M, et al. Multiple colorectal adenomas, classic adenomatous polyposis, and germ-line mutations in MYH. *N Engl J Med.* 2003;348(9):791-799. [doi:10.1056/NEJMoa025283](https://doi.org/10.1056/NEJMoa025283) · [PubMed 12606733](https://pubmed.ncbi.nlm.nih.gov/12606733/)
[^al-tassan-2002-mutyh]: Al-Tassan N, Chmiel NH, Maynard J, et al. Inherited variants of MYH associated with somatic G:C→T:A mutations in colorectal tumors. *Nat Genet.* 2002;30(2):227-232. [doi:10.1038/ng828](https://doi.org/10.1038/ng828) · [PubMed 11818965](https://pubmed.ncbi.nlm.nih.gov/11818965/)

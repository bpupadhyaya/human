---
schema: human-scale-entry/v1
id: bloom-syndrome
name: Bloom Syndrome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Bloom syndrome is caused by biallelic BLM mutations; small body size, sun-sensitive telangiectatic facial erythema, immunodeficiency; elevated sister chromatid exchanges (~10x); pan-cancer predisposition (ALL, lymphoma, GI carcinoma, skin cancers); median survival ~30 years."
aliases: ["Bloom syndrome", "Bloom's syndrome", "BLM syndrome", "Bloom syndrome cancer", "Bloom syndrome SCE", "RECQL3 syndrome", "Bloom syndrome ALL", "Bloom syndrome chromosomal instability", "Bloom syndrome hereditary"]
sources:
  - id: ellis-1995-blm-cloning
    type: peer-reviewed
    cite: "Ellis NA, Groden J, Ye TZ, et al. The Bloom's syndrome gene product is homologous to RecQ helicases. Cell. 1995;83(4):655-666."
    doi: "10.1016/0092-8674(95)90105-1"
    pmid: "7585968"
    url: "https://doi.org/10.1016/0092-8674(95)90105-1"
  - id: german-1997-bloom-cancer
    type: peer-reviewed
    cite: "German J. Bloom's syndrome. XX. The first 100 cancers. Cancer. 1997;71(12):4016-4023."
    doi: "10.1002/1097-0142(19930615)71:12<4016::AID-CNCR18>3.0.CO;2-E"
    pmid: "9216035"
    url: "https://doi.org/10.1002/1097-0142(19930615)71:12<4016::AID-CNCR18>3.0.CO;2-E"
cross_links:
  - target: 01-human/03-molecular/blm
    relation: connects-to
    note: "Biallelic BLM LOF → Bloom syndrome via crossover accumulation and SCE elevation (~10x); chromosomal instability → LOH at tumor suppressor loci → pan-cancer predisposition (ALL, lymphoma, GI carcinoma, skin); Bloom Syndrome Registry has tracked >300 patients for >60 years."
  - target: 01-human/03-molecular/brca1
    relation: connects-to
    note: "BLM and BRCA1 form a complex at stalled replication forks to suppress aberrant homologous recombination and resolve Holliday junctions; both BLM LOF and BRCA1 LOF result in chromosomal instability and pan-cancer predisposition via distinct but overlapping HR defects."
  - target: 01-human/03-molecular/wrn
    relation: connects-to
    note: "BLM and WRN are both RecQ helicases: BLM resolves double Holliday junctions to suppress crossover (SCE elevated ~10x in BLM LOF); WRN has exonuclease activity and maintains telomeres; BLM LOF → childhood-onset pan-cancer; WRN LOF → adult progeroid syndrome."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "BLM LOF in Bloom syndrome confers elevated colorectal cancer risk due to crossover-mediated LOH at APC and other CRC tumor suppressor loci; GI carcinomas are among the most common malignancies in adult Bloom syndrome patients; colonoscopy surveillance from early adulthood."
  - target: 01-human/07-system/burkitt-lymphoma
    relation: connects-to
    note: "Burkitt lymphoma and NHL are among the most common lymphoid malignancies in Bloom syndrome; crossover-mediated LOH at 8q24 (MYC) contributes; BS patients have ~50-100× elevated lymphoma risk; chemotherapy hypersensitivity in BS requires dose reduction in treatment."
  - target: 01-human/03-molecular/apc
    relation: connects-to
    note: "APC heterozygosity is vulnerable to crossover-mediated LOH in BLM-deficient cells → biallelic APC LOF without a second mutation → colorectal adenoma; GI carcinomas dominate the adult BS cancer spectrum; colonoscopy surveillance from age 15 is a management cornerstone."
  - target: 01-human/03-molecular/mlh1
    relation: connects-to
    note: "BLM interacts with MLH1 (MMR) via its N-terminal region; BLM-MLH1 cooperation suppresses microsatellite instability; BLM unwinds heteroduplex DNA during MMR; some BS GI cancers show MSI-H — dual HR + MMR defect may contribute to extreme GI carcinoma risk."
  - target: 01-human/07-system/dicer1-syndrome
    relation: connects-to
    note: "Bloom and DICER1 are both childhood cancer-predisposition syndromes but mechanistically unrelated: Bloom is genomic instability from a defective BLM helicase (high sister-chromatid exchange), DICER1 faulty microRNA processing — broken DNA repair versus gene dysregulation."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "The diagnostic hallmark of Bloom syndrome is a sun-sensitive facial rash: telangiectatic erythema in a butterfly distribution across the cheeks and nose that flares with UV exposure, reflecting cells that cannot properly repair replication-associated DNA damage."
  - target: 01-human/07-system/all
    relation: connects-to
    note: "Leukemia, especially acute lymphoblastic and myeloid, is the earliest and most common cancer in Bloom syndrome, often in childhood; the BLM-deficient genomic instability also makes these patients hypersensitive to chemotherapy, forcing substantial dose reductions."
  - target: 01-human/07-system/werner-syndrome
    relation: connects-to
    note: "Bloom and Werner syndrome are both RecQ-helicase disorders of genomic instability: Bloom (BLM) causes sister-chromatid exchange, sun-sensitive rash, short stature and early cancers, while Werner (WRN) causes premature aging and sarcomas—RecQ members whose loss destabilizes DNA."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Leukemia is a leading Bloom-syndrome cancer: the BLM helicase defect causes extreme chromosomal instability and sister-chromatid exchange, so AML and ALL arise at strikingly young ages, and—because Bloom cells are hypersensitive to DNA-damaging agents—chemo doses must be reduced."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Bloom syndrome is markedly photosensitive: BLM helicase loss leaves cells unable to resolve replication stress, so ultraviolet photons readily cause the characteristic sun-exposed facial erythema (butterfly rash) and add to the cancer risk—patients need strict sun protection."
  - target: 01-human/07-system/rothmund-thomson
    relation: connects-to
    note: "Bloom syndrome and Rothmund-Thomson are RecQ-helicase genome-instability disorders: Bloom (BLM), Rothmund-Thomson (RECQL4), and Werner (WRN) share defective DNA helicases causing chromosomal instability, growth failure, and high cancer risk."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Bloom syndrome carries a strikingly high rate of early type 2 diabetes: despite low body weight, severe insulin resistance develops, so diabetes appears in childhood—part of a broad phenotype of growth deficiency, immunodeficiency, and cancer from BLM helicase loss."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Bloom syndrome includes an immunodeficiency: BLM helicase loss impairs lymphocyte development and antibody class-switching, causing low immunoglobulins and recurrent respiratory and ear infections—so immune failure compounds the genome instability driving its cancers."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Bloom and Li-Fraumeni are both inherited genome-instability cancer syndromes by different routes: Bloom from BLM helicase loss causing excess recombination, Li-Fraumeni from p53 loss removing the damage checkpoint—both flood cells with mutations driving cancer."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "Bloom syndrome cells struggle to engage p53-driven safeguards: without BLM helicase, stalled forks and excess sister-chromatid exchange overwhelm the damage response, so the p53 checkpoint cannot keep pace—explaining the broad, early cancer risk of the syndrome."
  - target: 01-human/03-molecular/rad51
    relation: connects-to
    note: "BLM helicase partners with RAD51 in homologous recombination: BLM normally dissolves recombination intermediates that RAD51 forms, preventing crossovers, so its loss causes the hallmark surge in sister-chromatid exchange that defines Bloom syndrome diagnostically."
  - target: 01-human/03-molecular/brca2
    relation: connects-to
    note: "Bloom syndrome and BRCA2 cancers share a homologous-recombination theme: BLM helicase works alongside BRCA2 and RAD51 to repair DNA by recombination, so its loss—like BRCA2 loss—causes genomic instability and a broad lifelong cancer predisposition."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Bloom syndrome includes immunodeficiency: defective DNA repair impairs B-cell antibody class-switching, lowering immunoglobulins and causing recurrent infections, while the same instability fuels the lymphomas and leukemias that often arise from these cells."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Bloom syndrome impairs the reproductive system: men are typically infertile and women have reduced, early-ending fertility, reflecting how the genome instability and repair defect that drive its cancers also disrupt the meiotic recombination needed to make gametes."
  - target: 01-human/03-molecular/growth-hormone
    relation: connects-to
    note: "Bloom syndrome's most visible feature is profound short stature: BLM helicase loss stunts growth from before birth, producing proportionate dwarfism despite normal growth-hormone levels—so it is a growth disorder of the cell's replication machinery, not the hormone."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Bloom syndrome brings recurrent lung infection: an associated immunodeficiency (low immunoglobulins) leaves patients prone to pneumonia and chronic lung disease, so respiratory infections are a major cause of illness alongside the cancer risk."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Bloom syndrome carries an extreme, broad cancer risk including breast: genomic instability from BLM loss drives tumors at unusually young ages across many sites, so carriers need early, intensive surveillance for breast and other cancers."
  - target: 01-human/03-molecular/atm
    relation: connects-to
    note: "Bloom syndrome compounds a fragile genome's stress response: BLM helicase untangles stalled replication forks that ATM and ATR guard, so losing BLM forces these damage-sensing kinases to work overtime—and the resulting instability fuels the syndrome's many cancers."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Bloom syndrome includes immune deficiency: many patients have low IgG and other antibodies, causing recurrent ear, sinus, and lung infections—an immunodeficiency layered on top of the cancer risk from defective DNA repair."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Bloom syndrome impairs T-cell help: defective DNA repair hampers the lymphocyte proliferation behind antibody class-switching, so weak T-helper support contributes to the low immunoglobulins and recurrent infections these patients suffer."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Oxidative damage compounds Bloom syndrome's repair defect: with the BLM helicase gone, cells handle DNA breaks poorly, so reactive oxygen species and sunlight add lesions the cell cannot fix—fueling the genomic instability and cancer risk."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Bloom syndrome carries a steep colorectal cancer risk: the failed DNA repair lets mutations accumulate in the gut lining, so these patients develop bowel cancers young and need early, frequent colonoscopy among their many tumor risks."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Bloom syndrome is diagnosed in the fibroblast: cultured cells reveal sharply elevated sister-chromatid exchange, the cytogenetic fingerprint of BLM helicase loss that distinguishes it from other DNA-repair disorders."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Bloom syndrome makes the marrow turn leukemic: its runaway genomic instability seeds mutations in blood-forming cells, so leukemias and lymphomas arise from the bone marrow at strikingly young ages."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Bloom syndrome burdens the pancreas: patients commonly develop diabetes as the gland's insulin output falters, and their broad cancer predisposition includes pancreatic tumors among many sites."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Bloom syndrome dims immune surveillance: a mild immunodeficiency weakens natural killer and antibody responses, leaving patients prone to infections and less able to cull the cancerous cells their unstable DNA spawns."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Bloom syndrome's butterfly facial rash is vascular: sun exposure dilates dermal endothelial-lined vessels into the telangiectatic erythema across the cheeks that marks the disease."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Bloom syndrome's commonest cancers strike the gut lining: the unstable DNA of the intestinal epithelium spawns early colorectal and other GI cancers, demanding cancer surveillance from a young age."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Bloom syndrome's universal cancer risk includes the liver: its profound genomic instability predisposes to tumors across the body, hepatocellular carcinoma among the many sites."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Bloom syndrome cannot mend its own DNA: the broken BLM helicase lets chromosomes swap arms in a flurry of sister-chromatid exchanges — the diagnostic hallmark — and leaves cells hypersensitive to radiation and oxidative damage."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Sunlight inflames the Bloom syndrome face and eyes: the photosensitive butterfly rash of dilated telangiectatic vessels spreads across the cheeks and onto the conjunctiva, a visible sign of the disorder's UV sensitivity."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Bloom syndrome's cancer spectrum reaches the kidney: among the many tumors its genomic instability invites, Wilms tumor and renal carcinoma occur, so the kidney joins the broad lifelong cancer surveillance."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Bloom syndrome leaves the body short of antibody: a common variable immunodeficiency-like drop in immunoglobulins accompanies it, so recurrent ear, sinus, and lung infections trouble these patients from childhood."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "The diagnosis is read in the blood cells: Bloom's faulty BLM helicase produces a striking excess of sister-chromatid exchanges in cultured lymphocytes — the classic confirmatory test — while marrow failure can also drop the red cells into anemia."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "The gut troubles span a lifetime: severe reflux and feeding difficulty stunt growth in Bloom infants, and the genomic instability later raises the risk of gastric and other gastrointestinal cancers."
  - target: 01-human/06-organ/thymus
    relation: connects-to
    note: "Bloom syndrome comes with immune deficiency: poor antibody responses and reduced thymus-derived T-cell function leave children prone to recurrent ear, sinus and lung infections, part of why infections rival cancer as a cause of early death."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Bloom bodies resist insulin: many patients develop insulin resistance and early type 2 diabetes despite their small, lean frames, a metabolic derangement tied to the syndrome that adds to its lifelong health burden."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Bloom's failing immunity meets its cancer risk: weakened cytotoxic T-cell surveillance lets genomically unstable, mutation-riddled cells slip past immune killing, compounding the extraordinary lifetime cancer predisposition that defines the syndrome."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "The growth axis runs low in Bloom: despite normal growth hormone, low IGF-1 signaling underlies the profound pre- and postnatal growth deficiency that gives these patients their characteristic small, lean stature."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "The unstable genome breaks first in the marrow: Bloom syndrome's chromosomal instability drives myelodysplastic syndromes and leukemia at strikingly young ages, among the earliest of its many cancers."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Antibody output runs short: Bloom's immunodeficiency includes poor plasma-cell function and low immunoglobulin levels, leaving patients prone to the recurrent respiratory and ear infections of childhood."
  - target: 01-human/07-system/esophageal-cancer
    relation: connects-to
    note: "Adult Bloom patients face carcinomas of the gut lining: the genomic instability that brings early leukemia later drives GI carcinomas including esophageal cancer, part of the syndrome's relentless lifelong cancer toll."
  - target: 01-human/07-system/wilms-tumor
    relation: connects-to
    note: "The embryonal tumors appear in childhood: Bloom syndrome's chromosomal instability predisposes to Wilms tumor among other paediatric cancers, reflecting how broadly the loss of BLM helicase destabilizes the genome."
  - target: 01-human/03-molecular/msh2
    relation: connects-to
    note: "BLM works alongside mismatch repair: the BLM helicase cooperates with the MSH2-containing mismatch-repair machinery to resolve recombination intermediates, so its loss compounds the genomic instability that mismatch-repair defects also cause."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Relentless DNA damage smolders into inflammation: the unrepaired breaks and replication stress of Bloom syndrome trigger DNA-sensing inflammatory signaling that activates NF-κB, a chronic inflammatory tone layered on its cancer risk."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "A faltering immune system invites infection: Bloom syndrome includes an immunodeficiency with low immunoglobulins, so recurrent respiratory and gastrointestinal infections — and the sepsis they can become — are a major cause of illness."
  - target: 01-human/07-system/cervical-cancer
    relation: connects-to
    note: "Its cancer net is wide and starts early: Bloom syndrome's genomic instability and immunodeficiency raise the risk of carcinomas including HPV-driven cervical cancer, part of a remarkably broad, young-onset cancer spectrum."
  - target: 01-human/07-system/copd
    relation: connects-to
    note: "Recurrent lung infection scars the airways: the immunodeficiency of Bloom syndrome causes repeated respiratory infections that can lead to bronchiectasis and chronic obstructive lung disease over time."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Infection, cancer and marrow strain lower the count: chronic infections, the disease's many malignancies and bone-marrow involvement combine to produce an anemia of chronic disease in Bloom syndrome."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A lifetime of cancer and illness weighs on the mind: living with profound cancer predisposition, recurrent infection, short stature and lifelong surveillance carries a substantial psychological burden in Bloom syndrome."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: connects-to
    note: "Its immunodeficiency invites recurrent infection: Bloom syndrome includes an antibody deficiency that leaves patients prone to recurrent respiratory and ear infections, often pneumococcal."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Immune defects and cancer therapy open the lung to mold: the immunodeficiency of Bloom syndrome, compounded by chemotherapy for its frequent cancers, can permit invasive aspergillosis."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Its DNA-repair defect makes tissue fragile to treatment: Bloom cells are hypersensitive to chemotherapy and radiation, so the doses used against its cancers cause severe tissue damage and poor healing."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Sunlight inflames its skin: Bloom syndrome causes a photosensitive telangiectatic butterfly erythema across the face, along with café-au-lait macules and a raised risk of skin cancer."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It stunts growth and disturbs metabolism: Bloom syndrome features severe proportionate short stature, and patients develop diabetes and hypogonadism with subfertility, tying it to the endocrine system."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Profound cancer risk breeds worry: the chromosomal instability and very high lifetime malignancy risk of Bloom syndrome demand lifelong surveillance that fosters chronic health anxiety."
---

# Bloom Syndrome

## Overview

**Bloom syndrome (BS)** is a rare autosomal recessive **chromosomal instability syndrome** caused by biallelic loss-of-function mutations in the **BLM** gene (15q26.1), encoding the BLM RecQ helicase that dissolves double Holliday junctions (dHJs) to suppress crossover during homologous recombination. Bloom syndrome was first described by dermatologist David Bloom in 1954, who reported children with sun-sensitive telangiectatic facial erythema and small body size. The BLM gene was positionally cloned by Ellis et al. in 1995. The **Bloom Syndrome Registry (BSR)**, established by James German at Weill Cornell Medical College and ongoing for >60 years, has registered >300 patients from >40 countries and provides the primary epidemiological and cancer incidence dataset for BS [^ellis-1995-blm-cloning] [^german-1997-bloom-cancer].

BS is characterized by three cardinal features: **small body size** (the most consistent feature — all BS patients are substantially below the 3rd percentile for height and weight throughout life; not corrected by GH treatment), **sun-sensitive telangiectatic facial erythema** (butterfly-distribution erythema over nose/cheeks/lips, exacerbated by sun exposure, without photodamage; telangiectasias develop by 1-2 years), and **immunodeficiency** (reduced serum IgA, IgM; T-cell dysfunction; recurrent sinopulmonary infections). The **cytogenetic hallmark** is dramatically elevated **sister chromatid exchanges (SCE): ~10-fold higher** than in normal cells (50-100 SCEs/metaphase vs ~5-10 normal), the diagnostic gold standard. **Pan-cancer predisposition** affecting virtually every organ system is the dominant clinical threat in adults — arising from unconstrained crossover-mediated loss of heterozygosity (LOH) at tumor suppressor loci throughout the genome.

**Bloom syndrome vs. related chromosomal instability syndromes:**

| Feature | Bloom Syndrome (BLM) | Werner Syndrome (WRN) | Fanconi Anemia (FANC genes) |
|---|---|---|---|
| Inheritance | AR | AR | AR (XL for FANCB) |
| Age of onset | Birth | 3rd decade | Childhood |
| SCE | ~10x elevated | ~2-3x elevated | Normal (elevated breaks) |
| Hallmark cytogenetic | Elevated SCE | Variegated translocations | Radial chromosomes, DSBs |
| Cancer risk | Pan-cancer (ALL, lymphoma, GI) | Sarcomas, melanoma, thyroid | AML, squamous cell carcinoma |
| Skin | Sun-sensitive telangiectasia | Scleroderma-like, ulcers | Café-au-lait, hyperpigmentation |
| Immunodeficiency | Yes (IgA/IgM low) | Mild | Yes (bone marrow failure) |
| Median survival | ~26-30 years | ~47-54 years | Variable (marrow transplant) |

## Structure

### Genetic basis of Bloom syndrome

**BLM gene (15q26.1):**
- 22 exons; 1,417 aa; 159 kDa; ubiquitously expressed, highest in proliferating tissues
- All disease-causing BLM mutations result in loss of helicase activity, BTR complex assembly, or nuclear localization
- Over 70 distinct germline BLM mutations identified; diverse spectrum (nonsense, frameshift, missense in helicase core, splice site)

**blmAsh Ashkenazi Jewish founder mutation:**
- c.2207_2212delATCTGAinsTAGATTC: 6-bp deletion + 7-bp insertion in exon 10 → net +1 frameshift → premature stop codon at aa 740 → truncated non-functional protein
- Carrier frequency ~1/48,000 in Ashkenazi Jewish population; responsible for ~80% of Bloom syndrome in Ashkenazi families
- allele-specific PCR detects blmAsh; included in expanded Ashkenazi carrier panels (alongside HEXA, CFTR, FANCC)
- Non-Ashkenazi mutations: compound heterozygotes common; diverse mutations throughout BLM

**Somatic BLM reversion (diagnostic pitfall):**
- In BS cells (with ~10x elevated SCE), intragenic recombination can restore one BLM allele to wild-type within a clone → somatic mosaic revertant clones with normal SCE and growth advantage → overgrow BS cells in blood
- Clinical implication: a negative BLM gene test or normal SCE in blood does not exclude BS; must test fibroblasts or hair roots if blood results are discordant with clinical features

**Prevalence:**
- Estimated <1/1,000,000 worldwide; most concentrated in Ashkenazi Jewish populations; BSR has >300 registered patients since 1960

### Cytogenetics of Bloom syndrome

**SCE assay — diagnostic gold standard:**
- Cells cultured for two replication cycles in BrdU (bromodeoxyuridine) → sister chromatids differentially labeled (one strand BrdU-substituted) → metaphase spread staining (Hoechst 33258 + Giemsa) → sister chromatids differentially fluorescent → crossover exchanges (SCEs) visible as points where fluorescence switches between sister chromatids
- Normal human cells: ~5-10 SCEs/metaphase
- Bloom syndrome: ~50-100 SCEs/metaphase (~10x elevated; highly reproducible across tissues and age)
- Specificity: SCE ≥50/metaphase is specific for BLM LOF; WRN LOF (~2-3x), BRCA1/2 LOF, and other HR defects do NOT generate this degree of SCE elevation
- Diagnosis: SCE ≥50/metaphase in compatible clinical context = diagnostic; BLM molecular confirmation follows

**Additional cytogenetic findings:**
- Quadriradial chromosomes: four-armed chromosomal configurations from crossover between homologous chromosomes (non-sister); pathognomonic of BS when observed
- Elevated chromatid breaks and gaps
- Elevated numerical aberrations in some cell lineages

## Function

### Clinical features of Bloom syndrome

**Small body size (~100% penetrance):**
- The most consistent and defining feature; average adult height ~147-153 cm; average adult weight significantly below normal
- NOT caused by growth hormone deficiency (GH axis intact; GH treatment ineffective) — reflects intrinsic cellular replication defect
- Low birth weight (~2.5 kg typical); does not catch up with age

**Sun-sensitive facial erythema (~90% penetrance):**
- Telangiectatic erythema in butterfly distribution over nose, cheeks, ears, lower lip; exacerbated by sun exposure; develops 1-3 years of age
- Does NOT involve photodamage (no actinic keratoses, no photoaging — unlike xeroderma pigmentosum); biopsy shows telangiectasias and mild dermal inflammation
- ANA negative (distinguishes from lupus); strict sun avoidance and SPF 50+ sunscreen from infancy

**Immunodeficiency:**
- Reduced serum IgA (~90% of patients); reduced serum IgM (~60%); IgG often low-normal
- Variable T-cell dysfunction; CD4+ lymphopenia in some; NK cell reduction in some
- Clinical: recurrent sinopulmonary infections (otitis media, sinusitis, pneumonia) in childhood
- Management: prophylactic IgG replacement for severely hypogammaglobulinemic patients; antibiotic prophylaxis for recurrent infections

**Additional features:**
- Narrow elongated facies with prominent ears and retrognathia; characteristic but not severe dysmorphia
- Male infertility: azoospermia nearly universal (testes small; Sertoli-cell-only pattern on histology); female infertility: premature ovarian failure (~20-30 years); both sexes severely infertile
- High-pitched voice: laryngeal hypoplasia in many patients
- Diabetes mellitus: subset of older patients; mixed etiology (autoimmune T1DM, Type 3c from chronic pancreatitis, or T2DM-like insulin resistance)
- Normal intelligence: intellectual disability NOT typical (distinguishes BS from Seckel, Cockayne, Fanconi anemia with brain involvement)

### Cancer in Bloom syndrome

**Cancer spectrum (BSR data, >200 cancers in >300 patients) [^german-1997-bloom-cancer]:**
- Leukemia (AML/ALL): most common in first two decades; AML > ALL; ~50-100x general population risk; median age ~25 years for AML/ALL in BSR data
- Non-Hodgkin lymphoma: substantial risk in 3rd-4th decades; Burkitt lymphoma reported
- Gastrointestinal carcinomas: colorectal, gastric, esophageal, small bowel — dominant adult malignancy; colonoscopic surveillance from ~15 years
- Skin carcinomas (BCC, SCC): elevated lifetime risk; immune dysregulation + possible sun-skin interaction
- Breast cancer: elevated; early onset
- Other: lung, oral, cervical, bladder — virtually all carcinoma types have excess risk
- **Pan-cancer phenotype**: no organ is spared; reflects systemic LOH acceleration at all heterozygous tumor suppressor loci throughout the genome

**Cancer mechanism:**
- BLM LOF → unconstrained crossover → crossover-mediated LOH throughout the genome → when a heterozygous tumor suppressor allele undergoes crossover → distal LOH → biallelic TS LOF without additional mutation → tumor initiation
- Every BS patient has a unique background of heterozygous single-nucleotide variants across the genome; LOH can expose TS alleles at many loci → broad, non-tissue-specific predisposition
- Biallelic TS silencing by LOH is ~100x faster in BS cells than normal, because elevated SCE = elevated crossover frequency

## Pathology

### Diagnosis

**Diagnostic approach:**
1. **Clinical suspicion**: small body size + sun-sensitive facial erythema + immunodeficiency + Ashkenazi Jewish background OR family history of cancer → refer for SCE assay
2. **SCE assay (gold standard)**: blood lymphocytes or fibroblasts; ≥50 SCEs/metaphase in compatible clinical context = diagnostic for Bloom syndrome
3. **Molecular confirmation**: BLM sequencing + MLPA; in Ashkenazi patients, blmAsh allele-specific PCR first; compound heterozygotes common in non-Ashkenazi
4. **Pitfall — somatic reversion**: if blood SCE normal but clinical suspicion high, test fibroblasts (skin biopsy) or hair roots; somatic revertant clones in blood can normalize SCE

**Differential diagnosis:**
- Lupus erythematosus: butterfly rash but ANA+, photodamage present, SCE normal, size normal
- Xeroderma pigmentosum: sun sensitivity with photodamage, photoaging, SCE normal, NER deficiency (XPA-XPG genes)
- Fanconi anemia: chromosomal instability presenting as pancytopenia, radial chromosomes (not SCE), ICL sensitivity, FANC gene panel
- Werner syndrome: progeroid adult onset, scleroderma-like skin, SCE only ~2-3x elevated, normal childhood
- Rothmund-Thomson syndrome (RECQL4): poikiloderma from infancy, skeletal abnormalities, osteosarcoma; SCE not elevated
- Seckel syndrome (ATR): microcephaly, intellectual disability; SCE normal

**Surveillance protocol:**
- Annual CBC with differential: leukemia (AML, ALL) surveillance — lifelong from diagnosis
- Annual upper and lower GI endoscopy: from ~15 years; colorectal carcinoma most common adult malignancy
- Annual dermatological exam: skin carcinoma, rare melanoma
- Annual breast MRI/mammogram: from ~25 years
- Regular lymph node assessment: lymphoma surveillance
- Minimize CT scans (ionizing radiation sensitivity) — use MRI where feasible

**Treatment and management:**
- No disease-modifying therapy; management is surveillance and standard cancer treatment
- Chemotherapy sensitivity: BS cells hypersensitive to DNA crosslinkers (cisplatin, mitomycin C, cyclophosphamide) because BLM is required for interstrand crosslink (ICL) repair; dose reduction considerations for hematologic malignancies
- Radiation sensitivity: minimize therapeutic radiation; avoid unless essential; reduce diagnostic imaging
- IgG replacement therapy: for severe hypogammaglobulinemia with recurrent infections; IVIg or subcutaneous IgG
- Sun avoidance and SPF 50+ sunscreen: reduces facial erythema; lifelong
- Genetic counseling: AR inheritance; sibling recurrence 1/4; prenatal diagnosis by CVS/amniocentesis; Ashkenazi Jewish carrier screening includes blmAsh
- Registry: Bloom Syndrome Association and BSR — research cohort participation; clinical coordination; genetic counseling referral

## Connections

- `connects-to` → **[BLM](../../03-molecular/blm/README.md)** — Biallelic BLM LOF → Bloom syndrome via crossover accumulation and SCE elevation (~10x); chromosomal instability → LOH at tumor suppressor loci → pan-cancer predisposition (ALL, lymphoma, GI carcinoma, skin); Bloom Syndrome Registry has tracked >300 patients for >60 years.
- `connects-to` → **[BRCA1](../../03-molecular/brca1/README.md)** — BLM and BRCA1 form a complex at stalled replication forks to suppress aberrant homologous recombination and resolve Holliday junctions; both BLM LOF and BRCA1 LOF result in chromosomal instability and pan-cancer predisposition via distinct but overlapping HR defects.
- `connects-to` → **[WRN](../../03-molecular/wrn/README.md)** — BLM and WRN are both RecQ helicases: BLM resolves double Holliday junctions to suppress crossover (SCE elevated ~10x in BLM LOF); WRN has exonuclease activity and maintains telomeres; BLM LOF → childhood-onset pan-cancer; WRN LOF → adult progeroid syndrome.
- `connects-to` → **[Colorectal Cancer](../../07-system/colorectal-cancer/README.md)** — BLM LOF in Bloom syndrome confers elevated colorectal cancer risk due to crossover-mediated LOH at APC and other CRC tumor suppressor loci; GI carcinomas are among the most common malignancies in adult Bloom syndrome patients; colonoscopy surveillance from early adulthood.
- `connects-to` → **[Burkitt Lymphoma](../../07-system/burkitt-lymphoma/README.md)** — Burkitt lymphoma and NHL are among the most common lymphoid malignancies in Bloom syndrome; crossover-mediated LOH at 8q24 (MYC) contributes; BS patients have ~50-100× elevated lymphoma risk; chemotherapy hypersensitivity in BS requires dose reduction.
- `connects-to` → **[APC](../../03-molecular/apc/README.md)** — APC heterozygosity is vulnerable to crossover-mediated LOH in BLM-deficient cells → biallelic APC LOF without a second mutation → colorectal adenoma initiation; GI carcinomas dominate the adult BS cancer spectrum; colonoscopy from age 15 is a management cornerstone.
- `connects-to` → **[MLH1](../../03-molecular/mlh1/README.md)** — BLM interacts with MLH1 (MMR); BLM-MLH1 cooperation suppresses microsatellite instability; BLM unwinds heteroduplex DNA during MMR; some BS GI cancers show MSI-H — dual HR + MMR defect may contribute to extreme GI carcinoma risk.
- `connects-to` → **[DICER1 Syndrome](../dicer1-syndrome/README.md)** — Bloom and DICER1 are both childhood cancer-predisposition syndromes but mechanistically unrelated: Bloom is genomic instability from a defective BLM helicase (high sister-chromatid exchange), DICER1 faulty microRNA processing — broken DNA repair versus gene dysregulation.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — The diagnostic hallmark of Bloom syndrome is a sun-sensitive facial rash: telangiectatic erythema in a butterfly distribution across the cheeks and nose that flares with UV exposure, reflecting cells that cannot properly repair replication-associated DNA damage.
- `connects-to` → **[Acute Lymphoblastic Leukemia](../all/README.md)** — Leukemia, especially acute lymphoblastic and myeloid, is the earliest and most common cancer in Bloom syndrome, often in childhood; the BLM-deficient genomic instability also makes these patients hypersensitive to chemotherapy, forcing substantial dose reductions.
- `connects-to` → **[Werner Syndrome](../werner-syndrome/README.md)** — Bloom and Werner syndrome are both RecQ-helicase disorders of genomic instability: Bloom (BLM) causes sister-chromatid exchange, sun-sensitive rash, short stature and early cancers, while Werner (WRN) causes premature aging and sarcomas—RecQ members whose loss destabilizes DNA.
- `connects-to` → **[AML](../aml/README.md)** — Leukemia is a leading Bloom-syndrome cancer: the BLM helicase defect causes extreme chromosomal instability and sister-chromatid exchange, so AML and ALL arise at strikingly young ages, and—because Bloom cells are hypersensitive to DNA-damaging agents—chemo doses must be reduced.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Bloom syndrome is markedly photosensitive: BLM helicase loss leaves cells unable to resolve replication stress, so ultraviolet photons readily cause the characteristic sun-exposed facial erythema (butterfly rash) and add to the cancer risk—patients need strict sun protection.
- `connects-to` → **[Rothmund-Thomson Syndrome](../rothmund-thomson/README.md)** — Bloom syndrome and Rothmund-Thomson are RecQ-helicase genome-instability disorders: Bloom (BLM), Rothmund-Thomson (RECQL4), and Werner (WRN) share defective DNA helicases causing chromosomal instability, growth failure, and high cancer risk.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Bloom syndrome carries a strikingly high rate of early type 2 diabetes: despite low body weight, severe insulin resistance develops, so diabetes appears in childhood—part of a broad phenotype of growth deficiency, immunodeficiency, and cancer from BLM helicase loss.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Bloom syndrome includes an immunodeficiency: BLM helicase loss impairs lymphocyte development and antibody class-switching, causing low immunoglobulins and recurrent respiratory and ear infections—so immune failure compounds the genome instability driving its cancers.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Bloom and Li-Fraumeni are both inherited genome-instability cancer syndromes by different routes: Bloom from BLM helicase loss causing excess recombination, Li-Fraumeni from p53 loss removing the damage checkpoint—both flood cells with mutations driving cancer.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — Bloom syndrome cells struggle to engage p53-driven safeguards: without BLM helicase, stalled forks and excess sister-chromatid exchange overwhelm the damage response, so the p53 checkpoint cannot keep pace—explaining the broad, early cancer risk of the syndrome.
- `connects-to` → **[RAD51](../../03-molecular/rad51/README.md)** — BLM helicase partners with RAD51 in homologous recombination: BLM normally dissolves recombination intermediates that RAD51 forms, preventing crossovers, so its loss causes the hallmark surge in sister-chromatid exchange that defines Bloom syndrome diagnostically.
- `connects-to` → **[BRCA2](../../03-molecular/brca2/README.md)** — Bloom syndrome and BRCA2 cancers share a homologous-recombination theme: BLM helicase works alongside BRCA2 and RAD51 to repair DNA by recombination, so its loss—like BRCA2 loss—causes genomic instability and a broad lifelong cancer predisposition.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — Bloom syndrome includes immunodeficiency: defective DNA repair impairs B-cell antibody class-switching, lowering immunoglobulins and causing recurrent infections, while the same instability fuels the lymphomas and leukemias that often arise from these cells.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Bloom syndrome impairs the reproductive system: men are typically infertile and women have reduced, early-ending fertility, reflecting how the genome instability and repair defect that drive its cancers also disrupt the meiotic recombination needed to make gametes.
- `connects-to` → **[Growth Hormone](../../03-molecular/growth-hormone/README.md)** — Bloom syndrome's most visible feature is profound short stature: BLM helicase loss stunts growth from before birth, producing proportionate dwarfism despite normal growth-hormone levels—so it is a growth disorder of the cell's replication machinery, not the hormone.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Bloom syndrome brings recurrent lung infection: an associated immunodeficiency (low immunoglobulins) leaves patients prone to pneumonia and chronic lung disease, so respiratory infections are a major cause of illness alongside the cancer risk.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — Bloom syndrome carries an extreme, broad cancer risk including breast: genomic instability from BLM loss drives tumors at unusually young ages across many sites, so carriers need early, intensive surveillance for breast and other cancers.
- `connects-to` → **[ATM](../../03-molecular/atm/README.md)** — Bloom syndrome compounds a fragile genome's stress response: BLM helicase untangles stalled replication forks that ATM and ATR guard, so losing BLM forces these damage-sensing kinases to work overtime—and the resulting instability fuels the syndrome's many cancers.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Bloom syndrome includes immune deficiency: many patients have low IgG and other antibodies, causing recurrent ear, sinus, and lung infections—an immunodeficiency layered on top of the cancer risk from defective DNA repair.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Bloom syndrome impairs T-cell help: defective DNA repair hampers the lymphocyte proliferation behind antibody class-switching, so weak T-helper support contributes to the low immunoglobulins and recurrent infections these patients suffer.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Oxidative damage compounds Bloom syndrome's repair defect: with the BLM helicase gone, cells handle DNA breaks poorly, so reactive oxygen species and sunlight add lesions the cell cannot fix—fueling the genomic instability and cancer risk.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Bloom syndrome carries a steep colorectal cancer risk: the failed DNA repair lets mutations accumulate in the gut lining, so these patients develop bowel cancers young and need early, frequent colonoscopy among their many tumor risks.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Bloom syndrome is diagnosed in the fibroblast: cultured cells reveal sharply elevated sister-chromatid exchange, the cytogenetic fingerprint of BLM helicase loss that distinguishes it from other DNA-repair disorders.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Bloom syndrome makes the marrow turn leukemic: its runaway genomic instability seeds mutations in blood-forming cells, so leukemias and lymphomas arise from the bone marrow at strikingly young ages.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Bloom syndrome burdens the pancreas: patients commonly develop diabetes as the gland's insulin output falters, and their broad cancer predisposition includes pancreatic tumors among many sites.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Bloom syndrome dims immune surveillance: a mild immunodeficiency weakens natural killer and antibody responses, leaving patients prone to infections and less able to cull the cancerous cells their unstable DNA spawns.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Bloom syndrome's butterfly facial rash is vascular: sun exposure dilates dermal endothelial-lined vessels into the telangiectatic erythema across the cheeks that marks the disease.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Bloom syndrome's commonest cancers strike the gut lining: the unstable DNA of the intestinal epithelium spawns early colorectal and other GI cancers, demanding cancer surveillance from a young age.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Bloom syndrome's universal cancer risk includes the liver: its profound genomic instability predisposes to tumors across the body, hepatocellular carcinoma among the many sites.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Bloom syndrome cannot mend its own DNA: the broken BLM helicase lets chromosomes swap arms in a flurry of sister-chromatid exchanges — the diagnostic hallmark — and leaves cells hypersensitive to radiation and oxidative damage.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Sunlight inflames the Bloom syndrome face and eyes: the photosensitive butterfly rash of dilated telangiectatic vessels spreads across the cheeks and onto the conjunctiva, a visible sign of the disorder's UV sensitivity.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Bloom syndrome's cancer spectrum reaches the kidney: among the many tumors its genomic instability invites, Wilms tumor and renal carcinoma occur, so the kidney joins the broad lifelong cancer surveillance.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Bloom syndrome leaves the body short of antibody: a common variable immunodeficiency-like drop in immunoglobulins accompanies it, so recurrent ear, sinus, and lung infections trouble these patients from childhood.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — The diagnosis is read in the blood cells: Bloom's faulty BLM helicase produces a striking excess of sister-chromatid exchanges in cultured lymphocytes — the classic confirmatory test — while marrow failure can also drop the red cells into anemia.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — The gut troubles span a lifetime: severe reflux and feeding difficulty stunt growth in Bloom infants, and the genomic instability later raises the risk of gastric and other gastrointestinal cancers.
- `connects-to` → **[Thymus](../../06-organ/thymus/README.md)** — Bloom syndrome comes with immune deficiency: poor antibody responses and reduced thymus-derived T-cell function leave children prone to recurrent ear, sinus and lung infections, part of why infections rival cancer as a cause of early death.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Bloom bodies resist insulin: many patients develop insulin resistance and early type 2 diabetes despite their small, lean frames, a metabolic derangement tied to the syndrome that adds to its lifelong health burden.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Bloom's failing immunity meets its cancer risk: weakened cytotoxic T-cell surveillance lets genomically unstable, mutation-riddled cells slip past immune killing, compounding the extraordinary lifetime cancer predisposition that defines the syndrome.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — The growth axis runs low in Bloom: despite normal growth hormone, low IGF-1 signaling underlies the profound pre- and postnatal growth deficiency that gives these patients their characteristic small, lean stature.
- `connects-to` → **[Myelodysplastic Syndromes](../mds/README.md)** — The unstable genome breaks first in the marrow: Bloom syndrome's chromosomal instability drives myelodysplastic syndromes and leukemia at strikingly young ages, among the earliest of its many cancers.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Antibody output runs short: Bloom's immunodeficiency includes poor plasma-cell function and low immunoglobulin levels, leaving patients prone to the recurrent respiratory and ear infections of childhood.
- `connects-to` → **[Esophageal Cancer](../esophageal-cancer/README.md)** — Adult Bloom patients face carcinomas of the gut lining: the genomic instability that brings early leukemia later drives GI carcinomas including esophageal cancer, part of the syndrome's relentless lifelong cancer toll.
- `connects-to` → **[Wilms Tumor](../wilms-tumor/README.md)** — The embryonal tumors appear in childhood: Bloom syndrome's chromosomal instability predisposes to Wilms tumor among other paediatric cancers, reflecting how broadly the loss of BLM helicase destabilizes the genome.
- `connects-to` → **[MSH2](../../03-molecular/msh2/README.md)** — BLM works alongside mismatch repair: the BLM helicase cooperates with the MSH2-containing mismatch-repair machinery to resolve recombination intermediates, so its loss compounds the genomic instability that mismatch-repair defects also cause.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Relentless DNA damage smolders into inflammation: the unrepaired breaks and replication stress of Bloom syndrome trigger DNA-sensing inflammatory signaling that activates NF-κB, a chronic inflammatory tone layered on its cancer risk.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — A faltering immune system invites infection: Bloom syndrome includes an immunodeficiency with low immunoglobulins, so recurrent respiratory and gastrointestinal infections — and the sepsis they can become — are a major cause of illness.
- `connects-to` → **[Cervical Cancer](../cervical-cancer/README.md)** — Its cancer net is wide and starts early: Bloom syndrome's genomic instability and immunodeficiency raise the risk of carcinomas including HPV-driven cervical cancer, part of a remarkably broad, young-onset cancer spectrum.
- `connects-to` → **[COPD](../copd/README.md)** — Recurrent lung infection scars the airways: the immunodeficiency of Bloom syndrome causes repeated respiratory infections that can lead to bronchiectasis and chronic obstructive lung disease over time.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Infection, cancer and marrow strain lower the count: chronic infections, the disease's many malignancies and bone-marrow involvement combine to produce an anemia of chronic disease in Bloom syndrome.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A lifetime of cancer and illness weighs on the mind: living with profound cancer predisposition, recurrent infection, short stature and lifelong surveillance carries a substantial psychological burden in Bloom syndrome.
- `connects-to` → **[Streptococcus pneumoniae](../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — Its immunodeficiency invites recurrent infection: Bloom syndrome includes an antibody deficiency that leaves patients prone to recurrent respiratory and ear infections, often pneumococcal.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Immune defects and cancer therapy open the lung to mold: the immunodeficiency of Bloom syndrome, compounded by chemotherapy for its frequent cancers, can permit invasive aspergillosis.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Its DNA-repair defect makes tissue fragile to treatment: Bloom cells are hypersensitive to chemotherapy and radiation, so the doses used against its cancers cause severe tissue damage and poor healing.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Sunlight inflames its skin: Bloom syndrome causes a photosensitive telangiectatic butterfly erythema across the face, along with café-au-lait macules and a raised risk of skin cancer.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It stunts growth and disturbs metabolism: Bloom syndrome features severe proportionate short stature, and patients develop diabetes and hypogonadism with subfertility, tying it to the endocrine system.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Profound cancer risk breeds worry: the chromosomal instability and very high lifetime malignancy risk of Bloom syndrome demand lifelong surveillance that fosters chronic health anxiety.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^ellis-1995-blm-cloning]: Ellis NA, Groden J, Ye TZ, et al. The Bloom's syndrome gene product is homologous to RecQ helicases. *Cell.* 1995;83(4):655-666. [doi:10.1016/0092-8674(95)90105-1](https://doi.org/10.1016/0092-8674(95)90105-1) · [PubMed 7585968](https://pubmed.ncbi.nlm.nih.gov/7585968/)
[^german-1997-bloom-cancer]: German J. Bloom's syndrome. XX. The first 100 cancers. *Cancer.* 1997;71(12):4016-4023. [doi:10.1002/1097-0142(19930615)71:12<4016::AID-CNCR18>3.0.CO;2-E](https://doi.org/10.1002/1097-0142(19930615)71:12<4016::AID-CNCR18>3.0.CO;2-E) · [PubMed 9216035](https://pubmed.ncbi.nlm.nih.gov/9216035/)

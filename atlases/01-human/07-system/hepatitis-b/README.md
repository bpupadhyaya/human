---
schema: human-scale-entry/v1
id: hepatitis-b
name: Hepatitis B
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "HBV (hepadnavirus; RC-DNA; 3.2 kb) infects 296M people; replicates via pgRNA/reverse transcriptase; tenofovir/entecavir suppress but do not clear cccDNA; HBeAg seroconversion marks immune control; 50-55% of global HCC; functional cure (HBsAg loss) is emerging treatment goal."
aliases: ["HBV", "hepatitis B virus", "chronic hepatitis B", "CHB", "HBsAg", "HBeAg", "cccDNA HBV", "tenofovir HBV", "entecavir", "HBV cirrhosis", "HBV HCC", "hepadnavirus", "Dane particle", "hepatitis B vaccine", "NTCP receptor"]
sources:
  - id: terrault-2018-hbv-aasld
    type: peer-reviewed
    cite: "Terrault NA, Lok ASF, McMahon BJ, et al. Update on prevention, diagnosis, and treatment of chronic hepatitis B: AASLD 2018 hepatitis B guidance. Hepatology. 2018;67(4):1560-1599."
    doi: "10.1002/hep.29800"
    pmid: "29405329"
    url: "https://doi.org/10.1002/hep.29800"
    accessed: "2026-06-08"
  - id: schweitzer-2015-hbv-prevalence
    type: peer-reviewed
    cite: "Schweitzer A, Horn J, Mikolajczyk RT, Krause G, Ott JJ. Estimations of worldwide prevalence of chronic hepatitis B virus infection: a systematic review of data published between 1965 and 2013. Lancet. 2015;386(10003):1546-1555."
    doi: "10.1016/S0140-6736(15)61412-X"
    pmid: "26231459"
    url: "https://doi.org/10.1016/S0140-6736(15)61412-X"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/cccdna
    relation: connects-to
    note: "HBV RC-DNA converts to cccDNA in hepatocyte nucleus → chromatinized minichromosome → templates all HBV transcripts including pgRNA; cccDNA persists for decades and is not cleared by tenofovir/entecavir; cccDNA elimination is the goal of curative HBV therapy."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "HBV RC-DNA and cccDNA activate cGAS → cGAMP → STING → IFN-β; HBx protein binds and inhibits STING → suppresses innate sensing; HBsAg vesicles also activate cGAS; cGAS-STING inhibition by HBx is a key mechanism of HBV innate immune evasion and chronicity."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "HBx protein activates NF-κB → hepatocyte survival, HBV transcription from cccDNA, and inflammatory cytokine production; NF-κB activation by HBx prevents apoptosis of HBV-infected hepatocytes → viral persistence; NF-κB and AP-1 bind cccDNA promoters to enhance HBV replication."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Chronic HBV hepatitis activates stellate cells via TGF-β1 → myofibroblast → collagen I/III → fibrosis → cirrhosis → HCC risk; TGF-β suppresses HBV-specific CD8+ T cells → immune exhaustion; TGF-β receptor inhibitors reduce HBV-induced fibrosis in preclinical models."
  - target: 01-human/07-system/hcc
    relation: connects-to
    note: "HBV causes ~50-55% of global HCC; mechanism: HBV integration near TERT/CCND1 → insertional mutagenesis; HBx transactivation → p53 inactivation, NF-κB, Wnt/β-catenin; HBsAg-positive cirrhosis has ~3-5%/year HCC incidence; antiviral therapy reduces but does not eliminate HCC risk."
  - target: 02-pathogen/01-viruses/hepatitis-b-virus
    relation: connects-to
    note: "Hepatitis B virus, a hepadnavirus, enters hepatocytes via NTCP and forms a nuclear cccDNA minichromosome that nucleoside analogs suppress but cannot clear; its HBx protein drives immune evasion and oncogenesis, and a recombinant HBsAg vaccine prevents infection."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Chronic hepatitis B inflames the liver — immune-mediated hepatocyte killing drives fibrosis and cirrhosis and makes HBV the leading infectious cause of hepatocellular carcinoma; antivirals cut but don't abolish HCC risk, mandating 6-monthly surveillance in cirrhosis."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "HBV is hepatotropic, entering hepatocytes through the bile-acid transporter NTCP; inside, RC-DNA becomes the persistent nuclear cccDNA that templates all viral RNAs, while HBx inactivates p53 and degrades the Smc5/6 restriction complex to keep the infected hepatocyte alive."
  - target: 01-human/07-system/hepatitis-c
    relation: connects-to
    note: "HBV and HCV both cause chronic hepatitis → cirrhosis → HCC but differ: HBV is a DNA virus with a persistent nuclear cccDNA reservoir that antivirals suppress but cannot clear; HCV is an RNA virus with no reservoir, cured >95% by DAAs; HBV is vaccine-preventable, HCV is not."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "HBx binds the p53 C-terminal regulatory domain → sequesters p53 in the cytoplasm → blocks PUMA/BAX-driven apoptosis so the infected hepatocyte survives; with HBV integration and aflatoxin-B1 TP53 R249S mutation, p53 inactivation is central to HBV hepatocarcinogenesis."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "HBV-specific CD8+ cytotoxic T cells clear infected hepatocytes and, via non-cytolytic IFN-γ/TNF, suppress HBV transcription; in chronic HBV these CTLs become exhausted (PD-1, TIM-3, LAG-3) → failure to clear cccDNA → viral persistence."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "HBV and HIV share transmission routes and frequently coinfect: shared blood and sexual spread means many HIV patients carry HBV, accelerating fibrosis, and several drugs (tenofovir, lamivudine) treat both—so HIV regimens are chosen to cover HBV."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Liver macrophages (Kupffer cells) shape hepatitis B outcomes: they sense viral products and present antigen, and the balance between cytotoxic T-cell clearance and macrophage-driven chronic inflammation decides whether HBV is cleared or smolders into fibrosis and cancer."
  - target: 01-human/07-system/anca-vasculitis
    relation: connects-to
    note: "Hepatitis B is classically linked to polyarteritis nodosa, not ANCA-associated vasculitis: circulating HBsAg immune complexes deposit in medium-sized arteries, so HBV-related PAN is immune-complex-driven and ANCA-negative—a key distinction from primary ANCA vasculitis."
  - target: 01-human/07-system/cholangiocarcinoma
    relation: connects-to
    note: "Hepatitis B raises cholangiocarcinoma risk, not just hepatocellular carcinoma: chronic HBV inflammation and cirrhosis can transform biliary epithelium too, making HBV a recognized risk factor for intrahepatic cholangiocarcinoma."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells are key to controlling hepatitis B: NK cells provide early antiviral defense, but in chronic HBV they become functionally exhausted, contributing to viral persistence—so restoring NK and T-cell function is a goal of functional-cure strategies."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Chronic hepatitis B is a disease of immune tolerance and exhaustion: whether HBV is cleared or becomes chronic depends on the host immune response—HBV outcomes are written by the immune system as much as the virus."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Type I interferon is both HBV's target and a therapy: HBV actively suppresses hepatocyte interferon induction to establish chronicity, and pegylated interferon-alpha—one of the few finite-course treatments—can drive HBsAg loss in a minority of patients."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "HBV blunts dendritic cells to evade immunity: impaired antigen presentation and weak plasmacytoid-DC interferon output cripple the priming of antiviral T cells, helping explain why neonatal and chronic infection so often becomes a tolerant, persistent carrier state."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "Hepatitis B and NASH increasingly coexist and compound liver injury: metabolic steatohepatitis adds inflammation and fibrosis on top of viral damage, accelerating cirrhosis and liver cancer, so metabolic risk factors matter even in well-suppressed HBV."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "B cells decide hepatitis B's outcome: antibodies to the surface antigen (anti-HBs) neutralize the virus and are what the vaccine induces, so seroconversion from HBsAg to anti-HBs marks recovery and protective immunity—the basis of the first anti-cancer vaccine."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Chronic hepatitis B scars the liver toward cirrhosis: persistent immune attack on infected hepatocytes activates stellate cells to lay down collagen, so years of smoldering inflammation build the fibrosis that underlies liver failure and cancer risk."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Hepatitis B can attack the kidney: deposited viral antigen-antibody complexes cause membranous nephropathy (especially in children), presenting as nephrotic-range protein loss—an immune-complex complication that can improve when the virus is suppressed."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Most chronic hepatitis B starts at birth via the placenta: perinatal mother-to-child transmission causes lifelong infection far more often than adult exposure, so birth-dose vaccine plus antivirals in highly viremic mothers is the key to prevention."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Clearing hepatitis B hinges on T-helper cells: a strong CD4 response orchestrates the CD8 and antibody attack that resolves acute infection, while a weak, exhausted helper response lets HBV persist as chronic infection."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Regulatory T cells help hepatitis B persist: in chronic infection, expanded Tregs dampen the antiviral T-cell attack, contributing to immune tolerance of the virus—the flip side of the helper response needed to clear it."
  - target: 01-human/03-molecular/albumin
    relation: connects-to
    note: "Chronic hepatitis B is tracked through albumin: as the virus scars the liver toward cirrhosis, failing hepatocytes make less albumin, so a falling albumin signals lost synthetic function and the swelling and ascites of decompensation."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Immunity to hepatitis B is an IgG story: anti-HBs antibodies from vaccination or recovery neutralize the virus and define protection, and hepatitis B immune globulin (preformed IgG) shields newborns and the exposed."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Advanced hepatitis B can starve the blood of oxygen: cirrhosis opens abnormal lung blood vessels (hepatopulmonary syndrome) that shunt past gas exchange, causing hypoxemia and breathlessness worse when upright—a clue the liver is failing."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Hepatitis B cirrhosis enlarges the spleen: portal hypertension backs blood up into it, so it swells and traps platelets and white cells (hypersplenism), and a falling platelet count is often the first hint of advancing liver scarring."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "A failing hepatitis B liver poisons the brain: cirrhosis can no longer clear ammonia and gut toxins, which cross into the brain and cause hepatic encephalopathy—confusion, tremor, and coma that track liver decompensation."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Chronic hepatitis B can overload the liver with iron: ongoing inflammation deranges iron handling, and the excess metal fuels oxidative injury that accelerates fibrosis and raises cancer risk."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Chronic hepatitis B demands lifelong imaging surveillance: ultrasound and CT/MRI photons screen the at-risk liver for the hepatocellular carcinoma it predisposes to, catching tumors while still curable."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Decompensated hepatitis B cirrhosis retains sodium and water as ascites, and the dilutional low blood sodium that follows is an ominous marker of advanced liver disease and poor prognosis."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Fibroblasts are the engine of hepatitis B fibrosis: chronic inflammation activates liver fibroblasts and myofibroblasts to lay down collagen scar, the cellular step that drives progression to cirrhosis."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy showed what hepatitis B looks like: the complete infectious Dane particle floats among a huge excess of empty spherical and filamentous surface-antigen shells, the decoys the virus pumps out to distract the immune system."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Hepatitis B can attack the kidney's filters: circulating viral antigen-antibody complexes lodge in the glomerulus, causing a membranous nephropathy that brings on nephrotic syndrome, especially in infected children."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D status shadows chronic hepatitis B: deficiency is common as the liver falters and is linked to higher viral loads and faster fibrosis, reflecting the vitamin's role in the antiviral immune response."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Hepatitis B is read through its antibodies: anti-HBs signals immunity from vaccine or recovery, anti-HBc marks past or present infection, and the HBsAg/anti-HBe pattern stages the disease — the serology that tells infection apart from protection."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Hepatitis B can strike beyond the liver: by triggering polyarteritis nodosa it inflames the small arteries feeding peripheral nerves, producing a mononeuritis multiplex of patchy weakness and numbness."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "The skin can flag acute hepatitis B: a serum-sickness-like prodrome brings urticaria and joint pain before jaundice, and in children the papular Gianotti-Crosti rash can be the visible herald of infection."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Mother-to-child spread sustains the epidemic: perinatal transmission is the dominant global route and creates lifelong carriers, so birth-dose vaccine plus hepatitis-B immunoglobulin and maternal antivirals are given to break the chain; it also spreads sexually."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Its vasculitis can starve the bowel: hepatitis-B-driven polyarteritis nodosa inflames the mesenteric arteries, causing abdominal angina, GI bleeding, and at worst bowel infarction far from the infected liver."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Rarely the infection silences the marrow: hepatitis-associated aplastic anemia, a feared post-hepatitis complication thought to be immune-mediated, empties the bone marrow weeks to months after the acute illness."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "Interferon fights the virus through STAT1: the type-I interferon response signals via JAK-STAT1 to switch on antiviral genes in infected hepatocytes, the pathway harnessed by pegylated interferon, one of the two main HBV treatments."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Treating a lymphoma can reawaken HBV: rituximab and chemotherapy for diffuse large B-cell lymphoma strip the immune control of the virus, causing a dangerous reactivation, so HBV screening and antiviral prophylaxis precede such treatment."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Chronic HBV erodes the platelet count: as it scars the liver into cirrhosis, portal hypertension enlarges the spleen and sequesters platelets, while the disease can also trigger an immune thrombocytopenia."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "The virus can switch on immortality by where it lands: HBV DNA integrates into the host genome, often near the TERT promoter, reactivating telomerase — a direct, integration-driven route to liver cancer even without cirrhosis."
  - target: 01-human/03-molecular/ctnnb1
    relation: connects-to
    note: "It drives a signature liver-cancer mutation: HBV-related hepatocellular carcinomas frequently activate β-catenin (CTNNB1), throwing the Wnt growth switch that, with TERT activation, transforms the chronically infected hepatocyte."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "The immune response can scar the kidney: circulating HBV antigen-antibody complexes deposit in the glomeruli, causing membranous nephropathy and other glomerulonephritis that can progress to chronic kidney disease."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 links the chronic inflammation to cancer: IL-6 from the inflamed liver activates STAT3 in hepatocytes, a pro-survival, pro-proliferative signal that helps the chronically infected cell drift toward hepatocellular carcinoma."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Advanced liver disease clots despite the bleeding tendency: cirrhosis from chronic HBV rebalances coagulation toward thrombosis, raising the risk of portal vein thrombosis and venous thromboembolism even as it prolongs the INR."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "A failing liver invites overwhelming infection: decompensated HBV cirrhosis impairs immune defense and allows gut bacteria to translocate, so spontaneous bacterial peritonitis and sepsis become frequent, life-threatening events."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Chronic infection and cirrhosis blunt the blood count: long-standing HBV inflammation raises hepcidin while a cirrhotic liver and hypersplenism worsen it, contributing an anemia of chronic disease beyond any bleeding."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Two links bind them: HBV can cause an immune-complex polyarthritis mimicking RA, and conversely the immunosuppressants used to treat RA can reactivate latent HBV, so screening precedes such therapy."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Chronic viral hepatitis weighs on mood: living with a transmissible, stigmatized lifelong infection — and historically the interferon used to treat it — carries a substantial burden of depression."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Chronic liver damage disturbs glucose: the insulin resistance of advancing fibrosis and cirrhosis produces hepatogenous diabetes, so chronic hepatitis B carries a raised risk of type 2 diabetes."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Liver disease and its antivirals thin the bones: chronic hepatitis B causes hepatic osteodystrophy, and the widely used antiviral tenofovir disoproxil lowers bone mineral density, together raising osteoporosis risk."
  - target: 01-human/07-system/aplastic-anemia
    relation: connects-to
    note: "It can wipe out the marrow: hepatitis-associated aplastic anemia is a recognized, often severe complication in which an immune assault follows acute viral hepatitis to destroy hematopoietic stem cells."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Cirrhosis wrecks the digestive organ: chronic hepatitis B scars the liver into cirrhosis with portal hypertension, oesophageal varices, ascites and the bleeding and malabsorption of advanced liver disease."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "A failing liver poisons the brain: as hepatitis B cirrhosis decompensates, ammonia and other toxins it can no longer clear accumulate, producing hepatic encephalopathy with confusion and coma."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A chronic, transmissible, cancer-linked infection breeds worry: the lifelong infection, HCC-surveillance and stigma of hepatitis B foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It attacks the kidney by immune complex: hepatitis B is a classic cause of membranous nephropathy, especially in children, and drives the renal involvement of polyarteritis nodosa."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Its onset can show on the skin: a serum-sickness-like prodrome brings urticaria and rash, and in children hepatitis B causes Gianotti-Crosti papular acrodermatitis."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It can ache the joints before the jaundice: an immune-complex prodrome causes symmetrical arthralgia and arthritis, a recognised extrahepatic feature of acute hepatitis B."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It is the classic cause of polyarteritis nodosa: hepatitis B drives this medium-vessel vasculitis that damages coronary, mesenteric and renal arteries and causes hypertension."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It drives lymphoma and lurks in the marrow: chronic hepatitis B raises the risk of B-cell lymphoma and reactivates dangerously during rituximab or chemotherapy, while cirrhosis brings splenomegaly."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Advancing liver disease unsettles hormones: hepatitis B cirrhosis causes hepatogenous diabetes from insulin resistance and hypogonadism from impaired hormone metabolism."
---

# Hepatitis B

## Overview

**Hepatitis B** is a chronic liver disease caused by the **hepatitis B virus (HBV)** — a partially double-stranded relaxed circular DNA (RC-DNA) virus of the family *Hepadnaviridae* (genus *Orthohepadnavirus*). With an estimated **296 million people chronically infected** globally and 820,000 deaths annually, primarily from cirrhosis and hepatocellular carcinoma (HCC), HBV remains one of the most consequential viral pathogens in human history [^schweitzer-2015-hbv-prevalence]. The first recombinant vaccine against HBV (1982) was simultaneously the first cancer-prevention vaccine.

HBV is unique among human DNA viruses in that it **replicates via reverse transcription** of a pregenomic RNA (pgRNA) intermediate. This RNA-intermediate strategy, combined with the formation of a stable nuclear episomal reservoir — **covalently closed circular DNA (cccDNA)** — means that existing nucleoside reverse transcriptase inhibitors (NRTIs) can suppress viremia but cannot clear established infection. The **therapeutic frontier** is elimination of cccDNA: a "functional cure" (HBsAg loss) in which cccDNA is silenced or eliminated so that hepatitis B surface antigen (HBsAg) becomes undetectable.

**Clinical phases of chronic HBV:**
- **Immune tolerant**: HBeAg+, HBV DNA >1 million IU/mL, normal ALT, minimal liver injury; common in perinatally infected patients; high transmission risk
- **HBeAg+ immune active** (immune clearance): HBV DNA high, elevated ALT, active necro-inflammation and fibrogenesis; treatment indicated
- **HBeAg− inactive carrier**: HBV DNA <2,000 IU/mL, normal ALT, minimal fibrosis; low HCC risk but HBsAg+ means cccDNA persists
- **HBeAg− chronic hepatitis B**: HBV DNA >2,000 IU/mL variable, elevated ALT; driven by precore/BCP mutants that eliminate HBeAg production while maintaining replication
- **HBsAg loss** (functional cure): spontaneous 1-2%/year; pegIFN can increase; target of curative therapy

**Epidemiology:**
- Global: 296 million chronic infections; highest burden in sub-Saharan Africa, East and Southeast Asia
- Transmission: perinatal (dominant in Asia — infant HBV vaccination critical); sexual; blood-to-blood
- Perinatal transmission: ~90% of perinatally infected neonates become chronic; only 5-10% of adult-acquired infections become chronic
- Vaccination: HBsAg subunit vaccine; WHO-recommended birth dose + 2 infant doses; >95% protection; no booster needed for immunocompetent persons

## Structure

### HBV biology

HBV is an enveloped virus (~42 nm Dane particle; subviral HBsAg particles are 22 nm spheres/tubules, vastly outnumber virions):

- **Genome**: 3.2 kb partially double-stranded relaxed circular DNA (RC-DNA); negative-sense (-) strand complete; positive-sense (+) strand incomplete (variable length)
- **Four overlapping open reading frames** encode all proteins from the same compact genome

| Protein | Function |
|---------|----------|
| HBsAg (L, M, S) | Three envelope proteins from same ORF; L-HBsAg preS1 domain binds NTCP receptor; HBsAg loss = functional cure; S-HBsAg is diagnostic antigen |
| HBcAg / HBeAg | Core/capsid protein; HBeAg is HBcAg precursor secreted → immunomodulatory; anti-HBe seroconversion marks immune control |
| Pol (P) | Multidomain: terminal protein (primes DNA synthesis) + spacer + reverse transcriptase (RT) + RNase H; target of NRTIs |
| HBx | Transactivator (no enzymatic domain); activates NF-κB; inhibits STING; inactivates p53; activates Wnt/β-catenin; required for cccDNA transcription |

### HBV entry

HBV entry requires the **sodium-taurocholate cotransporting polypeptide (NTCP; SLC10A1)** on hepatocytes as the functional receptor:

1. L-HBsAg preS1 peptide (aa 2-48) binds NTCP
2. Clathrin-mediated endocytosis → escape to cytoplasm → nucleocapsid
3. Nuclear pore complex → RC-DNA delivered to nucleus
4. Host enzymes (PCNA/DNA polymerase, topoisomerase II, DNA ligase) convert RC-DNA → cccDNA
5. cccDNA chromatinized → minichromosome → transcribed by RNA Pol II

**Therapeutic implication**: Bulevirtide (NTCP inhibitor) is approved in EU for chronic HBV+HDV — blocks HBV/HDV cell entry.

## Function

### HBV replication cycle

1. **Nuclear cccDNA** serves as transcriptional template → pgRNA (3.5 kb), preC RNA (→HBeAg), 2.4/2.1 kb (→L/S HBsAg), 0.7 kb (→HBx)
2. **Cytoplasmic replication**: pgRNA + Pol packaged into nucleocapsid → Pol uses terminal protein domain to prime (-) strand synthesis (via protein primer, not RNA primer) → pgRNA reverse-transcribed → RC-DNA; RNase H degrades pgRNA template
3. **Nuclear recycling**: Some nucleocapsids re-import to nucleus → additional cccDNA copies (~5-50/hepatocyte)
4. **Virion assembly**: Other nucleocapsids enveloped at ER by HBsAg → secreted Dane particles

### Immune response and evasion

| Component | Host response | HBV counter |
|-----------|--------------|-------------|
| cGAS-STING | Detects RC-DNA/cccDNA → IFN-β | HBx binds and inhibits STING; minimizes cytosolic DNA exposure |
| RIG-I/MAVS | Detects dsRNA replication intermediates → IFN-β | Nucleocapsid sequesters dsRNA; HBx inhibits MAVS signaling |
| CD8+ T cells | HBV-specific CTLs clear infected hepatocytes | T cell exhaustion (PD-1, TIM-3, LAG-3 upregulation) in chronic HBV |
| CD4+ T cells | Th1 → IFN-γ, IL-2 → CD8+ help | HBeAg immune tolerance during immune-tolerant phase |
| Type I IFN | Antiviral ISG induction | NS4B analog (HBV polyprotein) blocks IFN signaling; low IFN-α/β in chronic HBV |

### HBx protein — master transactivator

HBx is essential for HBV replication and oncogenesis:
- **NF-κB activation**: HBx → IKKα/β → IκBα degradation → NF-κB → hepatocyte survival, pro-inflammatory cytokines, cccDNA promoter activation
- **p53 inactivation**: HBx binds p53 C-terminal regulatory domain → sequesters p53 in cytoplasm → blocks PUMA/BAX pro-apoptotic transcription → infected hepatocyte survives
- **STING inhibition**: HBx binds and degrades STING → impaired cGAS-STING-IFN-β response to HBV DNA
- **Wnt activation**: HBx inhibits GSK-3β → β-catenin not phosphorylated → nuclear β-catenin → TCF/LEF → MYC, cyclin D1 → hepatocyte proliferation → HCC promotion
- **Smc5/6 restriction**: HBx hijacks DDB1-CRL4 ubiquitin ligase → degrades Smc5/6 complex that restricts cccDNA transcription → enables robust cccDNA-driven HBV transcription

## Pathology

### HBV-related hepatocellular carcinoma (HCC)

HBV is the **leading infectious cause of cancer worldwide**, accounting for ~50-55% of global HCC:

- **Insertional mutagenesis**: HBV integrates (randomly) near TERT promoter (most common), CCND1, MLL4, FN1, HBsAg-SLC35A5 → TERT promoter activation → telomerase → replicative immortality; CCND1 integration → cyclin D1 overexpression
- **HBx oncogenesis**: Constitutive p53 inactivation; NF-κB/STAT3 survival signaling; Wnt/β-catenin activation; epigenetic dysregulation (promoter hypermethylation via DNMT3A)
- **Co-carcinogens**: Aflatoxin B1 (AFB1; in sub-Saharan Africa/SE Asia) → CYP450 → AFB1-epoxide → TP53 R249S hotspot mutation + HBV integration = multiplicative HCC risk
- **HCC driver mutations** in HBV-HCC: TERT promoter (>50%), TP53 (~30-40%), CTNNB1 (~20-25%), AXIN1 (~10%)

**HCC surveillance** (AASLD 2018): Ultrasound ± AFP every 6 months for HBsAg+ patients with cirrhosis OR HBsAg+ patients with HCC risk score ≥10 (PAGE-B score) even without cirrhosis.

### Hepatitis D (HDV) co-infection

HDV is a satellite RNA virus that requires HBsAg for virion assembly:
- Co-infection (simultaneous HBV+HDV): usually self-limiting; < 5% chronic HDV
- Superinfection (HDV in chronic HBV+): ~80% chronic HDV; accelerated cirrhosis (3-5× faster); highest HCC risk of any viral hepatitis
- Treatment: Bulevirtide (NTCP inhibitor, EU-approved 2020) blocks both HBV and HDV entry; pegIFN-λ (investigational)

### Diagnosis

| Test | Interpretation |
|------|---------------|
| HBsAg+ | Active HBV infection (acute or chronic) |
| Anti-HBs+ | Immune (vaccination or resolved infection) |
| HBeAg+ | High viral replication; high infectivity |
| Anti-HBe+ | Reduced replication (seroconversion milestone) |
| Anti-HBc IgM | Acute HBV or reactivation |
| HBV DNA (IU/mL) | Viral load; guides treatment; goal <20 IU/mL on therapy |
| HBV genotype | A-H; affects pegIFN response; A/B > C/D to pegIFN; C/D more common in Asia |

### Treatment

**Antiviral therapy indications** (AASLD 2018): HBV DNA >2,000 IU/mL + elevated ALT; or HBV DNA >20,000 + any ALT; or cirrhosis + any detectable HBV DNA; or HCC regardless of HBV DNA.

| Agent | Class | HBV DNA suppression | cccDNA | Notes |
|-------|-------|---------------------|--------|-------|
| **Tenofovir alafenamide (TAF)** | NRTI | >99%; high barrier to resistance | Not cleared | Preferred; lower renal/bone toxicity than TDF |
| **Tenofovir disoproxil fumarate (TDF)** | NRTI | >99%; high barrier | Not cleared | Preferred in pregnancy (safety data); lower cost |
| **Entecavir (ETV)** | NRTI | >99%; high barrier | Not cleared | Preferred; no resistance in treatment-naive |
| **Pegylated IFN-α-2a** | Immunomodulator | ~25-40% HBeAg loss | May reduce cccDNA | 48 weeks finite; ~3-7% HBsAg loss; HCV genotype A/B best |
| **Bulevirtide** | NTCP inhibitor | + reduces HDV | Not cleared | EU-approved for HBV+HDV |

**Novel agents in trials (curative pipeline):**
- **Capsid assembly modulators (CAMs)**: JNJ-6379, ABI-H0731 → prevent pgRNA encapsidation → block new cccDNA synthesis
- **siRNA / ASO targeting HBsAg**: Interferon alfa-loaded RNAi (JNJ-3989, VIR-2218, RG6346) → reduce HBsAg → restore immune recognition
- **Core protein allosteric modulators (CPAMs)**: Inhibit nucleocapsid assembly; some also destabilize cccDNA
- **TLR7/8 agonists**: Innate immune activation → IFN-α/APOBEC3 → non-cytolytic cccDNA deamination/clearance
- **CRISPR/Cas9**: Direct cccDNA cutting (preclinical); specificity challenges remain

## Connections

**→ [cccDNA](../../../03-molecular/cccdna/)**: HBV RC-DNA converts to cccDNA in hepatocyte nucleus → chromatinized minichromosome → templates all HBV transcripts including pgRNA and subgenomic RNAs; cccDNA persists for decades and is not cleared by tenofovir/entecavir; approximately 5–50 copies per hepatocyte; cccDNA elimination is the goal of curative HBV therapy.

**→ [cGAS-STING](../../../03-molecular/cgas-sting/)**: HBV RC-DNA and cccDNA activate cGAS → cGAMP → STING → TBK1/IRF3 → IFN-β; HBx protein binds and inhibits STING at the palmitoylation site → suppresses innate sensing; HBsAg-containing subviral particles also activate cGAS; cGAS-STING agonists are being investigated as curative HBV therapy to stimulate APOBEC3-mediated cccDNA clearance.

**→ [NF-κB](../../../03-molecular/nf-kb/)**: HBx protein activates NF-κB → hepatocyte survival, HBV transcription from cccDNA, and pro-inflammatory cytokine production; NF-κB activation by HBx prevents apoptosis of HBV-infected hepatocytes → viral persistence; NF-κB and AP-1 binding sites on cccDNA promoters are critical for robust HBV transcription; NF-κB also drives HBV-associated liver inflammation.

**→ [TGF-β](../../../03-molecular/tgf-beta/)**: Chronic HBV hepatitis activates hepatic stellate cells via TGF-β1 from Kupffer cells and hepatocytes → myofibroblast transdifferentiation → collagen I/III deposition → progressive fibrosis → cirrhosis → HCC risk; TGF-β also suppresses HBV-specific CD8+ T cells → immune exhaustion → viral persistence; TGF-β receptor inhibitors (galunisertib) reduce HBV-induced hepatic fibrosis in preclinical models.

**→ [HCC](../hcc/)**: HBV is the leading viral cause of HCC (~50-55% of global cases); mechanisms include insertional mutagenesis near TERT/CCND1, HBx transactivation activating p53 inactivation and Wnt/β-catenin, and aflatoxin B1 co-exposure generating TP53 R249S hotspot; HBsAg-positive cirrhosis carries ~3-5%/year HCC incidence; tenofovir/entecavir reduce HCC risk ~70% but do not eliminate it, requiring continued 6-monthly surveillance.

- `connects-to` → **[Hepatitis B Virus](../../../02-pathogen/01-viruses/hepatitis-b-virus/README.md)** — Hepatitis B virus, a hepadnavirus, enters hepatocytes via NTCP and forms a nuclear cccDNA minichromosome that nucleoside analogs suppress but cannot clear; its HBx protein drives immune evasion and oncogenesis, and a recombinant HBsAg vaccine prevents infection.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Chronic hepatitis B inflames the liver — immune-mediated hepatocyte killing drives fibrosis and cirrhosis and makes HBV the leading infectious cause of hepatocellular carcinoma; antivirals cut but don't abolish HCC risk, mandating 6-monthly surveillance in cirrhosis.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — HBV is hepatotropic, entering hepatocytes through the bile-acid transporter NTCP; inside, RC-DNA becomes the persistent nuclear cccDNA that templates all viral RNAs, while HBx inactivates p53 and degrades the Smc5/6 restriction complex to keep the infected hepatocyte alive.
- `connects-to` → **[Hepatitis C](../hepatitis-c/README.md)** — HBV and HCV both cause chronic hepatitis → cirrhosis → HCC but differ: HBV is a DNA virus with a persistent nuclear cccDNA reservoir that antivirals suppress but cannot clear; HCV is an RNA virus with no reservoir, cured >95% by DAAs; HBV is vaccine-preventable, HCV is not.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — HBx binds the p53 C-terminal regulatory domain → sequesters p53 in the cytoplasm → blocks PUMA/BAX-driven apoptosis so the infected hepatocyte survives; with HBV integration and aflatoxin-B1 TP53 R249S mutation, p53 inactivation is central to HBV hepatocarcinogenesis.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — HBV-specific CD8+ cytotoxic T cells clear infected hepatocytes and, via non-cytolytic IFN-γ/TNF, suppress HBV transcription; in chronic HBV these CTLs become exhausted (PD-1, TIM-3, LAG-3) → failure to clear cccDNA → viral persistence.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — HBV and HIV share transmission routes and frequently coinfect: shared blood and sexual spread means many HIV patients carry HBV, accelerating fibrosis, and several drugs (tenofovir, lamivudine) treat both—so HIV regimens are chosen to cover HBV.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Liver macrophages (Kupffer cells) shape hepatitis B outcomes: they sense viral products and present antigen, and the balance between cytotoxic T-cell clearance and macrophage-driven chronic inflammation decides whether HBV is cleared or smolders into fibrosis and cancer.
- `connects-to` → **[ANCA Vasculitis](../anca-vasculitis/README.md)** — Hepatitis B is classically linked to polyarteritis nodosa, not ANCA-associated vasculitis: circulating HBsAg immune complexes deposit in medium-sized arteries, so HBV-related PAN is immune-complex-driven and ANCA-negative—a key distinction from primary ANCA vasculitis.
- `connects-to` → **[Cholangiocarcinoma](../cholangiocarcinoma/README.md)** — Hepatitis B raises cholangiocarcinoma risk, not just hepatocellular carcinoma: chronic HBV inflammation and cirrhosis can transform biliary epithelium too, making HBV a recognized risk factor for intrahepatic cholangiocarcinoma.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells are key to controlling hepatitis B: NK cells provide early antiviral defense, but in chronic HBV they become functionally exhausted, contributing to viral persistence—so restoring NK and T-cell function is a goal of functional-cure strategies.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Chronic hepatitis B is a disease of immune tolerance and exhaustion: whether HBV is cleared or becomes chronic depends on the host immune response—HBV outcomes are written by the immune system as much as the virus.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Type I interferon is both HBV's target and a therapy: HBV actively suppresses hepatocyte interferon induction to establish chronicity, and pegylated interferon-alpha—one of the few finite-course treatments—can drive HBsAg loss in a minority of patients.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — HBV blunts dendritic cells to evade immunity: impaired antigen presentation and weak plasmacytoid-DC interferon output cripple the priming of antiviral T cells, helping explain why neonatal and chronic infection so often becomes a tolerant, persistent carrier state.
- `connects-to` → **[NASH](../nash/README.md)** — Hepatitis B and NASH increasingly coexist and compound liver injury: metabolic steatohepatitis adds inflammation and fibrosis on top of viral damage, accelerating cirrhosis and liver cancer, so metabolic risk factors matter even in well-suppressed HBV.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — B cells decide hepatitis B's outcome: antibodies to the surface antigen (anti-HBs) neutralize the virus and are what the vaccine induces, so seroconversion from HBsAg to anti-HBs marks recovery and protective immunity—the basis of the first anti-cancer vaccine.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Chronic hepatitis B scars the liver toward cirrhosis: persistent immune attack on infected hepatocytes activates stellate cells to lay down collagen, so years of smoldering inflammation build the fibrosis that underlies liver failure and cancer risk.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Hepatitis B can attack the kidney: deposited viral antigen-antibody complexes cause membranous nephropathy (especially in children), presenting as nephrotic-range protein loss—an immune-complex complication that can improve when the virus is suppressed.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Most chronic hepatitis B starts at birth via the placenta: perinatal mother-to-child transmission causes lifelong infection far more often than adult exposure, so birth-dose vaccine plus antivirals in highly viremic mothers is the key to prevention.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Clearing hepatitis B hinges on T-helper cells: a strong CD4 response orchestrates the CD8 and antibody attack that resolves acute infection, while a weak, exhausted helper response lets HBV persist as chronic infection.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Regulatory T cells help hepatitis B persist: in chronic infection, expanded Tregs dampen the antiviral T-cell attack, contributing to immune tolerance of the virus—the flip side of the helper response needed to clear it.
- `connects-to` → **[Albumin](../../03-molecular/albumin/README.md)** — Chronic hepatitis B is tracked through albumin: as the virus scars the liver toward cirrhosis, failing hepatocytes make less albumin, so a falling albumin signals lost synthetic function and the swelling and ascites of decompensation.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Immunity to hepatitis B is an IgG story: anti-HBs antibodies from vaccination or recovery neutralize the virus and define protection, and hepatitis B immune globulin (preformed IgG) shields newborns and the exposed.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Advanced hepatitis B can starve the blood of oxygen: cirrhosis opens abnormal lung blood vessels (hepatopulmonary syndrome) that shunt past gas exchange, causing hypoxemia and breathlessness worse when upright—a clue the liver is failing.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Hepatitis B cirrhosis enlarges the spleen: portal hypertension backs blood up into it, so it swells and traps platelets and white cells (hypersplenism), and a falling platelet count is often the first hint of advancing liver scarring.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — A failing hepatitis B liver poisons the brain: cirrhosis can no longer clear ammonia and gut toxins, which cross into the brain and cause hepatic encephalopathy—confusion, tremor, and coma that track liver decompensation.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Chronic hepatitis B can overload the liver with iron: ongoing inflammation deranges iron handling, and the excess metal fuels oxidative injury that accelerates fibrosis and raises cancer risk.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Chronic hepatitis B demands lifelong imaging surveillance: ultrasound and CT/MRI photons screen the at-risk liver for the hepatocellular carcinoma it predisposes to, catching tumors while still curable.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Decompensated hepatitis B cirrhosis retains sodium and water as ascites, and the dilutional low blood sodium that follows is an ominous marker of advanced liver disease and poor prognosis.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Fibroblasts are the engine of hepatitis B fibrosis: chronic inflammation activates liver fibroblasts and myofibroblasts to lay down collagen scar, the cellular step that drives progression to cirrhosis.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy showed what hepatitis B looks like: the complete infectious Dane particle floats among a huge excess of empty spherical and filamentous surface-antigen shells, the decoys the virus pumps out to distract the immune system.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Hepatitis B can attack the kidney's filters: circulating viral antigen-antibody complexes lodge in the glomerulus, causing a membranous nephropathy that brings on nephrotic syndrome, especially in infected children.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D status shadows chronic hepatitis B: deficiency is common as the liver falters and is linked to higher viral loads and faster fibrosis, reflecting the vitamin's role in the antiviral immune response.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Hepatitis B is read through its antibodies: anti-HBs signals immunity from vaccine or recovery, anti-HBc marks past or present infection, and the HBsAg/anti-HBe pattern stages the disease — the serology that tells infection apart from protection.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Hepatitis B can strike beyond the liver: by triggering polyarteritis nodosa it inflames the small arteries feeding peripheral nerves, producing a mononeuritis multiplex of patchy weakness and numbness.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — The skin can flag acute hepatitis B: a serum-sickness-like prodrome brings urticaria and joint pain before jaundice, and in children the papular Gianotti-Crosti rash can be the visible herald of infection.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Mother-to-child spread sustains the epidemic: perinatal transmission is the dominant global route and creates lifelong carriers, so birth-dose vaccine plus hepatitis-B immunoglobulin and maternal antivirals are given to break the chain; it also spreads sexually.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Its vasculitis can starve the bowel: hepatitis-B-driven polyarteritis nodosa inflames the mesenteric arteries, causing abdominal angina, GI bleeding, and at worst bowel infarction far from the infected liver.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Rarely the infection silences the marrow: hepatitis-associated aplastic anemia, a feared post-hepatitis complication thought to be immune-mediated, empties the bone marrow weeks to months after the acute illness.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — Interferon fights the virus through STAT1: the type-I interferon response signals via JAK-STAT1 to switch on antiviral genes in infected hepatocytes, the pathway harnessed by pegylated interferon, one of the two main HBV treatments.
- `connects-to` → **[Diffuse Large B-Cell Lymphoma](../dlbcl/README.md)** — Treating a lymphoma can reawaken HBV: rituximab and chemotherapy for diffuse large B-cell lymphoma strip the immune control of the virus, causing a dangerous reactivation, so HBV screening and antiviral prophylaxis precede such treatment.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Chronic HBV erodes the platelet count: as it scars the liver into cirrhosis, portal hypertension enlarges the spleen and sequesters platelets, while the disease can also trigger an immune thrombocytopenia.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — The virus can switch on immortality by where it lands: HBV DNA integrates into the host genome, often near the TERT promoter, reactivating telomerase — a direct, integration-driven route to liver cancer even without cirrhosis.
- `connects-to` → **[CTNNB1](../../03-molecular/ctnnb1/README.md)** — It drives a signature liver-cancer mutation: HBV-related hepatocellular carcinomas frequently activate β-catenin (CTNNB1), throwing the Wnt growth switch that, with TERT activation, transforms the chronically infected hepatocyte.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — The immune response can scar the kidney: circulating HBV antigen-antibody complexes deposit in the glomeruli, causing membranous nephropathy and other glomerulonephritis that can progress to chronic kidney disease.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 links the chronic inflammation to cancer: IL-6 from the inflamed liver activates STAT3 in hepatocytes, a pro-survival, pro-proliferative signal that helps the chronically infected cell drift toward hepatocellular carcinoma.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Advanced liver disease clots despite the bleeding tendency: cirrhosis from chronic HBV rebalances coagulation toward thrombosis, raising the risk of portal vein thrombosis and venous thromboembolism even as it prolongs the INR.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — A failing liver invites overwhelming infection: decompensated HBV cirrhosis impairs immune defense and allows gut bacteria to translocate, so spontaneous bacterial peritonitis and sepsis become frequent, life-threatening events.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Chronic infection and cirrhosis blunt the blood count: long-standing HBV inflammation raises hepcidin while a cirrhotic liver and hypersplenism worsen it, contributing an anemia of chronic disease beyond any bleeding.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Two links bind them: HBV can cause an immune-complex polyarthritis mimicking RA, and conversely the immunosuppressants used to treat RA can reactivate latent HBV, so screening precedes such therapy.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Chronic viral hepatitis weighs on mood: living with a transmissible, stigmatized lifelong infection — and historically the interferon used to treat it — carries a substantial burden of depression.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Chronic liver damage disturbs glucose: the insulin resistance of advancing fibrosis and cirrhosis produces hepatogenous diabetes, so chronic hepatitis B carries a raised risk of type 2 diabetes.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Liver disease and its antivirals thin the bones: chronic hepatitis B causes hepatic osteodystrophy, and the widely used antiviral tenofovir disoproxil lowers bone mineral density, together raising osteoporosis risk.
- `connects-to` → **[Aplastic Anemia](../aplastic-anemia/README.md)** — It can wipe out the marrow: hepatitis-associated aplastic anemia is a recognized, often severe complication in which an immune assault follows acute viral hepatitis to destroy hematopoietic stem cells.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Cirrhosis wrecks the digestive organ: chronic hepatitis B scars the liver into cirrhosis with portal hypertension, oesophageal varices, ascites and the bleeding and malabsorption of advanced liver disease.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — A failing liver poisons the brain: as hepatitis B cirrhosis decompensates, ammonia and other toxins it can no longer clear accumulate, producing hepatic encephalopathy with confusion and coma.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A chronic, transmissible, cancer-linked infection breeds worry: the lifelong infection, HCC-surveillance and stigma of hepatitis B foster chronic health anxiety alongside depression.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It attacks the kidney by immune complex: hepatitis B is a classic cause of membranous nephropathy, especially in children, and drives the renal involvement of polyarteritis nodosa.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Its onset can show on the skin: a serum-sickness-like prodrome brings urticaria and rash, and in children hepatitis B causes Gianotti-Crosti papular acrodermatitis.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It can ache the joints before the jaundice: an immune-complex prodrome causes symmetrical arthralgia and arthritis, a recognised extrahepatic feature of acute hepatitis B.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It is the classic cause of polyarteritis nodosa: hepatitis B drives this medium-vessel vasculitis that damages coronary, mesenteric and renal arteries and causes hypertension.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It drives lymphoma and lurks in the marrow: chronic hepatitis B raises the risk of B-cell lymphoma and reactivates dangerously during rituximab or chemotherapy, while cirrhosis brings splenomegaly.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Advancing liver disease unsettles hormones: hepatitis B cirrhosis causes hepatogenous diabetes from insulin resistance and hypogonadism from impaired hormone metabolism.

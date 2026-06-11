---
schema: human-scale-entry/v1
id: reproductive-system
name: Reproductive System
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-05
summary: "Gonads, ducts, and accessory glands governed by the pulsatile HPG axis (kisspeptin→GnRH→LH/FSH→sex steroids) mediating gametogenesis, sexual development, and endocrine modulation of bone, CVD, immunity, and CNS."
aliases: ["gonadal system", "genital system", "male reproductive system", "female reproductive system", "HPG axis"]
sources:
  - id: guyton-hall
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
  - id: alberts-mol-cell-biology
    type: textbook
    cite: "Alberts B, Johnson A, Lewis J, et al. Molecular Biology of the Cell. 7th ed. W.W. Norton; 2022."
    url: "https://www.ncbi.nlm.nih.gov/books/NBK26880/"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "Sex hormones modulate immunity: oestrogen ↑Th1/Th17 → female predominance of autoimmunity (SLE, RA, MS ~3:1 F:M); testosterone is immunosuppressive; oestrogen promotes B-cell survival and antibody production."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "Oestrogen is atheroprotective (↑eNOS, ↑HDL-C, ↑LDL-R); menopause → ↓E2 → ↑CVD risk; testosterone drives erythropoiesis → ↑haematocrit; both sex steroids modulate RAAS and blood pressure."
  - target: 01-human/07-system/nervous-system
    relation: modulates
    note: "E2 and progesterone receptors are in hypothalamus, limbic system, and cortex; E2 promotes synaptogenesis, neuroprotection, and serotonin turnover; E2 deficiency causes vasomotor symptoms, cognitive changes; testosterone promotes dopaminergic tone."
  - target: 01-human/06-organ/liver
    relation: modulates
    note: "Liver metabolises sex hormones (CYP3A4 oxidation, conjugation); hepatocytes produce SHBG and angiotensinogen; oestrogen ↑SHBG → ↓free testosterone; combined OCP ↑SHBG → ↓free androgens in women with hyperandrogenism."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Oestradiol (E2; CYP19A1 aromatase from ovarian granulosa cells) binds ERα/ERβ → bone protection (↑OPG→↓RANKL), cardioprotection (↑eNOS/HDL-C), CNS neuroprotection; menopause E2 deficiency → osteoporosis + ↑CVD; OCP suppresses HPG axis; HRT restores systemic effects of E2."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Testosterone (Leydig cells → CYP11A1/CYP17A1/17β-HSD3; ~7 mg/day) binds AR → anabolic (muscle, erythropoiesis) + androgenic (virilisation, spermatogenesis); 5α-reductase → DHT (prostate/skin/scalp); aromatase → E2 (bone, HPG feedback); PCOS: excess theca-cell testosterone via LH."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Hyperinsulinaemia in PCOS sensitises ovarian LH receptors → ↑theca androgen synthesis → ↑testosterone → anovulation + hirsutism; insulin directly stimulates IGF-1R on ovary; metformin reduces hepatic insulin resistance → ↓insulin → ↓androgen production → improved ovulation rates."
---

# Reproductive System

## Overview

The reproductive system encompasses the organs, ducts, glands, and endocrine axes that govern gametogenesis, fertilisation, gestation, and parturition — and, equally importantly, a hormonal signalling network (the hypothalamic-pituitary-gonadal [HPG] axis) whose products (oestrogens, androgens, progestins) exert pervasive effects on bone, the cardiovascular system, the immune system, the central nervous system, and body composition [^guyton-hall].

The reproductive system is unique in two ways: (1) it is the only system whose primary function is explicitly interindividual rather than individual survival; and (2) it is the only system with distinct male and female anatomical configurations converging on a shared endocrine regulatory architecture. Both sexes utilise the same HPG axis structure — GnRH → LH/FSH → gonadal steroids — with sex-specific feedback dynamics (negative vs. positive feedback by oestrogen), gametogenic rates (continuous spermatogenesis vs. cyclic folliculogenesis), and anatomical implementations.

## Structure

### HPG Axis — Shared Architecture

The hypothalamic-pituitary-gonadal axis is the master regulatory circuit of the entire reproductive system [^guyton-hall]:

**Kisspeptin neurons** (arcuate nucleus of hypothalamus: pulsatile "pulse generator"; anteroventral periventricular nucleus [AVPV] in females: LH surge generator) express KISS1 → secrete kisspeptin peptides (Kp-10, Kp-13, Kp-54) → bind GPR54 (kisspeptin receptor) on GnRH neurons → stimulate pulsatile GnRH release. Kisspeptin is the critical integrator of nutritional status, metabolic signals, and sex steroid feedback:
- ↓Kisspeptin in athletes/anorexia/undernutrition → ↓GnRH pulses → ↓LH/FSH → hypogonadism → amenorrhoea (females) or ↓testosterone (males)
- **MKRN3 gene** (maternally imprinted, paternally expressed): suppresses kisspeptin neuronal activity in childhood → puberty onset occurs when MKRN3 expression falls + kisspeptin activity rises

**GnRH** (gonadotropin-releasing hormone): decapeptide (10 aa); synthesised in arcuate nucleus and preoptic area; secreted in pulses (~every 60–120 min in males; varies by phase in females) into the hypothalamo-hypophyseal portal blood → anterior pituitary gonadotrophs

**Gonadotrophs**: LH and FSH secreting cells of anterior pituitary:
- **LH** (luteinizing hormone): glycoprotein heterodimer (α + LHβ); binds LHCGR on Leydig cells (males) and theca cells (females) + luteinized granulosa cells; stimulates testosterone synthesis (males) and ovulation + corpus luteum formation (females)
- **FSH** (follicle-stimulating hormone): glycoprotein heterodimer; binds FSHR on Sertoli cells (males) and granulosa cells (females); drives spermatogenesis support (males) and follicular development + aromatase expression (females)

**Feedback**:
- **Negative feedback**: sex steroids (testosterone and oestradiol [via aromatisation in males; directly in females]) and inhibin B (from Sertoli/granulosa cells) → suppress GnRH pulse frequency and LH/FSH amplitude
- **Positive feedback** (females only): high oestradiol (~200 pg/mL sustained for >36 h at midcycle) → switches from negative to positive feedback at AVPV kisspeptin neurons → massive LH surge (~10-fold above baseline) → ovulation within 36–40 hours

### Male Reproductive Anatomy

**Testes**: paired ovoid organs (~4.5 × 2.5 cm, ~20 mL volume) in the scrotum — suspended in scrotum to maintain temperature 2–4°C below core body temperature (spermatogenesis temperature-sensitive; failure in cryptorchidism = undescended testis → azoospermia + ↑germ cell tumour risk). Supplied by testicular artery (pampiniform venous plexus forms countercurrent heat exchanger) [^guyton-hall].

**Seminiferous tubules** (~250 m total length per testis): the site of spermatogenesis:
- **Sertoli cells** (nurse cells): form the blood-testis barrier (BTB) via tight junctions between adjacent Sertoli cells (claudin-11, occludin, JAM-A) — protects haploid germ cells from autoimmune attack; phagocytose residual bodies; secrete: androgen-binding protein (ABP, maintains local testosterone), inhibin B (suppresses FSH), AMH (Müllerian-inhibiting substance), GDNF/EGF (spermatogonial stem cell niche factors), transferrin, lactate (fuel for spermatocytes/spermatids). FSH → Sertoli → activates spermatogenesis
- **Spermatogenesis** takes 74 days: spermatogonial stem cells (SSCs, Adark and Apale types) → type B spermatogonia → primary spermatocyte → meiosis I → secondary spermatocyte → meiosis II → spermatid → spermiogenesis (acrosome [cap derived from Golgi, contains hyaluronidase and acrosin for zona pellucida penetration], flagellum [9+2 axoneme], mitochondrial sheath, nuclear condensation) → spermatozoa (head + midpiece + tail)

**Leydig cells** (between tubules): stimulated by LH → synthesise testosterone from cholesterol via CYP11A1 (side-chain cleavage → pregnenolone) → CYP17A1 (17α-hydroxylase/lyase → DHEA → androstenedione) → 17β-HSD3 → testosterone. ~7 mg testosterone secreted/day in young men; 95% of circulating testosterone from testes, 5% from adrenal (androstenedione → T). Total testosterone: 300–1000 ng/dL; 60% protein-bound to SHBG, 38% to albumin, 2% free (bioactive).

**Epididymis** (~6 m coiled; 12–21 days transit): sperm maturation — acquisition of progressive motility (↑CatSper Ca²⁺ channel, ↑CRISP proteins), capacitation potential; storage in tail (cauda).

**Accessory glands and seminal emission**:
- **Seminal vesicles** (70% of ejaculate volume): fructose (main carbon source for sperm), prostaglandins, seminal vesicle coagulation factors (semenogelin I/II → coagulated semen plug)
- **Prostate** (30% of ejaculate volume): PSA (prostate-specific antigen = kallikrein-3 serine protease → liquefies semenogelin), zinc-rich secretion (bacteriostatic), citric acid; prostatic fluid + sperm → semen
- **Bulbourethral (Cowper's) glands**: pre-ejaculatory mucus (alkalinises urethra, lubricates)
- **Vas deferens**: muscular duct; peristaltic contractions during emission; vasectomy severs here
- **Corpus cavernosum/spongiosum**: erectile tissue; erection = parasympathetic (S2–S4) → NOS activation → NO → sGC → cGMP → smooth muscle relaxation (MLCP dephosphorylation) → ↑arterial inflow + venous outflow restriction; PDE5 degrades cGMP → detumescence; PDE5 inhibitors (sildenafil, tadalafil) block degradation

**Testosterone metabolism**:
- **5α-reductase** (SRD5A1/2; skin, prostate, seminal vesicles, liver) → **DHT** (5α-dihydrotestosterone; 2–3× higher AR affinity than T → dominant androgen in prostate, skin, scalp [DHT → ↑follicular miniaturisation → androgenetic alopecia])
- **Aromatase** (CYP19A1; adipose, brain, bone, testes) → **oestradiol** (E2; in males ~80% from peripheral aromatisation; essential for negative feedback on HPG axis in males, bone mineral density, libido, and spermatogenesis — FSH secretion from pituitary requires E2 suppression through aromatisation of circulating T)

### Female Reproductive Anatomy

**Ovaries** (paired, almond-shaped, ~3.5 × 2 × 1 cm): site of oogenesis and sex steroid synthesis [^guyton-hall].

**Follicle stock and depletion**:
- Germ cells (oogonia) undergo mitotic expansion during fetal life → arrested in meiosis I prophase as **primary oocytes** → endowment of ~1–2 million primordial follicles at birth → ~400,000 at puberty (ongoing atresia throughout life) → ~400 ovulate over reproductive life → menopause when follicle stock depleted (~51 years mean in developed countries)

**Ovarian cycle** (28-day cycle):
- **Follicular phase** (days 1–13): FSH → cohort of primordial follicles → primary → secondary (antrum formation) → tertiary/Graafian follicle (dominant follicle); granulosa cells proliferate + express aromatase (FSH → cAMP → ↑CYP19A1) → convert theca-derived androstenedione (LH-stimulated, CYP17A1) to oestradiol → ↑E2 → positive feedback → LH surge (day ~14)
- **Ovulation** (day ~14): LH surge → cumulus oophorus expansion (hyaluronic acid, versican by PTGS2/COX-2-prostaglandin → HAS2) → follicle wall dissolution (MMP-1/9, plasminogen activator) → oocyte II + cumulus cells expelled → captured by fimbriae
- **Luteal phase** (days 15–28): granulosa + theca cells luteinize (↑lipid droplets, ↑StAR, ↑CYP11A1) → corpus luteum (CL) → progesterone (major product) + E2; P4 → secretory endometrium (↑glycogen, ↑glandular secretion → provides nidation environment for blastocyst); if no implantation → CL regression (luteolysis) after ~14 days → ↓P4/E2 → menstruation

**Fallopian tubes** (~10 cm): ciliated columnar epithelium + peristaltic smooth muscle transport the oocyte from ovary toward uterus; fertilisation normally occurs in the ampulla; cilia beat frequency modulated by E2 (↑) and P4 (↓); ectopic pregnancy when transport fails (tubal damage from PID — Chlamydia, N. gonorrhoeae — major cause).

**Uterus** (pear-shaped, ~7.5 × 5 cm nulliparous):
- **Endometrium**: functional layer shed monthly; composed of columnar epithelium + decidualized stroma; phases: proliferative (oestrogen → ↑glandular mitosis, ↑spiral arteries, ↑thickness up to 8–16 mm [functional layer]), secretory (progesterone → glandular secretion, stromal edema, decidualization, ↑LIF, IGFBP-1 → nidation-competent); menstruation: P4/E2 withdrawal → PGF2α → spiral artery vasoconstriction → endometrial ischaemia → shedding
- **Myometrium**: smooth muscle; quiescent during pregnancy via P4 → ↓gap junctions, ↑PDE; at term: ↓P4 signalling + ↑oxytocin receptors (oestrogen-induced) + ↑PGE2/PGF2α → coordinate uterine contractions (parturition)
- **Cervix**: fibrous collagen; internal os (mucus plug in pregnancy); cervical ripening at term (↑PGE2, relaxin → matrix remodelling by MMP-1/3/8 → collagen solubilisation → softening/effacement)

**Vagina**: stratified squamous epithelium; Lactobacillus-dominant microbiome (produces lactic acid → pH 3.8–4.5 → antimicrobial); Bartholin glands (greater vestibular glands, homologous to Cowper's — vestibular lubrication).

**Mammary glands** (modified apocrine glands, hormonally responsive): ductal tree in fibrous/adipose stroma; oestrogen → ductal proliferation; P4 + prolactin → alveolar lobular development; oxytocin → milk ejection reflex.

## Function

### Spermatogenesis and Sperm Function

Spermatogenesis is continuous from puberty throughout life (declining ~1%/year after age 30), producing ~1,500 spermatozoa per second [^guyton-hall]. After epididymal maturation, spermatozoa achieve progressive motility and must undergo **capacitation** in the female tract (removal of cholesterol from sperm plasma membrane → ↑membrane fluidity → ↑Ca²⁺ influx via CatSper → ↑cAMP → ↑PKA → hypermotility/hyperactivation and acrosome reaction potential). Fertilisation: capacitated sperm reaches zona pellucida → ZP3 binds sperm surface → acrosome reaction (exocytosis of acrosomal content: hyaluronidase, acrosin → ZP penetration) → ZP2 binding → membrane fusion → cortical reaction (cortical granule exocytosis → ZP3 modification → block to polyspermy) → pronuclear fusion.

### Menstrual Cycle Hormonal Dynamics

**Day 1–5 (Menstruation)**: P4/E2 withdrawal → prostaglandin F2α (PGF2α, via COX-2 in endometrial stroma) → spiral artery vasoconstriction → ischaemia → endometrial shedding. Blood loss: 30–80 mL (>80 mL = menorrhagia). Simultaneously, ↓P4 → ↑GnRH pulsatility → ↑FSH → follicle recruitment.

**Day 5–13 (Follicular)**: dominant follicle secretes ↑E2 → endometrial proliferation; E2 begins to suppress FSH (preventing multi-follicular selection), while the dominant follicle, now with more FSH receptors and higher inhibin B, outcompetes; LH:FSH ratio rises.

**Day ~14 (Ovulation)**: E2 >200 pg/mL for >36h → AVPV kisspeptin neurons switch to positive feedback → GnRH surge → LH surge → oocyte I completes meiosis I → polar body I → oocyte II; follicle ruptures; oocyte + cumulus expelled; fimbriae sweep oocyte into tube.

**Day 15–28 (Luteal)**: CL secretes P4 (peak ~20 ng/mL day 21) and E2 → secretory endometrium → implantation window (days 20–24); if embryo implants → trophoblast → hCG (identical LH subunit structure) → rescues CL from luteolysis → maintains P4; if no implantation → CL regression → ↓P4/E2 → menses.

### Oestrogen Actions (Broad Systemic Effects)

Oestradiol (E2) binds ERα (ESR1) and ERβ (ESR2) — nuclear receptors (NR3A subfamily) that dimerize and bind ERE (oestrogen response elements) to activate or suppress transcription; also rapid non-genomic signalling via membrane-associated ERα/GPER [^guyton-hall][^alberts-mol-cell-biology]:

| System | Oestrogen Effect |
|:---|:---|
| **Bone** | ↑OPG → ↓RANKL → ↓osteoclastogenesis (anti-resorptive); ↑type I collagen expression; deficiency → postmenopausal osteoporosis |
| **Cardiovascular** | ↑eNOS (→NO → vasodilation), ↑HDL-C (↑ApoA1, ↑CETP inhibition), ↑LDL-R → ↓LDL-C, anti-atherogenic; coronary vasodilation; ↓ICAM-1/VCAM-1 → ↓monocyte adhesion |
| **CNS** | Neuroprotection (↑BDNF, ↑BCL-2 → ↓apoptosis); ↑serotonin synthesis + reuptake inhibition → mood; ↑dopamine D2R → cognition; deficiency → vasomotor instability (hot flushes — VMH thermostat), cognitive changes, depression, insomnia |
| **Immune** | ↑Th1/Th17, ↑B cell survival, ↑autoantibody production → ↑autoimmune disease risk (SLE, RA, MS, thyroiditis); ↑IFN-γ production; ↑NK cell cytotoxicity |
| **Coagulation** | ↑FVII, FVIII, fibrinogen, vWF; ↓protein S (natural anticoagulant) → net pro-thrombotic → ↑DVT/PE risk (especially OCP/HRT); pharmacological doses (OCP) → 3–5× ↑VTE risk |
| **Breast** | Proliferative: ↑IGF-1, ↑EGF → ductal proliferation; ↑cell cycle entry; chronic excess → ↑breast cancer risk (especially in ER+/PR+ tumours) |
| **Liver** | ↑SHBG (↓free androgens), ↑angiotensinogen (→↑renin-angiotensin → ↑BP on OCP), ↑coagulation factors (see above), ↑TBG (thyroid-binding globulin → ↑T4 requirement in hypothyroid women on OCP/HRT) |

### Testosterone Actions

Testosterone binds androgen receptor (AR, nuclear receptor NR3C4) → AR dimerization → ARE (androgen response elements) binding → gene transcription:
- **Anabolic**: ↑skeletal muscle protein synthesis (↑mTORC1 pathway, ↑satellite cell activation); ↑erythropoiesis (↑EPO production, ↑bone marrow sensitivity → ↑haematocrit → explains gender difference in normal Hgb [males 13.5–17.5 g/dL; females 12–15.5 g/dL])
- **Androgenic**: pubertal virilisation (external genitalia, secondary sexual characteristics — beard, body hair, penile growth, deepening voice [laryngeal growth], sebaceous gland activity); spermatogenesis support (high intratesticular T essential)
- **CNS**: libido, aggressive behaviour, spatial cognition, dopaminergic tone (mood, energy); deficiency → depression, cognitive impairment, ↓libido
- **Bone**: anabolic via aromatisation to E2 (bone density) and direct AR-mediated periosteal expansion (larger bone cross-sectional area in males)

## Connections

- `modulates` → **[Immune System](../immune-system/README.md)** — sex steroids profoundly regulate immune cell populations; oestrogen promotes B-cell survival and Th1/Th17 dominance (autoimmunity); testosterone is broadly immunosuppressive
- `modulates` → **[Cardiovascular System](../cardiovascular-system/README.md)** — oestrogen is atheroprotective; menopause → ↑CVD risk; testosterone drives erythropoiesis and modulates RAAS; sex hormone fluctuation across the menstrual cycle alters BP, platelet activity, and endothelial function
- `modulates` → **[Nervous System](../nervous-system/README.md)** — sex hormones act throughout the hypothalamus, limbic system, and cortex; E2 neuroprotects and stabilises mood; vasomotor symptoms in menopause reflect hypothalamic thermoregulatory disruption; testosterone promotes motivation and dopaminergic tone
- `modulates` → **[Liver](../../06-organ/liver/README.md)** — liver metabolises sex hormones (CYP3A4/CYP3A5; glucuronidation; sulfation); hepatocytes are the source of SHBG, IGF-1, and angiotensinogen — all modulated by sex steroids
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Oestradiol (E2; CYP19A1 aromatase from ovarian granulosa cells) binds ERα/ERβ → bone protection (↑OPG→↓RANKL), cardioprotection (↑eNOS/HDL-C), CNS neuroprotection; menopause E2 deficiency → osteoporosis + ↑CVD; OCP suppresses HPG axis; HRT restores systemic effects of E2.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Testosterone (Leydig cells → CYP11A1/CYP17A1/17β-HSD3; ~7 mg/day) binds AR → anabolic (muscle, erythropoiesis) + androgenic (virilisation, spermatogenesis); 5α-reductase → DHT (prostate/skin/scalp); aromatase → E2 (bone, HPG feedback); PCOS: excess theca-cell testosterone via LH.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Hyperinsulinaemia in PCOS sensitises ovarian LH receptors → ↑theca androgen synthesis → ↑testosterone → anovulation + hirsutism; insulin directly stimulates IGF-1R on ovary; metformin reduces hepatic insulin resistance → ↓insulin → ↓androgen production → improved ovulation rates.

## Pathology

### Polycystic Ovary Syndrome (PCOS)

Most common endocrine disorder in reproductive-age females (~10–15% prevalence). Rotterdam criteria (2 of 3): oligo/anovulation, hyperandrogenism (clinical or biochemical), polycystic ovarian morphology on ultrasound [^guyton-hall].

**Pathophysiology**: ↑LH:FSH ratio (↑GnRH pulse frequency → preferentially stimulates LH) → ↑theca cell androgen synthesis (androstenedione, testosterone) → partial aromatisation to E2 → loss of cyclic LH surge → anovulation. Insulin resistance (present in ~70% of PCOS) → ↑insulin → ↑LH receptor sensitivity on theca cells → further ↑androgens. Granulosa cells show impaired aromatase → ↓follicular E2 → follicle arrest. Multiple small antral follicles (4–12 mm) accumulate → polycystic appearance.

**Clinical features**: irregular/absent periods, hirsutism, acne, androgenetic alopecia, acanthosis nigricans (insulin resistance), metabolic syndrome (↑T2D risk, ↑CVD risk).

**Treatment**: OCP (↑SHBG → ↓free androgens; ↑endometrial protection; cycle regulation); metformin (↓hepatic insulin resistance → ↓insulin → ↓androgen drive); clomiphene/letrozole (ovulation induction); weight loss (most effective if overweight — ↓insulin resistance); spironolactone (aldosterone antagonist + AR antagonist → ↓hirsutism).

### Endometriosis

Ectopic endometrial glands and stroma outside the uterus (most common: ovaries [endometriomas/'chocolate cysts'], peritoneum, uterosacral ligaments, rectovaginal septum) responding to cyclical hormonal stimulation → bleeding, inflammation, adhesions, fibrosis [^guyton-hall].

**Pathophysiology**: retrograde menstruation (Sampson theory — universally present but disease only in ~10% → impaired peritoneal immune clearance); oestrogen-dependent (lesions express high aromatase → local E2 production even in hypoestrogenic states); pro-inflammatory milieu: ↑IL-6, IL-8, TNF-α, PGE2 from macrophages → pain sensitisation (↑TRPV1/substance P in nerve fibres innervating lesions) + further oestrogen synthesis (PGE2 → ↑aromatase).

**Clinical**: dysmenorrhoea (primary symptom — often severe and refractory), deep dyspareunia, dyschezia, chronic pelvic pain, infertility (~30–50% of infertile women have endometriosis — impaired oocyte quality, altered tubal motility, inflammatory peritoneal environment). Diagnosis: laparoscopy (gold standard) or transvaginal ultrasound (for endometriomas).

**Treatment**: NSAIDs (COX-2 inhibition → ↓PGE2 → ↓pain + ↓aromatase); combined OCP (↑SHBG; suppresses cycle → ↓lesion activity); progestins (norethindrone, dienogest → decidualisation of lesions); GnRH agonists (leuprolide → medical menopause → ↓E2 → lesion regression; use with add-back HRT to prevent bone loss); GnRH antagonists (elagolix — oral, faster onset/offset); surgery (laparoscopic excision/ablation for endometriomas, adenomyosis); IVF for infertility.

### Benign Prostatic Hyperplasia (BPH)

Benign proliferation of prostate stromal (smooth muscle/fibrous) and glandular epithelial cells driven by **DHT** (5α-dihydrotestosterone → AR → ↑stromal/epithelial growth factors [EGF, IGF-1, FGF-7/10]). Begins in periurethral transition zone. Affects >50% of men >60 years [^guyton-hall].

**Clinical**: lower urinary tract symptoms (LUTS) — obstructive (poor stream, hesitancy, incomplete emptying) and irritative (urgency, frequency, nocturia); complications: urinary retention, bladder stones, renal insufficiency.

**Treatment**: α1-blockers (tamsulosin, doxazosin — relaxes smooth muscle of prostate stroma and bladder neck → ↑urine flow); 5α-reductase inhibitors (finasteride, dutasteride — ↓DHT → gland shrinkage ~20% over 6 months; also used for androgenetic alopecia); combination superior to monotherapy; surgery (TURP — transurethral resection of prostate — gold standard for refractory disease; laser enucleation [HoLEP]).

### Prostate Cancer (PCa)

Most common non-skin cancer in males in the developed world. Strongly androgen-dependent — most PCa express AR and require androgens for growth [^guyton-hall].

**Pathogenesis**: androgen-dependent transcription → ↑cell proliferation; early mutations in TMPRSS2:ERG fusion (AR-driven TMPRSS2 promoter drives ERG oncogene); PTEN loss (→ ↑PI3K/AKT/mTOR); CDK12, BRCA2 mutations in aggressive disease.

**Staging and treatment**:
- **Localised**: active surveillance (low-risk — PSA <10, Gleason 6); radical prostatectomy (robotic-assisted) or radiotherapy (EBRT + brachytherapy) — curative intent
- **Castration-sensitive metastatic (mCSPC)**: androgen deprivation therapy (ADT) — GnRH agonists (leuprolide, goserelin → initial testosterone flare [→ add anti-androgen briefly] then castrate testosterone <50 ng/dL) or GnRH antagonists (degarelix, relugolix — no flare) + novel hormonal agents (abiraterone + prednisone [CYP17A1 inhibitor → ↓adrenal androgen synthesis], enzalutamide/apalutamide/darolutamide [AR antagonists → block ligand binding + nuclear translocation])
- **Castration-resistant (mCRPC)**: disease progresses despite castrate testosterone; mechanisms: AR amplification, AR splice variant (ARv7 — lacks ligand-binding domain → constitutively active, enzalutamide-resistant), intratumoral androgen synthesis, non-AR pathways; treatment: abiraterone, enzalutamide, taxanes (docetaxel, cabazitaxel), PARP inhibitors (olaparib/rucaparib for BRCA1/2 mutated), ¹⁷⁷Lu-PSMA-617 (radioligand therapy)

### Ovarian Cancer

Fifth most common cancer death in women; usually diagnosed late (stage III/IV, 5-year OS ~29%) [^guyton-hall].

**High-grade serous ovarian carcinoma (HGSOC)**: ~70% of ovarian cancers; arises from fallopian tube fimbriae (serous tubal intraepithelial carcinoma [STIC] — precursor); TP53 mutation universal; BRCA1/2 mutations → ~15% hereditary; CCNE1 amplification, RB1 loss, BRCA homologous recombination deficiency (HRD). CA-125 and HE4 biomarkers. Treatment: carboplatin/paclitaxel + bevacizumab (VEGF inhibitor); PARP inhibitors (olaparib maintenance → BRCA-mutated; niraparib for HRD tumours) → significantly improved PFS.

### Cervical Cancer

HPV-driven (HPV-16 [squamous cell carcinoma], HPV-18 [adenocarcinoma] responsible for ~70%); E6 protein → E6AP ubiquitin ligase → p53 proteasomal degradation → ↑cell cycle; E7 → pRb degradation → ↑E2F → ↑CDK4/6 → uncontrolled cell cycle. Progression: infection → CIN1 (low-grade) → CIN2/CIN3 (high-grade dysplasia → LLETZ/LEEP excision) → invasive cervical cancer (ICC). Prevention: Gardasil-9 (nonavalent VLP vaccine: HPV-6/11/16/18/31/33/45/52/58 → IgG neutralising antibodies → >90% efficacy against targeted types before first sexual contact) [^alberts-mol-cell-biology].

### Turner Syndrome (45,X0)

Complete or partial X monosomy → streak gonads (fibrous bands, no follicles — congenital primary ovarian insufficiency) → profound oestrogen deficiency → ↑FSH/LH (hypergonadotropic hypogonadism) → absent puberty without HRT. Features: short stature (SHOX haploinsufficiency → ↓IGF-1 → short limbs; GH treatment indicated), webbed neck (cystic hygroma/lymphoedema in fetal life), shield chest, coarctation of aorta (~15%), bicuspid aortic valve (~30%), renal anomalies (horseshoe kidney), autoimmune thyroiditis, infertility. Management: oestrogen + progesterone replacement (puberty induction at age 12 → adult HRT); HRT essential for bone density and cardiovascular risk.

### Klinefelter Syndrome (47,XXY)

Most common sex chromosome aneuploidy (~1:500–1:600 males). Mechanism: meiotic non-disjunction (usually maternal). Pathology: supernumerary X → accelerated germ cell apoptosis in puberty → progressive seminiferous tubule hyalinisation/fibrosis → azoospermia (testicular fibrosis); Leydig cells partially preserved → testosterone often in low-normal range (reduced with age) but ↑LH (compensated hypogonadism) → gynaecomastia (aromatisation of androstenedione → E2 in excess of T). ↑FSH diagnostic (azoospermia + ↑FSH > 7.6 IU/L = primary testicular failure). Tall stature (delayed epiphyseal closure due to late puberty), long legs, learning difficulties (executive function), increased anxiety/autism spectrum traits. Treatment: testosterone replacement (↓gynaecomastia risk, ↑energy/libido, ↑bone density, ↑muscle); fertility possible via testicular sperm extraction (TESE) + ICSI even with Klinefelter.

## See Also

- [nervous-system](../../07-system/nervous-system/README.md) — HPG axis control via hypothalamic kisspeptin/GnRH; sex hormone CNS effects
- [cardiovascular-system](../../07-system/cardiovascular-system/README.md) — oestrogen cardioprotection; menopause and CVD risk
- [immune-system](../../07-system/immune-system/README.md) — sex hormone immune modulation; female autoimmune predominance
- [liver](../../06-organ/liver/README.md) — sex hormone metabolism; SHBG production; OCP effects on hepatic proteins
- [musculoskeletal-system](../../07-system/musculoskeletal-system/README.md) — oestrogen and testosterone in bone remodelling; sex differences in BMD and fracture risk
- [insulin](../../03-molecular/insulin/README.md) — insulin resistance in PCOS; androgen-insulin crosstalk
- [cortisol](../../03-molecular/cortisol/README.md) — HPA-HPG axis crosstalk; chronic stress → GnRH suppression → amenorrhoea

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^guyton-hall]: Hall JE, Hall ME. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021.
[^alberts-mol-cell-biology]: Alberts B, Johnson A, Lewis J, et al. *Molecular Biology of the Cell.* 7th ed. W.W. Norton; 2022.

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
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "The reproductive organs depend on lymphatic drainage that doubles as their cancer highway: pelvic, inguinal, and para-aortic nodes clear fluid from uterus, ovaries, prostate, and testes, and these node chains are the first metastatic sites of reproductive cancers."
  - target: 01-human/07-system/endocrine-system
    relation: modulates
    note: "The reproductive system is an endocrine organ system run by the hypothalamic-pituitary-gonadal axis: GnRH → LH/FSH → ovarian or testicular steroidogenesis (estrogen, progesterone, testosterone), with feedback driving puberty, the menstrual cycle, spermatogenesis, and fertility."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Progesterone completes the reproductive steroid trio with estrogen and testosterone: from the corpus luteum (and placenta) it prepares the endometrium for implantation, sustains pregnancy, and suppresses ovulation by feedback — the basis of progestin contraception."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "The reproductive and musculoskeletal systems are coupled through sex hormones: estrogen and testosterone build and maintain bone and muscle, so puberty drives the growth spurt and menopause's estrogen loss accelerates osteoporosis—tying gonads to skeletal health."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "The reproductive and digestive systems interact metabolically: the liver clears and conjugates sex steroids, the gut microbiome's 'estrobolome' recirculates estrogen, and pregnancy crowds abdominal organs—so hormonal and GI physiology are intertwined."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Sex hormones shape the skin, linking reproductive and integumentary systems: androgens drive sebaceous glands and acne and pattern hair, estrogen maintains dermal collagen, and pregnancy alters pigmentation—so skin reflects gonadal hormonal state."
  - target: 01-human/07-system/prostate-cancer
    relation: connects-to
    note: "Prostate cancer is the commonest male reproductive-system malignancy: its androgen-driven epithelium turns malignant, and because growth depends on testosterone, androgen-deprivation therapy is central—a hormone that both builds and treats its tumor."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "Ovarian cancer is the most lethal gynecologic reproductive-system cancer: arising from ovarian/fallopian epithelium it spreads silently through the peritoneum, so it usually presents late—and its hormonal and BRCA-linked biology ties it to the reproductive axis."
  - target: 01-human/07-system/cervical-cancer
    relation: connects-to
    note: "Cervical cancer shows how infection drives reproductive-system cancer: persistent HPV infection of the cervical transformation zone causes nearly all cases, making it largely preventable by vaccination—a reproductive-tract cancer with an external, eradicable cause."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "The placenta is the reproductive system's temporary endocrine organ: it sustains pregnancy by secreting hCG, progesterone and estrogen and exchanging gases and nutrients, so this disposable organ takes over hormonal control the ovaries and pituitary normally hold."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Oxytocin runs the reproductive system's mechanical events: it triggers uterine contractions in labor and milk ejection in breastfeeding through positive-feedback loops, so the same hormone drives both childbirth and lactation in the reproductive cycle."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "The reproductive system shapes skeletal health: ovarian estrogen protects bone, so menopause's estrogen loss accelerates bone resorption into osteoporosis—linking the reproductive system's hormonal decline to fracture risk in later life."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Prolactin governs the reproductive system's lactation and fertility: it drives milk production and, when excessive (prolactinoma), suppresses the GnRH-LH/FSH axis causing infertility and amenorrhea—so the pituitary hormone links the brain to reproduction."
  - target: 02-pathogen/01-viruses/hpv-16
    relation: connects-to
    note: "HPV is the reproductive system's major oncogenic infection: sexually transmitted high-risk types cause cervical, vulvar, penile and anal cancers, so this virus turns a reproductive-tract infection into cancer—now largely preventable by vaccination."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "The breast is the reproductive system's milk-producing organ and a major cancer site: estrogen and progesterone drive its development and cyclical changes, and these same hormones fuel most breast cancers—tying reproductive hormones to the commonest female cancer."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Smooth muscle powers the reproductive tract's movements: myometrial smooth muscle contracts to expel the fetus in labor and shed the lining in menstruation, while smooth muscle in the vas deferens and oviducts moves sperm and egg toward fertilization."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Leptin links body fat to fertility: this fat-derived hormone signals energy sufficiency to the hypothalamus, permitting the GnRH pulses that drive puberty and reproduction—so very low body fat suppresses menstruation and fertility."
  - target: 01-human/07-system/endometrial-cancer
    relation: connects-to
    note: "Endometrial cancer is the most common gynecologic malignancy: arising from the uterine lining under unopposed estrogen, it ties the reproductive system's hormone biology to cancer risk, with obesity and PCOS raising estrogen exposure."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: connects-to
    note: "The reproductive system runs on thyroid hormones: too little or too much thyroid hormone disrupts menstrual cycles, lowers fertility, and raises miscarriage risk, so thyroid status is checked whenever reproduction falters."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Reproduction depends on zinc: the mineral is essential for sperm production and testosterone synthesis, and is concentrated in semen, so zinc deficiency impairs male fertility and gonadal function."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages quietly run the reproductive organs: they help rupture the follicle at ovulation, support the corpus luteum and testis steroid cells, and police the maternal-fetal interface, making immune cells essential to fertility."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "The brain commands reproduction from the top: the hypothalamus pulses GnRH to drive the pituitary's FSH and LH, which run the ovaries and testes, so the whole reproductive system answers to this neural-hormonal axis."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Reproduction turns on a calcium signal: a wave of calcium sweeps through the egg at fertilization to activate it and block other sperm, and calcium influx also powers the sperm's capacitation, making the ion central to conception."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "The adrenal glands feed the reproductive hormone pool: they make DHEA and other androgens that supplement the gonads and drive adrenarche, so adrenal disorders can disturb puberty, fertility and menstrual function."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Reproduction is costly in iron: each menstrual period drains iron, and pregnancy's demand for the growing fetus and placenta often outpaces supply, making iron-deficiency anemia common in women of reproductive age."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Sex hormones are written on the skin: testosterone and estrogen shape body and facial hair, oil glands and acne, and the pigment and stretch changes of puberty and pregnancy, so the skin mirrors reproductive state."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Reproduction rebuilds blood vessels each cycle: the endometrium and placenta drive intense VEGF-fueled angiogenesis through endothelial cells to thicken the lining and nourish a pregnancy."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photons watch over reproduction: pelvic and obstetric ultrasound image the ovaries, uterus, and growing fetus, follicle scans guide IVF, and mammography screens the breast — sound and light made the unseen interior of reproductive medicine visible."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The reproductive and urinary tracts grow from one ridge: sharing the embryonic urogenital fold, they develop side by side, so a malformed uterus or absent vas often comes paired with a missing or misplaced kidney."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Dopamine holds the brake on fertility's milk hormone: it continuously suppresses prolactin, so a dopamine drop lets prolactin rise to enable lactation — and a prolactin-secreting tumor, treated with dopamine agonists, silences periods until corrected."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "The sperm is a structure only electron microscopy fully reveals: a 9+2 axoneme drives the flagellum, a midpiece sheath of mitochondria powers it, and an acrosome caps the head — and EM diagnoses the motility defects (e.g. primary ciliary dyskinesia) behind some male infertility."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D reaches into reproduction: VDRs sit in ovary, testis, endometrium, and placenta, and deficiency tracks with PCOS, lower fertility, and adverse pregnancy outcomes — one reason status is checked in preconception and pregnancy care."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium guards the pregnant reproductive tract: intravenous magnesium sulfate is the first-line treatment for eclamptic seizures and gives fetal neuroprotection in preterm birth, while also relaxing uterine smooth muscle as a tocolytic."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies both threaten and tolerate reproduction: antisperm antibodies cause immune infertility and anti-D antibodies drive hemolytic disease of the newborn, yet pregnancy itself is a feat of immune tolerance that keeps the half-foreign fetus from being rejected."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Body fat sets the reproductive thermostat: adipose tissue makes estrogen and leptin, so obesity drives the anovulation and PCOS of women and the low testosterone of men, while too little fat halts menstruation altogether."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "The thyroid paces fertility: hypo- and hyperthyroidism disorder the menstrual cycle, impair ovulation and sperm, and raise miscarriage risk, so thyroid function is a routine check in infertility and early-pregnancy care."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Nerves run the reproductive acts: autonomic neurons drive erection (parasympathetic) and ejaculation (sympathetic), and neural reflexes govern labor and orgasm, so nerve injury from surgery, diabetes or spinal damage commonly causes sexual dysfunction."
  - target: 01-human/07-system/hiv
    relation: connects-to
    note: "The reproductive tract is HIV's main gateway: the virus spreads through sexual contact across genital and rectal mucosa and passes from mother to child in pregnancy, birth and breastfeeding, making reproductive health central to its prevention."
  - target: 01-human/07-system/hereditary-breast-ovarian-cancer
    relation: connects-to
    note: "Germline BRCA strikes the reproductive organs: it sharply raises ovarian, breast and prostate cancer risk, so carriers face decisions about risk-reducing removal of the ovaries and tubes that bring early surgical menopause."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Stress shuts down reproduction: cortisol from the stress axis suppresses GnRH and the gonadotropins above the gonads, so chronic stress can halt ovulation and lower fertility — the body deferring reproduction when conditions seem unsafe."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Menstruation drains iron: the monthly blood loss of the reproductive cycle is the leading cause of iron deficiency anemia in menstruating people, and heavy bleeding from fibroids or disorders can deepen it into symptomatic anemia."
  - target: 02-pathogen/01-viruses/zika-virus
    relation: connects-to
    note: "A virus that targets reproduction: Zika is sexually transmitted and crosses the placenta to disrupt fetal brain development, making it a reproductive-tract pathogen whose gravest harm falls on the developing offspring."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Fat is a reproductive organ: adipocytes aromatize androgens to estrogen and secrete leptin that signals energy sufficiency to the HPG axis, so too little or too much body fat disrupts puberty, ovulation, and fertility."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Estrogen tips the blood toward clotting: pregnancy and estrogen-containing contraception or HRT are major acquired risk factors for venous thromboembolism, a key safety consideration across reproductive care."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The gut microbiome tunes sex hormones: the 'estrobolome' — gut bacteria that deconjugate estrogens — regulates circulating estrogen levels, linking the gut flora to reproductive and hormone-driven disease."
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: connects-to
    note: "It is the commonest fungal invader of the tract: shifts in vaginal pH and flora, estrogen, antibiotics or diabetes let Candida overgrow into vulvovaginal candidiasis, one of the most frequent reproductive-tract complaints."
  - target: 01-human/07-system/lynch-syndrome
    relation: connects-to
    note: "It is the top hereditary cause of endometrial cancer: Lynch syndrome's mismatch-repair defect drives a high lifetime risk of endometrial and ovarian cancer, often the sentinel malignancy that flags the syndrome in women."
  - target: 01-human/07-system/peutz-jeghers-syndrome
    relation: connects-to
    note: "It seeds distinctive sex-organ tumors: Peutz-Jeghers predisposes to ovarian sex-cord tumors with annular tubules, Sertoli-cell testicular tumors and cervical adenoma malignum, a hereditary stamp on the reproductive tract."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Its sex hormones sway mood across the lifespan: estrogen and progesterone fluctuations underlie premenstrual dysphoria, postpartum depression and the perimenopausal mood dip, tying reproductive endocrinology directly to depressive illness."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "It is entwined with insulin and metabolism: polycystic ovary syndrome links ovarian dysfunction to insulin resistance, gestational diabetes foreshadows later disease, and low testosterone tracks with metabolic risk in men."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Pregnancy can unmask a failing heart: the late-gestational and postpartum period can precipitate peripartum cardiomyopathy, a reproductive-specific cause of heart failure in previously healthy women."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "They share the genitourinary tract and embryology: the reproductive and urinary systems develop together and run side by side, so prostatic disease, pelvic surgery and pregnancy all directly affect the kidneys and bladder."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Pregnancy can drive blood pressure dangerously high: pre-eclampsia and gestational hypertension are reproductive-specific disorders of pregnancy, and they flag a woman's raised lifelong cardiovascular risk."
  - target: 02-pathogen/01-viruses/herpesvirus
    relation: connects-to
    note: "Herpesviruses colonise the genital tract: HSV causes genital herpes transmitted sexually, persisting latent in sacral ganglia and posing a serious risk of neonatal infection during delivery."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Childbirth and its surgery leave wounds to heal: vaginal delivery causes perineal tears and episiotomies, and caesarean section a uterine and abdominal-wall wound, all needing to heal in the postpartum period."
  - target: 02-pathogen/02-bacteria/streptococcus-pyogenes
    relation: connects-to
    note: "Childbed fever stalks the puerperium: Streptococcus pyogenes infecting the raw post-delivery uterus causes puerperal sepsis and endometritis, the historic killer that hand hygiene helped tame."
  - target: 02-pathogen/01-viruses/hepatitis-b-virus
    relation: connects-to
    note: "It transmits a virus sexually and to the newborn: hepatitis B spreads through sexual contact and, crucially, vertically from mother to baby at birth, which neonatal vaccination is designed to prevent."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Pregnancy reshapes breathing and vertical infection reaches the airway: the gravid uterus and progesterone raise ventilation and cause breathlessness, and vertically-transmitted HPV causes recurrent respiratory papillomatosis in the child."
  - target: 02-pathogen/01-viruses/hiv-1
    relation: connects-to
    note: "It carries HIV to partners and babies: HIV spreads through sexual contact and vertically from mother to child, the route that antiretroviral prophylaxis in pregnancy is designed to interrupt."
  - target: 02-pathogen/01-viruses/hepatitis-c-virus
    relation: connects-to
    note: "It can pass hepatitis C onward: the virus is transmitted sexually and vertically from mother to baby, though less efficiently than hepatitis B."
  - target: 02-pathogen/04-parasites/toxoplasma-gondii
    relation: connects-to
    note: "It crosses the placenta: maternal toxoplasmosis in pregnancy can transmit to the fetus, causing congenital toxoplasmosis with chorioretinitis and brain calcification, part of the TORCH group."
  - target: 02-pathogen/02-bacteria/listeria-monocytogenes
    relation: connects-to
    note: "It targets the pregnant uterus: Listeria has a tropism for the placenta, and listeriosis in pregnancy causes miscarriage, stillbirth and severe neonatal sepsis."
  - target: 03-medicine/03-food/zinc-dietary
    relation: connects-to
    note: "Zinc underpins fertility: it is essential for spermatogenesis, testosterone production and oocyte quality, so deficiency impairs reproduction in both sexes."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "Reproductive practices invite toxic shock: prolonged tampon use and the postpartum uterus let Staphylococcus aureus release TSST-1 superantigen causing menstrual toxic shock syndrome, and the organism also drives lactational mastitis and breast abscess."
  - target: 03-medicine/01-modern/04-cardio/aspirin
    relation: connects-to
    note: "Low-dose aspirin protects pregnancy: started before 16 weeks in high-risk women, low-dose aspirin lowers the incidence of pre-eclampsia and fetal growth restriction by rebalancing placental thromboxane and prostacyclin."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Sex steroids govern the skeleton: oestrogen and testosterone restrain osteoclasts and maintain bone density, so menopause, hypogonadism, and anti-hormonal cancer therapy all accelerate cortical bone loss and fracture risk."
  - target: 01-human/07-system/ovarian-clear-cell-carcinoma
    relation: connects-to
    note: "A gynaecological cancer born of endometriosis: ovarian clear cell carcinoma arises from endometriotic cysts of the reproductive tract, an ARID1A-driven, chemoresistant tumour that ties the reproductive system to oncology."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "A trace element male fertility needs: selenium is built into selenoproteins essential for sperm maturation and flagellar function, so selenium deficiency impairs sperm motility and male fertility."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "The molecule behind erection and uterine blood flow: nitric oxide relaxes vascular and smooth muscle to drive penile erection (the PDE5/cGMP pathway sildenafil targets) and to widen the blood supply of the uterus and placenta."
  - target: 01-human/07-system/dicer1-syndrome
    relation: connects-to
    note: "Inherited reproductive tumours: DICER1 predisposes to ovarian sex-cord-stromal tumours such as Sertoli-Leydig tumours, one of the germline syndromes that strike the reproductive system."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Angiogenesis in reproduction: VEGF drives the cyclical vessel growth of the corpus luteum, endometrium and placenta, the controlled angiogenesis on which the menstrual cycle and pregnancy depend."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Vessels of pregnancy and protection: the reproductive system remodels the spiral arteries of the endometrium and placenta, and oestrogen protects the arterial wall—lost at menopause when cardiovascular risk climbs."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Sex hormones and the arteries: oestrogen restrains atherosclerosis before menopause and its loss accelerates it, while erectile dysfunction from penile-artery disease is often the first warning sign of systemic atherosclerosis in men."
  - target: 01-human/07-system/hnscc
    relation: connects-to
    note: "HPV beyond the cervix: the same oncogenic human papillomavirus that causes cervical and anogenital cancers of the reproductive tract also drives a rising share of oropharyngeal head and neck cancers."
  - target: 01-human/07-system/thalassemia
    relation: connects-to
    note: "Iron and the gonads: lifelong transfusions in thalassaemia deposit iron in the pituitary and gonads, making hypogonadism and infertility the commonest endocrine complication of the disease."
  - target: 01-human/03-molecular/crh
    relation: connects-to
    note: "Stress suppresses fertility: corticotropin-releasing hormone, the apex of the stress axis, inhibits GnRH and the reproductive axis, the mechanism behind stress- and illness-related amenorrhoea."
  - target: 01-human/03-molecular/growth-hormone
    relation: connects-to
    note: "Growth axis and gonads: growth hormone and IGF-1 support gonadal steroidogenesis and gametogenesis, so GH deficiency or excess can impair fertility and reproductive function."
  - target: 02-pathogen/02-bacteria/escherichia-coli
    relation: connects-to
    note: "Ascending genitourinary infection: uropathogenic E. coli ascends the genital and urinary tract to cause epididymo-orchitis, prostatitis and pelvic infection, threatening fertility."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Reproductive timing: melatonin signals daylength to the reproductive axis, modulating GnRH and the timing of puberty and seasonal fertility."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Behaviour and parturition: vasopressin, alongside oxytocin, shapes pair-bonding and reproductive behaviour and contributes to the neurohypophyseal signalling of labour."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Libido and ejaculation: serotonin modulates sexual desire and ejaculatory control, which is why SSRIs commonly cause sexual dysfunction affecting reproductive function."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Ovulation to parturition: prostaglandins rupture the ovarian follicle at ovulation, trigger the menstrual shedding of the endometrium, and ripen the cervix and drive uterine contractions at labour — central mediators across the reproductive cycle."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "Androgen action: the androgen receptor transduces testosterone and DHT signals that drive male sexual differentiation, spermatogenesis and secondary sexual characteristics — the molecular endpoint of the reproductive endocrine axis in males."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "Gonadotropin feedback: the activin-inhibin system from the gonads tunes pituitary FSH secretion and regulates folliculogenesis and spermatogenesis, a peptide-feedback loop layered on the steroid-hormone axis of reproduction."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Growth-reproduction coupling: IGF-1 acts on ovarian granulosa cells and testicular Sertoli cells to amplify gonadotropin-driven folliculogenesis and spermatogenesis, coupling somatic growth status to the maturation of the reproductive axis at puberty."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Sexual development switch: WNT4/β-catenin signalling directs the bipotential gonad toward ovarian fate and patterns the Müllerian ducts, the developmental molecular pathway that builds the female reproductive tract opposite the SRY-driven testicular programme."
  - target: 01-human/03-molecular/ghrelin
    relation: connects-to
    note: "Energy-deficit gating: ghrelin, the fasting hunger signal, suppresses GnRH pulsatility and gonadotropin release, the counterpart to leptin's sufficiency signal — together coupling nutritional state to fertility so reproduction pauses during starvation."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Steroid precursor: cholesterol is the common substrate from which the gonads synthesise the steroid sex hormones — estrogen, progesterone and testosterone — that govern reproduction, making it the foundational molecule of reproductive endocrinology."
  - target: 01-human/03-molecular/kit
    relation: connects-to
    note: "Gametogenesis: KIT receptor signalling is essential for primordial germ-cell survival and migration, spermatogenesis and ovarian follicle development, a core pathway driving formation of the gametes the reproductive system exists to produce."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Gonadal regulation: the TGF-β superfamily, including the activin/inhibin axis already mapped, regulates gonadal function, follicular and Sertoli-cell development and FSH feedback, governing fertility across both sexes."
  - target: 01-human/03-molecular/npy
    relation: connects-to
    note: "Energy-fertility gate: hypothalamic neuropeptide Y links nutritional and energy status to the GnRH pulse generator, gating reproduction on energy availability alongside the leptin signal already mapped."
  - target: 01-human/03-molecular/endocannabinoid
    relation: connects-to
    note: "Fertility modulator: the endocannabinoid system regulates implantation, oviductal embryo transport and gametogenesis, a lipid-signalling system that tunes the early reproductive events governing fertility."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "Metabolic-reproductive link: insulin-receptor signalling in ovarian theca cells couples metabolic state to androgen production, the mechanism behind the reproductive dysfunction of polycystic ovary syndrome (insulin and androgen receptor mapped)."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Gonadotropin signal transduction: ERK-MAPK signalling transduces gonadotropin (LH/FSH) and growth-factor cues into the steroidogenesis, oocyte maturation and spermatogenesis coordinated by the reproductive system."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Nutrient-fertility coupling: mTOR nutrient-sensing couples metabolic state to oocyte and follicular development and to spermatogenesis, integrating energy availability with fertility."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Gametogenesis signalling: NOTCH signalling regulates folliculogenesis in the ovary and Sertoli-germ-cell interactions in the testis, a developmental pathway central to gametogenesis."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT signalling governs oocyte and follicle survival and the Sertoli-cell support of spermatogenesis in the reproductive system."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "Activin/TGF-β-SMAD signalling (activin-A and TGF-β mapped) regulates FSH secretion, folliculogenesis and gonadal development."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Prolactin and growth hormone signal through JAK-STAT (prolactin and GH mapped), a core endocrine transduction in reproductive physiology and lactation."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 (JAK1/2 already mapped) transduces gonadal cytokine and hormone signals governing ovarian, testicular and uterine function in the reproductive system."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 contributes to the immune tolerance and tissue remodelling of the maternal-fetal interface and reproductive tissues."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antimicrobial and immune defence of the reproductive tract, balancing protection against tolerance."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors (notably FOXO3) govern the ovarian follicle reserve and spermatogenic-cell survival across the reproductive system."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β signaling regulates oocyte maturation and the Wnt-dependent gonadal and uterine developmental programs of the reproductive system."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α couples the hypoxic niches of the ovarian follicle and testis to the angiogenesis and metabolic adaptation of the reproductive system."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) transduces the gonadotropin and growth-factor signals governing gonadal function and gametogenesis of the reproductive system."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK integrates the energy status of the reproductive axis, coupling nutritional state to fertility across the reproductive system."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB inflammatory signaling participates in the ovarian and testicular immune and inflammatory processes of the reproductive system."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy participates in the gametogenesis, hormone-producing-cell homeostasis, and tissue remodeling of the reproductive system."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of gonadotropin and growth-factor receptors participates in the germ-cell and gonadal-somatic-cell signaling of the reproductive system."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the germ-cell epigenetic reprogramming and imprinting of the reproductive system."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven chemokine signaling participates in the immune trafficking within the reproductive tissues of the reproductive system."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the germ-cell migration and gonadal-niche interactions of the reproductive system."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 signaling participates in the ovarian and testicular immune-endocrine processes of the reproductive system."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "GnRH neuron development: FGF8-FGFR1 signalling guides the embryonic migration of GnRH neurons from the olfactory placode to the hypothalamus, and its disruption causes Kallmann syndrome, hypogonadotropic hypogonadism with anosmia."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Ovulation as inflammation: the mid-cycle LH surge triggers an IL-1beta and prostaglandin-driven (prostaglandins already mapped) inflammatory cascade that ruptures the ovarian follicle, and related cytokine signalling governs endometrial receptivity for implantation."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Reproductive vascular tone: endothelin-1 regulates uterine and ovarian vascular flow and constricts penile corpus cavernosum smooth muscle, contributing to menstrual vascular control, placental perfusion and the balance underlying erectile function."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Maternal-fetal tolerance: the semi-allogeneic fetus is protected by specialised regulation of antigen presentation at the placenta, and HLA compatibility influences fertility and pregnancy, tying the reproductive system to the immune system."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Sperm protection: selenium, via glutathione peroxidases, shields developing sperm from oxidative damage and is built into the sperm midpiece, so selenium status affects male fertility alongside the zinc (already mapped) essential for spermatogenesis."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Reproductive renin-angiotensin: local renin-angiotensin systems in the ovary and placenta help regulate follicular development and placental perfusion, and their dysregulation is implicated in pre-eclampsia, a pregnancy-specific vascular disorder."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Pregnancy volume and RAAS: aldosterone rises in pregnancy to expand plasma volume (angiotensin II already mapped), a physiological adaptation of the reproductive renin-angiotensin-aldosterone system whose failure contributes to pre-eclampsia."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Materno-fetal tolerance: regulatory and helper T cells shift toward a tolerogenic profile at the maternal-fetal interface, allowing the semi-allogeneic fetus to be carried, a controlled immune adaptation central to successful reproduction."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Uterine NK cells: specialised decidual natural killer cells regulate trophoblast invasion and spiral-artery remodelling in early pregnancy, a reproductive role distinct from their cytotoxic function elsewhere."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Reproductive immunology: the reproductive system depends on the immune system for the materno-fetal tolerance (regulatory T cells and uterine NK cells already mapped) that lets a semi-allogeneic fetus be carried, a deep interface between the two systems."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Hormone-driven cancer: the sex steroids of the reproductive system (estrogen and progesterone already mapped) drive breast cancer, whose hormone-receptor status guides the endocrine therapy targeting the reproductive-endocrine axis."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Fertilisation calcium signalling: calcium is central to reproduction, from the acrosome reaction of the sperm to the calcium wave that activates the oocyte at fertilisation, triggering the start of embryonic development."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Reproductive iron demand: hepcidin governs the iron (already mapped) balance stressed by the menstrual blood loss and, in pregnancy, the large iron demand of the growing fetus, linking reproduction to systemic iron handling."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Neuroendocrine control: the hypothalamic GnRH pulse generator of the nervous system (via the brain already mapped) drives the pituitary gonadotrophins that command the reproductive system, the neural control of reproduction."
  - target: 01-human/07-system/endometrial-cancer
    relation: connects-to
    note: "Hormone-driven cancer: unopposed oestrogen (already mapped) drives endometrial cancer of the female reproductive tract, a hormone-dependent malignancy of the reproductive system's target organs."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipose-reproductive axis: adiponectin, with leptin (already mapped), links the body fat to the puberty, the fertility and the PCOS (insulin already mapped) of the reproductive system."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Metabolic-reproductive adipokine: resistin, with leptin and adiponectin (already mapped), is the adipokine of the metabolic-reproductive link (PCOS, insulin already mapped) of the reproductive system."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Uterine histamine: the histamine of the uterine and decidual mast cells modulates the implantation, the labour and the reproductive-tract vascular function of the reproductive system."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Maternal-fetal tolerance: the regulatory T cells expand to maintain the maternal tolerance of the fetal allograft, central to the immune-reproductive interface of the reproductive system."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Decidual immunity: the IFN-γ of the uterine/decidual NK cells (already mapped) shapes the spiral-artery remodelling and the maternal-fetal immunology of the reproductive system."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Reproductive-tract antiviral: the type-I interferon defends the reproductive-tract mucosa against the sexually-transmitted viruses, part of the mucosal immunity of the reproductive system."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Th2 maternal-fetal tolerance: IL-4, a type-2 cytokine, promotes the Th2-skewed immune tolerance at the maternal-fetal interface that permits the semi-allogeneic pregnancy of the reproductive system."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Th2 arm: IL-13, with IL-4 (already mapped), is part of the type-2 immune bias of the maternal-fetal tolerance of the reproductive system."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 counter-arm: IL-12 polarises the Th1 (IFN-γ already mapped) arm whose excess (opposing the Th2 tolerance) is implicated in the recurrent pregnancy loss of the reproductive system."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the uterine and endometrial immune milieu of the reproductive system."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 arm), whose balance with the regulatory T cells governs the maternal-fetal tolerance and, in excess, the pre-eclampsia/pregnancy-loss of the reproductive system."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 antibody dimension of the maternal-fetal immune bias of the reproductive system."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Placental complement: the complement C3 activation, tightly restrained by the placental complement regulators, is central to the maternal-fetal tolerance and, when dysregulated, the pre-eclampsia of the reproductive system."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Decidual antigen presentation: the tolerogenic dendritic cells of the decidua present the fetal antigen and, with the regulatory T cells (already mapped), maintain the maternal-fetal tolerance of the reproductive system."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Uterine mast cells: the mast cells of the uterus and the male tract contribute to the implantation, the tissue remodelling and the parturition of the reproductive system."
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
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — The reproductive organs depend on lymphatic drainage that doubles as their cancer highway: pelvic, inguinal, and para-aortic nodes clear fluid from uterus, ovaries, prostate, and testes, and these node chains are the first metastatic sites of reproductive cancers.
- `modulates` → **[Endocrine System](../endocrine-system/README.md)** — The reproductive system is an endocrine organ system run by the hypothalamic-pituitary-gonadal axis: GnRH → LH/FSH → ovarian or testicular steroidogenesis (estrogen, progesterone, testosterone), with feedback driving puberty, the menstrual cycle, spermatogenesis, and fertility.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Progesterone completes the reproductive steroid trio with estrogen and testosterone: from the corpus luteum (and placenta) it prepares the endometrium for implantation, sustains pregnancy, and suppresses ovulation by feedback — the basis of progestin contraception.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — The reproductive and musculoskeletal systems are coupled through sex hormones: estrogen and testosterone build and maintain bone and muscle, so puberty drives the growth spurt and menopause's estrogen loss accelerates osteoporosis—tying gonads to skeletal health.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — The reproductive and digestive systems interact metabolically: the liver clears and conjugates sex steroids, the gut microbiome's 'estrobolome' recirculates estrogen, and pregnancy crowds abdominal organs—so hormonal and GI physiology are intertwined.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Sex hormones shape the skin, linking reproductive and integumentary systems: androgens drive sebaceous glands and acne and pattern hair, estrogen maintains dermal collagen, and pregnancy alters pigmentation—so skin reflects gonadal hormonal state.
- `connects-to` → **[Prostate Cancer](../prostate-cancer/README.md)** — Prostate cancer is the commonest male reproductive-system malignancy: its androgen-driven epithelium turns malignant, and because growth depends on testosterone, androgen-deprivation therapy is central—a hormone that both builds and treats its tumor.
- `connects-to` → **[Ovarian Cancer](../ovarian-cancer/README.md)** — Ovarian cancer is the most lethal gynecologic reproductive-system cancer: arising from ovarian/fallopian epithelium it spreads silently through the peritoneum, so it usually presents late—and its hormonal and BRCA-linked biology ties it to the reproductive axis.
- `connects-to` → **[Cervical Cancer](../cervical-cancer/README.md)** — Cervical cancer shows how infection drives reproductive-system cancer: persistent HPV infection of the cervical transformation zone causes nearly all cases, making it largely preventable by vaccination—a reproductive-tract cancer with an external, eradicable cause.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — The placenta is the reproductive system's temporary endocrine organ: it sustains pregnancy by secreting hCG, progesterone and estrogen and exchanging gases and nutrients, so this disposable organ takes over hormonal control the ovaries and pituitary normally hold.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Oxytocin runs the reproductive system's mechanical events: it triggers uterine contractions in labor and milk ejection in breastfeeding through positive-feedback loops, so the same hormone drives both childbirth and lactation in the reproductive cycle.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — The reproductive system shapes skeletal health: ovarian estrogen protects bone, so menopause's estrogen loss accelerates bone resorption into osteoporosis—linking the reproductive system's hormonal decline to fracture risk in later life.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Prolactin governs the reproductive system's lactation and fertility: it drives milk production and, when excessive (prolactinoma), suppresses the GnRH-LH/FSH axis causing infertility and amenorrhea—so the pituitary hormone links the brain to reproduction.
- `connects-to` → **[HPV-16](../../../02-pathogen/01-viruses/hpv-16/README.md)** — HPV is the reproductive system's major oncogenic infection: sexually transmitted high-risk types cause cervical, vulvar, penile and anal cancers, so this virus turns a reproductive-tract infection into cancer—now largely preventable by vaccination.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — The breast is the reproductive system's milk-producing organ and a major cancer site: estrogen and progesterone drive its development and cyclical changes, and these same hormones fuel most breast cancers—tying reproductive hormones to the commonest female cancer.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Smooth muscle powers the reproductive tract's movements: myometrial smooth muscle contracts to expel the fetus in labor and shed the lining in menstruation, while smooth muscle in the vas deferens and oviducts moves sperm and egg toward fertilization.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Leptin links body fat to fertility: this fat-derived hormone signals energy sufficiency to the hypothalamus, permitting the GnRH pulses that drive puberty and reproduction—so very low body fat suppresses menstruation and fertility.
- `connects-to` → **[Endometrial Cancer](../endometrial-cancer/README.md)** — Endometrial cancer is the most common gynecologic malignancy: arising from the uterine lining under unopposed estrogen, it ties the reproductive system's hormone biology to cancer risk, with obesity and PCOS raising estrogen exposure.
- `connects-to` → **[Thyroid Hormones (T3/T4)](../../03-molecular/thyroid-hormones/README.md)** — The reproductive system runs on thyroid hormones: too little or too much thyroid hormone disrupts menstrual cycles, lowers fertility, and raises miscarriage risk, so thyroid status is checked whenever reproduction falters.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Reproduction depends on zinc: the mineral is essential for sperm production and testosterone synthesis, and is concentrated in semen, so zinc deficiency impairs male fertility and gonadal function.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages quietly run the reproductive organs: they help rupture the follicle at ovulation, support the corpus luteum and testis steroid cells, and police the maternal-fetal interface, making immune cells essential to fertility.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — The brain commands reproduction from the top: the hypothalamus pulses GnRH to drive the pituitary's FSH and LH, which run the ovaries and testes, so the whole reproductive system answers to this neural-hormonal axis.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Reproduction turns on a calcium signal: a wave of calcium sweeps through the egg at fertilization to activate it and block other sperm, and calcium influx also powers the sperm's capacitation, making the ion central to conception.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — The adrenal glands feed the reproductive hormone pool: they make DHEA and other androgens that supplement the gonads and drive adrenarche, so adrenal disorders can disturb puberty, fertility and menstrual function.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Reproduction is costly in iron: each menstrual period drains iron, and pregnancy's demand for the growing fetus and placenta often outpaces supply, making iron-deficiency anemia common in women of reproductive age.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Sex hormones are written on the skin: testosterone and estrogen shape body and facial hair, oil glands and acne, and the pigment and stretch changes of puberty and pregnancy, so the skin mirrors reproductive state.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Reproduction rebuilds blood vessels each cycle: the endometrium and placenta drive intense VEGF-fueled angiogenesis through endothelial cells to thicken the lining and nourish a pregnancy.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photons watch over reproduction: pelvic and obstetric ultrasound image the ovaries, uterus, and growing fetus, follicle scans guide IVF, and mammography screens the breast — sound and light made the unseen interior of reproductive medicine visible.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The reproductive and urinary tracts grow from one ridge: sharing the embryonic urogenital fold, they develop side by side, so a malformed uterus or absent vas often comes paired with a missing or misplaced kidney.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Dopamine holds the brake on fertility's milk hormone: it continuously suppresses prolactin, so a dopamine drop lets prolactin rise to enable lactation — and a prolactin-secreting tumor, treated with dopamine agonists, silences periods until corrected.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — The sperm is a structure only electron microscopy fully reveals: a 9+2 axoneme drives the flagellum, a midpiece sheath of mitochondria powers it, and an acrosome caps the head — and EM diagnoses the motility defects (e.g. primary ciliary dyskinesia) behind some male infertility.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D reaches into reproduction: VDRs sit in ovary, testis, endometrium, and placenta, and deficiency tracks with PCOS, lower fertility, and adverse pregnancy outcomes — one reason status is checked in preconception and pregnancy care.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium guards the pregnant reproductive tract: intravenous magnesium sulfate is the first-line treatment for eclamptic seizures and gives fetal neuroprotection in preterm birth, while also relaxing uterine smooth muscle as a tocolytic.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies both threaten and tolerate reproduction: antisperm antibodies cause immune infertility and anti-D antibodies drive hemolytic disease of the newborn, yet pregnancy itself is a feat of immune tolerance that keeps the half-foreign fetus from being rejected.
- `connects-to` → **[Obesity](../obesity/README.md)** — Body fat sets the reproductive thermostat: adipose tissue makes estrogen and leptin, so obesity drives the anovulation and PCOS of women and the low testosterone of men, while too little fat halts menstruation altogether.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — The thyroid paces fertility: hypo- and hyperthyroidism disorder the menstrual cycle, impair ovulation and sperm, and raise miscarriage risk, so thyroid function is a routine check in infertility and early-pregnancy care.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Nerves run the reproductive acts: autonomic neurons drive erection (parasympathetic) and ejaculation (sympathetic), and neural reflexes govern labor and orgasm, so nerve injury from surgery, diabetes or spinal damage commonly causes sexual dysfunction.
- `connects-to` → **[HIV](../hiv/README.md)** — The reproductive tract is HIV's main gateway: the virus spreads through sexual contact across genital and rectal mucosa and passes from mother to child in pregnancy, birth and breastfeeding, making reproductive health central to its prevention.
- `connects-to` → **[Hereditary Breast and Ovarian Cancer](../hereditary-breast-ovarian-cancer/README.md)** — Germline BRCA strikes the reproductive organs: it sharply raises ovarian, breast and prostate cancer risk, so carriers face decisions about risk-reducing removal of the ovaries and tubes that bring early surgical menopause.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Stress shuts down reproduction: cortisol from the stress axis suppresses GnRH and the gonadotropins above the gonads, so chronic stress can halt ovulation and lower fertility — the body deferring reproduction when conditions seem unsafe.
- `connects-to` → **[Iron Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Menstruation drains iron: the monthly blood loss of the reproductive cycle is the leading cause of iron deficiency anemia in menstruating people, and heavy bleeding from fibroids or disorders can deepen it into symptomatic anemia.
- `connects-to` → **[Zika Virus (ZIKV)](../../../02-pathogen/01-viruses/zika-virus/README.md)** — A virus that targets reproduction: Zika is sexually transmitted and crosses the placenta to disrupt fetal brain development, making it a reproductive-tract pathogen whose gravest harm falls on the developing offspring.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Fat is a reproductive organ: adipocytes aromatize androgens to estrogen and secrete leptin that signals energy sufficiency to the HPG axis, so too little or too much body fat disrupts puberty, ovulation, and fertility.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Estrogen tips the blood toward clotting: pregnancy and estrogen-containing contraception or HRT are major acquired risk factors for venous thromboembolism, a key safety consideration across reproductive care.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The gut microbiome tunes sex hormones: the 'estrobolome' — gut bacteria that deconjugate estrogens — regulates circulating estrogen levels, linking the gut flora to reproductive and hormone-driven disease.
- `connects-to` → **[Candida albicans](../../../02-pathogen/03-fungi/candida-albicans/README.md)** — It is the commonest fungal invader of the tract: shifts in vaginal pH and flora, estrogen, antibiotics or diabetes let Candida overgrow into vulvovaginal candidiasis, one of the most frequent reproductive-tract complaints.
- `connects-to` → **[Lynch Syndrome](../lynch-syndrome/README.md)** — It is the top hereditary cause of endometrial cancer: Lynch syndrome's mismatch-repair defect drives a high lifetime risk of endometrial and ovarian cancer, often the sentinel malignancy that flags the syndrome in women.
- `connects-to` → **[Peutz-Jeghers Syndrome](../peutz-jeghers-syndrome/README.md)** — It seeds distinctive sex-organ tumors: Peutz-Jeghers predisposes to ovarian sex-cord tumors with annular tubules, Sertoli-cell testicular tumors and cervical adenoma malignum, a hereditary stamp on the reproductive tract.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Its sex hormones sway mood across the lifespan: estrogen and progesterone fluctuations underlie premenstrual dysphoria, postpartum depression and the perimenopausal mood dip, tying reproductive endocrinology directly to depressive illness.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — It is entwined with insulin and metabolism: polycystic ovary syndrome links ovarian dysfunction to insulin resistance, gestational diabetes foreshadows later disease, and low testosterone tracks with metabolic risk in men.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Pregnancy can unmask a failing heart: the late-gestational and postpartum period can precipitate peripartum cardiomyopathy, a reproductive-specific cause of heart failure in previously healthy women.
- `connects-to` → **[Renal System](../renal-system/README.md)** — They share the genitourinary tract and embryology: the reproductive and urinary systems develop together and run side by side, so prostatic disease, pelvic surgery and pregnancy all directly affect the kidneys and bladder.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Pregnancy can drive blood pressure dangerously high: pre-eclampsia and gestational hypertension are reproductive-specific disorders of pregnancy, and they flag a woman's raised lifelong cardiovascular risk.
- `connects-to` → **[Herpesviridae](../../../02-pathogen/01-viruses/herpesvirus/README.md)** — Herpesviruses colonise the genital tract: HSV causes genital herpes transmitted sexually, persisting latent in sacral ganglia and posing a serious risk of neonatal infection during delivery.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Childbirth and its surgery leave wounds to heal: vaginal delivery causes perineal tears and episiotomies, and caesarean section a uterine and abdominal-wall wound, all needing to heal in the postpartum period.
- `connects-to` → **[Streptococcus pyogenes](../../../02-pathogen/02-bacteria/streptococcus-pyogenes/README.md)** — Childbed fever stalks the puerperium: Streptococcus pyogenes infecting the raw post-delivery uterus causes puerperal sepsis and endometritis, the historic killer that hand hygiene helped tame.
- `connects-to` → **[Hepatitis B Virus](../../../02-pathogen/01-viruses/hepatitis-b-virus/README.md)** — It transmits a virus sexually and to the newborn: hepatitis B spreads through sexual contact and, crucially, vertically from mother to baby at birth, which neonatal vaccination is designed to prevent.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Pregnancy reshapes breathing and vertical infection reaches the airway: the gravid uterus and progesterone raise ventilation and cause breathlessness, and vertically-transmitted HPV causes recurrent respiratory papillomatosis in the child.
- `connects-to` → **[HIV-1](../../../02-pathogen/01-viruses/hiv-1/README.md)** — It carries HIV to partners and babies: HIV spreads through sexual contact and vertically from mother to child, the route that antiretroviral prophylaxis in pregnancy is designed to interrupt.
- `connects-to` → **[Hepatitis C Virus](../../../02-pathogen/01-viruses/hepatitis-c-virus/README.md)** — It can pass hepatitis C onward: the virus is transmitted sexually and vertically from mother to baby, though less efficiently than hepatitis B.
- `connects-to` → **[Toxoplasma gondii](../../../02-pathogen/04-parasites/toxoplasma-gondii/README.md)** — It crosses the placenta: maternal toxoplasmosis in pregnancy can transmit to the fetus, causing congenital toxoplasmosis with chorioretinitis and brain calcification, part of the TORCH group.
- `connects-to` → **[Listeria monocytogenes](../../../02-pathogen/02-bacteria/listeria-monocytogenes/README.md)** — It targets the pregnant uterus: Listeria has a tropism for the placenta, and listeriosis in pregnancy causes miscarriage, stillbirth and severe neonatal sepsis.
- `connects-to` → **[Dietary Zinc](../../../03-medicine/03-food/zinc-dietary/README.md)** — Zinc underpins fertility: it is essential for spermatogenesis, testosterone production and oocyte quality, so deficiency impairs reproduction in both sexes.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — Reproductive practices invite toxic shock: prolonged tampon use and the postpartum uterus let Staphylococcus aureus release TSST-1 superantigen causing menstrual toxic shock syndrome, and the organism also drives lactational mastitis and breast abscess.
- `connects-to` → **[Aspirin](../../../03-medicine/01-modern/04-cardio/aspirin/README.md)** — Low-dose aspirin protects pregnancy: started before 16 weeks in high-risk women, low-dose aspirin lowers the incidence of pre-eclampsia and fetal growth restriction by rebalancing placental thromboxane and prostacyclin.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Sex steroids govern the skeleton: oestrogen and testosterone restrain osteoclasts and maintain bone density, so menopause, hypogonadism, and anti-hormonal cancer therapy all accelerate cortical bone loss and fracture risk.
- `connects-to` → **[Ovarian Clear Cell Carcinoma](../ovarian-clear-cell-carcinoma/README.md)** — A gynaecological cancer born of endometriosis: ovarian clear cell carcinoma arises from endometriotic cysts of the reproductive tract, an ARID1A-driven, chemoresistant tumour that ties the reproductive system to oncology.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — A trace element male fertility needs: selenium is built into selenoproteins essential for sperm maturation and flagellar function, so selenium deficiency impairs sperm motility and male fertility.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — The molecule behind erection and uterine blood flow: nitric oxide relaxes vascular and smooth muscle to drive penile erection (the PDE5/cGMP pathway sildenafil targets) and to widen the blood supply of the uterus and placenta.
- `connects-to` → **[DICER1 Syndrome](../dicer1-syndrome/README.md)** — Inherited reproductive tumours: DICER1 predisposes to ovarian sex-cord-stromal tumours such as Sertoli-Leydig tumours, one of the germline syndromes that strike the reproductive system.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Angiogenesis in reproduction: VEGF drives the cyclical vessel growth of the corpus luteum, endometrium and placenta, the controlled angiogenesis on which the menstrual cycle and pregnancy depend.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Vessels of pregnancy and protection: the reproductive system remodels the spiral arteries of the endometrium and placenta, and oestrogen protects the arterial wall—lost at menopause when cardiovascular risk climbs.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Sex hormones and the arteries: oestrogen restrains atherosclerosis before menopause and its loss accelerates it, while erectile dysfunction from penile-artery disease is often the first warning sign of systemic atherosclerosis in men.
- `connects-to` → **[HNSCC](../hnscc/README.md)** — HPV beyond the cervix: the same oncogenic human papillomavirus that causes cervical and anogenital cancers of the reproductive tract also drives a rising share of oropharyngeal head and neck cancers.
- `connects-to` → **[Thalassemia](../thalassemia/README.md)** — Iron and the gonads: lifelong transfusions in thalassaemia deposit iron in the pituitary and gonads, making hypogonadism and infertility the commonest endocrine complication of the disease.
- `connects-to` → **[CRH](../../03-molecular/crh/README.md)** — Stress suppresses fertility: corticotropin-releasing hormone, the apex of the stress axis, inhibits GnRH and the reproductive axis, the mechanism behind stress- and illness-related amenorrhoea.
- `connects-to` → **[Growth Hormone](../../03-molecular/growth-hormone/README.md)** — Growth axis and gonads: growth hormone and IGF-1 support gonadal steroidogenesis and gametogenesis, so GH deficiency or excess can impair fertility and reproductive function.
- `connects-to` → **[Escherichia coli](../../../02-pathogen/02-bacteria/escherichia-coli/README.md)** — Ascending genitourinary infection: uropathogenic E. coli ascends the genital and urinary tract to cause epididymo-orchitis, prostatitis and pelvic infection, threatening fertility.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Reproductive timing: melatonin signals daylength to the reproductive axis, modulating GnRH and the timing of puberty and seasonal fertility.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Behaviour and parturition: vasopressin, alongside oxytocin, shapes pair-bonding and reproductive behaviour and contributes to the neurohypophyseal signalling of labour.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Libido and ejaculation: serotonin modulates sexual desire and ejaculatory control, which is why SSRIs commonly cause sexual dysfunction affecting reproductive function.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Prostaglandins rupture the ovarian follicle at ovulation, trigger the menstrual shedding of the endometrium, and ripen the cervix and drive uterine contractions at labor—central mediators acting across the entire reproductive cycle from ovulation to parturition.
- `connects-to` → **[Androgen receptor](../../03-molecular/androgen-receptor/README.md)** — The androgen receptor transduces testosterone and DHT signals that drive male sexual differentiation, spermatogenesis, and secondary sexual characteristics—the molecular endpoint of the reproductive endocrine axis, mutations of which cause androgen insensitivity.
- `connects-to` → **[Activin A](../../03-molecular/activin-a/README.md)** — The activin-inhibin system from the gonads tunes pituitary FSH secretion and regulates folliculogenesis and spermatogenesis, a peptide-feedback loop layered on the steroid-hormone axis that fine-tunes gametogenesis in both sexes.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — IGF-1 acts on ovarian granulosa cells and testicular Sertoli cells to amplify gonadotropin-driven folliculogenesis and spermatogenesis, coupling somatic growth status to the maturation of the reproductive axis at puberty.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — WNT4/β-catenin signaling directs the bipotential gonad toward ovarian fate and patterns the Müllerian ducts, the developmental pathway that builds the female reproductive tract opposite the SRY-driven testicular program.
- `connects-to` → **[Ghrelin](../../03-molecular/ghrelin/README.md)** — Ghrelin, the fasting hunger signal, suppresses GnRH pulsatility and gonadotropin release, the counterpart to leptin's sufficiency signal—together coupling nutritional state to fertility so reproduction pauses during starvation.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Cholesterol is the common substrate from which the gonads synthesize the steroid sex hormones—estrogen, progesterone and testosterone—that govern reproduction, making it the foundational molecule of reproductive endocrinology.
- `connects-to` → **[KIT](../../03-molecular/kit/README.md)** — KIT receptor signaling is essential for primordial germ-cell survival and migration, spermatogenesis and ovarian follicle development, a core pathway driving formation of the gametes the reproductive system exists to produce.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — The TGF-β superfamily, including the activin/inhibin axis already mapped, regulates gonadal function, follicular and Sertoli-cell development and FSH feedback, governing fertility across both sexes.
- `connects-to` → **[Neuropeptide Y](../../03-molecular/npy/README.md)** — Hypothalamic neuropeptide Y links nutritional and energy status to the GnRH pulse generator, gating reproduction on energy availability alongside the leptin signal already mapped.
- `connects-to` → **[Endocannabinoid System](../../03-molecular/endocannabinoid/README.md)** — The endocannabinoid system regulates implantation, oviductal embryo transport and gametogenesis, a lipid-signaling system that tunes the early reproductive events governing fertility.
- `connects-to` → **[Insulin Receptor](../../03-molecular/insulin-receptor/README.md)** — Insulin-receptor signaling in ovarian theca cells couples metabolic state to androgen production, the mechanism behind the reproductive dysfunction of polycystic ovary syndrome (insulin and androgen receptor mapped).
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling transduces gonadotropin (LH/FSH) and growth-factor cues into the steroidogenesis, oocyte maturation and spermatogenesis coordinated by the reproductive system.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR nutrient-sensing couples metabolic state to oocyte and follicular development and to spermatogenesis, integrating energy availability with fertility.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH signaling regulates folliculogenesis in the ovary and Sertoli-germ-cell interactions in the testis, a developmental pathway central to gametogenesis.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling governs oocyte and follicle survival and the Sertoli-cell support of spermatogenesis in the reproductive system.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — Activin/TGF-β-SMAD signaling (activin-A and TGF-β mapped) regulates FSH secretion, folliculogenesis and gonadal development.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Prolactin and growth hormone signal through JAK-STAT (prolactin and GH mapped), a core endocrine transduction in reproductive physiology and lactation.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 (JAK1/2 already mapped) transduces gonadal cytokine and hormone signals governing ovarian, testicular and uterine function in the reproductive system.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 contributes to the immune tolerance and tissue remodeling of the maternal-fetal interface and reproductive tissues.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antimicrobial and immune defense of the reproductive tract, balancing protection against tolerance.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors (notably FOXO3) govern the ovarian follicle reserve and spermatogenic-cell survival across the reproductive system.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β signaling regulates oocyte maturation and the Wnt-dependent gonadal and uterine developmental programs of the reproductive system.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α couples the hypoxic niches of the ovarian follicle and testis to the angiogenesis and metabolic adaptation of the reproductive system.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) transduces the gonadotropin and growth-factor signals governing gonadal function and gametogenesis of the reproductive system.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK integrates the energy status of the reproductive axis, coupling nutritional state to fertility across the reproductive system.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB inflammatory signaling participates in the ovarian and testicular immune and inflammatory processes of the reproductive system.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy participates in the gametogenesis, hormone-producing-cell homeostasis, and tissue remodeling of the reproductive system.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of gonadotropin and growth-factor receptors participates in the germ-cell and gonadal-somatic-cell signaling of the reproductive system.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the germ-cell epigenetic reprogramming and imprinting of the reproductive system.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven chemokine signaling participates in the immune trafficking within the reproductive tissues of the reproductive system.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the germ-cell migration and gonadal-niche interactions of the reproductive system.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 signaling participates in the ovarian and testicular immune-endocrine processes of the reproductive system.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — GnRH neuron development: FGF8-FGFR1 signalling guides the embryonic migration of GnRH neurons from the olfactory placode to the hypothalamus, and its disruption causes Kallmann syndrome, hypogonadotropic hypogonadism with anosmia.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Ovulation as inflammation: the mid-cycle LH surge triggers an IL-1beta and prostaglandin-driven (prostaglandins already mapped) inflammatory cascade that ruptures the ovarian follicle, and related cytokine signalling governs endometrial receptivity for implantation.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Reproductive vascular tone: endothelin-1 regulates uterine and ovarian vascular flow and constricts penile corpus cavernosum smooth muscle, contributing to menstrual vascular control, placental perfusion and the balance underlying erectile function.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Maternal-fetal tolerance: the semi-allogeneic fetus is protected by specialised regulation of antigen presentation at the placenta, and HLA compatibility influences fertility and pregnancy, tying the reproductive system to the immune system.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Sperm protection: selenium, via glutathione peroxidases, shields developing sperm from oxidative damage and is built into the sperm midpiece, so selenium status affects male fertility alongside the zinc (already mapped) essential for spermatogenesis.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — Reproductive renin-angiotensin: local renin-angiotensin systems in the ovary and placenta help regulate follicular development and placental perfusion, and their dysregulation is implicated in pre-eclampsia, a pregnancy-specific vascular disorder.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Pregnancy volume and RAAS: aldosterone rises in pregnancy to expand plasma volume (angiotensin II already mapped), a physiological adaptation of the reproductive renin-angiotensin-aldosterone system whose failure contributes to pre-eclampsia.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — Materno-fetal tolerance: regulatory and helper T cells shift toward a tolerogenic profile at the maternal-fetal interface, allowing the semi-allogeneic fetus to be carried, a controlled immune adaptation central to successful reproduction.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Uterine NK cells: specialised decidual natural killer cells regulate trophoblast invasion and spiral-artery remodelling in early pregnancy, a reproductive role distinct from their cytotoxic function elsewhere.
- `connects-to` → **[Immune system](../immune-system/README.md)** — Reproductive immunology: the reproductive system depends on the immune system for the materno-fetal tolerance (regulatory T cells and uterine NK cells already mapped) that lets a semi-allogeneic fetus be carried, a deep interface between the two systems.
- `connects-to` → **[Breast cancer](../breast-cancer/README.md)** — Hormone-driven cancer: the sex steroids of the reproductive system (estrogen and progesterone already mapped) drive breast cancer, whose hormone-receptor status guides the endocrine therapy targeting the reproductive-endocrine axis.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Fertilisation calcium signalling: calcium is central to reproduction, from the acrosome reaction of the sperm to the calcium wave that activates the oocyte at fertilisation, triggering the start of embryonic development.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Reproductive iron demand: hepcidin governs the iron (already mapped) balance stressed by the menstrual blood loss and, in pregnancy, the large iron demand of the growing fetus, linking reproduction to systemic iron handling.
- `connects-to` → **[Nervous system](../nervous-system/README.md)** — Neuroendocrine control: the hypothalamic GnRH pulse generator of the nervous system (via the brain already mapped) drives the pituitary gonadotrophins that command the reproductive system, the neural control of reproduction.
- `connects-to` → **[Endometrial cancer](../endometrial-cancer/README.md)** — Hormone-driven cancer: unopposed oestrogen (already mapped) drives endometrial cancer of the female reproductive tract, a hormone-dependent malignancy of the reproductive system's target organs.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipose-reproductive axis: adiponectin, with leptin (already mapped), links the body fat to the puberty, the fertility and the PCOS (insulin already mapped) of the reproductive system.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Metabolic-reproductive adipokine: resistin, with leptin and adiponectin (already mapped), is the adipokine of the metabolic-reproductive link (PCOS, insulin already mapped) of the reproductive system.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Uterine histamine: the histamine of the uterine and decidual mast cells modulates the implantation, the labour and the reproductive-tract vascular function of the reproductive system.
- `connects-to` → **[Regulatory T cell](../../04-cellular/regulatory-t-cell/README.md)** — Maternal-fetal tolerance: the regulatory T cells expand to maintain the maternal tolerance of the fetal allograft, central to the immune-reproductive interface of the reproductive system.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Decidual immunity: the IFN-γ of the uterine/decidual NK cells (already mapped) shapes the spiral-artery remodelling and the maternal-fetal immunology of the reproductive system.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Reproductive-tract antiviral: the type-I interferon defends the reproductive-tract mucosa against the sexually-transmitted viruses, part of the mucosal immunity of the reproductive system.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Th2 maternal-fetal tolerance: IL-4, a type-2 cytokine, promotes the Th2-skewed immune tolerance at the maternal-fetal interface that permits the semi-allogeneic pregnancy of the reproductive system.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Th2 arm: IL-13, with IL-4 (already mapped), is part of the type-2 immune bias of the maternal-fetal tolerance of the reproductive system.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 counter-arm: IL-12 polarises the Th1 (IFN-γ already mapped) arm whose excess (opposing the Th2 tolerance) is implicated in the recurrent pregnancy loss of the reproductive system.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the uterine and endometrial immune milieu of the reproductive system.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 arm), whose balance with the regulatory T cells governs the maternal-fetal tolerance and, in excess, the pre-eclampsia/pregnancy-loss of the reproductive system.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 antibody dimension of the maternal-fetal immune bias of the reproductive system.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Placental complement: the complement C3 activation, tightly restrained by the placental complement regulators, is central to the maternal-fetal tolerance and, when dysregulated, the pre-eclampsia of the reproductive system.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Decidual antigen presentation: the tolerogenic dendritic cells of the decidua present the fetal antigen and, with the regulatory T cells (already mapped), maintain the maternal-fetal tolerance of the reproductive system.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Uterine mast cells: the mast cells of the uterus and the male tract contribute to the implantation, the tissue remodelling and the parturition of the reproductive system.

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

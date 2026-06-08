---
schema: human-scale-entry/v1
id: xanthine-oxidase
name: Xanthine Oxidase
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "Xanthine oxidase (XOR/XDH) catalyzes hypoxanthine → xanthine → uric acid, generating reactive oxygen species; hyperuricemia → MSU crystal deposition → NLRP3-driven gouty arthritis; allopurinol and febuxostat inhibit XOR to reduce uric acid in gout and chronic hyperuricemia."
aliases: ["xanthine oxidase", "XOR", "XDH", "xanthine dehydrogenase", "xanthine oxidoreductase", "XO", "uric acid enzyme", "allopurinol target", "febuxostat target", "purine catabolism"]
cross_links:
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "Xanthine oxidase converts xanthine → uric acid; serum urate >6.8 mg/dL exceeds solubility threshold → MSU crystal nucleation in joints and soft tissue → phagocytosis by neutrophils and macrophages → NLRP3 activation → acute gouty flare; allopurinol/febuxostat target XOR."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "MSU crystals activate NLRP3 inflammasome in macrophages via lysosomal rupture → cathepsin B → IL-1β → acute gouty inflammation; colchicine inhibits microtubule-dependent crystal processing → blunts NLRP3 activation; IL-1β inhibitors (canakinumab) abort acute gout flares."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "XOR-derived superoxide and H2O2 oxidize BH4 → eNOS uncoupling → reduced NO → endothelial dysfunction and hypertension; hyperuricemia is associated with increased cardiovascular risk; allopurinol reduces MACE in some observational studies."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Hyperuricemia promotes CKD progression via interstitial uric acid crystal deposition, renal vasoconstriction, and NLRP3-driven tubular inflammation; XOR inhibitors (allopurinol, febuxostat) modestly slow eGFR decline in hyperuricemic CKD patients in some clinical trials."
sources:
  - id: dalbeth-2016-gout-review
    type: peer-reviewed
    cite: "Dalbeth N, Merriman TR, Stamp LK. Gout. Lancet. 2016;388(10055):2039-2052."
    doi: "10.1016/S0140-6736(16)00346-9"
    pmid: "27112094"
    url: "https://doi.org/10.1016/S0140-6736(16)00346-9"
  - id: white-2018-cares-febuxostat
    type: peer-reviewed
    cite: "White WB, Saag KG, Becker MA, et al. Cardiovascular safety of febuxostat or allopurinol in patients with gout. N Engl J Med. 2018;378(13):1200-1210."
    doi: "10.1056/NEJMoa1710895"
    pmid: "29527974"
    url: "https://doi.org/10.1056/NEJMoa1710895"
---

# Xanthine Oxidase

## Overview

**Xanthine oxidase** (XOR; xanthine oxidoreductase; gene *XDH*, chromosome 2p23.1) is a **molybdenum-containing metalloenzyme** that catalyzes the terminal two steps of **purine catabolism** in humans: hypoxanthine → xanthine → **uric acid**. In doing so, XOR transfers electrons to molecular oxygen, generating **superoxide anion (O₂⁻) and hydrogen peroxide (H₂O₂)** — making XOR a major source of reactive oxygen species (ROS) in vascular endothelium, liver, and intestine.

The pathological significance of XOR is twofold:
1. **Uric acid overproduction/underexcretion** → hyperuricemia → **monosodium urate (MSU) crystal deposition** → NLRP3 inflammasome-mediated gouty arthritis — the most common inflammatory arthropathy in adults
2. **XOR-derived ROS** → oxidative stress → endothelial dysfunction, vascular disease, and ischemia-reperfusion injury

XOR inhibitors are the cornerstone of urate-lowering therapy (ULT): **allopurinol** (a xanthine analog, metabolized to oxypurinol which tightly binds the enzyme) is the most widely prescribed urate-lowering agent globally; **febuxostat (Uloric)** is a non-purine, highly selective XOR inhibitor approved for gout [^white-2018-cares-febuxostat]. Dalbeth et al. (2016) provided the comprehensive review of gout pathophysiology [^dalbeth-2016-gout-review].

**Uric acid and human evolution:**
Humans and great apes are the only mammals with high serum urate (~5–7 mg/dL) because we carry inactivating mutations in the **uricase (URIC1/UOX)** gene, unlike most mammals which further catabolize uric acid to allantoin (much more soluble). The loss of uricase in hominid evolution is hypothesized to have conferred a blood pressure-raising advantage during periods of dietary salt scarcity (uric acid activates the RAAS) — but now predisposes to gout and hypertension in the context of modern caloric excess and purine-rich diets.

## Structure

XOR is a **homodimer** (each subunit ~145 kDa) with three major functional domains per subunit:

**2Fe-2S iron-sulfur clusters (N-terminal; "2Fe-2S I and II"):**
- Accept electrons from the molybdenum cofactor and transfer them to FAD
- Essential for electron shuttling; disruption causes XOR inactivity

**FAD-binding domain (central):**
- Flavin adenine dinucleotide prosthetic group
- Terminal electron acceptor; transfers electrons to O₂ (XO form → O₂⁻/H₂O₂) or NAD⁺ (XDH form → NADH)
- The FAD domain is the site of action of **DPI (diphenyleneiodonium)** — a broad flavoenzyme inhibitor used experimentally to implicate XOR in ROS production

**Molybdenum cofactor (Mo-co; C-terminal catalytic domain):**
- Molybdopterin complex; coordinates the catalytic molybdenum center
- Xanthine binds here; Mo⁶⁺ → Mo⁴⁺ reduction during xanthine oxidation
- **Allopurinol** is metabolized by XOR to **oxypurinol** which is a tight-binding inhibitor of the Mo cofactor active site (irreversible-like slow-tight binding)
- **Febuxostat** binds the Mo-co channel in a non-competitive manner with a distinct binding mode (does not occupy the substrate site directly) → high selectivity for XOR over other molybdopterin enzymes

**XOR interconversion (XDH ↔ XO):**
- Native form: **xanthine dehydrogenase (XDH)** — uses NAD⁺ as electron acceptor → produces NADH + uric acid; minimal O₂⁻ production
- Under oxidative stress or ischemia: **proteolytic cleavage** or **reversible oxidation of cysteine residues (Cys535/Cys992)** → converts to **xanthine oxidase (XO form)** — uses O₂ → produces O₂⁻ and H₂O₂
- This interconversion is particularly important in **ischemia-reperfusion injury**: ischemia accumulates xanthine and converts XDH → XO; reperfusion delivers O₂ → burst of XOR-generated ROS → tissue injury

## Function

**Purine catabolism pathway:**
Adenosine/AMP → (adenosine deaminase) → Inosine → Hypoxanthine → (XOR) → Xanthine → (XOR) → Uric Acid

- **Uric acid** is the terminal metabolite of purine catabolism in humans; excreted primarily by the kidney (2/3) and intestine/gut bacteria (1/3)
- **Serum urate** is ~3–7 mg/dL in healthy adults (women lower due to estrogenic effects on URAT1)
- **MSU crystallization threshold:** 6.8 mg/dL at pH 7.4 and 37°C; lower in cooler peripheral joints (1st MTP joint temperature ~28°C) → explains the predilection for the first metatarsophalangeal (podagra) location

**Sources of hyperuricemia:**
- **Underexcretion (90% of cases):** Reduced renal urate excretion via URAT1 (SLC22A12), GLUT9 (SLC2A9), and OAT transporters; genetic variants in these transporters are the dominant cause of hyperuricemia
- **Overproduction (10%):** XOR overactivity due to high purine load (red meat, organ meats, shellfish, beer/spirits), cellular turnover (myeloproliferative disorders, tumor lysis syndrome), or Lesch-Nyhan syndrome (HPRT1 mutation → failed purine recycling → XOR substrate excess)
- **Both:** Chronic kidney disease (reduced renal excretion); diuretic therapy (thiazides, loop diuretics → volume contraction → increased urate reabsorption via URAT1)

**XOR and endothelial/vascular biology:**
- XO (the oxidase form) is expressed on endothelial cell surfaces (circulating XOR binds endothelial proteoglycans/glycosaminoglycans)
- Endothelial XO → O₂⁻ → peroxynitrite (with eNOS-derived NO) → BH4 oxidation → eNOS uncoupling → vicious cycle of reduced NO and increased ROS → endothelial dysfunction
- XOR-derived ROS is also relevant to: aldosterone-induced vascular damage, angiotensin II signaling, inflammatory cytokine production from macrophages

## Mechanism

**Urate crystal formation and NLRP3 activation:**

1. **Hyperuricemia → MSU crystallization:** Serum urate above 6.8 mg/dL exceeds the solubility product of MSU; crystals form preferentially in avascular tissue (cartilage, tendon), cooler peripheral joints, and joints with high collagen/proteoglycan content that seeds crystallization
2. **MSU recognition:** Crystals are recognized by macrophages and neutrophils via **TLR2/4** (surface pattern recognition → NF-kB → pro-IL-1β and NLRP3 priming) and **integrins** → phagocytosis
3. **Lysosomal destabilization:** MSU crystals' needle-like morphology → mechanically disrupts phagolysosomal membrane → cathepsin B release → cytoplasmic NLRP3 activation
4. **NLRP3 inflammasome assembly:** NLRP3-ASC-pro-caspase-1 complex → caspase-1 → IL-1β (mature) → release → profound local inflammation (redness, warmth, swelling, severe pain)
5. **Neutrophil influx:** IL-1β + IL-8/CXCL1 → massive neutrophil recruitment → neutrophil extracellular traps (NETs) → further crystal phagocytosis → ROS → tissue destruction

**XOR inhibitor mechanisms:**

- **Allopurinol:** A structural analog of hypoxanthine; metabolized by XOR to **oxypurinol** which is tightly bound to the reduced Mo⁴⁺ molybdenum center → irreversible-like inhibition; also reduces xanthine reabsorption; half-life of allopurinol ~2h but oxypurinol ~15h (once-daily dosing); dose-adjusted for CKD; rare but serious: allopurinol hypersensitivity syndrome (AHS/DRESS, ~1:1000; HLA-B*58:01 associated — screen in East Asians)
- **Febuxostat:** Non-purine heterocyclic compound; binds XOR Mo-co channel (both oxidized and reduced forms) with high affinity and selectivity; not renally cleared (hepatic metabolism) → no dose adjustment needed in mild-moderate CKD; **CARES trial** showed higher all-cause mortality with febuxostat vs. allopurinol (driven by CV death) in patients with established CVD — now carries FDA boxed warning; subsequent analyses suggest confounding

**Uricosuric drugs (alternate mechanism):** Probenecid, benzbromarone, lesinurad (URAT1 inhibitor, discontinued) — increase renal urate excretion by blocking tubular reabsorption; used in combination or when XOR inhibitors are contraindicated

**Novel approaches:**
- **Pegloticase (Krystexxa):** Recombinant porcine-baboon chimeric uricase; converts urate → allantoin (10× more soluble); IV every 2 weeks; reserved for refractory tophaceous gout; limited by immunogenicity (anti-drug antibodies → loss of efficacy in ~40%)
- **Arhalofenate, RDEA3170:** Selective URAT1 inhibitors in development for gout with cardiovascular safety profiles

## Connections

Xanthine oxidase converts xanthine → uric acid; serum urate >6.8 mg/dL exceeds solubility threshold → MSU crystal nucleation in joints and soft tissue → phagocytosis by neutrophils and macrophages → NLRP3 activation → acute gouty flare; allopurinol/febuxostat target XOR.

MSU crystals activate NLRP3 inflammasome in macrophages via lysosomal rupture → cathepsin B → IL-1β → acute gouty inflammation; colchicine inhibits microtubule-dependent crystal processing → blunts NLRP3 activation; IL-1β inhibitors (canakinumab) abort acute gout flares.

XOR-derived superoxide and H2O2 oxidize BH4 → eNOS uncoupling → reduced NO → endothelial dysfunction and hypertension; hyperuricemia is associated with increased cardiovascular risk; allopurinol reduces MACE in some observational studies.

Hyperuricemia promotes CKD progression via interstitial uric acid crystal deposition, renal vasoconstriction, and NLRP3-driven tubular inflammation; XOR inhibitors (allopurinol, febuxostat) modestly slow eGFR decline in hyperuricemic CKD patients in some clinical trials.

[^dalbeth-2016-gout-review]: Dalbeth N, Merriman TR, Stamp LK. Gout. *Lancet.* 2016;388(10055):2039-2052. [doi:10.1016/S0140-6736(16)00346-9](https://doi.org/10.1016/S0140-6736(16)00346-9) · [PubMed 27112094](https://pubmed.ncbi.nlm.nih.gov/27112094/)
[^white-2018-cares-febuxostat]: White WB, Saag KG, Becker MA, et al. Cardiovascular safety of febuxostat or allopurinol in patients with gout. *N Engl J Med.* 2018;378(13):1200-1210. [doi:10.1056/NEJMoa1710895](https://doi.org/10.1056/NEJMoa1710895) · [PubMed 29527974](https://pubmed.ncbi.nlm.nih.gov/29527974/)

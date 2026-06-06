---
schema: medicine-entry/v1
id: omeprazole
name: Omeprazole
atlas: 03-medicine
scale: 01-modern
status: draft
last_reviewed: 2026-06-06
summary: "Proton pump inhibitor (PPI); irreversibly inactivates H⁺/K⁺-ATPase on parietal cells → ≥95% acid suppression. First-line for peptic ulcer, GERD, Zollinger-Ellison syndrome, and H. pylori eradication. Sold as Prilosec/Losec."
aliases: ["omeprazole", "Prilosec", "Losec", "Mepral", "Omepral", "5-methoxy-2-[(4-methoxy-3,5-dimethylpyridin-2-yl)methylsulfinyl]-1H-benzo[d]imidazole"]
sources:
  - id: fellenius-1981-omeprazole
    type: peer-reviewed
    cite: "Fellenius E, Berglindh T, Sachs G, et al. Substituted benzimidazoles inhibit gastric acid secretion by blocking (H+ + K+)ATPase. Nature. 1981;290(5802):159-61."
    doi: "10.1038/290159a0"
    pmid: "7207579"
    url: "https://doi.org/10.1038/290159a0"
  - id: hunt-1999-ppi-hp
    type: peer-reviewed
    cite: "Hunt RH, Fallone C, Veldhuyzen van Zanten S, et al. Etiology of peptic ulcer disease — new approach. Eur J Gastroenterol Hepatol. 1999;11 Suppl 2:S5-11."
    pmid: "10575154"
    url: "https://pubmed.ncbi.nlm.nih.gov/10575154/"
  - id: moayyedi-2016-ppi-gerd
    type: peer-reviewed
    cite: "Moayyedi P, Santana J, Khan M, Preston C, Donnellan C. Medical treatments in the short term management of reflux oesophagitis. Cochrane Database Syst Rev. 2007;(2):CD003244."
    doi: "10.1002/14651858.CD003244.pub2"
    pmid: "17443527"
    url: "https://doi.org/10.1002/14651858.CD003244.pub2"
  - id: malfertheiner-2022-hp-guidelines
    type: clinical-guideline
    cite: "Malfertheiner P, Megraud F, Rokkas T, et al. Management of Helicobacter pylori infection: the Maastricht VI/Florence consensus report. Gut. 2022;71(9):1724-1762."
    doi: "10.1136/gutjnl-2022-327745"
    pmid: "35707400"
    url: "https://doi.org/10.1136/gutjnl-2022-327745"
cross_links:
  - target: 01-human/06-organ/stomach
    relation: targets
    evidence: fellenius-1981-omeprazole
    note: "Omeprazole concentrates in the acidic secretory canaliculi of parietal cells, where it is protonated and converted to the active sulfenamide form that covalently binds Cys813 and Cys892 of H⁺/K⁺-ATPase, irreversibly inhibiting acid secretion."
  - target: 03-medicine/01-modern/06-antimicrobial
    relation: part-of
    note: "Omeprazole is a required component of triple and quadruple H. pylori eradication regimens — it raises intragastric pH, enhancing antibiotic stability and efficacy."
---

# Omeprazole

## Overview

**Omeprazole** (brand names: Prilosec, Losec) is a **proton pump inhibitor (PPI)** — the first compound in its class, approved in 1988 — and remains one of the most widely prescribed drugs globally. It is a benzimidazole derivative that acts as a **prodrug**: systemically inactive in the circulation, it accumulates and is activated specifically within the highly acidic secretory canaliculi of gastric parietal cells, where it irreversibly inhibits the **H⁺/K⁺-ATPase** (the "proton pump"), the final enzymatic step in gastric acid secretion.

Omeprazole is the cornerstone pharmacotherapy for **gastroesophageal reflux disease (GERD)**, **peptic ulcer disease (PUD)**, **Zollinger-Ellison syndrome**, and **H. pylori eradication regimens**. Its discovery in the late 1970s — from the systematic screening of benzimidazoles by Astra's Hässle laboratory and the identification of H⁺/K⁺-ATPase as the target — represented a paradigm shift in gastroenterology [^fellenius-1981-omeprazole].

## Mechanism

**Prodrug activation:**
1. Omeprazole is a weak base (pKa ~4.0) absorbed in the small intestine (bioavailability ~40–65%, improved with repeat dosing as acid-labile destruction decreases)
2. Distributes systemically and selectively accumulates in the acidic secretory canaliculi of parietal cells (pH ~1–2), where the local acid environment protonates the drug
3. The protonated form undergoes a non-enzymatic rearrangement via a spiro intermediate to form the **sulfenamide** (active form)
4. The sulfenamide is highly reactive and forms **covalent disulfide bonds** with cysteine residues (Cys813 and Cys892) on the luminal face of the α-subunit of H⁺/K⁺-ATPase
5. This irreversible binding permanently inactivates the pump — acid secretion from that pump molecule can only resume after new pump protein is synthesized (t½ pump turnover ~18–24 h)

**H⁺/K⁺-ATPase (proton pump) biology:**
- Located on the apical membrane of parietal cells (gastric corpus)
- Uses ATP hydrolysis to exchange 2 H⁺ (secreted into stomach lumen) for 2 K⁺ (imported) — generates the extreme pH gradient of the gastric lumen (~pH 1–2 vs. intracellular pH 7.2)
- The sole final pathway for acid secretion regardless of the stimulus (acetylcholine, histamine, gastrin)

**Net effect:** Single daily omeprazole dose (20 mg) inhibits ~70–80% of pump molecules on active secreting cells; maximal effect at 3–5 days of repeated dosing (not all pumps are actively secreting at any given moment) → pH >4 maintained for >14–16 hours/day, sufficient for ulcer healing.

## Clinical Use

**GERD:**
- Standard dose: 20 mg once daily before breakfast × 4–8 weeks; 40 mg for severe/erosive esophagitis
- Maintenance: 10–20 mg OD for chronic/recurrent GERD
- Cochrane evidence: PPIs superior to H₂ blockers and placebo for symptom relief and mucosal healing of erosive esophagitis [^moayyedi-2016-ppi-gerd]

**Peptic Ulcer Disease:**
- Duodenal ulcer: 20 mg OD × 4 weeks (healing ~90–95%)
- Gastric ulcer: 20 mg OD × 8 weeks (healing ~85–90%)
- NSAID-induced ulcer: healing and prevention (20 mg OD as prophylaxis in high-risk patients on NSAIDs)

**H. pylori eradication:**
- Standard triple therapy (Maastricht VI/Florence 2022): PPI + clarithromycin + amoxicillin (or metronidazole) × 14 days [^malfertheiner-2022-hp-guidelines]
- Bismuth quadruple: PPI + bismuth + metronidazole + tetracycline × 14 days (preferred in areas with high clarithromycin resistance >15%)
- PPI role: raises intragastric pH >6, stabilizing antibiotics (especially clarithromycin, which degrades rapidly at low pH) and enhancing bacterial sensitivity

**Zollinger-Ellison Syndrome:**
- Gastrinoma-driven hypersecretion: high-dose omeprazole (60–120 mg/day, divided); titrate to acid output <10 mEq/h

**Key adverse effects:**
- Short-term: headache, nausea, diarrhea (generally mild)
- Long-term (≥1 year): hypomagnesemia, vitamin B12 deficiency (reduced intrinsic factor-independent absorption), increased risk of *Clostridioides difficile* infection, bone density reduction (osteoporotic fracture risk modest, ~20% increased relative risk)
- Drug interactions: reduced clopidogrel efficacy via CYP2C19 competition (omeprazole is a CYP2C19 inhibitor); reduced iron/atazanavir/ketoconazole absorption (pH-dependent)

**CYP2C19 pharmacogenomics:** Poor metabolizers (CYP2C19*2/*3 — ~2–5% Caucasians, 12–23% Asians) have 3–5× higher omeprazole AUC — may require dose reduction; ultra-rapid metabolizers may have reduced efficacy.

## Evidence

| Study/Review | Population | Key Finding |
|:---|:---|:---|
| Cochrane PPI vs H₂RA (Moayyedi 2007) [^moayyedi-2016-ppi-gerd] | Erosive esophagitis RCTs | PPIs significantly superior to H₂ blockers for 4-week healing (OR ~0.33 for non-healing with PPIs vs H₂RAs) |
| Maastricht VI/Florence 2022 [^malfertheiner-2022-hp-guidelines] | H. pylori management guideline | PPI-based triple therapy 80–90% eradication with clarithromycin-susceptible strains; bismuth quadruple preferred empirically in high-resistance areas |
| NSAID gastroprotection RCTs | High-risk NSAID users | Omeprazole 20 mg OD reduces NSAID-associated ulcer by ~80% vs placebo |
| Mechanism landmark (Fellenius 1981) [^fellenius-1981-omeprazole] | In vitro/animal | Identification of H⁺/K⁺-ATPase as the target; covalent inactivation mechanism established |

## Connections

- **Targets** → [Stomach parietal cell H⁺/K⁺-ATPase](../../../../../01-human/06-organ/stomach/README.md): Irreversibly inactivates the proton pump via covalent sulfenamide bond to Cys813/Cys892, blocking all acid secretion regardless of stimulus.
- **Part-of** → [H. pylori Eradication Regimens](../../06-antimicrobial/README.md): Omeprazole is obligatory in triple and quadruple therapy — pH >6 enhances antibiotic stability and bactericidal activity.

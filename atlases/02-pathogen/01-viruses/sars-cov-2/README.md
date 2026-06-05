---
schema: pathogen-entry/v1
id: sars-cov-2
name: SARS-CoV-2 (cardiac effects)
atlas: 02-pathogen
scale: 01-viruses
status: draft
last_reviewed: 2026-06-03
summary: "Betacoronavirus (Coronaviridae). Cardiac focus: ACE2-dependent entry into cardiomyocytes, direct viral myocarditis, immune-mediated myocardial injury, microvascular dysfunction, and systemic cardiovascular consequences of COVID-19."
aliases: ["COVID-19 cardiac", "SARS-CoV-2 myocarditis", "2019-nCoV"]
sources:
  - id: lindner-2020-cardiac-involvement
    type: peer-reviewed
    cite: "Lindner D, Fitzek A, Brauninger H, et al. Association of cardiac infection with SARS-CoV-2 in confirmed COVID-19 autopsy cases. JAMA Cardiol. 2020;5(11):1281-5."
    doi: "10.1001/jamacardio.2020.3551"
    pmid: "32730555"
    url: "https://doi.org/10.1001/jamacardio.2020.3551"
  - id: giustino-2020-cardiac-complications
    type: peer-reviewed
    cite: "Giustino G, Croft LB, Stefanini GG, et al. Characterization of myocardial injury in patients with COVID-19. J Am Coll Cardiol. 2020;76(18):2043-55."
    doi: "10.1016/j.jacc.2020.08.069"
    pmid: "33121713"
    url: "https://doi.org/10.1016/j.jacc.2020.08.069"
  - id: eiros-2020-myocarditis-cmr
    type: peer-reviewed
    cite: "Eiros R, Barreiro-Perez M, Martin-Garcia A, et al. Pericarditis and myocarditis long after SARS-CoV-2 infection. A cross-sectional descriptive study in healthcare workers. medRxiv. 2020."
    doi: "10.1101/2020.07.12.20151316"
    pmid: "32699853"
    url: "https://doi.org/10.1101/2020.07.12.20151316"
  - id: bhatt-2022-covid-cardiovascular
    type: peer-reviewed
    cite: "Bhatt DL, Lopes RD, Harrington RA. Diagnosis and treatment of acute coronary syndromes: a review. JAMA. 2022;327(7):662-675."
    doi: "10.1001/jama.2022.0358"
    pmid: "35166796"
    url: "https://doi.org/10.1001/jama.2022.0358"
  - id: hoffmann-2020-ace2-entry
    type: peer-reviewed
    cite: "Hoffmann M, Kleine-Weber H, Schroeder S, et al. SARS-CoV-2 Cell Entry Depends on ACE2 and TMPRSS2 and Is Blocked by a Clinically Proven Protease Inhibitor. Cell. 2020;181(2):271-280."
    doi: "10.1016/j.cell.2020.02.052"
    pmid: "32142651"
    url: "https://doi.org/10.1016/j.cell.2020.02.052"
cross_links:
  - target: 01-human/04-cellular/cardiomyocyte
    relation: infects
    note: "SARS-CoV-2 spike protein binds ACE2 on cardiomyocytes; direct viral infection demonstrated by in situ hybridization in autopsy studies."
  - target: 01-human/05-tissue/myocardium
    relation: damages
    note: "Myocarditis (lymphocytic and macrophage infiltration), microvascular injury, and cardiomyocyte death — demonstrable by cardiac MRI and autopsy."
  - target: 01-human/07-system/cardiovascular-system
    relation: damages
    note: "Systemic cardiovascular effects: acute MI (plaque rupture, microvascular thrombosis), arrhythmias, right heart failure (pulmonary hypertension), and endothelial dysfunction."
  - target: 01-human/06-organ/lung
    relation: damages
    note: "SARS-CoV-2 causes diffuse alveolar damage (DAD) and ARDS in severe COVID-19: bilateral alveolar flooding, hyaline membranes, and loss of surfactant — the most lethal pulmonary manifestation."
  - target: 01-human/07-system/immune-system
    relation: damages
    note: "SARS-CoV-2 evades innate immunity (NSP1/NSP3 block IFN-I production, ORF3b suppresses IFN signaling), depletes lymphocytes, and triggers dysregulated cytokine storm causing immune organ failure in severe COVID-19."
  - target: 01-human/04-cellular/dendritic-cell
    relation: infects
    note: "SARS-CoV-2 infects plasmacytoid DCs (via CLEC4M/DC-SIGN, ACE2-independent), impairing type I IFN production and antigen presentation early in infection."
  - target: 01-human/04-cellular/t-helper-cell
    relation: infects
    note: "Direct infection of CD4+ T cells demonstrated in autopsy tissue; contributes to lymphopenia and CD4 depletion observed in severe COVID-19, impairing adaptive immune response."
  - target: 01-human/05-tissue/glomerulus
    relation: damages
    note: "COVID-19-associated nephropathy: SARS-CoV-2 infects ACE2-expressing glomerular cells, causing collapsing focal segmental glomerulosclerosis (FSGS), particularly in APOL1 high-risk genotype patients."
  - target: 01-human/04-cellular/hepatocyte
    relation: damages
    note: "ACE2 is expressed in hepatocytes and cholangiocytes; direct viral hepatitis and ischemic/drug-induced liver injury contribute to enzyme elevation (ALT/AST ×3–5 ULN) in 14–53% of hospitalized patients."
  - target: 01-human/04-cellular/podocyte
    relation: damages
    note: "Podocyte ACE2-mediated viral entry leads to foot process effacement and slit diaphragm disruption, causing collapsing glomerulopathy in COVID-19 AKI."
  - target: 01-human/06-organ/kidney
    relation: damages
    note: "AKI occurs in 5–30% of hospitalized and up to 50% of ICU COVID-19 patients via cytopathic effect, cytokine storm-mediated tubular injury, microvascular thrombosis, and hemodynamic compromise."
  - target: 01-human/06-organ/liver
    relation: damages
    note: "COVID-19 liver injury includes direct viral hepatitis, ischemic hepatitis in severe cases, and drug-induced liver injury from COVID-19 treatments (remdesivir, dexamethasone)."
  - target: 01-human/07-system/digestive-system
    relation: damages
    note: "GI manifestations occur in ~17% of patients (diarrhea, nausea, abdominal pain); ACE2 in enterocytes enables viral replication in gut epithelium; fecal-oral transmission potential documented."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: target-of
    note: "Neutralizing IgG antibodies targeting the spike RBD (and S2 fusion domain) are the primary adaptive humoral defense against SARS-CoV-2; anti-spike IgG titers correlate with protection against reinfection and severe disease."
---

# SARS-CoV-2 (cardiac effects)

## Overview

SARS-CoV-2 is a **betacoronavirus** (genus *Betacoronavirus*, family *Coronaviridae*) with a ~30 kb positive-sense single-stranded RNA genome, an enveloped particle 80–120 nm in diameter, and a distinctive spike (S) protein trimer on its surface that mediates receptor binding and membrane fusion. The primary receptor is **angiotensin-converting enzyme 2 (ACE2)**, which is expressed not only in the respiratory epithelium — the primary site of replication — but also on **cardiomyocytes**, cardiac fibroblasts, endothelial cells, and pericytes [^hoffmann-2020-ace2-entry]. This broad cardiac expression pattern is the molecular basis for the diverse cardiovascular manifestations of COVID-19.

Cardiac involvement in COVID-19 ranges from asymptomatic troponin elevation (observed in 20–30% of hospitalized patients) to fulminant myocarditis, cardiogenic shock, and sudden cardiac death. The mechanisms are multiple and operate at different scales — from direct viral infection of cardiomyocytes, to immune-mediated myocardial injury, to systemic effects of the endotheliopathy, coagulopathy, and cytokine storm that characterize severe disease [^giustino-2020-cardiac-complications].

## Structure

SARS-CoV-2 key components relevant to cardiac pathophysiology:

| Protein | Function | Cardiac relevance |
|:---|:---|:---|
| **Spike (S)** | ACE2 binding (S1), membrane fusion (S2); primed by TMPRSS2 | ACE2 on cardiomyocytes and endothelium is the entry receptor |
| **RNA-dependent RNA polymerase (NSP12)** | Genome replication | Target of remdesivir |
| **M (membrane) protein** | Structural; immunosuppressive, counteracts IFN | Immune evasion during early infection |
| **N (nucleocapsid)** | RNA packaging, replication complex | Diagnostic antigen; may contribute to intracellular pathology |

## Infection Mechanism

SARS-CoV-2 cell entry requires binding of the spike (S1) subunit to **ACE2** on the target cell surface, followed by priming of the S2 subunit by the serine protease **TMPRSS2** (or endosomal cathepsins), enabling membrane fusion and genome delivery [^hoffmann-2020-ace2-entry]. ACE2 is expressed on cardiomyocytes, cardiac endothelial cells, pericytes, and fibroblasts — providing multiple cardiac entry routes. The minimal infectious dose via aerosol is estimated at 10–100 viral particles; viral load in respiratory secretions peaks ~1–3 days before symptom onset.

## Host Interactions

### ACE2 on Cardiomyocytes

ACE2 is a **carboxypeptidase** and a key regulator of the renin-angiotensin-aldosterone system (RAAS): it converts angiotensin II (pro-inflammatory, vasoconstrictive) to angiotensin 1-7 (cardioprotective, vasodilatory). When SARS-CoV-2 binds and internalizes ACE2, it downregulates surface ACE2 expression, shifting the local RAAS balance toward excess angiotensin II — with potential downstream effects on cardiomyocyte inflammation, oxidative stress, and fibrosis [^hoffmann-2020-ace2-entry].

Direct viral infection of cardiomyocytes has been confirmed in autopsy studies using in situ hybridization for SARS-CoV-2 RNA and electron microscopy showing virions within cardiac cells [^lindner-2020-cardiac-involvement]. However, the magnitude of direct viral cardiac infection is modest in most cases; immune-mediated mechanisms appear to dominate clinically.

## Mechanisms of Cardiac Injury

### 1. Direct Viral Myocarditis

A subset of COVID-19 patients develop biopsy- or cardiac MRI-confirmed myocarditis with lymphocytic infiltration of the myocardium, late gadolinium enhancement, and elevated troponin. The mechanism involves both direct viral cytolysis and immune-cell-mediated myocyte killing, paralleling CVB myocarditis.

### 2. Immune-Mediated Injury (Cytokine Storm)

Severe COVID-19 triggers a systemic hyperinflammatory state (cytokine storm) with markedly elevated IL-6, IL-1β, TNF-α, and ferritin. Myocardial inflammation in this context is partly a bystander effect of systemic inflammation rather than direct viral replication in the heart. Macrophage activation syndrome (MAS)-like phenotypes have been described in fatal COVID-19 with prominent cardiac involvement.

### 3. Microvascular Thrombosis and Coronary Plaque Destabilization

SARS-CoV-2 induces an **endotheliopathy** with endothelial cell activation, loss of antithrombotic properties, platelet hyperactivation, and a coagulopathy characterized by elevated D-dimer, fibrinogen, and von Willebrand factor. This creates conditions for:

- Coronary microvascular thrombosis (type 2 MI)
- Acute plaque rupture in patients with pre-existing atherosclerosis (type 1 MI)
- Pulmonary embolism → right ventricular pressure overload → right heart failure

### 4. Arrhythmias

QTc prolongation, atrial fibrillation, and ventricular arrhythmias are common in hospitalized COVID-19 patients. Mechanisms include myocardial inflammation (disrupts conduction), electrolyte derangements, hypoxia, catecholamine surge, and direct viral effects on ion-channel expression.

### 5. Right Ventricular Failure

Severe ARDS-related hypoxic pulmonary vasoconstriction, pulmonary embolism, and high PEEP ventilation all increase right ventricular afterload, precipitating acute cor pulmonale in critically ill patients.

## Pathology

### Cardiac Pathology Summary

| Syndrome | Frequency | Mechanism |
|:---|:---|:---|
| Troponin elevation (asymptomatic) | 20–30% of hospitalized | Demand ischemia, microvascular injury, myocarditis |
| Acute myocarditis (clinical) | 1–5% of hospitalized | Direct viral, immune-mediated |
| Type 1 MI | ~2–4% of hospitalized | Plaque rupture in setting of inflammation |
| Type 2 MI | ~5–10% of hospitalized | Demand-supply mismatch, microvascular |
| Arrhythmia | 5–20% of hospitalized | Multi-factorial (see above) |
| Right heart failure | Uncommon, high mortality | Pulmonary hypertension, PE |

Long COVID cardiac symptoms (palpitations, orthostatic tachycardia, dyspnea on exertion) are observed in a substantial minority of patients months after acute infection; the mechanism is under active investigation [^eiros-2020-myocarditis-cmr].

## Connections

- **Infects** → [Cardiomyocyte](../../../01-human/04-cellular/cardiomyocyte/README.md): ACE2-dependent SARS-CoV-2 entry; direct cardiomyocyte infection confirmed in autopsy specimens; functional consequences include contraction impairment and troponin release.
- **Damages** → [Myocardium](../../../01-human/05-tissue/myocardium/README.md): Lymphocytic myocarditis, macrophage infiltration, microvascular injury, edema, late gadolinium enhancement on CMR.
- **Damages** → [Cardiovascular System](../../../01-human/07-system/cardiovascular-system/README.md): Systemic endotheliopathy, coagulopathy, pulmonary hypertension, acute MI, atrial fibrillation, right heart failure.

## See Also

- [Cardiomyocyte entry](../../../01-human/04-cellular/cardiomyocyte/README.md)
- [Myocardium entry](../../../01-human/05-tissue/myocardium/README.md)
- [Cardiovascular System entry](../../../01-human/07-system/cardiovascular-system/README.md)

[^hoffmann-2020-ace2-entry]: Hoffmann M, Kleine-Weber H, Schroeder S, et al. SARS-CoV-2 Cell Entry Depends on ACE2 and TMPRSS2. *Cell.* 2020;181(2):271-280. [doi:10.1016/j.cell.2020.02.052](https://doi.org/10.1016/j.cell.2020.02.052) · [PubMed 32142651](https://pubmed.ncbi.nlm.nih.gov/32142651/)
[^lindner-2020-cardiac-involvement]: Lindner D, Fitzek A, Brauninger H, et al. Association of cardiac infection with SARS-CoV-2 in confirmed COVID-19 autopsy cases. *JAMA Cardiol.* 2020;5(11):1281-5. [doi:10.1001/jamacardio.2020.3551](https://doi.org/10.1001/jamacardio.2020.3551) · [PubMed 32730555](https://pubmed.ncbi.nlm.nih.gov/32730555/)
[^giustino-2020-cardiac-complications]: Giustino G, Croft LB, Stefanini GG, et al. Characterization of myocardial injury in patients with COVID-19. *J Am Coll Cardiol.* 2020;76(18):2043-55. [doi:10.1016/j.jacc.2020.08.069](https://doi.org/10.1016/j.jacc.2020.08.069) · [PubMed 33121713](https://pubmed.ncbi.nlm.nih.gov/33121713/)
[^eiros-2020-myocarditis-cmr]: Eiros R, Barreiro-Perez M, Martin-Garcia A, et al. Pericarditis and myocarditis long after SARS-CoV-2 infection. *medRxiv.* 2020. [doi:10.1101/2020.07.12.20151316](https://doi.org/10.1101/2020.07.12.20151316)

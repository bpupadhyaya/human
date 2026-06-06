---
schema: medicine-entry/v1
id: cancer-chemotherapy
name: Cancer Chemotherapy
atlas: 03-medicine
scale: 01-modern
status: draft
last_reviewed: 2026-06-06
summary: "Cytotoxic agents targeting rapidly dividing cells via alkylation, intercalation, antimetabolism, topoisomerase inhibition, or microtubule disruption. Introduced 1940s (nitrogen mustards). Cornerstone of curative regimens for leukemia, lymphoma, and solid tumors."
aliases: ["chemotherapy", "cytotoxic chemotherapy", "antineoplastic agents", "combination chemotherapy", "systemic chemotherapy"]
drug_class: cytotoxic antineoplastic
modality: small molecule
sources:
  - id: devita-1970-mopp
    type: peer-reviewed
    cite: "DeVita VT Jr, Serpick AA, Carbone PP. Combination chemotherapy in the treatment of advanced Hodgkin's disease. Ann Intern Med. 1970;73(6):881-95."
    doi: "10.7326/0003-4819-73-6-881"
    pmid: "5525541"
    url: "https://doi.org/10.7326/0003-4819-73-6-881"
  - id: frei-1958-methotrexate
    type: peer-reviewed
    cite: "Frei E III, Holland JF, Schneiderman MA, et al. A comparative study of two regimens of combination chemotherapy in acute leukemia. Blood. 1958;13(12):1126-48."
    pmid: "13596023"
    url: "https://pubmed.ncbi.nlm.nih.gov/13596023/"
  - id: skipper-1964-log-kill
    type: peer-reviewed
    cite: "Skipper HE, Schabel FM Jr, Wilcox WS. Experimental evaluation of potential anticancer agents. XIII. On the criteria and kinetics associated with 'curability' of experimental leukemia. Cancer Chemother Rep. 1964;35:1-111."
    pmid: "14117841"
    url: "https://pubmed.ncbi.nlm.nih.gov/14117841/"
cross_links:
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: modulates
    evidence: devita-1970-mopp
    note: "Cytotoxic chemotherapy causes lymphodepletion including CD8+ T cells, creating a period of immunosuppression; lymphodepletion is also exploited therapeutically before CAR-T infusion to enhance adoptive cell therapy engraftment."
  - target: 01-human/04-cellular/b-cell
    relation: modulates
    evidence: devita-1970-mopp
    note: "Alkylating agents and antimetabolites deplete B cells; rituximab-containing chemotherapy regimens (R-CHOP) target CD20+ B cells directly, causing prolonged hypogammaglobulinaemia requiring IVIG replacement in some patients."
  - target: 01-human/04-cellular/macrophage
    relation: modulates
    note: "Cyclophosphamide at metronomic doses reprograms tumour-associated macrophages from M2-like immunosuppressive to M1-like immunostimulatory phenotype, complementing anti-tumour immunity."
  - target: 01-human/07-system/immune-system
    relation: modulates
    evidence: devita-1970-mopp
    note: "Myelosuppression from chemotherapy (neutropenia, lymphopenia, thrombocytopenia) is the primary dose-limiting toxicity; G-CSF (filgrastim) counteracts neutropenia; opportunistic infections are major chemotherapy complications."
---

# Cancer Chemotherapy

## Overview

Cancer chemotherapy encompasses **cytotoxic pharmacological agents** that kill or arrest the growth of rapidly dividing cancer cells by interfering with DNA synthesis, DNA integrity, cell division machinery, or essential metabolic pathways. The field was inaugurated in the 1940s when Louis Goodman and Alfred Gilman at Yale demonstrated that nitrogen mustard (mechlorethamine) — a derivative of mustard gas weapons — produced lymphoma regression in a patient, translating chemical warfare knowledge into therapeutic application [^skipper-1964-log-kill].

The modern era of chemotherapy was defined by Vincent DeVita Jr. and colleagues at the National Cancer Institute, who demonstrated in 1970 that **combination chemotherapy** (MOPP regimen: mechlorethamine, vincristine/Oncovin, procarbazine, prednisone) could achieve **complete remissions and cures** in advanced Hodgkin lymphoma [^devita-1970-mopp] — establishing the principle that combinations of drugs with non-overlapping mechanisms could overcome resistance and achieve curative outcomes. This paradigm extended to ALL (acute lymphoblastic leukemia), Burkitt lymphoma, and later solid tumors.

Chemotherapy remains foundational in oncology — used as **curative intent** (e.g., hematologic malignancies), **neoadjuvant** (pre-surgical tumor shrinkage), **adjuvant** (post-surgical micrometastasis elimination), **palliative** (symptom control and life extension in advanced disease), and as **sensitizer** (combined with radiotherapy or targeted agents).

## Mechanism

### Classes of Chemotherapy Agents

| Class | Mechanism | Representative Agents | Cell Cycle Phase |
|:---|:---|:---|:---|
| **Alkylating agents** | Form covalent crosslinks within DNA (intrastrand and interstrand); prevent DNA replication/transcription | Cyclophosphamide, ifosfamide, cisplatin, carboplatin, oxaliplatin, melphalan, busulfan, temozolomide | Phase-nonspecific |
| **Antimetabolites** | Structural analogues of nucleosides/folate; inhibit DNA synthesis enzymes (DHFR, thymidylate synthase) or incorporate into DNA/RNA as fraudulent bases | Methotrexate, 5-fluorouracil (5-FU), gemcitabine, cytarabine (Ara-C), 6-mercaptopurine, pemetrexed | S-phase specific |
| **Topoisomerase inhibitors** | Inhibit TOP1 (camptothecins) or TOP2 (anthracyclines, etoposide) → prevent DNA religation → double-strand breaks → apoptosis | Irinotecan, topotecan (TOP1i); doxorubicin, etoposide, mitoxantrone (TOP2i) | S/G2 phase |
| **Anthracyclines** (sub-class of TOP2i) | DNA intercalation + TOP2 inhibition + free radical generation via redox cycling; also membrane effects | Doxorubicin, epirubicin, daunorubicin, idarubicin | S-phase |
| **Microtubule disruptors** | Taxanes: stabilise microtubules (prevent depolymerisation → mitotic arrest). Vinca alkaloids: inhibit tubulin polymerisation (prevent spindle formation) | Paclitaxel, docetaxel, cabazitaxel (taxanes); vincristine, vinblastine, vinorelbine (vinca alkaloids) | M-phase specific |
| **Platinum analogues** | Bifunctional alkylation; crosslink adjacent guanines → intra/interstrand adducts; cisplatin also triggers apoptosis via p53 | Cisplatin, carboplatin, oxaliplatin | Phase-nonspecific |
| **Miscellaneous** | Hydroxyurea (ribonucleotide reductase inhibitor); bleomycin (DNA strand breaks via free radicals); dacarbazine (alkylation) | — | Various |

### Pharmacological Principles

**Log-kill hypothesis (Skipper model):** A given dose of chemotherapy kills a **fixed fraction** (not a fixed number) of tumour cells — the log-kill principle. Thus, each cycle reduces tumour burden by the same proportion (e.g., 2-log kill = 99% cell kill per cycle). Mathematical models predict that complete eradication requires multiple treatment cycles even after clinical remission, establishing the rationale for **maintenance chemotherapy** and **post-remission consolidation** in hematologic malignancies [^skipper-1964-log-kill].

**Cell cycle phase specificity:** Antimetabolites and vinca alkaloids are phase-specific (maximally toxic only in a particular cell cycle phase), requiring prolonged exposure or scheduling relative to tumour growth fraction. Alkylating agents are phase-nonspecific (toxic to cycling and resting cells, though less so to resting cells).

**Combination rationale:** Combining agents with:
1. Non-overlapping mechanisms (additive/synergistic kill, different resistance mechanisms)
2. Non-overlapping toxicities (allowing dose-intensity without fatal additive organ toxicity)
3. Different cell cycle phase specificities (maximises total tumour cell kill)

## Clinical Use

### Major Curative Regimens

| Regimen | Components | Tumour Type | Cure Rate |
|:---|:---|:---|:---|
| **MOPP/ABVD** | Doxorubicin, bleomycin, vinblastine, dacarbazine | Hodgkin lymphoma | >85% advanced stage |
| **R-CHOP** | Rituximab + cyclophosphamide, doxorubicin, vincristine, prednisone | Diffuse large B-cell lymphoma | ~60–70% |
| **BEP** | Bleomycin, etoposide, cisplatin | Testicular germ cell tumour | >95% metastatic disease |
| **Hyper-CVAD** | Cyclophosphamide, vincristine, doxorubicin, dexamethasone alternating with MTX/Ara-C | ALL (adults) | ~40–50% OS adults |
| **FOLFOX/FOLFIRI** | 5-FU/leucovorin + oxaliplatin or irinotecan | Colorectal cancer | 50–70% (adjuvant setting) |
| **AC-T** | Doxorubicin + cyclophosphamide → paclitaxel | Breast cancer | Significant OS benefit in high-risk |

### Adverse Effects

| Toxicity | Responsible Agents | Management |
|:---|:---|:---|
| **Myelosuppression (neutropenia, anaemia, thrombocytopenia)** | Alkylators, anthracyclines, platinum, antimetabolites | G-CSF (filgrastim/pegfilgrastim); dose delays; blood product support |
| **Nausea and vomiting** | Cisplatin (highly emetogenic), doxorubicin, cyclophosphamide | 5-HT3 antagonists (ondansetron) + NK1 antagonists (aprepitant) + dexamethasone |
| **Alopecia** | Anthracyclines, cyclophosphamide, taxanes | Scalp cooling devices; reversible after therapy |
| **Cardiotoxicity (cardiomyopathy)** | Doxorubicin (cumulative dose-dependent; 550 mg/m² lifetime limit) | Limit cumulative dose; dexrazoxane prophylaxis; baseline/monitoring echocardiography |
| **Peripheral neuropathy** | Platinum (oxaliplatin), taxanes, vincristine | Dose reduction; duloxetine (modest benefit) |
| **Nephrotoxicity** | Cisplatin (proximal tubular toxicity) | Pre-hydration; amifostine; dose reduction in renal impairment |
| **Pulmonary fibrosis** | Bleomycin (dose-dependent, O2-exacerbated) | Limit cumulative dose; avoid >30% FiO2 during anaesthesia |
| **Secondary malignancy** | Alkylating agents → therapy-related AML (t-AML); topoisomerase 2 inhibitors → t-AML with 11q23 rearrangement | Long-term surveillance; risk-benefit assessment |
| **Haemorrhagic cystitis** | Cyclophosphamide, ifosfamide (acrolein metabolite) | Mesna (thiol scavenger); adequate hydration |

## Evidence

### MOPP and the Proof of Curability (DeVita 1970)

The landmark DeVita et al. trial [^devita-1970-mopp] treated 43 patients with advanced Hodgkin disease (stages III–IV) with combination MOPP chemotherapy:

- **Complete remission rate: 81%** — unprecedented in a uniformly fatal disease at that time
- **Long-term follow-up:** Approximately 50–60% of complete responders achieved durable remission (cure), definitively establishing that advanced cancer could be cured with chemotherapy
- This trial redefined oncology: previously considered merely palliative, chemotherapy was reconceived as potentially curative, leading to aggressive combination strategies across malignancy types

### Frei et al. — Combination vs. Sequential Therapy in ALL

Frei and colleagues at the NCI demonstrated in the 1950s–1960s that **combination chemotherapy** was far superior to sequential single-agent therapy in childhood ALL [^frei-1958-methotrexate]:
- Combination methotrexate + 6-MP achieved higher remission rates with reduced resistance development
- Established the four-drug induction regimen (vincristine, prednisone, L-asparaginase, anthracycline) that, refined over decades, brings childhood ALL cure rates to >90% today

### Modern RCT Evidence

Multiple large RCTs have established chemotherapy's curative and survival-extending role:
- **FOLFOX in adjuvant colon cancer** (MOSAIC trial): 6% absolute improvement in 6-year DFS with oxaliplatin addition
- **Docetaxel in early breast cancer** (BCIRG 001): TAC vs. FAC; 5-year DFS benefit 28% vs. 24%
- **Cisplatin/etoposide in SCLC**: ~80% objective response; ~20% long-term survivors (limited-stage)

## Connections

- **Modulates** → [Cytotoxic T Cell](../../../../01-human/04-cellular/t-cytotoxic-cell/README.md): Chemotherapy causes lymphodepletion including CD8+ T cells; lymphodepletion protocols are also exploited therapeutically before CAR-T infusion to create cytokine space and enhance adoptive cell therapy.
- **Modulates** → [B Cell](../../../../01-human/04-cellular/b-cell/README.md): Alkylating agents and antimetabolites deplete B cells; rituximab-containing regimens target CD20+ B cells, causing prolonged hypogammaglobulinaemia in some patients.
- **Modulates** → [Macrophage](../../../../01-human/04-cellular/macrophage/README.md): Metronomic cyclophosphamide reprograms tumour-associated macrophages from M2-like immunosuppressive to M1-like, complementing anti-tumour immune responses.
- **Modulates** → [Immune System](../../../../01-human/07-system/immune-system/README.md): Myelosuppression (dose-limiting toxicity) broadly suppresses innate and adaptive immunity; G-CSF and prophylactic antibiotics mitigate infection risk; paradoxically, lymphodepleting chemotherapy can enhance adoptive immunotherapy.

[^devita-1970-mopp]: DeVita VT Jr, Serpick AA, Carbone PP. Combination chemotherapy in the treatment of advanced Hodgkin's disease. *Ann Intern Med.* 1970;73(6):881-95. [doi:10.7326/0003-4819-73-6-881](https://doi.org/10.7326/0003-4819-73-6-881) · [PubMed 5525541](https://pubmed.ncbi.nlm.nih.gov/5525541/)
[^frei-1958-methotrexate]: Frei E III, Holland JF, Schneiderman MA, et al. A comparative study of two regimens of combination chemotherapy in acute leukemia. *Blood.* 1958;13(12):1126-48. [PubMed 13596023](https://pubmed.ncbi.nlm.nih.gov/13596023/)
[^skipper-1964-log-kill]: Skipper HE, Schabel FM Jr, Wilcox WS. Experimental evaluation of potential anticancer agents. XIII. On the criteria and kinetics associated with 'curability' of experimental leukemia. *Cancer Chemother Rep.* 1964;35:1-111. [PubMed 14117841](https://pubmed.ncbi.nlm.nih.gov/14117841/)

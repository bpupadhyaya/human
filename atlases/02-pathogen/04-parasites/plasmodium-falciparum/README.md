---
schema: pathogen-entry/v1
id: plasmodium-falciparum
name: Plasmodium falciparum
atlas: 02-pathogen
scale: 04-parasites
status: draft
last_reviewed: 2026-06-04
summary: "Apicomplexan protozoan; severe/cerebral malaria. Liver schizogony (5–7 d) → 48 h RBC cycles → gametocytes. 249M cases/yr; 608,000 deaths (WHO 2022). PfEMP1 cytoadherence causes cerebral malaria. Treated with ACT; no fully protective vaccine."
aliases: ["Pf", "P. falciparum", "malaria", "Plasmodium falciparum", "falciparum malaria"]
sources:
  - id: who-malaria-2023
    type: clinical-guideline
    cite: "World Health Organization. World Malaria Report 2023. WHO; 2023."
    url: "https://www.who.int/publications/i/item/9789240086173"
    accessed: "2026-06-04"
  - id: miller-2002-pf-biology
    type: peer-reviewed
    cite: "Miller LH, Baruch DI, Marsh K, Doumbo OK. The pathogenic basis of malaria. Nature. 2002;415(6872):673-9."
    doi: "10.1038/415673a"
    pmid: "11832955"
    url: "https://doi.org/10.1038/415673a"
  - id: cowman-2016-pf-review
    type: peer-reviewed
    cite: "Cowman AF, Healer J, Marapana D, Marsh K. Malaria: Biology and Disease. Cell. 2016;167(3):610-624."
    doi: "10.1016/j.cell.2016.07.055"
    pmid: "27768886"
    url: "https://doi.org/10.1016/j.cell.2016.07.055"
  - id: ashley-2018-artemisinin
    type: peer-reviewed
    cite: "Ashley EA, White NJ. The duration of Plasmodium falciparum infections. Malar J. 2014;13:500."
    doi: "10.1186/1475-2875-13-500"
    pmid: "25519842"
    url: "https://doi.org/10.1186/1475-2875-13-500"
cross_links:
  - target: 01-human/04-cellular/hepatocyte
    relation: infects
    evidence: cowman-2016-pf-review
    note: "Sporozoites injected by *Anopheles* mosquito travel to liver via bloodstream; invade hepatocytes via CD81/SR-B1 receptors and migrate through Kupffer cells; complete hepatic schizogony (5–7 days) producing 10,000–30,000 merozoites per infected hepatocyte, with no clinical symptoms during this phase."
  - target: 01-human/07-system/immune-system
    relation: damages
    evidence: miller-2002-pf-biology
    note: "P. falciparum evades adaptive immunity by extensive antigenic variation (PfEMP1/var gene family — ~60 var genes per parasite; expression switching); GPI anchors on parasite surface activate TLR2/TLR4 (systemic inflammation); rosetting (P. falciparum-infected RBCs binding uninfected RBCs) prevents complement-mediated clearance; splenomegaly and repeated episodes cause progressive immune exhaustion."
---

# Plasmodium falciparum

## Overview

***Plasmodium falciparum*** is the most lethal of the five *Plasmodium* species that infect humans, responsible for virtually all severe malaria, cerebral malaria, and malaria deaths. Malaria is one of humanity's oldest and most consequential infectious diseases: **249 million cases and 608,000 deaths in 2022**, concentrated in sub-Saharan Africa (94% of deaths) where children under 5 account for 76% of mortality [^who-malaria-2023].

*P. falciparum* is an **apicomplexan protozoan** — a eukaryotic intracellular parasite with a complex life cycle requiring both a **definitive host** (*Anopheles* mosquito, where sexual reproduction occurs) and a **human intermediate host** (asexual amplification in liver then blood). The parasite's biology is strikingly different from bacteria and viruses: it is a eukaryotic cell with its own organelles (nucleus, mitochondrion, apicoplast, ER), a genome of ~23 Mb across 14 chromosomes, and highly specialized invasion machinery.

The defining clinical features of *P. falciparum* — **cytoadherence, rosetting, and sequestration** — distinguish it from other malaria species and underlie the high mortality of cerebral and severe malaria [^miller-2002-pf-biology].

## Structure

**Parasite forms (major stages):**

| Stage | Location | Size | Duration |
|:---|:---|:---|:---|
| **Sporozoite** | Mosquito salivary gland → human blood | 10–15 µm elongated | Minutes in blood |
| **Hepatic merozoite** | Hepatocyte | 1–2 µm | Released after 5–7 days |
| **Ring stage** (early trophozoite) | Erythrocyte | 1–2 µm ring on RBC membrane | 0–24 h |
| **Trophozoite** | Erythrocyte | 3–10 µm | 24–36 h |
| **Schizont** | Erythrocyte | fills RBC | 36–48 h |
| **Merozoite** (blood) | Released into blood | 1–2 µm | Seconds-minutes |
| **Gametocyte** | Erythrocyte → mosquito | 8–12 µm crescent | Days–weeks |

**Key surface proteins:**
- **PfEMP1** (P. falciparum erythrocyte membrane protein 1): ~350 kDa; exported to RBC surface; binds ICAM-1, CD36, PECAM-1 on vascular endothelium (cytoadherence); encoded by ~60 *var* genes, only one expressed at a time (antigenic variation)
- **MSP1** (Merozoite Surface Protein 1): major invasion ligand; vaccine candidate
- **AMA1/RON2** complex: apical membrane antigen mediating tight junction formation during erythrocyte invasion
- **Apicoplast** (non-photosynthetic plastid): essential organelle for fatty acid, isoprenoid, and heme synthesis; target of antibiotics (doxycycline, clindamycin, azithromycin)

## Infection Mechanism

**Life cycle:**

**1. Hepatic phase (5–7 days, asymptomatic):**
- *Anopheles* female inoculates sporozoites during blood meal; sporozoites travel to liver via portal circulation within 30 minutes
- Sporozoites invade Kupffer cells (liver macrophages), traverse through them, then invade hepatocytes using **CD81** and **SR-B1** receptors
- Inside hepatocyte, parasite resides in a parasitophorous vacuole; undergoes **hepatic schizogony** — 10,000–30,000 merozoites produced per infected hepatocyte
- **Merosomes** (merozoite-filled vesicles) bud from infected hepatocytes and travel to lung capillaries, releasing merozoites into bloodstream

**2. Blood phase (48 h cycles, symptomatic):**
- Merozoites invade red blood cells via **MSP1, AMA1/RON2, EBA175** (binding glycophorin A), and multiple redundant invasion pathways
- Inside the RBC, parasite degrades hemoglobin (via hemoglobin-degrading proteases in the food vacuole), converting toxic heme to crystalline **hemozoin** (malaria pigment)
- 48-hour intra-erythrocytic development: ring → trophozoite → schizont → 16–32 new merozoites → RBC rupture → synchronous merozoite release → fever spike
- Some parasites commit to **gametocytogenesis** (sexual stage, 7–15 days); crescent-shaped gametocytes in peripheral blood are taken up by *Anopheles*

**3. Mosquito phase:**
- Gametocytes mature into gametes in midgut; fertilization → ookinete → oocyst → sporozoites → salivary gland (ready for next transmission)

**Cytoadherence and sequestration:**
After 12–16 hours of intra-erythrocytic development, infected RBCs (iRBCs) express **PfEMP1** on their surface, mediating binding to endothelial ICAM-1, CD36, and other receptors. Sequestration in microvasculature (brain, heart, placenta) prevents spleen-mediated clearance — but causes microvascular obstruction in cerebral malaria.

## Host Interactions

**Clinical spectrum:**
- **Uncomplicated malaria:** Cyclical fever spikes every 48 h (tertian pattern), rigors, headache, myalgia, nausea; caused by synchronous schizont rupture and release of GPI toxins, TNF-α, IL-6
- **Severe malaria (WHO criteria):** Cerebral malaria, severe anemia (Hb <7 g/dL), acute kidney injury, respiratory distress (metabolic acidosis), hypoglycemia, shock
- **Cerebral malaria:** Parasitized RBC sequestration in brain microvessels → mechanical obstruction + endothelial activation + blood-brain barrier disruption; coma, seizures, intracranial hypertension; 15–20% case fatality even with treatment

**Immune evasion:**
- Extensive **antigenic variation** via *var* gene switching (one gene expressed at a time; ~60 genes per parasite genome) — immune pressure selects for switch events
- **Intracellular habitat** protects from antibody during most of the blood-stage cycle
- Complement evasion: KAHRP (knob-associated histidine-rich protein) remodels RBC cytoskeleton; PfEMP1 binding to CRIg protects iRBCs from phagocytosis

## Connections

- **Infects** → [Hepatocyte](../../../01-human/04-cellular/hepatocyte/README.md): Sporozoites invade hepatocytes in the clinically silent hepatic phase, undergoing massive asexual amplification (up to 30,000 merozoites per cell) before releasing into the bloodstream.
- **Damages** → [Immune System](../../../01-human/07-system/immune-system/README.md): PfEMP1 antigenic variation prevents sustained adaptive immunity; GPI-mediated TLR activation drives systemic inflammation; repeated infections cause progressive immune exhaustion and splenomegaly.

## Pathology

**Severe anemia:** RBC destruction (direct lysis at schizont rupture + bystander uninfected RBC hemolysis) + dyserythropoiesis (bone marrow suppression) → anemia; in high-transmission areas, up to 25% of children are chronically anemic.

**Placental malaria:** PfEMP1 variants (VAR2CSA) bind chondroitin sulfate A on placental syncytiotrophoblasts → sequestration in placental intervillous space; causes maternal anemia, fetal growth restriction, low birth weight, preterm delivery — leading cause of maternal/infant morbidity in endemic Africa.

**Blackwater fever:** Rare; massive intravascular hemolysis (cause unclear; associated with quinine/primaquine use and G6PD deficiency) → hemoglobinuria (black urine) → acute kidney injury.

**Treatment:** Artemisinin-based combination therapy (ACT) — artesunate + amodiaquine/lumefantrine/mefloquine. IV artesunate for severe malaria. Partial artemisinin resistance emerging in Southeast Asia (*kelch13* mutations) and spreading to Africa — current major threat.

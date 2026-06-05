<div align="center">

# Human Engineering

### A unified, open model of human biology — from subatomic particles to the whole body.

So we can design vaccines, therapies, and adaptive immunity at the speed of mutation.
Built in the open. By anyone. For all of humanity. Free, forever.

**[Visit the site](https://equalinformation.com/human/)** · **[Browse the Atlases](atlases/README.md)** · **[Join the effort](#join-the-effort)** · **[Support the work](#support-the-work)**

[![License: MIT](https://img.shields.io/badge/License-MIT-00d9a3.svg?style=for-the-badge)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-3aa9ff.svg?style=for-the-badge)](#join-the-effort)
[![For Humanity](https://img.shields.io/badge/Built%20for-Humanity-ffb86b.svg?style=for-the-badge)](#)
[![Open Source](https://img.shields.io/badge/Open-Source-c084fc.svg?style=for-the-badge)](https://github.com/bpupadhyaya/human)

</div>

---

> *"When the next fast-mutating pathogen appears, a candidate vaccine should be hours away — not months or years."*

---

## The Mission

**Human Engineering** is an open, free, global initiative to build three coherent, open knowledge bases — of **human biology**, of the **pathogens that interact with it**, and of **every medicine humanity has used to heal** — across every scale of organization, from the subatomic to the whole-body.

We aim to make those models precise enough that we can do three things with the same rigor we apply to silicon and software:

1. **Engineer** — design new biology from first principles.
2. **Reverse-engineer** — recover the mechanism of any disease, pathogen, or healthy process end-to-end.
3. **Re-engineer** — repair, optimize, or replace components of human biology with confidence.

The end goal is two-fold: collapse the time between *pathogen detected* and *vaccine shipped* from years to hours — and eventually, design **adaptive immune layers** that generalize to threats we have not yet seen.

This project belongs to everyone. It will always be free.

---

## The Vision

The work organizes into **Four open, interlocking Atlases** — the body, the threats, the cures, and the vaccines — each held to the same standard of scientific rigor.

📚 **[Browse all atlases →](atlases/README.md)**

### Atlas One — The Human Atlas

Multi-scale model of host biology, from subatomic particles to the whole body. Eight levels of organization, each constraining and explaining the next.

**Read the full atlas → [`atlases/01-human/`](atlases/01-human/README.md)**

### Atlas Two — The Pathogen Atlas

Every microbe and pathogen that touches human biology — viruses, bacteria, fungi, parasites, prions, and the commensal microbiome. Modeled across structure, mechanism of harm, immune signature, and mutation pressure.

**Read the full atlas → [`atlases/02-pathogen/`](atlases/02-pathogen/README.md)**

### Atlas Three — The Medicine Atlas

An encyclopedia of every medicine humanity has used to heal — modern pharmaceuticals, traditional medicine systems thousands of years old, and the foods and spices we already cook with.

**Read the full atlas → [`atlases/03-medicine/`](atlases/03-medicine/README.md)** · **[Live page](https://equalinformation.com/human/medicine.html)**

### Atlas Four — The Vaccine Atlas

Every vaccine humanity has built, organized by delivery platform: mRNA, viral vector, recombinant subunit, inactivated whole-virion, and live-attenuated. Each entry covers antigen design, mechanism of immunity, clinical efficacy, safety profile, and connections to the Human and Pathogen atlases.

**Read the full atlas → [`atlases/04-vaccine/`](atlases/04-vaccine/README.md)**

> **The four atlases form an interconnected knowledge graph**: the Human Atlas supplies the biological targets, the Pathogen Atlas supplies the threats, the Medicine Atlas supplies the interventions, and the Vaccine Atlas supplies the prophylactic designs that collapse the gap between *pathogen detected* and *population protected*. Together they are an open **training corpus for AI agents** working on the next vaccine — and an open **educational foundation** for human researchers, clinicians, and students worldwide.

### Four Capabilities

Across all three atlases, four capabilities become tractable.

| Capability | What it unlocks |
|:---|:---|
| **Engineer** | Design new proteins, cells, tissues, and immune responses from first principles, with predictable behavior. |
| **Reverse-engineer** | Take a pathogen, disease, or healthy mechanism and recover its mechanism end-to-end. |
| **Re-engineer** | Repair, optimize, or replace components of human biology with the confidence of a hardware swap. |
| **Immunize** | Design adaptive defenses that generalize across fast-mutating threats — not chase each variant in retrospect. |

---

## Why Now

For most of history, a project this ambitious would have been science fiction. In the last decade, three independent fields each crossed a threshold — and they did it at roughly the same time.

- **The cost of slowness is now legible.** COVID-19 measured the gap between *pathogen* and *vaccine* in millions of lives. Next time, that gap should be hours.
- **Compute and AI are ready.** Protein folding, molecular dynamics, multi-scale simulation, and foundation models for biology have all crossed feasibility thresholds.
- **Biology is increasingly engineerable.** CRISPR, mRNA platforms, synthetic biology, and high-throughput assays make biology behave more like a programmable system every year.

Three simultaneous thresholds. The unlock is not waiting for a discovery — it is waiting for an *organization* of effort. That is what this project is.

---

## Principles

These are non-negotiable. They define what makes this project *Human Engineering* rather than just another research program.

- **Open** — every model, every dataset, every method, in public.
- **Free** — no paywalls, no licensing fees, no gatekeeping. Forever.
- **Global** — anyone from any country, any discipline, any career stage is welcome.
- **For humanity** — not for shareholders, not for nation-states, not for any single institution.
- **Rigorous** — humanitarian intent does not lower the bar for scientific quality. It raises it.
- **Transparent** — finances, governance, decisions, and roadmap visible to all.

---

## Project Status

> **Phase: Founding.** This repository currently hosts the project's public-facing site and mission statement. Technical infrastructure, model architecture, contributor governance, and funding channels are being designed in the open. Watch this repo, join the discussions, and shape the foundation.

---

## Repository Structure

The repo is organized **by kind of artifact**, not by topic. Every new atlas, project, agent, or dataset slots into the existing folders without restructuring.

```
human/
├── README.md                       # Project front door (you are here)
├── LICENSE                         # MIT
│
│  ─────────── CONTENT (what we know) ───────────
├── atlases/                        # KNOWLEDGE — markdown source of truth
│   ├── README.md                   # Atlases index (4 current + 5 planned)
│   ├── 01-human/                   # Atlas One — host biology
│   ├── 02-pathogen/                # Atlas Two — pathogens & microbes
│   ├── 03-medicine/                # Atlas Three — medicines
│   └── 04-vaccine/                 # Atlas Four — vaccines by platform
│
├── media/                          # IMAGES, VIDEOS, DIAGRAMS — referenced by atlases & docs
├── data/                           # DATASETS — small inline + pointers to external
│
│  ─────────── PRESENTATION (how it's shown) ───────────
├── docs/                           # PUBLIC WEBSITE — served via GitHub Pages
│   ├── index.html                  # Mission landing — equalinformation.com/human/
│   └── medicine.html               # Medicine Atlas page — /human/medicine.html
│
│  ─────────── MACHINERY (what makes it tick) ───────────
├── comp-prog-proj/                 # CODE — computational programming projects
│                                   # (each project may contain its own AI agents)
├── notebooks/                      # RESEARCH — Jupyter / marimo / Quarto, exploratory
├── schemas/                        # SPECS — data contracts, entry templates
└── tools/                          # INTERNAL — build scripts, dev utilities, CI
```

### The three layers

| Layer | Folders | Question it answers |
|:---|:---|:---|
| **Content** | `atlases/` `media/` `data/` | *What do we know?* |
| **Presentation** | `docs/` | *How does the world see it?* |
| **Machinery** | `comp-prog-proj/` `notebooks/` `schemas/` `tools/` | *What makes it run?* |

### Key conventions

- **Every folder has a `README.md`** — if it doesn't, it's broken. Read the README to learn the conventions inside each folder.
- **Naming is `kebab-case-noun/`** everywhere. Atlas folders use the `NN-name/` numbered pattern.
- **AI agents live inside `comp-prog-proj/<project>/agents/`**, never at the repo root. Shared agents become their own project.
- **Large binaries (>10 MB) use git-lfs** so the repo stays clonable.
- **Schemas are contracts** — when two artifacts must agree on a format, the format lives in `schemas/`.
- **Source of truth for knowledge stays in `atlases/`** — code, data, and notebooks reference back to atlas entries, not the other way around.

More atlases will appear as the project grows (Pathology, Clinical, Public Health, Imaging, Genetics — see the [atlases index](atlases/README.md) for the planned set). More projects, datasets, schemas, and notebooks will appear in their respective folders without changing the top-level layout.

---

## Join the Effort

> **Anyone. Anywhere. Any contribution.**

This is a project *for* humanity, *by* humanity. No matter your discipline, your country, or your stage of career — there is a way to contribute. The model needs every kind of mind.

### Roles welcome

<table>
<tr>
<td valign="top">

**Life Sciences**
- Biologists
- Chemists
- Physicists
- Clinicians
- Pharmacologists
- Virologists
- Microbiologists
- Immunologists
- Epidemiologists

</td>
<td valign="top">

**Technology**
- AI / ML researchers
- Software engineers
- Data engineers
- Systems architects
- Designers

</td>
<td valign="top">

**Communication & Society**
- Writers & educators
- Translators
- Ethicists & policy
- Citizen scientists
- Community organizers

</td>
</tr>
</table>

### How to contribute

1. **Star this repo** to follow the project and signal support.
2. **Open a [Discussion](https://github.com/bpupadhyaya/human/discussions)** — introduce yourself, propose an idea, ask a question, or share a relevant paper.
3. **Open an [Issue](https://github.com/bpupadhyaya/human/issues)** for concrete proposals or feedback on direction.
4. **Submit a Pull Request** if you would like to improve the site, documentation, or any future code.
5. **Get in touch directly** at **[bpupadhyaya@gmail.com](mailto:bpupadhyaya@gmail.com?subject=Human%20Engineering%20%E2%80%94%20I'd%20like%20to%20contribute)** — especially if you are interested in shaping the founding team, technical architecture, or governance.

There is no minimum contribution. A thoughtful comment, a translated paragraph, a corrected typo, a borrowed afternoon — all of it counts.

---

## Support the Work

The model, the data, and the tools will always be **free**. Donations pay for the compute, the researchers, and the infrastructure that keeps it that way.

> **Funding channels are opening soon** — transparent, accountable, with public ledgers and open finances. In the meantime, we are accepting **early supporters** directly.

- **Become an early supporter** — **[bpupadhyaya@gmail.com](mailto:bpupadhyaya@gmail.com?subject=Human%20Engineering%20%E2%80%94%20I'd%20like%20to%20support)**
- **Star the repository** — visibility is its own form of support
- **Share the mission** — every person reached is a potential contributor

---

## Code of Conduct

We are committed to a project environment that is welcoming, respectful, and free of harassment — for contributors of every background, country, identity, and discipline. A formal Code of Conduct (based on the Contributor Covenant) will be adopted as the community grows. Until then: act with the seriousness this work deserves, and the generosity humanity deserves.

---

## License

Released under the **[MIT License](LICENSE)**. Use it, fork it, build on it, ship it — with or without us. Just keep the spirit: open, free, for humanity.

---

## Contact

**Bhim Upadhyaya** — Founder
[bpupadhyaya@gmail.com](mailto:bpupadhyaya@gmail.com) · [github.com/bpupadhyaya](https://github.com/bpupadhyaya) · [bpupadhyaya.github.io](https://bpupadhyaya.github.io)

---

<div align="center">

### Humanity at its best.

*An open, free, global model of human biology — built in service of every person on Earth.*

**[equalinformation.com/human](https://equalinformation.com/human/)**

</div>

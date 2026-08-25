---
title: "Semantically-Informed Predictive Control for Autonomous UAV Connectivity in Urban Environments"
date: 2026-08-24
publishDate: 2026-08-24
authors: ['Vlachos, E.', 'Tsourounis, D.', 'Kaushik, A.']
publication_types: ["1"]
abstract: "Millimeter-wave (mmWave) frequencies enable high-throughput unmanned aerial vehicle (UAV) networks, but their directional links are sensitive to obstacle material composition. Conventional UAV path planners fail in environments with diverse materials. Geometric planners treat obstacles as opaque, while signal-strength planners chase high-SNR zones without distinguishing stable line-of-sight from fragile multipath. This work sits in the sensing-aided branch of integrated sensing and communication (ISAC), where radar and link share the same band, so the radar serves the link rather than a separate detection task. We fuse radar sensing with visual semantic classification to construct an effective capacity metric that decouples signal strength from material-dependent reliability. A two-stage planner generates paths that avoid both hard blockers and unreliable multipath, then optimizes the trajectory to maximize effective throughput. Hardware characterization confirms that radar alone cannot distinguish spectrally distinct materials. Simulations show that the proposed planner substantially improves effective throughput and link reliability over signal-strength baselines, closely approaching an oracle with perfect channel knowledge."
submitted: true
featured: false
publication: "*NextGCom 2026 — Special Session: Integrated Sensing and AI-Driven Communication in 6G Perceptive Mobile Networks*"
tags: ["Research", "UAVs", "6G", "mmWave", "ISAC", "Path Planning"]
---

## Key Contributions

- An **Effective Capacity** metric that extends the radio map paradigm by weighting raw throughput with a material-dependent reliability coefficient, decoupling signal strength from link stability and exposing permeable vegetation corridors that signal-strength planners overlook.
- A **two-layer planner** comprising (i) a Semantically-Informed RRT backbone augmented with material-dependent reliability and capacity acceptance checks that prune expansion through multipath zones, and (ii) a gradient-based trajectory optimizer that deforms the path by balancing signal-seeking and reliability-seeking forces derived from the product-rule decomposition of ∇C_eff.
- **Hardware validation** of the material ambiguity premise via characterization with a TI IWR6843AOP 60 GHz FMCW radar, confirming that radar alone cannot distinguish concrete from vegetation.

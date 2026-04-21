---
title: "Semantically-Informed Predictive Control for Autonomous UAV Connectivity in Urban Environments"
date: 2026-02-26
publishDate: 2026-02-26
authors: ['Vlachos, E.', 'Tsourounis, D.']
publication_types: ["3"]
abstract: "Millimeter-wave (mmWave) frequencies offer the multi-gigabit throughput required by next-generation UAV networks, but their directional propagation makes link quality sensitive to the material composition of nearby obstacles. Geometric planners treat all obstacles as binary blockers, while signal-strength planners chase high-SNR zones without distinguishing stable line-of-sight from fragile multipath. Both fail in urban environments where concrete, metal, glass, and vegetation coexist. We propose a control framework that fuses mmWave radar sensing with visual semantic classification to construct an effective capacity metric that decouples raw signal strength from material-dependent link reliability. A two-layer planner generates collision-free paths that avoid both hard blockers and unreliable multipath zones, then deforms the trajectory via gradient optimization to maximize reliable throughput. Hardware characterization with a 60 GHz sensor confirms that radar returns alone cannot distinguish spectrally distinct materials. Monte Carlo simulations show that the proposed controller improves effective throughput by 65% over signal-strength baselines while maintaining 0.96 link reliability, reaching 97.3% of an oracle with perfect global channel knowledge."
featured: true
publication: "*Under Development*"
tags: ["Research", "UAVs", "6G", "mmWave", "Path Planning"]
---

## Key Contributions

- An **Effective Capacity** metric that extends the radio map paradigm by weighting raw throughput with a material-dependent reliability coefficient, decoupling signal strength from link stability and exposing permeable vegetation corridors that signal-strength planners overlook.
- A **two-layer planner** comprising (i) a Semantically-Informed RRT backbone augmented with material-dependent reliability and capacity acceptance checks that prune expansion through multipath zones, and (ii) a gradient-based trajectory optimizer that deforms the path by balancing signal-seeking and reliability-seeking forces derived from the product-rule decomposition of ∇C_eff.
- **Hardware validation** of the material ambiguity premise via characterization with a TI IWR6843AOP 60 GHz FMCW radar, confirming that radar alone cannot distinguish concrete from vegetation.

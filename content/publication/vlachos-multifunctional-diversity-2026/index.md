---
title: "Multi-Functional Diversity via Flexible Spatial Partitioning for Massive MIMO ISAC"
date: 2026-03-05
publishDate: 2026-03-05
authors: ['Vlachos, E.', 'Kaushik, A.']
publication_types: ["2"]
abstract: "In massive MIMO Integrated Sensing and Communications (ISAC), conventional contiguous sub-array partitioning limits spatial degrees of freedom. This paper demonstrates that interleaved beam assignment unlocks multi-functional selection diversity, driven by distinct channel statistics. We analytically prove that while the gain from signal alignment inherently saturates, the gain from proactive spatial decoupling (leakage avoidance) scales logarithmically with the array size, dominating massive MIMO performance. To exploit this, we propose the Diversity-Aware Spatial Partitioning (DASP) algorithm, a covariance-based framework that eliminates instantaneous channel state information (CSI) overhead and solves the combinatorial beam assignment with log-linear per-update complexity. Furthermore, we derive an analytical signal-to-noise ratio (SNR) threshold demarcating where spatial partitioning outperforms orthogonal resource slicing (e.g., time-division multiplexing). Numerical results with up to 256 antennas confirm that flexible partitioning yields near-optimal sum-rates, strictly dominates contiguous approaches, and significantly outperforms resource slicing across standard mmWave link budgets, ceding superiority only under extreme SNR or highly overlapping scattering conditions."
draft: true
submitted: false
featured: false
publication: "*IEEE Transactions on Wireless Communications (under revision)*"
tags: ["Research", "ISAC", "Massive MIMO", "Hybrid Beamforming", "6G", "mmWave"]
---

## Key Contributions

- **Multi-functional selection diversity**: We prove that interleaved beam assignment between communication and radar unlocks a new diversity mechanism — spatial decoupling (leakage avoidance) — whose gain scales as **log(N)** with array size, while signal alignment saturates, making it the dominant gain at massive MIMO scales.
- **DASP algorithm**: A covariance-only framework that solves the combinatorial beam assignment problem with **O(N log N)** per-update complexity, eliminating instantaneous CSI overhead and operating directly in beamspace.
- **Analytical SNR threshold**: A closed-form condition demarcating when flexible spatial partitioning outperforms orthogonal resource slicing (TDM/FDM), showing that standard mmWave link budgets fall firmly in the partitioning-favorable regime.

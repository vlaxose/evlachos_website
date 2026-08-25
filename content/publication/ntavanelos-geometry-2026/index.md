---
title: "Geometry-Aware Regularization for Deep-Unfolded MIMO-OTFS Detection"
date: 2026-08-24
publishDate: 2026-08-24
authors: ['Ntavanelos, N.', 'Vlachos, E.']
publication_types: ["2"]
abstract: "We study symbol detection in Multiple-Input Multiple-Output Orthogonal Time Frequency Space (MIMO-OTFS) systems over geometry-based, time-varying multipath channels, where multipath propagation induces spatial and fractional Doppler–Delay (DD) coupling and leads to non-uniform scaling across symbol components. We analytically characterize this non-uniform diagonal structure of the MIMO-OTFS Gram matrix, showing that all diagonal variation arises exclusively from inter-path coupling. Motivated by this result, we adopt a deep-unfolded Conjugate Gradient (CG) framework and introduce a geometry-aware coordinate-wise regularizer directly into the underlying linear system, with weights learned in a data-driven manner. Simulation results under both low- and high-mobility scenarios show that, for moderately separated propagation paths, the proposed detector outperforms low-complexity baselines and approaches the performance of more complex neural architectures at medium and high Signal to Noise Ratio (SNR)."
featured: false
submitted: true
publication: "*NextGCom 2026 — Special Session: Integrated Sensing and AI-Driven Communication in 6G Perceptive Mobile Networks*"
tags: ["Research", "MIMO-OTFS", "Deep Unfolding", "Signal Detection", "6G"]
---

## Key Contributions

- **Gram matrix analysis**: Analytical characterization of the non-uniform diagonal structure of the MIMO-OTFS Gram matrix, proving that all diagonal variation arises exclusively from inter-path coupling.
- **Geometry-aware regularizer**: A coordinate-wise regularizer embedded into a deep-unfolded Conjugate Gradient detector, with per-component weights learned in a data-driven manner.
- **Performance gains**: The proposed detector outperforms low-complexity baselines and approaches heavier neural architectures at medium-to-high SNR, with improved robustness in high-mobility scenarios.

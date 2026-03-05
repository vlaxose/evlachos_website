---
title: "Paper Submitted to IEEE Transactions on Wireless Communications"
date: 2026-03-05
summary: "We submitted a paper on multi-functional diversity via flexible spatial partitioning for massive MIMO ISAC to IEEE TWC."
tags: ["publication", "research", "ISAC", "massive MIMO", "beamforming"]
pub_type: "paper"
categories: ["paper"]
---

We submitted a new paper to **IEEE Transactions on Wireless Communications**:

### Multi-Functional Diversity via Flexible Spatial Partitioning for Massive MIMO ISAC
*Evangelos Vlachos and Aryan Kaushik*

In massive MIMO ISAC systems, conventional contiguous sub-array partitioning limits spatial degrees of freedom. This work introduces **multi-functional selection diversity** — a new gain mechanism that arises from assigning spatial beams to communication and radar based on their long-term channel statistics.

Key contributions:

- **Scaling laws**: We prove that the dominant diversity component — spatial decoupling (leakage avoidance) — scales as **log(N)** with the array size, while signal alignment saturates.
- **DASP algorithm**: A covariance-only framework that solves the combinatorial beam assignment with **O(N log N)** complexity, eliminating the need for instantaneous CSI.
- **Regime analysis**: An analytical SNR threshold demarcating when spatial partitioning outperforms orthogonal resource slicing (e.g., TDM). Standard mmWave link budgets fall firmly in the partitioning-favorable regime.

Numerical results with up to 256 antennas confirm that flexible interleaved partitioning nearly doubles the spectral efficiency of resource slicing and strictly dominates contiguous sub-array approaches.

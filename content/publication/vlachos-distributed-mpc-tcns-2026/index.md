---
title: "Distributed MPC for Directional UAV Networks: Co-design of Motion and Hybrid Beam Alignment"
date: 2026-03-05
publishDate: 2026-03-05
authors: ['Vlachos, E.']
publication_types: ["2"]
abstract: "This paper addresses the coupled control and communication problem in UAV networks operating at millimeter-wave (mmWave) frequencies. While hybrid mechanical-electronic steering enables high-gain directional connectivity, the narrow Field of View (FoV) of phased arrays introduces a strong coupling between agent kinematics and link quality, rendering traditional velocity-aligned guidance strategies insufficient. We propose a Distributed Model Predictive Control (MPC) framework that jointly optimizes the translational trajectory and mechanical heading to maximize network capacity while ensuring safety. The key technical challenge lies in the non-convex, piecewise-smooth structure of the hybrid beamforming gain, which exhibits vanishing gradients outside the electronic FoV. We construct a smooth surrogate objective via a differentiable Gaussian envelope of the array factor and a log-barrier relaxation of the FoV boundary, establish a closed-form sufficiency condition for the linear convergence of the sequential best-response dynamics, and prove recursive feasibility of the distributed scheme under the warm-start initialization. Extensive numerical simulations demonstrate that the proposed joint formulation reduces link outage probability by approximately 96% compared to velocity-aligned heuristics, effectively bridging the gap between physical-layer constraints and autonomous guidance."
submitted: true
featured: true
publication: "*IEEE Transactions on Control of Network Systems*"
tags: ["Research", "UAVs", "MPC", "mmWave", "ISAC", "Distributed Control", "Beam Alignment"]
---

## Supplementary Video

{{< video src="demo.mp4" controls="yes" >}}

## Key Contributions

- **Joint Motion–Communication Framework**: A decentralized MPC that jointly optimizes trajectory and mechanical heading for hybrid mechanical-electronic beamforming, proactively maintaining neighbors within the electronic FoV.
- **Theoretical Guarantees**: A smooth Gaussian-envelope surrogate for the non-convex hybrid gain with a proven Lipschitz-continuous gradient; a closed-form spectral contraction condition linking tracking weight, communication coupling, and beamwidth into a single tunable inequality guaranteeing convergence. Recursive feasibility established via a DARE-based warm-start strategy.
- **Experimental Validation**: High-fidelity simulations showing ~96% reduction in link outage probability vs. velocity-aligned heuristics, with O(1) per-agent scaling up to K=16 agents.

*This work was supported by the European Union's Horizon Europe programme under Grant Agreement No. 101187121 (EUSOME).*

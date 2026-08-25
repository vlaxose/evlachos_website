---
title: "Safe Distributed MPC for Directional UAV Networks: One-Shot Co-Design of Motion and Two-Sided Beam Alignment"
date: 2026-03-05
publishDate: 2026-03-05
authors: ['Vlachos, E.']
publication_types: ["2"]
abstract: "This paper addresses the coupled control and communication problem in UAV networks operating at millimeter-wave (mmWave) frequencies with hybrid mechanical-electronic beam steering. Because each agent carries a single phased array, its mechanical heading must simultaneously serve the transmit and receive directions of distinct directional links: we show geometrically that when the angular spread of a neighborhood exceeds the electronic field of view, no heading policy can maintain connectivity, so the translational trajectory itself must reshape the link geometry. Motivated by this impossibility argument, we propose a distributed Model Predictive Control (MPC) framework that co-designs trajectory and heading under a two-sided beamforming gain model, with collision avoidance imposed as hard discrete-time control barrier function constraints rather than penalty terms. To handle the non-convex, piecewise-smooth hybrid gain, we construct a smooth surrogate with a proven Lipschitz-continuous gradient whose constant is explicit in the antenna parameters. The coordination protocol performs a single communication-and-solve round per control period, and we analyze exactly this implemented scheme: a proximal regularization yields a verifiable strong convexity condition, the best-response mapping is shown to contract under a closed-form physical-parameter inequality, and a tracking theorem bounds the distance of the warm-started one-shot iterate from the time-varying network equilibrium. Recursive feasibility is established under stated terminal and neighbor-compatibility assumptions, and feasibility of the barrier constraints renders the safe set forward invariant. Simulations with an IEEE 802.11ad physical layer show that the proposed co-design substantially reduces link outage relative to velocity-aligned, decoupled, and fixed-heading baselines, degrades gracefully under actuation disturbances, state noise, and packet loss, and sustains constant per-agent computation as the swarm grows."
featured: true
draft: true
publication: "*In preparation for IEEE Open Journal of Control Systems*"
tags: ["Research", "UAVs", "MPC", "mmWave", "ISAC", "Distributed Control", "Beam Alignment", "Control Barrier Functions"]
---

## Supplementary Video

{{< video src="demo.mp4" controls="yes" >}}

## Key Contributions

- **Impossibility-Driven Co-Design**: A geometric argument showing that mechanical heading alone cannot maintain a two-sided directional link once neighborhood angular spread exceeds the electronic FoV, motivating trajectory shaping as a first-class control objective rather than a byproduct of guidance.
- **Hard-Constraint Safety**: Collision avoidance is enforced via discrete-time control barrier function constraints rather than penalty terms, with recursive feasibility of the one-shot, single-round coordination protocol established under stated terminal and neighbor-compatibility assumptions.
- **Theoretical Guarantees**: A Lipschitz-continuous smooth surrogate for the non-convex two-sided beamforming gain; a closed-form contraction condition on the best-response mapping; a tracking theorem bounding the warm-started one-shot iterate from the time-varying network equilibrium.
- **Experimental Validation**: IEEE 802.11ad-based simulations showing substantially reduced link outage vs. velocity-aligned, decoupled, and fixed-heading baselines, with graceful degradation under actuation/state noise and packet loss, and constant per-agent computation as the swarm scales.

*This work was supported by the European Union's Horizon Europe programme under Grant Agreement No. 101187121 (EUSOME).*

---
title: "Hardware-Aware SE(3) Control Barrier Functions for Counter-UAS Interceptors with Directed Energy Payloads"
date: 2026-06-17
publishDate: 2026-06-17
authors: ['Vlachos, E.', 'Kolios, P.', 'Skliros, C.']
publication_types: ["1"]
abstract: "Drone-mounted directed energy payloads — RF jammers and High Power Microwave (HPM) sources — offer a reusable Counter-UAS capability, but their adoption on small interceptors is constrained by strict onboard power limits. Narrow, high-gain beams can close the engagement link budget with minimal transmit power, yet the tight Field of View (FoV) such beams demand conflicts with the aggressive attitude transients a multi-rotor must execute during pursuit. This paper resolves this conflict through a hardware-aware safety filter based on Control Barrier Functions (CBFs) on the SE(3) manifold. By providing formal pointing guarantees, the filter enables highly directional antennas whose gain would otherwise be sacrificed to tolerate pointing uncertainty. We formulate the electronic steering limits of a phased array as a relative-degree-two safety constraint with analytically verified Lie derivatives, and solve the resulting Quadratic Program via ADMM with a constant-time core factorization. Validation in a nonlinear SE(3) simulation and a PX4 Software-in-the-Loop (SITL) environment shows that the proposed CBF eliminates all FoV violations, recovers significant antenna gain through beam tightening, and reveals that conventional pitch clamping actively worsens pointing errors due to coupled rotational dynamics."
featured: false
publication: "*2026 International Conference on Unmanned Aircraft Systems (ICUAS)*"
tags: ["Research", "UAVs", "Control Barrier Functions", "Counter-UAS", "SE(3)", "ISAC"]
---

## Simulation Demo

The animation below compares two methods on the SE(3) CBF scenario: the **unfiltered** controller (red) and the proposed **ADMM-CBF** safety filter (blue), which maintains FoV pointing throughout the pursuit maneuver.

{{< video src="demo.mp4" controls="yes" >}}

## Key Contributions

- A **hardware-aware CBF safety filter** on the SE(3) manifold that provides formal FoV pointing guarantees for directed-energy payloads under aggressive pursuit dynamics.
- Formulation of phased-array electronic steering limits as a **relative-degree-two safety constraint** with analytically verified Lie derivatives.
- An **ADMM solver** with constant-time core factorization enabling real-time onboard execution.
- Validation in both a nonlinear SE(3) simulation and a **PX4 SITL** environment, demonstrating elimination of all FoV violations and recovery of antenna gain through beam tightening.

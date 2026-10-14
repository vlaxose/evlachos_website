---
title: "Hardware-Aware SE(3) Control Barrier Functions for Counter-UAS Interceptors with Directed Energy Payloads"
date: 2026-06-17
publishDate: 2026-06-17
authors: ['Vlachos, E.', 'Kolios, P.', 'Skliros, C.']
publication_types: ["1"]
abstract: "Strict power limits on small drone interceptors constrain the use of reusable directed energy payloads such as RF jammers and High Power Microwave (HPM) sources. High-gain beams can close the engagement link budget with minimal transmit power, but their required tight Field of View (FoV) conflicts with the aggressive maneuvers of a pursuing multi-rotor. This paper resolves this conflict with a hardware-aware safety filter using Control Barrier Functions (CBFs) on the SE(3) manifold. The filter provides formal pointing guarantees, enabling highly directional antennas whose gain would otherwise be sacrificed for pointing tolerance. We formulate a phased array's electronic steering limits as a relative-degree-two safety constraint with analytically verified Lie derivatives and solve the resulting Quadratic Program (QP) via ADMM with a constant-time core factorization. Validation in a nonlinear SE(3) simulation and a custom 6-DOF Software-in-the-Loop (SITL) environment demonstrates the proposed CBF eliminates all FoV violations and recovers up to 12.0 dB of antenna gain by tightening the beam. The approach also reveals conventional pitch clamping provides negligible benefit against FoV violations, avoids the severe actuator-saturation failure modes of multi-step Model Predictive Control (MPC)-CBF architectures, and executes reliably in under 350 μs."
featured: false
publication: "*2026 International Conference on Unmanned Aircraft Systems (ICUAS)*"
doi: "10.1109/ICUAS69441.2026.11598666"
# Code, data and slides: Zenodo record 20808892
url_code: "https://doi.org/10.5281/zenodo.20808892"
tags: ["Research", "UAVs", "Control Barrier Functions", "Counter-UAS", "SE(3)", "ISAC"]
projects: ["eusome"]
---

## Simulation Demo

The animation below compares two methods on the SE(3) CBF scenario: the **unfiltered** controller (red) and the proposed **ADMM-CBF** safety filter (blue), which maintains FoV pointing throughout the pursuit maneuver.

{{< video src="demo.mp4" controls="yes" >}}

## Key Contributions

- A **hardware-aware CBF safety filter** on the SE(3) manifold that provides formal FoV pointing guarantees for directed-energy payloads under aggressive pursuit dynamics.
- Formulation of phased-array electronic steering limits as a **relative-degree-two safety constraint** with analytically verified Lie derivatives.
- An **ADMM solver** with constant-time core factorization enabling real-time onboard execution.
- Validation in both a nonlinear SE(3) simulation and a **PX4 SITL** environment, demonstrating elimination of all FoV violations and recovery of antenna gain through beam tightening.

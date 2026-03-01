---
title: "Two Papers Submitted to ICUAS 2026"
date: 2026-02-26
summary: "We submitted two papers to ICUAS 2026: one on semantically-informed UAV path planning for mmWave connectivity in urban environments, and one on hardware-aware SE(3) Control Barrier Functions for counter-UAS interception with directed energy payloads."
tags: ["publication", "research", "UAV", "mmWave"]
pub_type: "paper"
categories: ["paper"]
---

We are excited to announce the submission of two papers to the **2026 International Conference on Unmanned Aircraft Systems (ICUAS)**:

---

### Semantically-Informed Predictive Control for Autonomous UAV Connectivity in Urban Environments
*Evangelos Vlachos and Dimitrios Tsourounis*

mmWave UAV links suffer in urban environments because radar cannot tell concrete from vegetation — both attenuate the signal, but only concrete truly blocks it. Our framework fuses 60 GHz radar with a YOLO-based semantic classifier to build an *Effective Capacity* field (C_raw × reliability) and plan through it via a two-layer controller:

1. **SI-RRT** — an RRT backbone that rejects candidate waypoints in multipath traps and low-reliability zones before they enter the tree.
2. **Gradient Planner** — deforms the backbone by ascending ∇C_eff, simultaneously signal-seeking and reliability-seeking through the product-rule decomposition.

Monte Carlo results over 100 independent urban canyon environments show **+65% effective throughput** vs. signal-strength baselines, **0.96 link reliability**, and **97.3% of an oracle** with perfect global channel knowledge.

---

### Hardware-Aware SE(3) Control Barrier Functions for Counter-UAS Interceptors with Directed Energy Payloads
*Evangelos Vlachos, Panayiotis Kolios, and Christos Skliros*

This paper addresses the safety-critical control problem of keeping a directed-energy phased-array payload's boresight aimed at a target UAS during high-speed interception. We develop SE(3) Control Barrier Functions that enforce a field-of-view constraint on the interceptor's attitude while respecting the physical limits of the onboard hardware, solved efficiently via ADMM at high update rates.

---

Both works are supported by the EU Horizon Europe project [EUSOME](https://eusome-project.eu/) (Grant Agreement No. 101187121).

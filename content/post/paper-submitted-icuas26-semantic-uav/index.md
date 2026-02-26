---
title: "New Paper Submitted: Semantically-Informed Predictive Control for Autonomous UAV Connectivity in Urban Environments"
date: 2026-02-26
summary: "We submitted a new paper to ICUAS 2026 proposing a two-layer UAV path planner that fuses 60 GHz mmWave radar with visual semantic classification to maximize reliable throughput in urban environments — achieving 65% improvement over signal-strength baselines and 97.3% of a perfect-knowledge oracle."
tags: ["publication", "research", "UAV", "mmWave"]
pub_type: "paper"
categories: ["paper"]
---

We are excited to announce the submission of our new paper to the **2026 International Conference on Unmanned Aircraft Systems (ICUAS)**:

> **Semantically-Informed Predictive Control for Autonomous UAV Connectivity in Urban Environments**
> Evangelos Vlachos and Dimitrios Tsourounis

mmWave UAV links suffer in urban environments because radar cannot tell concrete from vegetation — both attenuate the signal, but only concrete truly blocks it. Our framework fuses 60 GHz radar with a YOLO-based semantic classifier to build an *Effective Capacity* field (C_raw × reliability) and plan through it via a two-layer controller:

1. **SI-RRT** — an RRT backbone that rejects candidate waypoints in multipath traps and low-reliability zones before they enter the tree.
2. **Gradient Planner** — deforms the backbone by ascending ∇C_eff, simultaneously signal-seeking and reliability-seeking through the product-rule decomposition.

Monte Carlo results over 100 independent urban canyon environments show **+65% effective throughput** vs. signal-strength baselines, **0.96 link reliability**, and **97.3% of an oracle** with perfect global channel knowledge.

This work is supported by the EU Horizon Europe project [EUSOME](https://eusome-project.eu/) (Grant Agreement No. 101187121).

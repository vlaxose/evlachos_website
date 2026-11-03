---
title: "Paper Submitted to IEEE OJ-COMS"
date: 2026-11-03
summary: "We submitted a paper on sensing-aided channel estimation for THz XL-MIMO ISAC systems."
tags: ["publication", "research", "ISAC", "THz", "XL-MIMO", "channel estimation", "6G"]
pub_type: "paper"
categories: ["paper"]
---

We submitted a new paper to the **IEEE Open Journal of the Communications Society (OJ-COMS)**:

### Sensing-Aided Channel Estimation for THz XL-MIMO ISAC Systems
*Evangelos Vlachos and George C. Alexandropoulos*

Terahertz XL-MIMO links pose a channel estimation challenge because ultra-wide bandwidth couples angle and delay across large apertures and short pilot blocks limit identifiability. We propose a sensing-aided estimator for fixed THz links that uses a coarse range and departure angle from an uplink sounding stage to warm-start an alternating minimization over path gains, delays, and angles. The sensed angle serves as a prior so that small angle errors do not saturate the dictionary at an XL aperture. The estimator refines angles from pilots and returns a delay profile to the sensing function, closing an ISAC loop that carries refined angular information forward between frames. In simulations it gives a lower normalized mean-square error than beamspace and least-squares methods at short pilot lengths, and a lower steady-state pilot load. It extends our [EUSIPCO 2025](/publication/vlachos-biconvex-2025/) and [ISAC 2026](/publication/vlachos-sensing-thz-xlmimo-2026/) papers.

Key contributions:
- **Sensing warm start**: use coarse range and angle from sounding to initialize optimization for THz XL-MIMO.
- **Closed ISAC loop**: feed refined angles and delay profiles between sensing and estimation stages.
- **Estimator design**: derive angle accuracy requirements and an alternating minimization that supports short pilot blocks.

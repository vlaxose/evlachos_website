---
title: "Paper Submitted to IEEE ISAC 2026"
date: 2026-06-01
summary: "We submitted a conference paper on sensing-aided THz XL-MIMO channel estimation via biconvex ADMM to the 2026 IEEE International Symposium on Joint Communications and Sensing (ISAC 2026)."
tags: ["publication", "research", "ISAC", "THz", "XL-MIMO", "channel estimation", "ADMM", "6G"]
pub_type: "paper"
categories: ["paper"]
---

We submitted a new paper to the **2026 IEEE International Symposium on Joint Communications and Sensing (ISAC 2026)**:

### Sensing-Aided THz XL-MIMO Channel Estimation via Biconvex ADMM
*Evangelos Vlachos and George C. Alexandropoulos*

Terahertz XL-MIMO systems face a dual-wideband fading challenge: ultra-wide bandwidth introduces simultaneous spatial beam squint and temporal multipath spread, coupling angle and delay estimation across hundreds of antenna pairs. This work proposes a sensing-aided framework that exploits the base station's monostatic radar output to warm-start a biconvex ADMM algorithm, jointly recovering the channel matrix and the binary delay-support vector at no additional pilot overhead.

Key contributions:

- **Binary delay-support structure**: We show that the THz XL-MIMO dual-wideband channel concentrates onto a shared binary delay support of drastically reduced dimension, and develop a biconvex ADMM where iterative hard thresholding (IHT) exactly enforces this structure.
- **Sensing-aided warm start**: The monostatic radar output initialises the delay-support estimate, yielding provably exact support recovery beyond a pilot-length threshold — with no extra pilot cost and simultaneously delivering the delay profile as a sensing output.
- **CRB proximity**: The proposed estimator closely approaches the Cramér-Rao Bound, strictly outperforming sparse recovery and oracle-LS baselines in the barely-determined regime.

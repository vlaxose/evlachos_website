---
title: "Distributed ISAC State Estimation for UAV Swarms via Asynchronous Consensus ADMM"
date: 2026-06-13
publishDate: 2026-06-13
authors: ['Vlachos, E.']
publication_types: ["2"]
abstract: "We propose a fully distributed ADMM framework for integrated sensing and communication (ISAC) in UAV swarms over millimeter-wave massive MIMO links. Each UAV operates a single RF chain, making channel estimation severely underdetermined; position-based priors can regularize it, but GPS noise limits their utility. Our consensus formulation lets UAVs exchange only position estimates and dual variables over sidelinks, jointly solving channel estimation and cooperative position refinement in every ADMM iteration. Each UAV further employs monostatic radar sensing to obtain noisy inter-UAV displacement estimates that supplement GPS, closing the ISAC loop: sensing-derived geometry feeds back to improve communication performance. An asynchronous variant reuses stale neighbor data to tolerate sidelink packet losses, with provable almost-sure convergence under i.i.d. losses. Simulations under both heterogeneous and uniform GPS noise demonstrate near-genie-aided performance, outperforming non-cooperative and centralized baselines even at 80% packet loss and gracefully degrading with sensing noise."
featured: false
publication: "*In preparation for IEEE Open Journal of Signal Processing*"
tags: ["Research", "UAVs", "ISAC", "ADMM", "Distributed Estimation", "Massive MIMO", "6G"]
---

## Key Contributions

- **Joint consensus formulation**: A fully distributed ADMM framework in which UAVs exchange only position estimates and dual variables over sidelinks, solving single-RF-chain channel estimation jointly with cooperative position refinement at every iteration.
- **Closing the ISAC loop**: Monostatic radar sensing at each UAV supplies noisy inter-UAV displacement estimates that supplement GPS, so sensing-derived geometry directly improves communication performance.
- **Asynchronous robustness**: A variant that reuses stale neighbor data tolerates sidelink packet losses with provable almost-sure convergence under i.i.d. losses, sustaining near-genie-aided performance even at 80% packet loss.

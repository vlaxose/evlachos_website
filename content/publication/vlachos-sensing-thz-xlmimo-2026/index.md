---
title: "Sensing-Aided THz XL-MIMO Channel Estimation via Biconvex ADMM"
date: 2026-06-01
publishDate: 2026-06-01
authors: ['Vlachos, E.', 'Alexandropoulos, G. C.']
publication_types: ["1"]
abstract: "Terahertz (THz) extremely large-array MIMO is a cornerstone technology for 6G integrated sensing and communication (ISAC), but its ultra-wide bandwidth introduces dual-wideband fading: simultaneous spatial beam squint and temporal multipath spread that couple angle and delay estimation across hundreds of antenna pairs. This paper proposes a sensing-aided framework in which the base station's monostatic radar output warm-starts a biconvex ADMM algorithm that jointly recovers the channel matrix and the binary delay-support vector. The recovered delay profile simultaneously closes the ISAC loop as a sensing output at no additional pilot overhead. Simulations on a large-scale THz XL-MIMO system show that the proposed method substantially outperforms sparse recovery and oracle-LS baselines, achieves exact delay-support recovery beyond a pilot-length threshold, and closely approaches the Cramér-Rao Bound."
featured: false
publication: "*IEEE International Symposium on Joint Communications and Sensing (ISAC 2026)* — under review"
tags: ["Research", "ISAC", "THz", "XL-MIMO", "Channel Estimation", "ADMM", "6G"]
---

## Key Contributions

- **Biconvex ADMM with binary support enforcement**: We show that the THz XL-MIMO dual-wideband channel concentrates onto a shared binary delay support of drastically reduced dimension, and develop a biconvex ADMM where iterative hard thresholding (IHT) exactly enforces this structure — outperforming continuous-valued sparse recovery and oracle-LS baselines in the barely-determined regime.
- **Sensing-aided warm start at no pilot cost**: The base station's monostatic radar output initialises the delay-support estimate, yielding provably exact support recovery beyond a pilot-length threshold, with no additional pilot overhead.
- **CRB proximity**: The proposed estimator closely approaches the Cramér-Rao Bound and closes the ISAC sensing loop by delivering the recovered delay profile as a radar output.

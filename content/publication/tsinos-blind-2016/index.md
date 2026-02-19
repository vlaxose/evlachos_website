---
title: "Blind distributed beamforming via matrix completion"
date: 2016-01-01
doi: "10.1109/spawc.2016.7536750"
publishDate: 2016-01-01
authors: ['Tsinos, C. G.', 'Vlachos, E.', 'Berberidis, K.']
publication_types: ["1"]
abstract: "In this paper, we consider the problem of distributed beamforming for maximization of the receiver signal-to-noise­ ratio (SNR) subject to a total transmit power constraint. We investigate the case where the optimal beamforming weights are expressed based on the second-order statistics of the in­ volved channels, while the communication among the relays is interference-limited. In this context, we propose a relay­ cooperative scheme for interference minimization, where only a limited number of correlation quantities are sent to the fusion center (FC). We propose a technique which overcomes the problem of the incomplete covariance matrices via matrix completion. Through simulation results, we show that, after a number of iterations, the proposed technique converges to the true covariance matrices and thus the optimal beamformer may be computed."
featured: false
url_pdf: "paper.pdf"
publication: "*2016 IEEE 17th International Workshop on Signal Processing Advances in Wireless Communications (SPAWC)*"
tags: ["Research", "6G", "UAVs"]
---

## Key Contributions
- Addresses the challenge of distributed beamforming with incomplete channel statistics by leveraging matrix completion techniques.
- Proposes a low-complexity iterative method for estimating correlation matrices at the fusion center using partial measurements.
- Demonstrates that the technique converges to the optimal beamforming solution with a limited number of relays providing direct communication.

## Results & Insights

{{< figure src="fig2.png" caption="Convergence curves for matrix completion of correlation matrices R(t) and G(t) versus time, showing NMSE reduction for different numbers of known entries." >}}

These results demonstrate that the proposed matrix completion technique achieves near-optimal performance with significantly fewer known entries (34% for K=10), highlighting its efficiency in recovering the full correlation matrices needed for optimal beamforming.

{{< figure src="fig4.png" caption="Convergence curves for the beamforming vector estimation, showing the approach converging to the optimal beamformer after multiple iterations." >}}

These curves confirm that the iterative process successfully computes the optimal beamforming vector, leading to substantial SNR improvement and validating the effectiveness of the matrix completion approach in practical scenarios.

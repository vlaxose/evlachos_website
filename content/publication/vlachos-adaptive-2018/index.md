---
title: "Adaptive Windowing for ICI Mitigation in Vehicular Communications"
date: 2018-01-01
doi: "10.1109/lwc.2018.2842226"
publishDate: 2018-01-01
authors: ['Vlachos, E.', 'Lalos, A. S.', 'Berberidis, K.', 'Thompson, J.']
publication_types: ["2"]
abstract: "The performance of orthogonal frequency division multiplexing systems in vehicular environments suffers from intercarrier interference (ICI) and the inherent non station- arity of the channel statistics. Receiver windowing constitutes an effective technique for enhancing the banded structure of the frequency-domain channel matrix, thus improving the effec- tiveness of a banded equalizer for ICI mitigation. However, its optimality has been veriﬁed only for stationary channels with perfectly known statistics. In non stationary channels, the second-order statistics have to be tracked and the optimal per- formance can be achieved at the expense of cubic complexity over the number of the subcarriers. To overcome this limita- tion, an adaptive windowing technique is proposed that is able to track directly an optimal receiver window in terms of average signal-to-interference noise ratio, requiring only linear complex- ity. Extensive simulation results verify both the ability of the proposed approach to track the time varying channel statistics and its increased robustness to channel estimation errors that are common in vehicular environments."
featured: false
url_pdf: "paper.pdf"
publication: "*IEEE Wireless Communications Letters*"
tags: ["Research", "6G", "UAVs"]
---

## Key Contributions
- Proposed an adaptive windowing technique for ICI mitigation in OFDM systems operating in vehicular environments.
- The technique tracks time-varying channel statistics to maximize average SINR with linear computational complexity.
- Demonstrated enhanced robustness to channel estimation errors, which are common in vehicular communication scenarios.

## Results & Insights

The proposed technique shows superior ICI mitigation performance, particularly at high SNR, compared to existing fixed and adaptive windowing methods.

The adaptive windowing technique achieves lower bit error rates across various vehicular speeds, confirming its effectiveness in non-stationary channel conditions.

The algorithm demonstrates stable convergence with appropriate step-size selection, maintaining low computational complexity while adapting to channel variations.

The technique exhibits significantly better performance stability in the presence of channel estimation errors compared to conventional methods.

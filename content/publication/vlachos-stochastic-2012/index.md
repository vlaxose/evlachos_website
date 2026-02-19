---
title: "Stochastic Gradient Pursuit for Adaptive Equalization of Sparse Multipath Channels"
date: 2012-01-01
doi: "10.1109/JETCAS.2012.2214631"
publishDate: 2012-01-01
authors: ['Vlachos, E.', 'Lalos, A.S.', 'Berberidis, K.']
publication_types: ["2"]
abstract: "In this paper, a new heuristic algorithm for the sparse adaptive equalization problem, termed as stochastic gradient pursuit, is proposed. A decision-feedback equalization structure is used in order to effectively mitigate the effect of long mul- tipath channels. Diverging from the commonly used approach of sparse channel identiﬁcation, we exploit the sparsity of the inverse problem under the compressive sensing perspective. Also, an extension to the case where the sparsity order parameter is unknown, is developed. Simulation results verify that the pro- posed schemes exhibit faster convergence and improved tracking capabilities compared to conventional and other sparse aware equalization schemes, offering at the same time a reduced compu- tational complexity."
featured: false
url_pdf: "paper.pdf"
publication: "*IEEE Journal on Emerging and Selected Topics in Circuits and Systems*"
tags: ["Research", "6G", "UAVs"]
---

## Key Contributions
- Proposed a novel heuristic algorithm, termed Stochastic Gradient Pursuit, for sparse adaptive equalization.
- Utilized a decision-feedback equalization structure to effectively handle long multipath channels.
- Exploited channel sparsity from a compressive sensing perspective, developing an extension for unknown sparsity order.
- Offered reduced computational complexity while maintaining performance comparable to conventional methods.

## Results & Insights

{{< figure src="fig2.png" caption="Mean-square error (MSE) learning curves comparing the proposed Stochastic Gradient Pursuit algorithm against several benchmark methods." >}}
These curves demonstrate the fast convergence and improved tracking capabilities of the proposed algorithm compared to conventional and other sparse-aware equalization schemes.

{{< figure src="fig3.png" caption="Mean-square error (MSE) learning curves for different sparsity orders in the proposed Stochastic Gradient Pursuit algorithm." >}}
These results show the algorithm's effectiveness in tracking sparse multipath channels even when the exact sparsity order is unknown.

{{< figure src="fig4.png" caption="Bit error rate (BER) performance of the proposed Stochastic Gradient Pursuit algorithm compared to benchmark methods." >}}
The proposed algorithm achieves BER performance comparable to benchmark methods while requiring significantly less computational complexity.

{{< figure src="fig5.png" caption="Bit error rate (BER) performance versus input SNR for the proposed Stochastic Gradient Pursuit algorithm." >}}
The results indicate that the proposed algorithm maintains good performance across a range of SNR values, demonstrating its robustness.

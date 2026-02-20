---
title: "Low-complexity OSIC equalization for OFDM-based Vehicular Communications"
date: 2016-01-01
doi: "10.1109/TVT.2016.2598185"
publishDate: 2016-01-01
authors: ['Vlachos, E.', 'Lalos, A. S.', 'Berberidis, K.']
publication_types: ["2"]
abstract: "Vehicular communication systems are usually equipped with orthogonal frequency division multiplexing (OFDM) transceivers that operate on rapidly changing radio propagation environments, which results in high Doppler and delay spreads. More speciﬁcally, in these environments, the experienced channels are doubly selective and introduce severe intercarrier interference (ICI) at the receiver. An effective ICI mitigation technique is desired as a constituent part of an ordered successive interference cancellation (OSIC) architecture, which turns out to be computationally efﬁcient, since it may require the solution of linear systems with multiple right-hand sides. To decrease the complexity, several techniques suggest mitigating the ICI by considering only a small number of adjacent subcarriers. However, this approximation introduces an error ﬂoor, which may result in unacceptable bit error rates (BER) at high signal-to-noise ratio regimes. In this paper, we propose a new OSIC equalization technique based on an iterative Galerkin projection-based algorithm that reduces the computational cost without sacriﬁcing the performance gains of the OSIC architecture."
featured: false
url_pdf: "paper.pdf"
publication: "*IEEE Transactions on Vehicular Technology*"
tags: ["Research", "6G", "UAVs"]
---

## Key Contributions
- Proposing an OSIC equalization technique tailored for doubly selective vehicular channels to mitigate ICI effectively.
- Introducing an iterative Galerkin projection-based algorithm that reduces computational complexity while maintaining performance.
- Demonstrating the benefits of the proposed scheme in terms of both performance and complexity through simulations in high Doppler environments.

## Results & Insights

{{< figure src="fig4.png" caption="BER comparison versus SNR for low Doppler spread and 4-QAM modulation." >}}
This figure shows that the proposed OSIC equalizer outperforms existing methods at low SNR, highlighting its effectiveness in mitigating ICI even under less severe channel conditions.

{{< figure src="fig5.png" caption="BER comparison versus SNR for medium Doppler spread and 4-QAM modulation." >}}
The results indicate that the proposed algorithm maintains a performance advantage over benchmarks at medium Doppler spreads, confirming its robustness.

{{< figure src="fig6.png" caption="BER comparison versus SNR for high Doppler spread and 4-QAM modulation." >}}
The simulation results demonstrate that the proposed equalizer achieves lower BER values than existing nonbanded ICI cancellation schemes even at high Doppler spreads, validating its superior performance in challenging vehicular environments.

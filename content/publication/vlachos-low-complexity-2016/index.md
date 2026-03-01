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

{{< figure src="fig4.png" caption="Complexity order of the proposed ICI equalization method versus standard vehicular communication standards (V2V, Wi-Fi, WiMAX, LTE, DVB-T) as a function of Doppler spread and OFDM size N." >}}
The proposed Galerkin-based equalizer achieves O(N) complexity for typical vehicular channels, making it significantly more efficient than full ICI cancellation approaches that require O(N²) or O(N⁴) operations.

{{< figure src="fig1.png" caption="BER versus SNR comparison of the proposed OSIC equalizer against benchmark schemes for low Doppler spread and 4-QAM modulation." >}}
The proposed method closely tracks the performance of full OSIC while operating at a fraction of the complexity, demonstrating its practical viability for vehicular OFDM systems.

{{< figure src="fig2.png" caption="BER versus SNR comparison for medium and high Doppler spread scenarios, illustrating robustness of the proposed equalizer under severe ICI conditions." >}}
The results confirm that the Galerkin projection approach maintains performance gains over banded approximation benchmarks even as Doppler spread increases, validating its suitability for high-mobility environments.

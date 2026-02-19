---
title: "Regularized MMSE ICI equalization for OFDM systems over doubly selective channels"
date: 2013-01-01
doi: "10.1109/isspit.2013.6781924"
publishDate: 2013-01-01
authors: ['Vlachos, E.', 'Lalos, A.S.', 'Berberidis, K.']
publication_types: ["1"]
abstract: "In this work, we consider a wireless OFDM system operating over doubly selective channels, where the Doppler effect destroys the orthogonality between subcarriers and hence, results into severe intercarrier interference (ICI). To mitigate this effect, computational demanding equalization schemes that require the inversion of the channel matrix, should be applied. In order to achieve linear complexity in the number of the subcarriers, a banded approximation of the channel matrix is usually adopted, whereas the performance of the equalizer is sig­ nificantly degraded. To recover this performance loss, we propose a regularized estimation framework for MMSE ICI equalization in the frequency domain, where the complexity remains linear with respect to the number of the subcarriers. Simulation results verify the effectiveness of the proposed regularization. I. INTROD UCTION Orthogonal frequency-division multiplexing (OFDM) has been used for several wireless applications such as broadcast­ ing of digital audio and digital video [1], [2] and mobile radio communication [3], [4]."
featured: false
url_pdf: "paper.pdf"
publication: "*IEEE International Symposium on Signal Processing and Information Technology*"
tags: ["Research", "6G", "UAVs"]
---

## Key Contributions
- Development of a regularized MMSE ICI equalization technique for doubly selective channels to mitigate the effects of Doppler-induced ICI in OFDM systems.
- Proposing a banded approximation for the channel matrix to reduce computational complexity while maintaining performance.
- Demonstrating that the regularized estimation can recover performance similar to exact MMSE equalization, offering a balance between performance and computational efficiency.

## Results & Insights

{{< figure src="fig1.png" caption="Comparison of BER versus SNR for different equalization schemes, showing the performance of the proposed regularized MMSE equalizer." >}}
This figure demonstrates that the proposed regularized MMSE equalizer achieves performance comparable to other advanced methods like iterative MMSE and decision-feedback equalizers, particularly at higher SNR levels.

{{< figure src="fig2.png" caption="Comparison of BER versus normalized Doppler frequency for the proposed regularized MMSE equalizer and other methods." >}}
This result highlights the robustness of the proposed regularized MMSE equalizer against frequency-selective fading, showing lower BER across different Doppler conditions compared to the benchmark methods.

{{< figure src="fig3.png" caption="Comparison of BER versus the length K of the banded approximation matrix, with SNR fixed at 30 dB." >}}
This figure confirms that increasing the length K improves the BER performance, approaching the performance of the exact MMSE equalizer, while the banded approximation effectively reduces computational complexity.

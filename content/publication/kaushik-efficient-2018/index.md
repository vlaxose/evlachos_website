---
title: "Efficient Channel Estimation in Millimeter Wave Hybrid MIMO Systems with Low Resolution ADCs"
date: 2018-01-01
doi: "10.23919/eusipco.2018.8553303"
publishDate: 2018-01-01
authors: ['Kaushik, A.', 'Vlachos, E.', 'Thompson, J.', 'Perelli, A.']
publication_types: ["1"]
abstract: "This paper proposes an efﬁcient channel estima- tion algorithm for millimeter wave (mmWave) systems with a hybrid analog-digital multiple-input multiple-output (MIMO) architecture and few-bits quantization at the receiver. The sparsity of the mmWave MIMO channel is exploited for the problem formulation while limited resolution analog-to-digital converters (ADCs) are used in the receiver architecture. The estimation problem can be tackled using compressed sensing through the Stein’s unbiased risk estimate (SURE) based parametric denoiser with the generalized approximate message passing (GAMP) framework. Expectation-maximization (EM) density estimation is used to avoid the need of specifying channel statistics resulting the EM-SURE-GAMP algorithm to estimate the channel. SURE, depending on the noisy observation, is mini- mized to adaptively optimize the denoiser within the parametric class at each iteration. The proposed solution is compared with the expectation-maximization generalized AMP (EM-GAMP) solution and the mean square error (MSE) performs better with respect to low and high signal-to-noise ratio (SNR) regimes, the number of ADC bits, and the training length. The use of the low resolution ADCs reduces power consumption and leads to an efﬁcient mmWave MIMO system."
featured: false
url_pdf: "paper.pdf"
publication: "*2018 26th European Signal Processing Conference (EUSIPCO)*"
tags: ["Research", "6G", "UAVs"]
---

## Key Contributions
- Proposes an EM-SURE-GAMP algorithm that combines compressed sensing with expectation-maximization and adaptive denoising to exploit channel sparsity.
- Develops a solution that adapts to low-resolution ADCs by using an additive quantization noise model (AQNM) and minimizes estimation error through Stein's Unbiased Risk Estimate (SURE).
- Demonstrates significant performance improvements in MSE across various SNR regimes, ADC bit resolutions, and training lengths compared to existing methods like EM-GAMP.

## Results & Insights

{{< figure src="fig2.png" caption="Mean square error (MSE) versus signal-to-noise ratio (SNR) for different channel estimation methods." >}}
The proposed EM-SURE-GAMP algorithm achieves lower MSE across all SNR regimes compared to the EM-GAMP baseline, particularly at low and high SNR.

{{< figure src="fig3.png" caption="Mean square error (MSE) versus the number of ADC bits for different channel estimation methods." >}}
EM-SURE-GAMP consistently outperforms EM-GAMP as the number of ADC bits decreases, demonstrating robustness to quantization effects.

{{< figure src="fig4.png" caption="Comparison of channel estimation performance across different training lengths." >}}
The algorithm maintains superior performance even with shorter training sequences, highlighting its efficiency and adaptability to practical constraints.

{{< figure src="fig5.png" caption="Illustration of convergence behavior for the EM-SURE-GAMP algorithm." >}}
The EM-SURE-GAMP algorithm converges faster and achieves lower MSE compared to EM-GAMP, indicating its practical suitability for real-time applications.

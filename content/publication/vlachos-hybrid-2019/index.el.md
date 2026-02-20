---
title: "Hybrid Beamforming with Random Analog Sampling for Wideband Channel Estimation in Millimeter Wave Massive MIMO Systems"
date: 2019-01-01
doi: "10.1109/spawc.2019.8815512"
publishDate: 2019-01-01
authors: ['Vlachos, E.', 'Alexandropoulos, G. C.', 'Thompson, J.']
publication_types: ["1"]
abstract: "Hybrid analog and digital BeamForming (HBF) transceiver architectures realizing directive communication over large bandwidths in millimeter Wave (mmWave) massive Multi- ple Input Multiple Output (MIMO) systems require the availabil- ity of accurate channel estimation. This is, however, a challenging task mainly due to the short channel coherence time and the hardware limitations imposed by HBF architectures. In this paper, we capitalize on recent matrix completion tools and develop a novel wideband channel estimation technique for mmWave massive MIMO systems with HBF reception. The proposed iterative algorithm exploits jointly the low rank and beamspace sparsity properties to provide more accurate recovery, especially for short beam training intervals. We introduce a novel analog combining architecture that includes a random sub- sampling step before the input of the analog received signals to the digital component of the HBF receiver. This step supports the proposed estimation technique in providing the sampling set of measurements for recovering the unknown channel matrix. The impact of various system parameters on the effectiveness of the designed algorithm and the performance improvement of our technique over representative state-of-the-art ones is demonstrated through indicative simulation results."
featured: false
url_pdf: "paper.pdf"
publication: "*2019 IEEE 20th International Workshop on Signal Processing Advances in Wireless Communications (SPAWC)*"
tags: ["Research", "6G", "UAVs"]
---

## Key Contributions
- Development of a novel wideband channel estimation technique for mmWave massive MIMO systems with hybrid beamforming reception.
- Capitalization on matrix completion tools to exploit the sparsity and low-rank properties of wireless channels.
- Proposal of an analog combining architecture featuring an extended combiner and random sub-sampler to enhance estimation accuracy.
- Demonstration of improved performance in terms of MSE with reduced beam training length.

## Results & Insights
This figure demonstrates that the proposed algorithm achieves significantly lower channel estimation error (NMSE) compared to benchmark methods, particularly at higher SNR levels, validating its effectiveness.

The results show that the proposed algorithm converges faster and achieves lower steady-state NMSE even with shorter training lengths, highlighting its efficiency in practical scenarios with limited beam training time.

This plot indicates that the proposed algorithm maintains superior performance even as the number of antenna elements increases, showcasing its scalability for massive MIMO systems.

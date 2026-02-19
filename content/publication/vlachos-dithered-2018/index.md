---
title: "Dithered Beamforming for Channel Estimation in Mmwave-Based Massive Mimo"
date: 2018-01-01
doi: "10.1109/icassp.2018.8461911"
publishDate: 2018-01-01
authors: ['Vlachos, E.', 'Thompson, J.']
publication_types: ["1"]
abstract: "In this work we consider the challenging problem of chan- nel estimation at the receiver of a massive multiple-input multiple-output system with hybrid analog/digital beamform- ing and low-resolution quantization. We propose a dithered beamforming architecture, where random control signals are injected to the analog part of the receiver beamformer and to the analog-to-digital converters to introduce randomness into the signal capturing process and combat the stair-case quanti- zation effects. The statistical properties of the dithered output are captured via an Expectation-Maximization approximation of the maximum a-posteriori estimator. A low-complexity al- gorithm is proposed which exhibits performance close to the oracle-based least-squares estimation of the sparse channel."
featured: false
url_pdf: "paper.pdf"
publication: "*2018 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*"
tags: ["Research", "6G", "UAVs"]
---

## Key Contributions
- Proposed a dithered beamforming architecture by injecting random control signals into the analog beamformer and ADCs to combat quantization effects.
- Developed a low-complexity Expectation-Maximization algorithm for sparse channel estimation in hybrid beamforming systems with low-resolution ADCs.
- Demonstrated that the technique effectively mitigates quantization non-linearities and improves channel estimation performance in mmWave massive MIMO systems.

{{< figure src="fig4.png" caption="Mean squared error (MSE) performance comparison for different quantization resolutions and dithering techniques across various signal-to-noise ratios (SNR)." >}}
This figure shows that the proposed dithered beamforming technique significantly reduces estimation error compared to non-dithered approaches, achieving near-optimal performance with a 1dB improvement for 2- and 3-bit quantization cases.

{{< figure src="fig3.png" caption="Convergence behavior of the proposed algorithm compared to an oracle-based method for different SNR values." >}}
The results demonstrate rapid convergence of the proposed algorithm, approaching near-optimal performance even with an approximate solution for the sparse channel estimation problem.

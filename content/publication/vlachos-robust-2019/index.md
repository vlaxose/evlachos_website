---
title: "Robust Estimator for Lens-based Hybrid MIMO with Low-Resolution Sampling"
date: 2019-01-01
doi: "10.1109/spawc.2019.8815573"
publishDate: 2019-01-01
authors: ['Vlachos, E.', 'Thompson, J.', 'Abbasi, M. A. Babar', 'Fusco, V. F.', 'Matthaiou, M.']
publication_types: ["1"]
abstract: "It is well known that large antenna arrays with beamforming capabilities are required to compensate for the high path-loss at millimeter-wave (mmWave) frequencies. Recently, a practical two-stage Rotman lens beamformer has demonstrated increased antenna gain with reduced implementation complexity, since the conventional beam selection network was omitted. In this work, we adopt this system and we investigate its per- formance in terms of symbol estimation when analog-to-digital converters (ADCs) with low-resolution sampling being employed. Although this design is characterized by low-complexity and low- cost, the analog beamformer and the ADCs introduce several impairments to the received signal. To mitigate these effects, we have developed a robust maximum a posteriori (MAP) estimator based on the Expectation-Maximization (EM) iterative algorithm. The proposed algorithm outperforms the conventional EM approach, exhibiting small mean-square-error in the medium to high signal-to-noise ratio regimes. I."
featured: false
url_pdf: "paper.pdf"
publication: "*2019 IEEE 20th International Workshop on Signal Processing Advances in Wireless Communications (SPAWC)*"
tags: ["Research", "6G", "UAVs"]
---

## Key Contributions
- Development of a robust maximum a posteriori (MAP) estimator based on the Expectation-Maximization (EM) algorithm for symbol estimation in lens-based hybrid MIMO systems with low-resolution ADCs.
- The proposed estimator effectively mitigates the impairments introduced by low-resolution ADCs and the analog beamformer, improving performance in medium to high signal-to-noise ratio (SNR) regimes.
- The work demonstrates that lower ADC resolution does not necessarily degrade system performance, offering a pathway to reduce hardware complexity and power consumption in mmWave MIMO systems.

## Results & Insights

{{< figure src="fig1.png" caption="Performance comparison of the proposed MAP-EM estimator versus conventional methods in terms of NMSE for different ADC resolutions." >}}
This figure shows that the proposed MAP-EM estimator significantly outperforms conventional methods, particularly at medium to high SNR, across various ADC resolutions, demonstrating its robustness and effectiveness.

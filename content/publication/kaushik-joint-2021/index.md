---
title: "Joint Bit Allocation and Hybrid Beamforming Optimization for Energy Efficient Millimeter Wave MIMO Systems"
date: 2021-01-01
doi: "10.1109/tgcn.2020.3026725"
url_arxiv: "https://arxiv.org/abs/1910.01479"
publishDate: 2021-01-01
authors: ['Kaushik, A.', 'Vlachos, E.', 'Tsinos, C.', 'Thompson, J.', 'Chatzinotas, S.']
publication_types: ["2"]
abstract: "In this article, we aim to design highly energy efﬁcient end-to-end communication for millimeter wave multiple- input multiple-output systems. This is done by jointly optimizing the digital-to-analog converter (DAC)/analog-to-digital converter (ADC) bit resolutions and hybrid beamforming matrices. The novel decomposition of the hybrid precoder and the hybrid combiner to three parts is introduced at the transmitter (TX) and the receiver (RX), respectively, representing the analog precoder/combiner matrix, the DAC/ADC bit resolution matrix and the baseband precoder/combiner matrix. The unknown matrices are computed as a solution to the matrix factorization problem where the optimal fully digital precoder or combiner is approximated by the product of these matrices. A novel and efﬁcient solution based on the alternating direction method of multipliers is proposed to solve these problems at both the TX and the RX. The simulation results show that the proposed solution, where the DAC/ADC bit allocation is dynamic during operation, achieves higher energy efﬁciency when compared with existing benchmark techniques that use ﬁxed DAC/ADC bit resolutions."
featured: true
url_pdf: "paper.pdf"
publication: "*IEEE Transactions on Green Communications and Networking*"
tags: ["Research", "6G", "UAVs"]
---

## Key Contributions
- Introduces a novel decomposition of hybrid precoders and combiners into three matrices representing the analog precoder/combiner, DAC/ADC bit resolution matrix, and baseband precoder/combiner.
- Proposes a joint optimization framework for hybrid beamforming matrices and DAC/ADC bit resolutions to maximize energy efficiency (EE).
- Develops an efficient solution based on the alternating direction method of multipliers (ADMM) to solve the optimization problem at both transmitter and receiver.

## Results & Insights

{{< figure src="fig1.png" caption="System architecture of the mmWave hybrid MIMO system with low-resolution DACs/ADCs, illustrating the three-part decomposition of the hybrid precoder/combiner and the beam training phase." >}}
The proposed three-part decomposition enables joint optimization of analog beamforming, bit resolution allocation, and digital combining, forming the foundation of the energy-efficient end-to-end design.

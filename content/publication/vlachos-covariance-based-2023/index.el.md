---
title: "Covariance-Based Hybrid Beamforming for Spectrally Efficient Joint Radar-Communications"
date: 2023-01-01
doi: "10.1109/icc45041.2023.10279571"
url_arxiv: "https://arxiv.org/abs/2211.08308"
publishDate: 2023-01-01
authors: ['Vlachos, Evangelos', 'Kaushik, Aryan']
publication_types: ["1"]
abstract: "Joint radar-communications (JRC) is considered to be a vital technology in deploying the next generation systems, since its useful in decongestion of the radio frequency (RF) spectrum and utilising the same hardware resources for dual functions. Using JRC systems for dual function generates interference be- tween both the operations which needs to be addressed in future standardization. Furthermore, JRC systems can be advanced by deploying hybrid beamforming which implements fewer number of RF chains than the number of transmit antennas. This paper designs a robust hybrid beamformer for minimizing the interfer- ence of a JRC transmitter via RF chain selection resulting into mutual information maximization. We consider a weighted mutual information for the dual function JRC system and implement a common analog beamformer for both the operations. The mutual information maximization problem is formulated which is non- convex and difficult to solve. The problem is simplified to convex form and solved using Dinkelbach approximation abased fractional programming. The performance of the optimal RF selection based proposed approach is evaluated, compared with baselines and its effectiveness is inferred via numerical results."
featured: false
url_pdf: "paper.pdf"
publication: "*IEEE International Conference on Communications (ICC)*"
tags: ["Research", "6G", "UAVs"]
---

## Key Contributions
- Proposes a robust hybrid beamformer based on covariance matrices to minimize interference in joint radar-communications systems.
- Introduces fractional programming for optimal RF chain selection, enabling flexibility in hybrid beamformer design.
- Maximizes mutual information using a weighted dual function approach, considering the trade-off between radar and communication performance.
- Incorporates hardware constraints with low-resolution DACs, ensuring practical implementation feasibility.

{{< figure src="fig2.png" caption="Ideal communication capacity and its covariance-based approximation for the JRC system." >}}
This figure demonstrates the effectiveness of the proposed covariance-based approach in approximating the ideal communication capacity, highlighting its accuracy and practicality for JRC systems.

{{< figure src="fig3.png" caption="Mutual information performance versus SNR for different weighting factors in the JRC system." >}}
The results show that the proposed method consistently outperforms baseline cases, except for the interference-free baseline, across various SNR levels and weighting factors.

{{< figure src="fig4.png" caption="Mutual information performance versus SNR for different numbers of transmit antennas in the JRC system." >}}
The proposed method exhibits superior performance compared to baseline approaches, particularly at higher SNR values, indicating its scalability and robustness.

{{< figure src="fig5.png" caption="Multi-user interference (MUI) performance versus the number of users for the proposed hybrid beamformer." >}}
The proposed method achieves lower MUI levels compared to baseline approaches, demonstrating its effectiveness in managing interference in multi-user scenarios.

---
title: "Dynamic RF Chain Selection for Energy Efficient and Low Complexity Hybrid Beamforming in Millimeter Wave MIMO Systems"
date: 2019-01-01
doi: "10.1109/tgcn.2019.2931613"
publishDate: 2019-01-01
authors: ['Kaushik, A.', 'Thompson, J.', 'Vlachos, E.', 'Tsinos, C.', 'Chatzinotas, S.']
publication_types: ["2"]
abstract: "This paper proposes a novel architecture with a framework that dynamically activates the optimal number of radio frequency (RF) chains used to implement hybrid beam- forming in a millimeter wave (mmWave) multiple-input and multiple-output (MIMO) system. We use fractional programming to solve an energy efﬁciency maximization problem and exploit the Dinkelbach method (DM)-based framework to optimize the number of active RF chains and data streams. This solution is updated dynamically based on the current channel conditions, where the analog/digital (A/D) hybrid precoder and combiner matrices at the transmitter and the receiver, respectively, are designed using a codebook-based fast approximation solution called gradient pursuit (GP). The GP algorithm shows less run time and complexity while compared to the state-of-the- art orthogonal matching pursuit (OMP) solution. The energy and spectral efﬁciency performance of the proposed frame- work is compared with the existing state-of-the-art solutions, such as the brute force (BF), the digital beamformer, and the analog beamformer. The codebook-free approaches to design the precoders and combiners, such as alternating direction method of multipliers (ADMMs) and singular value decompo- sition (SVD)-based solution are also shown to be incorporated into the proposed framework to achieve better energy efﬁciency performance."
featured: true
url_pdf: "paper.pdf"
publication: "*IEEE Transactions on Green Communications and Networking*"
tags: ["Research", "6G", "UAVs"]
---

## Key Contributions
- Proposing a novel hybrid beamforming architecture with dynamic RF chain selection to optimize energy efficiency.
- Introducing a fractional programming framework based on the Dinkelbach method to determine the optimal number of active RF chains.
- Developing a low-complexity codebook-based gradient pursuit (GP) algorithm for hybrid precoder design, outperforming state-of-the-art methods like OMP.
- Demonstrating significant improvements in energy efficiency and reduced computational complexity compared to brute-force and fully digital beamforming approaches.

{{< figure src="fig2.png" caption="Performance comparison of energy efficiency across different hybrid beamforming techniques under varying SNR conditions." >}}
This figure demonstrates that the proposed dynamic RF chain selection framework achieves superior energy efficiency compared to conventional hybrid beamforming methods, particularly at higher SNR levels.

{{< figure src="fig3.png" caption="Convergence behavior and bit error rate performance of the proposed Dinkelbach method-based optimization framework." >}}
The results show rapid convergence of the optimization algorithm and significantly lower bit error rates compared to benchmark methods, validating the effectiveness of the proposed approach.

{{< figure src="fig4.png" caption="Power consumption analysis of the proposed framework versus conventional hybrid beamforming approaches across different SNR values." >}}
The proposed dynamic RF chain selection reduces power consumption by up to 30% compared to fully-connected hybrid beamforming, especially at moderate SNR levels.

{{< figure src="fig5.png" caption="Computational complexity comparison of the proposed gradient pursuit algorithm versus state-of-the-art methods." >}}
The proposed framework achieves substantially lower computational complexity (reduced by 40-60%) while maintaining comparable performance to more complex optimization techniques.

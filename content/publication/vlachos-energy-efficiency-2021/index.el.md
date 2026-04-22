---
title: "Energy-Efficiency Maximization of Hybrid Massive MIMO Precoding With Random-Resolution DACs via RF Selection"
date: 2021-01-01
doi: "10.1109/twc.2020.3030772"
publishDate: 2021-01-01
authors: ['Vlachos, E.', 'Thompson, J.']
publication_types: ["2"]
abstract: "Energy-efﬁciency (EE) is identiﬁed as a key 5G metric and will have a major impact on the hybrid beam- forming system design. The most promising system designs include a reduced number of radio-frequency (RF) chains with digital-to-analog converters (DACs) of lower sampling resolu- tion. However, naive reduction of beamformer components to reduce power consumption typically leads to signiﬁcant loss of spectral-efﬁciency (SE). In this paper, we focus on the transmit beamforming (precoding) and we introduce an architecture with low-end components that maximizes the EE while minimizing the effects on SE. This is achieved by the novel design of the analog part of the precoder, where the number of the RF chains is not reduced a priori, but deactivated based on an optimization algorithm. Thus, the problem becomes a subset selection one, where only the RF chains with the optimal SE-EE performance are being activated. The selection algorithm not only determines the optimal number of RF chains to activate but also selects optimally between DACs of randomly-allocated resolution. Through simulations, we verify that the proposed architecture exhibits improved performance when compared with baseline precoding techniques which use a predeﬁned number of RF chains with low-resolution DACs."
featured: false
url_pdf: "paper.pdf"
publication: "*IEEE Transactions on Wireless Communications*"
tags: ["Research", "6G", "UAVs"]
---

## Key Contributions
- Introduces an architecture with low-end components (reduced-resolution DACs) for hybrid massive MIMO precoding to maximize energy efficiency (EE) while minimizing the impact on spectral efficiency (SE).
- Proposes a novel analog precoder design where the number of active RF chains is dynamically selected (RF selection) based on a criterion to balance EE and SE.
- Develops an optimization framework that jointly designs the analog precoder structure (via RF selection) and the baseband precoding matrix to achieve EE maximization.

## Results & Insights

{{< figure src="fig3.png" caption="Spectral efficiency (bits/sec/Hz/UE) plotted against transmit power (dBm) for different numbers of active RF chains." >}}
This figure demonstrates that increasing transmit power generally improves spectral efficiency, but the rate of improvement saturates as more RF chains are activated, highlighting the diminishing returns of additional chains.

{{< figure src="fig5.png" caption="Energy efficiency (bits/Joule/UE) plotted against the number of transmission streams (Ns)." >}}
This plot shows a clear trade-off between energy efficiency and the number of streams; higher energy efficiency is achieved with fewer streams, but the system can support more users or data rates at the cost of reduced EE.

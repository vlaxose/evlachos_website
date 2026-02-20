---
title: "Joint Localization and Channel Estimation for UAV-Assisted Millimeter Wave Communications"
date: 2020-01-01
doi: "10.1109/ieeeconf51394.2020.9443514"
publishDate: 2020-01-01
authors: ['Alexandropoulos, G.', 'Vlachos, E.', 'Smida, B.']
publication_types: ["1"]
abstract: "In this paper, we consider millimeter Wave (mmWave) communications between an Unmanned Aerial Ve- hicle (UA V) and a base station. By assuming that both com- munication nodes are equipped with arrays of multiple antenna elements, we focus on the joint estimation of the UA V position and the Multiple Input Multiple Output (MIMO) channel coefﬁcients. Capitalizing on the line-of-sight signal propagation conditions and the beamspace representation of the wireless channel, we ﬁrst estimate the UA V position. Using this estimation, we then present a matrix completion formulation for the recovery of the remaining non-line-of-sight components of the MIMO channel matrix, which is efﬁciently solved via the alternating direction method of multipliers. Selected simulation results for a 28GHz channel model verify that the proposed scheme is beneﬁcial both in terms of estimation accuracy and resources utilization."
featured: false
url_pdf: "paper.pdf"
publication: "*2020 54th Asilomar Conference on Signals, Systems, and Computers*"
tags: ["Research", "6G", "UAVs"]
---

## Key Contributions
- Exploiting the line-of-sight (LOS) propagation conditions and beamspace representation of the wireless channel to estimate the UAV position.
- Utilizing the estimated UAV position to formulate a matrix completion-based approach for recovering the non-line-of-sight (NLOS) components of the MIMO channel.
- Demonstrating superior performance compared to baseline methods, requiring fewer channel training resources.

## Results & Insights

{{< figure src="fig1.png" caption="NMSE performance of the proposed LOS channel estimation technique versus baseline methods." >}}
The proposed method achieves significantly lower estimation error for the line-of-sight channel component across various scenarios, highlighting its effectiveness in leveraging UAV position information.

{{< figure src="fig2.png" caption="NMSE performance of the proposed method as a function of the number of channel training transmits." >}}
The results demonstrate that the proposed approach maintains low estimation error even with reduced channel training resources, offering a more efficient solution for joint localization and channel estimation in UAV-assisted mmWave systems.

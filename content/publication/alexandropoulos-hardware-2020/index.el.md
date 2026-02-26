---
title: "A Hardware Architecture For Reconfigurable Intelligent Surfaces with Minimal Active Elements for Explicit Channel Estimation"
date: 2020-01-01
doi: "10.1109/icassp40776.2020.9053976"
url_arxiv: "https://arxiv.org/abs/2002.10371"
publishDate: 2020-01-01
authors: ['Alexandropoulos, G. C.', 'Vlachos, E.']
publication_types: ["1"]
abstract: "Intelligent surfaces comprising of cost effective, nearly pas- sive, and reconﬁgurable unit elements are lately gaining in- creasing interest due to their potential in enabling fully pro- grammable wireless environments. They are envisioned to offer environmental intelligence for diverse communication objectives, when coated on various objects of the deployment area of interest. To achieve this overarching goal, the chan- nels where the Reconﬁgurable Intelligent Surfaces (RISs) are involved need to be in principle estimated. However, this is a challenging task with the currently available hardware RIS ar- chitectures requiring lengthy training periods among the net- work nodes utilizing RIS-assisted wireless communication. In this paper, we present a novel RIS architecture comprising of any number of passive reﬂecting elements, a simple con- troller for their adjustable conﬁguration, and a single Radio Frequency (RF) chain for baseband measurements. Capitaliz- ing on this architecture and assuming sparse wireless channels in the beamspace domain, we present an alternating optimiza- tion approach for explicit estimation of the channel gains at the RIS elements attached to the single RF chain. Represen- tative simulation results demonstrate the channel estimation accuracy and achievable end-to-end performance for various training lengths and numbers of reﬂecting unit elements."
featured: true
url_pdf: "paper.pdf"
publication: "*ICASSP 2020 - 2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*"
tags: ["Research", "6G", "UAVs"]
---

## Key Contributions
- Introduces a novel hardware architecture for reconfigurable intelligent surfaces (RISs) with minimal active elements, utilizing a single RF chain for baseband measurements.
- Proposes an alternating optimization approach for explicit channel estimation in the beamspace domain, leveraging the sparsity of wireless channels.
- Demonstrates that the proposed architecture enables efficient online RIS configuration for specific environments through reduced training periods.

## Results & Insights

The figure shows that the proposed technique achieves superior channel estimation accuracy with fewer training symbols compared to OMP and LS methods, highlighting its efficiency.

The results indicate that while the system achieves a rate of 8.5bps/Hz with perfect channel knowledge, the channel estimation process with T=200 training symbols results in a rate of approximately 7.6bps/Hz, demonstrating a trade-off between estimation accuracy and achievable rate.

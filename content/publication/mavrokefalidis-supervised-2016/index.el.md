---
title: "Supervised energy disaggregation using dictionary-based modelling of appliance states"
date: 2016-01-01
doi: "10.1109/isgteurope.2016.7856277"
publishDate: 2016-01-01
authors: ['Mavrokefalidis, C.', 'Ampeliotis, D.', 'Vlachos, E.', 'Berberidis, K.', 'Varvarigos, E.']
publication_types: ["1"]
abstract: "In this paper , a supervised energy disaggregation method is proposed. The appliances that are monitored, are modelled by multi-state ﬁnite state machines. Each state of an appliance is described by exactly one vector of power consumptions from a carefully designed set of such vectors (called atoms), that comprise a dictionary. The latter is constructed during a training phase, where it is assumed that individual power consumption signals are available. A clustering algorithm is applied on overlapping patches extracted from the training signals to select a ﬁxed number of representatives, i.e., the atoms of the dictionary. Moreover , in the training phase, an appropriate state transition probabilities matrix is constructed. During the operation phase, where the actual disaggregation task is performed, a trellis, with a reduced number of transitions, is used for the acquisition of the disaggregated power consumption signals per appliance. Numerical results, using the REDD dataset, are provided, in order to demonstrate the effectiveness of the proposed method. I."
featured: false
url_pdf: "paper.pdf"
publication: "*2016 IEEE PES Innovative Smart Grid Technologies Conference Europe (ISGT-Europe)*"
tags: ["Research", "6G", "UAVs"]
---

## Key Contributions
- Proposed a supervised energy disaggregation method using multi-state finite state machines to model appliance behavior.
- Introduced a dictionary-based approach where appliance states are represented by power consumption vectors selected via clustering from training data.
- Utilized state transition probabilities and a reduced trellis structure to efficiently perform disaggregation during operation.

## Results & Insights
The NMSE performance improves with an increasing number of appliances, demonstrating the method's scalability and effectiveness on real-world data.

The proposed method achieves lower NMSE compared to existing approaches, highlighting its superior accuracy in energy disaggregation.

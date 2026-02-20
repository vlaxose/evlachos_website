---
title: "Adaptive completion of the correlation matrix in wireless sensor networks"
date: 2016-01-01
doi: "10.1109/eusipco.2016.7760479"
publishDate: 2016-01-01
authors: ['Vlachos, E.', 'Berberidis, K.']
publication_types: ["1"]
abstract: "The correlation structure among the sensor observa- tions is a signiﬁcant characteristic of the wireless sensor network (WSN) which can be exploited to drastically enhance the overall network performance. This structure is usually expressed as a low-rank approximation of the correlation matrix, although, in many cases the correlation of the captured data is full- rank. Thus, the computation of the full-rank correlation matrix by centralizing all the measurements into one node, puts at risk the privacy of the WSN. To overcome this problem, we impose privacy-preserving restrictions, in order to constrain the cooperation among the nodes, and hence promote the privacy. To this end, the decentralized estimation of the network-wide corre- lation matrix is obtained via a novel adaptive matrix completion technique, where at each step, a rank-one completion problem is solved. Through simulation experiments it has been veriﬁed that proposed algorithm converges to the full rank correlation matrix. Moreover, the proposed algorithm exhibits signiﬁcantly lower computational complexity than the conventional technique. I."
featured: false
url_pdf: "paper.pdf"
publication: "*24th European Signal Processing Conference (EUSIPCO)*"
tags: ["Research", "6G", "UAVs"]
---

## Key Contributions
- Development of a privacy-preserving framework for decentralized correlation matrix estimation in wireless sensor networks.
- Proposal of a novel adaptive rank-one matrix completion technique to handle the constrained cooperation between sensor nodes.
- Demonstration of significantly faster convergence and lower computational complexity compared to traditional singular value thresholding (SVT) methods.

{{< figure src="fig1.png" caption="Convergence of the proposed algorithm showing the estimation error decreasing rapidly over iterations, reaching the ground-truth value after a small number of steps, while the SVT-based method converges much slower." >}}

The results demonstrate that the proposed adaptive completion technique achieves rapid convergence to the true correlation matrix with substantially lower computational overhead, making it particularly suitable for resource-constrained wireless sensor networks with privacy constraints.

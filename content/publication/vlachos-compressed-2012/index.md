---
title: "Compressed Sensing Techniques for Decision Feedback Equalization of Sparse Wireless Channels"
date: 2012-01-01
doi: "10.1109/vetecs.2012.6240285"
publishDate: 2012-01-01
authors: ['Vlachos, E.', 'Lalos, A.', 'Lionas, G.', 'Berberidis, K.']
publication_types: ["1"]
abstract: "In this paper new efﬁcient decision feedback equal- ization (DFE) schemes for channels with long and sparse im- pulse responses are proposed. It has been shown that under reasonable assumptions concerning the channel impulse response (CIR) coefﬁcients, the feedforward (FF) and feedback (FB) ﬁlters may be also approximated by sparse ﬁlters. Either the sparsity of the CIR, or the sparsity of the DFE ﬁlters may be exploited to derive efﬁcient implementations of the DFE. To this end, compressed sampling (CS) approaches, already successful in system identiﬁcation settings, can signiﬁcantly improve the performance of the non sparsity aware DFE. Building on basis pursuit and matching pursuit techniques new DFE schemes are proposed that exhibit considerable computational savings, increased performance properties and short training sequence requirements. To investigate the performance of the proposed schemes the restricted isometry property in the common DFE setup is also investigated. I. I NTRODUCTION In high-speed wireless communications, the involved multi- path channels are typically sparse, i.e."
featured: false
url_pdf: "paper.pdf"
publication: "*IEEE 75th Vehicular Technology Conference (VTC Spring)*"
tags: ["Research", "6G", "UAVs"]
---

## Key Contributions
- Development of compressed sensing-based decision feedback equalization (DFE) schemes for sparse wireless channels.
- Exploitation of channel sparsity to improve the performance of non-sparsity-aware DFE.
- Proposing new DFE implementations using basis pursuit and matching pursuit techniques.

## Results & Insights

{{< figure src="fig1.png" caption="Performance comparison of indirect DFE techniques under different SNR conditions." >}}
The results show that the proposed compressed sensing-based DFE schemes outperform traditional methods, especially at higher SNR levels.

{{< figure src="fig2.png" caption="SER performance of direct equalization schemes as a function of training sequence length." >}}
The SER performance improves with longer training sequences, indicating the importance of training for accurate channel estimation.

{{< figure src="fig3.png" caption="SER performance of DFE schemes across different SNR values." >}}
The proposed CS-based DFE schemes demonstrate superior performance across all tested SNR levels, confirming their effectiveness.

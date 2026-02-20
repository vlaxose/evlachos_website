---
title: "Massive MIMO Channel Estimation for Millimeter Wave Systems via Matrix Completion"
date: 2018-01-01
doi: "10.1109/lsp.2018.2870533"
url_arxiv: "https://arxiv.org/abs/1809.01603"
publishDate: 2018-01-01
authors: ['Vlachos, E.', 'Alexandropoulos, George C.', 'Thompson, J.']
publication_types: ["2"]
abstract: "Millimeter wave (mmWave) massive multiple input multiple output (MIMO) systems realizing directive beamforming require reliable estimation of the wireless propagation channel. However, mmWave channels are characterized by high variability that severely challenges their recovery over short training periods. Current channel estimation techniques exploit either the channel sparsity in the beamspace domain or its low-rank property in the antenna domain, nevertheless, they still require large numbers of training symbols for the satisfactory performance. In this letter, we present a novel channel estimation algorithm that jointly exploits the latter two properties of mmWave channels to provide more accurate recovery, especially for shorter training intervals. The proposed iterative algorithm is based on the alternating direction method of multipliers and provides the global optimum solution to the considered convex mmWave channel estimation problem with fast convergence properties. Index T erms —Alternating direction method of multiplier (ADMM), beamforming, channel estimation, massive multiple in- put multiple output (MIMO), matrix completion, millimeter wave. I."
featured: false
url_pdf: "paper.pdf"
publication: "*IEEE Signal Processing Letters*"
tags: ["Research", "6G", "UAVs"]
---

## Key Contributions
- Proposes a novel channel estimation algorithm for mmWave massive MIMO systems that jointly exploits both channel sparsity and low-rank properties via matrix completion.
- Introduces an ADMM-based iterative optimization approach that converges quickly even for very small training lengths.
- Demonstrates superior performance compared to state-of-the-art techniques, achieving better accuracy with significantly shorter training periods.
- Enables reliable channel recovery in mmWave systems, which are characterized by high variability and challenging conditions.

## Results & Insights

This figure clearly demonstrates the superior performance of the proposed technique across all training lengths, with the proposed method consistently achieving better accuracy than existing methods like SVT and VAMP, even at the smallest training lengths.

The proposed algorithm converges faster and achieves lower NMSE for all training lengths, indicating its efficiency and effectiveness in channel estimation.

This result highlights the proposed technique's ability to maintain good performance even with very short training sequences, outperforming other methods significantly for all considered training lengths.

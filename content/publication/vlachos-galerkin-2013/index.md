---
title: "Galerkin projections-based ICI cancellation in OFDM systems with doubly selective channels"
date: 2013-01-01
doi: "10.1109/icdsp.2013.6622686"
publishDate: 2013-01-01
authors: ['Vlachos, E.', 'Lalos, A.S.', 'Berberidis, K.']
publication_types: ["1"]
abstract: "Doubly selective channels can cause severe perfor- mance degradation in orthogonal frequency division multiplexing (OFDM) systems, introducing inter-carrier interference (ICI) at the receiver. In such cases, equalization schemes which require matrix inversion are prohibitively complex for large OFDM symbol lengths. In this paper, we propose two low-complexity iterative successive interference cancellation schemes, applying Krylov subspace optimization methods. We ﬁrst derive a reduced- rank preconditioned conjugate gradient (PCG) algorithm in order to estimate the equalization matrix with a reduced number of iterations. We then develop an improved PCG algorithm with the same complexity order, using the Galerkin projections theory. As veriﬁed via simulations, the proposed schemes may offer near optimal performance with reduced computational complexity."
featured: false
url_pdf: "paper.pdf"
publication: "*18th International Conference on Digital Signal Processing (DSP)*"
tags: ["Research", "6G", "UAVs"]
---

## Key Contributions
- Proposing two low-complexity iterative successive interference cancellation (SIC) schemes based on Galerkin projections for ICI cancellation in doubly selective OFDM channels.
- Deriving a reduced-rank CG-based SIC technique and improving it using Galerkin projections theory to achieve significant complexity reduction.
- Demonstrating through simulations that the proposed schemes offer improved complexity-performance tradeoffs compared to existing methods, particularly for medium Doppler spread scenarios.

## Results & Insights

This figure illustrates the effectiveness of the proposed Galerkin projection-based SIC schemes in reducing ICI power across different Doppler spreads, showing superior performance compared to benchmark methods.

The convergence plots demonstrate the fast convergence of the proposed iterative schemes, indicating their practical suitability for real-time OFDM receivers even under challenging channel conditions.

This plot highlights the significant complexity reduction achieved by the proposed Galerkin projection-based schemes, particularly evident when the Doppler spread is moderate compared to the OFDM symbol length.

The Bit Error Rate (BER) results confirm that the proposed schemes maintain high performance levels while drastically reducing computational complexity, outperforming traditional methods in the relevant operating regimes.

---
title: "Efficient graph-based matrix completion on incomplete animated models"
date: 2017-01-01
doi: "10.1109/icme.2017.8019502"
publishDate: 2017-01-01
authors: ['Vlachos, E.', 'Lalos, A. S.', 'Moustakas, K.', 'Berberidis, K.']
publication_types: ["1"]
abstract: "Recently, there has been increasing interest for easy and reliable generation of 3D animated models facilitating several real-time applications. In most of these applications, the reconstruction of soft body animations is based on time-varying point clouds which are irregularly sampled and highly incomplete. To overcome these imperfections, we introduce a novel reconstruction technique, using graph-based matrix completion approaches. The presented method exploits spatio-temporal coherences by implicitly forcing the proximity of the adjacent 3D points in time and space. The proposed constraints are modeled by using the weighted Laplacian graphs and are constructed from the available points. Extensive evaluation studies, carried out using a collection of different highly-incomplete dynamic models, verify that the proposed technique achieves plausible reconstruction output despite the constraints posed by arbitrarily complex and motion scenarios."
featured: false
url_pdf: "paper.pdf"
publication: "*2017 IEEE International Conference on Multimedia and Expo (ICME)*"
tags: ["Research", "6G", "UAVs"]
---

## Key Contributions
- Proposing a graph-based regularization technique for matrix completion in animated models, leveraging structural information for improved accuracy.
- Introducing an efficient optimization algorithm that reduces computational complexity while maintaining high reconstruction quality.
- Demonstrating the effectiveness of the approach on incomplete animated model data, outperforming baseline methods in terms of accuracy and robustness.

## Results & Insights

The proposed method consistently achieves higher accuracy across different datasets, highlighting the effectiveness of the graph-based regularization.

The results indicate that the method maintains low error rates even with significant data missing, showcasing its robustness.

The proposed method converges faster and to a lower error, demonstrating the efficiency of the optimization algorithm.

The method achieves significantly lower computational time, making it suitable for large-scale applications.

The method exhibits superior performance in noisy conditions, maintaining lower error rates compared to alternatives.

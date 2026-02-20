---
title: "Energy Efficient Transmission of 3D Meshes Over MMWave-Based Massive MIMO Systems"
date: 2019-01-01
doi: "10.1109/icme.2019.00295"
publishDate: 2019-01-01
authors: ['Lalos, A.', 'Arvanitis, G.', 'Vlachos, E.', 'Moustakas, K.']
publication_types: ["1"]
abstract: "Many mixed reality applications are b ased on the real-time compression and streaming of three-dimensional (3D) mod­ els. Thus, they demand very high- bandwidth and ultra-low latency from network specifications. The next-generation wireless networks will employ promising technologies to sig­ nificantly improve the communication data rates. However, due to implementation complexity and thus increased en­ ergy consumption of these technologies, a trade-off between the quality-of-use r-experience (QoE) and the hardware spec­ ifications is necessary. To overcome these limitations low- resolution quantizers have been of inte rest, which provide a trade-off between quality and complexity. In this p aper, we propose a complexity-aware perceptual coding scheme that minimizes the reconstruction losses of the 3D models. Ex­ tensive simulations assuming different 3D models show that the proposed scheme achieves plausible reconstruction output offering significantly higher energy efficiency gains, as com­ pared to a context unaware coding approaches."
featured: false
url_pdf: "paper.pdf"
publication: "*2019 IEEE International Conference on Multimedia and Expo (ICME)*"
tags: ["Research", "6G", "UAVs"]
---

## Key Contributions
- Proposes a complexity-aware perceptual coding scheme for 3D meshes that minimizes reconstruction losses while considering hardware limitations.
- Introduces an optimal bit allocation strategy that assigns different quantization resolutions to different levels of detail in the 3D mesh.
- Demonstrates significant energy efficiency gains and improved reconstruction quality compared to uniform transmission approaches.

{{< figure src="fig2.png" caption="Reconstruction quality comparison between uniform transmission and the proposed bit allocation approach for different 3D meshes and bit-per-vertex values." >}}
This figure shows that the proposed scheme provides superior reconstruction quality, particularly at lower bit rates, by adaptively allocating bits based on perceptual importance.

{{< figure src="fig3.png" caption="Comparison of uniform bit allocation versus optimized bit allocation for 3D mesh transmission." >}}
The optimized bit allocation strategy significantly outperforms the uniform approach in terms of reconstruction quality, demonstrating the effectiveness of assigning different bit rates to different mesh details.

{{< figure src="fig4.png" caption="Performance (metric 6) versus total power consumption for different transmission approaches." >}}
The results indicate that the proposed scheme achieves substantially better reconstruction quality at lower power levels, highlighting its energy efficiency benefits.

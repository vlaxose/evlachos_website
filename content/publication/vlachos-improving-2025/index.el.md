---
title: "Improving Wideband Massive MIMO Channel Estimation With UAV State-Space Information"
date: 2025-01-01
doi: "10.1109/tvt.2025.3569350"
publishDate: 2025-01-01
authors: ['Vlachos, Evangelos', 'Mavrokefalidis, Christos', 'Berberidis, Kostas', 'Alexandropoulos, George C.']
publication_types: ["2"]
abstract: "In this paper, we focus on the estimation of massive Multiple-Input Multiple-Output (mMIMO) channels in high-frequency point-to-point wireless communications between a terrestrial multi-antenna base station, realizing fully digital beamforming, and a multi-antenna Unmanned Aerial Vehicle (UA V), capable of only analog combining via a single reception Radio-Frequency (RF) chain. A wideband channel model, incorporating selectivity which is usually referred to as beam squint and is particularly relevant in high frequency bands, such as millimeter waves and terahertz, is considered. To account for the UA V’s limited capability to collect long training sequences, due to its single-RF reception architecture, and the beam-squint effect at both communication ends, we present a novel channel estimation approach that exploits information provided by the control module of the UA V , namely its state-space vector. The proposed approach comprises a hybrid parametric and non-parametric estimation op- timization framework that is efﬁciently solved through an iterative algorithm using the alternating direction method of multipliers. Our extensive performance investigations, including comparisons with benchmark schemes, showcase that considerable gains can be achieved if state-space information from the UA V’s control module is appropriately incorporated in the channel estimation process."
featured: false
url_pdf: "paper.pdf"
publication: "*IEEE Transactions on Vehicular Technology*"
tags: ["Research", "6G", "UAVs"]
---

## Key Contributions
- Development of a wideband channel model incorporating beam squint effects relevant for high-frequency mMIMO-UAV communications.
- Proposal of a state-assisted mMIMO channel estimation approach that leverages UAV motion information to improve estimation accuracy.
- Design of an efficient estimation algorithm suitable for single-RF chain architectures, minimizing training overhead.
- Demonstration via simulations that the proposed technique achieves high estimation accuracy with significantly reduced training data requirements.

## Results & Insights

{{< figure src="fig2.png" caption="Comparison of channel estimation performance between the proposed state-assisted method and benchmark schemes across different UAV velocities." >}}
The proposed estimator outperforms benchmark methods, particularly at higher UAV speeds, highlighting the effectiveness of incorporating state-space information for accurate channel estimation.

{{< figure src="fig4.png" caption="Performance of the proposed estimator in tracking channel variations within the coherence time of consecutive OFDM symbols." >}}
The estimator maintains low error levels even when tracking rapid channel changes, demonstrating its suitability for high-frequency, time-sensitive mMIMO-UAV communications.

{{< figure src="fig5.png" caption="Convergence behaviour of the proposed Algorithm 1 for estimating the channel state under different initialization conditions." >}}
Algorithm 1 exhibits rapid convergence with stable performance across various initialization scenarios, indicating its robustness and practical applicability for real-time channel estimation.

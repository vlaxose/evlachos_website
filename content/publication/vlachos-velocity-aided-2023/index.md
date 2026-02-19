---
title: "Velocity-aided Channel Estimation for Spatially Selective mmWave Massive MIMO Communications"
date: 2023-01-01
doi: "10.23919/eusipco58844.2023.10289899"
publishDate: 2023-01-01
authors: ['Vlachos, E.', 'Mavrokefalidis, C.', 'Berberidis, K.']
publication_types: ["1"]
abstract: "This paper focuses on addressing the challenge of estimating multiple-input multiple-output (MIMO) channels for wireless communication between a ground base-station and a moving vehicle. One recently recognised model for time-varying channels incorporates spatial selectivity, which is referred to as beam squint, and is particularly relevant in the millimeter-wave (mmWave) range. In such scenarios, it is essential to account for the beam squint when attempting to recover channel parameters using a training sequence. However, the use of a training sequence alone may be insufficient for this purpose. To overcome this issue, in this work, we propose a channel estimation approach that exploits information provided by the control module of the vehicle, namely its velocity. The estimation problem that is designed, regards the channel both in a parametric and a non-parametric form and the alternating direction method of multipliers is utilised to efficiently solve it. It is demonstrated via simulations that considerable gains can be achieved if information from the control unit of the vehicle can be appropriately introduced and exploited."
featured: false
url_pdf: "paper.pdf"
publication: "*31st European Signal Processing Conference (EUSIPCO)*"
tags: ["Research", "6G", "UAVs"]
---

## Key Contributions
- Addresses the challenge of channel estimation in time-varying mmWave massive MIMO channels for moving UAVs, where conventional training-based methods fail due to beam squint and channel dynamics.
- Proposes a novel channel estimation technique that leverages the UAV's velocity information, obtained from its control module, to compensate for the beam squint effect and improve parameter recovery.
- Introduces a time-varying channel model specifically designed for mmWave frequencies that incorporates the spatial selectivity (beam squint) effect, enabling more accurate and robust channel state information (CSI) estimation.
- Demonstrates the effectiveness of the proposed method in providing reliable channel estimates even with short training sequences, essential for real-time UAV communications.

## Results & Insights
This figure shows that the proposed velocity-aided method significantly outperforms conventional training-based approaches in terms of channel estimation accuracy (lower NMSE), especially at higher UAV velocities and moderate to high SNR levels, validating the effectiveness of incorporating velocity information.

The results indicate that the proposed method achieves lower BER for higher data rates and faster UAV speeds compared to baseline methods, demonstrating its practical benefit for reliable mmWave massive MIMO communication with moving platforms.

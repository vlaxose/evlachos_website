---
title: "Consistency-Gated Cooperative Localization for UAV Swarms Under Intermittent GPS"
date: 2026-05-11
publishDate: 2026-05-11
authors: ['Venetis, D.', 'Vlachos, E.', 'Berberidis, K.']
publication_types: ["1"]
abstract: "Cooperative localization under intermittent Global Navigation Satellite System (GNSS) is challenging, as naive cooperation may degrade estimation when relative measurements are inconsistent. This paper proposes a two-stage localization framework for Unmanned Aerial Vehicle (UAV) swarms, where each agent maintains a local Extended Kalman Filter (EKF) estimate using Global Positioning System (GPS) and Inertial Measuring Unit (IMU) data, and applies a distributed refinement based on relative Ultra-Wideband (UWB) range and Angle of Arrival (AoA) direction constraints. Moreover, a lightweight consistency gate is proposed, which relies on residual and consensus indicators and determines whether cooperative refinement is accepted, preventing harmful updates without online ground truth. Simulation results demonstrate consistent improvements in formation-relevant relative accuracy and stable absolute positioning compared to GPS and GPS+EKF baselines under intermittent GPS availability."
featured: false
url_pdf: "paper.pdf"
publication: "*34th European Signal Processing Conference (EUSIPCO 2026)*"
tags: ["Research", "UAVs", "Cooperative Localization", "GPS", "EKF", "ADMM", "UWB", "AoA"]
---

## Key Contributions

- **Consistency-gated framework**: A cooperative localization scheme that actively prevents harmful cooperative updates when inter-agent measurements are inconsistent under intermittent GPS.
- **Two-stage estimation**: Decoupled architecture separating local observability recovery (EKF with GPS/IMU) from cooperative refinement (distributed ADMM over UWB range and AoA constraints).
- **Lightweight acceptance gate**: A learning-based gate driven solely by runtime residual and consensus indicators — no ground truth required online.
- **Quantitative gains**: Demonstrated moderate improvements in absolute accuracy and substantial gains in formation-relevant relative accuracy over GPS/IMU baselines.

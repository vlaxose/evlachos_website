---
title: "Sensing-Aided Channel Estimation for THz XL-MIMO ISAC Systems"
date: 2026-06-01
publishDate: 2026-06-01
authors: ['Vlachos, E.', 'Alexandropoulos, G. C.']
publication_types: ["2"]
abstract: "Terahertz (THz) extremely large (XL) multiple-input multiple-output (MIMO) systems are a cornerstone of 6G integrated sensing and communication (ISAC), combining terabit-per-second data rates with centimeter-accurate environment sensing. In the THz band, single-carrier waveforms are preferred due to their robustness against power-amplifier nonlinearity and phase noise. However, the ultra-wide THz bandwidth induces dual-wideband fading, combining spatial wideband effects (beam squint coupling angle and delay across both end arrays) with temporal wideband effects (multipath delay spread), creating a channel estimation problem that existing methods designed for orthogonal frequency-division multiplexing (OFDM) do not address in the single-carrier setting. We propose a sensing-aided time-domain channel estimation framework for fixed THz links in which a coarse position estimate, obtained at the ISAC base station from a brief uplink sounding exchange, warm-starts a biconvex alternating optimization problem that jointly recovers the channel matrix and the multipath delay-support vector. Then, the recovered delay profile is fed back as a sensing output, closing the ISAC loop. Extensive simulations demonstrate that the proposed approach exhibits significantly lower normalized mean-square error than on-grid beamspace methods, provides a substantial advantage over oracle least-squares in the underdetermined regime, achieves exact delay-support recovery beyond a pilot-length threshold, and yields superior effective spectral efficiency across all training lengths."
featured: false
draft: true
publication: "*In preparation for IEEE Open Journal of the Communications Society*"
tags: ["Research", "ISAC", "THz", "XL-MIMO", "Channel Estimation", "ADMM", "6G"]
---

## Key Contributions

- **Sensing-aided warm start**: A coarse position estimate from a brief uplink ISAC sounding exchange warm-starts a biconvex alternating optimization that jointly recovers the channel matrix and the multipath delay-support vector for fixed THz links.
- **Dual-wideband fading model**: A unified time-domain framework that handles both spatial wideband effects (beam squint coupling angle and delay across transmit and receive arrays) and temporal wideband effects (multipath delay spread) for single-carrier THz XL-MIMO, closing a gap left by OFDM-oriented methods.
- **Closing the ISAC loop**: The recovered delay profile is fed back as a sensing output, and simulations show significantly lower NMSE than on-grid beamspace methods, exact delay-support recovery beyond a pilot-length threshold, and superior effective spectral efficiency across training lengths.

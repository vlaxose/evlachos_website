---
title: "Channel Estimation for mmWave and THz Massive MIMO"
short_title: "mmWave/THz channel estimation"
summary: "Our research on channel estimation for mmWave and THz massive MIMO: hybrid beamforming with low-resolution ADCs, UAV and vehicle links, THz XL-MIMO, RIS and quantum computing."
type: project
date: 2026-10-19
lastmod: 2026-10-19
tags:
- Channel Estimation
- mmWave
- THz
- Massive MIMO
- Hybrid Beamforming
- ISAC
- UAVs
---

Channel estimation is how a receiver learns the paths a radio signal has travelled: their directions, delays and strengths. At millimeter-wave (mmWave) and terahertz (THz) frequencies, where 5G and 6G networks find wide bandwidth, signals fade quickly and large antenna arrays must focus their energy into narrow beams. A beam can only be pointed at a channel that has been estimated well, so channel estimation decides how much of the promised bandwidth is actually usable. We have worked on this problem since 2018: for massive MIMO base stations, low-cost receivers, moving drones, extremely large THz arrays and, more recently, quantum computers.

## Why channel estimation is hard at mmWave and THz

- **Cheap hardware hides the signal.** Large arrays are affordable only with hybrid analog/digital beamforming, few radio-frequency (RF) chains and low-resolution analog-to-digital converters (ADCs), so the receiver sees a compressed and coarsely quantized version of the channel.
- **There is little time.** The channel changes quickly, especially for vehicles and UAVs, so only short training sequences can be afforded.
- **Wide bandwidth bends the beam.** Over a very wide band the beam direction drifts with frequency (beam squint) and echoes spread over many symbols. At THz both effects appear together, which is called dual-wideband fading.

## Sparse and low-rank channel estimation from short training

mmWave channels have only a few strong paths, so the channel matrix is sparse in the beamspace and has low rank. We exploit both properties at once, through matrix completion and the alternating direction method of multipliers (ADMM), to recover the channel from far shorter training than either property alone allows ([IEEE SPL 2018]({{< relref "/publication/vlachos-massive-2018" >}})). For wideband hybrid receivers we introduced a random spatial sampling stage in the analog combiner, so that a few RF chains capture enough of the channel to recover it ([IEEE JSTSP 2019]({{< relref "/publication/vlachos-wideband-2019" >}}), [SPAWC 2019]({{< relref "/publication/vlachos-hybrid-2019" >}})), and we extended the method to track the channel as it changes over time ([ICASSP 2020]({{< relref "/publication/alexandropoulos-wideband-2020" >}})).

## Hybrid beamforming receivers with low-resolution ADCs

Few-bit ADCs turn the received signal into a staircase. We add small random signals (dither) to the analog beamformer and to the ADCs, so that quantization becomes informative rather than destructive, and recover the channel with an expectation-maximization estimator that performs close to an oracle least-squares estimator ([ICASSP 2018]({{< relref "/publication/vlachos-dithered-2018" >}})). For few-bit receivers we also developed a message-passing estimator that needs no prior knowledge of the channel statistics ([EUSIPCO 2018]({{< relref "/publication/kaushik-efficient-2018" >}})). With colleagues at Queen's University Belfast we studied a two-stage Rotman lens beamformer, which gives high antenna gain without a beam-selection network, and designed a robust estimator for it under low-resolution sampling ([SPAWC 2019]({{< relref "/publication/vlachos-robust-2019" >}}), [ICC 2023 Workshops]({{< relref "/publication/vlachos-millimeter-2023" >}})).

## Channels of moving UAVs and vehicles

A drone or a car already knows where it is and how fast it moves. We feed this information from the control system into the channel estimator. For a UAV link we first estimate the UAV position from the line-of-sight path and then complete the rest of the channel ([Asilomar 2020]({{< relref "/publication/alexandropoulos-joint-2020" >}})). The vehicle's velocity reduces the training needed under beam squint ([EUSIPCO 2023]({{< relref "/publication/vlachos-velocity-aided-2023" >}})), and for a UAV with a single RF chain the state estimate from its flight controller makes the wideband channel recoverable from short training ([IEEE TVT 2025]({{< relref "/publication/vlachos-improving-2025" >}})).

{{< figure src="uav-flights.png" alt="Three UAV test flight paths around a base station, and the UAV position estimation error over time" caption="Test flights around a base station (top) and the error of the UAV's own position estimate (bottom), the side information our estimator uses. From IEEE TVT 2025." >}}

## THz XL-MIMO: dual-wideband fading and sensing-aided estimation

At THz, extremely large arrays (XL-MIMO) with hundreds of antennas face beam squint and inter-symbol interference at the same time. We model both in the time domain for single-carrier transmission, with a mixed-integer biconvex formulation that handles arbitrary delay patterns ([EUSIPCO 2025]({{< relref "/publication/vlachos-biconvex-2025" >}})). In an integrated sensing and communication (ISAC) system the base station's own radar output gives the estimator a head start: a biconvex ADMM algorithm warm-started by the radar jointly recovers the channel matrix and the delay support, and returns the delay profile as a sensing output at no extra pilot cost ([ISAC 2026]({{< relref "/publication/vlachos-sensing-thz-xlmimo-2026" >}})).

## Channel estimation with reconfigurable intelligent surfaces

A reconfigurable intelligent surface (RIS) can shape the propagation environment, but the channels through it must be estimated first, and a fully passive surface cannot observe them. We proposed an RIS hardware architecture with a minimal number of active elements that makes explicit channel estimation possible ([ICASSP 2020]({{< relref "/publication/alexandropoulos-hardware-2020" >}})), and a protocol for receiving RISs that estimate the channels of two multi-antenna terminals from non-orthogonal pilots, again exploiting beamspace sparsity and low rank ([Springer book chapter, 2026]({{< relref "/publication/alexandropoulos-receiving-2025" >}})).

## Quantum computing for channel estimation

Many channel estimators reduce to solving a large system of linear equations, a task where quantum algorithms promise large speed-ups. With Kostas Blekos we studied how quantum linear-system solvers could assist mmWave massive MIMO receivers, and how the amplitude encoding of the quantum state relates to recovering the channel ([VLSI-SoC 2022]({{< relref "/publication/vlachos-quantum-2022" >}})).

## Current directions

- Closing the loop between sensing and communication, so that each channel estimate improves the next sensing step and the sensing output improves the next estimate.
- Near-field (spherical-wave) propagation for XL-MIMO arrays, where the far-field model behind most estimators stops holding.
- Joint design of UAV motion and beam alignment, so that the flight path itself keeps the channel easy to estimate.

## Collaborators

George C. Alexandropoulos, John S. Thompson, Aryan Kaushik, Christos Mavrokefalidis, Kostas Berberidis, Michail Matthaiou, Vincent F. Fusco, Muhammad Z. Shakir, Besma Smida, Konstantinos D. Katsanos and Kostas Blekos.

## Work with us

We offer diploma and MSc theses, internships and PhD co-supervision on these problems, at ISI, ATHENA RC and at the University of Patras. Students get a well-defined problem, working simulation code to start from and compute time on the ARIS national supercomputer, and they co-author what they publish. Open thesis and internship topics are listed on the [open topics]({{< relref "/research/open-topics" >}}) page. Researchers interested in joint papers or proposals are equally welcome. [Get in touch]({{< relref "/contact" >}}), and see the [research group]({{< relref "/group" >}}) page for who works with us today.

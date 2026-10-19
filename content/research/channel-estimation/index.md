---
title: "Channel Estimation for mmWave and THz Massive MIMO"
summary: "How we estimate wireless channels for millimeter-wave and terahertz massive MIMO: low-cost receivers, moving UAVs, 6G sensing and quantum computing."
type: project
date: 2026-10-19
tags:
- Channel Estimation
- mmWave
- THz
- Massive MIMO
- ISAC
- UAVs
---

Future wireless networks move to higher frequencies, millimeter waves (mmWave) and terahertz (THz), where there is plenty of bandwidth. Signals at these frequencies fade quickly, so base stations and devices need large antenna arrays that focus energy into narrow beams. To point a beam, the receiver must first know the wireless channel: the paths the signal takes, their angles and their delays. Finding them is called channel estimation, and it has been a core part of our research since 2018.

Three things make it hard at high frequencies:

- **Cheap hardware.** Large arrays are affordable only with few radio chains, analog beamformers and low-resolution converters, which hide much of the signal.
- **Little time.** The channel changes quickly, especially for moving vehicles and drones, so there is little time for training signals.
- **Wide bandwidth.** Over a very wide band the beam direction drifts with frequency (beam squint), and echoes spread out in time.

## Learning the channel from few measurements

mmWave channels have only a few strong paths. We use this structure, through sparse recovery and matrix completion, to recover the full channel from short training periods ([IEEE SPL 2018]({{< relref "/publication/vlachos-massive-2018" >}}), [IEEE JSTSP 2019]({{< relref "/publication/vlachos-wideband-2019" >}}), [SPAWC 2019]({{< relref "/publication/vlachos-hybrid-2019" >}})) and to track it over time ([ICASSP 2020]({{< relref "/publication/alexandropoulos-wideband-2020" >}})).

## Low-cost receivers

Cheap receivers quantize the signal with very few bits. We add small random signals to the analog beamformer and the converters to undo the staircase effect of quantization ([ICASSP 2018]({{< relref "/publication/vlachos-dithered-2018" >}})), use message passing for few-bit receivers ([EUSIPCO 2018]({{< relref "/publication/kaushik-efficient-2018" >}})), and design estimators for lens-based arrays that need no beam-selection network ([SPAWC 2019]({{< relref "/publication/vlachos-robust-2019" >}}), [ICC 2023 Workshops]({{< relref "/publication/vlachos-millimeter-2023" >}})).

## Using what the vehicle already knows

A moving car or drone already knows its speed and position from its control system. We feed this information into channel estimation, which reduces the training needed under beam squint ([EUSIPCO 2023]({{< relref "/publication/vlachos-velocity-aided-2023" >}})). For drones with a single radio chain, the UAV's state estimate makes the channel recoverable from short training ([IEEE TVT 2025]({{< relref "/publication/vlachos-improving-2025" >}})).

{{< figure src="uav-flights.png" caption="Test flights around a base station (top) and the error of the UAV's own position estimate (bottom), the side information our estimator uses. From IEEE TVT 2025." >}}

## THz bands and 6G sensing

At THz, beam squint and delay spread appear together, which is called dual-wideband fading. We model both in the time domain with biconvex optimization ([EUSIPCO 2025]({{< relref "/publication/vlachos-biconvex-2025" >}})), and we use the base station's own radar output to give the estimator a head start at no extra pilot cost ([ISAC 2026]({{< relref "/publication/vlachos-sensing-thz-xlmimo-2026" >}})). This ties channel estimation to integrated sensing and communication (ISAC).

## Quantum computing for channel estimation

Many channel estimators reduce to solving a large system of linear equations, a task where quantum algorithms promise large speed-ups. With Kostas Blekos we studied how quantum linear solvers could assist mmWave massive MIMO receivers, and how the quantum amplitude encoding relates to recovering the channel ([VLSI-SoC 2022]({{< relref "/publication/vlachos-quantum-2022" >}})).

## Collaborators

George C. Alexandropoulos, John Thompson, Aryan Kaushik, Christos Mavrokefalidis, Kostas Berberidis, Muhammad Z. Shakir and Kostas Blekos.

## Work with us

Students and researchers who want to work on channel estimation, ISAC or quantum-assisted signal processing are welcome to [get in touch]({{< relref "/contact" >}}). The [research group]({{< relref "/group" >}}) page shows who works with us today.

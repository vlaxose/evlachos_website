---
title: "Paper Submitted to ICASSP 2027"
date: 2026-09-23
summary: "We submitted a paper on distributed kinematic state and channel estimation for UAV swarms."
tags: ["publication", "research", "UAVs", "ISAC", "channel estimation", "belief propagation", "swarms"]
pub_type: "paper"
categories: ["paper"]
---

We submitted a new paper to the **2027 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP 2027)**:

### Links as Sensors: Distributed Kinematic State and Channel Estimation for UAV Swarms over Lossy Sidelinks
*Evangelos Vlachos*

Swarm control needs accurate kinematic states and channel estimates but onboard navigation can be poor and sidelinks are lossy. We treat state and channel estimation as one integrated sensing and communication problem so that pilot transmissions both probe channels and yield bearings to the base station, and inter-UAV radar provides relative positions and radial velocities while carrying messages in steerable beams. We apply Gaussian belief propagation to fuse these heterogeneous measurements across the swarm so that bearings from one base station help localize every vehicle, including those out of direct view. The estimated kinematic state then improves link estimation by steering pilots and constraining reflection geometry, and a motion model can replace lost messages under heavy packet loss.

Key contributions:
- **Integrated ISAC formulation**: combine pilot bearings and inter-UAV radar in a single estimation problem.
- **Distributed inference**: use Gaussian belief propagation to fuse measurements across a swarm with lossy sidelinks.
- **Robustness mechanisms**: steer pilots and use motion priors to reduce channel error and recover from packet loss.

This work was funded by the European Union under Horizon Europe Grant Agreement 101187121 ([EUSOME](/projects/eusome/)).

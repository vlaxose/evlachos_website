---
title: "Open Topics for Theses, Internships and PhDs"
short_title: "Open topics"
summary: "Open diploma, MSc and PhD thesis topics and internships on UAV networks, integrated sensing and communication, cooperative localization, safe control and drone detection at ISI, ATHENA RC."
type: project
date: 2026-10-19
lastmod: 2026-10-19
tags:
- Theses
- Internships
- UAVs
- ISAC
- Control
---

Our group works on the joint design of sensing, communication and control for UAV networks and 6G. The topics below are open now. Each starts from a published paper of ours, comes with working code to begin from, and is scoped to end in a result that can be published with you as a co-author. Diploma and MSc theses are offered with the University of Patras, PhD topics through co-supervision, and internships at ISI, ATHENA RC. Simulations run on the ARIS national supercomputer. Hardware topics use the drones, mmWave radar and Wi-Fi/Remote ID equipment of the [EUSOME]({{< relref "/projects/eusome" >}}) project.

## Sensing and estimation

### 1. Sensing-aided channel estimation for UAV mmWave links

*MSc or diploma thesis · simulation in Python or MATLAB*

A drone's flight controller already knows its position and velocity, and a base station with radar can sense the drone itself. Use both to cut the training a wideband mmWave link needs, starting from our estimator in [IEEE TVT 2025]({{< relref "/publication/vlachos-improving-2025" >}}) and the sensing-aided method of [ISAC 2026]({{< relref "/publication/vlachos-sensing-thz-xlmimo-2026" >}}). Deliverable: a simulator with beam squint and a comparison of pilot overhead against standard estimators.

### 2. Cooperative localization for UAV swarms over lossy links

*MSc thesis or PhD · estimation theory and simulation*

Drones in a swarm can locate each other from mutual range and bearing measurements when GPS is degraded, but links drop and some measurements are wrong. Starting from our consistency-gated method in [EUSIPCO 2026]({{< relref "/publication/venetis-consistency-2026" >}}), design estimators that stay consistent under packet loss and outliers, and test them on a simulated swarm in Gazebo/PX4.

## Communication and control

### 3. Connectivity-aware motion planning for UAV formations with directional links

*Diploma or MSc thesis · ROS 2, Gazebo/PX4*

mmWave links work only when the beams of both drones point at each other, so motion and communication cannot be planned separately. Building on our predictive control for connectivity in [NextGCom 2026]({{< relref "/publication/vlachos-semantic-uav-2026" >}}), implement a planner that keeps a formation connected while it flies its mission, with a directional link model in Gazebo/PX4.

### 4. Safe collision avoidance and interception with control barrier functions

*MSc thesis or PhD · control theory and simulation, optionally hardware*

Our SE(3) control barrier functions in [ICUAS 2026]({{< relref "/publication/vlachos-cbf-se3-2026" >}}) keep a counter-UAS interceptor safe under its hardware limits. Extend them to actuator saturation and sensing delays, to several interceptors, and to hardware-in-the-loop tests on small quadrotors.

## Drone detection and air mobility

### 5. Passive Wi-Fi radar and Remote ID for drone detection

*Diploma or MSc thesis, or internship · ESP32 and Wi-Fi hardware, signal processing*

Ordinary Wi-Fi signals reflected by a drone reveal it, and Remote ID broadcasts identify it. Build a low-cost detector that combines both and evaluate it with measurements from the EUSOME field trials. Our radar simulation framework in [ISC2 2025]({{< relref "/publication/petroutsos-design-2025" >}}) is the starting point for the radar side.

### 6. Radar and camera fusion for detect-and-avoid on small drones

*Diploma or MSc thesis · Python, deep learning, mmWave radar*

A camera fails in low light and a radar gives few pixels; together they can detect obstacles and other aircraft reliably. Train and test fusion detectors on the synchronized radar and camera data of [FIRA-DAV]({{< relref "/projects/firadav" >}}), for the detect-and-avoid function of [SPLASH]({{< relref "/projects/splash" >}}).

### 7. Cellular ISAC for drone surveillance in U-space

*MSc thesis or PhD · simulation and standards*

5G and 6G base stations can act as radars and track drones. Quantify the accuracy and coverage they reach, and what this means for the separation between drones in U-space, starting from our study of ISAC for advanced air mobility in [ISC2 2025]({{< relref "/publication/vlachos-isac-2025" >}}). The results relate to our contribution to the ETSI ISG ISAC standardisation group.

## What you get

A well-defined problem, code to start from, a weekly meeting and the Friday group seminar, compute time on ARIS, and co-authorship of what you publish.

## How to apply

[Write to us]({{< relref "/contact" >}}) with the topic you are interested in, a CV or transcript, and something you have built: code, a report, a project. Your own ideas within these directions are welcome too.

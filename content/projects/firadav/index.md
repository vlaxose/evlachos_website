---
title: "FIRA-DAV: Feature-level Image and Radar Fusion for Detect and Avoid"
summary: "Synchronized mmWave radar and camera dataset for Detect-and-Avoid in autonomous aerial vehicles, funded by the Athena RC Proof-of-Concept programme."
tags:
- Deep Learning
- Dataset
- Radar
- Autonomous Systems
- Sensor Fusion
date: "2023-09-01"

image:
  caption: 'FIRA-DAV: mmWave radar and camera data fusion for UAV perception'
  focal_point: Smart

stats:
  - value: "€10k"
    label: "Funding"
  - value: "PI"
    label: "Role"
  - value: "Athena RC PoC"
    label: "Programme"
  - value: "6 months"
    label: "Duration"
---

## Project Overview

**FIRA-DAV** (*Feature-level Image and Radar Fusion for Improved Detect and Avoid Functionality in Autonomous Aerial Vehicles*) is a Proof-of-Concept project funded by the **Athena Research Center Technology Transfer Office** under the internal PoC programme (ΔΕΜΤ, project No. 80260). The project was competitively selected in June 2023 following evaluation by a three-member expert panel, and ran from **September 2023 for 6 months**.

As **Principal Investigator**, I led the design, equipment procurement, and dataset construction for radar–camera sensor fusion targeting UAV Detect-and-Avoid (DAA) — a critical safety requirement for beyond-visual-line-of-sight (BVLOS) operations. The project was carried out in collaboration with **Hellenic Drones** (industry partner, Dr. Christos Skliros) and **ROBOSURVEY LTD** (equipment supplier).

## Team

- **Dr. Evangelos Vlachos** — PI, Athena Research Center / ISI
- **Hellenic Drones** (Dr. Christos Skliros) — Industry partner

## Equipment & Dataset

The project procured a **Texas Instruments IWR6843AoP** 77 GHz FMCW mmWave radar (Antenna-on-Package variant) and a synchronized CSI camera, integrated on a drone-mounted embedded platform. Measurement campaigns produced a synchronized dataset of radar 3D point clouds and RGB camera frames in real flight conditions, including UAV-to-UAV scenarios for obstacle detection.

Key technical work:
- **Data collection**: Synchronized radar point clouds and RGB frames captured in real UAV flight scenarios
- **Calibration**: Radar-to-camera extrinsic transformation, intrinsic camera calibration
- **CFAR detection**: Configuration of detection and tracking layers for the IWR6843AoP sensor
- **Applied for Google Cloud Research Credits** to support deep neural network training on the collected dataset

## Technical Outcomes

- Synchronized radar–camera dataset collected under real flight conditions
- Derivation of transformation function mapping radar 3D point cloud to 2D image plane
- Training pipeline for **spatial attention fusion** neural network combining radar and vision features
- Efficient Python and Julia code for embedded AI deployment
- Dataset and equipment directly adopted by **EUSOME** (Horizon Europe, 2025–2028), which carries no equipment budget

## Reviewer Recognition

The proposal was rated positively by all three external reviewers:

> *"This is a huge market and everyone is working on it. This tech, if unique and solves real issues, has cross applicability."*

> *"Deep-tech IT solution that relies on state-of-the-art technology and strong know-how that is probably difficult to be copied."*

---

*Funded by the Athena Research Center under the internal Proof-of-Concept (PoC) programme (ΔΕΜΤ No. 80260) of the Technology Transfer Office.*

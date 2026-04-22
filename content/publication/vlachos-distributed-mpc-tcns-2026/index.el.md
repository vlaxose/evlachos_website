---
title: "Distributed MPC for Directional UAV Networks: Co-design of Motion and Hybrid Beam Alignment"
date: 2026-03-05
publishDate: 2026-03-05
authors: ['Vlachos, E.']
publication_types: ["2"]
abstract: "Αυτή η εργασία αντιμετωπίζει το συζευγμένο πρόβλημα ελέγχου και επικοινωνίας σε δίκτυα UAV που λειτουργούν σε συχνότητες millimeter-wave (mmWave). Προτείνουμε ένα Κατανεμημένο πλαίσιο Ελέγχου Μοντέλου Πρόβλεψης (MPC) που βελτιστοποιεί από κοινού την τροχιά μετατόπισης και την μηχανική κατεύθυνση για τη μεγιστοποίηση της χωρητικότητας δικτύου με ασφάλεια. Εκτεταμένες προσομοιώσεις δείχνουν μείωση πιθανότητας αποτυχίας ζεύξης κατά ~96% σε σχέση με ευρετικές μεθόδους."
featured: true
publication: "*IEEE Transactions on Control of Network Systems*"
tags: ["Έρευνα", "UAVs", "MPC", "mmWave", "ISAC", "Κατανεμημένος Έλεγχος"]
---

## Supplementary Video

{{< video src="demo.mp4" controls="yes" >}}

## Key Contributions

- **Joint Motion–Communication Framework**: A decentralized MPC that jointly optimizes trajectory and mechanical heading for hybrid mechanical-electronic beamforming, proactively maintaining neighbors within the electronic FoV.
- **Theoretical Guarantees**: A smooth Gaussian-envelope surrogate for the non-convex hybrid gain with a proven Lipschitz-continuous gradient; a closed-form spectral contraction condition linking tracking weight, communication coupling, and beamwidth into a single tunable inequality guaranteeing convergence. Recursive feasibility established via a DARE-based warm-start strategy.
- **Experimental Validation**: High-fidelity simulations showing ~96% reduction in link outage probability vs. velocity-aligned heuristics, with O(1) per-agent scaling up to K=16 agents.

*This work was supported by the European Union's Horizon Europe programme under Grant Agreement No. 101187121 (EUSOME).*

---
title: "Safe Distributed MPC for Directional UAV Networks: One-Shot Co-Design of Motion and Two-Sided Beam Alignment"
date: 2026-03-05
publishDate: 2026-03-05
authors: ['Vlachos, E.']
publication_types: ["2"]
abstract: "Αυτή η εργασία αντιμετωπίζει το συζευγμένο πρόβλημα ελέγχου και επικοινωνίας σε δίκτυα UAV που λειτουργούν σε συχνότητες millimeter-wave (mmWave) με υβριδική μηχανική-ηλεκτρονική κατεύθυνση δέσμης. Δείχνουμε γεωμετρικά ότι όταν η γωνιακή διασπορά μιας γειτονιάς υπερβαίνει το ηλεκτρονικό πεδίο θέασης, καμία πολιτική προσανατολισμού δεν μπορεί να διατηρήσει τη συνδεσιμότητα, οπότε η ίδια η τροχιά μετατόπισης πρέπει να διαμορφώνει τη γεωμετρία της ζεύξης. Προτείνουμε ένα Κατανεμημένο πλαίσιο Ελέγχου Μοντέλου Πρόβλεψης (MPC) που σχεδιάζει από κοινού την τροχιά και τον προσανατολισμό υπό ένα αμφίπλευρο μοντέλο κέρδους δέσμης, με την αποφυγή σύγκρουσης επιβαλλόμενη ως αυστηρός περιορισμός συνάρτησης φραγμού ελέγχου (control barrier function) αντί ποινής. Αποδεικνύουμε θεωρήματα σύγκλισης και ανακτησιμότητας εφικτότητας, και εκτεταμένες προσομοιώσεις με φυσικό επίπεδο IEEE 802.11ad δείχνουν σημαντική μείωση της πιθανότητας αποτυχίας ζεύξης σε σχέση με ευρετικές μεθόδους, με σταθερό υπολογιστικό κόστος ανά πράκτορα καθώς αυξάνεται το σμήνος."
featured: true
publication: "*Υπό προετοιμασία για το IEEE Open Journal of Control Systems*"
tags: ["Έρευνα", "UAVs", "MPC", "mmWave", "ISAC", "Κατανεμημένος Έλεγχος", "Συναρτήσεις Φραγμού Ελέγχου"]
---

## Supplementary Video

{{< video src="demo.mp4" controls="yes" >}}

## Key Contributions

- **Joint Motion–Communication Framework**: A decentralized MPC that jointly optimizes trajectory and mechanical heading for hybrid mechanical-electronic beamforming, proactively maintaining neighbors within the electronic FoV.
- **Theoretical Guarantees**: A smooth Gaussian-envelope surrogate for the non-convex hybrid gain with a proven Lipschitz-continuous gradient; a closed-form spectral contraction condition linking tracking weight, communication coupling, and beamwidth into a single tunable inequality guaranteeing convergence. Recursive feasibility established via a DARE-based warm-start strategy.
- **Experimental Validation**: High-fidelity simulations showing ~96% reduction in link outage probability vs. velocity-aligned heuristics, with O(1) per-agent scaling up to K=16 agents.

*This work was supported by the European Union's Horizon Europe programme under Grant Agreement No. 101187121 (EUSOME).*

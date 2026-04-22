---
title: "Semantically-Informed Predictive Control for Autonomous UAV Connectivity in Urban Environments"
date: 2026-02-26
publishDate: 2026-02-26
authors: ['Vlachos, E.', 'Tsourounis, D.']
publication_types: ["1"]
abstract: "Τα millimeter-wave (mmWave) συχνότητες προσφέρουν την απαιτούμενη multi-gigabit ρυθμαπόδοση για τα δίκτυα UAV νέας γενιάς, αλλά η κατευθυντική τους διάδοση καθιστά την ποιότητα της ζεύξης ευαίσθητη στη σύνθεση υλικού των γύρω εμποδίων. Προτείνουμε ένα πλαίσιο ελέγχου που συνδυάζει mmWave ραντάρ με οπτική σημασιολογική ταξινόμηση για να κατασκευάσει μια αποτελεσματική μετρική χωρητικότητας που αποσυνδέει την ακατέργαστη ισχύ σήματος από την αξιοπιστία σύνδεσης ανάλογα με το υλικό. Monte Carlo προσομοιώσεις δείχνουν ότι ο προτεινόμενος ελεγκτής βελτιώνει την αποτελεσματική ρυθμαπόδοση κατά 65% σε σχέση με τις βάσεις αναφοράς, διατηρώντας αξιοπιστία σύνδεσης 0.96."
featured: false
publication: "*Under Development*"
tags: ["Έρευνα", "UAVs", "6G", "mmWave", "Σχεδιασμός Τροχιάς"]
---

## Key Contributions

- An **Effective Capacity** metric that extends the radio map paradigm by weighting raw throughput with a material-dependent reliability coefficient, decoupling signal strength from link stability and exposing permeable vegetation corridors that signal-strength planners overlook.
- A **two-layer planner** comprising (i) a Semantically-Informed RRT backbone augmented with material-dependent reliability and capacity acceptance checks that prune expansion through multipath zones, and (ii) a gradient-based trajectory optimizer that deforms the path by balancing signal-seeking and reliability-seeking forces derived from the product-rule decomposition of ∇C_eff.
- **Hardware validation** of the material ambiguity premise via characterization with a TI IWR6843AOP 60 GHz FMCW radar, confirming that radar alone cannot distinguish concrete from vegetation.

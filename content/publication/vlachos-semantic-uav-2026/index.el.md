---
title: "Semantically-Informed Predictive Control for Autonomous UAV Connectivity in Urban Environments"
date: 2026-08-24
publishDate: 2026-08-24
authors: ['Vlachos, E.', 'Tsourounis, D.', 'Kaushik, A.']
publication_types: ["1"]
abstract: "Οι συχνότητες millimeter-wave (mmWave) επιτρέπουν δίκτυα UAV υψηλής ρυθμαπόδοσης, όμως οι κατευθυντικές τους ζεύξεις είναι ευαίσθητες στη σύνθεση υλικού των εμποδίων. Οι συμβατικοί σχεδιαστές διαδρομής αποτυγχάνουν σε περιβάλλοντα με ποικίλα υλικά: οι γεωμετρικοί σχεδιαστές αντιμετωπίζουν τα εμπόδια ως αδιαφανή, ενώ οι σχεδιαστές βάσει ισχύος σήματος αναζητούν ζώνες υψηλού SNR χωρίς να διακρίνουν σταθερή οπτική επαφή από ασταθή πολυδιαδρομική διάδοση. Η εργασία αυτή εντάσσεται στον κλάδο της αίσθησης-υποβοηθούμενης Ολοκληρωμένης Αίσθησης και Επικοινωνίας (ISAC), όπου το ραντάρ εξυπηρετεί τη ζεύξη. Συνδυάζουμε αίσθηση ραντάρ με οπτική σημασιολογική ταξινόμηση για μια αποτελεσματική μετρική χωρητικότητας που αποσυνδέει την ισχύ σήματος από την αξιοπιστία ανάλογα με το υλικό. Ένας διβάθμιος σχεδιαστής παράγει διαδρομές που αποφεύγουν εμπόδια και ασταθείς ζώνες πολυδιαδρομικής διάδοσης, βελτιστοποιώντας την ενεργό ρυθμαπόδοση. Προσομοιώσεις δείχνουν σημαντική βελτίωση έναντι βάσεων αναφοράς βασισμένων σε ισχύ σήματος, πλησιάζοντας έναν oracle με πλήρη γνώση καναλιού."
featured: false
publication: "*NextGCom 2026 — Ειδική Συνεδρία: Integrated Sensing and AI-Driven Communication in 6G Perceptive Mobile Networks*"
tags: ["Έρευνα", "UAVs", "6G", "mmWave", "ISAC", "Σχεδιασμός Τροχιάς"]
---

## Key Contributions

- An **Effective Capacity** metric that extends the radio map paradigm by weighting raw throughput with a material-dependent reliability coefficient, decoupling signal strength from link stability and exposing permeable vegetation corridors that signal-strength planners overlook.
- A **two-layer planner** comprising (i) a Semantically-Informed RRT backbone augmented with material-dependent reliability and capacity acceptance checks that prune expansion through multipath zones, and (ii) a gradient-based trajectory optimizer that deforms the path by balancing signal-seeking and reliability-seeking forces derived from the product-rule decomposition of ∇C_eff.
- **Hardware validation** of the material ambiguity premise via characterization with a TI IWR6843AOP 60 GHz FMCW radar, confirming that radar alone cannot distinguish concrete from vegetation.

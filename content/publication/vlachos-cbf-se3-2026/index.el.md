---
title: "Hardware-Aware SE(3) Control Barrier Functions for Counter-UAS Interceptors with Directed Energy Payloads"
date: 2026-06-17
publishDate: 2026-06-17
authors: ['Vlachos, E.', 'Kolios, P.', 'Skliros, C.']
publication_types: ["1"]
abstract: "Ωφέλιμα φορτία κατευθυνόμενης ενέργειας σε drones — RF jammers και πηγές Υψηλής Ισχύος Μικροκυμάτων (HPM) — προσφέρουν επαναχρησιμοποιούμενη ικανότητα Counter-UAS, αλλά η υιοθέτησή τους σε μικρούς αναχαιτιστές περιορίζεται από αυστηρά όρια ισχύος. Αυτή η εργασία επιλύει τη σύγκρουση μεταξύ του περιορισμένου Πεδίου Ορατότητας (FoV) των κεραιών υψηλού κέρδους και των επιθετικών μεταβατικών στάσεων ενός multi-rotor μέσω ενός ασφαλούς φίλτρου βασισμένου σε Συναρτήσεις Φραγμού Ελέγχου (CBF) στην πολλαπλότητα SE(3). Επαλήθευση σε προσομοίωση SE(3) και περιβάλλον PX4 SITL δείχνει ότι το προτεινόμενο CBF εξαλείφει όλες τις παραβιάσεις FoV."
featured: false
publication: "*2026 International Conference on Unmanned Aircraft Systems (ICUAS)*"
tags: ["Έρευνα", "UAVs", "Συναρτήσεις Φραγμού Ελέγχου", "Counter-UAS", "SE(3)", "ISAC"]
---

## Simulation Demo

The animation below compares two methods on the SE(3) CBF scenario: the **unfiltered** controller (red) and the proposed **ADMM-CBF** safety filter (blue), which maintains FoV pointing throughout the pursuit maneuver.

{{< video src="demo.mp4" controls="yes" >}}

## Key Contributions

- A **hardware-aware CBF safety filter** on the SE(3) manifold that provides formal FoV pointing guarantees for directed-energy payloads under aggressive pursuit dynamics.
- Formulation of phased-array electronic steering limits as a **relative-degree-two safety constraint** with analytically verified Lie derivatives.
- An **ADMM solver** with constant-time core factorization enabling real-time onboard execution.
- Validation in both a nonlinear SE(3) simulation and a **PX4 SITL** environment, demonstrating elimination of all FoV violations and recovery of antenna gain through beam tightening.

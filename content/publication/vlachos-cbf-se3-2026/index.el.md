---
title: "Hardware-Aware SE(3) Control Barrier Functions for Counter-UAS Interceptors with Directed Energy Payloads"
date: 2026-06-17
publishDate: 2026-06-17
authors: ['Vlachos, E.', 'Kolios, P.', 'Skliros, C.']
publication_types: ["1"]
abstract: "Τα αυστηρά όρια ισχύος των μικρών drones αναχαίτισης περιορίζουν τη χρήση επαναχρησιμοποιούμενων ωφέλιμων φορτίων κατευθυνόμενης ενέργειας, όπως RF jammers και πηγές Υψηλής Ισχύος Μικροκυμάτων (HPM). Οι δέσμες υψηλού κέρδους μπορούν να κλείσουν τον προϋπολογισμό ζεύξης με ελάχιστη ισχύ εκπομπής, όμως το στενό Πεδίο Ορατότητας (FoV) που απαιτούν συγκρούεται με τους επιθετικούς ελιγμούς ενός multi-rotor σε καταδίωξη. Η εργασία επιλύει αυτή τη σύγκρουση με ένα φίλτρο ασφαλείας που λαμβάνει υπόψη το υλικό, βασισμένο σε Συναρτήσεις Φραγμού Ελέγχου (CBF) στην πολλαπλότητα SE(3). Το φίλτρο παρέχει τυπικές εγγυήσεις σκόπευσης, επιτρέποντας κεραίες υψηλής κατευθυντικότητας των οποίων το κέρδος διαφορετικά θα θυσιαζόταν για ανοχή στη σκόπευση. Τα όρια ηλεκτρονικής στρέψης μιας στοιχειοκεραίας διατυπώνονται ως περιορισμός ασφαλείας σχετικού βαθμού δύο με αναλυτικά επαληθευμένες παραγώγους Lie, και το προκύπτον Τετραγωνικό Πρόβλημα (QP) επιλύεται μέσω ADMM με παραγοντοποίηση πυρήνα σταθερού χρόνου. Η επαλήθευση σε μη γραμμική προσομοίωση SE(3) και σε προσαρμοσμένο περιβάλλον Software-in-the-Loop (SITL) 6 βαθμών ελευθερίας δείχνει ότι το προτεινόμενο CBF εξαλείφει όλες τις παραβιάσεις FoV και ανακτά έως 12,0 dB κέρδους κεραίας με στένωση της δέσμης. Η προσέγγιση δείχνει επίσης ότι ο συμβατικός περιορισμός της γωνίας pitch δεν προσφέρει ουσιαστικό όφελος έναντι των παραβιάσεων FoV, αποφεύγει τις σοβαρές αστοχίες λόγω κορεσμού ενεργοποιητών των αρχιτεκτονικών MPC-CBF πολλαπλών βημάτων, και εκτελείται αξιόπιστα σε λιγότερο από 350 μs."
featured: false
publication: "*2026 International Conference on Unmanned Aircraft Systems (ICUAS)*"
doi: "10.1109/ICUAS69441.2026.11598666"
# Code, data and slides: Zenodo record 20808892
url_code: "https://doi.org/10.5281/zenodo.20808892"
projects: ["eusome"]
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

---
title: "Geometry-Aware Regularization for Deep-Unfolded MIMO-OTFS Detection"
date: 2026-08-24
publishDate: 2026-08-24
authors: ['Ntavanelos, N.', 'Vlachos, E.']
publication_types: ["1"]
abstract: "Μελετάμε την ανίχνευση συμβόλων σε συστήματα Multiple-Input Multiple-Output Orthogonal Time Frequency Space (MIMO-OTFS) πάνω σε χρονικά μεταβαλλόμενα κανάλια πολλαπλών διαδρομών βασισμένα στη γεωμετρία, όπου η πολυδιαδρομική διάδοση προκαλεί χωρική και κλασματική σύζευξη Doppler–καθυστέρησης (DD) και οδηγεί σε ανομοιόμορφη κλιμάκωση των συνιστωσών των συμβόλων. Χαρακτηρίζουμε αναλυτικά αυτή την ανομοιόμορφη διαγώνια δομή του πίνακα Gram του MIMO-OTFS και δείχνουμε ότι όλη η διαγώνια μεταβολή οφείλεται αποκλειστικά στη σύζευξη μεταξύ διαδρομών. Με βάση αυτό το αποτέλεσμα, υιοθετούμε ένα πλαίσιο Συζυγών Κλίσεων (CG) με deep unfolding και εισάγουμε έναν γεωμετρικά ενημερωμένο ομαλοποιητή ανά συνιστώσα απευθείας στο υποκείμενο γραμμικό σύστημα, με βάρη που μαθαίνονται από τα δεδομένα. Τα αποτελέσματα προσομοίωσης σε σενάρια χαμηλής και υψηλής κινητικότητας δείχνουν ότι, για επαρκώς διαχωρισμένες διαδρομές διάδοσης, ο προτεινόμενος ανιχνευτής υπερέχει των μεθόδων χαμηλής πολυπλοκότητας και πλησιάζει την απόδοση πιο σύνθετων νευρωνικών αρχιτεκτονικών σε μέσο και υψηλό λόγο σήματος προς θόρυβο (SNR)."
featured: false
publication: "*2026 Next Generation Communications Conference (NextGCom 2026)*"
tags: ["Έρευνα", "MIMO-OTFS", "Deep Unfolding", "Ανίχνευση Σήματος", "6G"]
---

## Key Contributions

- **Gram matrix analysis**: Analytical characterization of the non-uniform diagonal structure of the MIMO-OTFS Gram matrix, proving that all diagonal variation arises exclusively from inter-path coupling.
- **Geometry-aware regularizer**: A coordinate-wise regularizer embedded into a deep-unfolded Conjugate Gradient detector, with per-component weights learned in a data-driven manner.
- **Performance gains**: The proposed detector outperforms low-complexity baselines and approaches heavier neural architectures at medium-to-high SNR, with improved robustness in high-mobility scenarios.

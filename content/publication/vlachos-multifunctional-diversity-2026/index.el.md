---
title: "Multi-Functional Diversity via Flexible Spatial Partitioning for Massive MIMO ISAC"
date: 2026-03-05
publishDate: 2026-03-05
authors: ['Vlachos, E.', 'Masouros, C.']
publication_types: ["2"]
abstract: "Σε συστήματα massive MIMO Ολοκληρωμένης Αίσθησης και Επικοινωνιών (ISAC), η συμβατική συνεχόμενη κατανομή υπο-συστοιχιών περιορίζει τους χωρικούς βαθμούς ελευθερίας. Αυτή η εργασία αποδεικνύει ότι η εναλλασσόμενη ανάθεση δεσμών ξεκλειδώνει πολυλειτουργική ποικιλομορφία επιλογής. Αναλυτικά αποδεικνύουμε ότι το κέρδος από τη χωρική αποσύζευξη κλιμακώνεται λογαριθμικά με το μέγεθος της κεραίας. Προτείνουμε τον αλγόριθμο DASP, ένα πλαίσιο βασισμένο σε συνδιασπορά που εξαλείφει την επιβάρυνση άμεσης CSI με πολυπλοκότητα O(N log N) ανά ενημέρωση. Αριθμητικά αποτελέσματα με έως 256 κεραίες επιβεβαιώνουν ότι η ευέλικτη κατανομή υπερτερεί σημαντικά έναντι ορθογώνιου τεμαχισμού πόρων σε τυπικά mmWave link budgets."
featured: false
publication: "*Υπό προετοιμασία για το IEEE Transactions on Communications*"
tags: ["Έρευνα", "ISAC", "Massive MIMO", "Υβριδική Διαμόρφωση Δέσμης", "6G", "mmWave"]
---

## Key Contributions

- **Multi-functional selection diversity**: We prove that interleaved beam assignment between communication and radar unlocks a new diversity mechanism — spatial decoupling (leakage avoidance) — whose gain scales as **log(N)** with array size, while signal alignment saturates, making it the dominant gain at massive MIMO scales.
- **DASP algorithm**: A covariance-only framework that solves the combinatorial beam assignment problem with **O(N log N)** per-update complexity, eliminating instantaneous CSI overhead and operating directly in beamspace.
- **Analytical SNR threshold**: A closed-form condition demarcating when flexible spatial partitioning outperforms orthogonal resource slicing (TDM/FDM), showing that standard mmWave link budgets fall firmly in the partitioning-favorable regime.

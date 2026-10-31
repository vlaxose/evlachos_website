---
title: "Consistency-Gated Cooperative Localization for UAV Swarms Under Intermittent GPS"
date: 2026-06-02
publishDate: 2026-06-02
authors: ['Venetis, D.', 'Vlachos, E.', 'Berberidis, K.']
publication_types: ["1"]
abstract: "Ο συνεργατικός εντοπισμός θέσης με διακοπτόμενο Παγκόσμιο Δορυφορικό Σύστημα Πλοήγησης (GNSS) είναι δύσκολος, καθώς η αφελής συνεργασία μπορεί να υποβαθμίσει την εκτίμηση όταν οι σχετικές μετρήσεις είναι ασυνεπείς. Η εργασία προτείνει ένα πλαίσιο εντοπισμού δύο σταδίων για σμήνη Μη Επανδρωμένων Αεροσκαφών (UAV), όπου κάθε πράκτορας διατηρεί μια τοπική εκτίμηση με Εκτεταμένο Φίλτρο Kalman (EKF) από δεδομένα GPS και Αδρανειακής Μονάδας Μέτρησης (IMU), και εφαρμόζει κατανεμημένη βελτίωση με βάση σχετικούς περιορισμούς απόστασης Ultra-Wideband (UWB) και κατεύθυνσης από τη Γωνία Άφιξης (AoA). Επιπλέον, προτείνεται μια ελαφριά πύλη συνέπειας, που βασίζεται σε δείκτες υπολοίπων και συναίνεσης και αποφασίζει αν η συνεργατική βελτίωση θα γίνει δεκτή, αποτρέποντας επιβλαβείς ενημερώσεις χωρίς πραγματικές τιμές αναφοράς κατά τη λειτουργία. Τα αποτελέσματα προσομοίωσης δείχνουν σταθερές βελτιώσεις στη σχετική ακρίβεια που αφορά τον σχηματισμό και σταθερό απόλυτο εντοπισμό σε σύγκριση με τις βάσεις αναφοράς GPS και GPS+EKF υπό διακοπτόμενη διαθεσιμότητα GPS."
featured: false
url_pdf: "paper.pdf"
publication: "*34th European Signal Processing Conference (EUSIPCO 2026)*"
tags: ["Έρευνα", "UAVs", "Συνεργατικός Εντοπισμός", "GPS", "EKF", "ADMM", "UWB", "AoA"]
---

## Key Contributions

- **Consistency-gated framework**: A cooperative localization scheme that actively prevents harmful cooperative updates when inter-agent measurements are inconsistent under intermittent GPS.
- **Two-stage estimation**: Decoupled architecture separating local observability recovery (EKF with GPS/IMU) from cooperative refinement (distributed ADMM over UWB range and AoA constraints).
- **Lightweight acceptance gate**: A learning-based gate driven solely by runtime residual and consensus indicators — no ground truth required online.
- **Quantitative gains**: Demonstrated moderate improvements in absolute accuracy and substantial gains in formation-relevant relative accuracy over GPS/IMU baselines.

---
title: "Biconvex ADMM for Sensing-Aided XL-MIMO Channel Estimation at the THz Frequency Band"
date: 2026-06-13
publishDate: 2026-06-13
authors: ['Vlachos, E.', 'Alexandropoulos, G. C.']
publication_types: ["1"]
abstract: "Τα συστήματα MIMO με εξαιρετικά μεγάλες στοιχειοκεραίες (XL-MIMO) στα Terahertz (THz) είναι βασική τεχνολογία για την ολοκληρωμένη αίσθηση και επικοινωνία (ISAC) στο 6G, όμως το εξαιρετικά μεγάλο εύρος ζώνης τους προκαλεί διπλά ευρυζωνικές διαλείψεις (dual-wideband fading): ταυτόχρονη χωρική απόκλιση δέσμης (beam squint) και χρονική διασπορά πολλαπλών διαδρομών, που συζευγνύουν την εκτίμηση γωνίας και καθυστέρησης σε εκατοντάδες ζεύγη κεραιών. Η εργασία προτείνει ένα πλαίσιο με υποβοήθηση αίσθησης, στο οποίο η έξοδος του μονοστατικού ραντάρ του σταθμού βάσης αρχικοποιεί έναν δικυρτό (biconvex) αλγόριθμο ADMM που ανακτά από κοινού τον πίνακα του καναλιού και το δυαδικό διάνυσμα υποστήριξης των καθυστερήσεων. Το ανακτημένο προφίλ καθυστερήσεων κλείνει ταυτόχρονα τον βρόχο του ISAC ως έξοδος αίσθησης, χωρίς επιπλέον πιλοτικό φόρτο. Προσομοιώσεις σε σύστημα THz XL-MIMO μεγάλης κλίμακας δείχνουν ότι η προτεινόμενη μέθοδος υπερέχει σημαντικά των μεθόδων αραιής ανάκτησης και του oracle-LS, επιτυγχάνει ακριβή ανάκτηση της υποστήριξης καθυστερήσεων πέρα από ένα κατώφλι μήκους πιλοτικών, και προσεγγίζει στενά το όριο Cramér-Rao."
featured: false
publication: "*2026 IEEE 1st Annual Integrated Sensing and Communication Conference (ISAC)*"
tags: ["Έρευνα", "ISAC", "THz", "XL-MIMO", "Εκτίμηση Καναλιού", "ADMM", "6G"]
research: ["channel-estimation"]
---

## Key Contributions

- **Biconvex ADMM with binary support enforcement**: We show that the THz XL-MIMO dual-wideband channel concentrates onto a shared binary delay support of drastically reduced dimension, and develop a biconvex ADMM where iterative hard thresholding (IHT) exactly enforces this structure — outperforming continuous-valued sparse recovery and oracle-LS baselines in the barely-determined regime.
- **Sensing-aided warm start at no pilot cost**: The base station's monostatic radar output initialises the delay-support estimate, yielding provably exact support recovery beyond a pilot-length threshold, with no additional pilot overhead.
- **CRB proximity**: The proposed estimator closely approaches the Cramér-Rao Bound and closes the ISAC sensing loop by delivering the recovered delay profile as a radar output.

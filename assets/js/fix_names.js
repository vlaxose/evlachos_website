document.addEventListener("DOMContentLoaded", function() {
    
    // Ελέγχουμε αν είμαστε στην Ελληνική έκδοση
    const isGreek = window.location.pathname.includes('/el/');

    // Ο Χάρτης των Τύπων (Αγγλικά & Ελληνικά)
    const typeMap = {
        '0': isGreek ? 'Ακατηγοριοποίητο' : 'Uncategorized',
        '1': isGreek ? 'Άρθρο Συνεδρίου' : 'Conference Paper',
        '2': isGreek ? 'Άρθρο Περιοδικού' : 'Journal Article',
        '3': isGreek ? 'Preprint' : 'Preprint',
        '4': isGreek ? 'Τεχνική Αναφορά' : 'Technical Report',
        '5': isGreek ? 'Βιβλίο' : 'Book',
        '6': isGreek ? 'Κεφάλαιο Βιβλίου' : 'Book Section',
        '7': isGreek ? 'Διατριβή' : 'Thesis',
        '8': isGreek ? 'Πατέντα' : 'Patent'
    };

    // Λειτουργία 1: Αλλαγή των Links (π.χ. στα φίλτρα ή στα tags)
    // Ψάχνουμε συνδέσμους που περιέχουν το "/publication_types/"
    const links = document.querySelectorAll('a[href*="/publication_types/"]');
    links.forEach(link => {
        const code = link.textContent.trim();
        if (typeMap[code]) {
            link.textContent = typeMap[code];
        }
    });

    // Λειτουργία 2: Αλλαγή του κειμένου στη σελίδα (όπως στο screenshot σου)
    // Ψάχνουμε στοιχεία που έχουν ΑΚΡΙΒΩΣ έναν αριθμό μέσα τους
    const allDivs = document.querySelectorAll('.col-md-10, .col-md-9, .col-12, span, div');
    
    allDivs.forEach(div => {
        const text = div.textContent.trim();
        // Αν το κείμενο είναι ακριβώς "1", "2" κλπ.
        if (typeMap[text]) {
            // Έλεγχος: Βεβαιωνόμαστε ότι είναι δίπλα σε ετικέτα "Type" ή "Τύπος"
            // για να μην αλλάξουμε τυχαίους αριθμούς σελίδων.
            const parent = div.parentElement;
            if (parent && (parent.innerText.includes('Type') || parent.innerText.includes('Τύπος') || div.className.includes('pub-type'))) {
                div.textContent = typeMap[text];
            }
        }
    });
});

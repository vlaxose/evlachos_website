import bibtexparser
import os
import re

# --- ΡΥΘΜΙΣΕΙΣ ---
BIB_FILE = 'mybibliography_compy.bib'
PUBLICATION_DIR = 'content/publication/'

def clean_text(text):
    """Καθαρίζει κείμενο για YAML (αφαιρεί αγκύλες BibTeX)."""
    if not text: return ""
    # Αφαίρεση { και } που βάζει το BibTeX
    text = text.replace('{', '').replace('}', '')
    # Escape τα διπλά εισαγωγικά
    text = text.replace('"', '\\"')
    return text.strip()

def update_md_file(folder_path, doi, publication):
    index_file = os.path.join(folder_path, 'index.md')
    if not os.path.exists(index_file):
        return False

    with open(index_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    
    # Flags για να ξέρουμε αν βρήκαμε τα πεδία
    found_doi = False
    found_pub = False
    
    # Επεξεργασία υπαρχουσών γραμμών
    for line in lines:
        stripped = line.strip()
        
        # 1. Έλεγχος για DOI
        if stripped.startswith('doi:'):
            if doi:
                new_lines.append(f'doi: "{doi}"\n')
                found_doi = True
            else:
                new_lines.append(line) # Κρατάμε το παλιό αν δεν έχουμε νέο
                found_doi = True
        
        # 2. Έλεγχος για Publication (Περιοδικό/Συνέδριο)
        elif stripped.startswith('publication:'):
            # Ενημερώνουμε μόνο αν είναι κενό ή αν θέλουμε να το κάνουμε overwrite
            # Εδώ επιλέγουμε να το ενημερώσουμε αν βρήκαμε κάτι στο BibTeX
            if publication:
                new_lines.append(f'publication: "*{publication}*"\n')
                found_pub = True
            else:
                new_lines.append(line)
                found_pub = True
        
        else:
            new_lines.append(line)

    # Αν δεν βρέθηκαν, τα προσθέτουμε μετά το 'date:' ή 'title:'
    insertion_point = -1
    for i, line in enumerate(new_lines):
        if line.strip().startswith('date:') or line.strip().startswith('title:'):
            insertion_point = i
    
    # Αν δεν βρήκαμε κατάλληλο σημείο, βάλτα μετά το πρώτο ---
    if insertion_point == -1:
        insertion_point = 1

    # Προσθήκη νέων πεδίων (αν δεν υπήρχαν)
    extras = []
    if not found_doi and doi:
        extras.append(f'doi: "{doi}"\n')
    if not found_pub and publication:
        extras.append(f'publication: "*{publication}*"\n')

    # Εισαγωγή στη λίστα
    if extras:
        # Τα βάζουμε αμέσως μετά το date/title
        for extra in reversed(extras):
            new_lines.insert(insertion_point + 1, extra)
        
        # Γράψιμο αρχείου
        with open(index_file, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        return True

    return False # Δεν έγιναν αλλαγές (υπήρχαν ήδη ή δεν βρέθηκαν νέα στοιχεία)

def main():
    print(f"📂 Ανάγνωση BibTeX: {BIB_FILE}...")
    
    if not os.path.exists(BIB_FILE):
        print(f"❌ Το αρχείο {BIB_FILE} δεν βρέθηκε.")
        return

    with open(BIB_FILE, encoding='utf-8') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    count = 0
    print(f"🔍 Επεξεργασία {len(bib_database.entries)} εγγραφών...")

    for entry in bib_database.entries:
        bib_id = entry.get('ID', '')
        
        # Ανάκτηση δεδομένων
        doi = entry.get('doi', '')
        
        # Το όνομα του περιοδικού μπορεί να είναι 'journal' ή 'booktitle' (για συνέδρια)
        publication = entry.get('journal', entry.get('booktitle', ''))
        publication = clean_text(publication)
        
        if not doi and not publication:
            continue

        # Εύρεση φακέλου
        slug = bib_id.lower().replace('_', '-')
        folder_path = os.path.join(PUBLICATION_DIR, slug)
        
        # Fallback αν δεν βρεθεί με slug
        if not os.path.isdir(folder_path):
             folder_path = os.path.join(PUBLICATION_DIR, bib_id)
             if not os.path.isdir(folder_path):
                 continue

        # Ενημέρωση
        if update_md_file(folder_path, doi, publication):
            # print(f"✅ {bib_id}: Ενημερώθηκε (DOI: {bool(doi)}, Pub: {bool(publication)})")
            count += 1

    print("-" * 30)
    print(f"🎉 Εμπλουτίστηκαν {count} δημοσιεύσεις με Metadata!")

if __name__ == "__main__":
    main()

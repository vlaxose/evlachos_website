import bibtexparser
import os
import re

# --- ΡΥΘΜΙΣΕΙΣ ---
BIB_FILE = 'mybibliography_compy.bib'
PUBLICATION_DIR = 'content/publication/'

# Αντιστοίχιση BibTeX -> Hugo Blox ID
TYPE_MAPPING = {
    'article': "2",          # Journal Article
    'inproceedings': "1",    # Conference Paper
    'conference': "1",       # Conference Paper
    'phdthesis': "7",        # Thesis
    'mastersthesis': "7",    # Thesis
    'techreport': "4",       # Report
    'unpublished': "3",      # Preprint
    'misc': "0"              # Uncategorized
}

def update_md_file(folder_path, type_code):
    index_file = os.path.join(folder_path, 'index.md')
    if not os.path.exists(index_file):
        return False

    # Διαβάζουμε το αρχείο
    with open(index_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    found_types = False
    
    # Η μορφή που θέλουμε είναι: publication_types: ["2"]
    type_line = f'publication_types: ["{type_code}"]\n'

    for line in lines:
        if line.strip().startswith('publication_types:'):
            new_lines.append(type_line)
            found_types = True
        else:
            new_lines.append(line)
            
            # Αν φτάσαμε στο τέλος του YAML (---) και δεν βρήκαμε το tag, το προσθέτουμε
            if line.strip() == '---' and len(new_lines) > 1 and not found_types:
                # Το βάζουμε πριν το τελευταίο ---
                new_lines.insert(-1, type_line)
                found_types = True

    # Γράφουμε πάλι το αρχείο
    with open(index_file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    return True

def fix_types():
    print(f"📂 Ανάγνωση βιβλιογραφίας: {BIB_FILE}...")
    
    with open(BIB_FILE, encoding='utf-8') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    count = 0
    
    print(f"🔍 Επεξεργασία {len(bib_database.entries)} εγγραφών...")

    for entry in bib_database.entries:
        bib_id = entry.get('ID', '')
        entry_type = entry.get('ENTRYTYPE', '').lower()
        
        # Βρες τον σωστό κωδικό
        type_code = TYPE_MAPPING.get(entry_type, "0")
        
        # Βρες τον φάκελο (Slug)
        slug = bib_id.lower().replace('_', '-')
        target_dir = os.path.join(PUBLICATION_DIR, slug)
        
        # Αν δεν υπάρχει, δοκίμασε και με το original ID (αν δεν έχεις αλλάξει τα folder names)
        if not os.path.isdir(target_dir):
            target_dir_alt = os.path.join(PUBLICATION_DIR, bib_id)
            if os.path.isdir(target_dir_alt):
                target_dir = target_dir_alt
            else:
                continue

        # Ενημέρωση
        if update_md_file(target_dir, type_code):
            print(f"✅ {bib_id}: Ορίστηκε ως Type {type_code} ({entry_type})")
            count += 1
        else:
            print(f"❌ {bib_id}: Δεν βρέθηκε το index.md")

    print("-" * 30)
    print(f"🎉 Ενημερώθηκαν {count} αρχεία.")

if __name__ == "__main__":
    fix_types()

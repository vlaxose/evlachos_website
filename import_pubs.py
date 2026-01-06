import bibtexparser
import os
import re

# Ρυθμίσεις
BIB_FILE = 'mybibliography_compy.bib'
OUTPUT_DIR = 'content/publication/'

def clean_text(text):
    if not text: return ""
    return text.replace('{', '').replace('}', '').replace('\\', '')

def import_publications():
    if not os.path.exists(BIB_FILE):
        print(f"❌ Δεν βρέθηκε το αρχείο {BIB_FILE}")
        return

    with open(BIB_FILE, encoding='utf-8') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    print(f"Βρέθηκαν {len(bib_database.entries)} δημοσιεύσεις. Ξεκινάει η εισαγωγή...")

    for entry in bib_database.entries:
        title = clean_text(entry.get('title', 'No Title'))
        year = entry.get('year', '2025')
        date_str = f"{year}-01-01"
        
        # Καθαρισμός συγγραφέων
        authors_raw = entry.get('author', 'Admin')
        authors = [a.strip() for a in authors_raw.split(' and ')]
        
        # Τύπος δημοσίευσης (2=Journal, 1=Conference, 6=Book Chapter)
        entry_type = entry.get('ENTRYTYPE', '').lower()
        if 'article' in entry_type:
            pub_type = '2'
            publication = entry.get('journal', '')
        elif 'inproceedings' in entry_type:
            pub_type = '1'
            publication = entry.get('booktitle', '')
        elif 'incollection' in entry_type:
            pub_type = '6'
            publication = entry.get('booktitle', 'Book Chapter')
        else:
            pub_type = '0'
            publication = ""

        # Δημιουργία φακέλου
        slug = entry.get('ID', title[:20]).lower().replace('_', '-')
        folder_path = os.path.join(OUTPUT_DIR, slug)
        os.makedirs(folder_path, exist_ok=True)
        
        # Δημιουργία αρχείου index.md
        md_content = f"""---
title: "{title}"
date: {date_str}
publishDate: {date_str}
authors: {authors}
publication_types: ["{pub_type}"]
abstract: ""
featured: false
publication: "*{clean_text(publication)}*"
tags: ["Research", "6G", "UAVs"]
---
"""
        with open(os.path.join(folder_path, 'index.md'), 'w', encoding='utf-8') as f:
            f.write(md_content)

    print("✅ Ολοκληρώθηκε! Τρέξε 'hugo server' για να τα δεις.")

if __name__ == "__main__":
    import_publications()

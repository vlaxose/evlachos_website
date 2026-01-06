import os
import re
from pypdf import PdfReader

# --- ΡΥΘΜΙΣΕΙΣ ---
PUBLICATION_DIR = 'content/publication/'

def clean_markdown_file(folder_path):
    """
    Σβήνει τις ενότητες ## Introduction και ## Conclusion που προστέθηκαν
    από προηγούμενα scripts, για να ξεκινήσουμε καθαρά.
    """
    index_file = os.path.join(folder_path, 'index.md')
    if not os.path.exists(index_file): return False

    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Κρατάμε το κείμενο ΜΕΧΡΙ την πρώτη εμφάνιση του ## Introduction ή ## Conclusion
    # Αυτό υποθέτει ότι τα προσθέσαμε στο τέλος.
    
    clean_content = content
    
    # Αφαίρεση Introduction
    if "## Introduction" in clean_content:
        clean_content = clean_content.split("## Introduction")[0].strip()
        
    # Αφαίρεση Conclusion (αν υπάρχει ακόμα)
    if "## Conclusion" in clean_content:
        clean_content = clean_content.split("## Conclusion")[0].strip()
        
    # Αποθήκευση μόνο αν άλλαξε κάτι
    if clean_content != content:
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(clean_content + "\n")
        return True
    return False

def extract_strict_section(text, section_name):
    """
    Ψάχνει γραμμή-γραμμή για τον τίτλο της ενότητας (π.χ. "VI. CONCLUSION").
    """
    lines = text.split('\n')
    capture = False
    captured_text = []
    
    # Regex για αυστηρό τίτλο ενότητας (π.χ. "1. Conclusion", "VI. Conclusions", "Conclusion")
    # Πρέπει να είναι σε δική του γραμμή ή σχεδόν μόνος του.
    header_pattern = re.compile(fr'^\s*(?:[0-9IVX]+\.?\s*)?{section_name}s?\s*$', re.IGNORECASE)
    
    # Regex για να σταματήσουμε (References, Acknowledgment)
    stop_pattern = re.compile(r'^\s*(?:[0-9IVX]+\.?\s*)?(?:References|Bibliography|Acknowledgment)', re.IGNORECASE)

    for line in lines:
        clean_line = line.strip()
        
        # Αν δεν καταγράφουμε ακόμα, ψάχνουμε την αρχή
        if not capture:
            if header_pattern.match(clean_line):
                capture = True
                continue # Μην συμπεριλάβεις τον τίτλο στο κείμενο
        
        # Αν καταγράφουμε
        else:
            # Έλεγχος για τερματισμό
            if stop_pattern.match(clean_line):
                break
            
            # Φίλτρο για σκουπίδια (π.χ. αριθμοί σελίδας, headers που επαναλαμβάνονται)
            if len(clean_line) < 3 or clean_line.isdigit():
                continue
                
            captured_text.append(clean_line)

    if not captured_text:
        return None

    # Ενώνουμε το κείμενο
    full_text = " ".join(captured_text)
    
    # Καθαρισμός από hyphenation (λέξεις που κό- βονται)
    full_text = re.sub(r'(\w+)-\s+(\w+)', r'\1\2', full_text)
    
    # Αν το κείμενο είναι πολύ μικρό (<100 chars), μάλλον είναι λάθος extraction
    if len(full_text) < 100:
        return None
        
    return full_text

def analyze_pdf_strict(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        full_text = ""
        
        # Διαβάζουμε όλο το PDF γιατί το Conclusion μπορεί να μην είναι στην τελευταία σελίδα
        # (π.χ. αν ακολουθούν 2 σελίδες References)
        for page in reader.pages:
            full_text += page.extract_text() + "\n"
            
        data = {}
        
        # Αυστηρή εξαγωγή Conclusion
        conclusion = extract_strict_section(full_text, "Conclusion")
        if conclusion:
            data['conclusion'] = conclusion
            
        return data

    except Exception as e:
        print(f"⚠️ Error reading PDF: {e}")
        return {}

def update_md(folder_path, data):
    index_file = os.path.join(folder_path, 'index.md')
    
    if data.get('conclusion'):
        with open(index_file, 'a', encoding='utf-8') as f:
            f.write(f"\n## Conclusion\n\n{data['conclusion']}\n")
        return True
    return False

def main():
    print(f"🧹 Καθαρισμός παλιών 'trash' conclusions & Αυστηρή Εξαγωγή...")
    cleaned_count = 0
    added_count = 0
    
    for folder_name in os.listdir(PUBLICATION_DIR):
        folder_path = os.path.join(PUBLICATION_DIR, folder_name)
        if not os.path.isdir(folder_path): continue
        
        # 1. ΚΑΘΑΡΙΣΜΟΣ (Σβήσε τα παλιά χάλια)
        if clean_markdown_file(folder_path):
            cleaned_count += 1
        
        # 2. ΑΥΣΤΗΡΗ ΑΝΑΛΥΣΗ
        pdf_path = os.path.join(folder_path, 'paper.pdf')
        if os.path.exists(pdf_path):
            data = analyze_pdf_strict(pdf_path)
            
            if update_md(folder_path, data):
                print(f"✅ {folder_name}: Προστέθηκε ΚΑΘΑΡΟ Conclusion")
                added_count += 1
            else:
                pass 
                # print(f"🔸 {folder_name}: Δεν βρέθηκε καθαρό conclusion (Skipped).")

    print("-" * 30)
    print(f"🗑️  Καθαρίστηκαν {cleaned_count} αρχεία από παλιά δεδομένα.")
    print(f"✨ Προστέθηκαν {added_count} νέα, έγκυρα Conclusions.")

if __name__ == "__main__":
    main()

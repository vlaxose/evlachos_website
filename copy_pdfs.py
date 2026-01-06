import os
import shutil
import re
import difflib

# --- ΡΥΘΜΙΣΕΙΣ ---
# Ο φάκελος με τα χύμα PDF
PDF_SOURCE_DIR = '/home/vagos/Documents/MyPublications/CV_Attachments/'

# Ο φάκελος του Hugo site
HUGO_PUB_DIR = 'content/publication/'

def normalize_text(text):
    """
    Καθαρίζει κείμενο για σύγκριση.
    Αφαιρεί: [C17], .pdf, quotes, ειδικούς χαρακτήρες.
    """
    if not text: return ""
    # Αφαίρεση extensions
    text = text.replace('.pdf', '')
    # Αφαίρεση brackets στην αρχή π.χ. [C17], [J1]
    text = re.sub(r'^\[[A-Za-z0-9]+\]', '', text)
    # Αφαίρεση quotes αν υπάρχουν στο yaml (π.χ. "Title")
    text = text.strip('"\'')
    # Κρατάμε μόνο γράμματα και αριθμούς
    text = re.sub(r'[^a-zA-Z0-9]', '', text)
    return text.lower()

def get_hugo_title(folder_path):
    """Διαβάζει τον τίτλο από το index.md του Hugo."""
    index_file = os.path.join(folder_path, 'index.md')
    if not os.path.exists(index_file):
        return None
    
    try:
        with open(index_file, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip().startswith('title:'):
                    # Παίρνουμε το κείμενο μετά το 'title:'
                    return line.split(':', 1)[1].strip()
    except:
        pass
    return None

def copy_pdfs_reverse():
    print(f"📂 Σάρωση φακέλων στο {HUGO_PUB_DIR}...")
    
    # 1. Διαβάζουμε όλα τα PDF στον φάκελο πηγής και τα "καθαρίζουμε"
    if not os.path.isdir(PDF_SOURCE_DIR):
        print(f"❌ Λάθος διαδρομή πηγής: {PDF_SOURCE_DIR}")
        return

    source_files = [f for f in os.listdir(PDF_SOURCE_DIR) if f.endswith('.pdf')]
    # Λεξικό: { 'καθαρός_τίτλος': 'πραγματικό_όνομα_αρχείου' }
    normalized_source_map = {normalize_text(f): f for f in source_files}
    
    print(f"📦 Βρέθηκαν {len(source_files)} PDF στην πηγή.")

    count = 0
    missing = 0

    # 2. Μπαίνουμε σε κάθε φάκελο δημοσίευσης στο Hugo
    hugo_folders = [f.path for f in os.scandir(HUGO_PUB_DIR) if f.is_dir()]

    for folder in hugo_folders:
        folder_name = os.path.basename(folder)
        
        # Αγνοούμε φακέλους συστήματος (π.χ. featured) αν δεν έχουν index.md με title
        title = get_hugo_title(folder)
        if not title:
            continue

        clean_hugo_title = normalize_text(title)
        
        # 3. Ταίριασμα
        match_filename = None
        
        # Ακριβές ταίριασμα
        if clean_hugo_title in normalized_source_map:
            match_filename = normalized_source_map[clean_hugo_title]
        else:
            # Fuzzy Matching (αν υπάρχει μικρή διαφορά)
            matches = difflib.get_close_matches(clean_hugo_title, normalized_source_map.keys(), n=1, cutoff=0.85)
            if matches:
                match_filename = normalized_source_map[matches[0]]

        # 4. Αντιγραφή
        if match_filename:
            src = os.path.join(PDF_SOURCE_DIR, match_filename)
            dst = os.path.join(folder, 'paper.pdf')
            
            try:
                shutil.copy2(src, dst)
                print(f"✅ {folder_name}: Αντιγράφηκε -> {match_filename}")
                count += 1
            except Exception as e:
                print(f"❌ Error copying {folder_name}: {e}")
        else:
            # print(f"🔸 Δεν βρέθηκε PDF για: {folder_name}")
            missing += 1

    print("-" * 30)
    print(f"🎉 Τέλος! Αντιγράφηκαν {count} PDFs.")
    if missing > 0:
        print(f"⚠️  Δεν βρέθηκαν PDFs για {missing} δημοσιεύσεις.")

if __name__ == "__main__":
    copy_pdfs_reverse()

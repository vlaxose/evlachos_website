import os
import re
from pypdf import PdfReader

# --- ΡΥΘΜΙΣΕΙΣ ---
PUBLICATION_DIR = 'content/publication/'

def clean_text(text):
    """Καθαρίζει το κείμενο από πολλαπλά κενά και αλλαγές γραμμής."""
    text = text.replace('\n', ' ').replace('\r', '')
    text = re.sub(r'\s+', ' ', text)
    text = text.replace('"', '\\"') # Escape quotes for YAML
    return text.strip()

def extract_abstract_smart(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        # Διαβάζουμε τις 2 πρώτες σελίδες για σιγουριά
        for i in range(min(2, len(reader.pages))):
            text += reader.pages[i].extract_text() + " "
        
        raw_text = clean_text(text)

        # Λίστα με πιθανές αρχές και τέλη
        start_markers = [
            r'Abstract\s*[:.—-]', 
            r'ABSTRACT\s*[:.—-]', 
            r'A\s*B\s*S\s*T\s*R\s*A\s*C\s*T',
            r'Summary\s*[:.—-]'
        ]
        
        # Πιθανά σημεία που τελειώνει το abstract
        end_markers = [
            r'Index Terms', r'Keywords', r'Key words', 
            r'Introduction', r'I\.\s*Introduction', r'1\.\s*Introduction',
            r'I\.\s*INTRODUCTION', r'1\.\s*INTRODUCTION'
        ]

        # 1. Πρώτη Προσπάθεια: Αυστηρό Regex (Start ... End)
        for start in start_markers:
            for end in end_markers:
                # Ψάχνουμε κείμενο ανάμεσα στα markers
                pattern = f"(?i)({start})(.*?)({end})"
                match = re.search(pattern, raw_text)
                if match:
                    # Επιστρέφουμε την ομάδα 2 (το περιεχόμενο)
                    candidate = match.group(2).strip()
                    if len(candidate) > 20 and len(candidate) < 2500:
                        return candidate

        # 2. Δεύτερη Προσπάθεια: Βρες το "Abstract" και πάρε τα επόμενα 1000-1500 γράμματα
        # (Χρήσιμο αν το "Introduction" δεν διαβάζεται σωστά)
        fallback_match = re.search(r'(?i)Abstract\s*[:.—-]?(.*)', raw_text)
        if fallback_match:
            candidate = fallback_match.group(1).strip()
            # Κόβουμε "μπακάλικα" στους 1200 χαρακτήρες ή στην τελευταία τελεία
            if len(candidate) > 1200:
                cut_candidate = candidate[:1200]
                last_dot = cut_candidate.rfind('.')
                if last_dot > 100:
                    return cut_candidate[:last_dot+1]
                else:
                    return cut_candidate + "..."
            return candidate

        return None

    except Exception as e:
        # print(f"⚠️  Error reading {os.path.basename(pdf_path)}: {e}")
        return None

def update_md_file(folder_path, abstract_text):
    index_file = os.path.join(folder_path, 'index.md')
    if not os.path.exists(index_file):
        return False

    with open(index_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    updated = False
    found_abstract_key = False

    for line in lines:
        if line.strip().startswith('abstract:'):
            found_abstract_key = True
            # Ενημερώνουμε ΜΟΝΟ αν είναι κενό
            if line.strip() in ['abstract: ""', 'abstract:', "abstract: ''"]:
                new_lines.append(f'abstract: "{abstract_text}"\n')
                updated = True
            else:
                new_lines.append(line) # Κρατάμε το υπάρχον
        else:
            new_lines.append(line)

    # Αν δεν υπάρχει καν το κλειδί abstract, το προσθέτουμε στο τέλος του YAML header
    if not found_abstract_key:
        # Βρίσκουμε το δεύτερο '---'
        dash_counts = 0
        inserted = False
        final_lines = []
        for l in new_lines:
            if l.strip() == '---':
                dash_counts += 1
                if dash_counts == 2 and not inserted:
                    final_lines.append(f'abstract: "{abstract_text}"\n')
                    inserted = True
            final_lines.append(l)
        new_lines = final_lines
        updated = True

    if updated:
        with open(index_file, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        return True
    return False

def main():
    print(f"🚀 Έκδοση 2: Σάρωση για PDFs στο {PUBLICATION_DIR}...")
    count = 0
    
    for folder_name in os.listdir(PUBLICATION_DIR):
        folder_path = os.path.join(PUBLICATION_DIR, folder_name)
        if not os.path.isdir(folder_path): continue

        pdf_path = os.path.join(folder_path, 'paper.pdf')
        
        if os.path.exists(pdf_path):
            abstract = extract_abstract_smart(pdf_path)
            
            if abstract:
                if update_md_file(folder_path, abstract):
                    print(f"✅ {folder_name}: Διορθώθηκε ({len(abstract)} chars)")
                    count += 1
            else:
                pass
                # print(f"🔸 {folder_name}: Ακόμα δεν βρέθηκε (Ίσως είναι εικόνα;)")

    print("-" * 30)
    print(f"🎉 Προστέθηκαν περιλήψεις σε {count} ακόμη δημοσιεύσεις!")

if __name__ == "__main__":
    main()

import os
import re
from pypdf import PdfReader

# --- ΡΥΘΜΙΣΕΙΣ ---
PUBLICATION_DIR = 'content/publication/'

def clean_text(text):
    if not text: return ""
    text = text.replace('\n', ' ').replace('\r', '')
    text = re.sub(r'\s+', ' ', text) # Πολλαπλά κενά
    text = text.replace('"', "'")    # Quotes που χαλάνε το YAML
    return text.strip()

def get_intro_fallback(text):
    """
    Στρατηγική:
    1. Ψάχνει 'Introduction'.
    2. Αν δεν βρει, ψάχνει το τέλος του 'Abstract'.
    3. Αν δεν βρει, παίρνει χύμα κείμενο από τη μέση της 1ης σελίδας.
    """
    # 1. Προσπάθεια για Introduction
    match = re.search(r'(?i)(?:introduction|I\.\s*INTRODUCTION)', text)
    if match:
        start = match.end()
        return clean_text(text[start : start + 1500]) + "..."
    
    # 2. Προσπάθεια μετά το Abstract
    match = re.search(r'(?i)abstract', text)
    if match:
        start = match.end() + 200 # Πηδάμε λίγο κείμενο (το abstract)
        return clean_text(text[start : start + 1500]) + "..."

    # 3. Fallback: Πάρε από τον χαρακτήρα 1000 και μετά
    if len(text) > 2000:
        return clean_text(text[1000:2500]) + "..."
    
    return None

def get_conclusion_fallback(text):
    """
    Στρατηγική:
    1. Βρες τα 'References'.
    2. Πάρε τα 1500 γράμματα ΠΡΙΝ από αυτά.
    """
    # Ψάχνουμε References ή Bibliography
    match = re.search(r'(?i)(?:references|bibliography|R\s*E\s*F\s*E\s*R\s*E\s*N\s*C\s*E\s*S)', text)
    
    if match:
        end = match.start()
        start = max(0, end - 1500)
        content = text[start:end]
        
        # Προσπάθεια να βρούμε την αρχή της παραγράφου "Conclusion" μέσα σε αυτό το κομμάτι
        con_match = re.search(r'(?i)(?:conclusion|concluding|summary)', content)
        if con_match:
            return clean_text(content[con_match.end():])
        
        # Αν δεν βρούμε τη λέξη, επιστρέφουμε το κομμάτι ως έχει (καλύτερα από το τίποτα)
        return clean_text(content)
    
    # Fallback: Πάρε τα τελευταία 1500 γράμματα
    return clean_text(text[-1500:])

def analyze_pdf_vacuum(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        
        # Κείμενο Αρχής (Σελ 1-2)
        start_text = ""
        for i in range(min(2, len(reader.pages))):
            start_text += reader.pages[i].extract_text() + " "
            
        # Κείμενο Τέλους (Τελευταία Σελίδα)
        end_text = ""
        if len(reader.pages) > 0:
            end_text = reader.pages[-1].extract_text()
            # Αν η τελευταία σελίδα είναι μόνο References, πάρε και την προτελευταία
            if len(end_text) < 500 and len(reader.pages) > 1:
                end_text = reader.pages[-2].extract_text() + " " + end_text

        data = {}
        
        # Λήψη με Fallback
        intro = get_intro_fallback(start_text)
        conclusion = get_conclusion_fallback(end_text)

        if intro and len(intro) > 100: data['intro'] = intro
        if conclusion and len(conclusion) > 100: data['conclusion'] = conclusion
        
        return data

    except Exception as e:
        print(f"⚠️ Error: {e}")
        return {}

def update_md(folder_path, data):
    index_file = os.path.join(folder_path, 'index.md')
    if not os.path.exists(index_file): return False

    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = ""
    updated = False

    # Προσθήκη Intro
    if data.get('intro') and "## Introduction" not in content:
        new_content += f"\n\n## Introduction\n\n{data['intro']}\n"
        updated = True

    # Προσθήκη Conclusion
    if data.get('conclusion') and "## Conclusion" not in content:
        new_content += f"\n\n## Conclusion\n\n{data['conclusion']}\n"
        updated = True

    if updated:
        with open(index_file, 'a', encoding='utf-8') as f:
            f.write(new_content)
        return True
    
    return False

def main():
    print(f"🧹 Έναρξη 'Vacuum' Extraction...")
    count = 0
    
    for folder_name in os.listdir(PUBLICATION_DIR):
        folder_path = os.path.join(PUBLICATION_DIR, folder_name)
        if not os.path.isdir(folder_path): continue
        
        pdf_path = os.path.join(folder_path, 'paper.pdf')
        
        if os.path.exists(pdf_path):
            data = analyze_pdf_vacuum(pdf_path)
            
            if update_md(folder_path, data):
                print(f"✅ {folder_name}: Ενημερώθηκε!")
                count += 1
            else:
                pass
                # print(f"🔸 {folder_name}: Καμία αλλαγή.")

    print("-" * 30)
    print(f"🎉 Ενημερώθηκαν {count} αρχεία.")

if __name__ == "__main__":
    main()

import os
import re
from pypdf import PdfReader

# --- ΡΥΘΜΙΣΕΙΣ ---
PUBLICATION_DIR = 'content/publication/'

# Χάρτης συμβόλων: Unicode -> LaTeX
UNICODE_TO_LATEX = {
    # Ελληνικά πεζά
    'α': r'\alpha', 'β': r'\beta', 'γ': r'\gamma', 'δ': r'\delta', 'ϵ': r'\epsilon',
    'ε': r'\varepsilon', 'ζ': r'\zeta', 'η': r'\eta', 'θ': r'\theta', 'ι': r'\iota',
    'κ': r'\kappa', 'λ': r'\lambda', 'μ': r'\mu', 'ν': r'\nu', 'ξ': r'\xi',
    'π': r'\pi', 'ρ': r'\rho', 'σ': r'\sigma', 'τ': r'\tau', 'υ': r'\upsilon',
    'φ': r'\phi', 'χ': r'\chi', 'ψ': r'\psi', 'ω': r'\omega',
    # Ελληνικά κεφαλαία
    'Γ': r'\Gamma', 'Δ': r'\Delta', 'Θ': r'\Theta', 'Λ': r'\Lambda', 'Ξ': r'\Xi',
    'Π': r'\Pi', 'Σ': r'\Sigma', 'Υ': r'\Upsilon', 'Φ': r'\Phi', 'Ψ': r'\Psi', 'Ω': r'\Omega',
    # Μαθηματικά Σύμβολα
    '×': r'\times', '÷': r'\div', '±': r'\pm', '∓': r'\mp',
    '≤': r'\le', '≥': r'\ge', '≠': r'\neq', '≈': r'\approx',
    '∈': r'\in', '∉': r'\notin', '⊂': r'\subset', '⊃': r'\supset',
    '∪': r'\cup', '∩': r'\cap', '∞': r'\infty', '∇': r'\nabla',
    '∂': r'\partial', '∑': r'\sum', '∏': r'\prod', '∫': r'\int',
    '→': r'\rightarrow', '←': r'\leftarrow', '⇒': r'\Rightarrow',
    '∀': r'\forall', '∃': r'\exists', '∅': r'\emptyset'
}

def clean_text(text):
    if not text: return ""
    text = text.replace('\n', ' ').replace('\r', '')
    text = re.sub(r'\s+', ' ', text)
    text = text.replace('"', "'") # Quotes που χαλάνε το YAML
    return text.strip()

def fix_math_symbols(text):
    """
    Ψάχνει για μαθηματικά σύμβολα στο κείμενο και τα βάζει σε LaTeX math mode ($...$)
    """
    if not text: return None
    
    # 1. Αντικατάσταση Unicode με LaTeX
    for char, latex in UNICODE_TO_LATEX.items():
        if char in text:
            # Βάζουμε κενά γύρω γύρω για ασφάλεια
            text = text.replace(char, f" ${latex}$ ")

    # 2. Μικροδιορθώσεις εμφάνισης (να μην υπάρχουν διπλά κενά μέσα στα $)
    text = re.sub(r'\$\s+\\', r'$\\' , text) 
    text = re.sub(r'\s+\$', r'$', text)
    
    # 3. Διόρθωση συχνών λαθών PDF OCR
    text = text.replace("ﬁ", "fi").replace("ﬂ", "fl")
    
    return text

def extract_section_strict(text, section_name):
    """Αυστηρή εξαγωγή: Ψάχνει Header -> Stop Word"""
    # Regex για τον τίτλο (π.χ. "1. Introduction" ή "Introduction")
    match = re.search(fr'(?i)(?:[0-9IVX]+\.?\s*)?{section_name}', text)
    if not match: return None
    
    start = match.end()
    remaining = text[start:]
    
    # Πού σταματάμε; (Στο επόμενο Section Header ή References)
    stop_match = re.search(r'(?i)(?:[0-9IVX]+\.?\s*)?(?:Conclusion|Reference|Bibliograph|Acknowledgment|System Model|II\.|III\.)', remaining)
    
    if stop_match:
        end = stop_match.start()
    else:
        end = min(len(remaining), 2500) # Αν δεν βρει τέλος, κόψε στους 2500 chars
    
    raw_content = remaining[:end].strip()
    
    # Καθαρισμός και Math Fixing
    return fix_math_symbols(clean_text(raw_content))

def analyze_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        full_text = ""
        
        # Διαβάζουμε όλο το PDF για να είμαστε σίγουροι
        for page in reader.pages:
            full_text += page.extract_text() + " "

        data = {}
        
        # 1. Intro
        intro = extract_section_strict(full_text, "Introduction")
        if intro and len(intro) > 100: 
            data['intro'] = intro
        
        # 2. Conclusion (Ψάχνουμε και για Concluding Remarks)
        conclusion = extract_section_strict(full_text, "Conclusion")
        if not conclusion:
            conclusion = extract_section_strict(full_text, "Concluding Remarks")
            
        if conclusion and len(conclusion) > 100: 
            data['conclusion'] = conclusion
        
        return data
    except Exception as e:
        print(f"⚠️ Error: {e}")
        return {}

def update_md(folder_path, data):
    index_file = os.path.join(folder_path, 'index.md')
    if not os.path.exists(index_file): return False
    
    # Διαβάζουμε το αρχείο
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Καθαρισμός παλιών (Trash) Sections
    if "## Introduction" in content:
        content = content.split("## Introduction")[0].strip()
    elif "## Conclusion" in content:
        # Αν υπάρχει Conclusion χωρίς Intro (σπάνιο αλλά πιθανό)
        content = content.split("## Conclusion")[0].strip()

    new_content = content + "\n"
    updated = False

    if data.get('intro'):
        new_content += f"\n\n## Introduction\n\n{data['intro']}\n"
        updated = True
        
    if data.get('conclusion'):
        new_content += f"\n\n## Conclusion\n\n{data['conclusion']}\n"
        updated = True

    # Γράφουμε μόνο αν βρήκαμε κάτι νέο
    if updated:
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    print(f"🧮 Parsing Math & Text from PDFs (Strict Mode)...")
    count = 0
    for folder_name in os.listdir(PUBLICATION_DIR):
        folder_path = os.path.join(PUBLICATION_DIR, folder_name)
        if not os.path.isdir(folder_path): continue
        
        pdf_path = os.path.join(folder_path, 'paper.pdf')
        if os.path.exists(pdf_path):
            data = analyze_pdf(pdf_path)
            if update_md(folder_path, data):
                print(f"✅ {folder_name}: Updated with math symbols!")
                count += 1
            else:
                pass
                # print(f"🔸 {folder_name}: No valid sections found.")
                
    print(f"🎉 Processed {count} papers.")

if __name__ == "__main__":
    main()

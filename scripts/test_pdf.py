import os
from pypdf import PdfReader

# --- Άλλαξε αυτό με έναν φάκελο που υπάρχει ---
TEST_FILE = 'content/publication/vlachos-enabling-2026/paper.pdf'

def test_read():
    if not os.path.exists(TEST_FILE):
        print("❌ Το αρχείο δεν βρέθηκε. Άλλαξε τη διαδρομή στο script.")
        return

    reader = PdfReader(TEST_FILE)
    print(f"📄 Σελίδες: {len(reader.pages)}")
    
    # Διάβασε την 1η σελίδα
    text = reader.pages[0].extract_text()
    
    print("\n--- ΚΕΙΜΕΝΟ ΠΟΥ ΒΛΕΠΩ ---")
    print(text[:500]) # Τύπωσε τους πρώτους 500 χαρακτήρες
    print("--------------------------\n")
    
    if "Abstract" in text or "ABSTRACT" in text:
        print("✅ Βρήκα τη λέξη 'Abstract'")
    else:
        print("❌ ΔΕΝ βρήκα τη λέξη 'Abstract'. (Ίσως είναι εικόνα;)")

if __name__ == "__main__":
    test_read()

import os

# --- ΡΥΘΜΙΣΕΙΣ ---
PUBLICATION_DIR = 'content/publication/'

def clear_body_content(folder_path):
    index_file = os.path.join(folder_path, 'index.md')
    if not os.path.exists(index_file): return False

    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Το Hugo αρχείο χωρίζεται με '---'. 
    # Το μέρος [1] είναι τα metadata (εκεί είναι το abstract).
    # Το μέρος [2] και μετά είναι το κείμενο (το trash που θέλουμε να σβήσουμε).
    parts = content.split('---')

    if len(parts) < 3:
        # Αν δεν έχει 3 μέρη, σημαίνει ότι δεν έχει body text, άρα είναι ήδη καθαρό.
        return False

    # Ανακατασκευή: Κρατάμε μόνο το YAML Header
    # parts[0] είναι κενό (πριν το πρώτο ---)
    # parts[1] είναι το YAML
    new_content = '---' + parts[1] + '---\n'

    # Αν το περιεχόμενο είναι ίδιο, δεν κάνουμε εγγραφή
    if new_content == content:
        return False

    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def main():
    print(f"🧹 Έναρξη Καθαρισμού (Hard Reset)...")
    count = 0
    
    for folder_name in os.listdir(PUBLICATION_DIR):
        folder_path = os.path.join(PUBLICATION_DIR, folder_name)
        if not os.path.isdir(folder_path): continue
        
        if clear_body_content(folder_path):
            print(f"🗑️  {folder_name}: Καθαρίστηκε (Διεγράφη το Body Text)")
            count += 1
        else:
            # print(f"✨ {folder_name}: Ήταν ήδη καθαρό.")
            pass

    print("-" * 30)
    print(f"🎉 Ολοκληρώθηκε! Καθαρίστηκαν {count} αρχεία.")
    print("Τώρα τα αρχεία περιέχουν μόνο Τίτλους, Metadata και Abstract.")

if __name__ == "__main__":
    main()

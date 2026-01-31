import os
import urllib.request
from PIL import Image, ImageDraw, ImageFont

def find_system_font():
    """
    Intelligently searches for a Bold font on Linux/Mac/Windows.
    Returns the path to the font file.
    """
    # 1. Common specific paths
    common_paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", # Linux Standard
        "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf",             # Arch/Gentoo
        "/usr/share/fonts/liberation/LiberationSans-Bold.ttf",  # Linux Alt
        "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf",  # Linux Alt
        "C:\\Windows\\Fonts\\Arialbd.ttf",                      # Windows
        "/Library/Fonts/Arial Bold.ttf",                        # Mac
        "/System/Library/Fonts/HelveticaNeue-Bold.otf"          # Mac Alt
    ]
    
    for path in common_paths:
        if os.path.exists(path):
            print(f"✅ Found system font: {path}")
            return path

    # 2. Generic Search (if specific paths fail)
    # Recursively look for ANY file with "Bold" in the name in standard font dirs
    search_dirs = ["/usr/share/fonts", "/usr/local/share/fonts", os.path.expanduser("~/.local/share/fonts")]
    print("🔍 Searching system directories for any Bold font...")
    
    for d in search_dirs:
        if os.path.exists(d):
            for root, dirs, files in os.walk(d):
                for file in files:
                    if "Bold" in file and (file.endswith(".ttf") or file.endswith(".otf")):
                        full_path = os.path.join(root, file)
                        print(f"✅ Found generic system font: {full_path}")
                        return full_path
    
    return None

def download_fallback_font():
    """Attempts to download a font if local search fails."""
    font_filename = "temp_font_bold.ttf"
    # Using the OFL path which is standard for Google Fonts
    url = "https://raw.githubusercontent.com/google/fonts/main/ofl/opensans/OpenSans-Bold.ttf"
    
    print(f"⬇️  System font not found. Downloading from: {url}")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(font_filename, 'wb') as out_file:
            out_file.write(response.read())
        print("✅ Download successful.")
        return font_filename
    except Exception as e:
        print(f"❌ Download failed: {e}")
        return None

def create_icon():
    # --- Settings ---
    FILENAME = "icon.png"
    SIZE = (512, 512)
    BG_COLOR = "#1a1a1a"   # Matte Black
    TEXT_COLOR = "#ffffff" # Pure White
    TEXT = "EV"
    CORNER_RADIUS = 90
    FONT_SIZE = 360       # Large size

    # --- Find a Font ---
    font_path = find_system_font()
    
    if not font_path:
        font_path = download_fallback_font()

    # --- Create Image ---
    img = Image.new('RGBA', SIZE, (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    # Draw Background
    d.rounded_rectangle([(0, 0), SIZE], radius=CORNER_RADIUS, fill=BG_COLOR)

    # Load Font
    try:
        if font_path:
            font = ImageFont.truetype(font_path, FONT_SIZE)
        else:
            raise Exception("No font available")
    except:
        print("⚠️  Warning: Using default pixel font (might look small).")
        font = ImageFont.load_default()
        # Reset text to center simply if we are using the tiny default font
        w, h = d.textsize(TEXT, font=font)
        d.text(((512-w)/2, (512-h)/2), TEXT, fill=TEXT_COLOR, font=font)
        img.save(FILENAME)
        return

    # --- Smart Centering ---
    try:
        left, top, right, bottom = d.textbbox((0, 0), TEXT, font=font)
        text_w = right - left
        text_h = bottom - top
        x = (SIZE[0] - text_w) / 2 - left
        y = (SIZE[1] - text_h) / 2 - top - 25 # Visual adjustment
    except AttributeError:
        # Fallback for older Pillow versions
        text_w, text_h = d.textsize(TEXT, font=font)
        x = (SIZE[0] - text_w) / 2
        y = (SIZE[1] - text_h) / 2 - 35

    d.text((x, y), TEXT, fill=TEXT_COLOR, font=font)

    # --- Save ---
    img.save(FILENAME)
    
    # Clean up temp file if we downloaded one
    if font_path == "temp_font_bold.ttf" and os.path.exists(font_path):
        os.remove(font_path)

    print(f"✅ Success! Created {FILENAME}")

if __name__ == "__main__":
    create_icon()

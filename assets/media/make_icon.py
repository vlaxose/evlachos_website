from PIL import Image, ImageDraw, ImageFont
import os

def create_icon(filename, bg_color, text_color, style="simple"):
    # Create a 512x512 image (standard size for Hugo/Web icons)
    size = (512, 512)
    img = Image.new('RGB', size, color=bg_color)
    d = ImageDraw.Draw(img)
    
    # Try to use a sans-serif font, fallback to default if not found
    try:
        # This path works on most Linux systems (DejaVuSans is usually installed)
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 280)
    except:
        try:
            # Common fallback
            font = ImageFont.truetype("arial.ttf", 280)
        except:
            # Ultimate fallback
            font = ImageFont.load_default()

    text = "EV"
    
    # Calculate text position to center it perfectly
    # Using textbbox (newer Pillow versions) or textsize (older)
    try:
        left, top, right, bottom = d.textbbox((0, 0), text, font=font)
        text_width = right - left
        text_height = bottom - top
    except AttributeError:
        text_width, text_height = d.textsize(text, font=font)

    x = (size[0] - text_width) / 2
    y = (size[1] - text_height) / 2 - 20 # slight upward shift for visual balance

    # Style 1: Simple Circle
    if style == "circle":
        # Draw a circle container
        d.ellipse([20, 20, 492, 492], outline=text_color, width=20)
    
    # Style 2: Tech/Signal Dots (Abstract)
    elif style == "tech":
        # Draw small "nodes" connected to the letters
        d.ellipse([40, 40, 80, 80], fill=text_color)
        d.ellipse([432, 432, 472, 472], fill=text_color)
        d.line([80, 80, 150, 150], fill=text_color, width=10)

    # Draw the text
    d.text((x, y), text, fill=text_color, font=font)
    
    # Save
    img.save(filename)
    print(f"Created {filename}")

# --- Generate 3 Options ---

# Option 1: Dark Mode (Classic Academic)
# Dark Grey Background, White Text
create_icon("icon_dark.png", "#2b2b2b", "#ffffff", style="simple")

# Option 2: Light Mode (Clean & Modern)
# White Background, Navy Blue Text (matches typical academic themes)
create_icon("icon_light.png", "#ffffff", "#003366", style="circle")

# Option 3: "Tech" Style (Signal Processing feel)
# Navy Background, Cyan Text
create_icon("icon_tech.png", "#002b36", "#2aa198", style="tech")

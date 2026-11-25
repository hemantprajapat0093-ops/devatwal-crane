import os
from PIL import ImageFont

# Check fonts in C:\Windows\Fonts
font_dir = r"C:\Windows\Fonts"
hindi_fonts = []

for f in os.listdir(font_dir):
    f_lower = f.lower()
    if any(k in f_lower for k in ["mangal", "aparaj", "nirmala", "utsaah", "kokila", "devanagari", "arial", "segoe"]):
        full_p = os.path.join(font_dir, f)
        hindi_fonts.append((f, full_p))

print("Found fonts:")
for name, path in hindi_fonts:
    print(f" - {name}: {path}")

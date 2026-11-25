import glob, os

all_fonts = glob.glob(r"C:\Windows\Fonts\*.ttf") + glob.glob(r"C:\Windows\Fonts\*.otf")
print(f"Total fonts in Windows/Fonts: {len(all_fonts)}")
for f in all_fonts[:20]:
    print(os.path.basename(f))

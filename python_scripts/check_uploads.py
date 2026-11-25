import glob, os
from PIL import Image

for f in sorted(glob.glob(r'C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\*.jpg')):
    im = Image.open(f)
    print(os.path.basename(f), im.size)

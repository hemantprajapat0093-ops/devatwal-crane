import glob, os
from PIL import Image

user_dir = r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded"
for f in sorted(glob.glob(os.path.join(user_dir, "*.jpg"))):
    im = Image.open(f)
    base = os.path.splitext(os.path.basename(f))[0]
    thumb = im.copy()
    thumb.thumbnail((300, 300))
    thumb.save(rf"C:\Users\heman\Desktop\devatwal-crane-service\public\images\thumb_{base}.jpg")
print("Generated all thumbnails!")

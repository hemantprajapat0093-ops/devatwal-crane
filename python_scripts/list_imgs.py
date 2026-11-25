import os, glob
from PIL import Image

for p in glob.glob(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\*.jpg"):
    name = os.path.basename(p)
    im = Image.open(p)
    print(f"{name:35s}: {im.size}")

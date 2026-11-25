import glob
from PIL import Image

for p in glob.glob("C:/Users/heman/Desktop/devatwal-crane-service/public/images/*.*"):
    try:
        im = Image.open(p)
        print(f"{p.split('/')[-1]}: {im.size}")
    except:
        pass

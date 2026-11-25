from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_perfect_clean_backdrop.jpg")
arr = np.array(im)
br = arr[460:, 1050:, :3]
h, w, _ = br.shape

pts = []
for y in range(h):
    for x in range(w):
        r, g, b = int(br[y, x, 0]), int(br[y, x, 1]), int(br[y, x, 2])
        if (g > 80 and g > r + 15) or (b > 90 and b > r + 15):
            pts.append((x + 1050, y + 460, (r, g, b)))

print("Total points:", len(pts))
for p in pts[:10]:
    print("Pt:", p[0], p[1], "Color:", p[2])

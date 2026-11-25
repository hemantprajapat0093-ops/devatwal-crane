from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_perfect_clean_backdrop.jpg")
arr = np.array(im)
br = arr[480:, 1100:, :3]
h, w, _ = br.shape

count = 0
for y in range(h):
    for x in range(w):
        r, g, b = int(br[y, x, 0]), int(br[y, x, 1]), int(br[y, x, 2])
        if (g > 80 and g > r + 15) or (b > 90 and b > r + 15):
            count += 1

print("Green or blue pixel count in x>1100, y>480:", count)

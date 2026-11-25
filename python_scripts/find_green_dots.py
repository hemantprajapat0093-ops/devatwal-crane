from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\debug_slab_detail.jpg")
arr = np.array(im)
h, w, _ = arr.shape
# Crop was (1050, 150, 1400, 400).
# Let's find green/cyan dots (G > 180, B > 180, R < 100 or G > R+50 and G > B)
green_dots = []
for y in range(h):
    for x in range(w):
        r, g, b = arr[y, x, :3]
        if (g > 150 and g > r + 40 and g > b + 20) or (b > 180 and g > 150 and r < 100):
            green_dots.append((x + 1050, y + 150, (r, g, b)))

print(f"Found {len(green_dots)} green/cyan flare dots near slab.")
if green_dots:
    for p in green_dots[:10]:
        print("Dot at:", p[0], p[1], "Color:", p[2])

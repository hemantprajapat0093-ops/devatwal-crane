from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\exact_reference_hero.jpg")
arr = np.array(im)

# Let's find bright yellow pixels (like in "Go Futer.") between y=200 and y=350
yellow_pixels = []
for y in range(150, 400):
    for x in range(400, 800):
        r, g, b = arr[y, x, :3]
        if r > 180 and g > 130 and b < 80: # yellow text
            yellow_pixels.append((x, y))

if yellow_pixels:
    max_x = max(p[0] for p in yellow_pixels)
    min_x = min(p[0] for p in yellow_pixels)
    print(f"Yellow text found between x={min_x} and x={max_x}!")
else:
    print("No yellow pixels found in that range.")

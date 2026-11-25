from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\debug_bottom_right.jpg")
arr = np.array(im)
h, w, _ = arr.shape
print(f"debug_bottom_right size: {w}x{h}")

# Check for green or blue/cyan pixels in debug_bottom_right:
# The crop was from x=1100 to 1419, y=500 to 689 in exact_reference_hero.jpg
green_or_blue = []
for y in range(h):
    for x in range(w):
        r, g, b = int(arr[y, x, 0]), int(arr[y, x, 1]), int(arr[y, x, 2])
        # Check if blue (B > 120 and B > R+40) or green (G > 120 and G > R+40)
        if (b > 100 and b > r + 30 and b > g) or (g > 100 and g > r + 30 and g > b):
            green_or_blue.append((x, y, (r, g, b)))

print(f"Found {len(green_or_blue)} green/blue pixels in bottom right crop.")
if green_or_blue:
    print("Sample:", green_or_blue[:5])

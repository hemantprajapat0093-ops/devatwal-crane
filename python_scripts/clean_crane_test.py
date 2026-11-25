from PIL import Image, ImageFilter
import numpy as np

src = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_0_1795627290194.jpg")
w, h = src.size
arr = np.array(src).copy()

# Let's inspect the 3 areas closely:
# 1. Top left (y: 20 to 120, x: 0 to 60):
# In this area, we have sky and clouds.
# Let's see what arr[20:120, 65:80] looks like:
sky_patch = arr[20:120, 60:80]
for y in range(25, 120):
    for x in range(0, 60):
        # Sample smoothly from x + 60 with slight jitter or horizontal gradient
        arr[y, x] = arr[y, min(w - 1, x + 62)]

# 2. Mid left (y: 360 to 500, x: 0 to 45):
# Between y: 360 to 440, it's sky/horizon clouds.
# Between y: 440 to 500, it's the top of the rear tire / fender.
# In src, what was the text? It was "...r." in yellow at y: 380-490, x: 0-40.
# Let's look at the color at x=45..60 for these rows:
for y in range(365, 435):
    for x in range(0, 45):
        arr[y, x] = arr[y, min(w - 1, x + 48)]

# At y: 435 to 495, let's see what is at x=45..60:
# Is it the tire or the yellow frame?
for y in range(435, 495):
    for x in range(0, 35):
        # Check if row at x=40 is yellow or dark
        arr[y, x] = arr[y, min(w - 1, x + 38)]

# 3. Bottom left (y: 560 to h, x: 0 to 35):
# It's ground gravel/dirt.
for y in range(560, h):
    for x in range(0, 35):
        arr[y, x] = arr[y, min(w - 1, x + 38)]

# Neutralize bottom right green/blue artifacts if any
for y in range(int(h * 0.75), h):
    for x in range(int(w * 0.8), w):
        r, g, b = int(arr[y, x, 0]), int(arr[y, x, 1]), int(arr[y, x, 2])
        if (g > 80 and g > r + 15) or (b > 90 and b > r + 15):
            val = max(24, min(140, r))
            arr[y, x, 0] = val
            arr[y, x, 1] = max(18, val - 8)
            arr[y, x, 2] = max(14, val - 14)

cleaned = Image.fromarray(arr)

# Save intermediate cleaned
cleaned.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_cleaned_base.jpg", quality=98)
print("Base cleaned saved!")

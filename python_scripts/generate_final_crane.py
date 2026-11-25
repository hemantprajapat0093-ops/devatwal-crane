from PIL import Image, ImageFilter
import numpy as np

# Load the exact crane photo uploaded by Hemant sir
src_path = r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_0_1795627290194.jpg"
im = Image.open(src_path)
w, h = im.size
print(f"Source size: {w}x{h}")

arr = np.array(im).copy()

# 1. Clean the 3 edge snippets on the left (x: 0 to 65)
# Snippet 1: "...t Rating" (x: 0 to 60, y: 30 to 115) -> sample sky from (y, x + 65)
for y in range(30, 115):
    for x in range(0, 60):
        # sample smoothly
        arr[y, x] = arr[y, min(w - 1, x + 65)]

# Snippet 2: "...r." (x: 0 to 45, y: 365 to 495)
# Between y: 365 and 435 is sunset sky above the rear fender
for y in range(365, 435):
    for x in range(0, 45):
        arr[y, x] = arr[y, min(w - 1, x + 48)]

# Between y: 435 and 495 is the tire / fender contour
for y in range(435, 495):
    for x in range(0, 35):
        arr[y, x] = arr[y, min(w - 1, x + 38)]

# Snippet 3: "...le" (x: 0 to 35, y: 560 to h) -> sample ground from (y, x + 38)
for y in range(560, h):
    for x in range(0, 35):
        arr[y, x] = arr[y, min(w - 1, x + 38)]

# 2. Check and neutralize any green or blue artifacts in bottom right
for y in range(int(h * 0.75), h):
    for x in range(int(w * 0.8), w):
        r, g, b = int(arr[y, x, 0]), int(arr[y, x, 1]), int(arr[y, x, 2])
        if (g > 80 and g > r + 15) or (b > 90 and b > r + 15):
            val = max(24, min(140, r))
            arr[y, x, 0] = val
            arr[y, x, 1] = max(18, val - 8)
            arr[y, x, 2] = max(14, val - 14)

cleaned = Image.fromarray(arr)

# 3. Enhance resolution & clarity: upscale with LANCZOS to 1600px wide for ultra-crisp display
target_w = 1600
target_h = int(h * (target_w / w))
crane_hd = cleaned.resize((target_w, target_h), Image.Resampling.LANCZOS)

# Apply subtle unsharp mask to bring out crisp details of the hydraulic rams, cables, and tires
crane_hd = crane_hd.filter(ImageFilter.UnsharpMask(radius=1.2, percent=125, threshold=2))

out_path = r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_crane_full_view.jpg"
crane_hd.save(out_path, quality=98)
print(f"Successfully generated ultra-HD crane image: {out_path} ({target_w}x{target_h})!")

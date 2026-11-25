from PIL import Image, ImageFilter
import numpy as np

# Load the exact crane photo uploaded by Hemant sir
im = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_0_1795627290194.jpg")
w, h = im.size
print(f"Original user crane image: {w}x{h}")

arr = np.array(im).copy()

# 1. Clean the 3 edge snippets on the left (x: 0 to 65)
# Snippet 1: "...t Rating" (x: 0 to 65, y: 35 to 115) -> sample sky from (y, x + 70)
for y in range(35, 115):
    for x in range(0, 65):
        arr[y, x] = arr[y, min(w - 1, x + 70)]

# Snippet 2: "...r." (x: 0 to 45, y: 370 to 495) -> sample sky from (y, x + 50)
for y in range(370, 495):
    for x in range(0, 48):
        arr[y, x] = arr[y, min(w - 1, x + 50)]

# Snippet 3: "...le" (x: 0 to 30, y: 565 to 603) -> sample ground from (y, x + 35)
for y in range(565, h):
    for x in range(0, 35):
        arr[y, x] = arr[y, min(w - 1, x + 35)]

# 2. Check and neutralize any green or blue artifacts in bottom right
for y in range(int(h * 0.8), h):
    for x in range(int(w * 0.8), w):
        r, g, b = int(arr[y, x, 0]), int(arr[y, x, 1]), int(arr[y, x, 2])
        if (g > 80 and g > r + 15) or (b > 90 and b > r + 15):
            val = max(24, min(140, r))
            arr[y, x, 0] = val
            arr[y, x, 1] = max(18, val - 8)
            arr[y, x, 2] = max(14, val - 14)

cleaned = Image.fromarray(arr)

# 3. Enhance resolution & clarity: upscale with LANCZOS to 1400px wide (crisp 4K look)
target_w = 1400
target_h = int(h * (target_w / w))
crane_hd = cleaned.resize((target_w, target_h), Image.Resampling.LANCZOS)

# Apply subtle unsharp mask to bring out every detail of the hydraulic rams, cables, and tires
crane_hd = crane_hd.filter(ImageFilter.UnsharpMask(radius=1.5, percent=130, threshold=2))

crane_hd.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_crane_full_view.jpg", quality=98)
print(f"Saved hero_crane_full_view.jpg ({target_w}x{target_h})!")

from PIL import Image, ImageFilter
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\exact_reference_hero.jpg")
w, h = im.size
arr = np.array(im).copy()

# 1. Clean Top Area (y: 0 to 125) across entire width
for y in range(125):
    for x in range(w):
        factor = min(1.0, max(0.0, (125 - y) / 35.0))
        r, g, b = 7, 13, 24
        orig = arr[y, x, :3]
        arr[y, x, 0] = int(r * factor + orig[0] * (1 - factor))
        arr[y, x, 1] = int(g * factor + orig[1] * (1 - factor))
        arr[y, x, 2] = int(b * factor + orig[2] * (1 - factor))

# 2. Clean Left Side (x: 0 to 730)
for x in range(730):
    fade = min(1.0, max(0.0, (730 - x) / 30.0))
    if x < 700:
        fade = 1.0
    for y in range(h):
        y_ratio = y / h
        r_target = int(7 * (1 - y_ratio) + 4 * y_ratio)
        g_target = int(14 * (1 - y_ratio) + 8 * y_ratio)
        b_target = int(28 * (1 - y_ratio) + 16 * y_ratio)
        
        orig = arr[y, x, :3]
        arr[y, x, 0] = int(r_target * fade + orig[0] * (1 - fade))
        arr[y, x, 1] = int(g_target * fade + orig[1] * (1 - fade))
        arr[y, x, 2] = int(b_target * fade + orig[2] * (1 - fade))

# 3. Clean residual "ter." yellow text and swoosh at x: 700 to 880, y: 240 to 460
for y in range(240, 460):
    for x in range(700, 880):
        r, g, b = int(arr[y, x, 0]), int(arr[y, x, 1]), int(arr[y, x, 2])
        is_yellow = (r > 135 and g > 95 and b < 125) or (r > 180 and g > 130 and b < 140)
        is_shadow = (r < 50 and g < 50 and b < 50 and y > 270 and y < 440 and x < 870)
        
        if is_yellow or is_shadow:
            if y < 355:
                ref_y = max(130, y - 50)
                ref_x = min(w - 1, x + 35)
            else:
                ref_y = min(h - 1, y + 40)
                ref_x = min(w - 1, x + 25)
            
            arr[y, x, 0] = arr[ref_y, ref_x, 0]
            arr[y, x, 1] = arr[ref_y, ref_x, 1]
            arr[y, x, 2] = arr[ref_y, ref_x, 2]

# 4. Clean green/cyan flare dots near hoisted slab (x: 1040 to 1160, y: 145 to 235)
for y in range(145, 235):
    for x in range(1040, 1160):
        r, g, b = int(arr[y, x, 0]), int(arr[y, x, 1]), int(arr[y, x, 2])
        if (g > 140 and g > r + 30 and g > b - 15) or (b > 180 and g > 140 and r < 120):
            ref_y = max(130, y - 20)
            ref_x = min(w - 1, x + 30)
            arr[y, x, 0] = arr[ref_y, ref_x, 0]
            arr[y, x, 1] = arr[ref_y, ref_x, 1]
            arr[y, x, 2] = arr[ref_y, ref_x, 2]

# 5. Clean top-right hazard diagonal stripes (x: 1280 to 1419, y: 0 to 140)
for y in range(140):
    for x in range(1280, w):
        factor = min(1.0, max(0.0, (140 - y) / 35.0))
        r, g, b = 7, 13, 24
        orig = arr[y, x, :3]
        arr[y, x, 0] = int(r * factor + orig[0] * (1 - factor))
        arr[y, x, 1] = int(g * factor + orig[1] * (1 - factor))
        arr[y, x, 2] = int(b * factor + orig[2] * (1 - factor))

res = Image.fromarray(arr)

# Apply silky smooth blur to the patch
patch = res.crop((695, 235, 885, 465)).filter(ImageFilter.GaussianBlur(radius=3))
res.paste(patch, (695, 235))

flare_patch = res.crop((1040, 145, 1160, 235)).filter(ImageFilter.GaussianBlur(radius=1.5))
res.paste(flare_patch, (1040, 145))

res.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_perfect_clean_backdrop.jpg", quality=98)
res.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_clean_final.jpg", quality=98)
print("Finished complete cleanup!")

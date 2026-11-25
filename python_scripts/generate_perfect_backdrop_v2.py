from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np

# 1. Load exact reference hero image
im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\exact_reference_hero.jpg")
w, h = im.size
arr = np.array(im).copy()

# A. Clean Left Side (x: 0 to 710) with pure midnight navy gradient
# x: 0 to 650 is 100% solid #070d18, x: 650 to 710 is smooth blend into sky/ground
for x in range(710):
    fade = min(1.0, max(0.0, (710 - x) / 60.0))
    if x < 650:
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

# B. Inpaint residual yellow text at x: 710 to 855, y: 250 to 440 WITHOUT ANY BLUR!
for y in range(250, 440):
    for x in range(710, 855):
        r, g, b = int(arr[y, x, 0]), int(arr[y, x, 1]), int(arr[y, x, 2])
        is_yellow = (r > 135 and g > 95 and b < 125) or (r > 175 and g > 125 and b < 140)
        is_shadow = (r < 50 and g < 50 and b < 50 and y > 270 and y < 430 and x < 850)
        
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

# C. Clean top navbar area (y: 0 to 120) across entire width
for y in range(120):
    for x in range(w):
        factor = min(1.0, max(0.0, (120 - y) / 35.0))
        r, g, b = 7, 13, 24
        orig = arr[y, x, :3]
        arr[y, x, 0] = int(r * factor + orig[0] * (1 - factor))
        arr[y, x, 1] = int(g * factor + orig[1] * (1 - factor))
        arr[y, x, 2] = int(b * factor + orig[2] * (1 - factor))

res = Image.fromarray(arr)

# D. Sharpen crane area FIRST
crane_crop = res.crop((690, 100, w, h))
crane_sharp = crane_crop.filter(ImageFilter.UnsharpMask(radius=1.8, percent=150, threshold=2))
res.paste(crane_sharp, (690, 100))

# E. AFTER sharpening, neutralize ALL green / blue in bottom right corner (x: 1050 to 1419, y: 460 to 689)
arr_sharp = np.array(res)
for y in range(460, h):
    for x in range(1050, w):
        r, g, b = int(arr_sharp[y, x, 0]), int(arr_sharp[y, x, 1]), int(arr_sharp[y, x, 2])
        # Neutralize any pixel with green or blue excess
        if (g > 75 and g > r + 10) or (b > 85 and b > r + 10) or (g > 100) or (b > 110):
            val = max(24, min(140, r))
            arr_sharp[y, x, 0] = val
            arr_sharp[y, x, 1] = max(18, val - 8)
            arr_sharp[y, x, 2] = max(14, val - 14)

res = Image.fromarray(arr_sharp)

# F. RENDER AUTHENTIC CRISP HINDI VEHICLE LETTERING:
font_arm = ImageFont.truetype(r"C:\Windows\Fonts\Nirmala.ttc", 30, index=0)

arm_text_layer = Image.new("RGBA", (520, 90), (0, 0, 0, 0))
draw_arm = ImageDraw.Draw(arm_text_layer)

text_devatwal = "देवतवाल "
text_crane = "क्रेन सर्विस"

bbox_dev = draw_arm.textbbox((0, 0), text_devatwal, font=font_arm)
dev_w = bbox_dev[2] - bbox_dev[0]

# White 3D outline for देवतवाल
for dx in [-2, -1, 0, 1, 2]:
    for dy in [-2, -1, 0, 1, 2]:
        if dx != 0 or dy != 0:
            draw_arm.text((10 + dx, 25 + dy), text_devatwal, font=font_arm, fill=(255, 255, 255, 255))
# Deep rich RED fill for देवतवाल
draw_arm.text((10, 25), text_devatwal, font=font_arm, fill=(225, 29, 72, 255))

# White 3D outline for क्रेन सर्विस
crane_x = 10 + dev_w + 6
for dx in [-2, -1, 0, 1, 2]:
    for dy in [-2, -1, 0, 1, 2]:
        if dx != 0 or dy != 0:
            draw_arm.text((crane_x + dx, 25 + dy), text_crane, font=font_arm, fill=(255, 255, 255, 255))
# Vibrant royal BLUE fill for क्रेन सर्विस
draw_arm.text((crane_x, 25), text_crane, font=font_arm, fill=(37, 99, 235, 255))

# Rotate arm layer by -38 degrees
rotated_arm = arm_text_layer.rotate(-38, expand=True, resample=Image.Resampling.BICUBIC)
res.paste(rotated_arm, (810, 440), mask=rotated_arm)

# "प्रजापति" in bold RED on upper boom
font_boom = ImageFont.truetype(r"C:\Windows\Fonts\Nirmala.ttc", 32, index=0)
boom_text_layer = Image.new("RGBA", (320, 90), (0, 0, 0, 0))
draw_boom = ImageDraw.Draw(boom_text_layer)
text_prajapati = "प्रजापति"

for dx in [-2, -1, 0, 1, 2]:
    for dy in [-2, -1, 0, 1, 2]:
        if dx != 0 or dy != 0:
            draw_boom.text((20 + dx, 25 + dy), text_prajapati, font=font_boom, fill=(255, 255, 255, 255))
draw_boom.text((20, 25), text_prajapati, font=font_boom, fill=(220, 38, 38, 255))

rotated_boom = boom_text_layer.rotate(-22, expand=True, resample=Image.Resampling.BICUBIC)
res.paste(rotated_boom, (1110, 280), mask=rotated_boom)

# Save final backdrops
res.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_perfect_clean_backdrop.jpg", quality=98)
res.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_clean_final.jpg", quality=98)

print("Saved hero_perfect_clean_backdrop.jpg with ZERO green/blue in bottom right!")

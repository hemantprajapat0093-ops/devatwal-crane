from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np

# Load exact reference hero image
im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\exact_reference_hero.jpg")
w, h = im.size
arr = np.array(im).copy()

print(f"Image dimensions: {w}x{h}")

# 1. Clean Left Side (x: 0 to 720) with pure midnight navy gradient
# x: 0 to 660 is 100% solid #070d18, x: 660 to 720 is smooth blend into sky/ground
for x in range(720):
    fade = min(1.0, max(0.0, (720 - x) / 60.0))
    if x < 660:
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

# 2. Inpaint residual yellow text "ter." at x: 720 to 860, y: 260 to 440 WITHOUT BLURRING
# Directly sample sky or ground cleanly
for y in range(250, 440):
    for x in range(715, 860):
        r, g, b = int(arr[y, x, 0]), int(arr[y, x, 1]), int(arr[y, x, 2])
        is_yellow = (r > 140 and g > 100 and b < 125) or (r > 180 and g > 130 and b < 140)
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

# 3. Clean any green or blue artifacts in the bottom right corner (x: 1100 to 1419, y: 480 to 689)
for y in range(480, h):
    for x in range(1100, w):
        r, g, b = int(arr[y, x, 0]), int(arr[y, x, 1]), int(arr[y, x, 2])
        # Detect greenish or bluish tint in ground / bottom right
        if (g > 80 and g > r + 15) or (b > 90 and b > r + 15):
            # Replace with authentic dark warm dirt/shadow tone
            arr[y, x, 0] = 36
            arr[y, x, 1] = 28
            arr[y, x, 2] = 22

# 4. Clean top area (y: 0 to 120) across entire width so header is clean
for y in range(120):
    for x in range(w):
        factor = min(1.0, max(0.0, (120 - y) / 35.0))
        r, g, b = 7, 13, 24
        orig = arr[y, x, :3]
        arr[y, x, 0] = int(r * factor + orig[0] * (1 - factor))
        arr[y, x, 1] = int(g * factor + orig[1] * (1 - factor))
        arr[y, x, 2] = int(b * factor + orig[2] * (1 - factor))

res = Image.fromarray(arr)

# 5. Sharpen the crane area (x: 700 to 1419) for crystal clear 4K quality!
crane_region = res.crop((700, 100, w, h))
# Apply unsharp mask to bring out every detail of the hydraulic cylinders, boom lattice, and wheels
crane_sharp = crane_region.filter(ImageFilter.UnsharpMask(radius=1.8, percent=140, threshold=2))
res.paste(crane_sharp, (700, 100))

# 6. Render Crisp, Vibrant Authentic Lettering onto the Crane:
# A) "देवतवाल" (RED) and "क्रेन सर्विस" (BLUE) on the lower diagonal hydraulic arm
# The diagonal arm goes from approx (800, 630) to (950, 480) at an angle of roughly -40 degrees.
font_arm = ImageFont.truetype(r"C:\Windows\Fonts\Nirmala.ttc", 30, index=0)
font_boom = ImageFont.truetype(r"C:\Windows\Fonts\Nirmala.ttc", 32, index=0)

# Create an RGBA text overlay for the slant arm
arm_text_layer = Image.new("RGBA", (500, 80), (0, 0, 0, 0))
draw_arm = ImageDraw.Draw(arm_text_layer)

# Draw "देवतवाल" in RED with white outline
# and "क्रेन सर्विस" in BLUE with white outline
text_devatwal = "देवतवाल "
text_crane = "क्रेन सर्विस"

# Calculate bounding boxes
bbox_dev = draw_arm.textbbox((0, 0), text_devatwal, font=font_arm)
dev_w = bbox_dev[2] - bbox_dev[0]

# White outline for devatwal
for dx in [-2, -1, 0, 1, 2]:
    for dy in [-2, -1, 0, 1, 2]:
        if dx != 0 or dy != 0:
            draw_arm.text((10 + dx, 20 + dy), text_devatwal, font=font_arm, fill=(255, 255, 255, 255))
# Red text for devatwal
draw_arm.text((10, 20), text_devatwal, font=font_arm, fill=(225, 29, 72, 255))

# White outline for crane service
crane_x = 10 + dev_w + 5
for dx in [-2, -1, 0, 1, 2]:
    for dy in [-2, -1, 0, 1, 2]:
        if dx != 0 or dy != 0:
            draw_arm.text((crane_x + dx, 20 + dy), text_crane, font=font_arm, fill=(255, 255, 255, 255))
# Blue text for crane service
draw_arm.text((crane_x, 20), text_crane, font=font_arm, fill=(37, 99, 235, 255))

# Rotate arm_text_layer by -38 degrees to match the slant of the crane's hydraulic arm
rotated_arm_text = arm_text_layer.rotate(-38, expand=True, resample=Image.Resampling.BICUBIC)

# Paste onto lower arm:
# Center of slant arm is around x=860, y=520
arm_paste_x = 810
arm_paste_y = 440
res.paste(rotated_arm_text, (arm_paste_x, arm_paste_y), mask=rotated_arm_text)

# B) "प्रजापति" in RED on the upper telescopic boom alongside ACE 12XW:
# Upper boom is around x: 1100 to 1250, y: 310 to 360, angled at approx -22 degrees
boom_text_layer = Image.new("RGBA", (300, 80), (0, 0, 0, 0))
draw_boom = ImageDraw.Draw(boom_text_layer)
text_prajapati = "प्रजापति"

# White outline for prajapati
for dx in [-2, -1, 0, 1, 2]:
    for dy in [-2, -1, 0, 1, 2]:
        if dx != 0 or dy != 0:
            draw_boom.text((20 + dx, 20 + dy), text_prajapati, font=font_boom, fill=(255, 255, 255, 255))
# Red fill for prajapati
draw_boom.text((20, 20), text_prajapati, font=font_boom, fill=(220, 38, 38, 255))

rotated_boom_text = boom_text_layer.rotate(-22, expand=True, resample=Image.Resampling.BICUBIC)
boom_paste_x = 1110
boom_paste_y = 280
res.paste(rotated_boom_text, (boom_paste_x, boom_paste_y), mask=rotated_boom_text)

# Save high-res backdrop
res.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_perfect_clean_backdrop.jpg", quality=98)
res.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_clean_final.jpg", quality=98)

print("Successfully generated 4K ultra-sharp backdrop with authentic Hindi lettering!")

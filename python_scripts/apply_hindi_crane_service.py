import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# 1. Load the 2x master banner
path_2x = r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_exact_master_banner_2x.jpg"
im_2x = Image.open(path_2x)
w2, h2 = im_2x.size
print(f"Loaded 2x banner: {w2}x{h2}")

# Convert to OpenCV BGR array
cv_2x = cv2.cvtColor(np.array(im_2x), cv2.COLOR_RGB2BGR)

# In 1x banner, blue text was around line y = 0.8537 * x - 325 for x in [805..945]
# In 2x banner, x2 = x * 2, y2 = y * 2:
# line equation: y2 = 0.8537 * x2 - 650 for x2 in [1610..1890]
b = cv_2x[:, :, 0]
g = cv_2x[:, :, 1]
r = cv_2x[:, :, 2]

mask_2x = np.zeros((h2, w2), dtype=np.uint8)

for x2 in range(1610, 1890):
    y_center = int(0.8537 * x2 - 650)
    for y2 in range(y_center - 36, y_center + 40):
        if 0 <= y2 < h2:
            is_blue = (b[y2, x2] > 110) & (b[y2, x2] > int(r[y2, x2]) + 20)
            is_white = (b[y2, x2] > 175) & (g[y2, x2] > 175) & (r[y2, x2] > 175)
            is_dark = (r[y2, x2] < 75) & (g[y2, x2] < 75) & (b[y2, x2] < 95)
            if is_blue or is_white or is_dark:
                mask_2x[y2, x2] = 255

# Dilate mask slightly
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
mask_2x_dilated = cv2.dilate(mask_2x, kernel, iterations=1)

# Inpaint using Telea
inpainted_2x = cv2.inpaint(cv_2x, mask_2x_dilated, 5, cv2.INPAINT_TELEA)

# Convert back to PIL Image (RGB)
cleaned_banner_2x = Image.fromarray(cv2.cvtColor(inpainted_2x, cv2.COLOR_BGR2RGB))

# 2. Render "क्रेन सर्विस" in Nirmala Bold
font_path = r"C:\Windows\Fonts\Nirmala.ttc"
font_size = 46
font = ImageFont.truetype(font_path, size=font_size, index=1) # Bold

text_string = "क्रेन सर्विस"

# Calculate bounding box
dummy = Image.new("RGBA", (1, 1))
draw_dummy = ImageDraw.Draw(dummy)
bbox = draw_dummy.textbbox((0, 0), text_string, font=font, stroke_width=4)
tw = bbox[2] - bbox[0] + 40
th = bbox[3] - bbox[1] + 40

# Render on transparent RGBA canvas with padding
txt_canvas = Image.new("RGBA", (tw, th), (0, 0, 0, 0))
draw_txt = ImageDraw.Draw(txt_canvas)

# Subtle shadow for authentic commercial metal sign-painted look
draw_txt.text((22, 22), text_string, font=font, fill=(35, 20, 5, 120), stroke_width=4, stroke_fill=(35, 20, 5, 120))
# Crisp white border + vibrant royal blue fill
draw_txt.text((20, 20), text_string, font=font, fill=(18, 76, 215, 255), stroke_width=4, stroke_fill=(255, 255, 255, 255))

# Rotate by -40.5 degrees (clockwise by 40.5 degrees to match the beam angle)
rotated_txt = txt_canvas.rotate(-40.5, expand=True, resample=Image.Resampling.BICUBIC)
rw, rh = rotated_txt.size

# Target center coordinates on the 2x yellow beam:
# In 1x, start was (810, 364), end was (935, 471) -> center was (872, 417)
# In 2x, center is (1744, 834)
paste_x = int(1744 - rw / 2)
paste_y = int(834 - rh / 2)

# Composite using alpha mask
cleaned_banner_2x.paste(rotated_txt, (paste_x, paste_y), rotated_txt)

# Save the updated 2x master banner
cleaned_banner_2x.save(path_2x, quality=98)
print(f"Saved updated 2x banner: {path_2x}")

# Downscale with Lanczos to update 1x master banner
path_1x = r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_exact_master_banner.jpg"
banner_1x = cleaned_banner_2x.resize((1391, 592), Image.Resampling.LANCZOS)
banner_1x.save(path_1x, quality=98)
print(f"Saved updated 1x banner: {path_1x}")

# Save zoomed inspection crop of the crane arm
crop_arm_2x = cleaned_banner_2x.crop((1450, 600, 2000, 1050))
crop_arm_2x.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\final_crane_arm_inspection.png")
print("Saved final_crane_arm_inspection.png for visual verification!")

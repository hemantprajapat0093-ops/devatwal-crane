from PIL import Image
import numpy as np

banner = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_exact_master_banner.jpg")
arr = np.array(banner)
h, w, _ = arr.shape

# The text on the yellow arm is:
# 1. "देवतवाल" in RED (high R, low G, low B)
# 2. followed/below by blue text (high B, high B relative to R and G)
# On a yellow arm (where background is R > 200, G > 140, B < 60)
# Blue text has: B > R + 20 and B > 100
blue_mask = (arr[:, :, 2] > arr[:, :, 0] + 20) & (arr[:, :, 2] > 100) & (arr[:, :, 1] < 180)
# Look in x: 600..1000, y: 200..500
y_idx, x_idx = np.where(blue_mask[:, 600:1000])

if len(y_idx) > 0:
    min_x, max_x = 600 + x_idx.min(), 600 + x_idx.max()
    min_y, max_y = y_idx.min(), y_idx.max()
    print(f"Blue text location in master banner: x={min_x}..{max_x}, y={min_y}..{max_y}")
    
    # Save a crop of the arm around this blue text
    crop_arm = banner.crop((min_x - 50, min_y - 80, max_x + 50, max_y + 50))
    crop_arm.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\real_blue_text_crop.png")
    print("Saved real_blue_text_crop.png!")
else:
    print("No blue text found with criteria")

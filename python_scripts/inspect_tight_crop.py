from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\beam_text_tight_crop.png")
arr = np.array(im)

# Let's inspect:
# Red line: "देवतवाल"
# Blue line: "क्रेन सर्विस"
red_mask = (arr[:, :, 0] > 180) & (arr[:, :, 1] < 70) & (arr[:, :, 2] < 70)
# Blue line on yellow beam (not sky):
blue_mask = (arr[:, :, 2] > 140) & (arr[:, :, 2] > arr[:, :, 0] + 30) & (arr[:, :, 1] < 150) & (arr[:, :, 0] > 10)

yr, xr = np.where(red_mask)
yb, xb = np.where(blue_mask)

mr, cr = np.polyfit(xr, yr, 1)
mb, cb = np.polyfit(xb, yb, 1)

print(f"Tight crop: Devatwal red slope = {mr:.4f}, center = ({np.mean(xr):.1f}, {np.mean(yr):.1f})")
print(f"Tight crop: Crane Service blue slope = {mb:.4f}, center = ({np.mean(xb):.1f}, {np.mean(yb):.1f})")
print(f"Distance between text center lines: {cb - cr:.1f} pixels")

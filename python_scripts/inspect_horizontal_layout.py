from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\beam_horizontal.png")
arr = np.array(im)
w, h = im.size
print("Horizontal beam size:", w, h)

# Find red text "देवतवाल"
red_mask = (arr[:, :, 0] > 180) & (arr[:, :, 1] < 70) & (arr[:, :, 2] < 70)
yr, xr = np.where(red_mask)
print(f"Red text 'देवतवाल': x={xr.min()}..{xr.max()}, y={yr.min()}..{yr.max()}")

# Find blue text
blue_mask = (arr[:, :, 2] > 130) & (arr[:, :, 2] > arr[:, :, 0] + 30) & (arr[:, :, 1] < 160)
yb, xb = np.where(blue_mask)
print(f"Blue text: x={xb.min()}..{xb.max()}, y={yb.min()}..{yb.max()}")

# Save a crop of both texts together in horizontal orientation
im.crop((xr.min() - 20, min(yr.min(), yb.min()) - 10, max(xr.max(), xb.max()) + 20, max(yr.max(), yb.max()) + 10)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\both_texts_horizontal.png")
print("Saved both_texts_horizontal.png!")

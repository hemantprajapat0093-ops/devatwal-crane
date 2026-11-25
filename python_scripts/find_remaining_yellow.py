from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\verify_clean_text_area.jpg")
arr = np.array(im)
yellow_mask = (arr[:, :, 0] > 180) & (arr[:, :, 1] > 140) & (arr[:, :, 2] < 90)
y_idx, x_idx = np.where(yellow_mask)
print(f"X range: {x_idx.min()} to {x_idx.max()}, Y range: {150+y_idx.min()} to {150+y_idx.max()}")

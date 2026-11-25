from PIL import Image
import numpy as np

im_arm = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\orig_unblurred_arm.jpg")
# The crop was (650, 400, 950, 680)
# Let's find yellow metal pixels (R > 180, G > 130, B < 70)
arr = np.array(im_arm)
yellow = (arr[:, :, 0] > 180) & (arr[:, :, 1] > 130) & (arr[:, :, 2] < 70)
y_idx, x_idx = np.where(yellow)
if len(x_idx) > 0:
    print(f"Yellow metal in arm crop: x from {650+x_idx.min()} to {650+x_idx.max()}, y from {400+y_idx.min()} to {400+y_idx.max()}")

im_boom = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\orig_unblurred_boom.jpg")
# The crop was (850, 200, 1300, 450)
arr_b = np.array(im_boom)
yellow_b = (arr_b[:, :, 0] > 180) & (arr_b[:, :, 1] > 130) & (arr_b[:, :, 2] < 70)
yb_idx, xb_idx = np.where(yellow_b)
if len(xb_idx) > 0:
    print(f"Yellow metal in boom crop: x from {850+xb_idx.min()} to {850+xb_idx.max()}, y from {200+yb_idx.min()} to {200+yb_idx.max()}")

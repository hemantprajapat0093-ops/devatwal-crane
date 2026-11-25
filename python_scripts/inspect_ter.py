from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\crop_ter.jpg")
arr = np.array(im)
print("crop_ter shape:", arr.shape)
# Find yellow pixels in crop_ter
# crop_ter is x=650..850, y=250..420
yellow = (arr[:, :, 0] > 180) & (arr[:, :, 1] > 130) & (arr[:, :, 2] < 100)
y_idx, x_idx = np.where(yellow)
if len(x_idx) > 0:
    print(f"Yellow in crop_ter: x from {650+x_idx.min()} to {650+x_idx.max()}, y from {250+y_idx.min()} to {250+y_idx.max()}")
else:
    print("No yellow in crop_ter")

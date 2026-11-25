from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\clean_beam_text_area.png")
arr = np.array(im)
h, w, _ = arr.shape

# Let's check rows:
for y in range(0, h, 10):
    red_count = np.sum((arr[y, :, 0] > 180) & (arr[y, :, 1] < 70) & (arr[y, :, 2] < 70))
    blue_count = np.sum((arr[y, :, 2] > 120) & (arr[y, :, 2] > arr[y, :, 0] + 30) & (arr[y, :, 1] < 160))
    yellow_count = np.sum((arr[y, :, 0] > 190) & (arr[y, :, 1] > 130) & (arr[y, :, 2] < 60))
    print(f"y={y:3d}: red_pixels={red_count:3d}, blue_pixels={blue_count:3d}, yellow_pixels={yellow_count:3d}")

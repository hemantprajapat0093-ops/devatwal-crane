from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\crop_720_870.jpg")
print("Size:", im.size)
# In this crop, x=0 corresponds to x=720, y=0 corresponds to y=260.
# Where is the yellow?
arr = np.array(im)
# Let's save a visualization where non-yellow is darkened:
vis = arr.copy()
yellow = (vis[:, :, 0] > 180) & (vis[:, :, 1] > 140) & (vis[:, :, 2] < 90)
vis[~yellow] = vis[~yellow] // 3
Image.fromarray(vis).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\crop_720_yellow_only.jpg")
print("Saved crop_720_yellow_only.jpg")

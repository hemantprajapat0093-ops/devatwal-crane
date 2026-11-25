from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\exact_crane_crop.jpg")
arr = np.array(im)
print("exact_crane_crop:", arr.shape)
# Does exact_crane_crop have text?
# Let's check for yellow text in exact_crane_crop:
mask = (arr[:, :, 0] > 180) & (arr[:, :, 1] > 130) & (arr[:, :, 2] < 100)
print("Yellow pixels count in exact_crane_crop:", np.sum(mask))

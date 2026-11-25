from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\exact_crane_crop.jpg")
arr = np.array(im)
# exact_crane_crop was cropped from exact_reference_hero:
# let's see its x, y in exact_reference_hero:
# In test_crop.py: right_crane = im.crop((450, 140, w, h)) -> size: (1419-450, 689-140) = (969, 549)
# wait, exact_crane_crop is (899, 539)!
# Where was exact_crane_crop cropped from?
# Let's find out!

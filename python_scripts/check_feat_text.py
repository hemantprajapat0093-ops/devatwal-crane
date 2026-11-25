from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_crane_featured_large.jpg")
print("Dimensions:", im.size)
# What text is on hero_crane_featured_large?
im.crop((0, 0, 500, 200)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\feat_top_left.jpg")
im.crop((500, 0, 1000, 200)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\feat_top_mid.jpg")
print("Saved feat crops")

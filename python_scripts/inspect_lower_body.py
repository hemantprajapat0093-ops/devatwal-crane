from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\crane_lower_body.jpg")
print("crane_lower_body size:", im.size)
# The crop is from x=500 to 800 (width 300), y=350 to 689 (height 339)
# Let's see: Where is the yellow crane cabin and tires?
arr = np.array(im)
# Yellow metal of crane:
yellow = (arr[:, :, 0] > 180) & (arr[:, :, 1] > 130) & (arr[:, :, 2] < 70)
y_idx, x_idx = np.where(yellow)
if len(x_idx) > 0:
    print(f"Yellow crane metal in lower body: x from {500+x_idx.min()} to {500+x_idx.max()}")

from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_exact_master_banner.jpg")
w, h = im.size
arr = np.array(im)

# "Get a Quote" button has a border around y: 508..556, x: 330..550
# Let's inspect the border pixels (bright white/grey outline)
# Outline: R > 150, G > 150, B > 150
mask_border = (arr[500:565, 335:550, 0] > 140) & (arr[500:565, 335:550, 1] > 140) & (arr[500:565, 335:550, 2] > 140)
y_indices, x_indices = np.where(mask_border)

if len(y_indices) > 0:
    min_y, max_y = 500 + y_indices.min(), 500 + y_indices.max()
    min_x, max_x = 335 + x_indices.min(), 335 + x_indices.max()
    print(f"'Get a Quote' button: x={min_x}..{max_x} ({min_x/w*100:.1f}%..{max_x/w*100:.1f}%), y={min_y}..{max_y} ({min_y/h*100:.1f}%..{max_y/h*100:.1f}%)")

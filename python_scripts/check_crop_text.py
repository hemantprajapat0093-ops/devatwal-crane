from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\debug_text_gofuter.jpg")
arr = np.array(im)
# crop was from x=400 to 850, y=200 to 400
# Let's find any yellow or bright text pixels
# Yellow in Go Futer: R > 200, G > 150, B < 80
print("Finding yellow letters in debug_text_gofuter.jpg...")
mask = (arr[:, :, 0] > 180) & (arr[:, :, 1] > 130) & (arr[:, :, 2] < 100)
y_indices, x_indices = np.where(mask)
if len(x_indices) > 0:
    min_x, max_x = x_indices.min(), x_indices.max()
    min_y, max_y = y_indices.min(), y_indices.max()
    print(f"Yellow text in crop: x from {min_x} ({400+min_x}) to {max_x} ({400+max_x}), y from {min_y} ({200+min_y}) to {max_y} ({200+max_y})")

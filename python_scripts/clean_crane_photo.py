from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\user_crane_exact.jpg")
w, h = im.size
arr = np.array(im).copy()

# 1. Clean the top-left pill snippet "...t Rating" (x: 0 to 65, y: 35 to 115)
# In this region, replace with the surrounding sky
for y in range(35, 115):
    for x in range(0, 65):
        # Sample sky from (y, x + 70)
        arr[y, x] = arr[y, min(w - 1, x + 70)]

# 2. Clean the middle-left yellow snippet "...r." (x: 0 to 45, y: 370 to 495)
# In this region, sample sky/sunset from (y, x + 50)
for y in range(370, 495):
    for x in range(0, 48):
        arr[y, x] = arr[y, min(w - 1, x + 50)]

# 3. Clean the lower-left white snippet "...le" (x: 0 to 30, y: 565 to 603)
# In this region, sample ground/tire from (y, x + 35)
for y in range(565, h):
    for x in range(0, 35):
        arr[y, x] = arr[y, min(w - 1, x + 35)]

clean_im = Image.fromarray(arr)
clean_im.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\user_crane_clean.jpg", quality=98)
print("Saved user_crane_clean.jpg with zero residual snippets!")

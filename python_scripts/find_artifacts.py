from PIL import Image
import numpy as np

src = Image.open(r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.user_uploaded\uploaded_media_0_1795627290194.jpg")
w, h = src.size

# Let's inspect the entire left strip of src (x from 0 to 120)
strip = src.crop((0, 0, 120, h))
strip.save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\src_left_strip.png")

# Let's inspect where text/artifacts actually are in the left 100 pixels
arr = np.array(src)
print("Image dimensions:", w, h)

# Let's print out rows where x < 80 has white or yellow pixels
for y in range(0, h, 10):
    row_left = arr[y, :80]
    # check white
    has_white = np.any((row_left[:, 0] > 180) & (row_left[:, 1] > 180) & (row_left[:, 2] > 180))
    # check yellow
    has_yellow = np.any((row_left[:, 0] > 200) & (row_left[:, 1] > 150) & (row_left[:, 2] < 80))
    if has_white or has_yellow:
        print(f"y={y}: has_white={has_white}, has_yellow={has_yellow}")

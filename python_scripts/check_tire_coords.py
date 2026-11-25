from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\user_crop_clean.jpg")
w, h = im.size
print("user_crop_clean size:", w, h)

# Let's inspect where the crane machinery begins on the left edge of user_crop_clean
# Where is rear tire 7?
# Let's find the black rubber tire on the left edge:
arr = np.array(im)

# Look at x from 0 to 100, y from 400 to 600
# The rear tire is around y: 400 to 550, x: 0 to 80
for y in range(400, 560, 20):
    for x in range(0, 100, 10):
        print(f"y={y}, x={x}: RGB={arr[y, x]}")

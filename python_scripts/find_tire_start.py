from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\user_crane_exact.jpg")
arr = np.array(im)
h, w, _ = arr.shape

# Let's inspect where the rear tire and yellow fender start
# Tire is black (low values), fender is bright yellow (R > 180, G > 130, B < 70)
for x in range(0, 150, 10):
    yellow_in_col = np.sum((arr[:, x, 0] > 180) & (arr[:, x, 1] > 130) & (arr[:, x, 2] < 70))
    print(f"Col x={x}: yellow pixels={yellow_in_col}")

import cv2
import numpy as np

patch = cv2.imread(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\test_beam_inpainted.png")
# Check if any blue text remains
b = patch[:, :, 0]
g = patch[:, :, 1]
r = patch[:, :, 2]

blue_remaining = np.sum((b > 110) & (b > r.astype(np.int32) + 20))
print("Blue pixels remaining in inpainted beam:", blue_remaining)

# Check mean color in the inpainted center:
print("Center patch color (BGR):", np.mean(patch[60:100, 60:120], axis=(0,1)))

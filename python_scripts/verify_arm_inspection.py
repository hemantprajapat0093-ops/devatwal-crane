from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\final_crane_arm_inspection.png")
w, h = im.size
print("Inspection image size:", w, h)

# Check presence of red pixels ("देवतवाल")
arr = np.array(im)
red_count = np.sum((arr[:, :, 0] > 180) & (arr[:, :, 1] < 70) & (arr[:, :, 2] < 70))
print("Red pixels (देवतवाल):", red_count)

# Check presence of royal blue pixels ("क्रेन सर्विस")
# B > 140, B > R + 30
blue_count = np.sum((arr[:, :, 2] > 140) & (arr[:, :, 2] > arr[:, :, 0] + 30) & (arr[:, :, 1] < 150))
print("Royal blue pixels (क्रेन सर्विस):", blue_count)

# Check presence of white outline pixels
white_count = np.sum((arr[:, :, 0] > 220) & (arr[:, :, 1] > 220) & (arr[:, :, 2] > 220))
print("White outline pixels:", white_count)

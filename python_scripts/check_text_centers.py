from PIL import Image
import numpy as np

im = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\final_crane_arm_inspection.png")
arr = np.array(im)

red_mask = (arr[:, :, 0] > 180) & (arr[:, :, 1] < 70) & (arr[:, :, 2] < 70)
yr, xr = np.where(red_mask)

blue_mask = (arr[:, :, 2] > 140) & (arr[:, :, 2] > arr[:, :, 0] + 30) & (arr[:, :, 1] < 150)
yb, xb = np.where(blue_mask)

print(f"Red text (देवतवाल) center: x={np.mean(xr):.1f}, y={np.mean(yr):.1f}, span x={xr.min()}..{xr.max()}, y={yr.min()}..{yr.max()}")
print(f"Blue text (क्रेन सर्विस) center: x={np.mean(xb):.1f}, y={np.mean(yb):.1f}, span x={xb.min()}..{xb.max()}, y={yb.min()}..{yb.max()}")

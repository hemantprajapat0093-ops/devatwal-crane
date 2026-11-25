from PIL import Image
import numpy as np
import math

banner = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_exact_master_banner.jpg")
arr = np.array(banner)

# Let's find the angle of the red text "देवतवाल"
# The red text starts at some (x, y) and ends at some (x, y)
red_mask = (arr[300:460, 750:920, 0] > 180) & (arr[300:460, 750:920, 1] < 70) & (arr[300:460, 750:920, 2] < 70)
y_r, x_r = np.where(red_mask)

# Absolute coords
abs_x = 750 + x_r
abs_y = 300 + y_r

# Perform linear regression to find slope: y = m * x + c
m, c = np.polyfit(abs_x, abs_y, 1)
angle_rad = math.atan(m)
angle_deg = math.degrees(angle_rad)

print(f"Red text 'देवतवाल' fit: slope m = {m:.4f}")
print(f"Angle in degrees: {angle_deg:.2f}°")
print(f"Start of Devatwal: ({abs_x.min()}, {int(m * abs_x.min() + c)})")
print(f"End of Devatwal: ({abs_x.max()}, {int(m * abs_x.max() + c)})")

# Let's also check the blue text points
blue_mask = (arr[360:500, 800:960, 2] > 130) & (arr[360:500, 800:960, 2] > arr[360:500, 800:960, 0] + 30) & (arr[360:500, 800:960, 1] < 160)
y_b, x_b = np.where(blue_mask)
abs_xb = 800 + x_b
abs_yb = 360 + y_b

if len(abs_xb) > 10:
    mb, cb = np.polyfit(abs_xb, abs_yb, 1)
    print(f"Blue text fit: slope m = {mb:.4f}, angle = {math.degrees(math.atan(mb)):.2f}°")
    print(f"Start of Blue text: ({abs_xb.min()}, {int(mb * abs_xb.min() + cb)})")
    print(f"End of Blue text: ({abs_xb.max()}, {int(mb * abs_xb.max() + cb)})")

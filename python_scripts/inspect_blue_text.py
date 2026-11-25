from PIL import Image
import numpy as np

arm = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\arm_devatwal_area.png")
w, h = arm.size
arr = np.array(arm)

print("Arm crop size:", w, h)
# In arm_devatwal_area.png:
# crop was taken from (x1=711, y1=291, x2=1011, y2=521)
# Let's find blue pixels in this crop:
# Blue pixels on yellow background:
# R < 100, G < 140, B > 120 and B > R + 40
blue_mask = (arr[:, :, 2] > 120) & (arr[:, :, 2] > arr[:, :, 0] + 40) & (arr[:, :, 1] < 150)
y_b, x_b = np.where(blue_mask)

if len(y_b) > 0:
    min_x, max_x = x_b.min(), x_b.max()
    min_y, max_y = y_b.min(), y_b.max()
    print(f"Blue text in crop: x={min_x}..{max_x}, y={min_y}..{max_y}")
    print(f"Absolute banner coords: x={711 + min_x}..{711 + max_x}, y={291 + min_y}..{291 + max_y}")
    
    # Let's crop just the blue text with a little padding
    arm.crop((min_x - 10, min_y - 10, max_x + 10, max_y + 10)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\blue_text_only.png")
    print("Saved blue_text_only.png!")

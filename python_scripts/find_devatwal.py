from PIL import Image
import numpy as np

banner = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\hero_exact_master_banner.jpg")
arr = np.array(banner)

# Let's find "देवतवाल" in red:
# Red on yellow arm: R > 180, G < 80, B < 80
# Yellow arm around it: R > 200, G > 120, B < 50
# Let's look for red pixels:
red_pixels = (arr[:, :, 0] > 180) & (arr[:, :, 1] < 70) & (arr[:, :, 2] < 70)
# Look in crane area: x: 600..950, y: 200..500
y_r, x_r = np.where(red_pixels[200:500, 600:950])

if len(y_r) > 0:
    for idx in range(0, len(y_r), 50):
        print(f"Red pixel at x={600 + x_r[idx]}, y={200 + y_r[idx]}")
    
    devatwal_x = 600 + int(np.mean(x_r))
    devatwal_y = 200 + int(np.mean(y_r))
    print(f"Devatwal center approximately at x={devatwal_x}, y={devatwal_y}")

    # Crop 300x300 around this point:
    banner.crop((devatwal_x - 120, devatwal_y - 80, devatwal_x + 180, devatwal_y + 150)).save(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\arm_devatwal_area.png")
    print("Saved arm_devatwal_area.png!")

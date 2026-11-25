from PIL import Image
import numpy as np

# Let's inspect rotated (+40.5°) vs rotated_neg (-40.5°)
# In which image is the red text horizontal?
for name in ["beam_horizontal.png", "beam_horizontal_neg.png"]:
    im = Image.open(rf"C:\Users\heman\Desktop\devatwal-crane-service\public\images\{name}")
    arr = np.array(im)
    red_mask = (arr[:, :, 0] > 180) & (arr[:, :, 1] < 70) & (arr[:, :, 2] < 70)
    yr, xr = np.where(red_mask)
    if len(xr) > 10:
        m, _ = np.polyfit(xr, yr, 1)
        print(f"{name}: red text slope = {m:.4f}")

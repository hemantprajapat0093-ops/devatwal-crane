from PIL import Image
import numpy as np

# In exact_reference_hero.jpg, where is the crane body?
# Let's inspect x=550, 600, 650, 700
for x in [550, 600, 650, 700]:
    im = Image.open(rf"C:\Users\heman\Desktop\devatwal-crane-service\public\images\crane_start_{x}.jpg")
    arr = np.array(im)
    print(f"x={x}: min={arr.min()}, max={arr.max()}, mean={arr.mean():.1f}")

import os
from PIL import Image

# Let's inspect exact_crane_crop.jpg
crane_crop = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\exact_crane_crop.jpg")
print("exact_crane_crop.jpg size:", crane_crop.size)

# Let's see what is inside exact_reference_hero.jpg
ref = Image.open(r"C:\Users\heman\Desktop\devatwal-crane-service\public\images\exact_reference_hero.jpg")
print("exact_reference_hero.jpg size:", ref.size)
